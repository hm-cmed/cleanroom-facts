# バッチ95：SB（物質使用・嗜癖障害）5件

- 実施日：2026-11-15
- 対象：SB 章の対象カード全5件（SB-001・SB-002・SB-003・SB-004・SB-006）
- ルール：2026-11-11 のレポジトリ側指示に基づく新ルール（抄録・添付文書・医学百科は根拠にしない。使えるのは政府の全文文書・報告書、CC BY 全文、試験登録レコードなど全文で読める資料のみ。旧来の「先例に基づく A」は廃止）を適用。
- 方法：各カードの主出典（マスター SRC、本バッチでは SRC-3615・3616・3617・3618・3620 の5出典）の刊行版ライセンスを Crossref の版（version of record）データと Europe PMC の個別レコードで1件ずつ確認した。候補は CC BY 全文を実際に読んで裏づけ範囲を判定し、ライセンスは候補ごとに Crossref の版データと PMC 全文のライセンス表示で個別確認した。識別子（PMID・PMCID・DOI）は一括照会の値を使わず、DOI キー・PMID キー・PMCID キーの個別照会で相互に確かめた。出典の説明はマスター（repo_current2 の sources.yaml）の記載からそのまま取った。Europe PMC の全文 XML が断続的に HTTP 500 を返したため、PMC 全文の確認の一部は NCBI E-utilities（efetch）で代替した。本バッチでは Crossref のレート制限（429）には当たらなかった。

## 集計

- A：0件
- B：5件（すべて部分）
- C：0件
- D（マスターの区分訂正）：新規0出典（主出典5出典とも現行 RESTRICTED が正しいことを確認。SRC-3616 はバッチ78 と同一出典・同結論の再確認＝再掲）

## 明細

