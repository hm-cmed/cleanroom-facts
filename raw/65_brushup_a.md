# 第65回 成果物（ブラッシュアップA：神経・運動器（Ⅸ）と生活環境・職業性（ⅩⅢ））

- 依頼文：docs/tasks/round62_BRUSHUP_A.md の「第65回」（仕様 specs/round65.yaml）
- 対象：24項目（すべてレベル a）
- 件数：25件（SM-010、OC-024〜026、EV-025〜031、ST-051、ND-062〜064、TJ-077〜080、EP-045、BT-020〜021、NI-030、PN-025、SP-030）。転移性脳腫瘍は疫学と診断で出典が分かれるため2件で担う
- 新規出典：17件（SRC-4801〜4817）。未使用：SRC-4818〜4880
- 既存カードは直さず、各項目に依頼文の表の「2件目に書く側面」の新しいカードを足した

## 判断・申し送り（要点）

- **EP-046（欠神発作の治療）は本編に入れなかった**：治療成績の内容が既存の EP-007・EP-008（医学各論 Ⅸ-6-A-②）と実質的に重なるため。分野をまたぐ項目の扱い（1枚に両方の番号を付ける）に照らすと、本来の形は EP-007・EP-008 へ Ⅸ-11-C-② の番号を追加することであり、既存カードの編集は作り手の範囲外のため、起案したカードは別ファイル（65_appendix_ep046.md）に分離して判断材料とした。本編では EP-045 が臨床像・脳波・予後を担う
- ND の開始番号は仕様で null のため、第63回で ND-061 まで使用・納品済みの続きとして ND-062 からとした
- NI-030（髄膜炎）は、既存カードの出典である細菌性髄膜炎診療ガイドライン2014（国内）の本文が入手できなかったため、本文確認が可能な ESCMID ガイドライン2016（SRC-4815）を採用した。国内ガイドラインとの差異は未照合
- OC-024（頸肩腕障害）は、上肢作業の予防・作業管理の具体基準を示す厚労省の専用指針が確認できなかったため、認定基準の定義の範囲に限定した
- SM-010 は Cochrane 系統的レビューの2026年版（SRC-4801）を採用した。2026年版の PMID 等は未確認のため null・UNKNOWN とし、数値は平易要約で確認できた範囲に限定した

## 1. 出典ホワイトリスト（この回のカードが使う出典）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-1365 | Bendtsen L, Zakrzewska JM, Abbott J, et al. European Academy of Neurology guideline on trigeminal neuralgia. Eur J Neurol. 2019;26(6):831-849 | 10.1111/ene.13950 | 30860637 | © European Academy of Neurology（CC表示なし） | RESTRICTED | 既存出典（出典マスター登録済み。第65回で再利用） |
| SRC-1698 | Rose JJ, Wang L, Xu Q, et al. Carbon Monoxide Poisoning: Pathogenesis, Management, and Future Directions of Therapy. Am J Respir Crit Care Med. 2017 | 10.1164/rccm.201606-1275CI | 27753502 | American Journal of Respiratory and Critical Care Medicine（CC 表示なし） | UNKNOWN | 既存出典（出典マスター登録済み。第65回で再利用） |
| SRC-1967 | Sever MS, Vanholder R; RDRTF of ISN Work Group on Recommendations for the Management of Crush Victims in Mass Disasters. Recommendation for the management of crush victims in mass disasters. Nephrol Dial Transplant. 2012;27 Suppl 1:i1-i67 | 10.1093/ndt/gfs156 | 22467763 | Nephrology Dialysis Transplantation（CC表示なし） | RESTRICTED | 既存出典（出典マスター登録済み。第65回で再利用） |
| SRC-4041 | 労働省労働基準局長通知「上肢作業に基づく疾病の業務上外の認定基準について」（平成9年2月3日、基発第65号） | なし | なし | 政府標準利用規約 | GOV_JP | 既存出典（出典マスター登録済み。第65回で再利用） |
| SRC-4044 | 厚生労働省・都道府県労働局・労働基準監督署. 脳・心臓疾患の労災認定 ― 過労死等の労災補償（パンフレット、令和4年10月版） | なし | なし | 政府標準利用規約 | GOV_JP | 既存出典（出典マスター登録済み。第65回で再利用） |
| SRC-4119 | Paal P, Pasquier M, Darocha T, Lechner R, Kosinski S, Wallner B, Zafren K, Brugger H. Accidental Hypothermia: 2021 Update. International Journal of Environmental Research and Public Health. 2022;19(1):501 | 10.3390/ijerph19010501 | 35010760 | CC BY 4.0（Europe PMC の表示で確認） | OPEN | 既存出典（出典マスター登録済み。第65回で再利用） |
| SRC-4121 | 厚生労働省. 騒音障害防止のためのガイドライン（令和5年4月20日改訂、基発0420第2号）. 厚生労働省. 2023 | なし | なし | 政府標準利用規約 | GOV_JP | 既存出典（出典マスター登録済み。第65回で再利用） |
| SRC-4137 | 警察庁. 令和7年中の交通事故発生状況について／内閣府. 交通安全白書（令和8年版） | なし | なし | 政府標準利用規約 | GOV_JP | 既存出典（出典マスター登録済み。第65回で再利用） |
| SRC-4801 | Freijah I, Jones KA, Coleman T, Perlen SM, Kennedy M, Passey ME, McKenzie JE, Chamberlain C. Psychosocial interventions for supporting women to stop smoking in pregnancy. Cochrane Database of Systematic Reviews. 2026;(4):CD001055 | 10.1002/14651858.CD001055.pub6 | 未確認 | 未確認（刊行元のページで CC 表示を確認できず） | UNKNOWN | Cochrane 公式ページで現行版（2026年版、pub6）の書誌・平易要約・著者結論を確認。出典マスターに DOI の一致なし（新規） |
| SRC-4802 | 厚生労働省. 労働者の心の健康の保持増進のための指針（平成18年3月31日健康保持増進のための指針公示第3号、平成27年11月30日改正・健康保持増進のための指針公示第6号） | なし | なし | 政府標準利用規約 | GOV_JP | 厚生労働省の資料 PDF で指針の全文を確認。出典マスターに一致なし（新規） |
| SRC-4803 | International Federation of Red Cross and Red Crescent Societies. International First Aid, Resuscitation and Education Guidelines 2020. Geneva: IFRC, 2020 | なし | なし | CC 表示なし（© IFRC 2020） | RESTRICTED | 公式リソース（Global First Aid Reference Centre）の本文で窒息の章（171〜172頁、応急処置の手順と注意点）を確認 |
| SRC-4804 | Centers for Disease Control and Prevention. Clinical Guidance for Wound Management to Prevent Tetanus | なし | なし | 米国政府著作物（CDC） | GOV_US | CDC 公式ページの本文（創の分類、創処置、接種・TIG の適応と用量）を確認 |
| SRC-4805 | 消費者庁. 視聴覚資料「家庭用品等による中毒事故を防ぐために」指導者用解説書（平成21・22年度消費者庁委託業務に基づき作成。日本中毒情報センターの集積データによる） | なし | なし | 政府標準利用規約 | GOV_JP | 消費者庁公式サイトの PDF 本文（小児・高齢者の発生状況、図1-1・図1-2、表1）を確認 |
| SRC-4806 | 内閣府. 防災白書（令和8年版）／内閣府政策統括官（防災担当）付参事官（被災者行政担当）付. 災害関連死について | なし | なし | 政府標準利用規約 | GOV_JP | 防災白書（令和8年版）HTML 第3部の保健医療福祉体制の施策記載と、「災害関連死について」PDF 本文（定義・認定の仕組み・熊本地震の内訳）を確認。SRC-4137 と同様の公的資料併記方式 |
| SRC-4807 | Parry SM, Puthucheary ZA. The impact of extended bed rest on the musculoskeletal system in the critical care environment. Extrem Physiol Med. 2015;4:16 | 10.1186/s13728-015-0036-7 | 26457181 | CC BY 4.0（PMC ページのライセンス表示で確認） | OPEN | PubMed レコードで書誌・抄録を確認。PMC ページで CC BY 4.0 の表示を確認。出典マスターに DOI・PMID とも登録なし（新規） |
| SRC-4808 | O'Brien JT, Thomas A. Vascular dementia. Lancet. 2015;386(10004):1698-1706 | 10.1016/S0140-6736(15)00463-8 | 26595643 | Lancet（Elsevier、CC表示なし） | RESTRICTED | PubMed レコードで書誌と DOI の対応を確認し、本文で病型表（Table 1）と管理の節を確認。出典マスターに DOI・PMID とも登録なし（新規） |
| SRC-4809 | Mostafa AHAM, Kyriacou H, Chimutengwende-Gordon M, Khan WS. An overview of the key principles and guidelines in the management of pelvic fractures. J Perioper Pract. 2021;31(9):341-348 | 10.1177/1750458920947358 | 32894996 | CC BY 4.0（PMC ページのライセンス表示で確認） | OPEN | PMC 全文で分類・安定性・合併損傷の記載と CC BY 4.0 の表示を確認。出典マスターに DOI・PMID とも登録なし（新規） |
| SRC-4810 | Wright CJ, Brandon BA, Reisman EJ. Closed-Reduction Techniques for Glenohumeral-, Patellofemoral-, and Interphalangeal-Joint Dislocations. J Athl Train. 2020;55(8):757-767 | 10.4085/1062-6050-0311.19 | 32688375 | Journal of Athletic Training（National Athletic Trainers' Association、CC表示なし） | RESTRICTED | PMC 全文で整復の一般手順（Table 1）、単独脱臼と骨折脱臼の所見の対比（Table 2）、合併症の記載を確認。出典マスターに DOI・PMID とも登録なし（新規） |
| SRC-4811 | Sharma P, Maffulli N. Tendon injury and tendinopathy: healing and repair. J Bone Joint Surg Am. 2005;87(1):187-202 | 10.2106/JBJS.D.01850 | 15634833 | The Journal of Bone and Joint Surgery American Volume（CC表示なし） | RESTRICTED | PubMed レコードで書誌・抄録を確認し、本文で腱の治癒過程と修復の記載を確認。出典マスターに DOI・PMID とも登録なし（新規） |
| SRC-4812 | Hirsch E, French J, Scheffer IE, et al. ILAE definition of the Idiopathic Generalized Epilepsy Syndromes: Position statement by the ILAE Task Force on Nosology and Definitions. Epilepsia. 2022;63(6):1475-1499 | 10.1111/epi.17236 | 35503716 | CC BY 4.0（Epilepsia、Europe PMC の license 欄で確認） | OPEN | Europe PMC のレコードで書誌・PMID・ライセンスを確認。小児欠神てんかんの必須診断基準（定型欠神発作、発作開始時の 3 Hz（2.5〜4 Hz）全般性棘徐波）と臨床像は、同基準の転載ページで確認 |
| SRC-4813 | Achrol AS, Rennert RC, Anders C, et al. Brain metastases. Nat Rev Dis Primers. 2019;5(1):5 | 10.1038/s41572-018-0055-y | 30655533 | Nature Reviews Disease Primers（Springer Nature、CC 表示なし） | RESTRICTED | PubMed 抄録で脳転移の頻度（癌患者の約20%）と原発巣の構成を確認 |
| SRC-4814 | Tong E, McCullagh KL, Iv M. Advanced Imaging of Brain Metastases: From Augmenting Visualization and Improving Diagnosis to Evaluating Treatment Response. Front Neurol. 2020;11:270 | 10.3389/fneur.2020.00270 | 32351445 | CC BY 4.0（Frontiers in Neurology、PMC のライセンス表示で確認） | OPEN | PMC 全文で、造影 MRI が脳転移の診断で優先される画像検査であること等を確認 |
| SRC-4815 | van de Beek D, Cabellos C, Dzupova O, et al. ESCMID guideline: diagnosis and treatment of acute bacterial meningitis. Clin Microbiol Infect. 2016;22 Suppl 3:S37-S62 | 10.1016/j.cmi.2016.01.007 | 27062097 | © European Society of Clinical Microbiology and Infectious Diseases（Elsevier、CC 表示なし） | RESTRICTED | 出版者版 PDF の全文で、成人の臨床像（古典的三徴の頻度を含む）と腰椎穿刺前画像の適応基準（Grade A 推奨）を確認 |
| SRC-4816 | Nolan JP, Sandroni C, Böttiger BW, et al. European Resuscitation Council and European Society of Intensive Care Medicine Guidelines 2021: Post-resuscitation care. Resuscitation. 2021;161:220-269 | 10.1016/j.resuscitation.2021.02.012 | 33773827 | © European Resuscitation Council / European Society of Intensive Care Medicine（Elsevier、CC 表示なし） | RESTRICTED | 出版者版 PDF の全文で心停止後症候群の構成と神経学的予後評価（多角的評価と不良指標の組み合わせ）を確認。体温管理の推奨文は NICE の資料に引用された同ガイドラインの推奨文で確認 |
| SRC-4817 | Middleton K, Fish DE. Lumbar spondylosis: clinical presentation and treatment approaches. Curr Rev Musculoskelet Med. 2009;2(2):94-104 | 10.1007/s12178-009-9051-x | 19468872 | CC BY-NC（Springer、PMC のライセンス表示で確認） | RESTRICTED | PMC 全文で定義・変性カスケード・臨床像・保存療法中心の治療原則とライセンス表示を確認 |

