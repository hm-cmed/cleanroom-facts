# 医療者教育（ME）第3弾 分割案：5領域の候補一覧と出典の見通し

作成：2026-11-24（モコ）。今回は分割案のみで、カード本文は書いていない。
作業前に取得したレポジトリ：hm-cmed/cleanroom-facts 最新版、コミット `9591384836801b235a14e09c2df222d19c98907c`（2026-11-24）。出典マスター（sources.yaml、2,493件）と ME-001〜025 の登録内容はこの版で確認した。
仮番号：カードは取り込み時に ME-026 から付番。新規出典は SRC-5300〜5399 の範囲で仮番号を振った（既存マスター再利用の出典はその番号を書いた）。
識別子は Europe PMC API か発行元の公式ページで確認できたものだけを書いた。確認できていないものは「確認の状態」にその旨を書いた。主張の要旨は自分の言葉で書いており、定義文・結論文の和訳を前提にした候補はない。数値は、論文本文で確認していないものは書いていない（要旨では定性的な表現に留めた）。

## 0. 重なり確認の結果（先に実施）

### 0-1. ME-001〜025 で対応できる論点（新規候補にしない）

| 論点 | 対応する既存カード |
|---|---|
| フィードバックの定義と臨床教育での位置づけ | ME-008 |
| シミュレーション教育の効果（従来型臨床教育との比較）・有効なシミュレーションの特徴 | ME-009・ME-013 |
| PBL のアウトカム | ME-014 |
| 反転授業の効果 | ME-015 |
| TBL の進め方と効果 | ME-023 |
| OSCE（臨床実習前）の枠組み | ME-003 |
| Miller のピラミッド | ME-006 |
| EPA と entrustment | ME-007（裏づけに既存 SRC-5110 もあり） |
| 共用試験 CBT の仕組み | ME-011 |
| プログラム的評価 | ME-012 |
| ポートフォリオ評価の効果と限界 | ME-022 |
| コア・カリキュラムの位置づけ | ME-001 |
| 臨床研修の到達目標 | ME-005 |
| FD の効果（BEME レビュー） | ME-017 |
| 専門医制度の枠組み | ME-020 |
| インターネット基盤学習の効果 | ME-016 |
| 患者安全カリキュラム（WHO）・IPE の枠組み（WHO） | ME-024・ME-025 |
| 医学生の抑うつ・医師の燃え尽きへの介入 | ME-018・ME-019 |

### 0-2. ME 以外の章の全文検索

最新版の全章（107ファイル）を「生成AI」「大規模言語モデル」「e ラーニング」「シミュレーション」「人工知能」「機械学習」等で検索した。教育や生成 AI の教育利用に触れるカードは**なかった**。ヒットしたのは DT-032（ダーモスコピーの診断精度で人工知能に言及）、RE-022・RE-027（ぶどう膜炎分類基準の機械学習）、TR-013（耳介血腫）で、いずれも臨床の話題であり教育の論点ではない。生成 AI の教育利用は ME 章でも未着手（ME-016 が IT 領域で唯一の既存カード）。

### 0-3. 出典マスターの再利用の見通し

教育分野で再利用できる既存出典は、ME 第1・2弾で登録した SRC-5101〜5133 と SRC-5235（ME-010 の現行出典）、および SRC-5110（ten Cate らの EPA 総説、OPEN）・SRC-5119（反転授業メタ解析、OPEN）などに限られる。Kern、Kirkpatrick、Angoff 法、mini-CEX、WFME/JACME、文科省の生成 AI 文書、LLM の試験成績の研究はいずれもマスターにないため、新規出典が中心になる。

## 1. 領域ごとの候補表

### TL ティーチング＆ラーニング（9件）

