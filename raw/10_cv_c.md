# 第10回 循環器（HT・VS・CX）

- 作成日：2026-10-25
- 事実票：87件（HT-001〜HT-020（20件）、VS-001〜VS-046（46件）、CX-001〜CX-021（21件））。欠番なし。全件 `status: draft`、`verifier: null`
- 取り込み：`python scripts/ingest_round.py raw/10_cv_c.md HT,VS,CX`
- 形式：YAML ブロックは1つ、アンカー・マージキー・脚注番号・仮ID・`basis_tag` は使っていません。`schema/fact.schema.json` で検証済みです。
- SRC 番号：SRC-290〜312（第10回の範囲 SRC-290〜349 のうち23件）。
- 範囲：依頼文 docs/tasks/round8_CV.md の第10回。肺血栓塞栓症（呼吸器 Ⅳ）と腸間膜動脈閉塞症（AB）は扱っていません。
- 調査環境の制約：この回の作業環境では PubMed・PMC・Crossref・Europe PMC・nature.com・J-STAGE の一部に直接アクセスできませんでした。識別子は出版社ページ・学会掲載 PDF・検索結果の表示で確認できたものだけを書き、PMID の多くは null です（Phase 3 の API 照合で確定してください）。

## 1. 抽出元ホワイトリスト（新規 SRC-290〜312）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 使用カード数 |
|---|---|---|---|---|---|---|---|
| SRC-290 | Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621 | 10.1253/circj.CJ-22-0794 | 37661428 | 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会） | UNKNOWN | J-STAGE の英語版 HTML（早期公開版）を WebFetch で確認。本文の約10万字（第Ⅰ〜Ⅲ章）まで。PMID は検索結果の PubMed 表題で確認 | 13 |
| SRC-291 | Ohya Y, Sakima A, Arima H, et al. Key highlights of the Japanese Society of Hypertension Guidelines for the management of elevated blood pressure and hypertension 2025 (JSH2025). Hypertens Res 2025 (Epub 2025 Aug 29) | 10.1038/s41440-025-02331-8 | 40877471 | 未確認（nature.com の取得に失敗） | UNKNOWN | 抄録（lifescience.net の書誌ページ）で確認。DOI は nature.com の記事 URL、PMID は書誌ページで確認 | 1 |
| SRC-292 | 有馬久富. 成果報告2 日本高血圧学会での取り組み（成果報告会資料、2026年2月28日）. 国立保健医療科学院 掲載 | — | — | 表示なし | UNKNOWN | 国立保健医療科学院のサイトの PDF（スライド）を WebFetch で確認。ガイドライン本文ではない | 1 |
| SRC-293 | 2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/SGIM Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Circulation 2025 (published online 2025 Aug 14) | 10.1161/CIR.0000000000001356 | — | © American Heart Association（AHA 公式要約ページの表示） | RESTRICTED | AHA 公式の要約ページ（Top Things to Know）で確認。DOI は同ページに記載。ガイドライン本文は未確認 | 5 |
| SRC-294 | Adler GK, Stowasser M, Correa RR, et al. Primary Aldosteronism: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab 2025;110:2453-2495 | 10.1210/clinem/dgaf284 | — | © The Endocrine Society 2025, All rights reserved（出版社ページ） | RESTRICTED | OUP の記事ページを WebFetch で確認 | 6 |
| SRC-295 | Lei Q, Lv Y, Li K, et al. Effects of continuous positive airway pressure on blood pressure in patients with resistant hypertension and obstructive sleep apnea: a systematic review and meta-analysis of six randomized controlled trials. J Bras Pneumol 2017 | — | — | Creative Commons（版の表示なし） | UNKNOWN | 雑誌サイトの記事ページを WebFetch で確認。刊行年は DOAJ の表示（2017年7月）による | 1 |
| SRC-296 | National Library of Medicine. MeSH Descriptor: Hypotension, Orthostatic (D007024) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | MeSH Browser を WebFetch で確認 | 1 |
| SRC-297 | Shen WK, Sheldon RS, Benditt DG, et al. 2017 ACC/AHA/HRS guideline for the evaluation and management of patients with syncope: executive summary. Heart Rhythm 2017;14:e218-e254 | 10.1016/j.hrthm.2017.03.005 | — | © 2017 American College of Cardiology Foundation, AHA, HRS | RESTRICTED | HRS 掲載の刊行版 PDF（executive summary）を WebFetch で確認 | 5 |
| SRC-298 | 厚生労働省. 令和5年国民健康・栄養調査結果の概要（2024年11月公表） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 厚生労働省の PDF を WebFetch で確認（第1章3、第2章1） | 2 |
| SRC-299 | 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第8表 性別にみた死因順位（第10位まで）別死亡数・死亡率（人口10万対）・構成割合 | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 厚生労働省の PDF を WebFetch で確認 | 1 |
| SRC-300 | 厚生労働省. 令和5年（2023）患者調査の概況 | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 厚生労働省の PDF を WebFetch で確認（表7） | 1 |
| SRC-301 | US Preventive Services Task Force. Abdominal Aortic Aneurysm: Screening. Final Recommendation Statement (2019 Dec 10) | — | — | 米国連邦政府の資料（AHRQ が運営する USPSTF のサイト） | GOV_US | USPSTF のサイトを WebFetch で確認 | 3 |
| SRC-302 | MedlinePlus Genetics. Marfan syndrome (last updated 2018 May 1). National Library of Medicine | — | — | 米国連邦政府の著作物（NLM） | GOV_US | MedlinePlus Genetics を WebFetch で確認 | 2 |
| SRC-303 | MedlinePlus Genetics. Raynaud phenomenon (last updated 2018 Mar 1). National Library of Medicine | — | — | 米国連邦政府の著作物（NLM） | GOV_US | MedlinePlus Genetics を WebFetch で確認 | 2 |
| SRC-304 | 日本循環器学会ほか. 血管炎症候群の診療ガイドライン（2017年改訂版）. 2018年3月23日発行、2018年6月29日更新 | — | — | （無断転載を禁ずる）© 日本循環器学会 | RESTRICTED | 日本心臓血管外科学会サイト掲載の PDF を WebFetch で確認（抽出できた本文は約4万字。Buerger 病の章は見出しのみ） | 5 |
| SRC-305 | 厚生労働省. 指定難病 40 高安動脈炎（概要・診断基準等） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 厚生労働省の PDF を WebFetch で確認 | 3 |
| SRC-306 | 厚生労働省. 指定難病 47 バージャー病（概要・診断基準等） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 厚生労働省の PDF を WebFetch で確認 | 3 |
| SRC-307 | 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新 | — | — | （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会 | RESTRICTED | 日本循環器学会サイトの PDF を WebFetch で確認（抽出できたのは本文の前半。間歇性跛行の治療、腎動脈狭窄、Buerger 病の表は未抽出） | 12 |
| SRC-308 | 日本循環器学会ほか. 肺血栓塞栓症および深部静脈血栓症の診断、治療、予防に関するガイドライン（2017年改訂版）. 2018年3月23日発行、2018年12月10日更新 | — | — | （無断転載を禁ずる）© 日本循環器学会 | RESTRICTED | 日本心臓血管外科学会サイト掲載の PDF を WebFetch で確認（抽出できたのは目次と PTE の章。DVT の章本文は未抽出） | 5 |
| SRC-309 | Rautaharju PM, Surawicz B, Gettes LS. AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part IV: the ST segment, T and U waves, and the QT interval. Circulation 2009;119:e241-e250 | 10.1161/CIRCULATIONAHA.108.191096 | — | © 2009 AHA, ACCF, HRS | RESTRICTED | HRS 掲載の刊行版 PDF を WebFetch で確認 | 3 |
| SRC-310 | Surawicz B, Childers R, Deal BJ, et al. AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part III: intraventricular conduction disturbances. Circulation 2009;119:e235-e240 | 10.1161/CIRCULATIONAHA.108.191095 | — | © 2009 AHA, ACCF, HRS | RESTRICTED | HRS 掲載の刊行版 PDF を WebFetch で確認 | 3 |
| SRC-311 | Lang RM, Badano LP, Mor-Avi V, et al. Recommendations for cardiac chamber quantification by echocardiography in adults: an update from the American Society of Echocardiography and the European Association of Cardiovascular Imaging. J Am Soc Echocardiogr 2015;28:1-39 | 10.1016/j.echo.2014.10.003 | — | Copyright 2015 by the American Society of Echocardiography | RESTRICTED | ASE 掲載の日本語訳 PDF を WebFetch で確認（DOI は同 PDF に記載）。英語原本の書誌は API で確定する | 4 |
| SRC-312 | 日本循環器学会・日本心臓リハビリテーション学会ほか. 心血管疾患におけるリハビリテーションに関するガイドライン（2021年改訂版）. 2021年3月27日発行 | — | — | （無断転載を禁ずる）© 日本循環器学会・日本心臓リハビリテーション学会 | RESTRICTED | 日本心臓リハビリテーション学会サイトの PDF を WebFetch で確認（抽出できたのは本文の一部。表の数値は一部未抽出） | 5 |

- legal_basis は全件 B（出典の事実・数値を自作文で記述）です。表・図・原文の言い回しは使っていません。
- 日本の学会ガイドラインのうち、学会サイト掲載の日本語版 PDF で読んだもの（SRC-304・307・308・312）は、PDF の「無断転載を禁ずる」の表示を確認して RESTRICTED としました。対応する英語版（Circ J）の DOI は確認できなかったため null にしています。
- SRC-290（大動脈瘤・大動脈解離 GL 英語版）は J-STAGE の本文ページにライセンスの表示がなく UNKNOWN としました。同誌の別の記事は CC BY-NC-ND 4.0 の表示でした。

## 2. 事実票 YAML

