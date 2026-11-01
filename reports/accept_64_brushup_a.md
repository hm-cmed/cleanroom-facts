# 受け入れ検査：64_brushup_a（2026-11-01）

- 判定：**合格**（必須の修正 0 件、望ましい修正 1 件）
- カード 22 件、出典 19 件（DOI あり 10、PMID あり 12）、対象小項目 22/22、uncertainty の記載 22/22、地域の記載 22/22
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-665（Trayes KP, Studdiford JS, Pickle S, Tull…）、SRC-4723（European Association of Urology. EAU Gui…）、SRC-4724（National Institute for Health and Care E…）、SRC-4725（Türk C, Donaldson JF, Petřík A, et al. E…）、SRC-4727（McGregor TB, Pike JG, Leonard MP. Pathol…）、SRC-4730（European Association of Urology. EAU Gui…）、SRC-4732（Royal College of Obstetricians and Gynae…）、SRC-4733（National Institute for Health and Care E…）。DOI があれば書く（PMID も）

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
