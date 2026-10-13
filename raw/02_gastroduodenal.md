# 第2回 胃・十二指腸（GD-001〜GD-095）完成版

- 作成日：2026-10-12（補充ラウンド：2026-10-13）
- 事実票：95件（GD-001〜GD-095、欠番なし）。初回 GD-001〜073 に、補充ラウンドの GD-074〜095（22件）を加えた。全件 `status: draft`、`verifier: null`
- 取り込み時の注意：YAMLブロックは1つだけで、アンカー・マージキー・脚注番号は使っていません。`fact.schema.json` での検証を通過済みです。

## 1. 出典マスター（新規 SRC-028〜047、既存 SRC-017・018 を再利用）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 使用カード数 |
|---|---|---|---|---|---|---|
| SRC-017 | 日本門脈圧亢進症学会 門脈圧亢進症取扱い規約 第3版の内視鏡所見記載基準（日消誌116(5):395で確認） | — | — | 非CC | RESTRICTED | 1 |
| SRC-018 | Yoshiji H, et al. Evidence-based clinical practice guidelines for Liver Cirrhosis 2020. J Gastroenterol 2021;56:593-619 | 10.1007/s00535-021-01788-x | — | Springer OA（CC種別は未確認） | UNKNOWN | 1 |
| SRC-028 | Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61 | 10.1007/s00535-021-01843-7 | — | Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認） | UNKNOWN | 18 |
| SRC-029 | Japanese Gastric Cancer Association. Japanese Gastric Cancer Treatment Guidelines 2021 (6th edition). Gastric Cancer 2023;26:1-25 | 10.1007/s10120-022-01331-8 | — | Open access, © 2022 The Author(s)（CC種別はCrossrefで要確認） | UNKNOWN | 2 |
| SRC-030 | Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299 | 10.1007/s10120-025-01698-4 | — | Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認） | UNKNOWN | 23 |
| SRC-031 | Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381 | 10.1007/s00535-026-02504-3 | — | CC BY 4.0（パイロット時にCrossrefで確認） | OPEN | 14 |
| SRC-032 | Hirota S, et al. English version of Japanese Clinical Practice Guidelines 2022 for gastrointestinal stromal tumor (GIST). Int J Clin Oncol 2024;29:647-680 | 10.1007/s10147-024-02488-1 | 38609732 | Open access, © 2024 The Author(s)（CC種別はCrossrefで要確認） | UNKNOWN | 8 |
| SRC-033 | Joensuu H, et al. Adjuvant imatinib for high-risk GI stromal tumor: analysis of a randomized trial. J Clin Oncol 2016;34:244-250 | 10.1200/JCO.2015.62.9170 | 26527782 | 非CC（ASCO） | RESTRICTED | 1 |
| SRC-034 | Janjigian YY, et al. CheckMate 649. Lancet 2021;398:27-40 | 10.1016/S0140-6736(21)00797-2 | 34102137 | 非CC（Elsevier） | RESTRICTED | 1 |
| SRC-035 | Shitara K, et al. SPOTLIGHT. Lancet 2023;401:1655-1668 | 10.1016/S0140-6736(23)00620-7 | 37068504 | 非CC（Elsevier） | RESTRICTED | 1 |
| SRC-036 | 国立がん研究センター がん情報サービス 胃（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新） | — | — | 元データは政府統計。サイト利用規約は要確認 | GOV_JP | 1 |
| SRC-037 | 厚生労働省『がん予防重点健康教育及びがん検診実施のための指針』（平成28年2月改正）／厚労省がん検診ページ | — | — | 政府標準利用規約（原文は要確認） | GOV_JP | 1 |
| SRC-038 | アステラス製薬 適時開示（2024-07-29）：ゾルベツキシマブ 欧州CHMP販売承認勧告（国内承認日の記載あり） | — | — | 企業資料（非CC） | RESTRICTED | 1 |
| SRC-039 | Panzuto F, et al. ENETS 2023 guidance paper for gastroduodenal neuroendocrine tumours (NETs) G1-G3. J Neuroendocrinol 2023;35:e13306 | 10.1111/jne.13306 | — | Open access, © 2023 The Authors（CC種別はCrossrefで要確認） | UNKNOWN | 1 |
| SRC-040 | Scarpellini E, et al. International consensus on the diagnosis and management of dumping syndrome. Nat Rev Endocrinol 2020;16:448-466 | 10.1038/s41574-020-0357-5 | — | CC BY 4.0（出版社ページで確認） | OPEN | 6 |
| SRC-041 | 厚生労働省『アニサキスによる食中毒を予防しましょう』 | — | — | 厚労省ウェブサイト利用規約（政府標準利用規約準拠と想定、原文は要確認） | GOV_JP | 3 |
| SRC-042 | Sugiyama H, et al. Anisakiasis annual incidence and causative species, Japan, 2018-2019. Emerg Infect Dis 2022;28(10) | 10.3201/eid2810.220627 | — | CDC刊行誌。記事ページにパブリックドメインの明示はなく未確認 | UNKNOWN | 2 |
| SRC-043 | Islam RS, et al. Gastric polyps: a review on clinical, endoscopic, histopathologic features and management decisions. Gastroenterol Hepatol (N Y) 2013 Oct | — | — | © Millennium Medical Publishing（非CC） | RESTRICTED | 3 |
| SRC-044 | 岩室雅也. 薬剤起因性胃粘膜病変の内視鏡診断. 日本消化器内視鏡学会雑誌 2025;67(4):281-288 | 10.11280/gee.67.281 | — | © 日本消化器内視鏡学会（J-STAGE無料公開、非CC） | RESTRICTED | 3 |
| SRC-045 | Cook D, et al. Stress ulcer prophylaxis during invasive mechanical ventilation (REVISE). N Engl J Med 2024 | 10.1056/NEJMoa2404245 | — | 非CC（NEJM） | RESTRICTED | 1 |
| SRC-046 | Rizwan MM, et al. Duodenal diverticulum and associated pancreatitis: case report with brief review of literature. World J Gastrointest Endosc 2011;3(3):62-63 | 10.4253/wjge.v3.i3.62 | 21455344 | CC BY-NC 4.0 | RESTRICTED | 2 |
| SRC-047 | Ergüder E, et al. Lemmel syndrome: a single-center cohort and diagnostic considerations. Turk J Surg 2026;42(2):214-219 | 10.47717/turkjsurg.2026.2025-11-25 | — | © Galenos Publishing House（ライセンス種別は未確認） | UNKNOWN | 1 |

- Springer の日本の学会ガイドライン（FD、胃癌第6版・第7版、GIST）は、記事ページで「Open access、© The Author(s)」と表示されていますが、CCの種別は表示されていませんでした。そのため `UNKNOWN` としています。Crossref の license 欄で確定してください。
- JSGE 消化性潰瘍 GL 2026 は、パイロット時に Crossref で CC BY 4.0 を確認済みなので `OPEN` としています（SRC-031 を新規付与）。
- 補充ラウンドで追加した SRC-040〜047 のうち、OPEN は SRC-040（CC BY 4.0）だけです。SRC-046 は CC BY-NC のため RESTRICTED、SRC-042・047 は種別未確認のため UNKNOWN です。
- 全カードの `legal_basis` は B（自作文による事実の記述）です。

## 2. 事実票 YAML

