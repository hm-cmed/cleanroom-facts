"""自由に使える出典の調査（BL・GR・HF・PV と パブリックドメイン調査バッチ1〜7）の反映（三原の承認 2026-11-11）。

1. 出典マスターの区分の訂正（英語版ガイドライン等 → OPEN、NC 系の明確化 → RESTRICTED）と、参照カードの区分の同期
2. 主出典の置き換え（A）：自由に使える資料を主出典にし、元の主出典は corroboration に残す
3. 裏づけの追加（B）：corroboration に自由に使える資料と裏づける部分を記録
主張文・数値は変えない。PubMed の抄録、DailyMed の添付文書、MedlinePlus 医学百科、転載部分は使わない。
入力：proposals/free_sources_20261108/result.json と、取り込み側で選別した proposals/pd_survey_20261111/selected.json
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
T = "2026-11-11"
OPEN_FIX = {"SRC-018", "SRC-028", "SRC-029", "SRC-030", "SRC-032", "SRC-042", "SRC-048", "SRC-049", "SRC-051", "SRC-052", "SRC-141", "SRC-435"}
REST_FIX = {"SRC-2481": "CC BY-NC 3.0", "SRC-424": "CC BY-NC", "SRC-426": "CC BY-NC", "SRC-039": "CC BY-NC-ND", "SRC-047": "CC BY-NC", "SRC-4212": "CC BY-NC", "SRC-4224": "CC BY-NC-ND"}


def main() -> None:
    sel = json.loads((ROOT / "proposals/pd_survey_20261111/selected.json").read_text(encoding="utf-8"))
    files = {p: yaml.safe_load(p.read_text(encoding="utf-8")) for p in (ROOT / "data/facts").glob("*.yaml")}
    cards = {c["id"]: c for cs in files.values() for c in cs}
    sp = ROOT / "data/sources/sources.yaml"
    S = yaml.safe_load(sp.read_text(encoding="utf-8"))
    SM = {s["id"]: s for s in S}
    log = {"class": [], "A": [], "B": [], "new_src": []}

    def hist(c, msg):
        c.setdefault("history", []).append({"date": T, "by": "claude-code", "change": msg + "。三原の承認（2026-11-11）による"})

    # 1. class fixes
    changed = {}
    for sid in OPEN_FIX:
        s = SM[sid]
        if s.get("source_class") != "OPEN":
            old = s.get("source_class"); s["source_class"] = "OPEN"
            s["license_note"] = f"CC BY 4.0（作り手が Crossref の version-of-record ライセンスと Europe PMC の表示で確認、2026-11-11）。旧記録：{s.get('license_note')}"
            s.setdefault("history", []).append({"date": T, "by": "claude-code", "change": f"source_class を {old} から OPEN に訂正（パブリックドメイン出典の調査。三原の承認）"})
            changed[sid] = "OPEN"; log["class"].append((sid, old, "OPEN"))
    for sid, lic in REST_FIX.items():
        s = SM[sid]
        if s.get("source_class") == "UNKNOWN":
            s["source_class"] = "RESTRICTED"
            s["license_note"] = f"{lic}（作り手が Europe PMC の表示で確認、2026-11-11）。旧記録：{s.get('license_note')}"
            s.setdefault("history", []).append({"date": T, "by": "claude-code", "change": "source_class を UNKNOWN から RESTRICTED に明確化（三原の承認）"})
            changed[sid] = "RESTRICTED"; log["class"].append((sid, "UNKNOWN", "RESTRICTED"))
    for c in cards.values():
        r = c["provenance"].get("source_ref")
        if r in changed and c["provenance"].get("source_class") != changed[r]:
            old = c["provenance"].get("source_class"); c["provenance"]["source_class"] = changed[r]
            if changed[r] == "OPEN":
                c["provenance"]["source_license"] = "CC BY 4.0"
            hist(c, f"出典 {r} の区分の訂正にあわせて provenance.source_class を {old} から {changed[r]} にした")

    # new sources
    nxt = max(int(s["id"][4:]) for s in S) + 1
    reg = {}

    def new_src(key, title, doi, pmid, pmcid, url, cls, lic):
        nonlocal nxt
        if key in reg:
            return reg[key]
        sid = f"SRC-{nxt}"; nxt += 1
        S.append(dict(citation=title, doi=doi or None, history=[{"by": "claude-code", "change": "登録：自由に使える出典の調査（作り手、2026-11-08／11）から。識別子は作り手の API 確認によるもので、取り込み側は --online で照合予定。三原の承認（2026-11-11）", "date": T}],
                      id=sid, legacy_basis_tag=None, legacy_id=None, legal_basis="B", license_note=f"{lic}。ライセンスの根拠：{url}", pmcid=pmcid or None, pmid=pmid or None, source_class=cls, title=title))
        SM[sid] = S[-1]; reg[key] = sid; log["new_src"].append((sid, title[:80]))
        return sid

    # 2. A replacements
    for a in sel["A"]:
        c = cards[a["card"]]; pv = c["provenance"]
        if a.get("src"):
            sid = a["src"]; s = SM[sid]
            title, doi, pmid, pmcid, url, cls, lic = s.get("title") or s.get("citation"), s.get("doi"), s.get("pmid"), s.get("pmcid"), f"https://doi.org/{s.get('doi')}" if s.get("doi") else None, s["source_class"], "CC BY 4.0"
        else:
            cls = a["class"]; title = a["title"]; doi = a.get("doi"); pmid = a.get("pmid"); pmcid = a.get("pmcid"); url = a["url"]
            lic = {"GOV_US": "米国連邦政府の著作物", "GOV_JP": "日本の公的資料（法令・通知・政府標準利用規約）", "OPEN": "CC BY"}[cls]
            sid = new_src(a["title"], title, doi, pmid, pmcid, url, cls, lic)
        oldref, oldsrc = pv.get("source_ref"), pv.get("source")
        prev = pv.get("corroboration")
        pv["corroboration"] = (f"{prev}。" if prev else "") + f"元の主出典：{oldref}（{oldsrc}）"
        pv.update(source_ref=sid, source=title, doi=doi or None, pmid=pmid or None, pmcid=pmcid or None, url=url, source_license=lic, source_class=cls)
        hist(c, f"主出典を {oldref} から自由に使える資料 {sid} に置き換え、元の主出典を corroboration に記録した（作り手の判定 A：{a['why']}）")
        log["A"].append((a["card"], oldref, sid))

    # 3. B corroborations
    for b in sel["B"]:
        c = cards[b["card"]]; pv = c["provenance"]
        prev = pv.get("corroboration")
        pv["corroboration"] = (f"{prev}。" if prev else "") + f"自由に使える資料による裏づけ（{b['label']}）：{b['text']}"
        hist(c, f"corroboration に自由に使える資料による裏づけを追記した（{b['label']}）")
        log["B"].append(b["card"])

    sp.write_text(yaml.safe_dump(S, allow_unicode=True, sort_keys=False, width=10000), encoding="utf-8")
    for p, cs in files.items():
        p.write_text(yaml.safe_dump(cs, allow_unicode=True, sort_keys=False, width=10000), encoding="utf-8")
    (ROOT / "reports/free_sources_apply_20261111.json").write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding="utf-8")
    print({k: len(v) for k, v in log.items()})


if __name__ == "__main__":
    main()
