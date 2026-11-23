# 識別子・書誌・ライセンスの照合の依頼（7件）

依頼者：三原弘（2026-11-23）。11月23日の ME・EY の照合（me_ey_id_verification_20261123.md）と同じ方法で、Crossref API・PubMed E-utilities・PMC・出版社の公式ページを使って照合し、結果を1つの Markdown（id_check_20261123b.md）にまとめてください。**照合の前に、手元のレポジトリの写しを最新版に更新してください**（前回は写しが古く、登録済みの識別子が「未登録」と報告されました）。

## 照合してほしい項目

| # | 対象 | 今の記載 | 確かめること |
|---|---|---|---|
| 1 | SRC-2481（BL-004）Adewoyin AS, Nwogoh B. Peripheral blood film - a review. Ann Ib Postgrad Med. 2014;12(2):71-79 | PMID 25960697、PMCID PMC7127472、CC BY-NC 3.0 | PMCID は別論文のものという指摘あり。PMID 25960697 に対応する PMCID（候補 PMC4415389）と、PMC 版のライセンス表示 |
| 2 | SRC-4026（SM-002）Li Y, Hecht SS. Food Chem Toxicol. 2022 | 巻167、論文番号 113179、DOI 10.1016/j.fct.2022.113179 | 正しい巻（指摘では165）・論文番号・PMID |
| 3 | SRC-3856（PX-001）Daza C ほか. Acad Psychiatry. 2025;49(4):355-364 | DOI 10.1007/s40596-025-02157-z、PMID 40495096 | DOI と PMID が指す論文の題名・著者・巻号・ページ。記載と食い違う点を全部挙げる |
| 4 | SRC-3866（PX-012）King RA; AACAP. Practice parameters for the psychiatric assessment of children and adolescents. J Am Acad Child Adolesc Psychiatry. 1997;36(10 Suppl) | DOI 10.1097/00004583-199710001-00002、PMID 9606102 | 3と同じ |
| 5 | SRC-2027（VI-018）Koyama M ほか. Jpn J Infect Dis. 2024 | DOI 10.7883/yoken.JJID.2024.035、PMID 38825454、UNKNOWN | J-STAGE の論文ページと JJID の公式の投稿規程に書かれたライセンス（CC BY かどうか）。根拠のページの URL と、該当の記載の要約 |
| 6 | SRC-3351（FT-011）Moise KJ Jr ほか. JAMA Netw Open. 2025 | DOI 10.1001/jamanetworkopen.2025.44649、UNKNOWN | Crossref の license 欄、PMC の収載の有無と表示、出版社ページの表示。PMID と PMCID |
| 7 | SRC-096（BP-047）Ohtsuka T ほか. Kyoto guidelines for IPMN. Pancreatology. 2024 | DOI 10.1016/j.pan.2023.12.009、PMID 38182527、UNKNOWN | Crossref の license 欄と出版社ページの表示（CC BY-NC-ND かどうか）。巻・ページ |

## 書き方

- 項目ごとに「API や公式ページが返した値」「今の記載」「一致か不一致か」を書く。確かめられなかったものは「確認できず」と書き、推測で埋めない。
- ライセンスは、どのページのどの表示で確かめたかを書く。Unpaywall や OpenAlex だけを根拠にしない（版によって表示が違うことがあるため）。
- 論文の本文は保存しない。
