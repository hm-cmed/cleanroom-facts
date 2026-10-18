# 第7回 横断項目（XS-001〜XS-037）

- 作成日：2026-10-18
- 事実票：37件（XS-001〜XS-037、欠番なし）。全件 `status: draft`、`verifier: null`
- 取り込み時の注意：YAMLブロックは1つだけで、アンカー・マージキー・脚注番号は使っていません。`fact.schema.json` での検証を通過済みです。
- 形式は `docs/tasks/round2_GD_supplement.md` 第1節、番号は `docs/tasks/curriculum_reference.md` に従いました。SRC 番号は SRC-163 から振りました。
- 範囲：主要症候・検査・内視鏡・栄養のうち、第1〜6回と特別回 NG で扱っていないものに絞りました（急性下部消化管出血、鉄欠乏性貧血、抗血栓薬と内視鏡、大腸内視鏡の質の指標、肝機能検査値の異常と黄疸、低栄養の診断、周術期の栄養）。腹痛は AB、吐血は UG、腹水は LV、下痢・便秘は IN と NG で扱い済みです。
- 出典はすべて英国・欧州・国際のガイドラインで、日本の診療（保険、製剤、内視鏡学会の休薬基準など）と異なる点は `condition.region` と `uncertainty` に書きました。

## 1. 出典マスター（新規 SRC-163〜169）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 使用カード数 |
|---|---|---|---|---|---|---|
| SRC-163 | Oakland K, Chadwick G, East JE, et al. Diagnosis and management of acute lower gastrointestinal bleeding: guidelines from the British Society of Gastroenterology. Gut 2019;68:776-789 | 10.1136/gutjnl-2018-317807 | — | CC BY-NC 4.0（No commercial re-use） | RESTRICTED | 8 |
| SRC-164 | Snook J, Bhala N, Beales ILP, et al. British Society of Gastroenterology guidelines for the management of iron deficiency anaemia in adults. Gut 2021;70:2030-2051 | 10.1136/gutjnl-2021-325210 | — | CC BY-NC 4.0（No commercial re-use） | RESTRICTED | 7 |
| SRC-165 | Veitch AM, Radaelli F, Alikhan R, et al. Endoscopy in patients on antiplatelet or anticoagulant therapy: British Society of Gastroenterology (BSG) and European Society of Gastrointestinal Endoscopy (ESGE) guideline update. Gut 2021;70:1611-1628 | 10.1136/gutjnl-2021-325184 | — | CC BY-NC 4.0（No commercial re-use） | RESTRICTED | 6 |
| SRC-166 | Newsome PN, Cramb R, Davison SM, et al. Guidelines on the management of abnormal liver blood tests. Gut 2018;67:6-19 | 10.1136/gutjnl-2017-314924 | — | CC BY 4.0。ユーザー提供の刊行版PDFで確認 | OPEN | 7 |
| SRC-167 | Kaminski MF, Thomas-Gibson S, Bugajski M, et al. Performance measures for lower gastrointestinal endoscopy: a European Society of Gastrointestinal Endoscopy (ESGE) quality improvement initiative. United European Gastroenterol J 2017;5:309-334（Endoscopy 誌と同時掲載） | 10.1177/2050640617700014 | — | 未確認（リポジトリの表示は Taverne） | UNKNOWN | 2 |
| SRC-168 | Cederholm T, Jensen GL, Correia MITD, et al. GLIM criteria for the diagnosis of malnutrition - A consensus report from the global clinical nutrition community. Clin Nutr 2019;38:1-9 | 10.1016/j.clnu.2018.08.002 | — | 出版社の著作物（Elsevier。著者最終稿で確認） | RESTRICTED | 3 |
| SRC-169 | Weimann A, Braga M, Carli F, et al. ESPEN practical guideline: Clinical nutrition in surgery. Clin Nutr 2021 | — | — | 未確認（著者最終稿で確認） | UNKNOWN | 4 |

- 本文の確認元：SRC-163・164 は BSG 掲載の PDF、SRC-165 はライデン大学のリポジトリ、SRC-166 はユーザー提供の刊行版PDF（数値を機械照合）、SRC-167 はアムステルダム大学医療センターのリポジトリ（UEG Journal 版）、SRC-168 はトリエステ大学の著者最終稿、SRC-169 はノッティンガム大学の著者最終稿。
- Europe PMC は取得の制限で使えませんでした。

## 2. 事実票 YAML

