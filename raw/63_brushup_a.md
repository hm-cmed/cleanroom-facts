# 第63回 成果物（ブラッシュアップA：眼・耳・鼻・口腔・外傷、レベル a 項目の増強）

- 依頼文：docs/tasks/round62_BRUSHUP_A.md の「第63回」（仕様 specs/round63.yaml）
- 対象：25項目（Ⅲ-4〜11）。すべてレベル a
- 件数：26件（EY-060〜061、RE-031、OT-045〜051、NL-023、OR-033〜044、TR-029〜031）。各項目1件（急性扁桃炎は1件で臨床像・診断・合併症を担う）
- 新規出典：15件（SRC-4621〜4635）。未使用：SRC-4636〜4720
- 既存カードは直さず、各項目に依頼文の表の「2件目に書く側面」の新しいカードを足した。既存出典の再利用は、担当側面がその出典で確認できたものだけ（11件分）

## 判断・申し送り（要点）

- **NL の開始番号**：仕様では null のため、依頼文の「続き」指定と第61回で NL-022 まで使用・取り込み済みの経緯から、鼻せつは NL-023 とした。取り込み側の採番と合わなければ付け替えていただきたい
- EY-060（調節異常）は調節緊張・仮性近視の側に限定した。調節麻痺を担う一次資料級の総説が見つからず、項目自体は本カードで充足するが、調節麻痺側は将来の追加候補として §4 に残した
- OT-048（老人性難聴）は Cochrane レビューの2026年改訂版（SRC-4625）を確認して採用し、数値はすべて改訂版で照合した
- OT-047 の出典は、地ならしメモに著者名の取り違えがあり、DOI・PMID・PMCID から特定される Schacht らの総説（SRC-4624）が正しい
- OR-043（頸部膿瘍）は再利用見込みだった SRC-1450 の抄録で臨床像・合併症が確認できなかったため、新規レビュー（SRC-4634）に切り替えた（SRC-1450 自体は OR-029 で使用済み）
- OR-044（リンパ節転移）のレベル分類は、出典ガイドラインでは図のみで各レベルの境界定義を本文確認できなかったため、主張は「転移の分布を記載する枠組み」の水準に留めた
- RE-031 は EULAR 推奨の2025年改訂版（SRC-4622、Ann Rheum Dis 2026年掲載）に基づく。日本の承認の範囲（インフリキシマブは難治性網膜ぶどう膜炎等）との違いは uncertainty に明記した

## 1. 出典ホワイトリスト（この回のカードが使う出典）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-1210 | Pynnonen MA, Gillespie MB, Roman B, Rosenfeld RM, et al. Clinical Practice Guideline: Evaluation of the Neck Mass in Adults. Otolaryngol Head Neck Surg. 2017;157(2_suppl):S1-S30. | 10.1177/0194599817722550 | 28891406 | © American Academy of Otolaryngology-Head and Neck Surgery Foundation（SAGE、CC表示なし） | UNKNOWN | 既存マスター登録済み。ガイドライン本文 PDF（推奨文、画像検査と FNA の節、リンパ節レベルの図）で確認 |
| SRC-1276 | Xie JS, Donaldson L, Margolin E. Papilledema: A review of etiology, pathophysiology, diagnosis, and management. Surv Ophthalmol. 2022;67(4):1135-1159 | 10.1016/j.survophthal.2021.11.007 | 34813854 | ライセンス表示を確認できず | UNKNOWN | 既存出典（出典マスター登録済み。第63回で再利用） |
| SRC-1349 | Rosenfeld RM, Shin JJ, Schwartz SR, et al. Clinical Practice Guideline: Otitis Media with Effusion (Update). Otolaryngol Head Neck Surg. 2016;154(1 Suppl):S1-S41 | 10.1177/0194599815623467 | 26832942 | ライセンス表示を確認できず | UNKNOWN | 既存出典（出典マスター登録済み。第63回で再利用） |
| SRC-1363 | Zhang LL, Wang JQ, Qi RR, Pan LL, Li M, Cai YL. Motion Sickness: Current Knowledge and Recent Advance. CNS Neurosci Ther. 2016;22(1):15-24 | 10.1111/cns.12468 | 26452639 | © John Wiley & Sons（CC表示は Crossref・PMC で確認できず） | UNKNOWN | 既存出典（出典マスター登録済み。第63回で再利用） |
| SRC-1366 | Kanagalingam S, Miller NR. Horner syndrome: clinical perspectives. Eye Brain. 2015;7:35-46 | 10.2147/EB.S63633 | 28539793 | CC BY-NC 3.0 | RESTRICTED | 既存出典（出典マスター登録済み。第63回で再利用） |
| SRC-1432 | Akintoye SO, Greenberg MS. Recurrent aphthous stomatitis. Dent Clin North Am. 2014;58(2):281-297. | 10.1016/j.cden.2013.12.002 | 24655523 | ライセンス未確認 | UNKNOWN | 既存出典（OR-002 と同一）。PMC 全文（PMC3964366）の Management の項を開き、重症度・頻度・大きさ・個数に応じた外用療法・外用グルココルチコイド・局所注射・全身療法の記載を照合 |
| SRC-1439 | Shulman ST, Bisno AL, Clegg HW, et al. Clinical practice guideline for the diagnosis and management of group A streptococcal pharyngitis: 2012 update by the Infectious Diseases Society of America. Clin Infect Dis. 2012;55(10):e86-e102. | 10.1093/cid/cis629 | 22965026 | CCライセンス表示なし（学会ガイドライン） | RESTRICTED | 既存出典（OR-012 と同一）。PMC 全文（PMC7108032）で、臨床スコアの位置づけ、検査による確認の原則、第一選択薬と投与期間、治療の目的（合併症予防、発症9日以内の開始で急性リウマチ熱を予防、溶連菌感染後糸球体腎炎は予防できないこと）を照合 |
| SRC-1440 | Kaditis AG, Alonso Alvarez ML, Boudewyns A, et al. Obstructive sleep disordered breathing in 2- to 18-year-old children: diagnosis and management. Eur Respir J. 2016;47(1):69-94. | 10.1183/13993003.00385-2015 | 26541535 | CCライセンス表示なし（学会ステートメント） | RESTRICTED | 既存出典（OR-013 と同一）。ERJ 全文で、ステップ1の症状（頻回の大きな音のいびき、目撃される無呼吸、不穏な睡眠、口呼吸）とステップ6のアデノトンシレクトミーの適応（閉塞性睡眠時無呼吸症候群＋アデノイド・扁桃肥大、AHI 5回/時超で改善が最も得られやすく、成功率約75%）を照合 |
| SRC-1456 | McIntosh SE, Freer L, Grissom CK, Rodway GW, et al. Wilderness Medical Society Clinical Practice Guidelines for the Prevention and Treatment of Frostbite: 2024 Update. Wilderness & Environmental Medicine. 2024;35(2):183-197. | 10.1177/10806032231222359 | 38577729 | ライセンス表示を確認できず（学会ガイドライン、CC表示なし） | UNKNOWN | 既存マスター登録済み。WMS 公式要約（凍傷の分類の節）で4度分類と現場向け2分類を確認 |
| SRC-1459 | Bizrah M, Yusuf A, Ahmad S. An update on chemical eye burns. Eye (London). 2019;33(9):1362-1377. | 10.1038/s41433-019-0456-5 | 31086244 | ライセンス表示を確認できず | UNKNOWN | 既存マスター登録済み。PMC 本文（Roper-Hall 分類の表、洗浄療法の節）で確認 |
| SRC-4621 | García-Montero M, Felipe-Márquez G, Arriola-Villalobos P, Garzón N. Pseudomyopia: A Review. Vision (Basel). 2022;6(1):17 | 10.3390/vision6010017 | 35324602 | CC BY 4.0（PMC掲載ページで表示を確認） | OPEN | PMCの全文（PMC8950661）を開いて確認。出典マスターにDOI・PMIDの一致なし（新規） |
| SRC-4622 | Hatemi G, Ramiro S, Ozguler Y, et al. EULAR recommendations for the management of Behçet's syndrome: 2025 update. Ann Rheum Dis. 2026;85(6):1010-1025 | 10.1016/j.ard.2026.02.009 | 41876291 | ライセンス表示を確認できず | RESTRICTED | 出版社の全文ページを開き、Eye involvement の Recommendation 4 とその解説本文を確認。出典マスターにDOI・PMIDの一致なし（新規。2018年改訂版のDOIも登録なし） |
| SRC-4623 | Heim SW, Maughan KL. Foreign bodies in the ear, nose, and throat. Am Fam Physician. 2007;76(8):1185-1189 | なし（PubMedレコードにDOIの記載なし） | 17990843 | ライセンス表示を確認できず | RESTRICTED | AAFPサイトの全文とPubMedレコードを確認。出典マスターにPMID・題名の一致なし（新規） |
| SRC-4624 | Schacht J, Talaska AE, Rybak LP. Cisplatin and aminoglycoside antibiotics: hearing loss and its prevention. Anat Rec (Hoboken). 2012;295(11):1837-1850 | 10.1002/ar.22578 | 23045231 | © Wiley（PMC掲載は著者原稿で、CC表示を確認できず） | UNKNOWN | PMCの全文（PMC3596108）を開いて薬剤別の特徴を確認し、PubMedレコードで書誌を照合。出典マスターにDOI・PMIDの一致なし（新規） |
| SRC-4625 | Ferguson MA, Sarant JZ, Bennett RJ, McIlhiney P, Badcock N, Bothe E. Hearing aids for mild to moderate hearing loss in adults. Cochrane Database Syst Rev. 2026;8(8):CD012023 | 10.1002/14651858.CD012023.pub3 | 42644645 | CC BY-NC-ND 4.0（PMC掲載ページで表示を確認） | RESTRICTED | 2017年版（PMC6483809）の「2026年版への更新あり」の表示から改訂版を特定し、PMCの全文（PMC13509011）とPubMedレコードで改訂版の書誌と数値を確認。出典マスターにDOI・PMIDの一致なし（新規） |
| SRC-4626 | Bae CH, Na HG, Choi YS. Current diagnosis and treatment of vestibular neuritis: a narrative review. Yeungnam Univ J Med. 2022;39(2):81-88 | 10.12701/yujm.2021.01228 | 34411472 | CC BY-NC 4.0（PMC掲載ページで表示を確認） | RESTRICTED | PMCの全文（PMC8913909）を開いて臨床像・診断・対症療法を確認。出典マスターにDOI・PMIDの一致なし（新規） |
| SRC-4627 | Sheik-Ali S, Sheik-Ali S, Sheik-Ali A. Nasal vestibular furunculosis: Summarised case series. World J Otorhinolaryngol Head Neck Surg. 2022;8(3):217-223 | 10.1016/j.wjorl.2020.12.003 | 36159901 | CC BY-NC-ND 4.0（PMC掲載ページで表示を確認） | RESTRICTED | PMCの全文（PMC9479471）を開いて臨床像・管理・合併症を確認。出典マスターにDOI・PMIDの一致なし（新規） |
| SRC-4628 | Chiang CP, Chang JYF, Wang YP, Wu YH, Wu YC, Sun A. Atrophic glossitis: Etiology, serum autoantibodies, anemia, hematinic deficiencies, hyperhomocysteinemia, and management. J Formos Med Assoc. 2020;119(4):774-780. | 10.1016/j.jfma.2019.04.015 | 31076315 | CC BY-NC-ND 4.0 | RESTRICTED | 新規出典。PubMed で書誌・DOI・PMID を確認し、抄録で萎縮性舌炎の定義・背景疾患・頻度・管理を照合。出典マスターに DOI・PMID とも登録なし。ライセンスは誌（J Formos Med Assoc、オープンアクセス誌）の標準ライセンス CC BY-NC-ND 4.0 を同誌掲載論文の表示で確認 |
| SRC-4629 | Coppola N, Cantile T, Adamo D, et al. Supportive care and antiviral treatments in primary herpetic gingivostomatitis: a systematic review. Clin Oral Investig. 2023;27(11):6333-6344. | 10.1007/s00784-023-05250-5 | 37733027 | CC BY 4.0 | OPEN | 新規出典。PubMed と PMC 全文（PMC10630243）で書誌・DOI・PMID・PMCID・ライセンス（CC BY 4.0）を確認し、序論の臨床像・経過と、支持療法および発症72時間以内のアシクロビル経口投与の位置づけを照合。出典マスターに DOI・PMID とも登録なし |
| SRC-4630 | 国立健康危機管理研究機構 感染症情報提供サイト「ヘルパンギーナ」（2014年7月23日改訂） | なし | なし | 政府機関の公開ページ | GOV_JP | 新規出典。同ページ本文（冒頭の定義、疫学、臨床症状、治療・予防の各項）を開いて照合。出典マスターに同ページの登録なし |
| SRC-4631 | Gauer RL, Semidey MJ. Diagnosis and Treatment of Temporomandibular Disorders. Am Fam Physician. 2015;91(6):378-386. | なし | 25822556 | CC表示なし（© American Academy of Family Physicians） | RESTRICTED | 新規出典。PubMed で書誌・PMID を確認（DOI の登録なし）し、AAFP の全文 PDF で臨床像（咀嚼筋圧痛・関節音・開口制限）と分類、非侵襲的治療を基本とする治療原則を照合。出典マスターに PMID の登録なし |
| SRC-4632 | Galioto NJ. Peritonsillar Abscess. Am Fam Physician. 2017;95(8):501-506. | なし（PubMed レコードに DOI の記載なし） | 28409615 | © 2017 American Academy of Family Physicians（CC表示なし） | RESTRICTED | PubMed 抄録と出版社 PDF 本文（症状・所見の表、ドレナージ法の比較、扁桃摘出の位置づけ）で確認。出典マスターに DOI・PMID とも未登録であることを確認 |
| SRC-4633 | Lang S, Kansy B. Cervical lymph node diseases in children. GMS Curr Top Otorhinolaryngol Head Neck Surg. 2014;13:Doc08. | 10.3205/cto000111 | 25587368 | CC BY-NC-ND 3.0 | RESTRICTED | PMC 本文（原因の内訳、悪性を示唆する所見、超音波と組織診断の進め方、川崎病の節）で確認。出典マスターに DOI・PMID とも未登録であることを確認 |
| SRC-4634 | Cobzeanu BM, Moisii L, Palade OD, et al. Management of Deep Neck Infection Associated with Descending Necrotizing Mediastinitis: A Scoping Review. Medicina (Kaunas). 2025;61(2):325. | 10.3390/medicina61020325 | 40005441 | CC BY 4.0 | OPEN | PubMed 抄録と PMC 本文で確認（症状、縦隔への進展と合併症、CT の位置づけ、ドレナージと抗菌薬）。出典マスターに DOI・PMID とも未登録であることを確認 |
| SRC-4635 | Smith I, Kidd S, Kim S, Tennill RM. Assessment and Management of Electrical Injuries in Adults in the Emergency Department. Cureus. 2026;18(4):e107162. | 10.7759/cureus.107162 | 未確認（下記メモ参照） | CC BY 4.0 | OPEN | 出版社 PDF 本文（電流の経路、心電図とモニタリングの基準、横紋筋融解・腎障害・コンパートメント症候群の節）で確認。出典マスターに DOI 未登録であることを確認 |

