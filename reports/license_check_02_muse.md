# ライセンス未確認（UNKNOWN）出典の照合・第2回（50件）

- 照合日: 2026-11-24
- 対象リポジトリ: hm-cmed/cleanroom-facts（出典マスター `data/sources.yaml` と全章のカードファイル）
- 照合の基準にした版: コミット `0aa99331b13988793cd0c0411d9b60bca57cbbf8`（2026-11-23T17:14:43Z）時点の最新版。この時点で出典は全 2,493 件、うちライセンス UNKNOWN は 310 件、カードは全 3,899 枚。
- 方法・判定区分は第1回（`license_check_01.md`）と同一。判定区分: OPEN（刊行版が CC BY/CC0）／RESTRICTED（CC BY-NC・ND・NC-ND・SA・NC-SA、または CC 表示なし）／GOV_US／GOV_JP／確認できず（理由を明記）。根拠の優先順位は 出版社の論文ページ ＞ PMC の論文ページ（著者原稿でないこと）＞ Crossref の license 欄（vor）。Unpaywall・OpenAlex だけを根拠にしない。著者原稿の表示は刊行版の根拠に使わない。本文は保存していない。

## 対象リストの作り方

1. 最新版のマスターでライセンスが UNKNOWN の出典 310 件を抽出した。
2. 各出典について、全章のカードの `provenance.source_ref`（主出典としての使用）を数え、あわせて `corroboration` のみで使われているカードを区別した。
3. 次のものを除外した: 第1回の 50 件（`license_check_01.md` の一覧）、識別子照合で判定済みの 7 件（`id_check_20261123b.md` の SRC-2481・4026・3856・3866・2027・3351・096）、自由に使える出典の調査で区分が確定した出典（`free_sources_68_result.md` の SRC-5220・5214・5215・5218・5229・5221・5222・5225・2641・2642。うち SRC-115・116 は最新マスターでも UNKNOWN のまま残っていたため、既判定として本回からも除外した）。
4. 残りを「主出典カード数（降順）→ 裏づけのみの使用数（降順）→ SRC 番号（昇順）」で並べ、上位 50 件を第2回の対象とした。50 件で主出典としてカバーするカードは 83 枚、裏づけのみの使用は 2 件（SRC-142 が NG-125、SRC-5206 が ES-018）。

## 対象リスト（50件）

