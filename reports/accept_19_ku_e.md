# 受け入れ検査：19_ku_e（2026-10-28）

- 判定：**差し戻し**（必須の修正 2 件、望ましい修正 2 件）
- カード 60 件、出典 43 件（DOI あり 39、PMID あり 43）、対象小項目 20/24、uncertainty の記載 60/60、地域の記載 60/60
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**必須**

1. 出題基準の番号の誤り 24 件、コアカリの番号・id の誤り：RP-011: TBL-02-09-010/JlAKpoQ、RP-012: TBL-02-09-010/JlAKpoQ、RP-016: TBL-02-09-010/JlAKpoQ
2. カードがない対象の小項目：Ⅷ-8-D-① 月経前症候群、Ⅷ-8-E-⑤ 不育症、Ⅷ-8-F 避妊、Ⅷ-9-A 更年期障害

**できれば**

1. 論文と思われるのに DOI が空の出典：SRC-814（Holesh JE, Bass AN, Lord M. Physiology, …）、SRC-815（Lacroix AE, Gondal H, Shumway KR, Langak…）、SRC-816（Nawaz G, Rogol AD, Jenkins SM. Amenorrhe…）、SRC-823（Brott NR, Le JK. Mittelschmerz. In: Stat…）。DOI があれば書く（PMID も）
2. ライセンスが UNKNOWN の出典が 35/43 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。

## 補足（2026-10-28、Claude Code）

「出題基準の番号の誤り 24 件」の中身を確認した。成果物の `kokushi` は、依頼文 §7-1 の表にない番号と項目名を使っている（例：「Ⅷ-8-A-⑥（sex differentiation、c）」「Ⅷ-9-A-①（避妊法、a）」「Ⅷ-9-B-③（骨盤臓器脱、a）」）。表の Ⅷ-8・Ⅷ-9 とは番号も名称もレベルも対応しておらず、表を参照せずに番号を作ったとみられる。番号の付け直しには内容の判断が要るため、Claude Code では直さず差し戻す。あわせて、表のレベル a の項目のうち 月経前症候群（Ⅷ-8-D-①）・避妊（Ⅷ-8-F）・更年期障害（Ⅷ-9-A）にカードがない（不育症 Ⅷ-8-E-⑤ はレベル c）。コアカリの TBL-02-09-010 の id は JlAKpoU が正しい（成果物は JlAKpoQ）。
