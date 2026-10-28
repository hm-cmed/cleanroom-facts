"""分野をまたぐ重複カードの統合：後から出てきたカードを、先に出てきたカードに誘導する。

使い方（リポジトリ直下で。人間が統合を承認したものだけに使う）:
    python scripts/merge_cards.py TH-023 BD-001     # 残すカード 廃止するカード

- 残すカード（先に出てきたもの）の curriculum に、廃止するカードの出題基準・コアカリの番号を足す
  （「；」区切り。同じ番号は重ねない）。主張文・数値・出典は変えない。
- 廃止するカードは status: retired、superseded_by に残すカードの ID を入れる（ID は再利用しない）。
- 両方の history に記録する。監修は残すカードで1回だけ行えばよい（両方の章の番号で出題・配分に使われる）。
- 残すカードの curriculum が変わるので版（card_hash）が変わる。監修済みなら再監修が必要になる。
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "data" / "facts"


def split(s: str | None) -> list[str]:
    return [x.strip() for x in re.split(r"[；;]", s or "") if x.strip()]


def key(x: str) -> str:
    m = re.match(r"(医学各論\s*\S+?)（", x) or re.match(r"(\S+)\s*\(id:", x)
    return m.group(1) if m else x


def merged(a: str | None, b: str | None) -> str | None:
    out = split(a)
    have = {key(x) for x in out}
    out += [x for x in split(b) if key(x) not in have]
    return "；".join(out) or None


def load(cid: str):
    p = FACTS / f"{cid[:2]}.yaml"
    cards = yaml.safe_load(p.read_text(encoding="utf-8"))
    return p, cards, next(c for c in cards if c["id"] == cid)


def main(keep_id: str, drop_id: str) -> None:
    today = dt.date.today().isoformat()
    kp, kcards, keep = load(keep_id)
    dp, dcards, drop = (kp, kcards, next(c for c in kcards if c["id"] == drop_id)) if keep_id[:2] == drop_id[:2] else load(drop_id)
    assert drop["publication_info"].get("status") != "retired", f"{drop_id} は廃止済み"
    kc, dc = keep.setdefault("curriculum", {}), drop.get("curriculum") or {}
    before = dict(kc)
    for f in ("kokushi", "core_curriculum"):
        kc[f] = merged(kc.get(f), dc.get(f))
    keep.setdefault("history", []).append({"date": today, "by": "claude-code", "change":
        f"分野をまたぐ重複の統合：{drop_id} の出題基準・コアカリの番号をこのカードに足した（{before.get('kokushi')} → {kc.get('kokushi')}）。"
        f"{drop_id} は廃止してこのカードに誘導（三原の承認による）"})
    drop["publication_info"]["status"] = "retired"
    drop["publication_info"]["superseded_by"] = keep_id
    drop.setdefault("history", []).append({"date": today, "by": "claude-code", "change":
        f"廃止：{keep_id}（先に作成）と実質同じ内容のため、番号を {keep_id} に移して誘導（分野をまたぐ重複の統合、三原の承認による）"})
    for p, cards in {kp: kcards, dp: dcards}.items():
        p.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10000), encoding="utf-8")
    print(f"{drop_id} → {keep_id}：kokushi = {kc.get('kokushi')}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
