# 医療者教育（ME）第3回（第2弾・第2陣）：ME-020〜025（カード6件）

依頼文（round_ME3_request.md、2026-11-23登録）に基づく第2陣の6枚。決定事項の適用は次のとおり。

- 接頭辞は ME。カード番号は ME-020〜025（ME-008 は保留中のカードのために空けてあり、本回も使わない）。区分は subdomain に書いた（制度：ME-020・021、評価：ME-022、教育手法：ME-023、横断：ME-024・025）。出典番号は SRC-5124〜5160 の範囲を使い、本回は新規に SRC-5124〜5133 を割り当てた（SRC-5134〜5160 は未使用）。
- 対象範囲は医療系の全職種（2026-11-23 三原の決定）。各カードの主張文と `condition.対象` に職種を明記した。
- カリキュラム欄：日本の制度の2枚（ME-020・021）は国試の欄を空欄とし、番号はレポジトリ側で付ける扱いとした。教育者向けの理論・教育手法の2枚（ME-022・023）は空欄とし、`condition.対象` を「教育者」とした。学生が学ぶ内容の2枚（ME-024・025）には、2022年版コアカリ第1層の不変 id を付けた（ME-024 は CS (id: JnGV10w)、ME-025 は IP (id: JnGV11A)。レポジトリ登録の第1層 CSV で照合）。
- 依頼文の注意の適用：定義文・結論文の和訳は使わず、概念の説明は自作の文で組み立てた（注意1）。ME-025 では CAIPE 由来の IPE 定義文を主張に入れず、出どころは uncertainty に書いた。ME-024 では11トピックの名称を概念名として並べ、説明文は訳していない。ME-022・023 では抄録の結果を順番どおりに訳さず、必要な事実を選んで自分の構成で書いた。数値は一次資料で確定させた（注意2）。ME-021 のアルゴリズムは概念名として書き、申し込む側の特定は公式資料で確かめた範囲に限った（注意3）。識別子は API・公式登録情報で確認したものだけを書いた（注意4）。
- 新規出典10件（SRC-5124〜5133）は、出典マスター全体と第1弾・第2弾第1陣までの納品分（SRC-5101〜5123 を含む）と DOI・PMID で照合し、重複がないことを確認した。既存出典の再利用はない。

