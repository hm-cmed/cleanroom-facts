# ライセンス未確認（UNKNOWN）の出典の照合結果（第1回：50件）

- 照合日：2026-11-23
- 依頼：request_license_check_01.md（2026-11-23）
- 方法：Crossref API、PubMed E-utilities（esummary）、PMC の論文ページ、出版社の公式ページ（J-STAGE、Thieme、AHA Journals、NEJM、AAFP、PMDA、WHO IRIS ほか）
- 「今の記載」は、照合前に GitHub コネクタで取得した hm-cmed/cleanroom-facts の**最新版**（commit `9de6c42a06ca9cf8f49165f81be561f65ef5199e`、2026-11-23 13:38 UTC）の `data/sources/sources.yaml` と章ファイル（NG）の登録値で確認した。対象50件はすべて source_class **UNKNOWN**。
- 根拠の優先順位は依頼どおり：出版社の論文ページ ＞ PMC の論文ページ（著者原稿でないこと）＞ Crossref の license 欄（content-version が vor のもの）。Unpaywall・OpenAlex は根拠にしていない。
- 論文の本文は保存していない（©・ライセンス表示の確認のために冒頭ページ等を一時的に参照したのみ）。
- 追記（2026-11-23）：SRC-3740 は当初「確認できず」だったが、同日ユーザーがアップロードした NICE 公式 PDF で再照合し、RESTRICTED に更新した（§18）。集計も更新後の値。

## 判定の集計

| 判定 | 件数 |
|---|---|
| OPEN | 0 |
| RESTRICTED | 50 |
| GOV_US | 0 |
| GOV_JP | 0 |
| 確認できず | 0 |

---

## 1. SRC-290（VS-001 ほか14枚）Circ J 2023 大動脈瘤・解離ガイドライン

- 出版社ページ（J-STAGE、https://www.jstage.jst.go.jp/article/circj/87/10/87_CJ-22-0794/_article ）：記事ページには「JOURNAL OPEN ACCESS」とあるが CC ライセンスの表示はない。
- 刊行版 PDF の冒頭ページの表示：「**All rights are reserved to the Japanese Circulation Society. For permissions, please email: cj@j-circ.or.jp**」（Circulation Journal Vol.87, October 2023）。
- Crossref（DOI 10.1253/circj.CJ-22-0794）：license 欄なし。書誌・PMID 37661428 は PubMed と一致。
- **判定：RESTRICTED**（© 日本循環器学会、All rights reserved。CC 表示なし）

## 2. SRC-440（PV-002 ほか10枚）Circulation 2026 急性肺塞栓ガイドライン

- 出版社ページ（AHA Journals、https://www.ahajournals.org/doi/10.1161/CIR.0000000000001415 ）：全文が公開されているが、CC ライセンスの表示はない（本文中の著作権表示はすべて転載図の出典表示）。
- Crossref（DOI 10.1161/CIR.0000000000001415）：license 欄なし。
- **判定：RESTRICTED**（© American Heart Association。CC 表示なし）

## 3. SRC-1180（BA-031 ほか5枚）Clin Infect Dis 2014 皮膚・軟部組織感染症ガイドライン

- Crossref（DOI 10.1093/cid/ciu296）：license 欄なし。
- 出版社（Oxford University Press）の表示はマスター記録どおり「© The Author 2014, Oxford University Press」で CC 表示なし。書誌（59(2):147-159、PMID 24947530）は PubMed と一致。
- **判定：RESTRICTED**

## 4. SRC-1256（EY-009 ほか5枚）Ophthalmology 2019 結膜炎 PPP

- Crossref（DOI 10.1016/j.ophtha.2018.10.020）：license 欄はテキストマイニング用のみ（CC 表示なし）。
- 出版社の表示は「© American Academy of Ophthalmology / Elsevier」。書誌（126(1):P94-P169、PMID 30366797）は PubMed と一致。
- **判定：RESTRICTED**

## 5. SRC-1436（OR-006 ほか5枚）CA Cancer J Clin 2002 口腔癌

- Crossref（DOI 10.3322/canjclin.52.4.195）：license 欄はテキストマイニング用のみ（CC 表示なし）。
- 出版社ページ（Wiley）はアクセス制限（403）のため表示を直接確認できなかった。書誌（52(4):195-215、PMID 12139232）は PubMed と一致。
- **判定：RESTRICTED**（Crossref に刊行版の CC ライセンス登録なし）

## 6. SRC-009（ES-069 ほか4枚）Endoscopy 2016 ESGE 異物ガイドライン

- 出版社ページ（Thieme、https://www.thieme-connect.de/products/ejournals/abstract/10.1055/s-0042-100456 ）の表示：「**© Georg Thieme Verlag KG Stuttgart · New York**」。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：マスターは DOI が空欄。PubMed（PMID 26862844）のレコードに DOI **10.1055/s-0042-100456** がある。

## 7. SRC-252（MP-023 ほか4枚）Acta Cardiol 2016 Summary 2015 ESC guidelines

