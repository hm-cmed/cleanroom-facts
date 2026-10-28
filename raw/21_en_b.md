# 内分泌・代謝・栄養・乳腺 第21回：糖質代謝、脂質・蛋白代謝、その他の代謝異常（DM-001〜038、MT-001〜036）

- 作成日：2026-10-28
- 事実票：74件（DM 38件、MT 36件、欠番なし）。目標60〜90件の範囲内。全件 `status: draft`、`verifier: null`。
- 新規出典：52件。既存出典との重複は照合の結果なし。DOI が null の出典は6件（StatPearls の章5件と日本痛風・尿酸核酸学会ガイドライン第3版。理由は出典表の確認経路に記載）、PMID が null の出典は1件（同ガイドライン）。
- 国試は依頼文 §7-1 の表のうち担当範囲の35項目すべてにカードがあり、レベル a の13項目すべてに1件以上ある。体質性黄疸・Wilson病・ヘモクロマトーシスは境界どおり作っていない（LV を正とする）。
- 注意：本回から SRC 番号が4桁（SRC-1000）に入る。依頼文では4桁可とされているが、現行の schema/fact.schema.json の source_ref のパターンは3桁（^SRC-[0-9]{3}$）のままなので、取り込み側でパターンの確認をお願いしたい。

## 1. 抽出元ホワイトリスト（新規出典52件）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 使用カード |
|---|---|---|---|---|---|---|---|
| SRC-941 | Kawasaki E, et al. Diagnostic criteria for acute-onset type 1 diabetes mellitus (2012): Report of the Committee on Type 1 Diabetes in Japan Diabetes Society. J Diabetes Investig. 2014;5(1):115–118. | 10.1111/jdi.12119 | 24843746 | CC BY-NC-ND | RESTRICTED | PMC本文（抄録・診断基準表）で内容と識別子を確認 | DM-001 |
| SRC-942 | Seino Y, et al. Report of the Committee on the Classification and Diagnostic Criteria of Diabetes Mellitus. J Diabetes Investig. 2010;1(5):212–228. | 10.1111/j.2040-1124.2010.00074.x | 24843435 | CC表示未確認（学会委員会報告） | RESTRICTED | DOI・PMIDは書誌記録で照合。基準値は同基準を引用する資料で確認。PMCIDは確認できず null とした | DM-003 |
| SRC-943 | Gyeltshen T, Tanaka H, Katanoda K. Trends in self-reported current diabetes care use in Japan: an analysis of the Comprehensive Survey of Living Conditions (1986–2022). BMJ Open Diabetes Res Care. 2026;14(4). | 10.1136/bmjdrc-2026-006042 | 42457244 | CC BY 4.0 | OPEN | PMC本文で内容・識別子・ライセンスを確認 | DM-004 |
| SRC-944 | Araki E, et al. Japanese Clinical Practice Guideline for Diabetes 2019. J Diabetes Investig. 2020;11(4):1020–1076. | 10.1111/jdi.13306 | 33021749 | CC BY-NC-ND 4.0 | RESTRICTED | PMC本文（各章・表・図）で内容と識別子を確認 | DM-002、DM-005、DM-009、DM-011、DM-013、DM-015、DM-019 |
| SRC-945 | American Diabetes Association Professional Practice Committee. 6. Glycemic Goals and Hypoglycemia: Standards of Care in Diabetes—2025. Diabetes Care. 2025;48(Suppl.1):S128–S145. | 10.2337/dc25-S006 | 39651981 | © American Diabetes Association（CC表示なし） | UNKNOWN | 抄録・本文で内容と識別子を確認。PMCIDは確認できず null とした | DM-006 |
| SRC-946 | Bouchi R, et al. A consensus statement from the Japan Diabetes Society: a proposed algorithm for pharmacotherapy in people with type 2 diabetes — 2nd edition (English version). Diabetol Int. 2024;15(3):327–345. | 10.1007/s13340-024-00723-8 | 39101173 | CC表示未確認（学会コンセンサス） | RESTRICTED | PMC本文で内容と識別子を確認。並行する J Diabetes Investig 版（PMID 38988282）とは別版であり、本成果物では PMC で本文を確認した Diabetol Int 版に統一した | DM-007、DM-008 |
| SRC-947 | Shimada A, et al. New diagnostic criteria (2023) for slowly progressive type 1 diabetes (SPIDDM): Report from Committee on Type 1 Diabetes of the Japan Diabetes Society (English version). J Diabetes Investig. 2024;15(2):254–257. | 10.1111/jdi.14121 | 38184802 | CC BY-NC-ND 4.0 | RESTRICTED | PMC本文で内容と識別子を確認（2024年に訂正報あり） | DM-010 |
| SRC-948 | Tosur M, Philipson LH. Precision diabetes: Lessons learned from maturity-onset diabetes of the young (MODY). J Diabetes Investig. 2022;13(9):1465–1471. | 10.1111/jdi.13860 | 35638342 | CC BY-NC 4.0 | RESTRICTED | PMC本文（抄録・本文）で内容・識別子・ライセンスを確認 | DM-012 |
| SRC-949 | Japan Diabetes Society/Japan Geriatrics Society Joint Committee. Committee Report: Glycemic targets for elderly patients with diabetes. J Diabetes Investig. 2017;8(1):126–128. | 10.1111/jdi.12599 | 28054465 | CC BY-NC-ND | RESTRICTED | PMC本文で内容と識別子を確認 | DM-014 |
| SRC-950 | Knowler WC, et al.; Diabetes Prevention Program Research Group. Reduction in the incidence of type 2 diabetes with lifestyle intervention or metformin. N Engl J Med. 2002;346(6):393–403. | 10.1056/NEJMoa012512 | 11832527 | © Massachusetts Medical Society（CC表示なし） | UNKNOWN | 抄録および PMC の著者版で内容と識別子を確認 | DM-016 |
| SRC-951 | TODAY Study Group. Long-Term Complications in Youth-Onset Type 2 Diabetes. N Engl J Med. 2021;385(5):416–426. | 10.1056/NEJMoa2100165 | 34320286 | © Massachusetts Medical Society（CC表示なし） | UNKNOWN | 抄録および PMC で内容と識別子を確認 | DM-017 |
| SRC-952 | Kim T, Choi SH. Diabetes Mellitus and Infectious Diseases: Current Evidence and Clinical Implications. Diabetes Metab J. 2025;49(5):915–933. | 10.4093/dmj.2025.0508 | 40859782 | CC BY-NC 4.0 | RESTRICTED | PMC本文で内容・識別子・ライセンスを確認 | DM-018 |
| SRC-953 | Frid AH, et al. New Insulin Delivery Recommendations. Mayo Clin Proc. 2016;91(9):1231–1255. | 10.1016/j.mayocp.2016.06.010 | 27594187 | © Mayo Foundation / Elsevier（CC表示なし） | UNKNOWN | DOI・PMIDは PubMed 書誌記録で照合。内容は原著の公表資料で確認。PMCIDは確認できず null とした | DM-020 |
| SRC-956 | Umpierrez GE, Davis GM, ElSayed NA, et al. Hyperglycemic Crises in Adults With Diabetes: A Consensus Report. Diabetes Care. 2024;47(8):1257-1275. | 10.2337/dci24-0032 | 39052901 | © 2024 by the American Diabetes Association and the European Association for the Study of Diabetes（CC ライセンス表示なし） | RESTRICTED | Crossref と NCBI ID変換で DOI・PMID・PMCID を照合。本文（PMC 収載の同一コンセンサス報告、Diabetologia 併載版）で診断基準・治療・回復基準の数値を確認 | DM-021、DM-022、DM-023 |
| SRC-957 | DeFronzo R, Fleming GA, Chen K, Bicsak TA. Metformin-associated lactic acidosis: Current perspectives on causes and risk. Metabolism. 2016;65(2):20-29. | 10.1016/j.metabol.2015.10.014 | 26773926 | © 2015 The Authors. Published by Elsevier Inc. All rights reserved.（CC ライセンス表示は確認できず） | UNKNOWN | PubMed で DOI・PMID を照合し、抄録で機序・頻度・死亡率を確認。Crossref にライセンス表示なし | DM-024 |
| SRC-958 | American Diabetes Association Professional Practice Committee. 11. Chronic Kidney Disease and Risk Management: Standards of Care in Diabetes—2025. Diabetes Care. 2025;48(Suppl 1):S239-S251. | 10.2337/dc25-S011 | 39651975 | © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし） | RESTRICTED | Crossref と NCBI ID変換で DOI・PMID・PMCID を照合。PMC 本文で推奨文（11.2〜11.5c）を確認 | DM-025 |
| SRC-959 | Pop-Busui R, Boulton AJM, Feldman EL, et al. Diabetic Neuropathy: A Position Statement by the American Diabetes Association. Diabetes Care. 2017;40(1):136-154. | 10.2337/dc16-2042 | 27999003 | © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし） | RESTRICTED | Crossref と NCBI ID変換で DOI・PMID・PMCID を照合。PMC 本文でスクリーニングと疼痛治療の推奨文を確認 | DM-026、DM-027 |
| SRC-960 | Solomon SD, Chew E, Duh EJ, et al. Diabetic Retinopathy: A Position Statement by the American Diabetes Association. Diabetes Care. 2017;40(3):412-418. | 10.2337/dc16-2641 | 28223445 | © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし） | RESTRICTED | Crossref と NCBI ID変換で DOI・PMID・PMCID を照合。PMC 本文でスクリーニングと治療の推奨文を確認 | DM-028 |
| SRC-961 | Bus SA, Sacco ICN, Monteiro-Soares M, et al. Guidelines on the prevention of foot ulcers in persons with diabetes (IWGDF 2023 update). Diabetes/Metabolism Research and Reviews. 2024;40(3):e3651. | 10.1002/dmrr.3651 | 37302121 | CC BY-NC-ND 4.0 | RESTRICTED | PubMed で DOI・PMID を照合し抄録を確認。リスク層別化の区分と頻度はガイドライン本文の表で確認。ライセンスは Crossref で確認 | DM-029 |
| SRC-963 | American Diabetes Association Professional Practice Committee. 10. Cardiovascular Disease and Risk Management: Standards of Care in Diabetes—2025. Diabetes Care. 2025;48(Suppl 1):S207-S238. | 10.2337/dc25-S010 | 39651970 | © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし） | RESTRICTED | Crossref と NCBI ID変換で DOI・PMID・PMCID を照合。PMC 本文で推奨文（10.4、10.42a、10.42b ほか）を確認 | DM-030 |
| SRC-965 | American Diabetes Association Professional Practice Committee. 6. Glycemic Goals and Hypoglycemia: Standards of Care in Diabetes—2025. Diabetes Care. 2025;48(Suppl 1):S128-S145. | 10.2337/dc25-S006 | 39651981 | © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし） | RESTRICTED | Crossref と NCBI ID変換で DOI・PMID・PMCID を照合。PMC 本文で低血糖の分類と治療の記述を確認 | DM-031、DM-033 |
| SRC-966 | Cryer PE, Axelrod L, Grossman AB, et al. Evaluation and Management of Adult Hypoglycemic Disorders: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2009;94(3):709-728. | 10.1210/jc.2008-1410 | 19088155 | CC BY-NC-ND 4.0 | RESTRICTED | PubMed で DOI・PMID を照合し抄録を確認。内因性高インスリン血症の診断基準の数値はガイドライン本文で確認。ライセンスは Crossref で確認 | DM-032、DM-034、DM-035 |
| SRC-967 | Bodnar TW, Acevedo MJ, Pietropaolo M. Management of Non-Islet-Cell Tumor Hypoglycemia: A Clinical Review. The Journal of Clinical Endocrinology & Metabolism. 2014;99(3):713-722. | 10.1210/jc.2013-3382 | 24423303 | © 2014 by The Endocrine Society（CC ライセンス表示なし） | UNKNOWN | PubMed で DOI・PMID・PMCID を照合。PMC 本文で検査パターンと治療を確認。Crossref にライセンス表示なし | DM-037 |
| SRC-968 | Censi S, Mian C, Betterle C. Insulin autoimmune syndrome: from diagnosis to clinical management. Annals of Translational Medicine. 2018;6(17):335. | 10.21037/atm.2018.07.32 | 30306074 | © 2018 Annals of Translational Medicine. All rights reserved.（CC ライセンス表示は確認できず） | UNKNOWN | PubMed で DOI・PMID・PMCID を照合。PMC 本文で定義・誘因・経過・治療を確認 | DM-036 |
| SRC-969 | Misselwitz B, Butter M, Verbeke K, Fox MR. Update on lactose malabsorption and intolerance: pathogenesis, diagnosis and clinical management. Gut. 2019;68(11):2080-2091. | 10.1136/gutjnl-2019-318404 | 31427404 | Re-use permitted under CC BY-NC. No commercial re-use.（CC BY-NC） | RESTRICTED | PubMed で DOI・PMID・PMCID を照合し抄録を確認。ライセンス表示は PubMed 収載の著作権表示で確認 | DM-038 |
| SRC-971 | Okamura T, Tsukamoto K, Arai H, et al. Japan Atherosclerosis Society (JAS) Guidelines for Prevention of Atherosclerotic Cardiovascular Diseases 2022. Journal of Atherosclerosis and Thrombosis. 2024;31(6):641-853. | 10.5551/jat.GL2022 | 38123343 | CC BY-NC-SA 4.0 | RESTRICTED | PubMed で書誌・PMID・PMCID を照合し、PMC 全文でライセンス表示（CC BY-NC-SA 4.0）を確認。脂質異常症の診断基準（Table 1）、リスク区分別の管理目標（Table 5）、二次性脂質異常症の原因（第6章）、その他の原発性高脂血症（第5章）、食事・運動療法の推奨値、メタボリックシンドローム診断基準の転載表を本文・表で確認 | MT-001、MT-003、MT-007、MT-011、MT-017、MT-018 |
| SRC-972 | Harada-Shiba M, Arai H, Ohmura H, et al. Guidelines for the Diagnosis and Treatment of Adult Familial Hypercholesterolemia 2022. Journal of Atherosclerosis and Thrombosis. 2023;30(5):558-586. | 10.5551/jat.CR005 | 36682773 | CC BY-NC-SA 4.0 | RESTRICTED | PubMed で書誌・PMID・PMCID を照合し、PMC 全文でライセンス表示（CC BY-NC-SA 4.0）を確認。成人の診断基準（Table 1：未治療 LDL-C 180 mg/dL 以上、黄色腫、アキレス腱肥厚は X 線で男性 8.0 mm・女性 7.5 mm 以上など）、日本の頻度（約300人に1人）、治療目標（一次予防 100 mg/dL 未満、二次予防 70 mg/dL 未満）と薬物療法の順序を本文で確認 | MT-002、MT-005 |
| SRC-973 | Mach F, Baigent C, Catapano AL, et al. 2019 ESC/EAS Guidelines for the management of dyslipidaemias: lipid modification to reduce cardiovascular risk. European Heart Journal. 2020;41(1):111-188. | 10.1093/eurheartj/ehz455 | 31504418 | ライセンス表示を確認できず | UNKNOWN | PubMed で書誌・PMID を照合。出版社ページの本文で、リスク区分別の LDL-C 目標（Table 7：超高リスクは 50% 以上の低下と 55 mg/dL 未満、高リスクは 70 mg/dL 未満、中等度 100 mg/dL 未満、低リスク 116 mg/dL 未満）と non-HDL-C の副次目標を確認。CC 表示は確認できなかった | MT-004 |
| SRC-974 | Sabatine MS, Giugliano RP, Keech AC, et al. Evolocumab and Clinical Outcomes in Patients with Cardiovascular Disease (FOURIER). The New England Journal of Medicine. 2017;376(18):1713-1722. | 10.1056/NEJMoa1615664 | 28304224 | ライセンス表示を確認できず | UNKNOWN | PubMed で書誌・PMID を照合し、抄録で LDL-C の変化（中央値 92 から 30 mg/dL、59% 低下）、主要評価項目（9.8% 対 11.3%、HR 0.85）と主要副次評価項目（5.9% 対 7.4%、HR 0.80）、追跡期間中央値 2.2 年を確認。CC 表示は確認できなかった | MT-006 |
| SRC-975 | Examination Committee of Criteria for 'Obesity Disease' in Japan; Japan Society for the Study of Obesity. New criteria for 'obesity disease' in Japan. Circulation Journal. 2002;66(11):987-992. | 10.1253/circj.66.987 | 12419927 | ライセンス表示を確認できず | UNKNOWN | PubMed で書誌・PMID を照合し、抄録で BMI 25 の根拠（BMI 25 で肥満関連合併症の平均数が 1.0 を超える）と内臓脂肪面積 100 cm² の根拠（合併症数が 1.0 を超える値）を確認。CC 表示は確認できなかった | MT-009 |
| SRC-976 | Wilding JPH, Batterham RL, Calanna S, et al. Once-Weekly Semaglutide in Adults with Overweight or Obesity (STEP 1). The New England Journal of Medicine. 2021;384(11):989-1002. | 10.1056/NEJMoa2032183 | 33567185 | ライセンス表示を確認できず | UNKNOWN | PubMed で書誌・PMID を照合し、抄録で対象（糖尿病のない BMI 30 以上、または合併症ありで 27 以上、1,961 人）、68 週の体重変化（-14.9% 対 -2.4%、差 -12.4 ポイント）、5% 以上減量の達成割合（86.4% 対 31.5%）を確認。CC 表示は確認できなかった | MT-010 |
| SRC-977 | Mahmoud R, Kimonis V, Butler MG. Genetics of Obesity in Humans: A Clinical Review. International Journal of Molecular Sciences. 2022;23(19):11005. | 10.3390/ijms231911005 | 36232301 | CC BY 4.0 | OPEN | PubMed で書誌・PMID・PMCID を照合し、PMC 全文でライセンス表示（CC BY 4.0）を確認。症候群性肥満の例、単一遺伝子性肥満の原因遺伝子（MC4R が小児肥満で最も多く罹患者の約 4%）、Prader-Willi 症候群の遺伝学的機序（15q11.2-q13 の父性欠失が約 70%）を本文で確認 | MT-012 |
| SRC-978 | Gounden V, Easton-Carr R, Jialal I. Hypoalbuminemia. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK526080. | null | 30252336 | NCBI Bookshelf 収載。章ページのライセンス表示はアクセス制限のため確認できず | UNKNOWN | PubMed レコードで書誌・PMID・Bookshelf ID を確認。同レコードに DOI の記載がないため DOI は null。要約でアルブミンの基準濃度（35〜50 g/L）、半減期（14〜21 日）、炎症性メディエーターによる合成抑制を確認 | MT-013 |
| SRC-979 | Wechalekar AD, Gillmore JD, Hawkins PN. Systemic amyloidosis. The Lancet. 2016;387:2641-2654. | 10.1016/S0140-6736(15)01274-X | 26719234 | ライセンス表示を確認できず | UNKNOWN | PubMed で書誌・PMID を照合し、抄録で AL 型が全身性アミロイドーシスの中で最も多いこと、型判定（質量分析）の重要性、心アミロイドーシスの評価法、AL 型の生存の改善を確認。CC 表示は確認できなかった | MT-014 |
| SRC-980 | Maurer MS, Schwartz JH, Gundapaneni B, et al. Tafamidis Treatment for Patients with Transthyretin Amyloid Cardiomyopathy (ATTR-ACT). The New England Journal of Medicine. 2018;379(11):1007-1016. | 10.1056/NEJMoa1805689 | 30145929 | ライセンス表示を確認できず | UNKNOWN | PubMed で書誌・PMID を照合し、抄録で対象（441 人、30 か月）、全死亡（29.5% 対 42.9%、HR 0.70）、心血管関連入院（相対リスク比 0.68）を確認。CC 表示は確認できなかった | MT-015 |
| SRC-981 | Yang AL, McNabb-Baltar J. Hypertriglyceridemia and acute pancreatitis. Pancreatology. 2020;20(5):795-800. | 10.1016/j.pan.2020.06.005 | 32571534 | ライセンス表示を確認できず | UNKNOWN | PubMed で書誌・PMID を照合し、抄録で急性膵炎の原因として 3 番目に多いこと、基礎の脂質代謝異常と二次的要因の重なり、重症化しやすいこと、治療（アフェレーシス、インスリン療法を含む）を確認。CC 表示は確認できなかった | MT-008 |
| SRC-982 | Styne DM, Arslanian SA, Connor EL, et al. Pediatric Obesity-Assessment, Treatment, and Prevention: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2017;102(3):709-757. | 10.1210/jc.2016-2573 | 28359099 | ライセンス表示を確認できず | UNKNOWN | PubMed で書誌・PMID・PMCID を照合し、抄録（結論部）で米国の小児・青年の約 17% が肥満であること、内分泌性の原因はまれで成長の鈍化を伴うこと、合併症スクリーニングと遺伝性症候群検査の適応、薬物療法と外科療法の位置づけを確認。CC 表示は確認できなかった | MT-016 |
| SRC-986 | Kiani AK, Dhuli K, Donato K, et al. Main nutritional deficiencies. J Prev Med Hyg. 2022;63(2 Suppl 3):E93-E101. | 10.15167/2421-4248/jpmh2022.63.2S3.2752 | 36479498 | CC BY-NC-ND（Europe PMCのライセンス表示） | RESTRICTED | Europe PMC で書誌・DOI・PMID・PMCID・ライセンスを照合。全文で、栄養不十分と栄養欠乏の定義、欠乏の原因（嚥下障害・嘔吐・吸収障害・慢性疾患）、バイオマーカー（葉酸・ビタミンC・B群・ビタミンD等の血中濃度）による評価を確認。各ビタミン（A・C・E・K）と亜鉛の欠乏症状の記載も MT-022・029・035 の照合に使用 | MT-019 |
| SRC-987 | Chandrakumar A, Bhardwaj A, 't Jong GW. Review of thiamine deficiency disorders: Wernicke encephalopathy and Korsakoff psychosis. J Basic Clin Physiol Pharmacol. 2019;30(2):153-162. | 10.1515/jbcpp-2018-0075 | 30281514 | ライセンス表示を確認できず | UNKNOWN | PubMed レコードで書誌・DOI・PMIDを確認し、抄録でチアミンピロリン酸が炭水化物利用の経路に必須であること、欠乏がアルコール性・非アルコール性の要因で生じること、Wernicke 脳症と Korsakoff 症候群の位置づけを確認。脚気の症状（末梢神経障害・心血管機能障害）は Kennedy らの総説（SRC-1000）の表、Wernicke 脳症の三徴と完全な三徴が3分の1未満であることは StatPearls「Wernicke-Korsakoff Syndrome」章（Akhouri ら、PMID 28613480）の抜粋で照合 | MT-020 |
| SRC-988 | Devalia V, Hamilton MS, Molloy AM; British Committee for Standards in Haematology. Guidelines for the diagnosis and treatment of cobalamin and folate disorders. Br J Haematol. 2014;166(4):496-513. | 10.1111/bjh.12959 | 24942828 | ライセンス表示を確認できず（© John Wiley & Sons） | UNKNOWN | PubMed 抄録で、臨床像が最も重要であること、血清コバラミンが第一選択検査で血漿メチルマロン酸・ホモシステインが第二選択であること、葉酸は血清葉酸が第一選択であること、臨床像と検査が食い違う場合は治療を遅らせないことを確認。巨赤芽球性貧血との関係は Wolffenbuttel ら（PMID 31193945、Mayo Clin Proc Innov Qual Outcomes. 2019、CC BY-NC-ND）の抄録と Kennedy らの総説（SRC-1000）の表で照合 | MT-021 |
| SRC-989 | Maxfield L, Daley SF, Crane JS. Vitamin C Deficiency. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK493187. | null | 29630239 | NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず | UNKNOWN | PubMed レコードで書誌・PMID・Bookshelf ID を確認し、同レコードに DOI の記載がないことを確認したため DOI は null。抜粋で壊血病がビタミンC欠乏による臨床症候群であること、ビタミンCが皮膚・軟骨・骨・歯の成長と修復に必須であることを確認。壊血病の症状（歯肉出血、点状・斑状出血、毛孔性角化とらせん状体毛、創傷治癒遅延、関節痛）は Kiani らの総説（SRC-986）の全文、ペラグラの症状（光過敏性皮膚炎、下痢、精神症状）は Kennedy らの総説（SRC-1000）の表で照合 | MT-022 |
| SRC-990 | Reddy P, Jialal I. Biochemistry, Fat Soluble Vitamins. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK534869. | null | 30521290 | NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず | UNKNOWN | PubMed レコードで書誌・PMID・Bookshelf ID を確認し、DOI の記載がないため DOI は null。抜粋で脂溶性ビタミン A・D・E・K の役割（視覚、骨、免疫、凝固）と、本章が各ビタミンの欠乏症候群と毒性を扱う総説であることを確認。ビタミンAの欠乏（夜盲）と過剰（催奇形性、肝障害、頭蓋内圧亢進）は Carazo ら（PMID 34069881、Nutrients. 2021、CC BY 4.0）の全文、ビタミンD過剰（高カルシウム血症、血清25(OH)D 150 ng/mL超が指標）は Marcinowska-Suchowierska ら（PMID 30294301、Front Endocrinol. 2018、CC BY）の抄録、ビタミンK欠乏（PT-INR延長、新生児のビタミンK欠乏性出血症）は Kiani らの総説（SRC-986）の全文と Daley らの章（PMID 30725668）の抜粋、ビタミンE欠乏（脂肪吸収・代謝の異常に伴う、未熟児で貯蔵が少ない）は Kemnic らの章（PMID 30085593）の抜粋で照合 | MT-023、MT-035 |
| SRC-991 | Hisatome I, Ichida K, Mineo I, et al. Japanese Society of Gout and Uric & Nucleic Acids 2019 Guidelines for Management of Hyperuricemia and Gout 3rd edition. Gout and Uric & Nucleic Acids. 2020;44(Suppl):1-40. | null | null | 日本痛風・尿酸核酸学会のガイドライン。CC表示なし | RESTRICTED | J-STAGE 掲載の英語版全文で、高尿酸血症の定義（血清尿酸値7.0 mg/dL超）、病型分類（産生過剰型・排泄低下型・混合型、腎負荷型の提唱）、CQ1（発作治療の3剤は同等に推奨）・CQ2（痛風結節では6.0 mg/dL以下を維持）・CQ6（コルヒチンカバーは長期間）・CQ7（飲酒制限を含む食事教育）の推奨と治療アルゴリズムの図を確認。日本語版の書誌（日本痛風・尿酸核酸学会ガイドライン改訂委員会編、診断と治療社、2018年12月、第3版、ISBN 978-4-7878-2375-5）は図書館の書誌情報で確認。J-STAGE と Crossref で DOI の付与を確認できず、PubMed にも収載がないため DOI・PMID は null | MT-024、MT-025、MT-026 |
| SRC-992 | FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. Arthritis Care Res (Hoboken). 2020;72(6):744-760. | 10.1002/acr.24180 | 32391934 | PMC収載は著者原稿。CC表示なし（© American College of Rheumatology） | UNKNOWN | PubMed 抄録で強い推奨の内容（痛風結節・画像上の骨破壊・頻回発作では全例に尿酸降下療法を開始、アロプリノールが第一選択で開始用量100 mg/日以下、血清尿酸6 mg/dL未満を目標とする treat-to-target、開始時の抗炎症予防投与3〜6か月、発作治療はコルヒチン・NSAIDs・グルココルチコイド）を確認。重症例で血清尿酸5 mg/dL未満を維持する点は EULAR 2016 推奨（Richette ら、PMID 27457514）の抄録で照合 | MT-027 |
| SRC-993 | Balwani M, Desnick RJ. The porphyrias: advances in diagnosis and treatment. Blood. 2012;120(23):4496-4504. | 10.1182/blood-2012-05-423186 | 22791288 | PMC収載は著者原稿。CC表示なし | UNKNOWN | PubMed 抄録で、8つの遺伝的に異なる疾患を急性肝性・肝性皮膚・赤芽球性皮膚の3群に分類すること、晩発性皮膚ポルフィリン症が最も多く鉄過剰によるウロポルフィリン脱炭酸酵素の阻害で生じること、急性発作へのヘマチン投与、晩発性皮膚ポルフィリン症への瀉血、DNAに基づく診断を確認 | MT-028 |
| SRC-994 | Jagadeesan S, Kaliyadan F. Acrodermatitis Enteropathica. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK441835. | null | 28722865 | NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず | UNKNOWN | PubMed レコードで書誌・PMID・Bookshelf ID を確認し、DOI の記載がないため DOI は null。抜粋で、亜鉛トランスポーター遺伝子 SLC39A4 の変異による腸管での亜鉛吸収障害が原因であること、亜鉛が200を超える金属酵素の構成要素であること、後天性亜鉛欠乏でも同様の臨床像が現れることを確認。皮膚病変・下痢・脱毛の症状は Kiani らの総説（SRC-986）の全文（亜鉛欠乏の症状）で照合 | MT-029 |
| SRC-995 | Salik I, Rawla P. Marfan Syndrome. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK537339. | null | 30726024 | NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず | UNKNOWN | PubMed レコードで書誌・PMID・Bookshelf ID を確認し、DOI の記載がないため DOI は null。抜粋で、頻度（3,000〜5,000人に1人）、FBN1 遺伝子と常染色体優性遺伝、眼・心血管・骨格の所見、大動脈合併症が生命予後を決めること、β遮断薬などによる後負荷軽減と待機的手術、分子遺伝学的検査の位置づけを確認 | MT-030 |
| SRC-996 | Malfait F, Francomano C, Byers P, et al. The 2017 international classification of the Ehlers-Danlos syndromes. Am J Med Genet C Semin Med Genet. 2017;175(1):8-26. | 10.1002/ajmg.c.31552 | 28306229 | ライセンス表示を確認できず（© Wiley Periodicals） | UNKNOWN | PubMed 抄録で、関節過可動性・皮膚過伸展性・組織脆弱性という特徴、2017年国際分類が13亜型を認めること、過可動型を除く全亜型で原因遺伝子変異の同定による確定診断が必要であることを確認 | MT-031 |
| SRC-997 | Germain DP. Pseudoxanthoma elasticum. Orphanet J Rare Dis. 2017;12(1):85. | 10.1186/s13023-017-0639-8 | 28486967 | CC BY 4.0（Europe PMCの表示） | OPEN | PubMed 抄録と Europe PMC で書誌・DOI・PMID・PMCID・ライセンスを照合。抄録で ABCC6 変異と常染色体劣性遺伝、有病率（25,000〜100,000人に1人）、皮膚・眼（網膜色素線条と脈絡膜新生血管）・血管の病変、無機ピロリン酸（PPi）低下の機序、根治療法がないことを確認 | MT-032 |
| SRC-998 | Benn CL, et al. Physiology of hyperuricemia and urate-lowering treatments. Front Med (Lausanne). 2018;5:160. | 10.3389/fmed.2018.00160 | 29904633 | CC BY 4.0（Europe PMCの表示） | OPEN | Europe PMC でライセンスを確認し、全文で、キサンチンオキシダーゼがヒポキサンチンから尿酸までの変換を担うこと、ヒトは機能するウリカーゼを欠くため尿酸がプリン代謝の最終産物であること、排泄は約3分の2が尿中（通常の尿中排泄量は成人で620±75 mg/日）で残りが消化管からであること、糸球体で濾過された尿酸の91〜95%が近位尿細管で再吸収されること、再吸収の中心が URAT1（SLC22A12）で分泌に ABCG2 などが関わることを確認 | MT-033 |
| SRC-999 | Cameron JS, Moro F, Simmonds HA. Gout, uric acid and purine metabolism in paediatric nephrology. Pediatr Nephrol. 1993;7(1):105-118. | 10.1007/BF00861588 | 8439471 | ライセンス表示を確認できず | UNKNOWN | PubMed 抄録で、HPRT 欠損による尿酸産生過剰と、常染色体優性の尿酸再吸収亢進による家族性腎不全（腎機能障害に先行するか不釣り合いな高尿酸血症を伴う）の記載、アロプリノールによる治療の位置づけを確認。Lesch-Nyhan 症候群の神経症状（ジストニア、舞踏アテトーゼ、自傷行為）と X 連鎖性遺伝は Torres & Puig（PMID 18067674、Orphanet J Rare Dis. 2007、CC BY）の抄録で照合 | MT-034 |
| SRC-1000 | Kennedy DO. B Vitamins and the Brain: Mechanisms, Dose and Efficacy—A Review. Nutrients. 2016;8(2):68. | 10.3390/nu8020068 | 26828517 | CC BY 4.0（Crossrefのライセンス表示） | OPEN | Crossref で書誌と CC BY 4.0 ライセンスを照合し、全文で、ナイアシンの耐容上限量（米国・カナダで35 mg/日、100 mg超での紅潮、1 g以上の長期摂取での消化器症状とまれな肝障害）、ビタミンB6の耐容上限量（米国で100 mg/日、1,000 mg超の長期摂取での可逆性感覚性ニューロパチー）、ビタミンB6欠乏の症状（貧血、易刺激性、抑うつ、認知機能低下、痙攣）と危険因子（アルコール依存、加齢に伴う吸収低下）を確認。ペラグラと脚気の症状の照合にも使用 | MT-036 |

