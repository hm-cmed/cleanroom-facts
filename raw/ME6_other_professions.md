# ME第4弾・第2陣（他職種展開の残り）— ME-084〜112（29件）

- 依頼文：`round_ME6_request.md` §1（残り29件）。分割案：`ME_split_other_professions.md`（D-3〜D-5、D-7、D-8、P-3〜P-5、N-4〜N-6、O-2〜O-6、X-1、X-3、X-4）と `ME_split_other_professions_add.md`（O-7〜O-16）。
- 基準コミット：hm-cmed/cleanroom-facts `208dce0d7f132ccf209512b3ca8454d4fdaf62b2`（2026-11-24 取得）。第1陣（ME-072〜083）とその出典（SRC-5400〜5415）は取り込み済みであることを、レポジトリの data/facts/ME.yaml と data/sources/sources.yaml で確認した。出典マスターの最大番号は SRC-5415。
- 形式の修正（依頼文の指定）：カード本文の YAML は全29件を1つの ```yaml ブロックにまとめた。出典表の列名は依頼文の指定どおりとした。
- カリキュラム欄（kokushi・core_curriculum）は全件 null（空欄）。横断3件（ME-110〜112）の `condition.対象` は「教育者」とした。
- 法令の出典は1法令＝1 SRC とし、legal_basis C・source_class GOV_JP・URL は e-Gov 法令検索の現行法ページとした。条番号は uncertainty に記した。
- 番号の付け直し：分割案の仮番号 SRC-5415〜5419 は第1陣の実績（SRC-5415＝新薬剤師国家試験について）と衝突するため、本ファイルでは付け直した。対応は §5 の付け直し表に記した。
- 組み立て時に行った修正（ME-091 の裏づけ出典の新設ほか3点）は §6 に before → after で記した。

## §1 出典表

### 既存出典（再利用）

| SRC | 出典 | DOI | PMID | ライセンス表示 | legal_basis | source_class | 使うカード |
|---|---|---|---|---|---|---|---|
| SRC-5101 | 文部科学省. 医学／歯学教育モデル・コア・カリキュラム（令和4年度改訂版）. 2022年11月 | - | - | 政府標準利用規約（文部科学省ホームページ） | B | GOV_JP | ME-110 |
| SRC-5400 | 歯科医師法（昭和23年法律第202号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-086・ME-087（裏づけ） |
| SRC-5404 | 文部科学省. 薬学教育モデル・コア・カリキュラム（令和4年度改訂版）. 令和5年2月 | - | - | 政府標準利用規約（文部科学省ホームページ） | B | GOV_JP | ME-089・ME-090・ME-091、ME-110（裏づけ） |
| SRC-5405 | 薬剤師法（昭和35年法律第146号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-089・ME-090（裏づけ） |
| SRC-5406 | 厚生労働省. 薬剤師国家試験出題基準（平成28年11月22日とりまとめ、第106回以降適用） | - | - | 政府標準利用規約（厚生労働省ホームページ） | B | GOV_JP | ME-112（裏づけ） |
| SRC-5407 | 文部科学省 大学における看護系人材養成の在り方に関する検討会. 看護学教育モデル・コア・カリキュラム. 平成29年10月 | - | - | 政府標準利用規約（文部科学省ホームページ） | B | GOV_JP | ME-110（裏づけ） |
| SRC-5408 | 保健師助産師看護師学校養成所指定規則（昭和26年文部省・厚生省令第1号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-092、ME-109（裏づけ） |
| SRC-5409 | 保健師助産師看護師法（昭和23年法律第203号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-109、ME-092・ME-093・ME-094（裏づけ） |
| SRC-5410 | 厚生労働省. 保健師助産師看護師国家試験出題基準（令和5年版）. 令和4年3月 | - | - | 政府標準利用規約（厚生労働省ホームページ） | B | GOV_JP | ME-093・ME-112 |

### 新規出典（31件）

| SRC | 出典 | DOI | PMID | ライセンス表示 | legal_basis | source_class | 使うカード |
|---|---|---|---|---|---|---|---|
| SRC-5402 | 厚生労働省. 歯科医師臨床研修の到達目標（令和3年3月31日 医政発0331第75号通知の別添） | - | - | 政府標準利用規約（厚生労働省ホームページ） | B | GOV_JP | ME-087 |
| SRC-5403 | 厚生労働省. 歯科医師国家試験出題基準（令和3年度版） | - | - | 政府標準利用規約（厚生労働省ホームページ） | B | GOV_JP | ME-086、ME-112（裏づけ） |
| SRC-5411 | 厚生労働省. 新人看護職員研修ガイドライン. 平成26年2月 | - | - | 政府標準利用規約（厚生労働省ホームページ） | B | GOV_JP | ME-094 |
| SRC-5416 | 臨床検査技師等に関する法律（昭和33年法律第76号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-095 |
| SRC-5417 | 臨床検査技師学校養成所指定規則（昭和45年文部省・厚生省令第3号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-095（裏づけ） |
| SRC-5418 | 診療放射線技師法（昭和26年法律第226号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-096 |
| SRC-5419 | 診療放射線技師学校養成所指定規則（昭和26年文部省・厚生省令第4号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-096（裏づけ） |
| SRC-5420 | 特定非営利活動法人薬学共用試験センター. 薬学共用試験について. 薬学共用試験センター公式サイト | - | - | 実施機関の公表資料（権利者の表示に従う） | B | RESTRICTED | ME-089・ME-090（裏づけ） |
| SRC-5421 | 公益社団法人医療系大学間共用試験実施評価機構. 歯学生共用試験要綱（2023年11月14日発行、2023年11月24日理事会承認） | - | - | 利用規約の明示を確認できず（機構資料。厚生労働省の部会資料として掲載された版で確認） | B | RESTRICTED | ME-084・ME-085（裏づけ） |
| SRC-5422 | 厚生労働省 医道審議会歯科医師分科会歯学生共用試験部会. 公的化後の共用試験に関する意見（令和5年6月30日） | - | - | 政府標準利用規約（厚生労働省ホームページ） | B | GOV_JP | ME-084・ME-085 |
| SRC-5423 | 栄養士法（昭和22年法律第245号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-097 |
| SRC-5424 | 歯科衛生士法（昭和23年法律第204号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-098 |
| SRC-5425 | 歯科衛生士学校養成所指定規則（昭和25年文部省・厚生省令第1号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-098（裏づけ） |
| SRC-5426 | 救急救命士法（平成3年法律第36号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-099 |
| SRC-5427 | 看護師等の人材確保の促進に関する法律（平成4年法律第86号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-094（裏づけ） |
| SRC-5428 | 厚生労働省. 資格・試験情報（医療、医薬品、健康、食品衛生関連の国家試験一覧、令和9年実施試験の日程を掲載、2026年11月24日確認） | - | - | 政府標準利用規約（厚生労働省ホームページ） | B | GOV_JP | ME-111 |
| SRC-5429 | 一般社団法人日本歯科専門医機構. 日本歯科専門医制度概報（令和6年度版） | - | - | 利用規約の明示を確認できず（機構の公式サイトで公表された版で確認） | B | RESTRICTED | ME-088（裏づけ） |
| SRC-5430 | 厚生労働省. 第21回医療情報の提供内容等のあり方に関する検討会 資料1-1「専門医に関する広告について」（令和5年8月25日） | - | - | 政府標準利用規約（厚生労働省ホームページ） | B | GOV_JP | ME-088 |
| SRC-5431 | 薬学教育協議会. 臨床における実務実習に関するガイドライン. 令和5年12月（令和5年度文部科学省「大学における医療人養成の在り方に関する調査研究」、文部科学省の薬学教育のページに掲載） | - | - | 政府標準利用規約（文部科学省ホームページ） | B | GOV_JP | ME-091（裏づけ） |
| SRC-5450 | 臨床工学技士法（昭和62年法律第60号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-100・ME-101 |
| SRC-5451 | 厚生労働省. 臨床工学技士学校養成所カリキュラム等改善検討会報告書. 令和3年3月25日 | - | - | 政府標準利用規約（厚生労働省ホームページ） | B | GOV_JP | ME-101（裏づけ） |
| SRC-5452 | 言語聴覚士法（平成9年法律第132号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-102 |
| SRC-5453 | 視能訓練士法（昭和46年法律第64号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-103 |
| SRC-5454 | 歯科技工士法（昭和30年法律第168号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-104・ME-105 |
| SRC-5455 | 義肢装具士法（昭和62年法律第61号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-106 |
| SRC-5456 | 柔道整復師法（昭和45年法律第19号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-107 |
| SRC-5457 | あん摩マツサージ指圧師、はり師、きゆう師等に関する法律（昭和22年法律第217号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-108 |
| SRC-5458 | 歯科技工士学校養成所指定規則（昭和31年厚生省令第3号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-104（裏づけ） |
| SRC-5459 | 柔道整復師学校養成施設指定規則（昭和47年文部省・厚生省令第2号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-107（裏づけ） |
| SRC-5460 | あん摩マツサージ指圧師、はり師及びきゆう師に係る学校養成施設認定規則（昭和26年文部省・厚生省令第2号、現行法） | - | - | 法令（著作権法13条により権利の目的とならない） | C | GOV_JP | ME-108（裏づけ） |
| SRC-5461 | 厚生労働省. 第2回歯科技工士の養成・確保に関する検討会 資料2（歯科技工士養成の現況）. 平成30年7月5日 | - | - | 政府標準利用規約（厚生労働省ホームページ） | B | GOV_JP | ME-105（裏づけ） |

新規出典の内訳：法令19件（法律・省令）、省庁資料9件、実施機関資料（RESTRICTED）3件（SRC-5420・5421・5429、いずれも裏づけのみ）。


## §2 カード

```yaml
- id: ME-084
  domain: ME
  subdomain: アセスメント
  assertion:
    plain_statement_ja: 日本の歯学生共用試験のうちCBTは、臨床実習を始める前に修得すべき知識の総合的な理解を確認するコンピュータを用いた試験で、実施機関が作成する6ブロック合計320問で構成され、公的化後は全大学の受験者に共通する統一到達基準に基づいて合否が判定される
    condition:
      region: 日本
      対象: 歯学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5422
    source: 厚生労働省 医道審議会歯科医師分科会歯学生共用試験部会. 公的化後の共用試験に関する意見（令和5年6月30日）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10803000/001647856.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: SRC-5421（医療系大学間共用試験実施評価機構・歯学生共用試験要綱、RESTRICTED）による
  uncertainty: 主出典の「1.はじめに」（共用試験はCBTとOSCEで構成され臨床実習開始前の能力を測ること、実施機関は公益社団法人医療系大学間共用試験実施評価機構であること）と「2.（1）合格基準の設定の在り方」（公的化後は統一到達基準を設定し実施機関が合否を判定すること）で確認した（2026-11-24確認）。問題数320問・6ブロックは主出典には記載がなく、裏づけ出典の歯学生共用試験要綱「2-3-1. CBT（学科試験）」で確認した範囲に限って主張文に入れた。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-085
  domain: ME
  subdomain: アセスメント
  assertion:
    plain_statement_ja: 日本の歯学生共用試験のうち臨床実習前のOSCEは、臨床実習を始める前に修得すべき臨床能力を確認する実技試験で、公的化後は課題の数と種類が統一され、医療面接1課題、歯科治療に必要な診察と検査1課題、基本的臨床技能4課題の計6課題が実施される
    condition:
      region: 日本
      対象: 歯学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5422
    source: 厚生労働省 医道審議会歯科医師分科会歯学生共用試験部会. 公的化後の共用試験に関する意見（令和5年6月30日）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10803000/001647856.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: SRC-5421（医療系大学間共用試験実施評価機構・歯学生共用試験要綱、RESTRICTED）による
  uncertainty: 主出典の「2.（3）OSCEの在り方 ①課題の数及び種類」で、令和6年度から課題の数と種類を統一し「医療面接」1課題・「歯科治療に必要な診察と検査」1課題・「基本的臨床技能」4課題の計6課題を実施することが適当とされたことを確認した（2026-11-24確認）。裏づけ出典の歯学生共用試験要綱「2-3-2. OSCE（実技試験）」でも、臨床実習開始前に修得すべき臨床能力を確認する試験であることを確認した。各課題の制限時間や評価項目の詳細は確認した資料の範囲では主張文に入れていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-086
  domain: ME
  subdomain: アセスメント
  assertion:
    plain_statement_ja: 歯科医師国家試験は歯科医師法第9条に基づき臨床上必要な歯科医学と口腔衛生について行われ、出題基準は必修の基本的事項、歯科医学総論、歯科医学各論の3区分で出題の内容とブループリントによる出題割合を示し、試験委員はこの基準を踏まえて出題する
    condition:
      region: 日本
      対象: 歯学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5403
    source: 厚生労働省. 歯科医師国家試験出題基準（令和3年度版）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/file/05-Shingikai-10803000-Iseikyoku-Ijika/0000164154.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: SRC-5400（歯科医師法、法令）による
  uncertainty: "出題基準の「利用法」で、試験が歯科医師法第9条に基づくこと、出題基準が内容を具体的な項目で示すものであること、3区分（必修の基本的事項・歯科医学総論・歯科医学各論）の関係とブループリント（設計表）で出題割合を示すことを確認した（2026-11-24確認。確認に使ったURLは出題基準の利用法部分の公表PDF）。§2-1への対応として、コアカリキュラムとの関係に触れる解釈的表現は、令和3年度版の利用法で確認できなかったため主張文に入れていない（確認メモ参照）。総問題数は令和3年度版そのものでは確認できなかったため主張文に入れていない。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-087
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: 歯科医師臨床研修の到達目標は、A.歯科医師としての基本的価値観（プロフェッショナリズム）4項目、B.資質・能力9項目、C.基本的診療業務の3部で構成され、Cは基本的診療能力等と歯科医療に関連する連携と制度の理解等からなり項目ごとに必修と選択が定められている
    condition:
      region: 日本
      対象: 歯科医師（臨床研修歯科医）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5402
    source: 厚生労働省. 歯科医師臨床研修の到達目標（令和3年3月31日 医政発0331第75号通知の別添）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10800000/000765371.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: SRC-5400（歯科医師法、法令）による
  uncertainty: 通知別添の本文で、Aの4項目（社会的使命と公衆衛生への寄与、利他的な態度、人間性の尊重、自らを高める姿勢）、Bの9項目、Cの構成（1.基本的診療能力等＝基本的診察・検査・診断・診療計画、基本的臨床技能等、患者管理、患者の状態に応じた歯科医療の提供／2.歯科医療に関連する連携と制度の理解等）と、各項目への（必修）（選択）の付記を確認した（2026-11-24確認）。研修期間1年以上は裏づけ出典の歯科医師法第16条の2第1項（e-Gov現行法）で確認したが、本カードの主張は到達目標の構成に限った。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-088
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 日本の歯科専門医は、2018年に設立された日本歯科専門医機構が各領域の学会の制度を評価し認証する仕組みのもとで認定され、同機構の認定を受けた基本的な診療領域の専門性は医療広告に表示でき、基本領域は10領域とされ、そのうち仮称の2領域を除く8領域で制度の評価と認定が行われている
    condition:
      region: 日本
      対象: 歯科医師
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5430
    source: 厚生労働省. 第21回医療情報の提供内容等のあり方に関する検討会 資料1-1「専門医に関する広告について」（令和5年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10800000/001147750.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: SRC-5429（日本歯科専門医機構・日本歯科専門医制度概報（令和6年度版）、RESTRICTED）による
  uncertainty: 主出典で、令和3年10月1日適用の告示改正により日本歯科専門医機構が行う専門性に関する認定を受けた旨（基本的な診療領域に限る）が広告できる事項に追加されたこと、同機構が2018年に設立されたこと、10基本領域で認定の検討が進められたことを確認した（2026-11-24確認）。10領域のうち評価・認定を実施しているのが8領域（インプラント歯科専門医・総合歯科専門医の仮称2領域を除く）であることは、裏づけ出典の概報「令和6年度版日本歯科専門医制度概報の発刊にあたって」で確認した範囲に限る。各領域の専門医数や個別の認定者数は主張文に入れていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-089
  domain: ME
  subdomain: アセスメント
  assertion:
    plain_statement_ja: 薬学共用試験のCBTは、薬学生が臨床における実務実習を開始する前に、実習に必要な知識を身に付けているかどうかを評価するために大学が共用する試験（共用試験）の一部であり、コンピュータを用いて知識を問う客観試験である。共用試験は第三者機関である特定非営利活動法人薬学共用試験センターが実施し、薬学生は実務実習を行う前年度にこれを受験する。薬剤師法には共用試験に関する規定は置かれておらず、CBTは国家試験ではなく、実務実習に進むための前提として位置づけられる。
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
    corroboration: SRC-5420（特定非営利活動法人薬学共用試験センター・薬学共用試験について、RESTRICTED）とSRC-5405（薬剤師法、GOV_JP）による
  uncertainty: 出典内の位置は、薬学教育モデル・コア・カリキュラム（令和4年度改訂版）本文の「薬学教育モデル・コア・カリキュラムの考え方」における共用試験の定義（実務実習を開始する前に修得すべき知識及び技能を身に付けているかどうかを評価するために大学が共用する試験）と、患者・市民へのお願い文面例の注記（薬学共用試験センターが知識を問うコンピュータによる試験CBTと技能・態度を評価する試験OSCEを実施している旨）による。実施時期（実務実習の前年度、原則として12月1日から1月31日のうち各大学が設定した日程）は薬学共用試験センターの公表ページで確認した。問題数は、省庁資料で確認できなかったため主張文に入れていない（依頼文§2-3への対応は確認メモ参照）。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-090
  domain: ME
  subdomain: アセスメント
  assertion:
    plain_statement_ja: 薬学共用試験のOSCEは、薬学生が臨床における実務実習を開始する前に、実習に必要な技能を身に付けているかどうかを評価するために大学が共用する試験（共用試験）の一部であり、模擬患者の協力を得て技能や態度を評価する客観的臨床能力試験である。OSCEは知識を問うCBTと合わせて共用試験を構成し、実施主体は特定非営利活動法人薬学共用試験センターである。薬剤師法には共用試験に関する規定は置かれておらず、OSCEは国家試験ではなく、実務実習に進むための前提として位置づけられる。
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
    corroboration: SRC-5420（特定非営利活動法人薬学共用試験センター・薬学共用試験について、RESTRICTED）とSRC-5405（薬剤師法、GOV_JP）による
  uncertainty: 出典内の位置は、ME-089と同じく、薬学教育モデル・コア・カリキュラム（令和4年度改訂版）本文の共用試験の定義と、患者・市民へのお願い文面例の注記（模擬患者の協力を得て技能や態度を評価する試験OSCE）による。センターの公表ページでは、OSCEは実技を通して主に技能・態度を評価する試験と説明されている。課題数は、省庁資料で確認できなかったため主張文に入れていない（依頼文§2-3への対応は確認メモ参照）。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-091
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: 薬学の臨床における実務実習は、薬学教育モデル・コア・カリキュラム（令和4年度改訂版）の大項目F「臨床薬学」の学修の中核であり、学生が医療現場で継続的に患者・生活者を担当し、薬物治療の個別最適化を学ぶ参加型の実習である。実習の期間は、薬局と病院の連続性のある22週間で、各施設11週間を原則とし、全体で22週間を下回らないこととされている。実務実習は、実習前に大学で行う学修、医療現場での実務実習、実習終了後に大学で学修を深める段階を合わせた3つの段階からなる学修の一部である。
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
    corroboration: SRC-5431（薬学教育協議会・臨床における実務実習に関するガイドライン、GOV_JP）による
  uncertainty: 出典内の位置は、大項目F「臨床薬学」の位置づけと実務実習の意義はコア・カリキュラム本文の「薬学教育モデル・コア・カリキュラムの考え方」による。週数（各施設11週間・計22週間）そのものはコア・カリキュラム本文には記載がなく、文部科学省の薬学教育のページにコア・カリキュラムと並べて掲載されている「臨床における実務実習に関するガイドライン」（薬学教育協議会、令和5年12月、令和5年度文部科学省「大学における医療人養成の在り方に関する調査研究」）の第2章2-1「実習期間・実習順」で確認した。同ガイドラインは「各施設11週間を原則とする（ただし22週間を下回らないこと）」とする。3つの段階（フェーズ）の構成は同ガイドライン第1章1-2による。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-092
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 保健師と助産師の養成課程は、保健師助産師看護師学校養成所指定規則が課程ごとに指定基準を定めており、保健師課程・助産師課程とも修業年限は1年以上で、教育の内容は保健師課程が別表一、助産師課程が別表二に定められ、総単位数はそれぞれ31単位である。保健師課程は公衆衛生看護学18単位、疫学2単位、保健統計学2単位、保健医療福祉行政論4単位、臨地実習5単位からなり、助産師課程は基礎助産学6単位、助産診断・技術学10単位、地域母子保健2単位、助産管理2単位、臨地実習11単位からなる。国家試験の受験資格は保健師助産師看護師法により、指定された学校において1年以上必要な学科を修めた者などに認められる。
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
    corroboration: SRC-5409（保健師助産師看護師法、GOV_JP）第19条・第20条による
  uncertainty: 出典内の位置は、保健師課程の指定基準が第2条（修業年限1年以上、教育内容は別表一）、助産師課程の指定基準が第3条（修業年限1年以上、教育内容は別表二）であり、単位数と内訳はe-Gov現行法の別表一・別表二で確認し、合計がそれぞれ31単位になることを合算で検算した。別表一・別表二には括弧内の数値（保健師課程の合計28単位、助産師課程の合計30単位など）も併記されているが、本カードでは括弧外の数値を用いた。助産師課程の臨地実習では、分べんの取扱いを学生1人につき10回程度行わせることが別表二の備考に定められている。受験資格は保健師助産師看護師法第19条（保健師）・第20条（助産師）による。大学における選択制などの養成の実態は、国の一次資料で確認できる範囲を超えるため主張文に入れていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-093
  domain: ME
  subdomain: アセスメント
  assertion:
    plain_statement_ja: 保健師国家試験と助産師国家試験は、保健師助産師看護師法第17条に基づく国家試験であり、出題は保健師助産師看護師国家試験出題基準（令和5年版）に沿って行われる。保健師の試験科目は公衆衛生看護学、疫学、保健統計学、保健医療福祉行政論の4科目であり、助産師の試験科目は基礎助産学、助産診断・技術学、地域母子保健、助産管理の4科目である。両試験とも問題数は110問で、一般問題75問と状況設定問題35問からなる。試験時間は、令和3年3月の保健師助産師看護師国家試験制度改善検討部会報告書で保健師・助産師の試験時間を延長することが望ましいとされたことを受けて、令和5年に実施された試験から延長され、午前・午後各1時間20分の計2時間40分となっている。
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
    corroboration: SRC-5409（保健師助産師看護師法、GOV_JP）第17条による
  uncertainty: "出典内の位置は、出題基準（令和5年版）のうち保健師国家試験出題基準（公衆衛生看護学、疫学、保健統計、保健医療福祉行政論）と助産師国家試験出題基準（基礎助産学、助産診断・技術学、地域母子保健、助産管理）の体系による。問題数（110問、一般問題75問・状況設定問題35問）は厚生労働省の国家試験制度改善検討部会の資料・議事録で確認した。試験時間の延長は、令和3年3月31日の同部会報告書が「保健師国家試験及び助産師国家試験においては試験時間を延長することが望ましい」としたもので、令和8年1月19日の同部会における厚生労働省の説明で、令和5年に実施した試験から保健師・助産師国家試験の試験時間の延長を行ったことが明示されている。現在の試験時間（午前・午後各1時間20分）は、厚生労働省の第109回助産師国家試験受験者留意事項（試験時間10時40分から12時00分、13時55分から15時15分）で確認した。延長前は午前1時間15分・午後1時間20分の計2時間35分であった（平成27年度の同部会資料による）。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-094
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 新人看護職員研修は、免許取得後に初めて就労する新人看護職員が基本的な臨床実践能力を獲得するための研修であり、厚生労働省の新人看護職員研修ガイドライン（平成26年2月の改訂版）は、新人看護職員が1年以内に到達を目指す到達目標とその到達の目安を示している。この研修は、平成21年の保健師助産師看護師法と看護師等の人材確保の促進に関する法律の改正により、平成22年4月1日から努力義務とされている。すなわち、看護職員本人は免許を受けた後も臨床研修その他の研修を受けて資質の向上を図るよう努めることとされ、病院等の開設者は新たに業務に従事する看護師等に対する臨床研修その他の研修を実施するよう努めることとされており、医師や歯科医師の臨床研修のように修了が義務として課される必修の制度ではない。
    condition:
      region: 日本
      対象: 看護職員
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5411
    source: 厚生労働省. 新人看護職員研修ガイドライン. 平成26年2月
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10805000/0000049472.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: SRC-5409（保健師助産師看護師法、GOV_JP）第28条の2およびSRC-5427（看護師等の人材確保の促進に関する法律、GOV_JP）第5条による
  uncertainty: 出典内の位置は、ガイドライン改訂版の「新人看護職員研修ガイドラインの基本的な考え方」（目的、ガイドライン検討の経緯における平成22年4月1日からの努力義務化の記載、ガイドラインの構成と使い方における1年以内の到達目標の記載）による。新人看護職員の定義（免許取得後に初めて就労する看護職員）は同ガイドラインの基本的な考え方による。本人の努力義務は保健師助産師看護師法第28条の2、病院等の開設者等の努力義務は看護師等の人材確保の促進に関する法律第5条第1項であり、いずれもe-Gov現行法で条文を確認した。医師の臨床研修（医師法第16条の2）・歯科医師の臨床研修（歯科医師法第16条の2）が「受けなければならない」とする必修であることとの対比は、各法の条文の文言による。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-095
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 臨床検査技師になるには、指定された学校または養成所で3年以上必要な知識と技能を学んで国家試験に合格し免許を受ける必要があり、2021年10月1日施行の改正では採血や検体採取、生理学的検査とそれらに関連する厚生労働省令で定める行為が医師または歯科医師の具体的な指示の下で行える業務として位置づけられ、これとは別に指定規則の改正で総単位数が95単位から102単位へ、臨地実習が7単位から12単位へ引き上げられ2022年4月の入学生から適用された
    condition:
      region: 日本
      対象: 臨床検査技師の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5416
    source: 臨床検査技師等に関する法律（昭和33年法律第76号）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/333AC1000000076
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: SRC-5417（臨床検査技師学校養成所指定規則、法令）による
  uncertainty: "受験資格は第15条第1号（指定学校・養成所で3年以上修得）、免許は第3条、業務の関連行為は第20条の2第1項第4号で確認した。2021年改正は令和3年法律第49号によるもので施行は2021年10月1日。指定規則の改正は令和3年文部科学省・厚生労働省令第2号（2021年3月31日公布、2021年4月1日施行）で、総単位数と臨地実習の変更は厚生労働省の公布通知と現行指定規則別表第一（合計102単位、臨地実習12単位）で確認し、適用は検討会報告書概要の2022年4月の入学生からとした。業務拡大の具体的な行為の内訳は施行令・施行規則に委ねられており本カードでは法律レベルの範囲にとどめた。2026-11-24にe-Gov現行法で確認。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-096
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 診療放射線技師になるには、指定された学校または養成所で3年以上必要な知識と技能の修習を終えて国家試験に合格し免許を受ける必要があり、2021年10月1日施行の改正では放射性同位元素を人体内に挿入して行う照射や画像診断装置を用いた検査に関連する行為、出張して超音波診断装置を用いた検査を行う場合が業務として広げられ、これとは別に指定規則の改正で総単位数が95単位から102単位へ引き上げられ2022年4月の入学生から適用された
    condition:
      region: 日本
      対象: 診療放射線技師の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5418
    source: 診療放射線技師法（昭和26年法律第226号）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/326AC0100000226
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: SRC-5419（診療放射線技師学校養成所指定規則、法令）による
  uncertainty: "受験資格は第20条第1号（指定学校・養成所で3年以上修習）、免許は第3条、画像診断装置を用いた検査等の業務は第24条の2、病院・診療所以外の場所での出張による超音波検査は第26条第2項第4号で確認した。2021年改正は令和3年法律第49号によるもので施行は2021年10月1日で、放射性同位元素を体内に挿入する照射の追加は厚生労働省通知（医政発0709第7号）でも確認した。指定規則の正式名称は診療放射線技師学校養成所指定規則で、改正は令和3年文部科学省・厚生労働省令第1号（2021年3月31日公布、2021年4月1日施行）、現行別表第一の合計は102単位で、適用時期2022年4月の入学生からは厚生労働省のカリキュラム等改善検討会の記録で確認した。2026-11-24にe-Gov現行法で確認。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-097
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 管理栄養士の免許は栄養士の免許を前提とする仕組みで、4年制の管理栄養士養成施設を卒業した者は実務経験なしに国家試験を受けられ、2年制・3年制・4年制の栄養士養成施設を卒業した者はそれぞれ3年以上・2年以上・1年以上の栄養の指導の実務を経て受験でき、試験は毎年少なくとも1回行われ合格者に厚生労働大臣が免許を与える
    condition:
      region: 日本
      対象: 管理栄養士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5423
    source: 栄養士法（昭和22年法律第245号）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/322AC0000000245
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: "栄養士の免許は第2条第1項（指定養成施設で2年以上修得し都道府県知事が与える）、管理栄養士の免許は第2条第3項（国家試験合格者に厚生労働大臣が与える）、国家試験は第5条の2（毎年少なくとも1回）、受験資格の4経路は第5条の3第1号から第4号で確認した。臨地実習の単位数や実施方法は栄養士法自体には定めがなく施行令・施行規則と厚生労働省通知に委ねられているため、主張文には含めなかった。2026-11-24にe-Gov法令APIで現行法を確認。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-098
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 歯科衛生士になるには、文部科学大臣指定の歯科衛生士学校または都道府県知事指定の歯科衛生士養成所を卒業して国家試験に合格し免許を受ける必要があり、指定の基準では修業年限は3年以上とされ、業務は歯科医師の指導の下での歯科予防処置、歯科診療の補助、歯科保健指導の3つを柱とする
    condition:
      region: 日本
      対象: 歯科衛生士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5424
    source: 歯科衛生士法（昭和23年法律第204号）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/323AC0000000204
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: SRC-5425（歯科衛生士学校養成所指定規則、法令）による
  uncertainty: "業務の3本柱は第2条第1項（歯科予防処置として付着物・沈着物の除去と薬物塗布）、第2条第2項（歯科診療の補助）、第2条第3項（歯科保健指導）で確認し、免許は第3条、受験資格は第12条第1号・第2号で確認した。修業年限3年以上は法律自体ではなく歯科衛生士学校養成所指定規則第2条第2号の指定基準であるため、その旨を区別して書いた。指定規則の現行別表では臨地実習は20単位、合計93単位であることもあわせて確認した。2026-11-24にe-Gov法令APIで現行法を確認。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-099
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 救急救命士になるには、指定された学校または養成所で所定の期間必要な知識と技能を修得するなどの受験資格を満たして国家試験に合格し免許を受ける必要があり、救急救命処置は医師の指示の下で重度傷病者に行う緊急に必要な処置で、2021年10月1日施行の改正で実施できる場が搬送中に加えて病院や診療所に到着してから入院するまでの間にも広がり、病院等に勤務する者がその場で処置を行うにはあらかじめ所定の研修を受ける必要がある
    condition:
      region: 日本
      対象: 救急救命士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5426
    source: 救急救命士法（平成3年法律第36号）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/403AC0000000036
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: "救急救命処置の定義と実施できる場の拡大は第2条第1項、免許は第3条、受験資格の経路は第34条第1号から第5号（経路により養成所等での修得期間が2年以上・1年以上・6月以上など異なるため主張文では所定の期間とした）、業務の場所の制限と病院到着後の例外は第44条第2項、病院等勤務者の事前研修は第44条第3項で確認した。2021年改正は令和3年法律第49号によるもので施行は2021年10月1日。養成教育自体の指定規則改正とその適用入学年度は一次資料で確認できなかったため、§2-9に従い主張文には業務の場の拡大だけを書き、養成課程の見直しは書かなかった。2026-11-24にe-Gov現行法で確認。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-100
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 臨床工学技士になるには、臨床工学技士国家試験に合格し、厚生労働大臣の免許を受けなければならない。国家試験の基本的な受験資格は、大学に入学できる者で、文部科学大臣が指定した学校または都道府県知事が指定した臨床工学技士養成所において、3年以上、臨床工学技士として必要な知識と技能を修得したことである。
    condition:
      region: 日本
      対象: 臨床工学技士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5450
    source: 臨床工学技士法（昭和62年法律第60号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/362AC0000000060
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置は第3条（免許）と第14条第1号（受験資格の基本ルート）。e-Gov現行法（2026-11-24確認）による。第14条にはこのほか指定科目を修めた者向けの短縮ルート（第2号・第3号・第4号）と外国養成校卒業者の認定ルート（第5号）があるが、本カードは基本ルートのみを扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-101
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: "業務範囲については、2021年の改正（令和3年法律第49号、令和3年10月1日施行）で、臨床工学技士が診療の補助として行える業務に、生命維持管理装置を用いた治療に関連する医療用装置の操作（医師の具体的な指示を受けて行うものに限る）が加わった。令和7年4月1日前に免許を受けた者と、同日前に国家試験に合格して同日以後に免許を受けた者が、この追加された業務を行おうとするときは、あらかじめ厚生労働大臣が指定する研修を受けなければならない。養成教育については、これとは別に、養成課程の総単位数が93単位から101単位以上へ引き上げられ、新しいカリキュラムは修業年限3年以上の課程では令和5年度入学生から適用された。"
    condition:
      region: 日本
      対象: 臨床工学技士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5450
    source: 臨床工学技士法（昭和62年法律第60号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/362AC0000000060
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: SRC-5451（厚生労働省・臨床工学技士学校養成所カリキュラム等改善検討会報告書、GOV_JP）による
  uncertainty: "出典内の位置は第37条（業務）と、令和3年法律第49号による改正の附則第15条（研修の経過措置）。業務範囲の拡大と養成教育の見直しは別の事実として分けて書いた。総単位数93単位から101単位以上への引き上げは、SRC-5451の報告書本文（第2の2（1）「総単位数は、現行の93単位に必要な教育内容を追加し、101単位以上とする」）で直接確認したもので、理学療法士・作業療法士の指定規則改正の数字の取り違えではない。研修について令和7年4月1日は受講の期限ではなく、対象者を分ける日付である（この日より前に免許を受けた者等が追加業務を行うには事前の研修が必要）。指定規則の改正省令は「臨床工学技士学校養成所指定規則の一部を改正する省令（令和4年文部科学省・厚生労働省令第1号）」で令和4年3月31日公布・同年4月1日施行であり、新カリキュラムの適用開始（3年以上の課程は令和5年度入学生から）は厚生労働省の同省令の施行通知（令和4年3月31日）で確認した。改正省令そのものの附則の原文はe-Govの混雑で直接開けなかったため、適用年度は施行通知による確認であることをここに残す。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-102
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 言語聴覚士になるには、言語聴覚士国家試験に合格し、厚生労働大臣の免許を受けなければならない。国家試験の基本的な受験資格は、大学に入学できる者で、文部科学大臣が指定した学校または都道府県知事が指定した言語聴覚士養成所において、3年以上、言語聴覚士として必要な知識と技能を修得したことである。このほか、大学等で厚生労働大臣の指定する科目を修めた者には、養成所での修得期間が1年以上または2年以上で足りる短縮ルートがある。
    condition:
      region: 日本
      対象: 言語聴覚士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5452
    source: 言語聴覚士法（平成9年法律第132号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/409AC0000000132
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置は第3条（免許）と第33条（受験資格。第1号が3年以上の基本ルート、第2号が2年以上修業し指定科目を修めた者の1年以上ルート、第3号が1年以上修業し指定科目を修めた者の2年以上ルート、第4号が大学で指定科目を修めて卒業した者）。e-Gov現行法（令和7年8月16日時点の版、2026-11-24確認）による。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-103
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 視能訓練士になるには、視能訓練士国家試験に合格し、厚生労働大臣の免許を受けなければならない。国家試験の基本的な受験資格は、大学に入学できる者で、文部科学大臣が指定した学校または都道府県知事が指定した視能訓練士養成所において、3年以上、視能訓練士として必要な知識と技能を修得したことである。
    condition:
      region: 日本
      対象: 視能訓練士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5453
    source: 視能訓練士法（昭和46年法律第64号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/346AC0000000064
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置は第3条（免許）と第14条第1号（受験資格の基本ルート）。現行法（2026-11-24確認）による。第14条にはこのほか、大学等で2年以上修業し指定科目を修めた者の1年以上ルート（第2号）と外国養成校卒業者の認定ルート（第3号）があるが、本カードは基本ルートのみを扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-104
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 歯科技工士になるには、歯科技工士国家試験に合格して免許を受ける必要があり、国家試験は、文部科学大臣が指定した歯科技工士学校を卒業した者、または都道府県知事が指定した歯科技工士養成所を卒業した者などが受けることができる。指定の基準では、学校・養成所の修業年限は2年以上と定められている。これは、このバッチで確認した臨床工学技士・言語聴覚士・視能訓練士の基本ルートがいずれも3年以上であるのと比べて短い。
    condition:
      region: 日本
      対象: 歯科技工士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5454
    source: 歯科技工士法（昭和30年法律第168号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/330AC0000000168
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: SRC-5458（歯科技工士学校養成所指定規則、GOV_JP）による
  uncertainty: "出典内の位置は歯科技工士法第3条（免許）と第14条（受験資格。第1号が指定学校の卒業者、第2号が指定養成所の卒業者）。修業年限2年以上はSRC-5458の第2条第2号（指定基準）による。e-Gov現行法（令和7年6月1日施行の版、2026-11-24確認）による。「他の職種より短い」という比較は、依頼文の指示により、このバッチで確認した臨床工学技士（ME-100）・言語聴覚士（ME-102）・視能訓練士（ME-103）の基本ルート（いずれも3年以上）に限って書いた。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-105
  domain: ME
  subdomain: アセスメント
  assertion:
    plain_statement_ja: 歯科技工士国家試験は、かつては養成施設の所在地の都道府県知事がそれぞれ行っていたが、医療介護総合確保推進法による歯科技工士法の改正が平成27年4月1日に施行され、国（厚生労働大臣）が実施する全国統一の国家試験となった。指定試験機関には一般財団法人歯科医療振興財団が平成27年6月1日に指定され、全国統一となった最初の試験は平成28年2月28日に実施された。
    condition:
      region: 日本
      対象: 歯科技工士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5454
    source: 歯科技工士法（昭和30年法律第168号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/330AC0000000168
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: SRC-5461（厚生労働省・第2回歯科技工士の養成・確保に関する検討会資料、GOV_JP）による
  uncertainty: "現行法では試験は厚生労働大臣が行うものとされ、指定試験機関・指定登録機関の制度が置かれている。改正の経緯（平成27年4月1日施行、改正法は地域における医療及び介護の総合的な確保を推進するための関係法律の整備等に関する法律＝平成26年法律第83号）、指定試験機関の指定日（平成27年6月1日）と名称（一般財団法人歯科医療振興財団）、最初の全国統一試験の実施日（平成28年2月28日）はSRC-5461と、厚生労働省医政局長通知（平成27年4月1日、医政発0401第9号）で確認した。指定試験機関の名称は一次資料で確認できたため主張文に書いた。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-106
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 義肢装具士になるには、義肢装具士国家試験に合格し、厚生労働大臣の免許を受けなければならない。国家試験の受験資格の基本となる経路は、大学に入学することができる者で、文部科学大臣が指定した学校または都道府県知事が指定した義肢装具士養成所において、3年以上、義肢装具士として必要な知識及び技能を修得した者である。このほか、大学や高等専門学校等で1年（高等専門学校では4年）以上修業し厚生労働大臣の指定する科目を修めた者が指定の学校・養成所で2年以上修得する経路と、義肢及び装具の製作に係る技能検定に合格した者（厚生労働省令で定める者に限る）が指定の学校・養成所で1年以上修得する経路があり、いずれも指定された学校・養成所での教育を経る仕組みになっている。
    condition:
      region: 日本
      対象: 義肢装具士の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5455
    source: 義肢装具士法（昭和62年法律第61号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/362AC0000000061
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置は、免許の要件が第3条、国家試験の実施が第11条、受験資格が第14条（第1号が3年以上の基本経路、第2号が科目修得後の2年以上の経路、第3号が技能検定合格者の1年以上の経路、第4号が外国の学校・免許の認定経路）。2026年11月24日に e-Gov 法令検索の現行法（法令APIでも法令番号を確認）で条文を確認した。外国の学校・免許の経路（第4号）は主張文の中心ではないため触れていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-107
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 柔道整復師の免許は、柔道整復師国家試験に合格した者に対して厚生労働大臣が与える。国家試験は、大学に入学することができる者で、3年以上、文部科学省令・厚生労働省令で定める基準に適合するものとして文部科学大臣の指定した学校または都道府県知事の指定した柔道整復師養成施設において、解剖学、生理学、病理学、衛生学その他柔道整復師となるのに必要な知識及び技能を修得した者でなければ受けることができない。指定の基準では、修業年限は3年以上とされている。
    condition:
      region: 日本
      対象: 柔道整復師の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5456
    source: 柔道整復師法（昭和45年法律第19号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/345AC1000000019
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: SRC-5459（柔道整復師学校養成施設指定規則、法令）による
  uncertainty: 出典内の位置は、免許が第3条、国家試験の実施が第10条、受験資格が第12条第1項。指定基準の修業年限（3年以上）は柔道整復師学校養成施設指定規則（SRC-5459）第2条第2号で確認した。2026年11月24日に e-Gov 法令検索の現行法（法令APIでも両法令の番号と正式名称を確認）で条文を確認した。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-108
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: あん摩マッサージ指圧師、はり師、きゅう師の免許は、それぞれの国家試験に合格した者に対して厚生労働大臣が与える。免許の要件となる学修は、大学に入学することができる者で、3年以上、文部科学省令・厚生労働省令で定める基準に適合するものとして認定された学校または養成施設において、解剖学、生理学、病理学、衛生学その他必要な知識及び技能を修得することである。学校は文部科学大臣が認定し、養成施設は施設の種類に応じて厚生労働大臣または都道府県知事が認定する仕組みで、他の多くの医療関係職種で用いられる「指定」ではなく「認定」の語が法律上用いられている。認定の基準では、修業年限は3年以上とされている。
    condition:
      region: 日本
      対象: あん摩マッサージ指圧師・はり師・きゅう師の学生
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5457
    source: あん摩マツサージ指圧師、はり師、きゆう師等に関する法律（昭和22年法律第217号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/322AC0000000217
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: SRC-5460（あん摩マツサージ指圧師、はり師及びきゆう師に係る学校養成施設認定規則、法令）による
  uncertainty: 出典内の位置は、免許の要件と認定の仕組みが第2条第1項（学校は文部科学大臣の認定、あん摩マッサージ指圧師を含む養成施設は厚生労働大臣の認定、はり師・きゅう師のみの養成施設は都道府県知事の認定）、免許の登録と免許証の交付が第3条の2・第3条の3。認定基準の修業年限（3年以上）は認定規則（SRC-5460）第2条第2号で確認した。2026年11月24日に e-Gov 法令検索の現行法（法令APIでも両法令の番号と正式名称を確認）で条文を確認した。著しい視覚障害のある者を対象とする特例の経路（第18条の2）は主張文に含めていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-109
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 准看護師は、保健師・助産師・看護師とは免許と試験の担い手が異なる職種である。准看護師になろうとする者は、准看護師試験に合格し、都道府県知事の免許を受けなければならないとされ、准看護師試験は厚生労働大臣の定める基準に従い都道府県知事が毎年少なくとも1回行う（保健師・助産師・看護師の国家試験は厚生労働大臣が行い、免許も厚生労働大臣が与える）。受験資格の基本となる経路は、文部科学大臣の指定した学校において2年の看護に関する学科を修めた者、または都道府県知事の指定した准看護師養成所を卒業した者であり、指定の基準では准看護師学校養成所の修業年限は2年以上とされている。
    condition:
      region: 日本
      対象: 看護学生
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
    corroboration: SRC-5408（保健師助産師看護師学校養成所指定規則、法令）による
  uncertainty: "出典内の位置は、准看護師の定義が第6条、准看護師の免許が第8条、試験の実施主体が第18条（保健師・助産師・看護師の国家試験は厚生労働大臣、准看護師試験は都道府県知事が厚生労働大臣の定める基準に従い毎年少なくとも1回実施）、受験資格が第22条（第1号が指定学校で2年の学科、第2号が都道府県知事指定の准看護師養成所の卒業）。修業年限（2年以上）は、依頼文§2-6の指定どおり指定規則（SRC-5408）で確定させたもので、第5条（准看護師学校養成所の指定基準）第2号に「修業年限は、二年以上であること」とあり、教育内容は同条第3号で別表四以上とされる。2026年11月24日に e-Gov 法令検索の現行法で両法令の条文を確認した。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-110
  domain: ME
  subdomain: 横断
  assertion:
    plain_statement_ja: 医師・歯科医師・薬剤師・看護師の養成で求められる資質・能力は、各職種のコア・カリキュラムに示されているが、その構成はそろっていない。医学・歯学（令和4年度改訂版）では共通の10項目（プロフェッショナリズム、総合的に患者・生活者をみる姿勢、生涯にわたって共に学ぶ姿勢、科学的探究、専門知識に基づいた問題解決能力、情報・科学技術を活かす能力、患者ケアのための診療技能、コミュニケーション能力、多職種連携能力、社会における医療の役割の理解）が掲げられ、薬学（令和4年度改訂版）では医学・歯学と共通の9項目に薬学独自の「薬物治療の実践的能力」を加えた10項目となっている。これに対し看護学では、独自の9項目（プロフェッショナリズム、看護学の知識と看護実践、根拠に基づいた課題対応能力、コミュニケーション能力、保健・医療・福祉における協働、ケアの質と安全の管理、社会から求められる看護の役割の拡大、科学的探究、生涯にわたって研鑽し続ける姿勢）が掲げられている。なお、医・歯・薬の文書は令和4年度改訂版であるのに対し、看護学の文書は平成29年10月のものであり、比較に当たっては文書の時点がそろっていないことに注意が要る。
    condition:
      region: 日本
      対象: 教育者
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
    corroboration: SRC-5404（文部科学省 薬学教育モデル・コア・カリキュラム（令和4年度改訂版）、GOV_JP）および SRC-5407（文部科学省 大学における看護系人材養成の在り方に関する検討会 看護学教育モデル・コア・カリキュラム、GOV_JP）による
  uncertainty: "出典内の位置は、医学・歯学の10項目が第1章、薬学の10項目が大項目A、看護学の9項目が「看護系人材として求められる基本的な資質・能力」の節。記載は登録済みの第1陣カード（ME-001・ME-072・ME-075・ME-078）の内容と一致させた（依頼文§2-10）。薬学で医学・歯学と異なるのは「患者ケアのための診療技能」に当たる位置の「薬物治療の実践的能力」のみである。看護学の文書は平成29年10月で、令和4年度改訂版の医・歯・薬とは策定時点が異なるため、その点を主張文にも明記した。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-111
  domain: ME
  subdomain: 横断
  assertion:
    plain_statement_ja: 日本の医療関係職種の養成は、職種ごとに根拠となる法律があり、その法律で定められた指定（あん摩マッサージ指圧師・はり師・きゅう師では認定）の学校・養成施設で必要な知識及び技能を修得し、試験に合格して免許を受けるという流れを共通の骨格とする。厚生労働省の「資格・試験情報」（2026年11月24日確認時点では令和9年実施の試験日程を掲載）には、医師、歯科医師、保健師、助産師、看護師、薬剤師をはじめ、診療放射線技師、臨床検査技師、理学療法士、作業療法士、臨床工学技士、義肢装具士、歯科衛生士、歯科技工士、救急救命士、あん摩マッサージ指圧師、はり師、きゅう師、柔道整復師、言語聴覚士、管理栄養士などの国家試験が並んでいる。違いもある。修業年限は職種で異なり、例えば義肢装具士、柔道整復師、あん摩マッサージ指圧師・はり師・きゅう師では3年以上、准看護師では2年以上である。また、医師のように免許を受けた後に診療に従事するための臨床研修が法律で義務づけられている職種がある一方、そうした卒後研修の義務づけのない職種もある。さらに、免許と試験の担い手も一様ではなく、准看護師では免許も試験も都道府県知事が担う。
    condition:
      region: 日本
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5428
    source: 厚生労働省. 資格・試験情報（医療、医薬品、健康、食品衛生関連の国家試験一覧、令和9年実施試験の日程を掲載、2026年11月24日確認）
    doi: null
    pmid: null
    pmcid: null
    url: http://www.mhlw.go.jp/general/sikaku
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: "主出典は厚生労働省ホームページの「資格・試験情報」で、医療分野の国家試験の一覧と実施主体（厚生労働省の所管部局・指定試験機関）を示すページであり、時点は2026年11月24日確認（令和9年実施試験の日程を掲載している版）である（依頼文§2-11の指定どおり、資料名と時点を明示した）。共通の流れと修業年限の数値（3年以上・2年以上）は、本バッチで各根拠法の現行条文を確認した範囲（義肢装具士法第14条、柔道整復師法第12条、あん摩マツサージ指圧師、はり師、きゆう師等に関する法律第2条、保健師助産師看護師法第8条・第18条・第22条）に限った。医師の臨床研修の義務づけは登録済みの ME-004（医師法第16条の2第1項、2年以上）による。全ての医療関係職種の修業年限と卒後研修の有無を網羅的に確認したわけではない。"
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: ME-112
  domain: ME
  subdomain: 横断
  assertion:
    plain_statement_ja: 国家試験の出題基準は、厚生労働省が職種ごとに公表する文書で、その職種が医療の現場に第一歩を踏み出す際に少なくとも備えているべき基本的な知識及び技能を具体的な項目で示し、国家試験の妥当な内容や範囲と適切な水準を確保する目的で作成される仕組みである。保健師・助産師・看護師については「保健師助産師看護師国家試験出題基準 令和5年版」があり、令和5年に実施された第109回保健師国家試験、第106回助産師国家試験および第112回看護師国家試験から適用された。この令和5年版の改定概要には、国家試験制度の改善を検討した部会の報告で、教育内容を踏まえて出題基準の体系や項目を見直すことが提言されたことを受けて改定が行われたことが書かれている。出題基準は職種ごとに置かれ、歯科医師や薬剤師にもそれぞれの国家試験出題基準があるが、版や改定の時期は職種ごとに異なる。
    condition:
      region: 日本
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5410
    source: 厚生労働省. 保健師助産師看護師国家試験出題基準（令和5年版）. 令和4年3月
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10803000/000958440.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: SRC-5403（歯科医師国家試験出題基準、GOV_JP）および SRC-5406（薬剤師国家試験出題基準、GOV_JP）による
  uncertainty: "出典内の位置は、令和5年版の「改定概要」および「保健師助産師看護師国家試験出題基準とは」の節（出題基準の目的と位置づけ）、適用開始の回次は厚生労働省の改定通知（令和4年3月28日）による。依頼文§2-1への対応として、「出題基準はコア・カリキュラムや指定規則の見直しと連動して改定されることが多い」という一般的な解釈表現は主張文に入れていない。教育内容との関係については、令和5年版の改定概要自体に書かれている範囲（制度改善検討部会の報告が教育内容を踏まえた見直しを提言し、それを受けて改定したこと）に限って記載した。歯科医師（令和5年版があることを厚生労働省資料で確認）と薬剤師の出題基準の現行版の版次・改定時期の詳細は本カードでは確認しておらず、主張文では「職種ごとにあり、版や改定の時期は異なる」にとどめた。"
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

