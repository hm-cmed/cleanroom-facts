# 受け入れ検査：49_pn_d（2026-10-31）

- 判定：**合格**（必須の修正 0 件、望ましい修正 2 件）
- カード 19 件、出典 18 件（DOI あり 17、PMID あり 0）、対象小項目 14/14、uncertainty の記載 19/19、地域の記載 19/19
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-3444（Suleiman FA, Almaaitah AA, Aqrabawi HE. …）。DOI があれば書く（PMID も）
2. ライセンスが UNKNOWN の出典が 14/18 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
