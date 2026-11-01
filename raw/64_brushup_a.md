# 第64回 成果物（ブラッシュアップA：腎・泌尿器・生殖器（Ⅷ）と性感染症（Ⅻ-2））

- 依頼文：docs/tasks/round62_BRUSHUP_A.md の「第64回」（仕様 specs/round64.yaml）
- 対象：22項目（すべてレベル a）
- 件数：22件（CM-007、BA-046、GN-041、UR-035〜043、GU-040〜043、KT-029〜030、KF-041、GY-063、RP-068〜069）。膀胱結石、尿道結石（Ⅷ-4-A-②）は出典が異なるため2件で担う。淋菌感染症（Ⅻ-2-B-⑥）と淋菌性尿道炎（Ⅷ-5-D-①）は登録時の決定どおり BA-046 の1枚に両方の番号を付けた
- 新規出典：13件（SRC-4721〜4733）。未使用：SRC-4734〜4800
- 既存カードは直さず、各項目に依頼文の表の「2件目に書く側面」の新しいカードを足した

## 経緯と判断（申し送り）

- **担当指示の作成ミスと是正**：作り手側の担当割り当てに、登録前の段階の項目リストに基づく食い違い（項目名・国試番号の取り違え）があった。各パートは登録済みの依頼文と仕様を正として作成し直したため、本編の内容はすべて登録対象どおりになっている。未割り当てだった4項目（包茎、精巣損傷、膀胱結石・尿道結石、性器ヘルペス）は補完パートで作成した
- **対象外の2件を分離**：亀頭包皮炎と精索静脈瘤のカードが担当指示の誤りで作られたが、この回の登録対象ではないため、本編には入れず別ファイル（64_extra_gu.md）に分離した。将来の回の候補として使える
- **GU の重複カードを本編から外した**：腎・尿路損傷について UR-039 と重なる内容のカードが GU 側でも作られたため、本編は UR-039 の1件とし、GU の番号は GU-040〜043 に詰め直した
- 性感染症診断・治療ガイドライン2026（日本性感染症学会）が現行版であることは確認したが本文を照合できなかったため、CM-007・BA-046 の出典には使っていない。差し替え候補として §4 に挙げた
- GN-041（蛋白尿）は KDIGO 2024 に「糸球体性・尿細管性・溢出性」の三分法とネフローゼ域の数値定義がないため、その部分は主張に入れていない（必要なら別出典での追加が要る）

## 1. 出典ホワイトリスト（この回のカードが使う出典）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-573 | Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int. 2024;105(4S):S117-S314 | 10.1016/j.kint.2023.10.018 | 38490803 | 出版社の著作物（CC の表示なし） | RESTRICTED | 既存出典（出典マスター登録済み。第64回で再利用） |
| SRC-665 | Trayes KP, Studdiford JS, Pickle S, Tully AS. Edema: diagnosis and management. Am Fam Physician. 2013;88(2):102-110 | なし | 23939641 | 出版社（米国家庭医学会）の著作物（CC の表示なし） | RESTRICTED | 既存出典（KX-001）。PubMed レコードで書誌・抄録を確認 |
| SRC-666 | Ostermann M, Joannidis M. Acute kidney injury 2016: diagnosis and diagnostic workup. Crit Care. 2016;20:299 | 10.1186/s13054-016-1478-z | 27670788 | CC BY 4.0（PMC ページの表示で確認） | OPEN | 既存出典（KX-002）。PMC 全文で尿沈渣・尿中電解質（FENa 等）の項を確認 |
| SRC-703 | Workowski KA, Bachmann LH, Chan PA, et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recomm Rep. 2021;70(4):1-187 | 10.15585/mmwr.rr7004a1 | 34292926 | 米国政府著作物（CDC） | GOV_US | 既存出典（UR-019・UR-020 で使用、マスター登録済み）。CDC 公式ページの本文で Urethritis・Nongonococcal Urethritis・Persistent or Recurrent Nongonococcal Urethritis の各節を確認 |
| SRC-718 | Coccolini F, Moore EE, Kluger Y, et al; WSES-AAST Expert Panel. Kidney and uro-trauma: WSES-AAST guidelines. World J Emerg Surg. 2019;14:54 | 10.1186/s13017-019-0274-x | 31827593 | CC BY（出版社ページの表示） | OPEN | 既存出典（UR-033）。PMC 全文で WSES 分類表と非手術的管理のステートメントを確認 |
| SRC-817 | Gordon CM, Ackerman KE, Berga SL, Kaplan JR, Mastorakos G, Misra M, Murad MH, Santoro NF, Warren MP. Functional Hypothalamic Amenorrhea: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2017;102(5):1413-1439 | 10.1210/jc.2017-00131 | 28368518 | Endocrine Societyのガイドライン。CC表示を確認できず | UNKNOWN | 既存出典（RP-019 で使用、マスター登録済み）。PubMed 抄録とガイドラインの推奨要約で、原因・骨密度評価・治療の推奨を確認 |
| SRC-4721 | 国立健康危機管理研究機構（JIHS）感染症情報提供サイト「性器クラミジア感染症（詳細版）」 | null | null | 政府機関の公開ページ | GOV_JP | 公式サイトの詳細版ページの本文を直接確認 |
| SRC-4722 | Hamasuna R, Yasuda M, Takahashi S, Uehara S, Kawai Y, Miyairi I, Arakawa S, Kiyota H; JAID/JSC Guide/Guidelines Committee. The JAID/JSC guidelines to Clinical Management of Infectious Disease 2017 concerning male urethritis and related disorders. J Infect Chemother. 2021;27(4):546-554 | 10.1016/j.jiac.2019.12.001 | 33516669 | CC BY-NC-ND 4.0（論文中の表示） | RESTRICTED | 日本語版全文（感染症学雑誌 2018;92(3)）と英語版論文を確認。PMID は文献データベースで DOI と照合 |
| SRC-4723 | European Association of Urology. EAU Guidelines on Paediatric Urology. EAU Guidelines Office, Arnhem, The Netherlands. 2026（第19章 Ureterocele and Ectopic Ureter） | null | null | EAU（欧州泌尿器科学会）の著作物（CC の表示なし） | RESTRICTED | ガイドライン公式サイトの第19章の本文を直接確認。版は同サイトの引用情報（EAU Annual Congress London 2026 提示版）による |
| SRC-4724 | National Institute for Health and Care Excellence. Urinary incontinence and pelvic organ prolapse in women: management. NICE guideline NG123. 2019 | なし | なし | © NICE（CC の表示なし） | RESTRICTED | 既存出典（出典マスター登録済み。第64回で再利用） |
| SRC-4725 | Türk C, Donaldson JF, Petřík A, et al. EAU Guidelines on Bladder Stones. European Association of Urology. 2021 (Limited update March 2021) | なし | なし | © European Association of Urology 2021（CC表示なし） | RESTRICTED | EAU 公式のガイドライン全文で分類・臨床像・画像診断の感度・原因評価・治療（溶解療法と除去術の選択）を確認。DOI・題名で出典マスターと照合し重複なし |
| SRC-4726 | Morton A, Tariq A, Dunglison N, Esler R, Roberts MJ. Etiology and management of urethral calculi: a systematic review of contemporary series. Asian J Urol. 2024;11(1):10-18 | 10.1016/j.ajur.2021.12.011 | 38312816 | CC BY-NC-ND 4.0（PMC 掲載ページの表示） | RESTRICTED | PMC 全文（PMC10837653）で抄録と Table 1 の数値（症状・検査・背景病変・治療の内訳）を確認。DOI・PMID で出典マスターと照合し重複なし |
| SRC-4727 | McGregor TB, Pike JG, Leonard MP. Pathologic and physiologic phimosis: approach to the phimotic foreskin. Can Fam Physician. 2007;53(3):445-448 | なし | 17872680 | © College of Family Physicians of Canada（CC表示なし） | RESTRICTED | PMC 全文（PMC1949079）で生理的・病的包茎の区別、年齢別の翻転不能の割合、ステロイド外用、嵌頓包茎の整復、環切除の適応を確認。DOI・PMID で出典マスターと照合し重複なし |
| SRC-4728 | Dagur G, Gandhi J, Suh Y, et al. Classifying Hydroceles of the Pelvis and Groin: An Overview of Etiology, Secondary Complications, Evaluation, and Management. Curr Urol. 2017;10(1):1-14 | 10.1159/000447145 | 28559772 | © S. Karger AG（CC の表示なし） | RESTRICTED | 既存出典（出典マスター登録済み。第64回で再利用） |
| SRC-4729 | Mellick LB, Sinex JE, Gibson RW, Mears K. A Systematic Review of Testicle Survival Time After a Torsion Event. Pediatr Emerg Care. 2019;35(12):821-825 | 10.1097/PEC.0000000000001287 | 28953100 | 出版社（Wolters Kluwer）の著作物（CC の表示なし） | RESTRICTED | PubMed レコードで書誌・抄録（時間帯別の生存率）を確認。出典マスターに DOI・PMID とも登録なし（新規） |
| SRC-4730 | European Association of Urology. EAU Guidelines on Urological Trauma. EAU Guidelines Office. 2025 (Limited text update March 2025) | なし | なし | © European Association of Urology（CC表示なし） | RESTRICTED | EAU 公式のガイドライン全文で Genital Trauma の節（鈍的陰嚢外傷の型、精巣破裂の所見と管理、脱臼・血瘤の扱い、穿通外傷、推奨表）を確認。出典マスターに本ガイドラインの登録なし（EAU の登録は尿路結石症 SRC-691 など別文書） |
| SRC-4731 | Hart PD, Bakris GL. Hypertensive nephropathy: prevention and treatment recommendations. Expert Opin Pharmacother. 2010;11(16):2675-2686 | 10.1517/14656566.2010.485612 | 20718588 | 出版社（Taylor & Francis）の著作物（CC の表示なし） | RESTRICTED | PubMed レコードで書誌・抄録を確認。出典マスターに DOI・PMID とも登録なし（新規） |
| SRC-4732 | Royal College of Obstetricians and Gynaecologists; British Society for Gynaecological Endoscopy. Management of Endometrial Hyperplasia. Green-top Guideline No. 67. 2016 | なし | なし | RCOG/BSGE のガイドライン（© Royal College of Obstetricians and Gynaecologists、CC表示なし） | RESTRICTED | RCOG 公式ページ（版履歴：2016年初版）で書誌を確認し、ガイドライン本文（PDF）の Executive summary of recommendations で分類・診断・治療の推奨を確認。DOI・PMID は Crossref・PubMed で付与されていないことを確認 |
| SRC-4733 | National Institute for Health and Care Excellence. Heavy menstrual bleeding: assessment and management. NICE Guideline, No. 88. 2018 | なし | なし | © National Institute for Health and Care Excellence（CC表示なし） | RESTRICTED | NICE 公式ガイドライン本文（NCBI Bookshelf 収載の 2021年版）で 1.2（病歴・診察・血液検査）・1.3（原因検索の検査）・1.5（管理）の推奨を確認 |

