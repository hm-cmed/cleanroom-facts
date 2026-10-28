"""試行の比較：同じ依頼文から2つの作り手が作った成果物（trial_A.md・trial_B.md）を、客観的な指標で比べる。

使い方（リポジトリ直下で。成果物はレポジトリの外に置いてよい）:
    python scripts/eval_trial.py C:\\trial\\trial_A.md C:\\trial\\trial_B.md --spec docs/tasks/round14_RS_supp.yaml
    python scripts/eval_trial.py ... --online      # DOI・PMID・ライセンスを Crossref・NCBI で照合（PC で実行）

- 成果物はどちらも読むだけで、data/ には書き込まない。
- 結果は reports/trial_eval_<回>.md と、数値の抜き取り確認用の reports/trial_sample_<回>.csv に出す。
- 作り手の名前は扱わない（A・B のまま）。採点の重みは docs/tasks/trial_eval.md。
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import difflib
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingest_round import parse_src_table, null_if_dash  # noqa: E402

FACTS = ROOT / "data" / "facts"
CUR = ROOT / "data" / "curriculum"
SCHEMA = json.loads((ROOT / "schema" / "fact.schema.json").read_text(encoding="utf-8"))
KOKUSHI_RE = re.compile(r"医学各論\s*([ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]+-\d+(?:-[A-Z])?(?:-[①-⑳])?)")
CORE_RE = re.compile(r"\b(TBL-\d{2}-\d{2}-\d{3}|PS-\d{2}-\d{2}-\d{2})\s*\(id:\s*([A-Za-z0-9_\-]+)\)")
OPEN_LIC = re.compile(r"creativecommons\.org/(licenses/by/|publicdomain/zero)", re.I)
RESTRICTED_LIC = re.compile(r"creativecommons\.org/licenses/by-(nc|nd)", re.I)


def load_reference() -> dict:
    items = yaml.safe_load((CUR / "kokushi_r6_items.yaml").read_text(encoding="utf-8"))
    kok = {it["code"] for ch in items["chapters"] for g in ch["groups"] for it in g["items"]}
    core: dict[str, str] = {}
    base = CUR / "core-curriculum" / "2022" / "ja"
    for f in [base / "outcomes" / "layer4.csv", *sorted((base / "tables").glob("TBL*.csv"))]:
        with open(f, encoding="utf-8-sig", newline="") as fh:
            for r in csv.DictReader(fh):
                core[r["index"]] = r["id"]
    existing = []
    for f in FACTS.glob("*.yaml"):
        for c in yaml.safe_load(f.read_text(encoding="utf-8")) or []:
            existing.append((c["id"], c["assertion"]["plain_statement_ja"]))
    sources = yaml.safe_load((ROOT / "data" / "sources" / "sources.yaml").read_text(encoding="utf-8"))
    return {"kokushi": kok, "core": core, "existing": existing,
            "src_ids": {s["id"] for s in sources},
            "src_doi": {str(s["doi"]).lower(): s["id"] for s in sources if s.get("doi")}}


def parse(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"^```ya?ml\n(.*?)^```", text, re.S | re.M)
    out = {"text": text, "blocks": len(blocks), "cards": [], "parse_error": None, "srcs": parse_src_table(text)}
    try:
        for b in blocks:
            d = yaml.safe_load(b)
            out["cards"] += d if isinstance(d, list) else [d]
    except yaml.YAMLError as e:
        out["parse_error"] = str(e).splitlines()[0]
    return out


def pct(n: int, d: int) -> str:
    return f"{n}/{d}（{round(100 * n / d) if d else 0}%）"


def evaluate(label: str, p: dict, spec: dict, ref: dict) -> dict:
    cards = [c for c in p["cards"] if isinstance(c, dict)]
    n = len(cards)
    m: dict = {"label": label, "n": n, "issues": []}
    iss = m["issues"]
    if p["parse_error"]:
        iss.append(f"YAML として読めない：{p['parse_error']}")
    if p["blocks"] != 1:
        iss.append(f"YAML ブロックが {p['blocks']} 個（1個の指定）")
    joined = p["text"]
    yaml_txt = "\n".join(re.findall(r"^```ya?ml\n(.*?)^```", joined, re.S | re.M))
    if re.search(r"\[\d+\]", yaml_txt):
        iss.append("YAML 内に脚注番号がある")
    if re.search(r"(^|\s)[&*][A-Za-z_]\w*|<<:", yaml_txt, re.M):
        iss.append("アンカー・マージキーがある")
    if "basis_tag" in yaml_txt:
        iss.append("basis_tag がある")
    if re.search(r"(Muse|Meta AI|Claude(?! Code)|ChatGPT|Gemini|GPT-\d)", joined):
        iss.append("作り手の名前らしき語がある（盲検化の指定に反する）")

    # 形式・スキーマ
    v = Draft202012Validator(SCHEMA)
    bad_schema = [c.get("id") for c in cards if any(True for _ in v.iter_errors(c))]
    m["schema_ok"] = n - len(bad_schema)
    m["schema_bad"] = bad_schema
    m["status_bad"] = [c.get("id") for c in cards
                       if (c.get("publication_info") or {}).get("status") != "draft"
                       or (c.get("publication_info") or {}).get("verifier")]
    m["paren_bad"] = [c.get("id") for c in cards
                      if re.search(r"（要確認|（未確認|\(要確認", c.get("assertion", {}).get("plain_statement_ja", ""))]

    # ID と SRC 番号
    starts = spec["id_start"]
    ids = [str(c.get("id")) for c in cards]
    m["id_dup"] = [i for i, k in Counter(ids).items() if k > 1]
    id_bad, gaps = [], []
    for pf, st in starts.items():
        nums = sorted(int(i.split("-")[1]) for i in ids if i.startswith(pf + "-") and i.split("-")[1].isdigit())
        id_bad += [f"{pf}-{x:03d}" for x in nums if x < st]
        if nums:
            gaps += [f"{pf}-{x:03d}" for x in range(st, max(nums) + 1) if x not in nums]
    id_bad += [i for i in ids if i.split("-")[0] not in starts]
    m["id_bad"], m["id_gaps"] = id_bad, gaps
    lo, hi = spec["src_range"]
    table_ids = [r["SRC"] for r in p["srcs"]]
    new_src = [s for s in table_ids if s not in ref["src_ids"]]
    m["src_out_of_range"] = [s for s in new_src if not lo <= int(s[4:]) <= hi]
    refs = Counter((c.get("provenance") or {}).get("source_ref") for c in cards)
    m["src_missing"] = sorted(s for s in refs if s and s not in table_ids and s not in ref["src_ids"])
    m["src_unused"] = sorted(s for s in new_src if s not in refs)
    m["src_dup_doi"] = []
    for r in p["srcs"]:
        doi = (null_if_dash(r.get("DOI")) or "").lower()
        if doi and doi in ref["src_doi"] and ref["src_doi"][doi] != r["SRC"]:
            m["src_dup_doi"].append(f"{r['SRC']} は既存の {ref['src_doi'][doi]} と同じ DOI")
    m["n_src"] = len(p["srcs"])
    m["src_doi"] = sum(1 for r in p["srcs"] if null_if_dash(r.get("DOI")))
    m["src_pmid"] = sum(1 for r in p["srcs"] if null_if_dash(r.get("PMID")))
    m["src_class"] = Counter(r.get("source_class") for r in p["srcs"])

    # カリキュラム
    kok_ok = kok_bad = core_ok = 0
    core_bad: list[str] = []
    covered: Counter = Counter()
    for c in cards:
        cur = c.get("curriculum") or {}
        codes = KOKUSHI_RE.findall(cur.get("kokushi") or "")
        if codes and all(x in ref["kokushi"] for x in codes):
            kok_ok += 1
        elif codes:
            kok_bad += 1
        covered.update(codes)
        pairs = CORE_RE.findall(cur.get("core_curriculum") or "")
        wrong = [f"{a}/{b}" for a, b in pairs if ref["core"].get(a) != b]
        if pairs and not wrong:
            core_ok += 1
        core_bad += [f"{c.get('id')}: {w}" for w in wrong]
    m["kok_ok"], m["kok_bad"], m["core_ok"], m["core_bad"] = kok_ok, kok_bad, core_ok, core_bad
    m["targets_hit"] = [t["code"] for t in spec["targets"] if covered[t["code"]]]
    m["targets_miss"] = [f"{t['code']} {t['name']}" for t in spec["targets"] if not covered[t["code"]]]
    stm = " ".join(c.get("assertion", {}).get("plain_statement_ja", "") for c in cards)
    m["topics_hit"] = [t["name"] for t in spec["topics"] if any(k in stm for k in t["keywords"])]
    m["topics_miss"] = [t["name"] for t in spec["topics"] if t["name"] not in m["topics_hit"]]

    # 不確かさの書き方
    unc = [str(c.get("uncertainty") or "") for c in cards]
    m["unc"] = sum(1 for u in unc if u.strip() and u.strip().lower() != "null")
    m["unc_secondary"] = sum("二次資料" in u for u in unc)
    m["unc_table"] = sum("表から読み取り" in u for u in unc)
    m["region"] = sum(1 for c in cards if ((c.get("assertion") or {}).get("condition") or {}).get("region"))

    # 既存カードとの重複（主張文の類似度）
    near = []
    for c in cards:
        s = c.get("assertion", {}).get("plain_statement_ja", "")
        best = max(((difflib.SequenceMatcher(None, s, t).ratio(), i) for i, t in ref["existing"] if i != c.get("id")), default=(0, ""))
        if best[0] >= 0.6:
            near.append(f"{c.get('id')} ≒ {best[1]}（{best[0]:.2f}）")
    m["near_dup"] = near
    m["lengths"] = sorted(len(c.get("assertion", {}).get("plain_statement_ja", "")) for c in cards)
    return m


# ---------- オンライン照合（PC で実行） ----------

def online(label: str, p: dict, cache_note: list[str]) -> dict:
    import ncbi_crossref as nc  # .env の CONTACT_EMAIL・NCBI_API_KEY を使う
    res = {"doi_ok": 0, "doi_ng": [], "title_low": [], "pmid_ok": 0, "pmid_ng": [], "lic_agree": 0,
           "lic_disagree": [], "lic_unknown": 0, "unresolved": []}
    for r in p["srcs"]:
        sid, doi, pmid = r["SRC"], null_if_dash(r.get("DOI")), null_if_dash(r.get("PMID"))
        title_claim = r.get("出典") or ""
        if doi:
            try:
                w = nc.crossref_work(doi)
            except Exception as e:  # noqa: BLE001
                res["unresolved"].append(f"{sid} DOI {doi}: {e}")
                w = None
            if w:
                res["doi_ok"] += 1
                t = (w.get("title") or [""])[0]
                ratio = difflib.SequenceMatcher(None, t.lower(), title_claim.lower()).ratio()
                words = sorted({x for x in re.findall(r"[a-z0-9]+", t.lower()) if len(x) > 3})
                shared = sum(x in title_claim.lower() for x in words) / len(words) if words else 1
                if t and t.lower()[:40] not in title_claim.lower() and ratio < 0.5 and shared < 0.5:
                    res["title_low"].append(f"{sid}: Crossref「{t[:60]}」")
                lic = " ".join(x.get("URL", "") for x in w.get("license") or [])
                cls = r.get("source_class")
                if not lic:
                    res["lic_unknown"] += 1
                elif OPEN_LIC.search(lic) and not RESTRICTED_LIC.search(lic):
                    (res.__setitem__("lic_agree", res["lic_agree"] + 1) if cls == "OPEN"
                     else res["lic_disagree"].append(f"{sid}: Crossref は {lic}、原本は {cls}"))
                else:
                    (res.__setitem__("lic_agree", res["lic_agree"] + 1) if cls in ("RESTRICTED", "UNKNOWN")
                     else res["lic_disagree"].append(f"{sid}: Crossref は {lic}、原本は {cls}"))
            elif w is None and not any(sid in u for u in res["unresolved"]):
                res["doi_ng"].append(f"{sid}: {doi}")
        if pmid:
            try:
                s = nc.esummary(str(pmid))
            except Exception as e:  # noqa: BLE001
                res["unresolved"].append(f"{sid} PMID {pmid}: {e}")
                continue
            if s and s.get("title"):
                res["pmid_ok"] += 1
                if doi and re.match(r"10\.\d{4,9}/", doi) and doi.lower() not in json.dumps(s).lower():
                    res["pmid_ng"].append(f"{sid}: PMID {pmid} の DOI が原本の DOI と違う")
            else:
                res["pmid_ng"].append(f"{sid}: PMID {pmid} が見つからない")
    return res


def row(name: str, a, b) -> str:
    return f"| {name} | {a} | {b} |"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--online", action="store_true")
    ap.add_argument("--sample", type=int, default=8)
    args = ap.parse_args()
    spec = yaml.safe_load(Path(args.spec).read_text(encoding="utf-8"))
    ref = load_reference()
    P = {"A": parse(Path(args.a)), "B": parse(Path(args.b))}
    M = {k: evaluate(k, P[k], spec, ref) for k in P}
    O = {k: online(k, P[k], []) for k in P} if args.online else {}
    A, B = M["A"], M["B"]
    nt = len(spec["targets"])
    L = [f"# 試行の比較：第{spec['round']}回（{dt.date.today().isoformat()}）", "",
         f"`scripts/eval_trial.py`{' --online' if args.online else ''} の出力。作り手は伏せたまま（A・B）。採点は `docs/tasks/trial_eval.md` の表で行う。", "",
         "## 1. 客観指標", "", "| 指標 | A | B |", "|---|---|---|",
         row("カード数（目安 {}〜{}）".format(*spec["target_cards"]), A["n"], B["n"]),
         row("形式の問題（脚注・アンカー・ブロック数・作り手名など）", len(A["issues"]), len(B["issues"])),
         row("スキーマに合うカード", pct(A["schema_ok"], A["n"]), pct(B["schema_ok"], B["n"])),
         row("status・verifier の指定違反", len(A["status_bad"]), len(B["status_bad"])),
         row("主張文の括弧書き（要確認など）", len(A["paren_bad"]), len(B["paren_bad"])),
         row("ID の指定違反・重複・欠番", f"{len(A['id_bad'])}・{len(A['id_dup'])}・{len(A['id_gaps'])}",
             f"{len(B['id_bad'])}・{len(B['id_dup'])}・{len(B['id_gaps'])}"),
         row("SRC の範囲外・表にない参照・未使用", f"{len(A['src_out_of_range'])}・{len(A['src_missing'])}・{len(A['src_unused'])}",
             f"{len(B['src_out_of_range'])}・{len(B['src_missing'])}・{len(B['src_unused'])}"),
         row("既存 SRC と同じ文献を新番号で登録", len(A["src_dup_doi"]), len(B["src_dup_doi"])),
         row("出典数（DOI あり／PMID あり）", f"{A['n_src']}（{A['src_doi']}／{A['src_pmid']}）", f"{B['n_src']}（{B['src_doi']}／{B['src_pmid']}）"),
         row("source_class の内訳", dict(A["src_class"]), dict(B["src_class"])),
         row(f"対象小項目のカバー（{nt}項目）", pct(len(A["targets_hit"]), nt), pct(len(B["targets_hit"]), nt)),
         row(f"テーマのカバー（{len(spec['topics'])}件）", pct(len(A["topics_hit"]), len(spec["topics"])), pct(len(B["topics_hit"]), len(spec["topics"]))),
         row("出題基準の番号が正しいカード（誤り）", f"{pct(A['kok_ok'], A['n'])}（{A['kok_bad']}）", f"{pct(B['kok_ok'], B['n'])}（{B['kok_bad']}）"),
         row("コアカリの番号と id が正しいカード（誤り）", f"{pct(A['core_ok'], A['n'])}（{len(A['core_bad'])}）", f"{pct(B['core_ok'], B['n'])}（{len(B['core_bad'])}）"),
         row("uncertainty の記載", pct(A["unc"], A["n"]), pct(B["unc"], B["n"])),
         row("「二次資料経由」「表から読み取り」の明記", f"{A['unc_secondary']}・{A['unc_table']}", f"{B['unc_secondary']}・{B['unc_table']}"),
         row("condition.region の記載", pct(A["region"], A["n"]), pct(B["region"], B["n"])),
         row("既存カードと類似（0.6以上）", len(A["near_dup"]), len(B["near_dup"])),
         row("主張文の長さ（中央値・最大）",
             f"{A['lengths'][len(A['lengths'])//2] if A['lengths'] else '-'}・{max(A['lengths'], default='-')}",
             f"{B['lengths'][len(B['lengths'])//2] if B['lengths'] else '-'}・{max(B['lengths'], default='-')}"),
         ]
    if O:
        oa, ob = O["A"], O["B"]
        L += [row("DOI が Crossref で実在（不明）", f"{oa['doi_ok']}（{len(oa['doi_ng'])}）", f"{ob['doi_ok']}（{len(ob['doi_ng'])}）"),
              row("DOI の題名が原本と食い違う", len(oa["title_low"]), len(ob["title_low"])),
              row("PMID が実在し DOI と一致（問題）", f"{oa['pmid_ok']}（{len(oa['pmid_ng'])}）", f"{ob['pmid_ok']}（{len(ob['pmid_ng'])}）"),
              row("ライセンス判定が Crossref と一致（食い違い・欄なし）",
                  f"{oa['lic_agree']}（{len(oa['lic_disagree'])}・{oa['lic_unknown']}）",
                  f"{ob['lic_agree']}（{len(ob['lic_disagree'])}・{ob['lic_unknown']}）"),
              row("照合できなかったもの（unresolved）", len(oa["unresolved"]), len(ob["unresolved"]))]
    else:
        L += ["", "DOI・PMID・ライセンスの照合は、PC で `--online` を付けて実行すると表に加わる。"]
    L += ["", "## 2. 詳細", ""]
    for k in ("A", "B"):
        x = M[k]
        L += [f"### {k}", ""]
        for name, val in [("形式の問題", x["issues"]), ("スキーマ違反", x["schema_bad"]), ("status・verifier の違反", x["status_bad"]),
                          ("括弧書き", x["paren_bad"]), ("ID の指定違反", x["id_bad"]), ("ID の重複", x["id_dup"]), ("欠番", x["id_gaps"]),
                          ("SRC 範囲外", x["src_out_of_range"]), ("表にない SRC", x["src_missing"]), ("未使用の SRC", x["src_unused"]),
                          ("既存と同じ文献", x["src_dup_doi"]), ("カードがない対象小項目", x["targets_miss"]),
                          ("扱っていないテーマ", x["topics_miss"]), ("コアカリの誤り", x["core_bad"]), ("既存カードと類似", x["near_dup"])]:
            if val:
                L.append(f"- {name}：" + "、".join(map(str, val)))
        if O:
            for name, val in [("DOI が見つからない", O[k]["doi_ng"]), ("題名の食い違い", O[k]["title_low"]),
                              ("PMID の問題", O[k]["pmid_ng"]), ("ライセンスの食い違い", O[k]["lic_disagree"]),
                              ("unresolved", O[k]["unresolved"])]:
                if val:
                    L.append(f"- {name}：" + "、".join(val))
        L.append("")
    L += ["## 3. 数値の抜き取り確認", "",
          f"各成果物から {args.sample} 枚ずつ無作為に選び、`reports/trial_sample_{spec['round']}.csv` に出した。"
          "出典（抄録・本文）と照らして「一致／不一致／確認できず」を記入する。どちらの成果物かは列 `set` だけで示す。", ""]
    out = ROOT / "reports" / f"trial_eval_{spec['round']}.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")

    rnd = random.Random(spec["round"])
    sample_path = ROOT / "reports" / f"trial_sample_{spec['round']}.csv"
    if sample_path.exists():   # 判定を書き込んだ抜き取り表を上書きしない（作り直すときは消してから実行）
        print(f"{out.relative_to(ROOT)} を作りました（{sample_path.name} は既にあるので残した）")
        return
    with open(sample_path, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["set", "id", "主張文", "source_ref", "出典", "DOI", "PMID", "判定（一致／不一致／確認できず）", "メモ"])
        for k in ("A", "B"):
            srcs = {r["SRC"]: r for r in P[k]["srcs"]}
            cards = [c for c in P[k]["cards"] if isinstance(c, dict)]
            for c in rnd.sample(cards, min(args.sample, len(cards))):
                sr = (c.get("provenance") or {}).get("source_ref")
                s = srcs.get(sr, {})
                w.writerow([k, c.get("id"), c.get("assertion", {}).get("plain_statement_ja"), sr,
                            s.get("出典", ""), s.get("DOI", ""), s.get("PMID", ""), "", ""])
    print(f"{out.relative_to(ROOT)} を作りました")


if __name__ == "__main__":
    main()