| # | 領域 | 仮タイトル | 主張の要旨 | 既存カードとの関係 | 出典の候補（書誌・識別子） | 区分の見立て | 確認の状態 |
|---|---|---|---|---|---|---|---|
| TL-1 | TL | 認知負荷理論と教材・授業の設計 | 学習者の作業記憶には限りがあり、課題そのものの負荷と、提示の仕方による余分な負荷を分けて考えることで、教材や実習の設計を工夫できるという理論枠組み。 | 新規。ME-013（シミュレーションの特徴）とは別の理論 | Young JQ, Van Merriënboer J, Durning S, Ten Cate O. Cognitive Load Theory: implications for medical education: AMEE Guide No. 86. Med Teach. 2014. PMID: 24593808 / DOI: 10.3109/0142159X.2014.889290（仮 SRC-5300） | RESTRICTED（AMEE Guide、CC 表示なし） | 識別子は Europe PMC で確認済み（2026-11-24）。CC BY の総説で同じ内容を裏づけられるかは取り込み時に探索 |
| TL-2 | TL | テスト効果と間隔反復 | 学んだ内容を思い出すテストを繰り返すこと（検索練習）と、学習を時間間隔をあけて繰り返すこと（間隔反復）は、再読などの学習法より長期の保持に有利とする研究の蓄積がある。 | 新規 | The Effectiveness of Spaced Repetition in Medical Education: A Systematic Review and Meta-Analysis. Clin Teach. 2026（仮 SRC-5301）。裏づけ候補：A Systematic Review of Spaced Repetition, Retrieval Practice, and Academic Performance in Undergraduate Medical Education. Cureus. 2026. PMID: 42866698（仮 SRC-5302） | SRC-5301 は RESTRICTED 見立て（誌は OA ではない）。SRC-5302 は OPEN（Cureus は CC BY） | SRC-5302 の識別子は Europe PMC で確認済み。SRC-5301 は DOI 10.1111/tct.70353 を同 API で確認。数値は取り込み時に本文で確認する |
| TL-3 | TL | ワンミニッツプリセプター（5つのマイクロスキル） | 外来・病棟の短い指導場面で、学習者に考えを言わせ、根拠を尋ね、一般原則を教え、良い点を認め、誤りを正す、という5つの手順で指導を組み立てる方法。 | 新規。ME-008（フィードバック）とは手順の提示という点で別 | Neher JO, et al. The one-minute preceptor: shaping the teaching conversation. Fam Med. 2003. PMID: 12817861（仮 SRC-5303）。原典は Neher らの1992年のマイクロスキル論文 | RESTRICTED（CC 表示なし） | PMID は Europe PMC で確認済み。1992年原典の識別子は取り込み時に照合 |
| TL-4 | TL | SNAPPS（学習者中心の症例提示法） | 学習者が症例を要約し、鑑別を絞り、分析し、不確かな点を指導者に尋ね、管理計画を立て、自己学習の課題を選ぶ、という6段階で症例提示を進める学習者中心の方法。 | 新規。TL-3 と対をなす指導法 | Wolpaw TM, Wolpaw DR, Papp KK. SNAPPS: a learner-centered model for outpatient education. Acad Med. 2003. PMID: 14507619 / DOI: 10.1097/00001888-200309000-00010（仮 SRC-5304） | RESTRICTED | 識別子は Europe PMC で確認済み |
| TL-5 | TL | ベッドサイド教育の位置づけと工夫 | 患者のそばで行う教育は、診察技能だけでなく、患者との関係や専門職としての姿勢を学ぶ場になる一方、実施は減っており、進め方の工夫が文献で整理されている。 | 新規 | Peters M, ten Cate O. Bedside teaching in medical education: a literature review. Perspect Med Educ. 2014. PMID: 24049043 / PMCID: PMC3976479 / DOI: 10.1007/s40037-013-0083-y（仮 SRC-5305） | OPEN（CC BY、Europe PMC のライセンス欄で確認） | 確認済み |
| TL-6 | TL | 経験学習と省察（リフレクション） | 臨床経験そのものだけでは学びにならず、経験を振り返って意味づけし直す省察が学習を支える。省察の促し方や評価との関係が系統的レビューで整理されている。 | 新規。ME-022（ポートフォリオ）は省察の記録媒体の話で、こちらは学習過程の理論 | Mann K, Gordon J, MacLeod A. Reflection and reflective practice in health professions education: a systematic review. Adv Health Sci Educ. 2009. PMID: 18034364 / DOI: 10.1007/s10459-007-9090-2（仮 SRC-5306） | RESTRICTED | 識別子は Europe PMC で確認済み |
| TL-7 | TL | 自己主導型学習（SDL）の効果 | 学習者が自分の学習ニーズを把握し、資源を選び、振り返る自己主導型学習は、従来型の学習と比べて知識の習得で劣らず、条件によっては有利とする系統的レビューの結果がある。 | 新規。成人学習（アンドラゴジー）の実証面 | Murad MH, Coto-Yglesias F, Varkey P, Prokop LJ, Murad AL. The effectiveness of self-directed learning in health professions education: a systematic review. Med Educ. 2010. PMID: 20946476 / DOI: 10.1111/j.1365-2923.2010.03750.x（仮 SRC-5307） | RESTRICTED | 識別子は Europe PMC で確認済み。効果の数値は取り込み時に本文で確認する |
| TL-8 | TL | ピア学習（ピア・アシステッド・ラーニング） | 学習者同士が教え合う形式は、教える側・教わる側の双方の学習に役立つとされ、医学教育でも近ピア（ニアピア）指導を含め実施と検証が進んでいる。 | 新規。ME-023（TBL）はチーム学習の手順が主題で別 | Ten Cate O, Durning S. Peer teaching in medical education: twelve reasons to move from theory to practice. Med Teach. 2007（仮 SRC-5308）。近年の裏づけ候補として BMC Med Educ 等のピアチューター制のレビュー | RESTRICTED 見立て | 書誌は原典として周知のものだが、識別子は今回未確認。取り込み時に API で照合し、CC BY の新しいレビューがないか併せて探索する |
| TL-9 | TL | マスタリー学習（到達基準まで繰り返す学習） | 全員が定められた到達基準に達するまで、意図的練習と再評価を繰り返す学習方式で、シミュレーションと組み合わせた研究では技能や患者アウトカムまで含めた効果がメタ解析で検証されている。 | ME-009（意図的練習つきシミュレーション）と近接するが、こちらは「基準到達まで繰り返す」学習設計の枠組みが主題 | McGaghie WC, Issenberg SB, Barsuk JH, Wayne DB. A critical review of simulation-based mastery learning with translational outcomes. Med Educ. 2014／同著者らの Acad Med のメタ解析（仮 SRC-5309） | RESTRICTED 見立て | 今回は候補の同定まで。正確な書誌と識別子は取り込み時に API で確定する（ME-009 の出典 SRC-5112 と著者が重なるため、重複登録にならないよう照合が必要） |

### AS アセスメント（10件）

