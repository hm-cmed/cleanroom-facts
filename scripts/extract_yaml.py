"""Phase 1: raw/*.md の YAML ブロックを取り込み、スキーマ形式の事実票に正規化する。

使い方（リポジトリ直下で）:
    .\\.venv\\Scripts\\python.exe scripts\\extract_yaml.py

主張文（assertion.plain_statement_ja）と数値は一切書き換えない。
行う変換は CLAUDE.md 2-3 の規則と、識別子の空値・未確認値の null 化だけ。
"""
from __future__ import annotations

import datetime as dt
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
FACTS = ROOT / "data" / "facts"
SOURCES = ROOT / "data" / "sources"
REPORTS = ROOT / "reports"
SCHEMA = ROOT / "schema" / "fact.schema.json"

TODAY = dt.date.today().isoformat()
BY = "claude-code"

PILOT = "00_pilot_hp_ug.md"
ES_V1 = "01a_esophagus_v1.md"
ES_V2 = "01b_esophagus_v2.md"

CITE_RE = re.compile(r"\\\[(\d+)\\\]")
ID_LINE_RE = re.compile(r"^\s*- id:\s*(\S+)")
SECTION_RE = re.compile(r"^#\s*=+\s*\d+\.\s*(.+?)\s*=+\s*$")

# CLAUDE.md 2-3：第1回 食道（basis_tag はライセンスの意味）
ES_BASIS_MAP = {
    "A": ("B", "OPEN"),
    "B": ("B", "RESTRICTED"),
    "C": ("B", "GOV_JP"),
    "D": ("B", "GOV_US"),
    "E": ("B", "UNKNOWN"),
    "保留": ("B", "UNKNOWN"),
}

# SRC表の「資料」欄から取った照合キーワード（識別子で照合できなかった場合だけ使う）
SRC_KEYWORDS = {
    "SRC-001": ["JCOG1109"],
    "SRC-002": ["CheckMate 577"],
    "SRC-003": ["CheckMate 648"],
    "SRC-004": ["Sun JM", "Lancet 2021;398"],
    "SRC-005": ["Metges", "ESMO Open 2025"],
    "SRC-006": ["Ishihara R", "JGES食道ESD/EMR"],
    "SRC-007": ["Baveno VII"],
    "SRC-008": ["Gralnek"],
    "SRC-009": ["Birk M", "ESGE異物GL"],
    "SRC-010": ["Lyon consensus 2.0", "Lyon 2.0"],
    "SRC-011": ["Chicago Classification v4.0", "Chicago v4.0"],
    "SRC-012": ["Brooks PJ"],
    "SRC-013": ["Lewis SJ"],
    "SRC-014": ["国立がん研究センター"],
    "SRC-015": ["K653-6"],
    "SRC-016": ["小野薬品"],
    "SRC-017": ["門脈圧亢進症取扱い規約"],
    "SRC-018": ["Yoshiji"],
    "SRC-019": ["Verhoeven"],
    "SRC-020": ["Contini"],
    "SRC-021": ["Cheng HT"],
    "SRC-022": ["Boerhaave Syndrome", "Diagnostics 2025"],
    "SRC-023": ["IDCases 2020"],
    "SRC-024": ["Medicine 2019"],
    "SRC-025": ["Werner YB"],
    "SRC-026": ["Dupilumab"],
    "SRC-027": ["Villanueva"],
}

CARD_KEY_ORDER = ["id", "domain", "subdomain", "assertion", "provenance", "uncertainty",
                  "curriculum", "publication_info", "history"]
PROV_KEY_ORDER = ["source_ref", "source", "doi", "pmid", "pmcid", "url", "source_license",
                  "legal_basis", "source_class", "corroboration"]


# ---------------------------------------------------------------- 読み込み

def yaml_blocks(text: str) -> list[str]:
    return re.findall(r"^```yaml\n(.*?)^```", text, re.S | re.M)


