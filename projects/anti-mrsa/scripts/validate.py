# -*- coding: utf-8 -*-
"""事実票・出典台帳・ギャップ一覧の検証と、カバレッジ報告の生成。

使い方: python scripts/validate.py            # 検証のみ（エラーがあれば終了コード1）
        python scripts/validate.py --report   # 検証＋ reports/coverage.md を更新
"""
import sys, json, pathlib, collections
import yaml
from jsonschema import Draft202012Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]
COURSES = {"C1": "開始判断・薬剤選択", "C2": "VCM初期投与・TDM", "C3": "選択と投与設計の統合",
           "C4": "専門医の選択哲学", "C5": "再評価・デエスカレーション"}
LABELS = {"guideline_recommendation": "【ガイドラインに基づく推奨】", "regulatory_information": "【規制・添付文書情報】",
          "peer_reviewed_evidence": "【研究結果に基づく知見】", "expert_survey_tendency": "【専門医アンケートから得られた判断傾向】",
          "local_rule": "【施設固有の判断】", "educational_simplification": "【教育上の単純化】", "unresolved": "【根拠不十分・未解決】"}


def load(p):
    return yaml.safe_load(open(p, encoding="utf-8"))


def main():
    errors = []
    card_v = Draft202012Validator(json.load(open(ROOT / "schemas/evidence_card.schema.json", encoding="utf-8")))
    src_v = Draft202012Validator(json.load(open(ROOT / "schemas/source_registry.schema.json", encoding="utf-8")))
    gap_v = Draft202012Validator(json.load(open(ROOT / "schemas/gap_item.schema.json", encoding="utf-8")))

    sources = {}
    for s in load(ROOT / "sources/registry.yaml")["sources"]:
        for e in src_v.iter_errors(s):
            errors.append(f"registry {s.get('source_id')}: {e.message}")
        if s["source_id"] in sources:
            errors.append(f"registry: duplicate {s['source_id']}")
        sources[s["source_id"]] = s

    cards = []
    for f in sorted((ROOT / "facts").glob("*.yaml")):
        for c in (load(f) or {}).get("cards", []):
            c["_file"] = f.name
            body = {k: v for k, v in c.items() if not k.startswith("_")}
            for e in card_v.iter_errors(body):
                errors.append(f"{f.name} {c.get('fact_id')}: {e.message}")
            sid = c["source"]["source_id"]
            if sid not in sources:
                errors.append(f"{f.name} {c['fact_id']}: unknown source_id {sid}")
            elif sources[sid]["usage_tier"] in ("D", "E"):
                errors.append(f"{f.name} {c['fact_id']}: tier {sources[sid]['usage_tier']} の出典は事実票の根拠にできません ({sid})")
            cards.append(c)
    ids = collections.Counter(c["fact_id"] for c in cards)
    errors += [f"duplicate fact_id {k}" for k, n in ids.items() if n > 1]

    gaps = load(ROOT / "gaps/expert_input_items.yaml")["gaps"]
    for g in gaps:
        for e in gap_v.iter_errors(g):
            errors.append(f"gap {g.get('gap_id')}: {e.message}")
        for sid in g.get("cc_sources_checked", []):
            if sid not in sources:
                errors.append(f"gap {g['gap_id']}: unknown source_id {sid}")

    if errors:
        print("NG")
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: sources={len(sources)} cards={len(cards)} gaps={len(gaps)}")

    if "--report" in sys.argv:
        write_report(sources, cards, gaps)


def write_report(sources, cards, gaps):
    L = ["# カバレッジ報告", "", "`python scripts/validate.py --report` で自動生成。手で編集しない。", ""]
    L += ["## 出典の利用区分", "", "| 区分 | 意味 | 出典数 |", "|---|---|---|"]
    tiers = {"A": "商用・改変可（CC BY等）", "B": "改変可・継承義務（CC BY-SA）", "C": "非営利のみ（BY-NC, BY-NC-SA）",
             "D": "改変禁止（ND）：照合用のみ", "E": "権利留保・許諾待ち：事実票の根拠にしない"}
    tc = collections.Counter(s["usage_tier"] for s in sources.values())
    for t, m in tiers.items():
        L.append(f"| {t} | {m} | {tc.get(t, 0)} |")
    L += ["", "## コース別の事実票数", "", "| コース | 事実票 | うち非営利限定（区分C） | 未解決ギャップ |", "|---|---|---|---|"]
    for cid, name in COURSES.items():
        cs = [c for c in cards if cid in c.get("courses", [])]
        nc = [c for c in cs if sources[c["source"]["source_id"]]["usage_tier"] == "C"]
        gs = [g for g in gaps if cid in g["course"] and g["status"] in ("open", "in_review")]
        L.append(f"| {cid} {name} | {len(cs)} | {len(nc)} | {len(gs)} |")
    L += ["", "## 出典別の事実票数", "", "| 出典 | ライセンス | 区分 | 事実票 |", "|---|---|---|---|"]
    sc = collections.Counter(c["source"]["source_id"] for c in cards)
    for sid, n in sc.most_common():
        s = sources[sid]
        L.append(f"| {sid} | {s['license']} | {s['usage_tier']} | {n} |")
    L += ["", "## 未解決ギャップ（専門家意見・許諾等で補う項目）", "", "| ID | コース | 項目 | 解決方法 | 優先度 |", "|---|---|---|---|---|"]
    for g in gaps:
        if g["status"] in ("open", "in_review"):
            L.append(f"| {g['gap_id']} | {','.join(g['course'])} | {g['topic']} | {g['proposed_resolution']} | {g['priority']} |")
    L += ["", "## 事実票一覧", ""]
    for cid, name in COURSES.items():
        L += [f"### {cid} {name}", ""]
        for c in cards:
            if c.get("courses", [None])[0] == cid:
                lab = LABELS.get(c["evidence_class"], "")
                g = f"（{c['recommendation_strength']}）" if c.get("recommendation_strength") else ""
                L.append(f"- `{c['fact_id']}` {lab}{c['normalized_statement']}{g} — {c['source']['source_id']} {c['source']['location']} [{c['review_status']}]")
        L.append("")
    (ROOT / "reports").mkdir(exist_ok=True)
    (ROOT / "reports/coverage.md").write_text("\n".join(L), encoding="utf-8")
    print("wrote reports/coverage.md")


if __name__ == "__main__":
    main()
