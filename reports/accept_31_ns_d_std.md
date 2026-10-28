# 受け入れ検査：31_ns_d_std（2026-10-28）

- 判定：**合格**（必須の修正 0 件、望ましい修正 2 件）
- カード 97 件、出典 89 件（DOI あり 83、PMID あり 87）、対象小項目 56/56、uncertainty の記載 97/97、地域の記載 97/97
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 既存カードとほぼ同じ内容：BD-001 ≒ TH-023（0.82）
2. 論文と思われるのに DOI が空の出典：SRC-1831（骨粗鬆症の予防と治療ガイドライン作成委員会（日本骨粗鬆症学会・日本骨代謝学会・骨…）、SRC-1849（van der Heijde D. How to read radiograph…）、SRC-1871（Ramirez J. Adhesive Capsulitis: Diagnosi…）、SRC-1882（Herring JA, Kim HT, Browne R. Legg-Calve…）、SRC-1896（Sobti A, Agrawal P, Agarwala S, Agarwal …）。DOI があれば書く（PMID も）

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。

## 対応（2026-10-28、Claude Code）

- 原本 `raw/31_ns_d.md` の形の問題は第28〜30回と同じで、標準の形に移した `raw/31_ns_d_std.md` で検査し、合格したので取り込んだ。
- BD-001 ≒ TH-023：同じ出典（SRC-927）で原発性骨粗鬆症の診断基準（2012年改訂版）を述べた、実質同じ内容のカード。骨粗鬆症は出題基準の Ⅸ-7-C-①（BD）と Ⅹ-3-B-①（TH）の両方にあるため、両方を残して取り込んだ。一方を廃止して他方につなぐかは三原の判断を待つ。