## 2. 事実カード（YAML）

```yaml
- id: CM-007
  domain: CM
  subdomain: 性器クラミジア感染症
  assertion:
    plain_statement_ja: 性器クラミジア感染症は日本で最も多い性感染症であり、性活動の活発な若年層、とくに女性に多い。男性では尿道炎が最も多く、潜伏期間は2〜3週間と淋菌性尿道炎より長く、排尿痛や尿道の不快感、掻痒感を生じ、若年男性では精巣上体炎の原因となる。女性では子宮頸管炎を起こし、上行感染により骨盤内炎症性疾患やFitz-Hugh-Curtis症候群、不妊の原因となるが、無症状のことも多い。咽頭感染も起こる。妊婦が感染していると、産道感染により新生児に結膜炎や肺炎を起こす。診断は培養法が最も確実だが時間を要するため、実際には抗原検出法や核酸増幅法などの遺伝子検出法が用いられ、核酸検査は菌の生死にかかわらず陽性が続くため治療後の治癒判定には注意が要る。治療にはテトラサイクリン系、マクロライド系、ニューキノロン系の抗菌薬を用い、再感染を防ぐためパートナーと同時に治療することが重要である。
    condition:
      region: 日本
      対象: 性器クラミジア感染症の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4721
    source: 国立健康危機管理研究機構（JIHS）感染症情報提供サイト「性器クラミジア感染症（詳細版）」
    doi: null
    pmid: null
    pmcid: null
    url: https://id-info.jihs.go.jp/infectious-diseases/chlamydia-std/detail/index.html
    source_license: 政府機関の公開ページ（国立健康危機管理研究機構 感染症情報提供サイト）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典ページの基になる資料は2004年時点の感染症発生動向調査週報（IDWR）で、ページには更新作業中の表示がある。具体的な用法・用量は同ページでは薬剤の系統名のみが示されており、現行の日本性感染症学会『性感染症 診断・治療ガイドライン2026』で確認する必要がある（同書の本文は本パートでは照合できていない）。薬剤について、テトラサイクリン系のドキシサイクリンは国内で承認され保険適用があり、JAID/JSC感染症治療ガイドラインの尿道炎の部ではクラミジア性尿道炎に対しドキシサイクリン100mgを1日2回7日間投与することが挙げられ、治癒判定として治療後2〜3週に核酸増幅法で陰転化を確認することが望ましいとされている。
  curriculum:
    kokushi: 医学各論 Ⅻ-2-A-②（性器クラミジア感染症、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BA-046
  domain: BA
  subdomain: 淋菌感染症
  assertion:
    plain_statement_ja: 淋菌は、男性の尿道炎、女性の子宮頸管炎のほか、精巣上体炎、骨盤内炎症性疾患、咽頭・直腸・結膜の感染、播種性淋菌感染症を起こす。咽頭と直腸の感染は多くが無症状で、感染源となる。男性の尿道炎は感染機会から3〜7日で発症し、多量の黄白色の膿性分泌物と強い排尿痛を呈する。診断にはグラム染色による鏡検、培養、核酸増幅法が用いられ、多剤耐性化が進んでいるため、可能な限り培養と薬剤感受性試験を行う。日本ではペニシリン系はほぼ感受性がなく、テトラサイクリン系とフルオロキノロン系では70〜80%が耐性で、保険適用があり確実に有効な薬剤はセフトリアキソンとスペクチノマイシンのみであり、セフトリアキソン耐性株は2009年に世界で初めて日本から報告された。日本の推奨では、男性の淋菌性尿道炎にセフトリアキソン1g単回点滴静注が第一選択、スペクチノマイシン2g単回筋注が第二選択であり、咽頭感染に有効なのはセフトリアキソンのみである。淋菌性尿道炎の20〜30%にクラミジア感染が合併し、パートナーの検査と同時治療が重要である。
    condition:
      region: 日本
      対象: 淋菌感染症の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4722
    source: Hamasuna R, Yasuda M, Takahashi S, Uehara S, Kawai Y, Miyairi I, Arakawa S, Kiyota H; JAID/JSC Guide/Guidelines Committee. The JAID/JSC guidelines to Clinical Management of Infectious Disease 2017 concerning male urethritis and related disorders. J Infect Chemother. 2021;27(4):546-554
    doi: 10.1016/j.jiac.2019.12.001
    pmid: '33516669'
    pmcid: null
    url: https://doi.org/10.1016/j.jiac.2019.12.001
    source_license: CC BY-NC-ND 4.0（論文中の表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典はJAID/JSC感染症治療ガイドラインの尿道炎の部（日本語版は感染症学雑誌2018年、英語版は2021年）で、詳細なレジメンは主に男性の尿道炎と精巣上体炎を対象とし、子宮頸管炎や播種性淋菌感染症の記載は同ガイドラインの淋菌感染症の総論に基づく。薬剤について、セフトリアキソンとスペクチノマイシンは淋菌感染症に対し国内で承認され保険適用がある（同ガイドラインの記載による）。セフトリアキソンの添付文書の用法では、尿道炎、子宮頸管炎、咽頭炎、直腸炎には1g単回静脈内投与、精巣上体炎と骨盤内炎症性疾患には1gを1日1回投与する。現行の日本性感染症学会『性感染症 診断・治療ガイドライン2026』の本文とは照合できておらず、同書での確認が望ましい。
  curriculum:
    kokushi: 医学各論 Ⅷ-5-D-①（淋菌性尿道炎、a）；医学各論 Ⅻ-2-B-⑥（淋菌感染症、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: GN-041
  domain: GN
  subdomain: 蛋白尿
  assertion:
    plain_statement_ja: 蛋白尿・アルブミン尿の定量では、初回検査として随時尿のアルブミン・クレアチニン比（ACR）を第一選択とし、総蛋白を測る場合は蛋白・クレアチニン比（PCR）を用いる。試験紙で陽性の場合は定量法で確認し、ACR 30 mg/g以上の陽性は早朝第一尿の検体で再検して確認する。血尿、月経、運動、尿路感染はACRやPCRを一過性に上昇させうるため、解釈の際に考慮する。アルブミン用の試験紙は、免疫グロブリン軽鎖などの非アルブミン蛋白を見逃しうる。原因の評価では、尿沈渣、単クローン性蛋白による腎障害を調べる血清・尿の蛋白電気泳動と免疫固定、血清遊離軽鎖、抗PLA2R抗体、ANCA、抗GBM抗体などの検査を追加し、腎生検は光学顕微鏡、蛍光抗体法、電子顕微鏡による所見から、正確な診断、病変の活動性と慢性化の評価、治療方針の決定に用いる。
    condition:
      region: 国際
      対象: 蛋白尿・アルブミン尿の評価を受ける人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-573
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int. 2024;105(4S):S117-S314'
    doi: 10.1016/j.kint.2023.10.018
    pmid: '38490803'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2023.10.018
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: KDIGO 2024 CKDガイドライン第1章のPractice Point 1.3.1.1〜1.3.1.2、Table 6、Table 16の記載に基づく。同ガイドラインは、蛋白尿の原因を糸球体性・尿細管性・溢出性に分ける三分法や、ネフローゼ域蛋白尿の数値定義を直接には示していないため、それらは本カードの主張に含めていない。本カードに薬剤名は含まれない。
  curriculum:
    kokushi: 医学各論 Ⅷ-1-E-②（蛋白尿、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-011 (id: JlAKpmg)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: UR-035
  domain: UR
  subdomain: 重複腎盂尿管
  assertion:
    plain_statement_ja: 重複腎盂尿管に伴う尿管瘤や逆流の評価では、超音波検査で上腎・下腎の拡張と膀胱内の尿管瘤を確認し、排尿時膀胱尿道造影で同側・対側の膀胱尿管逆流と膀胱頸部の状態を、DMSAなどの腎シンチグラフィで上腎・下腎の分腎機能を、MR尿路造影で形態を評価する。尿管瘤は女児に多く、その約80%は重複系の上極尿管に伴う。無症状で膀胱出口部閉塞がなく、上腎の水尿管腎症が軽度で、逆流が低グレード（III度未満）の場合は、予防的抗菌薬投与を含めた保存的管理を継続でき、長期の経過観察が必要である。尿路敗血症や膀胱頸部の閉塞がある場合は直ちにドレナージを行い、分腎機能が低下した例では腎機能の温存や尿路感染の予防のために手術を検討する。追加手術は、内視鏡的減圧、上腎部分切除や尿管尿管吻合などの上位アプローチ、尿管再植などの下位アプローチから、臨床状態、年齢、上腎の機能、逆流や閉塞の有無などによって選ぶ。
    condition:
      region: 国際
      対象: 重複腎盂尿管の小児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4723
    source: European Association of Urology. EAU Guidelines on Paediatric Urology. EAU Guidelines Office, Arnhem, The Netherlands. 2026
    doi: null
    pmid: null
    pmcid: null
    url: https://uroweb.org/guidelines/paediatric-urology/chapter/ureterocele-and-ectopic-ureter
    source_license: EAU（欧州泌尿器科学会）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典のEAU小児泌尿器ガイドライン（2026年版）第19章に基づく。同章は重複系の閉塞性病態（尿管瘤と異所開口）を中心に扱い、完全重複と不完全重複の定義そのものや不完全重複に特有の経過は扱っていないため、本カードは尿管瘤や逆流を伴う重複系の評価と管理に限った。本カードでは予防的抗菌薬を系統の記載にとどめ、特定の薬剤名は含まない。
  curriculum:
    kokushi: 医学各論 Ⅷ-10-A-①（重複腎盂尿管、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-429 (id: JlvnmHg)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: UR-036
  domain: UR
  subdomain: 異所性尿管開口
  assertion:
    plain_statement_ja: 異所性尿管開口は、尿管の開口が膀胱頸部や尿道、尿路の外にあるもので、約80%は完全重複腎盂尿管の上極尿管に伴い、女児に多い（男女比1対5）。女児の開口部位は尿道、前庭、腟、子宮や卵管で、括約筋より遠位に開口すると、正常な排尿ができるにもかかわらず尿が持続的に滴る。男児の開口は後部尿道、精嚢、射精管などで、外括約筋より遠位にはならないため失禁は生じず、反復する精巣上体炎などが手がかりとなる。診断では、超音波検査、DMSAやMAG3による腎シンチグラフィ、排尿時膀胱尿道造影、MRIで、分腎機能、逆流、同側下腎への圧迫を評価する。治療は、上腎の機能が温存に値する場合は尿管尿管吻合や尿管再植などの再建術を、機能のない上腎で感染を繰り返す場合や、女児で尿の持続的な滴りがある場合は上腎の部分切除（上極半腎切除）などの手術を検討する。
    condition:
      region: 国際
      対象: 異所性尿管開口の小児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4723
    source: European Association of Urology. EAU Guidelines on Paediatric Urology. EAU Guidelines Office, Arnhem, The Netherlands. 2026
    doi: null
    pmid: null
    pmcid: null
    url: https://uroweb.org/guidelines/paediatric-urology/chapter/ureterocele-and-ectopic-ureter
    source_license: EAU（欧州泌尿器科学会）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典のEAU小児泌尿器ガイドライン（2026年版）第19章の異所性尿管の節に基づく。単施設の治療成績ではなくガイドラインの一般論であり、術式の選択は症例ごとの解剖と分腎機能による。本カードに薬剤名は含まれない。
  curriculum:
    kokushi: 医学各論 Ⅷ-10-A-②（異所性尿管開口、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-429 (id: JlvnmHg)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: UR-037
  domain: UR
  subdomain: 膀胱瘤
  assertion:
    plain_statement_ja: 骨盤臓器脱の評価では、脱出・尿路・排便・性機能に関する症状の病歴をとり、診察で骨盤内腫瘤を除外したうえで、前方・中央・後方の各区画の脱出の有無と程度を POP-Q システムで評価・記録する。治療は無治療・非手術的治療・手術の選択肢を、本人の希望、脱出の部位、併存症、出産希望を踏まえて検討する。症状のある POP-Q ステージ1または2の脱出には、少なくとも16週間の指導付き骨盤底筋訓練を第一の選択肢として検討し、症候性の脱出には腟ペッサリー（単独または指導付き骨盤底筋訓練との併用）を検討する。非手術的治療で症状が改善しない場合、または本人が非手術的治療を望まない場合に手術を提案し、前腟壁脱出に対してはメッシュを用いない前方修復術を提案する。
    condition:
      region: 英国
      study: NICE ガイドライン NG123（尿失禁と骨盤臓器脱の管理、2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4724
    source: 'National Institute for Health and Care Excellence. Urinary incontinence and pelvic organ prolapse in women: management. NICE guideline NG123. 2019'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.nice.org.uk/guidance/ng123
    source_license: © NICE（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は英国のガイドラインであり、主張はその推奨本文（§1.6〜§1.8）で確認した範囲である。POP-Q のステージ判定の具体的な測定基準は同ガイドライン本文に明記されておらず含めていない。NICE の権利表示（Notice of rights、OGL の適用範囲を含む）の最終確認は取り込み側に委ねる。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-10-A-③（膀胱瘤、a）
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: UR-038
  domain: UR
  subdomain: 腹圧性尿失禁
  assertion:
    plain_statement_ja: 女性の尿失禁は初回評価で腹圧性・混合性・切迫性に分類し、混合性尿失禁では主たる症状を治療の対象とする。腹圧性尿失禁に対する第一選択の治療は、少なくとも3か月間の指導付き骨盤底筋訓練であり、BMI が30を超える場合は減量を助言する。非手術的管理で改善せず本人が手術を希望する場合は、膀胱頸部吊り上げ術（開腹または腹腔鏡下）、自家腹直筋筋膜スリング、恥骨後方中部尿道メッシュスリングの中から選択肢を提示する。代替となる手術手技が適さない、または本人が受け入れられない場合は尿道周囲への増量剤注入を検討するが、その効果は限定的で持続しない。侵襲的な治療手技を行う場合は、地域の多職種チームで提案された治療を検討する。
    condition:
      region: 英国
      study: NICE ガイドライン NG123（尿失禁と骨盤臓器脱の管理、2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4724
    source: 'National Institute for Health and Care Excellence. Urinary incontinence and pelvic organ prolapse in women: management. NICE guideline NG123. 2019'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.nice.org.uk/guidance/ng123
    source_license: © NICE（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は英国のガイドラインであり、主張はその推奨本文（§1.3〜§1.5）で確認した範囲である。個々の術式の国内での実施状況・保険適用の扱いは同ガイドラインでは分からず、本カードには含めていない。同ガイドラインにはデュロキセチンを腹圧性尿失禁の第一選択としない旨の記載があるが、国内では腹圧性尿失禁への適応がないため主張には含めなかった。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-10-D-③（腹圧性尿失禁、a）
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: UR-039
  domain: UR
  subdomain: 腎・尿路損傷
  assertion:
    plain_statement_ja: 腎・尿路外傷の画像評価の選択は血行動態の状態によって決まり、血行動態が安定している、または安定化した患者では、遅延尿路相を含む造影CTが診断のゴールドスタンダードである（推奨度1A）。腎損傷の重症度はAAST臓器損傷スケール（グレードI〜V）で分類し、これに血行動態を組み合わせたWSES分類では、安定したAASTグレードI〜IIを軽症、安定したグレードIIIを中等症、安定したグレードIV〜V（または主血管の解離・閉塞を伴う実質損傷）を重症、血行動態が不安定な場合を最重症として管理方針を立てる。血行動態が安定した軽症から重症までの損傷では非手術的管理が治療の第一選択であり（推奨度1B）、その前提としてCTによる正確な分類が必須である。血行動態が回復した重症損傷では、血管塞栓術によって非手術的管理を継続できる場合がある。
    condition:
      region: 国際
      study: WSES-AASTの腎・尿路外傷ガイドライン（2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-718
    source: 'Coccolini F, Moore EE, Kluger Y, et al; WSES-AAST Expert Panel. Kidney and uro-trauma: WSES-AAST guidelines. World J Emerg Surg. 2019;14:54'
    doi: 10.1186/s13017-019-0274-x
    pmid: '31827593'
    pmcid: PMC6886230
    url: https://doi.org/10.1186/s13017-019-0274-x
    source_license: CC BY（出版社ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: AAST グレードごとの解剖学的な定義は出典論文では図（Figure 2）に示されており、本文テキストでは確認できなかったため、グレード別の基準は含めていない。血尿は腎外傷の88〜94%にみられるが損傷グレードの予測にはならないこと、E-FAST は腎外傷に対する感度・特異度が低いことも同ガイドラインに記載がある。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-340 (id: Jlvnl_E)'
    kokushi: 医学各論 Ⅷ-10-E-①（腎・尿路損傷、a）
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: UR-040
  domain: UR
  subdomain: 膀胱結石、尿道結石
  assertion:
    plain_statement_ja: 膀胱結石は全尿路結石の約5%を占め、男性は女性の4〜10倍多い。分類は、水分摂取や栄養の不足した小児にみられる原発性（風土性）、下部尿路閉塞・神経因性膀胱・慢性細菌尿・異物・膀胱憩室などの異常を背景とする二次性、上部尿路から下降した移動性に分けられ、成人の膀胱結石の45〜79%では下部尿路閉塞が原因である。症状は頻尿、終末時血尿、排尿の終わりに最も強い排尿痛・恥骨上部痛であり、再発性の尿路感染が唯一の症状のこともあり、約10%は無症状に偶然発見される。診断の画像検査では、単純X線の感度が21〜78%、超音波検査の感度が20〜83%・特異度が98〜100%で、CT と膀胱鏡はこれらより感度が高い。治療に先立ち、尿流量測定、残尿測定、尿pHと尿培養、代謝評価、結石分析で結石の原因を評価する。無症状の移動性結石は治療せずに済むことがあるが、原発性と二次性は通常症候性で積極的治療の対象であり、尿酸結石は尿pHを6.5超に保つ経口アルカリ化で溶解できる。結石の除去は開腹・腹腔鏡・ロボット支援・内視鏡（経尿道的または経皮的）による手術、または体外衝撃波砕石術で行われ、経尿道的砕石術では高い結石消失率が得られる。
    condition:
      region: 国際
      対象: 成人・小児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4725
    source: Türk C, Donaldson JF, Petřík A, et al. EAU Guidelines on Bladder Stones. European Association of Urology. 2021 (Limited update March 2021)
    doi: null
    pmid: null
    pmcid: null
    url: https://d56bochluxqnz.cloudfront.net/documents/EAU-Pocket-on-Bladder-Stones-2021.pdf
    source_license: © European Association of Urology 2021（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は欧州泌尿器科学会（EAU）の膀胱結石ガイドライン（2021年版、2021年3月 limited update）の本文で確認した。感度・特異度や原因の割合は同ガイドラインの記載範囲の数値である。薬剤名は含まない（尿アルカリ化薬の具体名は本カードでは特定しなかった）。既存の UR-004（SRC-694）は成人男性の疫学と関連因子であり、症状・診断・治療の一般論は本出典で補った。同じ出題項目の尿道結石の側面は UR-043（仮）（SRC-9744）が担う。出典内の位置：本文の Prevalence, aetiology and risk factors、Presentation、Diagnostic evaluation、Disease Management の各項。
  curriculum:
    kokushi: 医学各論 Ⅷ-4-A-②（膀胱結石、尿道結石、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: UR-041
  domain: UR
  subdomain: 非淋菌性尿道炎
  assertion:
    plain_statement_ja: 非淋菌性尿道炎は、尿道分泌物の鏡検で炎症が確認され、グラム陰性双球菌などの淋菌の所見がない尿道炎であり、原因の内訳はクラミジア・トラコマティスが15〜40%、Mycoplasma genitalium が10〜25%、腟トリコモナスが1〜8%を占め、精密な検査を行っても約半数では病原体が特定できない。診断では、尿道炎の客観的所見（粘液性・粘膿性・膿性の分泌物、尿道分泌物の染色標本で油浸視野あたり2個以上の白血球、初尿の白血球エステラーゼ陽性または初尿沈渣で高倍率視野あたり10個以上の白血球）を確認したうえで、全例にクラミジアと淋菌の核酸増幅検査を行う。治療の推奨レジメンはドキシサイクリン100mgを1日2回7日間経口であり、アジスロマイシン1g単回経口などは代替である。症状が持続・再発する場合の最も多い原因は M. genitalium であり、核酸増幅検査で確認し、薬剤耐性検査が利用できない場合はドキシサイクリン7日間投与に続けてモキシフロキサシン400mgを1日1回7日間投与する2段階治療を行う。腟トリコモナスの関与が考えられる持続例ではメトロニダゾール2g単回投与を考慮する。過去60日以内のセックスパートナーは評価・検査とクラミジアに有効な治療のために紹介し、本人とパートナーの治療が完了するまで性交を控える。クラミジアによる男性の合併症には、精巣上体炎、前立腺炎、反応性関節炎がある。
    condition:
      region: 米国
      対象: 成人男性
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-703
    source: Workowski KA, Bachmann LH, Chan PA, et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recomm Rep. 2021;70(4):1-187
    doi: 10.15585/mmwr.rr7004a1
    pmid: '34292926'
    pmcid: PMC8344968
    url: https://doi.org/10.15585/mmwr.rr7004a1
    source_license: 米国政府著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 薬剤（ドキシサイクリン、アジスロマイシン、モキシフロキサシン、メトロニダゾール）を含むカードである。本カードは米国CDCの性感染症治療ガイドライン2021年版の記載であり、日本の性感染症の診断・治療の推奨とは薬剤選択や用量が異なる場合がある。ドキシサイクリンは国内承認薬で適応症に尿道炎を含み、アジスロマイシンはクラミジア性尿道炎が、メトロニダゾール内服薬はトリコモナス症が、それぞれ適応症に含まれる。一方、モキシフロキサシンは国内承認薬だが、尿道炎・M. genitalium 感染症は適応症に含まれず、本カードに基づく使用は適応外となる。性器クラミジア感染症そのものの臨床像・合併症・日本の位置づけは本カードの対象外とした（第64回の CM-007 が担う範囲）。出典内の位置：Diseases Characterized by Urethritis and Cervicitis の Urethritis、Nongonococcal Urethritis、Persistent or Recurrent Nongonococcal Urethritis の各節。
  curriculum:
    kokushi: 医学各論 Ⅷ-5-D-②（非淋菌性尿道炎、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: UR-042
  domain: UR
  subdomain: 性器ヘルペス
  assertion:
    plain_statement_ja: 性器ヘルペスの診断は臨床所見だけでは不十分で、病変部からの型特異的なウイルス学的検査（核酸増幅検査またはウイルス培養）で確認する。核酸増幅検査が最も感度が高く、再発と無症候性のウイルス排泄は単純ヘルペスウイルス2型で1型より格段に多いため型別が重要であり、病変がない場合の診断には型特異的血清学的検査が補助となる。症候性の初発の2型感染ではほぼ全例がその後再発し、抗ウイルス薬による治療は再発のたびに投与する発症時療法か、連日投与する抑制療法のいずれかで行う。抑制療法は再発頻度の高い例で再発を70〜80%減らし、頻度の低い例にも有効で、そのレジメンはアシクロビル400mgを1日2回、バラシクロビル500mgを1日1回または1gを1日1回である。不一致カップルでは、バラシクロビル500mgを1日1回の抑制療法が2型の伝播を減らす。妊娠では、分娩間近に性器ヘルペスに初感染すると新生児への伝播リスクは30〜50%と高いのに対し、妊娠前から再発歴がある場合や妊娠前半の感染では1%未満である。妊娠36週からアシクロビル400mgを1日3回またはバラシクロビル500mgを1日2回の抑制療法を行うと分娩時の再発と帝王切開が減り、分娩開始時に再発病変がある女性は帝王切開とし、病変も前駆症状もなければ経腟分娩ができる。
    condition:
      region: 米国
      対象: 成人（妊婦を含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-703
    source: Workowski KA, Bachmann LH, Chan PA, et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recomm Rep. 2021;70(4):1-187
    doi: 10.15585/mmwr.rr7004a1
    pmid: '34292926'
    pmcid: PMC8344968
    url: https://doi.org/10.15585/mmwr.rr7004a1
    source_license: 米国政府著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 薬剤（アシクロビル、バラシクロビル）を含むカードである。バラシクロビルは国内で「性器ヘルペスの再発抑制」の承認適応があり（バルトレックス錠500、通常は成人に1回500mgを1日1回経口投与、PMDA の添付文書情報で確認）、CDC の抑制療法の用法の一部は国内適応の範囲内である。一方、アシクロビルの国内適応は単純疱疹、帯状疱疹、造血幹細胞移植における単純ヘルペスウイルス感染症の発症抑制などであり、成人への性器ヘルペス再発抑制の明示的な適応はバラシクロビルにあるため、CDC 記載のアシクロビル抑制療法（400mgを1日2回）と妊娠36週からの抑制療法は国内の承認用法と異なり、適応外使用となる場合がある。ファムシクロビルは CDC の抑制療法の選択肢に挙がるが、性器ヘルペス再発抑制の国内適応を確認していないため主張には含めなかった。出典は米国 CDC の性感染症治療ガイドライン2021年版であり、日本の性感染症ガイドラインにおける位置づけは本カードの範囲外である。初発例の治療レジメンは既存の UR-021 が担う。出典内の位置：Genital Herpes の Diagnosis、再発と抑制療法、Genital Herpes During Pregnancy の各項。
  curriculum:
    kokushi: 医学各論 Ⅷ-5-D-③（性器ヘルペス、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: UR-043
  domain: UR
  subdomain: 膀胱結石、尿道結石
  assertion:
    plain_statement_ja: 尿道結石は全尿路結石の1%未満とまれである。2000年から2019年の症例を集めた系統的レビュー（74論文・95例）では、所見として触知可能な尿道の腫瘤が57.9%、排尿症状が41.1%、疼痛が40.0%、急性尿閉が32.6%にみられた。最初の検査は単純X線が63.2%で最も多く、結石の98.3%がX線不透過性だった。背景に尿道病変を伴う例が53.7%あり、うち尿道憩室が33.7%、尿道狭窄が13.7%だった。結石は尿道の閉塞の近位や憩室内に原発性に生じる場合と、膀胱や上部尿路から移動して嵌頓する場合がある。治療は外的な尿道切石術が31.6%、結石を逆行性に押し戻す操作が22.1%、内視鏡下でその場で砕く in situ 砕石術が17.9%で、その選択は結石の大きさ、形、位置と尿道病変の有無によって決まる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4726
    source: 'Morton A, Tariq A, Dunglison N, Esler R, Roberts MJ. Etiology and management of urethral calculi: a systematic review of contemporary series. Asian J Urol. 2024;11(1):10-18'
    doi: 10.1016/j.ajur.2021.12.011
    pmid: '38312816'
    pmcid: PMC10837653
    url: https://doi.org/10.1016/j.ajur.2021.12.011
    source_license: CC BY-NC-ND 4.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は症例報告と症例集積の系統的レビュー（95例）の集計であり、頻度の解釈には報告バイアスの影響がありうる。同レビューでは膀胱・上部尿路結石の併存割合が抄録（16.8%）と Table 1（33.7%）で異なるため、その数値は主張に含めなかった。薬剤名は含まない。同じ出題項目の膀胱結石の側面は UR-040（仮）（SRC-9743）が担う。出典内の位置：抄録および本文の臨床像・検査・Table 1・治療の各項。
  curriculum:
    kokushi: 医学各論 Ⅷ-4-A-②（膀胱結石、尿道結石、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: GU-040
  domain: GU
  subdomain: 包茎
  assertion:
    plain_statement_ja: 小児の包茎は、包皮口が柔軟で瘢痕がなく、年齢とともに翻転できるようになる生理的包茎と、遠位部に瘢痕化（収縮した白色の線維性輪）を伴う病的包茎とに分けられる。生理的包茎で包皮が翻転できない子の割合は、3歳で10%、6歳で8%、16歳で1%と年齢とともに低下する。病的包茎の原因としては閉塞性乾皮性亀頭炎（硬化性苔癬）が多く、ステロイド外用に反応しにくい。包皮を無理に翻転すると微小な裂け目が生じて瘢痕化を招くため、無理な翻転は避ける。瘢痕のない包皮口へのステロイド外用（0.1%トリアムシノロンクリームを1日2回、6〜8週間）により、約80%で包皮口の組織が緩む。翻転した包皮が戻らなくなった嵌頓包茎は緊急の病態であり、浮腫を圧迫して用手的に整復し、重症例では背面切開を行う。包皮環切除の唯一の絶対適応は病的包茎である。
    condition:
      region: 国際
      対象: 小児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4727
    source: 'McGregor TB, Pike JG, Leonard MP. Pathologic and physiologic phimosis: approach to the phimotic foreskin. Can Fam Physician. 2007;53(3):445-448'
    doi: null
    pmid: '17872680'
    pmcid: PMC1949079
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC1949079/
    source_license: © College of Family Physicians of Canada（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤（トリアムシノロン外用）を含むカードである。副腎皮質ステロイド外用薬は国内で承認された薬効群であるが、包茎へのステロイド外用は添付文書上の適応ではなく適応外使用にあたる（個別製剤の添付文書では確認していない）。年齢別の割合は本総説が引用する Oster（1968年）のコホートの数値である。出典は2007年の総説であり、本カードは依頼文の指定どおり生理的包茎の自然経過と病的包茎の鑑別・保存的治療に範囲を限った。後天性包茎と亀頭炎の頻度は既存の GU-033（SRC-742）が担う。本論文の書誌（PMC・PubMed）に DOI の記載がなく、null とした。出典内の位置：本文の生理的包茎・病的包茎・嵌頓包茎の各項。
  curriculum:
    kokushi: 医学各論 Ⅷ-10-B-②（包茎、a）
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: GU-041
  domain: GU
  subdomain: 精巣・精索水瘤
  assertion:
    plain_statement_ja: 成人の精巣水瘤は精巣鞘膜内に漿液が貯留したもので、典型的には無痛性の陰嚢腫脹として現れ、不快感を伴うことがある。腹膜鞘状突起が開存して腹腔と陰嚢が交通する交通性と、交通がなく鞘膜内の分泌と吸収の不均衡によって生じる非交通性に分類され、分類と原因の同定が管理の方針に関わる。管理では、水腫切除術が主な外科的治療であり、大きく持続する水瘤に対して推奨される。穿刺吸引と硬化療法は低侵襲で安価な代替手段であるが、再発などの合併症がありうる。水腫切除術の術後合併症には、陰嚢浮腫、血腫、慢性疼痛、感染などがある。
    condition:
      region: 米国
      study: 骨盤・鼠径部の水瘤の分類・病因・評価・管理に関する総説（Current Urology、2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4728
    source: 'Dagur G, Gandhi J, Suh Y, et al. Classifying Hydroceles of the Pelvis and Groin: An Overview of Etiology, Secondary Complications, Evaluation, and Management. Curr Urol. 2017;10(1):1-14'
    doi: 10.1159/000447145
    pmid: '28559772'
    pmcid: PMC5436019
    url: https://doi.org/10.1159/000447145
    source_license: © S. Karger AG（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 既存出典 SRC-749（Tiemstra 2008）は透光性などの臨床像・評価は担うが水腫切除術など管理の記載が本文に確認できなかったため、本カードは管理まで扱う本総説を新規出典とした。透光性と新生児例の自然消失については既存カード GU-035 が担う。出版社のオープンアクセス条件（CC BY-NC-ND の適用有無）は本文の表示では確定できず、取り込み側での最終確認を要する。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-350 (id: JlvnmAI)'
    kokushi: 医学各論 Ⅷ-10-B-④（精巣・精索水瘤、a）
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: GU-042
  domain: GU
  subdomain: 精巣捻転症
  assertion:
    plain_statement_ja: 精巣捻転症の精巣温存は、発症から捻転解除までの時間に強く依存する。症例集積30研究・2,116例の系統的レビューでは、治療までの時間ごとの精巣生存率は、0〜6時間で97.2%、7〜12時間で79.3%、13〜18時間で61.3%、19〜24時間で42.5%、25〜48時間で24.4%、48時間超で7.4%であり、累積では12時間以内で90.4%、13〜24時間で54.0%、24時間超で18.1%だった。したがって、捻転が疑われる例では速やかな外科的対応が原則であり、発症から長時間を経た例でも生存の可能性が残るため、積極的な対応が推奨される。なお、ここでの生存率は、その後の精巣萎縮や機能の有無を問わない定義による。
    condition:
      region: 国際
      対象: 精巣捻転症の患者（主に小児・思春期。症例集積2,116例の系統的レビュー）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4729
    source: Mellick LB, Sinex JE, Gibson RW, Mears K. A Systematic Review of Testicle Survival Time After a Torsion Event. Pediatr Emerg Care. 2019;35(12):821-825
    doi: 10.1097/PEC.0000000000001287
    pmid: '28953100'
    pmcid: null
    url: https://doi.org/10.1097/PEC.0000000000001287
    source_license: 出版社（Wolters Kluwer）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は系統的レビューの抄録で確認した範囲であり、対象は小児・思春期の症例集積が中心である。「画像検査で手術を遅らせない」という原則そのものはガイドライン側の記載で、本出典（系統的レビュー）には含まれないため主張には入れていない。既存の GU-037 の出典 SRC-750（超音波の総説）では時間と温存率の数値が確認できなかったため、本カードは新規出典によった。
  curriculum:
    kokushi: 医学各論 Ⅷ-10-B-⑥（精巣捻転症、a）
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-351 (id: JlvnmAQ)；TBL-01-00-350 (id: JlvnmAI)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: GU-043
  domain: GU
  subdomain: 精巣損傷
  assertion:
    plain_statement_ja: 精巣損傷は機序により鈍的外傷と穿通外傷に分けられ、鈍的陰嚢外傷では精巣脱臼、精巣周囲の血瘤、精巣破裂、陰嚢血腫が生じうる。精巣破裂は、精巣が下恥骨枝や恥骨結合に強く圧迫されて白膜が断裂した状態で、直後の疼痛、悪心、嘔吐、ときに失神を伴う。精巣外傷の診断では陰嚢超音波検査が第一選択である。管理は損傷の型で異なり、血瘤が対側精巣の3倍未満であれば保存的に経過をみて、大きければ外科的に検索する。精巣破裂が疑われる場合と、超音波検査で結論が得られない場合は精巣を外科的に検索し、破裂では血腫と壊死した精細管を除去して白膜を閉鎖する。精巣脱臼は用手整復に続く二次的な精巣固定術で治療し、用手整復ができなければ即時の精巣固定術を行う。穿通外傷では外科的検索と保存的なデブリードマンを行い、精巣と陰嚢の一次再建が可能なことが多いが、再建できない場合は精巣摘除が適応となる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4730
    source: European Association of Urology. EAU Guidelines on Urological Trauma. EAU Guidelines Office. 2025 (Limited text update March 2025)
    doi: null
    pmid: null
    pmcid: null
    url: https://uroweb.org/guidelines/urological-trauma
    source_license: © European Association of Urology（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は欧州泌尿器科学会（EAU）の尿路外傷ガイドライン（2025年3月 limited text update）の Genital Trauma の節で確認した。EAU の公式ページでは2026年版が2025年版の全面再構成であると案内されており、取り込み時に最新版での照合が望ましい。薬剤名は含まない。既存の GU-039（SRC-750）は単施設の超音波所見の後ろ向き検討であり、分類と保存・手術の判断の一般論は本出典で補った。出典内の位置：Genital Trauma の Blunt scrotal trauma、Penetrating scrotal trauma、Table 1（testicular trauma）、Recommendations for the management of genital trauma。
  curriculum:
    kokushi: 医学各論 Ⅷ-10-E-③（精巣損傷、a）
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: KT-029
  domain: KT
  subdomain: 高血圧性腎硬化症
  assertion:
    plain_statement_ja: 高血圧性腎硬化症（高血圧性腎症）は、糖尿病に次いで多い進行性慢性腎臓病の原因とされる。長期の高血圧に伴ってアルブミン尿と腎機能低下が緩徐に進行し、末期腎不全に至りうる。治療の要点はアルブミン尿の低減と血圧管理であり、レニン・アンジオテンシン・アルドステロン系阻害薬を中心に、カルシウム拮抗薬や利尿薬などを組み合わせた積極的な降圧が、末期腎不全への進行を遅らせるうえで重要とされる。同総説では、血圧目標として130 mmHg未満が論じられている。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4731
    source: 'Hart PD, Bakris GL. Hypertensive nephropathy: prevention and treatment recommendations. Expert Opin Pharmacother. 2010;11(16):2675-2686'
    doi: 10.1517/14656566.2010.485612
    pmid: '20718588'
    pmcid: null
    url: https://doi.org/10.1517/14656566.2010.485612
    source_license: 出版社（Taylor & Francis）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは2010年の総説に基づく。血圧目標の数値は同総説の記載であり、その後のガイドライン（KDIGO 2021 の慢性腎臓病における血圧管理ガイドライン（既存 SRC-4382）など）では異なる目標が示されているため、本カードの数値は出典の範囲として読むこと。薬剤について、ACE阻害薬・ARBなどのレニン・アンジオテンシン・アルドステロン系阻害薬、カルシウム拮抗薬、利尿薬はいずれも国内で高血圧症に対して承認・保険適用のある薬剤クラスである（個別製剤の効能・効果の範囲は添付文書による）。既存の KT-001 の出典 SRC-605（腎硬化症の総説）は論点整理が中心で治療・予後の記載が薄かったため、本カードは新規出典によった。
  curriculum:
    kokushi: 医学各論 Ⅷ-2-A-①（高血圧性腎硬化症、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-327 (id: Jlvnl90)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: KT-030
  domain: KT
  subdomain: 急性尿細管壊死
  assertion:
    plain_statement_ja: 急性尿細管壊死と他の急性腎障害の鑑別では、尿沈渣と尿中電解質が手がかりになる。尿沈渣で尿細管細胞や、壊死した尿細管細胞がタム・ホルスフォール蛋白と集まった泥状褐色（muddy brown）円柱がみられれば、尿細管障害を示す。一方、FENa 1%未満、尿中尿酸排泄率12%未満、尿素排泄率34%未満という低値と正常な尿沈渣の組み合わせは、腎前性（機能的）急性腎障害を支持する。ただし、尿中電解質の単回測定の鑑別能は限られ、慢性腎臓病、利尿薬の使用、敗血症などでは典型的な所見が修飾されるため、典型所見を欠くことでは腎前性を除外できない。腎後性（閉塞性）は腎超音波で尿路閉塞の有無を評価して除外し、赤血球円柱や変形赤血球は糸球体性、白血球円柱は間質性・感染性の病変を示唆する。
    condition:
      region: 国際
      対象: 急性腎障害の患者（重症患者を中心とする総説）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-666
    source: 'Ostermann M, Joannidis M. Acute kidney injury 2016: diagnosis and diagnostic workup. Crit Care. 2016;20:299'
    doi: 10.1186/s13054-016-1478-z
    pmid: '27670788'
    pmcid: PMC5037640
    url: https://doi.org/10.1186/s13054-016-1478-z
    source_license: CC BY 4.0（PMC ページの表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: FENa 等の閾値と尿沈渣の解釈は本文の尿中電解質の項と尿沈渣の表から読み取った（表から読み取り）。同総説は重症患者を主な対象としており、利尿薬は治療薬としてではなく診断指標への影響因子として挙げられている。急性尿細管壊死の原因分類（虚血性・腎毒性）の一般像は既存の KT-009（SRC-613）が担い、本カードは鑑別に絞った。管理・透析適応は本カードの出典の範囲外である。
  curriculum:
    kokushi: 医学各論 Ⅷ-2-B-①（急性尿細管壊死、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: KF-041
  domain: KF
  subdomain: 脱水と浮腫
  assertion:
    plain_statement_ja: 浮腫は、毛細血管からの濾過がリンパドレナージの限界を上回り、間質に液体が貯留した状態である。原因の評価は、分布（片側か両側か、全身性か）と経過（急性か慢性か）、圧痕の有無で分けて進める。急速に生じた全身性の圧痕性浮腫は全身性疾患を示唆し、速やかな原因の診断と管理を要する。片側または両側の下腿に慢性的にみられる浮腫では静脈不全が多く、体位依存性の浮腫やヘモジデリン沈着が手がかりになる。硬く圧痕を残さない浮腫はリンパ浮腫の特徴で、二次性リンパ浮腫の原因には腫瘍、外傷、骨盤内手術、鼠径リンパ節郭清、放射線治療などがある。睡眠時無呼吸は、肺高血圧を伴わない場合でも両側下腿浮腫の原因となりうる。深部静脈血栓症の疑いが二重超音波検査の陰性結果の後も残る場合は、骨盤内や大腿近位部の静脈血栓・圧迫をMR静脈造影で評価することがある。
    condition:
      region: 米国
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-665
    source: 'Trayes KP, Studdiford JS, Pickle S, Tully AS. Edema: diagnosis and management. Am Fam Physician. 2013;88(2):102-110'
    doi: null
    pmid: '23939641'
    pmcid: null
    url: https://www.ncbi.nlm.nih.gov/pubmed/23939641
    source_license: 出版社（米国家庭医学会）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードの記載は抄録で確認できた範囲であり、薬剤性浮腫を含む原因表の詳細は抄録では確認していないため主張に入れていない。浮腫の鑑別の総論（両側性・片側性での分け方と検査の手がかり）は KX-001 が同じ出典で担っており、本カードは Ⅷ-3-E-① の2件目として、機序、リンパ浮腫の二次性原因、睡眠時無呼吸との関連など KX-001 にない側面を中心に置いた。既存の KF-028 が脱水の身体所見を担い、本カードで項目の浮腫側を補う。
  curriculum:
    kokushi: 医学各論 Ⅷ-3-E-①（脱水と浮腫、a）
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-013 (id: JlAKpmo)；TBL-02-08-009 (id: JlAKpmk)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: GY-063
  domain: GY
  subdomain: 子宮内膜増殖症
  assertion:
    plain_statement_ja: 子宮内膜増殖症は、改訂2014年WHO分類で、細胞異型の有無により異型のない増殖症と異型増殖症の2群に分けることが推奨されている。診断には子宮内膜組織の病理組織学的検査が必要で、外来での子宮内膜生検が経過観察を含めた基本となり、外来採取が失敗・診断不能な場合や、ポリープなどの局所病変内に増殖症が見つかった場合は子宮鏡による直視下の生検を検討する。異型のない増殖症は、20年間で子宮内膜癌へ進展するリスクが5%未満で、多くは経過観察中に自然に退縮する。管理では肥満やホルモン補充療法などの可逆的な危険因子への対応が基本で、観察のみで退縮しない場合や異常子宮出血の症状がある場合にプロゲスチン療法が適応となる。第一選択はレボノルゲストレル放出子宮内システムであり、経口プロゲスチンより退縮率が高く、出血の性状が好ましく、有害事象も少ない。これを希望しない場合は、メドロキシプロゲステロン10〜20mg/日またはノルエチステロン10〜15mg/日の連日経口投与を用い、周期投与は退縮効果が劣るため用いない。治療は組織学的退縮を得るために最低6か月行い、少なくとも6か月ごとの子宮内膜生検で経過をみる。子宮摘出は異型のない増殖症の第一選択ではなく、妊孕性の温存を希望しない女性で、経過中に異型増殖症へ進行した場合、12か月治療しても組織学的退縮がない場合、治療終了後に再発した場合、出血症状が続く場合、経過観察や内服治療を希望しない場合に適応となる。異型増殖症では、潜在する悪性腫瘍の合併や癌への進行のリスクがあるため、全子宮摘出術が推奨される。異型増殖症で妊孕性温存を希望する場合は、まずレボノルゲストレル放出子宮内システムを第一選択とし（経口プロゲスチンは次善）、3か月ごとの生検で経過をみて、妊孕性が不要になれば子宮摘出を提示する。
    condition:
      region: 英国
      対象: 成人女性
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4732
    source: Royal College of Obstetricians and Gynaecologists; British Society for Gynaecological Endoscopy. Management of Endometrial Hyperplasia. Green-top Guideline No. 67. 2016
    doi: null
    pmid: null
    pmcid: null
    url: https://www.rcog.org.uk/guidance/browse-all-guidance/green-top-guidelines/management-of-endometrial-hyperplasia-green-top-guideline-no-67/
    source_license: RCOG/BSGE のガイドライン（© Royal College of Obstetricians and Gynaecologists、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤（レボノルゲストレル放出子宮内システム、メドロキシプロゲステロン、ノルエチステロン）を含むカードである。レボノルゲストレル放出子宮内システム（ミレーナ52mg）は国内で承認されているが、効能・効果は避妊・過多月経・月経困難症であり、子宮内膜増殖症は含まれないため、本ガイドラインに基づく使用は適応外となる。経口プロゲスチン製剤も国内承認薬であるが、子宮内膜増殖症そのものは効能・効果に明記されていない（ノルエチステロンの添付文書で確認）。本ガイドラインは2016年の初版であり、RCOGの公式ページには改訂版が開発中である旨が記載されている（2026-11-01確認）。ガイドライン文書自体にはDOI・PMIDが付与されておらず、Crossref・PubMedで確認できなかったため null とした。出典内の位置：Executive summary of recommendations の分類・診断・異型のない増殖症の管理・異型増殖症の管理の各項。
  curriculum:
    kokushi: 医学各論 Ⅷ-7-C-①（子宮内膜増殖症、a）
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-661 (id: Jlvnmd4)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: RP-068
  domain: RP
  subdomain: 視床下部性無月経
  assertion:
    plain_statement_ja: 機能性視床下部性無月経は、器質的な原因が特定できない慢性の無排卵であり、ストレス、体重減少、過度の運動、またはその組み合わせによるエネルギーバランスの負の偏りに関連する。診断は除外診断であり、評価では妊娠を除外したうえで、食事、摂食障害、運動、体重変動、心理的ストレス要因などを含む詳細な病歴を聴取し、全身性・内分泌性の他の原因を除外する。合併症には骨量減少と不妊があり、6か月以上の無月経がある思春期・成人女性では、DXAによるベースラインの骨密度測定が勧められる（重度の栄養欠乏や骨の脆弱性が疑われる場合はより早期に）。管理の基本は、摂取量の増加、栄養の改善、運動量の減少によってエネルギー不足を是正し、視床下部-下垂体-卵巣系の機能を改善することであり、しばしば体重増加を要する。認知行動療法などの心理的支援も併せて行う。月経の回復や骨密度の改善だけを目的とした経口避妊薬の使用は勧められず、骨密度の改善を目的としたビスホスホネート、デノスマブ、テストステロン、レプチンの使用も行わない。栄養、心理、運動への介入を十分な期間行っても月経が回復しない場合は、経皮エストラジオールと周期的な経口プロゲスチンの短期使用が選択肢として示唆される。
    condition:
      region: 米国
      対象: 思春期・成人女性
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-817
    source: 'Gordon CM, Ackerman KE, Berga SL, Kaplan JR, Mastorakos G, Misra M, Murad MH, Santoro NF, Warren MP. Functional Hypothalamic Amenorrhea: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2017;102(5):1413-1439'
    doi: 10.1210/jc.2017-00131
    pmid: '28368518'
    pmcid: null
    url: https://doi.org/10.1210/jc.2017-00131
    source_license: Endocrine Societyのガイドライン。CC表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 薬剤（経皮エストラジオール、経口プロゲスチン、経口避妊薬）を含むカードである。エストラジオール製剤は国内で承認されているが、機能性視床下部性無月経を効能・効果とする製剤はなく、本ガイドラインに基づく経皮エストラジオールの使用は適応外となる。無月経の診断・初期検査（ホルモン検査と解釈）の側面は、同じ出典に基づく既存の RP-019 が担っているため、本カードは原因・骨への影響・管理に絞った。出典内の位置：抄録（Conclusions）と、骨密度評価および治療（エネルギー不足の是正、心理的支援、経口避妊薬・骨作用薬・経皮エストラジオール）に関する推奨。治療推奨の細部はガイドラインの推奨要約で確認した範囲である。
  curriculum:
    kokushi: 医学各論 Ⅷ-8-A-①（視床下部性無月経、a）
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: RP-069
  domain: RP
  subdomain: 過多月経
  assertion:
    plain_statement_ja: 過多月経の評価では、出血の性状に加えて、持続する月経間期出血や骨盤痛・圧迫症状など、子宮内腔の異常、組織学的異常、子宮腺筋症、子宮筋腫を示唆する関連症状の有無と、生活の質への影響を聴取する。関連症状を伴う場合や、検査・レボノルゲストレル放出子宮内システム装着の前には診察を行う。血液検査では、治療と並行して全例に全血算を行い、初経時から過多月経があり凝固障害を示唆する個人歴・家族歴がある女性では凝固障害の検査を考慮する一方、血清フェリチンと女性ホルモンの測定は定型としては行わない。原因検索では、病歴と診察に応じて子宮鏡または超音波検査を第一選択とし、粘膜下筋腫・ポリープ・子宮内膜病変が疑われる場合は外来子宮鏡を、子宮が腹部から触知できる場合、骨盤内腫瘤が疑われる場合、診察が困難・不十分な場合は骨盤超音波を行い、内膜病変の高リスク例では子宮鏡の際に内膜生検を併せて行う。治療の選択では本人の希望、併存疾患、筋腫・ポリープ・内膜病変・腺筋症の有無を考慮し、病変がない場合、子宮内腔の変形を伴わない直径3cm未満の筋腫の場合、子宮腺筋症が疑われる・診断された場合には、レボノルゲストレル放出子宮内システムを最初の治療として検討する。これを希望しない、または適さない場合は、非ホルモン薬のトラネキサム酸またはNSAIDs、ホルモン療法の低用量エストロゲン・プロゲスチン配合剤または周期型経口プロゲスチンを検討する。治療が奏効しない場合、本人が薬物療法を希望しない場合、症状が重い場合は専門施設へ紹介し、第2世代の子宮内膜アブレーションや子宮摘出などの外科的選択肢を検討する。
    condition:
      region: 英国
      対象: 成人女性
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4733
    source: 'National Institute for Health and Care Excellence. Heavy menstrual bleeding: assessment and management. NICE Guideline, No. 88. 2018'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.nice.org.uk/guidance/ng88
    source_license: © National Institute for Health and Care Excellence（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤（トラネキサム酸、NSAIDs、低用量エストロゲン・プロゲスチン配合剤、周期型経口プロゲスチン）を含むカードである。レボノルゲストレル放出子宮内システム（ミレーナ52mg）は、国内で過多月経が効能・効果に含まれ、承認・保険適用がある（添付文書で確認）。トラネキサム酸は国内承認薬で、性器出血を含む異常出血が効能・効果に含まれる。周期型経口プロゲスチンのノルエチステロンは、効能・効果の月経量異常に過多月経が含まれる（添付文書で確認）。一方、NSAIDs と、低用量エストロゲン・プロゲスチン配合剤（国内での承認は避妊または月経困難症）には過多月経の効能はなく、本ガイドラインに基づく使用は適応外となる。過多月経の定義と FIGO の PALM-COEIN 分類は既存の RP-009（SRC-818）が担っているため、本カードは評価と治療に絞った。ガイドライン文書には DOI・PMID は付与されていない。出典内の位置：1.2（病歴・診察・臨床検査）、1.3（原因検索のための検査）、1.5（過多月経の管理）の各項。
  curriculum:
    kokushi: 医学各論 Ⅷ-8-B-②（過多月経、a）
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-02-09-016 (id: JlAKpo4)；TBL-02-09-021 (id: JlAKppQ)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
```