## 2. 事実カード（YAML）

```yaml
- id: SM-010
  domain: SM
  subdomain: 妊婦・胎児への影響
  assertion:
    plain_statement_ja: 妊娠中の禁煙支援として薬物を使わない心理社会的介入（カウンセリング、健康教育、胎児への影響のフィードバック、禁煙へのインセンティブ、社会的支援、運動）があり、Cochrane 系統的レビューの2026年版では127件の研究（喫煙中または最近禁煙した妊婦47,361人）が統合された。カウンセリングと金銭的インセンティブは妊娠後期の禁煙を増やす可能性が高く、健康教育、フィードバック、社会的支援も禁煙を増やす可能性がある一方、運動にはほとんど差がない可能性が高い。心理社会的介入全体では、低出生体重児（2500 g未満）の割合が減り、平均出生体重が増え、新生児集中治療室への入院が減る可能性があるが、死産にはほとんど差がない可能性が高く、早産への影響は明らかでない。これらの知見は、民族的マイノリティや先住民族の女性では研究が少なく当てはまりが確認できていない。
    condition:
      region: 国際
      対象: 妊娠中に喫煙している、または最近禁煙した女性
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4801
    source: Freijah I, Jones KA, Coleman T, Perlen SM, Kennedy M, Passey ME, McKenzie JE, Chamberlain C. Psychosocial interventions for supporting women to stop smoking in pregnancy. Cochrane Database of Systematic Reviews. 2026;(4):CD001055
    doi: 10.1002/14651858.CD001055.pub6
    pmid: null
    pmcid: null
    url: https://doi.org/10.1002/14651858.CD001055.pub6
    source_license: 未確認（刊行元のページで CC 表示を確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードは2026年版（pub6）の平易要約・著者結論と試験数に基づく。刊行元のページでは抄録の Main results が旧版（2017年版）の集計のまま表示されていたため、旧版のリスク比等の数値は含めていない。2026年版の PMID・PMCID は作成時点で確認できず null とした（版は DOI で特定した）。薬剤について：本レビューは薬物を使わない介入のみを対象とし薬物療法の効果は評価していない。国内ではニコチン製剤（ニコチンパッチ・ガム）は妊婦・授乳婦に禁忌とされており、妊娠中の禁煙支援は行動支援が中心となる（禁煙治療のための標準手順書第7版に基づく既存カード SM-009 の記載による）。能動喫煙・受動喫煙の転帰そのものは既存カード SM-009 が担う。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-3-B-③（妊婦・胎児への影響、a）
    core_curriculum: 'GE-04-01-06 (id: JkxpswA)；PS-02-11-05 (id: JkxnuSU)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OC-024
  domain: OC
  subdomain: 頸肩腕障害
  assertion:
    plain_statement_ja: 上肢作業に基づく疾病の認定基準は、上肢等に負担のかかる作業として、①上肢の反復動作の多い作業、②上肢を上げた状態で行う作業、③頸部・肩の動きが少なく姿勢が拘束される作業、④上肢等の特定の部位に負担のかかる状態で行う作業、の4類型を挙げる。過重な業務とは、同一事業場における同種の労働者と比較しておおむね10％以上業務量が増加し、その状態が発症直前3か月程度にわたる場合や、1日の業務量が通常のおおむね20％以上増加した日が1か月のうち10日程度ある場合、1日の労働時間の3分の1程度にわたって通常のおおむね20％以上の業務量増加が1か月のうち10日程度ある場合などをいう。負担のかかる業務への従事期間（相当期間）は、原則として6か月程度以上とされる。
    condition:
      region: 日本
      対象: 上肢作業に従事する労働者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4041
    source: 労働省労働基準局長通知「上肢作業に基づく疾病の業務上外の認定基準について」（平成9年2月3日、基発第65号）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 政府標準利用規約
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 本カードは依頼文の指定する「予防と作業管理」の側面に対し、認定基準が定める負荷作業・過重業務の定義（作業管理の目安となる公的な定義）の範囲に限定した。作業時間・休憩・姿勢・作業環境の具体的な管理基準を示す厚生労働省の専用の予防指針は、本パートの調査では確認できなかった（情報機器作業に限れば既存カード OC-009 のガイドラインが作業管理を担う）。認定の3要件と頸肩腕症候群の定義は既存カード OC-008 が担う。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-4-B-②（頸肩腕障害、a）
    core_curriculum: 'SO-01-04-03 (id: JkxoNtg)；TBL-02-04-014 (id: Jlvnlp8)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OC-025
  domain: OC
  subdomain: 虚血性心疾患
  assertion:
    plain_statement_ja: 脳・心臓疾患の労災認定で「長期間の過重業務」は、発症前おおむね6か月間を評価期間とし、発症時における疲労の蓄積の観点から判断される。労働時間の目安として、発症前1か月間におおむね100時間を超える時間外労働、または発症前2か月間ないし6か月間にわたって1か月当たりおおむね80時間を超える時間外労働が認められる場合は、業務と発症との関連性が強いと評価できる。1か月当たりおおむね45時間を超えない場合は関連性が弱く、45時間を超えて長くなるほど関連性は徐々に強まるとされる。上記の水準に至らなくても、これに近い時間外労働に加えて一定の労働時間以外の負荷要因が認められるときは、総合的に評価して関連性が強いと評価できる。パンフレットの認定事例でも、心筋梗塞を発症したトラック運転手について、時間外労働は関連性が強いと評価できる水準には至らないものの、勤務時間の不規則性などの負荷要因をあわせて関連性が強いと評価され認定されている。「短期間の過重業務」の評価期間は発症前おおむね1週間で、過重な負荷は発症に近いほど影響が強いとして、発症直前から前日までの業務が特に過重かどうか、それが認められなくても発症前おおむね1週間以内に過重な業務が継続していたかどうかがみられる。関連性が強い例として、発症直前から前日までの特に過度の長時間労働や、発症前おおむね1週間継続して深夜時間帯に及ぶ時間外労働などが挙げられる（労働密度が特に低い場合を除く）。
    condition:
      region: 日本
      対象: 労働者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4044
    source: 厚生労働省・都道府県労働局・労働基準監督署. 脳・心臓疾患の労災認定 ― 過労死等の労災補償（パンフレット、令和4年10月版）
    doi: null
    pmid: null
    pmcid: null
    url: http://www.mhlw.go.jp/new-info/kobetu/roudou/gyousei/dl/2207252-1.pdf
    source_license: 政府標準利用規約
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: パンフレット（令和4年10月版）の全文で確認した範囲に限る。時間の数値（45・80・100時間）はパンフレットの図・本文の記載に基づき、80・100時間は厚生労働省の認定基準改正ポイント資料でも確認した。認定事例に示された時間外労働時間数などの個別の数値はパンフレットの図中にあり読み取れなかったため含めていない。認定基準の通達（基発0914第1号）本文の逐語照合は未了（既存カード OC-011 と同様）。対象疾病と枠組み、労働時間以外の負荷要因は既存カード OC-011 が担う。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-4-C-②（虚血性心疾患、a）
    core_curriculum: 'SO-01-04-03 (id: JkxoNtg)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OC-026
  domain: OC
  subdomain: 心身症
  assertion:
    plain_statement_ja: 労働者の心の健康の保持増進のための指針（労働安全衛生法第70条の2第1項に基づく）では、事業者は衛生委員会等において調査審議を行い、「心の健康づくり計画」を策定・実施することとされる。メンタルヘルス不調を未然に防止する一次予防、早期に発見し適切な措置を行う二次予防、職場復帰を支援する三次予防が円滑に行われるよう、4つのケアを継続的かつ計画的に行う。4つのケアとは、労働者自身がストレスに気づき対処する「セルフケア」、管理監督者が職場環境等の改善や労働者に対する相談対応を行う「ラインによるケア」、事業場内の産業医等が心の健康づくり対策の提言と推進を担い労働者と管理監督者を支援する「事業場内産業保健スタッフ等によるケア」、事業場外の機関や専門家を活用する「事業場外資源によるケア」である。職場復帰支援では、職場復帰支援プログラムを策定する（休業の開始から通常業務への復帰までの一連の標準的な流れと、それに対応する手順・内容・関係者の役割を定める）こと、その実施に関する体制や規程を整備し労働者に周知すること、組織的かつ計画的に取り組むこと、事業場内産業保健スタッフ等を中心に労働者と管理監督者が理解と協力を行い主治医との連携を図ることが示される。
    condition:
      region: 日本
      対象: 労働者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4802
    source: 厚生労働省. 労働者の心の健康の保持増進のための指針（平成18年3月31日健康保持増進のための指針公示第3号、平成27年11月30日改正・健康保持増進のための指針公示第6号）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/11201250/001249074.pdf
    source_license: 政府標準利用規約
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 指針の全文（厚生労働省の資料 PDF に収められた公示本文）で確認した範囲に限る。本項目に心身症に固有の認定基準・指針はなく、本カードは職場のメンタルヘルス対策の一般像として本指針を充てた。心身症そのものの診断・治療は扱わない。ストレスチェック制度そのものは既存カード OC-014 が担う。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-4-D-②（心身症、a）
    core_curriculum: 'PS-02-17-05 (id: JkxnuT8)；TBL-01-00-546 (id: JlvnmUc)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: EV-025
  domain: EV
  subdomain: 偶発性低体温{症}
  assertion:
    plain_statement_ja: 偶発性低体温症の古典的な病期分類（欧州蘇生協議会2021）では、HT I（軽症）は深部体温35〜32℃で意識がありシバリングを伴い、HT II（中等症）は32℃未満〜28℃で意識障害がありシバリングはあってもなくてもよく、HT III（重症）は28℃未満で意識はないがバイタルサインがあり、HT IV は古典的には24℃未満でバイタルサインがなく見かけ上の死亡とされる。復温は、軽症（HT I）では寒冷環境からの離脱、保温、温かい飲食、能動的な運動による受動的復温で通常は十分であり、中等症・重症（HT II・III）では能動的復温が必要で全身を保温する。復温速度の目安は、受動的復温と能動的体外復温が毎時0.5〜4℃、体外式生命維持（ECLS）が毎時約4〜10℃である。注意点として、突然の体動などの機械的刺激が心停止の引き金になりうるため患者は穏やかに扱うこと、復温を始めた後も深部体温がさらに下がることがあり（アフタードロップ。主因は冷えた体部位の再灌流とされる）、歩行はアフタードロップを増やすため水平位で発見された患者は食事をとり約30分シバリングするまで歩かせないことが挙げられる。病院内では、循環が安定していれば受動的復温と能動的体外復温を行い、心停止のリスクがある場合や循環が不安定な場合は ECLS を待機させ必要時に速やかに開始し、心停止例では ECLS（ECMO が優先される）が能動的体内復温として用いられる。
    condition:
      region: 国際
      対象: 偶発性低体温症の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4119
    source: 'Paal P, Pasquier M, Darocha T, Lechner R, Kosinski S, Wallner B, Zafren K, Brugger H. Accidental Hypothermia: 2021 Update. International Journal of Environmental Research and Public Health. 2022;19(1):501'
    doi: 10.3390/ijerph19010501
    pmid: '35010760'
    pmcid: PMC8744717
    url: https://doi.org/10.3390/ijerph19010501
    source_license: CC BY 4.0（Europe PMC の表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 病期分類と復温速度は出典の表から読み取り（病期分類の表は欧州蘇生協議会2021の転載）。出典の全文で確認した範囲に限る。定義と ECLS ができる施設への搬送基準は既存カード EV-004 が担うため本カードでは繰り返さない。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-5-A-②（偶発性低体温{症}、a）
    core_curriculum: 'PS-03-05-10 (id: Jkxnub4)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: EV-026
  domain: EV
  subdomain: 騒音性難聴
  assertion:
    plain_statement_ja: 騒音障害防止のためのガイドライン（2023年改訂）では、作業環境測定（A測定・B測定）の結果を A測定平均値と B測定の組み合わせで第Ⅰ〜第Ⅲ管理区分に区分する。A測定平均値が85 dB未満では B測定85 dB未満が第Ⅰ管理区分、85 dB以上90 dB未満が第Ⅱ管理区分、90 dB以上が第Ⅲ管理区分となり、A測定平均値が85 dB以上90 dB未満では第Ⅱまたは第Ⅲ管理区分、90 dB以上ではすべて第Ⅲ管理区分となる。措置は、第Ⅰ管理区分では作業環境の継続的維持に努め、第Ⅱ管理区分では標識で明示し、施設・設備・作業工程・作業方法を点検して改善措置を講じ第Ⅰ管理区分となるよう努め、必要に応じて聴覚保護具を使用させ、第Ⅲ管理区分では標識で明示し、点検と改善措置（第Ⅰまたは第Ⅱ管理区分となるよう努め、改善後は再測定で効果を確認する）を講じ、聴覚保護具を使用させて管理者に使用状況を確認させ掲示する。定点測定や個人ばく露測定では等価騒音レベルで評価し、85 dB未満は作業環境の継続的維持に努め、85 dB以上90 dB未満は点検・改善して85 dB未満となるよう努め必要に応じて聴覚保護具を使用させ、90 dB以上は点検・改善（85 dB未満を目標とし再測定で効果を確認する）と聴覚保護具の使用・確認・掲示を行う。作業時間の管理として、改善措置を講じても第Ⅰ管理区分とならない、または等価騒音レベルが85 dB未満とならない場合は、日本産業衛生学会の騒音の許容基準の表を参考に、騒音作業に従事する時間の短縮を検討する（85 dBで1日8時間、90 dBで2時間30分、95 dBで47分、100 dBで15分）。健康診断の事後措置として、前駆期の症状が認められる者や軽度の聴力低下が認められる者には、第Ⅱ管理区分の場所または等価騒音レベル85 dB以上90 dB未満の場所においても聴覚保護具を使用させるほか必要な措置を講じ、中等度以上の聴力低下が認められる者には、聴覚保護具を使用させるほか、騒音作業に従事する時間の短縮、配置転換その他必要な措置を講じる。
    condition:
      region: 日本
      対象: 騒音作業に従事する労働者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4121
    source: 厚生労働省. 騒音障害防止のためのガイドライン（令和5年4月20日改訂、基発0420第2号）. 厚生労働省. 2023
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/001089239.pdf
    source_license: 政府標準利用規約
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 管理区分の対応と許容基準の時間（85 dBで1日8時間など）はガイドライン本文の表から読み取り。ガイドライン本文・別紙で逐語確認した範囲に限る（既存カード EV-006 は解説資料ベースだった）。健康診断の項目と頻度の枠組みは既存カード EV-006 が担うため、本カードは管理区分・措置と事後措置を中心に記載した。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-5-B-①（騒音性難聴、a）
    core_curriculum: 'PS-03-05-11 (id: Jkxnub8)；TBL-02-15-010 (id: JlAKpwY)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: EV-027
  domain: EV
  subdomain: 誤嚥
  assertion:
    plain_statement_ja: 気道異物による窒息への応急処置は重症度で分ける。軽症（咳ができる）では咳を促し、改善するまで観察する。重症（咳・発声・呼吸ができない）では、成人・小児には肩甲骨の間への背部叩打を最大5回行い、除去できなければ腹部突き上げ（肋骨と臍の間に拳を当て、もう一方の手で内側かつ上方へ鋭く引く）を最大5回行う。それでも除去できなければ直ちに救急要請し、除去できるか意識を失うまで背部叩打と腹部突き上げを交互に繰り返す。乳児には腹部突き上げは行わず、背部叩打を最大5回、次いで胸部突き上げ（胸の中央を鋭く下方へ押す）を最大5回行い、交互に繰り返す。意識を失った場合は通常の心肺蘇生を開始する。口内の固形物は見えている場合にのみ指で除去し、見えないまま指で探ることはしない。重症例では腹部突き上げによる内臓損傷や異物の残存がありうるため、救急要請して医療機関の評価につなげる。
    condition:
      region: 国際
      対象: 気道異物による窒息の傷病者（成人・小児・乳児）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4803
    source: 'International Federation of Red Cross and Red Crescent Societies. International First Aid, Resuscitation and Education Guidelines 2020. Geneva: IFRC, 2020'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.globalfirstaidcentre.org/fr/resource/internationalfirstaidresuscitationandeducationguidelines-2020-2/
    source_license: CC 表示なし（© IFRC 2020）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は赤十字赤新月社連盟（IFRC）の国際的な応急処置ガイドライン2020年版で、窒息の章の本文で手順を確認した。既存 EV-016 の出典（ILCOR 応急処置コンセンサス2020、SRC-4131）の抄録に窒息時の手技の手順は含まれず確認できなかったため、新規出典とした。日本の JRC 蘇生ガイドライン2020でも背部叩打と腹部突き上げを組み合わせる手順が示されているが、その逐語確認は本カードの出典では行っていない。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-5-G-②（誤嚥、a）
    core_curriculum: 'PS-03-05-04 (id: Jkxnubg)；TBL-01-00-212 (id: Jlvnlx0)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: EV-028
  domain: EV
  subdomain: 創傷
  assertion:
    plain_statement_ja: 創傷後の破傷風予防は、創の性状と接種歴で判断する。すべての創を洗浄し、汚物・異物を除去し、壊死組織をデブリードマンする。破傷風の予防を目的とした抗菌薬投与は推奨されない。創は、清潔で軽微な創と、それ以外の汚染・重度創（刺創・貫通創、土壌・糞便・唾液で汚染された創、壊死組織を含む熱傷・複合骨折・挫滅創・凍傷など）に分ける。基礎免疫（初回接種シリーズ）が完了し、最終接種から5年未満であれば、創の種類を問わず追加接種は不要である。接種歴不明・未接種・基礎免疫未完了の場合は、すべての創でトキソイドの接種が推奨される。基礎免疫が完了している場合は、清潔で軽微な創では最終接種から10年以上、それ以外の創では5年以上経過していれば追加接種を行う。抗破傷風免疫グロブリン（TIG）は清潔で軽微な創には用いず、それ以外の創で接種歴不明・未接種・基礎免疫未完了の場合、および HIV 感染・重度免疫不全のある場合に適応となり、用量は250単位を筋肉内投与する。
    condition:
      region: 米国
      対象: 創傷のある患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4804
    source: Centers for Disease Control and Prevention. Clinical Guidance for Wound Management to Prevent Tetanus
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/tetanus/hcp/clinical-guidance/index.html
    source_license: 米国政府著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 判断基準は米国 CDC の臨床指針に基づく。本カードで扱う沈降破傷風トキソイドと抗破傷風人免疫グロブリン製剤（テタノブリン等）は国内でも承認・販売されているが、国内の定期接種歴に応じた実施判断は国内の指針・添付文書での確認が別途必要である。日本の破傷風の疫学・臨床像は既存の感染症側のカード（SRC-2122・SRC-2123 の出典群）が接点となる。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-5-G-③（創傷、a）
    core_curriculum: 'PS-03-05-12 (id: Jkxir3g)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: EV-029
  domain: EV
  subdomain: 急性中毒
  assertion:
    plain_statement_ja: 日本中毒情報センターへの問い合わせの集計では、5歳以下の小児の急性中毒事故は1999年から2008年の10年間に268,784件（年2万5千件以上、1日平均70件以上）寄せられ、人口当たりの件数では成人（20〜64歳）の70倍以上であった。原因物質は家庭用品等が75.8%を占め、医療用医薬品12.6%、一般用医薬品10.1%、自然毒1.2%、農薬0.3%と続いた。曝露経路は誤飲・誤食が95.7%と大半を占め、皮膚についた・触った2.2%、吸い込んだ1.2%、目に入った0.9%であった。問い合わせの多い家庭用品は、たばこ（31,939件）が最多で、乾燥剤・鮮度保持剤、芳香剤・消臭剤・脱臭剤、石けん、ピレスロイド含有殺虫剤、保冷剤が続いた。医療機関での診療が必要な事例や実際に受診した事例は2割以上を占めた。
    condition:
      region: 日本
      対象: 5歳以下の小児の急性中毒事故
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4805
    source: 消費者庁. 視聴覚資料「家庭用品等による中毒事故を防ぐために」指導者用解説書（平成21・22年度消費者庁委託業務に基づき作成。日本中毒情報センターの集積データによる）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.caa.go.jp/policies/policy/consumer_safety/other/information_005/pdf/120511kouhyou_2.pdf
    source_license: 政府標準利用規約
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 数値は日本中毒情報センターへの電話問い合わせの集計であり、実際の発生件数そのものではない。原因物質・曝露経路の割合は同資料の図1-1・図1-2から、品目別の件数は表1から読み取った。対象期間は1999〜2008年と古く、加熱式たばこ等の新しい製品の動向は含まれない。同資料には65歳以上の高齢者についても1996〜2009年に19,128件の問い合わせがあり原因の約7割が家庭用品等であったことが示されているが、本カードの内訳数値は5歳以下に限った。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-5-G-⑤（急性中毒、a）
    core_curriculum: 'PS-03-05-06 (id: Jkxnubo)；PS-03-05-07 (id: Jkxnubs)；PS-03-05-08 (id: Jkxnubw)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: EV-030
  domain: EV
  subdomain: 交通事故
  assertion:
    plain_statement_ja: 令和7年の交通事故死者（2,547人）を状態別にみると、歩行中が867人で最も多く、うち65歳以上が608人（70.1%）を占めた。自転車乗用中は301人で、うち65歳以上が197人であった。歩行中死者の約6割には法令違反があり、高齢の歩行中死者では横断中が442人（72.7%）と大半を占め、そのうち横断歩道以外の横断が283人であった。飲酒運転（第1当事者が一般原付以上の事故）による死亡事故は125件で、飲酒運転の場合の死亡事故率は飲酒なしの場合の約7.1倍であった。
    condition:
      region: 日本
      対象: 交通事故の発生状況（状態別・要因別の内訳）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4137
    source: 警察庁. 令和7年中の交通事故発生状況について／内閣府. 交通安全白書（令和8年版）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 政府標準利用規約
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 状態別・飲酒運転の数値は警察庁「令和7年における交通事故の発生状況について」の図表から読み取った（歩行中・自転車乗用中の年齢内訳を含む）。発生件数・死者数・負傷者数の総数は EV-022 が担う。自動車乗車中・二輪車乗車中の死者数は、同資料の図からの読み取りが確実でなかったため本カードには含めていない。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-5-I-①（交通事故、a）
    core_curriculum: 'SO-01-05-01 (id: JkxoNtw)；PS-03-05-12 (id: Jkxir3g)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: EV-031
  domain: EV
  subdomain: 自然災害
  assertion:
    plain_statement_ja: 災害関連死とは、当該災害による負傷の悪化又は避難生活等における身体的負担による疾病により死亡し、災害弔慰金の支給等に関する法律に基づき災害が原因で死亡したものと認められたものをいい、認定は市町村が行う。平成28年熊本地震では、死者270人のうち215人がこの災害関連死として認められたもので、警察が検視により確認した死者50人を大きく上回った（平成31年3月時点）。認定事例には、避難中の車内での疲労による心疾患、避難所生活に伴う肺炎、エコノミークラス症候群の疑い、栄養障害や持病の悪化などが含まれる。災害関連死を減らすため、避難所の生活環境の改善（簡易ベッド・簡易台所などの設備の整備）が市町村の取組として進められ、国は被災者の命に関わる生活必需品等のプッシュ型支援を行う。災害時の保健医療福祉の体制としては、災害派遣医療チーム（DMAT）、災害派遣精神医療チーム（DPAT）、災害支援ナース、災害派遣福祉チーム（DWAT）などの派遣チームの体制整備や、都道府県の保健医療福祉調整本部への支援、災害時保健医療福祉活動支援システム（D24H）による情報の統合が進められている。
    condition:
      region: 日本
      対象: 災害時の健康被害と保健医療福祉体制
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4806
    source: 内閣府. 防災白書（令和8年版）／内閣府政策統括官（防災担当）付参事官（被災者行政担当）付. 災害関連死について
    doi: null
    pmid: null
    pmcid: null
    url: https://www.bousai.go.jp/taisaku/kyuujo/pdf/r01kaigi/siryo8.pdf
    source_license: 政府標準利用規約
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 本カードは公的資料2件の併記を出典とする（SRC-4137 と同様の方式）。災害関連死の定義・認定の仕組み・熊本地震の内訳は「災害関連死について」で、保健医療福祉の体制は防災白書（令和8年版）第3部の施策記載で確認した。熊本地震の数値は平成31年3月13日発表の熊本県の被害状況（第288報）に基づく当時の値であり、その後の認定の進展で関連死の認定数はさらに増えている。能登半島地震の災害関連死の最新認定数や東日本大震災の震災関連死の総数は本カードの出典では確認していないため含めていない。避難所の健康管理の具体策は内閣府「避難所における良好な生活環境の確保に向けた取組指針」が別に示す。
  curriculum:
    kokushi: 医学各論 ⅩⅢ-5-I-③（自然災害、a）
    core_curriculum: 'SO-01-05-01 (id: JkxoNtw)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ST-051
  domain: ST
  subdomain: 廃用性萎縮
  assertion:
    plain_statement_ja: 廃用症候群（廃用性萎縮を含む）は、長期の不動・臥床によって筋や骨をはじめ多臓器に生じる有害な変化の総体である。不動による筋量と骨密度の低下は速く、臥床開始後1週間以内に明らかになり、重症病態ではさらに増悪する。筋萎縮の病態には筋タンパクの合成と分解のバランスの崩れが関わり、細胞内シグナル伝達の変化の面から検討されている。予防の基本は不動の期間をできるだけ短くすることであり、早期からの活動・離床とリハビリテーションを進めることが対策の中心となる。
    condition:
      region: 国際
      対象: 長期臥床・不動の患者（重症患者を含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4807
    source: Parry SM, Puthucheary ZA. The impact of extended bed rest on the musculoskeletal system in the critical care environment. Extrem Physiol Med. 2015;4:16
    doi: 10.1186/s13728-015-0036-7
    pmid: '26457181'
    pmcid: PMC4600281
    url: https://doi.org/10.1186/s13728-015-0036-7
    source_license: CC BY 4.0（PMC ページのライセンス表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 重症患者（集中治療環境）を中心とした総説に基づいており、一般病棟や在宅での臥床への当てはめは程度の問題として判断される。主張は抄録で確認できる範囲に限った。拘縮をはじめとする個々の症候の頻度や回復の時間経過の数値はこの総説では確認できず、主張に含めていない。脳卒中急性期の超早期離床の負荷については ST-050（AVERT 試験）が担う。（出典内の位置：抄録）
  curriculum:
    kokushi: 医学各論 Ⅸ-1-E-②（廃用性萎縮、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ND-062
  domain: ND
  subdomain: 脳血管性認知症
  assertion:
    plain_statement_ja: 脳血管性認知症はアルツハイマー病に次いで多い認知症で、認知症全体の約15%を占める。病型は病変の部位と成り立ちで分けられ、皮質の多発梗塞による多発梗塞性、小血管病による皮質下血管性（ラクナと広範な白質病変）、視床など戦略的部位の単一梗塞によるもの、分水嶺梗塞などの低灌流性、出血性、CADASIL などの遺伝性、アルツハイマー病に脳血管疾患が合併する混合型などがある。病理学的には大きな皮質梗塞よりも皮質下の血管病変が多数を占め、皮質下病変では前頭葉と線条体の回路の障害により注意・情報処理・遂行機能の障害が目立ち、記憶障害が前景に出ないことがある。診断では画像で脳血管病変（梗塞や白質病変）を示すことが支えとなる。血管性認知症に認可された治療薬はなく、管理の中心は併存症の把握と対応、血管危険因子の最適な管理、非認知症状への対応、患者と介護者への心理社会的支援であり、脳卒中再発予防を含む血管危険因子の管理が中核となる。
    condition:
      region: 国際
      対象: 脳血管性認知症の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4808
    source: O'Brien JT, Thomas A. Vascular dementia. Lancet. 2015;386(10004):1698-1706
    doi: 10.1016/S0140-6736(15)00463-8
    pmid: '26595643'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(15)00463-8
    source_license: Lancet（Elsevier、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: コリンエステラーゼ阻害薬（ドネペジル、リバスチグミン、ガランタミン）とメマンチンは小さい効果が示されたにとどまり、規制当局やガイドラインは血管性認知症への適応を認めていない。これらの薬剤は国内ではアルツハイマー型認知症（ドネペジルはレビー小体型認知症も）に承認・保険適用があるが、血管性認知症への適応はない。国内の認知症疾患診療ガイドラインは2026年版が現行だが、その本文は照合できなかったため、本カードは国際的な総説に基づく。脳小血管病の MRI マーカーそのものは ND-010 が担い、本カードでは扱わない。（出典内の位置：本文の病型表（Table 1）、認知機能の節、管理の節）
  curriculum:
    kokushi: 医学各論 Ⅸ-1-E-③（脳血管性認知症、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-039 (id: JlvnldY)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ND-063
  domain: ND
  subdomain: 一酸化炭素中毒
  assertion:
    plain_statement_ja: 一酸化炭素中毒の診断は、中毒に矛盾しない症状、最近の曝露歴、血中カルボキシヘモグロビン（COHb）の上昇の3点に基づく。症状は頭痛、めまい、倦怠感、悪心・嘔吐、意識障害などが多く、通常のパルスオキシメータでは COHb と酸素化ヘモグロビンを区別できない。COHb の異常高値の目安は非喫煙者で2%以上、喫煙者で10%以上とされる。治療は100%酸素投与が基本であり、CO の消失半減期は室内気での約320分から常圧100%酸素で約74分に、高気圧酸素（2.5〜3気圧）では約20分に短縮する。回復後、数日から数週間を経て遅発性の神経障害が現れることがある。
    condition:
      region: 国際
      対象: 一酸化炭素中毒の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1698
    source: 'Rose JJ, Wang L, Xu Q, et al. Carbon Monoxide Poisoning: Pathogenesis, Management, and Future Directions of Therapy. Am J Respir Crit Care Med. 2017'
    doi: 10.1164/rccm.201606-1275CI
    pmid: '27753502'
    pmcid: null
    url: https://doi.org/10.1164/rccm.201606-1275CI
    source_license: American Journal of Respiratory and Critical Care Medicine（CC 表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: COHb の目安値と消失半減期の数値は総説（SRC-1698）の本文で確認した。高気圧酸素療法の位置づけについては、無作為化比較試験の系統的レビュー（Buckley NA, et al. Cochrane Database Syst Rev. 2011;(4):CD002041、出典表には未収載）で神経学的転帰の改善は確立しておらず、その適応は定まっていない。SRC-1698 の PMCID は PMC5363978 が候補（マスターでは null のため本カードも null とし、補完は取り込み側の照合に委ねる）。神経認知障害の頻度などの予後は既存カード ND-054 が担い、本カードでは扱わない。
  curriculum:
    kokushi: 医学各論 Ⅸ-4-I-①（一酸化炭素中毒<CO中毒>、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ND-064
  domain: ND
  subdomain: 低酸素脳症
  assertion:
    plain_statement_ja: 心停止後症候群は、心停止後の低酸素虚血性脳障害、心筋機能障害、全身の虚血再灌流応答、持続する心停止の原因病態から構成される。神経学的予後評価は単一の指標では正確に行えないため、鎮静や体温管理などの交絡因子を除いたうえで複数の指標を組み合わせて行う。自己心拍再開後72時間以上の時点で昏睡が続き最良運動反応がモータースコア3以下（異常屈曲以下）の患者では、72時間以上での瞳孔反射と角膜反射の両側消失、24時間以上での体性感覚誘発電位 N20 波の両側消失、24時間以降の高度悪性脳波パターン、48時間および/または72時間での神経特異エノラーゼ60 µg/L超、72時間以内の持続性ミオクローヌス、頭部CT・MRIでの広範な低酸素性脳障害のうち2つ以上がそろえば転帰不良の可能性が高い。体温管理については、同ガイドラインは昏睡患者で32〜36℃の一定の目標体温を少なくとも24時間維持すること、自己心拍再開後少なくとも72時間は37.7℃を超える発熱を避けることを推奨した。
    condition:
      region: 欧州
      対象: 心停止後に自己心拍が再開した昏睡状態の成人患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4816
    source: 'Nolan JP, Sandroni C, Böttiger BW, et al. European Resuscitation Council and European Society of Intensive Care Medicine Guidelines 2021: Post-resuscitation care. Resuscitation. 2021;161:220-269'
    doi: 10.1016/j.resuscitation.2021.02.012
    pmid: '33773827'
    pmcid: null
    url: https://doi.org/10.1016/j.resuscitation.2021.02.012
    source_license: © European Resuscitation Council / European Society of Intensive Care Medicine（Elsevier、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 予後評価の指標と組み合わせの基準はガイドライン本文で確認した。体温管理の推奨文は、ガイドライン本文の推奨ボックスがテキストとして抽出できなかったため、NICE の資料に引用された同ガイドラインの推奨文で確認した。2022年には ILCOR の更新で37.5℃以下を目標とする積極的な発熱予防が提案され、ERC/ESICM も同年に発熱予防を重視する体温管理の改訂声明を出しており、現在の位置づけは発熱予防が中心である。33℃を目標とする管理が発熱予防中心の平温管理より死亡率を下げなかったことは既存カード ND-055（TTM2試験）が担う。
  curriculum:
    kokushi: 医学各論 Ⅸ-4-I-②（低酸素脳症、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-02-02-021 (id: JlAKpYw)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: TJ-077
  domain: TJ
  subdomain: 骨盤骨折
  assertion:
    plain_statement_ja: 骨盤骨折の分類には AO/OTA、Tile、Young-Burgess などがあり、Young-Burgess 分類が広く用いられ ATLS にも取り入れられている。安定性の観点では、Young-Burgess の前後圧迫（APC）I型と側方圧迫（LC）I型が安定型で、それ以外は不安定型とされ、垂直剪断型は転帰が最も不良である。治療は安定性に応じて選択され、不安定型の再建手術が議論の中心で、安定型は手術を要しない管理が前提となり、低エネルギー骨折の患者は通常は介助なしに歩行できる。合併損傷として尿生殖器系の損傷があり、尿道口の血液、血尿、陰嚢血腫などがあれば尿道損傷を疑って逆行性尿道造影や膀胱造影を検討し、直腸診では出血・血腫と前立腺の高位を確かめる。開放骨折で直腸損傷が疑われる場合は人工肛門造設を考慮する。
    condition:
      region: 国際
      対象: 骨盤骨折患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4809
    source: Mostafa AHAM, Kyriacou H, Chimutengwende-Gordon M, Khan WS. An overview of the key principles and guidelines in the management of pelvic fractures. J Perioper Pract. 2021;31(9):341-348
    doi: 10.1177/1750458920947358
    pmid: '32894996'
    pmcid: PMC8406373
    url: https://doi.org/10.1177/1750458920947358
    source_license: CC BY 4.0（PMC ページのライセンス表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本総説は英国のガイダンス（NICE、BOA など）を要約したもので、安定型の治療の記述は「不安定型の再建が手術の中心である」という本文の構成から読み取った範囲である。尿生殖器損傷の頻度の数値は本文が引用するコホート研究の値であり、主張には含めていない。血行動態不安定例の止血は TJ-034（WSES ガイドライン）が担い、寛骨臼骨折は対象外である。（出典内の位置：本文の分類、治療原則、合併損傷の節）
  curriculum:
    kokushi: 医学各論 Ⅸ-10-C-②（骨盤骨折、a）
    core_curriculum: 'TBL-01-00-118 (id: Jlvnlm8)；TBL-01-00-120 (id: Jlvnlnk)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: TJ-078
  domain: TJ
  subdomain: 脱臼、亜脱臼
  assertion:
    plain_statement_ja: 関節脱臼は、激しい疼痛、目視・触知できる関節の転位、可動域と機能の喪失を呈する外傷である。スポーツ外傷では肩関節（肩甲肱骨関節）、膝蓋大腿関節、指節間関節に多く、高校のスポーツでは関節脱臼のうち肩が55%、手と手指が17%、膝が16%を占めた。骨折を伴う場合（骨折脱臼）は骨性の圧痛や変形が加わり、診察所見だけでは単独の脱臼と区別しにくいことがある。閉鎖整復の一般的な手順は、整復前評価（脱臼の確認、骨折など禁忌の評価、神経血管の完全性の評価と記録、画像検査と疼痛管理の検討、利益とリスクを説明した上での同意）、整復、整復後再評価（神経血管の再評価、初回脱臼では全例で整復後の画像検査）、整復後ケア（適切な肢位での固定、記録、フォローアップ）の4段階である。迅速な整復は整復の成功率を高め、疼痛の軽減や関節の完全性、機能予後に有利とされる一方、骨折の徴候、裂創や腱断裂などの随伴損傷、成長板損傷の疑いがある場合は現場での整復を行わず、固定して医療機関へ搬送する。神経血管障害があること自体は閉鎖整復の禁忌ではないが試行は愛護的に限られ、医師向けの推奨では閉鎖整復の試行は最大2回までで、失敗すれば全身麻酔下または外科的整復に移行する。合併症や随伴損傷の一般像として神経血管損傷、随伴骨折、軟部組織損傷があり、肩関節脱臼では神経障害が約12%にみられ腋窩神経が最多である。
    condition:
      region: 国際
      対象: 関節脱臼の患者（アスリートを含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4810
    source: Wright CJ, Brandon BA, Reisman EJ. Closed-Reduction Techniques for Glenohumeral-, Patellofemoral-, and Interphalangeal-Joint Dislocations. J Athl Train. 2020;55(8):757-767
    doi: 10.4085/1062-6050-0311.19
    pmid: '32688375'
    pmcid: PMC7462174
    url: https://doi.org/10.4085/1062-6050-0311.19
    source_license: Journal of Athletic Training（National Athletic Trainers' Association、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本出典はアスレティックトレーナーの業務範囲を念頭に置いた臨床総説であり、好発部位の割合は高校スポーツの疫学に基づく。脱臼と亜脱臼を分ける定義（関節面の接触が完全に失われるか、部分的に残るか）の体系的な記述は本総説にはなく、主張に定義文は含めていない。分類についても方向と随伴骨折の有無による整理の範囲にとどまる。部位別の整復手技そのものは扱わず、代表関節である肩関節脱臼の詳細は TJ-052〜054 が担う。（出典内の位置：抄録、一般的手順の表（Table 1）、単独脱臼と骨折脱臼の対比表（Table 2）、本文の整復の根拠と肩関節の節）
  curriculum:
    kokushi: 医学各論 Ⅸ-10-D-③（脱臼、亜脱臼、a）
    core_curriculum: 'TBL-01-00-121 (id: JlvnlnE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: TJ-079
  domain: TJ
  subdomain: 筋断裂、腱断裂
  assertion:
    plain_statement_ja: 急性の腱断裂の背景には既存の腱の変性があることが多く、変性は急性断裂の危険因子とされる。フルオロキノロン系抗菌薬の使用も腱断裂との関連が指摘されている。腱内部の病変は MRI や超音波検査で検出できる。断裂した腱の治癒は、炎症期、増殖期（III型コラーゲンが主体となる）、再構築期（およそ6週から始まり、成熟にはおよそ1年を要する）が重なり合う3相で進む。治癒には、腱周囲組織から細胞が入り込む外因性治癒と、腱実質（腱上膜）の細胞による内因性治癒があり、断裂腱の治癒は腱上膜の細胞だけでも達成しうる。外因性治癒では癒着が形成されて腱の滑走が妨げられるため、修復では内因性治癒を活かし癒着を抑えることが目標となり、治癒した腱が正常な腱の性質を取り戻すことはない。
    condition:
      region: 国際
      対象: 腱断裂の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4811
    source: 'Sharma P, Maffulli N. Tendon injury and tendinopathy: healing and repair. J Bone Joint Surg Am. 2005;87(1):187-202'
    doi: 10.2106/JBJS.D.01850
    pmid: '15634833'
    pmcid: null
    url: https://doi.org/10.2106/JBJS.D.01850
    source_license: The Journal of Bone and Joint Surgery American Volume（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: フルオロキノロン系抗菌薬（レボフロキサシン、シプロフロキサシンなど）は国内で承認され保険適用のある抗菌薬であり、本カードはその使用と腱断裂との関連を述べるものである。本総説の主題は腱の治癒と修復の生物学であり、断裂部の陥凹の触知や部位別の機能テストといった身体診察の具体、一次縫合の手技や時期の詳細は扱われていないため、主張には含めていない。部位別の詳細（アキレス腱断裂は TJ-067・068）が担う範囲は対象外である。（出典内の位置：抄録、本文の治癒と修復の節）
  curriculum:
    kokushi: 医学各論 Ⅸ-10-E-③（筋断裂、腱断裂、a）
    core_curriculum: 'TBL-01-00-123 (id: Jlvnlno)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: TJ-080
  domain: TJ
  subdomain: 挫滅症候群
  assertion:
    plain_statement_ja: 挫滅症候群への具体的な対応は、災害時の国際推奨（ISN）で次のように示される。輸液は救出中から等張食塩液を成人で 1000 mL/h で開始し、救出に2時間を超える場合は 500 mL/h 以下に減らす。救出後はできるだけ速やかに開始し、救出前に投与がなければ成人 1000 mL/h（小児 15〜20 mL/kg/h）で、およそ6時間で 3〜6 L を目安に、尿量や循環動態を確かめながら個別に調整する。乏尿・無尿が循環血液量の不足によらず輸液に反応しない場合は、前日の喪失量に 500〜1000 mL/日 を加えた量に制限し、カリウムを含む輸液は避ける。高カリウム血症は直ちに治療し（グルコン酸カルシウム、グルコース・インスリン療法、重炭酸ナトリウム、β2刺激薬など）、最も有効な治療は血液透析である。血液浄化の絶対的な適応は、血清カリウム 6.5 mmol/L 以上または他の治療に反応しない急速な上昇、pH 7.1 以下、BUN 100 mg/dL 以上またはクレアチニン 8 mg/dL 以上、尿毒症の症状（体液過剰、心膜炎、出血、原因不明の意識の変化）、十分な輸液でも続く乏尿・無尿である。筋膜切開はルーチンには行わず、区画内圧が 30 mmHg を超えて6時間以内に低下傾向がない場合や、区画内圧と拡張期血圧の差が 30 mmHg 未満の場合に緊急に行い、区画内圧が上昇する場合はマンニトールを考慮して、1時間以内に明らかな改善がなければ外科的筋膜切開に移る。
    condition:
      region: 国際
      対象: 挫滅症候群患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1967
    source: Sever MS, Vanholder R; RDRTF of ISN Work Group on Recommendations for the Management of Crush Victims in Mass Disasters. Recommendation for the management of crush victims in mass disasters. Nephrol Dial Transplant. 2012;27 Suppl 1:i1-i67
    doi: 10.1093/ndt/gfs156
    pmid: '22467763'
    pmcid: null
    url: https://doi.org/10.1093/ndt/gfs156
    source_license: Nephrology Dialysis Transplantation（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はいずれも推奨集本文の推奨文に基づき、一部は本文の表（Table 8、高カリウム血症の重症度と治療）から読み取った。災害時の多数傷病者を主対象とした推奨であり、日常診療における単発の挫滅症候群への適用は状況に応じて判断される。薬剤については、グルコン酸カルシウム、重炭酸ナトリウム、ポリスチレンスルホン酸ナトリウム（ケイキサレート）はいずれも国内で承認された薬剤で、このうちポリスチレンスルホン酸ナトリウムには高カリウム血症そのものの適応がある。一方、グルコースとインスリンの点滴による高カリウム血症治療、β2刺激薬の高カリウム血症への使用、マンニトールの区画内圧上昇の予防への使用は、国内の添付文書の適応には含まれない使い方である。（出典内の位置：推奨文 II.4.A、II.6、III.2.D、IV.1、V.3 と Table 8）
  curriculum:
    kokushi: 医学各論 Ⅸ-10-E-⑤（挫滅<圧挫>症候群<crush syndrome>、a）
    core_curriculum: 'TBL-01-00-123 (id: Jlvnlno)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: EP-045
  domain: EP
  subdomain: 欠神発作
  assertion:
    plain_statement_ja: 小児欠神てんかんは2〜12歳（ピーク5〜7歳）に発症し、定型欠神発作は数秒から20秒程度の意識・反応の消失が突然始まり突然終わる発作で、1日に何十回も繰り返し、過呼吸で誘発される。診断には定型欠神発作に加え、発作開始時に3 Hz（範囲2.5〜4 Hz）の全般性棘徐波が脳波で認められることが必須とされる。欠神発作は思春期頃までに消失することが多い。
    condition:
      region: 国際
      対象: 小児欠神てんかんの小児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4812
    source: 'Hirsch E, French J, Scheffer IE, et al. ILAE definition of the Idiopathic Generalized Epilepsy Syndromes: Position statement by the ILAE Task Force on Nosology and Definitions. Epilepsia. 2022;63(6):1475-1499'
    doi: 10.1111/epi.17236
    pmid: '35503716'
    pmcid: null
    url: https://doi.org/10.1111/epi.17236
    source_license: CC BY 4.0（Epilepsia、Europe PMC の license 欄で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 発症年齢、発作の持続・頻度、過呼吸による誘発、脳波の必須所見は、ILAE の特発性全般てんかん症候群の定義（2022年）の小児欠神てんかんの診断基準と臨床像の記述で確認した。思春期頃までに消失することが多い点は定性的な予後の記述として入れたもので、寛解率の数値は含めていない。症候群分類上の位置づけは既存カード EP-006（SRC-1717）が担う。
  curriculum:
    kokushi: 医学各論 Ⅸ-11-C-②（欠神発作<全般非運動発作>、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-053 (id: Jlvnleo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BT-020
  domain: BT
  subdomain: 転移性脳腫瘍
  assertion:
    plain_statement_ja: 脳転移は全癌患者の約20%に生じると推定され、原発巣の多くは肺癌、乳癌、大腸癌、悪性黒色腫、腎細胞癌である。
    condition:
      region: 国際
      対象: 癌患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4813
    source: Achrol AS, Rennert RC, Anders C, et al. Brain metastases. Nat Rev Dis Primers. 2019;5(1):5
    doi: 10.1038/s41572-018-0055-y
    pmid: '30655533'
    pmcid: null
    url: https://doi.org/10.1038/s41572-018-0055-y
    source_license: Nature Reviews Disease Primers（Springer Nature、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頻度と原発巣の構成は総説の抄録で確認。原発巣としては肺癌が最も多いことが疫学として知られているが、本総説の抄録では原発巣別の割合の数値を確認できなかったため、主張に順位と割合の数値は含めていない（既存カード BT-017 の uncertainty も同じ事情を記している）。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-C-①（転移性脳腫瘍、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-633 (id: JlvnmbI)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BT-021
  domain: BT
  subdomain: 転移性脳腫瘍
  assertion:
    plain_statement_ja: 転移性脳腫瘍の診断では造影MRIが中心的な画像検査であり、病変の大きさ・形態・個数を評価する。治療方針は転移の個数にも左右されるため個数の正確な把握が必要であり、確定診断には生検を要することもある。
    condition:
      region: 国際
      対象: 転移性脳腫瘍が疑われる患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4814
    source: 'Tong E, McCullagh KL, Iv M. Advanced Imaging of Brain Metastases: From Augmenting Visualization and Improving Diagnosis to Evaluating Treatment Response. Front Neurol. 2020;11:270'
    doi: 10.3389/fneur.2020.00270
    pmid: '32351445'
    pmcid: PMC7174761
    url: https://doi.org/10.3389/fneur.2020.00270
    source_license: CC BY 4.0（Frontiers in Neurology、PMC のライセンス表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 造影MRIが診断で優先される画像検査であること、造影T1強調像とT2強調FLAIR像が標準的に用いられることは総説本文で確認した。原発巣の検索の進め方や髄膜癌腫症の評価など診断手順の全体は本カードの範囲外。
  curriculum:
    kokushi: 医学各論 Ⅸ-2-C-①（転移性脳腫瘍、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-633 (id: JlvnmbI)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: NI-030
  domain: NI
  subdomain: 髄膜炎
  assertion:
    plain_statement_ja: 成人の細菌性髄膜炎で最も多い臨床所見は発熱、頭痛、項部硬直、意識障害であり、発熱・項部硬直・意識障害の古典的三徴がそろうのは患者の半数以下で、個々の所見が欠けても細菌性髄膜炎は否定できない。診断の確定には腰椎穿刺による髄液検査が中心となる。穿刺に先立って頭部CTを行うのは、局所神経脱落所見（脳神経麻痺を除く）、新規発症のけいれん、Glasgow Coma Scale 10未満の高度の意識障害、高度の免疫不全のいずれかがある場合に限られ、これらがなければCTを待たずに穿刺する。穿刺が遅れる場合は血液培養を採取したうえで経験的抗菌薬投与を先行させ、抗菌薬投与は来院後1時間以内が目標とされる。
    condition:
      region: 欧州
      対象: 細菌性髄膜炎が疑われる成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4815
    source: 'van de Beek D, Cabellos C, Dzupova O, et al. ESCMID guideline: diagnosis and treatment of acute bacterial meningitis. Clin Microbiol Infect. 2016;22 Suppl 3:S37-S62'
    doi: 10.1016/j.cmi.2016.01.007
    pmid: '27062097'
    pmcid: null
    url: https://doi.org/10.1016/j.cmi.2016.01.007
    source_license: © European Society of Clinical Microbiology and Infectious Diseases（Elsevier、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは ESCMID ガイドライン（2016年）の本文で確認した範囲に基づく。既存カード NI-008 の出典である細菌性髄膜炎診療ガイドライン2014（国内）は本文未入手のため、臨床像と初期評価の逐語確認が可能な本ガイドラインを新規出典とした。Kernig 徴候・Brudzinski 徴候などの髄膜刺激徴候は感度が低く診断への寄与は限られることが同ガイドラインに記載されている。小児では発熱・頭痛・項部硬直・嘔吐が多いとされるが、本カードは成人の所見に絞った。経験的抗菌薬の具体的な薬剤選択は既存カード NI-009〜011 が担い、本カードでは薬剤名は含めていない（国内で承認された抗菌薬製剤を用いる）。
  curriculum:
    kokushi: 医学各論 Ⅸ-3-A-②（髄膜炎、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: PN-025
  domain: PN
  subdomain: 三叉神経痛
  assertion:
    plain_statement_ja: 三叉神経痛の発作は、三叉神経の支配領域に限局する片側性の電撃様の痛みが突然始まり突然終わる発作で、持続は1秒未満から2分以内であり、洗顔、咀嚼、歯磨きなどの無害な刺激で誘発される。病型は、神経血管接触による一次性（古典的または特発性）と、それ以外の病変による二次性に分けられ、臨床像だけでは二次性を除外できないため、鑑別にはMRIが必要である。
    condition:
      region: 欧州
      対象: 三叉神経痛の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1365
    source: Bendtsen L, Zakrzewska JM, Abbott J, et al. European Academy of Neurology guideline on trigeminal neuralgia. Eur J Neurol. 2019;26(6):831-849
    doi: 10.1111/ene.13950
    pmid: '30860637'
    pmcid: null
    url: https://doi.org/10.1111/ene.13950
    source_license: © European Academy of Neurology（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 発作の臨床像（電撃様、短時間、無害な刺激による誘発、三叉神経支配領域に限局）は、欧州神経学会ガイドラインが使用を推奨する国際頭痛分類第3版（ICHD-3）の三叉神経痛の記述と診断基準で確認した。分類とMRIの必要性は同ガイドラインの抄録で確認した。二次性の背景病変としては多発性硬化症や腫瘍などが知られるが、本カードの主張には個別の病変名を含めていない。治療薬（カルバマゼピン等）と手術は既存カード OT-037 が担い、本カードでは扱わない。
  curriculum:
    kokushi: 医学各論 Ⅸ-5-C-①（三叉神経痛、a）；医学各論 Ⅲ-8-C-②（三叉神経痛、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: SP-030
  domain: SP
  subdomain: 変形性脊椎症
  assertion:
    plain_statement_ja: 変形性脊椎症は、椎間板、椎体および椎間関節の変性変化を総称する概念である。病態は椎間板の変性から始まる段階的な経過（変性カスケード）をたどり、椎間板の狭小化や線維化とともに骨棘形成が進んで安定化に向かう。臨床像は軸性疼痛が中心で、神経根症や、脊柱管狭窄による神経性跛行（立位・歩行で増悪し座位・臥位で軽快する下肢痛やしびれ）を伴うことがある。治療に確立した標準はなく、運動療法を中心とする保存療法が基本であり、手術は保存療法が奏効しない場合に検討される。
    condition:
      region: 国際
      対象: 変形性脊椎症の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4817
    source: 'Middleton K, Fish DE. Lumbar spondylosis: clinical presentation and treatment approaches. Curr Rev Musculoskelet Med. 2009;2(2):94-104'
    doi: 10.1007/s12178-009-9051-x
    pmid: '19468872'
    pmcid: PMC2697338
    url: https://doi.org/10.1007/s12178-009-9051-x
    source_license: CC BY-NC（Springer、PMC のライセンス表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は腰椎の変形性脊椎症を対象とした総説であり、本カードの記述も腰椎の病態・臨床像に基づく（項目自体は脊椎全体の変形性脊椎症を指す）。運動療法以外の保存療法として NSAIDs や手技療法、日常の身体活動の維持が同総説に挙げられている。NSAIDs は国内で疼痛・炎症性疾患の適応で広く承認されている薬剤群であり、変形性脊椎症に固有の適応ではない。画像所見のみで症状の原因と判断できない点は既存カード SP-004 が担う。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-A-②（変形性脊椎症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-138 (id: JlvnlpU)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
```


