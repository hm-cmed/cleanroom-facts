# 第67回 成果物（ブラッシュアップA 最終回：精神（Ⅱ）・循環器（Ⅴ）・消化器（Ⅵ）・内分泌（Ⅹ）・免疫（Ⅺ））

- 依頼文：docs/tasks/round62_BRUSHUP_A.md の「第67回」（仕様 specs/round67.yaml）
- 対象：28項目（すべてレベル a）
- 件数：29件（SZ-009〜010、AX-020、AR-038〜042、IH-031、MP-043〜044、HT-024〜025、ES-094〜095、AB-117〜119、IN-114、BP-076〜077、LV-112、IE-018、TH-033〜034、DM-039〜040、SA-023〜024）。偽痛風は臨床像と急性発作の治療で出典が分かれるため2件で担う
- 新規出典：15件（SRC-4961〜4975）。未使用：SRC-4976〜5060
- 既存カードは直さず、各項目に依頼文の表の「2件目に書く側面」の新しいカードを足した

## 判断・申し送り（要点）

- **睡眠時無呼吸症候群（HT-024）は総論カードを作らなかった**：依頼表の側面（定義・診断・重症度・治療の総論）は、取り込み済みの第Ⅱ章の PH-009〜011（＋重症度は PL-020）が既に担っており、新作すると実質重複になるため。PH 群の kokushi は Ⅱ-4-B-② のみで Ⅴ-7-B-④ が未付与であり、本来の形は PH-009〜011 への Ⅴ-7-B-④ の番号追加である（既存カードの編集は作り手の範囲外のため申し送りとする。対応表は §5）。HT-024 は、既存カードのいずれも具体像を述べていない「高血圧との合併」に厳密に限定した狭義カードとした
- MP-043・044 は、既存カードの出典（SRC-252、2015年版の要約）ではなく現行の一次ガイドライン（2025 ESC 心筋炎・心膜炎ガイドライン、SRC-4965）を採用した
- MP・AB・IN・LV・SA の開始番号は仕様で null のため、前の回の納品済みの続き（MP-043、AB-117、IN-114、LV-112、SA-023）からとした

## 1. 出典ホワイトリスト（この回のカードが使う出典）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-094 | 日本肝胆膵外科学会ほか編『TG18新基準掲載 急性胆管炎・胆嚢炎診療ガイドライン2018（第3版）』医学図書出版、2018 | なし | なし | 著作権は著者・出版社に帰属（Mindsは私的利用の範囲に限ると明記） | RESTRICTED | 既存出典（出典マスター登録済み。第67回で再利用） |
| SRC-157 | Sartelli M, Chichom-Mefire A, Labricciosa FM, et al. The management of intra-abdominal infections from a global perspective: 2017 WSES guidelines for management of intra-abdominal infections. World J Emerg Surg 2017;12:29 | 10.1186/s13017-017-0141-6 | null | CC BY 4.0 | OPEN | 既存カード AB-075・076 の出典（出典マスター登録済み）。全文で二次性腹膜炎の原因（消化管穿孔など）、臨床評価に基づく診断、感染源制御を含む治療の柱と、WISS 研究の感染源の内訳の表を確認 |
| SRC-158 | HerniaSurge Group. International guidelines for groin hernia management. Hernia 2018;22:1-165 | 10.1007/s10029-017-1668-x | null | CC BY-NC 4.0 | RESTRICTED | 既存カード AB-069・073 の出典（出典マスター登録済み）。PMC 全文（PMC5809582）で第17章（大腿ヘルニア）と全体要約（嵌頓・絞扼の危険因子、女性の緊急修復の割合）を確認 |
| SRC-170 | Ono K, Iwasaki YK, Akao M, et al. JCS/JHRS 2020 Guideline on Pharmacotherapy of Cardiac Arrhythmias. J Arrhythm 2022;38:833-973（Circ J 2022;86:1790-1924 と同時掲載） | 10.1002/joa3.12714 | 36524037 | CC BY 4.0（Crossref の license 欄） | OPEN | 既存出典（出典マスター登録済み。第67回で再利用） |
| SRC-902 | Ross DS, Burch HB, Cooper DS, Greenlee MC, Laurberg P, Maia AL, Rivkees SA, Samuels M, Sosa JA, Stan MN, Walter MA. 2016 American Thyroid Association Guidelines for Diagnosis and Management of Hyperthyroidism and Other Causes of Thyrotoxicosis. Thyroid. 2016;26(10):1343-1421. | 10.1089/thy.2016.0229 | 27521067 | CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) | OPEN | 既存出典（出典マスター登録済み。第67回で再利用） |
| SRC-3746 | Akashiba T, Inoue Y, Uchimura N, et al. Sleep Apnea Syndrome (SAS) Clinical Practice Guidelines 2020. Sleep Biol Rhythms. 2022;20(1):5-37. | 10.1007/s41105-021-00353-6 | 38469064 | CC BY 4.0（論文ページの Open Access 表示で確認） | OPEN | 既存出典（出典マスター登録済み。第67回で再利用） |
| SRC-3974 | Jophlin LL, Singal AK, Bataller R, Wong RJ, Sauer BG, Terrault NA, Shah VH. ACG Clinical Guideline: Alcohol-Associated Liver Disease. Am J Gastroenterol. 2024;119(1):30-54 | 10.14309/ajg.0000000000002572 | 38174913 | CC 表示なし（購読誌。著者原稿が PMC に収載） | RESTRICTED | 既存出典（出典マスター登録済み。第67回で再利用） |
| SRC-4245 | Coccolini F, Coimbra R, Ordonez C, et al. Liver trauma: WSES 2020 guidelines. World J Emerg Surg. 2020;15:24 | 10.1186/s13017-020-00302-7 | 32228707 | CC BY 4.0（ジャーナルの OA ライセンス） | OPEN | 既存カード AB-109 の出典（出典マスター登録済み）。PMC 全文（PMC7106618）でステートメント一覧表（診断・NOM・手術的管理）と手術管理の節（ダメージコントロール手術での切除回避・パッキング・一時的閉腹）を確認 |
| SRC-4379 | Takase B, Ikeda T, Shimizu W, et al; Japanese Circulation Society and Japanese Heart Rhythm Society Joint Working Group. JCS/JHRS 2022 Guideline on Diagnosis and Risk Assessment of Arrhythmia. J Arrhythm. 2024;40(4):655-752. | 10.1002/joa3.13052 | 39139890 | CC表示なし | RESTRICTED | 既存出典（出典マスター登録済み。第67回で再利用） |
| SRC-4381 | Ohya Y, et al. The Japanese Society of Hypertension Guidelines for the management of elevated blood pressure and hypertension 2025 (JSH2025). Hypertens Res. 2026;49(1):9-235. | 10.1038/s41440-025-02462-y | 41476123 | CC表示なし（購読誌） | RESTRICTED | 既存出典（出典マスター登録済み。第67回で再利用） |
| SRC-4961 | World Health Organization. ICD-10: International Statistical Classification of Diseases and Related Health Problems, 10th Revision, Volume 1: Tabular List. Chapter V: Mental and Behavioural Disorders, F20.1 Hebephrenic Schizophrenia. Geneva: World Health Organization | なし | なし | © World Health Organization（All rights reserved、CC 表示なし） | RESTRICTED | ICD-10 第1巻（分類表）の F20.1 定義文を、同一本文を掲載する NHS の ICD-10 Class Browser（第5版・第1巻）とタイ保健省掲載の ICD-10 本文ページの2か所で一致を確認 |
| SRC-4962 | Rogers JP, Oldham MA, Fricchione G, et al. Evidence-based consensus guidelines for the management of catatonia: Recommendations from the British Association for Psychopharmacology. J Psychopharmacol. 2023;37(4):327-369 | 10.1177/02698811231158232 | 37039129 | CC BY 4.0（PMC の本文ページのライセンス表示で確認） | OPEN | PMC 全文で臨床像（Clinical features の節と DSM-5-TR／ICD-11 項目表）、悪性症候群の節（ドパミン拮抗薬への曝露、発熱・筋強剛・自律神経機能障害）、第一選択治療の推奨（ベンゾジアゼピン系薬および／または ECT、無効時は ECT）を確認 |
| SRC-4963 | O'Donnell ML, Agathos JA, Metcalf O, et al. Adjustment Disorder: Current Developments and Future Directions. Int J Environ Res Public Health. 2019;16(14):2537 | 10.3390/ijerph16142537 | 31315203 | CC BY 4.0（MDPI の論文ページのライセンス表示で確認） | OPEN | MDPI 全文で診断基準の比較（DSM-5：発症3か月以内・ストレス因消退後6か月を超えて持続しない、ICD-11：発症1か月以内）と症状（とらわれ、適応の失敗）、治療の節（2018年の系統的レビューで心理療法・薬物療法ともエビデンスの質は低〜非常に低い）を確認。PMID・PMCID は PMC のレコードで確認 |
| SRC-4964 | Theofilis P, Antonopoulos AS, Sagris M, Papanikolaou A, Oikonomou E, Tsioufis K, Tousoulis D. Silent Myocardial Ischemia: From Pathophysiology to Diagnosis and Treatment. Biomedicines. 2024;12(2):259. | 10.3390/biomedicines12020259 | 38397860 | CC BY 4.0（誌のオープンアクセス表示） | OPEN | PubMed レコード（PMID 38397860、題名・Review 種別）で書誌を確認し、全文を開いて定義（狭心症や同等症状を伴わない客観的な虚血の証明）・頻度（一般人口で2〜4%、虚血発作の50〜70%が無症候）・Cohn の3分類・検出方法（運動負荷試験・負荷心エコー・SPECT・PET・心臓 MRI、無症候の一般集団へのスクリーニングは ESC 慢性冠症候群ガイドラインで非推奨）・予後（無症候性心筋梗塞と心臓突然死の関連）・管理（薬物治療が基本、血行再建は予後改善が見込まれる解剖学的条件）を確認。出典マスターと第61〜66回の納品分に DOI・PMID の重複なし |
| SRC-4965 | Schulz-Menger J, Collini V, Gröschel J, et al; ESC Scientific Document Group. 2025 ESC Guidelines for the management of myocarditis and pericarditis. Eur Heart J. 2025;46(40):3952-4041. | 10.1093/eurheartj/ehaf192 | 40878297 | © The European Society of Cardiology 2025（All rights reserved） | RESTRICTED | PubMed レコード（PMID 40878297、DOI と対応）で書誌を確認し、ガイドライン全文（第11.7節 心囊液貯留・第11.8節 心タンポナーデ、表10・表17）を開いて、貯留の大きさの区分（中等量10〜20 mm・大量20 mm 超）、原因の内訳（特発性 最大50%、悪性腫瘍10〜32%、感染症15〜30%、医原性15〜20%、結合組織病5〜15%、結核流行地域では結核が60%超）、無症候性貯留の経過観察（中等量以上は6か月ごと、慢性特発性大量貯留のタンポナーデ発症は年2.2%）と、タンポナーデの臨床徴候（Beck の三徴・奇脈）と心エコー所見（右房の虚脱・右室の拡張期虚脱・下大静脈の拡張と呼吸性変動の減弱ほか、表17から読み取り）を確認。出典マスターと第61〜66回の納品分に重複なし |
| SRC-4966 | Fujishiro M, Iguchi M, Ono S, et al. Guidelines for endoscopic management of nonvariceal upper gastrointestinal bleeding (second edition). Dig Endosc. 2025;37(5):447-469 | 10.1111/den.15019 | null | CC 表示なし（日本消化器内視鏡学会のガイドライン） | RESTRICTED | 2026-11-01 に出版社（Wiley）の全文ページで CQ 一覧表（CQ3・CQ4・CQ11）と Mallory-Weiss 症候群の節の本文を確認。DOI は出版社ページで確認。PMID は確認できず null。出典マスターに DOI の登録がないことを確認 |
| SRC-4967 | Daly S, Kumar SS, Collings AT, et al. SAGES guidelines for the surgical treatment of hiatal hernias. Surg Endosc. 2024;38(9):4765-4775 | 10.1007/s00464-024-11092-3 | 39080063 | CC 表示なし（Springer、学会ガイドライン） | RESTRICTED | PubMed レコードで書誌・PMID・DOI を照合し、SAGES 公式サイトのガイドライン本文で I〜IV 型の定義と無症状の II〜IV 型への対応（KQ2）、噴門形成術の条件付き推奨（KQ3）を確認。出典マスターに DOI・PMID とも登録がないことを確認 |
| SRC-4968 | Lohsiriwat V. Hemorrhoids: From basic pathophysiology to clinical management. World J Gastroenterol. 2012;18(17):2009-2017 | 10.3748/wjg.v18.i17.2009 | 22563187 | 未確認（PMC 収載版・出版社ページとも CC 表示なし） | UNKNOWN | PubMed レコードと PMC 全文（PMC3342598）で書誌・識別子・Goligher 分類・症状・グレード別治療の表を確認。出典マスターに DOI・PMID とも登録がないことを確認 |
| SRC-4969 | Chen LT, Vogel A, Hsu C, et al. Pan-Asian adapted ESMO Clinical Practice Guidelines for the diagnosis, treatment and follow-up of patients with biliary tract cancer. ESMO Open. 2024;9(8):103647 | 10.1016/j.esmoop.2024.103647 | 39232586 | CC BY-NC-ND 4.0（PMC のライセンス表示で確認） | RESTRICTED | PMC 全文で推奨一覧（Table 1）と本文（補助療法の根拠、分子プロファイリング等）を確認 |
| SRC-4970 | Karrento K, Rosen JM, Gelfand AA, et al. North American Society for Pediatric Gastroenterology, Hepatology, and Nutrition 2025 guidelines for management of cyclic vomiting syndrome in children. J Pediatr Gastroenterol Nutr. 2025;80(6):1028-1061 | 10.1002/jpn3.70020 | 40223700 | Wiley（CC表示を確認できず） | UNKNOWN | PubMed レコードで DOI・PMID を確認し、ガイドライン全文 PDF（学会サイト）で全16推奨の内容と強さを確認 |
| SRC-4971 | Caturegli P, De Remigis A, Rose NR. Hashimoto thyroiditis: Clinical and diagnostic criteria. Autoimmun Rev. 2014;13(4-5):391-397 | 10.1016/j.autrev.2014.01.007 | 24434360 | Elsevier（購読制、CC表示なし） | RESTRICTED | 出版社ページの抄録で診断の要点を確認し、PMID は引用文献の PMID 表示と DOI の対応で確認 |
| SRC-4972 | Kraut JA, Madias NE. Lactic acidosis. N Engl J Med. 2014;371(24):2309-2319 | 10.1056/NEJMra1309483 | 25494270 | Massachusetts Medical Society（CC表示なし） | RESTRICTED | 全文 PDF（大学リポジトリ収載版）で分類・診断・治療を確認。PMID は PubMed レコードの DOI との対応で確認。出典マスターの Kraut & Madias 2010（Nat Rev Nephrol）とは別文献 |
| SRC-4973 | Kanasaki K, Ueki K, Nangaku M. Diabetic kidney disease: the kidney disease relevant to individuals with diabetes. Clin Exp Nephrol. 2024;28(12):1213-1220 | 10.1007/s10157-024-02537-z | 39031296 | CC BY 4.0 | OPEN | PMC 全文で DKD の概念定義・鑑別の進め方・病期分類の位置づけを確認。PMID・PMCID は PMC ページで確認 |
| SRC-4974 | Rosenthal AK, Ryan LM. Calcium pyrophosphate deposition disease. N Engl J Med. 2016;374(26):2575-2584 | 10.1056/NEJMra1511117 | 27355536 | Massachusetts Medical Society（著者稿が PMC に収載） | RESTRICTED | PMC 収載の著者稿全文で臨床像を確認。PMID・PMCID は PMC ページで確認 |
| SRC-4975 | Zhang W, Doherty M, Pascual E, et al. EULAR recommendations for calcium pyrophosphate deposition. Part II: Management. Ann Rheum Dis. 2011;70(4):571-575 | 10.1136/ard.2010.139360 | 21257614 | BMJ（CC表示なし） | RESTRICTED | 誌面 PDF の DOI 表示と抄録で推奨内容を確認。PMID は引用文献の PubMed リンク表示と DOI の対応で確認 |

