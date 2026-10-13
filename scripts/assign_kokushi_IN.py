"""Phase 4（IN）：出題基準（令和6年版）の項目番号を付ける（人間の委任 2026-10-13）。

調査ラウンドは Ⅵ-3・Ⅵ-4 の表を取得できず kokushi: null としていた。Claude Code が .cache/kokushi/ の PDF
（医学各論）で項目を確認し、次の対応で付ける。ⅩⅢ の番号は PDF のテキストに出ない字形のため、ページ画像で確認した。
既に値があるカード（Ⅵ-5 の項目）は変えない（IN-057 だけは Lynch 症候群を含むため結腸癌を追加）。
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
IN = ROOT / "data" / "facts" / "IN.yaml"
TODAY = dt.date.today().isoformat()

ITEMS = {
    "Ⅵ-3-A-①": ("便秘症", "a"), "Ⅵ-3-A-②": ("過敏性腸症候群", "a"), "Ⅵ-3-A-③": ("吸収不良症候群", "b"),
    "Ⅵ-3-B-①": ("感染性腸炎", "a"), "Ⅵ-3-B-③": ("薬物性腸炎（備考：偽膜性腸炎）", "a"),
    "Ⅵ-3-B-④": ("Crohn病", "a"), "Ⅵ-3-B-⑤": ("潰瘍性大腸炎", "a"),
    "Ⅵ-3-C-①": ("大腸ポリープ、大腸腺腫", "a"), "Ⅵ-3-C-②": ("結腸癌", "a"),
    "Ⅵ-4-C-①": ("直腸癌", "a"), "Ⅵ-4-D-①": ("痔核", "a"),
    "Ⅵ-5-B-③": ("消化管ポリポーシス", "b"), "Ⅵ-5-D-①": ("食道憩室、胃憩室、十二指腸憩室、Meckel憩室、大腸憩室（備考：憩室炎、憩室出血）", "a"),
    "Ⅻ-1-A-⑲": ("ノロウイルス感染症", "a"), "Ⅻ-2-B-⑬": ("大腸菌感染症（備考：腸管出血性大腸菌感染症）", "a"),
    "Ⅻ-2-B-㉑": ("クロストリジウム・ディフィシル腸炎", "a"),
    "ⅩⅢ-1-A-①": ("細菌性食中毒", "a"), "ⅩⅢ-1-A-②": ("ウイルス性食中毒", "a"),
}
UC, CD = "Ⅵ-3-B-⑤", "Ⅵ-3-B-④"
COLON, RECTUM = "Ⅵ-3-C-②", "Ⅵ-4-C-①"
MAP = {
    **{i: [UC, CD] for i in ("IN-001", "IN-002", "IN-006")},
    **{i: [UC] for i in ("IN-003", "IN-004", "IN-007", "IN-008", "IN-011", "IN-012", "IN-013")},
    **{i: [CD] for i in ("IN-005", "IN-009", "IN-010", "IN-014", "IN-015", "IN-016")},
    **{f"IN-{n:03d}": ["Ⅵ-3-A-②"] for n in range(17, 27)},
    **{f"IN-{n:03d}": ["Ⅵ-3-A-①"] for n in range(27, 36)},
    **{i: ["Ⅵ-3-C-①"] for i in ("IN-036", "IN-037", "IN-038", "IN-039", "IN-040", "IN-041", "IN-044")},
    **{i: [COLON, RECTUM] for i in ("IN-042", "IN-046", "IN-047", "IN-048", "IN-051", "IN-053", "IN-054", "IN-055", "IN-056")},
    **{i: [RECTUM] for i in ("IN-049", "IN-050", "IN-052")},
    "IN-057": [COLON, "Ⅵ-5-B-③"], "IN-058": [COLON],
    **{f"IN-{n:03d}": ["Ⅵ-5-D-①"] for n in range(60, 70)},
    **{f"IN-{n:03d}": ["Ⅻ-2-B-⑬", "Ⅵ-3-B-①"] for n in range(70, 74)},
    **{i: ["ⅩⅢ-1-A-①", "Ⅵ-3-B-①"] for i in ("IN-074", "IN-075")},
    **{i: ["Ⅻ-1-A-⑲", "Ⅵ-3-B-①"] for i in ("IN-076", "IN-077", "IN-078")},
    "IN-079": ["ⅩⅢ-1-A-②", "Ⅻ-1-A-⑲"],
    **{f"IN-{n:03d}": ["Ⅻ-2-B-㉑", "Ⅵ-3-B-③"] for n in range(80, 85)},
    **{f"IN-{n:03d}": ["Ⅵ-3-A-③"] for n in range(85, 88)},
    "IN-088": ["Ⅵ-4-D-①"],
}


def fmt(key: str) -> str:
    name, level = ITEMS[key]
    return f"医学各論 {key}（{name}、{level}）"


def main() -> None:
    cards = yaml.safe_load(IN.read_text(encoding="utf-8"))
    n = 0
    for c in cards:
        cur = c["curriculum"]
        if c["id"] not in MAP:
            continue
        new = "；".join(fmt(k) for k in MAP[c["id"]])
        if cur.get("kokushi") and c["id"] != "IN-057":
            continue
        if cur.get("kokushi") == new:
            continue
        before = cur.get("kokushi")
        cur["kokushi"] = new
        c["history"].append({"date": TODAY, "by": "claude-code",
            "change": f"Phase 4：kokushi を設定（出題基準 令和6年版の医学各論 PDF で項目を確認。人間が2026-10-13にチャットで委任）。変更前：{before}"})
        n += 1
    missing = [c["id"] for c in cards if not c["curriculum"].get("kokushi")]
    IN.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
    print(f"set {n}; still null: {missing}")


if __name__ == "__main__":
    main()
