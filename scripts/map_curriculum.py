"""Phase 4: コアカリ（令和4年度版）と医師国家試験出題基準（令和6年版）の番号の候補を出す。

使い方（リポジトリ直下で）:
    .\\.venv\\Scripts\\python.exe scripts\\map_curriculum.py ES            # proposals/curriculum_map_ES.csv を出す
    .\\.venv\\Scripts\\python.exe scripts\\map_curriculum.py ES --apply    # 承認列を書き込む（承認済みの行だけ）

- コアカリの id は data/curriculum/core-curriculum/ の CSV から引く（index は表示用、id は不変）。
- 出題基準の項目は .cache/kokushi/ の PDF（リポジトリ外）から確認した番号を KOKUSHI に転記している。
- 候補はキーワード照合で最大3件。CSV の approved_core・approved_kokushi 列を人間が埋め、--apply で反映する。
  「該当なし」と書けば、その旨を記録する。
"""
from __future__ import annotations

import csv
import datetime as dt
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "data" / "facts"
CC = ROOT / "data" / "curriculum" / "core-curriculum" / "2022" / "ja"
PROPOSALS = ROOT / "proposals"
REPORTS = ROOT / "reports"
TODAY = dt.date.today().isoformat()
NONE = "該当なし"

# コアカリ：index → 照合キーワード（id と項目名は CSV から引く）
CORE = {
    "PS-02-08-02": ["症状", "症候", "胸やけ", "嚥下障害", "吐血", "嚥下痛"],
    "PS-02-08-03": ["検査", "内視鏡所見", "モニタリング", "pH", "インピーダンス", "内圧", "HRM", "Chicago", "造影", "染色", "生検", "CT", "分類", "EREFS", "AET"],
    "PS-02-08-04": ["治療", "推奨", "投与", "切除", "EVL", "EIS", "TIPS", "POEM", "筋切開", "手術", "摘出", "拡張", "止血", "輸血", "保険収載", "承認"],
    "PS-02-08-05": ["疾患", "病態", "有病率", "定義", "危険因子", "GERD", "逆流性食道炎", "NERD", "Barrett", "EoE", "好酸球性食道炎", "アカラシア",
                    "静脈瘤", "門脈圧亢進症", "Mallory-Weiss", "Boerhaave", "食道破裂", "ヘルニア", "憩室", "Plummer", "食道炎", "腐食", "異物", "痙攣", "過収縮", "無効食道運動"],
    "PS-03-04-14": ["食道癌", "扁平上皮癌", "腺癌", "術前", "術後", "化学療法", "ニボルマブ", "ペムブロリズマブ", "JCOG", "癌化", "発癌", "多重癌", "内視鏡切除", "ESD"],
    "PS-03-03-03": ["カンジダ", "HSV", "CMV", "ヘルペス", "サイトメガロ", "免疫不全"],
}
# 別表2-7（消化器系）の項目：index → キーワード
TBL0207 = {
    "TBL-02-07-019": ["吐血", "静脈瘤出血", "消化管出血", "Mallory-Weiss"],
    "TBL-02-07-025": ["胸やけ"],
    "TBL-02-07-030": ["内視鏡所見", "内視鏡で", "内視鏡検査", "拡大内視鏡", "染色", "EREFS", "LA分類"],
    "TBL-02-07-033": ["EVL", "EIS", "内視鏡的", "内視鏡で摘出", "ESD", "内視鏡切除", "POEM", "ARMS", "クリップ", "局注"],
    "TBL-02-07-034": ["TIPS", "B-RTO", "BRTO"],
    "TBL-02-07-004": ["蠕動", "IRP", "DCI", "内圧", "運動障害"],
}
# 出題基準（令和6年版）：表記 → (項目名, レベル, キーワード)
KOKUSHI = {
    "医学各論 Ⅵ-1-A-①": ("食道アカラシア", "b", ["アカラシア", "POEM", "LHM", "Heller", "遠位食道痙攣", "過収縮", "無効食道運動", "EGJOO"]),
    "医学各論 Ⅵ-1-B-①": ("胃食道逆流症<GERD>、非びらん性胃食道逆流症<NERD>", "a", ["GERD", "NERD", "PPIテスト", "逆流モニタリング", "インピーダンス", "Lyon", "ARMS", "逆流防止"]),
    "医学各論 Ⅵ-1-B-②": ("逆流性食道炎（備考：Barrett上皮、Barrett食道）", "a", ["逆流性食道炎", "LA分類", "Barrett", "ボノプラザン"]),
    "医学各論 Ⅵ-1-C-①": ("食道癌", "a", ["食道癌", "扁平上皮癌", "腺癌", "JCOG", "CheckMate", "KEYNOTE", "多重癌", "ヨード", "拡大内視鏡分類", "ALDH2", "アセトアルデヒド", "表在"]),
    "医学各論 Ⅵ-1-D-①": ("食道静脈瘤（備考：胃静脈瘤、BRTO）", "a", ["静脈瘤", "EVL", "EIS", "B-RTO", "TIPS"]),
    "医学各論 Ⅵ-1-E-①": ("Mallory-Weiss症候群", "a", ["Mallory-Weiss"]),
    "医学各論 Ⅵ-1-E-②": ("食道穿孔・破裂（備考：Boerhaave症候群）", "b", ["Boerhaave", "食道破裂", "穿孔"]),
    "医学各論 Ⅵ-5-A-②": ("消化管アレルギー、好酸球性胃腸炎、好酸球性食道炎", "b", ["EoE", "好酸球性食道炎", "EREFS", "デュピルマブ"]),
    "医学各論 Ⅵ-6-D-①": ("門脈圧亢進症", "a", ["門脈圧亢進症", "CSPH", "HVPG", "NSBB", "カルベジロール"]),
    "医学各論 Ⅵ-9-A-①": ("食道裂孔ヘルニア", "a", ["裂孔ヘルニア"]),
    "医学各論 Ⅶ-1-A-①": ("鉄欠乏性貧血", "a", ["鉄欠乏性貧血"]),
    "医学各論 Ⅻ-1-A-⑩": ("単純ヘルペスウイルス感染症", "a", ["HSV", "ヘルペス"]),
    "医学各論 Ⅻ-1-A-⑭": ("サイトメガロウイルス感染症", "a", ["CMV", "サイトメガロ"]),
    "医学総論 Ⅵ-5-B": ("嚥下障害（嚥下痛・通過障害・誤嚥）", "-", ["嚥下障害", "嚥下痛", "食物塊"]),
    "医学総論 Ⅵ-5-C-①": ("胸やけ、呑酸", "-", ["胸やけ"]),
    "医学総論 Ⅵ-5-F-①": ("吐血", "-", ["吐血", "静脈瘤出血", "消化管出血"]),
    "医学総論 Ⅸ-3-B-①": ("輸血の適応と一般的注意", "-", ["輸血"]),
}
# subdomain ごとの既定値（キーワードが当たらない場合の第1候補）
SUBDOMAIN_DEFAULT_KOKUSHI = {
    "GERD・NERD・Barrett食道": "医学各論 Ⅵ-1-B-①",
    "好酸球性食道炎（EoE）": "医学各論 Ⅵ-5-A-②",
    "食道運動障害": "医学各論 Ⅵ-1-A-①",
    "食道癌": "医学各論 Ⅵ-1-C-①",
    "食道静脈瘤・門脈圧亢進症": "医学各論 Ⅵ-1-D-①",
}
SUBDOMAIN_DEFAULT_CORE = {"食道癌": "PS-03-04-14"}

