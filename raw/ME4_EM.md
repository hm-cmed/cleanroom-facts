# 医療者教育（ME）第3弾 EM：ME-054〜061（カード8件）

依頼文（round_ME4_request.md、2026-11-24）に基づく第3弾のうち、EM（教育管理）領域の8枚。決定事項の適用は次のとおり。

- 作業前に取得したレポジトリ：hm-cmed/cleanroom-facts 最新版、コミット `10bd46714ac6120e912b72cdb761af8d32925210`（2026-11-24）。出典マスターと既存 ME カードで DOI・PMID の重複を照合し、本ファイルの新規出典はいずれも未登録であることを確認した。
- subdomain は「教育管理」とした。カリキュラム欄は空欄とした（教育者・大学運営向けの枠組みと制度が主題のため）。法令を出典にする3枚（ME-057・058・060）は、ME-002・ME-004 と同じ作り（legal_basis C、source_class GOV_JP、条文番号を明記）とした。
- **法令の現行形の確認結果（依頼文 §2-1 への回答）**：FD の規定は、大学設置基準の令和4年改正により旧第25条の3から **第11条** に移っている（第1項が教員・事務職員等の研修＝SD、第2項が授業の内容・方法の改善のための組織的な研修及び研究＝FD）。学校教育法施行規則第165条の2（3つの方針）と学校教育法第109条（認証評価）は、依頼文の指定どおり現行条文を確認した。いずれも e-Gov 法令検索の現行法（2026-11-24 取得）で条文を読んだ。
- 新規出典は SRC-5330〜5338 を割り当てた（続く SRC-5339 は未使用）。

## 1. 出典表

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-5330 | Kirkpatrick DL. Techniques for evaluating training programs（4部作）. Journal of the American Society of Training Directors. 1959-1960 | なし | なし | © American Society for Training and Development（CC表示なし） | RESTRICTED | 4段階モデルの原典として周知の連載。書籍版（Evaluating Training Programs）は Berrett-Koehler から刊行 |
| SRC-5331 | Yardley S, Dornan T. Kirkpatrick's levels and education 'evidence'. Med Educ. 2012;46(1):97-106 | 10.1111/j.1365-2923.2011.04076.x | 22150201 | © Wiley（Medical Education、CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（モデルの前提と適用条件の批判的検討）を確認 |
| SRC-5332 | World Federation for Medical Education. Basic Medical Education: WFME Global Standards for Quality Improvement（2020 revision）. WFME; 2020 | なし | なし | © WFME（All rights reserved、CC表示なし） | RESTRICTED | WFME 公式サイト（BME Standards のページ）と基準書本文で、第3版・8つのテーマ・原則基盤型への転換を確認 |
| SRC-5333 | 日本医学教育評価機構. 医学教育分野別評価基準日本版（世界医学教育連盟グローバルスタンダード準拠） | なし | なし | © 一般社団法人 日本医学教育評価機構（CC表示なし） | RESTRICTED | JACME 公式サイトで、機構の設立（2015年）と WFME による認定（2017年3月18日）、現行の日本版基準 Ver.2.36 を確認。WFME 2020年版を反映した後継基準の公表は確認できていない |
| SRC-5334 | 大学設置基準（昭和31年文部省令第28号、現行法） | なし | なし | 法令（著作権法13条により権利の目的とならない） | GOV_JP | e-Gov 法令検索の現行法で第11条（組織的な研修等）を確認。旧第25条の3は令和4年改正で第11条に移行 |
| SRC-5335 | 学校教育法施行規則（昭和22年文部省令第11号、現行法） | なし | なし | 法令（著作権法13条により権利の目的とならない） | GOV_JP | e-Gov 法令検索の現行法で第165条の2（3つの方針）を確認 |
| SRC-5336 | 中央教育審議会大学分科会. 教学マネジメント指針. 令和2年1月22日 | なし | なし | 政府標準利用規約（文部科学省ホームページ） | GOV_JP | 文部科学省の公表資料で、公表日、教学マネジメントの定義、指針の構成（5部）を確認 |
| SRC-5337 | 学校教育法（昭和22年法律第26号、現行法） | なし | なし | 法令（著作権法13条により権利の目的とならない） | GOV_JP | e-Gov 法令検索の現行法で第109条（自己点検・評価と認証評価）を確認 |
| SRC-5338 | Frye AW, Hemmer PA. Program evaluation models and related theories: AMEE Guide No. 67. Med Teach. 2012;34(5):e288-99 | 10.3109/0142159X.2012.668637 | 22515309 | © Taylor & Francis（Medical Teacher、CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（評価モデルと理論的基盤）を確認 |