def split_markers(line: str) -> tuple[str, list[str], list[str]]:
    """脚注マーカー \\[n\\] を処理する。

    文字列の外にあるマーカーは除去する。二重引用符の文字列の中にあるマーカーは、
    主張文を勝手に変えないよう Markdown のエスケープだけ外して [n] として残す。
    戻り値は (処理後の行, 除去した番号, 文字列内に残した番号)。
    """
    out, removed, kept = [], [], []
    pos, in_str = 0, False
    for m in CITE_RE.finditer(line):
        seg = line[pos:m.start()]
        in_str ^= (len(re.findall(r'(?<!\\)"', seg)) % 2 == 1)
        out.append(seg)
        if in_str:
            out.append(f"[{m.group(1)}]")
            kept.append(m.group(1))
        else:
            removed.append(m.group(1))
        pos = m.end()
    out.append(line[pos:])
    return "".join(out), removed, kept


def scan_block(block: str) -> tuple[dict, dict, dict]:
    """カードごとに、除去した脚注番号・文字列内に残した番号・v1 の節見出し（subdomain）を集める。"""
    cites: dict[str, list[str]] = defaultdict(list)
    inline: dict[str, list[str]] = defaultdict(list)
    sections: dict[str, str] = {}
    current_id, current_section = None, None
    for line in block.split("\n"):
        m = SECTION_RE.match(line)
        if m:
            current_section = m.group(1)
            continue
        m = ID_LINE_RE.match(line)
        if m:
            current_id = m.group(1)
            if current_section:
                sections[current_id] = current_section
        if current_id:
            _, removed, kept = split_markers(line)
            cites[current_id] += removed
            inline[current_id] += kept
    return cites, inline, sections


def prepare_block(block: str) -> str:
    """脚注マーカーを処理し、定義（_pub 等）とカード列が同居するブロックを1つのマッピングにまとめる。"""
    lines = [split_markers(l)[0] for l in block.split("\n")]
    if not any(re.match(r"^_\w+:", l) for l in lines):
        return "\n".join(lines)
    out, in_list = [], False
    for l in lines:
        if not in_list and l.startswith("- "):
            out.append("_cards:")
            in_list = True
        out.append(("  " + l) if in_list and l.strip() else l)
    return "\n".join(out)


def load_raw(name: str) -> tuple[list[dict], dict, dict, dict]:
    text = (RAW / name).read_text(encoding="utf-8")
    cards, cites, inline, sections = [], {}, {}, {}
    for block in yaml_blocks(text):
        c, i, s = scan_block(block)
        cites.update(c)
        inline.update({k: v for k, v in i.items() if v})
        sections.update(s)
        data = yaml.safe_load(prepare_block(block))  # safe_load はアンカーと << を展開する
        if isinstance(data, dict):
            data = data.get("_cards", [])
        cards += [d for d in data if isinstance(d, dict) and not str(d.get("id", "")).startswith("_")]
    return cards, cites, inline, sections


# ---------------------------------------------------------------- SRC表

