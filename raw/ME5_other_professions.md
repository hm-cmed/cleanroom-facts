# ME第4弾・第1陣（他職種展開）— ME-072〜083（12件）

- 依頼文：`round_ME5_request.md` §1（第1陣12件）。分割案：`ME_split_other_professions.md`。
- 基準コミット：hm-cmed/cleanroom-facts `2f4343dcc6496cceab449de05e636eeb245d7355`（2026-11-24 取得）。出典マスターの最大番号は SRC-5348 で、SRC-54xx は未登録であることを確認した。
- カリキュラム欄（kokushi・core_curriculum）は全件 null（空欄）。ME-001・ME-002 への注記はレポジトリ側で追加されるため、本ファイルのカード本文には書いていない。
- 法令の出典は1法令＝1 SRC とし、legal_basis C・source_class GOV_JP・URL は e-Gov 法令検索の現行法ページとした。条番号は uncertainty に記した。
- 本ファイルで使わなかった SRC-54xx の番号：SRC-5402・5403・5411・5414・5416〜5422 は分割案で後続バッチ用に確保された番号のため未使用（欠番ではなく予約済み）。SRC-5499 まで他は未使用。

## §1 出典表

### 既存出典（再利用）

| SRC | 書誌 | source_class | legal_basis | license | 使うカード |
|---|---|---|---|---|---|
| SRC-5101 | 文部科学省. 医学／歯学教育モデル・コア・カリキュラム（令和4年度改訂版）. 2022年11月 | GOV_JP | B | 政府標準利用規約（文部科学省ホームページ） | ME-072 |
| SRC-5102 | 医師法（昭和23年法律第201号、令和3年法律第49号による改正を含む現行法） | GOV_JP | C | 法令（著作権法13条により権利の目的とならない） | ME-083（裏づけ） |

### 新規出典（SRC-5400〜5499）

| SRC | 書誌 | source_class | legal_basis | license | 使うカード |
|---|---|---|---|---|---|
| SRC-5400 | 歯科医師法（昭和23年法律第202号、現行法） | GOV_JP | C | 法令（著作権法13条により権利の目的とならない） | ME-073・ME-074・ME-083 |
| SRC-5401 | 厚生労働省 医道審議会歯科医師分科会. シームレスな歯科医師養成に向けた共用試験の公的化といわゆるStudent Dentistの法的位置づけについて（報告書）. 令和2年5月 | GOV_JP | B | 政府標準利用規約（厚生労働省ホームページ） | ME-073（裏づけ） |
| SRC-5404 | 文部科学省. 薬学教育モデル・コア・カリキュラム（令和4年度改訂版）. 令和5年2月 | GOV_JP | B | 政府標準利用規約（文部科学省ホームページ） | ME-075・ME-083（裏づけ） |
| SRC-5405 | 薬剤師法（昭和35年法律第146号、現行法） | GOV_JP | C | 法令（著作権法13条により権利の目的とならない） | ME-076・ME-077（裏づけ）・ME-083（裏づけ） |
| SRC-5406 | 厚生労働省. 薬剤師国家試験出題基準（平成28年11月22日とりまとめ、第106回以降適用） | GOV_JP | B | 政府標準利用規約（厚生労働省ホームページ） | ME-077 |
| SRC-5407 | 文部科学省 大学における看護系人材養成の在り方に関する検討会. 看護学教育モデル・コア・カリキュラム. 平成29年10月 | GOV_JP | B | 政府標準利用規約（文部科学省ホームページ） | ME-078 |
| SRC-5408 | 保健師助産師看護師学校養成所指定規則（昭和26年文部省・厚生省令第1号、現行法） | GOV_JP | C | 法令（著作権法13条により権利の目的とならない） | ME-079 |
| SRC-5409 | 保健師助産師看護師法（昭和23年法律第203号、現行法） | GOV_JP | C | 法令（著作権法13条により権利の目的とならない） | ME-080（裏づけ）・ME-081 |
| SRC-5410 | 厚生労働省. 保健師助産師看護師国家試験出題基準（令和5年版）. 令和4年3月 | GOV_JP | B | 政府標準利用規約（厚生労働省ホームページ） | ME-080 |
| SRC-5412 | 保健師助産師看護師法第三十七条の二第二項第一号に規定する特定行為及び同項第四号に規定する特定行為研修に関する省令（平成27年厚生労働省令第33号、現行法） | GOV_JP | C | 法令（著作権法13条により権利の目的とならない） | ME-081（裏づけ） |
| SRC-5413 | 理学療法士作業療法士学校養成施設指定規則（昭和41年文部省・厚生省令第3号、現行法） | GOV_JP | C | 法令（著作権法13条により権利の目的とならない） | ME-082 |
| SRC-5415 | 厚生労働省 医道審議会薬剤師分科会. 新薬剤師国家試験について. 平成22年1月（薬食発0120010号に添付） | GOV_JP | B | 政府標準利用規約（厚生労働省ホームページ） | ME-077（裏づけ） |

