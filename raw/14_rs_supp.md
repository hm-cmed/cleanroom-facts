# 第14回 呼吸器の補完（採用版）

- 作成：Claude Code（2026-10-28）。第14回の試行（`docs/tasks/round14_RS_supp.md` を2つの作り手に依頼）の評価（`reports/trial_eval_14_result.md`）にもとづき、**成果物A（28件）を全件採用し、成果物B から A と重ならない 13件を加えた**。
- 成果物B のカードは ID と SRC 番号を振り直した（下の対応表）。主張文・数値は変更していない。変更は各カードの history に記録した。
- 成果物B の SRC-538・540（新しい番号では SRC-561・563）は、Crossref の license 欄（CC BY 4.0）にもとづき source_class を UNKNOWN から OPEN にした。
- SRC-570 は第14回の範囲（530〜569）の外だが、振り直しで不足したため使った。

## 1. 出典マスター

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 備考 |
|---|---|---|---|---|---|---|---|
| SRC-530 | Johnson RJ, Jong EC, Dunning SB, Carberry WL, Minshew BH. Paragonimiasis: diagnosis and the use of praziquantel in treatment. Rev Infect Dis. 1985;7(2):200-206 | 10.1093/clinids/7.2.200 | 4001715 | ライセンス表示を確認できず（レコードに license 欄なし） | UNKNOWN | 抄録ページで症例数・用量・転帰と PMID・DOI を確認し、書誌と DOI を Crossref レコードでも確認 | 成果物A |
| SRC-531 | Šafránek J. Descending necrotizing mediastinitis – a surgical view. Rozhledy v chirurgii. 2024;103(12):502-504 | 10.48095/ccrvch2024502 | 40221899 | ライセンス表示を確認できず（レコードに license 欄なし） | UNKNOWN | 抄録ページで PMID を確認し、抄録本文・書誌・DOI を Crossref レコードで確認 | 成果物A |
| SRC-532 | Gulilat D, Genetu A, Kejela S, Kassa S, Bekele A, Tizazu A. Nonmalignant tracheal stenosis: presentation, management and outcome in limited resources setting. J Cardiothorac Surg. 2024;19(1):21 | 10.1186/s13019-024-02480-w | 38263174 | CC BY 4.0（誌面の Open Access 表示と Crossref の license 欄の両方で確認） | OPEN | 全文ページで PMID・PMCID・CC BY 4.0 表示と数値を確認し、Crossref レコードでも DOI とライセンスを確認 | 成果物A |
| SRC-533 | Ren S, Yang L, Xiao Y, Tong Z, Wang L, Hu Y. Pulmonary sequestration in adult patients: a single-center retrospective study. Respir Res. 2023;24(1):13 | 10.1186/s12931-023-02320-w | 36635696 | CC BY 4.0（誌面の Open Access 表示と Crossref の license 欄の両方で確認） | OPEN | 全文ページで PMID・PMCID・CC BY 4.0 表示と数値を確認し、Crossref レコードでも DOI とライセンスを確認 | 成果物A |
| SRC-534 | Ganie FA, Lone H, Lone GN, et al. Lung Contusion: A Clinico-Pathological Entity with Unpredictable Clinical Course. Bull Emerg Trauma. 2013;1(1):7-16 | 確認できず（null） | 27162815 | ライセンス表示を確認できず（CC の表示なし） | UNKNOWN | 全文ページで PMID・PMCID と抄録の数値を確認。DOI は表示で確認できなかった | 成果物A |
| SRC-538 | Cherian SV, Tang VK, Vijhani P, Ambelil M, Estrada-Y-Martin RM. Primary pulmonary lymphoproliferative neoplasms. Lung India 2018;35:220 | 10.4103/lungindia.lungindia_381_17 | 29697079 | CC BY-NC-SA 4.0（PMC ページの表示） | RESTRICTED | PMC ページ（抄録・本文・PMCID: PMC5946555）、Crossref（書誌・DOI） | 成果物A |
| SRC-539 | Abbott GF, Rosado-de-Christenson ML, Franks TJ, Frazier AA, Galvin JR. From the archives of the AFIP: Pulmonary Langerhans cell histiocytosis. RadioGraphics 2004;24:821-841 | 10.1148/rg.243045005 | 15143231 | Crossref の license 欄に記載なし（未確認） | UNKNOWN | PubMed 抄録、Crossref（書誌・DOI・ページ） | 成果物A |
| SRC-540 | Lu X, He B, Wang G, He B, Wang L, Chen Q. Bronchoscopic Diagnosis and Treatment of Primary Tracheobronchial Amyloidosis: A Retrospective Analysis from China. BioMed Res Int 2017;2017:3425812 | 10.1155/2017/3425812 | 28197412 | CC BY 4.0（Crossref の license 欄・PMC ページの表示） | OPEN | PMC ページ（抄録・本文・PMCID: PMC5288517）、Crossref（license 欄） | 成果物A |
| SRC-541 | Cordier JF. Cryptogenic organizing pneumonia. Clin Chest Med 2004;25:727-738 | 10.1016/j.ccm.2004.06.003 | 15564018 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | PMC ページ（抄録・本文・PMCID: PMC7119066）、Crossref（書誌・license 欄） | 成果物A |
| SRC-542 | Auchincloss JH, Abraham JL, Gilbert R, Lax M, Henneberger PK, Heitzman ER, Peppi DJ. Health hazard of poorly regulated exposure during manufacture of cemented tungsten carbides and cobalt. Br J Ind Med 1992;49:832-836 | 10.1136/oem.49.12.832 | 1472440 | Crossref の license 欄に記載なし（未確認） | UNKNOWN | PMC ページ（抄録・PMCID: PMC1061212）、Crossref（書誌・DOI・ページ） | 成果物A |
| SRC-543 | Lius EE, Syafaah I. Hyperoxia in the management of respiratory failure: A literature review. Ann Med Surg 2022;81:104393 | 10.1016/j.amsu.2022.104393 | 36147110 | CC BY-NC-ND 4.0（PMC ページ・Crossref の license 欄） | RESTRICTED | PMC ページ（本文・PMCID: PMC9486660）、Crossref（書誌・license 欄） | 成果物A |
| SRC-544 | Yoon SC. Clinical Outcome of Paraquat Poisoning. Korean J Intern Med 2009;24:93-94 | 10.3904/kjim.2009.24.2.93 | 19543485 | CC BY-NC 4.0（PMC ページの表示） | RESTRICTED | PMC ページ（本文・PMCID: PMC2698628）、Crossref（書誌・DOI） | 成果物A |
| SRC-545 | Enemark A, Jönsson ÅLM, Kronborg-White S, Bendstrup E. Pulmonary Alveolar Microlithiasis – A Review. Yale J Biol Med 2021;94 | なし（未確認のため null） | 34970102 | CC BY-NC（PMC ページの表示） | RESTRICTED | PMC ページ（抄録・本文・PMCID: PMC8686773）、Crossref と ID 変換で DOI を確認できず | 成果物A |
| SRC-548 | Shu C, et al. Diagnosis and Treatment of Primary Tracheobronchial Tumors. Cancer Med 2025;14:e70893 | 10.1002/cam4.70893 | 40289301 | CC BY 4.0（Crossref の license 欄） | OPEN | PubMed収載の抄録・PMC掲載本文・Crossrefレコード | 成果物A |
| SRC-549 | Reck M, et al. Pembrolizumab versus Chemotherapy for PD-L1-Positive Non-Small-Cell Lung Cancer. N Engl J Med 2016;375:1823-1833 | 10.1056/NEJMoa1606774 | 27718847 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | PubMed収載の抄録・Crossrefレコード | 成果物A |
| SRC-550 | Reck M, et al. Five-Year Outcomes With Pembrolizumab Versus Chemotherapy for Metastatic NSCLC With PD-L1 TPS ≥ 50%. J Clin Oncol 2021;39:2339-2349 | 10.1200/JCO.21.00174 | 33872070 | CC BY-NC-ND 4.0（PMC 掲載ページの表示） | RESTRICTED | PubMed収載の抄録・PMC掲載本文 | 成果物A |
| SRC-551 | Antonia SJ, et al. Durvalumab after Chemoradiotherapy in Stage III NSCLC. N Engl J Med 2017;377:1919-1929 | 10.1056/NEJMoa1709937 | 28885881 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | PubMed収載の抄録・Crossrefレコード | 成果物A |
| SRC-552 | Spigel DR, et al. Five-Year Survival Outcomes From the PACIFIC Trial. J Clin Oncol 2022;40:1301-1311 | 10.1200/JCO.21.01308 | 35108059 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | PubMed収載の抄録・Crossrefレコード（抄録含む） | 成果物A |
| SRC-553 | Saji H, et al. Segmentectomy versus lobectomy in small-sized peripheral NSCLC (JCOG0802/WJOG4607L). Lancet 2022;399:1607-1617 | 10.1016/S0140-6736(21)02333-3 | 35461558 | Elsevier の利用条件（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed収載の抄録・Crossrefレコード | 成果物A |
| SRC-554 | Altorki N, et al. Lobar or Sublobar Resection for Peripheral Stage IA NSCLC. N Engl J Med 2023;388:489-498 | 10.1056/NEJMoa2212083 | 36780674 | 出版社の著作物（CC の表示なし） | RESTRICTED | PubMed収載の抄録 | 成果物A |
| SRC-555 | Peters S, et al. Alectinib versus Crizotinib in Untreated ALK-Positive NSCLC. N Engl J Med 2017;377:829-838 | 10.1056/NEJMoa1704795 | 28586279 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | PubMed収載の抄録・Crossrefレコード | 成果物A |
| SRC-556 | Shaw AT, et al. First-Line Lorlatinib or Crizotinib in Advanced ALK-Positive Lung Cancer. N Engl J Med 2020;383:2018-2029 | 10.1056/NEJMoa2027187 | 33207094 | NEJM の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed収載の抄録・Crossrefレコード | 成果物A |
| SRC-557 | Nicholson AG, et al. IASLC Staging Project: Proposals for the Revision of the Clinical and Pathologic Staging of SCLC in the Forthcoming Eighth Edition of the TNM Classification. J Thorac Oncol 2016;11:300-311 | 10.1016/j.jtho.2015.10.008 | 26723244 | Elsevier の利用条件（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed収載の抄録・Crossrefレコード | 成果物A |
| SRC-558 | Horn L, et al. First-Line Atezolizumab plus Chemotherapy in Extensive-Stage SCLC. N Engl J Med 2018;379:2220-2229 | 10.1056/NEJMoa1809064 | 30280641 | 出版社の著作物（CC の表示なし） | RESTRICTED | PubMed収載の抄録 | 成果物A |
| SRC-559 | Baas P, et al. First-line nivolumab plus ipilimumab in unresectable malignant pleural mesothelioma (CheckMate 743). Lancet 2021;397:375-386 | 10.1016/S0140-6736(20)32714-8 | 33485464 | Elsevier の利用条件（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed収載の抄録・Crossrefレコード | 成果物A |
| SRC-560 | Peters S, et al. First-line nivolumab plus ipilimumab versus chemotherapy in unresectable MPM: 3-year outcomes from CheckMate 743. Ann Oncol 2022;33:488-499 | 10.1016/j.annonc.2022.01.074 | 35124183 | CC BY-NC-ND 4.0（Crossref の license 欄） | RESTRICTED | 抄録・Crossrefレコード | 成果物A |
| SRC-566 | Caleffi-Pereira M, et al. Unilateral diaphragm paralysis: a dysfunction restricted not just to one hemidiaphragm. BMC Pulm Med 2018;18:126 | 10.1186/s12890-018-0698-1 | 30068327 | CC BY 4.0 | OPEN | PMC の論文ページで抄録・PMID・PMCID・ライセンス表示を確認。Crossref で書誌と license（CC BY 4.0）を確認 | 成果物A |
| SRC-567 | Evman S, et al. Comparison of Mid-Term Clinical Outcomes of Different Surgical Approaches in Symptomatic Diaphragmatic Eventration. Ann Thorac Cardiovasc Surg 2016;22:224-229 | 10.5761/atcs.oa.16-00018 | 27076066 | 表示なし（未確認。©2016 Annals of Thoracic and Cardiovascular Surgery） | UNKNOWN | PMC の論文ページで抄録・本文・PMID・PMCID を確認。NCBI の ID 変換で DOI を確認。Crossref で書誌を確認（license の記載なし）。J-STAGE の論文ページにもライセンス表示なし | 成果物A |
| SRC-535 | Centers for Disease Control and Prevention. DPDx: Paragonimiasis（最終更新 2024-06-06） | — | — | 米国連邦政府の著作物（CDC） | GOV_US | CDC のページを直接取得 | 成果物B の SRC-530 |
| SRC-536 | Centers for Disease Control and Prevention. Clinical Overview of Strongyloides（最終更新 2026-02-11） | — | — | 米国連邦政府の著作物（CDC） | GOV_US | CDC のページを直接取得 | 成果物B の SRC-532 |
| SRC-537 | Guedes F, Branquinho MV, Sousa AC, et al. Central airway obstruction: is it time to move forward? BMC Pulm Med 2022;22:68 | 10.1186/s12890-022-01862-x | — | CC BY 4.0 | OPEN | 出版社 PDF（本文）でライセンス表示を確認 | 成果物B の SRC-534 |
| SRC-546 | Chau HS, Gutkin PM, Knight AW, Forrester JD. Contemporary management of pulmonary contusions: a narrative review. Curr Chall Thorac Surg 2025;7:26 | 10.21037/ccts-25-18 | — | CC BY-NC-ND 4.0 | RESTRICTED | 出版社ページ（本文）でライセンス表示を確認 | 成果物B の SRC-536 |
| SRC-547 | Sapuppo G, Frazzetto S, Pirosa MC, Zucca E. Epidemiology, diagnosis, and treatment of primary pulmonary mucosa-associated lymphoid tissue lymphoma. Chin Clin Oncol 2026;15(3):46 | 10.21037/cco-2025-1-134 | — | CC BY-NC-ND 4.0 | RESTRICTED | 出版社ページ（本文）でライセンス表示を確認 | 成果物B の SRC-537 |
| SRC-561 | Radzikowska E. Update on Pulmonary Langerhans Cell Histiocytosis. Front Med 2020;7:582581 | 10.3389/fmed.2020.582581 | — | Crossref の license 欄 CC BY 4.0（2026-10-28 の照合） | OPEN | 出版社ページ（本文）。PMCID は検索結果の題名で確認 | 成果物B の SRC-538（source_class を Crossref で UNKNOWN→OPEN） |
| SRC-562 | Milani P, Basset M, Russo F, et al. The lung in amyloidosis. Eur Respir Rev 2017;26:170046 | 10.1183/16000617.0046-2017 | — | CC BY-NC 4.0（© ERS 2017） | RESTRICTED | リポジトリ掲載の刊行版 PDF でライセンス表示を確認 | 成果物B の SRC-539 |
| SRC-563 | Saito Z, Kaneko Y, Hasegawa T, et al. Predictive factors for relapse of cryptogenic organizing pneumonia. BMC Pulm Med 2019;19 | 10.1186/s12890-018-0764-8 | — | Crossref の license 欄 CC BY 4.0（2026-10-28 の照合） | OPEN | DOAJ の抄録ページ。DOI は出版社 PDF の URL、PMCID は検索結果の題名で確認 | 成果物B の SRC-540（source_class を Crossref で UNKNOWN→OPEN） |
| SRC-564 | Agency for Toxic Substances and Disease Registry. Medical Management Guidelines for Chlorine（最終確認 2014-10-21、アーカイブ） | — | — | 米国連邦政府の著作物（ATSDR） | GOV_US | ATSDR のページを直接取得 | 成果物B の SRC-541 |
| SRC-565 | Madariaga MLL, Gaissert HA. Overview of malignant tracheal tumors. Ann Cardiothorac Surg 2018;7(2):244-254 | 10.21037/acs.2018.03.04 | — | CC BY-NC-ND 4.0 | RESTRICTED | 出版社ページ（本文）でライセンス表示を確認 | 成果物B の SRC-546 |
| SRC-568 | National Cancer Institute. Small Cell Lung Cancer Treatment (PDQ®)–Health Professional Version（最終更新 2025-05-14） | — | — | 米国連邦政府の著作物（NCI）。PDQ の名称で示すには全文掲載が条件 | GOV_US | NCI のページを直接取得 | 成果物B の SRC-555 |
| SRC-569 | Cheng Y, Spigel DR, Cho BC, et al. Durvalumab after Chemoradiotherapy in Limited-Stage Small-Cell Lung Cancer. N Engl J Med 2024（ADRIATIC） | 10.1056/NEJMoa2404873 | — | 未確認 | UNKNOWN | 大学の業績ページの抄録 | 成果物B の SRC-557 |
| SRC-570 | Ricoy J, Rodríguez-Núñez N, Álvarez-Dobaño JM, et al. Diaphragmatic dysfunction. Pulmonology 2019 | — | — | 未確認 | UNKNOWN | 出版社ページ（本文） | 成果物B の SRC-559 |