## 3. カリキュラム対応表

| カード | subdomain | kokushi | コアカリ |
|---|---|---|---|
| CM-007 | 性器クラミジア感染症 | 医学各論 Ⅻ-2-A-②（性器クラミジア感染症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c) |
| BA-046 | 淋菌感染症 | 医学各論 Ⅷ-5-D-①（淋菌性尿道炎、a）；医学各論 Ⅻ-2-B-⑥（淋菌感染症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c) |
| GN-041 | 蛋白尿 | 医学各論 Ⅷ-1-E-②（蛋白尿、a） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-011 (id: JlAKpmg) |
| UR-035 | 重複腎盂尿管 | 医学各論 Ⅷ-10-A-①（重複腎盂尿管、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-429 (id: JlvnmHg) |
| UR-036 | 異所性尿管開口 | 医学各論 Ⅷ-10-A-②（異所性尿管開口、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-429 (id: JlvnmHg) |
| UR-037 | 膀胱瘤 | 医学各論 Ⅷ-10-A-③（膀胱瘤、a） | PS-02-09-05 (id: JkxnuRs) |
| UR-038 | 腹圧性尿失禁 | 医学各論 Ⅷ-10-D-③（腹圧性尿失禁、a） | PS-02-09-05 (id: JkxnuRs) |
| UR-039 | 腎・尿路損傷 | 医学各論 Ⅷ-10-E-①（腎・尿路損傷、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-340 (id: Jlvnl_E) |
| UR-040 | 膀胱結石、尿道結石 | 医学各論 Ⅷ-4-A-②（膀胱結石、尿道結石、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I) |
| UR-041 | 非淋菌性尿道炎 | 医学各論 Ⅷ-5-D-②（非淋菌性尿道炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c) |
| UR-042 | 性器ヘルペス | 医学各論 Ⅷ-5-D-③（性器ヘルペス、a） | PS-02-09-05 (id: JkxnuRs) |
| UR-043 | 膀胱結石、尿道結石 | 医学各論 Ⅷ-4-A-②（膀胱結石、尿道結石、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I) |
| GU-040 | 包茎 | 医学各論 Ⅷ-10-B-②（包茎、a） | PS-02-10-05 (id: JkxnuSA) |
| GU-041 | 精巣・精索水瘤 | 医学各論 Ⅷ-10-B-④（精巣・精索水瘤、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-350 (id: JlvnmAI) |
| GU-042 | 精巣捻転症 | 医学各論 Ⅷ-10-B-⑥（精巣捻転症、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-351 (id: JlvnmAQ)；TBL-01-00-350 (id: JlvnmAI) |
| GU-043 | 精巣損傷 | 医学各論 Ⅷ-10-E-③（精巣損傷、a） | PS-02-10-05 (id: JkxnuSA) |
| KT-029 | 高血圧性腎硬化症 | 医学各論 Ⅷ-2-A-①（高血圧性腎硬化症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-327 (id: Jlvnl90) |
| KT-030 | 急性尿細管壊死 | 医学各論 Ⅷ-2-B-①（急性尿細管壊死、a） | PS-02-09-05 (id: JkxnuRs) |
| KF-041 | 脱水と浮腫 | 医学各論 Ⅷ-3-E-①（脱水と浮腫、a） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-013 (id: JlAKpmo)；TBL-02-08-009 (id: JlAKpmk) |
| GY-063 | 子宮内膜増殖症 | 医学各論 Ⅷ-7-C-①（子宮内膜増殖症、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-661 (id: Jlvnmd4) |
| RP-068 | 視床下部性無月経 | 医学各論 Ⅷ-8-A-①（視床下部性無月経、a） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU) |
| RP-069 | 過多月経 | 医学各論 Ⅷ-8-B-②（過多月経、a） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-016 (id: JlAKpo4)；TBL-02-09-021 (id: JlAKppQ) |

