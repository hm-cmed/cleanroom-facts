# 根拠に基づく医療・研究方法（EB）第1陣：EB-001〜012（カード12件）

依頼文（round_EB1_request.md、2026-11-26）に基づく新シリーズ第1陣の12枚。決定事項の適用は次のとおり。

- 作業前に取得したレポジトリ：hm-cmed/cleanroom-facts 最新版、コミット `e3e6e27`（2026-11-26、EB分野追加と本依頼文の登録を含む）。受け入れ仕様（roundEB1.yaml：EB-001から、SRC-5500〜5599、12〜13件）を確認した。
- カリキュラム欄（kokushi・core_curriculum）は全件 null とし、`condition.対象` には研究者・医療者・ガイドライン作成者などを書いた（依頼文 §1-2）。
- 新規出典は SRC-5500〜5515 を割り当てた。出典マスター（最新版 sources.yaml）と DOI・PMID で照合し、本ファイルの新規出典はいずれも未登録であることを確認した。
- ライセンスは依頼文 §3-8 に従い、BMJ 論文を中心に Crossref の license と PMC・出版社のページの両方で1件ずつ確かめた。分割案の「CC BY の見立て」は4件で誤りであり、RoB 2・EtD・GRADE 2008 は CC 表示なし、GRIPP2 は CC BY-NC 4.0 で、いずれも RESTRICTED とした（検証記録 §5-2）。
- 依頼文 §3 の指摘への対応：EB-002 の主出典は Cochrane Handbook Ch.8（割付の仕組みの明文がある章）に変更し「唯一の割付方法」の表現は使っていない。EB-006 の数値は Waffenschmidt らの本文（全文）で確かめた。EB-008 は下げる要因と上げる要因を1枚に収め、分割はしなかった（過密回避のため記述は骨格に限った）。EB-010 の判断項目は論文の表の12項目を過不足なく挙げた。EB-012 の主出典は現行の NIHR 文書とし、AMED ガイドブックを日本の裏づけとして併記した。
- 定義文・結論文の翻訳転載、チェックリスト項目文・表・図の転写はしていない。項目数と概念名のみを書いた。数値は一次資料の本文で確かめたものだけを書いた。

## 1. 出典表