| # | 領域 | 仮タイトル | 主張の要旨 | 既存カードとの関係 | 出典の候補（書誌・識別子） | 区分の見立て | 確認の状態 |
|---|---|---|---|---|---|---|---|
| AS-1 | AS | 評価の妥当性（Messick／Kane の考え方） | 評価の妥当性は、テスト自体の性質ではなく、その結果の解釈と使い方が正当化できるかで判断する。根拠は内容・反応過程・内的構造・他変数との関係・結果の5つの面から集める（Messick）、あるいは解釈から利用までの推論の連なりで検証する（Kane）。 | 新規。ME-012（プログラム的評価）の前提理論 | Cook DA, Beckman TJ. Current concepts in validity and reliability for psychometric instruments: theory and application. Am J Med. 2006. PMID: 16443422 / DOI: 10.1016/j.amjmed.2005.10.036（仮 SRC-5310） | RESTRICTED | 識別子は Europe PMC で確認済み |
| AS-2 | AS | 評価の有用性の式（van der Vleuten 1996） | 評価方法の有用性は、信頼性・妥当性・教育への効果・受け入れやすさ・コストの積で考えられ、どれか一つがゼロなら有用性全体が成り立たない、という枠組み。目的に応じて各要素の重みづけを変える。 | ME-012 と関連（プログラム的評価のモデル論文 SRC-5116 でも有用性が論じられるが、式そのものの原典はこちら） | van der Vleuten CPM. The assessment of professional competence: developments, research and practical implications. Adv Health Sci Educ. 1996. PMID: 24178994 / DOI: 10.1007/BF00596229（仮 SRC-5311） | RESTRICTED | 識別子は Europe PMC で確認済み |
| AS-3 | AS | 合格基準の設定（Angoff 法などの標準設定） | 合否の境目は、試験の出来とは別に、専門家が「最低限できる受験者」を想定して判断を積み上げる標準設定の手続きで決める。Angoff 法が代表的で、方法ごとに前提と限界が異なる。 | 新規。ME-003・ME-011（OSCE・CBT）の合否判定の前提 | Norcini JJ. Setting standards on educational tests. Med Educ. 2003. PMID: 12709190 / DOI: 10.1046/j.1365-2923.2003.01495.x（仮 SRC-5312） | RESTRICTED | 識別子は Europe PMC で確認済み |
| AS-4 | AS | OSCE の境界群法・境界回帰法 | OSCE では、各ステーションのチェックリスト得点と全体評価の関係から合否の境目を推定する境界回帰法などが使われ、判定者の全体評価を基準設定に組み込む点が特徴。 | ME-003（OSCE の枠組み）の発展。AS-3 の応用法 | Kramer A, et al. Med Educ. 2003（境界群法）／Pell G, et al.（境界回帰法の実務解説）（仮 SRC-5313） | RESTRICTED 見立て | 書誌の確定と識別子の照合は取り込み時に行う。CC BY の実務解説があればそちらを優先する |
| AS-5 | AS | mini-CEX と DOPS の教育効果 | 職場で直接観察してその場でフィードバックする mini-CEX と DOPS は、学習者の行動変容や自己評価の変化など、形成的評価としての教育効果が系統的レビューで整理されている。 | 新規。ME-008（フィードバック）・ME-007（EPA）の間をつなぐ職場評価 | Lörwald AC, Lahner FM, Nouns ZM, Berendonk C, Norcini J, Huwendiek S. The educational impact of Mini-Clinical Evaluation Exercise (Mini-CEX) and Direct Observation of Procedural Skills (DOPS): a systematic review. PLoS One. 2018. PMID: 29864130 / PMCID: PMC5986126 / DOI: 10.1371/journal.pone.0198009（仮 SRC-5314） | OPEN（CC BY、Europe PMC で確認） | 確認済み。効果の内訳は取り込み時に本文で確認する |
| AS-6 | AS | 職場基盤型評価（WBA）の考え方 | 診療現場での直接観察に基づく評価は、試験場の評価では測れない実際の仕事ぶりを扱う一方、評価者の負担や判定のばらつきが課題で、複数回の観察を積み重ねる設計が前提になる。 | AS-5 の総論版。ME-007（EPA）の評価面 | Norcini J, Burch V. Workplace-based assessment as an educational tool: AMEE Guide No. 31. Med Teach. 2007（仮 SRC-5315） | RESTRICTED（AMEE Guide） | 書誌は周知のものだが識別子は今回未確認。取り込み時に照合 |
| AS-7 | AS | 良い評価の合意枠組み（オタワ 2018） | 評価の専門家会議（オタワ会議）が、個々の評価と評価プログラムの両方について「良い評価」の基準を合意文書として示した。妥当性・再現性・同等性・実施可能性・教育効果・触媒効果・受け入れ可能性が柱。 | AS-1・AS-2 の現代版の整理。ME-012 とも関連 | Norcini J, Anderson MB, Bollela V, et al. 2018 Consensus framework for good assessment. Med Teach. 2018. PMID: 30299187 / DOI: 10.1080/0142159X.2018.1500016（仮 SRC-5316） | RESTRICTED（Europe PMC で OA でないことを確認） | 識別子は確認済み |
| AS-8 | AS | 多肢選択問題の作問（作問上の欠陥の影響） | 問題文の欠陥（手がかりを与える書き方、曖昧な表現など）は、知識とは無関係に正答率や合否を左右しうる。欠陥のある問題の割合と受験者への影響が実証研究で示されている。 | 新規。ME-011（CBT）の問題の質の面 | Tarrant M, Ware J. の item-writing flaws 研究（Med Educ）／Downing SM. の作問総説（仮 SRC-5317）。CC BY の裏づけとして JEEHP（J Educ Eval Health Prof）等の作問ガイドを探索 | RESTRICTED 見立て（裏づけが CC BY で見つかれば OPEN） | 候補の同定まで。書誌・識別子は取り込み時に確定する |
| AS-9 | AS | 形成的評価と総括的評価の役割の違い | 学習の途中での形成的評価は改善のための情報を返すことが目的で、修了判定などの総括的評価とは設計も扱いも異なる。両者を一つの評価で兼ねると緊張関係が生じることが指摘されている。 | AS-7・ME-012 と関連するが、目的の区別そのものが主題 | 評価論の総説（Norcini らの 2018 枠組み SRC-5316 と併用可）。独立の裏づけ候補として MedEdPublish の総説（仮 SRC-5318） | RESTRICTED 見立て | 裏づけの確定は取り込み時。既存の SRC-5316 で足りる場合は新規出典なしで作れる可能性もある |
| AS-10 | AS | 多面評価（360度評価）の使い方 | 同僚・他職種・患者など複数の立場からの評価を集める多面評価は、コミュニケーションや専門職としての振る舞いの把握に使われ、信頼性には一定数の評価者が必要とされる。 | 新規。ME-022（ポートフォリオ）とは別の他者評価 | Donnon T, Al Ansari A, Al Alawi S, Violato C. The reliability, validity, and feasibility of multisource feedback in an internal medicine residency program. 等の系統的検討（仮 SRC-5319） | RESTRICTED 見立て | 候補の同定まで。書誌・識別子と CC BY の総説の有無は取り込み時に確認する |

