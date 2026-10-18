# Phase 1：取り込みレポート（XS、2026-10-18）

生成：`scripts/ingest_round.py raw/07_cross_sectional.md XS`。主張文と数値は変更していない。

- 結果：書き込み済み
- カード：37件（XS-001〜XS-037）、欠番：なし
- スキーマ違反：0件
- 出典マスター：新規 7件（SRC-163, SRC-164, SRC-165, SRC-166, SRC-167, SRC-168, SRC-169）、既存の再利用 0件（）
- uncertainty に記載のあるカード：14件

## 形式の検査

問題なし（脚注マーカー・アンカー・basis_tag・仮ID・verifier の設定はない）

## subdomain 別

| subdomain | 件数 |
|---|---|
| 急性下部消化管出血 | 8 |
| 鉄欠乏性貧血と消化管の精査 | 7 |
| 肝機能検査値の異常と黄疸 | 7 |
| 抗血栓薬服用者の内視鏡 | 6 |
| 周術期の栄養管理 | 4 |
| 低栄養の診断（GLIM） | 3 |
| 大腸内視鏡の質の指標 | 2 |

## source_class 別（原本の値。Phase 3 で Crossref により確定）

| source_class | 件数 |
|---|---|
| RESTRICTED | 24 |
| OPEN | 7 |
| UNKNOWN | 6 |

## SRC 別の使用件数

| SRC | 件数 |
|---|---|
| SRC-163 | 8 |
| SRC-164 | 7 |
| SRC-165 | 6 |
| SRC-166 | 7 |
| SRC-167 | 2 |
| SRC-168 | 3 |
| SRC-169 | 4 |
