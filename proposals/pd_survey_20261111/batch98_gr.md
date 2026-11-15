# バッチ98：GR（成長・発達の障害）3件

- 実施日：2026-11-15
- 対象：GR 章の対象カード全3件（GR-001・GR-002・GR-003）
- ルール：2026-11-11 のレポジトリ側指示に基づく新ルール（抄録・添付文書・医学百科は根拠にしない。使えるのは政府の全文文書・報告書、CC BY 全文、試験登録レコードなど全文で読める資料のみ。旧来の「先例に基づく A」は廃止）を適用。
- 方法：各カードの主出典（マスター SRC、本バッチでは SRC-1027・SRC-1026・SRC-3529 の3出典）の刊行版ライセンスを Crossref の版（version of record）データと Europe PMC の個別レコードで1件ずつ確認した（SRC-1027 の PMC 収載コピーの書誌・著作権表示は、Europe PMC の全文 XML が HTTP 500 を返したため NCBI E-utilities の efetch で代替確認した）。候補は CC BY 全文と政府の公式ページを実際に読んで裏づけ範囲を判定し、ライセンスは候補ごとに Crossref の版データ、Europe PMC の個別レコード、PMC 全文のライセンス要素で個別確認した。識別子（PMID・PMCID・DOI）は一括照会の値を使わず、DOI キー・PMID キー・PMCID キーの個別照会で相互に確かめた。出典の説明はマスター（repo_current2 の sources.yaml）の記載からそのまま取った。本バッチでは Crossref のレート制限（429）には当たらなかった。

## 集計

- A：0件
- B：3件（すべて部分）
- C：0件
- D（マスターの区分訂正）：新規0出典（再掲2出典：SRC-1027・SRC-1026、いずれもバッチ77で提案済みの UNKNOWN→RESTRICTED。本バッチで再確認したが二重計上しない）

## 明細

