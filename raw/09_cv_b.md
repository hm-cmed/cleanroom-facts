# 第9回 循環器（弁膜症 VD・心筋/心膜疾患 MP・先天性心疾患 CH）

- 作成日：2026-10-25
- 事実票：89件（VD-001〜VD-032、MP-001〜MP-032、CH-001〜CH-025。欠番なし）。全件 `status: draft`、`verifier: null`、`legal_basis: B`
- 取り込み：`python scripts/ingest_round.py raw/09_cv_b.md VD,MP,CH`。YAML ブロックは1つで、アンカー・マージキー・脚注番号は使っていません。`schema/fact.schema.json` での検証と、リポジトリの写しでの取り込み試験を通過済みです。
- SRC 番号：SRC-230〜272（第9回の範囲 SRC-230〜289 のうち43件を使用）。
- 出典の方針：日本の学会ガイドラインは日本語版の本文で確認しました（J-STAGE の英語版 PDF はこの環境から取得できず）。そのため DOI のない日本語版を出典とし、取得できた範囲（各 PDF の前半）に書かれていることだけを使いました。厚生労働省の指定難病の資料（GOV_JP）、CDC・NHLBI・MedlinePlus（GOV_US）、CC BY の論文（OPEN）を優先しました。
- 本文の読み取り：各ページ・PDF は取得ツール（WebFetch）が本文から抜き出した内容で確認しました。長い PDF は前半しか読めず、表が抽出されないこともあったため、読めた範囲の記載だけを使い、読めなかった部分は各カードの `uncertainty` に書きました。数値は Phase 3 で原典と照合してください。
- PubMed・PMC はこの環境から取得できなかったため、PMID は研究者データベースなどで確認できた2件だけを書き、ほかは null です（Phase 3 の API 照合で埋めてください）。

## 1. 抽出元ホワイトリスト（新規 SRC-230〜272）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 使用カード数 | 確認経路 |
|---|---|---|---|---|---|---|---|
| SRC-230 | 日本循環器学会/日本胸部外科学会/日本血管外科学会/日本心臓血管外科学会合同ガイドライン. 2020年改訂版 弁膜症治療のガイドライン（班長：江石清行ほか）. 2020年3月13日発行（日本語版） | — | — | 「無断転載を禁ずる」の表示。CC の表示なし（英語版 Circ J 2020;84:2037-2119 は J-STAGE で CC BY-NC-ND 4.0） | RESTRICTED | 6 | 日本心臓血管外科学会が UMIN で公開している PDF を WebFetch で読んだ（前半の第2章 MR まで。AS・MS・AR の章は取得範囲外） |
| SRC-231 | Otto CM, Nishimura RA, Bonow RO, et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. Circulation 2021;143:e72-e227 | 10.1161/CIR.0000000000000923 | — | © 2020 American College of Cardiology Foundation and American Heart Association（刊行版の表示） | RESTRICTED | 8 | STS（米国胸部外科学会）が掲載する刊行版 PDF を WebFetch で読んだ（第3章 AS の途中まで） |
| SRC-232 | Victor K, Ring L, Tsampasian V, et al. Echocardiographic assessment of aortic regurgitation: a practical guideline from the British Society of Echocardiography. Echo Res Pract 2025;12:3 | 10.1186/s44156-024-00067-8 | — | CC BY 4.0（刊行版 PDF の表示） | OPEN | 3 | リバプール・ジョン・ムーアズ大学のリポジトリの刊行版 PDF |
| SRC-233 | Robinson S, Ring L, Augustine DX, et al. The assessment of mitral valve disease: a guideline from the British Society of Echocardiography. Echo Res Pract 2021;8:G87-G136 | 10.1530/ERP-20-0034 | — | 刊行版 PDF とリポジトリは CC BY-NC-ND 4.0。Springer の現在の論文ページは CC BY 4.0 と表示（食い違い） | RESTRICTED | 1 | Springer の論文ページと刊行版 PDF（MR の章まで） |
| SRC-234 | Zaidi A, Oxborough D, Augustine DX, et al. Echocardiographic assessment of the tricuspid and pulmonary valves: a practical guideline from the British Society of Echocardiography. Echo Res Pract 2020;7:G95-G122 | 10.1530/ERP-20-0033 | — | CC BY-NC-ND 4.0（リポジトリの表示。著者最終稿） | RESTRICTED | 3 | リバプール・ジョン・ムーアズ大学のリポジトリの著者最終稿（TR の表1の途中まで） |
| SRC-235 | Centers for Disease Control and Prevention. Diagnosing Acute Rheumatic Fever（Group A Strep, Clinical Guidance）. 2025年8月6日確認版 | — | — | 米国連邦政府の著作物 | GOV_US | 2 | CDC のページ |
| SRC-236 | National Heart, Lung, and Blood Institute. Heart Valve Diseases: Treatment. 2022年3月24日更新 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | NHLBI のページ |
| SRC-237 | 日本循環器学会ほか合同ガイドライン. 感染性心内膜炎の予防と治療に関するガイドライン（2017年改訂版）（班長：中谷敏）. 2018年3月23日発行、2019年7月1日更新（日本語版） | — | — | 「無断転載を禁ずる」の表示。CC の表示なし | RESTRICTED | 6 | 日本心臓血管外科学会が UMIN で公開している PDF（第Ⅳ章のレンサ球菌の治療の途中まで） |
| SRC-238 | Mack MJ, et al. Transcatheter Aortic-Valve Replacement with a Balloon-Expandable Valve in Low-Risk Patients. N Engl J Med 2019;380:1695-1705 | 10.1056/NEJMoa1814052 | 30883058 | 未確認（出版社の著作物と考えられる） | UNKNOWN | 1 | Duke University の研究者データベースの書誌と抄録（PMID は同ページの PubMed へのリンク） |
| SRC-239 | Connolly SJ, Karthikeyan G, et al. Rivaroxaban in Rheumatic Heart Disease-Associated Atrial Fibrillation. N Engl J Med 2022;387:978-988 | 10.1056/NEJMoa2209051 | 36036525 | 未確認（出版社の著作物と考えられる） | UNKNOWN | 1 | Aga Khan University の研究者データベースの書誌と抄録 |
| SRC-240 | Committee for Scientific Affairs, The Japanese Association for Thoracic Surgery; Yoshimura N, Sato Y, et al. Thoracic and cardiovascular surgeries in Japan during 2021: Annual report by the Japanese Association for Thoracic Surgery. Gen Thorac Cardiovasc Surg 2024;72:254-291 | 10.1007/s11748-023-01997-6 | — | CC BY 4.0（Springer の論文ページの表示） | OPEN | 2 | Springer の論文ページ（本文） |
| SRC-241 | 日本循環器学会/日本心不全学会合同ガイドライン. 心筋症診療ガイドライン（2018年改訂版）（班長：北岡裕章、筒井裕之）. 2019年3月29日発行、2019年6月28日更新（日本語版） | — | — | 「無断転載を禁ずる」の表示。CC の表示なし | RESTRICTED | 5 | 日本心臓血管外科学会が UMIN で公開している PDF（第3章 HCM の核医学の途中まで） |
| SRC-242 | 厚生労働省. 指定難病 58 肥大型心筋症 概要、診断基準等（令和8年4月時点の掲載） | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 1 | 厚生労働省の PDF |
| SRC-243 | 医薬品医療機器総合機構. カムザイオスカプセル（マバカムテン）審査報告書. 令和7年3月7日 | — | — | 未確認（PMDA の利用規約を確認していない） | UNKNOWN | 1 | PMDA の PDF（第7章の臨床試験は取得範囲外） |
| SRC-244 | 厚生労働省. 指定難病 57 特発性拡張型心筋症 概要、診断基準等（令和8年4月時点の掲載） | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 3 | 厚生労働省の PDF |
| SRC-245 | 厚生労働省. 指定難病 59 拘束型心筋症 概要、診断基準等（令和8年4月時点の掲載） | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 1 | 厚生労働省の PDF |
| SRC-246 | 日本循環器学会ほか合同ガイドライン. 2020年版 心アミロイドーシス診療ガイドライン（班長：北岡裕章）. 2020年3月13日発行（日本語版） | — | — | 「無断転載を禁ずる」の表示。CC の表示なし | RESTRICTED | 5 | 日本循環器学会の PDF（第2章の診断の途中まで。治療の章の推奨表は取得範囲外） |
| SRC-247 | 厚生労働省. 指定難病 28 全身性アミロイドーシス 概要、診断基準等（令和8年4月時点の掲載） | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 2 | 厚生労働省の PDF |
| SRC-248 | 厚生労働省. 指定難病 84 サルコイドーシス 概要、診断基準等（令和8年4月時点の掲載） | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 1 | 厚生労働省の PDF |
| SRC-249 | 厚生労働省. 指定難病 113 筋ジストロフィー 概要、診断基準等（令和8年4月時点の掲載） | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 1 | 厚生労働省の PDF |
| SRC-250 | National Heart, Lung, and Blood Institute. Heart Inflammation: Causes and Risk Factors. 2023年10月更新 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | NHLBI のページ |
| SRC-251 | Aoyama N, Izumi T, Hiramori K, et al. National Survey of Fulminant Myocarditis in Japan: Therapeutic Guidelines and Long-Term Prognosis of Using Percutaneous Cardiopulmonary Support for Fulminant Myocarditis. Circ J 2002;66:133-144 | 10.1253/circj.66.133 | — | © 2002 The Japanese Circulation Society（Free Access。CC の表示なし） | RESTRICTED | 1 | J-STAGE の論文ページ（抄録） |
| SRC-252 | Van Camp G, Pasquet A, Sinnaeve P, et al. Summary 2015 ESC guidelines（心膜疾患ほか）. Acta Cardiol 2016;71:7-13 | 10.2143/AC.71.1.3132092 | — | 未確認 | UNKNOWN | 4 | ルーヴァン・カトリック大学のリポジトリの PDF（ESC 2015 心膜疾患 GL の要約部分） |
| SRC-253 | Templin C, Ghadri JR, Diekmann J, et al. Clinical Features and Outcomes of Takotsubo (Stress) Cardiomyopathy. N Engl J Med 2015;373:929-938 | 10.1056/NEJMoa1406761 | — | 未確認（リポジトリに表示なし。出版社の著作物と考えられる） | UNKNOWN | 2 | ゲッティンゲン大学のリポジトリの書誌と抄録 |
| SRC-254 | Peng T, Trollinger Derry L, Yogeswaran V, et al. Commotio Cordis in 2023. Sports Med 2023;53:1527-1536 | 10.1007/s40279-023-01873-6 | — | Open access（© The Author(s)）。CC の種類は未確認 | UNKNOWN | 2 | Springer の論文ページ（総説） |
| SRC-255 | Alhasso AA, Ahmed OF, Mohammed-Saeed DH, et al. Operative management and outcomes in patients with myxomas: A single-center experience. Front Surg 2023;10:1084447 | 10.3389/fsurg.2023.1084447 | — | CC BY（刊行版 PDF の表示） | OPEN | 1 | Frontiers の論文ページと PDF |
| SRC-256 | MedlinePlus Genetics. Carney complex. 2025年3月10日更新 | — | — | 米国連邦政府の著作物（NLM） | GOV_US | 1 | MedlinePlus のページ |
| SRC-257 | Centers for Disease Control and Prevention. Data and Statistics on Congenital Heart Defects. 2026年10月14日確認版 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | CDC のページ |
| SRC-258 | Centers for Disease Control and Prevention. Atrial Septal Defect (ASD). 2025年12月15日確認版 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | CDC のページ |
| SRC-259 | Centers for Disease Control and Prevention. Ventricular Septal Defect. 2025年12月15日確認版 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | CDC のページ |
| SRC-260 | Centers for Disease Control and Prevention. Atrioventricular Septal Defect (AVSD). 2026年1月9日確認版 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | CDC のページ |
| SRC-261 | Centers for Disease Control and Prevention. Tetralogy of Fallot. 2026年1月9日確認版 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | CDC のページ |
| SRC-262 | Centers for Disease Control and Prevention. Coarctation of the Aorta. 2026年1月9日確認版 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | CDC のページ |
| SRC-263 | Centers for Disease Control and Prevention. Total Anomalous Pulmonary Venous Return (TAPVR). 2026年1月9日確認版 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | CDC のページ |
| SRC-264 | Centers for Disease Control and Prevention. Screening for Critical Congenital Heart Defects. 2026年10月14日確認版 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | CDC のページ |
| SRC-265 | National Heart, Lung, and Blood Institute. Congenital Heart Defects: Types. 2022年3月24日更新 | — | — | 米国連邦政府の著作物 | GOV_US | 1 | NHLBI のページ |
| SRC-266 | 厚生労働省. 指定難病 214 心室中隔欠損を伴う肺動脈閉鎖症・215 ファロー四徴症（ファロー四徴症類縁疾患）概要、診断基準等 | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 3 | 厚生労働省の PDF |
| SRC-267 | 厚生労働省. 指定難病 209 完全大血管転位症 概要、診断基準等 | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 2 | 厚生労働省の PDF |
| SRC-268 | 厚生労働省. 指定難病 208 修正大血管転位症 概要、診断基準等 | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 1 | 厚生労働省の PDF |
| SRC-269 | 厚生労働省. 指定難病 210〜213 単心室症・左心低形成症候群・三尖弁閉鎖症・心室中隔欠損を伴わない肺動脈閉鎖症（単心室循環症候群）概要、診断基準等 | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 2 | 厚生労働省の PDF |
| SRC-270 | 厚生労働省. 指定難病 216 両大血管右室起始症 概要、診断基準等 | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 1 | 厚生労働省の PDF |
| SRC-271 | 厚生労働省. 指定難病 217 エプスタイン病 臨床調査個人票 | — | — | 政府標準利用規約（厚生労働省ホームページ） | GOV_JP | 1 | 厚生労働省の PDF（記入様式。概要・診断基準等の文書は未取得） |
| SRC-272 | 日本循環器学会ほか合同ガイドライン. 成人先天性心疾患診療ガイドライン（2017年改訂版）（班長：市田蕗子）. 2018年3月23日発行（日本語版） | — | — | 「無断転載を禁ずる」の表示。CC の表示なし | RESTRICTED | 4 | 日本心臓血管外科学会が UMIN で公開している PDF（第3章の経胸壁心エコーの途中まで） |

source_class 別のカード数：RESTRICTED 39件、GOV_JP 19件、GOV_US 14件、UNKNOWN 11件、OPEN 6件

## 2. 事実票 YAML