## 2. 事実カード（YAML）

```yaml
- id: EY-060
  domain: EY
  subdomain: 調節異常
  assertion:
    plain_statement_ja: 仮性近視は、調節の過剰な働き（調節緊張）によって眼の屈折力が増し、遠見視力が下がって近視のように見える状態で、毛様体筋が光学的無限遠でも十分に弛緩しないために生じる。完全な調節麻痺下の屈折検査では消失し、通常の屈折値と調節麻痺下の屈折値との差が診断の手がかりになる。症状は遠見のぼやけや変動、頭痛などで、視力・検影・瞳孔の変動として観察されることがある。近業の後には0.2〜0.6ジオプトリー程度の一過性の近視化がみられることがあり、未矯正の遠視、間欠性外斜視、情緒・心理的要因、頭部外傷を含む脳損傷との関連も報告されている。縮瞳や輻湊の痙攣を伴う近見反射痙攣の形をとることもあれば、単独で生じることもある。
    condition:
      region: 全般
      対象: 調節緊張（仮性近視）の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4621
    source: 'García-Montero M, Felipe-Márquez G, Arriola-Villalobos P, Garzón N. Pseudomyopia: A Review. Vision (Basel). 2022;6(1):17'
    doi: 10.3390/vision6010017
    pmid: '35324602'
    pmcid: PMC8950661
    url: https://doi.org/10.3390/vision6010017
    source_license: CC BY 4.0（PMC掲載ページで表示を確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典は仮性近視に特化した総説であり、調節麻痺そのものの成因・経過・治療は本文で扱われていない。本カードは調節緊張（仮性近視）の側面に限り、調節麻痺については一次資料級の総説を確認できなかったため含めていない。数値（近業後の一過性近視化0.2〜0.6ジオプトリー）は総説本文の記載に基づく。本カードには薬剤名を含めていない（調節麻痺下検査に用いる薬剤の個別の承認状況は記載していない）。
  curriculum:
    kokushi: 医学各論 Ⅲ-4-A-③（調節異常、a）
    core_curriculum: 'PS-02-15-05 (id: JkxnuTU)；TBL-01-00-489 (id: JlvnmNk)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: EY-061
  domain: EY
  subdomain: うっ血乳頭
  assertion:
    plain_statement_ja: うっ血乳頭の治療は、原因疾患への対応が基本である。特発性頭蓋内圧亢進症では、多くの患者が減量と経口アセタゾラミドに反応する。来院時に中心視力の低下と視野狭窄がある患者、およびアセタゾラミドに反応しない患者では外科的治療を検討し、通常は脳室腹腔シャントが選択される手技である。
    condition:
      region: グローバル
      対象: うっ血乳頭の患者（特発性頭蓋内圧亢進症を含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1276
    source: 'Xie JS, Donaldson L, Margolin E. Papilledema: A review of etiology, pathophysiology, diagnosis, and management. Surv Ophthalmol. 2022;67(4):1135-1159'
    doi: 10.1016/j.survophthal.2021.11.007
    pmid: '34813854'
    pmcid: null
    url: https://doi.org/10.1016/j.survophthal.2021.11.007
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 主張の治療内容は出典（総説）の抄録で確認した範囲であり、薬剤の用量などの詳細は抄録に含まれていない。アセタゾラミドは国内で承認されている薬剤だが、その承認効能・効果は緑内障、てんかん（他の抗てんかん薬で効果不十分な場合に付加）、肺気腫における呼吸性アシドーシスの改善、心性浮腫、肝性浮腫、月経前緊張症、メニエル病及びメニエル症候群、睡眠時無呼吸症候群（錠剤）であり、特発性頭蓋内圧亢進症は承認効能に含まれないため、同症への使用は適応外使用となる。
  curriculum:
    kokushi: 医学各論 Ⅲ-4-B-①（うっ血乳頭、a）
    core_curriculum: 'PS-02-15-05 (id: JkxnuTU)；TBL-01-00-495 (id: JlvnmOc)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: RE-031
  domain: RE
  subdomain: Behçet病
  assertion:
    plain_statement_ja: Behçet病のぶどう膜炎では、全例に、臨床的寛解と蛍光眼底造影上の寛解の達成と維持を目標として免疫抑制療法を行う。後眼部の炎症が視力を脅かす場合には、モノクローナル抗TNFα抗体を用い、他の免疫抑制薬との併用でインフリキシマブが望ましいとされる。グルココルチコイドは炎症を速やかに抑えるのに有用で、0.5〜1 mg/kg/日で開始されるが、単独療法としては用いない。比較的軽症のぶどう膜炎ではアザチオプリンやシクロスポリンAなどの従来型免疫抑制薬で開始し、寛解が得られなければ生物学的製剤への切替えや追加を検討する余地がある。
    condition:
      region: 欧州（EULAR推奨）
      対象: Behçet病のぶどう膜炎患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4622
    source: 'Hatemi G, Ramiro S, Ozguler Y, et al. EULAR recommendations for the management of Behçet''s syndrome: 2025 update. Ann Rheum Dis. 2026;85(6):1010-1025'
    doi: 10.1016/j.ard.2026.02.009
    pmid: '41876291'
    pmcid: null
    url: https://doi.org/10.1016/j.ard.2026.02.009
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張はEULAR推奨2025年改訂版の Recommendation 4 とその解説本文の記載に基づく（グルココルチコイドの開始用量0.5〜1 mg/kg/日は本文の記載）。インフリキシマブは国内で「既存治療で効果不十分なベーチェット病による難治性網膜ぶどう膜炎」に承認され保険適用がある（厚生労働省の薬剤情報で確認）。同推奨で抗TNFα抗体として併せて論じられるアダリムマブは、国内では既存治療で効果不十分な非感染性の中間部・後部・汎ぶどう膜炎などに承認がある。ただし国内承認はいずれも既存治療で効果不十分な場合などに限られ、推奨における視力脅威例への早期使用の位置づけとは適用範囲が一致しない。日本のBehçet病診療ガイドラインとの推奨の差異は確認していない。出典の書誌は、誌面では2026年掲載（85巻6号）で、題名は「2025 update」である。
  curriculum:
    kokushi: 医学各論 Ⅲ-6-A-①（Behçet病、a）
    core_curriculum: 'PS-02-15-05 (id: JkxnuTU)；TBL-01-00-496 (id: JlvnmOY)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OT-045
  domain: OT
  subdomain: 外耳道異物
  assertion:
    plain_statement_ja: 外耳道異物の摘出には鉗子、水洗、吸引カテーテルなどの方法があり、成否は異物の位置、材質、把持できる形かどうか、患者の協力に左右される。生きた昆虫は、摘出の前にアルコール、2％リドカイン液、鉱物油などを注入して速やかに殺すが、鼓膜に穿孔がある場合はこの注入を行わない。ボタン電池では水洗を行わない（電流や電池の内容物によって液状化壊死を起こしうるため、速やかな摘出を要する）。最初の摘出の試みが最も重要で、失敗を繰り返すと成功率が下がり合併症が増えるため、鎮静や麻酔が必要な場合、外耳道や鼓膜に損傷がある場合、把持できない異物が外耳道の内側に強く嵌頓している場合、ガラスなど鋭利な異物の場合、摘出に失敗した場合は、専門科への紹介を検討する。
    condition:
      region: 米国
      対象: 外耳道異物の患者（小児に多い）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4623
    source: Heim SW, Maughan KL. Foreign bodies in the ear, nose, and throat. Am Fam Physician. 2007;76(8):1185-1189
    doi: null
    pmid: '17990843'
    pmcid: null
    url: https://www.aafp.org/pubs/afp/issues/2007/1015/p1185.html
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は米国の家庭医療向け総説（2007年）で、摘出法ごとの推奨を裏づけるエビデンスは出典自体が不十分としている。リドカインは国内承認薬（局所麻酔薬など）だが、外耳道内の昆虫を殺す目的での注入は承認された効能・効果ではなく、出典の記載に基づく使用法である。植物性の異物が水で膨らむため水洗を避けるという注意は、本出典の本文では確認できなかったため本カードには含めていない。
  curriculum:
    kokushi: 医学各論 Ⅲ-7-A-①（外耳道異物、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OT-046
  domain: OT
  subdomain: 滲出性中耳炎
  assertion:
    plain_statement_ja: 滲出性中耳炎では、ことばや学習の問題のリスクが高い児かどうかを判定し、リスクのある児は、そのリスク状態が診断された時点と生後12〜18か月の時点で評価する。滲出性中耳炎が3か月以上持続する場合、またはリスクのある児では持続期間にかかわらず、年齢に応じた聴力検査を行う。両側の滲出性中耳炎で難聴が記録された児の家族には、会話や言語の発達への影響について説明する。慢性の滲出性中耳炎は3〜6か月間隔で再評価する。手術を行う場合、4歳未満の児では鼓膜チューブ留置が推奨され、アデノイド切除は鼻閉や慢性アデノイド炎など別の適応がある場合に限る。4歳以上の児では、鼓膜チューブ留置、アデノイド切除、またはその両方が推奨される。
    condition:
      region: 米国
      対象: 生後2か月から12歳の小児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1349
    source: 'Rosenfeld RM, Shin JJ, Schwartz SR, et al. Clinical Practice Guideline: Otitis Media with Effusion (Update). Otolaryngol Head Neck Surg. 2016;154(1 Suppl):S1-S41'
    doi: 10.1177/0194599815623467
    pmid: '26832942'
    pmcid: null
    url: https://doi.org/10.1177/0194599815623467
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 主張は出典（米国の診療ガイドライン、2016年改訂版）の抄録に掲載されたアクションステートメントで確認した範囲である。日本の小児滲出性中耳炎の診療ガイドラインとの推奨の差異は確認していない。本カードには薬剤名を含めていない。
  curriculum:
    kokushi: 医学各論 Ⅲ-7-C-②（滲出性中耳炎、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-501 (id: JlvnmO0)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OT-047
  domain: OT
  subdomain: 薬剤性難聴
  assertion:
    plain_statement_ja: 薬剤性難聴（聴器毒性）の現れ方は原因薬剤によって異なる。白金製剤のシスプラチンは蝸牛のみを障害し、前庭障害はほとんどみられない。その難聴は両側性で、蝸牛の基底回転にある外有毛細胞の障害により高音域から始まり、投与が続くと低い音域へ広がる。アミノグリコシド系抗菌薬では、薬剤によって蝸牛毒性と前庭毒性の偏りが異なり、ゲンタマイシンは前庭毒性が強く、アミカシンとネオマイシンは主に蝸牛を障害する傾向があり、毒性の強さはネオマイシンが最も強い部類とされる。アミノグリコシドによる障害も両側性で高音域から始まり、症状は投与開始から数日〜数週間遅れて現れ、投与中止後も進行することがある。フロセミドなどのループ利尿薬は、単独では一過性の内耳への影響にとどまるが、アミノグリコシドと併用すると障害が著しく強まる。
    condition:
      region: 全般
      対象: 聴器毒性のある薬剤の投与を受ける患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4624
    source: 'Schacht J, Talaska AE, Rybak LP. Cisplatin and aminoglycoside antibiotics: hearing loss and its prevention. Anat Rec (Hoboken). 2012;295(11):1837-1850'
    doi: 10.1002/ar.22578
    pmid: '23045231'
    pmcid: PMC3596108
    url: https://doi.org/10.1002/ar.22578
    source_license: © Wiley（PMC掲載は著者原稿で、CC表示を確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードに挙げた薬剤（シスプラチン、ゲンタマイシン、アミカシン、ネオマイシン、フロセミド）はいずれも国内で承認されている薬剤であり、本カードは各薬剤の適応や用法を述べたものではなく、承認された治療に伴って生じうる聴器毒性の特徴を、原因薬剤としての観点から列挙したものである。個別薬剤の効能・効果と用法・用量は各製剤の添付文書による。ループ利尿薬については、出典の記載が単独投与時の一過性の影響とアミノグリコシド併用時の障害の増強にとどまるため、その範囲で記載した。聴器毒性の頻度の見積もりは研究間で差が大きいため、本カードには数値を含めていない。
  curriculum:
    kokushi: 医学各論 Ⅲ-8-A-②（薬剤性難聴、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-503 (id: JlvnmPI)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OT-048
  domain: OT
  subdomain: 老人性難聴
  assertion:
    plain_statement_ja: 補聴器は、軽度から中等度の難聴に対する主たる臨床的介入であり、聞こえの困難を訴える成人への第一選択の管理として広く提供されている。Cochrane系統的レビューの2026年改訂版では、ランダム化比較試験16件（参加者2,261人、各研究の参加者の平均年齢58〜83歳）を統合し、補聴器の使用によって、日常生活への参加に関する聴覚特異的な健康関連QOLが大きく改善し（標準化平均差 −1.25、95%信頼区間 −1.63〜−0.87。8件、1,683人。エビデンスの確実性は中等度）、聞き取り能力も大きく改善した（標準化平均差 −1.28。5件、622人。中等度）。全般的な健康関連QOLへの効果は小さく、孤独感と作業記憶については効果が示されなかった。
    condition:
      region: 国際
      対象: 軽度から中等度の難聴のある成人（加齢性難聴を含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4625
    source: Ferguson MA, Sarant JZ, Bennett RJ, McIlhiney P, Badcock N, Bothe E. Hearing aids for mild to moderate hearing loss in adults. Cochrane Database Syst Rev. 2026;8(8):CD012023
    doi: 10.1002/14651858.CD012023.pub3
    pmid: '42644645'
    pmcid: PMC13509011
    url: https://doi.org/10.1002/14651858.CD012023.pub3
    source_license: CC BY-NC-ND 4.0（PMC掲載ページで表示を確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典の系統的レビューは加齢性難聴に限定したものではなく、軽度から中等度の難聴のある成人一般を対象とするが、含まれる研究の参加者は平均年齢58〜83歳で高齢者が中心である。本カードでは、当初候補だった2017年版（CD012023.pub2）ではなく、PMCで更新表示を確認した2026年改訂版（CD012023.pub3）を採用し、数値は改訂版の抄録で照合した。補聴器は薬剤ではなく管理医療機器であり、本カードには薬剤名を含めていない。国内では補聴器の購入は健康保険の給付対象ではなく、障害者総合支援法に基づく補装具費の支給は、身体障害者手帳の対象となる聴覚障害の場合などに限られる。
  curriculum:
    kokushi: 医学各論 Ⅲ-8-A-③（老人性難聴、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-503 (id: JlvnmPI)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OT-049
  domain: OT
  subdomain: 前庭神経炎
  assertion:
    plain_statement_ja: 前庭神経炎は、末梢性のめまい疾患の中で良性発作性頭位めまい症とメニエール病に次いで頻度が高く、24時間以上続く突然の回転性めまいを特徴とし、難聴や耳鳴などの蝸牛症状や、その他の神経症状を伴わない。めまいは数時間をかけて増強して初日にピークに達し、悪心・嘔吐を伴うが、通常は1〜3日で大きく軽快する。障害側と反対向きの水平・回旋混合性の自発眼振がみられ、頭部インパルス試験では障害側への頭部回転で修正サッケードが現れる。診断の補助には、頭部インパルス試験のほか温度眼振検査や前庭誘発筋電位（VEMP）が用いられる。治療は対症療法が中心で、急性期には前庭抑制薬と制吐薬を用い、摂食が困難な場合には輸液などの支持療法を行う。前庭抑制薬の長期使用は中枢代償を遅らせるため急性期の使用にとどめ、回復に向けて前庭リハビリテーションによる代償の促進も行われる。
    condition:
      region: 全般
      対象: 前庭神経炎の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4626
    source: 'Bae CH, Na HG, Choi YS. Current diagnosis and treatment of vestibular neuritis: a narrative review. Yeungnam Univ J Med. 2022;39(2):81-88'
    doi: 10.12701/yujm.2021.01228
    pmid: '34411472'
    pmcid: PMC8913909
    url: https://doi.org/10.12701/yujm.2021.01228
    source_license: CC BY-NC 4.0（PMC掲載ページで表示を確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ステロイド治療の効果については既存カードOT-032（ステロイド治療のメタ解析）が扱っているため、本カードでは触れていない。出典の総説が前庭抑制薬の代表例として挙げる薬剤のうち、ジメンヒドリナートには国内で動揺病やメニエール症候群などに伴う悪心・嘔吐・眩暈への効能で承認された医療用製剤（ドラマミン錠）があり、メクリジン塩酸塩は国内の一般用乗り物酔い薬の配合成分として用いられている。ただし、いずれも前庭神経炎自体を効能・効果とするものではなく、本カードでの記載は急性期の対症療法としての位置づけである。
  curriculum:
    kokushi: 医学各論 Ⅲ-8-B-③（前庭神経炎、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-508 (id: JlvnmPs)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OT-050
  domain: OT
  subdomain: 動揺病
  assertion:
    plain_statement_ja: 動揺病の薬物療法では、抗コリン薬と抗ヒスタミン薬が最も有効な予防薬とされ、動揺への曝露前に投与して予防する使い方が中心である。抗コリン薬のスコポラミンは、ランダム化比較試験14件の系統的レビューでプラセボより予防効果に優れたが、抗ヒスタミン薬に対する優越性は示されなかった。剤形には経口剤のほか、耳介後部に貼付して長時間作用する経皮吸収型製剤がある。有効な抗ヒスタミン薬は、ジメンヒドリナート、メクリジン、プロメタジンなど第1世代のH1受容体拮抗薬であり、第2世代の抗ヒスタミン薬は有効でなかった。これらの薬剤では、眠気などの鎮静作用が使用上の制約になる。
    condition:
      region: 全般
      対象: 動揺病の予防・治療の対象者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1363
    source: 'Zhang LL, Wang JQ, Qi RR, Pan LL, Li M, Cai YL. Motion Sickness: Current Knowledge and Recent Advance. CNS Neurosci Ther. 2016;22(1):15-24'
    doi: 10.1111/cns.12468
    pmid: '26452639'
    pmcid: PMC6492910
    url: https://doi.org/10.1111/cns.12468
    source_license: © John Wiley & Sons（CC表示は Crossref・PMC で確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: スコポラミン貼付剤（経皮吸収型製剤）は国内では未承認で市販されていない（国内の文献とPMDAの公開情報で確認）。国内のスコポラミンは、臭化水素酸塩水和物として一部の一般用乗り物酔い薬の配合成分や、注射剤の形で用いられている。ジメンヒドリナートには、動揺病などに伴う悪心・嘔吐・眩暈への効能で国内承認された医療用製剤（ドラマミン錠50mg）があり、メクリジン塩酸塩は国内の一般用乗り物酔い薬の配合成分として用いられ、プロメタジン塩酸塩（ヒベルナ）は効能・効果に動揺病を含む国内承認薬である。スコポラミン貼付剤の効果持続時間（72時間）は、出典の薬剤表から読み取った数値である。
  curriculum:
    kokushi: 医学各論 Ⅲ-8-B-⑤（動揺病、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-505 (id: JlvnmPc)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OT-051
  domain: OT
  subdomain: Horner症候群
  assertion:
    plain_statement_ja: Horner症候群の原因は、眼交感神経路の障害部位によって異なる。1次ニューロン（中枢性）の障害では視床下部・脳幹・頸髄の病変が原因となり、延髄外側梗塞（Wallenberg症候群）、脳幹や脊髄の腫瘍・脱髄・梗塞などが含まれる。2次ニューロン（節前性）の障害では肺尖部腫瘍が代表的で、非小細胞肺癌によるPancoast症候群を呈することがあり、そのほか外傷や、肺・縦隔の手術などによる医原性の交感神経幹の損傷も原因となる。3次ニューロン（節後性）の障害では内頸動脈解離が代表的で、頭頸部痛を伴い、顔面の発汗を担う線維が温存されるため無汗症を欠くことが多い。そのほか、内頸動脈の動脈瘤などの血管病変、海綿静脈洞病変、群発頭痛なども原因となる。
    condition:
      region: 全般
      対象: Horner症候群の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1366
    source: 'Kanagalingam S, Miller NR. Horner syndrome: clinical perspectives. Eye Brain. 2015;7:35-46'
    doi: 10.2147/EB.S63633
    pmid: '28539793'
    pmcid: PMC5398733
    url: https://doi.org/10.2147/EB.S63633
    source_license: CC BY-NC 3.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 部位別の原因は、出典（総説）の局在診断に関する各項（1次・2次・3次ニューロンの障害）の本文を直接照合して記載した。原因が同定された症例集積における部位別の割合などの数値は、本カードには含めていない。本カードには薬剤名を含めていない（薬理学的検査に用いる点眼薬の詳細は既存カードOT-038の扱う範囲に関連する）。
  curriculum:
    kokushi: 医学各論 Ⅲ-8-C-③（Horner症候群、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: NL-023
  domain: NL
  subdomain: 鼻せつ
  assertion:
    plain_statement_ja: 鼻せつ（鼻前庭せつ）は、鼻前庭の皮膚の毛包に生じる急性の限局性感染症で、原因菌は黄色ブドウ球菌が多い。主な臨床像は、鼻尖の発赤、腫脹、圧痛である。治療は温罨法などの保存的対応が基本で、ムピロシンの鼻腔内への外用が頻用され、症例によって経口抗菌薬が併用され、多くは7日以内に軽快する。合併症はまれだが、膿瘍の形成のほか、眼静脈血栓症、海綿静脈洞血栓症、眼窩膿瘍といった重篤な合併症が起こりうるため、注意を要する。
    condition:
      region: 全般
      対象: 鼻せつ（鼻前庭せつ）の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4627
    source: 'Sheik-Ali S, Sheik-Ali S, Sheik-Ali A. Nasal vestibular furunculosis: Summarised case series. World J Otorhinolaryngol Head Neck Surg. 2022;8(3):217-223'
    doi: 10.1016/j.wjorl.2020.12.003
    pmid: '36159901'
    pmcid: PMC9479471
    url: https://doi.org/10.1016/j.wjorl.2020.12.003
    source_license: CC BY-NC-ND 4.0（PMC掲載ページで表示を確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は症例集積と文献レビューをまとめた総説であり、鼻せつを対象としたランダム化比較試験は存在しないことが出典自体に明記されているため、本カードの主張は一般像と管理の原則の範囲にとどめた。顔面の静脈交通（いわゆる危険領域）を介する波及の機序は出典に明示されていないため、合併症は出典の列挙の範囲で記載した。ムピロシンの国内製剤は鼻腔用軟膏2%（バクトロバン鼻腔用軟膏）のみで、その承認効能は対象者を限定した鼻腔内のMRSAの除菌であり、皮膚用のムピロシン軟膏は国内で販売されていない。したがって、出典に記載された鼻せつの治療としてのムピロシン外用は、国内では承認効能とは目的の異なる使用にあたる。出典で一部の症例に併用されたフシジン酸ナトリウム経口剤については、国内の承認・販売の状況を本調査では確認できなかった。
  curriculum:
    kokushi: 医学各論 Ⅲ-9-A-①（鼻せつ、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-033
  domain: OR
  subdomain: 口角炎、舌炎
  assertion:
    plain_statement_ja: 舌炎のうち萎縮性舌炎は、舌背の糸状乳頭が部分性または完全に消失した状態で、舌が平滑にみえる。背景にはリボフラビン、ナイアシン、ピリドキシン、ビタミンB12、葉酸、鉄、亜鉛、ビタミンEなどの栄養素の欠乏があり、タンパク・カロリー栄養障害、口腔カンジダ症、ヘリコバクター・ピロリの定着、口腔乾燥症、糖尿病なども原因となりうる。萎縮性舌炎患者1,064例の検討では、貧血が19.0%、鉄欠乏が16.9%、ビタミンB12欠乏が5.3%、葉酸欠乏が2.3%、高ホモシステイン血症が11.9%にみられ、胃壁細胞抗体陽性は26.7%であった。欠乏している造血因子を補充すると一部の患者で口腔症状と萎縮性舌炎の完全寛解が得られるため、治療を始める前に血算、血清の造血因子、ホモシステイン、自己抗体を調べることが重要である。
    condition:
      region: 国際
      対象: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4628
    source: 'Chiang CP, Chang JYF, Wang YP, Wu YH, Wu YC, Sun A. Atrophic glossitis: Etiology, serum autoantibodies, anemia, hematinic deficiencies, hyperhomocysteinemia, and management. J Formos Med Assoc. 2020;119(4):774-780.'
    doi: 10.1016/j.jfma.2019.04.015
    pmid: '31076315'
    pmcid: null
    url: https://doi.org/10.1016/j.jfma.2019.04.015
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は台湾の研究グループによる萎縮性舌炎1,064例の集積に基づき、抄録で確認した範囲である。口角炎については OR-001 が担当する。欠乏の補充に用いるビタミンB12製剤、鉄剤、葉酸製剤はいずれも国内で欠乏症や貧血を適応として承認され保険適用されている。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-A-①（口角炎、舌炎、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-523 (id: JlvnmQ8)；TBL-01-00-525 (id: JlvnmRM)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-034
  domain: OR
  subdomain: アフタ性口内炎
  assertion:
    plain_statement_ja: 再発性アフタ性口内炎の治療は、潰瘍の症状の重症度、頻度、大きさ、個数に応じて選ぶ。偶発的な小さいアフタでは、保護性の軟膏や局所麻酔薬などの外用療法で症状が緩和されることが多い。より頻度が高い例や重症例では、外用グルココルチコイドが潰瘍の大きさと治癒期間を縮小させるのに有効で、病変の発生早期に使うと効果的である。大きく治癒の遅い大アフタでは、ステロイドの病変内注射が治癒期間の短縮に用いられることもある。外用療法のみでは新しい病変の形成は抑えられないため、大アフタや頻回に多発する例では全身療法を検討するが、全身性ステロイドの長期使用は重篤な副作用のためまれである。
    condition:
      region: 国際
      対象: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1432
    source: Akintoye SO, Greenberg MS. Recurrent aphthous stomatitis. Dent Clin North Am. 2014;58(2):281-297.
    doi: 10.1016/j.cden.2013.12.002
    pmid: '24655523'
    pmcid: PMC3964366
    url: https://doi.org/10.1016/j.cden.2013.12.002
    source_license: ライセンス未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典は米国の総説で、本文に挙がる外用薬の一部（アンレキサノクスなど）は国内では販売されていない。外用ステロイドについては、国内ではトリアムシノロンアセトニド口腔用軟膏やデキサメタゾン口腔用軟膏が、びらん・潰瘍を伴う難治性口内炎および舌炎などを適応として承認され保険適用されている。分類と治療目標は OR-002 が担当し、本カードは重症度に応じた治療の具体に絞った。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-A-②（アフタ性口内炎、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-524 (id: JlvnmRE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-035
  domain: OR
  subdomain: 急性ヘルペス性口内炎
  assertion:
    plain_statement_ja: 原発性ヘルペス性歯肉口内炎は、単純ヘルペスウイルス1型の初感染が症状を呈する病型で、初感染の13〜30%に生じ、発症のピークは6か月〜5歳の小児と若年成人にある。潜伏期2〜15日の後、発熱、倦怠感、食欲低下などの前駆症状が現れ、1〜3日後に歯肉、口唇粘膜、口蓋を中心に1〜2mmの小水疱が集簇して生じ、速やかに破れて黄灰色の偽膜を伴う痛みの強い不規則なびらん・潰瘍となる。歯肉の腫脹、口臭、よだれ、発熱を伴い、病変は瘢痕を残さず10〜14日で治癒する。口腔内の疼痛のため飲水・摂食が制限され、脱水のために入院を要することがある。治療は補液と疼痛管理などの支持療法が基本で、発症後72時間以内のアシクロビル経口投与が用いられるが、その有効性を支持するエビデンスは弱いとされる。
    condition:
      region: 国際
      対象: 系統的レビュー（小児・若年成人）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4629
    source: 'Coppola N, Cantile T, Adamo D, et al. Supportive care and antiviral treatments in primary herpetic gingivostomatitis: a systematic review. Clin Oral Investig. 2023;27(11):6333-6344.'
    doi: 10.1007/s00784-023-05250-5
    pmid: '37733027'
    pmcid: PMC10630243
    url: https://doi.org/10.1007/s00784-023-05250-5
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典の系統的レビューが対象とした研究は5件・364例で、アシクロビルに有効性（口腔病変の治癒の改善と症状期間の短縮）を示した研究は1件のみであり、そのエビデンスは弱いと評価されている。入院例における症状頻度は OR-003 が担当する。アシクロビルは国内で単純疱疹を効能・効果として承認され保険適用されており、本症はその一病型である。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-A-③（急性ヘルペス性口内炎、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-524 (id: JlvnmRE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-036
  domain: OR
  subdomain: ヘルパンギーナ
  assertion:
    plain_statement_ja: ヘルパンギーナは、発熱と口腔粘膜に現れる水疱性の発疹を特徴とする急性のウイルス性咽頭炎で、乳幼児を中心に夏季に流行する。原因の大多数はエンテロウイルス属のウイルスで、主としてコクサッキーウイルスA群である。2〜4日の潜伏期の後、突然の発熱に続いて咽頭痛が現れ、口腔内、主として軟口蓋から口蓋弓にかけて、直径1〜2mm（大きいものでは5mmほど）の紅暈で囲まれた小水疱が出現し、やがて破れて浅い潰瘍を形成して疼痛を伴う。発熱は2〜4日間程度で解熱し、粘膜疹もそれにやや遅れて消失するなど、ほとんどは予後良好である。口腔内の疼痛のため不機嫌、拒食、哺乳障害を来し、脱水症を呈することがある。特異的な治療法はなく通常は対症療法のみであり、ときに脱水に対する治療が必要になる。手足口病とは原因ウイルスが共通するが、手足口病ではヘルパンギーナよりも口腔内の前方に水疱疹がみられ、手や足にも水疱疹がある点が異なる。
    condition:
      region: 日本
      対象: 乳幼児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4630
    source: 国立健康危機管理研究機構 感染症情報提供サイト「ヘルパンギーナ」（2014年7月23日改訂）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niid.go.jp/niid/ja/kansennohanashi/515-herpangina.html
    source_license: 政府機関の公開ページ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 年齢分布については、国内では患者の5歳以下が全体の90%以上を占め、1歳代が最も多いと同出典に記載されている。発熱や頭痛に対してアセトアミノフェンを用いることもあるとされ、アセトアミノフェンは国内で解熱・鎮痛を適応として承認され保険適用されている。中国の単一の集団発生の内訳は OR-004 が担当する。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-A-④（ヘルパンギーナ、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-037
  domain: OR
  subdomain: 顎関節症
  assertion:
    plain_statement_ja: 顎関節症は、顎関節複合体とその周囲の筋・骨に及ぶ筋骨格系・神経筋系の状態の総称で、成人の最大15%にみられ、発症のピークは20〜40歳である。関節内（関節内部の異常）と関節外（周囲の筋の異常）に分類される。主な症状は顎の痛みや機能障害、耳痛、頭痛、顔面痛で、診察では咀嚼筋の圧痛、開口制限、関節音（クリックやクレピタス）がみられることがある（開口量30〜35mm未満は異常とされる）。診断は主として病歴と身体診察に基づき、咬合異常や関節内異常が疑われる場合に画像検査が有用となる。多くの患者は、患者教育、セルフケア、認知行動療法、薬物療法、理学療法、咬合装置などの非侵襲的治療の組み合わせで改善する。薬物療法では非ステロイド性抗炎症薬が初期に推奨され、筋の攣縮があれば筋弛緩薬の追加が推奨される。保存的治療が無効な例や顎の機能制限・持続する痛みがある例では、口腔顎顔面外科への紹介が適応となる。
    condition:
      region: 国際
      対象: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4631
    source: Gauer RL, Semidey MJ. Diagnosis and Treatment of Temporomandibular Disorders. Am Fam Physician. 2015;91(6):378-386.
    doi: null
    pmid: '25822556'
    pmcid: null
    url: https://www.aafp.org/dam/brand/aafp/pubs/afp/issues/2015/0315/p378.pdf
    source_license: CC表示なし（© American Academy of Family Physicians）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は米国の総説（2015年）で、主張は抄録と本文の診察所見・推奨要約で確認した範囲である。診断基準 DC/TMD の性能は OR-010 が担当する。非ステロイド性抗炎症薬と筋弛緩薬はいずれも国内で承認され保険適用されている薬剤のクラスだが、顎関節症は各製剤の添付文書の効能・効果に明記されておらず、国内ではこの病名では適応外の位置づけで用いられることがある。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-B-①（顎関節症、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-529 (id: JlvnmR8)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-038
  domain: OR
  subdomain: 咽頭炎
  assertion:
    plain_statement_ja: A群溶連菌性咽頭炎の診断では、臨床所見と疫学的特徴を組み合わせた臨床スコア（Centor基準など）が、溶連菌感染の可能性を予測するのに有用であり、可能性がきわめて低い患者では咽頭培養や迅速抗原検査が通常不要となる。一方で、臨床医は溶連菌が原因である確率を大きく過大評価する傾向があり、正確な診断には検査による確認が不可欠である。鼻汁、咳、口腔内潰瘍、嗄声などウイルス性を強く示唆する特徴がある患者には、通常、溶連菌の検査は推奨されない。抗菌薬は検査で確認されたA群溶連菌性咽頭炎に投与し、ペニシリンアレルギーのない患者ではペニシリンまたはアモキシシリンが第一選択で、投与期間は通常10日間である。この自然に軽快する疾患への治療の主な根拠は化膿性・非化膿性の合併症の予防であり、発症から9日以内に治療を始めれば急性リウマチ熱を予防できるが、溶連菌感染後糸球体腎炎の発症は治療によって防げない。
    condition:
      region: 国際
      対象: IDSAガイドライン2012年版
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1439
    source: 'Shulman ST, Bisno AL, Clegg HW, et al. Clinical practice guideline for the diagnosis and management of group A streptococcal pharyngitis: 2012 update by the Infectious Diseases Society of America. Clin Infect Dis. 2012;55(10):e86-e102.'
    doi: 10.1093/cid/cis629
    pmid: '22965026'
    pmcid: PMC7108032
    url: https://doi.org/10.1093/cid/cis629
    source_license: CCライセンス表示なし（学会ガイドライン）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドライン本文では臨床スコアは総称として論じられており、Centor基準（1981年）はその参考文献の一つであるため、主張では「Centor基準など」とした。A群溶連菌の占める割合と検査で確認する方針は OR-012 が担当する。ペニシリンとアモキシシリンはいずれも国内で承認され保険適用されており、溶連菌感染症は適応に含まれる。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-C-①（咽頭炎、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-513 (id: JlvnmQU)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-039
  domain: OR
  subdomain: 口蓋扁桃肥大症、咽頭扁桃増殖症
  assertion:
    plain_statement_ja: 小児の閉塞性睡眠呼吸障害は、睡眠中の上気道機能障害の症候群で、いびきや呼吸努力の増大を特徴とする。上気道閉塞に関連する症状として、頻回の大きな音のいびき、目撃される無呼吸、不穏な睡眠、口呼吸が挙げられる。口蓋扁桃肥大と咽頭扁桃（アデノイド）増殖は、その素因となる主な異常の一つである。治療は、素因となるすべての異常に対処する段階的な方法で行い、各介入の後に残存する病変を再評価する。閉塞性睡眠時無呼吸症候群がありアデノイド・扁桃肥大を伴う小児では、口蓋扁桃摘出術とアデノイド切除術の併施が適応となり、無呼吸低呼吸指数が5回/時を超える例で睡眠ポリグラフ所見の改善が最も得られやすく、もともと健康な非肥満の小児での成功率（無呼吸低呼吸指数1回/時未満）は約75%とされる。
    condition:
      region: 欧州
      対象: 2〜18歳の小児（ERSステートメント2016年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1440
    source: 'Kaditis AG, Alonso Alvarez ML, Boudewyns A, et al. Obstructive sleep disordered breathing in 2- to 18-year-old children: diagnosis and management. Eur Respir J. 2016;47(1):69-94.'
    doi: 10.1183/13993003.00385-2015
    pmid: '26541535'
    pmcid: null
    url: https://doi.org/10.1183/13993003.00385-2015
    source_license: CCライセンス表示なし（学会ステートメント）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 記載はERSステートメント（2016年）本文のステップ1（上気道閉塞に関連する症状）とステップ6（アデノトンシレクトミーの適応）の要約に基づく。重症度の客観的評価と段階的治療の総論は OR-013 が担当する。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-C-②（口蓋扁桃肥大症、咽頭扁桃<アデノイド>増殖症、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-520 (id: JlvnmSo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-040
  domain: OR
  subdomain: 急性扁桃炎
  assertion:
    plain_statement_ja: A群溶連菌による咽頭・扁桃炎は主に5〜15歳にみられ、突然発症の咽頭痛、嚥下時痛、発熱を呈し、扁桃・咽頭の発赤や滲出物、圧痛を伴う前頸部リンパ節腫脹がみられる。小児では頭痛、悪心・嘔吐、腹痛を伴うこともある。咳嗽、鼻汁、嗄声、結膜炎などの所見が目立つ場合はウイルス性が示唆される。臨床所見だけでは両者を確実に鑑別できないため、咽頭拭い液による迅速抗原検査や培養で診断を確認することが推奨される。合併症には、扁桃周囲膿瘍、頸部リンパ節炎、乳様突起炎などの化膿性合併症と、急性リウマチ熱、溶連菌感染後糸球体腎炎などの非化膿性合併症がある。
    condition:
      region: 国際
      対象: IDSAガイドライン2012年版
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1439
    source: 'Shulman ST, Bisno AL, Clegg HW, et al. Clinical practice guideline for the diagnosis and management of group A streptococcal pharyngitis: 2012 update by the Infectious Diseases Society of America. Clin Infect Dis. 2012;55(10):e86-e102.'
    doi: 10.1093/cid/cis629
    pmid: '22965026'
    pmcid: PMC7108032
    url: https://doi.org/10.1093/cid/cis629
    source_license: CCライセンス表示なし（学会ガイドライン）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 記載は2012年版ガイドライン本文で確認した範囲（臨床像は同ガイドラインの特徴の表、合併症は序文と推奨の根拠の節）。同ガイドラインでは咽頭炎と扁桃炎は一体として扱われる。治療薬は OR-014 が担うため本カードには薬剤名を含めていない。PMCID は PMC 本文で確認した（出典マスターでは null のため補完候補）。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-C-③（急性扁桃炎、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-517 (id: JlvnmQM)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-041
  domain: OR
  subdomain: 扁桃周囲炎・膿瘍
  assertion:
    plain_statement_ja: 扁桃周囲膿瘍は頭頸部の深部感染症の中で最も頻度が高く、主に若年成人に生じ、米国での発症率は人口10万人あたり年約30人とされる。多くは複合菌感染であり、A群溶連菌と口腔内の嫌気性菌が関与する。発熱、強い咽頭痛、嚥下障害、開口障害、含み声（hot potato voice）がみられ、患側の軟口蓋の腫脹・発赤と、口蓋垂の対側への偏位が特徴的である。診断は主として臨床所見と診察による。治療の柱は膿瘍のドレナージ、抗菌薬療法、輸液と疼痛管理などの支持療法であり、ドレナージの方法（穿刺吸引、切開排膿、即時扁桃摘出）はいずれも有効で、患者転帰に有意差はなかったとされる。即時扁桃摘出は、反復性扁桃炎の既往がある例や、局所麻酔下のドレナージ手技に耐えにくい小児などで考慮される。認識と治療の開始が遅れると、気道閉塞や深頸部組織への感染の進展などの重篤な合併症を来しうる。
    condition:
      region: 米国
      対象: 総説（扁桃周囲膿瘍）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4632
    source: Galioto NJ. Peritonsillar Abscess. Am Fam Physician. 2017;95(8):501-506.
    doi: null
    pmid: '28409615'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/28409615/
    source_license: © 2017 American Academy of Family Physicians（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 発症率（10万人あたり年約30人）と年齢分布は米国の総説本文の記載に基づく。症状・所見とドレナージ法の比較は同総説の本文と表で確認した。本文から読み取りに相当する数値を含む。薬剤については、A群溶連菌と口腔嫌気性菌に有効な抗菌薬が第一選択である旨と副腎皮質ステロイド併用の可能性が同総説に記載されているが、本カードでは個別の薬剤名・用量を含めていないため、個別薬剤の国内承認・保険適用の確認は行っていない。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-C-④（扁桃周囲炎・膿瘍、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-518 (id: JlvnmQk)；TBL-01-00-519 (id: JlvnmQs)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-042
  domain: OR
  subdomain: 頸部リンパ節炎
  assertion:
    plain_statement_ja: 小児の頸部リンパ節腫脹の原因は多岐にわたる。ウイルス感染が最も頻度が高く、両側性に腫脹することが多い。急性の細菌性リンパ節炎では黄色ブドウ球菌とA群溶連菌が40〜80%を占め、片側性の有痛性腫脹を呈することが多い。慢性の経過をとる細菌性リンパ節炎では非結核性抗酸菌が主な原因で、次いで猫ひっかき病の原因菌（Bartonella）、結核菌、ブルセラなどが挙がる。川崎病では、前頸部の急性で非化膿性、比較的無痛性のリンパ節腫脹がみられる。悪性腫瘍を示唆する所見は、2〜2.5cmを超える大きさ、硬い性状、鎖骨上窩の部位、圧痛がないこと、可動性が低いこと、進行性の経過、B症状である。診断は病歴と診察を基礎とし、超音波検査が鑑別の中心的な画像検査であり、悪性が疑われる場合は穿刺吸引細胞診よりもリンパ節全体の摘出による組織診断が優先される。
    condition:
      region: 国際
      対象: 小児（総説）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4633
    source: Lang S, Kansy B. Cervical lymph node diseases in children. GMS Curr Top Otorhinolaryngol Head Neck Surg. 2014;13:Doc08.
    doi: 10.3205/cto000111
    pmid: '25587368'
    pmcid: PMC4273169
    url: https://doi.org/10.3205/cto000111
    source_license: CC BY-NC-ND 3.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は小児を対象とするドイツの総説であり、原因の頻度構成は小児のもので、成人では異なる。割合（40〜80%）と大きさの基準（2〜2.5cm）は出典本文から読み取った値である。薬剤名は含めていない。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-E-①（頸部リンパ節炎、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-530 (id: JlvnmS4)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-043
  domain: OR
  subdomain: 頸部膿瘍
  assertion:
    plain_statement_ja: 深頸部感染症（頸部膿瘍を含む）は頸部の筋膜間隙に生じる化膿性感染症で、内科・外科の緊急事態である。原因は歯原性と扁桃原性が最も多く、起因菌は好気性菌と嫌気性菌の複合感染が多い。主な症状は嚥下痛、嚥下障害、開口障害、よだれであり、発熱、頸部の腫脹・発赤、頸部硬直が持続的な所見となる。感染は下方へ進展して降下性壊死性縦隔炎を来し、予後不良となりうる。その他の合併症には、内頸静脈血栓症、気道閉塞、急性呼吸促迫症候群、敗血症、播種性血管内凝固がある。CTは病変の性状と関与する間隙の同定に有用で診断の中心とされ、初期評価では気道の評価が優先される。治療は、頸部間隙の開放ドレナージと壊死組織のデブリードマン、好気性菌と嫌気性菌をカバーする経験的抗菌薬療法を組み合わせ、集学的チームで対応する。
    condition:
      region: 国際
      対象: 深頸部感染症（スコーピングレビュー、2025年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4634
    source: 'Cobzeanu BM, Moisii L, Palade OD, et al. Management of Deep Neck Infection Associated with Descending Necrotizing Mediastinitis: A Scoping Review. Medicina (Kaunas). 2025;61(2):325.'
    doi: 10.3390/medicina61020325
    pmid: '40005441'
    pmcid: PMC11857515
    url: https://doi.org/10.3390/medicina61020325
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典は降下性壊死性縦隔炎を伴う深頸部感染症に焦点を当てたスコーピングレビューであり、縦隔炎を伴わない頸部膿瘍一般の経過とは重症度が異なる場合がある。薬剤名は含めていない（抗菌薬は対象菌の範囲の水準で記載し、国内で承認された抗菌薬製剤を用いる）。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-E-②（頸部膿瘍、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-531 (id: JlvnmTA)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: OR-044
  domain: OR
  subdomain: リンパ節転移
  assertion:
    plain_statement_ja: 成人の頸部腫瘤は、他の原因が証明されるまでは悪性と考えるべきであり、無症候の頸部腫瘤が頭頸部癌の初発の、または唯一の所見であることがある。悪性のリスクが高いと判断する手がかりは、感染性の病歴がなく2週間以上持続する腫瘤（または期間が不明な腫瘤）と、周囲組織への固定、硬い性状、1.5cmを超える大きさ、被覆皮膚の潰瘍といった診察所見である。リスクが高い例では、造影CT（またはMRI）を頭蓋底から胸郭入口部まで撮影し、診断がなお不明な場合は開創生検ではなく穿刺吸引細胞診（FNA）を行う。FNAの正確度は頸部腫瘤全体で93.1%、リンパ節では感度92.5%と報告される。頸部リンパ節のレベル分類は、診察と画像で転移の分布を記載する枠組みとして用いられる。嚢胞性の腫瘤であっても良性と決めつけず、診断が確定するまで評価を続ける。
    condition:
      region: 米国
      対象: 成人（診療ガイドライン）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1210
    source: 'Pynnonen MA, Gillespie MB, Roman B, Rosenfeld RM, et al. Clinical Practice Guideline: Evaluation of the Neck Mass in Adults. Otolaryngol Head Neck Surg. 2017;157(2_suppl):S1-S30.'
    doi: 10.1177/0194599817722550
    pmid: '28891406'
    pmcid: null
    url: https://doi.org/10.1177/0194599817722550
    source_license: © American Academy of Otolaryngology-Head and Neck Surgery Foundation（SAGE、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 正確度・感度と大きさの基準（1.5cm）はガイドライン本文から読み取った値である。レベル分類の各レベルの境界の定義は同ガイドラインの図（Figure 7）に示されるが、図の細部は本文で確認できないため主張には含めていない。本出典は既存マスターに SRC-1210 として登録済みであり、本カードはその再利用である。対象は成人で、小児の頸部腫瘤には適用されない。薬剤名は含めていない。
  curriculum:
    kokushi: 医学各論 Ⅲ-10-E-③（リンパ節転移、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-527 (id: JlvnmTI)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: TR-029
  domain: TR
  subdomain: 凍傷・凍瘡
  assertion:
    plain_statement_ja: 凍傷は組織の凍結による損傷であり、重症度は伝統的に4段階に分類される。1度はしびれと発赤を生じ、白または黄色の硬くわずかに隆起した局面ができ、組織の死は生じない。2度は透明または乳白色の液体を含む表在性の水疱で、発赤と炎症を伴う。3度は血疱（出血性の水疱）で、損傷が真皮の深層まで及んだことを示す。4度は皮膚の全層を超えて脂肪、筋、腱、骨などの深部組織に及ぶ。現場での分類としては、再加温の後、画像評価の前に、組織喪失が皆無か最小限にとどまる「表在性」（1〜2度に相当）と、組織喪失が見込まれる「深部」（3〜4度に相当）の2つに分ける方法が推奨される。なお、凍結を伴わない表在性の寒冷損傷である frostnip は凍傷とは区別される。
    condition:
      region: 米国
      対象: 凍傷（診療ガイドライン2024年改訂版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1456
    source: 'McIntosh SE, Freer L, Grissom CK, Rodway GW, et al. Wilderness Medical Society Clinical Practice Guidelines for the Prevention and Treatment of Frostbite: 2024 Update. Wilderness & Environmental Medicine. 2024;35(2):183-197.'
    doi: 10.1177/10806032231222359
    pmid: '38577729'
    pmcid: null
    url: https://doi.org/10.1177/10806032231222359
    source_license: ライセンス表示を確認できず（学会ガイドライン、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 分類の記載は WMS ガイドライン2024年改訂版の公式要約で確認した（分類の読み取りに相当）。深さと予後の対応は、現場向け2分類の定義（組織喪失の見込みの有無）に基づく。凍瘡（しもやけ）そのものの臨床像は同ガイドラインの主対象ではなく、本カードでは扱っていない。薬剤名は含めていない（治療は TR-003 が担う）。
  curriculum:
    kokushi: 医学各論 Ⅲ-11-A-②（凍傷・凍瘡、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: TR-030
  domain: TR
  subdomain: 電撃傷
  assertion:
    plain_statement_ja: 電撃傷の重症度は、電圧、電流の種類、接触時間、体内での電流の経路によって決まる。低電圧損傷は1000V未満、高電圧損傷は1000V超の曝露と定義される。交流は強直性の筋収縮を引き起こして接触時間を延ばすため、より危険である。電流は神経、筋、血管など伝導性の高い組織を通って流れ、縦方向の経路では脳、心臓、肺、呼吸筋が巻き込まれて広範な損傷となりうる。不整脈の多くは受傷後数時間以内に生じ、心室細動、心室頻拍、心静止も報告される。初期評価では全例で心電図を記録し、心電図の異常、意識消失、心疾患の既往、高電圧または落雷による受傷がある例では少なくとも24時間のモニタリングを行う。一方、心疾患がなく、意識消失がなく、来院時の心電図が正常な低電圧損傷では、入院での心臓モニタリングは不要とされる。深部の筋損傷は皮膚所見を大きく上回ることがあり、筋細胞の融解によってクレアチンキナーゼとミオグロビンが放出され、横紋筋融解症、急性腎障害、コンパートメント症候群を来す。血清クレアチンキナーゼは来院時に測定して経過を追い、四肢の診察は最初の24〜48時間は1〜2時間ごとに行い、適応があれば筋膜切開を行う。
    condition:
      region: 米国
      対象: 成人（救急部門向け総説、2026年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4635
    source: Smith I, Kidd S, Kim S, Tennill RM. Assessment and Management of Electrical Injuries in Adults in the Emergency Department. Cureus. 2026;18(4):e107162.
    doi: 10.7759/cureus.107162
    pmid: null
    pmcid: null
    url: https://doi.org/10.7759/cureus.107162
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 2026年刊行の総説であり、PMID は確認できなかったため null とし、DOI と出版社 PDF 本文で文献を特定した。電圧の境界（1000V）、モニタリングの時間（24時間）、四肢診察の間隔（1〜2時間）は出典本文から読み取った値である。対象は成人であり、小児の電撃傷への適用は出典の範囲外。薬剤名は含めていない。
  curriculum:
    kokushi: 医学各論 Ⅲ-11-A-③（電撃傷、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: TR-031
  domain: TR
  subdomain: 角・結膜化学損傷
  assertion:
    plain_statement_ja: 眼の化学損傷の重症度分類として Roper-Hall 分類が広く用いられ、角膜の混濁の程度と角膜輪部の虚血の範囲によって4つのグレードに分ける。グレードIは角膜上皮の障害のみで輪部虚血がなく予後は良好、グレードIIは角膜に混濁があっても虹彩の詳細が見え、輪部虚血が3分の1未満で予後は良好、グレードIIIは上皮の全欠損と実質の混濁で虹彩の詳細が見えず、輪部虚血が3分の1から2分の1で予後は要注意、グレードIVは角膜が不透明で虹彩と瞳孔が見えず、輪部虚血が2分の1を超え予後は不良である。急性期治療で最も重要な介入は即時の洗浄であり、等張食塩水または乳酸リンゲル液を用い、pHが生理的な範囲に中和されるまで続け、少なくとも1Lの液量と30分以上の洗浄が推奨される。洗浄液の選択のために洗浄の開始を遅らせてはならず、入手できなければ水道水でもよい。円蓋部に残った固形の異物は除去し、上眼瞼を二重に翻転して残留物を確認する。洗浄後も最大で1時間はpHを繰り返し確認する。
    condition:
      region: 国際
      対象: 総説（眼化学外傷）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1459
    source: Bizrah M, Yusuf A, Ahmad S. An update on chemical eye burns. Eye (London). 2019;33(9):1362-1377.
    doi: 10.1038/s41433-019-0456-5
    pmid: '31086244'
    pmcid: PMC7002428
    url: https://doi.org/10.1038/s41433-019-0456-5
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: Roper-Hall 分類は出典の表（Table 1）から読み取ったものである。洗浄の液量・時間と pH 確認の進め方は同総説の洗浄療法の節の記載に基づく（本文から読み取り）。Dua 分類も臨床で用いられるが、本カードでは Roper-Hall 分類に絞った。PMCID は PMC 本文で確認した（出典マスターでは null のため補完候補）。薬剤名は含めていない。
  curriculum:
    kokushi: 医学各論 Ⅲ-11-A-⑤（角・結膜化学損傷、a）
    core_curriculum: 'PS-02-15-05 (id: JkxnuTU)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
```