## 2. 事実カード（YAML）

```yaml
- id: SZ-009
  domain: SZ
  subdomain: 破瓜型統合失調症
  assertion:
    plain_statement_ja: 破瓜型統合失調症は ICD-10（F20.1）における統合失調症の一亜型で、感情の変化が目立ち、気分は浅薄で場にそぐわず、思考は解体して会話はまとまりを欠く。妄想や幻覚はあっても一過性で断片的にとどまり、行動は無責任で予測しがたく、衒奇的な振る舞いが多く、社会的孤立に陥りやすい。通常は青年期から若年成人に診断される。感情の平板化や意欲の喪失といった陰性症状が急速に進展するため、予後は一般に不良である。
    condition:
      region: 国際
      対象: 破瓜型統合失調症（ICD-10 F20.1）の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4961
    source: 'World Health Organization. ICD-10: International Statistical Classification of Diseases and Related Health Problems, 10th Revision, Volume 1: Tabular List. Chapter V: Mental and Behavioural Disorders, F20.1 Hebephrenic Schizophrenia. Geneva: World Health Organization'
    doi: null
    pmid: null
    pmcid: null
    url: https://classbrowser.nhs.uk/ICD-10-5TH-Edition/vol1/block-f20-f29.htm
    source_license: © World Health Organization（All rights reserved、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは ICD-10 第1巻（分類表）の F20.1 の定義文に基づく。依頼表の側面に挙げられた潜行性の発症については、採用した定義文に発症様式の明記がないため主張に含めなかった。亜型分類そのものの位置づけ（DSM-5・ICD-11 では不採用）は既存カード SZ-001 が担う。
  curriculum:
    kokushi: 医学各論 Ⅱ-2-B-②（破瓜型統合失調症、a）
    core_curriculum: 'PS-02-17-02 (id: JkxnuTw)；PS-02-17-03 (id: JkxnuT0)；PS-02-17-04 (id: JkxnuT4)；TBL-01-00-538 (id: JlvnmUA)；TBL-02-16-005 (id: JlAKpzE)；PS-02-17-05 (id: JkxnuT8)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: SZ-010
  domain: SZ
  subdomain: 緊張型統合失調症
  assertion:
    plain_statement_ja: 緊張型統合失調症の実体である緊張病症候群では、昏迷、カタレプシー（受動的にとらされた姿勢の保持）、蝋屈症、無言症、拒絶症、姿勢保持、衒奇症、常同症、興奮、しかめ面、反響言語・反響動作などの精神運動性の徴候がみられる。悪性症候群はドパミン拮抗薬（抗精神病薬など）への曝露後に生じるまれな反応で、意識の変化、著しい筋強剛、発熱、自律神経機能障害を伴い、緊張病の悪性型とは臨床的に区別が難しいことが多い。緊張病の治療の第一選択はベンゾジアゼピン系薬および／または修正型電気けいれん療法で、ベンゾジアゼピン系薬で寛解が得られない場合は電気けいれん療法を行う。
    condition:
      region: 国際
      対象: 緊張病症候群を呈する患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4962
    source: 'Rogers JP, Oldham MA, Fricchione G, et al. Evidence-based consensus guidelines for the management of catatonia: Recommendations from the British Association for Psychopharmacology. J Psychopharmacol. 2023;37(4):327-369'
    doi: 10.1177/02698811231158232
    pmid: '37039129'
    pmcid: PMC10101189
    url: https://doi.org/10.1177/02698811231158232
    source_license: CC BY 4.0（PMC の本文ページのライセンス表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典は英国精神薬理学会（BAP）の緊張病ガイドライン（2023年）で、緊張病は統合失調症に限らず気分障害や身体疾患にも伴う症候群として扱われている。本カードは緊張型統合失調症の項目として、緊張病症候群の一般像を記載した。薬剤の国内承認：ベンゾジアゼピン系薬の代表であるロラゼパムは国内で承認されているが、効能・効果は神経症等における不安・緊張等であり、緊張病への使用は適応外となる。修正型電気けいれん療法は国内で保険適用のある治療手技である。
  curriculum:
    kokushi: 医学各論 Ⅱ-2-B-③（緊張型統合失調症、a）
    core_curriculum: 'PS-02-17-02 (id: JkxnuTw)；PS-02-17-03 (id: JkxnuT0)；PS-02-17-04 (id: JkxnuT4)；TBL-01-00-538 (id: JlvnmUA)；TBL-02-16-005 (id: JlAKpzE)；PS-02-17-05 (id: JkxnuT8)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: AX-020
  domain: AX
  subdomain: 適応障害
  assertion:
    plain_statement_ja: 適応障害は、同定可能な心理社会的ストレス因への不適応な情動面・行動面の反応で、ストレス因の強さに不釣り合いな苦痛や、社会的・職業的機能の障害として現れる。DSM-5 では症状はストレス因から3か月以内に始まり、ストレス因とその結果が消退した後は6か月を超えて持続しないとされる（ICD-11 では発症はストレス因から1か月以内とされる）。症状には、ストレス因へのとらわれ（反芻や過度の心配）、睡眠障害や集中困難といった適応の失敗、不安や抑うつなどが含まれる。治療については心理的介入を中心に研究されてきたが、2018年の系統的レビューでは心理療法・薬物療法のいずれもエビデンスの質は低〜非常に低く、確立した薬物療法はない。
    condition:
      region: 国際
      対象: 適応障害患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4963
    source: 'O''Donnell ML, Agathos JA, Metcalf O, et al. Adjustment Disorder: Current Developments and Future Directions. Int J Environ Res Public Health. 2019;16(14):2537'
    doi: 10.3390/ijerph16142537
    pmid: '31315203'
    pmcid: PMC6678970
    url: https://doi.org/10.3390/ijerph16142537
    source_license: CC BY 4.0（MDPI の論文ページのライセンス表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 経過の期間（DSM-5 の3か月・6か月、ICD-11 の1か月）は本総説の診断基準の比較記述と表で確認した。依頼表の側面にある「支持的精神療法・環境調整が中心で、薬物療法は補助的」という位置づけのうち、環境調整への明示的な言及は本総説では確認できなかったため、治療はエビデンスの状況として記載した。適応障害を効能・効果とする国内承認薬はない。概念面（診断概念への批判と ICD-11／DSM-5 の定義の差異）は既存カード AX-016 が担う。
  curriculum:
    kokushi: 医学各論 Ⅱ-3-C-②（適応障害<適応反応症>、a）
    core_curriculum: 'PS-02-17-05 (id: JkxnuT8)；PS-02-17-02 (id: JkxnuTw)；TBL-02-16-002 (id: JlAKpy0)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: AR-038
  domain: AR
  subdomain: 発作性上室頻拍
  assertion:
    plain_statement_ja: 発作性上室頻拍は機序により、房室結節リエントリー性頻拍、副伝導路を介する房室リエントリー性頻拍、心房頻拍に分類される。発作が短く自然に収まる場合は予防療法は必ずしも必要ないが、急性期治療を要する発作には、根治が期待できるカテーテルアブレーションが第一選択の予防療法として推奨され（クラスI、レベルB）、成功率は90%以上とされる。アブレーションを希望しない場合や不成功の場合は、経口のベラパミル、ジルチアゼム、β遮断薬による薬物予防が推奨される（クラスI、レベルA）。
    condition:
      region: 日本
      対象: 発作性上室頻拍の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-170
    source: Ono K, Iwasaki YK, Akao M, et al. JCS/JHRS 2020 Guideline on Pharmacotherapy of Cardiac Arrhythmias. J Arrhythm 2022;38:833-973（Circ J 2022;86:1790-1924 と同時掲載）
    doi: 10.1002/joa3.12714
    pmid: '36524037'
    pmcid: PMC9745564
    url: https://doi.org/10.1002/joa3.12714
    source_license: CC BY 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典は JCS/JHRS 2020 不整脈薬物治療ガイドライン第IV章で、推奨のクラスとレベルは同ガイドラインの表16から読み取った。薬剤の国内承認：ベラパミル（経口）は頻脈性不整脈（発作性上室性頻拍を含む）に適応がある。ジルチアゼムは注射剤に頻脈性不整脈の適応があり、経口剤の適応は狭心症・本態性高血圧症である。β遮断薬の不整脈への適応は薬剤ごとに異なる。発作停止法は既存カード AR-021、WPW 症候群側のアブレーションは AR-022・AR-023 が担う。
  curriculum:
    kokushi: 医学各論 Ⅴ-1-A-②（発作性上室頻拍、a）
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-168 (id: Jlvnlsw)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: AR-039
  domain: AR
  subdomain: 心房粗動
  assertion:
    plain_statement_ja: 心房粗動は心房のマクロリエントリーによる頻拍で、心房拍数は規則的で 240〜440/分（典型例では約300/分）である。通常型（下大静脈‐三尖弁間峡部依存性で反時計回りのもの）では、下壁誘導で陰性の鋸歯状の粗動波がみられ、V1 誘導の粗動波は陽性である。血行動態が安定した心房粗動のレートコントロールには、ジルチアゼムまたはベラパミルの静注・経口投与が推奨される（クラスI、レベルA）。抗凝固療法の考え方は心房細動に準じ、除細動を行う場合は施行前3週間と施行後少なくとも4週間の抗凝固を行う。
    condition:
      region: 日本
      対象: 心房粗動の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-170
    source: Ono K, Iwasaki YK, Akao M, et al. JCS/JHRS 2020 Guideline on Pharmacotherapy of Cardiac Arrhythmias. J Arrhythm 2022;38:833-973（Circ J 2022;86:1790-1924 と同時掲載）
    doi: 10.1002/joa3.12714
    pmid: '36524037'
    pmcid: PMC9745564
    url: https://doi.org/10.1002/joa3.12714
    source_license: CC BY 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典は JCS/JHRS 2020 不整脈薬物治療ガイドライン第VI章2節で、心房拍数の範囲と粗動波の所見は病態生理の記述、推奨のクラスとレベルは表54から読み取った。薬剤の国内承認：ジルチアゼム注射剤とベラパミルには頻脈性不整脈の適応がある。抗凝固薬（ワルファリン、直接経口抗凝固薬）の国内の効能・効果は心房細動における血栓塞栓症の抑制であり、心房粗動に対する抗凝固は心房細動に準じた位置づけである。典型的心房粗動へのアブレーション推奨は既存カード AR-020 が担う。
  curriculum:
    kokushi: 医学各論 Ⅴ-1-A-④（心房粗動、a）
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-167 (id: Jlvnlso)；TBL-02-05-032 (id: JlAKpgM)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: AR-040
  domain: AR
  subdomain: 心室頻拍
  assertion:
    plain_statement_ja: 心室頻拍は His 束分岐部より末梢に起源を持つ頻拍で、30秒以上持続するか介入を要するものを持続性、30秒未満で自然に停止するものを非持続性と定義する。器質的心疾患に伴うものと、明らかな心疾患のない特発性心室頻拍に大別される。特発性心室頻拍の代表型は、流出路起源のもの（左脚ブロック型・下方軸が典型で、異常自動能や撃発活動が機序）と、左脚の Purkinje 網が関わるベラパミル感受性の左室頻拍（右脚ブロック型・左軸偏位が典型）であり、器質的心疾患に伴うものより一般に予後は良好である。器質的心疾患に伴う持続性心室頻拍は、多くは単形性の幅広い QRS 頻拍として現れる。
    condition:
      region: 日本
      対象: 心室頻拍の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-170
    source: Ono K, Iwasaki YK, Akao M, et al. JCS/JHRS 2020 Guideline on Pharmacotherapy of Cardiac Arrhythmias. J Arrhythm 2022;38:833-973（Circ J 2022;86:1790-1924 と同時掲載）
    doi: 10.1002/joa3.12714
    pmid: '36524037'
    pmcid: PMC9745564
    url: https://doi.org/10.1002/joa3.12714
    source_license: CC BY 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典は JCS/JHRS 2020 不整脈薬物治療ガイドライン第VII章。治療（直流通電・ICD・アブレーション・静注薬）は既存カード AR-026 が担う。「ベラパミル感受性」は機序に基づく呼称であり、本カードはベラパミルの投与法を主張しない。ベラパミルの国内承認の効能・効果は頻脈性不整脈（心房細動・粗動、発作性上室性頻拍）等で、心室頻拍は適応に含まれない。
  curriculum:
    kokushi: 医学各論 Ⅴ-1-B-②（心室頻拍、a）
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-169 (id: Jlvnls0)；TBL-02-05-032 (id: JlAKpgM)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: AR-041
  domain: AR
  subdomain: 洞不全症候群
  assertion:
    plain_statement_ja: 日本循環器学会と日本不整脈心電学会の合同ガイドライン（2022年版、不整脈の診断とリスク評価）によれば、洞不全症候群は洞結節機能の慢性的な障害により Stokes-Adams 発作・心不全・易疲労感などを来す病態で、Rubenstein 分類では I 型を持続する洞徐脈（50/分以下）、II 型を洞停止（PP 間隔が基本 PP 間隔の150%以上に突然延長）または洞房ブロック（PP 間隔が基本の整数倍に延長）、III 型を徐脈頻脈症候群（頻脈は心房細動が多く、夜間に洞停止を伴うことが多い）とする。診断の要は心電図所見と症状の対応を直接確認することであり、12誘導心電図で捉えられない場合はホルター心電図・体外式イベントレコーダ・植込み型心電図計による長期記録を用い、運動負荷心電図では年齢予測最大心拍数（220から年齢を引いた値）の85%に到達できない変時性不全を評価する。原因は自律神経・薬剤・電解質異常・内分泌疾患・頭蓋内圧亢進・低体温などの一過性で可逆的ないし生理的なものと、虚血性心疾患・高血圧・心筋症・心アミロイドーシスなどの器質的で慢性的なものに分けられる。
    condition:
      region: 日本
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4379
    source: Takase B, Ikeda T, Shimizu W, et al; Japanese Circulation Society and Japanese Heart Rhythm Society Joint Working Group. JCS/JHRS 2022 Guideline on Diagnosis and Risk Assessment of Arrhythmia. J Arrhythm. 2024;40(4):655-752.
    doi: 10.1002/joa3.13052
    pmid: '39139890'
    pmcid: PMC11317726
    url: https://doi.org/10.1002/joa3.13052
    source_license: CC表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 分類の数値基準はガイドライン本文と図で確認した（洞徐脈の閾値は図では50/分未満、本文では50/分以下の持続と表記される）。英語版（J Arrhythm 誌版）を出典とし、Circulation Journal 誌版（DOI 10.1253/circj.CJ-22-0827）と二重掲載の関係にある。ペースメーカーの適応そのものは既存の AR-030 が担い、本カードは分類と診断の枠組みに限る。原因として挙げた薬剤は分類上の総称で、個別の薬剤名は含まない。
  curriculum:
    kokushi: 医学各論 Ⅴ-1-C-①（洞不全症候群、a）
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-164 (id: JlvnlsU)；TBL-02-05-032 (id: JlAKpgM)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: AR-042
  domain: AR
  subdomain: 房室ブロック
  assertion:
    plain_statement_ja: 同ガイドラインによれば、房室ブロックは房室結節・ヒス束・ヒス-プルキンエ系における伝導の遅延または中断であり、1度（PR 間隔0.2秒超、0.3秒超は病的）、2度（PR 間隔が漸次延長して脱落する Wenckebach 型［Mobitz I 型］、PR 延長の前触れなく突然脱落する Mobitz II 型、2:1 ブロック、伝導比3:1以上の高度房室ブロック）、3度（完全房室ブロック、房室解離）に分類される。発作的に現れるため12誘導心電図で捉えられることは少なく、ホルター心電図・イベントレコーダ・植込み型心電図計による記録で確認する。ブロック部位が末梢（ヒス-プルキンエ系寄り）であるほど逸脱リズムが不安定で重症であり、部位の判定が難しい2:1 ブロックでは運動負荷でブロックが出現・悪化すれば房室結節より末梢のブロックを示唆し、それでも不明な場合は心臓電気生理検査を行う。1度房室ブロックと Wenckebach 型は夜間の迷走神経優位時には生理的にもみられる。
    condition:
      region: 日本
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4379
    source: Takase B, Ikeda T, Shimizu W, et al; Japanese Circulation Society and Japanese Heart Rhythm Society Joint Working Group. JCS/JHRS 2022 Guideline on Diagnosis and Risk Assessment of Arrhythmia. J Arrhythm. 2024;40(4):655-752.
    doi: 10.1002/joa3.13052
    pmid: '39139890'
    pmcid: PMC11317726
    url: https://doi.org/10.1002/joa3.13052
    source_license: CC表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドライン英語版の本文にはブロック部位に関する訳語の不統一がみられる箇所があり、アトロピンへの反応に関する記述は本カードに含めなかった。部位診断の記述は同ガイドラインの検査手順（運動負荷心電図・心臓電気生理検査）の論理に沿って標準的な表現に整えた。ペースメーカーの適応は既存の AR-031 が担い、本カードは分類・心電図所見・部位診断に限る。
  curriculum:
    kokushi: 医学各論 Ⅴ-1-C-②（房室ブロック、a）
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-165 (id: Jlvnlsc)；TBL-02-05-032 (id: JlAKpgM)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: IH-031
  domain: IH
  subdomain: 無痛性虚血性心疾患
  assertion:
    plain_statement_ja: 無症候性（無痛性）心筋虚血は、狭心症やその同等症状がないにもかかわらず心筋虚血が客観的に証明される状態であり、心筋虚血発作の50〜70%は無症候とされる。一般人口での頻度は2〜4%と推定され、糖尿病や安定狭心症の患者で高い。Cohn の分類では、虚血性心疾患の症状が全くない I 型、心筋梗塞の既往があり無症候である II 型、狭心症に加えて無症候の虚血発作を伴う III 型に分ける。検出には運動負荷試験、負荷心エコー、心筋血流イメージング（SPECT・PET）、心臓 MRI などが用いられるが、欧州心臓病学会の慢性冠症候群ガイドラインは無症候の一般集団への機能的画像検査によるスクリーニングを推奨せず、糖尿病・冠動脈疾患の強い家族歴・高リスクの場合に限って弱い推奨（IIb・レベル C）とする。無症候性心筋梗塞は心臓突然死のリスク上昇と関連し、心筋梗塞後や不安定狭心症に伴う無症候性虚血は予後不良の指標となる。管理は危険因子の是正と至適な薬物治療が基本で、抗虚血薬とアスピリンの使用が主要有害心血管イベントの減少と関連した小規模な無作為化試験がある一方、至適薬物治療への PCI の上乗せ効果は COURAGE 試験の事後解析では示されず、血行再建は左主幹部病変や左室機能低下を伴う多枝病変など予後改善が見込まれる解剖学的条件で検討される。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4964
    source: 'Theofilis P, Antonopoulos AS, Sagris M, Papanikolaou A, Oikonomou E, Tsioufis K, Tousoulis D. Silent Myocardial Ischemia: From Pathophysiology to Diagnosis and Treatment. Biomedicines. 2024;12(2):259.'
    doi: 10.3390/biomedicines12020259
    pmid: '38397860'
    pmcid: null
    url: https://doi.org/10.3390/biomedicines12020259
    source_license: CC BY 4.0（誌のオープンアクセス表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 総説（Biomedicines 誌、2024年）に基づく国際的な総論であり、日本に特化した数値ではない。頻度2〜4%は一般人口での推定値で、出典の記述範囲に限る。無症候性心筋梗塞と心臓突然死の関連は同総説が引く ARIC・CHS 研究の統合ハザード比2.65に基づく。アスピリンは国内では虚血性心疾患に対する抗血小板療法として承認・保険適用がある。既存の IH-024（DIAD 試験）は無症候の2型糖尿病へのスクリーニングの帰結を扱い、本カードは疾患の総論を担う。PMCID は確認できず null とした。
  curriculum:
    kokushi: 医学各論 Ⅴ-5-D（無痛性虚血性心疾患、a）
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-028 (id: JlAKpf8)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: MP-043
  domain: MP
  subdomain: 心囊液貯留
  assertion:
    plain_statement_ja: 欧州心臓病学会の心筋炎・心膜炎ガイドライン（2025年版）によれば、正常の心膜液は10〜50 mL で、心エコー上の拡張末期の無エコー域の最大幅で中等量を10〜20 mm、大量を20 mm 超とする。先進国における中等量〜大量の心囊液貯留の原因の内訳は、特発性が最大50%、悪性腫瘍が10〜32%、感染症が15〜30%、医原性が15〜20%、結合組織病が5〜15%で、結核が流行する地域では結核が60%超を占める。甲状腺機能低下症などの内科疾患に伴うものも多く、最大60%が既知・未知の内科疾患と関連する。貯留の相当部分は無症候で偶然に発見される。治療は原因への対応が基本で、心膜の炎症所見（CRP 上昇や画像上の炎症）がない場合の抗炎症治療は推奨されない。無症候で心膜炎を伴わない慢性の特発性大量貯留は保存的に経過をみることができ（タンポナーデの発症は年2.2%）、症状の出現や心エコーでの血行動態への影響が現れた場合にドレナージを行う。中等量以上の無症候の貯留は6か月ごとの経過観察が勧められ、軽度の無症候性特発性貯留は原則として特別な経過観察を要しない。予後は主として原因に依存する。
    condition:
      region: 欧州
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4965
    source: Schulz-Menger J, Collini V, Gröschel J, et al; ESC Scientific Document Group. 2025 ESC Guidelines for the management of myocarditis and pericarditis. Eur Heart J. 2025;46(40):3952-4041.
    doi: 10.1093/eurheartj/ehaf192
    pmid: '40878297'
    pmcid: null
    url: https://doi.org/10.1093/eurheartj/ehaf192
    source_license: © The European Society of Cardiology 2025（All rights reserved、ガイドライン本文の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 心エコーによる大きさの区分はガイドラインの表10から読み取り（中等量10〜20 mm・大量20 mm 超）。小規模（10 mm 未満）の区分は本カードの主張に含めていない。原因の割合は中等量〜大量の貯留を対象とした先進国のシリーズに基づく数値である。再発時の管理は、経過観察の間隔と症状・血行動態の変化に応じたドレナージの判断として含めた。既存の MP-025 は2015年版ガイドラインの要約論文（SRC-252）に基づくが、本カードは現行の一次ガイドラインである2025年版を出典とした。
  curriculum:
    kokushi: 医学各論 Ⅴ-6-D-②（心囊液貯留、a）
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-184 (id: Jlvnluw)；TBL-02-05-027 (id: JlAKpf4)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: MP-044
  domain: MP
  subdomain: 心タンポナーデ
  assertion:
    plain_statement_ja: 同ガイドライン（2025年版）によれば、心タンポナーデは心囊液貯留が心臓の拡張期充満を妨げて心拍出量が低下した状態で、診断は示唆的な病歴・症状・徴候に基づく臨床診断に心エコーによる確認を組み合わせて行う。身体所見では頻脈、低血圧（収縮期血圧90 mmHg 未満。亜急性・慢性では低下が軽いこともある）、頸静脈圧の上昇を伴う怒張、吸気時の収縮期血圧低下が10 mmHg 以上の奇脈、心音の減弱がみられる。低血圧・頸静脈怒張・心音減弱の Beck の三徴は、外傷や心筋・大動脈破裂による急性の心囊内出血（外科的タンポナーデ）で同定されたもので、緩徐に貯留する内科的タンポナーデでは欠けることがある。心電図では頻脈のほか QRS 低電位と電気的交互脈がみられる。心エコー所見としては、大きな貯留と心臓の揺れ（swinging heart）、右房の虚脱（持続時間が心周期の0.34を超える場合は特異度が高い）、右室の拡張期虚脱、僧帽弁 E 波速度の呼吸性変動25〜30%超と三尖弁 E 波速度の呼吸性変動40〜60%超、下大静脈の拡張（20 mm 超）と呼吸性変動の減弱（径の減少が50%未満）が挙げられる。心膜は硬く伸展性に乏しいため、急速な貯留では200〜300 mL でタンポナーデに至り、緩徐な貯留では1〜2 L に達することもある。
    condition:
      region: 欧州
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4965
    source: Schulz-Menger J, Collini V, Gröschel J, et al; ESC Scientific Document Group. 2025 ESC Guidelines for the management of myocarditis and pericarditis. Eur Heart J. 2025;46(40):3952-4041.
    doi: 10.1093/eurheartj/ehaf192
    pmid: '40878297'
    pmcid: null
    url: https://doi.org/10.1093/eurheartj/ehaf192
    source_license: © The European Society of Cardiology 2025（All rights reserved、ガイドライン本文の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 心エコー所見の感度・特異度に関わる数値（右房虚脱の持続時間の比0.34、下大静脈の感度など）はガイドラインの表17から読み取り。右房の虚脱について、ガイドラインの表は位相を限定しないため本カードも位相を特定しない表現にした（依頼文の表の見込みは「右房の収縮期虚脱」）。Beck の三徴は全例にそろう所見ではない。緊急心膜穿刺の適応は既存の MP-025 が担い、本カードは診断に限る。
  curriculum:
    kokushi: 医学各論 Ⅴ-6-E（心タンポナーデ、a）
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-184 (id: Jlvnluw)；TBL-02-05-027 (id: JlAKpf4)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: HT-024
  domain: HT
  subdomain: 睡眠時無呼吸症候群
  assertion:
    plain_statement_ja: 睡眠時無呼吸症候群（SAS）の診療ガイドライン2020（英語誌版）によれば、閉塞性睡眠時無呼吸は二次性高血圧の主な原因の一つであり（エビデンス A）、閉塞性睡眠時無呼吸の患者の約50%に高血圧が合併し、高血圧患者の約30%に閉塞性睡眠時無呼吸がみられる。
    condition:
      region: 日本
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-3746
    source: Akashiba T, Inoue Y, Uchimura N, et al. Sleep Apnea Syndrome (SAS) Clinical Practice Guidelines 2020. Sleep Biol Rhythms. 2022;20(1):5-37.
    doi: 10.1007/s41105-021-00353-6
    pmid: '38469064'
    pmcid: PMC10900032
    url: https://doi.org/10.1007/s41105-021-00353-6
    source_license: CC BY 4.0（論文ページの Open Access 表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本カードは、依頼表が求める定義・診断・重症度・治療の総論のうち、既存の PH-009〜011 と PL-019〜024 のいずれも具体的な位置づけや数値を収載していない「高血圧との合併」に厳密に限る。総論の側面は PH-009（診断の進め方とガイドライン全体像、SRC-495）、PH-010（CPAP の保険基準）、PH-011（CPAP 第一選択と口腔内装置、SRC-3746）と、呼吸器の PL-019（診断基準）・PL-020（AHI による重症度）・PL-022（治療の推奨）が既に担っており、新規の総論カードを作ると実質重複になるため作らなかった（対応表と番号追加の申し送りは引き継ぎメモに記載）。合併の頻度は英語誌版の CQ17 で確認したもので、日本語版ガイドラインの対応する記述の逐語照合はしていない。主張に薬剤名は含まない。
  curriculum:
    kokushi: 医学各論 Ⅴ-7-B-④（睡眠時無呼吸症候群、a）
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: HT-025
  domain: HT
  subdomain: 高血圧緊急症
  assertion:
    plain_statement_ja: 高血圧治療ガイドライン2025（JSH2025）第16章によれば、高血圧緊急症は著しい血圧上昇（通常180/120 mmHg 以上）に伴い脳・心臓・腎臓・大血管などの標的臓器に急性の障害とその進行を来した状態で、高血圧性脳症・子癇・大動脈解離は血圧の絶対値が高くなくても急峻な上昇自体により緊急症に含まれる。急速な臓器障害の進行を伴わない重症高血圧は高血圧切迫症として区別される。緊急症では原則として入院のうえ集中治療室での直接血圧モニタリングが望ましく、速効性で調節可能な静注降圧薬を用いる。降圧の速度と目標は、最初の1時間は基礎値の25%以内の低下にとどめ、続く2〜6時間で160/100 mmHg 程度、24〜48時間で140/90 mmHg 未満へと段階的に下げることが原則で、過度に急速な降圧は臓器の虚血を招く。在宅・外来ではなく病院での治療が前提であり、日本では代替となる薬剤がない場合にニカルジピン静注が頻用され、急性心不全や急性冠症候群を伴う重症高血圧にはニトログリセリン持続静注が適する。臓器別の例外として、大動脈解離では収縮期血圧を直ちに120 mmHg 未満（目標100〜120 mmHg、心拍数60/分未満、禁忌がなければ静注β遮断薬を先行）まで、急性期脳出血では収縮期血圧140 mmHg 未満へ速やかに（110 mmHg 超を維持し、90 mmHg 超の低下は避ける）、重症高血圧を伴う急性冠症候群では収縮期血圧140 mmHg 未満へ速やかに下げる。体液過剰がない場合のループ利尿薬は推奨されず、初期目標の達成後は経口薬へ移行する。
    condition:
      region: 日本
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4381
    source: Ohya Y, et al. The Japanese Society of Hypertension Guidelines for the management of elevated blood pressure and hypertension 2025 (JSH2025). Hypertens Res. 2026;49(1):9-235.
    doi: 10.1038/s41440-025-02462-y
    pmid: '41476123'
    pmcid: null
    url: https://doi.org/10.1038/s41440-025-02462-y
    source_license: CC表示なし（購読誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 降圧目標と臓器別の例外は JSH2025 第16章の本文で確認した。ニカルジピン注射薬は国内で高血圧性緊急症の適応で承認されている。ニトログリセリン静注薬は国内では急性心不全・不安定狭心症等の適応で承認されており、本カードの記述はそれらを合併する重症高血圧への使用である。β遮断薬とループ利尿薬はクラス単位の記述で個別の薬剤名は含まない。既存の HT-009 は切迫症側の外来対応を担い、本カードは緊急症の初期対応に限る。
  curriculum:
    kokushi: 医学各論 Ⅴ-7-C（高血圧緊急症、a）
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-200 (id: Jlvnlwg)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ES-094
  domain: ES
  subdomain: Mallory-Weiss症候群
  assertion:
    plain_statement_ja: Mallory-Weiss症候群では自然止血が多い一方、抗血栓薬の使用や肝硬変などの出血しやすい背景がある例では出血が遷延しうる。出血が遷延する例や高リスク例に対しては、機械的止血法による内視鏡的止血が強く推奨される（推奨グレード1、エビデンスレベルC）。機械的止血にはクリッピングと内視鏡的結紮術があり、責任血管が食道側にある場合は、食道の筋層が薄く局所注射や凝固法では穿孔の危険があるため機械的止血が優先される。局所注射は心疾患のある例では循環器系への影響にも注意が要る。内視鏡的止血が困難なまれな例ではIVRや外科治療が検討される。再出血予防は消化性潰瘍出血に準じ、絶食と輸液管理の後に酸分泌抑制薬と粘膜保護薬を投与し、症状と血液検査所見に応じて経口摂取を再開する。初期対応の一般原則として、高リスクの非静脈瘤性上部消化管出血では循環動態の安定化後24時間以内の内視鏡が強く推奨され（推奨グレード1、エビデンスレベルA）、心血管疾患のない例の輸血はHb 8 g/dLを目標上限として過剰な輸血を避けることが強く推奨される（推奨グレード1、エビデンスレベルA）。
    condition:
      region: 日本
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4966
    source: Fujishiro M, Iguchi M, Ono S, et al. Guidelines for endoscopic management of nonvariceal upper gastrointestinal bleeding (second edition). Dig Endosc. 2025;37(5):447-469
    doi: 10.1111/den.15019
    pmid: null
    pmcid: null
    url: https://doi.org/10.1111/den.15019
    source_license: CC 表示なし（日本消化器内視鏡学会のガイドライン）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は日本消化器内視鏡学会の非静脈瘤性上部消化管出血における内視鏡診療ガイドライン第2版で、Mallory-Weiss症候群の扱いはCQ11と同節の解説、内視鏡のタイミングと輸血は同ガイドラインのCQ3・CQ4（非静脈瘤性上部消化管出血全般へのステートメント）に基づく（出版社サイトの全文で確認）。PMIDは、他文献の引用リストでPubMedへのリンクが示され収載自体はうかがえたが、番号を確認できなかったためnullとした（DOIで一意に特定可能）。ESGEの2021年改訂は内視鏡的止血の推奨を消化性潰瘍出血に限定し、それ以外の病因は2015年版に委ねており、2026年改訂も潰瘍出血が対象のため、現行の国内ガイドラインを出典とした。薬剤は酸分泌抑制薬・粘膜保護薬を薬効群としてのみ言及し、個別の薬剤名は主張に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅵ-1-E-①（Mallory-Weiss症候群、a）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-033 (id: JlAKplQ)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ES-095
  domain: ES
  subdomain: 食道裂孔ヘルニア
  assertion:
    plain_statement_ja: 食道裂孔ヘルニアは型によって分類される。I型（滑脱型）は胃食道接合部が裂孔より上方に位置するもの、II型は胃食道接合部が正常な位置にあるまま胃底部が裂孔より上方へ突出するもの、III型はその混合で胃食道接合部と胃の両方が裂孔より上方にあるもの、IV型は胃に加えて他の臓器も脱出するものである。外科的修復の検討対象は主にII〜IV型（傍食道型）である。無症状のII〜IV型については、修復術を受けた患者では貧血（24〜57%）、呼吸困難（21〜67%）、胸痛（40〜60%）が高率にみられるため、まず本当に無症状かどうかを確認することが前提とされる。症状がヘルニアに帰属する場合や客観的な逆流・微小誤嚥の所見がある場合は、手術に耐えられる患者に修復術を提示でき、精査で異常がなく患者が胃軸捻転のリスクを受け入れる場合は経過観察も妥当であり、共有意思決定が重要とされる（エキスパートオピニオン）。II〜IV型の修復術に噴門形成術を併施することは、条件付きで推奨される（エビデンスの確実性は低い）。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4967
    source: Daly S, Kumar SS, Collings AT, et al. SAGES guidelines for the surgical treatment of hiatal hernias. Surg Endosc. 2024;38(9):4765-4775
    doi: 10.1007/s00464-024-11092-3
    pmid: '39080063'
    pmcid: null
    url: https://doi.org/10.1007/s00464-024-11092-3
    source_license: CC 表示なし（Springer、学会ガイドライン）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典はSAGESの食道裂孔ヘルニア外科治療ガイドライン（2024）で、型分類は同ガイドラインの定義、無症状例への対応はKQ2（エキスパートオピニオン）、噴門形成術はKQ3の条件付き推奨に基づく。メッシュ使用については推奨・反対のいずれの推奨も出されていない（KQ1）ため主張に含めなかった。I型（滑脱型）を逆流症として管理する方針は、本ガイドラインでは推奨として明記されておらず（序文で裂孔ヘルニアと逆流症の関連に触れるのみ）、未収載とした。症状の割合はガイドライン本文が引用する修復術シリーズの範囲である。
  curriculum:
    kokushi: 医学各論 Ⅵ-9-A-①（食道裂孔ヘルニア、a）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: AB-117
  domain: AB
  subdomain: 消化管穿孔
  assertion:
    plain_statement_ja: 二次性腹膜炎は腹腔内臓器の完全性の喪失によって生じ、その代表的な機序が消化管の穿孔である。原因には消化性潰瘍の穿孔（胃十二指腸穿孔）のほか、大腸の非憩室性穿孔、小腸穿孔、外傷性穿孔、術後の吻合部縫合不全などがある。国際的な腹腔内感染症の調査（WISS）では、感染源の内訳として胃十二指腸穿孔が11%、大腸の非憩室性穿孔が5.9%、小腸穿孔が5.4%、外傷後穿孔が2.5%であった。診断はまず臨床評価に基づいて行われ、腹痛と腹部の硬直が手がかりとなり、診断が不確かな場合などにCTが有用で、高所得国では画像診断の標準とされる。治療の柱は、早期の認識、適切な蘇生、早期の適切な抗菌薬投与、早期かつ有効な感染源制御であり、外科的な感染源制御には病変部・穿孔部の切除や縫合閉鎖が含まれる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-157
    source: 'Sartelli M, Chichom-Mefire A, Labricciosa FM, et al. The management of intra-abdominal infections from a global perspective: 2017 WSES guidelines for management of intra-abdominal infections. World J Emerg Surg 2017;12:29'
    doi: 10.1186/s13017-017-0141-6
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s13017-017-0141-6
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典は既存登録SRC-157（WSES腹腔内感染症ガイドライン2017、AB-075・076の出典）の再利用で、書誌と識別子はAB-076の登録にそろえた。依頼表の側面のうち画像所見としての腹腔内遊離ガスは、本ガイドラインに遊離ガス自体の記載が確認できなかったため主張に含めず、CTの位置づけまでにとどめた。感染源の割合はガイドライン本文中のWISS研究（4,553例）の表から読み取った数値である。抗菌薬は薬効群としての言及で、個別の薬剤名は含めていない。
  curriculum:
    kokushi: 医学各論 Ⅵ-10-E-①（消化管穿孔、a）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-308 (id: Jlvnl70)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: AB-118
  domain: AB
  subdomain: 腹部外傷
  assertion:
    plain_statement_ja: 腹部外傷の治療方針は、解剖学的な損傷の程度だけでなく、循環動態と合併損傷をあわせて判断する。来院時の診断手続きは循環動態によって決まり、E-FASTは腹腔内遊離液体の迅速な検出に有効である（推奨グレード1A）。循環が安定し、手術を要する他の腹腔内損傷がない患者では、軽症から重症（WSES分類I〜III）まで非手術的管理（NOM）が治療の第一選択となり（推奨グレード2A）、その間は臨床所見と検査の反復評価で状態の変化を捉えることが必須とされる（推奨グレード2A）。CTで動脈性の造影剤漏出を認める安定した患者では、血管造影・動脈塞栓術が第一選択の介入となりうる（推奨グレード2B）。一方、輸液・輸血に反応しない循環不安定な患者（WSES分類IV）は手術的管理の対象であり（推奨グレード2A）、手術の第一の目的は出血と胆汁漏の制御と、できるだけ早期のダメージコントロール蘇生の開始とされる（推奨グレード2A）。不安定な患者のダメージコントロール手術では解剖学的切除は避け、肝臓のパッキングなどの一時的な止血手段や、二期的手術を前提とした一時的な腹壁閉鎖が用いられる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4245
    source: 'Coccolini F, Coimbra R, Ordonez C, et al. Liver trauma: WSES 2020 guidelines. World J Emerg Surg. 2020;15:24.'
    doi: 10.1186/s13017-020-00302-7
    pmid: '32228707'
    pmcid: null
    url: https://doi.org/10.1186/s13017-020-00302-7
    source_license: CC BY 4.0（ジャーナルの OA ライセンス）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典は既存登録SRC-4245（WSES肝損傷ガイドライン2020、AB-109の出典）の再利用で、肝損傷に限らない総論的なステートメント（循環動態による方針決定、NOMと手術的管理の適応、ダメージコントロールの考え方）の範囲で用いた。腹膜炎所見そのものを開腹の適応として明示した文は本ガイドラインにはないため、NOMの条件はガイドラインの文言どおり「手術を要する他の腹腔内損傷がないこと」とした（腹膜炎をNOMの禁忌として明示するのは脾損傷ガイドラインSRC-161の記載であり、初期評価のAB-084側の範囲）。ダメージコントロール手術の細部（パッキング、一時的閉腹）は本文の手術管理の節に基づく。
  curriculum:
    kokushi: 医学各論 Ⅵ-11-A-①（腹部外傷、a）
    core_curriculum: null
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: AB-119
  domain: AB
  subdomain: 大腿ヘルニア
  assertion:
    plain_statement_ja: 大腿ヘルニアは、内臓または脂肪組織が大腿管を通って脱出する鼠径部ヘルニアである。待機的・緊急をあわせた大腿ヘルニア修復術は、全鼠径部ヘルニア修復術のおよそ2〜4%を占める。大腿ヘルニアは鼠径ヘルニアより嵌頓・絞扼のリスクが高く、嵌頓・絞扼の危険因子として女性であることと大腿ヘルニア自体が挙げられ、女性の鼠径部ヘルニアでは約17%が緊急修復を要するとされる。絞扼や腸管切除といった重篤で致死的となりうる合併症のリスクが許容できないほど高いため、無症状の大腿ヘルニアでも経過観察は勧められず、症状が曖昧な場合や無症状の場合でも時期を逸しない手術が推奨される。緊急修復は待機的修復に比べて小腸切除のリスクが高く、在院期間も長い。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-158
    source: HerniaSurge Group. International guidelines for groin hernia management. Hernia 2018;22:1-165
    doi: 10.1007/s10029-017-1668-x
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/s10029-017-1668-x
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は既存登録SRC-158（HerniaSurge国際ガイドライン2018、AB-069・073の出典）の再利用で、第17章（大腿ヘルニア）と全体要約に基づき、書誌と識別子は既存登録にそろえた。依頼表の側面のうち大腿輪の境界（前方の鼠径靱帯、内側の裂孔靱帯、後方の恥骨筋膜・クーパー靱帯、外側の大腿静脈）などの解剖の細部は、本ガイドラインに記載が確認できなかったため主張に含めず、大腿管を介する脱出という定義の範囲にとどめた。2〜4%は修復術に占める割合であり、真の発生頻度はこれより低いとガイドラインは述べている。
  curriculum:
    kokushi: 医学各論 Ⅵ-9-A-③（大腿ヘルニア、a）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-309 (id: Jlvnl78)；TBL-01-00-310 (id: Jlvnl8E)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: IN-114
  domain: IN
  subdomain: 痔核
  assertion:
    plain_statement_ja: 内痔核は脱出の程度によりGoligher分類で4度に分けられる。I度は出血するが脱出しないもの、II度は排便時のいきみで脱出するが自然に還納するもの、III度は脱出して用手的な還納を要するもの、IV度は常に脱出して還納できないもので、急性の血栓性・嵌頓性の内痔核もIV度に含まれる。症状として最も多いのは排便に伴う無痛性の鮮紅色の直腸出血で、脱出に伴う粘液の分泌やかゆみを伴うことがあり、疼痛は血栓が形成されたとき（とくに外痔核）やIV度の絞扼のときに生じるのが通常である。治療は重症度に応じて段階的に選択され、食事・生活習慣の改善は全ての重症度に適用される。食物繊維の補給は、症状の持続と出血のリスクをおよそ50%下げるが、脱出・疼痛・かゆみには効果がなかった。薬物療法はI〜II度（とIII度の一部）に、硬化療法と赤外線凝固法はI〜II度に、ゴムバンド結紮はI〜II度とIII度の一部に用いられ、非手術的治療の中で優先される方法とされる。痔核切除術はIII度・IV度とII度の一部が適応で、急性の血栓形成・絞扼の際には緊急手術の適応となる。環状切除術（stapled hemorrhoidopexy）はII〜III度に用いられる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4968
    source: 'Lohsiriwat V. Hemorrhoids: From basic pathophysiology to clinical management. World J Gastroenterol. 2012;18(17):2009-2017'
    doi: 10.3748/wjg.v18.i17.2009
    pmid: '22563187'
    pmcid: PMC3342598
    url: https://doi.org/10.3748/wjg.v18.i17.2009
    source_license: 未確認（PMC収載版・出版社ページともCC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典はLohsiriwatの痔核の総説（2012）で、グレード別の治療法の対応は同総説の表から読み取った。血栓性外痔核については、疼痛が血栓形成時に生じるという症状面までは確認したが、切除の適応や時期といった扱いの詳細は本総説の記載が乏しく、主張に含めなかった。国内には日本大腸肛門病学会の肛門疾患（痔核・痔瘻・裂肛）・直腸脱診療ガイドライン2020年版（改訂第2版）があるが、本文を照合していないため出典には用いず、今後の差し替え候補とする。個別の薬剤名は主張に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅵ-4-D-①（痔核、a）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-267 (id: Jlvnl30)；TBL-02-07-020 (id: JlAKpkk)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BP-076
  domain: BP
  subdomain: 肝内胆管癌
  assertion:
    plain_statement_ja: 肝内胆管癌を含む胆道癌の診断では、非外科的治療の前にコア生検で病理診断を得ることが勧められ、進行例では全身療法の適応となる患者に分子プロファイリングが推奨される。腫瘍マーカーCA19-9の高値は予後不良と関連し、治療効果の評価に利用できる。根治を目指す治療はリンパ節郭清を含む外科切除のみであり、切除後はS-1またはカペシタビンによる補助化学療法が検討される。手術ができない肝限局の小さい腫瘍（3 cm以下）ではアブレーションが選択肢となる。進行例の一次治療は、ゲムシタビンとシスプラチンにデュルバルマブまたはペムブロリズマブを併用する治療が標準とされる。
    condition:
      region: 国際
      対象: 肝内胆管癌の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4969
    source: Chen LT, Vogel A, Hsu C, et al. Pan-Asian adapted ESMO Clinical Practice Guidelines for the diagnosis, treatment and follow-up of patients with biliary tract cancer. ESMO Open. 2024;9(8):103647
    doi: 10.1016/j.esmoop.2024.103647
    pmid: '39232586'
    pmcid: PMC11410730
    url: https://doi.org/10.1016/j.esmoop.2024.103647
    source_license: CC BY-NC-ND 4.0（PMC のライセンス表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ESMO ガイドラインのアジア適応版（2024年、日本腫瘍学会を含むアジアの学会が参加）に基づく。推奨の多くは胆道癌全体に対するもので、肝内胆管癌に特化した推奨（3 cm 以下の腫瘍へのアブレーション等）と併せて記載した。症状については同ガイドラインにまとまった記載がなく、主張に含めていない。同ガイドラインには訂正（ESMO Open. 2025;10(1):104074）が出ている。薬剤の国内承認：デュルバルマブとゲムシタビン・シスプラチンの併用は根治切除不能な胆道癌に対して国内承認済み（2022年）で、ペムブロリズマブの同併用も切除不能な胆道癌に対して国内承認済みである。S-1 は国内で胆道癌に承認があり、ASCOT 試験（切除後の3年生存割合は S-1 群77.1%に対して経過観察群67.6%）に基づいて術後補助療法の標準とされる一方、カペシタビンには胆道癌の国内適応はなく、術後補助療法としては保険適用外である。
  curriculum:
    kokushi: 医学各論 Ⅵ-6-C-②（肝内胆管癌、a）
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)；TBL-01-00-293 (id: Jlvnl7Q)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BP-077
  domain: BP
  subdomain: 胆囊炎
  assertion:
    plain_statement_ja: 急性胆嚢炎の診断基準（東京ガイドライン2018）は、A：局所炎症所見（Murphy徴候、右上腹部の腫瘤・疼痛・圧痛）、B：全身炎症所見（発熱、CRP上昇、白血球数増加）、C：画像所見（急性胆嚢炎に特徴的な所見）の3群からなり、AとBから1項目ずつを満たせば疑診、A・B・Cすべてを満たせば確診とする。画像所見には胆嚢壁肥厚（4 mm以上）、胆嚢腫大、胆嚢結石やデブリ、胆嚢周囲の液体貯留などがあり、超音波検査が第一選択である。治療は、初期治療として抗菌薬と全身管理を行い（抗菌薬開始前に血液培養の採取を考慮する）、重症度と手術リスク（Charlson併存疾患指数とASA身体状態分類）で方針を決める。低リスクの軽症・中等症では早期の腹腔鏡下胆嚢摘出術が基本となり、手術リスクが高い場合は胆嚢ドレナージを先行させて炎症の改善後に待機的に摘出する。重症では臓器障害への支持療法と緊急の胆嚢ドレナージが優先され、早期手術は高次施設で厳格な条件を満たす場合に限られる。
    condition:
      region: 日本
      対象: 急性胆嚢炎の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-094
    source: 日本肝胆膵外科学会ほか編『TG18新基準掲載 急性胆管炎・胆嚢炎診療ガイドライン2018（第3版）』医学図書出版、2018
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 著作権は著者・出版社に帰属（Mindsは私的利用の範囲に限ると明記）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 診断基準は TG18 の診断基準表で確認した。重症度の判定項目そのものは既存カード BP-006 が担う。手術リスクの閾値（Charlson併存疾患指数5以下・ASA身体状態分類II以下）は TG18 フローチャートの図注と抄録で確認した（図表から読み取りを含む）。抗菌薬の具体的な薬剤選択は同ガイドラインの抗菌薬療法の項によるべきもので、本カードでは薬剤名を挙げていない。内容の確認は TG18 の英語版ガイドライン論文（診断基準は Yokoe ら 2018、治療フローチャートは Okamoto ら 2018）で行い、日本語版ガイドライン本体と同一版であることを照合した。
  curriculum:
    kokushi: 医学各論 Ⅵ-7-B-①（胆囊炎、a）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-300 (id: Jlvnl5U)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: LV-112
  domain: LV
  subdomain: アルコール性肝障害
  assertion:
    plain_statement_ja: アルコール関連肝疾患の診断は、慢性の有害な飲酒を飲酒歴の聴取やアルコールバイオマーカーで同定し、他の肝疾患を除外することによって行う。線維化の評価には FIB-4 や肝エラストグラフィなどの非侵襲的検査がまず用いられる。重症度評価では、アルコール性肝炎について MELD スコア（20を超えると重症の目安）に加えて Maddrey の判別関数（discriminant function）が歴史的に用いられてきた指標であり、32以上では30日死亡率がおよそ20〜50%とされる。管理の基盤は断酒であり、肝臓専門医と依存症の専門家を含む集学的な統合ケアの中で、行動療法と薬物療法を組み合わせたアルコール使用障害の治療を行うことが強く推奨される。アルコール性肝炎では栄養療法も重要で、エネルギー35 kcal/kg/日・タンパク質1.2〜1.5 g/kg/日が目標とされ、摂取量が21 kcal/kg/日未満の場合は経口・経腸栄養による補充が勧められる。
    condition:
      region: 米国
      対象: アルコール関連肝疾患の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-3974
    source: 'Jophlin LL, Singal AK, Bataller R, Wong RJ, Sauer BG, Terrault NA, Shah VH. ACG Clinical Guideline: Alcohol-Associated Liver Disease. Am J Gastroenterol. 2024;119(1):30-54'
    doi: 10.14309/ajg.0000000000002572
    pmid: '38174913'
    pmcid: null
    url: https://doi.org/10.14309/ajg.0000000000002572
    source_license: CC 表示なし（購読誌。著者原稿が PMC に収載）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国のガイドライン（ACG、2024年）に基づく。国内の診断基準は日本肝臓学会『アルコール性肝障害（アルコール関連肝疾患）診療ガイド 2022』に整理されているが、基準本文の逐語確認ができていないため、本カードの主張には含めていない（既存カード TX-005 と同じ事情）。重症アルコール性肝炎の薬物治療（ステロイド等）は TX-005 が担う。AST/ALT 比は ACG が参照する NIAAA の臨床診断基準の表に含まれる項目だが、本確認ではその表の数値を本文テキストで逐語確認できなかったため、主張には含めていない。栄養の目標量はアルコール性肝炎に対する推奨であり、重症でない例への当てはめには注意が要る。断酒の薬物療法の国内承認：アカンプロサートはアルコール依存症の断酒維持補助として国内承認済みだが、ナルトレキソンは国内未承認、バクロフェンは国内では痙性麻痺の適応のみでアルコール使用障害には適応外である。ジスルフィラムは国内で抗酒薬として承認があるが、肝毒性のため ACG は肝疾患患者では禁忌としている。
  curriculum:
    kokushi: 医学各論 Ⅵ-6-E-③（アルコール性肝障害、a）
    core_curriculum: 'PS-03-05-08 (id: Jkxnubw)；GE-04-01-06 (id: JkxpswA)；TBL-01-00-289 (id: Jlvnl64)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: IE-018
  domain: IE
  subdomain: アセトン血性嘔吐症
  assertion:
    plain_statement_ja: 小児の周期性嘔吐症候群の発作時治療では、片頭痛の個人歴・家族歴がある場合に抗片頭痛薬（トリプタン系薬・NSAIDs）による発作の頓挫が強く推奨され、5-HT3受容体拮抗薬（オンダンセトロン）も頓挫に用いられる。外来での頓挫療法が奏効しない場合は早期に受診させ直ちに静脈内輸液を開始し、急性期は静脈内輸液による水分補給を行う。発作予防にはβ遮断薬（プロプラノロール）、5-HT2A受容体拮抗薬（シプロヘプタジン）、NK1受容体拮抗薬（アプレピタント）、三環系抗うつ薬（アミトリプチリン）が条件付きで推奨され、三環系抗うつ薬は発作が頻回・重症でより安全な選択肢に反応しない場合に用い、抗てんかん薬は難治例を除き予防に用いない。
    condition:
      region: 北米
      対象: 小児の周期性嘔吐症候群患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4970
    source: Karrento K, Rosen JM, Gelfand AA, et al. North American Society for Pediatric Gastroenterology, Hepatology, and Nutrition 2025 guidelines for management of cyclic vomiting syndrome in children. J Pediatr Gastroenterol Nutr. 2025;80(6):1028-1061.
    doi: 10.1002/jpn3.70020
    pmid: '40223700'
    pmcid: null
    url: https://doi.org/10.1002/jpn3.70020
    source_license: Wiley（CC表示を確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 推奨の強さはガイドライン本文で確認した（強い推奨は抗片頭痛薬による頓挫のみで、他の薬剤はいずれも条件付き推奨、エビデンスの確実性は低い〜非常に低い）。国内承認の状況：オンダンセトロンは国内で抗悪性腫瘍剤投与に伴う悪心・嘔吐や術後の悪心・嘔吐に承認されているが、周期性嘔吐症候群への適応はない。トリプタン系薬は片頭痛への承認であり、プロプラノロール・シプロヘプタジン・アプレピタント・アミトリプチリンにも周期性嘔吐症候群への国内適応はなく、本カードの用法はいずれも適応外使用にあたる。誌面 PDF にはオープンアクセスである旨の表示があるが CC ライセンスの種別は確認できなかったため、診断編の SRC-1032 と同様に UNKNOWN とした。定義・診断は IE-008（SRC-1032、診断編ガイドライン）が担う。
  curriculum:
    kokushi: 医学各論 Ⅹ-10-B-①（アセトン血性嘔吐症<周期性嘔吐症>、a）
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: TH-033
  domain: TH
  subdomain: 慢性甲状腺炎
  assertion:
    plain_statement_ja: 慢性甲状腺炎（橋本病）の診断は、適切な臨床像を背景に、甲状腺抗原に対する血中抗体（主に抗甲状腺ペルオキシダーゼ抗体と抗サイログロブリン抗体）の証明と、甲状腺超音波検査でのエコー輝度の低下を組み合わせて行う。発症時の甲状腺機能は正常のことも甲状腺機能高進のこともあるが、多くの病型は最終的に甲状腺機能低下症へ進展する。
    condition:
      region: 国際
      対象: 慢性甲状腺炎が疑われる患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4971
    source: 'Caturegli P, De Remigis A, Rose NR. Hashimoto thyroiditis: Clinical and diagnostic criteria. Autoimmun Rev. 2014;13(4-5):391-397.'
    doi: 10.1016/j.autrev.2014.01.007
    pmid: '24434360'
    pmcid: null
    url: https://doi.org/10.1016/j.autrev.2014.01.007
    source_license: Elsevier（購読制、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は抄録で確認できた範囲に基づく（本文は購読制）。国内の関連ガイドラインの診断基準との照合はしていない。定義・疫学・組織像と甲状腺機能低下時の治療は TH-007 が担う。
  curriculum:
    kokushi: 医学各論 Ⅹ-2-B-①（慢性甲状腺炎<橋本病>、a）
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-464 (id: JlvnmLE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: TH-034
  domain: TH
  subdomain: 亜急性甲状腺炎
  assertion:
    plain_statement_ja: 亜急性甲状腺炎は破壊性甲状腺炎の一つで、甲状腺中毒期（通常3〜6週間）、甲状腺機能低下期（最長6か月）、回復という三相性の経過をたどり、多くは発症から12か月以内に甲状腺機能正常に戻るが、5〜15%は永続性甲状腺機能低下に至り、再発は1〜4%とされる。検査では赤血球沈降速度やCRPの上昇がみられ、軽度の貧血と白血球数の上昇もよく伴い、甲状腺中毒期には放射性ヨウ素摂取率は低値となる。治療は、軽症ではβ遮断薬とNSAIDsを最初に用い、NSAIDsに反応しない場合や中等度〜重度の疼痛・甲状腺中毒症状で発症した場合は、NSAIDsに代えて副腎皮質ステロイドを用いる（強い推奨、エビデンスの質は低い）。
    condition:
      region: 米国
      対象: 亜急性甲状腺炎患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-902
    source: Ross DS, Burch HB, Cooper DS, Greenlee MC, Laurberg P, Maia AL, Rivkees SA, Samuels M, Sosa JA, Stan MN, Walter MA. 2016 American Thyroid Association Guidelines for Diagnosis and Management of Hyperthyroidism and Other Causes of Thyrotoxicosis. Thyroid. 2016;26(10):1343-1421.
    doi: 10.1089/thy.2016.0229
    pmid: '27521067'
    pmcid: null
    url: https://doi.org/10.1089/thy.2016.0229
    source_license: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 経過・検査所見は同ガイドラインの [W1] 節、治療は推奨117に基づき、全文 PDF で確認した。国内承認の状況：プレドニゾロンの効能・効果には亜急性甲状腺炎が含まれ承認・保険適用がある（添付文書で確認）。ただし同ガイドラインが示す用量（プレドニゾン40 mg/日）は国内の通常用量と異なる場合がある。NSAIDs とβ遮断薬は国内承認のある薬剤だが、亜急性甲状腺炎専用の効能・効果ではない。発症率と永続性機能低下の割合（15%）は TH-008（単一地域コホート）が担い、本カードの 5〜15% はガイドラインが総説する範囲である。
  curriculum:
    kokushi: 医学各論 Ⅹ-2-B-②（亜急性甲状腺炎、a）
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-464 (id: JlvnmLE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: DM-039
  domain: DM
  subdomain: 乳酸アシドーシス
  assertion:
    plain_statement_ja: 乳酸アシドーシスは、原因によって組織低酸素を伴うA型と、組織低酸素を伴わないB型に分けられ、最も多い原因は心原性・循環血液量減少性ショック、重症心不全、重症外傷、敗血症である。診断の確定には血中乳酸値の上昇が必須であり（正常範囲はおおよそ0.5 mmol/Lから上限1.0〜2.2 mmol/Lで、上限は測定系により異なる）、アニオンギャップの上昇、とくに30 mmol/Lを超える場合は診断を支持する。治療で有効なのは原因となった病態を制御することのみであり、組織灌流の回復が要となり、薬剤や毒物が原因の場合はその中止と、除去のための透析が原因別の手段となる。重症のアシデミア（pH 7.2未満）に対する重炭酸塩投与の有効性は証明されていない。
    condition:
      region: 米国
      対象: 乳酸アシドーシスの患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4972
    source: Kraut JA, Madias NE. Lactic acidosis. N Engl J Med. 2014;371(24):2309-2319.
    doi: 10.1056/NEJMra1309483
    pmid: '25494270'
    pmcid: null
    url: https://doi.org/10.1056/NEJMra1309483
    source_license: Massachusetts Medical Society（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は総説の全文で確認した範囲に基づく。同総説では、旧来の定義（pH 7.35以下かつ重炭酸 20 mmol/L以下）は併存病態によりアシデミアが隠れるため必須要件とされていない。メトホルミン関連乳酸アシドーシスの機序・頻度・死亡率は DM-024 が担い、本カードは乳酸アシドーシス全般を扱う。薬剤名のある記載について：メトホルミンは国内で2型糖尿病に承認・保険適用があり、同総説の原因表ではメトホルミンを含む薬剤・毒物の除去に透析が有益とされる。
  curriculum:
    kokushi: 医学各論 Ⅹ-6-B-③（乳酸アシドーシス、a）
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-477 (id: JlvnmMM)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: DM-040
  domain: DM
  subdomain: 糖尿病腎症
  assertion:
    plain_statement_ja: 日本では、糖尿病患者にみられる慢性腎臓病のうち、糖尿病および糖尿病に関連する状態・合併症・治療の影響を受けうるものを糖尿病関連腎臓病（DKD）と定義し、糸球体腎炎や多発性嚢胞腎など他の明確な慢性腎臓病がある場合は DKD に含めず鑑別する。糖尿病性腎症は DKD の中で最も臨床的に重要な病態であり、その評価には尿中アルブミンと eGFR に基づく病期分類（2014年分類、2023年に小改訂）が用いられ、尿中アルブミンが予後と介入の主要な指標となる。正常アルブミン尿であっても、eGFR が 45 mL/min/1.73m2 未満の例、または eGFR が 45 以上60未満で近年の年間低下速度が 3 mL/min/1.73m2 を超える例は、高リスクの DKD として監視する。
    condition:
      region: 日本
      対象: 糖尿病患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4973
    source: 'Kanasaki K, Ueki K, Nangaku M. Diabetic kidney disease: the kidney disease relevant to individuals with diabetes. Clin Exp Nephrol. 2024;28(12):1213-1220.'
    doi: 10.1007/s10157-024-02537-z
    pmid: '39031296'
    pmcid: PMC11621156
    url: https://doi.org/10.1007/s10157-024-02537-z
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本カードは病期分類の枠組みと診断の進め方に限定し、病期ごとの数値境界（尿アルブミン・クレアチニン比と eGFR の対応表）は GN-021（SRC-589、糖尿病性腎症病期分類2014の合同委員会報告）が担うため再掲しない。2023年の小改訂では病期名が正常アルブミン尿期・微量アルブミン尿期・顕性アルブミン尿期・GFR高度低下・末期腎不全期・腎代替療法期へ変更された（枠組みと数値は不変）。この病期名は放送大学教材の追補で確認したが、合同委員会の原報告本文での照合は未了。DKD の定義は出典によれば学術的定義であり、それ自体は診断基準ではない。血糖・血圧管理と薬物療法は DM-025 が担う。
  curriculum:
    kokushi: 医学各論 Ⅹ-6-C-①（糖尿病腎症、a）
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-479 (id: JlvnmMY)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: SA-023
  domain: SA
  subdomain: 偽痛風
  assertion:
    plain_statement_ja: 急性CPP結晶関節炎（偽痛風）は、急性発症の単関節炎または少関節炎で、罹患関節の熱感・発赤・腫脹を伴い、痛風発作や化膿性関節炎と鑑別が困難なことが多い。罹患関節は膝関節が最も多く、次いで手関節であり、第1中足趾節関節の痛風様発作はまれである。発熱・悪寒などの全身症状を伴うことが多く、発作の持続は痛風の数日〜1週間より長く、数週間〜数か月に及ぶことがある。急性型は CPPD 病全体の約25%を占める。
    condition:
      region: 国際
      対象: CPPD病の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4974
    source: Rosenthal AK, Ryan LM. Calcium pyrophosphate deposition disease. N Engl J Med. 2016;374(26):2575-2584.
    doi: 10.1056/NEJMra1511117
    pmid: '27355536'
    pmcid: PMC6240444
    url: https://doi.org/10.1056/NEJMra1511117
    source_license: Massachusetts Medical Society（著者稿が PMC に収載）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は PMC に収載された著者稿の全文で確認した（出版版は購読制）。急性型が約25%という割合は、同総説が引用する推計に基づく。CPP 結晶の同定と分類基準は OS-007 が担い、急性発作の治療は SA-024 が担う。
  curriculum:
    kokushi: 医学各論 Ⅺ-2-E-②（偽痛風、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: SA-024
  domain: SA
  subdomain: 偽痛風
  assertion:
    plain_statement_ja: 急性CPP結晶関節炎の治療は非薬物療法と薬物療法の組み合わせが最適であり、冷却、関節の一時的な安静、関節穿刺とステロイド関節内注射の組み合わせで十分なことが多い。他の手段が不適当な場合や反応しない場合の急性発作には、経口または非経口の副腎皮質ステロイドを用いる。発作の予防と慢性炎症性関節炎には、消化管保護を併用した経口NSAIDsや低用量コルヒチン（0.5〜1.0 mg/日）が選択肢となり、無症候性の CPPD には治療は不要である。
    condition:
      region: 欧州
      対象: CPPD病の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4975
    source: 'Zhang W, Doherty M, Pascual E, et al. EULAR recommendations for calcium pyrophosphate deposition. Part II: Management. Ann Rheum Dis. 2011;70(4):571-575.'
    doi: 10.1136/ard.2010.139360
    pmid: '21257614'
    pmcid: null
    url: https://doi.org/10.1136/ard.2010.139360
    source_license: BMJ（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は EULAR 推奨2011年版（Part II、全9推奨、合意度79〜95%）の抄録で確認できた範囲に基づく。国内承認の状況：コルヒチンの効能・効果は痛風発作の緩解及び予防と家族性地中海熱であり、CPPD への適応はなく適応外使用にあたる。NSAIDs と副腎皮質ステロイドは国内承認のある抗炎症薬だが、CPPD 専用の効能・効果はない。臨床像は SA-023 が担う。
  curriculum:
    kokushi: 医学各論 Ⅺ-2-E-②（偽痛風、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
```


