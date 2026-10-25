# 第8回 循環器：不整脈・心不全・虚血性心疾患（AR-001〜AR-035、HF-001〜HF-025、IH-001〜IH-030）

- 作成日：2026-10-25
- 事実票：90件（AR 35件、HF 25件、IH 30件）。IDは各接頭辞の001からの連番で、欠番はありません。全件 `status: draft`、`verifier: null`。
- 出典マスター：SRC-170〜SRC-216（47件）。SRC-217〜229 は未使用です。
- 取り込み：`python scripts/ingest_round.py raw/08_cv_a.md AR,HF,IH` を想定しています。YAMLブロックは1つで、アンカー・マージキー・脚注番号・`basis_tag`・仮IDは使っていません。`schema/fact.schema.json` での検証と、`ingest_round.py` の形式検査を、リポジトリの写しで通過済みです（書き込みはしていません）。
- 出典の確認方法：識別子とライセンスは Crossref API（license 欄）と PubMed E-utilities で照合しました。数値は PubMed の抄録、PMC の本文（XML）、J-STAGE の本文で確認したものだけを書いています。ガイドラインの推奨の強さとエビデンスレベルは、その版の表の表記どおりです（JCS/JHFS 2025 は C-EO・B-R などの表記）。
- 主張文はすべて自作文です（legal_basis はすべて B）。

## 0. 結論と注意点

- **OPEN の出典を2件確保しました。** JCS/JHRS の不整脈ガイドライン（2020年薬物治療、2024年フォーカスアップデート）は、Circ J 版とは別に J Arrhythm に同時掲載されており、J Arrhythm 版は Crossref で CC BY 4.0 です。AR の15件はこの J Arrhythm 版を出典にしています（識別子も J Arrhythm 版にそろえ、Circ J 版は source 欄に併記のみ）。
- **JCS の循環器ガイドライン（Circ J）は Crossref に license 欄がありません。** J-STAGE の掲載ページの表示は、2022年以降の版（安定冠動脈疾患2022、冠攣縮2023、心不全2025）が CC BY-NC-ND 4.0、2018〜2020年の版（急性冠症候群、抗血栓療法、川崎病）が「© 日本循環器学会」のみでした。いずれも RESTRICTED としています。
- 日本と欧米で異なる点（抗凝固のスコア、DOAC とプラスグレルの用量、ICD の適応条件）は、日本のカードは `condition.region: 日本` と `condition.guideline`、海外の試験は `condition.region` と `condition.study` で分け、1枚に混ぜていません。
- `differential` は、同じ出典で確認できた内容だけを残し、他の出典や一般知識による補足は削除して null にしました。
- 国内の承認・保険適用は、ガイドラインの表に記載があるもの（上室頻拍への ATP の適応外使用など）だけを書き、確認できないもの（エドキサバン15 mg の承認条件、フィネレノンの心不全への適応、Impella の保険適用の条件）は `uncertainty` に書きました。

## 1. 抽出元ホワイトリスト（出典マスター、新規 SRC-170〜216）

確認経路の略号：CR＝Crossref API の license 欄、PM＝PubMed（PMID・抄録）、PMC＝PMC の本文、PMCX＝PMC の XML（本文・license 要素）、JS＝J-STAGE の掲載ページ（本文・ライセンス表示）、FDMA＝消防庁のウェブページ。

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 使用カード数 |
|---|---|---|---|---|---|---|---|
| SRC-170 | Ono K, Iwasaki YK, Akao M, et al. JCS/JHRS 2020 Guideline on Pharmacotherapy of Cardiac Arrhythmias. J Arrhythm 2022;38:833-973（Circ J 2022;86:1790-1924 と同時掲載） | 10.1002/joa3.12714 | 36524037 | CC BY 4.0（Crossref の license 欄） | OPEN | CR（license）・PM・PMCX 本文 | 11 |
| SRC-171 | Inoue H, Fujiki A, Origasa H, et al. Prevalence of atrial fibrillation in the general population of Japan: an analysis based on periodic health examination. Int J Cardiol 2009;137:102-107 | 10.1016/j.ijcard.2008.06.029 | 18691774 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-172 | Gage BF, Waterman AD, Shannon W, et al. Validation of clinical classification schemes for predicting stroke: results from the National Registry of Atrial Fibrillation. JAMA 2001;285:2864-2870 | 10.1001/jama.285.22.2864 | 11401607 | 出版社（AMA）の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-173 | Iwasaki YK, Noda T, Akao M, et al. JCS/JHRS 2024 Guideline Focused Update on Management of Cardiac Arrhythmias. J Arrhythm 2025;41:e70033（Circ J 2025;89:1012-1073 と同一内容の同時掲載） | 10.1002/joa3.70033 | 40524851 | CC BY 4.0（Crossref の license 欄） | OPEN | CR（license）・PM・PMC 本文 | 4 |
| SRC-174 | Lip GYH, Nieuwlaat R, Pisters R, et al. Refining clinical risk stratification for predicting stroke and thromboembolism in atrial fibrillation using a novel risk factor-based approach: the Euro Heart Survey on Atrial Fibrillation. Chest 2010;137:263-272 | 10.1378/chest.09-1584 | 19762550 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-175 | Pisters R, Lane DA, Nieuwlaat R, et al. A novel user-friendly score (HAS-BLED) to assess 1-year risk of major bleeding in patients with atrial fibrillation: the Euro Heart Survey. Chest 2010;138:1093-1100 | 10.1378/chest.10-0134 | 20299623 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-176 | Ruff CT, Giugliano RP, Braunwald E, et al. Comparison of the efficacy and safety of new oral anticoagulants with warfarin in patients with atrial fibrillation: a meta-analysis of randomised trials. Lancet 2014;383:955-962 | 10.1016/S0140-6736(13)62343-0 | 24315724 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-177 | Okumura K, Akao M, Yoshida T, et al. Low-Dose Edoxaban in Very Elderly Patients with Atrial Fibrillation (ELDERCARE-AF). N Engl J Med 2020;383:1735-1745 | 10.1056/NEJMoa2012883 | 32865374 | NEJM の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-178 | Wyse DG, Waldo AL, DiMarco JP, et al (AFFIRM Investigators). A comparison of rate control and rhythm control in patients with atrial fibrillation. N Engl J Med 2002;347:1825-1833 | 10.1056/NEJMoa021328 | 12466506 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-179 | Kirchhof P, Camm AJ, Goette A, et al. Early Rhythm-Control Therapy in Patients with Atrial Fibrillation (EAST-AFNET 4). N Engl J Med 2020;383:1305-1316 | 10.1056/NEJMoa2019422 | 32865375 | NEJM の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-180 | Marrouche NF, Brachmann J, Andresen D, et al. Catheter Ablation for Atrial Fibrillation with Heart Failure (CASTLE-AF). N Engl J Med 2018;378:417-427 | 10.1056/NEJMoa1707855 | 29385358 | NEJM の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-181 | Nogami A, Kurita T, Abe H, et al. JCS/JHRS 2019 guideline on non-pharmacotherapy of cardiac arrhythmias. J Arrhythm 2021;37:709-870（Circ J 2021;85:1104-1244 と同時掲載） | 10.1002/joa3.12491 | 34386109 | CC BY-NC-ND 4.0（Crossref の license 欄） | RESTRICTED | CR（license）・PM・PMCX 本文 | 8 |
| SRC-182 | Echt DS, Liebson PR, Mitchell LB, et al. Mortality and morbidity in patients receiving encainide, flecainide, or placebo. The Cardiac Arrhythmia Suppression Trial. N Engl J Med 1991;324:781-788 | 10.1056/NEJM199103213241201 | 1900101 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-183 | Antiarrhythmics versus Implantable Defibrillators (AVID) Investigators. A comparison of antiarrhythmic-drug therapy with implantable defibrillators in patients resuscitated from near-fatal ventricular arrhythmias. N Engl J Med 1997;337:1576-1584 | 10.1056/NEJM199711273372202 | 9411221 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-184 | Moss AJ, Zareba W, Hall WJ, et al. Prophylactic implantation of a defibrillator in patients with myocardial infarction and reduced ejection fraction (MADIT-II). N Engl J Med 2002;346:877-883 | 10.1056/NEJMoa013474 | 11907286 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-185 | Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J 2025;89:1278-1444（J Card Fail 2025;31:1164-1322 と同時掲載） | 10.1253/circj.CJ-25-0002 | 40159241 | CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし） | RESTRICTED | CR・PM・JS（本文） | 9 |
| SRC-186 | Okura Y, Ramadan MM, Ohno Y, et al. Impending epidemic: future projection of heart failure in Japan to the year 2055. Circ J 2008;72:489-491 | 10.1253/circj.72.489 | 18296852 | 未確認（Crossref に license 欄なし。掲載ページは未確認） | UNKNOWN | CR・PM（抄録） | 1 |
| SRC-187 | Marume K, Ogata S, Kaichi R, et al. Incidence Rate of Hospitalization for Heart Failure in a Japanese City - An Updated Reference for Japan's Aging Society. Circ Rep 2022;4:116-122 | 10.1253/circrep.CR-21-0142 | 35342838 | CC BY-NC-ND 4.0（PMC の XML の license 要素。Crossref に license 欄なし） | RESTRICTED | CR・PM（抄録）・PMCX（license） | 1 |
| SRC-188 | Maisel AS, Krishnaswamy P, Nowak RM, et al. Rapid measurement of B-type natriuretic peptide in the emergency diagnosis of heart failure. N Engl J Med 2002;347:161-167 | 10.1056/NEJMoa020233 | 12124404 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-189 | Januzzi JL Jr, van Kimmenade R, Lainchbury J, et al. NT-proBNP testing for diagnosis and short-term prognosis in acute destabilized heart failure: an international pooled analysis of 1256 patients: the International Collaborative of NT-proBNP Study. Eur Heart J 2006;27:330-337 | 10.1093/eurheartj/ehi631 | 16293638 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-190 | Nohria A, Tsang SW, Fang JC, et al. Clinical assessment identifies hemodynamic profiles that predict outcomes in patients admitted with heart failure. J Am Coll Cardiol 2003;41:1797-1804 | 10.1016/S0735-1097(03)00309-7 | 12767667 | Elsevier の open-access user license（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-191 | Mebazaa A, Gheorghiade M, Piña IL, et al. Practical recommendations for prehospital and early in-hospital management of patients presenting with acute heart failure syndromes. Crit Care Med 2008;36(1 Suppl):S129-S139 | 10.1097/01.CCM.0000296274.51933.4C | 18158472 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-192 | McMurray JJV, Packer M, Desai AS, et al. Angiotensin-neprilysin inhibition versus enalapril in heart failure (PARADIGM-HF). N Engl J Med 2014;371:993-1004 | 10.1056/NEJMoa1409077 | 25176015 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-193 | McMurray JJV, Solomon SD, Inzucchi SE, et al. Dapagliflozin in Patients with Heart Failure and Reduced Ejection Fraction (DAPA-HF). N Engl J Med 2019;381:1995-2008 | 10.1056/NEJMoa1911303 | 31535829 | NEJM の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-194 | Pitt B, Zannad F, Remme WJ, et al. The effect of spironolactone on morbidity and mortality in patients with severe heart failure (RALES). N Engl J Med 1999;341:709-717 | 10.1056/NEJM199909023411001 | 10471456 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-195 | Anker SD, Butler J, Filippatos G, et al. Empagliflozin in Heart Failure with a Preserved Ejection Fraction (EMPEROR-Preserved). N Engl J Med 2021;385:1451-1461 | 10.1056/NEJMoa2107038 | 34449189 | NEJM の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-196 | Cleland JGF, Daubert JC, Erdmann E, et al. The effect of cardiac resynchronization on morbidity and mortality in heart failure (CARE-HF). N Engl J Med 2005;352:1539-1549 | 10.1056/NEJMoa050496 | 15753115 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-197 | Baran DA, Grines CL, Bailey S, et al. SCAI clinical expert consensus statement on the classification of cardiogenic shock. Catheter Cardiovasc Interv 2019;94:29-37 | 10.1002/ccd.28329 | 31104355 | Wiley の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-198 | Hochman JS, Sleeper LA, Webb JG, et al. Early revascularization in acute myocardial infarction complicated by cardiogenic shock (SHOCK). N Engl J Med 1999;341:625-634 | 10.1056/NEJM199908263410901 | 10460813 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-199 | Thiele H, Zeymer U, Neumann FJ, et al. Intraaortic balloon support for myocardial infarction with cardiogenic shock (IABP-SHOCK II). N Engl J Med 2012;367:1287-1296 | 10.1056/NEJMoa1208410 | 22920912 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-200 | Thiele H, Akin I, Sandri M, et al. PCI Strategies in Patients with Acute Myocardial Infarction and Cardiogenic Shock (CULPRIT-SHOCK). N Engl J Med 2017;377:2419-2432 | 10.1056/NEJMoa1710261 | 29083953 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-201 | Møller JE, Engstrøm T, Jensen LO, et al. Microaxial Flow Pump or Standard Care in Infarct-Related Cardiogenic Shock (DanGer Shock). N Engl J Med 2024;390:1382-1393 | 10.1056/NEJMoa2312572 | 38587239 | NEJM の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-202 | Nakano S, Kohsaka S, Chikamori T, et al. JCS 2022 Guideline Focused Update on Diagnosis and Treatment in Patients With Stable Coronary Artery Disease. Circ J 2022;86:882-915 | 10.1253/circj.CJ-21-1041 | 35283401 | CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし） | RESTRICTED | CR・PM・JS（本文） | 3 |
| SRC-203 | Boden WE, O'Rourke RA, Teo KK, et al. Optimal medical therapy with or without PCI for stable coronary disease (COURAGE). N Engl J Med 2007;356:1503-1516 | 10.1056/NEJMoa070829 | 17387127 | 出版社の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-204 | Maron DJ, Hochman JS, Reynolds HR, et al. Initial Invasive or Conservative Strategy for Stable Coronary Disease (ISCHEMIA). N Engl J Med 2020;382:1395-1407 | 10.1056/NEJMoa1915922 | 32227755 | NEJM の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-205 | Hokimoto S, Kaikita K, Yasuda S, et al. JCS/CVIT/JCC 2023 Guideline Focused Update on Diagnosis and Treatment of Vasospastic Angina (Coronary Spastic Angina) and Coronary Microvascular Dysfunction. Circ J 2023;87:879-936 | 10.1253/circj.CJ-22-0779 | 36908169 | CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし） | RESTRICTED | CR・PM・JS（本文） | 2 |
| SRC-206 | Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196 | 10.1253/circj.CJ-19-0133 | 30930428 | © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし） | RESTRICTED | CR・PM・JS（本文） | 10 |
| SRC-207 | Nakamura M, Kimura K, Kimura T, et al. JCS 2020 Guideline Focused Update on Antithrombotic Therapy in Patients With Coronary Artery Disease. Circ J 2020;84:831-865 | 10.1253/circj.CJ-19-1109 | 32173684 | © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし） | RESTRICTED | CR・PM・JS（本文） | 3 |
| SRC-208 | Saito S, Isshiki T, Kimura T, et al. Efficacy and safety of adjusted-dose prasugrel compared with clopidogrel in Japanese patients with acute coronary syndrome: the PRASFIT-ACS study. Circ J 2014;78:1684-1692 | 10.1253/circj.CJ-13-1482 | 24759796 | 未確認（Crossref に license 欄なし。J-STAGE 掲載ページにライセンスの表示なし） | UNKNOWN | CR・PM（抄録）・JS（表示） | 1 |
| SRC-209 | Watanabe H, Domei T, Morimoto T, et al. Effect of 1-Month Dual Antiplatelet Therapy Followed by Clopidogrel vs 12-Month Dual Antiplatelet Therapy on Cardiovascular and Bleeding Events in Patients Receiving PCI: The STOPDAPT-2 Randomized Clinical Trial. JAMA 2019;321:2414-2427 | 10.1001/jama.2019.8145 | 31237644 | 出版社（AMA）の著作物（Crossref に license 欄なし。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-210 | Yasuda S, Kaikita K, Akao M, et al. Antithrombotic Therapy for Atrial Fibrillation with Stable Coronary Disease (AFIRE). N Engl J Med 2019;381:1103-1113 | 10.1056/NEJMoa1904143 | 31475793 | NEJM の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-211 | Young LH, Wackers FJT, Chyun DA, et al. Cardiac outcomes after screening for asymptomatic coronary artery disease in patients with type 2 diabetes: the DIAD study. JAMA 2009;301:1547-1555 | 10.1001/jama.2009.476 | 19366774 | 出版社（AMA）の著作物（Crossref に license 欄なし。PMC は著者稿） | RESTRICTED | CR・PM（抄録・PMCID） | 1 |
| SRC-212 | 総務省消防庁. 令和7年版 消防白書 第2章第5節（救急体制）：令和6年中の心肺機能停止傷病者の救命率 | — | — | 政府機関ウェブサイト（ページ表示は Copyright© Fire and Disaster Management Agency。利用規約の本文は未確認） | GOV_JP | FDMA（ウェブページ） | 1 |
| SRC-213 | Fukazawa R, Kobayashi J, Ayusawa M, et al. JCS/JSCS 2020 Guideline on Diagnosis and Management of Cardiovascular Sequelae in Kawasaki Disease. Circ J 2020;84:1348-1407 | 10.1253/circj.CJ-19-1094 | 32641591 | © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし） | RESTRICTED | CR・PM・JS（本文） | 2 |
| SRC-214 | Kobayashi T, Saji T, Otani T, et al. Efficacy of immunoglobulin plus prednisolone for prevention of coronary artery abnormalities in severe Kawasaki disease (RAISE study). Lancet 2012;379:1613-1620 | 10.1016/S0140-6736(11)61930-2 | 22405251 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-215 | Hamada H, Suzuki H, Onouchi Y, et al. Efficacy of primary treatment with immunoglobulin plus ciclosporin for prevention of coronary artery abnormalities in patients with Kawasaki disease predicted to be at increased risk of non-response to intravenous immunoglobulin (KAICA). Lancet 2019;393:1128-1137 | 10.1016/S0140-6736(18)32003-8 | 30853151 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |
| SRC-216 | Nakamura Y, Yashiro M, Yanagawa H, et al. Epidemiology of Kawasaki disease in Japan in 2021-2022: Results of the 27th nationwide survey. Pediatr Int 2025;67:e70007 | 10.1111/ped.70007 | 40189891 | Wiley の利用規約（Crossref の license 欄。CC の表示なし） | RESTRICTED | CR・PM（抄録） | 1 |

