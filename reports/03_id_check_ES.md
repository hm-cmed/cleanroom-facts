# Phase 3：識別子とライセンスの照合（2026-10-12、対象 ES）

生成：`scripts/verify_ids.py`。API 応答は `.cache/`（git 管理外）。

## 1. 概要

- 照合したカード：89 件（retired を除く）
- DOI を Crossref で解決：82 件
- 識別子を API で補完：0 件
- 食い違い：1 件
- source_class の判定差：0 件
- unresolved（API 失敗）：0 件
- 識別子なしで候補を出したもの：2 件

## 2. 食い違い（書き換えていない）

| ID | 項目 | 既存値 | API の値 | 内容 |
|---|---|---|---|---|
| ES-077 | doi | 10.22037/ghfbb.v15i3.2591 | Crossref 404 | DOI が実在しない可能性 |

## 3. source_class の判定差

| ID | 既存 | Crossref の判定 | license URL |
|---|---|---|---|
| — | | | なし |

ES は人間の委任により判定値を反映済み。HP・UG はレポートのみ。

## 4. API で補完した識別子

| ID | 項目 | 値 | 経路 |
|---|---|---|---|
| — | | | なし |

## 5. unresolved

なし

## 6. カードごとの結果

| ID | DOI解決 | PMID一致 | license | notes |
|---|---|---|---|---|
| ES-001 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-002 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-003 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-004 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-005 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-006 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-007 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-008 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-009 | True | True | http://creativecommons.org/licenses/by-nc/4.0/ |  |
| ES-010 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-011 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-012 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-013 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-014 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-015 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-016 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-017 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-018 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-019 | True | True | https://www.elsevier.com/tdm/userlicense/1.0/ |  |
| ES-020 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| ES-021 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-022 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-023 | True | True | http://www.nejmgroup.org/legal/terms-of-use.htm |  |
| ES-024 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| ES-025 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-026 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-027 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-028 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-029 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-030 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-031 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor | source は略記。同じ DOI を ES-025 で書誌照合済み |
| ES-032 | True | True | http://www.nejmgroup.org/legal/terms-of-use.htm |  |
| ES-033 | True | True | http://www.nejmgroup.org/legal/terms-of-use.htm |  |
| ES-034 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-035 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| ES-037 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-038 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-039 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-040 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-041 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-043 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-044 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-045 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-046 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-047 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-048 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-049 | True | True | https://www.elsevier.com/tdm/userlicense/1.0/ |  |
| ES-050 | True | True | https://www.elsevier.com/tdm/userlicense/1.0/ |  |
| ES-051 | True | True | http://www.nejmgroup.org/legal/terms-of-use.htm |  |
| ES-052 | True | True | http://www.nejmgroup.org/legal/terms-of-use.htm |  |
| ES-053 | True | True | https://www.elsevier.com/tdm/userlicense/1.0/ |  |
| ES-054 | True | True | http://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| ES-055 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-056 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-057 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-058 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-059 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-060 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-061 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| ES-062 | True | True | https://www.elsevier.com/tdm/userlicense/1.0/ |  |
| ES-063 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-064 | True | True | https://www.elsevier.com/tdm/userlicense/1.0/ |  |
| ES-065 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-066 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-069 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-070 | True | True | — | source は略記。同じ DOI を ES-069 で書誌照合済み／Crossrefに license の記載なし（source_class は現状維持） |
| ES-071 | True | True | — | source は略記。同じ DOI を ES-069 で書誌照合済み／Crossrefに license の記載なし（source_class は現状維持） |
| ES-072 | True | True | — | source は略記。同じ DOI を ES-069 で書誌照合済み／Crossrefに license の記載なし（source_class は現状維持） |
| ES-073 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-074 | True | True | http://www.springer.com/tdm |  |
| ES-075 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-076 | True | True | https://www.elsevier.com/tdm/userlicense/1.0/ |  |
| ES-077 | False | None | — | Crossref で DOI 10.22037/ghfbb.v15i3.2591 が見つからない |
| ES-078 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-079 | True | True | http://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| ES-080 | True | True | http://creativecommons.org/licenses/by-nc/4.0 |  |
| ES-081 | True | True | http://creativecommons.org/licenses/by-nc/4.0 |  |
| ES-082 | True | True | http://creativecommons.org/licenses/by/2.0 |  |
| ES-083 | True | True | https://creativecommons.org/licenses/by/4.0/ |  |
| ES-084 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-085 | True | True | https://creativecommons.org/licenses/by/4.0/ |  |
| ES-086 | True | True | https://creativecommons.org/licenses/by/4.0/ |  |
| ES-087 | True | True | https://creativecommons.org/licenses/by/4.0/ |  |
| ES-088 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-089 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor | source は略記。同じ DOI を ES-046 で書誌照合済み |
| ES-090 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| ES-091 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| ES-092 | True | True | https://creativecommons.org/publicdomain/zero/1.0/ |  |
| ES-093 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