| # | SRC | 書誌（マスターの記載） | DOI | PMID | マスターの現行メモ | 主出典カード | 裏づけのみ |
|---|---|---|---|---|---|---|---|
| 1 | SRC-1444 | Johnson DE, Burtness B, Leemans CR, Lui VWY, Bauman JE, Grandis JR. Head and neck squamous cell carcinoma. Nat Rev Dis Primers. 2020;6(1):92. | 10.1038/s41572-020-00224-3 | 33243986 | ライセンス未確認 | OR-020・OR-021 | — |
| 2 | SRC-1446 | Kim MJ, Milliren A, Gerold DJ Jr. Salivary Gland Disorders: Rapid Evidence Review. American Family Physician. 2024;109(6):550-559. | — | 38905553 | ライセンス表示を確認できず | OR-024・OR-025 | — |
| 3 | SRC-1545 | Klein DA, Poth MA. Amenorrhea: An Approach to Diagnosis and Management. Am Fam Physician. 2013;87(11):781-788. | — | 23939500 | ライセンス表示なし | RP-065・RP-066 | — |
| 4 | SRC-1691 | Andersen PM, Abrahams S, Borasio GD, et al.; EFNS Task Force on Diagnosis and Management of Amyotrophic Lateral Sclerosis. EFNS guidelines on the clinical management of amyotrophic lateral sclerosis (MALS)--revised report of an EFNS task force. Eur J Neurol. 2012;19(3):360-375 | 10.1111/j.1468-1331.2011.03501.x | 21914052 | — | ND-045・ND-048 | — |
| 5 | SRC-1698 | Rose JJ, Wang L, Xu Q, et al. Carbon Monoxide Poisoning: Pathogenesis, Management, and Future Directions of Therapy. Am J Respir Crit Care Med. 2017 | 10.1164/rccm.201606-1275CI | 27753502 | — | ND-054・ND-063 | — |
| 6 | SRC-1702 | Fisher RS, Cross JH, French JA, et al. Operational classification of seizure types by the International League Against Epilepsy: Position Paper of the ILAE Commission for Classification and Terminology. Epilepsia. 2017;58(4):522-530 | 10.1111/epi.13670 | 28276060 | — | EP-001・EP-009 | — |
| 7 | SRC-1718 | Glauser T, Kluger G, Sachdeo R, Krauss G, Perdomo C, Arroyo S. Rufinamide for generalized seizures associated with Lennox-Gastaut syndrome. Neurology. 2008;70(21):1950-1958 | 10.1212/01.wnl.0000303813.95800.0d | 18401024 | — | EP-025・EP-026 | — |
| 8 | SRC-1875 | Krul M, van der Wouden JC, Kruithof EJ, et al. Manipulative interventions for reducing pulled elbow in young children. Cochrane Database Syst Rev. 2017;7(7):CD007759 | 10.1002/14651858.CD007759.pub4 | 28753234 | — | OS-029・OS-030 | — |
| 9 | SRC-1878 | Ömeroğlu H, Yüksel S, Demir P, et al. An Eastern Europe and Middle East multinational expert Delphi consensus study on the prevention, diagnosis, and treatment of developmental dysplasia of the hip before walking age. Int Orthop. 2024;48(6):1373-1380 | 10.1007/s00264-023-06077-1 | 38150007 | — | OS-033・OS-034 | — |
| 10 | SRC-1929 | Ravikanth R, Majumdar P. Prognostic Significance of Magnetic Resonance Imaging in Detecting Diffuse Axonal Injuries: Analysis of Outcomes and Review of Literature. Neurol India. 2022;70(6):2371-2377 | 10.4103/0028-3886.364066 | 36537418 | 未確認 | TJ-010・TJ-011 | — |
| 11 | SRC-3431 | Kemper AR, Newman TB, Slaughter JL, et al. Clinical Practice Guideline Revision: Management of Hyperbilirubinemia in the Newborn Infant 35 or More Weeks of Gestation. Pediatrics. 2022;150(3):e2022058859 | 10.1542/peds.2022-058859 | — | — | NB-013・NB-014 | — |
| 12 | SRC-378 | Chalmers JD, Haworth CS, Flume P, et al. European Respiratory Society Clinical Practice Guideline for the Management of Adult Bronchiectasis (2025) | 10.1183/13993003.01126-2025 | — | 未確認 | RO-028・RO-042 | — |
| 13 | SRC-427 | Kudoh S, Kato H, Nishiwaki Y, et al. Interstitial lung disease in Japanese patients with lung cancer: a cohort and nested case-control study. Am J Respir Crit Care Med 2008;177(12):1348-1357 | 10.1164/rccm.200710-1501OC | — | 未確認 | IL-030・IL-031 | — |
| 14 | SRC-431 | Ranieri VM, Rubenfeld GD, Thompson BT, et al（ARDS Definition Task Force）. Acute respiratory distress syndrome: the Berlin Definition. JAMA 2012;307(23):2526-2533 | 10.1001/jama.2012.5669 | 22797452 | 未確認 | IL-036・IL-037 | — |
| 15 | SRC-441 | Meyer G, Vicaut E, Danays T, et al（PEITHO Investigators）. Fibrinolysis for patients with intermediate-risk pulmonary embolism. N Engl J Med 2014;370 | 10.1056/NEJMoa1302097 | — | 未確認 | PV-011・PV-012 | — |
| 16 | SRC-442 | Pengo V, Lensing AWA, Prins MH, et al. Incidence of Chronic Thromboembolic Pulmonary Hypertension after Pulmonary Embolism. N Engl J Med 2004;350(22):2257-2264 | — | — | 未確認 | PV-013・PV-014 | — |
| 17 | SRC-448 | Medical Research Council Working Party. Long term domiciliary oxygen therapy in chronic hypoxic cor pulmonale complicating chronic bronchitis and emphysema. Lancet 1981;317(8222):681-686 | 10.1016/S0140-6736(81)91970-X | — | 未確認 | PV-027・PV-028 | — |
| 18 | SRC-473 | National Lung Screening Trial Research Team, Aberle DR, Adams AM, et al. Reduced lung-cancer mortality with low-dose computed tomographic screening. N Engl J Med 2011;365:395-409 | — | 21714641 | 未確認 | LC-007・LC-008 | — |
| 19 | SRC-816 | Nawaz G, Rogol AD, Jenkins SM. Amenorrhea. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK482168. | — | 29489290 | NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず | RP-006・RP-007 | — |
| 20 | SRC-817 | Gordon CM, Ackerman KE, Berga SL, Kaplan JR, Mastorakos G, Misra M, Murad MH, Santoro NF, Warren MP. Functional Hypothalamic Amenorrhea: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2017;102(5):1413-1439. | 10.1210/jc.2017-00131 | 28368518 | Endocrine Societyのガイドライン。CC表示を確認できず | RP-019・RP-068 | — |
| 21 | SRC-838 | Balen AH, Morley LC, Misso M, et al. The management of anovulatory infertility in women with polycystic ovary syndrome: an analysis of the evidence to support the development of global WHO guidance. Human Reproduction Update. 2016;22(6):687-708. | 10.1093/humupd/dmw025 | 27511809 | 未確認 | RP-021・RP-027 | — |
| 22 | SRC-841 | Trussell J. Contraceptive failure in the United States. Contraception. 2011;83(5):397-404. | 10.1016/j.contraception.2011.01.021 | 21477680 | 出版社ページ・Crossref に CC ライセンスの表示なし（PMC 収載は著者原稿） | RP-041・RP-045 | — |
| 23 | SRC-847 | The North American Menopause Society. The 2022 hormone therapy position statement of The North American Menopause Society. Menopause. 2022;29(7):767-794. | 10.1097/GME.0000000000002028 | 35797481 | 学会誌掲載で CC ライセンスの表示なし | RP-049・RP-055 | — |
| 24 | SRC-849 | Eastell R, Rosen CJ, Black DM, et al. Pharmacological Management of Osteoporosis in Postmenopausal Women: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2019;104(5):1595-1622. | 10.1210/jc.2019-00221 | 30907953 | 学会ガイドラインで CC ライセンスの表示なし | RP-051・RP-052 | — |
| 25 | SRC-875 | Katznelson L, Laws ER Jr, Melmed S, et al. Acromegaly: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2014;99(11):3933-3951. | 10.1210/jc.2014-2700 | 25356808 | ライセンス表示を確認できず | EN-005・EN-006 | — |
| 26 | SRC-880 | Higham CE, Johannsson G, Shalet SM. Hypopituitarism. The Lancet. 2016;388(10058):2403-2415. | 10.1016/S0140-6736(16)30053-8 | 27041067 | ライセンス表示を確認できず（TDM のみ） | EN-014・EN-015 | — |
| 27 | SRC-881 | Christ-Crain M, Bichet DG, Fenske WK, et al. Diabetes Insipidus. Nature Reviews Disease Primers. 2019;5(1):54. | 10.1038/s41572-019-0103-2 | 31395885 | ライセンス表示を確認できず（TDM のみ） | EN-016・EN-017 | — |
| 28 | SRC-910 | Knobel M. Etiopathology, clinical features, and treatment of diffuse and multinodular nontoxic goiters. J Endocrinol Invest. 2016;39(4):357-373 | 10.1007/s40618-015-0391-7 | 26392367 | ライセンス表示を確認できず | TH-010・TH-011 | — |
| 29 | SRC-911 | McHenry CR, Phitayakorn R. Follicular adenoma and carcinoma of the thyroid gland. Oncologist. 2011;16(5):585-593 | 10.1634/theoncologist.2010-0405 | 21482585 | ライセンス表示を確認できず | TH-012・TH-015 | — |
| 30 | SRC-912 | Haugen BR, et al. 2015 American Thyroid Association Management Guidelines for Adult Patients with Thyroid Nodules and Differentiated Thyroid Cancer. Thyroid. 2016;26(1):1-133 | 10.1089/thy.2015.0020 | 26462967 | ライセンス表示を確認できず（PMC で無料公開） | TH-013・TH-014 | — |
| 31 | SRC-914 | Bartalena L, et al. The 2021 European Group on Graves' orbitopathy (EUGOGO) clinical practice guidelines for the medical management of Graves' orbitopathy. Eur J Endocrinol. 2021;185(4):G43-G67 | 10.1530/EJE-21-0479 | 34297684 | ライセンス表示を確認できず | EY-035・TH-017 | — |
| 32 | SRC-987 | Chandrakumar A, Bhardwaj A, 't Jong GW. Review of thiamine deficiency disorders: Wernicke encephalopathy and Korsakoff psychosis. J Basic Clin Physiol Pharmacol. 2019;30(2):153-162. | 10.1515/jbcpp-2018-0075 | 30281514 | ライセンス表示を確認できず | MT-020・ND-038 | — |
| 33 | SRC-990 | Reddy P, Jialal I. Biochemistry, Fat Soluble Vitamins. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK534869. | — | 30521290 | NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず | MT-023・MT-035 | — |
| 34 | SRC-142 | （題名の記載なし） | 10.21518/ms2026-232 | — | — | NG-124 | NG-125 |
| 35 | SRC-5206 | ACG Clinical Guideline: EoE. Am J Gastroenterol 2025 | 10.14309/ajg.0000000000003194 | 39745304 | 未確認 | ES-022 | ES-018 |
| 36 | SRC-1074 | Srivastava D, Sathe NC, Persaud Y. Asteatotic Eczema. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2026. | — | 31747214 | © StatPearls Publishing LLC（CCライセンス表示を確認できず） | SK-008 | — |
| 37 | SRC-1075 | Hardin CA, Love LW, Saleh HM, Farci F. Nummular Dermatitis. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2024. | — | 33351436 | © StatPearls Publishing LLC（CCライセンス表示を確認できず） | SK-009 | — |
| 38 | SRC-1080 | Beutler BD, Cohen PR, Lee RA. Prurigo Pigmentosa: Literature Review. American Journal of Clinical Dermatology. 2015;16(6):533-543. | 10.1007/s40257-015-0154-4 | 26334426 | Springer（CCライセンス表示を確認できず） | SK-015 | — |
| 39 | SRC-1082 | Sokumbi O, Wetter DA. Clinical features, diagnosis, and treatment of erythema multiforme: a review for the practicing dermatologist. International Journal of Dermatology. 2012;51(8):889-902. | 10.1111/j.1365-4632.2011.05348.x | 22788803 | Wiley（CCライセンス表示を確認できず） | SK-019 | — |
| 40 | SRC-1084 | Hsu DY, Brieva J, Silverberg NB, Silverberg JI. Morbidity and Mortality of Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis in United States Adults. J Invest Dermatol. 2016;136(7):1387-1397 | 10.1016/j.jid.2016.03.023 | 27039263 | © The Authors / Elsevier（CC表示なし） | SK-021 | — |
| 41 | SRC-1085 | Bastuji-Garin S, Fouchard N, Bertocchi M, Roujeau JC, Revuz J, Wolkenstein P. SCORTEN: A Severity-of-Illness Score for Toxic Epidermal Necrolysis. J Invest Dermatol. 2000;115(2):149-153 | 10.1046/j.1523-1747.2000.00061.x | 10951229 | Elsevier（CC表示なし） | SK-022 | — |
| 42 | SRC-1088 | Maverakis E, Ma C, Shinkai K, et al. Diagnostic Criteria of Ulcerative Pyoderma Gangrenosum: A Delphi Consensus of International Experts. JAMA Dermatol. 2018;154(4):461-466 | 10.1001/jamadermatol.2017.5980 | 29450466 | © American Medical Association（CC表示なし） | SK-025 | — |
| 43 | SRC-1089 | Decousus H, Prandoni P, Mismetti P, et al.; CALISTO Study Group. Fondaparinux for the Treatment of Superficial-Vein Thrombosis in the Legs. N Engl J Med. 2010;363(13):1222-1232 | 10.1056/NEJMoa0912072 | 20860504 | © Massachusetts Medical Society（CC表示なし） | SK-026 | — |
| 44 | SRC-1090 | Nyssen A, Benhadou F, Magnée M, André J, Koopmansch C, Wautrecht JC. Chilblains. Vasa. 2020;49(2):133-140 | 10.1024/0301-1526/a000838 | 31808732 | Hogrefe（CC表示なし） | SK-027 | — |
| 45 | SRC-1091 | Gibbs MB, English JC 3rd, Zirwas MJ. Livedo reticularis: An update. J Am Acad Dermatol. 2005;52(6):1009-1019 | 10.1016/j.jaad.2004.11.051 | 15928620 | © American Academy of Dermatology / Elsevier（CC表示なし） | SK-028 | — |
| 46 | SRC-1092 | Gupta LK, Martin AM, Agarwal N, et al. Guidelines for the management of Stevens-Johnson syndrome/toxic epidermal necrolysis: An Indian perspective. Indian J Dermatol Venereol Leprol. 2016;82(6):603-625 | 10.4103/0378-6323.191134 | 27716721 | ライセンス表示を確認できず | SK-029 | — |
| 47 | SRC-1096 | Nicholson CL, Daveluy S. Epidermal Nevus Syndromes. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2023 | — | 32644429 | ライセンス表示を確認できず | DT-001 | — |
| 48 | SRC-1097 | Agarwal P, Patel BC. Nevus of Ota and Ito. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2023 | — | 32809409 | ライセンス表示を確認できず | DT-002 | — |
| 49 | SRC-1100 | Lewis D, Vaidya R. Kasabach-Merritt Syndrome. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2023 | — | 30085595 | ライセンス表示を確認できず | DT-005 | — |
| 50 | SRC-1103 | Behravesh S, Yakes W, Gupta N, et al. Venous malformations: clinical diagnosis and treatment. Cardiovasc Diagn Ther. 2016;6(6):557-569 | 10.21037/cdt.2016.11.10 | 28123976 | ライセンス表示を確認できず | DT-008 | — |

