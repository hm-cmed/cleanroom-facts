# Phase 6：専門医レビュー用シート（2026-10-12）

## 出力

| ファイル | 件数 | 備考 |
|---|---|---|
| review/review_ES_20261012.xlsx | 89 | retired 4件を除く |
| review/review_HP_20261012.xlsx | 20 | |
| review/review_UG_20261012.xlsx | 18 | |

- 生成：`scripts/export_review.py`（`--csv` で UTF-8 BOM 付き CSV も出力）
- シート「説明」：確認者（B2）・確認日（B3）の記入欄と記入方法
- シート「review」：判定（OK／修正／削除のプルダウン）・修正案・コメントが記入欄（黄色）。DOI・PMID はリンク付き
- 「Claude Codeによる修正」列：Claude Code が一次資料をもとに主張文・出典を変更・作成した履歴。専門医に特に確認してほしい箇所

## 取り込み（`scripts/import_review.py`）

- 引数なしは確認のみ、`--apply` で反映。
- OK → 確認者・確認日を verifier・verified_at に転記し verified_expert に昇格（history は `human:<確認者>`）。
- 修正・削除 → `proposals/review_fixes_<領域>_<日付>.md` に提案として出す。本文は書き換えない。
- 次の場合は何も反映しない：確認者・確認日が空、判定が OK／修正／削除以外、修正案が空の「修正」、シート出力後に主張文が変わったカード。

## 動作確認

記入済みのテスト用シート（スクラッチ領域）で、確認のみ・不正な判定での中止・正常な反映を確認し、確認後に ES.yaml を元に戻した。
