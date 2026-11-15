# バッチ96：MY（結核・非結核性抗酸菌症）4件

- 実施日：2026-11-15
- 対象：MY 章の対象カード全4件（MY-001・MY-003・MY-004・MY-005）
- ルール：2026-11-11 のレポジトリ側指示に基づく新ルール（抄録・添付文書・医学百科は根拠にしない。使えるのは政府の全文文書・報告書、CC BY 全文、試験登録レコードなど全文で読める資料のみ。旧来の「先例に基づく A」は廃止）を適用。
- 方法：各カードの主出典（マスター SRC、本バッチでは SRC-2146・SRC-2148・SRC-2149・SRC-2150 の4出典）の刊行版ライセンスを Crossref の版（version of record）データと Europe PMC の個別レコードで1件ずつ確認した。候補は政府の全文ページと CC BY 全文を実際に読んで裏づけ範囲を判定し、ライセンスは候補ごとに Crossref の版データ、Europe PMC の個別レコード、PMC 全文のライセンス要素で個別確認した。識別子（PMID・PMCID・DOI）は一括照会の値を使わず、DOI キー・PMID キー・PMCID キーの個別照会で相互に確かめた。出典の説明はマスター（repo_current2 の sources.yaml）の記載からそのまま取った。Europe PMC の全文 XML が1件で HTTP 500 を返したため、その文献の全文確認は NCBI E-utilities（efetch）で代替した。本バッチでは Crossref のレート制限（429）には当たらなかった。

## 集計

- A：0件
- B：4件（すべて部分）
- C：0件
- D（マスターの区分訂正）：新規0出典（主出典4出典とも現行 RESTRICTED が正しいことを確認）

## 明細

