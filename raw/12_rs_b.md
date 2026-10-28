# 第12回 呼吸器（IL・PV）

- 作成日：2026-10-28
- 事実票：79件（IL-001〜IL-048（48件）、PV-001〜PV-031（31件））。欠番なし。全件 `status: draft`、`verifier: null`
- 取り込み：`python scripts/ingest_round.py raw/12_rs_b.md IL,PV`
- 形式：YAML ブロックは1つ、アンカー・マージキー・脚注番号・仮ID・`basis_tag` は使っていません。`schema/fact.schema.json` で全件検証済み（エラー0件）です。
- SRC 番号：SRC-410〜449（第12回の範囲 SRC-410〜469 のうち40件）。
- 範囲：依頼文 docs/tasks/round11_RS.md の第12回。深部静脈血栓症（循環器 VS）、心不全そのもの（循環器 HF）、睡眠時無呼吸は扱っていません。
- 調査環境の制約：この回の作業環境では PubMed・PMC・Crossref・Europe PMC の API とページに直接アクセスできず（プロキシ拒否または reCAPTCHA）、NEJM・AJRCCM・ERJ・Circulation の出版社ページも多くが取得できませんでした。数値は大学リポジトリ等に掲載された抄録・本文で確認したものだけを書いています。識別子は表示で確認できたものだけを書き、確認できなかった PMID・DOI は null です（Phase 3 の API 照合で確定してください）。ライセンスはほとんどが未確認のため `UNKNOWN` にしています。

## 1. 抽出元ホワイトリスト（新規 SRC-410〜449）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 使用カード数 |
|---|---|---|---|---|---|---|---|
| SRC-410 | Raghu G, Remy-Jardin M, Richeldi L, et al. Idiopathic Pulmonary Fibrosis (an Update) and Progressive Pulmonary Fibrosis in Adults: An Official ATS/ERS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med 2022;205:e18-e47 | 10.1164/rccm.202202-0399ST | 35486072 | 未確認 | UNKNOWN | 抄録の要約（QxMD）。DOI は QxMD の URL、PMID は Weill Cornell の書誌 URL で確認。本文未確認 | 4 |
| SRC-411 | Ryerson CJ, Adegunsoye A, Piciucchi S, et al. Update of the International Multidisciplinary Classification of the Interstitial Pneumonias: An ERS/ATS Statement. Eur Respir J 2025;2500158 | 10.1183/13993003.00158-2025 | — | 未確認 | UNKNOWN | ERS の配信ページ（抄録）を WebFetch で確認。本文未確認 | 1 |
| SRC-412 | Travis WD, Costabel U, Hansell DM, et al. An official American Thoracic Society/European Respiratory Society statement: Update of the international multidisciplinary classification of the idiopathic interstitial pneumonias. Am J Respir Crit Care Med 2013;188(6):733-748 | 10.1164/rccm.201308-1483ST | 24032382 | 未確認 | UNKNOWN | Weill Cornell の書誌ページ（抄録・DOI・PMID・PMCID）を WebFetch で確認。頁は未確認 | 1 |
| SRC-413 | Collard HR, Ryerson CJ, Corte TJ, et al. Acute Exacerbation of Idiopathic Pulmonary Fibrosis. An International Working Group Report. Am J Respir Crit Care Med 2016;194(3):265-275 | 10.1164/rccm.201604-0801CI | 27299520 | © American Thoracic Society（リポジトリの表示） | RESTRICTED | Imperial College のリポジトリの書誌ページを WebFetch で確認（DOI・巻頁）。PMID は書誌 URL で確認 | 1 |
| SRC-414 | Richeldi L, du Bois RM, Raghu G, et al. Efficacy and safety of nintedanib in idiopathic pulmonary fibrosis. N Engl J Med 2014;370:2071-2082 | 10.1056/NEJMoa1402584 | — | 未確認 | UNKNOWN | カターニア大学のリポジトリ掲載の本文 PDF（抄録）を WebFetch で確認 | 1 |
| SRC-415 | King TE Jr, Bradford WZ, Castro-Bernardini S, et al. A phase 3 trial of pirfenidone in patients with idiopathic pulmonary fibrosis. N Engl J Med 2014;370(22):2083-2092 | 10.1056/NEJMoa1402582 | — | 未確認 | UNKNOWN | アリゾナ大学の書誌ページ（抄録）を WebFetch で確認 | 1 |
| SRC-416 | Richeldi L, et al. Nerandomilast in Patients with Idiopathic Pulmonary Fibrosis. N Engl J Med 2025;392(22):2193-2202 | 10.1056/NEJMoa2414108 | 40387033 | 未確認 | UNKNOWN | UFG のリポジトリ（抄録）を WebFetch で確認。PMID は Weill Cornell の書誌 URL で確認 | 1 |
| SRC-417 | 医薬品医療機器総合機構. ジャスケイド錠9mg・同錠18mg（ネランドミラスト）審議結果報告書・審査報告書（令和8年4月28日付 審議結果報告書） | — | — | PMDA の公開資料（利用条件の表示は未確認） | GOV_JP | PMDA 公開の PDF を WebFetch で確認 | 1 |
| SRC-418 | Flaherty KR, Wells AU, Cottin V, et al. Nintedanib in Progressive Fibrosing Interstitial Lung Diseases. N Engl J Med 2019;381:1718-1727 | 10.1056/NEJMoa1908681 | — | 未確認 | UNKNOWN | ルーヴァン大学のリポジトリ掲載の本文 PDF（抄録）を WebFetch で確認 | 1 |
| SRC-419 | Distler O, Highland KB, Gahlemann M, et al. Nintedanib for Systemic Sclerosis-Associated Interstitial Lung Disease. N Engl J Med 2019;380(26):2518-2528 | 10.1056/NEJMoa1903076 | — | 未確認 | UNKNOWN | ジェノヴァ大学のリポジトリ掲載の本文 PDF（抄録）を WebFetch で確認 | 1 |
| SRC-420 | Robson JC, Grayson PC, Ponte C, et al. 2022 American College of Rheumatology/European Alliance of Associations for Rheumatology classification criteria for granulomatosis with polyangiitis. Arthritis Rheumatol 2022;74(3):393-399 | 10.1002/art.41986 | — | 未確認 | UNKNOWN | 米国リウマチ学会掲載の基準の PDF を WebFetch で確認 | 1 |
| SRC-421 | Suppiah R, Robson JC, Grayson PC, et al. 2022 American College of Rheumatology/European Alliance of Associations for Rheumatology classification criteria for microscopic polyangiitis | — | — | 未確認 | UNKNOWN | UWE リポジトリ掲載の基準の図を WebFetch で確認。書誌は未確認 | 1 |
| SRC-422 | Grayson PC, Ponte C, Suppiah R, et al. 2022 American College of Rheumatology/European Alliance of Associations for Rheumatology classification criteria for eosinophilic granulomatosis with polyangiitis. Ann Rheum Dis 2022;81:309-314 | 10.1136/annrheumdis-2021-221794 | — | No commercial re-use（BMJ の権利表示） | RESTRICTED | BMJ（Ann Rheum Dis）掲載の本文 PDF を WebFetch で確認 | 1 |
| SRC-423 | Crouser ED, Maier LA, Wilson KC, et al. Diagnosis and Detection of Sarcoidosis. An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med 2020;201(8):e26-e51 | 10.1164/rccm.202002-0251ST | — | CC BY-NC 4.0 | RESTRICTED | eScholarship の書誌ページと本文 PDF を WebFetch で確認 | 6 |
| SRC-424 | Raghu G, Remy-Jardin M, Ryerson CJ, et al. Diagnosis of Hypersensitivity Pneumonitis in Adults. An Official ATS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med 2020 | — | — | 未確認 | UNKNOWN | 日本呼吸器学会サイト掲載の ATS プレスリリースを WebFetch で確認。ガイドライン本文未確認 | 3 |
| SRC-425 | Shorr AF, et al. Acute eosinophilic pneumonia among US military personnel deployed in or near Iraq. JAMA 2004（12月号） | — | 15613668 | 未確認 | UNKNOWN | QxMD の書誌ページ（抄録）を WebFetch で確認 | 1 |
| SRC-426 | Agarwal R, et al（ISHAM-ABPA working group）. Revised ISHAM-ABPA working group clinical practice guidelines for diagnosing, classifying and treating allergic bronchopulmonary aspergillosis/mycoses. Eur Respir J 2024;63(4):2400061 | 10.1183/13993003.00061-2024 | — | 未確認 | UNKNOWN | ERS の掲載ページを WebFetch で確認 | 3 |
| SRC-427 | Kudoh S, Kato H, Nishiwaki Y, et al. Interstitial lung disease in Japanese patients with lung cancer: a cohort and nested case-control study. Am J Respir Crit Care Med 2008;177(12):1348-1357 | 10.1164/rccm.200710-1501OC | — | 未確認 | UNKNOWN | 藤田医科大学の書誌ページ（抄録）を WebFetch で確認 | 2 |
| SRC-428 | Marks LB, Bentzen SM, Deasy JO, et al. Radiation Dose-Volume Effects in the Lung. Int J Radiat Oncol Biol Phys 2010;76(3 Suppl):S70-S76 | 10.1016/j.ijrobp.2009.06.091 | — | 未確認 | UNKNOWN | ワシントン大学の書誌ページ（抄録）を WebFetch で確認 | 1 |
| SRC-429 | じん肺法（昭和35年法律第30号、最終改正 平成30年7月6日） | — | — | 法令（著作権法13条により権利の目的とならない） | GOV_JP | 法令掲載サイト（hourei.net）を WebFetch で確認。e-Gov 未照合 | 2 |
| SRC-430 | 千葉県. 石綿による健康被害の救済に関する法律（石綿健康被害救済制度）の案内ページ | — | — | 千葉県ウェブサイトの利用条件（未確認） | GOV_JP | 千葉県の案内ページを WebFetch で確認 | 1 |
| SRC-431 | Ranieri VM, Rubenfeld GD, Thompson BT, et al（ARDS Definition Task Force）. Acute respiratory distress syndrome: the Berlin Definition. JAMA 2012;307(23):2526-2533 | 10.1001/jama.2012.5669 | 22797452 | 未確認 | UNKNOWN | ミラノ大学のリポジトリ（抄録）を WebFetch で確認 | 2 |
| SRC-432 | Matthay MA, Arabi Y, Arroliga AC, et al. A New Global Definition of Acute Respiratory Distress Syndrome. Am J Respir Crit Care Med 2024;209(1):37-47 | — | — | 未確認 | UNKNOWN | ルワンダ大学のリポジトリの要約を WebFetch で確認 | 1 |
| SRC-433 | The Acute Respiratory Distress Syndrome Network. Ventilation with lower tidal volumes as compared with traditional tidal volumes for acute lung injury and the acute respiratory distress syndrome. N Engl J Med 2000;342(18):1301-1308 | — | 10793162 | 未確認 | UNKNOWN | コーネル大学サイト掲載の本文 PDF を WebFetch で確認。PMID は QxMD の URL で確認 | 1 |
| SRC-434 | Guérin C, Reignier J, Richard JC, et al（PROSEVA Study Group）. Prone positioning in severe acute respiratory distress syndrome. N Engl J Med 2013;368(23):2159-2168 | 10.1056/NEJMoa1214103 | — | 未確認 | UNKNOWN | カザフスタン医科大学サイト掲載の本文 PDF（抄録）を WebFetch で確認 | 1 |
| SRC-435 | Tasaka S, Ohshimo S, Takeuchi M, et al. ARDS Clinical Practice Guideline 2021. J Intensive Care 2022;10(1):32 | 10.1186/s40560-022-00615-6 | — | オープンアクセス、© The Author(s) 2022（ライセンス名は未確認） | UNKNOWN | Springer の掲載ページを WebFetch で確認 | 3 |
| SRC-436 | McCormack FX, et al. Official American Thoracic Society/Japanese Respiratory Society Clinical Practice Guidelines: Lymphangioleiomyomatosis Diagnosis and Management. Am J Respir Crit Care Med 2016（9月15日号） | — | — | 未確認 | UNKNOWN | newswise 掲載の ATS プレスリリースを WebFetch で確認。ガイドライン本文未確認 | 3 |
| SRC-437 | Tazawa R, Ueda T, Abe M, et al. Inhaled GM-CSF for Pulmonary Alveolar Proteinosis. N Engl J Med 2019;381:923-932 | 10.1056/NEJMoa1816216 | — | Copyright © 2019 Massachusetts Medical Society | RESTRICTED | 千葉大学のリポジトリ掲載の本文 PDF を WebFetch で確認 | 1 |
| SRC-438 | サルグマリン吸入用250μg（サルグラモスチム（遺伝子組換え））患者向医薬品ガイド（2024年4月作成）. 医薬品医療機器総合機構 掲載 | — | — | PMDA 掲載資料（利用条件の表示は未確認） | GOV_JP | PMDA 掲載の PDF を WebFetch で確認 | 1 |
| SRC-439 | Rochwerg B, Brochard L, Elliott MW, et al. Official ERS/ATS clinical practice guidelines: noninvasive ventilation for acute respiratory failure. Eur Respir J 2017;50:1602426 | — | 28860265 | Copyright ©ERS 2017 | RESTRICTED | ATS 掲載の本文 PDF を WebFetch で確認。PMID は検索結果の PubMed 表題で確認 | 1 |
| SRC-440 | Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051 | 10.1161/CIR.0000000000001415 | — | 未確認 | UNKNOWN | 第三者サイト掲載の本文 PDF を WebFetch で確認（抽出テキストは第4.4・5.2・6節を含まない）。出版社ページは取得失敗 | 10 |
| SRC-441 | Meyer G, Vicaut E, Danays T, et al（PEITHO Investigators）. Fibrinolysis for patients with intermediate-risk pulmonary embolism. N Engl J Med 2014;370 | 10.1056/NEJMoa1302097 | — | 未確認 | UNKNOWN | ゲッティンゲン大学のリポジトリ（抄録）を WebFetch で確認 | 2 |
| SRC-442 | Pengo V, Lensing AWA, Prins MH, et al. Incidence of Chronic Thromboembolic Pulmonary Hypertension after Pulmonary Embolism. N Engl J Med 2004;350(22):2257-2264 | — | — | 未確認 | UNKNOWN | パドヴァ大学のリポジトリ掲載の本文 PDF を WebFetch で確認 | 2 |
| SRC-443 | Ghofrani HA, D'Armini AM, Grimminger F, et al（CHEST-1 Study Group）. Riociguat for the treatment of chronic thromboembolic pulmonary hypertension. N Engl J Med 2013;369 | — | — | 未確認 | UNKNOWN | CORE の書誌ページ（抄録）を WebFetch で確認 | 1 |
| SRC-444 | Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Respir J 2023;61(1):2200879 | 10.1183/13993003.00879-2022 | 36028254 | Publisher holds Copyright（ERS、リポジトリの表示） | RESTRICTED | ベルン大学のリポジトリで書誌（DOI・PMID・権利表示）を確認。本文は未入手のため、内容は ACC の要約（二次資料）で照合 | 7 |
| SRC-445 | Galiè N, Barberà JA, Frost AE, et al（AMBITION Investigators）. Initial Use of Ambrisentan plus Tadalafil in Pulmonary Arterial Hypertension. N Engl J Med 2015;373(9):834-844 | 10.1056/NEJMoa1413687 | 26308684 | 未確認 | UNKNOWN | グラスゴー大学のリポジトリ（抄録・DOI・PMID）を WebFetch で確認 | 1 |
| SRC-446 | Hoeper MM, Badesch DB, Ghofrani HA, et al（STELLAR Trial Investigators）. Phase 3 Trial of Sotatercept for Treatment of Pulmonary Arterial Hypertension. N Engl J Med 2023;388 | 10.1056/NEJMoa2213558 | 36877098 | 未確認 | UNKNOWN | DZL の書誌ページ（抄録）を WebFetch で確認。PMID は検索結果の PubMed 表題で確認 | 1 |
| SRC-447 | Waxman A, Restrepo-Jaramillo R, Thenappan T, et al. Inhaled Treprostinil in Pulmonary Hypertension Due to Interstitial Lung Disease. N Engl J Med 2021;384(4):325-334 | 10.1056/NEJMoa2008470 | 33440084 | 未確認 | UNKNOWN | ミネソタ大学の書誌ページ（抄録）を WebFetch で確認。PMID は検索結果の PubMed 表題で確認 | 1 |
| SRC-448 | Medical Research Council Working Party. Long term domiciliary oxygen therapy in chronic hypoxic cor pulmonale complicating chronic bronchitis and emphysema. Lancet 1981;317(8222):681-686 | 10.1016/S0140-6736(81)91970-X | — | 未確認 | UNKNOWN | PEDro の書誌ページ（抄録・DOI）を WebFetch で確認 | 2 |
| SRC-449 | Faughnan ME, Mager JJ, Hetts SW, et al. Second International Guidelines for the Diagnosis and Management of Hereditary Hemorrhagic Telangiectasia. Ann Intern Med 2020;173（2020年9月8日 早期公開） | 10.7326/M20-1443 | — | 未確認 | UNKNOWN | HHT ガイドライン公式サイトの補足資料 PDF を WebFetch で確認 | 3 |

