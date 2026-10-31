# 第39回（ML・LY）血液・造血器疾患 事実票

- 対象：医学各論 Ⅶ-2（白血球系疾患とその他の骨髄性疾患、ML 8項目）と Ⅶ-3（リンパ系疾患、LY 15項目）
- 件数：49件（ML 17件・LY 32件）で、依頼文の目安（約49件）のとおり。ID の欠番はない
- 新規出典は SRC-2551〜2590 の40件、既存出典の再利用は5件（SRC-547・SRC-599・SRC-615・SRC-979・SRC-2031）。割り当ての残り SRC-2591〜2640 は未使用
- 出典リサーチのメモ（39_research_3.md）の手元ファイルが途中で切れていたため、パートCの不足分（MGUS・アミロイドーシス・HLH の節）は組み立て時に一次資料の抄録を直接開いて検証し直した（詳細は第4節パートCの申し送り）

## 1. 抽出元ホワイトリスト

| SRC | DOI | 出典 | source_class |
|---|---|---|---|
| SRC-547 | 10.21037/cco-2025-1-134 | Sapuppo G, Frazzetto S, Pirosa MC, Zucca E. Epidemiology, diagnosis, and treatment of primary pulmonary mucosa-associated lymphoid tissue lymphoma. Chin Clin Oncol. 2026;15(3):46. | RESTRICTED |
| SRC-599 | 10.1182/blood-2014-04-570010 | Palladini G, Hegenbart U, Milani P, et al. A staging system for renal outcome and early markers of renal response to chemotherapy in AL amyloidosis. Blood. 2014;124(15):2325-2332 | RESTRICTED |
| SRC-615 | 10.1016/j.kint.2020.11.010 | Bridoux F, Leung N, Belmouaz M, Royal V, Ronco P, Nasr SH. Management of acute kidney injury in symptomatic multiple myeloma. Kidney Int. 2021;99(3):570-580 | RESTRICTED |
| SRC-979 | 10.1016/S0140-6736(15)01274-X | Wechalekar AD, Gillmore JD, Hawkins PN. Systemic amyloidosis. Lancet. 2016;387:2641-2654 | UNKNOWN |
| SRC-2031 | 10.1016/j.jcv.2018.03.001 | Dunmire SK, Verghese PS, Balfour HH Jr. Primary Epstein-Barr virus infection. J Clin Virol. 2018;102:84-92 | RESTRICTED |
| SRC-2551 | 10.3390/jcm8091351 | Andrès E, Lorenzo-Villalba N, Zulfiqar AA, et al. State of Art of Idiosyncratic Drug-Induced Neutropenia or Agranulocytosis, with a Focus on Biotherapies. J Clin Med. 2019;8(9):1351. | OPEN |
| SRC-2552 | 10.1093/cid/cir073 | Freifeld AG, Bow EJ, Sepkowitz KA, et al. Clinical Practice Guideline for the Use of Antimicrobial Agents in Neutropenic Patients with Cancer: 2010 Update by the Infectious Diseases Society of America. Clin Infect Dis. 2011;52(4):e56-e93. | RESTRICTED |
| SRC-2553 | 10.1182/blood.2022016867 | Döhner H, Wei AH, Appelbaum FR, et al. Diagnosis and management of AML in adults: 2022 recommendations from an international expert panel on behalf of the ELN. Blood. 2022;140(12):1345-1377. | RESTRICTED |
| SRC-2554 | 10.1056/NEJMoa2012971 | DiNardo CD, Jonas BA, Pullarkat V, et al. Azacitidine and Venetoclax in Previously Untreated Acute Myeloid Leukemia. N Engl J Med. 2020;383(7):617-629. | RESTRICTED |
| SRC-2555 | 10.1056/NEJMoa1614359 | Stone RM, Mandrekar SJ, Sanford BL, et al. Midostaurin plus Chemotherapy for Acute Myeloid Leukemia with a FLT3 Mutation. N Engl J Med. 2017;377(5):454-464. | RESTRICTED |
| SRC-2556 | 10.1056/NEJMoa1300874 | Lo-Coco F, Avvisati G, Vignetti M, et al. Retinoic Acid and Arsenic Trioxide for Acute Promyelocytic Leukemia. N Engl J Med. 2013;369(2):111-121. | RESTRICTED |
| SRC-2557 | 10.1038/s41375-025-02664-w | Apperley JF, Milojkovic D, Cross NCP, et al. 2025 European LeukemiaNet recommendations for the management of chronic myeloid leukemia. Leukemia. 2025;39(8):1797-1813. | OPEN |
| SRC-2558 | 10.1056/NEJMoa062867 | Druker BJ, Guilhot F, O'Brien SG, et al. Five-year follow-up of patients receiving imatinib for chronic myeloid leukemia. N Engl J Med. 2006;355(23):2408-2417. | RESTRICTED |
| SRC-2559 | 10.1016/S1470-2045(10)70233-3 | Mahon FX, Réa D, Guilhot J, et al. Discontinuation of imatinib in patients with chronic myeloid leukaemia who have maintained complete molecular remission for at least 2 years: the prospective, multicentre Stop Imatinib (STIM) trial. Lancet Oncol. 2010;11(11):1029-1035. | RESTRICTED |
| SRC-2560 | 10.1182/blood-2009-09-245837 | Passamonti F, Cervantes F, Vannucchi AM, et al. A dynamic prognostic model to predict survival in primary myelofibrosis: a study by the IWG-MRT (DIPSS). Blood. 2010;115(9):1703-1708. | RESTRICTED |
| SRC-2561 | 10.1056/NEJMoa1110557 | Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. N Engl J Med. 2012;366(9):799-807. | RESTRICTED |
| SRC-2562 | 10.1182/blood-2012-07-444067 | Barbui T, Finazzi G, Carobbio A, et al. Development and validation of an International Prognostic Score of thrombosis in World Health Organization-essential thrombocythemia (IPSET-thrombosis). Blood. 2012;120(26):5128-5133. | RESTRICTED |
| SRC-2563 | 10.1038/bcj.2015.94 | Barbui T, Vannucchi AM, Buxhofer-Ausch V, et al. Practice-relevant revision of IPSET-thrombosis based on 1019 patients with WHO-defined essential thrombocythemia. Blood Cancer J. 2015;5(11):e369. | OPEN |
| SRC-2564 | 10.1016/S0140-6736(05)71142-9 | Baxter EJ, Scott LM, Campbell PJ, et al. Acquired mutation of the tyrosine kinase JAK2 in human myeloproliferative disorders. Lancet. 2005;365(9464):1054-1061. | RESTRICTED |
| SRC-2565 | 10.1056/NEJMoa1409002 | Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. N Engl J Med. 2015;372(5):426-435. | RESTRICTED |
| SRC-2566 | 10.1056/NEJMoa025217 | Cools J, DeAngelo DJ, Gotlib J, et al. A tyrosine kinase created by fusion of the PDGFRA and FIP1L1 genes as a therapeutic target of imatinib in idiopathic hypereosinophilic syndrome. N Engl J Med. 2003;348(13):1201-1214. | RESTRICTED |
| SRC-2567 | 10.1016/j.ejim.2006.04.004 | Sakka V, Tsiodras S, Giamarellos-Bourboulis EJ, Giamarellou H. An update on the etiology and diagnostic evaluation of a leukemoid reaction. Eur J Intern Med. 2006;17(6):394-398. | RESTRICTED |
| SRC-2568 | 10.1038/bcj.2017.53 | Terwilliger T, Abdul-Hay M. Acute lymphoblastic leukemia: a comprehensive review and 2017 update. Blood Cancer J. 2017;7(6):e577. | OPEN |
| SRC-2569 | 10.1007/s12185-024-03836-7 | Hatta Y, Izutsu K, Onizuka M, et al. JSH practical guidelines for hematological malignancies, 2023: leukemia-3. Acute lymphoblastic leukemia/lymphoblastic lymphoma: ALL/LBL. Int J Hematol. 2024;120(4):394-413. | RESTRICTED |
| SRC-2570 | 10.1007/s12185-025-04079-w | Kusumoto S, Tomita A, et al. JSH practical guidelines for hematological malignancies, 2023: II. Lymphoma 10. Hodgkin lymphoma (HL). Int J Hematol. 2025;122(6):781-802. | RESTRICTED |
| SRC-2571 | 10.1056/NEJMoa2206125 | Ansell SM, Radford J, Connors JM, et al. Overall Survival with Brentuximab Vedotin in Stage III or IV Hodgkin's Lymphoma. N Engl J Med. 2022;387(4):310-320. | RESTRICTED |
| SRC-2572 | 10.1056/NEJMoa2405888 | Herrera AF, LeBlanc M, Castellino SM, et al. Nivolumab+AVD in Advanced-Stage Classic Hodgkin's Lymphoma. N Engl J Med. 2024;391(15):1379-1389. | RESTRICTED |
| SRC-2573 | 10.1182/blood-2017-09-806398 | Hallek M, Cheson BD, Catovsky D, et al. iwCLL guidelines for diagnosis, indications for treatment, response assessment, and supportive management of CLL. Blood. 2018;131(25):2745-2760. | RESTRICTED |
| SRC-2574 | 10.1016/j.annonc.2020.09.019 | Eichhorst B, Robak T, Montserrat E, et al. Chronic lymphocytic leukaemia: ESMO Clinical Practice Guidelines for diagnosis, treatment and follow-up. Ann Oncol. 2021;32(1):23-33. | RESTRICTED |
| SRC-2575 | 10.1056/NEJMoa1614598 | Marcus R, Davies A, Ando K, et al. Obinutuzumab for the First-Line Treatment of Follicular Lymphoma. N Engl J Med. 2017;377(14):1331-1344. | RESTRICTED |
| SRC-2576 | 10.1007/s12185-025-03922-4 | Izutsu K, Fukuhara N, et al. JSH practical guidelines for hematological malignancies, 2023: II. Lymphoma-1. Follicular lymphoma (FL). Int J Hematol. 2025;121(5):577-585. | RESTRICTED |
| SRC-2577 | 10.1056/NEJMoa2115304 | Tilly H, Morschhauser F, Sehn LH, et al. Polatuzumab Vedotin in Previously Untreated Diffuse Large B-Cell Lymphoma. N Engl J Med. 2022;386(4):351-363. | RESTRICTED |
| SRC-2578 | 10.1007/s12185-025-03997-z | Ohmachi K, et al. JSH practical guidelines for hematological malignancies, 2023: II. Lymphoma 5. Diffuse large B-cell lymphoma, not otherwise specified (DLBCL, NOS). Int J Hematol. 2025;122(1):3-16. | OPEN |
| SRC-2579 | 10.1007/s12185-025-03947-9 | Yoshida I, et al. JSH Practical Guidelines for Hematological Malignancies, 2023: II. Lymphoma-2. Marginal zone lymphoma. Int J Hematol. 2025;121(6):725-739. | RESTRICTED |
| SRC-2580 | 10.1056/NEJMoa1501548 | Treon SP, Tripsas CK, Meid K, et al. Ibrutinib in previously treated Waldenström's macroglobulinemia. N Engl J Med. 2015;372(15):1430-1440. | RESTRICTED |
| SRC-2581 | 10.1056/NEJMoa1308392 | Dunleavy K, Pittaluga S, Shovlin M, et al. Low-Intensity Therapy in Adults with Burkitt's Lymphoma. N Engl J Med. 2013;369(20):1915-1925. | RESTRICTED |
| SRC-2582 | 10.1016/S1470-2045(14)70442-5 | Rajkumar SV, Dimopoulos MA, Palumbo A, et al. International Myeloma Working Group updated criteria for the diagnosis of multiple myeloma. Lancet Oncol. 2014;15(12):e538-e548 | RESTRICTED |
| SRC-2583 | null | 日本血液学会 編. 造血器腫瘍診療ガイドライン 第3.1版（2024年版）第Ⅲ章 骨髄腫. 日本血液学会ウェブサイト | RESTRICTED |
| SRC-2584 | 10.1200/JCO.2015.61.2267 | Palumbo A, Avet-Loiseau H, Oliva S, et al. Revised International Staging System for Multiple Myeloma: A Report From International Myeloma Working Group. J Clin Oncol. 2015;33(26):2863-2869 | RESTRICTED |
| SRC-2585 | 10.1056/NEJMoa01133202 | Kyle RA, Therneau TM, Rajkumar SV, et al. A long-term study of prognosis in monoclonal gammopathy of undetermined significance. N Engl J Med. 2002;346(8):564-569 | RESTRICTED |
| SRC-2586 | 10.1111/j.1365-2141.1991.tb08051.x | Shimoyama M; Lymphoma Study Group. Diagnostic criteria and classification of clinical subtypes of adult T-cell leukaemia-lymphoma. Br J Haematol. 1991;79(3):428-437 | RESTRICTED |
| SRC-2587 | 10.1182/blood-2015-03-632489 | Katsuya H, Ishitsuka K, Utsunomiya A, et al. Treatment and survival among 1594 patients with ATL. Blood. 2015;126(24):2570-2577 | RESTRICTED |
| SRC-2588 | 10.1016/S0140-6736(18)32984-2 | Horwitz S, O'Connor OA, Pro B, et al. Brentuximab vedotin with chemotherapy for CD30-positive peripheral T-cell lymphoma (ECHELON-2): a global, double-blind, randomised, phase 3 trial. Lancet. 2019;393(10168):229-240 | RESTRICTED |
| SRC-2589 | 10.1002/pbc.21039 | Henter JI, Horne A, Aricó M, et al. HLH-2004: Diagnostic and therapeutic guidelines for hemophagocytic lymphohistiocytosis. Pediatr Blood Cancer. 2007;48(2):124-131 | RESTRICTED |
| SRC-2590 | 10.1002/art.38690 | Fardet L, Galicier L, Lambotte O, et al. Development and validation of the HScore, a score for the diagnosis of reactive hemophagocytic syndrome. Arthritis Rheumatol. 2014;66(9):2613-2620 | RESTRICTED |

