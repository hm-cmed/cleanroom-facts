"""分野をまたぐ項目：既存カードに出題基準の番号を足す（人間が承認したものだけ）。

使い方（リポジトリ直下で）:
    python scripts/add_kokushi.py OT-037 Ⅸ-5-C-①
    python scripts/add_kokushi.py HP-001,HP-002 Ⅻ-2-B-⑧

- 番号の名称・レベルは data/curriculum/kokushi_r6_items.yaml から引き、「医学各論 番号（名称、レベル）」の形で
  curriculum.kokushi に「；」区切りで足す（すでにあれば何もしない）。主張文・数値・出典は変えない。
- history に記録する。カードの版（card_hash）が変わるので、監修済みなら再監修が必要になる。
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def registry() -> dict:
    y = yaml.safe_load((ROOT / "data/curriculum/kokushi_r6_items.yaml").read_text(encoding="utf-8"))
    return {it["code"]: it for ch in y["chapters"] for g in ch["groups"] for it in g["items"]}


def main(ids: str, code: str) -> None:
    it = registry()[code]
    label = f"医学各論 {code}（{it['name']}、{it['level']}）"
    by_file: dict[Path, list] = {}
    for cid in ids.split(","):
        p = ROOT / "data/facts" / f"{cid[:2]}.yaml"
        cards = by_file.setdefault(p, yaml.safe_load(p.read_text(encoding="utf-8")))
        c = next(x for x in cards if x["id"] == cid)
        assert (c.get("publication_info") or {}).get("status") != "retired", f"{cid} は廃止済み"
        cur = c.get("curriculum") or {}
        c["curriculum"] = cur
        old = cur.get("kokushi")
        if code in str(old or ""):
            print(f"{cid}: すでにある"); continue
        cur["kokushi"] = f"{old}；{label}" if old else label
        c.setdefault("history", []).append({"date": dt.date.today().isoformat(), "by": "claude-code", "change":
            f"分野をまたぐ項目：出題基準の番号 {code} を足した（{old or 'なし'} → {cur['kokushi']}）。三原の承認による"})
        print(f"{cid}: {cur['kokushi']}")
    for p, cards in by_file.items():
        p.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10000), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