legal_basis は、法令の内容を書いた SRC-429・SRC-430 のカードを C、それ以外をすべて B（自作文で事実を記述）にしています。

## 2. 事実票 YAML

```yaml
- id: IL-001
  domain: IL
  subdomain: 特発性間質性肺炎
  assertion:
    plain_statement_ja: 2025年の ERS/ATS による間質性肺炎の国際分類の改訂では、対象を特発性のものから二次性の原因を含む間質性肺炎全体に広げ、急性間質性肺炎を特発性びまん性肺胞傷害、剝離性間質性肺炎を肺胞マクロファージ肺炎と呼び替え、細気管支中心性間質性肺炎を主要な病型に加えた。
    condition:
      region: 国際
      guideline: ERS/ATS 2025 間質性肺炎分類
    differential: null
    common_misconception: 急性間質性肺炎・剝離性間質性肺炎は2025年の改訂後も同じ名称で分類されている
  provenance:
    source_ref: SRC-411
    source: 'Ryerson CJ, Adegunsoye A, Piciucchi S, et al. Update of the International Multidisciplinary Classification of the Interstitial Pneumonias: An ERS/ATS Statement. Eur Respir J 2025;2500158'
    doi: 10.1183/13993003.00158-2025
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（ERS の配信ページ）で確認。本文は未確認。PMID 未確認。出題基準（令和6年版）と国内の教科書的分類は2013年分類にもとづくため、用語の切り替え時期は国内の動向を見て判断する。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-002
  domain: IL
  subdomain: 特発性間質性肺炎
  assertion:
    plain_statement_ja: 2013年の ATS/ERS による特発性間質性肺炎の分類の改訂では、非特異性間質性肺炎の定義を明確にし、IPF と非特異性間質性肺炎の経過が一様でないことを認め、分類しにくい例について実際の経過にもとづく分類を提案し、胸膜肺実質線維弾性症を含む稀な病型の群を設けた。
    condition:
      region: 国際
      guideline: ATS/ERS 2013 IIP 分類
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-412
    source: 'Travis WD, Costabel U, Hansell DM, et al. An official American Thoracic Society/European Respiratory Society statement: Update of the international multidisciplinary classification of the idiopathic interstitial pneumonias. Am J Respir Crit Care Med 2013;188(6):733-748'
    doi: 10.1164/rccm.201308-1483ST
    pmid: '24032382'
    pmcid: PMC5803655
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（Weill Cornell の書誌ページ）で確認。2025年に ERS/ATS の改訂（SRC-411）が出ており、こちらは旧版。出題基準の病型名（NSIP・COP）との対応のために残す。頁は書誌ページに記載がなく、733-748 は API 照合で確認する。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: 医学各論 Ⅳ-4-A-②（非特異性間質性肺炎<NSIP>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-003
  domain: IL
  subdomain: 特発性肺線維症
  assertion:
    plain_statement_ja: 2022年の ATS/ERS/JRS/ALAT ガイドラインは、IPF の診断において、経気管支肺クライオ生検を、経験のある施設では外科的肺生検に代わりうる方法とする条件付き推奨を示した。
    condition:
      region: 国際
      guideline: ATS/ERS/JRS/ALAT 2022 IPF・PPF GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-410
    source: 'Raghu G, Remy-Jardin M, Richeldi L, et al. Idiopathic Pulmonary Fibrosis (an Update) and Progressive Pulmonary Fibrosis in Adults: An Official ATS/ERS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med 2022;205:e18-e47'
    doi: 10.1164/rccm.202202-0399ST
    pmid: '35486072'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録の要約で確認（本文は未確認）。DOI・PMID は検索結果の URL（qxmd・Weill Cornell）で確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)；TBL-02-06-024 (id: JlAKpic)'
    kokushi: 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-004
  domain: IL
  subdomain: 特発性肺線維症
  assertion:
    plain_statement_ja: 2022年の ATS/ERS/JRS/ALAT ガイドラインは、IPF の治療を目的とした制酸薬の投与と逆流防止手術を、いずれも行わないことを条件付きで推奨した。
    condition:
      region: 国際
      guideline: ATS/ERS/JRS/ALAT 2022 IPF・PPF GL
    differential: null
    common_misconception: 胃食道逆流が IPF を悪化させるので、IPF には制酸薬を投与することが推奨されている
  provenance:
    source_ref: SRC-410
    source: 'Raghu G, Remy-Jardin M, Richeldi L, et al. Idiopathic Pulmonary Fibrosis (an Update) and Progressive Pulmonary Fibrosis in Adults: An Official ATS/ERS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med 2022;205:e18-e47'
    doi: 10.1164/rccm.202202-0399ST
    pmid: '35486072'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録の要約で確認（本文は未確認）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-005
  domain: IL
  subdomain: 進行性肺線維症
  assertion:
    plain_statement_ja: 2022年の ATS/ERS/JRS/ALAT ガイドラインは、進行性肺線維症（PPF）を、IPF 以外の間質性肺疾患で、ほかに説明のつく原因がないまま、過去1年以内に症状の悪化・画像上の進行・肺機能上の進行の3つのうち2つ以上を満たすものと定義した。
    condition:
      region: 国際
      guideline: ATS/ERS/JRS/ALAT 2022 IPF・PPF GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-410
    source: 'Raghu G, Remy-Jardin M, Richeldi L, et al. Idiopathic Pulmonary Fibrosis (an Update) and Progressive Pulmonary Fibrosis in Adults: An Official ATS/ERS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med 2022;205:e18-e47'
    doi: 10.1164/rccm.202202-0399ST
    pmid: '35486072'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録の要約で確認。肺機能上の進行の具体的な閾値（FVC・DLco の低下幅）は本文で確認していないため書いていない。出題基準 Ⅳ に PPF の項目はないため kokushi は null。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)；TBL-01-00-219 (id: Jlvnlyc)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-006
  domain: IL
  subdomain: 進行性肺線維症
  assertion:
    plain_statement_ja: 2022年の ATS/ERS/JRS/ALAT ガイドラインは、進行性肺線維症にニンテダニブを使うことを条件付きで推奨し、ピルフェニドンについては推奨を出さず、さらなる研究を求めた。
    condition:
      region: 国際
      guideline: ATS/ERS/JRS/ALAT 2022 IPF・PPF GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-410
    source: 'Raghu G, Remy-Jardin M, Richeldi L, et al. Idiopathic Pulmonary Fibrosis (an Update) and Progressive Pulmonary Fibrosis in Adults: An Official ATS/ERS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med 2022;205:e18-e47'
    doi: 10.1164/rccm.202202-0399ST
    pmid: '35486072'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録の要約で確認。国内での PPF（進行性線維化を伴う間質性肺疾患）へのニンテダニブの承認時期は添付文書で確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)；TBL-01-00-219 (id: Jlvnlyc)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-007
  domain: IL
  subdomain: 特発性肺線維症
  assertion:
    plain_statement_ja: IPF を対象とした INPULSIS-1・INPULSIS-2 試験（52週）で、ニンテダニブ150 mg 1日2回はプラセボと比べて FVC の年間低下量を小さくした（INPULSIS-1：-114.7 対 -239.9 mL/年、INPULSIS-2：-113.6 対 -207.3 mL/年）。最も多い有害事象は下痢で、ニンテダニブ群の約6割にみられた。
    condition:
      population: IPF
      region: 国際
    differential: null
    common_misconception: 抗線維化薬は IPF の肺機能を改善させる（実際は低下の速さを抑える）
  provenance:
    source_ref: SRC-414
    source: Richeldi L, du Bois RM, Raghu G, et al. Efficacy and safety of nintedanib in idiopathic pulmonary fibrosis. N Engl J Med 2014;370:2071-2082
    doi: 10.1056/NEJMoa1402584
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（リポジトリ掲載の書誌ページまたは本文 PDF）で確認。PMID は本チャットで確認できず null（API 照合で確定する）。下痢の割合はニンテダニブ群で61.5%（INPULSIS-1）と63.2%（INPULSIS-2）、プラセボ群で18.6%と18.3%。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-008
  domain: IL
  subdomain: 特発性肺線維症
  assertion:
    plain_statement_ja: IPF を対象とした ASCEND 試験（52週）で、ピルフェニドンは、FVC の予測値に対する割合が10ポイント以上低下するか死亡した患者の割合を、プラセボと比べて相対的に47.9%減らした。消化器症状と皮膚の有害事象はピルフェニドン群で多かったが、中止に至ることは少なかった。
    condition:
      population: IPF
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-415
    source: King TE Jr, Bradford WZ, Castro-Bernardini S, et al. A phase 3 trial of pirfenidone in patients with idiopathic pulmonary fibrosis. N Engl J Med 2014;370(22):2083-2092
    doi: 10.1056/NEJMoa1402582
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（リポジトリ掲載の書誌ページまたは本文 PDF）で確認。PMID は本チャットで確認できず null（API 照合で確定する）。国内でのピルフェニドンの承認状況は添付文書で確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-009
  domain: IL
  subdomain: 特発性肺線維症
  assertion:
    plain_statement_ja: IPF を対象とした FIBRONEER-IPF 試験（52週）で、PDE4B 阻害薬のネランドミラストは FVC の低下をプラセボより小さくした（調整平均の変化：18 mg 1日2回 -114.7 mL、9 mg 1日2回 -138.6 mL、プラセボ -183.5 mL）。登録時に77.7%がニンテダニブかピルフェニドンを併用していた。
    condition:
      population: IPF
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-416
    source: Richeldi L, et al. Nerandomilast in Patients with Idiopathic Pulmonary Fibrosis. N Engl J Med 2025;392(22):2193-2202
    doi: 10.1056/NEJMoa2414108
    pmid: '40387033'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（UFG のリポジトリ）で確認。PMID は検索結果の URL（Weill Cornell）で確認。下痢は18 mg 群41.3%、9 mg 群31.1%、プラセボ群16.0%。抗線維化薬の併用の有無による効果の差は抄録では確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-010
  domain: IL
  subdomain: 特発性肺線維症
  assertion:
    plain_statement_ja: ネランドミラスト（販売名ジャスケイド）は、2026年に国内で特発性肺線維症と進行性肺線維症を効能として審議され、承認して差し支えないとされた。通常は成人に1回18 mg を1日2回経口投与し、忍容性に応じて1回9 mg に減量できる。
    condition:
      region: 日本
      guideline: 国内承認（PMDA 審議結果報告書）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-417
    source: 医薬品医療機器総合機構. ジャスケイド錠9mg・同錠18mg（ネランドミラスト）審議結果報告書・審査報告書（令和8年4月28日付 審議結果報告書）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/drugs/2026/P20260605001/530353000_30800AMX00131_A100_1.pdf
    source_license: PMDA の公開資料（利用条件の表示は未確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: PMDA 公開の審議結果報告書で確認（令和8年4月27日の医薬品第二部会、4月28日付の報告書）。承認日と薬価収載日は文書に明記がなく、添付文書で確認する。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)；TBL-01-00-219 (id: Jlvnlyc)'
    kokushi: 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-011
  domain: IL
  subdomain: 特発性肺線維症
  assertion:
    plain_statement_ja: IPF の急性増悪は、従来は原因を特定できない急性で臨床的に重大な呼吸状態の悪化と定義されていたが、2016年の国際作業部会は定義と診断基準の改訂案を示した。
    condition:
      region: 国際
      guideline: 国際作業部会 2016
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-413
    source: Collard HR, Ryerson CJ, Corte TJ, et al. Acute Exacerbation of Idiopathic Pulmonary Fibrosis. An International Working Group Report. Am J Respir Crit Care Med 2016;194(3):265-275
    doi: 10.1164/rccm.201604-0801CI
    pmid: '27299520'
    pmcid: null
    url: null
    source_license: © American Thoracic Society（リポジトリの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: リポジトリ（Imperial College）の書誌ページで確認。改訂後の定義の具体的な条件（期間、新たな両側の陰影、心不全・体液過剰の除外、誘因の有無による分類）は本文で確認していないため書いていない。補完回で本文を確認してカードを追加する。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-012
  domain: IL
  subdomain: 進行性肺線維症
  assertion:
    plain_statement_ja: INBUILD 試験は、HRCT で肺の10%超に線維化を伴い、過去24か月以内に治療にもかかわらず進行した IPF 以外の間質性肺疾患を対象とした。52週の FVC の年間低下量はニンテダニブ群 -80.8 mL/年、プラセボ群 -187.8 mL/年で、差は107.0 mL/年であった。
    condition:
      population: 進行性の線維化を伴う間質性肺疾患（IPF 以外）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-418
    source: Flaherty KR, Wells AU, Cottin V, et al. Nintedanib in Progressive Fibrosing Interstitial Lung Diseases. N Engl J Med 2019;381:1718-1727
    doi: 10.1056/NEJMoa1908681
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（リポジトリ掲載の書誌ページまたは本文 PDF）で確認。PMID は本チャットで確認できず null（API 照合で確定する）。UIP 様の画像所見をもつ群でも差は同様（-82.9 対 -211.1 mL/年）。下痢はニンテダニブ群66.9%、プラセボ群23.9%。出題基準 Ⅳ に PPF の項目はないため kokushi は null。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)；TBL-01-00-219 (id: Jlvnlyc)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-013
  domain: IL
  subdomain: 膠原病および類縁疾患に伴う肺病変
  assertion:
    plain_statement_ja: 全身性強皮症に伴う間質性肺疾患を対象とした SENSCIS 試験（52週）で、ニンテダニブは FVC の年間低下量をプラセボより小さくした（-52.4 対 -93.3 mL/年、差41.0 mL/年）。皮膚硬化（修正 Rodnan スコア）には差がなかった。
    condition:
      population: 全身性強皮症に伴う間質性肺疾患
      region: 国際
    differential: null
    common_misconception: ニンテダニブは強皮症の皮膚硬化も改善させる
  provenance:
    source_ref: SRC-419
    source: Distler O, Highland KB, Gahlemann M, et al. Nintedanib for Systemic Sclerosis-Associated Interstitial Lung Disease. N Engl J Med 2019;380(26):2518-2528
    doi: 10.1056/NEJMoa1903076
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（リポジトリ掲載の書誌ページまたは本文 PDF）で確認。PMID は本チャットで確認できず null（API 照合で確定する）。多重代入による感度分析では P=0.06〜0.10 で、主解析ほど頑健ではない。下痢はニンテダニブ群75.7%、プラセボ群31.6%。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-219 (id: Jlvnlyc)'
    kokushi: 医学各論 Ⅳ-3-B-②（膠原病および類縁疾患に伴う肺病変、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-014
  domain: IL
  subdomain: 多発血管炎性肉芽腫症
  assertion:
    plain_statement_ja: 2022年の ACR/EULAR による多発血管炎性肉芽腫症の分類基準では、小型・中型血管炎と診断し類似疾患を除外したうえで点数を合計し、5点以上で分類する。胸部画像で結節・腫瘤・空洞があれば2点、c-ANCA または PR3-ANCA 陽性は5点、鼻出血・痂皮・副鼻腔のうっ血は3点である。
    condition:
      region: 国際
      guideline: ACR/EULAR 2022 分類基準
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-420
    source: Robson JC, Grayson PC, Ponte C, et al. 2022 American College of Rheumatology/European Alliance of Associations for Rheumatology classification criteria for granulomatosis with polyangiitis. Arthritis Rheumatol 2022;74(3):393-399
    doi: 10.1002/art.41986
    pmid: null
    pmcid: null
    url: https://rheumatology.org/api/asset/bltc07b08f3cb2e6bee
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 表から読み取り（米国リウマチ学会掲載の基準の PDF）。分類基準は研究対象の均質化のためのもので、個々の患者の診断基準ではない。日本の厚生労働省研究班の診断基準とは別物。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-570 (id: JlvnmWg)'
    kokushi: 医学各論 Ⅳ-3-B-④（多発血管炎性肉芽腫症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-015
  domain: IL
  subdomain: 顕微鏡的多発血管炎
  assertion:
    plain_statement_ja: 2022年の ACR/EULAR による顕微鏡的多発血管炎の分類基準では、胸部画像での線維化または間質性肺疾患が3点、p-ANCA または MPO-ANCA 陽性が6点で、合計5点以上で分類する。鼻の症状（-3点）、c-ANCA または PR3-ANCA 陽性（-1点）、好酸球1×10^9/L 以上（-4点）は減点となる。
    condition:
      region: 国際
      guideline: ACR/EULAR 2022 分類基準
    differential: null
    common_misconception: 顕微鏡的多発血管炎の肺病変は肺胞出血だけで、間質性肺炎は伴わない
  provenance:
    source_ref: SRC-421
    source: Suppiah R, Robson JC, Grayson PC, et al. 2022 American College of Rheumatology/European Alliance of Associations for Rheumatology classification criteria for microscopic polyangiitis
    doi: null
    pmid: null
    pmcid: null
    url: https://uwe-repository.worktribe.com/index.php/OutputFile/7438087
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 表から読み取り（UWE リポジトリ掲載の図）。書誌（雑誌名・巻・頁・DOI）は掲載ファイルに記載がなく未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-569 (id: JlvnmWY)；TBL-01-00-219 (id: Jlvnlyc)'
    kokushi: 医学各論 Ⅳ-3-B-③（顕微鏡的多発血管炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-016
  domain: IL
  subdomain: 好酸球性多発血管炎性肉芽腫症
  assertion:
    plain_statement_ja: 2022年の ACR/EULAR による好酸球性多発血管炎性肉芽腫症の分類基準では、血中好酸球の最高値1×10^9/L 以上が5点、閉塞性気道疾患が3点、鼻ポリープが3点などを合計し、6点以上で分類する。c-ANCA または PR3-ANCA 陽性は3点の減点となる。
    condition:
      region: 国際
      guideline: ACR/EULAR 2022 分類基準
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-422
    source: Grayson PC, Ponte C, Suppiah R, et al. 2022 American College of Rheumatology/European Alliance of Associations for Rheumatology classification criteria for eosinophilic granulomatosis with polyangiitis. Ann Rheum Dis 2022;81:309-314
    doi: 10.1136/annrheumdis-2021-221794
    pmid: null
    pmcid: null
    url: null
    source_license: No commercial re-use（BMJ の権利表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 表から読み取り（抄録の重みづけ）。ほかの項目は、好酸球優位の血管外の炎症（+2）、多発単神経炎または運動神経障害（+1）、血尿（-1）。研究のための分類基準で、診断基準ではない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-571 (id: JlvnmWk)'
    kokushi: 医学各論 Ⅳ-3-B-⑤（好酸球性多発血管炎性肉芽腫症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-017
  domain: IL
  subdomain: サルコイドーシス
  assertion:
    plain_statement_ja: ATS の2020年ガイドラインは、サルコイドーシスの診断を、合致する臨床像、1つ以上の組織での壊死を伴わない肉芽腫性炎症、ほかの肉芽腫性疾患の除外、の3点にもとづくとし、客観的な基準がないため診断が完全に確定することはないとした。
    condition:
      region: 米国
      guideline: ATS 2020 サルコイドーシス診断 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-423
    source: Crouser ED, Maier LA, Wilson KC, et al. Diagnosis and Detection of Sarcoidosis. An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med 2020;201(8):e26-e51
    doi: 10.1164/rccm.202002-0251ST
    pmid: null
    pmcid: null
    url: https://escholarship.org/uc/item/35w6v8wz
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本文（eScholarship 掲載の PDF）で確認。日本サルコイドーシス／肉芽腫性疾患学会の診断基準とは照合していない。PMID 未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo)'
    kokushi: 医学各論 Ⅳ-3-B-①（サルコイドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-018
  domain: IL
  subdomain: サルコイドーシス
  assertion:
    plain_statement_ja: ATS の2020年ガイドラインは、Löfgren 症候群・lupus pernio・Heerfordt 症候群のように臨床的にサルコイドーシスの可能性が高い患者ではリンパ節の生検を行わずに経過を慎重にみることを提案し、組織の採取が必要な場合は超音波気管支鏡ガイド下の採取を最初の手技とすることを提案した。
    condition:
      region: 米国
      guideline: ATS 2020 サルコイドーシス診断 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-423
    source: Crouser ED, Maier LA, Wilson KC, et al. Diagnosis and Detection of Sarcoidosis. An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med 2020;201(8):e26-e51
    doi: 10.1164/rccm.202002-0251ST
    pmid: null
    pmcid: null
    url: https://escholarship.org/uc/item/35w6v8wz
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本文で確認。いずれも条件付き推奨・エビデンスの質は非常に低い。無症状の両側肺門リンパ節腫脹では、生検の要否について推奨を出していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo)；TBL-02-06-024 (id: JlAKpic)'
    kokushi: 医学各論 Ⅳ-3-B-①（サルコイドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-019
  domain: IL
  subdomain: サルコイドーシス
  assertion:
    plain_statement_ja: ATS の2020年ガイドラインは、サルコイドーシスの診断時に、症状がなくても血清カルシウムを測定することを強く推奨し、血清クレアチニン・ALP・血算・眼科診察・心電図を行うことを条件付きで提案した。
    condition:
      region: 米国
      guideline: ATS 2020 サルコイドーシス診断 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-423
    source: Crouser ED, Maier LA, Wilson KC, et al. Diagnosis and Detection of Sarcoidosis. An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med 2020;201(8):e26-e51
    doi: 10.1164/rccm.202002-0251ST
    pmid: null
    pmcid: null
    url: https://escholarship.org/uc/item/35w6v8wz
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本文で確認。エビデンスの質はいずれも非常に低い。トランスアミナーゼは推奨なし。ビタミン D を評価する場合は25-OH 体と1,25-OH 体の両方を測ることを提案。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo)'
    kokushi: 医学各論 Ⅳ-3-B-①（サルコイドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-020
  domain: IL
  subdomain: サルコイドーシス
  assertion:
    plain_statement_ja: ATS の2020年ガイドラインは、心症状のないサルコイドーシス患者に心エコーやホルター心電図をルーチンに行わないことを提案し、心病変が疑われる場合は PET や心エコーより心臓 MRI を優先し、MRI が使えない場合に専用のプロトコルによる PET を使うことを提案した。
    condition:
      region: 米国
      guideline: ATS 2020 サルコイドーシス診断 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-423
    source: Crouser ED, Maier LA, Wilson KC, et al. Diagnosis and Detection of Sarcoidosis. An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med 2020;201(8):e26-e51
    doi: 10.1164/rccm.202002-0251ST
    pmid: null
    pmcid: null
    url: https://escholarship.org/uc/item/35w6v8wz
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本文で確認。いずれも条件付き推奨・エビデンスの質は非常に低い。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-3-B-①（サルコイドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-021
  domain: IL
  subdomain: サルコイドーシス
  assertion:
    plain_statement_ja: サルコイドーシスでは、気管支肺胞洗浄液のリンパ球の増加や CD4/CD8 比の上昇は診断を支持する所見とされるが、ATS の2020年ガイドラインはこれを推奨の対象としていない。
    condition:
      region: 米国
      guideline: ATS 2020 サルコイドーシス診断 GL
    differential: null
    common_misconception: BAL の CD4/CD8 比の上昇だけでサルコイドーシスと診断できる
  provenance:
    source_ref: SRC-423
    source: Crouser ED, Maier LA, Wilson KC, et al. Diagnosis and Detection of Sarcoidosis. An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med 2020;201(8):e26-e51
    doi: 10.1164/rccm.202002-0251ST
    pmid: null
    pmcid: null
    url: https://escholarship.org/uc/item/35w6v8wz
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本文で確認（支持的な所見としての記載）。CD4/CD8 比の具体的な閾値は書いていない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo)；TBL-02-06-024 (id: JlAKpic)'
    kokushi: 医学各論 Ⅳ-3-B-①（サルコイドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-022
  domain: IL
  subdomain: サルコイドーシス
  assertion:
    plain_statement_ja: ATS の2020年ガイドラインは、サルコイドーシスで肺高血圧症が疑われる場合はまず心エコーを行い、心エコーで肺高血圧症が示唆されれば右心カテーテル検査を行うことを提案した。
    condition:
      region: 米国
      guideline: ATS 2020 サルコイドーシス診断 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-423
    source: Crouser ED, Maier LA, Wilson KC, et al. Diagnosis and Detection of Sarcoidosis. An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med 2020;201(8):e26-e51
    doi: 10.1164/rccm.202002-0251ST
    pmid: null
    pmcid: null
    url: https://escholarship.org/uc/item/35w6v8wz
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本文で確認。心エコーで示唆されない場合の右心カテーテルは個別に判断する（best practice statement）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-3-B-①（サルコイドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-023
  domain: IL
  subdomain: 過敏性肺炎
  assertion:
    plain_statement_ja: ATS/JRS/ALAT の2020年ガイドラインは、過敏性肺炎を、線維化を伴わない非線維性過敏性肺炎と、線維性過敏性肺炎の2つの臨床型に分けた。
    condition:
      region: 国際
      guideline: ATS/JRS/ALAT 2020 過敏性肺炎診断 GL
    differential: null
    common_misconception: 過敏性肺炎は今も急性・亜急性・慢性の3型で分類される
  provenance:
    source_ref: SRC-424
    source: Raghu G, Remy-Jardin M, Ryerson CJ, et al. Diagnosis of Hypersensitivity Pneumonitis in Adults. An Official ATS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med 2020
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/information/file/HPPracticeGuideline.pdf
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 日本呼吸器学会が掲載した ATS のプレスリリースで確認（ガイドライン本文は未確認）。DOI・PMID 未確認。急性・慢性という従来の分類とは基準が異なる。日本呼吸器学会の過敏性肺炎診療指針とは照合していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-227 (id: Jlvnlzk)'
    kokushi: 医学各論 Ⅳ-3-A-⑤（過敏性肺炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-024
  domain: IL
  subdomain: 過敏性肺炎
  assertion:
    plain_statement_ja: ATS/JRS/ALAT の2020年ガイドラインは、過敏性肺炎の診断で、環境中の曝露源を詳しく聴取することを推奨し、関連抗原に対する血清 IgG の検査を提案し、気管支肺胞洗浄液のリンパ球分画の解析を非線維性では推奨、線維性では提案した。
    condition:
      region: 国際
      guideline: ATS/JRS/ALAT 2020 過敏性肺炎診断 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-424
    source: Raghu G, Remy-Jardin M, Ryerson CJ, et al. Diagnosis of Hypersensitivity Pneumonitis in Adults. An Official ATS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med 2020
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/information/file/HPPracticeGuideline.pdf
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ATS のプレスリリースで確認（本文は未確認）。質問票は現時点では推奨せず、開発と検証を求めている。リンパ球分画の閾値は書いていない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-227 (id: Jlvnlzk)；TBL-02-06-024 (id: JlAKpic)'
    kokushi: 医学各論 Ⅳ-3-A-⑤（過敏性肺炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-025
  domain: IL
  subdomain: 過敏性肺炎
  assertion:
    plain_statement_ja: ATS/JRS/ALAT の2020年ガイドラインは、過敏性肺炎の組織診断として、非線維性では経気管支肺生検を、線維性では経気管支肺クライオ生検を提案し、外科的肺生検はほかの方法を尽くしたあとに提案した。
    condition:
      region: 国際
      guideline: ATS/JRS/ALAT 2020 過敏性肺炎診断 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-424
    source: Raghu G, Remy-Jardin M, Ryerson CJ, et al. Diagnosis of Hypersensitivity Pneumonitis in Adults. An Official ATS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med 2020
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/information/file/HPPracticeGuideline.pdf
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ATS のプレスリリースで確認（本文は未確認）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-227 (id: Jlvnlzk)；TBL-02-06-024 (id: JlAKpic)'
    kokushi: 医学各論 Ⅳ-3-A-⑤（過敏性肺炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-026
  domain: IL
  subdomain: 好酸球性肺炎
  assertion:
    plain_statement_ja: 2003〜2004年にイラク周辺に派遣された米軍兵士約18万3千人のうち18人が急性好酸球性肺炎を発症し（9.1/10万人年）、全員が喫煙者で、78%は喫煙を始めて間もなかった。
    condition:
      population: 米軍派遣兵士
      region: 米国
    differential: null
    common_misconception: 急性好酸球性肺炎は長年の重喫煙者に起こる（実際は喫煙開始直後の発症が多い）
  provenance:
    source_ref: SRC-425
    source: Shorr AF, et al. Acute eosinophilic pneumonia among US military personnel deployed in or near Iraq. JAMA 2004（12月号）
    doi: null
    pmid: '15613668'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（QxMD の書誌ページ）で確認。PMID は同ページで確認、DOI・巻・頁は未確認。気管支肺胞洗浄を受けた6人の好酸球の中央値は40.5%、死亡は2人。急性好酸球性肺炎の診断基準（BAL 好酸球の閾値など）はこの出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-229 (id: Jlvnlzw)'
    kokushi: 医学各論 Ⅳ-3-A-③（好酸球性肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-027
  domain: IL
  subdomain: アレルギー性気管支肺真菌症
  assertion:
    plain_statement_ja: 2024年の ISHAM-ABPA 作業部会の改訂基準では、喘息などの素因がある患者で、アスペルギルス・フミガーツス特異的 IgE 0.35 kUA/L 以上と血清総 IgE 500 IU/mL 以上の両方を必須とし、さらにアスペルギルス特異的 IgG 陽性、血中好酸球500/μL 以上、ABPA に合う胸部 CT 所見（気管支拡張・粘液栓・高吸収粘液）のうち2つを満たせば ABPA と診断する。
    condition:
      region: 国際
      guideline: ISHAM-ABPA 2024
    differential: null
    common_misconception: ABPA の診断には血清総 IgE 1000 IU/mL 以上が必須である（2024年の改訂基準では500）
  provenance:
    source_ref: SRC-426
    source: Agarwal R, et al（ISHAM-ABPA working group）. Revised ISHAM-ABPA working group clinical practice guidelines for diagnosing, classifying and treating allergic bronchopulmonary aspergillosis/mycoses. Eur Respir J 2024;63(4):2400061
    doi: 10.1183/13993003.00061-2024
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 表から読み取り（ERS の掲載ページ）。好酸球数は過去の値でもよいとされる。胸部 X 線の一過性陰影も画像所見として扱う。日本の ABPM 診断基準（Asano ら）とは基準が異なり、照合していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-231 (id: Jlvnlz8)'
    kokushi: 医学各論 Ⅳ-3-A-④（アレルギー性気管支肺真菌症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-028
  domain: IL
  subdomain: アレルギー性気管支肺真菌症
  assertion:
    plain_statement_ja: 2024年の ISHAM-ABPA 作業部会の改訂基準では、CT での高吸収粘液は ABPA に特徴的な所見とされ、ほかの基準を満たさなくても診断を確定できる。
    condition:
      region: 国際
      guideline: ISHAM-ABPA 2024
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-426
    source: Agarwal R, et al（ISHAM-ABPA working group）. Revised ISHAM-ABPA working group clinical practice guidelines for diagnosing, classifying and treating allergic bronchopulmonary aspergillosis/mycoses. Eur Respir J 2024;63(4):2400061
    doi: 10.1183/13993003.00061-2024
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ERS の掲載ページで確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-231 (id: Jlvnlz8)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-3-A-④（アレルギー性気管支肺真菌症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-029
  domain: IL
  subdomain: アレルギー性気管支肺真菌症
  assertion:
    plain_statement_ja: 2024年の ISHAM-ABPA 作業部会は、急性期の ABPA の初期治療として、経口プレドニゾロン（0.5 mg/kg/日を2〜4週、4か月で漸減）か、経口イトラコナゾール4か月のどちらかの単剤を推奨し、全身ステロイドが使えない場合はイトラコナゾールを優先するとした。両者の併用は初期治療としては推奨せず、生物学的製剤も初期治療には推奨しない。
    condition:
      region: 国際
      guideline: ISHAM-ABPA 2024
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-426
    source: Agarwal R, et al（ISHAM-ABPA working group）. Revised ISHAM-ABPA working group clinical practice guidelines for diagnosing, classifying and treating allergic bronchopulmonary aspergillosis/mycoses. Eur Respir J 2024;63(4):2400061
    doi: 10.1183/13993003.00061-2024
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ERS の掲載ページで確認。推奨はデルファイ法による合意（合意率70〜97%）で、GRADE の推奨の強さではない。用量は表から読み取り。併用療法は過去1〜2年に2回以上増悪した場合に推奨。国内での生物学的製剤の ABPA への保険適用は確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-231 (id: Jlvnlz8)'
    kokushi: 医学各論 Ⅳ-3-A-④（アレルギー性気管支肺真菌症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-030
  domain: IL
  subdomain: 薬剤性肺障害
  assertion:
    plain_statement_ja: 日本の非小細胞肺癌患者を対象としたコホート・コホート内症例対照研究で、12週間の間質性肺疾患の累積発症率はゲフィチニブ群4.0%、化学療法群2.1%で、ゲフィチニブの調整オッズ比は3.2であり、危険の上昇は投与開始後4週以内で目立った。
    condition:
      population: 日本の非小細胞肺癌患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-427
    source: 'Kudoh S, Kato H, Nishiwaki Y, et al. Interstitial lung disease in Japanese patients with lung cancer: a cohort and nested case-control study. Am J Respir Crit Care Med 2008;177(12):1348-1357'
    doi: 10.1164/rccm.200710-1501OC
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（藤田医科大学の書誌ページ）で確認。PMID は本チャットで確認できず null（API 照合で確定する）。最初の4週の調整オッズ比は3.8。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-230 (id: Jlvnlz0)'
    kokushi: 医学各論 Ⅳ-4-C-①（薬剤性肺障害、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-031
  domain: IL
  subdomain: 薬剤性肺障害
  assertion:
    plain_statement_ja: 日本の非小細胞肺癌患者の研究では、高齢、全身状態不良、喫煙、診断から間もないこと、CT で正常肺が少ないこと、既存の慢性間質性肺疾患、心疾患の合併が、治療薬の種類にかかわらず間質性肺疾患の発症と関連した。発症した患者の約3割が間質性肺疾患で死亡した。
    condition:
      population: 日本の非小細胞肺癌患者
      region: 日本
    differential: null
    common_misconception: 既存の間質性肺炎は抗癌薬による肺障害の危険因子にならない
  provenance:
    source_ref: SRC-427
    source: 'Kudoh S, Kato H, Nishiwaki Y, et al. Interstitial lung disease in Japanese patients with lung cancer: a cohort and nested case-control study. Am J Respir Crit Care Med 2008;177(12):1348-1357'
    doi: 10.1164/rccm.200710-1501OC
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認。間質性肺疾患による死亡はゲフィチニブ群31.6%、化学療法群27.9%で、両群に有意差はなかった。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-230 (id: Jlvnlz0)'
    kokushi: 医学各論 Ⅳ-4-C-①（薬剤性肺障害、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-032
  domain: IL
  subdomain: 放射線肺炎
  assertion:
    plain_statement_ja: QUANTEC の肺の線量体積効果のレビューによれば、症候性の放射線肺炎の頻度は多くの線量指標と関連するが、明確な耐容線量体積の閾値はなく、照射体積と分割法が危険に大きく影響する。
    condition:
      region: 国際
      guideline: QUANTEC 2010
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-428
    source: Marks LB, Bentzen SM, Deasy JO, et al. Radiation Dose-Volume Effects in the Lung. Int J Radiat Oncol Biol Phys 2010;76(3 Suppl):S70-S76
    doi: 10.1016/j.ijrobp.2009.06.091
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（ワシントン大学の書誌ページ）で確認。V20 や平均肺線量などの具体的な目安は本文で確認していないため書いていない。PMID 未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-223 (id: Jlvnlys)'
    kokushi: 医学各論 Ⅳ-4-C-③（放射線肺炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-033
  domain: IL
  subdomain: じん肺
  assertion:
    plain_statement_ja: じん肺法は、じん肺を、粉じんの吸入によって肺に生じた線維増殖性変化を主体とする疾病と定義している。
    condition:
      region: 日本
      guideline: じん肺法 第2条
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-429
    source: じん肺法（昭和35年法律第30号、最終改正 平成30年7月6日）
    doi: null
    pmid: null
    pmcid: null
    url: https://hourei.net/law/335AC0000000030
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 法令の条文を掲載するサイト（hourei.net）で確認。e-Gov 法令検索での照合は未了。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-220 (id: Jlvnlyw)；TBL-01-00-221 (id: Jlvnly4)'
    kokushi: 医学各論 Ⅳ-4-E-①（珪肺<silicosis>、b）；医学各論 Ⅳ-4-E-②（石綿肺<asbestosis>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-034
  domain: IL
  subdomain: じん肺
  assertion:
    plain_statement_ja: じん肺法では、じん肺健康診断の胸部エックス線写真の像によって第1型から第4型に分け、これに肺機能などを加えて管理一から管理四の管理区分を決める。管理四と決定された者と、合併症にかかっていると認められた者は療養を要する。
    condition:
      region: 日本
      guideline: じん肺法
    differential: null
    common_misconception: じん肺の管理区分は胸部エックス線の型だけで決まる
  provenance:
    source_ref: SRC-429
    source: じん肺法（昭和35年法律第30号、最終改正 平成30年7月6日）
    doi: null
    pmid: null
    pmcid: null
    url: https://hourei.net/law/335AC0000000030
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 法令の条文を掲載するサイトで確認（第3条・第4条・第23条）。各型・各管理区分の具体的な要件と、合併症の種類（施行規則で定める）は条文で確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-220 (id: Jlvnlyw)；TBL-01-00-221 (id: Jlvnly4)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-4-E-①（珪肺<silicosis>、b）；医学各論 Ⅳ-4-E-②（石綿肺<asbestosis>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-035
  domain: IL
  subdomain: 石綿肺
  assertion:
    plain_statement_ja: 石綿健康被害救済制度（石綿による健康被害の救済に関する法律）の対象となる指定疾病は、中皮腫、石綿による肺がん、著しい呼吸機能障害を伴う石綿肺、著しい呼吸機能障害を伴うびまん性胸膜肥厚の4つで、労災保険などの補償を受けられない人とその遺族が対象となる。申請先は環境再生保全機構である。
    condition:
      region: 日本
      guideline: 石綿健康被害救済法
    differential: null
    common_misconception: 石綿肺は労災の対象にならない人には補償がない
  provenance:
    source_ref: SRC-430
    source: 千葉県. 石綿による健康被害の救済に関する法律（石綿健康被害救済制度）の案内ページ
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pref.chiba.lg.jp/kenzu/gan/asbesto/kyuusai.html
    source_license: 千葉県ウェブサイトの利用条件（未確認）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 千葉県の案内ページで確認。法律本文（e-Gov）と環境再生保全機構のページでの照合は未了。給付額は改定されるため書いていない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-221 (id: Jlvnly4)'
    kokushi: 医学各論 Ⅳ-4-E-②（石綿肺<asbestosis>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-036
  domain: IL
  subdomain: 急性呼吸窮迫症候群<ARDS>
  assertion:
    plain_statement_ja: ARDS のベルリン定義（2012年）は、低酸素血症の程度により、PaO2/FIO2 が200超〜300以下を軽症、100超〜200以下を中等症、100以下を重症に分け、死亡率はそれぞれ27%、32%、45%であった。
    condition:
      region: 国際
      guideline: ベルリン定義 2012
    differential: null
    common_misconception: ARDS の重症度は胸部 X 線の陰影の範囲で決める
  provenance:
    source_ref: SRC-431
    source: 'Ranieri VM, Rubenfeld GD, Thompson BT, et al（ARDS Definition Task Force）. Acute respiratory distress syndrome: the Berlin Definition. JAMA 2012;307(23):2526-2533'
    doi: 10.1001/jama.2012.5669
    pmid: '22797452'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録（ミラノ大学のリポジトリ）で確認。定義の他の要件（発症1週間以内、両側陰影、心不全・体液過剰で説明できないこと、PEEP 5 cmH2O 以上での評価）は抄録に記載がなく、本文で確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)'
    kokushi: 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-037
  domain: IL
  subdomain: 急性呼吸窮迫症候群<ARDS>
  assertion:
    plain_statement_ja: ベルリン定義の死亡予測能（ROC 曲線下面積0.577）は、1994年の AECC 定義（0.536）より統計的に有意に高かったが、改善の幅は小さかった。
    condition:
      region: 国際
      guideline: ベルリン定義 2012
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-431
    source: 'Ranieri VM, Rubenfeld GD, Thompson BT, et al（ARDS Definition Task Force）. Acute respiratory distress syndrome: the Berlin Definition. JAMA 2012;307(23):2526-2533'
    doi: 10.1001/jama.2012.5669
    pmid: '22797452'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認。「改善の幅は小さい」は数値からの評価で、抄録の表現ではない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)'
    kokushi: 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-038
  domain: IL
  subdomain: 急性呼吸窮迫症候群<ARDS>
  assertion:
    plain_statement_ja: 2024年に提案された ARDS の新しい国際定義は、PaO2/FIO2 300以下に加えて SpO2 97%以下での SpO2/FIO2 315以下でも低酸素血症を判定でき、30 L/分以上の高流量鼻カニュラ酸素療法中の患者や挿管していない患者も含め、両側陰影の確認に超音波検査を使えるようにした。
    condition:
      region: 国際
      guideline: 新国際定義 2024
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-432
    source: Matthay MA, Arabi Y, Arroliga AC, et al. A New Global Definition of Acute Respiratory Distress Syndrome. Am J Respir Crit Care Med 2024;209(1):37-47
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ルワンダ大学のリポジトリの要約で確認（本文・抄録の全文は未確認）。DOI・PMID 未確認。資源の限られた地域での適用を想定した変更も含む。日本の ARDS 診療ガイドライン2021はベルリン定義を用いている（SRC-435）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-039
  domain: IL
  subdomain: 急性呼吸窮迫症候群<ARDS>
  assertion:
    plain_statement_ja: ARDS Network の ARMA 試験（2000年）で、予測体重あたり6 mL/kg の低一回換気量（プラトー圧30 cmH2O 以下）は、12 mL/kg（プラトー圧50 cmH2O 以下）と比べて死亡率を下げた（31.0% 対 39.8%）。
    condition:
      population: 急性肺傷害・ARDS
      region: 米国
    differential: null
    common_misconception: ARDS の一回換気量は実体重あたりで設定する（予測体重で設定する）
  provenance:
    source_ref: SRC-433
    source: The Acute Respiratory Distress Syndrome Network. Ventilation with lower tidal volumes as compared with traditional tidal volumes for acute lung injury and the acute respiratory distress syndrome. N Engl J Med 2000;342(18):1301-1308
    doi: null
    pmid: '10793162'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（コーネル大学のサイト）の抄録で確認。PMID は検索結果の URL（QxMD）で確認、DOI 未確認。主要評価項目は「補助呼吸なしで退院する前の死亡」。人工呼吸器を使わない日数も低換気量群で多かった。中間解析4回目で有効中止。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)；TBL-02-06-027 (id: JlAKpio)'
    kokushi: 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-040
  domain: IL
  subdomain: 急性呼吸窮迫症候群<ARDS>
  assertion:
    plain_statement_ja: PROSEVA 試験（2013年）で、PaO2/FIO2 150未満（FIO2 0.6以上、PEEP 5 cmH2O 以上）の重症 ARDS に1回16時間以上の腹臥位療法を早期に行うと、28日死亡率は16.0%（仰臥位32.8%）に下がった。
    condition:
      population: 重症 ARDS
      region: フランス・スペイン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-434
    source: Guérin C, Reignier J, Richard JC, et al（PROSEVA Study Group）. Prone positioning in severe acute respiratory distress syndrome. N Engl J Med 2013;368(23):2159-2168
    doi: 10.1056/NEJMoa1214103
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF の抄録で確認。PMID は本チャットで確認できず null（API 照合で確定する）。90日死亡率も23.6% 対 41.0%で低下。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)；TBL-02-06-027 (id: JlAKpio)'
    kokushi: 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-041
  domain: IL
  subdomain: 急性呼吸窮迫症候群<ARDS>
  assertion:
    plain_statement_ja: 日本の ARDS 診療ガイドライン2021は、成人 ARDS の人工呼吸で一回換気量を4〜8 mL/kg に制限することを推奨した（GRADE 1D）。
    condition:
      region: 日本
      guideline: ARDS 診療ガイドライン2021（日本集中治療医学会・日本呼吸器学会・日本呼吸療法医学会）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-435
    source: Tasaka S, Ohshimo S, Takeuchi M, et al. ARDS Clinical Practice Guideline 2021. J Intensive Care 2022;10(1):32
    doi: 10.1186/s40560-022-00615-6
    pmid: null
    pmcid: null
    url: null
    source_license: オープンアクセス、© The Author(s) 2022（ライセンス名は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: Springer の掲載ページ（英語版）で確認。体重が予測体重かどうかは掲載ページの範囲では確認できていない。PMID は本チャットで確認できず null（API 照合で確定する）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)；TBL-02-06-027 (id: JlAKpio)'
    kokushi: 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-042
  domain: IL
  subdomain: 急性呼吸窮迫症候群<ARDS>
  assertion:
    plain_statement_ja: 日本の ARDS 診療ガイドライン2021は、成人 ARDS に低用量のステロイドを使うことを推奨し（GRADE 1B）、高用量のステロイドは使わないことを提案した（GRADE 2C）。
    condition:
      region: 日本
      guideline: ARDS 診療ガイドライン2021
    differential: null
    common_misconception: ARDS にはステロイドパルス療法が推奨されている
  provenance:
    source_ref: SRC-435
    source: Tasaka S, Ohshimo S, Takeuchi M, et al. ARDS Clinical Practice Guideline 2021. J Intensive Care 2022;10(1):32
    doi: 10.1186/s40560-022-00615-6
    pmid: null
    pmcid: null
    url: null
    source_license: オープンアクセス、© The Author(s) 2022（ライセンス名は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: Springer の掲載ページで確認。低用量・高用量の具体的な用量と投与期間は確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)'
    kokushi: 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-043
  domain: IL
  subdomain: 急性呼吸窮迫症候群<ARDS>
  assertion:
    plain_statement_ja: 日本の ARDS 診療ガイドライン2021は、成人の重症 ARDS に体外式膜型人工肺（ECMO）を導入することを提案し（GRADE 2B）、成人で過度に低い SpO2 を目標とする管理は行わないことを提案した（GRADE 2D）。
    condition:
      region: 日本
      guideline: ARDS 診療ガイドライン2021
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-435
    source: Tasaka S, Ohshimo S, Takeuchi M, et al. ARDS Clinical Practice Guideline 2021. J Intensive Care 2022;10(1):32
    doi: 10.1186/s40560-022-00615-6
    pmid: null
    pmcid: null
    url: null
    source_license: オープンアクセス、© The Author(s) 2022（ライセンス名は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: Springer の掲載ページで確認。目標 SpO2 の具体的な範囲は確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)；TBL-02-06-027 (id: JlAKpio)'
    kokushi: 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-044
  domain: IL
  subdomain: 肺リンパ脈管筋腫症<LAM>
  assertion:
    plain_statement_ja: ATS/JRS の2016年の LAM ガイドラインは、肺機能が異常または低下している LAM 患者に、経過観察ではなくシロリムスによる治療を強く推奨した（エビデンスの質は中等度）。
    condition:
      region: 国際
      guideline: ATS/JRS 2016 LAM GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-436
    source: 'McCormack FX, et al. Official American Thoracic Society/Japanese Respiratory Society Clinical Practice Guidelines: Lymphangioleiomyomatosis Diagnosis and Management. Am J Respir Crit Care Med 2016（9月15日号）'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ATS のプレスリリース（newswise 掲載）で確認。ガイドライン本文・DOI・PMID は未確認。シロリムスの国内承認状況は添付文書で確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-238 (id: Jlvnl0o)'
    kokushi: 医学各論 Ⅳ-4-B-①（肺リンパ脈管筋腫症<LAM>、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-045
  domain: IL
  subdomain: 肺リンパ脈管筋腫症<LAM>
  assertion:
    plain_statement_ja: ATS/JRS の2016年の LAM ガイドラインは、CT で LAM に特徴的な嚢胞があるがほかに診断を確定する所見がない患者では、肺生検を考える前に血清 VEGF-D を測定することを強く推奨した。
    condition:
      region: 国際
      guideline: ATS/JRS 2016 LAM GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-436
    source: 'McCormack FX, et al. Official American Thoracic Society/Japanese Respiratory Society Clinical Practice Guidelines: Lymphangioleiomyomatosis Diagnosis and Management. Am J Respir Crit Care Med 2016（9月15日号）'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ATS のプレスリリースで確認。VEGF-D の診断閾値は確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-238 (id: Jlvnl0o)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-4-B-①（肺リンパ脈管筋腫症<LAM>、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-046
  domain: IL
  subdomain: 肺リンパ脈管筋腫症<LAM>
  assertion:
    plain_statement_ja: ATS/JRS の2016年の LAM ガイドラインは、LAM の治療にドキシサイクリンやホルモン療法を使わないことを提案した（いずれも条件付き）。
    condition:
      region: 国際
      guideline: ATS/JRS 2016 LAM GL
    differential: null
    common_misconception: LAM は女性ホルモンが関与するので、抗エストロゲン療法が推奨される
  provenance:
    source_ref: SRC-436
    source: 'McCormack FX, et al. Official American Thoracic Society/Japanese Respiratory Society Clinical Practice Guidelines: Lymphangioleiomyomatosis Diagnosis and Management. Am J Respir Crit Care Med 2016（9月15日号）'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ATS のプレスリリースで確認。乳び胸水が問題となる例では、侵襲的な処置の前にシロリムスを試すことを提案（条件付き）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-238 (id: Jlvnl0o)'
    kokushi: 医学各論 Ⅳ-4-B-①（肺リンパ脈管筋腫症<LAM>、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-047
  domain: IL
  subdomain: 肺胞蛋白症
  assertion:
    plain_statement_ja: 日本の自己免疫性肺胞蛋白症の患者64人を対象とした PAGE 試験で、サルグラモスチム（GM-CSF）125 μg 1日2回の吸入を7日間行い7日間休む方法を24週続けると、肺胞気-動脈血酸素分圧較差は改善した（-4.50 mmHg 対 プラセボ +0.17 mmHg）。
    condition:
      population: 自己免疫性肺胞蛋白症
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-437
    source: Tazawa R, Ueda T, Abe M, et al. Inhaled GM-CSF for Pulmonary Alveolar Proteinosis. N Engl J Med 2019;381:923-932
    doi: 10.1056/NEJMoa1816216
    pmid: null
    pmcid: null
    url: null
    source_license: Copyright © 2019 Massachusetts Medical Society
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本文 PDF（千葉大学のリポジトリ）の抄録で確認。PMID は本チャットで確認できず null（API 照合で確定する）。DLco・CT の肺野濃度も改善したが、肺活量・CAT スコア・6分間歩行距離には差がなく、著者は臨床的な利益は認めなかったとしている。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-239 (id: Jlvnl0s)'
    kokushi: 医学各論 Ⅳ-4-F-②（肺胞蛋白症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: IL-048
  domain: IL
  subdomain: 肺胞蛋白症
  assertion:
    plain_statement_ja: サルグラモスチム（販売名サルグマリン吸入用250 μg）は自己免疫性肺胞蛋白症の治療薬で、成人は1回125 μg を1日2回、ネブライザーで7日間吸入して7日間休む方法を1クールとして繰り返す。
    condition:
      region: 日本
      guideline: 国内承認（添付文書・患者向医薬品ガイド）
    differential: null
    common_misconception: 自己免疫性肺胞蛋白症の治療は全肺洗浄しかない
  provenance:
    source_ref: SRC-438
    source: サルグマリン吸入用250μg（サルグラモスチム（遺伝子組換え））患者向医薬品ガイド（2024年4月作成）. 医薬品医療機器総合機構 掲載
    doi: null
    pmid: null
    pmcid: null
    url: https://www.info.pmda.go.jp/downfiles/ph/GUI/620095_2290706G1023_1_00G.pdf
    source_license: PMDA 掲載資料（利用条件の表示は未確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: PMDA 掲載の患者向医薬品ガイド（2024年4月作成）で確認。承認日は文書に記載がない（発売は2024年7月との報道あり）。超音波式（メッシュ式を除く）以外のネブライザーを使う。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-239 (id: Jlvnl0s)'
    kokushi: 医学各論 Ⅳ-4-F-②（肺胞蛋白症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-001
  domain: PV
  subdomain: 心原性肺水腫
  assertion:
    plain_statement_ja: ERS/ATS の2017年の非侵襲的換気ガイドラインは、心原性肺水腫による急性呼吸不全に、バイレベル NIV または CPAP のいずれかを使うことを強く推奨した（エビデンスの確実性は中等度）。心原性ショックと急性冠症候群の患者はこの推奨の対象外である。
    condition:
      region: 国際
      guideline: ERS/ATS 2017 NIV GL
    differential: null
    common_misconception: 心原性肺水腫に NPPV を使うと心拍出量が下がるので禁忌である
  provenance:
    source_ref: SRC-439
    source: 'Rochwerg B, Brochard L, Elliott MW, et al. Official ERS/ATS clinical practice guidelines: noninvasive ventilation for acute respiratory failure. Eur Respir J 2017;50:1602426'
    doi: null
    pmid: '28860265'
    pmcid: null
    url: https://member.thoracic.org/statements/resources/cc/niv-guidelines.pdf
    source_license: Copyright ©ERS 2017
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ATS 掲載の本文 PDF で確認。PMID は検索結果の PubMed 表題で確認、DOI 未確認。de novo の低酸素性呼吸不全については推奨を出していない。
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-02-06-027 (id: JlAKpio)'
    kokushi: 医学各論 Ⅳ-5-A-①（心原性肺水腫、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-002
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2026年の AHA/ACC ほかの急性肺血栓塞栓症ガイドラインは、従来の「広範型」「亜広範型」に代えて、A（無症状・偶発的）、B（症状があり臨床重症度スコアが低い）、C（臨床重症度スコアが高い）、D（心肺不全の初期）、E（心肺不全）の5つの臨床分類を導入した。
    condition:
      region: 米国
      guideline: AHA/ACC ほか 2026 急性肺血栓塞栓症 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-440
    source: Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051
    doi: 10.1161/CIR.0000000000001415
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（第三者サイト掲載）の抽出テキストで確認。COR/LOE は抽出テキストどおり。米国のガイドラインで、日本の JCS/JPCPHS 2025 ガイドライン（DOI 10.1253/circj.CJ-25-1144）とは照合していない。ESC の2019年ガイドラインの後継版の有無は確認していない。表から読み取り。呼吸状態の異常が目立つ場合は R を付ける（例：C1R）。C1〜C3 の細分の基準は抽出テキストで確認できていない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-003
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2026年の AHA/ACC ほかのガイドラインでは、症状があり臨床重症度スコアが低い（PESI I〜II、sPESI 0、Hestia 0 など）カテゴリー B の急性肺血栓塞栓症は一般に早期退院が可能とし、カテゴリー C・D・E は入院とした。無症状のカテゴリー A は救急外来から帰宅できるとした。
    condition:
      region: 米国
      guideline: AHA/ACC ほか 2026 急性肺血栓塞栓症 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-440
    source: Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051
    doi: 10.1161/CIR.0000000000001415
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（第三者サイト掲載）の抽出テキストで確認。COR/LOE は抽出テキストどおり。米国のガイドラインで、日本の JCS/JPCPHS 2025 ガイドライン（DOI 10.1253/circj.CJ-25-1144）とは照合していない。ESC の2019年ガイドラインの後継版の有無は確認していない。要点（Top 10 Take-Home Messages）から読み取り。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-004
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2026年の AHA/ACC ほかのガイドラインでは、カテゴリー E1（持続する低血圧）には血栓溶解などの高度治療が妥当とされ、カテゴリー D1〜D2（正常血圧のショックなど心肺不全の初期）では考慮してよいとされた。肺塞栓症対応チーム（PERT）の設置も推奨された。
    condition:
      region: 米国
      guideline: AHA/ACC ほか 2026 急性肺血栓塞栓症 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-440
    source: Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051
    doi: 10.1161/CIR.0000000000001415
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（第三者サイト掲載）の抽出テキストで確認。COR/LOE は抽出テキストどおり。米国のガイドラインで、日本の JCS/JPCPHS 2025 ガイドライン（DOI 10.1253/circj.CJ-25-1144）とは照合していない。ESC の2019年ガイドラインの後継版の有無は確認していない。要点から読み取り。全身血栓溶解・カテーテル治療の個別の COR/LOE は抽出テキストに含まれず未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-005
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2026年の AHA/ACC ほかのガイドラインは、肺血栓塞栓症の検査前確率を問診と身体診察で評価することを推奨し（COR 1、LOE A）、確率が高い（50%超）か D ダイマーが上昇している場合に画像検査を行うことを推奨した（COR 1、LOE A）。
    condition:
      region: 米国
      guideline: AHA/ACC ほか 2026 急性肺血栓塞栓症 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-440
    source: Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051
    doi: 10.1161/CIR.0000000000001415
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（第三者サイト掲載）の抽出テキストで確認。COR/LOE は抽出テキストどおり。米国のガイドラインで、日本の JCS/JPCPHS 2025 ガイドライン（DOI 10.1253/circj.CJ-25-1144）とは照合していない。ESC の2019年ガイドラインの後継版の有無は確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-006
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2026年の AHA/ACC ほかのガイドラインでは、検査前確率が低〜中等度（50%未満）の患者で、年齢調整 D ダイマー（年齢×10 μg/L FEU）が閾値未満であれば肺血栓塞栓症を除外することが妥当とされた（COR 2a、LOE B-R）。YEARS アルゴリズムで画像検査が不要な患者を見分けることも考慮してよいとされた（COR 2b）。
    condition:
      region: 米国
      guideline: AHA/ACC ほか 2026 急性肺血栓塞栓症 GL
    differential: null
    common_misconception: D ダイマーの基準値は年齢にかかわらず一律である
  provenance:
    source_ref: SRC-440
    source: Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051
    doi: 10.1161/CIR.0000000000001415
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（第三者サイト掲載）の抽出テキストで確認。COR/LOE は抽出テキストどおり。米国のガイドラインで、日本の JCS/JPCPHS 2025 ガイドライン（DOI 10.1253/circj.CJ-25-1144）とは照合していない。ESC の2019年ガイドラインの後継版の有無は確認していない。妊娠中は妊娠用に調整した YEARS 基準が考慮されうる（COR 2b）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-007
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2026年の AHA/ACC ほかのガイドラインは、急性肺血栓塞栓症の確定には換気血流シンチグラフィより CT 肺動脈造影を推奨し（COR 1、LOE B-R）、CT 肺動脈造影の陽性か換気血流シンチグラフィの高確率所見があれば診断に十分とした（COR 1、LOE A）。造影剤が使えない場合は造影 MRA より換気血流シンチグラフィが妥当とした（COR 2b）。
    condition:
      region: 米国
      guideline: AHA/ACC ほか 2026 急性肺血栓塞栓症 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-440
    source: Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051
    doi: 10.1161/CIR.0000000000001415
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（第三者サイト掲載）の抽出テキストで確認。COR/LOE は抽出テキストどおり。米国のガイドラインで、日本の JCS/JPCPHS 2025 ガイドライン（DOI 10.1253/circj.CJ-25-1144）とは照合していない。ESC の2019年ガイドラインの後継版の有無は確認していない。妊娠中は低線量 CT 肺動脈造影を低線量の肺血流シンチグラフィより優先することが妥当（COR 2a）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-008
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2026年の AHA/ACC ほかのガイドラインは、肺血栓塞栓症の診断を確定または否定する目的で心エコーを使うことは推奨しない（COR 3：利益なし）とした。
    condition:
      region: 米国
      guideline: AHA/ACC ほか 2026 急性肺血栓塞栓症 GL
    differential: null
    common_misconception: 心エコーで右室拡大がなければ肺血栓塞栓症は否定できる
  provenance:
    source_ref: SRC-440
    source: Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051
    doi: 10.1161/CIR.0000000000001415
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（第三者サイト掲載）の抽出テキストで確認。COR/LOE は抽出テキストどおり。米国のガイドラインで、日本の JCS/JPCPHS 2025 ガイドライン（DOI 10.1253/circj.CJ-25-1144）とは照合していない。ESC の2019年ガイドラインの後継版の有無は確認していない。心エコーは重症度（右室機能）の評価には使われる。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-009
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2026年の AHA/ACC ほかのガイドラインは、急性肺血栓塞栓症の初期の非経口抗凝固薬として未分画ヘパリンより低分子ヘパリンを、経口抗凝固薬としてはワルファリンなどのビタミン K 拮抗薬より直接経口抗凝固薬を推奨した。
    condition:
      region: 米国
      guideline: AHA/ACC ほか 2026 急性肺血栓塞栓症 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-440
    source: Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051
    doi: 10.1161/CIR.0000000000001415
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（第三者サイト掲載）の抽出テキストで確認。COR/LOE は抽出テキストどおり。米国のガイドラインで、日本の JCS/JPCPHS 2025 ガイドライン（DOI 10.1253/circj.CJ-25-1144）とは照合していない。ESC の2019年ガイドラインの後継版の有無は確認していない。要点から読み取り。個別の COR/LOE は抽出テキストで未確認。国内の抗凝固薬の保険適用は JCS/JPCPHS 2025 ガイドラインと添付文書で確認する必要がある。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-010
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2026年の AHA/ACC ほかのガイドラインは、大きな可逆的危険因子のない初回の肺血栓塞栓症や、危険因子が持続する場合には、抗凝固療法を3〜6か月で終えずに継続することとした。
    condition:
      region: 米国
      guideline: AHA/ACC ほか 2026 急性肺血栓塞栓症 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-440
    source: Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051
    doi: 10.1161/CIR.0000000000001415
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（第三者サイト掲載）の抽出テキストで確認。COR/LOE は抽出テキストどおり。米国のガイドラインで、日本の JCS/JPCPHS 2025 ガイドライン（DOI 10.1253/circj.CJ-25-1144）とは照合していない。ESC の2019年ガイドラインの後継版の有無は確認していない。要点から読み取り。COR/LOE と、可逆的な危険因子がある場合の期間は抽出テキストで未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-011
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: PEITHO 試験で、右室機能障害とトロポニン陽性を伴う正常血圧の中間リスク肺血栓塞栓症にテネクテプラーゼを加えると、7日以内の死亡または血行動態の破綻は減った（2.6% 対 5.6%）が、30日死亡率には差がなかった（2.4% 対 3.2%）。
    condition:
      population: 中間リスクの急性肺血栓塞栓症
      region: 欧州
    differential: null
    common_misconception: 中間リスクの肺血栓塞栓症には全例に全身血栓溶解療法を行う
  provenance:
    source_ref: SRC-441
    source: Meyer G, Vicaut E, Danays T, et al（PEITHO Investigators）. Fibrinolysis for patients with intermediate-risk pulmonary embolism. N Engl J Med 2014;370
    doi: 10.1056/NEJMoa1302097
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: リポジトリ（ゲッティンゲン大学）の抄録で確認。PMID は本チャットで確認できず null（API 照合で確定する）。頁は未確認。テネクテプラーゼの国内承認状況は確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-012
  domain: PV
  subdomain: 急性肺血栓塞栓症
  assertion:
    plain_statement_ja: PEITHO 試験で、テネクテプラーゼ群は頭蓋外出血（6.3% 対 1.2%）と脳卒中（2.4% 対 0.2%、多くは出血性）が多かった。
    condition:
      population: 中間リスクの急性肺血栓塞栓症
      region: 欧州
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-441
    source: Meyer G, Vicaut E, Danays T, et al（PEITHO Investigators）. Fibrinolysis for patients with intermediate-risk pulmonary embolism. N Engl J Med 2014;370
    doi: 10.1056/NEJMoa1302097
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: リポジトリの抄録で確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)'
    kokushi: 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-013
  domain: PV
  subdomain: 慢性肺血栓塞栓症
  assertion:
    plain_statement_ja: 急性肺血栓塞栓症の患者を追跡した前向き研究で、症候性の慢性血栓塞栓性肺高血圧症の累積発生率は6か月で1.0%、1年で3.1%、2年で3.8%で、2年以降の発生はなかった。
    condition:
      population: 急性肺血栓塞栓症の既往
      region: イタリア
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-442
    source: Pengo V, Lensing AWA, Prins MH, et al. Incidence of Chronic Thromboembolic Pulmonary Hypertension after Pulmonary Embolism. N Engl J Med 2004;350(22):2257-2264
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: パドヴァ大学のリポジトリ掲載の本文 PDF の抄録で確認。DOI・PMID 未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-014
  domain: PV
  subdomain: 慢性肺血栓塞栓症
  assertion:
    plain_statement_ja: 急性肺血栓塞栓症後の慢性血栓塞栓性肺高血圧症の発生には、肺血栓塞栓症の既往、特発性の肺血栓塞栓症、血流欠損が大きいこと、若い年齢が関連した。
    condition:
      population: 急性肺血栓塞栓症の既往
      region: イタリア
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-442
    source: Pengo V, Lensing AWA, Prins MH, et al. Incidence of Chronic Thromboembolic Pulmonary Hypertension after Pulmonary Embolism. N Engl J Med 2004;350(22):2257-2264
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認（多変量解析のオッズ比：既往19.0、特発性5.70、血流欠損1十分位あたり2.22、年齢10歳若いごとに1.79）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-015
  domain: PV
  subdomain: 慢性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2026年の AHA/ACC ほかのガイドラインは、肺血栓塞栓症の患者には少なくとも1年間、受診のたびに症状と機能の制限を尋ね、慢性血栓塞栓性肺疾患を見逃さないようにすることとした。
    condition:
      region: 米国
      guideline: AHA/ACC ほか 2026 急性肺血栓塞栓症 GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-440
    source: Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for the Evaluation and Management of Acute Pulmonary Embolism in Adults. Circulation 2026;153:e977-e1051
    doi: 10.1161/CIR.0000000000001415
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文 PDF（第三者サイト掲載）の抽出テキストで確認。COR/LOE は抽出テキストどおり。米国のガイドラインで、日本の JCS/JPCPHS 2025 ガイドライン（DOI 10.1253/circj.CJ-25-1144）とは照合していない。ESC の2019年ガイドラインの後継版の有無は確認していない。要点から読み取り。COR/LOE は未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-016
  domain: PV
  subdomain: 慢性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2022年の ESC/ERS ガイドラインは、3か月以上の抗凝固療法後も症状があり、換気血流のミスマッチと慢性の器質化血栓の所見がある状態を、肺高血圧の有無にかかわらず慢性血栓塞栓性肺疾患（CTEPD）という概念で扱った。
    condition:
      region: 国際
      guideline: ESC/ERS 2022 PH GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-444
    source: Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Respir J 2023;61(1):2200879
    doi: 10.1183/13993003.00879-2022
    pmid: '36028254'
    pmcid: null
    url: null
    source_license: Publisher holds Copyright（ERS、リポジトリの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 二次資料経由（ACC の要約「Ten Points to Remember」で確認。ガイドライン本文は未入手）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-017
  domain: PV
  subdomain: 慢性肺血栓塞栓症
  assertion:
    plain_statement_ja: 2022年の ESC/ERS ガイドラインでは、慢性血栓塞栓性肺高血圧症の治療は手術（肺動脈血栓内膜摘除術）、肺高血圧症治療薬、バルーン肺動脈形成術を組み合わせて行い、抗凝固療法は生涯続ける。
    condition:
      region: 国際
      guideline: ESC/ERS 2022 PH GL
    differential: null
    common_misconception: 慢性血栓塞栓性肺高血圧症では血栓内膜摘除術が成功すれば抗凝固療法を中止できる
  provenance:
    source_ref: SRC-444
    source: Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Respir J 2023;61(1):2200879
    doi: 10.1183/13993003.00879-2022
    pmid: '36028254'
    pmcid: null
    url: null
    source_license: Publisher holds Copyright（ERS、リポジトリの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 二次資料経由（ACC の要約で確認）。各治療の推奨クラス・レベルは本文で確認していない。日本の JCS/JPCPHS 2025 ガイドラインとは照合していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-018
  domain: PV
  subdomain: 慢性肺血栓塞栓症
  assertion:
    plain_statement_ja: 手術不能の慢性血栓塞栓性肺高血圧症、または肺動脈血栓内膜摘除術後も残存・再発した肺高血圧症の患者261人を対象とした CHEST-1 試験で、可溶性グアニル酸シクラーゼ刺激薬リオシグアトは16週の6分間歩行距離をプラセボより46 m 延ばし、肺血管抵抗を下げた。
    condition:
      population: 手術不能または術後残存の CTEPH
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-443
    source: Ghofrani HA, D'Armini AM, Grimminger F, et al（CHEST-1 Study Group）. Riociguat for the treatment of chronic thromboembolic pulmonary hypertension. N Engl J Med 2013;369
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: CORE の書誌ページの抄録で確認。DOI は表示が途中で切れており未確認、PMID・頁も未確認。国内承認状況は添付文書で確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-019
  domain: PV
  subdomain: 肺高血圧症
  assertion:
    plain_statement_ja: 2022年の ESC/ERS ガイドラインは、肺高血圧症を安静時の平均肺動脈圧20 mmHg 超と定義し、肺動脈性肺高血圧症ではさらに肺血管抵抗2 WU 超と肺動脈楔入圧15 mmHg 以下を満たすこととした。
    condition:
      region: 国際
      guideline: ESC/ERS 2022 PH GL
    differential: null
    common_misconception: 肺高血圧症は平均肺動脈圧25 mmHg 以上で定義される（2022年版で20 mmHg 超に変更）
  provenance:
    source_ref: SRC-444
    source: Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Respir J 2023;61(1):2200879
    doi: 10.1183/13993003.00879-2022
    pmid: '36028254'
    pmcid: null
    url: null
    source_license: Publisher holds Copyright（ERS、リポジトリの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 二次資料経由（ACC の要約で確認。ガイドライン本文は未入手）。旧版の基準（平均肺動脈圧25 mmHg 以上）からの変更点は本文で確認していない。日本の JCS/JPCPHS 2025 ガイドラインとは照合していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-C-②（肺動脈性肺高血圧症<特発性、遺伝性、続発性>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-020
  domain: PV
  subdomain: 肺高血圧症
  assertion:
    plain_statement_ja: 左心系疾患に伴う肺高血圧症は臨床分類の第2群にあたり、肺動脈楔入圧の上昇を伴う毛細血管後性の肺高血圧症である。
    condition:
      region: 国際
      guideline: ESC/ERS 2022 PH GL
    differential: null
    common_misconception: 左心不全に伴う肺高血圧症にも肺動脈性肺高血圧症の治療薬が勧められる
  provenance:
    source_ref: SRC-444
    source: Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Respir J 2023;61(1):2200879
    doi: 10.1183/13993003.00879-2022
    pmid: '36028254'
    pmcid: null
    url: null
    source_license: Publisher holds Copyright（ERS、リポジトリの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ESC/ERS 2022 ガイドライン本文は未入手で、二次資料（ACC の要約）にも第2群の血行動態の記載はない。毛細血管後性の肺高血圧の楔入圧・肺血管抵抗の閾値（孤立性・混合性の区別）は本文で確認してからカードを追加する。心不全そのものの内容は循環器 HF で扱う。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-C-①（左心系疾患に伴う肺高血圧症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-021
  domain: PV
  subdomain: 肺動脈性肺高血圧症
  assertion:
    plain_statement_ja: 治療歴のない WHO 機能分類 II〜III 度の肺動脈性肺高血圧症500人を対象とした AMBITION 試験で、アンブリセンタンとタダラフィルの初期併用は、各単剤（合算）と比べて臨床的失敗の発生を半減させた（18% 対 31%、ハザード比0.50）。
    condition:
      population: 治療歴のない PAH（WHO 機能分類 II〜III）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-445
    source: Galiè N, Barberà JA, Frost AE, et al（AMBITION Investigators）. Initial Use of Ambrisentan plus Tadalafil in Pulmonary Arterial Hypertension. N Engl J Med 2015;373(9):834-844
    doi: 10.1056/NEJMoa1413687
    pmid: '26308684'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: グラスゴー大学のリポジトリの抄録で確認。併用群では末梢浮腫・頭痛・鼻閉・貧血が多かった。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-C-②（肺動脈性肺高血圧症<特発性、遺伝性、続発性>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-022
  domain: PV
  subdomain: 肺動脈性肺高血圧症
  assertion:
    plain_statement_ja: 2022年の ESC/ERS ガイドラインでは、肺動脈性肺高血圧症の治療は、リスク評価・併存症・治療目標にもとづいて進め、初期からの併用療法と経過観察時の治療強化が標準とされた。
    condition:
      region: 国際
      guideline: ESC/ERS 2022 PH GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-444
    source: Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Respir J 2023;61(1):2200879
    doi: 10.1183/13993003.00879-2022
    pmid: '36028254'
    pmcid: null
    url: null
    source_license: Publisher holds Copyright（ERS、リポジトリの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 二次資料経由（ACC の要約で確認）。初期併用の対象（低〜中リスクで心肺の併存症がない場合など）と推奨クラスは本文で確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-C-②（肺動脈性肺高血圧症<特発性、遺伝性、続発性>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-023
  domain: PV
  subdomain: 肺動脈性肺高血圧症
  assertion:
    plain_statement_ja: 既存の治療を続けている WHO 機能分類 II〜III 度の肺動脈性肺高血圧症を対象とした STELLAR 試験で、アクチビンシグナル阻害薬ソタテルセプトの3週ごとの皮下注射は、24週の6分間歩行距離をプラセボより延ばした（差の推定値40.8 m）。
    condition:
      population: 既存治療中の PAH（WHO 機能分類 II〜III）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-446
    source: Hoeper MM, Badesch DB, Ghofrani HA, et al（STELLAR Trial Investigators）. Phase 3 Trial of Sotatercept for Treatment of Pulmonary Arterial Hypertension. N Engl J Med 2023;388
    doi: 10.1056/NEJMoa2213558
    pmid: '36877098'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: リポジトリ（DZL）の抄録で確認。鼻出血・めまい・毛細血管拡張・ヘモグロビン増加・血小板減少・血圧上昇が多かった。国内では2025年6月に承認（販売名エアウィン）との報道があるが、添付文書で確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-C-②（肺動脈性肺高血圧症<特発性、遺伝性、続発性>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-024
  domain: PV
  subdomain: 肺動脈性肺高血圧症
  assertion:
    plain_statement_ja: 2022年の ESC/ERS ガイドラインでは、肺高血圧症の妊婦は多職種のそろった肺高血圧症センターで管理し、エンドセリン受容体拮抗薬・リオシグアト・セレキシパグは中止するとされた。
    condition:
      region: 国際
      guideline: ESC/ERS 2022 PH GL
    differential: null
    common_misconception: 肺動脈性肺高血圧症の妊婦にもエンドセリン受容体拮抗薬は継続してよい
  provenance:
    source_ref: SRC-444
    source: Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Respir J 2023;61(1):2200879
    doi: 10.1183/13993003.00879-2022
    pmid: '36028254'
    pmcid: null
    url: null
    source_license: Publisher holds Copyright（ERS、リポジトリの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 二次資料経由（ACC の要約で確認）。カルシウム拮抗薬・PDE5 阻害薬・プロスタサイクリン製剤はエビデンスは限られるが安全と考えられている。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-C-②（肺動脈性肺高血圧症<特発性、遺伝性、続発性>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-025
  domain: PV
  subdomain: 肺疾患あるいは低酸素血症に続発する肺高血圧症
  assertion:
    plain_statement_ja: 右心カテーテルで確認した間質性肺疾患に伴う肺高血圧症326人を対象とした INCREASE 試験で、トレプロスチニル吸入は16週の6分間歩行距離をプラセボより31.12 m 延ばし、臨床的な悪化を減らした（22.7% 対 33.1%）。
    condition:
      population: 間質性肺疾患に伴う肺高血圧症
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-447
    source: Waxman A, Restrepo-Jaramillo R, Thenappan T, et al. Inhaled Treprostinil in Pulmonary Hypertension Due to Interstitial Lung Disease. N Engl J Med 2021;384(4):325-334
    doi: 10.1056/NEJMoa2008470
    pmid: '33440084'
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ミネソタ大学の書誌ページの抄録で確認。国内でのトレプロスチニル吸入製剤の承認状況は確認していない。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: 医学各論 Ⅳ-5-C-③（肺疾患あるいは低酸素血症に続発する肺高血圧症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-026
  domain: PV
  subdomain: 肺疾患あるいは低酸素血症に続発する肺高血圧症
  assertion:
    plain_statement_ja: 2022年の ESC/ERS ガイドラインは、肺疾患に伴う肺高血圧症（第3群）に初めて薬物療法の推奨を設けた。治療はまず肺疾患の最適化から始め、重症の間質性肺疾患に伴う肺高血圧症では、肺高血圧症センターで個別に判断したうえで PDE5 阻害薬を考慮してよいとした。
    condition:
      region: 国際
      guideline: ESC/ERS 2022 PH GL
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-444
    source: Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Respir J 2023;61(1):2200879
    doi: 10.1183/13993003.00879-2022
    pmid: '36028254'
    pmcid: null
    url: null
    source_license: Publisher holds Copyright（ERS、リポジトリの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 二次資料経由（ACC の要約で確認）。根拠は間質性肺疾患での1つの陽性 RCT とされる（SRC-447 の INCREASE 試験と考えられるが、本文で確認していない）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
    kokushi: 医学各論 Ⅳ-5-C-③（肺疾患あるいは低酸素血症に続発する肺高血圧症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-027
  domain: PV
  subdomain: 肺性心
  assertion:
    plain_statement_ja: 英国 MRC の試験（1981年）で、慢性気管支炎・肺気腫による慢性の低酸素性肺性心（高度の低酸素血症と CO2 貯留、うっ血性心不全の既往）の70歳未満の患者87人に、1日15時間以上の在宅酸素療法を行うと、5年間の死亡は42人中19人で、対照の45人中30人より少なかった。
    condition:
      population: COPD に伴う慢性の低酸素性肺性心
      region: 英国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-448
    source: Medical Research Council Working Party. Long term domiciliary oxygen therapy in chronic hypoxic cor pulmonale complicating chronic bronchitis and emphysema. Lancet 1981;317(8222):681-686
    doi: 10.1016/S0140-6736(81)91970-X
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: PEDro の書誌ページの抄録で確認。PMID 未確認。酸素は通常、鼻カニュラで2 L/分。男性では効果が現れるまで約500日を要した。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-224 (id: Jlvnly8)；TBL-02-06-026 (id: JlAKpik)'
    kokushi: 医学各論 Ⅳ-5-D（肺性心、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-028
  domain: PV
  subdomain: 肺性心
  assertion:
    plain_statement_ja: 英国 MRC の在宅酸素療法の試験では、死亡は動脈血 CO2 分圧と赤血球量を組み合わせた指標で一部予測され、酸素療法は呼吸不全の増悪による入院日数や就労には影響しなかった。
    condition:
      population: COPD に伴う慢性の低酸素性肺性心
      region: 英国
    differential: null
    common_misconception: 在宅酸素療法は COPD の増悪による入院を減らすために行う
  provenance:
    source_ref: SRC-448
    source: Medical Research Council Working Party. Long term domiciliary oxygen therapy in chronic hypoxic cor pulmonale complicating chronic bronchitis and emphysema. Lancet 1981;317(8222):681-686
    doi: 10.1016/S0140-6736(81)91970-X
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-224 (id: Jlvnly8)；TBL-02-06-026 (id: JlAKpik)'
    kokushi: 医学各論 Ⅳ-5-D（肺性心、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-029
  domain: PV
  subdomain: 肺動静脈瘻
  assertion:
    plain_statement_ja: 2020年の第2版国際 HHT ガイドラインは、遺伝性出血性毛細血管拡張症（HHT）の、またはその可能性がある無症状の小児に、診断時に胸部 X 線とパルスオキシメトリ、または経胸壁コントラスト心エコーで肺動静脈奇形のスクリーニングを行うことを強く推奨した。CT はスクリーニングには勧めないが、スクリーニング陽性の場合の確認検査とされる。
    condition:
      population: HHT の小児
      region: 国際
      guideline: 第2版国際 HHT GL 2020
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-449
    source: Faughnan ME, Mager JJ, Hetts SW, et al. Second International Guidelines for the Diagnosis and Management of Hereditary Hemorrhagic Telangiectasia. Ann Intern Med 2020;173（2020年9月8日 早期公開）
    doi: 10.7326/M20-1443
    pmid: null
    pmcid: null
    url: https://hhtguidelines.org/wp-content/uploads/2020/09/Second-International-HHT-GL-Supp1-Annals-2020-1.pdf
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: HHT ガイドライン公式サイトの補足資料（小児・妊娠の章）で確認。成人のスクリーニングの推奨は本文の該当部分で確認していない。PMID・頁未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-5-E（肺動静脈瘻、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-030
  domain: PV
  subdomain: 肺動静脈瘻
  assertion:
    plain_statement_ja: 2020年の第2版国際 HHT ガイドラインは、小児の大きな肺動静脈奇形や酸素飽和度の低下を伴うものを治療して重い合併症を防ぐことを強く推奨し、流入動脈の径が3 mm 以上のものは塞栓術の対象とした。
    condition:
      population: HHT の小児
      region: 国際
      guideline: 第2版国際 HHT GL 2020
    differential: null
    common_misconception: 肺動静脈瘻は低酸素血症がなければ治療しない
  provenance:
    source_ref: SRC-449
    source: Faughnan ME, Mager JJ, Hetts SW, et al. Second International Guidelines for the Diagnosis and Management of Hereditary Hemorrhagic Telangiectasia. Ann Intern Med 2020;173（2020年9月8日 早期公開）
    doi: 10.7326/M20-1443
    pmid: null
    pmcid: null
    url: https://hhtguidelines.org/wp-content/uploads/2020/09/Second-International-HHT-GL-Supp1-Annals-2020-1.pdf
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 補足資料で確認。無症状の小児では通常5年ごとにスクリーニングを繰り返す（強い推奨）。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-5-E（肺動静脈瘻、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PV-031
  domain: PV
  subdomain: 肺動静脈瘻
  assertion:
    plain_statement_ja: 2020年の第2版国際 HHT ガイドラインの補足資料は、無症状の肺動静脈奇形の妊娠中のスクリーニングを妊娠12〜20週に行い、症状のあるものはすぐに塞栓術を行うとし、生理食塩水による経胸壁コントラスト心エコーは妊娠中も安全と考えられるとした。
    condition:
      population: HHT の妊婦
      region: 国際
      guideline: 第2版国際 HHT GL 2020
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-449
    source: Faughnan ME, Mager JJ, Hetts SW, et al. Second International Guidelines for the Diagnosis and Management of Hereditary Hemorrhagic Telangiectasia. Ann Intern Med 2020;173（2020年9月8日 早期公開）
    doi: 10.7326/M20-1443
    pmid: null
    pmcid: null
    url: https://hhtguidelines.org/wp-content/uploads/2020/09/Second-International-HHT-GL-Supp1-Annals-2020-1.pdf
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 補足資料の背景の記述で確認。妊娠に関する推奨本体（合意率・推奨の強さ）は抽出範囲外で未確認。
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-5-E（肺動静脈瘻、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応

| カードID | 出題基準 | コアカリ |
|---|---|---|
| IL-001 | — | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY) |
| IL-002 | 医学各論 Ⅳ-4-A-②（非特異性間質性肺炎<NSIP>、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY) |
| IL-003 | 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)；TBL-02-06-024 (id: JlAKpic) |
| IL-004 | 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY) |
| IL-005 | — | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)；TBL-01-00-219 (id: Jlvnlyc) |
| IL-006 | — | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)；TBL-01-00-219 (id: Jlvnlyc) |
| IL-007 | 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY) |
| IL-008 | 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY) |
| IL-009 | 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY) |
| IL-010 | 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)；TBL-01-00-219 (id: Jlvnlyc) |
| IL-011 | 医学各論 Ⅳ-4-A-①（特発性肺線維症<IPF>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY) |
| IL-012 | — | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)；TBL-01-00-219 (id: Jlvnlyc) |
| IL-013 | 医学各論 Ⅳ-3-B-②（膠原病および類縁疾患に伴う肺病変、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-219 (id: Jlvnlyc) |
| IL-014 | 医学各論 Ⅳ-3-B-④（多発血管炎性肉芽腫症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-570 (id: JlvnmWg) |
| IL-015 | 医学各論 Ⅳ-3-B-③（顕微鏡的多発血管炎、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-569 (id: JlvnmWY)；TBL-01-00-219 (id: Jlvnlyc) |
| IL-016 | 医学各論 Ⅳ-3-B-⑤（好酸球性多発血管炎性肉芽腫症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-571 (id: JlvnmWk) |
| IL-017 | 医学各論 Ⅳ-3-B-①（サルコイドーシス、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo) |
| IL-018 | 医学各論 Ⅳ-3-B-①（サルコイドーシス、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo)；TBL-02-06-024 (id: JlAKpic) |
| IL-019 | 医学各論 Ⅳ-3-B-①（サルコイドーシス、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo) |
| IL-020 | 医学各論 Ⅳ-3-B-①（サルコイドーシス、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo)；TBL-02-06-023 (id: JlAKpiY) |
| IL-021 | 医学各論 Ⅳ-3-B-①（サルコイドーシス、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo)；TBL-02-06-024 (id: JlAKpic) |
| IL-022 | 医学各論 Ⅳ-3-B-①（サルコイドーシス、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-228 (id: Jlvnlzo)；TBL-01-00-226 (id: JlvnlzQ) |
| IL-023 | 医学各論 Ⅳ-3-A-⑤（過敏性肺炎、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-227 (id: Jlvnlzk) |
| IL-024 | 医学各論 Ⅳ-3-A-⑤（過敏性肺炎、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-227 (id: Jlvnlzk)；TBL-02-06-024 (id: JlAKpic) |
| IL-025 | 医学各論 Ⅳ-3-A-⑤（過敏性肺炎、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-227 (id: Jlvnlzk)；TBL-02-06-024 (id: JlAKpic) |
| IL-026 | 医学各論 Ⅳ-3-A-③（好酸球性肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-229 (id: Jlvnlzw) |
| IL-027 | 医学各論 Ⅳ-3-A-④（アレルギー性気管支肺真菌症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-231 (id: Jlvnlz8) |
| IL-028 | 医学各論 Ⅳ-3-A-④（アレルギー性気管支肺真菌症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-231 (id: Jlvnlz8)；TBL-02-06-023 (id: JlAKpiY) |
| IL-029 | 医学各論 Ⅳ-3-A-④（アレルギー性気管支肺真菌症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-231 (id: Jlvnlz8) |
| IL-030 | 医学各論 Ⅳ-4-C-①（薬剤性肺障害、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-230 (id: Jlvnlz0) |
| IL-031 | 医学各論 Ⅳ-4-C-①（薬剤性肺障害、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-230 (id: Jlvnlz0) |
| IL-032 | 医学各論 Ⅳ-4-C-③（放射線肺炎、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-223 (id: Jlvnlys) |
| IL-033 | 医学各論 Ⅳ-4-E-①（珪肺<silicosis>、b）；医学各論 Ⅳ-4-E-②（石綿肺<asbestosis>、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-220 (id: Jlvnlyw)；TBL-01-00-221 (id: Jlvnly4) |
| IL-034 | 医学各論 Ⅳ-4-E-①（珪肺<silicosis>、b）；医学各論 Ⅳ-4-E-②（石綿肺<asbestosis>、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-220 (id: Jlvnlyw)；TBL-01-00-221 (id: Jlvnly4)；TBL-02-06-023 (id: JlAKpiY) |
| IL-035 | 医学各論 Ⅳ-4-E-②（石綿肺<asbestosis>、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-221 (id: Jlvnly4) |
| IL-036 | 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE) |
| IL-037 | 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE) |
| IL-038 | 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)；TBL-02-06-023 (id: JlAKpiY) |
| IL-039 | 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)；TBL-02-06-027 (id: JlAKpio) |
| IL-040 | 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)；TBL-02-06-027 (id: JlAKpio) |
| IL-041 | 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)；TBL-02-06-027 (id: JlAKpio) |
| IL-042 | 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE) |
| IL-043 | 医学各論 Ⅳ-4-D-①（急性呼吸窮迫症候群<ARDS>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-236 (id: JlvnlzE)；TBL-02-06-027 (id: JlAKpio) |
| IL-044 | 医学各論 Ⅳ-4-B-①（肺リンパ脈管筋腫症<LAM>、c） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-238 (id: Jlvnl0o) |
| IL-045 | 医学各論 Ⅳ-4-B-①（肺リンパ脈管筋腫症<LAM>、c） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-238 (id: Jlvnl0o)；TBL-02-06-023 (id: JlAKpiY) |
| IL-046 | 医学各論 Ⅳ-4-B-①（肺リンパ脈管筋腫症<LAM>、c） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-238 (id: Jlvnl0o) |
| IL-047 | 医学各論 Ⅳ-4-F-②（肺胞蛋白症、c） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-239 (id: Jlvnl0s) |
| IL-048 | 医学各論 Ⅳ-4-F-②（肺胞蛋白症、c） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-239 (id: Jlvnl0s) |
| PV-001 | 医学各論 Ⅳ-5-A-①（心原性肺水腫、a） | PS-02-07-04 (id: JkxnuRA)；TBL-02-06-027 (id: JlAKpio) |
| PV-002 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI) |
| PV-003 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI) |
| PV-004 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI) |
| PV-005 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI) |
| PV-006 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI) |
| PV-007 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)；TBL-02-06-023 (id: JlAKpiY) |
| PV-008 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)；TBL-02-06-023 (id: JlAKpiY) |
| PV-009 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI) |
| PV-010 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI) |
| PV-011 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI) |
| PV-012 | 医学各論 Ⅳ-5-B-①（急性肺血栓塞栓症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI) |
| PV-013 | 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-014 | 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-015 | 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-225 (id: JlvnlzI)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-016 | 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-017 | 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-018 | 医学各論 Ⅳ-5-B-②（慢性肺血栓塞栓症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-019 | 医学各論 Ⅳ-5-C-②（肺動脈性肺高血圧症<特発性、遺伝性、続発性>、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-020 | 医学各論 Ⅳ-5-C-①（左心系疾患に伴う肺高血圧症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-021 | 医学各論 Ⅳ-5-C-②（肺動脈性肺高血圧症<特発性、遺伝性、続発性>、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-022 | 医学各論 Ⅳ-5-C-②（肺動脈性肺高血圧症<特発性、遺伝性、続発性>、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-023 | 医学各論 Ⅳ-5-C-②（肺動脈性肺高血圧症<特発性、遺伝性、続発性>、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-024 | 医学各論 Ⅳ-5-C-②（肺動脈性肺高血圧症<特発性、遺伝性、続発性>、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-025 | 医学各論 Ⅳ-5-C-③（肺疾患あるいは低酸素血症に続発する肺高血圧症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)；TBL-01-00-218 (id: JlvnlyY) |
| PV-026 | 医学各論 Ⅳ-5-C-③（肺疾患あるいは低酸素血症に続発する肺高血圧症、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| PV-027 | 医学各論 Ⅳ-5-D（肺性心、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-224 (id: Jlvnly8)；TBL-02-06-026 (id: JlAKpik) |
| PV-028 | 医学各論 Ⅳ-5-D（肺性心、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-224 (id: Jlvnly8)；TBL-02-06-026 (id: JlAKpik) |
| PV-029 | 医学各論 Ⅳ-5-E（肺動静脈瘻、b） | PS-02-07-05 (id: JkxnuRE) |
| PV-030 | 医学各論 Ⅳ-5-E（肺動静脈瘻、b） | PS-02-07-05 (id: JkxnuRE) |
| PV-031 | 医学各論 Ⅳ-5-E（肺動静脈瘻、b） | PS-02-07-05 (id: JkxnuRE) |

## 4. 未解決事項（担当の目安つき）

| # | 内容 | 対象カード | 担当の目安 |
|---|---|---|---|
| 1 | PMID・DOI が null の出典（SRC-411・414・415・418〜422・424〜430・432〜443・448・449 の一部）を API で確定する。SRC-433（ARMA）と SRC-443（CHEST-1）は DOI、SRC-421（MPA 分類基準）は雑誌名・巻・頁・DOI が未確認 | 該当カード全件 | Claude Code（Phase 3：`scripts/ncbi_crossref.py`） |
| 2 | ライセンスの大半が未確認で `UNKNOWN`。Crossref の license 欄で判定し直す。SRC-435（J Intensive Care）は BMC の OA だがライセンス名を確認できていない | 全件 | Claude Code |
| 3 | ESC/ERS 2022 肺高血圧症ガイドライン（SRC-444）の本文に到達できず、内容は ACC の要約（二次資料）で照合した。毛細血管後性肺高血圧（孤立性・混合性）の閾値、運動時肺高血圧、血管反応性試験、リスク層別、各推奨のクラス・レベルは未記載 | PV-016・017・019・020・022・024・026 | 人間（本文を入手して照合）→ 補完回でカード追加 |
| 4 | 日本の最新ガイドライン JCS/JPCPHS 2025「肺高血圧症および肺血栓塞栓症・深部静脈血栓症」（DOI 10.1253/circj.CJ-25-1144、2026年7月2日公開）を入手できず、PV は米国（AHA/ACC 2026）と欧州（ESC/ERS 2022）の出典だけで作った。日本の推奨（抗凝固薬の選択、BPA の位置づけなど）を `region: 日本` で追加する必要がある | PV 全般 | 補完回（調査） |
| 5 | 日本呼吸器学会の診療ガイドライン（IPF 治療、過敏性肺炎、薬剤性肺障害、サルコイドーシスの国内診断基準、ABPM の国内基準）を出典にしたカードがない。英語版（Respir Investig など）の有無と DOI を確認して補う | IL 全般 | 補完回（調査） |
| 6 | 国内承認状況の確認：ニンテダニブ（PPF・SSc-ILD）、ピルフェニドン、ネランドミラストの承認日と薬価収載、シロリムス（LAM）、リオシグアト（CTEPH）、ソタテルセプト（エアウィン、2025年6月承認との報道）、トレプロスチニル吸入、テネクテプラーゼ、サルグラモスチムの承認日 | IL-006・008・010・044・048、PV-018・023・025・011 | Claude Code（PMDA の添付文書で照合）または人間 |
| 7 | 定義の細部が未確認：IPF 急性増悪の2016年改訂定義（IL-011）、PPF の肺機能上の進行の閾値（IL-005）、ベルリン定義の時間・陰影・PEEP の要件（IL-036）、日本の ARDS GL の体重の基準（IL-041）、AHA/ACC の C1〜C3 の細分（PV-002） | 左記 | 補完回（本文の確認） |
| 8 | 2025年の ERS/ATS 間質性肺炎分類の改訂（IL-001）で病型名が変わった（AIP→特発性びまん性肺胞傷害、DIP→肺胞マクロファージ肺炎）。出題基準・教材の用語をどちらに合わせるか | IL-001・002 | 人間（呼吸器専門医） |
| 9 | `subdomain` のうち「進行性肺線維症」（IL-005・006・012）、「じん肺」（IL-033・034）、「特発性間質性肺炎」（IL-001・002）、「肺高血圧症」（PV-019・020）は第6節の表の小項目名ではない。中項目名を原本で確認し、合わなければ置き換える | 左記 | Claude Code（`kokushi_r6_items.yaml` と照合） |
| 10 | PPF（IL-005・006・012）は出題基準 Ⅳ に該当する小項目がなく `kokushi: null`。IL-001 も同じ | 左記 | 人間（配分計算での扱いを決める） |
| 11 | 過敏性肺炎（IL-023〜025）と LAM（IL-044〜046）は、学会・ATS のプレスリリースで内容を確認した。ガイドライン本文での照合が必要 | 左記 | 補完回 |
| 12 | 第三者サイトに掲載された AHA/ACC 2026 の本文 PDF で照合した（SRC-440）。出版社版での再照合が望ましい | PV-002〜010・015 | Claude Code / 人間 |

## 5. 次回への引き継ぎ

### 5-1. 欠番

なし（IL-001〜IL-048、PV-001〜PV-031 はすべて使用）。

### 5-2. カードのない出題基準の小項目（第12回の範囲）

| 番号 | 項目 | レベル | 理由 |
|---|---|---|---|
| Ⅳ-3-B-⑥ | 悪性リンパ腫、白血病（の肺病変） | b | 出典を確認できず。血液（Ⅶ）と重なる |
| Ⅳ-3-B-⑦ | Langerhans細胞組織球症 | c | 出典の抄録に到達できず |
| Ⅳ-3-B-⑧ | アミロイドーシス | c | 未着手 |
| Ⅳ-4-A-③ | 特発性器質化肺炎<COP> | b | 2013年分類（SRC-412）の抄録に COP の記載がなく、カードにできなかった |
| Ⅳ-4-C-② | 化学薬品、重金属などによる肺障害 | b | 未着手 |
| Ⅳ-4-C-④ | 酸素中毒 | c | 未着手 |
| Ⅳ-4-C-⑤ | パラコート中毒 | c | 未着手 |
| Ⅳ-4-F-① | 肺胞微石症 | c | 未着手 |

レベル a の小項目（好酸球性肺炎、サルコイドーシス、IPF、ARDS、心原性肺水腫、急性肺血栓塞栓症、左心系疾患に伴う肺高血圧症、肺性心）にはすべてカードがあります。ただし左心系疾患に伴う肺高血圧症（PV-020）は1件だけで、閾値を含まない内容です。

依頼文の「主な対象」のうち、COP、慢性好酸球性肺炎、珪肺と結核の関係、石綿肺の労災認定基準、肺塞栓症の重症度スコア（PESI・sPESI）の項目内容、血管反応性試験は未作成です。

### 5-3. 重複を避ける範囲（第11回・第13回へ）

- 石綿健康被害救済制度の指定疾病（中皮腫・石綿による肺がんを含む）は IL-035 で作成済み。LC（胸膜中皮腫）では制度の説明を繰り返さない。
- 心原性肺水腫への NIV・CPAP（PV-001、ERS/ATS 2017 NIV GL）は作成済み。RX（NPPV）と RO（COPD 増悪への NIV）では、同じ出典の COPD 増悪への推奨（強い推奨・確実性高）は使ってよいが、心原性肺水腫の推奨は繰り返さない。
- 低酸素性肺性心への在宅酸素療法（MRC 1981、PV-027・028）は作成済み。RO・RX で在宅酸素療法を扱う場合は NOTT など別の出典を使う。
- ARDS の肺保護換気・腹臥位（IL-039〜043）は作成済み。RX（人工呼吸）では繰り返さない。
- 経気管支肺クライオ生検（IL-003・025）と超音波気管支鏡（IL-018）は疾患側で作成済み。RX（気管支鏡）では手技一般に絞る。
- 薬剤性肺障害のうち EGFR-TKI（ゲフィチニブ）の日本のデータ（IL-030・031）は作成済み。LC（分子標的薬）では有害事象としての間質性肺疾患を繰り返さない。

### 5-4. 扱った出典（第12回）

SRC-410〜449 の40件（第1節の表）。登録しなかったが確認した出典：JCS/JPCPHS 2025 Guideline on Pulmonary Hypertension and Pulmonary Embolism/Deep Vein Thrombosis（DOI 10.1253/circj.CJ-25-1144、本文未入手）、ACC「Ten Points to Remember」2022 ESC/ERS PH GL（二次資料。SRC-444 の照合経路としてのみ使用）。
