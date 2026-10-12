"""Phase 2-2: proposals/es_merge_map.csv の approved_* 列に、Claude Code の決定を記入する。

通常この列は人間が埋める。2026-10-12 に人間がチャットで「Claude の推奨で確定」と委任したため、
例外として Claude Code が記入する。決定の理由は reports/02_es_merge.md に出す。
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "proposals" / "es_merge_map.csv"

# R_id: (approved_v1_id, approved_retire_v1_ids, 理由)
DECISIONS = {
    "ES-R01": ("ES-049", "", "全生存の比較（ES-049）が本体。pCR率の数値を持つ ES-050 は存続"),
    "ES-R02": ("ES-051", "", "同一試験（CheckMate 577）の改訂"),
    "ES-R03": ("ES-052", "", "同一試験（CheckMate 648）の改訂"),
    "ES-R04": ("ES-054", "", "5年追跡の記述は ES-054 に対応（スコア1位の ES-053 は初回解析の数値を持つので存続）"),
    "ES-R05": ("new", "", "国内承認の記述で、v1 に対応カードなし"),
    "ES-R06": ("ES-032", "", "非劣性の主結果（ES-032）が本体。逆流性食道炎・有害事象の数値を持つ ES-033 は存続"),
    "ES-R07": ("ES-023", "", "同一試験（デュピルマブ第3相）の改訂"),
    "ES-R08": ("ES-024", "", "FDA承認・国内承認状況の改訂"),
    "ES-R09": ("new", "", "国内の保険適用薬の記述で、v1 に対応カードなし"),
    "ES-R10": ("ES-063", "", "同一試験（Villanueva 2013）の改訂"),
    "ES-R11": ("ES-065", "", "同一試験（García-Pagán 2010）の改訂"),
    "ES-R12": ("ES-009", "", "Lyon 2.0 の閾値。ES-009（出典未取得）の改訂"),
    "ES-R13": ("ES-029", "", "DCI の区分は ES-029（過収縮）に対応。遠位食道痙攣の ES-028 は存続"),
    "ES-R14": ("ES-031", "", "オピオイドの記述は ES-031 に対応（スコア1位の ES-025 はアカラシアの定義で別内容）"),
    "ES-R15": ("new", "", "ALDH2 のオッズ比。ES-040（アセトアルデヒドの発がん性）とは別の命題として新規"),
    "ES-R16": ("ES-035", "ES-036", "罹患（ES-035）と死亡（ES-036）を新しい年の数値で更新。ES-036 は ES-035 に統合して廃止"),
    "ES-R17": ("ES-061", "", "静脈瘤の記載基準。ES-061（出典未取得）の改訂"),
    "ES-R18": ("ES-066", "", "日本の静脈瘤治療（EIS・B-RTO）。ES-066（出典未取得）の改訂"),
    "ES-R19": ("new", "", "保険収載の記述。ES-011（治療の適応）とは観点が異なるため新規"),
    "ES-089": ("", "ES-042", "ヨード染色。ES-042（出典未取得）とほぼ同内容のため ES-042 を廃止"),
}
# ES-067（Mallory-Weiss と Boerhaave、出典未取得）は、欠番 ES-084（Mallory-Weiss）の起票後に
# ES-084・ES-085 で置き換えて廃止する（es_new_cards の工程で扱う）。

DELEGATION = "claude-code（人間が2026-10-12にチャットで委任）"


def main():
    with CSV.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys())
    if "decided_by" not in fields:
        fields += ["decided_by", "decision_reason"]
    for r in rows:
        if r["R_id"] in DECISIONS:
            v1, retire, why = DECISIONS[r["R_id"]]
            r["approved_v1_id"], r["approved_retire_v1_ids"] = v1, retire
            r["decided_by"], r["decision_reason"] = DELEGATION, why
        else:
            r.setdefault("decided_by", "")
            r.setdefault("decision_reason", "")
            if not r["R_id"].startswith("ES-R"):
                r["decided_by"] = DELEGATION
                r["decision_reason"] = r["decision_reason"] or "v2 で ID 確定済み。v1 に廃止すべき重複なし"
    missing = [r["R_id"] for r in rows if r["R_id"].startswith("ES-R") and not r["approved_v1_id"]]
    if missing:
        raise SystemExit(f"未決定の行があります: {missing}")
    with CSV.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print("decisions written:", len(DECISIONS))


if __name__ == "__main__":
    main()