- 登録済み DOI 10.2143/AC.71.1.3132092 は **Crossref にレコードが存在しない（404）**。
- 同一論文は Crossref に DOI **10.1080/AC.71.1.3132092**（Informa UK Limited＝Taylor & Francis、71(1):7-13、題名・著者一致）で登録されており、license 欄はない。
- **判定：RESTRICTED**（Taylor & Francis の通常記事。CC 表示なし）
- 備考：登録 DOI（10.2143…）は Crossref で解決できなかった。10.1080/AC.71.1.3132092 が Crossref 上の正規レコード。

## 8. SRC-410（IL-003 ほか4枚）Am J Respir Crit Care Med 2022 IPF/PPF ガイドライン

- Crossref（DOI 10.1164/rccm.202202-0399ST）：license 欄に刊行版（vor）として **CC BY-NC-ND 4.0**（https://creativecommons.org/licenses/by-nc-nd/4.0/ 、開始日 2026-03-16、delay 1415日＝刊行後にオープン化）の登録あり。
- PMC の刊行版ページ（PMC9851481、https://pmc.ncbi.nlm.nih.gov/articles/PMC9851481/ ）の表示：「Copyright © 2022 by the American Thoracic Society」。
- **判定：RESTRICTED**（CC BY-NC-ND 4.0 は本区分では RESTRICTED）
- 備考（識別子の補完候補）：マスターは PMCID が空欄。刊行版が **PMC9851481** で PMC 収載されている。

## 9. SRC-5227（UG-010 ほか4枚）Endoscopy 2026 ESGE 消化性潰瘍出血ガイドライン

- 出版社ページ（Thieme、https://www.thieme-connect.de/products/ejournals/abstract/10.1055/a-2863-8314 ）の表示：「**© 2026. European Society of Gastrointestinal Endoscopy. All rights reserved.**」
- **判定：RESTRICTED**
- 備考（書誌の補完候補）：マスターの title は「ESGE 2026（PubMed抄録 PMID 42127996）」という仮置きで、pmid 欄は空欄。正規の書誌は Gralnek IM, et al. "Endoscopic diagnosis and management of peptic ulcer bleeding: European Society of Gastrointestinal Endoscopy (ESGE) Guideline – Update 2026." Endoscopy. 2026;58(8):899-924. PMID **42127996**、DOI 10.1055/a-2863-8314（PubMed・Thieme で一致）。

## 10. SRC-830（RP-028 ほか4枚）Fertil Steril 2015 不妊女性の診断評価

- Crossref（DOI 10.1016/j.fertnstert.2015.03.019）：license 欄の刊行版（vor）は **Elsevier のオープンアクセス・ユーザーライセンス 1.0**（http://www.elsevier.com/open-access/userlicense/1.0/ 、2022-05-27 開始）で、CC ライセンスではない。
- **判定：RESTRICTED**（CC BY/CC0 ではないため OPEN に該当しない）

## 11. SRC-1107（DT-013 ほか3枚）Am Fam Physician 2003 良性皮膚腫瘍

- 出版社（AAFP）の刊行版 PDF 冒頭の表示：「Copyright© 2003 American Academy of Family Physicians.」（https://www.aafp.org/pubs/afp/issues/2003/0215/p729.html ）
- **判定：RESTRICTED**

## 12. SRC-115（NG-039・NG-040・NG-041）アコファイド錠100mg 添付文書

- 書誌の特定：マスターは書誌が空欄だったため、カード NG-039〜041 の記載から特定した。アコファイド錠100mg（アコチアミド塩酸塩水和物）添付文書、2023年8月改訂（第3版）、ゼリア新薬工業。
- PMDA の添付文書ページ（https://www.pmda.go.jp/PmdaSearch/iyakuDetail/380077_2399015F1020_1_09 ）で同版を確認。製造販売業者（ゼリア新薬工業）の作成文書で、CC ライセンスの表示はない。政府標準利用規約の対象となる府省の資料ではない。
- **判定：RESTRICTED**（CC 表示なし）

## 13. SRC-1168（SD-011 ほか3枚）JAMA 2020 乾癬レビュー

- Crossref（DOI 10.1001/jama.2020.4006）：license 欄なし。書誌（323(19):1945-1960、PMID 32427307）は PubMed と一致。JAMA の通常記事で © American Medical Association。
- **判定：RESTRICTED**

## 14. SRC-1186（SD-033 ほか3枚）N Engl J Med 2017 壊死性軟部組織感染症

- 出版社ページ（https://www.nejm.org/doi/full/10.1056/NEJMra1600673 ）で論文を確認。Crossref（DOI 10.1056/NEJMra1600673）：license 欄なし。© Massachusetts Medical Society で CC 表示なし。
- **判定：RESTRICTED**

## 15. SRC-1187（SD-035 ほか3枚）Clin Microbiol Rev 2019 皮膚抗酸菌感染症

- PMC の刊行版ページ（PMC6302357、https://pmc.ncbi.nlm.nih.gov/articles/PMC6302357/ ）の表示：「**Copyright © 2018 American Society for Microbiology. All Rights Reserved.**」
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：マスターは PMCID が空欄。刊行版が **PMC6302357** で PMC 収載されている。

