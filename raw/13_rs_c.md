# 第13回 呼吸器（LC・PL・RX）

- 作成日：2026-10-28
- 事実票：90件（LC-001〜LC-038（38件）、PL-001〜PL-027（27件）、RX-001〜RX-025（25件））。欠番なし。全件 `status: draft`、`verifier: null`
- 取り込み：`python scripts/ingest_round.py raw/13_rs_c.md LC,PL,RX`
- 形式：YAML ブロックは1つ、アンカー・マージキー・脚注番号・仮ID・`basis_tag` は使っていません。`schema/fact.schema.json` で検証済みです（`scripts/ingest_round.py` の検査も通ることを確認）。
- SRC 番号：SRC-470〜SRC-510（第13回の範囲 SRC-470〜529 のうち41件）。SRC-299（令和6年人口動態統計、第10回で登録）を再利用しました。
- 範囲：依頼文 docs/tasks/round11_RS.md の第13回。出題基準 Ⅳ-6〜Ⅳ-8 のレベル a の小項目には、すべて1件以上のカードがあります。
- 調査環境の制約：この回の作業環境では Crossref・PubMed の API とシェルからの通信が使えず、PMC と PubMed のページも途中から読み込みを拒まれました。識別子は出版社ページ・学会掲載 PDF・書誌頁の表示で確認できたものだけを書き、PMID の多くは null です（API 照合で確定してください）。肺癌の薬物療法（KEYNOTE-024、JCOG0802 など）と中皮腫の薬物療法（CheckMate 743）は、本文を取得できず作っていません（第4節）。

## 1. 抽出元ホワイトリスト（新規 SRC-470〜SRC-510、再利用 SRC-299）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 使用カード数 |
|---|---|---|---|---|---|---|---|
| SRC-470 | 国立がん研究センター. プレスリリース「有効性評価に基づく肺がん検診ガイドライン 2025年度版を公開」（2025年4月25日） | — | — | ©National Cancer Center Japan（コンテンツ利用規約は未確認） | GOV_JP | 国立がん研究センターのプレスリリースを WebFetch で確認。ガイドライン本文は未確認 | 4 |
| SRC-471 | 公益財団法人がん研究振興財団. Cancer Statistics in Japan 2025（2025年5月掲載）Table 1 Number of deaths by cancer site (2023) | — | — | 表示なし（掲載頁は (c) 国立研究開発法人国立がん研究センター。元データは人口動態統計） | UNKNOWN | ganjoho.jp 掲載の PDF を WebFetch で確認（死亡数の表のみ。罹患・生存率の表は抽出できず） | 1 |
| SRC-472 | 厚生労働省. がん検診受診率50%達成に向けた集中キャンペーン「がんの統計」（部位別順位） | — | — | Copyright 厚生労働省（運営：がん対策推進企業アクション事務局）。利用規約は未確認 | GOV_JP | サイトを WebFetch で確認（本文の順位の記載のみ。実数はグラフ画像で未確認） | 1 |
| SRC-473 | National Lung Screening Trial Research Team, Aberle DR, Adams AM, et al. Reduced lung-cancer mortality with low-dose computed tomographic screening. N Engl J Med 2011;365:395-409 | — | 21714641 | 未確認 | UNKNOWN | NCI CDAS の書誌頁（抄録）を WebFetch で確認。PMID は同頁の表示 | 2 |
| SRC-474 | Constantinescu A, Căprariu RN, Stoicescu ER, et al. From TNM 8 to TNM 9: Stage Migration and Histology-Specific Patterns in Lung Cancer. Cancers (Basel) 2025;17(20):3290 | 10.3390/cancers17203290 | 41154348 | CC BY 4.0（MDPI） | OPEN | PMC の本文を WebFetch で確認 | 3 |
| SRC-475 | Travis WD, Brambilla E, Noguchi M, et al. International Association for the Study of Lung Cancer/American Thoracic Society/European Respiratory Society International Multidisciplinary Classification of Lung Adenocarcinoma. J Thorac Oncol 2011;6:244-285 | — | — | © 2011 by the International Association for the Study of Lung Cancer | RESTRICTED | ATS サイト掲載の刊行版 PDF を WebFetch で確認 | 3 |
| SRC-476 | Ramalingam SS, Vansteenkiste J, Planchard D, et al. Overall Survival with Osimertinib in Untreated, EGFR-Mutated Advanced NSCLC. N Engl J Med 2020;382:41-50 | 10.1056/NEJMoa1913662 | — | 未確認（機関リポジトリ掲載の刊行版） | UNKNOWN | パルマ大学リポジトリの PDF を WebFetch で確認（抄録と本文） | 1 |
| SRC-477 | Pfannschmidt J, Egerer G, Bischof M, Thomas M, Dienemann H. Surgical Intervention for Pulmonary Metastases. Dtsch Arztebl Int 2012;109(40):645-651 | 10.3238/arztebl.2012.0645 | — | 表示なし | UNKNOWN | Deutsches Ärzteblatt の英語版記事を WebFetch で確認 | 3 |
| SRC-478 | Tavare AN, Cash C. The Clinical Picture: A 78-year-old smoker with an incidental pulmonary mass. Cleve Clin J Med 2014;81(8):477-478 | 10.3949/ccjm.81a.13150 | — | For personal use only. All other uses require permission. | RESTRICTED | CCJM の PDF を WebFetch で確認 | 2 |
| SRC-479 | Carter BW, Benveniste MF, Marom EM. Diagnostic approach to the anterior/prevascular mediastinum for radiologists. Mediastinum 2019;3:18 | 10.21037/med.2018.12.03 | — | CC BY-NC-ND 4.0 | RESTRICTED | AME の本文 HTML を WebFetch で確認 | 4 |
| SRC-480 | PDQ Adult Treatment Editorial Board. Thymoma and Thymic Carcinoma Treatment (PDQ)–Health Professional Version. National Cancer Institute（2024年10月25日更新） | — | — | PDQ の本文は文章として自由に利用できる（PDQ 要約の表示）。図は除く | GOV_US | NCBI Bookshelf 掲載版を WebFetch で確認 | 4 |
| SRC-481 | 厚生労働省. 都道府県（21大都市再掲）別にみた中皮腫による死亡数の年次推移（平成7年〜令和7年）人口動態統計（確定数）より | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 厚生労働省の PDF を WebFetch で確認（全国の令和7年の値のみ） | 1 |
| SRC-482 | 厚生労働省・都道府県労働局・労働基準監督署. 石綿による疾病の労災認定（パンフレット、令和5年9月版） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 東京労働局サイト掲載の PDF を WebFetch で確認 | 2 |
| SRC-483 | 環境省 大臣官房環境保健部 石綿健康被害対策室. 石綿健康被害救済制度の施行状況等について（資料3、令和4年6月6日） | — | — | 政府標準利用規約（第2.0版）に準拠する環境省のコンテンツ（表示は未確認） | GOV_JP | 環境省の PDF を WebFetch で確認 | 1 |
| SRC-484 | PDQ Supportive and Palliative Care Editorial Board. Cardiopulmonary Syndromes (PDQ)–Health Professional Version. National Cancer Institute（2023年2月21日公開版） | — | — | PDQ の本文は文章として自由に利用できる（PDQ 要約の表示。今回の取得範囲では利用条件の頁は未取得） | GOV_US | NCBI Bookshelf 掲載版を WebFetch で確認（約10万字のうち先頭10万字） | 6 |
| SRC-485 | Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156 | 10.1136/thorax-2023-220304 | — | © Author(s) (or their employer(s)) 2023. No commercial re-use. | RESTRICTED | Thorax の刊行版 PDF を WebFetch で確認 | 9 |
| SRC-486 | Hwang JW, Kim Y, Hwang JH, Kim TS, Ro DW, Lee KS. Lymphangitic Carcinomatosis of the Lung: Serial Changes on High-Resolution CT. J Korean Radiol Soc 1997;37(6):1051-1057 | 10.3348/jkrs.1997.37.6.1051 | — | Copyright © The Korean Radiological Society | RESTRICTED | KoreaMed Synapse の書誌・英文抄録を WebFetch で確認 | 2 |
| SRC-487 | Staats BA, et al. The lipoprotein profile of chylous and nonchylous pleural effusions. Mayo Clin Proc 1980;55(11):700-704 | — | 7442324 | 未確認 | UNKNOWN | PubMed の抄録頁を WebFetch で確認（著者名は表示されず。PMID は URL による） | 2 |
| SRC-488 | National Library of Medicine. MeSH Descriptor: Mediastinal Emphysema (D008478) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | NCBI MeSH を WebFetch で確認 | 1 |
| SRC-489 | National Library of Medicine. MeSH Descriptor: Tracheoesophageal Fistula (D014138) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | NCBI MeSH を WebFetch で確認 | 1 |
| SRC-490 | National Library of Medicine. MeSH Descriptor: Vocal Cord Paralysis (D014826) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | NCBI MeSH を WebFetch で確認 | 1 |
| SRC-491 | Kasotakis G, Hasenboehler EA, Streib EW, et al. Operative fixation of rib fractures after blunt trauma: A practice management guideline from the Eastern Association for the Surgery of Trauma. J Trauma Acute Care Surg 2017;82(3):618-626 | — | — | 未確認 | UNKNOWN | EAST の指針頁を WebFetch で確認（題名と第4著者以降は API で確定する） | 2 |
| SRC-492 | National Library of Medicine. MeSH Descriptor: Funnel Chest (D005660) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | NCBI MeSH を WebFetch で確認 | 1 |
| SRC-493 | National Library of Medicine. MeSH Descriptor: Hernia, Diaphragmatic (D006548) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | MeSH Browser を WebFetch で確認 | 1 |
| SRC-494 | National Library of Medicine. MeSH Descriptor: Hemothorax (D006491) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | MeSH Browser を WebFetch で確認 | 1 |
| SRC-495 | 日本呼吸器学会・厚生労働科学研究費補助金難治性疾患政策研究事業「難治性呼吸器疾患・肺高血圧症に関する調査研究」班（監修）. 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020 | — | — | 取得範囲に著作権表示なし（学会の著作物と考えられる） | RESTRICTED | 日本呼吸器学会サイトの PDF を WebFetch で確認 | 5 |
| SRC-496 | 厚生労働省東北厚生局. 保険診療と個別指導（医科）第6回 在宅医療について〜診療報酬算定に当たっての留意事項〜（参考資料、2024年3月22日） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ（表示は未確認） | GOV_JP | 東北厚生局の PDF を WebFetch で確認 | 1 |
| SRC-497 | National Library of Medicine. MeSH Descriptor: Hyperventilation (D006985) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | MeSH Browser を WebFetch で確認 | 1 |
| SRC-498 | Callaham M. Hypoxic hazards of traditional paper bag rebreathing in hyperventilating patients. Ann Emerg Med 1989;18(6):622-628 | 10.1016/s0196-0644(89)80515-3 | 2499228 | 未確認 | UNKNOWN | PubMed の抄録頁を WebFetch で確認 | 1 |
| SRC-499 | National Library of Medicine. MeSH Descriptor: Obesity Hypoventilation Syndrome (D010845) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | NCBI MeSH を WebFetch で確認 | 1 |
| SRC-500 | Karlafti E, Tsavdaris D, Kotzakioulafi E, et al. Which Is the Best Way to Treat Massive Hemoptysis? A Systematic Review and Meta-Analysis of Observational Studies. J Pers Med 2023;13(12):1649 | 10.3390/jpm13121649 | — | CC BY 3.0 | OPEN | MDPI の本文を WebFetch で確認 | 2 |
| SRC-501 | Stanojevic S, Kaminsky DA, Miller MR, et al. ERS/ATS technical standard on interpretive strategies for routine lung function tests. Eur Respir J 2022;60(1):2101499 | 10.1183/13993003.01499-2021 | — | 未確認（頁に PDF Permissions のリンクのみ） | UNKNOWN | ERS の本文 HTML を WebFetch で確認（約11万字のうち先頭10万字）。著者順は API で確定する | 5 |
| SRC-502 | Dweik RA, Boggs PB, Erzurum SC, et al. An official ATS clinical practice guideline: interpretation of exhaled nitric oxide levels (FENO) for clinical applications. Am J Respir Crit Care Med 2011;184:602-615 | — | — | 取得範囲に表示なし | UNKNOWN | ATS サイト掲載の PDF を WebFetch で確認 | 2 |
| SRC-503 | Matsunaga K, Hirano T, Kawayama T, et al. Reference Ranges for Exhaled Nitric Oxide Fraction in Healthy Japanese Adult Population. Allergol Int 2010;59(4):363-367 | 10.2332/allergolint.10-OA-0197 | — | © 2010 by Japanese Society of Allergology（JOURNAL FREE ACCESS） | RESTRICTED | J-STAGE の抄録頁を WebFetch で確認 | 1 |
| SRC-504 | Asano F, Aoe M, Ohsaki Y, et al. Complications associated with endobronchial ultrasound-guided transbronchial needle aspiration: a nationwide survey by the Japan Society for Respiratory Endoscopy. Respir Res 2013;14:50 | 10.1186/1465-9921-14-50 | — | Open Access の表示のみ（CC の版は未確認） | UNKNOWN | Springer Medicine の書誌・抄録頁を WebFetch で確認 | 1 |
| SRC-505 | British Thoracic Society. BTS Guideline for oxygen use in adults in healthcare and emergency settings, Web Appendix 3: Summary of guideline for hospital use（2017年5月）. 本体は O'Driscoll BR, et al. Thorax 2017;72(Suppl 1):i1-i89 | — | — | 取得範囲に表示なし | UNKNOWN | BTS サイトの要約頁を WebFetch で確認 | 1 |
| SRC-506 | 厚生労働省. 平成20年度診療報酬改定 告示・通知（在宅医療：C103 在宅酸素療法指導管理料、C107-2 在宅持続陽圧呼吸療法指導管理料） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 厚生労働省の PDF を WebFetch で確認（資料の正式名は抜粋中に記載なし） | 1 |
| SRC-507 | Rochwerg B, Brochard L, Elliott MW, et al. Official ERS/ATS clinical practice guidelines: noninvasive ventilation for acute respiratory failure. Eur Respir J 2017;50:1602426 | 10.1183/13993003.02426-2016 | — | ©ERS 2017 | RESTRICTED | ATS サイト掲載の刊行版 PDF を WebFetch で確認 | 3 |
| SRC-508 | Rochester CL, Alison JA, Carlin B, et al. Pulmonary Rehabilitation for Adults with Chronic Respiratory Disease: An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med 2023;208(4):e7-e26 | — | — | Copyright © 2023 by the American Thoracic Society | RESTRICTED | ハッセルト大学リポジトリ掲載の刊行版 PDF を WebFetch で確認 | 1 |
| SRC-509 | 厚生労働省. 令和4年国民健康・栄養調査結果の概要（2024年8月28日公表） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 厚生労働省の PDF を WebFetch で確認 | 2 |
| SRC-510 | 厚生労働省. 中央社会保険医療協議会 検-4-2参考「平成28年度診療報酬改定 重症化予防の取組の推進②（ニコチン依存症管理料の対象患者の拡大）」（平成29年11月10日） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 厚生労働省の PDF を WebFetch で確認 | 1 |
| SRC-299 | 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第8表 性別にみた死因順位（第10位まで）別死亡数・死亡率（人口10万対）・構成割合 | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | （再利用）厚生労働省の PDF を WebFetch で再確認 | 2 |

- legal_basis は全件 B（出典の事実・数値を自作文で記述）です。表・図・原文の言い回しは使っていません。
- ライセンスの表示を出版社ページで確認できなかったものは UNKNOWN としました（NEJM・ERJ・AJRCCM・EAST など）。Crossref の license 欄で確定してください。
- 日本呼吸器学会の SAS 診療ガイドライン2020（SRC-495）は、日本語版 PDF で読みました。CC の表示がないため RESTRICTED です。英語版（Sleep Biol Rhythms）は治療の章（CQ16〜36）だけを収載しており、診断基準のカード（PL-019〜021・024）の出典にはできないと判断しました。
- MeSH（SRC-488〜490・492〜494・497・499）は定義文だけのカードです。出典を取れなかったレベル a・b の小項目を空けないために使いました。補完回で、頻度・診断・治療のカードを足してください。
- 国立がん研究センターのページ（SRC-470）は、第2回以降の ganjoho の扱いにならって GOV_JP としました。コンテンツ利用規約の確認が要ります。

## 2. 事実票 YAML

