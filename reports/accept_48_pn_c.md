# 受け入れ検査：48_pn_c（2026-10-31）

- 判定：**合格**（必須の修正 0 件、望ましい修正 1 件）
- カード 26 件、出典 26 件（DOI あり 24、PMID あり 0）、対象小項目 18/18、uncertainty の記載 26/26、地域の記載 26/26
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-3365（Ogawa Y. Chronic lung disease of the ver…）。DOI があれば書く（PMID も）

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
