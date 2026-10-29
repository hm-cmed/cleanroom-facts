# 受け入れ検査：37_if_e（2026-10-29）

- 判定：**合格**（必須の修正 0 件、望ましい修正 1 件）
- カード 19 件、出典 17 件（DOI あり 13、PMID あり 0）、対象小項目 0/0、uncertainty の記載 19/19、地域の記載 19/19
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-2191（大城健哉. 血液培養検査における Diagnostic Stewardship.…）。DOI があれば書く（PMID も）

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。

## 対応（2026-10-30、Claude Code）

- 合格のため取り込んだ。出典表に PMID・ライセンス表示の列がなかったので、出典マスターの pmid・pmcid・license_note は、同じ成果物のカードの provenance から機械的に写した（history に記録）。
- 申し送りの source_class（Siegel 2007 を GOV_US、手引き第四版を GOV_JP）は成果物のまま取り込み、PC での `--online` 照合のときに確かめる。
