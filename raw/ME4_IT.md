# 医療者教育（ME）第3弾 IT：ME-062〜071（カード10件）

依頼文（round_ME4_request.md、2026-11-24）に基づく第3弾のうち、IT（ICTを用いた教育）領域の10枚。決定事項の適用は次のとおり。

- 作業前に取得したレポジトリ：hm-cmed/cleanroom-facts 最新版、コミット `10bd46714ac6120e912b72cdb761af8d32925210`（2026-11-24）。出典マスターと既存 ME カードで DOI・PMID の重複を照合し、本ファイルの新規出典はいずれも未登録であることを確認した。
- subdomain は「ICTを用いた教育」とした。カリキュラム欄は空欄とし、condition.対象 は各カードの内容に応じて記した。
- 初等中等教育向けの文部科学省生成 AI ガイドラインは、依頼文の決定により入れていない（大学向けの周知のみ）。
- IT-2（UNESCO）は CC BY-SA 3.0 IGO のため RESTRICTED とした（依頼文 §2-4）。
- IT-4・IT-5（LLM の試験成績）は、数値を本文で確定させ、モデル名・版・試験年度・研究の時点を uncertainty に書いた。主張文では製品名を使わず「大規模言語モデル（LLM）」等の一般名で書き、製品名・モデル名は出典の書誌と uncertainty に留めた。
- 新規出典は SRC-5340〜5348 を割り当てた（SRC-5349 は未使用。IT-7 は SRC-5340 と SRC-5341 の再利用で作り、新規出典を増やしていない）。

## 1. 出典表

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-5340 | 文部科学省高等教育局. 大学・高専における生成AIの教学面の取扱いについて（周知）. 令和5年7月13日 | なし | なし | 政府標準利用規約（文部科学省ホームページ） | GOV_JP | 文部科学省の公表資料（事務連絡と別紙）で、出力をそのまま用いることの不適切さ、明記・小テストや口述試験の併用等の評価上の工夫、虚偽・個人情報・著作権への留意を確認 |
| SRC-5341 | UNESCO. Guidance for generative AI in education and research. UNESCO; 2023. ISBN 978-92-3-100612-8 | 10.54675/EWZM9535 | なし | CC BY-SA 3.0 IGO（本プロジェクトの区分では RESTRICTED） | RESTRICTED | UNESCO の出版物ページで DOI・ISBN・ライセンス表示を確認 |
| SRC-5342 | World Health Organization. Ethics and governance of artificial intelligence for health: guidance on large multi-modal models. WHO; 2024. ISBN 978-92-4-008475-9（電子版） | なし | なし | CC BY-NC-SA 3.0 IGO | RESTRICTED | WHO 公式発表（2024年1月18日）と IRIS の書誌で、公表日・ISBN・医学/看護教育への応用とリスクの記載を確認。ライセンスは本書の奥付で CC BY-NC-SA 3.0 IGO（NC-SA 系のため区分は RESTRICTED） |
| SRC-5343 | Kung TH, Cheatham M, Medenilla A, et al. Performance of ChatGPT on USMLE: potential for AI-assisted medical education using large language models. PLOS Digit Health. 2023;2(2):e0000198 | 10.1371/journal.pdig.0000198 | 36812645 | CC BY 4.0（Europe PMC の license 欄） | OPEN | PMC 全文で、合格水準（正答率約60%）に近い成績と、入力形式による正答率の変動を確認 |
| SRC-5344 | Yano Y, Ohashi M, Miyagami T, et al. The advanced reasoning capabilities of large language models for detecting contraindicated options in medical exams. JMIR Med Inform. 2025;13:e68527 | 10.2196/68527 | 40354629 | CC BY 4.0（Europe PMC の license 欄） | OPEN | PMC 全文で、対象モデル、試験日（2024年10月10日）、15問の内訳と正答率・禁忌肢検出率を確認 |
| SRC-5345 | Izquierdo-Condoy JS, Arias-Intriago M, Tello-De-la-Torre A, Busch F, Ortiz-Prado E. Generative Artificial Intelligence in Medical Education: Enhancing Critical Thinking or Undermining Cognitive Autonomy? J Med Internet Res. 2025;27:e76340 | 10.2196/76340 | 41183320 | CC BY 4.0（Europe PMC の license 欄） | OPEN | Europe PMC で書誌・抄録（論説。両面の整理とカリキュラム統合の主張）を確認。分割案の仮題名（Undermining It?）は誤りで、本書誌の副題が正しい |
| SRC-5346 | Kononowicz AA, Woodham LA, Edelbring S, et al. Virtual patient simulations in health professions education: systematic review and meta-analysis by the Digital Health Education Collaboration. J Med Internet Res. 2019;21(7):e14676 | 10.2196/14676 | 31267981 | CC BY 4.0（Europe PMC の license 欄） | OPEN | Europe PMC で書誌・抄録（51件、知識と技能の効果量）を確認 |
| SRC-5347 | Kyaw BM, Saxena N, Posadzki P, et al. Virtual reality for health professions education: systematic review and meta-analysis by the Digital Health Education Collaboration. J Med Internet Res. 2019;21(1):e12959 | 10.2196/12959 | 30668519 | CC BY 4.0（Europe PMC の license 欄） | OPEN | Europe PMC で書誌・抄録（31件、知識と認知技能の効果量）を確認 |
| SRC-5348 | Means B, Toyama Y, Murphy R, Bakia M, Jones K. Evaluation of Evidence-Based Practices in Online Learning: A Meta-Analysis and Review of Online Learning Studies. U.S. Department of Education; 2010（revised September 2010） | なし | なし | 米国連邦政府の報告書（パブリックドメイン） | GOV_US | 米国教育省の報告書本文（SRI の公開ページ経由）で、50の効果の統合、オンラインの控えめな有利さ、ブレンデッドの大きな効果と解釈上の注意を確認 |