| SRC | 出典 | DOI | PMID | ライセンス表示 | legal_basis | source_class | 使うカード |
|---|---|---|---|---|---|---|---|
| SRC-5500 | Higgins JPT, Savović J, Page MJ, Elbers RG, Sterne JAC. Chapter 8: Assessing risk of bias in a randomized trial. In: Cochrane Handbook for Systematic Reviews of Interventions version 6.5. Cochrane; 2024（オンライン版、training.cochrane.org/handbook） | なし | なし | © The Cochrane Collaboration（章ごとに CC 表示がないことを確認） | B | RESTRICTED | EB-001（Ch.2・Ch.5 相当を含む Handbook 全体として）, EB-002, EB-006（裏づけ） |
| SRC-5501 | Richardson WS, Wilson MC, Nishikawa J, Hayward RSA. The well-built clinical question: a key to evidence-based decisions. ACP J Club. 1995;123(3):A12-A13 | なし | なし | © American College of Physicians（CC表示なし） | B | RESTRICTED | EB-001（裏づけ） |
| SRC-5502 | Moher D, Hopewell S, Schulz KF, et al. CONSORT 2010 explanation and elaboration: updated guidelines for reporting parallel group randomised trials. BMJ. 2010;340:c869 | 10.1136/bmj.c869 | 20332511 | CC BY-NC 2.0（PMC2844943 の license 表示） | B | RESTRICTED | EB-002（裏づけ） |
| SRC-5503 | Wasserstein RL, Lazar NA. The ASA Statement on p-Values: Context, Process, and Purpose. The American Statistician. 2016;70(2):129-133 | 10.1080/00031305.2016.1154108 | なし | © American Statistical Association（Crossref に license 登録なし、出版社ページに CC 表示なし） | B | RESTRICTED | EB-003 |
| SRC-5504 | Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71 | 10.1136/bmj.n71 | 33782057 | CC BY 4.0（PMC8005924 の license 表示、Crossref と一致） | B | OPEN | EB-004 |
| SRC-5505 | Rethlefsen ML, Kirtley S, Waffenschmidt S, et al. PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. Systematic Reviews. 2021;10:39 | 10.1186/s13643-020-01542-z | 33499930 | CC BY 4.0（PMC7839230 の license 表示、Crossref と一致） | B | OPEN | EB-005 |
| SRC-5506 | McGowan J, Sampson M, Salzwedel DM, Cogo E, Foerster V, Lefebvre C. PRESS Peer Review of Electronic Search Strategies: 2015 Guideline Statement. Journal of Clinical Epidemiology. 2016;75:40-46 | 10.1016/j.jclinepi.2016.01.021 | 27005575 | © 2016 The Authors. Published by Elsevier Inc.（CC表示なし） | B | RESTRICTED | EB-005（裏づけ） |
| SRC-5507 | Waffenschmidt S, Knelangen M, Sieben W, Bühn S, Pieper D. Single screening versus conventional double screening for study selection in systematic reviews: a methodological systematic review. BMC Medical Research Methodology. 2019;19:132 | 10.1186/s12874-019-0782-0 | 31253092 | CC BY 4.0（PMC6599339 の license 表示） | B | OPEN | EB-006 |
| SRC-5508 | Sterne JAC, Savović J, Page MJ, et al. RoB 2: a revised tool for assessing risk of bias in randomised trials. BMJ. 2019;366:l4898 | 10.1136/bmj.l4898 | 31462531 | CC表示なし（Crossref は BMJ の TDM ライセンスのみ。PMC 未収載、Europe PMC で Open Access でないことを確認） | B | RESTRICTED | EB-007 |
| SRC-5509 | Guyatt GH, Oxman AD, Vist GE, et al. GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. BMJ. 2008;336(7650):924-926 | 10.1136/bmj.39489.470347.AD | 18436948 | © BMJ Publishing Group Ltd 2008（PMC2335261 に CC の license 表示なし） | B | RESTRICTED | EB-008 |
| SRC-5510 | Schünemann H, Brożek J, Guyatt G, Oxman A, eds. GRADE Handbook. GRADE Working Group（オンライン版、gdt.gradepro.org/app/handbook） | なし | なし | GRADE Working Group（オンライン版、版は更新年月で特定。CC表示なし） | B | RESTRICTED | EB-008（裏づけ）, EB-009（裏づけ） |
| SRC-5511 | Andrews JC, Schünemann HJ, Oxman AD, et al. GRADE guidelines: 15. Going from evidence to recommendation—determinants of a recommendation's direction and strength. Journal of Clinical Epidemiology. 2013;66(7):726-735 | 10.1016/j.jclinepi.2013.02.003 | 23570745 | © 2013 Elsevier Inc.（CC表示なし） | B | RESTRICTED | EB-009 |
| SRC-5512 | Alonso-Coello P, Schünemann HJ, Moberg J, et al. GRADE Evidence to Decision (EtD) frameworks: a systematic and transparent approach to making well informed healthcare choices. 2: Clinical practice guidelines. BMJ. 2016;353:i2089 | 10.1136/bmj.i2089 | 27365494 | CC表示なし（Crossref は BMJ の TDM ライセンスのみ。PMC 未収載） | B | RESTRICTED | EB-010 |
| SRC-5513 | Staniszewska S, Brett J, Simera I, et al. GRIPP2 reporting checklists: tools to improve reporting of patient and public involvement in research. BMJ. 2017;358:j3453 | 10.1136/bmj.j3453 | 28768629 | CC BY-NC 4.0（PMC5539518 の license 表示） | B | RESTRICTED | EB-011 |
| SRC-5514 | National Institute for Health and Care Research (NIHR). Briefing notes for researchers: public involvement in NHS, health and social care research. NIHR; 2021（文書番号 27371、nihr.ac.uk） | なし | なし | 文書・ページにライセンス表示なし（確認できていないため UNKNOWN とし、RESTRICTED と同じ扱い） | B | UNKNOWN | EB-012 |
| SRC-5515 | 国立研究開発法人日本医療研究開発機構（AMED）. 患者・市民参画（PPI）ガイドブック ～患者と研究者の協働を目指す第一歩として～. AMED; 2019年4月 | なし | なし | AMED サイトポリシー：著作権は AMED に帰属し、出典明示の上での著作権法の範囲内の引用等を認め、商業利用は事前連絡が必要（オープンライセンスの付与なし） | B | RESTRICTED | EB-012（裏づけ） |

