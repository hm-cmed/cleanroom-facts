# 受け入れ検査：23_ds_a（2026-10-28）

- 判定：**合格**（必須の修正 0 件、望ましい修正 2 件）
- カード 66 件、出典 53 件（DOI あり 42、PMID あり 52）、対象小項目 46/46、uncertainty の記載 66/66、地域の記載 66/66
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-1074（Srivastava D, Sathe NC, Persaud Y. Astea…）、SRC-1075（Hardin CA, Love LW, Saleh HM, Farci F. N…）、SRC-1096（Nicholson CL, Daveluy S. Epidermal Nevus…）、SRC-1097（Agarwal P, Patel BC. Nevus of Ota and It…）、SRC-1100（Lewis D, Vaidya R. Kasabach-Merritt Synd…）、SRC-1104（Miceli A, Stewart KM. Lymphatic Malforma…）、SRC-1105（Zito PM, Scharf R. Epidermoid Cyst. In: …）、SRC-1106（Greco MJ, Bhutta BS. Seborrheic Keratosi…）、SRC-1107（Luba MC, Bangs SA, Mohler AM, Stulberg D…）、SRC-1123（Weir CB, Sathe NC, St.Hilaire NJ. Epider…）。DOI があれば書く（PMID も）
2. ライセンスが UNKNOWN の出典が 32/53 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
