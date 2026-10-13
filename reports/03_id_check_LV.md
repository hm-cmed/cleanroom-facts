# Phase 3：識別子とライセンスの照合（2026-10-13、対象 LV）

生成：`scripts/verify_ids.py`。API 応答は `.cache/`（git 管理外）。

## 1. 概要

- 照合したカード：104 件（retired を除く）
- DOI を Crossref で解決：44 件
- 識別子を API で補完：47 件
- 食い違い：0 件
- source_class の判定差：22 件
- unresolved（API 失敗）：0 件
- 識別子なしで候補を出したもの：12 件

## 2. 食い違い（書き換えていない）

| ID | 項目 | 既存値 | API の値 | 内容 |
|---|---|---|---|---|
| — | | | | なし |

## 3. source_class の判定差

| ID | 既存 | Crossref の判定 | license URL |
|---|---|---|---|
| LV-001 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-002 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-003 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-004 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-005 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-006 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-007 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-008 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-009 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-010 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-011 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-012 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-013 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-014 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-015 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-016 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-017 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-018 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-019 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-020 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-021 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| LV-022 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |

ES・GD・IN・LV は人間の委任により判定値を反映済み。HP・UG はレポートのみ。

## 4. API で補完した識別子

| ID | 項目 | 値 | 経路 |
|---|---|---|---|
| LV-001 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-002 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-003 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-004 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-005 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-006 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-007 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-008 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-009 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-010 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-011 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-012 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-013 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-014 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-015 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-016 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-017 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-018 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-019 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-020 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-021 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-022 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| LV-023 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-024 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-025 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-026 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-027 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-028 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-029 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-030 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-031 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-032 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-033 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-034 | pmid | 34533632 | DOI 10.1007/s00535-021-01796-x |
| LV-035 | pmid | 37364790 | DOI 10.1016/j.jhep.2023.06.003 |
| LV-036 | pmid | 37364790 | DOI 10.1016/j.jhep.2023.06.003 |
| LV-037 | pmid | 37364790 | DOI 10.1016/j.jhep.2023.06.003 |
| LV-068 | pmid | 22825549 | DOI 10.1007/s00535-012-0624-x |
| LV-069 | pmid | 22825549 | DOI 10.1007/s00535-012-0624-x |
| LV-070 | pmid | 22825549 | DOI 10.1007/s00535-012-0624-x |
| LV-071 | pmid | 22825549 | DOI 10.1007/s00535-012-0624-x |
| LV-095 | pmid | 19058303 | DOI 10.3748/wjg.14.6774 |
| LV-095 | pmcid | PMC2773872 | DOI 10.3748/wjg.14.6774 |
| LV-096 | pmid | 19058303 | DOI 10.3748/wjg.14.6774 |
| LV-096 | pmcid | PMC2773872 | DOI 10.3748/wjg.14.6774 |
| LV-097 | pmid | 19058303 | DOI 10.3748/wjg.14.6774 |
| LV-097 | pmcid | PMC2773872 | DOI 10.3748/wjg.14.6774 |

## 5. unresolved

なし

## 6. カードごとの結果

| ID | DOI解決 | PMID一致 | license | notes |
|---|---|---|---|---|
| LV-001 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-002 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-003 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-004 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-005 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-006 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-007 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-008 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-009 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-010 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-011 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-012 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-013 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-014 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-015 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-016 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-017 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-018 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-019 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-020 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-021 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-022 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-023 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-024 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-025 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-026 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-027 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-028 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-029 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-030 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-031 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-032 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-033 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-034 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| LV-035 | True | True | http://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| LV-036 | True | True | http://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| LV-037 | True | True | http://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| LV-038 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-039 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-040 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-041 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-042 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-043 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-044 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-045 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-046 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-047 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-048 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-049 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| LV-050 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-051 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-052 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-053 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-054 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-055 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-056 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-057 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-058 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-059 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-060 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-061 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-062 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-063 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-064 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-065 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-066 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-067 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-068 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| LV-069 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| LV-070 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| LV-071 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| LV-072 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-073 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-074 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-075 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-076 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-077 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-078 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-079 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-080 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-081 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-082 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-083 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-084 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-085 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-086 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-087 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-088 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-089 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-090 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-091 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-092 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-093 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-094 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-095 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| LV-096 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| LV-097 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| LV-098 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-099 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-100 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-101 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-102 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-103 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| LV-104 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
