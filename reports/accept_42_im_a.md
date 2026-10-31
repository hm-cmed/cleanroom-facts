# 受け入れ検査：42_im_a（2026-10-31）

- 判定：**合格**（必須の修正 0 件、望ましい修正 2 件）
- カード 23 件、出典 23 件（DOI あり 21、PMID あり 0）、対象小項目 14/14、uncertainty の記載 23/23、地域の記載 23/23
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-2825（松原篤、坂下雅文、後藤穣、ほか. 2019年全国疫学調査（鼻アレルギー）. 日本…）、SRC-2827（日本皮膚科学会. 蕁麻疹診療ガイドライン2026（第4版）. 日本皮膚科学会. …）。DOI があれば書く（PMID も）
2. ライセンスが UNKNOWN の出典が 10/23 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。

## 対応（2026-10-31、Claude Code）

- 合格のため取り込んだ。出典マスターの空欄はカードの provenance から補った（`scripts/fill_sources_from_cards.py`）。
- 既存の SRC-424（DOI・PMID の補完、RESTRICTED へ）と SRC-426（PMID の補完、RESTRICTED へ）の更新の提案は、識別子を API で確かめる決まりのため、PC での `--online` 照合のときに確かめてから反映する。