## 4. 未解決事項

- 性感染症診断・治療ガイドライン2026（日本性感染症学会、診断と治療社。本文未照合）は CM-007・BA-046 の出典差し替え候補。本文が確認できれば日本の推奨はこちらが正になる
- SRC-4730（EAU 尿路外傷ガイドライン）は2025年3月版に準拠。2026年版で全面再構成が公式に案内されており、再照合が望ましい。SRC-4725（EAU 膀胱結石ガイドライン）は2021年版で、以後の改訂有無は未確認
- SRC-4732（RCOG/BSGE GTG67）は RCOG で改訂版が開発中。SRC-4733（NICE NG88）の推奨確認は Bookshelf 収載版により、NICE 公式ではその後の更新が示される。いずれも取り込み時に最新版での再確認を推奨する
- SRC-4724（NICE NG123）のライセンス（Notice of rights／OGL の範囲）と SRC-4728（Dagur 2017）の CC BY-NC-ND 適用有無は未確定で RESTRICTED とした。取り込み側の最終確認を推奨する
- SRC-4729（Mellick 2019）・SRC-4731（Hart & Bakris 2010）は購読誌で CC 表示なしのため RESTRICTED。取り込み側の Crossref 照合で確定されたい
- EAU ガイドライン（SRC-4723・4725・4730）の個別書誌（ISBN）は合本のものしか確認できず、確定は取り込み側に委ねる
- UR-038 の術式列挙は NICE NG123 の §1.5.2 の取得テキストが一部欠けており、膀胱頸部吊り上げ術は直接確認、残りは見出しからの確認。§1.5.2 全文の再確認を推奨する
- RP-068 の治療推奨の細部は抄録と推奨要約での確認（ガイドライン本文は有料）。取り込み側の照合で本文確認を推奨する
- PMCID 補完候補（確認済み、マスターでは null。本カードには記入済み）：SRC-742 → PMC5439293
- 未使用の SRC 番号：SRC-4734〜4800（この回では使わない）