## 3. カリキュラム対応表

| カード | subdomain | kokushi | コアカリ |
|---|---|---|---|
| SM-010 | 妊婦・胎児への影響 | 医学各論 ⅩⅢ-3-B-③（妊婦・胎児への影響、a） | GE-04-01-06 (id: JkxpswA)；PS-02-11-05 (id: JkxnuSU) |
| OC-024 | 頸肩腕障害 | 医学各論 ⅩⅢ-4-B-②（頸肩腕障害、a） | SO-01-04-03 (id: JkxoNtg)；TBL-02-04-014 (id: Jlvnlp8) |
| OC-025 | 虚血性心疾患 | 医学各論 ⅩⅢ-4-C-②（虚血性心疾患、a） | SO-01-04-03 (id: JkxoNtg) |
| OC-026 | 心身症 | 医学各論 ⅩⅢ-4-D-②（心身症、a） | PS-02-17-05 (id: JkxnuT8)；TBL-01-00-546 (id: JlvnmUc) |
| EV-025 | 偶発性低体温{症} | 医学各論 ⅩⅢ-5-A-②（偶発性低体温{症}、a） | PS-03-05-10 (id: Jkxnub4) |
| EV-026 | 騒音性難聴 | 医学各論 ⅩⅢ-5-B-①（騒音性難聴、a） | PS-03-05-11 (id: Jkxnub8)；TBL-02-15-010 (id: JlAKpwY) |
| EV-027 | 誤嚥 | 医学各論 ⅩⅢ-5-G-②（誤嚥、a） | PS-03-05-04 (id: Jkxnubg)；TBL-01-00-212 (id: Jlvnlx0) |
| EV-028 | 創傷 | 医学各論 ⅩⅢ-5-G-③（創傷、a） | PS-03-05-12 (id: Jkxir3g) |
| EV-029 | 急性中毒 | 医学各論 ⅩⅢ-5-G-⑤（急性中毒、a） | PS-03-05-06 (id: Jkxnubo)；PS-03-05-07 (id: Jkxnubs)；PS-03-05-08 (id: Jkxnubw) |
| EV-030 | 交通事故 | 医学各論 ⅩⅢ-5-I-①（交通事故、a） | SO-01-05-01 (id: JkxoNtw)；PS-03-05-12 (id: Jkxir3g) |
| EV-031 | 自然災害 | 医学各論 ⅩⅢ-5-I-③（自然災害、a） | SO-01-05-01 (id: JkxoNtw) |
| ST-051 | 廃用性萎縮 | 医学各論 Ⅸ-1-E-②（廃用性萎縮、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-028 (id: JlvnlcQ) |
| ND-062 | 脳血管性認知症 | 医学各論 Ⅸ-1-E-③（脳血管性認知症、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-039 (id: JlvnldY) |
| ND-063 | 一酸化炭素中毒 | 医学各論 Ⅸ-4-I-①（一酸化炭素中毒<CO中毒>、a） | PS-02-03-05 (id: JkxnuP0) |
| ND-064 | 低酸素脳症 | 医学各論 Ⅸ-4-I-②（低酸素脳症、a） | PS-02-03-05 (id: JkxnuP0)；TBL-02-02-021 (id: JlAKpYw) |
| TJ-077 | 骨盤骨折 | 医学各論 Ⅸ-10-C-②（骨盤骨折、a） | TBL-01-00-118 (id: Jlvnlm8)；TBL-01-00-120 (id: Jlvnlnk) |
| TJ-078 | 脱臼、亜脱臼 | 医学各論 Ⅸ-10-D-③（脱臼、亜脱臼、a） | TBL-01-00-121 (id: JlvnlnE) |
| TJ-079 | 筋断裂、腱断裂 | 医学各論 Ⅸ-10-E-③（筋断裂、腱断裂、a） | TBL-01-00-123 (id: Jlvnlno) |
| TJ-080 | 挫滅症候群 | 医学各論 Ⅸ-10-E-⑤（挫滅<圧挫>症候群<crush syndrome>、a） | TBL-01-00-123 (id: Jlvnlno) |
| EP-045 | 欠神発作 | 医学各論 Ⅸ-11-C-②（欠神発作<全般非運動発作>、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-053 (id: Jlvnleo) |
| BT-020 | 転移性脳腫瘍 | 医学各論 Ⅸ-2-C-①（転移性脳腫瘍、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-633 (id: JlvnmbI) |
| BT-021 | 転移性脳腫瘍 | 医学各論 Ⅸ-2-C-①（転移性脳腫瘍、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-633 (id: JlvnmbI) |
| NI-030 | 髄膜炎 | 医学各論 Ⅸ-3-A-②（髄膜炎、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| PN-025 | 三叉神経痛 | 医学各論 Ⅸ-5-C-①（三叉神経痛、a）；医学各論 Ⅲ-8-C-②（三叉神経痛、a） | PS-02-16-05 (id: JkxnuTo) |
| SP-030 | 変形性脊椎症 | 医学各論 Ⅸ-7-A-②（変形性脊椎症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-138 (id: JlvnlpU) |