# キーワード照合の誤りを Claude Code が読み比べて直した推奨（理由つき）。人間の承認の対象。
_B2 = ("医学各論 Ⅵ-1-B-②", "逆流性食道炎・Barrett食道のカード（出題基準では Barrett は逆流性食道炎の備考）")
OVERRIDE_KOKUSHI = {
    **{cid: _B2 for cid in ("ES-003", "ES-004", "ES-005", "ES-006", "ES-007", "ES-012", "ES-013", "ES-014", "ES-015", "ES-016", "ES-017")},
    "ES-057": ("医学各論 Ⅵ-6-D-①", "CSPH の定義は門脈圧亢進症の項目"),
    "ES-059": ("医学各論 Ⅵ-6-D-①", "NSBB の用量は門脈圧亢進症の項目"),
    "ES-063": ("医学総論 Ⅸ-3-B-①；医学総論 Ⅵ-5-F-①", "輸血閾値のRCT。輸血と吐血の項目"),
    "ES-072": ("医学総論 Ⅵ-5-B", "食物塊嵌頓は嚥下障害（通過障害）。食道癌は鑑別語に引きずられた誤り"),
    "ES-074": (NONE, "腐食性食道傷害に該当する項目がない"),
    "ES-075": (NONE, "腐食性食道傷害に該当する項目がない"),
    "ES-078": (NONE, "カンジダ食道炎に該当する項目がない（EoE は鑑別語に引きずられた誤り）"),
    "ES-079": ("医学各論 Ⅻ-1-A-⑩；医学各論 Ⅻ-1-A-⑭", "HSV と CMV の両方を扱う"),
    "ES-080": ("医学各論 Ⅻ-1-A-⑩；医学各論 Ⅻ-1-A-⑭", "HSV と CMV の両方を扱う"),
    "ES-081": ("医学各論 Ⅻ-1-A-⑩；医学各論 Ⅻ-1-A-⑭", "HSV と CMV の両方を扱う"),
    "ES-082": ("医学各論 Ⅶ-1-A-①；医学総論 Ⅵ-5-B", "Plummer-Vinson は鉄欠乏性貧血と嚥下障害の項目（独立した項目はない）"),
    "ES-084": ("医学各論 Ⅵ-1-E-①", "Mallory-Weiss 症候群の項目（静脈瘤は鑑別語に引きずられた誤り）"),
}


