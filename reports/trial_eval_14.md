# 試行の比較：第14回（2026-10-28）

`scripts/eval_trial.py` --online の出力。作り手は伏せたまま（A・B）。採点は `docs/tasks/trial_eval.md` の表で行う。

## 1. 客観指標

| 指標 | A | B |
|---|---|---|
| カード数（目安 25〜45） | 28 | 35 |
| 形式の問題（脚注・アンカー・ブロック数・作り手名など） | 0 | 0 |
| スキーマに合うカード | 28/28（100%） | 35/35（100%） |
| status・verifier の指定違反 | 0 | 0 |
| 主張文の括弧書き（要確認など） | 0 | 0 |
| ID の指定違反・重複・欠番 | 0・0・0 | 0・0・0 |
| SRC の範囲外・表にない参照・未使用 | 0・0・0 | 0・0・0 |
| 既存 SRC と同じ文献を新番号で登録 | 0 | 0 |
| 出典数（DOI あり／PMID あり） | 28（28／28） | 30（19／9） |
| source_class の内訳 | {'UNKNOWN': 6, 'OPEN': 5, 'RESTRICTED': 17} | {'GOV_US': 6, 'RESTRICTED': 5, 'OPEN': 2, 'UNKNOWN': 17} |
| 対象小項目のカバー（16項目） | 16/16（100%） | 16/16（100%） |
| テーマのカバー（6件） | 6/6（100%） | 6/6（100%） |
| 出題基準の番号が正しいカード（誤り） | 28/28（100%）（0） | 35/35（100%）（0） |
| コアカリの番号と id が正しいカード（誤り） | 28/28（100%）（0） | 35/35（100%）（0） |
| uncertainty の記載 | 26/28（93%） | 33/35（94%） |
| 「二次資料経由」「表から読み取り」の明記 | 0・0 | 12・2 |
| condition.region の記載 | 17/28（61%） | 35/35（100%） |
| 既存カードと類似（0.6以上） | 0 | 0 |
| 主張文の長さ（中央値・最大） | 161・317 | 172・259 |
| DOI が Crossref で実在（不明） | 26（2） | 19（0） |
| DOI の題名が原本と食い違う | 1 | 0 |
| PMID が実在し DOI と一致（問題） | 28（2） | 9（0） |
| ライセンス判定が Crossref と一致（食い違い・欄なし） | 15（0・11） | 7（3・9） |
| 照合できなかったもの（unresolved） | 0 | 0 |

## 2. 詳細

### A

- DOI が見つからない：SRC-534: 確認できず（null）、SRC-545: なし（未確認のため null）
- 題名の食い違い：SRC-557: Crossref「The International Association for the Study of Lung Cancer L」
- PMID の問題：SRC-534: PMID 27162815 の DOI が原本の DOI と違う、SRC-545: PMID 34970102 の DOI が原本の DOI と違う

### B

- ライセンスの食い違い：SRC-538: Crossref は https://creativecommons.org/licenses/by/4.0/、原本は UNKNOWN、SRC-540: Crossref は http://creativecommons.org/licenses/by/4.0/、原本は UNKNOWN、SRC-543: Crossref は https://www.elsevier.com/tdm/userlicense/1.0/ https://www.elsevier.com/legal/tdmrep-license http://creativecommons.org/licenses/by-nc-nd/4.0/、原本は OPEN

## 3. 数値の抜き取り確認

各成果物から 8 枚ずつ無作為に選び、`reports/trial_sample_14.csv` に出した。出典（抄録・本文）と照らして「一致／不一致／確認できず」を記入する。どちらの成果物かは列 `set` だけで示す。

