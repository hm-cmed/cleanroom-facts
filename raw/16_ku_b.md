# 腎・泌尿器・生殖器 第16回：腎不全・水電解質・酸塩基平衡（KF-001〜040）と腎・泌尿器の横断項目（KX-001〜032）

- 作成日：2026-10-28
- 事実票：72件（KF 40件、KX 32件）。目標の60〜90件の範囲内。ID は接頭辞ごとに 001 からの連番で、欠番はない。全件 `status: draft`、`verifier: null`。
- カバー：KF の対象項目は Ⅷ-3 の全16項目（レベル a 13項目を含む）すべてにカードがある。KX は依頼文の方針どおり全件 `kokushi: null` とし、コアカリは別表2-8・2-9 と第4層の番号を付けた。
- 出典マスター：新規 SRC-631〜690 のうち 54件を使用。未使用は SRC-639、645〜648、670（番号は詰めていない）。うち SRC-639 と SRC-670 は、KDIGO 2024 CKD ガイドラインに割り当てられていたが、第15回で同じ文献が SRC-573 として登録済みだったため、既存番号への統合としてこちらで付け替えた（対象カード：KF-013、KF-016、KX-006、KX-009 は `source_ref: SRC-573`）。同じ出典を複数カードで使う場合は同じ SRC を再利用した。
- 第15回との重複回避：急性尿細管壊死は KT-009（原因中心）に対し、KF-006・007 は AKI の枠組み・バイオマーカー・回復に絞った。酸塩基平衡は代謝性の異常とアニオンギャップに絞った（呼吸性は呼吸器 RX で作成済み）。糖尿病は CKD の腎保護治療の範囲に限った。
- 検証（こちらで実施済み）：YAML の構文解析を通過。スキーマ検証は、接頭辞 KF・KX を検証用に加えた条件でエラー0（接頭辞の追加は取り込み側の作業）。`condition.region` は全72件に記載。DOI のある53件はすべて Crossref で解決し題名が一致、DOI・PMID の両方がある51組に不一致はなかった。DOI が null の出典は2件（SRC-653、SRC-665）、PMID が null の出典は2件（SRC-649、SRC-676）で、いずれも理由を出典表と各カードに明記した。
- 取り込み想定：YAML ブロックは1つで、アンカー・マージキー・脚注番号・`basis_tag`・仮IDは使っていない。主張文はすべて自作文である（legal_basis はすべて B）。

## 1. 抽出元ホワイトリスト（出典マスター、新規 SRC）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 使用カード |
|---|---|---|---|---|---|---|---|
| SRC-631 | Kellum JA, Lameire N; KDIGO AKI Guideline Work Group. Diagnosis, evaluation, and management of acute kidney injury: a KDIGO summary (Part 1). Crit Care. 2013;17(1):204 | 10.1186/cc11454 | 23394211 | CC BY（PMC 掲載ページの表示） | OPEN | PMC 本文（PMCID: PMC4057151）で定義・病期・評価・非透析管理を確認し、NCBI ID 変換で DOI・PMID・PMCID を照合 | KF-001, KF-002, KF-003 |
| SRC-632 | Weisbord SD, Gallagher M, Jneid H, Garcia S, Cass A, Thwin SS, Conner TA, Chertow GM, Bhatt DL, Shunk K, Parikh CR, McFalls EO, Brophy M, Ferguson R, et al. Outcomes after Angiography with Sodium Bicarbonate and Acetylcysteine. N Engl J Med. 2018;378(7):603-614 | 10.1056/NEJMoa1710933 | 29130810 | 出版社の利用条件（Crossref の license 欄。CC の表示なし） | RESTRICTED | 抄録（Europe PMC レコード）で症例数・主要評価項目・造影剤関連 AKI の数値を確認し、Crossref と NCBI ID 変換で書誌・DOI・PMID を照合 | KF-004 |
| SRC-633 | STARRT-AKI Investigators. Timing of Initiation of Renal-Replacement Therapy in Acute Kidney Injury. N Engl J Med. 2020;383(3):240-251 | 10.1056/NEJMoa2000741 | 32668114 | 出版社の利用条件（Crossref の license 欄。CC の表示なし） | RESTRICTED | 抄録（Europe PMC レコード）で症例数・90日死亡・腎代替療法依存・有害事象の数値を確認し、Crossref と NCBI ID 変換で照合 | KF-005 |
| SRC-634 | VA/NIH Acute Renal Failure Trial Network; Palevsky PM, Zhang JH, O'Connor TZ, Chertow GM, Crowley ST, Choudhury D, Finkel K, Kellum JA, Paganini E, Schein RM, et al. Intensity of Renal Support in Critically Ill Patients with Acute Kidney Injury. N Engl J Med. 2008;359(1):7-20 | 10.1056/NEJMoa0802639 | 18492867 | 出版社の著作物（CC の表示なし） | RESTRICTED | 抄録（Europe PMC レコード）で症例数・60日死亡・腎機能回復の数値を確認し、NCBI ID 変換で DOI・PMID・PMCID（PMC2574780）を照合 | KF-006 |
| SRC-635 | Kashani K, Al-Khafaji A, Ardiles T, Artigas A, Bagshaw SM, Bell M, Bihorac A, Birkhahn R, Cely CM, Chawla LS, Davison DL, et al. Discovery and validation of cell cycle arrest biomarkers in human acute kidney injury. Crit Care. 2013;17(1):R25 | 10.1186/cc12503 | 23388612 | CC BY（BMC の Open Access 表示） | OPEN | 抄録（Europe PMC レコード）で Sapphire 研究の症例数・AUC を確認し、NCBI ID 変換で DOI・PMID・PMCID（PMC4057242）を照合 | KF-007 |
| SRC-636 | Chavez LO, Leon M, Einav S, Varon J. Beyond muscle destruction: a systematic review of rhabdomyolysis for clinical practice. Crit Care. 2016;20:135 | 10.1186/s13054-016-1314-5 | 27301374 | CC BY 4.0（出版社ページの Open Access 表示） | OPEN | PMC 本文（PMCID: PMC4908773）で AKI の機序と輸液療法の記載を確認し、抄録で定義（CK 基準）と無作為化試験の不在を確認。NCBI ID 変換で照合 | KF-008, KF-009 |
| SRC-637 | Tarr PI, Gordon CA, Chandler WL. Shiga-toxin-producing Escherichia coli and haemolytic uraemic syndrome. Lancet. 2005;365(9464):1073-1086 | 10.1016/S0140-6736(05)71144-2 | 15781103 | Elsevier の利用条件（Crossref の license 欄。CC の表示なし） | RESTRICTED | 抄録（Europe PMC レコード）で原因・禁忌とされる薬剤・支持療法の方針を確認し、Crossref と NCBI ID 変換で照合 | KF-010 |
| SRC-638 | Legendre CM, Licht C, Muus P, Greenbaum LA, Babu S, Bedrosian C, Bingham C, Cohen DJ, Delmas Y, Douglas K, Eitner F, Feldkamp T, Fouque D, Furman RR, et al. Terminal Complement Inhibitor Eculizumab in Atypical Hemolytic-Uremic Syndrome. N Engl J Med. 2013;368(23):2169-2181 | 10.1056/NEJMoa1208981 | 23738544 | 出版社の著作物（CC の表示なし） | RESTRICTED | 抄録（Europe PMC レコード）で疾患の定義づけと2試験の症例数・血小板数・透析離脱の数値を確認し、Crossref と NCBI ID 変換で照合 | KF-011, KF-012 |
| SRC-640 | Japanese Society of Nephrology. Essential points from Evidence-based Clinical Practice Guidelines for Chronic Kidney Disease 2018. Clin Exp Nephrol. 2019;23(1):1-15 | 10.1007/s10157-018-1648-1 | 30506489 | CC BY 4.0（PMC ページの表示。© The Author(s) 2018） | OPEN | PMC 本文（PMCID: PMC6344397）で CKD の定義・CGA 分類・日本人の eGFR 式・降圧目標の各ステートメントを確認し、NCBI ID 変換で照合 | KF-014, KF-017 |
| SRC-641 | Imai E, Horio M, Watanabe T, Iseki K, Yamagata K, Hara S, Ura N, Kiyohara Y, Moriyama T, Ando Y, Fujimoto S, Konta T, Yokoyama H, Makino H, Hishida A, et al. Prevalence of chronic kidney disease in the Japanese general population. Clin Exp Nephrol. 2009;13(6):621-630 | 10.1007/s10157-009-0199-x | 19513802 | 出版社の著作物（Springer の利用条件。CC の表示なし） | RESTRICTED | 抄録（Europe PMC レコード）で対象者数・病期別有病率・全国推計を確認し、Crossref と NCBI ID 変換で照合 | KF-015 |
| SRC-642 | The EMPA-KIDNEY Collaborative Group. Empagliflozin in Patients with Chronic Kidney Disease. N Engl J Med. 2023;388(2):135-146 | 10.1056/NEJMoa2204233 | 36331190 | 出版社の利用条件（Crossref の license 欄。CC の表示なし） | RESTRICTED | 抄録で症例数・主要評価項目・全入院の数値を確認し、NCBI ID 変換で DOI・PMID・PMCID（PMC7614055）を照合 | KF-018 |
| SRC-643 | Weir MR, Bakris GL, Bushinsky DA, Mayo MR, Garza D, Stasiv Y, Wittes J, Christ-Schmidt H, Berman L, Pitt B; OPAL-HK Investigators. Patiromer in Patients with Kidney Disease and Hyperkalemia Receiving RAAS Inhibitors. N Engl J Med. 2015;372(3):211-221 | 10.1056/NEJMoa1410853 | 25415805 | 出版社の著作物（CC の表示なし） | RESTRICTED | 抄録（Europe PMC レコード）で症例数・血清カリウムの変化・目標到達割合を確認し、Crossref と NCBI ID 変換で照合 | KF-019 |
| SRC-644 | Bakris GL, Agarwal R, Anker SD, Pitt B, Ruilope LM, Rossing P, Kolkhof P, Nowack C, Schloemer P, Joseph A, Filippatos G; FIDELIO-DKD Investigators. Effect of Finerenone on Chronic Kidney Disease Outcomes in Type 2 Diabetes. N Engl J Med. 2020;383(23):2219-2229 | 10.1056/NEJMoa2025845 | 33264825 | 出版社の利用条件（Crossref の license 欄。CC の表示なし） | RESTRICTED | 抄録（Europe PMC レコード）で症例数・主要腎複合・高カリウム血症の数値を確認し、Crossref と NCBI ID 変換で照合 | KF-020 |
| SRC-649 | Yamamoto H, Nishi S, Tomo T, et al. 2015 Japanese Society for Dialysis Therapy: Guidelines for Renal Anemia in Chronic Kidney Disease. Renal Replacement Therapy. 2017;3:36 | 10.1186/s41100-017-0114-y | null（PubMedで確認できず） | CC表示を本セッションで直接確認できず | UNKNOWN | 出版社ページでDOIと本文（治療開始基準・目標Hb）を確認。PMIDはPubMed検索で確認できなかったため null | KF-021, KF-022 |
| SRC-650 | Chen N, Hao C, Liu BC, et al. Roxadustat Treatment for Anemia in Patients Undergoing Long-Term Dialysis. N Engl J Med. 2019;381(11):1011–1022 | 10.1056/NEJMoa1901713 | 31340116 | © Massachusetts Medical Society（非CC） | RESTRICTED | PubMed抄録でDOI・PMID・主要結果を照合 | KF-023 |
| SRC-651 | KDIGO CKD-MBD Update Work Group. KDIGO 2017 Clinical Practice Guideline Update for the Diagnosis, Evaluation, Prevention, and Treatment of Chronic Kidney Disease–Mineral and Bone Disorder (CKD-MBD). Kidney Int Suppl. 2017;7(1):1–59 | 10.1016/j.kisu.2017.04.001 | 30675420 | CC BY-NC-ND 4.0 | RESTRICTED | PMC本文（PMCID: PMC6340919）でDOI・PMID・ライセンスを照合 | KF-024, KF-025 |
| SRC-652 | Fukagawa M, Yokoyama K, Koiwa F, et al. Clinical practice guideline for the management of chronic kidney disease-mineral and bone disorder. Ther Apher Dial. 2013;17(3):247–288 | 10.1111/1744-9987.12058 | 23735142 | © 日本透析医学会／Wiley（非CC） | RESTRICTED | PubMedでDOI・PMIDを照合。管理目標値は二次資料経由で確認 | KF-026 |
| SRC-653 | Kopeć J, Gadek A, Drożdż M, et al. Carpal tunnel syndrome in hemodialysis patients as a dialysis-related amyloidosis manifestation: incidence, risk factors and results of surgical treatment. Med Sci Monit. 2011;17(9):CR505–CR509 | null（確認できず） | 21873947 | CC BY-NC-ND 3.0 | RESTRICTED | PMC本文（PMCID: PMC3560521）でPMID・本文・ライセンスを確認。DOI文字列はPMC・出版社ページで確認できず null | KF-027 |
| SRC-654 | McGee S, Abernethy WB 3rd, Simel DL. The rational clinical examination. Is this patient hypovolemic? JAMA. 1999;281(11):1022–1029 | 10.1001/jama.281.11.1022 | 10086438 | © American Medical Association（非CC） | RESTRICTED | PubMed抄録でDOI・PMID・感度・特異度・尤度比を照合 | KF-028 |
| SRC-655 | Spasovski G, Vanholder R, Allolio B, et al. Clinical practice guideline on diagnosis and treatment of hyponatraemia. Eur J Endocrinol. 2014;170(3):G1–G47 | 10.1530/EJE-13-1020 | 24569125 | © European Society of Endocrinology（非CC） | RESTRICTED | PubMed抄録とガイドライン要約でDOI・PMID・定義・補正上限を照合 | KF-029, KF-031 |
| SRC-656 | Yun G, Baek SH, Kim S. Evaluation and management of hypernatremia in adults: clinical perspectives. Korean J Intern Med. 2023;38(3):290–302 | 10.3904/kjim.2022.346 | 36578134 | CC BY-NC 4.0 | RESTRICTED | PMC本文（PMCID: PMC10175862）で本文・ライセンスを確認し、DOIはDOAJでも照合 | KF-030 |
| SRC-657 | Clase CM, Carrero JJ, Ellison DH, et al. Potassium homeostasis and management of dyskalemia in kidney diseases: conclusions from a Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference. Kidney Int. 2020;97(1):42–61 | 10.1016/j.kint.2019.09.018 | 31706619 | © International Society of Nephrology／Elsevier（非CC） | RESTRICTED | PubMedでDOI・PMIDを照合し、緊急治療の記載は本文抜粋で確認 | KF-032 |
| SRC-658 | Kardalas E, Paschou SA, Anagnostis P, et al. Hypokalemia: a clinical update. Endocr Connect. 2018;7(4):R135–R146 | 10.1530/EC-18-0109 | 29540487 | CC BY-NC 4.0 | RESTRICTED | PMC（PMCID: PMC5881435）でDOI・PMID・ライセンスを照合 | KF-033 |
| SRC-659 | Walker MD, Shane E. Hypercalcemia: A Review. JAMA. 2022;328(16):1624–1636 | 10.1001/jama.2022.18331 | 36282253 | © American Medical Association（非CC） | RESTRICTED | PubMed抄録でDOI・PMID・頻度・重症度区分を照合 | KF-034 |
| SRC-660 | Cooper MS, Gittoes NJL. Diagnosis and management of hypocalcaemia. BMJ. 2008;336(7656):1298–1302 | 10.1136/bmj.39582.589433.BE | 18535072 | © BMJ Publishing Group（非CC） | RESTRICTED | PMC（PMCID: PMC2413335）とPubMedでDOI・PMID・要点を照合 | KF-035 |
| SRC-661 | Blaine J, Chonchol M, Levi M. Renal control of calcium, phosphate, and magnesium homeostasis. Clin J Am Soc Nephrol. 2015;10(7):1257–1272 | 10.2215/CJN.09750913 | 25287933 | ライセンス表示は未確認 | UNKNOWN | PubMed・PMC（PMCID: PMC4491294）でDOI・PMIDを照合。ライセンス表示は確認できず UNKNOWN | KF-036 |
| SRC-662 | de Baaij JHF, Hoenderop JGJ, Bindels RJM. Magnesium in man: implications for health and disease. Physiol Rev. 2015;95(1):1–46 | 10.1152/physrev.00012.2014 | 25540137 | © American Physiological Society（非CC） | RESTRICTED | PubMedでDOI・PMIDを照合 | KF-037 |
| SRC-663 | Kraut JA, Madias NE. Metabolic acidosis: pathophysiology, diagnosis and management. Nat Rev Nephrol. 2010;6(5):274–285 | 10.1038/nrneph.2010.33 | 20308999 | © Nature Publishing Group（非CC） | RESTRICTED | PubMed抄録でDOI・PMID・アニオンギャップの計算式と代償の予測を照合 | KF-038, KF-039 |
| SRC-664 | Do C, Vasquez PC, Soleimani M. Metabolic Alkalosis Pathogenesis, Diagnosis, and Treatment: Core Curriculum 2022. Am J Kidney Dis. 2022;80(4):536–551 | 10.1053/j.ajkd.2021.12.016 | 35525634 | © National Kidney Foundation／Elsevier（非CC） | RESTRICTED | PubMedでDOI・PMID・関連病態を照合 | KF-040 |
| SRC-665 | Trayes KP, Studdiford JS, Pickle S, Tully AS. Edema: diagnosis and management. Am Fam Physician. 2013;88(2):102-110 | null | 23939641 | 出版社（米国家庭医学会）の著作物（CC の表示なし） | RESTRICTED | PMID と抄録は PubMed 収載情報で確認。DOI は PubMed 収載頁・誌面のいずれでも付与を確認できなかったため null とした。鑑別の要点は公開全文で確認 | KX-001 |
| SRC-666 | Ostermann M, Joannidis M. Acute kidney injury 2016: diagnosis and diagnostic workup. Crit Care. 2016;20:299 | 10.1186/s13054-016-1478-z | 27670788 | CC BY 4.0（PMC ページの表示で確認） | OPEN | PMC 全文で KDIGO の診断基準・原因分類・初期精査の内容を確認し、書誌・DOI・PMID・PMCID（PMC5037640）を照合 | KX-002 |
| SRC-667 | Priya G, Kalra S, Dasgupta A, Grewal E. Diabetes insipidus: a pragmatic approach to management. Cureus. 2021;13(1):e12498 | 10.7759/cureus.12498 | 33425560 | CC BY 4.0（PMC ページの表示で確認） | OPEN | PMC 全文で多尿の目安・尿浸透圧・病型と鑑別の表を確認し、DOI は誌面表示と引用情報で、PMID・PMCID（PMC7785480）は PMC ページで照合 | KX-003 |
| SRC-668 | Hollingsworth JM, Wilt TJ. Lower urinary tract symptoms in men. BMJ. 2014;349:g4474 | 10.1136/bmj.g4474 | 25125424 | 出版社（BMJ）の著作物（CC の表示なし） | RESTRICTED | PMC 掲載ページで IPSS の解釈と症状分類を確認し、書誌・DOI・PMID・PMCID（PMC4688452）を照合 | KX-004 |
| SRC-669 | Gaggar P, Raju SB. Diagnostic utility of urine microscopy in kidney diseases. Indian J Nephrol. 2024;34(3):213-221 | 10.25259/ijn_362_23 | 39114391 | CC BY-NC-SA 4.0（PMC ページの表示で確認） | RESTRICTED | PMC 全文で円柱・細胞成分と疾患の対応表を確認し、書誌・DOI・PMID・PMCID（PMC11303840）を照合。DOI は誌面の引用形式表示でも確認 | KX-005, KX-007 |
| SRC-671 | Matsuo S, Imai E, Horio M, Yasuda Y, Tomita K, Nitta K, et al. Revised equations for estimated GFR from serum creatinine in Japan. Am J Kidney Dis. 2009;53(6):982-992 | 10.1053/j.ajkd.2008.12.034 | 19339088 | 出版社の著作物（CC の表示なし） | RESTRICTED | 書誌・DOI・PMID は複数の引用情報で照合。推算式と検証結果（バイアス、30%以内の正確度）は抄録で確認 | KX-008 |
| SRC-672 | Hogan JJ, Mocanu M, Berns JS. The native kidney biopsy: update and evidence for best practice. Clin J Am Soc Nephrol. 2016;11(2):354-362 | 10.2215/CJN.05750515 | 26339068 | 出版社（米国腎臓学会）の著作物（CC の表示なし） | RESTRICTED | PMC 全文で実施の考え方・相対的禁忌の表・合併症の頻度（メタ解析の表）を確認し、書誌・DOI・PMID・PMCID（PMC4741037）を照合 | KX-010 |
| SRC-673 | Brisbane W, Bailey MR, Sorensen MD. An overview of kidney stone imaging techniques. Nat Rev Urol. 2016;13(11):654-662 | 10.1038/nrurol.2016.154 | 27578040 | 出版社の著作物（著者原稿の PMC 掲載。CC の表示なし） | RESTRICTED | PMC 掲載ページで各画像検査の長所と短所を確認し、書誌・DOI・PMID・PMCID（PMC5443345）を照合 | KX-011 |
| SRC-674 | Watanabe Y, Yamagata K, Nishi S, Hirakata H, Maruyama S, Saito C, et al.; Japanese Society for Dialysis Therapy Clinical Guideline Work Group. Japanese Society for Dialysis Therapy clinical guideline for "hemodialysis initiation for maintenance hemodialysis". Ther Apher Dial. 2015;19 Suppl 1:93-107 | 10.1111/1744-9987.12293 | 25817934 | 学会（日本透析医学会）の著作物（CC の表示なし） | RESTRICTED | 書誌・DOI・PMID は引用情報で照合。導入時期のステートメント（GFR の値と推奨グレード）は抄録で確認 | KX-012 |
| SRC-675 | Wei Z, Jin Y, Cheng J, Han X, Liu J, Liu S. Chinese experience on comparison of clinical efficacy and safety of hemodialysis and peritoneal dialysis in the treatment of diabetic kidney failure: a systematic review and meta-analysis. Front Med (Lausanne). 2023;10:1116103 | 10.3389/fmed.2023.1116103 | 37636569 | CC BY 4.0（PMC ページの表示で確認） | OPEN | PMC 全文で対象・研究数・統合結果（オッズ比・標準化平均差）を確認し、書誌・DOI・PMID・PMCID（PMC10449255）を照合 | KX-013 |
| SRC-676 | Hanafusa N, Abe M, Joki N, Hoshino J, Taniguchi M, Kikuchi K, Hasegawa T, Goto S, Ogawa T, Kanda E, et al. Annual dialysis data report 2022, Japanese Society for Dialysis Therapy (JSDT) Renal Data Registry. Ren Replace Ther. 2025;11:54 | 10.1186/s41100-025-00646-3 | null | CC BY 4.0（BMC の誌面表示） | OPEN | 抄録で患者数・原疾患・死亡原因などの数値を確認し、DOI は誌面と引用情報で照合。PMID は PubMed・PMC の収載を確認できなかったため null とした | KX-014 |
| SRC-677 | Jha VK, Padmaprakash KV. Extracorporeal treatment in the management of acute poisoning: what an intensivist should know? Indian J Crit Care Med. 2018;22(12):862-869 | 10.4103/ijccm.IJCCM_425_18 | 30662226 | CC BY-NC-SA 4.0（PMC ページの表示で確認） | RESTRICTED | PMC 全文で体外除去の方式の比較と適応の考え方を確認し、書誌・DOI・PMID・PMCID（PMC6311976）を照合。DOI は誌面表示でも確認 | KX-015 |
| SRC-678 | Chou JA, Kalantar-Zadeh K, Mathew AT. A brief review of intradialytic hypotension with a focus on survival. Semin Dial. 2017;30(6):473-480 | 10.1111/sdi.12627 | 28661565 | 出版社の著作物（著者原稿の PMC 掲載。CC の表示なし） | RESTRICTED | PMC 掲載ページで透析中血圧低下の定義・除水速度との関連・危険因子を確認し、書誌・DOI・PMID・PMCID（PMC5738929）を照合 | KX-016 |
| SRC-679 | Shin HJ, Choi S, Kim S. Shared decision-making for kidney replacement therapy: a comprehensive review and a proposed model. Korean J Intern Med. 2025;40(6):890-908 | 10.3904/kjim.2025.019 | 41223871 | CC BY-NC 4.0（PMC ページの表示） | RESTRICTED | PMC 全文で抄録、6段階モデルの表（血液透析・腹膜透析・移植・保存的療法を比較する手順）、ライセンス表示を確認し、書誌・DOI・PMID・PMCID（PMC12611495）を照合 | KX-017 |
| SRC-680 | Buur LE, Madsen JK, Eidemak I, Krarup E, Lauridsen TG, Taasti LH, Finderup J. Does conservative kidney management offer a quantity or quality of life benefit compared to dialysis? A systematic review. BMC Nephrol. 2021;22:307 | 10.1186/s12882-021-02516-6 | 34507554 | CC BY 4.0（PMC ページの Open Access 表示） | OPEN | PMC 全文で抄録（対象研究25件、統合ハザード比、80歳以上・併存症での結果）とライセンス表示を確認し、書誌・DOI・PMID・PMCID（PMC8434727）を照合。本レビューの対象研究には Murtagh ら 2007年（75歳超、保存的管理77例・透析52例）を含む | KX-018, KX-032 |
| SRC-681 | Lok CE, Huber TS, Lee T, Shenoy S, Yevzlin AS, Abreo K, Allon M, Asif A, Astor BC, Glickman MH, Graham J, Moist LM, Rajan DK, Roberts C, Vachharajani TJ, Valentini RP; National Kidney Foundation. KDOQI Clinical Practice Guideline for Vascular Access: 2019 Update. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164 | 10.1053/j.ajkd.2019.12.001 | 32778223 | 学会ガイドライン（CC の表示なし） | RESTRICTED | ガイドライン本文（PDF）で抄録、ESKD Life-Plan の定義、成熟不全の定義（作製後6か月）、感染した動静脈アクセスへの対応を確認。書誌・DOI・PMID は PubMed 収載情報と照合。PMCID は確認できず null | KX-019 |
| SRC-682 | Li PK, Chow KM, Cho Y, Fan S, Figueiredo AE, Harris T, Kanjanabuch T, Kim YL, Madero M, Malyszko J, Mehrotra R, Okpechi IG, Perl J, Piraino B, Runnegar N, Teitelbaum I, Wong JK, Yu X, Johnson DW. ISPD peritonitis guideline recommendations: 2022 update on prevention and treatment. Perit Dial Int. 2022;42(2):110-153 | 10.1177/08968608221080586 | 35264029 | CC BY-NC 4.0（Crossref の license 欄で確認） | RESTRICTED | PubMed 抄録で腹膜炎率の目標（0.40件/年以下、腹膜炎のない患者80%超/年）を確認し、ガイドライン本文で診断基準（3項目のうち2項目以上、排液白血球数・好中球割合）を確認。書誌・DOI・PMID を照合。PMCID は確認できず null | KX-020 |
| SRC-683 | Komaba H, Nakagawa Y, Koizumi M, Tomita Y, Nakamura M. Estimated Number of Prevalent Kidney Transplant Recipients in Japan From 1964 to 2023. Transpl Int. 2025;38:15732 | 10.3389/ti.2025.15732 | 41480389 | CC BY（誌面のオープンアクセス表示で確認） | OPEN | 収載レコードで DOI・PMID・PMCID を照合し、誌面全文で年間件数・累計件数（生体・献腎の内訳）・推計レシピエント数とライセンス表示を確認 | KX-021 |
| SRC-684 | Kidney Disease: Improving Global Outcomes (KDIGO) Transplant Work Group. KDIGO clinical practice guideline for the care of kidney transplant recipients. Am J Transplant. 2009;9 Suppl 3:S1-S155 | 10.1111/j.1600-6143.2009.02834.x | 19845597 | CC BY-NC-ND 4.0（Crossref の license 欄、version of record） | RESTRICTED | 抄録でガイドラインの対象と範囲を確認し、本文で導入療法・維持療法（第1〜2章）、急性拒絶反応の治療（第6章）、移植腎生検（第9章）の推奨文を確認。DOI・PMID は引用情報で照合 | KX-022, KX-023, KX-031 |
| SRC-685 | Hariharan S, Israni AK, Danovitch G. Long-Term Survival after Kidney Transplantation. N Engl J Med. 2021;385(8):729-743 | 10.1056/NEJMra2014530 | 34407344 | 出版社の著作物（CC の表示なし） | RESTRICTED | 収載レコードで DOI・PMID を照合（抄録は掲載なし）。本文で献腎移植の10年移植腎生存率・患者生存率と移植後管理の要点を確認 | KX-024 |
| SRC-686 | Matzke GR, Aronoff GR, Atkinson AJ Jr, Bennett WM, Decker BS, et al. Drug dosing consideration in patients with acute and chronic kidney disease—a clinical update from Kidney Disease: Improving Global Outcomes (KDIGO). Kidney Int. 2011;80(11):1122-1137 | 10.1038/ki.2011.322 | 21918498 | Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | 出版社の全文ページで抄録・段階的用量調整の表・血液透析時の推奨を確認し、書誌データベースの照合で DOI と PMID の対応を確認。PMC には収載なし | KX-025, KX-026 |
| SRC-687 | Ludwig U, Keller F. Prophylaxis of Contrast-Induced Nephrotoxicity. Biomed Res Int. 2014;2014:308316 | 10.1155/2014/308316 | 24812612 | CC BY 3.0（Crossref の license 欄と PMC 掲載ページの表示で確認） | OPEN | PMC 掲載ページで抄録・危険因子・予防のまとめ（腎毒性薬とメトホルミンの中止、造影剤の選択、補液）を確認し、書誌データベースの照合で DOI・PMID・PMCID の対応を確認 | KX-027 |
| SRC-688 | Fujikura T, Isobe S, Oikawa S, Ishigaki S, Katahashi N, et al. Comparison of seroconversion rates after hepatitis B vaccination in patients with advanced chronic kidney disease and those receiving maintenance hemodialysis. Clin Exp Nephrol. 2025;29(8):1045-1052 | 10.1007/s10157-025-02648-1 | 40035977 | Springer の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし） | RESTRICTED | PubMed 抄録で対象数・接種方法・抗体陽転率を確認し、書誌データベースの照合で DOI と PMID の対応を確認。PMC には収載なし | KX-028 |
| SRC-689 | Azegami T, Kounoue N, Sofue T, et al. Efficacy of pre-emptive kidney transplantation for adults with end-stage kidney disease: a systematic review and meta-analysis. Ren Fail. 2023;45(1):2169618 | 10.1080/0886022X.2023.2169618 | 36705051 | CC BY 4.0（誌面の表示、Crossref の license 欄でも CC BY 4.0 を確認） | OPEN | PMC 全文ページで書誌・PMID・PMCID・ライセンス表示と抄録（対象研究数と調整ハザード比）を確認し、DOI は Crossref レコードと照合 | KX-029 |
| SRC-690 | Takahashi K, Saito K, Takahara S, et al.; Japanese ABO-Incompatible Kidney Transplantation Committee. Excellent long-term outcome of ABO-incompatible living donor kidney transplantation in Japan. Am J Transplant. 2004;4(7):1089-1096 | 10.1111/j.1600-6143.2004.00464.x | 15196066 | CC BY-NC-ND 4.0（Crossref の license 欄、version of record） | RESTRICTED | 出版社ページで抄録（対象441例、患者・移植腎生着率）を確認し、DOI は Crossref レコードと引用文献リストで、PMID は PubMed 収載レコードで照合 | KX-030 |