## 3. カリキュラム対応表

| カード | subdomain | kokushi | コアカリ |
|---|---|---|---|
| SZ-009 | 破瓜型統合失調症 | 医学各論 Ⅱ-2-B-②（破瓜型統合失調症、a） | PS-02-17-02 (id: JkxnuTw)；PS-02-17-03 (id: JkxnuT0)；PS-02-17-04 (id: JkxnuT4)；TBL-01-00-538 (id: JlvnmUA)；TBL-02-16-005 (id: JlAKpzE)；PS-02-17-05 (id: JkxnuT8) |
| SZ-010 | 緊張型統合失調症 | 医学各論 Ⅱ-2-B-③（緊張型統合失調症、a） | PS-02-17-02 (id: JkxnuTw)；PS-02-17-03 (id: JkxnuT0)；PS-02-17-04 (id: JkxnuT4)；TBL-01-00-538 (id: JlvnmUA)；TBL-02-16-005 (id: JlAKpzE)；PS-02-17-05 (id: JkxnuT8) |
| AX-020 | 適応障害 | 医学各論 Ⅱ-3-C-②（適応障害<適応反応症>、a） | PS-02-17-05 (id: JkxnuT8)；PS-02-17-02 (id: JkxnuTw)；TBL-02-16-002 (id: JlAKpy0) |
| AR-038 | 発作性上室頻拍 | 医学各論 Ⅴ-1-A-②（発作性上室頻拍、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-168 (id: Jlvnlsw) |
| AR-039 | 心房粗動 | 医学各論 Ⅴ-1-A-④（心房粗動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-167 (id: Jlvnlso)；TBL-02-05-032 (id: JlAKpgM) |
| AR-040 | 心室頻拍 | 医学各論 Ⅴ-1-B-②（心室頻拍、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-169 (id: Jlvnls0)；TBL-02-05-032 (id: JlAKpgM) |
| AR-041 | 洞不全症候群 | 医学各論 Ⅴ-1-C-①（洞不全症候群、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-164 (id: JlvnlsU)；TBL-02-05-032 (id: JlAKpgM) |
| AR-042 | 房室ブロック | 医学各論 Ⅴ-1-C-②（房室ブロック、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-165 (id: Jlvnlsc)；TBL-02-05-032 (id: JlAKpgM) |
| IH-031 | 無痛性虚血性心疾患 | 医学各論 Ⅴ-5-D（無痛性虚血性心疾患、a） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-028 (id: JlAKpf8) |
| MP-043 | 心囊液貯留 | 医学各論 Ⅴ-6-D-②（心囊液貯留、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-184 (id: Jlvnluw)；TBL-02-05-027 (id: JlAKpf4) |
| MP-044 | 心タンポナーデ | 医学各論 Ⅴ-6-E（心タンポナーデ、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-184 (id: Jlvnluw)；TBL-02-05-027 (id: JlAKpf4) |
| HT-024 | 睡眠時無呼吸症候群 | 医学各論 Ⅴ-7-B-④（睡眠時無呼吸症候群、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-199 (id: JlvnlwU) |
| HT-025 | 高血圧緊急症 | 医学各論 Ⅴ-7-C（高血圧緊急症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-200 (id: Jlvnlwg) |
| ES-094 | Mallory-Weiss症候群 | 医学各論 Ⅵ-1-E-①（Mallory-Weiss症候群、a） | PS-02-08-05 (id: JkxnuRY)；TBL-02-07-033 (id: JlAKplQ) |
| ES-095 | 食道裂孔ヘルニア | 医学各論 Ⅵ-9-A-①（食道裂孔ヘルニア、a） | PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc) |
| AB-117 | 消化管穿孔 | 医学各論 Ⅵ-10-E-①（消化管穿孔、a） | PS-02-08-05 (id: JkxnuRY)；TBL-01-00-308 (id: Jlvnl70) |
| AB-118 | 腹部外傷 | 医学各論 Ⅵ-11-A-①（腹部外傷、a） | null |
| AB-119 | 大腿ヘルニア | 医学各論 Ⅵ-9-A-③（大腿ヘルニア、a） | PS-02-08-05 (id: JkxnuRY)；TBL-01-00-309 (id: Jlvnl78)；TBL-01-00-310 (id: Jlvnl8E) |
| IN-114 | 痔核 | 医学各論 Ⅵ-4-D-①（痔核、a） | PS-02-08-05 (id: JkxnuRY)；TBL-01-00-267 (id: Jlvnl30)；TBL-02-07-020 (id: JlAKpkk) |
| BP-076 | 肝内胆管癌 | 医学各論 Ⅵ-6-C-②（肝内胆管癌、a） | PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)；TBL-01-00-293 (id: Jlvnl7Q) |
| BP-077 | 胆囊炎 | 医学各論 Ⅵ-7-B-①（胆囊炎、a） | PS-02-08-05 (id: JkxnuRY)；TBL-01-00-300 (id: Jlvnl5U) |
| LV-112 | アルコール性肝障害 | 医学各論 Ⅵ-6-E-③（アルコール性肝障害、a） | PS-03-05-08 (id: Jkxnubw)；GE-04-01-06 (id: JkxpswA)；TBL-01-00-289 (id: Jlvnl64) |
| IE-018 | アセトン血性嘔吐症 | 医学各論 Ⅹ-10-B-①（アセトン血性嘔吐症<周期性嘔吐症>、a） | PS-02-14-05 (id: JkxnuTA) |
| TH-033 | 慢性甲状腺炎 | 医学各論 Ⅹ-2-B-①（慢性甲状腺炎<橋本病>、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-464 (id: JlvnmLE) |
| TH-034 | 亜急性甲状腺炎 | 医学各論 Ⅹ-2-B-②（亜急性甲状腺炎、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-464 (id: JlvnmLE) |
| DM-039 | 乳酸アシドーシス | 医学各論 Ⅹ-6-B-③（乳酸アシドーシス、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-477 (id: JlvnmMM) |
| DM-040 | 糖尿病腎症 | 医学各論 Ⅹ-6-C-①（糖尿病腎症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-479 (id: JlvnmMY) |
| SA-023 | 偽痛風 | 医学各論 Ⅺ-2-E-②（偽痛風、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE) |
| SA-024 | 偽痛風 | 医学各論 Ⅺ-2-E-②（偽痛風、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE) |