def load_core() -> dict[str, dict]:
    items = {}
    for f in ("outcomes/layer4.csv",):
        with (CC / f).open(encoding="utf-8-sig") as fh:
            for r in csv.DictReader(fh):
                items[r["index"]] = r
    with (CC / "tables" / "TBL0207.csv").open(encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            items[r["index"]] = r
    return items


def card_text(c: dict) -> str:
    a = c["assertion"]
    return " ".join(str(x) for x in (a.get("plain_statement_ja"), a.get("condition"), a.get("differential"), c.get("subdomain")) if x)


def rank(text: str, catalog: dict[str, list[str]], default: str | None) -> list[tuple[str, int, list[str]]]:
    scored = []
    for key, kws in catalog.items():
        hits = [k for k in kws if k.lower() in text.lower()]
        score = len(hits) + (2 if key == default else 0)
        if score:
            scored.append((key, score, hits))
    scored.sort(key=lambda x: (-x[1], x[0]))
    return scored[:3]


def fmt_core(index: str, core: dict) -> str:
    return f"{index} (id: {core[index]['id']})"


def propose(prefix: str) -> None:
    core = load_core()
    for idx in list(CORE) + list(TBL0207):
        if idx not in core:
            raise SystemExit(f"コアカリ CSV に {idx} がありません")
    cards = [c for c in yaml.safe_load((FACTS / f"{prefix}.yaml").read_text(encoding="utf-8"))
             if c["publication_info"]["status"] != "retired"]
    rows = []
    for c in cards:
        text = card_text(c)
        sd = c.get("subdomain") or ""
        core_rank = rank(text, CORE, SUBDOMAIN_DEFAULT_CORE.get(sd, "PS-02-08-05"))
        tbl_rank = rank(text, TBL0207, None)
        kok_rank = rank(text, {k: v[2] for k, v in KOKUSHI.items()}, SUBDOMAIN_DEFAULT_KOKUSHI.get(sd))
        rec_core = [fmt_core(core_rank[0][0], core)] if core_rank else []
        if tbl_rank:
            rec_core.append(fmt_core(tbl_rank[0][0], core))
        rec_kok = f"{kok_rank[0][0]}（{KOKUSHI[kok_rank[0][0]][0]}、{KOKUSHI[kok_rank[0][0]][1]}）" if kok_rank else NONE
        note = ""
        if c["id"] in OVERRIDE_KOKUSHI:
            keys, note = OVERRIDE_KOKUSHI[c["id"]]
            rec_kok = NONE if keys == NONE else "；".join(f"{k}（{KOKUSHI[k][0]}、{KOKUSHI[k][1]}）" for k in keys.split("；"))
            note = f"推奨を手で修正：{note}"
        rows.append({
            "id": c["id"], "subdomain": sd, "statement": c["assertion"]["plain_statement_ja"],
            "core_candidates": " / ".join(f"{k}（{core[k]['item'][:24]}；{','.join(h)}）" for k, _, h in core_rank),
            "table_candidates": " / ".join(f"{k}（{core[k]['item']}；{','.join(h)}）" for k, _, h in tbl_rank),
            "kokushi_candidates": " / ".join(f"{k}（{KOKUSHI[k][0]}；{','.join(h)}）" for k, _, h in kok_rank),
            "recommended_core": "；".join(rec_core) or NONE,
            "recommended_kokushi": rec_kok,
            "note": note,
            "approved_core": "", "approved_kokushi": "",
        })
    out = PROPOSALS / f"curriculum_map_{prefix}.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"{out.relative_to(ROOT)}: {len(rows)} rows；kokushi 該当なし {sum(r['recommended_kokushi'] == NONE for r in rows)}")


def apply(prefix: str, approver: str) -> None:
    path = PROPOSALS / f"curriculum_map_{prefix}.csv"
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = {r["id"]: r for r in csv.DictReader(f)}
    facts = FACTS / f"{prefix}.yaml"
    cards = yaml.safe_load(facts.read_text(encoding="utf-8"))
    n = 0
    for c in cards:
        r = rows.get(c["id"])
        if not r or not (r["approved_core"] or r["approved_kokushi"]):
            continue
        cur = c.setdefault("curriculum", {})
        before = dict(cur)
        if r["approved_core"]:
            cur["core_curriculum"] = r["approved_core"]
        if r["approved_kokushi"]:
            cur["kokushi"] = r["approved_kokushi"]
        c.setdefault("history", []).append({"date": TODAY, "by": "claude-code",
            "change": f"curriculum を設定（proposals/curriculum_map_{prefix}.csv、{approver}）。変更前：{before}"})
        n += 1
    facts.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
    print(f"applied {n} cards")


if __name__ == "__main__":
    args = sys.argv[1:]
    prefix = args[0]
    if "--apply" in args:
        approver = next((a.split("=", 1)[1] for a in args if a.startswith("--approver=")), "人間の承認")
        apply(prefix, approver)
    else:
        propose(prefix)
