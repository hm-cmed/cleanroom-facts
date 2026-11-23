# 識別子・書誌・ライセンスの照合結果（7件）

- 照合日：2026-11-23
- 依頼：request_id_check_20261123.md（2026-11-23）
- 方法：Crossref API、PubMed E-utilities（esummary）、PMC（記事ページ・ID Converter）、出版社の公式ページ（J-STAGE、JJID 投稿規程、JAMA Network）
- 「今の記載」は、照合前に GitHub コネクタで取得した hm-cmed/cleanroom-facts の**最新版**（commit `292684b06f77f1a34a9f9fd589daf0099caec782`、2026-11-23 12:58 UTC）の `data/sources/sources.yaml` と章ファイル（BL・SM・PX・VI・FT・BP）の登録値で確認した。
- 論文の本文は保存していない。

---

## 1. SRC-2481（BL-004）Adewoyin & Nwogoh, Ann Ib Postgrad Med 2014

**API・公式ページが返した値**
- PubMed（PMID 25960697）：Adewoyin AS, Nwogoh B. "Peripheral blood film - a review." Ann Ib Postgrad Med. 2014 Dec;12(2):71-79。レコード内の PMCID は **PMC4415389**。
- PMC 記事ページ（PMC4415389、https://pmc.ncbi.nlm.nih.gov/articles/PMC4415389/ ）の表示：「© Association of Resident Doctors, UCH, Ibadan」「This is an open access article licensed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/3.0)」、同一ページに「PMCID: PMC4415389 PMID: 25960697」。
- 登録済みの PMC7127472 は、PubMed レコード上 Tefferi A. "How to interpret and pursue an abnormal complete blood cell count in adults." Mayo Clin Proc. 2005;80(7):923-936（PMID 16007898）の PMCID で、別論文のもの。

**今の記載（最新版）**
- マスター：pmid '25960697'、pmcid **PMC7127472**、license_note「CC BY-NC 3.0（作り手が Europe PMC の表示で確認、2026-11-11）」、source_class RESTRICTED。
- カード BL-004：pmid '25960697'、pmcid **PMC7127472**、source_license 未確認、source_class RESTRICTED。

**判定：PMCID が不一致**
- 正しい PMCID は **PMC4415389**（マスター・カード双方の PMC7127472 は別論文のもの）。
- PMID 25960697 は一致。ライセンス **CC BY-NC 3.0** は PMC 版の表示で確認でき、マスターの license_note は正しい（カード側 source_license「未確認」は実態と異なり、CC BY-NC 3.0 が正しい）。

---

## 2. SRC-4026（SM-002）Li & Hecht, Food Chem Toxicol 2022

**API が返した値**
- PubMed（PMID 35643228）：Li Y, Hecht SS. "Carcinogenic components of tobacco and tobacco smoke: A 2022 update." Food Chem Toxicol. **2022 Jul;165:113179**。DOI 10.1016/j.fct.2022.113179、PMCID PMC9616535（著者稿、NIHMS1842250）。
- Crossref（DOI 10.1016/j.fct.2022.113179）：Food and Chemical Toxicology、**volume 165**、page 113179。license 欄は刊行版（vor）の CC 表示なし（テキストマイニング用ライセンスと、著者稿向けの Elsevier OA ユーザーライセンスのみ）。

**今の記載（最新版）**
- マスター：『… Food Chem Toxicol. 2022;**167**:113179』、doi 10.1016/j.fct.2022.113179、pmid null、source_class RESTRICTED。
- カード SM-002：source は巻 **167**、doi 同上、pmid '35643228'。

**判定：巻が不一致**
- 正しい巻は **165**（PubMed・Crossref ともに 165）。論文番号 113179 と DOI は一致。
- PMID はカード側の **35643228** が正しい（マスターの pmid は空欄で、補完候補）。PMCID PMC9616535（著者稿）も実在する（カード・マスターとも未登録）。

---

## 3. SRC-3856（PX-001）Daza ほか, Acad Psychiatry 2025

**API が返した値**
- PubMed（PMID 40495096）：Daza C ほか. "Mapping the Mental Status Examination: Insights from a Scoping Review of Popular Psychiatry Textbooks." Acad Psychiatry. 2025 Aug;49(4):355-364。レコード内の DOI は 10.1007/s40596-025-02157-z。
- Crossref（同 DOI）：著者は Daza Claudio, Mauriziano Chiara, Liberona Andrés, Bao Josefina, Flores Luis J.、Academic Psychiatry、vol 49、issue 4、page 355-364。license 欄はテキストマイニング用のみ（CC 表示なし）。

