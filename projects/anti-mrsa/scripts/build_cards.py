# -*- coding: utf-8 -*-
"""scripts/card_defs.py の初版定義から facts/*.yaml を生成する（初回のみ使用）。

使い方: python scripts/build_cards.py [--force]
既存の facts/*.yaml がある場合は、--force を付けない限り上書きしない。
"""
import sys, pathlib, yaml
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import card_defs as cd

ROOT = pathlib.Path(__file__).resolve().parents[1]
FACTS = ROOT / "facts"
FACTS.mkdir(exist_ok=True)
force = "--force" in sys.argv
CREATED = "2026-11-08"

for name, g in cd.GROUPS.items():
    out = FACTS / f"{name}.yaml"
    if out.exists() and not force:
        print(f"skip (exists): {out.name}")
        continue
    cards = []
    for (fid, courses, topic, stmt, ecls, grade, loc, conds, note) in g["cards"]:
        sid = g["source_id"] or cd.CARD_SOURCES[fid]
        cards.append({
            "fact_id": fid,
            "courses": courses,
            "topic": topic,
            "normalized_statement": stmt,
            "evidence_class": ecls,
            "population": g["population"],
            "conditions": conds,
            "exclusions": [],
            "recommendation_strength": grade,
            "certainty_of_evidence": None,
            "source": {"source_id": sid, "location": loc, "page": None,
                       "cq": loc if loc and loc.startswith("CQ") else None, "table_or_figure": None},
            "copyright_handling": {"mode": "fact_paraphrase", "verbatim_quote": False,
                                   "quotation_text": None, "quotation_reason": None},
            "clinical_use_prohibited": True,
            "review_status": "draft",
            "reviewers": [],
            "created_at": CREATED,
            "last_reviewed_at": None,
            "expiry_trigger": g["expiry"],
            "review_notes": note,
            "version": "0.1",
        })
    header = (f"# 事実票：{name}\n# 自動生成（scripts/build_cards.py, {CREATED}）。以後はこのファイルを直接編集してレビューする。\n"
              "# normalized_statement は原文の転載ではなく、事実を独自の表現で記載したもの。\n")
    with open(out, "w", encoding="utf-8") as f:
        f.write(header)
        yaml.safe_dump({"cards": cards}, f, allow_unicode=True, sort_keys=False, width=1000)
    print(f"wrote {out.name}: {len(cards)} cards")
