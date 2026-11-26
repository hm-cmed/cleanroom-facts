# 受け入れ検査：EB1_evidence_methods（2026-11-26）

- 判定：**合格**（必須の修正 0 件、望ましい修正 1 件）
- カード 12 件、出典 16 件（DOI あり 11、PMID あり 10）、対象小項目 0/0、uncertainty の記載 12/12、地域の記載 12/12
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-5500（Higgins JPT, Savović J, Page MJ, Elbers …）、SRC-5501（Richardson WS, Wilson MC, Nishikawa J, H…）、SRC-5510（Schünemann H, Brożek J, Guyatt G, Oxman …）、SRC-5515（国立研究開発法人日本医療研究開発機構（AMED）. 患者・市民参画（PPI）ガイ…）。DOI があれば書く（PMID も）

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
