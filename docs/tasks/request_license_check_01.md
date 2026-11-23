# ライセンス未確認（UNKNOWN）の出典の照合の依頼（第1回：50件）

依頼者：三原弘（2026-11-23）。11月23日の7件の照合（id_check_20261123b.md）と同じ方法で、下の50件の出典のライセンスを確かめてください。結果は1つの Markdown（license_check_01.md）にまとめてください。**照合の前に、hm-cmed/cleanroom-facts の最新版を取得してください。**

ライセンスがまだ確認できていない出典は332件（カード473枚）あります。使っているカードの多い順に50件ずつ、7回に分けて頼む予定で、今回はその1回目（カード154枚分）です。

## 判定の区分

| 判定 | 条件 |
|---|---|
| OPEN | 刊行版（version of record）が CC BY または CC0 |
| RESTRICTED | CC BY-NC・CC BY-ND・CC BY-NC-ND・CC BY-SA・CC BY-NC-SA、または CC 表示がない（©出版社・学会、All rights reserved など） |
| GOV_US | 米国連邦政府の著作物（CDC・NIH・NCI・AHRQ など。第三者の素材は除く） |
| GOV_JP | 日本の府省・公的機関の資料で、政府標準利用規約・公共データ利用規約が適用されるもの |
| 確認できず | 上のどれとも決められない（理由を書く） |

## 確かめ方

1. 刊行版の表示を優先する。根拠にする順は、出版社の論文ページ、PMC の論文ページ（著者原稿でないこと）、Crossref の license 欄（content-version が vor のもの）。
2. Unpaywall や OpenAlex だけを根拠にしない。
3. 著者原稿（PMC の NIHMS 版など）に付いた表示は、刊行版の区分には使わない。
4. 雑誌全体の方針（投稿規程など）を根拠にする場合は、その論文の発行時期に方針が適用されていたことを確かめる。
5. 項目ごとに、根拠にしたページの URL と、表示の要約を書く。本文は保存しない。
6. 書誌や識別子（DOI・PMID・PMCID）の食い違いに気づいたら、あわせて書く。

## 結果の書き方

最後に、次の形の一覧表を付けてください（取り込みで機械的に読みます）。

| SRC | 判定 | ライセンスの表示 | 根拠の URL | 備考 |
|---|---|---|---|---|

## 対象の50件