| 対象 | 判定 | 現行出典（主出典） | 候補 | 区分 | PMID | DOI | PMCID | ライセンス根拠URL | 裏づけ範囲 | 数値照合 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MY-001 | B（部分） | SRC-2146：World Health Organization. Tuberculosis（ファクトシート、2024年データ、2026-03-24更新） | Chen F, Zhang Y, Chen L. Global financing retrenchment threatens the recovery in TB control. IJTLD Open. 2026;3(10):681-682／Myat Y, Cerrone M, Kon OM. What is new in tuberculosis? Clin Med (Lond). 2026;26(5):100634 | OPEN／OPEN | 42866169／42575374 | 10.5588/ijtldopen.26.0371／10.1016/j.clinme.2026.100634 | PMC13657025／PMC13520985 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補1（IJTLD Open の編集記事、CC BY）は「2024年には推計1,070万人が発症し、123万人が死亡した（うち HIV 陽性者は15万人）」と、主出典の基になった Global Tuberculosis Report 2025 の値をそのまま再掲する。候補2（Clin Med の総説、CC BY）は「2024年に推計1,070万人が結核を発症した」「世界人口の約4分の1が潜在性結核感染症を有すると推定される」を再掲する。感染した人のうち発症するのは約5〜10%であるという要素は、自由な全文では再掲されない（CDC の一般向けページは「未治療では不活性結核の10人に1人が発症する」とするが、これは未治療の潜在性感染を分母とする別の枠組みの値であり、5〜10%の再掲には数えない。申し送り参照） | 一致：発症1,070万人・死亡123万人（2024年）は候補1の再掲と一致し、発症数は候補2も再掲する。世界人口の約4分の1は候補2の再掲と一致する。発症割合5〜10%は候補のいずれにも再掲がない。なお主出典のファクトシート現行版（2026-11-12更新）は2025年データ（発症1,060万人・死亡113万人）に差し替わっており、カードの値はカードが引用する版（2026-03-24更新、2024年データ）の値として正しい（監視事項として申し送り） | 主出典（SRC-2146）は WHO のファクトシートで、個別のライセンス表示はページ上に特定できず、マスターの license_note のとおり WHO 出版物の標準ライセンス（CC BY-NC-SA IGO 系、NC・SA を含む）に基づくため自由とはいえず、現行 RESTRICTED が正しい。候補のライセンスはいずれも個別確認した（候補1は PMC 全文のライセンス要素と Europe PMC の個別レコードで CC BY 4.0。Crossref にはライセンス登録なし。候補2は Crossref の版データ・Europe PMC の個別レコード・PMC 全文の表示で CC BY 4.0） |
| MY-003 | B（部分） | SRC-2148：Pai M, Behr MA, Dowdy D, et al. Tuberculosis. Nat Rev Dis Primers. 2016;2:16076 | Centers for Disease Control and Prevention. About Tuberculosis（CDC 公式ページ、2025-01-17版、https://www.cdc.gov/tb/about/index.html）／Esmail H, Barry CE 3rd, Young DB, Wilkinson RJ. The ongoing challenge of latent tuberculosis. Philos Trans R Soc Lond B Biol Sci. 2014;369(1645):20130437 | GOV_US／OPEN | 24821923（候補2。候補1は政府のウェブページで PMID なし） | 10.1098/rstb.2013.0437（候補2。候補1は DOI なし） | PMC4024230（候補2。候補1は PMCID なし） | https://creativecommons.org/licenses/by/3.0/ | 部分：候補1（CDC、GOV_US）は、結核が空気を介して人から人へ広がること、不活性結核（潜在性結核感染症）と活動性結核という2つの状態があること、不活性結核の人は他者にうつさないこと、感染を広げるのは肺または喉頭の活動性結核の人であることを再掲する。候補2（CC BY の総説）は、感染が制御された静止状態から無症状の活動性に近い状態までを両端とする感染状態のスペクトラムという枠組み、初感染後に細胞性免疫応答が発達して肉芽腫が形成され感染の制御に働くこと、5µm 未満の飛沫核が空気中に浮遊して吸入される空気伝播を再掲する。ただし「伝染性があるのは活動性肺結核のみ」という厳密な形は再掲されず（候補1は肺に加えて喉頭を含む）、Mycobacterium tuberculosis complex という複合体としての明示もない（候補1は主病原体を M. tuberculosis とし、M. bovis 等も人の結核の原因になりうると述べるにとどまる） | 数値的主張はカードにない（定性的な枠組みの再掲のみ） | 主出典（SRC-2148）の刊行版ライセンスは Crossref の版データで Springer Nature の TDM のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載（PMCID は存在しない）で、現行 RESTRICTED が正しい。候補2のライセンスは PMC 全文のライセンス要素（CC BY 3.0）と Europe PMC の個別レコード（cc by）で個別確認した（Crossref の版データには TDM のみの登録） |
| MY-004 | B（部分） | SRC-2149：Prevots DR, Marras TK. Epidemiology of human pulmonary infection with nontuberculous mycobacteria: a review. Clin Chest Med. 2015;36(1) | Ratnatunga CN, Lutzky VP, Kupz A, Doolan DL, Reid DW, Field M, Bell SC, Thomson RM, Miles JJ. The Rise of Non-Tuberculosis Mycobacterial Lung Disease. Front Immunol. 2020;11:303／Dahl VN, Pedersen AA, Norman A, Rasmussen EM, van Ingen J, Andersen AB, Wejse CM, Lillebaek T. Clinical Significance, Species Distribution, and Temporal Trends of Nontuberculous Mycobacteria, Denmark, 1991-2022. Emerg Infect Dis. 2024;30(9):1755-1762 | OPEN／GOV_US | 32194556／39173666 | 10.3389/fimmu.2020.00303／10.3201/eid3009.240095 | PMC7062685／PMC11346989 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補1（CC BY の総説）は、北米・欧州・アジアのいずれでも過去20年間に NTM 症の発生が増えていること、世界的に最も多い NTM の病原体は MAC であることを再掲する。候補2（デンマークの全国データ、GOV_US）は、1991〜2022年に肺 NTM 症の発生率が増加し続けたこと、M. malmoense がスカンジナビア以外の地域に比べて北欧で際立って多いこと、M. xenopi と M. kansasii はデンマークでは東欧・南欧に比べてまれであること（すなわち東欧・南欧では相対的に多いこと）を再掲する。ただし、MAC が「北米と東アジアで優位」という地域の組み合わせそのものと、欧州の一部地域で kansasii・xenopi・malmoense の3菌種が多いという主出典の形の再掲は、自由な全文にはない（候補2はデンマーク1国のデータと地域間の対比にとどまる） | 数値の一致を主張するものではない。候補2の菌種別割合（デンマークで MAC が肺 NTM の58%、M. malmoense 4.2%等）はデンマーク1国の値であり、カードの地域分布の記述の裏づけとして数値そのものは使わないこと | 主出典（SRC-2149）の刊行版ライセンスは Crossref の版データで Elsevier の TDM のみで CC 表示はなく、現行 RESTRICTED が正しい。PMC 収載コピー（PMC4332564）は著者稿でライセンス表示はなく、自由とはいえない。識別子補完候補あり（SRC-2149 の PMCID。カード側には記録済みでマスターは null）。候補のライセンスは個別確認した（候補1は Crossref の版データ・Europe PMC の個別レコード・PMC 全文のライセンス要素で CC BY 4.0。候補2は PMC 全文のライセンス要素が米国政府刊行物として public domain と明示し、Europe PMC の個別レコードでも cc by） |
| MY-005 | B（部分） | SRC-2150：Falkinham JO 3rd. Environmental sources of nontuberculous mycobacteria. Clin Chest Med. 2015;36(1) | Ratnatunga CN, Lutzky VP, Kupz A, Doolan DL, Reid DW, Field M, Bell SC, Thomson RM, Miles JJ. The Rise of Non-Tuberculosis Mycobacterial Lung Disease. Front Immunol. 2020;11:303 | OPEN | 32194556 | 10.3389/fimmu.2020.00303 | PMC7062685 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補（CC BY の総説）は、NTM が水系・土壌・植生に生息する遍在性の環境腐生菌であること、生息地が自然の水域から市営の配水システムや家庭の配管（飲料水を含む）まで及ぶこと、ヒト感染の源が環境であるという位置づけを再掲する。また、治療による寛解率が感染菌種によって異なること、感染菌種の迅速な同定が研究上の優先事項とされていることも述べ、菌種ごとの性質の違いと種レベルの同定の重要性の骨格は裏づけられる。ただし、菌種ごとに生態・抗菌薬感受性・病原性が異なるという3点の明示的な形では再掲されない | 菌種数：カードは「150種を超える（2015年時点）」とし、候補は「170種を超える同定済み菌種」（2020年の総説）とする。候補の値は時点の新しい別の集計であり、カードの2015年時点の値の裏づけとして登録しないこと（方向は一致する。カードの uncertainty 自身が2020年の治療ガイドラインの「190種を超える種・亜種」に言及している） | 主出典（SRC-2150）の刊行版ライセンスは Crossref の版データで Elsevier の TDM のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載（PMCID は存在しない）で、現行 RESTRICTED が正しい。候補のライセンスは Crossref の版データ・Europe PMC の個別レコード・PMC 全文のライセンス要素で CC BY 4.0 と個別確認した |