```yaml
- id: GD-001
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: 機能性ディスペプシア（FD）は、心窩部痛や心窩部不快感など上腹部を中心とする症状が慢性的に続き、それを説明できる器質的・全身性・代謝性疾患がない病態である。日本のガイドライン2021は、症状をRome基準の4症状に限定せず、どの症状をディスペプシアとみなすかを診療する医師の判断に委ねている。
    condition:
      region: 日本
      guideline: JSGE FD GL 2021
    differential: Rome IVの4症状：食後膨満感、早期飽満感、心窩部痛、心窩部灼熱感
    common_misconception: Rome IVの4症状以外の訴えがあればFDではないと考える
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-002
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: Rome IVは、診断前3か月間に症状があり、かつ診断の6か月以上前に発症していることを求める。日本の患者の多くは発症から1か月以内に受診するため、日本のガイドライン2021は「慢性」の期間を具体的に定めず医師の判断に委ねている。
    condition:
      region: 国際（Rome IV）vs 日本
    differential: 日本のGLは期間を規定しない
    common_misconception: 日本でもRome IVの期間要件を満たさなければFDと診断できないと考える
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-003
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: FDは症状で定義される病名であり、慢性胃炎は胃粘膜の組織学的な炎症で定義される病名であるため、両者は別の概念である。日本では2013年5月にFDが保険病名として認められた。
    condition:
      region: 日本
    differential: 慢性胃炎は症状の有無と無関係に診断される
    common_misconception: 上腹部症状がある患者はすべて慢性胃炎として扱えばよい
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-004
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: H. pylori感染を伴うディスペプシアは、除菌に成功してから6か月〜1年後に症状が改善した場合、H. pylori関連ディスペプシアとしてFDとは別に扱う。ただし症状があれば、除菌後の経過を待たずにFDに準じた治療を始めてよい。
    condition:
      source: 京都グローバルコンセンサスの概念をJSGE FD GL 2021が採用
    differential: 除菌後も症状が続く場合はFD
    common_misconception: 除菌後に症状が改善するまで治療を始めてはいけない
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: HP-015〜017（除菌の適応・京都コンセンサス）と内容が近いが、本カードはFDとの鑑別の観点に限定
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-005
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: 日本のFDの頻度は、健診受診者で11〜17%、上腹部症状で医療機関を受診した患者で45〜53%と報告されている。一般住民を対象としたWeb調査では7%だった。
    condition:
      region: 日本
    differential: 頻度はFDの定義と対象集団によって変わる
    common_misconception: 日本のFDは欧米より明らかに多い
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 日本のデータはいずれも単施設の横断研究（GL本文の記載）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-006
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: FDの発症には、感染性胃腸炎の既往（メタ解析でオッズ比2.54）、女性、若年、小児期の虐待歴などが関連すると報告されているが、コンセンサスは得られていない。
    condition:
      guideline: JSGE FD GL 2021
    differential: 感染後IBS
    common_misconception: FDは心理的要因だけで起こる
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-007
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: FDのうち胃排出遅延を伴う例は特発性の胃不全麻痺と重なり、その割合はFDの10〜20%程度とされる。胃不全麻痺は機械的閉塞がないのに胃排出が遅れる病態で、FDは排出遅延に加えて胃の適応性弛緩障害や内臓知覚過敏も含む点で異なる。
    condition:
      guideline: JSGE FD GL 2021
    differential: 糖尿病性胃不全麻痺、薬剤性（オピオイド、抗コリン薬）
    common_misconception: FDと胃不全麻痺は同一疾患である
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-008
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: 日本のガイドライン2021では、FDの診断に上部消化管内視鏡は必須ではない。高齢での新たな発症、体重減少、繰り返す嘔吐、出血、嚥下障害、嚥下痛、腹部腫瘤、発熱、食道癌・胃癌の家族歴などの警告徴候があり器質的疾患が疑われる場合に、内視鏡などで精査する。
    condition:
      region: 日本
      guideline: JSGE FD GL 2021（2014年版からの主な変更点）
    differential: 警告徴候がなくても器質的疾患は否定できず、初期治療に反応しなければ精査する
    common_misconception: FDと診断するには全例で内視鏡が必要
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-009
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: FDの初期治療として、PPIとH2受容体拮抗薬は有効とされ、強く推奨されている（エビデンスA）。P-CABはプラセボ対照RCTがなく、有効性を評価できないとされた（弱い推奨、エビデンスC）。
    condition:
      region: 日本
      guideline: JSGE FD GL 2021
    differential: 消化性潰瘍やGERDではP-CABの有効性が示されている
    common_misconception: FDにもP-CABがPPIより優れることが示されている
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-010
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: 2017年のコクランレビューでは、FDに対するPPIの奏効率は31.1%でプラセボの25.8%を上回り、治療必要数は11だった。
    condition:
      guideline: JSGE FD GL 2021が引用したPinto-Sanchez 2017
    differential: H2RAのプラセボに対する相対リスク減少は23%（Cochrane 2006）
    common_misconception: 酸分泌抑制薬はFDのほぼ全例に効く
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値はGL本文の引用値。原著（Cochrane CD011194）は未照合
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-011
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: アセチルコリンエステラーゼ阻害薬のアコチアミドはFDに有用で、使用が強く推奨されている（エビデンスA）。
    condition:
      region: 日本
      guideline: JSGE FD GL 2021
    differential: ドパミン受容体拮抗薬、5-HT4受容体作動薬は二次治療
    common_misconception: 消化管運動機能改善薬はすべて同じ推奨度である
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-012
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: 漢方薬の六君子湯はFDに有効で、使用が強く推奨されている（エビデンスA）。六君子湯以外の漢方薬は二次治療として弱く推奨されている（エビデンスB）。
    condition:
      region: 日本
      guideline: JSGE FD GL 2021
    differential: 六君子湯はRCT（DREAM試験）で不安の改善と症状改善の相関が示された
    common_misconception: 漢方薬はすべて一次治療である
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-013
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: FDの二次治療として、ドパミン受容体拮抗薬と5-HT4受容体作動薬の使用が弱く推奨されている（いずれもエビデンスB）。
    condition:
      region: 日本
      guideline: JSGE FD GL 2021
    differential: アコチアミドは一次治療
    common_misconception: モサプリドはFDの一次治療として強く推奨されている
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-014
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: FDに対して三環系抗うつ薬（エビデンスA）とタンドスピロンなどの抗不安薬（エビデンスB）は有効とされ、二次治療として弱く推奨されている。三環系抗うつ薬は副作用に注意して使う。心身医学的治療も弱く推奨されている。
    condition:
      region: 日本
      guideline: JSGE FD GL 2021
    differential: Fordらのメタ解析では5-HT1A作動薬の有効性は示されなかったが、日本のRCTではタンドスピロンが有効だった
    common_misconception: 向精神薬はFDの一次治療である
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-015
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: 制酸薬、プロスタグランジン製剤、スクラルファートやレバミピドなどの粘膜保護薬がFDに有効かどうかは明らかでない。
    condition:
      guideline: JSGE FD GL 2021（推奨なし、エビデンスB）
    differential: 日本のレバミピドのRCTでは効果が示されなかった
    common_misconception: 粘膜保護薬はFDの標準治療である
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-016
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: FDではプラセボの効果が大きく、メタ解析では5〜90%、平均56%と報告されている。良好な医師患者関係はFDの治療に有用とされる。
    condition:
      guideline: JSGE FD GL 2021
    differential: プラセボ反応の低下要因：低BMI、喫煙など
    common_misconception: プラセボで改善する症状は詐病である
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-017
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: FDにはIBS、GERD、慢性便秘などがよく重なる。Rome IVで診断したFDではIBSの合併が66.9%と報告されている。FDは再発することがあるが、死亡率の上昇とは関連しない。
    condition:
      guideline: JSGE FD GL 2021
    differential: 日本でアコチアミドで改善したFDの1年後の再発は25%
    common_misconception: FDは生命予後を悪化させる
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-018
  domain: GD
  subdomain: 機能性ディスペプシア
  assertion:
    plain_statement_ja: FDのサブタイプ（EPS、PDS）に基づいて治療を選ぶ方法は議論があり、ACG/CAGの2017年ガイドラインはサブタイプによる治療選択を推奨していない。難治例で治療を変更する時期は4〜8週後が提案されているが、さらなる検討が必要とされる。
    condition:
      guideline: JSGE FD GL 2021（FRQ）
    differential: Rome IVはEPSに酸分泌抑制薬、PDSに運動機能改善薬を提案した
    common_misconception: PDSには必ず運動機能改善薬、EPSには必ず酸分泌抑制薬を使う
  provenance:
    source_ref: SRC-028
    source: Miwa H, et al. Evidence-based clinical practice guidelines for functional dyspepsia 2021. J Gastroenterol 2022;57:47-61
    doi: 10.1007/s00535-021-01843-7
    pmid: null
    pmcid: PMC8831363
    url: https://link.springer.com/article/10.1007/s00535-021-01843-7
    source_license: Open access, © 2022 The Author(s)（CC種別は出版社ページで未表示。Crossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-019
  domain: GD
  subdomain: NSAID・LDA潰瘍の予防
  assertion:
    plain_statement_ja: 潰瘍の既往がない患者でも、NSAIDによる潰瘍の予防にはPPIが強く推奨されている（エビデンスA）。ただし日本では、NSAID服用者の一次予防へのPPIは保険適用外である。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 CQ-13
    differential: PG製剤や高用量H2RAにも予防効果があるが、PPIの方が効果が大きい
    common_misconception: 潰瘍の既往がなければ予防は不要
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-③（消化性潰瘍、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-020
  domain: GD
  subdomain: NSAID・LDA潰瘍の予防
  assertion:
    plain_statement_ja: 潰瘍の既往がありNSAIDが必要な患者には、VPZまたはPPIによる再発予防が強く推奨されている（エビデンスB）。出血性潰瘍の既往がある場合は、選択的COX-2阻害薬とVPZまたはPPIの併用が弱く推奨されている（エビデンスB）。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 CQ-14
    differential: PG製剤は有効だが下痢による脱落が多い
    common_misconception: COX-2阻害薬に切り替えれば酸分泌抑制薬は不要
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-③（消化性潰瘍、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-021
  domain: GD
  subdomain: NSAID・LDA潰瘍の予防
  assertion:
    plain_statement_ja: NSAIDを副腎皮質ステロイドや抗血栓薬と併用する患者では、潰瘍予防のため選択的COX-2阻害薬の使用が強く推奨されている（エビデンスB）。重い併存疾患がある患者では、VPZまたはPPIによる予防が強く推奨されている（エビデンスB）。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 CQ-15
    differential: 非選択的NSAIDやLDAとステロイド・抗凝固薬の併用は上部消化管出血のリスクを高める
    common_misconception: ステロイド単独と同じ扱いでよい
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-③（消化性潰瘍、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-022
  domain: GD
  subdomain: NSAID・LDA潰瘍の予防
  assertion:
    plain_statement_ja: NSAID潰瘍は原則としてNSAIDを中止して治療する。NSAIDを中止できない場合は、VPZまたはPPIで治療する。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 治療アルゴリズム
    differential: LDA潰瘍は可能な限りLDAを中止せずに治療する
    common_misconception: NSAIDを続けたままでは潰瘍は治らない
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-③（消化性潰瘍、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-023
  domain: GD
  subdomain: NSAID・LDA潰瘍の予防
  assertion:
    plain_statement_ja: 低用量アスピリン（LDA）関連の潰瘍は、LDAを継続したままPPIを併用して治療することが強く推奨されている（エビデンスA）。PPI単独とLDA＋PPIで潰瘍治癒率は同程度だった。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 CQ-16
    differential: 出血後のLDA再開時期はUG-016で扱う
    common_misconception: LDA潰瘍の治療中は必ずLDAを中止する
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-5-A-①（抗血小板薬による粘膜障害、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-024
  domain: GD
  subdomain: NSAID・LDA潰瘍の予防
  assertion:
    plain_statement_ja: 潰瘍の既往がないLDA服用者でも、潰瘍の一次予防にPPIが強く推奨されている（エビデンスA）。抗血小板薬2剤併用（DAPT）では、PPIまたはVPZによる上部消化管出血の一次予防が強く推奨されている（エビデンスA）。日本では、潰瘍の既往がない場合のこれらの使用は保険適用外である。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 CQ-17
    differential: DAPTではPPIがH2RAより上部消化管出血を減らした（RR 0.21）
    common_misconception: LDA単剤なら予防は不要
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-5-A-①（抗血小板薬による粘膜障害、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-025
  domain: GD
  subdomain: NSAID・LDA潰瘍の予防
  assertion:
    plain_statement_ja: 潰瘍の既往があるLDA服用者の再発予防には、PPIまたはVPZが強く推奨されている（エビデンスA）。VPZ 10 mgはランソプラゾールよりLDA潰瘍の再発を有意に抑えた。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 CQ-18
    differential: PPIはH2RAより再発を減らした
    common_misconception: H2RAとPPIの予防効果は同等である
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-5-A-①（抗血小板薬による粘膜障害、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-026
  domain: GD
  subdomain: NSAID・LDA潰瘍の予防
  assertion:
    plain_statement_ja: LDA服用中にNSAIDが必要な潰瘍既往患者では、セレコキシブとPPIの併用が強く推奨されている（エビデンスA）。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 CQ-20
    differential: 非選択的NSAID＋LDAは消化管イベントが多い
    common_misconception: LDA併用時はNSAIDの種類を問わない
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-5-A-①（抗血小板薬による粘膜障害、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-027
  domain: GD
  subdomain: NSAID・LDA潰瘍の予防
  assertion:
    plain_statement_ja: 出血リスクの高い抗凝固薬服用者では、消化性潰瘍出血の予防にPPIの併用が弱く推奨されている（エビデンスC）。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 CQ-21
    differential: ワルファリンとエドキサバンでPPI併用による出血リスク低下の報告がある
    common_misconception: 抗凝固薬は抗血小板薬と違い上部消化管出血の原因にならない
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-③（消化性潰瘍、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-028
  domain: GD
  subdomain: 酸分泌抑制薬の長期使用
  assertion:
    plain_statement_ja: PPIやVPZの長期使用は胃底腺ポリープの増加と関連する。胃癌との関連は観察研究の結果が一致せず、因果関係は確立していない。長期投与は慎重に行い、定期的な内視鏡を考慮する。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 FRQ-3
    differential: PPI/VPZ関連の胃神経内分泌腫瘍はまれで、主に症例報告
    common_misconception: PPIの長期使用は胃癌の原因であることが証明されている
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-D-①（胃ポリープ、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-029
  domain: GD
  subdomain: 消化性潰瘍
  assertion:
    plain_statement_ja: 球後部・下行部の十二指腸潰瘍はまれで、虚血の関与が示唆されている。高齢者や維持透析など重い併存疾患をもつ患者に多い。保存的治療としてVPZ、PPI、ミソプロストールが弱く推奨されており（エビデンスD）、血管病変の検索も必要である。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 CQ-24
    differential: 難治例では胆管・膵管ドレナージで治癒が得られた報告がある
    common_misconception: 球後部潰瘍も球部潰瘍と同様にH. pyloriが主因である
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-③（消化性潰瘍、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-030
  domain: GD
  subdomain: 消化性潰瘍
  assertion:
    plain_statement_ja: 残胃潰瘍の治療にはPPIが強く推奨されている（エビデンスC）。残胃潰瘍に対するH. pylori除菌の有効性を示したRCTはない。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 CQ-25
    differential: VPZがPPIより優れるとのエビデンスはない
    common_misconception: 残胃潰瘍は全例で除菌すれば治る
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-③（消化性潰瘍、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-031
  domain: GD
  subdomain: 消化性潰瘍
  assertion:
    plain_statement_ja: 非H. pyloriヘリコバクター（NHPH）感染は、日本の研究でH. pylori陰性の胃・十二指腸疾患患者の20.8%に、健診受診者の3.0%に認められた。NHPHによる潰瘍の頻度はまだ明らかでない。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 FRQ-4
    differential: HP-019（NHPH潰瘍の増加という指摘）とは別に頻度を扱う
    common_misconception: H. pylori陰性なら細菌性の胃炎は否定できる
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-②（慢性胃炎、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-032
  domain: GD
  subdomain: 慢性胃炎
  assertion:
    plain_statement_ja: 除菌成功後でも、胃酸分泌が低下した胃ではウレアーゼを産生するH. pylori以外の菌によって尿素呼気試験が弱陽性となることがある。これにより不要な除菌が繰り返される状態は「エンドレス除菌」と呼ばれ、自己免疫性胃炎で起こりやすい。除菌に2回以上失敗したとされた症例の18%が自己免疫性胃炎だったとの報告がある。
    condition:
      region: 日本
      guideline: JSGE PUD GL 2026 FRQ-1
    differential: 真の除菌失敗
    common_misconception: 尿素呼気試験が陽性なら必ずH. pyloriが残っている
  provenance:
    source_ref: SRC-031
    source: Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026;61:1361-1381
    doi: 10.1007/s00535-026-02504-3
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s00535-026-02504-3
    source_license: CC BY 4.0（パイロット時にCrossrefで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-②（慢性胃炎、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-033
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 日本の胃癌は、2023年に104,864例（男性71,135例、女性33,729例）が診断され、2024年に37,867人（男性24,720人、女性13,147人）が死亡した。2018年に診断された例の5年相対生存率は66.1%だった。
    condition:
      region: 日本
      data: 全国がん登録・人口動態統計
    differential: 食道癌（2023年罹患25,889例）
    common_misconception: 胃癌の罹患数は日本で増え続けている
  provenance:
    source_ref: SRC-036
    source: 国立がん研究センター がん情報サービス 胃（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新）
    doi: null
    pmid: null
    pmcid: null
    url: https://ganjoho.jp/reg_stat/statistics/stat/cancer/5_stomach.html
    source_license: 元データは政府統計。サイト利用規約は要確認
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-034
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 市町村の対策型胃がん検診は、50歳以上を対象に、胃部エックス線検査または胃内視鏡検査のいずれかを2年に1回行う。胃部エックス線検査は当分の間、40歳代にも実施でき、年1回の実施も可能とされている。
    condition:
      region: 日本
      rule: 2016年2月の指針改正で対象年齢の引き上げと内視鏡検査の導入
    differential: 大腸がん検診は40歳以上で便潜血検査を年1回
    common_misconception: 対策型胃がん検診の内視鏡検査は40歳以上・毎年である
  provenance:
    source_ref: SRC-037
    source: 厚生労働省『がん予防重点健康教育及びがん検診実施のための指針』（平成28年2月改正）／厚労省がん検診ページ
    doi: null
    pmid: null
    pmcid: null
    url: https://www.gankenshin50.mhlw.go.jp/campaign_2023/screening/index.html
    source_license: 政府標準利用規約（原文は要確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-035
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 胃癌のN分類は、所属リンパ節の転移個数で決まる。N1は1〜2個、N2は3〜6個、N3aは7〜15個、N3bは16個以上である。
    condition:
      classification: 胃癌取扱い規約第15版＝UICC TNM第8版
    differential: No.13リンパ節は通常M1だが、十二指腸浸潤例では所属リンパ節として扱う
    common_misconception: N分類は転移したリンパ節の部位で決まる
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-036
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 内視鏡治療の適応判断では、乳頭腺癌と高・中分化管状腺癌を分化型、低分化腺癌と印環細胞癌を未分化型とする。両者が混在する場合は量的に優勢な組織型で分類する。粘膜下層に粘液癌がある場合は未分化型として扱う。
    condition:
      guideline: JGCA 第7版
    differential: 潰瘍所見（UL）は生検瘢痕と区別が難しい場合、UL1とする
    common_misconception: 印環細胞癌は分化型に含まれる
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-037
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 早期胃癌の内視鏡切除の絶対適応は次のとおりである。EMRまたはESDの絶対適応は、潰瘍所見のない（UL0）cT1aの分化型で長径2 cm以下のもの。ESDの絶対適応は、UL0のcT1a分化型で2 cmを超えるもの、潰瘍所見のある（UL1）cT1a分化型で3 cm以下のもの、UL0のcT1a未分化型で2 cm以下のものである。
    condition:
      guideline: JGCA 第6版・第7版で同一
    differential: 絶対適応はリンパ節転移の可能性が1%未満で外科切除と同等の効果が期待できるもの
    common_misconception: 未分化型は大きさにかかわらず内視鏡切除の適応外
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-038
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 内視鏡切除の適応拡大病変は、絶対適応の分化型病変を初回切除してeCuraC-1となり、その後に局所再発したcT1aの病変である。絶対適応・適応拡大のいずれにも当たらない病変でも、高齢や重い併存疾患で手術が勧められない場合は、リンパ節転移の残存リスクを説明したうえで相対適応として内視鏡切除を選べる。
    condition:
      guideline: JGCA 第7版
    differential: 相対適応の標準治療は外科切除
    common_misconception: 高齢者には絶対適応外の病変でも常に内視鏡切除が標準
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-039
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 第7版では、一括切除・HM0・VM0・Ly0・V0を前提に、UL0のpT1aで分化型優位なら大きさを問わず、未分化型優位なら2 cm以下の場合をeCuraAとする。UL1のpT1a分化型優位で3 cm以下も、分化型優位で3 cm以下のpT1b1（SM1、粘膜筋板から500 µm未満）もeCuraAとなる。
    condition:
      guideline: JGCA 第7版（第6版ではSM1病変はeCuraBだった）
    differential: 未分化成分が2 cmを超える場合や、SM浸潤部に未分化成分がある場合はeCuraC-2
    common_misconception: SM浸潤があれば常に非治癒切除
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 第6版からの分類変更点。第7版本文で確認済みだが、教材では版を明記すること
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-040
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: eCuraC-1は、分化型で、分割切除または水平断端陽性であることを除けばeCuraAまたはBの条件を満たすものである。それ以外のeCuraCはeCuraC-2とする。eCuraC-1では再ESD、外科切除、焼灼効果を期待した厳重経過観察、レーザーやAPCによる焼灼から選べる。eCuraC-2ではリンパ節郭清を伴う胃切除が標準となる。
    condition:
      guideline: JGCA 第7版
    differential: 第7版のeCuraBは、適応拡大病変（局所再発）の切除で条件を満たすもの
    common_misconception: eCuraC-1は全例で追加外科切除が必要
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-041
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: eCuraAの切除後は年1回の内視鏡で経過を観察する。eCuraA・Bのいずれでも、H. pyloriを検査して陽性なら除菌することが推奨される。異時性胃癌のリスクは長く続くため、長期の経過観察が必要である。
    condition:
      guideline: JGCA 第7版
    differential: eCuraBでは年1〜2回の内視鏡に加え腹部超音波またはCTで転移を検索する
    common_misconception: 除菌すれば内視鏡の経過観察は不要
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-042
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 定型胃切除は、胃の3分の2以上の切除とD2リンパ節郭清を行う手術である。D2郭清はcT2〜T4とcT1N+の根治切除可能例に、D1またはD1+郭清はcT1N0に適応する。cT1aで内視鏡切除の適応外のものと、分化型で1.5 cm以下のcT1bN0にはD1郭清を行う。
    condition:
      guideline: JGCA 第7版
    differential: 術前・術中の深達度とリンパ節の診断は不確実なため、転移を否定できなければD2を行う
    common_misconception: 早期胃癌でも全例D2郭清が必要
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-043
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 根治切除の口側断端距離は、T2以深では限局型（1型・2型）で3 cm以上、浸潤型（3型・4型）で5 cm以上を確保する。T1では肉眼で2 cmの断端を確保する。確保できない場合は断端の術中迅速診断を行う。
    condition:
      guideline: JGCA 第7版
    differential: 食道浸潤例では5 cm超は必須ではなく、迅速診断でR0を確認する
    common_misconception: 断端距離は肉眼型に関係なく一律
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-044
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 大彎に浸潤しない胃上部の進行癌に対する胃全摘では、脾臓を温存することが強く推奨されている（エビデンスA）。大彎浸潤例では脾摘または脾門リンパ節郭清が弱く推奨されている。
    condition:
      guideline: JGCA 第6版 CQ7（JCOG0110）
    differential: 膵浸潤で膵脾合併切除が必要な場合は部位にかかわらず胃全摘
    common_misconception: 胃上部の進行癌では脾摘を標準とする
  provenance:
    source_ref: SRC-029
    source: Japanese Gastric Cancer Association. Japanese Gastric Cancer Treatment Guidelines 2021 (6th edition). Gastric Cancer 2023;26:1-25
    doi: 10.1007/s10120-022-01331-8
    pmid: null
    pmcid: PMC9813208
    url: https://link.springer.com/article/10.1007/s10120-022-01331-8
    source_license: Open access, © 2022 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-045
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 肝転移や腹膜転移など非治癒因子があり、出血・狭窄などの症状がない患者に腫瘍量を減らす目的で行う減量手術は、国際共同RCT（REGATTA、JCOG0705/KGCA01）で生存上の利益が示されなかった。化学療法が可能な患者には行わないよう勧められている。
    condition:
      guideline: JGCA 第7版
    differential: 出血や狭窄に対する姑息手術、化学療法奏効後のconversion surgeryは別の概念
    common_misconception: 切除できる非治癒胃癌は原発巣を切除した方が生存が延びる
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-046
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 第7版は、腹腔鏡下幽門側胃切除をStageⅡ以上の進行癌も含めて標準治療の一つとして強く推奨している（エビデンスA）。cStageⅠに対する腹腔鏡下胃全摘・噴門側胃切除も強く推奨され、進行癌に対する腹腔鏡下胃全摘とロボット支援胃切除は弱く推奨されている。
    condition:
      guideline: JGCA 第7版 CQ1-1〜1-3（第6版ではcStageⅡ/Ⅲは推奨なし）
    differential: 根拠：JCOG0912、KLASS-01、KLASS-02、CLASS-01、JLSSG0901
    common_misconception: 腹腔鏡手術は早期胃癌に限られる
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-047
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: cT1N0の胃中部の癌で、腫瘍の遠位端が幽門から4 cm以上離れている場合は、幽門保存胃切除が選択肢となる（弱い推奨）。
    condition:
      guideline: JGCA 第7版 CQ2-1
    differential: 胃上部の早期癌には噴門側胃切除、胃上部でわずかでも胃を残せる場合は亜全摘
    common_misconception: 幽門保存胃切除は進行癌にも適応
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-048
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 食道胃接合部癌（腫瘍中心が接合部の上下2 cm以内）のcT2以深では、食道浸潤長に応じて郭清範囲を決める。浸潤長が2 cmを超えれば下縦隔の、4 cmを超えれば上・中・下縦隔のリンパ節郭清が弱く推奨されている。浸潤長4 cm以下なら経裂孔的腹部アプローチを選べる。
    condition:
      guideline: JGCA 第6版 CQ12（日本胃癌学会・日本食道学会の前向き研究に基づく）
    differential: 組織型は腺癌でも扁平上皮癌でもよい
    common_misconception: 食道胃接合部癌は常に開胸手術が必要
  provenance:
    source_ref: SRC-029
    source: Japanese Gastric Cancer Association. Japanese Gastric Cancer Treatment Guidelines 2021 (6th edition). Gastric Cancer 2023;26:1-25
    doi: 10.1007/s10120-022-01331-8
    pmid: null
    pmcid: PMC9813208
    url: https://link.springer.com/article/10.1007/s10120-022-01331-8
    source_license: Open access, © 2022 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-049
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: pStageⅡ胃癌には、術後補助化学療法としてS-1の1年間投与が推奨される。JCOG1104試験では、S-1を1年間投与した群の3年無再発生存率は93.1%、3年全生存率は96.1%だった。
    condition:
      guideline: JGCA 第7版
    differential: pStageⅢでは併用療法が推奨される
    common_misconception: pStageⅡにもドセタキセル併用が標準
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値はGL本文の引用値。JCOG1104原著は未照合
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-050
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: pStageⅢ胃癌の術後補助化学療法には、S-1＋ドセタキセル、CapeOX、SOXなどの併用療法が推奨され、S-1単独は条件付き推奨となる。併用療法どうしの直接比較はない。ATTRACTION-5試験では、術後補助化学療法へのニボルマブ追加の効果は認められなかった。
    condition:
      guideline: JGCA 第7版（根拠：JACCRO GC-07、CLASSIC、ARTIST2）
    differential: 食道癌の術後ニボルマブ（CheckMate 577）とは対象が異なる
    common_misconception: 胃癌の術後補助療法にも免疫チェックポイント阻害薬が標準
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-051
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 切除可能な進行胃癌に対する術前化学療法は、欧米や中国・韓国のRCTで有効性が報告されているが、日本では日常診療への導入について合意が得られていない。高度リンパ節転移（bulky N）に対するS-1＋シスプラチンの術前化学療法は暫定的な標準治療とされる。4型・大型3型胃癌では、JCOG0501で術前S-1＋シスプラチンの優越性は示されなかった。
    condition:
      region: 日本 vs 欧米
      guideline: JGCA 第7版 CQ16-1
    differential: 欧米では周術期化学療法（FLOT など）が標準
    common_misconception: 日本でも切除可能進行胃癌の全例に術前化学療法を行う
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-052
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 切除不能進行・再発胃癌では、一次化学療法の開始前にHER2、CLDN18、PD-L1（CPS）、MSI/MMRの4つのバイオマーカーを測定し、結果に基づいて治療を選ぶことが望ましいとされる。
    condition:
      guideline: JGCA 第7版 CQ13-1（日本胃癌学会のバイオマーカー検査の手引き第1.1版に対応）
    differential: 第6版で一次治療前に必須とされたのはHER2のみ
    common_misconception: 一次治療前に調べればよいのはHER2だけである
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-02-07-030 (id: JlAKplE)；TBL-02-07-031 (id: JlAKplI)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-053
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: HER2陽性は、免疫染色3+、または免疫染色2+かつISH陽性で定義され、切除不能進行・再発胃癌の17.8%を占めると報告されている。HER2陽性例にはトラスツズマブをフッ化ピリミジン＋プラチナ製剤と併用する。
    condition:
      guideline: JGCA 第7版（根拠：ToGA試験のサブグループ解析）
    differential: 免疫染色2+でISH陰性はHER2陰性として扱う
    common_misconception: 免疫染色1+でもトラスツズマブの適応になる
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-02-07-030 (id: JlAKplE)；TBL-02-07-031 (id: JlAKplI)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-054
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: HER2陰性の切除不能進行・再発胃癌の一次治療では、化学療法とニボルマブまたはペムブロリズマブの併用、CLDN18陽性例では化学療法とゾルベツキシマブの併用が推奨される。プラチナ製剤はシスプラチンよりオキサリプラチンを用いる併用が好ましいとされる。CLDN18陰性でCPSが低い例では化学療法単独も考慮する。
    condition:
      guideline: JGCA 第7版
    differential: 免疫チェックポイント阻害薬とゾルベツキシマブを直接比較した研究はない
    common_misconception: CPSが低くても免疫チェックポイント阻害薬の上乗せ効果は高CPSと同じ
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-055
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: CheckMate 649試験では、未治療の切除不能なHER2陽性でない胃癌・食道胃接合部癌・食道腺癌に対し、ニボルマブ＋化学療法が化学療法単独より全生存と無増悪生存を改善した。主要評価項目はPD-L1 CPS 5以上の集団で設定された。
    condition:
      region: 国際（29か国175施設）
    differential: ATTRACTION-4（アジア、SOXまたはCapeOX＋ニボルマブ）
    common_misconception: PD-L1発現にかかわらず効果の大きさは同じ
  provenance:
    source_ref: SRC-034
    source: Janjigian YY, et al. CheckMate 649. Lancet 2021;398:27-40
    doi: 10.1016/S0140-6736(21)00797-2
    pmid: '34102137'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/34102137/
    source_license: 非CC（Elsevier）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 生存期間の数値は抄録全文を未照合のため主張文に含めない
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-056
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: SPOTLIGHT試験では、CLDN18.2陽性・HER2陰性の未治療切除不能胃癌・食道胃接合部腺癌に対し、ゾルベツキシマブ＋mFOLFOX6が無増悪生存期間の中央値を10.61か月とし、プラセボ＋mFOLFOX6の8.67か月より延長した。
    condition:
      region: 国際（20か国215施設、565例）
    differential: GLOW試験はCapeOXとの併用
    common_misconception: ゾルベツキシマブはHER2陽性胃癌に使う
  provenance:
    source_ref: SRC-035
    source: Shitara K, et al. SPOTLIGHT. Lancet 2023;401:1655-1668
    doi: 10.1016/S0140-6736(23)00620-7
    pmid: '37068504'
    pmcid: null
    url: https://clinicaltrials.gov/study/NCT03504397
    source_license: 非CC（Elsevier）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 全生存（18.23か月対15.54か月）は企業発表など二次資料経由のため主張文に含めない
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-057
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 日本では2024年3月26日、ゾルベツキシマブがCLDN18.2陽性の治癒切除不能な進行・再発の胃癌を効能・効果として承認された。抗CLDN18.2抗体の承認は世界で初めてだった。
    condition:
      region: 日本
      date: '2024-03-26'
    differential: 欧州承認は2024年9月
    common_misconception: ゾルベツキシマブは単剤で使う
  provenance:
    source_ref: SRC-038
    source: アステラス製薬 適時開示（2024-07-29）：ゾルベツキシマブ 欧州CHMP販売承認勧告（国内承認日の記載あり）
    doi: null
    pmid: null
    pmcid: null
    url: https://www2.jpx.co.jp/disc/45030/140120240729556149.pdf
    source_license: 企業資料（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: PMDA添付文書の改訂履歴では未照合
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-058
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 切除不能進行・再発胃癌の二次治療では、パクリタキセル＋ラムシルマブが推奨レジメンである。MSI-Highは進行・再発胃癌の約3〜5%で、一次治療で免疫チェックポイント阻害薬を使っていない場合に限り、二次治療としてペムブロリズマブ単剤が推奨される。
    condition:
      guideline: JGCA 第7版（根拠：RAINBOW、KEYNOTE-158）
    differential: パクリタキセル＋ラムシルマブが不適なら単剤（パクリタキセル、nab-パクリタキセル、ドセタキセル、イリノテカン、ラムシルマブ）
    common_misconception: 一次治療でニボルマブを使っていても二次治療でペムブロリズマブを使える
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-059
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 三次治療以降では、ニボルマブ、イリノテカン、トリフルリジン・チピラシルの単剤が推奨され、互いの優先順位は明らかでない。ニボルマブは免疫チェックポイント阻害薬の使用歴がない場合に限られる。HER2陽性胃癌の三次治療ではトラスツズマブ デルクステカンが優先される。病勢進行後のトラスツズマブ継続は行わないよう強く推奨されている。
    condition:
      guideline: JGCA 第7版（根拠：ATTRACTION-2、TAGS、DESTINY-Gastric01、WJOG7112G）
    differential: 二次治療のHER2陽性例はHER2陰性と同じレジメン
    common_misconception: HER2陽性例では進行後もトラスツズマブを継続する
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-060
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 切除不能進行・再発胃癌に対する国内外の臨床試験での生存期間中央値は、およそ17〜18か月である。化学療法の目的は、症状の出現を遅らせることと生存の延長である。
    condition:
      guideline: JGCA 第7版（第6版では約15か月）
    differential: MSI-HighやHER2陽性では著効によりconversion surgeryに至る例がある
    common_misconception: 化学療法で多くの切除不能胃癌が治癒する
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-061
  domain: GD
  subdomain: 胃癌
  assertion:
    plain_statement_ja: 胃癌の根治切除後は原則5年間経過を観察する。CT、腫瘍マーカー（CEAとCA19-9）、内視鏡が再発や重複癌の発見に有用と考えられ、腫瘍マーカーは画像所見より2〜3か月早く上昇することがある。ただし定期的な経過観察が生存を延ばすというエビデンスは乏しい。
    condition:
      guideline: JGCA 第7版
    differential: 5年以降にも再発や異時性多発癌がみられる
    common_misconception: 定期フォローで生存率が改善することが証明されている
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-D-②（胃癌、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-062
  domain: GD
  subdomain: GIST・粘膜下腫瘍
  assertion:
    plain_statement_ja: 粘膜下腫瘍が疑われたら内視鏡下生検で上皮性腫瘍を除外する。2 cm未満で半球状・表面平滑・潰瘍や陥凹のないものは年1〜2回経過を観察する。2 cm以上5 cm未満、または不整な辺縁・潰瘍・増大がある場合はCT、EUS、EUS-FNAで精査する。5.1 cm以上、有症状、または生検でGISTと診断された場合は手術を検討する。
    condition:
      region: 日本
      guideline: JSCO GIST GL 2022
    differential: 漿膜側からの生検は禁止
    common_misconception: 2 cm未満の粘膜下腫瘍は全例切除する
  provenance:
    source_ref: SRC-032
    source: Hirota S, et al. English version of Japanese Clinical Practice Guidelines 2022 for gastrointestinal stromal tumor (GIST). Int J Clin Oncol 2024;29:647-680
    doi: 10.1007/s10147-024-02488-1
    pmid: '38609732'
    pmcid: PMC11130037
    url: https://link.springer.com/article/10.1007/s10147-024-02488-1
    source_license: Open access, © 2024 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-063
  domain: GD
  subdomain: GIST・粘膜下腫瘍
  assertion:
    plain_statement_ja: GISTの約95%は免疫染色でKIT陽性で、DOG1もGISTの大多数（約95%）で陽性となる。KIT陰性のGIST（最大5%）の多くは胃原発、類上皮型で、PDGFRA変異をもつ。CD34は60〜80%で陽性である。
    condition:
      guideline: JSCO GIST GL 2022
    differential: 平滑筋腫はデスミンがびまん性に陽性、神経鞘腫はS-100がびまん性に陽性
    common_misconception: KIT陰性ならGISTは否定できる
  provenance:
    source_ref: SRC-032
    source: Hirota S, et al. English version of Japanese Clinical Practice Guidelines 2022 for gastrointestinal stromal tumor (GIST). Int J Clin Oncol 2024;29:647-680
    doi: 10.1007/s10147-024-02488-1
    pmid: '38609732'
    pmcid: PMC11130037
    url: https://link.springer.com/article/10.1007/s10147-024-02488-1
    source_license: Open access, © 2024 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-064
  domain: GD
  subdomain: GIST・粘膜下腫瘍
  assertion:
    plain_statement_ja: GISTの70〜80%はc-kitエクソン11変異をもつ。c-kitエクソン9変異は5〜10%で主に小腸に、PDGFRA変異は約10%で主に胃の類上皮型にみられる。PDGFRAエクソン18のD842V変異、SDH欠損型、NF1関連のGISTは通常イマチニブに抵抗性である。
    condition:
      guideline: JSCO GIST GL 2022
    differential: c-kitとPDGFRAのどちらの変異もないGISTが約10%
    common_misconception: すべてのGISTにイマチニブが効く
  provenance:
    source_ref: SRC-032
    source: Hirota S, et al. English version of Japanese Clinical Practice Guidelines 2022 for gastrointestinal stromal tumor (GIST). Int J Clin Oncol 2024;29:647-680
    doi: 10.1007/s10147-024-02488-1
    pmid: '38609732'
    pmcid: PMC11130037
    url: https://link.springer.com/article/10.1007/s10147-024-02488-1
    source_license: Open access, © 2024 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-065
  domain: GD
  subdomain: GIST・粘膜下腫瘍
  assertion:
    plain_statement_ja: GISTの発生部位は胃が最も多く（50〜70%）、十二指腸・小腸（20〜30%）、大腸（5〜10%、多くは直腸）と続く。胃以外のGISTは胃GISTより再発リスクが高いとされる。
    condition:
      guideline: JSCO GIST GL 2022
    differential: 食道・腸間膜・大網はまれ
    common_misconception: GISTは小腸に最も多い
  provenance:
    source_ref: SRC-032
    source: Hirota S, et al. English version of Japanese Clinical Practice Guidelines 2022 for gastrointestinal stromal tumor (GIST). Int J Clin Oncol 2024;29:647-680
    doi: 10.1007/s10147-024-02488-1
    pmid: '38609732'
    pmcid: PMC11130037
    url: https://link.springer.com/article/10.1007/s10147-024-02488-1
    source_license: Open access, © 2024 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-066
  domain: GD
  subdomain: GIST・粘膜下腫瘍
  assertion:
    plain_statement_ja: GISTの再発リスクは、腫瘍径と核分裂像数を組み合わせて超低・低・中・高リスクに分類する。Miettinen分類は部位を、modified Fletcher（Joensuu）分類はさらに腫瘍破裂を加える。核分裂像は顕微鏡の視野数によらず5 mm²あたりで数えることが推奨される。
    condition:
      guideline: JSCO GIST GL 2022
    differential: SDH欠損型GISTは従来の分類で転移を予測しにくい
    common_misconception: GISTは良性か悪性かに二分できる
  provenance:
    source_ref: SRC-032
    source: Hirota S, et al. English version of Japanese Clinical Practice Guidelines 2022 for gastrointestinal stromal tumor (GIST). Int J Clin Oncol 2024;29:647-680
    doi: 10.1007/s10147-024-02488-1
    pmid: '38609732'
    pmcid: PMC11130037
    url: https://link.springer.com/article/10.1007/s10147-024-02488-1
    source_license: Open access, © 2024 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-067
  domain: GD
  subdomain: GIST・粘膜下腫瘍
  assertion:
    plain_statement_ja: 切除可能な限局性GISTの標準術式は、系統的リンパ節郭清を行わない局所切除である。腫瘍破裂を避けて完全切除することが重要で、臓器機能温存手術が強く推奨されている。10 cm以上の大きな腫瘍などには術前イマチニブが提案され、術前・術中に破裂した例では術後イマチニブが推奨される。
    condition:
      guideline: JSCO GIST GL 2022
    differential: 胃癌の定型手術（D2郭清）とは異なる
    common_misconception: GISTの手術では胃癌と同様にリンパ節郭清が必要
  provenance:
    source_ref: SRC-032
    source: Hirota S, et al. English version of Japanese Clinical Practice Guidelines 2022 for gastrointestinal stromal tumor (GIST). Int J Clin Oncol 2024;29:647-680
    doi: 10.1007/s10147-024-02488-1
    pmid: '38609732'
    pmcid: PMC11130037
    url: https://link.springer.com/article/10.1007/s10147-024-02488-1
    source_license: Open access, © 2024 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-068
  domain: GD
  subdomain: GIST・粘膜下腫瘍
  assertion:
    plain_statement_ja: 5 cm以上の粘膜下腫瘍に腹腔鏡手術を行うことが弱く推奨されている（エビデンスD）。ただし根拠となったメタ解析では8 cmを超える腫瘍に開腹手術が多く選ばれており、非常に大きな腫瘍への腹腔鏡手術は推奨されない。
    condition:
      guideline: JSCO GIST GL 2022 Surgery 3（CQ）
    differential: 2〜5 cmでGISTまたは悪性が強く疑われる粘膜下腫瘍は手術が強く推奨される
    common_misconception: 大きさにかかわらず腹腔鏡手術が標準
  provenance:
    source_ref: SRC-032
    source: Hirota S, et al. English version of Japanese Clinical Practice Guidelines 2022 for gastrointestinal stromal tumor (GIST). Int J Clin Oncol 2024;29:647-680
    doi: 10.1007/s10147-024-02488-1
    pmid: '38609732'
    pmcid: PMC11130037
    url: https://link.springer.com/article/10.1007/s10147-024-02488-1
    source_license: Open access, © 2024 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-069
  domain: GD
  subdomain: GIST・粘膜下腫瘍
  assertion:
    plain_statement_ja: 再発高リスクGISTの完全切除後のイマチニブ補助療法は、3年間投与が1年間投与より生存を延長した。中央判定でGISTと確認され肉眼的転移のない集団の5年生存率は93.4%対86.8%（HR 0.53）だった。
    condition:
      population: modified NIH基準で高リスク、KIT陽性、肉眼的完全切除（SSG XVIII/AIO）
    differential: 低・中リスクGISTでは補助療法の有効性は確立していない
    common_misconception: 補助イマチニブは1年で十分
  provenance:
    source_ref: SRC-033
    source: 'Joensuu H, et al. Adjuvant imatinib for high-risk GI stromal tumor: analysis of a randomized trial. J Clin Oncol 2016;34:244-250'
    doi: 10.1200/JCO.2015.62.9170
    pmid: '26527782'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/26527782/
    source_license: 非CC（ASCO）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-070
  domain: GD
  subdomain: GIST・粘膜下腫瘍
  assertion:
    plain_statement_ja: 転移・再発GISTの初回治療の原則はイマチニブ投与である。薬物療法の効果判定では、腫瘍径10%以上の縮小またはCT値15%以上の低下を部分奏効とする修正基準（Choi基準）が用いられる。
    condition:
      guideline: JSCO GIST GL 2022
    differential: RECISTは腫瘍径のみで判定し、嚢胞化などの内部変化を反映しにくい
    common_misconception: GISTは腫瘍が縮小しなければ効いていない
  provenance:
    source_ref: SRC-032
    source: Hirota S, et al. English version of Japanese Clinical Practice Guidelines 2022 for gastrointestinal stromal tumor (GIST). Int J Clin Oncol 2024;29:647-680
    doi: 10.1007/s10147-024-02488-1
    pmid: '38609732'
    pmcid: PMC11130037
    url: https://link.springer.com/article/10.1007/s10147-024-02488-1
    source_license: Open access, © 2024 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-071
  domain: GD
  subdomain: 胃神経内分泌腫瘍
  assertion:
    plain_statement_ja: 胃神経内分泌腫瘍（NET）は背景病態で型が分かれる。自己免疫性の胃底腺萎縮による高ガストリン血症を背景とするものがI型、Zollinger-Ellison症候群（多くはMEN1）を背景とするものがII型である。
    condition:
      guideline: ENETS 2023（II型は同ガイダンスの対象外）
    differential: III型は高ガストリン血症を伴わない散発性
    common_misconception: 胃NETはすべて同じ予後である
  provenance:
    source_ref: SRC-039
    source: Panzuto F, et al. ENETS 2023 guidance paper for gastroduodenal neuroendocrine tumours (NETs) G1-G3. J Neuroendocrinol 2023;35:e13306
    doi: 10.1111/jne.13306
    pmid: null
    pmcid: null
    url: https://doi.org/10.1111/jne.13306
    source_license: Open access, © 2023 The Authors（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文未閲覧。抄録とPDF断片で確認した型の定義のみを記載。III型の記述は本文で要確認
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-5-B-④（消化管神経内分泌腫瘍、c）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-072
  domain: GD
  subdomain: 胃静脈瘤
  assertion:
    plain_statement_ja: 日本の内視鏡所見記載基準では、胃静脈瘤の占居部位を、噴門部に限局するLg-c、噴門部から胃穹窿部に連なるLg-cf、胃穹窿部に限局するLg-fなどに分けて記載する。
    condition:
      region: 日本
      rule: 門脈圧亢進症取扱い規約 第3版
    differential: 食道静脈瘤はLs・Lm・Li（ES側）
    common_misconception: 胃静脈瘤もF・RCだけで記載すればよい
  provenance:
    source_ref: SRC-017
    source: 日本門脈圧亢進症学会 門脈圧亢進症取扱い規約 第3版の内視鏡所見記載基準（日消誌116(5):395で確認）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/nisshoshi/116/5/116_395/_pdf
    source_license: 非CC
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ES-R17（ES側）から胃静脈瘤の部位分類を移管。部位名の和文表記は原典で要確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-1-D-①（食道静脈瘤、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-073
  domain: GD
  subdomain: 胃静脈瘤
  assertion:
    plain_statement_ja: 日本の肝硬変診療ガイドライン2020では、胃静脈瘤に対してB-RTOが有用とされ、国内研究ではNBCAを用いた内視鏡的硬化療法より再出血の予防に優れていた。
    condition:
      region: 日本
      guideline: JSGE 肝硬変 GL 2020
    differential: 欧米ではシアノアクリレートやTIPSが中心
    common_misconception: 胃静脈瘤にもEVLが第一選択
  provenance:
    source_ref: SRC-018
    source: Yoshiji H, et al. Evidence-based clinical practice guidelines for Liver Cirrhosis 2020. J Gastroenterol 2021;56:593-619
    doi: 10.1007/s00535-021-01788-x
    pmid: null
    pmcid: PMC8280040
    url: https://link.springer.com/article/10.1007/s00535-021-01788-x
    source_license: Springer OA（CC種別は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ES-R18（ES側）からB-RTOの記載を移管。2025年版の推奨は未確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-034 (id: JlAKplU)'
    kokushi: 医学各論 Ⅵ-1-D-①（食道静脈瘤、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-074
  domain: GD
  subdomain: 胃切除後症候群
  assertion:
    plain_statement_ja: 早期ダンピング症候群は食後1時間以内に起こる。腹痛、腹部膨満、腹鳴、悪心、下痢などの消化器症状と、顔面紅潮、動悸、頻脈、まれに失神などの血管運動症状が出る。幽門の機能や胃の貯留能が失われ、未消化の高浸透圧の内容物が急速に小腸へ流入し、血漿から腸管内への水分移動や消化管ホルモンの放出が起こることが原因とされる。
    condition:
      guideline: 国際コンセンサス 2020
    differential: 後期ダンピング（食後1〜3時間の低血糖）
    common_misconception: 早期ダンピングの主因は低血糖である
  provenance:
    source_ref: SRC-040
    source: Scarpellini E, et al. International consensus on the diagnosis and management of dumping syndrome. Nat Rev Endocrinol 2020;16:448-466
    doi: 10.1038/s41574-020-0357-5
    pmid: null
    pmcid: PMC7351708
    url: https://www.nature.com/articles/s41574-020-0357-5
    source_license: CC BY 4.0（出版社ページで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-②（胃切除後症候群、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-075
  domain: GD
  subdomain: 胃切除後症候群
  assertion:
    plain_statement_ja: 後期ダンピング症候群は通常食後1〜3時間に起こり、反応性の低血糖を特徴とする。糖の急速な吸収に対する過剰なインスリン分泌が原因で、GLP-1の過剰な反応が主要な仲介因子と考えられている。
    condition:
      guideline: 国際コンセンサス 2020
    differential: 早期ダンピング（食後1時間以内の消化器・血管運動症状）
    common_misconception: 後期ダンピングは高血糖で起こる
  provenance:
    source_ref: SRC-040
    source: Scarpellini E, et al. International consensus on the diagnosis and management of dumping syndrome. Nat Rev Endocrinol 2020;16:448-466
    doi: 10.1038/s41574-020-0357-5
    pmid: null
    pmcid: PMC7351708
    url: https://www.nature.com/articles/s41574-020-0357-5
    source_license: CC BY 4.0（出版社ページで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-②（胃切除後症候群、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-076
  domain: GD
  subdomain: 胃切除後症候群
  assertion:
    plain_statement_ja: ダンピング症候群の頻度は、迷走神経切離＋幽門形成術後で約20%、胃切除後で最大40%、食道切除後で最大50%と報告されている。胃癌手術後には、後期ダンピング単独の症状が最大25%にみられるとされる。
    condition:
      guideline: 国際コンセンサス 2020
    differential: 肥満手術（RYGB、スリーブ状胃切除）後にも起こる
    common_misconception: ダンピング症候群は胃全摘でしか起こらない
  provenance:
    source_ref: SRC-040
    source: Scarpellini E, et al. International consensus on the diagnosis and management of dumping syndrome. Nat Rev Endocrinol 2020;16:448-466
    doi: 10.1038/s41574-020-0357-5
    pmid: null
    pmcid: PMC7351708
    url: https://www.nature.com/articles/s41574-020-0357-5
    source_license: CC BY 4.0（出版社ページで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 頻度はコンセンサス論文が引用した値（二次資料経由）で、原著は未照合
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-②（胃切除後症候群、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-077
  domain: GD
  subdomain: 胃切除後症候群
  assertion:
    plain_statement_ja: ダンピング症候群の診断には修正75 g経口ブドウ糖負荷試験が用いられる。30分でヘマトクリットが3%を超えて上昇するか脈拍が10回/分を超えて増加すれば早期ダンピング、60〜180分に血糖が50 mg/dL未満となれば後期ダンピングを示す。Sigstadスコアは7を超えるとダンピングを示唆するが、質問票や胃排出検査は診断法として推奨されていない。
    condition:
      guideline: 国際コンセンサス 2020
    differential: 血糖60 mg/dLの基準は採用されなかった
    common_misconception: 胃排出シンチグラフィで診断が確定する
  provenance:
    source_ref: SRC-040
    source: Scarpellini E, et al. International consensus on the diagnosis and management of dumping syndrome. Nat Rev Endocrinol 2020;16:448-466
    doi: 10.1038/s41574-020-0357-5
    pmid: null
    pmcid: PMC7351708
    url: https://www.nature.com/articles/s41574-020-0357-5
    source_license: CC BY 4.0（出版社ページで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-②（胃切除後症候群、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-078
  domain: GD
  subdomain: 胃切除後症候群
  assertion:
    plain_statement_ja: ダンピング症候群の第一選択は食事療法である。1回の食事量を減らし、水分は食後30分以上あけて摂り、吸収の速い炭水化物を避け、食物繊維と蛋白質の多い食品をよく噛んでゆっくり食べる。食後30分間横になる指導や、グアーガムなどの増粘剤は推奨されなかった。
    condition:
      guideline: 国際コンセンサス 2020
    differential: 薬物療法は食事療法で改善しない場合
    common_misconception: 食事中に水分を多く摂ると症状が和らぐ
  provenance:
    source_ref: SRC-040
    source: Scarpellini E, et al. International consensus on the diagnosis and management of dumping syndrome. Nat Rev Endocrinol 2020;16:448-466
    doi: 10.1038/s41574-020-0357-5
    pmid: null
    pmcid: PMC7351708
    url: https://www.nature.com/articles/s41574-020-0357-5
    source_license: CC BY 4.0（出版社ページで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-②（胃切除後症候群、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-079
  domain: GD
  subdomain: 胃切除後症候群
  assertion:
    plain_statement_ja: 食事療法で改善しないダンピング症候群では、後期ダンピングにα-グルコシダーゼ阻害薬のアカルボース（50〜100 mgを1日3回食事とともに）が有効とされ、主な副作用は放屁である。それでも改善しない場合はソマトスタチンアナログが選択される。再手術や膵切除、ジアゾキシドは推奨されていない。
    condition:
      guideline: 国際コンセンサス 2020
    differential: アカルボースの早期ダンピングへの効果は確立していない
    common_misconception: 難治例には再手術が標準
  provenance:
    source_ref: SRC-040
    source: Scarpellini E, et al. International consensus on the diagnosis and management of dumping syndrome. Nat Rev Endocrinol 2020;16:448-466
    doi: 10.1038/s41574-020-0357-5
    pmid: null
    pmcid: PMC7351708
    url: https://www.nature.com/articles/s41574-020-0357-5
    source_license: CC BY 4.0（出版社ページで確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: アカルボースの用量は海外の記載。国内の保険適用は未確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-B-②（胃切除後症候群、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-080
  domain: GD
  subdomain: 胃切除後症候群
  assertion:
    plain_statement_ja: 胃癌手術で迷走神経前幹の肝枝や後幹の腹腔枝を温存すると、術後の胆石形成、下痢、体重減少が減り、術後のQOL改善に寄与すると報告されている。
    condition:
      guideline: JGCA 第7版（本文の記述。CQとしての推奨度はない）
    differential: 幽門保存胃切除では幽門機能を温存する
    common_misconception: 胃切除後の胆石は迷走神経と無関係である
  provenance:
    source_ref: SRC-030
    source: Japanese Gastric Cancer Association. Japanese gastric cancer treatment guidelines 2025 (7th edition). Gastric Cancer 2026;29:271-299
    doi: 10.1007/s10120-025-01698-4
    pmid: null
    pmcid: null
    url: https://link.springer.com/article/10.1007/s10120-025-01698-4
    source_license: Open access, © 2026 The Author(s)（CC種別はCrossrefで要確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)'
    kokushi: 医学各論 Ⅵ-2-B-②（胃切除後症候群、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-081
  domain: GD
  subdomain: 胃アニサキス症
  assertion:
    plain_statement_ja: アニサキスの幼虫は長さ2〜3 cm、幅0.5〜1 mm程度の白い糸状で、サバ、アジ、サンマ、カツオ、イワシ、サケ、ヒラメ、マグロ、イカなどに寄生する。宿主の魚介類が死ぬと、幼虫は内臓から筋肉へ移動する。
    condition:
      region: 日本
    differential: 北海道ではシュードテラノーバ属による症例もある
    common_misconception: 新鮮な魚の刺身なら寄生虫の心配はない
  provenance:
    source_ref: SRC-041
    source: 厚生労働省『アニサキスによる食中毒を予防しましょう』
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000042953.html
    source_license: 厚労省ウェブサイト利用規約（政府標準利用規約準拠と想定、原文は要確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-⑤（胃アニサキス症、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-082
  domain: GD
  subdomain: 胃アニサキス症
  assertion:
    plain_statement_ja: アニサキス症は生の魚介類を食べてから1時間〜数日で発症する。多くは急性胃アニサキス症で、食後12時間以内に激しい心窩部痛、悪心、嘔吐が起こる。急性腸アニサキス症は十数時間以降に激しい下腹部痛を起こす。
    condition:
      region: 日本
    differential: 急性胃炎、消化性潰瘍、急性膵炎
    common_misconception: アニサキス症は下痢が主症状である
  provenance:
    source_ref: SRC-041
    source: 厚生労働省『アニサキスによる食中毒を予防しましょう』
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000042953.html
    source_license: 厚労省ウェブサイト利用規約（政府標準利用規約準拠と想定、原文は要確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-⑤（胃アニサキス症、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-083
  domain: GD
  subdomain: 胃アニサキス症
  assertion:
    plain_statement_ja: アニサキスによる食中毒の予防には、−20℃で24時間以上の冷凍、または70℃以上か60℃で1分の加熱が有効である。食酢、塩漬け、醤油、わさびでは幼虫は死なない。魚は新鮮なうちに内臓を取り除き、内臓を生で食べないことも予防になる。
    condition:
      region: 日本
    differential: 通常の料理での酢締めや味付けは予防にならない
    common_misconception: しめ鯖のように酢で締めればアニサキスは死ぬ
  provenance:
    source_ref: SRC-041
    source: 厚生労働省『アニサキスによる食中毒を予防しましょう』
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000042953.html
    source_license: 厚労省ウェブサイト利用規約（政府標準利用規約準拠と想定、原文は要確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-⑤（胃アニサキス症、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-084
  domain: GD
  subdomain: 胃アニサキス症
  assertion:
    plain_statement_ja: 2018〜2019年の日本のレセプトデータに基づく推計では、アニサキス症は年間平均約19,737件発生しており、食中毒として公式に報告された件数はその40分の1未満だった。
    condition:
      region: 日本
      period: 2018〜2019年
    differential: 公式の食中毒統計は実際の発生数を大きく下回る
    common_misconception: アニサキス症はまれな疾患である
  provenance:
    source_ref: SRC-042
    source: Sugiyama H, et al. Anisakiasis annual incidence and causative species, Japan, 2018-2019. Emerg Infect Dis 2022;28(10)
    doi: 10.3201/eid2810.220627
    pmid: null
    pmcid: PMC9514333
    url: https://wwwnc.cdc.gov/eid/article/28/10/22-0627_article
    source_license: CDC刊行誌。記事ページにパブリックドメインの明示はなく未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ライセンス（EIDはパブリックドメインとされることが多い）は記事ページで未確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-⑤（胃アニサキス症、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-085
  domain: GD
  subdomain: 胃アニサキス症
  assertion:
    plain_statement_ja: 同じ研究で同定された原因幼虫189匹のうち、Anisakis simplex sensu strictoが168匹（88.9%）と大多数を占め、Anisakis pegreffiiが10匹（5.3%）、Pseudoterranova azarasiが11匹（5.8%）だった。P. azarasiの患者は主に北海道からだった。
    condition:
      region: 日本
    differential: 抄録ではA. simplex s.s.を88.4%と記載
    common_misconception: 日本のアニサキス症の原因はすべて同一種である
  provenance:
    source_ref: SRC-042
    source: Sugiyama H, et al. Anisakiasis annual incidence and causative species, Japan, 2018-2019. Emerg Infect Dis 2022;28(10)
    doi: 10.3201/eid2810.220627
    pmid: null
    pmcid: PMC9514333
    url: https://wwwnc.cdc.gov/eid/article/28/10/22-0627_article
    source_license: CDC刊行誌。記事ページにパブリックドメインの明示はなく未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本文と抄録で割合の記載が異なる（88.9%と88.4%）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-⑤（胃アニサキス症、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-086
  domain: GD
  subdomain: 胃ポリープ
  assertion:
    plain_statement_ja: 胃底腺ポリープは最も多い胃ポリープの一つで、PPI使用者に多い（使用者23%対非使用者12%と報告）。散発性の胃底腺ポリープの悪性化はまれ（1%未満）だが、家族性大腸腺腫症では20〜100%に生じ、その25〜41%に異形成を伴う。
    condition:
      source: 2013年の総説
    differential: H. pylori未感染の胃にみられることが多い
    common_misconception: 胃底腺ポリープは前癌病変として全例切除する
  provenance:
    source_ref: SRC-043
    source: 'Islam RS, et al. Gastric polyps: a review on clinical, endoscopic, histopathologic features and management decisions. Gastroenterol Hepatol (N Y) 2013 Oct'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.gastroenterologyandhepatology.net/?p=1952
    source_license: © Millennium Medical Publishing（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は総説が引用した値（二次資料経由）で、原著は未照合。GD-028（PPI長期使用と胃底腺ポリープ）と関連
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-D-①（胃ポリープ、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-087
  domain: GD
  subdomain: 胃ポリープ
  assertion:
    plain_statement_ja: 過形成性ポリープは、H. pylori胃炎や萎縮性胃炎などの慢性胃炎を背景に生じ、H. pyloriが原因の場合は除菌後に約80%が退縮すると報告されている。異形成は1.9〜19%、腺癌は0.6〜2.1%にみられると報告されている。
    condition:
      source: 2013年の総説
    differential: 切除する大きさの基準は0.5 cm超から2 cm以上まで報告により異なる
    common_misconception: 過形成性ポリープは癌化しない
  provenance:
    source_ref: SRC-043
    source: 'Islam RS, et al. Gastric polyps: a review on clinical, endoscopic, histopathologic features and management decisions. Gastroenterol Hepatol (N Y) 2013 Oct'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.gastroenterologyandhepatology.net/?p=1952
    source_license: © Millennium Medical Publishing（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は総説が引用した値（二次資料経由）で、原著は未照合。日本のH. pylori GLでの位置づけは未確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-D-①（胃ポリープ、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-088
  domain: GD
  subdomain: 胃ポリープ
  assertion:
    plain_statement_ja: 胃腺腫は真の腫瘍で胃癌の前駆病変であり、完全切除が勧められる。2 cmを超え絨毛成分をもつものでは腫瘍化のリスクが高いと報告されている。
    condition:
      source: 2013年の総説（欧米の頻度は胃ポリープの6〜10%）
    differential: 過形成性ポリープ、胃底腺ポリープ
    common_misconception: 胃腺腫は経過観察だけでよい
  provenance:
    source_ref: SRC-043
    source: 'Islam RS, et al. Gastric polyps: a review on clinical, endoscopic, histopathologic features and management decisions. Gastroenterol Hepatol (N Y) 2013 Oct'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.gastroenterologyandhepatology.net/?p=1952
    source_license: © Millennium Medical Publishing（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本の胃腺腫の扱い（Ⅵ-2-D-③）は別途確認が必要
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-D-①（胃ポリープ、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-089
  domain: GD
  subdomain: 胃ポリープ
  assertion:
    plain_statement_ja: PPIやボノプラザン内服中にみられる胃粘膜の変化の多くは、休薬や中止を必要としない。ただし出血を伴う過形成性ポリープがある場合は、中止またはH2受容体拮抗薬への変更を検討する。
    condition:
      region: 日本
      source: 日本消化器内視鏡学会雑誌 2025 総説
    differential: 蜘蛛の巣様粘液で観察が妨げられる場合は休薬して再検査を検討
    common_misconception: PPIによる胃粘膜変化があれば必ず中止する
  provenance:
    source_ref: SRC-044
    source: 岩室雅也. 薬剤起因性胃粘膜病変の内視鏡診断. 日本消化器内視鏡学会雑誌 2025;67(4):281-288
    doi: 10.11280/gee.67.281
    pmid: null
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/gee/67/4/67_281/_html/-char/ja
    source_license: © 日本消化器内視鏡学会（J-STAGE無料公開、非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-D-①（胃ポリープ、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-090
  domain: GD
  subdomain: 急性胃粘膜病変
  assertion:
    plain_statement_ja: NSAIDによる胃粘膜傷害は、前庭部から幽門部の潰瘍、びらん、出血として現れることが多い。対策として、最低有効量を最短期間で使い、H. pyloriを確認して必要なら除菌し、PPIの併用や選択的COX-2阻害薬への変更を検討する。
    condition:
      region: 日本
      source: 日本消化器内視鏡学会雑誌 2025 総説
    differential: H. pylori感染はNSAID起因性傷害のリスクを高める
    common_misconception: NSAID潰瘍は胃体部に多い
  provenance:
    source_ref: SRC-044
    source: 岩室雅也. 薬剤起因性胃粘膜病変の内視鏡診断. 日本消化器内視鏡学会雑誌 2025;67(4):281-288
    doi: 10.11280/gee.67.281
    pmid: null
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/gee/67/4/67_281/_html/-char/ja
    source_license: © 日本消化器内視鏡学会（J-STAGE無料公開、非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-①（急性胃炎、急性胃粘膜病変、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-091
  domain: GD
  subdomain: 急性胃粘膜病変
  assertion:
    plain_statement_ja: 酢酸亜鉛の内服では、胃体部に白苔を伴うびらんと周囲の発赤を生じることがあり、吐血の報告もある。
    condition:
      region: 日本
      source: 日本消化器内視鏡学会雑誌 2025 総説
    differential: NSAIDによる傷害は前庭部〜幽門部に多い
    common_misconception: 薬剤性の胃粘膜傷害の原因はNSAIDだけである
  provenance:
    source_ref: SRC-044
    source: 岩室雅也. 薬剤起因性胃粘膜病変の内視鏡診断. 日本消化器内視鏡学会雑誌 2025;67(4):281-288
    doi: 10.11280/gee.67.281
    pmid: null
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/gee/67/4/67_281/_html/-char/ja
    source_license: © 日本消化器内視鏡学会（J-STAGE無料公開、非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-①（急性胃炎、急性胃粘膜病変、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-092
  domain: GD
  subdomain: 急性胃粘膜病変
  assertion:
    plain_statement_ja: 人工呼吸管理中の重症患者を対象としたRCT（REVISE）で、パントプラゾール40 mg静注の予防投与は、プラセボに比べて臨床的に重要な上部消化管出血を減らしたが、90日死亡率には差がなかった。
    condition:
      population: 侵襲的人工呼吸管理中の成人ICU患者
      region: 国際
    differential: ストレス潰瘍は重症患者に生じる急性の胃粘膜病変
    common_misconception: 重症患者へのPPI予防投与で死亡率が下がる
  provenance:
    source_ref: SRC-045
    source: Cook D, et al. Stress ulcer prophylaxis during invasive mechanical ventilation (REVISE). N Engl J Med 2024
    doi: 10.1056/NEJMoa2404245
    pmid: null
    pmcid: null
    url: https://www.nejm.org/doi/full/10.1056/NEJMoa2404245
    source_license: 非CC（NEJM）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値（出血1.0%対3.5%、HR 0.30；90日死亡29.1%対30.9%、HR 0.94、解析4,821例）は二次資料（ACP Journal Club、The Bottom Line）経由のため主張文に含めない。巻・頁とPMIDは未確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-2-C-①（急性胃炎、急性胃粘膜病変、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-093
  domain: GD
  subdomain: 胃・十二指腸憩室
  assertion:
    plain_statement_ja: 十二指腸憩室の頻度は、上部消化管造影で1〜6%、内視鏡で12〜27%、剖検で15〜22%と報告され、年齢とともに増える。約70〜75%は乳頭周囲にあり、大多数は無症状である。
    condition:
      source: 2011年の症例報告と文献レビュー
    differential: 小腸憩室は空腸に最も多く、十二指腸が次ぐ
    common_misconception: 十二指腸憩室は見つかれば切除する
  provenance:
    source_ref: SRC-046
    source: 'Rizwan MM, et al. Duodenal diverticulum and associated pancreatitis: case report with brief review of literature. World J Gastrointest Endosc 2011;3(3):62-63'
    doi: 10.4253/wjge.v3.i3.62
    pmid: '21455344'
    pmcid: null
    url: https://www.wjgnet.com/1948-5190/full/v3/i3/62.htm
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はレビューが引用した値（二次資料経由）で、原著は未照合
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-5-D-①（食道憩室、胃憩室、十二指腸憩室など、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-094
  domain: GD
  subdomain: 胃・十二指腸憩室
  assertion:
    plain_statement_ja: 十二指腸憩室の合併症には、炎症、出血、穿孔、膵炎などがある。無症状やわずかな症状の憩室に対する待機的手術は正当化されず、外科的・内視鏡的治療は症状のある憩室に限られる。十二指腸憩室穿孔45例の報告では、全体の死亡率は31%だった。
    condition:
      source: 2011年の症例報告と文献レビュー
    differential: 膵炎との関連は胆石の合併も多く、因果関係は確定していない
    common_misconception: 漠然とした腹痛に憩室切除は有効である
  provenance:
    source_ref: SRC-046
    source: 'Rizwan MM, et al. Duodenal diverticulum and associated pancreatitis: case report with brief review of literature. World J Gastrointest Endosc 2011;3(3):62-63'
    doi: 10.4253/wjge.v3.i3.62
    pmid: '21455344'
    pmcid: null
    url: https://www.wjgnet.com/1948-5190/full/v3/i3/62.htm
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 死亡率は引用された症例集積の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-5-D-①（食道憩室、胃憩室、十二指腸憩室など、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
- id: GD-095
  domain: GD
  subdomain: 胃・十二指腸憩室
  assertion:
    plain_statement_ja: Lemmel症候群は、総胆管結石がないのに、乳頭周囲の十二指腸憩室が総胆管を外から圧排して閉塞性黄疸を起こす病態である。診断にはMRCPが有用で、ERCPは診断と治療の標準とされる。
    condition:
      source: 単施設コホート（12例）
    differential: 総胆管結石、膵頭部腫瘍、乳頭部腫瘍
    common_misconception: 閉塞性黄疸があれば必ず結石か腫瘍がある
  provenance:
    source_ref: SRC-047
    source: 'Ergüder E, et al. Lemmel syndrome: a single-center cohort and diagnostic considerations. Turk J Surg 2026;42(2):214-219'
    doi: 10.47717/turkjsurg.2026.2025-11-25
    pmid: null
    pmcid: null
    url: https://turkjsurg.com/articles/doi/turkjsurg.2026.2025-11-25
    source_license: © Galenos Publishing House（ライセンス種別は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ライセンス種別は未確認。同論文の有病率の引用には不整合があるため数値は採用しない
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: 医学各論 Ⅵ-5-D-①（食道憩室、胃憩室、十二指腸憩室など、a）
  publication_info:
    created: '2026-10-12'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カード一覧（ID・出典・国試出題基準）

| ID | サブ領域 | SRC | 国試出題基準 |
|---|---|---|---|
| GD-001 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-002 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-003 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-004 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-005 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-006 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-007 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-008 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-009 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-010 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-011 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-012 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-013 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-014 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-015 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-016 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-017 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-018 | 機能性ディスペプシア | SRC-028 | 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a） |
| GD-019 | NSAID・LDA潰瘍の予防 | SRC-031 | 医学各論 Ⅵ-2-C-③（消化性潰瘍、a） |
| GD-020 | NSAID・LDA潰瘍の予防 | SRC-031 | 医学各論 Ⅵ-2-C-③（消化性潰瘍、a） |
| GD-021 | NSAID・LDA潰瘍の予防 | SRC-031 | 医学各論 Ⅵ-2-C-③（消化性潰瘍、a） |
| GD-022 | NSAID・LDA潰瘍の予防 | SRC-031 | 医学各論 Ⅵ-2-C-③（消化性潰瘍、a） |
| GD-023 | NSAID・LDA潰瘍の予防 | SRC-031 | 医学各論 Ⅵ-5-A-①（抗血小板薬による粘膜障害、b） |
| GD-024 | NSAID・LDA潰瘍の予防 | SRC-031 | 医学各論 Ⅵ-5-A-①（抗血小板薬による粘膜障害、b） |
| GD-025 | NSAID・LDA潰瘍の予防 | SRC-031 | 医学各論 Ⅵ-5-A-①（抗血小板薬による粘膜障害、b） |
| GD-026 | NSAID・LDA潰瘍の予防 | SRC-031 | 医学各論 Ⅵ-5-A-①（抗血小板薬による粘膜障害、b） |
| GD-027 | NSAID・LDA潰瘍の予防 | SRC-031 | 医学各論 Ⅵ-2-C-③（消化性潰瘍、a） |
| GD-028 | 酸分泌抑制薬の長期使用 | SRC-031 | 医学各論 Ⅵ-2-D-①（胃ポリープ、a） |
| GD-029 | 消化性潰瘍 | SRC-031 | 医学各論 Ⅵ-2-C-③（消化性潰瘍、a） |
| GD-030 | 消化性潰瘍 | SRC-031 | 医学各論 Ⅵ-2-C-③（消化性潰瘍、a） |
| GD-031 | 消化性潰瘍 | SRC-031 | 医学各論 Ⅵ-2-C-②（慢性胃炎、a） |
| GD-032 | 慢性胃炎 | SRC-031 | 医学各論 Ⅵ-2-C-②（慢性胃炎、a） |
| GD-033 | 胃癌 | SRC-036 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-034 | 胃癌 | SRC-037 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-035 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-036 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-037 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-038 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-039 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-040 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-041 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-042 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-043 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-044 | 胃癌 | SRC-029 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-045 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-046 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-047 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-048 | 胃癌 | SRC-029 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-049 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-050 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-051 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-052 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-053 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-054 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-055 | 胃癌 | SRC-034 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-056 | 胃癌 | SRC-035 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-057 | 胃癌 | SRC-038 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-058 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-059 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-060 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-061 | 胃癌 | SRC-030 | 医学各論 Ⅵ-2-D-②（胃癌、a） |
| GD-062 | GIST・粘膜下腫瘍 | SRC-032 | 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b） |
| GD-063 | GIST・粘膜下腫瘍 | SRC-032 | 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b） |
| GD-064 | GIST・粘膜下腫瘍 | SRC-032 | 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b） |
| GD-065 | GIST・粘膜下腫瘍 | SRC-032 | 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b） |
| GD-066 | GIST・粘膜下腫瘍 | SRC-032 | 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b） |
| GD-067 | GIST・粘膜下腫瘍 | SRC-032 | 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b） |
| GD-068 | GIST・粘膜下腫瘍 | SRC-032 | 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b） |
| GD-069 | GIST・粘膜下腫瘍 | SRC-033 | 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b） |
| GD-070 | GIST・粘膜下腫瘍 | SRC-032 | 医学各論 Ⅵ-5-B-②（消化管粘膜下腫瘍、b） |
| GD-071 | 胃神経内分泌腫瘍 | SRC-039 | 医学各論 Ⅵ-5-B-④（消化管神経内分泌腫瘍、c） |
| GD-072 | 胃静脈瘤 | SRC-017 | 医学各論 Ⅵ-1-D-①（食道静脈瘤、a） |
| GD-073 | 胃静脈瘤 | SRC-018 | 医学各論 Ⅵ-1-D-①（食道静脈瘤、a） |
| GD-074 | 胃切除後症候群 | SRC-040 | 医学各論 Ⅵ-2-B-②（胃切除後症候群、a） |
| GD-075 | 胃切除後症候群 | SRC-040 | 医学各論 Ⅵ-2-B-②（胃切除後症候群、a） |
| GD-076 | 胃切除後症候群 | SRC-040 | 医学各論 Ⅵ-2-B-②（胃切除後症候群、a） |
| GD-077 | 胃切除後症候群 | SRC-040 | 医学各論 Ⅵ-2-B-②（胃切除後症候群、a） |
| GD-078 | 胃切除後症候群 | SRC-040 | 医学各論 Ⅵ-2-B-②（胃切除後症候群、a） |
| GD-079 | 胃切除後症候群 | SRC-040 | 医学各論 Ⅵ-2-B-②（胃切除後症候群、a） |
| GD-080 | 胃切除後症候群 | SRC-030 | 医学各論 Ⅵ-2-B-②（胃切除後症候群、a） |
| GD-081 | 胃アニサキス症 | SRC-041 | 医学各論 Ⅵ-2-C-⑤（胃アニサキス症、a） |
| GD-082 | 胃アニサキス症 | SRC-041 | 医学各論 Ⅵ-2-C-⑤（胃アニサキス症、a） |
| GD-083 | 胃アニサキス症 | SRC-041 | 医学各論 Ⅵ-2-C-⑤（胃アニサキス症、a） |
| GD-084 | 胃アニサキス症 | SRC-042 | 医学各論 Ⅵ-2-C-⑤（胃アニサキス症、a） |
| GD-085 | 胃アニサキス症 | SRC-042 | 医学各論 Ⅵ-2-C-⑤（胃アニサキス症、a） |
| GD-086 | 胃ポリープ | SRC-043 | 医学各論 Ⅵ-2-D-①（胃ポリープ、a） |
| GD-087 | 胃ポリープ | SRC-043 | 医学各論 Ⅵ-2-D-①（胃ポリープ、a） |
| GD-088 | 胃ポリープ | SRC-043 | 医学各論 Ⅵ-2-D-①（胃ポリープ、a） |
| GD-089 | 胃ポリープ | SRC-044 | 医学各論 Ⅵ-2-D-①（胃ポリープ、a） |
| GD-090 | 急性胃粘膜病変 | SRC-044 | 医学各論 Ⅵ-2-C-①（急性胃炎、急性胃粘膜病変、a） |
| GD-091 | 急性胃粘膜病変 | SRC-044 | 医学各論 Ⅵ-2-C-①（急性胃炎、急性胃粘膜病変、a） |
| GD-092 | 急性胃粘膜病変 | SRC-045 | 医学各論 Ⅵ-2-C-①（急性胃炎、急性胃粘膜病変、a） |
| GD-093 | 胃・十二指腸憩室 | SRC-046 | 医学各論 Ⅵ-5-D-①（食道憩室、胃憩室、十二指腸憩室など、a） |
| GD-094 | 胃・十二指腸憩室 | SRC-046 | 医学各論 Ⅵ-5-D-①（食道憩室、胃憩室、十二指腸憩室など、a） |
| GD-095 | 胃・十二指腸憩室 | SRC-047 | 医学各論 Ⅵ-5-D-①（食道憩室、胃憩室、十二指腸憩室など、a） |

## 4. 重複回避の確認

- HP・UG と同じ命題は作っていません。重なりやすい3点は次のように扱いました。
  - GD-004（H. pylori関連ディスペプシア）：FDとの鑑別の観点に限定しています。
  - GD-023（LDA潰瘍の治療）：潰瘍治療に限定し、出血後の再開時期は UG-016 に任せています。
  - GD-031（NHPHの頻度）：頻度の数値に限定し、増加の指摘は HP-019 に任せています。
- 補充ラウンドの追加分も HP・UG と重ならないようにしました。GD-086・087 の胃ポリープは除菌効果ではなく病変の性質に、GD-090 は潰瘍出血ではなく粘膜傷害の性状と対策に限定しています。GD-089 は GD-028（PPI長期使用）と関連するため、Phase 5 で重複の有無を確認してください。
- 胃 MALT リンパ腫は、病期や除菌無効例の治療についての出典が取れなかったため、今回は作っていません。
- ES からの移管：GD-072 は ES-R17 の胃静脈瘤部位分類、GD-073 は ES-R18 の B-RTO の記載です。ES 側から該当部分を削るかどうかは、人間の判断で決めてください。

## 5. 補充ラウンドの追加分（GD-074〜095）

| トピック | ID | 出典 |
|---|---|---|
| 胃切除後症候群（ダンピングの病型・頻度・診断・治療、迷走神経温存） | GD-074〜080 | SRC-040、SRC-030 |
| 胃アニサキス症（虫体・発症・予防・国内発生数・原因種） | GD-081〜085 | SRC-041、SRC-042 |
| 胃ポリープ・胃腺腫・PPI関連粘膜変化 | GD-086〜089 | SRC-043、SRC-044 |
| 急性胃粘膜病変（NSAID粘膜傷害、酢酸亜鉛、REVISE） | GD-090〜092 | SRC-044、SRC-045 |
| 胃・十二指腸憩室（頻度、合併症、Lemmel症候群） | GD-093〜095 | SRC-046、SRC-047 |

## 6. なお未作成のトピック（出典を取得できなかったもの。欠番補完ラウンドで扱う）

- 急性胃粘膜病変（AGML）の定義そのもの
- 胃憩室
- アニサキスの内視鏡的摘出
- GAVE、門脈圧亢進症性胃症
- 胃腺腫の日本での扱い（Ⅵ-2-D-③）、十二指腸腫瘍（腺腫・癌・乳頭部）
- 上腸間膜動脈症候群、好酸球性胃腸炎
- 胃MALTリンパ腫の病期と除菌無効例
- 消化管ポリポーシス、アミロイドーシス
- GIST の二次治療以降（スニチニブ、レゴラフェニブ、ピミテスピブ）
- 胃 NET III 型と治療
- 胃癌治療GL第7版の胃切除後障害・高齢者の CQ（本文の取得が途中で切れたため）

これらに ID は割り当てていないため、欠番は生じていません。

## 7. Claude Code での照合時に重点的に確認する点

1. **CC 種別の確定**：SRC-028・029・030・032・039・042・047 について、Crossref の license 欄で CC 種別を確定する。SRC-042（Emerg Infect Dis）は米国 CDC の刊行物なので、パブリックドメイン（GOV_US）に当たるかを記事ページで確認する。
2. **PMID の取得**：SRC-028・029・030・031・039・040・042・044・045・047 は DOI から PMID を取得する。
3. **ガイドライン・総説からの孫引き数値**（uncertainty に「二次資料経由」と記載）：GD-010（Cochrane PPI 31.1%対25.8%）、GD-047（JCOG1104 93.1%／96.1%）、GD-076（ダンピング頻度）、GD-086（胃底腺ポリープ 23%対12%）、GD-087（過形成性ポリープ退縮 約80%）、GD-093・094（十二指腸憩室の頻度・死亡率）。原著抄録と照合する。
4. **GD-092（REVISE）**：数値は二次資料でしか確認していないため uncertainty にだけ置いています。NEJM の抄録（DOI 10.1056/NEJMoa2404245）で確認できれば、主張文へ移す提案を `proposals/` に出す。
5. **GD-085**：本文と抄録で割合が異なる（88.9% と 88.4%）。どちらを採るかを人間が決める。
6. **GD-079（アカルボース）**：用量は海外の記載。国内添付文書の適応を人間が確認する。
7. **GD-071（胃 NET）**：本文を読んでいないため、専門医検証を優先する。
8. **SPOTLIGHT の全生存**（18.23か月対15.54か月）：二次資料でしか確認していないため、主張文に入れていません。抄録で確認できれば、別カードとして追加する。
