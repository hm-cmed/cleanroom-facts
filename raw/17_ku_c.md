# 腎・泌尿器・生殖器 第17回：尿路の結石・閉塞・炎症・形態異常・損傷（UR-001〜034）と尿路・男性生殖器の腫瘍・男性生殖器疾患（GU-001〜039）

- 作成日：2026-10-28
- 事実票：73件（UR 34件、GU 39件）。目標の60〜90件の範囲内。ID は接頭辞ごとに 001 からの連番で、欠番はない。全件 `status: draft`、`verifier: null`。
- カバー：対象の出題基準55項目すべてにカードがあり、レベル a の38項目（UR 19項目、GU 19項目）はすべて1件以上ある。
- 出典マスター：新規 SRC-691〜750 のうち 55件を使用。未使用は SRC-705、706、720 と、重複統合で空いた SRC-707、740（番号は詰めていない）。
- 重複出典の統合（こちらで実施）：CDC の性感染症治療ガイドライン2021（MMWR）に SRC-703・707・740 の3番号が付きかけていたため、最も小さい SRC-703 に統一した（対象：UR-016、UR-019〜022、GU-024）。また UR 分担では出典表と YAML の `source_class` に出典の種類（review 等）が入っていたため、ライセンス区分（OPEN・RESTRICTED 等）に機械的に直し、`source_license` に表示テキストを入れた。
- 形式の統一（こちらで実施）：GU-020 の kokushi の項目名を出題基準表の正式名称「精巣癌(非セミノーマ)」に、GU-021 の kokushi にレベル（a）を補った。
- 検証（こちらで実施済み）：YAML の構文解析を通過。スキーマ検証は、接頭辞 UR・GU を検証用に加えた条件でエラー0（接頭辞の追加は取り込み側の作業）。`condition.region` は全73件に記載。DOI のある52件はすべて Crossref で解決し、DOI・PMID の対応に不一致はなかった。PMID は全出典で確認できた。DOI が null の出典は3件（SRC-728 尿膜管癌総説、SRC-737 精巣癌総説、SRC-749 精巣・精索水瘤の総説）で、理由を出典表と各カードに明記した。
- 境界：尿路感染症は尿路感染症としての診断と治療に絞り、性感染症は CDC 2021（米国）の推奨を地域明記で扱った。排尿障害の症候評価は第16回 KX-004 で扱ったため、本回は疾患側（前立腺肥大症・過活動膀胱・尿失禁）に絞った。
- 取り込み想定：YAML ブロックは1つで、アンカー・マージキー・脚注番号・`basis_tag`・仮IDは使っていない。主張文はすべて自作文である（legal_basis はすべて B）。

## 1. 抽出元ホワイトリスト（出典マスター、新規 SRC）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 使用カード |
|---|---|---|---|---|---|---|---|
| SRC-691 | Skolarikos A, et al. EAU Guidelines on Urolithiasis. European Urology. 2025;88(1):64-75. | 10.1016/j.eururo.2025.03.011 | 40268592 | ガイドライン（RESTRICTED） | RESTRICTED | 索引情報で DOI・PMID を照合し、ガイドライン本文で数値を確認 | UR-001 |
| SRC-692 | Hollingsworth JM, et al. Alpha blockers for treatment of ureteric stones: systematic review and meta-analysis. BMJ. 2016;355:i6112. | 10.1136/bmj.i6112 | 27908918 | 未確認（UNKNOWN） | UNKNOWN | 抄録および引用文献情報で DOI・PMID を照合 | UR-002 |
| SRC-693 | Borghi L, Meschi T, Amato F, Briganti A, Novarini A, Giannini A. Urinary volume, water and recurrences in idiopathic calcium nephrolithiasis: a 5-year randomized prospective study. Journal of Urology. 1996;155(3):839-843. | 10.1016/S0022-5347(01)66321-3 | 8583588 | 未確認（UNKNOWN） | UNKNOWN | 引用文献リストで DOI を確認し、PMID は索引情報で照合。結果数値は本試験を引用した総説本文で確認 | UR-003 |
| SRC-694 | Jung JH, Park J, Kim WT, Kim HW, Kim HJ, Hong S, et al. The association of benign prostatic hyperplasia with lower urinary tract stones in adult men: a retrospective multicenter study. Asian Journal of Urology. 2018;5(2):118-121. | 10.1016/j.ajur.2017.06.008 | 29736374 | CC BY-NC-ND 4.0（RESTRICTED） | RESTRICTED | PMC 掲載ページで PMID・PMCID・ライセンス表記を確認し、引用文献情報で DOI を照合 | UR-004 |
| SRC-695 | Yaxley J, Yaxley W. Obstructive uropathy – acute and chronic medical management. World Journal of Nephrology. 2023;12(1):1-9. | 10.5527/wjn.v12.i1.1 | 36704657 | CC BY-NC 4.0（RESTRICTED） | RESTRICTED | PMC 掲載ページで PMID・PMCID・ライセンス表記・書誌・DOI を確認 | UR-005, UR-006, UR-007 |
| SRC-696 | Liao L. Evaluation and Management of Neurogenic Bladder: What Is New in China? International Journal of Molecular Sciences. 2015;16(8):18580-18600. | 10.3390/ijms160818580 | 26266405 | CC BY 4.0（OPEN） | OPEN | PMC 掲載ページで PMID・PMCID・ライセンス表記を確認し、出版社情報で DOI・ページを照合 | UR-008, UR-009 |
| SRC-697 | Goulin J, Demède D, Ranchin B, Mosca M, De-Mul A, Bidault Jourdainne V. What paediatricians need to know about modern urologic management of vesicoureteral reflux. Frontiers in Pediatrics. 2025;13:1607019. | 10.3389/fped.2025.1607019 | 40641902 | CC BY（OPEN） | OPEN | PMC 掲載ページで PMID・PMCID・CC BY 表記を確認し、出版社ページで書誌・DOI を照合 | UR-010, UR-018 |
| SRC-698 | RIVUR Trial Investigators; Hoberman A, Greenfield SP, Mattoo TK, et al. Antimicrobial prophylaxis for children with vesicoureteral reflux. New England Journal of Medicine. 2014;370(25):2367-2376. | 10.1056/NEJMoa1401811 | 24795142 | 未確認（UNKNOWN） | UNKNOWN | 抄録で結果を確認し、引用文献情報で DOI・PMID・PMCID を照合 | UR-011 |
| SRC-699 | Lee DG, Jeon SH, Lee CH, Lee SJ, Kim JI, Chang SG. Acute Pyelonephritis: Clinical Characteristics and the Role of the Surgical Treatment. Journal of Korean Medical Science. 2009;24(2):296-301. | 10.3346/jkms.2009.24.2.296 | 19399273 | CC BY-NC 3.0（RESTRICTED） | RESTRICTED | PMC 掲載ページで PMID・PMCID・ライセンス表記・書誌・DOI を確認 | UR-012 |
| SRC-700 | van Nieuwkoop C, van der Starre WE, Stalenhoef JE, et al. Treatment duration of febrile urinary tract infection: a pragmatic randomized, double-blind, placebo-controlled non-inferiority trial in men and women. BMC Medicine. 2017;15:70. | 10.1186/s12916-017-0835-3 | 28366170 | CC BY 4.0（OPEN） | OPEN | PMC 掲載ページおよび索引情報で PMID・PMCID・DOI・ライセンスを確認 | UR-013 |
| SRC-701 | Gupta K, Hooton TM, Naber KG, et al. International clinical practice guidelines for the treatment of acute uncomplicated cystitis and pyelonephritis in women: a 2010 update by the Infectious Diseases Society of America and the European Society for Microbiology and Infectious Diseases. Clinical Infectious Diseases. 2011;52(5):e103-e120. | 10.1093/cid/ciq257 | 21292654 | ガイドライン（RESTRICTED） | RESTRICTED | ガイドライン本文で推奨内容を確認し、引用文献情報で DOI・PMID を照合 | UR-014 |
| SRC-702 | Anger J, Lee U, Ackerman AL, et al. Recurrent Uncomplicated Urinary Tract Infections in Women: AUA/CUA/SUFU Guideline. Journal of Urology. 2019;202(2):282-289. | 10.1097/JU.0000000000000296 | 31042112 | ガイドライン（RESTRICTED） | RESTRICTED | 索引情報で DOI・PMID・書誌を照合し、ガイドライン要約で声明内容を確認 | UR-015 |
| SRC-703 | Workowski KA, Bachmann LH, Chan PA, et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recommendations and Reports. 2021;70(4):1-187. | 10.15585/mmwr.rr7004a1 | 34292926 | 米国政府資料（GOV_US） | GOV_US | PMC 収載記録および発行機関の引用情報で DOI・PMID・PMCID を照合し、本文で推奨内容を確認 | UR-016 |
| SRC-704 | Lee SH, Jung HJ, Mah SY, Chung BH. Renal Abscesses Measuring 5 cm or Less: Outcome of Medical Treatment without Therapeutic Drainage. Yonsei Medical Journal. 2010;51(4):569-573. | 10.3349/ymj.2010.51.4.569 | 20499424 | CC BY-NC 3.0（RESTRICTED） | RESTRICTED | PMC 掲載ページで PMID・PMCID・ライセンス表記・書誌・DOI を確認 | UR-017 |
| SRC-708 | Yener S, Pehlivanoğlu C, Akıs Yıldız Z, Ilce HT, Ilce Z. Duplex Kidney Anomalies and Associated Pathologies in Children: A Single-Center Retrospective Review. Cureus. 2022;14(6):e25777 | 10.7759/cureus.25777 | 35812643 | CC BY（PMC 掲載ページの表示） | OPEN | PMC 本文（PMCID: PMC9270195）で症例数・症状・合併異常の数値を確認し、DOI・PMID・PMCID を照合 | UR-023 |
| SRC-709 | Ahmed S, Morris LL, Byard RW. Ectopic ureter with complete ureteric duplication in the female child. J Pediatr Surg. 1992;27(11):1455-1460 | 10.1016/0022-3468(92)90199-h | 1479509 | 出版社の著作物（CC の表示を確認できず） | UNKNOWN | 抄録で症例数・症状・術式・転帰を確認し、DOI・PMID を照合。ライセンス表示は出版社ページで確認できなかったため UNKNOWN | UR-024 |
| SRC-710 | American College of Obstetricians and Gynecologists. Pelvic Organ Prolapse: ACOG Practice Bulletin, Number 214. Obstet Gynecol. 2019;134(5):e126-e142 | 10.1097/AOG.0000000000003519 | 31651832 | 出版社の著作物（CC の表示なし） | RESTRICTED | 抄録で生涯手術リスク・症状ピーク年齢・2050年予測を確認し、DOI・PMID を照合 | UR-025 |
| SRC-711 | Terada N, Ichioka K, Matsuta Y, Okubo K, Yoshimura K, Arai Y. The natural history of simple renal cysts. J Urol. 2002;167(1):21-23 | 10.1016/S0022-5347(05)65373-6 | 11743266 | 出版社の著作物（CC の表示を確認できず） | UNKNOWN | 抄録で健診コホートの頻度・年齢分布・増大速度を確認し、DOI・PMID を照合。ライセンス表示は確認できなかったため UNKNOWN | UR-026 |
| SRC-712 | Reiterová J, Tesař V. Autosomal Dominant Polycystic Kidney Disease: From Pathophysiology of Cystogenesis to Advances in the Treatment. Int J Mol Sci. 2022;23(6):3317 | 10.3390/ijms23063317 | 35328738 | CC BY 4.0（PMC 掲載ページの表示） | OPEN | PMC 本文（PMCID: PMC8949594）で有病率・原因遺伝子・トルバプタンの記載を確認し、DOI・PMID・PMCID を照合 | UR-027 |
| SRC-713 | Nechita OC, Badescu D, Popescu RI, Aurelian J, Constantin TC, Toma CV, Jinga V, Geavlete B. Reviewing the complexities of horseshoe kidney: insights into embryogenesis and surgical considerations. J Med Life. 2025;18(1):10-19 | 10.25122/jml-2024-0325 | 40071162 | CC BY 4.0（誌面の表示） | OPEN | PMC 本文（PMCID: PMC11891615）で下極癒合の割合・峡部の性状・頻度を確認し、DOI・PMID・PMCID を照合 | UR-028 |
| SRC-714 | Iscaife A, dos Anjos G, Barbosa Neto C, Nahas WC, Srougi M, Antunes AA. The role of bladder diverticula in the prevalence of acute urinary retention in patients with BPH who are candidates to surgery. Int Braz J Urol. 2018;44(4):765-770 | 10.1590/S1677-5538.IBJU.2017.0605 | 29617085 | CC BY（PMC 掲載ページの表示） | OPEN | PMC 抄録・本文（PMCID: PMC6092655）で47例の憩室径と尿閉の関係を確認し、DOI・PMID・PMCID を照合 | UR-029 |
| SRC-715 | DiBianco JM, Morley C, Al-Omar O. Nocturnal enuresis: A topic review and institution experience. Avicenna J Med. 2014;4(4):77-86 | 10.4103/2231-0770.140641 | 25506580 | CC BY-NC-SA 3.0（PMC 掲載ページの表示） | RESTRICTED | PMC 本文（PMCID: PMC4251068）で頻度・性比・一次／二次の定義・病態・第一選択治療を確認し、DOI・PMID・PMCID を照合 | UR-030 |
| SRC-716 | Lightner DJ, Gomelsky A, Souter L, Vasavada SP. Diagnosis and Treatment of Overactive Bladder (Non-Neurogenic) in Adults: AUA/SUFU Guideline Amendment 2019. J Urol. 2019;202(3):558-563 | 10.1097/JU.0000000000000309 | 31039103 | 出版社の著作物（CC の表示なし） | RESTRICTED | ガイドラインの推奨（初期評価と治療の段階）を確認し、DOI・PMID を照合 | UR-031 |
| SRC-717 | Ford AA, Rogerson L, Cody JD, Aluko P, Ogah JA. Mid-urethral sling operations for stress urinary incontinence in women. Cochrane Database Syst Rev. 2017;(7):CD006375 | 10.1002/14651858.CD006375.pub4 | 28756647 | 出版社の著作物（コクラン、CC の表示なし） | RESTRICTED | 抄録で試験数・参加者数・短期の客観的／主観的治癒率を確認し、DOI・PMID・PMCID（PMC6483329）を照合 | UR-032 |
| SRC-718 | Coccolini F, Moore EE, Kluger Y, et al; WSES-AAST Expert Panel. Kidney and uro-trauma: WSES-AAST guidelines. World J Emerg Surg. 2019;14:54 | 10.1186/s13017-019-0274-x | 31827593 | CC BY（出版社ページの表示） | OPEN | 抄録で外傷の頻度・管理の原則・小児の非手術的管理を確認し、DOI・PMID・PMCID（PMC6886230）を照合 | UR-033 |
| SRC-719 | Naidu K, Chung A, Mulcahy M. An unusual urethral foreign body. Int J Surg Case Rep. 2013;4(11):1052-1054 | 10.1016/j.ijscr.2013.07.017 | 24055017 | CC BY-NC-ND（PMC 掲載ページの表示） | RESTRICTED | PMC 本文（PMCID: PMC3825963）で挿入動機・摘出法・遅発性合併症を確認し、DOI・PMID・PMCID を照合 | UR-034 |
| SRC-721 | Hsieh JJ, Purdue MP, Signoretti S, et al. Renal cell carcinoma. Nat Rev Dis Primers. 2017;3:17009 | 10.1038/nrdp.2017.9 | 28276433 | 出版社（Springer Nature）の著作物（CC の表示なし） | RESTRICTED | PubMed・PMC（PMC5936048）で抄録と DOI・PMID・PMCID を照合 | GU-001, GU-003 |
| SRC-722 | Motzer RJ, Tannir NM, McDermott DF, et al. Nivolumab plus Ipilimumab versus Sunitinib in Advanced Renal-Cell Carcinoma. N Engl J Med. 2018;378(14):1277-1290 | 10.1056/NEJMoa1712126 | 29562145 | 出版社（NEJM）の著作物（CC の表示なし） | RESTRICTED | PubMed で抄録と数値を確認、PMC5972549 で照合 | GU-002 |
| SRC-723 | Rouprêt M, Seisen T, Birtle AJ, et al. European Association of Urology Guidelines on Upper Urinary Tract Urothelial Carcinoma: 2023 Update. Eur Urol. 2023;84(1):49-64 | 10.1016/j.eururo.2023.03.013 | 36967359 | 欧州泌尿器科学会（EAU）のガイドライン、Elsevier 掲載（CC の表示なし） | RESTRICTED | PubMed で抄録（推奨の要約）を確認 | GU-004 |
| SRC-724 | Birtle A, Johnson M, Chester J, et al. Adjuvant chemotherapy in upper tract urothelial carcinoma (the POUT trial): a phase 3, open-label, randomised controlled trial. Lancet. 2020;395(10232):1268-1277 | 10.1016/S0140-6736(20)30415-3 | 32145825 | 出版社（Elsevier）の著作物。PMC に著者原稿があるが CC ライセンスの表示は確認できない | RESTRICTED | PubMed・PMC7181180 で抄録と主要数値を確認 | GU-005 |
| SRC-725 | Oddens J, Brausi M, Sylvester R, et al. Final results of an EORTC-GU Cancers Group randomized study of maintenance BCG in intermediate- and high-risk Ta, T1 papillary carcinoma of the urinary bladder: one-third dose versus full dose and 1 year versus 3 years of maintenance. Eur Urol. 2013;63(3):462-472 | 10.1016/j.eururo.2012.10.039 | 23141049 | 出版社（Elsevier）の著作物（CC の表示なし） | RESTRICTED | PubMed で抄録と結論を確認 | GU-006 |
| SRC-726 | Grossman HB, Natale RB, Tangen CM, et al. Neoadjuvant chemotherapy plus cystectomy compared with cystectomy alone for locally advanced bladder cancer. N Engl J Med. 2003;349(9):859-866 | 10.1056/NEJMoa022148 | 12944571 | 出版社（NEJM）の著作物（CC の表示なし） | RESTRICTED | PubMed で抄録と数値を確認 | GU-007 |
| SRC-727 | Cumberbatch MGK, Jubber I, Black PC, et al. Epidemiology of Bladder Cancer: A Systematic Review and Contemporary Update of Risk Factors in 2018. Eur Urol. 2018;74(6):784-795 | 10.1016/j.eururo.2018.09.001 | 30268659 | 出版社（Elsevier）の著作物（CC の表示なし） | RESTRICTED | DOI は Crossref の引用記録で照合、PMID は DOI と対応する PubMed 引用記録で確認、抄録で GLOBOCAN 推計値を確認 | GU-008 |
| SRC-728 | Behrendt MA, de Jong J, van Rhijn BWG. Urachal cancer: contemporary review of the pathological, surgical, and prognostic aspects of this rare disease. Minerva Urol Nefrol. 2016;68(2):172-184 | なし（未確認） | 26583595 | 確認できず（CC の表示なし） | UNKNOWN | PubMed で PMID と抄録を確認。DOI は Crossref・出版社情報で確認できず、2016 年の当該誌掲載論文には DOI が付与されていないため null とした | GU-009 |
| SRC-729 | McConnell JD, Roehrborn CG, Bautista OM, et al.; MTOPS Research Group. The long-term effect of doxazosin, finasteride, and combination therapy on the clinical progression of benign prostatic hyperplasia. N Engl J Med. 2003;349(25):2387-2398 | 10.1056/NEJMoa030656 | 14681504 | 出版社（NEJM）の著作物（CC の表示なし） | RESTRICTED | PubMed で抄録を確認、進行リスク低下率は原著を引用する総説でも照合 | GU-010 |
| SRC-730 | Li S, Zeng XT, Ruan XL, et al. Holmium laser enucleation versus transurethral resection in patients with benign prostate hyperplasia: an updated systematic review with meta-analysis and trial sequential analysis. PLoS One. 2014;9(7):e101615 | 10.1371/journal.pone.0101615 | 25003963 | CC BY（オープンアクセス） | OPEN | PubMed（PMID: 25003963）・PMC4086899 で書誌と効果量を確認。当初候補の Tan ら 2007 年のメタ解析（Br J Surg）は PMID を確定できなかったため、識別子を両方確認できる本論文に差し替えた | GU-011 |
| SRC-731 | Ito K, Oki R, Sekine Y, et al. Screening for prostate cancer: History, evidence, controversies and future perspectives toward individualized screening. Int J Urol. 2019;26(10):956-970 | 10.1111/iju.14039 | 31183923 | 出版社（Wiley）の著作物（CC の表示なし） | RESTRICTED | PubMed で書誌を確認、本文で学会ガイドラインのカットオフ値と検診間隔を確認 | GU-012 |
| SRC-732 | US Preventive Services Task Force; Grossman DC, et al. Screening for Prostate Cancer: US Preventive Services Task Force Recommendation Statement. JAMA. 2018;319(18):1901-1913 | 10.1001/jama.2018.3710 | 29801017 | 米国政府機関（USPSTF）の勧告声明（JAMA 掲載） | GOV_US | PubMed と勧告文で推奨グレードと対象年齢を確認 | GU-013 |
| SRC-733 | Rebello RJ, Oing C, Knudsen KE, et al. Prostate cancer. Nat Rev Dis Primers. 2021;7(1):9 | 10.1038/s41572-020-00243-0 | 33542230 | 出版社（Springer Nature）の著作物（CC の表示なし） | RESTRICTED | PubMed で抄録と DOI・PMID を照合 | GU-014, GU-017 |
| SRC-734 | Fizazi K, Tran N, Fein L, et al.; LATITUDE Investigators. Abiraterone plus Prednisone in Metastatic, Castration-Sensitive Prostate Cancer. N Engl J Med. 2017;377(4):352-360 | 10.1056/NEJMoa1704174 | 28578607 | 出版社（NEJM）の著作物（CC の表示なし） | RESTRICTED | PubMed で抄録と数値を確認 | GU-015 |
| SRC-735 | Beer TM, Armstrong AJ, Rathkopf DE, et al.; PREVAIL Investigators. Enzalutamide in Metastatic Prostate Cancer before Chemotherapy. N Engl J Med. 2014;371(5):424-433 | 10.1056/NEJMoa1405095 | 24881730 | 出版社（NEJM）の著作物（CC の表示なし） | RESTRICTED | PubMed・PMC4418931 で抄録と数値を確認 | GU-016 |
| SRC-736 | Bajorin DF, Witjes JA, Gschwend JE, et al. Adjuvant Nivolumab versus Placebo in Muscle-Invasive Urothelial Carcinoma. N Engl J Med. 2021;384(22):2102-2114 | 10.1056/NEJMoa2034442 | 34077643 | 出版社（NEJM）の著作物（CC の表示なし） | RESTRICTED | PMC8215888 の全文で抄録の数値を確認 | GU-018 |
| SRC-737 | Beck SD. Optimal management of testicular cancer: from self-examination to treatment of advanced disease. Open Access J Urol. 2010;2:143-154 | null（確認できず） | 24198622 | 非営利利用のみ許可（出版社表示。CC BY-NC 相当） | RESTRICTED | PMC 本文（PMCID: PMC3818885）で抄録・腫瘍マーカー・TNM/IGCCCG の表・セミノーマと NSGCT の治療を確認し、PMID を照合。DOI は PMC・出版社 PDF・大学リポジトリの書誌表示のいずれでも確認できなかったため null | GU-019, GU-020, GU-021 |
| SRC-738 | Stecca CE, Alt M, Jiang DM, Chung P, Crook JM, Kulkarni GS, Sridhar SS. Recent Advances in the Management of Penile Cancer: A Contemporary Review of the Literature. Oncol Ther. 2021;9(1):21-39 | 10.1007/s40487-020-00135-z | 33454930 | CC BY-NC 4.0 | RESTRICTED | PMC 本文（PMCID: PMC8140030）で疫学・組織型・危険因子・生存率を確認し、出版社ページで書誌・DOI・ライセンスを照合 | GU-022 |
| SRC-739 | Rees J, Abrahams M, Doble A, Cooper A; Prostatitis Expert Reference Group. Diagnosis and treatment of chronic bacterial prostatitis and chronic prostatitis/chronic pelvic pain syndrome: a consensus guideline. BJU Int. 2015;116(4):509-525 | 10.1111/bju.13101 | 25711488 | CC BY-NC（PMC 掲載ページの表示） | RESTRICTED | PMC 本文（PMCID: PMC5008168）で NIH 分類・症状領域・第一選択治療を確認し、DOI・PMID・ライセンスを照合 | GU-023 |
| SRC-741 | Wu H, Wang F, Tang D, Han D. Mumps Orchitis: Clinical Aspects and Mechanisms. Front Immunol. 2021;12:582946 | 10.3389/fimmu.2021.582946 | 33815357 | CC BY（出版社ページの表示） | OPEN | 出版社の全文で頻度・経過・不妊への影響・支持療法を確認し、DOI・PMID・PMCID（PMC8013702）・ライセンスを照合 | GU-025 |
| SRC-742 | Morris BJ, Krieger JN. Penile Inflammatory Skin Disorders and the Preventive Role of Circumcision. Int J Prev Med. 2017;8:32 | 10.4103/ijpvm.IJPVM_377_16 | 28567234 | CC BY-NC-SA 3.0（PMC 掲載ページの表示） | RESTRICTED | PMC 本文（PMCID: PMC5439293）で亀頭包皮炎の原因・有病率・後天性包茎の記載を確認し、PMID・ライセンスを照合。DOI は引用情報2件で一致を確認 | GU-026, GU-033 |
| SRC-743 | Wosnitzer M, Goldstein M, Hardy MP. Review of Azoospermia. Spermatogenesis. 2014;4:e28218 | 10.4161/spmg.28218 | 25105055 | CC BY-NC 3.0（PMC 掲載ページの表示） | RESTRICTED | PMC 本文（PMCID: PMC4124057）で OA・NOA の頻度・鑑別・遺伝学的検査・治療を確認し、DOI・PMID・ライセンスを照合 | GU-027, GU-028 |
| SRC-744 | Schlegel PN, Sigman M, Collura B, et al. Diagnosis and treatment of infertility in men: AUA/ASRM guideline part I. Fertil Steril. 2021;115(1):54-61 | 10.1016/j.fertnstert.2020.11.015 | 33309062 | 学会ガイドライン（CC の表示なし） | RESTRICTED | ガイドラインのステートメント（初期評価・ホルモン評価・遺伝学的検査の推奨）を確認し、DOI・PMID を引用情報で照合。PMCID は確認できず null | GU-029 |
| SRC-745 | Burnett AL, Nehra A, Breau RH, et al. Erectile Dysfunction: AUA Guideline. J Urol. 2018;200(3):633-641 | 10.1016/j.juro.2018.05.004 | 29746858 | 学会ガイドライン（CC の表示なし） | RESTRICTED | PubMed 収載情報で書誌・DOI・PMID を照合し、ED の定義と共同意思決定・治療選択肢の提示に関する枠組みを確認。PMCID は確認できず null | GU-030 |
| SRC-746 | Dantas GC, Cavalcante F Jr, Yamauchi FI, Racy MCJ, Rahal A Jr, Baroni RH. Penile emergencies: a review of the main conditions. Radiol Bras. 2019;52(2):123-127 | 10.1590/0100-3984.2017.0072 | 31019343 | CC BY（PMC 掲載ページの表示） | OPEN | PMC 本文（PMCID: PMC6472861）で持続勃起症の分類・第一選択治療と陰茎折症の所見・画像・外科的修復を確認し、DOI は誌面表示で、PMID・ライセンスは PMC で照合 | GU-031, GU-038 |
| SRC-747 | Keays MA, Dave S. Current hypospadias management: diagnosis, surgical management, and long-term patient-centred outcomes. Can Urol Assoc J. 2017;11(1-2Suppl1):S48-S53 | 10.5489/cuaj.4386 | 28265319 | 学会誌の著作権表示のみ（CC 条件は確認できず） | UNKNOWN | PMC 本文（PMCID: PMC5332236）で頻度・分類・性分化疾患の評価・手術時期・合併症を確認し、DOI・PMID を照合。ライセンスは学会の著作権表示のみで CC 条件を確認できず UNKNOWN | GU-032 |
| SRC-748 | Shin J, Jeon GW. Comparison of diagnostic and treatment guidelines for undescended testis. Clin Exp Pediatr. 2020;63(11):415-421 | 10.3345/cep.2019.01438 | 32252147 | CC BY-NC 4.0（PMC 掲載ページの表示） | RESTRICTED | PMC 掲載ページ（PMCID: PMC7642136）で抄録（自然下降・紹介時期・精巣固定術の時期・不妊率・精巣癌リスク）を確認し、DOI・PMID・ライセンスを照合 | GU-034 |
| SRC-749 | Tiemstra JD, Kapoor S. Evaluation of scrotal masses. Am Fam Physician. 2008;78(10):1165-1170 | null（確認できず） | 19035065 | © American Academy of Family Physicians（CC の表示なし） | RESTRICTED | PubMed 抄録と公開全文で水瘤の透光性・自然消失と精索静脈瘤の触診所見・頻度・コクランレビューの結果を確認し、PMID を照合。DOI は PubMed 収載情報に付与がなく null | GU-035, GU-036 |
| SRC-750 | D'Andrea A, Coppolino F, Cesarano E, Russo A, Cappabianca S, Genovese EA, et al. US in the assessment of acute scrotum. Crit Ultrasound J. 2013;5 Suppl 1:S8 | 10.1186/2036-7902-5-S1-S8 | 23902859 | CC BY 2.0（PMC 掲載ページの表示） | OPEN | PMC 本文（PMCID: PMC3711727）で急性陰嚢症の定義・164例の内訳・外傷例の超音波所見を確認し、DOI・PMID・ライセンスを照合 | GU-037, GU-039 |

