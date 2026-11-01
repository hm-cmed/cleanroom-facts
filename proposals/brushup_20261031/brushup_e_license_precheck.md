# UNKNOWN 出典のライセンス事前確認（提案E 下準備）

作成日：2026-10-31

## 目的と位置づけ

出典マスターで source_class が UNKNOWN のままの出典616件について、DOI のメタデータ（Crossref の license 配列）に当たってライセンスの当たりを付けたもの。**これは事前の当たり付けであり、確定ではない。** source_class の確定は、従来どおり本文・出版社ページ側の確認を経てレポジトリ側で行う。

## 方法と判定ルール

- 対象：UNKNOWN 616件のうち DOI がある516件。DOI がない100件は本確認の対象外。
- 各 DOI の license 配列を確認し、最も開放的なライセンスを代表として採用した。
- OPEN候補：CC BY（バージョン不問）が license にあるもの。
- RESTRICTED候補：CC BY-NC／CC BY-ND／CC BY-NC-ND があるもの、または出版社の通常ライセンス（購読・TDM 等）のみでオープンライセンスの表示がないもの。後者は「出版社ライセンスのみ」と表示した（要・本文側の確認）。
- 判定保留：license 情報自体がないもの、DOI が解決できなかったもの。

## 集計

| 分類 | 件数 |
|---|---|
| OPEN候補 | 18 |
| RESTRICTED候補 | 284 |
| 判定保留 | 214 |
| 小計（DOI あり） | 516 |
| 対象外（DOI なし） | 100 |
| UNKNOWN 合計 | 616 |

RESTRICTED候補の内訳：
- CC BY-NC-ND 4.0：15件
- CC BY-NC 4.0：3件
- 出版社ライセンスのみ（オープンライセンス表示なし）：266件

判定保留の内訳：
- メタデータにライセンス情報がない：212件
- DOI が解決できない（404）：SRC-252（DOI: 10.2143/AC.71.1.3132092）
- DOI が解決できない（404）：SRC-4377（DOI: 10.3980/j.issn.2222-3959.2013.03.27）

## OPEN候補の一覧

| SRC | DOI | 確認したライセンス表示 |
|---|---|---|
| SRC-028 | 10.1007/s00535-021-01843-7 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-029 | 10.1007/s10120-022-01331-8 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-030 | 10.1007/s10120-025-01698-4 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-032 | 10.1007/s10147-024-02488-1 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-048 | 10.1007/s00535-021-01784-1 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-049 | 10.1007/s00535-020-01746-z | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-051 | 10.1007/s00535-021-01776-1 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-052 | 10.1007/s10147-025-02899-8 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-088 | 10.1007/s00535-022-01911-6 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-089 | 10.1007/s10147-023-02317-x | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-097 | 10.1007/s00535-023-02014-6 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-141 | 10.1016/j.cgh.2026.07.022 | CC BY 4.0 |
| SRC-254 | 10.1007/s40279-023-01873-6 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-371 | 10.1016/j.resinv.2026.101482 | CC BY 4.0 |
| SRC-383 | 10.3389/fmed.2026.1779715 | CC BY 4.0 |
| SRC-435 | 10.1186/s40560-022-00615-6 | CC BY 4.0（同一ライセンスの複数エントリあり） |
| SRC-4048 | 10.1093/joccuh/uiaf026 | CC BY 4.0 |
| SRC-4303 | 10.1136/archdischild-2019-317085 | CC BY 4.0 |

## RESTRICTED候補の一覧