| # | SRC | 出典（書誌） | DOI | PMID | 今のライセンスの記載 | 使っているカード |
|---|---|---|---|---|---|---|
| 1 | SRC-290 | Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621 | 10.1253/circj.CJ-22-0794 | 37661428 | 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会） | VS-001・VS-002・VS-003・VS-007・VS-008・VS-009 ほか（14枚） |
| 2 | SRC-440 | Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism  | 10.1161/CIR.0000000000001415 |  | 未確認 | PV-002・PV-003・PV-004・PV-005・PV-006・PV-007 ほか（10枚） |
| 3 | SRC-1180 | Stevens DL, Bisno AL, Chambers HF, et al. Practice guidelines for the diagnosis and management of skin and soft tissue infections: 2014 update by the Infectious | 10.1093/cid/ciu296 | 24947530 | © The Author 2014, Oxford University Press（CC表示なし） | BA-031・SD-025・SD-028・SD-030・SD-054（5枚） |
| 4 | SRC-1256 | Varu DM, Rhee MK, Akpek EK, Amescua G, Farid M, Garcia-Ferrer FJ, Lin A, Musch DC, Mah FS, Dunn SP; American Academy of Ophthalmology Cornea/External Disease Pa | 10.1016/j.ophtha.2018.10.020 | 30366797 | © American Academy of Ophthalmology / Elsevier | EY-009・EY-010・EY-011・EY-012・EY-013（5枚） |
| 5 | SRC-1436 | Neville BW, Day TA. Oral cancer and precancerous lesions. CA Cancer J Clin. 2002;52(4):195-215. | 10.3322/canjclin.52.4.195 | 12139232 | ライセンス未確認 | OR-006・OR-007・OR-008・OR-009・OR-023（5枚） |
| 6 | SRC-009 | Birk M, ESGE異物GL |  | 26862844 | 未確認 | ES-069・ES-070・ES-071・ES-072（4枚） |
| 7 | SRC-252 | Van Camp G, Pasquet A, Sinnaeve P, et al. Summary 2015 ESC guidelines（心膜疾患ほか）. Acta Cardiol 2016;71:7-13 | 10.2143/AC.71.1.3132092 |  | 未確認 | MP-023・MP-024・MP-025・MP-026（4枚） |
| 8 | SRC-410 | Raghu G, Remy-Jardin M, Richeldi L, et al. Idiopathic Pulmonary Fibrosis (an Update) and Progressive Pulmonary Fibrosis in Adults: An Official ATS/ERS/JRS/ALAT  | 10.1164/rccm.202202-0399ST | 35486072 | 未確認 | IL-003・IL-004・IL-005・IL-006（4枚） |
| 9 | SRC-5227 | ESGE 2026（PubMed抄録 PMID 42127996） | 10.1055/a-2863-8314 |  | 未確認 | UG-010・UG-015・UG-017・UG-018（4枚） |
| 10 | SRC-830 | Practice Committee of the American Society for Reproductive Medicine. Diagnostic evaluation of the infertile female: a committee opinion. Fertility and Sterilit | 10.1016/j.fertnstert.2015.03.019 | 25936238 | 未確認 | RP-028・RP-030・RP-038・RP-039（4枚） |
| 11 | SRC-1107 | Luba MC, Bangs SA, Mohler AM, Stulberg DL. Common benign skin tumors. Am Fam Physician. 2003;67(4):729-738 |  | 12613727 | ライセンス表示を確認できず | DT-013・DT-015・DT-016（3枚） |
| 12 | SRC-115 |  |  |  |  | NG-039・NG-040・NG-041（3枚） |
| 13 | SRC-1168 | Armstrong AW, Read C. Pathophysiology, Clinical Presentation, and Treatment of Psoriasis: A Review. JAMA. 2020;323(19):1945-1960. | 10.1001/jama.2020.4006 | 32427307 | ライセンス表示を確認できず | SD-011・SD-012・SD-013（3枚） |
| 14 | SRC-1186 | Stevens DL, Bryant AE. Necrotizing Soft-Tissue Infections. N Engl J Med. 2017;377(23):2253-2265. | 10.1056/NEJMra1600673 | 29211672 | © Massachusetts Medical Society（CC表示なし） | SD-033・SD-034・SD-056（3枚） |
| 15 | SRC-1187 | Franco-Paredes C, Marcos LA, Henao-Martínez AF, et al. Cutaneous Mycobacterial Infections. Clin Microbiol Rev. 2019;32(1):e00069-18. | 10.1128/CMR.00069-18 | 30429139 | © American Society for Microbiology（CC表示なし） | SD-035・SD-036・SD-037（3枚） |
| 16 | SRC-1265 | Lam D, Rao SK, Ratra V, Liu Y, Mitchell P, King J, Tassignon MJ, Jonas J, Pang CP, Chang DF. Cataract. Nat Rev Dis Primers. 2015;1:15014 | 10.1038/nrdp.2015.14 | 27188414 | © Nature Portfolio (Springer Nature) | EY-023・EY-024・EY-025（3枚） |
| 17 | SRC-1350 | Acuin J. Chronic suppurative otitis media: burden of illness and management options. Geneva: World Health Organization; 2004. ISBN 92-4-159158-7. |  |  | © World Health Organization 2004（All rights reserved、CC表示なし） | OT-012・OT-015・OT-022（3枚） |
| 18 | SRC-3740 | National Institute for Health and Care Excellence. Eating disorders: recognition and treatment. NICE guideline NG69. 2017 |  |  |  | PH-001・PH-002・PH-004（3枚） |
| 19 | SRC-436 | McCormack FX, et al. Official American Thoracic Society/Japanese Respiratory Society Clinical Practice Guidelines: Lymphangioleiomyomatosis Diagnosis and Manage |  |  | 未確認 | IL-044・IL-045・IL-046（3枚） |
| 20 | SRC-477 | Pfannschmidt J, Egerer G, Bischof M, Thomas M, Dienemann H. Surgical Intervention for Pulmonary Metastases. Dtsch Arztebl Int 2012;109(40):645-651 | 10.3238/arztebl.2012.0645 |  | 表示なし | LC-016・LC-017・LC-018（3枚） |
| 21 | SRC-602 | Savige J, Gregory M, Gross O, Kashtan C, Ding J, Flinter F. Expert guidelines for the management of Alport syndrome and thin basement membrane nephropathy. J Am | 10.1681/ASN.2012020148 | 23349312 | ライセンス表示を確認できず（Crossref のレコードに license 欄なし） | GN-036・GN-037・GN-038（3枚） |
| 22 | SRC-821 | Yonkers KA, Simoni MK. Premenstrual disorders. Am J Obstet Gynecol. 2018;218(1):68-74. | 10.1016/j.ajog.2017.05.045 | 28571724 | ライセンス表示を確認できず | RP-013・RP-014・RP-018（3枚） |
| 23 | SRC-828 | Melmed S, Casanueva FF, Hoffman AR, et al. Diagnosis and Treatment of Hyperprolactinemia: An Endocrine Society Clinical Practice Guideline. The Journal of Clini | 10.1210/jc.2010-1692 | 21296991 | 未確認 | RP-025・EN-012・EN-013（3枚） |
| 24 | SRC-845 | Harlow SD, Gass M, Hall JE, et al. Executive summary of the Stages of Reproductive Aging Workshop + 10: addressing the unfinished agenda of staging reproductive | 10.1097/gme.0b013e31824d8f40 | 22343510 | PMC 収載は著者原稿で CC ライセンスの表示なし | RP-046・RP-047・RP-058（3枚） |
| 25 | SRC-992 | FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. Arthritis Care Res (Hoboken). 2020;72(6): | 10.1002/acr.24180 | 32391934 | PMC収載は著者原稿。CC表示なし（© American College of Rheumatology） | MT-027・OS-005・OS-006（3枚） |
| 26 | SRC-101 |  |  |  |  | NG-004・NG-005（2枚） |
| 27 | SRC-1081 | Del Pozzo-Magaña BR, Liy-Wong C. Drugs and the skin: A concise review of cutaneous adverse drug reactions. British Journal of Clinical Pharmacology. 2024;90(8): | 10.1111/bcp.15490 | 35974692 | Wiley（CCライセンス表示を確認できず） | SK-017・SK-018（2枚） |
| 28 | SRC-1102 | Krowchuk DP, Frieden IJ, Mancini AJ, et al. Clinical Practice Guideline for the Management of Infantile Hemangiomas. Pediatrics. 2019;143(1):e20183475 | 10.1542/peds.2018-3475 | 30584062 | ライセンス表示を確認できず | DT-007・DT-009（2枚） |
| 29 | SRC-116 |  |  |  |  | NG-042・NG-043（2枚） |
| 30 | SRC-1163 | Murrell DF, Peña S, Joly P, Marinovic B, Hashimoto T, Diaz LA, et al. Diagnosis and management of pemphigus: Recommendations of an international panel of expert | 10.1016/j.jaad.2018.02.021 | 29438767 | ライセンス表示を確認できず | SD-003・SD-004（2枚） |
| 31 | SRC-1185 | Handler MZ, Schwartz RA. Staphylococcal scalded skin syndrome: diagnosis and management in children and adults. J Eur Acad Dermatol Venereol. 2014;28(11):1418-1 | 10.1111/jdv.12541 | 24841497 | © European Academy of Dermatology and Venereology（CC表示なし） | SD-032・SD-055（2枚） |
| 32 | SRC-1188 | Caplan AS, Gold JAW, Smith DJ, Ely JW. Diagnosis and Management of Tinea Infections. Am Fam Physician. 2025;112(4):382-392. |  | 41118183 | © American Academy of Family Physicians（CC表示なし） | SD-038・SD-039（2枚） |
| 33 | SRC-1191 | Ishii N, Asai T, Asahina A, Ishiko A, et al. Guideline for the diagnosis and treatment of scabies in Japan (third edition): Executive Committee of Guideline for | 10.1111/1346-8138.13896 | 28561292 | © Japanese Dermatological Association（Wiley、CC表示なし） | SD-042・SD-043（2枚） |
| 34 | SRC-1192 | Fatahzadeh M, Schwartz RA. Human herpes simplex virus infections: epidemiology, pathogenesis, symptomatology, diagnosis, and management. J Am Acad Dermatol. 200 | 10.1016/j.jaad.2007.06.027 | 17939933 | © American Academy of Dermatology（Elsevier、CC表示なし） | SD-044・SD-057（2枚） |
| 35 | SRC-1194 | Sterling JC, Gibbs S, Haque Hussain SS, Mohd Mustapa MF, et al. British Association of Dermatologists' guidelines for the management of cutaneous warts 2014. Br | 10.1111/bjd.13310 | 25273231 | © British Association of Dermatologists（Wiley、CC表示なし） | SD-046・SD-059（2枚） |
| 36 | SRC-1252 | Schiefer U, Kraus C, Baumbach P, Ungewiß J, Michels R. Refractive errors: Epidemiology, Effects and Treatment Options. Dtsch Arztebl Int. 2016;113(41):693-702 | 10.3238/arztebl.2016.0693 | 27839543 | © Deutscher Ärzte-Verlag（PMC 収載版で CC 表示を確認できず） | EY-002・EY-003（2枚） |
| 37 | SRC-1254 | Carlisle RT, Digiovanni J. Differential Diagnosis of the Swollen Red Eyelid. Am Fam Physician. 2015;92(2):106-112 |  | 26176369 | © American Academy of Family Physicians | EY-005・EY-006（2枚） |
| 38 | SRC-1255 | Carter SR. Eyelid disorders: diagnosis and management. Am Fam Physician. 1998;57(11):2695-2702 |  | 9636333 | © American Academy of Family Physicians | EY-007・EY-008（2枚） |
| 39 | SRC-1257 | Austin A, Lietman T, Rose-Nussbaumer J. Update on the Management of Infectious Keratitis. Ophthalmology. 2017;124(11):1678-1689 | 10.1016/j.ophtha.2017.05.012 | 28942073 | © Elsevier / American Academy of Ophthalmology（著者原稿が PMC 収載） | EY-014・EY-015（2枚） |
| 40 | SRC-1258 | Pinar-Sueiro S, Sota M, Lerchundi TX, Gibelalde A, Berasategui B, Vilar B, Hernandez JL. Dacryocystitis: Systematic Approach to Diagnosis and Therapy. Curr Infe | 10.1007/s11908-012-0238-8 | 22286338 | © Springer Science+Business Media, LLC 2012 | EY-016・EY-051（2枚） |
| 41 | SRC-1264 | Tan DTH, Dart JKG, Holland EJ, Kinoshita S. Corneal transplantation. Lancet. 2012;379(9827):1749-1761 | 10.1016/S0140-6736(12)60437-1 | 22559901 | © Elsevier (The Lancet) | EY-022・EY-026（2枚） |
| 42 | SRC-1276 | Xie JS, Donaldson L, Margolin E. Papilledema: A review of etiology, pathophysiology, diagnosis, and management. Surv Ophthalmol. 2022;67(4). | 10.1016/j.survophthal.2021.11.007 | 34813854 | ライセンス表示を確認できず | EY-038・EY-061（2枚） |
| 43 | SRC-1288 | Gariano RF, Kim CH. Evaluation and management of suspected retinal detachment. Am Fam Physician. 2004;69(7):1691-1698. |  | 15086041 | © 2004 American Academy of Family Physicians（CC表示なし） | RE-008・RE-009（2枚） |
| 44 | SRC-1295 | Fierson WM; American Academy of Pediatrics Section on Ophthalmology; American Academy of Ophthalmology; American Association for Pediatric Ophthalmology and Str | 10.1542/peds.2018-3061 | 30478242 | © 2018 American Academy of Pediatrics（CC表示なし） | NB-026・RE-016（2枚） |
| 45 | SRC-1349 | Rosenfeld RM, Shin JJ, Schwartz SR, Coggins R, Gagnon L, Hackell JM, et al. Clinical Practice Guideline: Otitis Media with Effusion (Update). Otolaryngology–Hea | 10.1177/0194599815623467 | 26832942 | ライセンス表示を確認できず | OT-011・OT-046（2枚） |
| 46 | SRC-1355 | Chandrasekhar SS, Tsai Do BS, Schwartz SR, Bontempo LJ, Faucett EA, Finestone SA, et al. Clinical Practice Guideline: Sudden Hearing Loss (Update). Otolaryngolo | 10.1177/0194599819859885 | 31369359 | ライセンス表示を確認できず | OT-020・OT-021（2枚） |
| 47 | SRC-1356 | Korver AMH, Smith RJH, Van Camp G, Schleiss MR, Bitner-Glindzicz MAK, Lustig LR, Usami SI, Boudewyns AN. Congenital hearing loss. Nat Rev Dis Primers. 2017;3:16 | 10.1038/nrdp.2016.94 | 28079113 | © Springer Nature（CC表示なし） | OT-025・OT-026（2枚） |
| 48 | SRC-1363 | Zhang LL, Wang JQ, Qi RR, Pan LL, Li M, Cai YL. Motion Sickness: Current Knowledge and Recent Advance. CNS Neurosci Ther. 2016;22(1):15-24. | 10.1111/cns.12468 | 26452639 | © John Wiley & Sons（CC表示は Crossref・PMC で確認できず） | OT-034・OT-050（2枚） |
| 49 | SRC-1367 | Aguilera-Pena MP, Castiblanco MA, Osejo-Arcos V, Aponte-Caballero R, Gutierrez-Gomez S, Abaunza-Camacho JF, Guevara-Moriones N, Benavides-Burbano CA, Riveros-Ca | 10.1007/s10143-023-02145-7 | 37707587 | © Springer Nature（exclusive licence、CC表示なし） | OT-039・OT-044（2枚） |
| 50 | SRC-1432 | Akintoye SO, Greenberg MS. Recurrent aphthous stomatitis. Dent Clin North Am. 2014;58(2):281-297. | 10.1016/j.cden.2013.12.002 | 24655523 | ライセンス未確認 | OR-002・OR-034（2枚） |