## 3. カリキュラム対応表

| カード | subdomain | kokushi | コアカリ |
|---|---|---|---|
| EY-060 | 調節異常 | 医学各論 Ⅲ-4-A-③（調節異常、a） | PS-02-15-05 (id: JkxnuTU)；TBL-01-00-489 (id: JlvnmNk) |
| EY-061 | うっ血乳頭 | 医学各論 Ⅲ-4-B-①（うっ血乳頭、a） | PS-02-15-05 (id: JkxnuTU)；TBL-01-00-495 (id: JlvnmOc) |
| RE-031 | Behçet病 | 医学各論 Ⅲ-6-A-①（Behçet病、a） | PS-02-15-05 (id: JkxnuTU)；TBL-01-00-496 (id: JlvnmOY) |
| OT-045 | 外耳道異物 | 医学各論 Ⅲ-7-A-①（外耳道異物、a） | PS-02-16-05 (id: JkxnuTo) |
| OT-046 | 滲出性中耳炎 | 医学各論 Ⅲ-7-C-②（滲出性中耳炎、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-501 (id: JlvnmO0) |
| OT-047 | 薬剤性難聴 | 医学各論 Ⅲ-8-A-②（薬剤性難聴、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-503 (id: JlvnmPI) |
| OT-048 | 老人性難聴 | 医学各論 Ⅲ-8-A-③（老人性難聴、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-503 (id: JlvnmPI) |
| OT-049 | 前庭神経炎 | 医学各論 Ⅲ-8-B-③（前庭神経炎、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-508 (id: JlvnmPs) |
| OT-050 | 動揺病 | 医学各論 Ⅲ-8-B-⑤（動揺病、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-505 (id: JlvnmPc) |
| OT-051 | Horner症候群 | 医学各論 Ⅲ-8-C-③（Horner症候群、a） | PS-02-16-05 (id: JkxnuTo) |
| NL-023 | 鼻せつ | 医学各論 Ⅲ-9-A-①（鼻せつ、a） | PS-02-16-05 (id: JkxnuTo) |
| OR-033 | 口角炎、舌炎 | 医学各論 Ⅲ-10-A-①（口角炎、舌炎、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-523 (id: JlvnmQ8)；TBL-01-00-525 (id: JlvnmRM) |
| OR-034 | アフタ性口内炎 | 医学各論 Ⅲ-10-A-②（アフタ性口内炎、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-524 (id: JlvnmRE) |
| OR-035 | 急性ヘルペス性口内炎 | 医学各論 Ⅲ-10-A-③（急性ヘルペス性口内炎、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-524 (id: JlvnmRE) |
| OR-036 | ヘルパンギーナ | 医学各論 Ⅲ-10-A-④（ヘルパンギーナ、a） | PS-02-16-05 (id: JkxnuTo) |
| OR-037 | 顎関節症 | 医学各論 Ⅲ-10-B-①（顎関節症、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-529 (id: JlvnmR8) |
| OR-038 | 咽頭炎 | 医学各論 Ⅲ-10-C-①（咽頭炎、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-513 (id: JlvnmQU) |
| OR-039 | 口蓋扁桃肥大症、咽頭扁桃増殖症 | 医学各論 Ⅲ-10-C-②（口蓋扁桃肥大症、咽頭扁桃<アデノイド>増殖症、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-520 (id: JlvnmSo) |
| OR-040 | 急性扁桃炎 | 医学各論 Ⅲ-10-C-③（急性扁桃炎、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-517 (id: JlvnmQM) |
| OR-041 | 扁桃周囲炎・膿瘍 | 医学各論 Ⅲ-10-C-④（扁桃周囲炎・膿瘍、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-518 (id: JlvnmQk)；TBL-01-00-519 (id: JlvnmQs) |
| OR-042 | 頸部リンパ節炎 | 医学各論 Ⅲ-10-E-①（頸部リンパ節炎、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-530 (id: JlvnmS4) |
| OR-043 | 頸部膿瘍 | 医学各論 Ⅲ-10-E-②（頸部膿瘍、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-531 (id: JlvnmTA) |
| OR-044 | リンパ節転移 | 医学各論 Ⅲ-10-E-③（リンパ節転移、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-527 (id: JlvnmTI) |
| TR-029 | 凍傷・凍瘡 | 医学各論 Ⅲ-11-A-②（凍傷・凍瘡、a） | PS-02-16-05 (id: JkxnuTo) |
| TR-030 | 電撃傷 | 医学各論 Ⅲ-11-A-③（電撃傷、a） | PS-02-16-05 (id: JkxnuTo) |
| TR-031 | 角・結膜化学損傷 | 医学各論 Ⅲ-11-A-⑤（角・結膜化学損傷、a） | PS-02-15-05 (id: JkxnuTU) |