```yaml
- id: XS-001
  domain: XS
  subdomain: 急性下部消化管出血
  assertion:
    plain_statement_ja: 急性下部消化管出血の発生率は人口10万人あたり33〜87人と推定され、英国の院内死亡率は3.4%である。入院中に起きた下部消化管出血では死亡率が18%と高く、赤血球輸血を4単位以上要した患者では20%と報告されている。
    condition:
      guideline: BSG 下部消化管出血 GL 2019
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-163
    source: 'Oakland K, Chadwick G, East JE, et al. Diagnosis and management of acute lower gastrointestinal bleeding: guidelines from the British Society of Gastroenterology. Gut 2019;68:776-789'
    doi: 10.1136/gutjnl-2018-317807
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2018-317807
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-02 (id: JkxnuRM)；TBL-02-07-020 (id: JlAKpkk)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-002
  domain: XS
  subdomain: 急性下部消化管出血
  assertion:
    plain_statement_ja: 急性下部消化管出血の評価では、ショック指数（心拍数÷収縮期血圧）が1を超えるものを不安定な出血とする。β遮断薬を飲んでいる患者では解釈に注意する。出血部位を最も速く低侵襲に特定できる方法は CT 血管造影である。
    condition:
      guideline: BSG 下部消化管出血 GL 2019
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: 下血ではまず緊急大腸内視鏡を行う
  provenance:
    source_ref: SRC-163
    source: 'Oakland K, Chadwick G, East JE, et al. Diagnosis and management of acute lower gastrointestinal bleeding: guidelines from the British Society of Gastroenterology. Gut 2019;68:776-789'
    doi: 10.1136/gutjnl-2018-317807
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2018-317807
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-02 (id: JkxnuRM)；TBL-02-07-020 (id: JlAKpkk)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-003
  domain: XS
  subdomain: 急性下部消化管出血
  assertion:
    plain_statement_ja: 下部消化管出血が疑われた患者の11〜15%は、最終的に上部消化管からの出血だったと報告されている。
    condition:
      guideline: BSG 下部消化管出血 GL 2019
      region: 英国の診療を前提とした推奨
    differential: 上部消化管出血
    common_misconception: 鮮血便なら出血源は必ず大腸にある
  provenance:
    source_ref: SRC-163
    source: 'Oakland K, Chadwick G, East JE, et al. Diagnosis and management of acute lower gastrointestinal bleeding: guidelines from the British Society of Gastroenterology. Gut 2019;68:776-789'
    doi: 10.1136/gutjnl-2018-317807
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2018-317807
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-02 (id: JkxnuRM)；TBL-02-07-020 (id: JlAKpkk)；TBL-02-07-019 (id: JlAKpkg)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-004
  domain: XS
  subdomain: 急性下部消化管出血
  assertion:
    plain_statement_ja: Oakland スコアは、年齢、性別、下部消化管出血による入院歴、直腸診での血液、心拍数、収縮期血圧、ヘモグロビンから計算し、8点以下なら95%の確率で安全に退院できる。
    condition:
      guideline: BSG 下部消化管出血 GL 2019
      region: 英国の診療を前提とした推奨
    differential: 上部消化管出血の Glasgow-Blatchford スコア（UG 側のカード）
    common_misconception: 下血の患者は全員入院が必要である
  provenance:
    source_ref: SRC-163
    source: 'Oakland K, Chadwick G, East JE, et al. Diagnosis and management of acute lower gastrointestinal bleeding: guidelines from the British Society of Gastroenterology. Gut 2019;68:776-789'
    doi: 10.1136/gutjnl-2018-317807
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2018-317807
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-02 (id: JkxnuRM)；TBL-02-07-020 (id: JlAKpkk)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-005
  domain: XS
  subdomain: 急性下部消化管出血
  assertion:
    plain_statement_ja: 急性下部消化管出血の輸血は、ヘモグロビン70 g/L を下回ったら行い、輸血後の目標を70〜90 g/L とする制限的な方針が勧められている。心血管疾患がある患者では80 g/L で輸血し、目標を100 g/L とする。
    condition:
      guideline: BSG 下部消化管出血 GL 2019
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: 下血ではヘモグロビンを正常値まで上げるよう輸血する
  provenance:
    source_ref: SRC-163
    source: 'Oakland K, Chadwick G, East JE, et al. Diagnosis and management of acute lower gastrointestinal bleeding: guidelines from the British Society of Gastroenterology. Gut 2019;68:776-789'
    doi: 10.1136/gutjnl-2018-317807
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2018-317807
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: 上部消化管出血の制限輸血（UG 側のカード）と同じ考え方
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-04 (id: JkxnuRU)；TBL-02-07-020 (id: JlAKpkk)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-006
  domain: XS
  subdomain: 急性下部消化管出血
  assertion:
    plain_statement_ja: 活動性の出血がない入院中の下部消化管出血の患者は、次に空いている検査枠で大腸内視鏡を受ければよい。12時間や24時間以内のルーチンの緊急大腸内視鏡を支持する根拠はない。
    condition:
      guideline: BSG 下部消化管出血 GL 2019
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: 下血の患者は24時間以内に大腸内視鏡を行わなければならない
  provenance:
    source_ref: SRC-163
    source: 'Oakland K, Chadwick G, East JE, et al. Diagnosis and management of acute lower gastrointestinal bleeding: guidelines from the British Society of Gastroenterology. Gut 2019;68:776-789'
    doi: 10.1136/gutjnl-2018-317807
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2018-317807
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-020 (id: JlAKpkk)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-007
  domain: XS
  subdomain: 急性下部消化管出血
  assertion:
    plain_statement_ja: 下部消化管出血を起こした患者では、心血管疾患の一次予防のために飲んでいるアスピリンは永久に中止し、二次予防のアスピリンはルーチンには中止しない。直接経口抗凝固薬（DOAC）とワルファリンは来院時に中断し、血栓リスクが低ければワルファリンは7日後に再開する。
    condition:
      guideline: BSG 下部消化管出血 GL 2019
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: 消化管出血を起こしたら抗血栓薬はすべて永久に中止する
  provenance:
    source_ref: SRC-163
    source: 'Oakland K, Chadwick G, East JE, et al. Diagnosis and management of acute lower gastrointestinal bleeding: guidelines from the British Society of Gastroenterology. Gut 2019;68:776-789'
    doi: 10.1136/gutjnl-2018-317807
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2018-317807
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: 大腸憩室出血後の抗血栓薬の再開（IN 側のカード）
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-04 (id: JkxnuRU)；TBL-02-07-020 (id: JlAKpkk)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-008
  domain: XS
  subdomain: 急性下部消化管出血
  assertion:
    plain_statement_ja: 英国で下部消化管出血の原因として最も多いのは憩室出血で、良性の肛門・直腸疾患は16.7%を占めた。入院した患者の23%は、診断がつかないまま退院していた。
    condition:
      guideline: BSG 下部消化管出血 GL 2019
      region: 英国の診療を前提とした推奨
    differential: 大腸憩室出血の詳細は IN 側のカードで扱い済み
    common_misconception: null
  provenance:
    source_ref: SRC-163
    source: 'Oakland K, Chadwick G, East JE, et al. Diagnosis and management of acute lower gastrointestinal bleeding: guidelines from the British Society of Gastroenterology. Gut 2019;68:776-789'
    doi: 10.1136/gutjnl-2018-317807
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2018-317807
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-02 (id: JkxnuRM)；TBL-02-07-020 (id: JlAKpkk)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-009
  domain: XS
  subdomain: 鉄欠乏性貧血と消化管の精査
  assertion:
    plain_statement_ja: 貧血はヘモグロビンが基準値の下限を下回る状態と定義され、WHO の基準では15歳を超える男性で130 g/L 未満、妊娠していない15歳を超える女性で120 g/L 未満である。鉄欠乏性貧血は、先進国の成人男性と閉経後女性の2〜5%にみられる。
    condition:
      guideline: BSG 鉄欠乏性貧血 GL 2021
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-164
    source: Snook J, Bhala N, Beales ILP, et al. British Society of Gastroenterology guidelines for the management of iron deficiency anaemia in adults. Gut 2021;70:2030-2051
    doi: 10.1136/gutjnl-2021-325210
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325210
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-010
  domain: XS
  subdomain: 鉄欠乏性貧血と消化管の精査
  assertion:
    plain_statement_ja: 血清フェリチン15 µg/L 未満は貯蔵鉄の枯渇を示し、30 µg/L 未満は一般に貯蔵鉄の低下を示す。BSG 2021 は、感度と特異度の兼ね合いから45 µg/L を鉄欠乏の目安として提案している。炎症性疾患があると、鉄欠乏があってもフェリチンが見かけ上正常になることがある。
    condition:
      guideline: BSG 鉄欠乏性貧血 GL 2021
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: フェリチンが正常範囲なら鉄欠乏は否定できる
  provenance:
    source_ref: SRC-164
    source: Snook J, Bhala N, Beales ILP, et al. British Society of Gastroenterology guidelines for the management of iron deficiency anaemia in adults. Gut 2021;70:2030-2051
    doi: 10.1136/gutjnl-2021-325210
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325210
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-011
  domain: XS
  subdomain: 鉄欠乏性貧血と消化管の精査
  assertion:
    plain_statement_ja: 鉄欠乏性貧血では、癌が見つかるのは8〜10%だが、約3分の1に意味のある消化管の病変が見つかる。新たに鉄欠乏性貧血と診断された男性と閉経後女性では、上部消化管内視鏡と大腸内視鏡の両方を最初の消化管の検査とする。大腸内視鏡が適さなければ CT コロノグラフィーで代える。
    condition:
      guideline: BSG 鉄欠乏性貧血 GL 2021
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: 鉄欠乏性貧血は鉄剤を出して経過をみればよい
  provenance:
    source_ref: SRC-164
    source: Snook J, Bhala N, Beales ILP, et al. British Society of Gastroenterology guidelines for the management of iron deficiency anaemia in adults. Gut 2021;70:2030-2051
    doi: 10.1136/gutjnl-2021-325210
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325210
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 癌と病変の頻度はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-012
  domain: XS
  subdomain: 鉄欠乏性貧血と消化管の精査
  assertion:
    plain_statement_ja: 閉経前の若い女性の鉄欠乏性貧血は、それだけでは内視鏡検査の適応にならない。50歳以上、月経がない、警告症状がある、遺伝的な高リスクがある、月経量に見合わない再発を繰り返す、といった場合は精査する。
    condition:
      guideline: BSG 鉄欠乏性貧血 GL 2021
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: 鉄欠乏性貧血は年齢や性別にかかわらず全員内視鏡を行う
  provenance:
    source_ref: SRC-164
    source: Snook J, Bhala N, Beales ILP, et al. British Society of Gastroenterology guidelines for the management of iron deficiency anaemia in adults. Gut 2021;70:2030-2051
    doi: 10.1136/gutjnl-2021-325210
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325210
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-013
  domain: XS
  subdomain: 鉄欠乏性貧血と消化管の精査
  assertion:
    plain_statement_ja: 鉄欠乏性貧血の初期検査では、セリアック病を血清学的検査か小腸生検で全例調べ（鉄欠乏性貧血の3〜5%にみられる）、尿検査で顕微鏡的血尿も確認する。便潜血の免疫法（FIT）は、鉄欠乏性貧血のリスク層別化や大腸癌の除外に使う根拠が現時点では不十分とされている。
    condition:
      guideline: BSG 鉄欠乏性貧血 GL 2021
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: 便潜血が陰性なら鉄欠乏性貧血の大腸の精査は不要である
  provenance:
    source_ref: SRC-164
    source: Snook J, Bhala N, Beales ILP, et al. British Society of Gastroenterology guidelines for the management of iron deficiency anaemia in adults. Gut 2021;70:2030-2051
    doi: 10.1136/gutjnl-2021-325210
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325210
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: セリアック病の診断は IN 側のカード
  uncertainty: セリアック病の頻度はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-014
  domain: XS
  subdomain: 鉄欠乏性貧血と消化管の精査
  assertion:
    plain_statement_ja: 上下部内視鏡で原因が見つからない鉄欠乏性貧血で、鉄剤への反応が不十分か再発を繰り返す場合は、小腸と腎・尿路を追加で調べる。小腸の検査にはカプセル内視鏡が第1選択とされる。
    condition:
      guideline: BSG 鉄欠乏性貧血 GL 2021
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-164
    source: Snook J, Bhala N, Beales ILP, et al. British Society of Gastroenterology guidelines for the management of iron deficiency anaemia in adults. Gut 2021;70:2030-2051
    doi: 10.1136/gutjnl-2021-325210
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325210
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-015
  domain: XS
  subdomain: 鉄欠乏性貧血と消化管の精査
  assertion:
    plain_statement_ja: 鉄欠乏性貧血の初期治療は、硫酸鉄、フマル酸鉄、グルコン酸鉄の錠剤を1日1錠とすることが勧められている。1日1回、元素鉄で50〜100 mg を空腹時に飲むことが提案され、1日おきの投与も検討されている。
    condition:
      guideline: BSG 鉄欠乏性貧血 GL 2021
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: 鉄剤は多く飲むほど早く効くので1日に何回も飲む
  provenance:
    source_ref: SRC-164
    source: Snook J, Bhala N, Beales ILP, et al. British Society of Gastroenterology guidelines for the management of iron deficiency anaemia in adults. Gut 2021;70:2030-2051
    doi: 10.1136/gutjnl-2021-325210
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325210
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 英国の製剤を前提とした記述。日本の製剤と用量は添付文書で確認する
  curriculum:
    core_curriculum: 'PS-02-08-04 (id: JkxnuRU)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-016
  domain: XS
  subdomain: 抗血栓薬服用者の内視鏡
  assertion:
    plain_statement_ja: BSG/ESGE 2021 は内視鏡の処置を出血リスクで分けている。低リスクは生検を含む診断的内視鏡、胆管・膵管ステント、消化管ステントなどで、高リスクはポリープ切除、乳頭括約筋切開を伴う ERCP、EMR・ESD、経皮内視鏡的胃瘻造設術（PEG）、EUS 下の穿刺や治療などである。1 cm 未満のポリープは、クロピドグレル単剤を続けたままコールドスネアで切除することも考えられる。
    condition:
      guideline: BSG/ESGE 抗血栓薬と内視鏡 GL 2021
      region: 英国・欧州
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-165
    source: 'Veitch AM, Radaelli F, Alikhan R, et al. Endoscopy in patients on antiplatelet or anticoagulant therapy: British Society of Gastroenterology (BSG) and European Society of Gastrointestinal Endoscopy (ESGE) guideline update. Gut 2021;70:1611-1628'
    doi: 10.1136/gutjnl-2021-325184
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325184
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本の消化器内視鏡学会の指針とは分類と対応が一部異なる
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-017
  domain: XS
  subdomain: 抗血栓薬服用者の内視鏡
  assertion:
    plain_statement_ja: 出血の低リスクの内視鏡では、P2Y12 受容体拮抗薬は単剤でも2剤併用でも続け、ワルファリンも続ける（処置前1週間の INR が治療域を超えていないことを確認する）。直接経口抗凝固薬（DOAC）は、検査当日の朝の分を飛ばすことが提案されている。
    condition:
      guideline: BSG/ESGE 抗血栓薬と内視鏡 GL 2021
      region: 英国・欧州
    differential: null
    common_misconception: 生検をするなら抗血栓薬は必ず休薬する
  provenance:
    source_ref: SRC-165
    source: 'Veitch AM, Radaelli F, Alikhan R, et al. Endoscopy in patients on antiplatelet or anticoagulant therapy: British Society of Gastroenterology (BSG) and European Society of Gastrointestinal Endoscopy (ESGE) guideline update. Gut 2021;70:1611-1628'
    doi: 10.1136/gutjnl-2021-325184
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325184
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-018
  domain: XS
  subdomain: 抗血栓薬服用者の内視鏡
  assertion:
    plain_statement_ja: 出血の高リスクの内視鏡では、抗血小板薬2剤併用中もアスピリンは続ける。血栓リスクが低ければ P2Y12 受容体拮抗薬を処置の7日前にやめ、血栓リスクが高ければアスピリンを続けつつ循環器内科医と相談する。ワルファリンは、血栓リスクが低ければ5日前にやめて処置前に INR 1.5未満を確認し、高ければ低分子ヘパリンに置き換える。
    condition:
      guideline: BSG/ESGE 抗血栓薬と内視鏡 GL 2021
      region: 英国・欧州
    differential: null
    common_misconception: 出血の高リスクの処置ではアスピリンも必ず休薬する
  provenance:
    source_ref: SRC-165
    source: 'Veitch AM, Radaelli F, Alikhan R, et al. Endoscopy in patients on antiplatelet or anticoagulant therapy: British Society of Gastroenterology (BSG) and European Society of Gastrointestinal Endoscopy (ESGE) guideline update. Gut 2021;70:1611-1628'
    doi: 10.1136/gutjnl-2021-325184
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325184
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-019
  domain: XS
  subdomain: 抗血栓薬服用者の内視鏡
  assertion:
    plain_statement_ja: 出血の高リスクの内視鏡では、DOAC の最終服用を処置の3日前とすることが推奨されている。ダビガトランでクレアチニン・クリアランス30〜50 mL/min の場合は5日前とする。処置後の抗凝固薬は、出血と血栓のリスクに応じて2〜3日以内に再開する。
    condition:
      guideline: BSG/ESGE 抗血栓薬と内視鏡 GL 2021
      region: 英国・欧州
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-165
    source: 'Veitch AM, Radaelli F, Alikhan R, et al. Endoscopy in patients on antiplatelet or anticoagulant therapy: British Society of Gastroenterology (BSG) and European Society of Gastrointestinal Endoscopy (ESGE) guideline update. Gut 2021;70:1611-1628'
    doi: 10.1136/gutjnl-2021-325184
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325184
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 「最終服用を3日前」の表現はガイドラインの記述どおり。日本の指針とは休薬期間が異なる
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-020
  domain: XS
  subdomain: 抗血栓薬服用者の内視鏡
  assertion:
    plain_statement_ja: 血栓リスクが高い状態として、機械弁（僧帽弁位、施設によっては大動脈弁位）、心房細動を伴う人工弁、僧帽弁狭窄を伴う心房細動、3か月以内の脳卒中・一過性脳虚血発作を伴う心房細動、3か月以内の静脈血栓塞栓症などが挙げられている。
    condition:
      guideline: BSG/ESGE 抗血栓薬と内視鏡 GL 2021
      region: 英国・欧州
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-165
    source: 'Veitch AM, Radaelli F, Alikhan R, et al. Endoscopy in patients on antiplatelet or anticoagulant therapy: British Society of Gastroenterology (BSG) and European Society of Gastrointestinal Endoscopy (ESGE) guideline update. Gut 2021;70:1611-1628'
    doi: 10.1136/gutjnl-2021-325184
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325184
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-021
  domain: XS
  subdomain: 抗血栓薬服用者の内視鏡
  assertion:
    plain_statement_ja: 急性消化管出血では、二次予防のアスピリンはルーチンには中止せず、P2Y12 受容体拮抗薬は必要なら5日以内に再開する。ビタミン K 拮抗薬を服用中で循環が不安定なら、ビタミン K の静注と4因子含有プロトロンビン複合体製剤を投与する。長期の抗凝固が必要な患者では出血後に再開し、血栓リスクが低ければ7日以降できるだけ早く、高ければヘパリンでつなぎながら3日以内を目安に再開する。
    condition:
      guideline: BSG/ESGE 抗血栓薬と内視鏡 GL 2021
      region: 英国・欧州
    differential: null
    common_misconception: 消化管出血のあとは抗凝固薬を再開しない
  provenance:
    source_ref: SRC-165
    source: 'Veitch AM, Radaelli F, Alikhan R, et al. Endoscopy in patients on antiplatelet or anticoagulant therapy: British Society of Gastroenterology (BSG) and European Society of Gastrointestinal Endoscopy (ESGE) guideline update. Gut 2021;70:1611-1628'
    doi: 10.1136/gutjnl-2021-325184
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2021-325184
    source_license: CC BY-NC 4.0（No commercial re-use）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: 下部消化管出血での抗血栓薬の扱い（SRC-163）と整合
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-04 (id: JkxnuRU)；TBL-02-07-019 (id: JlAKpkg)；TBL-02-07-020 (id: JlAKpkk)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-022
  domain: XS
  subdomain: 大腸内視鏡の質の指標
  assertion:
    plain_statement_ja: ESGE は大腸内視鏡の主要な質の指標と最低基準を、腸管前処置が適切な割合90%以上、盲腸到達率90%以上、腺腫発見率（ADR）25%以上と定めている。前処置と盲腸到達率の目標値はいずれも95%である。
    condition:
      guideline: ESGE 下部消化管内視鏡の質の指標 2017
    differential: null
    common_misconception: 腺腫発見率は内視鏡医の技量と関係しない
  provenance:
    source_ref: SRC-167
    source: 'Kaminski MF, Thomas-Gibson S, Bugajski M, et al. Performance measures for lower gastrointestinal endoscopy: a European Society of Gastrointestinal Endoscopy (ESGE) quality improvement initiative. United European Gastroenterol J 2017;5:309-334（Endoscopy 誌と同時掲載）'
    doi: 10.1177/2050640617700014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1177/2050640617700014
    source_license: 未確認（リポジトリの表示は Taverne）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-023
  domain: XS
  subdomain: 大腸内視鏡の質の指標
  assertion:
    plain_statement_ja: ESGE は大腸内視鏡の抜去時間の最低基準を平均6分、目標を平均10分としている。適切なポリープ切除の手技は最低80%・目標90%、合併症の指標として7日以内の再入院率0.5%以下を最低基準としている。
    condition:
      guideline: ESGE 下部消化管内視鏡の質の指標 2017
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-167
    source: 'Kaminski MF, Thomas-Gibson S, Bugajski M, et al. Performance measures for lower gastrointestinal endoscopy: a European Society of Gastrointestinal Endoscopy (ESGE) quality improvement initiative. United European Gastroenterol J 2017;5:309-334（Endoscopy 誌と同時掲載）'
    doi: 10.1177/2050640617700014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1177/2050640617700014
    source_license: 未確認（リポジトリの表示は Taverne）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-024
  domain: XS
  subdomain: 肝機能検査値の異常と黄疸
  assertion:
    plain_statement_ja: BSG 2018 は、標準の肝機能検査として、ビリルビン、アルブミン、ALT、ALP、γ-GT を勧めている（12か月以内になければ血算も加える）。肝機能検査の異常はよくみられ、英国の研究では検査依頼の2〜3割程度に1項目以上の異常があった。
    condition:
      guideline: BSG 肝機能検査値異常 GL 2018
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-166
    source: Newsome PN, Cramb R, Davison SM, et al. Guidelines on the management of abnormal liver blood tests. Gut 2018;67:6-19
    doi: 10.1136/gutjnl-2017-314924
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2017-314924
    source_license: CC BY 4.0。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 異常の頻度はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-023 (id: JlAKpks)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-025
  domain: XS
  subdomain: 肝機能検査値の異常と黄疸
  assertion:
    plain_statement_ja: 肝機能検査値の異常の臨床的な重要性は、異常の程度ではなく、どの項目が異常かと臨床的な状況で決まる。BSG 2018 は、肝機能検査値に異常がある患者では、異常の程度や持続期間にかかわらず、標準の原因検索を考慮するよう勧めている。
    condition:
      guideline: BSG 肝機能検査値異常 GL 2018
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: 肝機能検査値の異常は値が高いほど重要である
  provenance:
    source_ref: SRC-166
    source: Newsome PN, Cramb R, Davison SM, et al. Guidelines on the management of abnormal liver blood tests. Gut 2018;67:6-19
    doi: 10.1136/gutjnl-2017-314924
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2017-314924
    source_license: CC BY 4.0。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-023 (id: JlAKpks)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-026
  domain: XS
  subdomain: 肝機能検査値の異常と黄疸
  assertion:
    plain_statement_ja: 成人の肝機能異常の標準の原因検索として、腹部超音波検査、HBs 抗原、HCV 抗体（陽性なら PCR）、抗ミトコンドリア抗体、抗平滑筋抗体、抗核抗体、血清免疫グロブリン、血清フェリチンとトランスフェリン飽和度の同時測定が挙げられている。
    condition:
      guideline: BSG 肝機能検査値異常 GL 2018
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-166
    source: Newsome PN, Cramb R, Davison SM, et al. Guidelines on the management of abnormal liver blood tests. Gut 2018;67:6-19
    doi: 10.1136/gutjnl-2017-314924
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2017-314924
    source_license: CC BY 4.0。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-023 (id: JlAKpks)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-027
  domain: XS
  subdomain: 肝機能検査値の異常と黄疸
  assertion:
    plain_statement_ja: ビリルビンだけが高い場合に最も多い原因は Gilbert 症候群で、溶血がなく主に非抱合型であればほぼ Gilbert 症候群である。Gilbert 症候群は人口の5〜8%にみられる。
    condition:
      guideline: BSG 肝機能検査値異常 GL 2018
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: ビリルビン高値は必ず肝障害を意味する
  provenance:
    source_ref: SRC-166
    source: Newsome PN, Cramb R, Davison SM, et al. Guidelines on the management of abnormal liver blood tests. Gut 2018;67:6-19
    doi: 10.1136/gutjnl-2017-314924
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2017-314924
    source_license: CC BY 4.0。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: OPEN
    corroboration: Gilbert 症候群の病態は LV 側のカード
  uncertainty: 有病率はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-023 (id: JlAKpks)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-028
  domain: XS
  subdomain: 肝機能検査値の異常と黄疸
  assertion:
    plain_statement_ja: ALP が高いときは、γ-GT を測ると肝由来か肝以外（骨など）由来かの見当がつく。γ-GT は腎臓、腸、前立腺、膵臓にもあるが骨にはない。
    condition:
      guideline: BSG 肝機能検査値異常 GL 2018
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: ALP が高ければ必ず胆道系の異常である
  provenance:
    source_ref: SRC-166
    source: Newsome PN, Cramb R, Davison SM, et al. Guidelines on the management of abnormal liver blood tests. Gut 2018;67:6-19
    doi: 10.1136/gutjnl-2017-314924
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2017-314924
    source_license: CC BY 4.0。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-023 (id: JlAKpks)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-029
  domain: XS
  subdomain: 肝機能検査値の異常と黄疸
  assertion:
    plain_statement_ja: BSG 2018 は、NAFLD の線維化の評価に FIB-4 などを使うことを勧め、FIB-4 1.3未満（65歳以上は2.0未満）を低リスク、1.3〜3.25を判定保留、3.25超を専門医紹介としている。判定保留では ELF 検査（9.5超）や Fibroscan（7.8 kPa 超）で紹介を考える。
    condition:
      guideline: BSG 肝機能検査値異常 GL 2018
      region: 英国の診療を前提とした推奨
    differential: 高齢者では FIB-4 が高く出やすい
    common_misconception: null
  provenance:
    source_ref: SRC-166
    source: Newsome PN, Cramb R, Davison SM, et al. Guidelines on the management of abnormal liver blood tests. Gut 2018;67:6-19
    doi: 10.1136/gutjnl-2017-314924
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2017-314924
    source_license: CC BY 4.0。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: OPEN
    corroboration: 日本の NAFLD/NASH 診療GL での FIB-4 の使い方は LV 側のカード
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-030
  domain: XS
  subdomain: 肝機能検査値の異常と黄疸
  assertion:
    plain_statement_ja: BSG 2018 は、AUDIT スコア19超のアルコール依存はアルコール診療に紹介し、有害な飲酒（男性週50単位、女性週35単位）があって進行した肝疾患の所見か Fibroscan 16 kPa 超があれば肝臓専門医に紹介することを勧めている。原因不明の黄疸や肝胆道の悪性腫瘍の疑いは、ただちに紹介する。
    condition:
      guideline: BSG 肝機能検査値異常 GL 2018
      region: 英国の診療を前提とした推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-166
    source: Newsome PN, Cramb R, Davison SM, et al. Guidelines on the management of abnormal liver blood tests. Gut 2018;67:6-19
    doi: 10.1136/gutjnl-2017-314924
    pmid: null
    pmcid: null
    url: https://doi.org/10.1136/gutjnl-2017-314924
    source_license: CC BY 4.0。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 英国の単位（1単位＝純アルコール8 g）を前提とする
  curriculum:
    core_curriculum: 'PS-02-08-03 (id: JkxnuRQ)；TBL-02-07-023 (id: JlAKpks)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-031
  domain: XS
  subdomain: 低栄養の診断（GLIM）
  assertion:
    plain_statement_ja: GLIM 基準による低栄養の診断は2段階で、まず妥当性が確かめられたスクリーニング法で低栄養のリスクがある人を見つけ、次に診断と重症度の判定を行う。診断には、表現型の基準（体重減少、低い BMI、筋肉量の減少）と病因の基準（食事摂取量・吸収の低下、炎症・疾患の負担）を少なくとも1つずつ満たす必要がある。
    condition:
      guideline: GLIM 基準 2019
    differential: null
    common_misconception: BMI が正常なら低栄養ではない
  provenance:
    source_ref: SRC-168
    source: Cederholm T, Jensen GL, Correia MITD, et al. GLIM criteria for the diagnosis of malnutrition - A consensus report from the global clinical nutrition community. Clin Nutr 2019;38:1-9
    doi: 10.1016/j.clnu.2018.08.002
    pmid: null
    pmcid: null
    url: https://doi.org/10.1016/j.clnu.2018.08.002
    source_license: 出版社の著作物（Elsevier。著者最終稿で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-02 (id: JkxnuRM)；TBL-02-07-032 (id: JlAKplM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-032
  domain: XS
  subdomain: 低栄養の診断（GLIM）
  assertion:
    plain_statement_ja: GLIM 基準の表現型の基準は、体重減少が6か月以内で5%超か6か月を超えて10%超、BMI が70歳未満で20未満・70歳以上で22未満（アジアでは70歳未満で18.5未満・70歳以上で20未満）、体組成の測定などでの筋肉量の減少である。
    condition:
      guideline: GLIM 基準 2019
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-168
    source: Cederholm T, Jensen GL, Correia MITD, et al. GLIM criteria for the diagnosis of malnutrition - A consensus report from the global clinical nutrition community. Clin Nutr 2019;38:1-9
    doi: 10.1016/j.clnu.2018.08.002
    pmid: null
    pmcid: null
    url: https://doi.org/10.1016/j.clnu.2018.08.002
    source_license: 出版社の著作物（Elsevier。著者最終稿で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 不等号（以上・以下）は著者最終稿の抽出で一部欠けており、刊行版で確認する
  curriculum:
    core_curriculum: 'PS-02-08-02 (id: JkxnuRM)；TBL-02-07-032 (id: JlAKplM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-033
  domain: XS
  subdomain: 低栄養の診断（GLIM）
  assertion:
    plain_statement_ja: GLIM 基準の病因の基準のうち摂取量の低下は、必要エネルギーの50%以下が1週間を超えて続く、何らかの低下が2週間を超えて続く、または吸収を妨げる慢性の消化管の病態がある場合をいう。重症度は表現型の基準で分け、重度（ステージ2）は6か月以内の体重減少10%超か6か月超で20%超、BMI 70歳未満18.5未満・70歳以上20未満などとする。
    condition:
      guideline: GLIM 基準 2019
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-168
    source: Cederholm T, Jensen GL, Correia MITD, et al. GLIM criteria for the diagnosis of malnutrition - A consensus report from the global clinical nutrition community. Clin Nutr 2019;38:1-9
    doi: 10.1016/j.clnu.2018.08.002
    pmid: null
    pmcid: null
    url: https://doi.org/10.1016/j.clnu.2018.08.002
    source_license: 出版社の著作物（Elsevier。著者最終稿で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 不等号は著者最終稿の抽出で一部欠けており、刊行版で確認する
  curriculum:
    core_curriculum: 'PS-02-08-02 (id: JkxnuRM)；TBL-02-07-032 (id: JlAKplM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-034
  domain: XS
  subdomain: 周術期の栄養管理
  assertion:
    plain_statement_ja: ESPEN は、6か月以内の体重減少10〜15%超、BMI 18.5未満、SGA で C 判定か NRS 5超、肝・腎機能障害のない血清アルブミン30 g/L 未満のいずれかがあれば、重度の栄養リスクとしている。重度の栄養リスクのある患者では、7〜14日の術前栄養療法を行うことが考えられる。
    condition:
      guideline: ESPEN 周術期栄養 実践GL 2021
    differential: null
    common_misconception: 手術前の栄養状態は手術成績に影響しない
  provenance:
    source_ref: SRC-169
    source: 'Weimann A, Braga M, Carli F, et al. ESPEN practical guideline: Clinical nutrition in surgery. Clin Nutr 2021'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認（著者最終稿で確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-04 (id: JkxnuRU)；TBL-02-07-032 (id: JlAKplM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-035
  domain: XS
  subdomain: 周術期の栄養管理
  assertion:
    plain_statement_ja: ESPEN は、多くの患者で前夜からの絶食は不要とし、誤嚥のリスクが特にない患者では麻酔の2時間前まで清澄水、6時間前まで固形食をとってよいとしている。術後は多くの患者で数時間以内に清澄水を含む経口摂取を始める。
    condition:
      guideline: ESPEN 周術期栄養 実践GL 2021
    differential: null
    common_misconception: 手術前は前日の夜から絶飲食にしなければならない
  provenance:
    source_ref: SRC-169
    source: 'Weimann A, Braga M, Carli F, et al. ESPEN practical guideline: Clinical nutrition in surgery. Clin Nutr 2021'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認（著者最終稿で確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-04 (id: JkxnuRU)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-036
  domain: XS
  subdomain: 周術期の栄養管理
  assertion:
    plain_statement_ja: ESPEN は、経腸栄養が必要な手術患者では術後24時間以内に開始し、少量から5〜7日かけて慎重に増やすことを勧めている。経口と経腸で必要量の50%未満が7日を超えて続く場合は、静脈栄養を併用する。腸閉塞などで経腸栄養ができない場合は、できるだけ早く静脈栄養を始める。
    condition:
      guideline: ESPEN 周術期栄養 実践GL 2021
    differential: null
    common_misconception: 手術後はまず静脈栄養を行い、経腸栄養は1週間以上あとから始める
  provenance:
    source_ref: SRC-169
    source: 'Weimann A, Braga M, Carli F, et al. ESPEN practical guideline: Clinical nutrition in surgery. Clin Nutr 2021'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認（著者最終稿で確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-04 (id: JkxnuRU)；TBL-02-07-032 (id: JlAKplM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: XS-037
  domain: XS
  subdomain: 周術期の栄養管理
  assertion:
    plain_statement_ja: 高度の低栄養の患者に栄養を急に増やすとリフィーディング症候群を起こすおそれがあるため、段階的に増量し、検査値と心電図を監視しながら、カリウム、マグネシウム、リン、チアミンを補う。
    condition:
      guideline: ESPEN 周術期栄養 実践GL 2021
    differential: null
    common_misconception: 低栄養の患者には最初から目標量の栄養を入れるのがよい
  provenance:
    source_ref: SRC-169
    source: 'Weimann A, Braga M, Carli F, et al. ESPEN practical guideline: Clinical nutrition in surgery. Clin Nutr 2021'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認（著者最終稿で確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-04 (id: JkxnuRU)；TBL-02-07-032 (id: JlAKplM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カード一覧

| ID | 区分 | 出典 | 主張（冒頭） |
|---|---|---|---|
| XS-001 | 急性下部消化管出血 | SRC-163 | 急性下部消化管出血の発生率は人口10万人あたり33〜87人と推定され、英国の院内… |
| XS-002 | 急性下部消化管出血 | SRC-163 | 急性下部消化管出血の評価では、ショック指数（心拍数÷収縮期血圧）が1を超えるもの… |
| XS-003 | 急性下部消化管出血 | SRC-163 | 下部消化管出血が疑われた患者の11〜15%は、最終的に上部消化管からの出血だった… |
| XS-004 | 急性下部消化管出血 | SRC-163 | Oakland スコアは、年齢、性別、下部消化管出血による入院歴、直腸診での血液… |
| XS-005 | 急性下部消化管出血 | SRC-163 | 急性下部消化管出血の輸血は、ヘモグロビン70 g/L を下回ったら行い、輸血後の… |
| XS-006 | 急性下部消化管出血 | SRC-163 | 活動性の出血がない入院中の下部消化管出血の患者は、次に空いている検査枠で大腸内視… |
| XS-007 | 急性下部消化管出血 | SRC-163 | 下部消化管出血を起こした患者では、心血管疾患の一次予防のために飲んでいるアスピリ… |
| XS-008 | 急性下部消化管出血 | SRC-163 | 英国で下部消化管出血の原因として最も多いのは憩室出血で、良性の肛門・直腸疾患は1… |
| XS-009 | 鉄欠乏性貧血と消化管の精査 | SRC-164 | 貧血はヘモグロビンが基準値の下限を下回る状態と定義され、WHO の基準では15歳… |
| XS-010 | 鉄欠乏性貧血と消化管の精査 | SRC-164 | 血清フェリチン15 µg/L 未満は貯蔵鉄の枯渇を示し、30 µg/L 未満は一… |
| XS-011 | 鉄欠乏性貧血と消化管の精査 | SRC-164 | 鉄欠乏性貧血では、癌が見つかるのは8〜10%だが、約3分の1に意味のある消化管の… |
| XS-012 | 鉄欠乏性貧血と消化管の精査 | SRC-164 | 閉経前の若い女性の鉄欠乏性貧血は、それだけでは内視鏡検査の適応にならない。50歳… |
| XS-013 | 鉄欠乏性貧血と消化管の精査 | SRC-164 | 鉄欠乏性貧血の初期検査では、セリアック病を血清学的検査か小腸生検で全例調べ（鉄欠… |
| XS-014 | 鉄欠乏性貧血と消化管の精査 | SRC-164 | 上下部内視鏡で原因が見つからない鉄欠乏性貧血で、鉄剤への反応が不十分か再発を繰り… |
| XS-015 | 鉄欠乏性貧血と消化管の精査 | SRC-164 | 鉄欠乏性貧血の初期治療は、硫酸鉄、フマル酸鉄、グルコン酸鉄の錠剤を1日1錠とする… |
| XS-016 | 抗血栓薬服用者の内視鏡 | SRC-165 | BSG/ESGE 2021 は内視鏡の処置を出血リスクで分けている。低リスクは生… |
| XS-017 | 抗血栓薬服用者の内視鏡 | SRC-165 | 出血の低リスクの内視鏡では、P2Y12 受容体拮抗薬は単剤でも2剤併用でも続け、… |
| XS-018 | 抗血栓薬服用者の内視鏡 | SRC-165 | 出血の高リスクの内視鏡では、抗血小板薬2剤併用中もアスピリンは続ける。血栓リスク… |
| XS-019 | 抗血栓薬服用者の内視鏡 | SRC-165 | 出血の高リスクの内視鏡では、DOAC の最終服用を処置の3日前とすることが推奨さ… |
| XS-020 | 抗血栓薬服用者の内視鏡 | SRC-165 | 血栓リスクが高い状態として、機械弁（僧帽弁位、施設によっては大動脈弁位）、心房細… |
| XS-021 | 抗血栓薬服用者の内視鏡 | SRC-165 | 急性消化管出血では、二次予防のアスピリンはルーチンには中止せず、P2Y12 受容… |
| XS-022 | 大腸内視鏡の質の指標 | SRC-167 | ESGE は大腸内視鏡の主要な質の指標と最低基準を、腸管前処置が適切な割合90%… |
| XS-023 | 大腸内視鏡の質の指標 | SRC-167 | ESGE は大腸内視鏡の抜去時間の最低基準を平均6分、目標を平均10分としている… |
| XS-024 | 肝機能検査値の異常と黄疸 | SRC-166 | BSG 2018 は、標準の肝機能検査として、ビリルビン、アルブミン、ALT、A… |
| XS-025 | 肝機能検査値の異常と黄疸 | SRC-166 | 肝機能検査値の異常の臨床的な重要性は、異常の程度ではなく、どの項目が異常かと臨床… |
| XS-026 | 肝機能検査値の異常と黄疸 | SRC-166 | 成人の肝機能異常の標準の原因検索として、腹部超音波検査、HBs 抗原、HCV 抗… |
| XS-027 | 肝機能検査値の異常と黄疸 | SRC-166 | ビリルビンだけが高い場合に最も多い原因は Gilbert 症候群で、溶血がなく主… |
| XS-028 | 肝機能検査値の異常と黄疸 | SRC-166 | ALP が高いときは、γ-GT を測ると肝由来か肝以外（骨など）由来かの見当がつ… |
| XS-029 | 肝機能検査値の異常と黄疸 | SRC-166 | BSG 2018 は、NAFLD の線維化の評価に FIB-4 などを使うことを… |
| XS-030 | 肝機能検査値の異常と黄疸 | SRC-166 | BSG 2018 は、AUDIT スコア19超のアルコール依存はアルコール診療に… |
| XS-031 | 低栄養の診断（GLIM） | SRC-168 | GLIM 基準による低栄養の診断は2段階で、まず妥当性が確かめられたスクリーニン… |
| XS-032 | 低栄養の診断（GLIM） | SRC-168 | GLIM 基準の表現型の基準は、体重減少が6か月以内で5%超か6か月を超えて10… |
| XS-033 | 低栄養の診断（GLIM） | SRC-168 | GLIM 基準の病因の基準のうち摂取量の低下は、必要エネルギーの50%以下が1週… |
| XS-034 | 周術期の栄養管理 | SRC-169 | ESPEN は、6か月以内の体重減少10〜15%超、BMI 18.5未満、SGA… |
| XS-035 | 周術期の栄養管理 | SRC-169 | ESPEN は、多くの患者で前夜からの絶食は不要とし、誤嚥のリスクが特にない患者… |
| XS-036 | 周術期の栄養管理 | SRC-169 | ESPEN は、経腸栄養が必要な手術患者では術後24時間以内に開始し、少量から5… |
| XS-037 | 周術期の栄養管理 | SRC-169 | 高度の低栄養の患者に栄養を急に増やすとリフィーディング症候群を起こすおそれがある… |

## 4. 重複回避と境界の確認

- 上部消化管出血（GBS、制限輸血、内視鏡のタイミング）は UG、大腸憩室出血は IN で扱い済み。XS は下部消化管出血の全体像に限り、関係するカードを corroboration に書きました。
- Gilbert 症候群の病態と、日本の NAFLD/NASH 診療GL での FIB-4 の使い方は LV で扱い済み。XS では検査値の読み方（どの項目が異常か）と英国の紹介基準に限りました。
- セリアック病の診断は IN で扱い済み。

## 5. なお未作成のトピック（欠番補完ラウンドで扱う）

- 日本の消化器内視鏡学会の抗血栓薬服用者の内視鏡ガイドライン（休薬期間が欧州と異なる）と、日本の内視鏡の鎮静ガイドライン
- 悪心・嘔吐、急性下痢、黄疸の鑑別の症候からの体系的な整理（日本の資料）
- 腫瘍マーカーの使い方、画像検査の被ばく量、腸管前処置の方法
- 日本の静脈経腸栄養ガイドライン、リフィーディング症候群の診断基準

## 6. Claude Code での照合時に重点的に確認する点

1. SRC-163〜169 の PMID・PMCID とライセンスを DOI から確定する。SRC-169 は DOI を記入していない（PubMed の検索結果では PMID 34242915）。DOI を API で確定して記入する。
2. SRC-167（UEG Journal）と SRC-169（Clin Nutr）は、ライセンスを確認できず UNKNOWN とした。SRC-168 は Elsevier の論文で RESTRICTED とした（同じ内容の J Cachexia Sarcopenia Muscle 版は別のライセンスの可能性がある）。
3. GLIM のカード（XS-032・033）は、著者最終稿の抽出で不等号が一部欠けていた。刊行版で「以上・未満」を確認する。
4. 二次資料経由と書いたカードは、ガイドラインが引用した原著と照合する。
5. 国試出題基準は、この範囲に該当する番号表がないため全件 `kokushi: null`。必要なら医学総論の症候・検査の項目から付ける。

## 7. 消化器領域の全7回の完了と、欠番補完ラウンドへの引き継ぎ

- これで第1〜7回が揃った。次は欠番補完ラウンドで、各回の「なお未作成のトピック」と、食道の欠番7件（ES-076〜078、082〜084、088）を扱う。
- SRC 番号は SRC-170 から。