## 4. 未解決事項

- SRC-4801（Cochrane 妊娠中の禁煙支援、2026年版）の PMID・PMCID・ライセンス表示は未確認（null・UNKNOWN）。取り込み側の照合で確定されたい
- SRC-4803（IFRC 応急処置ガイドライン2020）は CC 表示なしのため RESTRICTED。公式リソース URL は引用資料経由の確認で、到達性の再確認を推奨する
- SRC-4804（CDC 破傷風予防の創管理ガイダンス）は版・更新日の明示がなく、米国の判断基準と国内運用（トキソイドの接種間隔等）の照合は残課題
- SRC-4805（消費者庁・JPIC の解説書）の基データは1999〜2008年と古い。JPIC の近年の年次統計が公開されれば差し替え候補
- EV-030（交通事故）は自動車乗車中・二輪車乗車中の状態別死者数を図から確実に読み取れず未収載（交通安全白書の表で補完の可能性）。EV-031（自然災害）は能登半島地震の災害関連死が認定進行中のため数値を入れていない
- ST-051（廃用性萎縮）は拘縮の具体（頻度・時期）を出典の抄録で確認できず主張に入れていない。TJ-078（脱臼）は定義文と分類の体系、TJ-079（筋・腱断裂）は身体診察の具体と一次縫合の時期が未カバー
- ND-062（脳血管性認知症）は認知症疾患診療ガイドライン2026年版の本文が照合できず国際総説によった。本文が入手できれば国内ガイドラインでの照合・差し替えが候補
- OC-025 の認定基準の通達本文（SRC-4043）の逐語照合は未了（OC-010・011 と同じ残件）
- EP-045 の診断基準は ILAE の定義論文（SRC-4812）で確認した。既存の症候群分類の文書（SRC-1717）の本文にも小児欠神てんかんの節がある見込みで、取り込み側で同基準の所在を再確認されたい
- 未使用の SRC 番号：SRC-4818〜4880（この回では使わない）

