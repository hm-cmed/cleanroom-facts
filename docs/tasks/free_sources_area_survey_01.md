# 依頼：自由に使える出典の分野ごとの再調査（第1回：OS・SD・ST・PG）

作成：2026-11-24（登録側＝Claude）／依頼者：三原弘／作業：Muse

## 1. 背景と目的

- 11月11日〜15日の調査（バッチ1〜100）では、制限付きの出典（RESTRICTED・UNKNOWN）だけに頼るカードについて、カードを1枚ずつ調べました。
- その結果の多くは、PubMed の抄録を根拠にした A・B でした。PubMed の抄録は論文の著者の文章なので、**論文自体が CC BY でない限り使わない**ことにしています（2026-11-11 の判断）。このため、自由に使える裏づけのないカードが、今も全体で約1,550枚あります。
- 今回は探し方を変えます。カードを1枚ずつ見る前に、**分野ごとに「自由に使える資料の地図」を先に作り**、その地図からカードに当てはめてください。
- その後に自由に使える資料として扱えるようになったものが3種類あります。前回の調査では、ほとんど探していません。
  1. 厚生労働科学研究成果データベース（mhlw-grants.niph.go.jp）の研究報告書。資料に著作権を主張する記載（©、無断転載禁止など）がなければ GOV_JP（2026-11-15 の決定）。
  2. 研究班の診療ガイド・ガイドラインのうち、このデータベースに報告書の添付資料として載り、資料に権利表記がないもの。GOV_JP（2026-11-24 の決定。例：SRC-2641）。
  3. 地方自治体（都道府県・市町村、その公的な相談機関など）の公開資料。GOV_JP（2026-11-24 の決定。例：SRC-5240 大阪市、SRC-5241 兵庫県難病相談センター）。
- **主張文と数値は変えません。** 成果物は出典の候補だけです。主張の修正が必要だと思われる点は、別欄に書いてください。
- 作業の前に、hm-cmed/cleanroom-facts の最新版を取得してください。

## 2. 対象の分野と、対象カードの選び方

今回の対象は、自由に使える裏づけのないカードの割合が高い次の4分野です（2026-11-24 時点、退役カードを除く）。

| 接頭辞 | 分野 | カード数 | 自由な裏づけなし | 割合 | 前回の調査結果 |
|---|---|---|---|---|---|
| OS | 上肢・下肢の運動器疾患、非感染性骨・関節・四肢軟部疾患 | 50 | 45 | 90% | proposals/pd_survey_20261111/batch17_os.md |
| SD | その他の皮膚疾患 | 61 | 54 | 89% | batch11_sd.md |
| ST | 脳血管障害 | 51 | 44 | 86% | batch15_st.md |
| PG | 妊娠の異常 | 47 | 39 | 83% | batch18_pg.md |

**対象カードは、最新版のレポジトリから自分で選んでください。** 条件は次の3つをすべて満たすカードです。

1. `publication_info.status` が retired でない。
2. `provenance.source_class` が RESTRICTED または UNKNOWN。
3. `provenance.corroboration` に、自由に使える資料の記録（OPEN・GOV_JP・GOV_US・CC BY 4.0・CC0・「自由に使える」のいずれかの語）がない。

付録に、登録側で同じ条件で選んだ一覧（182枚）を付けます。自分で選んだ結果と食い違ったら、その旨を書いてください。

次の回で、DT（皮膚腫瘍）・OT（耳）・PE（小児外科）・RP（月経・不妊）を同じ方法で依頼する予定です。

## 3. 進め方

### 3-1. 先に、分野ごとの資料の地図を作る

分野ごとに、自由に使える資料の候補を一覧にしてください。カードとの当てはめはまだしません。

1. **すでに出典の一覧にあるものを先に使う。** `data/sources/sources.yaml`（約2,540件）の OPEN・GOV_JP・GOV_US の出典のうち、その分野に使えそうなものを挙げてください。他の章のカードに使った出典でもかまいません。
2. **厚生労働科学研究成果データベース（mhlw-grants.niph.go.jp）**：分野の疾患名で検索し、研究報告書（総括・分担）と添付資料を探す。疫学の数値・日本の診療の実態・診断基準・研究班の診療ガイドが見つかりやすい。権利表記の有無は、資料ごとに確かめてください。
3. **国立保健医療科学院（niph.go.jp）**：機関誌『保健医療科学』の論文など。
4. **厚生労働省・こども家庭庁・文部科学省など**：検討会の資料、通知、統計（人口動態統計、患者調査、衛生行政報告例など）、指定難病の「概要、診断基準等」。
5. **地方自治体**：都道府県・市町村、保健所、難病相談支援センターなどの公開資料。
6. **米国連邦政府の資料（GOV_US）**：分野ごとの研究所を優先してください。
   - OS：NIAMS、NIH の MedlinePlus、AHRQ
   - SD：NIAMS、CDC、MedlinePlus
   - ST：NINDS、NHLBI、CDC（脳卒中）、ClinicalTrials.gov の結果登録（Results posted）
   - PG：NICHD、CDC（妊娠・周産期）、FDA、ClinicalTrials.gov の結果登録
7. **CC BY・CC0 の論文（OPEN）**：PMC の Open Access Subset などで、ライセンスが CC BY または CC0 と明示されているもの。CC BY-NC・ND・SA は RESTRICTED です。日本の学会の英語版ガイドラインは、CC BY のことがあります（例：SRC-049）。1件ずつ確かめてください。

### 3-2. 次に、地図からカードに当てはめる

- 地図の資料ごとに、どのカードのどの部分を裏づけるかを当てはめてください。
- 前回の調査で C（見つからない）だったカードも、新しい種類の資料で見直してください。

## 4. 使わないもの（これまでと同じ判断）

- **PubMed の抄録。** 論文自体が CC BY・CC0 でなければ使いません。前回の「先例 A」も同じです。
- 米国の添付文書（DailyMed）や、日本の添付文書（製薬会社の作成）。
- 難病情報センター（公益財団法人 難病医学研究財団）のページ、研究班が学会誌や自前のサイトで刊行し、権利表記があるガイドライン。
- NCBI Bookshelf の収載書籍（StatPearls、GeneReviews など）。政府著作物ではありません。個別のライセンスを確かめて、CC BY でなければ使いません。
- 連邦政府・日本の公的資料の中に転載された、第三者の図表や文章。

## 5. 判定と書き方

カードごとに次のどれかで判定してください（前回と同じ）。

| 判定 | 意味 |
|---|---|
| A 置き換え可 | 自由に使える資料だけで、主張文の全体（数値を含む）が裏づけられる。主出典をその資料に差し替える候補 |
| B 裏づけ追加 | 主張の一部が裏づけられる。主出典はそのままにして、corroboration に記録する候補 |
| C 見つからない | 探した範囲では見つからなかった。何を探したかを1行で書く |
| D 区分の訂正 | 現在の出典自体が実は OPEN・GOV だった（ライセンス表示の根拠を書く） |

必ず守ること：
- **数値は一致を確かめる。** 日本の報告書と海外の資料では、対象・年次・定義が違うことがあります。違えば「不一致」と書き、両方の数値と違う理由（分かれば）を書いてください。カードに合わせて丸めたり、選んだりしないでください。
- **推奨の強さ・向きは、資料の記載どおり。** 強めたり弱めたりしない。
- **識別子（NCT 番号、DOI、PMID、PMCID、mhlw-grants の研究課題番号）は、そのページで確かめたものだけ。** 確かめられなければ空欄にする。
- **権利表記の確認結果を書く。** mhlw-grants の資料と自治体の資料は、資料ごとに「権利表記なし」「© あり」などを書いてください。確認したページの URL も書いてください。
- **文章を写さない。** 成果物に書くのは、書誌・識別子・ライセンスの根拠 URL・数値と、どの部分を裏づけるかの短い説明だけ。
- 読み込んだ PDF は、出典台帳の手順どおり Google ドライブの cleanroom-sources に保存し、INTAKE_LOG.md に IN 番号を付けてください。

## 6. 成果物の形式

ファイル名：`free_sources_area_01_result.md`（4分野を1つのファイルにまとめる）

1. 分野ごとの資料の地図