| 対象 | 判定 | 現行出典（主出典） | 候補 | 区分 | PMID | DOI | PMCID | ライセンス根拠URL | 裏づけ範囲 | 数値照合 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SB-001 | B（部分） | SRC-3615：新アルコール・薬物使用障害の診断治療ガイドライン作成委員会（監修）, 樋口進, 齋藤利和, ほか（編）. 新アルコール・薬物使用障害の診断治療ガイドライン. 新興医学出版社; 2018 | So R, Nouso K, Matsushita S, Yoshiji H, Yuzuriha T, et al. Efficacy and safety of a digital therapeutic for alcohol dependence: A multicenter, open-label, randomized controlled trial. Psychiatry Clin Neurosci. 2025;79(10):667-676 | OPEN | 40719411 | 10.1111/pcn.13874 | PMC12498122 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補（アルコール依存症のデジタル治療アプリの RCT、CC BY）は、その引用文献8として主出典（2018年ガイドライン）を挙げたうえで、「最近の日本の診療ガイドラインは、過度の飲酒による重篤な身体的・精神的・社会的問題のない患者について、飲酒量低減を実現可能な治療目標として記述している」「日本の依存症専門家の多くは飲酒量低減を妥当な中間目標とみなしている」と再掲する。ガイドラインが断酒だけを目標とせず飲酒量低減を治療目標に位置づけたという骨格は裏づけられる。ただし、カードの中心部分、すなわち治療目標は原則として断酒であることと、重症例などで本人が断酒に同意せず説得もうまくいかない場合に治療からの脱落を防ぐため飲酒量低減を暫定的な治療目標とするという推奨の切り分けは、候補では再掲されない（候補が低減を結びつける対象像はガイドラインの軽症側の規定に対応し、カードの重症側の規定とは異なる。申し送り参照） | 数値的主張はカードにない。候補の「日本ではアルコール依存症の人の60〜75%が断酒より飲酒量低減の目標を好む」は別の調査の値であり、カードの主張の裏づけとして登録しないこと | 主出典（SRC-3615）は市販の書籍で DOI・PMID・PMCID は存在せず CC 表示もないため、現行 RESTRICTED が正しい。カードの推奨内容そのものは、精神神経学雑誌の特集論文（湯本洋介, 樋口進. アルコール依存症の新ガイドラインと治療ゴール. 精神経誌. 2021;123(8):475-481）がガイドラインの推奨事項を引用する形で確認でき、カードの記述（原則として断酒、重症例などで断酒に応じない場合に脱落を避けるため飲酒量低減を提案する）と一致するが、同誌は学会誌で CC 表示がなく自由な出典にはならないため候補に数えない。候補のライセンスは Crossref の版データ（CC BY 4.0）と PMC 全文のライセンス表示（CC BY 4.0）で個別確認した |
| SB-002 | B（部分） | SRC-3616：American Society of Addiction Medicine. The ASAM Clinical Practice Guideline on Alcohol Withdrawal Management. J Addict Med. 2020;14(3S Suppl 1):1-72 | Kumar MS, Vaishnav M, Saha G, Raheja D. Management algorithm for alcohol withdrawal syndrome, alcohol dependence (AD) and AD with anxiety in the Indian population: a narrative review with expert opinion. Front Psychiatry. 2026;17:1758995／Ratner JA, Blaney H, Rastegar DA. Management of alcohol withdrawal syndrome in patients with alcohol-associated liver disease. Hepatol Commun. 2024;8(2):e0372 | OPEN／OPEN | 41908117／38251886 | 10.3389/fpsyt.2026.1758995／10.1097/HC9.0000000000000372 | PMC13021624／PMC10805424 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補1（CC BY の管理アルゴリズム論文）は、検索・比較の対象としたガイドラインの一つとして ASAM ガイドラインを挙げ、検証済みの尺度（CIWA-Ar 等）による重症度評価に基づいて入院と外来を振り分ける管理の枠組みと、離脱リスクの同定に家族等からの側副情報を取ることが ASAM の推奨に含まれることを再掲する。候補2（CC BY 総説）は ASAM ガイドラインの推奨をアルコール関連肝疾患という特殊な患者集団へ適用する形で、重症度に基づく入院判断と症状対応型の管理を再掲する。ただし、主出典そのものの範囲表明、すなわち成人のアルコール離脱について重症度に応じた同定と管理を外来と入院の両方の場面について示し、特殊な患者集団への配慮も含むというガイドライン自体の位置づけを、そのまま再掲する自由な全文はない | 数値的主張はカードにない（重症度評価の尺度名と管理の枠組みの定性的な再掲のみ） | 主出典（SRC-3616）は Crossref の版データにライセンス登録がなく Europe PMC でも非 OA で、現行 RESTRICTED が正しい。これは TX-003 と同一出典であり、バッチ78 で確認済みの結論の再確認（再掲）である。識別子補完候補（PMID 32511109）もバッチ78 で提案済みの再掲（二重計上しない。カード側には記録済みでマスターは null）。候補のライセンスはいずれも Crossref の版データ（CC BY 4.0）と Europe PMC の個別レコード（cc by）で個別確認した |
| SB-003 | B（部分） | SRC-3617：Saunders JB, Aasland OG, Babor TF, de la Fuente JR, Grant M. Development of the Alcohol Use Disorders Identification Test (AUDIT): WHO collaborative project on early detection of persons with harmful alcohol consumption--II. Addiction. 1993;88(6):791-804 | López-González A, Buitrago-López A, Rodríguez Malagón N, et al. Strengthening alcohol consumption screening in primary care for culturally diverse populations in Latin America: Adaptation and content and face validity of the AUDIT in Guaviare, Colombia. PLoS One. 2026;21(9):e0359625 | OPEN | 42814685 | 10.1371/journal.pone.0359625 | PMC13626350 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補（AUDIT の文化適応研究、CC BY）は、AUDIT が WHO によってプライマリケアにおける危険な飲酒のスクリーニングのために開発されたこと、10項目が3つの領域（飲酒量＝項目1〜3、依存症状＝項目4〜6、有害な飲酒＝項目7〜10）からなること、各項目0〜4点で合計は0〜40点であること、8点以上が危険な飲酒を示すことを再掲する。WHO の6か国の共同プロジェクトという開発経緯と、開発研究の割合（危険・有害な飲酒の人の92%が8点以上、危険でない飲酒の人の94%が8点未満）は、自由な全文では再掲されない。WHO の AUDIT マニュアル（Babor et al., 2001）は全要素を再掲するが © WHO で CC 表示がなく、自由な出典としては使えない | 部分一致：10項目・3領域・各項目0〜4点・合計40点満点・8点以上という構造とカットオフは候補の再掲と一致する。開発研究の92%と94%は候補に再掲がない。候補が別の出典から引く感度90%・特異度80%は主出典の92%・94%とは別の値であり、カードの値の裏づけとして登録しないこと | 主出典（SRC-3617）の刊行版ライセンスは Wiley の利用条件のみで CC 表示はなく（Crossref の版データに CC の登録はなく、Europe PMC の個別レコードでも非 OA）、現行 RESTRICTED が正しい。識別子補完候補あり（SRC-3617 の PMID。カード側には記録済みでマスターは null）。候補のライセンスは Crossref の版データ（CC BY 4.0）と PMC 全文のライセンス表示（CC BY 4.0）で個別確認した |
| SB-004 | B（部分） | SRC-3618：McKetin R, McLaren J, Lubman DI, Hides L. The prevalence of psychotic symptoms among methamphetamine users. Addiction. 2006;101(10):1473-1478 | Wearne TA, Cornish JL. A Comparison of Methamphetamine-Induced Psychosis and Schizophrenia: A Review of Positive, Negative, and Cognitive Symptomatology. Front Psychiatry. 2018;9:491 | OPEN | 30364176 | 10.3389/fpsyt.2018.00491 | PMC6191498 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補（CC BY 総説）は、その引用文献32（＝主出典 McKetin 2006 であることを引用文献リストで照合済み）に帰属させる形で、「治療を求めていないオーストラリアのメタンフェタミン使用者の研究では、評価時点で13%が精神病のスクリーニングで陽性であり、過去1年間に『臨床的に有意な』精神病症状を報告した者は23%だった」と再掲する。対象者309人・過去1年間に月1回以上使用という標本の枠組みと、メタンフェタミン依存のある使用者では依存のない使用者に比べて精神病症状の経験が約3倍多いという比較は、自由な全文では再掲されない | 部分一致：23%と13%は候補の再掲と一致する。依存の有無による約3倍という値は候補に再掲がない。候補にある「一般人口の2〜3倍」という記述は比較の枠組みが異なる別の値であり、カードの「依存のない使用者に比べて約3倍」の裏づけとして登録しないこと | 主出典（SRC-3618）の刊行版ライセンスは Wiley の利用条件のみで CC 表示はなく（Crossref の版データに CC の登録はなく、Europe PMC の個別レコードでも非 OA）、現行 RESTRICTED が正しい。識別子補完候補あり（SRC-3618 の PMID。カード側には記録済みでマスターは null）。候補のライセンスは Crossref の版データ（CC BY 4.0）と PMC 全文のライセンス要素（CC BY）で個別確認した |
| SB-006 | B（部分） | SRC-3620：Potenza MN, Balodis IM, Derevensky J, et al. Gambling disorder. Nat Rev Dis Primers. 2019;5(1):51 | Sharma R, Weinstein A. Gambling disorder comorbidity: a narrative review. Dialogues Clin Neurosci. 2025;27(1):1-18／Bissig L, Mutschler J. Off-label and investigational drugs in the treatment of gambling disorder: a critical review. Front Pharmacol. 2026;17:1806954 | OPEN／OPEN | 40177908／42147309 | 10.1080/19585969.2025.2484288／10.3389/fphar.2026.1806954 | PMC11980244／PMC13176223 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補1（併存症の総説、CC BY）は、行動的介入として認知行動療法・動機づけ面接・Gamblers Anonymous を並べて挙げ、「ギャンブル障害を正式な適応とする薬物療法はない」と明記し、物質使用障害・アルコール使用障害をはじめとする他の精神疾患との併存の多さを主題として再掲する。候補2（薬物療法の総説、CC BY）は、「公式に承認された薬物療法はまだない」こと、ガイドラインが認知行動療法と動機づけ面接を最良の実践・第一選択として推奨すること、併存する精神疾患への並行治療の必要性を再掲する。米国の成人における有病率0.5%という推定値と、「臨床の場でも見逃されやすい」という位置づけそのものは、自由な全文では再掲されない | 一致する数値なし：カードの有病率0.5%（米国の成人の推定）は候補のいずれにも再掲がない。候補側には他国・他集団の有病率や範囲表示があるが、対象が異なるためカードの値の裏づけとして登録しないこと | 主出典（SRC-3620）の刊行版は Springer Nature の TDM ライセンスのみで CC 表示はなく（Crossref の版データ・Europe PMC の個別レコードとも非 OA）、現行 RESTRICTED が正しい。識別子補完候補あり（SRC-3620 の PMID。カード側には記録済みでマスターは null）。候補のライセンスはいずれも Crossref の版データ（CC BY 4.0）と PMC 全文のライセンス表示（CC BY 4.0）で個別確認した |

