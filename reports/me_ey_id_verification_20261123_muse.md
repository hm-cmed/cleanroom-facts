# 文献番号の照合結果（ME・EY）― 2026-11-23

実施：こちらの環境から Crossref API・PubMed E-utilities で直接照合（レポジトリ側で実行できなかった --online 相当）。
対象：ME の出典 SRC-5101〜5133（ME1・ME2・ME3 の出典表）、EY の SRC-5035。

## 照合件数

| 区分 | 件数 | 内訳 |
|---|---|---|
| DOI を Crossref で照合 | 15件 | SRC-5108・5109・5110・5112・5113・5116・5117・5118・5119・5120・5121・5122・5123・5130・5131 |
| PMID を PubMed で照合 | 15件 | SRC-5108・5109・5111・5112・5113・5116・5117・5118・5119・5120・5121・5122・5123・5130・5131 |
| PMCID の存在確認 | 2件 | SRC-5119（PMC5855972）・SRC-5122（PMC5613659） |
| 識別子なし（照合対象外） | 17件 | SRC-5101〜5107・5114・5115・5124〜5129・5132・5133（政府文書・WHO文書・国内資料。DOI・PMID・PMCID の記載自体なし） |

## 結果（出典ごと）

| SRC | DOI（Crossref） | PMID（PubMed） | DOI↔PMID 同一論文 | 判定 |
|---|---|---|---|---|
| SRC-5108 Miller 1990 | 一致 | 一致 | 一致 | ✅ |
| SRC-5109 ten Cate 2005 | 一致 | 一致 | 一致 | ✅ |
| SRC-5110 ten Cate 2024（章） | 一致（著者5名・書名・2024・book-chapter） | 記載なし | ― | ✅ |
| SRC-5111 Ende 1983 | 記載なし（PubMed 側にも DOI 登録なし） | 一致 | ― | ✅ |
| SRC-5112 McGaghie 2011 | 一致 | 一致 | 一致 | ✅（注記あり） |
| SRC-5113 医師憲章 2002 | 一致（Crossref に著者欄なし。団体著者は PubMed で一致） | 一致 | 一致 | ✅ |
| SRC-5116 van der Vleuten 2012 | 一致 | 一致 | 一致 | ✅ |
| SRC-5117 Issenberg 2005 | 一致 | 一致 | 一致 | ✅ |
| SRC-5118 Albanese & Mitchell 1993 | **不一致（下記）** | 一致 | PubMed 内では一致 | ⚠️ |
| SRC-5119 Hew & Lo 2018 | 一致 | 一致（PMCID PMC5855972 も一致） | 一致 | ✅ |
| SRC-5120 Cook 2008 | 一致 | 一致 | 一致 | ✅ |
| SRC-5121 Steinert 2006 | 一致 | 一致 | 一致 | ✅ |
| SRC-5122 Rotenstein 2016 | 一致 | 一致（PMCID PMC5613659 も一致） | 一致 | ✅ |
| SRC-5123 West 2016 | 一致 | 一致 | 一致 | ✅ |
| SRC-5130 Driessen 2007 | 一致 | 一致 | 一致 | ✅ |
| SRC-5131 Fatmi 2013 | 一致 | 一致 | 一致 | ✅ |
| SRC-5035 Yang & Lin 2019（EY） | 同定・一致（下記） | 同定・一致（下記） | 一致 | ✅（識別子は未登録だった） |

## 不一致・注記

### ⚠️ SRC-5118（Albanese MA, Mitchell S. Problem-based learning. Acad Med. 1993;68(1):52-81）― DOI の向け先が別の論文

- 成果物の記載：DOI 10.1097/00001888-199301000-00012、PMID 8447896。
- PMID 8447896 の PubMed レコードは成果物の書誌と完全一致し、PubMed 自身もこの DOI を同レコードに付けている。
- しかし Crossref の同 DOI レコードは、同じ号の別論文 **Petersdorf RG「The Transition」Acad Med. 1993;68(1):44** で、doi.org の解決先も academic.oup.com の 68/1/44（44ページの論文）になる。
- すなわち、データベース側の旧来メタデータの食い違いで、DOI リンクをたどると Albanese 論文ではなく44ページの論説に着く。PMID の方（8447896）は正しい。取り込み側で DOI の扱い（残す／落とす）の判断を要する。

### 注記：SRC-5112（McGaghie 2011）― PMCID が実在するが成果物は「なし」

- PMID 21512370 の PubMed レコードには PMCID **PMC3102783** が付いている（著者原稿）。成果物の PMCID 欄は「なし（null）」で、記載値の誤りではないが、補完するかどうかは取り込み側の判断。

### SRC-5035（EY-063 の corroboration 出典）― 識別子を同定

- ローカル資料（EY.yaml の corroboration 文）には書誌のみで識別子の登録なし：Yang MC, Lin KY. J Curr Glaucoma Pract. 2019;13(3):104-109。
- PubMed 検索で1件のみ該当：**PMID 32435123**、"Drug-induced Acute Angle-closure Glaucoma: A Review"、Yang MC・Lin KY、J Curr Glaucoma Pract. 2019;13(3):104-109 ― 書誌は完全一致。
- 同レコードの識別子：**DOI 10.5005/jp-journals-10078-1261**、**PMCID PMC7221246**。Crossref の書誌検索でも同一 DOI・同一書誌を確認。

## まとめ

- 照合した識別子は DOI 15件・PMID 15件・PMCID 2件（＋SRC-5035 の同定分）。
- 記載値の誤りは **SRC-5118 の DOI 1件のみ**（PMID は正しく、DOI の登録先が Crossref 側で別論文になっているデータベース側の問題）。
- SRC-5112 の PMCID 未記載（実在）と、SRC-5035 の識別子未登録（今回同定）は補完候補。
