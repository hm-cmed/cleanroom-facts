# 受け入れ検査：43_im_b（2026-10-31）

- 判定：**合格**（必須の修正 0 件、望ましい修正 2 件）
- カード 40 件、出典 37 件（DOI あり 32、PMID あり 0）、対象小項目 22/22、uncertainty の記載 40/40、地域の記載 40/40
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-2904（Yamaguchi M, Ohta A, Tsunematsu T, et al…）、SRC-2916（Petty RE, Southwood TR, Manners P, et al…）、SRC-2947（日本循環器学会ほか合同研究班. 2026年改訂版 大型血管炎診療ガイドライン. …）。DOI があれば書く（PMID も）
2. ライセンスが UNKNOWN の出典が 18/37 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。

## 対応（2026-10-31、Claude Code）

- 合格のため取り込んだ。出典マスターの空欄はカードの provenance から補った。アバコパンを有効な治療として書いたカードはない。撤回の日付の指摘（撤回通知は2026-06-29）を受け、依頼文の「登録時の決定」7を直した。