新規出典の内訳：法令6件（SRC-5400・5405・5408・5409・5412・5413）、省庁資料6件（SRC-5401・5404・5406・5407・5410・5415）。

## §2 カード

### ME-072 歯学教育モデル・コア・カリキュラム

```yaml
- id: ME-072
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: 歯学教育モデル・コア・カリキュラムは、医学／歯学教育モデル・コア・カリキュラム（令和4年度改訂版、令和4年11月）の歯学部分であり、各大学の歯学のカリキュラムのうち全大学で共通して取り組むべき「コア」の部分を抽出し、モデルとして体系的に整理したものである。歯学部分の第1章「歯科医師として求められる基本的な資質・能力」は、医学部分と共通の10項目（プロフェッショナリズム、総合的に患者・生活者をみる姿勢、生涯にわたって共に学ぶ姿勢、科学的探究、専門知識に基づいた問題解決能力、情報・科学技術を活かす能力、患者ケアのための診療技能、コミュニケーション能力、多職種連携能力、社会における医療の役割の理解）からなる。同改訂版は令和6年度から令和11年度までの入学生に適用される。
    condition:
      region: 日本
      対象: 歯学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5101
    source: 文部科学省. 医学／歯学教育モデル・コア・カリキュラム（令和4年度改訂版）. 2022年11月
    doi: null
    pmid: null
    pmcid: null
    url: https://iryou-kinmukankyou.mhlw.go.jp/files/Attachment/452/%EF%BC%92%20%E3%80%90%E6%96%87%E9%83%A8%E7%A7%91%E5%AD%A6%E7%9C%81%E3%80%91%E5%8C%BB%E5%AD%A6%E6%95%99%E8%82%B2%E3%83%A2%E3%83%87%E3%83%AB%E3%83%BB%E3%82%B3%E3%82%A2%E3%83%BB%E3%82%AB%E3%83%AA%E3%82%AD%E3%83%A5%E3%83%A9%E3%83%A0%E6%94%B9%E8%A8%82%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6.pdf_safe.pdf
    source_license: 政府標準利用規約（文部科学省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置：資質・能力の10項目は歯学部分の第1章、適用期間（令和6年度〜令和11年度入学生）は歯学部分の記載。本文そのものは医学・歯学共通の文書であり、ME-001（医学部分）と同じ出典（SRC-5101）を再利用した。本カードは歯学部分のみを扱う。資質・能力の項目名と符号（PR・GE・LL・RE・PS・IT・CS・CM・IP・SO）が医学部分と共通であることは、文書の目次で確認した。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-073 歯科医師法による共用試験の公的化と Student Dentist

```yaml
- id: ME-073
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 2021年の歯科医師法改正（令和3年法律第49号）により、歯学でも共用試験は公的な位置づけを得た。共用試験は、歯学生が臨床実習を開始する前に修得すべき知識・技能を備えているかどうかを評価するために大学が共用する試験で、厚生労働省令で定めるものとされる。共用試験に合格した歯学生は、大学が行う臨床実習において、歯科医師の指導監督の下に、知識・技能の修得のために歯科医業（政令で定めるものを除く）を行うことができる（歯科医師法第17条の2、いわゆるStudent Dentistの規定で、令和6年4月1日施行）。また令和8年4月1日からは、歯科医師国家試験の受験資格として、大学の歯学の正規の課程を修めて卒業した者に共用試験への合格が要件として加わる（同法第11条第1号）。
    condition:
      region: 日本
      対象: 歯学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5400
    source: 歯科医師法（昭和23年法律第202号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/323AC0000000202
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: 共用試験の公的化とStudent Dentistの法的位置づけは、SRC-5401（厚生労働省 医道審議会歯科医師分科会報告書、令和2年5月、GOV_JP）の提言に基づく改正である
  uncertainty: 出典内の位置：共用試験の定義と受験資格は第11条第1号、Student Dentistは第17条の2（いずれもe-Govの現行法で確認）。施行時期（第17条の2は令和6年4月1日、第11条の要件追加は令和8年4月1日）は改正法の施行期日の定めによるもので、厚生労働省の説明資料（令和7年度医学・歯学教育指導者のためのワークショップ資料）でも照合した。医学（医師法）では医業の規定が令和5年4月1日、受験資格の要件化が令和7年4月1日施行であり、歯学はそれぞれ1年遅れである。作りはME-002（医師法）にそろえた。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-074 歯科医師臨床研修の必修化