## 2. 事実票 YAML

```yaml
- id: RI-054
  domain: RI
  subdomain: 肺吸虫症
  assertion:
    plain_statement_ja: 肺吸虫症は、喀痰中の虫卵の証明で診断できた例と、便中の虫卵でのみ証明できた例があり、プラジカンテル75 mg/kg/日を2日間経口投与した報告では、投与を完遂した7例中6例で90日までに喀痰と便の虫卵が陰性化し、残る1例も120日までに陰性化した。
    condition:
      study: 1985年の症例シリーズ（8例）と総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-530
    source: 'Johnson RJ, Jong EC, Dunning SB, Carberry WL, Minshew BH. Paragonimiasis: diagnosis and the use of praziquantel in treatment. Rev Infect Dis. 1985;7(2):200-206'
    doi: 10.1093/clinids/7.2.200
    pmid: '4001715'
    pmcid: null
    url: https://doi.org/10.1093/clinids/7.2.200
    source_license: ライセンス表示を確認できず（Crossref のレコードに license 欄なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 1985年の報告であり、現在の国内の標準治療・承認状況は確認していない。出典のライセンスも未確認のため、取り込み時に確認が必要。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-1-F-①（吸虫症、線虫症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-055
  domain: RI
  subdomain: 縦隔炎
  assertion:
    plain_statement_ja: 下行性壊死性縦隔炎は、口腔咽頭の感染が深頸部の間隙を下行して縦隔へ広がる重篤な縦隔炎で、死亡率は約20%とされる。治療は集中治療下での抗菌薬投与と頸部の感染源の除去が前提で、縦隔の進展範囲に応じた適切な外科的ドレナージが基盤となり、外科・麻酔科・耳鼻咽喉科・歯科口腔外科などによる集学的治療を要する。
    condition: null
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-531
    source: Šafránek J. Descending necrotizing mediastinitis – a surgical view. Rozhledy v chirurgii. 2024;103(12):502-504
    doi: 10.48095/ccrvch2024502
    pmid: '40221899'
    pmcid: null
    url: https://doi.org/10.48095/ccrvch2024502
    source_license: ライセンス表示を確認できず（Crossref のレコードに license 欄なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 単一施設の実践を含む総説であり、死亡率約20%はその総説の記載に基づく。出典のライセンスは未確認のため、取り込み時に確認が必要。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-244 (id: Jlvnl1o)'
    kokushi: 医学各論 Ⅳ-1-G-③（縦隔炎、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-037
  domain: RO
  subdomain: 気管・気管支の狭窄・閉塞
  assertion:
    plain_statement_ja: 非悪性の気管狭窄60例を集計した後方視研究では、原因の93.3%（56例）が挿管後で、平均の挿管期間は13.8日、狭窄部位は気管の上部3分の1が81.7%を占め、外科的な切除と端々吻合で良好な転帰を得た割合は89.1%で、気管支鏡下の拡張術の75.0%を上回った。
    condition:
      region: エチオピアの3施設
      study: 2018〜2023年に治療された60例の後方視研究
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-532
    source: 'Gulilat D, Genetu A, Kejela S, Kassa S, Bekele A, Tizazu A. Nonmalignant tracheal stenosis: presentation, management and outcome in limited resources setting. J Cardiothorac Surg. 2024;19(1):21'
    doi: 10.1186/s13019-024-02480-w
    pmid: '38263174'
    pmcid: PMC10804803
    url: https://doi.org/10.1186/s13019-024-02480-w
    source_license: CC BY 4.0（誌面の Open Access 表示と Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 資源の限られた環境での単一国の後方視研究であり、日本の診療環境への一般化は確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-2-A-⑤（気管・気管支の狭窄・閉塞、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-038
  domain: RO
  subdomain: 肺分画症
  assertion:
    plain_statement_ja: 成人の肺分画症の手術例97例では、病変の96例が脊椎に近い下葉にあり、栄養動脈の起始は胸部大動脈が87.4%、腹部大動脈が10.5%で、肺葉内型が90.7%、肺葉外型が9.3%を占めた。CTでの形態は、腫瘤状が50.5%と最も多く、次いで嚢胞状が20.6%だった。
    condition:
      region: 中国の単一施設
      study: 2011〜2021年に治療された成人の手術例97例の後方視研究
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-533
    source: 'Ren S, Yang L, Xiao Y, Tong Z, Wang L, Hu Y. Pulmonary sequestration in adult patients: a single-center retrospective study. Respir Res. 2023;24(1):13'
    doi: 10.1186/s12931-023-02320-w
    pmid: '36635696'
    pmcid: PMC9837954
    url: https://doi.org/10.1186/s12931-023-02320-w
    source_license: CC BY 4.0（誌面の Open Access 表示と Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 手術に至った成人例のみの集計であり、無症状のまま経過する例や未手術例を含めた全体の分布とは異なる可能性がある。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-2-B-③（肺分画症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-039
  domain: RO
  subdomain: 肺損傷
  assertion:
    plain_statement_ja: 肺挫傷は鈍的胸部外傷の25〜35%に生じ、肺組織の裂傷を伴わずに肺胞の毛細血管が損傷して血液や液体が肺組織内にたまり、ガス交換が障害される病態である。治療は支持療法が中心で、酸素投与と、適応がある場合の人工呼吸を行う。
    condition: null
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-534
    source: 'Ganie FA, Lone H, Lone GN, Wani ML, Singh S, Dar AM, Wani N, Wani SN, Nazeer N. Lung Contusion: A Clinico-Pathological Entity with Unpredictable Clinical Course. Bull Emerg Trauma. 2013;1(1):7-16'
    doi: null
    pmid: '27162815'
    pmcid: PMC4771236
    url: null
    source_license: ライセンス表示を確認できず（誌面に CC の表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: DOI は誌面と抄録ページの表示で確認できなかったため null とした。出典のライセンスも未確認。本文中で引用されていた死亡率10〜25%は二次引用のため、主張文には採用していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-2-D-②（肺損傷、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-049
  domain: IL
  subdomain: 悪性リンパ腫、白血病
  assertion:
    plain_statement_ja: 原発性肺リンパ腫は肺腫瘍の1%未満を占めるまれなリンパ腫で、肺にみられるリンパ腫の大半は全身性リンパ腫の二次性肺病変である。原発性肺リンパ腫の内訳はMALTリンパ腫が70〜90%と最も多く、次いでびまん性大細胞型B細胞リンパ腫が10〜20%を占める。約半数は無症状で画像の異常を契機に見つかり、MALTリンパ腫の5年全生存率は80%を超える。
    condition: null
    differential: null
    common_misconception: 肺にみられるリンパ腫の多くは原発性である
  provenance:
    source_ref: SRC-538
    source: Cherian SV, Tang VK, Vijhani P, Ambelil M, Estrada-Y-Martin RM. Primary pulmonary lymphoproliferative neoplasms. Lung India 2018;35:220
    doi: 10.4103/lungindia.lungindia_381_17
    pmid: '29697079'
    pmcid: PMC5946555
    url: https://doi.org/10.4103/lungindia.lungindia_381_17
    source_license: CC BY-NC-SA 4.0（PMC ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 割合はいずれもレビューが引用する複数報告の集約であり、単一コホートの値ではない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-3-B-⑥（悪性リンパ腫、白血病、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-050
  domain: IL
  subdomain: Langerhans細胞組織球症
  assertion:
    plain_statement_ja: 肺Langerhans細胞組織球症は主に喫煙する若年成人に起こり、細気管支周囲にできた星芒状の結節が空洞化して厚壁・薄壁の嚢胞へと進む。高分解能CTでは上・中肺野に優位で肺底部が比較的保たれる結節と嚢胞の混在が特徴で、初期は結節優位、後期は嚢胞優位になる。治療の基本は禁煙である。
    condition: null
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-539
    source: 'Abbott GF, Rosado-de-Christenson ML, Franks TJ, Frazier AA, Galvin JR. From the archives of the AFIP: Pulmonary Langerhans cell histiocytosis. RadioGraphics 2004;24:821-841'
    doi: 10.1148/rg.243045005
    pmid: '15143231'
    pmcid: null
    url: https://doi.org/10.1148/rg.243045005
    source_license: Crossref の license 欄に記載なし（未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ライセンス表示を Crossref で確認できなかったため、source_class は UNKNOWN とした。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-3-B-⑦（Langerhans細胞組織球症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-051
  domain: IL
  subdomain: アミロイドーシス
  assertion:
    plain_statement_ja: 原発性気管気管支アミロイドーシスは、全身性アミロイドーシスを伴わずに気管・気管支の粘膜下にアミロイドが沈着するまれな疾患である。中国の報告例107例の解析では105例が気管支鏡生検で病理学的に確定診断され、自験2例を含む109例では初診時の誤診率が45%に達した。気管支鏡による介入治療を受けた53例では51例が改善した。
    condition:
      region: 中国
      study: 1981〜2015年の報告例107例と自験2例の後方視的解析
    differential: 慢性気管支炎、気管支内結核、肺腫瘍、気管支喘息
    common_misconception: null
  provenance:
    source_ref: SRC-540
    source: 'Lu X, He B, Wang G, He B, Wang L, Chen Q. Bronchoscopic Diagnosis and Treatment of Primary Tracheobronchial Amyloidosis: A Retrospective Analysis from China. BioMed Res Int 2017;2017:3425812'
    doi: 10.1155/2017/3425812
    pmid: '28197412'
    pmcid: PMC5288517
    url: https://doi.org/10.1155/2017/3425812
    source_license: CC BY 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-3-B-⑧（アミロイドーシス、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-052
  domain: IL
  subdomain: 特発性器質化肺炎
  assertion:
    plain_statement_ja: 特発性器質化肺炎（COP）は、感染・薬剤・膠原病などの原因が特定できない器質化肺炎で、典型的には呼吸困難と咳嗽で発症し、画像では多発性の斑状の肺胞陰影を示す。確定診断は肺生検で遠位気腔内に肉芽組織の芽を確認することによる。副腎皮質ステロイドが速やかに効くが、減量や中止の際に再発が多い。
    condition: null
    differential: null
    common_misconception: 細菌性肺炎であり抗菌薬が有効である
  provenance:
    source_ref: SRC-541
    source: Cordier JF. Cryptogenic organizing pneumonia. Clin Chest Med 2004;25:727-738
    doi: 10.1016/j.ccm.2004.06.003
    pmid: '15564018'
    pmcid: PMC7119066
    url: https://doi.org/10.1016/j.ccm.2004.06.003
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: 医学各論 Ⅳ-4-A-③（特発性器質化肺炎<COP>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-053
  domain: IL
  subdomain: 化学薬品、重金属などによる肺障害
  assertion:
    plain_statement_ja: 超硬金属（炭化タングステンとコバルト）部品を製造する工場の元労働者125人のうち42人を調べた研究では、胸部画像または肺機能の異常が16人にみられ、肺生検と剖検の例で巨細胞性間質性肺炎と炭化タングステンの存在が確認された。異常の有無と曝露期間の間に相関はみられなかった。
    condition:
      region: 米国
      study: 超硬金属工場の元労働者の調査（1983〜1985年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-542
    source: Auchincloss JH, Abraham JL, Gilbert R, Lax M, Henneberger PK, Heitzman ER, Peppi DJ. Health hazard of poorly regulated exposure during manufacture of cemented tungsten carbides and cobalt. Br J Ind Med 1992;49:832-836
    doi: 10.1136/oem.49.12.832
    pmid: '1472440'
    pmcid: PMC1061212
    url: https://doi.org/10.1136/oem.49.12.832
    source_license: Crossref の license 欄に記載なし（未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ライセンス表示を Crossref で確認できなかったため source_class は UNKNOWN とした。1992年の単一工場での調査であり、現在の曝露環境への一般化には限界がある。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-4-C-②（化学薬品、重金属などによる肺障害、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-054
  domain: IL
  subdomain: 酸素中毒
  assertion:
    plain_statement_ja: 酸素の肺毒性は吸入酸素分画と曝露時間で決まり、1気圧では吸入酸素分画が0.60を超える酸素を24時間を超えて投与すると肺に毒性が生じうる。肺毒性の経過は気管気管支炎、ARDS、肺の間質性線維化の段階をとり、毒性を抑える目安として吸入酸素分画を0.40〜0.5未満に保つことが挙げられる。
    condition:
      pressure: 1気圧（常圧）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-543
    source: 'Lius EE, Syafaah I. Hyperoxia in the management of respiratory failure: A literature review. Ann Med Surg 2022;81:104393'
    doi: 10.1016/j.amsu.2022.104393
    pmid: '36147110'
    pmcid: PMC9486660
    url: https://doi.org/10.1016/j.amsu.2022.104393
    source_license: CC BY-NC-ND 4.0（PMC ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 吸入酸素分画と時間の値はレビューが引用する既報の集約であり、個々の患者での厳密な安全域を示すものではない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-4-C-④（酸素中毒、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-055
  domain: IL
  subdomain: パラコート中毒
  assertion:
    plain_statement_ja: パラコートは30 mg/kg程度の摂取で致死的となり得て、これは市販の24.6%製剤7〜8 mLに相当する。重症例は早期に循環不全で死亡し、経過が延びた例では肺線維症を来す。肺内のパラコート濃度は血漿の6〜10倍に達しうるため、体外除去は肺への移行が進む前、摂取後15時間以内の開始が重要とされる。
    condition:
      route: 経口摂取
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-544
    source: Yoon SC. Clinical Outcome of Paraquat Poisoning. Korean J Intern Med 2009;24:93-94
    doi: 10.3904/kjim.2009.24.2.93
    pmid: '19543485'
    pmcid: PMC2698628
    url: https://doi.org/10.3904/kjim.2009.24.2.93
    source_license: CC BY-NC 4.0（PMC ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本出典は総説的な論説であり、致死量と生存率は本稿自体の症例データではなく、引用された既報に基づく二次的な記述を含む。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-4-C-⑤（パラコート中毒、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-056
  domain: IL
  subdomain: 肺胞微石症
  assertion:
    plain_statement_ja: 肺胞微石症は、SLC34A2遺伝子の機能喪失型変異による常染色体劣性遺伝疾患で、肺胞内にリン酸カルシウムの微小結石が広範に沈着し、世界で約1,100例が報告されている。胸部画像では砂嵐様のびまん性微小石灰化が特徴で、画像所見の広がりに比べて症状が軽いという乖離が大きい。根治的な治療はなく、一部の進行例では肺移植が必要になる。
    condition: null
    differential: null
    common_misconception: 血清カルシウムやリンの異常が原因である
  provenance:
    source_ref: SRC-545
    source: Enemark A, Jönsson ÅLM, Kronborg-White S, Bendstrup E. Pulmonary Alveolar Microlithiasis – A Review. Yale J Biol Med 2021;94
    doi: null
    pmid: '34970102'
    pmcid: PMC8686773
    url: null
    source_license: CC BY-NC（PMC ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: DOI は Crossref の検索と ID 変換のいずれでも確認できなかったため null とした。誌面のページ範囲も未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-4-F-①（肺胞微石症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-039
  domain: LC
  subdomain: 気管・気管支腫瘍
  assertion:
    plain_statement_ja: 原発性気管・気管支腫瘍は呼吸器腫瘍の約0.2%を占めるまれな腫瘍で、症状が喘息や気管支炎と紛らわしく誤診されやすい。診断にはCTと気管支鏡が最も有用で、切除可能であれば外科切除が最も有効な治療であり、切除不能例では放射線治療・化学療法・気管支鏡下インターベンションが補完的に用いられる。標準治療のコンセンサスは確立していない。
    condition:
      study: 原発性気管気管支腫瘍の診断と治療に関するレビュー
      region: 国際
    differential: 喘息・気管支炎（症状が類似し、誤診の原因となる）
    common_misconception: null
  provenance:
    source_ref: SRC-548
    source: Shu C, Liu YJ, Zheng KF, et al. Diagnosis and Treatment of Primary Tracheobronchial Tumors. Cancer Med 2025;14(9):e70893
    doi: 10.1002/cam4.70893
    pmid: '40289301'
    pmcid: PMC12034573
    url: https://doi.org/10.1002/cam4.70893
    source_license: CC BY 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本カードはレビュー論文に基づく。国内ガイドラインにおける位置づけは未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-6-B-②（気管・気管支腫瘍、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-040
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 未治療の進行非小細胞肺癌でPD-L1の腫瘍割合スコア（TPS）が50%以上、EGFR感作性変異とALK転座がない患者では、ペムブロリズマブ単剤はプラチナ併用化学療法より無増悪生存期間を延長し（中央値10.3か月対6.0か月、ハザード比0.50）、全生存期間も延長した（ハザード比0.60）。グレード3〜5の治療関連有害事象は26.6%対53.3%とペムブロリズマブ群で少なかった。
    condition:
      study: KEYNOTE-024（国際共同第III相試験、305例）
      region: 国際共同
    differential: null
    common_misconception: PD-L1の発現率にかかわらず、一次治療はペムブロリズマブ単剤でよい
  provenance:
    source_ref: SRC-549
    source: Reck M, Rodríguez-Abreu D, Robinson AG, et al. Pembrolizumab versus Chemotherapy for PD-L1-Positive Non-Small-Cell Lung Cancer. N Engl J Med 2016;375:1823-1833
    doi: 10.1056/NEJMoa1606774
    pmid: '27718847'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1606774
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ペムブロリズマブの国内承認・保険適用の範囲は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-041
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: KEYNOTE-024の5年追跡では、ペムブロリズマブ群の全生存期間中央値は26.3か月、化学療法群は13.4か月（ハザード比0.62）、5年生存割合は31.9%対16.3%であり、化学療法群から抗PD-1/PD-L1療法への実効クロスオーバーが66.0%あったにもかかわらず長期の生存優位が保たれた。ペムブロリズマブを35サイクル（約2年）完遂した39例では、82.1%がデータカットオフ時点で生存していた。
    condition:
      study: KEYNOTE-024の5年追跡報告（追跡中央値59.9か月）
      region: 国際共同
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-550
    source: Reck M, Rodríguez-Abreu D, Robinson AG, et al. Five-Year Outcomes With Pembrolizumab Versus Chemotherapy for Metastatic Non-Small-Cell Lung Cancer With PD-L1 Tumor Proportion Score ≥ 50%. J Clin Oncol 2021;39:2339-2349
    doi: 10.1200/JCO.21.00174
    pmid: '33872070'
    pmcid: PMC8280089
    url: https://doi.org/10.1200/JCO.21.00174
    source_license: CC BY-NC-ND 4.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ペムブロリズマブの国内承認・保険適用の範囲は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-042
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 切除不能III期非小細胞肺癌で同時化学放射線療法後に増悪しなかった患者では、地固め療法としてのデュルバルマブはプラセボより無増悪生存期間を延長した（中央値16.8か月対5.6か月、ハザード比0.52）。奏効率は28.4%対16.0%、死亡または遠隔転移までの期間の中央値は23.2か月対14.6か月だった。
    condition:
      study: PACIFIC（国際共同第III相試験）
      region: 国際共同
    differential: null
    common_misconception: 化学放射線療法で増悪した症例にも地固め療法として使える（対象は増悪しなかった症例）
  provenance:
    source_ref: SRC-551
    source: Antonia SJ, Villegas A, Daniel D, et al. Durvalumab after Chemoradiotherapy in Stage III Non-Small-Cell Lung Cancer. N Engl J Med 2017;377:1919-1929
    doi: 10.1056/NEJMoa1709937
    pmid: '28885881'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1709937
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: デュルバルマブの国内承認・保険適用の範囲は本調査では確認していない。全生存期間の長期成績は5年追跡報告（LC-043）を参照。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-043
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: PACIFIC試験の約5年追跡でもデュルバルマブ地固め療法の優位は持続し、全生存期間中央値は47.5か月対29.1か月（ハザード比0.72）、5年生存割合は42.9%対33.4%、無増悪生存期間中央値は16.9か月対5.6か月（ハザード比0.55）、5年無増悪生存割合は33.1%対19.0%だった。
    condition:
      study: PACIFICの5年追跡報告（713例が無作為化され、709例が治療を受けた）
      region: 国際共同
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-552
    source: 'Spigel DR, Faivre-Finn C, Gray JE, et al. Five-Year Survival Outcomes From the PACIFIC Trial: Durvalumab After Chemoradiotherapy in Stage III Non-Small-Cell Lung Cancer. J Clin Oncol 2022;40:1301-1311'
    doi: 10.1200/JCO.21.01308
    pmid: '35108059'
    pmcid: PMC9015199
    url: https://doi.org/10.1200/JCO.21.01308
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本報告は更新された探索的解析と位置づけられている。デュルバルマブの国内承認・保険適用の範囲は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-044
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 腫瘍径2cm以下で充実成分優位（CTR 0.5超）の末梢型臨床病期IA非小細胞肺癌では、区域切除は肺葉切除に対して全生存期間で劣らず、むしろ優れていた（5年生存割合94.3%対91.1%、ハザード比0.663）。無再発生存期間は両群でほぼ同等（5年88.0%対87.9%）だったが、局所再発は区域切除群で多かった（約11%対約5%）。
    condition:
      study: JCOG0802/WJOG4607L（国内多施設第III相試験、1106例、追跡中央値7.3年）
      region: 日本
    differential: null
    common_misconception: すりガラス成分優位の病変にもこの結果がそのまま当てはまる（対象はCTR 0.5超の充実成分優位病変）
  provenance:
    source_ref: SRC-553
    source: 'Saji H, Okada M, Tsuboi M, et al. Segmentectomy versus lobectomy in small-sized peripheral non-small-cell lung cancer (JCOG0802/WJOG4607L): a multicentre, open-label, phase 3, randomised, controlled, non-inferiority trial. Lancet 2022;399:1607-1617'
    doi: 10.1016/S0140-6736(21)02333-3
    pmid: '35461558'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(21)02333-3
    source_license: Elsevier の利用条件（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 術後1年のFEV1低下の群間差は3.5%で、事前に定められた臨床的意義の目安（10%）には届かなかった。結果は腫瘍径2cm以下・CTR 0.5超の末梢病変に限られ、それ以外への外挿はできない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-045
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 腫瘍径2cm以下の末梢型で臨床病期T1aN0の非小細胞肺癌で、術中にリンパ節転移陰性が確認された患者では、肺葉切除より小さい切除（部分切除）は肺葉切除に対して無病生存期間で劣らなかった（ハザード比1.01）。5年無病生存割合は63.6%対64.1%、5年生存割合は80.3%対78.9%で、局所領域・全身再発の頻度に大きな差はなく、術後6か月のFEV1（予測値に対する割合）の群間差は2ポイントと部分切除群が有利だった。
    condition:
      study: CALGB 140503（国際共同第III相非劣性試験、697例、追跡中央値7年）
      region: 国際共同
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-554
    source: Altorki N, Wang X, Kozono D, et al. Lobar or Sublobar Resection for Peripheral Stage IA Non-Small-Cell Lung Cancer. N Engl J Med 2023;388:489-498
    doi: 10.1056/NEJMoa2212083
    pmid: '36780674'
    pmcid: PMC10036605
    url: https://doi.org/10.1056/NEJMoa2212083
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 部分切除群の術式内訳（区域切除と楔状切除の割合）は抄録に記載なし。区域切除のみを扱ったJCOG0802（LC-044）とは対象と術式が異なる。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-046
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 未治療の進行ALK陽性非小細胞肺癌では、アレクチニブはクリゾチニブより無増悪生存期間を延長した（独立評価委員会評価の中央値25.7か月対10.4か月、ハザード比0.50）。中枢神経系の進行も抑えられ（原因特異的ハザード比0.16、12か月時点の累積CNS進行率9.4%対41.4%）、奏効率は82.9%対75.5%、グレード3〜5の有害事象は41%対50%とアレクチニブ群で少なかった。
    condition:
      study: ALEX（国際共同第III相試験、303例、無症候性の中枢神経系病変のある患者を含む）
      region: 国際共同
    differential: null
    common_misconception: 脳転移があるとALK阻害薬は使えない（本試験には無症候性の中枢神経系病変のある患者も登録された）
  provenance:
    source_ref: SRC-555
    source: Peters S, Camidge DR, Shaw AT, et al. Alectinib versus Crizotinib in Untreated ALK-Positive Non-Small-Cell Lung Cancer. N Engl J Med 2017;377:829-838
    doi: 10.1056/NEJMoa1704795
    pmid: '28586279'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1704795
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: アレクチニブの国内承認用量・保険適用の範囲は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-047
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 未治療の進行ALK陽性非小細胞肺癌では、第三世代ALK阻害薬のロルラチニブはクリゾチニブより無増悪生存期間を大きく延長した（12か月時点で増悪なく生存していた割合78%対39%、ハザード比0.28）。奏効率は76%対58%、測定可能な脳転移のある患者での頭蓋内奏効率は82%対23%で、ロルラチニブ群では71%に頭蓋内完全奏効がみられた。一方、グレード3〜4の有害事象（主に脂質異常）は72%対56%とロルラチニブ群で多かった。
    condition:
      study: CROWN（国際共同第III相試験、296例）
      region: 国際共同
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-556
    source: Shaw AT, Bauer TM, de Marinis F, et al. First-Line Lorlatinib or Crizotinib in Advanced ALK-Positive Lung Cancer. N Engl J Med 2020;383:2018-2029
    doi: 10.1056/NEJMoa2027187
    pmid: '33207094'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2027187
    source_license: NEJM の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本報告は計画された中間解析の結果である。ロルラチニブの国内承認・保険適用の範囲は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-048
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 小細胞肺癌は限局型と進展型に分ける方法が広く使われてきたが、国際肺癌学会のデータベースに登録された5002例の解析では、TNM分類のTカテゴリーとNカテゴリーごとに生存期間の差が確認され、第8版でも小細胞肺癌にTNM病期分類を用いることが支持された。転移については、脳のみの単一臓器転移が他の単一臓器転移より予後がよい傾向がみられた。
    condition:
      study: IASLC Lung Cancer Staging Project（1999〜2010年登録の小細胞肺癌5002例の生存解析）
      region: 国際
    differential: null
    common_misconception: 小細胞肺癌ではTNM分類は使わず、限局型・進展型の区別だけでよい
  provenance:
    source_ref: SRC-557
    source: 'Nicholson AG, Chansky K, Crowley J, et al. The International Association for the Study of Lung Cancer Lung Cancer Staging Project: Proposals for the Revision of the Clinical and Pathologic Staging of Small Cell Lung Cancer in the Forthcoming Eighth Edition of the TNM Classification for Lung Cancer. J Thorac Oncol 2016;11:300-311'
    doi: 10.1016/j.jtho.2015.10.008
    pmid: '26723244'
    pmcid: null
    url: https://doi.org/10.1016/j.jtho.2015.10.008
    source_license: Elsevier の利用条件（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 限局型・進展型の定義そのものは本資料の主対象ではなく、別資料での確認が要る。脳のみの単一臓器転移の予後差が解剖学的進展度によるのか治療選択の差によるのかは、本論文でも未確定とされている。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-049
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 進展型小細胞肺癌の一次治療では、プラチナ製剤とエトポシドの併用にアテゾリズマブを上乗せすると全生存期間が延長した（中央値12.3か月対10.3か月、ハザード比0.70）。無増悪生存期間も5.2か月対4.3か月（ハザード比0.77）と延長し、1年生存割合は51.7%対38.2%だった。
    condition:
      study: IMpower133（国際共同第III相試験、403例）
      region: 国際共同
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-558
    source: Horn L, Mansfield AS, Szczęsna A, et al. First-Line Atezolizumab plus Chemotherapy in Extensive-Stage Small-Cell Lung Cancer. N Engl J Med 2018;379:2220-2229
    doi: 10.1056/NEJMoa1809064
    pmid: '30280641'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1809064
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: アテゾリズマブの国内承認・保険適用の範囲は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-050
  domain: LC
  subdomain: 胸膜中皮腫
  assertion:
    plain_statement_ja: 未治療の切除不能な悪性胸膜中皮腫では、ニボルマブとイピリムマブの併用はプラチナ製剤とペメトレキセドによる化学療法より全生存期間を延長した（中央値18.1か月対14.1か月、ハザード比0.74）。
    condition:
      study: CheckMate 743（国際共同第III相試験、605例、ECOG PS 0〜1、追跡中央値29.7か月）
      region: 国際共同
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-559
    source: 'Baas P, Scherpereel A, Nowak AK, et al. First-line nivolumab plus ipilimumab in unresectable malignant pleural mesothelioma (CheckMate 743): a multicentre, randomised, open-label, phase 3 trial. Lancet 2021;397:375-386'
    doi: 10.1016/S0140-6736(20)32714-8
    pmid: '33485464'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(20)32714-8
    source_license: Elsevier の利用条件（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ニボルマブとイピリムマブ併用の国内承認・保険適用の範囲は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-644 (id: JlvnmcM)'
    kokushi: 医学各論 Ⅳ-6-D-①（胸膜中皮腫、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-051
  domain: LC
  subdomain: 胸膜中皮腫
  assertion:
    plain_statement_ja: CheckMate 743の追跡中央値43.1か月の報告でもニボルマブとイピリムマブ併用の優位は持続し、全生存期間中央値は18.1か月対14.1か月（ハザード比0.73）、3年生存割合は23%対15%、3年無増悪生存割合は14%対1%だった。奏効率は40%対44%と化学療法群がやや高かったが、3年時点で奏効が持続していたのは併用群の奏効例の28%に対し化学療法群では0%だった。
    condition:
      study: CheckMate 743の3年追跡報告（最低3年の追跡）
      region: 国際共同
    differential: null
    common_misconception: 奏効率が高い治療のほうが長期生存もよい（本試験では奏効率は化学療法群がやや高かったが、生存と奏効の持続は併用群が優れた）
  provenance:
    source_ref: SRC-560
    source: 'Peters S, Scherpereel A, Cornelissen R, et al. First-line nivolumab plus ipilimumab versus chemotherapy in patients with unresectable malignant pleural mesothelioma: 3-year outcomes from CheckMate 743. Ann Oncol 2022;33:488-499'
    doi: 10.1016/j.annonc.2022.01.074
    pmid: '35124183'
    pmcid: null
    url: https://doi.org/10.1016/j.annonc.2022.01.074
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ニボルマブとイピリムマブ併用の国内承認・保険適用の範囲は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-644 (id: JlvnmcM)'
    kokushi: 医学各論 Ⅳ-6-D-①（胸膜中皮腫、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-028
  domain: PL
  subdomain: 横隔神経麻痺
  assertion:
    plain_statement_ja: 症状のある一側横隔膜麻痺（横隔神経麻痺）では、吸気筋力の低下は麻痺側だけにとどまらない。努力肺活量（FVC）が予測値の80%未満の一側横隔膜麻痺27例（右9例・左18例）と健常対照20例の比較では、最大吸気圧は右麻痺群-57.4±16.9 cmH2O、左麻痺群-67.1±28.5 cmH2Oと、対照群の-103.1±30.4 cmH2Oより小さく、磁気刺激による横隔膜圧（PdiTw）も右麻痺群5.7±4 cmH2O、左麻痺群4.8±2.3 cmH2Oと対照群の15.3±5.7 cmH2Oより低かった。PdiTwは麻痺していない側を刺激しても低下しており、胃内圧の寄与が対照群の約50%に対して約30%と小さいことが関係していた。
    condition: null
    differential: null
    common_misconception: 一側の横隔膜麻痺では、吸気筋力の低下は麻痺した側の横隔膜だけが原因である
  provenance:
    source_ref: SRC-566
    source: 'Caleffi-Pereira M, et al. Unilateral diaphragm paralysis: a dysfunction restricted not just to one hemidiaphragm. BMC Pulm Med 2018;18:126'
    doi: 10.1186/s12890-018-0698-1
    pmid: '30068327'
    pmcid: PMC6090915
    url: https://doi.org/10.1186/s12890-018-0698-1
    source_license: CC BY 4.0（PMC の論文ページと Crossref の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 対象は単一施設で FVC が予測値の80%未満の有症状の一側横隔膜麻痺に限られ、無症状例と両側麻痺は含まれない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-246 (id: Jlvnl10)'
    kokushi: 医学各論 Ⅳ-7-C-④（横隔神経麻痺、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-029
  domain: PL
  subdomain: 横隔膜弛緩症
  assertion:
    plain_statement_ja: 横隔膜弛緩症は、横隔膜に解剖学的な欠損がないにもかかわらず片側の横隔膜が持続的に挙上する状態で、横隔膜ヘルニアとは区別される。先天性は横隔膜の筋構造の形成不全によるもの、後天性は横隔神経障害に続発するもので、横隔膜麻痺とは別の病態とされるが、画像所見や臨床像は似る。症状のある成人42例に縫縮術を行った検討では、左側が33例と多く、原因は特発性45.2%、外傷33.3%、手術21.4%で、術前の1秒量は予測値の62%、FVCは61%だった。縫縮術の1年後に1秒量は23%、FVCは24%改善し、呼吸困難のスコア（mMRC）は3.0から0.9に下がり、平均28か月の観察で再発はなかった。
    condition: null
    differential: 横隔膜ヘルニア、横隔膜麻痺
    common_misconception: 横隔膜の挙上はすべて横隔膜ヘルニアによるものである
  provenance:
    source_ref: SRC-567
    source: 'Evman S, et al. Comparison of Mid-Term Clinical Outcomes of Different Surgical Approaches in Symptomatic Diaphragmatic Eventration. Ann Thorac Cardiovasc Surg 2016;22:224-229'
    doi: 10.5761/atcs.oa.16-00018
    pmid: '27076066'
    pmcid: PMC5045849
    url: https://doi.org/10.5761/atcs.oa.16-00018
    source_license: 未確認（PMC と J-STAGE の論文ページ、Crossref のいずれにもライセンス表示なし。©2016 Annals of Thoracic and Cardiovascular Surgery）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 対象は単一施設で縫縮術を受けた有症状の成人42例に限られる後ろ向き検討で、無症状例の経過は示されていない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-7-C-⑤（横隔膜弛緩症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-056
  domain: RI
  subdomain: 吸虫症、線虫症
  assertion:
    plain_statement_ja: 肺吸虫症は、淡水産のカニやザリガニを生、加熱不十分、または酢漬け・塩漬けで食べて感染する。人で最も多い種はウェステルマン肺吸虫で、東南アジアと日本に分布する。食べた幼虫（メタセルカリア）は十二指腸で脱囊し、腸管壁と腹膜を貫き、横隔膜を通って肺に入って成虫になり、感染から65〜90日で虫卵が出始める。
    condition:
      region: US
      guideline: CDC
    differential:
    - 急性期（幼虫の移行期）には下痢・腹痛・発熱・咳嗽・蕁麻疹・肝脾腫・好酸球増多がみられ、慢性期には咳嗽、着色した痰、血痰と胸部画像の異常が続く
    - 脳や筋肉に迷入した虫は虫卵を体外に出せないが、脳への迷入は重症になる
    common_misconception: 肺吸虫は経気道的に吸い込んで感染する
  provenance:
    source_ref: SRC-535
    source: 'Centers for Disease Control and Prevention. DPDx: Paragonimiasis（最終更新 2024-06-06）'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/dpdx/paragonimiasis/index.html
    source_license: 米国連邦政府の著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 日本に分布する他の種（宮崎肺吸虫など）は出典に記載がない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-1-F-①（吸虫症、線虫症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を RI-054→RI-056、出典を SRC-530→SRC-535 に振り直した（主張文・数値は変更なし）
- id: RI-057
  domain: RI
  subdomain: 吸虫症、線虫症
  assertion:
    plain_statement_ja: 糞線虫症では、免疫の低下で自家感染が加速すると、多数の幼虫が消化管と肺を移動する過剰感染症候群となり、幼虫が多臓器に入ると播種性糞線虫症になる。最大の危険因子は喘息や COPD の増悪などに使う高用量の副腎皮質ステロイドである。肺では咳嗽・喘鳴・呼吸困難・喀血・呼吸不全とびまん性浸潤影がみられ、腸管から運ばれたグラム陰性菌による菌血症・敗血症や髄膜炎を合併し、未治療の死亡率は90%近くに達しうる。
    condition:
      region: US
      guideline: CDC
    differential:
    - 気管支肺胞洗浄液の湿潤標本で幼虫がみえることが多い
    common_misconception: 喘鳴に対して副腎皮質ステロイドを増量しても、糞線虫症は悪化しない
  provenance:
    source_ref: SRC-536
    source: Centers for Disease Control and Prevention. Clinical Overview of Strongyloides（最終更新 2026-02-11）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/strongyloides/hcp/clinical-overview/index.html
    source_license: 米国連邦政府の著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: HTLV-1 感染や臓器移植などの他の危険因子、免疫抑制前のスクリーニング、治療薬は今回取得したページに記載がない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-1-F-①（吸虫症、線虫症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を RI-056→RI-057、出典を SRC-532→SRC-536 に振り直した（主張文・数値は変更なし）
- id: RO-040
  domain: RO
  subdomain: 気管・気管支の狭窄・閉塞
  assertion:
    plain_statement_ja: 中枢気道狭窄では、労作時の呼吸困難は内腔が約8 mmまで、安静時の呼吸困難は5 mm未満まで狭くなって現れるとされ、初発症状は呼吸困難と喘鳴（stridor）が約半数を占める。診断には気管用の撮像条件の胸部 CT が有用である（感度約97%）。治療に使う気道ステントのうち、金属ステントは肉芽形成や破損の問題から良性狭窄には勧められず（2005年の米国 FDA の警告）、シリコンステントは抜去や位置の調整がしやすいが、移動や痰の貯留が起こりやすい。
    condition:
      region: global
      guideline: null
    differential:
    - 良性の気管狭窄への CO2 レーザー治療の成功率は、Myer-Cotton 分類のⅠ度92%、Ⅱ度46%、Ⅲ度13%と、狭窄が高度なほど低い
    common_misconception: 気管の内腔が半分程度に狭くなれば、必ず安静時にも呼吸困難が出る
  provenance:
    source_ref: SRC-537
    source: 'Guedes F, Branquinho MV, Sousa AC, et al. Central airway obstruction: is it time to move forward? BMC Pulm Med 2022;22:68'
    doi: 10.1186/s12890-022-01862-x
    pmid: null
    pmcid: null
    url: https://bmcpulmmed.biomedcentral.com/track/pdf/10.1186/s12890-022-01862-x
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 叙述的レビューに引用された研究の数値で、一次資料は未照合（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-02-06-024 (id: JlAKpic)'
    kokushi: 医学各論 Ⅳ-2-A-⑤（気管・気管支の狭窄・閉塞、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を RO-038→RO-040、出典を SRC-534→SRC-537 に振り直した（主張文・数値は変更なし）
- id: RO-041
  domain: RO
  subdomain: 肺損傷
  assertion:
    plain_statement_ja: 肺挫傷による呼吸不全は受傷後24〜48時間で明らかになることが多い。胸部エックス線は受傷早期の感度が低く、CT のほうが早く検出でき重症度の評価にも用いられる。管理では肺保護換気（1回換気量 約6 mL/kg 予測体重、プラトー圧30 cmH2O未満）と、最初の72時間の過剰な水分負荷を避けることが勧められ、副腎皮質ステロイドや感染のない時期の予防的抗菌薬のルーチン投与は勧められない。
    condition:
      region: global
      guideline: null
    differential:
    - 肋骨骨折の観血的固定は受傷後24〜72時間が望ましいとされ、肺挫傷は固定の禁忌とされない
    - 肺挫傷は肋骨骨折を伴う非軍事的な胸部外傷の約20%にみられるとされる
    common_misconception: 肺挫傷の範囲は来院時の胸部エックス線で正確に評価できる
  provenance:
    source_ref: SRC-546
    source: 'Chau HS, Gutkin PM, Knight AW, Forrester JD. Contemporary management of pulmonary contusions: a narrative review. Curr Chall Thorac Surg 2025;7:26'
    doi: 10.21037/ccts-25-18
    pmid: null
    pmcid: null
    url: https://ccts.amegroups.org/article/view/104722/html
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 叙述的レビューの記載。挫傷の容積20%以上で ARDS が82%（20%未満では22%）などの数値は引用元が別の研究で、一次資料は未照合（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-2-D-②（肺損傷、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を RO-040→RO-041、出典を SRC-536→SRC-546 に振り直した（主張文・数値は変更なし）
- id: IL-057
  domain: IL
  subdomain: 悪性リンパ腫、白血病
  assertion:
    plain_statement_ja: 原発性肺悪性リンパ腫の80〜90%は MALT リンパ腫（節外性辺縁帯リンパ腫）で、肺 MALT リンパ腫は肺の悪性腫瘍の0.5〜1%を占め、60〜70歳代に多く、約20%に自己免疫疾患を合併する。経過は緩徐で、後ろ向き研究の5年全生存率は約85〜90%である。無症状で病変量が少なければ経過観察、限局例には放射線療法（単発病変では切除も選択肢）、進行例や有症状例にはリツキシマブを含む免疫化学療法が用いられる。
    condition:
      region: global
      guideline: null
    differential:
    - 米国 SEER の解析では5年・10年全生存率が75%・53%と、施設の後ろ向き研究より低い
    common_misconception: 肺 MALT リンパ腫は診断後ただちに多剤併用化学療法を始める必要がある
  provenance:
    source_ref: SRC-547
    source: Sapuppo G, Frazzetto S, Pirosa MC, Zucca E. Epidemiology, diagnosis, and treatment of primary pulmonary mucosa-associated lymphoid tissue lymphoma. Chin Clin Oncol 2026;15(3):46
    doi: 10.21037/cco-2025-1-134
    pmid: null
    pmcid: null
    url: https://cco.amegroups.org/article/view/155714/html
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: レビューに引用された研究の数値で、一次資料は未照合（二次資料経由）。白血病の肺浸潤は扱っていない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-3-B-⑥（悪性リンパ腫、白血病、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を IL-049→IL-057、出典を SRC-537→SRC-547 に振り直した（主張文・数値は変更なし）
- id: IL-058
  domain: IL
  subdomain: Langerhans細胞組織球症
  assertion:
    plain_statement_ja: 肺 Langerhans 細胞組織球症の肺結節では約50%に BRAF V600E 変異、さらに約20%に MAP2K1 変異がみられる。気胸は10〜30%で初発症状となり、経過中に30〜45%に起こる。肺に限局した例では、禁煙だけで約半数が部分的に退縮または安定する。
    condition:
      region: global
      guideline: null
    differential:
    - 病状が進む例ではクラドリビンが用いられ、22例の検討で奏効率は91%だった
    common_misconception: 肺 Langerhans 細胞組織球症の治療は、まず全身化学療法である
  provenance:
    source_ref: SRC-561
    source: Radzikowska E. Update on Pulmonary Langerhans Cell Histiocytosis. Front Med 2020;7:582581
    doi: 10.3389/fmed.2020.582581
    pmid: null
    pmcid: PMC7982411
    url: https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2020.582581/full
    source_license: 未確認（取得した本文にライセンス表示なし）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: レビューの記載で、引用元の一次資料は未照合（二次資料経由）。経過中の気胸の頻度は本文内で30〜40%との記載もあり一致しない。クラドリビンの国内での適応は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-3-B-⑦（Langerhans細胞組織球症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を IL-051→IL-058、出典を SRC-538→SRC-561 に振り直した（主張文・数値は変更なし）
- id: IL-059
  domain: IL
  subdomain: アミロイドーシス
  assertion:
    plain_statement_ja: 肺アミロイドーシスは気管気管支型、結節型、びまん性肺胞隔壁型に分けられ、いずれも AL 型が多い。気管気管支型と結節型は通常は肺に限局し（結節型は MALT リンパ腫などの低悪性度 B 細胞増殖性疾患と関連することがある）、びまん性肺胞隔壁型は全身性アミロイドーシスの部分症として拘束性換気障害と拡散能低下を起こす。診断は生検組織のコンゴーレッド染色で、偏光下の緑色の複屈折を確認し、治療を選ぶために線維蛋白の種類を同定する。
    condition:
      region: global
      guideline: null
    differential:
    - 気管気管支型は気管後壁などに粘膜下の多発する斑を作って狭窄を起こし、咳嗽・血痰・呼吸困難のため喘息と誤認されやすい
    - AA 型は気管支拡張症や囊胞性線維症などの慢性炎症に関連する
    common_misconception: 肺のアミロイド沈着が見つかれば、全身性アミロイドーシスとして化学療法を行う
  provenance:
    source_ref: SRC-562
    source: Milani P, Basset M, Russo F, et al. The lung in amyloidosis. Eur Respir Rev 2017;26:170046
    doi: 10.1183/16000617.0046-2017
    pmid: null
    pmcid: null
    url: https://www.openaccessrepository.it/record/28159/files/fulltext.pdf
    source_license: CC BY-NC 4.0（© ERS 2017）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-3-B-⑧（アミロイドーシス、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を IL-052→IL-059、出典を SRC-539→SRC-562 に振り直した（主張文・数値は変更なし）
- id: IL-060
  domain: IL
  subdomain: 特発性器質化肺炎<COP>
  assertion:
    plain_statement_ja: 特発性器質化肺炎の33例（2008〜2013年に治療）の後ろ向き検討では、副腎皮質ステロイド治療の後に10例（30.3%）が再燃した。単変量解析では、両側性の陰影、牽引性気管支拡張、ステロイドへの部分寛解が再燃群に多かったが、多変量解析ではいずれも独立した予測因子にならなかった。
    condition:
      region: global
      guideline: null
    differential:
    - 2013年の ATS/ERS 分類では COP を主要な特発性間質性肺炎の亜急性型に含めている（IL-002、SRC-412）
    common_misconception: 特発性器質化肺炎はステロイドによく反応するので、治療後に再燃することはまれである
  provenance:
    source_ref: SRC-563
    source: Saito Z, Kaneko Y, Hasegawa T, et al. Predictive factors for relapse of cryptogenic organizing pneumonia. BMC Pulm Med 2019;19
    doi: 10.1186/s12890-018-0764-8
    pmid: null
    pmcid: PMC6327473
    url: https://doaj.org/article/ca859b396f4341c6b0efa7b045901985
    source_license: 未確認（BMC 誌。取得範囲にライセンス表示なし）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 施設・国は取得範囲で確認していない。初期のステロイド量と減量方法は抄録に記載がない。ライセンスは未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: 医学各論 Ⅳ-4-A-③（特発性器質化肺炎<COP>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を IL-053→IL-060、出典を SRC-540→SRC-563 に振り直した（主張文・数値は変更なし）
- id: IL-061
  domain: IL
  subdomain: 化学薬品、重金属などによる肺障害
  assertion:
    plain_statement_ja: 塩素ガスは組織の水分に触れて塩酸と次亜塩素酸を生じ、気道と肺を傷害する。約0.32 ppmで臭気や刺激を感じ、1〜10 ppmで眼・鼻の刺激、咽頭痛、咳嗽が、15 ppmを超えると急速な呼吸窮迫、気道の収縮、肺水腫が起こり、症状が数時間遅れて出ることもある。特異的な解毒薬はなく、治療は酸素投与や気管支拡張薬の吸入などの支持療法で、反応性気道機能不全症候群（RADS）を残すことがある。
    condition:
      region: US
      guideline: ATSDR Medical Management Guidelines
    differential:
    - 持続する息切れや強い咳嗽、胸部圧迫感のある患者は入院させ、症状が消えるまで観察する
    - 呼吸機能は通常7〜14日でほぼもとに戻る
    common_misconception: 塩素ガスは臭いがするので、臭いを感じなくなれば安全な濃度である
  provenance:
    source_ref: SRC-564
    source: Agency for Toxic Substances and Disease Registry. Medical Management Guidelines for Chlorine（最終確認 2014-10-21、アーカイブ）
    doi: null
    pmid: null
    pmcid: null
    url: https://wwwn.cdc.gov/TSP/MMG/MMGDetails.aspx?mmgid=198&toxid=36
    source_license: 米国連邦政府の著作物（ATSDR）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 2014年10月に最終確認され、以後は更新されないアーカイブ資料。濃度と症状の対応は表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-4-C-②（化学薬品、重金属などによる肺障害、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を IL-054→IL-061、出典を SRC-541→SRC-564 に振り直した（主張文・数値は変更なし）
- id: LC-052
  domain: LC
  subdomain: 気管・気管支腫瘍
  assertion:
    plain_statement_ja: 気管は、年齢、体格、頸部の可動性などにより、約半分まで安全に切除して再建できるとされる。単施設270例の切除成績では、5年生存率が腺様囊胞癌52%、扁平上皮癌39%（10年ではそれぞれ29%、18%）だった。
    condition:
      region: global
      guideline: null
    differential:
    - 脊柱後弯のある高齢者では2 cm程度しか切除できないこともあり、頸部が長く可動性のよい若年者では6 cm以上切除できることがある
    common_misconception: 腺様囊胞癌は進行が緩やかなので、切除しなくても扁平上皮癌より予後がよい
  provenance:
    source_ref: SRC-565
    source: Madariaga MLL, Gaissert HA. Overview of malignant tracheal tumors. Ann Cardiothorac Surg 2018;7(2):244-254
    doi: 10.21037/acs.2018.03.04
    pmid: null
    pmcid: null
    url: https://www.annalscts.com/article/view/16457/html
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 生存率は Gaissert ら（2004年）の単施設研究の数値をレビューから引いたもので、一次資料は未照合（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-6-B-②（気管・気管支腫瘍、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を LC-040→LC-052、出典を SRC-546→SRC-565 に振り直した（主張文・数値は変更なし）
- id: LC-053
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 限局型小細胞肺癌では、エトポシドとシスプラチンに胸部放射線療法を併用する集学的治療が標準で、胸部放射線療法の追加は化学療法単独より絶対生存率を約5%改善する。治療に反応した例への予防的全脳照射は脳転移のリスクを半分以上減らし、メタ解析で3年全生存率を15%から21%に改善した。
    condition:
      region: US
      guideline: NCI PDQ（2025年5月更新）
    differential:
    - 25 Gy/10回を超える予防的全脳照射の線量は、長期生存を改善しなかった
    - 長期生存者では中枢神経機能の障害が多い
    common_misconception: 小細胞肺癌は化学療法がよく効くので、限局型でも胸部放射線療法は不要である
  provenance:
    source_ref: SRC-568
    source: National Cancer Institute. Small Cell Lung Cancer Treatment (PDQ®)–Health Professional Version（最終更新 2025-05-14）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/lung/hp/small-cell-lung-treatment-pdq
    source_license: 米国連邦政府の著作物（NCI）。PDQ の名称で示すには全文掲載が条件
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 予防的全脳照射のメタ解析と各試験の一次資料は未照合（PDQ の記載による）
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を LC-050→LC-053、出典を SRC-555→SRC-568 に振り直した（主張文・数値は変更なし）
- id: LC-054
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: ADRIATIC 試験では、化学放射線療法の後に進行のない限局型小細胞肺癌で、デュルバルマブによる地固め療法（264人）はプラセボ（266人）より全生存期間（中央値55.9か月対33.4か月、ハザード比0.73）と無増悪生存期間（16.6か月対9.2か月、ハザード比0.76）を延長した。Grade 3〜4の肺臓炎・放射線肺臓炎は3.1%対2.6%だった。
    condition:
      region: 国際（多施設共同試験）
      guideline: null
    differential:
    - デュルバルマブとトレメリムマブの併用群（200人）も設けられていた
    common_misconception: 限局型小細胞肺癌では、化学放射線療法の後に維持療法を行っても生存は延びない
  provenance:
    source_ref: SRC-569
    source: Cheng Y, Spigel DR, Cho BC, et al. Durvalumab after Chemoradiotherapy in Limited-Stage Small-Cell Lung Cancer. N Engl J Med 2024（ADRIATIC）
    doi: 10.1056/NEJMoa2404873
    pmid: null
    pmcid: null
    url: https://avesis.akdeniz.edu.tr/yayin/ccd46a6e-ccae-472a-b444-1947385f556f/durvalumab-after-chemoradiotherapy-in-limited-stage-small-cell-lung-cancer
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: PMDA イミフィンジ点滴静注 審査報告書（2025年8月6日）https://www.pmda.go.jp/drugs/2025/P20251007001/670227000_23000AMX00485_A100_1.pdf
  uncertainty: PMID は未照合。国内ではデュルバルマブの効能に「限局型小細胞肺癌における根治的化学放射線療法後の維持療法」が含まれている（PMDA 審査報告書、2025年8月）
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を LC-052→LC-054、出典を SRC-557→SRC-569 に振り直した（主張文・数値は変更なし）
- id: PL-030
  domain: PL
  subdomain: 横隔神経麻痺
  assertion:
    plain_statement_ja: 一側の横隔膜麻痺は無症状のことが多く胸部エックス線で偶然見つかるが、両側麻痺では起坐呼吸、安静時の呼吸困難、吸気時の腹部の奇異性運動が特徴で、レム睡眠中の低換気も起こる。原因には心臓手術を含む胸部手術、外傷、縦隔腫瘍による圧迫・浸潤、神経痛性筋萎縮症（Parsonage-Turner 症候群）、帯状疱疹、Guillain-Barré 症候群などがあり、特発性もある。透視下の sniff test は一側麻痺の評価に有用だが両側麻痺には向かず、臥位での肺活量の低下（一側で15%超、両側で30%超）も手がかりになる。
    condition:
      region: global
      guideline: null
    differential:
    - 超音波検査では、吸気時に横隔膜が尾側へ動かないことが麻痺を示す
    - 症状のある両側麻痺には非侵襲的換気が用いられる
    common_misconception: 横隔膜麻痺は一側でも必ず強い呼吸困難を起こす
  provenance:
    source_ref: SRC-570
    source: Ricoy J, Rodríguez-Núñez N, Álvarez-Dobaño JM, et al. Diaphragmatic dysfunction. Pulmonology 2019
    doi: null
    pmid: null
    pmcid: null
    url: https://www.journalpulmonology.org/en-diaphragmatic-dysfunction-articulo-S2531043718301624
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 臥位肺活量の閾値は表から読み取り（本文では15〜30%と幅で記載）。DOI とライセンスは未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-246 (id: Jlvnl10)'
    kokushi: 医学各論 Ⅳ-7-C-④（横隔神経麻痺、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
  history:
  - date: '2026-10-28'
    by: claude-code
    change: 第14回の試行（成果物B）から採用。ID を PL-028→PL-030、出典を SRC-559→SRC-570 に振り直した（主張文・数値は変更なし）
```