**今の記載（最新版）**
- マスター：title/citation は上記と同一（49(4):355-364）、doi 10.1007/s40596-025-02157-z、pmid **null**、source_class RESTRICTED。
- カード PX-001：source は上記と同一、doi 同上、pmid '40495096'。

**判定：現行の登録値は全項目一致（食い違いなし）**
- DOI と PMID は同じ論文を指し、題名・著者・誌名・巻号・ページはマスター／カードの記載とすべて一致する。
- なお、カード PX-001 の corroboration 欄には、旧いカード側表記として「Daza O, et al. What Are the Components of the Mental Status Exam? 49(6):595-599」が引用されているが、この表記は現行の source 欄には存在せず、その題名の論文は PubMed・Crossref のいずれでも確認できない（著者の頭文字 O、題名、49(6)、595-599 のいずれも実在論文と食い違う）。現行登録値そのものの不一致ではない。
- マスターの pmid 空欄には、カード側で確認済みの **40495096** が補完候補。

---

## 4. SRC-3866（PX-012）King RA; AACAP, J Am Acad Child Adolesc Psychiatry 1997

**API が返した値**
- PubMed（PMID 9606102）：King RA; American Academy of Child and Adolescent Psychiatry. "Practice parameters for the psychiatric assessment of children and adolescents." J Am Acad Child Adolesc Psychiatry. 1997 Oct;36(10 Suppl):4S-20S。レコード内の DOI は 10.1097/00004583-199710001-00002。
- Crossref（同 DOI）：題名 "Practice Parameters for the Psychiatric Assessment of Children and Adolescents"、著者 King, Robert A.、volume 36、issue 10、page 4S-20S、special_numbering S、1997年10月。license 欄はテキストマイニング用のみ。

**今の記載（最新版）**
- マスター：title/citation は上記と同一（36(10 Suppl):4S-20S）、doi 10.1097/00004583-199710001-00002、pmid **null**、source_class RESTRICTED。
- カード PX-012：source は上記と同一、doi 同上、pmid '9606102'。

**判定：一致**
- DOI と PMID は同じ論文を指し、題名・著者・巻号・ページは記載とすべて一致する。食い違う点はない。
- マスターの pmid 空欄には、カード側で確認済みの **9606102** が補完候補。

---

## 5. SRC-2027（VI-018）Koyama ほか, Jpn J Infect Dis 2024

**API・公式ページが返した値**
- PubMed（PMID 38825454）／Crossref（DOI 10.7883/yoken.JJID.2024.035）：Koyama M, Hiroi S, Hirai Y, Kaida A. Jpn J Infect Dis. 2024;77(5):292-295。書誌は記載と一致。Crossref の license 欄は**表示なし**（マスターの license_note「Crossref にライセンス表示なし」と一致）。
- J-STAGE 論文ページ（https://www.jstage.jst.go.jp/article/yoken/77/5/77_JJID.2024.035/_article ）：メタデータで citation_volume 77、issue 5、292-295、DOI、出版社 National Institute of Infectious Diseases、著作権者表示は「Authors」を確認。ページ本文側の CC ロゴ表示は取得テキストでは確認できなかった。
- JJID 公式の投稿規程「Instructions to Authors」（国立感染症研究所、2024-08-13 版、https://www.niid.jihs.go.jp/images/jjid/Instructions_to_Authors_240813.pdf ）の記載：「**JJID articles are published open access under a CC BY license (Creative Commons Attribution 4.0 International License). Copyright: The copyright belongs to the authors.**」

**今の記載（最新版）**
- マスター：doi 10.7883/yoken.JJID.2024.035、pmid '38825454'、license_note「Crossref にライセンス表示なし」、source_class **UNKNOWN**。
- カード VI-018：同 DOI・PMID、source_license「Crossref にライセンス表示なし」、source_class UNKNOWN。

**判定：書誌・識別子は一致。ライセンスは CC BY 4.0 と確認**
- JJID の公式投稿規程により、同誌の論文は **CC BY（Creative Commons Attribution 4.0 International）** で公開され、著作権は著者に帰属する。本論文（2024年9月発行）はこの規程の下にある。したがって source_class UNKNOWN は OPEN（CC BY 4.0）への訂正候補。

---

## 6. SRC-3351（FT-011）Moise ほか, JAMA Netw Open 2025

