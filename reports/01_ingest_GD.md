# Phase 1：取り込みレポート（GD、2026-10-13）

生成：`scripts/ingest_round.py raw/02_gastroduodenal.md GD`。主張文と数値は変更していない。

- 結果：書き込み済み
- カード：95件（GD-001〜GD-095）、欠番：なし
- スキーマ違反：0件
- 出典マスター：新規 20件（SRC-028, SRC-029, SRC-030, SRC-031, SRC-032, SRC-033, SRC-034, SRC-035, SRC-036, SRC-037, SRC-038, SRC-039, SRC-040, SRC-041, SRC-042, SRC-043, SRC-044, SRC-045, SRC-046, SRC-047）、既存の再利用 2件（SRC-017, SRC-018）
- uncertainty に記載のあるカード：22件

## 形式の検査

問題なし（脚注マーカー・アンカー・basis_tag・仮ID・verifier の設定はない）

## subdomain 別

| subdomain | 件数 |
|---|---|
| 胃癌 | 29 |
| 機能性ディスペプシア | 18 |
| NSAID・LDA潰瘍の予防 | 9 |
| GIST・粘膜下腫瘍 | 9 |
| 胃切除後症候群 | 7 |
| 胃アニサキス症 | 5 |
| 胃ポリープ | 4 |
| 消化性潰瘍 | 3 |
| 急性胃粘膜病変 | 3 |
| 胃・十二指腸憩室 | 3 |
| 胃静脈瘤 | 2 |
| 酸分泌抑制薬の長期使用 | 1 |
| 慢性胃炎 | 1 |
| 胃神経内分泌腫瘍 | 1 |

## source_class 別（原本の値。Phase 3 で Crossref により確定）

| source_class | 件数 |
|---|---|
| UNKNOWN | 56 |
| OPEN | 20 |
| RESTRICTED | 14 |
| GOV_JP | 5 |

## SRC 別の使用件数

| SRC | 件数 |
|---|---|
| SRC-017 | 1 |
| SRC-018 | 1 |
| SRC-028 | 18 |
| SRC-029 | 2 |
| SRC-030 | 23 |
| SRC-031 | 14 |
| SRC-032 | 8 |
| SRC-033 | 1 |
| SRC-034 | 1 |
| SRC-035 | 1 |
| SRC-036 | 1 |
| SRC-037 | 1 |
| SRC-038 | 1 |
| SRC-039 | 1 |
| SRC-040 | 6 |
| SRC-041 | 3 |
| SRC-042 | 2 |
| SRC-043 | 3 |
| SRC-044 | 3 |
| SRC-045 | 1 |
| SRC-046 | 2 |
| SRC-047 | 1 |