全29件とも、依頼文 §1 の指定により kokushi・core_curriculum は null（空欄）とした。対応表は作成していない。

## §4 未解決事項

1. **ME-084**：CBT の問題数（6ブロック合計320問）は主出典（SRC-5422 部会意見）には記載がなく、裏づけの機構要綱（SRC-5421）で確認した範囲に限って主張文に入れ、uncertainty に明記した。機構要綱の単独公表ページは特定できず（厚生労働省の部会資料として掲載された版で確認）、SRC-5421・SRC-5429 ともサイト上でライセンス表示を確認できなかった。
2. **ME-086**：総問題数は令和3年度版の出題基準そのものでは確認できなかったため主張文に入れていない。令和5年版の歯科医師国家試験出題基準が別途公表されている点は、登録側での版の扱いの確認事項として残す（本カードは依頼文の配分どおり令和3年度版を主出典とした）。
3. **ME-092**：指定規則の別表一・別表二には括弧内の数値（保健師課程の合計28単位、助産師課程の合計30単位など）も併記されているが、その適用場面は省令本文から読み取れなかったため、括弧外の数値（各31単位）のみを用い、uncertainty に明記した。
4. **ME-093**：試験時間の延長自体は厚生労働省の制度改善検討部会の報告書（令和3年3月）と同部会における厚生労働省の説明（令和8年1月）で確認したが、保健師国家試験分の受験者留意事項の原典は直接開けなかった（助産師分の留意事項と施行紹介資料で照合）。厳密には保健師分の原典照合が残る。
5. **ME-095・ME-096**：指定規則の改正（令和3年文部科学省・厚生労働省令第2号／第1号）による適用入学年度（2022年4月入学生から）は、公布通知自体には明記がなく、厚生労働省の検討会報告書概要・議事録による確認である。
6. **ME-097**：臨地実習の単位数・実施方法は栄養士法には定めがなく、厚生労働省・文部科学省の実習要領（平成14年通知）レベルのため、本カードの主張には含めなかった。必要になれば通知を別 SRC として登録し、別カード化できる。
7. **ME-099**：養成教育の指定基準の改正と適用入学年度は、一次資料で確認できなかったため、依頼文 §2-9 に従い主張文には業務の場の拡大だけを書いた。
8. **ME-101**：改正省令（臨床工学技士学校養成所指定規則の一部を改正する省令、令和4年文部科学省・厚生労働省令第1号）そのものの附則原文は e-Gov で直接開けなかったため、新カリキュラムの適用入学年度の確認は同省令の施行通知（令和4年3月31日）による。この留保はカードの uncertainty にも残した。
9. **ME-111**：全ての医療関係職種の修業年限・卒後研修の義務づけの有無を網羅する厚生労働省の単一資料は確認できなかったため、主張文は本バッチで根拠法を確認した範囲の例示にとどめた。
10. **ME-112**：薬剤師国家試験出題基準の現行版の正式な版次・公表時期は本バッチでは確定させていない（改定案の資料のみ確認）。主張文では「職種ごとにあり、版や改定の時期は異なる」にとどめた。