## D（マスターの区分訂正）：新規0出典

- 本バッチでは新規の区分訂正はない。対象4件の主出典は4出典（SRC-2146・SRC-2148・SRC-2149・SRC-2150）で、いずれも現行の RESTRICTED が正しいことを確認した。
- SRC-2146（MY-001 の主出典）：WHO の結核ファクトシート。個別のライセンス表示はページ上に特定できないが、マスターの license_note のとおり WHO 出版物の標準ライセンス（CC BY-NC-SA IGO 系）は NC・SA を含み自由ではない。RESTRICTED が正しい。
- SRC-2148（MY-003 の主出典）：Pai et al., Nat Rev Dis Primers 2016。Crossref の版データは Springer Nature の TDM のみで CC 表示はなく、Europe PMC でも非 OA・PMC 未収載。RESTRICTED が正しい。
- SRC-2149（MY-004 の主出典）：Prevots & Marras, Clin Chest Med 2015。Crossref の版データは Elsevier の TDM のみで CC 表示はなく、PMC 収載コピーはライセンス表示のない著者稿。RESTRICTED が正しい。
- SRC-2150（MY-005 の主出典）：Falkinham, Clin Chest Med 2015。Crossref の版データは Elsevier の TDM のみで CC 表示はなく、Europe PMC でも非 OA・PMC 未収載。RESTRICTED が正しい。
- マスターの license_note は4出典とも実態と一致しており、文言の更新提案はない。

