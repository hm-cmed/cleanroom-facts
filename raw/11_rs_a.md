# 第11回 呼吸器（RI・RO）

- 作成日：2026-10-28
- 事実票：89件（RI-001〜RI-053（53件）、RO-001〜RO-036（36件））。欠番なし。全件 `status: draft`、`verifier: null`
- 取り込み：`python scripts/ingest_round.py raw/11_rs_a.md RI,RO`
- 形式：YAML ブロックは1つ、アンカー・マージキー・脚注番号・仮ID・`basis_tag` は使っていません。`schema/fact.schema.json` で検証し、リポジトリの複製で `ingest_round.py` を試し、エラー0件を確認しました。
- SRC 番号：SRC-350〜385（第11回の範囲 SRC-350〜409 のうち36件）。第10回の SRC-299（人口動態統計 第8表）を2件で再利用しています。
- 範囲：依頼文 `docs/tasks/round11_RS.md` の第11回（Ⅳ-1、Ⅳ-2、Ⅳ-3-A-①②）。出題基準のレベル a の小項目（RI 11項目、RO 9項目）には、すべて1件以上のカードがあります。
- 調査環境の制約：この回の作業環境では Crossref・NCBI の API に直接アクセスできず、PMC と ScienceDirect は取得できませんでした。識別子は出版社ページ・PubMed・大学の研究者情報ページで確認できたものだけを書き、PMID の多くは null です（PC での `scripts/ncbi_crossref.py` による照合が必要です）。
- 最新版の確認：COPD は日本呼吸器学会の第7版（2026年）、GOLD 2026、GINA 2026、ERS 気管支拡張症 2025 を確認しました。第7版 COPD・JGL2024・咳嗽ガイドライン2025 は本文を確認できず、旧版を使ったカードには理由を `uncertainty` に書いています。

## 1. 抽出元ホワイトリスト（新規 SRC-350〜385 と再利用 SRC-299）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | legal_basis | 確認経路 | 使用カード数 |
|---|---|---|---|---|---|---|---|---|
| SRC-299 | 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第8表 性別にみた死因順位（第10位まで）別死亡数・死亡率（人口10万対）・構成割合 | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | B | 第10回の既存 SRC を再利用。厚生労働省の PDF（概況）を WebFetch で確認（第8表） | 2 |
| SRC-350 | 厚生労働省健康・生活衛生局感染症対策部感染症対策課. 抗微生物薬適正使用の手引き 第三版（2023年） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | B | 厚生労働省の PDF を WebFetch で確認（急性気道感染症の章、p.22〜31）。PDF 内に利用規約の個別表示はなく、厚生労働省サイトの利用規約による | 3 |
| SRC-351 | Jones JM, Fleming-Dutra KE, Prill MM, et al. Use of Nirsevimab for the Prevention of Respiratory Syncytial Virus Disease Among Infants and Young Children: Recommendations of the Advisory Committee on Immunization Practices — United States, 2023. MMWR Morb Mortal Wkly Rep 2023;72(34):920-925 | 10.15585/mmwr.mm7234a4 | — | 米国連邦政府の著作物（CDC MMWR） | GOV_US | B | CDC の MMWR 記事ページを WebFetch で確認 | 1 |
| SRC-352 | Mukae H, Iwanaga N, Horita N, et al. The JRS guideline for the management of pneumonia in adults 2024. Respir Investig 2025;63(5):811-828 | 10.1016/j.resinv.2025.06.014 | 40614556 | 未確認（ScienceDirect の取得に失敗。富山大学の研究者情報ページに OA・ライセンスの表示なし） | UNKNOWN | B | 富山大学 Pure の書誌ページ（抄録・DOI・PMID）を WebFetch で確認。本文は未確認 | 2 |
| SRC-353 | 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部） | — | — | CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし） | RESTRICTED | B | 日本呼吸器学会サイトの PDF を WebFetch で確認（p.ii〜xviii、p.1〜9）。A-DROP・I-ROAD の項目表と薬剤名の推奨は抽出できず | 17 |
| SRC-354 | Tashiro M, Fushimi K, Takazono T, et al. A mortality prediction rule for non-elderly patients with community-acquired pneumonia. BMC Pulm Med 2016;16:39 | 10.1186/s12890-016-0199-z | — | CC BY 4.0（Creative Commons Attribution 4.0 International License、出版社ページの表示） | OPEN | B | Springer の記事ページを WebFetch で確認 | 1 |
| SRC-355 | Jones BE, Jones JP, Vines CG, Dean NC. Validating hospital admission criteria for decision support in pneumonia. BMC Pulm Med 2014;14:149 | 10.1186/1471-2466-14-149 | — | CC BY 4.0（論文 PDF の表示。データは CC0 1.0） | OPEN | B | BMC の論文 PDF を WebFetch で確認（Table 1） | 1 |
| SRC-356 | 厚生労働省. 肺炎球菌感染症（高齢者）（Q&A は2024年4月時点。2024年9月30日以降は更新停止と表示） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | B | 厚生労働省のページを WebFetch で確認 | 1 |
| SRC-357 | 札幌市保健所. 高齢者肺炎球菌予防接種（定期接種）について（2026年4月1日更新） | — | — | 未確認（札幌市ホームページ。利用規約の表示は未確認） | UNKNOWN | B | 札幌市のページを WebFetch で確認。根拠となる厚生労働省の通知はページに示されていない | 1 |
| SRC-358 | Centers for Disease Control and Prevention. Pneumococcal Vaccine Recommendations (last reviewed 2026 Feb 25) | — | — | 米国連邦政府の著作物（CDC） | GOV_US | B | CDC のページを WebFetch で確認 | 1 |
| SRC-359 | Centers for Disease Control and Prevention. Clinical Overview of Aspergillosis (last reviewed 2026 Oct 5) | — | — | 米国連邦政府の著作物（CDC） | GOV_US | B | CDC のページを WebFetch で確認 | 2 |
| SRC-360 | Centers for Disease Control and Prevention. Clinical Overview of Cryptococcosis (last reviewed 2024 Apr 24) | — | — | 米国連邦政府の著作物（CDC） | GOV_US | B | CDC のページを WebFetch で確認 | 1 |
| SRC-361 | Panel on Guidelines for the Prevention and Treatment of Opportunistic Infections in Adults and Adolescents With HIV. Guidelines for the Prevention and Treatment of Opportunistic Infections in Adults and Adolescents With HIV: Pneumocystis Pneumonia (updated 2026 May 27). NIH, CDC, HIVMA/IDSA | — | — | 米国連邦政府のサイト（clinicalinfo.hiv.gov、HHS）で公開。第三者素材の扱いは未確認 | GOV_US | B | clinicalinfo.hiv.gov の PDF を WebFetch で確認 | 3 |
| SRC-362 | 厚生労働省. 2024年 結核登録者情報調査年報集計結果について（2025年8月26日公表） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | B | 厚生労働省のページを WebFetch で確認（集計結果の PDF https://www.mhlw.go.jp/content/10900000/001547187.pdf は未確認） | 3 |
| SRC-363 | 厚生労働省. 感染症法に基づく医師の届出のお願い：結核（届出基準） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | B | 厚生労働省のページを WebFetch で確認 | 2 |
| SRC-364 | 厚生労働省健康局結核感染症課長. 「結核医療の基準」の一部改正について（健感発1018第1号、令和3年10月18日）。新旧対照（結核医療の基準：平成21年厚生労働省告示第16号）を含む | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ。告示の内容は著作権法第13条により権利の目的とならない | GOV_JP | C | 厚生労働省の PDF を WebFetch で確認 | 4 |
| SRC-365 | Centers for Disease Control and Prevention. Treatment for Drug-Susceptible Tuberculosis Disease (last reviewed 2025 Mar 7) | — | — | 米国連邦政府の著作物（CDC） | GOV_US | B | CDC のページを WebFetch で確認 | 1 |
| SRC-366 | Centers for Disease Control and Prevention. Treatment for Latent Tuberculosis Infection (last reviewed 2025 Jan 15) | — | — | 米国連邦政府の著作物（CDC） | GOV_US | B | CDC のページを WebFetch で確認 | 1 |
| SRC-367 | Namkoong H, Kurashima A, Morimoto K, et al. Epidemiology of pulmonary nontuberculous mycobacterial disease, Japan. Emerg Infect Dis 2016;22(6):1116-1117 | 10.3201/eid2206.151086 | — | 未確認（CDC 刊行の雑誌。取得した PDF に著作権・利用条件の表示なし） | UNKNOWN | B | CDC の EID サイトの PDF を WebFetch で確認 | 2 |
| SRC-368 | Centers for Disease Control and Prevention. Influenza Antiviral Medications: Summary for Clinicians (last reviewed 2026 Mar 10) | — | — | 米国連邦政府の著作物（CDC） | GOV_US | B | CDC のページを WebFetch で確認 | 1 |
| SRC-369 | 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第9表 死因簡単分類別にみた性別死亡数・死亡率（人口10万対） | — | — | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | B | 厚生労働省の PDF を WebFetch で確認（第9表） | 3 |
| SRC-370 | Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156 | 10.1136/thorax-2023-220304 | — | © Author(s) (or their employer(s)) 2023. No commercial re-use（論文 PDF の表示） | RESTRICTED | B | Thorax の論文 PDF を WebFetch で確認（胸膜感染症の推奨） | 2 |
| SRC-371 | Sugiura H, Fujino N, Shibata Y, Muro S, Matsunaga K, Horita N, Kawayama T. The JRS guideline for the management of chronic obstructive pulmonary disease 7th edition 2026. Respir Investig 2026;64(5):101482 (Epub 2026 Jul 14) | 10.1016/j.resinv.2026.101482 | 42447589 | 未確認（ScienceDirect の取得に失敗） | UNKNOWN | B | PubMed の抄録ページを WebFetch で確認。本文は未確認 | 4 |
| SRC-372 | 日本呼吸器学会 COPD ガイドライン第6版作成委員会. COPD（慢性閉塞性肺疾患）診断と治療のためのガイドライン 第6版 2022（学会サイト掲載 PDF：巻頭ガイドラインサマリー） | — | — | CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし） | RESTRICTED | B | 日本呼吸器学会サイトの PDF を WebFetch で確認（巻頭サマリー p.1〜5） | 7 |
| SRC-373 | Global Initiative for Chronic Obstructive Lung Disease. Pocket Guide to COPD Diagnosis, Management, and Prevention: 2026 Report (v1.1, 2025 Nov 20) | — | — | COPYRIGHT MATERIAL - DO NOT COPY OR DISTRIBUTE / © 2025, 2026 Global Initiative for Chronic Obstructive Lung Disease, Inc.（PDF の表示） | RESTRICTED | B | GOLD サイトの PDF を WebFetch で確認（p.4、9、22、42） | 3 |
| SRC-374 | Niimi A, Fukunaga K, Taniguchi M, et al. Executive summary: Japanese guidelines for adult asthma (JGL) 2021. Allergol Int 2023;72(2):207-226 | 10.1016/j.alit.2023.02.006 | — | 未確認（J-STAGE の表示は「© 2023 by Japanese Society of Allergology」「JOURNAL FREE ACCESS」のみ） | UNKNOWN | B | J-STAGE の記事ページ（抄録）を WebFetch で確認 | 1 |
| SRC-375 | Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention, 2026 update (Strategy Report) | — | — | GINA の著作物（無断配布・改変不可。GINA サイトの利用条件の表示） | RESTRICTED | B | GINA サイトの PDF を WebFetch で確認（p.20〜32、p.92 付近。Step 1〜4 の表、重症喘息の章は抽出できず） | 7 |
| SRC-376 | Mukae H, Kaneko T, Obase Y, et al. The Japanese respiratory society guidelines for the management of cough and sputum (digest edition). Respir Investig 2021;59(3):270-290 | 10.1016/j.resinv.2021.01.007 | 33642231 | 未確認 | UNKNOWN | B | 富山大学 Pure の書誌ページ（抄録・DOI・PMID）を WebFetch で確認 | 1 |
| SRC-377 | Ogawa H, Fujimura M, Ohkura N, Makimura K. Atopic cough and fungal allergy. J Thorac Dis 2014;6(Suppl 7):S689-S698 | 10.3978/j.issn.2072-1439.2014.09.25 | — | CC BY-NC-ND 4.0（記事ページの表示） | RESTRICTED | B | J Thorac Dis の記事ページを WebFetch で確認 | 2 |
| SRC-378 | Chalmers JD, Haworth CS, Flume P, et al. European Respiratory Society Clinical Practice Guideline for the Management of Adult Bronchiectasis (2025) | 10.1183/13993003.01126-2025 | — | 未確認 | UNKNOWN | B | ドイツ肺研究センター（DZL）のガイドライン紹介ページを WebFetch で確認。ERJ の本文・掲載巻号は未確認 | 1 |
| SRC-379 | Lin X, Lu J, Yang M, Dong BR, Wu HM. Macrolides for diffuse panbronchiolitis. Cochrane Database Syst Rev 2015;(1):CD007716 | 10.1002/14651858.CD007716.pub4 | — | Copyright © The Cochrane Collaboration（Cochrane サイトの表示） | RESTRICTED | B | Cochrane の要約ページを WebFetch で確認 | 1 |
| SRC-380 | Online Mendelian Inheritance in Man (OMIM). Panbronchiolitis, diffuse; #604809. Johns Hopkins University | — | — | 未確認（OMIM 本体ではなく、OMIM を出典と明記した FindZebra の転載ページで内容を確認） | UNKNOWN | B | FindZebra の転載ページ（OMIM を出典と表示、2019年取得）を WebFetch で確認。OMIM 本体は未確認 | 1 |
| SRC-381 | National Library of Medicine. MeSH Descriptor: Bronchiolitis Obliterans (D001989) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | B | MeSH Browser を WebFetch で確認 | 1 |
| SRC-382 | National Library of Medicine. MeSH Descriptor: Pulmonary Atelectasis (D001261) | — | — | 米国連邦政府の著作物（NLM） | GOV_US | B | MeSH Browser を WebFetch で確認 | 1 |
| SRC-383 | Chi J, Bai Y. Bronchoscopic management of airway foreign bodies in adults: a narrative educational review. Front Med 2026;13:1779715 | 10.3389/fmed.2026.1779715 | — | 未確認（取得した本文にライセンスの表示なし） | UNKNOWN | B | Frontiers の記事ページを WebFetch で確認 | 2 |
| SRC-384 | Goldberg C, Carey KE. Bullous Lung Disease. West J Emerg Med 2013;14(5):450- | — | — | 未確認（記事ページに CC BY のアイコン表示はあるが、版の表示なし） | UNKNOWN | B | WestJEM の記事ページを WebFetch で確認。DOI は記事ページに表示なし | 1 |
| SRC-385 | Prokakis C, Koletsis EN, Dedeilias P, et al. Airway trauma: a review on epidemiology, mechanisms of injury, diagnosis and treatment. J Cardiothorac Surg 2014;9:117 | 10.1186/1749-8090-9-117 | — | 未確認（オープンアクセスの表示のみ。ライセンスの版は未確認） | UNKNOWN | B | Springer の記事ページを WebFetch で確認 | 1 |

