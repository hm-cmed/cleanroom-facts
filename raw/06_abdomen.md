# 第6回 腹膜・腹壁・急性腹症（AB-001〜AB-086）

- 作成日：2026-10-18
- 事実票：86件（AB-001〜AB-086、欠番なし）。全件 `status: draft`、`verifier: null`
- 取り込み時の注意：YAMLブロックは1つだけで、アンカー・マージキー・脚注番号は使っていません。`fact.schema.json` での検証を通過済みです。
- 形式は `docs/tasks/round2_GD_supplement.md` 第1節、番号は `docs/tasks/curriculum_reference.md` に従いました。SRC 番号は SRC-154 から振りました（第5回の引き継ぎメモでは SRC-100 からとなっていますが、特別回 NG で SRC-153 まで使用済み）。
- **利益相反**：急性腹症診療ガイドライン2025（SRC-154）は、本リポジトリの管理者（三原弘）が作成委員として関わり、英語版の筆頭著者でもあります。このガイドラインを出典とするカード（54件）を教育・広報に使う場合は、その旨を表示してください。
- **出典の版**：急性腹症診療ガイドライン2025 は、日本語版（医学書院、2025年3月。Minds 本文公開 2026年9月）を、ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認しました。英語版（4誌同時掲載）は 2026-10-18 時点で公開を確認できなかったため、SRC を付けていません。公開後に同じ内容を英語版で照合し、別の SRC 番号で `corroboration` に記録してください。
- 腸閉塞は、作成中の腸閉塞診療ガイドラインを使わず、急性腹症診療ガイドライン2025 と国際ガイドライン（Bologna ASBO 2017）から作りました（ユーザーの指定）。

## 1. 出典マスター（新規 SRC-154〜161）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 使用カード数 |
|---|---|---|---|---|---|---|
| SRC-154 | 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日） | — | — | © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員 | RESTRICTED | 54 |
| SRC-155 | Di Saverio S, Podda M, De Simone B, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg 2020;15:27 | 10.1186/s13017-020-00306-3 | — | CC BY 4.0 | OPEN | 8 |
| SRC-156 | Ten Broek RPG, Krielen P, Di Saverio S, et al. Bologna guidelines for diagnosis and management of adhesive small bowel obstruction (ASBO): 2017 update. World J Emerg Surg 2018;13:24 | 10.1186/s13017-018-0185-2 | — | CC BY 4.0 | OPEN | 6 |
| SRC-157 | Sartelli M, Chichom-Mefire A, Labricciosa FM, et al. The management of intra-abdominal infections from a global perspective: 2017 WSES guidelines for management of intra-abdominal infections. World J Emerg Surg 2017;12:29 | 10.1186/s13017-017-0141-6 | — | CC BY 4.0 | OPEN | 3 |
| SRC-158 | HerniaSurge Group. International guidelines for groin hernia management. Hernia 2018;22:1-165 | 10.1007/s10029-017-1668-x | — | CC BY-NC 4.0 | RESTRICTED | 6 |
| SRC-159 | Bala M, Catena F, Kashuk J, et al. Acute mesenteric ischemia: updated guidelines of the World Society of Emergency Surgery. World J Emerg Surg 2022;17:54 | 10.1186/s13017-022-00443-x | — | CC BY 4.0 | OPEN | 4 |
| SRC-160 | Kirkpatrick AW, Roberts DJ, De Waele J, et al. Intra-abdominal hypertension and the abdominal compartment syndrome: updated consensus definitions and clinical practice guidelines from the World Society of the Abdominal Compartment Syndrome. Intensive Care Med 2013;39:1190-1206 | 10.1007/s00134-013-2906-z | — | CC BY-NC（Creative Commons Attribution Noncommercial License） | RESTRICTED | 2 |
| SRC-161 | Coccolini F, Montori G, Catena F, et al. Splenic trauma: WSES classification and guidelines for adult and pediatric patients. World J Emerg Surg 2017;12:40 | 10.1186/s13017-017-0151-4 | — | CC BY 4.0 | OPEN | 3 |

- WSES の「合併症を伴う腹壁ヘルニアの緊急修復GL 2017」（DOI 10.1186/s13017-017-0149-y）は、取得先の制限で本文を読めなかったため使っていません。

## 2. 事実票 YAML