## 2. 事実票 YAML

```yaml
- id: KF-001
  domain: KF
  subdomain: AKIの定義と病期分類
  assertion:
    plain_statement_ja: 急性腎障害（AKI）は、48時間以内の血清クレアチニン0.3 mg/dL以上の上昇、7日以内のベースラインの1.5倍以上の上昇、尿量0.5 mL/kg/時未満が6時間続くこと、のいずれかで定義される。病期はクレアチニンと尿量で決まり、ステージ1はクレアチニン1.5〜1.9倍（または0.3 mg/dL以上の上昇）か尿量0.5 mL/kg/時未満が6〜12時間、ステージ2はクレアチニン2.0〜2.9倍か尿量0.5 mL/kg/時未満が12時間以上、ステージ3はクレアチニン3倍以上か4.0 mg/dL以上への上昇か腎代替療法の開始、または尿量0.3 mL/kg/時未満が24時間以上か無尿12時間以上である。
    condition:
      region: 国際
      study: KDIGO 2012 AKIガイドラインの公式要約（Part 1）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-631
    source: 'Kellum JA, Lameire N; KDIGO AKI Guideline Work Group. Diagnosis, evaluation, and management of acute kidney injury: a KDIGO summary (Part 1). Crit Care. 2013;17(1):204'
    doi: 10.1186/cc11454
    pmid: '23394211'
    pmcid: PMC4057151
    url: https://doi.org/10.1186/cc11454
    source_license: CC BY（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 病期の基準値はガイドラインの表から読み取った。原典ガイドライン本体（Kidney Int Suppl. 2012;2:1-138、DOI 10.1038/kisup.2012.1）は PMC レコード（PMC4089581）に PMID の付与が確認できなかったため、本カードは DOI・PMID のそろった KDIGO 公式要約を出典とした。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q)'
    kokushi: 医学各論 Ⅷ-3-A-①（急性腎障害(腎前性・腎性・腎後性)、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-002
  domain: KF
  subdomain: AKIの原因分類と鑑別
  assertion:
    plain_statement_ja: AKI の原因は、腎血流の低下による腎前性、腎実質（糸球体・尿細管・間質・血管）の障害による腎性、尿路閉塞による腎後性の3つに大別される。評価では原因を速やかに特定すること、とくに可逆的な原因に注意することが求められ、病歴と身体所見に尿検査・血液検査・画像検査を組み合わせて鑑別を進め、原因と病期に基づいて管理する。
    condition:
      region: 国際
      study: KDIGO 2012 AKIガイドラインの公式要約（Part 1）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-631
    source: 'Kellum JA, Lameire N; KDIGO AKI Guideline Work Group. Diagnosis, evaluation, and management of acute kidney injury: a KDIGO summary (Part 1). Crit Care. 2013;17(1):204'
    doi: 10.1186/cc11454
    pmid: '23394211'
    pmcid: PMC4057151
    url: https://doi.org/10.1186/cc11454
    source_license: CC BY（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 尿中ナトリウム排泄分画など個別の鑑別指標の数値基準は、本要約では確認できなかったため本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q)'
    kokushi: 医学各論 Ⅷ-3-A-①（急性腎障害(腎前性・腎性・腎後性)、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-003
  domain: KF
  subdomain: AKIの予防と治療総論
  assertion:
    plain_statement_ja: AKI の予防と治療の柱は、リスクの評価と腎障害性の曝露の回避、原因の特定と治療、循環動態の是正、合併症の管理であり、透析を要しない管理の範囲で病期に応じて対応する。AKI のあとは、3か月時点で腎機能の回復、新規の慢性腎臓病の発症、既存の慢性腎臓病の悪化がないかを評価することがガイドラインで求められている。
    condition:
      region: 国際
      study: KDIGO 2012 AKIガイドラインの公式要約（Part 1）と同ガイドラインの推奨文
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-631
    source: 'Kellum JA, Lameire N; KDIGO AKI Guideline Work Group. Diagnosis, evaluation, and management of acute kidney injury: a KDIGO summary (Part 1). Crit Care. 2013;17(1):204'
    doi: 10.1186/cc11454
    pmid: '23394211'
    pmcid: PMC4057151
    url: https://doi.org/10.1186/cc11454
    source_license: CC BY（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 3か月時点の評価はガイドライン推奨文（2.3.4）の再掲で確認した。具体的な薬剤名は扱っておらず、国内の承認状況の注記は不要な範囲に限った。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q)'
    kokushi: 医学各論 Ⅷ-3-A-①（急性腎障害(腎前性・腎性・腎後性)、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-004
  domain: KF
  subdomain: 造影剤関連AKI
  assertion:
    plain_statement_ja: 血管造影を受ける腎合併症の高リスク患者4993例を解析した無作為化試験（PRESERVE、5177例を無作為化）では、90日時点の死亡・透析・クレアチニン50%以上の持続的上昇の複合は、炭酸水素ナトリウム静注群4.4%と生理食塩液群4.7%で差がなく（オッズ比0.93）、アセチルシステイン群4.6%とプラセボ群4.5%でも差がなかった（オッズ比1.02）。造影剤関連AKIの発生率にも両比較とも有意差はなく、周術期の炭酸水素ナトリウムとアセチルシステインに予防効果は示されなかった。
    condition:
      region: 国際
      study: PRESERVE試験（2×2要因無作為化試験）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-632
    source: 'Weisbord SD, Gallagher M, Jneid H, Garcia S, Cass A, Thwin SS, Conner TA, Chertow GM, Bhatt DL, Shunk K, Parikh CR, McFalls EO, Brophy M, Ferguson R, et al. Outcomes after Angiography with Sodium Bicarbonate and Acetylcysteine. N Engl J Med. 2018;378(7):603-614'
    doi: 10.1056/NEJMoa1710933
    pmid: '29130810'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1710933
    source_license: 出版社の利用条件（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬の名前が出るカードのため注記する。アセチルシステインと炭酸水素ナトリウムの造影剤関連AKI予防を目的とした使用について、国内の承認・保険適用の状況は未確認であり、取り込み側で添付文書による確認が必要。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q)'
    kokushi: 医学各論 Ⅷ-3-A-①（急性腎障害(腎前性・腎性・腎後性)、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-005
  domain: KF
  subdomain: AKIの腎代替療法の開始時期
  assertion:
    plain_statement_ja: 重症AKIの重症患者3019例を無作為化した試験（STARRT-AKI、解析2927例）では、適格判定から12時間以内に腎代替療法を始める加速戦略と、従来の適応が出るか72時間を超えて持続するまで開始を控える標準戦略とで、90日死亡は43.9%と43.7%で差がなかった（相対リスク1.00）。腎代替療法を受けた割合は加速群96.8%と標準群61.8%で、90日時点で生存していた患者の腎代替療法への依存は加速群10.4%と標準群6.0%であり、有害事象も加速群に多かった（23.0%対16.5%）。
    condition:
      region: 国際
      study: STARRT-AKI試験（15か国の多施設無作為化試験）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-633
    source: 'STARRT-AKI Investigators. Timing of Initiation of Renal-Replacement Therapy in Acute Kidney Injury. N Engl J Med. 2020;383(3):240-251'
    doi: 10.1056/NEJMoa2000741
    pmid: '32668114'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2000741
    source_license: 出版社の利用条件（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 緊急の腎代替療法適応がある患者や、すぐに回復すると見込まれた患者は本試験の対象外であり、開始を遅らせてよいという結論はその範囲に限られる。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q)'
    kokushi: 医学各論 Ⅷ-3-A-①（急性腎障害(腎前性・腎性・腎後性)、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-006
  domain: KF
  subdomain: 急性尿細管壊死
  assertion:
    plain_statement_ja: 腎代替療法を要する重症AKI（急性尿細管壊死を含む）で、腎臓以外の臓器不全か敗血症を伴う重症患者1124例では、60日死亡は腎代替療法を強化した群で53.6%、通常強度の群で51.5%と差がなく（オッズ比1.09）、腎機能の回復率にも差はなかった。透析を要するほどの重症の尿細管障害では死亡率が5割を超え、腎代替療法の強度を上げることは経過を変えない。
    condition:
      region: 米国
      study: VA/NIH Acute Renal Failure Trial Network の無作為化試験（重症患者）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-634
    source: 'VA/NIH Acute Renal Failure Trial Network; Palevsky PM, Zhang JH, O''Connor TZ, Chertow GM, Crowley ST, Choudhury D, Finkel K, Kellum JA, Paganini E, Schein RM, et al. Intensity of Renal Support in Critically Ill Patients with Acute Kidney Injury. N Engl J Med. 2008;359(1):7-20'
    doi: 10.1056/NEJMoa0802639
    pmid: '18492867'
    pmcid: PMC2574780
    url: https://doi.org/10.1056/NEJMoa0802639
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本試験の対象は急性尿細管壊死と確定した患者だけではなく、腎代替療法を要する重症AKI全体であり、数値はその集団のものである。第15回の尿細管・間質側のカードとは原因ではなく重症度と経過の面から区別した。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q)'
    kokushi: 医学各論 Ⅷ-3-A-②（急性尿細管壊死、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-007
  domain: KF
  subdomain: AKIのバイオマーカーと回復評価
  assertion:
    plain_statement_ja: 重症患者を対象とした Sapphire 研究（解析728例）では、中等症から重症のAKI（KDIGOステージ2〜3）が検体採取後12時間以内に14%に発生し、尿中の細胞周期停止マーカーである TIMP-2 と IGFBP7 の積は AUC 0.80（単独では0.76と0.79）を示して、既存のAKIマーカー（いずれも AUC 0.72以下）より優れていた（P<0.002）。この指標は臨床モデルに加えるとリスク層別化を改善し、重症化する患者を早期に選び出して経過観察と回復評価につなげる手がかりになる。
    condition:
      region: 国際
      study: Sapphire 研究（多施設観察研究、重症患者）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-635
    source: 'Kashani K, Al-Khafaji A, Ardiles T, Artigas A, Bagshaw SM, Bell M, Bihorac A, Birkhahn R, Cely CM, Chawla LS, Davison DL, et al. Discovery and validation of cell cycle arrest biomarkers in human acute kidney injury. Crit Care. 2013;17(1):R25'
    doi: 10.1186/cc12503
    pmid: '23388612'
    pmcid: PMC4057242
    url: https://doi.org/10.1186/cc12503
    source_license: CC BY（BMC の Open Access 表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 回復とフォローアップの具体的な方針（評価の間隔や急性腎臓病 AKD の病期）は本研究の対象外であり、本カードでは未確認。AKI 後の3か月評価は KF-003 に記載し、AKD の枠組みは未解決事項に残した。この検査の国内での承認・保険適用の状況も未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q)'
    kokushi: 医学各論 Ⅷ-3-A-②（急性尿細管壊死、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-008
  domain: KF
  subdomain: 横紋筋融解症
  assertion:
    plain_statement_ja: 横紋筋融解症は骨格筋の破壊により細胞内容が血中へ流出する症候群で、多くの研究ではクレアチンキナーゼが基準値上限の5倍を超えることが定義に使われている。腎障害の機序は複合的で、損傷した筋への体液の隔離による循環血液量の減少と腎血流の低下、ミオグロビンの直接の細胞毒性（分解で生じる遊離鉄の反応による活性酸素の産生と脂質過酸化）、代謝性アシドーシスで促進されるミオグロビン円柱による尿細管の閉塞が関与する。
    condition:
      region: 国際
      study: 系統的レビュー（2006〜2015年の文献）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-636
    source: 'Chavez LO, Leon M, Einav S, Varon J. Beyond muscle destruction: a systematic review of rhabdomyolysis for clinical practice. Crit Care. 2016;20:135'
    doi: 10.1186/s13054-016-1314-5
    pmid: '27301374'
    pmcid: PMC4908773
    url: https://doi.org/10.1186/s13054-016-1314-5
    source_license: CC BY 4.0（出版社ページの Open Access 表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 機序はレビュー本文で確認した。AKI の発症率には報告間で大きな幅があり、一次資料で確定できないため本カードには数値を入れていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-3-A-③（横紋筋融解症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-009
  domain: KF
  subdomain: 横紋筋融解症の治療
  assertion:
    plain_statement_ja: 横紋筋融解症の治療の中心は、早期に静脈内輸液で循環血液量を回復させ、尿量を確保してミオグロビンの排泄を促すことであり、輸液は筋損傷から6時間以内に始めることが望ましいとされ、尿量300 mL/時を目標とした整理がある。一方、輸液単独と、輸液への炭酸水素ナトリウムやマンニトールの追加とを比べた無作為化試験は行われておらず、追加療法の利益は確立していない。
    condition:
      region: 国際
      study: 系統的レビュー（2006〜2015年の文献）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-636
    source: 'Chavez LO, Leon M, Einav S, Varon J. Beyond muscle destruction: a systematic review of rhabdomyolysis for clinical practice. Crit Care. 2016;20:135'
    doi: 10.1186/s13054-016-1314-5
    pmid: '27301374'
    pmcid: PMC4908773
    url: https://doi.org/10.1186/s13054-016-1314-5
    source_license: CC BY 4.0（出版社ページの Open Access 表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 尿量300 mL/時の目標は、本レビューが引用した系統的レビューの値であり二次資料経由である。薬の名前が出るカードのため注記する。炭酸水素ナトリウムとマンニトールのこの目的での国内の承認・保険適用の状況は未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-3-A-③（横紋筋融解症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-010
  domain: KF
  subdomain: 溶血性尿毒症症候群
  assertion:
    plain_statement_ja: 下痢に伴う溶血性尿毒症症候群（HUS）の多くは志賀毒素産生性細菌が原因で、その中では大腸菌 O157:H7 が世界的に HUS との関連が最も強い。急性期の感染に対して抗菌薬、腸管運動を抑える薬、麻薬性鎮痛薬、非ステロイド性抗炎症薬は投与すべきではなく、入院のうえ静注輸液を行うことが勧められ、HUS 自体の管理は支持療法が中心で、経過を改善する特異的な治療はないとされる。
    condition:
      region: 国際
      study: 総説（志賀毒素産生性大腸菌と HUS）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-637
    source: 'Tarr PI, Gordon CA, Chandler WL. Shiga-toxin-producing Escherichia coli and haemolytic uraemic syndrome. Lancet. 2005;365(9464):1073-1086'
    doi: 10.1016/S0140-6736(05)71144-2
    pmid: '15781103'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(05)71144-2
    source_license: Elsevier の利用条件（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 感染後に HUS を発症する割合などの数値は総説の抄録では確認できなかったため、本カードには入れていない。内容は小児の下痢関連 HUS を中心とした総説に基づく。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-426 (id: JlvnmHQ)'
    kokushi: 医学各論 Ⅷ-3-A-④（溶血性尿毒症症候群<HUS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-011
  domain: KF
  subdomain: 非典型溶血性尿毒症症候群
  assertion:
    plain_statement_ja: 非典型溶血性尿毒症症候群は、補体が介在する血栓性微小血管症による、遺伝性の、生命を脅かす慢性の疾患である。血漿交換や血漿輸注は血液学的な指標を一時的に正常範囲に保ちうるが、全身性の基礎病態そのものを治療するものではない点が、志賀毒素産生性大腸菌による HUS と区別して理解する要点になる。
    condition:
      region: 国際
      study: エクリズマブの第2相試験2件の報告（背景の疾患定義）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-638
    source: 'Legendre CM, Licht C, Muus P, Greenbaum LA, Babu S, Bedrosian C, Bingham C, Cohen DJ, Delmas Y, Douglas K, Eitner F, Feldkamp T, Fouque D, Furman RR, et al. Terminal Complement Inhibitor Eculizumab in Atypical Hemolytic-Uremic Syndrome. N Engl J Med. 2013;368(23):2169-2181'
    doi: 10.1056/NEJMoa1208981
    pmid: '23738544'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1208981
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 補体制御因子の遺伝子（CFH、MCP/CD46、CFI など）ごとの頻度は、本試験の抄録では確認できなかったため本カードには入れていない。遺伝子別の頻度は総説での確認が取り込み側に残る。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-3-A-④（溶血性尿毒症症候群<HUS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-012
  domain: KF
  subdomain: 非典型溶血性尿毒症症候群の治療
  assertion:
    plain_statement_ja: 非典型溶血性尿毒症症候群に対する終末補体阻害薬エクリズマブの第2相試験2件では、12歳以上の計37例（血小板減少と腎障害のある17例と、血漿療法を続けていた20例）が投与を受け、血小板数が多い群では26週までに血小板数が平均で73×10^9/L増加し（P<0.001）、もう一方の群では80%が血栓性微小血管症イベントフリー（血小板数の25%を超える低下なし、血漿交換・輸注なし、透析の新規開始なし）に達した。透析を受けていた5例中4例が透析を離脱し、投与開始が早いほど推算GFRの改善が大きく、観察期間中に髄膜炎菌感染は認められなかった。
    condition:
      region: 国際
      study: 第2相試験2件（26週の投与と長期延長相）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-638
    source: 'Legendre CM, Licht C, Muus P, Greenbaum LA, Babu S, Bedrosian C, Bingham C, Cohen DJ, Delmas Y, Douglas K, Eitner F, Feldkamp T, Fouque D, Furman RR, et al. Terminal Complement Inhibitor Eculizumab in Atypical Hemolytic-Uremic Syndrome. N Engl J Med. 2013;368(23):2169-2181'
    doi: 10.1056/NEJMoa1208981
    pmid: '23738544'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1208981
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬の名前が出るカードのため注記する。エクリズマブの非典型溶血性尿毒症症候群に対する国内の承認・保険適用の状況は、本作成では添付文書で確認していないため未確認であり、取り込み側で PMDA の添付文書による確認が必要。投与量は抄録で確認した範囲を超えるため記載していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-3-A-④（溶血性尿毒症症候群<HUS>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-013
  domain: KF
  subdomain: 慢性腎臓病<CKD>
  assertion:
    plain_statement_ja: 慢性腎臓病（CKD）は、腎障害を示す所見か GFR 60 mL/min/1.73m2 未満のいずれかが3か月を超えて続く状態であり、重症度は原因（C）、GFR 区分（G）、アルブミン尿区分（A）の CGA で表す。GFR 区分は G1 が90以上、G2 が60〜89、G3a が45〜59、G3b が30〜44、G4 が15〜29、G5 が15未満（mL/min/1.73m2）、アルブミン尿区分は A1 が30 mg/g 未満、A2 が30〜300 mg/g、A3 が300 mg/g を超えるもので、GFR が低くアルブミン尿が多いほど腎不全と心血管イベントのリスクが高いことがヒートマップで示される。
    condition:
      region: 国際
      study: KDIGO 2024 CKDガイドライン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-573
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int. 2024;105(4S):S117-S314'
    doi: 10.1016/j.kint.2023.10.018
    pmid: '38490803'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2023.10.018
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: GFR 区分とアルブミン尿区分の数値はガイドラインの表から読み取った。日本の方式との違いは KF-014 に分けた。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-014
  domain: KF
  subdomain: 慢性腎臓病<CKD>（日本の方式）
  assertion:
    plain_statement_ja: 日本の診療では、CKD は腎障害の所見（血液・尿の異常、画像、病理）か GFR 60 mL/min/1.73m2 未満のいずれかが3か月を超えて続くことと定義され、とくに蛋白尿0.15 g/gCr 以上（アルブミン尿30 mg/gCr 以上）が重要な所見とされる。重症度は原因・GFR 区分・蛋白尿（アルブミン尿）による CGA 分類で評価することが推奨され、GFR の推算には日本人に合わせた式、eGFR = 194 × クレアチニン^-1.094 × 年齢^-0.287（女性は ×0.739）が用いられる。
    condition:
      region: 日本
      study: 日本腎臓学会 エビデンスに基づくCKD診療ガイドライン2018 の要旨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-640
    source: 'Japanese Society of Nephrology. Essential points from Evidence-based Clinical Practice Guidelines for Chronic Kidney Disease 2018. Clin Exp Nephrol. 2019;23(1):1-15'
    doi: 10.1007/s10157-018-1648-1
    pmid: '30506489'
    pmcid: PMC6344397
    url: https://doi.org/10.1007/s10157-018-1648-1
    source_license: CC BY 4.0（PMC ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 蛋白尿の閾値と eGFR の式はガイドライン要旨の本文から読み取った。本カードは2018年版に基づく。2023年版のガイドラインも公表されており、最新版との差異の確認は取り込み側に残る。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-015
  domain: KF
  subdomain: CKDの疫学
  assertion:
    plain_statement_ja: 2005年の日本の健診データ（20歳以上の574,024人、11都道府県）をもとに日本人の式で eGFR を算出した推計では、CKD の病期別有病率はステージ1が0.6%、ステージ2が1.7%、ステージ3が10.4%、ステージ4と5の合計が0.2%で、全国の患者数の推計はステージ3だけで1070万人に達した。CKD の大半は自覚症状に乏しいステージ3が占める。
    condition:
      region: 日本
      study: 2005年の健診受診者データに基づく横断的推計
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-641
    source: 'Imai E, Horio M, Watanabe T, Iseki K, Yamagata K, Hara S, Ura N, Kiyohara Y, Moriyama T, Ando Y, Fujimoto S, Konta T, Yokoyama H, Makino H, Hishida A, et al. Prevalence of chronic kidney disease in the Japanese general population. Clin Exp Nephrol. 2009;13(6):621-630'
    doi: 10.1007/s10157-009-0199-x
    pmid: '19513802'
    pmcid: null
    url: https://doi.org/10.1007/s10157-009-0199-x
    source_license: 出版社の著作物（Springer の利用条件。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2005年の健診受診者に基づく推計であり、現在の有病率そのものではない。蛋白尿は試験紙法で評価され、ステージ1と2の分類は全受診者では行われていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-016
  domain: KF
  subdomain: CKDの進行抑制
  assertion:
    plain_statement_ja: CKD の進行抑制は、原因疾患の治療を土台として、血圧の管理、レニン・アンギオテンシン系阻害薬や SGLT2 阻害薬などの腎保護的な薬物療法、血糖と脂質の管理、減塩や禁煙などの生活習慣の是正を、CGA 分類で評価したリスクの大きさに応じて組み合わせる包括的なアプローチで進め、モニタリングと専門医への紹介の要否もリスクに応じて判断する。
    condition:
      region: 国際
      study: KDIGO 2024 CKDガイドライン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-573
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int. 2024;105(4S):S117-S314'
    doi: 10.1016/j.kint.2023.10.018
    pmid: '38490803'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2023.10.018
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは進行抑制の枠組みのみを扱い、個別の薬剤の効果の数値は SGLT2 阻害薬（KF-018）、RAS 阻害と高カリウム管理（KF-019）、フィネレノン（KF-020）に分けた。各薬剤の国内の承認状況は各カードの注記に委ねる。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-017
  domain: KF
  subdomain: CKDの降圧目標
  assertion:
    plain_statement_ja: 日本のガイドラインでは、高血圧を伴う CKD の降圧目標は75歳未満では、糖尿病がある場合と、糖尿病がなく蛋白尿区分 A2 または A3 の場合は130/80 mmHg 未満、糖尿病がなく A1 の場合は140/90 mmHg 未満が推奨される。75歳以上では150/90 mmHg 未満が推奨され、降圧薬に忍容性があり有害事象がなければ140/90 mmHg 未満を目指す。いずれの年齢でも収縮期血圧を110 mmHg 未満に下げることは推奨されない。
    condition:
      region: 日本
      study: 日本腎臓学会 エビデンスに基づくCKD診療ガイドライン2018 の要旨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-640
    source: 'Japanese Society of Nephrology. Essential points from Evidence-based Clinical Practice Guidelines for Chronic Kidney Disease 2018. Clin Exp Nephrol. 2019;23(1):1-15'
    doi: 10.1007/s10157-018-1648-1
    pmid: '30506489'
    pmcid: PMC6344397
    url: https://doi.org/10.1007/s10157-018-1648-1
    source_license: CC BY 4.0（PMC ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 目標値はガイドライン本文のステートメントから読み取った。推奨のレベルとグレードは病期と蛋白尿区分の組み合わせで異なるため、個別の表記は本文に委ねる。2018年版に基づく。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-018
  domain: KF
  subdomain: SGLT2阻害薬（CKD）
  assertion:
    plain_statement_ja: SGLT2 阻害薬エンパグリフロジンを検討した EMPA-KIDNEY 試験では、eGFR が20以上45未満、または45以上90未満で尿中アルブミン・クレアチニン比200 mg/g 以上の CKD 患者6609例を無作為化し、中央値2.0年の追跡で、主要評価項目である腎疾患の進行か心血管死はエンパグリフロジン群13.1%（432/3304例）とプラセボ群16.9%（558/3305例）に発生した（ハザード比0.72）。効果は糖尿病の有無にかかわらず一貫し、全入院の発生率もエンパグリフロジン群で低かった（ハザード比0.86）。
    condition:
      region: 国際
      study: EMPA-KIDNEY試験（無作為化プラセボ対照試験）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-642
    source: 'The EMPA-KIDNEY Collaborative Group. Empagliflozin in Patients with Chronic Kidney Disease. N Engl J Med. 2023;388(2):135-146'
    doi: 10.1056/NEJMoa2204233
    pmid: '36331190'
    pmcid: PMC7614055
    url: https://doi.org/10.1056/NEJMoa2204233
    source_license: 出版社の利用条件（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬の名前が出るカードのため注記する。エンパグリフロジンの CKD に対する国内の承認・保険適用の状況は、本作成では添付文書で確認していないため未確認であり、取り込み側で PMDA の添付文書による確認が必要。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-019
  domain: KF
  subdomain: RAS阻害と高カリウム血症の管理
  assertion:
    plain_statement_ja: レニン・アンギオテンシン系阻害薬を使っている CKD 患者では高カリウム血症が阻害薬の継続を妨げる要因になるが、カリウム吸着薬パチロマーを検討した OPAL-HK 研究では、血清カリウム5.1以上6.5未満 mmol/L の237例で、4週間の投与により血清カリウムが平均1.01 mmol/L低下し、76%が目標域（3.8以上5.1未満 mmol/L）に達した。その後の離脱期では、パチロマーを続けた群よりプラセボに切り替えた群で血清カリウムの再上昇が大きかった。
    condition:
      region: 国際
      study: OPAL-HK研究（多施設前向き試験、初期治療期と無作為化離脱期）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-643
    source: 'Weir MR, Bakris GL, Bushinsky DA, Mayo MR, Garza D, Stasiv Y, Wittes J, Christ-Schmidt H, Berman L, Pitt B; OPAL-HK Investigators. Patiromer in Patients with Kidney Disease and Hyperkalemia Receiving RAAS Inhibitors. N Engl J Med. 2015;372(3):211-221'
    doi: 10.1056/NEJMoa1410853
    pmid: '25415805'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1410853
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬の名前が出るカードのため注記する。パチロマーの国内の承認・保険適用の状況は未確認であり、取り込み側で PMDA の添付文書による確認が必要。初期治療期は対照のない単群の評価であり、数値はその範囲のものである。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-020
  domain: KF
  subdomain: フィネレノン
  assertion:
    plain_statement_ja: 2型糖尿病を伴う CKD 患者5734例を、最大用量のレニン・アンギオテンシン系阻害薬に加えて非ステロイド性ミネラルコルチコイド受容体拮抗薬フィネレノンかプラセボに割り付けた FIDELIO-DKD 試験では、中央値2.6年の追跡で、主要腎複合評価項目（腎不全、eGFR の40%以上の持続的な低下、腎臓死）はフィネレノン群17.8%（504/2833例）とプラセボ群21.1%（600/2841例）に発生した（ハザード比0.82）。高カリウム血症はフィネレノン群に多く（18.3%対9.0%）、高カリウム血症による中止は2.3%と0.9%だった。
    condition:
      region: 国際
      study: FIDELIO-DKD試験（無作為化プラセボ対照試験）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-644
    source: 'Bakris GL, Agarwal R, Anker SD, Pitt B, Ruilope LM, Rossing P, Kolkhof P, Nowack C, Schloemer P, Joseph A, Filippatos G; FIDELIO-DKD Investigators. Effect of Finerenone on Chronic Kidney Disease Outcomes in Type 2 Diabetes. N Engl J Med. 2020;383(23):2219-2229'
    doi: 10.1056/NEJMoa2025845
    pmid: '33264825'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2025845
    source_license: 出版社の利用条件（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬の名前が出るカードのため注記する。フィネレノンの CKD に対する国内の承認・保険適用の状況は、本作成では添付文書で確認していないため未確認であり、取り込み側で PMDA の添付文書による確認が必要。本カードは糖尿病そのものではなく腎保護の追加治療に限った。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-021
  domain: KF
  subdomain: 腎性貧血
  assertion:
    plain_statement_ja: 腎性貧血は、慢性腎臓病の進行に伴って腎臓でのエリスロポエチン産生が低下して生じる貧血であり、診断にあたっては鉄欠乏をはじめとする他の貧血の原因を鑑別したうえで、慢性腎臓病に伴うものと判断する。鉄の状態はフェリチンとトランスフェリン飽和度で評価する。
    condition:
      region: 日本
      guideline: 日本透析医学会「慢性腎臓病患者における腎性貧血治療のガイドライン」2015年版
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-649
    source: "Yamamoto H, Nishi S, Tomo T, et al. 2015 Japanese Society for Dialysis Therapy: Guidelines for Renal Anemia in Chronic Kidney Disease. Renal Replacement Therapy. 2017;3:36"
    doi: 10.1186/s41100-017-0114-y
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s41100-017-0114-y
    source_license: CC表示を本セッションで直接確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 診断の参考となるヘモグロビン値の具体的な線引きは、出典（2015年版ガイドライン）の該当箇所を本セッションで確認できなかったため、主張文に数値を含めていない。出典論文のPMIDはPubMedで確認できず null とした。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-C-①（腎性貧血、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-022
  domain: KF
  subdomain: 腎性貧血
  assertion:
    plain_statement_ja: 腎性貧血の治療では、赤血球造血刺激因子製剤を用い、鉄欠乏があれば鉄を補充する。血液透析患者ではヘモグロビン10 g/dL未満で治療開始を検討し、維持目標は10〜12 g/dLとする。保存期および腹膜透析の患者では11 g/dL未満で開始を検討し、目標は11〜13 g/dLとするが、重篤な心血管合併症がある保存期患者では12 g/dLを超えた場合に減量や休薬を考慮する。
    condition:
      region: 日本
      guideline: 日本透析医学会「慢性腎臓病患者における腎性貧血治療のガイドライン」2015年版
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-649
    source: "Yamamoto H, Nishi S, Tomo T, et al. 2015 Japanese Society for Dialysis Therapy: Guidelines for Renal Anemia in Chronic Kidney Disease. Renal Replacement Therapy. 2017;3:36"
    doi: 10.1186/s41100-017-0114-y
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s41100-017-0114-y
    source_license: CC表示を本セッションで直接確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 薬剤（赤血球造血刺激因子製剤・鉄剤）の国内の承認・保険適用の詳細は、本セッションでは添付文書で確認していない（出典は日本の診療を前提とする国内ガイドラインである）。出典論文のPMIDはPubMedで確認できず null とした。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-C-①（腎性貧血、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-023
  domain: KF
  subdomain: 腎性貧血
  assertion:
    plain_statement_ja: 低酸素誘導因子プロリン水酸化酵素（HIF-PH）阻害薬のロキサデュスタットは、経口でエリスロポエチン産生を促す腎性貧血治療薬である。中国の長期透析患者305例を対象とした第III相試験では、投与23〜27週のヘモグロビン変化量はロキサデュスタット群で平均+0.7 g/dL、エポエチンアルファ群で平均+0.5 g/dLであり、群間差0.2 g/dL（95%信頼区間 −0.02〜0.5）で非劣性（非劣性マージン −1.0 g/dL）が示された。高カリウム血症と上気道感染はロキサデュスタット群に、高血圧はエポエチンアルファ群に多かった。
    condition:
      region: 国際
      population: 中国の長期透析患者を対象とした第III相ランダム化比較試験
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-650
    source: "Chen N, Hao C, Liu BC, et al. Roxadustat Treatment for Anemia in Patients Undergoing Long-Term Dialysis. N Engl J Med. 2019;381(11):1011–1022"
    doi: 10.1056/NEJMoa1901713
    pmid: '31340116'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1901713
    source_license: © Massachusetts Medical Society（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は中国の透析患者を対象とした単一試験の結果であり、日本人患者への外挿には注意が要る。ロキサデュスタットほかHIF-PH阻害薬の国内の承認・保険適用の状況は、本セッションではPMDAや添付文書で確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-C-①（腎性貧血、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-024
  domain: KF
  subdomain: CKD-MBD
  assertion:
    plain_statement_ja: CKD-MBDは慢性腎臓病に伴うミネラル・骨代謝の全身性障害であり、カルシウム・リン・副甲状腺ホルモン・ビタミンD代謝の異常、骨の代謝回転や石灰化の異常、血管など軟部組織の石灰化のいずれか、またはその組み合わせとして現れる。KDIGOのガイドラインでは、CKDのステージG3aから血清カルシウム、リン、副甲状腺ホルモン、アルカリホスファターゼのモニタリングを始めることが提案されている。
    condition:
      region: 国際
      population: CKDステージG3a〜G5D
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-651
    source: "KDIGO CKD-MBD Update Work Group. KDIGO 2017 Clinical Practice Guideline Update for the Diagnosis, Evaluation, Prevention, and Treatment of Chronic Kidney Disease–Mineral and Bone Disorder (CKD-MBD). Kidney Int Suppl. 2017;7(1):1–59"
    doi: 10.1016/j.kisu.2017.04.001
    pmid: '30675420'
    pmcid: PMC6340919
    url: https://doi.org/10.1016/j.kisu.2017.04.001
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: モニタリングの間隔（例：G3a〜G3bではカルシウム・リンは6〜12か月ごと）はガイドラインの表から読み取りであり、本文の推奨文で確認したものではないため主張文には含めていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-C-②（CKD-MBD、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-025
  domain: KF
  subdomain: CKD-MBD
  assertion:
    plain_statement_ja: CKD-MBDの管理では、上昇した血清リンを正常範囲に向けて下げること、成人のCKDステージG3a〜G5Dでは高カルシウム血症を避けることが基本となる。透析患者（G5D）では、intact PTHを測定施設の基準値上限のおおよそ2〜9倍の範囲に維持することが提案され、リン吸着薬を用いる場合はカルシウム含有リン吸着薬の投与量を制限することが提案されている。
    condition:
      region: 国際
      population: CKDステージG3a〜G5D
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-651
    source: "KDIGO CKD-MBD Update Work Group. KDIGO 2017 Clinical Practice Guideline Update for the Diagnosis, Evaluation, Prevention, and Treatment of Chronic Kidney Disease–Mineral and Bone Disorder (CKD-MBD). Kidney Int Suppl. 2017;7(1):1–59"
    doi: 10.1016/j.kisu.2017.04.001
    pmid: '30675420'
    pmcid: PMC6340919
    url: https://doi.org/10.1016/j.kisu.2017.04.001
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 記載は2017年改訂版の推奨に基づくが、各推奨のエビデンスグレードはカードに含めていない。リン吸着薬など薬剤の国内の承認・保険適用の状況は、本セッションでは添付文書で確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-C-②（CKD-MBD、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-026
  domain: KF
  subdomain: CKD-MBD
  assertion:
    plain_statement_ja: 日本透析医学会のガイドラインでは、血液透析患者の管理目標として、血清リン3.5〜6.0 mg/dL、補正カルシウム8.4〜10.0 mg/dL、intact PTH 60〜240 pg/mLが示され、管理の優先順位はリン、カルシウム、副甲状腺ホルモンの順とされている。
    condition:
      region: 日本
      guideline: 日本透析医学会「慢性腎臓病に伴う骨・ミネラル代謝異常の診療ガイドライン」2012年版
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-652
    source: "Fukagawa M, Yokoyama K, Koiwa F, et al. Clinical practice guideline for the management of chronic kidney disease-mineral and bone disorder. Ther Apher Dial. 2013;17(3):247–288"
    doi: 10.1111/1744-9987.12058
    pmid: '23735142'
    pmcid: null
    url: https://doi.org/10.1111/1744-9987.12058
    source_license: © 日本透析医学会／Wiley（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 管理目標値と優先順位は二次資料経由で確認したものであり、原論文本文の該当表では本セッションで直接確認できていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-C-②（CKD-MBD、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-027
  domain: KF
  subdomain: 透析アミロイドーシス
  assertion:
    plain_statement_ja: 透析アミロイドーシスは、β2ミクログロブリンの沈着によって生じる長期透析の合併症であり、最も多い症状は手根管症候群である。維持血液透析患者386例の検討では、手根管症候群は40例（10.4%）に認められ、透析期間が有意な危険因子だった（手根管症候群ありの平均16.05年に対し、なしでは平均4.51年）。手術を要した割合は、透析期間10年未満で1.6%、10〜14年で42.1%、15〜19年で66.7%、20〜30年で100%と、透析期間が長いほど高かった。
    condition:
      region: 国際
      population: 維持血液透析患者（ポーランド2施設、386例）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-653
    source: "Kopeć J, Gadek A, Drożdż M, et al. Carpal tunnel syndrome in hemodialysis patients as a dialysis-related amyloidosis manifestation: incidence, risk factors and results of surgical treatment. Med Sci Monit. 2011;17(9):CR505–CR509"
    doi: null
    pmcid: PMC3560521
    pmid: '21873947'
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3560521/
    source_license: CC BY-NC-ND 3.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 単一国2施設の後ろ向き検討であり、数値はその集団での値である。出典論文のDOI文字列はPMC・出版社ページで確認できず null とした。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U)'
    kokushi: 医学各論 Ⅷ-3-D-①（透析アミロイドーシス、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-028
  domain: KF
  subdomain: 脱水と浮腫
  assertion:
    plain_statement_ja: 成人で脱水（循環血液量の減少）を身体診察で評価する際、起立時の脈拍増加が30回/分以上、または起立に伴う強いめまいがある所見は、大量の血液喪失に対して感度97%、特異度98%とされるが、中等度の喪失に対する感度は22%にとどまる。腋窩の乾燥は陽性尤度比2.8、口腔粘膜の湿潤や舌に溝がないことは陰性尤度比0.3とされる。一方、毛細血管再充満時間と皮膚の張り（ツルゴール）は、成人では診断的価値が証明されていない。
    condition:
      region: 国際
      population: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-654
    source: "McGee S, Abernethy WB 3rd, Simel DL. The rational clinical examination. Is this patient hypovolemic? JAMA. 1999;281(11):1022–1029"
    doi: 10.1001/jama.281.11.1022
    pmid: '10086438'
    pmcid: null
    url: https://doi.org/10.1001/jama.281.11.1022
    source_license: © American Medical Association（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は主として失血による循環血液量減少を対象とした診察所見の検討であり、浮腫の原因鑑別そのものはこの出典の範囲外であるため、浮腫の評価については本カードでは扱っていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-02-08-013 (id: JlAKpmo)；TBL-02-08-009 (id: JlAKpmk)'
    kokushi: 医学各論 Ⅷ-3-E-①（脱水と浮腫、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-029
  domain: KF
  subdomain: ナトリウム代謝異常
  assertion:
    plain_statement_ja: 低ナトリウム血症は血清ナトリウム135 mmol/L未満と定義され、救急外来を受診する患者の15〜20%にみられる頻度の高い異常である。重症度は、軽度が130〜134 mmol/L、中等度が125〜129 mmol/L、高度が125 mmol/L未満と分類される。治療は原因に応じて行い、重い神経症状がある場合には高張食塩水のボーラス投与が推奨される。
    condition:
      region: 国際
      guideline: 欧州の低ナトリウム血症診療ガイドライン（2014年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-655
    source: "Spasovski G, Vanholder R, Allolio B, et al. Clinical practice guideline on diagnosis and treatment of hyponatraemia. Eur J Endocrinol. 2014;170(3):G1–G47"
    doi: 10.1530/EJE-13-1020
    pmid: '24569125'
    pmcid: null
    url: https://doi.org/10.1530/EJE-13-1020
    source_license: © European Society of Endocrinology（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 重症度の区分はガイドラインの表から読み取りである。高張食塩水の具体的な投与量や投与方法は、本セッションでガイドライン本文を確認できなかったため主張文に含めていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-314 (id: Jlvnl8g)'
    kokushi: 医学各論 Ⅷ-3-E-②（ナトリウム代謝異常、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-030
  domain: KF
  subdomain: ナトリウム代謝異常
  assertion:
    plain_statement_ja: 高ナトリウム血症は血清ナトリウム145 mmol/Lを超える状態で、多くはナトリウムに対して相対的な水分の不足、すなわち水分喪失や水分摂取不足によって生じる。持続するには口渇の障害や水分へのアクセス障害が背景にあることが多く、高齢者や重症患者にみられやすい。重症度は軽度146〜150 mmol/L、中等度151〜155 mmol/L、重度155 mmol/L超と分類され、症状は脳細胞の脱水による中枢神経症状が中心である。慢性の高ナトリウム血症では脳細胞が有機オスモライトを蓄積して適応しているため、急速な水分補正は脳浮腫を招くおそれがある。
    condition:
      region: 国際
      population: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-656
    source: "Yun G, Baek SH, Kim S. Evaluation and management of hypernatremia in adults: clinical perspectives. Korean J Intern Med. 2023;38(3):290–302"
    doi: 10.3904/kjim.2022.346
    pmid: '36578134'
    pmcid: PMC10175862
    url: https://doi.org/10.3904/kjim.2022.346
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 重症度の区分は出典の表から読み取りである。成人の急速補正の是非については出典内でも議論があり（過補正の害を示す成人データは限定的とされる）、本カードでは補正速度の数値を扱っていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-314 (id: Jlvnl8g)'
    kokushi: 医学各論 Ⅷ-3-E-②（ナトリウム代謝異常、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-031
  domain: KF
  subdomain: ナトリウム代謝異常
  assertion:
    plain_statement_ja: 低ナトリウム血症の補正では、浸透圧性脱髄症候群を防ぐため、血清ナトリウムの上昇を最初の24時間で10 mmol/L以内、その後の24時間では8 mmol/L以内にとどめることが推奨される。過補正のリスクが高いのは、著しく低い血清ナトリウム（105 mmol/L以下）、低カリウム血症、アルコール依存、栄養不良、進行した肝疾患などのある患者である。
    condition:
      region: 国際
      guideline: 欧州の低ナトリウム血症診療ガイドライン（2014年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-655
    source: "Spasovski G, Vanholder R, Allolio B, et al. Clinical practice guideline on diagnosis and treatment of hyponatraemia. Eur J Endocrinol. 2014;170(3):G1–G47"
    doi: 10.1530/EJE-13-1020
    pmid: '24569125'
    pmcid: null
    url: https://doi.org/10.1530/EJE-13-1020
    source_license: © European Society of Endocrinology（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 補正速度の上限はガイドライン本文の要約で確認した。米国の専門家推奨など他の指針では上限の示し方が異なる場合がある。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-314 (id: Jlvnl8g)'
    kokushi: 医学各論 Ⅷ-3-E-②（ナトリウム代謝異常、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-032
  domain: KF
  subdomain: カリウム代謝異常
  assertion:
    plain_statement_ja: 高カリウム血症の初期対応では心電図変化の有無を確認することが重要である。心電図変化がある場合は、グルコン酸カルシウムの静注で心筋膜を安定化させ、インスリンとブドウ糖の投与でカリウムを細胞内へ移行させる。再検でも血清カリウムが6.0 mmol/Lを超えて続く場合など、内科的治療で制御できないときは血液透析を考慮する。
    condition:
      region: 国際
      guideline: KDIGOカリウム管理に関する国際会議の結論（2020年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-657
    source: "Clase CM, Carrero JJ, Ellison DH, et al. Potassium homeostasis and management of dyskalemia in kidney diseases: conclusions from a Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference. Kidney Int. 2020;97(1):42–61"
    doi: 10.1016/j.kint.2019.09.018
    pmid: '31706619'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2019.09.018
    source_license: © International Society of Nephrology／Elsevier（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤（グルコン酸カルシウム、インスリン等）の国内の承認・保険適用の詳細は、本セッションでは添付文書で確認していない。カリウム吸着薬など他の治療選択肢は本カードでは扱っていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-315 (id: Jlvnl8o)'
    kokushi: 医学各論 Ⅷ-3-E-③（カリウム代謝異常、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-033
  domain: KF
  subdomain: カリウム代謝異常
  assertion:
    plain_statement_ja: 低カリウム血症の原因診断では、尿中カリウム排泄をみて腎臓からの喪失か、消化管からの喪失や細胞内への移行かを分け、酸塩基平衡の異常の有無と合わせて原因を絞り込む。重症または有症状の低カリウム血症では、心電図でモニタリングしながら静注による補正を検討し、低マグネシウム血症があれば同時に補正する。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-658
    source: "Kardalas E, Paschou SA, Anagnostis P, et al. Hypokalemia: a clinical update. Endocr Connect. 2018;7(4):R135–R146"
    doi: 10.1530/EC-18-0109
    pmid: '29540487'
    pmcid: PMC5881435
    url: https://doi.org/10.1530/EC-18-0109
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 静注補正を検討する重症の目安（血清カリウム2.5 mmol/L未満）は、関連レビューの記載に基づく二次資料経由の確認である。カリウム製剤の国内の承認・保険適用の詳細は、本セッションでは添付文書で確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-315 (id: Jlvnl8o)'
    kokushi: 医学各論 Ⅷ-3-E-③（カリウム代謝異常、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-034
  domain: KF
  subdomain: カルシウム代謝異常
  assertion:
    plain_statement_ja: 高カルシウム血症は一般人口の約1%にみられ、その原因の約90%は原発性副甲状腺機能亢進症と悪性腫瘍である。重症度は、軽度が総カルシウム12 mg/dL未満、重度が14 mg/dL以上とされる。原因診断の第一歩はintact PTHの測定であり、重症または有症状の高カルシウム血症では、輸液による水分補正とビスホスホネートの静注が治療の柱となる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-659
    source: "Walker MD, Shane E. Hypercalcemia: A Review. JAMA. 2022;328(16):1624–1636"
    doi: 10.1001/jama.2022.18331
    pmid: '36282253'
    pmcid: null
    url: https://doi.org/10.1001/jama.2022.18331
    source_license: © American Medical Association（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ビスホスホネートなど薬剤の国内の承認・保険適用の詳細は、本セッションでは添付文書で確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-316 (id: Jlvnl8s)'
    kokushi: 医学各論 Ⅷ-3-E-④（カルシウム代謝異常、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-035
  domain: KF
  subdomain: カルシウム代謝異常
  assertion:
    plain_statement_ja: 低カルシウム血症では、血清カルシウム値を血清アルブミン値と合わせて解釈する必要がある。補正カルシウムが1.9 mmol/L未満の場合は、緊急に評価し、入院のうえ原因検索と治療を行うことを検討する。低マグネシウム血症があると低カルシウム血症は是正しにくいため、先にマグネシウムを補正する。副甲状腺ホルモンの欠乏による低カルシウム血症では、通常量のビタミンDではなく、カルシトリオールやアルファカルシドールなどの活性型ビタミンDを用いる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-660
    source: "Cooper MS, Gittoes NJL. Diagnosis and management of hypocalcaemia. BMJ. 2008;336(7656):1298–1302"
    doi: 10.1136/bmj.39582.589433.BE
    pmid: '18535072'
    pmcid: PMC2413335
    url: https://doi.org/10.1136/bmj.39582.589433.BE
    source_license: © BMJ Publishing Group（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 活性型ビタミンD製剤など薬剤の国内の承認・保険適用の詳細は、本セッションでは添付文書で確認していない。出典は2008年の総説であり、治療薬の選択肢はその後変化している可能性がある。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-316 (id: Jlvnl8s)'
    kokushi: 医学各論 Ⅷ-3-E-④（カルシウム代謝異常、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-036
  domain: KF
  subdomain: リン代謝異常
  assertion:
    plain_statement_ja: リンの恒常性は、腸管からの吸収、骨とのやり取り、腎臓からの排泄のバランスで保たれ、副甲状腺ホルモン、活性型ビタミンD、FGF23が調節に関わる。排泄の中心は腎臓であり、近位尿細管での再吸収が調節点となる。腎機能が低下するとリン排泄が障害されて高リン血症を来し、CKD-MBDの一因となる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-661
    source: "Blaine J, Chonchol M, Levi M. Renal control of calcium, phosphate, and magnesium homeostasis. Clin J Am Soc Nephrol. 2015;10(7):1257–1272"
    doi: 10.2215/CJN.09750913
    pmid: '25287933'
    pmcid: PMC4491294
    url: https://doi.org/10.2215/CJN.09750913
    source_license: ライセンス表示は未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典論文のライセンス表示は本セッションで確認できなかったため source_class を UNKNOWN とした（取り込み側でCrossref等による確認を推奨）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-317 (id: Jlvnl80)'
    kokushi: 医学各論 Ⅷ-3-E-⑤（リン代謝異常、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-037
  domain: KF
  subdomain: マグネシウム代謝異常
  assertion:
    plain_statement_ja: マグネシウムの恒常性は、腸管からの吸収と腎臓での再吸収で保たれる。腎臓では、糸球体で濾過されたマグネシウムの大部分がヘンレ上行脚と遠位尿細管で再吸収され、この再吸収の調節が血中濃度を決める。低マグネシウム血症は消化管からの喪失や利尿薬などの薬剤、腎臓からの喪失で生じ、低カリウム血症や低カルシウム血症を伴いやすい。高マグネシウム血症は、主に腎機能低下のある患者へのマグネシウム負荷で生じる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-662
    source: "de Baaij JHF, Hoenderop JGJ, Bindels RJM. Magnesium in man: implications for health and disease. Physiol Rev. 2015;95(1):1–46"
    doi: 10.1152/physrev.00012.2014
    pmid: '25540137'
    pmcid: null
    url: https://doi.org/10.1152/physrev.00012.2014
    source_license: © American Physiological Society（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 低マグネシウム血症・高マグネシウム血症の血中濃度による定義値（例：低マグネシウム血症は0.70 mmol/L未満）は、本セッションでは出典の抄録で確認できなかったため、主張文に濃度の数値を含めていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-318 (id: Jlvnl84)'
    kokushi: 医学各論 Ⅷ-3-E-⑥（マグネシウム代謝異常、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-038
  domain: KF
  subdomain: 代謝性アシドーシス
  assertion:
    plain_statement_ja: 代謝性アシドーシスの評価にはアニオンギャップを用い、アニオンギャップは血清ナトリウムから重炭酸とクロライドの和を引いて求める。代償の予測として、重炭酸が1 mmol/L低下するごとに動脈血二酸化炭素分圧は約1 mmHg低下すると見積もる。急性の代謝性アシドーシスの多くは、ケト酸や乳酸など有機酸の産生亢進によって生じる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-663
    source: "Kraut JA, Madias NE. Metabolic acidosis: pathophysiology, diagnosis and management. Nat Rev Nephrol. 2010;6(5):274–285"
    doi: 10.1038/nrneph.2010.33
    pmid: '20308999'
    pmcid: null
    url: https://doi.org/10.1038/nrneph.2010.33
    source_license: © Nature Publishing Group（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは代謝性アシドーシスとアニオンギャップに限った内容であり、呼吸性の酸塩基平衡異常は扱っていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-319 (id: Jlvnl9A)'
    kokushi: 医学各論 Ⅷ-3-F-①（代謝性アシドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-039
  domain: KF
  subdomain: 代謝性アシドーシス
  assertion:
    plain_statement_ja: 高アニオンギャップ代謝性アシドーシスの代表的な原因は、乳酸アシドーシス、ケトアシドーシス（糖尿病性、アルコール性、飢餓性）、腎不全、およびメタノール、エチレングリコール、サリチル酸などによる中毒である。治療の基本は原因の除去と原因疾患の治療であり、急性アシドーシスに対するアルカリ投与（重炭酸ナトリウム）の是非については議論がある。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-663
    source: "Kraut JA, Madias NE. Metabolic acidosis: pathophysiology, diagnosis and management. Nat Rev Nephrol. 2010;6(5):274–285"
    doi: 10.1038/nrneph.2010.33
    pmid: '20308999'
    pmcid: null
    url: https://doi.org/10.1038/nrneph.2010.33
    source_license: © Nature Publishing Group（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原因の列挙は出典本文の分類に基づく（抄録では、有機酸の産生亢進が急性代謝性アシドーシスの中心であることを確認した）。重炭酸ナトリウムなど薬剤の国内の承認・保険適用の詳細は、本セッションでは添付文書で確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-319 (id: Jlvnl9A)'
    kokushi: 医学各論 Ⅷ-3-F-①（代謝性アシドーシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KF-040
  domain: KF
  subdomain: 代謝性アルカローシス
  assertion:
    plain_statement_ja: 代謝性アルカローシスは、酸の喪失や重炭酸の蓄積によって生成され、腎臓が過剰な重炭酸を排泄できない状態によって維持される。関連する病態として、嘔吐、アルドステロンやコルチゾールの過剰、甘草の摂取、クロライド利尿薬の使用、カルシウム・アルカリの過剰摂取、Bartter症候群やGitelman症候群などの遺伝性疾患がある。生理食塩水に反応する塩化物反応性かどうかは、尿中クロライドで判断する。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-664
    source: "Do C, Vasquez PC, Soleimani M. Metabolic Alkalosis Pathogenesis, Diagnosis, and Treatment: Core Curriculum 2022. Am J Kidney Dis. 2022;80(4):536–551"
    doi: 10.1053/j.ajkd.2021.12.016
    pmid: '35525634'
    pmcid: null
    url: https://doi.org/10.1053/j.ajkd.2021.12.016
    source_license: © National Kidney Foundation／Elsevier（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 尿中クロライドの閾値（20 mEq/L未満で塩化物反応性）は教科書等の二次資料で確認した値であり、出典本文では本セッションで確認できなかったため、主張文には閾値の数値を含めていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-320 (id: Jlvnl9I)'
    kokushi: 医学各論 Ⅷ-3-F-②（代謝性アルカローシス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-001
  domain: KX
  subdomain: 浮腫
  assertion:
    plain_statement_ja: 浮腫の鑑別では、まず両側性か片側性かと、発症が急か慢性かで分けて考える。両側性の浮腫では心疾患・肝疾患・腎疾患などの全身性疾患を考え、心不全が疑わしければBNP、腎疾患では血清クレアチニンと尿検査、肝疾患では肝酵素とアルブミンが手がかりになる。カルシウム拮抗薬などの薬剤も両側性浮腫の原因になる。片側性で急性の浮腫では深部静脈血栓症を疑い、慢性の片側性・両側性下腿浮腫では静脈不全やリンパ浮腫を考える。非圧痕性の硬い浮腫はリンパ浮腫の特徴である。
    condition:
      region: 米国
      study: 2013年の総説（プライマリケア向けの鑑別診断）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-665
    source: 'Trayes KP, Studdiford JS, Pickle S, Tully AS. Edema: diagnosis and management. Am Fam Physician. 2013;88(2):102-110'
    doi: null
    pmid: '23939641'
    pmcid: null
    url: https://www.ncbi.nlm.nih.gov/pubmed/23939641
    source_license: 出版社（米国家庭医学会）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本誌の論文には DOI の付与を PubMed 収載頁・誌面のいずれでも確認できなかったため doi は null とした。原因薬剤として挙げた薬効群（カルシウム拮抗薬など）は国内承認薬の範囲であるが、個別製剤の適応・保険適用の確認はしていない。米国のプライマリケア向け総説であり、日本の診療での検査の優先順位と同一とは限らない。
  curriculum:
    core_curriculum: 'PS-02-09-02 (id: JkxnuRg)；TBL-02-08-009 (id: JlAKpmk)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-002
  domain: KX
  subdomain: 乏尿・無尿
  assertion:
    plain_statement_ja: 急性腎障害の診断基準では、血清クレアチニンの48時間以内の0.3 mg/dL以上の上昇、または7日以内の基礎値の1.5倍以上の上昇が用いられ、尿量では0.5 mL/kg/時未満が6時間以上続く状態が乏尿の目安になる。乏尿・無尿の鑑別は腎前性（循環血液量の減少や腎灌流の低下）、腎性（尿細管・間質・糸球体などの実質障害）、腎後性（尿路閉塞）に分けて行い、初期評価として尿検査と尿沈渣の観察、尿路閉塞を除外するための超音波などの画像検査が最低限必要になる。腎後性は治療可能な原因であり、初期対応で見逃さないことが要点である。
    condition:
      region: 国際
      study: 2016年の総説（AKI の診断と精査。診断基準は KDIGO の定義に基づく）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-666
    source: 'Ostermann M, Joannidis M. Acute kidney injury 2016: diagnosis and diagnostic workup. Crit Care. 2016;20:299'
    doi: 10.1186/s13054-016-1478-z
    pmid: '27670788'
    pmcid: PMC5037640
    url: https://doi.org/10.1186/s13054-016-1478-z
    source_license: CC BY 4.0（PMC ページの表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 診断基準の数値は KDIGO の定義を総説が引用したものである。本カードは AKI 全般の初期評価の枠組みであり、乏尿・無尿だけを対象集団とした数値ではない。個別の原因疾患ごとの対応は各疾患のカードに譲る。
  curriculum:
    core_curriculum: 'PS-02-09-02 (id: JkxnuRg)；TBL-02-08-012 (id: JlAKpms)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-003
  domain: KX
  subdomain: 多尿
  assertion:
    plain_statement_ja: 多尿の目安は1日尿量がおおよそ40〜50 mL/kgを超える量で、成人では1日2.5〜3 L以上が目安になり、尿崩症では1日8〜16 Lに達することもある。尿崩症では尿浸透圧が300 mOsm/kg未満の低張尿が多量に排泄され、バソプレシンの分泌不足による中枢性、腎の反応性低下による腎性、妊娠に伴う妊娠性に分けられる。これに対して浸透圧性利尿（グルコース、尿素、マンニトール、生理食塩水の負荷、閉塞解除後利尿など）では尿浸透圧は高く、心因性多飲では水制限によって尿が濃縮される点が鑑別の要点になる。
    condition:
      region: 国際
      study: 2021年の総説（尿崩症の実践的な管理）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-667
    source: 'Priya G, Kalra S, Dasgupta A, Grewal E. Diabetes insipidus: a pragmatic approach to management. Cureus. 2021;13(1):e12498'
    doi: 10.7759/cureus.12498
    pmid: '33425560'
    pmcid: PMC7785480
    url: https://doi.org/10.7759/cureus.12498
    source_license: CC BY 4.0（PMC ページの表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 原著では治療薬としてデスモプレシン、サイアザイド系利尿薬、アミロライドが挙げられているが、本カードでは用法・用量は扱っていない。これらの薬剤の国内承認・保険適用（尿崩症への適応を含む）は未確認である。多尿の閾値は総説の記載に基づく目安であり、診断は尿・血清浸透圧と水制限試験などの総合評価による。
  curriculum:
    core_curriculum: 'PS-02-09-02 (id: JkxnuRg)；TBL-02-08-012 (id: JlAKpms)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-004
  domain: KX
  subdomain: 排尿障害
  assertion:
    plain_statement_ja: 男性の下部尿路症状の評価では、国際前立腺症状スコア（IPSS）が用いられ、合計は0〜35点で、7点を超えると中等症、19点を超えると重症の目安になり、3点以上の変化が臨床的に意味のある変化とされる。症状は排尿症状（尿勢の低下、排尿の遅延など）と蓄尿症状（頻尿、尿意切迫感、夜間頻尿など）に分けて聞き取る。前立腺肥大以外にも、神経因性膀胱、薬剤の影響、心疾患に伴う夜間多尿などが原因になるため、尿検査で尿路感染など治療可能な原因を探すことも評価に含まれる。
    condition:
      region: 国際
      study: 2014年の臨床総説（男性の下部尿路症状）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-668
    source: 'Hollingsworth JM, Wilt TJ. Lower urinary tract symptoms in men. BMJ. 2014;349:g4474'
    doi: 10.1136/bmj.g4474
    pmid: '25125424'
    pmcid: PMC4688452
    url: https://doi.org/10.1136/bmj.g4474
    source_license: 出版社（BMJ）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは男性の下部尿路症状を対象とした総説に基づいており、女性の排尿障害にはそのまま適用できない。IPSS の境界値は総説の記載に基づく。治療薬（α遮断薬など）の国内承認・保険適用は本カードでは扱っておらず未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-02 (id: JkxnuRg)；TBL-02-08-012 (id: JlAKpms)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-005
  domain: KX
  subdomain: 血尿
  assertion:
    plain_statement_ja: 血尿の症候としての鑑別では、出血部位が糸球体か非糸球体かを見分けることが要点になる。尿沈渣で変形（異形）赤血球や赤血球円柱がみられれば糸球体からの出血を示唆し、とくに赤血球円柱は腎炎性の沈渣所見である。一方、形態のそろった赤血球が中心で円柱を伴わない血尿は、結石・尿路の腫瘍・尿路感染など腎外（尿路）からの出血を考える。蛋白尿や腎機能低下を伴う場合は糸球体疾患の可能性が高まり、腎炎性の沈渣（赤血球円柱、白血球、腎尿細管上皮細胞など活動性の所見の混在）が診断の手がかりになる。
    condition:
      region: 国際
      study: 2024年の総説（尿沈渣の診断的利用）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-669
    source: 'Gaggar P, Raju SB. Diagnostic utility of urine microscopy in kidney diseases. Indian J Nephrol. 2024;34(3):213-221'
    doi: 10.25259/ijn_362_23
    pmid: '39114391'
    pmcid: PMC11303840
    url: https://doi.org/10.25259/ijn_362_23
    source_license: CC BY-NC-SA 4.0（PMC ページの表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは症候としての鑑別に絞り、個別の糸球体疾患は扱っていない（第15回の対象）。有棘赤血球などの所見の診断精度（感度・特異度）の数値は、SRC の枠数の都合で本カードの出典には含めなかったため記載していない。沈渣所見の判定は検者の熟練度に依存する。
  curriculum:
    core_curriculum: 'PS-02-09-02 (id: JkxnuRg)；TBL-02-08-010 (id: JlAKpmc)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-006
  domain: KX
  subdomain: 尿検査・尿蛋白定量
  assertion:
    plain_statement_ja: 尿蛋白の定量評価には尿アルブミン/クレアチニン比（ACR）が用いられ、アルブミン尿は A1（30 mg/g未満）、A2（30〜300 mg/g）、A3（300 mg/gを超える）の3区分に分けられる。試験紙法は半定量的なスクリーニングであり、陽性所見の評価や経過の判定は ACR などの定量法で行う。腎の異常が3か月以上持続することが慢性腎臓病の要件であり、eGFR や ACR の1回の異常値だけで慢性と決めず、再検で持続性を確認する。分類は原因、GFR 区分、アルブミン尿区分を組み合わせて行う。
    condition:
      region: 国際
      study: KDIGO 2024 CKD 評価・管理ガイドライン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-573
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int. 2024;105(4S):S117-S314'
    doi: 10.1016/j.kint.2023.10.018
    pmid: '38490803'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2023.10.018
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: アルブミン尿区分の境界値はガイドラインの表から読み取ったものである（表から読み取り）。日本の特定健診などで用いる試験紙法の判定区分とは方式が異なり、試験紙の半定量値と ACR は直接は対応しない。
  curriculum:
    core_curriculum: 'PS-02-09-03 (id: JkxnuRk)；TBL-02-08-011 (id: JlAKpmg)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-007
  domain: KX
  subdomain: 尿沈渣
  assertion:
    plain_statement_ja: 尿沈渣では円柱の種類が障害部位の手がかりになる。赤血球円柱は腎炎症候群、白血球円柱は急性間質性腎炎・腎盂腎炎・腎炎、腎尿細管上皮円柱や顆粒円柱は急性尿細管壊死に結びつき、泥状の褐色顆粒円柱は急性尿細管壊死に特異的とされる。硝子円柱は運動・脱水・発熱などでもみられる非特異的な所見であり、ろう様円柱は腎不全、脂肪円柱はネフローゼ域の蛋白尿に伴う。沈渣の基準の目安は赤血球0〜3個/HPF、白血球0〜8個/HPFで、検体は室温では1時間以内、冷蔵でも4時間以内に観察することが望ましい。
    condition:
      region: 国際
      study: 2024年の総説（尿沈渣の診断的利用）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-669
    source: 'Gaggar P, Raju SB. Diagnostic utility of urine microscopy in kidney diseases. Indian J Nephrol. 2024;34(3):213-221'
    doi: 10.25259/ijn_362_23
    pmid: '39114391'
    pmcid: PMC11303840
    url: https://doi.org/10.25259/ijn_362_23
    source_license: CC BY-NC-SA 4.0（PMC ページの表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 円柱と疾患の対応、基準値、観察までの時間は総説の表から読み取ったものである（表から読み取り）。泥状褐色顆粒円柱の特異度100%という数値は原著が引用した単一研究の結果であり、施設や検者によって判定が異なりうる。自動分析では病的円柱や変形赤血球の検出に限界があると原著は述べている。
  curriculum:
    core_curriculum: 'PS-02-09-03 (id: JkxnuRk)；TBL-02-08-015 (id: JlAKpm0)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-008
  domain: KX
  subdomain: 推算糸球体濾過量
  assertion:
    plain_statement_ja: 日本人の血清クレアチニンに基づく eGFR 推算式は、eGFR（mL/min/1.73 m²）＝194 × 血清クレアチニン^−1.094 × 年齢^−0.287 で計算し、女性では0.739を乗じる3変数の式である。この式は日本人での検証に基づき、国際式（IDMS-MDRD式）に日本人の係数0.808を当てはめる方法から改訂された。検証では実測GFRに対するバイアスが小さく、実測値の30%以内に収まる割合は75%であったと報告されている。筋肉量の大きく異なる患者では誤差が大きくなるため、式の限界を踏まえて解釈する。
    condition:
      region: 日本
      study: 2009年の原著（日本人での eGFR 推算式の改訂と検証）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-671
    source: 'Matsuo S, Imai E, Horio M, Yasuda Y, Tomita K, Nitta K, et al. Revised equations for estimated GFR from serum creatinine in Japan. Am J Kidney Dis. 2009;53(6):982-992'
    doi: 10.1053/j.ajkd.2008.12.034
    pmid: '19339088'
    pmcid: null
    url: https://doi.org/10.1053/j.ajkd.2008.12.034
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 推算式と検証の数値は抄録で確認した。クレアチニンの測定法（酵素法への標準化）を前提とした式であり、測定条件が異なる場合は適用に注意がいる。小児には適用できない。
  curriculum:
    core_curriculum: 'PS-02-09-03 (id: JkxnuRk)；TBL-02-08-015 (id: JlAKpm0)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-009
  domain: KX
  subdomain: シスタチンC
  assertion:
    plain_statement_ja: シスタチン C はクレアチニンと並ぶ糸球体濾過の指標であり、国際ガイドラインは、CKD のリスクがある成人ではまずクレアチニンに基づく eGFR を用い、シスタチン C が利用できる場合はクレアチニンとシスタチン C の両方から推算する eGFR（eGFRcr-cys）で GFR 区分を推定することを勧めている（推奨グレード1B）。クレアチニンは筋肉量の影響を受けやすいため、筋肉量が通常と大きく異なる患者など、クレアチニン式の正確さに疑問がある場面でシスタチン C の併用が評価の助けになる。
    condition:
      region: 国際
      study: KDIGO 2024 CKD 評価・管理ガイドライン（推奨1.1.2.1）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-573
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. Kidney Int. 2024;105(4S):S117-S314'
    doi: 10.1016/j.kint.2023.10.018
    pmid: '38490803'
    pmcid: null
    url: https://doi.org/10.1016/j.kint.2023.10.018
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: シスタチン C を用いる推算式そのものの係数や、クレアチニン単独式との精度比較の数値は、SRC の枠数の都合で本カードの出典には含めなかったため記載していない。日本でのシスタチン C 測定の保険適用の条件は未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-03 (id: JkxnuRk)；TBL-02-08-015 (id: JlAKpm0)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-010
  domain: KX
  subdomain: 腎生検
  assertion:
    plain_statement_ja: 腎生検は、組織診断が治療方針を決める場合に行う侵襲的検査である。孤立性の顕微鏡的血尿や1日0.5〜1.0 g未満の少量の蛋白尿だけでは、腎機能低下などの他の適応がない限り通常は行わない。相対的禁忌には、小さい腎臓・末期腎不全、多発性の両側嚢胞、矯正できない出血傾向や抗血小板薬・抗凝固薬の最近の使用、重度の血小板減少、降圧薬でコントロールできない重症高血圧、水腎症、尿路感染・腎盂腎炎・腎周囲感染、馬蹄腎、協力が得られない患者などが挙げられる。合併症の頻度はメタ解析（34研究・9474件）で、肉眼的血尿3.5%、赤血球輸血0.9%、処置を要したもの0.6%、腎摘出0.01%、死亡0.02%と報告されている。
    condition:
      region: 国際
      study: 2016年の総説（自己腎生検の適応・手技・合併症。合併症の頻度は Corapi らのメタ解析の引用）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-672
    source: 'Hogan JJ, Mocanu M, Berns JS. The native kidney biopsy: update and evidence for best practice. Clin J Am Soc Nephrol. 2016;11(2):354-362'
    doi: 10.2215/CJN.05750515
    pmid: '26339068'
    pmcid: PMC4741037
    url: https://doi.org/10.2215/CJN.05750515
    source_license: 出版社（米国腎臓学会）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 合併症の頻度は原著が引用したメタ解析の値であり、針の太さや患者背景で変わる（大規模単施設の報告では輸血率が5〜9%に達するものもあると原著は述べている）。日本の腎生検の実施基準（国内のガイドブック）とは細部が異なる可能性がある。
  curriculum:
    core_curriculum: 'PS-02-09-03 (id: JkxnuRk)；TBL-02-08-017 (id: JlAKpm8)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-011
  domain: KX
  subdomain: 画像検査
  assertion:
    plain_statement_ja: 腎・尿路の画像検査は目的によって選択する。尿路結石の急性期の評価では、単純 CT が最も一貫して正確な検査であるが放射線被ばくを伴う。超音波検査は感度・特異度で CT に劣るものの被ばくがなく、救急外来での無作為化試験では診断の正確さが CT と同等であったとされる。単純 X 線（KUB）は既知の結石の経過観察（増大の確認）には向くが、急性期の結石の検出には不向きである。MRI は被ばくがない一方で費用が高く、結石そのものは描出しにくい。水腎症の有無や腎の形態の確認など、閉塞のスクリーニングには超音波が広く用いられる。
    condition:
      region: 国際
      study: 2016年の総説（腎結石の画像検査技術の概観）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-673
    source: 'Brisbane W, Bailey MR, Sorensen MD. An overview of kidney stone imaging techniques. Nat Rev Urol. 2016;13(11):654-662'
    doi: 10.1038/nrurol.2016.154
    pmid: '27578040'
    pmcid: PMC5443345
    url: https://doi.org/10.1038/nrurol.2016.154
    source_license: 出版社の著作物（著者原稿の PMC 掲載。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードの出典は尿路結石の画像検査を主題とした総説であり、腎腫瘍や感染症など他の疾患の画像選択にはそのまま適用できない。各検査の感度・特異度の具体的な数値は原著の本文表に依存するため、本カードには数値を入れていない。
  curriculum:
    core_curriculum: 'PS-02-09-03 (id: JkxnuRk)；TBL-02-08-016 (id: JlAKpm4)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-012
  domain: KX
  subdomain: 透析導入
  assertion:
    plain_statement_ja: 日本の透析導入の指針では、腎不全症状があっても保存的治療に耐えられる間は GFR が8 mL/min/1.73 m²を下回るまで待つ方が予後は良好であること、症状がなくても GFR が2 mL/min/1.73 m²まで低下する前に血液透析を導入すべきであることが示されている（推奨グレード2C）。また、GFR が15〜30 mL/min/1.73 m²の段階で腎代替療法について詳しく説明することが勧められている。導入の判断は数値だけでなく、症状、栄養状態、体液管理の状況と患者の意向を合わせて行う。
    condition:
      region: 日本
      study: 日本透析医学会の維持血液透析導入ガイドライン（2015年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-674
    source: 'Watanabe Y, Yamagata K, Nishi S, Hirakata H, Maruyama S, Saito C, et al.; Japanese Society for Dialysis Therapy Clinical Guideline Work Group. Japanese Society for Dialysis Therapy clinical guideline for "hemodialysis initiation for maintenance hemodialysis". Ther Apher Dial. 2015;19 Suppl 1:93-107'
    doi: 10.1111/1744-9987.12293
    pmid: '25817934'
    pmcid: null
    url: https://doi.org/10.1111/1744-9987.12293
    source_license: 学会（日本透析医学会）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: GFR の閾値と推奨グレードは抄録に記載されたステートメントに基づく。ガイドラインは2015年のものであり、その後の診療報酬や国内の診療実態の変化は反映していない。腹膜透析の導入時期は本ガイドラインの主題ではない。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-013
  domain: KX
  subdomain: 血液透析と腹膜透析
  assertion:
    plain_statement_ja: 血液透析（HD）と腹膜透析（PD）は、実施場所と体への負荷のかかり方が異なる腎代替療法である。HD は施設で透析器を用いて行い、毎回の穿刺や急速な除水が血行動態に影響し、残存腎機能の低下が速いとされる。PD は患者自身の腹膜を用いて自宅で行うことができ、血行動態への影響が小さく残存腎機能を保ちやすい一方、腹膜炎の発生が多く、蛋白・エネルギーの栄養障害のリスクがある。糖尿病性腎不全の患者を対象としたメタ解析（16研究、PD 635例・HD 719例）では、PD 群で尿量が多く残存腎機能が保たれ、心血管イベント（オッズ比0.42）と出血（オッズ比0.41）のリスクが低かったが、アルブミンと総蛋白は低く、感染のリスクが高いという結果であった。
    condition:
      region: 国際
      study: 2023年の系統的レビュー・メタ解析（糖尿病性腎不全における HD と PD の比較。中国の経験を中心とする集積）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-675
    source: 'Wei Z, Jin Y, Cheng J, Han X, Liu J, Liu S. Chinese experience on comparison of clinical efficacy and safety of hemodialysis and peritoneal dialysis in the treatment of diabetic kidney failure: a systematic review and meta-analysis. Front Med (Lausanne). 2023;10:1116103'
    doi: 10.3389/fmed.2023.1116103
    pmid: '37636569'
    pmcid: PMC10449255
    url: https://doi.org/10.3389/fmed.2023.1116103
    source_license: CC BY 4.0（PMC ページの表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 対象は糖尿病性腎不全の患者に限られ、非糖尿病の患者集団への一般化には注意がいる。数値はメタ解析の統合値であり、含まれる研究の実施地域や時代背景の影響を受ける。生存率については研究間で結果が一致せず、本カードでは優劣を断定していない。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-014
  domain: KX
  subdomain: 透析患者統計
  assertion:
    plain_statement_ja: 日本透析医学会の統計調査（2022年末）では、慢性透析患者数は347,474人で、調査開始以来初めて前年より減少した。人口100万人あたりの患者数は2,781人、患者の平均年齢は69.87歳であった。年末患者の原疾患は糖尿病性腎症39.5%、慢性糸球体腎炎24.0%、腎硬化症13.4%の順で、2022年の新規導入患者は39,683人（平均年齢71.42歳、原疾患は糖尿病性腎症38.7%が最多）であった。2022年の死亡は38,464人で粗死亡率は11.0%と調査史上最も高く、死因は感染症22.6%、心不全21.0%、悪性腫瘍7.6%の順であった。治療法では血液透析濾過（HDF）が191,492人（55.1%）を占め、腹膜透析患者は10,531人、在宅血液透析は827人であった。
    condition:
      region: 日本
      study: 日本透析医学会 腎データレジストリ（JRDR）の2022年次調査報告（施設調査4,521施設、施設回答率98.7%、患者調査回答率94.6%）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-676
    source: 'Hanafusa N, Abe M, Joki N, Hoshino J, Taniguchi M, Kikuchi K, Hasegawa T, Goto S, Ogawa T, Kanda E, et al. Annual dialysis data report 2022, Japanese Society for Dialysis Therapy (JSDT) Renal Data Registry. Ren Replace Ther. 2025;11:54'
    doi: 10.1186/s41100-025-00646-3
    pmid: null
    pmcid: null
    url: https://doi.org/10.1186/s41100-025-00646-3
    source_license: CC BY 4.0（BMC の誌面表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 数値は2022年末時点の年次報告の抄録で確認したもので、その後の年次報告では更新される。PMID は PubMed・PMC での収載を確認できなかったため null とした。粗死亡率の高さについて原著は新型コロナウイルス感染症の影響の可能性に言及しているが、因果関係が確定したものではない。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-015
  domain: KX
  subdomain: 急性血液浄化
  assertion:
    plain_statement_ja: 急性血液浄化は、急性腎障害の代行と、急性中毒における毒物の体外除去の二つの目的で行われる。集中治療領域では、体液過剰を伴い血行動態が不安定な急性腎障害の患者に持続的腎代替療法が用いられる。中毒では、体外除去が必要になるのは中毒全体の0.1%程度とされ、多くの毒物で間欠的血液透析が第一選択になる。持続的腎代替療法の毒物クリアランスは間欠的手法より50〜80%低く、血行動態が不安定な場合や、透析後の濃度再上昇（リバウンド）への対策として位置づけられる。毒物ごとの適応は国際的な専門家作業部会（EXTRIP）の推奨が示されており、リチウム、サリチル酸、メタノールなどが代表的な対象である。
    condition:
      region: 国際
      study: 2018年の総説（急性中毒に対する体外除去。集中治療医向け）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-677
    source: 'Jha VK, Padmaprakash KV. Extracorporeal treatment in the management of acute poisoning: what an intensivist should know? Indian J Crit Care Med. 2018;22(12):862-869'
    doi: 10.4103/ijccm.IJCCM_425_18
    pmid: '30662226'
    pmcid: PMC6311976
    url: https://doi.org/10.4103/ijccm.IJCCM_425_18
    source_license: CC BY-NC-SA 4.0（PMC ページの表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 急性腎障害に対する腎代替療法の開始時期を比較した大規模無作為化試験の結果（早期開始と標準開始で転帰に差がなかったことなど）は、SRC の枠数の都合で本カードの出典には含めなかったため、数値は記載していない。個別の毒物の血中濃度の閾値は EXTRIP の毒物ごとの推奨を別途確認する必要がある。国内の中毒診療の体制（中毒情報センター等）は本カードでは扱っていない。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-016
  domain: KX
  subdomain: 維持透析の合併症
  assertion:
    plain_statement_ja: 維持血液透析の合併症である透析中血圧低下は、死亡との関連が強い定義として、透析中の最低収縮期血圧が90 mmHg未満になる回が全体の30%を超える状態が挙げられている。除水速度が10 mL/時/kgを超えると心血管死亡と全死亡のリスクが高まり、13 mL/時/kgを超えるとさらに顕著になる。危険因子には、透析間体重増加が大きいこと、降圧薬の使用、透析液ナトリウムや高い除水速度、透析液温度などがある。繰り返す血圧低下は心筋のスタニング（気絶心筋）や脳・腸管などの臓器障害をもたらしうるため、除水速度とドライウェイトの設定、透析液温度の調整などで予防する。
    condition:
      region: 国際
      study: 2017年の総説（透析中血圧低下と生存）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-678
    source: 'Chou JA, Kalantar-Zadeh K, Mathew AT. A brief review of intradialytic hypotension with a focus on survival. Semin Dial. 2017;30(6):473-480'
    doi: 10.1111/sdi.12627
    pmid: '28661565'
    pmcid: PMC5738929
    url: https://doi.org/10.1111/sdi.12627
    source_license: 出版社の著作物（著者原稿の PMC 掲載。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 血圧低下の定義と除水速度の閾値は、原著が引用した観察研究に基づくもので、定義によって頻度や関連の強さは異なる。管理で用いる薬剤（昇圧薬など）の国内承認・保険適用は本カードでは扱っておらず未確認である。日本の透析施設での実施基準とは細部が異なる可能性がある。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-017
  domain: KX
  subdomain: 腎代替療法の選択と共同意思決定
  assertion:
    plain_statement_ja: 腎代替療法の選択では、血液透析、腹膜透析、腎移植、透析を行わない保存的療法を比較の対象とし、患者の価値観と生活状況に沿って共同で意思決定を行う枠組みが提案されている。その手順は、ともに最適な選択肢を決めるという目標の共有、患者の参加が必要であることの説明、各選択肢の利点・欠点・生活への影響についての包括的な情報提供、患者の生活上の優先事項や家族の支援などの状況と価値観の把握、価値観に合う決定、決定の確認と選択した治療への準備、の6段階からなる。共同意思決定により患者の知識、満足度、自律性が高まることが報告されている。
    condition:
      region: 国際
      study: 腎代替療法の共同意思決定に関する包括的レビューと6段階モデルの提案（2025年、各国の臨床研究のレビューを含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-679
    source: 'Shin HJ, Choi S, Kim S. Shared decision-making for kidney replacement therapy: a comprehensive review and a proposed model. Korean J Intern Med. 2025;40(6):890-908'
    doi: 10.3904/kjim.2025.019
    pmid: '41223871'
    pmcid: PMC12611495
    url: https://doi.org/10.3904/kjim.2025.019
    source_license: CC BY-NC 4.0（PMC ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 提案された6段階モデルは韓国で開発され各国の研究を踏まえたものであり、長期的な臨床転帰への影響は今後の検証が必要と出典自身が述べている。日本での実施体制や意思決定支援ツールの利用可能性は本カードでは確認していない。本カードには薬剤名は含まれない。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-018
  domain: KX
  subdomain: 保存的腎臓療法
  assertion:
    plain_statement_ja: 保存的腎臓療法は、透析そのものを行わない点を除き、透析を行う場合と同様の薬物治療や症状への対応、栄養や貧血などの管理を続ける治療戦略であり、透析を導入しないという選択を症状緩和と生活の質を重視して支えるものである。ステージ5の慢性腎臓病を対象に保存的管理と透析を比較した観察研究25件の系統的レビューでは、全体として保存的管理を選んだ患者の生存期間は透析を選んだ患者より短く、死亡に関する統合ハザード比は0.47（95%信頼区間0.34〜0.65）だった。一方、80歳以上の患者と併存症の多い高齢者では透析の生存上の利点はあいまいになり失われる可能性があり、生活の質、症状負担、入院、死亡の場所については保存的管理に利点がありうるとされた。
    condition:
      region: 国際
      study: 保存的腎臓管理と透析を比較した観察研究25件の系統的レビュー（2021年、Murtagh ら2007年の75歳超のコホートを含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-680
    source: 'Buur LE, Madsen JK, Eidemak I, Krarup E, Lauridsen TG, Taasti LH, Finderup J. Does conservative kidney management offer a quantity or quality of life benefit compared to dialysis? A systematic review. BMC Nephrol. 2021;22:307'
    doi: 10.1186/s12882-021-02516-6
    pmid: '34507554'
    pmcid: PMC8434727
    url: https://doi.org/10.1186/s12882-021-02516-6
    source_license: CC BY 4.0（PMC ページの Open Access 表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 対象研究はすべて観察研究で研究間の異質性が大きく、透析に有利な方向のバイアスが指摘されている。統合ハザード比は透析群と保存的管理群の死亡比較として出典の抄録に記載された値であり、個々の患者の予後をそのまま示すものではない。症状緩和に用いる個別の薬剤名は本カードに記載しておらず、その国内の承認・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-019
  domain: KX
  subdomain: バスキュラーアクセス
  assertion:
    plain_statement_ja: 血液透析のバスキュラーアクセスは、患者ごとの末期腎不全の生活計画に基づいて、適切な患者に適切な時期に適切なアクセスを作るという考え方で計画し、作製計画だけでなく代替案と血管温存の計画を含めて定期的に見直す。自己血管による内シャントでは、放射線的または外科的な介入を行っても作製後6か月までに透析に使用できない場合を成熟不全という。管理上の合併症には、狭窄や血栓によるアクセス機能不全と感染があり、感染した動静脈アクセスでは経験的な広域抗菌薬を迅速に開始し、アクセス合併症に精通した外科医へ速やかに紹介することが妥当とされる。
    condition:
      region: 米国
      study: KDOQI 血管アクセスガイドライン 2019年更新（2020年掲載）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-681
    source: 'Lok CE, Huber TS, Lee T, Shenoy S, Yevzlin AS, Abreo K, Allon M, Asif A, Astor BC, Glickman MH, Graham J, Moist LM, Rajan DK, Roberts C, Vachharajani TJ, Valentini RP; National Kidney Foundation. KDOQI Clinical Practice Guideline for Vascular Access: 2019 Update. Am J Kidney Dis. 2020;75(4 Suppl 2):S1-S164'
    doi: 10.1053/j.ajkd.2019.12.001
    pmid: '32778223'
    pmcid: null
    url: https://doi.org/10.1053/j.ajkd.2019.12.001
    source_license: 学会ガイドライン（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国のガイドラインであり、日本の施設の体制や手技の実情と同一とは限らない。合併症の頻度の数値は本カードでは扱っていない。感染時に用いる抗菌薬の個別製剤について、国内の承認・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-020
  domain: KX
  subdomain: 腹膜透析の合併症
  assertion:
    plain_statement_ja: 腹膜透析関連腹膜炎は、腹痛や排液混濁などの腹膜炎に合致する臨床所見、少なくとも2時間貯留した後の排液白血球数が100/μLを超え好中球が50%を超えること、排液培養が陽性であること、の3項目のうち少なくとも2項目を満たす場合に診断する。排液の混濁がある患者は腹膜炎とみなして診断が確定または否定されるまで治療し、腹膜炎が疑われる場合は常に排液の細胞数と分画、グラム染色、培養を行う。経験的治療はグラム陽性菌とグラム陰性菌の両方を対象として施設ごとに選び、施設の目標として腹膜炎の発生率はリスク下の1年あたり0.40件以下、1年間に腹膜炎のない患者の割合は80%を超えることが示されている。
    condition:
      region: 国際
      study: ISPD 腹膜炎ガイドライン 2022年更新（予防と治療）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-682
    source: 'Li PK, Chow KM, Cho Y, Fan S, Figueiredo AE, Harris T, Kanjanabuch T, Kim YL, Madero M, Malyszko J, Mehrotra R, Okpechi IG, Perl J, Piraino B, Runnegar N, Teitelbaum I, Wong JK, Yu X, Johnson DW. ISPD peritonitis guideline recommendations: 2022 update on prevention and treatment. Perit Dial Int. 2022;42(2):110-153'
    doi: 10.1177/08968608221080586
    pmid: '35264029'
    pmcid: null
    url: https://doi.org/10.1177/08968608221080586
    source_license: CC BY-NC 4.0（Crossref の license 欄で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 診断基準の数値と発生率の目標はガイドライン本文と抄録で確認した。個別の抗菌薬名と用量は本カードに記載しておらず、経験的治療に用いる抗菌薬について国内の承認・保険適用は未確認である。起炎菌ごとの治療やカテーテル抜去の基準は本カードの範囲外である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-021
  domain: KX
  subdomain: 腎移植の適応と現状
  assertion:
    plain_statement_ja: 腎移植は腎不全に対する腎代替療法の主要な選択肢の一つであり、透析と比べて生存、生活の質、医療費の面で利点があるとされる。日本ではドナー不足などから実施は限られており、年間の実施件数は2010年代以降おおむね1,500〜2,000件で推移している。1964年から2023年までの累計は47,466件で、このうち生体腎移植が39,543件、献腎移植が7,923件と生体腎移植が大部分を占める。2023年時点で機能している移植腎を持つレシピエントは推計31,552人で、腎代替療法を受けている患者の8.4%を占めると推計されている。
    condition:
      region: 日本
      study: 日本の移植登録の集計に基づく推計研究（1964〜2023年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-683
    source: 'Komaba H, Nakagawa Y, Koizumi M, Tomita Y, Nakamura M. Estimated Number of Prevalent Kidney Transplant Recipients in Japan From 1964 to 2023. Transpl Int. 2025;38:15732'
    doi: 10.3389/ti.2025.15732
    pmid: '41480389'
    pmcid: PMC12755172
    url: https://doi.org/10.3389/ti.2025.15732
    source_license: CC BY（誌面のオープンアクセス表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: レシピエント数31,552人と8.4%は、移植登録の集計と時代ごとの移植腎生存率に基づく推計値であり、個々の症例を追跡して数えた実数ではない。レシピエントの適否を決める医学的基準の詳細は本出典では確認できないため記載していない。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-022
  domain: KX
  subdomain: 腎移植の免疫抑制療法
  assertion:
    plain_statement_ja: 腎移植では免疫抑制薬の併用を移植前または移植時に開始し、初期免疫抑制には生物学的製剤による導入療法を含めることが勧められる。導入療法ではインターロイキン2受容体拮抗薬が第一選択とされ、免疫学的リスクが高いレシピエントではリンパ球除去薬の使用が提案される。維持療法はカルシニューリン阻害薬と増殖抑制薬の併用を基本とし、副腎皮質ステロイドは併用する場合としない場合がある。カルシニューリン阻害薬ではタクロリムスが、増殖抑制薬ではミコフェノール酸がそれぞれ第一選択として提案され、カルシニューリン阻害薬は移植腎機能の発現を待たず、移植前または移植時に開始する。免疫学的リスクが低く導入療法を受けた患者では、副腎皮質ステロイドを移植後1週間以内に中止できる場合がある。
    condition:
      region: 国際
      study: KDIGO 腎移植レシピエント診療ガイドライン 2009
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-684
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) Transplant Work Group. KDIGO clinical practice guideline for the care of kidney transplant recipients. Am J Transplant. 2009;9 Suppl 3:S1-S155'
    doi: 10.1111/j.1600-6143.2009.02834.x
    pmid: '19845597'
    pmcid: null
    url: https://doi.org/10.1111/j.1600-6143.2009.02834.x
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄、version of record）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本出典は2009年のガイドラインであり、その後に導入された薬剤や現在の日本の標準的なレジメンとの差異は本出典では確認できない。本文に挙げた薬剤（タクロリムス、ミコフェノール酸製剤、インターロイキン2受容体拮抗薬、リンパ球除去薬、副腎皮質ステロイド）について、国内の承認・保険適用は未確認。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-023
  domain: KX
  subdomain: 腎移植の拒絶反応
  assertion:
    plain_statement_ja: 急性拒絶反応が疑われる場合、治療を大きく遅らせる場合を除き、治療開始前に移植腎生検を行うことが勧められる。持続し原因が明らかでない血清クレアチニン上昇がある場合にも移植腎生検が勧められ、移植腎機能の発現が遅れている期間中は7〜10日ごとに生検を行うことが提案される。急性細胞性拒絶反応の初期治療には副腎皮質ステロイドを用い、ステロイドに反応しない場合や再発した場合はリンパ球除去抗体による治療が提案される。抗体関連型の急性拒絶反応では、血漿交換、免疫グロブリン静注、抗CD20抗体、リンパ球除去抗体などの選択肢を用いることが提案される。拒絶反応を起こした患者では、ミコフェノール酸製剤の追加や、アザチオプリンからミコフェノール酸製剤への切り替えが提案される。
    condition:
      region: 国際
      study: KDIGO 腎移植レシピエント診療ガイドライン 2009
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-684
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) Transplant Work Group. KDIGO clinical practice guideline for the care of kidney transplant recipients. Am J Transplant. 2009;9 Suppl 3:S1-S155'
    doi: 10.1111/j.1600-6143.2009.02834.x
    pmid: '19845597'
    pmcid: null
    url: https://doi.org/10.1111/j.1600-6143.2009.02834.x
    source_license: CC BY-NC-ND 4.0（Crossref の license 欄、version of record）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本出典は2009年のガイドラインであり、拒絶反応の分類や治療はその後の改訂で変わっている可能性がある。本文に挙げた薬剤（副腎皮質ステロイド、リンパ球除去抗体、抗CD20抗体、免疫グロブリン製剤、ミコフェノール酸製剤、アザチオプリン）について、国内の承認・保険適用は未確認。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-024
  domain: KX
  subdomain: 腎移植の長期的成績と移植後管理
  assertion:
    plain_statement_ja: 米国では腎移植後の長期成績が改善している。献腎移植では10年移植腎生存率は1996〜1999年の移植で42.3%、2008〜2011年の移植で53.6%に上昇し、10年患者生存率も60.5%から66.9%に上昇した。この改善は、レシピエントの年齢や肥満、糖尿病の増加、ドナー年齢の上昇など不利な条件が増える中でみられたもので、臨床的急性拒絶反応の減少、ウイルス感染の監視と抗ウイルス予防、不適合な生体ドナーとのペア交換移植の利用などが要因として挙げられている。移植後1年以内の移植腎喪失は技術的・血管系の合併症と急性拒絶反応が主な原因であり、長期管理では拒絶の予防と治療に加え、心血管疾患、感染症、悪性腫瘍への対応が重要とされる。
    condition:
      region: 米国
      study: 米国の腎移植登録に基づく長期生存の総説（対象期間1996〜2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-685
    source: 'Hariharan S, Israni AK, Danovitch G. Long-Term Survival after Kidney Transplantation. N Engl J Med. 2021;385(8):729-743'
    doi: 10.1056/NEJMra2014530
    pmid: '34407344'
    pmcid: null
    url: https://doi.org/10.1056/NEJMra2014530
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本論文の収載レコードには抄録が掲載されておらず、記載した数値は本文で直接確認した献腎移植の10年成績に限る。生体腎移植の10年成績は本文の表から確実に判読できなかったため数値を記載していない。米国の成績であり、日本の成績とは異なる可能性がある。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-025
  domain: KX
  subdomain: 腎機能低下時の薬用量調整の原則
  assertion:
    plain_statement_ja: 急性・慢性の腎臓病患者では薬用量の調整が標準的な診療であり、用量調整の指標は糸球体濾過量だが、腎臓病は腎外クリアランスにも影響するため、糸球体濾過量だけでは薬の体内動態を十分に表せない。用量調整は段階的に行い、病歴と臨床情報を集め、糸球体濾過量を推算し、使用中の薬から個別化が必要なものを選び、薬の動態特性と体液量と腎機能に基づいて個別の投与法を計算し、効果と毒性を観察し、反応や腎機能の変化に応じて投与法を見直す。クリアランスの低下で定常状態への到達が遅れるため、半減期の長い薬では負荷量が要ることがあり、分布容積が増大した薬では負荷量の増量が要ることもある。維持量では、用量を変えずに投与間隔を延ばす方法が、最高・最低濃度と曝露量を正常腎機能時と同様に保ちやすい場合がある。
    condition:
      region: 国際
      study: 腎臓病患者の薬用量調整に関する国際会議の臨床アップデート（2011年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-686
    source: 'Matzke GR, Aronoff GR, Atkinson AJ Jr, Bennett WM, Decker BS, et al. Drug dosing consideration in patients with acute and chronic kidney disease—a clinical update from Kidney Disease: Improving Global Outcomes (KDIGO). Kidney Int. 2011;80(11):1122-1137'
    doi: 10.1038/ki.2011.322
    pmid: '21918498'
    pmcid: null
    url: https://doi.org/10.1038/ki.2011.322
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2011年の会議報告に基づく原則であり、個別薬剤ごとの具体的な調整量や、現在の添付文書の記載との一致は確認していない。本カードには特定の薬剤名を挙げていないが、実際に用量調整を行う際の各薬剤の国内の承認・保険適用は未確認で、取り込み時に添付文書で確認が必要である。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-026
  domain: KX
  subdomain: 透析患者の薬物投与
  assertion:
    plain_statement_ja: 血液透析で除去される薬は、次の投与まで有効な血中濃度を保つため、透析後に投与するのが原則である。腎不全に合わせて調整した維持量に、透析で除去された分を補う補充量を透析後に加えることを検討する。透析膜の性能が上がったため、古い研究に基づく推奨量は血液透析の影響を過小評価している可能性があり、用量を経験的に25〜50%増やす必要がある場合がある。低フラックスの膜での研究から得た補充量は、高フラックスの合成膜を用いる場合には経験的に少なくとも50%増やすとされる。治療域の狭い薬では、血中濃度測定を用いて用量を決める。
    condition:
      region: 国際
      study: 腎臓病患者の薬用量調整に関する国際会議の臨床アップデート（2011年）。血液透析時の薬用量に関する推奨
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-686
    source: 'Matzke GR, Aronoff GR, Atkinson AJ Jr, Bennett WM, Decker BS, et al. Drug dosing consideration in patients with acute and chronic kidney disease—a clinical update from Kidney Disease: Improving Global Outcomes (KDIGO). Kidney Int. 2011;80(11):1122-1137'
    doi: 10.1038/ki.2011.322
    pmid: '21918498'
    pmcid: null
    url: https://doi.org/10.1038/ki.2011.322
    source_license: Elsevier の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典自体が、あらゆる腎代替療法の形態について薬物動態の研究が不十分だと指摘しており、個別薬剤ごとの透析性（除去率）の数値はこの出典では確認していない。2011年の報告であり、その後のダイアライザや透析条件の変化は反映されていない。出典で血中濃度測定の例として挙がるアミノグリコシド系薬やバンコマイシンなどの国内の承認・保険適用は未確認で、取り込み時に添付文書で確認が必要である。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-027
  domain: KX
  subdomain: 造影剤と腎機能低下例での薬剤選択
  assertion:
    plain_statement_ja: 造影剤による腎障害の最も重要な危険因子は慢性腎臓病であり、推算糸球体濾過量が60 mL/min/1.73m²未満でリスクが上がり、値が低いほどリスクは高くなる。予防では、腎機能低下のある患者をあらかじめ見分け、腎毒性のある薬（非ステロイド性抗炎症薬など）とメトホルミンを造影剤投与の前に中止し、造影剤は可能な限り最少量を用い、高浸透圧造影剤を避けて低浸透圧または等浸透圧の造影剤を選ぶ。手技の前後を通じた十分な補液が、最も確実な予防策とされる。
    condition:
      region: 国際
      study: 造影剤腎症の予防に関する総説（2014年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-687
    source: 'Ludwig U, Keller F. Prophylaxis of Contrast-Induced Nephrotoxicity. Biomed Res Int. 2014;2014:308316'
    doi: 10.1155/2014/308316
    pmid: '24812612'
    pmcid: PMC4000949
    url: https://doi.org/10.1155/2014/308316
    source_license: CC BY 3.0（Crossref の license 欄と PMC 掲載ページの表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 2014年の総説に基づく記載で、メトホルミンの休薬や再開の具体的な基準（腎機能の値や期間）は出典のまとめでは数値で示されておらず確認していない。その後の国内外のガイドライン改訂による推奨の変化も確認していない。非ステロイド性抗炎症薬とメトホルミンの国内の承認・保険適用は未確認で、取り込み時に添付文書で確認が必要である。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-028
  domain: KX
  subdomain: 透析患者の感染症とワクチン
  assertion:
    plain_statement_ja: 透析患者は免疫機能の低下のためB型肝炎ウイルスの感染リスクが高い。日本の2施設の前向き観察研究では、進行した慢性腎臓病の患者113例（非透析63例、維持血液透析50例）にB型肝炎ワクチン10マイクログラムを0、1、6か月の3回接種し、3回目の1〜3か月後にB型肝炎表面抗原に対する抗体が10 IU/mL以上となった割合は、血液透析患者で54.2%、非透析患者で64.3%と、両群に有意な差はなかった。この標準的な接種方法では抗体獲得が十分とはいえず、より高用量の接種や新しい世代のワクチン、より早い慢性腎臓病の段階での接種など、より有効な方法が必要とされた。
    condition:
      region: 日本
      study: 2021〜2024年に2施設で行われた前向き観察研究（進行した慢性腎臓病113例。ワクチン3回接種後の抗体陽転率を比較）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-688
    source: 'Fujikura T, Isobe S, Oikawa S, Ishigaki S, Katahashi N, et al. Comparison of seroconversion rates after hepatitis B vaccination in patients with advanced chronic kidney disease and those receiving maintenance hemodialysis. Clin Exp Nephrol. 2025;29(8):1045-1052'
    doi: 10.1007/s10157-025-02648-1
    pmid: '40035977'
    pmcid: null
    url: https://doi.org/10.1007/s10157-025-02648-1
    source_license: Springer の TDM 用ライセンスのみ（Crossref の license 欄。CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 単一の観察研究（2施設、113例）の結果であり、接種したワクチンの製品名は抄録では確認していない。B型肝炎ワクチンの国内の承認・保険適用は未確認で、取り込み時に添付文書で確認が必要である。B型肝炎以外の感染症（肺炎球菌、インフルエンザなど）に対するワクチンの効果や、透析患者の感染症の頻度の数値は、この出典では確認していない。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-029
  domain: KX
  subdomain: 先行的腎移植
  assertion:
    plain_statement_ja: 先行的腎移植は、維持透析を始める前に行う腎移植であり、成人を対象に透析後に移植した群と比較した観察研究76件の系統的レビューとメタ解析では、先行群で全死亡の調整ハザード比が0.78、死亡で打ち切った移植腎喪失の調整ハザード比が0.81と、いずれも低かった。一方、心血管疾患、急性拒絶反応、サイトメガロウイルス感染、尿路感染の未調整リスク比は両群で同程度であり、死亡と移植腎喪失に関する証拠の確実性は中程度、その他の転帰では非常に低かったと評価されている。
    condition:
      region: 国際
      study: 成人の先行的移植と透析後移植を比較した観察研究の系統的レビュー・メタ解析（76件、登録年1968〜2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-689
    source: 'Azegami T, Kounoue N, Sofue T, et al. Efficacy of pre-emptive kidney transplantation for adults with end-stage kidney disease: a systematic review and meta-analysis. Ren Fail. 2023;45(1):2169618'
    doi: 10.1080/0886022X.2023.2169618
    pmid: '36705051'
    pmcid: PMC9888453
    url: https://doi.org/10.1080/0886022X.2023.2169618
    source_license: CC BY 4.0（誌面の表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 対象はすべて観察研究で無作為化試験はなく、先行群に状態のよい患者が集まる選択バイアスなどの残余交絡を否定できないため、差が先行という時期そのものによるものかは確定しない。小児のみの研究と多臓器同時移植は出典の対象外である。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-030
  domain: KX
  subdomain: ABO血液型不適合腎移植
  assertion:
    plain_statement_ja: 日本では献腎の不足を背景に、1989年からABO血液型不適合の生体腎移植が行われてきた。1989年1月から2001年12月までにこの移植を受けた441例では、患者生存率が移植後1年93％、3年89％、5年87％、7年85％、9年84％、移植腎生着率がそれぞれ84％、80％、71％、65％、59％であった。移植腎生着率は29歳以下で30歳以上より高く、抗凝固療法を受けた群で受けなかった群より高かった。A型不適合とB型不適合の間で転帰に有意差はなく、移植後1年の移植腎生着率は生体腎移植の歴史的対照1055例よりわずかに低かったが有意差はなかった。
    condition:
      region: 日本
      study: 日本のABO不適合生体腎移植441例の集計と生体腎移植の歴史的対照1055例との比較（対象期間1989〜2001年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-690
    source: 'Takahashi K, Saito K, Takahara S, et al.; Japanese ABO-Incompatible Kidney Transplantation Committee. Excellent long-term outcome of ABO-incompatible living donor kidney transplantation in Japan. Am J Transplant. 2004;4(7):1089-1096'
    doi: 10.1111/j.1600-6143.2004.00464.x
    pmid: '15196066'
    pmcid: null
    url: https://doi.org/10.1111/j.1600-6143.2004.00464.x
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 対象は1989〜2001年の症例であり、当時の免疫抑制療法や脾摘を含む前処置は現在の方法と異なるため、現在の成績へそのまま当てはめることはできない。この移植で用いる免疫抑制薬などについて、国内の承認・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-031
  domain: KX
  subdomain: 移植後の感染症スクリーニングと予防
  assertion:
    plain_statement_ja: 腎移植後のウイルス感染症対策では、スクリーニングと予防投与を病原体ごとに組み合わせる。BKウイルスについては、全ての腎移植レシピエントで血漿の定量的核酸検査によるスクリーニングを、移植後最初の3〜6か月は毎月、その後は移植後1年が終わるまで3か月ごとに行い、原因不明の血清クレアチニン上昇時と急性拒絶反応の治療後にも行うことが提案され、血漿のウイルス量が持続的に10000コピー毎ミリリットルを超える場合は免疫抑制薬の減量が提案されている。サイトメガロウイルスについては、ドナーとレシピエントの双方が血清学的に陰性の場合を除き、経口ガンシクロビルまたはバルガンシクロビルによる予防を移植後少なくとも3か月間行い、T細胞除去抗体による治療の後は6週間行うことが推奨されている。
    condition:
      region: 国際
      study: 腎移植レシピエント診療に関する国際ガイドライン（ウイルス疾患の章）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-684
    source: 'Kidney Disease: Improving Global Outcomes (KDIGO) Transplant Work Group. KDIGO clinical practice guideline for the care of kidney transplant recipients. Am J Transplant. 2009;9 Suppl 3:S1-S155'
    doi: 10.1111/j.1600-6143.2009.02834.x
    pmid: '19845597'
    pmcid: null
    url: https://doi.org/10.1111/j.1600-6143.2009.02834.x
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードはガイドラインのウイルス疾患の章で本文を確認できたBKウイルスとサイトメガロウイルスの範囲に限り、エプスタイン・バーウイルスや単純ヘルペスウイルス、水痘帯状疱疹ウイルス、細菌・真菌感染症の推奨は含めていない。2009年のガイドラインであり、その後の改訂や新しい知見は反映されていない。予防に用いるガンシクロビル、バルガンシクロビルおよび免疫抑制薬について、国内の承認・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: KX-032
  domain: KX
  subdomain: 高齢者の腎代替療法の選択と保存的管理
  assertion:
    plain_statement_ja: 高齢の進行した慢性腎臓病では、透析と保存的腎臓管理のどちらを選ぶかで生存と生活の質の見通しが異なる。ステージ5の慢性腎臓病を対象に保存的管理と透析を比較した観察研究25件の系統的レビューでは、全体として保存的管理を選んだ患者の生存期間は透析を選んだ患者より短かったが、80歳以上の患者と併存症の多い高齢者では透析の生存上の利点はあいまいになり失われる可能性が示された。一方、生活の質、症状負担、入院、死亡の場所については保存的管理に利点がありうるとされた。このため高齢やフレイルのある患者では、透析と保存的管理のどちらも選択肢として提示し、併存疾患や本人の価値観を踏まえて共同で決めることが求められる。
    condition:
      region: 国際
      study: 保存的腎臓管理と透析を比較した観察研究25件の系統的レビュー（2021年、80歳以上のサブグループと併存症の多い高齢者を含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-680
    source: 'Buur LE, Madsen JK, Eidemak I, Krarup E, Lauridsen TG, Taasti LH, Finderup J. Does conservative kidney management offer a quantity or quality of life benefit compared to dialysis? A systematic review. BMC Nephrol. 2021;22:307'
    doi: 10.1186/s12882-021-02516-6
    pmid: '34507554'
    pmcid: PMC8434727
    url: https://doi.org/10.1186/s12882-021-02516-6
    source_license: CC BY 4.0（PMC ページの Open Access 表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 対象研究はすべて観察研究で研究間の異質性が大きく、透析に有利な方向のバイアスが指摘されている。フレイルを指標として直接測定した比較は出典では確認できなかったため、フレイルそのものの数値は記載していない。症状緩和に用いる個別の薬剤名は本カードに記載しておらず、その国内の承認・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応の一覧

| カードID | 出題基準 | コアカリ |
|---|---|---|
| KF-001 | 医学各論 Ⅷ-3-A-①（急性腎障害(腎前性・腎性・腎後性)、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q) |
| KF-002 | 医学各論 Ⅷ-3-A-①（急性腎障害(腎前性・腎性・腎後性)、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q) |
| KF-003 | 医学各論 Ⅷ-3-A-①（急性腎障害(腎前性・腎性・腎後性)、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q) |
| KF-004 | 医学各論 Ⅷ-3-A-①（急性腎障害(腎前性・腎性・腎後性)、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q) |
| KF-005 | 医学各論 Ⅷ-3-A-①（急性腎障害(腎前性・腎性・腎後性)、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q) |
| KF-006 | 医学各論 Ⅷ-3-A-②（急性尿細管壊死、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q) |
| KF-007 | 医学各論 Ⅷ-3-A-②（急性尿細管壊死、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-311 (id: Jlvnl8Q) |
| KF-008 | 医学各論 Ⅷ-3-A-③（横紋筋融解症、a） | PS-02-09-05 (id: JkxnuRs) |
| KF-009 | 医学各論 Ⅷ-3-A-③（横紋筋融解症、a） | PS-02-09-05 (id: JkxnuRs) |
| KF-010 | 医学各論 Ⅷ-3-A-④（溶血性尿毒症症候群<HUS>、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-426 (id: JlvnmHQ) |
| KF-011 | 医学各論 Ⅷ-3-A-④（溶血性尿毒症症候群<HUS>、a） | PS-02-09-05 (id: JkxnuRs) |
| KF-012 | 医学各論 Ⅷ-3-A-④（溶血性尿毒症症候群<HUS>、a） | PS-02-09-05 (id: JkxnuRs) |
| KF-013 | 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-014 | 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-015 | 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-016 | 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-017 | 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-018 | 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-019 | 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-020 | 医学各論 Ⅷ-3-B（慢性腎臓病<CKD>、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-021 | 医学各論 Ⅷ-3-C-①（腎性貧血、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-022 | 医学各論 Ⅷ-3-C-①（腎性貧血、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-023 | 医学各論 Ⅷ-3-C-①（腎性貧血、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-024 | 医学各論 Ⅷ-3-C-②（CKD-MBD、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-025 | 医学各論 Ⅷ-3-C-②（CKD-MBD、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-026 | 医学各論 Ⅷ-3-C-②（CKD-MBD、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-027 | 医学各論 Ⅷ-3-D-①（透析アミロイドーシス、c） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-312 (id: Jlvnl8U) |
| KF-028 | 医学各論 Ⅷ-3-E-①（脱水と浮腫、a） | PS-02-09-05 (id: JkxnuRs)；TBL-02-08-013 (id: JlAKpmo)；TBL-02-08-009 (id: JlAKpmk) |
| KF-029 | 医学各論 Ⅷ-3-E-②（ナトリウム代謝異常、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-314 (id: Jlvnl8g) |
| KF-030 | 医学各論 Ⅷ-3-E-②（ナトリウム代謝異常、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-314 (id: Jlvnl8g) |
| KF-031 | 医学各論 Ⅷ-3-E-②（ナトリウム代謝異常、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-314 (id: Jlvnl8g) |
| KF-032 | 医学各論 Ⅷ-3-E-③（カリウム代謝異常、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-315 (id: Jlvnl8o) |
| KF-033 | 医学各論 Ⅷ-3-E-③（カリウム代謝異常、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-315 (id: Jlvnl8o) |
| KF-034 | 医学各論 Ⅷ-3-E-④（カルシウム代謝異常、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-316 (id: Jlvnl8s) |
| KF-035 | 医学各論 Ⅷ-3-E-④（カルシウム代謝異常、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-316 (id: Jlvnl8s) |
| KF-036 | 医学各論 Ⅷ-3-E-⑤（リン代謝異常、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-317 (id: Jlvnl80) |
| KF-037 | 医学各論 Ⅷ-3-E-⑥（マグネシウム代謝異常、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-318 (id: Jlvnl84) |
| KF-038 | 医学各論 Ⅷ-3-F-①（代謝性アシドーシス、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-319 (id: Jlvnl9A) |
| KF-039 | 医学各論 Ⅷ-3-F-①（代謝性アシドーシス、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-319 (id: Jlvnl9A) |
| KF-040 | 医学各論 Ⅷ-3-F-②（代謝性アルカローシス、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-320 (id: Jlvnl9I) |
| KX-001 | null | PS-02-09-02 (id: JkxnuRg)；TBL-02-08-009 (id: JlAKpmk) |
| KX-002 | null | PS-02-09-02 (id: JkxnuRg)；TBL-02-08-012 (id: JlAKpms) |
| KX-003 | null | PS-02-09-02 (id: JkxnuRg)；TBL-02-08-012 (id: JlAKpms) |
| KX-004 | null | PS-02-09-02 (id: JkxnuRg)；TBL-02-08-012 (id: JlAKpms) |
| KX-005 | null | PS-02-09-02 (id: JkxnuRg)；TBL-02-08-010 (id: JlAKpmc) |
| KX-006 | null | PS-02-09-03 (id: JkxnuRk)；TBL-02-08-011 (id: JlAKpmg) |
| KX-007 | null | PS-02-09-03 (id: JkxnuRk)；TBL-02-08-015 (id: JlAKpm0) |
| KX-008 | null | PS-02-09-03 (id: JkxnuRk)；TBL-02-08-015 (id: JlAKpm0) |
| KX-009 | null | PS-02-09-03 (id: JkxnuRk)；TBL-02-08-015 (id: JlAKpm0) |
| KX-010 | null | PS-02-09-03 (id: JkxnuRk)；TBL-02-08-017 (id: JlAKpm8) |
| KX-011 | null | PS-02-09-03 (id: JkxnuRk)；TBL-02-08-016 (id: JlAKpm4) |
| KX-012 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-013 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-014 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-015 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-016 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-017 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-018 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-019 | null | PS-02-09-05 (id: JkxnuRs)；PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-020 | null | PS-02-09-05 (id: JkxnuRs)；PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-021 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-022 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-023 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-024 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-025 | null | PS-02-09-04 (id: JkxnuRo) |
| KX-026 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-027 | null | PS-02-09-04 (id: JkxnuRo) |
| KX-028 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-029 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-030 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-031 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |
| KX-032 | null | PS-02-09-04 (id: JkxnuRo)；TBL-02-08-019 (id: JlAKpnE) |

## 4. 未解決事項

- スキーマと接頭辞（担当：取り込み側）：接頭辞 KF・KX は手元のスキーマと domains.yaml に未追加。取り込み時に追加が必要。
- 識別子が片方 null の出典（担当：取り込み側で再確認）：SRC-653（透析アミロイドーシス、DOI null）、SRC-665（浮腫の総説、DOI null。PMID は確認済み）、SRC-649（腎性貧血ガイドライン2015年版の英語版、PMID null。ライセンスも未確認で UNKNOWN）、SRC-676（日本透析医学会 JRDR 2022年次報告、PMID null）。
- ライセンス UNKNOWN：SRC-649、SRC-661（リン調節の総説）。SRC-684（KDIGO 腎移植ガイドライン2009）は Crossref の license 欄で CC BY-NC-ND を確認し RESTRICTED としたが、誌面表示の再確認と、2009年版であることによる現在の推奨との差異確認が取り込み側に残る。SRC-681・682 は PMCID を確認できず null とした。
- 薬剤の国内承認・保険適用（担当：取り込み側で PMDA 確認）：KF-004、009、012、018（SGLT2阻害薬）、019（パチロマーは優先確認）、020、022、023、025、032〜035、039、KX-001、003、009（シスタチン C 測定の保険適用条件）、016、019、020、022、023、025〜028、030、031 は、各カードの uncertainty に「未確認」と明記した。
- 版の新旧（担当：取り込み側）：KF-014・017 は CKD 診療ガイドライン2018年版に基づくため、2023年版との差異確認が必要。KF-015 の疫学数値は2005年の健診データに基づく推計。KX-025〜027 の出典は2011年・2014年の総説が基盤で、個別薬剤の調整量やメトホルミンの腎機能基準は現在の添付文書での補完が望ましい。
- 数値を入れなかった項目（一次資料で確定できず）：KF-010（STEC 感染後の HUS 発症割合）、KF-011（非典型 HUS の遺伝子別頻度）、KF-021（腎性貧血の診断の Hb の線引き）、KF-029（高張食塩水の具体的投与量）、KF-037（Mg 異常の濃度による定義値）、KF-040（尿中クロライド閾値 20 mEq/L は二次資料のみ）。KF-026 の日本の CKD-MBD 管理目標値は二次資料経由の確認で、各カードの uncertainty に明記した。
- 追加カードの候補（識別子確認済み・今回の枠外）：AKI 後の急性腎臓病（AKD）の枠組みは ADQI 16 コンセンサス（Nat Rev Nephrol 2017、DOI 10.1038/nrneph.2017.2、PMID 28239173）を出典に作れる。KX-005 の血尿の診断精度は Stark ら（Glomerular Diseases 2025、DOI 10.1159/000545051、PMID 40406196）、KX-009 のシスタチン C 推算式は Inker ら（NEJM 2012、DOI 10.1056/NEJMoa1114248、PMID 22762315）を出典に補える。AKI の腎代替療法の開始時期は KF-005（STARRT-AKI）で扱ったため、KX-015 は中毒の体外除去に絞ってある。KX-013（HD・PD 比較）は糖尿病性腎不全に限られるメタ解析が出典で、一般集団の出典が確保できれば差し替えを検討されたい。KX-021 は登録集計報告そのもの（DOI・PMID を照合できず）を使わず推計研究を採用した。KX-028 は B型肝炎ワクチンの単一観察研究のみで記載した。

## 5. 次回への引き継ぎ

- 欠番：なし（KF-001〜040、KX-001〜032 は連番）。未使用 SRC：SRC-639（KDIGO 2024 の重複のため SRC-573 に統合）、SRC-645〜648、SRC-670（同・統合）。番号は詰めていない。
- カードのない出題基準の小項目：KF の範囲（Ⅷ-3）にはない。KX は方針どおり全件 kokushi: null。
- 第17回との境界：尿路結石の画像は KX-011 で検査の選択として触れたが、結石の診断・治療そのものは第17回 UR で扱う。排尿障害の症候評価（KX-004）と、前立腺肥大症・過活動膀胱などの疾患は第17回 GU・UR で重複しないよう疾患側に絞る。
- 扱った出典の中心：KDIGO（AKI 要約、CKD-MBD、腎移植）、日本腎臓学会・日本透析医学会関連（CKD 診療ガイドライン2018、腎性貧血ガイドライン2015、JRDR 年次報告、eGFR 推算式）、主要 RCT（PRESERVE、STARRT-AKI、EMPA-KIDNEY、FIDELIO-DKD、OPAL-HK）。KDIGO 2024 CKD ガイドラインは既存の SRC-573 を使うこと（新しい番号を付けない）。