## 5. 引き継ぎメモ

- EP-046 を本編に入れなかった理由と、EP-007・EP-008 への Ⅸ-11-C-② の番号追加という本来の形は冒頭に記載した。分離した起案は 65_appendix_ep046.md
- ND-063（一酸化炭素中毒）の高気圧酸素療法の位置づけは、Cochrane レビューを出典登録せず、既存 ND-054 と同様に uncertainty 内で書誌を明記して引用する形にした
- PN-025（三叉神経痛）の kokushi は第Ⅸ章側を先にしたが、既存カード OT-037 は逆順（Ⅲ側が先）。取り込み側で表記順をそろえる場合は判断されたい
- EV-027（誤嚥）は依頼表の見込み（SRC-4131 系統）では抄録に手技の手順がなく、表の但し書きに従い IFRC ガイドライン（SRC-4803）に切り替えた
- EV-026 により、既存 EV-006 の uncertainty にあった「本文での逐語確認はしていない」は解消した。既存カード側の注記の扱いは取り込み側の判断
- 薬剤名のあるカード（SM-010 のニコチン製剤、EV-028 の破傷風トキソイド・免疫グロブリン、EP-045 以外では SP-030 の NSAIDs など）は、すべて uncertainty に薬剤名を特定した国内承認・保険適用の注記を入れた
