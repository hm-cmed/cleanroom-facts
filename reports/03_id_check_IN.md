# Phase 3：識別子とライセンスの照合（2026-10-13、対象 IN）

生成：`scripts/verify_ids.py`。API 応答は `.cache/`（git 管理外）。

## 1. 概要

- 照合したカード：88 件（retired を除く）
- DOI を Crossref で解決：58 件
- 識別子を API で補完：78 件
- 食い違い：0 件
- source_class の判定差：38 件
- unresolved（API 失敗）：0 件
- 識別子なしで候補を出したもの：0 件

## 2. 食い違い（書き換えていない）

| ID | 項目 | 既存値 | API の値 | 内容 |
|---|---|---|---|---|
| — | | | | なし |

## 3. source_class の判定差

| ID | 既存 | Crossref の判定 | license URL |
|---|---|---|---|
| IN-001 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-002 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-003 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-004 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-005 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-006 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-007 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-008 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-009 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-010 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-017 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-018 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-019 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-020 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-021 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-022 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-023 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-024 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-025 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-026 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-036 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-037 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-038 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-039 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-040 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-041 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-042 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-043 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-044 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-045 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-046 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-047 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-048 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-049 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-050 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-051 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-052 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| IN-053 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |

ES・GD・IN は人間の委任により判定値を反映済み。HP・UG はレポートのみ。

## 4. API で補完した識別子

| ID | 項目 | 値 | 経路 |
|---|---|---|---|
| IN-001 | pmid | 33885977 | DOI 10.1007/s00535-021-01784-1 |
| IN-001 | pmcid | PMC8137635 | DOI 10.1007/s00535-021-01784-1 |
| IN-002 | pmid | 33885977 | DOI 10.1007/s00535-021-01784-1 |
| IN-002 | pmcid | PMC8137635 | DOI 10.1007/s00535-021-01784-1 |
| IN-003 | pmid | 33885977 | DOI 10.1007/s00535-021-01784-1 |
| IN-003 | pmcid | PMC8137635 | DOI 10.1007/s00535-021-01784-1 |
| IN-004 | pmid | 33885977 | DOI 10.1007/s00535-021-01784-1 |
| IN-004 | pmcid | PMC8137635 | DOI 10.1007/s00535-021-01784-1 |
| IN-005 | pmid | 33885977 | DOI 10.1007/s00535-021-01784-1 |
| IN-005 | pmcid | PMC8137635 | DOI 10.1007/s00535-021-01784-1 |
| IN-006 | pmid | 33885977 | DOI 10.1007/s00535-021-01784-1 |
| IN-006 | pmcid | PMC8137635 | DOI 10.1007/s00535-021-01784-1 |
| IN-007 | pmid | 33885977 | DOI 10.1007/s00535-021-01784-1 |
| IN-007 | pmcid | PMC8137635 | DOI 10.1007/s00535-021-01784-1 |
| IN-008 | pmid | 33885977 | DOI 10.1007/s00535-021-01784-1 |
| IN-008 | pmcid | PMC8137635 | DOI 10.1007/s00535-021-01784-1 |
| IN-009 | pmid | 33885977 | DOI 10.1007/s00535-021-01784-1 |
| IN-009 | pmcid | PMC8137635 | DOI 10.1007/s00535-021-01784-1 |
| IN-010 | pmid | 33885977 | DOI 10.1007/s00535-021-01784-1 |
| IN-010 | pmcid | PMC8137635 | DOI 10.1007/s00535-021-01784-1 |
| IN-017 | pmid | 33538894 | DOI 10.1007/s00535-020-01746-z |
| IN-017 | pmcid | PMC7932982 | DOI 10.1007/s00535-020-01746-z |
| IN-018 | pmid | 33538894 | DOI 10.1007/s00535-020-01746-z |
| IN-018 | pmcid | PMC7932982 | DOI 10.1007/s00535-020-01746-z |
| IN-019 | pmid | 33538894 | DOI 10.1007/s00535-020-01746-z |
| IN-019 | pmcid | PMC7932982 | DOI 10.1007/s00535-020-01746-z |
| IN-020 | pmid | 33538894 | DOI 10.1007/s00535-020-01746-z |
| IN-020 | pmcid | PMC7932982 | DOI 10.1007/s00535-020-01746-z |
| IN-021 | pmid | 33538894 | DOI 10.1007/s00535-020-01746-z |
| IN-021 | pmcid | PMC7932982 | DOI 10.1007/s00535-020-01746-z |
| IN-022 | pmid | 33538894 | DOI 10.1007/s00535-020-01746-z |
| IN-022 | pmcid | PMC7932982 | DOI 10.1007/s00535-020-01746-z |
| IN-023 | pmid | 33538894 | DOI 10.1007/s00535-020-01746-z |
| IN-023 | pmcid | PMC7932982 | DOI 10.1007/s00535-020-01746-z |
| IN-024 | pmid | 33538894 | DOI 10.1007/s00535-020-01746-z |
| IN-024 | pmcid | PMC7932982 | DOI 10.1007/s00535-020-01746-z |
| IN-025 | pmid | 33538894 | DOI 10.1007/s00535-020-01746-z |
| IN-025 | pmcid | PMC7932982 | DOI 10.1007/s00535-020-01746-z |
| IN-026 | pmid | 33538894 | DOI 10.1007/s00535-020-01746-z |
| IN-026 | pmcid | PMC7932982 | DOI 10.1007/s00535-020-01746-z |
| IN-027 | pmcid | PMC11825134 | DOI 10.1159/000540912 |
| IN-028 | pmcid | PMC11825134 | DOI 10.1159/000540912 |
| IN-029 | pmcid | PMC11825134 | DOI 10.1159/000540912 |
| IN-030 | pmcid | PMC11825134 | DOI 10.1159/000540912 |
| IN-031 | pmcid | PMC11825134 | DOI 10.1159/000540912 |
| IN-032 | pmcid | PMC11825134 | DOI 10.1159/000540912 |
| IN-033 | pmcid | PMC11825134 | DOI 10.1159/000540912 |
| IN-034 | pmcid | PMC11825134 | DOI 10.1159/000540912 |
| IN-035 | pmcid | PMC11825134 | DOI 10.1159/000540912 |
| IN-036 | pmid | 33710392 | DOI 10.1007/s00535-021-01776-1 |
| IN-037 | pmid | 33710392 | DOI 10.1007/s00535-021-01776-1 |
| IN-038 | pmid | 33710392 | DOI 10.1007/s00535-021-01776-1 |
| IN-039 | pmid | 33710392 | DOI 10.1007/s00535-021-01776-1 |
| IN-040 | pmid | 33710392 | DOI 10.1007/s00535-021-01776-1 |
| IN-041 | pmid | 33710392 | DOI 10.1007/s00535-021-01776-1 |
| IN-042 | pmid | 33710392 | DOI 10.1007/s00535-021-01776-1 |
| IN-043 | pmid | 33710392 | DOI 10.1007/s00535-021-01776-1 |
| IN-044 | pmid | 33710392 | DOI 10.1007/s00535-021-01776-1 |
| IN-045 | pmid | 33710392 | DOI 10.1007/s00535-021-01776-1 |
| IN-046 | pmid | 41186794 | DOI 10.1007/s10147-025-02899-8 |
| IN-047 | pmid | 41186794 | DOI 10.1007/s10147-025-02899-8 |
| IN-048 | pmid | 41186794 | DOI 10.1007/s10147-025-02899-8 |
| IN-049 | pmid | 41186794 | DOI 10.1007/s10147-025-02899-8 |
| IN-050 | pmid | 41186794 | DOI 10.1007/s10147-025-02899-8 |
| IN-051 | pmid | 41186794 | DOI 10.1007/s10147-025-02899-8 |
| IN-052 | pmid | 41186794 | DOI 10.1007/s10147-025-02899-8 |
| IN-053 | pmid | 41186794 | DOI 10.1007/s10147-025-02899-8 |
| IN-060 | pmid | 30625484 | DOI 10.1159/000495282 |
| IN-061 | pmid | 30625484 | DOI 10.1159/000495282 |
| IN-062 | pmid | 30625484 | DOI 10.1159/000495282 |
| IN-063 | pmid | 30625484 | DOI 10.1159/000495282 |
| IN-064 | pmid | 30625484 | DOI 10.1159/000495282 |
| IN-065 | pmid | 30625484 | DOI 10.1159/000495282 |
| IN-066 | pmid | 30625484 | DOI 10.1159/000495282 |
| IN-067 | pmid | 30625484 | DOI 10.1159/000495282 |
| IN-068 | pmid | 30625484 | DOI 10.1159/000495282 |
| IN-069 | pmid | 30625484 | DOI 10.1159/000495282 |
| IN-084 | pmid | 34164674 | DOI 10.1093/cid/ciab549 |