### CD コースディベロップメント（9件）

| # | 領域 | 仮タイトル | 主張の要旨 | 既存カードとの関係 | 出典の候補（書誌・識別子） | 区分の見立て | 確認の状態 |
|---|---|---|---|---|---|---|---|
| CD-1 | CD | Kern の6段階カリキュラム開発 | カリキュラム開発を、問題の把握とニーズ評価、学習者のニーズ評価、目標と到達目標、教育方略、実施、評価とフィードバックの6段階で進める枠組み。評価を最後だけでなく循環として組み込む点が特徴。 | 新規。ME-001（コアカリ）・ME-005（到達目標）はこの枠組みの対象側 | Thomas PA, Kern DE, Hughes MT, Chen BY (eds). Curriculum Development for Medical Education: A Six-Step Approach. 3rd ed. Johns Hopkins University Press. 2016（書籍）（仮 SRC-5320） | RESTRICTED（教科書）。CC BY の総説・解説で同じ6段階を裏づけられるかを併記し、見つかればそちらを主出典にする | 書誌は周知のもの。CC BY の裏づけ候補の探索は取り込み時に行う |
| CD-2 | CD | アウトカム基盤型教育（OBE） | 教育の設計を、卒業時にできること（アウトカム）から逆向きに組み立てる考え方で、内容の網羅ではなく到達の明確化を起点にする。 | ME-001・ME-005 の理論的背景 | Harden RM, Crosby JR, Davis MH. AMEE Guide No. 14: Outcome-based education: Part 1 — An introduction to outcome-based education. Med Teach. 1999（仮 SRC-5321） | RESTRICTED（AMEE Guide） | 識別子は今回未確認。取り込み時に照合 |
| CD-3 | CD | コンピテンシー基盤型教育（CBME） | 時間（履修期間）ではなく、学習者が到達した能力を単位として教育を設計・評価する枠組み。国際的なワーキンググループが定義と構成要素を整理した。 | ME-007（EPA）は CBME の実装概念。こちらは枠組み全体 | Frank JR, Snell LS, Cate OT, et al. Toward a definition of competency-based education in medicine: a systematic review of published definitions. Med Teach. 2010. PMID: 20662573 / DOI: 10.3109/0142159X.2010.500898（仮 SRC-5322） | RESTRICTED | 識別子は Europe PMC で確認済み |
| CD-4 | CD | 構成的整合性（constructive alignment） | 意図した学習成果、学習活動、評価の3つを互いに整合させることが教育設計の原則で、評価が学習者の実際の学習行動を決めるため、整合の起点は成果と評価の対応にある。 | 新規。CD-2・CD-3 と関連 | Biggs J. Enhancing teaching through constructive alignment. High Educ. 1996／Biggs J, Tang C. の教科書（仮 SRC-5323） | RESTRICTED。CC BY の高等教育系総説で裏づけられるかを併記 | 識別子は今回未確認。取り込み時に照合し、CC BY の総説を探索する |
| CD-5 | CD | Bloom の分類（改訂版）と学習目標の記述 | 学習目標を認知領域の階層（記憶・理解・応用・分析・評価・創造）で記述する分類で、改訂版では知識の種類と認知過程の2つの軸で目標を整理する。目標記述と評価作りの共通言語として使われる。 | 新規。ME-005（到達目標の記述）の背景 | Anderson LW, Krathwohl DR (eds). A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives. 2001（書籍）（仮 SRC-5324） | RESTRICTED（書籍）。医学教育での利用を述べた CC BY 論文は多数あり、裏づけは確保しやすい見通し | 書籍の書誌は周知のもの。裏づけ論文の選定は取り込み時 |
| CD-6 | CD | SPICES モデル（カリキュラムの方向づけ） | カリキュラムの特徴を、学生中心か教師中心か、問題基盤か情報基盤か、統合か教科別か、地域基盤か病院基盤か、選択制か一律か、系統的か見習い的か、の6つの連続体で表すモデル。 | 新規 | Harden RM, Sowden S, Dunn WR. Educational strategies in curriculum development: the SPICES model. Med Educ. 1984（仮 SRC-5325） | RESTRICTED | 識別子は今回未確認。取り込み時に照合 |
| CD-7 | CD | スパイラル・カリキュラム | 同じ主題を、学年が上がるにつれて深さと複雑さを増しながら繰り返し学ぶ設計で、既習内容との結びつきと段階的な難化が条件になる。 | 新規。ME-001（コアカリの学年配置）と関連 | Harden RM, Stamper N. What is a spiral curriculum? Med Teach. 1999（仮 SRC-5326） | RESTRICTED | 識別子は今回未確認。取り込み時に照合 |
| CD-8 | CD | 隠れたカリキュラム | 公式のカリキュラムとは別に、組織の文化や現場の慣行を通じて学習者が学び取る規範や価値観があり、公式の教育意図と矛盾することがある。 | 新規 | Hafferty FW. Beyond curriculum reform: confronting medicine's hidden curriculum. Acad Med. 1998（仮 SRC-5327）。裏づけ候補：Lawrence C, et al. The hidden curriculum in medical education: a scoping review. Acad Med. 2019 | RESTRICTED 見立て | 候補の同定まで。識別子とスコーピングレビューの OA 状況は取り込み時に確認する |
| CD-9 | CD | 統合カリキュラム（統合のはしご） | 教科ごとの教育から、主題を中心に複数教科を束ね、学際的に統合する教育までを段階（はしご）で表し、統合の進め方と各段階の特徴を整理した枠組み。 | 新規。ME-001 のカリキュラム形態の面 | Harden RM. The integration ladder: a tool for curriculum planning and evaluation. Med Educ. 2000（仮 SRC-5328） | RESTRICTED | 識別子は今回未確認。取り込み時に照合 |