## 2. 事実カード（YAML）

```yaml
- id: EB-001
  domain: EB
  subdomain: EBMの基礎
  assertion:
    plain_statement_ja: PICOは、臨床上の疑問を、対象（Patient）、介入（Intervention）、比較（Comparison）、アウトカム（Outcome）の4要素に分けて構造化する枠組みである。疑問をこの形に整えることで、文献検索の語の組み立てと、システマティックレビューでどの研究を採用するかを決める適格基準の両方に、そのまま使える形になる。治療の疑問で生まれた枠組みだが、疑問の種類に応じて要素の置き方は変わり、曝露を扱う場合は介入の代わりに曝露を置く（PECO）などの形も使われる。
    condition:
      region: 国際
      対象: 医療者・研究者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5500
    source: 'Higgins JPT, Thomas J, Chandler J, et al, eds. Cochrane Handbook for Systematic Reviews of Interventions version 6.5. Cochrane; 2024（オンライン版。疑問の設定と適格基準に関する章）'
    doi: null
    pmid: null
    pmcid: null
    url: https://training.cochrane.org/handbook/current
    source_license: © The Cochrane Collaboration（章ごとに CC 表示がないことを確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: 'PICOの起源は Richardson WS et al. The well-built clinical question: a key to evidence-based decisions. ACP J Club. 1995（SRC-5501）で、構造化された疑問の立て方を提示した論文として位置づけられる'
  uncertainty: '主出典はオンライン版の Handbook（version 6.5、2024年）で、2026-11-26 に参照した。章の内容は版によって更新されるため、版と参照日をここに残す。Richardson 1995 には PMID・DOI が付与されていないため、題名・誌名・年で登録した。'
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-002
  domain: EB
  subdomain: EBMの基礎
  assertion:
    plain_statement_ja: 無作為割付が機能すると、割付に予後因子が影響することが避けられ、既知のものでも未知のものでも、予後因子は平均としては各群で等しくなる。そのため、群の差を介入の効果として読みやすくなる。仕組みは2つの工程からなる。割付の順序を無作為に作ることと、その順序を、参加者の登録が確定するまで参加者や試験担当者に知らせないこと（割付の隠蔽）である。次の割付が分かってしまうと、予後を見て登録するかどうかや登録の時期を選ぶことができてしまい、無作為化の利点が崩れる。なお、群間で予後が等しくなるのは平均としての性質で、規模の小さい試験では偶然の偏りが残ることがある。
    condition:
      region: 国際
      対象: 医療者・研究者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5500
    source: 'Higgins JPT, Savović J, Page MJ, Elbers RG, Sterne JAC. Chapter 8: Assessing risk of bias in a randomized trial. In: Cochrane Handbook for Systematic Reviews of Interventions version 6.5. Cochrane; 2024（オンライン版）'
    doi: null
    pmid: null
    pmcid: null
    url: https://training.cochrane.org/handbook/current/chapter-08
    source_license: © The Cochrane Collaboration（章ごとに CC 表示がないことを確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: 同じ内容は CONSORT 2010 の解説論文（Moher D et al. BMJ. 2010、SRC-5502、CC BY-NC 2.0）でも、適切に行われた無作為割付が選択バイアスを取り除き既知・未知の予後因子を均衡させる、と裏づけられる
  uncertainty: '分割案にあった「唯一の割付方法」という表現は、出典にその旨の記述がないため使っていない。主出典は Handbook version 6.5 の Chapter 8（最終更新2019年10月）で、2026-11-26 に参照した。RoB 2 の論文（SRC-5508）は割付の仕組みの説明としては弱いため、本カードの主出典にはしていない（依頼文 §3-1 への対応）。'
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-003
  domain: EB
  subdomain: EBMの基礎
  assertion:
    plain_statement_ja: p値は、帰無仮説を含む統計モデルの前提のもとで、観測されたデータ（またはそれより極端なデータ）がどれくらい出にくいかを示す指標である。仮説そのものが正しい確率を示すものではなく、効果の大きさや臨床的な重要性を示すものでもない。米国統計学会は2016年の声明で、p値の解釈に関する原則を示した。その要点は、p値だけで科学的な結論や意思決定を決めないこと、結果の選び方によって解釈が歪むため行った解析を透明に報告すること、0.05のような境界で「有意／非有意」に二分して結論を固定しないことにある。
    condition:
      region: 国際
      対象: 医療者・研究者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5503
    source: 'Wasserstein RL, Lazar NA. The ASA Statement on p-Values: Context, Process, and Purpose. The American Statistician. 2016;70(2):129-133'
    doi: 10.1080/00031305.2016.1154108
    pmid: null
    pmcid: null
    url: https://doi.org/10.1080/00031305.2016.1154108
    source_license: © American Statistical Association（Crossref に license 登録なし、出版社ページに CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 声明の6原則は、原文の文を訳したり並べたりせず、要点を自作の文でまとめた（依頼文 §3-2 への対応）。この論文は PubMed 未収載で PMID がなく、DOI で特定した。声明は p値の使用自体を禁じるものではない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-004
  domain: EB
  subdomain: レビュー論文の作成
  assertion:
    plain_statement_ja: PRISMA 2020は、システマティックレビューの報告の仕方を定めた声明で、27項目のチェックリストとフロー図からなる。チェックリストは、題名、抄録、背景、方法、結果、考察などの区分に沿って、何を報告すべきかを示す。フロー図は、文献の特定、スクリーニング、適格性の確認、採用という流れの中で、各段階に残った文献数と除外の理由を記録するものである。PRISMAは報告のための指針であり、レビューの実施方法そのものや、完成したレビューの質を評価する道具ではない。
    condition:
      region: 国際
      対象: 研究者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5504
    source: 'Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71'
    doi: 10.1136/bmj.n71
    pmid: '33782057'
    pmcid: PMC8005924
    url: https://doi.org/10.1136/bmj.n71
    source_license: CC BY 4.0（PMC8005924 の license 表示、Crossref と一致）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: チェックリストの項目文そのものは転記していない。項目数（27項目）は論文の公表値である。介入のレビューが主対象で、他の種類のレビューには拡張版や適用上の注意がある点は本カードでは扱っていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-005
  domain: EB
  subdomain: レビュー論文の作成
  assertion:
    plain_statement_ja: 文献検索の過程も、レビューの再現性に関わる報告の対象である。PRISMA-Sは、システマティックレビューの文献検索を報告するための16項目の拡張指針で、使ったデータベース、検索式の全文、検索した日付、同僚査読の有無などを報告の対象とする。検索式の同僚査読についてはPRESSという枠組みがあり、別の情報専門家が、研究疑問の検索への置き換え、AND・ORなどの演算子、件名標目、自由語、綴りや構文、制限やフィルターの6つの面から検索式の誤りを点検する。検索の漏れは後の統計処理では取り戻せないため、検索式は作って終わりではなく、報告と査読の対象になる。
    condition:
      region: 国際
      対象: 研究者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5505
    source: 'Rethlefsen ML, Kirtley S, Waffenschmidt S, et al. PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. Systematic Reviews. 2021;10:39'
    doi: 10.1186/s13643-020-01542-z
    pmid: '33499930'
    pmcid: PMC7839230
    url: https://doi.org/10.1186/s13643-020-01542-z
    source_license: CC BY 4.0（PMC7839230 の license 表示、Crossref と一致）
    legal_basis: B
    source_class: OPEN
    corroboration: 'PRESSの6つの点検面は McGowan J et al. PRESS Peer Review of Electronic Search Strategies: 2015 Guideline Statement. J Clin Epidemiol. 2016（SRC-5506）で裏づけられる'
  uncertainty: PRISMA-Sの項目文そのものは転記していない（項目数16は公表値）。PRESSの点検面は2015年版のガイドライン声明に基づく。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-006
  domain: EB
  subdomain: レビュー論文の作成
  assertion:
    plain_statement_ja: システマティックレビューの研究選択では、2人が独立に行う方法が標準とされる。1人だけでタイトル・抄録のスクリーニングを行った場合に、採用すべき研究をどれくらい見落とすかを調べた方法論研究の系統的レビュー（評価研究4件、単独スクリーニング23回分、スクリーニングされた文献41,730件）では、見落としの割合は中央値5%（範囲0〜58%）だった。経験の豊富なレビュアーでは中央値3%、経験の浅いレビュアーでは中央値13%と、経験によって差があった。見落とした研究を入れてメタ解析をやり直すと、結果が実質的に変わる場合もあった。このため単独スクリーニングは二重スクリーニングと同等とはみなされておらず、経験豊富なレビュアーが行う迅速レビューでの方法上の近道として、条件付きで許容されうるにとどまる。
    condition:
      region: 国際
      対象: 研究者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5507
    source: 'Waffenschmidt S, Knelangen M, Sieben W, Bühn S, Pieper D. Single screening versus conventional double screening for study selection in systematic reviews: a methodological systematic review. BMC Medical Research Methodology. 2019;19:132'
    doi: 10.1186/s12874-019-0782-0
    pmid: '31253092'
    pmcid: PMC6599339
    url: https://doi.org/10.1186/s12874-019-0782-0
    source_license: CC BY 4.0（PMC6599339 の license 表示）
    legal_basis: B
    source_class: OPEN
    corroboration: Cochrane Handbook（SRC-5500、研究の選択に関する章）は、2人が独立して選択を行うことを標準的な手順として示している
  uncertainty: 数値（評価研究4件、23回分、41,730件、見落とし中央値5%・範囲0〜58%、経験別3%と13%）は主出典の本文（全文）で確認した（依頼文 §3-9 への対応）。対象はタイトル・抄録のスクリーニングで、全文スクリーニングの単独実施はこの研究では検証されていない。根拠となる評価研究が4件と少ないことは著者らも限界として挙げている。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-007
  domain: EB
  subdomain: レビュー論文の作成
  assertion:
    plain_statement_ja: RoB 2は、ランダム化比較試験の結果についてバイアスのリスクを評価する道具である。評価は試験全体ではなく、結果（アウトカムの測定結果）ごとに行う。見る観点は5つに整理されており、無作為化の過程、意図した介入からの逸脱、アウトカムデータの欠測、アウトカムの測定、報告された結果の選択、である。各観点と全体の判定は、低リスク、いくらか懸念あり、高リスクの3段階で表す。点数を合計して1つの数値にする仕組みはなく、全体の判定は、原則として最も悪い観点の判定にそろえる形で決まる。
    condition:
      region: 国際
      対象: 研究者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5508
    source: 'Sterne JAC, Savović J, Page MJ, et al. RoB 2: a revised tool for assessing risk of bias in randomised trials. BMJ. 2019;366:l4898'
    doi: 10.1136/bmj.l4898
    pmid: '31462531'
    pmcid: null
    url: https://doi.org/10.1136/bmj.l4898
    source_license: CC表示なし（Crossref は BMJ の TDM ライセンスのみ。PMC 未収載、Europe PMC で Open Access でないことを確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: '「合計点を付けない」は、論文に禁止の文があるのではなく、判定が観点ごとの3段階のみで数値スコアの仕組み自体がないことから書いた（依頼文 §3-3 への対応。全体判定の決め方は論文の Table 3 と Handbook Ch.8 で確認）。分割案にあった「CC BY の見立て」は誤りで、本論文に CC 表示はない。判定の補助文書（riskofbias.info）は別資料で、本カードの出典には含めていない。'
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-008
  domain: EB
  subdomain: 診療ガイドラインの作成
  assertion:
    plain_statement_ja: GRADEでは、エビデンスの確実性をアウトカムごとに、高、中、低、非常に低の4段階で評価する。ランダム化試験のエビデンスは高い確実性から、観察研究のエビデンスは低い確実性から出発する。確実性を下げる方向に働くのは、研究の限界（バイアスのリスク）、結果の非一貫性、エビデンスの非直接性、不精確さ、出版バイアスの5つである。観察研究では逆に、効果が非常に大きいこと、用量反応関係があること、考えられる交絡が観察された効果を弱める方向に働いていること、があると確実性を上げることがある。
    condition:
      region: 国際
      対象: 診療ガイドライン作成者・研究者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5509
    source: 'Guyatt GH, Oxman AD, Vist GE, et al. GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. BMJ. 2008;336(7650):924-926'
    doi: 10.1136/bmj.39489.470347.AD
    pmid: '18436948'
    pmcid: PMC2335261
    url: https://doi.org/10.1136/bmj.39489.470347.AD
    source_license: © BMJ Publishing Group Ltd 2008（PMC2335261 に CC の license 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: 現在の用語と運用（確実性の評価手順）は GRADE Handbook（SRC-5510、オンライン版）でも裏づけられる。主出典は版の固定された論文とし、Handbook は裏づけにとどめた（依頼文 §2-5 への対応）
  uncertainty: 2008年の論文では確実性のことを quality of evidence（エビデンスの質）と呼び、下げる要因の名前も、研究の限界は study limitations、出版バイアスは reporting bias とされていた。現在の certainty of evidence という呼び方と、risk of bias、publication bias という要因名は、その後の GRADE guidelines シリーズと Handbook での言い換えである（依頼文 §3-4 への対応）。上げる要因は観察研究のエビデンスに適用されるものである。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-009
  domain: EB
  subdomain: 診療ガイドラインの作成
  assertion:
    plain_statement_ja: GRADEでは、推奨の向き（行うか、行わないか）と強さは、望ましい効果と望ましくない効果の見積もり、その見積もりへの確信の程度（エビデンスの確実性）、患者の価値観と選好、資源の利用の4つの領域を合わせて判断して決める。推奨の強さは、望ましい効果の合計が望ましくない効果の合計を上回ることに、どれくらい確信が持てるかを表す。確実性は判断材料の1つにすぎないため、エビデンスの確実性が低くても強い推奨になる場合や、確実性が高くても条件付きの推奨にとどまる場合がある。最終的には、パネルがこれらの要素を統合して判断する。
    condition:
      region: 国際
      対象: 診療ガイドライン作成者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5511
    source: 'Andrews JC, Schünemann HJ, Oxman AD, et al. GRADE guidelines: 15. Going from evidence to recommendation—determinants of a recommendation''s direction and strength. Journal of Clinical Epidemiology. 2013;66(7):726-735'
    doi: 10.1016/j.jclinepi.2013.02.003
    pmid: '23570745'
    pmcid: null
    url: https://doi.org/10.1016/j.jclinepi.2013.02.003
    source_license: © 2013 Elsevier Inc.（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: GRADE Handbook（SRC-5510、オンライン版）でも、推奨の強さの判断要素として同じ領域が示されている
  uncertainty: 2013年の論文では推奨の強さを strong と weak と呼んでいた。現在の GRADE では weak にあたるものを「条件付き（conditional）」と呼ぶことが多い。本カードでは強い／条件付きの言い方にそろえた。確実性が低いのに強い推奨とする具体的な条件（生命を脅かす状況など）の列挙は、別の GRADE 論文の範囲のため本カードには含めていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-010
  domain: EB
  subdomain: 診療ガイドラインの作成
  assertion:
    plain_statement_ja: 'EtD（Evidence to Decision）は、エビデンスから推奨へ進むときの判断を、項目ごとに分けて表に残すための枠組みである。集団の視点から臨床推奨を決める場合の判断項目は12あり、問題の優先度、望ましい効果、望ましくない効果、エビデンスの確実性、価値観（主要なアウトカムを人々がどれくらい重視するかの不確かさやばらつき）、効果のバランス、必要となる資源、資源に関するエビデンスの確実性、費用対効果、公平性への影響、受け入れ可能性、実行可能性、である。各項目について判断とその根拠を記録することで、なぜその推奨になったかを後からたどれるようにする。'
    condition:
      region: 国際
      対象: 診療ガイドライン作成者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5512
    source: 'Alonso-Coello P, Schünemann HJ, Moberg J, et al. GRADE Evidence to Decision (EtD) frameworks: a systematic and transparent approach to making well informed healthcare choices. 2: Clinical practice guidelines. BMJ. 2016;353:i2089'
    doi: 10.1136/bmj.i2089
    pmid: '27365494'
    pmcid: null
    url: https://doi.org/10.1136/bmj.i2089
    source_license: CC表示なし（Crossref は BMJ の TDM ライセンスのみ。PMC 未収載）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 判断項目は論文の表にある12項目を過不足なく挙げたが、表そのものや項目の説明文は転記していない（依頼文 §3-5 への対応）。個人の患者の視点で使う場合は項目の扱いが変わり、資源は自己負担、公平性などは中心にならないことが多いと論文は述べている。本カードは集団の視点の臨床推奨を対象とした。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-011
  domain: EB
  subdomain: 患者市民参画
  assertion:
    plain_statement_ja: 患者市民参画（PPI）を研究報告に書くためのチェックリストとしてGRIPP2がある。長い版と短い版があり、参画の目的、参画の方法、参画が研究に与えた影響や変化、うまくいかなかった点を含む振り返り、といった区分に沿って報告する。参画したかどうかだけでなく、参画によって研究の進め方や判断がどう変わったかまで書くことが、報告の対象に含まれている。
    condition:
      region: 国際
      対象: 研究者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5513
    source: 'Staniszewska S, Brett J, Simera I, et al. GRIPP2 reporting checklists: tools to improve reporting of patient and public involvement in research. BMJ. 2017;358:j3453'
    doi: 10.1136/bmj.j3453
    pmid: '28768629'
    pmcid: PMC5539518
    url: https://doi.org/10.1136/bmj.j3453
    source_license: CC BY-NC 4.0（PMC5539518 の license 表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: '分割案にあった「参画の評価は参加の有無ではなく、どの決定がどう変わったかで見る」という言い方は解釈を含むため使わず、GRIPP2の報告区分に書かれている範囲（参画の影響や変化を報告対象とする）に限った（依頼文 §3-6 への対応）。チェックリストの項目文そのものは転記していない。ライセンスは分割案の「CC BY の見立て」から CC BY-NC 4.0 に訂正した。'
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
- id: EB-012
  domain: EB
  subdomain: 患者市民参画
  assertion:
    plain_statement_ja: 患者市民参画（PPI）は、研究が患者・市民に対して、あるいは患者・市民について行われるのではなく、患者・市民と共に、または患者・市民によって行われることを指す。患者・市民が研究の対象者として参加すること（参加、participation）や、研究の知見を社会に伝えること（engagement）とは区別される。参画する「市民」には、患者、患者になりうる人、介護者、医療・介護サービスの利用者が含まれる。日本でも、AMEDがガイドブックを出し、研究者が患者・市民の経験や知見を聞いて研究計画に反映し、共に研究を設計していくことを参画として示している。
    condition:
      region: 国際
      対象: 研究者・医療者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5514
    source: 'National Institute for Health and Care Research (NIHR). Briefing notes for researchers: public involvement in NHS, health and social care research. NIHR; 2021（文書番号 27371）'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.nihr.ac.uk/documents/briefing-notes-for-researchers-public-involvement-in-nhs-health-and-social-care-research/27371
    source_license: 文書・ページにライセンス表示なし（確認できていないため UNKNOWN とし、RESTRICTED と同じ扱い）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: 日本の文脈では AMED『患者・市民参画（PPI）ガイドブック』（2019年4月、SRC-5515）が、研究対象者としての参加と情報発信を参画から区別し、患者・市民の知見を研究計画に反映する参画の形を示している
  uncertainty: '元の定義を出した INVOLVE は、2020年に NIHR の Centre for Engagement and Dissemination へ引き継がれたため、主出典は現行の NIHR 文書（2021年）とした（依頼文 §3-7 への対応）。NIHR 文書のライセンスは、文書とページのどちらにも表示がなく確認できなかったため UNKNOWN とした。Open Government Licence の適用があるかどうかは未確認である。定義は英国の制度文脈のもので、日本の制度そのものを述べたものではない。'
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-26'
    verifier: null
    verified_at: null
    status: draft
```