## §5 引き継ぎメモ

- 新規出典は31件（法令19件・省庁資料9件・実施機関資料3件）。既存出典の再利用は9件（SRC-5101・5400・5404・5405・5406・5407・5408・5409・5410）。
- 分割案の仮番号からの付け直し（第1陣で SRC-5415 が「新薬剤師国家試験について」に使われたための衝突回避）：
  - 臨床検査技師等に関する法律：分割案 SRC-5415 → SRC-5416
  - 臨床検査技師学校養成所指定規則：分割案では法律と一括 → SRC-5417（1法令＝1 SRC のため分離）
  - 診療放射線技師法：分割案 SRC-5416 → SRC-5418
  - 診療放射線技師学校養成所指定規則：分割案では法律と一括 → SRC-5419（分離）
  - 栄養士法：分割案 SRC-5417 → SRC-5423
  - 歯科衛生士法：分割案 SRC-5418 → SRC-5424
  - 歯科衛生士学校養成所指定規則：分割案では法律と一括 → SRC-5425（分離）
  - 救急救命士法：分割案 SRC-5419 → SRC-5426
  - 歯科技工士学校養成所指定規則：追加分割案では SRC-5454 と一括 → SRC-5458（分離）
  - 柔道整復師学校養成施設指定規則：追加分割案では SRC-5456 と一括 → SRC-5459（分離）
  - あん摩マツサージ指圧師、はり師及びきゆう師に係る学校養成施設認定規則：追加分割案では SRC-5457 と一括 → SRC-5460（分離）
  - 歯科技工士の養成・確保に関する検討会資料：新規に SRC-5461 を割り当てた。
  - 実務実習ガイドライン：新規に SRC-5431 を割り当てた（§6 の修正3を参照）。