### EM 教育管理（8件）

| # | 領域 | 仮タイトル | 主張の要旨 | 既存カードとの関係 | 出典の候補（書誌・識別子） | 区分の見立て | 確認の状態 |
|---|---|---|---|---|---|---|---|
| EM-1 | EM | Kirkpatrick の4段階プログラム評価 | 教育プログラムの評価を、参加者の反応、学習の到達、行動の変化、組織の成果の4段階で捉える枠組み。上の段階ほど評価は難しく、医学教育の研究では下の段階の評価が多いことが批判的に検討されている。 | 新規 | Kirkpatrick DL. の原典（書籍、1959年の論文群が起源）（仮 SRC-5330）。批判的検討：Yardley S, Dornan T. Kirkpatrick's levels and education 'evidence'. Med Educ. 2012（仮 SRC-5331） | RESTRICTED（原典・総説とも）。CC BY の総説で枠組み自体を裏づけられるかを併記 | 識別子は今回未確認。取り込み時に照合し、CC BY の総説を探索する |
| EM-2 | EM | WFME の医学教育世界基準（2020年改訂） | 世界医学教育連盟（WFME）が、基礎医学教育の質改善のための世界基準を示しており、各国の分野別評価はこの基準を参照して行われる。2020年に改訂版が出た。 | 新規。EM-3（JACME）の国際的な前提 | World Federation for Medical Education. Global Standards for Quality Improvement in Basic Medical Education (2020 revision). WFME（仮 SRC-5332） | RESTRICTED 見立て（WFME の著作物。無償公開でも CC 表示は確認できていない） | 文書の存在と改訂年は WFME 公式サイトで確認する前提で記載。ライセンス表示の確認は取り込み時 |
| EM-3 | EM | 日本の医学教育の分野別評価（JACME） | 日本医学教育評価機構（JACME）が、WFME の認定を受けた機関として、医学部の教育プログラムを世界基準に基づく日本版の基準で評価・認定する。分野別評価は機関別認証評価とは別の仕組み。 | 新規。ME-020（専門医制度）は卒後の制度で別 | 日本医学教育評価機構「医学教育分野別評価基準日本版」（仮 SRC-5333）。制度の位置づけの裏づけに文部科学省の高等教育関係ページ（GOV_JP） | JACME 文書は RESTRICTED 見立て（一般社団法人の著作物）。文科省ページは GOV_JP | JACME 文書の版と公表日は取り込み時に公式サイトで確認する |
| EM-4 | EM | FD の義務化（大学設置基準） | 大学設置基準で、大学は授業の内容・方法の改善のための組織的な研修（FD）の実施が義務づけられている。FD の「効果」の話（ME-017）とは別に、制度としての根拠はこちら。 | ME-017（FD の効果レビュー）と対になる制度面 | 大学設置基準（昭和31年文部省令第28号）第25条の3。e-Gov 法令検索（仮 SRC-5334） | GOV_JP（法令） | 条文番号は法令の現行形で取り込み時に e-Gov で再確認する |
| EM-5 | EM | 3つのポリシー（DP・CP・AP） | 大学は、卒業認定・学位授与の方針（DP）、教育課程編成・実施の方針（CP）、入学者受入れの方針（AP）の3つの方針を、学校教育法施行規則に基づいて定めて公表することとされている。 | 新規。CD 領域の設計とも関係するが、根拠は制度 | 学校教育法施行規則第165条の2。e-Gov 法令検索（仮 SRC-5335） | GOV_JP（法令） | 条文番号は取り込み時に e-Gov で再確認する |
| EM-6 | EM | 教学マネジメント指針 | 中央教育審議会大学分科会が、学修者本位の教育への転換のため、大学が教学マネジメント（3つのポリシーを起点とする教育の PDCA）を確立する指針を2020年に示した。 | EM-5 の運用面 | 中央教育審議会大学分科会「教学マネジメント指針」2020年1月22日。文部科学省（仮 SRC-5336） | GOV_JP | 公表日は文科省の公表資料で確認済みの範囲で記載。取り込み時に公式ページで再確認する |
| EM-7 | EM | 機関別認証評価の仕組み | 大学は、学校教育法により、文部科学大臣の認証を受けた評価機関による評価（認証評価）を定期的に受けることとされている。分野別評価（EM-3）とは対象も目的も異なる。 | EM-3 と対をなす制度 | 学校教育法第109条。e-Gov 法令検索（仮 SRC-5337） | GOV_JP（法令） | 条文は取り込み時に e-Gov で再確認する |
| EM-8 | EM | プログラム評価の進め方（評価計画とモデル） | 教育プログラムの評価は、成果の測定だけでなく、評価の目的・問い・方法を事前に設計して行う。ロジックモデルや CIPP などのモデルが計画の道具として使われる。 | EM-1（Kirkpatrick）の実務面 | Frye AW, Hemmer PA. Program evaluation models and related theories: AMEE Guide No. 67. Med Teach. 2012（仮 SRC-5338） | RESTRICTED（AMEE Guide） | 識別子は今回未確認。取り込み時に照合 |

### IT ICT を用いた教育（生成 AI を含む）（10件）

