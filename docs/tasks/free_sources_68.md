# 依頼：自由に使える出典の調査（未調査の68枚）

作成：2026-11-23（登録側＝Claude）／依頼者：三原弘／作業：Muse

## 1. 背景と目的

- 11月11日〜15日の調査（バッチ1〜100）で、制限付きの出典（RESTRICTED・UNKNOWN）だけに頼るカードについて、自由に使える資料を1枚ずつ探しました。
- その後に足したカードや、旧形式で調査から漏れていたカードが68枚あります（ES・UG・HP の旧形式カード、医療者教育 ME など）。今回はこの68枚を、同じ方法で調べてください。
- **主張文と数値は変えません。** 成果物は出典の候補だけです。主張の修正が必要だと思われる点は、別欄に書いてください。
- 照合の前に、hm-cmed/cleanroom-facts の最新版を取得してください。

## 2. 探す資料（優先順）

1. **米国連邦政府の資料（GOV_US）**
   - ClinicalTrials.gov の結果登録（Results posted のもの）：試験の主要評価項目の数値。HF の大規模試験（PARADIGM-HF、DAPA-HF、EMPEROR-Preserved、RALES、CARE-HF、SHOCK、IABP-SHOCK II、CULPRIT-SHOCK、DanGer Shock など）と PV の試験（PEITHO、CHEST-1、AMBITION、STELLAR など）は、まずここを確認する。
   - FDA：添付文書（Drugs@FDA の Label）と審査資料（Medical/Statistical Review）。
   - NIH（NHLBI、NCI、NLM の MedlinePlus など）、CDC、AHRQ のエビデンスレポート。
   - 注意：連邦政府の資料でも、中に転載された第三者の図表・文章は自由ではありません（その部分は使わない）。NCBI Bookshelf の収載書籍（StatPearls、GeneReviews など）は政府著作物ではありません。個別のライセンスを確認してください。
2. **日本の公的資料（GOV_JP）**
   - 厚生労働省（通知、検討会資料、患者調査・人口動態統計など）、e-Stat、国立感染症研究所。法令・告示・通知は著作権の対象外です。その他は政府標準利用規約（出典を明記し、加工した旨を示す）で使えます。
   - PMDA の審査報告書・添付文書は、PMDA のサイト利用規約を確認し、確認結果を書いてください（これまで添付文書は UNKNOWN として扱っています）。
   - 公的機関の名前があっても、財団や学会が運営するサイト（難病情報センターなど）は GOV_JP にしません。研究班が作ったガイドライン・診療ガイドは、厚労省のサイトにあっても RESTRICTED です（2026-11-13 の決定）。
   - **国立保健医療科学院（niph.go.jp）の掲載物と、厚生労働科学研究成果データベース（mhlw-grants.niph.go.jp）の研究報告書は、資料そのものに著作権を主張する記載がなければ GOV_JP です（2026-11-15 の決定）。** 日本の疫学・診療実態の数値は、まずここを探してください。
3. **CC BY・CC0 の論文（OPEN）**
   - PMC の Open Access Subset などで、ライセンスが CC BY または CC0 と明示されているもの。CC BY-NC・ND は RESTRICTED です。
4. **現在の出典の再確認**
   - 現在 UNKNOWN の出典（下表の区分を参照）の中には、実際には CC BY のものがあるかもしれません（例：SRC-2481 Ann Ib Postgrad Med）。出版社ページや PMC の表示で確認してください。OPEN と分かれば、それも成果に含めてください。

## 3. 判定と書き方

カードごとに次のどれかで判定してください。

| 判定 | 意味 |
|---|---|
| A 置き換え可 | 自由に使える資料だけで、主張文の全体（数値を含む）が裏づけられる。主出典をその資料に差し替える候補 |
| B 裏づけ追加 | 主張の一部（例：試験の主要評価項目の数値だけ）が裏づけられる。主出典はそのままにして、corroboration に記録する候補 |
| C 見つからない | 探した範囲では見つからなかった。何を探したかを1行で書く |
| D 区分の訂正 | 現在の出典自体が実は OPEN・GOV だった（ライセンス表示の根拠を書く） |