## D（マスターの区分訂正）：新規0出典

- 本バッチでは新規の区分訂正はない。対象5件の主出典は5出典（SRC-3615・SRC-3616・SRC-3617・SRC-3618・SRC-3620）で、いずれも現行の RESTRICTED が正しいことを確認した。
- SRC-3615（SB-001 の主出典）：市販の書籍（新興医学出版社、2018）で、DOI・PMID・PMCID はなく CC 表示もない。RESTRICTED が正しい。
- SRC-3616（SB-002 の主出典）：ASAM のアルコール離脱管理ガイドライン（J Addict Med. 2020）。Crossref の版データにライセンス登録がなく、Europe PMC の個別レコードでも非 OA（PMCID なし）。RESTRICTED が正しい。TX-003 と同一出典であり、バッチ78 の確認と同結論の再確認（再掲）として記録する。
- SRC-3617（SB-003 の主出典）：Saunders et al., Addiction 1993。刊行版ライセンスは Wiley の利用条件のみで CC 表示はなく、Europe PMC でも非 OA。RESTRICTED が正しい。
- SRC-3618（SB-004 の主出典）：McKetin et al., Addiction 2006。刊行版ライセンスは Wiley の利用条件のみで CC 表示はなく、Europe PMC でも非 OA。RESTRICTED が正しい。
- SRC-3620（SB-006 の主出典）：Potenza et al., Nat Rev Dis Primers 2019。刊行版は Springer Nature の TDM ライセンスのみで CC 表示はなく、Europe PMC でも非 OA。RESTRICTED が正しい。
- マスターの license_note は5出典とも null であり、実態との食い違いとして申し送る事項はない。

