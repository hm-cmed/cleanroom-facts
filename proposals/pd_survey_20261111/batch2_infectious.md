# パブリックドメイン出典の裏づけ調査 バッチ2（細菌 BA・間質性肺疾患 IL・ウイルス VI）

- 実施日：2026-11-11
- 対象：`~/workspace/pd_survey/targets.json` のうち IL・BA・VI のカード（自由に使える出典［OPEN／GOV_US／GOV_JP］を1つも持たないカード）**102件**（BA 26件・IL 53件・VI 23件）。
- 判定基準は先行調査（BL・GR・HF・PV、2026-11-08）およびバッチ1（精神領域、2026-11-11）と同一：**A 置き換え可／B 裏づけ追加／C 見つからない／D 区分の訂正**。主張文と数値は変えない前提で、出典の置き換え・裏づけ候補のみを探した。
- 照合基準：/tmp/repo_inv/data（origin/main 展開）のカード全文と出典マスター（data/sources/sources.yaml）。
- 注意：**IL は感染症ではなく間質性肺疾患（interstitial lung disease）の章**である。感染症系（BA・VI）は CDC 等の公的資料が厚い一方、IL は学会ガイドライン・NEJM 試験が中心で、公的資料の当たり方は領域で大きく異なる（結果にもそれが表れた）。
- 機械可読版：`batch2_infectious.json`（本ファイルと同じ内容）。

## 判定サマリー

| 判定 | 件数 | 内訳 |
|---|---|---|
| A 置き換え可 | 65 | **全件が先例依存（下記）**。BA 16、IL 31、VI 18 |
| B 裏づけ追加 | 32 | BA 10、IL 18、VI 4 |
| C 見つからない | 1 | IL 1（IL-028） |
| D 区分の訂正 | 4 | IL 3（IL-041〜043）、VI 1（VI-018） |

章別：BA 26件（A16・B10）／IL 53件（A31・B18・C1・D3）／VI 23件（A18・B4・D1）。

**先例に関する留保（本バッチで最も重要な点）**：A 判定65件は**全件**、当該論文の **PubMed 抄録レコード**（NLM＝米国政府の著作物）に主張の数値・内容が全部載ることを根拠とする「先例に基づくA」である。先例以外（政府文書本体や CC BY 原典そのもの）で主張全体を置き換えられる A は **0件**だった。抄録を置き換え出典として認めない運用なら、A は0件となり65件すべてが B に移る。バッチ1（A15件中、先例以外が1件）よりも先例への依存が全面的である点に注意されたい。判断は登録側に委ねる。

## 重要な発見

### 1. D（区分の訂正）4件 — 原典自体が CC BY で OPEN
- **IL-041・042・043（ARDS診療ガイドライン2021、J Intensive Care、SRC-435）**：現行 UNKNOWN は誤り。PMC ページの一次表示で「© The Author(s) 2022、CC BY 4.0」を確認。原典自体が OPEN になる。あわせて同出典の PMID 35799288・PMCID PMC9263056（カード・マスターとも null）を特定した。
- **VI-018（JJID 2024、大阪の咽頭結膜熱、SRC-2027）**：現行 UNKNOWN は誤り。JJID（国立感染症研究所、現 JIHS の機関誌）の公式 Instructions to Authors（研究所公式サイトで一次確認）に「JJID articles are published open access under a CC BY license」と明示。原典自体が OPEN になる。
- なお IL-043 では、抄録の要約表現（"recommend against"）と本文CQの正式文言（"suggest against (GRADE 2D)"）が食い違い、カードは本文どおりで正しいことも確認した（抄録だけで判定すると誤読する例）。

### 2. 数値の不一致は1件（VI-021 ノロウイルス）
- カードの潜伏期 **10〜51時間** に対し、CDC「About Norovirus」は **12〜48時間**。二次感染率30%以上を載せる自由な出典も見つからず B とした。
- あわせて、現出典 Glass 2009（NEJM）の PubMed／Europe PMC レコードには**抄録テキスト自体が存在しない**（abstractText 空）ことを確認した。「総説は抄録が厚い」という前提が成り立たない例。
- 先天性風疹症候群の世界推計（VI-012）は資料により約10万〜11万の幅があるが、現出典抄録・CDC とも約10万でカードと一致（A）。

### 3. C は1件のみ（IL-028、ABPA の高吸収粘液）
現出典（ISHAM-ABPA 2024）の抄録には高吸収粘液（HAM）への言及自体がない。「HAM は特徴的で他基準を満たさなくても診断確定できる」と明記する二次資料はあるが、いずれも CC BY-NC-SA／CC BY-NC-ND の NC 系で自由な出典にならない。

### 4. 識別子の「誤り」は0件、一方「未記載の補完候補」を多数特定
バッチ1で見つかったような別文献を指す PMID/DOI の誤りは、本バッチでは発見されなかった。その代わり、カード・マスターで null だった識別子を多数特定した（登録側での補完候補）：
- **IL-015**：カード・マスター（SRC-421）とも DOI・PMID が null で書誌自体が未確認だった。Arthritis Rheumatol 版 DOI 10.1002/art.41983／PMID 35106973 を特定（二重掲載の Ann Rheum Dis 版は DOI 10.1136/annrheumdis-2021-221796／PMID 35110332、点数は同一）。
- PMID の特定：IL-001（40774805）、IL-007（24836310）、IL-008（24836312）、IL-012（31566307）、IL-013（31112379）、IL-014（35106964）、IL-016（35110334）、IL-017／019（32293205）、IL-026（DOI 10.1001/jama.292.24.2997 も）、IL-027／029（38423624）、IL-030／031（18337594）、IL-032（20171521）、IL-038（37487152、DOI・PMCID も）、IL-040（23688302）、IL-041〜043（35799288）、IL-044〜046（27628078、DOI・PMCID も）、IL-047（31483963）、IL-057（42425779）、IL-059（28877975）、**IL-062（31253537。カードの uncertainty に「PMID は確認できなかったため null」と明記されていたもので、実際に存在した）**。
- PMCID の補完：BA-003（PMC7108032）、IL-002（PMC5803655）、IL-003〜006（PMC9851481）、IL-023（PMC7397797）、VI-001（PMC9411419）、VI-005（PMC9940918）。
- マスター側の小不整合：SRC-538（IL-049）は PMCID（PMC5946555）が未登録で、著者の並びも Europe PMC（Tang VK 先頭）とマスター（Cherian 先頭）で異なる。