## 2. 事実カード（YAML）

```yaml
- id: ME-054
  domain: ME
  subdomain: 教育管理
  assertion:
    plain_statement_ja: Kirkpatrick の4段階は、教育プログラムの評価を4つの水準で捉える枠組みである。第1段階は参加者の反応（満足度など）、第2段階は学習の到達（知識・技能・態度の変化）、第3段階は行動の変化（現場での実践の変化）、第4段階は組織の成果（患者アウトカムや組織の業績など）であり、段階が上がるほど評価は難しくなる。もともと産業界の訓練評価のために作られた枠組みで、医学教育の研究評価にも広く使われてきた。一方で、この段階には多くの暗黙の前提が含まれ、単純な教育設計・短期間の転帰・学習者以外の受益者という条件がそろう場合に限って評価の道具として適するという批判的検討があり、医学教育のエビデンスレビューの中でこの条件を満たすものは約5分の1にとどまるとされる。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5330
    source: 'Kirkpatrick DL. Techniques for evaluating training programs. Journal of the American Society of Training Directors. 1959-1960'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © American Society for Training and Development（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: 医学教育での適用の批判的検討は SRC-5331（Yardley S, Dornan T. Med Educ. 2012）で示されている（段階の前提、適用できる条件、該当するレビューは約5分の1）
  uncertainty: 4段階の名称は概念名として記載した。原典は1959〜1960年の雑誌連載（4部作）で、DOI・PMID はなく、書籍版（Evaluating Training Programs, Berrett-Koehler）の ISBN は今回 API で確認できなかったため記載していない。「約5分の1」は裏づけ論文の抄録で確認した数値。4段階を同じ内容で裏づける CC BY の総説は今回の探索では特定できなかった。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-055
  domain: ME
  subdomain: 教育管理
  assertion:
    plain_statement_ja: 世界医学教育連盟（WFME）は、基礎医学教育の質改善のための世界基準を示しており、各国の医学教育の分野別評価はこの基準を参照して行われる。2020年の改訂版（第3版）は、使命と価値、カリキュラム、評価、学生、教員、教育資源、質保証、統轄と管理運営の8つのテーマで構成される。今回の改訂では、各機関や国が自らの文脈に合わせて基準を作ることを認める原則基盤型（principles-based）の考え方に転換し、基準は一律の要求ではなく、各国の基準づくりの雛形と質改善の梃子として位置づけられている。WFME はまた、各国の評価機関を認定する仕組みを持ち、認定された機関による評価が国際的に通用する枠組みになっている。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5332
    source: 'World Federation for Medical Education. Basic Medical Education: WFME Global Standards for Quality Improvement（2020 revision）. WFME; 2020'
    doi: null
    pmid: null
    pmcid: null
    url: https://wfme.org/standards/bme/
    source_license: © WFME（All rights reserved、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 構成（8つのテーマ）と原則基盤型への転換は WFME 公式サイトと基準書の目次で確認した。初版は2003年、第2版は2012年（2015年に改訂）。基準の各項目の文言は転載していない。日本の分野別評価との関係は ME-056 で扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-056
  domain: ME
  subdomain: 教育管理
  assertion:
    plain_statement_ja: 日本の医学教育の分野別評価は、一般社団法人日本医学教育評価機構（JACME）が実施している。JACME は2015年に設立され、2017年に世界医学教育連盟（WFME）から評価機関として認定を受けた。評価は、WFME の世界基準に準拠して作られた日本の基準（医学教育分野別評価基準日本版）に基づいて、医学部の教育プログラムを対象に行われ、認定の期間は7年である。大学全体を対象とする機関別認証評価（学校教育法に基づく認証評価）とは、対象も目的も異なる仕組みで、分野別評価は医学教育の内容と質を専門の観点から評価するものである。基準は改訂が重ねられており、現在は日本版 Ver.2.36 に基づいて評価が行われている。
    condition:
      region: 日本
      対象: 大学（医学部）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5333
    source: 日本医学教育評価機構. 医学教育分野別評価基準日本版（世界医学教育連盟グローバルスタンダード準拠）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jacme.or.jp/
    source_license: © 一般社団法人 日本医学教育評価機構（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: 国際基準の側は SRC-5332（WFME 世界基準 2020年改訂版）が前提となる。機関別認証評価の法的な枠組みは ME-060（学校教育法第109条）で扱う
  uncertainty: 設立年（2015年12月1日）と WFME 認定の日付（2017年3月18日）は JACME の公表資料で確認した。日本版基準 Ver.2.36（WFME 2015年版準拠）が、2024〜2026年度の評価報告書でも用いられていることを確認した。WFME 2020年版を反映した後継基準の公表状況は、2026-11-24 時点で確認できていない。基準の各項目の文言は転載していない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-057
  domain: ME
  subdomain: 教育管理
  assertion:
    plain_statement_ja: 大学は、授業の内容及び方法の改善を図るための組織的な研修及び研究（FD）を実施することが、大学設置基準で義務づけられている（第11条第2項）。同じ第11条の第1項では、教員と事務職員等を対象に、知識・技能の習得と能力・資質の向上のための研修（SD）の機会を設けることも定められている。FD の規定は、もとは大学設置基準第25条の3に置かれていたが、令和4年（2022年）の大学設置基準の改正で条文が再編され、現行では第11条（組織的な研修等）に移っている。
    condition:
      region: 日本
      対象: 大学およびその教員
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5334
    source: 大学設置基準（昭和31年文部省令第28号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/331M50000080028
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置：FD は第11条第2項、SD は同条第1項、指導補助者への研修は同条第3項。条文は e-Gov 法令検索の現行法（2026-11-24 取得）で確認した。旧第25条の3は平成19年の改正で設けられた規定で、令和4年改正（令和4年10月1日施行の再編）で第11条に移った。FD の効果の検証は ME-017（BEME レビュー）で扱い、本カードは制度の根拠を扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-058
  domain: ME
  subdomain: 教育管理
  assertion:
    plain_statement_ja: 大学は、学校教育法施行規則第165条の2により、大学・学部・学科（大学院では研究科・専攻）ごとに、教育上の目的を踏まえて3つの方針を定めるものとされている。すなわち、卒業又は修了の認定に関する方針（ディプロマ・ポリシー）、教育課程の編成及び実施に関する方針（カリキュラム・ポリシー）、入学者の受入れに関する方針（アドミッション・ポリシー）である。教育課程の編成・実施の方針を定めるに当たっては、卒業・修了の認定の方針との一貫性の確保に特に意を用いなければならないとされ、3つの方針が学位プログラムの設計の起点として位置づけられている。
    condition:
      region: 日本
      対象: 大学
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5335
    source: 学校教育法施行規則（昭和22年文部省令第11号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/322M40000080011
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置：第165条の2第1項（3つの方針）、第2項（教育課程の方針と卒業認定の方針の一貫性）。条文は e-Gov 法令検索の現行法（2026-11-24 取得）で確認した。同条自体は方針の「公表」を定めておらず、方針の公表は同規則第172条の2第1項第1号（大学の教育研究上の目的及び第165条の2第1項の規定により定める方針に関すること）による。3つの方針の運用（教学マネジメント）は ME-059 で扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-059
  domain: ME
  subdomain: 教育管理
  assertion:
    plain_statement_ja: 教学マネジメント指針は、中央教育審議会大学分科会が2020年に示した、学修者本位の教育への転換のための指針である。教学マネジメントは「大学がその教育目的を達成するために行う管理運営」と定義され、大学の内部質保証の確立と密接に関わる営みとされる。指針は、3つの方針を通じた学修目標の具体化、授業科目・教育課程の編成と実施、学修成果・教育成果の把握と可視化、教学マネジメントを支える基盤（FD・SD の高度化と教学 IR 体制の確立）、情報公表の5つの部分からなり、3つの方針を起点とする教育の PDCA サイクルを各大学が確立することを求めている。
    condition:
      region: 日本
      対象: 大学
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5336
    source: 中央教育審議会大学分科会. 教学マネジメント指針. 令和2年1月22日
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mext.go.jp/content/20200206-mxt_daigakuc03-000004749_002.pdf
    source_license: 政府標準利用規約（文部科学省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 公表日（令和2年1月22日）と指針の構成（5部）は文部科学省の公表資料で確認した。なお、指針には「教学マネジメント指針（追補）」（令和5年2月24日、中央教育審議会大学分科会）がある。指針の主たる対象は学士課程で、大学院や専門職大学等でも参考にすることが期待されている。3つの方針の法的根拠は ME-058（学校教育法施行規則第165条の2）で扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-060
  domain: ME
  subdomain: 教育管理
  assertion:
    plain_statement_ja: 大学は、学校教育法第109条により、自ら教育研究等の状況について点検・評価を行って結果を公表することに加え、政令で定める期間ごとに、文部科学大臣の認証を受けた評価機関（認証評価機関）による評価（認証評価）を受けることとされている。認証評価では、大学の教育研究等の総合的な状況が、認証評価機関の定める大学評価基準に適合しているかどうかが認定される。適合認定を受けられなかった場合は、文部科学大臣が大学に報告や資料の提出を求めることができる。この機関別認証評価は大学全体を対象とする仕組みであり、医学部など分野ごとの教育を対象とする分野別評価とは別の制度である。
    condition:
      region: 日本
      対象: 大学
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5337
    source: 学校教育法（昭和22年法律第26号、現行法）
    doi: null
    pmid: null
    pmcid: null
    url: https://laws.e-gov.go.jp/law/322AC0000000026
    source_license: 法令（著作権法13条により権利の目的とならない）
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典内の位置：自己点検・評価と公表は第109条第1項、認証評価は同条第2項、専門職大学等への追加の認証評価は同条第3項、適合認定の仕組みは同条第4〜6項。条文は e-Gov 法令検索の現行法（2026-11-24 取得）で確認した。認証評価の周期（7年以内）は政令（学校教育法施行令第40条）で定められるもので、第109条自体は「政令で定める期間ごとに」と定める。分野別評価は ME-056 で扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-061
  domain: ME
  subdomain: 教育管理
  assertion:
    plain_statement_ja: 教育プログラムの評価は、成果を測るだけでなく、評価の目的と問いを先に設計して行うものであり、そのためのモデルがいくつか整理されている。実験的・準実験的なデザインで効果を検証するモデル、Kirkpatrick の4段階モデル、活動と成果のつながりを図で表すロジックモデル、文脈・投入・過程・成果の4面から評価する CIPP モデルなどが代表的である。各モデルには理論的な背景（還元主義、システム理論、複雑性理論）があり、プログラムの複雑さと評価のニーズに照らしてモデルの基盤を選ぶことが、適切な評価設計につながるとされる。意図した成果だけでなく、意図しない変化も含めて記述することが求められる。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5338
    source: 'Frye AW, Hemmer PA. Program evaluation models and related theories: AMEE Guide No. 67. Med Teach. 2012;34(5):e288-99'
    doi: 10.3109/0142159X.2012.668637
    pmid: '22515309'
    pmcid: null
    url: https://doi.org/10.3109/0142159X.2012.668637
    source_license: © Taylor & Francis（Medical Teacher、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は抄録で確認した範囲（扱われるモデルと理論的基盤、評価設計の考え方）に基づく。各モデルの手順の細部は本文の範囲のため含めていない。Kirkpatrick の4段階そのものは ME-054 で扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応表

| カード | kokushi | コアカリ |
|---|---|---|
| ME-054 | （空欄：教育者向け理論のため付けない） | （空欄） |
| ME-055 | （空欄：同上） | （空欄） |
| ME-056 | （空欄：制度・運営が主題のため付けない） | （空欄） |
| ME-057 | （空欄：法令が主題。ME-002・ME-004 と同じ扱い） | （空欄） |
| ME-058 | （空欄：同上） | （空欄） |
| ME-059 | （空欄：制度・運営が主題のため付けない） | （空欄） |
| ME-060 | （空欄：法令が主題。ME-002・ME-004 と同じ扱い） | （空欄） |
| ME-061 | （空欄：教育者向け理論のため付けない） | （空欄） |

## 4. 未解決事項

1. EM-4（ME-057）：FD 規定の移行先は現行条文で第11条と確認した。平成19年改正で第25条の3が設けられた経緯と、令和4年改正での再編の対応関係は、改正資料での逐語確認まではしていない（現行法に第25条の3が存在せず、第11条に同内容の規定があることは確認済み）。
2. EM-1（ME-054）：Kirkpatrick 原典の書籍版 ISBN は API で確認できず記載していない。4段階を裏づける CC BY の総説は特定できなかった。
3. EM-2（ME-055）：WFME 基準書の ISBN は確認していない（公式サイトで無償公開されている文書として扱った）。区分は RESTRICTED の見立てのままである。
4. EM-3（ME-056）：2024〜2026年度の評価は日本版 Ver.2.36 で行われていることを確認した。「2025年版 Ver.1.0」の公表は確認できておらず、後継基準の公表状況と受審年度ごとの適用版は JACME の公表で確認されたい。

## 5. 引き継ぎメモ

- 新規出典は9件（SRC-5330〜5338）。出典マスター全体と DOI・PMID で照合し、いずれも未登録であることを確認した。SRC-5339 は未使用（欠番の明示。IT ファイルの SRC-5349 と同じ扱い）。
- 法令3件（SRC-5334・5335・5337）は e-Gov の現行法データ（法令 API）で条文を直接読んで確認した。依頼文が懸念していた EM-4 の条文番号は、旧第25条の3ではなく現行の第11条が正しい。
- 第3弾の他の領域は別ファイル（TL：ME-026〜034、AS：ME-035〜044、CD：ME-045〜053、IT：ME-062〜071）。

## 6. 検証指摘への修正記録（2026-11-24）

レポジトリ側の検証で指摘された点について、本ファイルでは次の修正を行った。

1. ME-060：認証評価の周期を「7年」から「7年以内」に訂正した（uncertainty。学校教育法施行令の規定）。
2. ME-056：JACME 基準の版について、2024〜2026年度の評価報告書は Ver.2.36 で書かれていることを確認した。「2025年版 Ver.1.0」の公表は確認できていないため、公表されているとしていた記載（出典表・主張文・uncertainty・未解決事項）を実態に合わせて訂正した。
3. ME-058：方針の「公表」の根拠は、学校教育法施行規則第172条の2と明記した（uncertainty）。
4. ME-059：「教学マネジメント指針（追補）」（令和5年2月24日、中央教育審議会大学分科会）があることを uncertainty に添えた。
5. SRC-5339：欠番になっていたため、未使用であることを冒頭と引き継ぎメモに明記した（IT ファイルの SRC-5349 と同じ扱い）。
6. ME-058：uncertainty の公表根拠を「第172条の2（情報の積極的な提供）と明記できる」から「第172条の2第1項第1号による」に改めた。「情報の積極的な提供」は大学設置基準第2条の見出しであり、施行規則第172条の2 の内容（教育研究活動等の状況の公表）とは別のため。
7. カードの uncertainty 欄・出典表の確認経路欄に入っていた修正経緯の記述を外し、経緯は本節に集約した（uncertainty には確かさに関わる事実だけを残す）。対象：ME-056・ME-060・出典表 SRC-5333。ME-060 には施行令の条番号（第40条）を補った。