## 2. 事実カード（YAML）

```yaml
- id: ME-062
  domain: ME
  subdomain: ICTを用いた教育
  assertion:
    plain_statement_ja: 文部科学省は2023年7月、大学・高等専門学校における生成AIの教学面の取扱いについて周知を出し、各大学・高専が実態に応じて指針を定め、状況の変化に応じて見直すことを求めた。周知では、学生が生成AIの出力をそのまま用いてレポート等を作成することは一般に不適切であること、成績評価を適切に行うために生成AIを利用したことの明記や、小テスト・口述試験の併用といった工夫が有効であること、生成された内容に虚偽や偏りが含まれうること、機密情報や個人情報の流出、著作権の侵害に留意すべきことが示されている。あわせて、ブレインストーミングや文章校正などの学びの補助としての活用や、生成AIを使いこなすための教育も想定される場面として挙げられている。
    condition:
      region: 日本
      対象: 大学・高等専門学校の学生と教員
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5340
    source: 文部科学省高等教育局. 大学・高専における生成AIの教学面の取扱いについて（周知）. 令和5年7月13日
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mext.go.jp/content/20230714-koutou02-000030953-15.pdf
    source_license: 政府標準利用規約（文部科学省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 内容は周知の別紙（留意すべき観点）で確認した。2026-11-24 時点で、この周知を置き換える大学向けの新しい文書は確認できていない。初等中等教育向けの生成AIガイドライン（文部科学省）は別の文書であり、依頼文の決定により本カードに含めていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-063
  domain: ME
  subdomain: ICTを用いた教育
  assertion:
    plain_statement_ja: UNESCOは2023年、教育と研究における生成AIについての初の国際ガイダンスを公表した。ガイダンスは人間中心の考え方を原則に置き、データプライバシーの保護、提供者に対する規制の必要性、教育機関が生成AIの倫理的・教育的な適切さを検証したうえで導入することなどを示している。生成AIの急速な普及に対して、各国の政策が追いついていない状況を踏まえ、教育機関と政策立案者の双方に向けた指針として作られたもので、年齢に応じた利用の在り方や、学習者の主体性を損なわない使い方も論点になっている。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5341
    source: UNESCO. Guidance for generative AI in education and research. UNESCO; 2023
    doi: 10.54675/EWZM9535
    pmid: null
    pmcid: null
    url: https://doi.org/10.54675/EWZM9535
    source_license: CC BY-SA 3.0 IGO（SA 系のため本プロジェクトでは RESTRICTED 区分）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: DOI と ISBN（978-92-3-100612-8）は UNESCO の出版物ページで確認した。ライセンスは CC BY-SA 3.0 IGO で、自由に使える表示ではあるが、本プロジェクトの区分（第1回・第2回のライセンス照合の基準）では SA 系は RESTRICTED になる。国内向けの文書は ME-062（文部科学省の周知）で扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-064
  domain: ME
  subdomain: ICTを用いた教育
  assertion:
    plain_statement_ja: WHOは2024年1月、生成AIの一種である大規模マルチモーダルモデル（LMM）について、医療での倫理とガバナンスの指針を公表した。指針は、LMMの応用分野の一つに医学・看護教育（模擬患者との対話練習など）を挙げる一方で、不正確な出力、自動化バイアス（AIの出力を過度に信頼すること）、データの偏りといったリスクを示し、開発者・提供者・利用する医療機関それぞれへの勧告をまとめている。教育での利用についても、出力の正確さを前提にせず、人間による監督のもとで使うことが前提とされている。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5342
    source: 'World Health Organization. Ethics and governance of artificial intelligence for health: guidance on large multi-modal models. WHO; 2024'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.who.int/publications/i/item/9789240084759
    source_license: CC BY-NC-SA 3.0 IGO
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 公表日（2024年1月18日）と ISBN（978-92-4-008475-9、電子版）は WHO 公式発表と IRIS の書誌で確認した。指針の勧告の細部は本文（98ページ）の範囲のため、主張は教育への応用とリスクの位置づけに限定した。2021年の WHO の医療 AI 倫理指針を土台とする文書である。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-065
  domain: ME
  subdomain: ICTを用いた教育
  assertion:
    plain_statement_ja: 2023年に公表された検証では、大規模言語モデル（LLM）が、米国の医師免許試験（USMLE）形式の問題で、Step 1、Step 2CK、Step 3 のいずれでも合格水準（正答率約60%）に近い成績を示した。モデルは医学の専門的な追加訓練を受けておらず、汎用の言語モデルとしての学習のみでこの水準に達した。この結果は、LLM が医学知識の問題にある程度答えられることを示した初期の実証として、AI を医学教育にどう使うかという議論の出発点になった。ただし成績は問題の入力形式によって変わり、同じモデルの評価でも提示の仕方で正答率が変動することに注意が要る。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5343
    source: 'Kung TH, Cheatham M, Medenilla A, et al. Performance of ChatGPT on USMLE: potential for AI-assisted medical education using large language models. PLOS Digit Health. 2023;2(2):e0000198'
    doi: 10.1371/journal.pdig.0000198
    pmid: '36812645'
    pmcid: PMC9931230
    url: https://doi.org/10.1371/journal.pdig.0000198
    source_license: CC BY 4.0（PLOS Digital Health、Europe PMC の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: '研究の時点とモデル：2023年2月公表。対象モデルは GPT-3.5 系の大規模言語モデル（製品名は出典の書誌に記載）。数値は本文で確認した。入力形式により正答率は大きく変動し、自由回答形式では不確定な応答の扱いによって Step 1 で75.0%〜45.4% の幅があった。より新しい研究では、後継モデル（GPT-4）を用いた検証で合格水準を大きく上回る成績が報告されており（Nori ら、2023年）、本カードの数値は2023年時点のモデルの成績として読む必要がある。'
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-066
  domain: ME
  subdomain: ICTを用いた教育
  assertion:
    plain_statement_ja: 日本の医師国家試験の問題を用いた2025年の検証では、大規模言語モデル（LLM）が、選ぶと不合格になりうる禁忌肢をどの程度見分けられるかが検討された。禁忌肢を含む15問（2019〜2024年の国家試験問題、画像問題を除く）という小規模な検証で、従来モデルでは正答率80%、禁忌肢の検出率73%だったのに対し、推論を強化した新しいモデルでは正答率100%、禁忌肢の検出率87%と、いずれも新しいモデルが上回った。著者らは、対象が15問にとどまる予備的な検討であり、結果の一般化には限界があるとしている。正答できることと、避けるべき選択肢を避けられることは別の能力であり、後者には推論の質が関わることが示唆された。
    condition:
      region: 日本
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5344
    source: 'Yano Y, Ohashi M, Miyagami T, et al. The advanced reasoning capabilities of large language models for detecting contraindicated options in medical exams. JMIR Med Inform. 2025;13:e68527'
    doi: 10.2196/68527
    pmid: '40354629'
    pmcid: PMC12088613
    url: https://doi.org/10.2196/68527
    source_license: CC BY 4.0（JMIR Medical Informatics、Europe PMC の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 'モデル名と時点：従来モデルは GPT-4、推論強化モデルは OpenAI o1。試験の実施は2024年10月10日、問題は2019〜2024年の医師国家試験から禁忌肢を含む15問（日本語）。英語に翻訳した問題でも同様の傾向だった。数値は本文で確認した。より新しいモデルでの検証が今後も出続ける分野であり、本カードの数値は2024年時点のモデル同士の比較として読む必要がある。GPT-4 の日本の医師国家試験での初期の検証（2023年）も複数あるが、本カードは禁忌肢の検出に焦点を当てた本研究を出典とした。'
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-067
  domain: ME
  subdomain: ICTを用いた教育
  assertion:
    plain_statement_ja: 生成AIの医学教育への利用については、臨床推論の練習、文献の整理、文章作成、形成的評価の補助など、学習を支える使い方が広がる一方で、批判的思考への影響が論点になっている。2025年の論説では、効率や文章の質の向上が報告される反面、AIへの過度の依存によって学習者が受け身になり、誤情報に弱くなり、考える過程そのものを省いてしまう危険が指摘されている。生成AIを、倫理的な使い方、プロンプトの工夫、出力の批判的な評価を教えるカリキュラムの中に位置づけて使えば認知の助けになるが、そうした組み込みなしでは学習者の認知的な自律を損ないうる、というのが論説の整理である。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5345
    source: 'Izquierdo-Condoy JS, Arias-Intriago M, Tello-De-la-Torre A, Busch F, Ortiz-Prado E. Generative Artificial Intelligence in Medical Education: Enhancing Critical Thinking or Undermining Cognitive Autonomy? J Med Internet Res. 2025;27:e76340'
    doi: 10.2196/76340
    pmid: '41183320'
    pmcid: PMC12624298
    url: https://doi.org/10.2196/76340
    source_license: CC BY 4.0（Journal of Medical Internet Research、Europe PMC の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本出典は系統的レビューではなく論説（viewpoint）であり、主張は著者らの整理と主張に基づく。分割案の仮題名（…Undermining It?）は誤りで、実際の副題は Undermining Cognitive Autonomy? である。生成AIの教育利用については2026年に入っても新しい総説が出続けており、取り込み時点での最新状況の確認が望ましい。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-068
  domain: ME
  subdomain: ICTを用いた教育
  assertion:
    plain_statement_ja: 生成AIの出力をそのまま提出する行為への対応は、禁止の宣言だけではなく、評価の設計側の工夫として示されている。文部科学省の大学向けの周知では、生成AIを利用したことの明記を求めること、小テストや口述試験を併用して学習者本人の到達を確認すること、といった評価上の工夫が有効とされた。UNESCOのガイダンスでも、教育機関が生成AIの倫理的・教育的な適切さを検証し、利用のルールを定めることが求められている。
    condition:
      region: 日本
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5340
    source: 文部科学省高等教育局. 大学・高専における生成AIの教学面の取扱いについて（周知）. 令和5年7月13日
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mext.go.jp/content/20230714-koutou02-000030953-15.pdf
    source_license: 政府標準利用規約（文部科学省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: 国際的な指針として SRC-5341（UNESCO. Guidance for generative AI in education and research. 2023、RESTRICTED）も、教育機関による適切さの検証とルールづくりを求めている
  uncertainty: 本カードは ME-062（周知そのもの）と出典を共有し、評価と学術的誠実性に絞った論点として独立させた。主張は周知とガイダンスに明記された内容に限っている。AI検出ツールの性能や、検出ツールへの依拠の是非は、いずれの出典にも明記がないため含めていない。医学教育に限った裏づけ論文は今回選定しなかった（分割案の仮 SRC-5349 は未使用）。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-069
  domain: ME
  subdomain: ICTを用いた教育
  assertion:
    plain_statement_ja: バーチャル患者（コンピュータ上で対話できる仮想の患者症例）を用いた学習は、医療専門職教育で効果が検証されている。系統的レビューとメタ解析（51件の試験、参加者4,696人）では、従来型の教育と比べて、知識では同程度（標準化平均差0.11、95%信頼区間 −0.17〜0.39）だった一方、技能ではバーチャル患者の側が上回った（標準化平均差0.90、95%信頼区間 0.49〜1.32）。ただし、対象研究の方法論の限界と異質性のため、根拠の質は全体として低いと評価されている。画面上の仮想患者との対話で臨床推論や面接の進め方を繰り返し練習できる点が、この方法の特徴である。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5346
    source: 'Kononowicz AA, Woodham LA, Edelbring S, et al. Virtual patient simulations in health professions education: systematic review and meta-analysis by the Digital Health Education Collaboration. J Med Internet Res. 2019;21(7):e14676'
    doi: 10.2196/14676
    pmid: '31267981'
    pmcid: PMC6632099
    url: https://doi.org/10.2196/14676
    source_license: CC BY 4.0（Journal of Medical Internet Research、Europe PMC の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 数値（51件、参加者4,696人、知識と技能の効果量）は原著の抄録で確認した。対象は医療専門職教育全般（学部・卒後）で、医師教育に限らない。ME-009・ME-013 のシミュレーション（実物・模擬患者を用いるもの）とは媒体が異なり、本カードは画面上の仮想患者を扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-070
  domain: ME
  subdomain: ICTを用いた教育
  assertion:
    plain_statement_ja: VR（仮想現実）を用いた教育は、医療専門職教育で、知識の習得については従来型の学習よりやや有利とするメタ解析がある。系統的レビュー（31件の研究、参加者2,407人）では、知識の事後スコアは従来型学習との比較で標準化平均差0.44（95%信頼区間 0.18〜0.69、8件の統合、中程度の確実性）、認知技能では同1.12（95%信頼区間 0.81〜1.43、4件の統合）と報告された。一方、態度や満足度については結果が混在し、患者アウトカムや行動変容を見た研究はなかった。アウトカムの種類によって証拠の強さが異なる点に注意が要る。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5347
    source: 'Kyaw BM, Saxena N, Posadzki P, et al. Virtual reality for health professions education: systematic review and meta-analysis by the Digital Health Education Collaboration. J Med Internet Res. 2019;21(1):e12959'
    doi: 10.2196/12959
    pmid: '30668519'
    pmcid: PMC6362387
    url: https://doi.org/10.2196/12959
    source_license: CC BY 4.0（Journal of Medical Internet Research、Europe PMC の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 数値（31件、参加者2,407人、知識と認知技能の効果量）は原著の抄録で確認した。根拠の確実性は GRADE で低〜中程度と評価されている。対象は医療専門職教育全般である。技能（手技）の習得そのものを測った比較は限られ、認知技能の結果と分けて読む必要がある。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-071
  domain: ME
  subdomain: ICTを用いた教育
  assertion:
    plain_statement_ja: 米国教育省が委託したメタ解析（1996〜2008年の研究から、効果量を算出できた50の比較を統合）では、オンライン学習の条件は対面のみの授業と比べて、平均して控えめに良好な学習成果と結びついていた。効果がより大きかったのは、対面とオンラインを組み合わせたブレンデッド学習の条件であり、対面授業との差は純粋なオンライン学習の場合を上回っていた。ただし、ブレンデッドの条件では学習時間や教材の要素が対照より追加されていることが多く、この有利さを媒体そのものの効果とみなすことはできない、と報告書は注意している。対象は教育全般で、大学生・大学院生・専門職の研修が中心であり、医学・医療系の訓練も多く含まれていた。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5348
    source: 'Means B, Toyama Y, Murphy R, Bakia M, Jones K. Evaluation of Evidence-Based Practices in Online Learning: A Meta-Analysis and Review of Online Learning Studies. U.S. Department of Education; 2010'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.sri.com/publication/education-learning-pubs/digital-learning-pubs/evaluation-of-evidence-based-practices-in-online-learning-a-meta-analysis-and-review-of-online-learning-studies/
    source_license: 米国連邦政府の報告書（パブリックドメイン）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 報告書は2010年9月の改訂版が現行形。全体の平均効果（+0.20）とブレンデッドの効果（+0.35）は報告書の公表値だが、主張では方向性の記述に留めた。ME-016（医療専門職のインターネット基盤学習のメタ解析）とは対象範囲が異なり、本カードは教育全般の政府報告書を扱う。provenance の URL は実施機関（SRI）の公開ページで、報告書本文への案内を含む。
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
| ME-062 | （空欄：制度・指針が主題のため付けない） | （空欄） |
| ME-063 | （空欄：同上） | （空欄） |
| ME-064 | （空欄：同上） | （空欄） |
| ME-065 | （空欄：教育者向けの実証知見のため付けない） | （空欄） |
| ME-066 | （空欄：同上） | （空欄） |
| ME-067 | （空欄：同上） | （空欄） |
| ME-068 | （空欄：評価の設計が主題のため付けない） | （空欄） |
| ME-069 | （空欄：教育者向けの実証知見のため付けない） | （空欄） |
| ME-070 | （空欄：同上） | （空欄） |
| ME-071 | （空欄：同上） | （空欄） |

## 4. 未解決事項

1. IT-4・IT-5（ME-065・066）：LLM の成績は変化が速く、カードの数値は各研究の時点（2023年・2024年）のモデルでの結果である。より新しいモデルでの研究が出た場合は、カードの改訂ではなく新しいカードでの追加を検討されたい。
2. IT-6（ME-067）：出典は論説であり系統的レビューではない。生成AIの医学教育利用の系統的レビューが今後公表されれば、主出典の差し替え候補になる。
3. IT-7（ME-068）：医学教育に限った学術的誠実性の裏づけ論文は今回選定しなかった（仮 SRC-5349 は未使用のまま）。必要になれば MedEdPublish 等の総説を別途登録する。
4. IT-1（ME-062）：文部科学省の周知は2023年7月のもので、大学向けの後継文書が出た場合は差し替えが必要になる。

## 5. 引き継ぎメモ

- 新規出典は9件（SRC-5340〜5348）。出典マスター全体と DOI・PMID で照合し、いずれも未登録であることを確認した。SRC-5349 は未使用。
- IT-5 の書誌訂正：分割案の仮題名は内容の要約であり、実際の論文題名は「The advanced reasoning capabilities of large language models for detecting contraindicated options in medical exams」（Yano Y ら、JMIR Med Inform. 2025。末尾は Examinations ではなく Exams が正しい。当初 Examinations と記載していたため検証指摘により訂正した）。IT-6 も副題を訂正した（Undermining Cognitive Autonomy?）。
- 第3弾の他の領域は別ファイル（TL：ME-026〜034、AS：ME-035〜044、CD：ME-045〜053、EM：ME-054〜061）。第3弾の合計は46件（ME-026〜071）、新規出典は48件（SRC-5300〜5309、5310〜5319、5320〜5328、5329、5330〜5338、5340〜5348）。

## 6. 検証指摘への修正記録（2026-11-24）

レポジトリ側の検証で指摘された点について、本ファイルでは次の修正を行った。

1. ME-064（WHO）：ライセンス表示を「© World Health Organization 2024（All rights reserved）」から「CC BY-NC-SA 3.0 IGO」に訂正した（出典表・provenance の source_license）。区分は RESTRICTED のまま。
2. ME-066：論文題名の末尾を「…in medical examinations」から「…in Medical Exams」に訂正した（出典表・provenance・引き継ぎメモ）。
3. ME-068：主張文の末尾にあった「AI検出ツールの判定だけに依拠せず、評価方法そのものを見直すことが国内・国際の指針に共通する方向」という一文を削除した。文部科学省の周知にも UNESCO の指針にもない推論であったため。uncertainty の関連記述も実態に合わせて修正した。
4. ME-071：「純粋なオンライン学習との差より大きかった」という文意の通らない文を、出典の内容（ブレンデッド学習の対面授業との差が、純粋なオンライン学習の対面授業との差を上回っていた）に沿って書き直した。
5. カードの uncertainty 欄・出典表の確認経路欄に入っていた修正経緯の記述を外し、経緯は本節に集約した（uncertainty には確かさに関わる事実だけを残す）。対象：ME-068・出典表 SRC-5342。