## 4. 未解決事項

- SRC-4961（ICD-10 第1巻、SZ-009）の URL は本文確認に使ったミラー（NHS Class Browser）を指す。WHO 公式ブラウザへの差し替えは取り込み側の判断。SZ-009 では依頼表の側面の「潜行性の発症」は ICD-10 定義文に明記がなく主張に入れていない
- SRC-4966（JGES 非静脈瘤性上部消化管出血GL 第2版）の PMID は確認できず null（DOI で特定可能）
- SRC-4968（Lohsiriwat 2012、痔核）のライセンス表示は確認できず UNKNOWN。国内ガイドライン（肛門疾患・直腸脱診療ガイドライン2020年版・改訂第2版）は存在を確認したが本文未照合で、差し替え候補
- SRC-4970（NASPGHAN 周期性嘔吐症候群管理編GL）のライセンスは CC の種別が未確認で UNKNOWN（診断編の SRC-1032 と同じ扱い）
- MP-044（心タンポナーデ）の右房虚脱の位相は、採用ガイドラインの表が位相を限定しないため「右房の虚脱」とし、依頼表の見込み（収縮期虚脱）との差異を uncertainty に明記した。MP-043 の小規模貯留（10mm未満）の区分値は逐語確認が取れず主張に入れていない
- HT-024 の合併頻度は英語誌版の CQ で確認し、日本語版の逐語照合はしていない
- BP-076（肝内胆管癌）は採用ガイドラインに「症状」のまとまった記載がなく未収載。同ガイドラインの訂正（ESMO Open 2025）の主張範囲への影響は未確認。LV-112 の AST/ALT 比は、参照基準の表の数値を本文で逐語確認できず未収載
- DM-040（糖尿病腎症）の2023年病期名は追補資料で確認し uncertainty に明記したが、合同委員会の原報告本文での照合は未了
- SA-024（偽痛風の治療）の EULAR 推奨は2011年版。より新しい管理推奨の有無は未確認
- 既存出典の識別子補完候補：SRC-158（PMID 29330835・PMCID PMC5809582）、SRC-4245（PMCID PMC7106618）、SRC-157（カード間で記載にばらつき）、SRC-3974（PMID 38174913、既存カード TX-005 の記載）、SRC-4379・SRC-4381（マスターでは PMID が null だが既存カードが値を保持）
- 未使用の SRC 番号：SRC-4976〜5060（この回では使わない）