```yaml
- id: VD-001
  domain: VD
  subdomain: 僧帽弁閉鎖不全症
  assertion:
    plain_statement_ja: 僧帽弁閉鎖不全症（MR）は、弁尖・腱索・乳頭筋に器質的な異常がある一次性（器質性）MRと、弁そのものは保たれていて左室や左房の拡大・機能低下によって起こる二次性（機能性）MRに分けられる。一次性の原因には僧帽弁逸脱、リウマチ性変化、感染性心内膜炎、心筋梗塞後の乳頭筋断裂などがあり、二次性には左室の収縮不全による弁尖の牽引（テザリング）や、心房細動に伴う心房性機能性MRがある。
    condition:
      guideline: JCS/JATS/JSVS/JSCS 2020年改訂版 弁膜症治療のガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: 心房細動に伴う MR は弁尖の器質的な異常によって起こる
  provenance:
    source_ref: SRC-230
    source: 日本循環器学会/日本胸部外科学会/日本血管外科学会/日本心臓血管外科学会合同ガイドライン. 2020年改訂版 弁膜症治療のガイドライン（班長：江石清行ほか）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2020_Izumi_Eishi.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし（英語版 Circ J 2020;84:2037-2119 は J-STAGE で CC BY-NC-ND 4.0）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)'
    kokushi: 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-002
  domain: VD
  subdomain: 僧帽弁閉鎖不全症
  assertion:
    plain_statement_ja: 日本のガイドラインは、心エコーで重症 MR とする目安を、有効逆流弁口面積0.40 cm²以上、逆流量60 mL以上、逆流率50%以上、縮流部幅（vena contracta）0.7 cm以上としている。中等症はそれぞれ0.20〜0.39 cm²、30〜59 mL、30〜49%、0.3〜0.69 cm で、重症度は1つの指標でなく複数の指標を合わせて判定する。
    condition:
      guideline: JCS/JATS/JSVS/JSCS 2020年改訂版 弁膜症治療のガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: カラードプラの逆流ジェットの大きさだけで MR の重症度を決めてよい
  provenance:
    source_ref: SRC-230
    source: 日本循環器学会/日本胸部外科学会/日本血管外科学会/日本心臓血管外科学会合同ガイドライン. 2020年改訂版 弁膜症治療のガイドライン（班長：江石清行ほか）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2020_Izumi_Eishi.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし（英語版 Circ J 2020;84:2037-2119 は J-STAGE で CC BY-NC-ND 4.0）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-003
  domain: VD
  subdomain: 僧帽弁閉鎖不全症
  assertion:
    plain_statement_ja: 心不全症状のある重症の一次性 MR では、LVEF が30%を超えていれば弁形成術か弁置換術が推奨される（推奨クラスI）。耐久性のある形成が可能なら形成術が第一選択で、形成が難しい場合に置換術を選び、置換術でも腱索（とくに後尖側）を温存する。
    condition:
      guideline: JCS/JATS/JSVS/JSCS 2020年改訂版 弁膜症治療のガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-230
    source: 日本循環器学会/日本胸部外科学会/日本血管外科学会/日本心臓血管外科学会合同ガイドライン. 2020年改訂版 弁膜症治療のガイドライン（班長：江石清行ほか）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2020_Izumi_Eishi.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし（英語版 Circ J 2020;84:2037-2119 は J-STAGE で CC BY-NC-ND 4.0）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: クラスIは日本語版本文の記載による。手術適応の推奨表（表12・図6）の閾値は取得範囲外で未確認。日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)'
    kokushi: 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-004
  domain: VD
  subdomain: 僧帽弁閉鎖不全症
  assertion:
    plain_statement_ja: 症状のない重症の一次性 MR でも、左室収縮末期径40 mm未満かつ LVEF 60%超で、心房細動も肺高血圧もない段階で、安全で耐久性のある形成術ができるなら早期の手術が推奨される（CQ1：推奨の強さ2、エビデンス総体C）。
    condition:
      guideline: JCS/JATS/JSVS/JSCS 2020年改訂版 弁膜症治療のガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: 無症状の MR は症状が出るまで手術を考えない
  provenance:
    source_ref: SRC-230
    source: 日本循環器学会/日本胸部外科学会/日本血管外科学会/日本心臓血管外科学会合同ガイドライン. 2020年改訂版 弁膜症治療のガイドライン（班長：江石清行ほか）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2020_Izumi_Eishi.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし（英語版 Circ J 2020;84:2037-2119 は J-STAGE で CC BY-NC-ND 4.0）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: CQ の推奨は Minds 方式（推奨の強さ・エビデンス総体）で、推奨クラスとは表記が異なる。日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)'
    kokushi: 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-005
  domain: VD
  subdomain: 大動脈弁狭窄症
  assertion:
    plain_statement_ja: 日本のガイドラインは CQ3 で、大動脈弁最大血流速度5.0 m/秒以上、平均圧較差60 mmHg以上、弁口面積0.6 cm²未満を超重症の大動脈弁狭窄症（AS）の目安としてあげ、症状のない重症 AS でも手術リスクが低ければ手術を推奨している（推奨の強さ2、エビデンス総体B）。
    condition:
      guideline: JCS/JATS/JSVS/JSCS 2020年改訂版 弁膜症治療のガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: 症状のない重症 AS は手術の対象にならない
  provenance:
    source_ref: SRC-230
    source: 日本循環器学会/日本胸部外科学会/日本血管外科学会/日本心臓血管外科学会合同ガイドライン. 2020年改訂版 弁膜症治療のガイドライン（班長：江石清行ほか）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2020_Izumi_Eishi.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし（英語版 Circ J 2020;84:2037-2119 は J-STAGE で CC BY-NC-ND 4.0）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: VD-007（ACC/AHA 2020 の重症・超重症 AS の定義）
  uncertainty: 超重症の3項目の組み合わせ（いずれか1つか、すべてか）は抜粋では確認できなかった。AS の重症度区分の表（表30）は取得範囲外で未確認。日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)'
    kokushi: 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-006
  domain: VD
  subdomain: 大動脈弁狭窄症
  assertion:
    plain_statement_ja: 高齢の AS 患者の治療（外科的大動脈弁置換術か TAVI か、介入するかどうか）は、重症度に加えて年齢、フレイル、認知機能、併存疾患をふまえ、循環器内科医と心臓外科医を中心とする弁膜症チーム（ハートチーム）が専門に偏らずに協議して決める。
    condition:
      guideline: JCS/JATS/JSVS/JSCS 2020年改訂版 弁膜症治療のガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: TAVI か外科的弁置換かは年齢だけで決まる
  provenance:
    source_ref: SRC-230
    source: 日本循環器学会/日本胸部外科学会/日本血管外科学会/日本心臓血管外科学会合同ガイドライン. 2020年改訂版 弁膜症治療のガイドライン（班長：江石清行ほか）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2020_Izumi_Eishi.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし（英語版 Circ J 2020;84:2037-2119 は J-STAGE で CC BY-NC-ND 4.0）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: TAVI と外科的弁置換の選択の年齢の目安（表33 など）は取得範囲外で未確認。日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-007
  domain: VD
  subdomain: 大動脈弁狭窄症
  assertion:
    plain_statement_ja: 米国の ACC/AHA 2020 ガイドラインは、大動脈弁最大血流速度4 m/秒以上または平均圧較差40 mmHg以上を重症 AS とする。弁口面積は通常1.0 cm²以下（体表面積あたり0.6 cm²/m²以下）だが、重症の定義に必須ではない。最大血流速度5 m/秒以上または平均圧較差60 mmHg以上は超重症とされる。
    condition:
      guideline: ACC/AHA 2020 弁膜症ガイドライン
      region: 米国
    differential: null
    common_misconception: 弁口面積が1.0 cm²を超えていれば重症 AS ではない
  provenance:
    source_ref: SRC-231
    source: Otto CM, Nishimura RA, Bonow RO, et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. Circulation 2021;143:e72-e227
    doi: 10.1161/CIR.0000000000000923
    pmid: null
    pmcid: null
    url: https://doi.org/10.1161/CIR.0000000000000923
    source_license: © 2020 American College of Cardiology Foundation and American Heart Association（刊行版の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: VD-005（日本のガイドラインの超重症 AS の目安）
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-008
  domain: VD
  subdomain: 大動脈弁狭窄症
  assertion:
    plain_statement_ja: ACC/AHA 2020 の病期分類では、重症 AS のうち無症状で LVEF が保たれたものを C1、無症状で LVEF 50%未満のものを C2、症状のある高圧較差のものを D1 とする。D1 の症状として、労作時の呼吸困難・運動耐容能の低下・心不全、労作時の狭心痛、労作時の失神や前失神があげられている。
    condition:
      guideline: ACC/AHA 2020 弁膜症ガイドライン
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-231
    source: Otto CM, Nishimura RA, Bonow RO, et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. Circulation 2021;143:e72-e227
    doi: 10.1161/CIR.0000000000000923
    pmid: null
    pmcid: null
    url: https://doi.org/10.1161/CIR.0000000000000923
    source_license: © 2020 American College of Cardiology Foundation and American Heart Association（刊行版の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；TBL-02-05-017 (id: JlAKpfo)；TBL-02-05-021 (id: JlAKpfI)；TBL-02-05-020 (id: JlAKpfU)'
    kokushi: 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-009
  domain: VD
  subdomain: 大動脈弁狭窄症
  assertion:
    plain_statement_ja: 弁口面積1.0 cm²以下なのに安静時の最大血流速度4 m/秒未満・平均圧較差40 mmHg未満の重症 AS には、LVEF 50%未満の古典的な低流量・低圧較差 AS（D2）と、LVEF 50%以上で1回拍出量係数35 mL/m²未満の逆説的な低流量・低圧較差 AS（D3）がある。D2 では低用量ドブタミン負荷で、どの流量でも弁口面積1.0 cm²未満のまま最大血流速度4 m/秒以上に達することが重症の根拠となる（負荷検査は推奨2a、B-NR）。D3 の評価は収縮期血圧140 mmHg未満で行い（推奨1、B-NR）、CT による大動脈弁の石灰化スコアも参考にする（推奨2a、B-NR）。
    condition:
      guideline: ACC/AHA 2020 弁膜症ガイドライン
      region: 米国
    differential: null
    common_misconception: 圧較差が低ければ軽症の AS である
  provenance:
    source_ref: SRC-231
    source: Otto CM, Nishimura RA, Bonow RO, et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. Circulation 2021;143:e72-e227
    doi: 10.1161/CIR.0000000000000923
    pmid: null
    pmcid: null
    url: https://doi.org/10.1161/CIR.0000000000000923
    source_license: © 2020 American College of Cardiology Foundation and American Heart Association（刊行版の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；TBL-02-05-027 (id: JlAKpf4)；TBL-02-05-029 (id: JlAKpgA)'
    kokushi: 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-010
  domain: VD
  subdomain: 感染性心内膜炎
  assertion:
    plain_statement_ja: ACC/AHA 2020 は、人工弁（経カテーテル弁・ホモグラフトを含む）、弁形成に用いた人工材料（人工弁輪・人工腱索・クリップ）、感染性心内膜炎の既往、未修復のチアノーゼ性先天性心疾患、人工パッチやデバイスの近くに遺残短絡や逆流がある修復後の先天性心疾患、構造異常のある弁の逆流を伴う心移植後の患者に限り、歯肉の操作や口腔粘膜の穿孔を伴う歯科処置の前の抗菌薬予防を妥当としている（推奨2a、C-LD）。経食道心エコー、上部・下部消化管内視鏡、膀胱鏡など歯科以外の処置では、活動性の感染がなければ予防投与の利益はない（推奨3：利益なし、B-NR）。
    condition:
      guideline: ACC/AHA 2020 弁膜症ガイドライン
      region: 米国
    differential: null
    common_misconception: 感染性心内膜炎の高リスク患者には、内視鏡検査の前にも抗菌薬の予防投与が必要である
  provenance:
    source_ref: SRC-231
    source: Otto CM, Nishimura RA, Bonow RO, et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. Circulation 2021;143:e72-e227
    doi: 10.1161/CIR.0000000000000923
    pmid: null
    pmcid: null
    url: https://doi.org/10.1161/CIR.0000000000000923
    source_license: © 2020 American College of Cardiology Foundation and American Heart Association（刊行版の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: VD-032（日本の JCS 2017 の歯科処置前の予防投与）
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug)'
    kokushi: 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-011
  domain: VD
  subdomain: リウマチ性心炎
  assertion:
    plain_statement_ja: リウマチ性心疾患の患者にはリウマチ熱の二次予防が推奨される（推奨1、C-EO）。予防の期間は、心炎があり弁膜症が残った場合は10年間か40歳までの長い方、心炎があったが弁膜症が残らなかった場合は10年間か21歳までの長い方、心炎がなかった場合は5年間か21歳までの長い方で、弁置換後も続ける。方法の例は、ベンザチンペニシリンG 120万単位の筋注を4週ごと（一部の高リスクの状況では3週ごと）に行うものである。
    condition:
      guideline: ACC/AHA 2020 弁膜症ガイドライン
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-231
    source: Otto CM, Nishimura RA, Bonow RO, et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. Circulation 2021;143:e72-e227
    doi: 10.1161/CIR.0000000000000923
    pmid: null
    pmcid: null
    url: https://doi.org/10.1161/CIR.0000000000000923
    source_license: © 2020 American College of Cardiology Foundation and American Heart Association（刊行版の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国のガイドラインの推奨。日本でのベンザチンペニシリンG筋注製剤のリウマチ熱予防への承認・保険適用は確認していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-4-C-④（リウマチ性心炎、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-012
  domain: VD
  subdomain: 僧帽弁狭窄症
  assertion:
    plain_statement_ja: 心房細動を伴う弁膜症の抗凝固療法として、ACC/AHA 2020 は、リウマチ性の僧帽弁狭窄症ではビタミンK拮抗薬（ワルファリン）の長期投与を推奨する（推奨1、C-EO）。リウマチ性僧帽弁狭窄症以外の自己弁の弁膜症や、置換後3か月を超えた生体弁では、CHA2DS2-VASc スコアにもとづいて直接経口抗凝固薬（DOAC）をワルファリンの代わりに使える（推奨1、A）。
    condition:
      guideline: ACC/AHA 2020 弁膜症ガイドライン
      region: 米国
    differential: null
    common_misconception: 弁膜症を伴う心房細動には DOAC は使えない
  provenance:
    source_ref: SRC-231
    source: Otto CM, Nishimura RA, Bonow RO, et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. Circulation 2021;143:e72-e227
    doi: 10.1161/CIR.0000000000000923
    pmid: null
    pmcid: null
    url: https://doi.org/10.1161/CIR.0000000000000923
    source_license: © 2020 American College of Cardiology Foundation and American Heart Association（刊行版の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: VD-016（INVICTUS 試験）
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-013
  domain: VD
  subdomain: 弁膜症
  assertion:
    plain_statement_ja: 機械弁の患者では、心房細動の有無にかかわらず DOAC は使わず、ワルファリンなどのビタミンK拮抗薬で抗凝固を行う（DOAC は推奨3：有害、エビデンスB-R）。
    condition:
      guideline: ACC/AHA 2020 弁膜症ガイドライン
      region: 米国
    differential: null
    common_misconception: 機械弁の抗凝固はワルファリンでも DOAC でもよい
  provenance:
    source_ref: SRC-231
    source: Otto CM, Nishimura RA, Bonow RO, et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. Circulation 2021;143:e72-e227
    doi: 10.1161/CIR.0000000000000923
    pmid: null
    pmcid: null
    url: https://doi.org/10.1161/CIR.0000000000000923
    source_license: © 2020 American College of Cardiology Foundation and American Heart Association（刊行版の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）；医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-014
  domain: VD
  subdomain: 僧帽弁狭窄症
  assertion:
    plain_statement_ja: ACC/AHA 2020 は、症状のない僧帽弁狭窄症の心エコーによる経過観察の間隔を、弁口面積1.5 cm²超では3〜5年ごと、1.0〜1.5 cm²では1〜2年ごと、1.0 cm²未満では毎年としている。
    condition:
      guideline: ACC/AHA 2020 弁膜症ガイドライン
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-231
    source: Otto CM, Nishimura RA, Bonow RO, et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. Circulation 2021;143:e72-e227
    doi: 10.1161/CIR.0000000000000923
    pmid: null
    pmcid: null
    url: https://doi.org/10.1161/CIR.0000000000000923
    source_license: © 2020 American College of Cardiology Foundation and American Heart Association（刊行版の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: MS の病期（重症の弁口面積の定義）と経皮的僧帽弁交連切開術の適応の章は取得範囲外で未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-015
  domain: VD
  subdomain: 大動脈弁狭窄症
  assertion:
    plain_statement_ja: PARTNER 3 試験では、手術リスクの低い重症 AS の患者1,000人（平均73歳、STS スコア平均1.9%）をバルーン拡張型弁による TAVI と外科的弁置換に割り付け、1年時点の死亡・脳卒中・再入院の複合は TAVI で8.5%、外科で15.1%だった（ハザード比0.54、95%信頼区間0.37〜0.79）。TAVI では30日時点の脳卒中と新規の心房細動が少なく、入院期間も短かった。主要な血管合併症、ペースメーカー植込み、中等度以上の弁周囲逆流には差がなかった。
    condition:
      population: 手術リスクの低い重症 AS（71施設）
      region: 国際（主に北米）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-238
    source: Mack MJ, et al. Transcatheter Aortic-Valve Replacement with a Balloon-Expandable Valve in Low-Risk Patients. N Engl J Med 2019;380:1695-1705
    doi: 10.1056/NEJMoa1814052
    pmid: '30883058'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1814052
    source_license: 未確認（出版社の著作物と考えられる）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 1年時点の結果で、弁の長期耐久性は追跡報告で確認が必要。ライセンスは未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-016
  domain: VD
  subdomain: 僧帽弁狭窄症
  assertion:
    plain_statement_ja: INVICTUS 試験では、心エコーで確認したリウマチ性心疾患に心房細動を合併し、CHA2DS2-VASc 2以上、僧帽弁口面積2 cm²以下、左房のもやもやエコー、左房内血栓のいずれかをもつ4,565人を、リバーロキサバンとビタミンK拮抗薬に割り付けた。リバーロキサバン群は心血管イベントまたは死亡の複合が多く（制限平均生存時間1,599日対1,675日、差−76日）、死亡も多かった。大出血には有意な差がなかった。
    condition:
      population: リウマチ性心疾患に伴う心房細動
      region: 国際（アジア・アフリカ・南米が中心）
    differential: null
    common_misconception: リウマチ性僧帽弁狭窄症に伴う心房細動でも DOAC はワルファリンと同等に使える
  provenance:
    source_ref: SRC-239
    source: Connolly SJ, Karthikeyan G, et al. Rivaroxaban in Rheumatic Heart Disease-Associated Atrial Fibrillation. N Engl J Med 2022;387:978-988
    doi: 10.1056/NEJMoa2209051
    pmid: '36036525'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2209051
    source_license: 未確認（出版社の著作物と考えられる）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: VD-012（ACC/AHA 2020 の推奨）
  uncertainty: 対象地域は抄録で確認していない。ライセンスは未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-017
  domain: VD
  subdomain: 弁膜症
  assertion:
    plain_statement_ja: 日本胸部外科学会の2021年の集計では、TAVI が12,202件で、単独の大動脈弁置換・形成術（冠動脈バイパス術の併施を含む）8,206件を上回った。単独の僧帽弁手術（同）は4,415件で、僧帽弁手術全体のうち形成術が64.4%を占めた。
    condition:
      region: 日本
      period: 2021年の手術件数
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-240
    source: 'Committee for Scientific Affairs, The Japanese Association for Thoracic Surgery; Yoshimura N, Sato Y, et al. Thoracic and cardiovascular surgeries in Japan during 2021: Annual report by the Japanese Association for Thoracic Surgery. Gen Thorac Cardiovasc Surg 2024;72:254-291'
    doi: 10.1007/s11748-023-01997-6
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s11748-023-01997-6
    source_license: CC BY 4.0（Springer の論文ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: TAVI の件数の集計方法（登録の範囲）は本文で確認していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）；医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-018
  domain: VD
  subdomain: 大動脈弁閉鎖不全症
  assertion:
    plain_statement_ja: 英国心エコー図学会（BSE）2025 は、慢性の重症大動脈弁閉鎖不全症（AR）を示す所見として、縮流部幅0.6 cm超、圧半減時間200 ms未満、下行大動脈の全拡張期逆流（拡張末期流速20 cm/秒以上）、逆流量60 mL超、逆流率50%超、有効逆流弁口面積0.30 cm²超、ジェット幅の左室流出路径に対する比65%超をあげている。腹部大動脈に拡張期の逆流があることは、重症 AR に特異性の高い所見である。
    condition:
      guideline: 英国心エコー図学会（BSE）大動脈弁閉鎖不全症の心エコー評価ガイドライン 2025
      region: 英国（心エコー評価の基準）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-232
    source: 'Victor K, Ring L, Tsampasian V, et al. Echocardiographic assessment of aortic regurgitation: a practical guideline from the British Society of Echocardiography. Echo Res Pract 2025;12:3'
    doi: 10.1186/s44156-024-00067-8
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s44156-024-00067-8
    source_license: CC BY 4.0（刊行版 PDF の表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-4-B-②（大動脈弁閉鎖不全症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-019
  domain: VD
  subdomain: 大動脈弁閉鎖不全症
  assertion:
    plain_statement_ja: BSE 2025 は、AR の患者で左室収縮末期径50 mm超、体表面積あたり25 mm/m²以上、LVEF 55%以下、上行大動脈径55 mm以上（Marfan 症候群・二尖弁・大動脈縮窄では45 mm以上）、手術の閾値に近づく急速な左室拡大を、専門施設への紹介を考える高リスクの所見としている。
    condition:
      guideline: 英国心エコー図学会（BSE）大動脈弁閉鎖不全症の心エコー評価ガイドライン 2025
      region: 英国（心エコー評価の基準）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-232
    source: 'Victor K, Ring L, Tsampasian V, et al. Echocardiographic assessment of aortic regurgitation: a practical guideline from the British Society of Echocardiography. Echo Res Pract 2025;12:3'
    doi: 10.1186/s44156-024-00067-8
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s44156-024-00067-8
    source_license: CC BY 4.0（刊行版 PDF の表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 心エコー評価にもとづく紹介の目安で、手術適応の推奨（推奨クラス）ではない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-4-B-②（大動脈弁閉鎖不全症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-020
  domain: VD
  subdomain: 大動脈弁閉鎖不全症
  assertion:
    plain_statement_ja: 慢性の AR は弁尖の異常、大動脈基部の拡大、またはその両方で起こる。弁の形態異常では二尖弁が最も多く、大動脈の拡大を伴いやすい。急性の重症 AR の原因として多いのは感染性心内膜炎と大動脈解離で、まれに経カテーテル手技のあとや鈍的胸部外傷でも起こる。
    condition:
      guideline: 英国心エコー図学会（BSE）大動脈弁閉鎖不全症の心エコー評価ガイドライン 2025
      region: 英国（心エコー評価の基準）
    differential: 急性の重症 AR では大動脈解離と感染性心内膜炎を考える
    common_misconception: null
  provenance:
    source_ref: SRC-232
    source: 'Victor K, Ring L, Tsampasian V, et al. Echocardiographic assessment of aortic regurgitation: a practical guideline from the British Society of Echocardiography. Echo Res Pract 2025;12:3'
    doi: 10.1186/s44156-024-00067-8
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s44156-024-00067-8
    source_license: CC BY 4.0（刊行版 PDF の表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)'
    kokushi: 医学各論 Ⅴ-4-B-②（大動脈弁閉鎖不全症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-021
  domain: VD
  subdomain: 僧帽弁閉鎖不全症
  assertion:
    plain_statement_ja: 僧帽弁の動きによる Carpentier 分類では、I型は弁尖の動きが正常で弁輪拡大（ときに弁尖穿孔）による逆流、II型は弁尖の過剰な動き（逸脱・弁尖翻転）による逆流、IIIa型は収縮期・拡張期とも弁尖の動きが制限されるもの（リウマチ性の肥厚・癒合が典型）、IIIb型は収縮期だけ動きが制限されるもの（虚血や左室拡大による牽引）である。
    condition:
      guideline: 英国心エコー図学会（BSE）僧帽弁疾患の評価ガイドライン 2021
      region: 英国（心エコー評価の基準）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-233
    source: 'Robinson S, Ring L, Augustine DX, et al. The assessment of mitral valve disease: a guideline from the British Society of Echocardiography. Echo Res Pract 2021;8:G87-G136'
    doi: 10.1530/ERP-20-0034
    pmid: null
    pmcid: null
    url: https://doi.org/10.1530/ERP-20-0034
    source_license: 刊行版 PDF とリポジトリは CC BY-NC-ND 4.0。Springer の現在の論文ページは CC BY 4.0 と表示（食い違い）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a）；医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-022
  domain: VD
  subdomain: 三尖弁閉鎖不全症
  assertion:
    plain_statement_ja: 三尖弁の異常で最も多いのは二次性（機能性）の三尖弁閉鎖不全症（TR）で、主に心房細動や左心系の疾患による弁輪拡大で起こる。一次性の原因には Ebstein 奇形、リウマチ熱、感染性心内膜炎、粘液腫様変性、カルチノイド、放射線、一部のセロトニン作動薬、ペースメーカーなどのリードやカテーテルによる損傷がある。僧帽弁疾患の患者の約30%は、毛細血管後性の肺高血圧のために有意な TR を合併する。
    condition:
      guideline: 英国心エコー図学会（BSE）三尖弁・肺動脈弁の心エコー評価ガイドライン 2020
      region: 英国（心エコー評価の基準）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-234
    source: 'Zaidi A, Oxborough D, Augustine DX, et al. Echocardiographic assessment of the tricuspid and pulmonary valves: a practical guideline from the British Society of Echocardiography. Echo Res Pract 2020;7:G95-G122'
    doi: 10.1530/ERP-20-0033
    pmid: null
    pmcid: null
    url: https://doi.org/10.1530/ERP-20-0033
    source_license: CC BY-NC-ND 4.0（リポジトリの表示。著者最終稿）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 約30%は総説部分の記載（二次資料経由）。著者最終稿で確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-177 (id: Jlvnlt4)'
    kokushi: 医学各論 Ⅴ-4-C-①（三尖弁閉鎖不全症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-023
  domain: VD
  subdomain: 三尖弁閉鎖不全症
  assertion:
    plain_statement_ja: BSE は重症 TR の目安として、3D心エコーの縮流部面積0.4 cm²超、2D の PISA 法による逆流量45 mL超（3D の PISA 法では75 mL超）、心臓MRIでの逆流率50%以上をあげている。弁の構造が正常で右房・右室の拡大がない軽い TR は、健常者にもよくみられる。
    condition:
      guideline: 英国心エコー図学会（BSE）三尖弁・肺動脈弁の心エコー評価ガイドライン 2020
      region: 英国（心エコー評価の基準）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-234
    source: 'Zaidi A, Oxborough D, Augustine DX, et al. Echocardiographic assessment of the tricuspid and pulmonary valves: a practical guideline from the British Society of Echocardiography. Echo Res Pract 2020;7:G95-G122'
    doi: 10.1530/ERP-20-0033
    pmid: null
    pmcid: null
    url: https://doi.org/10.1530/ERP-20-0033
    source_license: CC BY-NC-ND 4.0（リポジトリの表示。著者最終稿）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2D の縮流部幅、有効逆流弁口面積、肝静脈の収縮期逆流などの数値は、取得した著者最終稿の表が途中で切れていて未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-177 (id: Jlvnlt4)；TBL-02-05-027 (id: JlAKpf4)；TBL-02-05-029 (id: JlAKpgA)'
    kokushi: 医学各論 Ⅴ-4-C-①（三尖弁閉鎖不全症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-024
  domain: VD
  subdomain: リウマチ性心炎
  assertion:
    plain_statement_ja: 急性リウマチ熱には確定的な検査がなく、2015年改訂の Jones 基準で臨床的に診断する。低リスク集団の大症状は心炎（臨床的なもの、または心エコーでのみわかる潜在性のもの）、多関節炎、舞踏病、輪状紅斑、皮下結節で、小症状は多関節痛、38.5℃以上の発熱、赤沈60 mm/時以上か CRP 3.0 mg/dL以上、年齢で補正した PR 延長である。初発例は大症状2つ、または大症状1つと小症状2つで可能性が高く、先行する A群溶血性レンサ球菌感染の証拠（咽頭培養、迅速抗原検査、抗体価の上昇）が原則として必要である。
    condition:
      guideline: CDC の急性リウマチ熱の診断（2015年改訂 Jones 基準にもとづく）
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-235
    source: Centers for Disease Control and Prevention. Diagnosing Acute Rheumatic Fever（Group A Strep, Clinical Guidance）. 2025年8月6日確認版
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/group-a-strep/hcp/clinical-guidance/diagnosing-acute-rheumatic-fever.html
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 関節と心臓の所見は、大症状か小症状のどちらか一方にだけ数える
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；PS-02-06-02 (id: JkxnuQk)'
    kokushi: 医学各論 Ⅴ-4-C-④（リウマチ性心炎、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-025
  domain: VD
  subdomain: リウマチ性心炎
  assertion:
    plain_statement_ja: Jones 基準の低リスク集団は、学童期の急性リウマチ熱の発症が10万人あたり年2人未満で、リウマチ性心疾患の有病率が人口1,000人あたり年1人以下の集団をいい、それ以外は中〜高リスク集団とする。中〜高リスク集団では単関節炎と（他の原因を除いた）多関節痛も大症状に、単関節痛と赤沈30 mm/時以上も小症状に含める。再発例は、大症状2つ、大症状1つと小症状2つ、または（他の原因を除外したうえで）小症状3つで推定診断できる。疑い例を含めて全例に心エコー・ドプラ検査を行う。
    condition:
      guideline: CDC の急性リウマチ熱の診断（2015年改訂 Jones 基準にもとづく）
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-235
    source: Centers for Disease Control and Prevention. Diagnosing Acute Rheumatic Fever（Group A Strep, Clinical Guidance）. 2025年8月6日確認版
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/group-a-strep/hcp/clinical-guidance/diagnosing-acute-rheumatic-fever.html
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 舞踏病や緩徐に進む慢性の心炎では、A群溶血性レンサ球菌感染の検査所見がなくても推定診断できる場合がある
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-4-C-④（リウマチ性心炎、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-026
  domain: VD
  subdomain: 弁膜症
  assertion:
    plain_statement_ja: 人工弁のうち生体弁は動物の組織から作られ、抗凝固薬を生涯飲む必要はないが、耐久性が劣り再置換が必要になることがある。機械弁は耐久性が高く通常は再置換を要さないが、生涯にわたる抗凝固療法が必要で、妊娠時のリスクも加わる。
    condition:
      region: 米国（NHLBI の一般向け解説）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-236
    source: 'National Heart, Lung, and Blood Institute. Heart Valve Diseases: Treatment. 2022年3月24日更新'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.nhlbi.nih.gov/health/heart-valve-diseases/treatment
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: VD-013（機械弁には DOAC を使わない）
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）；医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-027
  domain: VD
  subdomain: 感染性心内膜炎
  assertion:
    plain_statement_ja: 日本の感染性心内膜炎ガイドライン（2017年改訂版）は修正 Duke 基準を用いる。大基準は、典型的な起炎菌が2回の血液培養で陽性になるなど持続的な菌血症を示す血液培養所見と、疣腫、膿瘍、人工弁の新たな部分的裂開、新規の弁逆流といった心内膜病変の所見である。小基準は素因、38.0℃以上の発熱、血管現象、免疫学的現象、微生物学的所見の5つで、大基準2つ、大基準1つと小基準3つ、または小基準5つで確診、大基準1つと小基準1つ、または小基準3つで可能性ありとする。
    condition:
      guideline: JCS 2017年改訂版 感染性心内膜炎の予防と治療に関するガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-237
    source: 日本循環器学会ほか合同ガイドライン. 感染性心内膜炎の予防と治療に関するガイドライン（2017年改訂版）（班長：中谷敏）. 2018年3月23日発行、2019年7月1日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_nakatani_h.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2026年改訂版が公表されている（2023年の Duke-ISCVID 基準の扱いなど、改訂版での変更は未確認）。日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug)'
    kokushi: 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-028
  domain: VD
  subdomain: 感染性心内膜炎
  assertion:
    plain_statement_ja: 感染性心内膜炎を疑ったら、好気・嫌気ボトル（各約10 mL）を1セットとして、別々の部位から少なくとも3セットの血液培養をとり、カテーテルからの採血は避ける。重症敗血症などで急ぐ場合は、1時間以内に2セット以上をとって治療を始める。培養期間は通常7日間でよい。
    condition:
      guideline: JCS 2017年改訂版 感染性心内膜炎の予防と治療に関するガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: 血液培養は1セットで十分である
  provenance:
    source_ref: SRC-237
    source: 日本循環器学会ほか合同ガイドライン. 感染性心内膜炎の予防と治療に関するガイドライン（2017年改訂版）（班長：中谷敏）. 2018年3月23日発行、2019年7月1日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_nakatani_h.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 採血の間隔（30分ごと、初回と最後の間隔を1時間以上など）は定まっていないとされる。2026年改訂版での変更は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug)；PS-02-06-03 (id: JkxnuQo)'
    kokushi: 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-029
  domain: VD
  subdomain: 感染性心内膜炎
  assertion:
    plain_statement_ja: 感染性心内膜炎を疑う全例で経胸壁心エコー（TTE）を行い（クラスI、B）、TTE で十分な画像が得られない例、人工弁やデバイスがある例では経食道心エコー（TEE）を行う（クラスI、B）。初回が陰性でも疑いが続けば3〜7日後に再検する（クラスI、C）。疣腫の検出感度は、TTE で自己弁約70%・人工弁約50%、TEE ではいずれも90%以上とされる。
    condition:
      guideline: JCS 2017年改訂版 感染性心内膜炎の予防と治療に関するガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: 経胸壁心エコーで疣腫がなければ感染性心内膜炎は否定できる
  provenance:
    source_ref: SRC-237
    source: 日本循環器学会ほか合同ガイドライン. 感染性心内膜炎の予防と治療に関するガイドライン（2017年改訂版）（班長：中谷敏）. 2018年3月23日発行、2019年7月1日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_nakatani_h.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 感度の数値はガイドラインが引用した研究による（二次資料経由）。2026年改訂版での変更は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-030
  domain: VD
  subdomain: 感染性心内膜炎
  assertion:
    plain_statement_ja: 日本の感染性心内膜炎の起炎菌は、緑色レンサ球菌、ブドウ球菌、腸球菌が上位3つで、黄色ブドウ球菌は増加傾向にあり、MRSA による例は全体の7.5%とされる。腸球菌は約10%で、その多くは高齢者である。
    condition:
      guideline: JCS 2017年改訂版 感染性心内膜炎の予防と治療に関するガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-237
    source: 日本循環器学会ほか合同ガイドライン. 感染性心内膜炎の予防と治療に関するガイドライン（2017年改訂版）（班長：中谷敏）. 2018年3月23日発行、2019年7月1日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_nakatani_h.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug)'
    kokushi: 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-031
  domain: VD
  subdomain: 感染性心内膜炎
  assertion:
    plain_statement_ja: 重い弁機能障害を伴う10 mm以上の疣腫がある左心系（大動脈弁・僧帽弁）の自己弁感染性心内膜炎では、できるだけ早い手術が推奨される（CQ2：推奨の強さ1、エビデンス総体B）。脳梗塞を合併していても手術適応があれば手術を延期しない（CQ3：推奨の強さ1、B）一方、新たな頭蓋内出血があり循環動態が安定していれば、4週間待つことを提案している（推奨の強さ2、C）。
    condition:
      guideline: JCS 2017年改訂版 感染性心内膜炎の予防と治療に関するガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-237
    source: 日本循環器学会ほか合同ガイドライン. 感染性心内膜炎の予防と治療に関するガイドライン（2017年改訂版）（班長：中谷敏）. 2018年3月23日発行、2019年7月1日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_nakatani_h.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: CQ3 の対象から、昏睡、脳ヘルニア、脳出血の合併、大きな中枢神経病変の例は除かれる。心不全・制御できない感染を理由とする手術適応の本文は取得範囲外で未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: VD-032
  domain: VD
  subdomain: 感染性心内膜炎
  assertion:
    plain_statement_ja: 日本の感染性心内膜炎ガイドライン（2017年改訂版）は、成人の高度リスク群では抜歯など菌血症を起こす歯科処置の前の抗菌薬予防投与を推奨し（CQ4：推奨の強さ1、エビデンス総体B）、中等度リスク群でも予防投与を提案している（推奨の強さ2、C）。小児・先天性心疾患でも、高度リスク群で推奨（推奨の強さ1、C）、中等度リスク群で提案（推奨の強さ2、C）としている（CQ5）。
    condition:
      guideline: JCS 2017年改訂版 感染性心内膜炎の予防と治療に関するガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-237
    source: 日本循環器学会ほか合同ガイドライン. 感染性心内膜炎の予防と治療に関するガイドライン（2017年改訂版）（班長：中谷敏）. 2018年3月23日発行、2019年7月1日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_nakatani_h.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: VD-010（米国 ACC/AHA 2020 の予防投与の対象）
  uncertainty: 高度・中等度リスク群に含まれる具体的な疾患の表と、日本人での薬剤・用量は取得範囲外で未確認。2026年改訂版での変更は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug)'
    kokushi: 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-001
  domain: MP
  subdomain: 肥大型心筋症
  assertion:
    plain_statement_ja: 肥大型心筋症（HCM）は、左室または右室の心筋肥大と、肥大にもとづく左室拡張能の低下を特徴とする疾患群である。心エコーか心臓MRIで最大左室壁厚15 mm以上（HCM の家族歴があれば13 mm以上）を診断の目安とし、高血圧、弁膜症、蓄積病など心肥大を起こす二次性の原因を除外する。
    condition:
      guideline: JCS/JHFS 心筋症診療ガイドライン（2018年改訂版）（日本語版）
      region: 日本
    differential: 高血圧性心疾患、大動脈弁狭窄症、心アミロイドーシス、Fabry 病
    common_misconception: 左室肥大があれば HCM と診断できる
  provenance:
    source_ref: SRC-241
    source: 日本循環器学会/日本心不全学会合同ガイドライン. 心筋症診療ガイドライン（2018年改訂版）（班長：北岡裕章、筒井裕之）. 2019年3月29日発行、2019年6月28日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2018_tsutsui_kitaoka.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-6-B-①（肥大型心筋症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-002
  domain: MP
  subdomain: 肥大型心筋症
  assertion:
    plain_statement_ja: HCM は、安静時の左室流出路圧較差が30 mmHg以上（または誘発で30 mmHg以上）の閉塞性、安静時・誘発時とも30 mmHg未満の非閉塞性、心室中部の圧較差が30 mmHg以上の心室中部閉塞性、心尖部に肥大が限られる心尖部肥大型、肥大が減って LVEF が50%未満となった拡張相に分けられる。
    condition:
      guideline: JCS/JHFS 心筋症診療ガイドライン（2018年改訂版）（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-241
    source: 日本循環器学会/日本心不全学会合同ガイドライン. 心筋症診療ガイドライン（2018年改訂版）（班長：北岡裕章、筒井裕之）. 2019年3月29日発行、2019年6月28日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2018_tsutsui_kitaoka.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-6-B-①（肥大型心筋症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-003
  domain: MP
  subdomain: 肥大型心筋症
  assertion:
    plain_statement_ja: 日本の HCM は、1998年の全国調査で人口10万人あたり17.3人と報告され、コホート研究からは約500人に1人と推定されている。心尖部肥大型が約15%と米国（約3%）より多いのが日本の特徴で、心室中部閉塞性は約10%と報告されている。
    condition:
      guideline: JCS/JHFS 心筋症診療ガイドライン（2018年改訂版）（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-241
    source: 日本循環器学会/日本心不全学会合同ガイドライン. 心筋症診療ガイドライン（2018年改訂版）（班長：北岡裕章、筒井裕之）. 2019年3月29日発行、2019年6月28日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2018_tsutsui_kitaoka.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)'
    kokushi: 医学各論 Ⅴ-6-B-①（肥大型心筋症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-004
  domain: MP
  subdomain: 肥大型心筋症
  assertion:
    plain_statement_ja: HCM の約60%は常染色体優性遺伝の家族歴をもち、そのうち約40〜60%にサルコメア遺伝子の変異がみつかる。原因遺伝子として多いのは MYH7（β-ミオシン重鎖）と MYBPC3（心筋ミオシン結合蛋白C）で、ほかに TNNT2、TNNI3、TPM1、MYL3 などがある。
    condition:
      guideline: JCS/JHFS 心筋症診療ガイドライン（2018年改訂版）（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-241
    source: 日本循環器学会/日本心不全学会合同ガイドライン. 心筋症診療ガイドライン（2018年改訂版）（班長：北岡裕章、筒井裕之）. 2019年3月29日発行、2019年6月28日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2018_tsutsui_kitaoka.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)'
    kokushi: 医学各論 Ⅴ-6-B-①（肥大型心筋症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-005
  domain: MP
  subdomain: 肥大型心筋症
  assertion:
    plain_statement_ja: HCM の突然死の危険因子には、運動に関連した原因不明の失神、運動時の血圧上昇が25 mmHg未満にとどまるか低下する異常反応、非持続性心室頻拍などがある。心臓MRIの遅延造影の有無と広がりは突然死を含む心臓死と関連し、評価が推奨されている（推奨クラスI、エビデンスレベルA）。閉塞性の例では、血管拡張薬の使用、立ち上がり、飲酒をきっかけに失神しやすい。
    condition:
      guideline: JCS/JHFS 心筋症診療ガイドライン（2018年改訂版）（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-241
    source: 日本循環器学会/日本心不全学会合同ガイドライン. 心筋症診療ガイドライン（2018年改訂版）（班長：北岡裕章、筒井裕之）. 2019年3月29日発行、2019年6月28日更新（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2018_tsutsui_kitaoka.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 推奨クラスI・エビデンスレベルA の対象となる推奨文（表16）の文言は未確認。ICD の推奨と、最大壁厚などその他の危険因子は取得範囲外で未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；TBL-02-05-029 (id: JlAKpgA)；TBL-02-05-017 (id: JlAKpfo)'
    kokushi: 医学各論 Ⅴ-6-B-①（肥大型心筋症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-006
  domain: MP
  subdomain: 肥大型心筋症
  assertion:
    plain_statement_ja: 厚生労働省の指定難病の資料では、HCM の患者には競技スポーツなどの激しい運動を禁止し、症状があればβ遮断薬かベラパミルを使い、ジヒドロピリジン系カルシウム拮抗薬は通常使わない。心室頻拍がある例では植込み型除細動器を考え、薬が効かない閉塞性の例では経皮的中隔心筋焼灼術（PTSMA）や心室筋切除術を、拡張相で難治性の心不全となった例では心臓移植を考える。患者数（令和元年度の医療受給者証保持者）は4,205人である。
    condition:
      region: 日本
      framework: 指定難病58（難病法）
    differential: null
    common_misconception: 閉塞性 HCM の症状には血管拡張薬が有効である
  provenance:
    source_ref: SRC-242
    source: 厚生労働省. 指定難病 58 肥大型心筋症 概要、診断基準等（令和8年4月時点の掲載）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173536.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: MP-005（閉塞性では血管拡張薬で失神しやすい）
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-6-B-①（肥大型心筋症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-007
  domain: MP
  subdomain: 肥大型心筋症
  assertion:
    plain_statement_ja: マバカムテンは心筋ミオシンを選択的かつ可逆的に阻害し、ミオシンとアクチンの過剰な結合を減らして心筋の過収縮と左室流出路の狭窄を改善すると考えられている薬で、日本では閉塞性肥大型心筋症を効能・効果として審査された（2025年の審査報告書）。成人では1日1回2.5 mgから始め、状態に応じて増減し、最大は1回15 mgとされた。承認の条件として、一定数の症例が集まるまで全例を対象とする使用成績調査が求められた。
    condition:
      region: 日本
      framework: 医薬品の承認審査
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-243
    source: 医薬品医療機器総合機構. カムザイオスカプセル（マバカムテン）審査報告書. 令和7年3月7日
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/drugs/2025/P20250403002/670605000_30700AMX00075_A100_2.pdf
    source_license: 未確認（PMDA の利用規約を確認していない）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 承認日は抜粋に記載がなく未確認（令和7年3月6日の部会で承認可とされ、報告書は同年3月7日付）。添付文書の LVEF の監視や併用薬・遺伝子型による用量調節の記載は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-6-B-①（肥大型心筋症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-008
  domain: MP
  subdomain: 拡張型心筋症
  assertion:
    plain_statement_ja: 拡張型心筋症（DCM）は左室のびまん性の拡大と収縮能の低下を特徴とし、高血圧性・弁膜性・虚血性（冠動脈造影で原因となる病変がないことを確認する）のほか、アルコール性、心筋炎、神経・筋疾患、膠原病、栄養性・代謝性、不整脈性、アミロイドーシス、サルコイドーシス、薬剤性などの二次性の原因をすべて除外して診断する。家族性の割合は、海外の報告で20〜30%、国内の1999年の全国調査で5%である。
    condition:
      region: 日本
      framework: 指定難病57（難病法）
    differential: アルコール性心筋症、虚血性心筋症、心サルコイドーシス、心筋炎、頻脈誘発性心筋症
    common_misconception: null
  provenance:
    source_ref: SRC-244
    source: 厚生労働省. 指定難病 57 特発性拡張型心筋症 概要、診断基準等（令和8年4月時点の掲載）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173537.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: LVEF や左室径の具体的な閾値は資料に記載がない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)'
    kokushi: 医学各論 Ⅴ-6-B-②（拡張型心筋症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-009
  domain: MP
  subdomain: 拡張型心筋症
  assertion:
    plain_statement_ja: DCM の治療は心不全の治療に準じ、食塩を1日5〜8 gに制限し、ACE阻害薬、β遮断薬、サクビトリル・バルサルタン、SGLT2阻害薬、HCNチャネル遮断薬、うっ血には利尿薬を用いる。スピロノラクトンは長期予後を改善し、β遮断薬は突然死を減らす。重症の心室性不整脈にはアミオダロンを使い、薬が効かなければ植込み型除細動器を考える。根治的な治療は心臓移植だけである。
    condition:
      region: 日本
      framework: 指定難病57（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-244
    source: 厚生労働省. 指定難病 57 特発性拡張型心筋症 概要、診断基準等（令和8年4月時点の掲載）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173537.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 資料の「SGLT阻害薬」を SGLT2阻害薬と表記した。心臓再同期療法は資料に記載がない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；PS-02-06-04 (id: JkxnuQs)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-6-B-②（拡張型心筋症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-010
  domain: MP
  subdomain: 拡張型心筋症
  assertion:
    plain_statement_ja: 指定難病の資料では、DCM の5年生存率は76%で、主な死因は心不全と不整脈である。予後不良に関連する因子として、男性、高齢、家族歴、NYHA III度の心不全、心胸比60%以上、左室の拡大、駆出率の低下があげられている。患者数（令和元年度の医療受給者証保持者）は19,423人である。
    condition:
      region: 日本
      framework: 指定難病57（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-244
    source: 厚生労働省. 指定難病 57 特発性拡張型心筋症 概要、診断基準等（令和8年4月時点の掲載）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173537.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 5年生存率の調査年代は資料に明記がない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)'
    kokushi: 医学各論 Ⅴ-6-B-②（拡張型心筋症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-011
  domain: MP
  subdomain: 拘束型心筋症
  assertion:
    plain_statement_ja: 拘束型心筋症（RCM）は、硬い左室による拡張障害を基本とし、左室の拡大・肥大がなく、収縮能が正常かそれに近く、原因となる心疾患がないものをいう。目安は左室拡張末期径55 mm以下、心室中隔・後壁厚12 mm以下、LVEF 50%以上で、左房は拡大する（左房径50 mm超または左房容積140 mL超）。治療が異なる収縮性心膜炎との鑑別が重要で、心内膜心筋生検が望ましい。米国の成人の調査では5年生存率64%、10年生存率37%で、小児例の予後は極めて悪い。患者数（令和元年度の医療受給者証保持者）は100人未満である。
    condition:
      region: 日本
      framework: 指定難病59（難病法）
    differential: 収縮性心膜炎、心アミロイドーシス
    common_misconception: null
  provenance:
    source_ref: SRC-245
    source: 厚生労働省. 指定難病 59 拘束型心筋症 概要、診断基準等（令和8年4月時点の掲載）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173535.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: MP-026（収縮性心膜炎）
  uncertainty: 生存率は資料が引用した米国の調査による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)'
    kokushi: 医学各論 Ⅴ-6-B-③（拘束型心筋症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-012
  domain: MP
  subdomain: 心アミロイドーシス
  assertion:
    plain_statement_ja: 心アミロイドーシスの主な病型は、免疫グロブリン軽鎖による AL型、野生型トランスサイレチン（TTR）による ATTRwt型（主に60歳以上の男性に多い。旧称は老人性全身性アミロイドーシス）、TTR 遺伝子の変異による遺伝性の ATTRv型（日本では熊本県と長野県に集積）、血清アミロイドAによる AA型で、AA型の心病変はまれである。
    condition:
      guideline: JCS 2020年版 心アミロイドーシス診療ガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-246
    source: 日本循環器学会ほか合同ガイドライン. 2020年版 心アミロイドーシス診療ガイドライン（班長：北岡裕章）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2020/04/JCS2020_Kitaoka.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)'
    kokushi: 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-013
  domain: MP
  subdomain: 心アミロイドーシス
  assertion:
    plain_statement_ja: ATTRwt型は確定例の80〜98%が男性で、40〜50%に手根管症候群（多くは両側性）の既往があり、手根管症候群が心症状に平均約7年先行したという報告がある。
    condition:
      guideline: JCS 2020年版 心アミロイドーシス診療ガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: 手根管症候群は心疾患の手がかりにならない
  provenance:
    source_ref: SRC-246
    source: 日本循環器学会ほか合同ガイドライン. 2020年版 心アミロイドーシス診療ガイドライン（班長：北岡裕章）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2020/04/JCS2020_Kitaoka.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)'
    kokushi: 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-014
  domain: MP
  subdomain: 心アミロイドーシス
  assertion:
    plain_statement_ja: ATTR型心アミロイドーシスの診断には 99mTc-ピロリン酸シンチグラフィを使い、3時間後の視覚評価で Grade 2 以上、または1時間後の心臓と対側胸部の集積比（H/CL 比）1.5以上を陽性とする。ガイドライン作成時点（2020年）では、心アミロイドーシスに対するこの検査の保険適用はなかった。
    condition:
      guideline: JCS 2020年版 心アミロイドーシス診療ガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-246
    source: 日本循環器学会ほか合同ガイドライン. 2020年版 心アミロイドーシス診療ガイドライン（班長：北岡裕章）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2020/04/JCS2020_Kitaoka.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 保険適用は2020年時点の記載で、その後の状況は未確認。推奨の強さ（CQ1）の表は取得範囲外で未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)；TBL-02-05-028 (id: JlAKpf8)'
    kokushi: 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-015
  domain: MP
  subdomain: 心アミロイドーシス
  assertion:
    plain_statement_ja: ATTRwt型と診断するには、AL型を除外するため、血清・尿の免疫固定法と血清遊離軽鎖を組み合わせてM蛋白がないことを確かめる（免疫固定法は免疫電気泳動より感度が高い）。ATTRwt型に意義不明の単クローン性ガンマグロブリン血症（MGUS）が併存する例も10〜18%あると報告されている。生検は腹壁脂肪吸引、皮膚、消化管、口唇などで行い、陰性なら心筋生検を考える。
    condition:
      guideline: JCS 2020年版 心アミロイドーシス診療ガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: ピロリン酸シンチグラフィが陽性ならM蛋白の検査は不要である
  provenance:
    source_ref: SRC-246
    source: 日本循環器学会ほか合同ガイドライン. 2020年版 心アミロイドーシス診療ガイドライン（班長：北岡裕章）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2020/04/JCS2020_Kitaoka.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: MGUS 併存の割合はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)'
    kokushi: 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-016
  domain: MP
  subdomain: 心アミロイドーシス
  assertion:
    plain_statement_ja: タファミジスは TTR の四量体を安定化させる薬で、日本では2013年11月に ATTRv型の神経障害で保険収載され、2019年3月に ATTR型心アミロイドーシスへの適応が承認された（後者は ATTR-ACT 試験にもとづく）。投与は診断の確定を確認し、診断と治療に精通した医師のもとで行う。
    condition:
      guideline: JCS 2020年版 心アミロイドーシス診療ガイドライン（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-246
    source: 日本循環器学会ほか合同ガイドライン. 2020年版 心アミロイドーシス診療ガイドライン（班長：北岡裕章）. 2020年3月13日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.j-circ.or.jp/cms/wp-content/uploads/2020/04/JCS2020_Kitaoka.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 推奨の強さと施設・医師の要件（表38）は取得範囲外で未確認。日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-017
  domain: MP
  subdomain: 心アミロイドーシス
  assertion:
    plain_statement_ja: アミロイドーシスの確定診断は、生検組織のコンゴーレッド染色が陽性で偏光顕微鏡で緑色の複屈折を示すことで行い、免疫染色や質量分析で病型を決める。心病変では、心室壁の肥厚（心室中隔・左室後壁12 mm超など）、BNP・トロポニンの上昇、心臓MRIの遅延造影、左室基部の strain 低下（apical sparing）などがみられる。
    condition:
      region: 日本
      framework: 指定難病28（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-247
    source: 厚生労働省. 指定難病 28 全身性アミロイドーシス 概要、診断基準等（令和8年4月時点の掲載）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173465.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)；TBL-02-05-027 (id: JlAKpf4)；TBL-02-05-029 (id: JlAKpgA)'
    kokushi: 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-018
  domain: MP
  subdomain: 心アミロイドーシス
  assertion:
    plain_statement_ja: 指定難病の資料では、AL型に自家末梢血幹細胞移植を併用した大量化学療法、ボルテゾミブ、ダラツムマブ、ATTRv型に肝移植、タファミジス、siRNA 製剤のパチシラン、ATTRwt型の心症状にタファミジスが用いられるとしている。全身性アミロイドーシスの患者数（令和元年度の医療受給者証保持者）は3,131人である。
    condition:
      region: 日本
      framework: 指定難病28（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-247
    source: 厚生労働省. 指定難病 28 全身性アミロイドーシス 概要、診断基準等（令和8年4月時点の掲載）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173465.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: ATTR に対するその他の薬剤（TTR の産生を抑える薬など）の国内承認状況は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-019
  domain: MP
  subdomain: 心サルコイドーシス
  assertion:
    plain_statement_ja: 心サルコイドーシスの心臓病変は、主徴候5つ（高度房室ブロックまたは致死性心室性不整脈、心室中隔基部の菲薄化または心室壁の形態異常、LVEF 50%未満または局所壁運動異常、Ga シンチグラフィか FDG-PET での心臓への異常集積、ガドリニウム造影MRIの遅延造影）と副徴候3つ（心電図異常、心筋血流 SPECT の欠損、心内膜心筋生検での単核細胞浸潤と中等度以上の間質線維化）で判定し、主徴候2つ以上、または主徴候1つと副徴候2つ以上で心臓病変ありとする。全身治療の第一選択は副腎皮質ステロイドで、再発・難治例ではメトトレキサートなどの免疫抑制薬を加える。
    condition:
      region: 日本
      framework: 指定難病84（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-248
    source: 厚生労働省. 指定難病 84 サルコイドーシス 概要、診断基準等（令和8年4月時点の掲載）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173502.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: サルコイドーシス全体の患者数（令和元年度の医療受給者証保持者）は14,950人で、心病変をもつ患者数は資料に記載がない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)；TBL-02-05-028 (id: JlAKpf8)；TBL-02-05-029 (id: JlAKpgA)；TBL-01-00-165 (id: Jlvnlsc)'
    kokushi: 医学各論 Ⅴ-6-C-②（心サルコイドーシス、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-020
  domain: MP
  subdomain: 筋ジストロフィー
  assertion:
    plain_statement_ja: Duchenne型と Becker型の筋ジストロフィーはジストロフィン遺伝子（DMD）の異常によるX連鎖性の疾患で、Duchenne型では血清CKが著しく高い。筋ジストロフィーは骨格筋のほか心筋も侵し、Duchenne型では拡張型心筋症を合併して心不全や不整脈を起こしうる。心筋障害は呼吸不全とともに生命予後を左右する。
    condition:
      region: 日本
      framework: 指定難病113（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-249
    source: 厚生労働省. 指定難病 113 筋ジストロフィー 概要、診断基準等（令和8年4月時点の掲載）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001174033.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 死因に占める心筋障害の割合と心保護薬の記載は資料にない。筋ジストロフィー全体の患者数は約25,400人とされる
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)'
    kokushi: 医学各論 Ⅴ-6-C-⑤（筋ジストロフィー、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-021
  domain: MP
  subdomain: ウイルス性心筋炎
  assertion:
    plain_statement_ja: 心筋炎と心膜炎の多くはウイルスが原因で、SARS-CoV-2、アデノウイルス、コクサッキーウイルスなどがある。ほかに関節リウマチや全身性エリテマトーデスなどの自己免疫疾患、一部の薬剤やがん治療、まれにワクチンへの反応も原因となる。心筋炎と心膜炎は若年成人に多い。
    condition:
      region: 米国（NHLBI の一般向け解説）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-250
    source: 'National Heart, Lung, and Blood Institute. Heart Inflammation: Causes and Risk Factors. 2023年10月更新'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.nhlbi.nih.gov/health/heart-inflammation/causes
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-180 (id: JlvnluY)；TBL-01-00-182 (id: Jlvnluk)'
    kokushi: 医学各論 Ⅴ-6-A-①（ウイルス性心筋炎、a）；医学各論 Ⅴ-6-D-①（急性心膜炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-022
  domain: MP
  subdomain: ウイルス性心筋炎
  assertion:
    plain_statement_ja: 日本の全国調査（2002年報告）では、経皮的心肺補助（PCPS）で治療した劇症型心筋炎52人のうち30人（57.7%）が救命されて社会復帰し、平均962日の追跡で再入院は10%、死亡は10%だった。
    condition:
      region: 日本
      period: 2002年の報告
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-251
    source: 'Aoyama N, Izumi T, Hiramori K, et al. National Survey of Fulminant Myocarditis in Japan: Therapeutic Guidelines and Long-Term Prognosis of Using Percutaneous Cardiopulmonary Support for Fulminant Myocarditis. Circ J 2002;66:133-144'
    doi: 10.1253/circj.66.133
    pmid: null
    pmcid: null
    url: https://doi.org/10.1253/circj.66.133
    source_license: © 2002 The Japanese Circulation Society（Free Access。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 現在の補助循環（IMPELLA など）を含む治療成績とは異なる可能性がある。2023年改訂版の心筋炎ガイドラインの本文は取得できず未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-180 (id: JlvnluY)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-6-A-①（ウイルス性心筋炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-023
  domain: MP
  subdomain: 急性心膜炎
  assertion:
    plain_statement_ja: 急性心膜炎は、心膜炎に特徴的な胸痛、心膜摩擦音、広範な ST 上昇または PR 低下、心膜液貯留の4つのうち2つ以上で診断する。CRP・赤沈・白血球などの炎症所見や、CT・MRI での心膜の炎症所見が診断を支持する。
    condition:
      guideline: ESC 2015 心膜疾患ガイドライン（Acta Cardiol 2016 の要約）
      region: 欧州
    differential: 急性心筋梗塞（ST 上昇の分布や PR 低下の有無で見分ける）
    common_misconception: null
  provenance:
    source_ref: SRC-252
    source: Van Camp G, Pasquet A, Sinnaeve P, et al. Summary 2015 ESC guidelines（心膜疾患ほか）. Acta Cardiol 2016;71:7-13
    doi: 10.2143/AC.71.1.3132092
    pmid: null
    pmcid: null
    url: https://doi.org/10.2143/AC.71.1.3132092
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ESC 2015 ガイドラインの本文ではなく要約論文で確認した（二次資料経由）。2025年に ESC の心筋炎・心膜炎ガイドラインが公表されている
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-182 (id: Jlvnluk)；TBL-02-05-021 (id: JlAKpfI)'
    kokushi: 医学各論 Ⅴ-6-D-①（急性心膜炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-024
  domain: MP
  subdomain: 急性心膜炎
  assertion:
    plain_statement_ja: 急性心膜炎の初期治療は、アスピリンか NSAIDs にコルヒチンを加える（コルヒチンの併用は推奨クラスI、エビデンスレベルA）。コルヒチンは体重70 kg未満では0.5 mgを1日1回、70 kg以上では1日2回とし、3か月続ける。副腎皮質ステロイドは第一選択にしない（クラスIII、C）。38℃超の発熱、亜急性の発症、大量の心膜液、心タンポナーデ、1週間以上のアスピリン・NSAIDs に反応しないことは予後不良の主要因子で、入院を考える。
    condition:
      guideline: ESC 2015 心膜疾患ガイドライン（Acta Cardiol 2016 の要約）
      region: 欧州
    differential: null
    common_misconception: 急性心膜炎の第一選択はステロイドである
  provenance:
    source_ref: SRC-252
    source: Van Camp G, Pasquet A, Sinnaeve P, et al. Summary 2015 ESC guidelines（心膜疾患ほか）. Acta Cardiol 2016;71:7-13
    doi: 10.2143/AC.71.1.3132092
    pmid: null
    pmcid: null
    url: https://doi.org/10.2143/AC.71.1.3132092
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ESC 2015 ガイドラインの要約論文で確認した（二次資料経由）。国内でのコルヒチンの心膜炎への保険適用は確認していない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-182 (id: Jlvnluk)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-6-D-①（急性心膜炎、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-025
  domain: MP
  subdomain: 心タンポナーデ
  assertion:
    plain_statement_ja: 心膜液の量・分布・循環への影響はまず心エコーで評価する。心タンポナーデでは、心エコーか透視で誘導した緊急の心膜穿刺、または外科的ドレナージ（化膿性心膜炎や出血の場合）を行う。内科治療に反応しない症状のある中等量〜大量の心膜液や、細菌性・腫瘍性が疑われる心膜液も心膜穿刺の対象となる。
    condition:
      guideline: ESC 2015 心膜疾患ガイドライン（Acta Cardiol 2016 の要約）
      region: 欧州
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-252
    source: Van Camp G, Pasquet A, Sinnaeve P, et al. Summary 2015 ESC guidelines（心膜疾患ほか）. Acta Cardiol 2016;71:7-13
    doi: 10.2143/AC.71.1.3132092
    pmid: null
    pmcid: null
    url: https://doi.org/10.2143/AC.71.1.3132092
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ESC 2015 ガイドラインの要約論文で確認した（二次資料経由）。奇脈などの身体所見の記載は要約になく未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-184 (id: Jlvnluw)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-6-E（心タンポナーデ、a）；医学各論 Ⅴ-6-D-②（心囊液貯留、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-026
  domain: MP
  subdomain: 収縮性心膜炎
  assertion:
    plain_statement_ja: 収縮性心膜炎になるリスクは原因によって異なり、ウイルス性・特発性では低く、細菌性（とくに化膿性）では高い。右心不全の徴候と心エコーでの拡張期の充満障害から診断し、CT・MRI は二次的な検査、非侵襲的検査で決まらなければ心臓カテーテル検査を行う。3〜6か月を超えて続く慢性の収縮には心膜切除術が基本で、炎症に伴う一過性の収縮は内科治療で改善することがある。
    condition:
      guideline: ESC 2015 心膜疾患ガイドライン（Acta Cardiol 2016 の要約）
      region: 欧州
    differential: 拘束型心筋症
    common_misconception: null
  provenance:
    source_ref: SRC-252
    source: Van Camp G, Pasquet A, Sinnaeve P, et al. Summary 2015 ESC guidelines（心膜疾患ほか）. Acta Cardiol 2016;71:7-13
    doi: 10.2143/AC.71.1.3132092
    pmid: null
    pmcid: null
    url: https://doi.org/10.2143/AC.71.1.3132092
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: MP-011（拘束型心筋症）
  uncertainty: ESC 2015 ガイドラインの要約論文で確認した（二次資料経由）。原因別の発症率の数値は要約になく未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-183 (id: Jlvnlus)；TBL-02-05-027 (id: JlAKpf4)；TBL-02-05-030 (id: JlAKpgE)'
    kokushi: 医学各論 Ⅴ-6-D-③（収縮性心膜炎、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-027
  domain: MP
  subdomain: たこつぼ心筋症
  assertion:
    plain_statement_ja: 欧米26施設の登録研究（1,750人）では、たこつぼ症候群の89.8%が女性で、平均年齢は66.8歳だった。身体的な誘因（36.0%）が精神的な誘因（27.7%）より多く、28.5%は誘因がなかった。神経・精神疾患の合併は55.8%で、年齢・性別をそろえた急性冠症候群（25.7%）より多かった。
    condition:
      population: InterTAK 登録
      region: 欧州・米国
    differential: 急性冠症候群
    common_misconception: たこつぼ症候群の誘因はほとんどが精神的ストレスである
  provenance:
    source_ref: SRC-253
    source: Templin C, Ghadri JR, Diekmann J, et al. Clinical Features and Outcomes of Takotsubo (Stress) Cardiomyopathy. N Engl J Med 2015;373:929-938
    doi: 10.1056/NEJMoa1406761
    pmid: null
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1406761
    source_license: 未確認（リポジトリに表示なし。出版社の著作物と考えられる）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ライセンスは未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-6-H-①（たこつぼ心筋症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-028
  domain: MP
  subdomain: たこつぼ心筋症
  assertion:
    plain_statement_ja: 同じ登録研究で、たこつぼ症候群の入院時の LVEF は平均40.7%と急性冠症候群（51.5%）より低く、院内のショックと死亡の頻度は急性冠症候群と差がなかった。長期には主要心脳血管イベントが1人年あたり9.9%、死亡が1人年あたり5.6%で起きた。身体的な誘因、急性の神経・精神疾患、高いトロポニン値、入院時の低い駆出率が院内合併症の予測因子だった。
    condition:
      population: InterTAK 登録
      region: 欧州・米国
    differential: null
    common_misconception: たこつぼ症候群は予後のよい良性の病態である
  provenance:
    source_ref: SRC-253
    source: Templin C, Ghadri JR, Diekmann J, et al. Clinical Features and Outcomes of Takotsubo (Stress) Cardiomyopathy. N Engl J Med 2015;373:929-938
    doi: 10.1056/NEJMoa1406761
    pmid: null
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1406761
    source_license: 未確認（リポジトリに表示なし。出版社の著作物と考えられる）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ライセンスは未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-6-H-①（たこつぼ心筋症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-029
  domain: MP
  subdomain: 心臓震盪
  assertion:
    plain_statement_ja: 心臓震盪は、前胸部への鈍的な打撃で心室細動（または心室頻拍）が起こる病態である。動物実験では、T波の上行脚の約15ミリ秒（心周期の約1%）の間に衝撃が加わったときだけ心室細動が起きた。米国の登録（2012年7月までに216例）では95%が男性、平均年齢15歳で、野球が51%を占め、多くはボールなどの硬い投射物によるものだった。
    condition:
      region: 米国（登録研究）
    differential: null
    common_misconception: 心臓震盪は胸部に強い外傷や骨折があるときに起こる
  provenance:
    source_ref: SRC-254
    source: Peng T, Trollinger Derry L, Yogeswaran V, et al. Commotio Cordis in 2023. Sports Med 2023;53:1527-1536
    doi: 10.1007/s40279-023-01873-6
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s40279-023-01873-6
    source_license: Open access（© The Author(s)）。CC の種類は未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 総説の記載で、元の登録研究・動物実験の論文は未確認（二次資料経由）。ライセンスの種類は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-171 (id: JlvnltA)'
    kokushi: 医学各論 Ⅴ-6-H-②（心臓震盪、b）；医学各論 Ⅴ-1-B-③（心室細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-030
  domain: MP
  subdomain: 心臓震盪
  assertion:
    plain_statement_ja: 心臓震盪の生存率は初期の報告では10〜15%だったが、2013年の米国登録の更新では58%に上がった。倒れてから蘇生開始までが3分未満なら生存40%、3分を超えると5%で、ただちに心肺蘇生と AED による除細動を行うことが救命の鍵である。
    condition:
      region: 米国（登録研究）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-254
    source: Peng T, Trollinger Derry L, Yogeswaran V, et al. Commotio Cordis in 2023. Sports Med 2023;53:1527-1536
    doi: 10.1007/s40279-023-01873-6
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s40279-023-01873-6
    source_license: Open access（© The Author(s)）。CC の種類は未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 総説の記載で、元の登録研究の論文は未確認（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-171 (id: JlvnltA)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-6-H-②（心臓震盪、b）；医学各論 Ⅴ-1-B-③（心室細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-031
  domain: MP
  subdomain: 粘液腫
  assertion:
    plain_statement_ja: 心臓粘液腫の手術例80人の単施設研究（2010〜2021年）では、67.5%が女性、平均年齢は46.3歳で、腫瘍の83.75%が左房、13.75%が右房にあった。症状は息切れが86.25%と最も多く、脳卒中が6.25%にみられた。再発は11.25%、術後30日死亡は3.75%だった。
    condition:
      population: 1施設の手術例
      region: 単施設（国名は本文で未確認）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-255
    source: 'Alhasso AA, Ahmed OF, Mohammed-Saeed DH, et al. Operative management and outcomes in patients with myxomas: A single-center experience. Front Surg 2023;10:1084447'
    doi: 10.3389/fsurg.2023.1084447
    pmid: null
    pmcid: null
    url: https://doi.org/10.3389/fsurg.2023.1084447
    source_license: CC BY（刊行版 PDF の表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 単施設の後ろ向き研究で、頻度は集団によって異なる
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-642 (id: JlvnmcA)'
    kokushi: 医学各論 Ⅴ-6-F-①（粘液腫、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: MP-032
  domain: MP
  subdomain: 粘液腫
  assertion:
    plain_statement_ja: Carney 複合は、心臓・皮膚などの粘液腫、口唇や眼の周囲などの色素斑（黒子）、内分泌腫瘍（約25%に原発性色素性結節性副腎皮質病変による Cushing 症候群など）を特徴とする常染色体優性遺伝の疾患で、多くは PRKAR1A 遺伝子の変異による。心臓粘液腫は血流を妨げて突然死の原因となることがあり、切除後も再発しやすい。約30%は新生変異による。
    condition:
      region: 米国（NLM の解説）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-256
    source: MedlinePlus Genetics. Carney complex. 2025年3月10日更新
    doi: null
    pmid: null
    pmcid: null
    url: https://medlineplus.gov/genetics/condition/carney-complex
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-642 (id: JlvnmcA)'
    kokushi: 医学各論 Ⅴ-6-F-①（粘液腫、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-001
  domain: CH
  subdomain: 先天性心疾患
  assertion:
    plain_statement_ja: 先天性心疾患は出生の約1%（米国で年約4万人）にみられ、その約4人に1人は重症（critical）である。重症の先天性心疾患の1年生存率は約75%、18歳までの生存率は約69%で、重症でないもの（それぞれ約97%、約95%）より低い。重症例の1年生存率は1979〜1993年の約67%から1994〜2005年の約83%に改善した。
    condition:
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-257
    source: Centers for Disease Control and Prevention. Data and Statistics on Congenital Heart Defects. 2026年10月14日確認版
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/heart-defects/data/index.html
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: CDC が引用した研究（Oster 2013 など）の数値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-02-05-005 (id: JlAKpeg)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-002
  domain: CH
  subdomain: 先天性心疾患
  assertion:
    plain_statement_ja: 日本では先天性心疾患が出生の約1%（年約1万300人）に生じ、その約95%が成人に達する。成人の先天性心疾患の患者数は1997年ごろに小児とほぼ同数となり、2012年の推計では約45万人で、年4〜5%ずつ増えている。
    condition:
      guideline: JCS 成人先天性心疾患診療ガイドライン（2017年改訂版）（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-272
    source: 日本循環器学会ほか合同ガイドライン. 成人先天性心疾患診療ガイドライン（2017年改訂版）（班長：市田蕗子）. 2018年3月23日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_ichida_h.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 推計はガイドラインが引用した研究による（二次資料経由）。2025年改訂版が公表されており、新しい推計は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-003
  domain: CH
  subdomain: 先天性心疾患
  assertion:
    plain_statement_ja: Eisenmenger 症候群の患者では妊娠は禁忌である。ヘモグロビンやヘマトクリットを目標値に保つための予防的な瀉血は行わず、ヘマトクリット65%超で過粘稠の症状が続く場合に限って行う。抗凝固療法は生存の改善が示されておらず、心房性不整脈や再発性の血栓塞栓症がある場合に限って考える。
    condition:
      guideline: JCS 成人先天性心疾患診療ガイドライン（2017年改訂版）（日本語版）
      region: 日本
    differential: null
    common_misconception: チアノーゼ性心疾患の赤血球増加には定期的な瀉血が必要である
  provenance:
    source_ref: SRC-272
    source: 日本循環器学会ほか合同ガイドライン. 成人先天性心疾患診療ガイドライン（2017年改訂版）（班長：市田蕗子）. 2018年3月23日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_ichida_h.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2025年改訂版での変更は未確認。日本語版で確認した。英語版での該当箇所は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-186 (id: Jlvnlu8)；TBL-01-00-185 (id: Jlvnlu4)；TBL-01-00-187 (id: JlvnlvE)'
    kokushi: 医学各論 Ⅴ-3-A-②（心室中隔欠損症、a）；医学各論 Ⅴ-3-A-①（心房中隔欠損症、a）；医学各論 Ⅴ-3-A-③（動脈管開存症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-004
  domain: CH
  subdomain: 先天性心疾患
  assertion:
    plain_statement_ja: 日本の調査では、成人のチアノーゼ性先天性心疾患で、喀血16%、痛風9%、脳梗塞8%、慢性腎不全7%、過粘稠症候群6%、脳膿瘍4%、感染性心内膜炎4%などの全身合併症がみられた。SpO2 85%の患者ではヘモグロビン20 g/dL程度が必要で、14 g/dL では鉄欠乏を疑う。
    condition:
      guideline: JCS 成人先天性心疾患診療ガイドライン（2017年改訂版）（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-272
    source: 日本循環器学会ほか合同ガイドライン. 成人先天性心疾患診療ガイドライン（2017年改訂版）（班長：市田蕗子）. 2018年3月23日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_ichida_h.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: null
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-005
  domain: CH
  subdomain: 単心房、単心室
  assertion:
    plain_statement_ja: Fontan 手術後の10年生存率はおおむね80%を超えるが、心不全の有病率は術後早期の10〜20%から成人期には約50%に増える。原因には心室機能の低下、肺血管抵抗の上昇による前負荷の不足、蛋白漏出性胃腸症、肝うっ血、心房性不整脈、洞不全などがある。
    condition:
      guideline: JCS 成人先天性心疾患診療ガイドライン（2017年改訂版）（日本語版）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-272
    source: 日本循環器学会ほか合同ガイドライン. 成人先天性心疾患診療ガイドライン（2017年改訂版）（班長：市田蕗子）. 2018年3月23日発行（日本語版）
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/~jscvs/wordpress/wp-content/uploads/2020/06/JCS2017_ichida_h.pdf
    source_license: 「無断転載を禁ずる」の表示。CC の表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: CH-018（指定難病の資料の Fontan 術後症候群）
  uncertainty: 数値はガイドラインが引用した研究による（二次資料経由）。2025年改訂版での変更は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-3-C-⑦（単心房、単心室、c）；医学各論 Ⅴ-3-B-②（三尖弁閉鎖症、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-006
  domain: CH
  subdomain: 心房中隔欠損症
  assertion:
    plain_statement_ja: 心房中隔欠損症（ASD）は米国で出生1万あたり約13人（年約5,240人）にみられる。多くは症状がなく、成人になってから心雑音をきっかけにみつかることも多い。治療しないと肺血流の増加で肺血管が傷み、成人期に肺高血圧、心不全、不整脈、脳卒中のリスクが高まる。閉鎖はカテーテル治療か開心術で行い、閉鎖後も定期的な経過観察が必要である。
    condition:
      region: 米国
    differential: null
    common_misconception: 小児期にみつからなかった ASD は成人で問題にならない
  provenance:
    source_ref: SRC-258
    source: Centers for Disease Control and Prevention. Atrial Septal Defect (ASD). 2025年12月15日確認版
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/heart-defects/about/atrial-septal-defect.html
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 頻度は CDC が引用したアトランタの研究（1998〜2005年）による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-185 (id: Jlvnlu4)'
    kokushi: 医学各論 Ⅴ-3-A-①（心房中隔欠損症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-007
  domain: CH
  subdomain: 心室中隔欠損症
  assertion:
    plain_statement_ja: 心室中隔欠損症（VSD）は米国で出生1万あたり約42人（年約16,800人）にみられる。小さい欠損は症状がなく自然に閉じることが多いが、大きい欠損では多呼吸、発汗、哺乳時の疲れ、体重増加不良がみられ、修復しなければ心不全、肺高血圧、不整脈、脳卒中を起こしうる。大きい欠損や閉じない欠損はカテーテル治療か開心術で閉鎖する。
    condition:
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-259
    source: Centers for Disease Control and Prevention. Ventricular Septal Defect. 2025年12月15日確認版
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/heart-defects/about/ventricular-septal-defect.html
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 頻度は CDC が引用したアトランタの研究（1998〜2005年）による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-186 (id: Jlvnlu8)'
    kokushi: 医学各論 Ⅴ-3-A-②（心室中隔欠損症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-008
  domain: CH
  subdomain: 房室中隔欠損症<心内膜床欠損症>
  assertion:
    plain_statement_ja: 完全型の房室中隔欠損症では、心臓の中央に大きな欠損があり、三尖弁と僧帽弁に分かれない共通の房室弁が1つある。不完全型では2つの弁があるが僧帽弁の逆流を伴いやすく、乳児期に症状がなく診断が遅れることがある。Down 症候群に多いため、Down 症候群の乳児には全例で心エコーを行う。ほぼ全例で、肺に不可逆的な障害が起こる前の手術が必要で、術後に最も多い合併症は僧帽弁の逆流である。米国では約1,587人に1人（年約2,256人）にみられる。
    condition:
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-260
    source: Centers for Disease Control and Prevention. Atrioventricular Septal Defect (AVSD). 2026年1月9日確認版
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/heart-defects/about/atrioventricular-septal-defect.html
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 頻度の出典はページに明記がない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-3-A-④（房室中隔欠損症<心内膜床欠損症>、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-009
  domain: CH
  subdomain: Fallot四徴症
  assertion:
    plain_statement_ja: Fallot 四徴症は、心室中隔欠損、肺動脈弁と主肺動脈の狭窄、心室中隔欠損に騎乗する大動脈、右室肥大の4つからなる。出生時にはチアノーゼが目立たなくても、泣いたり哺乳したりするときに急にチアノーゼが強まる発作（低酸素発作）を起こすことがある。手術では肺動脈弁と右室流出路を広げ、欠損孔をパッチで閉じる。米国では約2,041人に1人（年約1,754人）にみられる。
    condition:
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-261
    source: Centers for Disease Control and Prevention. Tetralogy of Fallot. 2026年1月9日確認版
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/heart-defects/about/tetralogy-of-fallot.html
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 頻度は CDC が引用した2016〜2020年の全国推計による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-188 (id: JlvnlvM)'
    kokushi: 医学各論 Ⅴ-3-B-①（Fallot四徴症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-010
  domain: CH
  subdomain: Fallot四徴症
  assertion:
    plain_statement_ja: Fallot 四徴症の15〜20%は22q11.2欠失症候群を合併し、心室中隔欠損を伴う肺動脈閉鎖症では約30%が合併する。22q11.2欠失症候群の心疾患には TBX1 遺伝子の欠失が関与すると考えられている。Fallot 四徴症の約2%は肺動脈弁欠損を伴い、出生前から肺動脈が著しく拡大する。
    condition:
      region: 日本
      framework: 指定難病214・215（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-266
    source: 厚生労働省. 指定難病 214 心室中隔欠損を伴う肺動脈閉鎖症・215 ファロー四徴症（ファロー四徴症類縁疾患）概要、診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001174442.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-188 (id: JlvnlvM)'
    kokushi: 医学各論 Ⅴ-3-B-①（Fallot四徴症、b）；医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-011
  domain: CH
  subdomain: Fallot四徴症
  assertion:
    plain_statement_ja: 肺動脈狭窄が高度な Fallot 四徴症では、新生児期〜乳児期前半に Blalock-Taussig（BT）シャントで肺血流を増やし、1歳前後に心内修復術（心室中隔欠損の閉鎖と右室流出路の拡大、または Rastelli 手術）を行う。心室中隔欠損を伴う肺動脈閉鎖症では、出生直後からプロスタグランジンE1製剤で動脈管を開いたままにし、動脈管を閉じさせる酸素投与は行わない。
    condition:
      region: 日本
      framework: 指定難病214・215（難病法）
    differential: null
    common_misconception: チアノーゼのある新生児には常に酸素を投与する
  provenance:
    source_ref: SRC-266
    source: 厚生労働省. 指定難病 214 心室中隔欠損を伴う肺動脈閉鎖症・215 ファロー四徴症（ファロー四徴症類縁疾患）概要、診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001174442.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-188 (id: JlvnlvM)；TBL-01-00-187 (id: JlvnlvE)'
    kokushi: 医学各論 Ⅴ-3-B-①（Fallot四徴症、b）；医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-012
  domain: CH
  subdomain: Fallot四徴症
  assertion:
    plain_statement_ja: Fallot 四徴症の修復後の遠隔期には、肺動脈弁の狭窄や閉鎖不全による右室の拡大と機能低下、二次性の三尖弁閉鎖不全、心房性・心室性不整脈が問題となる。右室の機能が不可逆になる前に、心臓MRIの右室容積を指標として右室流出路を再建する（一部は経カテーテル肺動脈弁置換を選ぶ）。典型例の術後30年生存率は98%と報告されている。
    condition:
      region: 日本
      framework: 指定難病215（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-266
    source: 厚生労働省. 指定難病 214 心室中隔欠損を伴う肺動脈閉鎖症・215 ファロー四徴症（ファロー四徴症類縁疾患）概要、診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001174442.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: CH-013（右室容積の目安）
  uncertainty: 30年生存率は資料が引用した報告による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-188 (id: JlvnlvM)；TBL-02-05-029 (id: JlAKpgA)'
    kokushi: 医学各論 Ⅴ-3-B-①（Fallot四徴症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-013
  domain: CH
  subdomain: Fallot四徴症
  assertion:
    plain_statement_ja: 心臓MRIで肺動脈弁逆流の逆流率が40%を超えると重症とされる。Fallot 四徴症の修復後で、重症の肺動脈弁逆流と高度の右室拡大（右室拡張末期容積係数160 mL/m²超、または収縮末期容積係数82 mL/m²超）がある例では、肺動脈弁置換後も右室のリバースリモデリングが起こりにくい。微量の肺動脈弁逆流は健常者の最大75%にみられる。
    condition:
      guideline: 英国心エコー図学会（BSE）三尖弁・肺動脈弁の心エコー評価ガイドライン 2020
      region: 英国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-234
    source: 'Zaidi A, Oxborough D, Augustine DX, et al. Echocardiographic assessment of the tricuspid and pulmonary valves: a practical guideline from the British Society of Echocardiography. Echo Res Pract 2020;7:G95-G122'
    doi: 10.1530/ERP-20-0033
    pmid: null
    pmcid: null
    url: https://doi.org/10.1530/ERP-20-0033
    source_license: CC BY-NC-ND 4.0（リポジトリの表示。著者最終稿）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 著者最終稿で確認した。刊行版の表記は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-188 (id: JlvnlvM)；TBL-02-05-029 (id: JlAKpgA)'
    kokushi: 医学各論 Ⅴ-3-B-①（Fallot四徴症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-014
  domain: CH
  subdomain: 完全大血管転位症
  assertion:
    plain_statement_ja: 完全大血管転位症では、心房と心室のつながりは正常だが、大動脈が右室から、肺動脈が左室から出る。心室中隔欠損がないI型（約50%）、あるII型（約30%）、心室中隔欠損と肺動脈狭窄を伴うIII型（約20%）に分けられ、日本の先天性心疾患の約2%を占め、男女比は2:1である。出生直後は卵円孔と動脈管の開存が生存に欠かせず、I型では生直後から強いチアノーゼがみられる。
    condition:
      region: 日本
      framework: 指定難病209（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-267
    source: 厚生労働省. 指定難病 209 完全大血管転位症 概要、診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001174440.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-02-05-005 (id: JlAKpeg)'
    kokushi: 医学各論 Ⅴ-3-C-②（完全大血管転位症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-015
  domain: CH
  subdomain: 完全大血管転位症
  assertion:
    plain_statement_ja: 完全大血管転位症では、プロスタグランジンE1で動脈管を開いたままにし、卵円孔が小さく低酸素血症が強ければバルーン心房中隔裂開術（BAS）を行う。I型は生後約1週、II型は生後約2週に動脈スイッチ手術（Jatene 手術）を行い、III型は新生児期後期の BT シャントのあと1歳前後に Rastelli 手術を行う。動脈スイッチ手術後の遠隔期生存率は90%以上で、術後の合併症に肺動脈狭窄、大動脈弁閉鎖不全（有意な逆流は約3%）、冠動脈狭窄がある。
    condition:
      region: 日本
      framework: 指定難病209（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-267
    source: 厚生労働省. 指定難病 209 完全大血管転位症 概要、診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001174440.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 心房内血流転換術（Mustard・Senning 手術）は、特殊な場合を除き現在は単独では行われないとされる
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-187 (id: JlvnlvE)；TBL-02-05-030 (id: JlAKpgE)'
    kokushi: 医学各論 Ⅴ-3-C-②（完全大血管転位症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-016
  domain: CH
  subdomain: 修正大血管転位症
  assertion:
    plain_statement_ja: 修正大血管転位症は、心房と心室、心室と大血管の両方が入れ違っているため血流の向きは正常だが、解剖学的右室が体循環を担う。約90%に合併異常があり、心室中隔欠損60〜80%、左室流出路・肺動脈狭窄30〜50%、Ebstein 様の三尖弁異形成15〜20%である。刺激伝導系の異常が約60%にみられ、年2%の割合で完全房室ブロックに移行し、成人期以降は三尖弁閉鎖不全と右心不全が進む。
    condition:
      region: 日本
      framework: 指定難病208（難病法）
    differential: null
    common_misconception: 血流の向きが正常なので修正大血管転位症は治療を要さない
  provenance:
    source_ref: SRC-268
    source: 厚生労働省. 指定難病 208 修正大血管転位症 概要、診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001174439.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-165 (id: Jlvnlsc)'
    kokushi: 医学各論 Ⅴ-3-C-⑤（修正大血管転位症、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-017
  domain: CH
  subdomain: 単心房、単心室
  assertion:
    plain_statement_ja: 単心室症、左心低形成症候群、三尖弁閉鎖症、心室中隔欠損を伴わない肺動脈閉鎖症は、体循環と肺循環を実質的に1つの心室が担う単心室循環の疾患群で、多くは段階的に手術する。新生児〜乳児期に、肺血流が少なければ BT シャント、多ければ肺動脈絞扼術を行い、乳児期中期に両方向性 Glenn 手術、1〜2歳で上下大静脈の血液が心室を通らずに肺動脈へ流れる Fontan 型手術を行う。
    condition:
      region: 日本
      framework: 指定難病210〜213（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-269
    source: 厚生労働省. 指定難病 210〜213 単心室症・左心低形成症候群・三尖弁閉鎖症・心室中隔欠損を伴わない肺動脈閉鎖症（単心室循環症候群）概要、診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001174441.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-3-C-⑦（単心房、単心室、c）；医学各論 Ⅴ-3-B-②（三尖弁閉鎖症、c）；医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-018
  domain: CH
  subdomain: 単心房、単心室
  assertion:
    plain_statement_ja: Fontan 循環は長期的には破綻しやすく、Fontan 術後症候群として難治性不整脈、肝線維化・肝硬変、蛋白漏出性胃腸症、鋳型気管支炎、血栓塞栓症などが起こる。体心室が解剖学的左室の疾患（左室型単心室、三尖弁閉鎖症）は比較的予後がよいが、解剖学的右室が体心室の疾患（左心低形成症候群など）は予後が悪い。心室中隔欠損を伴わない肺動脈閉鎖症では、右室と冠動脈の類洞交通による心筋虚血で突然死することがある。
    condition:
      region: 日本
      framework: 指定難病210〜213（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-269
    source: 厚生労働省. 指定難病 210〜213 単心室症・左心低形成症候群・三尖弁閉鎖症・心室中隔欠損を伴わない肺動脈閉鎖症（単心室循環症候群）概要、診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001174441.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: CH-005（Fontan 術後の心不全）
  uncertainty: Fontan 型手術後の患者で40歳以上は少なく、50歳を超えて生存するのは困難とされる
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-3-C-⑦（単心房、単心室、c）；医学各論 Ⅴ-3-B-②（三尖弁閉鎖症、c）；医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-019
  domain: CH
  subdomain: 両大血管右室起始症
  assertion:
    plain_statement_ja: 両大血管右室起始症は、一方の大血管が完全に、もう一方も50%以上が右室から起始するもので、心室中隔欠損の位置（大動脈弁下、肺動脈弁下、両大血管下、遠隔）で分類される。肺動脈狭窄がなければ肺血流の増加による心不全、肺動脈狭窄があれば Fallot 四徴症に似たチアノーゼ、大血管転位型ではチアノーゼと心不全が混在し、解剖に応じて心内修復術、動脈スイッチ手術、Rastelli 手術、Fontan 型手術を選ぶ。
    condition:
      region: 日本
      framework: 指定難病216（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-270
    source: 厚生労働省. 指定難病 216 両大血管右室起始症 概要、診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001174443.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-3-C-⑥（両大血管右室起始症、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-020
  domain: CH
  subdomain: Ebstein奇形
  assertion:
    plain_statement_ja: Ebstein 奇形（エプスタイン病）は、心エコーで、三尖弁中隔尖の付着部が僧帽弁の付着部より心尖方向へ8 mm/m²以上ずれていること、右房化右室、三尖弁逆流のすべてを確認して診断する。指定難病の調査票では、合併しうる WPW 症候群や上室頻拍、治療として三尖弁形成術（Cone 手術など）、弁置換術、Glenn 手術・Fontan 型手術、カテーテルアブレーションがあげられている。
    condition:
      region: 日本
      framework: 指定難病217（難病法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-271
    source: 厚生労働省. 指定難病 217 エプスタイン病 臨床調査個人票
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001210443.pdf
    source_license: 政府標準利用規約（厚生労働省ホームページ）
    legal_basis: B
    source_class: GOV_JP
    corroboration: VD-022（一次性三尖弁閉鎖不全の原因としての Ebstein 奇形）
  uncertainty: 概要・診断基準の文書ではなく臨床調査個人票（記入様式）で確認した。頻度と予後は未確認
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-3-C-①（Ebstein奇形、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-021
  domain: CH
  subdomain: 大動脈縮窄症、大動脈離断症
  assertion:
    plain_statement_ja: 大動脈縮窄症では、頭部と上肢の血圧・脈拍は正常か高い一方で、下肢では血圧が低く脈が弱い。年長児や成人では上肢の高血圧でみつかることが多い。新生児のパルスオキシメトリ検診では見逃されやすく、症状が出たら年齢にかかわらず狭窄部を広げる（バルーン拡張、ステント、切除と再建の手術）。術後も高血圧が続くことが多く、生涯の経過観察が必要である。米国では約1,724人に1人（年約2,060人）にみられる。
    condition:
      region: 米国
    differential: null
    common_misconception: 大動脈縮窄症は新生児のパルスオキシメトリ検診で必ずみつかる
  provenance:
    source_ref: SRC-262
    source: Centers for Disease Control and Prevention. Coarctation of the Aorta. 2026年1月9日確認版
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/heart-defects/about/coarctation-of-the-aorta.html
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 頻度の出典はページに明記がない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
    kokushi: 医学各論 Ⅴ-3-C-③（大動脈縮窄症、大動脈離断症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-022
  domain: CH
  subdomain: 総肺静脈還流異常症
  assertion:
    plain_statement_ja: 総肺静脈還流異常症では、肺静脈が左房につながらず、異常な経路（心上部型、心臓型、心下部型）で右心系に戻るため、心房中隔欠損を通って混合血が左心系に流れる。多くは出生直後からチアノーゼや呼吸障害を示し、手術で肺静脈を左房につなぎ直して異常な接続と心房中隔欠損を閉じる。米国では約6,667人に1人（年約540人）にみられる。
    condition:
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-263
    source: Centers for Disease Control and Prevention. Total Anomalous Pulmonary Venous Return (TAPVR). 2026年1月9日確認版
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/heart-defects/about/tapvr.html
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 頻度は CDC が引用した2016〜2020年の全国推計による（二次資料経由）。肺静脈狭窄などの遠隔期合併症はページに記載がない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-3-C-④（総肺静脈還流異常症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-023
  domain: CH
  subdomain: 先天性心疾患
  assertion:
    plain_statement_ja: 新生児の重症先天性心疾患のパルスオキシメトリ検診は生後24時間以降（それより前に退院する場合はできるだけ遅く）に行い、主な対象は左心低形成症候群、肺動脈閉鎖症、Fallot 四徴症、総肺静脈還流異常症、大血管転位症、三尖弁閉鎖症、総動脈幹症の7つである。検診が正常でも重症心疾患は否定できない。米国では検診の義務化が、重症先天性心疾患による乳児早期の死亡の33%減少（年約120人）と関連している。
    condition:
      region: 米国
    differential: null
    common_misconception: パルスオキシメトリ検診が正常なら重症の先天性心疾患は否定できる
  provenance:
    source_ref: SRC-264
    source: Centers for Disease Control and Prevention. Screening for Critical Congenital Heart Defects. 2026年10月14日確認版
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/heart-defects/screening/index.html
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: SpO2 の判定基準の数値はページに記載がない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；PS-02-06-03 (id: JkxnuQo)'
    kokushi: 医学各論 Ⅴ-3-C-②（完全大血管転位症、b）；医学各論 Ⅴ-3-C-④（総肺静脈還流異常症、b）；医学各論 Ⅴ-3-B-①（Fallot四徴症、b）；医学各論 Ⅴ-3-B-②（三尖弁閉鎖症、c）；医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-024
  domain: CH
  subdomain: 動脈管開存症
  assertion:
    plain_statement_ja: 動脈管開存症は、大動脈と肺動脈をつなぐ動脈管が生後に閉じずに残るもので、頻度の高い単純な先天性心疾患の1つであり、小さいものは自然に閉じることがある。
    condition:
      region: 米国（NHLBI の一般向け解説）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-265
    source: 'National Heart, Lung, and Blood Institute. Congenital Heart Defects: Types. 2022年3月24日更新'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.nhlbi.nih.gov/health/congenital-heart-defects/types
    source_license: 米国連邦政府の著作物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 早産児での頻度と治療（薬物・カテーテル・手術）はページに記載がない
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-187 (id: JlvnlvE)；TBL-02-05-005 (id: JlAKpeg)'
    kokushi: 医学各論 Ⅴ-3-A-③（動脈管開存症、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: CH-025
  domain: CH
  subdomain: 先天性心疾患
  assertion:
    plain_statement_ja: 日本胸部外科学会の2021年の集計では、先天性心疾患の手術は8,349件（うち開心術6,510件）で、院内死亡率は全体で1.7%、新生児では7.1%だった。病変別の院内死亡率は、Fallot 四徴症0.5%、完全型房室中隔欠損症2.0%、心室中隔欠損症1.7%、Fontan 型手術（385件）0.8%だった。
    condition:
      region: 日本
      period: 2021年の手術件数
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-240
    source: 'Committee for Scientific Affairs, The Japanese Association for Thoracic Surgery; Yoshimura N, Sato Y, et al. Thoracic and cardiovascular surgeries in Japan during 2021: Annual report by the Japanese Association for Thoracic Surgery. Gen Thorac Cardiovasc Surg 2024;72:254-291'
    doi: 10.1007/s11748-023-01997-6
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s11748-023-01997-6
    source_license: CC BY 4.0（Springer の論文ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；PS-02-06-04 (id: JkxnuQs)'
    kokushi: 医学各論 Ⅴ-3-B-①（Fallot四徴症、b）；医学各論 Ⅴ-3-A-④（房室中隔欠損症<心内膜床欠損症>、c）；医学各論 Ⅴ-3-A-②（心室中隔欠損症、a）；医学各論 Ⅴ-3-C-⑦（単心房、単心室、c）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応

| ID | subdomain | 出典 | 出題基準 | コアカリ |
|---|---|---|---|---|
| VD-001 | 僧帽弁閉鎖不全症 | SRC-230 | 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg) |
| VD-002 | 僧帽弁閉鎖不全症 | SRC-230 | 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)；TBL-02-05-027 (id: JlAKpf4) |
| VD-003 | 僧帽弁閉鎖不全症 | SRC-230 | 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg) |
| VD-004 | 僧帽弁閉鎖不全症 | SRC-230 | 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg) |
| VD-005 | 大動脈弁狭窄症 | SRC-230 | 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts) |
| VD-006 | 大動脈弁狭窄症 | SRC-230 | 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；PS-02-06-04 (id: JkxnuQs) |
| VD-007 | 大動脈弁狭窄症 | SRC-231 | 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；TBL-02-05-027 (id: JlAKpf4) |
| VD-008 | 大動脈弁狭窄症 | SRC-231 | 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；TBL-02-05-017 (id: JlAKpfo)；TBL-02-05-021 (id: JlAKpfI)；TBL-02-05-020 (id: JlAKpfU) |
| VD-009 | 大動脈弁狭窄症 | SRC-231 | 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；TBL-02-05-027 (id: JlAKpf4)；TBL-02-05-029 (id: JlAKpgA) |
| VD-010 | 感染性心内膜炎 | SRC-231 | 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug) |
| VD-011 | リウマチ性心炎 | SRC-231 | 医学各論 Ⅴ-4-C-④（リウマチ性心炎、c） | PS-02-06-05 (id: JkxnuQw)；PS-02-06-04 (id: JkxnuQs) |
| VD-012 | 僧帽弁狭窄症 | SRC-231 | 医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)；TBL-01-00-166 (id: Jlvnlsg) |
| VD-013 | 弁膜症 | SRC-231 | 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）；医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；PS-02-06-04 (id: JkxnuQs) |
| VD-014 | 僧帽弁狭窄症 | SRC-231 | 医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)；TBL-02-05-027 (id: JlAKpf4) |
| VD-015 | 大動脈弁狭窄症 | SRC-238 | 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；PS-02-06-04 (id: JkxnuQs) |
| VD-016 | 僧帽弁狭窄症 | SRC-239 | 医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)；TBL-01-00-166 (id: Jlvnlsg) |
| VD-017 | 弁膜症 | SRC-240 | 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）；医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a） | PS-02-06-05 (id: JkxnuQw)；PS-02-06-04 (id: JkxnuQs) |
| VD-018 | 大動脈弁閉鎖不全症 | SRC-232 | 医学各論 Ⅴ-4-B-②（大動脈弁閉鎖不全症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；TBL-02-05-027 (id: JlAKpf4) |
| VD-019 | 大動脈弁閉鎖不全症 | SRC-232 | 医学各論 Ⅴ-4-B-②（大動脈弁閉鎖不全症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts)；TBL-02-05-027 (id: JlAKpf4) |
| VD-020 | 大動脈弁閉鎖不全症 | SRC-232 | 医学各論 Ⅴ-4-B-②（大動脈弁閉鎖不全症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-176 (id: Jlvnlts) |
| VD-021 | 僧帽弁閉鎖不全症 | SRC-233 | 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a）；医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-175 (id: Jlvnltg)；TBL-02-05-027 (id: JlAKpf4) |
| VD-022 | 三尖弁閉鎖不全症 | SRC-234 | 医学各論 Ⅴ-4-C-①（三尖弁閉鎖不全症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-177 (id: Jlvnlt4) |
| VD-023 | 三尖弁閉鎖不全症 | SRC-234 | 医学各論 Ⅴ-4-C-①（三尖弁閉鎖不全症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-177 (id: Jlvnlt4)；TBL-02-05-027 (id: JlAKpf4)；TBL-02-05-029 (id: JlAKpgA) |
| VD-024 | リウマチ性心炎 | SRC-235 | 医学各論 Ⅴ-4-C-④（リウマチ性心炎、c） | PS-02-06-05 (id: JkxnuQw)；PS-02-06-02 (id: JkxnuQk) |
| VD-025 | リウマチ性心炎 | SRC-235 | 医学各論 Ⅴ-4-C-④（リウマチ性心炎、c） | PS-02-06-05 (id: JkxnuQw)；TBL-02-05-027 (id: JlAKpf4) |
| VD-026 | 弁膜症 | SRC-236 | 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a）；医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a） | PS-02-06-05 (id: JkxnuQw)；PS-02-06-04 (id: JkxnuQs) |
| VD-027 | 感染性心内膜炎 | SRC-237 | 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug) |
| VD-028 | 感染性心内膜炎 | SRC-237 | 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug)；PS-02-06-03 (id: JkxnuQo) |
| VD-029 | 感染性心内膜炎 | SRC-237 | 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug)；TBL-02-05-027 (id: JlAKpf4) |
| VD-030 | 感染性心内膜炎 | SRC-237 | 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug) |
| VD-031 | 感染性心内膜炎 | SRC-237 | 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug)；PS-02-06-04 (id: JkxnuQs) |
| VD-032 | 感染性心内膜炎 | SRC-237 | 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-181 (id: Jlvnlug) |
| MP-001 | 肥大型心筋症 | SRC-241 | 医学各論 Ⅴ-6-B-①（肥大型心筋症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；TBL-02-05-027 (id: JlAKpf4) |
| MP-002 | 肥大型心筋症 | SRC-241 | 医学各論 Ⅴ-6-B-①（肥大型心筋症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；TBL-02-05-027 (id: JlAKpf4) |
| MP-003 | 肥大型心筋症 | SRC-241 | 医学各論 Ⅴ-6-B-①（肥大型心筋症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA) |
| MP-004 | 肥大型心筋症 | SRC-241 | 医学各論 Ⅴ-6-B-①（肥大型心筋症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA) |
| MP-005 | 肥大型心筋症 | SRC-241 | 医学各論 Ⅴ-6-B-①（肥大型心筋症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；TBL-02-05-029 (id: JlAKpgA)；TBL-02-05-017 (id: JlAKpfo) |
| MP-006 | 肥大型心筋症 | SRC-242 | 医学各論 Ⅴ-6-B-①（肥大型心筋症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；PS-02-06-04 (id: JkxnuQs) |
| MP-007 | 肥大型心筋症 | SRC-243 | 医学各論 Ⅴ-6-B-①（肥大型心筋症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；PS-02-06-04 (id: JkxnuQs) |
| MP-008 | 拡張型心筋症 | SRC-244 | 医学各論 Ⅴ-6-B-②（拡張型心筋症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA) |
| MP-009 | 拡張型心筋症 | SRC-244 | 医学各論 Ⅴ-6-B-②（拡張型心筋症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA)；PS-02-06-04 (id: JkxnuQs)；TBL-02-05-032 (id: JlAKpgM) |
| MP-010 | 拡張型心筋症 | SRC-244 | 医学各論 Ⅴ-6-B-②（拡張型心筋症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA) |
| MP-011 | 拘束型心筋症 | SRC-245 | 医学各論 Ⅴ-6-B-③（拘束型心筋症、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-178 (id: JlvnluA) |
| MP-012 | 心アミロイドーシス | SRC-246 | 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU) |
| MP-013 | 心アミロイドーシス | SRC-246 | 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU) |
| MP-014 | 心アミロイドーシス | SRC-246 | 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)；TBL-02-05-028 (id: JlAKpf8) |
| MP-015 | 心アミロイドーシス | SRC-246 | 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU) |
| MP-016 | 心アミロイドーシス | SRC-246 | 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)；PS-02-06-04 (id: JkxnuQs) |
| MP-017 | 心アミロイドーシス | SRC-247 | 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)；TBL-02-05-027 (id: JlAKpf4)；TBL-02-05-029 (id: JlAKpgA) |
| MP-018 | 心アミロイドーシス | SRC-247 | 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)；PS-02-06-04 (id: JkxnuQs) |
| MP-019 | 心サルコイドーシス | SRC-248 | 医学各論 Ⅴ-6-C-②（心サルコイドーシス、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU)；TBL-02-05-028 (id: JlAKpf8)；TBL-02-05-029 (id: JlAKpgA)；TBL-01-00-165 (id: Jlvnlsc) |
| MP-020 | 筋ジストロフィー | SRC-249 | 医学各論 Ⅴ-6-C-⑤（筋ジストロフィー、c） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-179 (id: JlvnluU) |
| MP-021 | ウイルス性心筋炎 | SRC-250 | 医学各論 Ⅴ-6-A-①（ウイルス性心筋炎、a）；医学各論 Ⅴ-6-D-①（急性心膜炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-180 (id: JlvnluY)；TBL-01-00-182 (id: Jlvnluk) |
| MP-022 | ウイルス性心筋炎 | SRC-251 | 医学各論 Ⅴ-6-A-①（ウイルス性心筋炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-180 (id: JlvnluY)；PS-02-06-04 (id: JkxnuQs) |
| MP-023 | 急性心膜炎 | SRC-252 | 医学各論 Ⅴ-6-D-①（急性心膜炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-182 (id: Jlvnluk)；TBL-02-05-021 (id: JlAKpfI) |
| MP-024 | 急性心膜炎 | SRC-252 | 医学各論 Ⅴ-6-D-①（急性心膜炎、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-182 (id: Jlvnluk)；PS-02-06-04 (id: JkxnuQs) |
| MP-025 | 心タンポナーデ | SRC-252 | 医学各論 Ⅴ-6-E（心タンポナーデ、a）；医学各論 Ⅴ-6-D-②（心囊液貯留、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-184 (id: Jlvnluw)；TBL-02-05-027 (id: JlAKpf4) |
| MP-026 | 収縮性心膜炎 | SRC-252 | 医学各論 Ⅴ-6-D-③（収縮性心膜炎、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-183 (id: Jlvnlus)；TBL-02-05-027 (id: JlAKpf4)；TBL-02-05-030 (id: JlAKpgE) |
| MP-027 | たこつぼ心筋症 | SRC-253 | 医学各論 Ⅴ-6-H-①（たこつぼ心筋症、b） | PS-02-06-05 (id: JkxnuQw) |
| MP-028 | たこつぼ心筋症 | SRC-253 | 医学各論 Ⅴ-6-H-①（たこつぼ心筋症、b） | PS-02-06-05 (id: JkxnuQw) |
| MP-029 | 心臓震盪 | SRC-254 | 医学各論 Ⅴ-6-H-②（心臓震盪、b）；医学各論 Ⅴ-1-B-③（心室細動、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-171 (id: JlvnltA) |
| MP-030 | 心臓震盪 | SRC-254 | 医学各論 Ⅴ-6-H-②（心臓震盪、b）；医学各論 Ⅴ-1-B-③（心室細動、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-171 (id: JlvnltA)；TBL-02-05-032 (id: JlAKpgM) |
| MP-031 | 粘液腫 | SRC-255 | 医学各論 Ⅴ-6-F-①（粘液腫、c） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-642 (id: JlvnmcA) |
| MP-032 | 粘液腫 | SRC-256 | 医学各論 Ⅴ-6-F-①（粘液腫、c） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-642 (id: JlvnmcA) |
| CH-001 | 先天性心疾患 | SRC-257 | null | PS-02-06-05 (id: JkxnuQw)；TBL-02-05-005 (id: JlAKpeg) |
| CH-002 | 先天性心疾患 | SRC-272 | null | PS-02-06-05 (id: JkxnuQw) |
| CH-003 | 先天性心疾患 | SRC-272 | 医学各論 Ⅴ-3-A-②（心室中隔欠損症、a）；医学各論 Ⅴ-3-A-①（心房中隔欠損症、a）；医学各論 Ⅴ-3-A-③（動脈管開存症、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-186 (id: Jlvnlu8)；TBL-01-00-185 (id: Jlvnlu4)；TBL-01-00-187 (id: JlvnlvE) |
| CH-004 | 先天性心疾患 | SRC-272 | null | PS-02-06-05 (id: JkxnuQw) |
| CH-005 | 単心房、単心室 | SRC-272 | 医学各論 Ⅴ-3-C-⑦（単心房、単心室、c）；医学各論 Ⅴ-3-B-②（三尖弁閉鎖症、c） | PS-02-06-05 (id: JkxnuQw) |
| CH-006 | 心房中隔欠損症 | SRC-258 | 医学各論 Ⅴ-3-A-①（心房中隔欠損症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-185 (id: Jlvnlu4) |
| CH-007 | 心室中隔欠損症 | SRC-259 | 医学各論 Ⅴ-3-A-②（心室中隔欠損症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-186 (id: Jlvnlu8) |
| CH-008 | 房室中隔欠損症<心内膜床欠損症> | SRC-260 | 医学各論 Ⅴ-3-A-④（房室中隔欠損症<心内膜床欠損症>、c） | PS-02-06-05 (id: JkxnuQw) |
| CH-009 | Fallot四徴症 | SRC-261 | 医学各論 Ⅴ-3-B-①（Fallot四徴症、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-188 (id: JlvnlvM) |
| CH-010 | Fallot四徴症 | SRC-266 | 医学各論 Ⅴ-3-B-①（Fallot四徴症、b）；医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-188 (id: JlvnlvM) |
| CH-011 | Fallot四徴症 | SRC-266 | 医学各論 Ⅴ-3-B-①（Fallot四徴症、b）；医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-188 (id: JlvnlvM)；TBL-01-00-187 (id: JlvnlvE) |
| CH-012 | Fallot四徴症 | SRC-266 | 医学各論 Ⅴ-3-B-①（Fallot四徴症、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-188 (id: JlvnlvM)；TBL-02-05-029 (id: JlAKpgA) |
| CH-013 | Fallot四徴症 | SRC-234 | 医学各論 Ⅴ-3-B-①（Fallot四徴症、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-188 (id: JlvnlvM)；TBL-02-05-029 (id: JlAKpgA) |
| CH-014 | 完全大血管転位症 | SRC-267 | 医学各論 Ⅴ-3-C-②（完全大血管転位症、b） | PS-02-06-05 (id: JkxnuQw)；TBL-02-05-005 (id: JlAKpeg) |
| CH-015 | 完全大血管転位症 | SRC-267 | 医学各論 Ⅴ-3-C-②（完全大血管転位症、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-187 (id: JlvnlvE)；TBL-02-05-030 (id: JlAKpgE) |
| CH-016 | 修正大血管転位症 | SRC-268 | 医学各論 Ⅴ-3-C-⑤（修正大血管転位症、c） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-165 (id: Jlvnlsc) |
| CH-017 | 単心房、単心室 | SRC-269 | 医学各論 Ⅴ-3-C-⑦（単心房、単心室、c）；医学各論 Ⅴ-3-B-②（三尖弁閉鎖症、c）；医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c） | PS-02-06-05 (id: JkxnuQw) |
| CH-018 | 単心房、単心室 | SRC-269 | 医学各論 Ⅴ-3-C-⑦（単心房、単心室、c）；医学各論 Ⅴ-3-B-②（三尖弁閉鎖症、c）；医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c） | PS-02-06-05 (id: JkxnuQw) |
| CH-019 | 両大血管右室起始症 | SRC-270 | 医学各論 Ⅴ-3-C-⑥（両大血管右室起始症、c） | PS-02-06-05 (id: JkxnuQw) |
| CH-020 | Ebstein奇形 | SRC-271 | 医学各論 Ⅴ-3-C-①（Ebstein奇形、b） | PS-02-06-05 (id: JkxnuQw)；TBL-02-05-027 (id: JlAKpf4) |
| CH-021 | 大動脈縮窄症、大動脈離断症 | SRC-262 | 医学各論 Ⅴ-3-C-③（大動脈縮窄症、大動脈離断症、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) |
| CH-022 | 総肺静脈還流異常症 | SRC-263 | 医学各論 Ⅴ-3-C-④（総肺静脈還流異常症、b） | PS-02-06-05 (id: JkxnuQw) |
| CH-023 | 先天性心疾患 | SRC-264 | 医学各論 Ⅴ-3-C-②（完全大血管転位症、b）；医学各論 Ⅴ-3-C-④（総肺静脈還流異常症、b）；医学各論 Ⅴ-3-B-①（Fallot四徴症、b）；医学各論 Ⅴ-3-B-②（三尖弁閉鎖症、c）；医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c） | PS-02-06-05 (id: JkxnuQw)；PS-02-06-03 (id: JkxnuQo) |
| CH-024 | 動脈管開存症 | SRC-265 | 医学各論 Ⅴ-3-A-③（動脈管開存症、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-187 (id: JlvnlvE)；TBL-02-05-005 (id: JlAKpeg) |
| CH-025 | 先天性心疾患 | SRC-240 | 医学各論 Ⅴ-3-B-①（Fallot四徴症、b）；医学各論 Ⅴ-3-A-④（房室中隔欠損症<心内膜床欠損症>、c）；医学各論 Ⅴ-3-A-②（心室中隔欠損症、a）；医学各論 Ⅴ-3-C-⑦（単心房、単心室、c） | PS-02-06-05 (id: JkxnuQw)；PS-02-06-04 (id: JkxnuQs) |

- 出題基準が null のカード：3件（CH-001, CH-002, CH-004）。いずれも先天性心疾患の総論・統計で、出題基準の表に対応する小項目がないものです。コアカリは全件に付けました。

出題基準の小項目ごとのカード数（第9回の範囲）：

| 出題基準 | カード数 |
|---|---|
| 医学各論 Ⅴ-4-A-①（僧帽弁狭窄症、a） | 6 |
| 医学各論 Ⅴ-4-A-②（僧帽弁閉鎖不全症、a） | 6 |
| 医学各論 Ⅴ-4-B-①（大動脈弁狭窄症、a） | 9 |
| 医学各論 Ⅴ-4-B-②（大動脈弁閉鎖不全症、a） | 3 |
| 医学各論 Ⅴ-4-C-①（三尖弁閉鎖不全症、a） | 2 |
| 医学各論 Ⅴ-4-C-②（感染性心内膜炎、a） | 7 |
| 医学各論 Ⅴ-4-C-③（連合弁膜症、b） | 0 |
| 医学各論 Ⅴ-4-C-④（リウマチ性心炎、c） | 3 |
| 医学各論 Ⅴ-6-A-①（ウイルス性心筋炎、a） | 2 |
| 医学各論 Ⅴ-6-B-①（肥大型心筋症、a） | 7 |
| 医学各論 Ⅴ-6-B-②（拡張型心筋症、a） | 3 |
| 医学各論 Ⅴ-6-B-③（拘束型心筋症、b） | 1 |
| 医学各論 Ⅴ-6-C-①（心アミロイドーシス、b） | 7 |
| 医学各論 Ⅴ-6-C-②（心サルコイドーシス、b） | 1 |
| 医学各論 Ⅴ-6-C-③（アルコール性心筋症、b） | 0 |
| 医学各論 Ⅴ-6-C-④（虚血性心筋症、b） | 0 |
| 医学各論 Ⅴ-6-C-⑤（筋ジストロフィー、c） | 1 |
| 医学各論 Ⅴ-6-D-①（急性心膜炎、a） | 3 |
| 医学各論 Ⅴ-6-D-②（心囊液貯留、a） | 1 |
| 医学各論 Ⅴ-6-D-③（収縮性心膜炎、b） | 1 |
| 医学各論 Ⅴ-6-E（心タンポナーデ、a） | 1 |
| 医学各論 Ⅴ-6-F-①（粘液腫、c） | 2 |
| 医学各論 Ⅴ-6-F-②（転移性腫瘍、c） | 0 |
| 医学各論 Ⅴ-6-G-①（心臓外傷、c） | 0 |
| 医学各論 Ⅴ-6-G-②（血管損傷、c） | 0 |
| 医学各論 Ⅴ-6-H-①（たこつぼ心筋症、b） | 2 |
| 医学各論 Ⅴ-6-H-②（心臓震盪、b） | 2 |
| 医学各論 Ⅴ-3-A-①（心房中隔欠損症、a） | 2 |
| 医学各論 Ⅴ-3-A-②（心室中隔欠損症、a） | 3 |
| 医学各論 Ⅴ-3-A-③（動脈管開存症、b） | 2 |
| 医学各論 Ⅴ-3-A-④（房室中隔欠損症<心内膜床欠損症>、c） | 2 |
| 医学各論 Ⅴ-3-B-①（Fallot四徴症、b） | 7 |
| 医学各論 Ⅴ-3-B-②（三尖弁閉鎖症、c） | 4 |
| 医学各論 Ⅴ-3-B-③（肺動脈閉鎖症、c） | 5 |
| 医学各論 Ⅴ-3-C-①（Ebstein奇形、b） | 1 |
| 医学各論 Ⅴ-3-C-②（完全大血管転位症、b） | 3 |
| 医学各論 Ⅴ-3-C-③（大動脈縮窄症、大動脈離断症、b） | 1 |
| 医学各論 Ⅴ-3-C-④（総肺静脈還流異常症、b） | 2 |
| 医学各論 Ⅴ-3-C-⑤（修正大血管転位症、c） | 1 |
| 医学各論 Ⅴ-3-C-⑥（両大血管右室起始症、c） | 1 |
| 医学各論 Ⅴ-3-C-⑦（単心房、単心室、c） | 4 |

カードのない小項目：医学各論 Ⅴ-4-C-③（連合弁膜症、b）、医学各論 Ⅴ-6-C-③（アルコール性心筋症、b）、医学各論 Ⅴ-6-C-④（虚血性心筋症、b）、医学各論 Ⅴ-6-F-②（転移性腫瘍、c）、医学各論 Ⅴ-6-G-①（心臓外傷、c）、医学各論 Ⅴ-6-G-②（血管損傷、c）（5-2 の補完候補を参照）

## 4. 未解決事項（担当の目安つき）

| # | 内容 | 対象 | 担当の目安 |
|---|---|---|---|
| 1 | 日本の学会ガイドラインは日本語版（DOI なし）を出典にした。英語版（Circulation Journal）にも同じ記載があるかを確認し、英語版を出典にする場合はカードを差し替える。J-STAGE で確認できた英語版は、弁膜症 GL 2020（DOI 10.1253/circj.CJ-20-0135、CC BY-NC-ND 4.0）だけ。 | SRC-230・237・241・246・272 を使う26件 | Claude Code（書誌）、専門医（内容） |
| 2 | 新しい版が出ている。JCS は感染性心内膜炎 GL の2026年改訂版、成人先天性心疾患 GL の2025年改訂版を公表済み。心膜疾患は ESC 2025 心筋炎・心膜炎 GL が出ている。JCS 2023 心筋炎 GL は本文を取得できなかった。新しい版で推奨や数値が変わっていないか確認する。 | VD-027〜032、CH-002〜005、MP-022〜026 | 専門医 |
| 3 | ライセンスが未確認：SRC-238・239・253（NEJM）、SRC-252（Acta Cardiol）、SRC-254（Sports Med、Open access だが CC の種類不明）、SRC-243（PMDA の利用規約）。SRC-233 は刊行版 PDF（CC BY-NC-ND）と Springer の現行ページ（CC BY）で表示が食い違う。 | 該当 SRC | Claude Code（Crossref） |
| 4 | PMID は SRC-238（30883058）と SRC-239（36036525）以外は null。PubMed・PMC・Crossref・Europe PMC はこの環境から取得できなかった。 | 全 SRC | Claude Code（NCBI API） |
| 5 | 数値の読み取りは取得ツールの抜き出しによる。とくに表から読んだ値（VD-002 の MR 重症度、VD-009 の低流量 AS、VD-018 の AR 重症度、MP-011 の RCM の目安、MP-019 の心サルコイドーシスの基準、CH-020 の Ebstein の 8 mm/m²）は原典の表と照合する。 | 全件（優先は左記） | Claude Code（照合）、専門医 |
| 6 | 「二次資料経由」と書いたカードは、ガイドラインや総説が引用した原著と照合する。 | VD-022・029・030、MP-003・004・011・013・015・023〜026・029・030、CH-001・002・004〜007・009・012・022 | Claude Code |
| 7 | 抜粋で確認できなかった点：VD-005 の超重症 AS の3項目の組み合わせ方、MP-005 の推奨クラスI・エビデンスレベルA の対象となる推奨文、MP-007 の承認日、MP-031 の研究の実施国。 | 該当カード | Claude Code（原典確認） |
| 8 | 出題基準の対応で判断が分かれうるもの：人工弁の抗凝固・弁の種類（VD-013・026）を大動脈弁狭窄症・僧帽弁狭窄症に、Eisenmenger 症候群（CH-003）を ASD・VSD・PDA に、新生児検診（CH-023）を対象疾患に対応させた。総論・統計の3件（CH-001・002・004）は対応する小項目がなく null。 | 該当カード | 専門医 |
| 9 | 日本の承認・保険適用で確認していないもの：ベンザチンペニシリンG筋注のリウマチ熱予防（VD-011）、コルヒチンの心膜炎（MP-024）、ピロリン酸シンチの現在の保険適用（MP-014）、ATTR に対するタファミジス以外の薬（MP-018）。 | 該当カード | 専門医 |

## 5. 次回への引き継ぎ

### 5-1. 欠番

- なし（VD-001〜032、MP-001〜032、CH-001〜025）。
- SRC-273〜289 は未使用。第9回の補完に使える。

### 5-2. 取得範囲外で作れなかった内容（補完ラウンドの候補）

- 弁膜症：AS の手術適応の推奨クラス（症候性重症 AS、無症候で LVEF 50%未満など）、TAVI と外科的弁置換を選ぶ年齢の目安（日本と欧米）、MS の重症度（弁口面積）と経皮的僧帽弁交連切開術の適応、AR の手術適応、連合弁膜症、EARLY TAVR・COAPT・TRILUMINATE などの試験（抄録を取得できず）、日本での TAVI・経皮的僧帽弁接合不全修復術の保険導入の経緯。
- 感染性心内膜炎：2026年改訂版の内容、Duke-ISCVID 基準（2023）、心不全・制御不能の感染による手術適応、起炎菌別の抗菌薬、高度・中等度リスク群の具体例と日本人での予防投与の用量。
- 心筋・心膜疾患：HCM の ICD の推奨と突然死リスクの評価法、閉塞性 HCM の薬物治療の推奨クラス、心筋炎（2023年改訂版の診断・心臓MRI・心筋生検・免疫抑制療法、巨細胞性心筋炎、免疫チェックポイント阻害薬・mRNA ワクチン関連）、再発性心膜炎、心タンポナーデの身体所見（奇脈など）、アルコール性心筋症、虚血性心筋症、転移性心臓腫瘍、心臓外傷・血管損傷、たこつぼ症候群の診断基準（InterTAK 診断基準）。
- 先天性心疾患：ASD の閉鎖適応（Qp/Qs、カテーテル閉鎖の条件）、PDA の治療（早産児の薬物治療、カテーテル閉鎖）、大動脈離断症、総動脈幹症、左心低形成症候群の Norwood 手術、成人先天性心疾患の妊娠・不整脈、学校心臓検診（2025年フォーカスアップデート）。

### 5-3. 重複を避ける範囲（第8回・第10回との境界）

- 弁膜症に伴う心房細動の抗凝固（VD-012・016）と機械弁の抗凝固（VD-013）は VD で扱った。AR（第8回）は非弁膜症性心房細動の抗凝固を扱う。
- 感染性心内膜炎の予防投与（VD-010・032）は VD で扱った。
- 上行大動脈径の紹介基準（VD-019）は AR の文脈に限る。大動脈瘤・Marfan 症候群の手術適応は VS（第10回）で扱う。
- 大動脈縮窄症の高血圧（CH-021）は CH で扱った。HT（第10回）の二次性高血圧では重ねない。
- たこつぼ症候群（MP-027・028）は MP。IH（第8回）の急性冠症候群の鑑別では重ねない。
- 心臓震盪（MP-029・030）は MP。AR（第8回）の心室細動・突然死の予防では重ねない。
- DCM の心不全治療薬（MP-009）は指定難病の資料の範囲に限った。心不全の薬物治療の推奨は HF（第8回）で扱う。
- 弁膜症の心エコーの重症度指標（VD-002・007〜009・018・023）とピロリン酸シンチ（MP-014）は扱った。CX（第10回）の心エコー・核医学の基本では重ねない。
- 川崎病は IH（第8回）。肺血栓塞栓症は呼吸器（Ⅳ）。

### 5-4. 扱った出典（SRC-230〜272）

- 日本の学会ガイドライン（日本語版）：弁膜症 2020（SRC-230）、感染性心内膜炎 2017（SRC-237）、心筋症 2018（SRC-241）、心アミロイドーシス 2020（SRC-246）、成人先天性心疾患 2017（SRC-272）。
- 厚生労働省 指定難病の資料：肥大型心筋症（SRC-242）、拡張型心筋症（SRC-244）、拘束型心筋症（SRC-245）、全身性アミロイドーシス（SRC-247）、サルコイドーシス（SRC-248）、筋ジストロフィー（SRC-249）、ファロー四徴症類縁疾患（SRC-266）、完全大血管転位症（SRC-267）、修正大血管転位症（SRC-268）、単心室循環症候群（SRC-269）、両大血管右室起始症（SRC-270）、エプスタイン病の臨床調査個人票（SRC-271）。
- 海外ガイドライン：ACC/AHA 2020 弁膜症（SRC-231）、BSE の大動脈弁閉鎖不全症 2025（SRC-232）・僧帽弁 2021（SRC-233）・三尖弁と肺動脈弁 2020（SRC-234）、ESC 2015 心膜疾患の要約（SRC-252）。
- 米国政府資料：CDC（SRC-235・257〜264）、NHLBI（SRC-236・250・265）、MedlinePlus Genetics（SRC-256）。
- 原著・総説・報告：PARTNER 3（SRC-238）、INVICTUS（SRC-239）、日本胸部外科学会 2021年報（SRC-240）、PMDA 審査報告書（SRC-243）、劇症型心筋炎の全国調査（SRC-251）、InterTAK 登録（SRC-253）、心臓震盪の総説（SRC-254）、心臓粘液腫の手術例（SRC-255）。

### 5-5. この環境での取得の可否（次の調査チャットへのメモ）

- 取得できた：厚生労働省・PMDA の PDF、CDC・NHLBI・MedlinePlus のページ、日本心臓血管外科学会が UMIN で公開する JCS ガイドライン PDF、日本循環器学会のサイトの一部の PDF、J-STAGE の論文ページ（抄録・ライセンス表示）、Springer・Frontiers の論文ページ、大学の研究者データベースとリポジトリ。
- 取得できなかった：J-STAGE の PDF（robots で拒否）、PubMed・PMC（ボット確認）、Crossref API、Europe PMC、NEJM・OUP・ahajournals の本文。
- 長い PDF は前半しか読めない。JCS ガイドラインの後半（治療の章）は、ブラウザを使える環境か、PC で PDF を開いて確認する必要がある。