## 3. 未解決事項

1. **SRC-5514（NIHR 文書）のライセンス**：文書・ページに表示がなく、Open Government Licence の適用も確認できなかったため UNKNOWN とした。登録時に NIHR 側の利用条件ページでの再確認をお願いしたい。
2. **SRC-5500（Cochrane Handbook）の版**：オンライン版 version 6.5（2024年）を参照日つきで記録した。章の更新で内容が変わりうるため、将来の照合直しでは版の確認が必要。
3. **SRC-5510（GRADE Handbook）の版**：オンライン版で更新年月を特定する形にとどめた。裏づけ専用とし、主張の主根拠は版の固定された論文（SRC-5509・5511）に置いた。
4. **EB-008 の分割見送り**：下げる要因・上げる要因まで1枚に収めた。依頼文 §3-4 は過密な場合の分割（EB-013）を認めていたが、記述を骨格に限ることで1枚に収まると判断した。取り込み側で過密と判断されれば分割する。
5. **EB-009 の「強い推奨＋低い確実性」の条件**：具体的な条件の列挙は別の GRADE 論文の範囲のため含めていない。第2陣以降で独立カードにする候補。
6. **数値の確認経路**：EB-006 の数値は全文（PMC）で確認した。EB-005 の PRESS の点検面は抄録とガイドライン声明の要約で確認しており、本文の各論は含めていない。

