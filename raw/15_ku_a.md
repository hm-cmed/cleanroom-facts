# 腎・泌尿器・生殖器 第15回：糸球体疾患（GN-001〜040）と腎血管・尿細管・間質疾患（KT-001〜028）

- 作成日：2026-10-28
- 事実票：68件（GN 40件、KT 28件）。目標の60〜90件の範囲内。ID は接頭辞ごとに 001 からの連番で、欠番はない。全件 `status: draft`、`verifier: null`。
- カバー：出題基準の対象項目43件のうち42件にカードがある（残る Ⅷ-1-D-③ 全身性強皮症は、同じ疾患を扱う KT-006（Ⅷ-2-A-⑥、強皮症腎クリーゼ）でカバーした）。レベル a の小項目13件（GN 10件、KT 3件）はすべて1件以上ある。
- 出典マスター：新規 SRC-571〜630 のうち 59件を使用（未使用は SRC-588 のみ）。同じガイドライン等を複数カードで使う場合は同じ SRC を再利用した（例：KDIGO 2021 糸球体疾患ガイドライン＝SRC-571 を4件、KDIGO 2024 ループス腎炎ガイドラインを3件、間質性腎炎の総説を3件）。
- 第14回の試行で指摘された点への対応：論文の出典は全59件とも DOI と PMID の両方を記載した（照合できなかったものはなし）。`condition.region` は全68件に記載。薬の名前が出るカードは uncertainty に国内の承認・保険適用の確認状況を記載した（確認済みは GN-018 のリツキシマブのみで、他は「未確認」と明記）。ライセンスは CC BY を確認できたものを OPEN とした（UNKNOWN は9件）。
- 検証（こちらで実施済み）：YAML の構文解析を通過。スキーマ検証は、手元のスキーマに未追加の接頭辞 GN・KT を検証用に加えた条件でエラー0（接頭辞の追加自体は取り込み側の作業として引き継ぎに記載）。全59件の DOI が Crossref で解決し題名が一致すること、DOI→PMID の対応に不一致がないことを確認した。
- 取り込み想定：YAML ブロックは1つで、アンカー・マージキー・脚注番号・`basis_tag`・仮IDは使っていない。主張文はすべて自作文である（legal_basis はすべて B）。
- 既存カードは書き換えていない。ほかの分野との境界は依頼文 1-1 に従い、腎血管性高血圧は腎の側に、血管炎・SLE・強皮症・IgG4関連疾患・骨髄腫は腎病変に絞った。

## 1. 抽出元ホワイトリスト（出典マスター、新規 SRC）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 使用カード |
|---|---|---|---|---|---|---|---|
| SRC-571 | Kidney Disease: Improving Global Outcomes (KDIGO) Glomerular Diseases Work Group. KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases. Kidney Int. 2021;100(4S):S1-S276 | 10.1016/j.kint.2021.05.021 | 34556256 | 出版社の著作物（CC の表示なし） | RESTRICTED | PubMed レコードで書誌・DOI・PMID を確認し、NCBI の ID 変換でも照合。対象疾患の範囲は Executive summary の抄録で確認 | GN-004, GN-005, GN-011, GN-014 |
| SRC-572 | Barocas DA, Lotan Y, Matulewicz RS, Raman JD, Westerman ME, Kirkby E, Pak L, Souter L. Updates to Microhematuria: AUA/SUFU Guideline (2025). J Urol. 2025;213(5):547-557 | 10.1097/JU.0000000000004490 | 40013563 | 出版社（AUA）の著作物（CC の表示なし） | RESTRICTED | 書誌・DOI・PMID を PubMed 引用情報で確認。定義とリスク層別の内容は 2025 年改訂の要約資料で確認（数値はガイドラインの表に基づく） | GN-001 |
| SRC-573 | Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int. 2024;105(4S):S117-S314 | 10.1016/j.kint.2023.10.018 | 38490803 | 出版社の著作物（CC の表示なし） | RESTRICTED | 書誌・DOI・PMID を引用情報で確認。アルブミン尿区分（A1〜A3）の範囲はガイドラインの表を転記した解説論文の表で確認 | GN-002 |
| SRC-574 | Rodriguez-Iturbe B, Musser JM. The current state of poststreptococcal glomerulonephritis. J Am Soc Nephrol. 2008;19(10):1855-1864 | 10.1681/ASN.2008010092 | 18667731 | ライセンス表示を確認できず（CC の表示なし） | UNKNOWN | DOI は引用文献情報で確認。長期予後の数値は本文テキスト（NCBI Bookshelf 収載分）で確認。PMID は NCBI の ID 検索で照合 | GN-003 |
| SRC-575 | Walsh M, Merkel PA, Peh CA, Szpirt W, Puéchal X, Fujimoto S, et al. Plasma Exchange and Glucocorticoids in Severe ANCA-Associated Vasculitis. N Engl J Med. 2020;382(7):622-631 | 10.1056/NEJMoa1803537 | 32053298 | 出版社の著作物（CC の表示なし） | RESTRICTED | 抄録で主要評価項目の数値を確認し、DOI・PMID・PMCID（PMC7325726）を NCBI の ID 変換で照合 | GN-006 |
| SRC-576 | Wyatt RJ, Julian BA. IgA nephropathy. N Engl J Med. 2013;368(25):2402-2414 | 10.1056/NEJMra1206793 | 23782179 | 出版社の著作物（CC の表示なし） | RESTRICTED | 本文テキストで IgA 沈着・補体の所見を確認し、DOI・PMID を引用情報で照合 | GN-007 |
| SRC-577 | Lv J, Wong MG, Hladunewich MA, Jha V, Hooi LS, Monaghan H, et al. Effect of Oral Methylprednisolone on Decline in Kidney Function or Kidney Failure in Patients With IgA Nephropathy: The TESTING Randomized Clinical Trial. JAMA. 2022;327(19):1888-1898 | 10.1001/jama.2022.5368 | 35579642 | 出版社の著作物（PMC 掲載ページにも CC の表示なし） | RESTRICTED | PubMed 抄録で主要評価項目・重篤な有害事象の数値を確認し、DOI・PMID・PMCID（PMC9115617）を NCBI の ID 変換で照合 | GN-008 |
| SRC-578 | Trimarchi H, Barratt J, Cattran DC, Cook HT, Coppo R, Haas M, et al. Oxford Classification of IgA nephropathy 2016: an update from the IgA Nephropathy Classification Working Group. Kidney Int. 2017;91(5):1014-1021 | 10.1016/j.kint.2017.02.003 | 28341274 | 出版社の著作物（CC の表示なし） | RESTRICTED | PubMed 抄録で MEST-C の内容（糸球体8個以上、M・S・T の予後予測、C の追加）を確認し、DOI・PMID を照合 | GN-009 |
| SRC-579 | Nishi S, Ubara Y, Utsunomiya Y, Okada K, Obata Y, Kai H, et al. Evidence-based clinical practice guidelines for nephrotic syndrome 2014. Clin Exp Nephrol. 2016;20(3):342-370 | 10.1007/s10157-015-1216-x | 27099136 | CC BY 4.0（PMC ページの Open Access 表示で確認） | OPEN | PMC 全文で定義の表（尿蛋白≧3.5 g/日、血清アルブミン≦3.0 g/dL）と治療効果判定の表を確認し、DOI・PMID・PMCID（PMC4891386）を照合 | GN-010 |
| SRC-580 | Maas RJ, Deegens JK, Beukhof JR, Reichert LJ, Ten Dam MA, Beutler JJ, et al. The clinical course of minimal change nephrotic syndrome with onset in adulthood or late adolescence: a case series. Am J Kidney Dis. 2017;69(5):637-646 | 10.1053/j.ajkd.2016.10.032 | 28089478 | ライセンス表示を確認できず（CC の表示なし） | UNKNOWN | 抄録で症例数・寛解率・再発率・合併症の数値を確認。DOI は引用情報、PMID は NCBI の ID 検索で照合 | GN-012 |
| SRC-581 | D'Agati VD, Fogo AB, Bruijn JA, Jennette JC. Pathologic classification of focal segmental glomerulosclerosis: a working proposal. Am J Kidney Dis. 2004;43(2):368-382 | 10.1053/j.ajkd.2003.10.024 | 14750104 | ライセンス表示を確認できず（CC の表示なし） | UNKNOWN | 5つの病理亜型（虚脱型・tip型・細胞型・傍糸球体門型・NOS）は総説の引用で確認。DOI は引用情報、PMID は NCBI の ID 検索で照合 | GN-013 |
| SRC-582 | Beck LH Jr, Bonegio RGB, Lambeau G, Beck DM, Powell DW, Cummins TD, et al. M-type phospholipase A2 receptor as target antigen in idiopathic membranous nephropathy. N Engl J Med. 2009;361(1):11-21 | 10.1056/NEJMoa0810457 | 19571279 | 出版社の著作物（CC の表示なし） | RESTRICTED | PubMed 抄録で抗 PLA2R 抗体の陽性割合（26/37、70%）を確認し、DOI・PMID・PMCID（PMC2762083）を NCBI の ID 変換で照合 | GN-015 |
| SRC-583 | Fervenza FC, Appel GB, Barbour SJ, Rovin BH, Lafayette RA, Aslam N, et al. Rituximab or Cyclosporine in the Treatment of Membranous Nephropathy. N Engl J Med. 2019;381(1):36-46 | 10.1056/NEJMoa1814427 | 31269364 | 出版社の著作物（CC の表示なし） | RESTRICTED | 12か月・24か月時点の寛解割合は試験の要約と二次引用で確認。DOI は引用情報、PMID は NCBI の ID 検索で照合 | GN-016 |
| SRC-584 | Sethi S, Fervenza FC. Membranoproliferative glomerulonephritis — a new look at an old entity. N Engl J Med. 2012;366(12):1119-1131 | 10.1056/NEJMra1108178 | 22435371 | 出版社の著作物（CC の表示なし） | RESTRICTED | 免疫複合体型と補体介在型への再分類の考え方は引用文献情報で確認し、DOI・PMID を NCBI の ID 検索で照合（PMID 22435371） | GN-017 |
| SRC-585 | Boils CL, Nasr SH, Walker PD, Couser WG, Larsen CP. Update on endocarditis-associated glomerulonephritis. Kidney Int. 2015;87(6):1241-1249 | 10.1038/ki.2014.424 | 25607109 | CC BY-NC-ND 3.0（PMC ページの表示） | RESTRICTED | PubMed 抄録と PMC 全文で 49例の臨床・病理所見の数値を確認し、DOI・PMID・PMCID（PMC4455140）を NCBI の ID 変換で照合 | GN-019 |
| SRC-586 | Hamada R, Kaku Y, Inaba A, Kaito H, Kimata T, Kondo S, et al. A digest of the clinical practice guideline for pediatric idiopathic nephrotic syndrome 2020 updated: medical therapy. Clin Exp Nephrol. 2025;29(6):691-701 | 10.1007/s10157-025-02636-5 | 40063214 | ライセンス表示を確認できず（出版社ページで CC の表示なし） | UNKNOWN | PubMed レコードで書誌・DOI・PMID を確認。2020年改訂と補遺の経緯は出版社ページの抜粋で確認 | GN-018 |
| SRC-587 | Chiu HF, Chen HC, Lu KC, Shu KH; Taiwan Society of Nephrology. Distribution of glomerular diseases in Taiwan: preliminary report of National Renal Biopsy Registry — publication on behalf of Taiwan Society of Nephrology. BMC Nephrol. 2018;19:6 | 10.1186/s12882-017-0810-4 | 29320993 | CC BY 4.0（誌面の Open Access 表示で確認） | OPEN | BMC の全文ページで症候分類の定義（急性腎炎症候群・RPGN・慢性腎炎症候群・ネフローゼ症候群）を確認し、DOI・PMID・PMCID（PMC5764016）を NCBI の ID 変換で照合 | GN-020 |
| SRC-589 | Haneda M, Utsunomiya K, Koya D, Babazono T, Moriya T, Makino H, et al.; Joint Committee on Diabetic Nephropathy. A new Classification of Diabetic Nephropathy 2014: a report from Joint Committee on Diabetic Nephropathy. J Diabetes Investig. 2015;6(2):242-246 | 10.1111/jdi.12319 | 25802733 | CC BY-NC-ND 4.0（Crossref の license 欄で確認） | RESTRICTED | PMC の本文ページで分類表（Table 1）と改訂点を確認し、PubMed 抄録と書誌・DOI・PMID を照合。Crossref で license を確認 | GN-021 |
| SRC-590 | Perkovic V, Jardine MJ, Neal B, et al.; CREDENCE Trial Investigators. Canagliflozin and Renal Outcomes in Type 2 Diabetes and Nephropathy. N Engl J Med. 2019;380(24):2295-2306 | 10.1056/NEJMoa1811744 | 30990260 | 出版社の利用条件（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録で対象・主要アウトカム・ハザード比を確認し、Crossref レコードで書誌・DOI・license を照合 | GN-022 |
| SRC-591 | KDIGO Diabetes Work Group. KDIGO 2022 Clinical Practice Guideline for Diabetes Management in Chronic Kidney Disease. Kidney Int. 2022;102(5S):S1-S127 | 10.1016/j.kint.2022.06.008 | 36272764 | CC BY-NC-ND 4.0（Crossref の license 欄で確認） | RESTRICTED | ガイドラインの推奨文（推奨1.3.1 と付随するプラクティスポイント）を本文要約で確認し、PubMed と Crossref で書誌・DOI・PMID・license を照合 | GN-023 |
| SRC-592 | KDIGO Lupus Nephritis Work Group. KDIGO 2024 Clinical Practice Guideline for the management of LUPUS NEPHRITIS. Kidney Int. 2024;105(1S):S1-S69 | 10.1016/j.kint.2023.09.002 | 38182286 | CC BY-NC-ND 4.0（ガイドライン本文の著作権表示で確認） | RESTRICTED | ガイドライン PDF 本文で診断フローチャート（図1）、クラス別の治療の章立て、推奨10.2.1.1 と 10.2.3.1.1、著作権表示を確認。PubMed と Crossref で書誌・DOI・PMID を照合 | GN-024, GN-025, GN-034 |
| SRC-593 | Furie R, et al. Two-Year, Randomized, Controlled Trial of Belimumab in Lupus Nephritis. N Engl J Med. 2020;383(12):1117-1128 | 10.1056/NEJMoa2001180 | 32937045 | 出版社の利用条件（NEJM。CC の表示なし） | RESTRICTED | PubMed 抄録で対象・主要評価項目・腎反応率を確認し、Crossref レコードで書誌・DOI を照合 | GN-026 |
| SRC-594 | Shi J, Shen Q, Chen XM, Du XG. Clinical characteristics and outcomes in microscopic polyangiitis patients with renal involvement: a study of 124 Chinese patients. BMC Nephrol. 2019;20:339 | 10.1186/s12882-019-1535-3 | 31477033 | CC BY 4.0（Crossref の license 欄と誌面の Open Access 表示で確認） | OPEN | PubMed 抄録と PMC 本文で症例数・ハザード比を確認し、Crossref で書誌・DOI・license を照合 | GN-027 |
| SRC-595 | Stone JH, et al. Rituximab versus Cyclophosphamide for ANCA-Associated Vasculitis. N Engl J Med. 2010;363(3):221-232 | 10.1056/NEJMoa0909905 | 20647199 | 出版社の利用条件（NEJM。Crossref に license 欄なし。CC の表示なし） | RESTRICTED | PubMed 抄録で対象・寛解率・非劣性を確認し、Crossref レコードで書誌・DOI を照合 | GN-028 |
| SRC-596 | Aasarød K, Bostad L, Hammerstrøm J, Jørstad S, Iversen BM. Renal histopathology and clinical course in 94 patients with Wegener's granulomatosis. Nephrol Dial Transplant. 2001;16(5):953-960 | 10.1093/ndt/16.5.953 | 11328900 | ライセンス表示を確認できず（Crossref のレコードに license 欄なし） | UNKNOWN | PubMed 抄録で生検所見の頻度と相関を確認し、Crossref レコードで書誌・DOI を照合 | GN-029 |
| SRC-597 | Cui Z, Zhao J, Jia XY, et al. Anti-glomerular basement membrane disease: outcomes of different therapeutic regimens in a large single-center Chinese cohort study. Medicine (Baltimore). 2011;90(5):303-311 | 10.1097/MD.0b013e31822f6f68 | 21862934 | ライセンス表示を確認できず（Crossref のレコードに license 欄なし） | UNKNOWN | PubMed 抄録で生存率と治療レジメン別のハザード比を確認し、Crossref レコードで書誌・DOI を照合 | GN-030 |
| SRC-598 | Narchi H. Risk of long term renal impairment and duration of follow up recommended for Henoch-Schonlein purpura with normal or minimal urinary findings: a systematic review. Arch Dis Child. 2005;90(9):916-920 | 10.1136/adc.2005.074641 | 15871983 | ライセンス表示を確認できず（Crossref のレコードに license 欄なし） | UNKNOWN | PubMed 抄録と PMC 本文で尿異常の出現時期と永続的腎障害の頻度を確認し、Crossref レコードで書誌・DOI を照合 | GN-031 |
| SRC-599 | Palladini G, et al. A staging system for renal outcome and early markers of renal response to chemotherapy in AL amyloidosis. Blood. 2014;124(15):2325-2332 | 10.1182/blood-2014-04-570010 | 25115890 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | PubMed 抄録で腎病期の閾値と透析移行率、腎反応の基準を確認し、Crossref レコードで書誌・DOI を照合 | GN-032 |
| SRC-600 | Lefaucheur C, et al. Membranous nephropathy and cancer: Epidemiologic evidence and determinants of high-risk cancer association. Kidney Int. 2006;70(8):1510-1517 | 10.1038/sj.ki.5001790 | 16941021 | Elsevier の利用条件（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録と出版社ページで悪性腫瘍の頻度・標準化発生比・炎症細胞のカットオフを確認し、Crossref レコードで書誌・DOI・license を照合 | GN-033 |
| SRC-601 | Sawamura M, Sawa N, Yamanouchi M, Ikuma D, Sekine A, Mizuno H, et al. Use of biologic agents and methotrexate improves renal manifestation and outcome in patients with rheumatoid arthritis: a retrospective analysis. Clin Exp Nephrol. 2022;26(4):341-349 | 10.1007/s10157-021-02160-2 | 34846624 | CC BY 4.0（Crossref の license 欄で確認） | OPEN | PubMed 抄録と PMC 本文で生検所見の内訳と AA アミロイドーシスの転帰を確認し、Crossref で書誌・DOI・license を照合 | GN-035 |
| SRC-602 | Savige J, Gregory M, Gross O, Kashtan C, Ding J, Flinter F. Expert guidelines for the management of Alport syndrome and thin basement membrane nephropathy. J Am Soc Nephrol. 2013;24(3):364-375 | 10.1681/ASN.2012020148 | 23349312 | ライセンス表示を確認できず（Crossref のレコードに license 欄なし） | UNKNOWN | PubMed 抄録で遺伝学的検査・RAS 阻害・ドナーに関する推奨を確認し、Crossref レコードで書誌・DOI を照合 | GN-036, GN-037, GN-038 |
| SRC-603 | Wanner C, Oliveira JP, Ortiz A, Mauer M, Germain DP, Linthorst GE, et al. Prognostic indicators of renal disease progression in adults with Fabry disease: natural history data from the Fabry Registry. Clin J Am Soc Nephrol. 2010;5(12):2220-2228 | 10.2215/CJN.04340510 | 20813854 | ライセンス表示を確認できず（Crossref のレコードに license 欄なし） | UNKNOWN | PubMed 抄録で未治療成人の eGFR 低下と尿蛋白との関係を確認し、Crossref レコードで書誌・DOI を照合 | GN-039 |
| SRC-604 | Hughes DA, et al. Oral pharmacological chaperone migalastat compared with enzyme replacement therapy in Fabry disease: 18-month results from the randomised phase III ATTRACT study. J Med Genet. 2017;54(4):288-296 | 10.1136/jmedgenet-2016-104178 | 27834756 | CC BY-NC 4.0（PMC ページの表示で確認） | RESTRICTED | PubMed 抄録と PMC 本文で対象・腎機能への影響・イベント発生率を確認し、Crossref で書誌・DOI を照合 | GN-040 |
| SRC-605 | Heras Benito M. Nephroangiosclerosis: an update. Hipertens Riesgo Vasc. 2023;40(2):98-103 | 10.1016/j.hipert.2022.07.004 | 36050216 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録で内容と書誌を確認し、Crossref レコードで DOI と license を確認 | KT-001 |
| SRC-606 | Shi W, Lian X, Li W, Lian R, Yu S, Dai Z. Significant proteinuria as a predictor of renal prognosis in malignant hypertension patients with thrombotic microangiopathy: a prospective cohort study. BMC Nephrol. 2025;26(1):513 | 10.1186/s12882-025-04407-6 | 40898080 | CC BY-NC-ND 4.0（Crossref の license 欄で確認） | RESTRICTED | PMC 掲載ページと PubMed 抄録で症例数・割合・ハザード比を確認し、Crossref レコードで DOI と license を確認 | KT-002 |
| SRC-607 | Tafur-Soto JD, White CJ. Renal artery stenosis. Cardiol Clin. 2015;33(1):59-73 | 10.1016/j.ccl.2014.09.006 | 25439331 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録で内容と書誌を確認し、Crossref レコードで DOI と license を確認 | KT-003 |
| SRC-608 | Oh YK, Yang CW, Kim YL, Kang SW, Park CW, et al. Clinical Characteristics and Outcomes of Renal Infarction. Am J Kidney Dis. 2016;67(2):243-50 | 10.1053/j.ajkd.2015.09.019 | 26545635 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録で症例数・原因の割合・転帰を確認し、Crossref レコードで DOI と license を確認 | KT-004 |
| SRC-609 | Scolari F, Ravani P, Gaggi R, Santostefano M, Rollino C, et al. The challenge of diagnosing atheroembolic renal disease: clinical features and prognostic factors. Circulation. 2007;116(3):298-304 | 10.1161/CIRCULATIONAHA.106.680991 | 17606842 | 出版社の著作物（Crossref のレコードに license 欄なし。CC の表示なし） | RESTRICTED | PubMed 抄録で症例数・転帰・予測因子を確認し、Crossref レコードで書誌と DOI を確認 | KT-005 |
| SRC-610 | Cozzi F, Marson P, Cardarelli S, Favaro M, Tison T, et al. Prognosis of scleroderma renal crisis: a long-term observational study. Nephrol Dial Transplant. 2012;27(12):4398-403 | 10.1093/ndt/gfs317 | 22859795 | 出版社の著作物（Crossref のレコードに license 欄なし。CC の表示なし） | RESTRICTED | PubMed 抄録で発症割合・末期腎不全への進行・生存率を確認し、Crossref レコードで書誌と DOI を確認 | KT-006 |
| SRC-611 | Zhang LJ, Zhang Z, Li SJ, Meinel FG, Nance JW Jr, et al. Pulmonary embolism and renal vein thrombosis in patients with nephrotic syndrome: prospective evaluation of prevalence and risk factors with CT. Radiology. 2014;273(3):897-906 | 10.1148/radiol.14140121 | 25072187 | 出版社の著作物（Crossref のレコードに license 欄なし。CC の表示なし） | RESTRICTED | PubMed 抄録で症例数と腎静脈血栓症の頻度を確認し、Crossref レコードで書誌と DOI を確認 | KT-007 |
| SRC-612 | Ozaki K, Miyayama S, Ushiogi Y, Matsui O. Renal involvement of polyarteritis nodosa: CT and MR findings. Abdom Imaging. 2009;34(2):265-70 | 10.1007/s00261-008-9377-7 | 18317834 | Springer の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録で画像所見と症例数を確認し、Crossref レコードで DOI と license を確認 | KT-008 |
| SRC-613 | Turgut F, Awad AS, Abdel-Rahman EM. Acute Kidney Injury: Medical Causes and Pathogenesis. J Clin Med. 2023;12(1):375 | 10.3390/jcm12010375 | 36615175 | CC BY 4.0（Crossref の license 欄で確認） | OPEN | PMC 掲載ページと PubMed 抄録で内容を確認し、Crossref レコードで DOI と license（CC BY 4.0）を確認 | KT-009 |
| SRC-614 | Praga M, González E. Acute interstitial nephritis. Kidney Int. 2010;77(11):956-61 | 10.1038/ki.2010.89 | 20336051 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録で頻度・原因・臨床像・治療と線維化への移行を確認し、Crossref レコードで DOI と license を確認 | KT-010, KT-011, KT-013 |
| SRC-615 | Bridoux F, Leung N, Belmouaz M, Royal V, Ronco P, Nasr SH. Management of acute kidney injury in symptomatic multiple myeloma. Kidney Int. 2021;99(3):570-580 | 10.1016/j.kint.2020.11.010 | 33440212 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録で円柱腎症の機序と治療の要点を確認し、Crossref レコードで DOI と license を確認 | KT-012 |
| SRC-616 | François H, Mariette X. Renal involvement in primary Sjögren syndrome. Nat Rev Nephrol. 2016;12(2):82-93 | 10.1038/nrneph.2015.174 | 26568188 | Springer の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録で腎病変の頻度と病型を確認し、Crossref レコードで DOI と license を確認 | KT-014 |
| SRC-617 | Saeki T, Kawano M. IgG4-related kidney disease. Kidney Int. 2014;85(2):251-7 | 10.1038/ki.2013.393 | 24107849 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録で病型・検査所見・ステロイドへの反応を確認し、Crossref レコードで DOI と license を確認 | KT-015 |
| SRC-618 | Perazella MA. Drug-induced acute kidney injury: diverse mechanisms of tubular injury. Curr Opin Crit Care. 2019;25(6):550-557 | 10.1097/MCC.0000000000000653 | 31483318 | 出版社の著作物（Crossref のレコードに license 欄なし。CC の表示なし） | RESTRICTED | PubMed 抄録で薬剤ごとの尿細管障害の機序を確認し、Crossref レコードで書誌と DOI を確認 | KT-016 |
| SRC-619 | Yanai H, Adachi H, Hakoshima M, Katsuyama H. Molecular Biological and Clinical Understanding of the Pathophysiology and Treatments of Hyperuricemia and Its Association with Metabolic Syndrome, Cardiovascular Diseases and Chronic Kidney Disease. Int J Mol Sci. 2021;22(17):9221 | 10.3390/ijms22179221 | 34502127 | CC BY 4.0（Crossref の license 欄で確認） | OPEN | PMC 掲載ページと PubMed 抄録で尿酸排泄の割合と腎障害との関連を確認し、Crossref レコードで DOI と license（CC BY 4.0）を確認 | KT-017 |
| SRC-620 | Bonner R, Hladik G. Renal Tubular Acidosis: Core Curriculum 2025. Am J Kidney Dis. 2025;85(4):501-512 | 10.1053/j.ajkd.2024.08.014 | 39864011 | 出版社の著作物（誌面・レコードに CC 表示なし） | RESTRICTED | PubMed ページで書誌・PMID・DOI・抄録を確認 | KT-018 |
| SRC-621 | Watanabe T. Improving outcomes for patients with distal renal tubular acidosis: recent advances and challenges ahead. Pediatric Health Med Ther. 2018;9:181-190 | 10.2147/PHMT.S174459 | 30588151 | CC BY-NC 3.0（誌面の表示） | RESTRICTED | PMC 全文ページで書誌・PMID・PMCID・ライセンス表示と抄録・本文を確認し、DOI は収載レコードと照合 | KT-019 |
| SRC-622 | Haque SK, Ariceta G, Batlle D. Proximal renal tubular acidosis: a not so rare disorder of multiple etiologies. Nephrol Dial Transplant. 2012;27(12):4273-4287 | 10.1093/ndt/gfs493 | 23235953 | 出版社の著作物（誌面・レコードに CC 表示なし） | RESTRICTED | PubMed と PMC ページで書誌・PMID・PMCID・DOI・抄録を確認 | KT-020 |
| SRC-623 | Cherqui S, Courtoy PJ. The renal Fanconi syndrome in cystinosis: pathogenic insights and therapeutic perspectives. Nat Rev Nephrol. 2017;13(2):115-131 | 10.1038/nrneph.2016.182 | 27990015 | 出版社の著作物（誌面・レコードに CC 表示なし） | RESTRICTED | PMC ページで書誌・PMID・PMCID・DOI・抄録を確認 | KT-021 |
| SRC-624 | Chillarón J, Font-Llitjós M, Fort J, Zorzano A, Goldfarb DS, Nunes V, Palacín M. Pathophysiology and treatment of cystinuria. Nat Rev Nephrol. 2010;6(7):424-434 | 10.1038/nrneph.2010.69 | 20517292 | 出版社の著作物（誌面・レコードに CC 表示なし） | RESTRICTED | 抄録本文で内容を確認し、書誌と DOI は論文レコードで、PMID は疾患データベースの参照情報と照合 | KT-022 |
| SRC-625 | Bockenhauer D, Bichet DG. Pathophysiology, diagnosis and management of nephrogenic diabetes insipidus. Nat Rev Nephrol. 2015;11(10):576-588 | 10.1038/nrneph.2015.89 | 26077742 | 出版社の著作物（誌面・レコードに CC 表示なし） | RESTRICTED | PubMed ページで書誌・PMID・抄録を確認し、DOI は書誌レコードと照合 | KT-023 |
| SRC-626 | Milano S, Carmosino M, Gerbino A, Svelto M, Procino G. Hereditary nephrogenic diabetes insipidus: pathophysiology and possible treatment. An update. Int J Mol Sci. 2017;18(11):2385 | 10.3390/ijms18112385 | 29125546 | CC BY 4.0（誌面の表示） | OPEN | PMC ページで書誌・PMID・PMCID・抄録を確認し、DOI は収載レコードと照合 | KT-024 |
| SRC-627 | Cunha TDS, Heilberg IP. Bartter syndrome: causes, diagnosis, and treatment. Int J Nephrol Renovasc Dis. 2018;11:291-301 | 10.2147/IJNRD.S155397 | 30519073 | CC BY-NC 3.0（誌面の表示） | RESTRICTED | PMC 全文ページで書誌・PMID・PMCID・ライセンス表示と抄録・本文（有病率と遺伝子型の表）を確認し、DOI は収載レコードと照合 | KT-025 |
| SRC-628 | Blanchard A, Bockenhauer D, Bolignano D, et al. Gitelman syndrome: consensus and guidance from a Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference. Kidney Int. 2017;91(1):24-33 | 10.1016/j.kint.2016.09.046 | 28003083 | 出版社の著作物（KDIGO 会議報告、CC 表示なし） | RESTRICTED | PubMed 収載の抄録と書誌レコードで PMID・DOI を確認 | KT-026 |
| SRC-629 | Tetti M, Monticone S, Burrello J, et al. Liddle Syndrome: Review of the Literature and Description of a New Case. Int J Mol Sci. 2018;19(3):812 | 10.3390/ijms19030812 | 29534496 | CC BY 4.0（誌面の表示） | OPEN | PMC ページと収載レコードで書誌・PMID・PMCID・DOI・抄録を確認 | KT-027 |
| SRC-630 | Downie ML, Lopez Garcia SC, Kleta R, Bockenhauer D. Inherited Tubulopathies of the Kidney: Insights from Genetics. Clin J Am Soc Nephrol. 2021;16(4):620-630 | 10.2215/CJN.14481119 | 32238367 | 出版社の著作物（学会誌、CC 表示なし） | RESTRICTED | 書誌レコードと学会誌ページで DOI・PMID・PMCID・抄録を確認 | KT-028 |

