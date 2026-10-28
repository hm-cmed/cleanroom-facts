# 受け入れ検査：24_ds_b（2026-10-28）

- 判定：**合格**（必須の修正 0 件、望ましい修正 4 件）
- カード 63 件、出典 49 件（DOI あり 44、PMID あり 47）、対象小項目 44/46、uncertainty の記載 63/63、地域の記載 63/63
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. カードがない対象の小項目：Ⅲ-3-K-④ 硬結性紅斑、Ⅲ-3-S-① アミロイド苔癬
2. 論文と思われるのに DOI が空の出典：SRC-1183（Nardi NM, McDonald EJ, Syed HA, Schaefer…）、SRC-1188（Caplan AS, Gold JAW, Smith DJ, Ely JW. D…）、SRC-1200（Ely JW, Seabury Stone M. The generalized…）、SRC-1204（Ponka D, Baddar F. Microscopic potassium…）。DOI があれば書く（PMID も）
3. StatPearls を出典にしたカードが 1 件（出典 SRC-1183）。StatPearls は補助的な出典にとどめる決まり。一次資料（原著論文・ガイドライン・公的資料）に置き換えられないか確認する
4. ライセンスが UNKNOWN の出典が 34/49 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。