## 1. 出典表

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-5124 | 厚生労働省. 専門医の在り方に関する検討会 報告書. 2013年4月22日 | なし | なし | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 厚生労働省の公表ページで報告書の公表（平成25年4月22日）を確認し、報告書の設計（中立的な第三者機関による専門医の認定と養成プログラムの評価・認定の統一、基本領域とサブスペシャルティの二段階制、更新制）は公表資料の概要で照合 |
| SRC-5125 | 厚生労働省 医道審議会医師分科会医師専門研修部会. 今後の専門研修制度に向けた検討について（令和6年度第3回医師専門研修部会 資料1）. 2024年12月13日 | なし | なし | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 厚生労働省の公表 PDF で、新たな専門医の仕組みの経緯（平成30（2018）年4月1日に日本専門医機構の専門研修プログラムで研修開始、19基本領域の養成を一斉に開始）を確認 |
| SRC-5126 | 日本専門医機構. 整備指針（第三版 2020年2月版）における「専門医の認定・更新」に関する補足説明（2024年12月20日一部改訂・理事会承認） | なし | なし | © 日本専門医機構（CC表示なし） | RESTRICTED | 機構の公表 PDF で、認定期間（原則として4月1日開始・5年後の3月31日まで）、更新（5年を原則として申請、診療実績の証明・共通講習・領域講習・単位取得等）、認定審査の分担（領域学会が一次審査、機構が二次審査と認定）を確認（事実のみ使用） |
| SRC-5127 | 厚生労働省. 令和8年度の医師臨床研修マッチング結果をお知らせします（報道発表資料）. 2026年10月22日 | なし | なし | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 厚生労働省の報道発表ページで、マッチングの定義（双方の希望を踏まえ、一定の規則（アルゴリズム）に従ってコンピュータにより組合せを決定するシステム）と、平成16年度の臨床研修義務化に合わせて導入されたことを確認 |
| SRC-5128 | 厚生労働省. 組み合わせ決定（マッチング）について（案）. 2003年 | なし | なし | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 厚生労働省の公表ページ（臨床研修制度の検討資料）で、制度の設計（希望順位表に基づくコンピュータによる組み合わせ決定、実施主体の中立性、参加契約とマッチングによる決定への従属、選考手続を受けた病院のプログラムに限る希望順位表）を確認 |
| SRC-5129 | 医師臨床研修マッチング協議会. 研修医マッチングの手引き（2026年度版）【6年生用・既卒者用】 | なし | なし | 権利表記を確認できず（下記 §4-3） | UNKNOWN | 協議会の公表 PDF（jrmp.jp）で、組合せがゲール・シャープレーのアルゴリズムによって決まること、実施体制（協議会が実施主体）を確認。手引きの年度版は2026年度版 |
| SRC-5130 | Driessen E, van Tartwijk J, van der Vleuten C, Wass V. Portfolios in medical education: why do they meet with mixed success? A systematic review. Med Educ. 2007;41(12):1224-1233 | 10.1111/j.1365-2923.2007.02944.x | 18045373 | © Wiley（CC表示なし） | RESTRICTED | PubMed（E-utilities API）で書誌・抄録を確認（1,939件から30件、卒前教育で効果が最も強い、成功要因、形成的・総括的の併用）し、DOI・巻号頁は Crossref で照合 |
| SRC-5131 | Fatmi M, Hartling L, Hillier T, Campbell S, Oswald AE. The effectiveness of team-based learning on learning outcomes in health professions education: BEME Guide No. 30. Med Teach. 2013;35(12):e1608-e1624 | 10.3109/0142159X.2013.849802 | 24245519 | © Taylor & Francis（CC表示なし） | RESTRICTED | PubMed（E-utilities API）で書誌・DOI・抄録を確認（330件から14件、知識スコア7件で有意な上昇・4件で差なし・3件は有意性への言及なし、学習者の反応は一様でない） |
| SRC-5132 | World Health Organization. Patient Safety Curriculum Guide: Multi-professional Edition. Geneva: World Health Organization; 2011. ISBN 978 92 4 150195 8 | なし | なし | © World Health Organization 2011（All rights reserved。WHO IRIS に CC ライセンスの表示なし） | RESTRICTED | WHO 公式ページと本文 PDF（WHO IRIS、ハンドル 10665/44641）で、2011年公表、多職種版であること、Part A（教員用ガイド）と Part B（11トピック）の構成とトピック名、対象（医学・歯学・助産・看護・薬学）を確認。ISBN は IRIS の登録情報と本文の奥付で照合。ライセンスは本文の権利表示と IRIS の登録情報（CC ライセンスの記載なし）で確認 |
| SRC-5133 | World Health Organization. Framework for Action on Interprofessional Education and Collaborative Practice. Geneva: World Health Organization; 2010 (WHO/HRH/HPN/10.3) | なし | なし | © World Health Organization 2010（All rights reserved。WHO IRIS に CC ライセンスの表示なし） | RESTRICTED | 本文 PDF（WHO IRIS、ハンドル 10665/70185）で、IPE と協働実践の位置づけ、仕組みの整理（教育者・カリキュラム／制度・運営・環境等）、保健医療人材の範囲を確認。ISBN は IRIS の登録情報にも本文にも付されておらず、文書番号 WHO/HRH/HPN/10.3 を識別子とした。ライセンスは本文の権利表示と IRIS の登録情報で確認 |

## 2. 事実カード（YAML）