| 分野 | 資料（書誌） | 種類（mhlw-grants・自治体・省庁・GOV_US・OPEN・既存マスター） | 識別子・URL | 区分と権利表記の確認結果 | 使えそうなカード |
|---|---|---|---|---|---|

2. 判定表（前回の free_sources_68_result.md と同じ形式）

| カード | 判定 | 候補資料（書誌） | 識別子 | 区分とライセンスの根拠 URL | 裏づける部分 | 数値の照合（一致／不一致と両方の値） | 備考 |
|---|---|---|---|---|---|---|---|

3. 新規出典表（SRC 番号は「新規（仮）」。既存マスターとの重複は DOI・PMID・NCT 番号・URL で確かめる）
4. 主張文の修正が必要と思われる点（あれば。修正案ではなく、理由と根拠だけ）
5. 集計（分野ごと・判定ごとの件数と、資料の種類ごとの件数）
6. 次の回（DT・OT・PE・RP）への申し送り：効いた資料の種類と、効かなかった種類

## 付録：対象カードの一覧（登録側の抽出、2026-11-24、182枚）


### OS

| カード | 今の出典 | 区分 | 出典の書誌（冒頭） | 主張文（冒頭） |
|---|---|---|---|---|
| OS-001 | SRC-1846 | RESTRICTED | Aletaha D, Neogi T, Silman AJ, et al. 2010 Rheumatoid arthri | 関節リウマチの2010年ACR/EULAR分類基準は、少なくとも1関節に他の疾患では説明できない滑膜炎があることを前提に… |
| OS-002 | SRC-1847 | RESTRICTED | Harigai M, Kaneko Y, Tanaka E, et al. 2024 Update of the Jap | 日本の関節リウマチ診療ガイドライン2024年改訂版では、治療目標と薬物治療アルゴリズムは2020年版から変更されず、メト… |
| OS-003 | SRC-1848 | RESTRICTED | Smolen JS, Landewé RBM, Bergstra SA, et al. EULAR recommenda | EULARの2022年改訂推奨では、関節リウマチの治療は臨床的寛解（到達が困難な場合は低疾患活動性）を目標とする tre… |
| OS-004 | SRC-1849 | RESTRICTED | van der Heijde D. How to read radiographs according to the S | 関節リウマチの関節破壊の進行は、手と足の単純X線写真でびらんと関節裂隙狭小化を半定量的に採点する Sharp スコアの … |
| OS-005 | SRC-992 | RESTRICTED | FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American Col | 急性痛風関節炎の確定診断は、関節液の偏光顕微鏡検査で針状で負の複屈折を示す尿酸一ナトリウム（MSU）結晶を同定することで… |
| OS-006 | SRC-992 | RESTRICTED | FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American Col | 急性痛風関節炎の治療の第一選択はNSAIDs、コルヒチン、糖質コルチコイド（経口・関節内・筋注）のいずれかであり、コルヒ… |
| OS-007 | SRC-1850 | RESTRICTED | Abhishek A, Tedeschi SK, Pascart T, et al. The 2023 ACR/EULA | 偽痛風の原因であるピロリン酸カルシウム（CPP）結晶は、偏光顕微鏡で菱形で正の複屈折を示し、尿酸一ナトリウム結晶（針状・… |
| OS-008 | SRC-1851 | RESTRICTED | Reilly D, Kamineni S. Olecranon bursitis. J Shoulder Elbow S | 肘頭滑液包炎では、発熱、発赤、熱感などの感染徴候の有無が感染性と非感染性の鑑別の手がかりとなり、確定には滑液包穿刺液のグ… |
| OS-009 | SRC-1852 | RESTRICTED | Peters-Veluthamaningal C, van der Windt DA, Winters JC, Meyb | ばね指は手指屈筋腱のA1プーリー部における狭窄性腱鞘炎で、指の引っかかりや弾発現象、進行するとロッキングを呈し、治療では… |
| OS-010 | SRC-1853 | RESTRICTED | Ilyas AM, Ast M, Schaffer AA, Thoder J. De quervain tenosyno | de Quervain病は手関節橈側の第一伸筋区画（長母指外転筋・短母指伸筋腱）の狭窄性腱鞘炎で、母指の使用で増悪する橈… |
| OS-012 | SRC-1855 | RESTRICTED | Bannuru RR, Osani MC, Vaysbrot EE, et al. OARSI guidelines f | 変形性関節症の非手術管理の中核は患者教育、運動療法、過体重例での減量であり、その上に外用・経口NSAIDsなどの薬物療法… |
| OS-013 | SRC-1856 | RESTRICTED | Rogers LC, Frykberg RG, Armstrong DG, et al. The Charcot foo | 神経病性関節症（Charcot関節）の代表である糖尿病性Charcot足は、末梢神経障害を背景に炎症、外傷、骨代謝の異常… |
| OS-014 | SRC-1857 | RESTRICTED | Srivastava A, Santagostino E, Dougall A, et al. WFH Guidelin | 血友病性関節症は、関節内出血の反復により滑膜炎と軟骨・骨の破壊が進行する病態で、同一関節に出血を繰り返す標的関節が問題と… |
| OS-015 | SRC-1858 | RESTRICTED | Gude W, Morelli V. Ganglion cysts of the wrist: pathophysiol | 手関節のガングリオンは背側（舟状月状関節部）に最も多く、約50%は自然に消退し、穿刺吸引は再発が多く、手術摘出は再発率が… |
| OS-017 | SRC-1860 | RESTRICTED | Schett G, Lories RJ, D'Agostino MA, et al. Enthesitis: from  | 腱付着部炎（enthesitis）は腱や靱帯の骨への付着部の炎症で、脊椎関節炎の中心的病変と位置づけられ、付着部への機械… |
| OS-018 | SRC-1861 | RESTRICTED | Cross D, Matullo KS. Kienböck disease. Orthop Clin North Am. | Kienböck病は月状骨の無腐性壊死で、病期は単純X線とMRIによる Lichtman 分類で評価され、月状骨の硬化の… |
| OS-019 | SRC-1862 | RESTRICTED | Karim AR, Cherian JJ, Jauregui JJ, et al. Osteonecrosis of t | 特発性膝骨壊死（自然発症膝骨壊死）は、高齢女性に多く、大腿骨内側顆に好発し、安静時・夜間に増悪する急激な膝痛で発症するの… |
| OS-021 | SRC-1864 | RESTRICTED | Hutchinson DT, Rane AA, Montanez A. The Natural History of P | 強剛母指（小児の母指ばね指）は、乳幼児にみられる母指IP関節の屈曲位拘縮で、MP関節部掌側に Notta 結節と呼ばれる… |
| OS-022 | SRC-1865 | RESTRICTED | Burkhart SS, De Beer JF. Traumatic glenohumeral bone defects | 肩関節の反復性前方脱臼では、前下方関節唇の剥離である Bankart 病変に加え、関節窩の骨欠損（inverted-pe… |
| OS-023 | SRC-1866 | RESTRICTED | Illig KA, Donahue D, Duncan A, et al. Reporting standards of | 胸郭出口症候群は、腕神経叢や鎖骨下動静脈が胸郭出口で圧迫される病態で、神経性が最も多く静脈性・動脈性がこれに続き、診断で… |
| OS-024 | SRC-1867 | RESTRICTED | Bisset L, Beller E, Jull G, et al. Mobilisation with movemen | 上腕骨外側上顆炎（テニス肘）は、抵抗下の手関節背屈で外側上顆部に疼痛が誘発されることを特徴とし、治療ではステロイド注射が… |
| OS-025 | SRC-1871 | RESTRICTED | Ramirez J. Adhesive Capsulitis: Diagnosis and Management. Am | 凍結肩（癒着性関節包炎）は、疼痛と肩関節可動域の低下（特に外旋制限）を特徴とし、疼痛が前景の時期から回復期へ移行する1〜… |
| OS-026 | SRC-1872 | RESTRICTED | Rangan A, Brealey SD, Keding A, et al. Management of adults  | 二次医療に紹介された原発性凍結肩の成人では、麻酔下授動術、関節鏡視下関節包切開、ステロイド注射を併用する早期の体系的理学… |
| OS-027 | SRC-1873 | RESTRICTED | Yamamoto A, Takagishi K, Osawa T, et al. Prevalence and risk | 日本の一般住民を対象とした健診（平均年齢57.9歳、1,366肩）では、全層腱板断裂の有病率は20.7%で加齢とともに増… |
| OS-028 | SRC-1874 | RESTRICTED | Kukkonen J, Ryösä A, Joukainen A, et al. Operative versus co | 55歳を超える患者の小さい非外傷性棘上筋断裂では、腱板修復術・肩峰形成術・理学療法の併用群と理学療法のみの群の間で、平均… |
| OS-029 | SRC-1875 | RESTRICTED | Krul M, van der Wouden JC, Kruithof EJ, et al. Manipulative  | 肘内障は、腕を急に引かれるなどして橈骨頭が輪状靱帯を越えて亜脱臼する病態で、7歳未満の幼児に起こり、患肢の急性の疼痛と機… |
| OS-030 | SRC-1875 | RESTRICTED | Krul M, van der Wouden JC, Kruithof EJ, et al. Manipulative  | 肘内障の整復手技では、過回内法（hyperpronation）は回外・屈曲法に比べて初回試行での整復失敗が少なかった（失… |
| OS-031 | SRC-1876 | RESTRICTED | Jingushi S, Ohfuji S, Sofue M, et al. Osteoarthritis hip joi | 日本の変形性股関節症では寛骨臼形成不全の関与が大きく、全国調査の OA 関節（720関節）では形成不全の各指標が対照関節… |
| OS-032 | SRC-1877 | RESTRICTED | Learmonth ID, Young C, Rorabeck C. The operation of the cent | 人工股関節全置換術は、関節症で障害された患者の治療として良好な長期成績が確立した手術であり、セメント固定・セメントレス固… |
| OS-033 | SRC-1878 | RESTRICTED | Ömeroğlu H, Yüksel S, Demir P, et al. An Eastern Europe and  | 歩行開始前の発育性股関節形成不全では、Ortolani テスト、Barlow テストと股関節の開排制限が最も重要な身体所… |
| OS-034 | SRC-1878 | RESTRICTED | Ömeroğlu H, Yüksel S, Demir P, et al. An Eastern Europe and  | 発育性股関節形成不全の装具治療では Pavlik ハーネス（リーメンビューゲル）が第一選択の装具であり、Graf 分類 … |
| OS-035 | SRC-1879 | RESTRICTED | Funk JF, Lebek S. Epiphyseolysis capitis femoris: new aspect | 大腿骨頭すべり症は思春期に起こり、BMI の高い小児で発生が増え、両側性に起こることが多い。診察では Drehmann … |
| OS-036 | SRC-1880 | RESTRICTED | Fukushima W, Fujioka M, Kubo T, et al. Nationwide epidemiolo | 日本の特発性大腿骨頭壊死症の全国疫学調査（2005年、臨床情報1,502例）では、年齢分布のピークは40歳代で、関連因子… |
| OS-037 | SRC-1881 | RESTRICTED | Ando W, Sakai T, Fukushima W, et al. Japanese Orthopaedic As | 特発性大腿骨頭壊死症診療ガイドライン2019（厚生労働省研究班・日本整形外科学会）では、治療法として保存療法、骨移植・細… |
| OS-038 | SRC-1882 | RESTRICTED | Herring JA, Kim HT, Browne R. Legg-Calve-Perthes disease. Pa | Perthes 病では、発症時年齢と lateral pillar 分類が骨成熟時の転帰と強く相関する予後因子であり、8… |
| OS-039 | SRC-1883 | RESTRICTED | Yoshimura N, Muraki S, Oka H, et al. Prevalence of knee oste | ROAD スタディ（日本人一般住民3,040人）では、X線学的変形性膝関節症（Kellgren-Lawrence 分類グ… |
| OS-040 | SRC-1855 | RESTRICTED | Bannuru RR, Osani MC, Vaysbrot EE, et al. OARSI guidelines f | OARSI ガイドライン2019では、変形性膝関節症のコア治療は関節炎に関する教育と体系的な陸上での運動プログラム（食事… |
| OS-041 | SRC-1885 | RESTRICTED | Pereira TV, Jüni P, Saadat P, et al. Viscosupplementation fo | 変形性膝関節症に対する関節内ヒアルロン酸注射（粘性補充）は、大規模プラセボ対照試験に限ったメタ解析では、プラセボに比べて… |
| OS-042 | SRC-1886 | RESTRICTED | Skou ST, Roos EM, Laursen MB, et al. A Randomized, Controlle | 片側の人工膝関節全置換術の適応となる中等症〜重症の変形性膝関節症患者では、人工膝関節全置換術に非手術治療を併用した群は、… |
| OS-043 | SRC-1887 | RESTRICTED | Ladenhauf HN, Seitlinger G, Green DW. Osgood-Schlatter disea | Osgood-Schlatter 病は、骨端線の開存する活動的な小児・思春期にみられる脛骨粗面の牽引性骨端症で、多くは自… |
| OS-044 | SRC-1888 | RESTRICTED | Sihvonen R, Paavola M, Malmivaara A, et al. Arthroscopic par | 変形性膝関節症がなく変性内側半月板断裂の症状を有する35〜65歳の患者では、関節鏡視下半月板部分切除術はシャム手術と比べ… |
| OS-046 | SRC-1890 | RESTRICTED | Wülker N, Mittag F. The treatment of hallux valgus. Dtsch Ar | 外反母趾の非手術治療は症状を緩和しうるが母趾の変形自体を矯正することはできず、疼痛が持続する場合に手術が適応となる。軽度… |
| OS-047 | SRC-1891 | RESTRICTED | Morcuende JA, Dolan LA, Dietz FR, et al. Radical reduction i | 先天性内反足に対する Ponseti 法（逐次的な徒手矯正とギプス固定）では、157例中98%で変形の矯正が得られ、広範… |
| OS-048 | SRC-1892 | RESTRICTED | Valderrabano V, Horisberger M, Russell I, et al. Etiology of | 末期の変形性足関節症の病因は外傷後が78%を占めて最も多く、二次性が13%、一次性は9%にとどまり、股関節・膝関節の変形… |
| OS-050 | SRC-1868 | RESTRICTED | Willy RW, Hoglund LT, Barton CJ, et al. Patellofemoral Pain. | 膝蓋大腿痛は思春期から若年成人に多く、女性で発生率が高い。膝蓋軟骨軟化症を含む膝蓋大腿痛では、膝蓋骨の周囲・後面の痛みが… |

