# 第28回 事実票（ST・BT・NI）

> この版は Claude Code が `raw/28_ns_a.md`（Muse の原本）から機械的に作った。原本は YAML ブロックの開始行（```yaml）の後に改行がなく、カードが独自の形（assertion が文字列、condition・legal_basis・source_class・source_license・status・verifier が上の階層、provenance に locator）だった。これを、主張文・数値・識別子を変えずに標準の形へ移した：assertion → assertion.plain_statement_ja、condition → assertion.condition、ライセンスの3欄 → provenance、status・verifier → publication_info、provenance の source・doi・pmid・url は原本の出典表から写した。locator はスキーマに欄がないため、この版には入れていない（原本に残る）。

第Ⅸ章 神経・運動器の第1回。脳血管障害（ST)、脳腫瘍（BT)、神経・運動器の感染性・炎症性疾患（NI)。対象44項目（うち Ⅸ-1-E-③ 脳血管性認知症は依頼文の境界どおり ST では作らず、第29回 ND で作る）のうち、43項目すべてにカードがある。欠番はない。

## 1. 抽出元ホワイトリスト

| SRC | 出典 | DOI | PMID | ライセンス | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-874 | Müller HL, Merchant TE, Warmuth-Metz M, Martinez-Barbera JP, Puget S. Craniopharyngioma. Nature Reviews Disease Primers. 2019;5(1):75. | 10.1038/s41572-019-0125-9 | 31699993 | UNKNOWN | UNKNOWN | 既存出典（第20回で登録済み。本回では新しい番号を付けず既存番号を使用） |
| SRC-877 | Molitch ME. Diagnosis and Treatment of Pituitary Adenomas: A Review. JAMA. 2017;317(5):516-524. | 10.1001/jama.2016.19699 | 28170483 | UNKNOWN | UNKNOWN | 既存出典（第20回で登録済み。本回では新しい番号を付けず既存番号を使用） |
| SRC-884 | Rajasekaran S, Vanderpump M, Baldeweg S, et al. UK Guidelines for the Management of Pituitary Apoplexy. Clinical Endocrinology. 2011;74(1):9-20. | 10.1111/j.1365-2265.2010.03913.x | 21044119 | UNKNOWN | UNKNOWN | 既存出典（第20回で登録済み。本回では新しい番号を付けず既存番号を使用） |
| SRC-1561 | 日本脳卒中学会 脳卒中治療ガイドライン委員会 編『脳卒中治療ガイドライン2021〔改訂2023〕』協和企画 | なし | なし | 日本脳卒中学会の著作物（CC表示なし） | RESTRICTED | 書籍。改訂2025の公開テキストで関連推奨の存続を確認 |
| SRC-1562 | Greenberg SM, et al. 2022 Guideline for the Management of Patients With Spontaneous Intracerebral Hemorrhage: A Guideline From the AHA/ASA. Stroke. 2022;53(7):e282-e361 | 10.1161/STR.0000000000000407 | 35579034 | AHA/ASAガイドライン（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合 |
| SRC-1563 | Anderson CS, et al.; INTERACT2 Investigators. Rapid blood-pressure lowering in patients with acute intracerebral hemorrhage. N Engl J Med. 2013;368(25):2355-2365 | 10.1056/NEJMoa1214609 | 23713578 | NEJM（CC表示なし） | RESTRICTED | PubMed・抄録で照合 |
| SRC-1564 | Qureshi AI, et al.; ATACH-2 Trial Investigators. Intensive Blood-Pressure Lowering in Patients with Acute Cerebral Hemorrhage. N Engl J Med. 2016;375(11):1033-1043 | 10.1056/NEJMoa1603460 | 27276234 | NEJM（CC表示なし） | RESTRICTED | PubMed・抄録で照合 |
| SRC-1565 | Mendelow AD, et al.; STICH II Investigators. Early surgery versus initial conservative treatment in patients with spontaneous supratentorial lobar intracerebral haematomas (STICH II): a randomised trial. Lancet. 2013;382(9890):397-408 | 10.1016/S0140-6736(13)60986-1 | 23726393 | CC BY-NC-ND 3.0 | RESTRICTED | PubMedで照合、Crossrefのlicense欄でCC BY-NC-NDを確認 |
| SRC-1566 | Charidimou A, et al. The Boston criteria version 2.0 for cerebral amyloid angiopathy: a multicentre, retrospective, MRI-neuropathology diagnostic accuracy study. Lancet Neurol. 2022;21(8):714-725 | 10.1016/S1474-4422(22)00208-3 | 35841910 | The Lancet Neurology（CC表示なし） | RESTRICTED | PubMed・抄録で照合 |
| SRC-1567 | Hoh BL, et al. 2023 Guideline for the Management of Patients With Aneurysmal Subarachnoid Hemorrhage: A Guideline From the AHA/ASA. Stroke. 2023;54(7):e314-e370 | 10.1161/STR.0000000000000436 | 37212182 | AHA/ASAガイドライン（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合 |
| SRC-1568 | Molyneux AJ, et al.; ISAT Collaborative Group. International Subarachnoid Aneurysm Trial (ISAT) of neurosurgical clipping versus endovascular coiling in 2143 patients with ruptured intracranial aneurysms: a randomised comparison. Lancet. 2005;366(9488):809-817 | 10.1016/S0140-6736(05)67214-5 | 16139655 | The Lancet（CC表示なし） | RESTRICTED | PubMed・抄録で照合 |
| SRC-1569 | The UCAS Japan Investigators (Morita A, et al.). The natural course of unruptured cerebral aneurysms in a Japanese cohort. N Engl J Med. 2012;366(26):2474-2482 | 10.1056/NEJMoa1113260 | 22738097 | NEJM（CC表示なし） | RESTRICTED | Crossrefでタイトル・DOIを照合、PMIDはPubMed収載誌の文献情報で照合 |
| SRC-1570 | Endo H, et al. Effects of clazosentan on cerebral vasospasm-related morbidity and all-cause mortality after aneurysmal subarachnoid hemorrhage: two randomized phase 3 trials in Japanese patients. J Neurosurg. 2022 | 10.3171/2022.2.JNS212914 | 35364589 | CC BY-NC-ND 4.0 | RESTRICTED | PubMed情報でDOI・PMIDを照合、Crossrefのlicense欄でCC BY-NC-NDを確認 |
| SRC-1571 | Takagi T, Takayasu M, Suzuki Y, Yoshida J. Prediction of rebleeding from angiographic features in vertebral artery dissecting aneurysms. Neurosurg Rev. 2007;30(1):32-38 | 10.1007/s10143-006-0049-1 | 17061136 | Springer（テキストマイニング用ライセンスのみ） | RESTRICTED | PubMed・抄録で照合、Crossrefでlicense欄を確認 |
| SRC-1572 | Pickard JD, et al. Effect of oral nimodipine on cerebral infarction and outcome after subarachnoid haemorrhage: British aneurysm nimodipine trial. BMJ. 1989;298(6674):636-642 | 10.1136/bmj.298.6674.636 | 2496789 | BMJ（CC表示なし） | RESTRICTED | PubMed・抄録（PMC）で照合 |
| SRC-1581 | 日本脳卒中学会 脳卒中治療ガイドライン2021［改訂2023］（書籍） | なし | なし | RESTRICTED | RESTRICTED | ガイドライン書籍・資料のため DOI・PMID なし（部分ファイルの出典表に理由を記載） |
| SRC-1582 | Powers WJ et al. Guidelines for the Early Management of Patients With Acute Ischemic Stroke: 2019 Update. Stroke 2019 | 10.1161/STR.0000000000000211 | 31662037 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1583 | Yamaguchi T et al. Alteplase at 0.6 mg/kg for acute ischemic stroke within 3 hours of onset: Japan Alteplase Clinical Trial (J-ACT). Stroke 2006 | 10.1161/01.STR.0000227191.01792.e3 | 16763187 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1584 | Fischer U et al. Early versus Later Anticoagulation for Stroke with Atrial Fibrillation (ELAN). N Engl J Med 2023 | 10.1056/NEJMoa2303048 | 37222476 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1585 | Kleindorfer DO et al. 2021 Guideline for the Prevention of Stroke in Patients With Stroke and Transient Ischemic Attack. Stroke 2021 | 10.1161/STR.0000000000000375 | 34024117 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1586 | Wang Y et al. Clopidogrel with aspirin in acute minor stroke or transient ischemic attack (CHANCE). N Engl J Med 2013 | 10.1056/NEJMoa1215340 | 23803136 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1587 | Johnston SC et al. Clopidogrel and Aspirin in Acute Ischemic Stroke and High-Risk TIA (POINT). N Engl J Med 2018 | 10.1056/NEJMoa1800410 | 29766750 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1588 | Toyoda K et al. Dual antiplatelet therapy using cilostazol for secondary prevention in patients with high-risk ischaemic stroke in Japan (CSPS.com). Lancet Neurol 2019 | 10.1016/S1474-4422(19)30148-6 | 31122494 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1589 | SPS3 Investigators. Effects of clopidogrel added to aspirin in patients with recent lacunar stroke. N Engl J Med 2012 | 10.1056/NEJMoa1204133 | 22931315 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1590 | Wardlaw JM et al. Neuroimaging standards for research into small vessel disease (STRIVE). Lancet Neurol 2013 | 10.1016/S1474-4422(13)70124-8 | 23867200 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1591 | Easton JD et al. Definition and evaluation of transient ischemic attack: AHA/ASA scientific statement. Stroke 2009 | 10.1161/STROKEAHA.108.192218 | 19423857 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1592 | Johnston SC et al. Validation and refinement of scores to predict very early stroke risk after transient ischaemic attack (ABCD2). Lancet 2007 | 10.1016/S0140-6736(07)60150-0 | 17258668 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1593 | Brott TG et al. Stenting versus endarterectomy for treatment of carotid-artery stenosis (CREST). N Engl J Med 2010 | 10.1056/NEJMoa0912321 | 20505173 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1594 | Chimowitz MI et al. Stenting versus aggressive medical therapy for intracranial arterial stenosis (SAMMPRIS). N Engl J Med 2011 | 10.1056/NEJMoa1105335 | 21899409 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1595 | Nogueira RG et al. Thrombectomy 6 to 24 Hours after Stroke with a Mismatch between Deficit and Infarct (DAWN). N Engl J Med 2018 | 10.1056/NEJMoa1706442 | 29129157 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1596 | Albers GW et al. Thrombectomy for Stroke at 6 to 16 Hours with Selection by Perfusion Imaging (DEFUSE 3). N Engl J Med 2018 | 10.1056/NEJMoa1713973 | 29364767 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1597 | Markus HS et al. Antiplatelet treatment compared with anticoagulation treatment for cervical artery dissection (CADISS). Lancet Neurol 2015 | 10.1016/S1474-4422(15)70018-9 | 25684164 | CC BY | OPEN | PubMed／Crossref で照合 |
| SRC-1598 | Debette S, Leys D. Cervical-artery dissections: predisposing factors, diagnosis, and outcome. Lancet Neurol 2009 | 10.1016/S1474-4422(09)70084-5 | 19539238 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1599 | Spetzler RF, Martin NA. A proposed grading system for arteriovenous malformations. J Neurosurg 1986 | 10.3171/jns.1986.65.4.0476 | 3760956 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1600 | Mohr JP et al. Medical management with or without interventional therapy for unruptured brain arteriovenous malformations (ARUBA). Lancet 2014 | 10.1016/S0140-6736(13)62302-8 | 24268105 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1601 | Saposnik G et al. Diagnosis and Management of Cerebral Venous Thrombosis: A Scientific Statement From the AHA. Stroke 2024 | 10.1161/STR.0000000000000456 | 38284265 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1602 | Ferro JM et al. Safety and Efficacy of Dabigatran Etexilate vs Dose-Adjusted Warfarin in Patients With Cerebral Venous Thrombosis (RESPECT-CVT). JAMA Neurol 2019 | 10.1001/jamaneurol.2019.2764 | 31479105 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1603 | Kuroda S et al. Diagnostic Criteria for Moyamoya Disease - 2021 Revised Version. Neurol Med Chir (Tokyo) 2022 | 10.2176/jns-nmc.2022-0072 | 35613882 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1604 | Miyamoto S et al. Effects of extracranial-intracranial bypass for patients with hemorrhagic moyamoya disease: Japan Adult Moyamoya Trial (JAM). Stroke 2014 | 10.1161/STROKEAHA.113.004386 | 24668203 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1605 | Cognard C et al. Cerebral dural arteriovenous fistulas: clinical and angiographic correlation with a revised classification of venous drainage. Radiology 1995 | 10.1148/radiology.194.3.7862961 | 7862961 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1606 | Borden JA et al. A proposed classification for spinal and cranial dural arteriovenous fistulous malformations and implications for treatment. J Neurosurg 1995 | 10.3171/jns.1995.82.2.0166 | 7815143 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1607 | AVERT Trial Collaboration. Efficacy and safety of very early mobilisation within 24 h of stroke onset (AVERT). Lancet 2015 | 10.1016/S0140-6736(15)60690-0 | 25892679 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1611 | Louis DN, et al. The 2021 WHO Classification of Tumours of the Central Nervous System: a summary. Neuro Oncol. 2021;23(8):1231-1251 | 10.1093/neuonc/noab106 | 34185076 | Oxford University Press 標準出版モデル（CC表示なし） | RESTRICTED | PubMed・Crossrefで書誌・DOI・PMID・license欄を照合 |
| SRC-1612 | Stupp R, et al. Radiotherapy plus concomitant and adjuvant temozolomide for glioblastoma. N Engl J Med. 2005;352(10):987-996 | 10.1056/NEJMoa043330 | 15758009 | NEJM（CC表示なし） | RESTRICTED | PubMed・抄録で照合 |
| SRC-1613 | Stupp R, et al. Effect of Tumor Treating Fields Plus Maintenance Temozolomide vs Maintenance Temozolomide Alone on Survival in Patients With Glioblastoma: A Randomized Clinical Trial. JAMA. 2017;318(23):2306-2316 | 10.1001/jama.2017.18718 | 29260225 | JAMA（CC表示なし） | RESTRICTED | PubMed・抄録で照合 |
| SRC-1614 | Buckner JC, et al. Radiation plus Procarbazine, CCNU, and Vincristine in Low-Grade Glioma. N Engl J Med. 2016;374(14):1344-1355 | 10.1056/NEJMoa1500925 | 27050206 | NEJM（CC表示なし） | RESTRICTED | PubMed・抄録で照合 |
| SRC-1615 | Ferreri AJM, et al. Primary central nervous system lymphomas: EHA-ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up. HemaSphere. 2024;8(6):e89 | 10.1002/hem3.89 | 38836097 | CC BY 4.0 | OPEN | PMC掲載ページで CC BY 4.0 の表示を確認、PubMed・Crossrefで書誌を照合 |
| SRC-1616 | Ferreri AJM, et al. Chemoimmunotherapy with methotrexate, cytarabine, thiotepa, and rituximab (MATRix regimen) in patients with primary CNS lymphoma: results of the first randomisation of the International Extranodal Lymphoma Study Group-32 (IELSG32) phase 2 trial. Lancet Haematol. 2016;3(5):e217-e227 | 10.1016/S2352-3026(16)00036-3 | 27132696 | Elsevier（テキストマイニング用ライセンスのみ） | RESTRICTED | PubMed・Crossrefで書誌・DOI・PMID・license欄を照合 |
| SRC-1617 | Frappaz D, et al. EANO, SNO and Euracan consensus review on the current management and future development of intracranial germ cell tumors in adolescents and young adults. Neuro Oncol. 2022;24(4):516-527 | 10.1093/neuonc/noab252 | 34724065 | CC BY-NC 4.0 | RESTRICTED | PubMed・抄録で照合、Crossrefのlicense欄で CC BY-NC 4.0 を確認 |
| SRC-1618 | Takami H, et al. Impact of tumor markers on diagnosis, treatment and prognosis in CNS germ cell tumors: correlations with clinical practice and histopathology. Brain Tumor Pathol. 2023;40(2):124-132 | 10.1007/s10014-023-00460-x | 36995447 | Springer（CC表示なし） | RESTRICTED | PubMed・抄録で照合、CrossrefでDOIを照合 |
| SRC-1619 | Wanebo JE, et al. The natural history of hemangioblastomas of the central nervous system in patients with von Hippel-Lindau disease. J Neurosurg. 2003;98(1):82-94 | 10.3171/jns.2003.98.1.0082 | 12546356 | Journal of Neurosurgery（CC表示なし） | RESTRICTED | PubMed・抄録で照合 |
| SRC-1620 | Goldbrunner R, et al. EANO guideline on the diagnosis and management of meningiomas. Neuro Oncol. 2021;23(11):1821-1834 | 10.1093/neuonc/noab150 | 34181733 | Oxford University Press 標準出版モデル（CC表示なし） | RESTRICTED | PubMed・抄録で照合、Crossrefでlicense欄を確認 |
| SRC-1621 | Goldbrunner R, et al. EANO guideline on the diagnosis and treatment of vestibular schwannoma. Neuro Oncol. 2020;22(1):31-45 | 10.1093/neuonc/noz153 | 31504802 | Oxford University Press 標準出版モデル（CC表示なし） | RESTRICTED | PubMed・抄録で照合、Crossrefでlicense欄を確認 |
| SRC-1622 | Vogelbaum MA, et al. (Schiff D, et al.) Treatment for Brain Metastases: ASCO-SNO-ASTRO Guideline. J Clin Oncol. 2022;40(3):242-264 | 10.1200/JCO.21.02314 | 34932393 | ASCO（CC表示なし） | RESTRICTED | PubMed・抄録で照合 |
| SRC-1623 | Le Rhun E, et al. Leptomeningeal metastasis from solid tumours: EANO-ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up. ESMO Open. 2023;8(5):101624 | 10.1016/j.esmoop.2023.101624 | 37863528 | CC BY-NC-ND 4.0 | RESTRICTED | PMC掲載ページで CC BY-NC-ND 4.0 の表示と本文を確認、PubMed・Crossrefで書誌を照合 |
| SRC-1624 | Mitsuya K, et al. Metastatic skull tumors: MRI features and a new conventional classification. J Neurooncol. 2011;104(1):239-245 | 10.1007/s11060-010-0465-5 | 21110218 | CC BY-NC（PMC掲載ページの表示） | RESTRICTED | PMC掲載ページで本文とライセンス表示を確認、PubMedで書誌を照合 |
| SRC-1625 | Graus F, Titulaer MJ, Balu R, et al. A clinical approach to diagnosis of autoimmune encephalitis. Lancet Neurol. 2016;15(4):391-404 | 10.1016/S1474-4422(15)00401-9 | 26906964 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1626 | Titulaer MJ, McCracken L, Gabilondo I, et al. Treatment and prognostic factors for long-term outcome in patients with anti-NMDA receptor encephalitis: an observational cohort study. Lancet Neurol. 2013;12(2):157-165 | 10.1016/S1474-4422(12)70310-1 | 23290630 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1631 | Tunkel AR, Glaser CA, Bloch KC, et al. The management of encephalitis: clinical practice guidelines by the Infectious Diseases Society of America. Clin Infect Dis. 2008;47(3):303-327 | 10.1086/589747 | 18582201 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1632 | Berger JR, Aksamit AJ, Clifford DB, et al. PML diagnostic criteria: consensus statement from the AAN Neuroinfectious Disease Section. Neurology. 2013;80(15):1430-1438 | 10.1212/WNL.0b013e31828c2fa1 | 23568998 | UNKNOWN | UNKNOWN | PubMed／Crossref で照合 |
| SRC-1633 | Antinori A, Arendt G, Becker JT, et al. Updated research nosology for HIV-associated neurocognitive disorders. Neurology. 2007;69(18):1789-1799 | 10.1212/01.WNL.0000287431.88658.8b | 17914061 | UNKNOWN | UNKNOWN | PubMed／Crossref で照合 |
| SRC-1634 | Puccioni-Sohler M, Poton AR, Cabral-Castro MJ, et al. Human T Lymphotropic Virus 1-Associated Myelopathy: Overview of Human T Cell Lymphotropic Virus-1/2 Tests and Potential Biomarkers. AIDS Res Hum Retroviruses. 2022;38(12):924-932 | 10.1089/AID.2022.0028 | 35819286 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1635 | Zerr I, Kallenberg K, Summers DM, et al. Updated clinical diagnostic criteria for sporadic Creutzfeldt-Jakob disease. Brain. 2009;132(Pt 10):2659-2668 | 10.1093/brain/awp191 | 19773352 | UNKNOWN | UNKNOWN | PubMed／Crossref で照合 |
| SRC-1636 | 厚生労働科学研究費補助金難治性疾患政策研究事業「プリオン病及び遅発性ウイルス感染症に関する調査研究班」、厚生労働行政推進調査事業費補助金「プリオン病のサーベイランスと感染予防に関する調査研究班」. プリオン病診療ガイドライン2026. 2026 | なし | なし | GOV_JP | GOV_JP | PubMed／Crossref で照合 |
| SRC-1637 | 厚生労働科学研究費補助金「プリオン病及び遅発性ウイルス感染症に関する調査研究班」ほか. プリオン病感染予防ガイドライン2020. 2020 | なし | なし | GOV_JP | GOV_JP | PubMed／Crossref で照合 |
| SRC-1638 | 日本神経学会・日本神経治療学会・日本神経感染症学会 監修、「細菌性髄膜炎診療ガイドライン」作成委員会 編. 細菌性髄膜炎診療ガイドライン2014. 南江堂. 2014 | なし | なし | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1639 | de Gans J, van de Beek D; European Dexamethasone in Adulthood Bacterial Meningitis Study Investigators. Dexamethasone in adults with bacterial meningitis. N Engl J Med. 2002;347(20):1549-1556 | 10.1056/NEJMoa021334 | 12432041 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1640 | Bodilsen J, D'Alessandris QG, Humphreys H, et al. European Society of Clinical Microbiology and Infectious Diseases guidelines on diagnosis and treatment of brain abscess in children and adults. Clin Microbiol Infect. 2024;30(1):66-89 | 10.1016/j.cmi.2023.08.016 | 37648062 | OPEN | OPEN | PubMed／Crossref で照合 |
| SRC-1641 | Chang CC, Harrison TS, Bicanic TA, et al. Global guideline for the diagnosis and management of cryptococcosis: an initiative of the ECMM and ISHAM in cooperation with the ASM. Lancet Infect Dis. 2024;24(8):e495-e512 | 10.1016/S1473-3099(23)00731-4 | 38346436 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1642 | Marais S, Thwaites G, Schoeman JF, et al. Tuberculous meningitis: a uniform case definition for use in clinical research. Lancet Infect Dis. 2010;10(11):803-812 | 10.1016/S1473-3099(10)70138-9 | 20822958 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1643 | Thwaites GE, Nguyen DB, Nguyen HD, et al. Dexamethasone for the treatment of tuberculous meningitis in adolescents and adults. N Engl J Med. 2004;351(17):1741-1751 | 10.1056/NEJMoa040573 | 15496623 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1644 | Krupp LB, Tardieu M, Amato MP, et al. International Pediatric Multiple Sclerosis Study Group criteria for pediatric multiple sclerosis and immune-mediated central nervous system demyelinating disorders: revisions to the 2007 definitions. Mult Scler. 2013;19(10):1261-1267 | 10.1177/1352458513484547 | 23572237 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1645 | Gunaratna GPS, Mohammad SS, Blyth CC, et al. Postinfectious Acute Cerebellar Syndromes in Children: A Nationally Ascertained Case Series From Australia 2013-2018. J Child Neurol. 2022 (online ahead of print) | 10.1177/08830738221093209 | 35546546 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1646 | Berbari EF, Kanj SS, Kowalski TJ, et al. 2015 Infectious Diseases Society of America (IDSA) Clinical Practice Guidelines for the Diagnosis and Treatment of Native Vertebral Osteomyelitis in Adults. Clin Infect Dis. 2015;61(6):e26-e46 | 10.1093/cid/civ482 | 26229122 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1647 | Leowattana W, Leowattana P, Leowattana T. Tuberculosis of the spine. World J Orthop. 2023;14(5):275-293 | 10.5312/wjo.v14.i5.275 | 37304201 | UNKNOWN | UNKNOWN | PubMed／Crossref で照合 |
| SRC-1648 | Hatzenbuehler J, Pulling TJ. Diagnosis and management of osteomyelitis. Am Fam Physician. 2011;84(9):1027-1033 | なし | 22046943 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1649 | Earwood JS, Walker TR, Sue GJC. Septic Arthritis: Diagnosis and Treatment. Am Fam Physician. 2021;104(6):589-597 | なし | 34913662 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |
| SRC-1650 | Gutierrez J, Issacson RS, Koppel BS. Subacute sclerosing panencephalitis: an update. Dev Med Child Neurol. 2010;52(10):901-907 | 10.1111/j.1469-8749.2010.03717.x | 20561004 | RESTRICTED | RESTRICTED | PubMed／Crossref で照合 |

## 2. 事実票 YAML

```yaml
- id: ST-001
  domain: ST
  subdomain: 脳内出血
  assertion:
    plain_statement_ja: 高血圧性脳出血は、穿通枝の支配領域である大脳基底核（被殻・尾状核）、視床、脳幹（橋）、小脳などの深部構造に好発する。
    condition:
      population: 高血圧を有する成人の脳内出血患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1562
    source: 'Greenberg SM, et al. 2022 Guideline for the Management of Patients With Spontaneous Intracerebral Hemorrhage: A Guideline From the AHA/ASA. Stroke. 2022;53(7):e282-e361'
    doi: 10.1161/STR.0000000000000407
    pmid: '35579034'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000407
    source_license: AHA/ASAガイドライン（Stroke誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 部位の列挙はガイドライン本文の記載に基づく。各部位の頻度の数値は本カードでは扱わない。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-002
  domain: ST
  subdomain: 脳内出血
  assertion:
    plain_statement_ja: 脳出血では出血部位により症状が異なり、被殻出血では対側の片麻痺と感覚障害、視床出血では感覚障害、小脳出血では運動失調と嘔吐、橋出血では意識障害と四肢麻痺がみられる。
    condition:
      population: 脳内出血患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1561
    source: 日本脳卒中学会 脳卒中治療ガイドライン委員会 編『脳卒中治療ガイドライン2021〔改訂2023〕』協和企画
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 日本脳卒中学会の著作物（書籍、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインの症候の記載に基づく。個別の頻度は示していない。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-003
  domain: ST
  subdomain: 脳内出血
  assertion:
    plain_statement_ja: 発症6時間以内で収縮期血圧150〜220 mmHgの脳内出血患者に対する、1時間以内に収縮期血圧140 mmHg未満を目指す積極的降圧は、通常治療（180 mmHg未満）と比べて90日後の死亡または重度障害（modified Rankin Scale 3〜6）を有意には減らさなかったが（52.0%対55.6%、オッズ比0.87）、順序解析では機能転帰の改善が示された（INTERACT2、2839例）。
    condition:
      population: 発症6時間以内の自発性脳内出血で収縮期血圧が上昇した患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1563
    source: Anderson CS, et al.; INTERACT2 Investigators. Rapid blood-pressure lowering in patients with acute intracerebral hemorrhage. N Engl J Med. 2013;368(25):2355-2365
    doi: 10.1056/NEJMoa1214609
    pmid: '23713578'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1214609
    source_license: NEJM（Massachusetts Medical Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。主要評価項目の群間差は有意水準に達しなかった（p=0.06）。降圧薬の種類は担当医の選択であり、特定の薬剤の効果を示す結果ではない。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-004
  domain: ST
  subdomain: 脳内出血
  assertion:
    plain_statement_ja: 脳内出血患者に対するニカルジピン持続静注による収縮期血圧110〜139 mmHgへの強化降圧は、標準治療（140〜179 mmHg）と比べて3か月後の死亡または障害（modified Rankin Scale 4〜6）を減らさず（38.7%対37.7%、相対リスク1.04）、7日以内の腎有害事象が多かった（9.0%対4.0%）（ATACH-2、1000例）。
    condition:
      population: 発症4.5時間以内に治療を開始した脳内出血患者（血腫量60 mL未満、GCS 5点以上）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1564
    source: Qureshi AI, et al.; ATACH-2 Trial Investigators. Intensive Blood-Pressure Lowering in Patients with Acute Cerebral Hemorrhage. N Engl J Med. 2016;375(11):1033-1043
    doi: 10.1056/NEJMoa1603460
    pmid: '27276234'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1603460
    source_license: NEJM（Massachusetts Medical Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。ニカルジピンは国内で承認された降圧薬である（適応の詳細は添付文書による）。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-005
  domain: ST
  subdomain: 脳内出血
  assertion:
    plain_statement_ja: 日本の脳卒中治療ガイドライン2021（改訂2023）は、脳出血急性期の血圧高値に対して、ニカルジピンの持続静注により収縮期血圧を140 mmHg未満に安定して保つことを妥当としている。
    condition:
      population: 脳出血急性期の患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1561
    source: 日本脳卒中学会 脳卒中治療ガイドライン委員会 編『脳卒中治療ガイドライン2021〔改訂2023〕』協和企画
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 日本脳卒中学会の著作物（書籍、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインの推奨文に基づく。ニカルジピンは国内承認薬である。なお2025年に改訂2025が公開されており、同じ趣旨の推奨が維持されていることを公開テキストで確認した。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-006
  domain: ST
  subdomain: 脳内出血
  assertion:
    plain_statement_ja: 脳表に近い脳葉出血（10〜100 mL、脳室内出血なし）に対する早期手術は、初期保存的治療と比べて6か月後の転帰を有意に改善しなかった（転帰不良59%対62%、オッズ比0.86）（STICH II、601例）。
    condition:
      population: 発症48時間以内に受診した表在性脳葉出血の患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1565
    source: 'Mendelow AD, et al.; STICH II Investigators. Early surgery versus initial conservative treatment in patients with spontaneous supratentorial lobar intracerebral haematomas (STICH II): a randomised trial. Lancet. 2013;382(9890):397-408'
    doi: 10.1016/S0140-6736(13)60986-1
    pmid: '23726393'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(13)60986-1
    source_license: CC BY-NC-ND 3.0（Crossrefのlicense欄で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。予後予測スコアが不良な群では生存の利益の可能性が示唆されたが、全体では有意差はなかった。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-007
  domain: ST
  subdomain: 脳内出血
  assertion:
    plain_statement_ja: 神経学的に悪化している場合、脳幹が圧迫されている場合、または脳室閉塞による水頭症を伴う小脳出血では、血腫除去術を行うことが推奨される。
    condition:
      population: 小脳出血患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1562
    source: 'Greenberg SM, et al. 2022 Guideline for the Management of Patients With Spontaneous Intracerebral Hemorrhage: A Guideline From the AHA/ASA. Stroke. 2022;53(7):e282-e361'
    doi: 10.1161/STR.0000000000000407
    pmid: '35579034'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000407
    source_license: AHA/ASAガイドライン（Stroke誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインの推奨文に基づく。血腫量の閾値を含む推奨の全文はガイドライン本文による。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-008
  domain: ST
  subdomain: アミロイドアンギオパチー
  assertion:
    plain_statement_ja: Boston criteria version 2.0では、50歳以上で、脳葉に限局した出血性病変（脳内出血、微小出血、皮質表層鉄沈着症・円蓋部くも膜下出血）が2つ以上ある場合、または脳葉の出血性病変1つと白質病変（半卵円中心の重度血管周囲腔拡大、または多発斑状の白質高信号）のいずれか1つがある場合に、深部の出血性病変がなければprobable CAA（ほぼ確実な脳アミロイドアンギオパチー）と診断する。
    condition:
      population: 50歳以上で脳内出血、認知機能障害または一過性局所神経症状を呈した患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1566
    source: 'Charidimou A, et al. The Boston criteria version 2.0 for cerebral amyloid angiopathy: a multicentre, retrospective, MRI-neuropathology diagnostic accuracy study. Lancet Neurol. 2022;21(8):714-725'
    doi: 10.1016/S1474-4422(22)00208-3
    pmid: '35841910'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(22)00208-3
    source_license: The Lancet Neurology（Elsevier、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 基準の定義は論文のPanel（表）から読み取り。小脳の出血性病変は脳葉・深部のいずれにも数えない。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-A-②（アミロイドアンギオパチー、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-009
  domain: ST
  subdomain: アミロイドアンギオパチー
  assertion:
    plain_statement_ja: Boston criteria version 2.0のprobable CAAの診断精度は、剖検を診断標準とした解析で感度74.5%、特異度95.0%であり、旧基準（感度64.5%、特異度95.0%）と比べて特異度を保ったまま感度が向上した。
    condition:
      population: 病理学的に脳アミロイドアンギオパチーの評価が行われた患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1566
    source: 'Charidimou A, et al. The Boston criteria version 2.0 for cerebral amyloid angiopathy: a multicentre, retrospective, MRI-neuropathology diagnostic accuracy study. Lancet Neurol. 2022;21(8):714-725'
    doi: 10.1016/S1474-4422(22)00208-3
    pmid: '35841910'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(22)00208-3
    source_license: The Lancet Neurology（Elsevier、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。コホートにより感度・特異度は異なり、脳内出血で発症した患者以外では感度が下がる。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-A-②（アミロイドアンギオパチー、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-010
  domain: ST
  subdomain: アミロイドアンギオパチー
  assertion:
    plain_statement_ja: 脳アミロイドアンギオパチーに関連する脳葉出血の既往がある患者では、抗血栓療法により脳出血再発のリスクが高まるため、抗凝固療法・抗血小板療法の適応は有益性と再発リスクを衡量して慎重に判断する必要がある。
    condition:
      population: 脳アミロイドアンギオパチーによる脳葉出血の既往がある患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1562
    source: 'Greenberg SM, et al. 2022 Guideline for the Management of Patients With Spontaneous Intracerebral Hemorrhage: A Guideline From the AHA/ASA. Stroke. 2022;53(7):e282-e361'
    doi: 10.1161/STR.0000000000000407
    pmid: '35579034'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000407
    source_license: AHA/ASAガイドライン（Stroke誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインの記載に基づく一般論であり、個別の再発率の数値は本カードでは扱わない。抗血栓薬の国内承認・保険適用は薬剤ごとに添付文書での確認が必要である。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-A-②（アミロイドアンギオパチー、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-011
  domain: ST
  subdomain: くも膜下出血
  assertion:
    plain_statement_ja: 動脈瘤性くも膜下出血は、突然発症し瞬時に最強となる激しい頭痛（雷鳴頭痛）を特徴とし、嘔吐、意識障害、痙攣発作を伴うことがある。
    condition:
      population: 動脈瘤性くも膜下出血患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1567
    source: 'Hoh BL, et al. 2023 Guideline for the Management of Patients With Aneurysmal Subarachnoid Hemorrhage: A Guideline From the AHA/ASA. Stroke. 2023;54(7):e314-e370'
    doi: 10.1161/STR.0000000000000436
    pmid: '37212182'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000436
    source_license: AHA/ASAガイドライン（Stroke誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインの臨床像の記載に基づく。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-012
  domain: ST
  subdomain: くも膜下出血
  assertion:
    plain_statement_ja: WFNS分類はGlasgow Coma Scaleに基づくくも膜下出血の重症度分類で、グレードIはGCS 15点、グレードIIはGCS 13〜14点で運動障害なし、グレードIIIはGCS 13〜14点で運動障害あり、グレードIVはGCS 7〜12点、グレードVはGCS 3〜6点と定義され、グレードが高いほど予後が不良である。
    condition:
      population: くも膜下出血患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1567
    source: 'Hoh BL, et al. 2023 Guideline for the Management of Patients With Aneurysmal Subarachnoid Hemorrhage: A Guideline From the AHA/ASA. Stroke. 2023;54(7):e314-e370'
    doi: 10.1161/STR.0000000000000436
    pmid: '37212182'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000436
    source_license: AHA/ASAガイドライン（Stroke誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 分類の定義はガイドラインの表から読み取り。Hunt & Kosnik分類も併用されるが、本カードではWFNS分類のみを扱う。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-013
  domain: ST
  subdomain: くも膜下出血
  assertion:
    plain_statement_ja: Fisher分類およびmodified Fisher分類は、発症時の頭部CTにおけるくも膜下血液の量と分布（脳室内出血の有無を含む）に基づき、脳血管攣縮と遅発性脳虚血のリスクを層別化する分類である。
    condition:
      population: 動脈瘤性くも膜下出血患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1567
    source: 'Hoh BL, et al. 2023 Guideline for the Management of Patients With Aneurysmal Subarachnoid Hemorrhage: A Guideline From the AHA/ASA. Stroke. 2023;54(7):e314-e370'
    doi: 10.1161/STR.0000000000000436
    pmid: '37212182'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000436
    source_license: AHA/ASAガイドライン（Stroke誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 分類の構成はガイドラインの表から読み取り。各グレードの定義の詳細は表による。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-014
  domain: ST
  subdomain: くも膜下出血
  assertion:
    plain_statement_ja: 破裂脳動脈瘤の再出血は発症後早期に多く、転帰を著しく悪化させるため、再出血を防ぐための動脈瘤治療（クリッピングまたはコイリング）は可能な限り早期に行うことが推奨される。
    condition:
      population: 破裂脳動脈瘤によるくも膜下出血患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1567
    source: 'Hoh BL, et al. 2023 Guideline for the Management of Patients With Aneurysmal Subarachnoid Hemorrhage: A Guideline From the AHA/ASA. Stroke. 2023;54(7):e314-e370'
    doi: 10.1161/STR.0000000000000436
    pmid: '37212182'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000436
    source_license: AHA/ASAガイドライン（Stroke誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインの推奨に基づく。再出血率の具体的な数値は本カードでは扱わない。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-015
  domain: ST
  subdomain: 脳動脈瘤
  assertion:
    plain_statement_ja: クリッピングとコイリングの両方が可能と判断された破裂脳動脈瘤では、コイリング群の1年後の死亡または依存（modified Rankin Scale 3〜6）の割合がクリッピング群より低かった（23.5%対30.9%）（ISAT、2143例）。
    condition:
      population: 両治療法のいずれも可能と判断された破裂脳動脈瘤患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1568
    source: 'Molyneux AJ, et al.; ISAT Collaborative Group. International Subarachnoid Aneurysm Trial (ISAT) of neurosurgical clipping versus endovascular coiling in 2143 patients with ruptured intracranial aneurysms: a randomised comparison. Lancet. 2005;366(9488):809-817'
    doi: 10.1016/S0140-6736(05)67214-5
    pmid: '16139655'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(05)67214-5
    source_license: The Lancet（Elsevier、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。対象は両治療が可能と判断された症例に限られ、後方循環や中大脳動脈の動脈瘤は少数であった。治療後の再出血はコイリング群でやや多かった。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)；TBL-01-00-030 (id: Jlvnlcg)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-016
  domain: ST
  subdomain: くも膜下出血
  assertion:
    plain_statement_ja: 日本で実施された第3相試験2件では、クラゾセンタン10 mg/時の持続静注（発症48時間以内に開始し、最長15日間）により、脳血管攣縮に関連する罹患率と全死亡の複合イベントが、コイリング後では28.8%から13.6%に（相対リスク減少53%）、クリッピング後では39.6%から16.2%に（同59%）有意に減少した（各試験221例）。
    condition:
      population: 動脈瘤性くも膜下出血後の日本人患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1570
    source: 'Endo H, et al. Effects of clazosentan on cerebral vasospasm-related morbidity and all-cause mortality after aneurysmal subarachnoid hemorrhage: two randomized phase 3 trials in Japanese patients. J Neurosurg. 2022'
    doi: 10.3171/2022.2.JNS212914
    pmid: '35364589'
    pmcid: null
    url: https://doi.org/10.3171/2022.2.JNS212914
    source_license: CC BY-NC-ND 4.0（Crossrefのlicense欄で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。クラゾセンタンは国内で承認されている（2022年に承認、商品名ピヴラッツ）。欧米では承認されておらず、地域差がある。有害事象として体液貯留に関連する事象（肺水腫、胸水、低ナトリウム血症など）に注意が必要である。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-017
  domain: ST
  subdomain: くも膜下出血
  assertion:
    plain_statement_ja: 経口ニモジピン60 mgを4時間ごとに21日間投与する治療（発症96時間以内に開始）は、くも膜下出血後の脳梗塞の発生を33%から22%へ（相対減少34%）、転帰不良（死亡・植物状態・重度障害）を33%から20%へ（同40%）減らした（British aneurysm nimodipine trial、554例）。
    condition:
      population: くも膜下出血患者（英国の多施設試験）
      region: 欧州
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1572
    source: 'Pickard JD, et al. Effect of oral nimodipine on cerebral infarction and outcome after subarachnoid haemorrhage: British aneurysm nimodipine trial. BMJ. 1989;298(6674):636-642'
    doi: 10.1136/bmj.298.6674.636
    pmid: '2496789'
    pmcid: null
    url: https://doi.org/10.1136/bmj.298.6674.636
    source_license: BMJ（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。ニモジピンは国内未承認薬であり、日本ではこの治療は行えない。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-018
  domain: ST
  subdomain: くも膜下出血
  assertion:
    plain_statement_ja: AHA/ASAガイドライン2023は、動脈瘤性くも膜下出血の患者に対し、遅発性脳虚血の予防と転帰改善のために経口ニモジピンを投与することを推奨している（Class 1）。
    condition:
      population: 動脈瘤性くも膜下出血患者
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1567
    source: 'Hoh BL, et al. 2023 Guideline for the Management of Patients With Aneurysmal Subarachnoid Hemorrhage: A Guideline From the AHA/ASA. Stroke. 2023;54(7):e314-e370'
    doi: 10.1161/STR.0000000000000436
    pmid: '37212182'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000436
    source_license: AHA/ASAガイドライン（Stroke誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 推奨文はガイドライン本文に基づく。用量は60 mgを4時間ごと、21日間が標準とされる。ニモジピンは国内未承認薬であり、日本では使用できない。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-019
  domain: ST
  subdomain: くも膜下出血
  assertion:
    plain_statement_ja: ニモジピンは日本では承認されていないため、日本の脳卒中治療ガイドライン2021（改訂2023）では、遅発性脳血管攣縮に対してクラゾセンタン、ファスジル、オザグレルナトリウムの静脈内投与を行うことが妥当とされている。
    condition:
      population: 動脈瘤性くも膜下出血患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1561
    source: 日本脳卒中学会 脳卒中治療ガイドライン委員会 編『脳卒中治療ガイドライン2021〔改訂2023〕』協和企画
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 日本脳卒中学会の著作物（書籍、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 推奨文は改訂2025の公開テキストでも同じ趣旨であることを確認した。クラゾセンタン、塩酸ファスジル、オザグレルナトリウムはいずれも国内承認薬である。ニモジピンの国内未承認は国内の学会資料でも明記されている。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-020
  domain: ST
  subdomain: 脳動脈瘤
  assertion:
    plain_statement_ja: 日本の未破裂脳動脈瘤の前向きコホート（UCAS Japan、5720例・6697個）では、年間破裂率は0.95%であり、破裂リスクは動脈瘤の大きさ、部位（中大脳動脈に比べて前交通動脈と後交通動脈で高い）、および娘瘤（daughter sac）の有無によって異なった。
    condition:
      population: 未破裂脳動脈瘤（3 mm以上）を有する日本人患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1569
    source: The UCAS Japan Investigators (Morita A, et al.). The natural course of unruptured cerebral aneurysms in a Japanese cohort. N Engl J Med. 2012;366(26):2474-2482
    doi: 10.1056/NEJMoa1113260
    pmid: '22738097'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1113260
    source_license: NEJM（Massachusetts Medical Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。治療を受けた動脈瘤は打ち切りとして扱われており、自然歴の解釈には選択バイアスの可能性がある。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)；TBL-01-00-030 (id: Jlvnlcg)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-021
  domain: ST
  subdomain: 脳動脈瘤
  assertion:
    plain_statement_ja: UCAS Japanでは、3〜4 mmの動脈瘤に対する破裂のハザード比は、5〜6 mmで1.13、7〜9 mmで3.35、10〜24 mmで9.09、25 mm以上で76.26であり、大きさとともに破裂リスクが著しく上昇した。
    condition:
      population: 未破裂脳動脈瘤を有する日本人患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1569
    source: The UCAS Japan Investigators (Morita A, et al.). The natural course of unruptured cerebral aneurysms in a Japanese cohort. N Engl J Med. 2012;366(26):2474-2482
    doi: 10.1056/NEJMoa1113260
    pmid: '22738097'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1113260
    source_license: NEJM（Massachusetts Medical Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。部位別・大きさ別の年間破裂率の表は本文による。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)；TBL-01-00-030 (id: Jlvnlcg)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-022
  domain: ST
  subdomain: 解離性脳動脈瘤
  assertion:
    plain_statement_ja: くも膜下出血を来した椎骨動脈解離性動脈瘤では再出血が高率に起こり（本邦62例の検討で37%）、その多くは24時間以内であり、再出血した患者は死亡率が高く転帰が不良であるため、早期の治療介入が必要である。
    condition:
      population: 椎骨動脈解離性動脈瘤によるくも膜下出血患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1571
    source: Takagi T, Takayasu M, Suzuki Y, Yoshida J. Prediction of rebleeding from angiographic features in vertebral artery dissecting aneurysms. Neurosurg Rev. 2007;30(1):32-38
    doi: 10.1007/s10143-006-0049-1
    pmid: '17061136'
    pmcid: null
    url: https://doi.org/10.1007/s10143-006-0049-1
    source_license: Neurosurgical Review（Springer、テキストマイニング用ライセンスのみ）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。単一施設の後ろ向き検討であり、再出血率は血管撮影上の形態（狭窄と拡張の型）と後下小脳動脈起始部との位置関係によっても異なった。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)；TBL-01-00-030 (id: Jlvnlcg)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-023
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: 心原性脳塞栓症は心腔内に形成された血栓が脳動脈を急激に閉塞して生じ、その最大の原因は心房細動であり、発症は突発的で重症化しやすい。
    condition:
      population: 心房細動を有する成人
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1585
    source: Kleindorfer DO et al. 2021 Guideline for the Prevention of Stroke in Patients With Stroke and Transient Ischemic Attack. Stroke 2021
    doi: 10.1161/STR.0000000000000375
    pmid: '34024117'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000375
    source_license: AHA/ASAガイドライン（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 心房細動の抗凝固療法そのものの詳細は循環器領域のカードに譲る。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-①（心原性脳塞栓症、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-024
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: 心房細動を伴う急性期脳梗塞後のDOAC開始は、ELAN試験では早期開始（軽症・中等症は48時間以内、重症は6〜7日目）と後期開始（軽症3〜4日目、中等症6〜7日目、重症12〜14日目）で30日以内の複合アウトカム（再発脳梗塞・全身性塞栓症・大出血・症候性頭蓋内出血・血管死）は早期群2.9%・後期群4.1%であり、症候性頭蓋内出血は両群とも0.2%であった。
    condition:
      population: 心房細動を伴う急性期脳梗塞患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1584
    source: Fischer U et al. Early versus Later Anticoagulation for Stroke with Atrial Fibrillation (ELAN). N Engl J Med 2023
    doi: 10.1056/NEJMoa2303048
    pmid: '37222476'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2303048
    source_license: NEJM（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: DOACは日本で心房細動の塞栓予防に承認・保険適用がある。開始時期の最終判断は梗塞サイズと出血性変化の画像評価による。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-①（心原性脳塞栓症、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-025
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: 日本の脳卒中治療ガイドライン2021（改訂2023）では、心原性脳塞栓症の二次予防として心房細動に対してDOACを含む経口抗凝固療法を行い、抗血小板薬の併用は原則として行わない。
    condition:
      population: 心房細動による心原性脳塞栓症患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1581
    source: 日本脳卒中学会 脳卒中治療ガイドライン2021［改訂2023］（書籍）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 日本脳卒中学会ガイドライン（書籍、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: DOAC・ワルファリンは日本で承認・保険適用がある。機械弁・中等度以上の僧帽弁狭窄ではワルファリンが対象となる。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-①（心原性脳塞栓症、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-026
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: アテローム血栓性脳梗塞は、頭蓋内外の主幹動脈のアテローム硬化性プラークの破綻と血栓形成により、動脈-動脈塞栓または血行力学性機序で脳梗塞を生じる病型である。
    condition:
      population: 非心原性脳梗塞患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1585
    source: Kleindorfer DO et al. 2021 Guideline for the Prevention of Stroke in Patients With Stroke and Transient Ischemic Attack. Stroke 2021
    doi: 10.1161/STR.0000000000000375
    pmid: '34024117'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000375
    source_license: AHA/ASAガイドライン（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ''
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-027
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: 軽症脳梗塞・高リスクTIAに対するアスピリンとクロピドグレルの併用（DAPT）は発症後早期に開始し、併用期間は21日間を基本として、その後は抗血小板薬単剤に切り替える。
    condition:
      population: 軽症脳梗塞・高リスクTIA患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1585
    source: Kleindorfer DO et al. 2021 Guideline for the Prevention of Stroke in Patients With Stroke and Transient Ischemic Attack. Stroke 2021
    doi: 10.1161/STR.0000000000000375
    pmid: '34024117'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000375
    source_license: AHA/ASAガイドライン（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: アスピリン・クロピドグレルは日本で脳梗塞再発予防に承認・保険適用がある。POINT試験では併用で大出血が増加したため長期併用は避ける。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-028
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: CHANCE試験では、発症24時間以内の軽症脳梗塞・TIAに対してクロピドグレルとアスピリンの併用はアスピリン単独より90日以内の脳卒中再発が少なく（8.2%対11.7%、ハザード比0.68）、中等度・重度出血は増えなかった。
    condition:
      population: 発症24時間以内の軽症脳梗塞・TIA患者（中国）
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1586
    source: Wang Y et al. Clopidogrel with aspirin in acute minor stroke or transient ischemic attack (CHANCE). N Engl J Med 2013
    doi: 10.1056/NEJMoa1215340
    pmid: '23803136'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1215340
    source_license: NEJM（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 対象は中国の集団であり、CYP2C19多型の頻度など日本への外挿には注意する。薬剤は国内承認・保険適用あり。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-029
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: 日本のCSPS.com試験では、再発リスクの高い非心原性脳梗塞に対してシロスタゾールとアスピリンまたはクロピドグレルの併用は、単剤療法より虚血性脳卒中再発が少なく（年率2.2%対4.5%、ハザード比0.49）、重篤な出血のリスクは同等であった。
    condition:
      population: 再発高リスクの非心原性脳梗塞患者（日本）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1588
    source: Toyoda K et al. Dual antiplatelet therapy using cilostazol for secondary prevention in patients with high-risk ischaemic stroke in Japan (CSPS.com). Lancet Neurol 2019
    doi: 10.1016/S1474-4422(19)30148-6
    pmid: '31122494'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(19)30148-6
    source_license: Lancet Neurology（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: シロスタゾールは日本で脳梗塞再発予防に承認・保険適用がある。うっ血性心不全では禁忌である。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-030
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: 日本では発症4.5時間以内の急性期脳梗塞に対するrt-PA（アルテプラーゼ）静注療法の用量は0.6mg/kgであり、J-ACTでは3か月後の転帰良好（mRS 0〜1）が36.9%、36時間以内の症候性頭蓋内出血が5.8%であった。
    condition:
      population: 発症4.5時間以内の急性期脳梗塞患者（日本）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1583
    source: 'Yamaguchi T et al. Alteplase at 0.6 mg/kg for acute ischemic stroke within 3 hours of onset: Japan Alteplase Clinical Trial (J-ACT). Stroke 2006'
    doi: 10.1161/01.STR.0000227191.01792.e3
    pmid: '16763187'
    pmcid: null
    url: https://doi.org/10.1161/01.STR.0000227191.01792.e3
    source_license: Stroke誌（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: アルテプラーゼは日本で虚血性脳血管障害に承認・保険適用があり、国内用量は0.6mg/kg（上限等は添付文書参照）。適応時間は国内では4.5時間以内。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-031
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: 米国のAHA/ASAガイドラインでは、適応のある発症4.5時間以内の急性期脳梗塞に対するアルテプラーゼ静注の用量は0.9mg/kg（最大90mg）とされており、日本の承認用量0.6mg/kgとは異なる。
    condition:
      population: 発症4.5時間以内の急性期脳梗塞患者（米国）
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1582
    source: 'Powers WJ et al. Guidelines for the Early Management of Patients With Acute Ischemic Stroke: 2019 Update. Stroke 2019'
    doi: 10.1161/STR.0000000000000211
    pmid: '31662037'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000211
    source_license: Stroke誌 AHA/ASAガイドライン（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは米国の推奨であり、日本で0.9mg/kgを用いることは承認範囲外である。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-032
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: DAWN試験では、最終健常から6〜24時間で臨床症状と梗塞体積のミスマッチがある前方循環閉塞患者に対して血栓回収療法と標準治療の併用は、標準治療単独より90日後の機能的転帰が良好であった。
    condition:
      population: 発症6〜24時間の前方循環主幹動脈閉塞患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1595
    source: Nogueira RG et al. Thrombectomy 6 to 24 Hours after Stroke with a Mismatch between Deficit and Infarct (DAWN). N Engl J Med 2018
    doi: 10.1056/NEJMoa1706442
    pmid: '29129157'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1706442
    source_license: NEJM（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: DEFUSE 3試験では灌流画像で選択した6〜16時間の患者で血栓回収の有効性が示された（SRC-1596）。国内の時間枠・適応は日本のガイドラインと各施設基準に従う。血栓回収用デバイスは国内承認・保険適用がある。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-033
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: ラクナ梗塞は穿通枝領域の小梗塞であり、脳小血管病（細動脈硬化・リポヒアリノーシス等）を背景とし、白質病変・微小出血・血管周囲腔拡大などの小血管病所見を伴うことが多い。
    condition:
      population: ラクナ梗塞患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1590
    source: Wardlaw JM et al. Neuroimaging standards for research into small vessel disease (STRIVE). Lancet Neurol 2013
    doi: 10.1016/S1474-4422(13)70124-8
    pmid: '23867200'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(13)70124-8
    source_license: Lancet Neurology（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ''
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-③（ラクナ梗塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-034
  domain: ST
  subdomain: 脳梗塞
  assertion:
    plain_statement_ja: SPS3試験では、最近のラクナ梗塞患者に対するアスピリンへのクロピドグレル追加（長期DAPT）は再発脳卒中を有意に減らさず、出血と死亡を有意に増やした。
    condition:
      population: ラクナ梗塞患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1589
    source: SPS3 Investigators. Effects of clopidogrel added to aspirin in patients with recent lacunar stroke. N Engl J Med 2012
    doi: 10.1056/NEJMoa1204133
    pmid: '22931315'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1204133
    source_license: NEJM（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤はいずれも国内承認・保険適用があるが、ラクナ梗塞への長期DAPTは行わない。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-③（ラクナ梗塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-035
  domain: ST
  subdomain: 一過性脳虚血発作
  assertion:
    plain_statement_ja: 一過性脳虚血発作（TIA）の現在の定義は時間ではなく組織に基づき、急性梗塞を伴わずに一過性の神経機能障害を来したエピソードを指し、MRIで梗塞があれば時間にかかわらず脳梗塞と診断する。
    condition:
      population: TIA疑い患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1591
    source: 'Easton JD et al. Definition and evaluation of transient ischemic attack: AHA/ASA scientific statement. Stroke 2009'
    doi: 10.1161/STROKEAHA.108.192218
    pmid: '19423857'
    pmcid: null
    url: https://doi.org/10.1161/STROKEAHA.108.192218
    source_license: Stroke誌 AHA科学的声明（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本のガイドラインでも組織ベースの定義が採用されている。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-④（一過性脳虚血発作、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-029 (id: JlvnlcY)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-036
  domain: ST
  subdomain: 一過性脳虚血発作
  assertion:
    plain_statement_ja: ABCD2スコアは年齢・血圧・臨床症状（一側性脱力・言語障害）・症状持続時間・糖尿病の5項目（0〜7点）からなり、TIA後の早期脳卒中リスク層別化に用いる。
    condition:
      population: TIA患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1592
    source: Johnston SC et al. Validation and refinement of scores to predict very early stroke risk after transient ischaemic attack (ABCD2). Lancet 2007
    doi: 10.1016/S0140-6736(07)60150-0
    pmid: '17258668'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(07)60150-0
    source_license: Lancet（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: スコアが低くても画像・機序評価を省略せず、緊急評価の要否は総合的に判断する。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-④（一過性脳虚血発作、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-029 (id: JlvnlcY)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-037
  domain: ST
  subdomain: 一過性脳虚血発作
  assertion:
    plain_statement_ja: TIAは脳梗塞の前兆であり、発症直後の再発リスクが高いため、頭部MRI・血管評価・心電図等による機序の緊急評価と、原因に応じた二次予防（抗血小板療法・抗凝固・頸動脈治療等）を直ちに開始する。
    condition:
      population: TIA患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1585
    source: Kleindorfer DO et al. 2021 Guideline for the Prevention of Stroke in Patients With Stroke and Transient Ischemic Attack. Stroke 2021
    doi: 10.1161/STR.0000000000000375
    pmid: '34024117'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000375
    source_license: AHA/ASAガイドライン（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤は国内承認・保険適用があるものを使用する。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-④（一過性脳虚血発作、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-029 (id: JlvnlcY)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-038
  domain: ST
  subdomain: 脳動脈狭窄・閉塞
  assertion:
    plain_statement_ja: CREST試験では、症候性・無症候性の頸動脈狭窄に対して頸動脈ステント留置術と頸動脈内膜剥離術（CEA）の間で主要評価項目（脳卒中・心筋梗塞・死亡の複合）の推定4年率は有意差がなかった（7.2%対6.8%）。
    condition:
      population: 頸動脈狭窄患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1593
    source: Brott TG et al. Stenting versus endarterectomy for treatment of carotid-artery stenosis (CREST). N Engl J Med 2010
    doi: 10.1056/NEJMoa0912321
    pmid: '20505173'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa0912321
    source_license: NEJM（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 周術期はステント群で脳卒中が、CEA群で心筋梗塞が相対的に多いことが同試験で示されている。国内での術式選択は日本のガイドラインと狭窄度・症候性で判断する。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-⑤（脳動脈狭窄・閉塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-039
  domain: ST
  subdomain: 脳動脈狭窄・閉塞
  assertion:
    plain_statement_ja: 症候性頭蓋内動脈狭窄に対しては、SAMMPRIS試験で積極的内科治療（抗血小板療法と危険因子管理）がステント留置術より優れており（30日以内の脳卒中・死亡14.7%対5.8%）、まず内科治療が基本となる。
    condition:
      population: 症候性頭蓋内動脈狭窄患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1594
    source: Chimowitz MI et al. Stenting versus aggressive medical therapy for intracranial arterial stenosis (SAMMPRIS). N Engl J Med 2011
    doi: 10.1056/NEJMoa1105335
    pmid: '21899409'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1105335
    source_license: NEJM（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤は国内承認・保険適用がある。頭蓋内ステントは国内では限られた適応で判断する。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-C-⑤（脳動脈狭窄・閉塞、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-040
  domain: ST
  subdomain: その他の脳血管障害
  assertion:
    plain_statement_ja: 脳動脈解離は頭痛・頸部痛で発症することが多く、脳梗塞・TIAのほかHorner症候群などの局所症状を来し、画像では壁内血腫・内膜フラップ・数珠状変化などが診断の手がかりとなる。
    condition:
      population: 脳動脈解離患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1598
    source: 'Debette S, Leys D. Cervical-artery dissections: predisposing factors, diagnosis, and outcome. Lancet Neurol 2009'
    doi: 10.1016/S1474-4422(09)70084-5
    pmid: '19539238'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(09)70084-5
    source_license: Lancet Neurology（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頭蓋内解離ではくも膜下出血を来す場合があり、治療方針が頭蓋外解離と異なる。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-D-①（脳動脈解離、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-041
  domain: ST
  subdomain: その他の脳血管障害
  assertion:
    plain_statement_ja: CADISS試験では、症候性の頸部動脈（頸動脈・椎骨動脈）解離に対する抗血小板療法と抗凝固療法の間で脳卒中・死亡の予防効果に差はなく、再発脳卒中自体が両群ともまれであった。
    condition:
      population: 症候性頸部動脈解離患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1597
    source: Markus HS et al. Antiplatelet treatment compared with anticoagulation treatment for cervical artery dissection (CADISS). Lancet Neurol 2015
    doi: 10.1016/S1474-4422(15)70018-9
    pmid: '25684164'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(15)70018-9
    source_license: CC BY（Lancet Neurology、Crossref・本文で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 抗血小板薬・抗凝固薬はいずれも国内承認・保険適用がある薬剤から選択する。頭蓋内解離・くも膜下出血例は対象外である。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-D-①（脳動脈解離、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-042
  domain: ST
  subdomain: その他の脳血管障害
  assertion:
    plain_statement_ja: Spetzler-Martin分類は脳動静脈奇形を、大きさ（3cm未満・3〜6cm・6cm超）、 eloquent領域への近接、静脈還流（表在性・深部）の3要素の合計（grade I〜V）で分類し、手術リスク評価に用いる。
    condition:
      population: 脳動静脈奇形患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1599
    source: Spetzler RF, Martin NA. A proposed grading system for arteriovenous malformations. J Neurosurg 1986
    doi: 10.3171/jns.1986.65.4.0476
    pmid: '3760956'
    pmcid: null
    url: https://doi.org/10.3171/jns.1986.65.4.0476
    source_license: Journal of Neurosurgery（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ''
  curriculum:
    kokushi: 医学各論 Ⅸ-1-D-②（脳動静脈奇形、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-031 (id: Jlvnlck)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-043
  domain: ST
  subdomain: その他の脳血管障害
  assertion:
    plain_statement_ja: ARUBA試験では、未破裂脳動静脈奇形に対して内科治療単独は介入治療（手術・塞栓・定位放射線の単独または併用）併用より死亡・脳卒中の予防に優れており、平均33か月の追跡で内科治療単独が優位であった。
    condition:
      population: 未破裂脳動静脈奇形患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1600
    source: Mohr JP et al. Medical management with or without interventional therapy for unruptured brain arteriovenous malformations (ARUBA). Lancet 2014
    doi: 10.1016/S0140-6736(13)62302-8
    pmid: '24268105'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(13)62302-8
    source_license: Lancet（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 破裂例は対象外であり、治療は症例ごとに専門施設で判断する。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-D-②（脳動静脈奇形、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-031 (id: Jlvnlck)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-044
  domain: ST
  subdomain: その他の脳血管障害
  assertion:
    plain_statement_ja: 脳静脈洞血栓症の危険因子には妊娠・産褥、経口避妊薬、血栓性素因、感染症、悪性腫瘍などがあり、診断はMR venography等の静脈系画像で血栓と静脈洞の描出欠損を確認して行う。
    condition:
      population: 脳静脈洞血栓症疑い患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1601
    source: 'Saposnik G et al. Diagnosis and Management of Cerebral Venous Thrombosis: A Scientific Statement From the AHA. Stroke 2024'
    doi: 10.1161/STR.0000000000000456
    pmid: '38284265'
    pmcid: null
    url: https://doi.org/10.1161/STR.0000000000000456
    source_license: Stroke誌 AHA科学的声明（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頭痛が主症状で、頭蓋内圧亢進・てんかん・局所症状を伴うことがある。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-D-③（静脈洞血栓症、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-045
  domain: ST
  subdomain: その他の脳血管障害
  assertion:
    plain_statement_ja: RESPECT-CVT試験では、脳静脈血栓症に対するダビガトランと用量調整ワルファリンの間で再発静脈血栓塞栓症は認めず、出血リスクは同等であり、ダビガトランはワルファリンと同様に安全で有効な選択肢となりうることが示された。
    condition:
      population: 脳静脈洞血栓症患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1602
    source: Ferro JM et al. Safety and Efficacy of Dabigatran Etexilate vs Dose-Adjusted Warfarin in Patients With Cerebral Venous Thrombosis (RESPECT-CVT). JAMA Neurol 2019
    doi: 10.1001/jamaneurol.2019.2764
    pmid: '31479105'
    pmcid: null
    url: https://doi.org/10.1001/jamaneurol.2019.2764
    source_license: JAMA Neurology（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ダビガトラン・ワルファリンは国内承認薬だが、脳静脈血栓症への保険適用は添付文書で確認すること（本カード作成時点では個別確認未実施）。急性期はヘパリンによる抗凝固が先行する。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-D-③（静脈洞血栓症、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-046
  domain: ST
  subdomain: その他の脳血管障害
  assertion:
    plain_statement_ja: もやもや病の診断は、両側の内頸動脈終末部を中心とする狭窄・閉塞と、異常血管網（もやもや血管）の存在を血管画像で確認することに基づき、厚労省研究班の診断基準（2021年改訂）では片側例も条件付きで含まれる。
    condition:
      population: もやもや病疑い患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1603
    source: Kuroda S et al. Diagnostic Criteria for Moyamoya Disease - 2021 Revised Version. Neurol Med Chir (Tokyo) 2022
    doi: 10.2176/jns-nmc.2022-0072
    pmid: '35613882'
    pmcid: null
    url: https://doi.org/10.2176/jns-nmc.2022-0072
    source_license: Neurologia medico-chirurgica（CC BY-NC-ND、学会誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 鈴木分類は脳血管撮影による進行度分類（I〜VI期）であり、診断基準の画像所見と併せて用いる。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-D-④（もやもや病、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-032 (id: Jlvnlcs)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-047
  domain: ST
  subdomain: その他の脳血管障害
  assertion:
    plain_statement_ja: JAM試験では、出血発症のもやもや病に対する直接バイパス術は非手術群より有害イベントが少なく（14.3%対34.2%）、再出血予防効果が示唆された。
    condition:
      population: 出血発症もやもや病患者（成人）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1604
    source: 'Miyamoto S et al. Effects of extracranial-intracranial bypass for patients with hemorrhagic moyamoya disease: Japan Adult Moyamoya Trial (JAM). Stroke 2014'
    doi: 10.1161/STROKEAHA.113.004386
    pmid: '24668203'
    pmcid: null
    url: https://doi.org/10.1161/STROKEAHA.113.004386
    source_license: Stroke誌（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 虚血発症例へのバイパスの適応は別途、血行力学的評価に基づき判断する。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-D-④（もやもや病、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-032 (id: Jlvnlcs)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-048
  domain: ST
  subdomain: その他の脳血管障害
  assertion:
    plain_statement_ja: 硬膜動静脈瘻はCognard分類・Borden分類により静脈還流様式（特に皮質静脈への逆流の有無）で分類され、皮質静脈逆流を伴う病変は出血・神経症状のリスクが高く治療適応となる。
    condition:
      population: 硬膜動静脈瘻患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1605
    source: 'Cognard C et al. Cerebral dural arteriovenous fistulas: clinical and angiographic correlation with a revised classification of venous drainage. Radiology 1995'
    doi: 10.1148/radiology.194.3.7862961
    pmid: '7862961'
    pmcid: null
    url: https://doi.org/10.1148/radiology.194.3.7862961
    source_license: Radiology誌（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: Borden分類（J Neurosurg 1995、SRC-1606）も併せて用いられる。耳鳴・眼症状など還流先に応じた症状を来す。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-D-⑤（硬膜動静脈瘻、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-049
  domain: ST
  subdomain: 脳卒中後遺症
  assertion:
    plain_statement_ja: 偽性球麻痺は両側の皮質延髄路障害により生じ、構音障害・嚥下障害・舌運動障害を来すが、球麻痺と異なり舌の萎縮・線維束攣縮はなく、強制笑い・強制泣きを伴うことがある。
    condition:
      population: 多発性脳梗塞等の両側大脳病変患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1581
    source: 日本脳卒中学会 脳卒中治療ガイドライン2021［改訂2023］（書籍）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 日本脳卒中学会ガイドライン（書籍、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 嚥下評価・訓練の横断的総論は本カードの範囲外とし、脳卒中後の嚥下障害として扱った。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-E-①（偽性球麻痺、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: ST-050
  domain: ST
  subdomain: 脳卒中後遺症
  assertion:
    plain_statement_ja: AVERT試験では、発症24時間以内の頻回・高用量の超早期離床は通常ケアより3か月後の転帰良好のオッズを下げた（46%対50%、調整オッズ比0.73）ため、早期離床は量と負荷に注意して段階的に進める。
    condition:
      population: 急性期脳卒中患者
      region: 海外
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1607
    source: AVERT Trial Collaboration. Efficacy and safety of very early mobilisation within 24 h of stroke onset (AVERT). Lancet 2015
    doi: 10.1016/S0140-6736(15)60690-0
    pmid: '25892679'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(15)60690-0
    source_license: Lancet（出版社著作物、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 廃用性萎縮を含む廃用症候群の予防には早期からのリハビリテーションが基本だが、超早期の高負荷離床は避けるというのが本試験の含意である。
  curriculum:
    kokushi: 医学各論 Ⅸ-1-E-②（廃用性萎縮、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-001
  domain: BT
  subdomain: 神経膠腫
  assertion:
    plain_statement_ja: WHO中枢神経系腫瘍分類第5版（2021年）では、成人びまん性神経膠腫は分子診断に基づいて分類され、IDH変異の有無が分類の軸となり、IDH変異型では1p/19q共欠失の有無により星細胞腫と乏突起膠腫が分けられるなど、組織像と分子所見を統合した診断（統合診断）が行われる。
    condition:
      population: 成人びまん性神経膠腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1611
    source: 'Louis DN, et al. The 2021 WHO Classification of Tumours of the Central Nervous System: a summary. Neuro Oncol. 2021;23(8):1231-1251'
    doi: 10.1093/neuonc/noab106
    pmid: '34185076'
    pmcid: null
    url: https://doi.org/10.1093/neuonc/noab106
    source_license: Oxford University Press 標準出版モデル（Neuro-Oncology誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 分類の枠組みは2021年版の総説に基づく。MGMTプロモーターのメチル化は主に膠芽腫の治療反応性の指標として用いられる点であり、分類そのものの軸ではない。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-①（神経膠腫、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-002
  domain: BT
  subdomain: 神経膠腫
  assertion:
    plain_statement_ja: 新規診断膠芽腫に対する放射線治療（60 Gy/30回）へのテモゾロミドの連日併用（75 mg/m²/日）と、その後のテモゾロミド補助療法（150〜200 mg/m²、5日間投与・28日周期、6サイクル）の追加は、放射線治療単独と比べて全生存期間を延長した（生存期間中央値14.6か月対12.1か月、2年生存率26.5%対10.4%）。
    condition:
      population: 新規診断膠芽腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1612
    source: Stupp R, et al. Radiotherapy plus concomitant and adjuvant temozolomide for glioblastoma. N Engl J Med. 2005;352(10):987-996
    doi: 10.1056/NEJMoa043330
    pmid: '15758009'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa043330
    source_license: NEJM（Massachusetts Medical Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。テモゾロミドは国内で悪性神経膠腫に対して承認された薬剤として臨床使用されているが、本作成では添付文書での適応・用法の個別確認は未実施であり、取り込み時に確認を要する。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-①（神経膠腫、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-630 (id: Jlvnma4)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-003
  domain: BT
  subdomain: 神経膠腫
  assertion:
    plain_statement_ja: 新規診断膠芽腫では、維持テモゾロミド療法に腫瘍治療電場療法（TTFields）を追加すると、テモゾロミド単独と比べて無増悪生存期間（中央値6.7か月対4.0か月）と全生存期間（中央値20.9か月対16.0か月）が延長した（EF-14試験）。
    condition:
      population: 放射線化学療法を終えた新規診断膠芽腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1613
    source: 'Stupp R, et al. Effect of Tumor Treating Fields Plus Maintenance Temozolomide vs Maintenance Temozolomide Alone on Survival in Patients With Glioblastoma: A Randomized Clinical Trial. JAMA. 2017;318(23):2306-2316'
    doi: 10.1001/jama.2017.18718
    pmid: '29260225'
    pmcid: null
    url: https://doi.org/10.1001/jama.2017.18718
    source_license: JAMA（American Medical Association、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。TTFieldsの国内承認・保険適用の状況は本作成では個別確認未実施であり、取り込み時に確認を要する。主な有害事象はアレイ装着部位の皮膚障害である。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-①（神経膠腫、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-630 (id: Jlvnma4)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-004
  domain: BT
  subdomain: 神経膠腫
  assertion:
    plain_statement_ja: 高リスク低悪性度神経膠腫（40歳以上、または亜全摘以下）に対する放射線治療後のPCV療法（プロカルバジン、ロムスチン、ビンクリスチン）の追加は、放射線治療単独と比べて全生存期間を延長した（生存期間中央値13.3年対7.8年）（RTOG 9802長期成績）。
    condition:
      population: 高リスク低悪性度神経膠腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1614
    source: Buckner JC, et al. Radiation plus Procarbazine, CCNU, and Vincristine in Low-Grade Glioma. N Engl J Med. 2016;374(14):1344-1355
    doi: 10.1056/NEJMoa1500925
    pmid: '27050206'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1500925
    source_license: NEJM（Massachusetts Medical Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。PCV療法の構成薬（プロカルバジン、ロムスチン、ビンクリスチン）の国内承認・保険適用の状況は本作成では個別確認未実施であり、取り込み時に確認を要する。現在の実臨床では分子分類に応じた治療選択が進んでおり、本試験は分子分類導入前の集団の結果である。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-①（神経膠腫、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-005
  domain: BT
  subdomain: 悪性リンパ腫
  assertion:
    plain_statement_ja: 中枢神経原発悪性リンパ腫（PCNSL）が疑われる場合、副腎皮質ステロイドは腫瘍細胞の生存能に速やかに影響するため、生検前に投与すると診断が困難になりうる。すでに投与されている場合は投与を中止し、必要に応じてMRIを再検してから定位生検を行うことがある。確定診断の標準は定位生検による組織病理診断である。
    condition:
      population: PCNSLが疑われる患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1615
    source: 'Ferreri AJM, et al. Primary central nervous system lymphomas: EHA-ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up. HemaSphere. 2024;8(6):e89'
    doi: 10.1002/hem3.89
    pmid: '38836097'
    pmcid: null
    url: https://doi.org/10.1002/hem3.89
    source_license: CC BY 4.0（HemaSphere誌掲載版）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: ガイドライン本文の記載に基づく。頭蓋内圧亢進などでステロイドが回避できない臨床状況の扱いは個別判断であり、本カードの範囲外。 副腎皮質ステロイドは国内で承認された薬剤であり、本カードは適応の推奨ではなく生検前投与が診断に与える影響に関するものである。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-②（悪性リンパ腫、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-006
  domain: BT
  subdomain: 悪性リンパ腫
  assertion:
    plain_statement_ja: 免疫能が正常なPCNSLの第一選択治療は、高用量メトトレキサートを基盤とする併用化学療法であり、前向き試験で検証されたレジメン（MATRixなど）が推奨される。
    condition:
      population: 免疫能が正常な新規診断PCNSL患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1615
    source: 'Ferreri AJM, et al. Primary central nervous system lymphomas: EHA-ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up. HemaSphere. 2024;8(6):e89'
    doi: 10.1002/hem3.89
    pmid: '38836097'
    pmcid: null
    url: https://doi.org/10.1002/hem3.89
    source_license: CC BY 4.0（HemaSphere誌掲載版）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: ガイドラインの推奨に基づく。高用量メトトレキサートを含むレジメンの国内承認・保険適用の状況は本作成では個別確認未実施であり、取り込み時に確認を要する。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-②（悪性リンパ腫、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-007
  domain: BT
  subdomain: 悪性リンパ腫
  assertion:
    plain_statement_ja: PCNSLに対するIELSG32試験の第1ランダム化では、MATRixレジメン（メトトレキサート、シタラビン、チオテパ、リツキシマブ）は、メトトレキサート＋シタラビン、またはそれにリツキシマブを加えた治療と比べて完全寛解率が高かった（49%対30%対23%）。
    condition:
      population: 新規診断PCNSL患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1616
    source: 'Ferreri AJM, et al. Chemoimmunotherapy with methotrexate, cytarabine, thiotepa, and rituximab (MATRix regimen) in patients with primary CNS lymphoma: results of the first randomisation of the International Extranodal Lymphoma Study Group-32 (IELSG32) phase 2 trial. Lancet Haematol. 2016;3(5):e217-e227'
    doi: 10.1016/S2352-3026(16)00036-3
    pmid: '27132696'
    pmcid: null
    url: https://doi.org/10.1016/S2352-3026(16)00036-3
    source_license: The Lancet Haematology（Elsevier、テキストマイニング用ライセンスのみ）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。チオテパを含むレジメンの国内承認・保険適用の状況は本作成では個別確認未実施であり、取り込み時に確認を要する。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-②（悪性リンパ腫、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-008
  domain: BT
  subdomain: 胚細胞腫瘍
  assertion:
    plain_statement_ja: 頭蓋内胚細胞腫瘍は、血清・髄液の腫瘍マーカーと組織所見によってジャーミノーマと非ジャーミノーマ性胚細胞腫瘍（NGGCT）に分けて治療方針が決められ、転移性病変は髄液細胞診陽性または頭蓋脊髄MRIでの播種所見によって定義される。
    condition:
      population: 思春期・若年成人の頭蓋内胚細胞腫瘍患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1617
    source: Frappaz D, et al. EANO, SNO and Euracan consensus review on the current management and future development of intracranial germ cell tumors in adolescents and young adults. Neuro Oncol. 2022;24(4):516-527
    doi: 10.1093/neuonc/noab252
    pmid: '34724065'
    pmcid: null
    url: https://doi.org/10.1093/neuonc/noab252
    source_license: CC BY-NC 4.0（Neuro-Oncology誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: コンセンサスレビューの抄録に基づく。診断は内視鏡下生検と血清・髄液検査の組み合わせで確定を図ることが同レビューで述べられている。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-③（胚細胞腫瘍、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-009
  domain: BT
  subdomain: 胚細胞腫瘍
  assertion:
    plain_statement_ja: 限局性ジャーミノーマは放射線感受性が高く、化学療法後に全脳室照射と局所追加照射を行う治療で5年無イベント生存率が90%を超え、転移性ジャーミノーマは全頭蓋脊髄照射で治癒が期待できる。
    condition:
      population: 頭蓋内ジャーミノーマ患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1617
    source: Frappaz D, et al. EANO, SNO and Euracan consensus review on the current management and future development of intracranial germ cell tumors in adolescents and young adults. Neuro Oncol. 2022;24(4):516-527
    doi: 10.1093/neuonc/noab252
    pmid: '34724065'
    pmcid: null
    url: https://doi.org/10.1093/neuonc/noab252
    source_license: CC BY-NC 4.0（Neuro-Oncology誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認（5年無イベント生存率90%超は限局性ジャーミノーマに対する化学療法＋全脳室照射の成績）。NGGCTの5年無イベント生存率は70%超と同抄録に記載されている。 化学療法の個別薬剤の国内承認・保険適用は未確認。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-③（胚細胞腫瘍、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-010
  domain: BT
  subdomain: 胚細胞腫瘍
  assertion:
    plain_statement_ja: 中枢神経系胚細胞腫瘍の腫瘍マーカーでは、HCGの上昇はジャーミノーマ成分または絨毛癌成分を含む場合に限られ、両者の間に明確なカットオフが存在する一方、AFPは卵黄嚢腫瘍成分がなくても、特に未熟奇形腫で上昇することが多い。HCGが髄液でのみ、AFPが血清でのみ上昇する例があるため、血清と髄液の両方を測定する意義がある。
    condition:
      population: 中枢神経系胚細胞腫瘍患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1618
    source: 'Takami H, et al. Impact of tumor markers on diagnosis, treatment and prognosis in CNS germ cell tumors: correlations with clinical practice and histopathology. Brain Tumor Pathol. 2023;40(2):124-132'
    doi: 10.1007/s10014-023-00460-x
    pmid: '36995447'
    pmcid: null
    url: https://doi.org/10.1007/s10014-023-00460-x
    source_license: Brain Tumor Pathology（Springer、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値の詳細（各群の症例数など）は抄録で確認した範囲に限る。マーカー上昇のみでNGGCTと確定することはできず、組織所見との統合解釈が必要である点も同論文で述べられている。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-③（胚細胞腫瘍、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-011
  domain: BT
  subdomain: 血管芽腫
  assertion:
    plain_statement_ja: von Hippel-Lindau病患者の中枢神経系血管芽腫は脊髄と小脳に多く発生し、症状を呈した小脳腫瘍では嚢胞を伴う割合が高く（72%）、無症状の小脳腫瘍（13%）と比べて嚢胞が腫瘍本体より大きくなることが多い。
    condition:
      population: von Hippel-Lindau病患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1619
    source: Wanebo JE, et al. The natural history of hemangioblastomas of the central nervous system in patients with von Hippel-Lindau disease. J Neurosurg. 2003;98(1):82-94
    doi: 10.3171/jns.2003.98.1.0082
    pmid: '12546356'
    pmcid: null
    url: https://doi.org/10.3171/jns.2003.98.1.0082
    source_license: Journal of Neurosurgery（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。本カードは腫瘍そのものの分布と嚢胞の特徴に限り、VHLの全身像（網膜・腎・膵などの病変）は扱わない。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-A-④（血管芽腫、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-012
  domain: BT
  subdomain: 髄膜腫
  assertion:
    plain_statement_ja: 髄膜腫は最も頻度の高い原発性頭蓋内腫瘍であり、無症状で偶然発見された場合は画像による経過観察（watch-and-scan）が選択でき、手術を行う場合は被膜・付着部硬膜を含めた全摘出がしばしば根治的となる。手術不能例や再発例では、病変の大きさと部位が許せば定位放射線治療や分割照射が用いられる。
    condition:
      population: 髄膜腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1620
    source: Goldbrunner R, et al. EANO guideline on the diagnosis and management of meningiomas. Neuro Oncol. 2021;23(11):1821-1834
    doi: 10.1093/neuonc/noab150
    pmid: '34181733'
    pmcid: null
    url: https://doi.org/10.1093/neuonc/noab150
    source_license: Oxford University Press 標準出版モデル（Neuro-Oncology誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインの抄録に基づく。WHO gradeに応じた術後照射の適応の詳細はガイドライン本文の推奨による。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-B-①（髄膜腫、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-631 (id: Jlvnma8)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-013
  domain: BT
  subdomain: 下垂体腫瘍
  assertion:
    plain_statement_ja: 下垂体腺腫は腫瘤効果により頭痛、下垂体機能低下、視交叉圧迫による視野障害（両耳側半盲）を来しうる。プロラクチノーマを除く下垂体腺腫の初期治療は原則として経蝶形骨洞下垂体手術であり、無症状の偶発例では経過観察も選択できる。
    condition:
      population: 下垂体腺腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-877
    source: 'Molitch ME. Diagnosis and Treatment of Pituitary Adenomas: A Review. JAMA. 2017;317(5):516-524.'
    doi: 10.1001/jama.2016.19699
    pmid: '28170483'
    pmcid: null
    url: https://doi.org/10.1001/jama.2016.19699
    source_license: ライセンス表示を確認できず（JAMA誌）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードは腫瘍としての側面（腫瘤効果と手術）に限り、ホルモン産生・内分泌の側面は扱わない。抄録では視野障害と総称されており、両耳側半盲は視交叉圧迫による典型的な視野障害として本文の記載に基づく。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-B-②（下垂体腫瘍(下垂体腺腫)、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-014
  domain: BT
  subdomain: 下垂体腫瘍
  assertion:
    plain_statement_ja: 下垂体卒中は、突然発症の頭痛などを呈する臨床症候群であり医学的緊急事態である。速やかなヒドロコルチゾンの補充が救命的となりうる。
    condition:
      population: 下垂体卒中患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-884
    source: Rajasekaran S, Vanderpump M, Baldeweg S, et al. UK Guidelines for the Management of Pituitary Apoplexy. Clinical Endocrinology. 2011;74(1):9-20.
    doi: 10.1111/j.1365-2265.2010.03913.x
    pmid: '21044119'
    pmcid: null
    url: https://doi.org/10.1111/j.1365-2265.2010.03913.x
    source_license: ライセンス表示を確認できず（Clinical Endocrinology誌）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ガイドラインの抄録に基づく。手術（経蝶形骨洞手術）の適応と時期は視力・意識の状態により判断され、本カードでは一般論にとどめる。ヒドロコルチゾンは国内承認薬である（適応の詳細は添付文書による）。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-B-②（下垂体腫瘍(下垂体腺腫)、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-015
  domain: BT
  subdomain: 神経鞘腫
  assertion:
    plain_statement_ja: 前庭神経鞘腫の診断はMRIによるもので、組織診断は必ずしも必要ない。治療の選択肢は経過観察、外科的切除、分割照射、定位放射線治療であり、小さな腫瘍では経過観察と定位放射線治療が比較検討され、大きな腫瘍では外科的な圧迫解除が必須で、術後に分割照射や定位放射線治療が追加されることがある。
    condition:
      population: 前庭神経鞘腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1621
    source: Goldbrunner R, et al. EANO guideline on the diagnosis and treatment of vestibular schwannoma. Neuro Oncol. 2020;22(1):31-45
    doi: 10.1093/neuonc/noz153
    pmid: '31504802'
    pmcid: null
    url: https://doi.org/10.1093/neuonc/noz153
    source_license: Oxford University Press 標準出版モデル（Neuro-Oncology誌、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインの抄録に基づく。聴力温存率などの治療法別の数値は抄録の範囲では確認できなかったため本カードには含めていない。片側の感音難聴・耳鳴が典型的な初発症状である点はガイドライン本文の記載による。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-B-③（神経鞘腫、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-632 (id: JlvnmbE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-016
  domain: BT
  subdomain: 頭蓋咽頭腫
  assertion:
    plain_statement_ja: 頭蓋咽頭腫にはエナメル上皮腫型と乳頭型があり、エナメル上皮腫型は5〜15歳と45〜60歳の二峰性の発症ピークを示し小児にみられる型である。視交叉、視床下部、下垂体に近接するため、視力障害、内分泌障害、頭蓋内圧亢進症状を来し、長期生存率は高い一方で視床下部の障害による生活の質の低下が問題となる。
    condition:
      population: 頭蓋咽頭腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-874
    source: Müller HL, Merchant TE, Warmuth-Metz M, Martinez-Barbera JP, Puget S. Craniopharyngioma. Nature Reviews Disease Primers. 2019;5(1):75.
    doi: 10.1038/s41572-019-0125-9
    pmid: '31699993'
    pmcid: null
    url: https://doi.org/10.1038/s41572-019-0125-9
    source_license: ライセンス表示を確認できず（Nature Reviews Disease Primers誌、TDM のみ）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値（発症年齢のピーク）は抄録で確認。石灰化はエナメル上皮腫型の画像上の特徴として知られるが、本出典の抄録の範囲では明示されなかったため本カードの命題には含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-B-④（頭蓋咽頭腫、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-017
  domain: BT
  subdomain: 転移性脳腫瘍
  assertion:
    plain_statement_ja: 転移性脳腫瘍では、腫瘤効果の強い大きな病変には手術が妥当であり、未切除の1〜4個の転移（小細胞肺癌を除く）には定位放射線治療単独が、切除された1〜2個の転移には術後腔への定位放射線治療が選択肢となる。全脳照射を行う場合は、海馬を避けメマンチンを併用することが、生存期間4か月以上が見込まれ海馬近傍に病変がない患者で提案される。
    condition:
      population: 転移性脳腫瘍患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1622
    source: 'Vogelbaum MA, et al. (Schiff D, et al.) Treatment for Brain Metastases: ASCO-SNO-ASTRO Guideline. J Clin Oncol. 2022;40(3):242-264'
    doi: 10.1200/JCO.21.02314
    pmid: '34932393'
    pmcid: null
    url: https://doi.org/10.1200/JCO.21.02314
    source_license: Journal of Clinical Oncology（ASCO、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインの抄録に基づく。原発巣の全身治療は本カードの範囲外。原発巣としては肺癌が最も多いことは脳転移の疫学として確立しているが、本ガイドラインの抄録の範囲では割合の数値を確認できなかったため数値は含めていない。メマンチンの国内承認は認知症に対するものであり、脳転移の全脳照射併用としての国内保険適用は本作成では確認未実施。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-C-①（転移性脳腫瘍、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-633 (id: JlvnmbI)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-018
  domain: BT
  subdomain: 髄膜癌腫症
  assertion:
    plain_statement_ja: 髄膜癌腫症（癌性髄膜炎）では、頭痛、悪心・嘔吐、認知機能の変化、歩行困難、脳神経麻痺、神経根症状、頸部・背部痛など多彩な症状がみられる。確定診断は髄液中の腫瘍細胞の証明（type I）によるもので、初回の髄液検査が陰性でも2回目の検査を行うことが推奨される。予後は不良で、治療目標は神経症状の進行を防ぎつつ生活の質を保って生存を延長することにある。
    condition:
      population: 固形癌の髄膜転移患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1623
    source: 'Le Rhun E, et al. Leptomeningeal metastasis from solid tumours: EANO-ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up. ESMO Open. 2023;8(5):101624'
    doi: 10.1016/j.esmoop.2023.101624
    pmid: '37863528'
    pmcid: null
    url: https://doi.org/10.1016/j.esmoop.2023.101624
    source_license: CC BY-NC-ND 4.0（ESMO Open誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドライン本文で確認。生存期間の具体的な中央値は本作成で一次資料から確認できなかったため本カードには含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-C-②（髄膜癌腫症<癌性髄膜炎>、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BT-019
  domain: BT
  subdomain: 頭蓋骨転移
  assertion:
    plain_statement_ja: 日本の単施設の転移性頭蓋骨腫瘍175例では、原発巣は乳癌（55%）が最も多く、次いで肺癌（14%）、前立腺癌（6%）であり、患者の多くは無症状だが、局所の疼痛や脳神経麻痺を呈する例があり、症候性の例では局所または頭蓋全体への放射線治療が主に用いられた。
    condition:
      population: 転移性頭蓋骨腫瘍患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1624
    source: 'Mitsuya K, et al. Metastatic skull tumors: MRI features and a new conventional classification. J Neurooncol. 2011;104(1):239-245'
    doi: 10.1007/s11060-010-0465-5
    pmid: '21110218'
    pmcid: null
    url: https://doi.org/10.1007/s11060-010-0465-5
    source_license: CC BY-NC（Journal of Neuro-Oncology誌、PMC掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は本文で確認した単施設後ろ向き研究の値であり、集団全体の疫学値ではない。原発巣の全身治療は本カードの範囲外。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-D-①（頭蓋骨転移、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-001
  domain: NI
  subdomain: 脳炎
  assertion:
    plain_statement_ja: 単純ヘルペス脳炎は側頭葉を中心とする壊死性脳炎であり、診断には髄液の単純ヘルペスウイルス PCR 検査が用いられ、疑った時点で PCR の結果を待たずにアシクロビルの静脈内投与を直ちに開始する。
    condition:
      population: 脳炎が疑われる成人および小児
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1631
    source: 'Tunkel AR, Glaser CA, Bloch KC, et al. The management of encephalitis: clinical practice guidelines by the Infectious Diseases Society of America. Clin Infect Dis. 2008;47(3):303-327'
    doi: 10.1086/589747
    pmid: '18582201'
    pmcid: null
    url: https://doi.org/10.1086/589747
    source_license: © Infectious Diseases Society of America（Oxford University Press、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: アシクロビルは国内承認薬であり、単純ヘルペス脳炎は国内の保険適用の範囲内である。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-A-①（脳炎、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-002
  domain: NI
  subdomain: 進行性多巣性白質脳症
  assertion:
    plain_statement_ja: 進行性多巣性白質脳症は、HIV 感染症やナタリズマブなどの免疫抑制治療に伴う細胞性免疫不全を背景に JC ウイルスが再活性化して生じる脱髄疾患であり、診断は臨床・画像所見に髄液 PCR での JC ウイルス検出を組み合わせて確立できる。
    condition:
      population: 免疫不全状態にある患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1632
    source: 'Berger JR, Aksamit AJ, Clifford DB, et al. PML diagnostic criteria: consensus statement from the AAN Neuroinfectious Disease Section. Neurology. 2013;80(15):1430-1438'
    doi: 10.1212/WNL.0b013e31828c2fa1
    pmid: '23568998'
    pmcid: null
    url: https://doi.org/10.1212/WNL.0b013e31828c2fa1
    source_license: ライセンス未確認（Neurology 誌、PMC に著者原稿が収載）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 免疫再構築に伴う IRIS（免疫再構築炎症反応症候群）は PML の経過上の重要な論点だが、採用した診断基準論文の抄録には明示がなく、本文での確認を要する。ナタリズマブは国内承認薬（多発性硬化症）である。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-A-③（進行性多巣性白質脳症、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-003
  domain: NI
  subdomain: HIV関連神経認知障害
  assertion:
    plain_statement_ja: HIV 関連神経認知障害は、無症候性神経認知障害、軽度神経認知障害、HIV 関連認知症の 3 段階に分類され、抗レトロウイルス療法の時代にも軽症型が残存する。
    condition:
      population: HIV 感染症患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1633
    source: Antinori A, Arendt G, Becker JT, et al. Updated research nosology for HIV-associated neurocognitive disorders. Neurology. 2007;69(18):1789-1799
    doi: 10.1212/01.WNL.0000287431.88658.8b
    pmid: '17914061'
    pmcid: null
    url: https://doi.org/10.1212/01.WNL.0000287431.88658.8b
    source_license: ライセンス未確認（Neurology 誌、PMC に著者原稿が収載）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本分類は研究用の操作的定義であり、臨床現場では他の認知症原因の除外を前提とする。 抗レトロウイルス薬の個別薬剤の国内承認・保険適用は未確認（本分類そのものは特定の薬剤に依存しない）。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-A-④（AIDS認知症<HIV脳症>、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-004
  domain: NI
  subdomain: HTLV-Ⅰ関連脊髄症
  assertion:
    plain_statement_ja: HTLV-Ⅰ関連脊髄症の診断は、進行性の痙性対麻痺を呈する患者で、血液および脳脊髄液中に抗 HTLV-Ⅰ抗体または HTLV-Ⅰゲノム（プロウイルス）を検出することに基づく。
    condition:
      population: HTLV-Ⅰ感染者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1634
    source: 'Puccioni-Sohler M, Poton AR, Cabral-Castro MJ, et al. Human T Lymphotropic Virus 1-Associated Myelopathy: Overview of Human T Cell Lymphotropic Virus-1/2 Tests and Potential Biomarkers. AIDS Res Hum Retroviruses. 2022;38(12):924-932'
    doi: 10.1089/AID.2022.0028
    pmid: '35819286'
    pmcid: null
    url: https://doi.org/10.1089/AID.2022.0028
    source_license: © Mary Ann Liebert, Inc.（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 国内では HTLV-Ⅰ感染が九州・沖縄を中心とする南日本に多いことは周知だが、今回確認した出典の抄録には国内分布の数値が含まれないため、assertion には含めなかった。国内分布の裏付けは取り込み側で診療ガイドライン等の本文確認を推奨する。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-A-⑤（HTLV-Ⅰ関連脊髄症<HAM>、c）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-005
  domain: NI
  subdomain: プリオン病
  assertion:
    plain_statement_ja: 孤発性 Creutzfeldt-Jakob 病の臨床診断基準には頭部 MRI 所見が組み込まれており、拡散強調画像または FLAIR 画像で大脳皮質の 2 領域以上、または尾状核と被殻の両方に高信号を認めることが診断を支持し、この所見は孤発性 CJD 症例の 83% で陽性となる。
    condition:
      population: 急速進行性認知症の患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1635
    source: Zerr I, Kallenberg K, Summers DM, et al. Updated clinical diagnostic criteria for sporadic Creutzfeldt-Jakob disease. Brain. 2009;132(Pt 10):2659-2668
    doi: 10.1093/brain/awp191
    pmid: '19773352'
    pmcid: null
    url: https://doi.org/10.1093/brain/awp191
    source_license: ライセンス未確認（Brain 誌、PMC に著者原稿が収載）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 髄液 14-3-3 蛋白や脳波の周期性同期性放電は従来の診断基準の要素であり、分子サブタイプにより有用性が異なることが同論文で示されている。数値（83%）は抄録から読み取った。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-B-①（Creutzfeldt-Jakob病、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-006
  domain: NI
  subdomain: プリオン病
  assertion:
    plain_statement_ja: 変異型 Creutzfeldt-Jakob 病は孤発性 CJD と異なり、精神症状で発症して認知機能障害は初期には目立たず、痛みや異常感覚などの感覚障害を早期に呈し、経過が長く、頭部 MRI の T2 強調画像・FLAIR 画像で両側対称性の視床枕高信号（pulvinar sign）を認める。
    condition:
      population: 変異型 CJD が疑われる患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1636
    source: 厚生労働科学研究費補助金難治性疾患政策研究事業「プリオン病及び遅発性ウイルス感染症に関する調査研究班」、厚生労働行政推進調査事業費補助金「プリオン病のサーベイランスと感染予防に関する調査研究班」. プリオン病診療ガイドライン2026. 2026
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 厚生労働省研究班による公的ガイドライン（無償公開。政府標準利用規約の適用は取り込み側で最終確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 変異型 CJD の国内発生はこれまで 1 例のみであり、記載は主に英国症例に基づく WHO 診断基準（2001）・EU 診断基準の紹介である。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-B-①（Creutzfeldt-Jakob病、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-007
  domain: NI
  subdomain: プリオン病
  assertion:
    plain_statement_ja: プリオンは通常の滅菌・消毒に抵抗性を示すため、プリオン病患者のハイリスク手技に用いた手術器具には、十分な洗浄のうえプレバキューム式高圧蒸気滅菌 134℃・18 分間など、通常より強力な専用の不活性化処理が必要である。
    condition:
      population: プリオン病患者・疑い患者に使用した医療器具
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1637
    source: 厚生労働科学研究費補助金「プリオン病及び遅発性ウイルス感染症に関する調査研究班」ほか. プリオン病感染予防ガイドライン2020. 2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 厚生労働省研究班による公的ガイドライン（無償公開。政府標準利用規約の適用は取り込み側で最終確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 滅菌条件は器具の耐熱性や洗浄方法により複数のパターンが示されており、134℃・18 分間はアルカリ洗浄を用いない場合の代表的な条件である。ガイドライン 2020 年版以降の改訂の有無は取り込み側で再確認を推奨する。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-B-①（Creutzfeldt-Jakob病、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-008
  domain: NI
  subdomain: 髄膜炎
  assertion:
    plain_statement_ja: 髄膜炎の髄液所見は、細菌性では好中球優位の細胞数著増・糖低下・蛋白上昇、ウイルス性ではリンパ球優位の細胞増多で糖は正常範囲という型が典型であり、この型の判別が初期対応の出発点になる。
    condition:
      population: 髄膜炎が疑われる患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1638
    source: 日本神経学会・日本神経治療学会・日本神経感染症学会 監修、「細菌性髄膜炎診療ガイドライン」作成委員会 編. 細菌性髄膜炎診療ガイドライン2014. 南江堂. 2014
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本神経学会・日本神経治療学会・日本神経感染症学会（南江堂、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドライン本文（書籍）は未入手のため、記載内容は学会の公開資料および本ガイドラインを引用する公的資料で確認した範囲に限った。取り込み時に本文での最終確認を推奨する。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-A-②（髄膜炎、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-009
  domain: NI
  subdomain: 細菌性髄膜炎
  assertion:
    plain_statement_ja: 日本の細菌性髄膜炎では、起因菌は年齢により異なり、成人では肺炎球菌が中心で薬剤耐性肺炎球菌が問題となるため、経験的治療はカルバペネム系抗菌薬を中心に組み立て、細菌性髄膜炎が強く疑われれば腰椎穿刺・培養の結果を待たずに直ちに開始する。
    condition:
      population: 細菌性髄膜炎の成人患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1638
    source: 日本神経学会・日本神経治療学会・日本神経感染症学会 監修、「細菌性髄膜炎診療ガイドライン」作成委員会 編. 細菌性髄膜炎診療ガイドライン2014. 南江堂. 2014
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本神経学会・日本神経治療学会・日本神経感染症学会（南江堂、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: カルバペネム系抗菌薬（パニペネム、メロペネム等）は国内承認薬であり細菌性髄膜炎は保険適用の範囲内だが、ガイドライン用量が添付文書の承認用量を上回る場合があることが同ガイドライン関係資料で指摘されている。ガイドライン本文（書籍）は未入手のため、取り込み時に本文での最終確認を推奨する。欧州 ESCMID ガイドラインが第 3 世代セフェムを中心とする点で国内の推奨と異なり、地域別の扱いとした。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-C-①（細菌性髄膜炎、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-010
  domain: NI
  subdomain: 細菌性髄膜炎
  assertion:
    plain_statement_ja: 日本の細菌性髄膜炎診療ガイドラインは、新生児を除く乳幼児・学童および成人に対して、デキサメタゾン 0.15 mg/kg を 6 時間ごとに、最初の抗菌薬投与の 10〜20 分前（または同時）に開始する副腎皮質ステロイド薬の併用を推奨する。
    condition:
      population: 新生児を除く細菌性髄膜炎の小児・成人患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1638
    source: 日本神経学会・日本神経治療学会・日本神経感染症学会 監修、「細菌性髄膜炎診療ガイドライン」作成委員会 編. 細菌性髄膜炎診療ガイドライン2014. 南江堂. 2014
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本神経学会・日本神経治療学会・日本神経感染症学会（南江堂、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: デキサメタゾンは国内承認薬だが、細菌性髄膜炎への補助療法としての用法は添付文書の効能・効果に明示されておらず、保険適用の扱いは取り込み側で確認を推奨する。推奨内容は学会公開資料および本ガイドラインを引用する資料で確認した。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-C-①（細菌性髄膜炎、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-011
  domain: NI
  subdomain: 細菌性髄膜炎
  assertion:
    plain_statement_ja: 成人の急性細菌性髄膜炎に対するデキサメタゾン併用（10 mg を 6 時間ごと 4 日間、最初の抗菌薬投与の 15〜20 分前または同時開始）は無作為化比較試験で予後不良のリスクを下げ（相対危険度 0.59）、死亡も減らし（相対危険度 0.48）、効果は肺炎球菌性髄膜炎で最も大きかった（予後不良 26% 対 52%）。
    condition:
      population: 急性細菌性髄膜炎の成人患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1639
    source: de Gans J, van de Beek D; European Dexamethasone in Adulthood Bacterial Meningitis Study Investigators. Dexamethasone in adults with bacterial meningitis. N Engl J Med. 2002;347(20):1549-1556
    doi: 10.1056/NEJMoa021334
    pmid: '12432041'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa021334
    source_license: © Massachusetts Medical Society（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本試験は欧州で実施され、髄膜炎菌性を含む成人例が対象である。低所得国での再現性は限定的とされ、欧州のガイドラインでは高所得国での使用が強く推奨される位置づけである。デキサメタゾンの国内承認・保険適用については NI-010 の uncertainty を参照。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-C-①（細菌性髄膜炎、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-012
  domain: NI
  subdomain: 脳膿瘍
  assertion:
    plain_statement_ja: 脳膿瘍は副鼻腔・中耳・歯などの隣接感染巣からの直接波及、血行性播種、外傷・脳神経外科手術後などの経路で生じ、診断には MRI が推奨され、典型的にはリング状増強と拡散制限を示す病変として描出される。
    condition:
      population: 脳膿瘍が疑われる小児・成人患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1640
    source: Bodilsen J, D'Alessandris QG, Humphreys H, et al. European Society of Clinical Microbiology and Infectious Diseases guidelines on diagnosis and treatment of brain abscess in children and adults. Clin Microbiol Infect. 2024;30(1):66-89
    doi: 10.1016/j.cmi.2023.08.016
    pmid: '37648062'
    pmcid: null
    url: https://doi.org/10.1016/j.cmi.2023.08.016
    source_license: CC BY 4.0（Crossref のライセンス情報で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 拡散制限はリング状増強病変の鑑別（腫瘍との判別）に用いられる所見であり、ガイドライン本文の画像診断の項に基づく。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-C-②（脳膿瘍、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-035 (id: Jlvnlc8)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-013
  domain: NI
  subdomain: 脳膿瘍
  assertion:
    plain_statement_ja: 脳膿瘍の治療では、実施可能な場合は穿刺吸引または摘出が推奨され、市中発症の免疫正常者に対する経験的抗菌薬は第 3 世代セファロスポリンとメトロニダゾールの併用が推奨され、抗菌薬の投与期間は静脈内投与で 6〜8 週間が推奨される。
    condition:
      population: 脳膿瘍の小児・成人患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1640
    source: Bodilsen J, D'Alessandris QG, Humphreys H, et al. European Society of Clinical Microbiology and Infectious Diseases guidelines on diagnosis and treatment of brain abscess in children and adults. Clin Microbiol Infect. 2024;30(1):66-89
    doi: 10.1016/j.cmi.2023.08.016
    pmid: '37648062'
    pmcid: null
    url: https://doi.org/10.1016/j.cmi.2023.08.016
    source_license: CC BY 4.0（Crossref のライセンス情報で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 第 3 世代セファロスポリン、メトロニダゾールはいずれも国内承認薬であり、脳膿瘍への使用は保険適用の範囲内である。重症でない患者では、手術が 24 時間以内に行える場合、穿刺・摘出まで抗菌薬を控える選択肢も同ガイドラインで条件付きで認められている。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-C-②（脳膿瘍、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-035 (id: Jlvnlc8)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-014
  domain: NI
  subdomain: 真菌性髄膜炎
  assertion:
    plain_statement_ja: HIV 関連クリプトコックス髄膜炎の導入療法として、リポソーマルアムホテリシン B 3〜4 mg/kg/日とフルシトシン 25 mg/kg を 1 日 4 回の 2 週間投与、またはリポソーマルアムホテリシン B 10 mg/kg の単回投与に 14 日間のフルシトシンとフルコナゾール 1200 mg/日を組み合わせる方法が推奨され、単回投与レジメンは HIV 関連例でのみ検証されている。
    condition:
      population: HIV 関連クリプトコックス髄膜炎患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1641
    source: 'Chang CC, Harrison TS, Bicanic TA, et al. Global guideline for the diagnosis and management of cryptococcosis: an initiative of the ECMM and ISHAM in cooperation with the ASM. Lancet Infect Dis. 2024;24(8):e495-e512'
    doi: 10.1016/S1473-3099(23)00731-4
    pmid: '38346436'
    pmcid: null
    url: https://doi.org/10.1016/S1473-3099(23)00731-4
    source_license: © Elsevier（The Lancet Infectious Diseases、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: リポソーマルアムホテリシン B、フルシトシン、フルコナゾールはいずれも国内承認薬だが、単回 10 mg/kg 投与などの用法は国内添付文書の用法・用量と異なるため、保険適用の扱いは取り込み側で確認を推奨する。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-C-③（真菌性髄膜炎、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-015
  domain: NI
  subdomain: 真菌性髄膜炎
  assertion:
    plain_statement_ja: 非 HIV のクリプトコックス髄膜炎では、導入療法としてリポソーマルアムホテリシン B 3〜4 mg/kg/日とフルシトシン 25 mg/kg を 1 日 4 回、2 週間以上の投与が推奨され（Cryptococcus gattii 感染症やクリプトコッコーマでは 4〜6 週間への延長を考慮）、その後はフルコナゾールによる 8 週間の地固め療法と 12 か月間の維持療法に移行する。
    condition:
      population: 非 HIV のクリプトコックス髄膜炎患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1641
    source: 'Chang CC, Harrison TS, Bicanic TA, et al. Global guideline for the diagnosis and management of cryptococcosis: an initiative of the ECMM and ISHAM in cooperation with the ASM. Lancet Infect Dis. 2024;24(8):e495-e512'
    doi: 10.1016/S1473-3099(23)00731-4
    pmid: '38346436'
    pmcid: null
    url: https://doi.org/10.1016/S1473-3099(23)00731-4
    source_license: © Elsevier（The Lancet Infectious Diseases、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 抗真菌薬の国内承認状況は NI-014 の uncertainty と同様である。導入期間の延長は患者背景（臓器移植後など）によっても判断される。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-C-③（真菌性髄膜炎、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-016
  domain: NI
  subdomain: 結核性髄膜炎
  assertion:
    plain_statement_ja: 結核性髄膜炎は 5 日を超える亜急性の経過をとることが診断の手がかりとなり、その統一症例定義では髄液のリンパ球優位の細胞増多、蛋白上昇、糖低下（髄液・血漿糖比の低下）などの所見を臨床像や画像所見と組み合わせて診断を階層化する。
    condition:
      population: 結核性髄膜炎が疑われる小児・成人患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1642
    source: 'Marais S, Thwaites G, Schoeman JF, et al. Tuberculous meningitis: a uniform case definition for use in clinical research. Lancet Infect Dis. 2010;10(11):803-812'
    doi: 10.1016/S1473-3099(10)70138-9
    pmid: '20822958'
    pmcid: null
    url: https://doi.org/10.1016/S1473-3099(10)70138-9
    source_license: © Elsevier（The Lancet Infectious Diseases、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 髄液 ADA（アデノシンデアミナーゼ）は結核性髄膜炎の補助診断として臨床で用いられるが、本統一症例定義の診断要素には含まれておらず、カットオフ値の裏付けには別途一次資料が必要なため assertion には含めなかった。本定義は研究用の症例定義であり、臨床診断では抗酸菌検査・培養や核酸増幅検査と合わせて判断する。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-C-④（結核性髄膜炎、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-017
  domain: NI
  subdomain: 結核性髄膜炎
  assertion:
    plain_statement_ja: 結核性髄膜炎に対するデキサメタゾンの併用は、14 歳超の患者を対象とした無作為化比較試験で死亡のリスクを下げた（相対危険度 0.69）が、生存者における重度障害の割合は有意には減らさなかった。
    condition:
      population: 結核性髄膜炎の青年・成人患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1643
    source: Thwaites GE, Nguyen DB, Nguyen HD, et al. Dexamethasone for the treatment of tuberculous meningitis in adolescents and adults. N Engl J Med. 2004;351(17):1741-1751
    doi: 10.1056/NEJMoa040573
    pmid: '15496623'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa040573
    source_license: © Massachusetts Medical Society（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本試験はベトナムで実施され、HIV 合併例を含む。抗結核薬（イソニアジド、リファンピシン等）はいずれも国内承認薬であり、結核性髄膜炎は保険適用の範囲内である。デキサメタゾンの位置づけは NI-010 の uncertainty と同様である。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-C-④（結核性髄膜炎、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-018
  domain: NI
  subdomain: 急性散在性脳脊髄炎
  assertion:
    plain_statement_ja: 急性散在性脳脊髄炎は、感染やワクチン接種に続いて生じる単相性の免疫介在性脱髄疾患であり、小児の診断定義では多巣性の神経症候に脳症を伴うことが要件とされる。
    condition:
      population: 小児患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1644
    source: 'Krupp LB, Tardieu M, Amato MP, et al. International Pediatric Multiple Sclerosis Study Group criteria for pediatric multiple sclerosis and immune-mediated central nervous system demyelinating disorders: revisions to the 2007 definitions. Mult Scler. 2013;19(10):1261-1267'
    doi: 10.1177/1352458513484547
    pmid: '23572237'
    pmcid: null
    url: https://doi.org/10.1177/1352458513484547
    source_license: © SAGE Publishing（Multiple Sclerosis、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 治療の第一選択とされる高用量ステロイドパルス療法は、採用した出典（診断定義の論文）の扱う範囲外であり、assertion には含めなかった。治療の裏付けには別途一次資料を要する。ステロイド製剤はいずれも国内承認薬である。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-D-①（急性散在性脳脊髄炎、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-019
  domain: NI
  subdomain: 急性小脳性失調症
  assertion:
    plain_statement_ja: 小児の感染後急性小脳症候群のうち急性小脳性失調症が最も多く（全国症例集積で 70%）、原因としては水痘が歴史的に最多とされ、大規模コホートでは最大で症例の 25% を占めた。
    condition:
      population: 小児患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1645
    source: 'Gunaratna GPS, Mohammad SS, Blyth CC, et al. Postinfectious Acute Cerebellar Syndromes in Children: A Nationally Ascertained Case Series From Australia 2013-2018. J Child Neurol. 2022 (online ahead of print)'
    doi: 10.1177/08830738221093209
    pmid: '35546546'
    pmcid: null
    url: https://doi.org/10.1177/08830738221093209
    source_license: © SAGE Publishing（Journal of Child Neurology、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 同集積（水痘ワクチン高接種率の集団）では水痘関連例は認められず、頻度はワクチン接種状況により大きく異なる。数値は抄録から読み取った。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-D-②（急性小脳性失調症、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-020
  domain: NI
  subdomain: 化膿性脊椎炎
  assertion:
    plain_statement_ja: 成人の化膿性脊椎炎（自然発症の椎体骨髄炎）では黄色ブドウ球菌が最も多い起因菌であり、診断には MRI が最も感度の高い画像検査とされ、血液培養と画像ガイド下生検による起因菌の同定が推奨される。
    condition:
      population: 成人の化膿性脊椎炎患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1646
    source: Berbari EF, Kanj SS, Kowalski TJ, et al. 2015 Infectious Diseases Society of America (IDSA) Clinical Practice Guidelines for the Diagnosis and Treatment of Native Vertebral Osteomyelitis in Adults. Clin Infect Dis. 2015;61(6):e26-e46
    doi: 10.1093/cid/civ482
    pmid: '26229122'
    pmcid: null
    url: https://doi.org/10.1093/cid/civ482
    source_license: © Infectious Diseases Society of America（Oxford University Press、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 血液培養が陽性で画像所見が典型的な場合は生検を省略できる場合があるなど、適用には条件がある。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-E-①（化膿性脊椎炎、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-131 (id: JlvnlqY)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-021
  domain: NI
  subdomain: 化膿性脊椎炎
  assertion:
    plain_statement_ja: 成人の化膿性脊椎炎に対する抗菌薬治療は、起因菌に感受性のある薬剤による 6 週間の投与が標準とされる。
    condition:
      population: 成人の化膿性脊椎炎患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1646
    source: Berbari EF, Kanj SS, Kowalski TJ, et al. 2015 Infectious Diseases Society of America (IDSA) Clinical Practice Guidelines for the Diagnosis and Treatment of Native Vertebral Osteomyelitis in Adults. Clin Infect Dis. 2015;61(6):e26-e46
    doi: 10.1093/cid/civ482
    pmid: '26229122'
    pmcid: null
    url: https://doi.org/10.1093/cid/civ482
    source_license: © Infectious Diseases Society of America（Oxford University Press、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 使用する抗菌薬はいずれも国内承認薬の範囲で選択され、骨・関節感染症への使用は保険適用の範囲内である。膿瘍合併例や起因菌により期間は延長されることがある。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-E-①（化膿性脊椎炎、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-131 (id: JlvnlqY)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-022
  domain: NI
  subdomain: 結核性骨関節炎
  assertion:
    plain_statement_ja: 結核性脊椎炎（脊椎カリエス、Pott 病）は結核菌の血行性播種により椎体前部を侵す脊椎外結核であり、治療の基盤は多剤併用抗結核化学療法で、手術は高度の後弯や神経障害を呈する例に限られる。
    condition:
      population: 脊椎結核の患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1647
    source: Leowattana W, Leowattana P, Leowattana T. Tuberculosis of the spine. World J Orthop. 2023;14(5):275-293
    doi: 10.5312/wjo.v14.i5.275
    pmid: '37304201'
    pmcid: null
    url: https://doi.org/10.5312/wjo.v14.i5.275
    source_license: ライセンス未確認（World Journal of Orthopedics、Crossref にライセンス登録なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードは脊椎病変を中心とした記載であり、脊椎以外の結核性骨関節炎（股関節・膝関節など）も同じ多剤併用化学療法が基盤となる。抗結核薬はいずれも国内承認薬であり保険適用の範囲内である。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-E-②（結核性骨関節炎、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-131 (id: JlvnlqY)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-023
  domain: NI
  subdomain: 化膿性骨髄炎
  assertion:
    plain_statement_ja: 小児の急性血行性骨髄炎では黄色ブドウ球菌を念頭に置いた経験的抗菌薬治療が適応となり、抗菌薬の投与期間は通常 4 週間が標準とされる。
    condition:
      population: 小児の急性血行性骨髄炎患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1648
    source: Hatzenbuehler J, Pulling TJ. Diagnosis and management of osteomyelitis. Am Fam Physician. 2011;84(9):1027-1033
    doi: null
    pmid: '22046943'
    pmcid: null
    url: null
    source_license: © American Academy of Family Physicians（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 使用する抗菌薬はいずれも国内承認薬の範囲で選択され、保険適用の範囲内である。MRSA の頻度により経験的治療の選択は地域で異なる。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-E-③（化膿性骨髄炎、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-130 (id: JlvnlqU)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-024
  domain: NI
  subdomain: 化膿性骨髄炎
  assertion:
    plain_statement_ja: 慢性骨髄炎では壊死した骨（腐骨）が感染の温床となるため外科的デブリドマンが通常必要であり、手術と長期の抗菌薬治療を行っても再発率は高い。
    condition:
      population: 慢性骨髄炎患者（糖尿病・末梢血管障害を背景とする例が多い）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1648
    source: Hatzenbuehler J, Pulling TJ. Diagnosis and management of osteomyelitis. Am Fam Physician. 2011;84(9):1027-1033
    doi: null
    pmid: '22046943'
    pmcid: null
    url: null
    source_license: © American Academy of Family Physicians（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 成人の慢性骨髄炎の抗菌薬期間は急性例より数週間長くなると同総説に記載されている。具体的な期間は感染巣の範囲と起因菌により個別化される。 個別の抗菌薬の国内承認・保険適用は未確認。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-E-③（化膿性骨髄炎、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-130 (id: JlvnlqU)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-025
  domain: NI
  subdomain: 化膿性関節炎
  assertion:
    plain_statement_ja: 化膿性関節炎は、急性の非外傷性の関節痛・腫脹・発熱を呈する患者では直ちに鑑別に挙げるべき緊急疾患であり、診断には関節穿刺による関節液検査が必須で、関節液を採取した後に経験的抗菌薬を開始し、起因菌は黄色ブドウ球菌が最も多く、治療期間は通常 2〜6 週間である。
    condition:
      population: 急性単関節炎の患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1649
    source: 'Earwood JS, Walker TR, Sue GJC. Septic Arthritis: Diagnosis and Treatment. Am Fam Physician. 2021;104(6):589-597'
    doi: null
    pmid: '34913662'
    pmcid: null
    url: null
    source_license: © American Academy of Family Physicians（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 使用する抗菌薬はいずれも国内承認薬の範囲で選択され、保険適用の範囲内である。淋菌性関節炎など起因菌により治療が異なるため、病歴と関節液のグラム染色が初期選択の手がかりになる。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-E-④（化膿性関節炎、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-129 (id: JlvnlqM)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-026
  domain: NI
  subdomain: 亜急性硬化性全脳炎
  assertion:
    plain_statement_ja: 亜急性硬化性全脳炎は麻疹ウイルス感染後に生じる慢性脳炎であり、発症は麻疹罹患から平均 6 年後で、精神症状に続いてミオクローヌスが出現し、診断は脳波の周期性複合波と麻疹感染の免疫学的証拠により支持され、95% が 5 年以内に死亡する予後不良な疾患である。
    condition:
      population: 麻疹罹患歴のある小児・若年者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1650
    source: 'Gutierrez J, Issacson RS, Koppel BS. Subacute sclerosing panencephalitis: an update. Dev Med Child Neurol. 2010;52(10):901-907'
    doi: 10.1111/j.1469-8749.2010.03717.x
    pmid: '20561004'
    pmcid: null
    url: https://doi.org/10.1111/j.1469-8749.2010.03717.x
    source_license: © Wiley（Developmental Medicine & Child Neurology、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 発症頻度は麻疹ワクチンの接種率に左右され、接種が普及した地域では稀である。インターフェロンやリバビリン等の治療は確立したものではなく、同総説でも試験的治療として扱われている。
  curriculum:
    kokushi: 医学各論 Ⅸ-11-E-②（亜急性硬化性全脳炎<SSPE>、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-027
  domain: NI
  subdomain: 自己免疫性脳炎
  assertion:
    plain_statement_ja: 自己免疫性脳炎は、抗体検査の結果を待たずに臨床症候群から診断を進めるアプローチが推奨され、possible autoimmune encephalitis は、3 か月未満の亜急性の経過で作業記憶障害（短期記憶障害）・精神状態の変化・精神症状のいずれかが現れ、新規の局所神経所見、けいれん、髄液細胞増多（5 個/mm³超）、脳炎を示唆する MRI 所見のうち少なくとも 1 つを伴い、他の原因が合理的に除外できる場合に診断でき、早期の免疫療法開始につなげる。
    condition:
      population: 脳炎が疑われる患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1625
    source: Graus F, Titulaer MJ, Balu R, et al. A clinical approach to diagnosis of autoimmune encephalitis. Lancet Neurol. 2016;15(4):391-404
    doi: 10.1016/S1474-4422(15)00401-9
    pmid: '26906964'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(15)00401-9
    source_license: © Elsevier Ltd（Lancet Neurology、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本基準は専門家コンセンサスに基づく操作的基準であり、確定診断には自己抗体の検出等が別途必要となる。免疫療法の内容は NI-029 を参照。 免疫療法に用いる薬剤の国内承認・保険適用の確認状況は NI-029 に記載した。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-A-①（脳炎、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-028
  domain: NI
  subdomain: 抗NMDA受容体脳炎
  assertion:
    plain_statement_ja: 抗 NMDA 受容体脳炎は若年者に多く、18 歳以上では女性が男性の約 4 倍を占め、18 歳以上の女性では腫瘍の合併が約 58% にみられその多くは卵巣奇形腫であり、臨床経過は精神症状（異常行動、妄想・幻覚などの精神病症状、興奮、カタトニア、不眠）で始まり、言語障害、ジスキネジア、記憶障害、自律神経不安定、意識レベル低下へと進行し、けいれんは経過のどの時期にも起こりうる。
    condition:
      population: 抗 NMDA 受容体脳炎患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1625
    source: Graus F, Titulaer MJ, Balu R, et al. A clinical approach to diagnosis of autoimmune encephalitis. Lancet Neurol. 2016;15(4):391-404
    doi: 10.1016/S1474-4422(15)00401-9
    pmid: '26906964'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(15)00401-9
    source_license: © Elsevier Ltd（Lancet Neurology、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 腫瘍合併率は年齢・性別で大きく異なり、12 歳未満の小児では 0〜5% と低い。数値は出典本文で確認した。治療は NI-029 を参照。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-A-①（脳炎、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: NI-029
  domain: NI
  subdomain: 自己免疫性脳炎
  assertion:
    plain_statement_ja: 抗体介在性脳炎の治療は、副腎皮質ステロイド・免疫グロブリン静注療法・血漿交換による第一選択免疫療法と、腫瘍がある場合の腫瘍摘出が基本であり、抗 NMDA 受容体脳炎の観察コホート（577 例）では第一選択免疫療法または腫瘍摘出により 53% が 4 週以内に改善し、第一選択で改善しない例へのリツキシマブやシクロホスファミドによる第二選択免疫療法は良好な転帰と関連し、治療開始が早いことが転帰良好の予測因子であった。
    condition:
      population: 抗体介在性脳炎（抗 NMDA 受容体脳炎）患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1626
    source: 'Titulaer MJ, McCracken L, Gabilondo I, et al. Treatment and prognostic factors for long-term outcome in patients with anti-NMDA receptor encephalitis: an observational cohort study. Lancet Neurol. 2013;12(2):157-165'
    doi: 10.1016/S1474-4422(12)70310-1
    pmid: '23290630'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(12)70310-1
    source_license: © Elsevier Ltd（Lancet Neurology、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。ステロイド、免疫グロブリン製剤、リツキシマブ、シクロホスファミドはいずれも国内承認薬だが、自己免疫性脳炎に対する適応・保険適用は薬剤ごとに異なり、リツキシマブ等の本疾患への保険適用は本カードでは未確認である。血漿交換の保険適用も疾患ごとに定められており、個別の確認を要する。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-A-①（脳炎、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応の一覧

| カードID | 出題基準 | コアカリ |
|---|---|---|
| ST-001 | 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA) |
| ST-002 | 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA) |
| ST-003 | 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA) |
| ST-004 | 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA) |
| ST-005 | 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA) |
| ST-006 | 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA) |
| ST-007 | 医学各論 Ⅸ-1-A-①（高血圧性脳出血、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA) |
| ST-008 | 医学各論 Ⅸ-1-A-②（アミロイドアンギオパチー、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA) |
| ST-009 | 医学各論 Ⅸ-1-A-②（アミロイドアンギオパチー、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA) |
| ST-010 | 医学各論 Ⅸ-1-A-②（アミロイドアンギオパチー、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-026 (id: JlvnlcA) |
| ST-011 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE) |
| ST-012 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE) |
| ST-013 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE) |
| ST-014 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE) |
| ST-015 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)；TBL-01-00-030 (id: Jlvnlcg) |
| ST-016 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE) |
| ST-017 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE) |
| ST-018 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE) |
| ST-019 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE) |
| ST-020 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)；TBL-01-00-030 (id: Jlvnlcg) |
| ST-021 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)；TBL-01-00-030 (id: Jlvnlcg) |
| ST-022 | 医学各論 Ⅸ-1-B-①（脳動脈瘤、解離性脳動脈瘤、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-027 (id: JlvnlcE)；TBL-01-00-030 (id: Jlvnlcg) |
| ST-023 | 医学各論 Ⅸ-1-C-①（心原性脳塞栓症、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-024 | 医学各論 Ⅸ-1-C-①（心原性脳塞栓症、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-025 | 医学各論 Ⅸ-1-C-①（心原性脳塞栓症、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-026 | 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-027 | 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-028 | 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-029 | 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-030 | 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-031 | 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-032 | 医学各論 Ⅸ-1-C-②（アテローム血栓性脳梗塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-033 | 医学各論 Ⅸ-1-C-③（ラクナ梗塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-034 | 医学各論 Ⅸ-1-C-③（ラクナ梗塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-035 | 医学各論 Ⅸ-1-C-④（一過性脳虚血発作、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-029 (id: JlvnlcY) |
| ST-036 | 医学各論 Ⅸ-1-C-④（一過性脳虚血発作、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-029 (id: JlvnlcY) |
| ST-037 | 医学各論 Ⅸ-1-C-④（一過性脳虚血発作、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-029 (id: JlvnlcY) |
| ST-038 | 医学各論 Ⅸ-1-C-⑤（脳動脈狭窄・閉塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-039 | 医学各論 Ⅸ-1-C-⑤（脳動脈狭窄・閉塞、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-040 | 医学各論 Ⅸ-1-D-①（脳動脈解離、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-041 | 医学各論 Ⅸ-1-D-①（脳動脈解離、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-042 | 医学各論 Ⅸ-1-D-②（脳動静脈奇形、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-031 (id: Jlvnlck) |
| ST-043 | 医学各論 Ⅸ-1-D-②（脳動静脈奇形、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-031 (id: Jlvnlck) |
| ST-044 | 医学各論 Ⅸ-1-D-③（静脈洞血栓症、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-045 | 医学各論 Ⅸ-1-D-③（静脈洞血栓症、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-046 | 医学各論 Ⅸ-1-D-④（もやもや病、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-032 (id: Jlvnlcs) |
| ST-047 | 医学各論 Ⅸ-1-D-④（もやもや病、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-032 (id: Jlvnlcs) |
| ST-048 | 医学各論 Ⅸ-1-D-⑤（硬膜動静脈瘻、c） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-049 | 医学各論 Ⅸ-1-E-①（偽性球麻痺、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ST-050 | 医学各論 Ⅸ-1-E-②（廃用性萎縮、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| BT-001 | 医学各論 Ⅸ-2-A-①（神経膠腫、a） | PS-02-03-05 (id: JkxnuP0) |
| BT-002 | 医学各論 Ⅸ-2-A-①（神経膠腫、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-630 (id: Jlvnma4) |
| BT-003 | 医学各論 Ⅸ-2-A-①（神経膠腫、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-630 (id: Jlvnma4) |
| BT-004 | 医学各論 Ⅸ-2-A-①（神経膠腫、a） | PS-02-03-05 (id: JkxnuP0) |
| BT-005 | 医学各論 Ⅸ-2-A-②（悪性リンパ腫、b） | PS-02-03-05 (id: JkxnuP0) |
| BT-006 | 医学各論 Ⅸ-2-A-②（悪性リンパ腫、b） | PS-02-03-05 (id: JkxnuP0) |
| BT-007 | 医学各論 Ⅸ-2-A-②（悪性リンパ腫、b） | PS-02-03-05 (id: JkxnuP0) |
| BT-008 | 医学各論 Ⅸ-2-A-③（胚細胞腫瘍、c） | PS-02-03-05 (id: JkxnuP0) |
| BT-009 | 医学各論 Ⅸ-2-A-③（胚細胞腫瘍、c） | PS-02-03-05 (id: JkxnuP0) |
| BT-010 | 医学各論 Ⅸ-2-A-③（胚細胞腫瘍、c） | PS-02-03-05 (id: JkxnuP0) |
| BT-011 | 医学各論 Ⅸ-2-A-④（血管芽腫、c） | PS-02-03-05 (id: JkxnuP0) |
| BT-012 | 医学各論 Ⅸ-2-B-①（髄膜腫、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-631 (id: Jlvnma8) |
| BT-013 | 医学各論 Ⅸ-2-B-②（下垂体腫瘍(下垂体腺腫)、b） | PS-02-03-05 (id: JkxnuP0) |
| BT-014 | 医学各論 Ⅸ-2-B-②（下垂体腫瘍(下垂体腺腫)、b） | PS-02-03-05 (id: JkxnuP0) |
| BT-015 | 医学各論 Ⅸ-2-B-③（神経鞘腫、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-632 (id: JlvnmbE) |
| BT-016 | 医学各論 Ⅸ-2-B-④（頭蓋咽頭腫、c） | PS-02-03-05 (id: JkxnuP0) |
| BT-017 | 医学各論 Ⅸ-2-C-①（転移性脳腫瘍、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-633 (id: JlvnmbI) |
| BT-018 | 医学各論 Ⅸ-2-C-②（髄膜癌腫症<癌性髄膜炎>、c） | PS-02-03-05 (id: JkxnuP0) |
| BT-019 | 医学各論 Ⅸ-2-D-①（頭蓋骨転移、c） | PS-02-03-05 (id: JkxnuP0) |
| NI-001 | 医学各論 Ⅸ-3-A-①（脳炎、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-002 | 医学各論 Ⅸ-3-A-③（進行性多巣性白質脳症、c） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-003 | 医学各論 Ⅸ-3-A-④（AIDS認知症<HIV脳症>、c） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-004 | 医学各論 Ⅸ-3-A-⑤（HTLV-Ⅰ関連脊髄症<HAM>、c） | PS-02-03-05 (id: JkxnuP0) |
| NI-005 | 医学各論 Ⅸ-3-B-①（Creutzfeldt-Jakob病、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-006 | 医学各論 Ⅸ-3-B-①（Creutzfeldt-Jakob病、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-007 | 医学各論 Ⅸ-3-B-①（Creutzfeldt-Jakob病、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-008 | 医学各論 Ⅸ-3-A-②（髄膜炎、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-009 | 医学各論 Ⅸ-3-C-①（細菌性髄膜炎、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-010 | 医学各論 Ⅸ-3-C-①（細菌性髄膜炎、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-011 | 医学各論 Ⅸ-3-C-①（細菌性髄膜炎、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-012 | 医学各論 Ⅸ-3-C-②（脳膿瘍、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-035 (id: Jlvnlc8) |
| NI-013 | 医学各論 Ⅸ-3-C-②（脳膿瘍、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-035 (id: Jlvnlc8) |
| NI-014 | 医学各論 Ⅸ-3-C-③（真菌性髄膜炎、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-015 | 医学各論 Ⅸ-3-C-③（真菌性髄膜炎、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-016 | 医学各論 Ⅸ-3-C-④（結核性髄膜炎、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-017 | 医学各論 Ⅸ-3-C-④（結核性髄膜炎、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-018 | 医学各論 Ⅸ-3-D-①（急性散在性脳脊髄炎、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-019 | 医学各論 Ⅸ-3-D-②（急性小脳性失調症、b） | PS-02-03-05 (id: JkxnuP0) |
| NI-020 | 医学各論 Ⅸ-3-E-①（化膿性脊椎炎、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-131 (id: JlvnlqY) |
| NI-021 | 医学各論 Ⅸ-3-E-①（化膿性脊椎炎、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-131 (id: JlvnlqY) |
| NI-022 | 医学各論 Ⅸ-3-E-②（結核性骨関節炎、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-131 (id: JlvnlqY) |
| NI-023 | 医学各論 Ⅸ-3-E-③（化膿性骨髄炎、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-130 (id: JlvnlqU) |
| NI-024 | 医学各論 Ⅸ-3-E-③（化膿性骨髄炎、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-130 (id: JlvnlqU) |
| NI-025 | 医学各論 Ⅸ-3-E-④（化膿性関節炎、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-129 (id: JlvnlqM) |
| NI-026 | 医学各論 Ⅸ-11-E-②（亜急性硬化性全脳炎<SSPE>、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-027 | 医学各論 Ⅸ-3-A-①（脳炎、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-028 | 医学各論 Ⅸ-3-A-①（脳炎、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| NI-029 | 医学各論 Ⅸ-3-A-①（脳炎、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |

## 4. 未解決事項

- 脳卒中治療ガイドラインは依頼文の指定どおり 2021〔改訂2023〕を出典としたが、2025年に改訂2025が公開されている。関連推奨（脳出血の降圧目標、攣縮治療薬など）が維持されていることは公開情報で確認し ST-005 の uncertainty に記載した。最新版との最終照合は取り込み側に残る。
- BT の薬剤カード（テモゾロミド、メトトレキサート、リツキシマブ等）は、国内承認・保険適用の個別確認を「未実施」と uncertainty に明記したものがある（取り込み時の確認課題）。
- RESPECT-CVT のダビガトランについて、脳静脈血栓症への個別の保険適用確認は未実施（ST 側カードの uncertainty に明記）。
- BT-016 頭蓋咽頭腫の「石灰化」、BT-017 転移性脳腫瘍の原発巣割合の数値は、採用出典の抄録で確認できなかったため命題に入れていない（補完候補として各カードの uncertainty に記載）。
- 細菌性髄膜炎診療ガイドライン2014は書籍本文を入手できなかったため、推奨内容は学会公開資料・引用資料で確認できた範囲に限定した（NI-008〜010 の uncertainty に明記）。
- 件数が目標（60〜90件）を上回る98件になった。理由は、ニモジピン（欧州・米国・日本の3地域）と rt-PA 用量（日本・米国）などの地域別カードと、レベル a 項目の複数カード化である。

## 5. 次回への引き継ぎ

- 欠番: なし。ST・BT・NI の3接頭辞とも連番でそろっている。
- カードのない小項目: なし（対象43項目すべてにカードあり）。Ⅸ-1-E-③ 脳血管性認知症は境界どおり第29回 ND（Ⅸ-4-A-②）で作る。
- 未使用の SRC: SRC-1573〜1580、SRC-1608〜1610、SRC-1627〜1630（本回の範囲内。次回は第29回の範囲 SRC-1651 から使う）。
- 既存出典の再利用: SRC-874（頭蓋咽頭腫)、SRC-877（下垂体腺腫)、SRC-884（下垂体卒中 UK ガイドライン）は第20回の番号をそのまま使った。
- 第29回は ND・EP。脳血管性認知症（ND)、欠神発作は EP の Ⅸ-6-A-② として作り Ⅸ-11-C-② では作らない。
