# ライセンス未確認（UNKNOWN）の出典の照合の依頼（第2回：50件）

依頼者：三原弘（2026-11-23）。11月23日の7件の照合（id_check_20261123b.md）と同じ方法で、下の50件の出典のライセンスを確かめてください。結果は1つの Markdown（license_check_02.md）にまとめてください。**照合の前に、hm-cmed/cleanroom-facts の最新版を取得してください。**

第1回の50件は反映済みです（48件を RESTRICTED に変更）。残りは280件（カード312枚）で、今回はその2回目（カード82枚分）です。

**第1回からの申し送り**

- 添付文書（製薬会社の作成）は、レポジトリの決まり（CLAUDE.md §2-2）で UNKNOWN のまま据え置くため、照合の対象から外しました。今後も対象にしません（第1回の SRC-115・SRC-116 は区分を据え置き、ライセンスの記載だけを更新しました）。
- 第1回で確かめた補完候補（DOI・PMID・PMCID・ページ）と、SRC-252 の DOI の訂正、SRC-5227 の書誌は反映済みです。今回も同じように、気づいた食い違いを備考に書いてください。

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
| 1 | SRC-1444 | Johnson DE, Burtness B, Leemans CR, Lui VWY, Bauman JE, Grandis JR. Head and neck squamous cell carcinoma. Nat Rev Dis Primers. 2020;6(1):92. | 10.1038/s41572-020-00224-3 | 33243986 | ライセンス未確認 | OR-020・OR-021（2枚） |
| 2 | SRC-1446 | Kim MJ, Milliren A, Gerold DJ Jr. Salivary Gland Disorders: Rapid Evidence Review. American Family Physician. 2024;109(6):550-559. |  | 38905553 | ライセンス表示を確認できず | OR-024・OR-025（2枚） |
| 3 | SRC-1545 | Klein DA, Poth MA. Amenorrhea: An Approach to Diagnosis and Management. Am Fam Physician. 2013;87(11):781-788. |  | 23939500 | ライセンス表示なし | RP-065・RP-066（2枚） |
| 4 | SRC-1691 | Andersen PM, Abrahams S, Borasio GD, et al.; EFNS Task Force on Diagnosis and Management of Amyotrophic Lateral Sclerosis. EFNS guidelines on the clinical manag | 10.1111/j.1468-1331.2011.03501.x | 21914052 |  | ND-045・ND-048（2枚） |
| 5 | SRC-1698 | Rose JJ, Wang L, Xu Q, et al. Carbon Monoxide Poisoning: Pathogenesis, Management, and Future Directions of Therapy. Am J Respir Crit Care Med. 2017 | 10.1164/rccm.201606-1275CI | 27753502 |  | ND-054・ND-063（2枚） |
| 6 | SRC-1702 | Fisher RS, Cross JH, French JA, et al. Operational classification of seizure types by the International League Against Epilepsy: Position Paper of the ILAE Comm | 10.1111/epi.13670 | 28276060 |  | EP-001・EP-009（2枚） |
| 7 | SRC-1718 | Glauser T, Kluger G, Sachdeo R, Krauss G, Perdomo C, Arroyo S. Rufinamide for generalized seizures associated with Lennox-Gastaut syndrome. Neurology. 2008;70(2 | 10.1212/01.wnl.0000303813.95800.0d | 18401024 |  | EP-025・EP-026（2枚） |
| 8 | SRC-1875 | Krul M, van der Wouden JC, Kruithof EJ, et al. Manipulative interventions for reducing pulled elbow in young children. Cochrane Database Syst Rev. 2017;7(7):CD0 | 10.1002/14651858.CD007759.pub4 | 28753234 |  | OS-029・OS-030（2枚） |
| 9 | SRC-1878 | Ömeroğlu H, Yüksel S, Demir P, et al. An Eastern Europe and Middle East multinational expert Delphi consensus study on the prevention, diagnosis, and treatment  | 10.1007/s00264-023-06077-1 | 38150007 |  | OS-033・OS-034（2枚） |
| 10 | SRC-1929 | Ravikanth R, Majumdar P. Prognostic Significance of Magnetic Resonance Imaging in Detecting Diffuse Axonal Injuries: Analysis of Outcomes and Review of Literatu | 10.4103/0028-3886.364066 | 36537418 | 未確認 | TJ-010・TJ-011（2枚） |
| 11 | SRC-3431 | Kemper AR, Newman TB, Slaughter JL, et al. Clinical Practice Guideline Revision: Management of Hyperbilirubinemia in the Newborn Infant 35 or More Weeks of Gest | 10.1542/peds.2022-058859 |  |  | NB-013・NB-014（2枚） |
| 12 | SRC-378 | Chalmers JD, Haworth CS, Flume P, et al. European Respiratory Society Clinical Practice Guideline for the Management of Adult Bronchiectasis (2025) | 10.1183/13993003.01126-2025 |  | 未確認 | RO-028・RO-042（2枚） |
| 13 | SRC-427 | Kudoh S, Kato H, Nishiwaki Y, et al. Interstitial lung disease in Japanese patients with lung cancer: a cohort and nested case-control study. Am J Respir Crit C | 10.1164/rccm.200710-1501OC |  | 未確認 | IL-030・IL-031（2枚） |
| 14 | SRC-431 | Ranieri VM, Rubenfeld GD, Thompson BT, et al（ARDS Definition Task Force）. Acute respiratory distress syndrome: the Berlin Definition. JAMA 2012;307(23):2526-253 | 10.1001/jama.2012.5669 | 22797452 | 未確認 | IL-036・IL-037（2枚） |
| 15 | SRC-441 | Meyer G, Vicaut E, Danays T, et al（PEITHO Investigators）. Fibrinolysis for patients with intermediate-risk pulmonary embolism. N Engl J Med 2014;370 | 10.1056/NEJMoa1302097 |  | 未確認 | PV-011・PV-012（2枚） |
| 16 | SRC-442 | Pengo V, Lensing AWA, Prins MH, et al. Incidence of Chronic Thromboembolic Pulmonary Hypertension after Pulmonary Embolism. N Engl J Med 2004;350(22):2257-2264 |  |  | 未確認 | PV-013・PV-014（2枚） |
| 17 | SRC-448 | Medical Research Council Working Party. Long term domiciliary oxygen therapy in chronic hypoxic cor pulmonale complicating chronic bronchitis and emphysema. Lan | 10.1016/S0140-6736(81)91970-X |  | 未確認 | PV-027・PV-028（2枚） |
| 18 | SRC-473 | National Lung Screening Trial Research Team, Aberle DR, Adams AM, et al. Reduced lung-cancer mortality with low-dose computed tomographic screening. N Engl J Me |  | 21714641 | 未確認 | LC-007・LC-008（2枚） |
| 19 | SRC-5206 | ACG Clinical Guideline: EoE. Am J Gastroenterol 2025 | 10.14309/ajg.0000000000003194 | 39745304 | 未確認 | ES-018・ES-022（2枚） |
| 20 | SRC-817 | Gordon CM, Ackerman KE, Berga SL, Kaplan JR, Mastorakos G, Misra M, Murad MH, Santoro NF, Warren MP. Functional Hypothalamic Amenorrhea: An Endocrine Society Cl | 10.1210/jc.2017-00131 | 28368518 | Endocrine Societyのガイドライン。CC表示を確認できず | RP-019・RP-068（2枚） |
| 21 | SRC-838 | Balen AH, Morley LC, Misso M, et al. The management of anovulatory infertility in women with polycystic ovary syndrome: an analysis of the evidence to support t | 10.1093/humupd/dmw025 | 27511809 | 未確認 | RP-021・RP-027（2枚） |
| 22 | SRC-841 | Trussell J. Contraceptive failure in the United States. Contraception. 2011;83(5):397-404. | 10.1016/j.contraception.2011.01.021 | 21477680 | 出版社ページ・Crossref に CC ライセンスの表示なし（PMC 収載は著者原稿） | RP-041・RP-045（2枚） |
| 23 | SRC-847 | The North American Menopause Society. The 2022 hormone therapy position statement of The North American Menopause Society. Menopause. 2022;29(7):767-794. | 10.1097/GME.0000000000002028 | 35797481 | 学会誌掲載で CC ライセンスの表示なし | RP-049・RP-055（2枚） |
| 24 | SRC-849 | Eastell R, Rosen CJ, Black DM, et al. Pharmacological Management of Osteoporosis in Postmenopausal Women: An Endocrine Society Clinical Practice Guideline. The  | 10.1210/jc.2019-00221 | 30907953 | 学会ガイドラインで CC ライセンスの表示なし | RP-051・RP-052（2枚） |
| 25 | SRC-875 | Katznelson L, Laws ER Jr, Melmed S, et al. Acromegaly: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 201 | 10.1210/jc.2014-2700 | 25356808 | ライセンス表示を確認できず | EN-005・EN-006（2枚） |
| 26 | SRC-880 | Higham CE, Johannsson G, Shalet SM. Hypopituitarism. The Lancet. 2016;388(10058):2403-2415. | 10.1016/S0140-6736(16)30053-8 | 27041067 | ライセンス表示を確認できず（TDM のみ） | EN-014・EN-015（2枚） |
| 27 | SRC-881 | Christ-Crain M, Bichet DG, Fenske WK, et al. Diabetes Insipidus. Nature Reviews Disease Primers. 2019;5(1):54. | 10.1038/s41572-019-0103-2 | 31395885 | ライセンス表示を確認できず（TDM のみ） | EN-016・EN-017（2枚） |
| 28 | SRC-910 | Knobel M. Etiopathology, clinical features, and treatment of diffuse and multinodular nontoxic goiters. J Endocrinol Invest. 2016;39(4):357-373 | 10.1007/s40618-015-0391-7 | 26392367 | ライセンス表示を確認できず | TH-010・TH-011（2枚） |
| 29 | SRC-911 | McHenry CR, Phitayakorn R. Follicular adenoma and carcinoma of the thyroid gland. Oncologist. 2011;16(5):585-593 | 10.1634/theoncologist.2010-0405 | 21482585 | ライセンス表示を確認できず | TH-012・TH-015（2枚） |
| 30 | SRC-912 | Haugen BR, et al. 2015 American Thyroid Association Management Guidelines for Adult Patients with Thyroid Nodules and Differentiated Thyroid Cancer. Thyroid. 20 | 10.1089/thy.2015.0020 | 26462967 | ライセンス表示を確認できず（PMC で無料公開） | TH-013・TH-014（2枚） |
| 31 | SRC-914 | Bartalena L, et al. The 2021 European Group on Graves' orbitopathy (EUGOGO) clinical practice guidelines for the medical management of Graves' orbitopathy. Eur  | 10.1530/EJE-21-0479 | 34297684 | ライセンス表示を確認できず | TH-017・EY-035（2枚） |
| 32 | SRC-987 | Chandrakumar A, Bhardwaj A, 't Jong GW. Review of thiamine deficiency disorders: Wernicke encephalopathy and Korsakoff psychosis. J Basic Clin Physiol Pharmacol | 10.1515/jbcpp-2018-0075 | 30281514 | ライセンス表示を確認できず | MT-020・ND-038（2枚） |
| 33 | SRC-1080 | Beutler BD, Cohen PR, Lee RA. Prurigo Pigmentosa: Literature Review. American Journal of Clinical Dermatology. 2015;16(6):533-543. | 10.1007/s40257-015-0154-4 | 26334426 | Springer（CCライセンス表示を確認できず） | SK-015（1枚） |
| 34 | SRC-1082 | Sokumbi O, Wetter DA. Clinical features, diagnosis, and treatment of erythema multiforme: a review for the practicing dermatologist. International Journal of De | 10.1111/j.1365-4632.2011.05348.x | 22788803 | Wiley（CCライセンス表示を確認できず） | SK-019（1枚） |
| 35 | SRC-1084 | Hsu DY, Brieva J, Silverberg NB, Silverberg JI. Morbidity and Mortality of Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis in United States Adults. J In | 10.1016/j.jid.2016.03.023 | 27039263 | © The Authors / Elsevier（CC表示なし） | SK-021（1枚） |
| 36 | SRC-1085 | Bastuji-Garin S, Fouchard N, Bertocchi M, Roujeau JC, Revuz J, Wolkenstein P. SCORTEN: A Severity-of-Illness Score for Toxic Epidermal Necrolysis. J Invest Derm | 10.1046/j.1523-1747.2000.00061.x | 10951229 | Elsevier（CC表示なし） | SK-022（1枚） |
| 37 | SRC-1088 | Maverakis E, Ma C, Shinkai K, et al. Diagnostic Criteria of Ulcerative Pyoderma Gangrenosum: A Delphi Consensus of International Experts. JAMA Dermatol. 2018;15 | 10.1001/jamadermatol.2017.5980 | 29450466 | © American Medical Association（CC表示なし） | SK-025（1枚） |
| 38 | SRC-1089 | Decousus H, Prandoni P, Mismetti P, et al.; CALISTO Study Group. Fondaparinux for the Treatment of Superficial-Vein Thrombosis in the Legs. N Engl J Med. 2010;3 | 10.1056/NEJMoa0912072 | 20860504 | © Massachusetts Medical Society（CC表示なし） | SK-026（1枚） |
| 39 | SRC-1090 | Nyssen A, Benhadou F, Magnée M, André J, Koopmansch C, Wautrecht JC. Chilblains. Vasa. 2020;49(2):133-140 | 10.1024/0301-1526/a000838 | 31808732 | Hogrefe（CC表示なし） | SK-027（1枚） |
| 40 | SRC-1091 | Gibbs MB, English JC 3rd, Zirwas MJ. Livedo reticularis: An update. J Am Acad Dermatol. 2005;52(6):1009-1019 | 10.1016/j.jaad.2004.11.051 | 15928620 | © American Academy of Dermatology / Elsevier（CC表示なし） | SK-028（1枚） |
| 41 | SRC-1092 | Gupta LK, Martin AM, Agarwal N, et al. Guidelines for the management of Stevens-Johnson syndrome/toxic epidermal necrolysis: An Indian perspective. Indian J Der | 10.4103/0378-6323.191134 | 27716721 | ライセンス表示を確認できず | SK-029（1枚） |
| 42 | SRC-1103 | Behravesh S, Yakes W, Gupta N, et al. Venous malformations: clinical diagnosis and treatment. Cardiovasc Diagn Ther. 2016;6(6):557-569 | 10.21037/cdt.2016.11.10 | 28123976 | ライセンス表示を確認できず | DT-008（1枚） |
| 43 | SRC-1108 | Gauglitz GG, Korting HC, Pavicic T, et al. Hypertrophic scarring and keloids: pathomechanisms and current and emerging treatment strategies. Mol Med. 2011;17(1- | 10.2119/molmed.2009.00153 | 20927486 | ライセンス表示を確認できず | DT-014（1枚） |
| 44 | SRC-1110 | Hartmann K, Escribano L, Grattan C, et al. Cutaneous manifestations in patients with mastocytosis: Consensus report of the European Competence Network on Mastoc | 10.1016/j.jaci.2015.08.034 | 26476479 | ライセンス表示を確認できず | DT-018（1枚） |
| 45 | SRC-1111 | Ishihara K, Saida T, Otsuka F, Yamazaki N; Prognosis and Statistical Investigation Committee of the Japanese Skin Cancer Society. Statistical profiles of malign | 10.1007/s10147-007-0751-1 | 18307017 | Springer TDM license（CC表示なし） | DT-025（1枚） |
| 46 | SRC-1113 | Vestergaard ME, Macaskill P, Holt PE, Menzies SW. Dermoscopy compared with naked eye examination for the diagnosis of primary melanoma: a meta-analysis of studi | 10.1111/j.1365-2133.2008.08713.x | 18616769 | Wiley TDM license（CC表示なし） | DT-032（1枚） |
| 47 | SRC-1114 | Gershenwald JE, Scolyer RA, Hess KR, et al. Melanoma staging: Evidence-based changes in the American Joint Committee on Cancer eighth edition cancer staging man | 10.3322/caac.21409 | 29028110 | © 2017 American Cancer Society（CC表示なし） | DT-023（1枚） |
| 48 | SRC-1117 | Migden MR, Rischin D, Schmults CD, et al. PD-1 Blockade with Cemiplimab in Advanced Cutaneous Squamous-Cell Carcinoma. New England Journal of Medicine. 2018;379 | 10.1056/NEJMoa1805131 | 29863979 | © Massachusetts Medical Society（CC表示なし） | DT-020（1枚） |
| 49 | SRC-1124 | Faries MB, Thompson JF, Cochran AJ, et al. Completion Dissection or Observation for Sentinel-Node Metastasis in Melanoma. New England Journal of Medicine. 2017; | 10.1056/NEJMoa1613210 | 28591523 | © Massachusetts Medical Society（CC表示なし） | DT-034（1枚） |
| 50 | SRC-1125 | Green AC, Williams GM, Logan V, Strutton GM. Reduced Melanoma after Regular Sunscreen Use: Randomized Trial Follow-up. Journal of Clinical Oncology. 2011;29(3): | 10.1200/JCO.2010.28.7078 | 21135266 | © American Society of Clinical Oncology（CC表示なし） | DT-035（1枚） |