## 判定結果の集計

- RESTRICTED: 49 件
- OPEN: 1 件（SRC-142）
- GOV_US・GOV_JP: 0 件
- 確認できず: 0 件
- 追記（2026-11-24）: 当初「確認できず」だった5件（SRC-142・816・990・1096・1100）を、実ブラウザで刊行版ページ自体の表示を確認して再判定した。StatPearls の4章（SRC-816・990・1096・1100）は章ページ末尾の表示で CC BY-NC-ND 4.0 を確認し RESTRICTED、SRC-142（Meditsinskiy sovet）は誌のオープンアクセス方針ページと論文ページの双方で CC BY 4.0 の表示を確認し OPEN とした。これで第2回の50件は全件判定済み。
- 第1回（当時のマスターで UNKNOWN 332 件中 50 件）に続き、本回は最新版で UNKNOWN の 310 件から、既判定分（SRC-115・116）を除いた未照合の上位 50 件を照合した。未照合の残りは 258 件で、第3回以降の対象になる。

## 項目ごとの根拠と判定

### SRC-1444（Nat Rev Dis Primers 2020、頭頸部扁平上皮癌）— RESTRICTED
- Crossref の license 欄（vor）は Springer Nature のテキスト・データマイニング利用条件ページへのリンクのみで、CC ライセンスの指定はない。
- PMC 収載分（PMC7944998）は著者原稿（NIHMS1667936、"The publisher's version of this article is available at Nat Rev Dis Primers" の表示あり）のため、刊行版の根拠には使わない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1446（Am Fam Physician 2024、唾液腺疾患）— RESTRICTED
- American Family Physician 誌の論文 PDF には標準フッター「Downloaded from the American Family Physician website at www.aafp.org/afp. Copyright © American Academy of Family Physicians. For the private, noncommercial use of one individual user of the website. All other rights reserved.」が付き、CC 表示はない（同誌の 2024 年発行 PDF で確認。第1回の AAFP 分と同一の根拠）。
- Crossref・PubMed に CC ライセンスの記録はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1545（Am Fam Physician 2013、無月経）— RESTRICTED
- SRC-1446 と同じく AFP 誌の標準フッター（© American Academy of Family Physicians、私的・非商用利用のみ、その他の権利は留保）が同誌の利用条件であり、CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1691（Eur J Neurol 2012、EFNS ALS ガイドライン）— RESTRICTED
- Crossref の license 欄（vor）は Wiley の標準利用条件（onlinelibrary.wiley.com/termsAndConditions#vor）へのリンクのみで、CC ライセンスではない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1698（Am J Respir Crit Care Med 2017、一酸化炭素中毒）— RESTRICTED
- PMC 収載の刊行版ページ（PMC5363978）に「Copyright © 2017 by the American Thoracic Society」の表示があり、CC 表示はない。
- Crossref の license 欄（vor）も OUP の標準公表・再利用条件ページへのリンクのみ。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1702（Epilepsia 2017、ILAE てんかん分類）— RESTRICTED
- Crossref の license 欄（vor・am とも）は Wiley の標準利用条件へのリンクのみで、CC ライセンスではない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1718（Neurology 2008、ルフィナミド／レノックス・ガストー症候群）— RESTRICTED
- Crossref に license 欄はなく、刊行版は American Academy of Neurology の著作権表示のみで CC 表示はない（Wolters Kluwer／Ovid 配信）。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1875（Cochrane Database Syst Rev 2017）— RESTRICTED
- PMC 収載の刊行版ページ（PMC6483272）に「Copyright © 2017 The Cochrane Collaboration. Published by John Wiley & Sons, Ltd.」の表示があり、CC 表示はない。
- Crossref の license 欄（vor）も Wiley の標準利用条件へのリンクのみ。
- 判定: RESTRICTED（CC 表示なし）。PMCID 補完候補: PMC6483272（刊行版）。