```yaml
- id: ME-020
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 専門医の資格は、かつては診療科ごとの学会がそれぞれ認定していたが、厚生労働省の「専門医の在り方に関する検討会」は2013年の報告書で、中立的な第三者機関が専門医の認定と養成プログラムの評価・認定を統一的に行う新しい仕組みを提言した。これを受けて2014年に一般社団法人日本専門医機構が設立され、2018年4月から、19の基本領域（内科、小児科、皮膚科、精神科、外科、整形外科、産婦人科、眼科、耳鼻咽喉科、泌尿器科、脳神経外科、放射線科、麻酔科、病理、臨床検査、救急科、形成外科、リハビリテーション科、総合診療）で専門研修が一斉に開始された。枠組みは、基本領域の専門医を取得したうえで、より細分化されたサブスペシャルティ領域の専門医を取得する二段階制を基本とする。専門研修は、機構が認定した研修プログラムに基づき、基幹施設と連携施設からなる施設群で行われる。認定の審査は各領域学会が一次審査を行い、機構が二次審査と認定を行う。機構認定専門医の認定期間は原則として5年で、更新の際には診療実績の証明、共通講習・領域講習の受講、所定の単位の取得などが求められる。
    condition:
      region: 日本
      対象: 医師（専門研修を受ける専攻医と専門医）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5124
    source: 厚生労働省. 専門医の在り方に関する検討会 報告書. 2013年4月22日
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/shingi/2r985200000300ju.html
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: 新制度の開始時期と基本領域数（2018年4月1日に19基本領域の専門研修を一斉に開始）は SRC-5125（厚生労働省 医道審議会医師分科会医師専門研修部会の資料、GOV_JP）で確認した。認定期間（原則5年）と更新の要件、認定審査の分担（領域学会が一次審査、機構が二次審査と認定）は SRC-5126（日本専門医機構の補足説明、RESTRICTED）による
  uncertainty: 出典内の位置：2013年報告書は新しい仕組みの設計（第三者機関による認定と養成プログラムの評価・認定の統一、二段階制、更新制）を示した文書であり、実際の開始は当初目安とされた2017年度から2018年度にずれ込んだ。数値（基本領域19、開始2018年4月、認定期間5年）は資料の時点とあわせて記載した。サブスペシャルティ領域の数と構成は見直しの対象となっており、本カードでは数に触れていない。日本専門医機構の資料は補助にとどめ、主出典は厚生労働省の資料とした（依頼文の方針）。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-23'
    verifier: null
    verified_at: null
    status: draft
- id: ME-021
  domain: ME
  subdomain: 制度
  assertion:
    plain_statement_ja: 医師臨床研修マッチングは、臨床研修を受けようとする者（研修希望者）と臨床研修病院の研修プログラムとを、双方の希望を踏まえて、一定のアルゴリズムに従ってコンピュータで組み合わせる仕組みであり、医師の臨床研修が必修化された2004年度に導入された。実施主体は、研修希望者と研修病院の双方に対して中立的な立場にある医師臨床研修マッチング協議会である。研修希望者は、研修を希望する病院の選考手続（応募・面接・試験等）を受けたうえで、希望するプログラムを希望順位表に登録し、病院も採用したい研修希望者を希望順位表に登録する。組合せは、ゲール・シャープレーのアルゴリズム（受入保留方式）によって決定され、希望順位表に記載されていない組合せは生じない。参加は参加規約への同意を条件とし、マッチした結果はそのまま採用の内定として扱われ、参加者と病院は結果に従って研修契約を結ぶ。
    condition:
      region: 日本
      対象: 医師（臨床研修を受けようとする研修希望者）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5127
    source: 厚生労働省. 令和8年度の医師臨床研修マッチング結果をお知らせします（報道発表資料）. 2026年10月22日
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/houdou/0000180824_00012.html
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: 制度の設計（希望順位表に基づくコンピュータによる組合せ決定、実施主体の中立性、参加契約と決定への従属）は SRC-5128（厚生労働省が2003年に公表した組み合わせ決定の仕組みの案、GOV_JP）による。アルゴリズムがゲール・シャープレーのアルゴリズムであることと、マッチ結果が内定として扱われることは SRC-5129（医師臨床研修マッチング協議会「研修医マッチングの手引き」2026年度版、ライセンス区分 UNKNOWN）で確認した
  uncertainty: 出典内の位置：仕組みの概要と2004年度の導入は厚生労働省の報道発表資料の説明文による。参加者数やマッチ率などの年度ごとの数値は、協議会と厚生労働省が毎年公表しているが、本カードの主張には含めていない。現行の組合せ決定には、都道府県ごとの募集定員の上限など、制度上の調整が加わっている。手引き（SRC-5129）の権利表記は、本文の取得が完了せず確認できなかったため、ライセンス区分は UNKNOWN とした。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-23'
    verifier: null
    verified_at: null
    status: draft
- id: ME-022
  domain: ME
  subdomain: 評価
  assertion:
    plain_statement_ja: ポートフォリオ（学習の記録や省察を蓄積するファイル）を医学教育で用いることの効果について、文献データベース等から得られた1,939件のうち実証研究30件を対象とした系統的レビューでは、効果の報告は一様ではなかった。肯定的な効果が最も強く示されたのは卒前教育の段階だった。成功と関連する要因として、目的と手順が明確に伝達されていること、カリキュラムや評価と統合されていること、構造に柔軟性があること、メンター（指導者）による支援があること、実施のしやすさを高め所要時間を減らす工夫があることが挙げられた。評価者間の信頼性は中程度と報告され、全体的な評価基準を用いることや評価者同士の討議が有益だった。形成的評価と総括的評価の併用は可能とされた一方、評価に用いられないポートフォリオは、他の総括的評価の手段との競合で埋没しやすいことも示された。著者らは、ポートフォリオが能力の発達を支え評価する手段として機能するには、カリキュラムへの確かな組み込みと指導者の支援が欠かせないと結論づけた。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5130
    source: 'Driessen E, van Tartwijk J, van der Vleuten C, Wass V. Portfolios in medical education: why do they meet with mixed success? A systematic review. Med Educ. 2007;41(12):1224-1233'
    doi: 10.1111/j.1365-2923.2007.02944.x
    pmid: '18045373'
    pmcid: null
    url: https://doi.org/10.1111/j.1365-2923.2007.02944.x
    source_license: © Wiley（Medical Education、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値（1,939件から30件）と効果の方向、成功要因は原著の抄録で確認した。研究間の違いが大きいため統計的なメタ解析は行われていない。抄録の結果を順番どおりに訳すことはせず、必要な事実を選んで自分の構成で記載した。対象は医学教育の全段階（卒前・卒後・生涯教育）を含む。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-23'
    verifier: null
    verified_at: null
    status: draft
- id: ME-023
  domain: ME
  subdomain: 教育手法
  assertion:
    plain_statement_ja: チーム基盤型学習（TBL）は、学習者が事前に学習したうえで、個人テスト（iRAT）、チームテスト（tRAT）、応用演習の順に進める能動学習法で、他の能動学習法に比べて教員の負担が少ないとされる。保健医療職教育におけるTBLの学習成果への効果を検討したBEME系統的レビュー（BEME Guide No. 30）では、330件の題目から14件の研究が選ばれた。知識のスコアについては、14件のうち7件でTBL群の有意な上昇が報告され、4件では差がなく、3件では上昇は見られたものの統計的な有意性への言及がなかった。学習者の反応は一様ではなく、TBL群で有意な改善を報告した研究は1件、比較対照の側が有意に好意的だった研究も1件あった。著者らは、知識のスコアが改善する一方で学習者の反応が分かれたのは、学習者中心の方法であるTBLが学習者に求める負荷の大きさを反映している可能性があると考察した。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5131
    source: 'Fatmi M, Hartling L, Hillier T, Campbell S, Oswald AE. The effectiveness of team-based learning on learning outcomes in health professions education: BEME Guide No. 30. Med Teach. 2013;35(12):e1608-e1624'
    doi: 10.3109/0142159X.2013.849802
    pmid: '24245519'
    pmcid: null
    url: https://doi.org/10.3109/0142159X.2013.849802
    source_license: © Taylor & Francis（Medical Teacher、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値（330件から14件、知識スコアの内訳）と効果の方向は原著の抄録で確認した。抄録の結果を順番どおりに訳すことはせず、必要な事実を選んで自分の構成で記載した。対象は保健医療職教育全般であり、医学教育のみの数値ではない。TBLの進め方（iRAT・tRAT・応用演習）は方法の概念名として記載した。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-23'
    verifier: null
    verified_at: null
    status: draft
- id: ME-024
  domain: ME
  subdomain: 横断
  assertion:
    plain_statement_ja: 世界保健機関（WHO）は2011年、医療専門職の学校教育で患者安全を教えるための「患者安全カリキュラムガイド（多職種版）」を公表した。対象は医学・歯学・助産・看護・薬学の学生であり、すべての医療専門職の継続的な研修にも使える構成とされている。ガイドは2部構成で、Part A は患者安全の教育を導入し広げるための教員向けガイド、Part B は授業にそのまま使える11のトピックからなる。Part B のトピックは、患者安全とは何か、ヒューマンファクターズの適用が重要である理由、システムと複雑性が患者ケアに及ぼす影響、効果的なチームの一員として働くこと、エラーから学んで害を防ぐこと、臨床リスクの理解と管理、質改善の方法を用いたケアの改善、患者と介護者との関わり、感染予防と管理、侵襲的処置における患者安全、薬剤の安全性の改善、である。
    condition:
      region: 国際
      対象: 医療系の学生（医学・歯学・助産・看護・薬学）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5132
    source: 'World Health Organization. Patient Safety Curriculum Guide: Multi-professional Edition. Geneva: World Health Organization; 2011. ISBN 978 92 4 150195 8'
    doi: null
    pmid: null
    pmcid: null
    url: https://iris.who.int/handle/10665/44641
    source_license: © World Health Organization 2011（All rights reserved。WHO IRIS に CC ライセンスの表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典内の位置：構成（Part A・Part B）と11トピックは本文の目次で確認した。トピック名は概念名の並びとして挙げ、各トピックの説明文は訳していない（依頼文の注意1）。ライセンスは WHO IRIS の登録情報と本文の権利表示で確認し、CC ライセンスの表示がないため RESTRICTED とした。日本語版は東京医科大学から刊行されているが、本カードは英語版に基づく。コアカリ第1層には患者安全の独立した項目がないため、説明文に患者安全を含む CS（患者ケアのための診療技能）を付けた。
  curriculum:
    kokushi: null
    core_curriculum: 'CS (id: JnGV10w)'
  publication_info:
    created: '2026-11-23'
    verifier: null
    verified_at: null
    status: draft
- id: ME-025
  domain: ME
  subdomain: 横断
  assertion:
    plain_statement_ja: 多職種連携教育（IPE）は、異なる職種の学習者が、互いの職種の役割や専門性を理解し合い、将来チームで協働して働くための準備をする教育の進め方を指す。世界保健機関（WHO）は2010年、「多職種連携教育と協働実践のための行動枠組み」を公表し、IPE を、協働実践に対応できる保健医療人材を育てるための方策として位置づけた。この枠組みでは、IPE の進め方を左右する仕組みとして教育者とカリキュラムに関する仕組みを整理し、現場での協働実践を左右する仕組みとして、制度の運営、業務の進め方、職場の文化や環境などに関する仕組みを整理して、各国や各機関が自国の状況に合わせて検討する際の材料を示している。枠組みが対象とする保健医療人材は、医師や看護師などの専門職に限らず、健康に関わる幅広い働き手を含む。
    condition:
      region: 国際
      対象: 医療系の学生と医療専門職（全職種）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5133
    source: 'World Health Organization. Framework for Action on Interprofessional Education and Collaborative Practice. Geneva: World Health Organization; 2010 (WHO/HRH/HPN/10.3)'
    doi: null
    pmid: null
    pmcid: null
    url: https://iris.who.int/handle/10665/70185
    source_license: © World Health Organization 2010（All rights reserved。WHO IRIS に CC ライセンスの表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: IPE の定義について：WHO の枠組みは、英国の多職種連携教育推進センター（CAIPE）の定義（2つ以上の職種の学習者が互いについて・互いから・互いと共に学ぶ、という趣旨の定義文）を採用している。主張文ではこの定義文を訳して用いず、IPE が何を指すかを自分の言葉で説明した（依頼文の注意1）。枠組み文書には ISBN は付されておらず、文書番号は WHO/HRH/HPN/10.3 である（WHO IRIS の登録情報で確認）。ライセンスは本文の権利表示（All rights reserved）と IRIS の登録情報で確認し、CC ライセンスの表示がないため RESTRICTED とした。
  curriculum:
    kokushi: null
    core_curriculum: 'IP (id: JnGV11A)'
  publication_info:
    created: '2026-11-23'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応表

| カード | kokushi | コアカリ |
|---|---|---|
| ME-020 | （空欄：日本の制度。番号はレポジトリ側で付番） | （空欄） |
| ME-021 | （空欄：日本の制度。番号はレポジトリ側で付番） | （空欄） |
| ME-022 | （空欄：教育者向け理論のため付けない） | （空欄） |
| ME-023 | （空欄：教育者向け教育手法のため付けない） | （空欄） |
| ME-024 | （空欄） | CS (id: JnGV10w) |
| ME-025 | （空欄） | IP (id: JnGV11A) |

## 4. 未解決事項

1. ME-020・021 の国試（必修・医学総論）項目番号は、第1弾・第2弾と同じ扱いで空欄とした。レポジトリ側で出題基準の PDF から付番されたい。
2. ME-024 のコアカリ対応：第1層（2022年版）に患者安全の独立した項目はないため、説明文に「医療の質と患者安全を踏まえた診療」を含む CS（患者ケアのための診療技能、id: JnGV10w）を付けた。取り込み側で扱いを確認されたい。
3. SRC-5129（研修医マッチングの手引き、2026年度版）の権利表記は、手引き PDF の取得が時間内に完了せず、奥付の権利表示を確認できなかったため、ライセンス区分を UNKNOWN とした。本文の検索結果で確認できた範囲（ゲール・シャープレーのアルゴリズム、実施体制）の事実のみに使用した。権利表記が確認できれば RESTRICTED への変更を検討されたい。
4. ME-021：マッチングの参加者数・マッチ率などの年度数値は、協議会と厚生労働省が毎年公表しているが、今回は報道発表資料の添付 PDF の数値まで照合していないため、主張には含めていない。数値を入れる場合は年度を明記して別途確定されたい。
5. ME-020：サブスペシャルティ領域の数と構成は制度見直しの対象となっており、本カードでは数に触れていない。扱う場合は時点を明記して機構の現行資料で確定されたい。
6. WHO 文書2件（SRC-5132・5133）は、WHO IRIS の登録情報に CC ライセンスの表示がなく、本文の権利表示も All rights reserved のため、依頼文の方針どおり RESTRICTED とした。将来 IRIS 側で CC BY-NC-SA 3.0 IGO の表示が付された場合は、区分の見直しを検討されたい。
7. GOV_JP 出典の政府標準利用規約の適用は、第1弾と同様、取り込み側で最終確認を要する。

## 5. 引き継ぎメモ

- 新規出典は10件（SRC-5124〜5133）。出典マスター全体と第1弾・第2弾第1陣までの納品分（SRC-5101〜5123）と DOI・PMID で照合し、いずれも未登録であることを確認した。SRC-5134〜5160 は未使用で、第3弾以降の ME ラウンドで使える。
- 既存出典の再利用は0件。統合した重複出典はない。
- 第2弾は本回（第2陣6枚）で完了し、分割案の確定候補26件のうち作成済みは25枚（ME-001〜007、ME-009〜025）となった。残るは保留中の ME-008（フィードバック）のみで、扱いが決まれば作成・動画化の対象に戻せる。
- 拡張候補6件（JACME、医師国家試験そのもの、臨床研修の評価システム、専門医更新・生涯教育、他職種の養成制度、教育基盤）は本回に含めていない。対象範囲が医療系の全職種に決定した（2026-11-23）ため、他職種の養成制度は第3弾以降の分割案で扱える。
- 動画化の在庫は、本回の6枚を加えて第1弾9〜10日分・第2弾第1陣9日分・第2陣6日分の合計24〜25日分となる（ME-008 を除く）。