| SRC | DOI | 確認したライセンス表示 |
|---|---|---|
| SRC-024 | 10.1097/MD.0000000000015845 | CC BY-NC 4.0 |
| SRC-039 | 10.1111/jne.13306 | CC BY-NC-ND 4.0 |
| SRC-096 | 10.1016/j.pan.2023.12.009 | CC BY-NC-ND 4.0 |
| SRC-142 | 10.21518/ms2026-232 | 出版社ライセンスのみ: https://www.med-sovet.pro/jour/about/editorialPolicies#openAccessPolicy |
| SRC-167 | 10.1177/2050640617700014 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-238 | 10.1056/NEJMoa1814052 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-239 | 10.1056/NEJMoa2209051 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-291 | 10.1038/s41440-025-02331-8 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-352 | 10.1016/j.resinv.2025.06.014 | CC BY-NC-ND 4.0 |
| SRC-374 | 10.1016/j.alit.2023.02.006 | CC BY-NC-ND 4.0 |
| SRC-376 | 10.1016/j.resinv.2021.01.007 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-378 | 10.1183/13993003.01126-2025 | 出版社ライセンスのみ: https://publications.ersnet.org/user-licence |
| SRC-385 | 10.1186/1749-8090-9-117 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-410 | 10.1164/rccm.202202-0399ST | CC BY-NC-ND 4.0 |
| SRC-411 | 10.1183/13993003.00158-2025 | 出版社ライセンスのみ: https://publications.ersnet.org/user-licence |
| SRC-412 | 10.1164/rccm.201308-1483ST | 出版社ライセンスのみ: https://academic.oup.com/pages/standard-publication-reuse-rights |
| SRC-416 | 10.1056/NEJMoa2414108 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-418 | 10.1056/NEJMoa1908681 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-419 | 10.1056/NEJMoa1903076 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-420 | 10.1002/art.41986 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-426 | 10.1183/13993003.00061-2024 | CC BY-NC 4.0 |
| SRC-427 | 10.1164/rccm.200710-1501OC | 出版社ライセンスのみ: https://academic.oup.com/pages/standard-publication-reuse-rights |
| SRC-428 | 10.1016/j.ijrobp.2009.06.091 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-446 | 10.1056/NEJMoa2213558 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-447 | 10.1056/NEJMoa2008470 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-448 | 10.1016/S0140-6736(81)91970-X | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-476 | 10.1056/NEJMoa1913662 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-498 | 10.1016/s0196-0644(89)80515-3 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-501 | 10.1183/13993003.01499-2021 | 出版社ライセンスのみ: https://www.ersjournals.com/user-licence |
| SRC-569 | 10.1056/NEJMoa2404873 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-580 | 10.1053/j.ajkd.2016.10.032 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-581 | 10.1053/j.ajkd.2003.10.024 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-586 | 10.1007/s10157-025-02636-5 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-692 | 10.1136/bmj.i6112 | 出版社ライセンスのみ: http://www.bmj.org/licenses/tdm/1.0/terms-and-conditions.html |
| SRC-693 | 10.1016/S0022-5347(01)66321-3 | 出版社ライセンスのみ: http://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-709 | 10.1016/0022-3468(92)90199-h | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-711 | 10.1016/S0022-5347(05)65373-6 | 出版社ライセンスのみ: http://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-771 | 10.1093/jnci/djx214 | 出版社ライセンスのみ: http://academic.oup.com/journals/pages/about_us/legal/notices |
| SRC-818 | 10.1002/ijgo.12666 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-821 | 10.1016/j.ajog.2017.05.045 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-829 | 10.1016/j.fertnstert.2021.02.010 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-830 | 10.1016/j.fertnstert.2015.03.019 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-831 | 10.1016/j.fertnstert.2021.01.051 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-833 | 10.1016/j.fertnstert.2018.08.027 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-837 | 10.1016/j.beem.2007.11.001 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-841 | 10.1016/j.contraception.2011.01.021 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-842 | 10.1177/2042098614548857 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-846 | 10.1016/j.ecl.2015.05.001 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-855 | 10.1016/j.contraception.2016.02.006 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-874 | 10.1038/s41572-019-0125-9 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-880 | 10.1016/S0140-6736(16)30053-8 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-881 | 10.1038/s41572-019-0103-2 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-884 | 10.1111/j.1365-2265.2010.03913.x | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-894 | 10.1038/nrdp.2016.78 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-907 | 10.1016/j.beem.2019.101367 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-910 | 10.1007/s40618-015-0391-7 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-911 | 10.1634/theoncologist.2010-0405 | 出版社ライセンスのみ: https://academic.oup.com/journals/pages/open_access/funder_policies/chorus/standard_publication_model |
| SRC-912 | 10.1089/thy.2015.0020 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-915 | 10.1016/S0140-6736(11)60276-6 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-945 | 10.2337/dc25-S006 | 出版社ライセンスのみ: https://www.diabetesjournals.org/journals/pages/license |
| SRC-951 | 10.1056/NEJMoa2100165 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-953 | 10.1016/j.mayocp.2016.06.010 | CC BY-NC-ND 4.0 |
| SRC-957 | 10.1016/j.metabol.2015.10.014 | CC BY-NC-ND 4.0 |
| SRC-973 | 10.1093/eurheartj/ehz455 | 出版社ライセンスのみ: https://academic.oup.com/journals/pages/open_access/funder_policies/chorus/standard_publication_model |
| SRC-976 | 10.1056/NEJMoa2032183 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-979 | 10.1016/S0140-6736(15)01274-X | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-980 | 10.1056/NEJMoa1805689 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-981 | 10.1016/j.pan.2020.06.005 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-988 | 10.1111/bjh.12959 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-992 | 10.1002/acr.24180 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-996 | 10.1002/ajmg.c.31552 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-999 | 10.1007/BF00861588 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1011 | 10.1007/s12282-023-01526-6 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1015 | 10.1007/s12282-023-01510-0 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1020 | 10.1089/bfm.2022.29207.kbm | 出版社ライセンスのみ: https://www.liebertpub.com/nv/resources-tools/text-and-data-mining-policy/121/ |
| SRC-1024 | 10.1136/bmj.39511.493391.BE | 出版社ライセンスのみ: http://www.bmj.org/licenses/tdm/1.0/terms-and-conditions.html |
| SRC-1026 | 10.1159/000452150 | 出版社ライセンスのみ: https://www.karger.com/Services/SiteLicenses |
| SRC-1027 | 10.1159/000502231 | CC BY-NC-ND 4.0（同一ライセンスの複数エントリあり） |
| SRC-1031 | 10.1016/S2213-8587(15)00380-0 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1032 | 10.1002/jpn3.70193 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1036 | 10.1038/s41572-018-0025-4 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1039 | 10.1002/jimd.12100 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1047 | 10.1056/NEJMoa1803760 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-1049 | 10.1111/obr.12836 | CC BY-NC-ND 4.0 |
| SRC-1054 | 10.1016/j.amjmed.2014.09.030 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1057 | 10.1016/j.amjmed.2013.07.006 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1058 | 10.1111/anae.14963 | CC BY-NC-ND 4.0 |
| SRC-1080 | 10.1007/s40257-015-0154-4 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1081 | 10.1111/bcp.15490 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1082 | 10.1111/j.1365-4632.2011.05348.x | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1083 | 10.1007/s40257-021-00592-w | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1084 | 10.1016/j.jid.2016.03.023 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1085 | 10.1046/j.1523-1747.2000.00061.x | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1091 | 10.1016/j.jaad.2004.11.051 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1110 | 10.1016/j.jaci.2015.08.034 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1111 | 10.1007/s10147-007-0751-1 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1113 | 10.1111/j.1365-2133.2008.08713.x | 出版社ライセンスのみ: http://doi.wiley.com/10.1002/tdm_license_1.1 |
| SRC-1114 | 10.3322/caac.21409 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1117 | 10.1056/NEJMoa1805131 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-1163 | 10.1016/j.jaad.2018.02.021 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1175 | 10.1016/S0140-6736(14)60763-7 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1178 | 10.1016/j.arr.2016.03.002 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1185 | 10.1111/jdv.12541 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1187 | 10.1128/CMR.00069-18 | 出版社ライセンスのみ: https://journals.asm.org/non-commercial-tdm-license |
| SRC-1190 | 10.1128/CMR.00007-11 | 出版社ライセンスのみ: https://journals.asm.org/non-commercial-tdm-license |
| SRC-1191 | 10.1111/1346-8138.13896 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1192 | 10.1016/j.jaad.2007.06.027 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1193 | 10.1067/s0190-9622(03)00896-x | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1194 | 10.1111/bjd.13310 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1195 | 10.1016/j.jaad.2023.12.017 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1196 | 10.1016/j.jaad.2017.04.1141 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1197 | 10.1007/s40257-017-0334-5 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1205 | 10.1111/bjd.16117 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1206 | 10.1016/j.ophtha.2025.12.031 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1208 | 10.1177/0194599819890327 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1209 | 10.1177/0194599817751030 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1210 | 10.1177/0194599817722550 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1253 | 10.1016/j.survophthal.2016.03.005 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1256 | 10.1016/j.ophtha.2018.10.020 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1257 | 10.1016/j.ophtha.2017.05.012 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1258 | 10.1007/s11908-012-0238-8 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1259 | 10.1016/j.jtos.2017.05.008 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1262 | 10.1097/ICO.0000000000003420 | CC BY-NC-ND 4.0 |
| SRC-1263 | 10.1016/j.survophthal.2021.02.013 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1264 | 10.1016/S0140-6736(12)60437-1 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1265 | 10.1038/nrdp.2015.14 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1268 | 10.1016/j.ophtha.2004.03.029 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1271 | 10.1128/CMR.00113-16 | 出版社ライセンスのみ: https://journals.asm.org/non-commercial-tdm-license |
| SRC-1272 | 10.1016/j.ajo.2021.03.061 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1275 | 10.1016/S1474-4422(22)00200-9 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1276 | 10.1016/j.survophthal.2021.11.007 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1279 | 10.1038/s41572-020-0158-0 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1281 | 10.1016/S0161-6420(03)00475-5 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1282 | 10.1016/j.ophtha.2018.04.007 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1284 | 10.1016/j.ophtha.2010.02.021 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1285 | 10.1016/j.ophtha.2010.02.022 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1287 | 10.1016/S0140-6736(07)60198-6 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1290 | 10.1016/S0140-6736(12)60282-7 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1297 | 10.1016/S0039-6257(97)84041-6 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1309 | 10.1016/j.ophtha.2011.07.013 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1312 | 10.1016/j.ajo.2005.03.057 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1313 | 10.1016/j.ajo.2021.03.036 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1314 | 10.1016/j.ajo.2015.01.022 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1341 | 10.1016/j.amjoto.2025.104774 | CC BY-NC 4.0 |
| SRC-1343 | 10.1177/0194599813517083 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1344 | 10.1177/0194599816671491 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1346 | 10.1016/j.anl.2025.02.001 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1349 | 10.1177/0194599815623467 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1352 | 10.1016/j.anl.2022.11.004 | CC BY-NC-ND 4.0 |
| SRC-1355 | 10.1177/0194599819859885 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1356 | 10.1038/nrdp.2016.94 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1362 | 10.1159/000490277 | 出版社ライセンスのみ: https://www.karger.com/Services/SiteLicenses |
| SRC-1363 | 10.1111/cns.12468 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1367 | 10.1007/s10143-023-02145-7 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1369 | 10.1016/S0030-6665(03)00172-5 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1371 | 10.1016/j.diagmicrobio.2017.06.007 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1377 | 10.1007/s00405-011-1636-5 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1378 | 10.1038/nrclinonc.2014.97 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1380 | 10.1016/j.ajem.2022.04.018 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1382 | 10.3322/caac.21386 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1384 | 10.1016/j.otc.2019.03.004 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1385 | 10.1016/j.rmed.2017.03.030 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1431 | 10.1111/j.1529-8019.2010.01320.x | 出版社ライセンスのみ: http://doi.wiley.com/10.1002/tdm_license_1.1 |
| SRC-1432 | 10.1016/j.cden.2013.12.002 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1436 | 10.3322/canjclin.52.4.195 | 出版社ライセンスのみ: http://doi.wiley.com/10.1002/tdm_license_1.1 |
| SRC-1438 | 10.1111/odi.12646 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1441 | 10.1016/j.anpedi.2018.09.014 | CC BY-NC-ND 4.0 |
| SRC-1443 | 10.1016/S0140-6736(19)30956-0 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1444 | 10.1038/s41572-020-00224-3 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1445 | 10.1002/lary.23843 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1447 | 10.1016/j.otc.2015.10.005 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1449 | 10.1177/0003489416665194 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-1452 | 10.1016/j.clp.2018.07.012 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1453 | 10.1016/j.otohns.2010.02.026 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1455 | 10.1093/jbcr/irac025 | 出版社ライセンスのみ: https://academic.oup.com/journals/pages/open_access/funder_policies/chorus/standard_publication_model |
| SRC-1456 | 10.1177/10806032231222359 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-1459 | 10.1038/s41433-019-0456-5 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1461 | 10.1016/j.otc.2008.01.006 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1462 | 10.1002/lary.25358 | 出版社ライセンスのみ: http://doi.wiley.com/10.1002/tdm_license_1.1 |
| SRC-1465 | 10.1016/j.ijom.2020.06.004 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1473 | 10.1016/j.clp.2018.07.006 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1474 | 10.1016/j.ccc.2016.06.008 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1475 | 10.1016/j.ijnurstu.2019.103483 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1478 | 10.1016/s0896-1549(02)00007-x | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1480 | 10.1002/lary.29580 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1521 | 10.1245/s10434-021-10188-7 | 出版社ライセンスのみ: https://www.springer.com/tdm |
| SRC-1523 | 10.1016/j.rcl.2023.12.008 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1524 | 10.1016/j.ad.2018.05.005 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1526 | 10.1016/S0022-3476(97)70249-X | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1676 | 10.1038/nrdp.2015.5 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1677 | 10.1002/mds.25475 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1678 | 10.1038/nrneurol.2015.86 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1683 | 10.1111/ajad.12372 | 出版社ライセンスのみ: http://doi.wiley.com/10.1002/tdm_license_1.1 |
| SRC-1684 | 10.1111/j.1468-1331.2010.03153.x | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1691 | 10.1111/j.1468-1331.2011.03501.x | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1698 | 10.1164/rccm.201606-1275CI | 出版社ライセンスのみ: https://academic.oup.com/pages/standard-publication-reuse-rights |
| SRC-1700 | 10.1177/1060028016657553 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-1701 | 10.1111/epi.12550 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1702 | 10.1111/epi.13670 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#am |
| SRC-1709 | 10.1111/epi.13121 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1710 | 10.5698/1535-7597-16.1.48 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-1746 | 10.1111/ene.14959 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1749 | 10.1111/j.1529-8027.2010.00281.x | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-1755 | 10.1007/s12178-016-9327-x | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1760 | 10.1177/0333102417738202 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-1782 | 10.1177/0269215514540919 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-1785 | 10.1016/j.spinee.2017.08.241 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1796 | 10.1177/03635465241264804 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-1798 | 10.1136/ard.2009.108233 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1799 | 10.1136/ard-2022-223296 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1873 | 10.1016/j.jse.2009.04.006 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1875 | 10.1002/14651858.CD007759.pub4 | 出版社ライセンスのみ: http://doi.wiley.com/10.1002/tdm_license_1.1 |
| SRC-1878 | 10.1007/s00264-023-06077-1 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-1879 | 10.1007/s00132-013-2226-6 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1883 | 10.1007/s00774-009-0080-8 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-1901 | 10.1634/theoncologist.2007-0237 | 出版社ライセンスのみ: https://academic.oup.com/journals/pages/open_access/funder_policies/chorus/standard_publication_model |
| SRC-1911 | 10.1016/j.jcot.2016.04.006 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-1916 | 10.1634/theoncologist.2013-0328 | 出版社ライセンスのみ: https://academic.oup.com/journals/pages/open_access/funder_policies/chorus/standard_publication_model |
| SRC-1983 | 10.1016/S1726-4901(10)70088-5 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2157 | 10.1038/334519a0 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-2161 | 10.1128/CMR.00021-11 | 出版社ライセンスのみ: https://journals.asm.org/non-commercial-tdm-license |
| SRC-2732 | 10.1016/j.blre.2008.06.001 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2735 | 10.1016/S0140-6736(22)00536-0 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2738 | 10.1111/j.1365-2141.2011.08921.x | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-2740 | 10.1016/S2352-3026(23)00377-0 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2741 | 10.1111/bjh.15409 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-2812 | 10.1111/all.15032 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-2814 | 10.1111/all.12350 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-2818 | 10.1016/j.jaip.2022.06.008 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2821 | 10.1111/all.13262 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-2824 | 10.1016/j.anl.2025.05.005 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2826 | 10.1016/j.anai.2019.07.022 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2829 | 10.1016/j.anai.2022.08.003 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2906 | 10.1002/art.40930 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-2907 | 10.1136/ard-2023-224762 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2909 | 10.1136/annrheumdis-2016-210571 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2911 | 10.1136/annrheumdis-2013-204424 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2913 | 10.1002/art.24621 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-2946 | 10.1136/ard-2022-223480 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2948 | 10.1136/ard-2022-223764 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2951 | 10.1136/annrheumdis-2011-200329 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2953 | 10.1136/ard-2022-223482 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2954 | 10.1002/art.41776 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-2955 | 10.1002/art.37715 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-2991 | 10.1016/S0140-6736(16)31591-4 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2992 | 10.1136/ard.2010.133645 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2993 | 10.1002/art.21972 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-2994 | 10.1136/ard-2024-225531 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-2995 | 10.1093/mr/roab103 | 出版社ライセンスのみ: https://academic.oup.com/journals/pages/open_access/funder_policies/chorus/standard_publication_model |
| SRC-2998 | 10.1183/13993003.04079-2020 | 出版社ライセンスのみ: https://www.ersjournals.com/user-licence |
| SRC-2999 | 10.1016/j.semarthrit.2016.08.012 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-3000 | 10.1136/annrheumdis-2016-209724 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-3001 | 10.1016/j.berh.2023.101867 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-3081 | 10.1038/nrdp.2015.61 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-3084 | 10.1016/j.jaip.2016.09.013 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-3085 | 10.1111/bjh.15831 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-3087 | 10.1038/nrdp.2015.71 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-3171 | 10.1016/j.ajog.2022.06.059 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-3174 | 10.1111/1471-0528.70239 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-3252 | 10.2337/dc26-S015 | 出版社ライセンスのみ: https://www.diabetesjournals.org/content/license |
| SRC-3255 | 10.1177/10507256261445624 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-3257 | 10.1016/j.ard.2025.02.023 | CC BY-NC-ND 4.0 |
| SRC-3259 | 10.1016/j.ajog.2023.12.023 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-3260 | 10.1016/j.ajog.2021.06.008 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-3277 | 10.1016/j.ajog.2016.03.012 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-3278 | 10.1016/S1701-2163(16)30594-1 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-3280 | 10.1007/s12185-025-03918-0 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-3281 | 10.1089/jwh.2006.15.352 | 出版社ライセンスのみ: http://www.liebertpub.com/nv/resources-tools/text-and-data-mining-policy/121/ |
| SRC-3284 | 10.1016/j.ajog.2019.01.216 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-3363 | 10.1038/s41372-020-0757-3 | 出版社ライセンスのみ: https://www.springer.com/tdm |
| SRC-3432 | 10.1111/ped.13635 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-3440 | 10.1111/jpc.12698 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-3443 | 10.1056/NEJMoa2020248 | 出版社ライセンスのみ: http://www.nejmgroup.org/legal/terms-of-use.htm |
| SRC-3522 | 10.1038/s41572-019-0143-7 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-3525 | 10.1002/ajmg.c.31527 | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-3836 | 10.1016/j.pediatrneurol.2007.12.008 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-4038 | 10.1016/S0140-6736(07)61202-1 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-4039 | 10.1111/j.1365-2125.2011.04026.x | 出版社ライセンスのみ: http://onlinelibrary.wiley.com/termsAndConditions#vor |
| SRC-4050 | 10.1007/s13671-021-00339-0 | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |
| SRC-4125 | 10.1016/j.wem.2023.05.013 | 出版社ライセンスのみ: https://journals.sagepub.com/page/policies/text-and-data-mining-license |
| SRC-4126 | 10.1016/j.rpor.2011.05.001 | 出版社ライセンスのみ: https://www.elsevier.com/tdm/userlicense/1.0/ |
| SRC-4224 | 10.1111/jgh.70083 | CC BY-NC-ND 4.0 |
| SRC-4393 | 10.1038/nrcardio.2016.57 | 出版社ライセンスのみ: http://www.springer.com/tdm |
| SRC-4399 | 10.1007/s10029-025-03561-y | 出版社ライセンスのみ: https://www.springernature.com/gp/researchers/text-and-data-mining |

## 判定保留について

判定保留は214件。ライセンス情報がない212件は、出版社ページや本文のライセンス表示を個別に確認する必要がある。DOI が解決できなかった2件は、DOI 自体の登録状況（転記誤りを含む）の点検対象として切り分けた。

## 注意

- メタデータの license 配列は出版社の申告ベースであり、本文のライセンス表示と食い違う場合がある（過去にも出版社 PDF と Crossref で表示が食い違った例がある）。OPEN候補・RESTRICTED候補のいずれも、確定前に本文側の表示と突き合わせること。
- 「出版社ライセンスのみ」には、本文が実際はオープンアクセスでもメタデータに CC 表示が登録されていないだけのものが混ざりうる。