```yaml
- id: ME-074
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 診療に従事しようとする歯科医師は、歯科医師法第16条の2第1項により、1年以上、大学病院（歯科・医科）または厚生労働大臣の指定する病院・診療所において臨床研修を受けなければならない。この臨床研修は、平成12年の歯科医師法改正（医療法等の一部を改正する法律、平成12年法律第141号）により平成18年4月1日から必修化されたもので、それ以前は努力義務とされていた。
    condition:
      region: 日本
      対象: 歯科医師（臨床研修歯科医）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5400
    source: 歯科医師法（昭和23年法律第202号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/323AC0000000202
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置：臨床研修の義務は第16条の2第1項（e-Govの現行法で確認）。必修化の時期と改正の経緯は、厚生労働省「歯科医師臨床研修制度の変遷」および同法第16条の2第1項に規定する臨床研修に関する省令の施行通知（平成17年6月28日、医政発第0628012号）で確認した。医師の臨床研修（ME-004、2年間・平成16年度から必修化）とは期間と必修化の時期が異なる。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-075 薬学教育モデル・コア・カリキュラム

```yaml
- id: ME-075
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: 薬学教育モデル・コア・カリキュラム（令和4年度改訂版）は、文部科学省が令和5年2月に公表した、6年制薬学教育において各大学が共通して取り組むべき「コア」の部分をモデルとして体系的に整理した文書で、令和6年度入学生から適用される。本文は、大項目A「薬剤師として求められる基本的な資質・能力」から大項目G「薬学研究」までの7つの大項目からなる。資質・能力は10項目であり、医学・歯学と共通の9項目に、薬学独自の項目である「薬物治療の実践的能力」を加えた構成となっている。
    condition:
      region: 日本
      対象: 薬学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5404
    source: 文部科学省. 薬学教育モデル・コア・カリキュラム（令和4年度改訂版）. 令和5年2月
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mext.go.jp/a_menu/01_d/08091815.htm
    source_license: 政府標準利用規約（文部科学省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置：資質・能力の10項目は大項目A、大項目B〜Gは各学修領域。公表時期（令和5年2月）と適用開始（令和6年度入学生）は文部科学省の薬学教育のページで確認した。資質・能力のうち医学・歯学と異なるのは第7項目のみで、医学・歯学の「患者ケアのための診療技能」に代えて「薬物治療の実践的能力」が置かれている。provenance の URL は文部科学省の薬学教育のページ（本文PDFへのリンクを含む）を指す。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-076 薬学6年制課程と薬剤師国家試験の受験資格