| 対象 | 判定 | 現行出典（主出典） | 候補 | 区分 | PMID | DOI | PMCID | ライセンス根拠URL | 裏づけ範囲 | 数値照合 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GR-001 | B（部分） | SRC-1027：Collett-Solberg PF, Ambler G, Backeljauw PF, et al. Diagnosis, Genetics, and Therapy of Short Stature in Children: A Growth Hormone Research Society International Perspective. Horm Res Paediatr. 2019;92(1):1-14 | Paparella R, Bei A, Bernabei I, et al. Idiopathic Short Stature in the Genomic Era: Integrating Auxology, Endocrinology, and Emerging Genetic Insights. Children (Basel). 2025;12(7):855／Linglart A, Cianfarani S, Dattani MT, et al. International Consensus on the Diagnosis and Clinical Management of Idiopathic Short Stature: A Modified Delphi Method. Horm Res Paediatr. 2026 | OPEN／OPEN | 40723048／42658741 | 10.3390/children12070855／10.1159/hrp/adaag008 | PMC12294097／PMC13713050 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補1（CC BY 総説）は「オークソロジーによる評価は低身長評価の要（cornerstone）であり、身長・成長速度・思春期の経過の精密な縦断的計測と標的身長の評価によって異常な成長の経過を早期に捉えられる」と述べ、カードの主張の中核（病歴・身体所見に加えて、計測値を成長曲線上で経時的に追う評価が最も重要な方法であり、単一時点の身長だけでなく成長の経過そのものを評価することが診断の出発点）と一致する。また「低身長は小児内分泌への紹介の一般的な理由（a common reason for pediatric endocrinology referral）」とも述べる。候補2（CC BY の国際コンセンサス）は、集団の成長曲線で身長 SDS を解釈すること、身長速度の評価には最低6か月空けた2回以上の計測が必要なこと、評価は病歴・身体所見・成長速度の文脈で解釈することを推奨として再掲する。ただし「小児内分泌医への紹介理由として最も頻度が高い」という最上級の表現そのものは候補のいずれにも再掲がない（候補1は common reason の表現にとどまる） | 数値的主張はカードにない（身長 −2 SDS の定義はカードの uncertainty にあるとおり主張に入れられていない）。候補2の身長速度評価の条件（2回以上の計測・最低6か月間隔）はカードの主張の数値照合の対象ではない | 主出典 SRC-1027 の区分訂正（UNKNOWN→RESTRICTED）と license_note の更新、PMCID の補完はいずれもバッチ77で提案済みの再掲（区分訂正・識別子補完の節参照）。カード側はすでに source_class が RESTRICTED、source_license に「CC BY-NC-ND 4.0（Crossref・Europe PMC で確認）」の記載があり、マスター側の反映待ち。候補のライセンスはいずれも Crossref の版データ・Europe PMC の個別レコード・PMC 全文のライセンス要素で CC BY 4.0 と個別確認した。候補2は主出典と著者陣の重なる後継的なコンセンサス文書で、バッチ77で次回改訂時の出典差し替え（OPEN 化）候補として申し送り済み |
| GR-002 | B（部分） | SRC-1026：Grimberg A, DiVall SA, Polychronakos C, et al. Guidelines for Growth Hormone and Insulin-Like Growth Factor-I Treatment in Children and Adolescents: Growth Hormone Deficiency, Idiopathic Short Stature, and Primary Insulin-Like Growth Factor-I Deficiency. Horm Res Paediatr. 2016;86(6):361-397 | Linglart A, Cianfarani S, Dattani MT, et al. International Consensus on the Diagnosis and Clinical Management of Idiopathic Short Stature: A Modified Delphi Method. Horm Res Paediatr. 2026／Backeljauw PF, Andrews M, Bang P, et al. Challenges in the care of individuals with severe primary insulin-like growth factor-I deficiency (SPIGFD): an international, multi-stakeholder perspective. Orphanet J Rare Dis. 2023;18(1):312 | OPEN／OPEN | 42658741／37805563 | 10.1159/hrp/adaag008／10.1186/s13023-023-02928-7 | PMC13713050／PMC10559630 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補1（CC BY の国際コンセンサス）は主出典（Grimberg et al. 2016）を引用文献として挙げ、特発性低身長症（ISS）は除外診断であること、ISS の診断は GH 刺激試験で刺激時 GH が欠乏の閾値を超え、IGF-1・IGFBP-3 が正常範囲であることを確認して行うこと（すなわち成長ホルモン分泌不全症（GHD）との区別に IGF-I の測定を含む評価が必要なこと）、思春期前の低身長では ISS と体質性思春期遅延が初回評価で区別できない場合があることを述べ、鑑別の困難さと IGF-I を含む評価の進め方の骨格を裏づける。候補2（CC BY）は、原発性 IGF-I 欠損症（PIGFD）の重症型（SPIGFD）が GH 不感受性の枠組みに位置づけられること、診断の道筋自体が困難（challenging）であること、組換えヒト IGF-1（rhIGF-1）が SPIGFD に対する唯一の有効な治療であることを述べ、PIGFD 側の位置づけと組換え IGF-I 治療の位置づけを裏づける。ただし、2016年の小児内分泌学会ガイドラインがこの3病態を対象とし、評価の進め方と成長ホルモン治療・組換え IGF-I 治療の適応判断に関する推奨を示したというガイドライン自身の範囲表明そのものは、自由な全文には再掲がない（両候補とも主出典を引用文献として挙げるにとどまる） | 数値的主張はカードにない。候補1の GH 刺激試験の閾値（ピーク GH 7.5〜10 µg/L、測定法・地域で異なると注記）は候補側の値であり、主出典の数値として裏づけ登録しないこと（申し送り参照） | 主出典 SRC-1026 の区分訂正（UNKNOWN→RESTRICTED）はバッチ77で提案済みの再掲（区分訂正の節参照）。候補のライセンスはいずれも Crossref の版データ・Europe PMC の個別レコード・PMC 全文のライセンス要素で CC BY 4.0 と個別確認した。カードの uncertainty にある国内承認の注記（特発性低身長症は国内の成長ホルモン承認適応に含まれない）は本棚卸しの対象外であり、変更していない |
| GR-003 | B（部分） | SRC-3529：Lipkin PH, Macias MM; Council on Children With Disabilities. Promoting Optimal Development: Identifying Infants and Young Children With Developmental Disorders Through Developmental Surveillance and Screening. Pediatrics. 2020;145(1):e20193449 | CDC（National Center on Birth Defects and Developmental Disabilities）「Developmental Monitoring and Screening」（公式ページ、2026-02-16更新。参照文献1として主出典 Lipkin & Macias 2020 を明示） | GOV_US | なし（政府の公式ウェブページ） | なし（政府の公式ウェブページ） | なし（政府の公式ウェブページ） | https://www.cdc.gov/act-early/about/developmental-monitoring-and-screening.html | 部分：候補（米国政府 CDC の公式ページ、GOV_US）は、主出典（Lipkin & Macias 2020）を参照文献1として明示したうえで、健診のたびに発達について確認し、到達の遅れや懸念があればスクリーニング検査を次の段階とする発達モニタリング（主出典のいうサーベイランスに相当）の進め方と、米国小児科学会（AAP）が標準化された発達スクリーニング検査を生後9か月・18か月・30か月の健診で実施するよう推奨していることをそのまま再掲し、懸念がある場合は予定の月齢以外でもスクリーニングを行うこと、発達の懸念が特定された場合は州の早期介入システムへの紹介・評価が次の段階であることを述べ、カードの主張の骨格（すべての健診の機会に発達サーベイランスを行うこと、標準化されたスクリーニングを9か月・18か月・30か月に実施する体制、懸念が得られた場合は月齢を問わずスクリーニングの実施または早期介入・専門医療への紹介に進めること）と一致する。ただし候補は保護者向けの平易な説明であり、AAP 臨床報告自身の推奨文の形（サーベイランスの構成要素の定義など）までは再掲がなく、サーベイランスに当たる概念は developmental monitoring の語で説明されている | スクリーニング実施月齢（生後9か月・18か月・30か月）は候補の再掲と完全一致する | 主出典 SRC-3529 は Crossref の版データにライセンス登録がなく、Europe PMC の個別レコードでも非 OA・PMC 未収載で、© AAP の著作物として現行 RESTRICTED が正しい（区分訂正なし）。識別子補完候補あり（識別子補完の節参照）。候補は米国政府の公式ページで、その内容は政府の全文として読める（GOV_US） |

