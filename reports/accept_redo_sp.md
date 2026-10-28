# 受け入れ検査：redo_sp（2026-10-28）

- 判定：**合格**（必須の修正 0 件、望ましい修正 4 件）
- カード 23 件、出典 21 件（DOI あり 19、PMID あり 21）、対象小項目 0/0、uncertainty の記載 23/23、地域の記載 23/23
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 既存カードとほぼ同じ内容：RP-066 ≒ RP-007（0.92）
2. 薬の名前があるのに、国内の承認・保険適用の確認状況が uncertainty にない：SK-032
3. 論文と思われるのに DOI が空の出典：SRC-1545（Klein DA, Poth MA. Amenorrhea: An Approa…）、SRC-1547（Caproni M, Torchia D, Pestelli E, Volpi …）。DOI があれば書く（PMID も）
4. ライセンスが UNKNOWN の出典が 11/21 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。

## 対応（2026-10-28、Claude Code）

合格のため取り込んだ（`--append`）。対応表にもとづき、元の23件（BR-011〜013、DT-001・002・005・010・011・012・033、MT-013・022・023・029・030・035、RP-004〜007・016、SK-008・009）を `status: retired`、`superseded_by: <新しいID>` にした（三原の承認済み）。StatPearls を出典にした有効なカードは0件になった。「既存カードとほぼ同じ内容（RP-066 ≒ RP-007）」は置き換え元との類似で、問題ない。