## 3. 成果物B からの振り直し

| 元の ID | 新しい ID |
|---|---|
| 成果物B RI-054 | RI-056 |
| 成果物B RI-056 | RI-057 |
| 成果物B RO-038 | RO-040 |
| 成果物B RO-040 | RO-041 |
| 成果物B IL-049 | IL-057 |
| 成果物B IL-051 | IL-058 |
| 成果物B IL-052 | IL-059 |
| 成果物B IL-053 | IL-060 |
| 成果物B IL-054 | IL-061 |
| 成果物B LC-040 | LC-052 |
| 成果物B LC-050 | LC-053 |
| 成果物B LC-052 | LC-054 |
| 成果物B PL-028 | PL-030 |

| 元の SRC | 新しい SRC |
|---|---|
| 成果物B SRC-530 | SRC-535 |
| 成果物B SRC-532 | SRC-536 |
| 成果物B SRC-534 | SRC-537 |
| 成果物B SRC-536 | SRC-546 |
| 成果物B SRC-537 | SRC-547 |
| 成果物B SRC-538 | SRC-561 |
| 成果物B SRC-539 | SRC-562 |
| 成果物B SRC-540 | SRC-563 |
| 成果物B SRC-541 | SRC-564 |
| 成果物B SRC-546 | SRC-565 |
| 成果物B SRC-555 | SRC-568 |
| 成果物B SRC-557 | SRC-569 |
| 成果物B SRC-559 | SRC-570 |
