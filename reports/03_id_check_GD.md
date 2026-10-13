# Phase 3：識別子とライセンスの照合（2026-10-13、対象 GD）

生成：`scripts/verify_ids.py`。API 応答は `.cache/`（git 管理外）。

## 1. 概要

- 照合したカード：95 件（retired を除く）
- DOI を Crossref で解決：85 件
- 識別子を API で補完：110 件
- 食い違い：0 件
- source_class の判定差：53 件
- unresolved（API 失敗）：0 件
- 識別子なしで候補を出したもの：4 件

## 2. 食い違い（書き換えていない）

| ID | 項目 | 既存値 | API の値 | 内容 |
|---|---|---|---|---|
| — | | | | なし |

## 3. source_class の判定差

| ID | 既存 | Crossref の判定 | license URL |
|---|---|---|---|
| GD-001 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-002 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-003 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-004 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-005 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-006 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-007 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-008 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-009 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-010 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-011 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-012 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-013 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-014 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-015 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-016 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-017 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-018 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-035 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-036 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-037 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-038 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-039 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-040 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-041 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-042 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-043 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-044 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-045 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-046 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-047 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-048 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-049 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-050 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-051 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-052 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-053 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-054 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-058 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-059 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-060 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-061 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-062 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-063 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-064 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-065 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-066 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-067 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-068 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-070 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-071 | UNKNOWN | RESTRICTED | http://creativecommons.org/licenses/by-nc-nd/4.0/ |
| GD-073 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |
| GD-080 | UNKNOWN | OPEN | https://creativecommons.org/licenses/by/4.0 |

ES・GD は人間の委任により判定値を反映済み。HP・UG はレポートのみ。

## 4. API で補完した識別子

| ID | 項目 | 値 | 経路 |
|---|---|---|---|
| GD-001 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-002 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-003 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-004 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-005 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-006 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-007 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-008 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-009 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-010 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-011 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-012 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-013 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-014 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-015 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-016 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-017 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-018 | pmid | 35061057 | DOI 10.1007/s00535-021-01843-7 |
| GD-019 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-019 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-020 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-020 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-021 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-021 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-022 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-022 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-023 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-023 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-024 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-024 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-025 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-025 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-026 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-026 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-027 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-027 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-028 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-028 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-029 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-029 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-030 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-030 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-031 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-031 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-032 | pmid | 42635735 | DOI 10.1007/s00535-026-02504-3 |
| GD-032 | pmcid | PMC13615929 | DOI 10.1007/s00535-026-02504-3 |
| GD-035 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-035 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-036 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-036 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-037 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-037 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-038 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-038 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-039 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-039 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-040 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-040 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-041 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-041 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-042 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-042 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-043 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-043 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-044 | pmid | 36342574 | DOI 10.1007/s10120-022-01331-8 |
| GD-045 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-045 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-046 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-046 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-047 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-047 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-048 | pmid | 36342574 | DOI 10.1007/s10120-022-01331-8 |
| GD-049 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-049 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-050 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-050 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-051 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-051 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-052 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-052 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-053 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-053 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-054 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-054 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-055 | pmcid | PMC8436782 | DOI 10.1016/S0140-6736(21)00797-2 |
| GD-058 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-058 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-059 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-059 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-060 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-060 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-061 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-061 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-071 | pmid | 37401795 | DOI 10.1111/jne.13306 |
| GD-073 | pmid | 34231046 | DOI 10.1007/s00535-021-01788-x |
| GD-074 | pmid | 32457534 | DOI 10.1038/s41574-020-0357-5 |
| GD-075 | pmid | 32457534 | DOI 10.1038/s41574-020-0357-5 |
| GD-076 | pmid | 32457534 | DOI 10.1038/s41574-020-0357-5 |
| GD-077 | pmid | 32457534 | DOI 10.1038/s41574-020-0357-5 |
| GD-078 | pmid | 32457534 | DOI 10.1038/s41574-020-0357-5 |
| GD-079 | pmid | 32457534 | DOI 10.1038/s41574-020-0357-5 |
| GD-080 | pmid | 41569370 | DOI 10.1007/s10120-025-01698-4 |
| GD-080 | pmcid | PMC12956939 | DOI 10.1007/s10120-025-01698-4 |
| GD-084 | pmid | 36148963 | DOI 10.3201/eid2810.220627 |
| GD-085 | pmid | 36148963 | DOI 10.3201/eid2810.220627 |
| GD-092 | pmid | 38875111 | DOI 10.1056/NEJMoa2404245 |
| GD-093 | pmcid | PMC3066647 | DOI 10.4253/wjge.v3.i3.62 |
| GD-094 | pmcid | PMC3066647 | DOI 10.4253/wjge.v3.i3.62 |
| GD-095 | pmid | 42100946 | DOI 10.47717/turkjsurg.2026.2025-11-25 |
| GD-095 | pmcid | PMC13237573 | DOI 10.47717/turkjsurg.2026.2025-11-25 |

## 5. unresolved

なし

## 6. カードごとの結果

| ID | DOI解決 | PMID一致 | license | notes |
|---|---|---|---|---|
| GD-001 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-002 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-003 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-004 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-005 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-006 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-007 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-008 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-009 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-010 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-011 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-012 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-013 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-014 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-015 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-016 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-017 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-018 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-019 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-020 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-021 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-022 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-023 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-024 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-025 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-026 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-027 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-028 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-029 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-030 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-031 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-032 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-033 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| GD-034 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| GD-035 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-036 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-037 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-038 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-039 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-040 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-041 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-042 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-043 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-044 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-045 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-046 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-047 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-048 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-049 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-050 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-051 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-052 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-053 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-054 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-055 | True | True | https://www.elsevier.com/tdm/userlicense/1.0/ |  |
| GD-056 | True | True | https://www.elsevier.com/tdm/userlicense/1.0/ |  |
| GD-057 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| GD-058 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-059 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-060 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-061 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-062 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-063 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-064 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-065 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-066 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-067 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-068 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-069 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| GD-070 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-071 | True | True | http://creativecommons.org/licenses/by-nc-nd/4.0/ |  |
| GD-072 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| GD-073 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-074 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-075 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-076 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-077 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-078 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-079 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-080 | True | True | https://creativecommons.org/licenses/by/4.0 |  |
| GD-081 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| GD-082 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| GD-083 | False | None | — | 識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外 |
| GD-084 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| GD-085 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| GD-086 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| GD-087 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| GD-088 | False | None | — | 識別子なし。Crossref の候補 3 件を proposals/id_candidates.csv に出力 |
| GD-089 | True | None | — | DOI は JaLC 登録（Crossref の対象外）。doi.org で解決を確認（https://www.jstage.jst.go.jp/article/gee/67/4/67_281/_article/-char/ja/）。license は未確認（source_class は現状維持） |
| GD-090 | True | None | — | DOI は JaLC 登録（Crossref の対象外）。doi.org で解決を確認（https://www.jstage.jst.go.jp/article/gee/67/4/67_281/_article/-char/ja/）。license は未確認（source_class は現状維持） |
| GD-091 | True | None | — | DOI は JaLC 登録（Crossref の対象外）。doi.org で解決を確認（https://www.jstage.jst.go.jp/article/gee/67/4/67_281/_article/-char/ja/）。license は未確認（source_class は現状維持） |
| GD-092 | True | True | http://www.nejmgroup.org/legal/terms-of-use.htm |  |
| GD-093 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| GD-094 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
| GD-095 | True | True | — | Crossrefに license の記載なし（source_class は現状維持） |