## 2. 事実票 YAML

```yaml
- id: GN-001
  domain: GN
  subdomain: 血尿
  assertion:
    plain_statement_ja: 顕微鏡的血尿は、適切に採取した尿の顕微鏡検査で赤血球3個/HPF以上を認めるものと定義される。米国の2025年改訂ガイドラインでは、年齢と性、喫煙量、1回の尿検査での赤血球数、肉眼的血尿の既往、尿路上皮癌の危険因子の有無で低リスク・中間リスク・高リスクに層別し、低リスクでは6か月後の尿検査の再検、中間リスクでは膀胱鏡と腎超音波、高リスクでは膀胱鏡と上部尿路の軸位断画像（CT尿路造影など）による評価を行う。
    condition:
      region: 米国
      study: AUA/SUFU ガイドライン 2025年改訂
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-572
    source: 'Barocas DA, Lotan Y, Matulewicz RS, Raman JD, Westerman ME, Kirkby E, Pak L, Souter L. Updates to Microhematuria: AUA/SUFU Guideline (2025). J Urol. 2025;213(5):547-557'
    doi: 10.1097/JU.0000000000004490
    pmid: '40013563'
    pmcid: null
    url: https://doi.org/10.1097/JU.0000000000004490
    source_license: 出版社（AUA）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: リスク層別の境界値（赤血球数・喫煙量など）はガイドラインの表から読み取ったものである（表から読み取り）。米国のガイドラインであり、日本の検尿・診療の基準と同一とは限らない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-010 (id: JlAKpmc)'
    kokushi: 医学各論 Ⅷ-1-E-①（血尿、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-002
  domain: GN
  subdomain: 蛋白尿
  assertion:
    plain_statement_ja: 蛋白尿の評価では尿アルブミン/クレアチニン比（ACR）が用いられ、国際的な CKD の枠組みではアルブミン尿は A1（30 mg/g未満）、A2（30〜300 mg/g）、A3（300 mg/gを超える）の3区分に分けられる。アルブミン尿の増加は腎障害のマーカーであり心血管リスクとも関連するため、一過性の増加の原因を除いたうえで持続性を確認し、糸球体濾過量の区分と組み合わせて評価する。
    condition:
      region: 国際
      study: KDIGO 2024 CKD 評価・管理ガイドライン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-573
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int. 2024;105(4S):S117-S314'
    doi: 10.1016/j.kint.2023.10.018
    pmid: '38490803'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2023.10.018
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: アルブミン尿区分の境界値はガイドラインの表から読み取ったものである（表から読み取り）。日本の特定健診などで用いる試験紙法による蛋白尿の判定とは方式が異なる。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-011 (id: JlAKpmg)'
    kokushi: 医学各論 Ⅷ-1-E-②（蛋白尿、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-003
  domain: GN
  subdomain: 急性糸球体腎炎
  assertion:
    plain_statement_ja: 溶連菌感染後急性糸球体腎炎は、A群溶連菌の感染後に急性腎炎症候群として発症する。小児の長期予後は一般に良好で、流行性と散発性の110例を15〜18年間追跡した報告では、蛋白尿7.2%、顕微鏡的血尿5.4%、高血圧3.0%、高窒素血症0.9%にとどまり、一般人口とほぼ変わらなかった。一方、溶連菌感染が反復する環境にある集団では、後にアルブミン尿を呈する調整オッズ比が6.1と高く、背景集団によって長期予後は異なる。
    condition:
      region: 国際
      study: 2008年の総説（著者らの小児110例の15〜18年の前向き追跡を含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-574
    source: 'Rodriguez-Iturbe B, Musser JM. The current state of poststreptococcal glomerulonephritis. J Am Soc Nephrol. 2008;19(10):1855-1864'
    doi: 10.1681/ASN.2008010092
    pmid: '18667731'
    pmcid: null
    url: https://doi.org/10.1681/ASN.2008010092
    source_license: ライセンス表示を確認できず（CC の表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 長期予後の数値は著者らの単一コホートに基づくもので、成人の発症例や腎機能低下を伴う例では経過が異なる。出典のライセンスは未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-321 (id: Jlvnl9M)'
    kokushi: 医学各論 Ⅷ-1-A-①（急性糸球体腎炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-004
  domain: GN
  subdomain: 急性糸球体腎炎
  assertion:
    plain_statement_ja: 感染に関連する急性糸球体腎炎では、なお続いている感染への治療と、浮腫・高血圧・体液過剰に対する支持療法が管理の中心となり、典型的な経過をたどる溶連菌感染後糸球体腎炎に対して免疫抑制療法は用いない。国際ガイドラインは感染関連糸球体腎炎を独立した領域として扱い、診断、予後、治療、特殊な状況という枠組みで推奨を示している。
    condition:
      region: 国際
      study: KDIGO 2021 糸球体疾患ガイドライン（感染関連糸球体腎炎の章）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-571
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) Glomerular Diseases Work Group. KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases. Kidney Int. 2021;100(4S):S1-S276'
    doi: 10.1016/j.kint.2021.05.021
    pmid: '34556256'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2021.05.021
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードはガイドラインの一般原則であり、個別の薬剤名と用量は記載していない。支持療法で用いる利尿薬や降圧薬は国内承認薬であるが、個別製剤の適応確認はしていない。半月体形成を伴うなど非典型的な経過では扱いが異なる。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-321 (id: Jlvnl9M)'
    kokushi: 医学各論 Ⅷ-1-A-①（急性糸球体腎炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-005
  domain: GN
  subdomain: 急速進行性糸球体腎炎症候群
  assertion:
    plain_statement_ja: 急速進行性糸球体腎炎は、数週から数か月の経過で腎機能が急速に低下する臨床症候群で、腎生検では半月体形成を特徴とする。機序により、抗糸球体基底膜（抗GBM）抗体型、免疫複合体型、免疫沈着の乏しい pauci-immune 型（多くは ANCA 関連血管炎）に分類され、治療方針が異なるため、ANCA や抗GBM抗体、補体などの血清学と腎生検による早期の鑑別が重要である。
    condition:
      region: 国際
      study: KDIGO 2021 糸球体疾患ガイドライン（ANCA関連血管炎・抗GBM抗体系球体腎炎の章を含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-571
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) Glomerular Diseases Work Group. KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases. Kidney Int. 2021;100(4S):S1-S276'
    doi: 10.1016/j.kint.2021.05.021
    pmid: '34556256'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2021.05.021
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 分類の枠組みはガイドラインに基づく。各型の頻度は年齢と地域で異なり、本カードでは頻度の数値は扱っていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-1-A-②（急速進行性糸球体腎炎症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-006
  domain: GN
  subdomain: 急速進行性糸球体腎炎症候群
  assertion:
    plain_statement_ja: 重症の ANCA 関連血管炎（糸球体濾過量50 mL/min/1.73 m2未満またはびまん性肺出血）を対象とした国際共同ランダム化試験（704例）では、血漿交換を行っても死亡または末期腎不全の複合転帰は減らなかった（28.4% 対 31.0%、ハザード比0.86、95%信頼区間0.65〜1.13）。経口グルココルチコイドの減量レジメンは標準量レジメンに対して非劣性で、1年以内の重篤な感染症は減量群で少なかった（発生率比0.69）。
    condition:
      region: 国際
      study: 2020年の多施設共同ランダム化比較試験（2×2要因デザイン）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-575
    source: 'Walsh M, Merkel PA, Peh CA, Szpirt W, Puéchal X, Fujimoto S, et al. Plasma Exchange and Glucocorticoids in Severe ANCA-Associated Vasculitis. N Engl J Med. 2020;382(7):622-631'
    doi: 10.1056/NEJMoa1803537
    pmid: '32053298'
    pmcid: PMC7325726
    url: https://doi.org/10.1056/NEJMoa1803537
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: グルココルチコイドは国内承認薬だが、本試験の減量レジメンそのものの国内の適応・保険適用は未確認である。抗GBM抗体型など対象外の病型にはこの結果をそのまま当てはめない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-1-A-②（急速進行性糸球体腎炎症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-007
  domain: GN
  subdomain: IgA腎症
  assertion:
    plain_statement_ja: IgA腎症は世界で最も多い原発性の慢性糸球体疾患で、診断の決め手は糸球体メサンギウムに IgA が優位に沈着することである。蛍光抗体法では IgA が単独で、または IgG や IgM を伴って沈着し、補体 C3 とプロペルジンはほぼ常にみられる一方、C1q は通常みられない。臨床像は、上気道感染に伴う肉眼的血尿から検尿異常のみの例まで幅広い。
    condition:
      region: 国際
      study: 2013年の総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-576
    source: 'Wyatt RJ, Julian BA. IgA nephropathy. N Engl J Med. 2013;368(25):2402-2414'
    doi: 10.1056/NEJMra1206793
    pmid: '23782179'
    pmcid: null
    url: https://doi.org/10.1056/NEJMra1206793
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 免疫グロブリン沈着の内訳の頻度は施設により大きく異なることが本文に記されている。診断には腎生検が必要である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-322 (id: Jlvnl9U)'
    kokushi: 医学各論 Ⅷ-1-A-③（慢性糸球体腎炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-008
  domain: GN
  subdomain: IgA腎症
  assertion:
    plain_statement_ja: 進行リスクの高い IgA 腎症（蛋白尿1 g/日以上が最適化した支持療法を3か月以上行った後も持続する例）を対象とした国際共同ランダム化試験（503例）では、経口メチルプレドニゾロンを6〜9か月間投与した群で、推算糸球体濾過量の40%低下・腎不全・腎疾患による死亡の複合転帰が少なかった（28.8% 対 43.1%、ハザード比0.53）。一方、重篤な有害事象はメチルプレドニゾロン群で多く（10.9% 対 2.8%）、とくに高用量レジメンで重篤な感染症が増えた。
    condition:
      region: 国際
      study: 2022年の多施設共同二重盲検ランダム化比較試験（TESTING）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-577
    source: 'Lv J, Wong MG, Hladunewich MA, Jha V, Hooi LS, Monaghan H, et al. Effect of Oral Methylprednisolone on Decline in Kidney Function or Kidney Failure in Patients With IgA Nephropathy: The TESTING Randomized Clinical Trial. JAMA. 2022;327(19):1888-1898'
    doi: 10.1001/jama.2022.5368
    pmid: '35579642'
    pmcid: PMC9115617
    url: https://doi.org/10.1001/jama.2022.5368
    source_license: 出版社の著作物（PMC 掲載ページにも CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: メチルプレドニゾロンは国内承認薬だが、IgA腎症に対する国内の適応・保険適用は未確認である。試験では途中で用量が減量レジメンに変更されており、用いる場合は利益と感染症のリスクを個別に評価する必要がある。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-322 (id: Jlvnl9U)'
    kokushi: 医学各論 Ⅷ-1-A-③（慢性糸球体腎炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-009
  domain: GN
  subdomain: IgA腎症
  assertion:
    plain_statement_ja: IgA腎症の Oxford 分類は、2016年の改訂で従来の MEST スコアに半月体（C）が加わり、MEST-C スコアとして生検報告に記載することが推奨された。糸球体が8個以上ある生検標本では、メサンギウム細胞増多（M）、分節性硬化（S）、間質線維化・尿細管萎縮（T）が臨床転帰を予測し、より大規模なコホートで半月体（C）も予後予測因子であることが確認された。管内増殖（E）は、免疫抑制療法を受けていない例でのみ予後と関連した。
    condition:
      region: 国際
      study: 2016年の Oxford 分類改訂（分類ワーキンググループの報告）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-578
    source: 'Trimarchi H, Barratt J, Cattran DC, Cook HT, Coppo R, Haas M, et al. Oxford Classification of IgA nephropathy 2016: an update from the IgA Nephropathy Classification Working Group. Kidney Int. 2017;91(5):1014-1021'
    doi: 10.1016/j.kint.2017.02.003
    pmid: '28341274'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2017.02.003
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: M と E の判定には報告間のばらつきが指摘されており、予後予測は生検時の臨床データと組み合わせて行うものとされている。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-322 (id: Jlvnl9U)'
    kokushi: 医学各論 Ⅷ-1-A-③（慢性糸球体腎炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-010
  domain: GN
  subdomain: ネフローゼ症候群
  assertion:
    plain_statement_ja: 日本のネフローゼ症候群の臨床的定義では、尿蛋白3.5 g/日以上の持続（随時尿では尿蛋白/クレアチニン比3.5 g/gCr以上に相当）と血清アルブミン3.0 g/dL以下が診断に必須の条件であり、浮腫と脂質異常症（高LDLコレステロール血症）は必須ではないが重要な参考所見とされる。卵円形脂肪体も診断の参考になる。治療効果の評価は尿蛋白量に基づいて行われる。
    condition:
      region: 日本
      study: 日本腎臓学会などのエビデンスに基づくネフローゼ症候群診療ガイドライン2014（英語版2016年掲載）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-579
    source: 'Nishi S, Ubara Y, Utsunomiya Y, Okada K, Obata Y, Kai H, et al. Evidence-based clinical practice guidelines for nephrotic syndrome 2014. Clin Exp Nephrol. 2016;20(3):342-370'
    doi: 10.1007/s10157-015-1216-x
    pmid: '27099136'
    pmcid: PMC4891386
    url: https://doi.org/10.1007/s10157-015-1216-x
    source_license: CC BY 4.0（PMC ページの Open Access 表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 定義の数値はガイドラインの表から読み取ったものである（表から読み取り）。小児では定義が異なり、高度蛋白尿と血清アルブミン2.5 g/dL以下が用いられる。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-011
  domain: GN
  subdomain: ネフローゼ症候群
  assertion:
    plain_statement_ja: ネフローゼ症候群の治療は、原因疾患に対する免疫抑制療法と、浮腫に対する塩分制限と利尿薬、レニン・アンジオテンシン系阻害薬による蛋白尿の抑制と血圧管理、血栓塞栓症や感染症などの合併症への注意を組み合わせて行う。国際ガイドラインはネフローゼ症候群を独立した領域として扱い、微小変化群や巣状分節性糸球体硬化症など原因疾患ごとに診断と治療の推奨を示している。
    condition:
      region: 国際
      study: KDIGO 2021 糸球体疾患ガイドライン（ネフローゼ症候群の章）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-571
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) Glomerular Diseases Work Group. KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases. Kidney Int. 2021;100(4S):S1-S276'
    doi: 10.1016/j.kint.2021.05.021
    pmid: '34556256'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2021.05.021
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードはガイドラインに基づく管理の総論であり、合併症の頻度などの個別の数値は扱っていない。免疫抑制薬や利尿薬、レニン・アンジオテンシン系阻害薬は国内承認薬だが、疾患ごとの適応・保険適用の確認は個別のカードで行う。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-012
  domain: GN
  subdomain: 微小変化群
  assertion:
    plain_statement_ja: 成人および思春期後期に発症した微小変化型ネフローゼ症候群125例の集積では、初期治療として副腎皮質ステロイドが投与された105例のうち88%が16週までに寛解し、寛解までの期間の中央値は4週だった。一方、再発は54%にみられ、急性腎障害が40%、動静脈血栓症が9%に生じた。最終観察時点では90%が腎機能を保ったまま寛解していた。
    condition:
      region: オランダ
      study: 2017年の多施設（10施設）後ろ向き症例集積（1985〜2011年発症例）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-580
    source: 'Maas RJ, Deegens JK, Beukhof JR, Reichert LJ, Ten Dam MA, Beutler JJ, et al. The clinical course of minimal change nephrotic syndrome with onset in adulthood or late adolescence: a case series. Am J Kidney Dis. 2017;69(5):637-646'
    doi: 10.1053/j.ajkd.2016.10.032
    pmid: '28089478'
    pmcid: null
    url: https://doi.org/10.1053/j.ajkd.2016.10.032
    source_license: ライセンス表示を確認できず（CC の表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 単一国の後ろ向き集積であり、小児発症例や日本の症例構成にはそのまま当てはまらない。副腎皮質ステロイドは国内承認薬だが、成人発症例に対する用量・期間の国内の標準は未確認である。出典のライセンスは未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-325 (id: Jlvnl9k)'
    kokushi: 医学各論 Ⅷ-1-B-①（微小変化群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-013
  domain: GN
  subdomain: 巣状分節性糸球体硬化症
  assertion:
    plain_statement_ja: 巣状分節性糸球体硬化症（FSGS）の Columbia 分類は、腎生検標本の形態に基づく病理分類の作業提案として2004年に示され、虚脱型、糸球体尖部（tip）型、細胞型、傍糸球体門型、特定不能型（NOS）の5つの亜型に分ける。形態分類は病因の分類とは別であり、原発性か二次性かといった臨床的な病因の評価と組み合わせて解釈する。
    condition:
      region: 米国
      study: 2004年の病理分類の作業提案（Columbia 分類）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-581
    source: 'D''Agati VD, Fogo AB, Bruijn JA, Jennette JC. Pathologic classification of focal segmental glomerulosclerosis: a working proposal. Am J Kidney Dis. 2004;43(2):368-382'
    doi: 10.1053/j.ajkd.2003.10.024
    pmid: '14750104'
    pmcid: null
    url: https://doi.org/10.1053/j.ajkd.2003.10.024
    source_license: ライセンス表示を確認できず（CC の表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 5亜型の名称は後年の総説の引用でも確認した（二次資料経由の確認を含む）。出典のライセンスは未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-324 (id: Jlvnl9g)'
    kokushi: 医学各論 Ⅷ-1-B-②（巣状分節性糸球体硬化症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-014
  domain: GN
  subdomain: 巣状分節性糸球体硬化症
  assertion:
    plain_statement_ja: 原発性巣状分節性糸球体硬化症の初期治療は高用量のグルココルチコイドであり、蛋白尿の寛解を目指して十分な期間継続し、反応をみて漸減する。ステロイドに抵抗性または不耐の例では、カルシニューリン阻害薬などの免疫抑制療法が検討される。これに対して二次性のものでは免疫抑制療法は行わず、原因への対処と血圧管理、レニン・アンジオテンシン系阻害による腎保護が中心となる。
    condition:
      region: 国際
      study: KDIGO 2021 糸球体疾患ガイドライン（FSGS の章）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-571
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) Glomerular Diseases Work Group. KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases. Kidney Int. 2021;100(4S):S1-S276'
    doi: 10.1016/j.kint.2021.05.021
    pmid: '34556256'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2021.05.021
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: グルココルチコイドとカルシニューリン阻害薬はいずれも国内承認薬だが、原発性FSGSに対する用量と投与期間の国内の適応・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-324 (id: Jlvnl9g)'
    kokushi: 医学各論 Ⅷ-1-B-②（巣状分節性糸球体硬化症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-015
  domain: GN
  subdomain: 膜性腎症
  assertion:
    plain_statement_ja: 特発性膜性腎症では、患者の約70%（37例中26例）にM型ホスホリパーゼA2受容体（PLA2R）に対する自己抗体が検出され、この抗体は二次性膜性腎症では認められなかった。PLA2Rは糸球体上皮細胞（ポドサイト）に発現する185 kDaの糖蛋白で、患者の抗体は主としてIgG4であり、糸球体の免疫沈着物の中でPLA2Rと共局在する。
    condition:
      region: 米国
      study: 2009年の症例対照研究（特発性膜性腎症37例を含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-582
    source: 'Beck LH Jr, Bonegio RGB, Lambeau G, Beck DM, Powell DW, Cummins TD, et al. M-type phospholipase A2 receptor as target antigen in idiopathic membranous nephropathy. N Engl J Med. 2009;361(1):11-21'
    doi: 10.1056/NEJMoa0810457
    pmid: '19571279'
    pmcid: PMC2762083
    url: https://doi.org/10.1056/NEJMoa0810457
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 70%という数値は37例の発見研究に基づくもので、測定系や対象集団により陽性割合は異なる。抗PLA2R抗体測定の国内での実施・保険適用の状況は未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-323 (id: Jlvnl9Y)'
    kokushi: 医学各論 Ⅷ-1-B-③（膜性腎症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-016
  domain: GN
  subdomain: 膜性腎症
  assertion:
    plain_statement_ja: 蛋白尿が持続する膜性腎症130例を対象としたランダム化試験では、リツキシマブはシクロスポリンに対して12か月時点の完全寛解と部分寛解を合わせた割合で非劣性であり（60% 対 52%）、24か月時点では寛解率はリツキシマブ群で維持されたのに対しシクロスポリン群では低下した（60% 対 20%）。完全寛解は24か月時点でリツキシマブ群の35%に得られ、シクロスポリン群では得られなかった。
    condition:
      region: 国際
      study: 2019年の多施設共同ランダム化比較試験（MENTOR、北米の施設で実施）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-583
    source: 'Fervenza FC, Appel GB, Barbour SJ, Rovin BH, Lafayette RA, Aslam N, et al. Rituximab or Cyclosporine in the Treatment of Membranous Nephropathy. N Engl J Med. 2019;381(1):36-46'
    doi: 10.1056/NEJMoa1814427
    pmid: '31269364'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1814427
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録の要約と二次資料で照合したものである（二次資料経由の確認を含む）。リツキシマブは国内では難治性ネフローゼ症候群などに承認があるが、膜性腎症そのものに対する国内の適応・保険適用は未確認である。シクロスポリンは国内承認薬だが、膜性腎症に対する位置づけの国内確認はしていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-323 (id: Jlvnl9Y)'
    kokushi: 医学各論 Ⅷ-1-B-③（膜性腎症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-017
  domain: GN
  subdomain: 膜性増殖性糸球体腎炎
  assertion:
    plain_statement_ja: 膜性増殖性糸球体腎炎は光学顕微鏡による病理パターンの名称であり、病因に基づく現在の分類では、免疫複合体が介在する型と、補体の調節異常による補体介在型（C3腎症を含む）に大別される。この分類に従って、背景にある感染症や自己免疫疾患、単クローン性免疫グロブリン血症の検索と、補体経路の評価が診断の出発点になる。
    condition:
      region: 国際
      study: 2012年の総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-584
    source: 'Sethi S, Fervenza FC. Membranoproliferative glomerulonephritis — a new look at an old entity. N Engl J Med. 2012;366(12):1119-1131'
    doi: 10.1056/NEJMra1108178
    pmid: '22435371'
    pmcid: null
    url: https://doi.org/10.1056/NEJMra1108178
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは分類の枠組みのみを扱い、個別の治療の推奨は扱っていない。2012年の総説であり、その後の補体関連の診断・治療の進歩は反映されていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-326 (id: Jlvnl9s)'
    kokushi: 医学各論 Ⅷ-1-B-④（膜性増殖性糸球体腎炎、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-018
  domain: GN
  subdomain: ネフローゼ症候群
  assertion:
    plain_statement_ja: 小児の特発性ネフローゼ症候群に対する日本の診療ガイドラインは2020年に全面改訂され、2022年に補遺が発行された。内科的治療に関する英語版の要約は2025年に公表されており、ステロイドへの反応性（感受性・抵抗性）や再発のパターンに応じた治療の枠組みを示している。
    condition:
      region: 日本
      study: 小児特発性ネフローゼ症候群診療ガイドライン2020の英語版要約（2025年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-586
    source: 'Hamada R, Kaku Y, Inaba A, Kaito H, Kimata T, Kondo S, et al. A digest of the clinical practice guideline for pediatric idiopathic nephrotic syndrome 2020 updated: medical therapy. Clin Exp Nephrol. 2025;29(6):691-701'
    doi: 10.1007/s10157-025-02636-5
    pmid: '40063214'
    pmcid: null
    url: https://doi.org/10.1007/s10157-025-02636-5
    source_license: ライセンス表示を確認できず（出版社ページで CC の表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: リツキシマブは、頻回再発型・ステロイド依存性の小児発症ネフローゼ症候群に対して国内で承認され保険適用があることを国内の総説で確認した（承認は2014年）。個別の用法・用量は確認していない。出典のライセンスは未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-427 (id: JlvnmHU)'
    kokushi: 医学各論 Ⅷ-1-B-①（微小変化群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-019
  domain: GN
  subdomain: 急性糸球体腎炎
  assertion:
    plain_statement_ja: 感染性心内膜炎に伴う糸球体腎炎では、腎生検で診断された49例の集積で、急性腎障害が最も多い臨床像であり、検査された例の56%に低補体血症、28%にANCA陽性を認めた。病理では壊死性・半月体形成性糸球体腎炎が53%、管内増殖性糸球体腎炎が37%を占め、原因菌は黄色ブドウ球菌が53%と最も多かった。糸球体にはC3の沈着が全例で目立ち、IgGの沈着は30%未満にとどまった。
    condition:
      region: 米国
      study: 2015年の腎生検症例49例の集積
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-585
    source: 'Boils CL, Nasr SH, Walker PD, Couser WG, Larsen CP. Update on endocarditis-associated glomerulonephritis. Kidney Int. 2015;87(6):1241-1249'
    doi: 10.1038/ki.2014.424
    pmid: '25607109'
    pmcid: PMC4455140
    url: https://doi.org/10.1038/ki.2014.424
    source_license: CC BY-NC-ND 3.0（PMC ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 単一施設の生検症例集積であり、弁膜症や静注薬物使用といった背景の割合は集団により異なる。治療は原疾患である心内膜炎の治療が中心であり、免疫抑制療法の位置づけは本カードでは扱っていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-321 (id: Jlvnl9M)'
    kokushi: 医学各論 Ⅷ-1-A-①（急性糸球体腎炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-020
  domain: GN
  subdomain: 腎炎症候群
  assertion:
    plain_statement_ja: 腎炎の症候分類では、急性腎炎症候群は血尿（赤血球円柱を伴う）、通常はネフローゼ域に至らない蛋白尿、軽度の腎機能障害と高血圧を特徴とし、急速進行性糸球体腎炎は急性腎炎症候群の像に週から月単位の急速な腎機能低下を伴うもの、慢性腎炎症候群は蛋白尿と血尿が3か月を超えて持続するものと定義される。台湾の腎生検登録（2014〜2016年、1445件）では、原発性糸球体疾患のうちIgA腎症が慢性腎炎症候群の55.2%、急性腎炎症候群の36.7%、持続性血尿の76.7%を占めて最も多く、ネフローゼ症候群では膜性腎症が28.8%、微小変化群が28.2%を占めた。
    condition:
      region: 台湾
      study: 2018年の全国腎生検登録の予備報告（17施設、1445件）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-587
    source: 'Chiu HF, Chen HC, Lu KC, Shu KH; Taiwan Society of Nephrology. Distribution of glomerular diseases in Taiwan: preliminary report of National Renal Biopsy Registry — publication on behalf of Taiwan Society of Nephrology. BMC Nephrol. 2018;19:6'
    doi: 10.1186/s12882-017-0810-4
    pmid: '29320993'
    pmcid: PMC5764016
    url: https://doi.org/10.1186/s12882-017-0810-4
    source_license: CC BY 4.0（誌面の Open Access 表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 症候の定義と疾患頻度は台湾の登録データに基づく。生検の適応基準が異なるため、日本における頻度とは異なる可能性がある。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-014 (id: JlAKpm0)'
    kokushi: 医学各論 Ⅷ-1-E-①（血尿、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-021
  domain: GN
  subdomain: 糖尿病性腎症
  assertion:
    plain_statement_ja: 日本の糖尿病性腎症病期分類（2014年改訂）は、尿アルブミン（または尿蛋白）と eGFR によって第1期から第5期に分ける。第1期（腎症前期）は正常アルブミン尿（30 mg/gCr 未満）、第2期（早期腎症期）は微量アルブミン尿（30〜299 mg/gCr）、第3期（顕性腎症期）は顕性アルブミン尿（300 mg/gCr 以上）または持続性蛋白尿（0.5 g/gCr 以上）で、第1〜3期はいずれも eGFR 30 mL/min/1.73m² 以上である。第4期（腎不全期）はアルブミン尿の程度を問わず eGFR 30 未満、第5期は透析療法中とされる。2014年改訂では第4期の定義が eGFR 30 未満に改められ、全病期を通じて糖尿病性腎症と非糖尿病性腎疾患との鑑別が重要とされた。
    condition:
      region: 日本
      study: 糖尿病性腎症合同委員会による病期分類の改訂報告（2014年版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-589
    source: 'Haneda M, Utsunomiya K, Koya D, Babazono T, Moriya T, Makino H, et al.; Joint Committee on Diabetic Nephropathy. A new Classification of Diabetic Nephropathy 2014: a report from Joint Committee on Diabetic Nephropathy. J Diabetes Investig. 2015;6(2):242-246'
    doi: 10.1111/jdi.12319
    pmid: '25802733'
    pmcid: PMC4364860
    url: https://doi.org/10.1111/jdi.12319
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 病期の境界値は分類表（Table 1）から読み取った（表から読み取り）。分類は糖尿病性腎症が非糖尿病性腎疾患と鑑別されていることを前提とする。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-332 (id: Jlvnl-Q)'
    kokushi: 医学各論 Ⅷ-1-C-①（糖尿病腎症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-022
  domain: GN
  subdomain: 糖尿病性腎症
  assertion:
    plain_statement_ja: 2型糖尿病とアルブミン尿を伴う慢性腎臓病の患者4,401例（eGFR 30〜90 mL/min/1.73m² 未満、尿アルブミン/クレアチニン比 300 超〜5,000 mg/g、全例がレニン・アンジオテンシン系阻害薬で治療中）を対象とした二重盲検試験（CREDENCE）では、SGLT2阻害薬カナグリフロジン100 mg/日は、主要複合アウトカム（末期腎不全、血清クレアチニンの倍化、腎死または心血管死）のリスクをプラセボより30%低下させた（発生率43.2 対 61.2/1,000人年、ハザード比0.70）。追跡期間の中央値は2.62年で、試験は中間解析を受けて早期に終了した。腎特異的な複合アウトカムのハザード比は0.66、末期腎不全のハザード比は0.68だった。
    condition:
      region: 国際
      study: 多施設二重盲検ランダム化比較試験（CREDENCE、4,401例、追跡中央値2.62年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-590
    source: 'Perkovic V, Jardine MJ, Neal B, et al.; CREDENCE Trial Investigators. Canagliflozin and Renal Outcomes in Type 2 Diabetes and Nephropathy. N Engl J Med. 2019;380(24):2295-2306'
    doi: 10.1056/NEJMoa1811744
    pmid: '30990260'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1811744
    source_license: 出版社の利用条件（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: カナグリフロジンを含む SGLT2 阻害薬の国内の承認・保険適用の範囲（糖尿病性腎症・慢性腎臓病への適応を含む）は未確認であり、取り込み時に PMDA の添付文書で確認が必要。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-332 (id: Jlvnl-Q)'
    kokushi: 医学各論 Ⅷ-1-C-①（糖尿病腎症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-023
  domain: GN
  subdomain: 糖尿病性腎症
  assertion:
    plain_statement_ja: KDIGO の2022年ガイドラインは、糖尿病と慢性腎臓病を併せ持つ患者について、腎疾患の進行と心血管疾患のリスクを下げる包括的な治療戦略をとることを求めている。推奨1.3.1では、2型糖尿病と慢性腎臓病があり、eGFR が20 mL/min/1.73m² 以上の患者に、腎・心血管保護を目的として SGLT2 阻害薬で治療することを推奨している（推奨の強さ1、エビデンスの確実性A）。いったん開始した SGLT2 阻害薬は、eGFR が20未満に下がっても、忍容性に問題がないか腎代替療法が始まるまでは継続してよいとされ、長時間の絶食・手術・重篤な疾患の際にはケトーシスのリスクのため一時的に休薬を検討するとされる。
    condition:
      region: 国際
      study: KDIGO 2022 糖尿病・慢性腎臓病ガイドラインの推奨とプラクティスポイント
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-591
    source: 'KDIGO Diabetes Work Group. KDIGO 2022 Clinical Practice Guideline for Diabetes Management in Chronic Kidney Disease. Kidney Int. 2022;102(5S):S1-S127'
    doi: 10.1016/j.kint.2022.06.008
    pmid: '36272764'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2022.06.008
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 推奨の強さとエビデンスの確実性はガイドライン本文の表記どおりに書いた。SGLT2 阻害薬の国内の承認・保険適用の範囲は未確認であり、国内の eGFR 基準や適応は添付文書で別途確認が必要。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-332 (id: Jlvnl-Q)'
    kokushi: 医学各論 Ⅷ-1-C-①（糖尿病腎症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-024
  domain: GN
  subdomain: ループス腎炎
  assertion:
    plain_statement_ja: KDIGO の2024年ループス腎炎ガイドラインは、腎生検による ISN/RPS 分類のクラスを治療方針の軸に置いている。Class I・II では免疫抑制は主に腎外の全身性エリテマトーデスの症状に応じて決め、活動性の Class III・IV（増殖型）には初期治療の推奨が、純粋な Class V（膜型）には蛋白尿の程度に応じた対応が、それぞれ分けて示されている。腎生検の報告には活動性と慢性化を表す所見の項目を含めることとされ、治療への反応は蛋白尿の減少と腎機能の安定・改善で判定する枠組みが示されている。
    condition:
      region: 国際
      study: KDIGO 2024 ループス腎炎ガイドライン（診断と治療の章立て、反応の定義）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-592
    source: 'KDIGO Lupus Nephritis Work Group. KDIGO 2024 Clinical Practice Guideline for the management of LUPUS NEPHRITIS. Kidney Int. 2024;105(1S):S1-S69'
    doi: 10.1016/j.kint.2023.09.002
    pmid: '38182286'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2023.09.002
    source_license: CC BY-NC-ND 4.0（ガイドライン本文の著作権表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 各クラスの組織学的定義そのものは ISN/RPS 分類（2018年改訂で Class IV の S/G 細分が廃止され、活動性・慢性化指数が全クラスに適用されることになった）に従うものであり、本ガイドラインで定義の詳細までは確認していない。定義を扱うカードが要る場合は ISN/RPS 改訂報告を別途出典にすること。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-336 (id: Jlvnl-k)'
    kokushi: 医学各論 Ⅷ-1-D-②（全身性エリテマトーデス<SLE>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-025
  domain: GN
  subdomain: ループス腎炎
  assertion:
    plain_statement_ja: 活動性の Class III または Class IV のループス腎炎（膜性成分の合併を含む）への初期治療として、KDIGO の2024年ガイドラインは、グルココルチコイドに次のいずれか1つを組み合わせることを推奨している（推奨10.2.3.1.1、強さ1・確実性B）。ミコフェノール酸誘導体、低用量の静注シクロホスファミド、ベリムマブとミコフェノール酸誘導体または低用量静注シクロホスファミドの併用、あるいは腎機能が著しく低下していない（eGFR 45 mL/min/1.73m² 以上）場合のミコフェノール酸誘導体とカルシニューリン阻害薬の併用である。あわせて、禁忌がない限りループス腎炎を含む SLE 患者全員にヒドロキシクロロキン（または同等の抗マラリア薬）を使うことが推奨されている（推奨10.2.1.1、1C）。
    condition:
      region: 国際
      study: KDIGO 2024 ループス腎炎ガイドラインの推奨文
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-592
    source: 'KDIGO Lupus Nephritis Work Group. KDIGO 2024 Clinical Practice Guideline for the management of LUPUS NEPHRITIS. Kidney Int. 2024;105(1S):S1-S69'
    doi: 10.1016/j.kint.2023.09.002
    pmid: '38182286'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2023.09.002
    source_license: CC BY-NC-ND 4.0（ガイドライン本文の著作権表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 推奨の強さとエビデンスの確実性はガイドライン本文の表記どおりに書いた。ここに挙げた薬剤（ミコフェノール酸誘導体、シクロホスファミド、ベリムマブ、カルシニューリン阻害薬、ヒドロキシクロロキン）のループス腎炎に対する国内の承認・保険適用の範囲は未確認であり、取り込み時に添付文書で確認が必要。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-336 (id: Jlvnl-k)'
    kokushi: 医学各論 Ⅷ-1-D-②（全身性エリテマトーデス<SLE>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-026
  domain: GN
  subdomain: ループス腎炎
  assertion:
    plain_statement_ja: 生検で確認された活動性ループス腎炎の成人448例を対象とした104週間の二重盲検試験（BLISS-LN、21か国107施設）では、標準治療（ミコフェノール酸誘導体、またはシクロホスファミドとアザチオプリンの逐次療法）にベリムマブ（10 mg/kg 静注）を上乗せした群で、主要腎反応（尿蛋白/クレアチニン比0.7以下、eGFR が再燃前の値から20%を超えて低下していないこと、救援療法なし）を達成した割合がプラセボ群より高かった（43% 対 32%、オッズ比1.6）。完全腎反応は30% 対 20%（オッズ比1.7）で、腎関連イベントまたは死亡のリスクはベリムマブ群で低かった（ハザード比0.51）。
    condition:
      region: 国際
      study: 第3相多施設二重盲検ランダム化比較試験（BLISS-LN、448例、104週間）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-593
    source: 'Furie R, et al. Two-Year, Randomized, Controlled Trial of Belimumab in Lupus Nephritis. N Engl J Med. 2020;383(12):1117-1128'
    doi: 10.1056/NEJMoa2001180
    pmid: '32937045'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2001180
    source_license: 出版社の利用条件（NEJM。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ベリムマブの国内の承認・保険適用（全身性エリテマトーデスに対する適応の範囲と腎炎への扱い）は未確認であり、取り込み時に PMDA の添付文書で確認が必要。反応の定義は試験の主要評価項目の定義による。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-336 (id: Jlvnl-k)'
    kokushi: 医学各論 Ⅷ-1-D-②（全身性エリテマトーデス<SLE>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-027
  domain: GN
  subdomain: 顕微鏡的多発血管炎
  assertion:
    plain_statement_ja: 腎病変を伴う顕微鏡的多発血管炎の新規患者124例（末期腎不全の例を除く）を後方視的に調べた研究では、診断時の血清クレアチニン500 μmol/L 以上が腎生存の独立した悪化因子であり（ハザード比8.24）、免疫抑制治療は腎生存の保護因子だった（ハザード比0.35）。死亡については、65歳以上（ハザード比2.44）、血清クレアチニン500 μmol/L 以上（同2.21）、間質性肺疾患の合併（同2.37）が独立した予測因子だった。診断時のクレアチニン値は、末期腎不全への移行またはクレアチニン倍化の予測で ROC 曲線下面積0.870を示した。
    condition:
      region: 中国
      study: 単一施設の後方視コホート研究（腎病変を伴う顕微鏡的多発血管炎124例、2012〜2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-594
    source: 'Shi J, Shen Q, Chen XM, Du XG. Clinical characteristics and outcomes in microscopic polyangiitis patients with renal involvement: a study of 124 Chinese patients. BMC Nephrol. 2019;20:339'
    doi: 10.1186/s12882-019-1535-3
    pmid: '31477033'
    pmcid: PMC6719371
    url: https://doi.org/10.1186/s12882-019-1535-3
    source_license: CC BY 4.0（Crossref の license 欄と誌面の Open Access 表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 中国の単一施設コホートの結果であり、日本の患者集団への外挿には注意が要る。免疫抑制治療の具体的なレジメン別の効果はこの研究では分けて示されていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-337 (id: Jlvnl-s)'
    kokushi: 医学各論 Ⅷ-1-D-①（顕微鏡的多発血管炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-028
  domain: GN
  subdomain: ANCA関連血管炎
  assertion:
    plain_statement_ja: 重症の ANCA 関連血管炎患者197例を対象としたランダム化試験（RAVE）では、リツキシマブ（375 mg/m² を週1回、4週間投与）は、寛解導入の主要評価項目（6か月時点で病勢が寛解しプレドニゾンを中止できていること）について、連日のシクロホスファミド内服に対して非劣性だった（達成率64% 対 53%）。再発例に限るとリツキシマブ群の達成率が高かった（67% 対 42%）。主要な腎病変のある患者でもリツキシマブはシクロホスファミドと同等の効果を示し、有害事象の発生率に両群で有意な差はなかった。
    condition:
      region: 国際
      study: 多施設ランダム化二重盲検非劣性試験（RAVE、197例、9施設）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-595
    source: 'Stone JH, et al. Rituximab versus Cyclophosphamide for ANCA-Associated Vasculitis. N Engl J Med. 2010;363(3):221-232'
    doi: 10.1056/NEJMoa0909905
    pmid: '20647199'
    pmcid: PMC3137658
    url: https://doi.org/10.1056/NEJMoa0909905
    source_license: 出版社の利用条件（NEJM。Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: リツキシマブとシクロホスファミドの国内の承認・保険適用（ANCA 関連血管炎に対する適応の範囲）は未確認であり、取り込み時に添付文書で確認が必要。対象には顕微鏡的多発血管炎と多発血管炎性肉芽腫症の両方が含まれ、腎病変に限った試験ではない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-337 (id: Jlvnl-s)'
    kokushi: 医学各論 Ⅷ-1-D-①（顕微鏡的多発血管炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-029
  domain: GN
  subdomain: 多発血管炎性肉芽腫症
  assertion:
    plain_statement_ja: 活動性の腎病変を伴う Wegener 肉芽腫症（現在の多発血管炎性肉芽腫症）患者94例の腎生検では、分節性壊死性糸球体腎炎が85.1%、管外増殖（半月体形成）が91.5%にみられた。生検時の血清クレアチニンは、半月体のある糸球体の割合と相関し（相関係数0.52）、正常な糸球体の割合とは負の相関を示した（同 -0.55）。多変量解析では、正常糸球体の割合だけが腎機能と末期腎不全への進行に関連した。血清クレアチニンが正常で尿蛋白が0.5 g/日未満だった7例でも、全例に半月体がみられ、6例に分節性の糸球体壊死があった。
    condition:
      region: ノルウェー
      study: 腎生検を受けた94例の後方視研究（追跡期間の中央値42.5か月）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-596
    source: 'Aasarød K, Bostad L, Hammerstrøm J, Jørstad S, Iversen BM. Renal histopathology and clinical course in 94 patients with Wegener''s granulomatosis. Nephrol Dial Transplant. 2001;16(5):953-960'
    doi: 10.1093/ndt/16.5.953
    pmid: '11328900'
    pmcid: null
    url: https://doi.org/10.1093/ndt/16.5.953
    source_license: ライセンス表示を確認できず（Crossref のレコードに license 欄なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典のライセンスは未確認のため、取り込み時に出版社ページで確認が必要。2001年の報告で、疾患名は現在の多発血管炎性肉芽腫症に読み替えた。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-337 (id: Jlvnl-s)'
    kokushi: 医学各論 Ⅷ-1-D-⑤（多発血管炎性肉芽腫症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-030
  domain: GN
  subdomain: 抗糸球体基底膜病
  assertion:
    plain_statement_ja: 抗糸球体基底膜（抗GBM）病の連続221例を解析した研究では、発症1年後の患者生存率は72.7%、腎生存率は25.0%だった。血漿交換と副腎皮質ステロイド・シクロホスファミドの併用療法は、患者生存（死亡のハザード比0.31）と腎生存（腎不全のハザード比0.60）の両方で有利だった。発症時の血清クレアチニンは腎不全の独立した予測因子で、1.5 mg/dL を起点に値が倍増するごとにハザード比が2.07上がった。抗GBM抗体値の上昇と ANCA の陽性は、患者死亡の独立した予測因子だった。
    condition:
      region: 中国
      study: 単一施設の後方視研究（抗GBM病221例、1998〜2008年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-597
    source: 'Cui Z, Zhao J, Jia XY, et al. Anti-glomerular basement membrane disease: outcomes of different therapeutic regimens in a large single-center Chinese cohort study. Medicine (Baltimore). 2011;90(5):303-311'
    doi: 10.1097/MD.0b013e31822f6f68
    pmid: '21862934'
    pmcid: null
    url: https://doi.org/10.1097/MD.0b013e31822f6f68
    source_license: ライセンス表示を確認できず（Crossref のレコードに license 欄なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典のライセンスは未確認のため、取り込み時に出版社ページで確認が必要。治療法の比較はランダム化されていない後方視の比較である。シクロホスファミドを含む治療薬の国内の承認・保険適用は未確認。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-335 (id: Jlvnl-w)'
    kokushi: 医学各論 Ⅷ-1-A-②（急速進行性糸球体腎炎症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-031
  domain: GN
  subdomain: IgA血管炎
  assertion:
    plain_statement_ja: Henoch-Schönlein 紫斑病（現在の IgA 血管炎）の小児1,133例を集めた系統的レビューでは、蛋白尿または血尿は34.2%に生じ、出現した時期は診断後4週以内が85%、6週以内が91%、6か月以内が97%だった。永続的な腎障害は、経過中に尿所見が正常だった例では生じず、孤立性の尿異常にとどまった例では1.6%、腎炎またはネフローゼ症候群を発症した例では19.5%にみられた。このため、発症時に尿所見が正常でも、少なくとも6か月間は尿検査を続けることが推奨される。
    condition:
      region: 国際
      study: 小児1,133例・12研究の系統的レビュー（追跡期間6週〜36年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-598
    source: 'Narchi H. Risk of long term renal impairment and duration of follow up recommended for Henoch-Schonlein purpura with normal or minimal urinary findings: a systematic review. Arch Dis Child. 2005;90(9):916-920'
    doi: 10.1136/adc.2005.074641
    pmid: '15871983'
    pmcid: PMC1720564
    url: https://doi.org/10.1136/adc.2005.074641
    source_license: ライセンス表示を確認できず（Crossref のレコードに license 欄なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典のライセンスは未確認のため、取り込み時に出版社ページで確認が必要。対象は、診断時に腎炎・ネフローゼ症候群・腎不全を呈していなかった小児であり、成人や発症時に腎病変が強い例にはそのまま当てはまらない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-333 (id: Jlvnl-Y)'
    kokushi: 医学各論 Ⅷ-1-C-②（IgA血管炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-032
  domain: GN
  subdomain: アミロイド腎症
  assertion:
    plain_statement_ja: 免疫グロブリン軽鎖（AL）アミロイドーシスでは、腎臓は患者の約70%で侵される。新たに診断された AL アミロイドーシスの腎病変について、尿蛋白5 g/24時間超と eGFR 50 mL/min/1.73m² 未満が透析への進行を最もよく予測する指標だった。尿蛋白がこの閾値以下で eGFR が閾値以上の低リスク例では、3年時点の透析移行は検証集団を含め0〜4%だったのに対し、尿蛋白が多く eGFR が低い高リスク例では60〜85%だった。治療開始6か月時点で、尿蛋白が30%以上減るか0.5 g/24時間未満になり、かつ腎の進行（eGFR の25%以上の低下）がないことが、腎反応の基準とされた。
    condition:
      region: 欧州
      study: イタリアとドイツの2施設の新規診断例（検証集団を含め計732例）による腎病期と反応基準の検証研究
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-599
    source: 'Palladini G, et al. A staging system for renal outcome and early markers of renal response to chemotherapy in AL amyloidosis. Blood. 2014;124(15):2325-2332'
    doi: 10.1182/blood-2014-04-570010
    pmid: '25115890'
    pmcid: null
    url: https://doi.org/10.1182/blood-2014-04-570010
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 病期と反応の基準値は出典の解析結果から読み取った（表・基準の読み取りに相当）。対象は AL アミロイドーシスであり、AA アミロイドーシスには当てはまらない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-334 (id: Jlvnl-g)'
    kokushi: 医学各論 Ⅷ-1-C-③（アミロイド腎症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-033
  domain: GN
  subdomain: 二次性膜性腎症
  assertion:
    plain_statement_ja: 膜性腎症240例のコホートでは、腎生検の時点またはその後1年以内に悪性腫瘍が見つかった患者が24例あり、一般集団と比べた悪性腫瘍の発生は男性で標準化発生比9.8、女性で12.3と有意に高かった。悪性腫瘍の頻度は年齢とともに上がり、喫煙者に多かった。悪性腫瘍を伴う膜性腎症では糸球体内に浸潤する炎症細胞が特発性より多く、1糸球体あたり8個をカットオフとすると、悪性腫瘍を伴う例を感度92%、特異度75%で区別できた。悪性腫瘍が寛解した例では蛋白尿の減少と強く関連していた。
    condition:
      region: 欧州
      study: 膜性腎症240例のコホート研究（悪性腫瘍24例）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-600
    source: 'Lefaucheur C, et al. Membranous nephropathy and cancer: Epidemiologic evidence and determinants of high-risk cancer association. Kidney Int. 2006;70(8):1510-1517'
    doi: 10.1038/sj.ki.5001790
    pmid: '16941021'
    pmcid: null
    url: https://doi.org/10.1038/sj.ki.5001790
    source_license: Elsevier の利用条件（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: このカードは悪性腫瘍に伴う二次性膜性腎症についてのもので、薬剤や感染症に伴う二次性の頻度はこの出典では扱っていない。2006年のコホートであり、PLA2R 抗体が普及する前の集団である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-1-C-④（二次性膜性腎症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-034
  domain: GN
  subdomain: ループス腎炎
  assertion:
    plain_statement_ja: 全身性エリテマトーデスの患者で腎病変を調べるときは、血清クレアチニンと eGFR、尿検査（試験紙と尿沈渣）、尿蛋白クレアチニン比、抗 dsDNA 抗体と補体を、発症時と定期的な経過観察のたびに測定する。KDIGO の2024年ガイドラインの診断フローチャートでは、異常な蛋白尿や尿沈渣、または eGFR の低下があれば蛋白尿を定量し、24時間尿蛋白が500 mg/日以上であれば腎生検を検討する流れになっている。尿沈渣の異常としては、有棘赤血球が5%以上、赤血球円柱や白血球円柱が挙げられ、ほかに説明のつかない eGFR の低下も生検を考える契機になる。
    condition:
      region: 国際
      study: KDIGO 2024 ループス腎炎ガイドラインの診断フローチャート（図1）とプラクティスポイント10.1.1
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-592
    source: 'KDIGO Lupus Nephritis Work Group. KDIGO 2024 Clinical Practice Guideline for the management of LUPUS NEPHRITIS. Kidney Int. 2024;105(1S):S1-S69'
    doi: 10.1016/j.kint.2023.09.002
    pmid: '38182286'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2023.09.002
    source_license: CC BY-NC-ND 4.0（ガイドライン本文の著作権表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 生検を検討する尿蛋白の閾値はガイドラインのフローチャート（図）から読み取った（図から読み取り）。生検の実施は尿所見・腎機能・全身の活動性をあわせて判断するもので、閾値だけで決まるものではない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-336 (id: Jlvnl-k)'
    kokushi: 医学各論 Ⅷ-1-D-②（全身性エリテマトーデス<SLE>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-035
  domain: GN
  subdomain: 関節リウマチの腎障害
  assertion:
    plain_statement_ja: 関節リウマチの患者に腎生検を行った156例（1990〜2019年）の解析では、腎病変の主なものは膜性腎症、腎硬化症、AA アミロイドーシス、IgA 腎症の4つだった。AA アミロイドーシスは21例にみられ、時期別では1990年代に7例、2000年代に10例、2010年代に4例で、2015年以降は新たな例がなかった。AA アミロイドーシスの21例はいずれも生物学的製剤やメトトレキサートによる治療を受けておらず、そのうち15例が透析を必要とし、13例が死亡した。生物学的製剤やメトトレキサートが使われるようになった時代には、ほかの腎病変も含めて透析への進行は減った。
    condition:
      region: 日本
      study: 単一施設で腎生検を受けた関節リウマチ患者156例の後方視解析
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-601
    source: 'Sawamura M, Sawa N, Yamanouchi M, Ikuma D, Sekine A, Mizuno H, et al. Use of biologic agents and methotrexate improves renal manifestation and outcome in patients with rheumatoid arthritis: a retrospective analysis. Clin Exp Nephrol. 2022;26(4):341-349'
    doi: 10.1007/s10157-021-02160-2
    pmid: '34846624'
    pmcid: PMC8930889
    url: https://doi.org/10.1007/s10157-021-02160-2
    source_license: CC BY 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 腎生検を受けた患者に限った集計であり、関節リウマチ全体での腎障害の頻度を示すものではない。薬剤性の腎障害（鎮痛薬や抗リウマチ薬による間質性腎炎など）は、この生検集計では主要な病変としては扱われていない。メトトレキサートや生物学的製剤の国内の承認・保険適用は未確認。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-1-D-④（関節リウマチ、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-036
  domain: GN
  subdomain: Alport症候群
  assertion:
    plain_statement_ja: Alport 症候群は IV 型コラーゲンの異常による遺伝性の腎疾患で、専門家ガイドラインでは、遺伝学的検査が診断と遺伝形式の判定の標準的な方法とされる。X連鎖型では、罹患した男性の母親の多くも発症者であり、本人を同定して経過を追う必要があるとされる。罹患した母親は自分自身が腎不全になるリスクを持つため、腎移植の生体ドナーになることは勧められない。常染色体劣性型でも同様に、家族内での発症者の把握が重要になる。
    condition:
      region: 国際
      study: Alport 症候群と菲薄基底膜腎症の専門家ガイドライン（推奨18項目、エビデンスは専門家意見と記述研究が中心）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-602
    source: 'Savige J, Gregory M, Gross O, Kashtan C, Ding J, Flinter F. Expert guidelines for the management of Alport syndrome and thin basement membrane nephropathy. J Am Soc Nephrol. 2013;24(3):364-375'
    doi: 10.1681/ASN.2012020148
    pmid: '23349312'
    pmcid: null
    url: https://doi.org/10.1681/ASN.2012020148
    source_license: ライセンス表示を確認できず（Crossref のレコードに license 欄なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典のライセンスは未確認のため、取り込み時に出版社ページで確認が必要。このガイドラインの推奨は、ランダム化試験ではなく専門家意見と記述研究に基づく水準のものである。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-1-F-①（Alport症候群、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-037
  domain: GN
  subdomain: Alport症候群
  assertion:
    plain_statement_ja: Alport 症候群の専門家ガイドラインでは、X連鎖型の男性と常染色体劣性型の患者に対して、レニン・アンジオテンシン系の阻害による治療を行い、蛋白尿が現れる前から開始することもありうるとされている。これは、腎機能の悪化を早い段階から抑えることを狙った方針で、遺伝学的検査による診断と遺伝形式の確定が前提になる。罹患した母親を含む家族内の発症者でも、腎機能と尿所見の経過観察が続けられる。
    condition:
      region: 国際
      study: Alport 症候群と菲薄基底膜腎症の専門家ガイドラインの治療推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-602
    source: 'Savige J, Gregory M, Gross O, Kashtan C, Ding J, Flinter F. Expert guidelines for the management of Alport syndrome and thin basement membrane nephropathy. J Am Soc Nephrol. 2013;24(3):364-375'
    doi: 10.1681/ASN.2012020148
    pmid: '23349312'
    pmcid: null
    url: https://doi.org/10.1681/ASN.2012020148
    source_license: ライセンス表示を確認できず（Crossref のレコードに license 欄なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードは早期の RAS 阻害についての専門家ガイドラインの推奨を記したもので、早期介入を検証した個別のランダム化試験（小児を対象に ACE 阻害薬を調べた試験など）の数値はこの出典には含まれていない。試験の数値を扱う場合はその試験を別途出典として確認が必要。RAS 阻害薬の Alport 症候群に対する国内の承認・保険適用は未確認。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-1-F-①（Alport症候群、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-038
  domain: GN
  subdomain: 基底膜菲薄化症候群
  assertion:
    plain_statement_ja: 基底膜菲薄化症候群（菲薄基底膜腎症）は、糸球体基底膜が薄くなることによる持続性の血尿をみる病態で、専門家ガイドラインでは、症例によっては X連鎖型 Alport 症候群を除外するために遺伝学的検査を検討するとされている。これは、菲薄基底膜腎症とされる人の中に、Alport 症候群の原因遺伝子の異常を持つ人が含まれうるためで、家族歴や経過によっては Alport 症候群として家族内発症者の把握と経過観察が必要になる。
    condition:
      region: 国際
      study: Alport 症候群と菲薄基底膜腎症の専門家ガイドラインの診断推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-602
    source: 'Savige J, Gregory M, Gross O, Kashtan C, Ding J, Flinter F. Expert guidelines for the management of Alport syndrome and thin basement membrane nephropathy. J Am Soc Nephrol. 2013;24(3):364-375'
    doi: 10.1681/ASN.2012020148
    pmid: '23349312'
    pmcid: null
    url: https://doi.org/10.1681/ASN.2012020148
    source_license: ライセンス表示を確認できず（Crossref のレコードに license 欄なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典のライセンスは未確認のため、取り込み時に出版社ページで確認が必要。菲薄基底膜腎症そのものの長期予後の数値はこの出典（ガイドライン抄録）では確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-1-F-②（基底膜菲薄化症候群<良性家族性血尿>、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-039
  domain: GN
  subdomain: Fabry病
  assertion:
    plain_statement_ja: 酵素補充療法を受けていない成人 Fabry 病患者462例（男性121例、女性341例）の登録データでは、腎機能の急速な低下（eGFR が年1 mL/min/1.73m² を超える速さで下がること）は男性の71%（121例中86例）にみられたが、女性では39%だった。尿蛋白/クレアチニン比が高い患者ほど低下は速く、比が1.5を超える男性では eGFR が平均で年5.6 mL/min/1.73m² 下がった。回帰モデルでも、尿蛋白/クレアチニン比が腎疾患進行の最も重要な指標であり、女性では診断時の eGFR の低さと年齢も進行に関連した。
    condition:
      region: 国際
      study: Fabry Registry に登録された未治療成人462例の自然経過データ（eGFR を12か月以上にわたり2回以上測定）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-603
    source: 'Wanner C, Oliveira JP, Ortiz A, Mauer M, Germain DP, Linthorst GE, et al. Prognostic indicators of renal disease progression in adults with Fabry disease: natural history data from the Fabry Registry. Clin J Am Soc Nephrol. 2010;5(12):2220-2228'
    doi: 10.2215/CJN.04340510
    pmid: '20813854'
    pmcid: PMC2994083
    url: https://doi.org/10.2215/CJN.04340510
    source_license: ライセンス表示を確認できず（Crossref のレコードに license 欄なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典のライセンスは未確認のため、取り込み時に出版社ページで確認が必要。登録研究の未治療例の解析であり、酵素補充療法が普及した現在の患者集団とは背景が異なる可能性がある。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-1-F-③（Fabry病、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GN-040
  domain: GN
  subdomain: Fabry病
  assertion:
    plain_statement_ja: 酵素補充療法を受けていた成人 Fabry 病患者57例を対象とした18か月のランダム化試験（ATTRACT）では、ミガーラスタットに反応する（amenableな）GLA 変異を持つ患者で、経口の薬理学的シャペロン薬ミガーラスタットへの切り替えは、酵素補充療法の継続と比べて腎機能への影響が同等だった。あらかじめ定めた腎・心・脳血管イベントの発生は、ミガーラスタット群で29%、酵素補充療法群で44%だった。左室心筋重量係数はミガーラスタット群で有意に低下し（-6.6 g/m²）、血漿グロボトリアオシルスフィンゴシンは切り替え後も低く安定していた。
    condition:
      region: 国際
      study: 第3相ランダム化実薬対照試験（ATTRACT、57例、18か月、酵素補充療法からの切り替え）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-604
    source: 'Hughes DA, et al. Oral pharmacological chaperone migalastat compared with enzyme replacement therapy in Fabry disease: 18-month results from the randomised phase III ATTRACT study. J Med Genet. 2017;54(4):288-296'
    doi: 10.1136/jmedgenet-2016-104178
    pmid: '27834756'
    pmcid: PMC5502308
    url: https://doi.org/10.1136/jmedgenet-2016-104178
    source_license: CC BY-NC 4.0（PMC ページの表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ミガーラスタットが使えるのは反応性のある GLA 変異を持つ患者に限られ、試験では変異の反応性を細胞アッセイで判定した。ミガーラスタットと酵素補充療法（アガルシダーゼ製剤）の国内の承認・保険適用の範囲は未確認であり、取り込み時に添付文書で確認が必要。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-1-F-③（Fabry病、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-001
  domain: KT
  subdomain: 高血圧性腎硬化症
  assertion:
    plain_statement_ja: 腎硬化症（ネフロアンギオスクレローシス）は慢性の本態性高血圧に伴う腎疾患で、確定診断は腎生検によるが、生検は診断が疑わしい例や非典型的な経過の例に限られ、多くの場合は臨床的な推定診断にとどまる。有病率と発症率は不明とされる。
    condition:
      region: 国際
      study: 総説（2023年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-605
    source: 'Heras Benito M. Nephroangiosclerosis: an update. Hipertens Riesgo Vasc. 2023;40(2):98-103'
    doi: 10.1016/j.hipert.2022.07.004
    pmid: '36050216'
    pmcid: null
    url: https://doi.org/10.1016/j.hipert.2022.07.004
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 単一の総説に基づく記載で、日本の集団での有病率や進行速度の数値はこの出典では確認していない。近年の遺伝学研究により、高血圧性腎疾患という用語の再定義が議論されている点も出典に記されている。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-327 (id: Jlvnl90)'
    kokushi: 医学各論 Ⅷ-2-A-①（高血圧性腎硬化症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-002
  domain: KT
  subdomain: 悪性腎硬化症、悪性高血圧症
  assertion:
    plain_statement_ja: 悪性高血圧に伴う血栓性微小血管症で腎生検を受けた276例のコホートでは、185例（67.0%）に1 g/24時間以上の有意な蛋白尿がみられ、有意蛋白尿は腎代替療法導入の独立した予測因子だった（調整ハザード比1.30）。
    condition:
      region: 中国
      study: 2008〜2023年に腎生検で評価された悪性高血圧関連血栓性微小血管症276例の観察コホート研究
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-606
    source: 'Shi W, Lian X, Li W, Lian R, Yu S, Dai Z. Significant proteinuria as a predictor of renal prognosis in malignant hypertension patients with thrombotic microangiopathy: a prospective cohort study. BMC Nephrol. 2025;26(1):513'
    doi: 10.1186/s12882-025-04407-6
    pmid: '40898080'
    pmcid: PMC12406467
    url: https://doi.org/10.1186/s12882-025-04407-6
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 腎生検を受けた血栓性微小血管症合併例に限った集団であり、悪性高血圧全体の頻度や予後をそのまま示すものではない。日本の集団での検証はこの出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-2-A-③（悪性腎硬化症、悪性高血圧症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-003
  domain: KT
  subdomain: 腎血管性高血圧症
  assertion:
    plain_statement_ja: 動脈硬化性腎動脈狭窄は二次性高血圧の最も多い原因で、進行性の腎機能低下やフラッシュ肺水腫などの心血管合併症と関連する。腎の側の評価では、スクリーニング検査としてドプラ超音波検査、CT血管造影、MR血管造影が用いられる。
    condition:
      region: 米国
      study: 総説（2015年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-607
    source: 'Tafur-Soto JD, White CJ. Renal artery stenosis. Cardiol Clin. 2015;33(1):59-73'
    doi: 10.1016/j.ccl.2014.09.006
    pmid: '25439331'
    pmcid: null
    url: https://doi.org/10.1016/j.ccl.2014.09.006
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 境界の方針に沿い、腎の側の評価（腎機能と画像）に絞った記載で、高血圧そのものの管理や血行再建の適応判断は循環器側の範囲として扱っていない。各画像検査の感度・特異度の数値はこの出典の抄録では確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-328 (id: Jlvnl94)'
    kokushi: 医学各論 Ⅷ-2-A-②（腎血管性高血圧症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-004
  domain: KT
  subdomain: 腎梗塞
  assertion:
    plain_statement_ja: 腎梗塞438例の症例集積では、原因は心原性が55.7%と最も多く、特発性30.1%、腎動脈損傷7.5%、過凝固状態6.6%だった。経過では急性腎障害が20.1%に起こり、新規にeGFR 60 mL/min/1.73m²未満となった例が10.9%、末期腎不全への進行が2.1%、入院中の死亡が5%だった。
    condition:
      region: 韓国
      study: 1993〜2013年に9施設で画像診断された腎梗塞438例の後方視症例集積（追跡期間中央値20.0か月）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-608
    source: 'Oh YK, Yang CW, Kim YL, Kang SW, Park CW, et al. Clinical Characteristics and Outcomes of Renal Infarction. Am J Kidney Dis. 2016;67(2):243-50'
    doi: 10.1053/j.ajkd.2015.09.019
    pmid: '26545635'
    pmcid: null
    url: https://doi.org/10.1053/j.ajkd.2015.09.019
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 後方視研究であり、一部の例では原因機序を明確に決められていないと出典に記されている。抗凝固薬などの治療薬の国内の承認・保険適用は本カードでは確認していない（取り込み時に確認が必要）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-2-A-④（腎梗塞、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-005
  domain: KT
  subdomain: コレステロール塞栓症
  assertion:
    plain_statement_ja: アテローム塞栓性腎疾患354例の多施設コホートでは、男性が83%、70歳超が60%を占め、自然発症は23.5%だった。平均2年の追跡で116例が透析を要し、102例が死亡した。スタチンを使用していた例では、透析と死亡のリスクが50%低かった。
    condition:
      region: 欧州
      study: イタリアの多施設で登録されたアテローム塞栓性腎疾患354例の前向きコホート（平均追跡2年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-609
    source: 'Scolari F, Ravani P, Gaggi R, Santostefano M, Rollino C, et al. The challenge of diagnosing atheroembolic renal disease: clinical features and prognostic factors. Circulation. 2007;116(3):298-304'
    doi: 10.1161/CIRCULATIONAHA.106.680991
    pmid: '17606842'
    pmcid: null
    url: https://doi.org/10.1161/CIRCULATIONAHA.106.680991
    source_license: 出版社の著作物（Crossref のレコードに license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: スタチンと転帰の関連は観察研究の解析であり、因果関係を示すものではない。スタチンを含む治療薬の国内の承認・保険適用は本カードでは確認していない（取り込み時に確認が必要）。2007年の研究であり、現在の治療環境とは異なる可能性がある。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-2-A-⑤（コレステロール塞栓症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-006
  domain: KT
  subdomain: 強皮症腎クリーゼ
  assertion:
    plain_statement_ja: 全身性強皮症606例の観察研究では、20例（3.3%）が強皮症腎クリーゼを発症した。全例がACE阻害薬で治療されたが、発症1年で55%が末期腎不全に進行し、生存率は1年70%、5年50%で、腎クリーゼ関連の死亡率は35%だった。
    condition:
      region: イタリア
      study: 1980〜2005年に全身性強皮症で受診した606例の長期観察研究（腎クリーゼ発症20例）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-610
    source: 'Cozzi F, Marson P, Cardarelli S, Favaro M, Tison T, et al. Prognosis of scleroderma renal crisis: a long-term observational study. Nephrol Dial Transplant. 2012;27(12):4398-403'
    doi: 10.1093/ndt/gfs317
    pmid: '22859795'
    pmcid: null
    url: https://doi.org/10.1093/ndt/gfs317
    source_license: 出版社の著作物（Crossref のレコードに license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ACE阻害薬は国内で承認された薬剤だが、強皮症腎クリーゼに対する国内の適応・保険適用は未確認（取り込み時に添付文書で確認が必要）。1980〜2005年の症例であり、現在の治療成績とは異なる可能性がある。境界の方針に沿い、腎クリーゼに絞った記載である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-2-A-⑥（全身性強皮症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-007
  domain: KT
  subdomain: 腎静脈血栓症
  assertion:
    plain_statement_ja: ネフローゼ症候群512例にCTによる前向き評価を行った研究では、肺塞栓症か腎静脈血栓症を35%に認め、腎静脈血栓症は505例中112例（22%）にみられた。合併は成人（38%）で小児（19%）より多く、関連する組織型では膜性腎症が最も多かった。
    condition:
      region: 中国
      study: ネフローゼ症候群512例（うち小児80例）にCT肺血管造影と腎CT静脈造影を行った前向き研究
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-611
    source: 'Zhang LJ, Zhang Z, Li SJ, Meinel FG, Nance JW Jr, et al. Pulmonary embolism and renal vein thrombosis in patients with nephrotic syndrome: prospective evaluation of prevalence and risk factors with CT. Radiology. 2014;273(3):897-906'
    doi: 10.1148/radiol.14140121
    pmid: '25072187'
    pmcid: null
    url: https://doi.org/10.1148/radiol.14140121
    source_license: 出版社の著作物（Crossref のレコードに license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 全例にCTを行った単一研究の頻度であり、症状があって検査された集団での頻度とは異なる。ネフローゼ症候群以外の原因（腫瘍、外傷など）による腎静脈血栓症の頻度はこの出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-2-A-⑦（腎静脈血栓症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-008
  domain: KT
  subdomain: 結節性多発動脈炎
  assertion:
    plain_statement_ja: 結節性多発動脈炎の腎病変4例の画像検討では、CTとMRの共通所見として、腎のびまん性腫大、ダイナミック造影で多発する小さな楔状の低増強域、平衡相での皮髄境界の不明瞭化がみられ、腎動脈造影では全例に多発する微小動脈瘤を認めた。微小動脈瘤が示されない場合、画像所見は腎盂腎炎と似て鑑別が難しい。
    condition:
      region: 日本
      study: 結節性多発動脈炎と診断された4例のCT・MR画像の後方視検討
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-612
    source: 'Ozaki K, Miyayama S, Ushiogi Y, Matsui O. Renal involvement of polyarteritis nodosa: CT and MR findings. Abdom Imaging. 2009;34(2):265-70'
    doi: 10.1007/s00261-008-9377-7
    pmid: '18317834'
    pmcid: null
    url: https://doi.org/10.1007/s00261-008-9377-7
    source_license: Springer の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 4例のみの検討であり、頻度や典型像の一般化には限界がある。腎障害の進行や治療への反応の数値はこの出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-2-A-⑧（結節性多発動脈炎、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-009
  domain: KT
  subdomain: 急性尿細管壊死
  assertion:
    plain_statement_ja: 急性尿細管壊死は、虚血または腎毒性物質によって生じる尿細管の障害で、急性腎障害の腎性の原因として一般的である。急性腎障害は腎前性・腎性・腎後性に分類され、血清クレアチニンと尿量で病期が定められ、慢性腎臓病への移行リスクの増加と関連する。
    condition:
      region: 国際
      study: 総説（2023年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-613
    source: 'Turgut F, Awad AS, Abdel-Rahman EM. Acute Kidney Injury: Medical Causes and Pathogenesis. J Clin Med. 2023;12(1):375'
    doi: 10.3390/jcm12010375
    pmid: '36615175'
    pmcid: PMC9821234
    url: https://doi.org/10.3390/jcm12010375
    source_license: CC BY 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: この出典は急性腎障害全体の総説であり、急性尿細管壊死に特有の経過（乏尿期・利尿期などの期間や回復率）の数値は確認していない。腎毒性薬剤の国内の承認・保険適用は本カードでは確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-2-B-①（急性尿細管壊死、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-010
  domain: KT
  subdomain: 急性間質性腎炎
  assertion:
    plain_statement_ja: 急性間質性腎炎は急性腎障害の原因として頻度が高く、急性腎障害のために腎生検を受けた例の15〜27%を占める。現在の原因として薬剤性が最も多く、抗菌薬と非ステロイド性抗炎症薬が主な原因薬剤である。発熱、皮疹、関節痛、末梢血の好酸球増多といった腎外症状が診断の手がかりになるが、症状に乏しい例も少なくない。病理ではリンパ球や好酸球などによる間質への炎症細胞浸潤が特徴である。
    condition:
      region: 国際
      study: 総説（2010年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-614
    source: 'Praga M, González E. Acute interstitial nephritis. Kidney Int. 2010;77(11):956-61'
    doi: 10.1038/ki.2010.89
    pmid: '20336051'
    pmcid: null
    url: https://doi.org/10.1038/ki.2010.89
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 15〜27%は急性腎障害で生検された集団での割合であり、急性腎障害全体に占める割合ではない。原因薬剤の国内の承認・保険適用は本カードでは確認していない（取り込み時に確認が必要）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-330 (id: Jlvnl-E)'
    kokushi: 医学各論 Ⅷ-2-B-②（急性間質性腎炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-011
  domain: KT
  subdomain: 急性間質性腎炎
  assertion:
    plain_statement_ja: 薬剤性急性間質性腎炎の治療の基本は、原因薬剤を同定して中止することである。副腎皮質ステロイドは、診断後7日以内に開始する早期投与で腎機能の回復を改善し、慢性腎障害のリスクを下げるとされる一方、間質の線維化が進んだ後に開始した遅い投与では効果が乏しい。
    condition:
      region: 国際
      study: 総説（2010年）。ステロイドの効果はランダム化比較試験ではなく観察研究に基づく記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-614
    source: 'Praga M, González E. Acute interstitial nephritis. Kidney Int. 2010;77(11):956-61'
    doi: 10.1038/ki.2010.89
    pmid: '20336051'
    pmcid: null
    url: https://doi.org/10.1038/ki.2010.89
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ステロイドの有効性はこの総説が引用する観察研究に基づき、ランダム化比較試験による裏づけはない。副腎皮質ステロイドの急性間質性腎炎に対する国内の適応・保険適用は未確認（取り込み時に添付文書で確認が必要）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-330 (id: Jlvnl-E)'
    kokushi: 医学各論 Ⅷ-2-B-②（急性間質性腎炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-012
  domain: KT
  subdomain: 骨髄腫腎
  assertion:
    plain_statement_ja: 症候性多発性骨髄腫に伴う急性腎障害の最も多い機序は、モノクローナルな遊離軽鎖が遠位尿細管でウロモジュリンと沈着する軽鎖円柱腎症である。しばしば重症の急性腎障害で発症し、腎機能の回復には、十分な補液と誘因の是正に加え、腎毒性のある遊離軽鎖の産生を速やかに減らす抗形質細胞療法が必要で、新規診断例の標準はボルテゾミブと高用量デキサメタゾンの併用とされる。
    condition:
      region: 国際
      study: 総説（2021年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-615
    source: 'Bridoux F, Leung N, Belmouaz M, Royal V, Ronco P, Nasr SH. Management of acute kidney injury in symptomatic multiple myeloma. Kidney Int. 2021;99(3):570-580'
    doi: 10.1016/j.kint.2020.11.010
    pmid: '33440212'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2020.11.010
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 境界の方針に沿い、腎障害（円柱腎症）に絞った記載で、骨髄腫そのものの診断や血液学的な治療体系は扱っていない。ボルテゾミブやデキサメタゾンを含む治療薬の国内の承認・保険適用は本カードでは確認していない（取り込み時に PMDA の添付文書で確認が必要）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-2-B-③（骨髄腫腎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-013
  domain: KT
  subdomain: 慢性間質性腎炎
  assertion:
    plain_statement_ja: 間質性腎炎では、間質への炎症細胞浸潤が急速に間質の線維化した領域へと移行しうるため、炎症の段階での治療が遅れると慢性の腎障害として残る。急性の薬剤性間質性腎炎が慢性化する経路もこの線維化であり、原因の除去と早期治療が慢性間質性腎炎への進行を防ぐうえで重要である。
    condition:
      region: 国際
      study: 総説（2010年）。急性間質性腎炎の病理経過に基づく記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-614
    source: 'Praga M, González E. Acute interstitial nephritis. Kidney Int. 2010;77(11):956-61'
    doi: 10.1038/ki.2010.89
    pmid: '20336051'
    pmcid: null
    url: https://doi.org/10.1038/ki.2010.89
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは薬剤性急性間質性腎炎から間質線維化への移行を中心に記載した。慢性間質性腎炎の成因全体（鎮痛薬性、自己免疫性、感染症、遺伝性など）の頻度や進行速度の数値は、この出典では確認していない（未解決事項参照）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-330 (id: Jlvnl-E)'
    kokushi: 医学各論 Ⅷ-2-B-④（慢性間質性腎炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-014
  domain: KT
  subdomain: Sjögren症候群
  assertion:
    plain_statement_ja: 原発性Sjögren症候群の腎病変は10%未満と比較的まれで、最も多い病型は形質細胞の浸潤を特徴とする尿細管間質性腎炎である。遠位尿細管性アシドーシス、尿崩症、Gitelman症候群様の異常、Fanconi症候群などの電解質異常を伴うことがあり、糸球体病変はクリオグロブリン血症に伴う膜性増殖性糸球体腎炎が多い。尿細管間質性腎炎の例では腎予後はおおむね良好だが、慢性腎臓病のリスクは高いままである。
    condition:
      region: 欧州
      study: 総説（2016年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-616
    source: 'François H, Mariette X. Renal involvement in primary Sjögren syndrome. Nat Rev Nephrol. 2016;12(2):82-93'
    doi: 10.1038/nrneph.2015.174
    pmid: '26568188'
    pmcid: null
    url: https://doi.org/10.1038/nrneph.2015.174
    source_license: Springer の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頻度10%未満は総説の記載であり、集団や腎病変の定義により変わりうる。日本の集団での頻度はこの出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-330 (id: Jlvnl-E)'
    kokushi: 医学各論 Ⅷ-2-B-⑤（Sjögren症候群、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-015
  domain: KT
  subdomain: IgG4関連腎臓病
  assertion:
    plain_statement_ja: IgG4関連腎臓病では、IgG4陽性形質細胞の浸潤と線維化を伴う尿細管間質性腎炎が主体で、膜性腎症などの糸球体病変を伴うこともある。中高年の男性に多く、唾液腺炎やリンパ節腫脹、1型自己免疫性膵炎などの腎外病変を伴うことが多い。血清IgGとIgG4の高値に加え、IgE高値や低補体血症もしばしばみられる。副腎皮質ステロイドが通常よく効き、腎機能と画像・血清所見が改善するが、治療の遅れは不可逆的な腎不全につながりうる。
    condition:
      region: 日本
      study: 総説（2014年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-617
    source: 'Saeki T, Kawano M. IgG4-related kidney disease. Kidney Int. 2014;85(2):251-7'
    doi: 10.1038/ki.2013.393
    pmid: '24107849'
    pmcid: null
    url: https://doi.org/10.1038/ki.2013.393
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 境界の方針に沿い、腎病変に絞った記載である。副腎皮質ステロイドのIgG4関連腎臓病に対する国内の適応・保険適用は未確認（取り込み時に添付文書で確認が必要）。再発率などの長期経過の数値はこの出典の抄録では確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-330 (id: Jlvnl-E)'
    kokushi: 医学各論 Ⅷ-2-B-⑥（IgG4関連疾患、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-016
  domain: KT
  subdomain: 中毒性腎障害
  assertion:
    plain_statement_ja: 薬剤性の尿細管障害では、薬剤の腎での輸送と蓄積が障害の機序になる。アミノグリコシドは近位尿細管の管腔側からエンドサイトーシスで取り込まれ、テノホビルは基底側の有機アニオントランスポーター、シスプラチンは有機カチオントランスポーターを介して細胞内に蓄積して尿細管を障害する。メトトレキサートなどは尿細管内に結晶として沈着して閉塞と障害を起こす。
    condition:
      region: 米国
      study: 総説（2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-618
    source: 'Perazella MA. Drug-induced acute kidney injury: diverse mechanisms of tubular injury. Curr Opin Crit Care. 2019;25(6):550-557'
    doi: 10.1097/MCC.0000000000000653
    pmid: '31483318'
    pmcid: null
    url: https://doi.org/10.1097/MCC.0000000000000653
    source_license: 出版社の著作物（Crossref のレコードに license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 各薬剤の発症頻度や用量依存性の数値はこの出典の抄録では確認していない。アミノグリコシド、テノホビル、シスプラチン、メトトレキサートの国内の承認・保険適用は本カードでは個別に確認していない（取り込み時に PMDA の添付文書で確認が必要）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-2-B-⑦（中毒性腎障害、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-017
  domain: KT
  subdomain: 尿酸腎症
  assertion:
    plain_statement_ja: 尿酸は1日に産生される量の約70%が腎臓から排泄され、産生が排泄を上回ると高尿酸血症になる。高尿酸血症は、炎症、内皮障害、血管平滑筋の増殖、レニン・アンギオテンシン系の活性化を介して慢性腎臓病の発症と進展に関連するとされ、痛風に伴う腎障害の背景になる。
    condition:
      region: 国際
      study: 総説（2021年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-619
    source: 'Yanai H, Adachi H, Hakoshima M, Katsuyama H. Molecular Biological and Clinical Understanding of the Pathophysiology and Treatments of Hyperuricemia and Its Association with Metabolic Syndrome, Cardiovascular Diseases and Chronic Kidney Disease. Int J Mol Sci. 2021;22(17):9221'
    doi: 10.3390/ijms22179221
    pmid: '34502127'
    pmcid: PMC8431537
    url: https://doi.org/10.3390/ijms22179221
    source_license: CC BY 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 高尿酸血症と慢性腎臓病の因果関係については議論があり、この出典でも関連を示す基礎・臨床の証拠の紹介にとどまる。腫瘍崩壊症候群に伴う急性尿酸腎症の頻度や予防の数値は、この出典では確認していない。尿酸降下薬の国内の承認・保険適用は本カードでは確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-2-B-⑧（尿酸腎症<痛風腎>、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-018
  domain: KT
  subdomain: 尿細管性アシドーシス
  assertion:
    plain_statement_ja: 尿細管性アシドーシスは、非アニオンギャップ型の代謝性アシドーシスの一群で、重炭酸の再吸収や、アンモニアとリン酸による緩衝を介した水素イオンの排泄といった、腎の酸排泄の仕組みのいずれかの障害から生じる。診断では血清と尿の指標を組み合わせ、酸血症に対して腎がどの程度応答できているかを評価して障害の性質を分け、治療方針の決定に使う。未治療では生命を脅かす経過を取りうる。
    condition:
      region: 米国
      study: 2025年の総説（Core Curriculum）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-620
    source: 'Bonner R, Hladik G. Renal Tubular Acidosis: Core Curriculum 2025. Am J Kidney Dis. 2025;85(4):501-512'
    doi: 10.1053/j.ajkd.2024.08.014
    pmid: '39864011'
    pmcid: null
    url: https://doi.org/10.1053/j.ajkd.2024.08.014
    source_license: 出版社の著作物（誌面・レコードに CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは総論であり、各型の診断手順の数値基準（尿アニオンギャップや重炭酸負荷試験の値など）は出典本文の表から読み取る必要があるため、本カードには数値を記載していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-329 (id: Jlvnl-A)；TBL-01-00-319 (id: Jlvnl9A)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ)'
    kokushi: 医学各論 Ⅷ-2-C-①（尿細管性アシドーシス、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-019
  domain: KT
  subdomain: 遠位型尿細管性アシドーシス
  assertion:
    plain_statement_ja: 原発性遠位型尿細管性アシドーシスは、集合管のA型介在細胞の障害により尿の酸性化が進まないために生じ、全身の代謝性アシドーシスがあるにもかかわらず尿pHを十分に下げることができない。高塩素血症と正常のアニオンギャップを伴い、高カルシウム尿、低クエン酸尿、腎石灰化、腎結石、成長遅延、くる病を来しうる。原因遺伝子は、水素イオンATPaseのサブユニットをコードするATP6V1B1とATP6V0A4、および陰イオン交換体AE1をコードするSLC4A1で、治療には早期からの十分な量のアルカリ投与が必要である。
    condition:
      region: 日本
      study: 日本の著者による総説（原発性遠位型が対象）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-621
    source: 'Watanabe T. Improving outcomes for patients with distal renal tubular acidosis: recent advances and challenges ahead. Pediatric Health Med Ther. 2018;9:181-190'
    doi: 10.2147/PHMT.S174459
    pmid: '30588151'
    pmcid: PMC6296208
    url: https://doi.org/10.2147/PHMT.S174459
    source_license: CC BY-NC 3.0（誌面の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典本文では、原因遺伝子が同定できるのは全体の70〜80%程度とされ、残りは原因未同定がありうる。アルカリ療法に用いる製剤の国内の承認・保険適用は本調査では確認していない（国内の適応は未確認）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-329 (id: Jlvnl-A)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ)'
    kokushi: 医学各論 Ⅷ-2-C-①（尿細管性アシドーシス、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-020
  domain: KT
  subdomain: 近位型尿細管性アシドーシス
  assertion:
    plain_statement_ja: 近位型尿細管性アシドーシスは、近位尿細管での重炭酸再吸収の障害により、尿中へ重炭酸が喪失する病態である。重炭酸だけの単独の輸送障害はまれで、多くはリン酸、尿酸、糖、アミノ酸、低分子量蛋白も失うFanconi症候群に伴う。遺伝性は常染色体潜性遺伝が多く、基底膜側のナトリウム重炭酸共輸送体NBCe1の変異と関連する。後天性では薬剤性が最も多く、イホスファミド、バルプロ酸、テノホビルなどが、Fanconi症候群を伴う近位型の原因として報告されている。
    condition:
      region: 国際
      study: 2012年の総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-622
    source: 'Haque SK, Ariceta G, Batlle D. Proximal renal tubular acidosis: a not so rare disorder of multiple etiologies. Nephrol Dial Transplant. 2012;27(12):4273-4287'
    doi: 10.1093/ndt/gfs493
    pmid: '23235953'
    pmcid: PMC3616759
    url: https://doi.org/10.1093/ndt/gfs493
    source_license: 出版社の著作物（誌面・レコードに CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原因薬として挙げたイホスファミド、バルプロ酸、テノホビルなどの国内の承認・保険適用の状況は、本調査では個別に確認していない（国内の適応は未確認）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-329 (id: Jlvnl-A)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ)'
    kokushi: 医学各論 Ⅷ-2-C-①（尿細管性アシドーシス、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-021
  domain: KT
  subdomain: Fanconi症候群
  assertion:
    plain_statement_ja: Fanconi症候群は、近位尿細管の再吸収機能が全般に障害され、重炭酸、リン酸、糖、アミノ酸、低分子量蛋白などが尿中に失われる病態である。遺伝性Fanconi症候群の代表的な原因であるシスチノーシスは、リソソームのシスチン輸送体シスチノシンの欠損による常染色体潜性遺伝の蓄積症で、腎Fanconi症候群が生後1年以内に初発症状として現れることが多い。システアミン治療はリソソーム内のシスチンを減らして腎不全への進行を大きく遅らせるが、確立したFanconi症候群そのものは是正できない。
    condition:
      region: 国際
      study: シスチノーシスに伴う腎Fanconi症候群に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-623
    source: 'Cherqui S, Courtoy PJ. The renal Fanconi syndrome in cystinosis: pathogenic insights and therapeutic perspectives. Nat Rev Nephrol. 2017;13(2):115-131'
    doi: 10.1038/nrneph.2016.182
    pmid: '27990015'
    pmcid: PMC5657490
    url: https://doi.org/10.1038/nrneph.2016.182
    source_license: 出版社の著作物（誌面・レコードに CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: システアミンの国内の承認・保険適用は本調査では確認していない（国内の適応は未確認）。後天性Fanconi症候群（薬剤性など）の細目は本カードの出典の範囲外である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-022
  domain: KT
  subdomain: シスチン尿症
  assertion:
    plain_statement_ja: シスチン尿症は、アミノ酸輸送系b0,+を構成するrBATとb0,+ATの2つのサブユニットをコードする遺伝子の変異による、原発性の遺伝性アミノ酸尿で、多くは常染色体潜性遺伝である。近位尿細管で濾過されたシスチンと二塩基性アミノ酸の再吸収が障害され、溶解度の低いシスチンが析出して結石を形成する。小児の腎結石の原因として一定の割合を占め、治療は再発するシスチン結石の予防を目的に行われる。
    condition:
      region: 国際
      study: 2010年の総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-624
    source: 'Chillarón J, Font-Llitjós M, Fort J, Zorzano A, Goldfarb DS, Nunes V, Palacín M. Pathophysiology and treatment of cystinuria. Nat Rev Nephrol. 2010;6(7):424-434'
    doi: 10.1038/nrneph.2010.69
    pmid: '20517292'
    pmcid: null
    url: https://doi.org/10.1038/nrneph.2010.69
    source_license: 出版社の著作物（誌面・レコードに CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 結石予防に用いる薬剤の国内の承認・保険適用は本調査では確認していない（国内の適応は未確認）。有病率などの疫学数値は資料により差があるため、本カードには記載していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)'
    kokushi: 医学各論 Ⅷ-2-C-②（シスチン尿症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-023
  domain: KT
  subdomain: 腎性尿崩症
  assertion:
    plain_statement_ja: 腎性尿崩症は、集合管がアルギニンバソプレシンに反応できず、アクアポリンを介した水の再吸収が実質的に欠けた状態になるため、尿を濃縮できず、希釈尿が持続的に多量に排泄される病態である。一次性は、バソプレシンV2受容体をコードするAVPR2と、水チャネルであるアクアポリン2をコードするAQP2の変異による。二次性は、生化学的な異常や閉塞性尿路障害、薬剤、とくにリチウムと関連する。治療の方針は、原因を同定することによって決まる。
    condition:
      region: 国際
      study: 2015年の総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-625
    source: 'Bockenhauer D, Bichet DG. Pathophysiology, diagnosis and management of nephrogenic diabetes insipidus. Nat Rev Nephrol. 2015;11(10):576-588'
    doi: 10.1038/nrneph.2015.89
    pmid: '26077742'
    pmcid: null
    url: https://doi.org/10.1038/nrneph.2015.89
    source_license: 出版社の著作物（誌面・レコードに CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原因薬として挙げたリチウム製剤の国内の承認・保険適用は、本調査では確認していない（国内の適応は未確認）。水制限試験などの診断手順の数値基準は本カードには記載していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)'
    kokushi: 医学各論 Ⅷ-2-C-③（腎性尿崩症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-024
  domain: KT
  subdomain: 腎性尿崩症
  assertion:
    plain_statement_ja: 遺伝性の腎性尿崩症には根本的な治療法がなく、治療は、持続的な水分の供給と、塩分などを制限する食事療法、非特異的な薬物療法によって症状を抑えることが中心で、現在の治療選択肢は限られ、効果も部分的にとどまる。従来の薬物療法として、サイアザイド系利尿薬、カリウム保持性利尿薬、インドメタシンなどが、尿量を減らす対症療法として用いられてきた。二次性の場合は、原因への対応が治療方針を左右する。
    condition:
      region: 国際
      study: 遺伝性腎性尿崩症の治療に関する2017年の総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-626
    source: 'Milano S, Carmosino M, Gerbino A, Svelto M, Procino G. Hereditary nephrogenic diabetes insipidus: pathophysiology and possible treatment. An update. Int J Mol Sci. 2017;18(11):2385'
    doi: 10.3390/ijms18112385
    pmid: '29125546'
    pmcid: PMC5713354
    url: https://doi.org/10.3390/ijms18112385
    source_license: CC BY 4.0（誌面の表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: サイアザイド系利尿薬、カリウム保持性利尿薬、インドメタシンの腎性尿崩症に対する国内の保険適用は、本調査では確認していない（国内の適応は未確認で、適応外使用となる可能性がある）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)'
    kokushi: 医学各論 Ⅷ-2-C-③（腎性尿崩症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-025
  domain: KT
  subdomain: Bartter症候群
  assertion:
    plain_statement_ja: Bartter症候群は、ヘンレループの太い上行脚における塩の再吸収障害による遺伝性の尿細管疾患で、人口約100万人に1人とされ、塩の喪失、低カリウム血症、代謝性アルカローシスを来し、血圧は正常から低めで、レニンとアルドステロンは高値となる。原因遺伝子は輸送体ごとに分かれ、NKCC2をコードするSLC12A1、ROMKをコードするKCNJ1、ClC-KbをコードするCLCNKB、バルチンをコードするBSNDなどが知られ、型によって羊水過多や腎石灰化、感音難聴を伴うことがある。
    condition:
      region: ブラジル
      study: ブラジルの著者による総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-627
    source: 'Cunha TDS, Heilberg IP. Bartter syndrome: causes, diagnosis, and treatment. Int J Nephrol Renovasc Dis. 2018;11:291-301'
    doi: 10.2147/IJNRD.S155397
    pmid: '30519073'
    pmcid: PMC6233707
    url: https://doi.org/10.2147/IJNRD.S155397
    source_license: CC BY-NC 3.0（誌面の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率（約100万人に1人）は出典本文の記載に基づく概数で、集団により異なる可能性がある。遺伝子型と表現型の対応は一対一ではなく、出典でも表現型からの推定が第一歩とされている。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ)'
    kokushi: 医学各論 Ⅷ-2-C-④（Bartter症候群、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-026
  domain: KT
  subdomain: Gitelman症候群
  assertion:
    plain_statement_ja: Gitelman症候群は、遠位曲尿細管のサイアザイド感受性ナトリウム・クロライド共輸送体NCCをコードするSLC12A3の不活化変異による、常染色体潜性遺伝の塩喪失性尿細管疾患で、低カリウム性代謝性アルカローシスに、低マグネシウム血症と低カルシウム尿を伴うことが特徴である。多くは思春期から成人期に、偶然の検査所見や軽い非特異的な症状をきっかけに見つかり、治療は、塩分の自由な摂取と、経口のマグネシウムおよびカリウムの補充が中心となる。
    condition:
      region: 国際
      study: KDIGOのコンセンサス会議報告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-628
    source: 'Blanchard A, Bockenhauer D, Bolignano D, et al. Gitelman syndrome: consensus and guidance from a Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference. Kidney Int. 2017;91(1):24-33'
    doi: 10.1016/j.kint.2016.09.046
    pmid: '28003083'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2016.09.046
    source_license: 出版社の著作物（KDIGO 会議報告、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 補充に用いるカリウム・マグネシウム製剤の国内の保険適用は、本調査では確認していない（国内の適応は未確認）。表現型には個人差が大きく、重い症状を伴う例もあることが出典に記載されている。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ)'
    kokushi: 医学各論 Ⅷ-2-C-⑤（Gitelman症候群、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-027
  domain: KT
  subdomain: Liddle症候群
  assertion:
    plain_statement_ja: Liddle症候群は、上皮性ナトリウムチャネルENaCのサブユニットをコードするSCNN1A、SCNN1B、SCNN1Gの生殖細胞系列変異による、常染色体顕性遺伝の低レニン性高血圧である。変異によりチャネルの細胞膜での発現が増えて遠位ネフロンでのナトリウム再吸収が高まるため、若年発症の高血圧、低カリウム血症、代謝性アルカローシス、血漿レニン活性の抑制と低アルドステロンがみられる。報告された症例では、アミロライドにより高血圧と低カリウム血症が良好にコントロールされた。
    condition:
      region: 欧州
      study: 文献レビューと新規症例の報告（イタリア）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-629
    source: 'Tetti M, Monticone S, Burrello J, et al. Liddle Syndrome: Review of the Literature and Description of a New Case. Int J Mol Sci. 2018;19(3):812'
    doi: 10.3390/ijms19030812
    pmid: '29534496'
    pmcid: PMC5877673
    url: https://doi.org/10.3390/ijms19030812
    source_license: CC BY 4.0（誌面の表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: アミロライドの国内の承認・保険適用は本調査では確認していない（国内の適応は未確認）。症例報告を含む総説に基づいており、有病率は確立していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)'
    kokushi: 医学各論 Ⅷ-2-C-⑥（Liddle症候群、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KT-028
  domain: KT
  subdomain: Bartter症候群とGitelman症候群の鑑別
  assertion:
    plain_statement_ja: Bartter症候群とGitelman症候群は、どちらも低カリウム性代謝性アルカローシスと、血圧の正常から低下、レニンとアルドステロンの上昇を共有する塩喪失性の尿細管疾患だが、障害部位が異なる。Bartter症候群はヘンレループの太い上行脚の障害で、尿中カルシウム排泄は正常から増加し、腎石灰化を伴いやすく、発症はより早期で重症になりやすい。Gitelman症候群は遠位曲尿細管の障害で、低カルシウム尿と目立つ低マグネシウム血症を伴い、思春期から成人期に見つかることが多い。尿中カルシウムと血清マグネシウムが、両者を分ける手がかりになる。
    condition:
      region: 国際
      study: 遺伝性尿細管疾患に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-630
    source: 'Downie ML, Lopez Garcia SC, Kleta R, Bockenhauer D. Inherited Tubulopathies of the Kidney: Insights from Genetics. Clin J Am Soc Nephrol. 2021;16(4):620-630'
    doi: 10.2215/CJN.14481119
    pmid: '32238367'
    pmcid: PMC8092065
    url: https://doi.org/10.2215/CJN.14481119
    source_license: 出版社の著作物（学会誌、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 鑑別点は遺伝性尿細管疾患の総説の記載に基づく総論であり、尿中カルシウムの数値基準（比のカットオフなど）は出典の表から読み取る必要があるため、本カードには数値を記載していない。表現型が重なる例では、最終的に遺伝学的検査で分けることがある。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ)'
    kokushi: 医学各論 Ⅷ-2-C-④（Bartter症候群、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応の一覧

| カードID | 出題基準 | コアカリ |
|---|---|---|
| GN-001 | 医学各論 Ⅷ-1-E-①（血尿、a） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-010 (id: JlAKpmc) |
| GN-002 | 医学各論 Ⅷ-1-E-②（蛋白尿、a） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-011 (id: JlAKpmg) |
| GN-003 | 医学各論 Ⅷ-1-A-①（急性糸球体腎炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-321 (id: Jlvnl9M) |
| GN-004 | 医学各論 Ⅷ-1-A-①（急性糸球体腎炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-321 (id: Jlvnl9M) |
| GN-005 | 医学各論 Ⅷ-1-A-②（急速進行性糸球体腎炎症候群、a） | PS-02-09-05 (id: JkxnuRs) |
| GN-006 | 医学各論 Ⅷ-1-A-②（急速進行性糸球体腎炎症候群、a） | PS-02-09-05 (id: JkxnuRs) |
| GN-007 | 医学各論 Ⅷ-1-A-③（慢性糸球体腎炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-322 (id: Jlvnl9U) |
| GN-008 | 医学各論 Ⅷ-1-A-③（慢性糸球体腎炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-322 (id: Jlvnl9U) |
| GN-009 | 医学各論 Ⅷ-1-A-③（慢性糸球体腎炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-322 (id: Jlvnl9U) |
| GN-010 | null | PS-02-09-05 (id: JkxnuRs) |
| GN-011 | null | PS-02-09-05 (id: JkxnuRs) |
| GN-012 | 医学各論 Ⅷ-1-B-①（微小変化群、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-325 (id: Jlvnl9k) |
| GN-013 | 医学各論 Ⅷ-1-B-②（巣状分節性糸球体硬化症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-324 (id: Jlvnl9g) |
| GN-014 | 医学各論 Ⅷ-1-B-②（巣状分節性糸球体硬化症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-324 (id: Jlvnl9g) |
| GN-015 | 医学各論 Ⅷ-1-B-③（膜性腎症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-323 (id: Jlvnl9Y) |
| GN-016 | 医学各論 Ⅷ-1-B-③（膜性腎症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-323 (id: Jlvnl9Y) |
| GN-017 | 医学各論 Ⅷ-1-B-④（膜性増殖性糸球体腎炎、c） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-326 (id: Jlvnl9s) |
| GN-018 | 医学各論 Ⅷ-1-B-①（微小変化群、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-427 (id: JlvnmHU) |
| GN-019 | 医学各論 Ⅷ-1-A-①（急性糸球体腎炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-321 (id: Jlvnl9M) |
| GN-020 | 医学各論 Ⅷ-1-E-①（血尿、a） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-014 (id: JlAKpm0) |
| GN-021 | 医学各論 Ⅷ-1-C-①（糖尿病腎症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-332 (id: Jlvnl-Q) |
| GN-022 | 医学各論 Ⅷ-1-C-①（糖尿病腎症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-332 (id: Jlvnl-Q) |
| GN-023 | 医学各論 Ⅷ-1-C-①（糖尿病腎症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-332 (id: Jlvnl-Q) |
| GN-024 | 医学各論 Ⅷ-1-D-②（全身性エリテマトーデス<SLE>、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-336 (id: Jlvnl-k) |
| GN-025 | 医学各論 Ⅷ-1-D-②（全身性エリテマトーデス<SLE>、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-336 (id: Jlvnl-k) |
| GN-026 | 医学各論 Ⅷ-1-D-②（全身性エリテマトーデス<SLE>、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-336 (id: Jlvnl-k) |
| GN-027 | 医学各論 Ⅷ-1-D-①（顕微鏡的多発血管炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-337 (id: Jlvnl-s) |
| GN-028 | 医学各論 Ⅷ-1-D-①（顕微鏡的多発血管炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-337 (id: Jlvnl-s) |
| GN-029 | 医学各論 Ⅷ-1-D-⑤（多発血管炎性肉芽腫症、c） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-337 (id: Jlvnl-s) |
| GN-030 | 医学各論 Ⅷ-1-A-②（急速進行性糸球体腎炎症候群、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-335 (id: Jlvnl-w) |
| GN-031 | 医学各論 Ⅷ-1-C-②（IgA血管炎、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-333 (id: Jlvnl-Y) |
| GN-032 | 医学各論 Ⅷ-1-C-③（アミロイド腎症、c） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-334 (id: Jlvnl-g) |
| GN-033 | 医学各論 Ⅷ-1-C-④（二次性膜性腎症、c） | PS-02-09-05 (id: JkxnuRs) |
| GN-034 | 医学各論 Ⅷ-1-D-②（全身性エリテマトーデス<SLE>、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-336 (id: Jlvnl-k) |
| GN-035 | 医学各論 Ⅷ-1-D-④（関節リウマチ、c） | PS-02-09-05 (id: JkxnuRs) |
| GN-036 | 医学各論 Ⅷ-1-F-①（Alport症候群、c） | PS-02-09-05 (id: JkxnuRs) |
| GN-037 | 医学各論 Ⅷ-1-F-①（Alport症候群、c） | PS-02-09-05 (id: JkxnuRs) |
| GN-038 | 医学各論 Ⅷ-1-F-②（基底膜菲薄化症候群<良性家族性血尿>、c） | PS-02-09-05 (id: JkxnuRs) |
| GN-039 | 医学各論 Ⅷ-1-F-③（Fabry病、c） | PS-02-09-05 (id: JkxnuRs) |
| GN-040 | 医学各論 Ⅷ-1-F-③（Fabry病、c） | PS-02-09-05 (id: JkxnuRs) |
| KT-001 | 医学各論 Ⅷ-2-A-①（高血圧性腎硬化症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-327 (id: Jlvnl90) |
| KT-002 | 医学各論 Ⅷ-2-A-③（悪性腎硬化症、悪性高血圧症、b） | PS-02-09-05 (id: JkxnuRs) |
| KT-003 | 医学各論 Ⅷ-2-A-②（腎血管性高血圧症、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-328 (id: Jlvnl94) |
| KT-004 | 医学各論 Ⅷ-2-A-④（腎梗塞、b） | PS-02-09-05 (id: JkxnuRs) |
| KT-005 | 医学各論 Ⅷ-2-A-⑤（コレステロール塞栓症、b） | PS-02-09-05 (id: JkxnuRs) |
| KT-006 | 医学各論 Ⅷ-2-A-⑥（全身性強皮症、b） | PS-02-09-05 (id: JkxnuRs) |
| KT-007 | 医学各論 Ⅷ-2-A-⑦（腎静脈血栓症、c） | PS-02-09-05 (id: JkxnuRs) |
| KT-008 | 医学各論 Ⅷ-2-A-⑧（結節性多発動脈炎、c） | PS-02-09-05 (id: JkxnuRs) |
| KT-009 | 医学各論 Ⅷ-2-B-①（急性尿細管壊死、a） | PS-02-09-05 (id: JkxnuRs) |
| KT-010 | 医学各論 Ⅷ-2-B-②（急性間質性腎炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-330 (id: Jlvnl-E) |
| KT-011 | 医学各論 Ⅷ-2-B-②（急性間質性腎炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-330 (id: Jlvnl-E) |
| KT-012 | 医学各論 Ⅷ-2-B-③（骨髄腫腎、b） | PS-02-09-05 (id: JkxnuRs) |
| KT-013 | 医学各論 Ⅷ-2-B-④（慢性間質性腎炎、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-330 (id: Jlvnl-E) |
| KT-014 | 医学各論 Ⅷ-2-B-⑤（Sjögren症候群、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-330 (id: Jlvnl-E) |
| KT-015 | 医学各論 Ⅷ-2-B-⑥（IgG4関連疾患、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-330 (id: Jlvnl-E) |
| KT-016 | 医学各論 Ⅷ-2-B-⑦（中毒性腎障害、b） | PS-02-09-05 (id: JkxnuRs) |
| KT-017 | 医学各論 Ⅷ-2-B-⑧（尿酸腎症<痛風腎>、c） | PS-02-09-05 (id: JkxnuRs) |
| KT-018 | 医学各論 Ⅷ-2-C-①（尿細管性アシドーシス、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-329 (id: Jlvnl-A)；TBL-01-00-319 (id: Jlvnl9A)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ) |
| KT-019 | 医学各論 Ⅷ-2-C-①（尿細管性アシドーシス、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-329 (id: Jlvnl-A)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ) |
| KT-020 | 医学各論 Ⅷ-2-C-①（尿細管性アシドーシス、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-329 (id: Jlvnl-A)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ) |
| KT-021 | null | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM) |
| KT-022 | 医学各論 Ⅷ-2-C-②（シスチン尿症、b） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM) |
| KT-023 | 医学各論 Ⅷ-2-C-③（腎性尿崩症、c） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM) |
| KT-024 | 医学各論 Ⅷ-2-C-③（腎性尿崩症、c） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM) |
| KT-025 | 医学各論 Ⅷ-2-C-④（Bartter症候群、c） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ) |
| KT-026 | 医学各論 Ⅷ-2-C-⑤（Gitelman症候群、c） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ) |
| KT-027 | 医学各論 Ⅷ-2-C-⑥（Liddle症候群、c） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM) |
| KT-028 | 医学各論 Ⅷ-2-C-④（Bartter症候群、c） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-005 (id: JlAKpmM)；TBL-02-08-006 (id: JlAKpmQ) |

## 4. 未解決事項

- スキーマと接頭辞（担当：取り込み側）：手元のリポジトリの `schema/fact.schema.json` と `data/domains.yaml` には接頭辞 GN・KT がまだない。取り込み時に両方へ追加が必要。こちらでは接頭辞を追加した条件でスキーマ検証を行い、エラー0を確認した。
- 出典マスター全体との重複確認（担当：取り込み側）：手元の出典マスター（SRC-312まで）には腎臓分野の出典は見当たらなかったが、呼吸器までの全マスター（〜SRC-569）との最終照合は取り込み側に残る。とくに KDIGO の各ガイドラインと ANCA 関連血管炎の出典。
- ライセンス UNKNOWN 9件（担当：取り込み側で出版社ページを再確認）：SRC-574、SRC-580、SRC-581、SRC-586、SRC-596、SRC-597、SRC-598、SRC-602、SRC-603。いずれも Crossref のレコードに license 欄がなかった。RESTRICTED としたもののうち SRC-609〜611・618・622〜625・628・630 も、出版社ページ・Crossref での最終確認が望ましい。
- 薬剤の国内承認・保険適用（担当：取り込み側で PMDA の添付文書により確認）：確認済みは GN-018（小児特発性ネフローゼ症候群へのリツキシマブ）のみ。他の薬剤カード（GN-006、008、012、014、016、022、023、025、026、028、030、035、037、040、KT の薬剤を含む各カード、K2 の全カード）は、各カードの uncertainty に「国内の適応は未確認」と明記した。
- kokushi が null の3件（担当：取り込み側で対応付け）：GN-010・GN-011（ネフローゼ症候群の定義と治療総論。出題基準の表に症候群そのものの項目がないため）、KT-021（Fanconi症候群。表に項目がないため）。コアカリ番号は付けてある。
- GN-007〜009 の kokushi は Ⅷ-1-A-③（項目名「慢性糸球体腎炎」）とした（IgA腎症をその代表として扱う構成）。表記が異なる場合は取り込み側で修正が必要。
- 表から読み取った数値（各カードの uncertainty に明記済み）：GN-001（AUA 2025 のリスク層別）、GN-002（KDIGO 2024 のアルブミン尿区分）、GN-010（日本のネフローゼ定義）、GN-021（糖尿病性腎症の病期境界値）、GN-034（腎生検の閾値）、KT-018・KT-028（尿細管疾患の数値基準は本文の表依存のため数値を入れず留保を記載）。
- 二次資料経由の確認を含むもの：GN-013（FSGS の Columbia 分類の亜型名）、GN-016（膜性腎症 MENTOR 試験の寛解率）。uncertainty に明記済み。
- 内容の補完候補（担当：取り込み側・次回以降）：GN-024 は ISN/RPS 分類の使い方として作成し、分類定義そのものは Bajema らの改訂報告（Kidney Int 2018、DOI 10.1016/j.kint.2017.11.023、PMID 29459092、識別子確認済み・今回の枠外）を出典に別カード化できる。GN-037 は専門家ガイドラインの推奨で作成し、EARLY PRO-TECT 試験（Kidney Int 2020、DOI 10.1016/j.kint.2019.12.015、PMID 32299679、同・枠外）の数値カードに差し替え可能。GN-033 は悪性腫瘍に伴う二次性膜性腎症のみ（薬剤・感染症は未確認）。GN-035 は薬剤性腎障害を主要病変として扱っていない。KT-009 は急性尿細管壊死の時期区分・回復率の数値が未確認。KT-013 は慢性間質性腎炎の成因全体の数値が未確認。KT-003 は画像検査の感度・特異度が未確認。

## 5. 次回への引き継ぎ

- 欠番：なし（GN-001〜040、KT-001〜028 は連番）。未使用 SRC：SRC-588 のみ（番号は詰めていない）。
- カードのない出題基準の小項目：Ⅷ-1-D-③（全身性強皮症）は KT-006（Ⅷ-2-A-⑥）で実質カバー済み。それ以外は対象43項目すべてにカードがある。
- 第16回との重複注意：急性尿細管壊死は Ⅷ-2-B-①（KT-009、尿細管・間質の側から原因中心）と Ⅷ-3-A-②（第16回 KF、急性腎障害の文脈）の両方に項目がある。第16回では AKI の枠組み・重症度との関係に絞り、KT-009 と重複させない。酸塩基平衡は KF で代謝性に絞る（呼吸性は呼吸器 RX で作成済み）。
- 扱った出典の中心：KDIGO 2021（糸球体疾患）、KDIGO 2024（CKD 評価・ループス腎炎）、AUA/SUFU 2025（顕微鏡的血尿）、日本腎臓学会関連の英語版（糖尿病性腎症の病期分類、ネフローゼの定義、小児ネフローゼ）、主要 RCT（DAPA-CKD、BLISS-LN、RAVE、MENTOR など）。次回以降、同じ出典を再使用する場合は新しい SRC を付けず今回の番号を使うこと。
- 作成方法の注意（第14回の受け入れ検査の観点）：DOI・PMID は全件そろえた。ライセンス UNKNOWN の9件は出版社ページ確認で減らせる可能性がある。