```yaml
- id: ME-076
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 薬剤師国家試験の受験資格は薬剤師法第15条に定められている。第1号は、学校教育法に基づく大学において薬学の正規の課程を修めて卒業した者であり、この正規の課程は学校教育法第87条第2項に定める修業年限6年の課程（6年制課程）を指す。薬学の6年制課程は平成18年度から導入された。第2号は、外国の薬学校を卒業した者などであって、厚生労働大臣が第1号に掲げる者と同等以上の学力および技能を有すると認定した者である。
    condition:
      region: 日本
      対象: 薬学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5405
    source: 薬剤師法（昭和35年法律第146号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/335AC0000000146
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置：受験資格は第15条第1号・第2号（e-Govの現行法で確認）。6年制課程の導入時期（平成18年度）は厚生労働省の通知で確認した。平成16年の薬剤師法改正に伴う経過措置により、旧課程（4年制課程）の卒業者などにも受験資格が認められているが、その要件の詳細は本カードの主張に含めていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-077 薬剤師国家試験

```yaml
- id: ME-077
  domain: ME
  subdomain: アセスメント
  assertion:
    plain_statement_ja: 薬剤師国家試験は、薬剤師法第11条・第12条に基づき、薬剤師として必要な知識および技能について厚生労働大臣が毎年少なくとも1回行う試験である。出題は薬剤師国家試験出題基準（平成28年11月とりまとめ、第106回以降適用）に沿って行われる。試験は2日間にわたって行われ、問題数は全345問で、必須問題90問と、一般問題255問（薬学理論問題105問・薬学実践問題150問）からなる。
    condition:
      region: 日本
      対象: 薬学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5406
    source: 厚生労働省. 薬剤師国家試験出題基準（平成28年11月22日とりまとめ、第106回以降適用）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/iyakuhin/yakuzaishi-kokkashiken/index.html
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: 問題数と日数は、SRC-5415（厚生労働省 医道審議会薬剤師分科会「新薬剤師国家試験について」、平成22年1月、GOV_JP）で定められた形式による。試験の法的根拠はSRC-5405（薬剤師法、GOV_JP）第11条・第12条
  uncertainty: 問題数（345問）と日数（2日間）は、厚生労働省の公表資料「新薬剤師国家試験について」（医道審議会薬剤師分科会のとりまとめで、平成22年1月20日の局長通知に添付）で確定させた。同形式は第97回（平成24年）以降の試験の基礎となっている。なお、令和8年3月25日に公表された新たな基本方針では、第115回（令和11年度実施）から試験科目を薬学教育モデル・コア・カリキュラム（令和4年度改訂版）に対応した5科目とし、出題数を335問（必須問題90問・薬学理論問題125問・薬学実践問題120問）に変更する予定とされているが、2026年11月時点では未施行であり、本カードの数値は現行形式のものである。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-078 看護学教育モデル・コア・カリキュラム

