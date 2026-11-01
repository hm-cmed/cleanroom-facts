# 受け入れ検査：63_brushup_a（2026-11-01）

- 判定：**差し戻し**（必須の修正 1 件、望ましい修正 2 件）
- カード 26 件、出典 25 件（DOI あり 21、PMID あり 23）、対象小項目 26/26、uncertainty の記載 26/26、地域の記載 26/26
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**必須**

1. 既存の出典と同じ文献に新しい番号を付けた：SRC-1366 は既存の SRC-1277 と同じ DOI。既存の番号を再利用する

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-4623（Heim SW, Maughan KL. Foreign bodies in t…）、SRC-4631（Gauer RL, Semidey MJ. Diagnosis and Trea…）、SRC-4632（Galioto NJ. Peritonsillar Abscess. Am Fa…）。DOI があれば書く（PMID も）
2. ライセンスが UNKNOWN の出典が 8/25 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