- 本ファイルで使わなかった SRC-54xx の番号：SRC-5414（分割案で理学療法士・作業療法士の養成施設指導ガイドライン用に確保されたが、本バッチでは使用しなかった）、SRC-5432〜5449、SRC-5462〜5499。SRC-5412・5413・5415 は第1陣で登録済みの出典であり、本バッチでは使用していない。
- ME-110 の資質・能力の項目名は、登録済みの ME-001・ME-072・ME-075・ME-078 の記載と一致させた（検証は §6）。
- ME-111 の主出典（SRC-5428）は厚生労働省ホームページの「資格・試験情報」ページであり、時点（2026年11月24日確認、令和9年実施試験の日程を掲載）を書誌と主張文に明記した。ページの内容は更新されうるため、取り込み時に時点の扱いを確認されたい。


## §6 納品前検証の記録（2026-11-24）

### 検証表

| 項目 | 方法 | 結果 |
|---|---|---|
| 基準の確定 | 作業前に hm-cmed/cleanroom-facts 最新版（コミット 208dce0d）を取得し、第1陣 ME-072〜083 と出典 SRC-5400〜5415 の登録を確認 | 登録済みを確認。マスターの最大番号は SRC-5415 |
| 書誌・条文の原典照合 | 法令は全件 e-Gov 法令検索の現行法（法令APIを含む）で条番号と内容を確認。省庁資料は公表 PDF・ページを実際に開いて確認 | 各カードの uncertainty に条番号・該当箇所を記録 |
| ME-101 の単位数（依頼文 §2-5） | 臨床工学技士の検討会報告書（SRC-5451）の本文で直接確認 | 報告書第2の2(1) に「総単位数は、現行の93単位に必要な教育内容を追加し、101単位以上とする」と明記。理学療法士・作業療法士の数字の取り違えではない |
| ME-101 の研修の線引き・改正省令名・適用年度（§2-5） | 改正法（令和3年法律第49号）の附則第15条、改正省令の施行通知（令和4年3月31日）で確認 | 令和7年4月1日は受講期限ではなく対象者を分ける日付として記載。省令名は「臨床工学技士学校養成所指定規則の一部を改正する省令（令和4年文部科学省・厚生労働省令第1号）」。適用は3年以上の課程で令和5年度入学生から（省令附則の原文は未確認のため §4-8 に留保） |
| ME-093 の試験時間延長（§2-2） | 厚生労働省の制度改善検討部会報告書（令和3年3月31日）と同部会における厚生労働省の説明（令和8年1月19日）で確認 | 「令和5年に実施した試験から延長」が明示されていたため主張文に記載。現行は午前・午後各1時間20分（第109回助産師国家試験受験者留意事項で確認） |
| ME-089・090 の問題数・課題数（§2-3） | 文部科学省・厚生労働省の資料で確認を試みた | 省庁資料では確認できず、主張文に入れていない（センター資料の値のみ確認メモ相当として各カードの uncertainty に経緯を記録） |
| ME-091 の週数（§2-4） | 文部科学省の薬学教育のページに掲載された実務実習ガイドライン（SRC-5431）第2章で確認 | 病院・薬局各11週・計22週間を確認し主張文に記載。コアカリ本文自体に週数の記載はないことを uncertainty に明記 |
| ME-109 の修業年限（§2-6） | 指定規則（SRC-5408）第5条第2号で確定 | 「修業年限は、二年以上であること」を確認。受験資格は保健師助産師看護師法第22条で確認 |
| ME-104 の比較の範囲（§2-7） | 本バッチで確認した職種に限定 | 比較対象は臨床工学技士・言語聴覚士・視能訓練士（いずれも基本ルート3年以上）に限定して記載 |
| ME-088 の主出典（§2-8） | 厚生労働省の検討会資料（SRC-5430）を主出典とし、専門医機構の資料（SRC-5429）は裏づけに限定 | 機構の設立年（2018年）と基本領域10領域は厚労省資料で確認。評価・認定実施中の8領域は機構概報で確認した範囲として uncertainty に明記 |
| 業務拡大と養成見直しの分離（§2-9） | ME-095・096・099・101 で個別に確認 | ME-095・096 は指定規則の改正（令和3年の改正で総単位数95→102）を確認し別事実として記載。ME-099 は養成側が確認できず業務の拡大のみ記載。ME-101 は文を分けて記載 |
| ME-110 の整合（§2-10） | 登録済み ME-001・ME-072・ME-075・ME-078 の項目名と機械照合 | 医・歯の10項目、看護学の9項目、薬学の「薬物治療の実践的能力」が登録済みカードと一致することを確認。時点のずれ（看護学のみ平成29年）を主張文に明記 |
| ME-111 の主出典と時点（§2-11） | 厚生労働省「資格・試験情報」を SRC-5428 として登録し、資料名と確認時点を書誌・主張文に明記 | 都道府県知事が免許・試験を担う職種（准看護師）も確認範囲で記載 |
| 解釈的表現の排除（§2-1） | ME-086・ME-112 の主張文を点検 | 「コアカリの改訂と歩調」等の表現は主出典に裏づけがなく、両カードとも主張文に入れていない。ME-112 は令和5年版の改定概要自体に書かれた範囲に限定 |
| 件数・番号の照合 | 最終ファイルで機械照合 | カード29件（ME-084〜112、欠番なし）。出典表40行（既存9・新規31）で、カードの provenance が参照する SRC は全て出典表にあり、出典表の全行がカードから参照されている |
| 形式の検証 | 最終ファイルの YAML をパースして検証 | YAML ブロックは1つ。全カードに region（日本）と対象があり、curriculum は全件 null、assertion は対象の形、アンカー・エイリアスなし |

