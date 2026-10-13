# Phase 1：取り込みレポート（IN、2026-10-13）

生成：`scripts/ingest_round.py raw/03_intestine.md IN`。主張文と数値は変更していない。

- 結果：書き込み済み
- カード：88件（IN-001〜IN-088）、欠番：なし
- スキーマ違反：0件
- 出典マスター：新規 17件（SRC-048, SRC-049, SRC-050, SRC-051, SRC-052, SRC-053, SRC-054, SRC-055, SRC-056, SRC-057, SRC-058, SRC-059, SRC-060, SRC-061, SRC-062, SRC-063, SRC-064）、既存の再利用 1件（SRC-037）
- uncertainty に記載のあるカード：36件

## 形式の検査

問題なし（脚注マーカー・アンカー・basis_tag・仮ID・verifier の設定はない）

## subdomain 別

| subdomain | 件数 |
|---|---|
| 炎症性腸疾患 | 16 |
| 大腸癌 | 14 |
| 過敏性腸症候群 | 10 |
| 大腸ポリープ | 10 |
| 大腸憩室出血・憩室炎 | 10 |
| 感染性腸炎 | 10 |
| 慢性便秘症 | 9 |
| Clostridioides difficile感染症 | 5 |
| セリアック病 | 3 |
| 痔核 | 1 |

## source_class 別（原本の値。Phase 3 で Crossref により確定）

| source_class | 件数 |
|---|---|
| UNKNOWN | 44 |
| RESTRICTED | 20 |
| GOV_JP | 13 |
| GOV_US | 11 |

## SRC 別の使用件数

| SRC | 件数 |
|---|---|
| SRC-037 | 1 |
| SRC-048 | 10 |
| SRC-049 | 10 |
| SRC-050 | 9 |
| SRC-051 | 10 |
| SRC-052 | 8 |
| SRC-053 | 2 |
| SRC-054 | 3 |
| SRC-055 | 3 |
| SRC-056 | 3 |
| SRC-057 | 10 |
| SRC-058 | 4 |
| SRC-059 | 2 |
| SRC-060 | 4 |
| SRC-061 | 4 |
| SRC-062 | 1 |
| SRC-063 | 3 |
| SRC-064 | 1 |
