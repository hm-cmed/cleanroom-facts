# 受け入れ検査：32_ns_e（2026-10-28）

- 判定：**合格**（必須の修正 0 件、望ましい修正 2 件）
- カード 105 件、出典 86 件（DOI あり 80、PMID あり 82）、対象小項目 50/50、uncertainty の記載 105/105、地域の記載 105/105
- 照合：未実施（PC で --online を付けて実行する）

## 差し戻しの内容（作り手にそのまま渡せる）

次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。

**できれば**

1. 既存カードとほぼ同じ内容：TJ-003 ≒ NX-001（0.61）
2. 論文と思われるのに DOI が空の出典：SRC-1921（日本脳神経外科学会・日本脳神経外傷学会（監）. 頭部外傷治療・管理のガイドライン…）、SRC-1955（British Orthopaedic Association, British…）、SRC-1956（Ivins D. Acute ankle sprain: an update. …）、SRC-2008（Rosenbaum P, et al. A report: the defini…）。DOI があれば書く（PMID も）

## 取り込み

合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。

## 対応（2026-10-28、Claude Code）

- 合格のため取り込んだ。TJ-003 ≒ NX-001（GCS の定義、同じ出典 SRC-1806）は、分野をまたぐ重複として `proposals/cross_domain_codes_20261028.md` の B3 に加えた（統合は三原の承認後）。