## D（マスターの区分訂正）：新規0出典（再掲2出典）

- 本バッチでは新規の区分訂正はない。対象3件の主出典は3出典（SRC-1027・SRC-1026・SRC-3529）で、SRC-3529 は現行の RESTRICTED が正しいことを確認した。SRC-1027・SRC-1026 の区分訂正はバッチ77（IE 章、主出典を共有）で提案済みの再掲であり、本バッチで刊行版ライセンスを個別に再確認したが二重計上しない。
- SRC-1027（GR-001 の主出典）：UNKNOWN→RESTRICTED【再掲・バッチ77】。Collett-Solberg et al., Horm Res Paediatr 2019（Karger）。Crossref の版データと Europe PMC の個別レコードの双方で刊行版ライセンスは CC BY-NC-ND 4.0 と特定でき、自由区分には当たらない。PMC 収載コピー（PMC6979443）の著作権表示は「© 2019 by S. Karger AG, Basel」。マスターの license_note（「© 2019 S. Karger AG, Basel（CC表示なし）」）は特定されたライセンスと異なるため、区分訂正とあわせた文言更新の提案も再掲する。なおカード GR-001 側はすでに source_class が RESTRICTED で、source_license に「CC BY-NC-ND 4.0（Crossref・Europe PMC で確認）」の記載があり、マスター側の反映待ちである。
- SRC-1026（GR-002 の主出典）：UNKNOWN→RESTRICTED【再掲・バッチ77】。Grimberg et al., Horm Res Paediatr 2016（Karger）。Crossref の版データのライセンスは Karger のサイトライセンスへのリンクのみ（vor・tdm とも）で CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載。マスターの license_note（「© S. Karger AG（CC表示なし）」）は実態と一致する。
- SRC-3529（GR-003 の主出典）：現行 RESTRICTED が正しい（区分訂正なし）。Lipkin & Macias, Pediatrics 2020（AAP）。Crossref の版データにライセンス登録はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載で、© AAP の著作物である。