**API・公式ページが返した値**
- PubMed（PMID 41284292）：Moise KJ Jr ほか. "A Clinical Practice Guideline for the Management of Pregnancy Alloimmunized to Red Blood Cell Antigens." JAMA Netw Open. 2025 Nov 3;8(11):e2544649。レコード内の DOI は 10.1001/jamanetworkopen.2025.44649。
- Crossref（同 DOI）：JAMA Network Open、vol 8、issue 11、page e2544649。license 欄は**表示なし**。
- PMC：ID Converter で PMID 41284292 は「Identifier not found in PMC」。**PMC 未収載（PMCID なし）**。
- 出版社ページ（JAMA Network、https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2841768 ）の表示：「**Open Access: This is an open access article distributed under the terms of the CC-BY License. © 2025 Moise KJ Jr et al. JAMA Network Open.**」、書誌表示「JAMA Netw Open 2025;8;(11):e2544649. doi: 10.1001/jamanetworkopen.2025.44649」。

**今の記載（最新版）**
- マスター：『… JAMA Netw Open. 2025;8(11):e2544649』、doi 10.1001/jamanetworkopen.2025.44649、pmid **null**、pmcid null、license_note null、source_class **UNKNOWN**。
- カード FT-011：source 同上、doi 同上、pmid '41284292'、source_license「CC 表示を確認できず（Europe PMC でライセンス欄なし）」、source_class UNKNOWN。

**判定：書誌・DOI は一致。PMID はカード側が正しく、ライセンスは CC BY と確認**
- 正しい PMID は **41284292**（カード側に登録済み。マスターは空欄で補完候補）。
- PMCID は**なし**（PMC 未収載）。
- ライセンスは出版社ページの表示により **CC BY**（CC-BY License）。source_class UNKNOWN は OPEN への訂正候補で、カード側の「CC 表示を確認できず」は実態と異なる。

---

## 7. SRC-096（BP-047）Ohtsuka ほか, Pancreatology 2024（Kyoto guidelines for IPMN）

**API・公式ページが返した値**
- PubMed（PMID 38182527）：Ohtsuka T ほか. "International evidence-based Kyoto guidelines for the management of intraductal papillary mucinous neoplasm of the pancreas." Pancreatology. 2024 Mar;24(2):255-270。レコード内の DOI は 10.1016/j.pan.2023.12.009。
- Crossref（同 DOI）：Pancreatology、vol 24、issue 2、page 255-270。license 欄：刊行版（content-version **vor**）に **http://creativecommons.org/licenses/by-nc-nd/4.0/**（開始日 2023-12-31）の登録あり（ほかにテキストマイニング用ライセンス）。
- 出版社ページ（ScienceDirect、https://www.sciencedirect.com/science/article/pii/S1424390323018835 ）：直接取得は **403 のため表示を確認できず**。

**今の記載（最新版）**
- マスター：『… Pancreatology 2024;24:255-270』、doi 10.1016/j.pan.2023.12.009、pmid '38182527'、license_note「未確認（抄録のみ参照）」、source_class **UNKNOWN**。
- カード BP-047：同書誌・DOI・PMID、source_license「未確認（抄録のみ参照）」、source_class UNKNOWN。

**判定：書誌・識別子は一致。ライセンスは CC BY-NC-ND 4.0（Crossref の license 欄で確認）**
- 巻・ページは 24(2):255-270 で記載と一致（号はマスター未記載）。
- ライセンスは Crossref の刊行版ライセンス表示により **CC BY-NC-ND 4.0**。出版社ページ側の表示はアクセス制限（403）で**確認できず**。CC BY-NC-ND は本プロジェクトの区分では RESTRICTED 相当のため、UNKNOWN は RESTRICTED への訂正候補。

---

## まとめ

| # | 対象 | 結論 |
|---|---|---|
| 1 | SRC-2481 | **不一致**：PMCID は PMC4415389 が正しい（登録値 PMC7127472 は Tefferi 2005 のもの）。ライセンス CC BY-NC 3.0 は PMC 表示で確認 |
| 2 | SRC-4026 | **不一致**：巻は 165 が正しい（登録値 167）。PMID 35643228（カード側）は正しい |
| 3 | SRC-3856 | **一致**：現行登録値は実在論文と全項目一致。旧表記の引用が corroboration 内に残るのみ。マスター pmid 空欄に 40495096 が補完候補 |
| 4 | SRC-3866 | **一致**：全項目一致。マスター pmid 空欄に 9606102 が補完候補 |
| 5 | SRC-2027 | 書誌・識別子は一致。ライセンスは **CC BY 4.0**（JJID 公式投稿規程で確認）→ OPEN 訂正候補 |
| 6 | SRC-3351 | 書誌・DOI は一致。PMID 41284292（カード側）が正しい。PMCID なし（PMC 未収載）。ライセンスは **CC BY**（JAMA ページ表示で確認）→ OPEN 訂正候補 |
| 7 | SRC-096 | 書誌・識別子は一致。ライセンスは **CC BY-NC-ND 4.0**（Crossref の license 欄で確認。出版社ページは 403 で確認できず）→ RESTRICTED 訂正候補 |