### SRC-1878（Int Orthop 2024）— RESTRICTED
- Crossref の license 欄（vor）は Springer Nature の TDM 利用条件ページへのリンクのみで、CC ライセンスの指定はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1929（Neurol India 2022）— RESTRICTED
- 出版社プラットフォーム（Ovid）掲載の全文フッターに「Copyright © 2022 Neurology India, Neurological Society of India」の表示があり、全文中に Creative Commons の記載はない。
- なお、同誌は Medknow 系で CC BY-NC-SA の定型文が使われる場合があるが、いずれにせよ RESTRICTED の区分は変わらない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-3431（Pediatrics 2022、AAP）— RESTRICTED
- Crossref に license 欄はなく、刊行版は American Academy of Pediatrics の著作権表示のみで CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。PMID 補完候補: 35927462（マスターは PMID 空欄。DOI 検索で PubMed レコードを特定）。

### SRC-378（Eur Respir J 2025、ERS 気管支拡張症ガイドライン）— RESTRICTED
- 刊行版 PDF（出版社の publications.ersnet.org から配信された正本の写し）の1ページ目に「Copyright ©The authors 2025. For reproduction rights and permissions contact permissions@ersnet.org」の表示があり、全文中に Creative Commons の記載はない。
- Crossref の license 欄（vor）が指す ERS の user licence ページは、CC で公開された論文には同ライセンスが適用されない旨を明記しており、本論文が CC である根拠にはならない。
- 判定: RESTRICTED（CC 表示なし）。PMID 補完候補: 41016738、書誌は Eur Respir J 2025;66(6)。

### SRC-427（Am J Respir Crit Care Med 2008）— RESTRICTED
- Crossref の license 欄（vor）は OUP の標準公表・再利用条件ページへのリンクのみで、CC ライセンスではない。
- 判定: RESTRICTED（CC 表示なし）。PMID 補完候補: 18337594。

### SRC-431（JAMA 2012、Berlin Definition）— RESTRICTED
- Crossref に license 欄はなく、刊行版は American Medical Association の著作権表示のみで CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-441（N Engl J Med 2014、PEITHO）— RESTRICTED
- Crossref に license 欄はなく、刊行版は Massachusetts Medical Society の著作権表示のみで CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。PMID 補完候補: 24716681（書誌: 370(15):1402-1411）。

### SRC-442（N Engl J Med 2004、Pengo ら CTEPH）— RESTRICTED
- マスターでは DOI・PMID ともに空欄だったが、PubMed の DOI 検索で本論文を特定した（DOI 10.1056/NEJMoa032274、PMID 15163775）。
- 刊行版は Massachusetts Medical Society の著作権表示のみで CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。DOI・PMID の補完候補として記録する。