情報の時点：この領域の候補は 2026-11-24 時点の資料に基づく。生成 AI 関係は変化が速いため、各候補に出典の公表日を書いた。

| # | 領域 | 仮タイトル | 主張の要旨 | 既存カードとの関係 | 出典の候補（書誌・識別子） | 区分の見立て | 確認の状態 |
|---|---|---|---|---|---|---|---|
| IT-1 | IT | 大学における生成 AI の教学面の取扱い（文部科学省の周知） | 文部科学省は2023年7月、各大学・高専に対し、生成 AI の出力をそのまま用いてレポート等を作成することは一般に不適切であること、利用した場合は種類や箇所を明記させるなどの評価上の工夫、虚偽や個人情報の漏洩への注意を示し、各大学が実態に応じて指針を定め見直すことを求めた。 | 新規（生成 AI は全体で初） | 文部科学省 高等教育局「大学・高専における生成 AI の教学面の取扱いについて（周知）」2023年7月13日（仮 SRC-5340） | GOV_JP | 文科省の報道発表ページと別紙の内容を 2026-11-24 に確認。現時点でこの周知を置き換える大学向け文書は出ていない（初等中等教育向けガイドラインは別文書。§3 参照） |
| IT-2 | IT | UNESCO の生成 AI 教育ガイダンス（2023） | UNESCO は2023年、教育と研究における生成 AI について初の国際ガイダンスを出し、人間中心の原則、データプライバシーの保護、提供者への要件、教育機関が倫理的・教育的な適切さを検証することなどを示した。 | 新規。IT-1 の国際版 | UNESCO. Guidance for generative AI in education and research. 2023. DOI: 10.54675/EWZM9535 / ISBN 978-92-3-100612-8（仮 SRC-5341） | RESTRICTED（CC BY-SA 3.0 IGO。SA 系は本プロジェクトでは RESTRICTED 区分） | DOI とライセンス表示は UNESCO の出版物ページで確認済み（2026-11-24） |
| IT-3 | IT | WHO の大規模マルチモーダルモデル指針と医学教育 | WHO は2024年1月、生成 AI の一種である大規模マルチモーダルモデル（LMM）について、医療での倫理とガバナンスの指針を公表し、応用分野の一つに医学・看護教育（模擬患者との対話練習など）を挙げつつ、不正確な出力や自動化バイアスなどのリスクを示した。 | 新規 | World Health Organization. Ethics and governance of artificial intelligence for health: guidance on large multi-modal models. 2024年1月18日公表（仮 SRC-5342） | RESTRICTED 見立て（WHO の刊行物は All rights reserved が通例。第1弾の照合でも WHO 文書は RESTRICTED） | 公表日と内容の概要は WHO 公式発表で確認済み。ISBN・DOI と権利表示は取り込み時に刊行物本体で確認する |
| IT-4 | IT | LLM の医師国家試験形式問題の成績（USMLE、2023） | 2023年の検証で、ChatGPT（GPT-3.5 系）が USMLE 形式の問題で合格圏に近い成績を示したと報告され、LLM の医学知識の到達度と教育利用の議論の出発点になった。モデルと時点を特定して扱う必要がある。 | 新規 | Kung TH, et al. Performance of ChatGPT on USMLE: potential for AI-assisted medical education using large language models. PLOS Digit Health. 2023. PMID: 36812645 / PMCID: PMC9931230 / DOI: 10.1371/journal.pdig.0000198（仮 SRC-5343） | OPEN（CC BY、Europe PMC で確認） | 識別子は確認済み。具体的な正答率は取り込み時に本文で確認してから書く |
| IT-5 | IT | LLM と日本の医師国家試験（禁忌肢の検出、2025） | 日本の医師国家試験の問題を用いた 2025 年の検証では、LLM が禁忌肢（選ぶと不合格になりうる選択肢）の検出でどの程度の推論ができるかが検討されている。国試の成績はモデル名・版と試験年度をそろえて扱う。 | 新規。IT-4 の日本版 | The advanced reasoning capabilities of large language models for detecting contraindicated options in medical examinations（日本の医師国家試験を用いた研究）. JMIR Med Inform. 2025. PMID: 40354629 / PMCID: PMC12088613 / DOI: 10.2196/68527（仮 SRC-5344） | OPEN（CC BY、Europe PMC で確認） | 識別子は確認済み。対象モデルと成績の数値は取り込み時に本文で確認する。GPT-4 の国試成績の初期研究（2023年）も併せて照合し、より適切な主出典があれば差し替える |
| IT-6 | IT | 生成 AI の医学教育利用の総説（2025） | 生成 AI の医学教育への利用について、批判的思考を促す使い方と、学習を迂回させてしまう使い方の両面が総説で整理されており、カリキュラムへの組み込み方が論点になっている。 | 新規。IT-1〜IT-5 の総論 | Generative Artificial Intelligence in Medical Education: Enhancing Critical Thinking or Undermining It? J Med Internet Res. 2025. PMID: 41183320 / PMCID: PMC12624298 / DOI: 10.2196/76340（仮 SRC-5345） | OPEN（CC BY、Europe PMC で確認） | 識別子は確認済み。2026年に入っても新しい総説が出続けており、取り込み時点で最新の系統的レビューがないか再確認する |
| IT-7 | IT | 生成 AI 時代の学習評価と学術的誠実性 | 生成 AI の出力をそのまま提出する行為への対応として、利用の明記、小テストや口述試験の併用、AI 検出ツールの結果を過信しないことなど、評価の設計側の対応が国内・国際の指針で共通して示されている。 | IT-1・IT-2 と出典が重なるが、評価（AS）に近い独立の論点として候補化 | 主出典候補：文部科学省の周知（仮 SRC-5340、再利用）と UNESCO ガイダンス（仮 SRC-5341、再利用）。医学教育に限った裏づけとして MedEdPublish 等の総説（仮 SRC-5349） | GOV_JP＋RESTRICTED の組み合わせ見立て | 指針側は確認済み。医学教育固有の裏づけ論文は取り込み時に選定する |
| IT-8 | IT | バーチャル患者（仮想患者シミュレーション）の効果 | コンピュータ上の仮想患者との対話形式の学習は、医療専門職教育で知識や臨床推論などの改善が系統的レビュー・メタ解析で検証されている。 | ME-009・ME-013（シミュレーション）とは媒体が異なる（画面上の仮想患者） | Kononowicz AA, et al. Virtual patient simulations in health professions education: systematic review and meta-analysis by the Digital Health Education Collaboration. J Med Internet Res. 2019. PMID: 31267981 / PMCID: PMC6632099 / DOI: 10.2196/14676（仮 SRC-5346） | OPEN（CC BY、Europe PMC で確認） | 確認済み。効果量は取り込み時に本文で確認する |
| IT-9 | IT | VR（仮想現実）の医療専門職教育の効果 | VR を用いた教育は、従来の教育と比べて知識の習得では有利とするメタ解析がある一方、技能については証拠が限られるなど、アウトカムによって結果が異なる。 | ME-009・ME-013 と近接（シミュレーションの一形態） | Kyaw BM, et al. Virtual reality for health professions education: systematic review and meta-analysis by the Digital Health Education Collaboration. J Med Internet Res. 2019. PMID: 30668519 / PMCID: PMC6362387 / DOI: 10.2196/12959（仮 SRC-5347） | OPEN（CC BY、Europe PMC で確認） | 確認済み。効果の内訳は取り込み時に本文で確認する |
| IT-10 | IT | オンライン学習の効果（米国教育省のメタ解析） | 米国教育省が委託したメタ解析では、オンライン学習は対面のみの学習と比べて平均して同等以上で、対面とオンラインを組み合わせたブレンデッド学習で効果が大きい傾向が示された。医療専門職に限らない教育全般の証拠。 | ME-016（医療専門職のインターネット基盤学習）と近接。こちらは政府のメタ解析で対象が教育全般 | Means B, Toyama Y, Murphy R, Bakia M, Jones K. Evaluation of Evidence-Based Practices in Online Learning: A Meta-Analysis and Review of Online Learning Studies. U.S. Department of Education. 2010（仮 SRC-5348） | GOV_US | 報告書の存在は周知だが、版と URL は取り込み時に米国教育省のページで確認する |

