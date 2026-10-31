"""Phase 1（第2回以降）：新形式（legal_basis・source_class 済み）の調査レポートを取り込む。

使い方（リポジトリ直下で）:
    .\\.venv\\Scripts\\python.exe scripts\\ingest_round.py raw\\02_gastroduodenal.md GD
    python scripts/ingest_round.py raw/14_rs_supp.md RI,RO,IL,LC,PL --append   # 補完回（既存ファイルの末尾に足す）

- raw の YAML ブロックをそのまま読み込み、スキーマで検証して data/facts/<接頭辞>.yaml に書く。
- 出典マスター表（| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | …）の新規 SRC を data/sources/sources.yaml に追加する。
  既存の SRC 番号は上書きしない（再利用として記録する）。
- 主張文・数値は変更しない。正規化は、日付を文字列にすること、history の付与、空文字の識別子の null 化だけ。
- 第1回の取り込み（scripts/extract_yaml.py）で問題になった形式（脚注マーカー、アンカー、basis_tag、
  仮ID、verifier・verified_* の設定）が残っていないかを検査し、あればレポートに出して書き込みを止める。
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "data" / "facts"
SOURCES = ROOT / "data" / "sources" / "sources.yaml"
REPORTS = ROOT / "reports"
SCHEMA = ROOT / "schema" / "fact.schema.json"
TODAY = dt.date.today().isoformat()
BY = "claude-code"


def h(change: str) -> dict:
    return {"date": TODAY, "by": BY, "change": change}


def parse_src_table(text: str) -> list[dict]:
    rows = []
    header = None
    for line in text.split("\n"):
        if re.match(r"^\|\s*SRC\s*(番号|ID|No\.?)?\s*\|", line):   # 見出しの「SRC番号」なども受け付ける
            header = [c.strip() for c in line.strip("|").split("|")]
            header[0] = "SRC"
            header = ["ライセンス表示" if h == "ライセンス" else h for h in header]
            continue
        m = re.match(r"^\|\s*(SRC-\d{3,4})\s*\|", line)
        if header and m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(dict(zip(header, cells)))
    return rows


def null_if_dash(v):
    """出典表の識別子の欄。空・ダッシュ・「確認できず（null）」のような説明文は null にする（値を推測で埋めない）。"""
    v = (v or "").strip()
    if v in ("", "—", "―", "–", "-", "－", "ー", "null") or re.search(r"null|確認できず|未確認|なし|不明", v):
        return None
    return v


def main(raw_path: str, prefix: str, append: bool = False) -> None:
    raw = ROOT / raw_path
    text = raw.read_text(encoding="utf-8")
    origin = raw.relative_to(ROOT).as_posix()
    blocks = re.findall(r"^```yaml\n(.*?)^```", text, re.S | re.M)
    problems: list[str] = []

    # 形式の検査（第1回で問題になった点）
    joined = "\n".join(blocks)
    if re.search(r"\\\[\d+\\\]|\[\d+\]", joined):
        problems.append("YAML 内に脚注マーカー（[n]）がある")
    if re.search(r"(^|\s)[&*][A-Za-z_]\w*|<<:", joined, re.M):
        problems.append("アンカー・エイリアス・マージキーがある")
    if "basis_tag" in joined:
        problems.append("旧形式の basis_tag がある")

    cards = []
    for b in blocks:
        data = yaml.safe_load(b)
        cards += data if isinstance(data, list) else [data]

    ids = [c.get("id") for c in cards]
    dup = [i for i, n in Counter(ids).items() if n > 1]
    if dup:
        problems.append(f"ID の重複：{dup}")
    # 1つの原本に複数の接頭辞があってよい（例：python scripts/ingest_round.py raw/08_cv_a.md AR,HF,IH）
    prefixes = [x.strip() for x in prefix.split(",") if x.strip()]
    bad_prefix = [i for i in ids if str(i).split("-")[0] not in prefixes]
    if bad_prefix:
        problems.append(f"接頭辞 {prefix} でない ID：{bad_prefix}")
    # 補完回（--append）：既存のファイルの末尾に足す。ID は既存の最大番号の次から連番であること
    last: dict[str, int] = {}
    for pf in prefixes:
        existing = FACTS / f"{pf}.yaml"
        if existing.exists() and not append:
            problems.append(f"{existing.relative_to(ROOT)} が既にある（上書きしない。補完回は --append を付ける）")
        if append:
            old = yaml.safe_load(existing.read_text(encoding="utf-8")) if existing.exists() else []
            old_ids = {c["id"] for c in old}
            last[pf] = max((int(i.split("-")[1]) for i in old_ids), default=0)
            clash = [i for i in ids if i in old_ids]
            if clash:
                problems.append(f"既存の ID と重なる：{clash}")

    for c in cards:
        pub = c.setdefault("publication_info", {})
        if isinstance(pub.get("created"), (dt.date, dt.datetime)):
            pub["created"] = pub["created"].isoformat()
        if pub.get("verifier") or pub.get("verified_at"):
            problems.append(f"{c['id']}: verifier・verified_at に値がある（人間だけが設定する）")
        if pub.get("status") not in ("draft",):
            problems.append(f"{c['id']}: status が {pub.get('status')}（取り込み時は draft を想定）")
        pub.setdefault("superseded_by", None)
        p = c.get("provenance") or {}
        for k in ("doi", "pmid", "pmcid", "url"):
            if isinstance(p.get(k), str) and not p[k].strip():
                p[k] = None
        if p.get("pmid") is not None:
            p["pmid"] = str(p["pmid"])
        hist = c.get("history") or []
        hist.append(h(f"取り込み：{origin} から（新形式。legal_basis・source_class は原本の値）"))
        c["history"] = hist

    validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    violations = [(c.get("id"), "/".join(map(str, e.path)), e.message) for c in cards for e in validator.iter_errors(c)]

    # 出典マスター
    src_rows = parse_src_table(text)
    sources = yaml.safe_load(SOURCES.read_text(encoding="utf-8"))
    known = {s["id"]: s for s in sources}
    added, reused = [], []
    for r in src_rows:
        sid = r["SRC"]
        if sid in known:
            reused.append(sid)
            continue
        doi = null_if_dash(r.get("DOI"))
        pmid = null_if_dash(r.get("PMID"))
        sources.append({
            "id": sid, "legacy_id": None, "title": r.get("出典"), "citation": r.get("出典"),
            "doi": doi, "pmid": pmid, "pmcid": None,
            "license_note": r.get("ライセンス表示"), "legacy_basis_tag": None,
            "legal_basis": "B", "source_class": r.get("source_class"),
            "history": [h(f"取り込み：{origin} の出典マスター表から")],
        })
        added.append(sid)
    refs = Counter(c["provenance"].get("source_ref") for c in cards)
    missing_src = sorted(s for s in refs if s and s not in known and s not in added)
    if missing_src:
        problems.append(f"カードが参照しているが出典マスターにない SRC：{missing_src}")

    write = not problems and not violations
    if write:
        for pf in prefixes:
            part = [c for c in cards if str(c.get("id")).startswith(pf + "-")]
            if part:
                dumped = yaml.safe_dump(part, allow_unicode=True, sort_keys=False, width=10_000)
                path = FACTS / f"{pf}.yaml"
                if append and path.exists():
                    old_text = path.read_text(encoding="utf-8")
                    dumped = old_text + ("" if old_text.endswith("\n") else "\n") + dumped
                path.write_text(dumped, encoding="utf-8", newline="\n")
        SOURCES.write_text(yaml.safe_dump(sources, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")

    # レポート
    by_sd = Counter(c.get("subdomain") for c in cards)
    by_cls = Counter(c["provenance"].get("source_class") for c in cards)
    unc = [c["id"] for c in cards if c.get("uncertainty")]
    gaps, ranges = [], []
    for pf in prefixes:
        nums = sorted(int(str(i).split("-")[1]) for i in ids if str(i).startswith(pf + "-"))
        if nums:
            first = last.get(pf, 0) + 1
            gaps += [f"{pf}-{n:03d}" for n in range(first, nums[-1] + 1) if n not in nums]
            ranges.append(f"{pf}-{first:03d}〜{pf}-{nums[-1]:03d}")
    L = [f"# Phase 1：取り込みレポート（{prefix}、{TODAY}）\n",
         f"生成：`scripts/ingest_round.py {origin} {prefix}`。主張文と数値は変更していない。\n",
         f"- 結果：{'書き込み済み' if write else '**書き込みを中止**（下の問題を解消してから再実行）'}",
         f"- カード：{len(cards)}件（{'、'.join(ranges)}）、欠番：{', '.join(gaps) or 'なし'}",
         f"- スキーマ違反：{len(violations)}件",
         f"- 出典マスター：新規 {len(added)}件（{', '.join(added)}）、既存の再利用 {len(reused)}件（{', '.join(reused)}）",
         f"- uncertainty に記載のあるカード：{len(unc)}件\n",
         "## 形式の検査\n"]
    L += [f"- {p}" for p in problems] or ["問題なし（脚注マーカー・アンカー・basis_tag・仮ID・verifier の設定はない）"]
    if violations:
        L += ["\n## スキーマ違反\n"] + [f"- {a} {b}: {m}" for a, b, m in violations]
    L += ["\n## subdomain 別\n", "| subdomain | 件数 |", "|---|---|"] + [f"| {k} | {v} |" for k, v in by_sd.most_common()]
    L += ["\n## source_class 別（原本の値。Phase 3 で Crossref により確定）\n", "| source_class | 件数 |", "|---|---|"] + [f"| {k} | {v} |" for k, v in by_cls.most_common()]
    L += ["\n## SRC 別の使用件数\n", "| SRC | 件数 |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(refs.items(), key=lambda x: str(x[0]))]
    (REPORTS / f"01_ingest_{prefix.replace(',', '_')}{'_supp' if append else ''}.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(L[:8]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], append="--append" in sys.argv[3:])