### SRC-448（Lancet 1981、MRC 長期酸素療法）— RESTRICTED
- Crossref の license 欄は Elsevier の TDM 利用条件のみで、刊行版に CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。PMID 補完候補: 6110912。

### SRC-473（N Engl J Med 2011、NLST）— RESTRICTED
- PMC 収載分（PMC4356534）は著者原稿のため、刊行版の根拠には使わない。
- 刊行版は Massachusetts Medical Society の著作権表示のみで CC 表示はない（Crossref に license 欄なし）。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-816（StatPearls "Amenorrhea"、NBK482168）— RESTRICTED
- 当初は章ページ末尾のライセンス表示ブロックを取得手段の制約で取り出せず「確認できず」としたが、2026-11-24 に実ブラウザで章ページ（https://www.ncbi.nlm.nih.gov/books/NBK482168/）の末尾表示を直接確認した: 「Copyright © 2024, StatPearls Publishing LLC.」に続き、CC BY-NC-ND 4.0（Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International）で配布される旨の定型文がある。
- 判定: RESTRICTED（CC BY-NC-ND 4.0）。

### SRC-817（J Clin Endocrinol Metab 2017、Endocrine Society ガイドライン）— RESTRICTED
- Crossref に license 欄はなく、刊行版は The Endocrine Society の著作権表示のみで CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-838（Hum Reprod Update 2016、PCOS に関する WHO ガイダンス分析）— RESTRICTED
- Crossref に license 欄はなく、刊行版は著者／Oxford University Press の著作権表示のみで CC 表示はない。
- なお、同テーマの ESHRE ガイドライン Hum Reprod 版（10.1093/humrep/dew027）とは別文献であり、混同しないよう確認した。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-841（Contraception 2011）— RESTRICTED
- Crossref の license 欄は Elsevier の TDM 利用条件のみ。
- PMC 収載分（PMC3638209）は著者原稿（マスターの備考どおり）であり、刊行版の根拠には使わない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-847（Menopause 2022、NAMS ホルモン療法声明）— RESTRICTED
- Crossref に license 欄はなく、刊行版は The North American Menopause Society の著作権表示のみで CC 表示はない（Wolters Kluwer／Ovid 配信）。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-849（J Clin Endocrinol Metab 2019、Endocrine Society ガイドライン）— RESTRICTED
- Crossref に license 欄はなく、刊行版は The Endocrine Society の著作権表示のみで CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-875（J Clin Endocrinol Metab 2014、Endocrine Society ガイドライン）— RESTRICTED
- Crossref に license 欄はなく、刊行版は The Endocrine Society の著作権表示のみで CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-880（Lancet 2016）— RESTRICTED
- Crossref の license 欄は Elsevier の TDM 利用条件のみで、刊行版に CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-881（Nat Rev Dis Primers 2019）— RESTRICTED
- Crossref の license 欄（vor）は Springer Nature の TDM 利用条件ページへのリンクのみで、CC ライセンスの指定はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-910（J Endocrinol Invest 2016）— RESTRICTED
- Crossref の license 欄は Springer の TDM 利用条件のみ（vor に CC の指定なし）。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-911（Oncologist 2011）— RESTRICTED
- PMC 収載の刊行版ページ（PMC3228182）に「©AlphaMed Press」の表示があり、CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。PMCID 補完候補: PMC3228182（刊行版）。

### SRC-912（Thyroid 2016、ATA 甲状腺癌ガイドライン）— RESTRICTED
- PMC 収載の刊行版ページ（PMC4739132）に「Copyright 2016, Mary Ann Liebert, Inc.」の表示があり、CC 表示はない（PMC で無料公開されているが、ライセンスは CC ではない）。
- 判定: RESTRICTED（CC 表示なし）。PMCID 補完候補: PMC4739132（刊行版）。

### SRC-914（Eur J Endocrinol 2021、EUGOGO バセドウ病眼症ガイドライン）— RESTRICTED
- 刊行版 PDF の1ページ目に「© 2021 European Society of Endocrinology Published by Bioscientifica Ltd.」の表示があり、全文中に Creative Commons の記載はない（"Downloaded from Bioscientifica.com … via free access" の注記のみ）。
- 注意: Amsterdam UMC の機関リポジトリのレコードには本論文の出版社版 PDF について「Document license: CC BY」とのメタデータ記載があるが、これはリポジトリ側のメタデータであり、刊行版自体の表示と矛盾する。方法の優先順位（刊行版自体の表示を優先）に従い、リポジトリのメタデータは採用しない。Crossref にも license 欄はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-987（J Basic Clin Physiol Pharmacol 2019、チアミン欠乏）— RESTRICTED
- Crossref に license 欄はなく、刊行版は Walter de Gruyter の著作権表示のみで CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-990（StatPearls "Biochemistry, Fat Soluble Vitamins"、NBK534869）— RESTRICTED
- SRC-816 と同じ理由で当初「確認できず」としたが、2026-11-24 に実ブラウザで章ページ（https://www.ncbi.nlm.nih.gov/books/NBK534869/）の末尾表示を直接確認した: 「Copyright © 2022, StatPearls Publishing LLC.」に続き、CC BY-NC-ND 4.0 で配布される旨の定型文がある。
- 判定: RESTRICTED（CC BY-NC-ND 4.0）。

### SRC-142（Meditsinskiy sovet 2026、Rome V 基準の解説）— OPEN
- マスターでは題名が空欄だったが、Crossref で DOI 10.21518/ms2026-232 から同定した: "Rome V Criteria (2026): Continuity, innovations and major updates", Meditsinskiy sovet（Medical Council）2026;(8):8-21、出版社 Remedium, Ltd.
- 当初は誌のサイトに到達できず「確認できず」としたが、2026-11-24 に実ブラウザで確認できた。誌の編集方針ページ（https://www.med-sovet.pro/jour/about/editorialPolicies）の Open Access Policy の項に、コンテンツは Creative Commons Attribution 4.0 の下で提供される旨の記載があり、購読の項でも電子版は同ライセンスのオープンアクセスである旨が確認できた。
- 論文ページ（https://www.med-sovet.pro/jour/article/view/10201）の下部にも、コンテンツは Creative Commons Attribution 4.0 License の下で提供される旨の表示があり、論文自体への CC BY 4.0 の付与を確認した（著者: Maev IV ほか。表示の抜粋が途中で切れたため、ページ範囲 8-21 はこの画面からは直接確認できていない）。
- 判定: OPEN（CC BY 4.0）。