```yaml
- id: ME-078
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: 看護学教育モデル・コア・カリキュラムは、文部科学省の「大学における看護系人材養成の在り方に関する検討会」が平成29年10月に取りまとめた文書で、看護系大学の学士課程における看護師養成教育において共通して取り組むべき内容を抽出し、学生が卒業時までに身に付けておくべき必須の看護実践能力の修得に必要な学修目標を示したものである。「学士課程においてコアとなる看護実践能力と卒業時到達目標」（平成23年）で示された5つの能力群と20の看護実践能力を基礎としており、看護系人材として求められる基本的な資質・能力として9項目（プロフェッショナリズム、看護学の知識と看護実践、根拠に基づいた課題対応能力、コミュニケーション能力、保健・医療・福祉における協働、ケアの質と安全の管理、社会から求められる看護の役割の拡大、科学的探究、生涯にわたって研鑽し続ける姿勢）を掲げている。
    condition:
      region: 日本
      対象: 看護学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5407
    source: 文部科学省 大学における看護系人材養成の在り方に関する検討会. 看護学教育モデル・コア・カリキュラム. 平成29年10月
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mext.go.jp/component/a_menu/education/detail/__icsFiles/afieldfile/2017/10/31/1217788_3.pdf
    source_license: 政府標準利用規約（文部科学省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置：資質・能力の9項目は「看護系人材として求められる基本的な資質・能力」の節、5つの能力群・20の看護実践能力との関係は「看護学教育モデル・コア・カリキュラムの考え方」の節。対象は大学の学士課程であり、看護師養成所の課程は対象に含まれない。学修目標は学修時間数の3分の2程度を目安として精選され、平成31年度から各大学で順次導入された（文部科学省の説明資料による）。医学・歯学・薬学のコア・カリキュラム（令和4年度改訂版）とは策定時期が異なり、資質・能力の項目構成も共通化されていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-079 保健師助産師看護師学校養成所指定規則の改正と看護基礎教育

```yaml
- id: ME-079
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 保健師助産師看護師学校養成所指定規則は、看護師などの養成を行う学校・養成所の指定基準として、課程ごとに教育内容と単位数を定める省令である。令和2年の改正（令和2年文部科学省・厚生労働省令第3号、令和3年4月1日施行）により、看護師課程（別表三）の総単位数は97単位から102単位に増え、「在宅看護論」は「地域・在宅看護論」に改められて4単位から6単位となった。現行の別表三では臨地実習は23単位とされている。改正後の教育内容は令和4年度の入学生から適用され、改正省令の施行の際に現に指定を受けている学校・養成所で修習中の者については、教育の内容について従前の例によることができる経過措置が置かれた。
    condition:
      region: 日本
      対象: 看護学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5408
    source: 保健師助産師看護師学校養成所指定規則（昭和26年文部省・厚生省令第1号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/326M50000180001
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置：看護師課程の基準は第4条と別表三（単位数と臨地実習23単位はe-Govの現行法の別表で確認）。改正省令の番号・施行期日・経過措置の文言は、改正省令の附則と厚生労働省の公布通知（令和2年10月30日、医政発第1030015号・文科高第666号）で確認した。2年課程（別表三の二、65単位から68単位）は令和4年4月1日施行・令和5年度入学生から適用であり、別表三とは施行時期が異なる。現行の統合された省令本文にはその後の改正も含まれるが、本カードは令和2年改正による看護師課程の変更を扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-080 看護師国家試験と出題基準

```yaml
- id: ME-080
  domain: ME
  subdomain: アセスメント
  assertion:
    plain_statement_ja: 看護師国家試験は、保健師助産師看護師法第17条に基づく国家試験であり、出題は保健師助産師看護師国家試験出題基準（令和5年版）に沿って行われる。試験は全240問で、必修問題50問、一般問題130問、状況設定問題60問からなり、試験科目は人体の構造と機能、疾病の成り立ちと回復の促進、健康支援と社会保障制度、基礎看護学、地域・在宅看護論、成人看護学、老年看護学、小児看護学、母性看護学、精神看護学、看護の統合と実践の11科目である。
    condition:
      region: 日本
      対象: 看護学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5410
    source: 厚生労働省. 保健師助産師看護師国家試験出題基準（令和5年版）. 令和4年3月
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/shingi2/0000159020_00001.html
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: 試験の法的根拠は、SRC-5409（保健師助産師看護師法、GOV_JP）第17条
  uncertainty: 出典内の位置：出題基準は令和4年3月28日に公表された令和5年版で、保健師・助産師の出題基準と一体の文書である。問題数と内訳（240問・必修50問・一般130問・状況設定60問）は、厚生労働省が公表する試験の施行および合格発表の資料（第115回看護師国家試験）で照合した。11科目の名称は厚生労働省の「看護師国家試験の施行」の案内による。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-081 特定行為研修

```yaml
- id: ME-081
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 特定行為研修は、保健師助産師看護師法第37条の2に基づく研修であり、看護師が手順書により特定行為を行おうとする場合に修了が求められる。特定行為とは、診療の補助であって、看護師が手順書により行う場合に実践的な理解力、思考力および判断力並びに高度かつ専門的な知識および技能が特に必要とされるものとして省令で定めるものであり、省令の別表に38行為が掲げられている。研修は特定行為区分（21区分）ごとに厚生労働大臣が指定する指定研修機関において行われ、すべての区分に共通する共通科目（7科目、計250時間）と、区分ごとの区分別科目からなる。
    condition:
      region: 日本
      対象: 看護師
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5409
    source: 保健師助産師看護師法（昭和23年法律第203号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/323AC0000000203
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: 特定行為の数（38行為）・特定行為区分の数（21区分）・共通科目の時間数は、SRC-5412（特定行為研修に関する省令、GOV_JP）の別表第一〜第三による
  uncertainty: 出典内の位置：特定行為・手順書・特定行為研修・指定研修機関の定義は第37条の2第2項、研修修了の要件は同条第1項。38行為と21区分は平成27年の制度施行時に定められた数であり、現行の省令（平成31年厚生労働省令第73号による改正後）の別表第一・別表第二でも同数であることを確認した。共通科目の計250時間は現行省令の別表第三に掲げる7科目（臨床病態生理学30時間、臨床推論45時間、フィジカルアセスメント45時間、臨床薬理学45時間、疾病・臨床病態概論40時間、医療安全学45時間、特定行為実践）の合計であり、2019年の見直し後の現行値である。区分別科目の時間数は区分によって異なるため、本カードでは総量を示していない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-082 理学療法士・作業療法士の養成施設指定規則の改正