## 4. 引き継ぎメモ

- 動画との対応：EB-001〜012 は動画テーマ EB_001〜003、EB_009〜012、EB_017〜019、EB_024、EB_025 に1対1で対応する（対応は出典表の「使うカード」ではなく本ファイル §2 の各カードと EBM_VIDEO_QUEUE.md の第1陣一覧が正）。
- 監修は動画化時点で行う既定方針（依頼文 §1-5）。カードは draft のまま渡す。
- 第2陣（残り16テーマ）の出典候補は EBM_VIDEO_QUEUE.md に残してある。EB_016（AIスクリーニング）は報告規範の公開状況が確定してから着手する。
- 本ファイルで使わなかった SRC 番号：SRC-5516〜5599 は未使用。

## 5. 納品前検証の記録

### 5-1. 機械検証（最終ファイルに対して実施）

- カード件数と番号：EB-001〜012 の12件、欠番なし。受け入れ仕様（12〜13件、SRC-5500〜5599）の範囲内。
- YAML 検証：単一の yaml ブロックとしてパースし、全カードで id・domain・assertion・provenance・publication_info の必須構造と、condition.region が全件設定されていることを確認した（結果は納品報告に記載）。
- 重複照合：新規出典16件の DOI・PMID を最新版出典マスター（sources.yaml）と照合し、重複なし。同一ファイル内の DOI 重複もなし（SRC-5500 は EB-001・EB-002 で共用するが、出典表では1行のみ）。
- 「 #」を含むプレーン値がないこと、YAML のアンカー・アライアスがないことを最終ファイルで検索して確認した。