必ず守ること：
- **数値は一致を確認する。** 試験登録の数値は、論文と解析対象や追跡期間が違うことがあります。違えば「不一致」と書き、両方の数値と違う理由（分かれば）を書いてください。カードに合わせて丸めたり、選んだりしないでください。
- **推奨の強さ・向きは、資料の記載どおり。** 強めたり弱めたりしない。
- **識別子（NCT 番号、DOI、PMID、PMCID）は、そのページで確認できたものだけ。** 確認できなければ空欄にする。
- **文章を写さない。** 成果物に書くのは、書誌・識別子・ライセンスの根拠 URL・数値と、どの部分を裏づけるかの短い説明だけ。
- 読み込んだ PDF は、出典台帳の手順どおり Google ドライブの cleanroom-sources に保存し、INTAKE_LOG.md に IN 番号を付けてください。

## 4. 成果物の形式

ファイル名：`free_sources_68_result.md`

1. 判定表

| カード | 判定 | 候補資料（書誌） | 識別子 | 区分とライセンスの根拠 URL | 裏づける部分 | 数値の照合（一致／不一致と両方の値） | 備考 |
|---|---|---|---|---|---|---|---|

2. 新規出典表（SRC 番号は「新規（仮）」。既存マスターとの重複は DOI・PMID・NCT 番号で確かめる）
3. 主張文の修正が必要と思われる点（あれば。修正案ではなく、理由と根拠だけ）
4. 集計（判定ごとの件数）

## 5. 対象カード一覧（2026-11-23 時点）