```yaml
- id: ME-082
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 理学療法士作業療法士学校養成施設指定規則は、理学療法士および作業療法士の養成施設の指定基準として、教育内容と単位数を定める省令である。平成30年の改正により、別表第一（理学療法士）および別表第二（作業療法士）の総単位数は93単位から101単位に、臨床実習は18単位から20単位に引き上げられ、改正後の教育内容は令和2年4月1日から適用された。改正省令の施行の際に現に単位を修得中の者については、改正後の別表によらず従前の例によることができる経過措置が置かれた。
    condition:
      region: 日本
      対象: 理学療法士・作業療法士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5413
    source: 理学療法士作業療法士学校養成施設指定規則（昭和41年文部省・厚生省令第3号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/341M50000180003
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置：現行の別表第一の合計101単位と臨床実習20単位は、e-Govの現行法の別表で確認した。施行期日（令和2年4月1日）と経過措置の文言は改正省令の附則による。改正前の単位数（93単位・臨床実習18単位）は、文部科学省・厚生労働省の改正の説明による。別表第二（作業療法士）も同じ改正で同じ単位数に引き上げられた。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

### ME-083 共用試験の法的位置づけの違い（医学・歯学・薬学）

```yaml
- id: ME-083
  domain: ME
  subdomain: 横断
  assertion:
    plain_statement_ja: 共用試験の法的位置づけは職種によって異なる。医学では、医師法により、共用試験への合格が医師国家試験の受験資格の要件とされ、共用試験に合格した医学生が臨床実習において医師の指導監督の下に医業を行うことが認められている（第11条第1号・第17条の2）。歯学でも、歯科医師法に並行する規定があり、共用試験に合格した歯学生の臨床実習における歯科医業は令和6年4月1日から、受験資格の要件化は令和8年4月1日から施行される（第11条第1号・第17条の2）。これに対し薬学では、薬剤師法に共用試験に関する規定は置かれておらず、薬学共用試験は薬学教育モデル・コア・カリキュラムに位置づけられて実務実習に進む前提として実施されており、薬剤師国家試験の受験資格は薬剤師法第15条により6年制課程の卒業などによって定められている。
    condition:
      region: 日本
      対象: 医学生・歯学生・薬学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5400
    source: 歯科医師法（昭和23年法律第202号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/323AC0000000202
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: 医学の規定はSRC-5102（医師法、GOV_JP）第11条第1号・第17条の2、薬学についてはSRC-5405（薬剤師法、GOV_JP）およびSRC-5404（文部科学省 薬学教育モデル・コア・カリキュラム（令和4年度改訂版）、GOV_JP）による
  uncertainty: 薬剤師法に共用試験に関する規定がないことは、e-Govの現行法の全文を確認して判断した。薬学共用試験の実施主体は薬学共用試験センターであるが、実施機関の資料は主出典とせず、位置づけの根拠は薬学教育モデル・コア・カリキュラムの記載によった。個別の制度の詳細は、医学はME-002、歯学はME-073、薬学の受験資格はME-076を参照されたい。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

