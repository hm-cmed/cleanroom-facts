"""分野をまたぐ重複カードの候補を探す（統合は人間が決め、scripts/merge_cards.py で行う）。

使い方: python scripts/find_cross_domain.py   → reports/cross_domain_candidates.md

候補の条件（有効なカードだけ、接頭辞が違う組）:
- 同じ出典（source_ref）で、主張文の類似度が 0.6 以上、または
- 同じ subdomain（小項目名など）で、主張文の類似度が 0.6 以上
先に作られた（ID の回が早い）ほうを「残す案」とする。データは変えない。
"""
from __future__ import annotations

import difflib
import itertools
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ORDER = [l.split("prefix:")[1].split(",")[0].strip() for l in (ROOT / "data/domains.yaml").read_text(encoding="utf-8").splitlines() if "prefix:" in l]


def main() -> None:
    cards = []
    for p in sorted((ROOT / "data/facts").glob("*.yaml")):
        for c in yaml.safe_load(p.read_text(encoding="utf-8")) or []:
            if (c.get("publication_info") or {}).get("status") != "retired":
                cards.append(c)
    groups: dict[tuple, list] = defaultdict(list)
    for c in cards:
        groups[("src", (c.get("provenance") or {}).get("source_ref"))].append(c)
        sd = re.sub(r"\s", "", str(c.get("subdomain") or ""))
        if sd:
            groups[("sub", sd)].append(c)
    seen, rows = set(), []
    for (_, _), g in groups.items():
        for a, b in itertools.combinations(g, 2):
            if a["id"][:2] == b["id"][:2] or (a["id"], b["id"]) in seen:
                continue
            seen.add((a["id"], b["id"])); seen.add((b["id"], a["id"]))
            sa, sb = a["assertion"]["plain_statement_ja"], b["assertion"]["plain_statement_ja"]
            r = difflib.SequenceMatcher(None, sa, sb).ratio()
            if r >= 0.6:
                if ORDER.index(b["id"][:2]) < ORDER.index(a["id"][:2]):
                    a, b = b, a
                rows.append((r, a, b))
    rows.sort(key=lambda x: -x[0])
    L = ["# 分野をまたぐ重複カードの候補", "",
         "`python scripts/find_cross_domain.py` で作成。統合するかは三原が決め、承認した組だけ `python scripts/merge_cards.py <残す> <廃止>` で統合する。",
         "統合すると、残すカードに両方の出題基準・コアカリの番号が付き、廃止するカードは残すカードに誘導される（監修は1回）。",
         "内容の側面が違う（例：内分泌の側と運動器の側）なら統合しない。", "",
         f"候補 {len(rows)} 組", "",
         "| 類似度 | 残す案 | 廃止案 | 同じ出典 | 残す案の出題基準 | 廃止案の出題基準 | 残す案の主張文（冒頭） | 廃止案の主張文（冒頭） |", "|---|---|---|---|---|---|---|---|"]
    for r, a, b in rows:
        same = "○" if a["provenance"].get("source_ref") == b["provenance"].get("source_ref") else ""
        k = lambda c: (c.get("curriculum") or {}).get("kokushi") or "－"
        s = lambda c: c["assertion"]["plain_statement_ja"][:60].replace("|", "｜") + "…"
        L.append(f"| {r:.2f} | {a['id']} | {b['id']} | {same} | {k(a)} | {k(b)} | {s(a)} | {s(b)} |")
    out = ROOT / "reports" / "cross_domain_candidates.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"候補 {len(rows)} 組 → {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
