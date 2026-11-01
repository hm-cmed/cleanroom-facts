# Phase 1：取り込みレポート（IN,LV,AB,MP,DV,FT,SA,HF,PE,NL,SK,ND、2026-11-01）

生成：`scripts/ingest_round.py raw/61_brushup.md IN,LV,AB,MP,DV,FT,SA,HF,PE,NL,SK,ND`。主張文と数値は変更していない。

- 結果：書き込み済み
- カード：26件（IN-111〜IN-113、LV-111〜LV-111、AB-116〜AB-116、MP-040〜MP-042、DV-021〜DV-022、FT-015〜FT-016、SA-021〜SA-022、HF-030〜HF-031、PE-038〜PE-040、NL-022〜NL-022、SK-033〜SK-033、ND-057〜ND-061）、欠番：なし
- スキーマ違反：0件
- 出典マスター：新規 10件（SRC-4441, SRC-4442, SRC-4443, SRC-4444, SRC-4445, SRC-4446, SRC-4447, SRC-4448, SRC-4449, SRC-4450）、既存の再利用 9件（SRC-185, SRC-2825, SRC-3092, SRC-3348, SRC-4214, SRC-4215, SRC-4226, SRC-4227, SRC-4433）
- uncertainty に記載のあるカード：26件

## 形式の検査

問題なし（脚注マーカー・アンカー・basis_tag・仮ID・verifier の設定はない）

## subdomain 別

| subdomain | 件数 |
|---|---|
| 多発性硬化症 | 5 |
| 心臓外傷 | 3 |
| 注意欠如多動性障害<注意欠如多動症><ADHD> | 2 |
| 胎児貧血 | 2 |
| 反応性関節炎 | 2 |
| 右心不全 | 2 |
| 先天性食道閉鎖症 | 2 |
| 放射線性腸炎 | 1 |
| 小腸癌 | 1 |
| 毛細血管拡張症 | 1 |
| 肝囊胞 | 1 |
| 後腹膜腫瘍 | 1 |
| 鼠径ヘルニア | 1 |
| 鼻炎 | 1 |
| 遺伝性血管性浮腫 | 1 |

## source_class 別（原本の値。Phase 3 で Crossref により確定）

| source_class | 件数 |
|---|---|
| RESTRICTED | 25 |
| UNKNOWN | 1 |

## SRC 別の使用件数

| SRC | 件数 |
|---|---|
| SRC-185 | 2 |
| SRC-2825 | 1 |
| SRC-3092 | 1 |
| SRC-3348 | 1 |
| SRC-4214 | 1 |
| SRC-4215 | 1 |
| SRC-4226 | 1 |
| SRC-4227 | 1 |
| SRC-4433 | 5 |
| SRC-4441 | 1 |
| SRC-4442 | 1 |
| SRC-4443 | 1 |
| SRC-4444 | 1 |
| SRC-4445 | 2 |
| SRC-4446 | 1 |
| SRC-4447 | 2 |
| SRC-4448 | 1 |
| SRC-4449 | 1 |
| SRC-4450 | 1 |
