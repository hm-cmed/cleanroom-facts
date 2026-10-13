# Phase 1：取り込みレポート（BP、2026-10-14）

生成：`scripts/ingest_round.py raw/05_biliary_pancreas.md BP`。主張文と数値は変更していない。

- 結果：書き込み済み
- カード：68件（BP-001〜BP-068）、欠番：なし
- スキーマ違反：0件
- 出典マスター：新規 13件（SRC-087, SRC-088, SRC-089, SRC-090, SRC-091, SRC-092, SRC-093, SRC-094, SRC-095, SRC-096, SRC-097, SRC-098, SRC-099）、既存の再利用 0件（）
- uncertainty に記載のあるカード：29件

## 形式の検査

問題なし（脚注マーカー・アンカー・basis_tag・仮ID・verifier の設定はない）

## subdomain 別

| subdomain | 件数 |
|---|---|
| 急性膵炎 | 12 |
| 慢性膵炎 | 10 |
| 胆道癌 | 9 |
| 胆石症 | 9 |
| 膵癌 | 8 |
| 胆石症・胆道感染症 | 6 |
| 膵神経内分泌腫瘍 | 5 |
| 原発性硬化性胆管炎 | 4 |
| 自己免疫性膵炎・IgG4関連疾患 | 4 |
| 膵嚢胞性腫瘍 | 1 |

## source_class 別（原本の値。Phase 3 で Crossref により確定）

| source_class | 件数 |
|---|---|
| UNKNOWN | 26 |
| RESTRICTED | 18 |
| GOV_JP | 12 |
| GOV_US | 12 |

## SRC 別の使用件数

| SRC | 件数 |
|---|---|
| SRC-087 | 12 |
| SRC-088 | 10 |
| SRC-089 | 6 |
| SRC-090 | 2 |
| SRC-091 | 2 |
| SRC-092 | 4 |
| SRC-093 | 4 |
| SRC-094 | 6 |
| SRC-095 | 5 |
| SRC-096 | 1 |
| SRC-097 | 9 |
| SRC-098 | 3 |
| SRC-099 | 4 |