## 識別子補完候補：新規1出典1項目（DOI・PMID・PMCID キーの個別照会で照合済み）

- SRC-2149：PMCID PMC4332564（新規。カード側には記録済みでマスターが null）

新規分はマスターの null の欄への補完候補であり、DOI キー・PMID キー・PMCID キーの個別照会が互いに一致し、当該論文（Prevots & Marras, Clin Chest Med. 2015;36(1):13-34）の識別子であることを確認した。PMC 収載コピーは著者稿でライセンス表示はなく、区分は RESTRICTED のままである。SRC-2148 と SRC-2150 には PMCID が存在せず（いずれも PMC 未収載）、SRC-2146 はウェブページのため DOI・PMID・PMCID は存在しない。

## 申し送り

- MY-001 の監視事項：主出典の WHO ファクトシートは 2026-11-12 に2025年データ（Global Tuberculosis Report 2026）へ更新済みで、現行版の値は発症1,060万人・死亡113万人（うち HIV 陽性者13.7万人）である。カードの数値（発症1,070万人・死亡123万人）は、カードが引用する版（2026-03-24更新、2024年データ、Global Tuberculosis Report 2025）の値として本バッチの裏づけ候補とも一致しており、カード側の誤りではない。次回改訂時に2025年データへの照合が必要。なお「世界人口の約4分の1が感染」「感染した人のうち発症するのは約5〜10%」の記述は現行版にもそのまま残っている。
- MY-001 の発症割合5〜10%は自由な全文に再掲がない。CDC の一般向けページ（About Tuberculosis）の「未治療では不活性結核の10人に1人が発症する」は、未治療の潜在性感染を分母とする別の枠組みの値であり、5〜10%の裏づけとして登録しないこと。
- MY-003 の感染性の範囲：候補1（CDC）は感染源を「肺または喉頭の活動性結核」とし、カード（主出典 Pai 2016）の「活動性肺結核のみ」より喉頭を含む分だけ広い。裏づけ登録は「潜在性結核は感染性がなく、活動性の肺結核が感染源になる」という骨格に限り、候補1の喉頭の文言をもってカードの記述と矛盾すると扱わないこと。
- MY-004 の地域分布：候補はいずれも主出典の地域の組み合わせ（MAC は北米と東アジアで優位、kansasii・xenopi・malmoense は欧州の一部地域で多い）をそのままは再掲しない。候補1は世界的に MAC が最多という水準、候補2はデンマーク1国のデータと北欧／東欧・南欧の対比にとどまる。候補2の菌種別割合はデンマークの値であり、カードの記述の数値的な裏づけとして登録しないこと。
- MY-005 の菌種数：候補の「170種を超える」は2020年時点の集計で、カードの「150種を超える（2015年時点）」とは時点が異なる。方向は一致するが、カードの値の裏づけとして登録しないこと。
- 方法上の注記：Europe PMC の全文 XML が PMC13520985（MY-001 候補2）で HTTP 500 を返したため、同文献の全文確認は NCBI E-utilities（efetch、db=pmc）で代替した。本バッチでは Crossref のレート制限（429）には当たらなかった。
- 主出典・候補とも識別子の誤記（別論文の識別子の混入）は本バッチでは発見されなかった。主出典4出典と候補7件の識別子は DOI キー・PMID キー・PMCID キーの個別照会で相互に照合した。
- 本バッチの判定は以上で完結しており、カードの主張・数値の変更は一切行っていない。
