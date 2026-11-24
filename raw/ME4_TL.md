# 医療者教育（ME）第3弾 TL：ME-026〜034（カード9件）

依頼文（round_ME4_request.md、2026-11-24）に基づく第3弾のうち、TL（ティーチング＆ラーニング）領域の9枚。決定事項の適用は次のとおり。

- 作業前に取得したレポジトリ：hm-cmed/cleanroom-facts 最新版、コミット `10bd46714ac6120e912b72cdb761af8d32925210`（2026-11-24）。出典マスター（sources.yaml）と既存 ME カードで番号・出典の重複を DOI・PMID で照合し、本ファイルの新規出典はいずれも未登録であることを確認した。
- subdomain は「ティーチング＆ラーニング」とした。本領域は教育者向けの理論・手法が主題のため、カリキュラム欄は空欄とし、condition.対象 を「教育者」とした（依頼文の決定）。
- 新規出典は SRC-5300〜5309 を割り当てた。RESTRICTED の原典（AMEE Guide、古典論文）は、主張を概念の骨格と検証済みの数値に限って自作の文で書き、定義文・結論文の翻訳は転載していない。CC BY の論文で同じ内容を裏づけられるものは、主出典ではなく裏づけ（corroboration）として併記した（TL-2）。見つからなかったものは未解決事項に記した。（当初この箇条書きで「主出典にした」と書いていたのは実態と異なる記述で、検証指摘により訂正した）
- 数値は一次資料で確認したものだけを書いた。抄録で確認した場合は uncertainty にその旨を記した。

## 1. 出典表

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-5300 | Young JQ, Van Merriënboer J, Durning S, Ten Cate O. Cognitive Load Theory: implications for medical education: AMEE Guide No. 86. Med Teach. 2014;36(5):371-384 | 10.3109/0142159X.2014.889290 | 24593808 | © Taylor & Francis（Medical Teacher、CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（3種の負荷、worked example、expertise-reversal effect）を確認 |
| SRC-5301 | Maye JA, Hurley F. The Effectiveness of Spaced Repetition in Medical Education: A Systematic Review and Meta-Analysis. Clin Teach. 2026;23(2):e70353 | 10.1111/tct.70353 | 41601436 | © Wiley（The Clinical Teacher、CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（メタ解析13件、学習者21,415人、SMD 0.78）を確認 |
| SRC-5302 | Luu NK, Severance S. A Systematic Review of Spaced Repetition, Retrieval Practice, and Academic Performance in Undergraduate Medical Students. Cureus. 2026;18(9):e116147 | 10.7759/cureus.116147 | 42866698 | CC BY 4.0（Europe PMC の license 欄） | OPEN | Europe PMC で書誌・抄録（21件のナラティブ統合）・ライセンスを確認 |
| SRC-5303 | Neher JO, Stevens NG. The one-minute preceptor: shaping the teaching conversation. Fam Med. 2003;35(6):391-393 | なし | 12817861 | © Society of Teachers of Family Medicine（CC表示なし） | RESTRICTED | Europe PMC で書誌を確認。5つのマイクロスキルの内容は原典（Neher ら 1992、PMID: 1496899）の抄録で確認 |
| SRC-5304 | Wolpaw TM, Wolpaw DR, Papp KK. SNAPPS: a learner-centered model for outpatient education. Acad Med. 2003;78(9):893-898 | 10.1097/00001888-200309000-00010 | 14507619 | © Association of American Medical Colleges（CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（6段階の内容）を確認 |
| SRC-5305 | Peters M, Ten Cate O. Bedside teaching in medical education: a literature review. Perspect Med Educ. 2014;3(2):76-88 | 10.1007/s40037-013-0083-y | 24049043 | CC BY（Europe PMC の license 欄） | OPEN | Europe PMC で書誌・抄録・ライセンスを確認 |
| SRC-5306 | Mann K, Gordon J, MacLeod A. Reflection and reflective practice in health professions education: a systematic review. Adv Health Sci Educ. 2009;14(4):595-621 | 10.1007/s10459-007-9090-2 | 18034364 | © Springer（CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（根拠は主に理論的で文献が分散）を確認 |
| SRC-5307 | Murad MH, Coto-Yglesias F, Varkey P, Prokop LJ, Murad AL. The effectiveness of self-directed learning in health professions education: a systematic review. Med Educ. 2010;44(11):1057-1068 | 10.1111/j.1365-2923.2010.03750.x | 20946476 | © Wiley（Medical Education、CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（59件、学習者8,011人、知識 SMD 0.45 等）を確認 |
| SRC-5308 | Ten Cate O, Durning S. Peer teaching in medical education: twelve reasons to move from theory to practice. Med Teach. 2007;29(6):591-599 | 10.1080/01421590701606799 | 17922354 | © Taylor & Francis（Medical Teacher、CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（12の理由、近ピアの位置づけ）を確認 |
| SRC-5309 | McGaghie WC, Issenberg SB, Barsuk JH, Wayne DB. A critical review of simulation-based mastery learning with translational outcomes. Med Educ. 2014;48(4):375-385 | 10.1111/medu.12391 | 24606621 | © Wiley（Medical Education、CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（23件の批判的レビュー、T1〜T4 の転帰）を確認。ME-009 の出典 SRC-5112（2011年のメタ解析）とは別論文であることを DOI で照合 |

