# 受け入れ検査：65_brushup_a（2026-11-01）

- 判定：**合格**（必須の修正 0 件、望ましい修正 1 件）
- カード 25 件、出典 25 件（DOI あり 16、PMID あり 15）、対象小項目 24/24、uncertainty の記載 25/25、地域の記載 25/25
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-4803（International Federation of Red Cross an…）、SRC-4805（消費者庁. 視聴覚資料「家庭用品等による中毒事故を防ぐために」指導者用解説書（平…）。DOI があれば書く（PMID も）

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
