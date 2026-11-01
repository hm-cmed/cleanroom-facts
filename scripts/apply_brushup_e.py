"""ブラッシュアップE（2026-11-01 三原の承認）を反映する。

- 出題基準：作り手の最終リスト（brushup_e_kokushi_final.json）の区分A・Bと、区分Cのうち承認した8件に、
  番号を付記する。名称・レベルは data/curriculum/kokushi_r6_items.yaml から引き直す（表記を表に合わせる）。
- 地域：brushup_e_region_final.json の確度「高」「中」を condition.region に入れる。
  condition が文字列のカードは {対象: 元の文字列, region: …} に、空のカードは {region: …} にする。
主張文・数値・出典は変えない。history に記録する。
"""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
P = ROOT / "proposals/brushup_20261031"
C_OK = {"NG-046", "NG-073", "NG-105", "NG-148", "NG-123", "NG-125", "NG-219", "NG-140"}
TODAY = dt.date.today().isoformat()


def main() -> None:
    reg = {it["code"]: it for ch in yaml.safe_load((ROOT / "data/curriculum/kokushi_r6_items.yaml").read_text(encoding="utf-8"))["chapters"]
           for g in ch["groups"] for it in g["items"]}
    files = {p: yaml.safe_load(p.read_text(encoding="utf-8")) for p in (ROOT / "data/facts").glob("*.yaml")}
    cards = {c["id"]: c for cs in files.values() for c in cs}
    nk = nr = 0
    for e in json.loads((P / "brushup_e_kokushi_final.json").read_text(encoding="utf-8")):
        if not (e["tier"] in ("A", "B") or (e["tier"] == "C" and e["card"] in C_OK)):
            continue
        c = cards[e["card"]]
        assert c["publication_info"].get("status") != "retired", e["card"]
        cur = c.setdefault("curriculum", {}) or {}
        c["curriculum"] = cur
        assert not cur.get("kokushi"), e["card"]
        codes = re.findall(r"[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]+-\d+-[A-Z](?:-[①-⑳㉑-㉟㊱-㊿])?", e["kokushi"])
        assert codes, e
        label = "；".join(f"医学各論 {k}（{reg[k]['name']}、{reg[k]['level']}）" for k in dict.fromkeys(codes))
        cur["kokushi"] = label
        c.setdefault("history", []).append({"date": TODAY, "by": "claude-code", "change":
            f"ブラッシュアップE：出題基準の番号を付記した（なし → {label}。作り手の区分{e['tier']}、名称は項目表に合わせた）。三原の承認による"})
        nk += 1
    for e in json.loads((P / "brushup_e_region_final.json").read_text(encoding="utf-8")):
        if e["confidence"] not in ("高", "中"):
            continue
        a = cards[e["card"]]["assertion"]
        cond = a.get("condition")
        if isinstance(cond, dict):
            assert not cond.get("region"), e["card"]
            cond["region"] = e["region"]; how = ""
        elif isinstance(cond, str) and cond.strip():
            a["condition"] = {"対象": cond, "region": e["region"]}; how = "。文字列だった condition を 対象 に移した"
        else:
            a["condition"] = {"region": e["region"]}; how = "。condition が空だったので新設した"
        cards[e["card"]].setdefault("history", []).append({"date": TODAY, "by": "claude-code", "change":
            f"ブラッシュアップE：condition.region に「{e['region']}」を入れた（作り手の候補、確度{e['confidence']}{how}）。三原の承認による"})
        nr += 1
    for p, cs in files.items():
        p.write_text(yaml.safe_dump(cs, allow_unicode=True, sort_keys=False, width=10000), encoding="utf-8")
    print("kokushi", nk, "region", nr)


if __name__ == "__main__":
    main()
