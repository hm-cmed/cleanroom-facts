# 受け入れ検査：19_ku_e（2026-10-28）

- 判定：**合格**（必須の修正 0 件、望ましい修正 4 件）
- カード 60 件、出典 44 件（DOI あり 40、PMID あり 44）、対象小項目 22/24、uncertainty の記載 60/60、地域の記載 60/60
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 欠番（理由の記載あり）：RP-053、RP-057
2. カードがない対象の小項目：Ⅷ-9-B-④ 動脈硬化、Ⅷ-9-B-⑤ 冠動脈疾患
3. 論文と思われるのに DOI が空の出典：SRC-814（Holesh JE, Bass AN, Lord M. Physiology, …）、SRC-815（Lacroix AE, Gondal H, Shumway KR, Langak…）、SRC-816（Nawaz G, Rogol AD, Jenkins SM. Amenorrhe…）、SRC-823（Brott NR, Le JK. Mittelschmerz. In: Stat…）。DOI があれば書く（PMID も）
4. ライセンスが UNKNOWN の出典が 35/44 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
