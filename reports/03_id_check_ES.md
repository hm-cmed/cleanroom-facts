# Phase 3：識別子とライセンスの照合（2026-10-12、対象 ES）

生成：`scripts/verify_ids.py`。API 応答は `.cache/`（git 管理外）。

## 1. 概要

- 照合したカード：83 件（retired を除く）
- DOI を Crossref で解決：69 件
- 識別子を API で補完：54 件
- 食い違い：1 件
- source_class の判定差：8 件
- unresolved（API 失敗）：0 件
- 識別子なしで候補を出したもの：6 件

## 2. 食い違い（書き換えていない）

| ID | 項目 | 既存値 | API の値 | 内容 |
|---|---|---|---|---|
| ES-054 | pmid | 34454674 | 41259897 | DOI 10.1016/j.esmoop.2025.105854 から得た値と既存値が異なる。書き換えていない |

## 3. source_class の判定差

| ID | 既存 | Crossref の判定 | license URL |
|---|---|---|---|
| ES-020 | UNKNOWN | RESTRICTED | https://creativecommons.org/licenses/by-nc/4.0/ |
| ES-029 | UNKNOWN | RESTRICTED | http://onlinelibrary.wiley.com/termsAndConditions#vor |
| ES-031 | UNKNOWN | RESTRICTED | http://onlinelibrary.wiley.com/termsAndConditions#vor |
| ES-066 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| ES-074 | OPEN | RESTRICTED | http://www.springer.com/tdm |
| ES-079 | UNKNOWN | RESTRICTED | http://creativecommons.org/licenses/by-nc-nd/4.0/ |
| ES-080 | UNKNOWN | RESTRICTED | http://creativecommons.org/licenses/by-nc/4.0 |
| ES-081 | UNKNOWN | RESTRICTED | http://creativecommons.org/licenses/by-nc/4.0 |

ES は人間の委任により判定値を反映済み。HP・UG はレポートのみ。

## 4. API で補完した識別子

| ID | 項目 | 値 | 経路 |
|---|---|---|---|
| ES-001 | pmid | 35226174 | DOI 10.1007/s00535-022-01861-z |
| ES-002 | pmid | 35226174 | DOI 10.1007/s00535-022-01861-z |
| ES-003 | pmid | 35226174 | DOI 10.1007/s00535-022-01861-z |
| ES-004 | pmid | 35226174 | DOI 10.1007/s00535-022-01861-z |
| ES-006 | pmid | 35226174 | DOI 10.1007/s00535-022-01861-z |
| ES-007 | pmid | 35226174 | DOI 10.1007/s00535-022-01861-z |
| ES-009 | pmid | 37734911 | DOI 10.1136/gutjnl-2023-330616 |
| ES-009 | pmcid | PMC10846564 | DOI 10.1136/gutjnl-2023-330616 |
| ES-010 | pmid | 35226174 | DOI 10.1007/s00535-022-01861-z |
| ES-011 | pmid | 35226174 | DOI 10.1007/s00535-022-01861-z |
| ES-013 | pmid | 35354777 | DOI 10.14309/ajg.0000000000001680 |
| ES-013 | pmcid | PMC10259184 | DOI 10.14309/ajg.0000000000001680 |
| ES-014 | pmid | 35354777 | DOI 10.14309/ajg.0000000000001680 |
| ES-014 | pmcid | PMC10259184 | DOI 10.14309/ajg.0000000000001680 |
| ES-016 | pmid | 35354777 | DOI 10.14309/ajg.0000000000001680 |
| ES-016 | pmcid | PMC10259184 | DOI 10.14309/ajg.0000000000001680 |
| ES-017 | pmid | 35354777 | DOI 10.14309/ajg.0000000000001680 |
| ES-017 | pmcid | PMC10259184 | DOI 10.14309/ajg.0000000000001680 |
| ES-018 | pmid | 39745304 | DOI 10.14309/ajg.0000000000003194 |
| ES-020 | doi | 10.5415/apallergy.2020.10.e16 | PMID 32411581 の esummary |
| ES-020 | pmcid | PMC7203441 | DOI 10.5415/apallergy.2020.10.e16 |
| ES-022 | pmid | 39745304 | DOI 10.14309/ajg.0000000000003194 |
| ES-029 | pmid | 33373111 | PMCID PMC8034247 |
| ES-029 | doi | 10.1111/nmo.14058 | PMCID PMC8034247 |
| ES-031 | pmid | 33373111 | PMCID PMC8034247 |
| ES-031 | doi | 10.1111/nmo.14058 | PMCID PMC8034247 |
| ES-033 | pmid | 31800987 | DOI 10.1056/NEJMoa1905380 |
| ES-046 | pmid | 32072683 | DOI 10.1111/den.13654 |
| ES-050 | pmid | 38876133 | DOI 10.1016/S0140-6736(24)00745-1 |
| ES-051 | pmid | 33789008 | DOI 10.1056/NEJMoa2032125 |
| ES-052 | pmid | 35108470 | DOI 10.1056/NEJMoa2111380 |
| ES-053 | pmid | 34454674 | DOI 10.1016/S0140-6736(21)01234-4 |
| ES-054 | pmcid | PMC12670541 | DOI 10.1016/j.esmoop.2025.105854 |
| ES-062 | pmcid | PMC11090185 | DOI 10.1016/j.jhep.2021.12.022 |
| ES-064 | pmcid | PMC11090185 | DOI 10.1016/j.jhep.2021.12.022 |
| ES-065 | doi | 10.1056/NEJMoa0910102 | PMID 20573925 の esummary |
| ES-066 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| ES-074 | pmid | 18655708 | PMCID PMC2533005 |
| ES-074 | doi | 10.1186/1471-230X-8-31 | PMCID PMC2533005 |
| ES-079 | pmid | 33005566 | PMCID PMC7519373 |
| ES-079 | doi | 10.1016/j.idcr.2020.e00925 | PMCID PMC7519373 |
| ES-080 | pmid | 31169688 | DOI 10.1097/MD.0000000000015845 |
| ES-080 | pmcid | PMC6571398 | DOI 10.1097/MD.0000000000015845 |
| ES-081 | pmid | 31169688 | DOI 10.1097/MD.0000000000015845 |
| ES-081 | pmcid | PMC6571398 | DOI 10.1097/MD.0000000000015845 |
| ES-085 | pmid | 41095682 | PMCID PMC12524210 |
| ES-085 | doi | 10.3390/diagnostics15192463 | PMCID PMC12524210 |
| ES-086 | pmid | 41095682 | PMCID PMC12524210 |
| ES-086 | doi | 10.3390/diagnostics15192463 | PMCID PMC12524210 |
| ES-087 | pmid | 41095682 | PMCID PMC12524210 |
| ES-087 | doi | 10.3390/diagnostics15192463 | PMCID PMC12524210 |
| ES-089 | pmid | 32072683 | DOI 10.1111/den.13654 |
| ES-092 | pmid | 19320537 | DOI 10.1371/journal.pmed.1000050 |
| ES-092 | pmcid | PMC2659709 | DOI 10.1371/journal.pmed.1000050 |