### SD

| カード | 今の出典 | 区分 | 出典の書誌（冒頭） | 主張文（冒頭） |
|---|---|---|---|---|
| SD-003 | SRC-1163 | RESTRICTED | Murrell DF, Peña S, Joly P, Marinovic B, Hashimoto T, Diaz L | 天疱瘡の診断は、臨床所見だけでは不十分であり、病理組織学的検査と、直接蛍光抗体法または血清学的検査（抗デスモグレイン抗体… |
| SD-004 | SRC-1163 | RESTRICTED | Murrell DF, Peña S, Joly P, Marinovic B, Hashimoto T, Diaz L | 天疱瘡の治療では、全身性コルチコステロイドと抗CD20抗体リツキシマブが第一選択の柱であり、アザチオプリンやミコフェノー… |
| SD-005 | SRC-1164 | RESTRICTED | Ujiie H, Iwata H, Yamagami J, Nakama T, Aoyama Y, Ikeda S, e | 類天疱瘡群は、表皮基底膜部に自己抗体が線状に沈着する自己免疫性表皮下水疱症の一群で、IgG自己抗体による主な病型として水… |
| SD-006 | SRC-1164 | RESTRICTED | Ujiie H, Iwata H, Yamagami J, Nakama T, Aoyama Y, Ikeda S, e | 後天性表皮水疱症は類天疱瘡群に含まれる自己免疫性表皮下水疱症であり、日本皮膚科学会のガイドラインでは、水疱性類天疱瘡の治… |
| SD-008 | SRC-1166 | RESTRICTED | Yoneda K, Kubo A, Nomura T, Ishida-Yamamoto A, Suga Y, Akiya | 掌蹠角化症は、手掌と足底の過角化を主症状とする角化症の総称である。日本皮膚科学会のガイドラインは、その臨床像、病態生理、… |
| SD-010 | SRC-1167 | RESTRICTED | Kanitakis J. Porokeratoses: an update of clinical, aetiopath | 汗孔角化症は、角化の異常による環状または線状の角化性局面を特徴とする疾患群で、組織学的な指標は、角質層内に不全角化細胞が… |
| SD-011 | SRC-1168 | RESTRICTED | Armstrong AW, Read C. Pathophysiology, Clinical Presentation | 乾癬は慢性の炎症性皮膚疾患で、局面型の尋常性乾癬が最も多い病型である。世界で約1億2,500万人が罹患するとされ、病態に… |
| SD-012 | SRC-1168 | RESTRICTED | Armstrong AW, Read C. Pathophysiology, Clinical Presentation | 軽症の尋常性乾癬では外用療法が治療の中心であり、外用コルチコステロイド、ビタミンD誘導体、カルシニューリン阻害薬、角質溶… |
| SD-013 | SRC-1168 | RESTRICTED | Armstrong AW, Read C. Pathophysiology, Clinical Presentation | 中等症から重症の尋常性乾癬では、TNF-α阻害薬、IL-12／23のp40阻害薬、IL-17阻害薬、IL-23のp19阻… |
| SD-014 | SRC-1169 | RESTRICTED | Weston G, Payette M. Update on lichen planus and its clinica | 扁平苔癬は炎症性皮膚疾患で、典型例では、そう痒を伴う多角形で紫紅色の平坦な丘疹と局面を呈する。口腔や爪などにも病変を生じ… |
| SD-015 | SRC-1170 | RESTRICTED | Mahajan K, Relhan V, Relhan AK, Garg VK. Pityriasis Rosea: A | Gibertばら色粃糠疹は、体幹や頸部に大きな紅斑性鱗屑性局面である原発疹（herald patch）が出現し、続いて体… |
| SD-016 | SRC-1171 | RESTRICTED | Chairatchaneeboon M, Thanomkitti K, Kim EJ. Parapsoriasis—A  | 類乾癬は、現在の分類では小型局面状類乾癬と大型局面状類乾癬を指す。皮膚リンパ腫（最も多いのは菌状息肉症）への進展リスクは… |
| SD-017 | SRC-1172 | RESTRICTED | Fujita H, Terui T, Hayama K, Akiyama M, Ikeda S, Mabuchi T,  | 汎発性膿疱性乾癬は、発熱と全身の潮紅を伴い、無菌性膿疱が広範囲に再発性に出現するまれな疾患である。日本皮膚科学会のガイド… |
| SD-018 | SRC-1173 | RESTRICTED | Japanese Dermatological Association Palmoplantar Pustulosis  | 掌蹠膿疱症は、手掌と足底に無菌性膿疱が繰り返し出現する疾患で、日本ではレセプトデータに基づき約14万人の患者がいると推計… |
| SD-019 | SRC-1174 | RESTRICTED | Paek SY, Lim HW. Chronic actinic dermatitis. Dermatologic Cl | 慢性光線性皮膚炎は、免疫が関与する光線過敏症で、日光露光部にそう痒性の湿疹性・苔癬化局面を生じ、眼瞼、皮膚のしわ、耳介後… |
| SD-020 | SRC-1175 | RESTRICTED | Ezzedine K, Eleftheriadou V, Whitton M, van Geel N. Vitiligo | 尋常性白斑は、機能するメラノサイトの消失により白色斑を生じる後天性の色素異常症で、世界人口の約1%にみられると推計される… |
| SD-023 | SRC-1178 | RESTRICTED | Oshima J, Sidorova JM, Monnat RJ Jr. Werner syndrome: Clinic | Werner 症候群は、RECQ ファミリーの DNA ヘリカーゼをコードする WRN 遺伝子の機能喪失変異による常染色… |
| SD-024 | SRC-1179 | RESTRICTED | Coon EA, Cheshire WP Jr. Sweating Disorders. Continuum (Minn | 発汗障害は多汗症と無汗症（低汗症）に大別され、視床下部から脳幹・脊髄を経て交感神経節・末梢神経・エックリン汗腺へ至る発汗… |
| SD-025 | SRC-1180 | RESTRICTED | Stevens DL, Bisno AL, Chambers HF, et al. Practice guideline | せつ（癤）は黄色ブドウ球菌による毛包とその周囲の深部感染であり、癰は複数の毛包に及んだものである。波動を触れる膿瘍を形成… |
| SD-026 | SRC-1181 | RESTRICTED | Raff AB, Kroshinsky D. Cellulitis: A Review. JAMA. 2016;316( | 蜂窩織炎は真皮深層と皮下組織の感染症で、拡大する発赤、熱感、圧痛、腫脹を呈する。診断は主に病歴と身体所見に基づいて行われ… |
| SD-028 | SRC-1180 | RESTRICTED | Stevens DL, Bisno AL, Chambers HF, et al. Practice guideline | 米国の IDSA 皮膚・軟部組織感染症ガイドライン（2014年版）では、蜂窩織炎を含む皮膚軟部組織感染症について、膿を伴… |
| SD-029 | SRC-1183 | RESTRICTED | Nardi NM, McDonald EJ, Syed HA, Schaefer TJ. Felon. In: Stat | ひょう疽は指尖腹側の閉鎖された区画（指腹）内に生じる感染症で、腫脹により強い拍動性疼痛を来す。浮腫と膿の貯留による圧迫で… |
| SD-030 | SRC-1180 | RESTRICTED | Stevens DL, Bisno AL, Chambers HF, et al. Practice guideline | 丹毒は真皮の浅層と表在リンパ管に限局する皮膚感染症で、主に A 群β溶血性レンサ球菌が原因となり、周囲の正常皮膚との境界… |
| SD-031 | SRC-1184 | RESTRICTED | Koning S, van der Sande R, Verhagen AP, et al. Interventions | 伝染性膿痂疹は小児に多い表在性の細菌性皮膚感染症である。システマティックレビューでは、外用抗菌薬はプラセボより治癒率が高… |
| SD-032 | SRC-1185 | RESTRICTED | Handler MZ, Schwartz RA. Staphylococcal scalded skin syndrom | ブドウ球菌性熱傷様皮膚症候群（SSSS）は、黄色ブドウ球菌が産生する表皮剥脱性毒素が血行性に広がって生じる疾患で、毒素は… |
| SD-033 | SRC-1186 | RESTRICTED | Stevens DL, Bryant AE. Necrotizing Soft-Tissue Infections. N | 壊死性筋膜炎は、皮下組織から筋膜に沿って急速に進展する壊死性の軟部組織感染症で、複数の菌による多菌性のものと、A 群レン… |
| SD-034 | SRC-1186 | RESTRICTED | Stevens DL, Bryant AE. Necrotizing Soft-Tissue Infections. N | ガス壊疽は、ウェルシュ菌（Clostridium perfringens）をはじめとするクロストリジウム属による筋壊死（… |
| SD-035 | SRC-1187 | RESTRICTED | Franco-Paredes C, Marcos LA, Henao-Martínez AF, et al. Cutan | 皮膚の非結核性抗酸菌症では、Mycobacterium marinum がリンパ管に沿って並ぶ結節（スポロトリコイド型）… |
| SD-036 | SRC-1187 | RESTRICTED | Franco-Paredes C, Marcos LA, Henao-Martínez AF, et al. Cutan | 尋常性狼瘡は皮膚結核の代表的な病型の一つである。皮膚結核は、結核菌の外からの接種や、他部位の病巣からの播種など、感染の経… |
| SD-037 | SRC-1187 | RESTRICTED | Franco-Paredes C, Marcos LA, Henao-Martínez AF, et al. Cutan | 結核菌感染に伴う皮膚病変には、菌そのものが皮膚に侵入・播種して生じる病変のほか、感染に対する過敏反応として生じる病変（結… |
| SD-038 | SRC-1188 | RESTRICTED | Caplan AS, Gold JAW, Smith DJ, Ely JW. Diagnosis and Managem | 白癬（皮膚糸状菌症）は侵される部位によって分類され、体部白癬と頭部白癬は思春期前の小児に多く、股部白癬、足白癬、爪白癬（… |
| SD-039 | SRC-1188 | RESTRICTED | Caplan AS, Gold JAW, Smith DJ, Ely JW. Diagnosis and Managem | 体部白癬、股部白癬、足白癬は通常、安価な外用抗真菌薬に反応する。広範囲な病変、外用で改善しない場合、免疫不全がある場合、… |
| SD-040 | SRC-1189 | RESTRICTED | Leung AKC, Barankin B, Lam JM, Leong KF, Hon KL. Tinea versi | 癜風は Malassezia 属（主に M. globosa、M. furfur、M. sympodialis）による表… |
| SD-041 | SRC-1190 | RESTRICTED | Barros MBL, de Almeida Paes R, Schubach AO. Sporothrix schen | スポロトリコーシスは二形性真菌 Sporothrix schenckii による感染症で、菌に汚染された土壌、植物、有機… |
| SD-042 | SRC-1191 | RESTRICTED | Ishii N, Asai T, Asahina A, Ishiko A, et al. Guideline for t | 疥癬はヒト疥癬ダニの感染による疾患で、日本皮膚科学会の疥癬診療ガイドライン第3版は診断基準、通常疥癬と角化型疥癬の治療ア… |
| SD-043 | SRC-1191 | RESTRICTED | Ishii N, Asai T, Asahina A, Ishiko A, et al. Guideline for t | 疥癬の集団発生対策では、早期の診断確定と予防が要点となる。日本皮膚科学会の疥癬診療ガイドライン第3版は、診断と治療に加え… |
| SD-044 | SRC-1192 | RESTRICTED | Fatahzadeh M, Schwartz RA. Human herpes simplex virus infect | 単純ヘルペスウイルス（HSV）感染症は一般人口の中に大きな感染源のプールを持つ伝染性の感染症で、口唇や性器などの粘膜皮膚… |
| SD-045 | SRC-1193 | RESTRICTED | Wollenberg A, Zoch C, Wetzel S, Plewig G, et al. Predisposin | カポジ水痘様発疹症（eczema herpeticum）は、炎症のある皮膚、とくにアトピー性皮膚炎の湿疹病変に単純ヘルペ… |
| SD-046 | SRC-1194 | RESTRICTED | Sterling JC, Gibbs S, Haque Hussain SS, Mohd Mustapa MF, et  | 尋常性疣贅をはじめとする皮膚の疣贅は、ヒト乳頭腫ウイルス（HPV）の感染による良性の角化性病変であり、自然に消退すること… |
| SD-047 | SRC-1195 | RESTRICTED | Reynolds RV, Yeung H, Cheng CE, Cook-Bolden F, et al. Guidel | 尋常性痤瘡は思春期以降に広くみられる疾患で、米国皮膚科学会の診療ガイドライン（2024年）は、過酸化ベンゾイル、外用レチ… |
| SD-048 | SRC-1196 | RESTRICTED | Strazzulla LC, Wang EHC, Avila L, Lo Sicco K, et al. Alopeci | 円形脱毛症は、瘢痕を残さない炎症性の脱毛症である。小さく境界明瞭な脱毛斑から、頭髪と体毛のすべてが失われるものまで病像の… |
| SD-049 | SRC-1197 | RESTRICTED | Wang J, Khachemoune A. Granuloma Annulare: A Focused Review  | 環状肉芽腫は良性の炎症性皮膚疾患で、悪性腫瘍、外傷、甲状腺疾患、糖尿病、HIV感染など多くの病態との関連が報告されている… |
| SD-050 | SRC-1198 | RESTRICTED | Miguel D, Schliemann S, Elsner P. Treatment of Scleroedema A | 浮腫性硬化症（scleroedema adultorum Buschke）はまれな皮膚疾患で、呼吸器感染に続発する古典的… |
| SD-051 | SRC-1199 | RESTRICTED | Fatourechi V. Pretibial myxedema: pathophysiology and treatm | 脛骨前粘液水腫（甲状腺皮膚症）は Graves 病の自己免疫性の皮膚病変で、橋本病でもまれに起こる。病変は通常は無症状で… |
| SD-052 | SRC-1164 | RESTRICTED | Ujiie H, Iwata H, Yamagami J, Nakama T, Aoyama Y, Ikeda S, e | 水疱性類天疱瘡は高齢者に好発する自己免疫性水疱症で、瘙痒を伴う紅斑の上に、破れにくい緊満性水疱とびらんが多発する。診断は… |
| SD-053 | SRC-4525 | RESTRICTED | 原発性局所多汗症診療ガイドライン策定委員会. 原発性局所多汗症診療ガイドライン2023年改訂版. 日本皮膚科学会雑誌.  | 原発性局所多汗症の治療は、部位と重症度に応じた段階的治療である。塩化アルミニウム外用療法がまず行われる治療であり、掌蹠多… |
| SD-054 | SRC-1180 | RESTRICTED | Stevens DL, Bisno AL, Chambers HF, et al. Practice guideline | 伝染性膿痂疹は表皮の表在性細菌感染症で、水疱を生じる水疱性と、痂皮を主体とする痂皮性（非水疱性）に分けられる。水疱性は黄… |
| SD-055 | SRC-1185 | RESTRICTED | Handler MZ, Schwartz RA. Staphylococcal scalded skin syndrom | ブドウ球菌性熱傷様皮膚症候群（SSSS）は、黄色ブドウ球菌の表皮剥脱毒素が局所の感染巣から血行性に広がり、デスモグレイン… |
| SD-056 | SRC-1186 | RESTRICTED | Stevens DL, Bryant AE. Necrotizing Soft-Tissue Infections. N | 壊死性筋膜炎の診断は臨床所見が中心である。初期は皮膚所見に乏しく、所見に不釣り合いな強い疼痛が主症状のこともあるが、進行… |
| SD-057 | SRC-1192 | RESTRICTED | Fatahzadeh M, Schwartz RA. Human herpes simplex virus infect | 単純ヘルペスウイルス（HSV）感染症では、皮膚・粘膜に疼痛や瘙痒を伴う小水疱が群集して生じ、びらん・潰瘍を経て治癒する。… |
| SD-058 | SRC-4526 | RESTRICTED | Traidl S, Roesner L, Zeitvogel J, Werfel T. Eczema herpeticu | カポジ水痘様発疹症（eczema herpeticum）は、アトピー性皮膚炎の湿疹病変を中心に、群集しない小水疱や膿疱が… |
| SD-059 | SRC-1194 | RESTRICTED | Sterling JC, Gibbs S, Haque Hussain SS, Mohd Mustapa MF, et  | 皮膚疣贅はヒト乳頭腫ウイルス（HPV）が角化細胞に感染し、表皮の肥厚と過角化を生じて数週間から数か月後に可視化する病変で… |
| SD-060 | SRC-4527 | RESTRICTED | 日本皮膚科学会 円形脱毛症診療ガイドライン2024. 日本皮膚科学会雑誌. 2024;134(10):2491-2526 | 日本皮膚科学会の円形脱毛症診療ガイドライン2024では、ステロイド外用療法とステロイド局所注射がいずれも推奨の強さ1（エ… |
| SD-061 | SRC-4527 | RESTRICTED | 日本皮膚科学会 円形脱毛症診療ガイドライン2024. 日本皮膚科学会雑誌. 2024;134(10):2491-2526 | 日本皮膚科学会の円形脱毛症診療ガイドライン2024は、経口JAK阻害薬等の使用を推奨の強さ1（エビデンスの強さA）として… |

### ST

| カード | 今の出典 | 区分 | 出典の書誌（冒頭） | 主張文（冒頭） |
|---|---|---|---|---|
| ST-002 | SRC-4431 | RESTRICTED | 日本脳卒中学会 脳卒中ガイドライン委員会 編. 脳卒中治療ガイドライン2021〔改訂2025〕（第3版）. 協和企画.  | 脳出血では出血部位により症状が異なり、被殻出血では対側の片麻痺と感覚障害、視床出血では感覚障害、小脳出血では運動失調と嘔… |
| ST-003 | SRC-1563 | RESTRICTED | Anderson CS, et al.; INTERACT2 Investigators. Rapid blood-pr | 発症6時間以内で収縮期血圧150〜220 mmHgの脳内出血患者に対する、1時間以内に収縮期血圧140 mmHg未満を目… |
| ST-004 | SRC-1564 | RESTRICTED | Qureshi AI, et al.; ATACH-2 Trial Investigators. Intensive B | 脳内出血患者に対するニカルジピン持続静注による収縮期血圧110〜139 mmHgへの強化降圧は、標準治療（140〜179… |
| ST-005 | SRC-4431 | RESTRICTED | 日本脳卒中学会 脳卒中ガイドライン委員会 編. 脳卒中治療ガイドライン2021〔改訂2025〕（第3版）. 協和企画.  | 日本の脳卒中治療ガイドライン2021〔改訂2025〕は、脳出血急性期の血圧高値に対して、ニカルジピンの持続静注により収縮… |
| ST-006 | SRC-1565 | RESTRICTED | Mendelow AD, et al.; STICH II Investigators. Early surgery v | 脳表に近い脳葉出血（10〜100 mL、脳室内出血なし）に対する早期手術は、初期保存的治療と比べて6か月後の転帰を有意に… |
| ST-007 | SRC-1562 | RESTRICTED | Greenberg SM, et al. 2022 Guideline for the Management of Pa | 神経学的に悪化している場合、脳幹が圧迫されている場合、または脳室閉塞による水頭症を伴う小脳出血では、血腫除去術を行うこと… |
| ST-008 | SRC-1566 | RESTRICTED | Charidimou A, et al. The Boston criteria version 2.0 for cer | Boston criteria version 2.0では、50歳以上で、脳葉に限局した出血性病変（脳内出血、微小出血、… |
| ST-009 | SRC-1566 | RESTRICTED | Charidimou A, et al. The Boston criteria version 2.0 for cer | Boston criteria version 2.0のprobable CAAの診断精度は、剖検を診断標準とした解析で… |
| ST-012 | SRC-1567 | RESTRICTED | Hoh BL, et al. 2023 Guideline for the Management of Patients | WFNS分類はGlasgow Coma Scaleに基づくくも膜下出血の重症度分類で、グレードIはGCS 15点、グレー… |
| ST-014 | SRC-1567 | RESTRICTED | Hoh BL, et al. 2023 Guideline for the Management of Patients | 破裂脳動脈瘤の再出血は発症後早期に多く、転帰を著しく悪化させるため、再出血を防ぐための動脈瘤治療（クリッピングまたはコイ… |
| ST-015 | SRC-1568 | RESTRICTED | Molyneux AJ, et al.; ISAT Collaborative Group. International | クリッピングとコイリングの両方が可能と判断された破裂脳動脈瘤では、コイリング群の1年後の死亡または依存（modified… |
| ST-016 | SRC-1570 | RESTRICTED | Endo H, et al. Effects of clazosentan on cerebral vasospasm- | 日本で実施された第3相試験2件では、クラゾセンタン10 mg/時の持続静注（発症48時間以内に開始し、最長15日間）によ… |
| ST-017 | SRC-1572 | RESTRICTED | Pickard JD, et al. Effect of oral nimodipine on cerebral inf | 経口ニモジピン60 mgを4時間ごとに21日間投与する治療（発症96時間以内に開始）は、くも膜下出血後の脳梗塞の発生を3… |
| ST-018 | SRC-1567 | RESTRICTED | Hoh BL, et al. 2023 Guideline for the Management of Patients | AHA/ASAガイドライン2023は、動脈瘤性くも膜下出血の患者に対し、遅発性脳虚血の予防と転帰改善のために経口ニモジピ… |
| ST-019 | SRC-4431 | RESTRICTED | 日本脳卒中学会 脳卒中ガイドライン委員会 編. 脳卒中治療ガイドライン2021〔改訂2025〕（第3版）. 協和企画.  | ニモジピンは日本では承認されていないため、日本の脳卒中治療ガイドライン2021〔改訂2025〕では、遅発性脳血管攣縮に対… |
| ST-020 | SRC-1569 | RESTRICTED | The UCAS Japan Investigators (Morita A, et al.). The natural | 日本の未破裂脳動脈瘤の前向きコホート（UCAS Japan、5720例・6697個）では、年間破裂率は0.95%であり、… |
| ST-021 | SRC-1569 | RESTRICTED | The UCAS Japan Investigators (Morita A, et al.). The natural | UCAS Japanでは、3〜4 mmの動脈瘤に対する破裂のハザード比は、5〜6 mmで1.13、7〜9 mmで3.35… |
| ST-022 | SRC-1571 | RESTRICTED | Takagi T, Takayasu M, Suzuki Y, Yoshida J. Prediction of reb | くも膜下出血を来した椎骨動脈解離性動脈瘤では再出血が高率に起こり（本邦62例の検討で37%）、その多くは24時間以内であ… |
| ST-024 | SRC-1584 | RESTRICTED | Fischer U et al. Early versus Later Anticoagulation for Stro | 心房細動を伴う急性期脳梗塞後のDOAC開始は、ELAN試験では早期開始（軽症・中等症は48時間以内、重症は6〜7日目）と… |
| ST-025 | SRC-4431 | RESTRICTED | 日本脳卒中学会 脳卒中ガイドライン委員会 編. 脳卒中治療ガイドライン2021〔改訂2025〕（第3版）. 協和企画.  | 日本の脳卒中治療ガイドライン2021〔改訂2025〕では、心原性脳塞栓症の二次予防として心房細動に対してDOACを含む経… |
| ST-026 | SRC-1585 | RESTRICTED | Kleindorfer DO et al. 2021 Guideline for the Prevention of S | アテローム血栓性脳梗塞は、頭蓋内外の主幹動脈のアテローム硬化性プラークの破綻と血栓形成により、動脈-動脈塞栓または血行力… |
| ST-027 | SRC-1585 | RESTRICTED | Kleindorfer DO et al. 2021 Guideline for the Prevention of S | 軽症脳梗塞・高リスクTIAに対するアスピリンとクロピドグレルの併用（DAPT）は発症後早期に開始し、併用期間は21日間を… |
| ST-028 | SRC-1586 | RESTRICTED | Wang Y et al. Clopidogrel with aspirin in acute minor stroke | CHANCE試験では、発症24時間以内の軽症脳梗塞・TIAに対してクロピドグレルとアスピリンの併用はアスピリン単独より9… |
| ST-029 | SRC-1588 | RESTRICTED | Toyoda K et al. Dual antiplatelet therapy using cilostazol f | 日本のCSPS.com試験では、再発リスクの高い非心原性脳梗塞に対してシロスタゾールとアスピリンまたはクロピドグレルの併… |
| ST-030 | SRC-1583 | RESTRICTED | Yamaguchi T et al. Alteplase at 0.6 mg/kg for acute ischemic | 日本では発症4.5時間以内の急性期脳梗塞に対するrt-PA（アルテプラーゼ）静注療法の用量は0.6mg/kgであり、J-… |
| ST-031 | SRC-1582 | RESTRICTED | Powers WJ et al. Guidelines for the Early Management of Pati | 米国のAHA/ASAガイドラインでは、適応のある発症4.5時間以内の急性期脳梗塞に対するアルテプラーゼ静注の用量は0.9… |
| ST-032 | SRC-1595 | RESTRICTED | Nogueira RG et al. Thrombectomy 6 to 24 Hours after Stroke w | DAWN試験では、最終健常から6〜24時間で臨床症状と梗塞体積のミスマッチがある前方循環閉塞患者に対して血栓回収療法と標… |
| ST-033 | SRC-1590 | RESTRICTED | Wardlaw JM et al. Neuroimaging standards for research into s | ラクナ梗塞は穿通枝領域の小梗塞であり、脳小血管病（細動脈硬化・リポヒアリノーシス等）を背景とし、白質病変・微小出血・血管… |
| ST-034 | SRC-1589 | RESTRICTED | SPS3 Investigators. Effects of clopidogrel added to aspirin  | SPS3試験では、最近のラクナ梗塞患者に対するアスピリンへのクロピドグレル追加（長期DAPT）は再発脳卒中を有意に減らさ… |
| ST-035 | SRC-1591 | RESTRICTED | Easton JD et al. Definition and evaluation of transient isch | 一過性脳虚血発作（TIA）の現在の定義は時間ではなく組織に基づき、急性梗塞を伴わずに一過性の神経機能障害を来したエピソー… |
| ST-036 | SRC-1592 | RESTRICTED | Johnston SC et al. Validation and refinement of scores to pr | ABCD2スコアは年齢・血圧・臨床症状（一側性脱力・言語障害）・症状持続時間・糖尿病の5項目（0〜7点）からなり、TIA… |
| ST-037 | SRC-1585 | RESTRICTED | Kleindorfer DO et al. 2021 Guideline for the Prevention of S | TIAは脳梗塞の前兆であり、発症直後の再発リスクが高いため、頭部MRI・血管評価・心電図等による機序の緊急評価と、原因に… |
| ST-038 | SRC-1593 | RESTRICTED | Brott TG et al. Stenting versus endarterectomy for treatment | CREST試験では、症候性・無症候性の頸動脈狭窄に対して頸動脈ステント留置術と頸動脈内膜剥離術（CEA）の間で主要評価項… |
| ST-039 | SRC-1594 | RESTRICTED | Chimowitz MI et al. Stenting versus aggressive medical thera | 症候性頭蓋内動脈狭窄に対しては、SAMMPRIS試験で積極的内科治療（抗血小板療法と危険因子管理）がステント留置術より優… |
| ST-040 | SRC-1598 | RESTRICTED | Debette S, Leys D. Cervical-artery dissections: predisposing | 脳動脈解離は頭痛・頸部痛で発症することが多く、脳梗塞・TIAのほかHorner症候群などの局所症状を来し、画像では壁内血… |
| ST-042 | SRC-1599 | RESTRICTED | Spetzler RF, Martin NA. A proposed grading system for arteri | Spetzler-Martin分類は脳動静脈奇形を、大きさ（3cm未満・3〜6cm・6cm超）、 eloquent領域へ… |
| ST-043 | SRC-1600 | RESTRICTED | Mohr JP et al. Medical management with or without interventi | ARUBA試験では、未破裂脳動静脈奇形に対して内科治療単独は介入治療（手術・塞栓・定位放射線の単独または併用）併用より死… |
| ST-044 | SRC-1601 | RESTRICTED | Saposnik G et al. Diagnosis and Management of Cerebral Venou | 脳静脈洞血栓症の危険因子には妊娠・産褥、経口避妊薬、血栓性素因、感染症、悪性腫瘍などがあり、診断はMR venograp… |
| ST-045 | SRC-1602 | RESTRICTED | Ferro JM et al. Safety and Efficacy of Dabigatran Etexilate  | RESPECT-CVT試験では、脳静脈血栓症に対するダビガトランと用量調整ワルファリンの間で再発静脈血栓塞栓症は認めず、… |
| ST-046 | SRC-1603 | RESTRICTED | Kuroda S et al. Diagnostic Criteria for Moyamoya Disease - 2 | もやもや病の診断は、両側の内頸動脈終末部を中心とする狭窄・閉塞と、異常血管網（もやもや血管）の存在を血管画像で確認するこ… |
| ST-047 | SRC-1604 | RESTRICTED | Miyamoto S et al. Effects of extracranial-intracranial bypas | JAM試験では、出血発症のもやもや病に対する直接バイパス術は非手術群より有害イベントが少なく（14.3%対34.2%）、… |
| ST-048 | SRC-1605 | RESTRICTED | Cognard C et al. Cerebral dural arteriovenous fistulas: clin | 硬膜動静脈瘻はCognard分類・Borden分類により静脈還流様式（特に皮質静脈への逆流の有無）で分類され、皮質静脈逆… |
| ST-049 | SRC-4431 | RESTRICTED | 日本脳卒中学会 脳卒中ガイドライン委員会 編. 脳卒中治療ガイドライン2021〔改訂2025〕（第3版）. 協和企画.  | 偽性球麻痺は両側の皮質延髄路障害により生じ、構音障害・嚥下障害・舌運動障害を来すが、球麻痺と異なり舌の萎縮・線維束攣縮は… |
| ST-050 | SRC-1607 | RESTRICTED | AVERT Trial Collaboration. Efficacy and safety of very early | AVERT試験では、発症24時間以内の頻回・高用量の超早期離床は通常ケアより3か月後の転帰良好のオッズを下げた（46%対… |

### PG

| カード | 今の出典 | 区分 | 出典の書誌（冒頭） | 主張文（冒頭） |
|---|---|---|---|---|
| PG-001 | SRC-3161 | RESTRICTED | 日本産科婦人科学会／日本産婦人科医会 編・監修. 産婦人科診療ガイドライン 産科編 2026. 東京：日本産科婦人科学会 | 妊娠悪阻は全妊婦の0.5〜2%に発症する。治療では心身の安静と少量頻回の食事・水分補給を基本とし、脱水に対してはブドウ糖… |
| PG-002 | SRC-3162 | RESTRICTED | Nelson-Piercy C, Dean C, Shehmar M, et al.; Royal College of | 妊娠悪阻の重症度は、PUQEやHELPなどの検証された指標で評価する。尿中ケトンは脱水の指標ではないため、重症度評価には… |
| PG-003 | SRC-3161 | RESTRICTED | 日本産科婦人科学会／日本産婦人科医会 編・監修. 産婦人科診療ガイドライン 産科編 2026. 東京：日本産科婦人科学会 | 異所性妊娠は全妊娠の1〜2%に起こり、着床部位の90%以上は卵管妊娠である。治療の原則は手術療法で、薬物療法や待機療法の… |
| PG-004 | SRC-3163 | RESTRICTED | American College of Obstetricians and Gynecologists. ACOG Pr | 卵管妊娠では、血行動態が不安定な症例は医学的緊急事態であり迅速な手術介入が必要で、安定した症例は低侵襲手術またはメトトレ… |
| PG-005 | SRC-3161 | RESTRICTED | 日本産科婦人科学会／日本産婦人科医会 編・監修. 産婦人科診療ガイドライン 産科編 2026. 東京：日本産科婦人科学会 | 流産の診断は原則として1回のみの検査では確定せず、1〜2週間以内の適切な間隔で複数回診察して診断する（経腟超音波で胎嚢平… |
| PG-006 | SRC-3164 | RESTRICTED | Schreiber CA, Creinin MD, Atrio J, et al. Mifepristone Pretr | 早期妊娠喪失（無胚胎嚢または胎芽・胎児死亡が確認された妊娠）の薬物管理では、ミソプロストール800µgの腟投与の前にミフ… |
| PG-007 | SRC-3161 | RESTRICTED | 日本産科婦人科学会／日本産婦人科医会 編・監修. 産婦人科診療ガイドライン 産科編 2026. 東京：日本産科婦人科学会 | 胞状奇胎の除去後は、1〜2週ごとに血中hCGを測定して経過をみる。判別線の目安は除去術後5週で1,000 mIU/mL未… |
| PG-008 | SRC-3161 | RESTRICTED | 日本産科婦人科学会／日本産婦人科医会 編・監修. 産婦人科診療ガイドライン 産科編 2026. 東京：日本産科婦人科学会 | 頸管無力症（切迫流早産の徴候を自覚しないのに子宮口が開大し胎胞が形成されてくる状態）には明確な診断基準がない。既往妊娠で… |
| PG-009 | SRC-3165 | RESTRICTED | Watanabe K, Matsubara K, Nakamoto O, et al. Outline of the n | 日本の妊娠高血圧症候群は、妊娠中に高血圧（血圧140/90 mmHg以上）を認める場合を指し、妊娠高血圧腎症、妊娠高血圧… |
| PG-010 | SRC-3166 | RESTRICTED | The Magpie Trial Collaborative Group. Do women with pre-ecla | 妊娠高血圧腎症の女性に対する硫酸マグネシウムの投与は、子癇の発症リスクをプラセボより58%低下させた（0.8%対1.9%… |
| PG-012 | SRC-3168 | RESTRICTED | McGoldrick E, Stewart F, Parker R, Dalziel SR. Antenatal cor | 早産のリスクがある女性への出生前ステロイド投与は、周産期死亡（相対リスク0.85）、新生児死亡（同0.78）、呼吸窮迫症… |
| PG-013 | SRC-3169 | RESTRICTED | Romero R, Conde-Agudelo A, Da Fonseca E, et al. Vaginal prog | 妊娠中期に頸管長25mm以下の短頸管が見つかった単胎・無症状の女性への腟プロゲステロン投与は、妊娠33週未満の早産を有意… |
| PG-014 | SRC-3170 | RESTRICTED | Rouse DJ, Hirtz DG, Thom E, et al. A randomized, controlled  | 妊娠24〜31週で分娩が差し迫った女性への硫酸マグネシウム投与は、主要評価項目（死亡または中等度〜重度の脳性麻痺の複合）… |
| PG-015 | SRC-3171 | RESTRICTED | Brandt JS, Ananth CV. Placental abruption at near-term and t | 常位胎盤早期剝離は、胎児娩出前に胎盤が子宮への付着部から早期に剝離するもので、全妊娠の0.6〜1.2%に起こり、約半数は… |
| PG-016 | SRC-3172 | RESTRICTED | Society for Maternal-Fetal Medicine; Gyamfi-Bannerman C. SMF | 常位胎盤早期剝離の診断は病歴と臨床像によるのが最良であり、超音波検査では剝離の約20〜50%を見逃す。後期早産期（妊娠3… |
| PG-017 | SRC-3173 | RESTRICTED | American College of Obstetricians and Gynecologists; Society | 癒着胎盤スペクトラム（癒着胎盤・嵌入胎盤・穿通胎盤を含む胎盤の病的付着）は、帝王切開の既往がもっとも多い危険因子で、その… |
| PG-018 | SRC-3174 | RESTRICTED | Jauniaux E, Bhide A, Hussein AM, et al.; Royal College of Ob | 癒着胎盤スペクトラムと関連する子宮への外傷は、帝王切開の既往に限らず、掻爬、子宮鏡手術、子宮内膜アブレーション、子宮動脈… |
| PG-019 | SRC-3175 | RESTRICTED | American College of Obstetricians and Gynecologists; Society | 米国の双胎出生率は1980年の出生1,000対18.9から2009年の33.3へ76%増加した後にやや低下し、三胎以上の… |
| PG-021 | SRC-3177 | RESTRICTED | American College of Obstetricians and Gynecologists. Prelabo | 早産期前期破水（PPROM）は全妊娠の約2〜3%に起こり早産の大きな割合を占め、正期産の前期破水は約8%に起こる。前期破… |
| PG-022 | SRC-3177 | RESTRICTED | American College of Obstetricians and Gynecologists. Prelabo | 前期破水の扱いは妊娠週数ごとに一体として組み立てられ、正期産の前期破水では待機的管理の可否が、妊娠34週0日〜36週6日… |
| PG-023 | SRC-3178 | RESTRICTED | American College of Obstetricians and Gynecologists. Practic | RhD陰性の妊婦では、分娩後の抗D免疫グロブリン投与により同種免疫（感作）のリスクが約13〜16%から約0.5〜1.8%… |
| PG-024 | SRC-3179 | RESTRICTED | 日本血液製剤機構. 抗D人免疫グロブリン筋注用1000倍「JB」（乾燥抗D（Rho）人免疫グロブリン）添付文書. 202 | 国内製剤の乾燥抗D（Rho）人免疫グロブリン（抗D人免疫グロブリン筋注用1000倍「JB」）は、D（Rho）陰性の妊産婦… |
| PG-025 | SRC-3180 | RESTRICTED | Burton GJ, Jauniaux E. Pathophysiology of placental-derived  | 胎盤由来の胎児発育不全の病態の中心は、妊娠初期の子宮螺旋動脈のリモデリング不全による胎盤の灌流不全である。灌流不全は胎盤… |
| PG-026 | SRC-3180 | RESTRICTED | Burton GJ, Jauniaux E. Pathophysiology of placental-derived  | 重症の胎盤灌流不全では胎盤に梗塞とフィブリン沈着が加わる。妊娠高血圧腎症を伴う胎児発育不全では胎盤の変化がより強く、母体… |
| PG-027 | SRC-3181 | RESTRICTED | American College of Obstetricians and Gynecologists; Society | 米国では母体ケアは基礎ケア（レベルI）、専門ケア（レベルII）、subspecialtyケア（レベルIII）、地域周産期… |
| PG-028 | SRC-3182 | RESTRICTED | American College of Obstetricians and Gynecologists. Practic | 過期妊娠は最終月経から42週0日以上に達した妊娠を指し、晩期正期産は41週0日〜41週6日の妊娠を指す。米国における過期… |
| PG-029 | SRC-3183 | RESTRICTED | Dashe JS, Pressman EK, Hibbard JU; Society for Maternal-Feta | SMFM は単胎の羊水過多を、最大羊水深度8cm以上またはAFI 24cm以上のいずれかで定義することを提案する（GRA… |
| PG-030 | SRC-3184 | RESTRICTED | Magann EF, Chauhan SP, Bofill JA, Martin JN Jr. Toward consi | 羊水量の評価には AFI と最大羊水深度（MVP）が用いられるが、いずれも色素希釈法で測った実測羊水量との相関は弱い。妊… |
| PG-031 | SRC-3185 | RESTRICTED | American College of Obstetricians and Gynecologists. Committ | 羊膜内感染（絨毛膜羊膜炎）は、羊水・胎盤・胎児・卵膜・脱落膜のいずれかの組み合わせの感染とそれに伴う炎症であり、早産期・… |
| PG-032 | SRC-3186 | RESTRICTED | American College of Obstetricians and Gynecologists. ACOG Cl | ACOG は2024年の Clinical Practice Update で、羊膜内感染が疑われる臨床場面で用いる診断… |
| PG-034 | SRC-3161 | RESTRICTED | 日本産科婦人科学会／日本産婦人科医会 編・監修. 産婦人科診療ガイドライン 産科編 2026. 東京：日本産科婦人科学会 | 糖代謝異常合併妊娠の血糖管理目標は、空腹時血糖95 mg/dL未満かつ食後1時間値140 mg/dL未満、あるいは空腹時… |
| PG-035 | SRC-3252 | RESTRICTED | American Diabetes Association Professional Practice Committe | ADA の Standards of Care 2026 は、妊娠中の血糖目標を空腹時70〜95 mg/dL、食後1時間… |
| PG-039 | SRC-3161 | RESTRICTED | 日本産科婦人科学会／日本産婦人科医会 編・監修. 産婦人科診療ガイドライン 産科編 2026. 東京：日本産科婦人科学会 | バセドウ病合併妊娠では、胎児への影響を避けるため妊娠5週0日から9週6日まではチアマゾール（MMI）を避けることが推奨さ… |
| PG-040 | SRC-3256 | RESTRICTED | Provan D, Arnold DM, Bussel JB, et al. Updated international | ITP 合併妊娠では、無症状でも血小板数が2万〜3万/µL未満で治療を検討し、分娩に向けては経腟分娩で5万/µL以上、硬… |
| PG-041 | SRC-3257 | RESTRICTED | Rüegg L, et al. EULAR recommendations for use of antirheumat | EULAR の2024年改訂推奨では、妊娠と両立しうる合成抗リウマチ薬として抗マラリア薬、アザチオプリン、コルヒチン、シ… |
| PG-042 | SRC-3258 | RESTRICTED | Andreoli L, Bertsias GK, Agmon-Levin N, et al. EULAR recomme | SLE・抗リン脂質抗体症候群（APS）の妊娠管理では、疾患活動性が高い時期の妊娠は母児の転帰を悪化させるため、寛解・低活… |
| PG-044 | SRC-3259 | RESTRICTED | Society for Maternal-Fetal Medicine. Consult Series #69: Hep | SMFM の2024年指針は、B型肝炎合併妊娠では初回妊婦健診で HBs抗原・抗HBs抗体・抗HBc抗体の3項目（tri… |
| PG-045 | SRC-3260 | RESTRICTED | Society for Maternal-Fetal Medicine. Consult Series #56: Hep | SMFM の2021年指針は、C型肝炎について全妊婦を妊娠ごとに抗HCV抗体でスクリーニングすることを推奨する（GRAD… |
| PG-047 | SRC-3161 | RESTRICTED | 日本産科婦人科学会／日本産婦人科医会 編・監修. 産婦人科診療ガイドライン 産科編 2026. 東京：日本産科婦人科学会 | 日本では、早発型 GBS 感染症の予防のため妊娠36〜37週に腟入口部と肛門から検体を採取する GBS 培養検査を行う（… |
