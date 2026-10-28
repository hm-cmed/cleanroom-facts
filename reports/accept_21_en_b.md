# 受け入れ検査：21_en_b（2026-10-28）

- 判定：**差し戻し**（必須の修正 1 件、望ましい修正 4 件）
- カード 74 件、出典 52 件（DOI あり 46、PMID あり 51）、対象小項目 35/38、uncertainty の記載 74/74、地域の記載 74/74
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**必須**

1. 既存の出典と同じ文献に新しい番号を付けた：SRC-965 は同じ成果物の SRC-945 と同じ DOI。既存の番号を再利用する

**できれば**

1. カードがない対象の小項目：Ⅹ-9-D-① 体質性黄疸、Ⅹ-9-E-① Wilson病、Ⅹ-9-E-② ヘモクロマトーシス
2. 薬の名前があるのに、国内の承認・保険適用の確認状況が uncertainty にない：DM-011、DM-032、MT-004、MT-008
3. 論文と思われるのに DOI が空の出典：SRC-978（Gounden V, Easton-Carr R, Jialal I. Hypo…）、SRC-989（Maxfield L, Daley SF, Crane JS. Vitamin …）、SRC-990（Reddy P, Jialal I. Biochemistry, Fat Sol…）、SRC-991（Hisatome I, Ichida K, Mineo I, et al. Ja…）、SRC-994（Jagadeesan S, Kaliyadan F. Acrodermatiti…）、SRC-995（Salik I, Rawla P. Marfan Syndrome. In: S…）。DOI があれば書く（PMID も）
4. ライセンスが UNKNOWN の出典が 26/52 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。

## 対応（2026-10-28、Claude Code）

必須の指摘（SRC-965 が同じ成果物の SRC-945 と同じ文献）は、差し戻さずに取り込み後に処理した。SRC-965 を使うカードを SRC-945 に付け替え、SRC-965 は同一である旨を出典マスターに記録した（主張文・数値は変更なし）。第20回の後に追加した「成果物の中の重複」の検査で、取り込み前に見つけられた。