```yaml
- id: AB-001
  domain: AB
  subdomain: 急性腹症の定義と分類
  assertion:
    plain_statement_ja: 急性腹症は、発症から1週間以内に始まった急な腹痛か、慢性の腹痛が急に悪化したものを特徴とする疾患群と定義される。緊急手術や速やかな治療を要する腹部の疾患に加え、胸部など腹部以外の疾患も含む。文献によっては発症5日以内とするものもあるが、日本のガイドラインは1週間以内を採っている。
    condition:
      guideline: 急性腹症診療GL2025 BQ1
      evidence_certainty: D
    differential: 慢性腹痛、腸脳相関障害による腹痛
    common_misconception: 急性腹症は手術が必要な腹部の病気だけを指す
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-002
  domain: AB
  subdomain: 急性腹症の定義と分類
  assertion:
    plain_statement_ja: 急性腹症の痛みの病態は、壁側腹膜の炎症（体性痛）、管腔臓器の閉塞（内臓痛）、血管障害（体性痛と内臓痛）、非特異的腹痛（内臓痛と関連痛）の4つに整理できる。前の2つ（腹膜の炎症と血管障害）では緊急手術や血管内治療（IVR）を考え、管腔臓器の閉塞と非特異的腹痛ではドレナージや保存的治療を考える。
    condition:
      guideline: 急性腹症診療GL2025 BQ1 本文
    differential: null
    common_misconception: 痛みの強さだけで緊急手術の要否が決まる
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 4分類はガイドラインが引用した総説による
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-003
  domain: AB
  subdomain: 急性腹症の定義と分類
  assertion:
    plain_statement_ja: 日本のガイドラインは、機械的な閉塞を伴うものを「腸閉塞症」、機械的な閉塞がなく腸の蠕動や運動の欠如によるものを「イレウス」として、明確に区別して定義している。日本では両者を区別せずに使ってきた経緯があり、英語の ileus を「腸閉塞」と訳す誤りがしばしばみられる。
    condition:
      guideline: 急性腹症診療GL2025 BQ2
    differential: 偽性腸閉塞症（機械的閉塞がないのに閉塞症状を繰り返す）
    common_misconception: イレウスと腸閉塞は同じ意味である
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-004
  domain: AB
  subdomain: 急性腹症の定義と分類
  assertion:
    plain_statement_ja: 機械的な閉塞のない偽性腸閉塞症は、分類上はイレウス（機械的閉塞を伴わない）に入るが、閉塞症状を繰り返し、腸切除などの手術が必要になることも多い疾患群である。
    condition:
      guideline: 急性腹症診療GL2025 BQ2
    differential: 機械的腸閉塞
    common_misconception: 手術が必要なのは機械的腸閉塞だけである
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: 慢性特発性偽性腸閉塞症の診断基準は NG 側のカードで扱い済み
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-005
  domain: AB
  subdomain: 急性腹症の定義と分類
  assertion:
    plain_statement_ja: 急性虫垂炎は、組織学的にカタル性、蜂窩織炎性、壊疽性に分けられ、臨床的には単純性、複雑性、汎発性腹膜炎を伴うものに分けられる。ただし、手術前にこれらを正確に分類することは難しい。
    condition:
      guideline: 急性腹症診療GL2025 BQ3
    differential: null
    common_misconception: 画像検査で術前に虫垂炎の病期を正確に判定できる
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-006
  domain: AB
  subdomain: 急性腹症の疫学と予後
  assertion:
    plain_statement_ja: 急性腹症の原因として多いのは、急性虫垂炎、腸閉塞、胆石症、尿管結石、憩室炎である。女性では子宮・卵巣の腫瘍や炎症も多く、年齢や性別によって頻度が異なる。
    condition:
      guideline: 急性腹症診療GL2025 BQ4
      evidence_certainty: B
    differential: null
    common_misconception: 急性腹症の原因は年齢や性別によらずほぼ同じである
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-007
  domain: AB
  subdomain: 急性腹症の疫学と予後
  assertion:
    plain_statement_ja: 日本の DPC データ（2009〜2011年）では、急性腹症で最も多かったのは男女とも腸管感染症（男性11.5%、女性11.0%）だった。男性では急性虫垂炎9.2%、腸閉塞9.1%、腹膜炎6.4%が続き、女性では腸閉塞8.0%、子宮・卵巣の腫瘍7.9%、急性虫垂炎7.2%が続いた。
    condition:
      guideline: 急性腹症診療GL2025 BQ4 本文 表Ⅳ-1
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-264 (id: Jlvnl3k)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-008
  domain: AB
  subdomain: 急性腹症の疫学と予後
  assertion:
    plain_statement_ja: 日本で手術を受けた急性腹症1,456例の年齢別の検討では、7〜17歳の87.7%が急性虫垂炎で、65歳以上では腸閉塞が44.7%で最も多かった。
    condition:
      guideline: 急性腹症診療GL2025 BQ4 本文 表Ⅳ-2
    differential: null
    common_misconception: 高齢者の急性腹症で最も多いのも虫垂炎である
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-264 (id: Jlvnl3k)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-009
  domain: AB
  subdomain: 急性腹症の疫学と予後
  assertion:
    plain_statement_ja: 急性腹痛は救急外来の受診者の5〜10%を占めると報告されている。致死的な症例は0.5%未満、重篤で手術が必要な症例は約20%である。入院が必要になるのは約20〜40%で、入院患者のうち約20〜30%が外科的介入を要する。
    condition:
      guideline: 急性腹症診療GL2025 BQ8・BQ9
      evidence_certainty: B（BQ8）、C（BQ9）
    differential: null
    common_misconception: 救急外来の腹痛の大半は手術が必要である
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-010
  domain: AB
  subdomain: 急性腹症の疫学と予後
  assertion:
    plain_statement_ja: 急性発症の腹痛では、初診時に約7割で診断がつき、約3割は非特異的腹痛（NSAP）と診断される。診断がつかなかった患者の多くは2〜3日以内に痛みが消えるか軽くなるが、一部は後に治療が必要な疾患が見つかる。
    condition:
      guideline: 急性腹症診療GL2025 BQ10・BQ11
      evidence_certainty: C
    differential: null
    common_misconception: 初診で診断がつかない腹痛は心配いらない
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-011
  domain: AB
  subdomain: 急性腹症の疫学と予後
  assertion:
    plain_statement_ja: 急性腹症では、原因が心血管系の病変である場合や、SOFA スコアが高く全身状態が悪い場合に予後が悪く、特に高齢者で悪化しやすい。高齢者は他の年代に比べて死亡率が高く、リハビリなどのための転院も多い。
    condition:
      guideline: 急性腹症診療GL2025 BQ6・BQ7
      evidence_certainty: C
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-012
  domain: AB
  subdomain: 急性腹症の疫学と予後
  assertion:
    plain_statement_ja: 消化管穿孔では、食道穿孔と下部消化管穿孔の死亡率が、胃・十二指腸穿孔より一般に高い。高齢者と、発症から時間がたった患者は予後が悪い。
    condition:
      guideline: 急性腹症診療GL2025 BQ13
    differential: 胃・十二指腸穿孔
    common_misconception: 消化管穿孔の予後は穿孔部位によらない
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-013
  domain: AB
  subdomain: 急性腹症の疫学と予後
  assertion:
    plain_statement_ja: 急性腹症は、症例数の多い施設のほうが少ない施設より診断率や予後がよい傾向がある。総合臨床医（内科・外科）や放射線科医の読影があることも予後によい影響を与える可能性がある。
    condition:
      guideline: 急性腹症診療GL2025 BQ14
      evidence_certainty: C（症例数）、D（読影）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-014
  domain: AB
  subdomain: 急性腹症の疫学と予後
  assertion:
    plain_statement_ja: 腹痛に関連して医療訴訟になりやすい疾患として、腹膜炎（汎発性を含む）、心筋梗塞、腸閉塞（絞扼性を含む）、大動脈解離、急性膵炎が挙げられている。
    condition:
      guideline: 急性腹症診療GL2025 BQ73
      evidence_certainty: C
    differential: null
    common_misconception: 医療訴訟になりやすいのは手術の合併症だけである
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-265 (id: Jlvnl3o)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-015
  domain: AB
  subdomain: 緊急度の判断と緊急処置
  assertion:
    plain_statement_ja: 緊急手術の対象になるのは、一般に、血管の破裂、腹腔内出血、腸管の虚血・壊死、汎発性腹膜炎、炎症性の急性腹症などである。
    condition:
      guideline: 急性腹症診療GL2025 BQ12
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-016
  domain: AB
  subdomain: 緊急度の判断と緊急処置
  assertion:
    plain_statement_ja: 短時間で命にかかわる腹痛として、大動脈瘤破裂や大動脈解離による出血があり、敗血症性ショックを起こす急性腹症も速やかな対応が必要である。ショックを伴う腹部中央の激痛では、急性膵炎、腸間膜動脈閉塞症、腹腔内出血、大動脈瘤破裂、大動脈解離、消化管穿孔や腸管壊死、急性冠症候群、異所性妊娠を鑑別する。
    condition:
      guideline: 急性腹症診療GL2025 BQ15・BQ58
      evidence_certainty: C（BQ58）
    differential: null
    common_misconception: 腹痛でショックがあれば消化管穿孔である
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-017
  domain: AB
  subdomain: 緊急度の判断と緊急処置
  assertion:
    plain_statement_ja: 緊急の内視鏡検査や処置が必要になる腹痛の原因として、消化管出血、急性胆管炎、消化管異物、腸閉塞症がある。緊急の血管造影や血管内治療が必要になる病態には、出血に対する塞栓術（腫瘍破裂、内視鏡で止血できない消化管出血、内臓動脈瘤破裂など）、腸間膜動脈閉塞などに対する血管形成術、腹部大動脈瘤に対するステントグラフト内挿術、急性腸間膜虚血に対する動注療法がある。
    condition:
      guideline: 急性腹症診療GL2025 BQ16・BQ17
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-018
  domain: AB
  subdomain: 緊急度の判断と緊急処置
  assertion:
    plain_statement_ja: 急性腹症を疑ったら、まずバイタルサインを確認し、異常があれば緊急処置を行いながら原因疾患の治療を始める。自施設で根治的な治療ができない場合は、緊急処置をしたうえで転院を考える。バイタルサインに異常がなければ、医療面接と身体所見から緊急手術の必要性を判断し、血液検査と画像検査で出血、臓器の虚血、汎発性腹膜炎、臓器の急性炎症がないかを判断する。
    condition:
      guideline: 急性腹症診療GL2025 BQ75
      evidence_certainty: C
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-019
  domain: AB
  subdomain: 緊急度の判断と緊急処置
  assertion:
    plain_statement_ja: 急性腹症で腹腔内感染症と診断したら、循環動態が安定していても初期輸液をすぐに始める。輸液はまず末梢静脈路から始め、成人の敗血症性ショックでは中心静脈路の確保を待たずに末梢静脈から昇圧薬を始めて平均血圧を回復させることが勧められている（短期間に限り、肘窩かそれより中枢の静脈を使う）。末梢静脈路がとれなければ、小児・成人とも骨髄輸液を考える。
    condition:
      guideline: 急性腹症診療GL2025 BQ76・BQ77
      evidence_certainty: C
    differential: null
    common_misconception: 昇圧薬は中心静脈路を確保してからでなければ始められない
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-020
  domain: AB
  subdomain: 緊急度の判断と緊急処置
  assertion:
    plain_statement_ja: 腹腔内感染が疑われる急性腹症には、できるだけ早く抗菌薬を投与することが提案されている（強い推奨、エビデンスの確実性 C）。敗血症を疑う場合は、抗菌薬の投与前か、できるだけ早い時期に血液培養をとる。
    condition:
      guideline: 急性腹症診療GL2025 CQ13・BQ43
      recommendation: 強い推奨（CQ13）
      evidence_certainty: C
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-021
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 急性腹症の病歴では、腹痛の性状、警告症状（red flag sign）、疾患に特異性の高い病歴を聴く。随伴症状として、悪心・嘔吐、食欲不振、排便習慣の変化、血便・黒色便、発熱と悪寒・戦慄、性器出血を確認する。患者背景は SAMPLE（症状、アレルギー、薬、既往歴・妊娠、最終食事、経過）に沿って聴く。
    condition:
      guideline: 急性腹症診療GL2025 BQ18・BQ19・BQ20
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-022
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 急性腹症の身体診察では、外観とバイタルサインで緊急度と重症度を評価し、腹部は視診、聴診、打診、触診を行う。必要に応じて黄疸・貧血、胸部、腰背部、直腸・泌尿生殖器領域も診る。表情、顔色、呼吸、立ち居振る舞いといった第一印象や、ベッド上の姿勢・歩き方も緊急度の推定や診断の手がかりになる。
    condition:
      guideline: 急性腹症診療GL2025 BQ21・BQ22・BQ23
      evidence_certainty: D
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-023
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 急性腹症では、頻呼吸があると肺炎、心肺不全、菌血症の可能性が高まり（エビデンスの確実性 B）、頻脈、低血圧、発熱は重症度や予後と関連する（C）。
    condition:
      guideline: 急性腹症診療GL2025 BQ24
      evidence_certainty: B・C
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-024
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 腹部の視診では、手術瘢痕、皮膚所見、腹部膨満、腹壁ヘルニア、拍動、腫瘤、呼吸に伴う腹壁の動きを確認する。腹部膨満、腸の蠕動の亢進、手術瘢痕は腸閉塞の可能性を高める。
    condition:
      guideline: 急性腹症診療GL2025 BQ25
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-265 (id: Jlvnl3o)；TBL-02-07-024 (id: JlAKpko)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-025
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 腸蠕動音はよく伝わるので、聴診は1か所で十分とされる。急性腹症での聴診の臨床的意義は限られるため、蠕動音が聞こえないときに聴診部位を増やしたり時間を延ばしたりすることは勧められていない。異常な腸蠕動音は腸閉塞の診断に役立つが、血管雑音の意義ははっきりしない。
    condition:
      guideline: 急性腹症診療GL2025 BQ26・BQ27
    differential: null
    common_misconception: 腸蠕動音の消失を確認するには4か所で数分ずつ聴く必要がある
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-026
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 小腸閉塞の患者50例の報告では、腸蠕動音の亢進が50%、減弱または消失が24%にみられた。
    condition:
      guideline: 急性腹症診療GL2025 BQ27 本文
    differential: null
    common_misconception: 腸閉塞では必ず金属音が聴取される
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-027
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 腹膜刺激徴候は、炎症などが壁側・臓側腹膜に及んで刺激されたときに出る徴候で、直接みる手技に筋性防御、筋強直（板状硬）、反跳痛、打診痛があり、間接的にみる手技に咳嗽試験と踵落とし試験がある。腹膜刺激徴候は腹膜炎の検出に役立ち、打診痛が陽性なら反跳痛をあえて誘発する必要はない。
    condition:
      guideline: 急性腹症診療GL2025 BQ31・BQ32
    differential: null
    common_misconception: 腹膜炎の確認には反跳痛を必ず誘発する
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-028
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 腹膜刺激徴候がなくても、臨床的に腹膜炎や腸間膜虚血が疑われる場合は画像検査を追加する。高齢の腹膜炎患者で筋性防御や板状硬がみられたのは34%にとどまったという報告がある。
    condition:
      guideline: 急性腹症診療GL2025 BQ32・BQ21 本文
    differential: null
    common_misconception: 腹膜刺激徴候がなければ腹膜炎は否定できる
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 34%はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-029
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 急性虫垂炎では、腸腰筋テストと閉鎖筋テストの特異度が高い（エビデンスの確実性 C）。閉鎖孔ヘルニアが疑わしければ、Howship-Romberg 徴候の有無をみる（D）。一方、腹水の診察所見（波動、濁音界の移動など）は急性腹症の診断ではあまり役立たない（D）。
    condition:
      guideline: 急性腹症診療GL2025 BQ30
      evidence_certainty: C・D
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-264 (id: Jlvnl3k)；TBL-01-00-309 (id: Jlvnl78)'
    kokushi: 医学各論 Ⅵ-9-A-④（閉鎖孔ヘルニア、b）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-030
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: Carnett 徴候は、仰臥位で腕を胸の前で組んだ患者に頭を少し持ち上げて腹筋を緊張させ、最も強い圧痛点の痛みが変わらないか強まれば陽性、弱まれば陰性とする診察法である。腹腔内の病変の除外や、腹壁の痛み、心因性の腹痛の診断に役立つ。
    condition:
      guideline: 急性腹症診療GL2025 BQ33
      evidence_certainty: D
    differential: 腹腔内臓器の炎症
    common_misconception: 腹壁を緊張させると腹腔内の病変の圧痛も強まる
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-031
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 急性腹症の診断で直腸診をルーチンに行う意義は限られている。ただし、排便障害、便の性状の確認、肛門疾患、消化管出血、直腸癌、前立腺癌・前立腺炎が疑われる場合は適応がある。女性の内診（双合診）もルーチンには勧められないが、異所性妊娠や骨盤内炎症性疾患を疑うときは子宮頸部の可動痛や付属器の圧痛が参考になる。
    condition:
      guideline: 急性腹症診療GL2025 BQ34・BQ35
      evidence_certainty: C（BQ34）、B（BQ35）
    differential: null
    common_misconception: 急性腹症では全例に直腸診を行うべきである
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-032
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 腹痛の診断がつく前に鎮痛薬（アセトアミノフェンやオピオイド）を使っても、診断率の低下や予後の悪化にはつながらない（エビデンスの確実性 A）。このため、原因にかかわらず診断前から早めに鎮痛薬を使うことが勧められている。
    condition:
      guideline: 急性腹症診療GL2025 BQ64・BQ78
      evidence_certainty: A（BQ64）、C（BQ78）
    differential: null
    common_misconception: 鎮痛薬を使うと所見が隠れて診断を誤るので、診断がつくまで使わない
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-033
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 急性腹症の鎮痛では、痛みの強さにかかわらずアセトアミノフェンの静脈投与が勧められ、痛みが強ければオピオイドの静脈投与を加える。ブチルスコポラミンなどの鎮痙薬は第1選択ではなく、疝痛に対する補助として使う。NSAIDs は胆道疾患の疝痛にオピオイドと同等の効果があり、尿管結石の疝痛には NSAIDs を使い、使えない場合にオピオイドを使う。
    condition:
      guideline: 急性腹症診療GL2025 BQ78
      evidence_certainty: C
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: アセトアミノフェンの用量（1回1,000 mg、50 kg 未満は15 mg/kg）と日本の保険適応量はガイドラインの注に記載がある
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-034
  domain: AB
  subdomain: 急性腹症の医療面接と身体診察
  assertion:
    plain_statement_ja: 血液検査や画像検査は偽陰性になることがあるため、急性腹症は病歴と身体所見を含めて総合的に判断する。
    condition:
      guideline: 急性腹症診療GL2025 BQ36・BQ37
    differential: null
    common_misconception: 血液検査と CT が正常なら急性腹症は否定できる
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-035
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: プロカルシトニンは、敗血症の診断と重症度の判定、急性膵炎の重症度の判定、複雑性虫垂炎と絞扼性腸閉塞の診断に役立つとされる（弱い推奨、エビデンスの確実性 C）。乳酸値はショックなど重症化の判断に役立つが、血液ガス分析だけで腸管虚血を診断するのは難しく、腸管虚血を疑えば造影 CT を行う（弱い推奨、B）。
    condition:
      guideline: 急性腹症診療GL2025 CQ2・CQ3
      recommendation: 弱い推奨
      evidence_certainty: C・B
    differential: null
    common_misconception: 乳酸値が正常なら腸管虚血は否定できる
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-265 (id: Jlvnl3o)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-036
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: 複雑性虫垂炎の診断には、プロカルシトニン、CRP、好中球/リンパ球比（NLR）が役立つ（弱い推奨、エビデンスの確実性 C）。ただし虫垂炎の約20%は白血球数や CRP が正常で、約10%は両方とも正常である。
    condition:
      guideline: 急性腹症診療GL2025 CQ4
      recommendation: 弱い推奨
      evidence_certainty: C
    differential: null
    common_misconception: 白血球数と CRP が正常なら虫垂炎は否定できる
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-037
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: 急性腹症の鑑別では、急性膵炎の診断にはリパーゼの測定が役立つが、それ以外の疾患ではリパーゼやアミラーゼの測定の有用性は小さい（弱い推奨、エビデンスの確実性 B）。
    condition:
      guideline: 急性腹症診療GL2025 CQ5
      recommendation: 弱い推奨
      evidence_certainty: B
    differential: 急性膵炎の診断基準は BP 側のカードで扱い済み
    common_misconception: 急性腹症ではアミラーゼを測れば多くの疾患を鑑別できる
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-038
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: 心窩部痛があり虚血性心疾患の危険因子がある患者では、心筋梗塞を考えて心電図をとる。腸間膜、脾臓、腎臓の虚血や梗塞を疑うときは心房細動の有無を確認し、急性腹症で心房細動があれば腸間膜虚血、脾梗塞、腎梗塞を考える。
    condition:
      guideline: 急性腹症診療GL2025 BQ38・BQ39
    differential: null
    common_misconception: 腹痛の患者に心電図は不要である
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-039
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: 妊娠しうる年齢の女性で妊娠を否定できない場合は、急性腹症の評価に妊娠反応検査が役立つ。尿の定性検査は尿管結石、尿路感染症、糖尿病性ケトアシドーシスの診断に役立ち、尿中ポルホビリノゲンは急性ポルフィリン症の診断に役立つ。
    condition:
      guideline: 急性腹症診療GL2025 BQ40・BQ41
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-040
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: 急性腹症の画像検査で最初に行うのは超音波検査で、非侵襲的で簡便で普及しているため、特に妊婦と小児に勧められる。一定の訓練を受けた臨床医がベッドサイドで行う超音波検査（POCUS）は診断のために行うことが提案されているが（弱い推奨、エビデンスの確実性 C）、予後を改善するという報告はない。
    condition:
      guideline: 急性腹症診療GL2025 BQ44・CQ7
      recommendation: 弱い推奨（CQ7）
      evidence_certainty: C
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-041
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: POCUS の診断精度は、部位ごとに50例程度の経験で超音波検査の専門家と同等になると報告されており、急性腹症を診る医師は50例程度の超音波の訓練を行うことが提案されている（弱い推奨、エビデンスの確実性 C）。
    condition:
      guideline: 急性腹症診療GL2025 CQ14
      recommendation: 弱い推奨
      evidence_certainty: C
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-042
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: 腹部単純 X 線検査の診断能は限られ、急性腹症のルーチン検査として行う意義は乏しい。超音波検査や CT ができない環境で、腸閉塞、イレウス、消化管穿孔、尿路結石、気腫性病変、異物などを疑う場合には行う。
    condition:
      guideline: 急性腹症診療GL2025 BQ45
    differential: null
    common_misconception: 急性腹症ではまず腹部単純 X 線を撮る
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-029 (id: JlAKplA)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-043
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: 急性腹症の多くは単純 CT で診断できる。臓器虚血、血管性病変、急性膵炎の重症度判定、急性胆管炎・胆嚢炎、複雑性虫垂炎などでは単純 CT だけでは評価が難しく、造影 CT が勧められる（強い推奨、エビデンスの確実性 B）。絞扼性腸閉塞による腸管壁内の血腫や、血栓閉塞型の大動脈解離・切迫破裂の大動脈瘤の評価には、単純 CT も併せて撮るのが望ましい。
    condition:
      guideline: 急性腹症診療GL2025 BQ46・CQ8
      recommendation: 強い推奨（CQ8）
      evidence_certainty: B
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-029 (id: JlAKplA)；TBL-01-00-265 (id: Jlvnl3o)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-044
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: eGFR が30 mL/min/1.73 m²未満の患者に急性腹症でヨード造影剤を使う場合は、造影剤腎症の予防に生理食塩水か重曹液を投与し、造影剤を減量することが提案されている（弱い推奨、エビデンスの確実性 B）。eGFR が30〜60の患者では、ビグアナイド系糖尿病薬を検査後48時間休薬することが提案されている（弱い推奨、B）。
    condition:
      guideline: 急性腹症診療GL2025 CQ9・CQ10
      recommendation: 弱い推奨
      evidence_certainty: B
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-045
  domain: AB
  subdomain: 急性腹症の検査
  assertion:
    plain_statement_ja: MRI は、超音波検査で確定診断がつかない妊婦の急性腹症や、超音波検査や CT で確定できない総胆管結石・虫垂炎の疑いで行うことが提案されている（弱い推奨、エビデンスの確実性 C）。妊娠中の放射線被ばくは50〜100 mGy 以下なら胎児の奇形や中枢神経障害のリスクを上げないが、胎児と小児は発がんリスクが高いため、CT は代替検査より有益な場合に限る。
    condition:
      guideline: 急性腹症診療GL2025 CQ12・FRQ3
      recommendation: 弱い推奨（CQ12）
      evidence_certainty: C
    differential: null
    common_misconception: 妊婦には CT を一切撮ってはいけない
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-046
  domain: AB
  subdomain: 急性腹症の鑑別診断
  assertion:
    plain_statement_ja: 腹痛の部位別にみると、右上腹部痛では食道・胃・十二指腸疾患と肝胆道系疾患が、心窩部痛では食道・胃・十二指腸・胆道系疾患が多い。右下腹部、臍下部、左下腹部の痛みでは腸疾患、尿路疾患、産婦人科疾患が多い。腹部全体の痛みでは血管疾患、消化器疾患、内分泌代謝疾患が多く、背部痛を伴うときは後腹膜の病変に注意する。
    condition:
      guideline: 急性腹症診療GL2025 BQ49〜BQ57
      evidence_certainty: C
    differential: null
    common_misconception: 右下腹部痛はほぼ虫垂炎である
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-047
  domain: AB
  subdomain: 急性腹症の鑑別診断
  assertion:
    plain_statement_ja: 急性腹症と紛らわしい病態には、腹腔外の臓器や全身疾患によるものがあり、特に胸腔内臓器、腹壁、骨盤内臓器が関わることがある。
    condition:
      guideline: 急性腹症診療GL2025 BQ48
      evidence_certainty: C
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-048
  domain: AB
  subdomain: 急性腹症の鑑別診断
  assertion:
    plain_statement_ja: 高齢者の急性腹症では、身体所見や血液検査が病状を正確に反映しないことが多く、手術適応や転帰の判断が難しい。死亡率は年齢とともに高まり、急性腸管虚血、腹部大動脈瘤破裂、腹腔外臓器の不全で特に高い。高齢者の腹痛は緊急入院や外科的処置につながることが多く、CT が診断と治療方針の決定に役立つ。
    condition:
      guideline: 急性腹症診療GL2025 BQ61
      evidence_certainty: C
    differential: null
    common_misconception: 高齢者は所見が軽ければ重症ではない
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-049
  domain: AB
  subdomain: 急性腹症の鑑別診断
  assertion:
    plain_statement_ja: 免疫不全の患者では重症の腹膜炎でも発熱が乏しい傾向があり、軽い身体所見を重視し、血液検査と画像検査で慎重に評価する。麻痺や感覚障害のある患者では痛みが隠れて診断が遅れ、死亡率が上がるおそれがある。認知症などで意思疎通が難しい患者も軽症と判断されやすいため、軽い所見も見逃さず CT を含む画像検査を行う。
    condition:
      guideline: 急性腹症診療GL2025 BQ62・BQ63・BQ66
      evidence_certainty: C・D
    differential: null
    common_misconception: 発熱がなければ腹膜炎は考えにくい
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-050
  domain: AB
  subdomain: 急性腹症の鑑別診断
  assertion:
    plain_statement_ja: 手術歴のある患者の急性腹症では、癒着性腸閉塞、胆嚢炎、胆道再建後の胆管炎、輸入脚症候群に注意する。透析患者では、腹膜炎、消化管穿孔、腸管虚血、筋層内・腹腔内の出血を鑑別する。
    condition:
      guideline: 急性腹症診療GL2025 BQ65・BQ74
      evidence_certainty: C（BQ74）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-051
  domain: AB
  subdomain: 急性腹症の鑑別診断
  assertion:
    plain_statement_ja: 妊婦の急性腹症では、異所性妊娠（内外同時妊娠を含む）、流早産、陣痛、常位胎盤早期剝離、子宮破裂、絨毛膜羊膜炎、HELLP 症候群などの妊娠関連疾患は緊急性が高い。妊娠と関係しない虫垂炎、胆嚢炎、腸閉塞、急性膵炎、尿路結石、卵巣茎捻転なども考える。
    condition:
      guideline: 急性腹症診療GL2025 BQ60
      evidence_certainty: C
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-052
  domain: AB
  subdomain: 急性腹症の鑑別診断
  assertion:
    plain_statement_ja: 異所性妊娠は、無月経（最終月経から6週間以上）、性器出血または下腹部痛があり、妊娠反応が陽性のときに疑う。超音波検査では、子宮内に胎嚢がないこと、子宮外に胎嚢様の構造や液体貯留があることが特徴である。
    condition:
      guideline: 急性腹症診療GL2025 BQ69
      evidence_certainty: A
    differential: null
    common_misconception: 妊娠反応が陽性で腹痛があれば正常妊娠の症状である
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-053
  domain: AB
  subdomain: 急性腹症の鑑別診断
  assertion:
    plain_statement_ja: 学童期の腹痛の原因で最も多いのは急性胃腸炎で、緊急手術が必要なものでは急性虫垂炎が多い。IgA 血管炎も頻度が高い。まれだが致死的な疾患として、急性心筋炎、糖尿病性ケトアシドーシス、溶血性尿毒症症候群がある。
    condition:
      guideline: 急性腹症診療GL2025 BQ59
      evidence_certainty: C・D
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-054
  domain: AB
  subdomain: 急性腹症の鑑別診断
  assertion:
    plain_statement_ja: 急性発症の腹痛で、血尿、腰部・腎部の圧痛、痛みの持続が12時間以下、食欲が保たれていること、男性であることは尿管結石を示唆する。診断には、STONE スコアや CHOKAI スコアといった予測モデルの利用が提案されている（弱い推奨、エビデンスの確実性 C）。
    condition:
      guideline: 急性腹症診療GL2025 BQ71・CQ6
      recommendation: 弱い推奨（CQ6）
      evidence_certainty: C
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-154
    source: 急性腹症診療ガイドライン2025改訂出版委員会編『急性腹症診療ガイドライン2025 第2版』医学書院、2025年3月（Minds 本文公開 2026年9月1日）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00901/
    source_license: © 医学書院・作成学会（非CC。Minds 掲載は個人利用の範囲）。ユーザー提供の刊行版PDF（第Ⅰ〜Ⅹ章）で確認。利益相反：本リポジトリの管理者（三原弘）は本ガイドラインの作成委員
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-055
  domain: AB
  subdomain: 急性虫垂炎
  assertion:
    plain_statement_ja: 急性虫垂炎の生涯リスクは米国で9%、欧州で8%、アフリカで2%と報告されている。
    condition:
      guideline: WSES Jerusalem GL 2020
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-155
    source: 'Di Saverio S, Podda M, De Simone B, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg 2020;15:27'
    doi: 10.1186/s13017-020-00306-3
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-020-00306-3
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 数値はWSES ガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-056
  domain: AB
  subdomain: 急性虫垂炎
  assertion:
    plain_statement_ja: WSES 2020 は、成人の急性虫垂炎の予測に AIR スコアと AAS スコアを使うことを推奨し、Alvarado スコアは虫垂炎の確定には使わないよう提案している。Alvarado スコア5点未満は感度99%で除外に使える。小児では臨床スコアだけで診断しないよう提案している。
    condition:
      guideline: WSES Jerusalem GL 2020
    differential: null
    common_misconception: Alvarado スコアが高ければ虫垂炎と確定できる
  provenance:
    source_ref: SRC-155
    source: 'Di Saverio S, Podda M, De Simone B, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg 2020;15:27'
    doi: 10.1186/s13017-020-00306-3
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-020-00306-3
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-057
  domain: AB
  subdomain: 急性虫垂炎
  assertion:
    plain_statement_ja: WSES 2020 は、成人・小児とも最初の画像検査としてベッドサイドの超音波検査（POCUS）を推奨し、CT を撮る場合は標準線量より低線量の造影 CT を推奨している。小児では CT を最初の画像検査としてルーチンに使わないよう提案している。
    condition:
      guideline: WSES Jerusalem GL 2020
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-155
    source: 'Di Saverio S, Podda M, De Simone B, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg 2020;15:27'
    doi: 10.1186/s13017-020-00306-3
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-020-00306-3
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: 急性腹症診療GL2025 BQ44（超音波を最初に行う）と一致
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-264 (id: Jlvnl3k)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-058
  domain: AB
  subdomain: 急性虫垂炎
  assertion:
    plain_statement_ja: 妊婦で虫垂炎を疑う場合、WSES 2020 は最初に段階的圧迫法の経腹超音波検査を行い、診断がつかなければ MRI を行うことを提案している。妊娠中の虫垂炎は抗菌薬による非手術的治療を行わず、手術は腹腔鏡下で行うことを提案している。
    condition:
      guideline: WSES Jerusalem GL 2020
    differential: null
    common_misconception: 妊娠中の虫垂炎はまず抗菌薬で治療する
  provenance:
    source_ref: SRC-155
    source: 'Di Saverio S, Podda M, De Simone B, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg 2020;15:27'
    doi: 10.1186/s13017-020-00306-3
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-020-00306-3
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: 急性腹症診療GL2025 CQ12（妊婦の MRI）と一致
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-059
  domain: AB
  subdomain: 急性虫垂炎
  assertion:
    plain_statement_ja: WSES 2020 は、糞石のない単純性虫垂炎の一部の患者には、抗菌薬による非手術的治療を手術に代わる選択肢として話し合うことを推奨している。ただし1年以内の再発は27.4%、APPAC 試験の5年追跡では遅発性の再発の可能性が39.1%と報告され、糞石は治療失敗の独立した危険因子である。
    condition:
      guideline: WSES Jerusalem GL 2020
    differential: null
    common_misconception: 抗菌薬で治った虫垂炎は再発しない
  provenance:
    source_ref: SRC-155
    source: 'Di Saverio S, Podda M, De Simone B, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg 2020;15:27'
    doi: 10.1186/s13017-020-00306-3
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-020-00306-3
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 再発率はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-060
  domain: AB
  subdomain: 急性虫垂炎
  assertion:
    plain_statement_ja: WSES 2020 は、手術が必要な虫垂炎では24時間以内の次の手術枠で腹腔鏡下虫垂切除術を予定し、24時間を超えて遅らせないことを推奨している。小児の複雑性虫垂炎では8時間以内の早期手術を勧めている。術式は、設備と技術があれば開腹より腹腔鏡下を推奨している。
    condition:
      guideline: WSES Jerusalem GL 2020
    differential: null
    common_misconception: 虫垂炎は診断したら夜間でも直ちに手術しなければならない
  provenance:
    source_ref: SRC-155
    source: 'Di Saverio S, Podda M, De Simone B, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg 2020;15:27'
    doi: 10.1186/s13017-020-00306-3
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-020-00306-3
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-061
  domain: AB
  subdomain: 急性虫垂炎
  assertion:
    plain_statement_ja: WSES 2020 は、急性虫垂炎の手術前に広域抗菌薬を1回投与し、単純性虫垂炎では術後の抗菌薬を投与しないことを推奨している。複雑性虫垂炎でも感染源の制御が十分なら、術後の抗菌薬を3〜5日より延ばさないことを推奨している。
    condition:
      guideline: WSES Jerusalem GL 2020
    differential: null
    common_misconception: 虫垂切除後は全例に抗菌薬を数日続ける
  provenance:
    source_ref: SRC-155
    source: 'Di Saverio S, Podda M, De Simone B, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg 2020;15:27'
    doi: 10.1186/s13017-020-00306-3
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-020-00306-3
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-062
  domain: AB
  subdomain: 急性虫垂炎
  assertion:
    plain_statement_ja: WSES 2020 は、膿瘍を伴う虫垂炎では、腹腔鏡の技術がない施設では抗菌薬と（可能なら）経皮的ドレナージによる非手術的治療を提案している。40歳未満と小児では非手術的治療のあとにルーチンの待機的虫垂切除術を行わないことを推奨し、40歳以上では大腸内視鏡と造影 CT で腫瘍を確認することを提案している。
    condition:
      guideline: WSES Jerusalem GL 2020
    differential: null
    common_misconception: 膿瘍形成性虫垂炎は治癒後に全例で待機的虫垂切除術を行う
  provenance:
    source_ref: SRC-155
    source: 'Di Saverio S, Podda M, De Simone B, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg 2020;15:27'
    doi: 10.1186/s13017-020-00306-3
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-020-00306-3
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-264 (id: Jlvnl3k)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-063
  domain: AB
  subdomain: 癒着性小腸閉塞
  assertion:
    plain_statement_ja: 小腸閉塞の原因で最も多いのは術後の癒着で、約60%を占める。大腸切除後には10人に1人が3年以内に少なくとも1回の小腸閉塞を起こす。
    condition:
      guideline: Bologna ASBO GL 2017 update（WSES）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-156
    source: 'Ten Broek RPG, Krielen P, Di Saverio S, et al. Bologna guidelines for diagnosis and management of adhesive small bowel obstruction (ASBO): 2017 update. World J Emerg Surg 2018;13:24'
    doi: 10.1186/s13017-018-0185-2
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-018-0185-2
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: 急性腹症診療GL2025 BQ65（手術歴のある患者では癒着性腸閉塞に注意）
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-064
  domain: AB
  subdomain: 癒着性小腸閉塞
  assertion:
    plain_statement_ja: 癒着性小腸閉塞では、CT は絞扼と緊急手術の必要性を約90%の精度で予測する。閉鎖ループ、腸管虚血の所見、腹水は、手術を遅らせるべきでないことを示す。
    condition:
      guideline: Bologna ASBO GL 2017 update（WSES）
    differential: null
    common_misconception: 腸閉塞の手術適応は腹部単純 X 線で判断する
  provenance:
    source_ref: SRC-156
    source: 'Ten Broek RPG, Krielen P, Di Saverio S, et al. Bologna guidelines for diagnosis and management of adhesive small bowel obstruction (ASBO): 2017 update. World J Emerg Surg 2018;13:24'
    doi: 10.1186/s13017-018-0185-2
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-018-0185-2
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: 急性腹症診療GL2025 CQ8（造影 CT の追加）
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-265 (id: Jlvnl3o)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-065
  domain: AB
  subdomain: 癒着性小腸閉塞
  assertion:
    plain_statement_ja: 腹膜炎、絞扼、腸管虚血の徴候がない癒着性小腸閉塞は、絶飲食と経鼻胃管または長いイレウス管による減圧で、まず非手術的治療を行う。成功率は約70〜90%で、改善しない場合に手術に移るまでの期間は72時間が安全で適切とされている。
    condition:
      guideline: Bologna ASBO GL 2017 update（WSES）
    differential: null
    common_misconception: 癒着性腸閉塞は改善するまで何日でも保存的治療を続けてよい
  provenance:
    source_ref: SRC-156
    source: 'Ten Broek RPG, Krielen P, Di Saverio S, et al. Bologna guidelines for diagnosis and management of adhesive small bowel obstruction (ASBO): 2017 update. World J Emerg Surg 2018;13:24'
    doi: 10.1186/s13017-018-0185-2
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-018-0185-2
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-066
  domain: AB
  subdomain: 癒着性小腸閉塞
  assertion:
    plain_statement_ja: 癒着性小腸閉塞では水溶性造影剤を投与し、24時間後の腹部 X 線で造影剤が大腸に達していなければ、非手術的治療の失敗を強く示唆する。水溶性造影剤の検査は手術の必要性を予測し、入院期間を短くし、手術の必要性を減らすとする報告もある。
    condition:
      guideline: Bologna ASBO GL 2017 update（WSES）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-156
    source: 'Ten Broek RPG, Krielen P, Di Saverio S, et al. Bologna guidelines for diagnosis and management of adhesive small bowel obstruction (ASBO): 2017 update. World J Emerg Surg 2018;13:24'
    doi: 10.1186/s13017-018-0185-2
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-018-0185-2
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 造影剤の量は本文に記載がない
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-265 (id: Jlvnl3o)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-067
  domain: AB
  subdomain: 癒着性小腸閉塞
  assertion:
    plain_statement_ja: 癒着性小腸閉塞の再発は、非手術的治療後で1年12%・5年20%、手術後で1年8%・5年16%と報告されている。ヒアルロン酸・カルボキシメチルセルロースの癒着防止材は、癒着の形成と、癒着性小腸閉塞による再手術を減らす（大腸手術での再手術の相対リスク0.49）。
    condition:
      guideline: Bologna ASBO GL 2017 update（WSES）
    differential: null
    common_misconception: 癒着性腸閉塞は一度治れば再発しにくい
  provenance:
    source_ref: SRC-156
    source: 'Ten Broek RPG, Krielen P, Di Saverio S, et al. Bologna guidelines for diagnosis and management of adhesive small bowel obstruction (ASBO): 2017 update. World J Emerg Surg 2018;13:24'
    doi: 10.1186/s13017-018-0185-2
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-018-0185-2
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-068
  domain: AB
  subdomain: 癒着性小腸閉塞
  assertion:
    plain_statement_ja: 癒着性小腸閉塞の手術では、選ばれた症例で腹腔鏡下の癒着剝離術が合併症を減らす可能性がある。ただし腸管損傷が6.3〜26.9%に起きたとする報告がある。
    condition:
      guideline: Bologna ASBO GL 2017 update（WSES）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-156
    source: 'Ten Broek RPG, Krielen P, Di Saverio S, et al. Bologna guidelines for diagnosis and management of adhesive small bowel obstruction (ASBO): 2017 update. World J Emerg Surg 2018;13:24'
    doi: 10.1186/s13017-018-0185-2
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-018-0185-2
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 腸管損傷の頻度はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-265 (id: Jlvnl3o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-069
  domain: AB
  subdomain: 鼠径部ヘルニア
  assertion:
    plain_statement_ja: 鼠径部ヘルニアの生涯の発生率は、男性で27〜43%、女性で3〜6%と報告されている。
    condition:
      guideline: HerniaSurge 国際GL 2018
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-158
    source: HerniaSurge Group. International guidelines for groin hernia management. Hernia 2018;22:1-165
    doi: 10.1007/s10029-017-1668-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s10029-017-1668-x
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はHerniaSurge ガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-309 (id: Jlvnl78)；TBL-01-00-310 (id: Jlvnl8E)'
    kokushi: 医学各論 Ⅵ-9-A-②（鼠径ヘルニア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-070
  domain: AB
  subdomain: 鼠径部ヘルニア
  assertion:
    plain_statement_ja: 鼠径部ヘルニアの多くは身体診察で診断でき、超音波検査が必要になることはまれである。再発ヘルニアが疑われる場合は、診察に超音波検査を組み合わせることが勧められている。
    condition:
      guideline: HerniaSurge 国際GL 2018
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-158
    source: HerniaSurge Group. International guidelines for groin hernia management. Hernia 2018;22:1-165
    doi: 10.1007/s10029-017-1668-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s10029-017-1668-x
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-309 (id: Jlvnl78)；TBL-01-00-310 (id: Jlvnl8E)'
    kokushi: 医学各論 Ⅵ-9-A-②（鼠径ヘルニア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-071
  domain: AB
  subdomain: 鼠径部ヘルニア
  assertion:
    plain_statement_ja: 症状がないか軽い男性の鼠径ヘルニアは、経過観察（watchful waiting）で管理してよい。ただし経過観察した患者の多くは最終的に手術を受け、5年で54%、10年で推定68%が手術に移行したと報告されている。
    condition:
      guideline: HerniaSurge 国際GL 2018
    differential: null
    common_misconception: 鼠径ヘルニアは見つけたら全例すぐに手術が必要である
  provenance:
    source_ref: SRC-158
    source: HerniaSurge Group. International guidelines for groin hernia management. Hernia 2018;22:1-165
    doi: 10.1007/s10029-017-1668-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s10029-017-1668-x
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 移行率はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-309 (id: Jlvnl78)；TBL-01-00-310 (id: Jlvnl8E)'
    kokushi: 医学各論 Ⅵ-9-A-②（鼠径ヘルニア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-072
  domain: AB
  subdomain: 鼠径部ヘルニア
  assertion:
    plain_statement_ja: 鼠径ヘルニアの修復はメッシュを使う方法が第1選択で、開腹（Lichtenstein 法など）でも腹腔鏡・内視鏡下でもよい。腹腔鏡・内視鏡下の修復は、資源と技術があれば回復が早く、慢性疼痛が少なく、費用対効果もよい。
    condition:
      guideline: HerniaSurge 国際GL 2018
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-158
    source: HerniaSurge Group. International guidelines for groin hernia management. Hernia 2018;22:1-165
    doi: 10.1007/s10029-017-1668-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s10029-017-1668-x
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-309 (id: Jlvnl78)；TBL-01-00-310 (id: Jlvnl8E)'
    kokushi: 医学各論 Ⅵ-9-A-②（鼠径ヘルニア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-073
  domain: AB
  subdomain: 鼠径部ヘルニア
  assertion:
    plain_statement_ja: 嵌頓・絞扼の危険因子には、女性、大腿ヘルニア、鼠径部ヘルニアによる入院歴がある。大腿ヘルニアは、技術があれば腹腔鏡・内視鏡下のメッシュ修復を時機を逃さず行うことが提案されている。
    condition:
      guideline: HerniaSurge 国際GL 2018
    differential: null
    common_misconception: 大腿ヘルニアも症状がなければ経過観察でよい
  provenance:
    source_ref: SRC-158
    source: HerniaSurge Group. International guidelines for groin hernia management. Hernia 2018;22:1-165
    doi: 10.1007/s10029-017-1668-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s10029-017-1668-x
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-309 (id: Jlvnl78)；TBL-01-00-310 (id: Jlvnl8E)'
    kokushi: 医学各論 Ⅵ-9-A-③（大腿ヘルニア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-074
  domain: AB
  subdomain: 鼠径部ヘルニア
  assertion:
    plain_statement_ja: 鼠径部ヘルニアの緊急手術は待機手術より合併症と死亡が多い。プールした解析では、待機手術の合併症は約8%・死亡0.2〜0.5%、緊急手術では合併症約32%・死亡4〜5.5%と報告されている。
    condition:
      guideline: HerniaSurge 国際GL 2018
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-158
    source: HerniaSurge Group. International guidelines for groin hernia management. Hernia 2018;22:1-165
    doi: 10.1007/s10029-017-1668-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s10029-017-1668-x
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-309 (id: Jlvnl78)；TBL-01-00-310 (id: Jlvnl8E)'
    kokushi: 医学各論 Ⅵ-9-A-②（鼠径ヘルニア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-075
  domain: AB
  subdomain: 腹膜炎・腹腔内感染症
  assertion:
    plain_statement_ja: 腹腔内感染症は、感染が1つの臓器にとどまり腹膜に及んでいない「単純性」と、臓器を越えて限局性または汎発性の腹膜炎を起こした「複雑性」に分けられる。
    condition:
      guideline: WSES 腹腔内感染症 GL 2017
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-157
    source: 'Sartelli M, Chichom-Mefire A, Labricciosa FM, et al. The management of intra-abdominal infections from a global perspective: 2017 WSES guidelines for management of intra-abdominal infections. World J Emerg Surg 2017;12:29'
    doi: 10.1186/s13017-017-0141-6
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-017-0141-6
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-076
  domain: AB
  subdomain: 腹膜炎・腹腔内感染症
  assertion:
    plain_statement_ja: 腹膜炎は、消化管の連続性が保たれたまま起こる一次性（特発性細菌性腹膜炎など）、最も多い二次性（消化管穿孔などによる）、一次性または二次性の腹膜炎のあとに再燃する三次性に分けられる。
    condition:
      guideline: WSES 腹腔内感染症 GL 2017
    differential: 特発性細菌性腹膜炎の診断は LV 側のカードで扱い済み
    common_misconception: 腹膜炎の多くは特発性細菌性腹膜炎である
  provenance:
    source_ref: SRC-157
    source: 'Sartelli M, Chichom-Mefire A, Labricciosa FM, et al. The management of intra-abdominal infections from a global perspective: 2017 WSES guidelines for management of intra-abdominal infections. World J Emerg Surg 2017;12:29'
    doi: 10.1186/s13017-017-0141-6
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-017-0141-6
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-077
  domain: AB
  subdomain: 腹膜炎・腹腔内感染症
  assertion:
    plain_statement_ja: 腹腔内感染症の治療では、感染源の制御を可能な限り早く完全に行うことが重要で、手術などの処置が遅れたり不十分だったりすると転帰が大きく悪化する。適切な抗菌薬を早く始めることも治療の柱の1つである。世界の多施設研究（WISS）では、腹腔内感染症の全体の死亡率は9.2%だった。
    condition:
      guideline: WSES 腹腔内感染症 GL 2017
    differential: null
    common_misconception: 腹膜炎は抗菌薬だけで治せる
  provenance:
    source_ref: SRC-157
    source: 'Sartelli M, Chichom-Mefire A, Labricciosa FM, et al. The management of intra-abdominal infections from a global perspective: 2017 WSES guidelines for management of intra-abdominal infections. World J Emerg Surg 2017;12:29'
    doi: 10.1186/s13017-017-0141-6
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-017-0141-6
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: 急性腹症診療GL2025 CQ13（抗菌薬をできるだけ早く）
  uncertainty: 死亡率はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-308 (id: Jlvnl70)'
    kokushi: 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-078
  domain: AB
  subdomain: 急性腸間膜虚血
  assertion:
    plain_statement_ja: 急性腸間膜虚血は、緊急外科入院の0.09〜0.2%とまれだが、年齢とともに増え、死亡率は50%を超える。原因は、上腸間膜動脈の塞栓症が約50%、血栓症が15〜25%、静脈血栓症が5〜15%で、非閉塞性腸間膜虚血（NOMI）は約20%を占める。
    condition:
      guideline: WSES 急性腸間膜虚血 GL 2022
    differential: null
    common_misconception: 腸間膜虚血は血管が詰まった場合にしか起こらない
  provenance:
    source_ref: SRC-159
    source: 'Bala M, Catena F, Kashuk J, et al. Acute mesenteric ischemia: updated guidelines of the World Society of Emergency Surgery. World J Emerg Surg 2022;17:54'
    doi: 10.1186/s13017-022-00443-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-022-00443-x
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: NOMI の割合は本文で約20%と25%の2通りに書かれている。数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-079
  domain: AB
  subdomain: 急性腸間膜虚血
  assertion:
    plain_statement_ja: 身体所見に比べて不釣り合いに強い腹痛は、否定されるまで急性腸間膜虚血として扱うことが強く推奨されている。乳酸値2 mmol/L 超は不可逆的な腸管虚血と関連するが、単独で診断できるほど正確なバイオマーカーはない。
    condition:
      guideline: WSES 急性腸間膜虚血 GL 2022
    differential: null
    common_misconception: 乳酸値が正常なら腸間膜虚血は否定できる
  provenance:
    source_ref: SRC-159
    source: 'Bala M, Catena F, Kashuk J, et al. Acute mesenteric ischemia: updated guidelines of the World Society of Emergency Surgery. World J Emerg Surg 2022;17:54'
    doi: 10.1186/s13017-022-00443-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-022-00443-x
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: 急性腹症診療GL2025 CQ3（血液ガスだけでは腸管虚血を診断できない）と一致
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-080
  domain: AB
  subdomain: 急性腸間膜虚血
  assertion:
    plain_statement_ja: 急性腸間膜虚血を疑ったら、遅滞なく CT 血管造影を行うことが強く推奨されている。診断（CT 血管造影）が6時間遅れるごとに死亡率が2倍になると述べられている。
    condition:
      guideline: WSES 急性腸間膜虚血 GL 2022
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-159
    source: 'Bala M, Catena F, Kashuk J, et al. Acute mesenteric ischemia: updated guidelines of the World Society of Emergency Surgery. World J Emerg Surg 2022;17:54'
    doi: 10.1186/s13017-022-00443-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-022-00443-x
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 死亡率の倍増はガイドラインの記述による
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-081
  domain: AB
  subdomain: 急性腸間膜虚血
  assertion:
    plain_statement_ja: 急性腸間膜虚血の治療では、動脈閉塞には技術があれば血管内治療による血行再建を第1選択とし、壊死した腸はすぐに切除する。再開腹（セカンドルック）は多くの場合24〜48時間以内に行う。腸間膜静脈血栓症は未分画ヘパリンの持続投与で治療できることが多い。
    condition:
      guideline: WSES 急性腸間膜虚血 GL 2022
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-159
    source: 'Bala M, Catena F, Kashuk J, et al. Acute mesenteric ischemia: updated guidelines of the World Society of Emergency Surgery. World J Emerg Surg 2022;17:54'
    doi: 10.1186/s13017-022-00443-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-022-00443-x
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-082
  domain: AB
  subdomain: 腹腔内圧上昇と腹部コンパートメント症候群
  assertion:
    plain_statement_ja: 重症成人の腹腔内圧は通常5〜7 mmHg である。腹腔内高血圧は12 mmHg 以上が持続または反復する状態と定義され、12〜15（I度）、16〜20（II度）、21〜25（III度）、25超（IV度）に分けられる。腹部コンパートメント症候群は、腹腔内圧が20 mmHg を超えて持続し、新たな臓器障害を伴う状態をいう。
    condition:
      guideline: WSACS 合意定義 2013
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-160
    source: 'Kirkpatrick AW, Roberts DJ, De Waele J, et al. Intra-abdominal hypertension and the abdominal compartment syndrome: updated consensus definitions and clinical practice guidelines from the World Society of the Abdominal Compartment Syndrome. Intensive Care Med 2013;39:1190-1206'
    doi: 10.1007/s00134-013-2906-z
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s00134-013-2906-z
    source_license: CC BY-NC（Creative Commons Attribution Noncommercial License）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: null
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-083
  domain: AB
  subdomain: 腹腔内圧上昇と腹部コンパートメント症候群
  assertion:
    plain_statement_ja: 腹腔内圧は膀胱内圧で測るのが標準で、滅菌生理食塩水を最大25 mL 注入し、仰臥位で腹筋の収縮がないことを確かめ、中腋窩線で零点を合わせ、呼気終末に mmHg で表す。腹部灌流圧は平均動脈圧から腹腔内圧を引いて求める。明らかな腹部コンパートメント症候群には減圧開腹術が推奨されている。
    condition:
      guideline: WSACS 合意定義 2013
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-160
    source: 'Kirkpatrick AW, Roberts DJ, De Waele J, et al. Intra-abdominal hypertension and the abdominal compartment syndrome: updated consensus definitions and clinical practice guidelines from the World Society of the Abdominal Compartment Syndrome. Intensive Care Med 2013;39:1190-1206'
    doi: 10.1007/s00134-013-2906-z
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s00134-013-2906-z
    source_license: CC BY-NC（Creative Commons Attribution Noncommercial License）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: null
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-084
  domain: AB
  subdomain: 腹部外傷の基本
  assertion:
    plain_statement_ja: 腹部外傷では、E-FAST（拡大した迅速超音波検査）が腹腔内の液体貯留を速やかに見つけるのに有効で、循環が安定しているか安定化した患者では造影 CT が標準の検査である。循環動態の不安定は、来院時の収縮期血圧90 mmHg 未満で皮膚の血管収縮を伴う状態などで定義される。
    condition:
      guideline: WSES 脾損傷 GL 2017
    differential: null
    common_misconception: 腹部外傷では循環が不安定でもまず CT を撮る
  provenance:
    source_ref: SRC-161
    source: 'Coccolini F, Montori G, Catena F, et al. Splenic trauma: WSES classification and guidelines for adult and pediatric patients. World J Emerg Surg 2017;12:40'
    doi: 10.1186/s13017-017-0151-4
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-017-0151-4
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: null
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-085
  domain: AB
  subdomain: 腹部外傷の基本
  assertion:
    plain_statement_ja: 循環が安定し、ほかに手術を要する損傷がない脾損傷では、損傷の程度にかかわらず、まず非手術的治療を試みることが勧められている。CT で造影剤の血管外漏出がある安定した患者では、血管造影・塞栓術を第1の介入として考えてよい。
    condition:
      guideline: WSES 脾損傷 GL 2017
    differential: null
    common_misconception: 脾損傷は重症度が高ければ全例で脾摘出術を行う
  provenance:
    source_ref: SRC-161
    source: 'Coccolini F, Montori G, Catena F, et al. Splenic trauma: WSES classification and guidelines for adult and pediatric patients. World J Emerg Surg 2017;12:40'
    doi: 10.1186/s13017-017-0151-4
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-017-0151-4
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: null
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: AB-086
  domain: AB
  subdomain: 腹部外傷の基本
  assertion:
    plain_statement_ja: 脾摘出術後のワクチン接種は術後14日以降に始めることが提案されている。脾摘出術や脾動脈塞栓術のあと15日より前に退院する場合は、退院前の接種が望ましい。
    condition:
      guideline: WSES 脾損傷 GL 2017
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-161
    source: 'Coccolini F, Montori G, Catena F, et al. Splenic trauma: WSES classification and guidelines for adult and pediatric patients. World J Emerg Surg 2017;12:40'
    doi: 10.1186/s13017-017-0151-4
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-017-0151-4
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: null
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カード一覧

| ID | 区分 | 出典 | 主張（冒頭） | 国試出題基準 |
|---|---|---|---|---|
| AB-001 | 急性腹症の定義と分類 | SRC-154 | 急性腹症は、発症から1週間以内に始まった急な腹痛か、慢性の腹痛が急に悪化したもの… | — |
| AB-002 | 急性腹症の定義と分類 | SRC-154 | 急性腹症の痛みの病態は、壁側腹膜の炎症（体性痛）、管腔臓器の閉塞（内臓痛）、血管… | — |
| AB-003 | 急性腹症の定義と分類 | SRC-154 | 日本のガイドラインは、機械的な閉塞を伴うものを「腸閉塞症」、機械的な閉塞がなく腸… | — |
| AB-004 | 急性腹症の定義と分類 | SRC-154 | 機械的な閉塞のない偽性腸閉塞症は、分類上はイレウス（機械的閉塞を伴わない）に入る… | — |
| AB-005 | 急性腹症の定義と分類 | SRC-154 | 急性虫垂炎は、組織学的にカタル性、蜂窩織炎性、壊疽性に分けられ、臨床的には単純性… | — |
| AB-006 | 急性腹症の疫学と予後 | SRC-154 | 急性腹症の原因として多いのは、急性虫垂炎、腸閉塞、胆石症、尿管結石、憩室炎である… | — |
| AB-007 | 急性腹症の疫学と予後 | SRC-154 | 日本の DPC データ（2009〜2011年）では、急性腹症で最も多かったのは男… | — |
| AB-008 | 急性腹症の疫学と予後 | SRC-154 | 日本で手術を受けた急性腹症1,456例の年齢別の検討では、7〜17歳の87.7%… | — |
| AB-009 | 急性腹症の疫学と予後 | SRC-154 | 急性腹痛は救急外来の受診者の5〜10%を占めると報告されている。致死的な症例は0… | — |
| AB-010 | 急性腹症の疫学と予後 | SRC-154 | 急性発症の腹痛では、初診時に約7割で診断がつき、約3割は非特異的腹痛（NSAP）… | — |
| AB-011 | 急性腹症の疫学と予後 | SRC-154 | 急性腹症では、原因が心血管系の病変である場合や、SOFA スコアが高く全身状態が… | — |
| AB-012 | 急性腹症の疫学と予後 | SRC-154 | 消化管穿孔では、食道穿孔と下部消化管穿孔の死亡率が、胃・十二指腸穿孔より一般に高… | 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a） |
| AB-013 | 急性腹症の疫学と予後 | SRC-154 | 急性腹症は、症例数の多い施設のほうが少ない施設より診断率や予後がよい傾向がある。… | — |
| AB-014 | 急性腹症の疫学と予後 | SRC-154 | 腹痛に関連して医療訴訟になりやすい疾患として、腹膜炎（汎発性を含む）、心筋梗塞、… | — |
| AB-015 | 緊急度の判断と緊急処置 | SRC-154 | 緊急手術の対象になるのは、一般に、血管の破裂、腹腔内出血、腸管の虚血・壊死、汎発… | — |
| AB-016 | 緊急度の判断と緊急処置 | SRC-154 | 短時間で命にかかわる腹痛として、大動脈瘤破裂や大動脈解離による出血があり、敗血症… | — |
| AB-017 | 緊急度の判断と緊急処置 | SRC-154 | 緊急の内視鏡検査や処置が必要になる腹痛の原因として、消化管出血、急性胆管炎、消化… | — |
| AB-018 | 緊急度の判断と緊急処置 | SRC-154 | 急性腹症を疑ったら、まずバイタルサインを確認し、異常があれば緊急処置を行いながら… | — |
| AB-019 | 緊急度の判断と緊急処置 | SRC-154 | 急性腹症で腹腔内感染症と診断したら、循環動態が安定していても初期輸液をすぐに始め… | — |
| AB-020 | 緊急度の判断と緊急処置 | SRC-154 | 腹腔内感染が疑われる急性腹症には、できるだけ早く抗菌薬を投与することが提案されて… | 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a） |
| AB-021 | 急性腹症の医療面接と身体診察 | SRC-154 | 急性腹症の病歴では、腹痛の性状、警告症状（red flag sign）、疾患に特… | — |
| AB-022 | 急性腹症の医療面接と身体診察 | SRC-154 | 急性腹症の身体診察では、外観とバイタルサインで緊急度と重症度を評価し、腹部は視診… | — |
| AB-023 | 急性腹症の医療面接と身体診察 | SRC-154 | 急性腹症では、頻呼吸があると肺炎、心肺不全、菌血症の可能性が高まり（エビデンスの… | — |
| AB-024 | 急性腹症の医療面接と身体診察 | SRC-154 | 腹部の視診では、手術瘢痕、皮膚所見、腹部膨満、腹壁ヘルニア、拍動、腫瘤、呼吸に伴… | — |
| AB-025 | 急性腹症の医療面接と身体診察 | SRC-154 | 腸蠕動音はよく伝わるので、聴診は1か所で十分とされる。急性腹症での聴診の臨床的意… | — |
| AB-026 | 急性腹症の医療面接と身体診察 | SRC-154 | 小腸閉塞の患者50例の報告では、腸蠕動音の亢進が50%、減弱または消失が24%に… | — |
| AB-027 | 急性腹症の医療面接と身体診察 | SRC-154 | 腹膜刺激徴候は、炎症などが壁側・臓側腹膜に及んで刺激されたときに出る徴候で、直接… | 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a） |
| AB-028 | 急性腹症の医療面接と身体診察 | SRC-154 | 腹膜刺激徴候がなくても、臨床的に腹膜炎や腸間膜虚血が疑われる場合は画像検査を追加… | 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a） |
| AB-029 | 急性腹症の医療面接と身体診察 | SRC-154 | 急性虫垂炎では、腸腰筋テストと閉鎖筋テストの特異度が高い（エビデンスの確実性 C… | 医学各論 Ⅵ-9-A-④（閉鎖孔ヘルニア、b） |
| AB-030 | 急性腹症の医療面接と身体診察 | SRC-154 | Carnett 徴候は、仰臥位で腕を胸の前で組んだ患者に頭を少し持ち上げて腹筋を… | — |
| AB-031 | 急性腹症の医療面接と身体診察 | SRC-154 | 急性腹症の診断で直腸診をルーチンに行う意義は限られている。ただし、排便障害、便の… | — |
| AB-032 | 急性腹症の医療面接と身体診察 | SRC-154 | 腹痛の診断がつく前に鎮痛薬（アセトアミノフェンやオピオイド）を使っても、診断率の… | — |
| AB-033 | 急性腹症の医療面接と身体診察 | SRC-154 | 急性腹症の鎮痛では、痛みの強さにかかわらずアセトアミノフェンの静脈投与が勧められ… | — |
| AB-034 | 急性腹症の医療面接と身体診察 | SRC-154 | 血液検査や画像検査は偽陰性になることがあるため、急性腹症は病歴と身体所見を含めて… | — |
| AB-035 | 急性腹症の検査 | SRC-154 | プロカルシトニンは、敗血症の診断と重症度の判定、急性膵炎の重症度の判定、複雑性虫… | — |
| AB-036 | 急性腹症の検査 | SRC-154 | 複雑性虫垂炎の診断には、プロカルシトニン、CRP、好中球/リンパ球比（NLR）が… | — |
| AB-037 | 急性腹症の検査 | SRC-154 | 急性腹症の鑑別では、急性膵炎の診断にはリパーゼの測定が役立つが、それ以外の疾患で… | — |
| AB-038 | 急性腹症の検査 | SRC-154 | 心窩部痛があり虚血性心疾患の危険因子がある患者では、心筋梗塞を考えて心電図をとる… | — |
| AB-039 | 急性腹症の検査 | SRC-154 | 妊娠しうる年齢の女性で妊娠を否定できない場合は、急性腹症の評価に妊娠反応検査が役… | — |
| AB-040 | 急性腹症の検査 | SRC-154 | 急性腹症の画像検査で最初に行うのは超音波検査で、非侵襲的で簡便で普及しているため… | — |
| AB-041 | 急性腹症の検査 | SRC-154 | POCUS の診断精度は、部位ごとに50例程度の経験で超音波検査の専門家と同等に… | — |
| AB-042 | 急性腹症の検査 | SRC-154 | 腹部単純 X 線検査の診断能は限られ、急性腹症のルーチン検査として行う意義は乏し… | — |
| AB-043 | 急性腹症の検査 | SRC-154 | 急性腹症の多くは単純 CT で診断できる。臓器虚血、血管性病変、急性膵炎の重症度… | — |
| AB-044 | 急性腹症の検査 | SRC-154 | eGFR が30 mL/min/1.73 m²未満の患者に急性腹症でヨード造影剤… | — |
| AB-045 | 急性腹症の検査 | SRC-154 | MRI は、超音波検査で確定診断がつかない妊婦の急性腹症や、超音波検査や CT … | — |
| AB-046 | 急性腹症の鑑別診断 | SRC-154 | 腹痛の部位別にみると、右上腹部痛では食道・胃・十二指腸疾患と肝胆道系疾患が、心窩… | — |
| AB-047 | 急性腹症の鑑別診断 | SRC-154 | 急性腹症と紛らわしい病態には、腹腔外の臓器や全身疾患によるものがあり、特に胸腔内… | — |
| AB-048 | 急性腹症の鑑別診断 | SRC-154 | 高齢者の急性腹症では、身体所見や血液検査が病状を正確に反映しないことが多く、手術… | — |
| AB-049 | 急性腹症の鑑別診断 | SRC-154 | 免疫不全の患者では重症の腹膜炎でも発熱が乏しい傾向があり、軽い身体所見を重視し、… | — |
| AB-050 | 急性腹症の鑑別診断 | SRC-154 | 手術歴のある患者の急性腹症では、癒着性腸閉塞、胆嚢炎、胆道再建後の胆管炎、輸入脚… | — |
| AB-051 | 急性腹症の鑑別診断 | SRC-154 | 妊婦の急性腹症では、異所性妊娠（内外同時妊娠を含む）、流早産、陣痛、常位胎盤早期… | — |
| AB-052 | 急性腹症の鑑別診断 | SRC-154 | 異所性妊娠は、無月経（最終月経から6週間以上）、性器出血または下腹部痛があり、妊… | — |
| AB-053 | 急性腹症の鑑別診断 | SRC-154 | 学童期の腹痛の原因で最も多いのは急性胃腸炎で、緊急手術が必要なものでは急性虫垂炎… | — |
| AB-054 | 急性腹症の鑑別診断 | SRC-154 | 急性発症の腹痛で、血尿、腰部・腎部の圧痛、痛みの持続が12時間以下、食欲が保たれ… | — |
| AB-055 | 急性虫垂炎 | SRC-155 | 急性虫垂炎の生涯リスクは米国で9%、欧州で8%、アフリカで2%と報告されている。… | — |
| AB-056 | 急性虫垂炎 | SRC-155 | WSES 2020 は、成人の急性虫垂炎の予測に AIR スコアと AAS スコ… | — |
| AB-057 | 急性虫垂炎 | SRC-155 | WSES 2020 は、成人・小児とも最初の画像検査としてベッドサイドの超音波検… | — |
| AB-058 | 急性虫垂炎 | SRC-155 | 妊婦で虫垂炎を疑う場合、WSES 2020 は最初に段階的圧迫法の経腹超音波検査… | — |
| AB-059 | 急性虫垂炎 | SRC-155 | WSES 2020 は、糞石のない単純性虫垂炎の一部の患者には、抗菌薬による非手… | — |
| AB-060 | 急性虫垂炎 | SRC-155 | WSES 2020 は、手術が必要な虫垂炎では24時間以内の次の手術枠で腹腔鏡下… | — |
| AB-061 | 急性虫垂炎 | SRC-155 | WSES 2020 は、急性虫垂炎の手術前に広域抗菌薬を1回投与し、単純性虫垂炎… | — |
| AB-062 | 急性虫垂炎 | SRC-155 | WSES 2020 は、膿瘍を伴う虫垂炎では、腹腔鏡の技術がない施設では抗菌薬と… | — |
| AB-063 | 癒着性小腸閉塞 | SRC-156 | 小腸閉塞の原因で最も多いのは術後の癒着で、約60%を占める。大腸切除後には10人… | — |
| AB-064 | 癒着性小腸閉塞 | SRC-156 | 癒着性小腸閉塞では、CT は絞扼と緊急手術の必要性を約90%の精度で予測する。閉… | — |
| AB-065 | 癒着性小腸閉塞 | SRC-156 | 腹膜炎、絞扼、腸管虚血の徴候がない癒着性小腸閉塞は、絶飲食と経鼻胃管または長いイ… | — |
| AB-066 | 癒着性小腸閉塞 | SRC-156 | 癒着性小腸閉塞では水溶性造影剤を投与し、24時間後の腹部 X 線で造影剤が大腸に… | — |
| AB-067 | 癒着性小腸閉塞 | SRC-156 | 癒着性小腸閉塞の再発は、非手術的治療後で1年12%・5年20%、手術後で1年8%… | — |
| AB-068 | 癒着性小腸閉塞 | SRC-156 | 癒着性小腸閉塞の手術では、選ばれた症例で腹腔鏡下の癒着剝離術が合併症を減らす可能… | — |
| AB-069 | 鼠径部ヘルニア | SRC-158 | 鼠径部ヘルニアの生涯の発生率は、男性で27〜43%、女性で3〜6%と報告されてい… | 医学各論 Ⅵ-9-A-②（鼠径ヘルニア、a） |
| AB-070 | 鼠径部ヘルニア | SRC-158 | 鼠径部ヘルニアの多くは身体診察で診断でき、超音波検査が必要になることはまれである… | 医学各論 Ⅵ-9-A-②（鼠径ヘルニア、a） |
| AB-071 | 鼠径部ヘルニア | SRC-158 | 症状がないか軽い男性の鼠径ヘルニアは、経過観察（watchful waiting… | 医学各論 Ⅵ-9-A-②（鼠径ヘルニア、a） |
| AB-072 | 鼠径部ヘルニア | SRC-158 | 鼠径ヘルニアの修復はメッシュを使う方法が第1選択で、開腹（Lichtenstei… | 医学各論 Ⅵ-9-A-②（鼠径ヘルニア、a） |
| AB-073 | 鼠径部ヘルニア | SRC-158 | 嵌頓・絞扼の危険因子には、女性、大腿ヘルニア、鼠径部ヘルニアによる入院歴がある。… | 医学各論 Ⅵ-9-A-③（大腿ヘルニア、a） |
| AB-074 | 鼠径部ヘルニア | SRC-158 | 鼠径部ヘルニアの緊急手術は待機手術より合併症と死亡が多い。プールした解析では、待… | 医学各論 Ⅵ-9-A-②（鼠径ヘルニア、a） |
| AB-075 | 腹膜炎・腹腔内感染症 | SRC-157 | 腹腔内感染症は、感染が1つの臓器にとどまり腹膜に及んでいない「単純性」と、臓器を… | 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a） |
| AB-076 | 腹膜炎・腹腔内感染症 | SRC-157 | 腹膜炎は、消化管の連続性が保たれたまま起こる一次性（特発性細菌性腹膜炎など）、最… | 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a） |
| AB-077 | 腹膜炎・腹腔内感染症 | SRC-157 | 腹腔内感染症の治療では、感染源の制御を可能な限り早く完全に行うことが重要で、手術… | 医学各論 Ⅵ-9-B-①（細菌性腹膜炎、a） |
| AB-078 | 急性腸間膜虚血 | SRC-159 | 急性腸間膜虚血は、緊急外科入院の0.09〜0.2%とまれだが、年齢とともに増え、… | — |
| AB-079 | 急性腸間膜虚血 | SRC-159 | 身体所見に比べて不釣り合いに強い腹痛は、否定されるまで急性腸間膜虚血として扱うこ… | — |
| AB-080 | 急性腸間膜虚血 | SRC-159 | 急性腸間膜虚血を疑ったら、遅滞なく CT 血管造影を行うことが強く推奨されている… | — |
| AB-081 | 急性腸間膜虚血 | SRC-159 | 急性腸間膜虚血の治療では、動脈閉塞には技術があれば血管内治療による血行再建を第1… | — |
| AB-082 | 腹腔内圧上昇と腹部コンパートメント症候群 | SRC-160 | 重症成人の腹腔内圧は通常5〜7 mmHg である。腹腔内高血圧は12 mmHg … | — |
| AB-083 | 腹腔内圧上昇と腹部コンパートメント症候群 | SRC-160 | 腹腔内圧は膀胱内圧で測るのが標準で、滅菌生理食塩水を最大25 mL 注入し、仰臥… | — |
| AB-084 | 腹部外傷の基本 | SRC-161 | 腹部外傷では、E-FAST（拡大した迅速超音波検査）が腹腔内の液体貯留を速やかに… | — |
| AB-085 | 腹部外傷の基本 | SRC-161 | 循環が安定し、ほかに手術を要する損傷がない脾損傷では、損傷の程度にかかわらず、ま… | — |
| AB-086 | 腹部外傷の基本 | SRC-161 | 脾摘出術後のワクチン接種は術後14日以降に始めることが提案されている。脾摘出術や… | — |

## 4. 重複回避と境界の確認

- 特発性細菌性腹膜炎（急性腹症GL BQ67）は LV で扱い済みのため作っていません。AB-076 では腹膜炎の分類の中で触れるだけにしました。
- 慢性特発性偽性腸閉塞症の診断基準は NG で扱い済み。AB-004 は腸閉塞症とイレウスの定義の中での位置づけに限りました。
- 急性膵炎の診断基準は BP で扱い済み。AB-037 はリパーゼとアミラーゼの有用性の比較に限りました。
- 第5回からの引き継ぎ「急性腹症としての胆嚢炎・膵炎の初期鑑別」は、部位別の鑑別（AB-046）、造影CTの適応（AB-043）、鎮痛（AB-033）で症候の側から扱いました。
- 食道裂孔ヘルニア（Ⅵ-9-A-①）は ES で扱い済みです。

## 5. なお未作成のトピック（欠番補完ラウンドで扱う）

- 腹壁瘢痕ヘルニア・臍ヘルニア、閉鎖孔ヘルニアの疫学と治療（WSES 腹壁ヘルニア緊急修復GL が読めなかったため）
- 腸重積（小児・成人）、S状結腸軸捻転、大腸癌による閉塞
- 消化管穿孔（消化性潰瘍穿孔）の治療、横隔膜下・Douglas 窩膿瘍（Ⅵ-9-B-②）
- 癌性腹膜炎、腹膜中皮腫、腹膜偽粘液腫、後腹膜腫瘍（Ⅵ-9-C）
- 腹部外傷の肝・膵・腸管損傷、小児の急性腹症の詳細
- 国試出題基準 Ⅵ-3 の急性虫垂炎・腸閉塞の番号（調査側で表を取得できず `kokushi: null`。出題基準の PDF から付ける）

## 6. Claude Code での照合時に重点的に確認する点

1. SRC-155〜161 の PMID・PMCID とライセンスを DOI から確定する。本文の確認では、Europe PMC の全文で次を確かめた：SRC-155 PMID 32295644、SRC-156 PMID 29946347・PMC6006983、SRC-157 PMID 28702076・PMC5504840、SRC-158 PMID 29330835・PMC5809582、SRC-159 PMID 36261857・PMC9580452、SRC-160 PMID 23673399・PMC3680657、SRC-161 PMID 28828034・PMC5562999。ルールに従い、カードには書かず API で確定すること。
2. SRC-158（HerniaSurge）は CC BY-NC 4.0、SRC-160（WSACS）は CC BY-NC のため RESTRICTED とした。Crossref の license 欄で確認する。
3. SRC-154 を出典とするカードの数値は、ユーザー提供の刊行版PDFの本文と機械照合し、全件一致した。本文との長い一致文字列（20字以上）がないことも確認済み。「二次資料経由」と書いたカード（AB-007・008・026・028 など）は、ガイドラインが引用した原著と照合する。
4. 腹部コンパートメント症候群（AB-082・083）と腹部外傷（AB-084〜086）は、コアカリの番号表に該当がないため `core_curriculum: null` とした。
5. 急性腹症GL2025 英語版の公開後、SRC を付けて corroboration を追記する。

## 7. 第7回（横断項目、接頭辞 XS）への引き継ぎ

- SRC 番号は SRC-162 から。
- 腹痛・嘔吐などの主要症候は、AB で急性腹症の側から扱った（医療面接、身体診察、検査、鎮痛）。第7回では慢性の症候と、腹痛以外の症候（吐下血、黄疸、腹水、下痢・便秘）を中心にし、AB と同じ命題を作らない。
- 画像検査（超音波、単純X線、CT、MRI、造影剤の注意）は AB-040〜045 で急性腹症の文脈で扱った。第7回では検査の一般論として重ならない範囲にする。