```yaml
- id: HT-001
  domain: HT
  subdomain: 本態性高血圧
  assertion:
    plain_statement_ja: 令和5年（2023年）の国民健康・栄養調査では、20歳以上の収縮期血圧の平均は男性131.6 mmHg、女性126.2 mmHgで、収縮期血圧140 mmHg以上の人の割合は男性27.5%、女性22.5%だった。令和元年から水銀を使わない血圧計に変わったため、それ以前の値と比べるときは注意が要る。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 140 mmHg 以上の人の割合がそのまま高血圧の有病率である
  provenance:
    source_ref: SRC-298
    source: 厚生労働省. 令和5年国民健康・栄養調査結果の概要（2024年11月公表）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10900000/001338334.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 令和2年・3年は調査が中止されている。収縮期血圧140 mmHg以上の割合は高血圧の有病率（服薬中の人を含む定義）とは一致しない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-A（本態性高血圧、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-002
  domain: HT
  subdomain: 本態性高血圧
  assertion:
    plain_statement_ja: 令和5年（2023年）の国民健康・栄養調査では、20歳以上の1日の食塩摂取量の平均は9.8 gで、男性10.7 g、女性9.1 gだった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-298
    source: 厚生労働省. 令和5年国民健康・栄養調査結果の概要（2024年11月公表）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10900000/001338334.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 摂取量は食事記録にもとづく推計で、尿中ナトリウム排泄量からの推定とは値が異なりうる
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-A（本態性高血圧、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-003
  domain: HT
  subdomain: 本態性高血圧
  assertion:
    plain_statement_ja: 日本高血圧学会の JSH2025 は、降圧目標を対象集団によらず130/80 mmHg未満に統一した。あわせて、家庭血圧の活用、心血管リスクの層別化、デジタルヘルスや行動面への介入、高齢者・女性・がんサバイバーごとの管理を新たに示している。
    condition:
      guideline: JSH2025（日本高血圧学会 高血圧管理・治療ガイドライン2025）
      region: 日本
    differential: null
    common_misconception: 高齢の高血圧患者の降圧目標は一律に 140/90 mmHg 未満である
  provenance:
    source_ref: SRC-291
    source: Ohya Y, Sakima A, Arima H, et al. Key highlights of the Japanese Society of Hypertension Guidelines for the management of elevated blood pressure and hypertension 2025 (JSH2025). Hypertens Res 2025 (Epub 2025 Aug 29)
    doi: 10.1038/s41440-025-02331-8
    pmid: '40877471'
    pmcid: null
    url: https://doi.org/10.1038/s41440-025-02331-8
    source_license: 未確認（nature.com の取得に失敗）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録で確認した内容。家庭血圧の目標値や例外（フレイル、終末期など）の扱いは本文で確認が要る
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-A（本態性高血圧、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-004
  domain: HT
  subdomain: 本態性高血圧
  assertion:
    plain_statement_ja: JSH2025 の降圧目標は、診察室血圧130/80 mmHg未満、家庭血圧125/75 mmHg未満とされる。高血圧患者一般と脳卒中既往者について、収縮期血圧130 mmHg未満を目標にすることが、推奨の強さ1、エビデンスレベルAで推奨されている。
    condition:
      guideline: JSH2025（日本高血圧学会 高血圧管理・治療ガイドライン2025）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-292
    source: 有馬久富. 成果報告2 日本高血圧学会での取り組み（成果報告会資料、2026年2月28日）. 国立保健医療科学院 掲載
    doi: null
    pmid: null
    pmcid: null
    url: https://c2h.niph.go.jp/eecg/assets/reiwa_7/pdf/05_JPNSH_report.pdf
    source_license: 表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 二次資料経由（ガイドライン作成に関わった研究者の発表スライド）。家庭血圧の目標値と推奨の強さは JSH2025 本文で確認が要る
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-A（本態性高血圧、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-005
  domain: HT
  subdomain: 本態性高血圧
  assertion:
    plain_statement_ja: 2025年の AHA/ACC の高血圧ガイドラインは、成人の血圧を、正常（120/80 mmHg未満）、上昇（収縮期120〜129かつ拡張期80未満）、ステージ1高血圧（収縮期130〜139または拡張期80〜89）、ステージ2高血圧（収縮期140以上または拡張期90以上）に分けている。
    condition:
      guideline: 2025 AHA/ACC 高血圧 GL
      region: 米国の診療を前提とした推奨
    differential: 日本の高血圧の診断基準（診察室血圧140/90 mmHg以上）とは区分の境界が異なる
    common_misconception: 米国でも高血圧の診断基準は 140/90 mmHg である
  provenance:
    source_ref: SRC-293
    source: 2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/SGIM Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Circulation 2025 (published online 2025 Aug 14)
    doi: 10.1161/CIR.0000000000001356
    pmid: null
    pmcid: null
    url: https://professional.heart.org/en/science-news/2025-high-blood-pressure-guideline\top-things-to-know
    source_license: © American Heart Association（AHA 公式要約ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: AHA 公式の要約ページで確認した内容（本文は未確認）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-A（本態性高血圧、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-006
  domain: HT
  subdomain: 本態性高血圧
  assertion:
    plain_statement_ja: 2025年の AHA/ACC の高血圧ガイドラインは、成人全体の降圧目標を130/80 mmHg未満としている。施設に入所している人、余命が限られる人、妊娠中の人は例外として扱う。
    condition:
      guideline: 2025 AHA/ACC 高血圧 GL
      region: 米国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-293
    source: 2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/SGIM Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Circulation 2025 (published online 2025 Aug 14)
    doi: 10.1161/CIR.0000000000001356
    pmid: null
    pmcid: null
    url: https://professional.heart.org/en/science-news/2025-high-blood-pressure-guideline\top-things-to-know
    source_license: © American Heart Association（AHA 公式要約ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: AHA 公式の要約ページで確認した内容（本文は未確認）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-A（本態性高血圧、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-007
  domain: HT
  subdomain: 本態性高血圧
  assertion:
    plain_statement_ja: 2025年の AHA/ACC の高血圧ガイドラインでは、平均血圧が140/90 mmHg以上なら生活習慣の改善と同時に降圧薬を始める。130/80 mmHg以上で、心血管疾患、脳卒中の既往、糖尿病、慢性腎臓病のいずれかがあるか、PREVENT 式の10年リスクが7.5%以上なら降圧薬を始める。それ以外は3〜6か月の生活習慣の改善後も130/80 mmHg以上なら薬を始める。
    condition:
      guideline: 2025 AHA/ACC 高血圧 GL
      region: 米国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-293
    source: 2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/SGIM Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Circulation 2025 (published online 2025 Aug 14)
    doi: 10.1161/CIR.0000000000001356
    pmid: null
    pmcid: null
    url: https://professional.heart.org/en/science-news/2025-high-blood-pressure-guideline\top-things-to-know
    source_license: © American Heart Association（AHA 公式要約ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: AHA 公式の要約ページで確認した内容（本文は未確認）。PREVENT 式は米国の集団で作られたリスク式で、日本人での妥当性は確かめていない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-A（本態性高血圧、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-008
  domain: HT
  subdomain: 本態性高血圧
  assertion:
    plain_statement_ja: 2025年の AHA/ACC の高血圧ガイドラインは、ステージ2高血圧で薬物治療を始めるとき、種類の異なる第一選択薬2剤から始め、2剤を別々に飲むより1錠の配合剤にすることを勧めている。
    condition:
      guideline: 2025 AHA/ACC 高血圧 GL
      region: 米国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-293
    source: 2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/SGIM Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Circulation 2025 (published online 2025 Aug 14)
    doi: 10.1161/CIR.0000000000001356
    pmid: null
    pmcid: null
    url: https://professional.heart.org/en/science-news/2025-high-blood-pressure-guideline\top-things-to-know
    source_license: © American Heart Association（AHA 公式要約ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: AHA 公式の要約ページで確認した内容（本文は未確認）。第一選択薬の種類は要約ページに記載がない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-A（本態性高血圧、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-009
  domain: HT
  subdomain: 高血圧緊急症
  assertion:
    plain_statement_ja: 2025年の AHA/ACC の高血圧ガイドラインは、妊娠していない人で血圧が180/120 mmHgを超えても急性の臓器障害がないものを重症高血圧とし、外来で経口降圧薬を速やかに開始・再開・増量して対応するとしている。
    condition:
      guideline: 2025 AHA/ACC 高血圧 GL
      region: 米国の診療を前提とした推奨
    differential: 高血圧緊急症（急性の臓器障害を伴い、入院での静注薬による降圧を要する）
    common_misconception: 血圧が180/120 mmHgを超えたら臓器障害の有無にかかわらず静注薬で急いで下げる
  provenance:
    source_ref: SRC-293
    source: 2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/SGIM Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Circulation 2025 (published online 2025 Aug 14)
    doi: 10.1161/CIR.0000000000001356
    pmid: null
    pmcid: null
    url: https://professional.heart.org/en/science-news/2025-high-blood-pressure-guideline\top-things-to-know
    source_license: © American Heart Association（AHA 公式要約ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: AHA 公式の要約ページで確認した内容。高血圧緊急症（急性の臓器障害を伴うもの）の降圧速度は要約ページに記載がなく、未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-200 (id: Jlvnlwg)'
    kokushi: 医学各論 Ⅴ-7-C（高血圧緊急症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-010
  domain: HT
  subdomain: 内分泌性高血圧症
  assertion:
    plain_statement_ja: 米国内分泌学会の2025年のガイドラインがまとめた高血圧患者での原発性アルドステロン症の推定有病率は、プライマリケアで5.9%（範囲3.2〜14.0%）、専門施設で7.2%、18〜40歳の若年成人で16.2%、治療抵抗性高血圧で11.3〜29.1%である。
    condition:
      guideline: 米国内分泌学会 原発性アルドステロン症 GL 2025
      region: 国際（米国内分泌学会）。日本内分泌学会 GL 2021 とは照合していない
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-294
    source: 'Adler GK, Stowasser M, Correa RR, et al. Primary Aldosteronism: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab 2025;110:2453-2495'
    doi: 10.1210/clinem/dgaf284
    pmid: null
    pmcid: null
    url: https://academic.oup.com/jcem/article/110/9/2453/8196671
    source_license: © The Endocrine Society 2025, All rights reserved（出版社ページ）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 背景の本文には、プライマリケアで5〜14%、専門施設で最大30%という別の幅の記載もある
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-011
  domain: HT
  subdomain: 内分泌性高血圧症
  assertion:
    plain_statement_ja: 米国内分泌学会の2025年のガイドラインは、原発性アルドステロン症のスクリーニングを高血圧のある人全員に行うことを提案している（条件付き推奨、エビデンスの確実性は低）。実施は地域の資源と体制に応じて判断するとしている。
    condition:
      guideline: 米国内分泌学会 原発性アルドステロン症 GL 2025
      region: 国際（米国内分泌学会）。日本内分泌学会 GL 2021 とは照合していない
    differential: null
    common_misconception: 原発性アルドステロン症は低カリウム血症のある高血圧患者だけを調べればよい
  provenance:
    source_ref: SRC-294
    source: 'Adler GK, Stowasser M, Correa RR, et al. Primary Aldosteronism: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab 2025;110:2453-2495'
    doi: 10.1210/clinem/dgaf284
    pmid: null
    pmcid: null
    url: https://academic.oup.com/jcem/article/110/9/2453/8196671
    source_license: © The Endocrine Society 2025, All rights reserved（出版社ページ）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本内分泌学会の2021年のガイドラインの対象（どの高血圧患者を調べるか）とは照合していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-012
  domain: HT
  subdomain: 内分泌性高血圧症
  assertion:
    plain_statement_ja: 米国内分泌学会の2025年のガイドラインでは、原発性アルドステロン症のスクリーニングは、午前中に座位で、直前に減塩をしていない状態で血中アルドステロンとレニンを測り、カリウムも測る。レニンが抑制され（PRA 1 ng/mL/時以下など）、アルドステロンが不適切に高い（免疫測定法で10 ng/dL以上など）ことを陽性の目安とし、比（ARR）の目安は免疫測定法で20超（ng/dL 対 ng/mL/時）とする。
    condition:
      guideline: 米国内分泌学会 原発性アルドステロン症 GL 2025
      region: 国際（米国内分泌学会）。日本内分泌学会 GL 2021 とは照合していない
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-294
    source: 'Adler GK, Stowasser M, Correa RR, et al. Primary Aldosteronism: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab 2025;110:2453-2495'
    doi: 10.1210/clinem/dgaf284
    pmid: null
    pmcid: null
    url: https://academic.oup.com/jcem/article/110/9/2453/8196671
    source_license: © The Endocrine Society 2025, All rights reserved（出版社ページ）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: カットオフは測定法と単位で異なり、ガイドラインは施設の基準値を使うことを勧めている。日本での測定法（化学発光法など）と単位での値は別に確認が要る
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-013
  domain: HT
  subdomain: 内分泌性高血圧症
  assertion:
    plain_statement_ja: 米国内分泌学会の2025年のガイドラインでは、スクリーニングが陰性でも偽陰性が疑われるときは、安全であれば、MR 拮抗薬・ENaC 阻害薬・その他の利尿薬を4週間、ACE 阻害薬・ARB を2週間中止して再検する。β遮断薬や中枢性α2作動薬の服用中に陽性となったときは、2週間中止して再検する。
    condition:
      guideline: 米国内分泌学会 原発性アルドステロン症 GL 2025
      region: 国際（米国内分泌学会）。日本内分泌学会 GL 2021 とは照合していない
    differential: null
    common_misconception: スクリーニングの前にはすべての降圧薬を中止しなければならない
  provenance:
    source_ref: SRC-294
    source: 'Adler GK, Stowasser M, Correa RR, et al. Primary Aldosteronism: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab 2025;110:2453-2495'
    doi: 10.1210/clinem/dgaf284
    pmid: null
    pmcid: null
    url: https://academic.oup.com/jcem/article/110/9/2453/8196671
    source_license: © The Endocrine Society 2025, All rights reserved（出版社ページ）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインは休薬を最小限にする方法と休薬しない方法の両方を示している
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-014
  domain: HT
  subdomain: 内分泌性高血圧症
  assertion:
    plain_statement_ja: 米国内分泌学会の2025年のガイドラインは、手術を考える原発性アルドステロン症の患者には、治療法を決める前に副腎 CT と副腎静脈サンプリングを行うことを提案している。例外として、35歳未満で病態が明らか、低カリウム血症があり、片側に1.0 cmを超える腺腫がある場合が挙げられている。
    condition:
      guideline: 米国内分泌学会 原発性アルドステロン症 GL 2025
      region: 国際（米国内分泌学会）。日本内分泌学会 GL 2021 とは照合していない
    differential: null
    common_misconception: CT で片側の副腎腫瘍が見えれば、その側が原因と判断して手術できる
  provenance:
    source_ref: SRC-294
    source: 'Adler GK, Stowasser M, Correa RR, et al. Primary Aldosteronism: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab 2025;110:2453-2495'
    doi: 10.1210/clinem/dgaf284
    pmid: null
    pmcid: null
    url: https://academic.oup.com/jcem/article/110/9/2453/8196671
    source_license: © The Endocrine Society 2025, All rights reserved（出版社ページ）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-015
  domain: HT
  subdomain: 内分泌性高血圧症
  assertion:
    plain_statement_ja: 米国内分泌学会の2025年のガイドラインでは、片側性の原発性アルドステロン症で手術を選ぶ患者には片側の副腎全摘を行い、両側性、病側不明、手術の対象にならない、または手術を望まない患者には MR 拮抗薬を生涯続ける。MR 拮抗薬は ENaC 阻害薬より優先し、費用と入手しやすさからスピロノラクトンを優先する。
    condition:
      guideline: 米国内分泌学会 原発性アルドステロン症 GL 2025
      region: 国際（米国内分泌学会）。日本内分泌学会 GL 2021 とは照合していない
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-294
    source: 'Adler GK, Stowasser M, Correa RR, et al. Primary Aldosteronism: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab 2025;110:2453-2495'
    doi: 10.1210/clinem/dgaf284
    pmid: null
    pmcid: null
    url: https://academic.oup.com/jcem/article/110/9/2453/8196671
    source_license: © The Endocrine Society 2025, All rights reserved（出版社ページ）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 国内で使える MR 拮抗薬の種類と保険適用は確認していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-016
  domain: HT
  subdomain: 睡眠時無呼吸症候群
  assertion:
    plain_statement_ja: 治療抵抗性高血圧と閉塞性睡眠時無呼吸のある患者を対象にした6件の RCT（479人）のメタ解析では、CPAP により24時間平均の収縮期血圧が5.40 mmHg、拡張期血圧が3.86 mmHg低下した。
    condition:
      guideline: null
      region: 国際（6件の RCT のメタ解析）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-295
    source: 'Lei Q, Lv Y, Li K, et al. Effects of continuous positive airway pressure on blood pressure in patients with resistant hypertension and obstructive sleep apnea: a systematic review and meta-analysis of six randomized controlled trials. J Bras Pneumol 2017'
    doi: null
    pmid: null
    pmcid: null
    url: https://jbp.org.br/details/2705/en-US
    source_license: Creative Commons（版の表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 論文内で p 値と異質性（I²）の記載が抄録と本文で一致しない。DOI と書誌は API で確定が要る
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-B-④（睡眠時無呼吸症候群、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-017
  domain: HT
  subdomain: 起立性低血圧
  assertion:
    plain_statement_ja: 起立性低血圧は、臥位から立位になって3分以内に収縮期血圧が20 mmHg以上、または拡張期血圧が10 mmHg以上低下するものと定義される。主な症状はめまい、霧視、失神である。
    condition:
      guideline: null
      region: 国際（用語の定義）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-296
    source: 'National Library of Medicine. MeSH Descriptor: Hypotension, Orthostatic (D007024)'
    doi: null
    pmid: null
    pmcid: null
    url: https://meshb.nlm.nih.gov/record/ui?ui=D007024
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-201 (id: Jlvnlwo)'
    kokushi: 医学各論 Ⅴ-7-D（起立性低血圧、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-018
  domain: HT
  subdomain: 起立性低血圧
  assertion:
    plain_statement_ja: 2017年の ACC/AHA/HRS の失神ガイドラインは、起立性低血圧による失神を、反射性失神と並ぶ非心原性失神に分類している。運転の再開までの目安として、起立性低血圧による失神では症状のない期間1か月を示している。
    condition:
      guideline: 2017 ACC/AHA/HRS 失神 GL
      region: 米国の診療を前提とした推奨
    differential: 反射性（神経調節性）失神、心原性失神
    common_misconception: null
  provenance:
    source_ref: SRC-297
    source: 'Shen WK, Sheldon RS, Benditt DG, et al. 2017 ACC/AHA/HRS guideline for the evaluation and management of patients with syncope: executive summary. Heart Rhythm 2017;14:e218-e254'
    doi: 10.1016/j.hrthm.2017.03.005
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/2017-acc-aha-hrs-syncope-guideline-executive-summarypdf-0/download
    source_license: © 2017 American College of Cardiology Foundation, AHA, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 運転の目安は米国の勧告で、日本の道路交通法上の扱いとは異なる
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-201 (id: Jlvnlwo)；TBL-02-05-017 (id: JlAKpfo)'
    kokushi: 医学各論 Ⅴ-7-D（起立性低血圧、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-019
  domain: HT
  subdomain: 腎血管性高血圧症
  assertion:
    plain_statement_ja: 高安動脈炎では、腎動脈狭窄や大動脈縮窄による高血圧が予後を左右する因子の一つで、腎動脈狭窄は治療抵抗性の高血圧の原因になる。小児の高安動脈炎では腹部大動脈と腎動脈が侵されやすい。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-305
    source: 厚生労働省. 指定難病 40 高安動脈炎（概要・診断基準等）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173555.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)；TBL-01-00-194 (id: Jlvnlvw)'
    kokushi: 医学各論 Ⅴ-7-B-②（腎血管性高血圧症、a）；医学各論 Ⅴ-8-A-⑤（高安動脈炎、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HT-020
  domain: HT
  subdomain: 腎血管性高血圧症
  assertion:
    plain_statement_ja: 線維筋性異形成は動脈硬化によらない動脈の病変で、腎動脈に生じることが多い。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: 動脈硬化性の腎動脈狭窄
    common_misconception: null
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 腎動脈狭窄の章（第9章）の本文は抽出できず、治療の推奨は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-7-B-②（腎血管性高血圧症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-001
  domain: VS
  subdomain: 胸部大動脈瘤
  assertion:
    plain_statement_ja: 大動脈の正常径は胸部で約30 mm、腹部で約20 mmである。紡錘状の大動脈瘤は正常径の1.5倍を超える拡張で、胸部では45 mm、腹部では30 mmを超えるものにあたる。壁に大動脈壁の構造が残るものを真性瘤、残らないもの（外傷や感染によることが多い）を仮性瘤、大動脈解離によるものを解離性大動脈瘤と呼ぶ。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc)'
    kokushi: 医学各論 Ⅴ-8-A-①（胸部大動脈瘤、a）；医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-002
  domain: VS
  subdomain: 胸部大動脈瘤
  assertion:
    plain_statement_ja: 日本の大動脈瘤・大動脈解離ガイドラインでは、CT の章で、胸部大動脈瘤は径55〜60 mm以上、腹部大動脈瘤は径50〜55 mm以上を侵襲的治療の適応の目安としている。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: この記載には推奨クラスの付記がない。治療の章（部位別、Marfan 症候群・二尖弁、拡大速度の基準）は抽出できておらず未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc)'
    kokushi: 医学各論 Ⅴ-8-A-①（胸部大動脈瘤、a）；医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-003
  domain: VS
  subdomain: 腹部大動脈瘤
  assertion:
    plain_statement_ja: 嚢状の大動脈瘤は、腹部で横径45 mm以上、胸部で50 mm以上が治療の適応になりうるとされるが、基準は確立していない。瘤の深さと頸部の幅の比が0.8を超えるもの、縦径と横径の比が1.0未満のものは破裂のリスクが高い形とされる。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 推奨クラスの付記はない（PQ としての記載）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc)'
    kokushi: 医学各論 Ⅴ-8-A-①（胸部大動脈瘤、a）；医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-004
  domain: VS
  subdomain: 腹部大動脈瘤
  assertion:
    plain_statement_ja: 米国予防医学専門委員会（USPSTF）の2019年の勧告では、腹部大動脈瘤を径3.0 cm以上の拡張と定義し、1回の腹部超音波検査でスクリーニングする。喫煙歴のある65〜75歳の男性では中等度の正味の利益、喫煙歴のない男性では小さな利益があるとし、喫煙歴も家族歴もない65〜75歳の女性では害が利益を上回るとしている。
    condition:
      guideline: USPSTF 2019 腹部大動脈瘤スクリーニング勧告
      region: 米国の診療を前提とした勧告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-301
    source: 'US Preventive Services Task Force. Abdominal Aortic Aneurysm: Screening. Final Recommendation Statement (2019 Dec 10)'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.uspreventiveservicestaskforce.org/uspstf/document/RecommendationStatementFinal/abdominal-aortic-aneurysm-screening
    source_license: 米国連邦政府の資料（AHRQ が運営する USPSTF のサイト）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 日本では公的な腹部大動脈瘤スクリーニング制度はない（日本の推奨は未確認）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc)'
    kokushi: 医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-005
  domain: VS
  subdomain: 腹部大動脈瘤
  assertion:
    plain_statement_ja: USPSTF の2019年の勧告によると、腹部大動脈瘤の年間破裂リスクは径3.0〜3.9 cmでほぼ0%、4.0〜4.9 cmで1%、5.0〜5.9 cmで11%とされ、破裂した場合の死亡率は最大81%に達する。
    condition:
      guideline: USPSTF 2019 腹部大動脈瘤スクリーニング勧告
      region: 米国の診療を前提とした勧告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-301
    source: 'US Preventive Services Task Force. Abdominal Aortic Aneurysm: Screening. Final Recommendation Statement (2019 Dec 10)'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.uspreventiveservicestaskforce.org/uspstf/document/RecommendationStatementFinal/abdominal-aortic-aneurysm-screening
    source_license: 米国連邦政府の資料（AHRQ が運営する USPSTF のサイト）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 数値は勧告が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc)'
    kokushi: 医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-006
  domain: VS
  subdomain: 腹部大動脈瘤
  assertion:
    plain_statement_ja: USPSTF の2019年の勧告によると、男性の腹部大動脈瘤は、径5.5 cm以上、または径4.0 cmを超え1年で1.0 cm以上大きくなったものに待機的修復を行うのが標準とされる。女性での基準は男性と異なる可能性がある。
    condition:
      guideline: USPSTF 2019 腹部大動脈瘤スクリーニング勧告
      region: 米国の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-301
    source: 'US Preventive Services Task Force. Abdominal Aortic Aneurysm: Screening. Final Recommendation Statement (2019 Dec 10)'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.uspreventiveservicestaskforce.org/uspstf/document/RecommendationStatementFinal/abdominal-aortic-aneurysm-screening
    source_license: 米国連邦政府の資料（AHRQ が運営する USPSTF のサイト）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 女性の基準（米国血管外科学会の5.0〜5.4 cm）は勧告が引用した二次資料経由。日本の大動脈瘤 GL の治療の章の基準とは照合していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc)'
    kokushi: 医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-007
  domain: VS
  subdomain: 大動脈解離
  assertion:
    plain_statement_ja: 大動脈解離の Stanford 分類では、上行大動脈に解離があるものを A 型、ないものを B 型とする。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)'
    kokushi: 医学各論 Ⅴ-8-A-④（大動脈解離、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-008
  domain: VS
  subdomain: 大動脈解離
  assertion:
    plain_statement_ja: 大動脈解離の DeBakey 分類では、上行大動脈に内膜の亀裂があり弓部を越えて広がるものを I 型、上行大動脈に限局するものを II 型、下行大動脈に亀裂があるものを III 型とする。III 型のうち腹部大動脈に及ばないものを IIIa、及ぶものを IIIb とする。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)'
    kokushi: 医学各論 Ⅴ-8-A-④（大動脈解離、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-009
  domain: VS
  subdomain: 大動脈解離
  assertion:
    plain_statement_ja: 大動脈解離の病期は、発症から48時間以内を超急性期、2週間以内を急性期、2週間から3か月を亜急性期、3か月を超えるものを慢性期とする。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)'
    kokushi: 医学各論 Ⅴ-8-A-④（大動脈解離、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-010
  domain: VS
  subdomain: 大動脈解離
  assertion:
    plain_statement_ja: 日本の急性大動脈解離の発生率は人口10万人あたり年約3人と推定されるが、東京の急性大動脈スーパーネットワークのデータでは約10人である。地域の調査では年2.62〜5.2人と幅がある。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 病院に着く前の死亡を含むかどうかで値が変わる
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)'
    kokushi: 医学各論 Ⅴ-8-A-④（大動脈解離、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-011
  domain: VS
  subdomain: 大動脈解離
  assertion:
    plain_statement_ja: 東京都監察医務院の剖検例では、大動脈解離による突然死の61.4%が病院に着く前に死亡しており、病院到着前を含め93%が発症24時間以内に死亡していた。直接の死因の大半は大動脈の破裂で、心タンポナーデが86.6%を占めた。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 突然死の剖検例の値で、大動脈解離全体の死亡率ではない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)'
    kokushi: 医学各論 Ⅴ-8-A-④（大動脈解離、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-012
  domain: VS
  subdomain: 大動脈解離
  assertion:
    plain_statement_ja: 大動脈解離は冬に多く、時刻では午前6時から正午に多い。好発年齢は70歳代である。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)'
    kokushi: 医学各論 Ⅴ-8-A-④（大動脈解離、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-013
  domain: VS
  subdomain: 大動脈解離
  assertion:
    plain_statement_ja: 急性大動脈解離の約6%は痛みを伴わず、失神は9〜20%にみられる。38℃を超える発熱は約3分の1にみられる。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: 大動脈解離では必ず激しい胸背部痛がある
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 発熱の割合は本文中で約30%と約3分の1の2通りの記載がある
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)；TBL-02-05-021 (id: JlAKpfI)'
    kokushi: 医学各論 Ⅴ-8-A-④（大動脈解離、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-014
  domain: VS
  subdomain: 大動脈解離
  assertion:
    plain_statement_ja: 大動脈解離による臓器の灌流障害（malperfusion）の頻度は、冠動脈3〜7%、脳虚血3〜7%、対麻痺約4%、腸管虚血2〜7%、腎虚血約7%、下肢虚血7〜18%とされる。左右の上肢で20 mmHgを超える血圧差は約半数にみられる。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 灌流障害の機序には、動的閉塞、静的閉塞、両者の組み合わせがある
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)'
    kokushi: 医学各論 Ⅴ-8-A-④（大動脈解離、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-015
  domain: VS
  subdomain: 大動脈解離
  assertion:
    plain_statement_ja: D ダイマーを500 ng/mLで区切ると、急性大動脈解離に対する感度は96.6%、特異度は46.6%と報告されている。ADD-RS が0か1で D ダイマーが500 ng/mL未満なら解離を除外して CT を省略でき、ADD-RS が2か3なら D ダイマーを待たずに CT を行う。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: D ダイマーが正常なら、どの患者でも大動脈解離を否定できる
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: カットオフは試薬で異なり、施設ごとに確認するよう本文に注記がある
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)；TBL-02-05-021 (id: JlAKpfI)'
    kokushi: 医学各論 Ⅴ-8-A-④（大動脈解離、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-016
  domain: VS
  subdomain: 大動脈解離
  assertion:
    plain_statement_ja: 胸部単純 X 線写真で、内膜の石灰化と大動脈外縁の距離は通常2〜3 mmで、6 mm以上なら解離を疑う。大動脈解離の約20%は胸部単純 X 線写真に異常がない。
    condition:
      guideline: JCS/JSCVS/JATS/JSVS 2020 大動脈瘤・大動脈解離 GL（英語版 2023）
      region: 日本の診療を前提とした記載
    differential: null
    common_misconception: 胸部 X 線写真で縦隔の拡大がなければ大動脈解離は否定できる
  provenance:
    source_ref: SRC-290
    source: Ogino H, et al. JCS/JSCVS/JATS/JSVS 2020 Guideline on Diagnosis and Treatment of Aortic Aneurysm and Aortic Dissection. Circ J 2023;87:1410-1621
    doi: 10.1253/circj.CJ-22-0794
    pmid: '37661428'
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/circj/advpub/0/advpub_CJ-22-0794/_html/-char/en
    source_license: 未確認（J-STAGE の本文ページに表示なし。同誌の他の記事は CC BY-NC-ND 4.0・© 日本循環器学会）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)'
    kokushi: 医学各論 Ⅴ-8-A-④（大動脈解離、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-017
  domain: VS
  subdomain: Marfan症候群
  assertion:
    plain_statement_ja: Marfan 症候群は FBN1 遺伝子（フィブリリン1をコードする）の変異による常染色体顕性（優性）遺伝の疾患で、世界で約5,000人に1人にみられる。少なくとも25%は家族歴のない新規の変異による。
    condition:
      guideline: null
      region: 国際
    differential: null
    common_misconception: 家族歴がなければ Marfan 症候群は否定できる
  provenance:
    source_ref: SRC-302
    source: MedlinePlus Genetics. Marfan syndrome (last updated 2018 May 1). National Library of Medicine
    doi: null
    pmid: null
    pmcid: null
    url: https://medlineplus.gov/genetics/condition/marfan-syndrome
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc)'
    kokushi: 医学各論 Ⅴ-8-A-⑥（Marfan症候群、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-018
  domain: VS
  subdomain: Marfan症候群
  assertion:
    plain_statement_ja: Marfan 症候群の主要な特徴は大動脈の拡張と水晶体偏位で、大動脈瘤や大動脈解離は命にかかわる。高身長でやせ型、長い指趾、関節の過可動、指極（両腕を広げた長さ）が身長を上回ること、側弯・後弯、漏斗胸・鳩胸などの骨格の特徴を伴う。
    condition:
      guideline: null
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-302
    source: MedlinePlus Genetics. Marfan syndrome (last updated 2018 May 1). National Library of Medicine
    doi: null
    pmid: null
    pmcid: null
    url: https://medlineplus.gov/genetics/condition/marfan-syndrome
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 改訂 Ghent 基準の内容は今回は扱っていない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc)'
    kokushi: 医学各論 Ⅴ-8-A-⑥（Marfan症候群、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-019
  domain: VS
  subdomain: 高安動脈炎
  assertion:
    plain_statement_ja: 日本の高安動脈炎の登録患者は6,000人を超え、年に約300人が新たに発症すると推定されている。男女比は約1：9で、平均発症年齢は女性35歳、男性43.5歳である。女性では20歳前後に発症のピークがあるが、中高年の発症もまれではない。
    condition:
      guideline: JCS 2017 血管炎症候群 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-304
    source: 日本循環器学会ほか. 血管炎症候群の診療ガイドライン（2017年改訂版）. 2018年3月23日発行、2018年6月29日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_isobe_h.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 指定難病の資料（SRC-305）では、2019年度の受給者証所持者4,463人、男女比1：8とされ、数値の基準が異なる
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw)'
    kokushi: 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-020
  domain: VS
  subdomain: 高安動脈炎
  assertion:
    plain_statement_ja: 高安動脈炎は若い女性に多い原因不明の大型血管炎で、大動脈、その主要分枝、肺動脈、冠動脈に狭窄・閉塞・拡張を起こす。橈骨動脈の脈が触れないことが多いため脈なし病とも呼ばれる。2019年度の指定難病の受給者証所持者は4,463人で、患者の約10%に炎症性腸疾患（潰瘍性大腸炎など）を合併する。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-305
    source: 厚生労働省. 指定難病 40 高安動脈炎（概要・診断基準等）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173555.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw)'
    kokushi: 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-021
  domain: VS
  subdomain: 高安動脈炎
  assertion:
    plain_statement_ja: 日本の高安動脈炎患者の約50%が HLA-B*52 をもつのに対し、日本の一般人口での保有率は10〜20%である。
    condition:
      guideline: JCS 2017 血管炎症候群 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-304
    source: 日本循環器学会ほか. 血管炎症候群の診療ガイドライン（2017年改訂版）. 2018年3月23日発行、2018年6月29日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_isobe_h.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 診断の参考所見として HLA-B*52 または B*67 の陽性が挙げられている
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw)'
    kokushi: 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-022
  domain: VS
  subdomain: 高安動脈炎
  assertion:
    plain_statement_ja: 高安動脈炎1,372例の報告では、発熱や倦怠感などの全身症状が約74.9%、脈拍の消失や左右の血圧差などの上肢虚血の所見が約66.4%、頭頸部の症状が約47.5%、高血圧が約38%にみられた。大動脈弁閉鎖不全は約30%にみられ、予後を左右する。
    condition:
      guideline: JCS 2017 血管炎症候群 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-304
    source: 日本循環器学会ほか. 血管炎症候群の診療ガイドライン（2017年改訂版）. 2018年3月23日発行、2018年6月29日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_isobe_h.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 大動脈弁閉鎖不全の割合は本文で約30%、表で33.2%と記載されている
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw)'
    kokushi: 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-023
  domain: VS
  subdomain: 高安動脈炎
  assertion:
    plain_statement_ja: 高安動脈炎の初期治療はプレドニゾロン0.5〜1 mg/kg/日を2〜4週間投与する。トシリズマブはクラス I・エビデンスレベル B で推奨され、2017年8月25日に保険適用となった。
    condition:
      guideline: JCS 2017 血管炎症候群 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-304
    source: 日本循環器学会ほか. 血管炎症候群の診療ガイドライン（2017年改訂版）. 2018年3月23日発行、2018年6月29日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_isobe_h.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 緊急時・難治例のステロイドパルスはクラス IIb・レベル C
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw)'
    kokushi: 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-024
  domain: VS
  subdomain: 高安動脈炎
  assertion:
    plain_statement_ja: 高安動脈炎では、ステロイドを減量する過程で約70%が再燃する。外科治療や血管内治療が必要になるのは約20%で、なるべく炎症が落ち着いてから行う。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-305
    source: 厚生労働省. 指定難病 40 高安動脈炎（概要・診断基準等）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173555.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw)'
    kokushi: 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-025
  domain: VS
  subdomain: 高安動脈炎
  assertion:
    plain_statement_ja: 高安動脈炎の病変分布による分類（沼野分類）では、I 型は大動脈弓の分枝、IIa 型は上行大動脈・弓部とその分枝、IIb 型は IIa 型に下行胸部大動脈を加えたもの、III 型は下行胸部大動脈・腹部大動脈・腎動脈、IV 型は腹部大動脈と腎動脈の一方または両方、V 型は IIb 型と IV 型を合わせたものである。
    condition:
      guideline: JCS 2017 血管炎症候群 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-304
    source: 日本循環器学会ほか. 血管炎症候群の診療ガイドライン（2017年改訂版）. 2018年3月23日発行、2018年6月29日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_isobe_h.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw)'
    kokushi: 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-026
  domain: VS
  subdomain: Buerger病
  assertion:
    plain_statement_ja: バージャー病（閉塞性血栓血管炎）は四肢、主に下肢の動脈に分節的な閉塞を起こす血管炎で、遊走性静脈炎を伴うことがある。原因は不明だが喫煙との関係が強く、最近の調査では患者の93%に明らかな喫煙歴があった。2019年度の指定難病の受給者証所持者は2,259人である。症状は冷感・しびれ・寒冷時のレイノー現象から、間歇性跛行、安静時痛、潰瘍・壊死へ進む。
    condition:
      guideline: null
      region: 日本
    differential: 閉塞性動脈硬化症
    common_misconception: null
  provenance:
    source_ref: SRC-306
    source: 厚生労働省. 指定難病 47 バージャー病（概要・診断基準等）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173547.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-193 (id: Jlvnlvo)'
    kokushi: 医学各論 Ⅴ-8-B-④（Buerger病、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-027
  domain: VS
  subdomain: Buerger病
  assertion:
    plain_statement_ja: バージャー病の診断には、動脈硬化による壁の変化を伴わない、多発性で分節的な末梢動脈の閉塞を画像で示すことが必要である。50歳以上の発症、喫煙歴が明らかでない場合、女性、糖尿病・高血圧・脂質異常症がある場合は、特に厳密に鑑別する。除外すべき疾患は、閉塞性動脈硬化症、外傷性動脈血栓症、膝窩動脈捕捉症候群、膝窩動脈外膜嚢腫、膠原病、血管ベーチェット病、胸郭出口症候群、塞栓症である。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-306
    source: 厚生労働省. 指定難病 47 バージャー病（概要・診断基準等）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173547.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 除外疾患の名称は抽出結果（英語の要約）から訳した。特に膝窩動脈外膜嚢腫は原文の表記で確認が要る
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-193 (id: Jlvnlvo)'
    kokushi: 医学各論 Ⅴ-8-B-④（Buerger病、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-028
  domain: VS
  subdomain: Buerger病
  assertion:
    plain_statement_ja: バージャー病の治療で最も重要なのは、受動喫煙の回避を含めた厳格な禁煙である。患肢の保温と保護、歩行などの運動療法、抗血小板薬・抗凝固薬・プロスタグランジン E1 の静注、適応のある例のバイパス術を行う。心臓・脳・大血管の病変は通常起こらず生命予後はよいが、肢の切断が必要になることがある。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-306
    source: 厚生労働省. 指定難病 47 バージャー病（概要・診断基準等）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173547.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-193 (id: Jlvnlvo)'
    kokushi: 医学各論 Ⅴ-8-B-④（Buerger病、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-029
  domain: VS
  subdomain: 閉塞性動脈硬化症
  assertion:
    plain_statement_ja: 安静時の足関節上腕血圧比（ABI）は、0.90以下を異常低値、0.91〜0.99を境界域、1.00〜1.40を正常、1.40を超えるものを異常高値とする。0.90以下は主幹動脈の狭窄または閉塞を示す。安静時 ABI によるスクリーニングと、安静時 ABI が正常で間歇性跛行がある場合の運動後 ABI はいずれもクラス I・エビデンスレベル B である。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: ABI が正常なら下肢の動脈疾患は否定できる
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)'
    kokushi: 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-030
  domain: VS
  subdomain: 閉塞性動脈硬化症
  assertion:
    plain_statement_ja: ABI が1.40を超えるときは動脈の高度の石灰化が疑われ、足趾上腕血圧比（TBI）、経皮酸素分圧、皮膚灌流圧などを追加で調べる（クラス I・エビデンスレベル B）。TBI の虚血の目安は約0.6〜0.7、足趾血圧60 mmHg未満は虚血、経皮酸素分圧は安静時60 mmHg未満で虚血、30 mmHg未満で重症虚血とされ、皮膚灌流圧が30〜40 mmHg未満では創傷が治りにくい。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 石灰化は糖尿病や透析の患者に多いが、その記載は今回の抽出範囲では確認していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)'
    kokushi: 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-031
  domain: VS
  subdomain: 閉塞性動脈硬化症
  assertion:
    plain_statement_ja: 一般住民で ABI が0.90以下の人の割合は、60歳以上で1〜3%、70歳以上で2〜5%で、男性は女性の約2倍である。日本の一般住民のメタ解析では1.1%だった。喫煙は下肢閉塞性動脈疾患のオッズ比を3.8に高め、20年以上禁煙を続けた人のリスクは非喫煙者と同程度まで下がる。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)；TBL-01-00-189 (id: JlvnlvQ)'
    kokushi: 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-032
  domain: VS
  subdomain: 閉塞性動脈硬化症
  assertion:
    plain_statement_ja: 日本の REACH 登録の下肢閉塞性動脈疾患627例では、冠動脈疾患の合併が30%、脳血管疾患が21%、両方が7%だった。症状のない下肢閉塞性動脈疾患でも、全死亡のハザード比は1.53、心血管死は1.94と高い。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: 症状がない下肢の動脈疾患は予後に影響しない
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)；TBL-01-00-189 (id: JlvnlvQ)'
    kokushi: 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-033
  domain: VS
  subdomain: 閉塞性動脈硬化症
  assertion:
    plain_statement_ja: 間歇性跛行の患者で5年間に症状の悪化や包括的高度慢性下肢虚血（CLTI）への進行が起こるのは21%、大切断に至るのは5年で1〜3%である。CLTI は、虚血による安静時痛、または下肢の潰瘍・壊疽が少なくとも2週間以上続くものと定義され、重症度は創・虚血・足の感染の3要素で評価する（WIfI 分類）。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: 間歇性跛行の患者の多くは数年で下肢切断に至る
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)'
    kokushi: 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-034
  domain: VS
  subdomain: 閉塞性動脈硬化症
  assertion:
    plain_statement_ja: 血行再建後の抗血栓療法として、アスピリン100 mg/日に少量のリバーロキサバン（2.5 mgを1日2回）を加えると、大出血を増やさずに複合エンドポイントを減らしたという試験（VOYAGER PAD）があるが、この用法は日本では承認されていない。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 承認状況はガイドライン（2025年5月の更新版）の記載による。その後の承認の有無は確認していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)'
    kokushi: 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-035
  domain: VS
  subdomain: 急性動脈閉塞症
  assertion:
    plain_statement_ja: 急性下肢虚血は、急激に起きた肢の虚血で、通常は発症から2週間以内のものをいう。日本の2014年の報告では原因は塞栓症45.0%、血栓症55.0%で、心原性の塞栓の大部分は心房細動による左房内の血栓である。症状は疼痛、蒼白、脈拍消失、知覚鈍麻、運動麻痺の5P で、虚脱を加えて6P とすることもある。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 英国の報告では塞栓症46%、動脈硬化病変の血栓症24%などと内訳が異なる
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)'
    kokushi: 医学各論 Ⅴ-8-B-③（急性動脈閉塞症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-036
  domain: VS
  subdomain: 急性動脈閉塞症
  assertion:
    plain_statement_ja: 急性下肢虚血の Rutherford 分類では、カテゴリー I が救肢可能、II が危機的（IIa が境界型、IIb が即時型）、III が不可逆性である。血行再建の目安は、カテゴリー II では6時間以内、カテゴリー I では24時間以内とされる。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)'
    kokushi: 医学各論 Ⅴ-8-B-③（急性動脈閉塞症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-037
  domain: VS
  subdomain: 急性動脈閉塞症
  assertion:
    plain_statement_ja: 急性下肢虚血では、禁忌がなければ未分画ヘパリン5,000単位または70〜100単位/kgを静注する（クラス I・エビデンスレベル C）。日本では外科的血栓除去術が第一選択で、動脈硬化が強い場合や手術が難しい場合は血管内治療やハイブリッド治療を考慮する（クラス IIa・エビデンスレベル B）。動脈硬化を原因とする例では、二次予防として抗血小板薬とスタチンを投与する（クラス I・エビデンスレベル A）。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)'
    kokushi: 医学各論 Ⅴ-8-B-③（急性動脈閉塞症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-038
  domain: VS
  subdomain: 急性動脈閉塞症
  assertion:
    plain_statement_ja: 急性下肢虚血の再灌流後には、代謝性アシドーシス、高カリウム血症、急性腎不全などを起こす筋腎代謝症候群（MNMS）が起こりうるが、確立した予防法・治療法はない。コンパートメント症候群は区画内圧20〜30 mmHg以上で診断し、発症から6時間以内の筋膜切開が必要である。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)'
    kokushi: 医学各論 Ⅴ-8-B-③（急性動脈閉塞症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-039
  domain: VS
  subdomain: 急性動脈閉塞症
  assertion:
    plain_statement_ja: 急性下肢虚血の死亡率は15〜20%と報告されている。膝窩動脈瘤は急性下肢虚血の原因の3.5%を占め、膝窩動脈瘤の約半数は急性下肢虚血で発症する。膝窩動脈瘤の血栓化による急性下肢虚血では、血行再建後も8〜18%が肢の切断に至る。
    condition:
      guideline: JCS/JSVS 2022 末梢動脈疾患 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-307
    source: 日本循環器学会・日本血管外科学会. 末梢動脈疾患ガイドライン（2022年改訂版）. 2022年3月11日発行、2025年5月15日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2022/03/JCS2022_Azuma.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本血管外科学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)'
    kokushi: 医学各論 Ⅴ-8-B-③（急性動脈閉塞症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-040
  domain: VS
  subdomain: Raynaud症候群
  assertion:
    plain_statement_ja: レイノー現象は、寒冷や精神的ストレスに対する細動脈の過剰な収縮で、主に手指が白色または青色になり、温まると赤くなる。発作は誘因がなくなってから約15分続くことが多い。成人の3〜5%にみられ、女性に多い。
    condition:
      guideline: null
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-303
    source: MedlinePlus Genetics. Raynaud phenomenon (last updated 2018 Mar 1). National Library of Medicine
    doi: null
    pmid: null
    pmcid: null
    url: https://medlineplus.gov/genetics/condition/raynaud-phenomenon
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-8-B-②（Raynaud症候群、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-041
  domain: VS
  subdomain: Raynaud症候群
  assertion:
    plain_statement_ja: 基礎疾患のない一次性レイノー現象は通常15〜25歳で始まり、二次性は30歳以降に始まることが多い。二次性の原因には、全身性エリテマトーデス、強皮症、関節リウマチ、Sjögren 症候群などの自己免疫疾患のほか、甲状腺機能低下症、一部の血液腫瘍、薬剤、喫煙、振動工具の長期使用などがある。重い二次性では指尖の潰瘍や壊死を起こすことがある。
    condition:
      guideline: null
      region: 国際
    differential: Buerger 病（喫煙者の四肢末梢の動脈閉塞で、寒冷時のレイノー現象を伴うことがある）
    common_misconception: null
  provenance:
    source_ref: SRC-303
    source: MedlinePlus Genetics. Raynaud phenomenon (last updated 2018 Mar 1). National Library of Medicine
    doi: null
    pmid: null
    pmcid: null
    url: https://medlineplus.gov/genetics/condition/raynaud-phenomenon
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-8-B-②（Raynaud症候群、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-042
  domain: VS
  subdomain: 深部静脈血栓症<DVT>
  assertion:
    plain_statement_ja: 静脈血栓塞栓症の成因は、血流の停滞、血管内皮の障害、血液凝固能の亢進（Virchow の3徴）である。日本人では第 V 因子 Leiden 変異とプロトロンビン G20210A 変異は見つかっておらず、ヘテロ接合の保因率はアンチトロンビン欠乏0.18%、プロテイン C 欠乏0.16%、プロテイン S 欠乏1.8%とされる。
    condition:
      guideline: JCS 2017 肺血栓塞栓症・深部静脈血栓症 GL
      region: 日本
    differential: null
    common_misconception: 日本人の血栓性素因として第 V 因子 Leiden 変異を調べるべきである
  provenance:
    source_ref: SRC-308
    source: 日本循環器学会ほか. 肺血栓塞栓症および深部静脈血栓症の診断、治療、予防に関するガイドライン（2017年改訂版）. 2018年3月23日発行、2018年12月10日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_ito_h.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2017年改訂版の記載。2025年の新しいガイドライン（JCS/JPCPHS 2025、DOI 10.1253/circj.CJ-25-1144）とは照合していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-195 (id: Jlvnlv0)'
    kokushi: 医学各論 Ⅴ-8-C-①（深部静脈血栓症<DVT>、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-043
  domain: VS
  subdomain: 深部静脈血栓症<DVT>
  assertion:
    plain_statement_ja: 静脈血栓塞栓症のうち、診断前3か月以内に一時的または可逆的な危険因子があるものを誘因あり（provoked）、そのような因子がないものを誘因なし（unprovoked）とする。
    condition:
      guideline: JCS 2017 肺血栓塞栓症・深部静脈血栓症 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-308
    source: 日本循環器学会ほか. 肺血栓塞栓症および深部静脈血栓症の診断、治療、予防に関するガイドライン（2017年改訂版）. 2018年3月23日発行、2018年12月10日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_ito_h.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2017年改訂版の記載。2025年の新しいガイドラインとは照合していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-195 (id: Jlvnlv0)'
    kokushi: 医学各論 Ⅴ-8-C-①（深部静脈血栓症<DVT>、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-044
  domain: VS
  subdomain: 深部静脈血栓症<DVT>
  assertion:
    plain_statement_ja: 静脈血栓塞栓症の抗凝固療法は、初期（0〜7日）、維持期（8日〜3か月）、延長期（3か月以降）に分ける。エドキサバンは十分な非経口抗凝固薬による初期治療の後に始め、リバーロキサバンとアピキサバンは高用量の初期治療の後に通常量にする（いずれもクラス I・エビデンスレベル A）。日本で静脈血栓塞栓症の治療に使える DOAC として、エドキサバン、リバーロキサバン、アピキサバンが挙げられている。
    condition:
      guideline: JCS 2017 肺血栓塞栓症・深部静脈血栓症 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-308
    source: 日本循環器学会ほか. 肺血栓塞栓症および深部静脈血栓症の診断、治療、予防に関するガイドライン（2017年改訂版）. 2018年3月23日発行、2018年12月10日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_ito_h.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2017年改訂版の記載で、肺血栓塞栓症の章の薬物療法を深部静脈血栓症にも共通とする記述による。抽出結果ではフォンダパリヌクスが2011年、3剤の DOAC が2014年の承認とされていたが、薬剤ごとの承認時期は確認できておらず主張文から外した。2025年の新しいガイドラインとは照合していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-195 (id: Jlvnlv0)'
    kokushi: 医学各論 Ⅴ-8-C-①（深部静脈血栓症<DVT>、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-045
  domain: VS
  subdomain: 深部静脈血栓症<DVT>
  assertion:
    plain_statement_ja: 静脈血栓塞栓症の抗凝固療法の期間は、可逆的な危険因子がある場合は3か月、誘因がない場合は少なくとも3か月とし（クラス I・エビデンスレベル A）、再発例ではより長く（クラス I・エビデンスレベル B）、がんのある患者ではがんが治るまで続ける（クラス IIa・エビデンスレベル B）。ワルファリンの目標 PT-INR は1.5〜2.5とされる（クラス IIa・エビデンスレベル C）。
    condition:
      guideline: JCS 2017 肺血栓塞栓症・深部静脈血栓症 GL
      region: 日本（PT-INR の目標は日本の基準）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-308
    source: 日本循環器学会ほか. 肺血栓塞栓症および深部静脈血栓症の診断、治療、予防に関するガイドライン（2017年改訂版）. 2018年3月23日発行、2018年12月10日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_ito_h.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2017年改訂版の記載。2025年の新しいガイドラインとは照合していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-195 (id: Jlvnlv0)'
    kokushi: 医学各論 Ⅴ-8-C-①（深部静脈血栓症<DVT>、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VS-046
  domain: VS
  subdomain: 深部静脈血栓症<DVT>
  assertion:
    plain_statement_ja: 下腿に限局した深部静脈血栓症は下肢静脈超音波で経過をみて、血栓が中枢に進展した場合に下大静脈フィルターを考える。下大静脈フィルターは、出血のリスクなどで抗凝固療法ができない場合に考慮する。
    condition:
      guideline: JCS 2017 肺血栓塞栓症・深部静脈血栓症 GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-308
    source: 日本循環器学会ほか. 肺血栓塞栓症および深部静脈血栓症の診断、治療、予防に関するガイドライン（2017年改訂版）. 2018年3月23日発行、2018年12月10日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_ito_h.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2017年改訂版の記載で、DVT の章の本文は抽出できていない。下腿 DVT への抗凝固療法の適否は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-195 (id: Jlvnlv0)'
    kokushi: 医学各論 Ⅴ-8-C-①（深部静脈血栓症<DVT>、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-001
  domain: CX
  subdomain: 循環器疾患の統計（日本）
  assertion:
    plain_statement_ja: 令和6年（2024年）の日本の死因は、1位が悪性新生物（死亡率は人口10万対319.3、全死亡の23.9%）、2位が心疾患（高血圧性を除く）で死亡数226,388人、死亡率188.2、全死亡の14.1%だった。脳血管疾患は4位で死亡数102,821人、死亡率85.5、全死亡の6.4%だった。
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
  uncertainty: 心疾患の内訳（急性心筋梗塞、心不全など）と大動脈瘤・解離の死亡数はこの表にない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-002
  domain: CX
  subdomain: 循環器疾患の統計（日本）
  assertion:
    plain_statement_ja: 令和5年（2023年）の患者調査では、循環器系の疾患の総患者数（継続的に医療を受けている推計患者数）は2,210万1千人だった。総患者数は、平均診療間隔の上限を98日として算出している。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-300
    source: 厚生労働省. 令和5年（2023）患者調査の概況
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/toukei/saikin/hw/kanja/23/dl/kanjya.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 高血圧性疾患や心疾患ごとの総患者数は概況の表7にはなく、詳細表で確認が要る。平均診療間隔の上限は令和2年から30日を98日に変更しており、それ以前と比べるときは注意が要る
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-003
  domain: CX
  subdomain: 失神
  assertion:
    plain_statement_ja: 失神は、脳の低灌流によって起こる突然の一過性の意識消失で、姿勢を保てなくなり、速やかに自然に回復するものをいう。原因は、反射性（神経調節性。血管迷走神経性が最も多い）、起立性低血圧、心原性（徐脈、頻脈、心拍出量の低下、血流の閉塞、大動脈解離など）に分けられる。
    condition:
      guideline: 2017 ACC/AHA/HRS 失神 GL
      region: 米国の診療を前提とした推奨
    differential: てんかん発作、低血糖、頭部外傷などの失神以外の一過性意識障害
    common_misconception: null
  provenance:
    source_ref: SRC-297
    source: 'Shen WK, Sheldon RS, Benditt DG, et al. 2017 ACC/AHA/HRS guideline for the evaluation and management of patients with syncope: executive summary. Heart Rhythm 2017;14:e218-e254'
    doi: 10.1016/j.hrthm.2017.03.005
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/2017-acc-aha-hrs-syncope-guideline-executive-summarypdf-0/download
    source_license: © 2017 American College of Cardiology Foundation, AHA, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-02 (id: JkxnuQk)；TBL-02-05-017 (id: JlAKpfo)；TBL-01-00-202 (id: Jlvnlws)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-004
  domain: CX
  subdomain: 失神
  assertion:
    plain_statement_ja: 失神の初期評価では、詳しい病歴と身体診察（クラス I）と安静時12誘導心電図（クラス I）を行う。ルーチンの包括的な血液検査と、心原性が疑われない場合のルーチンの心臓画像検査は有用でない（クラス III）。構造的心疾患が疑われる患者では経胸壁心エコーが有用でありうる（クラス IIa）。
    condition:
      guideline: 2017 ACC/AHA/HRS 失神 GL
      region: 米国の診療を前提とした推奨
    differential: null
    common_misconception: 失神の患者には全員に頭部 CT と心エコーを行う
  provenance:
    source_ref: SRC-297
    source: 'Shen WK, Sheldon RS, Benditt DG, et al. 2017 ACC/AHA/HRS guideline for the evaluation and management of patients with syncope: executive summary. Heart Rhythm 2017;14:e218-e254'
    doi: 10.1016/j.hrthm.2017.03.005
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/2017-acc-aha-hrs-syncope-guideline-executive-summarypdf-0/download
    source_license: © 2017 American College of Cardiology Foundation, AHA, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-02 (id: JkxnuQk)；TBL-02-05-017 (id: JlAKpfo)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-005
  domain: CX
  subdomain: 失神
  assertion:
    plain_statement_ja: 心原性失神を示唆する特徴として、60歳を超える年齢、男性、虚血性・構造的・先天性心疾患や心機能低下の既往、前兆が短い（動悸など）か前兆のない突然の意識消失、労作中や臥位での失神、少ない発作回数（1〜2回）、心臓の診察所見の異常、遺伝性疾患や50歳未満の突然死の家族歴が挙げられる。
    condition:
      guideline: 2017 ACC/AHA/HRS 失神 GL
      region: 米国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-297
    source: 'Shen WK, Sheldon RS, Benditt DG, et al. 2017 ACC/AHA/HRS guideline for the evaluation and management of patients with syncope: executive summary. Heart Rhythm 2017;14:e218-e254'
    doi: 10.1016/j.hrthm.2017.03.005
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/2017-acc-aha-hrs-syncope-guideline-executive-summarypdf-0/download
    source_license: © 2017 American College of Cardiology Foundation, AHA, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインはこれらの特徴は診断的ではないと注記している
  curriculum:
    core_curriculum: 'PS-02-06-02 (id: JkxnuQk)；TBL-02-05-017 (id: JlAKpfo)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-006
  domain: CX
  subdomain: 失神
  assertion:
    plain_statement_ja: 血管迷走神経性失神では、診断と予後についての患者教育を行う（クラス I）。前兆が十分に長い患者には下肢の交差や手の握りしめなどの身体的対抗手技が有用（クラス IIa）、高血圧・心不全・尿閉のない再発例にはミドドリンが妥当（クラス IIa）、フルドロコルチゾンは考慮してよい（クラス IIb）とされる。
    condition:
      guideline: 2017 ACC/AHA/HRS 失神 GL
      region: 米国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-297
    source: 'Shen WK, Sheldon RS, Benditt DG, et al. 2017 ACC/AHA/HRS guideline for the evaluation and management of patients with syncope: executive summary. Heart Rhythm 2017;14:e218-e254'
    doi: 10.1016/j.hrthm.2017.03.005
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/2017-acc-aha-hrs-syncope-guideline-executive-summarypdf-0/download
    source_license: © 2017 American College of Cardiology Foundation, AHA, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤の国内の承認・保険適用（失神への適応）は確認していない
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-02-05-017 (id: JlAKpfo)；TBL-01-00-202 (id: Jlvnlws)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-007
  domain: CX
  subdomain: 心電図の基本所見
  assertion:
    plain_statement_ja: QT 間隔の心拍数補正には Bazett の式より線形回帰の式が勧められ、報告には補正法を明記する。Bazett の式は特に心拍数が速いときに大きな誤差を生む。心房細動など RR 間隔の変動が大きいときや T 波の終末が不明瞭なときは補正しない。
    condition:
      guideline: AHA/ACCF/HRS 心電図の標準化と判読の勧告 Part IV（2009）
      region: 米国の学会の勧告
    differential: null
    common_misconception: QTc はどの心拍数でも Bazett の式で正しく補正できる
  provenance:
    source_ref: SRC-309
    source: 'Rautaharju PM, Surawicz B, Gettes LS. AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part IV: the ST segment, T and U waves, and the QT interval. Circulation 2009;119:e241-e250'
    doi: 10.1161/CIRCULATIONAHA.108.191096
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/interpretation-electrocardiogram-part-iv-st-segment-t-and-u-waves-and-qt-intervalpdf/download
    source_license: © 2009 AHA, ACCF, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-008
  domain: CX
  subdomain: 心電図の基本所見
  assertion:
    plain_statement_ja: 成人の補正 QT 間隔は、女性で460 ms以上、男性で450 ms以上を延長とし、390 ms以下を短縮とする。
    condition:
      guideline: AHA/ACCF/HRS 心電図の標準化と判読の勧告 Part IV（2009）
      region: 米国の学会の勧告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-309
    source: 'Rautaharju PM, Surawicz B, Gettes LS. AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part IV: the ST segment, T and U waves, and the QT interval. Circulation 2009;119:e241-e250'
    doi: 10.1161/CIRCULATIONAHA.108.191096
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/interpretation-electrocardiogram-part-iv-st-segment-t-and-u-waves-and-qt-intervalpdf/download
    source_license: © 2009 AHA, ACCF, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 男性の延長の基準は本文の別の箇所で「450 msを超える」と書かれている
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-009
  domain: CX
  subdomain: 心電図の基本所見
  assertion:
    plain_statement_ja: J 点の ST 上昇の異常の閾値は、V2・V3誘導では40歳以上の男性0.2 mV、40歳未満の男性0.25 mV、女性0.15 mVで、その他の誘導では男女とも0.1 mVである。
    condition:
      guideline: AHA/ACCF/HRS 心電図の標準化と判読の勧告 Part IV（2009）
      region: 米国の学会の勧告
    differential: null
    common_misconception: ST 上昇の閾値はすべての誘導・性別で0.1 mV（1 mm）である
  provenance:
    source_ref: SRC-309
    source: 'Rautaharju PM, Surawicz B, Gettes LS. AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part IV: the ST segment, T and U waves, and the QT interval. Circulation 2009;119:e241-e250'
    doi: 10.1161/CIRCULATIONAHA.108.191096
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/interpretation-electrocardiogram-part-iv-st-segment-t-and-u-waves-and-qt-intervalpdf/download
    source_license: © 2009 AHA, ACCF, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-010
  domain: CX
  subdomain: 心電図の基本所見
  assertion:
    plain_statement_ja: 成人の完全右脚ブロックは、QRS 幅120 ms以上、V1 または V2 での rsr′・rsR′・rSR′ 型、I 誘導と V6 で R 波より長いか40 msを超える S 波で診断する。不完全右脚ブロックは QRS 幅110〜120 msである。
    condition:
      guideline: AHA/ACCF/HRS 心電図の標準化と判読の勧告 Part III（2009）
      region: 米国の学会の勧告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-310
    source: 'Surawicz B, Childers R, Deal BJ, et al. AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part III: intraventricular conduction disturbances. Circulation 2009;119:e235-e240'
    doi: 10.1161/CIRCULATIONAHA.108.191095
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/interpretation-electrocardiogram-part-iii-intraventricular-conduction-disturbancespdf/download
    source_license: © 2009 AHA, ACCF, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-011
  domain: CX
  subdomain: 心電図の基本所見
  assertion:
    plain_statement_ja: 成人の完全左脚ブロックは、QRS 幅120 ms以上、I・aVL・V5・V6 での幅広く結節のある（または不明瞭な）R 波、I・V5・V6 での q 波の欠如、V5・V6 での R 波頂点時間60 ms超で診断する。不完全左脚ブロックは QRS 幅110〜119 msである。
    condition:
      guideline: AHA/ACCF/HRS 心電図の標準化と判読の勧告 Part III（2009）
      region: 米国の学会の勧告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-310
    source: 'Surawicz B, Childers R, Deal BJ, et al. AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part III: intraventricular conduction disturbances. Circulation 2009;119:e235-e240'
    doi: 10.1161/CIRCULATIONAHA.108.191095
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/interpretation-electrocardiogram-part-iii-intraventricular-conduction-disturbancespdf/download
    source_license: © 2009 AHA, ACCF, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-012
  domain: CX
  subdomain: 心電図の基本所見
  assertion:
    plain_statement_ja: 左脚前枝ブロックは前額面の電気軸が−45°〜−90°で、aVL が qR 型、QRS 幅120 ms未満である。左脚後枝ブロックは電気軸が90°〜180°で、I・aVL が rS 型、III・aVF が qR 型、QRS 幅120 ms未満である。
    condition:
      guideline: AHA/ACCF/HRS 心電図の標準化と判読の勧告 Part III（2009）
      region: 米国の学会の勧告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-310
    source: 'Surawicz B, Childers R, Deal BJ, et al. AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part III: intraventricular conduction disturbances. Circulation 2009;119:e235-e240'
    doi: 10.1161/CIRCULATIONAHA.108.191095
    pmid: null
    pmcid: null
    url: https://hrsonline.org/documents/interpretation-electrocardiogram-part-iii-intraventricular-conduction-disturbancespdf/download
    source_license: © 2009 AHA, ACCF, HRS
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-013
  domain: CX
  subdomain: 心エコー・心臓 CT・心臓 MRI・カテーテル検査の基本
  assertion:
    plain_statement_ja: 二次元心エコーの biplane 法による左室駆出率の正常範囲は、男性52〜72%（平均62±5%）、女性54〜74%（平均64±5%）である。
    condition:
      guideline: ASE/EACVI 心腔計測の勧告 2015
      region: 米国・欧州の学会の勧告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-311
    source: 'Lang RM, Badano LP, Mor-Avi V, et al. Recommendations for cardiac chamber quantification by echocardiography in adults: an update from the American Society of Echocardiography and the European Association of Cardiovascular Imaging. J Am Soc Echocardiogr 2015;28:1-39'
    doi: 10.1016/j.echo.2014.10.003
    pmid: null
    pmcid: null
    url: https://www.asecho.org/wp-content/uploads/2018/01/ChamberQuant_Japanese.pdf
    source_license: Copyright 2015 by the American Society of Echocardiography
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本文の別の箇所に21歳以上の成人で53〜73%という記載があり、表と一致しない
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-014
  domain: CX
  subdomain: 心エコー・心臓 CT・心臓 MRI・カテーテル検査の基本
  assertion:
    plain_statement_ja: 心エコーの線形計測法による左室心筋重量係数の上限は、女性95 g/m²、男性115 g/m²である。相対的壁厚が0.42を超えるものは求心性（リモデリングまたは肥大）、0.42以下で心筋重量が増えているものは遠心性肥大とする。
    condition:
      guideline: ASE/EACVI 心腔計測の勧告 2015
      region: 米国・欧州の学会の勧告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-311
    source: 'Lang RM, Badano LP, Mor-Avi V, et al. Recommendations for cardiac chamber quantification by echocardiography in adults: an update from the American Society of Echocardiography and the European Association of Cardiovascular Imaging. J Am Soc Echocardiogr 2015;28:1-39'
    doi: 10.1016/j.echo.2014.10.003
    pmid: null
    pmcid: null
    url: https://www.asecho.org/wp-content/uploads/2018/01/ChamberQuant_Japanese.pdf
    source_license: Copyright 2015 by the American Society of Echocardiography
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-015
  domain: CX
  subdomain: 心エコー・心臓 CT・心臓 MRI・カテーテル検査の基本
  assertion:
    plain_statement_ja: 心エコーでは、左房容積係数の正常上限は男女とも34 mL/m²である。右室は、右室に焦点を当てた心尖部四腔像で基部径が41 mmを超えれば拡大とし、三尖弁輪収縮期移動距離（TAPSE）が17 mm未満なら右室の収縮能低下を示唆する。
    condition:
      guideline: ASE/EACVI 心腔計測の勧告 2015
      region: 米国・欧州の学会の勧告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-311
    source: 'Lang RM, Badano LP, Mor-Avi V, et al. Recommendations for cardiac chamber quantification by echocardiography in adults: an update from the American Society of Echocardiography and the European Association of Cardiovascular Imaging. J Am Soc Echocardiogr 2015;28:1-39'
    doi: 10.1016/j.echo.2014.10.003
    pmid: null
    pmcid: null
    url: https://www.asecho.org/wp-content/uploads/2018/01/ChamberQuant_Japanese.pdf
    source_license: Copyright 2015 by the American Society of Echocardiography
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 右室基部径の基準は「41 mm以上」と「41 mmを超える」の両方の表現がある
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-016
  domain: CX
  subdomain: 心エコー・心臓 CT・心臓 MRI・カテーテル検査の基本
  assertion:
    plain_statement_ja: 心エコーで下大静脈径が2.1 cm以下で、鼻すすり（sniff）による虚脱が50%以上なら右房圧は約3 mmHg（0〜5）、径が2.1 cmを超え虚脱が50%未満なら約15 mmHg（10〜20）と推定する。どちらにも当てはまらない場合は約8 mmHg（5〜10）とする。
    condition:
      guideline: ASE/EACVI 心腔計測の勧告 2015
      region: 米国・欧州の学会の勧告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-311
    source: 'Lang RM, Badano LP, Mor-Avi V, et al. Recommendations for cardiac chamber quantification by echocardiography in adults: an update from the American Society of Echocardiography and the European Association of Cardiovascular Imaging. J Am Soc Echocardiogr 2015;28:1-39'
    doi: 10.1016/j.echo.2014.10.003
    pmid: null
    pmcid: null
    url: https://www.asecho.org/wp-content/uploads/2018/01/ChamberQuant_Japanese.pdf
    source_license: Copyright 2015 by the American Society of Echocardiography
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 境界（2.1 cm ちょうど、50% ちょうど）の扱いは英語原本で確認が要る
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-017
  domain: CX
  subdomain: 心臓リハビリテーション
  assertion:
    plain_statement_ja: 心臓リハビリテーションは、心血管疾患の患者の身体的・心理的・社会的・職業的な状態を改善し、再発・再入院・死亡を減らすための長期的で包括的なプログラムである。医学的評価、運動処方にもとづく運動療法、冠危険因子の是正、患者教育とカウンセリング、最適な薬物療法から成り、2021年版では疾病管理が加わった。対象には、急性冠症候群、安定狭心症・PCI 後、心不全、心臓手術後、TAVI 後、不整脈・デバイス植込み後、肺高血圧症、大動脈瘤・大動脈解離、末梢動脈疾患が含まれる。
    condition:
      guideline: JCS/JACR 2021 心血管疾患リハビリテーション GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-312
    source: 日本循環器学会・日本心臓リハビリテーション学会ほか. 心血管疾患におけるリハビリテーションに関するガイドライン（2021年改訂版）. 2021年3月27日発行
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jacr.jp/cms/wp-content/uploads/2015/04/JCS2021_Makita2.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本心臓リハビリテーション学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 保険適用の対象疾患（表21・22）の本文は抽出できず未確認
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-02-05-033 (id: JlAKpgQ)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-018
  domain: CX
  subdomain: 心臓リハビリテーション
  assertion:
    plain_statement_ja: 心臓リハビリテーションは、発症・手術の当日から離床までの急性期（第 I 相）、離床後から社会復帰までの回復期（第 II 相）、社会復帰後に生涯続ける維持期（第 III 相）に分ける。急性期から運動療法へ移る目安の一つは、最後の6分間歩行試験で300 m以上歩けることである。保険で算定できる期間は150日間とされる。
    condition:
      guideline: JCS/JACR 2021 心血管疾患リハビリテーション GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-312
    source: 日本循環器学会・日本心臓リハビリテーション学会ほか. 心血管疾患におけるリハビリテーションに関するガイドライン（2021年改訂版）. 2021年3月27日発行
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jacr.jp/cms/wp-content/uploads/2015/04/JCS2021_Makita2.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本心臓リハビリテーション学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 150日の起算日と延長の条件は本文で確認が要る
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-02-05-033 (id: JlAKpgQ)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-019
  domain: CX
  subdomain: 心臓リハビリテーション
  assertion:
    plain_statement_ja: 有酸素運動の強度は、ランプ負荷の心肺運動負荷試験（CPX）で求めた嫌気性代謝閾値（AT）の1分前の仕事率で処方する。AT は最高酸素摂取量の約50〜55%にあたる。予測最高心拍数を使うと誤差が大きいため実測値を使うべきで、β遮断薬を飲んでいる患者では特に重要である。
    condition:
      guideline: JCS/JACR 2021 心血管疾患リハビリテーション GL
      region: 日本
    differential: null
    common_misconception: 運動強度は年齢からの予測最高心拍数で処方すれば十分である
  provenance:
    source_ref: SRC-312
    source: 日本循環器学会・日本心臓リハビリテーション学会ほか. 心血管疾患におけるリハビリテーションに関するガイドライン（2021年改訂版）. 2021年3月27日発行
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jacr.jp/cms/wp-content/uploads/2015/04/JCS2021_Makita2.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本心臓リハビリテーション学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: Borg 指数や Karvonen 法の係数は今回の抽出範囲になく未確認
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-02-05-033 (id: JlAKpgQ)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-020
  domain: CX
  subdomain: 心臓リハビリテーション
  assertion:
    plain_statement_ja: 心不全患者の運動療法を週3〜5回、1回40〜50分、3か月続けると、最高酸素摂取量が8〜16%改善する。
    condition:
      guideline: JCS/JACR 2021 心血管疾患リハビリテーション GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-312
    source: 日本循環器学会・日本心臓リハビリテーション学会ほか. 心血管疾患におけるリハビリテーションに関するガイドライン（2021年改訂版）. 2021年3月27日発行
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jacr.jp/cms/wp-content/uploads/2015/04/JCS2021_Makita2.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本心臓リハビリテーション学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）。心不全への心臓リハビリテーションの推奨クラスは今回の抽出範囲になく未確認
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-02-05-033 (id: JlAKpgQ)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CX-021
  domain: CX
  subdomain: 心臓リハビリテーション
  assertion:
    plain_statement_ja: 心臓リハビリテーションのガイドラインでは、労作時の呼吸困難や易疲労の原因の鑑別、予後評価のための最高酸素摂取量の測定、心移植などの適応の検討のための CPX はクラス I、運動処方のための CPX と、CPX ができない場合の6分間歩行試験はクラス IIa、ルーチン検査としての CPX はクラス III（利益なし）とされる。
    condition:
      guideline: JCS/JACR 2021 心血管疾患リハビリテーション GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-312
    source: 日本循環器学会・日本心臓リハビリテーション学会ほか. 心血管疾患におけるリハビリテーションに関するガイドライン（2021年改訂版）. 2021年3月27日発行
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jacr.jp/cms/wp-content/uploads/2015/04/JCS2021_Makita2.pdf
    source_license: （無断転載を禁ずる）© 日本循環器学会・日本心臓リハビリテーション学会
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；PS-02-06-04 (id: JkxnuQs)；TBL-02-05-033 (id: JlAKpgQ)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応

| ID | subdomain | 出題基準 | コアカリ | 出典 |
|---|---|---|---|---|
| HT-001 | 本態性高血圧 | 医学各論 Ⅴ-7-A（本態性高血圧、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-298 |
| HT-002 | 本態性高血圧 | 医学各論 Ⅴ-7-A（本態性高血圧、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-298 |
| HT-003 | 本態性高血圧 | 医学各論 Ⅴ-7-A（本態性高血圧、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-291 |
| HT-004 | 本態性高血圧 | 医学各論 Ⅴ-7-A（本態性高血圧、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-292 |
| HT-005 | 本態性高血圧 | 医学各論 Ⅴ-7-A（本態性高血圧、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-293 |
| HT-006 | 本態性高血圧 | 医学各論 Ⅴ-7-A（本態性高血圧、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-293 |
| HT-007 | 本態性高血圧 | 医学各論 Ⅴ-7-A（本態性高血圧、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-293 |
| HT-008 | 本態性高血圧 | 医学各論 Ⅴ-7-A（本態性高血圧、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-293 |
| HT-009 | 高血圧緊急症 | 医学各論 Ⅴ-7-C（高血圧緊急症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-200 (id: Jlvnlwg) | SRC-293 |
| HT-010 | 内分泌性高血圧症 | 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-294 |
| HT-011 | 内分泌性高血圧症 | 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-294 |
| HT-012 | 内分泌性高血圧症 | 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-294 |
| HT-013 | 内分泌性高血圧症 | 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-294 |
| HT-014 | 内分泌性高血圧症 | 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-294 |
| HT-015 | 内分泌性高血圧症 | 医学各論 Ⅴ-7-B-③（内分泌性高血圧症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-294 |
| HT-016 | 睡眠時無呼吸症候群 | 医学各論 Ⅴ-7-B-④（睡眠時無呼吸症候群、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-295 |
| HT-017 | 起立性低血圧 | 医学各論 Ⅴ-7-D（起立性低血圧、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-201 (id: Jlvnlwo) | SRC-296 |
| HT-018 | 起立性低血圧 | 医学各論 Ⅴ-7-D（起立性低血圧、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-201 (id: Jlvnlwo)；TBL-02-05-017 (id: JlAKpfo) | SRC-297 |
| HT-019 | 腎血管性高血圧症 | 医学各論 Ⅴ-7-B-②（腎血管性高血圧症、a）；医学各論 Ⅴ-8-A-⑤（高安動脈炎、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)；TBL-01-00-194 (id: Jlvnlvw) | SRC-305 |
| HT-020 | 腎血管性高血圧症 | 医学各論 Ⅴ-7-B-②（腎血管性高血圧症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) | SRC-307 |
| VS-001 | 胸部大動脈瘤 | 医学各論 Ⅴ-8-A-①（胸部大動脈瘤、a）；医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc) | SRC-290 |
| VS-002 | 胸部大動脈瘤 | 医学各論 Ⅴ-8-A-①（胸部大動脈瘤、a）；医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc) | SRC-290 |
| VS-003 | 腹部大動脈瘤 | 医学各論 Ⅴ-8-A-①（胸部大動脈瘤、a）；医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc) | SRC-290 |
| VS-004 | 腹部大動脈瘤 | 医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc) | SRC-301 |
| VS-005 | 腹部大動脈瘤 | 医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc) | SRC-301 |
| VS-006 | 腹部大動脈瘤 | 医学各論 Ⅴ-8-A-②（腹部大動脈瘤、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc) | SRC-301 |
| VS-007 | 大動脈解離 | 医学各論 Ⅴ-8-A-④（大動脈解離、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY) | SRC-290 |
| VS-008 | 大動脈解離 | 医学各論 Ⅴ-8-A-④（大動脈解離、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY) | SRC-290 |
| VS-009 | 大動脈解離 | 医学各論 Ⅴ-8-A-④（大動脈解離、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY) | SRC-290 |
| VS-010 | 大動脈解離 | 医学各論 Ⅴ-8-A-④（大動脈解離、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY) | SRC-290 |
| VS-011 | 大動脈解離 | 医学各論 Ⅴ-8-A-④（大動脈解離、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY) | SRC-290 |
| VS-012 | 大動脈解離 | 医学各論 Ⅴ-8-A-④（大動脈解離、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY) | SRC-290 |
| VS-013 | 大動脈解離 | 医学各論 Ⅴ-8-A-④（大動脈解離、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)；TBL-02-05-021 (id: JlAKpfI) | SRC-290 |
| VS-014 | 大動脈解離 | 医学各論 Ⅴ-8-A-④（大動脈解離、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY) | SRC-290 |
| VS-015 | 大動脈解離 | 医学各論 Ⅴ-8-A-④（大動脈解離、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY)；TBL-02-05-021 (id: JlAKpfI) | SRC-290 |
| VS-016 | 大動脈解離 | 医学各論 Ⅴ-8-A-④（大動脈解離、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-190 (id: JlvnlvY) | SRC-290 |
| VS-017 | Marfan症候群 | 医学各論 Ⅴ-8-A-⑥（Marfan症候群、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc) | SRC-302 |
| VS-018 | Marfan症候群 | 医学各論 Ⅴ-8-A-⑥（Marfan症候群、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-191 (id: Jlvnlvc) | SRC-302 |
| VS-019 | 高安動脈炎 | 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw) | SRC-304 |
| VS-020 | 高安動脈炎 | 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw) | SRC-305 |
| VS-021 | 高安動脈炎 | 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw) | SRC-304 |
| VS-022 | 高安動脈炎 | 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw) | SRC-304 |
| VS-023 | 高安動脈炎 | 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw) | SRC-304 |
| VS-024 | 高安動脈炎 | 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw) | SRC-305 |
| VS-025 | 高安動脈炎 | 医学各論 Ⅴ-8-A-⑤（高安動脈炎、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-194 (id: Jlvnlvw) | SRC-304 |
| VS-026 | Buerger病 | 医学各論 Ⅴ-8-B-④（Buerger病、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-193 (id: Jlvnlvo) | SRC-306 |
| VS-027 | Buerger病 | 医学各論 Ⅴ-8-B-④（Buerger病、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-193 (id: Jlvnlvo) | SRC-306 |
| VS-028 | Buerger病 | 医学各論 Ⅴ-8-B-④（Buerger病、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-193 (id: Jlvnlvo) | SRC-306 |
| VS-029 | 閉塞性動脈硬化症 | 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk) | SRC-307 |
| VS-030 | 閉塞性動脈硬化症 | 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk) | SRC-307 |
| VS-031 | 閉塞性動脈硬化症 | 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)；TBL-01-00-189 (id: JlvnlvQ) | SRC-307 |
| VS-032 | 閉塞性動脈硬化症 | 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk)；TBL-01-00-189 (id: JlvnlvQ) | SRC-307 |
| VS-033 | 閉塞性動脈硬化症 | 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk) | SRC-307 |
| VS-034 | 閉塞性動脈硬化症 | 医学各論 Ⅴ-8-B-①（閉塞性動脈硬化症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk) | SRC-307 |
| VS-035 | 急性動脈閉塞症 | 医学各論 Ⅴ-8-B-③（急性動脈閉塞症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk) | SRC-307 |
| VS-036 | 急性動脈閉塞症 | 医学各論 Ⅴ-8-B-③（急性動脈閉塞症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk) | SRC-307 |
| VS-037 | 急性動脈閉塞症 | 医学各論 Ⅴ-8-B-③（急性動脈閉塞症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk) | SRC-307 |
| VS-038 | 急性動脈閉塞症 | 医学各論 Ⅴ-8-B-③（急性動脈閉塞症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk) | SRC-307 |
| VS-039 | 急性動脈閉塞症 | 医学各論 Ⅴ-8-B-③（急性動脈閉塞症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-192 (id: Jlvnlvk) | SRC-307 |
| VS-040 | Raynaud症候群 | 医学各論 Ⅴ-8-B-②（Raynaud症候群、a） | PS-02-06-05 (id: JkxnuQw) | SRC-303 |
| VS-041 | Raynaud症候群 | 医学各論 Ⅴ-8-B-②（Raynaud症候群、a） | PS-02-06-05 (id: JkxnuQw) | SRC-303 |
| VS-042 | 深部静脈血栓症<DVT> | 医学各論 Ⅴ-8-C-①（深部静脈血栓症<DVT>、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-195 (id: Jlvnlv0) | SRC-308 |
| VS-043 | 深部静脈血栓症<DVT> | 医学各論 Ⅴ-8-C-①（深部静脈血栓症<DVT>、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-195 (id: Jlvnlv0) | SRC-308 |
| VS-044 | 深部静脈血栓症<DVT> | 医学各論 Ⅴ-8-C-①（深部静脈血栓症<DVT>、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-195 (id: Jlvnlv0) | SRC-308 |
| VS-045 | 深部静脈血栓症<DVT> | 医学各論 Ⅴ-8-C-①（深部静脈血栓症<DVT>、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-195 (id: Jlvnlv0) | SRC-308 |
| VS-046 | 深部静脈血栓症<DVT> | 医学各論 Ⅴ-8-C-①（深部静脈血栓症<DVT>、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-195 (id: Jlvnlv0) | SRC-308 |
| CX-001 | 循環器疾患の統計（日本） | null | PS-02-06-05 (id: JkxnuQw) | SRC-299 |
| CX-002 | 循環器疾患の統計（日本） | null | PS-02-06-05 (id: JkxnuQw) | SRC-300 |
| CX-003 | 失神 | null | PS-02-06-02 (id: JkxnuQk)；TBL-02-05-017 (id: JlAKpfo)；TBL-01-00-202 (id: Jlvnlws) | SRC-297 |
| CX-004 | 失神 | null | PS-02-06-02 (id: JkxnuQk)；TBL-02-05-017 (id: JlAKpfo)；TBL-02-05-026 (id: JlAKpf0) | SRC-297 |
| CX-005 | 失神 | null | PS-02-06-02 (id: JkxnuQk)；TBL-02-05-017 (id: JlAKpfo) | SRC-297 |
| CX-006 | 失神 | null | PS-02-06-04 (id: JkxnuQs)；TBL-02-05-017 (id: JlAKpfo)；TBL-01-00-202 (id: Jlvnlws) | SRC-297 |
| CX-007 | 心電図の基本所見 | null | PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0) | SRC-309 |
| CX-008 | 心電図の基本所見 | null | PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0) | SRC-309 |
| CX-009 | 心電図の基本所見 | null | PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0) | SRC-309 |
| CX-010 | 心電図の基本所見 | null | PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0) | SRC-310 |
| CX-011 | 心電図の基本所見 | null | PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0) | SRC-310 |
| CX-012 | 心電図の基本所見 | null | PS-02-06-03 (id: JkxnuQo)；TBL-02-05-026 (id: JlAKpf0) | SRC-310 |
| CX-013 | 心エコー・心臓 CT・心臓 MRI・カテーテル検査の基本 | null | PS-02-06-03 (id: JkxnuQo)；TBL-02-05-027 (id: JlAKpf4) | SRC-311 |
| CX-014 | 心エコー・心臓 CT・心臓 MRI・カテーテル検査の基本 | null | PS-02-06-03 (id: JkxnuQo)；TBL-02-05-027 (id: JlAKpf4) | SRC-311 |
| CX-015 | 心エコー・心臓 CT・心臓 MRI・カテーテル検査の基本 | null | PS-02-06-03 (id: JkxnuQo)；TBL-02-05-027 (id: JlAKpf4) | SRC-311 |
| CX-016 | 心エコー・心臓 CT・心臓 MRI・カテーテル検査の基本 | null | PS-02-06-03 (id: JkxnuQo)；TBL-02-05-027 (id: JlAKpf4) | SRC-311 |
| CX-017 | 心臓リハビリテーション | null | PS-02-06-04 (id: JkxnuQs)；TBL-02-05-033 (id: JlAKpgQ) | SRC-312 |
| CX-018 | 心臓リハビリテーション | null | PS-02-06-04 (id: JkxnuQs)；TBL-02-05-033 (id: JlAKpgQ) | SRC-312 |
| CX-019 | 心臓リハビリテーション | null | PS-02-06-04 (id: JkxnuQs)；TBL-02-05-033 (id: JlAKpgQ) | SRC-312 |
| CX-020 | 心臓リハビリテーション | null | PS-02-06-04 (id: JkxnuQs)；TBL-02-05-033 (id: JlAKpgQ) | SRC-312 |
| CX-021 | 心臓リハビリテーション | null | PS-02-06-03 (id: JkxnuQo)；PS-02-06-04 (id: JkxnuQs)；TBL-02-05-033 (id: JlAKpgQ) | SRC-312 |

出題基準の小項目ごとのカード数（1枚が2項目に対応する場合は両方に数えた）：

| 小項目 | カード数 |
|---|---|
| 医学各論 Ⅴ-7-A | 8 |
| 医学各論 Ⅴ-7-B-① | 0 |
| 医学各論 Ⅴ-7-B-② | 2 |
| 医学各論 Ⅴ-7-B-③ | 6 |
| 医学各論 Ⅴ-7-B-④ | 1 |
| 医学各論 Ⅴ-7-C | 1 |
| 医学各論 Ⅴ-7-D | 2 |
| 医学各論 Ⅴ-8-A-① | 3 |
| 医学各論 Ⅴ-8-A-② | 6 |
| 医学各論 Ⅴ-8-A-③ | 0 |
| 医学各論 Ⅴ-8-A-④ | 10 |
| 医学各論 Ⅴ-8-A-⑤ | 8 |
| 医学各論 Ⅴ-8-A-⑥ | 2 |
| 医学各論 Ⅴ-8-B-① | 6 |
| 医学各論 Ⅴ-8-B-② | 2 |
| 医学各論 Ⅴ-8-B-③ | 5 |
| 医学各論 Ⅴ-8-B-④ | 3 |
| 医学各論 Ⅴ-8-C-① | 5 |
| 医学各論 Ⅴ-8-D-① | 0 |

CX のカード（21件）は各論に当てはまらないため `kokushi: null` とし、コアカリは PS-02-06-02〜05 と別表2-5（失神 TBL-02-05-017、心電図 TBL-02-05-026、心臓超音波 TBL-02-05-027、心臓リハ TBL-02-05-033）を付けました。
## 4. 未解決事項（担当の目安つき）

| # | 内容 | 該当 | 担当の目安 |
|---|---|---|---|
| 1 | PMID・PMCID の確定。PMID が入っているのは SRC-290（37661428）と SRC-291（40877471）だけ。ほかは DOI か URL から API で確定する | 全 SRC | Claude Code（Phase 3） |
| 2 | 日本語版 PDF で読んだ JCS ガイドライン（SRC-304・307・308・312）の英語版（Circ J）の DOI と、英語版を出典にするかの判断。英語版の Crossref の license 欄も確認する | SRC-304・307・308・312 | Claude Code → ユーザー |
| 3 | ライセンスが UNKNOWN の出典の確認：SRC-290（J-STAGE 英語版）、SRC-291（Hypertens Res）、SRC-292（発表スライド）、SRC-295（J Bras Pneumol、CC の版） | 4件 | Claude Code |
| 4 | SRC-295 の DOI と巻・頁の確定（雑誌ページに記載がなかった） | HT-016 | Claude Code |
| 5 | JSH2025 の本文での確認：家庭血圧の目標125/75 mmHg、CQ4・CQ8 の推奨の強さ、血圧の分類、高齢者・フレイルの扱い。HT-004 は二次資料（発表スライド）経由 | HT-003・004 | ユーザー（書籍）／循環器専門医 |
| 6 | 2025 AHA/ACC 高血圧 GL は AHA 公式の要約ページで確認しただけで、本文は未確認 | HT-005〜009 | Claude Code（本文の取得）|
| 7 | 大動脈瘤・大動脈解離 GL（SRC-290）は第Ⅰ〜Ⅲ章までしか抽出できていない。部位別の手術適応径（上行・弓部・下行、Marfan 症候群・二尖弁）、拡大速度の基準、急性解離の初期の降圧・心拍数の目標、A 型の緊急手術と合併症のない B 型の内科治療の推奨クラスは未作成 | VS-002 など | 次回（補完） |
| 8 | DVT は JCS 2017 年改訂版で作成した。2025年の新しいガイドライン（JCS/JPCPHS 2025、DOI 10.1253/circj.CJ-25-1144）で数値・推奨が変わっていないかの照合が要る。DOAC の国内承認時期も未確認 | VS-042〜046 | Claude Code → 循環器専門医 |
| 9 | 指定難病の資料（SRC-305・306）の除外疾患名などは、英語の要約を経て抽出したため、原文の表記と照合する | VS-020・024・026〜028 | Claude Code |
| 10 | 原発性アルドステロン症は米国内分泌学会 2025 で作成した。日本内分泌学会 2021（Endocr J 2022、PMID 35418526）の本文は取得できず、日本の基準（対象、カットオフ、確認検査）は未作成 | HT-010〜015 | 次回（補完） |
| 11 | 内分泌性高血圧症のうち、褐色細胞腫・Cushing 症候群、腎実質性高血圧、高血圧緊急症の初期降圧の速度（日本の基準）は出典を取れず未作成 | Ⅴ-7-B-①・③、Ⅴ-7-C | 次回（補完） |
| 12 | 胸腹部大動脈瘤（Ⅴ-8-A-③）とリンパ浮腫（Ⅴ-8-D-①）はカードなし。リンパ浮腫は国際リンパ学会（ISL）の合意文書と NCI PDQ を候補にしたが取得できなかった | Ⅴ-8-A-③、Ⅴ-8-D-① | 次回（補完） |
| 13 | CX の主要症候のうち胸痛（大動脈解離以外の鑑別）・動悸・浮腫・呼吸困難、心臓 CT・MRI・カテーテル検査、主要循環器薬の作用と注意は未作成 | CX | 次回（補完） |

## 5. 次回への引き継ぎ

### 5-1. 欠番

なし（HT-001〜020、VS-001〜046、CX-001〜021 はすべて作成）。

### 5-2. カードがない出題基準の小項目（第10回の範囲）

- 医学各論 Ⅴ-7-B-①（腎実質性高血圧症、a）
- 医学各論 Ⅴ-8-A-③（胸腹部大動脈瘤、a）
- 医学各論 Ⅴ-8-D-①（リンパ浮腫、b）
- カードが1件だけ：Ⅴ-7-B-④（睡眠時無呼吸症候群）、Ⅴ-7-C（高血圧緊急症。重症高血圧との区別のみ）

### 5-3. 重複を避ける範囲（第8・9回との境界）

- 失神は CX で、定義・分類・初期評価・心原性を示唆する特徴・血管迷走神経性失神の治療だけを扱った。不整脈による失神の各論（洞不全、房室ブロック、QT 延長症候群、Brugada 症候群）は AR の範囲。
- 心電図は CX で、QT 補正と基準値、ST 上昇の閾値、脚ブロック・枝ブロックの診断基準だけを扱った。不整脈の心電図所見は AR、急性冠症候群の ST 変化の解釈は IH の範囲。
- 心エコーは CX で、正常値（LVEF、左室心筋重量、左房容積、右室、下大静脈）だけを扱った。弁膜症の重症度は VD、心不全の LVEF による区分は HF の範囲。
- 心臓リハビリテーションは CX で、定義・時期区分・運動処方・CPX の推奨を扱った。心不全の非薬物療法としての位置づけは HF の範囲。
- 大動脈解離の胸痛は VS で扱った（D ダイマー、ADD-RS、無痛性の割合）。
- 高安動脈炎の大動脈弁閉鎖不全の頻度は VS で扱った（VD では扱わない）。
- 肺血栓塞栓症は呼吸器（Ⅳ）の範囲のため、DVT のカードは肺血栓塞栓症の診断・治療に触れない形にした（抗凝固療法は VTE 共通の記載として扱った）。

### 5-4. 扱った出典（再利用するときは同じ SRC 番号を使う）

SRC-290 JCS 2020 大動脈瘤・大動脈解離 GL 英語版、SRC-291 JSH2025 Key highlights、SRC-292 JSH2025 の発表資料、SRC-293 2025 AHA/ACC 高血圧 GL、SRC-294 米国内分泌学会 原発性アルドステロン症 GL 2025、SRC-295 CPAP のメタ解析、SRC-296 MeSH 起立性低血圧、SRC-297 2017 ACC/AHA/HRS 失神 GL、SRC-298 令和5年 国民健康・栄養調査、SRC-299 令和6年 人口動態統計、SRC-300 令和5年 患者調査、SRC-301 USPSTF 2019 AAA、SRC-302 MedlinePlus Marfan、SRC-303 MedlinePlus Raynaud、SRC-304 JCS 2017 血管炎症候群 GL、SRC-305 指定難病 高安動脈炎、SRC-306 指定難病 バージャー病、SRC-307 JCS/JSVS 2022 末梢動脈疾患 GL、SRC-308 JCS 2017 PTE/DVT GL、SRC-309・310 AHA/ACCF/HRS 心電図勧告 Part IV・III、SRC-311 ASE/EACVI 心腔計測 2015、SRC-312 JCS/JACR 2021 心血管疾患リハ GL。

SRC-313〜349 は未使用（第10回の補完で使える）。

### 5-5. Claude Code での照合時に重点的に確認する点

1. 数値の照合：VS-003（嚢状瘤の形の指標）、VS-014（灌流障害の頻度）、VS-019（高安動脈炎の登録数）、CX-013・015・016（心エコーの境界値の「以上・超える」）は、抽出時の表記ゆれがあった箇所。
2. HT-004 は二次資料経由。JSH2025 本文で確認できたら出典を本文に差し替え、確認できなければ保留にする。
3. VS-034 の「日本では未承認」は2025年5月更新時点の記載。現在の承認状況を確認する。