## 識別子補完候補：新規3出典3項目＋再掲1出典1項目（いずれも DOI・PMID キーの個別照会で照合済み）

- SRC-3617：PMID 8329970（新規。カード側には記録済みでマスターが null）
- SRC-3618：PMID 16968349（新規。カード側には記録済みでマスターが null）
- SRC-3620：PMID 31346179（新規。カード側には記録済みでマスターが null）
- SRC-3616：PMID 32511109（再掲。バッチ78 で提案済みであり二重計上しない。カード側には記録済みでマスターが null）

新規分はいずれもマスターの null の欄への補完候補であり、DOI キーと PMID キーの個別照会が互いに一致し、それぞれ当該論文の識別子であることを確認した。SRC-3617・SRC-3618・SRC-3620・SRC-3616 には PMCID が存在しない（いずれも PMC 未収載）。SRC-3615 は和書のため DOI・PMID・PMCID が存在せず、補完候補はない。

## 申し送り

- SB-001 の候補の対象像の食い違い：候補（So et al. 2025）は飲酒量低減を「重篤な身体的・精神的・社会的問題のない患者」に結びつけており、これはガイドラインの軽症側の規定に対応する。カードが述べる重症側の規定（本人が断酒に同意せず説得もうまくいかない場合に、治療からの脱落を防ぐため飲酒量低減を暫定的な目標とする）は、ガイドラインの推奨事項を引用する精神神経学雑誌の特集論文（2021;123(8):475-481、自由な出典ではない）でのみ逐語的に確認できる。裏づけ登録は「ガイドラインが飲酒量低減を治療目標に位置づけた」という骨格に限り、候補の対象像の表現をカードの重症例の条件の裏づけとして使わないこと。なお、カードの記述自体は特集論文の引用する推奨文と一致しており、カード側の誤りは認めなかった。
- SB-002 の主出典 SRC-3616 は TX-003 と同一出典である。区分 RESTRICTED の再確認と PMID 32511109 の補完候補はバッチ78 の再掲であり、二重計上しないこと。
- SB-003 の再調査候補：AHRQ の Evidence Synthesis No. 171（Bookshelf NBK534916、米国政府著作物）は AUDIT を扱う政府の全文報告書だが、本バッチでは本文における AUDIT の記述範囲を確認していないため候補に数えていない。登録側で本文を確認できれば裏づけが広がる可能性がある。WHO の AUDIT マニュアル（2001）は全要素を再掲するが © WHO で CC 表示がなく使えない。
- 候補側の数値の扱い：SB-003 候補の感度90%・特異度80%、SB-004 候補の「一般人口の2〜3倍」、SB-006 候補側の他国・他集団の有病率は、いずれもカードの値とは別の報告または別の枠組みの値であり、裏づけ登録時にカードの値の裏づけとして使わないこと。
- 方法上の注記：Europe PMC の全文 XML が断続的に HTTP 500 を返したため、PMC 全文の確認の一部は NCBI E-utilities（efetch、db=pmc）で代替した。本バッチでは Crossref のレート制限（429）には当たらなかった。
- 主出典・候補とも識別子の誤記（別論文の識別子の混入）は本バッチでは発見されなかった。主出典5出典と候補7件の識別子は DOI キー・PMID キー・PMCID キーの個別照会で相互に照合した。
- 本バッチの判定は以上で完結しており、カードの主張・数値の変更は一切行っていない。
