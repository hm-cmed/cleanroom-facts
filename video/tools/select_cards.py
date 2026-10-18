"""① カード選定：テーマに合い、一般向け区分のカードを選ぶ"""
import yaml, json, sys, os

DRUGS = ["アコチアミド","ラモセトロン","リナクロチド","エロビキシバット","ナルデメジン","リファキシミン","ルビプロストン",
         "アミトリプチリン","ミルタザピン","デュロキセチン","クエチアピン","ロペラミド","ポリエチレングリコール"]

def public_class(c):
    i = int(c["id"][3:]); s = c["assertion"]["plain_statement_ja"]; u = str(c.get("uncertainty") or "")
    if 39 <= i <= 47: return "除外"
    if any(d in s for d in DRUGS): return "要注意"
    if "二次資料経由" in u: return "保留"
    return "候補"

def select(cards, wanted):
    out = []
    for cid in wanted:
        c = next(x for x in cards if x["id"] == cid)
        out.append({"id": cid, "class": public_class(c), "status": c["publication_info"]["status"],
                    "statement": c["assertion"]["plain_statement_ja"],
                    "misconception": c["assertion"]["common_misconception"],
                    "condition": c["assertion"]["condition"], "source": c["provenance"]["source"]})
    return out

if __name__ == "__main__":
    cards = yaml.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "facts", "NG.yaml"), encoding="utf-8"))
    # テーマ「IBSは気のせい？」：誤解の欄が掴みになるカード＋基準＋定義
    sel = select(cards, ["NG-130", "NG-127", "NG-232"])
    for s in sel:
        assert s["class"] == "候補", f"{s['id']} は一般向け候補ではない: {s['class']}"
    import os; os.makedirs("out", exist_ok=True)
    json.dump(sel, open(os.path.join("out", "selected_cards.json"), "w"), ensure_ascii=False, indent=1)
    for s in sel: print(s["id"], s["class"], s["status"], "|", s["misconception"])