### 組み立て・検証時に行った修正（before → after）

1. **ME-091 の裏づけ出典の新設**：before＝週数（各施設11週）の根拠資料が uncertainty の文章内のみで、出典として登録されていなかった。after＝「臨床における実務実習に関するガイドライン」（薬学教育協議会、令和5年12月）を SRC-5431 として新規登録し、ME-091 の corroboration を null から「SRC-5431（…）による」に変更した。
2. **ME-089・ME-090 の裏づけの追加**：before＝corroboration は SRC-5420 のみ。after＝SRC-5405（薬剤師法）を追加し、「薬剤師法に共用試験に関する規定は置かれていない」ことの根拠を、第1陣の ME-083 と同じ作りで明示した。
3. **ME-112 の uncertainty の文の削除**：before＝末尾に「（SRC-5403・SRC-5406の書誌は組み立て側で補う前提で番号のみ言及）」という作業手続きの文があった。after＝同部分を削除した（両出典は §1 出典表に記載済み）。
4. **法令書誌の数字表記の統一**：before＝臨床検査技師等に関する法律ほか8件の法令書誌が漢数字表記（例：昭和三十三年法律第七十六号）。after＝第1陣・出典マスターの表記にそろえて算用数字（例：昭和33年法律第76号）に統一した（出典表とカードの provenance の両方）。