### SRC-5206（Am J Gastroenterol 2025、ACG 好酸球性食道炎ガイドライン）— RESTRICTED
- PubMed レコードに「Copyright © 2024 by The American College of Gastroenterology.」の表示があり、CC 表示はない。Crossref にも license 欄はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1074（StatPearls "Asteatotic Eczema"、NBK549807）— RESTRICTED
- Bookshelf の章ページ末尾ブロックはテキスト抽出で落ちるため、同章の図ページ（Figure 1 の objectonly ページ）で確認した: 「Copyright © 2026, StatPearls Publishing LLC. This book is distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)」。
- 判定: RESTRICTED（CC BY-NC-ND 4.0）。

### SRC-1075（StatPearls "Nummular Dermatitis"、NBK565878）— RESTRICTED
- 同章の図ページで確認: 「Copyright © 2024, StatPearls Publishing LLC. … Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)」。
- 判定: RESTRICTED（CC BY-NC-ND 4.0）。

### SRC-1080（Am J Clin Dermatol 2015）— RESTRICTED
- Crossref の license 欄は Springer の TDM 利用条件のみ（vor に CC の指定なし）。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1082（Int J Dermatol 2012）— RESTRICTED
- Crossref の license 欄（vor）は Wiley の標準利用条件へのリンクのみで、CC ライセンスではない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1084（J Invest Dermatol 2016）— RESTRICTED
- Crossref の license 欄（vor）は Elsevier のオープンアクセス・ユーザーライセンス（elsevier.com/open-access/userlicense/1.0）へのリンク。これは Elsevier 独自の利用許諾であり、CC ライセンスではない。
- 判定: RESTRICTED（CC 表示なし。Elsevier OA ユーザーライセンス）。

### SRC-1085（J Invest Dermatol 2000、SCORTEN）— RESTRICTED
- Crossref の license 欄（vor）は SRC-1084 と同じ Elsevier のオープンアクセス・ユーザーライセンスへのリンクであり、CC ライセンスではない。
- 判定: RESTRICTED（CC 表示なし。Elsevier OA ユーザーライセンス）。

### SRC-1088（JAMA Dermatol 2018）— RESTRICTED
- Crossref に license 欄はなく、刊行版は American Medical Association の著作権表示のみで CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1089（N Engl J Med 2010、CALISTO）— RESTRICTED
- Crossref に license 欄はなく、刊行版は Massachusetts Medical Society の著作権表示のみで CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1090（Vasa 2020、Hogrefe）— RESTRICTED
- Crossref の license 欄は空（再確認済み）で、刊行版に CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1091（J Am Acad Dermatol 2005）— RESTRICTED
- Crossref の license 欄は Elsevier の TDM 利用条件のみで、刊行版に CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。

### SRC-1092（Indian J Dermatol Venereol Leprol 2016）— RESTRICTED
- 誌の PDF に「This is an open access article distributed under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License」の表示がある。
- 判定: RESTRICTED（CC BY-NC-SA 3.0）。

### SRC-1096（StatPearls "Epidermal Nevus Syndromes"、NBK559003）— RESTRICTED
- SRC-816 と同じ理由で当初「確認できず」としたが、2026-11-24 に実ブラウザで章ページ（https://www.ncbi.nlm.nih.gov/books/NBK559003/）の末尾表示を直接確認した: 「Copyright © 2023, StatPearls Publishing LLC.」に続き、CC BY-NC-ND 4.0 で配布される旨の定型文がある。
- 判定: RESTRICTED（CC BY-NC-ND 4.0）。

### SRC-1097（StatPearls "Nevus of Ota and Ito"、NBK560574）— RESTRICTED
- 同章の図ページ（Figure 1 の objectonly ページ）で確認: 「Copyright © 2023, StatPearls Publishing LLC. This book is distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)」。
- 判定: RESTRICTED（CC BY-NC-ND 4.0）。

### SRC-1100（StatPearls "Kasabach-Merritt Syndrome"、NBK519053）— RESTRICTED
- SRC-816 と同じ理由で当初「確認できず」としたが、2026-11-24 に実ブラウザで章ページ（https://www.ncbi.nlm.nih.gov/books/NBK519053/）の末尾表示を直接確認した: 「Copyright © 2023, StatPearls Publishing LLC.」に続き、CC BY-NC-ND 4.0 で配布される旨の定型文がある。
- 判定: RESTRICTED（CC BY-NC-ND 4.0）。

### SRC-1103（Cardiovasc Diagn Ther 2016）— RESTRICTED
- PMC 収載の刊行版ページ（PMC5220204）のヘッダーに「2016 Cardiovascular Diagnosis and Therapy. All rights reserved.」の表示があり、CC 表示はない。
- 判定: RESTRICTED（CC 表示なし）。PMCID 補完候補: PMC5220204（刊行版）。

## 書誌・識別子の食い違いと補完候補

- **SRC-442**: マスターで DOI・PMID がともに空欄だったものを特定した。DOI 10.1056/NEJMoa032274、PMID 15163775（N Engl J Med 2004;350(22):2257-2264）。
- **SRC-142**: マスターで題名が空欄だったものを Crossref で同定した。"Rome V Criteria (2026): Continuity, innovations and major updates", Meditsinskiy sovet 2026;(8):8-21（Remedium, Ltd.）。
- **PMID 補完候補**（マスター空欄 → PubMed で確認）: SRC-3431 → 35927462、SRC-378 → 41016738、SRC-427 → 18337594、SRC-441 → 24716681、SRC-448 → 6110912。
- **PMCID 補完候補（刊行版として PMC 収載）**: SRC-1875 → PMC6483272、SRC-911 → PMC3228182、SRC-912 → PMC4739132、SRC-1103 → PMC5220204、SRC-1698 → PMC5363978。
- **PMCID（著者原稿。刊行版のライセンス根拠には使わない）**: SRC-1444 → PMC7944998、SRC-473 → PMC4356534、SRC-841 → PMC3638209。
- **SRC-914 の表示の競合**: 機関リポジトリ（Amsterdam UMC）のメタデータは「CC BY」とするが、刊行版自体は「© 2021 European Society of Endocrinology」と表示し CC の記載がない。刊行版を優先し RESTRICTED とした（リポジトリ側でメタデータの出所を確認されたい）。
- 上記以外の対象については、書誌（誌名・巻号・ページ）と DOI・PMID の一致を確認し、食い違いはなかった。

