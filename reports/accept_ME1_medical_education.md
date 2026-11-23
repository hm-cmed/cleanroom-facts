# 受け入れ検査：ME1_medical_education（2026-11-23）

- 判定：**合格**（必須の修正 0 件、望ましい修正 1 件）
- カード 10 件、出典 13 件（DOI あり 5、PMID あり 5）、対象小項目 0/0、uncertainty の記載 10/10、地域の記載 10/10
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-5101（文部科学省. 医学／歯学教育モデル・コア・カリキュラム（令和4年度改訂版）. 2…）、SRC-5104（日本医師会. 特別寄稿「全国の医学生が受験する『共用試験』」. 日医 on-li…）、SRC-5111（Ende J. Feedback in clinical medical edu…）。DOI があれば書く（PMID も）

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
