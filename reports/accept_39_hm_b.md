# 受け入れ検査：39_hm_b（2026-10-31）

- 判定：**合格**（必須の修正 0 件、望ましい修正 2 件）
- カード 49 件、出典 45 件（DOI あり 44、PMID あり 0）、対象小項目 23/23、uncertainty の記載 49/49、地域の記載 49/49
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 既存カードとほぼ同じ内容：LY-021 ≒ KT-012（0.70）
2. 薬の名前があるのに、国内の承認・保険適用の確認状況が uncertainty にない：LY-028

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。

## 対応（2026-10-31、Claude Code）

- 合格のため取り込んだ。出典表に PMID・ライセンス表示の列がなかったので、`scripts/fill_sources_from_cards.py` で出典マスターの空欄をカードの provenance から写した。
- LY-021 ≒ KT-012 は同じ出典の同じ内容。統合を `proposals/cross_domain_codes_20261031.md` の E1 として提案した。