## 5. 引き継ぎメモ

- BA-046 の治療は JAID/JSC 尿道炎ガイドライン（SRC-4722）に基づき、セフトリアキソン 1g 単回点滴静注を第一選択とした（CDC の筋注とは投与経路が異なる）。CM-007 の出典は JIHS 感染症情報提供サイト詳細版（SRC-4721、GOV_JP）
- KT-029 の血圧目標（130 mmHg 未満）は出典の2010年総説の記載で、KDIGO 2021 等の現行目標とは異なる旨を uncertainty に明記した
- KT-030 は診断・鑑別の範囲で、管理・透析適応は出典の範囲外として扱っていない。依頼文の表には管理も含まれていたため、不足なら KDIGO AKI 系での追加が候補
- KF-041 は同じ出典（SRC-665）を使う KX-001 と部分的に重なるため、機序・リンパ浮腫の二次性原因・睡眠時無呼吸との関連など KX-001 にない側面に寄せた
- GU-043（精巣損傷）の出典 EAU ガイドラインでは、血瘤が対側精巣の3倍を超える場合が保存的治療と外科的検索の境界とされる
- GU-040（包茎）の年齢別割合は出典の総説が引用する Oster 1968 コホートの値である旨を uncertainty に明記した
- UR-043（尿道結石）は Morton 2024 の抄録と表で併存結石の割合が異なるため、その数値はカードに入れていない
- 薬剤名のあるカード（CM-007、BA-046、UR-041、UR-042、GY-063、RP-068、RP-069、KT-029 など）は、すべて uncertainty に薬剤名を特定した国内承認・保険適用の注記を入れた（例：バラシクロビルの性器ヘルペス再発抑制は国内承認適応、アシクロビルの同適応は適応外になりうる旨）