## 5. unresolved

なし

## 6. カードごとの結果

| ID | DOI解決 | PMID一致 | license | notes |
|---|---|---|---|---|
| IN-001 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-002 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-003 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-004 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-005 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-006 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-007 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-008 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-009 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-010 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-011 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-012 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-013 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-014 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-015 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-016 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-017 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-018 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-019 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-020 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-021 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-022 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-023 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-024 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-025 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-026 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-027 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| IN-028 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| IN-029 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| IN-030 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| IN-031 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| IN-032 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| IN-033 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| IN-034 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| IN-035 | True | True | https://creativecommons.org/licenses/by-nc/4.0/ |  |
| IN-036 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-037 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-038 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-039 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-040 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-041 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-042 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-043 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-044 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-045 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-046 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-047 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-048 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-049 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-050 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-051 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-052 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-053 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| IN-054 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-055 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-056 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-057 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-058 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-059 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-060 | True | True | https://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| IN-061 | True | True | https://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| IN-062 | True | True | https://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| IN-063 | True | True | https://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| IN-064 | True | True | https://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| IN-065 | True | True | https://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| IN-066 | True | True | https://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| IN-067 | True | True | https://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| IN-068 | True | True | https://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| IN-069 | True | True | https://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| IN-070 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-071 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-072 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-073 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-074 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-075 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-076 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-077 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-078 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-079 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-080 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-081 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-082 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-083 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-084 | True | True | https://academic.oup.com/journals/pages/open_access/funder_policies/chorus/standard_publication_model |  |
| IN-085 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-086 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-087 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| IN-088 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
