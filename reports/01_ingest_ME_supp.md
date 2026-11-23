# Phase 1：取り込みレポート（ME、2026-11-23）

生成：`scripts/ingest_round.py raw/ME2_medical_education.md ME`。主張文と数値は変更していない。

- 結果：書き込み済み
- カード：9件（ME-011〜ME-019）、欠番：なし
- スキーマ違反：0件
- 出典マスター：新規 10件（SRC-5114, SRC-5115, SRC-5116, SRC-5117, SRC-5118, SRC-5119, SRC-5120, SRC-5121, SRC-5122, SRC-5123）、既存の再利用 3件（SRC-5101, SRC-5102, SRC-5104）
- uncertainty に記載のあるカード：9件

## 形式の検査

問題なし（脚注マーカー・アンカー・basis_tag・仮ID・verifier の設定はない）

## subdomain 別

| subdomain | 件数 |
|---|---|
| 教育手法 | 4 |
| 横断 | 3 |
| 制度 | 1 |
| 評価 | 1 |

## source_class 別（原本の値。Phase 3 で Crossref により確定）

| source_class | 件数 |
|---|---|
| RESTRICTED | 7 |
| GOV_JP | 1 |
| OPEN | 1 |

## SRC 別の使用件数

| SRC | 件数 |
|---|---|
| SRC-5102 | 1 |
| SRC-5116 | 1 |
| SRC-5117 | 1 |
| SRC-5118 | 1 |
| SRC-5119 | 1 |
| SRC-5120 | 1 |
| SRC-5121 | 1 |
| SRC-5122 | 1 |
| SRC-5123 | 1 |