### 5-2. 内容検証（作成と分けて実施）

- **ライセンスの訂正（分割案 §2 の見立て → 本ファイル）**：Crossref の license と PMC・出版社のページで1件ずつ確かめた結果、次の4件で見立てが誤っていたため訂正した。
  - RoB 2（SRC-5508）：OPEN（CC BY）の見立て → CC表示なし・RESTRICTED
  - EtD（SRC-5512）：OPEN（CC BY）の見立て → CC表示なし・RESTRICTED
  - GRADE 2008（SRC-5509）：OPEN（CC BY 系）の見立て → © BMJ Publishing Group Ltd 2008・RESTRICTED
  - GRIPP2（SRC-5513）：OPEN（CC BY）の見立て → CC BY-NC 4.0・RESTRICTED
  - 見立てどおりだったもの：PRISMA 2020＝CC BY 4.0・OPEN、PRISMA-S＝CC BY 4.0・OPEN、ASA声明＝RESTRICTED。CONSORT 2010 解説（SRC-5502）は CC BY-NC 2.0 で RESTRICTED とした。PRESS（SRC-5506）は © The Authors・Elsevier で CC表示なし。
- **書誌の原典確認**：全論文の書誌・PMID・DOI・PMCID は PubMed（E-utilities）と PMC で照合した。PMID を null とした ASA 声明は PubMed 未収載であることを検索で確認した上で DOI のみとした。
- **主張の根拠確認**：EB-006 の数値は Waffenschmidt らの全文（PMC6599339 の表と本文）で確認し、抄録だけでは分からない内訳（評価研究4件・23回分・41,730件、経験別中央値）まで本文値にそろえた。EB-010 の12項目は Alonso-Coello らの表と本文の「12 criteria」の記述で照合した。EB-002 の「平均として等しくなる」留保と EB-007 の「合計点の仕組みがない」書き方は、Handbook Ch.8 と RoB 2 本文の構造に基づいており、出典にない断定（「唯一の方法」「禁止されている」）は入れていない。
- **用語の版差**：GRADE の quality → certainty の言い換えと要因名の変更（study limitations → risk of bias、reporting bias → publication bias）、推奨の weak → conditional の言い換えは、2008年・2013年の各論文の原文用語と照合し、uncertainty に明記した。