## 2. 事実票

```yaml
- id: ML-001
  domain: ML
  subdomain: 薬剤性無顆粒球症
  assertion:
    plain_statement_ja: 薬剤性無顆粒球症は、まれな特発性（idiosyncratic）の薬剤性有害事象であり、生物学的製剤を含むさまざまな薬剤が原因となりうる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2551
    source: Andrès E, Lorenzo-Villalba N, Zulfiqar AA, et al. State of Art of Idiosyncratic Drug-Induced Neutropenia or Agranulocytosis, with a Focus on Biotherapies. J Clin Med. 2019;8(9):1351.
    doi: 10.3390/jcm8091351
    pmid: '31480527'
    pmcid: PMC6788182
    url: https://doi.org/10.3390/jcm8091351
    source_license: CC BY 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 総説（2010〜2019年の文献を対象）の抄録で確認した範囲である。個別薬剤ごとの頻度や国内での発症状況は本出典では確認していない。発熱を伴う場合の管理は ML-002 を参照。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-A-①（薬剤性無顆粒球症、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-023 (id: Jlvnlbs)；TBL-02-01-007 (id: JlAKpV4)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-002
  domain: ML
  subdomain: 薬剤性無顆粒球症
  assertion:
    plain_statement_ja: 発熱性好中球減少症の管理では、合併症のリスクを高リスクと低リスクに層別化することが出発点となり、すべての患者に対してグラム陽性菌とグラム陰性菌の双方をカバーする広域抗菌薬を速やかに経験的に投与する。
    condition:
      region: 米国
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2552
    source: 'Freifeld AG, Bow EJ, Sepkowitz KA, et al. Clinical Practice Guideline for the Use of Antimicrobial Agents in Neutropenic Patients with Cancer: 2010 Update by the Infectious Diseases Society of America. Clin Infect Dis. 2011;52(4):e56-e93.'
    doi: 10.1093/cid/cir073
    pmid: '21258094'
    pmcid: null
    url: https://doi.org/10.1093/cid/cir073
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国感染症学会（IDSA）ガイドラインの抄録で確認した範囲である。発熱の定義は国内の発熱性好中球減少症診療ガイドライン（腋窩温37.5℃以上等）と異なるため、日本の診療では国内ガイドラインを併せて参照すること。個別の抗菌薬の国内承認・保険適用は本カードでは扱っていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-A-①（薬剤性無顆粒球症、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-023 (id: Jlvnlbs)；TBL-02-01-009 (id: JlAKpWA)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-003
  domain: ML
  subdomain: 急性骨髄性白血病
  assertion:
    plain_statement_ja: ELNの2022年勧告では、急性骨髄性白血病の遺伝子リスク分類と治療効果判定の基準が改訂され、ゲノム診断と測定可能残存病変（MRD）の評価が診療に組み込まれた。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2553
    source: 'Döhner H, Wei AH, Appelbaum FR, et al. Diagnosis and management of AML in adults: 2022 recommendations from an international expert panel on behalf of the ELN. Blood. 2022;140(12):1345-1377.'
    doi: 10.1182/blood.2022016867
    pmid: '35797463'
    pmcid: null
    url: https://doi.org/10.1182/blood.2022016867
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 抄録で確認した範囲である。遺伝子リスク分類の個別の遺伝子異常の一覧は抄録の範囲外であり、主張に含めていない（組み立て時に全文で照合すること）。分類の土台にはWHO分類第5版（HAEM5、2022）とICC 2022も併存し、版による食い違いがありうる。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-①（急性骨髄性白血病、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；PS-02-02-04 (id: JkxnuPY)；TBL-01-00-621 (id: JlvnmaE)；TBL-02-01-021 (id: JlAKpW0)；TBL-02-01-018 (id: JlAKpWo)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-004
  domain: ML
  subdomain: 急性骨髄性白血病
  assertion:
    plain_statement_ja: 強力化学療法が適応とならない未治療の急性骨髄性白血病では、アザシチジンにベネトクラクスを併用すると、アザシチジン単独と比べて全生存期間が延長し（中央値14.7か月対9.6か月、死亡のハザード比0.66）、完全寛解率も高かった（36.7%対17.9%）。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2554
    source: DiNardo CD, Jonas BA, Pullarkat V, et al. Azacitidine and Venetoclax in Previously Untreated Acute Myeloid Leukemia. N Engl J Med. 2020;383(7):617-629.
    doi: 10.1056/NEJMoa2012971
    pmid: '32786187'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2012971
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: VIALE-A試験（431例、年齢中央値76歳）の抄録で確認した数値である。発熱性好中球減少症は併用群で多かった（42%対19%）。ベネトクラクスは2021年3月23日に国内で急性骨髄性白血病の適応追加承認を取得している（発売元の発表で確認）。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-①（急性骨髄性白血病、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-04 (id: JkxnuPY)；TBL-01-00-621 (id: JlvnmaE)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-005
  domain: ML
  subdomain: 急性骨髄性白血病
  assertion:
    plain_statement_ja: 新規診断のFLT3変異陽性急性骨髄性白血病では、標準化学療法にミドスタウリンを追加すると、全生存と無イベント生存がいずれも延長した（いずれもハザード比0.78）。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2555
    source: Stone RM, Mandrekar SJ, Sanford BL, et al. Midostaurin plus Chemotherapy for Acute Myeloid Leukemia with a FLT3 Mutation. N Engl J Med. 2017;377(5):454-464.
    doi: 10.1056/NEJMoa1614359
    pmid: '28644114'
    pmcid: PMC5754190
    url: https://doi.org/10.1056/NEJMoa1614359
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: RATIFY試験（717例、18〜59歳）の抄録で確認した数値であり、効果はFLT3変異のサブタイプを通じて一貫していた。ミドスタウリンの国内承認は出典リサーチの範囲で確認できなかった（国内の適応は未確認）。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-①（急性骨髄性白血病、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-04 (id: JkxnuPY)；TBL-01-00-621 (id: JlvnmaE)；TBL-02-01-021 (id: JlAKpW0)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-006
  domain: ML
  subdomain: 急性骨髄性白血病
  assertion:
    plain_statement_ja: 低〜中間リスクの急性前骨髄球性白血病では、全トランスレチノイン酸と三酸化二ヒ素の併用は、全トランスレチノイン酸と化学療法の併用と比べて2年無イベント生存率が高く（97%対86%）、血液毒性と感染は少なかった。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2556
    source: Lo-Coco F, Avvisati G, Vignetti M, et al. Retinoic Acid and Arsenic Trioxide for Acute Promyelocytic Leukemia. N Engl J Med. 2013;369(2):111-121.
    doi: 10.1056/NEJMoa1300874
    pmid: '23841729'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1300874
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: APL0406試験（白血球数10×10⁹/L以下の低〜中間リスクが対象）の抄録で確認した数値である。完全寛解は併用群で評価可能例の全例、化学療法群で95%であった。三酸化二ヒ素製剤の国内適応範囲（初回治療への拡大の有無）は未確認であり、組み立て時にPMDAで確認すること。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-①（急性骨髄性白血病、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-04 (id: JkxnuPY)；TBL-01-00-621 (id: JlvnmaE)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-007
  domain: ML
  subdomain: 慢性骨髄性白血病
  assertion:
    plain_statement_ja: 慢性骨髄性白血病の管理に関するELNの2025年勧告は現行の国際指針であり、WHOによる慢性期と芽球期の2相への再分類を反映し、分子学的マイルストーン未達時の対応は一律の治療変更ではなく個別の事情を踏まえて判断するとした。
    condition:
      region: 欧州
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2557
    source: Apperley JF, Milojkovic D, Cross NCP, et al. 2025 European LeukemiaNet recommendations for the management of chronic myeloid leukemia. Leukemia. 2025;39(8):1797-1813.
    doi: 10.1038/s41375-025-02664-w
    pmid: '40646132'
    pmcid: PMC12310532
    url: https://doi.org/10.1038/s41375-025-02664-w
    source_license: CC BY 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 抄録で確認した範囲である。ELN 2020年勧告は旧版であり、本カードは2025年版に基づく。分類の版の食い違いとして、WHO分類第5版（HAEM5）では移行期を置かない2相性に整理された一方、国内ガイドライン（日本血液学会2023年版）の記載とはずれる部分がありうる。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-②（慢性骨髄性白血病、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-622 (id: JlvnmaM)；TBL-02-01-021 (id: JlAKpW0)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-008
  domain: ML
  subdomain: 慢性骨髄性白血病
  assertion:
    plain_statement_ja: 慢性骨髄性白血病の初回治療としてのイマチニブでは、60か月時点で完全細胞遺伝学的寛解の累積最良達成率は87%、全生存率は89%であり、移行期・芽球転化への進行は推定7%であった。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2558
    source: Druker BJ, Guilhot F, O'Brien SG, et al. Five-year follow-up of patients receiving imatinib for chronic myeloid leukemia. N Engl J Med. 2006;355(23):2408-2417.
    doi: 10.1056/NEJMoa062867
    pmid: '17151364'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa062867
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: IRIS試験5年追跡の抄録で確認した数値である。イマチニブは国内承認・保険適用のある薬剤である（個別の承認年の照合はしていない）。SRC-033（イマチニブの消化管間質腫瘍の試験）は適応が異なるため本項目の出典にしていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-②（慢性骨髄性白血病、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-622 (id: JlvnmaM)；TBL-02-01-018 (id: JlAKpWo)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-009
  domain: ML
  subdomain: 慢性骨髄性白血病
  assertion:
    plain_statement_ja: 完全分子学的寛解を少なくとも2年維持した慢性骨髄性白血病でイマチニブを中止すると、約6割が再発する（12か月時点の完全分子学的寛解維持率は41%）が、再発例は全例イマチニブの再開に反応した。
    condition:
      region: 欧州
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2559
    source: 'Mahon FX, Réa D, Guilhot J, et al. Discontinuation of imatinib in patients with chronic myeloid leukaemia who have maintained complete molecular remission for at least 2 years: the prospective, multicentre Stop Imatinib (STIM) trial. Lancet Oncol. 2010;11(11):1029-1035.'
    doi: 10.1016/S1470-2045(10)70233-3
    pmid: '20965785'
    pmcid: null
    url: https://doi.org/10.1016/S1470-2045(10)70233-3
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: STIM試験（12か月以上追跡できた69例）の抄録で確認した数値であり、再発の大半は中止後6か月以内であった。イマチニブは国内承認・保険適用のある薬剤である。治療中止の判断はELN 2025年勧告などの現行指針に基づく。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-②（慢性骨髄性白血病、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-622 (id: JlvnmaM)；TBL-02-01-021 (id: JlAKpW0)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-010
  domain: ML
  subdomain: 原発性骨髄線維症
  assertion:
    plain_statement_ja: 原発性骨髄線維症のDIPSSは、年齢65歳超、ヘモグロビン10 g/dL未満、白血球数25×10⁹/L超、末梢血芽球1%以上、全身症状の5因子で低・中間-1・中間-2・高の4群に分ける動的予後モデルであり、診断時だけでなく経過中のどの時点でも適用できる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2560
    source: 'Passamonti F, Cervantes F, Vannucchi AM, et al. A dynamic prognostic model to predict survival in primary myelofibrosis: a study by the IWG-MRT (DIPSS). Blood. 2010;115(9):1703-1708.'
    doi: 10.1182/blood-2009-09-245837
    pmid: '20008785'
    pmcid: null
    url: https://doi.org/10.1182/blood-2009-09-245837
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原発性骨髄線維症525例の検討に基づく原著の抄録で確認した内容である。各リスク群の生存期間の数値は抄録の範囲外であり、主張に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-③（原発性骨髄線維症、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-627 (id: Jlvnmao)；TBL-02-01-018 (id: JlAKpWo)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-011
  domain: ML
  subdomain: 原発性骨髄線維症
  assertion:
    plain_statement_ja: 中間-2〜高リスクの骨髄線維症では、ルキソリチニブはプラセボと比べて24週時点の脾容積35%以上の縮小（41.9%対0.7%）と総症状スコア50%以上の改善（45.9%対5.3%）をもたらし、死亡も少なかった（ハザード比0.50）。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2561
    source: Verstovsek S, Mesa RA, Gotlib J, et al. A double-blind, placebo-controlled trial of ruxolitinib for myelofibrosis. N Engl J Med. 2012;366(9):799-807.
    doi: 10.1056/NEJMoa1110557
    pmid: '22375971'
    pmcid: PMC4822164
    url: https://doi.org/10.1056/NEJMoa1110557
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: COMFORT-I試験の抄録で確認した数値である。有害事象で最も多かったのは貧血と血小板減少であった。ルキソリチニブは骨髄線維症の適応で2014年7月4日に国内承認されている（製造販売業者の資料で確認）。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-③（原発性骨髄線維症、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-627 (id: Jlvnmao)；TBL-02-01-018 (id: JlAKpWo)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-012
  domain: ML
  subdomain: 本態性血小板血症
  assertion:
    plain_statement_ja: 本態性血小板血症のIPSET-thrombosisは、血栓症の既往2点、JAK2 V617F変異2点、60歳超1点、心血管リスク因子1点の合計点で血栓症リスクを低・中間・高の3群に分けるスコアであり、血栓発症率は低リスク群で年1.03%、高リスク群で年2.35%であった。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2562
    source: Barbui T, Finazzi G, Carobbio A, et al. Development and validation of an International Prognostic Score of thrombosis in World Health Organization-essential thrombocythemia (IPSET-thrombosis). Blood. 2012;120(26):5128-5133.
    doi: 10.1182/blood-2012-07-444067
    pmid: '23033268'
    pmcid: null
    url: https://doi.org/10.1182/blood-2012-07-444067
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: WHO定義の本態性血小板血症891例に基づく原著の抄録で確認した内容であり、配点も抄録の記載に基づく。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-④（本態性血小板血症、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-626 (id: Jlvnmak)；TBL-02-01-021 (id: JlAKpW0)；TBL-02-01-015 (id: JlAKpWY)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-013
  domain: ML
  subdomain: 本態性血小板血症
  assertion:
    plain_statement_ja: IPSET-thrombosisには、WHO定義の本態性血小板血症1,019例に基づく実臨床向けの改訂版があり、血栓症リスクの層別が見直された。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2563
    source: Barbui T, Vannucchi AM, Buxhofer-Ausch V, et al. Practice-relevant revision of IPSET-thrombosis based on 1019 patients with WHO-defined essential thrombocythemia. Blood Cancer J. 2015;5(11):e369.
    doi: 10.1038/bcj.2015.94
    pmid: '26617062'
    pmcid: PMC4670947
    url: https://doi.org/10.1038/bcj.2015.94
    source_license: CC BY 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 改訂版の書誌は確認したが、PubMedに抄録がなく、リスク群の再編の詳細は未確認であるため主張に含めていない。詳細はPMC全文（PMC4670947）で照合できる。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-④（本態性血小板血症、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-626 (id: Jlvnmak)；TBL-02-01-015 (id: JlAKpWY)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-014
  domain: ML
  subdomain: 真性赤血球増加症
  assertion:
    plain_statement_ja: JAK2 V617F変異は後天性の体細胞変異であり、陽性率は真性赤血球増加症で97%、本態性血小板血症で57%、特発性骨髄線維症で50%であった。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2564
    source: Baxter EJ, Scott LM, Campbell PJ, et al. Acquired mutation of the tyrosine kinase JAK2 in human myeloproliferative disorders. Lancet. 2005;365(9464):1054-1061.
    doi: 10.1016/S0140-6736(05)71142-9
    pmid: '15781101'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(05)71142-9
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原著の抄録で確認した数値であり、各疾患の例数は真性赤血球増加症73例、本態性血小板血症51例、特発性骨髄線維症16例と小さい。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-⑤（真性赤血球増加症、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-625 (id: Jlvnmac)；TBL-02-01-021 (id: JlAKpW0)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-015
  domain: ML
  subdomain: 真性赤血球増加症
  assertion:
    plain_statement_ja: ハイドロキシウレアに抵抗性または不耐容で脾腫のある真性赤血球増加症では、ルキソリチニブは標準治療と比べて、32週時点のヘマトクリット制御と脾容積35%以上の縮小を合わせた主要評価項目の達成率が高かった（21%対1%）。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2565
    source: Vannucchi AM, Kiladjian JJ, Griesshammer M, et al. Ruxolitinib versus standard therapy for the treatment of polycythemia vera. N Engl J Med. 2015;372(5):426-435.
    doi: 10.1056/NEJMoa1409002
    pmid: '25629741'
    pmcid: PMC4358820
    url: https://doi.org/10.1056/NEJMoa1409002
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: RESPONSE試験の抄録で確認した数値である。内訳はヘマトクリット制御60%対20%、脾容積35%以上の縮小38%対1%であった。ルキソリチニブの真性赤血球増加症への効能追加（既存治療が効果不十分又は不適当な場合に限る）は2015年9月に国内承認されている（製造販売業者の資料で確認）。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-⑤（真性赤血球増加症、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-625 (id: Jlvnmac)；TBL-02-01-021 (id: JlAKpW0)；TBL-02-01-015 (id: JlAKpWY)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-016
  domain: ML
  subdomain: 慢性好酸球性白血病
  assertion:
    plain_statement_ja: FIP1L1とPDGFRAの融合遺伝子は恒常的に活性化したチロシンキナーゼを作りイマチニブで阻害され、特発性好酸球増多症候群16例中9例に検出され、イマチニブを投与された11例中9例で3か月を超える奏効（好酸球数の正常化）が得られた。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2566
    source: Cools J, DeAngelo DJ, Gotlib J, et al. A tyrosine kinase created by fusion of the PDGFRA and FIP1L1 genes as a therapeutic target of imatinib in idiopathic hypereosinophilic syndrome. N Engl J Med. 2003;348(13):1201-1214.
    doi: 10.1056/NEJMoa025217
    pmid: '12660384'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa025217
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原著の抄録で確認した内容である。融合遺伝子は染色体4q12の間質性欠失により生じる。イマチニブは国内承認・保険適用のある薬剤だが、好酸球増多症候群・慢性好酸球性白血病に対する国内適応の有無は未確認である。慢性好酸球性白血病とチロシンキナーゼ融合遺伝子で定義される腫瘍群との切り分けはWHO分類第5版（HAEM5）のカテゴリ構成に基づく。別表1には本項目に対応する行がないため付けていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-B-⑥（慢性好酸球性白血病、c）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-007 (id: JlAKpV4)；TBL-02-01-021 (id: JlAKpW0)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: ML-017
  domain: ML
  subdomain: 類白血病反応
  assertion:
    plain_statement_ja: 類白血病反応は、白血病以外の原因による50,000/µLを超える持続的な好中球性白血球増多であり、診断は慢性骨髄性白血病と慢性好中球性白血病の除外と、重症感染症、中毒、悪性腫瘍、重篤な出血、急性溶血などの基礎原因の検出から進める。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2567
    source: Sakka V, Tsiodras S, Giamarellos-Bourboulis EJ, Giamarellou H. An update on the etiology and diagnostic evaluation of a leukemoid reaction. Eur J Intern Med. 2006;17(6):394-398.
    doi: 10.1016/j.ejim.2006.04.004
    pmid: '16962944'
    pmcid: null
    url: https://doi.org/10.1016/j.ejim.2006.04.004
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 総説の抄録で確認した範囲であり、定義の閾値も同総説に基づく。この項目にはガイドライン級の一次資料は見当たらなかった。別表1には本項目に対応する行がないため付けていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-2-C（類白血病反応、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-01 (id: JkxnuPM)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-007 (id: JlAKpV4)；TBL-02-01-016 (id: JlAKpWg)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-001
  domain: LY
  subdomain: 急性リンパ性白血病
  assertion:
    plain_statement_ja: 成人の急性リンパ性白血病では、症例の75%がB細胞前駆細胞由来であり、残りはT細胞前駆細胞の腫瘍である。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2568
    source: 'Terwilliger T, Abdul-Hay M. Acute lymphoblastic leukemia: a comprehensive review and 2017 update. Blood Cancer J. 2017;7(6):e577.'
    doi: 10.1038/bcj.2017.53
    pmid: '28665419'
    pmcid: PMC5520400
    url: https://doi.org/10.1038/bcj.2017.53
    source_license: CC BY 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典は総説であり、米国の年間発症数（6,500例超）など地域で異なる疫学の数値は主張に入れていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-A（急性リンパ性白血病、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；TBL-01-00-621 (id: JlvnmaE)；TBL-02-01-021 (id: JlAKpW0)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-002
  domain: LY
  subdomain: 急性リンパ性白血病
  assertion:
    plain_statement_ja: 急性リンパ性白血病のリスク層別化は、年齢・白血球数・化学療法への反応などの臨床因子に加え、再発性の遺伝子異常の同定によって精緻化されている。
    condition:
      region: 国際
      対象: 急性リンパ性白血病患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2568
    source: 'Terwilliger T, Abdul-Hay M. Acute lymphoblastic leukemia: a comprehensive review and 2017 update. Blood Cancer J. 2017;7(6):e577.'
    doi: 10.1038/bcj.2017.53
    pmid: '28665419'
    pmcid: PMC5520400
    url: https://doi.org/10.1038/bcj.2017.53
    source_license: CC BY 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 個別の遺伝子異常ごとの予後の数値は抄録の範囲では確認していない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-A（急性リンパ性白血病、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-021 (id: JlAKpW0)；TBL-02-01-018 (id: JlAKpWo)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-003
  domain: LY
  subdomain: 急性リンパ性白血病
  assertion:
    plain_statement_ja: 日本血液学会『造血器腫瘍診療ガイドライン2023年版』では、急性リンパ性白血病／リンパ芽球性リンパ腫（ALL/LBL）が白血病の独立章として扱われ、国内の診療の枠組みとなっている。
    condition:
      region: 日本
      対象: 急性リンパ性白血病／リンパ芽球性リンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2569
    source: 'Hatta Y, Izutsu K, Onizuka M, et al. JSH practical guidelines for hematological malignancies, 2023: leukemia-3. Acute lymphoblastic leukemia/lymphoblastic lymphoma: ALL/LBL. Int J Hematol. 2024;120(4):394-413.'
    doi: 10.1007/s12185-024-03836-7
    pmid: '39242492'
    pmcid: null
    url: https://doi.org/10.1007/s12185-024-03836-7
    source_license: Crossref の登録は Springer の TDM のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本章は抄録が収録されておらず、個別の推奨文は本文の照合が前提である。分類の現行版はWHO第5版（HAEM5、2022）であり、ガイドラインとの版のずれに注意すること。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-A（急性リンパ性白血病、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-04 (id: JkxnuPY)；TBL-01-00-621 (id: JlvnmaE)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-004
  domain: LY
  subdomain: Hodgkinリンパ腫
  assertion:
    plain_statement_ja: Hodgkinリンパ腫は欧米では全悪性リンパ腫の約10〜30%を占めるが、日本では約3〜6%にとどまる。
    condition:
      region: 日本
      対象: 悪性リンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2570
    source: 'Kusumoto S, Tomita A, et al. JSH practical guidelines for hematological malignancies, 2023: II. Lymphoma 10. Hodgkin lymphoma (HL). Int J Hematol. 2025;122(6):781-802.'
    doi: 10.1007/s12185-025-04079-w
    pmid: '41123791'
    pmcid: null
    url: https://doi.org/10.1007/s12185-025-04079-w
    source_license: Crossref の登録は Springer の TDM のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドライン英語版章の掲載誌ページで確認した（出典リサーチメモによる）。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-B（Hodgkinリンパ腫、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-005
  domain: LY
  subdomain: Hodgkinリンパ腫
  assertion:
    plain_statement_ja: 未治療のIII期・IV期古典的Hodgkinリンパ腫では、ブレンツキシマブ ベドチンとAVDの併用（A+AVD）はABVDに比べ、6年全生存割合が高かった（93.9%対89.4%、死亡のハザード比0.59）。
    condition:
      region: 国際
      対象: 未治療のIII期またはIV期古典的Hodgkinリンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2571
    source: Ansell SM, Radford J, Connors JM, et al. Overall Survival with Brentuximab Vedotin in Stage III or IV Hodgkin's Lymphoma. N Engl J Med. 2022;387(4):310-320.
    doi: 10.1056/NEJMoa2206125
    pmid: '35830649'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2206125
    source_license: NEJM の利用条件のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ブレンツキシマブ ベドチンは国内で2014年1月に再発・難治性のCD30陽性Hodgkinリンパ腫等で承認され、2018年9月に未治療のCD30陽性Hodgkinリンパ腫へのAVD併用の適応追加があった（製薬企業のプレスリリースで確認、出典リサーチメモによる）。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-B（Hodgkinリンパ腫、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-006
  domain: LY
  subdomain: Hodgkinリンパ腫
  assertion:
    plain_statement_ja: 12歳以上の未治療III期・IV期古典的Hodgkinリンパ腫では、ニボルマブとAVDの併用はブレンツキシマブ ベドチンとAVDの併用に比べ、2年無増悪生存割合が高かった（92%対83%、ハザード比0.45）。
    condition:
      region: 国際
      対象: 12歳以上の未治療III期またはIV期古典的Hodgkinリンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2572
    source: Herrera AF, LeBlanc M, Castellino SM, et al. Nivolumab+AVD in Advanced-Stage Classic Hodgkin's Lymphoma. N Engl J Med. 2024;391(15):1379-1389.
    doi: 10.1056/NEJMoa2405888
    pmid: '39413375'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2405888
    source_license: NEJM の利用条件のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ニボルマブは国内で2016年12月に再発・難治性の古典的Hodgkinリンパ腫で承認された（製薬企業のプレスリリースで確認、出典リサーチメモによる）。未治療の一次治療としてのニボルマブ併用（N+AVD）の国内承認は未確認である。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-B（Hodgkinリンパ腫、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-007
  domain: LY
  subdomain: 慢性リンパ性白血病
  assertion:
    plain_statement_ja: 慢性リンパ性白血病のiwCLLガイドラインは2018年に改訂され、効果判定基準の改訂、測定可能残存病変（MRD）評価の位置づけ、治療中のウイルス性疾患の評価・予防が盛り込まれた。
    condition:
      region: 国際
      対象: 慢性リンパ性白血病患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2573
    source: Hallek M, Cheson BD, Catovsky D, et al. iwCLL guidelines for diagnosis, indications for treatment, response assessment, and supportive management of CLL. Blood. 2018;131(25):2745-2760.
    doi: 10.1182/blood-2017-09-806398
    pmid: '29540348'
    pmcid: null
    url: https://doi.org/10.1182/blood-2017-09-806398
    source_license: Crossref にライセンス登録なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 診断基準の数値（単クローン性Bリンパ球数など）は抄録の範囲では確認しておらず、本文照合が前提である。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-①（慢性リンパ性白血病、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-021 (id: JlAKpW0)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-008
  domain: LY
  subdomain: 慢性リンパ性白血病
  assertion:
    plain_statement_ja: 慢性リンパ性白血病と小リンパ球性リンパ腫は、同一の疾患単位として扱われる。
    condition:
      region: 国際
      対象: 慢性リンパ性白血病／小リンパ球性リンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2574
    source: 'Eichhorst B, Robak T, Montserrat E, et al. Chronic lymphocytic leukaemia: ESMO Clinical Practice Guidelines for diagnosis, treatment and follow-up. Ann Oncol. 2021;32(1):23-33.'
    doi: 10.1016/j.annonc.2020.09.019
    pmid: '33091559'
    pmcid: null
    url: https://doi.org/10.1016/j.annonc.2020.09.019
    source_license: Elsevier の利用ライセンスのみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 診断基準の数値は出典の本文照合が前提であり、主張には入れていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-①（慢性リンパ性白血病、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-009
  domain: LY
  subdomain: 濾胞性リンパ腫
  assertion:
    plain_statement_ja: 未治療の進行期濾胞性リンパ腫では、オビヌツズマブ併用化学療法はリツキシマブ併用化学療法に比べ、3年無増悪生存割合の推定が高かった（80.0%対73.3%、ハザード比0.66）。
    condition:
      region: 国際
      対象: 未治療の進行期濾胞性リンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2575
    source: Marcus R, Davies A, Ando K, et al. Obinutuzumab for the First-Line Treatment of Follicular Lymphoma. N Engl J Med. 2017;377(14):1331-1344.
    doi: 10.1056/NEJMoa1614598
    pmid: '28976863'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1614598
    source_license: NEJM の利用条件のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: オビヌツズマブはCD20陽性濾胞性リンパ腫で国内承認があるが、承認年は出典リサーチで一次資料を未照合である。Grade 3〜5の有害事象はオビヌツズマブ群で多かった（74.6%対67.8%）。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-②（濾胞性リンパ腫、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-010
  domain: LY
  subdomain: 濾胞性リンパ腫
  assertion:
    plain_statement_ja: 日本血液学会『造血器腫瘍診療ガイドライン2023年版』では、濾胞性リンパ腫がリンパ腫の独立章として扱われ、国内の診療の枠組みとなっている。
    condition:
      region: 日本
      対象: 濾胞性リンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2576
    source: 'Izutsu K, Fukuhara N, et al. JSH practical guidelines for hematological malignancies, 2023: II. Lymphoma-1. Follicular lymphoma (FL). Int J Hematol. 2025;121(5):577-585.'
    doi: 10.1007/s12185-025-03922-4
    pmid: '39903435'
    pmcid: null
    url: https://doi.org/10.1007/s12185-025-03922-4
    source_license: Crossref の登録は Springer の TDM のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 分類の現行版はWHO第5版（HAEM5、2022）だが、本ガイドラインのリンパ腫章はWHO改訂第4版（2017）を基盤としており、版のずれがある。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-②（濾胞性リンパ腫、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-011
  domain: LY
  subdomain: びまん性大細胞型B細胞リンパ腫
  assertion:
    plain_statement_ja: 未治療の中・高リスクびまん性大細胞型B細胞リンパ腫では、ポラツズマブ ベドチン併用療法（pola-R-CHP）はR-CHOPに比べ2年無増悪生存割合が高かったが（76.7%対70.2%、ハザード比0.73）、2年全生存割合に有意差はなかった。
    condition:
      region: 国際
      対象: 未治療の中・高リスクびまん性大細胞型B細胞リンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2577
    source: Tilly H, Morschhauser F, Sehn LH, et al. Polatuzumab Vedotin in Previously Untreated Diffuse Large B-Cell Lymphoma. N Engl J Med. 2022;386(4):351-363.
    doi: 10.1056/NEJMoa2115304
    pmid: '34904799'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2115304
    source_license: NEJM の利用条件のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ポラツズマブ ベドチンは国内で再発・難治性のDLBCLに2021年に承認され、2022年8月24日に未治療DLBCLへの適応追加が承認された（製薬企業のプレスリリースで確認、出典リサーチメモによる）。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-③（びまん性大細胞型B細胞リンパ腫、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-009 (id: JlAKpWA)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-012
  domain: LY
  subdomain: びまん性大細胞型B細胞リンパ腫
  assertion:
    plain_statement_ja: びまん性大細胞型B細胞リンパ腫では、R-CHOP療法で治癒するのは患者の約60%にとどまる。
    condition:
      region: 国際
      対象: びまん性大細胞型B細胞リンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2577
    source: Tilly H, Morschhauser F, Sehn LH, et al. Polatuzumab Vedotin in Previously Untreated Diffuse Large B-Cell Lymphoma. N Engl J Med. 2022;386(4):351-363.
    doi: 10.1056/NEJMoa2115304
    pmid: '34904799'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2115304
    source_license: NEJM の利用条件のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 約60%という数値はPOLARIX試験論文の抄録の背景記述で確認した。リツキシマブの国内承認・保険適用の個別照合は本パートでは行っていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-③（びまん性大細胞型B細胞リンパ腫、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-013
  domain: LY
  subdomain: びまん性大細胞型B細胞リンパ腫
  assertion:
    plain_statement_ja: 日本血液学会『造血器腫瘍診療ガイドライン2023年版』では、びまん性大細胞型B細胞リンパ腫（DLBCL, NOS）がリンパ腫の独立章として扱われ、国内の診療の枠組みとなっている。
    condition:
      region: 日本
      対象: びまん性大細胞型B細胞リンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2578
    source: 'Ohmachi K, et al. JSH practical guidelines for hematological malignancies, 2023: II. Lymphoma 5. Diffuse large B-cell lymphoma, not otherwise specified (DLBCL, NOS). Int J Hematol. 2025;122(1):3-16.'
    doi: 10.1007/s12185-025-03997-z
    pmid: '40434571'
    pmcid: PMC12202654
    url: https://doi.org/10.1007/s12185-025-03997-z
    source_license: CC BY 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 分類の現行版はWHO第5版（HAEM5、2022）だが、本ガイドラインのリンパ腫章はWHO改訂第4版（2017）を基盤としており、版のずれがある。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-③（びまん性大細胞型B細胞リンパ腫、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-014
  domain: LY
  subdomain: 粘膜関連リンパ組織<MALT>リンパ腫
  assertion:
    plain_statement_ja: 粘膜関連リンパ組織<MALT>リンパ腫は節外性辺縁帯リンパ腫の一病型であり、日本血液学会のガイドラインでは辺縁帯リンパ腫の章で一括して扱われる。
    condition:
      region: 日本
      対象: 粘膜関連リンパ組織リンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2579
    source: 'Yoshida I, et al. JSH Practical Guidelines for Hematological Malignancies, 2023: II. Lymphoma-2. Marginal zone lymphoma. Int J Hematol. 2025;121(6):725-739.'
    doi: 10.1007/s12185-025-03947-9
    pmid: '40091100'
    pmcid: null
    url: https://doi.org/10.1007/s12185-025-03947-9
    source_license: Crossref の登録は Springer の TDM のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 消化管原発病変の局所の詳細（内視鏡所見・消化管限局例の治療）は境界により作っていない。除菌療法の効果などの数値は本文照合が前提で、主張には入れていない。分類はWHO第5版（HAEM5）とガイドライン（WHO改訂第4版基盤）で版のずれがある。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-⑤（粘膜関連リンパ組織<MALT>リンパ腫、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-015
  domain: LY
  subdomain: 粘膜関連リンパ組織<MALT>リンパ腫
  assertion:
    plain_statement_ja: 原発性肺MALTリンパ腫は、肺に原発する節外性辺縁帯リンパ腫（MALTリンパ腫）の一病型である。
    condition:
      region: 国際
      対象: 原発性肺粘膜関連リンパ組織リンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-547
    source: Sapuppo G, Frazzetto S, Pirosa MC, Zucca E. Epidemiology, diagnosis, and treatment of primary pulmonary mucosa-associated lymphoid tissue lymphoma. Chin Clin Oncol. 2026;15(3):46.
    doi: 10.21037/cco-2025-1-134
    pmid: null
    pmcid: null
    url: https://doi.org/10.21037/cco-2025-1-134
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本出典は原発性肺MALTリンパ腫に限る総説であり、肺病変の側面に限る補助出典として使う。消化管原発病変の局所の詳細は境界により作っていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-⑤（粘膜関連リンパ組織<MALT>リンパ腫、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-016
  domain: LY
  subdomain: マクログロブリン血症
  assertion:
    plain_statement_ja: 治療歴のある症候性マクログロブリン血症では、イブルチニブ投与により全奏効率90.5%・主要奏効率（major response）73.0%が得られ、血清IgMの低下とヘモグロビンの上昇を伴った。
    condition:
      region: 国際
      対象: 治療歴のある症候性マクログロブリン血症患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2580
    source: Treon SP, Tripsas CK, Meid K, et al. Ibrutinib in previously treated Waldenström's macroglobulinemia. N Engl J Med. 2015;372(15):1430-1440.
    doi: 10.1056/NEJMoa1501548
    pmid: '25853747'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1501548
    source_license: NEJM の利用条件のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: イブルチニブは国内で原発性マクログロブリン血症及びリンパ形質細胞リンパ腫の適応で承認されていることをPMDA資料で確認した（国内発売は2016年5月）。本試験は単群の前向き研究であり、対象は治療歴のある患者である。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-⑥（マクログロブリン血症、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-020 (id: JlAKpWw)；TBL-02-01-005 (id: JlAKpVw)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-017
  domain: LY
  subdomain: Burkittリンパ腫
  assertion:
    plain_statement_ja: 成人Burkittリンパ腫では、低強度DA-EPOCH-R療法を受けたHIV陰性例で、追跡期間中央値86か月時点の無増悪割合95%・全生存割合100%であった。
    condition:
      region: 米国
      対象: 成人Burkittリンパ腫患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2581
    source: Dunleavy K, Pittaluga S, Shovlin M, et al. Low-Intensity Therapy in Adults with Burkitt's Lymphoma. N Engl J Med. 2013;369(20):1915-1925.
    doi: 10.1056/NEJMoa1308392
    pmid: '24224624'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1308392
    source_license: NEJM の利用条件のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: DA-EPOCH-Rは米国の研究のレジメンであり、構成薬の国内承認・保険適用の個別照合は本パートでは行っていない。Burkittリンパ腫に専用の国際ガイドラインは確認できなかった。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-⑧（Burkittリンパ腫、c）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-021 (id: JlAKpW0)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-018
  domain: LY
  subdomain: 多発性骨髄腫
  assertion:
    plain_statement_ja: 多発性骨髄腫の診断では、クローナルな骨髄形質細胞の存在に加え、臓器障害（CRAB）に相当する事象だけでなく、検証済みのバイオマーカー（骨髄クローナル形質細胞60%以上、血清遊離軽鎖比100以上、MRIで2カ所以上の巣状病変）を満たす場合も骨髄腫と診断する。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2582
    source: Rajkumar SV, Dimopoulos MA, Palumbo A, et al. International Myeloma Working Group updated criteria for the diagnosis of multiple myeloma. Lancet Oncol. 2014;15(12):e538-e548.
    doi: 10.1016/S1470-2045(14)70442-5
    pmid: '25439696'
    pmcid: null
    url: https://doi.org/10.1016/S1470-2045(14)70442-5
    source_license: CC 表示なし（Europe PMC で非OA を確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値の閾値は造血器腫瘍診療ガイドライン第3.1版第Ⅲ章の診断規準表から読み取り（IMWG 2014年改訂規準の転記）。Rajkumar 2014 の抄録ではバイオマーカー追加の根拠（CRAB 発症がほぼ必至）までを確認した。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-④（多発性骨髄腫、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-629 (id: Jlvnmaw)；TBL-02-01-020 (id: JlAKpWw)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-019
  domain: LY
  subdomain: 多発性骨髄腫
  assertion:
    plain_statement_ja: 日本における多発性骨髄腫の発症率は人口10万人あたり約5人で、年間の死亡者数は4,000人前後であり、全造血器腫瘍の約10%を占める。
    condition:
      region: 日本
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2583
    source: 日本血液学会 編. 造血器腫瘍診療ガイドライン 第3.1版（2024年版）第Ⅲ章 骨髄腫. 日本血液学会ウェブサイト.
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 学会の著作物（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は造血器腫瘍診療ガイドライン第3.1版第Ⅲ章の本文から読み取り。ガイドラインは Web 公開版であり、書籍版（2023年版、第3版）と版の対応は組み立て時に再確認する。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-④（多発性骨髄腫、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-629 (id: Jlvnmaw)；TBL-02-01-020 (id: JlAKpWw)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-020
  domain: LY
  subdomain: 多発性骨髄腫
  assertion:
    plain_statement_ja: 改訂国際病期分類（R-ISS）は、ISSに高リスク染色体異常（del(17p)、t(4;14)、t(14;16)）と血清LDHを組み合わせた病期分類で、R-ISS I・II・IIIの5年全生存率はそれぞれ82%・62%・40%である。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2584
    source: 'Palumbo A, Avet-Loiseau H, Oliva S, et al. Revised International Staging System for Multiple Myeloma: A Report From International Myeloma Working Group. J Clin Oncol. 2015;33(26):2863-2869.'
    doi: 10.1200/JCO.2015.61.2267
    pmid: '26240224'
    pmcid: null
    url: https://doi.org/10.1200/JCO.2015.61.2267
    source_license: Crossref のライセンス欄は空（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は Palumbo 2015 の抄録から読み取り（11試験・4,445例の統合解析、追跡中央値46カ月）。後継の R2-ISS（2022）が報告されているが、本カードは R-ISS の記載に限る。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-④（多発性骨髄腫、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-629 (id: Jlvnmaw)；TBL-02-01-020 (id: JlAKpWw)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-021
  domain: LY
  subdomain: 多発性骨髄腫
  assertion:
    plain_statement_ja: 症候性多発性骨髄腫に伴う急性腎障害の最多の機序は軽鎖円柱腎症であり、腎回復には補液と誘因の是正に加えて遊離軽鎖の産生を速やかに減らす治療が要り、新規診断例での標準はボルテゾミブと高用量デキサメタゾンの併用である。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-615
    source: Bridoux F, Leung N, Belmouaz M, Royal V, Ronco P, Nasr SH. Management of acute kidney injury in symptomatic multiple myeloma. Kidney Int. 2021;99(3):570-580.
    doi: 10.1016/j.kint.2020.11.010
    pmid: '33440212'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2020.11.010
    source_license: Elsevier の TDM 用ライセンスのみ（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本出典は腎障害の側面に限る補助候補であり、骨髄腫本体の出典にはしない（依頼文 §8）。ボルテゾミブは国内で多発性骨髄腫の適応で承認され保険適用があることは造血器腫瘍診療ガイドライン第3.1版に標準治療として記載されていることで確認したが、PMDA 添付文書での個別照合は未了。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-④（多発性骨髄腫、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-629 (id: Jlvnmaw)；TBL-02-01-020 (id: JlAKpWw)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-022
  domain: LY
  subdomain: 意義不明の単クローン性免疫グロブリン血症<MGUS>
  assertion:
    plain_statement_ja: MGUSは、血清M蛋白が3 g/dL未満で骨髄のクローナルな形質細胞が10%未満にとどまり、骨髄腫に伴う臓器障害（CRAB）を欠く前駆状態として定義される。
    condition:
      region: 日本
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2583
    source: 日本血液学会 編. 造血器腫瘍診療ガイドライン 第3.1版（2024年版）第Ⅲ章 骨髄腫. 日本血液学会ウェブサイト.
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 学会の著作物（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 定義の閾値は造血器腫瘍診療ガイドライン第3.1版第Ⅲ章の診断規準表から読み取り（IMWG 規準に基づく）。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-⑦（意義不明の単クローン性免疫グロブリン血症<MGUS>、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-020 (id: JlAKpWw)；TBL-02-01-005 (id: JlAKpVw)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-023
  domain: LY
  subdomain: 意義不明の単クローン性免疫グロブリン血症<MGUS>
  assertion:
    plain_statement_ja: MGUSが多発性骨髄腫などの形質細胞腫瘍へ進行するリスクは平均して年約1%で、累積進行割合は10年で12%、20年で25%、25年で30%である。
    condition:
      region: 米国
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2585
    source: Kyle RA, Therneau TM, Rajkumar SV, et al. A long-term study of prognosis in monoclonal gammopathy of undetermined significance. N Engl J Med. 2002;346(8):564-569.
    doi: 10.1056/NEJMoa01133202
    pmid: '11856795'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa01133202
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は Kyle 2002 の抄録から読み取り（米国ミネソタ州南東部の住民コホート1,384例、11,009人年の追跡）。日本人集団での進行率は本出典では確認していない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-⑦（意義不明の単クローン性免疫グロブリン血症<MGUS>、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-020 (id: JlAKpWw)；TBL-02-01-005 (id: JlAKpVw)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-024
  domain: LY
  subdomain: 原発性アミロイドーシス
  assertion:
    plain_statement_ja: 全身性アミロイドーシスのうち最も多いのはALアミロイドーシスで、単クローン性免疫グロブリン軽鎖由来のアミロイド線維が臓器に沈着して障害を起こし、治療方針の決定にはアミロイド線維の型判定が重要である。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-979
    source: Wechalekar AD, Gillmore JD, Hawkins PN. Systemic amyloidosis. Lancet. 2016;387:2641-2654.
    doi: 10.1016/S0140-6736(15)01274-X
    pmid: '26719234'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(15)01274-X
    source_license: ライセンス表示を確認できず（出典マスター登録どおり）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードは AL（原発性）の側面に限る。ATTR（タファミジスの対象、SRC-980）は病型が異なるため混同しない。出典マスターでは本出典の class は UNKNOWN で登録されている。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-⑨（原発性アミロイドーシス、c）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-01 (id: JkxnuPM)；TBL-02-01-020 (id: JlAKpWw)；TBL-02-01-005 (id: JlAKpVw)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-025
  domain: LY
  subdomain: 原発性アミロイドーシス
  assertion:
    plain_statement_ja: ALアミロイドーシスでは腎障害が約70%にみられ、蛋白尿5 g/日超とeGFR 50 mL/min未満の組合せが透析への進行の高リスクを示し、腎反応は蛋白尿の30%以上の減少（または0.5 g/日未満への低下）で判定される。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-599
    source: Palladini G, Hegenbart U, Milani P, et al. A staging system for renal outcome and early markers of renal response to chemotherapy in AL amyloidosis. Blood. 2014;124(15):2325-2332.
    doi: 10.1182/blood-2014-04-570010
    pmid: '25115890'
    pmcid: null
    url: https://doi.org/10.1182/blood-2014-04-570010
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は Palladini 2014 の抄録から読み取り（Pavia 461例と Heidelberg 271例での検証）。本出典は腎病期と腎反応の早期マーカーに関するもので、心病期の分類には用いていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-C-⑨（原発性アミロイドーシス、c）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-01 (id: JkxnuPM)；TBL-02-01-020 (id: JlAKpWw)；TBL-02-01-005 (id: JlAKpVw)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-026
  domain: LY
  subdomain: 成人T細胞白血病・リンパ腫
  assertion:
    plain_statement_ja: 成人T細胞白血病・リンパ腫（ATL）は、臨床像からくすぶり型・慢性型・リンパ腫型・急性型の4病型に分類され、病型ごとに末梢血の異常リンパ球の割合やLDH・補正カルシウム・臓器浸潤の有無による診断基準が定められている。
    condition:
      region: 日本
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2586
    source: Shimoyama M; Lymphoma Study Group. Diagnostic criteria and classification of clinical subtypes of adult T-cell leukaemia-lymphoma. Br J Haematol. 1991;79(3):428-437.
    doi: 10.1111/j.1365-2141.1991.tb08051.x
    pmid: '1751370'
    pmcid: null
    url: https://doi.org/10.1111/j.1365-2141.1991.tb08051.x
    source_license: Wiley の利用条件のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 病型分類と診断基準の枠組みは Shimoyama 1991 の抄録で確認。各病型の基準値の詳細は本文照合が前提であり、本カードには含めていない。HTLV-1 のウイルス学と母子感染予防は Ⅻ の範囲（SRC-2062・2063）であり、ここでは扱わない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-D-①（成人T細胞白血病・リンパ腫、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-624 (id: JlvnmaY)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-027
  domain: LY
  subdomain: 成人T細胞白血病・リンパ腫
  assertion:
    plain_statement_ja: 日本のATL患者1,594例の解析では、生存期間中央値は急性型8.3か月・リンパ腫型10.6か月・慢性型31.5か月・くすぶり型55.0か月と、病型によって予後が大きく異なる。
    condition:
      region: 日本
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2587
    source: Katsuya H, Ishitsuka K, Utsunomiya A, et al. Treatment and survival among 1594 patients with ATL. Blood. 2015;126(24):2570-2577.
    doi: 10.1182/blood-2015-03-632489
    pmid: '26361794'
    pmcid: null
    url: https://doi.org/10.1182/blood-2015-03-632489
    source_license: Crossref にライセンス登録なし（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は Katsuya 2015 の抄録から読み取り（2000〜2009年診断例）。ATL の生涯発症率（キャリアの何%が発症するか）は原推計の一次資料で未確認のため、本パートのカードには含めていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-D-①（成人T細胞白血病・リンパ腫、b）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-624 (id: JlvnmaY)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-028
  domain: LY
  subdomain: 末梢T細胞性リンパ腫
  assertion:
    plain_statement_ja: 未治療のCD30陽性末梢T細胞リンパ腫では、ブレンツキシマブ ベドチンと化学療法（A+CHP）の併用はCHOP療法に比べて無増悪生存期間を延長し、中央値は48.2か月対20.8か月（ハザード比0.71）であった。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2588
    source: 'Horwitz S, O’Connor OA, Pro B, et al. Brentuximab vedotin with chemotherapy for CD30-positive peripheral T-cell lymphoma (ECHELON-2): a global, double-blind, randomised, phase 3 trial. Lancet. 2019;393(10168):229-240.'
    doi: 10.1016/S0140-6736(18)32984-2
    pmid: '30522922'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(18)32984-2
    source_license: Crossref の登録は Elsevier の TDM のみ（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は Horwitz 2019（ECHELON-2、452例）の抄録から読み取り。ブレンツキシマブ ベドチンは国内で2019年12月に末梢性T細胞リンパ腫の適応を取得したとされるが、本リサーチでは二次資料経由の確認であり、組み立て時に PMDA・販売元の一次資料で再確認すること。皮膚原発の側面は SRC-1122（皮膚原発リンパ腫ガイドライン2020の概要）の範囲であり、本カードには含めていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-D-②（末梢T細胞性リンパ腫、c）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-029
  domain: LY
  subdomain: 血球貪食性リンパ組織球症<HLH>
  assertion:
    plain_statement_ja: HLHの診断はHLH-2004基準により、発熱、脾腫、2系統以上の血球減少、高トリグリセリド血症または低フィブリノゲン血症、血球貪食像、NK細胞活性の低下または欠如、高フェリチン血症、可溶性IL-2受容体高値の8項目のうち5項目以上を満たすこと（またはHLHに合致する分子診断）で行う。
    condition:
      region: 国際
      対象: 小児・成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2589
    source: 'Henter JI, Horne A, Aricó M, et al. HLH-2004: Diagnostic and therapeutic guidelines for hemophagocytic lymphohistiocytosis. Pediatr Blood Cancer. 2007;48(2):124-131.'
    doi: 10.1002/pbc.21039
    pmid: '16937360'
    pmcid: null
    url: https://doi.org/10.1002/pbc.21039
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 基準の項目構成は Henter 2007 の抄録で確認。各項目の数値の閾値は本文照合が前提であり、本カードには含めていない。本カードは病態と診断に絞り、膠原病に伴うマクロファージ活性化症候群（MAS）としての全身管理は Ⅺ の範囲として扱わない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-F-①（血球貪食性リンパ組織球症<HLH>、c）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-024 (id: Jlvnlbw)；TBL-02-01-009 (id: JlAKpWA)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-030
  domain: LY
  subdomain: 血球貪食性リンパ組織球症<HLH>
  assertion:
    plain_statement_ja: 成人の反応性血球貪食症候群の診断にはHScoreが用いられ、9つの変数から算出されるスコアが90以下では発症確率は1%未満、250以上では99%を超えるとされる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2590
    source: Fardet L, Galicier L, Lambotte O, et al. Development and validation of the HScore, a score for the diagnosis of reactive hemophagocytic syndrome. Arthritis Rheumatol. 2014;66(9):2613-2620.
    doi: 10.1002/art.38690
    pmid: '24782338'
    pmcid: null
    url: https://doi.org/10.1002/art.38690
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は Fardet 2014 の抄録から読み取り（312例の多施設後ろ向きコホートで開発・検証）。スコアの各変数の配点の詳細は本文照合が前提であり、本カードには含めていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-F-①（血球貪食性リンパ組織球症<HLH>、c）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-024 (id: Jlvnlbw)；TBL-02-01-009 (id: JlAKpWA)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-031
  domain: LY
  subdomain: 伝染性単核球症
  assertion:
    plain_statement_ja: 伝染性単核球症はEBウイルスの初感染によって起こり、末梢血のリンパ球増多、咽頭痛、リンパ節腫脹、倦怠感を特徴とし、症状は数週間続くことがある。
    condition:
      region: 国際
      対象: 青年
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2031
    source: Dunmire SK, Verghese PS, Balfour HH Jr. Primary Epstein-Barr virus infection. J Clin Virol. 2018;102:84-92.
    doi: 10.1016/j.jcv.2018.03.001
    pmid: '29525635'
    pmcid: null
    url: https://doi.org/10.1016/j.jcv.2018.03.001
    source_license: CC 表示なし（Crossref は TDM ライセンスのみ）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは血液・リンパ系の病像に絞ったもので、EBV感染症の総論は Ⅻ の範囲（VI-022・023）として作り直していない。異型リンパ球の割合など血液像の具体的な数値は、本出典と Luzuriaga 2010 のいずれでも抄録の範囲で確認できなかったため含めていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-G（伝染性単核球症、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-012 (id: JlAKpWM)；TBL-02-01-009 (id: JlAKpWA)；TBL-02-01-016 (id: JlAKpWg)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
- id: LY-032
  domain: LY
  subdomain: 伝染性単核球症
  assertion:
    plain_statement_ja: 伝染性単核球症の潜伏期は約6週間と長く、診断は異好性抗体検査とEBウイルス特異的抗体検査によって行われる。
    condition:
      region: 国際
      対象: 青年
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2031
    source: Dunmire SK, Verghese PS, Balfour HH Jr. Primary Epstein-Barr virus infection. J Clin Virol. 2018;102:84-92.
    doi: 10.1016/j.jcv.2018.03.001
    pmid: '29525635'
    pmcid: null
    url: https://doi.org/10.1016/j.jcv.2018.03.001
    source_license: CC 表示なし（Crossref は TDM ライセンスのみ）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 潜伏期と検査法は Dunmire 2018 の抄録で確認。脾破裂の頻度や運動制限の期間など合併症の数値は抄録の範囲で確認できなかったため含めていない。
  curriculum:
    kokushi: 医学各論 Ⅶ-3-G（伝染性単核球症、a）
    core_curriculum: 'PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-012 (id: JlAKpWM)；TBL-02-01-009 (id: JlAKpWA)；TBL-02-01-016 (id: JlAKpWg)'
  publication_info:
    created: '2026-10-31'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応の一覧

| カードID | 出題基準 | コアカリ |
|---|---|---|
| ML-001 | 医学各論 Ⅶ-2-A-①（薬剤性無顆粒球症、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-023 (id: Jlvnlbs)；TBL-02-01-007 (id: JlAKpV4) |
| ML-002 | 医学各論 Ⅶ-2-A-①（薬剤性無顆粒球症、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-023 (id: Jlvnlbs)；TBL-02-01-009 (id: JlAKpWA) |
| ML-003 | 医学各論 Ⅶ-2-B-①（急性骨髄性白血病、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；PS-02-02-04 (id: JkxnuPY)；TBL-01-00-621 (id: JlvnmaE)；TBL-02-01-021 (id: JlAKpW0)；TBL-02-01-018 (id: JlAKpWo) |
| ML-004 | 医学各論 Ⅶ-2-B-①（急性骨髄性白血病、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-04 (id: JkxnuPY)；TBL-01-00-621 (id: JlvnmaE) |
| ML-005 | 医学各論 Ⅶ-2-B-①（急性骨髄性白血病、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-04 (id: JkxnuPY)；TBL-01-00-621 (id: JlvnmaE)；TBL-02-01-021 (id: JlAKpW0) |
| ML-006 | 医学各論 Ⅶ-2-B-①（急性骨髄性白血病、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-04 (id: JkxnuPY)；TBL-01-00-621 (id: JlvnmaE) |
| ML-007 | 医学各論 Ⅶ-2-B-②（慢性骨髄性白血病、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-622 (id: JlvnmaM)；TBL-02-01-021 (id: JlAKpW0) |
| ML-008 | 医学各論 Ⅶ-2-B-②（慢性骨髄性白血病、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-622 (id: JlvnmaM)；TBL-02-01-018 (id: JlAKpWo) |
| ML-009 | 医学各論 Ⅶ-2-B-②（慢性骨髄性白血病、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-622 (id: JlvnmaM)；TBL-02-01-021 (id: JlAKpW0) |
| ML-010 | 医学各論 Ⅶ-2-B-③（原発性骨髄線維症、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-627 (id: Jlvnmao)；TBL-02-01-018 (id: JlAKpWo) |
| ML-011 | 医学各論 Ⅶ-2-B-③（原発性骨髄線維症、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-627 (id: Jlvnmao)；TBL-02-01-018 (id: JlAKpWo) |
| ML-012 | 医学各論 Ⅶ-2-B-④（本態性血小板血症、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-626 (id: Jlvnmak)；TBL-02-01-021 (id: JlAKpW0)；TBL-02-01-015 (id: JlAKpWY) |
| ML-013 | 医学各論 Ⅶ-2-B-④（本態性血小板血症、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-626 (id: Jlvnmak)；TBL-02-01-015 (id: JlAKpWY) |
| ML-014 | 医学各論 Ⅶ-2-B-⑤（真性赤血球増加症、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-625 (id: Jlvnmac)；TBL-02-01-021 (id: JlAKpW0) |
| ML-015 | 医学各論 Ⅶ-2-B-⑤（真性赤血球増加症、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-625 (id: Jlvnmac)；TBL-02-01-021 (id: JlAKpW0)；TBL-02-01-015 (id: JlAKpWY) |
| ML-016 | 医学各論 Ⅶ-2-B-⑥（慢性好酸球性白血病、c） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-007 (id: JlAKpV4)；TBL-02-01-021 (id: JlAKpW0) |
| ML-017 | 医学各論 Ⅶ-2-C（類白血病反応、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-01 (id: JkxnuPM)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-007 (id: JlAKpV4)；TBL-02-01-016 (id: JlAKpWg) |
| LY-001 | 医学各論 Ⅶ-3-A（急性リンパ性白血病、a） | PS-02-02-05 (id: JkxnuPc)；TBL-01-00-621 (id: JlvnmaE)；TBL-02-01-021 (id: JlAKpW0) |
| LY-002 | 医学各論 Ⅶ-3-A（急性リンパ性白血病、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-021 (id: JlAKpW0)；TBL-02-01-018 (id: JlAKpWo) |
| LY-003 | 医学各論 Ⅶ-3-A（急性リンパ性白血病、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-04 (id: JkxnuPY)；TBL-01-00-621 (id: JlvnmaE) |
| LY-004 | 医学各論 Ⅶ-3-B（Hodgkinリンパ腫、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas) |
| LY-005 | 医学各論 Ⅶ-3-B（Hodgkinリンパ腫、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM) |
| LY-006 | 医学各論 Ⅶ-3-B（Hodgkinリンパ腫、a） | PS-02-02-05 (id: JkxnuPc)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM) |
| LY-007 | 医学各論 Ⅶ-3-C-①（慢性リンパ性白血病、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-021 (id: JlAKpW0) |
| LY-008 | 医学各論 Ⅶ-3-C-①（慢性リンパ性白血病、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM) |
| LY-009 | 医学各論 Ⅶ-3-C-②（濾胞性リンパ腫、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM) |
| LY-010 | 医学各論 Ⅶ-3-C-②（濾胞性リンパ腫、b） | PS-02-02-05 (id: JkxnuPc)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM) |
| LY-011 | 医学各論 Ⅶ-3-C-③（びまん性大細胞型B細胞リンパ腫、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-009 (id: JlAKpWA) |
| LY-012 | 医学各論 Ⅶ-3-C-③（びまん性大細胞型B細胞リンパ腫、a） | PS-02-02-05 (id: JkxnuPc)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM) |
| LY-013 | 医学各論 Ⅶ-3-C-③（びまん性大細胞型B細胞リンパ腫、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas) |
| LY-014 | 医学各論 Ⅶ-3-C-⑤（粘膜関連リンパ組織<MALT>リンパ腫、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM) |
| LY-015 | 医学各論 Ⅶ-3-C-⑤（粘膜関連リンパ組織<MALT>リンパ腫、b） | PS-02-02-05 (id: JkxnuPc)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM) |
| LY-016 | 医学各論 Ⅶ-3-C-⑥（マクログロブリン血症、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-020 (id: JlAKpWw)；TBL-02-01-005 (id: JlAKpVw) |
| LY-017 | 医学各論 Ⅶ-3-C-⑧（Burkittリンパ腫、c） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-021 (id: JlAKpW0) |
| LY-018 | 医学各論 Ⅶ-3-C-④（多発性骨髄腫、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-629 (id: Jlvnmaw)；TBL-02-01-020 (id: JlAKpWw) |
| LY-019 | 医学各論 Ⅶ-3-C-④（多発性骨髄腫、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-629 (id: Jlvnmaw)；TBL-02-01-020 (id: JlAKpWw) |
| LY-020 | 医学各論 Ⅶ-3-C-④（多発性骨髄腫、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-629 (id: Jlvnmaw)；TBL-02-01-020 (id: JlAKpWw) |
| LY-021 | 医学各論 Ⅶ-3-C-④（多発性骨髄腫、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-01-00-629 (id: Jlvnmaw)；TBL-02-01-020 (id: JlAKpWw) |
| LY-022 | 医学各論 Ⅶ-3-C-⑦（意義不明の単クローン性免疫グロブリン血症<MGUS>、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-020 (id: JlAKpWw)；TBL-02-01-005 (id: JlAKpVw) |
| LY-023 | 医学各論 Ⅶ-3-C-⑦（意義不明の単クローン性免疫グロブリン血症<MGUS>、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-020 (id: JlAKpWw)；TBL-02-01-005 (id: JlAKpVw) |
| LY-024 | 医学各論 Ⅶ-3-C-⑨（原発性アミロイドーシス、c） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-01 (id: JkxnuPM)；TBL-02-01-020 (id: JlAKpWw)；TBL-02-01-005 (id: JlAKpVw) |
| LY-025 | 医学各論 Ⅶ-3-C-⑨（原発性アミロイドーシス、c） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-01 (id: JkxnuPM)；TBL-02-01-020 (id: JlAKpWw)；TBL-02-01-005 (id: JlAKpVw) |
| LY-026 | 医学各論 Ⅶ-3-D-①（成人T細胞白血病・リンパ腫、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-624 (id: JlvnmaY)；TBL-02-01-012 (id: JlAKpWM) |
| LY-027 | 医学各論 Ⅶ-3-D-①（成人T細胞白血病・リンパ腫、b） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-624 (id: JlvnmaY)；TBL-02-01-012 (id: JlAKpWM) |
| LY-028 | 医学各論 Ⅶ-3-D-②（末梢T細胞性リンパ腫、c） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-628 (id: Jlvnmas)；TBL-02-01-012 (id: JlAKpWM) |
| LY-029 | 医学各論 Ⅶ-3-F-①（血球貪食性リンパ組織球症<HLH>、c） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-024 (id: Jlvnlbw)；TBL-02-01-009 (id: JlAKpWA) |
| LY-030 | 医学各論 Ⅶ-3-F-①（血球貪食性リンパ組織球症<HLH>、c） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；TBL-01-00-024 (id: Jlvnlbw)；TBL-02-01-009 (id: JlAKpWA) |
| LY-031 | 医学各論 Ⅶ-3-G（伝染性単核球症、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-012 (id: JlAKpWM)；TBL-02-01-009 (id: JlAKpWA)；TBL-02-01-016 (id: JlAKpWg) |
| LY-032 | 医学各論 Ⅶ-3-G（伝染性単核球症、a） | PS-02-02-05 (id: JkxnuPc)；PS-02-02-02 (id: JkxnuPQ)；PS-02-02-03 (id: JkxnuPU)；TBL-02-01-012 (id: JlAKpWM)；TBL-02-01-009 (id: JlAKpWA)；TBL-02-01-016 (id: JlAKpWg) |

## 4. 未解決事項

### パートA（ML）からの申し送り
- **数値の確認範囲**：全カードの数値は出典リサーチ（39_research_1.md）で抄録により確認済みの範囲だけを主張に入れた。ELN 2022 の遺伝子リスク分類の個別遺伝子の一覧、DIPSS の各リスク群の生存期間は抄録の範囲外のため主張に含めていない。
- **JSH ガイドライン章はカード化していない**：日本血液学会『造血器腫瘍診療ガイドライン』2023年版の各論（AML章 Int J Hematol. 2024;119(4):347-373、APL章 2024;119(5):481-492、CML/MPN章 2025;121(1):5-38）は PubMed に抄録がなく、推奨文・数値を一次確認できないため本パートでは出典に使わなかった。組み立て時に誌面・学会サイトで照合できれば、日本（region: 日本）のカードの追加候補になる。WHO HAEM5（Leukemia. 2022;36(7):1703-1719、CC BY、OPEN）と ICC 2022（Blood. 2022;140(11):1200-1228）も分類の土台として申し送る（本パートでは個別カードの出典にはしていない）。
- **使わなかった候補**（他パート・組み立て時の追加候補）：MASCC スコア原著（J Clin Oncol. 2000;18(16):3038-3051）、日本臨床腫瘍学会 FN 診療ガイドライン改訂第2版（2017、第3版の刊行有無は未確認）、G-CSF 適正使用ガイドライン2022年版、ギルテリチニブ ADMIRAL 試験（N Engl J Med. 2019;381(18):1728-1740、国内承認は2018年）、アシミニブ ASCEMBL 試験（Blood. 2021;138(21):2031-2041、国内承認2022年・効能拡大2025年）、IRIS 長期追跡（N Engl J Med. 2017;376(10):917-927）、Klion の HES 総説（Blood. 2015;126(9):1069-1077）。
- **国内承認の未確認事項**：ミドスタウリン（ML-005）は国内承認を確認できなかった。三酸化二ヒ素製剤（ML-006）の国内適応範囲、FIP1L1::PDGFRA 陽性例に対するイマチニブの国内適応（ML-016）も未確認で、いずれも uncertainty に明記した。組み立て時に PMDA で確認すること。
- **IPSET-thrombosis 改訂版（ML-013）**：PubMed に抄録がなく、リスク群の再編の詳細は未確認のまま書誌的事実だけを主張にした。詳細を厚くする場合は PMC 全文（PMC4670947、CC BY）で照合すること。
- **地域分け**：IDSA の発熱性好中球減少症ガイドラインは米国、ELN 2025 と STIM は欧州として地域を付けた。日本の FN の定義との違いは ML-002 の uncertainty に明記した。
- **MDS との境界**：骨髄異形成症候群は第38回（RC）で作成済みであり、本パートでは作り直していない。AML への進展の側面は組み立て時に第38回の MDS カードとの相互参照で扱うこと。

### パートB（LY 前半）からの申し送り
- 急性リンパ性白血病（Ⅶ-3-A）とマクログロブリン血症（Ⅶ-3-C-⑥）には出典リサーチの専用パートがなかったため、組み立て時に一次資料を追加で照合した（Terwilliger & Abdul-Hay 2017、JSH ガイドライン ALL/LBL 章 2024、Treon ら 2015）。識別子は題名検索の結果をそのまま使わず、DOI をキーに PubMed で照合して確定した
- Hodgkinリンパ腫章（SRC-2573）の号は、出典リサーチメモでは 122(5) だったが Crossref では 122(6) のため、Crossref の値を採用した
- 日本血液学会ガイドライン2023年版の英語版章は、章ごとにライセンスが異なる（DLBCL 章は CC BY で OPEN、ALL・Hodgkin・濾胞性・辺縁帯の各章は TDM のみで RESTRICTED）
- 分類の現行版は WHO 第5版（HAEM5、2022）と ICC 2022 だが、JSH 2023 のリンパ腫章は WHO 改訂第4版（2017）基盤である。版のずれは該当カードの uncertainty に明記した。HAEM5 の総説（Alaggio ら 2022）自体は本パートでは出典に使っていないため、分類そのもののカードが要る場合は統合時に追加できる
- 主張に入れなかった未照合の数値：慢性リンパ性白血病の診断基準の閾値、MALTリンパ腫の除菌療法の効果（いずれも抄録の範囲では確認できず、本文照合が前提）
- 薬剤の国内承認で未確認・未照合の点：オビヌツズマブの承認年（一次資料未照合）、未治療一次治療としてのニボルマブ併用（N+AVD）の国内承認（未確認）、DA-EPOCH-R の構成薬の個別照合（未実施）、リツキシマブの個別照合（未実施）。いずれも該当カードの uncertainty に明記した
- 使わなかった候補：ESMO の辺縁帯リンパ腫ガイドライン（Zucca ら 2020）、ESMO の Hodgkin・DLBCL・濾胞性ガイドライン、ICC 2022 分類。統合時に不足があれば追加できる
- 欠番はない。担当8項目すべてにカードがあり、レベル a の3項目（Ⅶ-3-A・Ⅶ-3-B・Ⅶ-3-C-③）は各3件ある

### パートC（LY 後半）からの申し送り


## 5. 次回への引き継ぎ

- 第39回の未使用 SRC：SRC-2591〜2640（次回へは繰り越さない）
- 対象23項目（ML 8・LY 15）をすべてカバーした。レベル a の8項目（ML：Ⅶ-2-A-①・2-B-①・2-B-②、LY：Ⅶ-3-A・3-B・3-C-③・3-C-④・3-G）には各2件以上のカードがある
- 境界の扱い：MALT リンパ腫は全身疾患としての位置づけに絞り、消化管原発病変の局所の詳細は作っていない（補完の回で Ⅵ の候補）。HLH は病態と診断に絞り、治療と MAS の全身管理は作っていない（Ⅺ の範囲）。伝染性単核球症は血液・リンパ系の病像に絞り、EBV 感染症の総論は作り直していない。ATL の生涯発症率は一次資料で未確認のため主張に入れていない
- 第40回（HS）への申し送り：赤血球破砕症候群（第38回 RC）では TMA の詳細を作っていないため、TTP・HUS の本体は HS で作ること