## 4. 未解決事項

- EY-060 の調節麻痺側は未カバー（一次資料級の総説が見つからず）。調節異常の追加候補として残す
- SRC-4622（EULAR 推奨2025年改訂版）のライセンス表示・PMCID は未確認で RESTRICTED の目安。取り込み側の Crossref 照合で確定されたい
- SRC-4624（Schacht 2012）のライセンスは PMC 掲載が著者原稿で CC 表示を確認できず UNKNOWN。取り込み側の照合で確定されたい
- SRC-4628（Chiang 2020）のライセンス（CC BY-NC-ND 4.0）は同誌論文の表示で確認したが、当該論文の出版社ページは直接開けなかった。取り込み側での最終確認を推奨する
- SRC-4623（Heim 2007）・SRC-4631（Gauer & Semidey 2015）・SRC-4632（Galioto 2017）は PubMed レコードに DOI がなく doi は null
- SRC-4635（Smith ら、Cureus 2026）は2026年刊行で PMID が確認できず null（DOI・出版社 PDF で特定済み）
- NL-023 で言及したフシジン酸ナトリウム経口剤の国内承認・販売状況は未確認
- PMCID 補完候補（本文で確認済み、マスターでは null。本カードには記入済み）：SRC-1363 → PMC6492910、SRC-1366 → PMC5398733、SRC-1439 → PMC7108032、SRC-1459 → PMC7002428
- 出典マスター側の重複の疑い：SRC-1277 と SRC-1366 は同一文献（Kanagalingam & Miller 2015、DOI・PMID ともに一致）。OT-051 は既存の OT-038 と同じ SRC-1366 にそろえた。マスター側の整理は取り込み側の判断
- 未使用の SRC 番号：SRC-4636〜4720（この回では使わない）

