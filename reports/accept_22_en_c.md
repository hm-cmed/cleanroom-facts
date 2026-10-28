# 受け入れ検査：22_en_c（2026-10-28）

- 判定：**合格**（必須の修正 0 件、望ましい修正 3 件）
- カード 47 件、出典 41 件（DOI あり 36、PMID あり 40）、対象小項目 19/19、uncertainty の記載 45/47、地域の記載 47/47
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 薬の名前があるのに、国内の承認・保険適用の確認状況が uncertainty にない：IE-009
2. 論文と思われるのに DOI が空の出典：SRC-1021（Li A, Kirk L. Intraductal Papilloma. In:…）、SRC-1022（Ajmal M, Khan M, Van Fossen K. Breast Fi…）、SRC-1023（Malherbe K, Szymanski KD. Fibrocystic Br…）、SRC-1048（Gaddey HL, Holder KK. Unintentional Weig…）。DOI があれば書く（PMID も）
3. ライセンスが UNKNOWN の出典が 24/41 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