未使用の SRC 番号（941〜1010 のうち）：SRC-954・955・962・964・970・983〜985・1001〜1010。

## 2. 事実票

```yaml
- id: DM-001
  domain: DM
  subdomain: 1型糖尿病の病態と診断
  assertion:
    plain_statement_ja: 1型糖尿病は膵β細胞の破壊により絶対的なインスリン欠乏に至る病型であり、日本では劇症・急性発症・緩徐進行の3亜型に分類される。急性発症（自己免疫性）1型糖尿病は、高血糖症状が出現してからおおむね3か月以内にケトーシスまたはケトアシドーシスを発症し、発症時からインスリン治療を継続して必要とし、膵島関連自己抗体が陽性であることを診断の基本とする。自己抗体の存在が確認できない場合は、空腹時血清Cペプチド0.6 ng/mL未満など内因性インスリン分泌の欠乏を示す所見をもって診断できる。
    condition:
      region: 日本
      study: 日本糖尿病学会1型糖尿病委員会の診断基準（2012年基準、2014年掲載）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-941
    source: 'Kawasaki E, et al. Diagnostic criteria for acute-onset type 1 diabetes mellitus (2012): Report of the Committee on Type 1 Diabetes in Japan Diabetes Society. J Diabetes Investig. 2014;5(1):115–118.'
    doi: 10.1111/jdi.12119
    pmid: '24843746'
    pmcid: PMC4025242
    url: https://doi.org/10.1111/jdi.12119
    source_license: Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND)
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 診断基準の数値（3か月以内、空腹時血清Cペプチド0.6 ng/mL未満）は原著の診断基準表から読み取った。インスリン治療への言及は診断基準の記述であり、個別製剤の国内承認・保険適用の確認は本調査の対象外である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-472 (id: JlvnmL0)'
    kokushi: 医学各論 Ⅹ-6-A-①（1型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-002
  domain: DM
  subdomain: 1型糖尿病の治療（インスリン療法）
  assertion:
    plain_statement_ja: 1型糖尿病では発症時からインスリン療法が必須であり、1日3〜4回の頻回注射法または持続皮下インスリン注入療法（CSII）が標準的な治療法である。インスリン製剤は作用の発現と持続時間により超速効型・速効型・中間型・持効型溶解・配合溶解などに分類され、基礎インスリン（中間型・持効型）と追加インスリン（速効型・超速効型）を組み合わせて用いる。強化インスリン療法に血糖自己測定を組み合わせることで、細小血管症の発症と進展を抑制できる。
    condition:
      region: 日本
      study: 日本糖尿病学会「糖尿病診療ガイドライン2019」英語版（第6章 インスリン療法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-944
    source: Araki E, et al. Japanese Clinical Practice Guideline for Diabetes 2019. J Diabetes Investig. 2020;11(4):1020–1076.
    doi: 10.1111/jdi.13306
    pmid: '33021749'
    pmcid: PMC7378414
    url: https://doi.org/10.1111/jdi.13306
    source_license: Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: インスリン製剤の分類と用法はガイドライン本文に基づく記載であり、国内で承認・保険適用のある治療を前提としているが、個別製剤ごとの承認内容・保険適用の確認は本調査では行っていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-472 (id: JlvnmL0)'
    kokushi: 医学各論 Ⅹ-6-A-①（1型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-003
  domain: DM
  subdomain: 2型糖尿病の診断基準（日本）
  assertion:
    plain_statement_ja: 日本の糖尿病診断基準では、空腹時血糖値126 mg/dL以上、75 g経口ブドウ糖負荷試験2時間値200 mg/dL以上、随時血糖値200 mg/dL以上、HbA1c（NGSP値）6.5%以上のいずれかを「糖尿病型」とする。同一日の採血で血糖値とHbA1cの両方が糖尿病型であれば、1回の検査で糖尿病と診断できる。血糖値のみが糖尿病型の場合は、口渇・多飲・多尿・体重減少などの典型的な症状があるか確実な糖尿病網膜症を認めれば診断でき、いずれもなければ別日の再検査で糖尿病型を再確認する。
    condition:
      region: 日本
      study: 日本糖尿病学会「糖尿病の分類と診断基準に関する委員会報告」
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-942
    source: Seino Y, et al. Report of the Committee on the Classification and Diagnostic Criteria of Diabetes Mellitus. J Diabetes Investig. 2010;1(5):212–228.
    doi: 10.1111/j.2040-1124.2010.00074.x
    pmid: '24843435'
    pmcid: null
    url: https://doi.org/10.1111/j.2040-1124.2010.00074.x
    source_license: 日本糖尿病学会委員会報告。CCライセンス表示は確認できなかった
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 基準値は委員会報告の診断基準（本文および表）から読み取った。本論文のPMCIDは確認できなかったため null とした。ライセンスはPMCページで直接確認できておらず、学会委員会報告として RESTRICTED とした。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-004
  domain: DM
  subdomain: 日本の糖尿病の疫学
  assertion:
    plain_statement_ja: 2024年の国民健康・栄養調査では、20歳以上で「糖尿病が強く疑われる者」の割合は12.9%（男性17.7%、女性9.3%）であり、その数は1100万人を超えるとされる。過去に糖尿病と診断された者のうち、現在治療を受けている者は67.4%であった。また、国民生活基礎調査にもとづく年齢調整済みの自己申告による糖尿病治療中の者の割合は、1986年から2022年にかけて男性で2.2%から8.3%へ、女性で1.7%から4.4%へ増加した。
    condition:
      region: 日本
      study: 国民生活基礎調査（1986〜2022年）の解析および2024年国民健康・栄養調査の公表値
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-943
    source: 'Gyeltshen T, Tanaka H, Katanoda K. Trends in self-reported current diabetes care use in Japan: an analysis of the Comprehensive Survey of Living Conditions (1986–2022). BMJ Open Diabetes Res Care. 2026;14(4).'
    doi: 10.1136/bmjdrc-2026-006042
    pmid: '42457244'
    pmcid: PMC13374473
    url: https://doi.org/10.1136/bmjdrc-2026-006042
    source_license: Creative Commons Attribution (CC BY) 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 2024年の割合と人数は、国民健康・栄養調査の公表値として原著論文に引用されたものである。治療中の者の割合は自己申告にもとづく調査値であり、診断確定例の割合とは異なる。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-005
  domain: DM
  subdomain: 血糖管理目標（日本）
  assertion:
    plain_statement_ja: 日本の血糖管理目標では、合併症予防のための目標はHbA1c 7.0%未満とされ、これに対応する血糖値はおおむね空腹時血糖130 mg/dL未満、食後2時間血糖180 mg/dL未満である。血糖正常化を目指す際の目標はHbA1c 6.0%未満、低血糖などの副作用や治療強化が困難な場合の目標はHbA1c 8.0%未満とされ、年齢・罹病期間・合併症・低血糖リスクなどを考慮して患者ごとに設定する。
    condition:
      region: 日本
      study: 日本糖尿病学会「糖尿病診療ガイドライン2019」英語版（血糖管理目標の図）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-944
    source: Araki E, et al. Japanese Clinical Practice Guideline for Diabetes 2019. J Diabetes Investig. 2020;11(4):1020–1076.
    doi: 10.1111/jdi.13306
    pmid: '33021749'
    pmcid: PMC7378414
    url: https://doi.org/10.1111/jdi.13306
    source_license: Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: HbA1c目標の階層（6.0%未満・7.0%未満・8.0%未満）と対応する血糖値は、ガイドラインの図から読み取った値である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-006
  domain: DM
  subdomain: 血糖管理目標（米国ADA）
  assertion:
    plain_statement_ja: 米国の基準では、多くの非妊娠成人についてHbA1c 7%未満が血糖管理の目標とされる。食前血糖は80〜130 mg/dL、食後のピーク血糖は180 mg/dL未満が目安であり、持続血糖測定では目標範囲内（70〜180 mg/dL）の時間が70%超、70 mg/dL未満の時間が4%未満、54 mg/dL未満の時間が1%未満が目標とされる。血糖状態の評価は少なくとも年2回行い、目標未達成や治療変更時は3か月ごとに行う。低血糖はレベル1（70 mg/dL未満）、レベル2（54 mg/dL未満）、レベル3（他者の援助を要する重篤なイベント）に分類される。
    condition:
      region: 米国
      study: 米国糖尿病学会 Standards of Care in Diabetes—2025 第6章（血糖目標と低血糖）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-945
    source: 'American Diabetes Association Professional Practice Committee. 6. Glycemic Goals and Hypoglycemia: Standards of Care in Diabetes—2025. Diabetes Care. 2025;48(Suppl.1):S128–S145.'
    doi: 10.2337/dc25-S006
    pmid: '39651981'
    pmcid: null
    url: https://doi.org/10.2337/dc25-S006
    source_license: © American Diabetes Association. CCライセンス表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 目標値と低血糖の分類は同章の表および推奨文から読み取った。日本の目標（DM-005）とは別基準である。本論文のPMCIDは確認できなかったため null とした。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-007
  domain: DM
  subdomain: 2型糖尿病の薬物療法（経口薬の選択）
  assertion:
    plain_statement_ja: 2型糖尿病の薬物療法では、まずインスリン治療の適応の有無を判断し、HbA1cの目標を設定したうえで病態に応じて薬剤を選択する。日本では肥満（BMI 25以上）をインスリン抵抗性の代理指標とし、肥満例ではビグアナイド薬、SGLT2阻害薬、チアゾリジン薬、GLP-1受容体作動薬などを、非肥満のインスリン分泌低下例ではインスリン分泌促進薬やDPP-4阻害薬を中心に検討する。次に安全性を確認し、SU薬やグリニド薬の低血糖リスク、腎機能障害・肝障害・心不全における禁忌を避ける（メトホルミンはeGFR 30未満で禁忌）。心血管疾患・心不全・慢性腎臓病を合併する場合は、SGLT2阻害薬やGLP-1受容体作動薬による追加の利益を考慮する。
    condition:
      region: 日本
      study: 日本糖尿病学会コンセンサスステートメント「2型糖尿病治療薬アルゴリズム第2版」英語版
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-946
    source: 'Bouchi R, et al. A consensus statement from the Japan Diabetes Society: a proposed algorithm for pharmacotherapy in people with type 2 diabetes — 2nd edition (English version). Diabetol Int. 2024;15(3):327–345.'
    doi: 10.1007/s13340-024-00723-8
    pmid: '39101173'
    pmcid: PMC11291844
    url: https://doi.org/10.1007/s13340-024-00723-8
    source_license: 日本糖尿病学会コンセンサスステートメント。CCライセンス表示は確認できなかった
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤クラスの選択手順は同コンセンサス本文に基づく国内診療を前提とした記載であり、個別製剤ごとの国内承認・保険適用の確認は本調査では行っていない。同アルゴリズムには並行する別誌の英語版があり、PMIDが異なるため、本カードではDiabetol Int版に識別子を統一した。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-008
  domain: DM
  subdomain: 2型糖尿病の注射療法（GLP-1受容体作動薬とインスリン）
  assertion:
    plain_statement_ja: GLP-1受容体作動薬は、血糖依存性のインスリン分泌促進とグルカゴン分泌抑制によって血糖を下げ、単独使用では低血糖のリスクが低く、プラセボと比べて平均約2 kgの体重減少効果が報告されている。インスリン療法にはインスリン依存状態などの絶対的適応と、経口薬で管理目標に達しない場合などの相対的適応があり、病態と管理状況に応じて導入する。GIP/GLP-1受容体作動薬であるチルゼパチドは、日本で2023年4月に発売された。
    condition:
      region: 日本
      study: 日本糖尿病学会コンセンサスステートメント「2型糖尿病治療薬アルゴリズム第2版」英語版
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-946
    source: 'Bouchi R, et al. A consensus statement from the Japan Diabetes Society: a proposed algorithm for pharmacotherapy in people with type 2 diabetes — 2nd edition (English version). Diabetol Int. 2024;15(3):327–345.'
    doi: 10.1007/s13340-024-00723-8
    pmid: '39101173'
    pmcid: PMC11291844
    url: https://doi.org/10.1007/s13340-024-00723-8
    source_license: 日本糖尿病学会コンセンサスステートメント。CCライセンス表示は確認できなかった
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 体重減少の数値（平均約2 kg）は同文献本文から確認した。記載した注射薬は同コンセンサスに基づく国内診療を前提としたものであり、個別製剤ごとの国内承認・保険適用の確認は本調査では行っていない（チルゼパチドの国内発売時期は同文献の記載による）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-009
  domain: DM
  subdomain: 糖尿病の食事療法と運動療法
  assertion:
    plain_statement_ja: 食事療法では、総エネルギー摂取量を目標体重にエネルギー係数を掛けて設定する。目標体重は65歳未満では身長（m）の2乗に22を掛けた値、65歳以上では22〜25を掛けた値を目安とし、エネルギー係数は身体活動量に応じて軽い労作で25〜30、普通の労作で30〜35、重い労作で35以上 kcal/kgを用いる。食物繊維は1日20 g以上、食塩は男性7.5 g未満・女性6.5 g未満（高血圧合併時は6.0 g未満）を目安とする。運動療法では、中等度の有酸素運動を週150分以上・週3日以上（連続した休止は2日まで）行い、レジスタンス運動を週2〜3回組み合わせる。
    condition:
      region: 日本
      study: 日本糖尿病学会「糖尿病診療ガイドライン2019」英語版（第3章 食事療法、第4章 運動療法）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-944
    source: Araki E, et al. Japanese Clinical Practice Guideline for Diabetes 2019. J Diabetes Investig. 2020;11(4):1020–1076.
    doi: 10.1111/jdi.13306
    pmid: '33021749'
    pmcid: PMC7378414
    url: https://doi.org/10.1111/jdi.13306
    source_license: Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 目標体重・エネルギー係数・各栄養素の目安と運動量は、ガイドライン本文および表から読み取った値である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)；TBL-02-13-007 (id: JlAKpsU)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-010
  domain: DM
  subdomain: 緩徐進行1型糖尿病と劇症1型糖尿病
  assertion:
    plain_statement_ja: 緩徐進行1型糖尿病（SPIDDM）の確定診断には、(1)経過中のいずれかの時点で膵島関連自己抗体が陽性であること、(2)原則として診断時にケトーシスやケトアシドーシスがなく直ちにインスリン治療を必要としないこと、(3)発症（診断）から3か月を超えてインスリン治療が必要となり、最終観察時点で空腹時血清Cペプチドが0.6 ng/mL未満であること、の3項目すべてを満たす必要がある。(1)と(2)のみを満たす場合はSPIDDM（probable）とする。日本では1型糖尿病は劇症・急性発症・緩徐進行の3亜型に分類され、劇症1型糖尿病はそのうち急激な経過をとる亜型である。
    condition:
      region: 日本
      study: 日本糖尿病学会1型糖尿病委員会 SPIDDM診断基準（2023年）英語版
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-947
    source: 'Shimada A, et al. New diagnostic criteria (2023) for slowly progressive type 1 diabetes (SPIDDM): Report from Committee on Type 1 Diabetes of the Japan Diabetes Society (English version). J Diabetes Investig. 2024;15(2):254–257.'
    doi: 10.1111/jdi.14121
    pmid: '38184802'
    pmcid: PMC10804889
    url: https://doi.org/10.1111/jdi.14121
    source_license: Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: SPIDDMの基準値は原著の診断基準表から読み取った（2024年に文言の訂正報がある）。劇症1型糖尿病については、引用したSPIDDM診断基準にはその診断基準の詳細が含まれていないため、本カードでは亜型としての位置づけのみを記載し、診断数値は記載していない。インスリン治療への言及は診断基準の記述であり、個別製剤の国内承認・保険適用の確認は本調査の対象外である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-472 (id: JlvnmL0)'
    kokushi: 医学各論 Ⅹ-6-A-①（1型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-011
  domain: DM
  subdomain: 二次性糖尿病
  assertion:
    plain_statement_ja: 日本の糖尿病の分類では、糖尿病は1型、2型、その他の特定の機序・疾患による糖尿病、妊娠糖尿病の4つに大別される。「その他の特定の機序・疾患による糖尿病」には、膵β細胞機能やインスリン作用に関わる遺伝子異常、膵外分泌疾患、内分泌疾患、肝疾患、薬剤や化学物質によるもの、感染症、まれな免疫介在性糖尿病、その他の遺伝症候群に伴う糖尿病が含まれ、二次性糖尿病はこの区分に位置づけられる。背景にある原因疾患や原因薬剤の同定が診断と治療の出発点となる。
    condition:
      region: 日本
      study: 日本糖尿病学会「糖尿病診療ガイドライン2019」英語版（分類表）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-944
    source: Araki E, et al. Japanese Clinical Practice Guideline for Diabetes 2019. J Diabetes Investig. 2020;11(4):1020–1076.
    doi: 10.1111/jdi.13306
    pmid: '33021749'
    pmcid: PMC7378414
    url: https://doi.org/10.1111/jdi.13306
    source_license: Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 分類の区分と含まれる疾患群は、ガイドラインの分類表から読み取った。個別の原因疾患ごとの診断基準や頻度は本カードの範囲外である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-6-A-③（二次性糖尿病、遺伝子異常による糖尿病、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-012
  domain: DM
  subdomain: 遺伝子異常による糖尿病（MODY）
  assertion:
    plain_statement_ja: 若年発症糖尿病（MODY）は単一遺伝子の異常による糖尿病で、常染色体優性遺伝を示し、多くは25歳未満に発症する。遺伝子診断が確定した症例の90%以上をGCK、HNF1A、HNF4Aの3遺伝子が占め、HNF1Bも主要な原因遺伝子である。GCK-MODYは軽度で非進行性の高血糖を呈し、原則として薬物治療を必要としない。HNF1A-MODYは思春期から若年成人期に発症する最も頻度の高い症候性MODYで、スルホニル尿素薬に高い感受性を示すため、食事療法とスルホニル尿素薬が治療の中心となる。小児糖尿病におけるMODYの頻度は1.1〜6.5%と推定され、1型や2型糖尿病と誤診されている症例が多いとされる。
    condition:
      region: 米国
      study: MODYに関する総説（米国・欧州の研究データを含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-948
    source: 'Tosur M, Philipson LH. Precision diabetes: Lessons learned from maturity-onset diabetes of the young (MODY). J Diabetes Investig. 2022;13(9):1465–1471.'
    doi: 10.1111/jdi.13860
    pmid: '35638342'
    pmcid: PMC9434589
    url: https://doi.org/10.1111/jdi.13860
    source_license: Creative Commons Attribution-NonCommercial (CC BY-NC) 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頻度と原因遺伝子の割合は総説の記載に基づき、対象集団（地域・年齢）によって異なる。スルホニル尿素薬への言及は総説に基づくものであり、MODYに対する国内の承認・保険適用の扱いは本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-6-A-③（二次性糖尿病、遺伝子異常による糖尿病、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-013
  domain: DM
  subdomain: 妊娠糖尿病（分類と管理）
  assertion:
    plain_statement_ja: 妊娠中の糖代謝異常は、妊娠糖尿病、妊娠中の明らかな糖尿病、糖尿病合併妊娠に分類される。妊娠糖尿病は、75 g経口ブドウ糖負荷試験で空腹時92 mg/dL以上、1時間値180 mg/dL以上、2時間値153 mg/dL以上のいずれか1点以上を満たし、妊娠中の明らかな糖尿病には該当しないものと定義される。妊娠中の明らかな糖尿病は、空腹時血糖126 mg/dL以上またはHbA1c 6.5%以上などで診断される。血糖管理の目標は空腹時95 mg/dL未満、食後1時間値140 mg/dL未満または食後2時間値120 mg/dL未満であり、食事・運動療法で目標に達しない場合はインスリン療法を行う。産後は6〜12週に75 g経口ブドウ糖負荷試験で糖代謝を再評価する。
    condition:
      region: 日本
      study: 日本糖尿病学会「糖尿病診療ガイドライン2019」英語版（第17章 妊娠）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-944
    source: Araki E, et al. Japanese Clinical Practice Guideline for Diabetes 2019. J Diabetes Investig. 2020;11(4):1020–1076.
    doi: 10.1111/jdi.13306
    pmid: '33021749'
    pmcid: PMC7378414
    url: https://doi.org/10.1111/jdi.13306
    source_license: Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 診断値と管理目標はガイドラインの表から読み取った。本カードは糖尿病としての分類と血糖管理に絞り、分娩や胎児の管理など妊娠管理の詳細は範囲外とした。インスリン療法への言及はガイドラインに基づく記載であり、個別製剤の国内承認・保険適用の確認は本調査では行っていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-6-A-④（妊娠糖尿病、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-014
  domain: DM
  subdomain: 高齢者の糖尿病
  assertion:
    plain_statement_ja: 高齢者糖尿病の血糖管理目標は、認知機能とADLによって、カテゴリーI（認知機能正常かつADL自立）、カテゴリーII（軽度認知障害から軽度認知症、または手段的ADLの低下）、カテゴリーIII（中等度以上の認知症、基本的ADLの低下、または多併存疾患あり）に分けて個別化する。基本となる目標はHbA1c 7.0%未満であり、状態によって6.0%未満を目指す場合や、カテゴリーIIIでは8.5%未満まで緩和する場合がある。インスリン、SU薬、グリニド薬など重症低血糖を起こしやすい薬剤を使用する場合は、目標に下限値を設ける。高齢者は重症低血糖を起こしやすく、重症低血糖は認知機能の低下や心血管イベントのリスクと関連する。
    condition:
      region: 日本
      study: 日本糖尿病学会・日本老年医学会合同委員会報告（高齢者糖尿病の血糖コントロール目標）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-949
    source: 'Japan Diabetes Society/Japan Geriatrics Society Joint Committee. Committee Report: Glycemic targets for elderly patients with diabetes. J Diabetes Investig. 2017;8(1):126–128.'
    doi: 10.1111/jdi.12599
    pmid: '28054465'
    pmcid: PMC5217949
    url: https://doi.org/10.1111/jdi.12599
    source_license: Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND)
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: カテゴリー別の目標値の詳細は原著では図として提示されており、本カードの数値は本文で確認できた範囲と図から読み取った値を含む。薬剤クラス名は委員会報告に基づく記載であり、個別製剤ごとの国内承認・保険適用の確認は本調査では行っていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-015
  domain: DM
  subdomain: 糖尿病のモニタリング
  assertion:
    plain_statement_ja: 糖尿病の血糖モニタリングでは、HbA1cが血糖管理状態を評価する基本的な指標となる。血糖自己測定（SMBG）は、1型糖尿病およびインスリン治療中の2型糖尿病において有用である（推奨グレードA）。持続血糖測定（CGM）にはリアルタイムCGMと間欠スキャン式CGMがあり、リアルタイムCGMは1型・2型糖尿病でSMBGより優れる可能性があり、間欠スキャン式CGMは低血糖の持続時間を短縮しうる。
    condition:
      region: 日本
      study: 日本糖尿病学会「糖尿病診療ガイドライン2019」英語版（第7章 血糖モニタリング）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-944
    source: Araki E, et al. Japanese Clinical Practice Guideline for Diabetes 2019. J Diabetes Investig. 2020;11(4):1020–1076.
    doi: 10.1111/jdi.13306
    pmid: '33021749'
    pmcid: PMC7378414
    url: https://doi.org/10.1111/jdi.13306
    source_license: Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 推奨の表現（グレードおよび「可能性」）はガイドラインのCQ本文に基づく。CGMやSMBGの個別機器の保険適用の詳細は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-016
  domain: DM
  subdomain: 2型糖尿病の発症予防
  assertion:
    plain_statement_ja: 米国のDiabetes Prevention Programでは、空腹時および負荷後血糖が高値の非糖尿病成人3234人を平均2.8年追跡した結果、2型糖尿病の発症率は100人年あたりプラセボ群11.0、メトホルミン群7.8、生活習慣介入群4.8であり、生活習慣介入はプラセボと比べて発症を58%、メトホルミンは31%減少させた。生活習慣介入の目標は体重7%以上の減量と週150分以上の身体活動であり、3年間の発症予防に必要な治療数は生活習慣介入で6.9、メトホルミンで13.9であった。
    condition:
      region: 米国
      study: 無作為化比較試験（Diabetes Prevention Program）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-950
    source: Knowler WC, et al.; Diabetes Prevention Program Research Group. Reduction in the incidence of type 2 diabetes with lifestyle intervention or metformin. N Engl J Med. 2002;346(6):393–403.
    doi: 10.1056/NEJMoa012512
    pmid: '11832527'
    pmcid: PMC1370926
    url: https://doi.org/10.1056/NEJMoa012512
    source_license: © Massachusetts Medical Society. CCライセンス表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値は原著論文の抄録および本文から確認した。メトホルミンによる予防は本試験（米国）の条件での結果であり、糖尿病発症予防を目的とした国内の承認・保険適用は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-017
  domain: DM
  subdomain: 思春期・小児の2型糖尿病
  assertion:
    plain_statement_ja: 米国のTODAY研究の長期追跡では、10〜17歳で発症した若年発症2型糖尿病の500人（追跡終了時の平均年齢26.4歳、平均罹病期間13.3年）において、高血圧の累積発症率は67.5%、脂質異常症は51.6%、糖尿病腎症は54.8%、神経障害は32.4%に達し、網膜症の有病率は2017〜2018年の評価で51.0%であった。1つ以上の合併症をもつ者は60.1%、2つ以上をもつ者は28.4%であり、若年発症の2型糖尿病では合併症が若い年齢から高率にみられる。
    condition:
      region: 米国
      study: TODAY研究コホートの長期観察研究
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-951
    source: TODAY Study Group. Long-Term Complications in Youth-Onset Type 2 Diabetes. N Engl J Med. 2021;385(5):416–426.
    doi: 10.1056/NEJMoa2100165
    pmid: '34320286'
    pmcid: PMC8697255
    url: https://doi.org/10.1056/NEJMoa2100165
    source_license: © Massachusetts Medical Society. CCライセンス表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値は原著論文の抄録から確認した。米国の若年発症コホートの結果であり、日本の小児・思春期2型糖尿病の頻度や経過にそのまま当てはまるかは確認していない。糖尿病腎症の病期分類には触れていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-018
  domain: DM
  subdomain: 糖尿病と感染症
  assertion:
    plain_statement_ja: 糖尿病では、一般的な感染症および重症感染症のリスクが1.5〜4倍に上昇する。慢性的な高血糖は好中球の走化性や酸化的バースト、補体の活性化を障害し、血管障害や神経障害も感染のリスクを高める。特徴的な感染症として、尿路感染症（気腫性腎盂腎炎を含む）、肺炎、結核、皮膚・軟部組織感染症、糖尿病足感染症、ムーコル症などが挙げられる。予防には、インフルエンザワクチン、肺炎球菌ワクチン、新型コロナワクチン、B型肝炎ワクチン、帯状疱疹ワクチン、破傷風・ジフテリアトキソイドなどのワクチン接種と、足の観察が推奨される。
    condition:
      region: 韓国
      study: 糖尿病と感染症に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-952
    source: 'Kim T, Choi SH. Diabetes Mellitus and Infectious Diseases: Current Evidence and Clinical Implications. Diabetes Metab J. 2025;49(5):915–933.'
    doi: 10.4093/dmj.2025.0508
    pmid: '40859782'
    pmcid: PMC12436038
    url: https://doi.org/10.4093/dmj.2025.0508
    source_license: Creative Commons Attribution-NonCommercial (CC BY-NC) 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: リスクの倍率（1.5〜4倍）は総説の記載に基づく範囲であり、感染症の種類や対象集団によって異なる。ワクチンの国内の接種推奨の詳細は本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-019
  domain: DM
  subdomain: 糖尿病患者の周術期管理
  assertion:
    plain_statement_ja: 糖尿病患者の周術期には、全身管理を必要とする手術においてインスリン治療による血糖管理が推奨される。これは普段インスリン治療を受けていないインスリン非依存状態の患者でも同様であり、手術や重症感染症の際にはインスリン治療の導入を検討する。インスリン治療の絶対的適応はインスリン依存状態と高血糖性の昏睡であり、全身管理を要する手術や重症感染症は、インスリン治療が推奨される相対的な適応として位置づけられる。
    condition:
      region: 日本
      study: 日本糖尿病学会「糖尿病診療ガイドライン2019」英語版（第2章・第6章のインスリン適応）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-944
    source: Araki E, et al. Japanese Clinical Practice Guideline for Diabetes 2019. J Diabetes Investig. 2020;11(4):1020–1076.
    doi: 10.1111/jdi.13306
    pmid: '33021749'
    pmcid: PMC7378414
    url: https://doi.org/10.1111/jdi.13306
    source_license: Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 周術期の具体的な血糖目標値や経口薬の中止・再開の詳細は、引用したガイドライン英語版の該当箇所で確認できた範囲を超えるため記載していない。インスリン治療への言及はガイドラインに基づく記載であり、個別製剤の国内承認・保険適用の確認は本調査では行っていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)'
    kokushi: 医学各論 Ⅹ-6-A-②（2型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-020
  domain: DM
  subdomain: インスリン治療の実際（注射手技と低血糖予防）
  assertion:
    plain_statement_ja: インスリン注射手技の推奨では、ペン型注入器では4 mm、シリンジでは6 mmの最も短い針を、年齢や体型にかかわらず用いることが勧められる。過度に長い針は筋肉内注射のリスクを高め、インスリンの吸収が速まることで血糖変動や低血糖のリスクが増す。注射部位を正しくローテーションすることでリポハイパートロフィーを減らすことができる。リポハイパートロフィーのある部位への注射は吸収が低下しばらつくため、予期せぬ血糖変動や低血糖の原因となりうる。リポハイパートロフィーはインスリン治療中の患者の約3分の1にみられると報告されており、注射針は単回使用が推奨される。
    condition:
      region: 米国
      study: インスリン投与に関する国際専門家会議（FITTER）の推奨（Mayo Clinic Proceedings掲載）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-953
    source: Frid AH, et al. New Insulin Delivery Recommendations. Mayo Clin Proc. 2016;91(9):1231–1255.
    doi: 10.1016/j.mayocp.2016.06.010
    pmid: '27594187'
    pmcid: null
    url: https://doi.org/10.1016/j.mayocp.2016.06.010
    source_license: © Mayo Foundation for Medical Education and Research / Elsevier. CCライセンス表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 針の長さとリポハイパートロフィーの頻度は原著およびその公表資料から確認した。本論文のPMCIDは確認できなかったため null とした。本カードは注射手技に関するものであり、インスリン製剤そのものの国内承認、および個別の注射デバイスの保険適用は確認していない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-472 (id: JlvnmL0)'
    kokushi: 医学各論 Ⅹ-6-A-①（1型糖尿病、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-021
  domain: DM
  subdomain: 糖尿病ケトアシドーシス
  assertion:
    plain_statement_ja: 糖尿病ケトアシドーシス（DKA）の診断には3つの要件をすべて満たすことが必要である。第1に血糖200 mg/dL以上または糖尿病の既往（D）、第2にケトーシス、すなわち血中β-ヒドロキシ酪酸3.0 mmol/L以上または尿ケトン2+以上（K）、第3に代謝性アシドーシス、すなわちpH 7.3未満または重炭酸18 mmol/L未満あるいはその両方（A）である。重症度はpH・重炭酸・β-ヒドロキシ酪酸と意識状態で分ける。アニオンギャップは第一選択の診断基準としては推奨されない。
    condition:
      region: 国際
      study: コンセンサスレポート（ADA・EASD・JBDS・AACE・DTS、2024年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-956
    source: 'Umpierrez GE, Davis GM, ElSayed NA, et al. Hyperglycemic Crises in Adults With Diabetes: A Consensus Report. Diabetes Care. 2024;47(8):1257-1275.'
    doi: 10.2337/dci24-0032
    pmid: '39052901'
    pmcid: PMC11272983
    url: https://doi.org/10.2337/dci24-0032
    source_license: © 2024 by the American Diabetes Association and the European Association for the Study of Diabetes（CC ライセンス表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 重症度の区分（軽症：pH 7.25超・7.30未満、重炭酸15〜18 mmol/L、β-ヒドロキシ酪酸3.0〜6.0 mmol/L／中等症：pH 7.0〜7.25、重炭酸10〜15 mmol/L未満／重症：pH 7.0未満、重炭酸10 mmol/L未満、β-ヒドロキシ酪酸6.0 mmol/L超）はコンセンサス報告の診断基準の表から読み取った。血糖の基準値は2024年版で200 mg/dLに改められており、2009年版の250 mg/dLとは異なる。数値は同報告のDiabetes Care版と同一内容の併載版本文で確認した。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-475 (id: JlvnmMA)'
    kokushi: 医学各論 Ⅹ-6-B-①（糖尿病ケトアシドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-022
  domain: DM
  subdomain: 糖尿病ケトアシドーシス
  assertion:
    plain_statement_ja: DKAの治療の柱は輸液、インスリン、カリウム補充と、誘因となった病態の治療である。輸液は等張液（生理食塩水またはバランス晶質液）を、心・腎の合併症がなければ最初の2〜4時間は500〜1000 mL/時で開始し、不足分を24〜48時間で補正する。インスリンは短時間作用型の持続静注を0.1単位/kg/時で開始し、血糖が250 mg/dL未満になったら5〜10%ブドウ糖液を併用して0.05単位/kg/時に減らし、血糖をおおむね200 mg/dLに保ちながらケトアシドーシスが回復するまで続ける。カリウムは血清値が5.0 mmol/Lを下回ったら補充を始めて4〜5 mmol/Lを維持し、来院時に3.5 mmol/L未満の場合はインスリンの開始を遅らせてカリウム補充を先行させる。重炭酸のルーチン投与は推奨されず、pH 7.0未満の重度のアシドーシスで検討する。回復の定義は、血中ケトン0.6 mmol/L未満かつ静脈血pH 7.3以上または重炭酸18 mmol/L以上である。
    condition:
      region: 国際
      study: コンセンサスレポート（ADA・EASD・JBDS・AACE・DTS、2024年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-956
    source: 'Umpierrez GE, Davis GM, ElSayed NA, et al. Hyperglycemic Crises in Adults With Diabetes: A Consensus Report. Diabetes Care. 2024;47(8):1257-1275.'
    doi: 10.2337/dci24-0032
    pmid: '39052901'
    pmcid: PMC11272983
    url: https://doi.org/10.2337/dci24-0032
    source_license: © 2024 by the American Diabetes Association and the European Association for the Study of Diabetes（CC ライセンス表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤（インスリン製剤、輸液製剤、塩化カリウム）の国内承認・保険適用は、本調査では添付文書での個別確認を行っていない（未確認）。数値はコンセンサス報告本文で確認した。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-475 (id: JlvnmMA)'
    kokushi: 医学各論 Ⅹ-6-B-①（糖尿病ケトアシドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-023
  domain: DM
  subdomain: 高血糖高浸透圧症候群
  assertion:
    plain_statement_ja: 高血糖高浸透圧症候群（HHS）の診断には4つの要件が必要である。血糖600 mg/dL以上、計算した有効血清浸透圧300 mOsm/kg超または総血清浸透圧320 mOsm/kg超、著明なケトーシスの欠如（β-ヒドロキシ酪酸3.0 mmol/L未満または尿ケトン2+未満）、アシドーシスの欠如（pH 7.3以上かつ重炭酸15 mmol/L以上）である。DKAとの重なり（混合型）は高血糖クリーゼの3分の1以上にみられる。治療は輸液を先行させ、血糖の低下は1時間あたり90〜120 mg/dLを超えないようにし、浸透圧の低下は1時間あたり3.0〜8.0 mOsm/kg以内、血清ナトリウムの低下は24時間あたり10 mmol/L以内にとどめる。ケトーシスがないか軽度の場合はインスリン持続静注を0.05単位/kg/時で開始し、著明なケトーシスを伴う混合型では0.1単位/kg/時とする。回復の目安は、血清浸透圧300 mOsm/kg未満、血糖250 mg/dL未満、尿量0.5 mL/kg/時を超えること、意識状態の改善である。
    condition:
      region: 国際
      study: コンセンサスレポート（ADA・EASD・JBDS・AACE・DTS、2024年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-956
    source: 'Umpierrez GE, Davis GM, ElSayed NA, et al. Hyperglycemic Crises in Adults With Diabetes: A Consensus Report. Diabetes Care. 2024;47(8):1257-1275.'
    doi: 10.2337/dci24-0032
    pmid: '39052901'
    pmcid: PMC11272983
    url: https://doi.org/10.2337/dci24-0032
    source_license: © 2024 by the American Diabetes Association and the European Association for the Study of Diabetes（CC ライセンス表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: HHSの回復の定義については統一したコンセンサスがなく、本文に示された著者らの目安によった。DKAとの重なりの頻度は本文の記述による。薬剤（インスリン製剤、輸液製剤）の国内承認・保険適用は、本調査では個別に確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-476 (id: JlvnmMI)'
    kokushi: 医学各論 Ⅹ-6-B-②（高血糖高浸透圧症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-024
  domain: DM
  subdomain: 乳酸アシドーシス
  assertion:
    plain_statement_ja: 乳酸アシドーシスは、全身の低酸素を伴わない状況でも起こりうる代謝性アシドーシスである。糖尿病治療薬に関連するものとして重要なのはメトホルミン関連乳酸アシドーシスで、メトホルミンは主として肝臓でミトコンドリア呼吸を抑えて血漿乳酸値を濃度依存的に上昇させるため、腎機能障害などで血中濃度が高くなった状態に、肝硬変、敗血症、低灌流など乳酸の産生や除去をさらに乱す二次的な出来事が重なったときに発症しやすい。報告される発症頻度は10万患者年あたり10件未満と低い一方、死亡率は約50%に達するとされる。
    condition:
      region: 米国
      study: 総説（メトホルミン関連乳酸アシドーシス）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-957
    source: 'DeFronzo R, Fleming GA, Chen K, Bicsak TA. Metformin-associated lactic acidosis: Current perspectives on causes and risk. Metabolism. 2016;65(2):20-29.'
    doi: 10.1016/j.metabol.2015.10.014
    pmid: '26773926'
    pmcid: null
    url: https://doi.org/10.1016/j.metabol.2015.10.014
    source_license: © 2015 The Authors. Published by Elsevier Inc. All rights reserved.（CC ライセンス表示は確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードは抄録で確認できた範囲に基づく。乳酸アシドーシス一般の診断閾値（乳酸値やpHの数値）は、実際に開いた一次資料の範囲では確認できなかったため数値を書いていない。頻度と死亡率は総説が引用する報告に基づく値である。メトホルミンの国内承認・保険適用（腎機能障害時の投与制限を含む）は、本調査では確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-477 (id: JlvnmMM)'
    kokushi: 医学各論 Ⅹ-6-B-③（乳酸アシドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-025
  domain: DM
  subdomain: 糖尿病腎症
  assertion:
    plain_statement_ja: 糖尿病に合併する慢性腎臓病（CKD）の管理では、血糖管理の最適化と血圧管理（目標130/80 mmHg未満）が進行抑制の基本である。高血圧を伴う非妊娠の患者では、ACE阻害薬またはARBが、中等度に増加したアルブミン尿（UACR 30〜299 mg/g）で推奨され、高度に増加したアルブミン尿（300 mg/g以上）またはeGFR 60 mL/min/1.73m2未満では最大耐容量まで用いることが強く推奨される。2型糖尿病とCKDのある患者では、有効性が示されたSGLT2阻害薬がeGFR 20 mL/min/1.73m2以上の場合にCKDの進行と心血管イベントの抑制のために推奨され、有効性が示されたGLP-1受容体作動薬も心血管リスクと腎臓病進行の抑制に推奨される。アルブミン尿を伴うCKDでは、eGFR 25 mL/min/1.73m2以上を条件に、臨床試験で有効性が示された非ステロイド型ミネラルコルチコイド受容体拮抗薬も選択肢となり、使用時には血清カリウムのモニタリングが必要である。
    condition:
      region: 米国
      study: 診療ガイドライン（ADA Standards of Care in Diabetes—2025、第11章）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-958
    source: 'American Diabetes Association Professional Practice Committee. 11. Chronic Kidney Disease and Risk Management: Standards of Care in Diabetes—2025. Diabetes Care. 2025;48(Suppl 1):S239-S251.'
    doi: 10.2337/dc25-S011
    pmid: '39651975'
    pmcid: PMC11635029
    url: https://doi.org/10.2337/dc25-S011
    source_license: © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 境界：糖尿病腎症の病期分類は第15回のGN-021を正とし、本カードでは作成せず、管理（血糖・血圧管理と進行抑制）の側面のみを扱った。薬剤（ACE阻害薬、ARB、SGLT2阻害薬、GLP-1受容体作動薬、非ステロイド型MRAであるフィネレノン）の国内承認・保険適用は薬剤ごとに異なり、本調査では個別の添付文書確認が完了していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-479 (id: JlvnmMY)'
    kokushi: 医学各論 Ⅹ-6-C-①（糖尿病腎症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-026
  domain: DM
  subdomain: 糖尿病神経障害
  assertion:
    plain_statement_ja: 遠位対称性多発神経障害のスクリーニングは、2型糖尿病では診断時から、1型糖尿病では診断の5年後から、少なくとも年1回行う。評価は病歴の聴取に加えて、細い神経線維の機能をみる温度覚またはピン痛覚と、太い神経線維の機能をみる128 Hz音叉による振動覚で行い、潰瘍と切断のリスクがある足を評価するために10 gモノフィラメント検査を年1回行う。電気生理学的検査や神経内科への紹介は、臨床像が非典型的な場合や診断が不確かな場合を除き、スクリーニングには通常不要である。
    condition:
      region: 米国
      study: ポジションステートメント（ADA、2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-959
    source: 'Pop-Busui R, Boulton AJM, Feldman EL, et al. Diabetic Neuropathy: A Position Statement by the American Diabetes Association. Diabetes Care. 2017;40(1):136-154.'
    doi: 10.2337/dc16-2042
    pmid: '27999003'
    pmcid: PMC6977405
    url: https://doi.org/10.2337/dc16-2042
    source_license: © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国のポジションステートメントの推奨であり、日本の診療における検査の実施体制とは異なる場合がある。本文の推奨文で確認した範囲に基づく。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-480 (id: JlvnmMg)'
    kokushi: 医学各論 Ⅹ-6-C-②（糖尿病神経障害、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-027
  domain: DM
  subdomain: 糖尿病神経障害
  assertion:
    plain_statement_ja: 糖尿病性神経障害に伴う疼痛の薬物療法では、プレガバリンまたはデュロキセチンを初期治療として検討する。ガバペンチンも、患者の経済状況や合併症、薬物相互作用を考慮したうえで、有効な初期治療の選択肢である。一方、タペンタドールやトラマドールを含むオピオイドは、依存をはじめとする合併症のリスクが高いため、この疼痛に対する第一選択薬・第二選択薬としては推奨されない。
    condition:
      region: 米国
      study: ポジションステートメント（ADA、2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-959
    source: 'Pop-Busui R, Boulton AJM, Feldman EL, et al. Diabetic Neuropathy: A Position Statement by the American Diabetes Association. Diabetes Care. 2017;40(1):136-154.'
    doi: 10.2337/dc16-2042
    pmid: '27999003'
    pmcid: PMC6977405
    url: https://doi.org/10.2337/dc16-2042
    source_license: © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 国内承認の確認状況：デュロキセチンは「糖尿病性神経障害に伴う疼痛」の適応で、プレガバリンは「神経障害性疼痛」の適応で、いずれも国内承認されていることを国内の資料（添付文書の記載）で確認した。ガバペンチンについては、国内では神経障害性疼痛の適応を確認していない（未確認）。個別の用量や保険適用の詳細条件は添付文書の確認が必要である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-480 (id: JlvnmMg)'
    kokushi: 医学各論 Ⅹ-6-C-②（糖尿病神経障害、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-028
  domain: DM
  subdomain: 糖尿病網膜症
  assertion:
    plain_statement_ja: 糖尿病網膜症は、毛細血管瘤を特徴とする軽症の非増殖網膜症から中等症・重症を経て増殖網膜症へ進展し、黄斑浮腫はどの段階でも起こりうる。眼科スクリーニングは、1型糖尿病では発症後5年以内に、2型糖尿病では診断時に、散瞳下の精密眼底検査を行う。網膜症が認められない検査が続けば1〜2年ごとの間隔も検討できるが、網膜症があれば少なくとも年1回は繰り返し、進行性または視力を脅かす病変ではより頻回に診察する。血糖、血圧、血清脂質の管理を最適化することが、発症と進行の抑制につながる。中心窩に及ぶ糖尿病黄斑浮腫の治療は抗VEGF薬の硝子体内注射が中心であり、増殖網膜症では汎網膜光凝固が重篤な視力低下のリスクを減らすことが示されている。
    condition:
      region: 米国
      study: ポジションステートメント（ADA、2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-960
    source: 'Solomon SD, Chew E, Duh EJ, et al. Diabetic Retinopathy: A Position Statement by the American Diabetes Association. Diabetes Care. 2017;40(3):412-418.'
    doi: 10.2337/dc16-2641
    pmid: '28223445'
    pmcid: PMC5402875
    url: https://doi.org/10.2337/dc16-2641
    source_license: © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 境界：網膜症は糖尿病の合併症として扱い、抗VEGF薬の硝子体内注射や光凝固の手技の詳細は扱っていない。抗VEGF薬の国内承認・保険適用は、本調査では確認していない（未確認）。米国のポジションステートメントの推奨であり、日本の眼科診療の実施間隔と異なる場合がある。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-478 (id: JlvnmMU)'
    kokushi: 医学各論 Ⅹ-6-C-③（糖尿病網膜症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-029
  domain: DM
  subdomain: 糖尿病足病変
  assertion:
    plain_statement_ja: 糖尿病足潰瘍の予防では、保護感覚の喪失（LOPS）と末梢動脈疾患（PAD）の有無によって潰瘍リスクを層別化する。LOPSもPADもない場合はリスク0（非常に低い）で年1回、LOPSまたはPADのいずれかがある場合はリスク1（低い）で6〜12か月ごと、LOPSとPADの併存、またはLOPSかPADと足変形の組み合わせがある場合はリスク2（中等度）で3〜6か月ごと、LOPSまたはPADに加えて足潰瘍の既往、下肢切断の既往、末期腎不全のいずれかがある場合はリスク3（高い）で1〜3か月ごとにスクリーニングする。リスクのある患者には、足の自己管理の教育、素足で歩かないことの指導、潰瘍前駆病変の治療を行い、中等度から高度のリスクでは治療用履物の使用や統合的なフットケアを提供する。
    condition:
      region: 国際
      study: ガイドライン（IWGDF 予防ガイドライン、2023年改訂版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-961
    source: Bus SA, Sacco ICN, Monteiro-Soares M, et al. Guidelines on the prevention of foot ulcers in persons with diabetes (IWGDF 2023 update). Diabetes/Metabolism Research and Reviews. 2024;40(3):e3651.
    doi: 10.1002/dmrr.3651
    pmid: '37302121'
    pmcid: null
    url: https://doi.org/10.1002/dmrr.3651
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: リスク区分とスクリーニング頻度はガイドラインのリスク層別化の表から読み取った。表の注記では、スクリーニング間隔はエビデンスではなく専門家の意見に基づくとされている。足感染症の重症度分類については、分類表の本文を確認できなかったため本カードでは扱っていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-481 (id: JlvnmMk)'
    kokushi: 医学各論 Ⅹ-6-C-④（糖尿病足病変、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-030
  domain: DM
  subdomain: 大血管障害
  assertion:
    plain_statement_ja: 動脈硬化性心血管疾患（ASCVD）は糖尿病患者の罹患と死亡の最大の原因であり、血糖、血圧、脂質など複数の心血管危険因子を同時に管理することで大きな利益が得られる。糖尿病と高血圧のある患者の血圧の治療目標は130/80 mmHg未満である。2型糖尿病でASCVDまたは腎臓病が確立している患者では、心血管疾患への有効性が示されたSGLT2阻害薬またはGLP-1受容体作動薬を、包括的な心血管リスク低減の一部として用いることが推奨され、確立したASCVDのある患者では高強度スタチン療法が推奨される。
    condition:
      region: 米国
      study: 診療ガイドライン（ADA Standards of Care in Diabetes—2025、第10章）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-963
    source: 'American Diabetes Association Professional Practice Committee. 10. Cardiovascular Disease and Risk Management: Standards of Care in Diabetes—2025. Diabetes Care. 2025;48(Suppl 1):S207-S238.'
    doi: 10.2337/dc25-S010
    pmid: '39651970'
    pmcid: PMC11635050
    url: https://doi.org/10.2337/dc25-S010
    source_license: © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 心血管リスク低減の推奨のエビデンスは主として2型糖尿病の試験に基づき、1型糖尿病への推奨は外挿であると本文に注記されている。薬剤（SGLT2阻害薬、GLP-1受容体作動薬、スタチン）の国内承認・保険適用は、本調査では個別に確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-6-C-⑤（大血管障害、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-031
  domain: DM
  subdomain: 低血糖（急性期対応）
  assertion:
    plain_statement_ja: 低血糖は3段階に分けられる。レベル1は血糖70 mg/dL未満54 mg/dL以上、レベル2は54 mg/dL未満、レベル3は血糖値にかかわらず他者の介助を要する重篤なイベントである。意識のある患者では、血糖70 mg/dL以下で速効性の炭水化物（通常はブドウ糖15 g）を摂取させ、15分後に血糖を再測定し、依然として低ければ摂取を繰り返す。純粋なブドウ糖が望ましく、脂肪は急性期の反応を遅らせるため脂肪の多い食品は避け、タンパク質は治療に用いない。インスリン使用中または低血糖リスクの高いすべての患者にはグルカゴンを処方し、家族や介護者に使い方と保管方法を教育する。
    condition:
      region: 米国
      study: 診療ガイドライン（ADA Standards of Care in Diabetes—2025、第6章）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-965
    source: 'American Diabetes Association Professional Practice Committee. 6. Glycemic Goals and Hypoglycemia: Standards of Care in Diabetes—2025. Diabetes Care. 2025;48(Suppl 1):S128-S145.'
    doi: 10.2337/dc25-S006
    pmid: '39651981'
    pmcid: PMC11635034
    url: https://doi.org/10.2337/dc25-S006
    source_license: © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: グルカゴン製剤（注射製剤・点鼻製剤）の国内承認・保険適用は、本調査では個別に確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs)'
    kokushi: 医学各論 Ⅹ-6-D-②（薬剤による低血糖、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-032
  domain: DM
  subdomain: インスリノーマ
  assertion:
    plain_statement_ja: インスリノーマは内因性高インスリン血症性低血糖を起こす膵島腫瘍である。診断の前提はWhippleの三徴（低血糖に合致する症状・徴候、血漿グルコースの低下、その上昇による症状の消失）の確認であり、生化学的には最長72時間の監視下絶食で低血糖を再現し、血糖55 mg/dL未満の時点でインスリン3.0 μU/mL以上、Cペプチド0.6 ng/mL以上、プロインスリン5.0 pmol/L以上が不適切に保たれていることを示す。β-ヒドロキシ酪酸2.7 mmol/L以下であることと、グルカゴン1 mg静注後に血糖が25 mg/dL以上上昇することは、インスリン（またはIGF）過剰の生物学的証拠となる。低血糖時の検体では経口血糖降下薬のスクリーニングも行い、分泌促進薬の摂取を除外する。画像による局在診断は生化学的に確定してから行う。
    condition:
      region: 米国
      study: 診療ガイドライン（Endocrine Society、2009年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-966
    source: 'Cryer PE, Axelrod L, Grossman AB, et al. Evaluation and Management of Adult Hypoglycemic Disorders: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2009;94(3):709-728.'
    doi: 10.1210/jc.2008-1410
    pmid: '19088155'
    pmcid: null
    url: https://doi.org/10.1210/jc.2008-1410
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 診断基準の数値はガイドライン本文の基準による。2009年のガイドラインであり、その後の改訂の有無は確認していない。本カードは診断を中心とし、外科切除など治療の詳細は扱っていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs)'
    kokushi: 医学各論 Ⅹ-6-D-①（インスリノーマ、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-033
  domain: DM
  subdomain: 薬剤性低血糖
  assertion:
    plain_statement_ja: 糖尿病治療薬による低血糖の主な原因はインスリンとインスリン分泌促進薬（スルホニル尿素薬などの経口血糖降下薬）である。これらの薬剤の作用が体内に残っている間は、いったん血糖が回復した後も低血糖が再発しうるため、回復後も追加の食事摂取と経過観察が必要である。レベル2またはレベル3の低血糖が1回以上起きた場合は、治療計画を速やかに見直し、薬剤の減量や変更を含めた治療強度の引き下げを検討する。
    condition:
      region: 米国
      study: 診療ガイドライン（ADA Standards of Care in Diabetes—2025、第6章）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-965
    source: 'American Diabetes Association Professional Practice Committee. 6. Glycemic Goals and Hypoglycemia: Standards of Care in Diabetes—2025. Diabetes Care. 2025;48(Suppl 1):S128-S145.'
    doi: 10.2337/dc25-S006
    pmid: '39651981'
    pmcid: PMC11635034
    url: https://doi.org/10.2337/dc25-S006
    source_license: © by the American Diabetes Association（Readers may use this article as long as the work is properly cited, the use is educational and not for profit, and the work is not altered. CC ライセンス表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 個別のスルホニル尿素薬・グリニド薬について、国内添付文書上の低血糖に関する注意や保険適用の範囲は本調査では確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs)'
    kokushi: 医学各論 Ⅹ-6-D-②（薬剤による低血糖、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-034
  domain: DM
  subdomain: 内分泌異常による低血糖
  assertion:
    plain_statement_ja: 糖尿病のない患者の低血糖では、まず薬剤、重症疾患、ホルモン欠乏、膵外腫瘍といった手がかりを検討する。ホルモン欠乏の代表は副腎皮質機能低下症によるコルチゾール欠乏と、下垂体機能低下に伴う成長ホルモンやACTHの欠乏であり、コルチゾールと成長ホルモンは血糖低下に対する防御（反調節）に働くため、その欠乏は低血糖の原因となる。評価はWhippleの三徴が確認された患者に限って行い、臨床的な手がかりからホルモン欠乏を疑った場合は内分泌学的検査で確定する。
    condition:
      region: 米国
      study: 診療ガイドライン（Endocrine Society、2009年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-966
    source: 'Cryer PE, Axelrod L, Grossman AB, et al. Evaluation and Management of Adult Hypoglycemic Disorders: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2009;94(3):709-728.'
    doi: 10.1210/jc.2008-1410
    pmid: '19088155'
    pmcid: null
    url: https://doi.org/10.1210/jc.2008-1410
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは2009年ガイドラインの評価の枠組み（手がかりの優先順位）に基づく。各ホルモン欠乏の個別の診断基準や負荷試験の判定値は、本調査では確認していない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs)'
    kokushi: 医学各論 Ⅹ-6-D-③（内分泌異常による低血糖、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-035
  domain: DM
  subdomain: 反応性低血糖
  assertion:
    plain_statement_ja: 食後に起こる症状だけでは反応性低血糖とは診断できない。診断には、症状が起きた時点での血漿グルコースの低下と、グルコースが上昇した後の症状の消失、すなわちWhippleの三徴を実際に確認する必要がある。自然な発作時に検体が得られなかった場合は、普段の食事に近い食事を与えて症状と血糖を同時に記録する方法で発作を再現し、三徴が確認できなければ低血糖として扱わない。
    condition:
      region: 米国
      study: 診療ガイドライン（Endocrine Society、2009年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-966
    source: 'Cryer PE, Axelrod L, Grossman AB, et al. Evaluation and Management of Adult Hypoglycemic Disorders: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2009;94(3):709-728.'
    doi: 10.1210/jc.2008-1410
    pmid: '19088155'
    pmcid: null
    url: https://doi.org/10.1210/jc.2008-1410
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは2009年ガイドライン本文の評価方法（発作の再現と三徴の確認）に基づく。混合食負荷の具体的な実施手順の細部は、本文で確認できた範囲にとどめた。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs)'
    kokushi: 医学各論 Ⅹ-6-D-④（反応性低血糖、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-036
  domain: DM
  subdomain: インスリン自己免疫症候群
  assertion:
    plain_statement_ja: インスリン自己免疫症候群（平田病）は、外因性インスリンの投与歴がなく、膵島に病変がないにもかかわらず、インスリン自己抗体が高値となって高インスリン血症性低血糖を起こす疾患であり、日本では低血糖の原因として比較的頻度が高い。発症にはHLA-DRB1*0406との強い関連が報告されている。誘因としてスルフヒドリル基を持つ薬剤が多く、甲状腺疾患治療薬のメチマゾールや、サプリメントとして使われるα-リポ酸が代表的である。多くは誘因となった薬剤の中止により3〜6か月以内に自然に軽快する。管理は少量頻回で炭水化物の少ない食事が基本であり、食後の血糖とインスリンの上昇を抑える目的でアカルボースが使われることがあり、重症で難治性の場合は高用量の副腎皮質ステロイドなどによる治療が行われる。
    condition:
      region: イタリア
      study: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-968
    source: 'Censi S, Mian C, Betterle C. Insulin autoimmune syndrome: from diagnosis to clinical management. Annals of Translational Medicine. 2018;6(17):335.'
    doi: 10.21037/atm.2018.07.32
    pmid: '30306074'
    pmcid: PMC6174196
    url: https://doi.org/10.21037/atm.2018.07.32
    source_license: © 2018 Annals of Translational Medicine. All rights reserved.（CC ライセンス表示は確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 日本での頻度とHLAの記述はこの総説の記載による。アカルボースと副腎皮質ステロイドの本症候群への使用は国内では適応外使用となる可能性があり、承認・保険適用は未確認である。メチマゾール自体は甲状腺疾患の適応で国内承認されている薬剤だが、本症候群の誘因としての位置づけは総説の記載に基づく。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs)'
    kokushi: 医学各論 Ⅹ-6-D-⑤（インスリン自己免疫症候群、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-037
  domain: DM
  subdomain: 膵外腫瘍による低血糖
  assertion:
    plain_statement_ja: 膵外腫瘍による低血糖（非膵島細胞腫瘍性低血糖、NICTH）は、腫瘍が高分子量のIGF-II（big IGF-II）を分泌し、インスリン様作用を発揮することで起こる腫瘍随伴症候群であり、胸部の孤立性線維性腫瘍に伴うものはDoege-Potter症候群と呼ばれる。検査では、低血糖（55 mg/dL未満）に対してインスリン・プロインスリン・Cペプチドが低く、β-ヒドロキシ酪酸も低く、IGF-Iは抑制され（100 ng/mL未満）、IGF-II/IGF-I比は上昇する（正常のモル比3:1を超え、10:1以上になることが多い）というパターンをとる。治療は腫瘍の完全切除が根本治療であり、切除できない場合はブドウ糖投与に加えて副腎皮質ステロイド（プレドニゾン換算で1日30〜60 mg程度）が最も多く使われる薬物療法で、成長ホルモン投与やグルカゴンの持続投与が用いられることもある。ジアゾキシドとオクトレオチドは有効でない。
    condition:
      region: 米国
      study: 臨床レビュー（症例報告・小規模症例集積の総括）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-967
    source: 'Bodnar TW, Acevedo MJ, Pietropaolo M. Management of Non-Islet-Cell Tumor Hypoglycemia: A Clinical Review. The Journal of Clinical Endocrinology & Metabolism. 2014;99(3):713-722.'
    doi: 10.1210/jc.2013-3382
    pmid: '24423303'
    pmcid: PMC5393479
    url: https://doi.org/10.1210/jc.2013-3382
    source_license: © 2014 by The Endocrine Society（CC ライセンス表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: エビデンスは症例報告と小規模な症例集積が中心で、無作為化試験はない（本文の明記による）。副腎皮質ステロイド・成長ホルモン・グルカゴンの本症候群への使用は適応外であり、国内承認・保険適用は未確認である。big IGF-IIそのものの測定は研究機関でのみ可能と本文にある。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs)'
    kokushi: 医学各論 Ⅹ-6-D-⑥（膵外腫瘍、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: DM-038
  domain: DM
  subdomain: 乳糖不耐症
  assertion:
    plain_statement_ja: 乳糖不耐症は、小腸で乳糖を分解するラクターゼが不足して乳糖の消化吸収ができない状態（乳糖吸収不良）がある人に、乳糖の摂取後に腹痛、腹部膨満、下痢などの腹部症状が現れるものをいう。症状の出やすさは、摂取した乳糖の量、ラクターゼの発現量、腸内細菌叢によって変わる。成人のラクターゼ活性の持続は、LCT遺伝子の-13910位のCからTへの多型と関連する。ラクターゼ欠乏には一次性のもののほか、感染などによる小腸粘膜の障害で起こる二次性のものがある。診断には遺伝子検査、内視鏡的検査、生理学的検査が用いられ、管理は低乳糖食とラクターゼ製剤の補充が中心である。
    condition:
      region: 欧州
      study: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-969
    source: 'Misselwitz B, Butter M, Verbeke K, Fox MR. Update on lactose malabsorption and intolerance: pathogenesis, diagnosis and clinical management. Gut. 2019;68(11):2080-2091.'
    doi: 10.1136/gutjnl-2019-318404
    pmid: '31427404'
    pmcid: PMC6839734
    url: https://doi.org/10.1136/gutjnl-2019-318404
    source_license: Re-use permitted under CC BY-NC. No commercial re-use.（CC BY-NC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは抄録で確認できた範囲に基づく。呼気試験など個別の診断法の判定基準の数値は、抄録の範囲では確認できなかったため書いていない。ラクターゼ製剤の国内承認・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-6-E-①（乳糖分解酵素障害症<乳糖不耐症>、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-001
  domain: MT
  subdomain: 脂質異常症の診断基準
  assertion:
    plain_statement_ja: 日本の診断基準（動脈硬化性疾患予防ガイドライン2022年版）では、脂質異常症のスクリーニング値を、LDLコレステロール140 mg/dL以上（高LDLコレステロール血症、120〜139 mg/dLは境界域）、HDLコレステロール40 mg/dL未満（低HDLコレステロール血症）、トリグリセリド空腹時150 mg/dL以上または随時175 mg/dL以上（高トリグリセリド血症）、non-HDLコレステロール170 mg/dL以上（高non-HDLコレステロール血症、150〜169 mg/dLは境界域）と定める。
    condition:
      region: 日本
      study: ガイドライン（日本動脈硬化学会、2022年版の英語版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-971
    source: Okamura T, Tsukamoto K, Arai H, et al. Japan Atherosclerosis Society (JAS) Guidelines for Prevention of Atherosclerotic Cardiovascular Diseases 2022. Journal of Atherosclerosis and Thrombosis. 2024;31(6):641-853.
    doi: 10.5551/jat.GL2022
    pmid: '38123343'
    pmcid: PMC11150976
    url: https://doi.org/10.5551/jat.GL2022
    source_license: CC BY-NC-SA 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインの診断基準の表（Table 1）から読み取り。空腹時は10時間以上の絶食を指す（表の脚注）。薬剤の名前は出ないため、国内承認に関する注記は不要である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-A-①（原発性高脂血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-002
  domain: MT
  subdomain: 家族性高コレステロール血症
  assertion:
    plain_statement_ja: 成人の家族性高コレステロール血症（15歳以上）は、1) 未治療のLDLコレステロール180 mg/dL以上、2) 腱黄色腫（アキレス腱肥厚を含む）または皮膚結節性黄色腫、3) 家族性高コレステロール血症または早発性冠動脈疾患の家族歴、の3項目のうち2項目以上を満たせば診断する（他の原発性・二次性脂質異常症を除外したうえで）。アキレス腱肥厚はX線計測で男性8.0 mm以上、女性7.5 mm以上（超音波では男性6.0 mm以上、女性5.5 mm以上）を目安とする。日本の一般人口での頻度は約300人に1人とされ、若年から冠動脈疾患のリスクが高いため、家族のスクリーニング（カスケードスクリーニング）が推奨される。
    condition:
      region: 日本
      study: ガイドライン（日本動脈硬化学会、成人家族性高コレステロール血症、2022年版の英語版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-972
    source: Harada-Shiba M, Arai H, Ohmura H, et al. Guidelines for the Diagnosis and Treatment of Adult Familial Hypercholesterolemia 2022. Journal of Atherosclerosis and Thrombosis. 2023;30(5):558-586.
    doi: 10.5551/jat.CR005
    pmid: '36682773'
    pmcid: PMC10164595
    url: https://doi.org/10.5551/jat.CR005
    source_license: CC BY-NC-SA 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 診断基準の数値はガイドラインの診断基準の表（Table 1）から読み取り。頻度（約300人に1人）はガイドライン本文で確認した。遺伝子検査の国内の実施体制・保険適用の詳細は未確認である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-A-①（原発性高脂血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-003
  domain: MT
  subdomain: 脂質異常症の管理目標
  assertion:
    plain_statement_ja: 日本の管理目標（動脈硬化性疾患予防ガイドライン2022年版）では、一次予防は絶対リスク評価（久山町スコア）で低・中・高リスクに分類し、LDLコレステロールの管理目標を低リスク160 mg/dL未満、中リスク140 mg/dL未満、高リスク120 mg/dL未満とする。二次予防の目標は100 mg/dL未満で、急性冠症候群、家族性高コレステロール血症、糖尿病などを合併する高リスクの二次予防では70 mg/dL未満（non-HDLコレステロール100 mg/dL未満）が考慮される。すべてのリスク区分で、HDLコレステロール40 mg/dL以上とトリグリセリド150 mg/dL未満もあわせて目指す。一次予防では原則として3〜6か月の生活習慣の修正を行ってから薬物療法を検討するが、LDLコレステロール180 mg/dL以上が持続する場合は薬物療法の併用を考慮する。
    condition:
      region: 日本
      study: ガイドライン（日本動脈硬化学会、2022年版の英語版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-971
    source: Okamura T, Tsukamoto K, Arai H, et al. Japan Atherosclerosis Society (JAS) Guidelines for Prevention of Atherosclerotic Cardiovascular Diseases 2022. Journal of Atherosclerosis and Thrombosis. 2024;31(6):641-853.
    doi: 10.5551/jat.GL2022
    pmid: '38123343'
    pmcid: PMC11150976
    url: https://doi.org/10.5551/jat.GL2022
    source_license: CC BY-NC-SA 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 管理目標の数値はガイドラインのリスク区分別の目標値の表（Table 5）と本文から読み取り。久山町スコアによる絶対リスク評価の計算方法の詳細は本カードでは確認していない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-A-①（原発性高脂血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-004
  domain: MT
  subdomain: 脂質異常症の管理目標（欧州）
  assertion:
    plain_statement_ja: 欧州の2019年ESC/EASガイドラインでは、LDLコレステロールの目標を超高リスクでは治療前値からの50%以上の低下と55 mg/dL（1.4 mmol/L）未満、高リスクでは50%以上の低下と70 mg/dL（1.8 mmol/L）未満、中等度リスクでは100 mg/dL（2.6 mmol/L）未満、低リスクでは116 mg/dL（3.0 mmol/L）未満と定める。最大耐量のスタチン治療中に2年以内に2回目の血管イベントを起こした動脈硬化性心血管疾患の患者では、40 mg/dL（1.0 mmol/L）未満も考慮される。non-HDLコレステロールの副次目標は、超高リスク85 mg/dL、高リスク100 mg/dL、中等度リスク130 mg/dLである。
    condition:
      region: 欧州
      study: ガイドライン（欧州心臓病学会・欧州動脈硬化学会、2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-973
    source: 'Mach F, Baigent C, Catapano AL, et al. 2019 ESC/EAS Guidelines for the management of dyslipidaemias: lipid modification to reduce cardiovascular risk. European Heart Journal. 2020;41(1):111-188.'
    doi: 10.1093/eurheartj/ehz455
    pmid: '31504418'
    pmcid: null
    url: https://doi.org/10.1093/eurheartj/ehz455
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値はガイドラインの治療目標の表（Table 7）と推奨文から読み取り。米国の2018年AHA/ACCガイドラインは絶対的な目標値ではなく治療の閾値に基づく方式で枠組みが異なるが、1枚のカードの出典を1文献にそろえるため本カードには含めていない（米国分の数値は未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-A-①（原発性高脂血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-005
  domain: MT
  subdomain: 家族性高コレステロール血症の治療
  assertion:
    plain_statement_ja: ヘテロ接合体家族性高コレステロール血症のLDLコレステロールの管理目標は、一次予防で100 mg/dL未満、二次予防で70 mg/dL未満である。生活習慣の改善だけでは目標を達成しにくいことが多く、薬物療法が必須で、第一選択はスタチン（強力なスタチンが中心）である。効果が不十分な場合は最大耐量まで増量するかエゼチミブを併用し、それでも不十分な場合はPCSK9阻害薬の追加を検討する。薬物療法に抵抗性の重症例ではLDLアフェレーシスが選択肢となる。
    condition:
      region: 日本
      study: ガイドライン（日本動脈硬化学会、成人家族性高コレステロール血症、2022年版の英語版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-972
    source: Harada-Shiba M, Arai H, Ohmura H, et al. Guidelines for the Diagnosis and Treatment of Adult Familial Hypercholesterolemia 2022. Journal of Atherosclerosis and Thrombosis. 2023;30(5):558-586.
    doi: 10.5551/jat.CR005
    pmid: '36682773'
    pmcid: PMC10164595
    url: https://doi.org/10.5551/jat.CR005
    source_license: CC BY-NC-SA 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 管理目標の数値と薬物療法の順序はガイドライン本文で確認した。国内承認については、PCSK9阻害薬エボロクマブが家族性高コレステロール血症・高コレステロール血症（心血管イベントのリスクが高くスタチンで効果不十分な場合に限る）に承認されていることをPMDAの添付文書情報で別途確認した。スタチン・エゼチミブの個別製剤の最新の承認・保険適用範囲は添付文書で未確認である。LDLアフェレーシスの保険適用条件の詳細はガイドライン本文に記載があるが、最新の診療報酬上の条件は未確認である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-A-①（原発性高脂血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-006
  domain: MT
  subdomain: 脂質低下療法のエビデンス
  assertion:
    plain_statement_ja: FOURIER試験は、スタチン治療を受けていてもLDLコレステロール70 mg/dL以上の動脈硬化性心血管疾患の患者27,564人を対象とした無作為化二重盲検試験である。PCSK9阻害薬エボロクマブは48週時点でLDLコレステロールを中央値92 mg/dLから30 mg/dLへ59%低下させた。主要評価項目（心血管死、心筋梗塞、脳卒中、不安定狭心症による入院、冠血行再建の複合）は9.8%対11.3%（ハザード比0.85）、主要な副次評価項目（心血管死、心筋梗塞、脳卒中の複合）は5.9%対7.4%（ハザード比0.80）で、いずれもエボロクマブ群で有意に低かった。追跡期間の中央値は2.2年で、新規糖尿病や神経認知イベントを含む有害事象に有意差はなかった。
    condition:
      region: 国際
      study: 無作為化二重盲検プラセボ対照試験（FOURIER、2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-974
    source: Sabatine MS, Giugliano RP, Keech AC, et al. Evolocumab and Clinical Outcomes in Patients with Cardiovascular Disease (FOURIER). The New England Journal of Medicine. 2017;376(18):1713-1722.
    doi: 10.1056/NEJMoa1615664
    pmid: '28304224'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1615664
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値は試験の抄録で確認した。心血管死単独の有意な低下は抄録の範囲では示されていない。国内承認については、エボロクマブが家族性高コレステロール血症・高コレステロール血症（心血管イベントの発現リスクが高く、HMG-CoA還元酵素阻害剤で効果不十分な場合に限る）に承認されていることをPMDAの添付文書情報で確認した。スタチン自体の心血管イベント抑制のエビデンス（個別試験の数値）は本カードの出典には含まれない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-A-①（原発性高脂血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-007
  domain: MT
  subdomain: 二次性高脂血症
  assertion:
    plain_statement_ja: 二次性脂質異常症は脂質異常症全体の30〜40%を占める。原因には、甲状腺機能低下症、ネフローゼ症候群、慢性腎臓病、原発性胆汁性胆管炎・閉塞性黄疸、糖尿病・肥満、Cushing症候群、褐色細胞腫、薬剤、多量飲酒などがある。治療の基本は原因となる疾患・病態の治療で、原因薬剤の中止や変更によって改善することもある。甲状腺機能低下症による脂質異常を見逃したままスタチン治療を安易に始めると横紋筋融解症などの重篤な有害事象を招くことがあるため、脂質低下療法の前に二次性の原因を同定することが重要である。
    condition:
      region: 日本
      study: ガイドライン（日本動脈硬化学会、2022年版の英語版、第6章）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-971
    source: Okamura T, Tsukamoto K, Arai H, et al. Japan Atherosclerosis Society (JAS) Guidelines for Prevention of Atherosclerotic Cardiovascular Diseases 2022. Journal of Atherosclerosis and Thrombosis. 2024;31(6):641-853.
    doi: 10.5551/jat.GL2022
    pmid: '38123343'
    pmcid: PMC11150976
    url: https://doi.org/10.5551/jat.GL2022
    source_license: CC BY-NC-SA 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 割合（30〜40%）はガイドライン第6章の本文で確認し、原因の一覧は同章の構成（各節の見出し）と表に基づく。脂質異常を来す薬剤の個別のリストは、表の詳細までは確認していない。薬剤名は薬効分類の範囲にとどめ、個別製剤の国内承認に関する注記は不要と判断した。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-A-②（二次性高脂血症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-008
  domain: MT
  subdomain: 高トリグリセリド血症と急性膵炎
  assertion:
    plain_statement_ja: 高トリグリセリド血症は、急性膵炎の原因として胆石とアルコールに次いで3番目に多い。基礎にリポ蛋白代謝の異常がある人に、コントロール不良の糖尿病、飲酒、薬剤などの二次的な要因が重なって発症することが多い。症状は他の原因による急性膵炎と同様だが、経過が重症になりやすく、臓器不全が持続しやすい。初期治療は他の膵炎と同様の輸液、疼痛管理、栄養サポートが基本で、トリグリセリドを下げるためにアフェレーシスやインスリン療法が行われることがある。再発を防ぐには、トリグリセリドの長期的な管理が重要である。
    condition:
      region: 国際
      study: 総説（高トリグリセリド血症による急性膵炎、2020年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-981
    source: Yang AL, McNabb-Baltar J. Hypertriglyceridemia and acute pancreatitis. Pancreatology. 2020;20(5):795-800.
    doi: 10.1016/j.pan.2020.06.005
    pmid: '32571534'
    pmcid: null
    url: https://doi.org/10.1016/j.pan.2020.06.005
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 内容は総説の抄録で確認した。膵炎の発症リスクが高まる具体的なトリグリセリド値の閾値は抄録の範囲では確認できなかったため、主張文には数値を入れていない。アフェレーシスとインスリン療法は治療法の名前にとどめ、適応の詳細は未確認である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-A-①（原発性高脂血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-009
  domain: MT
  subdomain: 肥満症
  assertion:
    plain_statement_ja: 日本ではBMI 25 kg/m²以上を肥満とする。この値は、BMI 25で肥満に関連する合併症（耐糖能異常、脂質異常症、高血圧など）の平均数が1.0を超えることに基づく。肥満のうち、肥満に起因または関連する健康障害を合併する場合、および内臓脂肪の蓄積（臍の高さでのCTによる内臓脂肪面積100 cm²以上が目安）によって健康障害の合併が予測される場合を「肥満症」として区別し、医学的な減量の対象とする。
    condition:
      region: 日本
      study: 診断基準の原著（日本肥満学会の肥満症診断基準検討委員会、2002年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-975
    source: Examination Committee of Criteria for 'Obesity Disease' in Japan; Japan Society for the Study of Obesity. New criteria for 'obesity disease' in Japan. Circulation Journal. 2002;66(11):987-992.
    doi: 10.1253/circj.66.987
    pmid: '12419927'
    pmcid: null
    url: https://doi.org/10.1253/circj.66.987
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値（BMI 25、内臓脂肪面積100 cm²）は出典論文の抄録で確認した。肥満症の健康障害の全項目（11項目）の一覧は抄録の範囲では確認していないため、主張文では同論文で評価された合併症の例示にとどめた。現行の肥満症診療ガイドライン（2022年版）との定義の差分は未確認である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-483 (id: JlvnmM4)'
    kokushi: 医学各論 Ⅹ-7-B-①（単純性肥満、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-010
  domain: MT
  subdomain: 肥満症の治療
  assertion:
    plain_statement_ja: 肥満症の薬物療法は、食事・運動などの生活習慣への介入を基盤とし、その補助として用いられる。STEP 1試験は、糖尿病のない、BMI 30以上（肥満に関連する合併症がある場合は27以上）の成人1,961人を対象に、セマグルチド2.4 mgの週1回皮下投与と生活習慣介入を組み合わせた無作為化二重盲検試験で、68週時点の体重変化はセマグルチド群で平均-14.9%、プラセボ群で-2.4%（推定治療差-12.4ポイント）であった。5%以上の減量を達成した割合は86.4%対31.5%であった。
    condition:
      region: 国際
      study: 無作為化二重盲検プラセボ対照試験（STEP 1、2021年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-976
    source: Wilding JPH, Batterham RL, Calanna S, et al. Once-Weekly Semaglutide in Adults with Overweight or Obesity (STEP 1). The New England Journal of Medicine. 2021;384(11):989-1002.
    doi: 10.1056/NEJMoa2032183
    pmid: '33567185'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2032183
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値は試験の抄録で確認した。国内承認については、セマグルチド（ウゴービ）が肥満症に効能・効果のある薬剤として2023年11月に薬価収載されたことを日本肥満学会のステートメントで確認した。ただし保険適用は、高血圧・脂質異常症・2型糖尿病のいずれかを有し食事・運動療法で効果が不十分で、BMI 27以上かつ肥満に関連する健康障害を2つ以上有する場合、またはBMI 35以上の場合に限られ、STEP 1の登録基準とは異なる。外科療法（スリーブ状胃切除術など）の適応基準と治療成績は本カードの出典では確認していないため、主張文には含めていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-483 (id: JlvnmM4)'
    kokushi: 医学各論 Ⅹ-7-B-①（単純性肥満、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-011
  domain: MT
  subdomain: メタボリックシンドローム
  assertion:
    plain_statement_ja: 日本のメタボリックシンドロームの診断基準（2005年、メタボリックシンドローム診断基準検討委員会）では、ウエスト周囲径が臍の高さで男性85 cm以上、女性90 cm以上（内臓脂肪面積100 cm²に相当する値）であることを必須項目とし、これに加えて、1) トリグリセリド150 mg/dL以上かつ/またはHDLコレステロール40 mg/dL未満、2) 収縮期血圧130 mmHg以上かつ/または拡張期血圧85 mmHg以上、3) 空腹時血糖110 mg/dL以上、の3項目のうち2項目以上を満たす場合にメタボリックシンドロームと診断する。
    condition:
      region: 日本
      study: 診断基準（2005年。動脈硬化性疾患予防ガイドライン2022年版に転載された表で確認）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-971
    source: Okamura T, Tsukamoto K, Arai H, et al. Japan Atherosclerosis Society (JAS) Guidelines for Prevention of Atherosclerotic Cardiovascular Diseases 2022. Journal of Atherosclerosis and Thrombosis. 2024;31(6):641-853.
    doi: 10.5551/jat.GL2022
    pmid: '38123343'
    pmcid: PMC11150976
    url: https://doi.org/10.5551/jat.GL2022
    source_license: CC BY-NC-SA 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 基準値は、2005年の診断基準の表を転載した動脈硬化性疾患予防ガイドライン2022年版の表から読み取り。原典（日本内科学会雑誌 2005年；94:794-809）そのものは、掲載サイトの障害のため直接開いて確認できていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；PS-02-14-06 (id: J5Zjel4)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-B-②（メタボリックシンドローム、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-012
  domain: MT
  subdomain: 症候性肥満
  assertion:
    plain_statement_ja: 症候群性肥満は、発達の遅れなどを伴って早期に発症する肥満で、Prader-Willi症候群、Bardet-Biedl症候群、Cohen症候群、Albright遺伝性骨異栄養症などが含まれる。症候群を伴わない単一遺伝子性の肥満の原因遺伝子としては、レプチン（LEP）、レプチン受容体（LEPR）、POMC、PCSK1、メラノコルチン4受容体（MC4R）、SIM1、BDNF、NTRK2などが報告されており、このうちMC4Rの異常が小児肥満で最も多く、罹患者の約4%にみられる。Prader-Willi症候群は15番染色体q11.2-q13領域の父性発現遺伝子の欠失（約70%）などによって生じる。
    condition:
      region: 国際
      study: 総説（ヒトの肥満の遺伝学、2022年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-977
    source: 'Mahmoud R, Kimonis V, Butler MG. Genetics of Obesity in Humans: A Clinical Review. International Journal of Molecular Sciences. 2022;23(19):11005.'
    doi: 10.3390/ijms231911005
    pmid: '36232301'
    pmcid: PMC9569701
    url: https://doi.org/10.3390/ijms231911005
    source_license: CC BY 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 遺伝子と割合（MC4R約4%、Prader-Willi症候群の欠失約70%）は総説の本文で確認した。甲状腺機能低下症やCushing症候群などの内分泌性の症候性肥満は、この出典（遺伝学の総説）の扱う範囲外のため主張文に含めていない。各症候群の診断基準の詳細は未確認である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-483 (id: JlvnmM4)'
    kokushi: 医学各論 Ⅹ-7-B-③（症候性肥満、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-013
  domain: MT
  subdomain: 低蛋白血症
  assertion:
    plain_statement_ja: 低蛋白血症は、主に血清アルブミンの低下によって評価される。アルブミンは肝臓でのみ合成される血漿蛋白で、血漿蛋白の50〜60%を占め、基準濃度は35〜50 g/L、半減期は14〜21日であり、血漿の膠質浸透圧の約80%を担う。低アルブミン血症の成り立ちは、肝疾患や栄養不良、炎症（インターロイキン6、インターロイキン1、腫瘍壊死因子などの炎症性メディエーターが合成を抑制する）による合成の低下と、腎臓や消化管からの喪失の増加、体液分布の異常などに大別される。血清アルブミンは栄養状態や疾患の重症度の指標としても用いられる。
    condition:
      region: 米国
      study: 教科書章（StatPearls、低アルブミン血症）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-978
    source: 'Gounden V, Easton-Carr R, Jialal I. Hypoalbuminemia. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK526080.'
    doi: null
    pmid: '30252336'
    pmcid: null
    url: https://www.ncbi.nlm.nih.gov/books/NBK526080/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値は出典の章の要約で確認した。DOIは、PubMedレコードにDOIの記載がないため null とした。低蛋白血症を総蛋白量で定義する場合の基準値と、原因疾患ごとの診断の進め方は未確認である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-8-A-①（低蛋白血症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-014
  domain: MT
  subdomain: 全身性アミロイドーシス
  assertion:
    plain_statement_ja: 全身性アミロイドーシスは、蛋白質の線維（アミロイド）が組織に沈着する疾患群で、免疫グロブリン軽鎖に由来するAL型が最も多い。治療法の選択は型によって決まるため、沈着したアミロイドの型判定が重要で、固定組織からのレーザーキャプチャーと質量分析による判定が普及している。心アミロイドーシスの評価には、心臓MRIや、骨シンチグラフィ用トレーサーを転用した核医学検査が用いられる。AL型の生存は新しい化学療法薬の登場によって大きく改善したが、進行した臓器障害がある例では今なお難しく、早期診断が重要である。
    condition:
      region: 国際
      study: 総説（Seminar、全身性アミロイドーシス、2016年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-979
    source: Wechalekar AD, Gillmore JD, Hawkins PN. Systemic amyloidosis. The Lancet. 2016;387:2641-2654.
    doi: 10.1016/S0140-6736(15)01274-X
    pmid: '26719234'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(15)01274-X
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 内容は総説の抄録で確認した。AL型の臓器障害の頻度や病期分類の数値は本カードでは確認していない。国内の指定難病としての診断基準は厚生労働省の資料（出典マスターのSRC-247）があるが、本カードの出典には含めていない。薬剤の名前は出ないため、国内承認に関する注記は不要である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-486 (id: JlvnmNM)'
    kokushi: 医学各論 Ⅹ-8-B-①（全身性アミロイドーシス、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-015
  domain: MT
  subdomain: 全身性アミロイドーシス（ATTR型）
  assertion:
    plain_statement_ja: トランスサイレチン型（ATTR）アミロイドーシスは、野生型または変異型のトランスサイレチンが不安定化してミスフォールドし、心筋などにアミロイドとして沈着する疾患である。タファミジスはトランスサイレチンの四量体に結合してその解離を防ぎ、アミロイド形成を抑える。ATTR-ACT試験（トランスサイレチン型心アミロイドーシスの患者441人、30か月間の無作為化二重盲検試験）では、全死亡はタファミジス群29.5%に対してプラセボ群42.9%（ハザード比0.70）とタファミジス群で低く、心血管関連の入院の頻度も低かった（相対リスク比0.68）。
    condition:
      region: 国際
      study: 無作為化二重盲検プラセボ対照試験（ATTR-ACT、2018年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-980
    source: Maurer MS, Schwartz JH, Gundapaneni B, et al. Tafamidis Treatment for Patients with Transthyretin Amyloid Cardiomyopathy (ATTR-ACT). The New England Journal of Medicine. 2018;379(11):1007-1016.
    doi: 10.1056/NEJMoa1805689
    pmid: '30145929'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1805689
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値は試験の抄録で確認した。国内承認については、タファミジスがトランスサイレチン型心アミロイドーシス（野生型及び変異型）に承認されていることをPMDAの医薬品リスク管理計画書（ビンダケル・ビンマック）で確認した。トランスサイレチン型家族性アミロイドポリニューロパチーへの適応は用量・製剤が別であり、本カードの範囲外である。野生型と変異型で効果に差があるかどうかは抄録の範囲では確認していない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-486 (id: JlvnmNM)'
    kokushi: 医学各論 Ⅹ-8-B-①（全身性アミロイドーシス、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-016
  domain: MT
  subdomain: 小児肥満
  assertion:
    plain_statement_ja: 小児・思春期の肥満は、米国の小児・青年の約17%にみられる。内分泌疾患による肥満はまれで、通常は身長の伸びの鈍化（成長速度の低下）を伴うため、成長パターンの評価が原因の鑑別に役立つ。評価では、脂質異常症を含む肥満の合併症を系統的にスクリーニングして早期に発見することが推奨され、遺伝性症候群の検査は、特徴的な病歴や身体所見がある場合に限って行う。治療は生活習慣への介入が基本であり、薬物療法は臨床試験の範囲に限るべきとされ、生活習慣の介入で効果が得られない重症の、成熟した思春期児では、減量・代謝手術が選択肢となる。
    condition:
      region: 米国
      study: ガイドライン（米国内分泌学会、小児肥満、2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-982
    source: 'Styne DM, Arslanian SA, Connor EL, et al. Pediatric Obesity-Assessment, Treatment, and Prevention: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2017;102(3):709-757.'
    doi: 10.1210/jc.2016-2573
    pmid: '28359099'
    pmcid: PMC6283429
    url: https://doi.org/10.1210/jc.2016-2573
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 内容はガイドラインの抄録（結論部）で確認したもので、割合（約17%）は米国の数値である。脂質スクリーニングの具体的な対象年齢と頻度は抄録の範囲では確認していない。日本の小児肥満の判定方法（肥満度など）と国内の診療体制は本カードでは扱っていない。薬物療法の位置づけは2017年時点の推奨であり、その後の承認薬の状況は未確認である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-483 (id: JlvnmM4)'
    kokushi: 医学各論 Ⅹ-7-B-①（単純性肥満、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-017
  domain: MT
  subdomain: 脂質異常症の生活習慣介入
  assertion:
    plain_statement_ja: 脂質異常症の生活習慣への介入（動脈硬化性疾患予防ガイドライン2022年版）では、食事は脂質のエネルギー比率20〜25%、飽和脂肪酸のエネルギー比率7%未満を目安とし、高LDLコレステロール血症ではコレステロールの摂取を200 mg/日未満に制限する。炭水化物のエネルギー比率は50〜60%、食物繊維は25 g/日以上とし、n-3系多価不飽和脂肪酸を増やし、トランス脂肪酸を避ける。運動は有酸素運動を1日合計30分以上、週3回以上（可能であれば毎日）、または中強度で週150分以上行うことが推奨される。禁煙は必須であり、体重はBMI 25未満の維持（25以上の場合は減量）を目指す。
    condition:
      region: 日本
      study: ガイドライン（日本動脈硬化学会、2022年版の英語版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-971
    source: Okamura T, Tsukamoto K, Arai H, et al. Japan Atherosclerosis Society (JAS) Guidelines for Prevention of Atherosclerotic Cardiovascular Diseases 2022. Journal of Atherosclerosis and Thrombosis. 2024;31(6):641-853.
    doi: 10.5551/jat.GL2022
    pmid: '38123343'
    pmcid: PMC11150976
    url: https://doi.org/10.5551/jat.GL2022
    source_license: CC BY-NC-SA 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はガイドラインの食事療法・運動療法の推奨文と生活習慣改善項目の表から読み取り。高トリグリセリド血症に特化した飲酒・糖質の指導の数値は本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-A-①（原発性高脂血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-018
  domain: MT
  subdomain: 原発性高脂血症のその他の病型
  assertion:
    plain_statement_ja: 家族性複合型高脂血症は、表現型がIIb型を基本としてIIa型やIV型の間を変動し、家族内にも異なる表現型が混在する原発性高脂血症である。日本の診断基準では、アポ蛋白BとLDLコレステロールの比が1.0を超えること、またはsmall dense LDLが存在すること、家族性高コレステロール血症と二次性高脂血症が除外されること、近親者にIIa型・IIb型・IV型の高脂血症がみられることなどを組み合わせて診断する。家族性III型高脂血症は、アポ蛋白Eの異常（主にE2/E2型）によってレムナントリポ蛋白が血中に蓄積する疾患で、手掌の線状黄色腫や結節性黄色腫を特徴とする。E2/E2型であるだけでは発症せず、糖尿病、肥満、甲状腺機能低下症などの合併を契機に顕在化することが多い。
    condition:
      region: 日本
      study: ガイドライン（日本動脈硬化学会、2022年版の英語版、第5章）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-971
    source: Okamura T, Tsukamoto K, Arai H, et al. Japan Atherosclerosis Society (JAS) Guidelines for Prevention of Atherosclerotic Cardiovascular Diseases 2022. Journal of Atherosclerosis and Thrombosis. 2024;31(6):641-853.
    doi: 10.5551/jat.GL2022
    pmid: '38123343'
    pmcid: PMC11150976
    url: https://doi.org/10.5551/jat.GL2022
    source_license: CC BY-NC-SA 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 内容はガイドライン第5章の本文で確認した。家族性複合型高脂血症の診断基準は、確認できた項目（アポ蛋白B/LDLコレステロール比、除外項目、家族歴など）に基づいて要約しており、基準の全文ではない。薬剤の名前は出ないため、国内承認に関する注記は不要である。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw)'
    kokushi: 医学各論 Ⅹ-7-A-①（原発性高脂血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-019
  domain: MT
  subdomain: ビタミン欠乏症の総論
  assertion:
    plain_statement_ja: ビタミンは水溶性（B群・ビタミンC）と脂溶性（A・D・E・K）に大別され、欠乏症の現れ方はビタミンごとに異なる。栄養素の摂取が平均必要量を下回る状態は栄養不十分であり、1つ以上の栄養素が著しく低下して身体機能が保てなくなる状態が栄養欠乏である。ビタミンを含む微量栄養素の欠乏は、食料不足などの環境要因のほか、嚥下障害、持続する嘔吐、消化・吸収障害、慢性疾患などでも生じる。評価には、葉酸、ビタミンC、B群ビタミン、ビタミンDなどの血中濃度（バイオマーカー）が用いられる。微量栄養素の欠乏は、成長障害、知的障害、周産期合併症、罹患率・死亡率の上昇につながり、その予防と解消には補充（サプリメント）と食事によるアプローチが用いられる。
    condition:
      region: 国際
      study: 総説（2022年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-986
    source: Kiani AK, Dhuli K, Donato K, et al. Main nutritional deficiencies. J Prev Med Hyg. 2022;63(2 Suppl 3):E93-E101.
    doi: 10.15167/2421-4248/jpmh2022.63.2S3.2752
    pmid: '36479498'
    pmcid: PMC9710417
    url: https://doi.org/10.15167/2421-4248/jpmh2022.63.2S3.2752
    source_license: CC BY-NC-ND（Europe PMCのライセンス表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は微量栄養素全般（鉄・亜鉛・ヨウ素などを含む）を扱う総説であり、ビタミン欠乏症に限った日本の診療基準（食事摂取基準や診断の閾値）を示すものではない。水溶性・脂溶性の別は同総説の全文で各ビタミンについて記載されていることを確認した。個別のビタミンの欠乏症は MT-020〜022・035 を参照。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU)'
    kokushi: 医学各論 Ⅹ-9-A-①（ビタミン欠乏症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-020
  domain: MT
  subdomain: ビタミンB1欠乏症（脚気・Wernicke脳症）
  assertion:
    plain_statement_ja: チアミン（ビタミンB1）欠乏は、末梢神経障害と心血管機能障害を来す脚気と、神経精神症状を来すWernicke-Korsakoff症候群を起こす。チアミンの活性型であるチアミンピロリン酸は、炭水化物の利用に関わる複数の生化学経路に必須の補因子である。欠乏はアルコール依存によるもののほか、非アルコール性の要因でも生じ、遺伝的素因も関与する。Wernicke脳症は、精神状態の変化、眼球運動障害（眼振・眼筋麻痺）、歩行失調を三徴とするが、完全な三徴がそろうのは患者の3分の1未満であり、診断が遅れやすい。未治療のWernicke脳症は、健忘と作話を特徴とするKorsakoff症候群へ進展し、しばしば不可逆となるため、早期の認識とチアミンの補充が重要である。
    condition:
      region: 国際
      study: 総説（2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-987
    source: 'Chandrakumar A, Bhardwaj A, ''t Jong GW. Review of thiamine deficiency disorders: Wernicke encephalopathy and Korsakoff psychosis. J Basic Clin Physiol Pharmacol. 2019;30(2):153-162.'
    doi: 10.1515/jbcpp-2018-0075
    pmid: '30281514'
    pmcid: null
    url: https://doi.org/10.1515/jbcpp-2018-0075
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 脚気の臨床像（末梢神経障害・心不全）とWernicke脳症の三徴・頻度は、出典表の確認経路に記した2文献で照合した内容であり、本カードの出典そのものの抄録には含まれていない。チアミン製剤の国内承認・保険適用は、本調査では添付文書で確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU)'
    kokushi: 医学各論 Ⅹ-9-A-①（ビタミン欠乏症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-021
  domain: MT
  subdomain: ビタミンB12・葉酸欠乏
  assertion:
    plain_statement_ja: ビタミンB12（コバラミン）欠乏と葉酸欠乏は、巨赤芽球性貧血の代表的な原因である。B12欠乏では、貧血に加えて神経症状・精神症状が多彩に現れ、古典的な巨赤芽球性貧血を欠くこともある。診断では臨床像が最も重要であり、欠乏を定義する決定的な単一の検査はない。コバラミン状態の第一選択検査は血清コバラミンで、機能的欠乏の判定には血漿メチルマロン酸が第二選択として有用であり、血漿ホモシステインはそれより特異度が劣る。葉酸状態の第一選択検査は血清葉酸である。検査結果と、欠乏を強く示す臨床像が食い違う場合は、神経障害を避けるため治療を遅らせてはならない。
    condition:
      region: 英国
      study: ガイドライン（英国血液学会基準委員会、2014年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-988
    source: Devalia V, Hamilton MS, Molloy AM; British Committee for Standards in Haematology. Guidelines for the diagnosis and treatment of cobalamin and folate disorders. Br J Haematol. 2014;166(4):496-513.
    doi: 10.1111/bjh.12959
    pmid: '24942828'
    pmcid: null
    url: https://doi.org/10.1111/bjh.12959
    source_license: ライセンス表示を確認できず（© John Wiley & Sons）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 英国のガイドラインであり、第二選択検査（メチルマロン酸、ホロトランスコバラミン）の実施可能性や保険適用は日本と異なる可能性がある。巨赤芽球性貧血との関係は出典表の確認経路に記した文献で照合した。ビタミンB12製剤・葉酸製剤の国内承認・保険適用は、本調査では添付文書で確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU)'
    kokushi: 医学各論 Ⅹ-9-A-①（ビタミン欠乏症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-022
  domain: MT
  subdomain: ビタミンC欠乏（壊血病）とペラグラ
  assertion:
    plain_statement_ja: 壊血病は、ビタミンCの欠乏による臨床症候群である。ビタミンCは皮膚・軟骨・骨・歯の成長と修復に必須で、抗酸化作用も持つ。欠乏が進むと、歯肉出血、点状出血・斑状出血、毛孔性角化とらせん状の体毛、創傷治癒の遅延、関節痛などが現れる。ナイアシン（ビタミンB3）欠乏によるペラグラは、日光に当たる部位の皮膚炎、下痢、抑うつから精神病症状に至る認知・精神症状を特徴とし、壊血病と並ぶ代表的なビタミン欠乏症である。
    condition:
      region: 国際
      study: 総説（2023年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-989
    source: 'Maxfield L, Daley SF, Crane JS. Vitamin C Deficiency. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK493187.'
    doi: null
    pmid: '29630239'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/29630239/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 壊血病の個別症状は Kiani らの総説（SRC-986）の全文、ペラグラの症状は Kennedy らの総説（SRC-1000）の表で照合した内容であり、本カードの出典（ビタミンC欠乏の章）の抜粋にはペラグラの記載はない。章の本文はアクセス制限のため全文を確認できていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU)'
    kokushi: 医学各論 Ⅹ-9-A-①（ビタミン欠乏症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-023
  domain: MT
  subdomain: ビタミン過剰症
  assertion:
    plain_statement_ja: ビタミン過剰症は、体内に蓄積しやすい脂溶性ビタミン（A・D・E・K）で起こりやすく、サプリメントや薬剤としての過剰摂取が主な原因となる。ビタミンAの過剰では、妊娠中の過剰摂取による催奇形性、肝障害、頭蓋内圧亢進などが問題となり、慢性毒性は長期の大量摂取で生じる。ビタミンDの過剰では高カルシウム血症が中心となり、多尿・多飲、反復する嘔吐、腹痛、脱水などを来し、過剰摂取による中毒では血清25(OH)Dが150 ng/mLを超えることが指標とされる。水溶性ビタミンは過剰分が排泄されやすく毒性は低いが、ビタミンB6とナイアシンの大量摂取では障害が起こる（MT-036）。
    condition:
      region: 国際
      study: 総説（2022年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-990
    source: 'Reddy P, Jialal I. Biochemistry, Fat Soluble Vitamins. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK534869.'
    doi: null
    pmid: '30521290'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/30521290/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ビタミンA過剰とビタミンD過剰の具体的な内容は、出典表の確認経路に記した各ビタミンの総説（Carazo ら、Marcinowska-Suchowierska ら）で照合したものであり、本カードの出典の抜粋は脂溶性ビタミンの毒性を扱う旨にとどまる。章の本文はアクセス制限のため全文を確認できていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-02-13-007 (id: JlAKpsU)'
    kokushi: 医学各論 Ⅹ-9-A-②（ビタミン過剰症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-024
  domain: MT
  subdomain: 痛風の診断と急性発作の治療
  assertion:
    plain_statement_ja: 痛風性関節炎は、関節内に析出した尿酸一ナトリウム（MSU）結晶を白血球が貪食し、サイトカインによる炎症が起こることで生じる。海外のガイドラインでは、関節液や痛風結節からMSU結晶を同定することが痛風性関節炎の診断と定義されている。急性発作の治療では、コルヒチン、NSAIDs、副腎皮質ステロイドは同等に推奨され（CQ1）、第一選択は特定の1剤に限らない。尿酸降下薬の開始後に発作を予防するためのコルヒチンカバーは、短期間より長期間の投与が推奨される（CQ6）。
    condition:
      region: 日本
      study: ガイドライン（日本痛風・尿酸核酸学会、2019年改訂第3版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-991
    source: Hisatome I, Ichida K, Mineo I, et al. Japanese Society of Gout and Uric & Nucleic Acids 2019 Guidelines for Management of Hyperuricemia and Gout 3rd edition. Gout and Uric & Nucleic Acids. 2020;44(Suppl):1-40.
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/gnamtsunyo/44/Supplement/44_sp-1/_article/-char/ja
    source_license: 日本痛風・尿酸核酸学会のガイドライン。CC表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: MSU結晶の同定による診断の位置づけは、本ガイドライン第3版が海外ガイドラインの定義として紹介している記述に基づく（日本の臨床診断基準そのものではない）。コルヒチン・NSAIDs・副腎皮質ステロイドはいずれも国内で使用される薬剤だが、個別製剤の適応・用量は本調査では添付文書で確認していない（未確認）。本カードは第3版（2019年改訂）の記載に基づく。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE)'
    kokushi: 医学各論 Ⅹ-9-B-①（痛風、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-025
  domain: MT
  subdomain: 高尿酸血症の分類と診断
  assertion:
    plain_statement_ja: 高尿酸血症は、尿酸の溶解度に基づき、性別を問わず血清尿酸値が7.0 mg/dLを超える状態と定義される。病型は、尿酸産生過剰型、尿酸排泄低下型、混合型に大別され、近年は腎外排泄の低下を含む腎負荷型の存在も提唱されている。高尿酸血症自体は無症状だが、持続すると体内の尿酸プールが増え、MSU結晶が関節や尿路に析出して、痛風や尿路結石の原因となる。成因として、核酸代謝酵素や尿酸トランスポーターの遺伝子の異常のほか、食事・飲酒・運動などの生活習慣が強く関与する。
    condition:
      region: 日本
      study: ガイドライン（日本痛風・尿酸核酸学会、2019年改訂第3版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-991
    source: Hisatome I, Ichida K, Mineo I, et al. Japanese Society of Gout and Uric & Nucleic Acids 2019 Guidelines for Management of Hyperuricemia and Gout 3rd edition. Gout and Uric & Nucleic Acids. 2020;44(Suppl):1-40.
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/gnamtsunyo/44/Supplement/44_sp-1/_article/-char/ja
    source_license: 日本痛風・尿酸核酸学会のガイドライン。CC表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 病型分類の判定に用いる尿中尿酸排泄量や尿酸クリアランスの具体的な手順・閾値は、英語版全文では確認できなかったため本カードには含めていない。定義の7.0 mg/dL超は日本のガイドラインのもので、海外の定義（例：ACRの6.8 mg/dL超）とは異なる。本カードは第3版（2019年改訂）の記載に基づく。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE)'
    kokushi: 医学各論 Ⅹ-9-B-②（高尿酸血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-026
  domain: MT
  subdomain: 高尿酸血症の治療と管理目標（日本）
  assertion:
    plain_statement_ja: 日本の治療アルゴリズムでは、血清尿酸値が7.0 mg/dLを超え、痛風発作または痛風結節がある場合は薬物治療を行う。無症候性高尿酸血症では、合併症（腎障害、尿路結石、高血圧、虚血性心疾患、糖尿病、メタボリックシンドロームなど）がある場合は8.0 mg/dL以上、合併症がない場合は9.0 mg/dL以上で薬物治療を検討し、それ未満では生活指導を行う。管理目標は血清尿酸値6.0 mg/dL以下で、痛風結節がある場合も薬物治療により6.0 mg/dL以下を維持することが推奨される（CQ2）。生活指導として、飲酒制限を含む食事教育が推奨される（CQ7）。尿酸降下薬には、キサンチンオキシダーゼ阻害薬（アロプリノール、フェブキソスタット、トピロキソスタット）などの尿酸生成抑制薬と、尿酸排泄促進薬がある。
    condition:
      region: 日本
      study: ガイドライン（日本痛風・尿酸核酸学会、2019年改訂第3版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-991
    source: Hisatome I, Ichida K, Mineo I, et al. Japanese Society of Gout and Uric & Nucleic Acids 2019 Guidelines for Management of Hyperuricemia and Gout 3rd edition. Gout and Uric & Nucleic Acids. 2020;44(Suppl):1-40.
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jstage.jst.go.jp/article/gnamtsunyo/44/Supplement/44_sp-1/_article/-char/ja
    source_license: 日本痛風・尿酸核酸学会のガイドライン。CC表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬物治療の開始基準（8.0 mg/dL、9.0 mg/dL）と合併症の範囲は、本ガイドラインの治療アルゴリズムの図（Figure 1）から読み取った（図から読み取り）。挙げた尿酸降下薬はいずれも国内で使用されているが、無症候性高尿酸血症を含む適応・保険適用の範囲は、本調査では添付文書で確認していない（未確認）。本カードは第3版（2019年改訂）の記載に基づく。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE)'
    kokushi: 医学各論 Ⅹ-9-B-②（高尿酸血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-027
  domain: MT
  subdomain: 痛風結節と慢性痛風の管理
  assertion:
    plain_statement_ja: 痛風結節のある痛風、痛風による画像上の骨破壊がある場合、発作が頻回な場合には、すべての患者に尿酸降下療法を開始することが強く推奨される。第一選択はアロプリノールで、中等度以上の慢性腎臓病（ステージ3以上）でも同様であり、開始用量は100 mg/日以下（腎機能障害ではさらに低用量）とし、血清尿酸値を測定しながら6 mg/dL未満を目標に漸増する（treat-to-target）。フェブキソスタットを用いる場合も開始用量は40 mg/日未満とする。尿酸降下療法の開始時には、少なくとも3〜6か月の抗炎症薬による発作予防を併用することが強く推奨される。重症の痛風（痛風結節を含む）では、欧州の推奨（EULAR 2016）で血清尿酸値5 mg/dL未満の維持が掲げられている。
    condition:
      region: 米国
      study: ガイドライン（米国リウマチ学会、2020年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-992
    source: FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. Arthritis Care Res (Hoboken). 2020;72(6):744-760.
    doi: 10.1002/acr.24180
    pmid: '32391934'
    pmcid: PMC10563586
    url: https://doi.org/10.1002/acr.24180
    source_license: PMC収載は著者原稿。CC表示なし（© American College of Rheumatology）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 米国のガイドラインであり、日本の管理目標は日本のガイドライン（SRC-991）の6.0 mg/dL以下が基準となる。5 mg/dL未満の目標はEULAR 2016推奨の抄録で照合した内容である。アロプリノール・フェブキソスタットの国内承認・保険適用は、本調査では添付文書で確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE)'
    kokushi: 医学各論 Ⅹ-9-B-①（痛風、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-028
  domain: MT
  subdomain: ポルフィリン症
  assertion:
    plain_statement_ja: ポルフィリン症は、ヘム生合成の先天性異常による8つの遺伝的に異なる代謝疾患の総称で、急性肝性、肝性皮膚、赤芽球性皮膚の3群に分類される。最も多い晩発性皮膚ポルフィリン症は、鉄過剰が肝のウロポルフィリン脱炭酸酵素の活性を阻害して生じる。急性肝性ポルフィリン症の急性発作の治療にはヘマチン（ヘミン）の投与が行われ、晩発性皮膚ポルフィリン症では、瀉血で鉄過剰を除去すると皮膚病変が改善する。診断は、DNAに基づく遺伝学的検査が全ての型で可能になっている。
    condition:
      region: 国際
      study: 総説（2012年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-993
    source: 'Balwani M, Desnick RJ. The porphyrias: advances in diagnosis and treatment. Blood. 2012;120(23):4496-4504.'
    doi: 10.1182/blood-2012-05-423186
    pmid: '22791288'
    pmcid: PMC3512229
    url: https://doi.org/10.1182/blood-2012-05-423186
    source_license: PMC収載は著者原稿。CC表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 2012年の総説であり、その後の治療の進展（急性肝性ポルフィリン症への新規治療など）は含まれていない。ヘミン製剤の国内承認・保険適用は、本調査では添付文書で確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-9-C-①（ポルフィリン症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-029
  domain: MT
  subdomain: 亜鉛欠乏症候群（腸性肢端皮膚炎）
  assertion:
    plain_statement_ja: 腸性肢端皮膚炎は、亜鉛トランスポーター遺伝子SLC39A4の変異により、腸管での亜鉛吸収が障害されて生じる遺伝性の亜鉛欠乏症である。亜鉛は200を超える金属酵素の構成要素であり、多くの代謝・生化学経路に必須の微量元素である。亜鉛欠乏では皮膚病変、下痢、脱毛などが現れ、吸収不良症候群、肝・腎疾患、不適切な食事、医原性などによる後天性の亜鉛欠乏でも、腸性肢端皮膚炎と同様の臨床像を呈することがある。
    condition:
      region: 国際
      study: 総説（2023年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-994
    source: 'Jagadeesan S, Kaliyadan F. Acrodermatitis Enteropathica. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK441835.'
    doi: null
    pmid: '28722865'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/28722865/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 皮膚病変・下痢・脱毛という症状は Kiani らの総説（SRC-986）の全文に挙げられた亜鉛欠乏の症状で照合した。本カードの出典の抜粋は病因と後天性欠乏の位置づけが中心で、章の本文はアクセス制限のため全文を確認できていない。亜鉛製剤の国内承認・保険適用は、本調査では添付文書で確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-9-E-③（亜鉛欠乏症候群<腸性肢端皮膚炎>、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-030
  domain: MT
  subdomain: Marfan症候群
  assertion:
    plain_statement_ja: Marfan症候群は、結合組織の蛋白であるフィブリリンをコードする15番染色体のFBN1遺伝子の異常による、常染色体優性遺伝の結合組織疾患で、頻度は3,000〜5,000人に1人とされる。眼（水晶体脱臼、近視、網膜剥離、白内障）、心血管（大動脈基部の拡張と解離、大動脈弁逆流、僧帽弁逸脱）、骨格（長く細い指、四肢に比べて長い体幹、脊柱側弯、漏斗胸・鳩胸）が主に侵される。生命予後を決めるのは大動脈合併症であり、治療はβ遮断薬などの後負荷を減らす薬剤で大動脈拡張の進行を遅らせ、適切な時期に待機的手術を行うことが中心となる。診断は臨床像に基づいて行われ、特異的な検査は分子遺伝学的検査のみである。
    condition:
      region: 国際
      study: 総説（2023年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-995
    source: 'Salik I, Rawla P. Marfan Syndrome. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK537339.'
    doi: null
    pmid: '30726024'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/30726024/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 頻度（3,000〜5,000人に1人）は出典の抜粋に報告値として記載されたものである。β遮断薬など後負荷軽減薬のMarfan症候群に対する国内の適応・保険適用は、薬剤ごとに異なると考えられるが、本調査では添付文書で確認していない（未確認）。章の本文はアクセス制限のため全文を確認できていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-9-F-①（Marfan症候群、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-031
  domain: MT
  subdomain: Ehlers-Danlos症候群
  assertion:
    plain_statement_ja: Ehlers-Danlos症候群は、関節の過可動性、皮膚の過伸展性、組織の脆弱性を特徴とする、遺伝性結合組織疾患の総称である。2017年の国際分類では、それまで標準だったVillefranche分類の6亜型に代わり、新たに見つかった原因遺伝子の広がりを反映して13亜型が定められた。亜型の間では臨床像の重なりが大きく、過可動型を除く全ての亜型で、原因となる遺伝子変異を同定する分子レベルの確定診断が求められる。過可動型については、他の関節過可動性疾患と区別できるよう臨床基準が改訂された。
    condition:
      region: 国際
      study: 国際分類（2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-996
    source: Malfait F, Francomano C, Byers P, et al. The 2017 international classification of the Ehlers-Danlos syndromes. Am J Med Genet C Semin Med Genet. 2017;175(1):8-26.
    doi: 10.1002/ajmg.c.31552
    pmid: '28306229'
    pmcid: null
    url: https://doi.org/10.1002/ajmg.c.31552
    source_license: ライセンス表示を確認できず（© Wiley Periodicals）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 各亜型の個別の臨床基準と原因遺伝子の一覧は、本カードでは抄録で確認できた範囲（13亜型、分子診断の位置づけ）にとどめ、含めていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-9-F-②（Ehlers-Danlos症候群、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-032
  domain: MT
  subdomain: 弾性線維性偽性黄色腫
  assertion:
    plain_statement_ja: 弾性線維性偽性黄色腫（PXE）は、ABCC6遺伝子の変異による常染色体劣性遺伝の代謝性疾患で、機能するABCC6蛋白の不足により、皮膚・眼・血管の弾性組織に異所性の石灰化が生じる。有病率は25,000〜100,000人に1人と推定され、女性にやや多い。初発症状はほぼ常に、頸部や屈曲部にできる小さい黄色丘疹で、進行すると丘疹が癒合し、皮膚はたるんでしわ状になる。眼では、Bruch膜の石灰化による網膜色素線条をきっかけに脈絡膜新生血管が生じ、進行すると中心視力の喪失に至る。動脈の病変では間欠性跛行などの末梢動脈疾患を来す。血中の抗石灰化因子である無機ピロリン酸（PPi）の低下が機序と考えられており、根治療法はない。
    condition:
      region: 国際
      study: 総説（2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-997
    source: Germain DP. Pseudoxanthoma elasticum. Orphanet J Rare Dis. 2017;12(1):85.
    doi: 10.1186/s13023-017-0639-8
    pmid: '28486967'
    pmcid: PMC5424392
    url: https://doi.org/10.1186/s13023-017-0639-8
    source_license: CC BY 4.0（Europe PMCの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 有病率は出典の抄録に推定値として記載された範囲である。ABCC6蛋白が輸送・調節する基質は未解明である旨も同抄録に記載されている。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)'
    kokushi: 医学各論 Ⅹ-9-G-①（弾性線維性偽性黄色腫、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-033
  domain: MT
  subdomain: 尿酸の産生と排泄（プリン代謝）
  assertion:
    plain_statement_ja: ヒトでは尿酸はプリン代謝の最終産物である。キサンチンオキシダーゼ（キサンチンオキシドレダクターゼ）が、ヒポキサンチンをキサンチンへ、キサンチンを尿酸へ変換する2段階を担い、ヒトは機能するウリカーゼを欠くため、尿酸はそれ以上分解されない。尿酸の排泄は、約3分の2が尿中から、残りが主に消化管からである。腎では、糸球体で濾過された尿酸の91〜95%が近位尿細管で再吸収され、この再吸収ではURAT1（SLC22A12）が中心的な役割を果たす。一方、尿細管への分泌にはABCG2などのトランスポーターが関わる。産生と排泄のバランスが崩れることが高尿酸血症の成因となる。
    condition:
      region: 国際
      study: 総説（2018年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-998
    source: Benn CL, et al. Physiology of hyperuricemia and urate-lowering treatments. Front Med (Lausanne). 2018;5:160.
    doi: 10.3389/fmed.2018.00160
    pmid: '29904633'
    pmcid: PMC5990632
    url: https://doi.org/10.3389/fmed.2018.00160
    source_license: CC BY 4.0（Europe PMCの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 濾過された尿酸の再吸収率（91〜95%）と排泄経路の割合は、同総説の本文に引用研究に基づく値として記載されたものである（同総説では通常の尿中尿酸排泄量は成人で620±75 mg/日とされる）。数値は一次研究そのものでは確認していない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE)'
    kokushi: 医学各論 Ⅹ-9-B-②（高尿酸血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-034
  domain: MT
  subdomain: Lesch-Nyhan症候群と家族性若年性高尿酸血症性腎症
  assertion:
    plain_statement_ja: Lesch-Nyhan症候群は、プリンのサルベージ酵素であるヒポキサンチン-グアニン・ホスホリボシルトランスフェラーゼ（HPRT）の欠損によるX連鎖性の疾患で、尿酸の産生過剰により高尿酸血症・高尿酸尿症、尿路結石、痛風を来し、ジストニアや舞踏アテトーゼ、自傷行為、認知・注意の障害などの神経症状を伴う。家族性若年性高尿酸血症性腎症は、常染色体優性の、尿細管での尿酸再吸収の亢進（排泄の低下）による疾患で、腎機能障害に先行するか、それに不釣り合いな高尿酸血症と、家族性の腎不全を呈する。いずれも小児期から尿酸管理の対象となり、尿酸の産生過剰はアロプリノールで管理できる。
    condition:
      region: 英国
      study: 総説（1993年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-999
    source: Cameron JS, Moro F, Simmonds HA. Gout, uric acid and purine metabolism in paediatric nephrology. Pediatr Nephrol. 1993;7(1):105-118.
    doi: 10.1007/BF00861588
    pmid: '8439471'
    pmcid: null
    url: https://doi.org/10.1007/BF00861588
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典は1993年の総説であり、家族性若年性高尿酸血症性腎症の原因遺伝子（ウロモジュリンUMODなど）の同定と、現在の常染色体優性尿細管間質性腎疾患（ADTKD）としての分類は、その後の進展であるため本カードには含めていない。Lesch-Nyhan症候群の神経症状と遺伝形式は、出典表の確認経路に記した Torres & Puig（2007年）の抄録で照合した。アロプリノールの国内承認・保険適用は、本調査では添付文書で確認していない（未確認）。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE)'
    kokushi: 医学各論 Ⅹ-9-B-②（高尿酸血症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-035
  domain: MT
  subdomain: ビタミンA・K・Eの欠乏
  assertion:
    plain_statement_ja: 脂溶性ビタミンA・E・Kは、食事脂肪とともに吸収されるため、脂肪吸収障害があると欠乏を来しやすい。ビタミンAは視覚に必須で、欠乏では夜盲が初期症状となり、眼球乾燥症（ビトー斑）や、進行すると角膜軟化症による失明を来す。ビタミンKは、凝固に関わるビタミンK依存性蛋白の合成に必要で、欠乏ではフィブリノゲンや血小板数が正常でもプロトロンビン時間（PT-INR）が延長して出血傾向を来し、新生児ではビタミンK欠乏性出血症が問題となる。ビタミンE欠乏は食事性のものはまれで、脂肪吸収・代謝の異常や遺伝性疾患に伴って生じ、位置覚・振動覚の低下や筋力低下などの神経症状を来す。また、未熟児ではビタミンEの貯蔵が少ない。
    condition:
      region: 国際
      study: 総説（2022年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-990
    source: 'Reddy P, Jialal I. Biochemistry, Fat Soluble Vitamins. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK534869.'
    doi: null
    pmid: '30521290'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/30521290/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 各ビタミンの欠乏症状の具体は、出典表の確認経路に記した文献（ビタミンAは Carazo らと Kiani ら、ビタミンKは Kiani らと Daley らの章、ビタミンEは Kemnic らの章と Kiani ら）で照合した内容であり、本カードの出典の抜粋は脂溶性ビタミンの役割と欠乏症候群を扱う旨にとどまる。章の本文はアクセス制限のため全文を確認できていない。ビタミンDの欠乏（骨代謝の側面）は第20回の範囲として本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU)'
    kokushi: 医学各論 Ⅹ-9-A-①（ビタミン欠乏症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: MT-036
  domain: MT
  subdomain: ナイアシン・ビタミンB6の異常（過剰と欠乏）
  assertion:
    plain_statement_ja: ナイアシン（ビタミンB3）の欠乏はペラグラ（皮膚炎、下痢、精神症状）を来す。過剰では、100 mgを超える摂取で皮膚の紅潮（フラッシング）が起こり、米国・カナダの耐容上限量はこの作用に基づいて35 mg/日とされる。1 g以上の長期摂取では、悪心・嘔吐・下痢や、まれに肝障害が報告されている。ビタミンB6の欠乏では、貧血のほか、易刺激性、抑うつ、認知機能の低下、痙攣などが現れ、アルコール依存や加齢に伴う吸収低下が危険因子となる。過剰では、1,000 mgを超える長期摂取で可逆性の感覚性ニューロパチーが報告されており、米国の耐容上限量は100 mg/日とされる。
    condition:
      region: 国際
      study: 総説（2016年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1000
    source: 'Kennedy DO. B Vitamins and the Brain: Mechanisms, Dose and Efficacy—A Review. Nutrients. 2016;8(2):68.'
    doi: 10.3390/nu8020068
    pmid: '26828517'
    pmcid: PMC4772032
    url: https://doi.org/10.3390/nu8020068
    source_license: CC BY 4.0（Crossrefのライセンス表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 耐容上限量と過剰摂取の用量は、同総説の本文に記載された米国・カナダおよび米国の値であり、日本の食事摂取基準の耐容上限量とは限らない。ビタミンB6の過剰については、750 mg/日までの長期投与試験でニューロパチーを認めなかった報告も同総説に併記されており、上限量の設定には不確実性がある。
  curriculum:
    core_curriculum: 'PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU)'
    kokushi: 医学各論 Ⅹ-9-A-②（ビタミン過剰症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応の一覧

| カード | 出題基準 | コアカリ |
|---|---|---|
| DM-001 | 医学各論 Ⅹ-6-A-①（1型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-472 (id: JlvnmL0) |
| DM-002 | 医学各論 Ⅹ-6-A-①（1型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-472 (id: JlvnmL0) |
| DM-003 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-004 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-005 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-006 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-007 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-008 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-009 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8)；TBL-02-13-007 (id: JlAKpsU) |
| DM-010 | 医学各論 Ⅹ-6-A-①（1型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-472 (id: JlvnmL0) |
| DM-011 | 医学各論 Ⅹ-6-A-③（二次性糖尿病、遺伝子異常による糖尿病、b） | PS-02-14-05 (id: JkxnuTA) |
| DM-012 | 医学各論 Ⅹ-6-A-③（二次性糖尿病、遺伝子異常による糖尿病、b） | PS-02-14-05 (id: JkxnuTA) |
| DM-013 | 医学各論 Ⅹ-6-A-④（妊娠糖尿病、b） | PS-02-14-05 (id: JkxnuTA) |
| DM-014 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-015 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-016 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-017 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-018 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-019 | 医学各論 Ⅹ-6-A-②（2型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-473 (id: JlvnmL8) |
| DM-020 | 医学各論 Ⅹ-6-A-①（1型糖尿病、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-472 (id: JlvnmL0) |
| DM-021 | 医学各論 Ⅹ-6-B-①（糖尿病ケトアシドーシス、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-475 (id: JlvnmMA) |
| DM-022 | 医学各論 Ⅹ-6-B-①（糖尿病ケトアシドーシス、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-475 (id: JlvnmMA) |
| DM-023 | 医学各論 Ⅹ-6-B-②（高血糖高浸透圧症候群、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-476 (id: JlvnmMI) |
| DM-024 | 医学各論 Ⅹ-6-B-③（乳酸アシドーシス、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-477 (id: JlvnmMM) |
| DM-025 | 医学各論 Ⅹ-6-C-①（糖尿病腎症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-479 (id: JlvnmMY) |
| DM-026 | 医学各論 Ⅹ-6-C-②（糖尿病神経障害、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-480 (id: JlvnmMg) |
| DM-027 | 医学各論 Ⅹ-6-C-②（糖尿病神経障害、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-480 (id: JlvnmMg) |
| DM-028 | 医学各論 Ⅹ-6-C-③（糖尿病網膜症、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-478 (id: JlvnmMU) |
| DM-029 | 医学各論 Ⅹ-6-C-④（糖尿病足病変、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-481 (id: JlvnmMk) |
| DM-030 | 医学各論 Ⅹ-6-C-⑤（大血管障害、b） | PS-02-14-05 (id: JkxnuTA) |
| DM-031 | 医学各論 Ⅹ-6-D-②（薬剤による低血糖、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs) |
| DM-032 | 医学各論 Ⅹ-6-D-①（インスリノーマ、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs) |
| DM-033 | 医学各論 Ⅹ-6-D-②（薬剤による低血糖、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs) |
| DM-034 | 医学各論 Ⅹ-6-D-③（内分泌異常による低血糖、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs) |
| DM-035 | 医学各論 Ⅹ-6-D-④（反応性低血糖、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs) |
| DM-036 | 医学各論 Ⅹ-6-D-⑤（インスリン自己免疫症候群、c） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs) |
| DM-037 | 医学各論 Ⅹ-6-D-⑥（膵外腫瘍、c） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-474 (id: JlvnmMs) |
| DM-038 | 医学各論 Ⅹ-6-E-①（乳糖分解酵素障害症<乳糖不耐症>、c） | PS-02-14-05 (id: JkxnuTA) |
| MT-001 | 医学各論 Ⅹ-7-A-①（原発性高脂血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw) |
| MT-002 | 医学各論 Ⅹ-7-A-①（原発性高脂血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw) |
| MT-003 | 医学各論 Ⅹ-7-A-①（原発性高脂血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw) |
| MT-004 | 医学各論 Ⅹ-7-A-①（原発性高脂血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw) |
| MT-005 | 医学各論 Ⅹ-7-A-①（原発性高脂血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw) |
| MT-006 | 医学各論 Ⅹ-7-A-①（原発性高脂血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw) |
| MT-007 | 医学各論 Ⅹ-7-A-②（二次性高脂血症、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw) |
| MT-008 | 医学各論 Ⅹ-7-A-①（原発性高脂血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw) |
| MT-009 | 医学各論 Ⅹ-7-B-①（単純性肥満、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-483 (id: JlvnmM4) |
| MT-010 | 医学各論 Ⅹ-7-B-①（単純性肥満、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-483 (id: JlvnmM4) |
| MT-011 | 医学各論 Ⅹ-7-B-②（メタボリックシンドローム、a） | PS-02-14-05 (id: JkxnuTA)；PS-02-14-06 (id: J5Zjel4)；TBL-01-00-482 (id: JlvnmMw) |
| MT-012 | 医学各論 Ⅹ-7-B-③（症候性肥満、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-483 (id: JlvnmM4) |
| MT-013 | 医学各論 Ⅹ-8-A-①（低蛋白血症、b） | PS-02-14-05 (id: JkxnuTA) |
| MT-014 | 医学各論 Ⅹ-8-B-①（全身性アミロイドーシス、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-486 (id: JlvnmNM) |
| MT-015 | 医学各論 Ⅹ-8-B-①（全身性アミロイドーシス、b） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-486 (id: JlvnmNM) |
| MT-016 | 医学各論 Ⅹ-7-B-①（単純性肥満、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-483 (id: JlvnmM4) |
| MT-017 | 医学各論 Ⅹ-7-A-①（原発性高脂血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw) |
| MT-018 | 医学各論 Ⅹ-7-A-①（原発性高脂血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-482 (id: JlvnmMw) |
| MT-019 | 医学各論 Ⅹ-9-A-①（ビタミン欠乏症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU) |
| MT-020 | 医学各論 Ⅹ-9-A-①（ビタミン欠乏症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU) |
| MT-021 | 医学各論 Ⅹ-9-A-①（ビタミン欠乏症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU) |
| MT-022 | 医学各論 Ⅹ-9-A-①（ビタミン欠乏症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU) |
| MT-023 | 医学各論 Ⅹ-9-A-②（ビタミン過剰症、c） | PS-02-14-05 (id: JkxnuTA)；TBL-02-13-007 (id: JlAKpsU) |
| MT-024 | 医学各論 Ⅹ-9-B-①（痛風、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE) |
| MT-025 | 医学各論 Ⅹ-9-B-②（高尿酸血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE) |
| MT-026 | 医学各論 Ⅹ-9-B-②（高尿酸血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE) |
| MT-027 | 医学各論 Ⅹ-9-B-①（痛風、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE) |
| MT-028 | 医学各論 Ⅹ-9-C-①（ポルフィリン症、c） | PS-02-14-05 (id: JkxnuTA) |
| MT-029 | 医学各論 Ⅹ-9-E-③（亜鉛欠乏症候群<腸性肢端皮膚炎>、c） | PS-02-14-05 (id: JkxnuTA) |
| MT-030 | 医学各論 Ⅹ-9-F-①（Marfan症候群、b） | PS-02-14-05 (id: JkxnuTA) |
| MT-031 | 医学各論 Ⅹ-9-F-②（Ehlers-Danlos症候群、c） | PS-02-14-05 (id: JkxnuTA) |
| MT-032 | 医学各論 Ⅹ-9-G-①（弾性線維性偽性黄色腫、c） | PS-02-14-05 (id: JkxnuTA) |
| MT-033 | 医学各論 Ⅹ-9-B-②（高尿酸血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE) |
| MT-034 | 医学各論 Ⅹ-9-B-②（高尿酸血症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-485 (id: JlvnmNE) |
| MT-035 | 医学各論 Ⅹ-9-A-①（ビタミン欠乏症、a） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU) |
| MT-036 | 医学各論 Ⅹ-9-A-②（ビタミン過剰症、c） | PS-02-14-05 (id: JkxnuTA)；TBL-01-00-484 (id: JlvnmNA)；TBL-02-13-007 (id: JlAKpsU) |

## 4. 未解決事項

- 薬剤を含むカードの国内承認・保険適用は、確認できたもの（MT-005・006・010・015、DM-027）は uncertainty に確認済みと記載し、それ以外は「未確認」と明記した（担当：取り込み側）。
- DM-024（乳酸アシドーシス）は診断閾値（乳酸値・pH）を一次資料で確認できず、数値を入れていない。
- DM-029（糖尿病足病変）は IWGDF/IDSA の足感染症の重症度分類の表を確認できず含めていない。検証済みの同ガイドライン（未使用枠 SRC-962）で補完できる。
- MT-004（脂質管理目標・海外）は欧州 ESC/EAS 2019 のみを出典とした。米国 AHA/ACC の閾値方式は別カード化が要判断。
- MT-011 のメタボリックシンドローム基準値は、日本動脈硬化学会ガイドラインに転載された表からの読み取り（原典の直接確認は未了）。
- MT-010 は薬物療法中心で、肥満外科療法の適応・成績は一次資料を確認できず入れていない。
- SRC-991（日本痛風・尿酸核酸学会ガイドライン第3版）は DOI・PMID ともに確認できなかった（J-STAGE・Crossref・PubMed で確認）。病型分類の判定手順の数値は英語版全文で確認できず MT-025 に含めていない。
- DM-032・034・035 の出典ガイドラインは2009年版で、改訂の有無は未確認。MT-034 の出典は1993年の総説で、ADTKD の現行分類を含まない。

## 5. 次回への引き継ぎ

- 第22回は BR・IE・EX、SRC-1011〜1070。BR は PS-02-13-05（id: JkxnuSs）が基本コアカリ。EX は kokushi null を基本にコアカリ 2-13・2-12 を使う。
- 本回の欠番：なし（DM・MT とも連番）。カードのない出題基準の小項目：なし（担当範囲の35項目すべてにカードあり。境界で除いた3項目を除く）。