## 2. 事実票 YAML

```yaml
- id: UR-001
  domain: UR
  subdomain: 尿路結石症
  assertion:
    plain_statement_ja: "急性の側腹部痛で尿路結石を疑う場合、診断は病歴聴取と生化学的評価に画像検査を組み合わせて行う。画像検査は超音波検査が第一選択で、超音波検査で確定できない場合の標準は非造影CTである。超音波検査の感度・特異度は尿管結石で45%・94%、低線量CTでは感度93.1%・特異度96.6%とされる。結石の成分分析と、結石の大きさや部位などの負荷の評価が治療選択を左右する。"
    condition:
      region: 欧州
      study: ガイドライン（2025年版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-691
    source: "Skolarikos A, et al. EAU Guidelines on Urolithiasis. European Urology. 2025;88(1):64-75."
    doi: 10.1016/j.eururo.2025.03.011
    pmid: "40268592"
    pmcid: null
    url: https://doi.org/10.1016/j.eururo.2025.03.011
    source_license: ガイドライン
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "欧州のガイドラインに基づく内容であり、日本における画像診断の実施体制や診療報酬上の扱いは本調査では未確認である。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I)"
    kokushi: "医学各論 Ⅷ-4-A-①（腎結石、尿管結石、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-002
  domain: UR
  subdomain: 尿路結石症
  assertion:
    plain_statement_ja: "尿管結石に対するα遮断薬を用いた薬物的排石療法は、自然排石の確率を高める（排石のリスク比1.49、95%信頼区間1.39〜1.61）。利益は比較的大きな結石で認められ（リスク比1.57）、小さな結石では有意な利益は示されなかった。排石までの期間は平均3.79日短縮し、手術介入と入院のリスクも低下した。"
    condition:
      region: 国際
      study: 系統的レビュー・メタ解析（無作為化比較試験55件）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-692
    source: "Hollingsworth JM, et al. Alpha blockers for treatment of ureteric stones: systematic review and meta-analysis. BMJ. 2016;355:i6112."
    doi: 10.1136/bmj.i6112
    pmid: "27908918"
    pmcid: null
    url: https://doi.org/10.1136/bmj.i6112
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "タムスロシンなどのα遮断薬には、国内では尿管結石の排石を効能・効果とする承認がなく、排石目的の使用は適応外となる。保険適用の詳細は本調査では未確認である。また、体外衝撃波結石破砕術や内視鏡的治療の選択基準は本出典の対象範囲外であり、本カードでは扱っていない。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I)"
    kokushi: "医学各論 Ⅷ-4-A-①（腎結石、尿管結石、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-003
  domain: UR
  subdomain: 尿路結石症
  assertion:
    plain_statement_ja: "初発の特発性カルシウム結石の患者では、食事内容を変えずに水分摂取を増やして尿量2 L/日以上を保つことで、5年間の再発率が27.0%から12.1%に低下し（p=0.008）、再発までの平均期間も25.1か月から38.7か月に延長した。"
    condition:
      region: イタリア
      study: 無作為化比較試験（220例、5年追跡）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-693
    source: "Borghi L, Meschi T, Amato F, Briganti A, Novarini A, Giannini A. Urinary volume, water and recurrences in idiopathic calcium nephrolithiasis: a 5-year randomized prospective study. Journal of Urology. 1996;155(3):839-843."
    doi: 10.1016/S0022-5347(01)66321-3
    pmid: "8583588"
    pmcid: null
    url: https://doi.org/10.1016/S0022-5347(01)66321-3
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "対象は代謝異常のない初発の特発性カルシウム結石患者であり、再発例や代謝異常を伴う患者に対する食事療法・薬物療法は本出典では扱われていない。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I)"
    kokushi: "医学各論 Ⅷ-4-A-①（腎結石、尿管結石、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-004
  domain: UR
  subdomain: 尿路結石症
  assertion:
    plain_statement_ja: "成人男性の下部尿路結石では、膀胱結石が87.8%、尿道結石が12.2%を占めた。膀胱結石と独立に関連したのは年齢（オッズ比1.075）と前立腺体積（オッズ比1.069）であり、前立腺肥大症による尿の停滞が背景にある。一方、尿道結石は上部尿路結石や水腎症の合併と関連した（オッズ比3.468）。"
    condition:
      region: 韓国
      study: 後ろ向き多施設研究（成人男性221例）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-694
    source: "Jung JH, Park J, Kim WT, Kim HW, Kim HJ, Hong S, et al. The association of benign prostatic hyperplasia with lower urinary tract stones in adult men: a retrospective multicenter study. Asian Journal of Urology. 2018;5(2):118-121."
    doi: 10.1016/j.ajur.2017.06.008
    pmid: "29736374"
    pmcid: PMC5934505
    url: https://doi.org/10.1016/j.ajur.2017.06.008
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "韓国の3施設における成人男性の後ろ向き研究であり、女性・小児の下部尿路結石にはそのまま当てはまらない。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I)"
    kokushi: "医学各論 Ⅷ-4-A-②（膀胱結石、尿道結石、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-005
  domain: UR
  subdomain: 尿路閉塞
  assertion:
    plain_statement_ja: "上部尿路閉塞の原因には結石、腫瘍、腎盂尿管移行部狭窄などがあり、閉塞による上部尿路内圧の上昇は糸球体濾過量と腎血流量を低下させる。完全閉塞では2時間以内に炎症、尿細管萎縮、間質線維化が始まるとされる。閉塞の解除は尿管ステント留置または腎瘻造設による上部尿路の減圧で行い、閉塞性腎症は急性および慢性腎疾患の約10%を占める。"
    condition:
      region: 国際
      study: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-695
    source: "Yaxley J, Yaxley W. Obstructive uropathy – acute and chronic medical management. World Journal of Nephrology. 2023;12(1):1-9."
    doi: 10.5527/wjn.v12.i1.1
    pmid: "36704657"
    pmcid: PMC9846865
    url: https://doi.org/10.5527/wjn.v12.i1.1
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "総説に基づく記述であり、頻度や時間経過に関する数値は、引用された原著の対象集団に依存する。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)"
    kokushi: "医学各論 Ⅷ-4-B-①（上部尿路閉塞、水腎症、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-006
  domain: UR
  subdomain: 尿路閉塞
  assertion:
    plain_statement_ja: "下部尿路閉塞の原因には、結石のほか前立腺肥大症、神経因性膀胱、尿道狭窄、後部尿道弁などがある。下部尿路閉塞の減圧は尿道カテーテル留置で行い、慢性尿閉では残尿量がおよそ300 mLを超える場合にカテーテル留置が検討される。減圧後には約10%で血尿がみられる。"
    condition:
      region: 国際
      study: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-695
    source: "Yaxley J, Yaxley W. Obstructive uropathy – acute and chronic medical management. World Journal of Nephrology. 2023;12(1):1-9."
    doi: 10.5527/wjn.v12.i1.1
    pmid: "36704657"
    pmcid: PMC9846865
    url: https://doi.org/10.5527/wjn.v12.i1.1
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "総説に基づく記述であり、残尿量の目安は患者の状態により変わりうる。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)"
    kokushi: "医学各論 Ⅷ-4-B-②（下部尿路閉塞性疾患、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-007
  domain: UR
  subdomain: 尿路閉塞
  assertion:
    plain_statement_ja: "尿路閉塞による腎後性腎不全では、閉塞の解除後に閉塞後利尿が生じうる。閉塞後利尿は、尿量200 mL/時以上が2時間以上続くこと、または尿量3 L/日以上と定義され、完全な両側閉塞の解除後では最大で約半数にみられる。危険因子は血清クレアチニン高値と解除前の膀胱内尿量1,500 mL超であり、管理では前1時間の尿量の50%を輸液で補う方法が示されている。"
    condition:
      region: 国際
      study: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-695
    source: "Yaxley J, Yaxley W. Obstructive uropathy – acute and chronic medical management. World Journal of Nephrology. 2023;12(1):1-9."
    doi: 10.5527/wjn.v12.i1.1
    pmid: "36704657"
    pmcid: PMC9846865
    url: https://doi.org/10.5527/wjn.v12.i1.1
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "総説に基づく記述であり、輸液補充の具体的方法は施設や患者の状態により異なる。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)"
    kokushi: "医学各論 Ⅷ-4-B-①（上部尿路閉塞、水腎症）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-008
  domain: UR
  subdomain: 神経因性膀胱
  assertion:
    plain_statement_ja: "神経因性膀胱では、神経病変の性質・高位・広がりによって膀胱が過活動にも低活動にもなる。脊髄より上位の制御が失われると神経因性排尿筋過活動と排尿筋括約筋協調不全が生じ、膀胱内圧の上昇から膀胱尿管逆流、上部尿路拡張、腎機能障害へ進みうる。機能の客観的評価は尿流動態検査によってのみ可能で、ビデオ尿流動態検査が標準的な評価法とされ、分類は排尿筋と括約筋の状態に基づいて行われる。"
    condition:
      region: 中国
      study: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-696
    source: "Liao L. Evaluation and Management of Neurogenic Bladder: What Is New in China? International Journal of Molecular Sciences. 2015;16(8):18580-18600."
    doi: 10.3390/ijms160818580
    pmid: "26266405"
    pmcid: PMC4581261
    url: https://doi.org/10.3390/ijms160818580
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "中国の診療を中心にまとめた総説であり、評価法の実施体制は国内と異なる場合がある。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-342 (id: Jlvnl_g)"
    kokushi: "医学各論 Ⅷ-4-C-①（神経因性膀胱、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-009
  domain: UR
  subdomain: 神経因性膀胱
  assertion:
    plain_statement_ja: "神経因性膀胱の排尿管理の基本は清潔間欠導尿であり、標準的治療と位置づけられる。導尿は1日4〜6回、12〜14 Frのカテーテルを用い、導尿時の膀胱容量が400 mL未満になるよう調整する。排尿筋過活動に対しては抗ムスカリン薬などの薬物療法や、ボツリヌス毒素Aの膀胱内注入も用いられる。"
    condition:
      region: 中国
      study: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-696
    source: "Liao L. Evaluation and Management of Neurogenic Bladder: What Is New in China? International Journal of Molecular Sciences. 2015;16(8):18580-18600."
    doi: 10.3390/ijms160818580
    pmid: "26266405"
    pmcid: PMC4581261
    url: https://doi.org/10.3390/ijms160818580
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "抗ムスカリン薬およびボツリヌス毒素Aについて、神経因性膀胱に対する国内承認・保険適用の範囲は本調査では未確認である。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-342 (id: Jlvnl_g)"
    kokushi: "医学各論 Ⅷ-4-C-①（神経因性膀胱、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-010
  domain: UR
  subdomain: 膀胱尿管逆流
  assertion:
    plain_statement_ja: "小児の膀胱尿管逆流は排尿時膀胱尿道造影で診断し、重症度は国際分類でI度からV度に分ける。I度は尿管への逆流、II度は拡張のない腎盂までの逆流、III度は軽度の拡張、IV度は中等度の拡張で腎杯乳頭の印象が保たれるもの、V度は著明な拡張と尿管の蛇行があり乳頭の印象が失われるもの。有病率は小児の約1%で、有熱性尿路感染症の既往がある小児ではほぼ40%、出生前に水腎症と診断された小児では約20%にみられる。"
    condition:
      region: 欧州
      study: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-697
    source: "Goulin J, Demède D, Ranchin B, Mosca M, De-Mul A, Bidault Jourdainne V. What paediatricians need to know about modern urologic management of vesicoureteral reflux. Frontiers in Pediatrics. 2025;13:1607019."
    doi: 10.3389/fped.2025.1607019
    pmid: "40641902"
    pmcid: PMC12241063
    url: https://doi.org/10.3389/fped.2025.1607019
    source_license: CC BY
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "欧州の総説に基づく内容であり、検査の実施方針は国内の小児診療の指針と異なる場合がある。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-339 (id: Jlvnl-8)"
    kokushi: "医学各論 Ⅷ-4-C-②（膀胱尿管逆流、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-011
  domain: UR
  subdomain: 膀胱尿管逆流
  assertion:
    plain_statement_ja: "1回目または2回目の尿路感染症の後にI〜IV度の膀胱尿管逆流と診断された生後2〜71か月の小児607例では、トリメトプリム・スルファメトキサゾール合剤の2年間の予防投与により、再発が予防群39例・プラセボ群72例と減少した（ハザード比0.50、95%信頼区間0.34〜0.74）。一方で腎瘢痕の発生は減らなかった。再発時の大腸菌における同合剤への耐性の割合は予防群63%・プラセボ群19%であった。"
    condition:
      region: 米国
      study: 無作為化比較試験（二重盲検・プラセボ対照）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-698
    source: "RIVUR Trial Investigators; Hoberman A, Greenfield SP, Mattoo TK, et al. Antimicrobial prophylaxis for children with vesicoureteral reflux. New England Journal of Medicine. 2014;370(25):2367-2376."
    doi: 10.1056/NEJMoa1401811
    pmid: "24795142"
    pmcid: PMC4137319
    url: https://doi.org/10.1056/NEJMoa1401811
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "トリメトプリム・スルファメトキサゾール合剤の小児膀胱尿管逆流に対する予防投与について、国内承認・保険適用は本調査では未確認である。米国で実施された試験であり、起炎菌の耐性状況は国内と異なる可能性がある。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-339 (id: Jlvnl-8)"
    kokushi: "医学各論 Ⅷ-4-C-②（膀胱尿管逆流、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-012
  domain: UR
  subdomain: 尿路感染症
  assertion:
    plain_statement_ja: "急性腎盂腎炎の入院患者1,026例の集計では、男女比は約1対7.7で女性に多く、尿培養の陽性率は49.1%、分離された菌種では大腸菌が84.3%を占め、以下、肺炎桿菌、緑膿菌、腸球菌属、プロテウス属の順であった。血液培養の陽性率は10.1%で、その89.4%が大腸菌であり、敗血症は10.1%に認められた。"
    condition:
      region: 韓国
      study: 後ろ向き観察研究（入院例1,026例）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-699
    source: "Lee DG, Jeon SH, Lee CH, Lee SJ, Kim JI, Chang SG. Acute Pyelonephritis: Clinical Characteristics and the Role of the Surgical Treatment. Journal of Korean Medical Science. 2009;24(2):296-301."
    doi: 10.3346/jkms.2009.24.2.296
    pmid: "19399273"
    pmcid: PMC2672131
    url: https://doi.org/10.3346/jkms.2009.24.2.296
    source_license: CC BY-NC 3.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "韓国の大学病院における入院例の後ろ向き集計であり、起炎菌の分布や薬剤耐性の状況は国内と異なる可能性がある。複雑性腎盂腎炎の割合は出典の抄録と本文で数値が異なるため、本カードでは採用していない。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-331 (id: Jlvnl-M)"
    kokushi: "医学各論 Ⅷ-5-A-①（急性腎盂腎炎、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-013
  domain: UR
  subdomain: 尿路感染症
  assertion:
    plain_statement_ja: "有熱性尿路感染症の抗菌薬治療期間を7日間と14日間で比較した無作為化試験（200例）では、短期の臨床治癒率は全体で7日群90%・14日群95%となり、全体では7日治療の非劣性は確認されなかった。女性では94%対93%で非劣性が確認された一方、男性では86%対98%と7日治療の劣性が示された。長期の臨床治癒率は92%対91%で非劣性が確認された。"
    condition:
      region: オランダ
      study: 無作為化比較試験（二重盲検・プラセボ対照）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-700
    source: "van Nieuwkoop C, van der Starre WE, Stalenhoef JE, et al. Treatment duration of febrile urinary tract infection: a pragmatic randomized, double-blind, placebo-controlled non-inferiority trial in men and women. BMC Medicine. 2017;15:70."
    doi: 10.1186/s12916-017-0835-3
    pmid: "28366170"
    pmcid: PMC5376681
    url: https://doi.org/10.1186/s12916-017-0835-3
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "本試験では2週目にシプロフロキサシン500 mg 1日2回またはプラセボが用いられた。この用法が国内承認の用法・用量と一致するか、および腎盂腎炎に対する国内の保険適用の範囲は、本調査では未確認である。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-331 (id: Jlvnl-M)"
    kokushi: "医学各論 Ⅷ-5-A-①（急性腎盂腎炎、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-014
  domain: UR
  subdomain: 尿路感染症
  assertion:
    plain_statement_ja: "女性の急性単純性膀胱炎の第一選択薬は、ニトロフラントイン100 mg 1日2回を5日間、トリメトプリム・スルファメトキサゾール合剤を3日間（地域の耐性率が20%未満の場合）、ホスホマイシン・トロメタモール3 g単回投与、入手可能な地域ではピブメシリナム400 mg 1日2回であり、フルオロキノロン系薬は他の選択肢が使えない場合に温存される。"
    condition:
      region: 米国・欧州
      study: ガイドライン（2010年改訂版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-701
    source: "Gupta K, Hooton TM, Naber KG, et al. International clinical practice guidelines for the treatment of acute uncomplicated cystitis and pyelonephritis in women: a 2010 update by the Infectious Diseases Society of America and the European Society for Microbiology and Infectious Diseases. Clinical Infectious Diseases. 2011;52(5):e103-e120."
    doi: 10.1093/cid/ciq257
    pmid: "21292654"
    pmcid: null
    url: https://doi.org/10.1093/cid/ciq257
    source_license: ガイドライン
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "ニトロフラントイン、ホスホマイシンの単回投与製剤、ピブメシリナムは、国内での承認・供給状況が本調査では未確認であり、国内の標準的な膀胱炎治療とは異なる。薬剤の選択は地域の耐性率に基づくことが前提となる。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-343 (id: Jlvnl_Q)"
    kokushi: "医学各論 Ⅷ-5-A-②（急性単純性膀胱炎、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-015
  domain: UR
  subdomain: 尿路感染症
  assertion:
    plain_statement_ja: "女性の再発性単純性尿路感染症では、診断のために過去の症候性エピソードについて尿培養陽性の記録を確認し、汚染が疑われる場合は尿培養を繰り返すかカテーテル尿で取り直す。各エピソードでは治療前に尿検査、尿培養、感受性試験を行う。無症候性細菌尿は治療せず、無症状時の監視培養も行わない。膀胱鏡検査や上部尿路の画像検査は定型例ではルーチンに行わず、第一選択の治療は地域の感受性情報に基づくニトロフラントイン、トリメトプリム・スルファメトキサゾール合剤、ホスホマイシンで、治療期間は可能な範囲で7日以内とする。"
    condition:
      region: 米国・カナダ
      study: ガイドライン（2019年版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-702
    source: "Anger J, Lee U, Ackerman AL, et al. Recurrent Uncomplicated Urinary Tract Infections in Women: AUA/CUA/SUFU Guideline. Journal of Urology. 2019;202(2):282-289."
    doi: 10.1097/JU.0000000000000296
    pmid: "31042112"
    pmcid: null
    url: https://doi.org/10.1097/JU.0000000000000296
    source_license: ガイドライン
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "本ガイドラインの対象は再発性単純性尿路感染症であり、複雑性尿路感染症は対象に含まれない。ニトロフラントイン等の第一選択薬の国内承認・供給状況は本調査では未確認である。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-343 (id: Jlvnl_Q)"
    kokushi: "医学各論 Ⅷ-5-A-②（再発性膀胱炎、複雑性尿路感染症、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-016
  domain: UR
  subdomain: 尿路感染症
  assertion:
    plain_statement_ja: "尿道炎は排尿時痛、尿道の掻痒感や灼熱感、尿道分泌物を特徴とし、原因微生物として淋菌とクラミジア・トラコマティスが最も多く、持続する症例ではマイコプラズマ・ジェニタリウムの関与が増えている。評価では淋菌とクラミジアに対する核酸増幅検査を行う。非淋菌性尿道炎の推奨レジメンはドキシサイクリン100 mg 1日2回を7日間で、代替としてアジスロマイシン1 g単回投与がある。"
    condition:
      region: 米国
      study: ガイドライン（2021年版、政府機関）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-703
    source: "Workowski KA, Bachmann LH, Chan PA, et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recommendations and Reports. 2021;70(4):1-187."
    doi: 10.15585/mmwr.rr7004a1
    pmid: "34292926"
    pmcid: PMC8344968
    url: https://doi.org/10.15585/mmwr.rr7004a1
    source_license: 米国政府資料
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: "ドキシサイクリンおよびアジスロマイシンは国内承認薬であるが、尿道炎に対する用法・用量および保険適用の詳細は本調査では未確認である。米国の指針であり、国内の性感染症診療の指針とは異なる場合がある。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c)"
    kokushi: "医学各論 Ⅷ-5-A-③（尿道炎、a）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-017
  domain: UR
  subdomain: 尿路感染症
  assertion:
    plain_statement_ja: "5 cm以下の腎膿瘍および腎周囲膿瘍49例では、治療的ドレナージを行わず点滴抗菌薬のみで治療し、全例で臨床的な回復と3〜14週でのCT上の消失が得られた。素因では糖尿病が46.9%と最も多く、症状は発熱83.7%、側腹部痛53.1%であった。尿培養陽性率は64.6%で、最も多い起炎菌は大腸菌（50.0%）であった。平均在院期間は15.3日であった。"
    condition:
      region: 韓国
      study: 後ろ向き観察研究（49例）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-704
    source: "Lee SH, Jung HJ, Mah SY, Chung BH. Renal Abscesses Measuring 5 cm or Less: Outcome of Medical Treatment without Therapeutic Drainage. Yonsei Medical Journal. 2010;51(4):569-573."
    doi: 10.3349/ymj.2010.51.4.569
    pmid: "20499424"
    pmcid: PMC2880271
    url: https://doi.org/10.3349/ymj.2010.51.4.569
    source_license: CC BY-NC 3.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "韓国の単一施設における後ろ向き研究であり、対象は5 cm以下の膿瘍に限られる。これより大きな膿瘍における治療方針は本出典では示されていない。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)"
    kokushi: "医学各論 Ⅷ-5-A-④（腎膿瘍、b）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft

- id: UR-018
  domain: UR
  subdomain: 尿路感染症
  assertion:
    plain_statement_ja: "慢性腎盂腎炎の代表的な病態である逆流性腎症は、膀胱尿管逆流に伴う尿路感染症後の腎瘢痕や腎形成異常によって生じ、小児における慢性腎臓病、末期腎不全、高血圧の主要な原因となる。腎盂腎炎後の腎瘢痕の危険因子は、高度の逆流、排尿障害、腎盂腎炎の反復、抗菌薬治療開始の遅れであり、核医学検査で局所的な取り込み欠損を示す患者の10〜20%が高血圧または末期腎不全を呈する。管理は、再発する有熱性尿路感染症への対応と、高度の逆流など背景となる尿路異常への対処が中心となる。"
    condition:
      region: 欧州
      study: 総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-697
    source: "Goulin J, Demède D, Ranchin B, Mosca M, De-Mul A, Bidault Jourdainne V. What paediatricians need to know about modern urologic management of vesicoureteral reflux. Frontiers in Pediatrics. 2025;13:1607019."
    doi: 10.3389/fped.2025.1607019
    pmid: "40641902"
    pmcid: PMC12241063
    url: https://doi.org/10.3389/fped.2025.1607019
    source_license: CC BY
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "本カードは膀胱尿管逆流と逆流性腎症を扱った総説に基づく。閉塞など他の機序による慢性腎盂腎炎および成人例の経過については本出典では詳述されておらず、慢性腎盂腎炎に特化した一次資料は本調査では確認できなかった。"
  curriculum:
    core_curriculum: "PS-02-09-05 (id: JkxnuRs)"
    kokushi: "医学各論 Ⅷ-5-A-⑤（慢性腎盂腎炎、c）"
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-019
  domain: UR
  subdomain: 淋菌性尿道炎
  assertion:
    plain_statement_ja: 米国CDCの性感染症治療ガイドライン2021年版では、淋菌感染症に対する推奨はセフトリアキソン500mgの単回筋肉内注射（体重150kg以上では1g）であり、クラミジア感染が除外できない場合はドキシサイクリン100mgを1日2回7日間経口で併用する。
    condition:
      region: 米国
      study: CDC性感染症治療ガイドライン2021年版の推奨レジメン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-703
    source: 'Workowski KA, Bachmann LH, Chan PA, et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recomm Rep. 2021;70(4):1-187'
    doi: 10.15585/mmwr.rr7004a1
    pmid: '34292926'
    pmcid: PMC8344968
    url: https://doi.org/10.15585/mmwr.rr7004a1
    source_license: 米国政府著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 薬剤（セフトリアキソン、ドキシサイクリン）を含むカードである。本カードは米国の推奨であり、日本の性感染症の診断・治療の推奨とは用量・用法が異なる場合がある。両薬剤の国内の承認・保険適用の状況は、本調査では未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c)'
    kokushi: 医学各論 Ⅷ-5-D-①（淋菌性尿道炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-020
  domain: UR
  subdomain: 非淋菌性尿道炎
  assertion:
    plain_statement_ja: 非淋菌性尿道炎の主因であるクラミジア感染に対し、米国CDCの性感染症治療ガイドライン2021年版の推奨はドキシサイクリン100mgを1日2回7日間経口であり、代替レジメンとしてアジスロマイシン1g単回経口とレボフロキサシン500mgを1日1回7日間経口が挙げられている。
    condition:
      region: 米国
      study: CDC性感染症治療ガイドライン2021年版の推奨レジメン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-703
    source: 'Workowski KA, Bachmann LH, Chan PA, et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recomm Rep. 2021;70(4):1-187'
    doi: 10.15585/mmwr.rr7004a1
    pmid: '34292926'
    pmcid: PMC8344968
    url: https://doi.org/10.15585/mmwr.rr7004a1
    source_license: 米国政府著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 薬剤（ドキシサイクリン、アジスロマイシン、レボフロキサシン）を含むカードである。本カードは米国の推奨であり、日本の推奨とは異なる場合がある。各薬剤の国内の承認・保険適用の状況は、本調査では未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c)'
    kokushi: 医学各論 Ⅷ-5-D-②（非淋菌性尿道炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-021
  domain: UR
  subdomain: 性器ヘルペス
  assertion:
    plain_statement_ja: 性器ヘルペスの初発例は全例が抗ウイルス薬による治療の対象であり、米国CDCの性感染症治療ガイドライン2021年版の推奨は、アシクロビル400mgを1日3回7〜10日間、ファムシクロビル250mgを1日3回7〜10日間、バラシクロビル1gを1日2回7〜10日間のいずれかの経口投与で、10日間で治癒が不完全な場合は治療を延長する。抗ウイルス薬の外用は効果が乏しく勧められない。
    condition:
      region: 米国
      study: CDC性感染症治療ガイドライン2021年版の推奨レジメン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-703
    source: 'Workowski KA, Bachmann LH, Chan PA, et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recomm Rep. 2021;70(4):1-187'
    doi: 10.15585/mmwr.rr7004a1
    pmid: '34292926'
    pmcid: PMC8344968
    url: https://doi.org/10.15585/mmwr.rr7004a1
    source_license: 米国政府著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 薬剤（アシクロビル、ファムシクロビル、バラシクロビル）を含むカードである。本カードは米国の推奨であり、日本の用法・用量とは異なる場合がある。各薬剤の国内の承認・保険適用の状況は、本調査では未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-5-D-③（性器ヘルペス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-022
  domain: UR
  subdomain: 尖圭コンジローマ
  assertion:
    plain_statement_ja: 尖圭コンジローマ（外性器・肛門周囲の疣贅）の治療は、患者自身が塗布するイミキモドクリーム、ポドフィロックス0.5%液・ゲル、シネカテキン15%軟膏と、医療者が行う液体窒素による凍結療法、外科的切除、トリクロロ酢酸またはビクロロ酢酸80〜90%の塗布に分けられる。イミキモド5%クリームは就寝前に週3回、最長16週間塗布する。
    condition:
      region: 米国
      study: CDC性感染症治療ガイドライン2021年版の推奨レジメン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-703
    source: 'Workowski KA, Bachmann LH, Chan PA, et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recomm Rep. 2021;70(4):1-187'
    doi: 10.15585/mmwr.rr7004a1
    pmid: '34292926'
    pmcid: PMC8344968
    url: https://doi.org/10.15585/mmwr.rr7004a1
    source_license: 米国政府著作物（CDC）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 薬剤（イミキモド、ポドフィロックス、シネカテキン）を含むカードである。本カードは米国の推奨であり、日本で使用可能な薬剤や適応は異なる場合がある。各薬剤の国内の承認・保険適用の状況は、本調査では未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-5-D-④（尖圭コンジローマ、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-023
  domain: UR
  subdomain: 重複腎盂尿管
  assertion:
    plain_statement_ja: 重複腎盂尿管のうち完全重複では、腎盂腎杯系と尿管がそれぞれ2つに分かれ、尿管の開口位置にはWeigert-Meyerの法則が90%を超える例で当てはまる。トルコの単施設で2010年から2021年に診療した小児239例では、女児が143例（60%）、両側性が22例（9.2%）で、受診の契機で最も多かったのは尿路感染の85例（35.6%）であり、合併異常として胎児期水腎症23例（9.6%）、膀胱尿管逆流13例（5.4%）、尿管瘤10例（4.2%）がみられた。
    condition:
      region: トルコ
      study: 単施設の小児239例を対象とした後方視的検討（2010〜2021年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-708
    source: 'Yener S, Pehlivanoğlu C, Akıs Yıldız Z, Ilce HT, Ilce Z. Duplex Kidney Anomalies and Associated Pathologies in Children: A Single-Center Retrospective Review. Cureus. 2022;14(6):e25777'
    doi: 10.7759/cureus.25777
    pmid: '35812643'
    pmcid: PMC9270195
    url: https://doi.org/10.7759/cureus.25777
    source_license: CC BY（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 数値はトルコの単施設の後方視的検討の本文から読み取ったものであり、受診した小児に限られるため、一般集団での頻度とは異なる。Weigert-Meyerの法則の割合は同論文の総説的記載に基づく。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-429 (id: JlvnmHg)'
    kokushi: 医学各論 Ⅷ-10-A-①（重複腎盂尿管、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-024
  domain: UR
  subdomain: 異所性尿管開口
  assertion:
    plain_statement_ja: 女児の異所性尿管開口では、完全重複尿管の上極尿管が膀胱より遠位に開口するため、通常の排尿ができるにもかかわらず持続的に尿が滴る失禁が典型的な症状となる。オーストラリアの単施設で15年間に経験した女児22例（うち両側2例）ではこの滴状の失禁が最も多い症状で、超音波検査が診断に有用であり、治療は21腎で上極の半腎切除、3腎で尿管腎盂吻合が行われ、全例で滴状の失禁が消失した。
    condition:
      region: オーストラリア
      study: 単施設の女児22例の症例集積（15年間）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-709
    source: 'Ahmed S, Morris LL, Byard RW. Ectopic ureter with complete ureteric duplication in the female child. J Pediatr Surg. 1992;27(11):1455-1460'
    doi: 10.1016/0022-3468(92)90199-h
    pmid: '1479509'
    pmcid: null
    url: https://doi.org/10.1016/0022-3468(92)90199-h
    source_license: 出版社の著作物（CC の表示を確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 1992年の単施設症例集積の抄録で確認した範囲であり、現在の画像診断や術式の実情とは異なる場合がある。出典のライセンス表示は確認できなかった。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-429 (id: JlvnmHg)'
    kokushi: 医学各論 Ⅷ-10-A-②（異所性尿管開口、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-025
  domain: UR
  subdomain: 膀胱瘤
  assertion:
    plain_statement_ja: 膀胱瘤は骨盤臓器脱における前腟壁脱の一形態である。米国の産婦人科の診療指針によれば、米国女性が骨盤臓器脱の手術を受ける生涯リスクは13%で、症状のピークは70〜79歳にみられ、骨盤臓器脱のある女性の数は2050年までに約50%増加すると予測されている。
    condition:
      region: 米国
      study: 米国産婦人科学会の診療指針（プラクティス・ブレティン第214号、2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-710
    source: 'American College of Obstetricians and Gynecologists. Pelvic Organ Prolapse: ACOG Practice Bulletin, Number 214. Obstet Gynecol. 2019;134(5):e126-e142'
    doi: 10.1097/AOG.0000000000003519
    pmid: '31651832'
    pmcid: null
    url: https://doi.org/10.1097/AOG.0000000000003519
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は同指針の抄録で確認した米国の疫学であり、日本の頻度や診療実態とは異なる場合がある。膀胱瘤の病期分類や術式の詳細は本文で確認できなかったため、本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-10-A-③（膀胱瘤、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-026
  domain: UR
  subdomain: 単純性腎嚢胞
  assertion:
    plain_statement_ja: 単純性腎嚢胞は加齢とともに頻度が増える。日本の健診受診者14,314人を対象とした調査では、1,700人（11.9%）に少なくとも1つの嚢胞がみられ、男女比は2対1、頻度は30歳代の5.1%から70歳代の36.1%へ増加した。嚢胞を有する45人の経過観察（平均6年）では、嚢胞は年平均2.82mm（年率6.3%）増大し、増大速度は50歳未満（年3.94mm）の方が50歳以上（年1.84mm）より速かった。
    condition:
      region: 日本
      study: 健診受診者14,314人の横断調査と45人の経過観察
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-711
    source: 'Terada N, Ichioka K, Matsuta Y, Okubo K, Yoshimura K, Arai Y. The natural history of simple renal cysts. J Urol. 2002;167(1):21-23'
    doi: 10.1016/S0022-5347(05)65373-6
    pmid: '11743266'
    pmcid: null
    url: https://doi.org/10.1016/S0022-5347(05)65373-6
    source_license: 出版社の著作物（CC の表示を確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値は2002年の日本の健診集団の抄録で確認した範囲である。出典のライセンス表示は確認できなかった。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-10-A-④（単純性腎嚢胞、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-027
  domain: UR
  subdomain: 嚢胞腎
  assertion:
    plain_statement_ja: 常染色体顕性多発性嚢胞腎は最も頻度の高い遺伝性腎疾患で、有病率は1,000〜2,500人に1人と推定され、主にPKD1遺伝子とPKD2遺伝子の変異によって生じる。バソプレシン受容体拮抗薬のトルバプタンは、病勢の進行を遅らせる薬として承認されている。
    condition:
      region: 国際
      study: 病態と治療の進歩に関する総説（2022年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-712
    source: 'Reiterová J, Tesař V. Autosomal Dominant Polycystic Kidney Disease: From Pathophysiology of Cystogenesis to Advances in the Treatment. Int J Mol Sci. 2022;23(6):3317'
    doi: 10.3390/ijms23063317
    pmid: '35328738'
    pmcid: PMC8949594
    url: https://doi.org/10.3390/ijms23063317
    source_license: CC BY 4.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 薬剤（トルバプタン）を含むカードである。総説では承認の事実のみが述べられており、トルバプタンの国内の承認・保険適用の状況（適応や投与条件を含む）は、本調査では未確認である。有病率は総説に引用された推定値である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-338 (id: Jlvnl-4)'
    kokushi: 医学各論 Ⅷ-10-A-⑤（嚢胞腎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-028
  domain: UR
  subdomain: 馬蹄腎
  assertion:
    plain_statement_ja: 馬蹄腎は最も頻度の高い腎癒合異常で、両側の腎の下極が峡部によって癒合し（下極癒合は90%を超える）、位置異常、回転異常、血管供給の変化を伴う。峡部は通常、機能する腎実質を含む。解剖学的調査での頻度は0.15〜0.48%とされ、下腸間膜動脈が第3腰椎の高さで峡部の腹側にとどまる配置は40%にみられるにとどまる。
    condition:
      region: 国際
      study: 発生学と外科的配慮に関する系統的文献レビュー（2025年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-713
    source: 'Nechita OC, Badescu D, Popescu RI, Aurelian J, Constantin TC, Toma CV, Jinga V, Geavlete B. Reviewing the complexities of horseshoe kidney: insights into embryogenesis and surgical considerations. J Med Life. 2025;18(1):10-19'
    doi: 10.25122/jml-2024-0325
    pmid: '40071162'
    pmcid: PMC11891615
    url: https://doi.org/10.25122/jml-2024-0325
    source_license: CC BY 4.0（誌面の表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 頻度と割合は系統的レビューの本文と表から読み取ったもので、原著研究の集計値を含む（二次資料経由）。個々の割合の原典は本カードではたどっていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-429 (id: JlvnmHg)'
    kokushi: 医学各論 Ⅷ-10-A-⑥（馬蹄腎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-029
  domain: UR
  subdomain: 膀胱憩室
  assertion:
    plain_statement_ja: 前立腺肥大症に伴う膀胱憩室では、憩室内の尿の停滞が結石、尿路感染、腫瘍の原因となりうる。ブラジルの単施設で前立腺手術と憩室切除を受けた47例の後方視的解析では、急性尿閉を生じた群の憩室径は平均6.8cmで、生じなかった群の平均4.5cmより大きく（p=0.005）、5.15cmを境とした感度は73%、特異度は72%で、多変量解析では憩室径のみが独立した危険因子であった。
    condition:
      region: ブラジル
      study: 手術を受けた前立腺肥大症47例の単施設後方視コホート（2006〜2016年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-714
    source: 'Iscaife A, dos Anjos G, Barbosa Neto C, Nahas WC, Srougi M, Antunes AA. The role of bladder diverticula in the prevalence of acute urinary retention in patients with BPH who are candidates to surgery. Int Braz J Urol. 2018;44(4):765-770'
    doi: 10.1590/S1677-5538.IBJU.2017.0605
    pmid: '29617085'
    pmcid: PMC6092655
    url: https://doi.org/10.1590/S1677-5538.IBJU.2017.0605
    source_license: CC BY（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 数値は抄録で確認した範囲であり、対象は手術適応となった前立腺肥大症の患者に限られるため、膀胱憩室のある一般集団への一般化には注意がいる。先天性憩室は原著で除外されており、本カードは後天性の憩室に関するものである。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-10-A-⑦（膀胱憩室、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-030
  domain: UR
  subdomain: 夜尿症
  assertion:
    plain_statement_ja: 夜尿症は5歳以上の小児にみられる睡眠中の尿失禁で、男児は女児の約2倍多く、5歳時点での頻度は約15%とされる。6か月以上の夜間乾燥期間を一度も得たことのないものを一次夜尿症といい、約80%を占める。背景には夜間多尿、膀胱容量の低下、睡眠からの覚醒障害などが関与し、治療の第一選択はアラーム療法と薬物療法である。
    condition:
      region: 米国
      study: 病態・診断・治療に関する総説と単施設の経験（2014年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-715
    source: 'DiBianco JM, Morley C, Al-Omar O. Nocturnal enuresis: A topic review and institution experience. Avicenna J Med. 2014;4(4):77-86'
    doi: 10.4103/2231-0770.140641
    pmid: '25506580'
    pmcid: PMC4251068
    url: https://doi.org/10.4103/2231-0770.140641
    source_license: CC BY-NC-SA 3.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頻度の数値は総説の本文から読み取ったもので、引用された疫学研究の集計を含む（二次資料経由）。薬物療法の代表薬であるデスモプレシンについて、夜尿症に対する国内の承認・保険適用の状況は、本調査では未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-10-D-①（夜尿症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-031
  domain: UR
  subdomain: 過活動膀胱
  assertion:
    plain_statement_ja: 過活動膀胱の初期評価は病歴聴取、身体診察、尿検査を最低限とし、合併症のない患者の初期精査に尿流動態検査、膀胱鏡、診断目的の超音波検査は用いるべきでない。治療は全患者に対する行動療法が第一選択で、経口の抗ムスカリン薬、経口のβ3アドレナリン受容体作動薬、経皮オキシブチニンが第二選択、膀胱壁内へのオナボツリヌストキシンA注入（100単位）、仙骨神経刺激療法、経皮的脛骨神経刺激が第三選択とされる。
    condition:
      region: 米国
      study: AUA/SUFUの過活動膀胱ガイドライン2019年改訂版
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-716
    source: 'Lightner DJ, Gomelsky A, Souter L, Vasavada SP. Diagnosis and Treatment of Overactive Bladder (Non-Neurogenic) in Adults: AUA/SUFU Guideline Amendment 2019. J Urol. 2019;202(3):558-563'
    doi: 10.1097/JU.0000000000000309
    pmid: '31039103'
    pmcid: null
    url: https://doi.org/10.1097/JU.0000000000000309
    source_license: 出版社の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤（抗ムスカリン薬、β3アドレナリン受容体作動薬、オキシブチニン、オナボツリヌストキシンA）を含むカードである。本カードは米国のガイドラインに基づき、日本で使用可能な薬剤・手技やその適応は異なる場合がある。各薬剤の国内の承認・保険適用の状況は、本調査では未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-10-D-②（過活動膀胱、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-032
  domain: UR
  subdomain: 腹圧性尿失禁
  assertion:
    plain_statement_ja: 女性の腹圧性尿失禁に対する中部尿道スリング手術について、系統的レビュー（40試験、参加者6,145人）では、短期の客観的治癒率は経閉鎖孔アプローチで85.7%、恥骨後アプローチで87.2%と同等であり、短期の主観的治癒率は経閉鎖孔アプローチで62〜98%、恥骨後アプローチで71〜97%の範囲であった。
    condition:
      region: 国際
      study: コクランの系統的レビューとメタ解析（2017年版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-717
    source: 'Ford AA, Rogerson L, Cody JD, Aluko P, Ogah JA. Mid-urethral sling operations for stress urinary incontinence in women. Cochrane Database Syst Rev. 2017;(7):CD006375'
    doi: 10.1002/14651858.CD006375.pub4
    pmid: '28756647'
    pmcid: PMC6483329
    url: https://doi.org/10.1002/14651858.CD006375.pub4
    source_license: 出版社の著作物（コクラン、CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認した短期成績の範囲であり、長期成績と有害事象（膀胱穿孔や排尿障害など）の詳細は本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-10-D-③（腹圧性尿失禁、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-033
  domain: UR
  subdomain: 腎・尿路損傷
  assertion:
    plain_statement_ja: 腎および尿路の外傷は、成人と小児の腹部外傷の約10〜20%に生じる。管理は解剖学的な損傷の程度、血行動態、合併損傷を踏まえて決めるものであり、小児では非手術的管理が標準とされ、多職種による対応が求められる。
    condition:
      region: 国際
      study: WSES-AASTの腎・尿路外傷ガイドライン（2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-718
    source: 'Coccolini F, Moore EE, Kluger Y, et al; WSES-AAST Expert Panel. Kidney and uro-trauma: WSES-AAST guidelines. World J Emerg Surg. 2019;14:54'
    doi: 10.1186/s13017-019-0274-x
    pmid: '31827593'
    pmcid: PMC6886230
    url: https://doi.org/10.1186/s13017-019-0274-x
    source_license: CC BY（出版社ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本カードはガイドラインの抄録で確認した原則の範囲であり、損傷の重症度分類ごとの具体的な治療選択や観察期間は本文で確認できなかったため含めていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-340 (id: Jlvnl_E)'
    kokushi: 医学各論 Ⅷ-10-E-①（腎・尿路損傷、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: UR-034
  domain: UR
  subdomain: 尿路・性器異物
  assertion:
    plain_statement_ja: 尿道異物の自己挿入の動機として最も多いのは性的刺激の追求である。除去方法は異物の形態と位置によって決まり、尿路上皮の損傷を最小限に抑えることが目標で、内視鏡的摘出がしばしば成功する。除去後は尿道狭窄などの遅発性合併症への経過観察が必要であり、文献では尿道狭窄の頻度は5%とされる。引用された成人20例・9年間のシリーズでは、男性は女性の1.7倍で、平均年齢は35.8歳であった。
    condition:
      region: オーストラリア
      study: 症例報告と文献レビュー（2013年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-719
    source: 'Naidu K, Chung A, Mulcahy M. An unusual urethral foreign body. Int J Surg Case Rep. 2013;4(11):1052-1054'
    doi: 10.1016/j.ijscr.2013.07.017
    pmid: '24055017'
    pmcid: PMC3825963
    url: https://doi.org/10.1016/j.ijscr.2013.07.017
    source_license: CC BY-NC-ND（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 単一の症例報告に基づく記載であり、尿道狭窄5%と成人20例の数値は、同論文の本文中で引用された既報シリーズの値である（二次資料経由）。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-10-E-⑦（尿路・性器異物、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-001
  domain: GU
  subdomain: 腎細胞癌
  assertion:
    plain_statement_ja: 腎細胞癌は腎臓に発生する癌の90%を超え、10を超える組織・分子サブタイプがあり、最多の淡明細胞型が腎細胞癌による死亡の大部分を占める。限局した腎細胞癌は手術で治療し得る一方、転移した腎細胞癌は従来の化学療法に抵抗性であり、分子標的薬や免疫チェックポイント阻害薬が治療の柱となる。
    condition:
      region: 国際
      study: 疾患プライマー総説（Nature Reviews Disease Primers、2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-721
    source: 'Hsieh JJ, Purdue MP, Signoretti S, et al. Renal cell carcinoma. Nat Rev Dis Primers. 2017;3:17009'
    doi: 10.1038/nrdp.2017.9
    pmid: '28276433'
    pmcid: PMC5936048
    url: https://doi.org/10.1038/nrdp.2017.9
    source_license: 出版社（Springer Nature）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 病期分類（TNM）の具体的な区分や腫瘍径の閾値、腎部分切除と全摘除の選択基準は抄録では確認できないため本カードには含めていない。分子標的薬・免疫チェックポイント阻害薬の国内の承認・保険適用の個別確認はしていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-656 (id: JlvnmdY)'
    kokushi: 医学各論 Ⅷ-6-A-①（腎細胞癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-002
  domain: GU
  subdomain: 転移性腎細胞癌
  assertion:
    plain_statement_ja: 未治療の進行腎細胞癌でIMDC分類の中リスク・高リスクの患者を対象とした第III相試験では、ニボルマブとイピリムマブの併用はスニチニブ単独に比べ、18か月時点の全生存割合が75%対60%、死亡のハザード比0.63、奏効率42%対27%、完全奏効率9%対1%であった。グレード3〜4の治療関連有害事象は併用群46%対単独群63%であった。
    condition:
      region: 国際
      study: 第III相ランダム化比較試験（CheckMate 214、1096例登録、中・高リスク集団での主要評価）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-722
    source: 'Motzer RJ, Tannir NM, McDermott DF, et al. Nivolumab plus Ipilimumab versus Sunitinib in Advanced Renal-Cell Carcinoma. N Engl J Med. 2018;378(14):1277-1290'
    doi: 10.1056/NEJMoa1712126
    pmid: '29562145'
    pmcid: PMC5972549
    url: https://doi.org/10.1056/NEJMoa1712126
    source_license: 出版社（NEJM）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 追跡期間中央値25.2か月時点の結果である。ニボルマブ、イピリムマブ、スニチニブの国内の承認・保険適用は未確認であり、取り込み側で確認が必要である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-656 (id: JlvnmdY)'
    kokushi: 医学各論 Ⅷ-6-A-①（腎細胞癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-003
  domain: GU
  subdomain: 腎細胞癌
  assertion:
    plain_statement_ja: 腎細胞癌は腎に発生する癌の90%超を占め、淡明細胞型が最多の組織型で腎細胞癌による死亡の大部分を占める。淡明細胞型ではVHL遺伝子の変異が高頻度にみられ、エピジェネティックな制御に関わる遺伝子の変化も同定されており、これらの遺伝子変化が発症に関与する。
    condition:
      region: 国際
      study: 疾患プライマー総説（Nature Reviews Disease Primers、2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-721
    source: 'Hsieh JJ, Purdue MP, Signoretti S, et al. Renal cell carcinoma. Nat Rev Dis Primers. 2017;3:17009'
    doi: 10.1038/nrdp.2017.9
    pmid: '28276433'
    pmcid: PMC5936048
    url: https://doi.org/10.1038/nrdp.2017.9
    source_license: 出版社（Springer Nature）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 喫煙・肥満・高血圧などの環境要因の寄与の定量や、遺伝性腎細胞癌の頻度の数値は抄録では確認できないため本カードには数値を含めていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-656 (id: JlvnmdY)'
    kokushi: 医学各論 Ⅷ-6-A-①（腎細胞癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-004
  domain: GU
  subdomain: 腎盂・尿管癌
  assertion:
    plain_statement_ja: 上部尿路尿路上皮癌は診断時に約60%が浸潤性であり、組織型と画像検査を含む臨床評価によるリスク層別化と、リンチ症候群のリスク評価が管理の指針となる。低リスクの腫瘍では、対側の腎が健常でも腎温存治療を第一の選択肢として提示する。高リスクの腫瘍では根治的腎尿管全摘が基本となり、術後のプラチナ製剤による化学療法が選択肢となり、化学療法を受けられない、または希望しない患者では術後ニボルマブも選択肢となる。
    condition:
      region: 欧州
      study: EAUガイドライン（上部尿路尿路上皮癌、2023年改訂版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-723
    source: 'Rouprêt M, Seisen T, Birtle AJ, et al. European Association of Urology Guidelines on Upper Urinary Tract Urothelial Carcinoma: 2023 Update. Eur Urol. 2023;84(1):49-64'
    doi: 10.1016/j.eururo.2023.03.013
    pmid: '36967359'
    pmcid: null
    url: https://doi.org/10.1016/j.eururo.2023.03.013
    source_license: 欧州泌尿器科学会（EAU）のガイドライン、Elsevier 掲載（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 欧州のガイドラインの推奨文に基づく記述である。リスク分類の具体的な判定項目と数値閾値はガイドライン本文の表から読み取る必要があるため本カードには含めていない。プラチナ製剤とニボルマブの国内の承認・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg)'
    kokushi: 医学各論 Ⅷ-6-A-②（腎盂・尿管癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-005
  domain: GU
  subdomain: 腎盂・尿管癌
  assertion:
    plain_statement_ja: 腎尿管全摘後の病理学的病期pT2〜T4またはリンパ節転移陽性の上部尿路尿路上皮癌261例を対象とした第III相試験では、術後90日以内に開始したゲムシタビンとプラチナ製剤（シスプラチン、腎機能が低い場合はカルボプラチン）の併用4サイクルは、経過観察に比べ3年無病生存割合が71%対46%、無病生存のハザード比0.45と良好であった。
    condition:
      region: 英国
      study: 第III相ランダム化比較試験（POUT試験、英国71施設）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-724
    source: 'Birtle A, Johnson M, Chester J, et al. Adjuvant chemotherapy in upper tract urothelial carcinoma (the POUT trial): a phase 3, open-label, randomised controlled trial. Lancet. 2020;395(10232):1268-1277'
    doi: 10.1016/S0140-6736(20)30415-3
    pmid: '32145825'
    pmcid: PMC7181180
    url: https://doi.org/10.1016/S0140-6736(20)30415-3
    source_license: 出版社（Elsevier）の著作物。PMC に著者原稿があるが CC ライセンスの表示は確認できない
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 術後補助化学療法の成績であり、術前化学療法の成績ではない。ゲムシタビン、シスプラチン、カルボプラチンの国内の承認・保険適用は未確認であり、取り込み側で確認が必要である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg)'
    kokushi: 医学各論 Ⅷ-6-A-②（腎盂・尿管癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-006
  domain: GU
  subdomain: 膀胱癌
  assertion:
    plain_statement_ja: 中リスク・高リスクのTa・T1乳頭状膀胱癌に対するBCG膀胱内注入の維持療法を検討したEORTCのランダム化試験（1355例、追跡中央値7.1年）では、1/3用量への減量と1年間の維持はいずれも非劣性を示すことができず、1/3用量・1年維持の組み合わせは通常用量・3年維持より再発予防効果が劣っていた。高リスク患者では、通常用量での3年維持が1年維持より再発を減らした。
    condition:
      region: 欧州
      study: ランダム化比較試験（EORTC-GU cancers group、用量と維持期間の2×2要因デザイン）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-725
    source: 'Oddens J, Brausi M, Sylvester R, et al. Final results of an EORTC-GU Cancers Group randomized study of maintenance BCG in intermediate- and high-risk Ta, T1 papillary carcinoma of the urinary bladder: one-third dose versus full dose and 1 year versus 3 years of maintenance. Eur Urol. 2013;63(3):462-472'
    doi: 10.1016/j.eururo.2012.10.039
    pmid: '23141049'
    pmcid: null
    url: https://doi.org/10.1016/j.eururo.2012.10.039
    source_license: 出版社（Elsevier）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: BCG製剤の国内の承認・保険適用（使用される菌株・製剤の違いを含む）は未確認であり、取り込み側で確認が必要である。進展や生存についてはこの試験では群間差が示されなかった。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg)'
    kokushi: 医学各論 Ⅷ-6-B-①（膀胱癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-007
  domain: GU
  subdomain: 膀胱癌
  assertion:
    plain_statement_ja: 局所進行膀胱癌（T2〜T4a、転移なし）307例を対象としたランダム化試験では、根治的膀胱全摘の前にMVAC療法（メトトレキサート、ビンブラスチン、ドキソルビシン、シスプラチン）を3サイクル行った群は全摘単独群に比べ、生存期間中央値が77か月対46か月、全摘標本で残存癌を認めない割合が38%対15%であった。
    condition:
      region: 米国
      study: ランダム化比較試験（SWOG 8710）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-726
    source: 'Grossman HB, Natale RB, Tangen CM, et al. Neoadjuvant chemotherapy plus cystectomy compared with cystectomy alone for locally advanced bladder cancer. N Engl J Med. 2003;349(9):859-866'
    doi: 10.1056/NEJMoa022148
    pmid: '12944571'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa022148
    source_license: 出版社（NEJM）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: MVAC療法の各薬剤の国内の承認・保険適用は未確認である。ゲムシタビンとシスプラチンの併用など現在のレジメンとの直接比較は本試験の範囲外である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg)'
    kokushi: 医学各論 Ⅷ-6-B-①（膀胱癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-008
  domain: GU
  subdomain: 膀胱癌
  assertion:
    plain_statement_ja: 膀胱癌の新規症例はGLOBOCANの推計で2012年に世界で約43万件、死亡は約16.5万件とされる。危険因子の中で寄与リスクが最も大きいのは喫煙と職業性の発癌物質への曝露であり、一部の集団では喫煙の減少に伴い罹患率が下がっている。
    condition:
      region: 国際
      study: 系統的レビュー（全文279編を対象、2018年時点の更新）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-727
    source: 'Cumberbatch MGK, Jubber I, Black PC, et al. Epidemiology of Bladder Cancer: A Systematic Review and Contemporary Update of Risk Factors in 2018. Eur Urol. 2018;74(6):784-795'
    doi: 10.1016/j.eururo.2018.09.001
    pmid: '30268659'
    pmcid: null
    url: https://doi.org/10.1016/j.eururo.2018.09.001
    source_license: 出版社（Elsevier）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2012年のGLOBOCAN推計に基づく数値であり、その後の推計とは異なる可能性がある。膀胱鏡や尿細胞診などの診断手順の詳細はこの出典の対象外であり、本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg)'
    kokushi: 医学各論 Ⅷ-6-B-①（膀胱癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-009
  domain: GU
  subdomain: 尿膜管癌
  assertion:
    plain_statement_ja: 尿膜管癌は尿膜管の遺残から発生する稀な悪性腫瘍で、50〜60歳代に多く、組織型は通常の膀胱癌と異なり腸型に似た腺癌が多数を占める。膀胱頂部に発生し、血尿や粘液尿を症状とし、発症時に約3分の1は切除不能である。治療は外科的切除が中心で、根治を目指す場合は尿膜管靱帯、膀胱頂部、臍の一括切除とR0切除が重要とされる。
    condition:
      region: 欧州
      study: 総説（オランダの専門施設によるレビュー）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-728
    source: 'Behrendt MA, de Jong J, van Rhijn BWG. Urachal cancer: contemporary review of the pathological, surgical, and prognostic aspects of this rare disease. Minerva Urol Nefrol. 2016;68(2):172-184'
    doi: null
    pmid: '26583595'
    pmcid: null
    url: null
    source_license: 確認できず（CC の表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 稀少疾患でありランダム化試験のエビデンスはなく、記述は症例集積と総説に基づく。この出典にはDOIが付与されておらず（2016年の当該誌掲載論文のため）、doiはnullとした。ライセンス表示も確認できていない。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)'
    kokushi: 医学各論 Ⅷ-6-B-②（尿膜管癌、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-010
  domain: GU
  subdomain: 前立腺肥大症
  assertion:
    plain_statement_ja: 前立腺肥大症の男性3047例を平均4.5年追跡したMTOPS試験では、ドキサゾシンとフィナステリドの併用はプラセボに比べ臨床的進行のリスクを66%低下させ、各薬剤の単独療法より有意に大きく進行を抑えた。急性尿閉と侵襲的治療の必要性は、フィナステリドを含む治療（併用療法とフィナステリド単独）で低下し、ドキサゾシン単独では低下しなかった。
    condition:
      region: 米国
      study: ランダム化比較試験（MTOPS、平均追跡4.5年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-729
    source: 'McConnell JD, Roehrborn CG, Bautista OM, et al.; MTOPS Research Group. The long-term effect of doxazosin, finasteride, and combination therapy on the clinical progression of benign prostatic hyperplasia. N Engl J Med. 2003;349(25):2387-2398'
    doi: 10.1056/NEJMoa030656
    pmid: '14681504'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa030656
    source_license: 出版社（NEJM）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ドキサゾシンとフィナステリドの国内の承認・保険適用は未確認であり、取り込み側で確認が必要である。日本で一般的なα遮断薬（タムスロシンなど）との比較は本試験の範囲外である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-347 (id: Jlvnl_0)'
    kokushi: 医学各論 Ⅷ-6-C-①（前立腺肥大症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-011
  domain: GU
  subdomain: 前立腺肥大症
  assertion:
    plain_statement_ja: 前立腺肥大症に対するホルミウムレーザー前立腺核出術（HoLEP）と経尿道的前立腺切除術（TURP）を比較した8件のランダム化試験・855例のメタ解析では、HoLEPは手術時間が約14分長い一方、輸血のリスクが低く（相対リスク0.17）、カテーテル留置期間が約20時間、入院期間が約25時間短かった。最大尿流率は術後3か月と12か月でHoLEPが良好であった。
    condition:
      region: 国際
      study: 系統的レビュー・メタ解析（ランダム化試験8件、855例）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-730
    source: 'Li S, Zeng XT, Ruan XL, et al. Holmium laser enucleation versus transurethral resection in patients with benign prostate hyperplasia: an updated systematic review with meta-analysis and trial sequential analysis. PLoS One. 2014;9(7):e101615'
    doi: 10.1371/journal.pone.0101615
    pmid: '25003963'
    pmcid: PMC4086899
    url: https://doi.org/10.1371/journal.pone.0101615
    source_license: CC BY（オープンアクセス）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 効果量の数値はメタ解析本文の集計値から読み取ったものである（表から読み取り）。対象は2014年までのランダム化試験であり、その後の術式の改良は反映されていない。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-347 (id: Jlvnl_0)'
    kokushi: 医学各論 Ⅷ-6-C-①（前立腺肥大症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-012
  domain: GU
  subdomain: 前立腺癌
  assertion:
    plain_statement_ja: 日本では泌尿器科の専門学会の検診ガイドラインが、精密検査を勧めるPSAのカットオフ値を4.0 ng/mL、年齢別では50〜64歳3.0、65〜69歳3.5、70歳以上4.0 ng/mLと提示し、初回PSA値に応じた検診間隔（1.1 ng/mL以上では毎年、1.0 ng/mL以下では3年ごと）を提案している。一方、公的ながん検診のガイドラインは対策型検診としてのPSA検診を推奨しておらず、日本国内でも立場が分かれているため、受診は利益と不利益を説明したうえでの個人の判断に基づくものとされる。
    condition:
      region: 日本
      study: 総説（日本のPSA検診の歴史・エビデンス・論点の検討、2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-731
    source: 'Ito K, Oki R, Sekine Y, et al. Screening for prostate cancer: History, evidence, controversies and future perspectives toward individualized screening. Int J Urol. 2019;26(10):956-970'
    doi: 10.1111/iju.14039
    pmid: '31183923'
    pmcid: null
    url: https://doi.org/10.1111/iju.14039
    source_license: 出版社（Wiley）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: カットオフ値と検診間隔は、総説本文に記載された学会ガイドラインの内容を読み取ったものである（本文から読み取り）。学会ガイドラインと公的ガイドラインで推奨が異なる点に注意が必要である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk)'
    kokushi: 医学各論 Ⅷ-6-C-②（前立腺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-013
  domain: GU
  subdomain: 前立腺癌
  assertion:
    plain_statement_ja: 米国の予防医療専門委員会は、55〜69歳の男性ではPSA検診を受けるかどうかは利益と不利益を説明したうえで個人が判断すべきとし（C推奨）、70歳以上の男性にはPSA検診を行わないよう勧告している（D推奨）。検診により1000人あたり約1.3人の前立腺癌死亡と約3人の転移症例を防げる可能性がある一方、偽陽性による追加検査、過剰診断・過剰治療、治療に伴う尿失禁や勃起障害などの不利益がある。
    condition:
      region: 米国
      study: 米国予防医療専門委員会（USPSTF）勧告声明（2018年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-732
    source: 'US Preventive Services Task Force; Grossman DC, et al. Screening for Prostate Cancer: US Preventive Services Task Force Recommendation Statement. JAMA. 2018;319(18):1901-1913'
    doi: 10.1001/jama.2018.3710
    pmid: '29801017'
    pmcid: null
    url: https://doi.org/10.1001/jama.2018.3710
    source_license: 米国政府機関（USPSTF）の勧告声明（JAMA 掲載）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 2018年の勧告であり、その後の改訂で内容が変わる可能性がある。欧州の学会ガイドラインの立場（リスクに応じた検診の提案）は本カードの出典の範囲外であり、別途確認が必要である。利益の数値は約13年の追跡に基づく推計である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk)'
    kokushi: 医学各論 Ⅷ-6-C-②（前立腺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-014
  domain: GU
  subdomain: 前立腺癌
  assertion:
    plain_statement_ja: 限局性前立腺癌は、PSA検査や直腸指診の異常を契機に前立腺生検で診断される。再発リスクが低〜中程度の限局性疾患では、早期に発見・治療されれば予後は良好で10年全生存割合は99%とされる。限局性疾患の治療の選択肢には監視療法、前立腺全摘除術、放射線治療があり、再発した場合は救済治療やアンドロゲン除去療法が用いられる。
    condition:
      region: 国際
      study: 疾患プライマー総説（Nature Reviews Disease Primers、2021年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-733
    source: 'Rebello RJ, Oing C, Knudsen KE, et al. Prostate cancer. Nat Rev Dis Primers. 2021;7(1):9'
    doi: 10.1038/s41572-020-00243-0
    pmid: '33542230'
    pmcid: null
    url: https://doi.org/10.1038/s41572-020-00243-0
    source_license: 出版社（Springer Nature）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: リスク分類の具体的な境界値（PSA値、グリソンスコア、病期による層別）は原著の表から読み取る必要があるため、本カードには分類の数値を含めていない（表から読み取りが必要）。10年全生存割合99%は低〜中リスクの限局性疾患が早期に発見・治療された場合の記載である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk)'
    kokushi: 医学各論 Ⅷ-6-C-②（前立腺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-015
  domain: GU
  subdomain: 前立腺癌
  assertion:
    plain_statement_ja: 新規に診断された高リスクの転移性去勢感受性前立腺癌1199例を対象としたLATITUDE試験では、アンドロゲン除去療法にアビラテロンとプレドニゾンを併用すると、全生存期間中央値は未到達対34.7か月（死亡のハザード比0.62）、画像的無増悪生存期間中央値は33.0か月対14.8か月（ハザード比0.47）であった。グレード3の高血圧と低カリウム血症は併用群で多かった。
    condition:
      region: 国際
      study: 第III相ランダム化比較試験（LATITUDE、追跡期間中央値30.4か月）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-734
    source: 'Fizazi K, Tran N, Fein L, et al.; LATITUDE Investigators. Abiraterone plus Prednisone in Metastatic, Castration-Sensitive Prostate Cancer. N Engl J Med. 2017;377(4):352-360'
    doi: 10.1056/NEJMoa1704174
    pmid: '28578607'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1704174
    source_license: 出版社（NEJM）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: アビラテロンとプレドニゾンの国内の承認・保険適用は未確認であり、取り込み側で確認が必要である。対象は新規診断の高リスク転移性去勢感受性前立腺癌に限られる。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk)'
    kokushi: 医学各論 Ⅷ-6-C-②（前立腺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-016
  domain: GU
  subdomain: 前立腺癌
  assertion:
    plain_statement_ja: 化学療法歴のない転移性去勢抵抗性前立腺癌1717例を対象としたPREVAIL試験では、エンザルタミドはプラセボに比べ、12か月時点の画像的無増悪生存割合が65%対14%（ハザード比0.19）、死亡のハザード比0.71であり、化学療法の開始までの期間も延長した。
    condition:
      region: 国際
      study: 第III相ランダム化比較試験（PREVAIL）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-735
    source: 'Beer TM, Armstrong AJ, Rathkopf DE, et al.; PREVAIL Investigators. Enzalutamide in Metastatic Prostate Cancer before Chemotherapy. N Engl J Med. 2014;371(5):424-433'
    doi: 10.1056/NEJMoa1405095
    pmid: '24881730'
    pmcid: PMC4418931
    url: https://doi.org/10.1056/NEJMoa1405095
    source_license: 出版社（NEJM）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: エンザルタミドの国内の承認・保険適用は未確認であり、取り込み側で確認が必要である。数値は中間解析（データカットオフ時点）を含む結果である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk)'
    kokushi: 医学各論 Ⅷ-6-C-②（前立腺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-017
  domain: GU
  subdomain: 前立腺癌
  assertion:
    plain_statement_ja: 前立腺癌は世界で多くの男性が罹患し、人間開発指数の高い地域に多い。分子レベルではTMPRSS2とETSファミリー遺伝子の融合遺伝子、MYCの増幅、PTENやTP53の欠失・変異が知られ、進行した病態ではアンドロゲン受容体遺伝子の増幅・変異がみられる。診断はPSA検査や直腸指診を契機に行われる前立腺生検による。
    condition:
      region: 国際
      study: 疾患プライマー総説（Nature Reviews Disease Primers、2021年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-733
    source: 'Rebello RJ, Oing C, Knudsen KE, et al. Prostate cancer. Nat Rev Dis Primers. 2021;7(1):9'
    doi: 10.1038/s41572-020-00243-0
    pmid: '33542230'
    pmcid: null
    url: https://doi.org/10.1038/s41572-020-00243-0
    source_license: 出版社（Springer Nature）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 世界の罹患数・死亡数の具体的な推計値は抄録では確認できないため、本カードには数値を含めていない。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk)'
    kokushi: 医学各論 Ⅷ-6-C-②（前立腺癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-018
  domain: GU
  subdomain: 膀胱癌
  assertion:
    plain_statement_ja: 根治的手術後の再発高リスクの筋層浸潤尿路上皮癌709例を対象としたCheckMate 274試験では、術後のニボルマブ（240 mgを2週ごと、最長1年）はプラセボに比べ、無病生存期間中央値が20.8か月対10.8か月、6か月時点で再発なく生存している割合が74.9%対60.3%（ハザード比0.70）であった。腫瘍のPD-L1発現が1%以上の集団ではハザード比0.55であった。グレード3以上の治療関連有害事象は17.9%対7.2%であった。
    condition:
      region: 国際
      study: 第III相ランダム化比較試験（CheckMate 274、膀胱・尿管・腎盂原発を含む）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-736
    source: 'Bajorin DF, Witjes JA, Gschwend JE, et al. Adjuvant Nivolumab versus Placebo in Muscle-Invasive Urothelial Carcinoma. N Engl J Med. 2021;384(22):2102-2114'
    doi: 10.1056/NEJMoa2034442
    pmid: '34077643'
    pmcid: PMC8215888
    url: https://doi.org/10.1056/NEJMoa2034442
    source_license: 出版社（NEJM）の著作物（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 上部尿路原発は登録全体の約2割に制限された試験であり、上部尿路原発のみでの効果量は限定的である。ニボルマブの国内の承認・保険適用は未確認であり、取り込み側で確認が必要である。
  curriculum:
    core_curriculum: 'PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg)'
    kokushi: 医学各論 Ⅷ-6-B-①（膀胱癌、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-019
  domain: GU
  subdomain: セミノーマの治療
  assertion:
    plain_statement_ja: 精巣セミノーマの治療は病期によって決まる。臨床病期I期では治癒率はほぼ100%で、精巣摘除後の選択肢は経過観察、補助放射線療法、カルボプラチン単剤1コースである。病期I期では約20%に潜在的なリンパ節転移があり、再発の危険因子は原発腫瘍径4 cm超と精巣網への浸潤で、危険因子が0個・1個・2個の場合の5年再発率はそれぞれ12%・16%・32%である。低容量（3 cm未満）の病期II期には放射線療法が、より大きな病期II期と病期III期には化学療法が用いられる。
    condition:
      region: 米国
      study: 精巣胚細胞癌の管理に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-737
    source: 'Beck SD. Optimal management of testicular cancer: from self-examination to treatment of advanced disease. Open Access J Urol. 2010;2:143-154'
    doi: null
    pmid: '24198622'
    pmcid: PMC3818885
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3818885/
    source_license: 非営利利用のみ許可（出版社表示。CC BY-NC 相当）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2010年の総説に基づいており、現在のガイドラインの推奨とは異なる可能性がある。カルボプラチンを含む化学療法薬の国内承認・保険適用の状況は未確認である。出典論文の DOI は PMC・出版社 PDF・大学リポジトリのいずれでも表示を確認できず null とした。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-659 (id: Jlvnmds)'
    kokushi: 医学各論 Ⅷ-6-C-③（精巣癌(セミノーマ)、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-020
  domain: GU
  subdomain: 非セミノーマ性胚細胞腫瘍の治療
  assertion:
    plain_statement_ja: 非セミノーマ性胚細胞腫瘍（NSGCT）の病期I期の治癒率はほぼ100%で、精巣摘除後の選択肢は経過観察、後腹膜リンパ節郭清（RPLND）、補助化学療法である。腫瘍マーカーが正常な低容量（5 cm未満）の病期II期は、RPLND か化学療法で管理できる。転移性疾患では予後分類により、予後良好群には BEP 療法（ブレオマイシン、エトポシド、シスプラチン）3コース、予後中間・不良群には4コースが標準とされ、化学療法後に残存する腫瘤は50〜60%に奇形腫または活動性癌を含むため切除が推奨される。再発の多くは治療後2年以内に起こり、2年を超えた再発は晩期再発と呼ばれる。
    condition:
      region: 米国
      study: 精巣胚細胞癌の管理に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-737
    source: 'Beck SD. Optimal management of testicular cancer: from self-examination to treatment of advanced disease. Open Access J Urol. 2010;2:143-154'
    doi: null
    pmid: '24198622'
    pmcid: PMC3818885
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3818885/
    source_license: 非営利利用のみ許可（出版社表示。CC BY-NC 相当）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2010年の総説に基づいており、現在のガイドラインの推奨とは異なる可能性がある。BEP 療法を構成する薬剤（ブレオマイシン、エトポシド、シスプラチン）の国内承認・保険適用の状況は未確認である。出典論文の DOI は確認できず null とした（SRC-737 の出典表を参照）。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-659 (id: Jlvnmds)'
    kokushi: 医学各論 Ⅷ-6-C-④（精巣癌(非セミノーマ)、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-021
  domain: GU
  subdomain: 精巣腫瘍の腫瘍マーカーと病期分類
  assertion:
    plain_statement_ja: 精巣腫瘍では精巣摘除の前後で血清腫瘍マーカー（AFP、β-hCG、LDH）を測定する。AFP は胎児性癌、奇形腫、卵黄嚢腫瘍が分泌するが、純粋なセミノーマと純粋な絨毛癌では分泌されないため、AFP が上昇した純粋なセミノーマは非セミノーマとして分類する。β-hCG は絨毛癌では全例、胎児性癌では40〜60%、純粋なセミノーマでは約10%（通常は500 U/L未満）で上昇する。NSGCT では AFP が50〜70%、β-hCG が40〜60%で上昇し、どちらか一方は最大90%で上昇する。マーカーの半減期は AFP が7日未満、β-hCG が3日未満である。病期分類は TNM に S 分類を加え、S1 は LDH が正常上限の1.5倍未満・hCG 5000未満・AFP 1000未満、S2 は LDH 1.5〜10倍・hCG 5000〜50000・AFP 1000〜10000、S3 は LDH 10倍超・hCG 50000超・AFP 10000超である。IGCCCG 分類では予後良好群・中間群・不良群の割合は56%・28%・16%、5年生存率は90%・80%・50%で、セミノーマには予後不良群がない。
    condition:
      region: 米国
      study: 精巣胚細胞癌の管理に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-737
    source: 'Beck SD. Optimal management of testicular cancer: from self-examination to treatment of advanced disease. Open Access J Urol. 2010;2:143-154'
    doi: null
    pmid: '24198622'
    pmcid: PMC3818885
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3818885/
    source_license: 非営利利用のみ許可（出版社表示。CC BY-NC 相当）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: S 分類と IGCCCG 分類の数値は、論文の表（TNM 分類表と IGCCCG 分類表）から読み取りした。マーカー上昇の割合は本文の記載に基づく。出典論文の DOI は確認できず null とした（SRC-737 の出典表を参照）。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-659 (id: Jlvnmds)'
    kokushi: 医学各論 Ⅷ-6-C-③（精巣癌(セミノーマ)、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-022
  domain: GU
  subdomain: 陰茎癌
  assertion:
    plain_statement_ja: 陰茎癌はまれな癌で、60歳代の男性に多く、発生率は男性10万人あたり1人未満である。組織型は扁平上皮癌が原発性陰茎癌の約95%を占めて最も多く、症例の約半数が HPV 感染と関連する。危険因子には包茎、HPV 感染、喫煙が含まれる。初診時に触知できる鼠径リンパ節を認める症例は28〜64%に上り、5年生存率は全体で約50%、リンパ節転移陽性例では27%である。
    condition:
      region: 国際
      study: 陰茎癌管理に関する最新総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-738
    source: 'Stecca CE, Alt M, Jiang DM, Chung P, Crook JM, Kulkarni GS, Sridhar SS. Recent Advances in the Management of Penile Cancer: A Contemporary Review of the Literature. Oncol Ther. 2021;9(1):21-39'
    doi: 10.1007/s40487-020-00135-z
    pmid: '33454930'
    pmcid: PMC8140030
    url: https://doi.org/10.1007/s40487-020-00135-z
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 発生率と生存率は主に欧米の集計に基づく総説の記載であり、日本の値ではない。危険因子のオッズ比（包茎11.4など）は表から読み取る必要があるため本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
    kokushi: 医学各論 Ⅷ-6-C-⑤（陰茎癌、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-023
  domain: GU
  subdomain: 前立腺炎
  assertion:
    plain_statement_ja: 前立腺炎は NIH 分類で、I群（急性細菌性前立腺炎）、II群（慢性細菌性前立腺炎）、III群（慢性前立腺炎/慢性骨盤痛症候群。精液、前立腺圧出液、マッサージ後尿に白血球を認める IIIa と認めない IIIb）、IV群（無症候性炎症性前立腺炎）に分けられる。症状は泌尿生殖器痛、下部尿路症状、心理的問題、性機能障害の4領域に及び、前立腺炎様症状は男性の35〜50%が生涯のうちに経験する。慢性細菌性前立腺炎と III群に対する第一選択の治療選択肢は、抗菌薬、排尿症状がある場合のα遮断薬、単純な鎮痛薬であり、培養で感染が支持されない場合や症状の改善が得られない場合に、キノロン系抗菌薬を繰り返し使うことは避けるべきとされる。
    condition:
      region: 英国
      study: 英国のコンセンサスガイドライン（Prostatitis Expert Reference Group、2015年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-739
    source: 'Rees J, Abrahams M, Doble A, Cooper A; Prostatitis Expert Reference Group. Diagnosis and treatment of chronic bacterial prostatitis and chronic prostatitis/chronic pelvic pain syndrome: a consensus guideline. BJU Int. 2015;116(4):509-525'
    doi: 10.1111/bju.13101
    pmid: '25711488'
    pmcid: PMC5008168
    url: https://doi.org/10.1111/bju.13101
    source_license: CC BY-NC（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: NIH 分類はガイドラインの表から読み取りした。英国のガイドラインの記載であり、抗菌薬やα遮断薬の国内承認・保険適用の状況は未確認である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-348 (id: Jlvnl_8)'
    kokushi: 医学各論 Ⅷ-5-B-①（前立腺炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-024
  domain: GU
  subdomain: 精巣上体炎
  assertion:
    plain_statement_ja: 急性精巣上体炎のうち性感染症によると考えられる場合（原因としてクラミジアと淋菌が最も多い）について、CDC のガイドラインはセフトリアキソン500 mg単回筋注（体重150 kg以上では1 g）とドキシサイクリン100 mg 1日2回10日間の併用を推奨する。腸内細菌も関与しうる場合（肛門性交の挿入側など）は、セフトリアキソンにレボフロキサシン500 mg 1日1回10日間を併用し、腸内細菌のみが考えられる場合はレボフロキサシン単独を用いる。突然発症した陰嚢痛では、外科的緊急症である精巣捻転を疑う必要がある。
    condition:
      region: 米国
      study: CDC 性感染症治療ガイドライン（2021年版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-703
    source: 'Workowski KA, Bachmann LH, Chan PA, Johnston CM, Muzny CA, Park I, Reno H, Zenilman JM, Bolan GA. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recomm Rep. 2021;70(4):1-187'
    doi: 10.15585/mmwr.rr7004a1
    pmid: '34292926'
    pmcid: PMC8344968
    url: https://doi.org/10.15585/mmwr.rr7004a1
    source_license: 米国政府機関（CDC）の公表物
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 米国 CDC ガイドライン2021年版の推奨用量であり、日本の用法・用量や薬剤耐性の状況とは異なる可能性がある。セフトリアキソン、ドキシサイクリン、レボフロキサシンの国内承認・保険適用の状況は未確認である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
    kokushi: 医学各論 Ⅷ-5-B-②（精巣上体炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-025
  domain: GU
  subdomain: 精巣炎
  assertion:
    plain_statement_ja: ムンプス（流行性耳下腺炎）に伴う精巣炎は、唾液腺以外の合併症の中で最も多く、若年成人男性のムンプス症例の最大40%に起こり、10〜30%は両側性である。通常は耳下腺炎の発症から約1週間後に生じる。思春期後のムンプス精巣炎患者の約30%に不妊または妊孕性の低下が生じ、精巣萎縮は患者の約半数に起こりうる。特異的な抗ウイルス療法はなく、治療は安静、陰嚢の支持、鎮痛薬や抗炎症薬による支持療法が中心で、症状は通常4〜10日で軽快する。ステロイドは痛みや腫脹を和らげても、病状の経過や精巣萎縮の予防には影響しない。
    condition:
      region: 国際
      study: ムンプス精巣炎の臨床像と機序に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-741
    source: 'Wu H, Wang F, Tang D, Han D. Mumps Orchitis: Clinical Aspects and Mechanisms. Front Immunol. 2021;12:582946'
    doi: 10.3389/fimmu.2021.582946
    pmid: '33815357'
    pmcid: PMC8013702
    url: https://doi.org/10.3389/fimmu.2021.582946
    source_license: CC BY（出版社ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 頻度や転帰の数値は、総説が既報の臨床報告を集約した記載であり、単一の一次研究の値ではない。鎮痛薬・抗炎症薬の国内承認・保険適用の詳細は未確認である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
    kokushi: 医学各論 Ⅷ-5-B-③（精巣炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-026
  domain: GU
  subdomain: 亀頭包皮炎
  assertion:
    plain_statement_ja: 亀頭炎は亀頭の炎症、包皮炎は包皮の炎症、その両方が起きた状態が亀頭包皮炎である。感染症の原因として最も多いのは真菌で、カンジダ・アルビカンスが最も多く分離され、誘因として最も多いのは衛生状態の不良である。亀頭炎は環状切除を受けていない男性の11〜13%、受けた男性の2%に報告され、糖尿病で環状切除を受けていない男性では35%に症状のある亀頭炎がみられた。メタ解析では、環状切除を受けた男性は亀頭炎の有病率が68%低く、亀頭炎には陰茎癌リスクの3.8倍の上昇が伴った。治療には外用抗真菌薬と衛生指導が用いられ、根治的な治療は環状切除である。
    condition:
      region: 国際
      study: 陰茎炎症性皮膚疾患と環状切除の予防的役割に関する系統的レビュー
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-742
    source: 'Morris BJ, Krieger JN. Penile Inflammatory Skin Disorders and the Preventive Role of Circumcision. Int J Prev Med. 2017;8:32'
    doi: 10.4103/ijpvm.IJPVM_377_16
    pmid: '28567234'
    pmcid: PMC5439293
    url: https://doi.org/10.4103/ijpvm.IJPVM_377_16
    source_license: CC BY-NC-SA 3.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率の数値は系統的レビューが集約した観察研究とメタ解析の値である。外用抗真菌薬の国内承認・保険適用の状況は未確認である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
    kokushi: 医学各論 Ⅷ-5-B-④（亀頭包皮炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-027
  domain: GU
  subdomain: 閉塞性無精子症
  assertion:
    plain_statement_ja: 無精子症は不妊男性の15%に認められ、閉塞性無精子症（OA）と非閉塞性無精子症（NOA）に分類される。OA は無精子症の約40%を占め、精巣での精子形成は保たれたまま精路の閉塞によって生じる。原因には精管切除や鼠径ヘルニア手術などの医原性のもの、CFTR 変異と関連する先天性精管欠損、精巣上体炎などの炎症、射精管閉塞がある。診断は、病歴と診察（精巣容積は正常で精巣上体は硬い）、FSH が正常であること、先天性の場合は CFTR 検査、画像検査を組み合わせて行う。治療は、可能な場合に顕微鏡下の精管精管吻合術や精管精巣上体吻合術による再建を行い、再建できない場合は精巣上体からの精子吸引（MESA）と体外受精・顕微授精（IVF/ICSI）を用いる。
    condition:
      region: 米国
      study: 無精子症に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-743
    source: 'Wosnitzer M, Goldstein M, Hardy MP. Review of Azoospermia. Spermatogenesis. 2014;4:e28218'
    doi: 10.4161/spmg.28218
    pmid: '25105055'
    pmcid: PMC4124057
    url: https://doi.org/10.4161/spmg.28218
    source_license: CC BY-NC 3.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国の専門施設グループによる2014年の総説の記載である。再建手術の開通率などの数値は術者や施設で幅が大きいため本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-346 (id: Jlvnl_w)'
    kokushi: 医学各論 Ⅷ-8-E-②（閉塞性無精子症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-028
  domain: GU
  subdomain: 非閉塞性無精子症
  assertion:
    plain_statement_ja: 非閉塞性無精子症（NOA）は無精子症の約60%を占め、原発性精巣機能不全（LH と FSH が高値で精巣は小さい）と、続発性精巣機能不全（先天性低ゴナドトロピン性性腺機能低下症などで LH と FSH が低い）を含む。NOA は、精巣の硬さと容積、FSH、核型や Y 染色体微小欠失などの遺伝学的検査によって閉塞性無精子症と鑑別する。核型異常は NOA の男性の最大19%に認められ、最も多いのはクラインフェルター症候群（47,XXY）で、Y 染色体の AZF 領域の微小欠失は無精子症男性の10〜20%に認められる。治療は、先天性低ゴナドトロピン性性腺機能低下症に対する内科的治療と、適切な症例に対する顕微鏡下精巣内精子採取術（micro-TESE）と IVF/ICSI が中心であり、AZFc 微小欠失では最大80%で精子採取が可能とされる。
    condition:
      region: 米国
      study: 無精子症に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-743
    source: 'Wosnitzer M, Goldstein M, Hardy MP. Review of Azoospermia. Spermatogenesis. 2014;4:e28218'
    doi: 10.4161/spmg.28218
    pmid: '25105055'
    pmcid: PMC4124057
    url: https://doi.org/10.4161/spmg.28218
    source_license: CC BY-NC 3.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頻度の数値は総説が既報を集約した記載である。AZFa や AZFb の欠失では精子採取が期待できない点も同じ総説の本文に記載されている。遺伝学的検査の国内の保険適用の状況は未確認である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-346 (id: Jlvnl_w)；TBL-02-09-015 (id: JlAKpo0)'
    kokushi: 医学各論 Ⅷ-8-E-③（非閉塞性無精子症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-029
  domain: GU
  subdomain: 男性不妊症の評価
  assertion:
    plain_statement_ja: AUA/ASRM ガイドラインでは、不妊の初期評価は両方のパートナーに対して同時に行い、男性の初期評価には生殖に関する病歴の聴取と1回以上の精液検査を含める。精液検査で1項目以上の異常がある男性は、男性生殖の専門家による評価を受けるべきである。性欲低下、勃起障害、乏精子症または無精子症、精巣萎縮がある場合は、FSH とテストステロンを含むホルモン評価を行う。原発性不妊で無精子症または重度乏精子症（精子濃度500万/mL未満）があり、FSH 上昇か精巣萎縮を伴う場合は、核型と Y 染色体微小欠失の検査が推奨される。精管欠損や特発性の閉塞性無精子症では CFTR 検査を行う。精子 DNA 断片化の検査は初期評価では推奨されない。
    condition:
      region: 米国
      study: AUA/ASRM 男性不妊ガイドライン Part I（2021年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-744
    source: 'Schlegel PN, Sigman M, Collura B, et al. Diagnosis and treatment of infertility in men: AUA/ASRM guideline part I. Fertil Steril. 2021;115(1):54-61'
    doi: 10.1016/j.fertnstert.2020.11.015
    pmid: '33309062'
    pmcid: null
    url: https://doi.org/10.1016/j.fertnstert.2020.11.015
    source_license: 学会ガイドライン（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国の学会ガイドライン2021年版の推奨であり、核型・Y染色体微小欠失・CFTR などの遺伝学的検査の国内の保険適用の状況は未確認である。PMCID は確認できず null とした。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-346 (id: Jlvnl_w)；TBL-02-09-015 (id: JlAKpo0)'
    kokushi: 医学各論 Ⅷ-8-E-④（男性不妊症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-030
  domain: GU
  subdomain: 勃起障害
  assertion:
    plain_statement_ja: 勃起障害（ED）は、性的な満足に十分な勃起を一貫して、または繰り返し得られない、あるいは維持できない状態と定義される。AUA ガイドラインは、治療方針の決定に共同意思決定を中心に据え、禁忌のない治療選択肢はすべて患者に提示すべきだとしている。提示される選択肢には、PDE5 阻害薬などの経口薬、海綿体内注射や尿道内投与、陰圧式勃起補助具、陰茎プロステーシスなどがあり、患者の希望と状況に沿って選択する。
    condition:
      region: 米国
      study: AUA 勃起障害ガイドライン（2018年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-745
    source: 'Burnett AL, Nehra A, Breau RH, et al. Erectile Dysfunction: AUA Guideline. J Urol. 2018;200(3):633-641'
    doi: 10.1016/j.juro.2018.05.004
    pmid: '29746858'
    pmcid: null
    url: https://doi.org/10.1016/j.juro.2018.05.004
    source_license: 学会ガイドライン（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: PDE5 阻害薬の個別の用法・用量や使い分けは、ガイドライン本文の個別ステートメントを確認していないため本カードには含めていない。PDE5 阻害薬を含む ED 治療薬の国内承認・保険適用の状況は未確認である。PMCID は確認できず null とした。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-02-09-005 (id: JlAKpoA)；TBL-02-09-013 (id: JlAKpos)'
    kokushi: 医学各論 Ⅷ-10-D-④（勃起障害、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-031
  domain: GU
  subdomain: 持続勃起症
  assertion:
    plain_statement_ja: 持続勃起症は、性的刺激と無関係に、または性的刺激の後も持続する陰茎の勃起である。低流量型（虚血性）が最も多く、痛みと硬い勃起を伴い、泌尿器科的緊急症である。原因には、鎌状赤血球症などの血栓傾向のある病態、腫瘍、薬剤がある。高流量型（動脈性）は外傷後に生じることが多く、痛みはなく緊急症ではない。低流量型の第一選択の治療は、海綿体の吸引とフェニレフリンの投与である。ドプラ超音波では、低流量型で海綿体動脈の血流の高抵抗化または消失が、高流量型で低抵抗の高血流や仮性動脈瘤、動脈海綿体瘻がみられる。
    condition:
      region: ブラジル
      study: 陰茎救急疾患の画像診断に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-746
    source: 'Dantas GC, Cavalcante F Jr, Yamauchi FI, Racy MCJ, Rahal A Jr, Baroni RH. Penile emergencies: a review of the main conditions. Radiol Bras. 2019;52(2):123-127'
    doi: 10.1590/0100-3984.2017.0072
    pmid: '31019343'
    pmcid: PMC6472861
    url: https://doi.org/10.1590/0100-3984.2017.0072
    source_license: CC BY（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: ブラジルの画像診断総説に基づく記載である。フェニレフリンの海綿体内投与についての国内承認・保険適用の状況は未確認である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-02-09-005 (id: JlAKpoA)'
    kokushi: 医学各論 Ⅷ-10-D-⑤（持続勃起症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-032
  domain: GU
  subdomain: 尿道下裂
  assertion:
    plain_statement_ja: 尿道下裂は、尿道が陰茎の腹側に開口し、陰茎の腹側への弯曲を伴う先天異常で、停留精巣に次いで男児で2番目に多い生殖器の先天異常であり、男児出生200人に1人の頻度で生じる。外尿道口の位置によって遠位型、中間型、近位型に分類され、背側の包皮フードと腹側の皮膚の不足を伴う。包皮は再建に用いるため、環状切除は延期すべきである。近位型で触知できない停留精巣を伴う場合は、性分化疾患が17〜29%に認められるため、電解質、17-ヒドロキシプロゲステロン、核型、腹部超音波による初期評価と内分泌専門医への紹介を行う。手術は生後6〜18か月に行うことが推奨され、遠位型の修復では合併症が5〜10%に生じる。
    condition:
      region: カナダ
      study: 尿道下裂の診断と外科治療に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-747
    source: 'Keays MA, Dave S. Current hypospadias management: diagnosis, surgical management, and long-term patient-centred outcomes. Can Urol Assoc J. 2017;11(1-2Suppl1):S48-S53'
    doi: 10.5489/cuaj.4386
    pmid: '28265319'
    pmcid: PMC5332236
    url: https://doi.org/10.5489/cuaj.4386
    source_license: 学会誌の著作権表示のみ（CC 条件は確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: カナダの小児泌尿器科総説（2017年）に基づく。手術時期の6〜18か月は米国小児科学会の推奨として本文で紹介されているものである。出典のライセンスは学会の著作権表示のみで CC 条件を確認できず UNKNOWN とした。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
    kokushi: 医学各論 Ⅷ-10-B-①（尿道下裂、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-033
  domain: GU
  subdomain: 包茎
  assertion:
    plain_statement_ja: 包茎は、陰茎の炎症性疾患や硬化性苔癬などの炎症の後に後天性に生じることがある。後天性包茎の男性では、26%に糖尿病の既往が認められた。小児では包茎があると亀頭炎が多く、5歳未満では包茎のある児の25%に対し、包茎のない児では6%に亀頭炎がみられた。包皮と亀頭の炎症に対する根治的な治療は環状切除である。
    condition:
      region: 国際
      study: 陰茎炎症性皮膚疾患と環状切除の予防的役割に関する系統的レビュー
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-742
    source: 'Morris BJ, Krieger JN. Penile Inflammatory Skin Disorders and the Preventive Role of Circumcision. Int J Prev Med. 2017;8:32'
    doi: 10.4103/ijpvm.IJPVM_377_16
    pmid: '28567234'
    pmcid: PMC5439293
    url: https://doi.org/10.4103/ijpvm.IJPVM_377_16
    source_license: CC BY-NC-SA 3.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は系統的レビューが集約した観察研究の値である。環状切除（包茎手術）の国内の保険適用の条件は未確認である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
    kokushi: 医学各論 Ⅷ-10-B-②（包茎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-034
  domain: GU
  subdomain: 停留精巣
  assertion:
    plain_statement_ja: 停留精巣は、男児新生児で最も多い泌尿生殖器疾患である。多くは生後3か月までに自然に下降し、6か月までに下降しなければ、その後に自然下降する可能性は低く、生後6か月を超えた男児の約1〜2%にみられる。6か月までに下降しない場合は外科専門医への紹介が推奨される。国際的なガイドラインは、超音波などの画像検査（診断精度を上げず治療方針も変えないため）や、ルーチンのホルモン療法を推奨していない。精巣固定術は、妊孕性の温存と悪性化のリスク低下のため、生後6〜18か月の間に、遅くともこの時期までに実施することが推奨される。片側の停留精巣では不妊率が最大10%に達し、精巣癌のリスクは一般集団の約3倍に上昇するため、思春期後の自己触診が推奨される。
    condition:
      region: 国際
      study: 停留精巣の診断と治療に関する各国ガイドラインの比較総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-748
    source: 'Shin J, Jeon GW. Comparison of diagnostic and treatment guidelines for undescended testis. Clin Exp Pediatr. 2020;63(11):415-421'
    doi: 10.3345/cep.2019.01438
    pmid: '32252147'
    pmcid: PMC7642136
    url: https://doi.org/10.3345/cep.2019.01438
    source_license: CC BY-NC 4.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 各国ガイドラインを比較した総説（韓国、2020年）に基づく。日本のガイドラインの推奨との差異は未確認である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-349 (id: JlvnmAA)'
    kokushi: 医学各論 Ⅷ-10-B-③（停留精巣、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-035
  domain: GU
  subdomain: 精巣・精索水瘤
  assertion:
    plain_statement_ja: 精巣水瘤は、卵円形で圧痛がなく、可動性のある陰嚢内腫瘤として触知され、透光性を示す（光を透過する）ことが診断の手がかりになる。新生児に多くみられ、生後1年以内に自然に消失することが多い。
    condition:
      region: 米国
      study: 陰嚢内腫瘤の評価に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-749
    source: 'Tiemstra JD, Kapoor S. Evaluation of scrotal masses. Am Fam Physician. 2008;78(10):1165-1170'
    doi: null
    pmid: '19035065'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/19035065/
    source_license: © American Academy of Family Physicians（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典論文（2008年）の DOI は PubMed 収載情報に付与が確認できず null とした。PMCID も確認できず null とした。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-350 (id: JlvnmAI)'
    kokushi: 医学各論 Ⅷ-10-B-④（精巣・精索水瘤、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-036
  domain: GU
  subdomain: 精索静脈瘤
  assertion:
    plain_statement_ja: 精索静脈瘤は、触診で「袋の中のミミズ」と表現される陰嚢内の腫瘤として触れ、多くは左側に生じ、仰臥位では小さくなる。男性の15%にみられ、通常は思春期に初めて現れる。原因不明の不妊に対する手術治療については、10件の無作為化比較試験を対象としたコクランレビューで妊孕性の改善が示され、治療必要数は17であった。
    condition:
      region: 米国
      study: 陰嚢内腫瘤の評価に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-749
    source: 'Tiemstra JD, Kapoor S. Evaluation of scrotal masses. Am Fam Physician. 2008;78(10):1165-1170'
    doi: null
    pmid: '19035065'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/19035065/
    source_license: © American Academy of Family Physicians（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 妊孕性改善の数値（治療必要数17）は、本総説が引用したコクランレビューの結果であり、二次資料経由である。出典論文の DOI と PMCID は確認できず null とした。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-350 (id: JlvnmAI)；TBL-01-00-346 (id: Jlvnl_w)'
    kokushi: 医学各論 Ⅷ-10-B-⑤（精索静脈瘤、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-037
  domain: GU
  subdomain: 精巣捻転症
  assertion:
    plain_statement_ja: 急性陰嚢症は、急性に発症した陰嚢の疼痛、腫脹、発赤と定義される医学的緊急症であり、病変は精巣外病変、精巣内病変、外傷に大別される。精巣捻転は急性陰嚢症の原因の一つで、感染（精巣上体炎や精巣炎）や外傷と鑑別しながら緊急に評価する必要がある。陰嚢症状で救急受診し超音波検査を受けた患者164例の後ろ向き検討では、受診理由は陰嚢痛が最も多く、次いで痛みのない腫瘤や腫脹、外傷であり、超音波検査が急性陰嚢症の初期評価に用いられた。
    condition:
      region: イタリア
      study: 急性陰嚢症に対する超音波検査の後ろ向き検討
      population: 陰嚢症状で救急受診した患者164例（単一施設、2008〜2010年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-750
    source: "D'Andrea A, Coppolino F, Cesarano E, Russo A, Cappabianca S, Genovese EA, et al. US in the assessment of acute scrotum. Crit Ultrasound J. 2013;5 Suppl 1:S8"
    doi: 10.1186/2036-7902-5-S1-S8
    pmid: '23902859'
    pmcid: PMC3711727
    url: https://doi.org/10.1186/2036-7902-5-S1-S8
    source_license: CC BY 2.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 精巣の温存率と発症からの経過時間の関係を示す具体的数値は、本出典では確認できなかったため本カードには含めていない。単一施設の後ろ向き検討に基づく記載である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-351 (id: JlvnmAQ)；TBL-01-00-350 (id: JlvnmAI)'
    kokushi: 医学各論 Ⅷ-10-B-⑥（精巣捻転症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-038
  domain: GU
  subdomain: 陰茎折症
  assertion:
    plain_statement_ja: 陰茎折症は陰茎白膜の断裂であり、勃起した陰茎への鈍的外傷（多くは性交時）によって生じる。典型的には、断裂する音とともに突然の痛みが生じ、勃起が急速に消退して、腫脹、血腫、陰茎の偏位を来す。断裂は通常は片側で、遠位の3分の2に多い。画像検査では超音波が第一選択で、結果が確定しない場合は MRI を用いる。治療は原則として緊急の外科的修復であり、血腫や尿道損傷のない小さな断裂など、選択された症例に限って保存的治療が可能である。血尿や尿閉がある場合は、逆行性尿道造影で尿道損傷を評価する。
    condition:
      region: ブラジル
      study: 陰茎救急疾患の画像診断に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-746
    source: 'Dantas GC, Cavalcante F Jr, Yamauchi FI, Racy MCJ, Rahal A Jr, Baroni RH. Penile emergencies: a review of the main conditions. Radiol Bras. 2019;52(2):123-127'
    doi: 10.1590/0100-3984.2017.0072
    pmid: '31019343'
    pmcid: PMC6472861
    url: https://doi.org/10.1590/0100-3984.2017.0072
    source_license: CC BY（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: ブラジルの画像診断総説に基づく記載であり、外科的修復の適応の細部は施設の方針で異なる場合がある。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
    kokushi: 医学各論 Ⅷ-10-E-②（陰茎折症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: GU-039
  domain: GU
  subdomain: 精巣損傷
  assertion:
    plain_statement_ja: 陰嚢の外傷では、血腫、水瘤、血瘤（血液の貯留）、精巣の破裂などが生じる。陰嚢症状で救急受診し超音波検査を受けた164例の後ろ向き検討には外傷の8例が含まれ、超音波検査で精巣破裂1例と陰嚢血腫2例が検出され、破裂した精巣には部分切除を含む精巣摘除が行われた。外傷性病変の初期評価では超音波検査が中心的な役割を果たす。
    condition:
      region: イタリア
      study: 急性陰嚢症に対する超音波検査の後ろ向き検討
      population: 陰嚢症状で救急受診した患者164例（単一施設、2008〜2010年）。うち外傷は8例
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-750
    source: "D'Andrea A, Coppolino F, Cesarano E, Russo A, Cappabianca S, Genovese EA, et al. US in the assessment of acute scrotum. Crit Ultrasound J. 2013;5 Suppl 1:S8"
    doi: 10.1186/2036-7902-5-S1-S8
    pmid: '23902859'
    pmcid: PMC3711727
    url: https://doi.org/10.1186/2036-7902-5-S1-S8
    source_license: CC BY 2.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 単一施設の後ろ向き検討であり、外傷例は8例と少ないため、頻度はこの集団での値である。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
    kokushi: 医学各論 Ⅷ-10-E-③（精巣損傷、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応の一覧

| カードID | 出題基準 | コアカリ |
|---|---|---|
| UR-001 | 医学各論 Ⅷ-4-A-①（腎結石、尿管結石、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I) |
| UR-002 | 医学各論 Ⅷ-4-A-①（腎結石、尿管結石、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I) |
| UR-003 | 医学各論 Ⅷ-4-A-①（腎結石、尿管結石、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I) |
| UR-004 | 医学各論 Ⅷ-4-A-②（膀胱結石、尿道結石、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-341 (id: Jlvnl_I) |
| UR-005 | 医学各論 Ⅷ-4-B-①（上部尿路閉塞、水腎症、a） | PS-02-09-05 (id: JkxnuRs) |
| UR-006 | 医学各論 Ⅷ-4-B-②（下部尿路閉塞性疾患、a） | PS-02-09-05 (id: JkxnuRs) |
| UR-007 | 医学各論 Ⅷ-4-B-①（上部尿路閉塞、水腎症） | PS-02-09-05 (id: JkxnuRs) |
| UR-008 | 医学各論 Ⅷ-4-C-①（神経因性膀胱、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-342 (id: Jlvnl_g) |
| UR-009 | 医学各論 Ⅷ-4-C-①（神経因性膀胱、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-342 (id: Jlvnl_g) |
| UR-010 | 医学各論 Ⅷ-4-C-②（膀胱尿管逆流、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-339 (id: Jlvnl-8) |
| UR-011 | 医学各論 Ⅷ-4-C-②（膀胱尿管逆流、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-339 (id: Jlvnl-8) |
| UR-012 | 医学各論 Ⅷ-5-A-①（急性腎盂腎炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-331 (id: Jlvnl-M) |
| UR-013 | 医学各論 Ⅷ-5-A-①（急性腎盂腎炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-331 (id: Jlvnl-M) |
| UR-014 | 医学各論 Ⅷ-5-A-②（急性単純性膀胱炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-343 (id: Jlvnl_Q) |
| UR-015 | 医学各論 Ⅷ-5-A-②（再発性膀胱炎、複雑性尿路感染症、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-343 (id: Jlvnl_Q) |
| UR-016 | 医学各論 Ⅷ-5-A-③（尿道炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c) |
| UR-017 | 医学各論 Ⅷ-5-A-④（腎膿瘍、b） | PS-02-09-05 (id: JkxnuRs) |
| UR-018 | 医学各論 Ⅷ-5-A-⑤（慢性腎盂腎炎、c） | PS-02-09-05 (id: JkxnuRs) |
| UR-019 | 医学各論 Ⅷ-5-D-①（淋菌性尿道炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c) |
| UR-020 | 医学各論 Ⅷ-5-D-②（非淋菌性尿道炎、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-345 (id: Jlvnl_c) |
| UR-021 | 医学各論 Ⅷ-5-D-③（性器ヘルペス、a） | PS-02-09-05 (id: JkxnuRs) |
| UR-022 | 医学各論 Ⅷ-5-D-④（尖圭コンジローマ、b） | PS-02-09-05 (id: JkxnuRs) |
| UR-023 | 医学各論 Ⅷ-10-A-①（重複腎盂尿管、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-429 (id: JlvnmHg) |
| UR-024 | 医学各論 Ⅷ-10-A-②（異所性尿管開口、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-429 (id: JlvnmHg) |
| UR-025 | 医学各論 Ⅷ-10-A-③（膀胱瘤、a） | PS-02-09-05 (id: JkxnuRs) |
| UR-026 | 医学各論 Ⅷ-10-A-④（単純性腎嚢胞、b） | PS-02-09-05 (id: JkxnuRs) |
| UR-027 | 医学各論 Ⅷ-10-A-⑤（嚢胞腎、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-338 (id: Jlvnl-4) |
| UR-028 | 医学各論 Ⅷ-10-A-⑥（馬蹄腎、b） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-429 (id: JlvnmHg) |
| UR-029 | 医学各論 Ⅷ-10-A-⑦（膀胱憩室、b） | PS-02-09-05 (id: JkxnuRs) |
| UR-030 | 医学各論 Ⅷ-10-D-①（夜尿症、a） | PS-02-09-05 (id: JkxnuRs) |
| UR-031 | 医学各論 Ⅷ-10-D-②（過活動膀胱、a） | PS-02-09-05 (id: JkxnuRs) |
| UR-032 | 医学各論 Ⅷ-10-D-③（腹圧性尿失禁、a） | PS-02-09-05 (id: JkxnuRs) |
| UR-033 | 医学各論 Ⅷ-10-E-①（腎・尿路損傷、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-340 (id: Jlvnl_E) |
| UR-034 | 医学各論 Ⅷ-10-E-⑦（尿路・性器異物、c） | PS-02-09-05 (id: JkxnuRs) |
| GU-001 | 医学各論 Ⅷ-6-A-①（腎細胞癌、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-656 (id: JlvnmdY) |
| GU-002 | 医学各論 Ⅷ-6-A-①（腎細胞癌、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-656 (id: JlvnmdY) |
| GU-003 | 医学各論 Ⅷ-6-A-①（腎細胞癌、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-656 (id: JlvnmdY) |
| GU-004 | 医学各論 Ⅷ-6-A-②（腎盂・尿管癌、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg) |
| GU-005 | 医学各論 Ⅷ-6-A-②（腎盂・尿管癌、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg) |
| GU-006 | 医学各論 Ⅷ-6-B-①（膀胱癌、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg) |
| GU-007 | 医学各論 Ⅷ-6-B-①（膀胱癌、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg) |
| GU-008 | 医学各論 Ⅷ-6-B-①（膀胱癌、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg) |
| GU-009 | 医学各論 Ⅷ-6-B-②（尿膜管癌、c） | PS-02-09-05 (id: JkxnuRs) |
| GU-010 | 医学各論 Ⅷ-6-C-①（前立腺肥大症、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-347 (id: Jlvnl_0) |
| GU-011 | 医学各論 Ⅷ-6-C-①（前立腺肥大症、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-347 (id: Jlvnl_0) |
| GU-012 | 医学各論 Ⅷ-6-C-②（前立腺癌、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk) |
| GU-013 | 医学各論 Ⅷ-6-C-②（前立腺癌、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk) |
| GU-014 | 医学各論 Ⅷ-6-C-②（前立腺癌、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk) |
| GU-015 | 医学各論 Ⅷ-6-C-②（前立腺癌、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk) |
| GU-016 | 医学各論 Ⅷ-6-C-②（前立腺癌、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk) |
| GU-017 | 医学各論 Ⅷ-6-C-②（前立腺癌、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-658 (id: Jlvnmdk) |
| GU-018 | 医学各論 Ⅷ-6-B-①（膀胱癌、a） | PS-02-09-05 (id: JkxnuRs)；TBL-01-00-657 (id: Jlvnmdg) |
| GU-019 | 医学各論 Ⅷ-6-C-③（精巣癌(セミノーマ)、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-659 (id: Jlvnmds) |
| GU-020 | 医学各論 Ⅷ-6-C-④（精巣癌(非セミノーマ)、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-659 (id: Jlvnmds) |
| GU-021 | 医学各論 Ⅷ-6-C-③（精巣癌(セミノーマ)、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-659 (id: Jlvnmds) |
| GU-022 | 医学各論 Ⅷ-6-C-⑤（陰茎癌、b） | PS-02-10-05 (id: JkxnuSA) |
| GU-023 | 医学各論 Ⅷ-5-B-①（前立腺炎、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-348 (id: Jlvnl_8) |
| GU-024 | 医学各論 Ⅷ-5-B-②（精巣上体炎、a） | PS-02-10-05 (id: JkxnuSA) |
| GU-025 | 医学各論 Ⅷ-5-B-③（精巣炎、b） | PS-02-10-05 (id: JkxnuSA) |
| GU-026 | 医学各論 Ⅷ-5-B-④（亀頭包皮炎、b） | PS-02-10-05 (id: JkxnuSA) |
| GU-027 | 医学各論 Ⅷ-8-E-②（閉塞性無精子症、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-346 (id: Jlvnl_w) |
| GU-028 | 医学各論 Ⅷ-8-E-③（非閉塞性無精子症、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-346 (id: Jlvnl_w)；TBL-02-09-015 (id: JlAKpo0) |
| GU-029 | 医学各論 Ⅷ-8-E-④（男性不妊症、b） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-346 (id: Jlvnl_w)；TBL-02-09-015 (id: JlAKpo0) |
| GU-030 | 医学各論 Ⅷ-10-D-④（勃起障害、b） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-005 (id: JlAKpoA)；TBL-02-09-013 (id: JlAKpos) |
| GU-031 | 医学各論 Ⅷ-10-D-⑤（持続勃起症、c） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-005 (id: JlAKpoA) |
| GU-032 | 医学各論 Ⅷ-10-B-①（尿道下裂、a） | PS-02-10-05 (id: JkxnuSA) |
| GU-033 | 医学各論 Ⅷ-10-B-②（包茎、a） | PS-02-10-05 (id: JkxnuSA) |
| GU-034 | 医学各論 Ⅷ-10-B-③（停留精巣、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-349 (id: JlvnmAA) |
| GU-035 | 医学各論 Ⅷ-10-B-④（精巣・精索水瘤、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-350 (id: JlvnmAI) |
| GU-036 | 医学各論 Ⅷ-10-B-⑤（精索静脈瘤、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-350 (id: JlvnmAI)；TBL-01-00-346 (id: Jlvnl_w) |
| GU-037 | 医学各論 Ⅷ-10-B-⑥（精巣捻転症、a） | PS-02-10-05 (id: JkxnuSA)；TBL-01-00-351 (id: JlvnmAQ)；TBL-01-00-350 (id: JlvnmAI) |
| GU-038 | 医学各論 Ⅷ-10-E-②（陰茎折症、a） | PS-02-10-05 (id: JkxnuSA) |
| GU-039 | 医学各論 Ⅷ-10-E-③（精巣損傷、a） | PS-02-10-05 (id: JkxnuSA) |

## 4. 未解決事項

- スキーマと接頭辞（担当：取り込み側）：接頭辞 UR・GU は手元のスキーマと domains.yaml に未追加。取り込み時に追加が必要。
- ライセンス UNKNOWN（担当：取り込み側で出版社ページを再確認）：SRC-692、693、698（UR）、SRC-709、711（U2）、SRC-728（GU、DOI も null）、SRC-747（GU）。SRC-737・749 は DOI が確認できなかった出典（PMID は確認済み）。
- 薬剤の国内承認・保険適用（担当：取り込み側で PMDA 確認）：UR-002、009、011、013〜016、019〜022、027、030、031、GU-002、004〜007、010、015、016、018〜020、023、024、026、030、031 は、各カードの uncertainty に「未確認」と明記した。
- 性感染症の地域差（担当：取り込み側の判断）：UR-019〜022 と GU-024 は CDC 2021（米国）の推奨に基づく。日本の性感染症の診断・治療の推奨との差異は未検証で、日本側の別カード化は統合側の判断待ち。
- 数値を入れなかった・範囲を絞った項目：UR-002（ESWL・内視鏡の選択基準は出典の範囲外）、UR-012（複雑性腎盂腎炎の割合は出典内で抄録と本文が異なるため不採用）、UR-018（慢性腎盂腎炎は逆流性腎症の出典で代替し、閉塞性などの機序は未カバー）、UR-025・033（分類・術式や重症度別の治療は本文未確認）、GU-001（TNM の区分・腫瘍径の閾値）、GU-003（環境リスク因子の定量）、GU-008（膀胱鏡などの診断手順）、GU-013（欧州側の PSA 検診推奨）、GU-030（PDE5 阻害薬の個別用量・作用時間は二次資料のみ）、GU-037（精巣温存率と経過時間の関係は割当出典で確認できず）。
- 表から読み取った値（各カードの uncertainty に明記）：GU-014（前立腺癌のリスク分類の境界値）、GU-021（精巣腫瘍の S 分類・IGCCCG の閾値と割合）、GU-023（前立腺炎の NIH 分類）。GU-036 の治療必要数17は二次資料経由と明記した。UR-030（夜尿症）も数値は二次資料経由と明記した。

## 5. 次回への引き継ぎ

- 欠番：なし（UR-001〜034、GU-001〜039 は連番）。未使用 SRC：SRC-705、706、720、707・740（CDC ガイドラインの SRC-703 への統合で空いた分）。番号は詰めていない。
- カードのない出題基準の小項目：対象55項目にはない。
- 第18回との境界：性感染症のうち女性側の炎症（腟炎・PID）は第18回 GY で扱う（本回の UR-019〜022 は尿道炎・性器の病変に絞った）。前立腺・精巣の炎症は GU で扱い済み。子宮・卵巣の腫瘍は第18回、月経異常・不妊（女性側）・避妊・更年期は第19回 RP で扱い、GU-027〜029（男性不妊）と重複させない。
- 扱った出典の中心：EAU・AUA・IDSA のガイドライン、CDC 性感染症治療ガイドライン2021（SRC-703、既存番号として今後も使うこと）、日本泌尿器科学会関連の英語版、主要なメタ解析と RCT（RIVUR、α遮断薬のメタ解析など）。