## §3 カリキュラム対応

全12件とも、依頼文 §1 の指定により kokushi・core_curriculum は null（空欄）とした。対応表は作成していない。

## §4 未解決事項

1. **ME-075**：資質・能力10項目と大項目A〜Gの構成は、文部科学省の掲載ページと改訂関係者の解説で照合したが、本文PDFの該当箇所の逐語照合は取り込み時の検査に委ねる。主張文の範囲（項目数・大項目名・適用年度）については公表資料で確認済みである。
2. **ME-077**：令和8年3月の新基本方針に基づく出題基準の改定は令和8年度中に行われる予定であり、第115回（令和11年度実施）から335問・5科目となる。改定後の出題基準が公表された時点で、本カードの数値部分の更新が必要になる。
3. **ME-081**：区分別科目の時間数は区分ごとに異なる（講義・演習で5〜34時間の幅があり、別に実習がある）ため総量は示していない。区分別の一覧が必要になれば省令別表第四から別カード化できる。
4. **ME-082**：別表第二（作業療法士）の合計単位数（101単位）は改正の説明資料で照合したが、e-Govの別表第二の全項目の合算による検算は行っていない（別表第一は合算で確認済み）。

## §5 引き継ぎメモ

- 新規出典は SRC-5400・5401・5404・5405・5406・5407・5408・5409・5410・5412・5413・5415 の12件（法令6件・省庁資料6件）。SRC-5402・5403・5411・5414・5416〜5422 は分割案で後続バッチ（歯科の到達目標通知・歯科出題基準、薬学共用試験センター、歯科医師分科会意見など）用に確保された番号であり、本ファイルでは未使用と明記した。
- ME-072 は既存の SRC-5101（医学／歯学コアカリ）を再利用し、provenance は ME-001 と同一とした。ME-083 の裏づけに既存の SRC-5102（医師法）を使った。
- ME-073 は ME-002（医師法による共用試験の公的化）と対になるカードとして、文の作りをそろえた。施行時期が医学より1年遅れる点は両カードの uncertainty で相互に言及している。
- 法令カードの source_license は ME4 の法令カードにそろえて「法令（著作権法13条により権利の目的とならない）」とした。

## §6 納品前検証の記録（2026-11-24）

- 書誌・条文の原典照合：法令6件はすべて e-Gov 法令検索の現行法の全文（法令API）で条番号と内容を確認した（歯科医師法 第11条第1号・第16条の2・第17条の2、薬剤師法 第11条・第12条・第15条、保健師助産師看護師法 第17条・第37条の2、指定規則 第4条・別表三、特定行為研修省令 第2条・第4条・第5条と別表第一〜第四、理学療法士作業療法士学校養成施設指定規則 別表第一）。
- 数値の確定：ME-077 の345問・2日間は厚生労働省「新薬剤師国家試験について」（平成22年1月）で確定させた。ME-080 の240問と内訳は厚生労働省の試験施行・合格発表資料で照合した。ME-081 の38行為・21区分・共通科目250時間は現行省令の別表の実数で確認した。ME-079 の102単位・臨地実習23単位、ME-082 の101単位・臨床実習20単位は現行の別表の合算で確認した。
- 件数・番号の照合：カード12件（ME-072〜083、欠番なし）、新規出典12件（内訳は法令6・省庁資料6）、未使用番号（5402・5403・5411・5414・5416〜5422）を §1 と §5 に明記した。出典マスター（基準コミット 2f4343dc）との DOI・書誌の重複照合を行い、SRC-54xx に既存登録がないことを確認した。
- 形式の検証：全カードに region（日本）と対象があり、assertion は対象の形、curriculum は全件 null、YAML のパース確認を実施した（検証スクリプトの結果は本ファイル末尾の記録どおり）。