## 機械可読の一覧表

| SRC | 判定 | ライセンスの表示 | 根拠の URL | 備考 |
|---|---|---|---|---|
| SRC-1444 | RESTRICTED | CC表示なし（Crossref vor は Springer Nature の TDM 利用条件のみ） | https://www.springernature.com/gp/researchers/text-and-data-mining | PMC7944998 は著者原稿のため根拠に使わない（PMCID は著者原稿分として補完候補） |
| SRC-1446 | RESTRICTED | © American Academy of Family Physicians（AFP誌標準フッター：私的・非商用利用のみ、その他の権利は留保。CC表示なし） | https://pubmed.ncbi.nlm.nih.gov/38905553/ | AFP誌の論文PDFフッターで確認（第1回のAAFP分と同一根拠） |
| SRC-1545 | RESTRICTED | © American Academy of Family Physicians（同上。CC表示なし） | https://pubmed.ncbi.nlm.nih.gov/23939500/ | AFP誌標準フッターによる |
| SRC-1691 | RESTRICTED | CC表示なし（Wiley 標準利用条件） | http://onlinelibrary.wiley.com/termsAndConditions#vor | Crossref vor の license リンクによる |
| SRC-1698 | RESTRICTED | Copyright © 2017 by the American Thoracic Society（CC表示なし） | https://pmc.ncbi.nlm.nih.gov/articles/PMC5363978/ | PMC 刊行版ページで確認。PMCID 補完候補 PMC5363978（刊行版） |
| SRC-1702 | RESTRICTED | CC表示なし（Wiley 標準利用条件） | http://onlinelibrary.wiley.com/termsAndConditions#vor | Crossref vor の license リンクによる |
| SRC-1718 | RESTRICTED | © American Academy of Neurology（CC表示なし） | https://doi.org/10.1212/01.wnl.0000303813.95800.0d | Crossref に license 欄なし |
| SRC-1875 | RESTRICTED | Copyright © 2017 The Cochrane Collaboration. Published by John Wiley & Sons, Ltd.（CC表示なし） | https://pmc.ncbi.nlm.nih.gov/articles/PMC6483272/ | PMC 刊行版ページで確認。PMCID 補完候補 PMC6483272（刊行版） |
| SRC-1878 | RESTRICTED | CC表示なし（Crossref vor は Springer Nature の TDM 利用条件のみ） | https://www.springernature.com/gp/researchers/text-and-data-mining |  |
| SRC-1929 | RESTRICTED | Copyright © 2022 Neurology India, Neurological Society of India（CC表示なし） | https://doi.org/10.4103/0028-3886.364066 | 出版社プラットフォーム（Ovid）全文フッターで確認 |
| SRC-3431 | RESTRICTED | © American Academy of Pediatrics（CC表示なし） | https://doi.org/10.1542/peds.2022-058859 | PMID 補完候補 35927462（マスター空欄） |
| SRC-378 | RESTRICTED | Copyright ©The authors 2025. For reproduction rights and permissions contact permissions@ersnet.org（CC表示なし） | https://publications.ersnet.org/user-licence | 刊行版PDF 1ページ目の表示と ERS user licence ページ（CC論文には適用されない旨明記）で確認。PMID 補完候補 41016738 |
| SRC-427 | RESTRICTED | CC表示なし（OUP 標準公表・再利用条件） | https://academic.oup.com/pages/standard-publication-reuse-rights | Crossref vor の license リンクによる。PMID 補完候補 18337594 |
| SRC-431 | RESTRICTED | © American Medical Association（CC表示なし） | https://doi.org/10.1001/jama.2012.5669 | Crossref に license 欄なし |
| SRC-441 | RESTRICTED | © Massachusetts Medical Society（CC表示なし） | https://doi.org/10.1056/NEJMoa1302097 | PMID 補完候補 24716681 |
| SRC-442 | RESTRICTED | © Massachusetts Medical Society（CC表示なし） | https://doi.org/10.1056/NEJMoa032274 | マスターで DOI・PMID 空欄 → DOI 10.1056/NEJMoa032274、PMID 15163775 を特定（補完候補） |
| SRC-448 | RESTRICTED | CC表示なし（Elsevier TDM 利用条件のみ） | https://doi.org/10.1016/S0140-6736(81)91970-X | PMID 補完候補 6110912 |
| SRC-473 | RESTRICTED | © Massachusetts Medical Society（CC表示なし） | https://pubmed.ncbi.nlm.nih.gov/21714641/ | PMC4356534 は著者原稿のため根拠に使わない |
| SRC-816 | RESTRICTED | Copyright © 2024, StatPearls Publishing LLC. CC BY-NC-ND 4.0 | https://www.ncbi.nlm.nih.gov/books/NBK482168/ | 2026-11-24 に実ブラウザで章ページ末尾の表示を直接確認（当初は取得手段の制約で確認できず） |
| SRC-817 | RESTRICTED | © The Endocrine Society（CC表示なし） | https://doi.org/10.1210/jc.2017-00131 | Crossref に license 欄なし |
| SRC-838 | RESTRICTED | © The Author / Oxford University Press（CC表示なし） | https://doi.org/10.1093/humupd/dmw025 | Crossref に license 欄なし。同テーマの Hum Reprod 版ガイドラインとは別文献 |
| SRC-841 | RESTRICTED | CC表示なし（Elsevier TDM 利用条件のみ） | https://doi.org/10.1016/j.contraception.2011.01.021 | PMC3638209 は著者原稿のため根拠に使わない |
| SRC-847 | RESTRICTED | © The North American Menopause Society（CC表示なし） | https://doi.org/10.1097/GME.0000000000002028 | Crossref に license 欄なし |
| SRC-849 | RESTRICTED | © The Endocrine Society（CC表示なし） | https://doi.org/10.1210/jc.2019-00221 | Crossref に license 欄なし |
| SRC-875 | RESTRICTED | © The Endocrine Society（CC表示なし） | https://doi.org/10.1210/jc.2014-2700 | Crossref に license 欄なし |
| SRC-880 | RESTRICTED | CC表示なし（Elsevier TDM 利用条件のみ） | https://doi.org/10.1016/S0140-6736(16)30053-8 |  |
| SRC-881 | RESTRICTED | CC表示なし（Crossref vor は Springer Nature の TDM 利用条件のみ） | https://www.springernature.com/gp/researchers/text-and-data-mining |  |
| SRC-910 | RESTRICTED | CC表示なし（Springer、vor は TDM 利用条件のみ） | https://doi.org/10.1007/s40618-015-0391-7 |  |
| SRC-911 | RESTRICTED | ©AlphaMed Press（CC表示なし） | https://pmc.ncbi.nlm.nih.gov/articles/PMC3228182/ | PMC 刊行版ページで確認。PMCID 補完候補 PMC3228182（刊行版） |
| SRC-912 | RESTRICTED | Copyright 2016, Mary Ann Liebert, Inc.（CC表示なし） | https://pmc.ncbi.nlm.nih.gov/articles/PMC4739132/ | PMC 刊行版ページで確認。PMCID 補完候補 PMC4739132（刊行版） |
| SRC-914 | RESTRICTED | © 2021 European Society of Endocrinology Published by Bioscientifica Ltd.（CC表示なし） | https://doi.org/10.1530/EJE-21-0479 | 刊行版PDFで確認。機関リポジトリのメタデータに「CC BY」の記載があるが刊行版の表示と矛盾するため採用しない |
| SRC-987 | RESTRICTED | © Walter de Gruyter（CC表示なし） | https://doi.org/10.1515/jbcpp-2018-0075 | Crossref に license 欄なし |
| SRC-990 | RESTRICTED | Copyright © 2022, StatPearls Publishing LLC. CC BY-NC-ND 4.0 | https://www.ncbi.nlm.nih.gov/books/NBK534869/ | 2026-11-24 に実ブラウザで章ページ末尾の表示を直接確認（SRC-816 と同じ経緯） |
| SRC-142 | OPEN | Creative Commons Attribution 4.0（CC BY 4.0） | https://www.med-sovet.pro/jour/article/view/10201 | 2026-11-24 に実ブラウザで誌の OA 方針ページと論文ページ下部の表示を確認。題名は Crossref で同定（本文参照） |
| SRC-5206 | RESTRICTED | Copyright © 2024 by The American College of Gastroenterology（CC表示なし） | https://pubmed.ncbi.nlm.nih.gov/39745304/ | PubMed レコードの表示で確認。Crossref に license 欄なし |
| SRC-1074 | RESTRICTED | Copyright © 2026, StatPearls Publishing LLC. CC BY-NC-ND 4.0 | https://www.ncbi.nlm.nih.gov/sites/books/NBK549807/figure/article-20893.image.f1/?report=objectonly | Bookshelf 同章の図ページ末尾ブロックで確認 |
| SRC-1075 | RESTRICTED | Copyright © 2024, StatPearls Publishing LLC. CC BY-NC-ND 4.0 | https://www.ncbi.nlm.nih.gov/sites/books/NBK565878/figure/article-20381.image.f1/?report=objectonly | Bookshelf 同章の図ページ末尾ブロックで確認 |
| SRC-1080 | RESTRICTED | CC表示なし（Springer、vor は TDM 利用条件のみ） | https://doi.org/10.1007/s40257-015-0154-4 |  |
| SRC-1082 | RESTRICTED | CC表示なし（Wiley 標準利用条件） | http://onlinelibrary.wiley.com/termsAndConditions#vor | Crossref vor の license リンクによる |
| SRC-1084 | RESTRICTED | CC表示なし（Elsevier のオープンアクセス・ユーザーライセンス。CC ではない） | http://www.elsevier.com/open-access/userlicense/1.0/ | Crossref vor の license リンクによる |
| SRC-1085 | RESTRICTED | CC表示なし（Elsevier のオープンアクセス・ユーザーライセンス。CC ではない） | https://www.elsevier.com/open-access/userlicense/1.0/ | Crossref vor の license リンクによる |
| SRC-1088 | RESTRICTED | © American Medical Association（CC表示なし） | https://doi.org/10.1001/jamadermatol.2017.5980 | マスターの備考どおり。Crossref に license 欄なし |
| SRC-1089 | RESTRICTED | © Massachusetts Medical Society（CC表示なし） | https://doi.org/10.1056/NEJMoa0912072 | Crossref に license 欄なし |
| SRC-1090 | RESTRICTED | CC表示なし（Hogrefe） | https://doi.org/10.1024/0301-1526/a000838 | Crossref の license 欄は空（再確認済み） |
| SRC-1091 | RESTRICTED | CC表示なし（Elsevier TDM 利用条件のみ） | https://doi.org/10.1016/j.jaad.2004.11.051 |  |
| SRC-1092 | RESTRICTED | CC BY-NC-SA 3.0 | https://doi.org/10.4103/0378-6323.191134 | 誌の PDF の表示で確認 |
| SRC-1096 | RESTRICTED | Copyright © 2023, StatPearls Publishing LLC. CC BY-NC-ND 4.0 | https://www.ncbi.nlm.nih.gov/books/NBK559003/ | 2026-11-24 に実ブラウザで章ページ末尾の表示を直接確認（SRC-816 と同じ経緯） |
| SRC-1097 | RESTRICTED | Copyright © 2023, StatPearls Publishing LLC. CC BY-NC-ND 4.0 | https://www.ncbi.nlm.nih.gov/sites/books/NBK560574/figure/article-110341.image.f1/?report=objectonly | Bookshelf 同章の図ページ末尾ブロックで確認 |
| SRC-1100 | RESTRICTED | Copyright © 2023, StatPearls Publishing LLC. CC BY-NC-ND 4.0 | https://www.ncbi.nlm.nih.gov/books/NBK519053/ | 2026-11-24 に実ブラウザで章ページ末尾の表示を直接確認（SRC-816 と同じ経緯） |
| SRC-1103 | RESTRICTED | 2016 Cardiovascular Diagnosis and Therapy. All rights reserved.（CC表示なし） | https://pmc.ncbi.nlm.nih.gov/articles/PMC5220204/ | PMC 刊行版ページで確認。PMCID 補完候補 PMC5220204（刊行版） |