- SRC-170・173 の本文は PMC（J Arrhythm 版、CC BY 4.0）、SRC-181 は PMC の XML（CC BY-NC-ND 4.0）で確認しました。SRC-185・202・205・206・207・213 は J-STAGE の Circ J 版の本文で確認しました。
- 臨床試験・コホート研究はすべて PubMed の抄録で数値を確認しました。抄録にない数値は書いていません。

## 2. 事実票 YAML

```yaml
- id: AR-001
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 心房細動は持続期間で分類され、7日以内に自然停止するものを発作性、7日を超えて続くものを持続性、リズムコントロールを行う時点で1年以上続いているものを長期持続性、患者と医師がリズムの回復を目指さないことを受け入れたものを永続性とよぶ。初めて心電図で記録されたものは初発心房細動とする。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表18
      region: 日本
    differential: null
    common_misconception: 発作性は1日以内に止まるものに限られる
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
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-002
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 2003年の日本の定期健康診断（40歳以上の約63万人）では、心房細動の有病率は男性1.35%、女性0.43%で、80歳以上では男性4.4%、女性2.2%であった。この有病率から、日本の心房細動患者は約72万人（全人口の0.56%）と推計され、2050年には約103万人に増えると予測された。
    condition:
      region: 日本
      study: 健診データに基づく横断研究（2003年）
    differential: null
    common_misconception: 心房細動の有病率に男女差はない
  provenance:
    source_ref: SRC-171
    source: 'Inoue H, Fujiki A, Origasa H, et al. Prevalence of atrial fibrillation in the general population of Japan: an analysis based on periodic health examination. Int J Cardiol 2009;137:102-107'
    doi: 10.1016/j.ijcard.2008.06.029
    pmid: '18691774'
    pmcid: null
    url: https://doi.org/10.1016/j.ijcard.2008.06.029
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 健診受診者に基づく推計で、受診しない高齢者や発作性の見逃しを含まない可能性がある。
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-003
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: CHADS2スコアは、心不全・高血圧・75歳以上・糖尿病を各1点、脳梗塞または一過性脳虚血発作の既往を2点とする（最大6点）。米国の抗血栓薬を使っていない心房細動患者では、点数が1点上がるごとに脳梗塞の発生率がおよそ1.5倍になり、0点で年1.9%、6点で年18.2%であった。
    condition:
      region: 米国（Medicare 受給者、65〜95歳）
      study: NRAF 登録
    differential: null
    common_misconception: CHADS2の脳梗塞既往は1点である
  provenance:
    source_ref: SRC-172
    source: 'Gage BF, Waterman AD, Shannon W, et al. Validation of clinical classification schemes for predicting stroke: results from the National Registry of Atrial Fibrillation. JAMA 2001;285:2864-2870'
    doi: 10.1001/jama.285.22.2864
    pmid: '11401607'
    pmcid: null
    url: https://doi.org/10.1001/jama.285.22.2864
    source_license: 出版社（AMA）の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 発生率は抗血栓薬を使っていない高齢者集団の値で、現在の日本の患者にそのまま当てはまるとは限らない。
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-004
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 日本の心房細動患者の心原性脳塞栓症リスク評価として、JCS/JHRS 2024年改訂版は、CHADS2スコアの使用を推奨し（クラスI、レベルB）、日本独自のHELT-E2S2スコアの使用を考慮してよい（IIa、B）、CHA2DS2-VAScスコアの使用を考慮してもよい（IIb、B）としている。
    condition:
      guideline: JCS/JHRS 2024 不整脈 フォーカスアップデート 表19
      region: 日本
    differential: null
    common_misconception: 日本でもCHA2DS2-VAScが第一選択のスコアである
  provenance:
    source_ref: SRC-173
    source: Iwasaki YK, Noda T, Akao M, et al. JCS/JHRS 2024 Guideline Focused Update on Management of Cardiac Arrhythmias. J Arrhythm 2025;41:e70033（Circ J 2025;89:1012-1073 と同一内容の同時掲載）
    doi: 10.1002/joa3.70033
    pmid: '40524851'
    pmcid: PMC12168493
    url: https://doi.org/10.1002/joa3.70033
    source_license: CC BY 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-005
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: HELT-E2S2スコアは、日本の3つの心房細動レジストリ（J-RHYTHM、伏見AF、心研データベース）の統合解析から作られ、高血圧・75〜84歳・BMI 18.5未満・持続性または永続性心房細動を各1点、85歳以上と脳梗塞の既往を各2点とする。この解析では、糖尿病・心不全・血管疾患は独立した危険因子とならなかった。
    condition:
      guideline: JCS/JHRS 2024 不整脈 フォーカスアップデート 表18
      region: 日本
    differential: null
    common_misconception: 日本人でも糖尿病はCHADS2と同じく独立した脳塞栓の危険因子である
  provenance:
    source_ref: SRC-173
    source: Iwasaki YK, Noda T, Akao M, et al. JCS/JHRS 2024 Guideline Focused Update on Management of Cardiac Arrhythmias. J Arrhythm 2025;41:e70033（Circ J 2025;89:1012-1073 と同一内容の同時掲載）
    doi: 10.1002/joa3.70033
    pmid: '40524851'
    pmcid: PMC12168493
    url: https://doi.org/10.1002/joa3.70033
    source_license: CC BY 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-006
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: CHA2DS2-VAScスコアは、欧州の心房細動患者1,084人の調査（Euro Heart Survey）で検証された。このスコアで低リスクと分類された患者では血栓塞栓症が起きなかったのに対し、CHADS2で低リスクとされた患者では1.4%に起きた。
    condition:
      region: 欧州
      study: Euro Heart Survey on AF
    differential: null
    common_misconception: CHA2DS2-VAScは日本人のコホートから作られた
  provenance:
    source_ref: SRC-174
    source: 'Lip GYH, Nieuwlaat R, Pisters R, et al. Refining clinical risk stratification for predicting stroke and thromboembolism in atrial fibrillation using a novel risk factor-based approach: the Euro Heart Survey on Atrial Fibrillation. Chest 2010;137:263-272'
    doi: 10.1378/chest.09-1584
    pmid: '19762550'
    pmcid: null
    url: https://doi.org/10.1378/chest.09-1584
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 予測能（C統計量）はいずれのスコアも中等度であった。
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-007
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: HAS-BLEDスコアは、抗凝固療法中の心房細動患者の1年以内の大出血リスクを見積もる指標で、高血圧、腎・肝機能異常、脳卒中、出血の既往や素因、不安定なINR、65歳を超える高齢、薬剤またはアルコールを項目とする。欧州の3,978人で作られ、1年間の大出血は1.5%であった。
    condition:
      region: 欧州
      study: Euro Heart Survey on AF
    differential: null
    common_misconception: HAS-BLEDは脳梗塞リスクを評価するスコアである
  provenance:
    source_ref: SRC-175
    source: 'Pisters R, Lane DA, Nieuwlaat R, et al. A novel user-friendly score (HAS-BLED) to assess 1-year risk of major bleeding in patients with atrial fibrillation: the Euro Heart Survey. Chest 2010;138:1093-1100'
    doi: 10.1378/chest.10-0134
    pmid: '20299623'
    pmcid: null
    url: https://doi.org/10.1378/chest.10-0134
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 各項目の詳しい定義は抄録に記載がない。
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-008
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 心房細動に経口抗凝固療法を始めるとき、DOAC（ダビガトラン、リバーロキサバン、アピキサバン、エドキサバン）が使える患者ではワルファリンよりDOACが推奨される（クラスI、レベルA）。一方、中等度以上の僧帽弁狭窄症や機械弁を伴う心房細動では、ワルファリンが推奨される（I、B）。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表35
      region: 日本
    differential: null
    common_misconception: 機械弁置換後の心房細動にもDOACを使ってよい
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
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-009
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 日本で非弁膜症性心房細動に使うDOACの通常量と減量量は、ダビガトラン150 mgまたは110 mgを1日2回、リバーロキサバン15 mgまたは10 mgを1日1回、アピキサバン5 mgまたは2.5 mgを1日2回、エドキサバン60 mgまたは30 mgを1日1回である。アピキサバンは血清クレアチニン1.5 mg/dL以上・80歳以上・体重60 kg以下のうち2つ以上、エドキサバンはクレアチニンクリアランス50 mL/分未満・P糖蛋白阻害薬の併用・体重60 kg以下のいずれか1つで減量する。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表37
      region: 日本
    differential: null
    common_misconception: DOACの減量基準は4剤とも同じである
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
  uncertainty: 用量は2020年版の表による。その後の添付文書改訂は本出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-010
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 4つの大規模試験（計71,683人）のメタ解析では、DOACはワルファリンに比べて脳卒中・全身性塞栓症を19%減らし（相対リスク0.81）、頭蓋内出血をほぼ半分にし（0.48）、全死亡も減らした（0.90）。一方、消化管出血は増えた（1.25）。
    condition:
      region: 国際共同試験（RE-LY、ROCKET AF、ARISTOTLE、ENGAGE AF-TIMI 48）
    differential: null
    common_misconception: DOACは消化管出血も含めてすべての出血を減らす
  provenance:
    source_ref: SRC-176
    source: 'Ruff CT, Giugliano RP, Braunwald E, et al. Comparison of the efficacy and safety of new oral anticoagulants with warfarin in patients with atrial fibrillation: a meta-analysis of randomised trials. Lancet 2014;383:955-962'
    doi: 10.1016/S0140-6736(13)62343-0
    pmid: '24315724'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(13)62343-0
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-011
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 通常量の抗凝固薬が使えない80歳以上の日本人の非弁膜症性心房細動患者984人を対象としたELDERCARE-AF試験では、エドキサバン15 mg 1日1回はプラセボに比べ、脳卒中・全身性塞栓症を年6.7%から2.3%に減らした（ハザード比0.34）。大出血は年3.3%対1.8%で有意差はなかったが、消化管出血はエドキサバン群で多かった。
    condition:
      region: 日本
      study: ELDERCARE-AF（第3相、プラセボ対照）
    differential: null
    common_misconception: 高齢で出血リスクが高い患者には抗凝固療法を行わないのが原則である
  provenance:
    source_ref: SRC-177
    source: Okumura K, Akao M, Yoshida T, et al. Low-Dose Edoxaban in Very Elderly Patients with Atrial Fibrillation (ELDERCARE-AF). N Engl J Med 2020;383:1735-1745
    doi: 10.1056/NEJMoa2012883
    pmid: '32865374'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2012883
    source_license: NEJM の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: エドキサバン15 mgの国内承認の条件は本出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-012
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: JCS/JHRS 2024年改訂版は、抗凝固療法でリスクの高い高齢心房細動患者について、通常量が使えない出血リスクの高い超高齢者にエドキサバン15 mgを推奨し（クラスI、レベルB）、低体重・フレイル・認知機能低下（MMSE 23点以下）があっても抗凝固療法を考慮すべき（いずれもIIa、B）とし、抗血小板薬の併用は行うべきでない（III（有害）、B）としている。
    condition:
      guideline: JCS/JHRS 2024 不整脈 フォーカスアップデート 表21〜23
      region: 日本
    differential: null
    common_misconception: フレイルや認知症のある高齢者は抗凝固療法の対象外である
  provenance:
    source_ref: SRC-173
    source: Iwasaki YK, Noda T, Akao M, et al. JCS/JHRS 2024 Guideline Focused Update on Management of Cardiac Arrhythmias. J Arrhythm 2025;41:e70033（Circ J 2025;89:1012-1073 と同一内容の同時掲載）
    doi: 10.1002/joa3.70033
    pmid: '40524851'
    pmcid: PMC12168493
    url: https://doi.org/10.1002/joa3.70033
    source_license: CC BY 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 「超高齢」「出血リスクが高い」の定義は表の注に記載があるが、本カードでは扱っていない。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-013
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 腎機能が低下した高齢の心房細動患者について、JCS/JHRS 2024年改訂版は、クレアチニンクリアランス30〜50 mL/分では抗凝固療法を行い、ワルファリンよりDOACを選ぶことを推奨する（クラスI、レベルA）。15〜30 mL/分ではダビガトラン以外のDOACを考慮すべき（IIa、B）とし、透析患者へのワルファリンは推奨しない（III（無益）、B）。
    condition:
      guideline: JCS/JHRS 2024 不整脈 フォーカスアップデート 表20
      region: 日本
    differential: null
    common_misconception: 透析中の心房細動にはワルファリンが標準である
  provenance:
    source_ref: SRC-173
    source: Iwasaki YK, Noda T, Akao M, et al. JCS/JHRS 2024 Guideline Focused Update on Management of Cardiac Arrhythmias. J Arrhythm 2025;41:e70033（Circ J 2025;89:1012-1073 と同一内容の同時掲載）
    doi: 10.1002/joa3.70033
    pmid: '40524851'
    pmcid: PMC12168493
    url: https://doi.org/10.1002/joa3.70033
    source_license: CC BY 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-014
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 脳卒中や死亡のリスクが高い心房細動患者4,060人を対象としたAFFIRM試験では、リズムコントロール群とレートコントロール群の5年死亡率は23.8%と21.3%で有意差がなく（ハザード比1.15）、リズムコントロール群で入院と薬の副作用が多かった。脳梗塞の多くはワルファリン中止後かINRが不十分なときに起きた。
    condition:
      region: 北米
      study: AFFIRM
    differential: null
    common_misconception: 洞調律を維持すれば抗凝固薬はやめてよい
  provenance:
    source_ref: SRC-178
    source: Wyse DG, Waldo AL, DiMarco JP, et al (AFFIRM Investigators). A comparison of rate control and rhythm control in patients with atrial fibrillation. N Engl J Med 2002;347:1825-1833
    doi: 10.1056/NEJMoa021328
    pmid: '12466506'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa021328
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-015
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 診断から1年以内の早期心房細動で心血管疾患を伴う患者2,789人を対象としたEAST-AFNET 4試験では、抗不整脈薬またはアブレーションによる早期リズムコントロールが、通常治療に比べ心血管死・脳卒中・心不全または急性冠症候群による入院の複合を減らした（100人年あたり3.9対5.0、ハザード比0.79）。
    condition:
      region: 欧州
      study: EAST-AFNET 4
    differential: null
    common_misconception: リズムコントロールは予後を改善しないことが確立している
  provenance:
    source_ref: SRC-179
    source: Kirchhof P, Camm AJ, Goette A, et al. Early Rhythm-Control Therapy in Patients with Atrial Fibrillation (EAST-AFNET 4). N Engl J Med 2020;383:1305-1316
    doi: 10.1056/NEJMoa2019422
    pmid: '32865375'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2019422
    source_license: NEJM の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: リズムコントロール関連の重篤な有害事象は早期治療群で多かった（4.9%対1.4%）。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-016
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 心房細動のレートコントロールでは、左室駆出率が25%以上40%未満に低下した例にはβ遮断薬（ビソプロロール、カルベジロール）の長期経口投与が推奨され（クラスI、レベルA）、非ジヒドロピリジン系カルシウム拮抗薬は使うべきでない（III、C）。駆出率40%以上ではβ遮断薬またはベラパミル・ジルチアゼムが推奨される（I、B）。持続性・永続性心房細動では安静時心拍数110/分未満を目安とする。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表44と本文
      region: 日本
    differential: 目標心拍数は自覚症状や心不全の徴候に応じて個別に決める
    common_misconception: 心機能が低下した心房細動のレートコントロールにはベラパミルが第一選択である
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
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-017
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 血行動態が不安定な心房細動には、R波同期の直流通電による除細動を行う（クラスI、レベルC）。発症から48時間以内で抗凝固療法を行っていない場合も除細動を考慮でき、48時間を超えている可能性を否定できない場合は、経食道心エコーで心房内血栓がないことを確かめるか、3週間以上適切な抗凝固療法を続けてから行う（いずれもIIa、C）。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表45
      region: 日本
    differential: null
    common_misconception: 持続時間にかかわらず、すぐに電気的除細動をしてよい
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
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-018
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 心房細動のカテーテルアブレーションは、少なくとも1剤の抗不整脈薬が無効な症候性の発作性心房細動に推奨され（クラスI、レベルA）、症候性の発作性心房細動の第一選択（IIa、B）や症候性の持続性心房細動（IIa、B）にも考慮される。左房内血栓がある例と抗凝固療法が禁忌の例には行わない（III、A）。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表50
      region: 日本
    differential: null
    common_misconception: 抗凝固療法ができない患者こそアブレーションの適応である
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
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-019
  domain: AR
  subdomain: 心房細動
  assertion:
    plain_statement_ja: 心不全（左室駆出率35%以下、NYHA II〜IV度、植込み型除細動器あり）を伴う症候性心房細動患者363人を対象としたCASTLE-AF試験では、カテーテルアブレーションは薬物治療に比べ、全死亡または心不全悪化による入院を減らした（28.5%対44.6%、ハザード比0.62）。全死亡も13.4%対25.0%と少なかった。
    condition:
      region: 欧州・北米ほか
      study: CASTLE-AF
    differential: null
    common_misconception: 心不全を伴う心房細動にはアブレーションの適応はない
  provenance:
    source_ref: SRC-180
    source: Marrouche NF, Brachmann J, Andresen D, et al. Catheter Ablation for Atrial Fibrillation with Heart Failure (CASTLE-AF). N Engl J Med 2018;378:417-427
    doi: 10.1056/NEJMoa1707855
    pmid: '29385358'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1707855
    source_license: NEJM の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)；TBL-01-00-159 (id: Jlvnlr4)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-A-⑤（心房細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-020
  domain: AR
  subdomain: 心房粗動
  assertion:
    plain_statement_ja: 典型的心房粗動のカテーテルアブレーションは、症状がある場合または薬によるレートコントロール・リズムコントロールが効かない場合に推奨される（クラスI、レベルB）。
    condition:
      guideline: JCS/JHRS 2019 不整脈非薬物治療GL 表60
      region: 日本
    differential: null
    common_misconception: 心房粗動は薬物でしか治療できない
  provenance:
    source_ref: SRC-181
    source: Nogami A, Kurita T, Abe H, et al. JCS/JHRS 2019 guideline on non-pharmacotherapy of cardiac arrhythmias. J Arrhythm 2021;37:709-870（Circ J 2021;85:1104-1244 と同時掲載）
    doi: 10.1002/joa3.12491
    pmid: '34386109'
    pmcid: PMC8339126
    url: https://doi.org/10.1002/joa3.12491
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-167 (id: Jlvnlso)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-A-④（心房粗動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-021
  domain: AR
  subdomain: 発作性上室頻拍
  assertion:
    plain_statement_ja: QRS幅の狭い上室頻拍の停止には、迷走神経刺激（クラスI、レベルB）とATPの急速静注（I、A）が推奨され、血行動態が不安定な場合や薬が効かない場合は同期下の電気的除細動を行う（I、C）。ベラパミルまたはジルチアゼムの静注も考慮される（IIa、A）。ATPは日本では上室頻拍への適応外使用で、喘息患者には禁忌である。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表14・15
      region: 日本
    differential: null
    common_misconception: 上室頻拍の停止には最初からアミオダロンを使う
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
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-168 (id: Jlvnlsw)'
    kokushi: 医学各論 Ⅴ-1-A-②（発作性上室頻拍、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-022
  domain: AR
  subdomain: WPW症候群
  assertion:
    plain_statement_ja: 副伝導路のカテーテルアブレーションは、副伝導路を介する症候性の上室頻拍と、早期興奮を伴う症状の強い頻拍性心房細動・心房頻拍に推奨される（いずれもクラスI、レベルB）。無症状でも、早期興奮があると本人や他人に危険が及ぶ職業に就けない場合には考慮される（IIa、B）。
    condition:
      guideline: JCS/JHRS 2019 不整脈非薬物治療GL 表57
      region: 日本
    differential: null
    common_misconception: WPW型心電図は無症状でもすべてアブレーションの適応である
  provenance:
    source_ref: SRC-181
    source: Nogami A, Kurita T, Abe H, et al. JCS/JHRS 2019 guideline on non-pharmacotherapy of cardiac arrhythmias. J Arrhythm 2021;37:709-870（Circ J 2021;85:1104-1244 と同時掲載）
    doi: 10.1002/joa3.12491
    pmid: '34386109'
    pmcid: PMC8339126
    url: https://doi.org/10.1002/joa3.12491
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-173 (id: JlvnltU)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-A-③（WPW症候群、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-023
  domain: AR
  subdomain: WPW症候群
  assertion:
    plain_statement_ja: 副伝導路を順行する頻拍（逆方向性房室回帰性頻拍）でQRS幅が広い場合は、ATP、ベラパミル、ジルチアゼム、β遮断薬の静注を避け、Ⅰ群抗不整脈薬の静注を行う（クラスIIa、レベルC）。早期興奮を伴う心房細動で血行動態が不安定な場合は、直流通電による除細動を行う（I、C）。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表15の注・表45
      region: 日本
    differential: 早期興奮のない上室頻拍ではATPやベラパミルが使える
    common_misconception: WPW症候群の頻拍にはまずベラパミルを静注する
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
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-173 (id: JlvnltU)'
    kokushi: 医学各論 Ⅴ-1-A-③（WPW症候群、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-024
  domain: AR
  subdomain: 心室期外収縮
  assertion:
    plain_statement_ja: 器質的心疾患のない症候性の心室期外収縮には、生活の質の改善を目的にβ遮断薬やカルシウム拮抗薬を考慮できる（クラスIIa、レベルB）。頻発する期外収縮による心筋症ではβ遮断薬やアミオダロンを考慮できる（IIa、B）。心筋梗塞後の期外収縮にⅠA群・ⅠC群抗不整脈薬を使ってはならない（III、B）。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表13
      region: 日本
    differential: null
    common_misconception: 心筋梗塞後の心室期外収縮はⅠ群薬で抑えるべきである
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
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-172 (id: JlvnltI)'
    kokushi: 医学各論 Ⅴ-1-B-①（心室期外収縮、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-025
  domain: AR
  subdomain: 心室期外収縮
  assertion:
    plain_statement_ja: 心筋梗塞後の心室期外収縮を抑えられた患者を対象としたCAST試験では、エンカイニドとフレカイニドで死亡が増えたため投与が中止された。不整脈による死亡は実薬群43人に対しプラセボ群16人であった。
    condition:
      region: 北米
      study: CAST
    differential: null
    common_misconception: 期外収縮を抑えれば突然死が減る
  provenance:
    source_ref: SRC-182
    source: Echt DS, Liebson PR, Mitchell LB, et al. Mortality and morbidity in patients receiving encainide, flecainide, or placebo. The Cardiac Arrhythmia Suppression Trial. N Engl J Med 1991;324:781-788
    doi: 10.1056/NEJM199103213241201
    pmid: '1900101'
    pmcid: null
    url: https://doi.org/10.1056/NEJM199103213241201
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-172 (id: JlvnltI)；TBL-01-00-163 (id: JlvnlsQ)'
    kokushi: 医学各論 Ⅴ-1-B-①（心室期外収縮、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-026
  domain: AR
  subdomain: 心室頻拍
  assertion:
    plain_statement_ja: 器質的心疾患に伴う持続性心室頻拍で血行動態が不安定な場合は、ただちに直流通電を行う（クラスI、レベルB）。再発する心室頻拍と突然死の予防には植込み型除細動器（ICD）が推奨され（I、A）、虚血性心疾患による薬剤抵抗性の心室頻拍にはカテーテルアブレーションが推奨される（I、B）。除細動後も不安定な場合はアミオダロンまたはニフェカラントの静注を考慮する（IIa、A）。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表57
      region: 日本
    differential: null
    common_misconception: 脈のある不安定な心室頻拍にはまず抗不整脈薬を静注する
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
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-169 (id: Jlvnls0)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-B-②（心室頻拍、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-027
  domain: AR
  subdomain: 心室細動
  assertion:
    plain_statement_ja: 心室細動から蘇生した患者、または重い症状を伴う持続性心室頻拍の患者1,016人を対象としたAVID試験では、植込み型除細動器は抗不整脈薬（主にアミオダロン）より生存率が高く、3年生存率は75.4%対64.1%であった。
    condition:
      region: 北米
      study: AVID（二次予防）
    differential: null
    common_misconception: 致死性不整脈の二次予防はアミオダロンで十分である
  provenance:
    source_ref: SRC-183
    source: Antiarrhythmics versus Implantable Defibrillators (AVID) Investigators. A comparison of antiarrhythmic-drug therapy with implantable defibrillators in patients resuscitated from near-fatal ventricular arrhythmias. N Engl J Med 1997;337:1576-1584
    doi: 10.1056/NEJM199711273372202
    pmid: '9411221'
    pmcid: null
    url: https://doi.org/10.1056/NEJM199711273372202
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-171 (id: JlvnltA)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-B-③（心室細動、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-028
  domain: AR
  subdomain: 致死性不整脈
  assertion:
    plain_statement_ja: 心筋梗塞の既往があり左室駆出率30%以下の患者1,232人を対象としたMADIT-II試験では、電気生理検査によるリスク評価をせずに予防的に植込み型除細動器を入れると、通常治療に比べて死亡が減った（平均20か月で14.2%対19.8%、ハザード比0.69）。
    condition:
      region: 米国・欧州
      study: MADIT-II（一次予防）
    differential: null
    common_misconception: ICDの一次予防には電気生理検査で心室頻拍が誘発されることが必須である
  provenance:
    source_ref: SRC-184
    source: Moss AJ, Zareba W, Hall WJ, et al. Prophylactic implantation of a defibrillator in patients with myocardial infarction and reduced ejection fraction (MADIT-II). N Engl J Med 2002;346:877-883
    doi: 10.1056/NEJMoa013474
    pmid: '11907286'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa013474
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-171 (id: JlvnltA)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-D-③（致死性不整脈、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-029
  domain: AR
  subdomain: 致死性不整脈
  assertion:
    plain_statement_ja: 日本のガイドラインでは、冠動脈疾患（心筋梗塞から40日以上、血行再建から90日以上）で、至適薬物治療を受け、NYHA II度以上、左室駆出率35%以下、非持続性心室頻拍がある患者に、突然死の一次予防としてICDが推奨される（クラスI、レベルA）。非持続性心室頻拍がなくても、NYHA II度以上で駆出率35%以下ならICDを考慮すべきとされる（IIa、B）。
    condition:
      guideline: JCS/JHRS 2019 不整脈非薬物治療GL 表15
      region: 日本
    differential: null
    common_misconception: 心筋梗塞の直後でも駆出率が低ければすぐにICDを入れる
  provenance:
    source_ref: SRC-181
    source: Nogami A, Kurita T, Abe H, et al. JCS/JHRS 2019 guideline on non-pharmacotherapy of cardiac arrhythmias. J Arrhythm 2021;37:709-870（Circ J 2021;85:1104-1244 と同時掲載）
    doi: 10.1002/joa3.12491
    pmid: '34386109'
    pmcid: PMC8339126
    url: https://doi.org/10.1002/joa3.12491
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-D-③（致死性不整脈、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-030
  domain: AR
  subdomain: 洞不全症候群
  assertion:
    plain_statement_ja: 洞不全症候群では、失神・めまい・息切れ・心不全などの症状が徐脈、洞房ブロック、洞停止によることが確認された場合に、永久ペースメーカーが推奨される（クラスI、レベルC）。やめられない薬による場合も含む。徐脈頻脈症候群で頻拍を抑える薬が徐脈を悪化させる場合も考慮される（IIa、C）。
    condition:
      guideline: JCS/JHRS 2019 不整脈非薬物治療GL 表9
      region: 日本
    differential: null
    common_misconception: 無症状の洞停止もすべてペースメーカーの適応である
  provenance:
    source_ref: SRC-181
    source: Nogami A, Kurita T, Abe H, et al. JCS/JHRS 2019 guideline on non-pharmacotherapy of cardiac arrhythmias. J Arrhythm 2021;37:709-870（Circ J 2021;85:1104-1244 と同時掲載）
    doi: 10.1002/joa3.12491
    pmid: '34386109'
    pmcid: PMC8339126
    url: https://doi.org/10.1002/joa3.12491
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 無症状の洞房ブロック・洞停止はクラスIIb、レベルCとされている。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-164 (id: JlvnlsU)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-C-①（洞不全症候群、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-031
  domain: AR
  subdomain: 房室ブロック
  assertion:
    plain_statement_ja: 徐脈による症状を伴う2度・高度・3度房室ブロックには永久ペースメーカーが推奨される（クラスI、レベルC）。無症状の3度房室ブロックにも考慮される（IIa、C）。無症状の2度・高度房室ブロックでも、電気生理検査でヒス束内またはヒス束以下のブロックが示された場合などは考慮される（IIa、C）。
    condition:
      guideline: JCS/JHRS 2019 不整脈非薬物治療GL 表7
      region: 日本
    differential: null
    common_misconception: 3度房室ブロックは症状がなければ治療は不要である
  provenance:
    source_ref: SRC-181
    source: Nogami A, Kurita T, Abe H, et al. JCS/JHRS 2019 guideline on non-pharmacotherapy of cardiac arrhythmias. J Arrhythm 2021;37:709-870（Circ J 2021;85:1104-1244 と同時掲載）
    doi: 10.1002/joa3.12491
    pmid: '34386109'
    pmcid: PMC8339126
    url: https://doi.org/10.1002/joa3.12491
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-165 (id: Jlvnlsc)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-C-②（房室ブロック、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-032
  domain: AR
  subdomain: QT延長症候群
  assertion:
    plain_statement_ja: 先天性QT延長症候群は、二次性のQT延長の原因がない状態で、リスクスコアが3.5点以上、LQTSの遺伝子に明らかな病的変異がある、または繰り返し記録した12誘導心電図でBazett補正QT（QTc）が500 ms以上のいずれかで診断する。原因不明の失神がありQTcが480〜499 msの場合も診断できる。
    condition:
      guideline: JCS/JHRS 2019 不整脈非薬物治療GL 表25（HRS/EHRA/APHRS 2013 の基準を引用）
      region: 国際（日本の指針も採用）
    differential: null
    common_misconception: QTcが450 msを超えればそれだけでQT延長症候群と診断できる
  provenance:
    source_ref: SRC-181
    source: Nogami A, Kurita T, Abe H, et al. JCS/JHRS 2019 guideline on non-pharmacotherapy of cardiac arrhythmias. J Arrhythm 2021;37:709-870（Circ J 2021;85:1104-1244 と同時掲載）
    doi: 10.1002/joa3.12491
    pmid: '34386109'
    pmcid: PMC8339126
    url: https://doi.org/10.1002/joa3.12491
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-170 (id: Jlvnls8)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: 医学各論 Ⅴ-1-D-①（QT延長症候群、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-033
  domain: AR
  subdomain: QT延長症候群
  assertion:
    plain_statement_ja: 二次性（後天性）QT延長の原因には、Ⅰ群・Ⅲ群抗不整脈薬、マクロライド系やニューキノロン系抗菌薬、抗真菌薬、抗精神病薬、三環系抗うつ薬などの薬剤、徐脈、低カリウム・低マグネシウム・低カルシウム血症、急性心筋梗塞やたこつぼ心筋症、くも膜下出血などがある。
    condition:
      guideline: JCS/JHRS 2020 不整脈薬物治療GL 表61
      region: 日本
    differential: null
    common_misconception: QT延長は先天性のものに限られる
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
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-170 (id: Jlvnls8)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: 医学各論 Ⅴ-1-D-①（QT延長症候群、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-034
  domain: AR
  subdomain: Brugada症候群
  assertion:
    plain_statement_ja: Brugada症候群は、通常の肋間または高位肋間の誘導で記録される自然発生のtype 1心電図、発熱で誘発されたtype 1心電図、または薬物負荷でtype 2・3からtype 1に変わる心電図を確定所見とする。type 2・3の心電図だけでは診断しない。原因不明の心停止、夜間の苦悶様呼吸、不整脈が疑われる失神などを主要所見とする。
    condition:
      guideline: JCS/JHRS 2019 不整脈非薬物治療GL 表21
      region: 日本
    differential: null
    common_misconception: type 2のサドルバック型心電図だけでBrugada症候群と診断できる
  provenance:
    source_ref: SRC-181
    source: Nogami A, Kurita T, Abe H, et al. JCS/JHRS 2019 guideline on non-pharmacotherapy of cardiac arrhythmias. J Arrhythm 2021;37:709-870（Circ J 2021;85:1104-1244 と同時掲載）
    doi: 10.1002/joa3.12491
    pmid: '34386109'
    pmcid: PMC8339126
    url: https://doi.org/10.1002/joa3.12491
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-174 (id: Jlvnltc)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: 医学各論 Ⅴ-1-D-②（Brugada症候群、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: AR-035
  domain: AR
  subdomain: Brugada症候群
  assertion:
    plain_statement_ja: type 1 Brugada心電図があり、心停止からの蘇生歴または心室頻拍・心室細動の記録がある患者には植込み型除細動器が推奨される（クラスI、レベルB）。type 1心電図に不整脈性の失神または夜間の苦悶様呼吸を伴う場合も考慮すべきである（IIa、C）。
    condition:
      guideline: JCS/JHRS 2019 不整脈非薬物治療GL 表22
      region: 日本
    differential: null
    common_misconception: Brugada症候群の突然死予防はキニジンなどの薬物が第一選択である
  provenance:
    source_ref: SRC-181
    source: Nogami A, Kurita T, Abe H, et al. JCS/JHRS 2019 guideline on non-pharmacotherapy of cardiac arrhythmias. J Arrhythm 2021;37:709-870（Circ J 2021;85:1104-1244 と同時掲載）
    doi: 10.1002/joa3.12491
    pmid: '34386109'
    pmcid: PMC8339126
    url: https://doi.org/10.1002/joa3.12491
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-174 (id: Jlvnltc)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-1-D-②（Brugada症候群、b）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-001
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: JCS/JHFS 2025年版は心不全の国際的な定義・分類に合わせ、左室駆出率40%以下をHFrEF、41〜49%をHFmrEF、50%以上をHFpEFとする。初回40%以下だった駆出率が10ポイント以上改善して40%を超えたものをHFimpEFとする。
    condition:
      guideline: JCS/JHFS 2025 心不全GL
      region: 日本
    differential: null
    common_misconception: 駆出率が正常なら心不全ではない
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J 2025;89:1278-1444（J Card Fail 2025;31:1164-1322 と同時掲載）
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 国際的な定義（Universal Definition）の原典の表記は本カードでは確認していない。
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-159 (id: Jlvnlr4)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-002
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: JCS/JHFS 2025年版は、心不全のステージA（心不全のリスクがある）とステージB（前心不全）の説明を拡充し、ステージAの危険因子に慢性腎臓病を加えた。日本の疫学研究では、ステージCの69%、ステージDの51%がHFpEFと報告されている。
    condition:
      guideline: JCS/JHFS 2025 心不全GL
      region: 日本
    differential: null
    common_misconception: 心不全の大半は駆出率が低下したタイプである
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J 2025;89:1278-1444（J Card Fail 2025;31:1164-1322 と同時掲載）
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 69%・51%の値はガイドラインが引用した研究による（二次資料経由）。
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-159 (id: Jlvnlr4)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-003
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: 佐渡市の左室機能障害の有病率と人口推計をもとにした研究では、日本の左室機能障害の外来患者は2005年に約97.9万人で、高齢化により2030年には約130万人に達すると予測された。
    condition:
      region: 日本
      study: Sado Heart Failure Study と将来推計人口（2006年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-186
    source: 'Okura Y, Ramadan MM, Ohno Y, et al. Impending epidemic: future projection of heart failure in Japan to the year 2055. Circ J 2008;72:489-491'
    doi: 10.1253/circj.72.489
    pmid: '18296852'
    pmcid: null
    url: https://doi.org/10.1253/circj.72.489
    source_license: 未確認（Crossref に license 欄なし。掲載ページは未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 一地域の有病率をもとにした推計である。
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-159 (id: Jlvnlr4)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-004
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: 宮崎県延岡市の地域住民を対象とした研究（3年間、初回の心不全入院406件、平均82歳）では、心不全による初回入院の発生率は人口10万人年あたり129で、2015年の日本の人口で年齢調整すると105であった。発生率に男女差はなく、高齢になるほど急に上がった。
    condition:
      region: 日本
      study: 延岡市の地域住民研究
    differential: null
    common_misconception: 心不全の入院発生率は男性のほうが明らかに高い
  provenance:
    source_ref: SRC-187
    source: Marume K, Ogata S, Kaichi R, et al. Incidence Rate of Hospitalization for Heart Failure in a Japanese City - An Updated Reference for Japan's Aging Society. Circ Rep 2022;4:116-122
    doi: 10.1253/circrep.CR-21-0142
    pmid: '35342838'
    pmcid: PMC8901245
    url: https://doi.org/10.1253/circrep.CR-21-0142
    source_license: CC BY-NC-ND 4.0（PMC の XML の license 要素。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 一地域の研究である。
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-158 (id: Jlvnlrw)'
    kokushi: 医学各論 Ⅴ-2-A-③（急性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-005
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: 心不全の診断または除外のためにBNPまたはNT-proBNPを測定すべきとされ（クラスI、レベルA）、日本心不全学会は心不全を除外する目安としてBNP 35 pg/mL未満、NT-proBNP 125 pg/mL未満を示している。腎機能低下ではいずれも高値になる。
    condition:
      guideline: JCS/JHFS 2025 心不全GL
      region: 日本
    differential: null
    common_misconception: BNPが基準値をわずかに超えれば心不全と確定できる
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J 2025;89:1278-1444（J Card Fail 2025;31:1164-1322 と同時掲載）
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-159 (id: Jlvnlr4)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-006
  domain: HF
  subdomain: 急性心不全
  assertion:
    plain_statement_ja: 救急外来を急性の呼吸困難で受診した1,586人の研究では、BNPは病歴・身体所見・他の検査より正確に心不全を見分け、100 pg/mLをカットオフとした診断精度は83.4%、50 pg/mL未満の陰性的中率は96%であった。
    condition:
      region: 米国・欧州
      study: Breathing Not Properly
    differential: null
    common_misconception: BNPだけで心不全の診断を確定できる
  provenance:
    source_ref: SRC-188
    source: Maisel AS, Krishnaswamy P, Nowak RM, et al. Rapid measurement of B-type natriuretic peptide in the emergency diagnosis of heart failure. N Engl J Med 2002;347:161-167
    doi: 10.1056/NEJMoa020233
    pmid: '12124404'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa020233
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-158 (id: Jlvnlrw)；TBL-02-05-020 (id: JlAKpfU)'
    kokushi: 医学各論 Ⅴ-2-A-③（急性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-007
  domain: HF
  subdomain: 急性心不全
  assertion:
    plain_statement_ja: 急性の呼吸困難患者1,256人の国際共同解析では、NT-proBNPの年齢別のカットオフ（50歳未満450、50〜75歳900、75歳超1,800 pg/mL）が急性心不全の診断に有用で、感度90%、特異度84%であった。年齢によらない300 pg/mLでは、急性心不全を否定する陰性的中率が98%であった。
    condition:
      region: 国際（ICON）
    differential: null
    common_misconception: NT-proBNPは年齢に関係なく同じ値で判断する
  provenance:
    source_ref: SRC-189
    source: 'Januzzi JL Jr, van Kimmenade R, Lainchbury J, et al. NT-proBNP testing for diagnosis and short-term prognosis in acute destabilized heart failure: an international pooled analysis of 1256 patients: the International Collaborative of NT-proBNP Study. Eur Heart J 2006;27:330-337'
    doi: 10.1093/eurheartj/ehi631
    pmid: '16293638'
    pmcid: null
    url: https://doi.org/10.1093/eurheartj/ehi631
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-158 (id: Jlvnlrw)；TBL-02-05-020 (id: JlAKpfU)'
    kokushi: 医学各論 Ⅴ-2-A-③（急性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-008
  domain: HF
  subdomain: 急性心不全
  assertion:
    plain_statement_ja: 心不全で入院した452人の研究では、うっ血と低灌流の有無で4群（A：うっ血も低灌流もない、B：うっ血あり・灌流は保たれる、C：うっ血と低灌流がある、L：うっ血はなく低灌流がある）に分けると予後を予測でき、BとCは死亡または緊急心移植のリスクが高かった。
    condition:
      region: 米国
      study: Nohria-Stevenson 分類
    differential: null
    common_misconception: 臨床所見による分類は予後と関係しない
  provenance:
    source_ref: SRC-190
    source: Nohria A, Tsang SW, Fang JC, et al. Clinical assessment identifies hemodynamic profiles that predict outcomes in patients admitted with heart failure. J Am Coll Cardiol 2003;41:1797-1804
    doi: 10.1016/S0735-1097(03)00309-7
    pmid: '12767667'
    pmcid: null
    url: https://doi.org/10.1016/S0735-1097(03)00309-7
    source_license: Elsevier の open-access user license（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-158 (id: Jlvnlrw)'
    kokushi: 医学各論 Ⅴ-2-A-③（急性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-009
  domain: HF
  subdomain: 急性心不全
  assertion:
    plain_statement_ja: 急性心不全の発症早期（受診後6〜12時間）の対応には、初期の収縮期血圧と症状で5つに分けるクリニカルシナリオ（CS）が提案されている。CS1は収縮期血圧140 mmHg超、CS2は100〜140 mmHg、CS3は100 mmHg未満、CS4は急性冠症候群の徴候を伴うもの、CS5は孤立性の右心不全である。
    condition:
      region: 欧州・米国の専門家合意
    differential: null
    common_misconception: クリニカルシナリオは入院後の慢性期の治療方針を決めるための分類である
  provenance:
    source_ref: SRC-191
    source: Mebazaa A, Gheorghiade M, Piña IL, et al. Practical recommendations for prehospital and early in-hospital management of patients presenting with acute heart failure syndromes. Crit Care Med 2008;36(1 Suppl):S129-S139
    doi: 10.1097/01.CCM.0000296274.51933.4C
    pmid: '18158472'
    pmcid: null
    url: https://doi.org/10.1097/01.CCM.0000296274.51933.4C
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 抄録で確認した。各群の具体的な治療は本カードでは扱っていない。
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-158 (id: Jlvnlrw)'
    kokushi: 医学各論 Ⅴ-2-A-③（急性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-010
  domain: HF
  subdomain: 急性心不全
  assertion:
    plain_statement_ja: 急性非代償性心不全で体液貯留がある場合は、うっ血症状を和らげるためループ利尿薬を静注すべきとされる（クラスI、レベルC-EO）。初回の利尿薬に反応が乏しい場合は、増量またはトルバプタンやサイアザイド系利尿薬の併用を考慮できる（IIa、B-R）。血管拡張薬は低血圧がない場合に考慮してよく（IIb、B-NR）、高度の低血圧、心原性ショック、脱水、急性右室梗塞では使ってはならない（III（有害）、C-EO）。
    condition:
      guideline: JCS/JHFS 2025 心不全GL
      region: 日本
    differential: null
    common_misconception: 右室梗塞による低血圧にも硝酸薬を使う
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J 2025;89:1278-1444（J Card Fail 2025;31:1164-1322 と同時掲載）
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-158 (id: Jlvnlrw)'
    kokushi: 医学各論 Ⅴ-2-A-③（急性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-011
  domain: HF
  subdomain: 急性心不全
  assertion:
    plain_statement_ja: 急性心不全で呼吸不全（呼吸数25/分超、SpO2 90%未満）がある場合は、呼吸困難を和らげ気管挿管を避けるためにNPPVを速やかに始めるべきとされる（クラスI、レベルA）。SpO2 90%未満またはPaO2 60 mmHg未満では酸素療法を行う（I、C-EO）。
    condition:
      guideline: JCS/JHFS 2025 心不全GL
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J 2025;89:1278-1444（J Card Fail 2025;31:1164-1322 と同時掲載）
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-158 (id: Jlvnlrw)；TBL-02-05-020 (id: JlAKpfU)'
    kokushi: 医学各論 Ⅴ-2-A-③（急性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-012
  domain: HF
  subdomain: 急性心不全
  assertion:
    plain_statement_ja: 急性非代償性心不全では、ドブタミンは肺うっ血に低心拍出・組織低灌流を伴う場合に（クラスIIa、レベルC-LD）、ノルアドレナリンは十分な輸液後もショックや低血圧が続く場合に（IIa、B-R）考慮できる。低心拍出・低灌流・ショックがない患者に強心薬をルーチンで使ってはならない（III（有害）、C-EO）。
    condition:
      guideline: JCS/JHFS 2025 心不全GL
      region: 日本
    differential: null
    common_misconception: 急性心不全には全例に強心薬を使う
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J 2025;89:1278-1444（J Card Fail 2025;31:1164-1322 と同時掲載）
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-158 (id: Jlvnlrw)'
    kokushi: 医学各論 Ⅴ-2-A-③（急性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-013
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: 左室駆出率40%以下の心不全（HFrEF）では、禁忌がなければACE阻害薬（クラスI、レベルA）、β遮断薬（カルベジロールまたはビソプロロール、I、A）、ミネラルコルチコイド受容体拮抗薬（NYHA II〜IV度、I、A）、SGLT2阻害薬（エンパグリフロジンまたはダパグリフロジン、糖尿病の有無を問わず、I、A）を使う。ACE阻害薬かARBを使っているNYHA II〜III度の症候性患者ではARNIへの切り替えが推奨される（I、B-R）。
    condition:
      guideline: JCS/JHFS 2025 心不全GL（HFrEFの薬物治療の推奨表）
      region: 日本
    differential: 治療薬はできるだけ早く始め、目標量まで増やすことが推奨される（I、A）
    common_misconception: SGLT2阻害薬は糖尿病を合併した心不全にしか使わない
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J 2025;89:1278-1444（J Card Fail 2025;31:1164-1322 と同時掲載）
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-014
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: NYHA II〜IV度で駆出率40%以下の心不全患者8,442人を対象としたPARADIGM-HF試験では、サクビトリル・バルサルタン（ARNI）はエナラプリルに比べ、心血管死または心不全入院を減らし（21.8%対26.5%、ハザード比0.80）、全死亡も減らした（ハザード比0.84）。ARNI群では低血圧と重篤でない血管性浮腫が多く、腎機能障害・高カリウム血症・咳は少なかった。
    condition:
      region: 国際
      study: PARADIGM-HF
    differential: null
    common_misconception: ARNIはACE阻害薬と併用して使う
  provenance:
    source_ref: SRC-192
    source: McMurray JJV, Packer M, Desai AS, et al. Angiotensin-neprilysin inhibition versus enalapril in heart failure (PARADIGM-HF). N Engl J Med 2014;371:993-1004
    doi: 10.1056/NEJMoa1409077
    pmid: '25176015'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1409077
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ACE阻害薬との併用禁忌などの国内の添付文書の記載は本出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-015
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: 駆出率40%以下の心不全患者4,744人を対象としたDAPA-HF試験では、ダパグリフロジン10 mgはプラセボに比べ、心不全の悪化または心血管死を減らした（16.3%対21.2%、ハザード比0.74）。効果は糖尿病の有無で同様であった。
    condition:
      region: 国際
      study: DAPA-HF
    differential: null
    common_misconception: SGLT2阻害薬の心不全への効果は血糖低下によるものである
  provenance:
    source_ref: SRC-193
    source: McMurray JJV, Solomon SD, Inzucchi SE, et al. Dapagliflozin in Patients with Heart Failure and Reduced Ejection Fraction (DAPA-HF). N Engl J Med 2019;381:1995-2008
    doi: 10.1056/NEJMoa1911303
    pmid: '31535829'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1911303
    source_license: NEJM の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-016
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: 駆出率35%以下の重症心不全患者1,663人を対象としたRALES試験では、スピロノラクトン25 mgの追加で死亡が46%から35%に減り（相対リスク0.70）、心不全悪化による入院も減った。男性の10%に女性化乳房または乳房痛がみられた。
    condition:
      region: 国際
      study: RALES
    differential: null
    common_misconception: 重い高カリウム血症が多いためMRAは心不全に使えない
  provenance:
    source_ref: SRC-194
    source: Pitt B, Zannad F, Remme WJ, et al. The effect of spironolactone on morbidity and mortality in patients with severe heart failure (RALES). N Engl J Med 1999;341:709-717
    doi: 10.1056/NEJM199909023411001
    pmid: '10471456'
    pmcid: null
    url: https://doi.org/10.1056/NEJM199909023411001
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 重い高カリウム血症は両群とも少なかった（抄録）。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-017
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: 左室駆出率50%以上の症候性心不全（HFpEF）では、SGLT2阻害薬（エンパグリフロジンまたはダパグリフロジン）が心血管死または心不全入院を減らすため推奨され（クラスI、レベルA）、うっ血には利尿薬を使う（I、C-LD）。非ステロイド型MRAのフィネレノンは考慮でき（IIa、B-R）、ARNIは駆出率が正常より低い例で考慮してもよい（IIb、B-R）。
    condition:
      guideline: JCS/JHFS 2025 心不全GL
      region: 日本
    differential: null
    common_misconception: HFpEFには予後を改善する薬がない
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J 2025;89:1278-1444（J Card Fail 2025;31:1164-1322 と同時掲載）
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: フィネレノンの心不全への国内承認状況は本出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-018
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: 駆出率40%を超える心不全患者5,988人を対象としたEMPEROR-Preserved試験では、エンパグリフロジンはプラセボに比べ、心血管死または心不全入院を減らした（13.8%対17.1%、ハザード比0.79）。主に心不全入院の減少による効果であった。
    condition:
      region: 国際
      study: EMPEROR-Preserved
    differential: null
    common_misconception: SGLT2阻害薬はHFpEFの死亡を大きく減らす
  provenance:
    source_ref: SRC-195
    source: Anker SD, Butler J, Filippatos G, et al. Empagliflozin in Heart Failure with a Preserved Ejection Fraction (EMPEROR-Preserved). N Engl J Med 2021;385:1451-1461
    doi: 10.1056/NEJMoa2107038
    pmid: '34449189'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2107038
    source_license: NEJM の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-019
  domain: HF
  subdomain: 慢性心不全
  assertion:
    plain_statement_ja: NYHA III〜IV度で心臓の同期不全がある心不全患者813人を対象としたCARE-HF試験では、心臓再同期療法（CRT）の追加で、死亡または主要な心血管イベントによる入院が55%から39%に減り（ハザード比0.63）、死亡も30%から20%に減った。
    condition:
      region: 欧州
      study: CARE-HF
    differential: null
    common_misconception: CRTは症状を改善するが予後は変えない
  provenance:
    source_ref: SRC-196
    source: Cleland JGF, Daubert JC, Erdmann E, et al. The effect of cardiac resynchronization on morbidity and mortality in heart failure (CARE-HF). N Engl J Med 2005;352:1539-1549
    doi: 10.1056/NEJMoa050496
    pmid: '15753115'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa050496
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-2-A-④（慢性心不全、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-020
  domain: HF
  subdomain: 心原性ショック
  assertion:
    plain_statement_ja: 心原性ショックの患者は、機械的循環補助を管理できるICU・CCUに移すべきとされ（クラスI、レベルC-EO）、体液過剰の所見がなければ生理食塩液またはリンゲル液200 mL以上を15〜30分で投与することを考慮できる（IIa、C-EO）。侵襲的血行動態の指標では、心係数2.2 L/分/m²以下、心拍出力（CPO）0.6 W未満が心原性ショックの目安とされている。
    condition:
      guideline: JCS/JHFS 2025 心不全GL（表6を含む）
      region: 日本
    differential: null
    common_misconception: 心原性ショックでは輸液を一切してはならない
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J 2025;89:1278-1444（J Card Fail 2025;31:1164-1322 と同時掲載）
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-02-05-030 (id: JlAKpgE)'
    kokushi: 医学各論 Ⅴ-2-B（心原性ショック、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-021
  domain: HF
  subdomain: 心原性ショック
  assertion:
    plain_statement_ja: SCAI分類は心原性ショックの重症度をA（リスクあり）、B（始まり）、C（典型的）、D（悪化）、E（極限）の5段階に分ける。BとCの違いは低灌流の有無で、Dは最初の治療を少なくとも30分行っても安定せず灌流が回復しない状態である。
    condition:
      region: 米国の専門家合意（SCAI 2019）
    differential: null
    common_misconception: 低灌流がなく低血圧だけの状態も典型的な心原性ショックに含める
  provenance:
    source_ref: SRC-197
    source: Baran DA, Grines CL, Bailey S, et al. SCAI clinical expert consensus statement on the classification of cardiogenic shock. Catheter Cardiovasc Interv 2019;94:29-37
    doi: 10.1002/ccd.28329
    pmid: '31104355'
    pmcid: null
    url: https://doi.org/10.1002/ccd.28329
    source_license: Wiley の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2022年の改訂版の内容は本カードでは扱っていない。
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-2-B（心原性ショック、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-022
  domain: HF
  subdomain: 心原性ショック
  assertion:
    plain_statement_ja: 急性心筋梗塞に伴う心原性ショック患者302人を対象としたSHOCK試験では、緊急血行再建は初期の内科的安定化と比べて30日死亡率に有意差はなかった（46.7%対56.0%）が、6か月死亡率は低かった（50.3%対63.1%）。
    condition:
      region: 国際
      study: SHOCK
    differential: null
    common_misconception: 心原性ショックでは血行再建の効果はない
  provenance:
    source_ref: SRC-198
    source: Hochman JS, Sleeper LA, Webb JG, et al. Early revascularization in acute myocardial infarction complicated by cardiogenic shock (SHOCK). N Engl J Med 1999;341:625-634
    doi: 10.1056/NEJM199908263410901
    pmid: '10460813'
    pmcid: null
    url: https://doi.org/10.1056/NEJM199908263410901
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI)'
    kokushi: 医学各論 Ⅴ-2-B（心原性ショック、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-023
  domain: HF
  subdomain: 心原性ショック
  assertion:
    plain_statement_ja: 早期の血行再建を予定した急性心筋梗塞による心原性ショック患者600人を対象としたIABP-SHOCK II試験では、大動脈内バルーンパンピング（IABP）は30日死亡率を下げなかった（39.7%対41.3%）。
    condition:
      region: ドイツ
      study: IABP-SHOCK II
    differential: null
    common_misconception: 心原性ショックにIABPをルーチンで使うと死亡が減る
  provenance:
    source_ref: SRC-199
    source: Thiele H, Zeymer U, Neumann FJ, et al. Intraaortic balloon support for myocardial infarction with cardiogenic shock (IABP-SHOCK II). N Engl J Med 2012;367:1287-1296
    doi: 10.1056/NEJMoa1208410
    pmid: '22920912'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1208410
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)'
    kokushi: 医学各論 Ⅴ-2-B（心原性ショック、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-024
  domain: HF
  subdomain: 心原性ショック
  assertion:
    plain_statement_ja: 多枝病変のある急性心筋梗塞による心原性ショック患者706人を対象としたCULPRIT-SHOCK試験では、責任病変だけのPCIは即時の多枝PCIより、30日以内の死亡または腎代替療法を要する腎不全が少なかった（45.9%対55.4%、相対リスク0.83）。
    condition:
      region: 欧州
      study: CULPRIT-SHOCK
    differential: null
    common_misconception: 心原性ショックでは同じ手技で全病変を治療するほうがよい
  provenance:
    source_ref: SRC-200
    source: Thiele H, Akin I, Sandri M, et al. PCI Strategies in Patients with Acute Myocardial Infarction and Cardiogenic Shock (CULPRIT-SHOCK). N Engl J Med 2017;377:2419-2432
    doi: 10.1056/NEJMoa1710261
    pmid: '29083953'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1710261
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI)'
    kokushi: 医学各論 Ⅴ-2-B（心原性ショック、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: HF-025
  domain: HF
  subdomain: 心原性ショック
  assertion:
    plain_statement_ja: ST上昇型心筋梗塞による心原性ショック患者360人を対象としたDanGer Shock試験では、経皮的微小軸流ポンプ（Impella CP）の追加で180日死亡が58.5%から45.8%に減った（ハザード比0.74）が、重い出血・下肢虚血・溶血などの有害事象（24.0%対6.2%）と腎代替療法が増えた。
    condition:
      region: デンマーク・ドイツ・英国
      study: DanGer Shock
    differential: null
    common_misconception: 補助循環は合併症を増やさない
  provenance:
    source_ref: SRC-201
    source: Møller JE, Engstrøm T, Jensen LO, et al. Microaxial Flow Pump or Standard Care in Infarct-Related Cardiogenic Shock (DanGer Shock). N Engl J Med 2024;390:1382-1393
    doi: 10.1056/NEJMoa2312572
    pmid: '38587239'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2312572
    source_license: NEJM の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 国内での保険適用の条件は本出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)'
    kokushi: 医学各論 Ⅴ-2-B（心原性ショック、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-001
  domain: IH
  subdomain: 労作性狭心症
  assertion:
    plain_statement_ja: 安定冠動脈疾患が疑われ、検査前確率が中等度以上の患者には、診断とイベントリスク評価のために、冠動脈CT（解剖学的評価）または負荷心筋シンチグラフィ・負荷心臓MRI・負荷心エコー（機能的評価）による非侵襲的画像検査が推奨される（クラスI、レベルA）。
    condition:
      guideline: JCS 2022 安定冠動脈疾患 フォーカスアップデート 表7
      region: 日本
    differential: null
    common_misconception: 胸痛のある患者には最初から全例に冠動脈造影を行う
  provenance:
    source_ref: SRC-202
    source: Nakano S, Kohsaka S, Chikamori T, et al. JCS 2022 Guideline Focused Update on Diagnosis and Treatment in Patients With Stable Coronary Artery Disease. Circ J 2022;86:882-915
    doi: 10.1253/circj.CJ-21-1041
    pmid: '35283401'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-21-1041
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-029 (id: JlAKpgA)；TBL-02-05-028 (id: JlAKpf8)'
    kokushi: 医学各論 Ⅴ-5-A-①（労作性狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-002
  domain: IH
  subdomain: 労作性狭心症
  assertion:
    plain_statement_ja: 冠内圧の評価では、FFRが0.80を超える病変は一般に血行再建の対象とならず、iFRでは0.89がカットオフとして妥当とされる。日本のCVIT-DEFER研究では、FFRの測定で39%の患者の治療方針が変わり、PCIの実施が22%減った。
    condition:
      guideline: JCS 2022 安定冠動脈疾患 フォーカスアップデート
      region: 日本
    differential: null
    common_misconception: 冠動脈造影で狭窄が強く見えれば虚血の評価なしにステントを入れてよい
  provenance:
    source_ref: SRC-202
    source: Nakano S, Kohsaka S, Chikamori T, et al. JCS 2022 Guideline Focused Update on Diagnosis and Treatment in Patients With Stable Coronary Artery Disease. Circ J 2022;86:882-915
    doi: 10.1253/circj.CJ-21-1041
    pmid: '35283401'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-21-1041
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: CVIT-DEFER の数値はガイドラインが引用した研究による（二次資料経由）。
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-030 (id: JlAKpgE)；TBL-02-05-031 (id: JlAKpgI)'
    kokushi: 医学各論 Ⅴ-5-A-①（労作性狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-003
  domain: IH
  subdomain: 労作性狭心症
  assertion:
    plain_statement_ja: 安定冠動脈疾患の血行再建は、左主幹部病変で心血管イベントを減らすため（クラスI、レベルB）、非侵襲的画像で広範な虚血がある患者で予後改善のため（I、B）、至適薬物治療でも日常生活を制限する狭心症が残る患者で症状改善のため（I、A）に推奨される。後の2つは共同意思決定にもとづく。
    condition:
      guideline: JCS 2022 安定冠動脈疾患 フォーカスアップデート 表10
      region: 日本
    differential: null
    common_misconception: 安定狭心症はすべてPCIで治療すべきである
  provenance:
    source_ref: SRC-202
    source: Nakano S, Kohsaka S, Chikamori T, et al. JCS 2022 Guideline Focused Update on Diagnosis and Treatment in Patients With Stable Coronary Artery Disease. Circ J 2022;86:882-915
    doi: 10.1253/circj.CJ-21-1041
    pmid: '35283401'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-21-1041
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-031 (id: JlAKpgI)'
    kokushi: 医学各論 Ⅴ-5-A-①（労作性狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-004
  domain: IH
  subdomain: 労作性狭心症
  assertion:
    plain_statement_ja: 心筋虚血のある安定冠動脈疾患患者2,287人を対象としたCOURAGE試験では、至適薬物治療にPCIを加えても、死亡または非致死性心筋梗塞は減らなかった（中央値4.6年で19.0%対18.5%、ハザード比1.05）。
    condition:
      region: 米国・カナダ
      study: COURAGE
    differential: null
    common_misconception: 安定狭心症にPCIを行うと心筋梗塞と死亡が減る
  provenance:
    source_ref: SRC-203
    source: Boden WE, O'Rourke RA, Teo KK, et al. Optimal medical therapy with or without PCI for stable coronary disease (COURAGE). N Engl J Med 2007;356:1503-1516
    doi: 10.1056/NEJMoa070829
    pmid: '17387127'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa070829
    source_license: 出版社の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-031 (id: JlAKpgI)'
    kokushi: 医学各論 Ⅴ-5-A-①（労作性狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-005
  domain: IH
  subdomain: 労作性狭心症
  assertion:
    plain_statement_ja: 中等度以上の虚血がある安定冠動脈疾患患者5,179人を対象としたISCHEMIA試験では、初期の侵襲的戦略は保存的戦略に比べて虚血性心血管イベントや全死亡を減らさなかった（中央値3.2年）。イベント率は6か月では侵襲的戦略で高く（5.3%対3.4%）、5年では低かった（16.4%対18.2%）が、差は有意でなかった。
    condition:
      region: 国際
      study: ISCHEMIA
    differential: null
    common_misconception: 中等度以上の虚血があれば早期の血行再建で死亡が減る
  provenance:
    source_ref: SRC-204
    source: Maron DJ, Hochman JS, Reynolds HR, et al. Initial Invasive or Conservative Strategy for Stable Coronary Disease (ISCHEMIA). N Engl J Med 2020;382:1395-1407
    doi: 10.1056/NEJMoa1915922
    pmid: '32227755'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1915922
    source_license: NEJM の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 結果は心筋梗塞の定義によって変わった。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-031 (id: JlAKpgI)'
    kokushi: 医学各論 Ⅴ-5-A-①（労作性狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-006
  domain: IH
  subdomain: 冠攣縮性狭心症
  assertion:
    plain_statement_ja: 冠攣縮性狭心症は、ニトログリセリンで発作がすぐ消えることに加え、安静時（特に夜間から早朝）の発作、運動耐容能の日内変動（早朝の低下）、発作時のST上昇、過換気による誘発、カルシウム拮抗薬で抑えられβ遮断薬で抑えられないことのいずれか1つがあれば、冠動脈造影をしなくても診断できるとする基準（Yasueら）がある。
    condition:
      guideline: JCS/CVIT/JCC 2023 冠攣縮性狭心症 フォーカスアップデート
      region: 日本
    differential: null
    common_misconception: 冠攣縮性狭心症は労作で起きるのが典型である
  provenance:
    source_ref: SRC-205
    source: Hokimoto S, Kaikita K, Yasuda S, et al. JCS/CVIT/JCC 2023 Guideline Focused Update on Diagnosis and Treatment of Vasospastic Angina (Coronary Spastic Angina) and Coronary Microvascular Dysfunction. Circ J 2023;87:879-936
    doi: 10.1253/circj.CJ-22-0779
    pmid: '36908169'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-22-0779
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-161 (id: JlvnlsE)'
    kokushi: 医学各論 Ⅴ-5-A-②（冠攣縮性狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-007
  domain: IH
  subdomain: 冠攣縮性狭心症
  assertion:
    plain_statement_ja: アセチルコリンまたはエルゴノビンによる冠攣縮誘発試験は、心筋虚血の徴候・症状（胸痛と虚血性の心電図変化）を伴って冠動脈が一時的に完全または亜完全に閉塞する（90%を超える狭窄）か、連続する2つ以上の区域に90%のびまん性の収縮が起きた場合を陽性とする。
    condition:
      guideline: JCS/CVIT/JCC 2023 冠攣縮性狭心症 フォーカスアップデート
      region: 日本
    differential: null
    common_misconception: 誘発試験は胸痛がなくても血管が少し細くなれば陽性である
  provenance:
    source_ref: SRC-205
    source: Hokimoto S, Kaikita K, Yasuda S, et al. JCS/CVIT/JCC 2023 Guideline Focused Update on Diagnosis and Treatment of Vasospastic Angina (Coronary Spastic Angina) and Coronary Microvascular Dysfunction. Circ J 2023;87:879-936
    doi: 10.1253/circj.CJ-22-0779
    pmid: '36908169'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-22-0779
    source_license: CC BY-NC-ND 4.0（J-STAGE 掲載ページの表示。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-161 (id: JlvnlsE)；TBL-02-05-029 (id: JlAKpgA)'
    kokushi: 医学各論 Ⅴ-5-A-②（冠攣縮性狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-008
  domain: IH
  subdomain: 冠攣縮性狭心症
  assertion:
    plain_statement_ja: 冠攣縮が原因の場合や冠攣縮性狭心症には、発作予防のため長時間作用型のカルシウム拮抗薬が推奨される（クラスI、レベルB）。冠攣縮が基礎にある患者にβ遮断薬を単独で使ってはならない（III（有害）、B）。日本人の心筋梗塞患者では、発症早期の誘発試験で冠攣縮が欧米人の約3倍多いと報告されている。
    condition:
      guideline: JCS 2018 急性冠症候群GL 表47・表84
      region: 日本
    differential: null
    common_misconception: 冠攣縮性狭心症にはβ遮断薬単独が第一選択である
  provenance:
    source_ref: SRC-206
    source: Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196
    doi: 10.1253/circj.CJ-19-0133
    pmid: '30930428'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-0133
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 約3倍の値はガイドラインが引用した研究による（二次資料経由）。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-161 (id: JlvnlsE)'
    kokushi: 医学各論 Ⅴ-5-A-②（冠攣縮性狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-009
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: 急性冠症候群を疑う症状がある患者には、到着後10分以内に12誘導心電図を記録する（クラスI、レベルC）。診断には心筋トロポニン（IまたはT）を測定し（I、C）、トロポニンが測れる場合はCK-MBやミオグロビンを診断に使うことは推奨されない（III（無益）、A）。
    condition:
      guideline: JCS 2018 急性冠症候群GL 表5・表6
      region: 日本
    differential: 初回の心電図で診断がつかない場合は5〜10分ごとに繰り返し記録する
    common_misconception: トロポニンが正常なら1回の測定で心筋梗塞を否定できる
  provenance:
    source_ref: SRC-206
    source: Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196
    doi: 10.1253/circj.CJ-19-0133
    pmid: '30930428'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-0133
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-026 (id: JlAKpf0)；TBL-02-05-021 (id: JlAKpfI)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-010
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: ST上昇型心筋梗塞の再灌流は発症から120分以内を目標とし、そのために線溶療法を選ぶ場合は医療者との最初の接触（救急隊を含む）から30分以内、PCIを選ぶ場合は90分以内に治療を始めることを目標とする。再灌流療法のできない施設では、到着から転送までの時間を30分以内にすることが目標とされる。
    condition:
      guideline: JCS 2018 急性冠症候群GL（本文）
      region: 日本
    differential: null
    common_misconception: door-to-balloon時間を短くすることだけが目標である
  provenance:
    source_ref: SRC-206
    source: Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196
    doi: 10.1253/circj.CJ-19-0133
    pmid: '30930428'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-0133
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 日本のCREDO-Kyoto AMIレジストリでは、door-to-balloon 90分未満と以上で長期予後に差がなかったと引用されている。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-011
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: ST上昇型心筋梗塞では、発症12時間以内に速やかにプライマリーPCI（ステント留置を含む）を行う（クラスI、レベルA）。発症3時間以内でPCIまでの遅れが1時間を超える場合は線溶療法を考慮し（I、B）、最初の医療接触から120分以内にPCIができない場合は、発症12時間以内なら線溶療法を行う（I、A）。ST上昇のない患者（後壁梗塞を除く）に線溶療法を行ってはならない（III（有害）、B）。
    condition:
      guideline: JCS 2018 急性冠症候群GL 表18・表29
      region: 日本
    differential: 75歳以上では線溶薬の半量を考慮する（IIa、B）
    common_misconception: 非ST上昇型の急性冠症候群にも線溶療法が有効である
  provenance:
    source_ref: SRC-206
    source: Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196
    doi: 10.1253/circj.CJ-19-0133
    pmid: '30930428'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-0133
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-012
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: 心筋虚血による胸部症状にはニトログリセリンの舌下投与またはスプレーを使う（クラスI、レベルC）。ただし、右室梗塞を合併した下壁梗塞、収縮期血圧90 mmHg未満（または基礎値から30 mmHg以上の低下）、高度の徐脈（50/分未満）、頻脈（100/分超）では使ってはならず（III（有害）、C）、勃起不全治療薬の服用後24時間以内も使ってはならない（III（有害）、B）。
    condition:
      guideline: JCS 2018 急性冠症候群GL 表15
      region: 日本
    differential: null
    common_misconception: 右室梗塞の胸痛にはまず硝酸薬を使う
  provenance:
    source_ref: SRC-206
    source: Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196
    doi: 10.1253/circj.CJ-19-0133
    pmid: '30930428'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-0133
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 勃起不全治療薬の種類による違い（タダラフィルなど）は本カードでは扱っていない。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-01-00-157 (id: Jlvnlro)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-013
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: 下壁のST上昇型心筋梗塞では右側胸部誘導（特にV4R）を追加記録し、V4Rで1.0 mm（0.1 mV）以上のST上昇があれば右室梗塞と診断できる。標準12誘導で捉えにくい後壁梗塞は、背部誘導（V7〜V9）の連続する2誘導以上で0.5 mm（0.05 mV）以上のST上昇で診断される。
    condition:
      guideline: JCS 2018 急性冠症候群GL（本文）
      region: 日本
    differential: null
    common_misconception: 右室梗塞と後壁梗塞は標準12誘導だけで十分に診断できる
  provenance:
    source_ref: SRC-206
    source: Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196
    doi: 10.1253/circj.CJ-19-0133
    pmid: '30930428'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-0133
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-026 (id: JlAKpf0)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-014
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: 急性冠症候群が強く疑われる場合はアスピリン162〜200 mgをかみ砕いて服用させる（クラスI、レベルA）。プライマリーPCIの前にはアスピリン162〜325 mgを投与し、PCI後は禁忌がなければ81〜162 mg/日を生涯続ける（いずれもI、A）。
    condition:
      guideline: JCS 2018 急性冠症候群GL 表17・表24
      region: 日本
    differential: null
    common_misconception: アスピリンは腸溶錠をそのまま飲み込めば十分である
  provenance:
    source_ref: SRC-206
    source: Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196
    doi: 10.1253/circj.CJ-19-0133
    pmid: '30930428'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-0133
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-015
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: 日本のガイドラインは、ST上昇型心筋梗塞のプライマリーPCI前のP2Y12阻害薬の負荷投与として、プラスグレル20 mgを推奨し（クラスI、レベルA）、プラスグレルが使えないか禁忌の場合はクロピドグレル300 mgを推奨する（I、A）。チカグレロル180 mgは両者が使えない場合に考慮してもよい（IIb、B）。
    condition:
      guideline: JCS 2020 抗血栓療法 フォーカスアップデート 表10
      region: 日本
    differential: null
    common_misconception: 日本でもチカグレロルが第一選択のP2Y12阻害薬である
  provenance:
    source_ref: SRC-207
    source: Nakamura M, Kimura K, Kimura T, et al. JCS 2020 Guideline Focused Update on Antithrombotic Therapy in Patients With Coronary Artery Disease. Circ J 2020;84:831-865
    doi: 10.1253/circj.CJ-19-1109
    pmid: '32173684'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-1109
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-016
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: PCIを受けた日本人の急性冠症候群患者1,363人を対象としたPRASFIT-ACS試験では、日本人向けに減量したプラスグレル（負荷20 mg、維持3.75 mg）は、クロピドグレル（300 mg、75 mg）に比べ24週の主要心血管イベントが9.4%対11.8%（ハザード比0.77、95%信頼区間0.56〜1.07）で、CABGに関連しない大出血は1.9%対2.2%と同程度であった。
    condition:
      region: 日本
      study: PRASFIT-ACS
    differential: null
    common_misconception: 日本人でも欧米と同じ用量のプラスグレルを使う
  provenance:
    source_ref: SRC-208
    source: 'Saito S, Isshiki T, Kimura T, et al. Efficacy and safety of adjusted-dose prasugrel compared with clopidogrel in Japanese patients with acute coronary syndrome: the PRASFIT-ACS study. Circ J 2014;78:1684-1692'
    doi: 10.1253/circj.CJ-13-1482
    pmid: '24759796'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-13-1482
    source_license: 未確認（Crossref に license 欄なし。J-STAGE 掲載ページにライセンスの表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 主要心血管イベントの差は統計学的に有意ではなかった（点推定での比較）。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-017
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: 急性冠症候群でステントを留置した後は、アスピリン81〜162 mgにプラスグレル3.75 mgまたはクロピドグレル75 mgを加えた抗血小板薬2剤併用療法（DAPT）を3〜12か月行うことが推奨される（クラスI、レベルA）。出血リスクが高い患者ではDAPTを1〜3か月に短縮することが推奨される（I、A）。安定冠動脈疾患でのステント留置後のDAPTは1〜3か月が推奨される（I、A）。
    condition:
      guideline: JCS 2020 抗血栓療法 フォーカスアップデート 表14・表17
      region: 日本
    differential: 出血リスクの評価にはARC-HBRに低体重・フレイル・心不全・透析を加えた日本版の基準が提案されている
    common_misconception: DAPTは全例で12か月以上続ける
  provenance:
    source_ref: SRC-207
    source: Nakamura M, Kimura K, Kimura T, et al. JCS 2020 Guideline Focused Update on Antithrombotic Therapy in Patients With Coronary Artery Disease. Circ J 2020;84:831-865
    doi: 10.1253/circj.CJ-19-1109
    pmid: '32173684'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-1109
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-018
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: 日本でPCIを受けた3,045人を対象としたSTOPDAPT-2試験では、1か月のDAPTの後にクロピドグレル単剤にする方法は、12か月のDAPTに比べ、心血管イベントと出血の複合が少なく（2.36%対3.70%、ハザード比0.64）、出血は大きく減った（0.41%対1.54%）。
    condition:
      region: 日本
      study: STOPDAPT-2
    differential: null
    common_misconception: DAPTを短くすると必ず血栓イベントが増える
  provenance:
    source_ref: SRC-209
    source: 'Watanabe H, Domei T, Morimoto T, et al. Effect of 1-Month Dual Antiplatelet Therapy Followed by Clopidogrel vs 12-Month Dual Antiplatelet Therapy on Cardiovascular and Bleeding Events in Patients Receiving PCI: The STOPDAPT-2 Randomized Clinical Trial. JAMA 2019;321:2414-2427'
    doi: 10.1001/jama.2019.8145
    pmid: '31237644'
    pmcid: null
    url: https://doi.org/10.1001/jama.2019.8145
    source_license: 出版社（AMA）の著作物（Crossref に license 欄なし。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 対象には安定冠動脈疾患も含まれる。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-019
  domain: IH
  subdomain: 急性冠症候群
  assertion:
    plain_statement_ja: 高リスクの非ST上昇型急性冠症候群には早期侵襲的戦略が推奨され（クラスI、レベルA）、中等度から高リスクの患者がPCIのできない病院を受診した場合は、ただちにPCIのできる施設に転送する（I、C）。
    condition:
      guideline: JCS 2018 急性冠症候群GL 表35
      region: 日本
    differential: null
    common_misconception: 非ST上昇型の急性冠症候群は全例が保存的治療でよい
  provenance:
    source_ref: SRC-206
    source: Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196
    doi: 10.1253/circj.CJ-19-0133
    pmid: '30930428'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-0133
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-162 (id: JlvnlsI)；TBL-01-00-163 (id: JlvnlsQ)'
    kokushi: 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-020
  domain: IH
  subdomain: 陳旧性心筋梗塞
  assertion:
    plain_statement_ja: 経口抗凝固薬が必要な冠動脈疾患患者では、ステント留置の周術期（2週間以内）は3剤併用、その後はP2Y12阻害薬と抗凝固薬の併用が推奨される（周術期はクラスI、レベルC、その後はI、A）。ステント留置から1年を超えた患者、CABG後、血行再建をしていない患者では、抗血小板薬を使わない抗凝固薬単剤が推奨される（I、B）。非弁膜症性心房細動ではワルファリンよりDOACを選ぶ（I、A）。
    condition:
      guideline: JCS 2020 抗血栓療法 フォーカスアップデート 表19
      region: 日本
    differential: null
    common_misconception: 心房細動とステント留置後の患者は生涯3剤を続ける
  provenance:
    source_ref: SRC-207
    source: Nakamura M, Kimura K, Kimura T, et al. JCS 2020 Guideline Focused Update on Antithrombotic Therapy in Patients With Coronary Artery Disease. Circ J 2020;84:831-865
    doi: 10.1253/circj.CJ-19-1109
    pmid: '32173684'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-1109
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 抗凝固薬単剤の推奨の根拠はリバーロキサバンのデータである。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-5-C（陳旧性心筋梗塞、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-021
  domain: IH
  subdomain: 陳旧性心筋梗塞
  assertion:
    plain_statement_ja: PCIまたはCABGから1年以上たった、または血行再建を要しない冠動脈疾患を伴う心房細動患者2,236人を対象とした日本のAFIRE試験では、リバーロキサバン単剤は抗血小板薬との併用に比べ、有効性で非劣性（年4.14%対5.75%、ハザード比0.72）、大出血で優越していた（年1.62%対2.76%、ハザード比0.59）。併用群で死亡が多かったため試験は早期に終了した。
    condition:
      region: 日本
      study: AFIRE
    differential: null
    common_misconception: 安定冠動脈疾患を伴う心房細動には抗凝固薬と抗血小板薬の併用を続ける
  provenance:
    source_ref: SRC-210
    source: Yasuda S, Kaikita K, Akao M, et al. Antithrombotic Therapy for Atrial Fibrillation with Stable Coronary Disease (AFIRE). N Engl J Med 2019;381:1103-1113
    doi: 10.1056/NEJMoa1904143
    pmid: '31475793'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1904143
    source_license: NEJM の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-01-00-166 (id: Jlvnlsg)'
    kokushi: 医学各論 Ⅴ-5-C（陳旧性心筋梗塞、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-022
  domain: IH
  subdomain: 陳旧性心筋梗塞
  assertion:
    plain_statement_ja: 心筋梗塞後の二次予防では、最大耐用量のストロングスタチンを使う（クラスI、レベルA）。それでもLDLコレステロールが70 mg/dL未満にならない高リスク患者にはエゼチミブを考慮すべきとされる（IIa、B）。心不全の徴候があるか駆出率40%以下ならβ遮断薬とACE阻害薬の長期投与が推奨される（いずれもI、A）。
    condition:
      guideline: JCS 2018 急性冠症候群GL 表84・85・88
      region: 日本
    differential: null
    common_misconception: 心筋梗塞後のLDLコレステロールの目標は一次予防と同じである
  provenance:
    source_ref: SRC-206
    source: Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196
    doi: 10.1253/circj.CJ-19-0133
    pmid: '30930428'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-0133
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: LDLコレステロールの目標値は後に動脈硬化学会のガイドラインで改訂されている可能性があるが、本カードは2018年版の記載に限る。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)'
    kokushi: 医学各論 Ⅴ-5-C（陳旧性心筋梗塞、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-023
  domain: IH
  subdomain: 心臓性突然死
  assertion:
    plain_statement_ja: 急性心筋梗塞の発症から48時間を過ぎて起きた、虚血や他の可逆的な原因によらない持続性心室頻拍・心室細動には、植込み型除細動器が推奨される（クラスI、レベルB）。非持続性心室頻拍の患者は、至適薬物治療のもとで発症40日以降に適応を見直す。
    condition:
      guideline: JCS 2018 急性冠症候群GL 表54
      region: 日本
    differential: null
    common_misconception: 心筋梗塞の急性期に起きた心室細動はすべてICDの適応である
  provenance:
    source_ref: SRC-206
    source: Kimura K, Kimura T, Ishihara M, et al. JCS 2018 Guideline on Diagnosis and Treatment of Acute Coronary Syndrome. Circ J 2019;83:1085-1196
    doi: 10.1253/circj.CJ-19-0133
    pmid: '30930428'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-0133
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-01-00-171 (id: JlvnltA)；TBL-02-05-032 (id: JlAKpgM)'
    kokushi: 医学各論 Ⅴ-5-B-②（心臓性突然死、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-024
  domain: IH
  subdomain: 無痛性虚血性心疾患
  assertion:
    plain_statement_ja: 症状のない2型糖尿病患者1,123人を対象としたDIAD試験では、アデノシン負荷心筋シンチグラフィによるスクリーニングは、4.8年間の心臓死・非致死性心筋梗塞を減らさなかった（2.7%対3.0%、ハザード比0.88）。中等度以上の欠損があった場合の陽性的中率は12%にとどまった。
    condition:
      region: 米国・カナダ
      study: DIAD
    differential: null
    common_misconception: 症状のない糖尿病患者全員に負荷検査を行えば心筋梗塞を防げる
  provenance:
    source_ref: SRC-211
    source: 'Young LH, Wackers FJT, Chyun DA, et al. Cardiac outcomes after screening for asymptomatic coronary artery disease in patients with type 2 diabetes: the DIAD study. JAMA 2009;301:1547-1555'
    doi: 10.1001/jama.2009.476
    pmid: '19366774'
    pmcid: PMC2895332
    url: https://doi.org/10.1001/jama.2009.476
    source_license: 出版社（AMA）の著作物（Crossref に license 欄なし。PMC は著者稿）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: differential は本出典の結論ではない一般的な背景である。
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-028 (id: JlAKpf8)'
    kokushi: 医学各論 Ⅴ-5-D（無痛性虚血性心疾患、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-025
  domain: IH
  subdomain: 心臓性突然死
  assertion:
    plain_statement_ja: 2024年の日本では、心原性で一般市民に目撃された心肺機能停止の傷病者は27,769人で、1か月後の生存率は12.4%、社会復帰率は7.7%であった。一般市民がAEDで除細動を行った1,449人では、1か月後の生存率は53.6%、社会復帰率は44.4%であった。
    condition:
      region: 日本
      study: 消防庁 救急・救助の現況（令和6年中）
    differential: 一般市民による応急手当がなかった場合の1か月後社会復帰率は3.7%であった
    common_misconception: 目撃者の心肺蘇生やAEDは救命率にほとんど影響しない
  provenance:
    source_ref: SRC-212
    source: 総務省消防庁. 令和7年版 消防白書 第2章第5節（救急体制）：令和6年中の心肺機能停止傷病者の救命率
    doi: null
    pmid: null
    pmcid: null
    url: https://www.fdma.go.jp/publication/hakusho/r7/chapter2/section5/69383.html
    source_license: 政府機関ウェブサイト（ページ表示は Copyright© Fire and Disaster Management Agency。利用規約の本文は未確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-171 (id: JlvnltA)'
    kokushi: 医学各論 Ⅴ-5-B-②（心臓性突然死、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-026
  domain: IH
  subdomain: 川崎病
  assertion:
    plain_statement_ja: 川崎病の急性期（発症30日未満）の冠動脈病変は、心エコーで測ったZスコアで分類し、2.5以上5未満を小動脈瘤、5以上10未満を中等瘤、10以上を巨大瘤とする。実測値では内径8 mm以上を巨大瘤とする。5歳以上ではZスコアによる判定を優先する。
    condition:
      guideline: JCS/JSCS 2020 川崎病心臓血管後遺症GL
      region: 日本
    differential: 急性期に内径が6 mmを超えると遠隔期に狭窄性病変が増えると報告されている
    common_misconception: 冠動脈病変の大きさは年齢によらず実測値だけで判定する
  provenance:
    source_ref: SRC-213
    source: Fukazawa R, Kobayashi J, Ayusawa M, et al. JCS/JSCS 2020 Guideline on Diagnosis and Management of Cardiovascular Sequelae in Kawasaki Disease. Circ J 2020;84:1348-1407
    doi: 10.1253/circj.CJ-19-1094
    pmid: '32641591'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-1094
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-03 (id: JkxnuQo)；PS-02-06-05 (id: JkxnuQw)；TBL-02-05-027 (id: JlAKpf4)'
    kokushi: 医学各論 Ⅴ-5-E（川崎病、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-027
  domain: IH
  subdomain: 川崎病
  assertion:
    plain_statement_ja: 川崎病の急性期にはアスピリン30〜50 mg/kg/日を分3で投与し、解熱後に3〜5 mg/kg/日に減量して発症後2〜3か月続ける（クラスI、レベルC）。冠動脈瘤が残る場合は低用量アスピリンを続け（I、C）、巨大瘤・心筋梗塞の既往・瘤内血栓がある場合はワルファリン（PT-INR 2.0〜2.5）を併用する（IIa、C）。
    condition:
      guideline: JCS/JSCS 2020 川崎病心臓血管後遺症GL
      region: 日本
    differential: null
    common_misconception: 冠動脈病変が残っても抗血小板薬は2〜3か月でやめる
  provenance:
    source_ref: SRC-213
    source: Fukazawa R, Kobayashi J, Ayusawa M, et al. JCS/JSCS 2020 Guideline on Diagnosis and Management of Cardiovascular Sequelae in Kawasaki Disease. Circ J 2020;84:1348-1407
    doi: 10.1253/circj.CJ-19-1094
    pmid: '32641591'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-19-1094
    source_license: © 日本循環器学会（J-STAGE 掲載ページの表示。CC の表示なし。Crossref に license 欄なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-5-E（川崎病、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-028
  domain: IH
  subdomain: 川崎病
  assertion:
    plain_statement_ja: 重症の川崎病患者248人を対象とした日本のRAISE試験では、免疫グロブリン（2 g/kg）とアスピリンにプレドニゾロン（2 mg/kg/日）を加えると、冠動脈病変が23%から3%に減った。
    condition:
      region: 日本
      study: RAISE
    differential: null
    common_misconception: 川崎病にステロイドを使うと冠動脈瘤が増える
  provenance:
    source_ref: SRC-214
    source: Kobayashi T, Saji T, Otani T, et al. Efficacy of immunoglobulin plus prednisolone for prevention of coronary artery abnormalities in severe Kawasaki disease (RAISE study). Lancet 2012;379:1613-1620
    doi: 10.1016/S0140-6736(11)61930-2
    pmid: '22405251'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(11)61930-2
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 重症（不応予測）の判定基準は抄録に詳しい記載がない。
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-5-E（川崎病、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-029
  domain: IH
  subdomain: 川崎病
  assertion:
    plain_statement_ja: 免疫グロブリン不応が予測される川崎病患者175人を対象とした日本のKAICA試験では、免疫グロブリンにシクロスポリン（5 mg/kg/日、5日間）を加えると、12週までの冠動脈病変が31%から14%に減った（リスク比0.46）。有害事象に差はなかった。
    condition:
      region: 日本
      study: KAICA
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-215
    source: Hamada H, Suzuki H, Onouchi Y, et al. Efficacy of primary treatment with immunoglobulin plus ciclosporin for prevention of coronary artery abnormalities in patients with Kawasaki disease predicted to be at increased risk of non-response to intravenous immunoglobulin (KAICA). Lancet 2019;393:1128-1137
    doi: 10.1016/S0140-6736(18)32003-8
    pmid: '30853151'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(18)32003-8
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-04 (id: JkxnuQs)；PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-5-E（川崎病、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
- id: IH-030
  domain: IH
  subdomain: 川崎病
  assertion:
    plain_statement_ja: 日本の第27回川崎病全国調査（2021〜2022年）では患者は21,930人で、約20%が不全型、ほぼ全員が免疫グロブリンで治療され、そのうち約25%が不応であった。発症1か月後の心後遺症は2.3%であった。
    condition:
      region: 日本
      study: 第27回川崎病全国調査
    differential: null
    common_misconception: 川崎病は日本ではほとんどみられなくなった
  provenance:
    source_ref: SRC-216
    source: 'Nakamura Y, Yashiro M, Yanagawa H, et al. Epidemiology of Kawasaki disease in Japan in 2021-2022: Results of the 27th nationwide survey. Pediatr Int 2025;67:e70007'
    doi: 10.1111/ped.70007
    pmid: '40189891'
    pmcid: null
    url: https://doi.org/10.1111/ped.70007
    source_license: Wiley の利用規約（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)'
    kokushi: 医学各論 Ⅴ-5-E（川崎病、a）
  publication_info:
    created: '2026-10-25'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応

出題基準は第6節の表（医学各論 Ⅴ）、コアカリは第4層 PS-02-06 と別表1（TBL-01）・別表2-5（TBL-02-05）から選びました。

| カードID | subdomain | 出題基準 | コアカリ |
|---|---|---|---|
| AR-001 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-002 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-003 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-004 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-005 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-006 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-007 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-008 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-009 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-010 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-011 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-012 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-013 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-014 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-015 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-016 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg) |
| AR-017 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)；TBL-02-05-032 (id: JlAKpgM) |
| AR-018 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)；TBL-02-05-032 (id: JlAKpgM) |
| AR-019 | 心房細動 | 医学各論 Ⅴ-1-A-⑤（心房細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-166 (id: Jlvnlsg)；TBL-01-00-159 (id: Jlvnlr4)；TBL-02-05-032 (id: JlAKpgM) |
| AR-020 | 心房粗動 | 医学各論 Ⅴ-1-A-④（心房粗動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-167 (id: Jlvnlso)；TBL-02-05-032 (id: JlAKpgM) |
| AR-021 | 発作性上室頻拍 | 医学各論 Ⅴ-1-A-②（発作性上室頻拍、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-168 (id: Jlvnlsw) |
| AR-022 | WPW症候群 | 医学各論 Ⅴ-1-A-③（WPW症候群、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-173 (id: JlvnltU)；TBL-02-05-032 (id: JlAKpgM) |
| AR-023 | WPW症候群 | 医学各論 Ⅴ-1-A-③（WPW症候群、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-173 (id: JlvnltU) |
| AR-024 | 心室期外収縮 | 医学各論 Ⅴ-1-B-①（心室期外収縮、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-172 (id: JlvnltI) |
| AR-025 | 心室期外収縮 | 医学各論 Ⅴ-1-B-①（心室期外収縮、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-172 (id: JlvnltI)；TBL-01-00-163 (id: JlvnlsQ) |
| AR-026 | 心室頻拍 | 医学各論 Ⅴ-1-B-②（心室頻拍、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-169 (id: Jlvnls0)；TBL-02-05-032 (id: JlAKpgM) |
| AR-027 | 心室細動 | 医学各論 Ⅴ-1-B-③（心室細動、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-171 (id: JlvnltA)；TBL-02-05-032 (id: JlAKpgM) |
| AR-028 | 致死性不整脈 | 医学各論 Ⅴ-1-D-③（致死性不整脈、b） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-171 (id: JlvnltA)；TBL-02-05-032 (id: JlAKpgM) |
| AR-029 | 致死性不整脈 | 医学各論 Ⅴ-1-D-③（致死性不整脈、b） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-032 (id: JlAKpgM) |
| AR-030 | 洞不全症候群 | 医学各論 Ⅴ-1-C-①（洞不全症候群、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-164 (id: JlvnlsU)；TBL-02-05-032 (id: JlAKpgM) |
| AR-031 | 房室ブロック | 医学各論 Ⅴ-1-C-②（房室ブロック、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-165 (id: Jlvnlsc)；TBL-02-05-032 (id: JlAKpgM) |
| AR-032 | QT延長症候群 | 医学各論 Ⅴ-1-D-①（QT延長症候群、b） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-170 (id: Jlvnls8)；TBL-02-05-026 (id: JlAKpf0) |
| AR-033 | QT延長症候群 | 医学各論 Ⅴ-1-D-①（QT延長症候群、b） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-170 (id: Jlvnls8)；TBL-02-05-026 (id: JlAKpf0) |
| AR-034 | Brugada症候群 | 医学各論 Ⅴ-1-D-②（Brugada症候群、b） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-174 (id: Jlvnltc)；TBL-02-05-026 (id: JlAKpf0) |
| AR-035 | Brugada症候群 | 医学各論 Ⅴ-1-D-②（Brugada症候群、b） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-174 (id: Jlvnltc)；TBL-02-05-032 (id: JlAKpgM) |
| HF-001 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-159 (id: Jlvnlr4) |
| HF-002 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-159 (id: Jlvnlr4) |
| HF-003 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-159 (id: Jlvnlr4) |
| HF-004 | 慢性心不全 | 医学各論 Ⅴ-2-A-③（急性心不全、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-158 (id: Jlvnlrw) |
| HF-005 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-159 (id: Jlvnlr4) |
| HF-006 | 急性心不全 | 医学各論 Ⅴ-2-A-③（急性心不全、a） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-158 (id: Jlvnlrw)；TBL-02-05-020 (id: JlAKpfU) |
| HF-007 | 急性心不全 | 医学各論 Ⅴ-2-A-③（急性心不全、a） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-158 (id: Jlvnlrw)；TBL-02-05-020 (id: JlAKpfU) |
| HF-008 | 急性心不全 | 医学各論 Ⅴ-2-A-③（急性心不全、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-158 (id: Jlvnlrw) |
| HF-009 | 急性心不全 | 医学各論 Ⅴ-2-A-③（急性心不全、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-158 (id: Jlvnlrw) |
| HF-010 | 急性心不全 | 医学各論 Ⅴ-2-A-③（急性心不全、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-158 (id: Jlvnlrw) |
| HF-011 | 急性心不全 | 医学各論 Ⅴ-2-A-③（急性心不全、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-158 (id: Jlvnlrw)；TBL-02-05-020 (id: JlAKpfU) |
| HF-012 | 急性心不全 | 医学各論 Ⅴ-2-A-③（急性心不全、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-158 (id: Jlvnlrw) |
| HF-013 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4) |
| HF-014 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4) |
| HF-015 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4) |
| HF-016 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4) |
| HF-017 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4) |
| HF-018 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4) |
| HF-019 | 慢性心不全 | 医学各論 Ⅴ-2-A-④（慢性心不全、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-159 (id: Jlvnlr4)；TBL-02-05-032 (id: JlAKpgM) |
| HF-020 | 心原性ショック | 医学各論 Ⅴ-2-B（心原性ショック、a） | PS-02-06-04 (id: JkxnuQs)；TBL-02-05-030 (id: JlAKpgE) |
| HF-021 | 心原性ショック | 医学各論 Ⅴ-2-B（心原性ショック、a） | PS-02-06-05 (id: JkxnuQw) |
| HF-022 | 心原性ショック | 医学各論 Ⅴ-2-B（心原性ショック、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI) |
| HF-023 | 心原性ショック | 医学各論 Ⅴ-2-B（心原性ショック、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ) |
| HF-024 | 心原性ショック | 医学各論 Ⅴ-2-B（心原性ショック、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI) |
| HF-025 | 心原性ショック | 医学各論 Ⅴ-2-B（心原性ショック、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ) |
| IH-001 | 労作性狭心症 | 医学各論 Ⅴ-5-A-①（労作性狭心症、a） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-029 (id: JlAKpgA)；TBL-02-05-028 (id: JlAKpf8) |
| IH-002 | 労作性狭心症 | 医学各論 Ⅴ-5-A-①（労作性狭心症、a） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-030 (id: JlAKpgE)；TBL-02-05-031 (id: JlAKpgI) |
| IH-003 | 労作性狭心症 | 医学各論 Ⅴ-5-A-①（労作性狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-031 (id: JlAKpgI) |
| IH-004 | 労作性狭心症 | 医学各論 Ⅴ-5-A-①（労作性狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-031 (id: JlAKpgI) |
| IH-005 | 労作性狭心症 | 医学各論 Ⅴ-5-A-①（労作性狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-031 (id: JlAKpgI) |
| IH-006 | 冠攣縮性狭心症 | 医学各論 Ⅴ-5-A-②（冠攣縮性狭心症、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-161 (id: JlvnlsE) |
| IH-007 | 冠攣縮性狭心症 | 医学各論 Ⅴ-5-A-②（冠攣縮性狭心症、a） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-161 (id: JlvnlsE)；TBL-02-05-029 (id: JlAKpgA) |
| IH-008 | 冠攣縮性狭心症 | 医学各論 Ⅴ-5-A-②（冠攣縮性狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-161 (id: JlvnlsE) |
| IH-009 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-026 (id: JlAKpf0)；TBL-02-05-021 (id: JlAKpfI) |
| IH-010 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI) |
| IH-011 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI) |
| IH-012 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-01-00-157 (id: Jlvnlro) |
| IH-013 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-026 (id: JlAKpf0) |
| IH-014 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ) |
| IH-015 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ) |
| IH-016 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ) |
| IH-017 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI) |
| IH-018 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-02-05-031 (id: JlAKpgI) |
| IH-019 | 急性冠症候群 | 医学各論 Ⅴ-5-B-①（急性心筋梗塞（ST上昇型・非ST上昇型心筋梗塞）、不安定狭心症、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-162 (id: JlvnlsI)；TBL-01-00-163 (id: JlvnlsQ) |
| IH-020 | 陳旧性心筋梗塞 | 医学各論 Ⅴ-5-C（陳旧性心筋梗塞、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-01-00-166 (id: Jlvnlsg) |
| IH-021 | 陳旧性心筋梗塞 | 医学各論 Ⅴ-5-C（陳旧性心筋梗塞、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-01-00-166 (id: Jlvnlsg) |
| IH-022 | 陳旧性心筋梗塞 | 医学各論 Ⅴ-5-C（陳旧性心筋梗塞、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ) |
| IH-023 | 心臓性突然死 | 医学各論 Ⅴ-5-B-②（心臓性突然死、a） | PS-02-06-04 (id: JkxnuQs)；TBL-01-00-163 (id: JlvnlsQ)；TBL-01-00-171 (id: JlvnltA)；TBL-02-05-032 (id: JlAKpgM) |
| IH-024 | 無痛性虚血性心疾患 | 医学各論 Ⅴ-5-D（無痛性虚血性心疾患、a） | PS-02-06-03 (id: JkxnuQo)；TBL-01-00-160 (id: Jlvnlr8)；TBL-02-05-028 (id: JlAKpf8) |
| IH-025 | 心臓性突然死 | 医学各論 Ⅴ-5-B-②（心臓性突然死、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-171 (id: JlvnltA) |
| IH-026 | 川崎病 | 医学各論 Ⅴ-5-E（川崎病、a） | PS-02-06-03 (id: JkxnuQo)；PS-02-06-05 (id: JkxnuQw)；TBL-02-05-027 (id: JlAKpf4) |
| IH-027 | 川崎病 | 医学各論 Ⅴ-5-E（川崎病、a） | PS-02-06-04 (id: JkxnuQs)；PS-02-06-05 (id: JkxnuQw) |
| IH-028 | 川崎病 | 医学各論 Ⅴ-5-E（川崎病、a） | PS-02-06-04 (id: JkxnuQs)；PS-02-06-05 (id: JkxnuQw) |
| IH-029 | 川崎病 | 医学各論 Ⅴ-5-E（川崎病、a） | PS-02-06-04 (id: JkxnuQs)；PS-02-06-05 (id: JkxnuQw) |
| IH-030 | 川崎病 | 医学各論 Ⅴ-5-E（川崎病、a） | PS-02-06-05 (id: JkxnuQw) |

## 4. 未解決事項（担当の目安つき）

| # | 内容 | 担当の目安 |
|---|---|---|
| 1 | **心筋梗塞の第4版国際定義（Fourth Universal Definition, 2018）を使えなかった。** MIの病型（1〜5型）と、STEMI の心電図基準（連続2誘導のST上昇の閾値）のカードがありません。Circulation 版（DOI 10.1161/CIR.0000000000000617、PMID 30571511）は出版社サイトのボット確認で本文を開けず、EHJ 版（10.1093/eurheartj/ehy462）・JACC 版（10.1016/j.jacc.2018.08.1038）・Global Heart 版（10.1016/j.gheart.2018.08.004）はいずれも CC の表示がありません。PubMed には抄録がありません。本文を確認できる版で数値を照合してから追加してください。 | 補完回（調査チャット）＋人間（本文の入手） |
| 2 | SRC-186（Okura 2008、Circ J）と SRC-208（PRASFIT-ACS、Circ J 2014）は、Crossref に license 欄がなく、J-STAGE の掲載ページにもライセンスの表示がなかったため UNKNOWN にしました。 | Claude Code（Phase 3 の照合） |
| 3 | SRC-212（消防白書）は、ページの表示が「Copyright© Fire and Disaster Management Agency」で、利用規約の本文は未確認です。政府標準利用規約が適用されるかを確認してください。 | Claude Code または人間 |
| 4 | JCS ガイドライン（Circ J）の5件は Crossref に license 欄がなく、J-STAGE の表示で判定しました。Phase 3 で同じ判定になるか確認してください（2018〜2020年版は CC 表示なし、2022年以降は CC BY-NC-ND）。JCS/JHFS 2025 は J Card Fail にも同時掲載されています（DOI 10.1016/j.cardfail.2025.02.014、Elsevier、CC 表示なし）。 | Claude Code |
| 5 | 国内の承認・保険適用：エドキサバン15 mg の承認条件（AR-011・AR-012）、フィネレノンの心不全への適応（HF-017）、Impella の保険適用の条件（HF-025）は未確認です。 | 専門医（監修時） |
| 6 | 川崎病（IH-026〜030）と心原性ショック（HF-020〜025）は、コアカリ別表1の循環器系に該当する疾患がないため、第4層 PS-02-06-05 だけを付けました。川崎病は他の臓器・小児の表に載っている可能性があります。 | 人間（コアカリ表の確認） |
| 7 | 出題基準の表は原本との照合前です（リポジトリの注記どおり）。本回の番号はすべて第6節の表から選んでいます。 | Claude Code |
| 8 | HF-001 は JCS/JHFS 2025 の本文で確認した定義です。国際的な定義の原典（Bozkurt B, et al. J Card Fail 2021;27:387-413、DOI 10.1016/j.cardfail.2021.01.022、PMID 33663906、Elsevier）の本文は確認していません。 | 補完回 |
| 9 | 二次資料経由の数値が3件あります（HF-002 の HFpEF の割合、IH-002 の CVIT-DEFER、IH-008 の冠攣縮の頻度）。いずれもガイドラインが引用した研究の値で、原著では照合していません。 | 補完回 |

## 5. 次回への引き継ぎ

### 5-1. 欠番

- なし（AR-001〜035、HF-001〜025、IH-001〜030 は連番）。
- 作成したが、件数の上限（90件）に収めるため取り込み原本から外した主題：アブレーション時の左心耳閉鎖（JCS/JHRS 2021 非薬物治療フォーカスアップデート、IIb B）、AVNRT の遅伝導路アブレーション（2019年版 表58、I B）、心房粗動の抗凝固（2020年版 表55、I A）、NPPV の3CPO 試験、HFrEF のⅠc群薬禁忌とイバブラジン、拡張型心筋症の HFimpEF での薬の中止（III Harm）、冠攣縮性狭心症のアスピリン（III No benefit）とICD、SAVE 試験、日本の公共AED研究（Kitamura 2010）。補完回で追加できます（出典は 5-3 に記載）。

### 5-2. 重複を避ける範囲（第9・10回と補完回）

- **第9回 VD**：AR-008 で「中等度以上の僧帽弁狭窄症・機械弁を伴う心房細動にはワルファリン」を扱いました。弁膜症側では抗凝固薬の選択を繰り返さず、弁膜症そのものを扱ってください。
- **第9回 MP**：心サルコイドーシスの ICD（JCS/JHRS 2024 表4）、心アミロイドーシスの薬（JCS/JHFS 2025 表8）、HFpEF の原因検索は扱っていません。MP で扱ってください。たこつぼ心筋症は AR-033 で「後天性QT延長の原因の1つ」として名前だけ出しています。
- **第10回 CX**：心電図の基本所見のうち、Brugada 型心電図（AR-034）、QT延長の診断基準（AR-032）、右室梗塞・後壁梗塞の誘導（IH-013）は扱い済みです。心臓リハビリテーション、心不全の死亡数などの人口動態統計、主要循環器薬の一般的な作用は扱っていません。BNP・NT-proBNP のカットオフは HF-005〜007 で扱い済みです。
- **第10回 HT**：高血圧の治療目標は扱っていません。HF の降圧に関する推奨（JCS/JHFS 2025）も扱っていません。
- **第10回 VS**：深部静脈血栓症の予防（急性心不全入院時の VTE 予防の推奨）は扱っていません。
- **消化器との境界**：抗血栓療法による消化管出血の扱いは UG・IN・XS で扱い済みのため、本回は抗血栓薬の適応・選択・期間に限りました（DOAC と消化管出血の関係は AR-010 の数値のみ）。

### 5-3. 扱った出典と、確認済みで未使用の出典

- 使用：SRC-170〜216（第1節の表）。
- 確認済み・未使用（識別子は PubMed と Crossref で確認済み。補完回で使う場合は新しい SRC 番号を付ける）：
  - JCS/JHRS 2021 Guideline Focused Update on Non-Pharmacotherapy of Cardiac Arrhythmias. J Arrhythm 2022;38:1-30（DOI 10.1002/joa3.12649、PMID 35222748、PMC8851582、CC BY-NC-ND 4.0）
  - JCS/JHRS 2022 Guideline on Diagnosis and Risk Assessment of Arrhythmia. J Arrhythm 2024;40:655-752（DOI 10.1002/joa3.13052、PMID 39139890、PMC11317726、Wiley の利用規約）／Circ J 2024;88:1509-1595（DOI 10.1253/circj.CJ-22-0827、PMID 37690816）
  - RACE II：N Engl J Med 2010;362:1363-1373（DOI 10.1056/NEJMoa1001337、PMID 20231232）
  - SCD-HeFT：N Engl J Med 2005;352:225-237（DOI 10.1056/NEJMoa043399、PMID 15659722）
  - Brugada P, Brugada J. J Am Coll Cardiol 1992;20:1391-1396（DOI 10.1016/0735-1097(92)90253-J、PMID 1309182）
  - Jackman WM, et al. N Engl J Med 1991;324:1605-1611（WPW の高周波アブレーション、DOI 10.1056/NEJM199106063242301、PMID 2030716）
  - EMPEROR-Reduced：N Engl J Med 2020;383:1413-1424（DOI 10.1056/NEJMoa2022190、PMID 32865377）
  - CONSENSUS：N Engl J Med 1987;316:1429-1435（DOI 10.1056/NEJM198706043162301、PMID 2883575）
  - DOSE：N Engl J Med 2011;364:797-805（DOI 10.1056/NEJMoa1005419、PMID 21366472）
  - 3CPO：N Engl J Med 2008;359:142-151（DOI 10.1056/NEJMoa0707992、PMID 18614781）
  - FAME：N Engl J Med 2009;360:213-224（DOI 10.1056/NEJMoa0807611、PMID 19144937）
  - Keeley EC, et al. Lancet 2003;361:13-20（プライマリーPCI 対 線溶療法のメタ解析、DOI 10.1016/S0140-6736(03)12113-7、PMID 12517460）
  - PLATO：N Engl J Med 2009;361:1045-1057（DOI 10.1056/NEJMoa0904327、PMID 19717846）
  - REDUCE-AMI：N Engl J Med 2024;390:1372-1381（DOI 10.1056/NEJMoa2401479、PMID 38587241）
  - SAVE：N Engl J Med 1992;327:669-677（DOI 10.1056/NEJM199209033271001、PMID 1386652）
  - Kitamura T, et al. N Engl J Med 2010;362:994-1004（日本の公共AED、DOI 10.1056/NEJMoa0906644、PMID 20237345）
  - Kobayashi T, et al. Circulation 2006;113:2606-2612（IVIG 不応予測スコア、DOI 10.1161/CIRCULATIONAHA.105.592865、PMID 16735679）
  - Newburger JW, et al. N Engl J Med 1991;324:1633-1639（IVIG 2 g/kg 単回、DOI 10.1056/NEJM199106063242305、PMID 1709446）
  - 川崎病全国調査 2023〜2024：JAMA Netw Open 2026;9:e2626910（DOI 10.1001/jamanetworkopen.2026.26910、PMID 42550508、PMC13439430。PMC の XML では CC BY-NC-ND）
  - 2024 ESC AF ガイドライン（Eur Heart J 2024;45:3314-3414、DOI 10.1093/eurheartj/ehae176、PMID 39210723、OUP の標準規約）、2022 AHA/ACC/HFSA 心不全ガイドライン（DOI 10.1161/CIR.0000000000001063、PMID 35363499）、2021 ESC 心不全ガイドライン（DOI 10.1093/eurheartj/ehab368、PMID 34447992）、2023 ESC ACS ガイドライン（DOI 10.1093/eurheartj/ehad191、PMID 37622654）：いずれも CC の表示なし。欧米の基準と比べるカードを作る場合の候補。