## 2. 第1陣のおすすめ（13件）

| 順 | 候補 | 理由 |
|---|---|---|
| 1 | IT-1 文科省の生成 AI 周知 | 生成 AI は全体で未着手の一番大きな空白。GOV_JP で出典が固く、内容も評価・誠実性まで含む |
| 2 | IT-4 LLM の USMLE 成績（Kung 2023） | OPEN（CC BY）で識別子確認済み。生成 AI 論点の実証側の起点として扱いやすい |
| 3 | TL-5 ベッドサイド教育 | OPEN（CC BY）で確認済み。臨床教育の基本テーマで既存カードとの重なりがない |
| 4 | AS-5 mini-CEX と DOPS の教育効果 | OPEN（CC BY）で確認済み。日本の臨床研修でも使われる評価法で実務性が高い |
| 5 | AS-2 評価の有用性の式 | 評価領域の基礎理論。ME-012 とつながり、出典は原典が特定できている |
| 6 | AS-3 合格基準の設定 | OSCE・CBT の既存カードの前提になる理論で、空白が大きい |
| 7 | TL-1 認知負荷理論 | 学習理論の中心の一つ。AMEE Guide で出典が特定できている |
| 8 | TL-3 ワンミニッツプリセプター | 臨床現場の指導法として最も広く知られる手順。TL-4（SNAPPS）と対で第2陣に回してもよい |
| 9 | CD-1 Kern の6段階 | カリキュラム開発の標準枠組み。CD 領域の土台になる |
| 10 | CD-3 CBME | EPA（ME-007）の上位枠組みで、国際的にも中心テーマ |
| 11 | EM-1 Kirkpatrick の4段階 | プログラム評価の共通言語。医学教育以外からの引用も多く汎用性が高い |
| 12 | EM-4 FD の義務化 | GOV_JP（法令）で作りやすく、ME-017 と制度・効果の対になる |
| 13 | IT-8 バーチャル患者 | OPEN（CC BY）で確認済み。ME-016・ME-009 と並ぶ ICT 教育の柱 |

残りの候補は第2陣以降で、出典の裏づけ（CC BY の総説の有無）の確認が済んだものから順に進めるのがよい。

## 3. 対象範囲で迷った点

