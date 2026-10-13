# Phase 1：取り込みレポート（LV、2026-10-13）

生成：`scripts/ingest_round.py raw/04_liver.md LV`。主張文と数値は変更していない。

- 結果：書き込み済み
- カード：104件（LV-001〜LV-104）、欠番：なし
- スキーマ違反：0件
- 出典マスター：新規 22件（SRC-065, SRC-066, SRC-067, SRC-068, SRC-069, SRC-070, SRC-071, SRC-072, SRC-073, SRC-074, SRC-075, SRC-076, SRC-077, SRC-078, SRC-079, SRC-080, SRC-081, SRC-082, SRC-083, SRC-084, SRC-085, SRC-086）、既存の再利用 1件（SRC-018）
- uncertainty に記載のあるカード：32件

## 形式の検査

問題なし（脚注マーカー・アンカー・basis_tag・仮ID・verifier の設定はない）

## subdomain 別

| subdomain | 件数 |
|---|---|
| 肝硬変とその合併症 | 22 |
| ウイルス性肝炎 | 19 |
| NAFLD/NASH・MASLD | 15 |
| 肝細胞癌 | 14 |
| 自己免疫性肝疾患 | 10 |
| 代謝性肝疾患 | 5 |
| 体質性黄疸 | 4 |
| 急性肝不全 | 4 |
| 肝の血管性疾患 | 4 |
| 薬物性肝障害 | 3 |
| 寄生虫性肝疾患 | 2 |
| 肝膿瘍 | 2 |

## source_class 別（原本の値。Phase 3 で Crossref により確定）

| source_class | 件数 |
|---|---|
| UNKNOWN | 26 |
| GOV_JP | 26 |
| RESTRICTED | 23 |
| GOV_US | 17 |
| OPEN | 12 |

## SRC 別の使用件数

| SRC | 件数 |
|---|---|
| SRC-018 | 22 |
| SRC-065 | 12 |
| SRC-066 | 3 |
| SRC-067 | 12 |
| SRC-068 | 2 |
| SRC-069 | 3 |
| SRC-070 | 4 |
| SRC-071 | 4 |
| SRC-072 | 3 |
| SRC-073 | 2 |
| SRC-074 | 4 |
| SRC-075 | 2 |
| SRC-076 | 5 |
| SRC-077 | 5 |
| SRC-078 | 3 |
| SRC-079 | 2 |
| SRC-080 | 2 |
| SRC-081 | 2 |
| SRC-082 | 1 |
| SRC-083 | 1 |
| SRC-084 | 3 |
| SRC-085 | 5 |
| SRC-086 | 2 |