## 識別子補完候補：新規1出典1項目・再掲1出典1項目（DOI・PMID・PMCID キーの個別照会で照合済み）

- SRC-3529：PMID 31843861（新規。マスターは null、カード側には記録済み。DOI（10.1542/peds.2019-3449）キーと PMID（31843861）キーの個別照会が相互に一致し、当該論文（Lipkin & Macias, Pediatrics. 2020;145(1):e20193449）の識別子であることを確認。PMCID は存在しない（PMC 未収載））
- SRC-1027：PMCID PMC6979443（再掲・バッチ77で提案済み、二重計上しない。マスター・カードとも null。本バッチでは DOI キー・PMID キーの Europe PMC 個別照会と NCBI efetch で取得した PMC 収載コピーのヘッダ（同一レコードに PMID 31514194・DOI 10.1159/000502231 を収載）で再確認した。PMC 収載コピーの著作権表示は © 2019 S. Karger AG, Basel で刊行版ライセンスは CC BY-NC-ND 4.0 のため、識別子を補っても区分は RESTRICTED のまま）

新規分はマスターの null の欄への補完候補であり、カード側には記録済みの値である。SRC-1026・SRC-1027 の PMID（27884013・31514194）はマスター登録済みの値が個別照会の結果と一致することを確認した（補完対象ではない）。

## 申し送り

- GR-001 の「紹介理由として最も頻度が高い」について：候補1（Paparella et al. 2025）は “a common reason for pediatric endocrinology referral” の表現であり、最上級の頻度順位そのものは自由な全文のいずれにも再掲がない。この要素の裏づけとして候補を登録しないこと。
- GR-002 の裏づけの性格：3病態の枠組みは2候補の組み合わせによる要素別の裏づけであり、ガイドライン自身の範囲表明や推奨文の再掲ではない。候補1（特発性低身長の国際コンセンサス 2026）の GH 刺激試験の閾値（ピーク GH 7.5〜10 µg/L、測定法・地域で異なると注記）は候補側の値であり、主出典の数値として登録しないこと。
- GR-003 の用語対応と現行性：CDC のページは AAP のサーベイランスに当たる概念を developmental monitoring の語で説明する保護者向けページであり、裏づけは枠組みと実施月齢の骨格に限る。同ページは2026-02-16の更新時点でも参照文献1に主出典（2020年の臨床報告）を挙げており、主出典の枠組みが現行であることの傍証になる。主出典の後継版に当たる監視事項は本バッチでは見つからなかった。
- GR-001 の候補2（Linglart et al. 2026、特発性低身長の国際コンセンサス）は主出典 SRC-1027 と著者陣の重なる後継的なコンセンサス文書で刊行版が CC BY であり、バッチ77で次回改訂時の主出典差し替え（OPEN 化）候補として申し送り済みである（再掲）。本バッチの裏づけは本体照合の代替にはならない。
- 方法上の注記：Europe PMC の全文 XML が SRC-1027 の PMC 収載コピー（PMC6979443）で HTTP 500 を返したため、同コピーの書誌・著作権表示の確認は NCBI E-utilities（efetch、db=pmc）で代替した。本バッチでは Crossref のレート制限（429）には当たらなかった。
- 主出典・候補とも識別子の誤記（別論文の識別子の混入）は本バッチでは発見されなかった。主出典3出典の書誌（誌名・年・巻・号・ページ）は Crossref と Europe PMC の個別レコードの値とすべて一致し、要・正本確認に当たる食い違いはない。GR-001 のカードの uncertainty にある「誌面発行は2019年で、2018年はオンライン先行の年である」という注記も個別レコードと矛盾しない。
- 本バッチの判定は以上で完結しており、カードの主張・数値の変更は一切行っていない。