### 5. 区分の「明確化」申し送り（D ではないが UNKNOWN のままは不正確）
- SRC-424（過敏性肺炎GL、IL-023〜025）と SRC-426（ISHAM-ABPA、IL-027〜029）はマスターで UNKNOWN だが、Europe PMC で **CC BY-NC** と確認できた。自由化にはならないが、区分は RESTRICTED への明確化が適切。
- 同様に BA-043（cc by-nc）、BA-046 の現出典（cc by-nc-nd）、BA-050（cc by-nc-nd）、IL-049（cc by-nc-sa）、IL-054（cc by-nc-nd）、IL-056（cc by-nc）は現行の RESTRICTED が正しいことを再確認した。

### 6. 新規登録候補（マスター未登録の自由な出典）
- **BA-046（淋菌）への強い B**：Ohnishi ら Emerg Infect Dis 2011（CDC の学術誌、CC BY、PMID 21192886／PMC3204624）。「有効な薬剤はセフトリアキソンとスペクチノマイシンのみ」「2009年世界初のセフトリアキソン耐性株（日本）」を支持。ただし日本の耐性率70〜80%・推奨レジメンの用量・クラミジア合併率までは GOV_JP 資料でも裏づけられなかった。
- **VI-006（ニルセビマブ）への B**：厚労省の薬価基準収載品目リスト・中医協の薬価算定資料（GOV_JP）で、薬価収載日（2024年5月22日）と薬価2規格（459,147円／906,302円）が一致。「保険給付の範囲の切り分け」の説明自体は学会文書固有のため B に留めた。
- **IL-001 の補助候補**：2025年分類を解説する Histopathology 2026 レビュー（PMID 42249728、CC BY 確認）が OPEN の裏づけ候補になる。
- **BA-052 の第二候補**：Awad 2001（PMID 11705975、マスター未登録）の抄録が α毒素とパーフリンゴリジンO の相乗を補う。
- **IL-055（パラコート）への B**：米国 EPA の農薬中毒マニュアル（GOV_US）。現出典の抄録は数値を含まず、全文は CC BY-NC のため自由にならない。
- **VI-026（先天性CMV）への部分的裏づけ**：兵庫県公式サイト（GOV_JP、ガイドライン引用）が「生後2か月以内」を支持。「中等度・重度が治療対象」は自由な出典で確認できず B。

### 7. 感染症系でも CDC の直接ヒットは限定的だった
当初の見込み（CDC ページ・ガイドライン要約が各疾患に当たる）に対し、実際に CDC の資料が判定の核になったのは BA-035（ABCs、ただし根拠は抄録）、BA-046（EID 論文）、BA-047（NHSN プロトコル）、VI-021（ノロ、ただし数値不一致）、VI-033（CDC ページとの併用）程度で、大半は抄録レコードが担った。CDC の疾患ページは定性的な総論が中心で、カードの数値的主張（試験値・推計値）をそのまま載せるものは少ない。WHO 資料は CC BY-NC-SA のため今回も候補にできなかった。

## 結果一覧

### BA（細菌）26件