## 5. 引き継ぎメモ

- 睡眠時無呼吸症候群の側面と既存カードの対応：定義・診断の流れ＝PH-009（SRC-495）、CPAP の保険基準＝PH-010（SRC-3745）、CPAP 第一選択・口腔内装置＝PH-011（SRC-3746）、重症度＝PL-020、高血圧との合併＝本回 HT-024（SRC-3746）。PH-009〜011 への Ⅴ-7-B-④ の番号追加が本来の形で、採否は取り込み側の判断
- AR-041・042 の出典 SRC-4379 は不整脈の診断ガイドラインで、既存 AR-030・031 の出典 SRC-181（ペースメーカー等の適応）とは役割が異なる
- AB-118（腹部外傷）のコアカリは依頼表どおり null
- 薬剤名のあるカードはすべて uncertainty に薬剤名を特定した国内承認・適応の注記を入れた（ロラゼパムの緊張病使用は適応外、ジルチアゼム経口剤に不整脈適応なし、カペシタビンは胆道癌の国内適応なし、ナルトレキソンは国内未承認、バクロフェンは適応外、など）

## 6. ブラッシュアップA全体（第62〜67回）の残件一覧（最終回のため）

- 出典マスター内の重複疑い：SRC-1277 と SRC-1366 は同一文献（Kanagalingam 2015）（第63回 §4）。整理は取り込み側の判断
- 既存カードへの番号追加の申し送り：EP-007・EP-008 へ Ⅸ-11-C-②（第65回）、PH-009〜011 へ Ⅴ-7-B-④（本回）
- 本文が入手できれば差し替え・照合が望ましいもの：皮膚リンパ腫ガイドライン2025年版（DT-030・DT-045、第62回）、性感染症診断・治療ガイドライン2026 の本文（CM-007・BA-046、第64回）、認知症疾患診療ガイドライン2026年版の本文（ND-062、第65回）、EAU 尿路外傷ガイドラインの2026年版再構成（GU-043、第64回）
- 適応の確定が宿題のもの：IL-062 のプレドニゾロンの好酸球性肺炎への適応明記（第66回、PMDA 添付文書での確定）