## 16. SRC-1265（EY-023 ほか3枚）Nat Rev Dis Primers 2015 白内障

- Crossref（DOI 10.1038/nrdp.2015.14）：license 欄は Springer Nature のテキストマイニング用のみ（CC 表示なし）。© Nature Portfolio（Springer Nature）。
- **判定：RESTRICTED**

## 17. SRC-1350（OT-012 ほか3枚）WHO 2004 慢性化膿性中耳炎

- WHO IRIS のレコード（https://iris.who.int/handle/10665/42941 ）と文書自体の奥付表示：「**© World Health Organization 2004. All rights reserved.**」（ISBN 92-4-159158-7、書誌一致）。
- **判定：RESTRICTED**（WHO の刊行物。CC 表示なし。米国連邦政府の著作物ではないため GOV_US には該当しない）

## 18. SRC-3740（PH-001・PH-002・PH-004）NICE guideline NG69 摂食障害

- 当初、NICE の公式ページ（https://www.nice.org.uk/guidance/ng69 ）はアクセス制限（403）のため権利表示をテキストとして確認できず「確認できず」としたが、2026-11-23 にユーザーがアップロードした NICE 公式 PDF（刊行版）で表示を確認し、判定を更新した。
- PDF の書誌：『Eating disorders: recognition and treatment』NICE guideline NG69、Published: 23 May 2017、Last updated: 16 December 2020（1ページ目）、ISBN 978-1-4731-2508-7（45ページ目）。マスター登録（NG69、2017）と一致する現行の刊行版（その後の minor changes を含む版）。
- 権利表示（1ページ目および全ページのフッター）：「**© NICE 2025. All rights reserved. Subject to Notice of rights (https://www.nice.org.uk/terms-and-conditions#notice-of-rights)**」。文書内に CC ライセンスや Open Government Licence の表示はない。
- Notice of rights の内容（NICE 利用条件 第18項）：英国国内では NICE 独自の「NICE UK Open Content Licence」の下で再利用が認められるが、これは CC ライセンスではない。英国外では、個人利用・学習・個人的調査を除き、複製・翻訳・配布等には NICE の事前の書面による合意が必要で、ライセンスと料金の対象となり得る（18.2）。AI 目的の利用も承認手続きとライセンスが必要（18.3）。
- **判定：RESTRICTED**（© NICE、All rights reserved で CC 表示がなく、利用は NICE 独自の Notice of rights に従う。英国の公的機関の著作物であり、GOV_US・GOV_JP のいずれにも該当しない）

## 19. SRC-436（IL-044・IL-045・IL-046）Am J Respir Crit Care Med 2016 LAM ガイドライン

- 書誌の特定：マスターは DOI・PMID が空欄だったため PubMed で同定した。McCormack FX, et al. Am J Respir Crit Care Med. 2016 Sep 15;194(6):748-761. DOI **10.1164/rccm.201607-1384ST**、PMID **27628078**。
- PMC の刊行版ページ（PMC5803656、https://pmc.ncbi.nlm.nih.gov/articles/PMC5803656/ ）の表示：「**Copyright © 2016 by the American Thoracic Society**」。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：DOI 10.1164/rccm.201607-1384ST、PMID 27628078、PMCID PMC5803656 の3点がマスター未登録。

## 20. SRC-477（LC-016・LC-017・LC-018）Dtsch Arztebl Int 2012 肺転移の外科治療

- PMC の刊行版ページ（PMC3476611、https://pmc.ncbi.nlm.nih.gov/articles/PMC3476611/ ）：Deutscher Ärzte-Verlag 提供の刊行版で、CC ライセンスの表示はない（© Deutscher Ärzte-Verlag）。
- Crossref（DOI 10.3238/arztebl.2012.0645）：license 欄なし。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：マスターは PMID が空欄。正しくは PMID **23094000**、PMCID **PMC3476611**（PubMed で確認）。

## 21. SRC-602（GN-036 ほか3枚）J Am Soc Nephrol 2013 Alport 症候群ガイドライン

- Crossref（DOI 10.1681/ASN.2012020148）：license 欄なし。書誌（24(3):364-375、PMID 23349312）は PubMed と一致。JASN の通常記事（© American Society of Nephrology）。
- **判定：RESTRICTED**

## 22. SRC-821（RP-013 ほか3枚）Am J Obstet Gynecol 2018 月経前症候群

- Crossref（DOI 10.1016/j.ajog.2017.05.045）：license 欄はテキストマイニング用のみ（CC 表示なし）。Elsevier の通常記事。
- **判定：RESTRICTED**

## 23. SRC-828（RP-025・EN-012・EN-013）J Clin Endocrinol Metab 2011 高プロラクチン血症ガイドライン

- Crossref（DOI 10.1210/jc.2010-1692）：license 欄なし。書誌（96(2):273-288、PMID 21296991）は PubMed と一致。© Endocrine Society。
- **判定：RESTRICTED**

## 24. SRC-845（RP-046 ほか3枚）Menopause 2012 STRAW+10

- PMC 収載版（PMC3340903）は**著者原稿**（Author Manuscript のバナー表示）のため刊行版の根拠に使わない。
- Crossref（DOI 10.1097/gme.0b013e31824d8f40）：license 欄なし。刊行版は © The North American Menopause Society（Lippincott Williams & Wilkins）で CC 表示なし。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：PMCID PMC3340903（著者原稿）がマスター未登録。

## 25. SRC-992（MT-027・OS-005・OS-006）Arthritis Care Res 2020 痛風ガイドライン

- PMC 収載版（PMC10563586）は**著者原稿**のため根拠に使わない。
- Crossref（DOI 10.1002/acr.24180）：license 欄の刊行版（vor）は Wiley の通常利用条件（http://onlinelibrary.wiley.com/termsAndConditions#vor ）で、CC ライセンスではない。© American College of Rheumatology。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：PMCID PMC10563586（著者原稿）がマスター未登録。

## 26. SRC-101（NG-004・NG-005）日本神経消化器病学会ウェブサイト『沿革』

- 書誌の特定：マスターは書誌が空欄だったため、カード NG-004・NG-005 の記載から特定した。日本神経消化器病学会の公式ウェブサイト（UMIN PLAZA、http://plaza.umin.ac.jp/neuro-g/ ）の『沿革』ページ。
- 学会のウェブサイトで、CC ライセンスの表示はない。府省・公的機関の資料ではないため GOV_JP には該当しない。
- **判定：RESTRICTED**（CC 表示なし）

## 27. SRC-1081（SK-017・SK-018）Br J Clin Pharmacol 2024 薬疹レビュー

- Crossref（DOI 10.1111/bcp.15490）：license 欄の刊行版（vor）は Wiley の通常利用条件（termsAndConditions#vor）で、CC ライセンスではない。
- 出版社ページ（Wiley）はアクセス制限（403）のため表示を直接確認できなかった。
- **判定：RESTRICTED**

## 28. SRC-1102（DT-007・DT-009）Pediatrics 2019 乳児血管腫ガイドライン

- Crossref（DOI 10.1542/peds.2018-3475）：license 欄なし。© American Academy of Pediatrics で CC 表示なし。
- **判定：RESTRICTED**

## 29. SRC-116（NG-042・NG-043）イリボー錠 添付文書

- 書誌の特定：マスターは書誌が空欄だったため、カード NG-042・NG-043 の記載から特定した。イリボー錠2.5μg・5μg（ラモセトロン塩酸塩）添付文書、2021年3月改訂（第2版）、アステラス製薬。
- PMDA の添付文書ページ（https://www.pmda.go.jp/PmdaSearch/iyakuDetail/800126_2399014F1026_1_15 ）で同版を確認。製造販売業者（アステラス製薬）の作成文書で、CC ライセンスの表示はない。
- **判定：RESTRICTED**（CC 表示なし）

## 30. SRC-1163（SD-003・SD-004）J Am Acad Dermatol 2020 天疱瘡の診断と管理

- PMC 収載版（PMC7313440）は**著者原稿**のため根拠に使わない。
- Crossref（DOI 10.1016/j.jaad.2018.02.021）：license 欄はテキストマイニング用のみ（CC 表示なし）。© American Academy of Dermatology（Elsevier）。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：PMCID PMC7313440（著者原稿）がマスター未登録。

## 31. SRC-1185（SD-032・SD-055）J Eur Acad Dermatol Venereol 2014 SSSS

- Crossref（DOI 10.1111/jdv.12541）：license 欄の刊行版（vor）は Wiley の通常利用条件で、CC ライセンスではない。© European Academy of Dermatology and Venereology。
- **判定：RESTRICTED**

## 32. SRC-1188（SD-038・SD-039）Am Fam Physician 2025 白癬感染症

- 出版社（AAFP）の表示は「© American Academy of Family Physicians」で CC 表示なし（刊行版 PDF はアクセス制限のため直接確認できず、マスター記録と同誌の刊行形式による）。PubMed（PMID 41118183）で書誌（112(4):382-392）一致。
- **判定：RESTRICTED**

## 33. SRC-1191（SD-042・SD-043）J Dermatol 2017 疥癬ガイドライン（第3版）

- Crossref（DOI 10.1111/1346-8138.13896）：license 欄の刊行版（vor）は Wiley の通常利用条件で、CC ライセンスではない。© Japanese Dermatological Association。
- **判定：RESTRICTED**

## 34. SRC-1192（SD-044・SD-057）J Am Acad Dermatol 2007 単純ヘルペス

- Crossref（DOI 10.1016/j.jaad.2007.06.027）：license 欄はテキストマイニング用のみ（CC 表示なし）。© American Academy of Dermatology（Elsevier）。
- **判定：RESTRICTED**

## 35. SRC-1194（SD-046・SD-059）Br J Dermatol 2014 疣贅ガイドライン

- Crossref（DOI 10.1111/bjd.13310）：license 欄の刊行版（vor）は Wiley の通常利用条件で、CC ライセンスではない。© British Association of Dermatologists。
- **判定：RESTRICTED**

## 36. SRC-1252（EY-002・EY-003）Dtsch Arztebl Int 2016 屈折異常

- PMC の刊行版ページ（PMC5143802、https://pmc.ncbi.nlm.nih.gov/articles/PMC5143802/ ）：Deutscher Ärzte-Verlag 提供の刊行版で、CC ライセンスの表示はない。
- Crossref（DOI 10.3238/arztebl.2016.0693）：license 欄なし。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：PMCID **PMC5143802**（刊行版）がマスター未登録。

## 37. SRC-1254（EY-005・EY-006）Am Fam Physician 2015 眼瞼の発赤・腫脹

- 出版社（AAFP）の刊行版 PDF 冒頭の表示：「Copyright © 2015 American Academy of Family Physicians.」（Am Fam Physician. 2015;92(2):106-112）
- **判定：RESTRICTED**

## 38. SRC-1255（EY-007・EY-008）Am Fam Physician 1998 眼瞼疾患

- 出版社（AAFP）の表示は「© American Academy of Family Physicians」で CC 表示なし（1998年当時の AFP の刊行形式。記事ページは AAFP サイトに現存）。書誌（57(11):2695-2702、PMID 9636333）は PubMed と一致。
- **判定：RESTRICTED**

## 39. SRC-1257（EY-014・EY-015）Ophthalmology 2017 感染性角膜炎

- PMC 収載版（PMC5710829）は**著者原稿**のため根拠に使わない。
- Crossref（DOI 10.1016/j.ophtha.2017.05.012）：license 欄はテキストマイニング用のみ（CC 表示なし）。© Elsevier / American Academy of Ophthalmology。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：PMCID PMC5710829（著者原稿）がマスター未登録（マスターの注記「著者原稿が PMC 収載」と対応）。

## 40. SRC-1258（EY-016・EY-051）Curr Infect Dis Rep 2012 涙嚢炎

- Crossref（DOI 10.1007/s11908-012-0238-8）：license 欄は Springer のテキストマイニング用のみ（CC 表示なし）。© Springer Science+Business Media, LLC 2012。
- **判定：RESTRICTED**

## 41. SRC-1264（EY-022・EY-026）Lancet 2012 角膜移植

- Crossref（DOI 10.1016/S0140-6736(12)60437-1）：license 欄はテキストマイニング用と STM 許可ポリシーのみ（CC 表示なし）。© Elsevier（The Lancet）。
- **判定：RESTRICTED**

## 42. SRC-1276（EY-038・EY-061）Surv Ophthalmol 2022 乳頭浮腫

- Crossref（DOI 10.1016/j.survophthal.2021.11.007）：license 欄はテキストマイニング用と STM 許可ポリシーのみ（CC 表示なし）。Elsevier の通常記事。
- **判定：RESTRICTED**
- 備考（書誌の補完候補）：マスターの citation は「67(4)」まででページが未登録。PubMed（PMID 34813854）では 67(4):**1135-1159**。

## 43. SRC-1288（RE-008・RE-009）Am Fam Physician 2004 網膜剥離

- 出版社（AAFP）の刊行版 PDF の表示：「Copyright© 2004 American Academy of Family Physicians.」（Am Fam Physician. 2004;69:1691-8）
- **判定：RESTRICTED**

## 44. SRC-1295（NB-026・RE-016）Pediatrics 2018 未熟児網膜症スクリーニング

- Crossref（DOI 10.1542/peds.2018-3061）：license 欄なし。© 2018 American Academy of Pediatrics で CC 表示なし。
- **判定：RESTRICTED**

## 45. SRC-1349（OT-011・OT-046）Otolaryngol Head Neck Surg 2016 滲出性中耳炎ガイドライン

- Crossref（DOI 10.1177/0194599815623467）：license 欄の刊行版（vor）は Wiley の通常利用条件で、CC ライセンスではない。
- **判定：RESTRICTED**

## 46. SRC-1355（OT-020・OT-021）Otolaryngol Head Neck Surg 2019 突発性難聴ガイドライン

- Crossref（DOI 10.1177/0194599819859885）：license 欄の刊行版（vor）は Wiley の通常利用条件で、CC ライセンスではない。
- **判定：RESTRICTED**

## 47. SRC-1356（OT-025・OT-026）Nat Rev Dis Primers 2017 先天性難聴

- PMC 収載版（PMC5675031）は**著者原稿**のため根拠に使わない。
- Crossref（DOI 10.1038/nrdp.2016.94）：license 欄は Springer Nature のテキストマイニング用のみ（CC 表示なし）。© Springer Nature。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：PMCID PMC5675031（著者原稿）がマスター未登録。

## 48. SRC-1363（OT-034・OT-050）CNS Neurosci Ther 2016 動揺病

- PMC の刊行版ページ（PMC6492910、https://pmc.ncbi.nlm.nih.gov/articles/PMC6492910/ ）の表示：「**© 2015 John Wiley & Sons Ltd**」（CC 表示なし）。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：PMCID **PMC6492910**（刊行版）がマスター未登録。

## 49. SRC-1367（OT-039・OT-044）Neurosurg Rev 2023 Collet-Sicard 症候群

- Crossref（DOI 10.1007/s10143-023-02145-7）：license 欄は Springer Nature のテキストマイニング用のみ（CC 表示なし）。© Springer Nature（著者から出版社への exclusive licence）。
- **判定：RESTRICTED**

## 50. SRC-1432（OR-002・OR-034）Dent Clin North Am 2014 再発性アフタ性口内炎

- PMC のページ（PMC3964366、https://pmc.ncbi.nlm.nih.gov/articles/PMC3964366/ ）の表示：「**© 2013 Elsevier Inc. All rights reserved.**」（収載版は著者原稿 NIHMS550882 だが、著作権表示は刊行版と同一の © Elsevier）。
- Crossref（DOI 10.1016/j.cden.2013.12.002）：license 欄はテキストマイニング用のみ。
- **判定：RESTRICTED**
- 備考（識別子の補完候補）：PMCID PMC3964366（著者原稿）がマスター未登録。

---

## 書誌・識別子の食い違いと補完候補（まとめ）

| SRC | 内容 |
|---|---|
| SRC-252 | **DOI の食い違い**：登録値 10.2143/AC.71.1.3132092 は Crossref にレコードなし。同一論文の Crossref レコードは 10.1080/AC.71.1.3132092（Informa UK） |
| SRC-009 | DOI の補完候補：10.1055/s-0042-100456（PubMed。マスターは空欄） |
| SRC-436 | DOI・PMID・PMCID の補完候補：10.1164/rccm.201607-1384ST／27628078／PMC5803656（マスターはすべて空欄） |
| SRC-477 | PMID・PMCID の補完候補：23094000／PMC3476611（マスターは PMID 空欄） |
| SRC-5227 | 書誌の補完候補：title が仮置き表記。正規書誌は Endoscopy. 2026;58(8):899-924、PMID 42127996 |
| SRC-410 | PMCID の補完候補：PMC9851481（刊行版） |
| SRC-1187 | PMCID の補完候補：PMC6302357（刊行版） |
| SRC-1252 | PMCID の補完候補：PMC5143802（刊行版） |
| SRC-1363 | PMCID の補完候補：PMC6492910（刊行版） |
| SRC-845 | PMCID の補完候補：PMC3340903（著者原稿） |
| SRC-992 | PMCID の補完候補：PMC10563586（著者原稿） |
| SRC-1163 | PMCID の補完候補：PMC7313440（著者原稿） |
| SRC-1257 | PMCID の補完候補：PMC5710829（著者原稿） |
| SRC-1356 | PMCID の補完候補：PMC5675031（著者原稿） |
| SRC-1432 | PMCID の補完候補：PMC3964366（著者原稿） |
| SRC-1276 | ページの補完候補：67(4):1135-1159（マスターはページ未登録） |
| SRC-115・SRC-116・SRC-101 | マスターの書誌欄が空欄だった3件は、カード側の記載から書誌を特定した（SRC-115＝アコファイド錠添付文書、SRC-116＝イリボー錠添付文書、SRC-101＝日本神経消化器病学会ウェブサイト『沿革』） |

---

## 一覧表

| SRC | 判定 | ライセンスの表示 | 根拠の URL | 備考 |
|---|---|---|---|---|
| SRC-290 | RESTRICTED | All rights are reserved to the Japanese Circulation Society（© 日本循環器学会、CC表示なし） | https://www.jstage.jst.go.jp/article/circj/87/10/87_CJ-22-0794/_article | 刊行版PDF冒頭で確認。Crossrefにlicense欄なし |
| SRC-440 | RESTRICTED | © American Heart Association（CC表示なし） | https://www.ahajournals.org/doi/10.1161/CIR.0000000000001415 | 出版社ページ・CrossrefともCC表示なし |
| SRC-1180 | RESTRICTED | © The Author 2014, Oxford University Press（CC表示なし） | https://api.crossref.org/works/10.1093/cid/ciu296 | Crossrefにlicense欄なし |
| SRC-1256 | RESTRICTED | © American Academy of Ophthalmology / Elsevier | https://api.crossref.org/works/10.1016/j.ophtha.2018.10.020 | CrossrefはTDM用ライセンスのみ |
| SRC-1436 | RESTRICTED | © American Cancer Society（CC表示なし） | https://api.crossref.org/works/10.3322/canjclin.52.4.195 | 出版社ページは403で未確認。CrossrefはTDM用のみ |
| SRC-009 | RESTRICTED | © Georg Thieme Verlag KG Stuttgart · New York | https://www.thieme-connect.de/products/ejournals/abstract/10.1055/s-0042-100456 | DOI 10.1055/s-0042-100456 がマスター未登録（補完候補） |
| SRC-252 | RESTRICTED | CC表示なし（Taylor & Francis） | https://api.crossref.org/works/10.1080/AC.71.1.3132092 | 登録DOI 10.2143/AC.71.1.3132092 はCrossrefにレコードなし（DOIの食い違い） |
| SRC-410 | RESTRICTED | CC BY-NC-ND 4.0（Crossref・刊行版）／© 2022 American Thoracic Society（PMC刊行版） | https://api.crossref.org/works/10.1164/rccm.202202-0399ST | PMCID PMC9851481 がマスター未登録（補完候補） |
| SRC-5227 | RESTRICTED | © 2026. European Society of Gastrointestinal Endoscopy. All rights reserved. | https://www.thieme-connect.de/products/ejournals/abstract/10.1055/a-2863-8314 | 正規書誌は Endoscopy 2026;58(8):899-924、PMID 42127996（マスターのtitleは仮置き、pmid空欄） |
| SRC-830 | RESTRICTED | Elsevier オープンアクセス・ユーザーライセンス 1.0（CCではない） | https://api.crossref.org/works/10.1016/j.fertnstert.2015.03.019 | Crossrefの刊行版ライセンス（2022-05-27開始） |
| SRC-1107 | RESTRICTED | Copyright© 2003 American Academy of Family Physicians. | https://www.aafp.org/pubs/afp/issues/2003/0215/p729.html | 刊行版PDF冒頭で確認 |
| SRC-115 | RESTRICTED | CC表示なし（ゼリア新薬工業の添付文書） | https://www.pmda.go.jp/PmdaSearch/iyakuDetail/380077_2399015F1020_1_09 | マスターの書誌空欄をカードから特定（アコファイド錠100mg添付文書 2023年8月改訂第3版） |
| SRC-1168 | RESTRICTED | © American Medical Association（CC表示なし） | https://api.crossref.org/works/10.1001/jama.2020.4006 | Crossrefにlicense欄なし |
| SRC-1186 | RESTRICTED | © Massachusetts Medical Society（CC表示なし） | https://www.nejm.org/doi/full/10.1056/NEJMra1600673 | Crossrefにlicense欄なし |
| SRC-1187 | RESTRICTED | Copyright © 2018 American Society for Microbiology. All Rights Reserved. | https://pmc.ncbi.nlm.nih.gov/articles/PMC6302357/ | PMCID PMC6302357 がマスター未登録（補完候補、刊行版） |
| SRC-1265 | RESTRICTED | © Nature Portfolio (Springer Nature)（CC表示なし） | https://api.crossref.org/works/10.1038/nrdp.2015.14 | CrossrefはTDM用のみ |
| SRC-1350 | RESTRICTED | © World Health Organization 2004. All rights reserved. | https://iris.who.int/handle/10665/42941 | WHO刊行物（GOV_US非該当） |
| SRC-3740 | RESTRICTED | © NICE 2025. All rights reserved. Subject to Notice of rights（CC表示なし） | https://www.nice.org.uk/guidance/ng69 | 公式 PDF（アップロード版）で表示を確認。Notice of rights により英国外での利用は原則として NICE の事前の書面合意が必要 |
| SRC-436 | RESTRICTED | Copyright © 2016 by the American Thoracic Society | https://pmc.ncbi.nlm.nih.gov/articles/PMC5803656/ | DOI 10.1164/rccm.201607-1384ST・PMID 27628078・PMCID PMC5803656 がマスター未登録（補完候補） |
| SRC-477 | RESTRICTED | © Deutscher Ärzte-Verlag（CC表示なし） | https://pmc.ncbi.nlm.nih.gov/articles/PMC3476611/ | PMID 23094000・PMCID PMC3476611 がマスター未登録（補完候補） |
| SRC-602 | RESTRICTED | © American Society of Nephrology（CC表示なし） | https://api.crossref.org/works/10.1681/ASN.2012020148 | Crossrefにlicense欄なし |
| SRC-821 | RESTRICTED | © Elsevier（CC表示なし） | https://api.crossref.org/works/10.1016/j.ajog.2017.05.045 | CrossrefはTDM用のみ |
| SRC-828 | RESTRICTED | © Endocrine Society（CC表示なし） | https://api.crossref.org/works/10.1210/jc.2010-1692 | Crossrefにlicense欄なし |
| SRC-845 | RESTRICTED | © The North American Menopause Society（CC表示なし） | https://api.crossref.org/works/10.1097/gme.0b013e31824d8f40 | PMC収載版は著者原稿のため根拠に使わず。PMCID PMC3340903（著者原稿）が未登録 |
| SRC-992 | RESTRICTED | © American College of Rheumatology（Wiley通常条件、CCではない） | https://api.crossref.org/works/10.1002/acr.24180 | PMC収載版は著者原稿のため根拠に使わず。PMCID PMC10563586（著者原稿）が未登録 |
| SRC-101 | RESTRICTED | CC表示なし（学会ウェブサイト） | http://plaza.umin.ac.jp/neuro-g/riji.html | マスターの書誌空欄をカードから特定（日本神経消化器病学会ウェブサイト『沿革』） |
| SRC-1081 | RESTRICTED | Wiley通常条件（CCではない） | https://api.crossref.org/works/10.1111/bcp.15490 | 出版社ページは403で未確認。Crossrefの刊行版ライセンスによる |
| SRC-1102 | RESTRICTED | © American Academy of Pediatrics（CC表示なし） | https://api.crossref.org/works/10.1542/peds.2018-3475 | Crossrefにlicense欄なし |
| SRC-116 | RESTRICTED | CC表示なし（アステラス製薬の添付文書） | https://www.pmda.go.jp/PmdaSearch/iyakuDetail/800126_2399014F1026_1_15 | マスターの書誌空欄をカードから特定（イリボー錠添付文書 2021年3月改訂第2版） |
| SRC-1163 | RESTRICTED | © American Academy of Dermatology（CC表示なし） | https://api.crossref.org/works/10.1016/j.jaad.2018.02.021 | PMC収載版は著者原稿のため根拠に使わず。PMCID PMC7313440（著者原稿）が未登録 |
| SRC-1185 | RESTRICTED | © European Academy of Dermatology and Venereology（Wiley通常条件） | https://api.crossref.org/works/10.1111/jdv.12541 | Crossrefの刊行版ライセンスによる |
| SRC-1188 | RESTRICTED | © American Academy of Family Physicians（CC表示なし） | https://pubmed.ncbi.nlm.nih.gov/41118183/ | 刊行版PDFはアクセス制限のためマスター記録と同誌の刊行形式による |
| SRC-1191 | RESTRICTED | © Japanese Dermatological Association（Wiley通常条件） | https://api.crossref.org/works/10.1111/1346-8138.13896 | Crossrefの刊行版ライセンスによる |
| SRC-1192 | RESTRICTED | © American Academy of Dermatology（CC表示なし） | https://api.crossref.org/works/10.1016/j.jaad.2007.06.027 | CrossrefはTDM用のみ |
| SRC-1194 | RESTRICTED | © British Association of Dermatologists（Wiley通常条件） | https://api.crossref.org/works/10.1111/bjd.13310 | Crossrefの刊行版ライセンスによる |
| SRC-1252 | RESTRICTED | © Deutscher Ärzte-Verlag（CC表示なし） | https://pmc.ncbi.nlm.nih.gov/articles/PMC5143802/ | PMCID PMC5143802（刊行版）がマスター未登録（補完候補） |
| SRC-1254 | RESTRICTED | Copyright © 2015 American Academy of Family Physicians. | https://www.aafp.org/pubs/afp/issues/2015/0715/p106.html | 刊行版PDF冒頭で確認 |
| SRC-1255 | RESTRICTED | © American Academy of Family Physicians（CC表示なし） | https://pubmed.ncbi.nlm.nih.gov/9636333/ | 同誌の刊行形式とマスター記録による |
| SRC-1257 | RESTRICTED | © Elsevier / American Academy of Ophthalmology（CC表示なし） | https://api.crossref.org/works/10.1016/j.ophtha.2017.05.012 | PMC収載版は著者原稿のため根拠に使わず。PMCID PMC5710829（著者原稿）が未登録 |
| SRC-1258 | RESTRICTED | © Springer Science+Business Media, LLC 2012 | https://api.crossref.org/works/10.1007/s11908-012-0238-8 | CrossrefはTDM用のみ |
| SRC-1264 | RESTRICTED | © Elsevier (The Lancet)（CC表示なし） | https://api.crossref.org/works/10.1016/S0140-6736(12)60437-1 | CrossrefはTDM・STMポリシーのみ |
| SRC-1276 | RESTRICTED | © Elsevier（CC表示なし） | https://api.crossref.org/works/10.1016/j.survophthal.2021.11.007 | ページ 1135-1159 がマスター未登録（補完候補） |
| SRC-1288 | RESTRICTED | Copyright© 2004 American Academy of Family Physicians. | https://www.aafp.org/pubs/afp/issues/2004/0401/p1691.html | 刊行版PDFで確認 |
| SRC-1295 | RESTRICTED | © 2018 American Academy of Pediatrics（CC表示なし） | https://api.crossref.org/works/10.1542/peds.2018-3061 | Crossrefにlicense欄なし |
| SRC-1349 | RESTRICTED | Wiley通常条件（CCではない） | https://api.crossref.org/works/10.1177/0194599815623467 | Crossrefの刊行版ライセンスによる |
| SRC-1355 | RESTRICTED | Wiley通常条件（CCではない） | https://api.crossref.org/works/10.1177/0194599819859885 | Crossrefの刊行版ライセンスによる |
| SRC-1356 | RESTRICTED | © Springer Nature（CC表示なし） | https://api.crossref.org/works/10.1038/nrdp.2016.94 | PMC収載版は著者原稿のため根拠に使わず。PMCID PMC5675031（著者原稿）が未登録 |
| SRC-1363 | RESTRICTED | © 2015 John Wiley & Sons Ltd（CC表示なし） | https://pmc.ncbi.nlm.nih.gov/articles/PMC6492910/ | PMCID PMC6492910（刊行版）がマスター未登録（補完候補） |
| SRC-1367 | RESTRICTED | © Springer Nature（exclusive licence、CC表示なし） | https://api.crossref.org/works/10.1007/s10143-023-02145-7 | CrossrefはTDM用のみ |
| SRC-1432 | RESTRICTED | © 2013 Elsevier Inc. All rights reserved. | https://pmc.ncbi.nlm.nih.gov/articles/PMC3964366/ | PMCページの著作権表示で確認。PMCID PMC3964366（著者原稿）が未登録 |