| カード | 判定 | 候補・備考 |
|---|---|---|
| BA-001 | A（先例） | Walker MJ, et al. Clin Microbiol Rev 2014（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典は既存登録 SRC-2087 で、候補はその抄録レコード。原典自体の Europe PMC license は None で OPEN にはならない |
| BA-003 | A（先例） | Shulman ST, et al. Clin Infect Dis 2012（IDSA ガイドライン、当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典は既存登録 SRC-1439。カードの PMCID は null だが Europe PMC では PMC7108032 として収載を確認（識別子の誤りではなく未記載）。原典自体は学会ガイドラインで RESTRICTED のまま |
| BA-004 | B | Arias CA, Murray BE. Nat Rev Microbiol 2012（当該論文）の PubMed 抄録レコード。抄録は遺伝的系統を一般論として述べるのみで、カードの核の一つである「clonal complex 17系統」という固有名は抄録に載らないため A ではなく B とした。現出典は既存登録 SRC-2089。原典の Europe PMC license は None |
| BA-008 | A（先例） | Tong SYC, et al. Clin Microbiol Rev 2015（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典は既存登録 SRC-2093。原典の Europe PMC license は None で OPEN にはならない |
| BA-010 | A（先例） | Becker K, et al. Clin Microbiol Rev 2014（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典は既存登録 SRC-2095。原典の Europe PMC license は None |
| BA-013 | A（先例） | de Noordhout CM, et al. Lancet Infect Dis 2014（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典は既存登録 SRC-2098 で © WHO/Elsevier の RESTRICTED のまま。候補は抄録レコードのみ |
| BA-015 | A（先例） | Murphy TF, Parameswaran GI. Clin Infect Dis 2009（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典は既存登録 SRC-2100。Europe PMC では inEPMC=N だが抄録テキストは同APIで取得・確認済み |
| BA-018 | A（先例） | Kilgore PE, et al. Clin Microbiol Rev 2016（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典は既存登録 SRC-2103。なお抄録の waning immunity は感染由来かワクチン由来かを区別しない一般論としての記載であり、カードの「感染やワクチンによる免疫」という内訳の細部は抄録では区別されない点を申し送る。原典の Europe PMC lic |
| BA-020 | A（先例） | Poirel L, et al. Microbiol Spectr 2018（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典は既存登録 SRC-2105。原典の Europe PMC license は None |
| BA-021 | A（先例） | Nataro JP, Kaper JB. Clin Microbiol Rev 1998（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典は既存登録 SRC-2106。原典の Europe PMC license は None |
| BA-022 | B | Nicolas-Chanoine MH, et al. Clin Microbiol Rev 2014（当該論文）の PubMed 抄録レコード。カード末尾の「尿路感染症や菌血症の主要な起因菌としての位置づけ」は抄録に疾患名としての明示がなく（抄録は腸管外感染症のスペクトラムと総論にとどまる）、この1点が抄録では裏づけられないため A ではなく B とした。現出典は既存登録 SRC-2107。カードの uncertainty 自身も尿路感染症 |
| BA-023 | A（先例） | Navon-Venezia S, et al. FEMS Microbiol Rev 2017（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典は既存登録 SRC-2108 で © FEMS 2017 の RESTRICTED のまま。Europe PMC では inEPMC=N だが抄録テキストは同APIで取得・確認済み |
| BA-027 | A（先例） | Phin N, et al. Lancet Infect Dis 2014（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。原典自体は Europe PMC で license 表示なし・OA ではないため RESTRICTED のまま（Dではない）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）で、抄録を置き換え出典と認めるかは登録側の判断に委ねる |
| BA-031 | B | MedlinePlus（NLM）Gas gangrene 記事（Medical Encyclopedia 000620）＋ Stevens DL, et al.…。カードの主張は「IDSAガイドライン2014年版にガス壊疽の診断・治療の推奨が収められている」という書誌的事実であり、抄録は壊死性感染症を含む対象範囲までしか明示しない（ガス壊疽の個別推奨文そのものは本文範囲）。そのため置き換えではなく裏づけ追加に留める。現出典の source_class はマスタ |
| BA-032 | A（先例） | Wexler HM. Clin Microbiol Rev 2007（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。原典（ASM）は Europe PMC で license 表示なしのため RESTRICTED のまま。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）で、抄録を置き換え出典と認めるかは登録側の判断に委ねる |
| BA-035 | A（先例） | Brown NE, et al. Clin Infect Dis 2021（当該論文、CDC の Active Bacterial Core surveilla…。先例に基づくA（抄録レコード）。現出典は CDC 職員が著者の ABCs 論文で、カード記載の PMCID（PMC11307574）は著者原稿版。抄録レコード自体が数値の一次確認になる。CDC の ABCs サーベイランス報告ページも同系データの政府公開資料として併記候補になるが、本判定は抄録レコー |
| BA-043 | A（先例） | Valour F, et al. Infect Drug Resist 2014（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典のライセンスを Europe PMC で再確認したところ license は cc by-nc であり、カード・マスターの「CC BY-NC／RESTRICTED」は正しい（Dove Press の CC BY-NC 系）。自由な出典にはならないため D ではな |
| BA-044 | A（先例） | Wilson JW. Mayo Clin Proc 2012（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。原典（Mayo Clin Proc）は Europe PMC で license 表示なしのため RESTRICTED のまま。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）で、抄録を置き換え出典と認めるかは登録側の判断に委ねる |
| BA-045 | A（先例） | Truelove SA, et al. Clin Infect Dis 2020（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。原典（OUP）は Europe PMC で license 表示なしのため RESTRICTED のまま。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）で、抄録を置き換え出典と認めるかは登録側の判断に委ねる |
| BA-046 | B | Ohnishi M, et al. Ceftriaxone-Resistant Neisseria gonorrhoeae, Japan. Emerg Infe…。現出典（JAID/JSC ガイドライン英語版）のライセンスは Europe PMC で cc by-nc-nd を再確認し、RESTRICTED は正しい（Dではない）。同ガイドラインの抄録は Europe PMC に収載がなかった（abstractText 空）。EID 論文は出典マスター未登録（ |
| BA-047 | B | CDC NHSN「Bloodstream Infection Event (CLABSI and non-central line-associated BSI…。現出典（IDSA 2009ガイドライン）の抄録は Europe PMC で abstractText が空であり、抄録レコードによる裏づけは使えなかった。治療期間・陽性化時間差などの IDSA 推奨の具体をそのまま載せる自由な出典（CC BY の総説等）は本調査では特定できなかったため、判定は診断解 |
| BA-048 | B | Russo TA, Marr CM. Clin Microbiol Rev 2019（当該論文）の PubMed 抄録レコード。裏づけ対象外の部分：古典株が医療機関で基礎疾患・デバイスのある患者に起こる日和見感染であることの明示、糖尿病が危険因子で血糖管理不良が転移性合併症と関連すること、ESBL／カルバペネマーゼ産生株の耐性範囲、セフタジジム・アビバクタム／コリスチン／チゲサイクリンの in vitro 活性とメタロ-β- |
| BA-049 | B | Mahlen SD. Clin Microbiol Rev 2011（当該論文）の PubMed 抄録レコード。裏づけ対象外の部分：内因性耐性の薬剤リスト（ペニシリンG、アンピシリン、アモキシシリン・クラブラン酸、セフロキシム、コリスチン、ニトロフラントイン）、染色体性誘導型 AmpC による第3世代セファロスポリン治療中の脱抑制変異、経験的治療の薬剤選択（ピペラシリン・タゾバクタム等）は抄録に載らず本文範囲 |
| BA-050 | B | Bassetti M, et al. Drugs Context 2018（当該論文）の PubMed 抄録レコード。現出典のライセンスは Europe PMC で cc by-nc-nd を再確認し、カードの「CC BY-NC-ND 4.0／RESTRICTED」は正しい（Dではない）。裏づけ対象外の部分：壊疽性膿瘡、熱傷創部での経験的併用療法とデブリードマン、具体的な抗緑膿菌薬のリスト、耐性株へのセフトロザン・ |
| BA-051 | B | Wong D, et al. Clin Microbiol Rev 2017（当該論文）の PubMed 抄録レコード。裏づけ対象外の部分：スルバクタムが本菌に直接の抗菌活性を持つこと、それを踏まえたカルバペネム／スルバクタム軸の併用療法、代替薬としてのコリスチン・チゲサイクリン・ミノサイクリンは抄録に載らず本文範囲。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物） |
| BA-052 | B | Uzal FA, et al. Future Microbiol 2014（当該論文）の PubMed 抄録レコード ＋ Awad MM, et al. Inf…。裏づけ対象外の部分：α毒素のスフィンゴミエリナーゼ活性、α毒素欠損変異株は筋壊死を起こさないという必須性の明示、血栓形成と感染部位への多形核白血球浸潤の欠如、パーフリンゴリジンOによる白血球の血管内停留、病変組織の顕微鏡所見（好中球の血管内停留と血管外浸潤の乏しさ）の細部は、両抄録には載らず本文（お |

### IL（間質性肺疾患）53件

| カード | 判定 | 候補・備考 |
|---|---|---|
| IL-001 | A（先例） | Ryerson CJ, et al. Eur Respir J 2025（当該論文、SRC-411）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。【PMID特定】カード・出典マスター（SRC-411）とも PMID が null だったが、DOI 検索で PMID 40774805 を |
| IL-002 | A（先例） | Travis WD, et al. Am J Respir Crit Care Med 2013（当該論文、SRC-412）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。出典マスター（SRC-412）は pmcid が null だが、Europe PMC では PMCID PMC5803655 が付いており |
| IL-003 | A（先例） | Raghu G, et al. Am J Respir Crit Care Med 2022（ATS/ERS/JRS/ALAT ガイドライン、当該論文、SRC-…。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。原典自体は Europe PMC で license=cc by-nc-nd と確認され、NC/ND のため OPEN にはならず D では |
| IL-004 | A（先例） | Raghu G, et al. Am J Respir Crit Care Med 2022（ATS/ERS/JRS/ALAT ガイドライン、当該論文、SRC-…。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。原典自体は Europe PMC で license=cc by-nc-nd と確認され、NC/ND のため OPEN にはならず D では |
| IL-005 | A（先例） | Raghu G, et al. Am J Respir Crit Care Med 2022（ATS/ERS/JRS/ALAT ガイドライン、当該論文、SRC-…。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。原典自体は Europe PMC で license=cc by-nc-nd と確認され、NC/ND のため OPEN にはならず D では |
| IL-006 | A（先例） | Raghu G, et al. Am J Respir Crit Care Med 2022（ATS/ERS/JRS/ALAT ガイドライン、当該論文、SRC-…。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。原典自体は Europe PMC で license=cc by-nc-nd と確認され、NC/ND のため OPEN にはならず D では |
| IL-007 | A（先例） | Richeldi L, et al. N Engl J Med 2014（INPULSIS、当該論文、SRC-414）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。【PMID特定】カード・出典マスター（SRC-414）とも PMID が null だったが、DOI 照合で PMID 24836310 を |
| IL-008 | A（先例） | King TE Jr, et al. N Engl J Med 2014（ASCEND、当該論文、SRC-415）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。【PMID特定】カード・出典マスター（SRC-415）とも PMID が null だったが、DOI 照合で PMID 24836312 を |
| IL-009 | A（先例） | Richeldi L, et al. N Engl J Med 2025（FIBRONEER-IPF、当該論文、SRC-416）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。NCT05321069 は抄録に記載があり、ClinicalTrials.gov API で登録結果と照合済み |
| IL-011 | A（先例） | Collard HR, et al. Am J Respir Crit Care Med 2016（国際作業部会報告、当該論文、SRC-413）の PubMed…。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。原典自体は © American Thoracic Society でマスターの RESTRICTED は正しい（D ではない） |
| IL-012 | A（先例） | Flaherty KR, et al. N Engl J Med 2019（INBUILD、当該論文、SRC-418）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。【PMID特定】カード・出典マスター（SRC-418）とも PMID が null だったが、DOI 照合で PMID 31566307 を |
| IL-013 | A（先例） | Distler O, et al. N Engl J Med 2019（SENSCIS、当該論文、SRC-419）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。【PMID特定】カード・出典マスター（SRC-419）とも PMID が null だったが、DOI 照合で PMID 31112379 を |
| IL-014 | A（先例） | Robson JC, et al. Arthritis Rheumatol 2022（ACR/EULAR GPA 分類基準、当該論文、SRC-420）の Pub…。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。【PMID特定】カード・出典マスター（SRC-420）とも PMID が null だったが、DOI 照合で PMID 35106964 を |
| IL-015 | A（先例） | Suppiah R, et al. Arthritis Rheumatol 2022（ACR/EULAR MPA 分類基準）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。【重要・識別子の補完】カード・出典マスター（SRC-421）とも DOI・PMID が null で書誌（雑誌名・巻・頁）未確認だったが、本 |
| IL-016 | A（先例） | Grayson PC, et al. Ann Rheum Dis 2022（ACR/EULAR EGPA 分類基準、当該論文、SRC-422）の PubMed …。先例に基づくA（抄録レコード）。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる。【PMID特定】カード・出典マスター（SRC-422）とも PMID が null だったが、DOI 照合で PMID 35110334 を |
| IL-017 | A（先例） | Crouser ED, et al. Diagnosis and Detection of Sarcoidosis. An Official ATS Clini…。先例に基づくA（抄録レコード）。カード・SRC-423 に PMID が無く今回特定（識別子補完の候補：PMID 32293205、PMCID PMC7159433）。原典自体のライセンスは Europe PMC で cc by-nc（カードの CC BY-NC 4.0・RESTRICTED と一致 |
| IL-018 | B | Establishing a Diagnosis of Pulmonary Sarcoidosis. J Clin Med 2023（CC BY レビュー）。lupus pernio・Heerfordt 症候群での生検回避と「EBUS を最初の手技とする」という ATS 推奨そのものは候補に載らず裏づけ対象外。ガイドライン抄録は条件付き推奨13件と述べるのみで個別内容は載らない |
| IL-019 | B | Crouser ED, et al. Am J Respir Crit Care Med 2020（当該論文）の PubMed 抄録レコード＋ NHLBI Sa…。クレアチニン・ALP・血算・眼科診察・心電図を「条件付きで提案」という推奨の組み立て自体は抄録に列挙されず（抄録は条件付き推奨13件と総数のみ）、この部分は裏づけ対象外。カードに PMID が無く今回特定（32293205） |
| IL-020 | B | NHLBI（NIH）Sarcoidosis - Diagnosis ページ。カードの核である推奨内容（心症状のない患者に心エコー/ホルターをルーチンに行わない、心病変が疑わしければ PET や心エコーより心臓MRIを優先）は政府ページに記載がなく裏づけ対象外。ガイドライン抄録にも個別の条件付き推奨は載らない |
| IL-021 | B | Establishing a Diagnosis of Pulmonary Sarcoidosis. J Clin Med 2023（CC BY レビュー）。「ATS 2020 が推奨の対象としていない」はガイドライン側の記載事項であり、候補では裏づけられない（ガイドライン抄録の推奨一覧にも BAL は含まれないことと整合するが、それ自体は本文確認のまま） |
| IL-022 | B | NHLBI（NIH）Pulmonary Hypertension - Diagnosis ページ。サルコイドーシスに特化した手順（まず心エコー、心エコーで示唆されれば右心カテーテル）という順序の明記は政府ページになく、この点は裏づけ対象外。ガイドライン抄録にも個別推奨は載らない |
| IL-023 | A（先例） | Raghu G, et al. Diagnosis of Hypersensitivity Pneumonitis in Adults. An Official…。先例に基づくA（抄録レコード）。カード・SRC-424 に DOI・PMID が無く今回特定（識別子補完の候補：DOI 10.1164/rccm.202005-2032ST、PMID 32706311、PMCID PMC7397797）。原典ライセンスは Europe PMC で cc by-nc  |
| IL-024 | A（先例） | Raghu G, et al. Am J Respir Crit Care Med 2020（ATS/JRS/ALAT 過敏性肺炎ガイドライン、当該論文）の P…。先例に基づくA（抄録レコード）。識別子は今回特定（DOI 10.1164/rccm.202005-2032ST、PMID 32706311）。原典は cc by-nc（Europe PMC で確認） |
| IL-025 | B | Raghu G, et al. Am J Respir Crit Care Med 2020（ATS/JRS/ALAT 過敏性肺炎ガイドライン、当該論文）の P…。外科的肺生検について抄録は両型への suggestion と述べるのみで、カードの「ほかの方法を尽くしたあとに」という位置づけは抄録に載らず裏づけ対象外のため B。識別子は今回特定（PMID 32706311） |
| IL-026 | A（先例） | Shorr AF, et al. Acute eosinophilic pneumonia among US Military personnel deploy…。先例に基づくA（抄録レコード）。カードに DOI が無く今回特定（識別子補完の候補：DOI 10.1001/jama.292.24.2997、292巻24号）。第一著者の所属は Walter Reed Army Medical Center（米軍医療機関）で米国政府著作物の可能性はあるが、Europ |
| IL-027 | B | Agarwal R, et al. Revised ISHAM-ABPA working group clinical practice guidelines.…。カードに PMID が無く今回特定（PMID 38423624、PMCID PMC10991853）。原典ライセンスは Europe PMC で cc by-nc（SRC-426 の UNKNOWN は実際には CC BY-NC＝RESTRICTED 相当で、自由化にはならないため D とはしない） |
| IL-028 | C | 原典（Eur Respir J 2024）の抄録には高吸収粘液（HAM）への言及自体がない。高吸収粘液は pathognomonic で他の基準を満たさなくても診断を確定できると明記する二次資料は確認できたが、いずれも NC 系で OPEN にならない（Lung India 2025 の解説論文 P |
| IL-029 | B | Agarwal R, et al. Eur Respir J 2024（ISHAM-ABPA ガイドライン、当該論文）の PubMed 抄録レコード。「全身ステロイドが使えない場合はイトラコナゾールを優先」「生物学的製剤も初期治療には推奨しない」は抄録に記載がなく裏づけ対象外。PMID は今回特定（38423624）。原典は cc by-nc |
| IL-030 | A（先例） | Kudoh S, et al. Interstitial lung disease in Japanese patients with lung cancer:…。先例に基づくA（抄録レコード）。カードに PMID が無く今回特定（識別子補完の候補：PMID 18337594） |
| IL-031 | A（先例） | Kudoh S, et al. Am J Respir Crit Care Med 2008（当該論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。PMID は今回特定（18337594） |
| IL-032 | A（先例） | Marks LB, et al. Radiation Dose-Volume Effects in the Lung（QUANTEC）. Int J Radia…。先例に基づくA（抄録レコード）。カードに PMID が無く今回特定（識別子補完の候補：PMID 20171521、PMCID PMC3576042。PMC 収載は NIH 公的アクセス経由で、Europe PMC にライセンス表示はないため原典自体は OPEN としない） |
| IL-036 | A（先例） | Ranieri VM, et al（ARDS Definition Task Force）. Acute respiratory distress syndro…。先例に基づくA（抄録レコード）。原典（JAMA）は © AMA で RESTRICTED 相当のまま。候補は当該論文の PubMed 抄録レコード（NLM作成・米国政府著作物）。抄録を置き換え出典と認めるかは登録側の判断に委ねる |
| IL-037 | A（先例） | Ranieri VM, et al（ARDS Definition Task Force）. Acute respiratory distress syndro…。先例に基づくA（抄録レコード）。カードの「改善の幅は小さかった」は数値からの評価で抄録の表現ではない（カード自身の uncertainty にも明記あり）。主張の数値部分は全て抄録で裏づく |
| IL-038 | A（先例） | Matthay MA, et al. A New Global Definition of Acute Respiratory Distress Syndrom…。先例に基づくA（抄録レコード）。カード・出典マスター SRC-432 とも DOI・PMID・PMCID が null だったが、タイトル検索→Europe PMC で DOI 10.1164/rccm.202303-0558WS・PMID 37487152・PMCID PMC10870872 を特 |
| IL-039 | A（先例） | The Acute Respiratory Distress Syndrome Network. Ventilation with lower tidal vo…。先例に基づくA（抄録レコード）。カード・SRC-433 とも DOI は null だったが Europe PMC で 10.1056/NEJM200005043421801 を確認。ClinicalTrials.gov は本試験が登録制度の初期（1996-1999年実施）のため結果レコードを確認で |
| IL-040 | A（先例） | Guérin C, et al（PROSEVA Study Group）. Prone positioning in severe acute respirat…。先例に基づくA（抄録レコード）。カード・SRC-434 とも PMID は null だったが Europe PMC の DOI 照合で PMID 23688302 を特定。試験登録番号 NCT00527813 は抄録末尾の資金源欄で確認した（ClinicalTrials.gov の結果数値そのもの |
| IL-041 | D | Tasaka S, Ohshimo S, Takeuchi M, et al. ARDS Clinical Practice Guideline 2021. J…。現出典の source_class は UNKNOWN だが、PMC 掲載ページの一次表示で「© The Author(s) 2022、Open Access、Creative Commons Attribution 4.0 International License（CC BY 4.0）」を確認し |
| IL-042 | D | Tasaka S, Ohshimo S, Takeuchi M, et al. ARDS Clinical Practice Guideline 2021. J…。IL-041 と同じく、現出典は PMC ページの一次表示で CC BY 4.0（© The Author(s) 2022）のため OPEN。UNKNOWN は誤り。PMID 35799288・PMCID PMC9263056 は今回特定 |
| IL-043 | D | Tasaka S, Ohshimo S, Takeuchi M, et al. ARDS Clinical Practice Guideline 2021. J…。IL-041 と同じく、現出典は PMC ページの一次表示で CC BY 4.0 のため OPEN。UNKNOWN は誤り。PMID 35799288・PMCID PMC9263056 は今回特定 |
| IL-044 | B | McCormack FX, et al. Official American Thoracic Society/Japanese Respiratory Soc…。カード・SRC-436 とも DOI・PMID・PMCID が null だったが、タイトル検索→Europe PMC で DOI 10.1164/rccm.201607-1384ST・PMID 27628078・PMCID PMC5803656 を特定。推奨の強さまで引用する Clinician  |
| IL-045 | B | McCormack FX, et al. Official American Thoracic Society/Japanese Respiratory Soc…。識別子は今回特定（IL-044 の notes 参照）。推奨文の全文は ATS プレスリリースと Clinician Summary（© ATS）に載るが、いずれも自由な出典ではないため候補にしない |
| IL-046 | B | McCormack FX, et al. Official American Thoracic Society/Japanese Respiratory Soc…。識別子は今回特定（IL-044 の notes 参照）。条件付きの明示を含む推奨文全文は Clinician Summary（PMC5566288）に引用されているが © ATS のため候補にしない |
| IL-047 | A（先例） | Tazawa R, Ueda T, Abe M, et al. Inhaled GM-CSF for Pulmonary Alveolar Proteinosi…。先例に基づくA（抄録レコード）。カード・SRC-437 とも PMID は null だったが Europe PMC の DOI 照合で PMID 31483963 を特定。試験登録は抄録末尾で ClinicalTrials.gov NCT02835742 と JMA-IIA00205（日本医師会治 |
| IL-049 | B | Tang VK, Vijhani P, Cherian SV, Ambelil M, Estrada-Y-Martin RM. Primary pulmonar…。Europe PMC の license フィールドで cc by-nc-sa を確認した。カード・マスター記載の CC BY-NC-SA 4.0・RESTRICTED は正しく、D ではない。出典マスター SRC-538 は PMCID が未登録（カードには PMC5946555 の記載あり）。ま |
| IL-050 | A（先例） | Abbott GF, Rosado-de-Christenson ML, Franks TJ, Frazier AA, Galvin JR. From the …。先例に基づくA（抄録レコード）。AFIP（米軍病理学研究所）のアーカイブ論文だが、抄録に表示される筆頭著者の所属は Brown Medical School／Rhode Island Hospital で、米国政府著作物であることの一次表示は抄録の範囲では確認できないため、政府著作物としての D は |
| IL-052 | A（先例） | Cordier JF. Cryptogenic organizing pneumonia. Clin Chest Med 2004（現出典 SRC-541 と同…。先例に基づくA（抄録レコード）。原典自体は Elsevier で RESTRICTED のまま。抄録を置き換え出典と認めるかは登録側の判断（バッチ1と同じ留保） |
| IL-053 | A（先例） | Auchincloss JH, et al. Br J Ind Med 1992（現出典 SRC-542 と同一論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。1992年論文で Europe PMC の license フィールドは空（OAライセンス表示なし）のため、現出典の source_class=UNKNOWN はそのまま妥当で D には当たらない |
| IL-054 | B | Mach WJ, Thimmesch AR, Pierce JT, Pierce JD. Consequences of hyperoxia and the t…。【D確認】現出典（Ann Med Surg 2022）のライセンスは Europe PMC で cc by-nc-nd と再確認でき、RESTRICTED は正しい（D ではない）。候補本文では「気管気管支炎」という段階名そのものは明記されず（気管支・肺胞内面の障害として記述）、段階の言い回しがカー |
| IL-055 | B | 米国環境保護庁（EPA）. Recognition and Management of Pesticide Poisonings, Chapter 12: Pa…。現出典（Korean J Intern Med 2009）の抄録は総説的論説の短い要旨で数値を含まないため抄録レコードでは裏づけられない。同論文の全文（PMC2698628）にはカードの全数値が原文どおり載るが、ライセンスは CC BY-NC のため自由な出典にはならず、RESTRICTED は正し |
| IL-056 | B | Jönsson ÅLM, Hilberg O, Simonsen U, Christensen JH, Bendstrup E. New insights in…。【D確認】現出典（Yale J Biol Med 2021）のライセンスは Europe PMC で cc by-nc と再確認でき、RESTRICTED は正しい（D ではない）。現出典の抄録レコード自体も、砂嵐様の画像所見と症状との乖離、遺伝形式、根治治療なし・一部の症例で肺移植、まで含み B  |
| IL-057 | B | Sapuppo G, et al. Chin Clin Oncol 2026（現出典 SRC-547 と同一論文）の PubMed 抄録レコード。【識別子の追加候補】カードでは PMID が null だが、Europe PMC で PMID 42425779 が確認できた（登録側での補完候補）。候補は抄録レコードによる部分的な裏づけであり、先例に基づくAではない |
| IL-059 | B | Milani P, et al. The lung in amyloidosis. Eur Respir Rev 2017（現出典 SRC-562 と同一論文）…。【識別子の追加候補】カードでは PMID・PMCID が null だが、Europe PMC で PMID 28877975・PMCID PMC9488920 が確認できた。抄録には「いずれも AL 型が多い」こととコンゴーレッド染色の偏光下緑色複屈折の記載がないため B。現出典のライセンスは E |
| IL-062 | B | Suzuki Y, Suda T. Eosinophilic pneumonia: A review of the previous literature, c…。【識別子の訂正候補】カードの uncertainty では「PMID は確認できなかったため null」とされているが、Europe PMC で PMID 31253537 が DOI と対応して確認できた（登録側での補完候補）。現出典のライセンスは Europe PMC で cc by-nc-nd |

### VI（ウイルス）23件

| カード | 判定 | 候補・備考 |
|---|---|---|
| VI-001 | A（先例） | Uyeki TM, et al. Influenza. Lancet 2022（現出典 SRC-2011 と同一論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。【識別子の追加候補】カードでは PMCID が null だが Europe PMC で PMC9411419（著者稿）が確認できた |
| VI-002 | A（先例） | Dobson J, et al. Oseltamivir treatment for influenza in adults: a meta-analysis …。先例に基づくA（抄録レコード）。原典自体は Lancet で RESTRICTED のまま |
| VI-005 | A（先例） | Simões EAF, et al. Lancet Child Adolesc Health 2023（現出典 SRC-2015 と同一論文）の PubMed …。先例に基づくA（抄録レコード）。ClinicalTrials.gov の MELODY 等の個別登録は統合解析値そのものを含まないため、候補の核は抄録レコードとした【識別子の追加候補】カードでは PMCID が null だが Europe PMC で PMC9940918 が確認できた |
| VI-006 | B | 厚生労働省 薬価基準収載品目リストおよび中医協の新医薬品薬価算定資料（ベイフォータス筋注50mg・100mgシリンジ、令和6年5月22日収載分）。保険給付の範囲（重篤な RSウイルス感染症のリスクを有する児における発症抑制に限る）は算定資料の効能・効果の記載と整合するが、「適応にはリスクのない児を含むのに保険給付は限られる」という切り分けの説明自体は現出典の学会文書（日本小児科学会、SRC-2016）の解説固有のため、全体としては B とした |
| VI-009 | A（先例） | Moss WJ. Measles. Lancet 2017（現出典 SRC-2018 と同一論文）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。WHO ファクトシートは CC BY-NC-SA のため自由な出典にせず、CDC を優先した（バッチ方針どおり） |
| VI-012 | A（先例） | Lambert N, Strebel P, Orenstein W, Icenogle J, Poland GA. Rubella. Lancet 2015（現…。先例に基づくA（抄録レコード）。訂正履歴：初版では抄録の数値を 110,000 と誤記し B としていたが、Europe PMC の抄録全文の再確認で 100,000 と判明し、後段の論旨まで抄録に含まれるため A に訂正した（2026-11-11）。WHO ファクトシートも約10万例を掲げるが C |
| VI-014 | A（先例） | Yamanishi K, et al. Identification of human herpesvirus-6 as a causal agent for …。先例に基づくA（抄録レコード）。1988年の歴史的原著であり、主張自体が抄録で確認できる範囲に限られている（カードの uncertainty と整合） |
| VI-015 | A（先例） | Leung AKC, et al. Roseola Infantum: An Updated Review. Curr Pediatr Rev 2024（現出典…。先例に基づくA（抄録レコード）。【D確認】現出典のライセンスは Europe PMC の license フィールドが空・Crossref にも表示がなく、自由なライセンスは確認できないため RESTRICTED のままが妥当で D には当たらない。MedlinePlus の roseola 記事は |
| VI-017 | A（先例） | Sawyer LA, et al. Am J Epidemiol 1989（当該論文、既存 SRC-2026）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。エンテロウイルス70については、抄録では1981-82年の急性出血性結膜炎流行の原因として記載される形で裏づけられる |
| VI-018 | D | 現出典そのもの：Koyama M, et al. Jpn J Infect Dis 2024（既存 SRC-2027）の区分訂正（UNKNOWN→OPEN）。区分の訂正：JJID は国立感染症研究所（現・国立健康危機管理研究機構 JIHS）の機関誌で、公式 Instructions to Authors（2024-01-24改訂、研究所公式サイトで一次確認）に「JJID articles are published open access under a |
| VI-019 | A（先例） | Jhanji V, et al. Surv Ophthalmol 2015（当該論文、既存 SRC-2028）の PubMed 抄録レコード。先例に基づくA（抄録レコード） |
| VI-020 | A（先例） | Flynn TG, et al. Lancet 2024（当該論文、既存 SRC-2029）の PubMed 抄録レコード。先例に基づくA（抄録レコード） |
| VI-021 | B | CDC「About Norovirus」ページ（GOV_US、新規登録候補）。重要な発見：現出典 Glass 2009（NEJM）の PubMed／Europe PMC レコードには抄録テキスト自体が存在しない（Europe PMC の abstractText は空、NCBI efetch でも抄録なし）ため、「抄録が厚い」という事前の見込みは外れ、先例Aは成立しない。カー |
| VI-022 | A（先例） | Dunmire SK, et al. J Clin Virol 2018（当該論文、既存 SRC-2031）の PubMed 抄録レコード。先例に基づくA（抄録レコード） |
| VI-023 | A（先例） | Sylvester JE, et al. Am Fam Physician 2023（当該論文、既存 SRC-2032）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。現出典に DOI が無い点は Europe PMC でも DOI なしで一致しており、識別子異常ではない（カードの uncertainty の記載どおり） |
| VI-024 | A（先例） | Heegaard ED, Brown KE. Clin Microbiol Rev 2002（当該論文、既存 SRC-2033）の PubMed 抄録レコード。先例に基づくA（抄録レコード） |
| VI-025 | A（先例） | Enders M, et al. Prenat Diagn 2004（当該論文、既存 SRC-2034）の PubMed 抄録レコード。先例に基づくA（抄録レコード） |
| VI-026 | B | Ito Y, et al. Pediatr Infect Dis J 2024（当該論文、既存 SRC-2035）の PubMed 抄録レコード＋兵庫県公式サイ…。「治療対象は中等度・重度の症候性」という部分は自由な出典では確認できなかった。ガイドライン2023日本語本文（日本小児感染症学会サイト公開のPDF）には CQ3-1／CQ3-2 の結論として「中等度から重度の症候性cCMV児へのバルガンシクロビル内服治療は…効果がある」、CQ3-3 推奨として「内服 |
| VI-027 | A（先例） | Kimberlin DW, et al. N Engl J Med 2015（当該論文、既存 SRC-2036）の PubMed 抄録レコード（補助：Clini…。先例に基づくA（抄録レコード）。ClinicalTrials.gov NCT00466817（抄録末尾に記載、NIAID funded）には結果登録があり（hasResults=true を API で確認）、試験の実在と枠組みの GOV_US 裏づけになる |
| VI-028 | A（先例） | Rawlinson WD, et al. Lancet Infect Dis 2017（当該論文、既存 SRC-2037）の PubMed 抄録レコード。先例に基づくA（抄録レコード） |
| VI-030 | A（先例） | Robilotti E, et al. Clin Microbiol Rev 2015（当該論文、既存 SRC-2039）の PubMed 抄録レコード。先例に基づくA（抄録レコード） |
| VI-031 | A（先例） | Ruiz-Palacios GM, et al. N Engl J Med 2006（当該論文、既存 SRC-2040）の PubMed 抄録レコード。先例に基づくA（抄録レコード）。ClinicalTrials.gov での照合は不成立：抄録が引く NCT00139347（多国間有効性試験）には結果登録がなく（hasResults=false を API で確認）、もう一方の NCT00263666 は南アフリカのHIV感染乳児を対象とする別試験 |
| VI-033 | B | Wright WF, et al. J Neurol Sci 2019（当該論文、既存 SRC-4881）の PubMed 抄録レコード＋CDC「About V…。抄録単独では原因ウイルスの列挙（非ポリオエンテロウイルスが最多等）がないため CDC との併用とした。CDC の「最も多い」は米国を前提とする記載であり、カードの「国際」スコープとの間には地域の留保が残るため B とした |
## 方法と留保

- ライセンスは Europe PMC の license フィールド、PMC ページ・誌公式サイト（JJID の Instructions to Authors 等）の一次表示で個別に確認した。
- PubMed／Europe PMC の抄録は REST API（resultType=core）で取得し、主張・数値と1件ずつ照合した。一部（PMID 22797452、Tasaka の DOI）は API がタイムアウトし再試行しなかったため、検索インデックス上の PubMed 抄録表示や PMC 全文ページで代替確認し、各行の `searched` に明記した。
- NEJM 試験群は ClinicalTrials.gov の登録結果でも照合した（INPULSIS、ASCEND、FIBRONEER-IPF、INBUILD、SENSCIS、先天性CMV の NCT00466817 は結果登録ありで一致。一方 VI-031 の NCT00139347 は結果登録なし、VI-005 の統合解析値は個別登録に含まれない）。
- 候補のうち出典マスターに無いもの（Ohnishi 2011、Awad 2001、Histopathology 2026 レビュー、厚労省薬価算定資料、EPA 農薬中毒マニュアル等）は新規登録候補であり、SRC 番号は付けていない（採番は登録側）。
- BA-018 には留保がある：抄録の「免疫の減衰」は感染由来／ワクチン由来を区別しない一般論で、カードの内訳の細部は抄録では区別されない。厳密に見る場合は B への格下げ余地あり（JSON の notes に明記）。
- PDF の新規保存は行っていない（読んだのは API・HTML の公開資料のみ）。Drive 台帳への IN 番号も付けていない。
