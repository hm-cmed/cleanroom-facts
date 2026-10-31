"""出典表に PMID・PMCID・ライセンス表示の列がない成果物を取り込んだあと、出典マスターの空欄を、
同じ成果物のカードの provenance から機械的に写す（値は作り手が書いたもの。推測では埋めない）。

使い方: python scripts/fill_sources_from_cards.py RC,BL 2461 2550    # 接頭辞、SRC の範囲
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def main(prefixes: str, lo: int, hi: int) -> None:
    by: dict[str, dict] = {}
    for pf in prefixes.split(","):
        for c in yaml.safe_load((ROOT / "data/facts" / f"{pf}.yaml").read_text(encoding="utf-8")):
            by.setdefault(c["provenance"]["source_ref"], c["provenance"])
    p = ROOT / "data/sources/sources.yaml"
    S = yaml.safe_load(p.read_text(encoding="utf-8"))
    n = 0
    for s in S:
        num = int(s["id"].split("-")[1])
        pv = by.get(s["id"])
        if not pv or not lo <= num <= hi:
            continue
        ch = []
        for src, dst in (("pmid", "pmid"), ("pmcid", "pmcid"), ("source_license", "license_note")):
            if not s.get(dst) and pv.get(src):
                s[dst] = str(pv[src]); ch.append(dst)
        if ch:
            n += 1
            s.setdefault("history", []).append({"date": dt.date.today().isoformat(), "by": "claude-code",
                "change": f"出典表に列がなかったため、同じ成果物のカード（provenance）から {'・'.join(ch)} を写した（機械的な補完）"})
    p.write_text(yaml.safe_dump(S, allow_unicode=True, sort_keys=False, width=10000), encoding="utf-8")
    print(f"補完した出典 {n} 件")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