- legal_basis は SRC-364（結核医療の基準＝告示の内容）だけ C、ほかは全件 B（出典の事実・数値を自作文で記述）です。表・図・原文の言い回しは使っていません。
- 日本の学会ガイドラインのうち学会サイトの日本語版 PDF で読んだもの（SRC-353・372）は、CC の表示がないため RESTRICTED としました。対応する英語版（SRC-352・371）は DOI・PMID を確認しましたが、本文とライセンスは取得できず UNKNOWN です。
- 日本と欧米で推奨が違う項目（肺炎の重症度、肺炎球菌ワクチン、COPD の診断・増悪治療、喘息の段階的治療、結核と潜在性結核感染症の治療）は、`condition.region` と `condition.guideline` を分けた別のカードにしています。

## 2. 事実票 YAML

```yaml
- id: RI-001
  domain: RI
  subdomain: 感冒<かぜ症候群>、上気道炎
  assertion:
    plain_statement_ja: 感冒（かぜ症候群）の症状は発症3日目前後に最も強くなり、7〜10日ほどで軽快していく。厚生労働省の手引きは、感冒には抗菌薬を投与しないことを推奨している。
    condition:
      guideline: 抗微生物薬適正使用の手引き 第三版（厚生労働省）
      region: 日本
    differential: null
    common_misconception: 感冒でも黄色や緑色の鼻汁が出たら細菌感染なので抗菌薬が必要である
  provenance:
    source_ref: SRC-350
    source: 厚生労働省健康・生活衛生局感染症対策部感染症対策課. 抗微生物薬適正使用の手引き 第三版（2023年）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10900000/001169116.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 経過の日数は手引きに記載された一般的な経過で、個々の症例では差がある
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-204 (id: JlvnlxA)'
    kokushi: 医学各論 Ⅳ-1-A-①（感冒<かぜ症候群>、上気道炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-002
  domain: RI
  subdomain: 気管支炎、細気管支炎
  assertion:
    plain_statement_ja: 慢性呼吸器疾患などの基礎疾患や合併症のない成人の急性気管支炎には、百日咳を除き抗菌薬を投与しないことが推奨されている。百日咳ではマクロライド系抗菌薬が第一選択とされる。
    condition:
      guideline: 抗微生物薬適正使用の手引き 第三版（厚生労働省）
      region: 日本
    differential: null
    common_misconception: 咳が1週間以上続く急性気管支炎には抗菌薬を処方すべきである
  provenance:
    source_ref: SRC-350
    source: 厚生労働省健康・生活衛生局感染症対策部感染症対策課. 抗微生物薬適正使用の手引き 第三版（2023年）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10900000/001169116.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 小児のマイコプラズマ感染などにも触れられているが、小児の扱いは小児の回で扱う
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-206 (id: JlvnlxM)'
    kokushi: 医学各論 Ⅳ-1-A-②（気管支炎、細気管支炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-003
  domain: RI
  subdomain: 気管支炎、細気管支炎
  assertion:
    plain_statement_ja: 急性気管支炎の咳は平均で約18日（報告により15〜29日程度）続くとされ、咳が長引くこと自体は抗菌薬の適応を示さない。
    condition:
      guideline: 抗微生物薬適正使用の手引き 第三版（厚生労働省）
      region: 日本
    differential: null
    common_misconception: 急性気管支炎の咳は1週間以内に治まるのが普通である
  provenance:
    source_ref: SRC-350
    source: 厚生労働省健康・生活衛生局感染症対策部感染症対策課. 抗微生物薬適正使用の手引き 第三版（2023年）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10900000/001169116.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 手引きが引用している海外の報告の値（平均17.8日、15.3〜28.6日）を丸めて記載した。二次資料経由
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-206 (id: JlvnlxM)'
    kokushi: 医学各論 Ⅳ-1-A-②（気管支炎、細気管支炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-004
  domain: RI
  subdomain: 気管支炎、細気管支炎
  assertion:
    plain_statement_ja: 米国では RS ウイルスが乳児の入院原因の第1位であり、5歳未満の小児で年間約5万〜8万人の入院がある。2023年に ACIP は、初めての RS ウイルス流行期を迎える生後8か月未満の全乳児に長時間作用型の抗体薬ニルセビマブを1回投与することを推奨した。
    condition:
      guideline: ACIP（2023）
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-351
    source: 'Jones JM, Fleming-Dutra KE, Prill MM, et al. Use of Nirsevimab for the Prevention of Respiratory Syncytial Virus Disease Among Infants and Young Children: Recommendations of the Advisory Committee on Immunization Practices — United States, 2023. MMWR Morb Mortal Wkly Rep 2023;72(34):920-925'
    doi: 10.15585/mmwr.mm7234a4
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/mmwr/volumes/72/wr/mm7234a4.htm
    source_license: 米国連邦政府の著作物（CDC MMWR）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 米国の推計と推奨であり、日本の承認・定期接種の状況は確認していない。細気管支炎の治療（支持療法）の記述は含まない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-207 (id: JlvnlxU)；TBL-01-00-416 (id: JlvnmGY)'
    kokushi: 医学各論 Ⅳ-1-A-②（気管支炎、細気管支炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-005
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 日本呼吸器学会の成人肺炎診療ガイドライン2024（2024年4月発行）は、超高齢社会で肺炎の負担が大きいことを踏まえ、抗菌薬の適正使用と高齢者の肺炎の予防・管理を改訂の柱とした。高齢者では誤嚥性肺炎が多く抗菌薬だけでは解決しにくいため、ワクチン、リハビリテーション、口腔ケアを重視している。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-352
    source: Mukae H, Iwanaga N, Horita N, et al. The JRS guideline for the management of pneumonia in adults 2024. Respir Investig 2025;63(5):811-828
    doi: 10.1016/j.resinv.2025.06.014
    pmid: '40614556'
    pmcid: null
    url: https://doi.org/10.1016/j.resinv.2025.06.014
    source_license: 未確認（ScienceDirect の取得に失敗。富山大学の研究者情報ページに OA・ライセンスの表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 英語版の抄録で確認した内容。本文は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-212 (id: Jlvnlx0)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）；医学各論 Ⅳ-1-B-③（医療・介護関連肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-006
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 令和6年（2024年）の人口動態統計（確定数）では、肺炎による死亡は80,176人（死亡率 人口10万対66.6）で死因の第5位、誤嚥性肺炎は63,667人（同52.9）で第6位だった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 肺炎の死亡数には誤嚥性肺炎が含まれている
  provenance:
    source_ref: SRC-299
    source: 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第8表 性別にみた死因順位（第10位まで）別死亡数・死亡率（人口10万対）・構成割合
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/kakutei24/dl/15_gaikyouR06.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 表から読み取り。死因統計では肺炎と誤嚥性肺炎を別に分類している
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-212 (id: Jlvnlx0)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-007
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 市中肺炎では肺炎球菌、インフルエンザ菌、肺炎マイコプラズマが検出されることが多い。成人肺炎診療ガイドライン2024のシステマティックレビューでは、原因菌として最も多いのは肺炎球菌で、15〜20%程度とされた。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: 市中肺炎の原因菌は過半数が肺炎球菌である
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 15〜20%は原因菌を検索した研究の集計にもとづく値で、原因菌が特定できない例を含めた割合かどうかは本文で確認が要る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-008
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 細菌性肺炎はβ-ラクタム系薬が有効で、好中球優位の白血球増多、CRP・プロカルシトニンの上昇、気管支透亮像を伴う浸潤影をとりやすい。非定型肺炎はβ-ラクタム系薬が無効でマクロライド系・テトラサイクリン系・ニューキノロン系薬が有効であり、乾性咳嗽が多く、白血球数や CRP は比較的低く、両肺に散在するすりガラス影をとることが多い。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: 非定型肺炎でもβ-ラクタム系薬で十分に治療できる
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドライン本文は所見を総合して判断するとしている。点数化した鑑別基準（6項目）は今回抽出できた範囲に含まれず、別の版・資料で確認が要る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-009
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 日本呼吸器学会の A-DROP は、CURB-65 を改変した市中肺炎の重症度スコアで、年齢、脱水（臨床的な脱水所見または BUN 21 mg/dL 以上）、呼吸不全（SpO2 90%以下または PaO2 60 mmHg以下）、意識障害、低血圧（収縮期血圧90 mmHg以下）の5項目からなる。0点を軽症、1〜2点を中等症、3点を重症、4〜5点を超重症とする。
    condition:
      guideline: A-DROP（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: A-DROP は肺炎球菌性肺炎だけに使う指標である
  provenance:
    source_ref: SRC-354
    source: Tashiro M, Fushimi K, Takazono T, et al. A mortality prediction rule for non-elderly patients with community-acquired pneumonia. BMC Pulm Med 2016;16:39
    doi: 10.1186/s12890-016-0199-z
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s12890-016-0199-z
    source_license: CC BY 4.0（Creative Commons Attribution 4.0 International License、出版社ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 論文中の BUN の基準は 210 mg/L と表記されており、21 mg/dL に換算して記載した。年齢の基準値はこの論文に記載がない（RI-010 を参照）。表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-010
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: A-DROP の年齢の項目は男性70歳以上、女性75歳以上で1点となる。日本呼吸器学会は A-DROP 2点以上で入院を推奨しており、米国の救急外来の患者2,308人での検証では、A-DROP 2点以上の入院予測の AUC は0.78、30日死亡予測の AUC は0.79だった。
    condition:
      guideline: A-DROP（日本呼吸器学会）
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-355
    source: Jones BE, Jones JP, Vines CG, Dean NC. Validating hospital admission criteria for decision support in pneumonia. BMC Pulm Med 2014;14:149
    doi: 10.1186/1471-2466-14-149
    pmid: null
    pmcid: null
    url: https://bmcpulmmed.biomedcentral.com/counter/pdf/10.1186/1471-2466-14-149.pdf
    source_license: CC BY 4.0（論文 PDF の表示。データは CC0 1.0）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 論文の表では BUN の基準が 210 mg/dL と印刷されており、誤植と考えられる（21 mg/dL が正しい）。表から読み取り。検証は米国の単一医療システムの後ろ向き研究
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-011
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024の市中肺炎の診療の流れでは、まず敗血症性ショックの有無を判断し、次に A-DROP で重症度を評価して治療の場を決める。重症〜超重症や敗血症性ショックでは ICU またはそれに準じる病室、中等症〜重症では一般病棟への入院、軽症〜中等症では外来治療も選択肢となる。市中肺炎の流れには耐性菌リスクの判定は含まれない。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: 市中肺炎でも全例で耐性菌リスク因子を数えて広域抗菌薬を選ぶ
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: フローチャートの文字の抽出が一部崩れており、表から読み取り。中等症の扱い（外来と入院の境界）は本文で確認が要る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-012
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024は、市中肺炎の重症度評価に CURB-65 や PSI ではなく A-DROP を用いることを弱く推奨している（エビデンスの確実性 C）。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）CQ01
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 欧米の重症度評価（CURB-65・PSI）の推奨はこの出典では確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-013
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024は、市中肺炎で症状と検査所見が改善すれば注射薬から経口薬へ切り替えるスイッチ療法を強く推奨し（確実性 B）、初期治療が有効なら治療期間を1週間以内とする短期治療を弱く推奨している（確実性 B）。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）CQ02・CQ03
      region: 日本
    differential: null
    common_misconception: 肺炎の抗菌薬は CRP が正常化するまで静注で続けなければならない
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-014
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024は、市中肺炎の重症例ではβ-ラクタム系薬にマクロライド系薬を併用し、非重症例では併用しないことを弱く推奨している（確実性 C）。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）CQ04
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 具体的な薬剤名・用量の推奨は今回抽出できた範囲に含まれない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-015
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024は、市中肺炎の重症例では抗菌薬に全身性ステロイドを併用し、非重症例では併用しないことを弱く推奨している（確実性 C）。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）CQ05
      region: 日本
    differential: null
    common_misconception: ステロイドはすべての市中肺炎の予後を改善する
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ステロイドの種類・量・期間は今回抽出できた範囲に含まれない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-016
  domain: RI
  subdomain: 院内肺炎
  assertion:
    plain_statement_ja: 院内肺炎（HAP）は入院後48時間以上たってから新たに発症した肺炎をいい、人工呼吸器関連肺炎（VAP）は気管挿管による人工呼吸の開始から48時間以降に新たに発症した院内肺炎をいう。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE)'
    kokushi: 医学各論 Ⅳ-1-B-②（院内肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-017
  domain: RI
  subdomain: 院内肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024の院内肺炎の診療の流れでは、敗血症性ショックの有無を判断したあと I-ROAD で重症度を評価し、耐性菌リスクを判定する。I-ROAD で中等症・重症、敗血症性ショック、または耐性菌リスク因子が2個以上なら広域抗菌薬を検討し、軽症でリスク因子が1個以下なら狭域抗菌薬から始める。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: I-ROAD の各項目と基準値は今回抽出できた範囲に含まれない。フローチャートの抽出が一部崩れており、表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE)'
    kokushi: 医学各論 Ⅳ-1-B-②（院内肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-018
  domain: RI
  subdomain: 院内肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024は、院内肺炎で、抗緑膿菌作用のある広域抗菌薬をルーチンに使わないこと（確実性 C）、初期治療で抗 MRSA 薬をルーチンに併用しないこと（確実性 C）、de-escalation を行うこと（確実性 D）、治療期間を1週間以内とすること（確実性 C）を、いずれも弱く推奨している。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）CQ09〜CQ12
      region: 日本
    differential: null
    common_misconception: 院内肺炎は全例で抗緑膿菌薬と抗 MRSA 薬を併用して始める
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE)'
    kokushi: 医学各論 Ⅳ-1-B-②（院内肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-019
  domain: RI
  subdomain: 院内肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024は、人工呼吸器関連肺炎について、気管支鏡を用いた侵襲的な培養を行わないこと、経験的治療は抗緑膿菌薬の多剤併用ではなく単剤とすること、カルバペネム系薬ではなく非カルバペネム系薬を使うこと、投与期間を比較的短くすることを、いずれも弱く推奨している（確実性 C）。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）CQ14〜CQ17
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 「比較的短期間」の具体的な日数は今回抽出できた範囲に含まれない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE)'
    kokushi: 医学各論 Ⅳ-1-B-②（院内肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-020
  domain: RI
  subdomain: 医療・介護関連肺炎
  assertion:
    plain_statement_ja: 医療・介護関連肺炎（NHCAP）は、院内肺炎以外で、長期療養型病床（精神病床を含む）や介護施設への入所、過去90日以内の退院、介護を要する高齢者・身体障害者、通院での継続的な血管内治療（透析、抗菌薬、化学療法、免疫抑制薬など）のいずれかにあてはまる人に発症した肺炎をいう。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE)'
    kokushi: 医学各論 Ⅳ-1-B-③（医療・介護関連肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-021
  domain: RI
  subdomain: 医療・介護関連肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024は、医療・介護関連肺炎の重症度を A-DROP または I-ROAD で評価することを弱く推奨する（確実性 C）。A-DROP 3点以上の重症例では耐性菌リスク因子1個以上、2点以下の非重症例では3個以上で広域抗菌薬を検討する。緑膿菌をカバーする広域抗菌薬を一律に使わないことも弱く推奨されている（確実性 D）。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）CQ06・CQ08
      region: 日本
    differential: null
    common_misconception: 介護施設からの肺炎は全例が耐性菌を想定した広域抗菌薬の対象である
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: フローチャートの抽出が一部崩れており、表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE)'
    kokushi: 医学各論 Ⅳ-1-B-③（医療・介護関連肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-022
  domain: RI
  subdomain: 医療・介護関連肺炎
  assertion:
    plain_statement_ja: 医療・介護関連肺炎（NHCAP）は、米国 ATS/IDSA の医療ケア関連肺炎（HCAP）を日本向けに改変した分類である。海外では広域抗菌薬の過剰使用への懸念から HCAP の概念が使われなくなっているが、日本の2024年版は高齢者のために NHCAP を残し、抗菌薬の使い方をより厳しく絞っている。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: NHCAP は国際的に共通の肺炎分類である
  provenance:
    source_ref: SRC-352
    source: Mukae H, Iwanaga N, Horita N, et al. The JRS guideline for the management of pneumonia in adults 2024. Respir Investig 2025;63(5):811-828
    doi: 10.1016/j.resinv.2025.06.014
    pmid: '40614556'
    pmcid: null
    url: https://doi.org/10.1016/j.resinv.2025.06.014
    source_license: 未確認（ScienceDirect の取得に失敗。富山大学の研究者情報ページに OA・ライセンスの表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 英語版の抄録で確認した内容
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE)'
    kokushi: 医学各論 Ⅳ-1-B-③（医療・介護関連肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-023
  domain: RI
  subdomain: 医療・介護関連肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024は、院内肺炎・医療・介護関連肺炎の耐性菌リスク因子として、経腸栄養、活動性の低下・歩行不能、免疫抑制状態、透析を含む慢性腎臓病、過去90日以内の抗菌薬使用歴、過去90日以内の入院歴、過去1年以内の耐性菌検出歴を臨床背景として挙げ、低アルブミン血症、挿管による人工呼吸管理、ICU での発症、敗血症・敗血症性ショックを発症時の状況として挙げている。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 表の段組みが抽出で崩れており、各因子が院内肺炎と医療・介護関連肺炎のどちらに適用されるかは原典で確認が要る。表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE)'
    kokushi: 医学各論 Ⅳ-1-B-②（院内肺炎、a）；医学各論 Ⅳ-1-B-③（医療・介護関連肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-024
  domain: RI
  subdomain: 誤嚥性肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024は、誤嚥性肺炎を嚥下機能障害のある人に生じた肺炎と定義し、明確な診断基準はないとしている。嚥下機能障害の背景には意識障害、ADL の低下、脳血管障害、認知症があり、主に加齢に伴う身体の衰えが関わる。中枢神経・頭頸部・胃食道の腫瘍などの器質的疾患を除外し、早期のリハビリテーションで背景の病態の改善を図ることが重要とされる。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: 誤嚥性肺炎は抗菌薬で肺炎を治せば再発しない
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-212 (id: Jlvnlx0)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-025
  domain: RI
  subdomain: 誤嚥性肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024では、誤嚥性肺炎に嫌気性菌をカバーする抗菌薬を使うべきかについて推奨を決められなかった（推奨決定不能）。一方、肺炎の予防に口腔ケアを行うことは弱く推奨されている（確実性 C）。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）CQ18・CQ20
      region: 日本
    differential: null
    common_misconception: 誤嚥性肺炎では必ず嫌気性菌をカバーしなければならない
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: CQ18 は3回の投票で推奨決定の条件（委員の7割以上の賛成）を満たさなかった
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-212 (id: Jlvnlx0)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-026
  domain: RI
  subdomain: 誤嚥性肺炎
  assertion:
    plain_statement_ja: 成人肺炎診療ガイドライン2024は、誤嚥性肺炎を繰り返す人や、疾患の末期・老衰と判断される人では、肺炎の分類にもとづく方針ではなく、本人の意思と QOL を考慮した診療を検討するとしている。本人・家族と予後や選択肢を話し合うアドバンス・ケア・プランニングを行い、合意にもとづいて症状の緩和を基本とし、静注抗菌薬や人工呼吸を行わない選択肢もありうる。
    condition:
      guideline: 成人肺炎診療ガイドライン2024（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-353
    source: 日本呼吸器学会 成人肺炎診療ガイドライン2024作成委員会. 成人肺炎診療ガイドライン2024（学会サイト掲載 PDF：推奨一覧・フローチャート・用語の定義・第1〜2章の一部）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/adult_pneumonia_2024v5.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ACP を始める目安として、1年以内に亡くなっても驚かないかを問う Surprise Question が挙げられている
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-212 (id: Jlvnlx0)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-027
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 2024年4月以降、日本の高齢者の肺炎球菌感染症の定期接種の対象は、65歳の人と、心臓・腎臓・呼吸器の機能障害または HIV による免疫機能障害で日常生活が極度に制限される60〜64歳の人である。接種は1回で、65歳を超える人への経過措置は2024年3月31日で終わった。
    condition:
      guideline: 予防接種法にもとづく定期接種（厚生労働省）
      region: 日本
    differential: null
    common_misconception: 65歳以上なら何歳でも定期接種として受けられる
  provenance:
    source_ref: SRC-356
    source: 厚生労働省. 肺炎球菌感染症（高齢者）（Q&A は2024年4月時点。2024年9月30日以降は更新停止と表示）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/kenkou/kekkaku-kansenshou/haienkyukin/index_1.html
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 2024年4月時点の情報。このページは2024年9月30日以降更新されていない。使用ワクチンは RI-028 を参照
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-617 (id: JlvnmZs)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-028
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 日本の高齢者の肺炎球菌感染症の定期接種に使うワクチンは、2026年4月から23価莢膜ポリサッカライドワクチン（PPSV23）から20価結合型ワクチン（PCV20）に変わった。すでに定期接種を受けた人は再度定期接種を受けることはできない。
    condition:
      guideline: 予防接種法にもとづく定期接種
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-357
    source: 札幌市保健所. 高齢者肺炎球菌予防接種（定期接種）について（2026年4月1日更新）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.city.sapporo.jp/hokenjo/f1kansen/koureihaienn.html
    source_license: 未確認（札幌市ホームページ。利用規約の表示は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 札幌市保健所のページで確認した。変更の根拠となる厚生労働省の通知・告示は未確認で、確認が要る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-617 (id: JlvnmZs)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-029
  domain: RI
  subdomain: 市中肺炎
  assertion:
    plain_statement_ja: 米国 CDC は、肺炎球菌結合型ワクチンを受けたことがない50歳以上の成人に、PCV15、PCV20、PCV21 のいずれかを推奨している。PCV20 か PCV21 なら1回で完了し、PCV15 の場合は原則1年以上あけて PPSV23 を1回追加する。
    condition:
      guideline: CDC（ACIP）の推奨
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-358
    source: Centers for Disease Control and Prevention. Pneumococcal Vaccine Recommendations (last reviewed 2026 Feb 25)
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/pneumococcal/hcp/vaccine-recommendations/index.html
    source_license: 米国連邦政府の著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 日本の定期接種（RI-027・RI-028）とは対象年齢とワクチンが異なる
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-617 (id: JlvnmZs)'
    kokushi: 医学各論 Ⅳ-1-B-①（市中肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-030
  domain: RI
  subdomain: 肺真菌症
  assertion:
    plain_statement_ja: アスペルギルス症には、免疫不全者に生じる侵襲性アスペルギルス症、喘息や嚢胞性線維症などの肺疾患のある人に生じるアレルギー性の病型（アレルギー性気管支肺アスペルギルス症など）、アスペルギローマなどの病型がある。侵襲性アスペルギルス症の危険因子は、高度・長期の好中球減少、造血器腫瘍、造血幹細胞移植・臓器移植、高用量ステロイドや免疫抑制療法である。
    condition:
      guideline: CDC Clinical Overview
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-359
    source: Centers for Disease Control and Prevention. Clinical Overview of Aspergillosis (last reviewed 2026 Oct 5)
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/aspergillosis/hcp/clinical-overview
    source_license: 米国連邦政府の著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 慢性進行性肺アスペルギルス症（CPA）はこのページに記載がない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs)'
    kokushi: 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-031
  domain: RI
  subdomain: 肺真菌症
  assertion:
    plain_statement_ja: アスペルギルス症の診断には、組織の顕微鏡検査・病理、培養、ガラクトマンナン抗原（血清・気管支肺胞洗浄液）、β-D-グルカン、PCR が用いられる。アレルギー性の病型には通常イトラコナゾールが使われ、ステロイドも選択肢となる。アスペルギローマには手術と抗真菌薬を組み合わせることがある。
    condition:
      guideline: CDC Clinical Overview
      region: 米国
    differential: null
    common_misconception: β-D-グルカンが陽性ならアスペルギルス症と確定できる
  provenance:
    source_ref: SRC-359
    source: Centers for Disease Control and Prevention. Clinical Overview of Aspergillosis (last reviewed 2026 Oct 5)
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cdc.gov/aspergillosis/hcp/clinical-overview
    source_license: 米国連邦政府の著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 侵襲性アスペルギルス症の第一選択薬はこのページに記載がなく、IDSA の診療ガイドラインを参照するよう示されている
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs)'
    kokushi: 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-032
  domain: RI
  subdomain: 肺真菌症
  assertion:
    plain_statement_ja: クリプトコックスは土壌や朽ちた木に生息し、C. neoformans は鳥の糞にも存在して、胞子の吸入で感染する。肺の感染は咳・発熱・胸痛など肺炎に似た症状と、胸部画像での結節影や肺門リンパ節腫大を示し、中枢神経に広がると髄膜脳炎を起こす。軽症〜中等症の肺病変にはフルコナゾール、重症の肺病変や中枢神経病変にはアムホテリシンBとフルシトシンの併用で始め、その後フルコナゾールを長く続ける。
    condition:
      guideline: CDC Clinical Overview
      region: 米国
    differential: null
    common_misconception: クリプトコックス症は免疫不全者にしか起こらない
  provenance:
    source_ref: SRC-360
    source: Centers for Disease Control and Prevention. Clinical Overview of Cryptococcosis (last reviewed 2024 Apr 24)
    doi: null
    pmid: null
    pmcid: null
    url: https://cdc.gov/cryptococcosis/hcp/clinical-overview/index.html
    source_license: 米国連邦政府の著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 免疫正常者にも頻度は低いが発症する。診断の基準は培養で、髄液の墨汁染色や抗原検査も用いる
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs)'
    kokushi: 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-033
  domain: RI
  subdomain: 肺真菌症
  assertion:
    plain_statement_ja: ニューモシスチス肺炎は、数日〜数週かけて進む労作時呼吸困難、発熱、乾性咳嗽で始まることが多く、低酸素血症が最も特徴的な検査所見である。胸部画像では両側びまん性・対称性のすりガラス影が典型だが、初期の胸部X線は正常のことがある。血清β-D-グルカンは上昇することが多いが特異度は低い。
    condition:
      guideline: 米国 HIV 日和見感染症ガイドライン（NIH・CDC・HIVMA/IDSA）
      region: 米国
    differential: null
    common_misconception: 胸部X線が正常ならニューモシスチス肺炎は否定できる
  provenance:
    source_ref: SRC-361
    source: 'Panel on Guidelines for the Prevention and Treatment of Opportunistic Infections in Adults and Adolescents With HIV. Guidelines for the Prevention and Treatment of Opportunistic Infections in Adults and Adolescents With HIV: Pneumocystis Pneumonia (updated 2026 May 27). NIH, CDC, HIVMA/IDSA'
    doi: null
    pmid: null
    pmcid: null
    url: https://clinicalinfo.hiv.gov/sites/g/files/mnhszr391/files/guidelines/documents/adult-adolescent-oi/pneumocystis-pneumonia-adult-adolescent-oi.pdf
    source_license: 米国連邦政府のサイト（clinicalinfo.hiv.gov、HHS）で公開。第三者素材の扱いは未確認
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: HIV 感染者を対象とした記述。HIV 以外の免疫不全者では経過がより急速なことがあるが、この出典では確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs)'
    kokushi: 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-034
  domain: RI
  subdomain: 肺真菌症
  assertion:
    plain_statement_ja: ニューモシスチス肺炎の確定診断には、組織、気管支肺胞洗浄液、誘発喀痰で病原体を確認する（自然喀出痰は検体に適さない）。治療の第一選択は ST 合剤で、期間は21日間である。室内気で PaO2 70 mmHg未満または A-aDO2 35 mmHg以上なら、治療開始から72時間以内に副腎皮質ステロイドを併用する。
    condition:
      guideline: 米国 HIV 日和見感染症ガイドライン（NIH・CDC・HIVMA/IDSA）
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-361
    source: 'Panel on Guidelines for the Prevention and Treatment of Opportunistic Infections in Adults and Adolescents With HIV. Guidelines for the Prevention and Treatment of Opportunistic Infections in Adults and Adolescents With HIV: Pneumocystis Pneumonia (updated 2026 May 27). NIH, CDC, HIVMA/IDSA'
    doi: null
    pmid: null
    pmcid: null
    url: https://clinicalinfo.hiv.gov/sites/g/files/mnhszr391/files/guidelines/documents/adult-adolescent-oi/pneumocystis-pneumonia-adult-adolescent-oi.pdf
    source_license: 米国連邦政府のサイト（clinicalinfo.hiv.gov、HHS）で公開。第三者素材の扱いは未確認
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 推奨の評価は ST 合剤（AI）、21日間（AII）、ステロイド併用（AI）。HIV 感染者を対象とした推奨
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs)'
    kokushi: 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-035
  domain: RI
  subdomain: 肺真菌症
  assertion:
    plain_statement_ja: HIV 感染者では、CD4 陽性リンパ球が200/μL未満になったらニューモシスチス肺炎の一次予防を始め、ST 合剤を第一選択とする。抗 HIV 療法で CD4 が200/μL以上に3か月以上保たれたら、一次予防を中止する。
    condition:
      guideline: 米国 HIV 日和見感染症ガイドライン（NIH・CDC・HIVMA/IDSA）
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-361
    source: 'Panel on Guidelines for the Prevention and Treatment of Opportunistic Infections in Adults and Adolescents With HIV. Guidelines for the Prevention and Treatment of Opportunistic Infections in Adults and Adolescents With HIV: Pneumocystis Pneumonia (updated 2026 May 27). NIH, CDC, HIVMA/IDSA'
    doi: null
    pmid: null
    pmcid: null
    url: https://clinicalinfo.hiv.gov/sites/g/files/mnhszr391/files/guidelines/documents/adult-adolescent-oi/pneumocystis-pneumonia-adult-adolescent-oi.pdf
    source_license: 米国連邦政府のサイト（clinicalinfo.hiv.gov、HHS）で公開。第三者素材の扱いは未確認
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 推奨の評価はいずれも AI。HIV 以外の免疫抑制患者の予防の基準は含まない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs)'
    kokushi: 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-036
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 2024年の日本の新登録結核患者は10,051人、罹患率は人口10万対8.1で前年と同じだった。罹患率10以下の低まん延の水準は2021年から続いている。喀痰塗抹陽性肺結核は3,352人（罹患率2.7）だった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 日本の結核は過去の病気で、新たな患者はほとんどいない
  provenance:
    source_ref: SRC-362
    source: 厚生労働省. 2024年 結核登録者情報調査年報集計結果について（2025年8月26日公表）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000175095_00016.html
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 厚生労働省の公表ページの数値。集計結果の PDF 本体は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-037
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 2024年の日本の新登録結核患者の年齢は80〜89歳が28.4%と最も多く、罹患率（人口10万対）は70〜79歳で10.9、80〜89歳で28.3、90歳以上で51.1と高齢ほど高い。外国生まれの患者は1,980人で全体の19.7%を占め、前年の16.0%から増えた。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-362
    source: 厚生労働省. 2024年 結核登録者情報調査年報集計結果について（2025年8月26日公表）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000175095_00016.html
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 厚生労働省の公表ページの数値。集計結果の PDF 本体は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-038
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 2024年の日本では、多剤耐性肺結核の新登録は45人（うち外国生まれ22人）、糖尿病の合併は15.7%だった。2023年に新登録された患者の2024年末時点の治療成功率は67.3%、死亡は25.1%だった。潜在性結核感染症の新登録は5,967人で、前年より18.6%増えた。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-362
    source: 厚生労働省. 2024年 結核登録者情報調査年報集計結果について（2025年8月26日公表）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000175095_00016.html
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 厚生労働省の公表ページの数値。集計結果の PDF 本体は未確認。死亡には結核以外の原因による死亡も含まれうる
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-039
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 結核は感染症法にもとづき、医師が患者、疑似症患者、治療を要する無症状病原体保有者（潜在性結核感染症）を診断したとき、直ちに最寄りの保健所長に届け出る。診断に用いる検査には塗抹・培養・核酸増幅法による病原体の検出、病理検査、ツベルクリン反応、インターフェロンγ遊離試験（IGRA）、画像検査がある。
    condition:
      guideline: 感染症法第12条（結核の届出基準、厚生労働省）
      region: 日本
    differential: null
    common_misconception: 潜在性結核感染症は発病していないので届出の対象ではない
  provenance:
    source_ref: SRC-363
    source: 厚生労働省. 感染症法に基づく医師の届出のお願い：結核（届出基準）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/bunya/kenkou/kekkaku-kansenshou11/01-02-02.html
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 5歳未満では、検査で確認できなくても濃厚接触などから感染の可能性が高い場合に無症状病原体保有者として届け出る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-040
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 結核は主に飛沫核による空気感染で広がり、感染源の多くは喀痰塗抹陽性の肺結核患者である。感染者のうち発病するのは約30%とされ、感染後1年以内、乳幼児期・思春期、糖尿病の合併、胃切除歴、免疫抑制剤による治療中は発病の危険が高い。肺外結核として胸膜、リンパ節、骨関節、腎尿路生殖器、中枢神経の病変や粟粒結核もある。
    condition:
      guideline: 結核の届出基準（厚生労働省）
      region: 日本
    differential: null
    common_misconception: 結核に感染した人はほぼ全員が発病する
  provenance:
    source_ref: SRC-363
    source: 厚生労働省. 感染症法に基づく医師の届出のお願い：結核（届出基準）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/bunya/kenkou/kekkaku-kansenshou11/01-02-02.html
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 発病率約30%は届出基準の臨床的特徴の記載による。どの期間・集団での割合かは原典に記載がなく、確認が要る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-041
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 日本の結核医療の基準では、肺結核の初回治療は、イソニアジド・リファンピシン・ピラジナミドにエタンブトールまたはストレプトマイシンを加えた4剤を2か月使い、その後イソニアジドとリファンピシンの2剤を治療開始から6か月（180日）まで続ける。ピラジナミドを使えない場合は、3剤を2〜6か月使ったあと2剤を開始から9か月（270日）まで続ける。
    condition:
      guideline: 結核医療の基準（平成21年厚生労働省告示第16号）
      region: 日本
    differential: null
    common_misconception: 肺結核の標準治療は3剤併用で1年間行う
  provenance:
    source_ref: SRC-364
    source: 厚生労働省健康局結核感染症課長. 「結核医療の基準」の一部改正について（健感発1018第1号、令和3年10月18日）。新旧対照（結核医療の基準：平成21年厚生労働省告示第16号）を含む
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/000844766.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ。告示の内容は著作権法第13条により権利の目的とならない
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 米国 CDC の標準治療（RI-045）と基本の組み合わせは同じだが、4か月レジメンの扱いが異なる
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-042
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 日本の結核医療の基準では、治療開始時に症状が著しく重い、2か月たっても培養が陰性化しない、糖尿病・じん肺・HIV 感染など結核の経過に影響する病気を合併する、ステロイドや免疫抑制剤を長く使っている場合に、治療期間を3か月延長できる。再治療でも初回より3か月延長できる。
    condition:
      guideline: 結核医療の基準（平成21年厚生労働省告示第16号）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-364
    source: 厚生労働省健康局結核感染症課長. 「結核医療の基準」の一部改正について（健感発1018第1号、令和3年10月18日）。新旧対照（結核医療の基準：平成21年厚生労働省告示第16号）を含む
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/000844766.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ。告示の内容は著作権法第13条により権利の目的とならない
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-043
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 2021年の結核医療の基準の改正で、イソニアジドとリファンピシンの両方に耐性の多剤耐性結核には5剤併用療法を行い、治療期間は培養陰性化から18か月とされた。基本となる薬剤はレボフロキサシンとベダキリンで、エタンブトール、ピラジナミド、デラマニド、サイクロセリンなどの使用を検討する。
    condition:
      guideline: 結核医療の基準（2021年10月18日改正）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-364
    source: 厚生労働省健康局結核感染症課長. 「結核医療の基準」の一部改正について（健感発1018第1号、令和3年10月18日）。新旧対照（結核医療の基準：平成21年厚生労働省告示第16号）を含む
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/000844766.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ。告示の内容は著作権法第13条により権利の目的とならない
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: WHO の多剤耐性結核の短期レジメンとは期間が異なる。WHO の推奨はこの出典では確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-044
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 日本の結核医療の基準では、潜在性結核感染症の治療は、原則としてイソニアジド単独を6か月（必要に応じてさらに3か月）か、イソニアジドとリファンピシンの併用を3か月または4か月行う。イソニアジドを使えないか副作用が予想される場合は、リファンピシン単独を4か月行う。
    condition:
      guideline: 結核医療の基準（2021年10月18日改正）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-364
    source: 厚生労働省健康局結核感染症課長. 「結核医療の基準」の一部改正について（健感発1018第1号、令和3年10月18日）。新旧対照（結核医療の基準：平成21年厚生労働省告示第16号）を含む
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/000844766.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ。告示の内容は著作権法第13条により権利の目的とならない
    legal_basis: C
    source_class: GOV_JP
    corroboration: null
  uncertainty: 米国 CDC の推奨（RI-046）では3HP などリファマイシンを含む短期レジメンが優先される
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-045
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 米国 CDC は、薬剤感受性肺結核の治療として、イソニアジド・リファンピシン・ピラジナミド・エタンブトールの2か月と、イソニアジド・リファンピシンの4か月からなる6か月レジメンを示している。12歳以上・体重40 kg以上などの条件を満たせば、リファペンチンとモキシフロキサシンを含む4か月レジメンも選択肢となる。直接服薬確認（DOT）が標準とされる。
    condition:
      guideline: CDC（2016年 ATS/CDC/IDSA ガイドラインと2022年の4か月レジメンの推奨）
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-365
    source: Centers for Disease Control and Prevention. Treatment for Drug-Susceptible Tuberculosis Disease (last reviewed 2025 Mar 7)
    doi: null
    pmid: null
    pmcid: null
    url: https://cdc.gov/TB/topic/treatment/TBdisease.htm
    source_license: 米国連邦政府の著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: HIV 感染者で4か月レジメンを使う条件は CD4 100/μL以上など。空洞があり2か月時点で培養陽性なら9か月に延長する
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-046
  domain: RI
  subdomain: 肺結核症
  assertion:
    plain_statement_ja: 米国 CDC は、潜在性結核感染症の治療として、リファマイシンを含む3〜4か月の短期レジメン（イソニアジドとリファペンチンの週1回12回の3HP、リファンピシン連日4か月の4R、イソニアジドとリファンピシン連日3か月の3HR）を優先して推奨し、イソニアジド単独6か月・9か月は代替とする。
    condition:
      guideline: CDC・National Tuberculosis Coalition of America
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-366
    source: Centers for Disease Control and Prevention. Treatment for Latent Tuberculosis Infection (last reviewed 2025 Jan 15)
    doi: null
    pmid: null
    pmcid: null
    url: https://cdc.gov/tb/topic/treatment/ltbi.htm
    source_license: 米国連邦政府の著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 3HP は2歳未満と妊婦には推奨されない。日本ではリファペンチンの承認状況を確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg)'
    kokushi: 医学各論 Ⅳ-1-D-①（肺結核症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-047
  domain: RI
  subdomain: 非結核性抗酸菌症
  assertion:
    plain_statement_ja: 2014年の全国調査では、日本の肺非結核性抗酸菌症の推定罹患率は人口10万人年あたり14.7で、2007年（5.7）の約2.6倍に増え、同年の結核の罹患率（12.9）を上回った。菌種別では MAC が13.1と大部分を占め、M. kansasii が0.6、M. abscessus が0.5だった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 日本では非結核性抗酸菌症は結核よりまれである
  provenance:
    source_ref: SRC-367
    source: Namkoong H, Kurashima A, Morimoto K, et al. Epidemiology of pulmonary nontuberculous mycobacterial disease, Japan. Emerg Infect Dis 2016;22(6):1116-1117
    doi: 10.3201/eid2206.151086
    pmid: null
    pmcid: null
    url: https://wwwnc.cdc.gov/eid/article/22/6/pdfs/15-1086.pdf
    source_license: 未確認（CDC 刊行の雑誌。取得した PDF に著作権・利用条件の表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 呼吸器学会認定施設へのアンケート（回答率62.3%）と、結核との比率からの推計値
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-210 (id: Jlvnlxo)'
    kokushi: 医学各論 Ⅳ-1-D-②（非結核性抗酸菌症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-048
  domain: RI
  subdomain: 非結核性抗酸菌症
  assertion:
    plain_statement_ja: 日本の肺 MAC 症では、M. avium の割合は北日本・東日本で高く、M. intracellulare の割合は南日本・西日本で高い。M. abscessus 症は2001年の人口10万人年あたり0.1から2014年の0.5に増えた。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-367
    source: Namkoong H, Kurashima A, Morimoto K, et al. Epidemiology of pulmonary nontuberculous mycobacterial disease, Japan. Emerg Infect Dis 2016;22(6):1116-1117
    doi: 10.3201/eid2206.151086
    pmid: null
    pmcid: null
    url: https://wwwnc.cdc.gov/eid/article/22/6/pdfs/15-1086.pdf
    source_license: 未確認（CDC 刊行の雑誌。取得した PDF に著作権・利用条件の表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 全国調査にもとづく推計
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-210 (id: Jlvnlxo)'
    kokushi: 医学各論 Ⅳ-1-D-②（非結核性抗酸菌症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-049
  domain: RI
  subdomain: インフルエンザ、サイトメガロウイルス肺炎
  assertion:
    plain_statement_ja: 米国 CDC は、入院患者、重症・合併症のある・進行性の患者、合併症の高リスク者のインフルエンザには、疑いの段階でもできるだけ早く抗インフルエンザ薬を始めるよう推奨しており、入院患者にはオセルタミビルを用いる。効果は発症48時間以内の開始で最も大きいが、入院・重症例では48時間を過ぎて始めても利益が示されている。重症例では肺炎球菌、化膿レンサ球菌、MRSA を含む黄色ブドウ球菌による二次性細菌性肺炎に注意する。
    condition:
      guideline: 'CDC Influenza Antiviral Medications: Summary for Clinicians'
      region: 米国
    differential: null
    common_misconception: 発症から48時間を過ぎたインフルエンザには抗ウイルス薬は意味がない
  provenance:
    source_ref: SRC-368
    source: 'Centers for Disease Control and Prevention. Influenza Antiviral Medications: Summary for Clinicians (last reviewed 2026 Mar 10)'
    doi: null
    pmid: null
    pmcid: null
    url: https://cdc.gov/flu/hcp/antivirals/summary-clinicians.html
    source_license: 米国連邦政府の著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 米国で承認されている薬はオセルタミビル（経口）、ザナミビル（吸入）、ペラミビル（静注）、バロキサビル（経口）。日本の承認薬はこの出典では確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-619 (id: JlvnmZ4)'
    kokushi: 医学各論 Ⅳ-1-E-①（インフルエンザ、サイトメガロウイルス肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-050
  domain: RI
  subdomain: インフルエンザ、サイトメガロウイルス肺炎
  assertion:
    plain_statement_ja: 令和6年（2024年）の人口動態統計（確定数）では、インフルエンザによる死亡は2,857人（死亡率 人口10万対2.4）だった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-369
    source: 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第9表 死因簡単分類別にみた性別死亡数・死亡率（人口10万対）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/kakutei24/dl/15_gaikyouR06.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 表から読み取り。インフルエンザ後の細菌性肺炎による死亡は肺炎に分類されうる
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-619 (id: JlvnmZ4)'
    kokushi: 医学各論 Ⅳ-1-E-①（インフルエンザ、サイトメガロウイルス肺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-051
  domain: RI
  subdomain: インフルエンザ、サイトメガロウイルス肺炎
  assertion:
    plain_statement_ja: 令和6年（2024年）の人口動態統計（確定数）では、新型コロナウイルス感染症による死亡は35,865人（死亡率 人口10万対29.8）で、死因の第8位だった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-299
    source: 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第8表 性別にみた死因順位（第10位まで）別死亡数・死亡率（人口10万対）・構成割合
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/kakutei24/dl/15_gaikyouR06.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 表から読み取り。COVID-19 は出題基準 Ⅳ の表にないため、出題基準の番号は付けていない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-620 (id: JlvnmaA)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-052
  domain: RI
  subdomain: 胸膜炎
  assertion:
    plain_statement_ja: 英国胸部学会（BTS）の2023年ガイドラインは、胸腔穿刺で明らかな膿が引けない胸膜感染症では、胸水の pH をすぐに測るよう強く推奨している。pH 7.2以下なら複雑性肺炎随伴性胸水の可能性が高く胸腔ドレーンを入れ、7.2〜7.4なら LDH が900 IU/L を超えるときにドレナージを考慮し、7.4以上ならすぐのドレナージは不要とする。pH が測れない場合は、胸水の糖が3.3 mmol/L未満であることをドレナージの判断に使える。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: 胸水の pH は検体を放置してからまとめて測ればよい
  provenance:
    source_ref: SRC-370
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use（論文 PDF の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 局所麻酔薬やヘパリンの混入で pH は低く、測定が遅れると高く出る。糖3.3 mmol/L は約60 mg/dL に相当する。表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-213 (id: Jlvnlx4)；TBL-01-00-240 (id: Jlvnl08)'
    kokushi: 医学各論 Ⅳ-1-G-①（胸膜炎、a）；医学各論 Ⅳ-1-G-②（膿胸、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RI-053
  domain: RI
  subdomain: 膿胸
  assertion:
    plain_statement_ja: BTS の2023年ガイドラインは、胸膜感染症の最初のドレナージには14 Fr 以下の細いチューブを使い、ドレナージが止まっても胸水が残る場合は組織プラスミノーゲン活性化因子（tPA）と DNase の併用による胸腔内注入を考慮するとしている。どちらか一方だけの注入や、ストレプトキナーゼは推奨されない。最初の治療として早期の胸腔鏡手術を胸腔ドレナージより優先することはしない。
    condition:
      guideline: BTS Guideline for pleural disease 2023
      region: 英国
    differential: null
    common_misconception: 胸腔内の線溶療法はウロキナーゼなどの単剤で十分である
  provenance:
    source_ref: SRC-370
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use（論文 PDF の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: tPA・DNase の胸腔内投与の日本での承認・保険適用は確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-213 (id: Jlvnlx4)；TBL-01-00-240 (id: Jlvnl08)'
    kokushi: 医学各論 Ⅳ-1-G-②（膿胸、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-001
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: 日本では40歳以上の約8.6%が COPD を有すると推定されているが、正式に診断されているのはそのうち10%未満である。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第7版 2026（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: COPD 患者の大部分はすでに診断され治療を受けている
  provenance:
    source_ref: SRC-371
    source: Sugiura H, Fujino N, Shibata Y, Muro S, Matsunaga K, Horita N, Kawayama T. The JRS guideline for the management of chronic obstructive pulmonary disease 7th edition 2026. Respir Investig 2026;64(5):101482 (Epub 2026 Jul 14)
    doi: 10.1016/j.resinv.2026.101482
    pmid: '42447589'
    pmcid: null
    url: https://doi.org/10.1016/j.resinv.2026.101482
    source_license: 未確認（ScienceDirect の取得に失敗）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 英語版の抄録で確認した内容。8.6%の根拠となる疫学調査は本文で確認が要る。二次資料経由
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-002
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: 令和6年（2024年）の人口動態統計（確定数）では、慢性閉塞性肺疾患（COPD）による死亡は16,629人（死亡率 人口10万対13.8）だった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-369
    source: 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第9表 死因簡単分類別にみた性別死亡数・死亡率（人口10万対）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/kakutei24/dl/15_gaikyouR06.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-003
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: 日本呼吸器学会の COPD ガイドライン第7版（2026年3月発行）は、GOLD 2023 の病因別分類（etiotype）を正式に採り入れ、CT で見つかる粘液栓を独立した予後因子とし、細胞老化を病態の機序として加えた。日本人の COPD の特徴として、やせ型が多いこと、増悪が少ないこと、喘息 COPD オーバーラップの割合が高いことを挙げている。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第7版 2026（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-371
    source: Sugiura H, Fujino N, Shibata Y, Muro S, Matsunaga K, Horita N, Kawayama T. The JRS guideline for the management of chronic obstructive pulmonary disease 7th edition 2026. Respir Investig 2026;64(5):101482 (Epub 2026 Jul 14)
    doi: 10.1016/j.resinv.2026.101482
    pmid: '42447589'
    pmcid: null
    url: https://doi.org/10.1016/j.resinv.2026.101482
    source_license: 未確認（ScienceDirect の取得に失敗）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 英語版の抄録で確認した内容。本文は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-004
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: COPD ガイドライン第7版（2026年）は、第6版の15のクリニカルクエスチョンに長期マクロライド療法、気管支鏡的肺容量減少術、増悪時の包括的管理などの7つを加えた。2型炎症があり増悪を繰り返す患者にデュピルマブを新たに推奨し、増悪中・増悪後の心血管リスクの管理を管理目標の中心に置いている。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第7版 2026（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-371
    source: Sugiura H, Fujino N, Shibata Y, Muro S, Matsunaga K, Horita N, Kawayama T. The JRS guideline for the management of chronic obstructive pulmonary disease 7th edition 2026. Respir Investig 2026;64(5):101482 (Epub 2026 Jul 14)
    doi: 10.1016/j.resinv.2026.101482
    pmid: '42447589'
    pmcid: null
    url: https://doi.org/10.1016/j.resinv.2026.101482
    source_license: 未確認（ScienceDirect の取得に失敗）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 英語版の抄録で確認した内容。デュピルマブの推奨の強さ・対象の基準（好酸球数など）と、日本での COPD への承認状況は確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-005
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: 日本呼吸器学会の COPD ガイドライン（第6版）では、長期の喫煙などの曝露歴があり、気管支拡張薬吸入後のスパイロメトリーで1秒率（FEV1/FVC）が70%未満で、ほかの気流閉塞をきたす疾患を除外できることを COPD の診断の条件としている。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第6版 2022（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: 気管支拡張薬を吸入する前の1秒率で COPD を診断してよい
  provenance:
    source_ref: SRC-372
    source: 日本呼吸器学会 COPD ガイドライン第6版作成委員会. COPD（慢性閉塞性肺疾患）診断と治療のためのガイドライン 第6版 2022（学会サイト掲載 PDF：巻頭ガイドラインサマリー）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/COPD6_20220726.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 最新版は第7版（2026年）だが本文を確認できなかったため、第6版のサマリーを出典にした。第7版での変更の有無は確認が要る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-021 (id: JlAKpiU)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-006
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: COPD の病期は、気管支拡張薬吸入後の1秒率70%未満を前提に、予測1秒量に対する割合（%FEV1）で分類する。80%以上がⅠ期（軽度）、50%以上80%未満がⅡ期（中等度）、30%以上50%未満がⅢ期（高度）、30%未満がⅣ期（きわめて高度）である。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第6版 2022（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: 病期は1秒率（FEV1/FVC）の値で分ける
  provenance:
    source_ref: SRC-372
    source: 日本呼吸器学会 COPD ガイドライン第6版作成委員会. COPD（慢性閉塞性肺疾患）診断と治療のためのガイドライン 第6版 2022（学会サイト掲載 PDF：巻頭ガイドラインサマリー）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/COPD6_20220726.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 表から読み取り。第7版の本文は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-021 (id: JlAKpiU)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-007
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: GOLD 2026 は、COPD を慢性の呼吸器症状を特徴とする不均一な肺の状態とし、診断には気管支拡張薬吸入後の FEV1/FVC 0.7未満を示すスパイロメトリーが必須であるとしている。
    condition:
      guideline: GOLD 2026 Report
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-373
    source: 'Global Initiative for Chronic Obstructive Lung Disease. Pocket Guide to COPD Diagnosis, Management, and Prevention: 2026 Report (v1.1, 2025 Nov 20)'
    doi: null
    pmid: null
    pmcid: null
    url: https://goldcopd.org/wp-content/uploads/2025/11/GOLD-Pocket-Guide-2026-v1.1-20Nov2025_WMV.pdf
    source_license: COPYRIGHT MATERIAL - DO NOT COPY OR DISTRIBUTE / © 2025, 2026 Global Initiative for Chronic Obstructive Lung Disease, Inc.（PDF の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本の第6版（RO-005）も同じ基準を70%未満と表記している
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-021 (id: JlAKpiU)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-008
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: 日本の COPD ガイドライン（第6版）では、安定期の薬物療法の中心は長時間作用性気管支拡張薬（LAMA、LABA、LAMA/LABA 配合薬）である。喘息の病態を合併しない例では LAMA（または LABA）から始めて LAMA＋LABA に進め、吸入ステロイドを含む配合薬は喘息の病態を合併する例や、増悪を繰り返し末梢血好酸球が増えている例で使う。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第6版 2022（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: COPD の吸入療法は吸入ステロイドから始める
  provenance:
    source_ref: SRC-372
    source: 日本呼吸器学会 COPD ガイドライン第6版作成委員会. COPD（慢性閉塞性肺疾患）診断と治療のためのガイドライン 第6版 2022（学会サイト掲載 PDF：巻頭ガイドラインサマリー）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/COPD6_20220726.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 好酸球数の具体的な基準値は今回抽出できた範囲に含まれない。第7版の本文は未確認
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-009
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: 日本の COPD ガイドライン（第6版）は、禁煙が COPD の進行を遅らせるとし、禁煙を達成させる指導を重視している。喫煙者の20%前後が COPD を発症するとされる。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第6版 2022（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: COPD と診断されたあとに禁煙しても意味がない
  provenance:
    source_ref: SRC-372
    source: 日本呼吸器学会 COPD ガイドライン第6版作成委員会. COPD（慢性閉塞性肺疾患）診断と治療のためのガイドライン 第6版 2022（学会サイト掲載 PDF：巻頭ガイドラインサマリー）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/COPD6_20220726.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 20%前後という値の原著は未確認。二次資料経由
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-010
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: 日本の COPD ガイドライン（第6版）は、安定期の管理として、教育・運動・栄養を含む呼吸リハビリテーションを導入して続けること、手洗い・口腔ケア・ワクチン・マスクによる感染予防を挙げている。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第6版 2022（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-372
    source: 日本呼吸器学会 COPD ガイドライン第6版作成委員会. COPD（慢性閉塞性肺疾患）診断と治療のためのガイドライン 第6版 2022（学会サイト掲載 PDF：巻頭ガイドラインサマリー）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/COPD6_20220726.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 呼吸リハビリテーションの具体的なプログラムは今回抽出できた範囲に含まれない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-025 (id: JlAKpig)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-011
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: GOLD 2026 は、安静時の高度な慢性低酸素血症（PaO2 55 mmHg以下、または肺性心や二次性多血症があれば60 mmHg未満）の COPD 患者では長期酸素療法が生存を改善しうるとし、中等度の酸素飽和度低下にとどまる安定期の患者にはルーチンに処方しないとしている。
    condition:
      guideline: GOLD 2026 Report
      region: 国際
    differential: null
    common_misconception: 労作時に少しでも SpO2 が下がる COPD 患者には全例で在宅酸素療法を行う
  provenance:
    source_ref: SRC-373
    source: 'Global Initiative for Chronic Obstructive Lung Disease. Pocket Guide to COPD Diagnosis, Management, and Prevention: 2026 Report (v1.1, 2025 Nov 20)'
    doi: null
    pmid: null
    pmcid: null
    url: https://goldcopd.org/wp-content/uploads/2025/11/GOLD-Pocket-Guide-2026-v1.1-20Nov2025_WMV.pdf
    source_license: COPYRIGHT MATERIAL - DO NOT COPY OR DISTRIBUTE / © 2025, 2026 Global Initiative for Chronic Obstructive Lung Disease, Inc.（PDF の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本の在宅酸素療法の保険適用の基準（睡眠時・運動時の低酸素血症の扱いなど）はこの出典では確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-026 (id: JlAKpik)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-012
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: 日本の COPD ガイドライン（第6版）では、増悪の薬物療法は抗菌薬・気管支拡張薬・ステロイドの ABC アプローチが基本である。痰の膿性化や CRP 陽性などの炎症反応があれば抗菌薬を使い、短時間作用性β2刺激薬を反復吸入し、不十分なら短時間作用性抗コリン薬を併用する。全身ステロイドはプレドニゾロン換算30〜40 mg/日を5〜7日間使う。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第6版 2022（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: COPD 増悪の全身ステロイドは2週間以上かけて漸減する
  provenance:
    source_ref: SRC-372
    source: 日本呼吸器学会 COPD ガイドライン第6版作成委員会. COPD（慢性閉塞性肺疾患）診断と治療のためのガイドライン 第6版 2022（学会サイト掲載 PDF：巻頭ガイドラインサマリー）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/COPD6_20220726.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 第7版では増悪時の管理に新しいクリニカルクエスチョンが加わっており（RO-004）、用量・期間が変わっていないか確認が要る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-013
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: 日本の COPD ガイドライン（第6版）は、COPD の増悪時に PaO2 60 Torr未満または SpO2 90%未満であれば酸素療法の適応としている。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第6版 2022（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-372
    source: 日本呼吸器学会 COPD ガイドライン第6版作成委員会. COPD（慢性閉塞性肺疾患）診断と治療のためのガイドライン 第6版 2022（学会サイト掲載 PDF：巻頭ガイドラインサマリー）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jrs.or.jp/publication/file/COPD6_20220726.pdf
    source_license: CC の表示なし（学会の著作物。抽出できた範囲に転載条件の個別表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: CO2 ナルコーシスへの注意や目標 SpO2 は今回抽出できた範囲に含まれない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-026 (id: JlAKpik)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-014
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: GOLD 2026 は、COPD の増悪を数日（最大14日）のうちに症状が悪化するものとし、重症度は Rome 提案にもとづいて軽症・中等症・重症に分ける。中等症・重症の増悪には全身ステロイドを最長5日、膿性痰などがあれば抗菌薬を計5日使い、メチルキサンチンは推奨しない。
    condition:
      guideline: GOLD 2026 Report
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-373
    source: 'Global Initiative for Chronic Obstructive Lung Disease. Pocket Guide to COPD Diagnosis, Management, and Prevention: 2026 Report (v1.1, 2025 Nov 20)'
    doi: null
    pmid: null
    pmcid: null
    url: https://goldcopd.org/wp-content/uploads/2025/11/GOLD-Pocket-Guide-2026-v1.1-20Nov2025_WMV.pdf
    source_license: COPYRIGHT MATERIAL - DO NOT COPY OR DISTRIBUTE / © 2025, 2026 Global Initiative for Chronic Obstructive Lung Disease, Inc.（PDF の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ステロイドの用量はこの出典では確認していない。日本の第6版の増悪治療（RO-012）とは期間の表記が異なる
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-015
  domain: RO
  subdomain: 慢性閉塞性肺疾患
  assertion:
    plain_statement_ja: 日本呼吸器学会の COPD ガイドライン第7版（2026年）は、日本の COPD 患者では喘息 COPD オーバーラップ（ACO）の割合が高いことを日本人の特徴の一つとし、こうした特徴が日本独自の管理の方針を形づくっているとしている。
    condition:
      guideline: COPD 診断と治療のためのガイドライン 第7版 2026（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: ACO は欧米に多く、日本ではまれである
  provenance:
    source_ref: SRC-371
    source: Sugiura H, Fujino N, Shibata Y, Muro S, Matsunaga K, Horita N, Kawayama T. The JRS guideline for the management of chronic obstructive pulmonary disease 7th edition 2026. Respir Investig 2026;64(5):101482 (Epub 2026 Jul 14)
    doi: 10.1016/j.resinv.2026.101482
    pmid: '42447589'
    pmcid: null
    url: https://doi.org/10.1016/j.resinv.2026.101482
    source_license: 未確認（ScienceDirect の取得に失敗）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 英語版の抄録で確認した内容。ACO の診断基準と治療は本文で確認が要る。日本呼吸器学会の喘息と COPD のオーバーラップ診断と治療の手引き第2版（2023年）の英語要約（Respir Investig）があり、次回以降に照合が要る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-01-00-217 (id: JlvnlyQ)'
    kokushi: 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-016
  domain: RO
  subdomain: 気管支喘息
  assertion:
    plain_statement_ja: 日本の成人喘息ガイドライン（JGL2021）では、長期管理の薬物療法を重症度に応じた4段階のステップで行い、どのステップでも毎日の吸入ステロイドを基本として、ステップが上がるほど低用量から高用量に増やす。追加薬には長時間作用性β2刺激薬、ロイコトリエン受容体拮抗薬、徐放性テオフィリン、長時間作用性抗コリン薬がある。日本の喘息死は増え続ける有病率とは逆に減り、2020年には人口10万対0.94になった。
    condition:
      guideline: 喘息予防・管理ガイドライン（JGL2021、日本アレルギー学会）
      region: 日本
    differential: null
    common_misconception: 喘息の長期管理は症状のあるときだけ短時間作用性β2刺激薬を使えばよい
  provenance:
    source_ref: SRC-374
    source: 'Niimi A, Fukunaga K, Taniguchi M, et al. Executive summary: Japanese guidelines for adult asthma (JGL) 2021. Allergol Int 2023;72(2):207-226'
    doi: 10.1016/j.alit.2023.02.006
    pmid: null
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/allergolint/72/2/72_207/_article/-char/en
    source_license: 未確認（J-STAGE の表示は「© 2023 by Japanese Society of Allergology」「JOURNAL FREE ACCESS」のみ）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 英語版の要約（抄録）で確認した内容。最新版は JGL2024 だが、英語版の要約を確認できなかったため JGL2021 を出典にした。GINA（RO-021）とは段階数や発作治療薬の扱いが異なる
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-017
  domain: RO
  subdomain: 気管支喘息
  assertion:
    plain_statement_ja: 令和6年（2024年）の人口動態統計（確定数）では、喘息による死亡は1,088人（死亡率 人口10万対0.9）だった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-369
    source: 厚生労働省. 令和6年（2024）人口動態統計（確定数）の概況 第9表 死因簡単分類別にみた性別死亡数・死亡率（人口10万対）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/toukei/saikin/hw/jinkou/kakutei24/dl/15_gaikyouR06.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 表から読み取り
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-018
  domain: RO
  subdomain: 気管支喘息
  assertion:
    plain_statement_ja: GINA 2026 は、喘息を通常は慢性の気道炎症を特徴とする不均一な疾患とし、時間とともに強さが変わる喘鳴・息切れ・胸部絞扼感・咳と、変動する呼気の気流制限によって定義している。
    condition:
      guideline: GINA 2026
      region: 国際
    differential: null
    common_misconception: 喘息の気流制限は常に固定している
  provenance:
    source_ref: SRC-375
    source: Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention, 2026 update (Strategy Report)
    doi: null
    pmid: null
    pmcid: null
    url: https://ginasthma.org/wp-content/uploads/2026/05/GINA-2026-Strategy-Report-WMS.pdf
    source_license: GINA の著作物（無断配布・改変不可。GINA サイトの利用条件の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-019
  domain: RO
  subdomain: 気管支喘息
  assertion:
    plain_statement_ja: GINA 2026 では、成人の変動する気流制限の根拠として、気管支拡張薬吸入後に FEV1 または FVC が12%以上かつ200 mL以上増えること（15%以上かつ400 mL以上ならより確実）、スパイロメトリーがなければ PEF が20%以上増えること、PEF の日内変動の平均が10%を超えることを挙げている。
    condition:
      guideline: GINA 2026
      region: 国際
    differential: null
    common_misconception: 気道可逆性がなければ喘息は否定できる
  provenance:
    source_ref: SRC-375
    source: Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention, 2026 update (Strategy Report)
    doi: null
    pmid: null
    pmcid: null
    url: https://ginasthma.org/wp-content/uploads/2026/05/GINA-2026-Strategy-Report-WMS.pdf
    source_license: GINA の著作物（無断配布・改変不可。GINA サイトの利用条件の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 表から読み取り。小児の基準は異なる（FEV1 の増加12%以上など）
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)；TBL-02-06-021 (id: JlAKpiU)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-020
  domain: RO
  subdomain: 気管支喘息
  assertion:
    plain_statement_ja: GINA 2026 は、スパイロメトリーや PEF で喘息を確認できないとき、呼気 NO（FeNO）が成人で50 ppb を超えれば2型の喘息を支持する所見になるとしている。ただし値が低くても喘息は否定できない。
    condition:
      guideline: GINA 2026
      region: 国際
    differential: null
    common_misconception: 呼気 NO が正常なら喘息ではない
  provenance:
    source_ref: SRC-375
    source: Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention, 2026 update (Strategy Report)
    doi: null
    pmid: null
    pmcid: null
    url: https://ginasthma.org/wp-content/uploads/2026/05/GINA-2026-Strategy-Report-WMS.pdf
    source_license: GINA の著作物（無断配布・改変不可。GINA サイトの利用条件の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 小児の目安は35 ppb を超える値。日本のガイドラインの呼気 NO の基準値はこの出典では確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)；TBL-02-06-022 (id: JvVZg-4)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-021
  domain: RO
  subdomain: 気管支喘息
  assertion:
    plain_statement_ja: GINA 2026 では、成人・青年の治療の推奨経路（Track 1）として、低用量吸入ステロイド・ホルモテロール配合薬を発作治療薬として使う方法（AIR、維持と発作の両方に使う MART を含む）を優先しており、短時間作用性β2刺激薬にもとづく治療に比べて重い増悪の危険を大きく減らすとしている。2026年版では、代替経路（Track 2）の Step 1 に吸入ステロイド・短時間作用性β2刺激薬配合薬を発作時に使う方法が加わった。
    condition:
      guideline: GINA 2026
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-375
    source: Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention, 2026 update (Strategy Report)
    doi: null
    pmid: null
    pmcid: null
    url: https://ginasthma.org/wp-content/uploads/2026/05/GINA-2026-Strategy-Report-WMS.pdf
    source_license: GINA の著作物（無断配布・改変不可。GINA サイトの利用条件の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本の JGL とは発作治療薬の推奨が異なる。日本での ICS・SABA 配合薬の承認状況は確認していない。Step 1〜4 の表は抽出できなかった
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-022
  domain: RO
  subdomain: 気管支喘息
  assertion:
    plain_statement_ja: GINA 2026 は、喘息の増悪時の酸素投与を SpO2 が92%未満のときに限って推奨し、投与する場合の上限を成人・青年・6〜11歳の小児で95%としている。
    condition:
      guideline: GINA 2026
      region: 国際
    differential: null
    common_misconception: 喘息発作では SpO2 にかかわらず高流量酸素を続ける
  provenance:
    source_ref: SRC-375
    source: Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention, 2026 update (Strategy Report)
    doi: null
    pmid: null
    pmcid: null
    url: https://ginasthma.org/wp-content/uploads/2026/05/GINA-2026-Strategy-Report-WMS.pdf
    source_license: GINA の著作物（無断配布・改変不可。GINA サイトの利用条件の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 経口ステロイドの用量・期間はこの出典の抽出範囲に含まれない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)；TBL-02-06-026 (id: JlAKpik)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-023
  domain: RO
  subdomain: 気管支喘息
  assertion:
    plain_statement_ja: GINA 2026 は、重症喘息に使う生物学的製剤として抗 IgE 抗体、抗 IL-5／IL-5受容体α抗体、抗 IL-4受容体α抗体、抗 TSLP 抗体を挙げ、2026年版で26週ごとに投与する長時間作用型の抗 IL-5抗体デペモキマブ（12歳以上の重症好酸球性喘息）とオマリズマブのバイオシミラーを加えた。
    condition:
      guideline: GINA 2026
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-375
    source: Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention, 2026 update (Strategy Report)
    doi: null
    pmid: null
    pmcid: null
    url: https://ginasthma.org/wp-content/uploads/2026/05/GINA-2026-Strategy-Report-WMS.pdf
    source_license: GINA の著作物（無断配布・改変不可。GINA サイトの利用条件の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 各製剤の適応基準（好酸球数・FeNO・IgE の値）は抽出できなかった。日本での各製剤の承認・保険適用は確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-024
  domain: RO
  subdomain: 気管支喘息
  assertion:
    plain_statement_ja: GINA 2026 は、咳が唯一の症状で、気管支誘発試験以外では気流制限がほとんど見られない咳喘息が成人・小児にあるとし、のちに喘鳴や気道可逆性が現れる例があること、吸入ステロイドを含む治療が有効であることを示している。
    condition:
      guideline: GINA 2026
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-375
    source: Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention, 2026 update (Strategy Report)
    doi: null
    pmid: null
    pmcid: null
    url: https://ginasthma.org/wp-content/uploads/2026/05/GINA-2026-Strategy-Report-WMS.pdf
    source_license: GINA の著作物（無断配布・改変不可。GINA サイトの利用条件の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-025
  domain: RO
  subdomain: アトピー咳嗽
  assertion:
    plain_statement_ja: 日本呼吸器学会の咳嗽・喀痰の診療ガイドライン（2019年版の英語ダイジェスト）は、3週間以内の咳を急性咳嗽、それより長い咳を遷延性・慢性咳嗽とする。急性咳嗽の多くは感染症で、ピークを過ぎた咳には抗菌薬を推奨しない。長引く乾性咳嗽の主な原因は、咳喘息、アトピー咳嗽・喉頭アレルギー、胃食道逆流、感染後咳嗽である。
    condition:
      guideline: 咳嗽・喀痰の診療ガイドライン 2019（日本呼吸器学会）
      region: 日本
    differential: null
    common_misconception: 長引く咳はまず抗菌薬で治療する
  provenance:
    source_ref: SRC-376
    source: Mukae H, Kaneko T, Obase Y, et al. The Japanese respiratory society guidelines for the management of cough and sputum (digest edition). Respir Investig 2021;59(3):270-290
    doi: 10.1016/j.resinv.2021.01.007
    pmid: '33642231'
    pmcid: null
    url: https://doi.org/10.1016/j.resinv.2021.01.007
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 英語ダイジェストの抄録で確認した内容。2025年に改訂版（咳嗽・喀痰の診療ガイドライン2025）が出ているが、内容を確認できなかったため旧版を出典にした。遷延性と慢性の境界（週数）は抄録では確認できなかった
  curriculum:
    core_curriculum: 'PS-02-07-02 (id: JkxnuQ4)；TBL-02-06-011 (id: JlAKph0)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）；医学各論 Ⅳ-3-A-②（アトピー咳嗽、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-026
  domain: RO
  subdomain: アトピー咳嗽
  assertion:
    plain_statement_ja: アトピー咳嗽は、気管支拡張薬が効かない8週以上の乾性咳嗽で、咽喉頭のイガイガ感を伴い、気道過敏性の亢進はなく、咳の感受性が亢進している。アトピー素因があり、喀痰や中枢気道に好酸球がみられ、ヒスタミン H1 受容体拮抗薬や吸入・経口ステロイドで咳が消える。
    condition:
      guideline: アトピー咳嗽の診断基準（日本の提唱）
      region: 日本
    differential: null
    common_misconception: アトピー咳嗽には気管支拡張薬がよく効く
  provenance:
    source_ref: SRC-377
    source: Ogawa H, Fujimura M, Ohkura N, Makimura K. Atopic cough and fungal allergy. J Thorac Dis 2014;6(Suppl 7):S689-S698
    doi: 10.3978/j.issn.2072-1439.2014.09.25
    pmid: null
    pmcid: null
    url: https://jtd.amegroups.org/article/view/3296/html
    source_license: CC BY-NC-ND 4.0（記事ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 提唱者グループによる総説の記述。診断基準の正式な版（学会ガイドライン）とは照合していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-02-06-011 (id: JlAKph0)'
    kokushi: 医学各論 Ⅳ-3-A-②（アトピー咳嗽、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-027
  domain: RO
  subdomain: アトピー咳嗽
  assertion:
    plain_statement_ja: 咳喘息は気管支拡張薬が効き、好酸球性炎症は末梢気道が主体で、呼気 NO はアトピー咳嗽より高い。アトピー咳嗽は気管支拡張薬が効かず、炎症は中枢気道が主体である。典型的な喘息への移行は、アトピー咳嗽で84人中1人（1.2%）、未治療の咳喘息で20人中6人（30%）、吸入ステロイドで治療した咳喘息で35人中2人（5.7%）と報告されている。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: 咳喘息もアトピー咳嗽も同じ割合で典型的な喘息に移行する
  provenance:
    source_ref: SRC-377
    source: Ogawa H, Fujimura M, Ohkura N, Makimura K. Atopic cough and fungal allergy. J Thorac Dis 2014;6(Suppl 7):S689-S698
    doi: 10.3978/j.issn.2072-1439.2014.09.25
    pmid: null
    pmcid: null
    url: https://jtd.amegroups.org/article/view/3296/html
    source_license: CC BY-NC-ND 4.0（記事ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 移行率は提唱者グループの小規模な観察研究の値で、追跡期間は出典で確認が要る
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)'
    kokushi: 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）；医学各論 Ⅳ-3-A-②（アトピー咳嗽、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-028
  domain: RO
  subdomain: 気管支拡張症
  assertion:
    plain_statement_ja: 欧州呼吸器学会（ERS）の2025年の成人気管支拡張症ガイドラインは、多くの患者への気道クリアランス法、運動耐容能が落ちた患者への呼吸リハビリテーション、増悪の危険が高い患者への長期マクロライド療法、緑膿菌の慢性感染があり増悪の危険が高い患者への長期吸入抗菌薬を、いずれも強く推奨している。一方、マクロライド以外の長期経口抗菌薬と吸入ステロイドのルーチン使用は推奨していない。
    condition:
      guideline: ERS Clinical Practice Guideline for the Management of Adult Bronchiectasis 2025
      region: 欧州
    differential: null
    common_misconception: 気管支拡張症には吸入ステロイドを一律に使う
  provenance:
    source_ref: SRC-378
    source: Chalmers JD, Haworth CS, Flume P, et al. European Respiratory Society Clinical Practice Guideline for the Management of Adult Bronchiectasis (2025)
    doi: 10.1183/13993003.01126-2025
    pmid: null
    pmcid: null
    url: https://dzl.de/guidelines/european-respiratory-society-clinical-practice-guideline-for-the-management-of-adult-bronchiectasis/
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 紹介ページで確認した推奨で、本文は未確認。DPP-1 阻害薬（ブレンソカチブ）の扱いと日本での承認状況は確認していない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-234 (id: Jlvnl0U)'
    kokushi: 医学各論 Ⅳ-2-A-①（気管支拡張症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-029
  domain: RO
  subdomain: びまん性汎細気管支炎
  assertion:
    plain_statement_ja: びまん性汎細気管支炎（DPB）は進行性の気流制限と気道感染の反復を特徴とする慢性気道疾患で、主に東アジアの人に起こり、日本の有病率は人口10万人あたり約11人とされる。1980年代からマクロライド系抗菌薬が第一選択とされてきたが、2015年の Cochrane レビューで見つかったランダム化比較試験は19人の1件だけで、質の高い根拠は乏しい。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: DPB へのマクロライド少量長期療法は大規模ランダム化比較試験で確立している
  provenance:
    source_ref: SRC-379
    source: Lin X, Lu J, Yang M, Dong BR, Wu HM. Macrolides for diffuse panbronchiolitis. Cochrane Database Syst Rev 2015;(1):CD007716
    doi: 10.1002/14651858.CD007716.pub4
    pmid: null
    pmcid: null
    url: https://www.cochrane.org/CD007716/ARI_macrolides-for-diffuse-panbronchiolitis
    source_license: Copyright © The Cochrane Collaboration（Cochrane サイトの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: レビューの著者は、診断後早期に少量マクロライドを始めて6か月以上続ける既存の指針の方針は妥当としている
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-222 (id: Jlvnlyk)'
    kokushi: 医学各論 Ⅳ-2-A-②（びまん性汎細気管支炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-030
  domain: RO
  subdomain: びまん性汎細気管支炎
  assertion:
    plain_statement_ja: びまん性汎細気管支炎の患者の多くは慢性副鼻腔炎を合併する。東アジア人に多い HLA-B54 との強い関連が報告されており、日本人患者では HLA-B*5401 が37%にみられ、健常対照の15%より多かった。
    condition:
      guideline: null
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-380
    source: 'Online Mendelian Inheritance in Man (OMIM). Panbronchiolitis, diffuse; #604809. Johns Hopkins University'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.omim.org/entry/604809
    source_license: 未確認（OMIM 本体ではなく、OMIM を出典と明記した FindZebra の転載ページで内容を確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: OMIM の記載を転載ページで確認した。OMIM 本体と原著論文は未確認。二次資料経由
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-222 (id: Jlvnlyk)'
    kokushi: 医学各論 Ⅳ-2-A-②（びまん性汎細気管支炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-031
  domain: RO
  subdomain: 閉塞性細気管支炎
  assertion:
    plain_statement_ja: 閉塞性細気管支炎は細気管支の炎症によって閉塞性換気障害を起こす病態で、細気管支の内腔が肉芽組織や滲出物で埋まる。典型的な症状は乾性咳嗽と息切れである。
    condition:
      guideline: MeSH（米国国立医学図書館）
      region: null
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-381
    source: 'National Library of Medicine. MeSH Descriptor: Bronchiolitis Obliterans (D001989)'
    doi: null
    pmid: null
    pmcid: null
    url: https://meshb.nlm.nih.gov/record/ui?ui=D001989
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 用語集の定義。造血幹細胞移植や肺移植後の閉塞性細気管支炎症候群など原因別の記述はこの出典に含まれない
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-2-A-③（閉塞性細気管支炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-032
  domain: RO
  subdomain: 気道異物
  assertion:
    plain_statement_ja: 成人の気道異物は右主気管支に多く、右主気管支が左より短く太く、気管からの角度が垂直に近いことが理由とされる。主な症状は慢性の咳（60〜85%）で、呼吸困難、片側性の喘鳴、血痰、同じ肺葉の肺炎の反復もみられる。むせた病歴がないことが多く、見逃されやすい。
    condition:
      guideline: null
      region: null
    differential: null
    common_misconception: 気道異物は必ずむせた病歴がある
  provenance:
    source_ref: SRC-383
    source: 'Chi J, Bai Y. Bronchoscopic management of airway foreign bodies in adults: a narrative educational review. Front Med 2026;13:1779715'
    doi: 10.3389/fmed.2026.1779715
    pmid: null
    pmcid: null
    url: https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1779715/full
    source_license: 未確認（取得した本文にライセンスの表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 成人を対象とした総説の記述。小児の気道異物は小児の回で扱う
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-2-A-④（気道異物、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-033
  domain: RO
  subdomain: 気道異物
  assertion:
    plain_statement_ja: 成人の気道異物の診断は CT が第一で、統合した感度は98.8%、特異度は96.6%と報告されているが、X線透過性の有機物は見逃されることがある。間接所見として過膨張（エアトラッピング）、無気肺、閉塞後肺炎がある。末梢の異物には全身麻酔下の軟性気管支鏡が選ばれることが多く（成功率約90%）、大きい・鋭い・中枢の異物には硬性気管支鏡が標準とされる。
    condition:
      guideline: null
      region: null
    differential: null
    common_misconception: CT で異物が見えなければ気道異物は否定できる
  provenance:
    source_ref: SRC-383
    source: 'Chi J, Bai Y. Bronchoscopic management of airway foreign bodies in adults: a narrative educational review. Front Med 2026;13:1779715'
    doi: 10.3389/fmed.2026.1779715
    pmid: null
    pmcid: null
    url: https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1779715/full
    source_license: 未確認（取得した本文にライセンスの表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 感度・特異度と成功率は総説が引用したメタ解析の値で、原著は未確認。二次資料経由
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-02-06-024 (id: JlAKpic)'
    kokushi: 医学各論 Ⅳ-2-A-④（気道異物、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-034
  domain: RO
  subdomain: 気腫性囊胞<ブラ、ブレブ>
  assertion:
    plain_statement_ja: 巨大気腫性ブラは片側胸郭の3分の1以上を占める含気腔で、全般的な肺気腫で壊された肺に生じる。胸部X線では気胸と紛らわしく、ブラを気胸と誤って胸腔ドレーンを入れた例が報告されているため、CT で区別する。高度の呼吸困難や感染・気胸などの合併症があれば、切除やビデオ胸腔鏡手術などの外科治療の適応となる。
    condition:
      guideline: null
      region: null
    differential: null
    common_misconception: 胸部X線で肺の外側に透亮像があれば必ず気胸として胸腔ドレーンを入れる
  provenance:
    source_ref: SRC-384
    source: Goldberg C, Carey KE. Bullous Lung Disease. West J Emerg Med 2013;14(5):450-
    doi: null
    pmid: null
    pmcid: null
    url: https://westjem.com/articles/bullous-lung-disease.html
    source_license: 未確認（記事ページに CC BY のアイコン表示はあるが、版の表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 症例報告にもとづく記述。ブラ（1 cm 以上）とブレブ（臓側胸膜内）の大きさ・位置による定義はこの出典で確認できなかった
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-216 (id: JlvnlyM)'
    kokushi: 医学各論 Ⅳ-2-B-①（気腫性囊胞<ブラ、ブレブ>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-035
  domain: RO
  subdomain: 無気肺
  assertion:
    plain_statement_ja: 無気肺は肺の全体または一部に空気が含まれない状態で、気道の閉塞、外からの圧迫、線維組織による収縮などで起こる。新生児で肺が十分に広がらない場合も含む。
    condition:
      guideline: MeSH（米国国立医学図書館）
      region: null
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-382
    source: 'National Library of Medicine. MeSH Descriptor: Pulmonary Atelectasis (D001261)'
    doi: null
    pmid: null
    pmcid: null
    url: https://meshb.nlm.nih.gov/record/ui?ui=D001261
    source_license: 米国連邦政府の著作物（NLM）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 用語集の定義。新生児の無気肺・呼吸窮迫症候群は小児の回で扱う
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-235 (id: Jlvnl0c)'
    kokushi: 医学各論 Ⅳ-2-B-②（無気肺、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RO-036
  domain: RO
  subdomain: 気管・気管支損傷
  assertion:
    plain_statement_ja: 外傷性の気管・気管支損傷は胸部・頸部外傷の0.5〜2%に起こり、鈍的外傷では75〜80%が気管分岐部から2.5 cm以内に生じる。皮下気腫が最も多い所見（最大87%）で、胸腔ドレーンを入れても大量の空気漏れが続く、または肺が再膨張しない場合は強く疑う。部位の確認と重症度の評価には気管支鏡が第一の検査で、治療は一次修復が原則である。
    condition:
      guideline: null
      region: null
    differential: null
    common_misconception: 胸部X線が正常なら気管・気管支損傷は否定できる
  provenance:
    source_ref: SRC-385
    source: 'Prokakis C, Koletsis EN, Dedeilias P, et al. Airway trauma: a review on epidemiology, mechanisms of injury, diagnosis and treatment. J Cardiothorac Surg 2014;9:117'
    doi: 10.1186/1749-8090-9-117
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/1749-8090-9-117
    source_license: 未確認（オープンアクセスの表示のみ。ライセンスの版は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 胸部X線で異常がない例が10〜20%あるとされる。数値は総説が引用した文献の値で、原著は未確認。二次資料経由
  curriculum:
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
    kokushi: 医学各論 Ⅳ-2-D-①（気管・気管支損傷、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応

| ID | subdomain | 出題基準 | コアカリ | 出典 |
|---|---|---|---|---|
| RI-001 | 感冒<かぜ症候群>、上気道炎 | 医学各論 Ⅳ-1-A-①（感冒<かぜ症候群>、上気道炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-204 (id: JlvnlxA) | SRC-350 |
| RI-002 | 気管支炎、細気管支炎 | 医学各論 Ⅳ-1-A-②（気管支炎、細気管支炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-206 (id: JlvnlxM) | SRC-350 |
| RI-003 | 気管支炎、細気管支炎 | 医学各論 Ⅳ-1-A-②（気管支炎、細気管支炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-206 (id: JlvnlxM) | SRC-350 |
| RI-004 | 気管支炎、細気管支炎 | 医学各論 Ⅳ-1-A-②（気管支炎、細気管支炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-207 (id: JlvnlxU)；TBL-01-00-416 (id: JlvnmGY) | SRC-351 |
| RI-005 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a）；医学各論 Ⅳ-1-B-③（医療・介護関連肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-212 (id: Jlvnlx0) | SRC-352 |
| RI-006 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-212 (id: Jlvnlx0) | SRC-299 |
| RI-007 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc) | SRC-353 |
| RI-008 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc) | SRC-353 |
| RI-009 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc) | SRC-354 |
| RI-010 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc) | SRC-355 |
| RI-011 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc) | SRC-353 |
| RI-012 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc) | SRC-353 |
| RI-013 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc) | SRC-353 |
| RI-014 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc) | SRC-353 |
| RI-015 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-208 (id: Jlvnlxc)；TBL-01-00-592 (id: JlvnmXc) | SRC-353 |
| RI-016 | 院内肺炎 | 医学各論 Ⅳ-1-B-②（院内肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE) | SRC-353 |
| RI-017 | 院内肺炎 | 医学各論 Ⅳ-1-B-②（院内肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE) | SRC-353 |
| RI-018 | 院内肺炎 | 医学各論 Ⅳ-1-B-②（院内肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE) | SRC-353 |
| RI-019 | 院内肺炎 | 医学各論 Ⅳ-1-B-②（院内肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE) | SRC-353 |
| RI-020 | 医療・介護関連肺炎 | 医学各論 Ⅳ-1-B-③（医療・介護関連肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE) | SRC-353 |
| RI-021 | 医療・介護関連肺炎 | 医学各論 Ⅳ-1-B-③（医療・介護関連肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE) | SRC-353 |
| RI-022 | 医療・介護関連肺炎 | 医学各論 Ⅳ-1-B-③（医療・介護関連肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE) | SRC-352 |
| RI-023 | 医療・介護関連肺炎 | 医学各論 Ⅳ-1-B-②（院内肺炎、a）；医学各論 Ⅳ-1-B-③（医療・介護関連肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-599 (id: JlvnmYE) | SRC-353 |
| RI-024 | 誤嚥性肺炎 | — | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-212 (id: Jlvnlx0) | SRC-353 |
| RI-025 | 誤嚥性肺炎 | — | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-212 (id: Jlvnlx0) | SRC-353 |
| RI-026 | 誤嚥性肺炎 | — | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-212 (id: Jlvnlx0) | SRC-353 |
| RI-027 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-617 (id: JlvnmZs) | SRC-356 |
| RI-028 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-617 (id: JlvnmZs) | SRC-357 |
| RI-029 | 市中肺炎 | 医学各論 Ⅳ-1-B-①（市中肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-617 (id: JlvnmZs) | SRC-358 |
| RI-030 | 肺真菌症 | 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs) | SRC-359 |
| RI-031 | 肺真菌症 | 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs) | SRC-359 |
| RI-032 | 肺真菌症 | 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs) | SRC-360 |
| RI-033 | 肺真菌症 | 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs) | SRC-361 |
| RI-034 | 肺真菌症 | 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs) | SRC-361 |
| RI-035 | 肺真菌症 | 医学各論 Ⅳ-1-C-①（アスペルギルス症、クリプトコックス症、カンジダ症、ニューモシスチス肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-211 (id: Jlvnlxs) | SRC-361 |
| RI-036 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-362 |
| RI-037 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-362 |
| RI-038 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-362 |
| RI-039 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-363 |
| RI-040 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-363 |
| RI-041 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-364 |
| RI-042 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-364 |
| RI-043 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-364 |
| RI-044 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-364 |
| RI-045 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-365 |
| RI-046 | 肺結核症 | 医学各論 Ⅳ-1-D-①（肺結核症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-209 (id: Jlvnlxg) | SRC-366 |
| RI-047 | 非結核性抗酸菌症 | 医学各論 Ⅳ-1-D-②（非結核性抗酸菌症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-210 (id: Jlvnlxo) | SRC-367 |
| RI-048 | 非結核性抗酸菌症 | 医学各論 Ⅳ-1-D-②（非結核性抗酸菌症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-210 (id: Jlvnlxo) | SRC-367 |
| RI-049 | インフルエンザ、サイトメガロウイルス肺炎 | 医学各論 Ⅳ-1-E-①（インフルエンザ、サイトメガロウイルス肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-619 (id: JlvnmZ4) | SRC-368 |
| RI-050 | インフルエンザ、サイトメガロウイルス肺炎 | 医学各論 Ⅳ-1-E-①（インフルエンザ、サイトメガロウイルス肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-619 (id: JlvnmZ4) | SRC-369 |
| RI-051 | インフルエンザ、サイトメガロウイルス肺炎 | — | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-620 (id: JlvnmaA) | SRC-299 |
| RI-052 | 胸膜炎 | 医学各論 Ⅳ-1-G-①（胸膜炎、a）；医学各論 Ⅳ-1-G-②（膿胸、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-213 (id: Jlvnlx4)；TBL-01-00-240 (id: Jlvnl08) | SRC-370 |
| RI-053 | 膿胸 | 医学各論 Ⅳ-1-G-②（膿胸、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-213 (id: Jlvnlx4)；TBL-01-00-240 (id: Jlvnl08) | SRC-370 |
| RO-001 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE) | SRC-371 |
| RO-002 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE) | SRC-369 |
| RO-003 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE) | SRC-371 |
| RO-004 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE) | SRC-371 |
| RO-005 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-021 (id: JlAKpiU) | SRC-372 |
| RO-006 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-021 (id: JlAKpiU) | SRC-372 |
| RO-007 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-021 (id: JlAKpiU) | SRC-373 |
| RO-008 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE) | SRC-372 |
| RO-009 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE) | SRC-372 |
| RO-010 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-025 (id: JlAKpig) | SRC-372 |
| RO-011 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-026 (id: JlAKpik) | SRC-373 |
| RO-012 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE) | SRC-372 |
| RO-013 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-02-06-026 (id: JlAKpik) | SRC-372 |
| RO-014 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE) | SRC-373 |
| RO-015 | 慢性閉塞性肺疾患 | 医学各論 Ⅳ-2-C-①（慢性閉塞性肺疾患<COPD>、喘息COPDオーバーラップ<ACO>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-215 (id: JlvnlyE)；TBL-01-00-217 (id: JlvnlyQ) | SRC-371 |
| RO-016 | 気管支喘息 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ) | SRC-374 |
| RO-017 | 気管支喘息 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ) | SRC-369 |
| RO-018 | 気管支喘息 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ) | SRC-375 |
| RO-019 | 気管支喘息 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)；TBL-02-06-021 (id: JlAKpiU) | SRC-375 |
| RO-020 | 気管支喘息 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)；TBL-02-06-022 (id: JvVZg-4) | SRC-375 |
| RO-021 | 気管支喘息 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ) | SRC-375 |
| RO-022 | 気管支喘息 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ)；TBL-02-06-026 (id: JlAKpik) | SRC-375 |
| RO-023 | 気管支喘息 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ) | SRC-375 |
| RO-024 | 気管支喘息 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ) | SRC-375 |
| RO-025 | アトピー咳嗽 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）；医学各論 Ⅳ-3-A-②（アトピー咳嗽、a） | PS-02-07-02 (id: JkxnuQ4)；TBL-02-06-011 (id: JlAKph0) | SRC-376 |
| RO-026 | アトピー咳嗽 | 医学各論 Ⅳ-3-A-②（アトピー咳嗽、a） | PS-02-07-05 (id: JkxnuRE)；TBL-02-06-011 (id: JlAKph0) | SRC-377 |
| RO-027 | アトピー咳嗽 | 医学各論 Ⅳ-3-A-①（気管支喘息、咳喘息、a）；医学各論 Ⅳ-3-A-②（アトピー咳嗽、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-217 (id: JlvnlyQ) | SRC-377 |
| RO-028 | 気管支拡張症 | 医学各論 Ⅳ-2-A-①（気管支拡張症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-234 (id: Jlvnl0U) | SRC-378 |
| RO-029 | びまん性汎細気管支炎 | 医学各論 Ⅳ-2-A-②（びまん性汎細気管支炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-222 (id: Jlvnlyk) | SRC-379 |
| RO-030 | びまん性汎細気管支炎 | 医学各論 Ⅳ-2-A-②（びまん性汎細気管支炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-222 (id: Jlvnlyk) | SRC-380 |
| RO-031 | 閉塞性細気管支炎 | 医学各論 Ⅳ-2-A-③（閉塞性細気管支炎、a） | PS-02-07-05 (id: JkxnuRE) | SRC-381 |
| RO-032 | 気道異物 | 医学各論 Ⅳ-2-A-④（気道異物、a） | PS-02-07-05 (id: JkxnuRE) | SRC-383 |
| RO-033 | 気道異物 | 医学各論 Ⅳ-2-A-④（気道異物、a） | PS-02-07-05 (id: JkxnuRE)；TBL-02-06-024 (id: JlAKpic) | SRC-383 |
| RO-034 | 気腫性囊胞<ブラ、ブレブ> | 医学各論 Ⅳ-2-B-①（気腫性囊胞<ブラ、ブレブ>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-216 (id: JlvnlyM) | SRC-384 |
| RO-035 | 無気肺 | 医学各論 Ⅳ-2-B-②（無気肺、b） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-235 (id: Jlvnl0c) | SRC-382 |
| RO-036 | 気管・気管支損傷 | 医学各論 Ⅳ-2-D-①（気管・気管支損傷、b） | PS-02-07-05 (id: JkxnuRE) | SRC-385 |

## 4. 未解決事項（担当の目安つき）

| # | 内容 | 対象カード | 担当の目安 |
|---|---|---|---|
| 1 | PMID・ライセンスの API 照合。PMID が確認できたのは SRC-352・371・376 だけ。BMC（SRC-354・355・385）、Frontiers（SRC-383）、EID（SRC-367）、Allergol Int（SRC-374）、Respir Investig（SRC-352・371・376）、ERJ（SRC-378）の license 欄を Crossref で確認し、`source_class` を確定する | 全般 | Claude Code（`scripts/ncbi_crossref.py`） |
| 2 | A-DROP・I-ROAD の項目表と、市中肺炎の経験的治療の薬剤名が、成人肺炎診療ガイドライン2024 の学会 PDF から抽出できなかった。A-DROP は CC BY の論文2本（SRC-354・355）で補ったが、I-ROAD の項目はカードがない | RI-009〜011、RI-017 | 監修者（呼吸器）＋補完回 |
| 3 | SRC-355 の表では BUN の基準が 210 mg/dL と印刷されている（誤植と判断し、カードでは SRC-354 の 210 mg/L＝21 mg/dL を使った） | RI-009、RI-010 | 監修者 |
| 4 | 高齢者の肺炎球菌の定期接種のワクチン変更（2026年4月から PCV20）は札幌市保健所のページで確認した。厚生労働省の通知・告示で確認し、出典を差し替える | RI-028 | Claude Code（出典の差し替え提案）→ 監修者 |
| 5 | COPD ガイドライン第7版（2026年）は英語版の抄録しか確認できず、診断・病期・治療の数値は第6版（2022年）を出典にした。第7版で変わった点（Rome 提案の扱い、増悪時のステロイドの期間など）を確認する | RO-005〜RO-013 | 監修者（呼吸器） |
| 6 | 喘息は JGL2024 が最新だが、英語版の要約を確認できず JGL2021 の要約を出典にした。GINA 2026 の Step 1〜4 の表、重症喘息の生物学的製剤の適応基準は抽出できなかった。日本での生物学的製剤（デュピルマブの COPD への適応を含む）の承認状況も未確認 | RO-004、RO-016、RO-021、RO-023 | 監修者＋補完回 |
| 7 | 咳嗽・喀痰の診療ガイドラインは2025年版が出ているが、2019年版の英語ダイジェストの抄録を出典にした。遷延性・慢性咳嗽の週数の区分は確認できていない | RO-025 | 補完回（RX の咳嗽と合わせて第13回で扱う案） |
| 8 | ERS の気管支拡張症ガイドライン2025 は紹介ページでの確認で、掲載誌の巻号・本文・ライセンスが未確認。ブレンソカチブ（DPP-1 阻害薬）の推奨と国内承認も未確認 | RO-028 | Claude Code（書誌照合）→ 監修者 |
| 9 | DPB の HLA-B54 の記述は OMIM の転載ページ（FindZebra）で確認した。OMIM 本体か原著で確認する | RO-030 | Claude Code |
| 10 | ブラ（1 cm 以上）とブレブ（臓側胸膜内）の大きさ・位置による定義の出典が取れなかった（Fleischner 用語集2024 は書誌だけ確認、本文は取得できず。DOI 10.1148/radiol.232558、PMID 38411514、PMCID PMC10902601） | RO-034 | 補完回 |
| 11 | COVID-19 肺炎の治療（ステロイド・抗ウイルス薬）は、厚生労働省の診療の手引き第10.1版・NIH のガイドラインとも本文を取得できず、カードを作っていない（死亡数の RI-051 のみ） | — | 感染症（Ⅻ）の回 |
| 12 | 米国の市中肺炎ガイドライン（ATS 2025 更新版：Am J Respir Crit Care Med 2026;212(1):24-44、DOI 10.1164/rccm.202507-1692ST、PMID 40679934）は抄録までしか確認できず、推奨の中身のカードがない。日本の A-DROP と欧米の CURB-65・PSI の対比カードも未作成 | — | 補完回 |
| 13 | 結核登録者情報調査年報は厚生労働省の公表ページの数値で、集計結果の PDF 本体は未確認 | RI-036〜RI-038 | Claude Code |
| 14 | 細気管支炎のカード（RI-004）は RS ウイルスの予防の推奨で、細気管支炎の診断・治療（支持療法）のカードがない | RI-004 | 補完回 |

## 5. 次回への引き継ぎ

### 5-1. 欠番
- なし（RI-001〜RI-053、RO-001〜RO-036 は連番）。

### 5-2. カードのない出題基準の小項目（第11回の範囲）
- レベル b：Ⅳ-2-A-⑤ 気管・気管支の狭窄・閉塞、Ⅳ-2-D-② 肺損傷
- レベル c：Ⅳ-1-F-① 吸虫症・線虫症（CDC の肺吸虫症のページは確認済み：https://www.cdc.gov/paragonimus/hcp/clinical-overview/index.html。件数の上限のため作らなかった）、Ⅳ-1-G-③ 縦隔炎、Ⅳ-2-B-③ 肺分画症（MeSH D001998 は確認済み：https://meshb.nlm.nih.gov/record/ui?ui=D001998）
- レベル a のうち内容が薄いもの：Ⅳ-1-C-① のカンジダ症、Ⅳ-1-E-① のサイトメガロウイルス肺炎（カードなし）。Ⅳ-1-G-① 胸膜炎は胸膜感染症の1件だけで、結核性胸膜炎・Light の基準は第13回 RX で扱う想定
- 出題基準の番号を付けていないカード：RI-024〜RI-026（誤嚥性肺炎。表に独立した項目がないため `kokushi: null`、コアカリ TBL-01-00-212）、RI-051（COVID-19）

### 5-3. 重複を避ける範囲（第12・13回へ）
- ABPA（Ⅳ-3-A-④）は IL で扱う。RI-030・RI-031 はアスペルギルス症の病型としてアレルギー性の病型に触れただけ。
- 胸水の鑑別（Light の基準）・呼吸機能検査・呼気 NO・酸素療法の一般論は RX（第13回）で扱う。RO-019・RO-020・RO-011・RO-013・RO-022 は COPD・喘息の診断基準・治療の中での記述にとどめた。
- 咳嗽の持続期間による分類は RX の主要症候と重なる。RO-025 は咳嗽ガイドラインの記述として作った。
- 気胸・縦隔気腫・肋骨骨折は PL（第13回）で扱う。RO-034（ブラ）と RO-036（気管・気管支損傷）は気胸の治療に触れていない。
- 喫煙と禁煙治療の詳細は RX で扱う。RO-009 は COPD での禁煙の位置づけだけ。
- 結核・インフルエンザ・COVID-19・肺炎球菌ワクチンの全身の感染症としての内容は感染症（Ⅻ）で扱う。

### 5-4. 扱った出典（第12・13回で再利用できるもの）
- SRC-299・SRC-369：令和6年人口動態統計（確定数）第8表・第9表。間質性肺疾患の死亡（24,395人、人口10万対20.3）は第9表に載っており、IL で SRC-369 を再利用できる。
- SRC-370：BTS 胸膜疾患ガイドライン2023（気胸・悪性胸水の推奨も含む。PL・LC で再利用可）。
- SRC-371・SRC-372・SRC-373：COPD（第7版抄録、第6版サマリー、GOLD 2026 Pocket Guide）。GOLD 2026 は肺癌検診（喫煙歴のある人への年1回の低線量 CT）にも触れており、LC で参照できる。
- SRC-375：GINA 2026（呼気 NO・ピークフローの基準は RX で再利用可）。
- SRC-361：米国 HIV 日和見感染症ガイドライン（ニューモシスチス肺炎）。
- 今回確認したが使わなかった出典：GOLD 2026 Report 本体 v1.3（https://goldcopd.org/wp-content/uploads/2025/12/GOLD-REPORT-2026-v1.3-8Dec2025_WMV.pdf、第1章まで抽出可）、Fleischner 用語集2024（書誌のみ）、ATS CAP 2025（書誌と抄録のみ）、ATS/ERS/ESCMID/IDSA の NTM 治療ガイドライン2020（Eur Respir J 2020;56(1):2000535、DOI 10.1183/13993003.00535-2020、抄録のみ）。