## 2. 事実カード（YAML）

```yaml
- id: ME-026
  domain: ME
  subdomain: ティーチング＆ラーニング
  assertion:
    plain_statement_ja: 認知負荷理論は、学習の制約を作業記憶の容量の限界から説明する理論である。学習課題そのものに伴う負荷、教材や指導の提示の仕方によって生じる余分な負荷、学びを深める方向に働く負荷の3種類を区別し、合計の負荷が作業記憶の容量を超えると学習や遂行が妨げられると考える。医学教育では、知識・技能・態度を同時に統合する活動が多いため負荷が高くなりやすく、教材や実習の設計では、余分な負荷を減らす工夫（例：worked example の提示）や、学習者の発達段階に合わせて課題の複雑さを調整することが求められる。また、初学者に有効な指導法が上級者にはかえって妨げになることがある（expertise-reversal effect）ため、学習の進展に応じて設計を変える必要がある。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5300
    source: 'Young JQ, Van Merriënboer J, Durning S, Ten Cate O. Cognitive Load Theory: implications for medical education: AMEE Guide No. 86. Med Teach. 2014;36(5):371-384'
    doi: 10.3109/0142159X.2014.889290
    pmid: '24593808'
    pmcid: null
    url: https://doi.org/10.3109/0142159X.2014.889290
    source_license: © Taylor & Francis（Medical Teacher、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は抄録で確認した範囲（3種の負荷の区別、worked example 等の設計技法、expertise-reversal effect）に限って自作の文で記載した。本文（購読制）の各論は含めていない。認知負荷理論を医学教育向けに解説した CC BY の総説は、今回の探索では同内容を裏づけるものを特定できなかった。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-027
  domain: ME
  subdomain: ティーチング＆ラーニング
  assertion:
    plain_statement_ja: 学習した内容を時間間隔をあけて繰り返し想起する学習法（間隔反復と検索練習）は、医学教育の学習者の試験成績を高めることが系統的レビューで示されている。フラッシュカードや多肢選択問題の配信などを用いた間隔反復の研究を統合したメタ解析（13件、学習者21,415人）では、通常の学習法と比べて標準化平均差0.78（95%信頼区間 0.56〜0.99）と、間隔反復の側に有意な有利さが認められた。学部医学教育を対象とした別の系統的レビュー（21件）でも、管理された研究では成績や保持の改善がおおむね支持された一方、学習者が自発的に使うフラッシュカードの観察研究では結果が混在し、選択バイアスの影響を受けやすいことが指摘されている。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5301
    source: 'Maye JA, Hurley F. The Effectiveness of Spaced Repetition in Medical Education: A Systematic Review and Meta-Analysis. Clin Teach. 2026;23(2):e70353'
    doi: 10.1111/tct.70353
    pmid: '41601436'
    pmcid: null
    url: https://doi.org/10.1111/tct.70353
    source_license: © Wiley（The Clinical Teacher、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: 学部医学教育での間隔反復・検索練習については SRC-5302（Luu NK, Severance S. Cureus. 2026、CC BY 4.0）の系統的レビューでも、管理された研究で成績・保持の改善が支持されている
  uncertainty: 数値（メタ解析13件、学習者21,415人、標準化平均差0.78、95%信頼区間0.56〜0.99）は主出典の抄録で確認した。主出典は2026年刊行の新しいレビューであり、対象研究の内訳は本文未確認。テスト効果（検索練習そのもの）の古典的実験研究は本カードの出典に含めていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-028
  domain: ME
  subdomain: ティーチング＆ラーニング
  assertion:
    plain_statement_ja: ワンミニッツプリセプターは、外来や病棟の短い指導場面で使われる臨床指導の進め方で、5つのマイクロスキルからなる。すなわち、学習者に考え（見立て）をまず言わせること、その根拠を尋ねること、一般原則を教えること、うまくできた点を認めて強化すること、誤りを正すこと、の5つである。学習者の報告を聞いて指導者が一方的に解説する進め方と違い、学習者の思考過程を引き出してから教える点に特徴があり、限られた時間の指導を組み立てる枠として広く使われている。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5303
    source: 'Neher JO, Stevens NG. The one-minute preceptor: shaping the teaching conversation. Fam Med. 2003;35(6):391-393'
    doi: null
    pmid: '12817861'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/12817861/
    source_license: © Society of Teachers of Family Medicine（Family Medicine、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 5つのマイクロスキルの具体的内容は、原典である Neher JO, Gordon KC, Meyer B, Stevens N. A five-step "microskills" model of clinical teaching. J Am Board Fam Pract. 1992;5(4):419-424（PMID：1496899、DOIなし）の抄録で確認した。原典は出典として登録せず、本カードの主出典は2003年の解説論文とした。2003年論文に DOI は付与されていない。効果の大きさを示す比較研究は本カードに含めていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-029
  domain: ME
  subdomain: ティーチング＆ラーニング
  assertion:
    plain_statement_ja: SNAPPSは、外来教育で学習者が主体となって症例提示を進めるための学習者中心の方法で、6つの段階からなる。症例を簡潔に要約し、鑑別診断を2〜3に絞り、それらを比較して分析し、不確かな点や迷う点を指導者に質問し、患者の管理計画を立て、最後に症例に関連した自己学習の課題を自ら選ぶ、という流れである。従来の、学習者が病歴と診察所見を報告し指導者が受け身に聞く提示の仕方と比べ、学習者が自分の思考と疑問を提示の中心に置く点に特徴がある。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5304
    source: 'Wolpaw TM, Wolpaw DR, Papp KK. SNAPPS: a learner-centered model for outpatient education. Acad Med. 2003;78(9):893-898'
    doi: 10.1097/00001888-200309000-00010
    pmid: '14507619'
    pmcid: null
    url: https://doi.org/10.1097/00001888-200309000-00010
    source_license: © Association of American Medical Colleges（Academic Medicine、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 6段階の内容は原著の抄録で確認し、自作の文で記載した。原著のパイロット研究は医学生と指導者の反応をみた小規模なもので、学習成果への効果の検証は本カードの主張に含めていない。ME-028（ワンミニッツプリセプター）が指導者側の進め方であるのに対し、本カードは学習者側の提示の進め方を扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-030
  domain: ME
  subdomain: ティーチング＆ラーニング
  assertion:
    plain_statement_ja: ベッドサイド教育（患者のそばで行う教育）は、診察技能の修得に役立つだけでなく、患者・学習者・指導者のいずれからも好意的に受け止められてきた教育方法であるが、その実施は減少傾向にある。文献レビューでは、減少の背景として、入院期間の短縮と患者の回転の速さ、患者のプライバシーへの配慮、診断における技術への依存の高まりが挙げられている。対策としては、研修医やインターンを指導役に活用すること、教員にベッドサイド教育の重要性と進め方の要点を伝えることなどが提案されている。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5305
    source: 'Peters M, Ten Cate O. Bedside teaching in medical education: a literature review. Perspect Med Educ. 2014;3(2):76-88'
    doi: 10.1007/s40037-013-0083-y
    pmid: '24049043'
    pmcid: PMC3976479
    url: https://doi.org/10.1007/s40037-013-0083-y
    source_license: CC BY（Perspectives on Medical Education、Europe PMC の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 主張は抄録で確認した範囲（臨床診断技能への効果、患者・学習者・指導者の受け止め、減少の理由と対策の方向性）に基づく。効果の大きさを示す数値は原著の抄録にないため含めていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-031
  domain: ME
  subdomain: ティーチング＆ラーニング
  assertion:
    plain_statement_ja: 省察（リフレクション）は、経験を振り返って意味づけ直す過程であり、医療専門職の能力の基盤の一つとされる。学部・卒後・生涯教育の各段階で省察を促す活動が取り入れられているが、医療専門職教育における省察と省察的実践の系統的レビューでは、その効果や影響を裏づける根拠は主に理論的なものにとどまり、研究文献も複数の分野に分散していて、どのような働きかけが有効かはまだ明らかでないとされている。省察を促す方法や、評価との関係づけは、教育設計上の検討課題として残されている。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5306
    source: 'Mann K, Gordon J, MacLeod A. Reflection and reflective practice in health professions education: a systematic review. Adv Health Sci Educ. 2009;14(4):595-621'
    doi: 10.1007/s10459-007-9090-2
    pmid: '18034364'
    pmcid: null
    url: https://doi.org/10.1007/s10459-007-9090-2
    source_license: © Springer（Advances in Health Sciences Education、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は抄録で確認した範囲（省察の位置づけ、根拠の性質、文献の分散）に基づく。Kolb の経験学習サイクルなどの個別の理論モデルは原著の本文の範囲であり、本カードには含めていない。ME-022（ポートフォリオ）は省察の記録と評価の媒体を扱うもので、本カードは学習過程としての省察そのものを扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-032
  domain: ME
  subdomain: ティーチング＆ラーニング
  assertion:
    plain_statement_ja: 自己主導型学習（学習者が自分の学習ニーズを把握し、目標と資源を選び、成果を振り返る学習法）は、医療専門職教育で従来型の教授法と比べて知識の習得で中程度の改善と結びつくことが系統的レビューで示されている。59件の研究（学習者8,011人）を統合した結果、知識領域では標準化平均差0.45（95%信頼区間 0.23〜0.67）と自己主導型学習が上回った一方、技能領域（標準化平均差0.05）と態度領域（同0.39）では統計学的に有意な差は認められなかった。学習資源の選択に学習者が関わる場合に効果が大きく、上級の学習者で利益が大きい傾向も報告されている。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5307
    source: 'Murad MH, Coto-Yglesias F, Varkey P, Prokop LJ, Murad AL. The effectiveness of self-directed learning in health professions education: a systematic review. Med Educ. 2010;44(11):1057-1068'
    doi: 10.1111/j.1365-2923.2010.03750.x
    pmid: '20946476'
    pmcid: null
    url: https://doi.org/10.1111/j.1365-2923.2010.03750.x
    source_license: © Wiley（Medical Education、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値（59件、学習者8,011人、各領域の標準化平均差と信頼区間）は原著の抄録で確認した。統合した研究間の異質性はいずれの解析でも有意であり、研究の方法論の質は中程度と評価されている。対象は医療専門職教育全般で、医師教育に限った結果ではない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-033
  domain: ME
  subdomain: ティーチング＆ラーニング
  assertion:
    plain_statement_ja: ピア学習（学習者同士が教え合う形式）は、医学教育で広く実践されており、その根拠として、教員の指導負担の軽減、下級生にとってのロールモデルの提供、学習の動機づけの高まり、将来教育者となる医師の準備になることなど、12の理由が文献の整理から挙げられている。とりわけ、教える側と学ぶ側の学年の差が小さい近ピア（ニアピア）指導は、教える側・学ぶ側の双方と教育組織のいずれにとっても有益とされる。教える側の学生は、見習いと熟練者の中間に位置する存在として、教えること自体を通じて学ぶ面がある。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5308
    source: 'Ten Cate O, Durning S. Peer teaching in medical education: twelve reasons to move from theory to practice. Med Teach. 2007;29(6):591-599'
    doi: 10.1080/01421590701606799
    pmid: '17922354'
    pmcid: null
    url: https://doi.org/10.1080/01421590701606799
    source_license: © Taylor & Francis（Medical Teacher、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は抄録で確認した範囲（2006年の医学教育文献の調査に基づく実践状況と12の理由の整理）に基づく。12の理由の全項目の列挙は本文の範囲のため含めていない。効果量を示すメタ解析ではなく、実践の根拠を整理した論考である。ME-023（TBL）はチームで課題に取り組む学習手順が主題であり、本カードとは扱う形式が異なる。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-034
  domain: ME
  subdomain: ティーチング＆ラーニング
  assertion:
    plain_statement_ja: マスタリー学習は、全ての学習者があらかじめ定められた到達基準に達するまで、意図的練習と再評価を繰り返す学習方式である。シミュレーションと組み合わせたマスタリー学習（SBML）の研究を批判的にレビューした検討（23件）では、教育現場内の成果にとどまらず、診療実践の改善、患者アウトカムの改善、さらには波及効果といった下流の転帰まで測定した研究が蓄積されていることが示された。こうした成果は、単発の介入ではなく、テーマを持って継続・蓄積される教育と医療サービスの統合的な研究プログラムから生じているとされる。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5309
    source: 'McGaghie WC, Issenberg SB, Barsuk JH, Wayne DB. A critical review of simulation-based mastery learning with translational outcomes. Med Educ. 2014;48(4):375-385'
    doi: 10.1111/medu.12391
    pmid: '24606621'
    pmcid: null
    url: https://doi.org/10.1111/medu.12391
    source_license: © Wiley（Medical Education、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は抄録で確認した範囲（23件の批判的レビュー、転帰の段階 T1〜T4）に基づく。効果量を統合したメタ解析ではなく、数値は含めていない。ME-009 の出典 SRC-5112（McGaghie ら 2011、意図的練習つきシミュレーションと従来型臨床教育の比較メタ解析）とは別論文であり、重複登録でないことを DOI で確認した。本カードは「基準到達まで繰り返す」という学習設計の枠組みを主題とする。
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
| ME-026 | （空欄：教育者向け理論のため付けない） | （空欄） |
| ME-027 | （空欄：同上） | （空欄） |
| ME-028 | （空欄：同上） | （空欄） |
| ME-029 | （空欄：同上） | （空欄） |
| ME-030 | （空欄：同上） | （空欄） |
| ME-031 | （空欄：同上） | （空欄） |
| ME-032 | （空欄：同上） | （空欄） |
| ME-033 | （空欄：同上） | （空欄） |
| ME-034 | （空欄：同上） | （空欄） |

## 4. 未解決事項

1. TL-1（ME-026）：認知負荷理論の AMEE Guide は RESTRICTED のままとした。同じ内容を裏づける CC BY の総説は今回の探索（Europe PMC）では特定できなかった。本文（購読制）の各論（負荷の測定法など）は主張に含めていない。
2. TL-2（ME-027）：主出典は2026年刊行の新しいメタ解析で、数値は抄録で確認した。本文での対象研究の内訳確認は取り込み側の判断に委ねる。テスト効果の古典的原著（検索練習の実験研究）は出典に含めていない。
3. TL-3（ME-028）：マイクロスキルの原典（Neher ら 1992）は出典登録せず、uncertainty に書誌を記した。登録が必要なら取り込み側で判断されたい。
4. TL-8（ME-033）：12の理由の全項目は本文の範囲のため主張に含めていない。

## 5. 引き継ぎメモ

- 新規出典は10件（SRC-5300〜5309）。出典マスター全体（最新版）と DOI・PMID で照合し、いずれも未登録であることを確認した。既存出典の再利用は本ファイルでは0件。（当初このメモに「9件」と書いていたのは数え違いで、検証指摘により訂正した）
- ME-034 の主出典（McGaghie ら 2014）は ME-009 の出典 SRC-5112（McGaghie ら 2011）と著者が重なるが別論文であり、重複登録ではない。
- 第3弾の残りは AS（ME-035〜044）、CD（ME-045〜053）、EM（ME-054〜061）、IT（ME-062〜071）で、別ファイルに分けた。

## 6. 検証指摘への修正記録（2026-11-24）

レポジトリ側の検証で指摘された点について、本ファイルでは次の修正を行った。

1. 引き継ぎメモの新規出典の件数を「9件」から「10件（SRC-5300〜5309）」に訂正した。
2. 冒頭の「CC BY の総説で同じ内容を裏づけられるものは主出典にした（TL-2）」という記述を、実態どおりに書き直した。TL-2（ME-027）では CC BY の論文（SRC-5302）は主出典ではなく裏づけ（corroboration）側にある。