## 5. 引き継ぎメモ

- EY-061 の術式は出典の抄録の範囲（脳室腹腔シャントまで）で、視神経鞘開窓術等の位置づけは未記載
- OT-049（前庭神経炎）ではステロイドの効果を扱っていない（既存 OT-032 の担当範囲との重複回避）
- OT-050 は既存出典 SRC-1363 の本文に薬物療法の節と薬剤表があることを確認して再利用した（地ならしの代替候補 Brandt 2018 は未使用）
- OR-039 の subdomain は項目名そのまま（「口蓋扁桃肥大症、咽頭扁桃増殖症」）とした。既存 OR-013 の「扁桃・アデノイド」にそろえるかは取り込み側の判断
- OR-038 の Centor 基準は、ガイドライン本文では「臨床スコア」の総称で論じられ Centor 1981 は参考文献の一つであるため、主張は「Centor基準など」とし uncertainty に明記した
- OR-035 は当初候補（Kolokotronis 2006）の全文にアシクロビルの記載がなかったため系統的レビュー（SRC-4629）に切り替えた。OR-036 は入院調査では自然経過・対症療法が確認できず、感染症情報提供サイトの解説（SRC-4630、GOV_JP）に切り替えた
- OR-041 など OR の各カードは薬剤群の水準に留め、個別薬剤名は含めていない（OR-041 の uncertainty に明記）
- 薬剤名のあるカード（EY-061 のアセタゾラミド、RE-031 の抗TNFα抗体等、OT-047 の原因薬剤、OT-050 の動揺病薬、NL-023 のムピロシンなど）は、すべて uncertainty に薬剤名を特定した国内承認・保険適用の注記を入れた