| カード | 今の出典 | 区分 | 出典の書誌 | 主張文（冒頭） |
|---|---|---|---|---|
| ES-005 | SRC-5202 | RESTRICTED | Lundell LR, et al. Gut 1999 | ロサンゼルス（LA）分類は、粘膜傷害の長さと広がりで重症度を分ける。粘膜ひだの間で連続しない5 mm以下の傷害をA、5 mm超をB、2条以上のひだにまたがり全周の75%未満のものをC、75%以上をDとする。 |
| ES-013 | SRC-5204 | RESTRICTED | Shaheen NJ, et al. ACG Barrett's Esophagus guideline. Am J Gastroenterol 2022;117:559-587 | 米国ACG 2022は、Barrett食道の診断に二つの条件を求める。食道胃接合部より口側の円柱上皮が1 cm以上あること、そして生検で腸上皮化生を認めることである。 |
| ES-014 | SRC-5204 | RESTRICTED | Shaheen NJ, et al. ACG Barrett's Esophagus guideline. Am J Gastroenterol 2022;117:559-587 | ACG 2022は、Barrett食道の癌への進展率を、異形成なし（NDBE）で年0.05〜0.2%程度、低異型度異形成（LGD）で年約0.7%と見積もっている。 |
| ES-016 | SRC-5204 | RESTRICTED | Shaheen NJ, et al. ACG Barrett's Esophagus guideline. Am J Gastroenterol 2022;117:559-587 | ACG 2022は、NDBEのサーベイランス間隔を長さで分けている。3 cm未満は5年ごと、3 cm以上は3年ごとである。 |
| ES-017 | SRC-5204 | RESTRICTED | Shaheen NJ, et al. ACG Barrett's Esophagus guideline. Am J Gastroenterol 2022;117:559-587 | ACGは、Barrett食道の生検について、炎症を制御してから2 cm間隔で4方向から系統的に行う方法（Seattle protocol）を標準としている。 |
| ES-018 | SRC-5206 | UNKNOWN | ACG Clinical Guideline: EoE. Am J Gastroenterol 2025 | EoEは、次の三つがそろったときに診断する。食道の機能障害による症状があること、食道生検で上皮内の好酸球が15個/HPF以上（約60個/mm²）であること、好酸球増多をきたす他の疾患を除外したことである。 |
| ES-019 | SRC-5207 | RESTRICTED | Dellon ES, et al. Updated international consensus diagnostic criteria for eosinophilic eso | 現在の国際診断基準では、PPIが効くことはEoEを除外する理由にならない。PPIはEoEの治療選択肢の一つとして扱われる。 |
| ES-020 | SRC-5208 | RESTRICTED | Clinical and endoscopic characteristics of EoE in Japan: a case-control study | 日本の多施設研究では、上部消化管内視鏡130,013件のうちEoEは66例（0.051%）で、約38%は健診の内視鏡で見つかった。 |
| ES-021 | SRC-5209 | RESTRICTED | Hirano I, et al. Endoscopic assessment of the oesophageal features of eosinophilic oesopha | EoEの典型的な内視鏡所見は、輪状溝、縦走溝、白斑（滲出物）、浮腫で、狭窄を伴うこともある。これらはEREFSで点数化する。 |
| ES-022 | SRC-5206 | UNKNOWN | ACG Clinical Guideline: EoE. Am J Gastroenterol 2025 | EoEの初期治療には、PPI、嚥下させる局所ステロイド、除去食療法の3つがある。治療目標の目安は、組織学的に好酸球15個/HPF未満である。 |
| ES-024 | （なし） | RESTRICTED | デュピクセント 医薬品インタビューフォーム（2026年3月改訂 第20版）、サノフィ国内申請報道 | デュピルマブは米国FDAで2022年5月20日に12歳以上（体重40kg以上）のEoEに承認され、2024年1月に1〜11歳（体重15kg以上）へ適応が拡大された。日本では今回の調査でEoEへの承認の記録を確認できなかった。 |
| ES-034 | SRC-5210 | RESTRICTED | Vaezi MF, et al. ACG clinical guidelines: diagnosis and management of achalasia. Am J Gast | ACG 2020は、III型アカラシアには空気圧拡張術（PD）より有効な治療として、筋切開長を病変に合わせて延ばしたPOEM（tailored POEM）またはLHMを推奨している。III型はLESに限った治療では成績が劣り、長い筋切開が重… |
| ES-057 | SRC-5211 | RESTRICTED | Kaplan DE, et al. AASLD Practice Guidance, portal hypertension and varices. Hepatology 202 | 臨床的に有意な門脈圧亢進症（CSPH）は、肝静脈圧較差（HVPG）10 mmHg以上で定義される。 |
| ES-058 | SRC-5211 | RESTRICTED | Kaplan DE, et al. AASLD Practice Guidance, portal hypertension and varices. Hepatology 202 | Baveno VIIとAASLD 2024は、CSPHのある代償性肝硬変に非選択的β遮断薬（NSBB）を勧めており、カルベジロールを優先する。目的は非代償化の予防にまで及ぶ。 |
| ES-059 | SRC-5211 | RESTRICTED | Kaplan DE, et al. AASLD Practice Guidance, portal hypertension and varices. Hepatology 202 | AASLD 2024は、門脈圧亢進症に用いるNSBBとしてカルベジロールを第一に勧め、維持量を1日6.25〜12.5 mgとしている。 |
| ES-060 | SRC-5211 | RESTRICTED | Kaplan DE, et al. AASLD Practice Guidance, portal hypertension and varices. Hepatology 202 | AASLD 2024は、高リスク静脈瘤の一次予防としてNSBBとEVLの両方を認めるが、NSBBを優先する。EVLは、NSBBを使えない場合に行う。 |
| ES-065 | SRC-5212 | RESTRICTED | García-Pagán JC, et al. NEJM 2010 | 急性静脈瘤出血を起こした高リスクの肝硬変（Child-Pugh C 10〜13点、またはBで活動性出血）では、72時間以内の早期TIPSが標準治療に比べ生存を改善した。 |
| ES-076 | SRC-5213 | RESTRICTED | Kahrilas PJ, et al. Approaches to the diagnosis and grading of hiatal hernia. Best Pract R | 食道裂孔ヘルニアで最も多いのはI型（滑脱型）で、横隔食道膜の弛緩により胃噴門部が縦隔へ脱出する。軸方向のずれが2 cmを超えれば、バリウム造影、内視鏡、内圧検査で診断できる。 |
| ES-077 | SRC-5214 | UNKNOWN | Abdi S, et al. Drug-induced esophagitis and helpful management for healthcare providers. G | 薬剤性食道炎の原因薬には、抗菌薬（テトラサイクリン系、特にドキシサイクリン）、ビスホスホネート、NSAIDs、塩化カリウム、鉄剤などがある。症状は胸骨後部痛、胸やけ、嚥下痛、嚥下障害で、多くは原因薬の中止と支持療法で改善する。 |
| ES-078 | SRC-5215 | UNKNOWN | Chen YH, et al. Prevalence and risk factors for Candida esophagitis among human immunodefi | 台湾の健診受診者（HIV陰性）11,802例では、生検で確認したカンジダ食道炎は0.4%だった。多変量解析での独立した危険因子は、高齢、慢性腎臓病、飲酒、ステロイド使用だった。 |
| ES-084 | SRC-5218 | UNKNOWN | Mertens A, et al. A systematic analysis of incidence, therapeutic strategies, and in-hospi | Mallory-Weiss症候群（嘔吐などによる食道胃接合部の粘膜裂創）は多くが自然に止血し、緊急の内視鏡治療を要しないことが多い。ドイツの全国入院データ（2010〜2019年、59,291例）では、内視鏡的止血は局注13.7%、クリップ1… |
| ES-088 | SRC-5209 | RESTRICTED | Hirano I, et al. Endoscopic assessment of the oesophageal features of eosinophilic oesopha | EREFSは、EoEの4つの主要な内視鏡所見（浮腫、輪状溝、白斑、縦走溝）と追加所見（狭窄、crepe paper esophagus）を等級化する分類である。修正版では、主要4所見の観察者間一致はκ 0.40〜0.54と良好だった。 |
| ES-091 | （なし） | UNKNOWN | 慶應義塾大学病院 KOMPAS 好酸球性消化管疾患（2024年5月） | 日本では、局所ステロイド（嚥下するブデソニドやフルチカゾン）を含め、EoEを効能とする保険適用薬は2024年時点で存在しない。 |
| HP-002 | SRC-5220 | UNKNOWN | Murakami K et al. Gut 2016;65:1439-46 | 日本の第III相二重盲検RCTでは、一次除菌（三剤）の除菌率がボノプラザン群92.6%、ランソプラゾール群75.9%だった。 |
| HP-003 | （なし） | UNKNOWN | Murakami 2016 原著本文（PMC5036253、online supplementary table S1参照）; Frontiers Pharmacol 2018 ( | 同じRCTのCAM耐性株感染例では、除菌率がボノプラザン三剤で82.0%、ランソプラゾール三剤で40.0%だった（p<0.0001）。 |
| HP-008 | SRC-5221 | RESTRICTED | Malfertheiner P et al. Gut 2022;71:1724-62 | 欧州のMaastricht VI/Florenceコンセンサスは、感受性が不明な場合やCAM耐性率が15%を超える地域では、経験的一次治療として14日間のビスマス4剤療法を推奨している。 |
| HP-009 | SRC-5222 | RESTRICTED | Chey WD et al. Am J Gastroenterol 2024;119:1730-53（要旨はJCAG誌の解説（CC BY）経由） | 米国ACG 2024は、未治療例の選択肢として最適化ビスマス4剤療法を優先し、感受性が確認されない限りCAMやレボフロキサシンを含むレジメンは避けるよう求めている。 |
| HP-012 | SRC-5222 | RESTRICTED | ACG 2024（Emory大学の要約資料経由） | 除菌判定の検査前には、PPIを2週間以上、ビスマスと抗菌薬を4週間以上中止し、治療終了から4週間以上あけて判定する。 |
| HP-014 | （なし） | UNKNOWN | Yoshii S et al. Dig Endosc 2020;32:74-83（JSHR GL 2024で引用） | 京都分類に基づく内視鏡所見のうち、現感染を最も強く示すのはびまん性発赤（診断オッズ比26.8）で、粘膜腫脹13.3、白濁粘液10.2、皺襞腫大8.6が続く。 |
| HP-017 | SRC-5225 | RESTRICTED | Sugano K et al. Gut 2015;64:1353-67 | 京都グローバルコンセンサスは、H. pylori胃炎を症状の有無にかかわらず感染症として位置づけた。 |
| HP-018 | （なし） | UNKNOWN | 厚労省 患者調査2023（JSGE PUD GL 2026の序論で引用） | 日本の胃潰瘍患者数は2023年に年間19.4万人、十二指腸潰瘍は2.0万人まで減少し、40年前と比べるとそれぞれ約10分の1、約20分の1になった。 |
| HP-020 | （なし） | RESTRICTED | JSHR GL 2024（除菌適応疾患の一覧）／Maastricht VI | H. pylori陽性の限局期胃MALTリンパ腫では、除菌療法が一次治療として位置づけられている。 |
| HS-001 | SRC-2641 | RESTRICTED | 厚生労働科学研究費補助金（エイズ対策政策研究事業）研究班. 救急領域における止血機能異常症の診療ガイド 第2版（ITPの章）. 厚生労働省研究成果公開ページ掲載PDF. | 免疫性血小板減少症（ITP）に疾患特異的な診断法はなく、他の原因による血小板減少を除外して診断する。病期は、診断後3か月以内を新規診断、3〜12か月を持続性、12か月以上を慢性と分類する。出血症状は一般に血小板数が5万/µL以下で明らかにな… |
| HS-004 | SRC-2641 | RESTRICTED | 厚生労働科学研究費補助金（エイズ対策政策研究事業）研究班. 救急領域における止血機能異常症の診療ガイド 第2版（ITPの章）. 厚生労働省研究成果公開ページ掲載PDF. | 成人のITPでHelicobacter pylori感染があれば除菌療法を行い、約半数の症例で血小板数の増加が得られる。除菌で血小板数が2〜3万/µL以上に回復しない場合に副腎皮質ステロイドを開始する。治療目標は血小板数の正常化ではなく、重… |
| ME-008 | SRC-5111 | RESTRICTED | Ende J. Feedback in clinical medical education. JAMA. 1983;250(6):777-781 | 臨床教育におけるフィードバックとは、教育者が学習者の臨床場面での行動を観察し、その観察に基づいて学習者へ情報を返すことで、学習者がその後の実践で自らの行動を改善していけるよう支える働きをいう。フィードバックは臨床技能の修得に欠かせない過程で… |
| ME-009 | SRC-5112 | RESTRICTED | McGaghie WC, Issenberg SB, Cohen ER, Barsuk JH, Wayne DB. Does simulation-based medical ed | 意図的練習（deliberate practice）を組み込んだシミュレーション基盤型の医学教育は、従来型の臨床教育と比べて、臨床技能の習得アウトカムで優れることがメタ解析で示されている。1990年から2010年までの文献を対象とし、組み入… |
| ME-010 | SRC-5113 | RESTRICTED | ABIM Foundation, ACP-ASIM Foundation, European Federation of Internal Medicine. Medical pr | 医師憲章（Medical professionalism in the new millennium: a physician charter）は、医師のプロフェッショナリズムを、患者の福利の最優先、患者の自律、社会正義の3つの基本原則と、… |
| ME-012 | SRC-5116 | RESTRICTED | van der Vleuten CPM, Schuwirth LWT, Driessen EW, Dijkstra J, Tigelaar D, Baartman LKJ, van | プログラム的評価は、評価を個々の試験としてではなく、学習の過程全体にわたるプログラムとして設計する考え方である。個々の評価の機会（データポイント）は、それ自体では進級や合否のような重大な判定には用いず、学習とフィードバックの価値を最大化する… |
| ME-013 | SRC-5117 | RESTRICTED | Issenberg SB, McGaghie WC, Petrusa ER, Lee Gordon D, Scalese RJ. Features and uses of high | 高忠実度シミュレーションを用いた医学教育について、1969年から2003年までの文献を対象としたBEME系統的レビューでは、初めの670件の論文から、シミュレーターを教育介入として用い学習成果を定量的に測った実証研究109件が選ばれ、学習効… |
| ME-014 | SRC-5118 | RESTRICTED | Albanese MA, Mitchell S. Problem-based learning: a review of literature on its outcomes an | 問題基盤型学習（PBL）のアウトカムについて、1972年から1992年までの英語文献を統合したレビューでは、アウトカムごとに方向の異なる結果が報告された。臨床面では、PBLの卒業生は従来型の教育の卒業生と同等か、臨床試験や教員による評価では… |
| ME-016 | SRC-5120 | RESTRICTED | Cook DA, Levinson AJ, Garside S, Dupras DM, Erwin PJ, Montori VM. Internet-based learning  | 医療専門職教育におけるインターネット基盤学習の効果を統合したメタ解析（対象201件の研究）では、比較の相手によって効果の大きさが大きく異なった。教育介入のない場合との比較では効果が大きく、知識で効果量1.00（95%信頼区間 0.90〜1.… |
| ME-017 | SRC-5121 | RESTRICTED | Steinert Y, Mann K, Centeno A, Dolmans D, Spencer J, Gelula M, Prideaux D. A systematic re | 医学教育における教員育成（FD：ファカルティ・ディベロップメント）の取り組みについて、1980年から2002年までの文献を対象としたBEME系統的レビューでは、初めの2,777件の抄録から53件の研究（無作為化比較試験6件、準実験的研究47… |
| ME-018 | SRC-5122 | RESTRICTED | Rotenstein LS, Ramos MA, Torre M, Segal JB, Peluso MJ, Guille C, Sen S, Mata DA. Prevalenc | 医学生のうつ病・抑うつ症状と自殺念慮の有病率について、43か国の研究を統合した系統的レビュー・メタ解析では、抑うつ症状の有病率は27.2%（95%信頼区間 24.7〜29.9%）と推定された（横断研究167件・対象116,628人と、縦断研… |
| ME-019 | SRC-5123 | RESTRICTED | West CP, Dyrbye LN, Erwin PJ, Shanafelt TD. Interventions to prevent and reduce physician  | 医師の燃え尽き（バーンアウト）に対する介入の効果について、無作為化試験15件（医師716人）とコホート研究37件（医師2,914人）を統合した系統的レビュー・メタ解析では、介入後に燃え尽き全体を示す割合が54%から44%へ下がった（差10ポ… |
| ME-022 | SRC-5130 | RESTRICTED | Driessen E, van Tartwijk J, van der Vleuten C, Wass V. Portfolios in medical education: wh | ポートフォリオ（学習の記録や省察を蓄積するファイル）を医学教育で用いることの効果について、文献データベース等から得られた1,939件のうち実証研究30件を対象とした系統的レビューでは、効果の報告は一様ではなかった。肯定的な効果が最も強く示さ… |
| ME-023 | SRC-5131 | RESTRICTED | Fatmi M, Hartling L, Hillier T, Campbell S, Oswald AE. The effectiveness of team-based lea | チーム基盤型学習（TBL）は、学習者が事前に学習したうえで、個人テスト（iRAT）、チームテスト（tRAT）、応用演習の順に進める能動学習法で、他の能動学習法に比べて教員の負担が少ないとされる。保健医療職教育におけるTBLの学習成果への効果… |
| ME-024 | SRC-5132 | RESTRICTED | World Health Organization. Patient Safety Curriculum Guide: Multi-professional Edition. Ge | 世界保健機関（WHO）は2011年、医療専門職の学校教育で患者安全を教えるための「患者安全カリキュラムガイド（多職種版）」を公表した。対象は医学・歯学・助産・看護・薬学の学生であり、すべての医療専門職の継続的な研修にも使える構成とされている… |
| ME-025 | SRC-5133 | RESTRICTED | World Health Organization. Framework for Action on Interprofessional Education and Collabo | 多職種連携教育（IPE）は、異なる職種の学習者が、互いの職種の役割や専門性を理解し合い、将来チームで協働して働くための準備をする教育の進め方を指す。世界保健機関（WHO）は2010年、「多職種連携教育と協働実践のための行動枠組み」を公表し、… |
| ND-041 | SRC-1687 | RESTRICTED | 難病情報センター. 脊髄小脳変性症（多系統萎縮症を除く）（指定難病 18）概要・診断基準等 | 日本における脊髄小脳変性症の患者は約3万人と推定され、その約2/3が孤発性、約1/3が遺伝性である。孤発性の大多数は多系統萎縮症であり、遺伝性ではMachado-Joseph病（SCA3）、SCA6、SCA31、DRPLAが日本で頻度の高い… |
| ND-049 | SRC-1694 | RESTRICTED | 難病情報センター. 球脊髄性筋萎縮症（指定難病 1）概要・診断基準等 | 球脊髄性筋萎縮症（Kennedy病）は、X染色体上のアンドロゲン受容体遺伝子第1エクソンにあるCAGリピートが38回以上に異常伸長すること（正常は36以下）で生じ、通常は成人男性に発症する遺伝性の下位運動ニューロン疾患であり、女性は保因者と… |
| NI-006 | SRC-1636 | RESTRICTED | 厚生労働科学研究費補助金難治性疾患政策研究事業「プリオン病及び遅発性ウイルス感染症に関する調査研究班」、厚生労働行政推進調査事業費補助金「プリオン病のサーベイランスと感染予防に関す | 変異型 Creutzfeldt-Jakob 病は孤発性 CJD と異なり、精神症状で発症して認知機能障害は初期には目立たず、痛みや異常感覚などの感覚障害を早期に呈し、経過が長く、頭部 MRI の T2 強調画像・FLAIR 画像で両側対称性… |
| NI-007 | SRC-1637 | RESTRICTED | 厚生労働科学研究費補助金「プリオン病及び遅発性ウイルス感染症に関する調査研究班」ほか. プリオン病感染予防ガイドライン2020. 2020 | プリオンは通常の滅菌・消毒に抵抗性を示すため、プリオン病患者のハイリスク手技に用いた手術器具には、十分な洗浄のうえプレバキューム式高圧蒸気滅菌 134℃・18 分間など、通常より強力な専用の不活性化処理が必要である。 |
| UG-001 | SRC-5226 | RESTRICTED | Laine L et al. Am J Gastroenterol 2021;116:899-917 | 救急外来を受診した上部消化管出血のうち、院内での介入または死亡の見逃し率が1%以下となる超低リスク例（例：Glasgow-Blatchfordスコア0〜1）は、入院させず外来フォローで帰宅させることが提案されている。 |
| UG-002 | SRC-5226 | RESTRICTED | ACG 2021 | GBS 0の感度の点推定値は99〜100%だが、特異度は8〜22%と低い。 |
| UG-003 | SRC-5226 | RESTRICTED | ACG 2021 | 上部消化管出血の入院患者では、Hb 7 g/dLを閾値とする制限輸血が提案されている。 |
| UG-004 | （なし） | RESTRICTED | Villanueva C et al. N Engl J Med 2013;368(1):11-21（ACG 2021が引用） | 閾値7 g/dLの根拠となった上部消化管出血のRCT（単施設、n=921：制限群461例＜7 g/dL、非制限群460例＜9 g/dL）では、輸血を受けた患者の割合が制限群49%、非制限群86%（P<0.001）で、45日死亡率は5% vs… |
| UG-005 | SRC-5226 | RESTRICTED | ACG 2021 | システマティックレビューでは、制限輸血によって輸血を受ける患者数が43%減り、臨床的に重要な転帰の悪化は認められなかった。 |
| UG-006 | （なし） | RESTRICTED | JGES NVUGIB GL 第2版（強い推奨）、ESGE 2021、ACG 2021 | 非静脈瘤性上部消化管出血では、循環動態を安定させた後、24時間以内に上部内視鏡を行うことが推奨される。 |
| UG-007 | SRC-4966 | RESTRICTED | JGES NVUGIB GL 第2版 | 上部消化管出血が疑われる患者に、スクリーニング目的で経鼻胃管をルーチンに挿入することは推奨されない。 |
| UG-008 | （なし） | UNKNOWN | ESGE 2015/2021、ESGE 2026 | 重症または活動性出血が続く上部消化管出血では、内視鏡の30〜120分前にエリスロマイシン250 mgを単回静注することが推奨される。 |
| UG-009 | （なし） | RESTRICTED | ESGE 2015 (10.1055/s-0034-1393172)、ACG 2021 | Forrest分類のIa（噴出性出血）、Ib（湧出性出血）、IIa（露出血管）は高リスク所見で内視鏡的止血の対象となる。IIc（平坦な色素斑）とIII（清浄潰瘍底）は再出血リスクが低く、止血処置を要しない。 |
| UG-010 | SRC-5227 | RESTRICTED | ESGE 2026（PubMed抄録 PMID 42127996） | ESGE 2026は、高リスク所見（FIa・FIb）の消化性潰瘍出血に対し、再出血がより少ないことから、over-the-scope（OTS）クリップ単独を従来の併用療法に代わる一次治療として提案している。 |
| UG-011 | （なし） | RESTRICTED | ESGE 2021／ACG 2021 | エピネフリン局注のみによる止血は不十分で、他の止血法と併用すべきである。 |
| UG-014 | SRC-5226 | RESTRICTED | ACG 2021（Emory大学の要約資料経由） | 内視鏡治療を行った高リスク潰瘍出血では、高用量PPI（1日80 mg以上）を3日間投与した後、2週間は1日2回のPPIを続けることが提案されている。 |
| UG-015 | SRC-5227 | RESTRICTED | ESGE 2026 | ESGE 2026は、再出血例にはOTSクリップでの再止血を考慮し、それも不成功なら経カテーテル動脈塞栓術（TAE）、TAEができない・不成功なら手術という順序を推奨している。 |
| UG-016 | SRC-5229 | UNKNOWN | ESGE 2015 | 心血管疾患の二次予防として低用量アスピリンを服用中の患者が消化性潰瘍出血を起こした場合、再出血リスクが低ければ、内視鏡直後からアスピリンを再開することが推奨される。 |
| UG-017 | SRC-5227 | RESTRICTED | ESGE 2026 | 抗凝固療法の継続が必要な患者では、血栓塞栓リスクに応じて、臨床的に可能になった時点でできるだけ早く抗凝固薬を再開することが推奨される。 |
| UG-018 | SRC-5227 | RESTRICTED | ESGE 2026 | 持続的な止血が得られた消化性潰瘍出血では、止血後24時間以内に経口摂取を始め、鉄欠乏や貧血があれば退院前に鉄補充を開始することが提案されている。 |