1. **初等中等教育向けの生成 AI ガイドライン（文科省、2024年12月に改訂版）を入れるか。** 医学教育は高等教育が対象のため、IT-1 は大学向けの周知（2023年）に絞った。学校教育のガイドラインは内容が具体的で参照されることも多いが、対象（児童生徒と教員）が異なるため、入れる場合は別候補として判断が要る。
2. **医師以外の職種の教育資料をどこまで入れるか。** JMIR 系の系統的レビュー（IT-8・IT-9 など）は「医療専門職教育」として看護・薬学等を含むものが多い。ME の既存カード（ME-015・016）も医療専門職教育の研究を採用してきたので、それに倣ったが、医師教育に限る場合は候補の絞り込みが必要になる。
3. **UNESCO ガイダンスの区分。** CC BY-SA 3.0 IGO で公開されているが、本プロジェクトの区分では SA 系は RESTRICTED になる（ライセンス照合第1・2回の基準と同じ）。「自由に使える資料」としての期待と区分がずれる点を明記した。
4. **LLM の試験成績は時点の指定が必須で、陳腐化が速い。** IT-4・IT-5 はモデル名・版・試験年度を固定して書く前提の候補だが、取り込み時点ではさらに新しいモデルでの研究が出ている可能性が高い。カード化の際に「いつの時点の成績か」を uncertainty に書く運用が要る。
5. **製品名（ChatGPT 等）を仮タイトルに出すか。** IT-4 は原論文の題名に製品名が含まれるため出典としては避けられないが、カードのタイトルでは「LLM の〜」と一般名にした。宣伝と読まれないよう、本文でも製品名は出典の範囲に留めるのがよい。
6. **Kirkpatrick と Means（IT-10）は医学教育に固有の出典ではない。** どちらも教育一般の枠組み・証拠で、ME 章に入れるかは章の性格づけに関わる。Kirkpatrick は医学教育での使用が定着しているため残し、Means は ME-016 との近さもあり優先度を下げた。
7. **法令を出典にする候補（EM-4・EM-5・EM-7）の作り方。** 条文そのものは短く、カードの主張は制度の説明になる。既存の ME-002・ME-004（医師法）と同じ作りでよいか、確認が要る。

## 4. 既存カードの subdomain 付け替え提案

現行の subdomain は「制度・評価・教育手法・横断」の4種。5領域（TL・AS・CD・EM・IT）と「制度」への付け替え案は次のとおり。原則として、依頼文 §2 の当てはめに従い、法令・資格制度そのものが主題のものだけを「制度」に残した。

| カード | 現行 | 提案 | 理由 |
|---|---|---|---|
| ME-001 コア・カリキュラム | 制度 | CD | カリキュラムの枠組みそのものが主題 |
| ME-002 共用試験の法的位置づけ・Student Doctor | 制度 | 制度（据え置き） | 医師法改正が主題 |
| ME-003 臨床実習前 OSCE | 制度 | AS | 評価手法が主題 |
| ME-004 臨床研修の必修化 | 制度 | 制度（据え置き） | 医師法の義務規定が主題 |
| ME-005 臨床研修の到達目標 | 制度 | CD | 到達目標＝アウトカム設計が主題（制度面も強いので併記も可） |
| ME-006 Miller のピラミッド | 評価 | AS | 評価の枠組み |
| ME-007 EPA | 評価 | AS | 評価・任せ方の枠組み |
| ME-008 フィードバック | 評価 | TL | 教授・学習の過程が主題 |
| ME-009 シミュレーションと意図的練習 | 教育手法 | TL | 学習法が主題 |
| ME-010 医師憲章（プロフェッショナリズム） | 横断 | 横断（残置を提案） | 5領域のどれにも当てはまらない。無理に分けず横断を残す |
| ME-011 共用試験 CBT | 制度 | AS | 試験の仕組み＝評価が主題 |
| ME-012 プログラム的評価 | 評価 | AS | 評価の設計 |
| ME-013 シミュレーションの有効な特徴（BEME） | 教育手法 | TL | 学習法が主題 |
| ME-014 PBL | 教育手法 | TL | 同上 |
| ME-015 反転授業 | 教育手法 | TL | 授業の進め方が主題（IT とも近いが手法として TL） |
| ME-016 インターネット基盤学習 | 教育手法 | IT | ICT 利用が主題 |
| ME-017 FD の効果（BEME） | 横断 | EM | 教員の育成＝教育運営・質保証の面が主題 |
| ME-018 医学生の抑うつ | 横断 | 横断（残置を提案） | 学習者の健康の問題で、5領域に当てはまらない |
| ME-019 燃え尽きへの介入 | 横断 | 横断（残置を提案） | 同上（医師の健康） |
| ME-020 新専門医制度 | 制度 | 制度（据え置き） | 資格制度そのものが主題。質保証の面は EM の新規候補（EM-2・EM-3）と関連 |
| ME-021 臨床研修マッチング | 制度 | 制度（据え置き） | 制度の仕組みが主題 |
| ME-022 ポートフォリオ | 評価 | AS | 評価手法が主題 |
| ME-023 TBL | 教育手法 | TL | 学習法が主題 |
| ME-024 患者安全教育（WHO） | 横断 | CD（併記として横断も可） | カリキュラムガイドが主題 |
| ME-025 IPE（WHO） | 横断 | TL（併記として横断も可） | 教育の進め方の枠組みが主題 |

提案の要点：完全に5領域＋制度へ寄せるのではなく、ME-010・ME-018・ME-019 のような専門職性・学習者の健康のテーマのために「横断」を例外的に残す形を勧める。全てを付け替えると、この3件の置き場が不自然になるため。

## 5. 出典の見通しの集計

- 既存マスターの再利用で済む候補：IT-7 の指針部分（新規の仮 SRC-5340・5341 の再利用）、AS-9（SRC-5316 の併用で作れる可能性）。ME-007 の裏づけ SRC-5110 など既存出典は関連カード側で既に使用済み。
- 新規出典の仮番号：SRC-5300〜5349 の範囲で 33 件程度（法令3件を含む）。
- 区分の見立ての内訳（主出典ベース）：OPEN 6件（TL-5、AS-5、IT-4、IT-5、IT-6、IT-8、IT-9 のうち主出典として数えると 7 件）、GOV_JP 5件（IT-1、EM-4、EM-5、EM-6、EM-7）、GOV_US 1件（IT-10）、RESTRICTED が残り全て（古典的原典・AMEE Guide・教科書・WHO・UNESCO を含む）。
- RESTRICTED の原典を使う候補では、CC BY の総説で同じ内容を裏づけられるかを各行に併記した。裏づけが見つかれば、原典は corroboration に回して OPEN/GOV の出典を主出典にする運用が可能。
