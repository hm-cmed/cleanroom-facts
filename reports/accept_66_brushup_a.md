# 受け入れ検査：66_brushup_a（2026-11-01）

- 判定：**合格**（必須の修正 0 件、望ましい修正 0 件）
- カード 20 件、出典 20 件（DOI あり 19、PMID あり 15）、対象小項目 20/20、uncertainty の記載 20/20、地域の記載 17/20
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

なし。

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