```yaml
- id: LC-001
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 2023年の日本の肺癌（気管・気管支・肺）の死亡数は75,725人（男性52,887人、女性22,838人）で、がん死亡全体の19.8%を占め、部位別の死亡数で最も多かった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 女性のがん死亡で最も多いのは乳癌である
  provenance:
    source_ref: SRC-471
    source: 公益財団法人がん研究振興財団. Cancer Statistics in Japan 2025（2025年5月掲載）Table 1 Number of deaths by cancer site (2023)
    doi: null
    pmid: null
    pmcid: null
    url: https://ganjoho.jp/public/qa_links/report/statistics/pdf/cancer_statistics_2025_data_E.pdf
    source_license: 表示なし（掲載頁は (c) 国立研究開発法人国立がん研究センター。元データは人口動態統計）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 表から読み取り。部位の区分は結腸と直腸を分けた集計で、大腸（結腸と直腸の合計）として集計すると女性の順位は変わりうる。罹患数・5年生存率の表は抽出できず未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-002
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 厚生労働省のがん検診啓発サイトによると、肺がんは2024年のがん死亡数で男女計と男性で1位、女性で2位であり、2021年の罹患数では男女計・男性・女性のいずれも3位である。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 肺がんは罹患数でも死亡数でも1位である
  provenance:
    source_ref: SRC-472
    source: 厚生労働省. がん検診受診率50%達成に向けた集中キャンペーン「がんの統計」（部位別順位）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.gankenshin50.mhlw.go.jp/cancer/statistics.html
    source_license: Copyright 厚生労働省（運営：がん対策推進企業アクション事務局）。利用規約は未確認
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 本文の順位の記載による。実数はグラフ画像にしかなく確認できていない。女性の死亡順位は大腸を一括した集計によるとみられるが、本文で部位の区分は確認できていない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-003
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 国立がん研究センターの「有効性評価に基づく肺がん検診ガイドライン」2025年度版（2006年度版の改訂）は、喫煙指数600以上の重喫煙者に対する低線量CT検診を、50〜74歳を対象に年1回、対策型・任意型の両方で推奨した（推奨グレードA）。喫煙指数は1日の喫煙本数と喫煙年数の積で、禁煙者は禁煙した年数を除き、加熱式たばこはカートリッジの本数で数える。
    condition:
      guideline: 有効性評価に基づく肺がん検診ガイドライン 2025年度版（国立がん研究センター）
      region: 日本
    differential: null
    common_misconception: 低線量CT検診は喫煙歴にかかわらず全員に勧められている
  provenance:
    source_ref: SRC-470
    source: 国立がん研究センター. プレスリリース「有効性評価に基づく肺がん検診ガイドライン 2025年度版を公開」（2025年4月25日）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.ncc.go.jp/jp/information/pr_release/2025/0425/index.html
    source_license: ©National Cancer Center Japan（コンテンツ利用規約は未確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 国立がん研究センターのプレスリリースで確認した推奨の要旨。ガイドライン本文（推奨の根拠、不利益の評価、精度管理の条件）は未確認。厚生労働省の「がん予防重点健康教育及びがん検診実施のための指針」への反映状況は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-004
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 同ガイドライン2025年度版では、重喫煙者以外への低線量CT検診は推奨グレードIとされ、対策型検診としては実施しないことが勧められた。任意型検診では、医療者が利益と不利益を説明したうえで受診者個人の判断に委ねるとされ、国内で進行中の無作為化比較試験の結果を注視するとしている。
    condition:
      guideline: 有効性評価に基づく肺がん検診ガイドライン 2025年度版（国立がん研究センター）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-470
    source: 国立がん研究センター. プレスリリース「有効性評価に基づく肺がん検診ガイドライン 2025年度版を公開」（2025年4月25日）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.ncc.go.jp/jp/information/pr_release/2025/0425/index.html
    source_license: ©National Cancer Center Japan（コンテンツ利用規約は未確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 国立がん研究センターのプレスリリースで確認した推奨の要旨。ガイドライン本文（推奨の根拠、不利益の評価、精度管理の条件）は未確認。厚生労働省の「がん予防重点健康教育及びがん検診実施のための指針」への反映状況は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-005
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 同ガイドライン2025年度版では、胸部エックス線検査による肺がん検診は喫煙状況によらず40〜79歳を対象に年1回、対策型・任意型の両方で推奨された（推奨グレードA）。
    condition:
      guideline: 有効性評価に基づく肺がん検診ガイドライン 2025年度版（国立がん研究センター）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-470
    source: 国立がん研究センター. プレスリリース「有効性評価に基づく肺がん検診ガイドライン 2025年度版を公開」（2025年4月25日）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.ncc.go.jp/jp/information/pr_release/2025/0425/index.html
    source_license: ©National Cancer Center Japan（コンテンツ利用規約は未確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 国立がん研究センターのプレスリリースで確認した推奨の要旨。ガイドライン本文（推奨の根拠、不利益の評価、精度管理の条件）は未確認。厚生労働省の「がん予防重点健康教育及びがん検診実施のための指針」への反映状況は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-006
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 同ガイドライン2025年度版では、重喫煙者に対する喀痰細胞診と胸部エックス線検査の併用は推奨グレードDとされ、対策型・任意型のいずれでも実施しないことが勧められた。従来は50歳以上の重喫煙者に併用されていた。
    condition:
      guideline: 有効性評価に基づく肺がん検診ガイドライン 2025年度版（国立がん研究センター）
      region: 日本
    differential: null
    common_misconception: 重喫煙者の肺がん検診では喀痰細胞診の併用が勧められている
  provenance:
    source_ref: SRC-470
    source: 国立がん研究センター. プレスリリース「有効性評価に基づく肺がん検診ガイドライン 2025年度版を公開」（2025年4月25日）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.ncc.go.jp/jp/information/pr_release/2025/0425/index.html
    source_license: ©National Cancer Center Japan（コンテンツ利用規約は未確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 国立がん研究センターのプレスリリースで確認した推奨の要旨。ガイドライン本文（推奨の根拠、不利益の評価、精度管理の条件）は未確認。厚生労働省の「がん予防重点健康教育及びがん検診実施のための指針」への反映状況は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)；TBL-02-06-019 (id: JlAKpiM)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-007
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 米国の National Lung Screening Trial（NLST）では、高リスク者53,454人を低線量CTと胸部エックス線の検診に無作為に割り付け、低線量CT群で肺癌死亡が相対的に20.0%、全死亡が6.7%減少した。
    condition:
      guideline: null
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-473
    source: National Lung Screening Trial Research Team, Aberle DR, Adams AM, et al. Reduced lung-cancer mortality with low-dose computed tomographic screening. N Engl J Med 2011;365:395-409
    doi: null
    pmid: '21714641'
    pmcid: null
    url: https://cdas.cancer.gov/publications/320/
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認。対象の年齢と喫煙歴の条件は確認した頁に記載がなく、主張文に含めていない。DOI は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-008
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: NLST の3回の検診を通じた陽性の割合は、低線量CTで24.2%、胸部エックス線で6.9%だった。
    condition:
      guideline: null
      region: 米国
    differential: null
    common_misconception: 低線量CTは胸部エックス線より陽性になる割合が低い
  provenance:
    source_ref: SRC-473
    source: National Lung Screening Trial Research Team, Aberle DR, Adams AM, et al. Reduced lung-cancer mortality with low-dose computed tomographic screening. N Engl J Med 2011;365:395-409
    doi: null
    pmid: '21714641'
    pmcid: null
    url: https://cdas.cancer.gov/publications/320/
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認。陽性のうち肺癌だった割合（偽陽性の割合）は確認した頁に記載がなく未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-009
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 肺癌の TNM 分類第9版（2025年1月から適用）では、T因子は変更されず、N2が単一のリンパ節ステーションへの転移（N2a）と複数ステーションへの転移（N2b）に分けられた。N因子は転移したリンパ節の個数ではなくステーションの数で評価する。
    condition:
      guideline: UICC/AJCC TNM 分類 第9版（IASLC 提案）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-474
    source: 'Constantinescu A, Căprariu RN, Stoicescu ER, et al. From TNM 8 to TNM 9: Stage Migration and Histology-Specific Patterns in Lung Cancer. Cancers (Basel) 2025;17(20):3290'
    doi: 10.3390/cancers17203290
    pmid: '41154348'
    pmcid: PMC12564687
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12564687
    source_license: CC BY 4.0（MDPI）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: IASLC の原提案（J Thorac Oncol 2024）ではなく、第9版を解説した原著論文（CC BY）を出典とした。原提案との照合が要る。日本の肺癌取扱い規約の対応版は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-010
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: TNM 分類第9版では、M1c が単一の肺外臓器への多発転移（M1c1）と複数の肺外臓器への多発転移（M1c2）に分けられたが、どちらもⅣB期のままである。
    condition:
      guideline: UICC/AJCC TNM 分類 第9版（IASLC 提案）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-474
    source: 'Constantinescu A, Căprariu RN, Stoicescu ER, et al. From TNM 8 to TNM 9: Stage Migration and Histology-Specific Patterns in Lung Cancer. Cancers (Basel) 2025;17(20):3290'
    doi: 10.3390/cancers17203290
    pmid: '41154348'
    pmcid: PMC12564687
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12564687
    source_license: CC BY 4.0（MDPI）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: IASLC の原提案との照合が要る（LC-009 と同じ）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-011
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: TNM 分類第9版では、第8版と比べて T1N1 がⅡB期からⅡA期に、T1N2a がⅢA期からⅡB期に、T3N2a がⅢB期からⅢA期に下がり、T2N2b はⅢA期からⅢB期に上がった。
    condition:
      guideline: UICC/AJCC TNM 分類 第9版（IASLC 提案）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-474
    source: 'Constantinescu A, Căprariu RN, Stoicescu ER, et al. From TNM 8 to TNM 9: Stage Migration and Histology-Specific Patterns in Lung Cancer. Cancers (Basel) 2025;17(20):3290'
    doi: 10.3390/cancers17203290
    pmid: '41154348'
    pmcid: PMC12564687
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12564687
    source_license: CC BY 4.0（MDPI）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: IASLC の原提案との照合が要る。病期の対応は論文本文の記載（Section 1.3、Figure 8）による
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-012
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 2011年の IASLC/ATS/ERS 肺腺癌分類では、上皮内腺癌（AIS）を3 cm以下の単発で置換性増殖だけからなり間質・脈管・胸膜への浸潤がないもの、微少浸潤性腺癌（MIA）を3 cm以下で置換性増殖が主体かつ浸潤部が最大径5 mm以下のものと定義した。
    condition:
      guideline: IASLC/ATS/ERS 肺腺癌国際多分野分類（2011）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-475
    source: Travis WD, Brambilla E, Noguchi M, et al. International Association for the Study of Lung Cancer/American Thoracic Society/European Respiratory Society International Multidisciplinary Classification of Lung Adenocarcinoma. J Thorac Oncol 2011;6:244-285
    doi: null
    pmid: null
    pmcid: null
    url: https://www.thoracic.org/statements/resources/lcod/adenocarcinoma.pdf
    source_license: © 2011 by the International Association for the Study of Lung Cancer
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2011年の分類。2021年の WHO 分類（第5版）にも AIS・MIA の区分は引き継がれているとされるが、今回 WHO 分類の文献は取得できなかった。DOI は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-013
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 同分類では、完全切除された AIS は疾患特異的生存率100%、MIA はほぼ100%と見込まれるとし、細気管支肺胞上皮癌（BAC）という用語の使用をやめるよう推奨した（強い推奨、低い質のエビデンス）。
    condition:
      guideline: IASLC/ATS/ERS 肺腺癌国際多分野分類（2011）
      region: 国際
    differential: null
    common_misconception: 細気管支肺胞上皮癌（BAC）は現在も正式な組織分類名である
  provenance:
    source_ref: SRC-475
    source: Travis WD, Brambilla E, Noguchi M, et al. International Association for the Study of Lung Cancer/American Thoracic Society/European Respiratory Society International Multidisciplinary Classification of Lung Adenocarcinoma. J Thorac Oncol 2011;6:244-285
    doi: null
    pmid: null
    pmcid: null
    url: https://www.thoracic.org/statements/resources/lcod/adenocarcinoma.pdf
    source_license: © 2011 by the International Association for the Study of Lung Cancer
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2011年の分類。生存率は分類の根拠として示された見込みで、新しい追跡研究との照合は未了
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-014
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 2011年の IASLC/ATS/ERS 肺腺癌分類は、進行肺腺癌の患者に EGFR 遺伝子変異の検査を行うよう推奨した。
    condition:
      guideline: IASLC/ATS/ERS 肺腺癌国際多分野分類（2011）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-475
    source: Travis WD, Brambilla E, Noguchi M, et al. International Association for the Study of Lung Cancer/American Thoracic Society/European Respiratory Society International Multidisciplinary Classification of Lung Adenocarcinoma. J Thorac Oncol 2011;6:244-285
    doi: null
    pmid: null
    pmcid: null
    url: https://www.thoracic.org/statements/resources/lcod/adenocarcinoma.pdf
    source_license: © 2011 by the International Association for the Study of Lung Cancer
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2011年時点の推奨。現在検査の対象とする遺伝子の範囲（ALK・ROS1・BRAF など）と日本の保険適用は、新しい指針で確認が要る（未作成）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-015
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 未治療の EGFR 変異（エクソン19欠失または L858R）陽性進行非小細胞肺癌556人を対象とした FLAURA 試験で、オシメルチニブは従来の EGFR チロシンキナーゼ阻害薬（ゲフィチニブまたはエルロチニブ）と比べて全生存期間を延長した（ハザード比0.80）。Grade 3以上の有害事象は42%対47%だった。
    condition:
      guideline: null
      region: 国際（多施設共同試験）
    differential: null
    common_misconception: EGFR 変異陽性肺癌の初回治療では、どの EGFR チロシンキナーゼ阻害薬を選んでも全生存期間は変わらない
  provenance:
    source_ref: SRC-476
    source: Ramalingam SS, Vansteenkiste J, Planchard D, et al. Overall Survival with Osimertinib in Untreated, EGFR-Mutated Advanced NSCLC. N Engl J Med 2020;382:41-50
    doi: 10.1056/NEJMoa1913662
    pmid: null
    pmcid: null
    url: https://air.unipr.it/bitstream/11381/2872427/3/Flaura.pdf
    source_license: 未確認（機関リポジトリ掲載の刊行版）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ハザード比は抄録で0.799（95.05% CI 0.641〜0.997）、本文では上限が0.996と記載が異なる。無増悪生存期間の主解析（Soria 2018）は別の文献で未取得。オシメルチニブの国内承認・保険適用は未確認
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-016
  domain: LC
  subdomain: 転移性肺腫瘍
  assertion:
    plain_statement_ja: 剖検研究では、がんで死亡した例の約20%で肺が唯一の転移部位だった。肺に転移しやすい腫瘍として、大腸癌・腎癌・乳癌・前立腺癌・口腔咽頭癌のほか、絨毛癌・骨肉腫・軟部肉腫・精巣腫瘍・Ewing 肉腫・甲状腺癌が挙げられる。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-477
    source: Pfannschmidt J, Egerer G, Bischof M, Thomas M, Dienemann H. Surgical Intervention for Pulmonary Metastases. Dtsch Arztebl Int 2012;109(40):645-651
    doi: 10.3238/arztebl.2012.0645
    pmid: null
    pmcid: null
    url: https://di.aerzteblatt.de/int/archive/article/131567
    source_license: 表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 総説の記載（二次資料経由）。各数値の一次資料は総説の引用文献
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-645 (id: JlvnmcU)'
    kokushi: 医学各論 Ⅳ-6-A-②（転移性肺腫瘍、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-017
  domain: LC
  subdomain: 転移性肺腫瘍
  assertion:
    plain_statement_ja: 根治を目的とする肺転移の切除は、原発巣が制御され肺外に転移がないことが前提で、技術的に切除でき手術リスクが許容できることに加え、原発巣の組織型、転移の数と部位、術後に残る肺機能、完全切除（R0）の見込みをもとに判断する。
    condition:
      guideline: null
      region: ドイツ
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-477
    source: Pfannschmidt J, Egerer G, Bischof M, Thomas M, Dienemann H. Surgical Intervention for Pulmonary Metastases. Dtsch Arztebl Int 2012;109(40):645-651
    doi: 10.3238/arztebl.2012.0645
    pmid: null
    pmcid: null
    url: https://di.aerzteblatt.de/int/archive/article/131567
    source_license: 表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ドイツの総説の記載。日本の指針による適応は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-645 (id: JlvnmcU)'
    kokushi: 医学各論 Ⅳ-6-A-②（転移性肺腫瘍、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-018
  domain: LC
  subdomain: 転移性肺腫瘍
  assertion:
    plain_statement_ja: 国際肺転移登録（5,206人）では、肺転移の完全切除後の5年生存率は36%、不完全切除後は13%で、手術死亡は1%だった。原発巣治療後の無病期間が長いこと、胸郭内リンパ節転移がないこと、肺転移の数が少ないことが予後良好の因子とされる。
    condition:
      guideline: null
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-477
    source: Pfannschmidt J, Egerer G, Bischof M, Thomas M, Dienemann H. Surgical Intervention for Pulmonary Metastases. Dtsch Arztebl Int 2012;109(40):645-651
    doi: 10.3238/arztebl.2012.0645
    pmid: null
    pmcid: null
    url: https://di.aerzteblatt.de/int/archive/article/131567
    source_license: 表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 総説に引用された登録研究の数値（二次資料経由）。登録研究の原著（J Thorac Cardiovasc Surg 1997）は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-645 (id: JlvnmcU)'
    kokushi: 医学各論 Ⅳ-6-A-②（転移性肺腫瘍、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-019
  domain: LC
  subdomain: 良性肺腫瘍
  assertion:
    plain_statement_ja: 過誤腫は最も多い良性肺腫瘍で、良性肺腫瘍の約75%、肺の限局性腫瘤の6〜8%を占める。ポップコーン状の石灰化はほぼ特徴的だが一部の例にしかみられず、腫瘤内の脂肪の存在が診断の手がかりになる。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 過誤腫ではほとんどの例でポップコーン状の石灰化がみられる
  provenance:
    source_ref: SRC-478
    source: 'Tavare AN, Cash C. The Clinical Picture: A 78-year-old smoker with an incidental pulmonary mass. Cleve Clin J Med 2014;81(8):477-478'
    doi: 10.3949/ccjm.81a.13150
    pmid: null
    pmcid: null
    url: https://www.ccjm.org/content/81/8/477.full.pdf
    source_license: For personal use only. All other uses require permission.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 症例提示記事の解説部分（二次資料経由）。数値の一次資料は記事の引用文献
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-6-B-①（良性肺腫瘍、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-020
  domain: LC
  subdomain: 良性肺腫瘍
  assertion:
    plain_statement_ja: 肺過誤腫は男性に女性の約2倍多く、70歳代に多い。多くは2.5 cm未満でゆっくり大きくなり、症状がないことが多い（症状を訴えるのは最大39%）。FDG-PET では通常強い集積を示さない。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-478
    source: 'Tavare AN, Cash C. The Clinical Picture: A 78-year-old smoker with an incidental pulmonary mass. Cleve Clin J Med 2014;81(8):477-478'
    doi: 10.3949/ccjm.81a.13150
    pmid: null
    pmcid: null
    url: https://www.ccjm.org/content/81/8/477.full.pdf
    source_license: For personal use only. All other uses require permission.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 症例提示記事の解説部分（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-6-B-①（良性肺腫瘍、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-021
  domain: LC
  subdomain: 神経原性腫瘍
  assertion:
    plain_statement_ja: ITMIG の分類では縦隔を血管前区画（前縦隔）・臓側区画（中縦隔）・椎体傍区画（後縦隔）の3つに分ける。神経原性腫瘍は椎体傍区画に生じ、後根神経節や椎間孔付近の神経から発生する。
    condition:
      guideline: ITMIG 縦隔区画分類
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-479
    source: Carter BW, Benveniste MF, Marom EM. Diagnostic approach to the anterior/prevascular mediastinum for radiologists. Mediastinum 2019;3:18
    doi: 10.21037/med.2018.12.03
    pmid: null
    pmcid: null
    url: https://med.amegroups.org/article/view/5013/html
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 画像診断の総説の記載。神経原性腫瘍の組織型別の頻度は未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-6-C-③（神経原性腫瘍、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-022
  domain: LC
  subdomain: 縦隔腫瘍
  assertion:
    plain_statement_ja: 血管前区画（前縦隔）の病変には、胸腺上皮性腫瘍（原発腫瘍では胸腺腫が最も多い）、リンパ腫、胚細胞腫瘍、胸腺囊胞、胸腺過形成がある。
    condition:
      guideline: ITMIG 縦隔区画分類
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-479
    source: Carter BW, Benveniste MF, Marom EM. Diagnostic approach to the anterior/prevascular mediastinum for radiologists. Mediastinum 2019;3:18
    doi: 10.21037/med.2018.12.03
    pmid: null
    pmcid: null
    url: https://med.amegroups.org/article/view/5013/html
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 画像診断の総説の記載。リンパ腫の組織型（縦隔原発大細胞型 B 細胞リンパ腫、Hodgkin リンパ腫など）の内訳は未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)'
    kokushi: 医学各論 Ⅳ-6-C-①（悪性リンパ腫、a）；医学各論 Ⅳ-6-C-②（胸腺腫瘍、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-023
  domain: LC
  subdomain: 胚細胞腫瘍
  assertion:
    plain_statement_ja: 縦隔のセミノーマは主に10〜39歳の男性にみられ、hCG の軽度上昇は約10%、LDH は通常上昇し、AFP は通常正常である。非セミノーマ性胚細胞腫瘍は主に40歳未満の男性にみられ、約90%で診断時に AFP か hCG が著明に上昇している。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 縦隔セミノーマでは AFP が上昇する
  provenance:
    source_ref: SRC-479
    source: Carter BW, Benveniste MF, Marom EM. Diagnostic approach to the anterior/prevascular mediastinum for radiologists. Mediastinum 2019;3:18
    doi: 10.21037/med.2018.12.03
    pmid: null
    pmcid: null
    url: https://med.amegroups.org/article/view/5013/html
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 画像診断の総説の記載（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)'
    kokushi: 医学各論 Ⅳ-6-C-⑤（胚細胞腫瘍、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-024
  domain: LC
  subdomain: 囊胞性腫瘍
  assertion:
    plain_statement_ja: 前縦隔の病変の評価で、MRI は囊胞と充実性病変の区別や、出血・蛋白成分を含む囊胞の評価に優れる。化学シフト画像では胸腺過形成が逆位相で信号低下を示し（比0.5〜0.6程度）、腫瘍（0.9〜1.0程度）と区別できる。化学療法後には10〜25%程度で胸腺の反跳性過形成が起こる。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 化学療法後に胸腺が大きくなったら、まず再発を考える
  provenance:
    source_ref: SRC-479
    source: Carter BW, Benveniste MF, Marom EM. Diagnostic approach to the anterior/prevascular mediastinum for radiologists. Mediastinum 2019;3:18
    doi: 10.21037/med.2018.12.03
    pmid: null
    pmcid: null
    url: https://med.amegroups.org/article/view/5013/html
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 画像診断の総説の記載。化学シフト比の数値は総説の本文による
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-6-C-④（囊胞性腫瘍、b）；医学各論 Ⅳ-6-C-②（胸腺腫瘍、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-025
  domain: LC
  subdomain: 胸腺腫瘍
  assertion:
    plain_statement_ja: 胸腺上皮性腫瘍は成人の前縦隔で最も多い腫瘍で、全悪性腫瘍の0.2〜1.5%を占める。米国 SEER の胸腺腫の罹患率は10万人年あたり0.13で、胸腺癌は胸腺上皮性腫瘍の約20%である。
    condition:
      guideline: NCI PDQ
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-480
    source: PDQ Adult Treatment Editorial Board. Thymoma and Thymic Carcinoma Treatment (PDQ)–Health Professional Version. National Cancer Institute（2024年10月25日更新）
    doi: null
    pmid: null
    pmcid: null
    url: https://ncbi.nlm.nih.gov/books/NBK66041
    source_license: PDQ の本文は文章として自由に利用できる（PDQ 要約の表示）。図は除く
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQ（2024年10月25日更新）の記載。米国の資料で、数値の一次資料は PDQ の引用文献。WHO 分類は第5版（2021年）が刊行されているが、PDQ は第4版（2015年）を最も広く受け入れられている分類として記載している
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)'
    kokushi: 医学各論 Ⅳ-6-C-②（胸腺腫瘍、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-026
  domain: LC
  subdomain: 胸腺腫瘍
  assertion:
    plain_statement_ja: 胸腺腫には傍腫瘍性疾患が合併しやすく、重症筋無力症が約30〜65%、低ガンマグロブリン血症（Good 症候群）が5〜20%、赤芽球癆が約4%にみられる。胸腺癌に傍腫瘍性疾患が合併することはまれである。
    condition:
      guideline: NCI PDQ
      region: 米国
    differential: null
    common_misconception: 重症筋無力症を合併しやすいのは胸腺腫より胸腺癌である
  provenance:
    source_ref: SRC-480
    source: PDQ Adult Treatment Editorial Board. Thymoma and Thymic Carcinoma Treatment (PDQ)–Health Professional Version. National Cancer Institute（2024年10月25日更新）
    doi: null
    pmid: null
    pmcid: null
    url: https://ncbi.nlm.nih.gov/books/NBK66041
    source_license: PDQ の本文は文章として自由に利用できる（PDQ 要約の表示）。図は除く
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQ（2024年10月25日更新）の記載。米国の資料で、数値の一次資料は PDQ の引用文献。WHO 分類は第5版（2021年）が刊行されているが、PDQ は第4版（2015年）を最も広く受け入れられている分類として記載している
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)'
    kokushi: 医学各論 Ⅳ-6-C-②（胸腺腫瘍、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-027
  domain: LC
  subdomain: 胸腺腫瘍
  assertion:
    plain_statement_ja: WHO 分類では胸腺腫を A・AB・B1・B2・B3 型に分け、胸腺癌には扁平上皮癌、類基底細胞癌、リンパ上皮腫様癌、NUT 癌などが含まれる。病期分類は修正正岡-古賀分類が最も広く使われ、IASLC と ITMIG が作成した TNM 分類も採用されている。
    condition:
      guideline: NCI PDQ
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-480
    source: PDQ Adult Treatment Editorial Board. Thymoma and Thymic Carcinoma Treatment (PDQ)–Health Professional Version. National Cancer Institute（2024年10月25日更新）
    doi: null
    pmid: null
    pmcid: null
    url: https://ncbi.nlm.nih.gov/books/NBK66041
    source_license: PDQ の本文は文章として自由に利用できる（PDQ 要約の表示）。図は除く
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQ（2024年10月25日更新）の記載。米国の資料で、数値の一次資料は PDQ の引用文献。WHO 分類は第5版（2021年）が刊行されているが、PDQ は第4版（2015年）を最も広く受け入れられている分類として記載している
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)'
    kokushi: 医学各論 Ⅳ-6-C-②（胸腺腫瘍、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-028
  domain: LC
  subdomain: 胸腺腫瘍
  assertion:
    plain_statement_ja: 正岡分類による胸腺腫の5年生存率はⅠ期96%、Ⅱ期86%、Ⅲ期69%、Ⅳ期50%で、Ⅰ・Ⅱ期はほぼ全例で完全切除できる。Ⅲ・Ⅳ期の胸腺腫の5年生存率は、完全切除で93%、不完全切除で64%、切除不能で36%と報告されている。
    condition:
      guideline: NCI PDQ
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-480
    source: PDQ Adult Treatment Editorial Board. Thymoma and Thymic Carcinoma Treatment (PDQ)–Health Professional Version. National Cancer Institute（2024年10月25日更新）
    doi: null
    pmid: null
    pmcid: null
    url: https://ncbi.nlm.nih.gov/books/NBK66041
    source_license: PDQ の本文は文章として自由に利用できる（PDQ 要約の表示）。図は除く
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQ（2024年10月25日更新）の記載。米国の資料で、数値の一次資料は PDQ の引用文献。WHO 分類は第5版（2021年）が刊行されているが、PDQ は第4版（2015年）を最も広く受け入れられている分類として記載している。表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)'
    kokushi: 医学各論 Ⅳ-6-C-②（胸腺腫瘍、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-029
  domain: LC
  subdomain: 胸膜中皮腫
  assertion:
    plain_statement_ja: 人口動態統計による日本の中皮腫の死亡数は、2025年に1,561人（男性1,297人、女性264人）だった。この集計は1995年から公表されている。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 中皮腫は女性に多い
  provenance:
    source_ref: SRC-481
    source: 厚生労働省. 都道府県（21大都市再掲）別にみた中皮腫による死亡数の年次推移（平成7年〜令和7年）人口動態統計（確定数）より
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/tokusyu/chuuhisyu25/dl/R07chuuhisyu.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 表から読み取り。部位（胸膜・腹膜など）の内訳と年次推移の数値は抽出できず未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-644 (id: JlvnmcM)'
    kokushi: 医学各論 Ⅳ-6-D-①（胸膜中皮腫、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-030
  domain: LC
  subdomain: 胸膜中皮腫
  assertion:
    plain_statement_ja: 日本の労災認定では、石綿にさらされた労働者の胸膜・腹膜・心膜・精巣鞘膜の中皮腫は、胸部エックス線写真で第1型以上の石綿肺所見があるか、石綿ばく露作業に1年以上従事していれば業務上と認められる。最初のばく露作業開始から10年未満の発症は除かれる。
    condition:
      guideline: 石綿による疾病の認定基準（厚生労働省）
      region: 日本
    differential: null
    common_misconception: 中皮腫の労災認定には10年以上の石綿ばく露作業歴が必要である
  provenance:
    source_ref: SRC-482
    source: 厚生労働省・都道府県労働局・労働基準監督署. 石綿による疾病の労災認定（パンフレット、令和5年9月版）
    doi: null
    pmid: null
    pmcid: null
    url: https://jsite.mhlw.go.jp/tokyo-roudoukyoku/content/contents/001749711.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 令和5年9月版のパンフレットで確認。認定基準の通達本文との照合は未了
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-644 (id: JlvnmcM)'
    kokushi: 医学各論 Ⅳ-6-D-①（胸膜中皮腫、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-031
  domain: LC
  subdomain: 肺癌
  assertion:
    plain_statement_ja: 日本の労災認定では、石綿にさらされた労働者の原発性肺癌は、石綿肺所見がある、胸膜プラークがあり石綿ばく露作業に10年以上従事した、石綿小体（乾燥肺1 gあたり5,000本以上または気管支肺胞洗浄液1 mLあたり5本以上）などの所見があり1年以上従事した、などのいずれかに当てはまれば業務上と認められる。
    condition:
      guideline: 石綿による疾病の認定基準（厚生労働省）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-482
    source: 厚生労働省・都道府県労働局・労働基準監督署. 石綿による疾病の労災認定（パンフレット、令和5年9月版）
    doi: null
    pmid: null
    pmcid: null
    url: https://jsite.mhlw.go.jp/tokyo-roudoukyoku/content/contents/001749711.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 令和5年9月版のパンフレットで確認。要件は6項目あり、主張文はその一部。表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)'
    kokushi: 医学各論 Ⅳ-6-A-①（肺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-032
  domain: LC
  subdomain: 胸膜中皮腫
  assertion:
    plain_statement_ja: 石綿健康被害救済法（平成18年法律第4号）による救済制度は、労災補償などの対象とならない人を対象に、中皮腫、肺癌、著しい呼吸機能障害を伴う石綿肺、著しい呼吸機能障害を伴うびまん性胸膜肥厚の4疾病を指定し、医療費の自己負担分や療養手当などを給付する。申請は環境再生保全機構が受け付ける。
    condition:
      guideline: 石綿による健康被害の救済に関する法律
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-483
    source: 環境省 大臣官房環境保健部 石綿健康被害対策室. 石綿健康被害救済制度の施行状況等について（資料3、令和4年6月6日）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.env.go.jp/content/000047431.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する環境省のコンテンツ（表示は未確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 令和4年6月時点の資料。給付額は主張文に含めていない。石綿肺・びまん性胸膜肥厚は第12回（IL）の範囲と重なるため、IL 側と重複がないか確認する
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-644 (id: JlvnmcM)'
    kokushi: 医学各論 Ⅳ-6-D-①（胸膜中皮腫、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-033
  domain: LC
  subdomain: 癌性胸膜炎
  assertion:
    plain_statement_ja: 症状のある胸水の約40%は悪性腫瘍によるもので、悪性胸水の約75%は肺癌・乳癌・リンパ腫・白血病による。悪性胸水と診断された後の生存期間の中央値は3〜4か月程度とされる。
    condition:
      guideline: NCI PDQ
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-484
    source: PDQ Supportive and Palliative Care Editorial Board. Cardiopulmonary Syndromes (PDQ)–Health Professional Version. National Cancer Institute（2023年2月21日公開版）
    doi: null
    pmid: null
    pmcid: null
    url: https://https.ncbi.nlm.nih.gov/books/NBK65834
    source_license: PDQ の本文は文章として自由に利用できる（PDQ 要約の表示。今回の取得範囲では利用条件の頁は未取得）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQ（2023年2月21日公開版）の記載。米国の資料で、数値の一次資料は PDQ の引用文献（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-02-06-018 (id: JlAKpiI)'
    kokushi: 医学各論 Ⅳ-6-E（癌性胸膜炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-034
  domain: LC
  subdomain: 癌性胸膜炎
  assertion:
    plain_statement_ja: 悪性胸水に対する胸腔穿刺排液は症状を一時的に和らげるが、約98%が30日以内に再貯留する。留置型の胸腔カテーテルでは最大96%で症状が改善し、最大44%で自然に胸膜癒着が得られ、胸膜癒着術より入院期間が短い。
    condition:
      guideline: NCI PDQ
      region: 米国
    differential: null
    common_misconception: 悪性胸水は一度排液すれば再びたまることは少ない
  provenance:
    source_ref: SRC-484
    source: PDQ Supportive and Palliative Care Editorial Board. Cardiopulmonary Syndromes (PDQ)–Health Professional Version. National Cancer Institute（2023年2月21日公開版）
    doi: null
    pmid: null
    pmcid: null
    url: https://https.ncbi.nlm.nih.gov/books/NBK65834
    source_license: PDQ の本文は文章として自由に利用できる（PDQ 要約の表示。今回の取得範囲では利用条件の頁は未取得）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQ（2023年2月21日公開版）の記載。米国の資料で、数値の一次資料は PDQ の引用文献（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-02-06-018 (id: JlAKpiI)；TBL-02-06-020 (id: JlAKpiQ)'
    kokushi: 医学各論 Ⅳ-6-E（癌性胸膜炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-035
  domain: LC
  subdomain: 癌性胸膜炎
  assertion:
    plain_statement_ja: 英国胸部疾患学会（BTS）2023 は、肺の再膨張不全が知られていない悪性胸水では、初回治療として留置型胸腔カテーテルか胸膜癒着術を患者が選べるようにすることを推奨した（Conditional）。画像上25%を超える再膨張不全がある場合は、タルクによる癒着術より留置型カテーテルを勧めている（good practice point）。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-485
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143.full.pdf
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: BTS 2023 の推奨文の要旨（英国）。日本の気胸・胸水診療の指針（日本気胸・囊胞性肺疾患学会など）は今回確認していない。タルクの国内承認状況は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-02-06-018 (id: JlAKpiI)'
    kokushi: 医学各論 Ⅳ-6-E（癌性胸膜炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-036
  domain: LC
  subdomain: 癌性胸膜炎
  assertion:
    plain_statement_ja: BTS 2023 は、続発性の悪性胸膜病変が疑われる場合の最初の検査を胸水細胞診とし、25〜50 mLの胸水を提出するよう勧めた（Strong – by consensus）。細胞診が陰性なら追加の検査を行い、胸水のバイオマーカーで診断しないこと、CT で異常がなくても悪性は否定できないことも示している。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: 胸水細胞診が陰性なら悪性胸水は否定できる
  provenance:
    source_ref: SRC-485
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143.full.pdf
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: BTS 2023 の推奨文の要旨（英国）。日本の気胸・胸水診療の指針（日本気胸・囊胞性肺疾患学会など）は今回確認していない
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-020 (id: JlAKpiQ)'
    kokushi: 医学各論 Ⅳ-6-E（癌性胸膜炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-037
  domain: LC
  subdomain: 癌性リンパ管症
  assertion:
    plain_statement_ja: 肺の癌性リンパ管症18例の高分解能CTの検討では、小葉間隔壁の肥厚が全例にみられ（平滑15例、平滑と結節状の混在3例）、気管支血管束の肥厚が17例、すりガラス影と多角形の線状影が各15例、結節が10例にみられた。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-486
    source: 'Hwang JW, Kim Y, Hwang JH, Kim TS, Ro DW, Lee KS. Lymphangitic Carcinomatosis of the Lung: Serial Changes on High-Resolution CT. J Korean Radiol Soc 1997;37(6):1051-1057'
    doi: 10.3348/jkrs.1997.37.6.1051
    pmid: null
    pmcid: null
    url: https://synapse.koreamed.org/articles/1067885
    source_license: Copyright © The Korean Radiological Society
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 1997年の単施設18例の研究で、韓国語論文の英文抄録で確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-6-F（癌性リンパ管症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: LC-038
  domain: LC
  subdomain: 癌性リンパ管症
  assertion:
    plain_statement_ja: 同研究の経過観察では、化学療法を行わなかった例で CT 所見が広がり、平滑な隔壁肥厚が結節状に変わる例があった。化学療法を行った例では所見が改善するか進行が止まった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-486
    source: 'Hwang JW, Kim Y, Hwang JH, Kim TS, Ro DW, Lee KS. Lymphangitic Carcinomatosis of the Lung: Serial Changes on High-Resolution CT. J Korean Radiol Soc 1997;37(6):1051-1057'
    doi: 10.3348/jkrs.1997.37.6.1051
    pmid: null
    pmcid: null
    url: https://synapse.koreamed.org/articles/1067885
    source_license: Copyright © The Korean Radiological Society
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 1997年の単施設18例の研究（英文抄録で確認）。症状や予後の数値は記載がない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-6-F（癌性リンパ管症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-001
  domain: PL
  subdomain: 気胸
  assertion:
    plain_statement_ja: BTS 2023 は、成人の原発性自然気胸で症状がないか軽い（強い痛み・息切れ・生理学的な悪化がない）場合は、虚脱の大きさにかかわらず経過観察を考慮できるとした（Conditional – by consensus）。治療の選択は大きさより症状で決める。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: 気胸の治療方針は虚脱の大きさだけで決まる
  provenance:
    source_ref: SRC-485
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143.full.pdf
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: BTS 2023 の推奨文の要旨（英国）。日本の気胸・胸水診療の指針（日本気胸・囊胞性肺疾患学会など）は今回確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-241 (id: Jlvnl1A)'
    kokushi: 医学各論 Ⅳ-7-A-①（気胸、緊張性気胸、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-002
  domain: PL
  subdomain: 気胸
  assertion:
    plain_statement_ja: BTS 2023 は、十分な支援と経過観察の体制がある成人の原発性自然気胸では、外来での管理（携帯型の脱気器具）を初期治療として考慮し、経過観察や外来管理が適さない場合は穿刺吸引か胸腔ドレナージを考慮するとした（いずれも Conditional）。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-485
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143.full.pdf
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: BTS 2023 の推奨文の要旨（英国）。日本の気胸・胸水診療の指針（日本気胸・囊胞性肺疾患学会など）は今回確認していない。携帯型脱気器具の国内での使用状況は未確認
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-01-00-241 (id: Jlvnl1A)'
    kokushi: 医学各論 Ⅳ-7-A-①（気胸、緊張性気胸、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-003
  domain: PL
  subdomain: 気胸
  assertion:
    plain_statement_ja: BTS 2023 は、続発性自然気胸の再発予防として、たとえば気胸で状態が悪化した重症 COPD の患者などに化学的胸膜癒着術を考慮できるとした（Conditional）。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-485
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143.full.pdf
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: BTS 2023 の推奨文の要旨（英国）。日本の気胸・胸水診療の指針（日本気胸・囊胞性肺疾患学会など）は今回確認していない
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-01-00-241 (id: Jlvnl1A)'
    kokushi: 医学各論 Ⅳ-7-A-①（気胸、緊張性気胸、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-004
  domain: PL
  subdomain: 気胸
  assertion:
    plain_statement_ja: BTS 2023 は、同側2回目または対側初回の自然気胸では待機的手術を考慮し、潜水士・航空機操縦士・軍人や初回が緊張性気胸だった人など再発予防が特に重要な場合は初回から手術を考慮するとした（good practice point、Conditional）。手術としては外科的胸膜癒着術やブラ切除を挙げている。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: 緊張性気胸を起こしても、初回であれば再発予防の手術は検討しない
  provenance:
    source_ref: SRC-485
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143.full.pdf
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: BTS 2023 の推奨文の要旨（英国）。日本の気胸・胸水診療の指針（日本気胸・囊胞性肺疾患学会など）は今回確認していない
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-01-00-241 (id: Jlvnl1A)'
    kokushi: 医学各論 Ⅳ-7-A-①（気胸、緊張性気胸、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-005
  domain: PL
  subdomain: 血胸
  assertion:
    plain_statement_ja: 血胸は胸膜腔内に出血した状態をいう。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-494
    source: 'National Library of Medicine. MeSH Descriptor: Hemothorax (D006491)'
    doi: null
    pmid: null
    pmcid: null
    url: https://meshb.nlm.nih.gov/record/ui?ui=D006491
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: MeSH（米国国立医学図書館の統制語彙）の定義文。定義のみで、頻度・治療の記載はない。外傷性血胸の排液・手術の適応（EAST 2011 など）は出典を取得できず未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-243 (id: Jlvnl1Y)'
    kokushi: 医学各論 Ⅳ-7-A-②（血胸、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-006
  domain: PL
  subdomain: 乳び胸
  assertion:
    plain_statement_ja: 胸水の中性脂肪が110 mg/dLを超えると乳び胸水が強く疑われ、50〜110 mg/dLのときはリポ蛋白電気泳動でカイロミクロンの帯を確認して判定する。141例の胸水を検討した研究にもとづく。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-487
    source: Staats BA, et al. The lipoprotein profile of chylous and nonchylous pleural effusions. Mayo Clin Proc 1980;55(11):700-704
    doi: null
    pmid: '7442324'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/7442324/
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認。50 mg/dL 未満で乳び胸を否定するという基準は抄録には明記されていない。著者名は API で確定する
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-020 (id: JlAKpiQ)'
    kokushi: 医学各論 Ⅳ-7-A-③（乳び胸、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-007
  domain: PL
  subdomain: 乳び胸
  assertion:
    plain_statement_ja: 同研究で胸水の中性脂肪の中央値は、乳び胸水で249 mg/dL（49〜2,270）、乳びでない胸水で33 mg/dL（13〜107）だった。肉眼で乳びらしく見えたのは乳び胸水の半数未満で、外観は判定の手がかりとして不十分だった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 乳び胸水は必ず乳白色に見える
  provenance:
    source_ref: SRC-487
    source: Staats BA, et al. The lipoprotein profile of chylous and nonchylous pleural effusions. Mayo Clin Proc 1980;55(11):700-704
    doi: null
    pmid: '7442324'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/7442324/
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-020 (id: JlAKpiQ)'
    kokushi: 医学各論 Ⅳ-7-A-③（乳び胸、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-008
  domain: PL
  subdomain: 縦隔気腫
  assertion:
    plain_statement_ja: 縦隔気腫は、気管・気管支から空気が漏れて縦隔の組織内に空気がたまった状態で、多くは外傷による。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-488
    source: 'National Library of Medicine. MeSH Descriptor: Mediastinal Emphysema (D008478)'
    doi: null
    pmid: null
    pmcid: null
    url: https://ncbi.nlm.nih.gov/mesh/68008478
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: MeSH（米国国立医学図書館の統制語彙）の定義文。定義のみで、頻度・治療の記載はない。自然縦隔気腫の頻度・経過（若年男性に多い、保存的治療など）は出典を取得できず未作成。皮下気腫のカードもなし
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-242 (id: Jlvnl1U)'
    kokushi: 医学各論 Ⅳ-7-B-①（縦隔気腫、皮下気腫、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-009
  domain: PL
  subdomain: 気管食道瘻
  assertion:
    plain_statement_ja: 気管食道瘻は食道と気管の間の異常な交通で、先天性と後天性があり、先天性のものはしばしば食道閉鎖を伴う。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-489
    source: 'National Library of Medicine. MeSH Descriptor: Tracheoesophageal Fistula (D014138)'
    doi: null
    pmid: null
    pmcid: null
    url: https://ncbi.nlm.nih.gov/mesh/D014138
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: MeSH（米国国立医学図書館の統制語彙）の定義文。定義のみで、頻度・治療の記載はない。先天性は小児（Ⅰ）の範囲。悪性腫瘍による後天性瘻のステント治療（ESGE 2021）は本文を取得できず未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-7-B-②（気管食道瘻、食道気管瘻、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-010
  domain: PL
  subdomain: 上大静脈症候群
  assertion:
    plain_statement_ja: 近年の報告では、上大静脈症候群の約95%は癌に関連し、原因として最も多いのは小細胞肺癌で、扁平上皮癌、腺癌、非 Hodgkin リンパ腫、大細胞癌が続く。癌患者の悪性でない原因として、中心静脈カテーテルやペースメーカーのリードに伴う血栓がある。
    condition:
      guideline: NCI PDQ
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-484
    source: PDQ Supportive and Palliative Care Editorial Board. Cardiopulmonary Syndromes (PDQ)–Health Professional Version. National Cancer Institute（2023年2月21日公開版）
    doi: null
    pmid: null
    pmcid: null
    url: https://https.ncbi.nlm.nih.gov/books/NBK65834
    source_license: PDQ の本文は文章として自由に利用できる（PDQ 要約の表示。今回の取得範囲では利用条件の頁は未取得）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQ（2023年2月21日公開版）の記載。米国の資料で、数値の一次資料は PDQ の引用文献（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-196 (id: JlvnlwE)'
    kokushi: 医学各論 Ⅳ-7-B-③（上大静脈症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-011
  domain: PL
  subdomain: 上大静脈症候群
  assertion:
    plain_statement_ja: 上大静脈症候群の症状は呼吸困難・咳と、顔面・頸部・上半身・上肢の腫脹で、頸部や胸壁の静脈の怒張、浮腫、顔面の紅潮、頻呼吸がみられる。最初の評価は胸部エックス線写真で、造影した胸部CTが最も多くの情報を与える。
    condition:
      guideline: NCI PDQ
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-484
    source: PDQ Supportive and Palliative Care Editorial Board. Cardiopulmonary Syndromes (PDQ)–Health Professional Version. National Cancer Institute（2023年2月21日公開版）
    doi: null
    pmid: null
    pmcid: null
    url: https://https.ncbi.nlm.nih.gov/books/NBK65834
    source_license: PDQ の本文は文章として自由に利用できる（PDQ 要約の表示。今回の取得範囲では利用条件の頁は未取得）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQ（2023年2月21日公開版）の記載。米国の資料で、数値の一次資料は PDQ の引用文献（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-196 (id: JlvnlwE)；TBL-02-06-023 (id: JlAKpiY)'
    kokushi: 医学各論 Ⅳ-7-B-③（上大静脈症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-012
  domain: PL
  subdomain: 上大静脈症候群
  assertion:
    plain_statement_ja: 上大静脈症候群の約3〜5%は癌によらないため、治療の前に組織診断を確定する。気道閉塞や脳浮腫がなければ、原因が確定するまで放射線治療や化学療法は控え、その間は頭部挙上、副腎皮質ステロイド、利尿薬で対応する。
    condition:
      guideline: NCI PDQ
      region: 米国
    differential: null
    common_misconception: 上大静脈症候群は緊急に放射線照射を始めるべきで、組織診断は後でよい
  provenance:
    source_ref: SRC-484
    source: PDQ Supportive and Palliative Care Editorial Board. Cardiopulmonary Syndromes (PDQ)–Health Professional Version. National Cancer Institute（2023年2月21日公開版）
    doi: null
    pmid: null
    pmcid: null
    url: https://https.ncbi.nlm.nih.gov/books/NBK65834
    source_license: PDQ の本文は文章として自由に利用できる（PDQ 要約の表示。今回の取得範囲では利用条件の頁は未取得）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQ（2023年2月21日公開版）の記載。米国の資料で、数値の一次資料は PDQ の引用文献（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-196 (id: JlvnlwE)'
    kokushi: 医学各論 Ⅳ-7-B-③（上大静脈症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-013
  domain: PL
  subdomain: 上大静脈症候群
  assertion:
    plain_statement_ja: 上大静脈症候群では、リンパ腫や小細胞肺癌のように化学療法が効きやすい腫瘍には化学療法が第一選択となる。放射線治療による症状の軽減は小細胞癌で62〜80%、非小細胞癌で約46%と報告され、ステント留置は約90%以上の奏効が報告されているが、前向きの比較試験はない。
    condition:
      guideline: NCI PDQ
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-484
    source: PDQ Supportive and Palliative Care Editorial Board. Cardiopulmonary Syndromes (PDQ)–Health Professional Version. National Cancer Institute（2023年2月21日公開版）
    doi: null
    pmid: null
    pmcid: null
    url: https://https.ncbi.nlm.nih.gov/books/NBK65834
    source_license: PDQ の本文は文章として自由に利用できる（PDQ 要約の表示。今回の取得範囲では利用条件の頁は未取得）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQ（2023年2月21日公開版）の記載。米国の資料で、数値の一次資料は PDQ の引用文献（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-01-00-196 (id: JlvnlwE)'
    kokushi: 医学各論 Ⅳ-7-B-③（上大静脈症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-014
  domain: PL
  subdomain: 反回神経麻痺
  assertion:
    plain_statement_ja: 声帯麻痺は片側または両側の声帯の麻痺で、先天性と後天性があり、中枢神経・迷走神経・喉頭の神経の枝の障害で起こり、嗄声や失声を生じる。反回神経麻痺はこの一部として扱われる。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-490
    source: 'National Library of Medicine. MeSH Descriptor: Vocal Cord Paralysis (D014826)'
    doi: null
    pmid: null
    pmcid: null
    url: https://https.ncbi.nlm.nih.gov/mesh/68014826
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: MeSH（米国国立医学図書館の統制語彙）の定義文。定義のみで、頻度・治療の記載はない。左右差（大動脈弓を回る左反回神経に多い）や原因疾患（肺癌・食道癌・甲状腺手術など）の頻度は出典を取得できず未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-7-B-④（反回神経麻痺、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-015
  domain: PL
  subdomain: 肋骨骨折
  assertion:
    plain_statement_ja: フレイルチェストは古典的には、連続する3本以上の肋骨がそれぞれ2か所以上で骨折したものと定義される。研究ごとに定義は異なる。
    condition:
      guideline: EAST practice management guideline 2017
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-491
    source: 'Kasotakis G, Hasenboehler EA, Streib EW, et al. Operative fixation of rib fractures after blunt trauma: A practice management guideline from the Eastern Association for the Surgery of Trauma. J Trauma Acute Care Surg 2017;82(3):618-626'
    doi: null
    pmid: null
    pmcid: null
    url: https://east.org/education-resources/practice-management-guidelines/details/rib-fractures-open-reduction-and-internal-fixation-of-update-in-process
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: EAST の指針頁の記載。題名と第4著者以降は API で確定する
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-7-C-①（肋骨骨折、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-016
  domain: PL
  subdomain: 肋骨骨折
  assertion:
    plain_statement_ja: 米国外傷外科学会（EAST）2017 の指針は、鈍的外傷による成人のフレイルチェストに対し、死亡、人工呼吸の期間、ICU・入院期間、肺炎、気管切開を減らす目的で、非手術治療より肋骨の観血的整復固定を条件付きで推奨した（エビデンスの質は低い）。フレイルでない肋骨骨折については推奨を示していない。
    condition:
      guideline: EAST practice management guideline 2017
      region: 米国
    differential: null
    common_misconception: 多発肋骨骨折なら、フレイルチェストでなくても肋骨固定術が推奨されている
  provenance:
    source_ref: SRC-491
    source: 'Kasotakis G, Hasenboehler EA, Streib EW, et al. Operative fixation of rib fractures after blunt trauma: A practice management guideline from the Eastern Association for the Surgery of Trauma. J Trauma Acute Care Surg 2017;82(3):618-626'
    doi: null
    pmid: null
    pmcid: null
    url: https://east.org/education-resources/practice-management-guidelines/details/rib-fractures-open-reduction-and-internal-fixation-of-update-in-process
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: エビデンスの質は頁内で low と very low の記載が混在。EAST は改訂作業中（UPDATE IN PROCESS）と表示されている
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)'
    kokushi: 医学各論 Ⅳ-7-C-①（肋骨骨折、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-017
  domain: PL
  subdomain: 胸郭変形
  assertion:
    plain_statement_ja: 漏斗胸は、胸骨の下部が後方に偏位して前胸壁が漏斗状にくぼむ発達上の異常である。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-492
    source: 'National Library of Medicine. MeSH Descriptor: Funnel Chest (D005660)'
    doi: null
    pmid: null
    pmcid: null
    url: https://https.ncbi.nlm.nih.gov/mesh/68005660
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: MeSH（米国国立医学図書館の統制語彙）の定義文。定義のみで、頻度・治療の記載はない。重症度の指標（Haller 指数）や手術（Nuss 法）の適応は出典を取得できず未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-245 (id: Jlvnl1s)'
    kokushi: 医学各論 Ⅳ-7-C-②（胸郭変形、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-018
  domain: PL
  subdomain: 横隔膜ヘルニア
  assertion:
    plain_statement_ja: 横隔膜ヘルニアは、横隔膜の先天性または外傷性の欠損から腹部の臓器が胸腔内に脱出した状態である。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-493
    source: 'National Library of Medicine. MeSH Descriptor: Hernia, Diaphragmatic (D006548)'
    doi: null
    pmid: null
    pmcid: null
    url: https://meshb.nlm.nih.gov/record/ui?ui=D006548
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: MeSH（米国国立医学図書館の統制語彙）の定義文。定義のみで、頻度・治療の記載はない。先天性横隔膜ヘルニアは小児（Ⅰ）の範囲。外傷性の左右差などは未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-247 (id: Jlvnl14)'
    kokushi: 医学各論 Ⅳ-7-C-③（横隔膜ヘルニア、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-019
  domain: PL
  subdomain: 睡眠時無呼吸症候群
  assertion:
    plain_statement_ja: 日本呼吸器学会の SAS 診療ガイドライン2020 は ICSD-3 にもとづき、眠気・目撃された無呼吸・高血圧などの症状や合併症があり睡眠ポリグラフ検査（PSG）で閉塞性の呼吸イベントが1時間に5回以上ある場合、または症状によらず15回以上ある場合を閉塞性睡眠時無呼吸と診断するとした。
    condition:
      guideline: 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020（日本呼吸器学会ほか、ICSD-3 準拠）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-495
    source: 日本呼吸器学会・厚生労働科学研究費補助金難治性疾患政策研究事業「難治性呼吸器疾患・肺高血圧症に関する調査研究」班（監修）. 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/guidelines_sas2020.pdf
    source_license: 取得範囲に著作権表示なし（学会の著作物と考えられる）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本語版 PDF で確認。英語版（Sleep Biol Rhythms、DOI 10.1007/s41105-021-00353-6）は CQ16〜36 の治療部分のみを収載しており、診断基準の部分は日本語版にしかない可能性がある。表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-233 (id: Jlvnl0I)；TBL-02-06-021 (id: JlAKpiU)'
    kokushi: 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-020
  domain: PL
  subdomain: 睡眠時無呼吸症候群
  assertion:
    plain_statement_ja: 同ガイドラインでは、閉塞性睡眠時無呼吸の重症度を無呼吸低呼吸指数（AHI）で、5以上15未満を軽症、15以上30未満を中等症、30以上を重症とする。
    condition:
      guideline: 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020（日本呼吸器学会ほか）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-495
    source: 日本呼吸器学会・厚生労働科学研究費補助金難治性疾患政策研究事業「難治性呼吸器疾患・肺高血圧症に関する調査研究」班（監修）. 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/guidelines_sas2020.pdf
    source_license: 取得範囲に著作権表示なし（学会の著作物と考えられる）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本語版 PDF で確認。英語版（Sleep Biol Rhythms、DOI 10.1007/s41105-021-00353-6）は CQ16〜36 の治療部分のみを収載しており、診断基準の部分は日本語版にしかない可能性がある
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-233 (id: Jlvnl0I)'
    kokushi: 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-021
  domain: PL
  subdomain: 睡眠時無呼吸症候群
  assertion:
    plain_statement_ja: 同ガイドラインは、中等症以上の閉塞性睡眠時無呼吸が成人男性の約20%、閉経後女性の約10%にみられるとし、AHI 15以上に日中の眠気を伴う睡眠時無呼吸症候群は男性の約5%、女性の2〜3%と記載している。
    condition:
      guideline: 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020（日本呼吸器学会ほか）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-495
    source: 日本呼吸器学会・厚生労働科学研究費補助金難治性疾患政策研究事業「難治性呼吸器疾患・肺高血圧症に関する調査研究」班（監修）. 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/guidelines_sas2020.pdf
    source_license: 取得範囲に著作権表示なし（学会の著作物と考えられる）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本語版 PDF で確認。英語版（Sleep Biol Rhythms、DOI 10.1007/s41105-021-00353-6）は CQ16〜36 の治療部分のみを収載しており、診断基準の部分は日本語版にしかない可能性がある。有病率が日本人の調査にもとづくかどうかは本文の引用文献で確認が要る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-233 (id: Jlvnl0I)'
    kokushi: 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-022
  domain: PL
  subdomain: 睡眠時無呼吸症候群
  assertion:
    plain_statement_ja: 同ガイドラインは、中等症から重症の閉塞性睡眠時無呼吸や日中の症状が強い例では CPAP を第一選択として推奨し（推奨の強さ1、エビデンスの強さA）、CPAP の適応にならないか使えない軽症〜中等症には口腔内装置を提案している（推奨の強さ2、エビデンスの強さB）。
    condition:
      guideline: 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020（日本呼吸器学会ほか）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-495
    source: 日本呼吸器学会・厚生労働科学研究費補助金難治性疾患政策研究事業「難治性呼吸器疾患・肺高血圧症に関する調査研究」班（監修）. 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/guidelines_sas2020.pdf
    source_license: 取得範囲に著作権表示なし（学会の著作物と考えられる）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本語版 PDF で確認。英語版（Sleep Biol Rhythms、DOI 10.1007/s41105-021-00353-6）は CQ16〜36 の治療部分のみを収載しており、診断基準の部分は日本語版にしかない可能性がある。CPAP の降圧効果は循環器 HT-016 で扱う
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-01-00-233 (id: Jlvnl0I)'
    kokushi: 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-023
  domain: PL
  subdomain: 睡眠時無呼吸症候群
  assertion:
    plain_statement_ja: 日本の在宅持続陽圧呼吸療法（CPAP）の保険算定は、AHI が20以上で、日中の傾眠や起床時の頭痛など日常生活に支障がある自覚症状があり、PSG で睡眠の分断や深睡眠の著しい減少がみられ、CPAP で改善する例が対象となる。AHI が40以上の場合は自覚症状の要件を満たせば対象となり、開始後最長2か月で治療状況を評価し、続けられる例だけ算定を続ける。
    condition:
      guideline: 診療報酬 C107-2 在宅持続陽圧呼吸療法指導管理料
      region: 日本
    differential: null
    common_misconception: CPAP は AHI 5以上であれば保険で導入できる
  provenance:
    source_ref: SRC-496
    source: 厚生労働省東北厚生局. 保険診療と個別指導（医科）第6回 在宅医療について〜診療報酬算定に当たっての留意事項〜（参考資料、2024年3月22日）
    doi: null
    pmid: null
    pmcid: null
    url: https://kouseikyoku.mhlw.go.jp/tohoku/news/000326889.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ（表示は未確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 東北厚生局の個別指導資料（2024年3月）で確認。点数表と留意事項通知（令和6年度改定）の本文との照合が要る。簡易検査で判定できる条件は資料から読み取れなかった
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-01-00-233 (id: Jlvnl0I)'
    kokushi: 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-024
  domain: PL
  subdomain: 睡眠時無呼吸症候群
  assertion:
    plain_statement_ja: 同ガイドラインでは、中枢性睡眠時無呼吸症候群は中枢性イベントが1時間に5回以上で全イベントの50%以上を占めるものとされる。チェーンストークス呼吸は中枢性睡眠時無呼吸の一型で、心不全、脳卒中後、重症の腎不全で多い。
    condition:
      guideline: 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020（日本呼吸器学会ほか）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-495
    source: 日本呼吸器学会・厚生労働科学研究費補助金難治性疾患政策研究事業「難治性呼吸器疾患・肺高血圧症に関する調査研究」班（監修）. 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/guidelines_sas2020.pdf
    source_license: 取得範囲に著作権表示なし（学会の著作物と考えられる）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本語版 PDF で確認。英語版（Sleep Biol Rhythms、DOI 10.1007/s41105-021-00353-6）は CQ16〜36 の治療部分のみを収載しており、診断基準の部分は日本語版にしかない可能性がある。心不全に伴うものの治療（ASV など）は循環器 HF の範囲
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-233 (id: Jlvnl0I)'
    kokushi: 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-025
  domain: PL
  subdomain: 過換気症候群
  assertion:
    plain_statement_ja: 過換気は、呼吸数の増加や一回換気量の増加により、ガス交換に必要な量を超えて肺が換気され、二酸化炭素が過剰に排出される状態である。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-497
    source: 'National Library of Medicine. MeSH Descriptor: Hyperventilation (D006985)'
    doi: null
    pmid: null
    pmcid: null
    url: https://meshb.nlm.nih.gov/record/ui?ui=D006985
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: MeSH（米国国立医学図書館の統制語彙）の定義文。定義のみで、頻度・治療の記載はない。過換気症候群の診断・治療の指針は出典を取得できず未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-232 (id: Jlvnl0A)'
    kokushi: 医学各論 Ⅳ-8-A-②（過換気症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-026
  domain: PL
  subdomain: 過換気症候群
  assertion:
    plain_statement_ja: 紙袋再呼吸の検討では、過換気をした健常者20人が紙袋で再呼吸すると酸素分圧が3分で平均26.6 mmHg低下し、最大42 mmHg低下した。低酸素血症や心筋虚血が見逃されたまま紙袋再呼吸が行われ死亡した3例も報告されている。
    condition:
      guideline: null
      region: 米国
    differential: null
    common_misconception: 過換気発作には紙袋再呼吸が安全で標準的な対処法である
  provenance:
    source_ref: SRC-498
    source: Callaham M. Hypoxic hazards of traditional paper bag rebreathing in hyperventilating patients. Ann Emerg Med 1989;18(6):622-628
    doi: 10.1016/s0196-0644(89)80515-3
    pmid: '2499228'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/2499228/
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認。酸素分圧の測定部位（呼気か動脈血か）は抄録の範囲で確定できていない
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-01-00-232 (id: Jlvnl0A)'
    kokushi: 医学各論 Ⅳ-8-A-②（過換気症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: PL-027
  domain: PL
  subdomain: 肺胞低換気症候群
  assertion:
    plain_statement_ja: 肥満低換気症候群は、高度の肥満で腹部や横隔膜周囲の脂肪が換気を制限し、血液ガスの変化に対する呼吸調節の反応が低下して、慢性の低酸素血症と高二酸化炭素血症、多血症、昼夜の過眠を生じる病態で、閉塞性睡眠時無呼吸を伴うことが多いが伴わない場合もある。Pickwick 症候群とも呼ばれる。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-499
    source: 'National Library of Medicine. MeSH Descriptor: Obesity Hypoventilation Syndrome (D010845)'
    doi: null
    pmid: null
    pmcid: null
    url: https://https.ncbi.nlm.nih.gov/mesh/68010845
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: MeSH（米国国立医学図書館の統制語彙）の定義文。定義のみで、頻度・治療の記載はない。ATS 2019 の診断基準（BMI・PaCO2 の閾値、血清重炭酸の目安）と治療推奨は本文を取得できず未作成
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-203 (id: Jlvnlw8)；TBL-01-00-233 (id: Jlvnl0I)'
    kokushi: 医学各論 Ⅳ-8-A-③（肺胞低換気症候群、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-001
  domain: RX
  subdomain: 主要症候（血痰・喀血）
  assertion:
    plain_statement_ja: 大量喀血の定義は統一されておらず、24時間で600 mLを超える、または1時間に150 mLを超える出血とする定義があり、このメタ解析では24時間で200 mLを超えるものとした。出血の経路としては、圧の高い気管支動脈が最も多い。
    condition:
      guideline: null
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-500
    source: Karlafti E, Tsavdaris D, Kotzakioulafi E, et al. Which Is the Best Way to Treat Massive Hemoptysis? A Systematic Review and Meta-Analysis of Observational Studies. J Pers Med 2023;13(12):1649
    doi: 10.3390/jpm13121649
    pmid: null
    pmcid: null
    url: https://www.mdpi.com/2075-4426/13/12/1649
    source_license: CC BY 3.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 定義は論文の序論と考察の記載
  curriculum:
    core_curriculum: 'PS-02-07-02 (id: JkxnuQ4)；TBL-02-06-012 (id: JlAKph4)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-002
  domain: RX
  subdomain: 主要症候（血痰・喀血）
  assertion:
    plain_statement_ja: 大量喀血に対する気管支動脈塞栓術の観察研究30件のメタ解析では、統合した技術的成功率97.2%、臨床的成功率92.5%、再出血21.5%、死亡3.5%だった。含まれた研究はすべて後ろ向きで、出版バイアスが示唆された。
    condition:
      guideline: null
      region: 国際
    differential: null
    common_misconception: 気管支動脈塞栓術で止血できれば再出血はまれである
  provenance:
    source_ref: SRC-500
    source: Karlafti E, Tsavdaris D, Kotzakioulafi E, et al. Which Is the Best Way to Treat Massive Hemoptysis? A Systematic Review and Meta-Analysis of Observational Studies. J Pers Med 2023;13(12):1649
    doi: 10.3390/jpm13121649
    pmid: null
    pmcid: null
    url: https://www.mdpi.com/2075-4426/13/12/1649
    source_license: CC BY 3.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: すべて後ろ向き観察研究の統合値
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-02-06-012 (id: JlAKph4)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-003
  domain: RX
  subdomain: 主要症候（胸水）
  assertion:
    plain_statement_ja: BTS 2023 では、胸水/血清の蛋白比が0.5を超える、胸水/血清の LDH 比が0.6を超える、胸水 LDH が血清 LDH の基準上限の3分の2を超える、のいずれか1つを満たせば滲出性胸水とする（Light の基準）。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: Light の基準は3項目すべてを満たしたときに滲出性と判定する
  provenance:
    source_ref: SRC-485
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143.full.pdf
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: BTS 2023 の推奨文の要旨（英国）。日本の気胸・胸水診療の指針（日本気胸・囊胞性肺疾患学会など）は今回確認していない。表から読み取り（診断の流れ図の表）。Light の原著（Ann Intern Med 1972）は取得できなかった
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-018 (id: JlAKpiI)；TBL-02-06-020 (id: JlAKpiQ)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-004
  domain: RX
  subdomain: 主要症候（胸水）
  assertion:
    plain_statement_ja: BTS 2023 は、胸腔穿刺は合併症を減らすため常に画像ガイド下で行い（Strong – by consensus）、盲目的な胸膜生検は行わない（Strong – by consensus）とした。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-485
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143.full.pdf
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: BTS 2023 の推奨文の要旨（英国）。日本の気胸・胸水診療の指針（日本気胸・囊胞性肺疾患学会など）は今回確認していない
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-020 (id: JlAKpiQ)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-005
  domain: RX
  subdomain: 主要症候（胸水）
  assertion:
    plain_statement_ja: BTS 2023 は、胸水の原因として心不全を支持するために血清 NT-proBNP の測定を考慮し、ループス胸膜炎には抗核抗体、結核の多い地域では結核性胸水の診断に胸水 ADA や IFN-γ の測定を考慮できるとした（いずれも Conditional）。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-485
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143.full.pdf
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use.
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: BTS 2023 の推奨文の要旨（英国）。日本の気胸・胸水診療の指針（日本気胸・囊胞性肺疾患学会など）は今回確認していない
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-020 (id: JlAKpiQ)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-006
  domain: RX
  subdomain: 呼吸機能検査
  assertion:
    plain_statement_ja: ERS/ATS 2022 は、閉塞性換気障害を FEV1/FVC が正常下限（LLN、5パーセンタイル、zスコア−1.645）を下回ることで定義し、健常者の基準範囲には GLI の参照式を使うとした。
    condition:
      guideline: ERS/ATS technical standard on interpretive strategies 2022
      region: 欧米
    differential: null
    common_misconception: 閉塞性換気障害はどの年齢でも FEV1/FVC 70% 未満で一律に判定される
  provenance:
    source_ref: SRC-501
    source: Stanojevic S, Kaminsky DA, Miller MR, et al. ERS/ATS technical standard on interpretive strategies for routine lung function tests. Eur Respir J 2022;60(1):2101499
    doi: 10.1183/13993003.01499-2021
    pmid: null
    pmcid: null
    url: https://publications.ersnet.org/content/erj/60/1/2101499
    source_license: 未確認（頁に PDF Permissions のリンクのみ）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ERS/ATS 2022 の記載（欧米の基準、GLI 参照式による LLN）。日本呼吸器学会の基準（1秒率70%未満、%VC 80%未満など）や日本人の参照式（LMS 法）とは判定方法が異なる。日本の基準の出典は未取得
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-021 (id: JlAKpiU)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-007
  domain: RX
  subdomain: 呼吸機能検査
  assertion:
    plain_statement_ja: ERS/ATS 2022 は、呼吸機能の低下の程度を zスコアで、−1.65〜−2.5を軽度、−2.51〜−4.0を中等度、−4.1未満を高度とした。
    condition:
      guideline: ERS/ATS technical standard on interpretive strategies 2022
      region: 欧米
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-501
    source: Stanojevic S, Kaminsky DA, Miller MR, et al. ERS/ATS technical standard on interpretive strategies for routine lung function tests. Eur Respir J 2022;60(1):2101499
    doi: 10.1183/13993003.01499-2021
    pmid: null
    pmcid: null
    url: https://publications.ersnet.org/content/erj/60/1/2101499
    source_license: 未確認（頁に PDF Permissions のリンクのみ）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ERS/ATS 2022 の記載（欧米の基準、GLI 参照式による LLN）。日本呼吸器学会の基準（1秒率70%未満、%VC 80%未満など）や日本人の参照式（LMS 法）とは判定方法が異なる。日本の基準の出典は未取得。−4.0 と −4.1 の間は原文の区切りのとおり
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-021 (id: JlAKpiU)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-008
  domain: RX
  subdomain: 呼吸機能検査
  assertion:
    plain_statement_ja: ERS/ATS 2022 は、気管支拡張薬への反応陽性を、FEV1 または FVC の変化量が予測値の10%を超える場合とした。これは吸入前後の値どうしの10%の変化とは異なる。
    condition:
      guideline: ERS/ATS technical standard on interpretive strategies 2022
      region: 欧米
    differential: null
    common_misconception: 気管支拡張薬への反応は、吸入前の値から12%かつ200 mL以上の改善で判定するのが現在の ERS/ATS の基準である
  provenance:
    source_ref: SRC-501
    source: Stanojevic S, Kaminsky DA, Miller MR, et al. ERS/ATS technical standard on interpretive strategies for routine lung function tests. Eur Respir J 2022;60(1):2101499
    doi: 10.1183/13993003.01499-2021
    pmid: null
    pmcid: null
    url: https://publications.ersnet.org/content/erj/60/1/2101499
    source_license: 未確認（頁に PDF Permissions のリンクのみ）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ERS/ATS 2022 の記載（欧米の基準、GLI 参照式による LLN）。日本呼吸器学会の基準（1秒率70%未満、%VC 80%未満など）や日本人の参照式（LMS 法）とは判定方法が異なる。日本の基準の出典は未取得
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-021 (id: JlAKpiU)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-009
  domain: RX
  subdomain: 呼吸機能検査
  assertion:
    plain_statement_ja: ERS/ATS 2022 では、拘束性障害は全肺気量（TLC）が正常下限を下回ることで定義し、FVC の低下だけでは拘束性とはいえない。FEV1/FVC は正常で FEV1 や FVC が低く TLC が正常のパターンは PRISm（preserved ratio impaired spirometry）と呼ばれる。
    condition:
      guideline: ERS/ATS technical standard on interpretive strategies 2022
      region: 欧米
    differential: null
    common_misconception: '%VC が低ければ拘束性障害と確定できる'
  provenance:
    source_ref: SRC-501
    source: Stanojevic S, Kaminsky DA, Miller MR, et al. ERS/ATS technical standard on interpretive strategies for routine lung function tests. Eur Respir J 2022;60(1):2101499
    doi: 10.1183/13993003.01499-2021
    pmid: null
    pmcid: null
    url: https://publications.ersnet.org/content/erj/60/1/2101499
    source_license: 未確認（頁に PDF Permissions のリンクのみ）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ERS/ATS 2022 の記載（欧米の基準、GLI 参照式による LLN）。日本呼吸器学会の基準（1秒率70%未満、%VC 80%未満など）や日本人の参照式（LMS 法）とは判定方法が異なる。日本の基準の出典は未取得
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-021 (id: JlAKpiU)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-010
  domain: RX
  subdomain: 呼吸機能検査
  assertion:
    plain_statement_ja: ERS/ATS 2022 は、肺拡散能（DLCO）を5〜95パーセンタイルの範囲で判定し、低下時は肺胞気量（VA）と KCO を合わせて評価するとした。VA が正常で DLCO が低ければ肺血管の障害、肺気量の保たれた肺気腫、貧血を考え、基準値はヘモグロビンで補正する。
    condition:
      guideline: ERS/ATS technical standard on interpretive strategies 2022
      region: 欧米
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-501
    source: Stanojevic S, Kaminsky DA, Miller MR, et al. ERS/ATS technical standard on interpretive strategies for routine lung function tests. Eur Respir J 2022;60(1):2101499
    doi: 10.1183/13993003.01499-2021
    pmid: null
    pmcid: null
    url: https://publications.ersnet.org/content/erj/60/1/2101499
    source_license: 未確認（頁に PDF Permissions のリンクのみ）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ERS/ATS 2022 の記載（欧米の基準、GLI 参照式による LLN）。日本呼吸器学会の基準（1秒率70%未満、%VC 80%未満など）や日本人の参照式（LMS 法）とは判定方法が異なる。日本の基準の出典は未取得
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-021 (id: JlAKpiU)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-011
  domain: RX
  subdomain: 呼気NO
  assertion:
    plain_statement_ja: ATS 2011 の指針は、呼気 NO（FeNO）が成人で25 ppb未満（小児20 ppb未満）なら好酸球性気道炎症と副腎皮質ステロイドへの反応の可能性は低く、50 ppbを超える（小児35 ppb超）なら好酸球性炎症の可能性が高いとした（強い推奨、中等度の質）。25〜50 ppbは臨床状況に照らして慎重に解釈する。
    condition:
      guideline: 'ATS clinical practice guideline: FENO 2011'
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-502
    source: 'Dweik RA, Boggs PB, Erzurum SC, et al. An official ATS clinical practice guideline: interpretation of exhaled nitric oxide levels (FENO) for clinical applications. Am J Respir Crit Care Med 2011;184:602-615'
    doi: null
    pmid: null
    pmcid: null
    url: https://THORACIC.ORG/statements/resources/allergy-asthma/feno-document.pdf
    source_license: 取得範囲に表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 米国の指針。日本の喘息診断に用いる目安（日本アレルギー学会など）は出典を取得できず未作成。DOI は PDF の表記と既知の形式が一致せず、API で確定する
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-022 (id: JvVZg-4)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-012
  domain: RX
  subdomain: 呼気NO
  assertion:
    plain_statement_ja: ATS 2011 の指針では、FeNO の有意な上昇を、50 ppbを超える値では20%を超える増加、50 ppb未満では10 ppbを超える増加とした（弱い推奨、低い質）。喫煙者は FeNO が低く、アトピーのある人は高い傾向がある。
    condition:
      guideline: 'ATS clinical practice guideline: FENO 2011'
      region: 米国
    differential: null
    common_misconception: 喫煙者では FeNO が高くなる
  provenance:
    source_ref: SRC-502
    source: 'Dweik RA, Boggs PB, Erzurum SC, et al. An official ATS clinical practice guideline: interpretation of exhaled nitric oxide levels (FENO) for clinical applications. Am J Respir Crit Care Med 2011;184:602-615'
    doi: null
    pmid: null
    pmcid: null
    url: https://THORACIC.ORG/statements/resources/allergy-asthma/feno-document.pdf
    source_license: 取得範囲に表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 米国の指針
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-022 (id: JvVZg-4)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-013
  domain: RX
  subdomain: 呼気NO
  assertion:
    plain_statement_ja: 日本の4施設の健常成人240人（18〜74歳、現喫煙者とアトピー性疾患の既往がある人を除く）の検討では、FeNO の平均は16.9 ppb、95%予測区間は6.5〜35.0 ppbで、健常成人の上限は約36 ppbと提案された。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-503
    source: Matsunaga K, Hirano T, Kawayama T, et al. Reference Ranges for Exhaled Nitric Oxide Fraction in Healthy Japanese Adult Population. Allergol Int 2010;59(4):363-367
    doi: 10.2332/allergolint.10-OA-0197
    pmid: null
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/allergolint/59/4/59_4_363/_article
    source_license: © 2010 by Japanese Society of Allergology（JOURNAL FREE ACCESS）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 抄録で確認。喘息の診断のためのカットオフを示した研究ではない
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-022 (id: JvVZg-4)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-014
  domain: RX
  subdomain: 気管支鏡
  assertion:
    plain_statement_ja: 日本呼吸器内視鏡学会の全国調査では、超音波気管支鏡ガイド下針生検（EBUS-TBNA）7,345件の合併症の頻度は1.23%で、最も多いのは出血（0.68%）、感染は0.19%、死亡は1例（0.01%）だった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-504
    source: 'Asano F, Aoe M, Ohsaki Y, et al. Complications associated with endobronchial ultrasound-guided transbronchial needle aspiration: a nationwide survey by the Japan Society for Respiratory Endoscopy. Respir Res 2013;14:50'
    doi: 10.1186/1465-9921-14-50
    pmid: null
    pmcid: null
    url: https://www.springermedicine.com/complications-associated-with-endobronchial-ultrasound-guided-tr/22347198
    source_license: Open Access の表示のみ（CC の版は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認。通常の気管支鏡検査（経気管支生検など）の合併症の全国調査は未取得
  curriculum:
    core_curriculum: 'PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-024 (id: JlAKpic)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-015
  domain: RX
  subdomain: 酸素療法
  assertion:
    plain_statement_ja: BTS 2017 は、急性疾患の多くの患者で SpO2 の目標を94〜98%、高二酸化炭素性呼吸不全のリスクがある患者では88〜92%とし、酸素は薬剤として処方して投与すべきものとした。
    condition:
      guideline: BTS Guideline for oxygen use in adults in healthcare and emergency settings 2017
      region: 英国
    differential: null
    common_misconception: COPD などで高二酸化炭素血症のリスクがあっても、SpO2 は100%近くを目標にする
  provenance:
    source_ref: SRC-505
    source: 'British Thoracic Society. BTS Guideline for oxygen use in adults in healthcare and emergency settings, Web Appendix 3: Summary of guideline for hospital use（2017年5月）. 本体は O''Driscoll BR, et al. Thorax 2017;72(Suppl 1):i1-i89'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.brit-thoracic.org.uk/document-library/guidelines/emergency-oxygen/web-appendix-3-summary-of-guideline-for-hospital-use
    source_license: 取得範囲に表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: BTS の要約頁（Web Appendix 3）で確認。高二酸化炭素性呼吸不全のリスクがある疾患の一覧は要約頁にない。本体の DOI は未確認
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-02-06-026 (id: JlAKpik)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-016
  domain: RX
  subdomain: 酸素療法
  assertion:
    plain_statement_ja: 日本の在宅酸素療法の保険適用の対象には、高度慢性呼吸不全で動脈血酸素分圧が55 mmHg以下の人と、60 mmHg以下で睡眠時または運動負荷時に著しい低酸素血症を来す人が含まれる。
    condition:
      guideline: 診療報酬 C103 在宅酸素療法指導管理料
      region: 日本
    differential: null
    common_misconception: 在宅酸素療法は SpO2 が90%を下回れば誰でも保険で導入できる
  provenance:
    source_ref: SRC-506
    source: 厚生労働省. 平成20年度診療報酬改定 告示・通知（在宅医療：C103 在宅酸素療法指導管理料、C107-2 在宅持続陽圧呼吸療法指導管理料）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/topics/2008/03/dl/tp0305-1d_0008.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 平成20年度の告示・通知で確認。2024年の東北厚生局資料の抽出では「50 mmHg 以下」と読み取られたが、抽出時の誤りと考えられる。現行（令和6年度）の留意事項通知との照合が要る。肺高血圧症・慢性心不全・チアノーゼ型先天性心疾患などの対象は主張文に含めていない
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-02-06-026 (id: JlAKpik)；TBL-01-00-203 (id: Jlvnlw8)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-017
  domain: RX
  subdomain: 人工呼吸
  assertion:
    plain_statement_ja: ERS/ATS 2017 は、COPD 増悪で急性または慢性の急性増悪による呼吸性アシドーシス（pH 7.35以下）を来した場合に bilevel の非侵襲的陽圧換気（NIV）を推奨し（強い推奨、高い確実性）、アシドーシスのない高二酸化炭素血症には NIV を使わないことを提案した（条件付き、低い確実性）。
    condition:
      guideline: 'ERS/ATS clinical practice guidelines: NIV for acute respiratory failure 2017'
      region: 欧米
    differential: null
    common_misconception: COPD 増悪で PaCO2 が高ければ、pH が正常でも NIV を始める
  provenance:
    source_ref: SRC-507
    source: 'Rochwerg B, Brochard L, Elliott MW, et al. Official ERS/ATS clinical practice guidelines: noninvasive ventilation for acute respiratory failure. Eur Respir J 2017;50:1602426'
    doi: 10.1183/13993003.02426-2016
    pmid: null
    pmcid: null
    url: https://member.thoracic.org/statements/resources/cc/niv-guidelines.pdf
    source_license: ©ERS 2017
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 欧米の指針。日本の NPPV ガイドライン（日本呼吸器学会）は未確認
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-02-06-027 (id: JlAKpio)；TBL-01-00-215 (id: JlvnlyE)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-018
  domain: RX
  subdomain: 人工呼吸
  assertion:
    plain_statement_ja: ERS/ATS 2017 は、心原性肺水腫による急性呼吸不全に bilevel NIV か CPAP を推奨した（強い推奨、中等度の確実性）。免疫不全、術後、胸部外傷、終末期の呼吸困難では NIV を提案し（条件付き）、それ以外の新規発症の低酸素性呼吸不全には推奨を示さなかった。
    condition:
      guideline: 'ERS/ATS clinical practice guidelines: NIV for acute respiratory failure 2017'
      region: 欧米
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-507
    source: 'Rochwerg B, Brochard L, Elliott MW, et al. Official ERS/ATS clinical practice guidelines: noninvasive ventilation for acute respiratory failure. Eur Respir J 2017;50:1602426'
    doi: 10.1183/13993003.02426-2016
    pmid: null
    pmcid: null
    url: https://member.thoracic.org/statements/resources/cc/niv-guidelines.pdf
    source_license: ©ERS 2017
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 欧米の指針。心原性肺水腫の鑑別・画像は第12回（PV）、心不全の治療は循環器 HF の範囲
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-02-06-027 (id: JlAKpio)'
    kokushi: 医学各論 Ⅳ-5-A-①（心原性肺水腫、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-019
  domain: RX
  subdomain: 人工呼吸
  assertion:
    plain_statement_ja: ERS/ATS 2017 は、抜管後の呼吸不全のリスクが高い患者の予防に NIV を提案した（条件付き、低い確実性）一方、抜管後にすでに呼吸不全を来した患者には NIV を使わないことを提案した（条件付き、低い確実性）。高二酸化炭素性呼吸不全の患者の人工呼吸からの離脱を早める目的でも NIV を提案している。
    condition:
      guideline: 'ERS/ATS clinical practice guidelines: NIV for acute respiratory failure 2017'
      region: 欧米
    differential: null
    common_misconception: 抜管後に呼吸不全を来したら、再挿管の前にまず NIV を試みるのが推奨されている
  provenance:
    source_ref: SRC-507
    source: 'Rochwerg B, Brochard L, Elliott MW, et al. Official ERS/ATS clinical practice guidelines: noninvasive ventilation for acute respiratory failure. Eur Respir J 2017;50:1602426'
    doi: 10.1183/13993003.02426-2016
    pmid: null
    pmcid: null
    url: https://member.thoracic.org/statements/resources/cc/niv-guidelines.pdf
    source_license: ©ERS 2017
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 欧米の指針
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-02-06-027 (id: JlAKpio)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-020
  domain: RX
  subdomain: 呼吸リハビリテーション
  assertion:
    plain_statement_ja: ATS 2023 の指針は、安定期の COPD、増悪で入院した後の COPD、間質性肺疾患の成人に呼吸リハビリテーションを強く推奨し（中等度の質）、肺高血圧症には条件付きで提案した（低い質）。施設型と遠隔リハビリテーションのどちらかを選べるようにすることも強く推奨した。
    condition:
      guideline: 'ATS clinical practice guideline: Pulmonary Rehabilitation 2023'
      region: 米国
    differential: null
    common_misconception: 間質性肺疾患では呼吸リハビリテーションの効果は期待できない
  provenance:
    source_ref: SRC-508
    source: 'Rochester CL, Alison JA, Carlin B, et al. Pulmonary Rehabilitation for Adults with Chronic Respiratory Disease: An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med 2023;208(4):e7-e26'
    doi: null
    pmid: null
    pmcid: null
    url: https://documentserver.uhasselt.be/bitstream/1942/41607/1/Pulmonary%20Rehabilitation%20for%20Adults%20with%20Chronic%20Respiratory%20Disease_%20An%20Official%20American%20Thoracic%20Society%20Clinical%20Practice%20Guideline.pdf
    source_license: Copyright © 2023 by the American Thoracic Society
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国の指針。肺癌の切除前後と肺移植は指針の範囲外。COPD の呼吸リハビリテーションの詳細は第11回（RO）の範囲。DOI は本文に記載がなく未確認
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)；TBL-02-06-025 (id: JlAKpig)；TBL-01-00-215 (id: JlvnlyE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-021
  domain: RX
  subdomain: 喫煙と禁煙治療
  assertion:
    plain_statement_ja: 令和4年の国民健康・栄養調査では、20歳以上で習慣的に喫煙している人の割合は14.8%（男性24.8%、女性6.2%）で、平成22年（19.5%、男性32.2%、女性8.4%）から減り、直近10年間で男女とも有意に減少した。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-509
    source: 厚生労働省. 令和4年国民健康・栄養調査結果の概要（2024年8月28日公表）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10901000/001325269.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 令和4年の調査。令和5年以降の調査で喫煙の項目が公表されているかは未確認。加熱式たばこの使用割合はこの資料に記載がない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-022
  domain: RX
  subdomain: 喫煙と禁煙治療
  assertion:
    plain_statement_ja: 令和4年の国民健康・栄養調査では、受動喫煙の機会がある人の割合は平成15年以降、家庭・職場・学校・飲食店のいずれでも有意に減っており、家庭では平成15年の22.0%から令和4年の4.7%になった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-509
    source: 厚生労働省. 令和4年国民健康・栄養調査結果の概要（2024年8月28日公表）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10901000/001325269.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 令和4年の調査
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-023
  domain: RX
  subdomain: 喫煙と禁煙治療
  assertion:
    plain_statement_ja: 禁煙治療の保険算定（ニコチン依存症管理料）の対象は、ニコチン依存症のスクリーニングテスト（TDS）でニコチン依存症と診断され、すぐに禁煙を希望して文書で治療に同意した人で、35歳以上では喫煙指数（1日の本数×年数）200以上も要件となる。平成28年度の改定で、35歳未満では喫煙指数の要件がなくなった。
    condition:
      guideline: 診療報酬 B001-3-2 ニコチン依存症管理料
      region: 日本
    differential: null
    common_misconception: 禁煙治療を保険で受けるには、年齢にかかわらず喫煙指数200以上が必要である
  provenance:
    source_ref: SRC-510
    source: 厚生労働省. 中央社会保険医療協議会 検-4-2参考「平成28年度診療報酬改定 重症化予防の取組の推進②（ニコチン依存症管理料の対象患者の拡大）」（平成29年11月10日）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/file/05-Shingikai-12404000-Hokenkyoku-Iryouka/0000184204.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 平成28年度改定時点の中医協資料。TDS の判定点数（5点以上）は資料に記載がなく主張文に含めていない。令和6年度改定後の要件、加熱式たばこの扱い、バレニクリンの供給状況は未確認
  curriculum:
    core_curriculum: 'PS-02-07-04 (id: JkxnuRA)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-024
  domain: RX
  subdomain: 呼吸器疾患の統計
  assertion:
    plain_statement_ja: 令和6年（2024年）の人口動態統計では、肺炎が死因の第5位（80,176人、人口10万対66.6）、誤嚥性肺炎が第6位（63,667人、52.9）、新型コロナウイルス感染症が第8位（35,865人）だった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 肺炎と誤嚥性肺炎は人口動態統計で同じ死因として合算されている
  provenance:
    source_ref: SRC-299
    source: 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第8表 性別にみた死因順位（第10位まで）別死亡数・死亡率（人口10万対）・構成割合
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/kakutei24/dl/10_h8.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 表から読み取り。令和7年の確定数は2026年9月30日に公表されたが、死因別の死亡率などの詳細は2026年11月公表予定とされ、今回は令和6年の値を使った
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-212 (id: Jlvnlx0)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RX-025
  domain: RX
  subdomain: 呼吸器疾患の統計
  assertion:
    plain_statement_ja: 令和6年（2024年）の人口動態統計では、間質性肺疾患が男性の死因の第10位で、死亡数は16,024人（2023年は15,516人）だった。総数と女性の上位10位には入っていない。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-299
    source: 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第8表 性別にみた死因順位（第10位まで）別死亡数・死亡率（人口10万対）・構成割合
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/kakutei24/dl/10_h8.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 表から読み取り。COPD は総数・男女とも上位10位に入っておらず、この表では死亡数を確認できない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応

| ID | subdomain | 出題基準 | コアカリ | 出典 |
|---|---|---|---|---|
| LC-001 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-471 |
| LC-002 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-472 |
| LC-003 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-470 |
| LC-004 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-470 |
| LC-005 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)；TBL-02-06-023 (id: JlAKpiY) | SRC-470 |
| LC-006 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)；TBL-02-06-019 (id: JlAKpiM) | SRC-470 |
| LC-007 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)；TBL-02-06-023 (id: JlAKpiY) | SRC-473 |
| LC-008 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI)；TBL-02-06-023 (id: JlAKpiY) | SRC-473 |
| LC-009 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-474 |
| LC-010 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-474 |
| LC-011 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-474 |
| LC-012 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-475 |
| LC-013 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-475 |
| LC-014 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-475 |
| LC-015 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-04 (id: JkxnuRA)；TBL-01-00-643 (id: JlvnmcI) | SRC-476 |
| LC-016 | 転移性肺腫瘍 | 医学各論 Ⅳ-6-A-②（転移性肺腫瘍、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-645 (id: JlvnmcU) | SRC-477 |
| LC-017 | 転移性肺腫瘍 | 医学各論 Ⅳ-6-A-②（転移性肺腫瘍、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-645 (id: JlvnmcU) | SRC-477 |
| LC-018 | 転移性肺腫瘍 | 医学各論 Ⅳ-6-A-②（転移性肺腫瘍、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-645 (id: JlvnmcU) | SRC-477 |
| LC-019 | 良性肺腫瘍 | 医学各論 Ⅳ-6-B-①（良性肺腫瘍、a） | PS-02-07-05 (id: JkxnuRE)；TBL-02-06-023 (id: JlAKpiY) | SRC-478 |
| LC-020 | 良性肺腫瘍 | 医学各論 Ⅳ-6-B-①（良性肺腫瘍、a） | PS-02-07-05 (id: JkxnuRE)；TBL-02-06-023 (id: JlAKpiY) | SRC-478 |
| LC-021 | 神経原性腫瘍 | 医学各論 Ⅳ-6-C-③（神経原性腫瘍、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)；TBL-02-06-023 (id: JlAKpiY) | SRC-479 |
| LC-022 | 縦隔腫瘍 | 医学各論 Ⅳ-6-C-①（悪性リンパ腫、a）；医学各論 Ⅳ-6-C-②（胸腺腫瘍、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY) | SRC-479 |
| LC-023 | 胚細胞腫瘍 | 医学各論 Ⅳ-6-C-⑤（胚細胞腫瘍、c） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY) | SRC-479 |
| LC-024 | 囊胞性腫瘍 | 医学各論 Ⅳ-6-C-④（囊胞性腫瘍、b）；医学各論 Ⅳ-6-C-②（胸腺腫瘍、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)；TBL-02-06-023 (id: JlAKpiY) | SRC-479 |
| LC-025 | 胸腺腫瘍 | 医学各論 Ⅳ-6-C-②（胸腺腫瘍、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY) | SRC-480 |
| LC-026 | 胸腺腫瘍 | 医学各論 Ⅳ-6-C-②（胸腺腫瘍、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY) | SRC-480 |
| LC-027 | 胸腺腫瘍 | 医学各論 Ⅳ-6-C-②（胸腺腫瘍、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY) | SRC-480 |
| LC-028 | 胸腺腫瘍 | 医学各論 Ⅳ-6-C-②（胸腺腫瘍、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY) | SRC-480 |
| LC-029 | 胸膜中皮腫 | 医学各論 Ⅳ-6-D-①（胸膜中皮腫、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-644 (id: JlvnmcM) | SRC-481 |
| LC-030 | 胸膜中皮腫 | 医学各論 Ⅳ-6-D-①（胸膜中皮腫、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-644 (id: JlvnmcM) | SRC-482 |
| LC-031 | 肺癌 | 医学各論 Ⅳ-6-A-①（肺癌、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-643 (id: JlvnmcI) | SRC-482 |
| LC-032 | 胸膜中皮腫 | 医学各論 Ⅳ-6-D-①（胸膜中皮腫、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-644 (id: JlvnmcM) | SRC-483 |
| LC-033 | 癌性胸膜炎 | 医学各論 Ⅳ-6-E（癌性胸膜炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-02-06-018 (id: JlAKpiI) | SRC-484 |
| LC-034 | 癌性胸膜炎 | 医学各論 Ⅳ-6-E（癌性胸膜炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-02-06-018 (id: JlAKpiI)；TBL-02-06-020 (id: JlAKpiQ) | SRC-484 |
| LC-035 | 癌性胸膜炎 | 医学各論 Ⅳ-6-E（癌性胸膜炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-02-06-018 (id: JlAKpiI) | SRC-485 |
| LC-036 | 癌性胸膜炎 | 医学各論 Ⅳ-6-E（癌性胸膜炎、a） | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-020 (id: JlAKpiQ) | SRC-485 |
| LC-037 | 癌性リンパ管症 | 医学各論 Ⅳ-6-F（癌性リンパ管症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-02-06-023 (id: JlAKpiY) | SRC-486 |
| LC-038 | 癌性リンパ管症 | 医学各論 Ⅳ-6-F（癌性リンパ管症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-02-06-023 (id: JlAKpiY) | SRC-486 |
| PL-001 | 気胸 | 医学各論 Ⅳ-7-A-①（気胸、緊張性気胸、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-241 (id: Jlvnl1A) | SRC-485 |
| PL-002 | 気胸 | 医学各論 Ⅳ-7-A-①（気胸、緊張性気胸、a） | PS-02-07-04 (id: JkxnuRA)；TBL-01-00-241 (id: Jlvnl1A) | SRC-485 |
| PL-003 | 気胸 | 医学各論 Ⅳ-7-A-①（気胸、緊張性気胸、a） | PS-02-07-04 (id: JkxnuRA)；TBL-01-00-241 (id: Jlvnl1A) | SRC-485 |
| PL-004 | 気胸 | 医学各論 Ⅳ-7-A-①（気胸、緊張性気胸、a） | PS-02-07-04 (id: JkxnuRA)；TBL-01-00-241 (id: Jlvnl1A) | SRC-485 |
| PL-005 | 血胸 | 医学各論 Ⅳ-7-A-②（血胸、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-243 (id: Jlvnl1Y) | SRC-494 |
| PL-006 | 乳び胸 | 医学各論 Ⅳ-7-A-③（乳び胸、c） | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-020 (id: JlAKpiQ) | SRC-487 |
| PL-007 | 乳び胸 | 医学各論 Ⅳ-7-A-③（乳び胸、c） | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-020 (id: JlAKpiQ) | SRC-487 |
| PL-008 | 縦隔気腫 | 医学各論 Ⅳ-7-B-①（縦隔気腫、皮下気腫、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-242 (id: Jlvnl1U) | SRC-488 |
| PL-009 | 気管食道瘻 | 医学各論 Ⅳ-7-B-②（気管食道瘻、食道気管瘻、a） | PS-02-07-05 (id: JkxnuRE) | SRC-489 |
| PL-010 | 上大静脈症候群 | 医学各論 Ⅳ-7-B-③（上大静脈症候群、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-196 (id: JlvnlwE) | SRC-484 |
| PL-011 | 上大静脈症候群 | 医学各論 Ⅳ-7-B-③（上大静脈症候群、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-196 (id: JlvnlwE)；TBL-02-06-023 (id: JlAKpiY) | SRC-484 |
| PL-012 | 上大静脈症候群 | 医学各論 Ⅳ-7-B-③（上大静脈症候群、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-196 (id: JlvnlwE) | SRC-484 |
| PL-013 | 上大静脈症候群 | 医学各論 Ⅳ-7-B-③（上大静脈症候群、a） | PS-02-07-04 (id: JkxnuRA)；TBL-01-00-196 (id: JlvnlwE) | SRC-484 |
| PL-014 | 反回神経麻痺 | 医学各論 Ⅳ-7-B-④（反回神経麻痺、a） | PS-02-07-05 (id: JkxnuRE) | SRC-490 |
| PL-015 | 肋骨骨折 | 医学各論 Ⅳ-7-C-①（肋骨骨折、a） | PS-02-07-05 (id: JkxnuRE) | SRC-491 |
| PL-016 | 肋骨骨折 | 医学各論 Ⅳ-7-C-①（肋骨骨折、a） | PS-02-07-04 (id: JkxnuRA) | SRC-491 |
| PL-017 | 胸郭変形 | 医学各論 Ⅳ-7-C-②（胸郭変形、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-245 (id: Jlvnl1s) | SRC-492 |
| PL-018 | 横隔膜ヘルニア | 医学各論 Ⅳ-7-C-③（横隔膜ヘルニア、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-247 (id: Jlvnl14) | SRC-493 |
| PL-019 | 睡眠時無呼吸症候群 | 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-233 (id: Jlvnl0I)；TBL-02-06-021 (id: JlAKpiU) | SRC-495 |
| PL-020 | 睡眠時無呼吸症候群 | 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-233 (id: Jlvnl0I) | SRC-495 |
| PL-021 | 睡眠時無呼吸症候群 | 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-233 (id: Jlvnl0I) | SRC-495 |
| PL-022 | 睡眠時無呼吸症候群 | 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a） | PS-02-07-04 (id: JkxnuRA)；TBL-01-00-233 (id: Jlvnl0I) | SRC-495 |
| PL-023 | 睡眠時無呼吸症候群 | 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a） | PS-02-07-04 (id: JkxnuRA)；TBL-01-00-233 (id: Jlvnl0I) | SRC-496 |
| PL-024 | 睡眠時無呼吸症候群 | 医学各論 Ⅳ-8-A-①（睡眠時無呼吸症候群、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-233 (id: Jlvnl0I) | SRC-495 |
| PL-025 | 過換気症候群 | 医学各論 Ⅳ-8-A-②（過換気症候群、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-232 (id: Jlvnl0A) | SRC-497 |
| PL-026 | 過換気症候群 | 医学各論 Ⅳ-8-A-②（過換気症候群、a） | PS-02-07-04 (id: JkxnuRA)；TBL-01-00-232 (id: Jlvnl0A) | SRC-498 |
| PL-027 | 肺胞低換気症候群 | 医学各論 Ⅳ-8-A-③（肺胞低換気症候群、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-203 (id: Jlvnlw8)；TBL-01-00-233 (id: Jlvnl0I) | SRC-499 |
| RX-001 | 主要症候（血痰・喀血） | null | PS-02-07-02 (id: JkxnuQ4)；TBL-02-06-012 (id: JlAKph4) | SRC-500 |
| RX-002 | 主要症候（血痰・喀血） | null | PS-02-07-04 (id: JkxnuRA)；TBL-02-06-012 (id: JlAKph4) | SRC-500 |
| RX-003 | 主要症候（胸水） | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-018 (id: JlAKpiI)；TBL-02-06-020 (id: JlAKpiQ) | SRC-485 |
| RX-004 | 主要症候（胸水） | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-020 (id: JlAKpiQ) | SRC-485 |
| RX-005 | 主要症候（胸水） | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-020 (id: JlAKpiQ) | SRC-485 |
| RX-006 | 呼吸機能検査 | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-021 (id: JlAKpiU) | SRC-501 |
| RX-007 | 呼吸機能検査 | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-021 (id: JlAKpiU) | SRC-501 |
| RX-008 | 呼吸機能検査 | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-021 (id: JlAKpiU) | SRC-501 |
| RX-009 | 呼吸機能検査 | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-021 (id: JlAKpiU) | SRC-501 |
| RX-010 | 呼吸機能検査 | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-021 (id: JlAKpiU) | SRC-501 |
| RX-011 | 呼気NO | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-022 (id: JvVZg-4) | SRC-502 |
| RX-012 | 呼気NO | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-022 (id: JvVZg-4) | SRC-502 |
| RX-013 | 呼気NO | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-022 (id: JvVZg-4) | SRC-503 |
| RX-014 | 気管支鏡 | null | PS-02-07-03 (id: JkxnuQ8)；TBL-02-06-024 (id: JlAKpic) | SRC-504 |
| RX-015 | 酸素療法 | null | PS-02-07-04 (id: JkxnuRA)；TBL-02-06-026 (id: JlAKpik) | SRC-505 |
| RX-016 | 酸素療法 | null | PS-02-07-04 (id: JkxnuRA)；TBL-02-06-026 (id: JlAKpik)；TBL-01-00-203 (id: Jlvnlw8) | SRC-506 |
| RX-017 | 人工呼吸 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-04 (id: JkxnuRA)；TBL-02-06-027 (id: JlAKpio)；TBL-01-00-215 (id: JlvnlyE) | SRC-507 |
| RX-018 | 人工呼吸 | 医学各論 Ⅳ-5-A-①（心原性肺水腫、a） | PS-02-07-04 (id: JkxnuRA)；TBL-02-06-027 (id: JlAKpio) | SRC-507 |
| RX-019 | 人工呼吸 | null | PS-02-07-04 (id: JkxnuRA)；TBL-02-06-027 (id: JlAKpio) | SRC-507 |
| RX-020 | 呼吸リハビリテーション | null | PS-02-07-04 (id: JkxnuRA)；TBL-02-06-025 (id: JlAKpig)；TBL-01-00-215 (id: JlvnlyE)；TBL-01-00-218 (id: JlvnlyY) | SRC-508 |
| RX-021 | 喫煙と禁煙治療 | null | PS-02-07-05 (id: JkxnuRE) | SRC-509 |
| RX-022 | 喫煙と禁煙治療 | null | PS-02-07-05 (id: JkxnuRE) | SRC-509 |
| RX-023 | 喫煙と禁煙治療 | null | PS-02-07-04 (id: JkxnuRA) | SRC-510 |
| RX-024 | 呼吸器疾患の統計 | null | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-212 (id: Jlvnlx0) | SRC-299 |
| RX-025 | 呼吸器疾患の統計 | null | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-218 (id: JlvnlyY) | SRC-299 |

- 出題基準の番号が付いたカード：67/90件。番号がないのは RX のうち症候・検査・治療・統計のカード（コアカリは別表2-6 の番号を付けた）。
- RX-017（COPD 増悪の NIV）は Ⅳ-2-C-①、RX-018（心原性肺水腫の NIV）は Ⅳ-5-A-① に付けました。
## 4. 未解決事項（担当の目安つき）

| # | 内容 | 該当 | 担当の目安 |
|---|---|---|---|
| 1 | PMID・PMCID・DOI の確定。PMID が入っているのは SRC-473（21714641）、474（41154348）、487（7442324）、498（2499228）だけ。DOI が null の SRC-473・475・491・502・505・508 は API で確定する（SRC-502 は PDF の表記「rccm.912011ST」が通常の DOI 形式と合わない） | 全 SRC | Claude Code（Phase 3） |
| 2 | ライセンスが UNKNOWN の出典（SRC-471・473・476・477・487・491・498・501・502・504・505）の Crossref license 欄の確認。SRC-504（Respir Res）は CC の版を確定する | 11件 | Claude Code |
| 3 | 著者名の確定：SRC-487（Staats ほか、PubMed 頁に著者の表示なし）、SRC-491（EAST 2017 の題名と第4著者以降）、SRC-501（著者順） | 3件 | Claude Code |
| 4 | 肺癌の薬物療法と手術のカードが不足。KEYNOTE-024（PD-L1 高発現へのペムブロリズマブ）、PACIFIC（化学放射線療法後のデュルバルマブ）、JCOG0802（区域切除と肺葉切除）、ALK などほかのドライバー遺伝子、小細胞肺癌の治療は本文を取得できず未作成。日本肺癌学会の診療ガイドライン2024年版（第8版、Minds では「旧版」表示）の後継版の有無と、英語版の DOI も未確認 | LC | 次回（補完）／呼吸器内科医 |
| 5 | 分子標的薬・免疫チェックポイント阻害薬の国内承認と保険適用（オシメルチニブを含む）は未確認 | LC-015 | Claude Code → 呼吸器内科医 |
| 6 | 胸膜中皮腫の治療（CheckMate 743 のニボルマブ＋イピリムマブ、ペメトレキセド＋シスプラチン）と、石綿ばく露から発症までの潜伏期間の数値は出典を取れず未作成 | Ⅳ-6-D-① | 次回（補完） |
| 7 | TNM 第9版は解説論文（SRC-474、CC BY）で作った。IASLC の原提案（J Thorac Oncol 2024）と、日本の肺癌取扱い規約の対応版で照合する | LC-009〜011 | Claude Code |
| 8 | 肺がん検診ガイドライン2025年度版（SRC-470）は国立がん研究センターのプレスリリースで確認しただけで、本文（推奨の根拠・不利益）は未確認。厚生労働省のがん検診の指針への反映状況も確認する | LC-003〜006 | Claude Code |
| 9 | 在宅酸素療法の PaO2 の基準（55 mmHg 以下）は平成20年の通知で確認した。2024年の東北厚生局資料からの抽出では「50 mmHg 以下」と読み取られたため、現行の留意事項通知の原文で確認する。CPAP の算定要件（PL-023）も点数表の原文と照合する | RX-016、PL-023 | Claude Code |
| 10 | 禁煙治療（RX-023）は平成28年度改定時点の資料。令和6年度改定後の要件、TDS の判定点数、加熱式たばこの扱い、バレニクリンの供給再開の状況を確認する（ニュースサイトは照合の手がかりにのみ使う） | RX-023 | Claude Code |
| 11 | 喫煙率（RX-021・022）は令和4年の調査。令和5年以降の国民健康・栄養調査で喫煙の項目が公表されていれば差し替える | RX-021・022 | Claude Code |
| 12 | RX の未作成項目：咳嗽の持続期間による分類（日本呼吸器学会 咳嗽・喀痰の診療ガイドライン。2025年に第2版が出ている可能性あり）、呼吸困難（mMRC）、喘鳴、スパイロメトリーの実施基準（ATS/ERS 2019）と日本の判定基準・参照式、動脈血液ガスと酸塩基平衡、胸部画像の基本用語（Fleischner 用語集 2024）、肺結節の扱い（Fleischner 2017）、人工呼吸の離脱 | RX | 次回（補完） |
| 13 | PL の定義だけのカード（MeSH）に、頻度・診断・治療のカードを足す：外傷性血胸の排液と手術の適応（EAST 2011）、自然縦隔気腫の経過、悪性の気管食道瘻のステント治療（ESGE 2021）、反回神経麻痺の左右差と原因、漏斗胸の重症度と手術、外傷性横隔膜ヘルニア、肥満低換気症候群の診断基準と治療（ATS 2019）、過換気症候群の診断 | PL-005・008・009・014・017・018・025・027 | 次回（補完） |
| 14 | 石綿健康被害救済制度（LC-032）は第12回（IL）の石綿肺・石綿健康被害のカードと重なる可能性がある。両回の取り込み後に重複を確認し、片方を `retired` にするか判断する | LC-032 | ユーザー |
| 15 | 胸腺上皮性腫瘍の WHO 分類は PDQ の記載（第4版、2015年）による。第5版（2021年）での変更点は未確認 | LC-027 | 呼吸器外科医・病理医 |

## 5. 次回への引き継ぎ

### 5-1. 欠番

なし（LC-001〜038、PL-001〜027、RX-001〜025 はすべて作成）。SRC-511〜529 は未使用（第13回の補完で使える）。

### 5-2. カードがない出題基準の小項目（第13回の範囲）

- 医学各論 Ⅳ-6-B-②（気管・気管支腫瘍、c）
- 医学各論 Ⅳ-7-C-④（横隔神経麻痺、c）
- 医学各論 Ⅳ-7-C-⑤（横隔膜弛緩症、c）
- 定義（MeSH）のカードだけの小項目：Ⅳ-7-A-②（血胸）、Ⅳ-7-B-①（縦隔気腫、皮下気腫。皮下気腫のカードはない）、Ⅳ-7-B-②（気管食道瘻）、Ⅳ-7-B-④（反回神経麻痺）、Ⅳ-7-C-②（胸郭変形）、Ⅳ-7-C-③（横隔膜ヘルニア）、Ⅳ-8-A-③（肺胞低換気症候群）
- レベル a の小項目は、すべて1件以上のカードがある。

### 5-3. 重複を避ける範囲

- 睡眠時無呼吸：PL は診断基準・重症度・有病率・CPAP と口腔内装置の推奨・保険算定・中枢性無呼吸の定義を扱った。CPAP の降圧効果は循環器 HT-016、心不全に伴うチェーンストークス呼吸の治療（ASV）は循環器 HF の範囲。
- NIV：RX は ERS/ATS 2017 の適応（COPD 増悪、心原性肺水腫、抜管後など）を扱った。COPD 増悪の治療全体は第11回（RO）、心原性肺水腫の鑑別と画像は第12回（PV）の範囲。
- 呼吸リハビリテーション：RX は ATS 2023 の疾患横断の推奨だけを扱った。COPD の呼吸リハビリテーションの詳細は第11回（RO）。
- 胸水：RX は Light の基準、画像ガイド下穿刺、補助検査（NT-proBNP・ADA など）を扱った。膿胸・肺炎随伴性胸水の pH 基準と線溶療法（BTS 2023 にある）は第11回（RI）の範囲として作っていない。悪性胸水は LC（Ⅳ-6-E）で扱った。
- 石綿：LC は中皮腫と肺癌の労災認定、中皮腫の死亡数、救済制度の指定疾病を扱った。石綿肺・びまん性胸膜肥厚・じん肺法は第12回（IL）の範囲（LC-032 は重複の確認が要る）。
- 胸腺腫と重症筋無力症：LC は合併の頻度だけを扱った。重症筋無力症の診断と治療は神経（Ⅸ）の範囲。
- 縦隔のリンパ腫：LC は前縦隔の鑑別に含まれることだけを扱った。リンパ腫の各論は血液（Ⅶ）の範囲。
- 先天性の気管食道瘻と先天性横隔膜ヘルニアは小児（Ⅰ）の範囲で、PL では定義だけを扱った。
- 統計：RX は令和6年の人口動態統計（SRC-299）から肺炎・誤嚥性肺炎・間質性肺疾患の死亡を扱った。肺癌の死亡数は LC-001・002。

### 5-4. 扱った出典（再利用するときは同じ SRC 番号を使う）

SRC-470 肺がん検診ガイドライン2025年度版（国立がん研究センターのプレスリリース）、SRC-471 Cancer Statistics in Japan 2025、SRC-472 厚生労働省がん検診啓発サイトの統計、SRC-473 NLST（NEJM 2011）、SRC-474 TNM 第9版の解説論文（Cancers 2025）、SRC-475 IASLC/ATS/ERS 肺腺癌分類 2011、SRC-476 FLAURA 全生存期間（NEJM 2020）、SRC-477 肺転移の外科治療の総説（Dtsch Arztebl Int 2012）、SRC-478 肺過誤腫（CCJM 2014）、SRC-479 前縦隔の画像診断（Mediastinum 2019）、SRC-480 PDQ 胸腺腫・胸腺癌、SRC-481 中皮腫死亡数（令和7年）、SRC-482 石綿による疾病の労災認定（令和5年9月版）、SRC-483 石綿健康被害救済制度の施行状況（環境省、令和4年）、SRC-484 PDQ Cardiopulmonary Syndromes、SRC-485 BTS 胸膜疾患ガイドライン2023、SRC-486 癌性リンパ管症の HRCT（1997）、SRC-487 乳び胸水のリポ蛋白（1980）、SRC-488 MeSH 縦隔気腫、SRC-489 MeSH 気管食道瘻、SRC-490 MeSH 声帯麻痺、SRC-491 EAST 2017 肋骨固定、SRC-492 MeSH 漏斗胸、SRC-493 MeSH 横隔膜ヘルニア、SRC-494 MeSH 血胸、SRC-495 SAS 診療ガイドライン2020（日本語版）、SRC-496 東北厚生局 在宅医療の留意事項（2024）、SRC-497 MeSH 過換気、SRC-498 紙袋再呼吸（Ann Emerg Med 1989）、SRC-499 MeSH 肥満低換気症候群、SRC-500 大量喀血のメタ解析（J Pers Med 2023）、SRC-501 ERS/ATS 呼吸機能検査の解釈 2022、SRC-502 ATS FeNO 2011、SRC-503 日本人健常成人の FeNO 基準範囲（Allergol Int 2010）、SRC-504 EBUS-TBNA の合併症の全国調査（Respir Res 2013）、SRC-505 BTS 酸素療法ガイドライン2017（要約頁）、SRC-506 平成20年度 診療報酬の告示・通知（在宅酸素・CPAP）、SRC-507 ERS/ATS NIV 2017、SRC-508 ATS 呼吸リハビリテーション 2023、SRC-509 令和4年 国民健康・栄養調査、SRC-510 中医協資料 ニコチン依存症管理料（平成28年度改定）。SRC-299 令和6年人口動態統計（第10回から再利用）。

### 5-5. Claude Code での照合時に重点的に確認する点

1. 数値の照合：LC-001（死亡数の表）、LC-028（正岡分類別の生存率）、LC-031（石綿小体の基準）、PL-019（OSA の診断基準の表）、RX-003（Light の基準）、RX-016（在宅酸素の PaO2 基準）、RX-024・025（死因順位）は表から読み取った値。
2. LC-016・018・019・020・023 は総説・症例提示記事の記載（二次資料経由）。一次資料に差し替えられるか確認する。
3. LC-015 のハザード比は抄録と本文で信頼区間の上限が異なる（0.997 と 0.996）。
4. LC-002 と LC-001 で女性の肺癌の死亡順位が異なる（2位と1位）。部位区分（大腸を一括するか）の違いと考えられるが、SRC-472 の元データで確認する。
