# 受け入れ検査：52_ps_b（2026-10-31）

- 判定：**合格**（必須の修正 0 件、望ましい修正 1 件）
- カード 40 件、出典 35 件（DOI あり 30、PMID あり 0）、対象小項目 21/21、uncertainty の記載 40/40、地域の記載 40/40
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-495（日本呼吸器学会・厚生労働科学研究費補助金難治性疾患政策研究事業「難治性呼吸器疾患…）、SRC-3740（National Institute for Health and Care E…）、SRC-3742（Fluoxetine Bulimia Nervosa Collaborative…）、SRC-3753（日本心身医学会用語委員会. 心身症の定義. 心身医学. 1991;31(7)…）。DOI があれば書く（PMID も）

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