def parse_src_table(text: str) -> list[dict]:
    rows = []
    for line in text.split("\n"):
        m = re.match(r"^\|\s*(SRC-(\d+))\s*\|(.*)\|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in CITE_RE.sub("", m.group(3)).split("|")]
        title, citation, license_note, basis = (cells + [""] * 4)[:4]
        new_id = f"SRC-{int(m.group(2)):03d}"
        doi = re.search(r"10\.\d{4,9}/[^\s,;，、）)]+", citation)
        pmid = re.search(r"PMID\s*(\d+)", citation)
        pmcid = re.search(r"PMC\d+", citation)
        legal, cls = ES_BASIS_MAP.get(basis, (None, None))
        rows.append({
            "id": new_id,
            "legacy_id": m.group(1),
            "title": title,
            "citation": citation,
            "doi": doi.group(0) if doi else None,
            "pmid": pmid.group(1) if pmid else None,
            "pmcid": pmcid.group(0) if pmcid else None,
            "license_note": license_note,
            "legacy_basis_tag": basis,
            "legal_basis": legal,
            "source_class": cls,
            "history": [{"date": TODAY, "by": BY,
                         "change": f"取り込み：raw/{ES_V2} の SRC表 {m.group(1)} から（IDを3桁に正規化、basis_tag {basis} を CLAUDE.md 2-3 第1回規則で変換）"}],
        })
    return rows


# ---------------------------------------------------------------- 正規化

def norm_identifier(value, label: str, notes: list[str]):
    """空・「要確認」・記憶由来の候補は null にする（CLAUDE.md 1-3）。"""
    if value is None:
        return None
    s = str(value).strip()
    if s == "":
        return None
    if "可能性" in s:
        notes.append(f"{label}は未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除）")
        return None
    if "要確認" in s or "未確認" in s:
        notes.append(f"{label}は原本で「{s}」のためnull")
        return None
    return s


def pilot_source_class(lic: str) -> tuple[str, str]:
    """パイロット版：source_license の記載から source_class を判定する。戻り値は (区分, 判定理由)。"""
    lic = lic or ""
    restrictive = [k for k in ("NC", "ND", "No commercial", "©", "Wiley", "非CC") if k in lic]
    if restrictive:
        return "RESTRICTED", f"制限的な記載（{'・'.join(restrictive)}）を含む"
    if "未確認" in lic or "要確認" in lic:
        return "UNKNOWN", "未確認・要確認の記載を含む"
    if re.search(r"CC BY(?![-‐])|CC0", lic):
        return "OPEN", "CC BY / CC0 のみ"
    if "政府" in lic:
        return "GOV_JP", "政府資料"
    return "UNKNOWN", "判定できる記載なし"


def normalize(card: dict, origin: str, cites: dict, inline: dict, sections: dict) -> tuple[dict, list[str]]:
    flags: list[str] = []
    cid = card["id"]
    m = re.match(r"^([A-Z]{2})-", cid)
    domain = m.group(1) if m else None
    history = [{"date": TODAY, "by": BY, "change": f"取り込み：raw/{origin} から"}]
    if cites.get(cid):
        refs = "".join(f"[{n}]" for n in cites[cid])
        history.append({"date": TODAY, "by": BY,
                        "change": f"原本の文字列外の脚注マーカー {refs} を除去（YAMLとして読めないため。文字列の値は不変）"})
    if inline.get(cid):
        refs = "".join(f"[{n}]" for n in inline[cid])
        history.append({"date": TODAY, "by": BY,
                        "change": f"文字列内の脚注マーカー {refs} は Markdown のエスケープ（\\）だけ外して保持。削除するかは proposals/01_inline_citation_markers.md で提案中"})
        flags.append(f"文字列内に脚注マーカー {refs} が残っている（proposals/01_inline_citation_markers.md）")

    src = dict(card.get("provenance") or {})
    notes: list[str] = []
    prov = {"source_ref": None, "source": src.get("source")}
    for key, label in (("doi", "DOI"), ("pmid", "PMID"), ("pmcid", "PMCID")):
        prov[key] = norm_identifier(src.get(key), label, notes)
    prov["url"] = (src.get("url") or None)
    prov["source_license"] = src.get("source_license")

    basis = src.get("basis_tag")
    basis_s = "" if basis is None else str(basis)
    if origin == PILOT:
        cls, why = pilot_source_class(prov["source_license"])
        prov["legal_basis"], prov["source_class"] = basis_s, cls
        history.append({"date": TODAY, "by": BY,
                        "change": f"basis_tag {basis_s} を legal_basis に移行。source_class={cls}（source_license「{prov['source_license']}」：{why}。CLAUDE.md 2-3 パイロット規則）"})
        if "／" in (prov["source_license"] or "") or "引用元" in (prov["source_license"] or ""):
            flags.append("source_license が複合記載（原典と引用元が混在）。source_class の判定を人間が確認")
    else:
        if basis_s not in ES_BASIS_MAP:
            flags.append(f"basis_tag「{basis_s}」は変換規則にない")
            prov["legal_basis"], prov["source_class"] = None, None
        else:
            prov["legal_basis"], prov["source_class"] = ES_BASIS_MAP[basis_s]
            history.append({"date": TODAY, "by": BY,
                            "change": f"basis_tag {basis_s} → legal_basis {prov['legal_basis']}／source_class {prov['source_class']}（CLAUDE.md 2-3 第1回規則）"})
    if src.get("corroboration") is not None:
        prov["corroboration"] = src["corroboration"]
    for key in src:
        if key not in PROV_KEY_ORDER and key != "basis_tag":
            flags.append(f"provenance の未知の項目「{key}」を除外")

    if notes:
        history.append({"date": TODAY, "by": BY, "change": "識別子を null 化：" + "／".join(notes)})

    unc = card.get("uncertainty")
    if notes:
        add = "［取り込み時］" + "／".join(notes)
        if unc is None:
            unc = add
        elif isinstance(unc, str):
            unc = f"{unc}｜{add}"
        else:
            flags.append("uncertainty が文字列でないため、識別子 null 化の理由を追記できなかった")

    pub_src = dict(card.get("publication_info") or {})
    created = pub_src.get("created")
    pub = {
        "created": created.isoformat() if isinstance(created, (dt.date, dt.datetime)) else (str(created) if created is not None else None),
        "verifier": None,  # CLAUDE.md 1-4：Claude Code は値を入れない（原本は空文字）
        "verified_at": pub_src.get("verified_at") or None,
        "status": pub_src.get("status"),
        "superseded_by": pub_src.get("superseded_by") or None,
    }
    if pub_src.get("verifier"):
        flags.append(f"原本に verifier「{pub_src['verifier']}」があったが、Claude Code は設定できないため null にした")
    if basis_s == "保留" and pub["status"] != "draft":
        history.append({"date": TODAY, "by": BY, "change": f"basis_tag 保留のため status {pub['status']} → draft（CLAUDE.md 2-3）"})
        pub["status"] = "draft"
    if pub["status"] == "verified_sources":
        flags.append("原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施")
    if pub["status"] == "verified_expert":
        flags.append("原本で status: verified_expert。人間による設定か確認が必要")

    cur = card.get("curriculum") or {}
    curriculum = {"core_curriculum": cur.get("core_curriculum"), "kokushi": cur.get("kokushi")}

    for key in card:
        if key not in CARD_KEY_ORDER:
            flags.append(f"未知の項目「{key}」を除外")

    out = {
        "id": cid,
        "domain": domain,
        "subdomain": card.get("subdomain") or sections.get(cid),
        "assertion": card["assertion"],
        "provenance": {k: prov[k] for k in PROV_KEY_ORDER if k in prov},
        "uncertainty": unc,
        "curriculum": curriculum,
        "publication_info": pub,
        "history": history,
    }
    return out, flags


# ---------------------------------------------------------------- SRC の照合

def match_src(card: dict, srcs: list[dict]) -> tuple[str | None, str, list[str]]:
    p = card["provenance"]
    id_hits = []
    for key in ("doi", "pmid", "pmcid"):
        v = p.get(key)
        if not v:
            continue
        for s in srcs:
            if s.get(key) and s[key].lower() == str(v).lower() and s["id"] not in [h for h, _ in id_hits]:
                id_hits.append((s["id"], key))
    text = p.get("source") or ""
    name_hits = [sid for sid, kws in SRC_KEYWORDS.items() if any(k in text for k in kws)]
    if id_hits:
        primary = id_hits[0][0]
        method = "identifier(" + ",".join(f"{sid}:{k}" for sid, k in id_hits) + ")"
        others = [h for h, _ in id_hits[1:]] + [n for n in name_hits if n not in [h for h, _ in id_hits]]
        return primary, method, others
    if len(name_hits) == 1:
        return name_hits[0], "keyword", []
    if len(name_hits) > 1:
        return None, "ambiguous", name_hits
    return None, "none", []


# ---------------------------------------------------------------- 出力

def dump_yaml(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=10_000, default_flow_style=False)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    loaded = {name: load_raw(name) for name in (PILOT, ES_V1, ES_V2)}
    srcs = parse_src_table((RAW / ES_V2).read_text(encoding="utf-8"))
    dump_yaml(SOURCES / "sources.yaml", srcs)

    outputs: dict[str, list[dict]] = {"HP.yaml": [], "UG.yaml": [], "_staging_ES_v1.yaml": [], "_staging_ES_v2.yaml": []}
    flags: dict[str, list[str]] = defaultdict(list)
    src_matches = []
    raw_counts = {}

    for origin, (cards, cites, inline, sections) in loaded.items():
        raw_counts[origin] = len(cards)
        for card in cards:
            norm, f = normalize(card, origin, cites, inline, sections)
            flags[norm["id"]] += f
            if origin == PILOT:
                outputs[f"{norm['domain']}.yaml"].append(norm)
            else:
                ref, method, others = match_src(norm, srcs)
                if ref:
                    norm["provenance"]["source_ref"] = ref
                    norm["history"].append({"date": TODAY, "by": BY,
                                            "change": f"source_ref={ref} を付与（照合方法：{method}）"})
                src_matches.append((origin, norm["id"], ref, method, others, norm["provenance"]["source"]))
                outputs["_staging_ES_v1.yaml" if origin == ES_V1 else "_staging_ES_v2.yaml"].append(norm)

    if (FACTS / "ES.yaml").exists():
        # 統合済み（Phase 2）。staging を作り直すと ES.yaml と二重になるため出力しない
        for fname in ("_staging_ES_v1.yaml", "_staging_ES_v2.yaml"):
            outputs.pop(fname)
        print("ES.yaml があるため、食道の staging は出力しない")

    violations: dict[str, list[tuple[str, str]]] = {}
    for fname, cards in outputs.items():
        dump_yaml(FACTS / fname, cards)
        violations[fname] = []
        for c in cards:
            for e in sorted(validator.iter_errors(c), key=lambda e: list(e.path)):
                loc = "/".join(str(p) for p in e.path) or "(root)"
                violations[fname].append((c["id"], f"{loc}: {e.message}"))

    write_inline_marker_proposal(outputs, {cid: refs for _, (_, _, inl, _) in loaded.items() for cid, refs in inl.items()})

    # 書き出したファイルが読めることを確認
    reread = {fname: len(yaml.safe_load((FACTS / fname).read_text(encoding="utf-8"))) for fname in outputs}

    write_report(raw_counts, outputs, reread, srcs, src_matches, flags, violations)
    print(f"done: {', '.join(f'{k}={len(v)}' for k, v in outputs.items())}, sources={len(srcs)}")
    for fname, v in violations.items():
        print(f"  schema violations {fname}: {len(v)}")


def verbatim_check(outputs) -> tuple[int, list[str]]:
    """主張文が原本に一字一句そのまま含まれているか（取り込みで主張文を変えていないこと）を確認する。"""
    origin_of = {"HP.yaml": PILOT, "UG.yaml": PILOT, "_staging_ES_v1.yaml": ES_V1, "_staging_ES_v2.yaml": ES_V2}
    n, bad = 0, []
    for fname, cards in outputs.items():
        raw = (RAW / origin_of[fname]).read_text(encoding="utf-8").replace("\\[", "[").replace("\\]", "]")
        for c in cards:
            n += 1
            if f'"{c["assertion"]["plain_statement_ja"]}"' not in raw:
                bad.append(c["id"])
    return n, bad


def write_inline_marker_proposal(outputs, inline) -> None:
    path = ROOT / "proposals" / "01_inline_citation_markers.md"
    if not inline:
        return
    L = [f"# 提案：文字列内に残った脚注マーカーの削除（{TODAY}、claude-code）\n",
         "原本では、次のカードの文字列の**内側**に調査レポートの脚注マーカー（`\\[n\\]`）が入っていた。",
         "CLAUDE.md 1-2 により Claude Code は主張文を書き換えられないため、取り込みでは Markdown のエスケープだけ外して `[n]` のまま保持した。",
         "マーカーは出典の脚注番号で、文意の一部ではないと考えられるため、削除を提案する。\n",
         "**承認方法**：各行の「承認」欄に `可` または `否` を記入してください。承認された行だけを、Claude Code が history に記録して反映します。\n",
         "| ID | 項目 | 現在の値 | 提案後の値 | 承認 |", "|---|---|---|---|---|"]
    for cards in outputs.values():
        for c in cards:
            if c["id"] not in inline:
                continue
            for field, val in [("plain_statement_ja", c["assertion"].get("plain_statement_ja"))] + \
                              [(k, v) for k, v in c["assertion"].items() if k != "plain_statement_ja"]:
                if isinstance(val, str) and re.search(r"\[\d+\]", val):
                    after = re.sub(r"(\[\d+\])+", "", val)
                    L.append(f"| {c['id']} | assertion.{field} | {val} | {after} | |")
    path.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")


def write_report(raw_counts, outputs, reread, srcs, src_matches, flags, violations) -> None:
    L = []
    L.append(f"# Phase 1：取り込みレポート（{TODAY}）\n")
    L.append("生成：`scripts/extract_yaml.py`。主張文と数値は変更していない。\n")

    L.append("## 0. 処理上の注意\n")
    L.append("- 原本の YAML には調査レポートの脚注マーカー（`\\[n\\]`）が混在しており、そのままでは YAML として読めない。文字列の外にあるマーカーは除去し、カードごとに番号を `history` に記録した。")
    L.append("- 文字列の内側にあったマーカー（2件）は、主張文を変えないよう `[n]` として残し、削除を `proposals/01_inline_citation_markers.md` で提案した。")
    L.append("- v1 は定義（`_pub`・`_cur`・`_src`）とカード列が同じブロックにあり、YAML として不正だったため、カード列を `_cards:` の下に入れて読み込んだ（アンカーと `<<:` は PyYAML で展開）。")
    L.append("- v1 の節見出し（`# ===== 1. GERD・NERD・Barrett食道 =====` など）を `subdomain` に入れた。パイロット版と v2 は `null`。")
    L.append("- `verifier` は原本ではすべて空文字だったため `null` にした。`created` は原本の値（2026-10-10）を保持した。")
    stm = verbatim_check(outputs)
    L.append(f"- **主張文の同一性チェック**：出力した {stm[0]} 件の `plain_statement_ja` が、原本の中に一字一句そのまま存在するかを照合した（`\\[`→`[` のみ許容）。不一致 {len(stm[1])} 件{('：' + ', '.join(stm[1])) if stm[1] else ''}。\n")

    L.append("## 1. 件数\n")
    L.append("| 原本 | 抽出したカード数 |\n|---|---|")
    for k, v in raw_counts.items():
        L.append(f"| raw/{k} | {v} |")
    L.append("\n| 出力 | 件数 | 再読込 |\n|---|---|---|")
    for k, v in outputs.items():
        L.append(f"| data/facts/{k} | {len(v)} | {reread[k]} |")
    L.append(f"| data/sources/sources.yaml | {len(srcs)} | — |\n")

    L.append("## 2. タグの変換\n")
    conv = Counter()
    for fname, cards in outputs.items():
        for c in cards:
            p = c["provenance"]
            conv[(fname, p["legal_basis"], p["source_class"])] += 1
    L.append("| 出力 | legal_basis | source_class | 件数 |\n|---|---|---|---|")
    for (f, lb, sc), n in sorted(conv.items(), key=lambda x: (x[0][0], str(x[0][1]), str(x[0][2]))):
        L.append(f"| {f} | {lb} | {sc} | {n} |")

    L.append("\n### 2-1. パイロット版の source_class 判定（source_license の記載別）\n")
    L.append("判定規則：NC・ND・No commercial・©・Wiley・非CC のいずれかを含む → RESTRICTED。それ以外で「未確認」「要確認」を含む → UNKNOWN。CC BY／CC0 のみ → OPEN。\n")
    L.append("| source_license | source_class | 件数 | 該当ID |\n|---|---|---|---|")
    by_lic = defaultdict(list)
    for fname in ("HP.yaml", "UG.yaml"):
        for c in outputs[fname]:
            by_lic[(c["provenance"]["source_license"], c["provenance"]["source_class"])].append(c["id"])
    for (lic, sc), ids in sorted(by_lic.items(), key=lambda x: (x[0][1], str(x[0][0]))):
        L.append(f"| {lic} | {sc} | {len(ids)} | {', '.join(ids)} |")

    L.append("\n## 3. 出典マスター（SRC）と source_ref\n")
    L.append("SRC表の ID は `SRC-01` 形式だったため、スキーマの `^SRC-[0-9]{3}$` に合わせて `SRC-001` 形式に正規化した（`legacy_id` に旧IDを保持）。\n")
    m_count = Counter(m[3].split("(")[0] for m in src_matches)
    L.append("| 照合方法 | 件数 |\n|---|---|")
    for k, v in m_count.items():
        L.append(f"| {k} | {v} |")
    L.append("\n- identifier：カードの DOI・PMID・PMCID が SRC表の識別子と一致。\n- keyword：識別子が一致せず、出典名のキーワード（スクリプト内 `SRC_KEYWORDS`）で1件に決まった。**人間の確認を推奨。**\n- none：SRC表に該当がない（v1 の W番号の出典など）。source_ref は null。\n")
    L.append("| 原本 | ID | source_ref | 照合方法 | 他の候補 | source |\n|---|---|---|---|---|---|")
    for origin, cid, ref, method, others, source in src_matches:
        L.append(f"| {origin[:3]} | {cid} | {ref or '—'} | {method} | {', '.join(others) or '—'} | {(source or '').replace('|', '／')[:70]} |")
    used = {m[2] for m in src_matches if m[2]}
    unused = [s["id"] for s in srcs if s["id"] not in used]
    L.append(f"\nどのカードからも参照されなかった SRC：{', '.join(unused) or 'なし'}\n")

    L.append("## 4. 識別子の null 化\n")
    L.append("| ID | 内容 |\n|---|---|")
    for fname, cards in outputs.items():
        for c in cards:
            for h in c["history"]:
                if h["change"].startswith("識別子を null 化"):
                    L.append(f"| {c['id']} | {h['change'].removeprefix('識別子を null 化：')} |")

    L.append("\n## 5. 人間の確認が必要な項目\n")
    L.append("| ID | 内容 |\n|---|---|")
    for cid, fl in flags.items():
        for f in fl:
            L.append(f"| {cid} | {f} |")
    multi = [(c["id"], c["provenance"]["doi"]) for cards in outputs.values() for c in cards
             if c["provenance"].get("doi") and re.search(r"[;,\s]", c["provenance"]["doi"])]
    for cid, doi in multi:
        L.append(f"| {cid} | doi に複数の値「{doi}」。Phase 3 の照合前に主たる DOI を決める必要がある |")

    L.append("\n## 6. スキーマ違反\n")
    for fname, v in violations.items():
        L.append(f"### {fname}（{len(v)}件）\n")
        if not v:
            L.append("なし\n")
            continue
        summary = Counter(msg.split(": ", 1)[0] + ": " + re.sub(r"'[^']*'", "'…'", msg.split(": ", 1)[1]) for _, msg in v)
        L.append("| 違反の種類 | 件数 |\n|---|---|")
        for k, n in summary.most_common():
            L.append(f"| {k} | {n} |")
        L.append("\n<details><summary>全件</summary>\n")
        for cid, msg in v:
            L.append(f"- {cid}: {msg}")
        L.append("\n</details>\n")

    (REPORTS / "01_ingest.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