## 5. unresolved

なし

## 6. カードごとの結果

| ID | DOI解決 | PMID一致 | license | notes |
|---|---|---|---|---|
| ES-001 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-002 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-003 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-004 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-005 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| ES-006 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-007 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| ES-008 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
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
| ES-019 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| ES-020 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| ES-021 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| ES-022 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-023 | True | True | http://www.nejmgroup.org/legal/terms-of-use.htm |  |
| ES-024 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| ES-025 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-026 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-027 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-028 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-029 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-030 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor |  |
| ES-031 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor | source は略記。同じ文献（DOI 10.1111/nmo.14058）を ES-025 で書誌照合済み／source は略記。同じ DOI を ES-025 で書誌照合済み |
| ES-032 | True | True | http://www.nejmgroup.org/legal/terms-of-use.htm |  |
| ES-033 | True | True | http://www.nejmgroup.org/legal/terms-of-use.htm |  |
| ES-034 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
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
| ES-054 | True | False | http://creativecommons.org/licenses/by-nc-nd/4.0/ | pmid 食い違い：既存 34454674／API 41259897 |
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
| ES-067 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| ES-069 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| ES-070 | True | True | — | source は略記。同じ DOI を ES-069 で書誌照合済み／Crossrefに license の記載なし（source_class は現状維持） |
| ES-071 | True | True | — | source は略記。同じ DOI を ES-069 で書誌照合済み／Crossrefに license の記載なし（source_class は現状維持） |
| ES-072 | True | True | — | source は略記。同じ DOI を ES-069 で書誌照合済み／Crossrefに license の記載なし（source_class は現状維持） |
| ES-073 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| ES-074 | True | True | http://www.springer.com/tdm |  |
| ES-075 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| ES-079 | True | True | http://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| ES-080 | True | True | http://creativecommons.org/licenses/by-nc/4.0 |  |
| ES-081 | True | True | http://creativecommons.org/licenses/by-nc/4.0 |  |
| ES-085 | True | True | https://creativecommons.org/licenses/by/4.0/ |  |
| ES-086 | True | True | https://creativecommons.org/licenses/by/4.0/ |  |
| ES-087 | True | True | https://creativecommons.org/licenses/by/4.0/ |  |
| ES-089 | True | True | http://onlinelibrary.wiley.com/termsAndConditions#vor | source は略記。同じ DOI を ES-046 で書誌照合済み |
| ES-090 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| ES-091 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| ES-092 | True | True | https://creativecommons.org/publicdomain/zero/1.0/ |  |
| ES-093 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
