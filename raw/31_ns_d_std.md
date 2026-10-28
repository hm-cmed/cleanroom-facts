# 第31回 事実票（BD・OS・BO）

> この版は Claude Code が `raw/31_ns_d.md`（Muse の原本）から機械的に作った。原本の形の問題（```yaml の後の改行抜け、独自のカードの形）は第28〜30回と同じで、同じ方法で標準の形に移した（詳しくは `raw/28_ns_a_std.md` の冒頭）。主張文・数値・識別子は変えていない。

第Ⅸ章 神経・運動器の第4回。骨系統疾患・代謝性骨疾患（BD）、運動器疾患（OS）、骨・軟部腫瘍（BO）。対象56項目すべてにカードがある。欠番はない。

## 1. 抽出元ホワイトリスト

| SRC | 出典 | DOI | PMID | ライセンス | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-927 | Soen S, Fukunaga M, Sugimoto T, Sone T, Fujiwara S, Endo N, Gorai I, Shiraki M, Hagino H, Hosoi T, Ohta H, Yoneda T, Tomomitsu T; Japanese Society for Bone and Mineral Research and Japan Osteoporosis Society Joint Review Committee for the Revision of the Diagnostic Criteria for Primary Osteoporosis. Diagnostic criteria for primary osteoporosis: year 2012 revision. J Bone Miner Metab. 2013;31(3):247-257. | 10.1007/s00774-013-0447-8 | 23553500 | RESTRICTED | RESTRICTED | 既存出典（前の分野で登録済み。本回では新しい番号を付けず既存番号を使用） |
| SRC-932 | Munns CF, Shaw N, Kiely M, Specker BL, Thacher TD, Ozono K, Michigami T, Tiosano D, Mughal MZ, Mäkitie O, et al. Global Consensus Recommendations on Prevention and Management of Nutritional Rickets. J Clin Endocrinol Metab. 2016;101(2):394-415. | 10.1210/jc.2015-2175 | 26745253 | RESTRICTED | RESTRICTED | 既存出典（前の分野で登録済み。本回では新しい番号を付けず既存番号を使用） |
| SRC-992 | FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. Arthritis Care Res (Hoboken). 2020;72(6):744-760. | 10.1002/acr.24180 | 32391934 | UNKNOWN | UNKNOWN | 既存出典（前の分野で登録済み。本回では新しい番号を付けず既存番号を使用） |
| SRC-1831 | 骨粗鬆症の予防と治療ガイドライン作成委員会（日本骨粗鬆症学会・日本骨代謝学会・骨粗鬆症財団）（編）. 骨粗鬆症の予防と治療ガイドライン2025年版. ライフサイエンス出版; 2025 | なし | なし | 学会ガイドライン書籍（CC表示なし） | RESTRICTED | 日本骨粗鬆症学会サイトで公開された公式PDFで本文を確認。第4章D-b薬物治療開始基準（図4-2）とD-c治療薬選択の考え方、第5章の収載薬（デノスマブ、アバロパラチド、ロモソズマブ等）を確認。2015年版以来10年ぶりの改訂版 |
| SRC-1832 | Kanis JA, et al. FRAX and the assessment of fracture probability in men and women from the UK. Osteoporos Int. 2008;19(4):385-397 | 10.1007/s00198-007-0543-5 | 18292978 | CC BY-NC 4.0 | RESTRICTED | PubMed APIで書誌・DOI・PMIDを照合し、抄録でFRAXの枠組み（臨床危険因子±大腿骨頚部骨密度による大腿骨近位部骨折・主要骨粗鬆症性骨折の10年確率）を確認。ライセンスはCrossrefのlicense欄（CC BY-NC 4.0）で確認 |
| SRC-1833 | US Preventive Services Task Force. Screening for Osteoporosis to Prevent Fractures: US Preventive Services Task Force Recommendation Statement. JAMA. 2025 | 10.1001/jama.2024.27154 | 39808425 | © 2025 American Medical Association and United States Government（All rights reserved） | RESTRICTED | PubMed APIで書誌・DOI・PMIDを照合し、USPSTF公式サイトの勧告文全文で対象集団別の勧告（女性はB勧告、男性はIステートメント）とスクリーニング方法（中軸骨DXA±骨折リスク評価）を確認 |
| SRC-1834 | Cummings SR, et al. Denosumab for prevention of fractures in postmenopausal women with osteoporosis. N Engl J Med. 2009 | 10.1056/NEJMoa0809493 | 19671655 | N Engl J Med（CC表示なし） | RESTRICTED | PubMed APIで書誌・DOI・PMIDを照合し、抄録でFREEDOM試験の主要結果（椎体骨折リスク68%低下、大腿骨近位部骨折40%低下、非椎体骨折20%低下）を確認 |
| SRC-1835 | Miller PD, et al. Effect of abaloparatide vs placebo on new vertebral fractures in postmenopausal women with osteoporosis: a randomized clinical trial. JAMA. 2016 | 10.1001/jama.2016.11136 | 27533157 | JAMA（CC表示なし） | RESTRICTED | PubMed APIで書誌・DOI・PMIDを照合し、抄録でACTIVE試験の枠組み（アバロパラチド80μg連日、テリパラチド20μgは非盲検参照群、18か月）と高カルシウム血症の頻度（3.4%対6.4%）を確認 |
| SRC-1836 | Cosman F, et al. Romosozumab treatment in postmenopausal women with osteoporosis. N Engl J Med. 2016 | 10.1056/NEJMoa1607948 | 27641143 | N Engl J Med（CC表示なし） | RESTRICTED | PubMed APIで書誌・DOI・PMIDを照合し、抄録でFRAME試験の主要結果（12か月時点の新規椎体骨折0.5%対1.8%、73%低下、その後デノスマブへ移行）を確認 |
| SRC-1837 | Singer FR, et al. Paget's disease of bone: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2014 | 10.1210/jc.2014-2910 | 25406796 | J Clin Endocrinol Metab（The Endocrine Society、CC表示なし） | RESTRICTED | PubMed APIで書誌・DOI・PMIDを照合し、抄録で診断（単純X線、骨シンチ、血清総ALP）と治療（ビスホスホネート、ゾレドロン酸5mg単回静注が第一選択）の推奨を確認 |
| SRC-1838 | Carpenter TO, et al. Burosumab therapy in children with X-linked hypophosphatemia. N Engl J Med. 2018 | 10.1056/NEJMoa1714641 | 29791829 | N Engl J Med（CC表示なし） | RESTRICTED | PubMed APIで書誌・DOI・PMIDを照合し、抄録でXLHの病態（FGF23分泌亢進）と第2相試験の結果（Thacherスコア改善、血清リン上昇、ALP低下）を確認 |
| SRC-1839 | Savarirayan R, et al. Once-daily, subcutaneous vosoritide therapy in children with achondroplasia: a randomised, double-blind, phase 3, placebo-controlled, multicentre trial. Lancet. 2020 | 10.1016/S0140-6736(20)31541-5 | 32891212 | Lancet（Elsevier、CC表示なし） | RESTRICTED | PubMed APIで書誌・DOI・PMIDを照合し、抄録で第3相試験の主要結果（年間成長速度の調整済み群間差+1.57cm/年、95%信頼区間1.22〜1.93）を確認 |
| SRC-1840 | Marini JC, et al. Osteogenesis imperfecta. Nat Rev Dis Primers. 2017;3:17052 | 10.1038/nrdp.2017.52 | 28820180 | Nat Rev Dis Primers（Springer Nature、CC表示なし） | RESTRICTED | PubMed APIで書誌・DOI・PMIDを照合し、抄録で原因（COL1A1・COL1A2の常染色体優性変異が約85%）と診断の枠組みを確認 |
| SRC-1841 | Pauli RM. Achondroplasia: a comprehensive clinical review. Orphanet J Rare Dis. 2019;14:1 | 10.1186/s13023-018-0972-6 | 30606190 | CC BY 4.0 | OPEN | PubMed APIで書誌・DOI・PMID・PMCID（PMC6318916）を照合し、PMCの全文で遺伝学（FGFR3のG380R、出生頻度1/25,000〜30,000）と合併症（大後頭孔狭窄、水頭症の機序）を確認。ライセンスは本文のCC BY 4.0表示とCrossrefで確認 |
| SRC-1842 | Trends in hip fracture incidence in Japan: estimates based on nationwide hip fracture surveys from 1992 to 2017. JBMR Plus. 2021;5(2):e10428 | 10.1002/jbm4.10428 | 33615101 | CC BY 4.0 | OPEN | PubMed APIで書誌・DOI・PMIDを照合し、抄録で2017年の推計発生数（約193,400件、男性44,100件・女性149,300件）と年齢調整発生率の推移を確認。ライセンスはCrossrefのlicense欄（CC BY 4.0）で確認 |
| SRC-1843 | Bliuc D, et al. Mortality risk associated with low-trauma osteoporotic fracture and subsequent fracture in men and women. JAMA. 2009 | 10.1001/jama.2009.50 | 19190316 | JAMA（CC表示なし） | RESTRICTED | PubMed APIで書誌・DOI・PMIDを照合し、抄録でDubboコホートの骨折型別標準化死亡比（大腿骨近位部骨折：女性2.43・男性3.51、椎体骨折：女性1.82・男性2.12）と再骨折の影響を確認 |
| SRC-1844 | Haffner D, et al. Clinical practice recommendations for the diagnosis and management of X-linked hypophosphataemia. Nat Rev Nephrol. 2019 | 10.1038/s41581-019-0152-5 | 31068690 | CC BY 4.0 | OPEN | PubMed APIで書誌・DOI・PMIDを照合し、抄録でXLHの診断の推奨（低リン血症＋腎性リン喪失、遺伝子検査・FGF23測定での確認）と成人病変（偽骨折など）を確認。ライセンスはCrossrefのlicense欄（CC BY 4.0）で確認 |
| SRC-1845 | 厚生労働省. 指定難病に係る診断基準及び重症度分類等：274 骨形成不全症（難病情報センター掲載） | なし | なし | 政府標準利用規約に基づく公的資料（要最終確認） | GOV_JP | 厚生労働省・難病情報センターの診断基準文書で、症状（骨脆弱性、成長障害、青色強膜、象牙質形成不全、難聴など）、検査所見、遺伝学的検査（COL1A1・COL1A2を含む）の項目を確認。指定難病の告示番号274は厚生労働省の指定難病一覧でも確認 |
| SRC-1846 | Aletaha D, Neogi T, Silman AJ, et al. 2010 Rheumatoid arthritis classification criteria: an American College of Rheumatology/European League Against Rheumatism collaborative initiative. Arthritis Rheum. 2010;62(9):2569-2581 | 10.1002/art.27584 | 20872595 | Wiley（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合し、抄録で4ドメインの合計6点以上（10点満点）で definite RA に分類すること、早期例への感度を意図した基準であることを確認 |
| SRC-1847 | Harigai M, Kaneko Y, Tanaka E, et al. 2024 Update of the Japan College of Rheumatology Clinical Practice Guidelines for the Management of Rheumatoid Arthritis: Secondary publication. Mod Rheumatol. 2025;35(3):387-401 | 10.1093/mr/roaf006 | 39820350 | 日本リウマチ学会ガイドラインの二次掲載（CC表示なし） | RESTRICTED | PubMed・Crossrefで照合し、抄録で治療目標と薬物治療アルゴリズムは2020年版から変更なし、JAK阻害薬・リツキシマブ等の推奨が更新されたことを確認。日本語版ガイドライン本体（診断と治療社、2024）の二次掲載 |
| SRC-1848 | Smolen JS, Landewé RBM, Bergstra SA, et al. EULAR recommendations for the management of rheumatoid arthritis with synthetic and biological disease-modifying antirheumatic drugs: 2022 update. Ann Rheum Dis. 2023;82(1):3-18 | 10.1136/ard-2022-223356 | 36357155 | BMJ（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。MTXを第一選択のアンカードラッグとし、treat-to-target で寛解（到達困難な場合は低疾患活動性）を目指す推奨の根拠として使用 |
| SRC-1849 | van der Heijde D. How to read radiographs according to the Sharp/van der Heijde method. J Rheumatol. 1999;26(3):743-745 | なし | 10090194 | The Journal of Rheumatology（CC表示なし） | RESTRICTED | PubMedで書誌・PMIDを照合。手足のX線でびらんと関節裂隙狭小化を採点する Sharp/van der Heijde 変法の原法論文 |
| SRC-1850 | Abhishek A, Tedeschi SK, Pascart T, et al. The 2023 ACR/EULAR classification criteria for calcium pyrophosphate deposition disease. Ann Rheum Dis. 2023;82(10):1248-1257 | 10.1136/ard-2023-224575 | 37495237 | BMJ（© Author(s) 2023、商業利用不可の表示あり） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合し、抄録で関節液中CPP結晶または crowned dens 症候群があれば分類可能、重み付きスコア56点超でも分類可能、感度92.2%・特異度87.9%（derivation cohort）を確認 |
| SRC-1851 | Reilly D, Kamineni S. Olecranon bursitis. J Shoulder Elbow Surg. 2016;25(1):158-167 | 10.1016/j.jse.2015.08.032 | 26577126 | Elsevier（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。肘頭滑液包炎の感染性・非感染性の鑑別と穿刺液検査の根拠として使用 |
| SRC-1852 | Peters-Veluthamaningal C, van der Windt DA, Winters JC, Meyboom-de Jong B. Corticosteroid injection for trigger finger in adults. Cochrane Database Syst Rev. 2009;(1):CD005617 | 10.1002/14651858.CD005617.pub2 | 19160256 | Cochrane Library／Wiley（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。ばね指に対するステロイド腱鞘内注射の有効性の根拠として使用 |
| SRC-1853 | Ilyas AM, Ast M, Schaffer AA, Thoder J. De quervain tenosynovitis of the wrist. J Am Acad Orthop Surg. 2007;15(12):757-764 | 10.5435/00124635-200712000-00009 | 18063716 | AAOS（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。第一伸筋区画の狭窄性腱鞘炎の所見（Finkelsteinテスト）と治療の根拠として使用 |
| SRC-1854 | Hunter DJ, Bierma-Zeinstra S. Osteoarthritis. Lancet. 2019;393(10182):1745-1759 | 10.1016/S0140-6736(19)30417-9 | 31034380 | Elsevier（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。変形性関節症の病態（軟骨変性と関節全体の疾患）、危険因子、画像所見の総論として使用 |
| SRC-1855 | Bannuru RR, Osani MC, Vaysbrot EE, et al. OARSI guidelines for the non-surgical management of knee, hip, and polyarticular osteoarthritis. Osteoarthritis Cartilage. 2019;27(11):1578-1589 | 10.1016/j.joca.2019.06.011 | 31278997 | Elsevier（テキストマイニング用ライセンスのみ、CC表示なし） | RESTRICTED | PubMed・Crossrefで照合。教育・運動療法・減量を中核とし、NSAIDs等の薬物療法を段階的に用いる非手術管理の階層の根拠として使用 |
| SRC-1856 | Rogers LC, Frykberg RG, Armstrong DG, et al. The Charcot foot in diabetes. Diabetes Care. 2011;34(9):2123-2129 | 10.2337/dc11-0844 | 21868781 | American Diabetes Association（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合し、抄録で糖尿病性 Charcot 足が神経障害・外傷・骨代謝異常を背景とする炎症性症候群で、骨・関節の破壊と変形を来すことを確認 |
| SRC-1857 | Srivastava A, Santagostino E, Dougall A, et al. WFH Guidelines for the Management of Hemophilia, 3rd edition. Haemophilia. 2020;26 Suppl 6:1-158 | 10.1111/hae.14046 | 32744769 | Wiley（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。反復する関節内出血による血友病性関節症と標的関節、定期補充（予防投与）の位置づけの根拠として使用 |
| SRC-1858 | Gude W, Morelli V. Ganglion cysts of the wrist: pathophysiology, clinical picture, and management. Curr Rev Musculoskelet Med. 2008;1(3-4):205-211 | 10.1007/s12178-008-9033-4 | 19468907 | CC BY-NC 2.0 | RESTRICTED | PubMed・Crossrefで照合し、抄録で約50%が自然消退すること、穿刺吸引は再発が多く、摘出術は再発が少ないが合併症が多いことを確認。ライセンスは Crossref で CC BY-NC 2.0 を確認 |
| SRC-1859 | Baird EO, Kang QK. Prophylaxis of heterotopic ossification - an updated review. J Orthop Surg Res. 2009;4:12 | 10.1186/1749-799X-4-12 | 19379483 | CC BY 2.0 | OPEN | PubMed・Crossrefで照合。Crossref のライセンス情報で CC BY 2.0 を確認。外傷・手術後および神経損傷後の異所性骨化と、NSAIDs・放射線照射による予防の根拠として使用 |
| SRC-1860 | Schett G, Lories RJ, D'Agostino MA, et al. Enthesitis: from pathophysiology to treatment. Nat Rev Rheumatol. 2017;13(12):731-741 | 10.1038/nrrheum.2017.188 | 29158573 | Nature Portfolio（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。腱付着部炎が脊椎関節炎の中心的病変であることの根拠として使用 |
| SRC-1861 | Cross D, Matullo KS. Kienböck disease. Orthop Clin North Am. 2014;45(1):141-152 | 10.1016/j.ocl.2013.09.004 | 24267215 | Elsevier（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。月状骨壊死と Lichtman 分類による病期評価の根拠として使用 |
| SRC-1862 | Karim AR, Cherian JJ, Jauregui JJ, et al. Osteonecrosis of the knee: review. Ann Transl Med. 2015;3(1):6 | 10.3978/j.issn.2305-5839.2014.11.13 | 25705638 | AME Publishing（CC表示を本調査では確認できず） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。特発性膝骨壊死（高齢女性、大腿骨内側顆、夜間痛）の臨床像の根拠として使用 |
| SRC-1863 | Hurst LC, Badalamente MA, Hentz VR, et al. Injectable collagenase clostridium histolyticum for Dupuytren's contracture. N Engl J Med. 2009;361(10):968-979 | 10.1056/NEJMoa0810866 | 19726771 | NEJM（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。Dupuytren拘縮に対するコラゲナーゼ注射（CORD試験）の根拠として使用 |
| SRC-1864 | Hutchinson DT, Rane AA, Montanez A. The Natural History of Pediatric Trigger Thumb in the United States. J Hand Surg Am. 2021;46(5):424.e1-424.e7 | 10.1016/j.jhsa.2020.10.016 | 33436280 | Elsevier（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合し、抄録で5年時点で32%（95%CI 20〜43%）が自然軽快したこと、初診時IP関節屈曲30°超では自然軽快が乏しいことを確認 |
| SRC-1865 | Burkhart SS, De Beer JF. Traumatic glenohumeral bone defects and their relationship to failure of arthroscopic Bankart repairs: significance of the inverted-pear glenoid and the humeral engaging Hill-Sachs lesion. Arthroscopy. 2000;16(7):677-694 | 10.1053/jars.2000.17715 | 11027751 | Elsevier（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。関節窩骨欠損と engaging Hill-Sachs 病変が鏡視下 Bankart 修復の失敗因子であることの根拠として使用 |
| SRC-1866 | Illig KA, Donahue D, Duncan A, et al. Reporting standards of the Society for Vascular Surgery for thoracic outlet syndrome. J Vasc Surg. 2016;64(3):e23-e35 | 10.1016/j.jvs.2016.04.039 | 27565607 | Society for Vascular Surgery（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合。胸郭出口症候群の型（神経性・静脈性・動脈性）と評価の標準の根拠として使用 |
| SRC-1867 | Bisset L, Beller E, Jull G, et al. Mobilisation with movement and exercise, corticosteroid injection, or wait and see for tennis elbow: randomised trial. BMJ. 2006;333(7575):939 | 10.1136/bmj.38961.584653.AE | 17012266 | BMJ（CC表示なし） | RESTRICTED | PubMedで書誌・DOI・PMIDを照合し、抄録でステロイド注射は6週時点で優れるが再発が多く（成功例65例中47例が後退）、52週では理学療法より転帰が劣ることを確認 |
| SRC-1868 | Willy RW, Hoglund LT, Barton CJ, et al. Patellofemoral Pain. J Orthop Sports Phys Ther. 2019;49(9):CPG1-CPG95 | 10.2519/jospt.2019.0302 | 31475628 | JOSPT（CC表示なし） | RESTRICTED | PubMed・Crossref で書誌・DOI・PMID を照合し、出版社ページで本文を確認。推奨事項の要約で診断基準（膝蓋骨周囲・後面の痛みが、しゃがみ込み・階段昇降・長時間坐位など膝屈曲位で膝蓋大腿関節に負荷がかかる活動で再現されること）と、股関節・膝関節の複合運動療法の推奨を確認。本文の疫学記述で女性の発生率が男性より高いことを確認。Crossref の license 欄に CC 表示なし |
| SRC-1869 | Zheng W, Li H, Hu K, Li L, Bei M. Chondromalacia patellae: current options and emerging cell therapies. Stem Cell Res Ther. 2021;12(1):412 | 10.1186/s13287-021-02478-4 | 34275494 | CC BY 4.0 | OPEN | PubMed・Crossref で書誌・DOI・PMID を照合し、抄録で若年者に多く膝前面痛を呈すること、初期病変が関節軟骨の軟化・膨化・浮腫であること、可逆性の場合と膝蓋大腿関節の変形性関節症へ進行する場合があることを確認。ライセンスは Crossref の license 欄で CC BY 4.0 を確認 |
| SRC-1871 | Ramirez J. Adhesive Capsulitis: Diagnosis and Management. Am Fam Physician. 2019;99(5):297-300 | なし | 30811157 | （なし） | UNKNOWN | PubMed で書誌・抄録を確認。PubMed の書誌情報に DOI の登録なし |
| SRC-1872 | Rangan A, Brealey SD, Keding A, et al. Management of adults with primary frozen shoulder in secondary care (UK FROST): a multicentre, pragmatic, three-arm, superiority randomised clinical trial. Lancet. 2020;396(10256):977-989 | 10.1016/S0140-6736(20)31965-6 | 33010843 | （なし） | RESTRICTED | PubMed で書誌・抄録を確認。Crossref の license 欄で CC BY-NC-ND 4.0 を確認 |
| SRC-1873 | Yamamoto A, Takagishi K, Osawa T, et al. Prevalence and risk factors of a rotator cuff tear in the general population. J Shoulder Elbow Surg. 2010;19(1):116-120 | 10.1016/j.jse.2009.04.006 | 19540777 | （なし） | UNKNOWN | PubMed で書誌・抄録を確認。Crossref の license 欄はテキストマイニング用ライセンスのみ |
| SRC-1874 | Kukkonen J, Ryösä A, Joukainen A, et al. Operative versus conservative treatment of small, nontraumatic supraspinatus tears in patients older than 55 years: over 5-year follow-up of a randomized controlled trial. J Shoulder Elbow Surg. 2021;30(11):2455-2464 | 10.1016/j.jse.2021.03.133 | 33774172 | （なし） | RESTRICTED | PubMed で書誌・抄録を確認。Crossref の license 欄で CC BY-NC-ND 4.0 を確認 |
| SRC-1875 | Krul M, van der Wouden JC, Kruithof EJ, et al. Manipulative interventions for reducing pulled elbow in young children. Cochrane Database Syst Rev. 2017;7(7):CD007759 | 10.1002/14651858.CD007759.pub4 | 28753234 | PMC6483272 | UNKNOWN | PubMed で書誌・抄録を確認。Crossref の license 欄はテキストマイニング用ライセンスのみ |
| SRC-1876 | Jingushi S, Ohfuji S, Sofue M, et al. Osteoarthritis hip joints in Japan: involvement of acetabular dysplasia. J Orthop Sci. 2011;16(2):156-164 | 10.1007/s00776-011-0025-7 | 21359510 | （なし） | RESTRICTED | PubMed で書誌・抄録を確認。Journal of Orthopaedic Science は CC BY-NC-ND のため RESTRICTED |
| SRC-1877 | Learmonth ID, Young C, Rorabeck C. The operation of the century: total hip replacement. Lancet. 2007;370(9597):1508-1519 | 10.1016/S0140-6736(07)60457-7 | 17964352 | （なし） | RESTRICTED | PubMed で書誌・抄録を確認 |
| SRC-1878 | Ömeroğlu H, Yüksel S, Demir P, et al. An Eastern Europe and Middle East multinational expert Delphi consensus study on the prevention, diagnosis, and treatment of developmental dysplasia of the hip before walking age. Int Orthop. 2024;48(6):1373-1380 | 10.1007/s00264-023-06077-1 | 38150007 | （なし） | UNKNOWN | PubMed で書誌・抄録を確認。Crossref の license 欄はテキストマイニング用ライセンスのみ |
| SRC-1879 | Funk JF, Lebek S. Epiphyseolysis capitis femoris: new aspects of diagnostics and therapy. Orthopade. 2014;43(8):742-749 | 10.1007/s00132-013-2226-6 | 25116242 | （なし） | UNKNOWN | PubMed で書誌・抄録（英語）を確認。Crossref の license 欄はテキストマイニング用ライセンスのみ |
| SRC-1880 | Fukushima W, Fujioka M, Kubo T, et al. Nationwide epidemiologic survey of idiopathic osteonecrosis of the femoral head. Clin Orthop Relat Res. 2010;468(10):2715-2724 | 10.1007/s11999-010-1292-x | 20224959 | PMC2939331 | UNKNOWN | PubMed で書誌・抄録を確認。Crossref の license 欄に表示なし |
| SRC-1881 | Ando W, Sakai T, Fukushima W, et al. Japanese Orthopaedic Association 2019 Guidelines for osteonecrosis of the femoral head. J Orthop Sci. 2021;26(1):46-68 | 10.1016/j.jos.2020.06.013 | 33388233 | （なし） | RESTRICTED | PubMed で書誌・抄録を確認。原典は特発性大腿骨頭壊死症診療ガイドライン2019（厚生労働省指定難病研究班・日本整形外科学会）。JOS は CC BY-NC-ND のため RESTRICTED |
| SRC-1882 | Herring JA, Kim HT, Browne R. Legg-Calve-Perthes disease. Part II: Prospective multicenter study of the effect of treatment on outcome. J Bone Joint Surg Am. 2004;86(10):2121-2134 | なし | 15466720 | （なし） | UNKNOWN | PubMed で書誌・抄録を確認。PubMed の書誌情報に DOI の登録なし |
| SRC-1883 | Yoshimura N, Muraki S, Oka H, et al. Prevalence of knee osteoarthritis, lumbar spondylosis, and osteoporosis in Japanese men and women: the research on osteoarthritis/osteoporosis against disability study. J Bone Miner Metab. 2009;27(5):620-628 | 10.1007/s00774-009-0080-8 | 19568689 | （なし） | UNKNOWN | PubMed で書誌・抄録を確認。Crossref の license 欄はテキストマイニング用ライセンスのみ |
| SRC-1885 | Pereira TV, Jüni P, Saadat P, et al. Viscosupplementation for knee osteoarthritis: systematic review and meta-analysis. BMJ. 2022;378:e069722 | 10.1136/bmj-2022-069722 | 36333100 | PMC9258606 | RESTRICTED | PubMed で書誌・抄録を確認。Crossref の license 欄で CC BY-NC 4.0 を確認 |
| SRC-1886 | Skou ST, Roos EM, Laursen MB, et al. A Randomized, Controlled Trial of Total Knee Replacement. N Engl J Med. 2015;373(17):1597-1606 | 10.1056/NEJMoa1505467 | 26488691 | （なし） | RESTRICTED | PubMed で書誌・抄録を確認 |
| SRC-1887 | Ladenhauf HN, Seitlinger G, Green DW. Osgood-Schlatter disease: a 2020 update of a common knee condition in children. Curr Opin Pediatr. 2020;32(1):107-112 | 10.1097/MOP.0000000000000842 | 31714260 | （なし） | UNKNOWN | PubMed で書誌・抄録を確認。Crossref の license 欄に表示なし |
| SRC-1888 | Sihvonen R, Paavola M, Malmivaara A, et al. Arthroscopic partial meniscectomy versus sham surgery for a degenerative meniscal tear. N Engl J Med. 2013;369(26):2515-2524 | 10.1056/NEJMoa1305189 | 24369076 | （なし） | RESTRICTED | PubMed で書誌・抄録を確認 |
| SRC-1889 | Nix S, Smith M, Vicenzino B. Prevalence of hallux valgus in the general population: a systematic review and meta-analysis. J Foot Ankle Res. 2010;3:21 | 10.1186/1757-1146-3-21 | 20868524 | PMC2955707 | OPEN | PubMed で書誌・抄録を確認。Crossref の license 欄で CC BY 2.0 を確認 |
| SRC-1890 | Wülker N, Mittag F. The treatment of hallux valgus. Dtsch Arztebl Int. 2012;109(49):857-867 | 10.3238/arztebl.2012.0857 | 23267411 | PMC3528062 | UNKNOWN | PubMed で書誌・抄録を確認。Crossref の license 欄に表示なし |
| SRC-1891 | Morcuende JA, Dolan LA, Dietz FR, et al. Radical reduction in the rate of extensive corrective surgery for clubfoot using the Ponseti method. Pediatrics. 2004;113(2):376-380 | 10.1542/peds.113.2.376 | 14754952 | （なし） | UNKNOWN | PubMed で書誌・抄録を確認 |
| SRC-1892 | Valderrabano V, Horisberger M, Russell I, et al. Etiology of ankle osteoarthritis. Clin Orthop Relat Res. 2009;467(7):1800-1806 | 10.1007/s11999-008-0543-6 | 18830791 | PMC2690733 | UNKNOWN | PubMed で書誌・抄録を確認。Crossref の license 欄に表示なし |
| SRC-1893 | Tepelenis K, Papathanakos G, Kitsouli A, et al. Osteochondromas: An Updated Review of Epidemiology, Pathogenesis, Clinical Presentation, Radiological Features and Treatment Options. In Vivo. 2021;35(2):681-691（PMCID: PMC8045119） | 10.21873/invivo.12308 | 33622860 | © International Institute of Anticancer Research（In Vivo、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認。Crossref の license 欄に CC 表示なし |
| SRC-1894 | Kramer HD, Valentine MJ, Pettinelli N, et al. Ollier Disease: A Case Report and Review of Treatment Options. Cureus. 2023;15(8):e43815（PMCID: PMC10509006） | 10.7759/cureus.43815 | 37731444 | CC BY 4.0 | OPEN | PubMed で書誌・抄録を確認。Europe PMC の license 欄で CC BY を確認 |
| SRC-1895 | Carneiro BC, Da Cruz IAN, Ormond Filho AG, et al. Osteoid osteoma: the great mimicker. Insights Imaging. 2021;12(1):32（PMCID: PMC7940467） | 10.1186/s13244-021-00978-8 | 33683492 | CC BY 4.0 | OPEN | PubMed で書誌・抄録を確認。Europe PMC の license 欄で CC BY を確認 |
| SRC-1896 | Sobti A, Agrawal P, Agarwala S, Agarwal M. Giant Cell Tumor of Bone - An Overview. Arch Bone Jt Surg. 2016;4(1):2-9（PMCID: PMC4733230） | なし | 26894211 | ライセンス未確認（PMC 収載版に CC 表示を確認できず） | UNKNOWN | PubMed で書誌・抄録を確認 |
| SRC-1897 | Chawla S, Blay JY, Rutkowski P, et al. Denosumab in patients with giant-cell tumour of bone: a multicentre, open-label, phase 2 study. Lancet Oncol. 2019;20(12):1719-1729 | 10.1016/S1470-2045(19)30663-1 | 31704134 | © Elsevier（The Lancet Oncology、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認。Crossref の license 欄は TDM 用ライセンスのみ |
| SRC-1898 | Ottaviani G, Jaffe N. The epidemiology of osteosarcoma. Cancer Treat Res. 2009;152:3-13 | 10.1007/978-1-4419-0284-9_1 | 20213383 | © Springer（Cancer Treatment and Research 収載の章、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認 |
| SRC-1899 | Isakoff MS, Bielack SS, Meltzer P, Gorlick R. Osteosarcoma: Current Treatment and a Collaborative Pathway to Success. J Clin Oncol. 2015;33(27):3029-3035（PMCID: PMC4979196） | 10.1200/JCO.2014.59.4895 | 26304877 | © American Society of Clinical Oncology（Journal of Clinical Oncology、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認 |
| SRC-1900 | Gu R, Sun Y. Does serum alkaline phosphatase level really indicate the prognosis in patients with osteosarcoma? A meta-analysis. J Cancer Res Ther. 2018;14(Supplement):S468-S472 | 10.4103/0973-1482.177217 | 29970708 | ライセンス未確認（Journal of Cancer Research and Therapeutics、CC 表示を確認できず） | UNKNOWN | PubMed で書誌・抄録を確認 |
| SRC-1901 | Gelderblom H, Hogendoorn PC, Dijkstra SD, et al. The clinical approach towards chondrosarcoma. Oncologist. 2008;13(3):320-329 | 10.1634/theoncologist.2007-0237 | 18378543 | ライセンス未確認（The Oncologist、Crossref の license 欄は標準出版モデルのみで CC 表示なし） | UNKNOWN | PubMed で書誌・抄録を確認 |
| SRC-1902 | Grünewald TGP, Cidre-Aranaz F, Surdez D, et al. Ewing sarcoma. Nat Rev Dis Primers. 2018;4(1):5 | 10.1038/s41572-018-0003-x | 29977059 | © Springer Nature（Nature Reviews Disease Primers、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認。Crossref の license 欄は TDM 用ライセンスのみ |
| SRC-1903 | Walcott BP, Nahed BV, Mohyeldin A, et al. Chordoma: current concepts, management, and future directions. Lancet Oncol. 2012;13(2):e69-76 | 10.1016/S1470-2045(11)70337-0 | 22300861 | © Elsevier（The Lancet Oncology、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認。Crossref の license 欄は TDM 用ライセンスのみ |
| SRC-1904 | Macedo F, Ladeira K, Pinho F, et al. Bone Metastases: An Overview. Oncol Rev. 2017;11(1):321（PMCID: PMC5444408） | 10.4081/oncol.2017.321 | 28584570 | CC BY-NC 4.0 | RESTRICTED | PubMed で書誌・抄録を確認し、Europe PMC の全文で骨修飾薬・放射線治療・手術の記述を確認。Crossref の license 欄で CC BY-NC 4.0 を確認 |
| SRC-1905 | Pretell-Mazzini J, Murphy RF, Kushare I, Dormans JP. Unicameral bone cysts: general characteristics and management controversies. J Am Acad Orthop Surg. 2014;22(5):295-303 | 10.5435/JAAOS-22-05-295 | 24788445 | © American Academy of Orthopaedic Surgeons（JAAOS、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認 |
| SRC-1906 | Rapp TB, Ward JP, Alaia MJ. Aneurysmal bone cyst. J Am Acad Orthop Surg. 2012;20(4):233-241 | 10.5435/JAAOS-20-04-233 | 22474093 | © American Academy of Orthopaedic Surgeons（JAAOS、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認 |
| SRC-1907 | Javaid MK, Boyce A, Appelman-Dijkstra N, et al. Best practice management guidelines for fibrous dysplasia/McCune-Albright syndrome: a consensus statement from the FD/MAS international consortium. Orphanet J Rare Dis. 2019;14(1):139（PMCID: PMC6567644） | 10.1186/s13023-019-1102-9 | 31196103 | CC BY 4.0 | OPEN | PubMed で書誌・抄録を確認し、Europe PMC の全文ですりガラス状陰影と McCune-Albright 症候群の定義を確認。Crossref の license 欄で CC BY 4.0 を確認 |
| SRC-1908 | Le Nail LR, Crenn V, Rosset P, Ropars M. Management of adipose tumors in the limbs. Orthop Traumatol Surg Res. 2022;108(1S):103162 | 10.1016/j.otsr.2021.103162 | 34863958 | © Elsevier Masson SAS（著作権表示あり・CC 表示なし） | RESTRICTED | PubMed で書誌・抄録（著作権表示を含む）を確認 |
| SRC-1909 | Griffin N, Khan N, Thomas JM, Fisher C, Moskovic EC. The radiological manifestations of intramuscular haemangiomas in adults: magnetic resonance imaging, computed tomography and ultrasound appearances. Skeletal Radiol. 2007;36(11):1051-1059 | 10.1007/s00256-007-0375-6 | 17849114 | © Springer（Skeletal Radiology、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認。Crossref の license 欄は TDM 用ライセンスのみ |
| SRC-1910 | Tang CY, Fung B, Fok M, Zhu J. Schwannoma in the upper limbs. Biomed Res Int. 2013;2013:167196（PMCID: PMC3777180） | 10.1155/2013/167196 | 24093090 | CC BY | OPEN | PubMed で書誌・抄録を確認。Europe PMC の license 欄で CC BY を確認 |
| SRC-1911 | Morey VM, Garg B, Kotwal PP. Glomus tumours of the hand: Review of literature. J Clin Orthop Trauma. 2016;7(4):286-291（PMCID: PMC5106475） | 10.1016/j.jcot.2016.04.006 | 27857505 | ライセンス未確認（Journal of Clinical Orthopaedics and Trauma、CC 表示を確認できず） | UNKNOWN | PubMed で書誌・抄録を確認 |
| SRC-1912 | Desmoid Tumor Working Group. The management of desmoid tumours: A joint global consensus-based guideline approach for adult and paediatric patients. Eur J Cancer. 2020;127:96-107 | 10.1016/j.ejca.2019.11.013 | 32004793 | CC BY-NC-ND 4.0 | RESTRICTED | PubMed で書誌・抄録を確認。Crossref の license 欄で CC BY-NC-ND 4.0 を確認 |
| SRC-1913 | Gounder M, Ratan R, Alcindor T, et al. Nirogacestat, a γ-Secretase Inhibitor for Desmoid Tumors. N Engl J Med. 2023;388(10):898-912 | 10.1056/NEJMoa2210140 | 36884323 | © Massachusetts Medical Society（NEJM、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認 |
| SRC-1914 | Thway K. Well-differentiated liposarcoma and dedifferentiated liposarcoma: An updated review. Semin Diagn Pathol. 2019;36(2):112-121 | 10.1053/j.semdp.2019.02.006 | 30852045 | © Elsevier（Seminars in Diagnostic Pathology、CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認。Crossref の license 欄は TDM 用ライセンスのみ |
| SRC-1915 | Gazendam AM, Popovic S, Munir S, et al. Synovial Sarcoma: A Clinical Review. Curr Oncol. 2021;28(3):1909-1920（PMCID: PMC8161765） | 10.3390/curroncol28030177 | 34069748 | CC BY 4.0 | OPEN | PubMed で書誌・抄録を確認。Europe PMC の license 欄で CC BY を確認 |
| SRC-1916 | Farid M, Demicco EG, Garcia R, et al. Malignant peripheral nerve sheath tumors. Oncologist. 2014;19(2):193-201（PMCID: PMC3926794） | 10.1634/theoncologist.2013-0328 | 24470531 | ライセンス未確認（The Oncologist、CC 表示を確認できず） | UNKNOWN | PubMed で書誌・抄録を確認 |
| SRC-1917 | Haddox CL, Papke DJ Jr, Serrano C. Leiomyosarcoma Therapeutic Approaches and Future Directions. Hematol Oncol Clin North Am. 2025;39(4):785-804 | 10.1016/j.hoc.2025.04.007 | 40410055 | © Elsevier Inc.（著作権表示あり・CC 表示なし） | RESTRICTED | PubMed で書誌・抄録（著作権表示を含む）を確認 |
| SRC-1918 | Mankin HJ, Mankin CJ, Simon MA. The hazards of the biopsy, revisited. Members of the Musculoskeletal Tumor Society. J Bone Joint Surg Am. 1996;78(5):656-663 | 10.2106/00004623-199605000-00004 | 8642021 | © The Journal of Bone and Joint Surgery（CC 表示なし） | RESTRICTED | PubMed で書誌・抄録を確認 |

## 2. 事実票 YAML

```yaml
- id: BD-001
  domain: BD
  subdomain: 骨粗鬆症
  assertion:
    plain_statement_ja: 日本の原発性骨粗鬆症の診断基準（2012年改訂版）では、低骨量を来す他の疾患や続発性骨粗鬆症がないことを前提に、脆弱性骨折がある場合は、椎体骨折または大腿骨近位部骨折であれば骨密度にかかわらず骨粗鬆症と診断し、その他の脆弱性骨折では骨密度が若年成人平均（YAM）の80%未満で診断する。脆弱性骨折がない場合は、骨密度がYAMの70%以下または-2.5SD以下で診断する。骨密度は原則として腰椎または大腿骨近位部のDXAで測定し、複数部位で測定した場合は低い方の値を採用する。
    condition:
      population: 原発性骨粗鬆症の診断対象となる閉経後女性・高齢者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-927
    source: 'Soen S, Fukunaga M, Sugimoto T, Sone T, Fujiwara S, Endo N, Gorai I, Shiraki M, Hagino H, Hosoi T, Ohta H, Yoneda T, Tomomitsu T; Japanese Society for Bone and Mineral Research and Japan Osteoporosis Society Joint Review Committee for the Revision of the Diagnostic Criteria for Primary Osteoporosis. Diagnostic criteria for primary osteoporosis: year 2012 revision. J Bone Miner Metab. 2013;31(3):247-257.'
    doi: 10.1007/s00774-013-0447-8
    pmid: '23553500'
    pmcid: null
    url: https://doi.org/10.1007/s00774-013-0447-8
    source_license: J Bone Miner Metab（Springer、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本票は2012年改訂版の診断基準に基づく。骨粗鬆症の予防と治療ガイドライン2025年版にも診断基準の章があるが、同版での改訂の有無は未確認。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-①（骨粗鬆症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-002
  domain: BD
  subdomain: 骨粗鬆症
  assertion:
    plain_statement_ja: 日本の骨粗鬆症の予防と治療ガイドライン2025年版の原発性骨粗鬆症の薬物治療開始基準では、大腿骨近位部骨折または椎体骨折の脆弱性骨折がある場合は治療を開始し、その他の脆弱性骨折がある場合は骨密度がYAMの80%未満で開始し、脆弱性骨折がない場合は骨密度YAM70%以下で開始し、骨密度がYAMの70%より大きく80%未満の場合は、FRAXによる主要骨粗鬆症性骨折の10年確率が15%以上（75歳未満に適用）または大腿骨近位部骨折の家族歴があるときに開始する。
    condition:
      population: 原発性骨粗鬆症の患者（薬物治療開始の判断対象）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1831
    source: 骨粗鬆症の予防と治療ガイドライン作成委員会（日本骨粗鬆症学会・日本骨代謝学会・骨粗鬆症財団）（編）. 骨粗鬆症の予防と治療ガイドライン2025年版. ライフサイエンス出版; 2025
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 日本骨粗鬆症学会・日本骨代謝学会・骨粗鬆症財団のガイドライン書籍（ライフサイエンス出版、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 開始基準はガイドラインの図4-2から読み取り。FRAXの値はそれ単独では治療開始の判断に用いず、診断基準を補う情報として用いる位置づけであることが本文に明記されている。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-①（骨粗鬆症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-003
  domain: BD
  subdomain: 骨粗鬆症
  assertion:
    plain_statement_ja: 日本の骨粗鬆症の予防と治療ガイドライン2025年版では、大腿骨近位部骨折リスクが高い患者の第一選択薬としてアレンドロネート、リセドロネート、ゾレドロン酸、デノスマブ、ロモソズマブが挙げられ、椎体骨折リスクの高い重症骨粗鬆症例ではテリパラチド、アバロパラチド、ロモソズマブがよい適応とされ、椎体骨折のない閉経後早期の骨吸収亢進例では選択的エストロゲン受容体修飾薬（SERM）も第一選択薬の一つとして検討される。
    condition:
      population: 原発性骨粗鬆症の患者（治療薬選択の対象）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1831
    source: 骨粗鬆症の予防と治療ガイドライン作成委員会（日本骨粗鬆症学会・日本骨代謝学会・骨粗鬆症財団）（編）. 骨粗鬆症の予防と治療ガイドライン2025年版. ライフサイエンス出版; 2025
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 日本骨粗鬆症学会・日本骨代謝学会・骨粗鬆症財団のガイドライン書籍（ライフサイエンス出版、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 挙げた薬剤はいずれも同ガイドライン収載の国内承認薬であることを同ガイドライン（第5章の各薬物の項）で確認した。個別薬剤の推奨度・エビデンスレベルは本票では扱っていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-①（骨粗鬆症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-004
  domain: BD
  subdomain: 骨粗鬆症
  assertion:
    plain_statement_ja: FRAXは、既存骨折、親の大腿骨近位部骨折、喫煙、経口グルココルチコイド使用、関節リウマチなどの臨床的危険因子に、大腿骨頚部骨密度（任意）を組み合わせて、大腿骨近位部骨折と主要骨粗鬆症性骨折の10年確率を算出する骨折リスク評価ツールであり、国ごとの骨折・死亡の疫学で較正される。
    condition:
      population: 閉経後女性および50歳以上の男性（骨折リスク評価の対象）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1832
    source: Kanis JA, et al. FRAX and the assessment of fracture probability in men and women from the UK. Osteoporos Int. 2008;19(4):385-397
    doi: 10.1007/s00198-007-0543-5
    pmid: '18292978'
    pmcid: null
    url: https://doi.org/10.1007/s00198-007-0543-5
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原論文は英国モデルについての報告であり、日本では日本版モデルが用いられる。日本での治療開始の目安（主要骨折10年確率15%）はガイドライン側の基準であり、本票のBD-002に分けた。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-①（骨粗鬆症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-005
  domain: BD
  subdomain: 骨粗鬆症
  assertion:
    plain_statement_ja: 米国のUSPSTFは2025年の勧告で、骨粗鬆症性骨折の予防のためのスクリーニングとして、65歳以上の女性と、臨床的リスク評価で骨折リスクが高いと判定された65歳未満の閉経後女性に対して骨量測定によるスクリーニングを推奨し（いずれもB勧告）、男性については利益と害のバランスを判断するエビデンスが不十分である（Iステートメント）とした。スクリーニングは中軸骨のDXA骨密度測定を、骨折リスク評価と組み合わせて、または組み合わせずに行う。
    condition:
      population: 骨粗鬆症の診断や脆弱性骨折の既往のない40歳以上の成人
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1833
    source: 'US Preventive Services Task Force. Screening for Osteoporosis to Prevent Fractures: US Preventive Services Task Force Recommendation Statement. JAMA. 2025'
    doi: 10.1001/jama.2024.27154
    pmid: '39808425'
    pmcid: null
    url: https://doi.org/10.1001/jama.2024.27154
    source_license: © 2025 American Medical Association and United States Government（All rights reserved）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国の勧告であり、日本の自治体による骨粗鬆症検診とは制度・対象が異なる。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-①（骨粗鬆症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-006
  domain: BD
  subdomain: 骨粗鬆症
  assertion:
    plain_statement_ja: 完全ヒト型抗RANKLモノクローナル抗体デノスマブ60mgの6か月ごとの皮下投与は、骨密度Tスコアが-2.5未満-4.0以上の閉経後骨粗鬆症女性7,868人を対象としたFREEDOM試験で、36か月間の新規椎体骨折のリスクを68%（累積発生率2.3%対7.2%）、大腿骨近位部骨折のリスクを40%（0.7%対1.2%）、非椎体骨折のリスクを20%低下させた。
    condition:
      population: 閉経後骨粗鬆症女性（60〜90歳、腰椎または大腿骨近位部のTスコア-2.5未満-4.0以上）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1834
    source: Cummings SR, et al. Denosumab for prevention of fractures in postmenopausal women with osteoporosis. N Engl J Med. 2009
    doi: 10.1056/NEJMoa0809493
    pmid: '19671655'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa0809493
    source_license: N Engl J Med（Massachusetts Medical Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: デノスマブは国内で骨粗鬆症治療薬として承認され、日本のガイドライン2025年版にも収載されていることを同ガイドラインで確認した。投与中止・延期時の骨折リスク上昇は本試験の範囲外のため本票では扱っていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-①（骨粗鬆症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-007
  domain: BD
  subdomain: 骨粗鬆症
  assertion:
    plain_statement_ja: 副甲状腺ホルモン1型受容体の選択的活性化薬アバロパラチド80μgの連日皮下投与は、骨折リスクの高い閉経後骨粗鬆症女性を対象としたACTIVE試験で、18か月間の新規椎体骨折および非椎体骨折のリスクをプラセボより低下させ、高カルシウム血症の頻度はテリパラチド20μg連日投与より低かった（3.4%対6.4%）。
    condition:
      population: 骨折リスクの高い閉経後骨粗鬆症女性
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1835
    source: 'Miller PD, et al. Effect of abaloparatide vs placebo on new vertebral fractures in postmenopausal women with osteoporosis: a randomized clinical trial. JAMA. 2016'
    doi: 10.1001/jama.2016.11136
    pmid: '27533157'
    pmcid: null
    url: https://doi.org/10.1001/jama.2016.11136
    source_license: JAMA（American Medical Association、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: アバロパラチドとテリパラチドはいずれも日本のガイドライン2025年版に収載された国内承認薬であることを同ガイドラインで確認した。テリパラチドは本試験では非盲検の参照群であり、新規椎体骨折の発生率の具体値は抄録の表に依存するため本票では記載していない。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-①（骨粗鬆症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-008
  domain: BD
  subdomain: 骨粗鬆症
  assertion:
    plain_statement_ja: 抗スクレロスチンモノクローナル抗体ロモソズマブ210mgの月1回皮下投与は、大腿骨近位部のTスコアが-2.5〜-3.5の閉経後骨粗鬆症女性7,180人を対象としたFRAME試験で、12か月時点の新規椎体骨折の発生率をプラセボより73%低下させ（0.5%対1.8%）、その後は両群ともデノスマブ投与へ移行する逐次療法が行われた。
    condition:
      population: 閉経後骨粗鬆症女性（total hipまたは大腿骨頚部のTスコア-2.5〜-3.5）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1836
    source: Cosman F, et al. Romosozumab treatment in postmenopausal women with osteoporosis. N Engl J Med. 2016
    doi: 10.1056/NEJMoa1607948
    pmid: '27641143'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1607948
    source_license: N Engl J Med（Massachusetts Medical Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ロモソズマブは国内で骨粗鬆症治療薬として承認され、日本のガイドライン2025年版にも収載されていることを同ガイドラインで確認した。心血管イベントに関する注意喚起は本試験の抄録の範囲では確認していない。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-①（骨粗鬆症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-009
  domain: BD
  subdomain: 骨粗鬆症
  assertion:
    plain_statement_ja: 日本の全国大腿骨近位部骨折調査に基づく推計では、2017年の大腿骨近位部骨折の新規発生数は約193,400件（95%信頼区間187,300〜199,500件）で、うち男性が約44,100件、女性が約149,300件であり、年齢調整発生率は1992年から2017年までの25年間で有意な変化を示さなかった一方、70〜79歳の発生率は有意に低下した。
    condition:
      population: 日本の高齢者（全国調査の対象となった整形外科医療機関の受診者）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1842
    source: 'Trends in hip fracture incidence in Japan: estimates based on nationwide hip fracture surveys from 1992 to 2017. JBMR Plus. 2021;5(2):e10428'
    doi: 10.1002/jbm4.10428
    pmid: '33615101'
    pmcid: null
    url: https://doi.org/10.1002/jbm4.10428
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 発生数は郵送調査に基づく推計値である。地域差があり、年齢調整発生率には東北と西南で差がみられたと報告されている。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-①（骨粗鬆症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-010
  domain: BD
  subdomain: 骨粗鬆症
  assertion:
    plain_statement_ja: 60歳以上の地域住民を対象としたオーストラリアDubboのコホート研究では、低外力による骨粗鬆症性骨折の後に死亡率が一般人口より上昇し、大腿骨近位部骨折後の標準化死亡比は女性2.43・男性3.51、椎体骨折後は女性1.82・男性2.12であり、死亡率の上昇は骨折後5年間（大腿骨近位部骨折では最長10年）持続し、再骨折によってさらに高まった。
    condition:
      population: 60歳以上の地域住民（オーストラリアDubboの前向きコホート）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1843
    source: Bliuc D, et al. Mortality risk associated with low-trauma osteoporotic fracture and subsequent fracture in men and women. JAMA. 2009
    doi: 10.1001/jama.2009.50
    pmid: '19190316'
    pmcid: null
    url: https://doi.org/10.1001/jama.2009.50
    source_license: JAMA（American Medical Association、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: オーストラリアの単一地域コホートの結果であり、日本人集団での検証ではない。日本における大腿骨近位部骨折1年後の死亡率は約10%と日本のガイドライン2025年版が国内調査を引用して述べている（本票では出典を分けていない）。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-①（骨粗鬆症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-011
  domain: BD
  subdomain: くる病・骨軟化症
  assertion:
    plain_statement_ja: 栄養性くる病と骨軟化症はビタミンD欠乏とカルシウム欠乏によって引き起こされる骨の石灰化障害であり、乳幼児・小児・思春期児の健康、成長、発達に大きな影響を与えるが予防可能な公衆衛生上の問題であって、国際コンセンサス文書がその定義・診断基準と予防・管理の推奨を示している。
    condition:
      population: 乳幼児・小児・思春期児
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-932
    source: Munns CF, Shaw N, Kiely M, Specker BL, Thacher TD, Ozono K, Michigami T, Tiosano D, Mughal MZ, Mäkitie O, et al. Global Consensus Recommendations on Prevention and Management of Nutritional Rickets. J Clin Endocrinol Metab. 2016;101(2):394-415.
    doi: 10.1210/jc.2015-2175
    pmid: '26745253'
    pmcid: null
    url: https://doi.org/10.1210/jc.2015-2175
    source_license: J Clin Endocrinol Metab（The Endocrine Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本コンセンサスは小児の栄養性くる病を中心としており、成人の骨軟化症の検査・治療の詳細は扱っていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-②（くる病、骨軟化症、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-133 (id: Jlvnln4)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-012
  domain: BD
  subdomain: くる病・骨軟化症
  assertion:
    plain_statement_ja: X連鎖性低リン血症症（XLH）は遺伝性リン喪失の最も多い原因であり、その診断は、ビタミンD欠乏やカルシウム欠乏がない状況で、低リン血症と腎性リン喪失を伴うくる病または骨軟化症の所見に基づいて行い、治療開始前に可能な限り遺伝子検査またはFGF23測定で確認することが推奨される。成人では骨軟化症に加えて偽骨折（Looser帯）、付着部症、変形性関節症などを生じる。
    condition:
      population: XLHが疑われる小児および成人
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1844
    source: Haffner D, et al. Clinical practice recommendations for the diagnosis and management of X-linked hypophosphataemia. Nat Rev Nephrol. 2019
    doi: 10.1038/s41581-019-0152-5
    pmid: '31068690'
    pmcid: null
    url: https://doi.org/10.1038/s41581-019-0152-5
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本票はXLHの診断の枠組みであり、腫瘍性骨軟化症など他のFGF23関連疾患の診断手順の詳細は扱っていない。偽骨折は抄録中の pseudofractures の訳語としてLooser帯を併記した。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-②（くる病、骨軟化症、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-133 (id: Jlvnln4)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-013
  domain: BD
  subdomain: くる病・骨軟化症
  assertion:
    plain_statement_ja: X連鎖性低リン血症症（XLH）はFGF23の分泌亢進によって低リン血症と、それに伴うくる病・骨軟化症・骨格変形を来す疾患であり、抗FGF23モノクローナル抗体ブロスマブの皮下投与（2週ごとまたは4週ごと）により、小児XLH患者52人でくる病重症度スコア（Thacherスコア）が改善し、血清リンが上昇して半数超が正常範囲に達し、血清ALPが低下した。
    condition:
      population: X連鎖性低リン血症症の小児
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1838
    source: Carpenter TO, et al. Burosumab therapy in children with X-linked hypophosphatemia. N Engl J Med. 2018
    doi: 10.1056/NEJMoa1714641
    pmid: '29791829'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1714641
    source_license: N Engl J Med（Massachusetts Medical Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ブロスマブは国内で2019年9月にFGF23関連低リン血症性くる病・骨軟化症の効能・効果で承認され薬価収載されていることを、製造販売元の公表資料で確認した。本試験は第2相試験で、投与量は血清リン値が正常下限付近になるよう調整された。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-②（くる病、骨軟化症、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-133 (id: Jlvnln4)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-014
  domain: BD
  subdomain: 骨Paget病
  assertion:
    plain_statement_ja: 骨Paget病の診断と評価では、疑わしい骨格部位の単純X線写真で診断を行い、診断が確定したら骨シンチグラフィで病変の広がりを評価し、血清総ALPを測定して疾患の活動性の評価や治療反応・未治療例の経過観察に用いることが、米国内分泌学会のガイドラインで推奨されている。
    condition:
      population: 骨Paget病が疑われる患者および診断後の患者
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1837
    source: 'Singer FR, et al. Paget''s disease of bone: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2014'
    doi: 10.1210/jc.2014-2910
    pmid: '25406796'
    pmcid: null
    url: https://doi.org/10.1210/jc.2014-2910
    source_license: J Clin Endocrinol Metab（The Endocrine Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 単骨性病変で血清総ALPが正常な例では、骨形成・骨吸収マーカーを測定しても正常なことがあるとガイドラインは述べている。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-③（骨Paget病、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-015
  domain: BD
  subdomain: 骨Paget病
  assertion:
    plain_statement_ja: 米国内分泌学会の骨Paget病ガイドラインでは、活動性の骨Paget病で将来の合併症のリスクがある患者の多くにビスホスホネート治療を推奨し、禁忌がなければゾレドロン酸5mgの単回静脈内投与を第一選択の治療としている。
    condition:
      population: 活動性の骨Paget病患者
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1837
    source: 'Singer FR, et al. Paget''s disease of bone: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab. 2014'
    doi: 10.1210/jc.2014-2910
    pmid: '25406796'
    pmcid: null
    url: https://doi.org/10.1210/jc.2014-2910
    source_license: J Clin Endocrinol Metab（The Endocrine Society、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ゾレドロン酸の骨Paget病に対する国内の承認・保険適用は未確認であり、本票は米国ガイドラインの推奨である。骨の変形、高拍出性心不全、骨肉腫化などの合併症は本疾患の重要な論点だが、今回確認したガイドライン抄録の範囲では合併症の内訳を検証できなかったため、本票の命題には含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-C-③（骨Paget病、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-016
  domain: BD
  subdomain: 骨形成不全症
  assertion:
    plain_statement_ja: 骨形成不全症は骨脆弱性と骨格変形を特徴とする疾患で、その約85%はI型コラーゲンをコードするCOL1A1・COL1A2遺伝子の常染色体優性変異によって生じ、コラーゲンの量または構造の異常が原因となる。診断は家族歴と、出生前・出生時・小児期早期の骨折などの臨床像に基づいて行われ、遺伝子検査で確認できる。
    condition:
      population: 骨形成不全症の患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1840
    source: Marini JC, et al. Osteogenesis imperfecta. Nat Rev Dis Primers. 2017;3:17052
    doi: 10.1038/nrdp.2017.52
    pmid: '28820180'
    pmcid: null
    url: https://doi.org/10.1038/nrdp.2017.52
    source_license: Nat Rev Dis Primers（Springer Nature、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: COL1A1・COL1A2以外の原因遺伝子（I型コラーゲンの合成・修飾・輸送や骨形成細胞の分化・活性を担う遺伝子の異常）も多数報告されており、遺伝学的分類は流動的である。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-B-②（骨形成不全症、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-017
  domain: BD
  subdomain: 骨形成不全症
  assertion:
    plain_statement_ja: 骨形成不全症は日本で指定難病（告示番号274）に指定されており、その診断基準では、症状として骨脆弱性症状（易骨折性や進行性の骨変形）、成長障害、青色強膜、象牙質形成不全、難聴、家族歴、小児期の骨折歴を、検査所見として長管骨の変形を伴う骨折、変形を伴う細い長管骨、頭蓋骨のウォルム骨、椎骨圧迫骨折、骨密度低下を挙げ、COL1A1・COL1A2を含む遺伝学的検査と組み合わせて診断のカテゴリーを判定する。
    condition:
      population: 骨形成不全症が疑われる患者（日本）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1845
    source: 厚生労働省. 指定難病に係る診断基準及び重症度分類等：274 骨形成不全症（難病情報センター掲載）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 厚生労働省の指定難病の診断基準（政府標準利用規約に基づく公的資料として扱う。要最終確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: GOV_JPとしての区分は取り込み側で最終確認されたい。Definiteの判定には症状・検査所見の項目数と鑑別疾患の除外が関わるが、項目数の詳細は基準の表から読み取りのため本票の命題には含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-B-②（骨形成不全症、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-018
  domain: BD
  subdomain: 軟骨無形成症
  assertion:
    plain_statement_ja: 軟骨無形成症は、線維芽細胞増殖因子受容体3（FGFR3）の機能獲得型変異による常染色体優性の疾患で、変異のほぼ全例がFGFR3蛋白のG380R置換であり、著しい低身長を来す骨系統疾患の中で最も頻度が高く、出生頻度は約25,000〜30,000人に1人と推定される。
    condition:
      population: 軟骨無形成症の患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1841
    source: 'Pauli RM. Achondroplasia: a comprehensive clinical review. Orphanet J Rare Dis. 2019;14:1'
    doi: 10.1186/s13023-018-0972-6
    pmid: '30606190'
    pmcid: null
    url: https://doi.org/10.1186/s13023-018-0972-6
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出生頻度は複数の集団ベース・病院ベース研究の推計の幅であり、本文から読み取り。新規変異による発症が約80%を占めると本文は述べている。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-B-①（軟骨無形成症、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-019
  domain: BD
  subdomain: 軟骨無形成症
  assertion:
    plain_statement_ja: 軟骨無形成症の乳児では、頭蓋底が軟骨性骨であるためその成長低下によって大後頭孔が狭小化し、頸髄・延髄圧迫のリスクがある。また水頭症は、大後頭孔の両側にある頸静脈孔の狭小化による静脈還流の部分的閉塞と頭蓋内静脈圧の上昇を介して生じると考えられている。
    condition:
      population: 軟骨無形成症の乳児・小児
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1841
    source: 'Pauli RM. Achondroplasia: a comprehensive clinical review. Orphanet J Rare Dis. 2019;14:1'
    doi: 10.1186/s13023-018-0972-6
    pmid: '30606190'
    pmcid: null
    url: https://doi.org/10.1186/s13023-018-0972-6
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 大後頭孔狭窄の減圧術が必要となる予測因子や水頭症の発症頻度などの数値は、本票では確認していないため記載していない。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-B-①（軟骨無形成症、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BD-020
  domain: BD
  subdomain: 軟骨無形成症
  assertion:
    plain_statement_ja: C型ナトリウム利尿ペプチド（CNP）の類縁体であるボソリチド15μg/kgの連日皮下投与は、軟骨無形成症の小児（5歳から18歳未満）121人を対象とした第3相プラセボ対照試験で、52週時点の年間成長速度をプラセボ群より1.57cm/年（95%信頼区間1.22〜1.93）増加させた。
    condition:
      population: 軟骨無形成症の小児（5歳から18歳未満、歩行可能）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1839
    source: 'Savarirayan R, et al. Once-daily, subcutaneous vosoritide therapy in children with achondroplasia: a randomised, double-blind, phase 3, placebo-controlled, multicentre trial. Lancet. 2020'
    doi: 10.1016/S0140-6736(20)31541-5
    pmid: '32891212'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(20)31541-5
    source_license: Lancet（Elsevier、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ボソリチドは国内で2022年に「骨端線閉鎖を伴わない軟骨無形成症」の効能・効果で承認され、年齢の下限がないことをPMDAの添付文書情報で確認した。本試験の対象は5歳以上であり、最終身長が増加するかは未確立であると論文は述べている。
  curriculum:
    kokushi: 医学各論 Ⅸ-7-B-①（軟骨無形成症、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-001
  domain: OS
  subdomain: 関節リウマチ
  assertion:
    plain_statement_ja: 関節リウマチの2010年ACR/EULAR分類基準は、少なくとも1関節に他の疾患では説明できない滑膜炎があることを前提に、罹患関節の数と部位（0〜5点）、血清学的異常（0〜3点）、急性期反応の上昇（0〜1点）、症状の持続期間（0〜1点）の4ドメインの合計が10点中6点以上で definite RA と分類し、早期例の分類を意図している。
    condition:
      population: 関節リウマチが疑われる患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1846
    source: 'Aletaha D, Neogi T, Silman AJ, et al. 2010 Rheumatoid arthritis classification criteria: an American College of Rheumatology/European League Against Rheumatism collaborative initiative. Arthritis Rheum. 2010;62(9):2569-2581'
    doi: 10.1002/art.27584
    pmid: '20872595'
    pmcid: null
    url: https://doi.org/10.1002/art.27584
    source_license: Wiley（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 分類基準であり診断基準そのものではない。早期診断では分類基準を満たす前から関節炎の持続とびらん性変化のリスクで治療開始を判断する点に留意する。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-H-①（関節リウマチ、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-557 (id: JmxLo0Y)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-002
  domain: OS
  subdomain: 関節リウマチ
  assertion:
    plain_statement_ja: 日本の関節リウマチ診療ガイドライン2024年改訂版では、治療目標と薬物治療アルゴリズムは2020年版から変更されず、メトトレキサート（MTX）を中心とする従来型合成DMARDで治療を開始し、効果が不十分な場合に生物学的製剤またはJAK阻害薬へ進む段階的治療が示されている。
    condition:
      population: 関節リウマチ患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1847
    source: 'Harigai M, Kaneko Y, Tanaka E, et al. 2024 Update of the Japan College of Rheumatology Clinical Practice Guidelines for the Management of Rheumatoid Arthritis: Secondary publication. Mod Rheumatol. 2025;35(3):387-401'
    doi: 10.1093/mr/roaf006
    pmid: '39820350'
    pmcid: null
    url: https://doi.org/10.1093/mr/roaf006
    source_license: 日本リウマチ学会ガイドラインの二次掲載（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: MTX、生物学的製剤（TNF阻害薬・IL-6受容体阻害薬・T細胞選択的共刺激調節薬等）、JAK阻害薬（トファシチニブ、バリシチニブ、ペフィシチニブ、ウパダシチニブ、フィルゴチニブ等）はいずれも関節リウマチの適応で国内承認され保険適用されている。個別製剤の最新の適応・用量は本票では扱っていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-H-①（関節リウマチ、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-557 (id: JmxLo0Y)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-003
  domain: OS
  subdomain: 関節リウマチ
  assertion:
    plain_statement_ja: EULARの2022年改訂推奨では、関節リウマチの治療は臨床的寛解（到達が困難な場合は低疾患活動性）を目標とする treat-to-target で行い、第一選択のDMARDはMTXをアンカーとし、治療開始後3か月で改善がなく6か月で目標に到達しなければ治療を変更し、予後不良因子がある場合は生物学的製剤または標的型合成DMARD（JAK阻害薬等）を追加する。
    condition:
      population: 関節リウマチ患者
      region: 欧州
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1848
    source: 'Smolen JS, Landewé RBM, Bergstra SA, et al. EULAR recommendations for the management of rheumatoid arthritis with synthetic and biological disease-modifying antirheumatic drugs: 2022 update. Ann Rheum Dis. 2023;82(1):3-18'
    doi: 10.1136/ard-2022-223356
    pmid: '36357155'
    pmcid: null
    url: https://doi.org/10.1136/ard-2022-223356
    source_license: BMJ（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 欧州の推奨であり、日本では日本リウマチ学会ガイドライン（OS-002）が優先される。JAK阻害薬を含む各薬剤は関節リウマチの適応で国内承認・保険適用されている。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-H-①（関節リウマチ、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-557 (id: JmxLo0Y)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-004
  domain: OS
  subdomain: 関節リウマチ
  assertion:
    plain_statement_ja: 関節リウマチの関節破壊の進行は、手と足の単純X線写真でびらんと関節裂隙狭小化を半定量的に採点する Sharp スコアの van der Heijde 変法（modified Total Sharp Score）で定量化され、臨床試験や診療における構造的損傷の評価指標となる。
    condition:
      population: 関節リウマチ患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1849
    source: van der Heijde D. How to read radiographs according to the Sharp/van der Heijde method. J Rheumatol. 1999;26(3):743-745
    doi: null
    pmid: '10090194'
    pmcid: null
    url: null
    source_license: The Journal of Rheumatology（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原法論文の抄録では総スコアの最大値を本調査で確認できなかったため、本票では数値を記載していない。出典の DOI は PubMed・Crossref で確認できず null とした。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-H-①（関節リウマチ、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-557 (id: JmxLo0Y)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-005
  domain: OS
  subdomain: 痛風、偽痛風
  assertion:
    plain_statement_ja: 急性痛風関節炎の確定診断は、関節液の偏光顕微鏡検査で針状で負の複屈折を示す尿酸一ナトリウム（MSU）結晶を同定することであり、結晶の証明が痛風と他の関節炎との鑑別の決め手になる。
    condition:
      population: 急性関節炎患者
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-992
    source: FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. Arthritis Care Res (Hoboken). 2020;72(6):744-760.
    doi: 10.1002/acr.24180
    pmid: '32391934'
    pmcid: null
    url: https://doi.org/10.1002/acr.24180
    source_license: 未確認（出典マスターの登録どおり UNKNOWN）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 米国のガイドラインに基づく。関節液結晶の性状は本ガイドラインおよび分類基準で確認した。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-H-②（痛風、偽痛風、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-006
  domain: OS
  subdomain: 痛風、偽痛風
  assertion:
    plain_statement_ja: 急性痛風関節炎の治療の第一選択はNSAIDs、コルヒチン、糖質コルチコイド（経口・関節内・筋注）のいずれかであり、コルヒチンは発症早期に低用量で用いると有効性と忍容性が得られる。
    condition:
      population: 急性痛風関節炎患者
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-992
    source: FitzGerald JD, Dalbeth N, Mikuls T, et al. 2020 American College of Rheumatology Guideline for the Management of Gout. Arthritis Care Res (Hoboken). 2020;72(6):744-760.
    doi: 10.1002/acr.24180
    pmid: '32391934'
    pmcid: null
    url: https://doi.org/10.1002/acr.24180
    source_license: 未確認（出典マスターの登録どおり UNKNOWN）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 米国のガイドラインに基づく。NSAIDs、コルヒチン、副腎皮質ステロイドはいずれも国内承認され保険適用されている。尿酸代謝と降尿酸治療の総論は第21回（MT）を正とし、本票では関節炎としての治療に限った。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-H-②（痛風、偽痛風、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-007
  domain: OS
  subdomain: 痛風、偽痛風
  assertion:
    plain_statement_ja: 偽痛風の原因であるピロリン酸カルシウム（CPP）結晶は、偏光顕微鏡で菱形で正の複屈折を示し、尿酸一ナトリウム結晶（針状・負の複屈折）と区別され、画像では軟骨石灰化を伴い、2023年ACR/EULAR分類基準では関節液中のCPP結晶の証明があればCPPD病に分類できる。
    condition:
      population: CPPD病が疑われる患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1850
    source: Abhishek A, Tedeschi SK, Pascart T, et al. The 2023 ACR/EULAR classification criteria for calcium pyrophosphate deposition disease. Ann Rheum Dis. 2023;82(10):1248-1257
    doi: 10.1136/ard-2023-224575
    pmid: '37495237'
    pmcid: null
    url: https://doi.org/10.1136/ard-2023-224575
    source_license: BMJ（© Author(s) 2023、商業利用不可の表示あり）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 分類基準であり診断基準そのものではない。軟骨石灰化は無症候性にもみられるため、臨床像とあわせて解釈する。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-H-②（痛風、偽痛風、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-008
  domain: OS
  subdomain: 滑液包炎、腱鞘炎
  assertion:
    plain_statement_ja: 肘頭滑液包炎では、発熱、発赤、熱感などの感染徴候の有無が感染性と非感染性の鑑別の手がかりとなり、確定には滑液包穿刺液のグラム染色と培養を用い、感染性では抗菌薬治療と排膿が必要になる。
    condition:
      population: 肘頭滑液包炎患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1851
    source: Reilly D, Kamineni S. Olecranon bursitis. J Shoulder Elbow Surg. 2016;25(1):158-167
    doi: 10.1016/j.jse.2015.08.032
    pmid: '26577126'
    pmcid: null
    url: https://doi.org/10.1016/j.jse.2015.08.032
    source_license: Elsevier（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 感染徴候の頻度の具体的な数値は資料により異なるため、本票では数値を記載していない。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-H-③（滑液包炎、腱鞘炎、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-144 (id: JlvnloQ)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-009
  domain: OS
  subdomain: 滑液包炎、腱鞘炎
  assertion:
    plain_statement_ja: ばね指は手指屈筋腱のA1プーリー部における狭窄性腱鞘炎で、指の引っかかりや弾発現象、進行するとロッキングを呈し、治療ではステロイドの腱鞘内注射が短期の症状改善に有効である。
    condition:
      population: ばね指患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1852
    source: Peters-Veluthamaningal C, van der Windt DA, Winters JC, Meyboom-de Jong B. Corticosteroid injection for trigger finger in adults. Cochrane Database Syst Rev. 2009;(1):CD005617
    doi: 10.1002/14651858.CD005617.pub2
    pmid: '19160256'
    pmcid: null
    url: https://doi.org/10.1002/14651858.CD005617.pub2
    source_license: Cochrane Library／Wiley（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ステロイド腱鞘内注射は国内でも一般的診療として保険適用の範囲で行われているが、個別製剤の適応表記は本票では確認していない。再発例やロッキング例では腱鞘切開術が選択される。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-H-③（滑液包炎、腱鞘炎、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-143 (id: JlvnloI)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-010
  domain: OS
  subdomain: 滑液包炎、腱鞘炎
  assertion:
    plain_statement_ja: de Quervain病は手関節橈側の第一伸筋区画（長母指外転筋・短母指伸筋腱）の狭窄性腱鞘炎で、母指の使用で増悪する橈側手関節痛とFinkelsteinテスト陽性を特徴とし、治療は安静・装具とステロイド腱鞘内注射、難治例では腱鞘切開を行う。
    condition:
      population: de Quervain病患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1853
    source: Ilyas AM, Ast M, Schaffer AA, Thoder J. De quervain tenosynovitis of the wrist. J Am Acad Orthop Surg. 2007;15(12):757-764
    doi: 10.5435/00124635-200712000-00009
    pmid: '18063716'
    pmcid: null
    url: https://doi.org/10.5435/00124635-200712000-00009
    source_license: AAOS（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ステロイド腱鞘内注射は国内でも保険診療の範囲で行われているが、個別製剤の適応表記は本票では確認していない。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-H-③（滑液包炎、腱鞘炎、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-143 (id: JlvnloI)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-011
  domain: OS
  subdomain: 変形性関節症
  assertion:
    plain_statement_ja: 変形性関節症は、原因が明らかでない一次性と、外傷・先行疾患などに続く二次性に分けられ、加齢、肥満、関節外傷、遺伝などが危険因子であり、軟骨の変性・摩耗を中心に骨や滑膜を含めた関節全体の疾患で、画像では関節裂隙の狭小化、骨棘形成、軟骨下骨の硬化が特徴である。
    condition:
      population: 変形性関節症患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1854
    source: Hunter DJ, Bierma-Zeinstra S. Osteoarthritis. Lancet. 2019;393(10182):1745-1759
    doi: 10.1016/S0140-6736(19)30417-9
    pmid: '31034380'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(19)30417-9
    source_license: Elsevier（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 画像所見の重症度と症状の強さは必ずしも一致しない。個別の関節（股関節・膝関節・足関節）の各論は本回の他担当の範囲とした。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-I-①（変形性関節症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-012
  domain: OS
  subdomain: 変形性関節症
  assertion:
    plain_statement_ja: 変形性関節症の非手術管理の中核は患者教育、運動療法、過体重例での減量であり、その上に外用・経口NSAIDsなどの薬物療法や関節内注射を段階的に組み合わせ、保存療法で不十分な末期例で人工関節置換術などの手術を検討する階層構造をとる。
    condition:
      population: 膝・股・多関節の変形性関節症患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1855
    source: Bannuru RR, Osani MC, Vaysbrot EE, et al. OARSI guidelines for the non-surgical management of knee, hip, and polyarticular osteoarthritis. Osteoarthritis Cartilage. 2019;27(11):1578-1589
    doi: 10.1016/j.joca.2019.06.011
    pmid: '31278997'
    pmcid: null
    url: https://doi.org/10.1016/j.joca.2019.06.011
    source_license: Elsevier（テキストマイニング用ライセンスのみ、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 国際的なガイドラインに基づく。NSAIDs（外用・経口）は国内承認され保険適用されている。関節内注射薬の種類と適応の詳細は本票では扱っていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-I-①（変形性関節症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-013
  domain: OS
  subdomain: 神経病性関節症
  assertion:
    plain_statement_ja: 神経病性関節症（Charcot関節）の代表である糖尿病性Charcot足は、末梢神経障害を背景に炎症、外傷、骨代謝の異常が加わって骨と関節の破壊・脱臼・変形が進行する病態で、疼痛を欠くか軽いまま関節破壊が進むことがあり、急性期の治療は免荷が基本である。
    condition:
      population: 糖尿病患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1856
    source: Rogers LC, Frykberg RG, Armstrong DG, et al. The Charcot foot in diabetes. Diabetes Care. 2011;34(9):2123-2129
    doi: 10.2337/dc11-0844
    pmid: '21868781'
    pmcid: null
    url: https://doi.org/10.2337/dc11-0844
    source_license: American Diabetes Association（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 糖尿病以外に脊髄空洞症や脊髄癆などでも Charcot 関節が生じるが、本票の出典は糖尿病性 Charcot 足のコンセンサス文書であり、他疾患での頻度の数値は記載していない。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-I-②（神経病性関節症、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-014
  domain: OS
  subdomain: 血友病性関節症
  assertion:
    plain_statement_ja: 血友病性関節症は、関節内出血の反復により滑膜炎と軟骨・骨の破壊が進行する病態で、同一関節に出血を繰り返す標的関節が問題となり、凝固因子製剤の定期補充による出血予防が関節症の予防に重要である。
    condition:
      population: 血友病患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1857
    source: Srivastava A, Santagostino E, Dougall A, et al. WFH Guidelines for the Management of Hemophilia, 3rd edition. Haemophilia. 2020;26 Suppl 6:1-158
    doi: 10.1111/hae.14046
    pmid: '32744769'
    pmcid: null
    url: https://doi.org/10.1111/hae.14046
    source_license: Wiley（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 凝固因子製剤は血友病の適応で国内承認され保険適用されている。標的関節の操作的定義（一定期間内の出血回数）は団体により異なるため、本票では回数の数値を記載していない。画像変化の詳細な病期分類は本票では扱っていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-I-③（血友病性関節症、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-015
  domain: OS
  subdomain: ガングリオン
  assertion:
    plain_statement_ja: 手関節のガングリオンは背側（舟状月状関節部）に最も多く、約50%は自然に消退し、穿刺吸引は再発が多く、手術摘出は再発率が低い一方で合併症が多いため、無症状例では経過観察も選択肢となる。
    condition:
      population: 手関節ガングリオン患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1858
    source: 'Gude W, Morelli V. Ganglion cysts of the wrist: pathophysiology, clinical picture, and management. Curr Rev Musculoskelet Med. 2008;1(3-4):205-211'
    doi: 10.1007/s12178-008-9033-4
    pmid: '19468907'
    pmcid: null
    url: https://doi.org/10.1007/s12178-008-9033-4
    source_license: CC BY-NC 2.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 自然消退率と再発率は総説の抄録で確認した値であり、部位（背側・掌側）別の再発率の数値は本票では記載していない。専用のコアカリ TBL 項目が提示範囲内になかったため PS のみとした。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-J-①（ガングリオン、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-016
  domain: OS
  subdomain: 異所性骨化
  assertion:
    plain_statement_ja: 異所性骨化は、外傷や手術後（人工股関節全置換術後、寛骨臼骨折後など）のほか、脊髄損傷や頭部外傷などの神経損傷後にも生じ、高リスク例ではNSAIDs（インドメタシンなど）や放射線照射による予防が行われる。
    condition:
      population: 外傷・手術後および神経損傷後の患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1859
    source: Baird EO, Kang QK. Prophylaxis of heterotopic ossification - an updated review. J Orthop Surg Res. 2009;4:12
    doi: 10.1186/1749-799X-4-12
    pmid: '19379483'
    pmcid: null
    url: https://doi.org/10.1186/1749-799X-4-12
    source_license: CC BY 2.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: NSAIDsは国内承認されているが、異所性骨化の予防目的での使用は適応外となる場合があり、保険適用の確認状況は個別製剤では本票で確認していない。予防効果の具体的な数値は研究により異なるため記載していない。専用のコアカリ TBL 項目が提示範囲内になかったため PS のみとした。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-J-②（異所性骨化、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-017
  domain: OS
  subdomain: 腱付着部炎
  assertion:
    plain_statement_ja: 腱付着部炎（enthesitis）は腱や靱帯の骨への付着部の炎症で、脊椎関節炎の中心的病変と位置づけられ、付着部への機械的ストレスと免疫系の関与が病態に関係する。
    condition:
      population: 脊椎関節炎患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1860
    source: 'Schett G, Lories RJ, D''Agostino MA, et al. Enthesitis: from pathophysiology to treatment. Nat Rev Rheumatol. 2017;13(12):731-741'
    doi: 10.1038/nrrheum.2017.188
    pmid: '29158573'
    pmcid: null
    url: https://doi.org/10.1038/nrrheum.2017.188
    source_license: Nature Portfolio（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本票は概念と脊椎関節炎との関係に限り、脊椎関節炎の全身像や個別疾患の総論は作っていない（他分野に残す）。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-J-③（腱付着部炎、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-018
  domain: OS
  subdomain: Kienböck病、特発性膝骨壊死
  assertion:
    plain_statement_ja: Kienböck病は月状骨の無腐性壊死で、病期は単純X線とMRIによる Lichtman 分類で評価され、月状骨の硬化のみの初期から、月状骨の圧潰、手根骨の配列異常、変形性変化へと進行する段階で治療方針が異なる。
    condition:
      population: Kienböck病患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1861
    source: Cross D, Matullo KS. Kienböck disease. Orthop Clin North Am. 2014;45(1):141-152
    doi: 10.1016/j.ocl.2013.09.004
    pmid: '24267215'
    pmcid: null
    url: https://doi.org/10.1016/j.ocl.2013.09.004
    source_license: Elsevier（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: Lichtman 分類の各病期の細目（III期の細分類など）は本票では要約にとどめた。専用のコアカリ TBL 項目が提示範囲内になかったため PS のみとした。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-G-①（Kienböck病、特発性膝骨壊死、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-019
  domain: OS
  subdomain: Kienböck病、特発性膝骨壊死
  assertion:
    plain_statement_ja: 特発性膝骨壊死（自然発症膝骨壊死）は、高齢女性に多く、大腿骨内側顆に好発し、安静時・夜間に増悪する急激な膝痛で発症するのが特徴である。
    condition:
      population: 特発性膝骨壊死患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1862
    source: 'Karim AR, Cherian JJ, Jauregui JJ, et al. Osteonecrosis of the knee: review. Ann Transl Med. 2015;3(1):6'
    doi: 10.3978/j.issn.2305-5839.2014.11.13
    pmid: '25705638'
    pmcid: null
    url: https://doi.org/10.3978/j.issn.2305-5839.2014.11.13
    source_license: AME Publishing（CC表示を本調査では確認できず）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 発症頻度や性比の具体的な数値は資料により異なるため、本票では数値を記載していない。二次性膝骨壊死（ステロイド・アルコール関連）とは区別される。専用のコアカリ TBL 項目が提示範囲内になかったため PS のみとした。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-G-①（Kienböck病、特発性膝骨壊死、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-020
  domain: OS
  subdomain: Dupuytren拘縮
  assertion:
    plain_statement_ja: Dupuytren拘縮は手掌腱膜の結節と索状の肥厚により指の屈曲拘縮が進行する疾患で、高齢男性、糖尿病、北欧系の家系などが危険因子とされ、治療には手術のほか、拘縮索へのコラゲナーゼ（Clostridium histolyticum 由来）注射による非手術的治療がある。
    condition:
      population: Dupuytren拘縮患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1863
    source: Hurst LC, Badalamente MA, Hentz VR, et al. Injectable collagenase clostridium histolyticum for Dupuytren's contracture. N Engl J Med. 2009;361(10):968-979
    doi: 10.1056/NEJMoa0810866
    pmid: '19726771'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa0810866
    source_license: NEJM（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: コラゲナーゼ製剤（ザイアフレックス）は2015年7月に国内承認され同年9月に薬価収載・発売されたことを企業発表で確認したが、その後の販売・供給状況は本調査では確認できなかったため、現在の国内での使用可否は取り込み側で確認されたい。危険因子のうち飲酒・喫煙・抗てんかん薬との関連は資料により評価が異なるため本票では列挙していない。専用のコアカリ TBL 項目が提示範囲内になかったため PS のみとした。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-C-①（Dupuytren拘縮、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-021
  domain: OS
  subdomain: 強剛母指
  assertion:
    plain_statement_ja: 強剛母指（小児の母指ばね指）は、乳幼児にみられる母指IP関節の屈曲位拘縮で、MP関節部掌側に Notta 結節と呼ばれる腱の腫大を触れ、前向き追跡では5年時点で約32%が自然軽快し、初診時のIP関節屈曲が30°を超える例では自然軽快が乏しく手術の適応判断の目安になる。
    condition:
      population: 小児の母指ばね指患者
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1864
    source: Hutchinson DT, Rane AA, Montanez A. The Natural History of Pediatric Trigger Thumb in the United States. J Hand Surg Am. 2021;46(5):424.e1-424.e7
    doi: 10.1016/j.jhsa.2020.10.016
    pmid: '33436280'
    pmcid: null
    url: https://doi.org/10.1016/j.jhsa.2020.10.016
    source_license: Elsevier（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国の単施設前向き研究の値であり、日本の小児での自然経過が同一とは限らない。手術時期の統一した基準はなく、観察を続ける方針も一般的である。専用のコアカリ TBL 項目が提示範囲内になかったため PS のみとした。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-C-②（強剛母指、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-022
  domain: OS
  subdomain: 反復性脱臼
  assertion:
    plain_statement_ja: 肩関節の反復性前方脱臼では、前下方関節唇の剥離である Bankart 病変に加え、関節窩の骨欠損（inverted-pear 型関節窩）や上腕骨頭の engaging Hill-Sachs 病変があると、鏡視下 Bankart 修復のみでは再脱臼のリスクが高い。
    condition:
      population: 肩関節反復性前方脱臼患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1865
    source: 'Burkhart SS, De Beer JF. Traumatic glenohumeral bone defects and their relationship to failure of arthroscopic Bankart repairs: significance of the inverted-pear glenoid and the humeral engaging Hill-Sachs lesion. Arthroscopy. 2000;16(7):677-694'
    doi: 10.1053/jars.2000.17715
    pmid: '11027751'
    pmcid: null
    url: https://doi.org/10.1053/jars.2000.17715
    source_license: Elsevier（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 骨欠損の大きさの具体的な閾値（関節窩幅に対する割合）は研究により扱いが異なるため、本票では数値を記載していない。専用のコアカリ TBL 項目が提示範囲内になかったため PS のみとした。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-A-③（反復性脱臼、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-023
  domain: OS
  subdomain: 胸郭出口症候群
  assertion:
    plain_statement_ja: 胸郭出口症候群は、腕神経叢や鎖骨下動静脈が胸郭出口で圧迫される病態で、神経性が最も多く静脈性・動脈性がこれに続き、診断では誘発テスト（Adson、Wright、Roosテストなど）と頸肋をはじめとする骨性異常の評価を組み合わせる。
    condition:
      population: 胸郭出口症候群患者
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1866
    source: Illig KA, Donahue D, Duncan A, et al. Reporting standards of the Society for Vascular Surgery for thoracic outlet syndrome. J Vasc Surg. 2016;64(3):e23-e35
    doi: 10.1016/j.jvs.2016.04.039
    pmid: '27565607'
    pmcid: null
    url: https://doi.org/10.1016/j.jvs.2016.04.039
    source_license: Society for Vascular Surgery（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 米国の学会報告基準に基づく。各型の割合の具体的な数値は資料により異なるため、本票では数値を記載していない。誘発テスト単独の診断精度は限定的とされる。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-A-④（胸郭出口症候群、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-126 (id: JlvnlpA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-024
  domain: OS
  subdomain: 上腕骨外側上顆炎
  assertion:
    plain_statement_ja: 上腕骨外側上顆炎（テニス肘）は、抵抗下の手関節背屈で外側上顆部に疼痛が誘発されることを特徴とし、治療ではステロイド注射が6週時点では優れるものの再発が多く、52週時点の転帰は理学療法や経過観察より劣ることが無作為化試験で示されている。
    condition:
      population: 上腕骨外側上顆炎患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1867
    source: 'Bisset L, Beller E, Jull G, et al. Mobilisation with movement and exercise, corticosteroid injection, or wait and see for tennis elbow: randomised trial. BMJ. 2006;333(7575):939'
    doi: 10.1136/bmj.38961.584653.AE
    pmid: '17012266'
    pmcid: null
    url: https://doi.org/10.1136/bmj.38961.584653.AE
    source_license: BMJ（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ステロイド関節周辺注射は国内でも保険診療の範囲で行われているが、個別製剤の適応表記は本票では確認していない。専用のコアカリ TBL 項目が提示範囲内になかったため PS のみとした。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-B-②（上腕骨外側上顆炎、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-025
  domain: OS
  subdomain: 肩関節周囲炎
  assertion:
    plain_statement_ja: 凍結肩（癒着性関節包炎）は、疼痛と肩関節可動域の低下（特に外旋制限）を特徴とし、疼痛が前景の時期から回復期へ移行する1〜2年程度の経過をたどるとされる
    condition:
      population: 原発性凍結肩の成人
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1871
    source: 'Ramirez J. Adhesive Capsulitis: Diagnosis and Management. Am Fam Physician. 2019;99(5):297-300'
    doi: null
    pmid: '30811157'
    pmcid: null
    url: null
    source_license: American Family Physician（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 経過を炎症期・凍結期・解凍期の3期に分ける呼称は成書の慣用であり、本抄録は「疼痛期から回復期へ移行する1〜2年の経過」と記述している。無治療でも完全回復するとは限らない点も同抄録で指摘されている
  curriculum:
    kokushi: 医学各論 Ⅸ-8-A-①（肩関節周囲炎、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-152 (id: JlvnlqI)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-026
  domain: OS
  subdomain: 肩関節周囲炎
  assertion:
    plain_statement_ja: 二次医療に紹介された原発性凍結肩の成人では、麻酔下授動術、関節鏡視下関節包切開、ステロイド注射を併用する早期の体系的理学療法の3群間で、12か月後の Oxford Shoulder Score の平均差はいずれも事前に設定した臨床的目標差を下回り、臨床的に優れた治療法はなかった。重篤な有害事象は関節包切開群で8件、授動術群で2件報告された
    condition:
      population: 二次医療に紹介された原発性凍結肩の成人（英国、503例）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1872
    source: 'Rangan A, Brealey SD, Keding A, et al. Management of adults with primary frozen shoulder in secondary care (UK FROST): a multicentre, pragmatic, three-arm, superiority randomised clinical trial. Lancet. 2020;396(10256):977-989'
    doi: 10.1016/S0140-6736(20)31965-6
    pmid: '33010843'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(20)31965-6
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ステロイド注射は各群の治療の一部として用いられたもので、注射製剤の国内承認・保険適用の個別確認は未実施。費用対効果では麻酔下授動術が最も高い確率で優位だった点は本カードに含めていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-A-①（肩関節周囲炎、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-152 (id: JlvnlqI)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-027
  domain: OS
  subdomain: 腱板断裂
  assertion:
    plain_statement_ja: 日本の一般住民を対象とした健診（平均年齢57.9歳、1,366肩）では、全層腱板断裂の有病率は20.7%で加齢とともに増加し、断裂の危険因子は外傷歴、利き腕側、年齢であった。症状のある人の36%に断裂があった一方、無症状の人の16.9%にも断裂が認められた
    condition:
      population: 日本の一般住民
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1873
    source: Yamamoto A, Takagishi K, Osawa T, et al. Prevalence and risk factors of a rotator cuff tear in the general population. J Shoulder Elbow Surg. 2010;19(1):116-120
    doi: 10.1016/j.jse.2009.04.006
    pmid: '19540777'
    pmcid: null
    url: https://doi.org/10.1016/j.jse.2009.04.006
    source_license: Elsevier（テキストマイニング用ライセンスのみ、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 断裂部位は超音波検査による評価で、棘上筋腱の断裂が中心である。有痛弧やドロップアームなどの個別の身体所見の診断精度は本抄録には含まれていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-A-②（腱板断裂、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-028
  domain: OS
  subdomain: 腱板断裂
  assertion:
    plain_statement_ja: 55歳を超える患者の小さい非外傷性棘上筋断裂では、腱板修復術・肩峰形成術・理学療法の併用群と理学療法のみの群の間で、平均6.2年の追跡時点で Constant スコアの改善量に有意差はなかった（20.0点対18.5点）
    condition:
      population: 55歳超の症候性非外傷性棘上筋断裂患者（180肩）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1874
    source: 'Kukkonen J, Ryösä A, Joukainen A, et al. Operative versus conservative treatment of small, nontraumatic supraspinatus tears in patients older than 55 years: over 5-year follow-up of a randomized controlled trial. J Shoulder Elbow Surg. 2021;30(11):2455-2464'
    doi: 10.1016/j.jse.2021.03.133
    pmid: '33774172'
    pmcid: null
    url: https://doi.org/10.1016/j.jse.2021.03.133
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 対象は小さい非外傷性（変性）断裂に限られ、外傷性断裂や大きな断裂の治療方針には当てはまらない。理学療法群の8肩が追跡中に腱板修復術へ移行した
  curriculum:
    kokushi: 医学各論 Ⅸ-8-A-②（腱板断裂、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-029
  domain: OS
  subdomain: 肘内障
  assertion:
    plain_statement_ja: 肘内障は、腕を急に引かれるなどして橈骨頭が輪状靱帯を越えて亜脱臼する病態で、7歳未満の幼児に起こり、患肢の急性の疼痛と機能喪失を呈する
    condition:
      population: 7歳未満の小児
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1875
    source: Krul M, van der Wouden JC, Kruithof EJ, et al. Manipulative interventions for reducing pulled elbow in young children. Cochrane Database Syst Rev. 2017;7(7):CD007759
    doi: 10.1002/14651858.CD007759.pub4
    pmid: '28753234'
    pmcid: null
    url: https://doi.org/10.1002/14651858.CD007759.pub4
    source_license: Wiley（テキストマイニング用ライセンスのみ、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 収載試験の対象は全例7歳未満で、好発年齢の細かな内訳（1〜4歳に集中すること）は本レビューの抄録では数値として示されていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-B-①（肘内障、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-150 (id: JlvnlnM)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-030
  domain: OS
  subdomain: 肘内障
  assertion:
    plain_statement_ja: 肘内障の整復手技では、過回内法（hyperpronation）は回外・屈曲法に比べて初回試行での整復失敗が少なかった（失敗率9.2%対26.4%、リスク比0.35、95%信頼区間0.25〜0.50）
    condition:
      population: 肘内障の小児（8試験、811例）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1875
    source: Krul M, van der Wouden JC, Kruithof EJ, et al. Manipulative interventions for reducing pulled elbow in young children. Cochrane Database Syst Rev. 2017;7(7):CD007759
    doi: 10.1002/14651858.CD007759.pub4
    pmid: '28753234'
    pmcid: null
    url: https://doi.org/10.1002/14651858.CD007759.pub4
    source_license: Wiley（テキストマイニング用ライセンスのみ、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: エビデンスの質は低い（low-quality）と評価されている。整復後の予後（再発率など）は本レビューでは結論が得られていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-B-①（肘内障、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-150 (id: JlvnlnM)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-031
  domain: OS
  subdomain: 変形性股関節症
  assertion:
    plain_statement_ja: 日本の変形性股関節症では寛骨臼形成不全の関与が大きく、全国調査の OA 関節（720関節）では形成不全の各指標が対照関節より有意に重度で、各指標が変形性股関節症のオッズ比を有意に上昇させ、病期の進行とも関連した
    condition:
      population: 日本の変形性股関節症患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1876
    source: 'Jingushi S, Ohfuji S, Sofue M, et al. Osteoarthritis hip joints in Japan: involvement of acetabular dysplasia. J Orthop Sci. 2011;16(2):156-164'
    doi: 10.1007/s00776-011-0025-7
    pmid: '21359510'
    pmcid: null
    url: https://doi.org/10.1007/s00776-011-0025-7
    source_license: CC BY-NC-ND 4.0（Journal of Orthopaedic Science）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 病期は日本整形外科学会の変形性股関節症病期分類（改訂版）で判定されているが、各病期の内訳の数値は抄録に示されていない。形成不全に起因する二次性が多いという割合そのものは本抄録ではパーセンテージで示されていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-D-①（変形性股関節症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-032
  domain: OS
  subdomain: 変形性股関節症
  assertion:
    plain_statement_ja: 人工股関節全置換術は、関節症で障害された患者の治療として良好な長期成績が確立した手術であり、セメント固定・セメントレス固定のいずれでも耐久性のある固定が得られる
    condition:
      population: 末期股関節症の患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1877
    source: 'Learmonth ID, Young C, Rorabeck C. The operation of the century: total hip replacement. Lancet. 2007;370(9597):1508-1519'
    doi: 10.1016/S0140-6736(07)60457-7
    pmid: '17964352'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(07)60457-7
    source_license: © Elsevier（The Lancet、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2007年の総説であり、インプラントの機種別の生存率などの数値は本カードに含めていない。関節温存手術（骨切り術など）の適応については本出典では扱っていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-D-①（変形性股関節症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-033
  domain: OS
  subdomain: 発育性股関節形成不全
  assertion:
    plain_statement_ja: 歩行開始前の発育性股関節形成不全では、Ortolani テスト、Barlow テストと股関節の開排制限が最も重要な身体所見であり、生後6か月未満の診断には股関節超音波検査が適した手段である
    condition:
      population: 歩行開始前の乳児
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1878
    source: Ömeroğlu H, Yüksel S, Demir P, et al. An Eastern Europe and Middle East multinational expert Delphi consensus study on the prevention, diagnosis, and treatment of developmental dysplasia of the hip before walking age. Int Orthop. 2024;48(6):1373-1380
    doi: 10.1007/s00264-023-06077-1
    pmid: '38150007'
    pmcid: null
    url: https://doi.org/10.1007/s00264-023-06077-1
    source_license: Springer（テキストマイニング用ライセンスのみ、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 専門家の Delphi 合意に基づく所見であり、各テストの感度・特異度の数値は示されていない。Allis（Galeazzi）徴候は本抄録の合意事項に含まれていない。Graf 法の型分類の詳細は、IIa の一部と IIb 以上が装具治療の対象となる点のみ本抄録で言及されている
  curriculum:
    kokushi: 医学各論 Ⅸ-8-D-②（発育性股関節形成不全<先天性股関節脱臼>、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-034
  domain: OS
  subdomain: 発育性股関節形成不全
  assertion:
    plain_statement_ja: 発育性股関節形成不全の装具治療では Pavlik ハーネス（リーメンビューゲル）が第一選択の装具であり、Graf 分類 IIb 以上の股関節、および IIa の一部では開排装具による治療が必要とされる
    condition:
      population: 歩行開始前の発育性股関節形成不全の乳児
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1878
    source: Ömeroğlu H, Yüksel S, Demir P, et al. An Eastern Europe and Middle East multinational expert Delphi consensus study on the prevention, diagnosis, and treatment of developmental dysplasia of the hip before walking age. Int Orthop. 2024;48(6):1373-1380
    doi: 10.1007/s00264-023-06077-1
    pmid: '38150007'
    pmcid: null
    url: https://doi.org/10.1007/s00264-023-06077-1
    source_license: Springer（テキストマイニング用ライセンスのみ、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 専門家の Delphi 合意であり、装具治療の成功率の数値は示されていない。装具治療に関するランダム化比較試験のエビデンスは乏しいことが別途システマティックレビューで指摘されている
  curriculum:
    kokushi: 医学各論 Ⅸ-8-D-②（発育性股関節形成不全<先天性股関節脱臼>、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-035
  domain: OS
  subdomain: 大腿骨頭すべり症
  assertion:
    plain_statement_ja: 大腿骨頭すべり症は思春期に起こり、BMI の高い小児で発生が増え、両側性に起こることが多い。診察では Drehmann 徴候を評価し、軽度〜中等度の安定型すべりでは単一スクリューによる in situ 固定が標準治療である
    condition:
      population: 思春期の小児
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1879
    source: 'Funk JF, Lebek S. Epiphyseolysis capitis femoris: new aspects of diagnostics and therapy. Orthopade. 2014;43(8):742-749'
    doi: 10.1007/s00132-013-2226-6
    pmid: '25116242'
    pmcid: null
    url: https://doi.org/10.1007/s00132-013-2226-6
    source_license: Springer（テキストマイニング用ライセンスのみ、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 骨頭が後方へすべるという方向自体は本抄録に明記されていない。両側例の頻度のパーセンテージは示されておらず、対側の予防的固定は「少なくとも中欧では標準的に行う」とされている（地域により方針が異なる）
  curriculum:
    kokushi: 医学各論 Ⅸ-8-D-③（大腿骨頭すべり症、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-036
  domain: OS
  subdomain: 特発性大腿骨頭壊死症
  assertion:
    plain_statement_ja: 日本の特発性大腿骨頭壊死症の全国疫学調査（2005年、臨床情報1,502例）では、年齢分布のピークは40歳代で、関連因子として全身性ステロイド投与歴が51%、習慣性飲酒が31%に認められた
    condition:
      population: 日本の特発性大腿骨頭壊死症患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1880
    source: Fukushima W, Fujioka M, Kubo T, et al. Nationwide epidemiologic survey of idiopathic osteonecrosis of the femoral head. Clin Orthop Relat Res. 2010;468(10):2715-2724
    doi: 10.1007/s11999-010-1292-x
    pmid: '20224959'
    pmcid: null
    url: https://doi.org/10.1007/s11999-010-1292-x
    source_license: Springer（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 2004年の受診患者に基づく調査である。ステロイド関連例の基礎疾患では全身性エリテマトーデスが最も多かった（31%）点は本カードに含めていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-D-④（特発性大腿骨頭壊死症、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-136 (id: JlvnlrA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-037
  domain: OS
  subdomain: 特発性大腿骨頭壊死症
  assertion:
    plain_statement_ja: 特発性大腿骨頭壊死症診療ガイドライン2019（厚生労働省研究班・日本整形外科学会）では、治療法として保存療法、骨移植・細胞療法、骨切り術、人工股関節置換が章立てされ、背景疑問12件と臨床疑問13件に基づいて診療の推奨が示されている
    condition:
      population: 特発性大腿骨頭壊死症患者
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1881
    source: Ando W, Sakai T, Fukushima W, et al. Japanese Orthopaedic Association 2019 Guidelines for osteonecrosis of the femoral head. J Orthop Sci. 2021;26(1):46-68
    doi: 10.1016/j.jos.2020.06.013
    pmid: '33388233'
    pmcid: null
    url: https://doi.org/10.1016/j.jos.2020.06.013
    source_license: CC BY-NC-ND 4.0（Journal of Orthopaedic Science）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 病期分類・タイプ分類の細目や帯状硬化像などの画像所見の定義は、本論文（ガイドライン紹介）の抄録には含まれておらず未確認。個別の臨床疑問に対する推奨の強さも抄録からは確認していない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-D-④（特発性大腿骨頭壊死症、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-136 (id: JlvnlrA)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-038
  domain: OS
  subdomain: Perthes病
  assertion:
    plain_statement_ja: Perthes 病では、発症時年齢と lateral pillar 分類が骨成熟時の転帰と強く相関する予後因子であり、8歳を超えて発症した lateral pillar B 群および B/C 境界群では、手術治療（骨切り術）が非手術治療より転帰が良好だった
    condition:
      population: 6〜12歳発症の Perthes 病患者（多施設前向き研究、438例）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1882
    source: 'Herring JA, Kim HT, Browne R. Legg-Calve-Perthes disease. Part II: Prospective multicenter study of the effect of treatment on outcome. J Bone Joint Surg Am. 2004;86(10):2121-2134'
    doi: null
    pmid: '15466720'
    pmcid: null
    url: null
    source_license: Journal of Bone and Joint Surgery（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: containment の考え方自体は本研究の治療群（装具・骨切り術など）に反映されているが、装具単独の効果は無治療群と差がなかった。lateral pillar C 群では手術・非手術とも転帰は最も不良だった
  curriculum:
    kokushi: 医学各論 Ⅸ-8-D-⑤（Perthes病、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-039
  domain: OS
  subdomain: 変形性膝関節症
  assertion:
    plain_statement_ja: ROAD スタディ（日本人一般住民3,040人）では、X線学的変形性膝関節症（Kellgren-Lawrence 分類グレード2以上）の有病率は加齢とともに上昇して80歳以上で男性51.6%・女性80.7%に達し、国内の患者数は約2,500万人と推定された
    condition:
      population: 日本の一般住民（40歳以上中心）
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1883
    source: 'Yoshimura N, Muraki S, Oka H, et al. Prevalence of knee osteoarthritis, lumbar spondylosis, and osteoporosis in Japanese men and women: the research on osteoarthritis/osteoporosis against disability study. J Bone Miner Metab. 2009;27(5):620-628'
    doi: 10.1007/s00774-009-0080-8
    pmid: '19568689'
    pmcid: null
    url: https://doi.org/10.1007/s00774-009-0080-8
    source_license: Springer（テキストマイニング用ライセンスのみ、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 2005年開始のコホートのベースライン調査に基づく数値。肥満などの個別の危険因子の寄与は本抄録では定量されていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-E-①（変形性膝関節症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-040
  domain: OS
  subdomain: 変形性膝関節症
  assertion:
    plain_statement_ja: OARSI ガイドライン2019では、変形性膝関節症のコア治療は関節炎に関する教育と体系的な陸上での運動プログラム（食事による体重管理の併用を含む）とされ、外用 NSAIDs が強く推奨される（Level 1A）
    condition:
      population: 変形性膝関節症患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1855
    source: Bannuru RR, Osani MC, Vaysbrot EE, et al. OARSI guidelines for the non-surgical management of knee, hip, and polyarticular osteoarthritis. Osteoarthritis Cartilage. 2019;27(11):1578-1589
    doi: 10.1016/j.joca.2019.06.011
    pmid: '31278997'
    pmcid: null
    url: https://doi.org/10.1016/j.joca.2019.06.011
    source_license: Elsevier（テキストマイニング用ライセンスのみ、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードに挙げた薬剤（NSAIDs）の国内承認・保険適用の個別確認は未実施。推奨は国際ガイドラインのものであり、国内の診療ガイドラインの推奨とは異なる場合がある
  curriculum:
    kokushi: 医学各論 Ⅸ-8-E-①（変形性膝関節症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-041
  domain: OS
  subdomain: 変形性膝関節症
  assertion:
    plain_statement_ja: 変形性膝関節症に対する関節内ヒアルロン酸注射（粘性補充）は、大規模プラセボ対照試験に限ったメタ解析では、プラセボに比べて疼痛をわずかに軽減したが、その効果量（標準化平均差 −0.08）は事前に定めた臨床的に意味のある最小差（−0.37）を下回った
    condition:
      population: 変形性膝関節症患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1885
    source: 'Pereira TV, Jüni P, Saadat P, et al. Viscosupplementation for knee osteoarthritis: systematic review and meta-analysis. BMJ. 2022;378:e069722'
    doi: 10.1136/bmj-2022-069722
    pmid: '36333100'
    pmcid: null
    url: https://doi.org/10.1136/bmj-2022-069722
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 関節内ヒアルロン酸製剤の国内承認・保険適用の確認は未実施であり、国内での位置づけは本カードの対象外。重篤な有害事象の相対リスクの増加が同解析で報告されている点は、数値の詳細を確認していないため本カードに含めていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-E-①（変形性膝関節症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-042
  domain: OS
  subdomain: 変形性膝関節症
  assertion:
    plain_statement_ja: 片側の人工膝関節全置換術の適応となる中等症〜重症の変形性膝関節症患者では、人工膝関節全置換術に非手術治療を併用した群は、非手術治療のみの群に比べて12か月後の疼痛・機能（KOOS4）の改善が大きかった（調整平均差15.8点）が、重篤な有害事象は多かった（24件対6件）
    condition:
      population: 中等症〜重症の変形性膝関節症患者（100例）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1886
    source: Skou ST, Roos EM, Laursen MB, et al. A Randomized, Controlled Trial of Total Knee Replacement. N Engl J Med. 2015;373(17):1597-1606
    doi: 10.1056/NEJMoa1505467
    pmid: '26488691'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1505467
    source_license: NEJM（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 非手術治療群の26%が12か月以内に人工膝関節全置換術を受けており、結果の解釈にはこの移行を考慮する必要がある
  curriculum:
    kokushi: 医学各論 Ⅸ-8-E-①（変形性膝関節症、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-043
  domain: OS
  subdomain: Osgood-Schlatter病
  assertion:
    plain_statement_ja: Osgood-Schlatter 病は、骨端線の開存する活動的な小児・思春期にみられる脛骨粗面の牽引性骨端症で、多くは自然軽快し、保存治療が90%を超える患者で成功する
    condition:
      population: 成長期のスポーツを行う小児・思春期
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1887
    source: 'Ladenhauf HN, Seitlinger G, Green DW. Osgood-Schlatter disease: a 2020 update of a common knee condition in children. Curr Opin Pediatr. 2020;32(1):107-112'
    doi: 10.1097/MOP.0000000000000842
    pmid: '31714260'
    pmcid: null
    url: https://doi.org/10.1097/MOP.0000000000000842
    source_license: Wolters Kluwer（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 男児で12〜15歳にピークがあるとされてきたが、近年の女子のスポーツ参加の増加により性差はなくなってきていると同総説は述べている
  curriculum:
    kokushi: 医学各論 Ⅸ-8-E-②（Osgood-Schlatter病、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-044
  domain: OS
  subdomain: 半月板障害
  assertion:
    plain_statement_ja: 変形性膝関節症がなく変性内側半月板断裂の症状を有する35〜65歳の患者では、関節鏡視下半月板部分切除術はシャム手術と比べて、12か月後の症状・機能スコアおよび運動後疼痛の改善に有意差がなかった
    condition:
      population: 変性内側半月板断裂の症状を有する35〜65歳の患者（146例）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1888
    source: Sihvonen R, Paavola M, Malmivaara A, et al. Arthroscopic partial meniscectomy versus sham surgery for a degenerative meniscal tear. N Engl J Med. 2013;369(26):2515-2524
    doi: 10.1056/NEJMoa1305189
    pmid: '24369076'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa1305189
    source_license: NEJM（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 対象は変性断裂で変形性膝関節症のない患者に限られ、若年者の外傷性断裂やロッキングを呈する断裂には当てはまらない。MRI による断裂の診断精度は本試験の対象外である
  curriculum:
    kokushi: 医学各論 Ⅸ-8-E-③（半月板障害、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-045
  domain: OS
  subdomain: 外反母趾
  assertion:
    plain_statement_ja: 外反母趾の有病率は、一般住民を対象とした研究のメタ解析で、18〜65歳の成人で23%、65歳を超える高齢者で35.7%と推定され、女性（30%）は男性（13%）より高かった
    condition:
      population: 一般住民（成人）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1889
    source: 'Nix S, Smith M, Vicenzino B. Prevalence of hallux valgus in the general population: a systematic review and meta-analysis. J Foot Ankle Res. 2010;3:21'
    doi: 10.1186/1757-1146-3-21
    pmid: '20868524'
    pmcid: null
    url: https://doi.org/10.1186/1757-1146-3-21
    source_license: CC BY 2.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 収載研究間で外反母趾の診断方法が異なり、有病率の推定にはばらつきがある。HV 角による変形の程度の定義や、靴・遺伝などの危険因子の定量は本抄録には含まれていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-F-①（外反母趾、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-147 (id: Jlvnlok)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-046
  domain: OS
  subdomain: 外反母趾
  assertion:
    plain_statement_ja: 外反母趾の非手術治療は症状を緩和しうるが母趾の変形自体を矯正することはできず、疼痛が持続する場合に手術が適応となる。軽度の変形には Chevron 骨切り術などの第1中足骨遠位骨切り術が適し、重度の変形には第1中足趾節関節の軟部組織処置と近位骨切り術を要する
    condition:
      population: 外反母趾患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1890
    source: Wülker N, Mittag F. The treatment of hallux valgus. Dtsch Arztebl Int. 2012;109(49):857-867
    doi: 10.3238/arztebl.2012.0857
    pmid: '23267411'
    pmcid: null
    url: https://doi.org/10.3238/arztebl.2012.0857
    source_license: Deutsches Ärzteblatt International（Crossref にライセンス表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 2012年の総説であり、装具治療の個別の効果量は示されていない。手術成績は適切な術式選択で85%が良好とされている
  curriculum:
    kokushi: 医学各論 Ⅸ-8-F-①（外反母趾、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-147 (id: Jlvnlok)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-047
  domain: OS
  subdomain: 内反足
  assertion:
    plain_statement_ja: 先天性内反足に対する Ponseti 法（逐次的な徒手矯正とギプス固定）では、157例中98%で変形の矯正が得られ、広範囲な矯正手術を要したのは2.5%にとどまった。再発は足部外転装具の非遵守と関連した
    condition:
      population: 先天性特発性内反足の小児（157例、256足）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1891
    source: Morcuende JA, Dolan LA, Dietz FR, et al. Radical reduction in the rate of extensive corrective surgery for clubfoot using the Ponseti method. Pediatrics. 2004;113(2):376-380
    doi: 10.1542/peds.113.2.376
    pmid: '14754952'
    pmcid: null
    url: https://doi.org/10.1542/peds.113.2.376
    source_license: American Academy of Pediatrics（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 単施設の連続症例の検討であり、90%の患者で5回以下のギプスで矯正が得られている。アキレス腱皮下切腱の併用率などの手技の細部は本カードに含めていない
  curriculum:
    kokushi: 医学各論 Ⅸ-8-F-②（内反足、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-135 (id: Jlvnlqw)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-048
  domain: OS
  subdomain: 変形性足関節症
  assertion:
    plain_statement_ja: 末期の変形性足関節症の病因は外傷後が78%を占めて最も多く、二次性が13%、一次性は9%にとどまり、股関節・膝関節の変形性関節症と異なって外傷後のものが大半を占める
    condition:
      population: 末期変形性足関節症患者（390例、406関節）
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1892
    source: Valderrabano V, Horisberger M, Russell I, et al. Etiology of ankle osteoarthritis. Clin Orthop Relat Res. 2009;467(7):1800-1806
    doi: 10.1007/s11999-008-0543-6
    pmid: '18830791'
    pmcid: null
    url: https://doi.org/10.1007/s11999-008-0543-6
    source_license: Springer（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 単施設を受診した末期症例の内訳であり、一般住民における病因の分布とは異なる可能性がある。治療（人工足関節置換・関節固定の比較など）は本出典の対象外である
  curriculum:
    kokushi: 医学各論 Ⅸ-8-F-③（変形性足関節症、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-049
  domain: OS
  subdomain: 膝蓋軟骨軟化症
  assertion:
    plain_statement_ja: 膝蓋軟骨軟化症は若年者に多くみられる膝前面痛の原因であり、膝蓋大腿関節の関節軟骨の軟化・膨化・浮腫を初期病変とする。初期変化は可逆性の場合もあるが、進行すると膝蓋大腿関節の変形性関節症へ移行しうる。
    condition:
      population: 若年者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1869
    source: 'Zheng W, Li H, Hu K, Li L, Bei M. Chondromalacia patellae: current options and emerging cell therapies. Stem Cell Res Ther. 2021;12(1):412'
    doi: 10.1186/s13287-021-02478-4
    pmid: '34275494'
    pmcid: null
    url: https://doi.org/10.1186/s13287-021-02478-4
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本出典は膝蓋軟骨軟化症そのものを対象とする総説だが、治療面の重点は細胞療法などの新規治療にあり、標準的な保存療法と手術の位置づけは膝蓋大腿痛の診療ガイドラインに基づく OS-202 で扱った。若年女性に多い点は OS-202 の根拠ガイドライン本文の疫学記述による。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-E-④（膝蓋軟骨軟化症、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: OS-050
  domain: OS
  subdomain: 膝蓋軟骨軟化症
  assertion:
    plain_statement_ja: 膝蓋大腿痛は思春期から若年成人に多く、女性で発生率が高い。膝蓋軟骨軟化症を含む膝蓋大腿痛では、膝蓋骨の周囲・後面の痛みが、階段の昇降、しゃがみ込み、長時間の坐位（movie sign）など、膝を屈曲した状態で膝蓋大腿関節に負荷がかかる活動で増悪する。治療は保存療法が主体であり、その中核は大腿四頭筋を含む膝関節周囲筋と股関節周囲筋を対象とする運動療法で、診療ガイドラインは股関節・膝関節の複合運動療法による疼痛軽減と機能改善を推奨している。外科的治療は、保存療法で改善しない場合に検討される例外的選択肢である。
    condition:
      population: 膝蓋大腿痛（膝蓋軟骨軟化症を含む）の患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1868
    source: Willy RW, Hoglund LT, Barton CJ, et al. Patellofemoral Pain. J Orthop Sports Phys Ther. 2019;49(9):CPG1-CPG95
    doi: 10.2519/jospt.2019.0302
    pmid: '31475628'
    pmcid: null
    url: https://doi.org/10.2519/jospt.2019.0302
    source_license: JOSPT（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードの根拠は膝蓋大腿痛（patellofemoral pain）の診療ガイドラインであり、膝蓋軟骨軟化症は同ガイドラインの対象範囲に含まれる（ICD-10 の M22.40 として収載）膝蓋大腿痛の原因・関連病変の一つとして扱った。女性で発生率が高い点はガイドライン本文の発生率データ（米海軍士官候補生で女性33/1000人年、男性15/1000人年）に基づき、集団により値は異なる。ガイドライン本文では長時間坐位は prolonged sitting と表記され、movie sign の語自体は用いられていない。同ガイドラインは保存的管理（理学療法）の指針であり外科的治療の適応自体は扱っていないため、「手術は例外的」は、推奨される標準管理が保存療法で構成されることによる位置づけであり、難治例での手術適応は個別に判断される。
  curriculum:
    kokushi: 医学各論 Ⅸ-8-E-④（膝蓋軟骨軟化症、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-001
  domain: BO
  subdomain: 骨軟骨腫
  assertion:
    plain_statement_ja: 骨軟骨腫は最も多い良性骨腫瘍であり、85%が単発性で、15%が常染色体優性遺伝の多発性外骨腫症に伴う。成人で軟骨帽の厚さが2cmを超える場合や、骨成長板閉鎖後の疼痛出現・増大は悪性転化を示唆する所見である。
    condition:
      population: 骨軟骨腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1893
    source: 'Tepelenis K, Papathanakos G, Kitsouli A, et al. Osteochondromas: An Updated Review of Epidemiology, Pathogenesis, Clinical Presentation, Radiological Features and Treatment Options. In Vivo. 2021;35(2):681-691（PMCID: PMC8045119）'
    doi: 10.21873/invivo.12308
    pmid: '33622860'
    pmcid: null
    url: https://doi.org/10.21873/invivo.12308
    source_license: © International Institute of Anticancer Research（In Vivo、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 好発部位（長管骨の骨幹端）や有茎性・広基性の形態は抄録の記述に基づく一般像であり、本カードの数値（85%/15%、軟骨帽2cm）はこの総説の記載による。国内の診療指針での扱いは別途確認を要する。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-A-①（骨軟骨腫、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-002
  domain: BO
  subdomain: 内軟骨腫
  assertion:
    plain_statement_ja: 内軟骨腫は四肢長管骨に生じる良性軟骨腫瘍で、病的骨折で発症することが多い。多発性に生じる場合は Ollier 病と呼ばれ、軟骨肉腫への悪性転化を早期に捉えるため定期的な画像経過観察を要する。
    condition:
      population: 内軟骨腫・Ollier 病患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1894
    source: 'Kramer HD, Valentine MJ, Pettinelli N, et al. Ollier Disease: A Case Report and Review of Treatment Options. Cureus. 2023;15(8):e43815（PMCID: PMC10509006）'
    doi: 10.7759/cureus.43815
    pmid: '37731444'
    pmcid: null
    url: https://doi.org/10.7759/cureus.43815
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 出典は Ollier 病の症例報告と治療選択肢の総説であり、単発性内軟骨腫に限った疫学・自然史の数値は確認していない。単発例と多発例で悪性転化のリスクは異なる点に注意。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-A-②（内軟骨腫、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-003
  domain: BO
  subdomain: 類骨骨腫
  assertion:
    plain_statement_ja: 類骨骨腫は若年に多い良性骨腫瘍で、夜間に増悪し非ステロイド性抗炎症薬で軽快する疼痛を特徴とし、画像では骨硬化・皮質肥厚・周囲の骨髄浮腫を伴う透亮像（nidus）が診断の鍵となる。
    condition:
      population: 類骨骨腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1895
    source: 'Carneiro BC, Da Cruz IAN, Ormond Filho AG, et al. Osteoid osteoma: the great mimicker. Insights Imaging. 2021;12(1):32（PMCID: PMC7940467）'
    doi: 10.1186/s13244-021-00978-8
    pmid: '33683492'
    pmcid: null
    url: https://doi.org/10.1186/s13244-021-00978-8
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 男女比などの疫学数値は抄録で確認できなかったため命題に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-A-③（類骨骨腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-004
  domain: BO
  subdomain: 骨巨細胞腫
  assertion:
    plain_statement_ja: 骨巨細胞腫は組織学的には良性だが局所侵襲性を示し転移する能力を持つ腫瘍で、若年成人の長管骨の関節近傍（骨端部）に好発し、一部の患者では肺転移を生じる。
    condition:
      population: 骨巨細胞腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1896
    source: 'Sobti A, Agrawal P, Agarwala S, Agarwal M. Giant Cell Tumor of Bone - An Overview. Arch Bone Jt Surg. 2016;4(1):2-9（PMCID: PMC4733230）'
    doi: null
    pmid: '26894211'
    pmcid: null
    url: null
    source_license: ライセンス未確認（PMC 収載版に CC 表示を確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 「骨端部」は出典抄録の「関節近傍（peri-articular / near a joint）」の解剖学的表現として併記した。肺転移の頻度の数値は出典抄録に明示がなく命題に含めていない。本出典には DOI が付与されていない（出典表参照）。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-A-④（骨巨細胞腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-005
  domain: BO
  subdomain: 骨巨細胞腫
  assertion:
    plain_statement_ja: 抗 RANKL 抗体デノスマブは骨巨細胞腫に有効であり、切除不能例で長期の病勢制御が得られ、手術により重篤な機能障害が見込まれる切除可能例では、投与開始後6か月の時点で92%の患者が手術を受けずに済んだ。
    condition:
      population: 切除不能または手術で重篤な障害が見込まれる骨巨細胞腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1897
    source: 'Chawla S, Blay JY, Rutkowski P, et al. Denosumab in patients with giant-cell tumour of bone: a multicentre, open-label, phase 2 study. Lancet Oncol. 2019;20(12):1719-1729'
    doi: 10.1016/S1470-2045(19)30663-1
    pmid: '31704134'
    pmcid: null
    url: https://doi.org/10.1016/S1470-2045(19)30663-1
    source_license: © Elsevier（The Lancet Oncology、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: デノスマブ（ランマーク皮下注120mg）は国内で2014年5月に「骨巨細胞腫」の効能追加が承認され保険適用があることを、製造販売業者（第一三共）の公表資料と PMDA の審査資料で確認した。投与中止後の再燃や術前投与時の掻爬後の再発については本試験の抄録範囲を超えるため命題に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-A-④（骨巨細胞腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-006
  domain: BO
  subdomain: 骨肉腫
  assertion:
    plain_statement_ja: 骨肉腫は小児・若年に最も多い原発性悪性骨腫瘍で、思春期の成長スパート期（10〜14歳）に発症のピークがあり、長管骨の骨幹端に好発する。部位は大腿骨（42%、うち75%が遠位）、脛骨（19%、うち80%が近位）の順に多い。
    condition:
      population: 骨肉腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1898
    source: Ottaviani G, Jaffe N. The epidemiology of osteosarcoma. Cancer Treat Res. 2009;152:3-13
    doi: 10.1007/978-1-4419-0284-9_1
    pmid: '20213383'
    pmcid: null
    url: https://doi.org/10.1007/978-1-4419-0284-9_1
    source_license: © Springer（Cancer Treatment and Research 収載の章、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頻度の数値は米国の登録データに基づく本章の記載であり、国内の発生頻度とは異なる可能性がある。高齢者の第二のピーク（Paget 病に続発するものなど）は命題に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-B-①（骨肉腫、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-638 (id: Jlvnmbo)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-007
  domain: BO
  subdomain: 骨肉腫
  assertion:
    plain_statement_ja: 高悪性度骨肉腫の化学療法では、高用量メトトレキサート・ドキソルビシン・シスプラチンの3剤併用（MAP療法）が最も有効なレジメンの一つとして確立しており、多剤併用化学療法の導入により限局性骨肉腫の長期生存率は20%未満から65〜70%へ改善した。治療には腫瘍の完全切除を伴う手術が組み合わされる。
    condition:
      population: 限局性高悪性度骨肉腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1899
    source: 'Isakoff MS, Bielack SS, Meltzer P, Gorlick R. Osteosarcoma: Current Treatment and a Collaborative Pathway to Success. J Clin Oncol. 2015;33(27):3029-3035（PMCID: PMC4979196）'
    doi: 10.1200/JCO.2014.59.4895
    pmid: '26304877'
    pmcid: null
    url: https://doi.org/10.1200/JCO.2014.59.4895
    source_license: © American Society of Clinical Oncology（Journal of Clinical Oncology、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤名のあるカードとしての注記：MAP 療法を構成する3薬剤はいずれも国内承認薬であるが、骨肉腫に対する適応・保険適用の文言は本作成では添付文書で個別に確認していない。患肢温存術の適応判断や切除縁の詳細は本出典の抄録範囲を超えるため命題に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-B-①（骨肉腫、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-638 (id: Jlvnmbo)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-008
  domain: BO
  subdomain: 骨肉腫
  assertion:
    plain_statement_ja: 骨肉腫では、血清アルカリホスファターゼ（ALP）高値は全生存率の低下と関連する予後不良因子である（メタ解析における高 ALP 群の死亡ハザード比 1.60、95%信頼区間 1.38〜1.86）。
    condition:
      population: 骨肉腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1900
    source: Gu R, Sun Y. Does serum alkaline phosphatase level really indicate the prognosis in patients with osteosarcoma? A meta-analysis. J Cancer Res Ther. 2018;14(Supplement):S468-S472
    doi: 10.4103/0973-1482.177217
    pmid: '29970708'
    pmcid: null
    url: https://doi.org/10.4103/0973-1482.177217
    source_license: ライセンス未確認（Journal of Cancer Research and Therapeutics、CC 表示を確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: ALP のカットオフ値は各原著研究で異なり統一されていない。治療反応性や腫瘍量の指標としての位置づけは本メタ解析の範囲を超える。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-B-①（骨肉腫、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-638 (id: Jlvnmbo)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-009
  domain: BO
  subdomain: 軟骨肉腫
  assertion:
    plain_statement_ja: 従来型軟骨肉腫は化学療法・放射線療法に抵抗性であり、治療の主体は外科的切除で、中悪性度・高悪性度のものでは広範な一塊切除が望ましい治療である。
    condition:
      population: 軟骨肉腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1901
    source: Gelderblom H, Hogendoorn PC, Dijkstra SD, et al. The clinical approach towards chondrosarcoma. Oncologist. 2008;13(3):320-329
    doi: 10.1634/theoncologist.2007-0237
    pmid: '18378543'
    pmcid: null
    url: https://doi.org/10.1634/theoncologist.2007-0237
    source_license: ライセンス未確認（The Oncologist、Crossref の license 欄は標準出版モデルのみで CC 表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典は2008年の総説であり、その後の分子標的治療（IDH 変異など）の進展は反映されていない。中高年好発という年齢分布は本出典の抄録では明示されておらず命題に含めていない。 化学療法の個別薬剤の国内承認・保険適用は、本カードの命題（化学療法抵抗性）には直接関係しないため未確認。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-B-②（軟骨肉腫、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-639 (id: Jlvnmbs)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-010
  domain: BO
  subdomain: Ewing肉腫
  assertion:
    plain_statement_ja: Ewing肉腫は小児・思春期で2番目に多い骨腫瘍で、EWSR1-FLI1 融合遺伝子（85%）を特徴とし、治療は手術・放射線治療・多剤併用化学療法を組み合わせた集学的治療が標準で、限局例の生存率は70〜80%である。
    condition:
      population: Ewing肉腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1902
    source: Grünewald TGP, Cidre-Aranaz F, Surdez D, et al. Ewing sarcoma. Nat Rev Dis Primers. 2018;4(1):5
    doi: 10.1038/s41572-018-0003-x
    pmid: '29977059'
    pmcid: null
    url: https://doi.org/10.1038/s41572-018-0003-x
    source_license: © Springer Nature（Nature Reviews Disease Primers、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: onion-peel 状骨膜反応は古典的な画像所見として知られるが、本出典の抄録では明示されなかったため命題に含めていない。使用薬剤（ビンクリスチン、ドキソルビシン、シクロホスファミド、イホスファミド、エトポシドなど）の国内承認はいずれも抗悪性腫瘍薬として承認済みの薬剤だが、Ewing肉腫への適応文言は個別に確認していない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-B-③（Ewing肉腫、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-640 (id: Jlvnmb0)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-011
  domain: BO
  subdomain: 脊索腫
  assertion:
    plain_statement_ja: 脊索腫は脊索の遺残組織から発生すると考えられる悪性骨腫瘍で、仙骨・頭蓋底（斜台）・脊椎の体軸正中部に好発し、可動脊椎・仙骨病変では広い切除縁での一塊切除と術後放射線治療が標準治療である。
    condition:
      population: 脊索腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1903
    source: 'Walcott BP, Nahed BV, Mohyeldin A, et al. Chordoma: current concepts, management, and future directions. Lancet Oncol. 2012;13(2):e69-76'
    doi: 10.1016/S1470-2045(11)70337-0
    pmid: '22300861'
    pmcid: null
    url: https://doi.org/10.1016/S1470-2045(11)70337-0
    source_license: © Elsevier（The Lancet Oncology、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: brachyury の発現や TBXT 遺伝子については本出典の抄録で数値・頻度を確認できなかったため命題に含めていない。粒子線治療の国内実施体制は本カードの範囲外。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-B-④（脊索腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-012
  domain: BO
  subdomain: 転移性骨腫瘍
  assertion:
    plain_statement_ja: 骨転移の過半数は乳癌と前立腺癌によるものであり、骨転移は疼痛、病的骨折、脊髄圧迫、高カルシウム血症などの骨関連事象を引き起こし、病的状態の主要な原因となる。骨転移は原発性骨腫瘍よりはるかに頻度が高い。
    condition:
      population: 骨転移を有するがん患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1904
    source: 'Macedo F, Ladeira K, Pinho F, et al. Bone Metastases: An Overview. Oncol Rev. 2017;11(1):321（PMCID: PMC5444408）'
    doi: 10.4081/oncol.2017.321
    pmid: '28584570'
    pmcid: null
    url: https://doi.org/10.4081/oncol.2017.321
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原発巣の全身治療は本カードの対象外（転移巣の病態に限定）。肺癌・腎癌など他の原発の頻度順位は本出典の本文記載にばらつきがあるため、命題は過半数を占める乳癌・前立腺癌に絞った。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-C（転移性骨腫瘍、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-641 (id: Jlvnmb8)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-013
  domain: BO
  subdomain: 転移性骨腫瘍
  assertion:
    plain_statement_ja: 転移性骨腫瘍の管理では、ビスホスホネートや抗 RANKL 抗体デノスマブなどの骨修飾薬が骨折などの骨関連事象の予防・遅延に用いられ、局所の骨痛には放射線治療が選択され、切迫骨折には内固定と術後照射、長管骨・股関節の骨折や脊髄圧迫には手術が適応となる。
    condition:
      population: 骨転移を有するがん患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1904
    source: 'Macedo F, Ladeira K, Pinho F, et al. Bone Metastases: An Overview. Oncol Rev. 2017;11(1):321（PMCID: PMC5444408）'
    doi: 10.4081/oncol.2017.321
    pmid: '28584570'
    pmcid: null
    url: https://doi.org/10.4081/oncol.2017.321
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤名のあるカードとしての注記：デノスマブ（ランマーク皮下注120mg）は国内で「多発性骨髄腫による骨病変及び固形癌骨転移による骨病変」の効能で2012年に承認され保険適用があることを PMDA 資料で確認した。ゾレドロン酸（ゾメタ）も国内承認薬だが、効能文言の個別照合は本作成では行っていない。投与間隔の最適化（12週ごと投与など）は本出典の範囲外。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-C（転移性骨腫瘍、a）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)；TBL-01-00-641 (id: Jlvnmb8)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-014
  domain: BO
  subdomain: 単発性骨囊腫
  assertion:
    plain_statement_ja: 単発性骨囊腫は骨未成熟の患者の上腕骨近位・大腿骨近位に好発する良性病変で、病的骨折で発見されることが多く、画像では骨幹端の中央に位置する透亮像と皮質の菲薄化を示す。
    condition:
      population: 骨未成熟の単発性骨囊腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1905
    source: 'Pretell-Mazzini J, Murphy RF, Kushare I, Dormans JP. Unicameral bone cysts: general characteristics and management controversies. J Am Acad Orthop Surg. 2014;22(5):295-303'
    doi: 10.5435/JAAOS-22-05-295
    pmid: '24788445'
    pmcid: null
    url: https://doi.org/10.5435/JAAOS-22-05-295
    source_license: © American Academy of Orthopaedic Surgeons（JAAOS、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 治療（経過観察、穿刺・注入、掻爬など）の優劣は確立しておらず、本出典でも管理方法に定まった標準はないとされているため、治療の命題は立てていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-D-①（単発性骨囊腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-015
  domain: BO
  subdomain: 動脈瘤様骨囊腫
  assertion:
    plain_statement_ja: 動脈瘤様骨囊腫は10〜20代に多く、骨幹端の膨隆した透亮性病変として現れ、MRI で fluid-fluid level を示し、組織学的には血液で満たされた腔が線維性組織に隔てられた構造である。治療の主体は掻爬と骨移植である。
    condition:
      population: 動脈瘤様骨囊腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1906
    source: Rapp TB, Ward JP, Alaia MJ. Aneurysmal bone cyst. J Am Acad Orthop Surg. 2012;20(4):233-241
    doi: 10.5435/JAAOS-20-04-233
    pmid: '22474093'
    pmcid: null
    url: https://doi.org/10.5435/JAAOS-20-04-233
    source_license: © American Academy of Orthopaedic Surgeons（JAAOS、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: USP6 遺伝子再構成などの分子病理や、続発性（他の腫瘍に伴う）動脈瘤様骨囊腫の頻度は本出典の抄録範囲を超えるため命題に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-D-②（動脈瘤様骨囊腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-016
  domain: BO
  subdomain: 線維性骨異形成
  assertion:
    plain_statement_ja: 線維性骨異形成は GNAS 遺伝子の体細胞機能獲得変異によるモザイク疾患で、単純X線ではすりガラス状陰影が特徴であり、骨病変にカフェオレ斑や思春期早発症などの骨外病変を伴うものが McCune-Albright 症候群である。
    condition:
      population: 線維性骨異形成・McCune-Albright 症候群患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1907
    source: 'Javaid MK, Boyce A, Appelman-Dijkstra N, et al. Best practice management guidelines for fibrous dysplasia/McCune-Albright syndrome: a consensus statement from the FD/MAS international consortium. Orphanet J Rare Dis. 2019;14(1):139（PMCID: PMC6567644）'
    doi: 10.1186/s13023-019-1102-9
    pmid: '31196103'
    pmcid: null
    url: https://doi.org/10.1186/s13023-019-1102-9
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: すりガラス状陰影と症候群の定義はガイドライン本文（全文）で確認し、抄録のみでは確認できない内容であることを明記する。ビスホスホネートの疼痛への使用など治療の詳細は本カードの範囲外。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-D-③（線維性骨異形成、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-017
  domain: BO
  subdomain: 脂肪腫
  assertion:
    plain_statement_ja: 四肢の脂肪性腫瘍は最も多い軟部病変で、その大部分は良性の脂肪腫である。ただし筋膜より深部にあり長径5cmを超える脂肪性病変は、異型脂肪性腫瘍や脱分化型脂肪肉腫との鑑別のため、経皮生検（MDM2 遺伝子増幅の検出を含む）による精査を要する。
    condition:
      population: 四肢の脂肪性軟部腫瘍患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1908
    source: Le Nail LR, Crenn V, Rosset P, Ropars M. Management of adipose tumors in the limbs. Orthop Traumatol Surg Res. 2022;108(1S):103162
    doi: 10.1016/j.otsr.2021.103162
    pmid: '34863958'
    pmcid: null
    url: https://doi.org/10.1016/j.otsr.2021.103162
    source_license: © Elsevier Masson SAS（著作権表示あり・CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は四肢の脂肪性腫瘍に関するフランスの専門家グループの総説であり、体幹・後腹膜の脂肪性腫瘍の扱いは異なる場合がある。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-E-①（脂肪腫、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-018
  domain: BO
  subdomain: 血管腫
  assertion:
    plain_statement_ja: 筋肉内血管腫は緩徐に経過する軟部腫瘤で軟部肉腫と紛らわしいことがあるが、画像では境界明瞭で分葉状を呈し、内部に脂肪・血管チャンネル・石灰化（静脈石）を伴うことが特徴である。
    condition:
      population: 筋肉内血管腫の成人患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1909
    source: 'Griffin N, Khan N, Thomas JM, Fisher C, Moskovic EC. The radiological manifestations of intramuscular haemangiomas in adults: magnetic resonance imaging, computed tomography and ultrasound appearances. Skeletal Radiol. 2007;36(11):1051-1059'
    doi: 10.1007/s00256-007-0375-6
    pmid: '17849114'
    pmcid: null
    url: https://doi.org/10.1007/s00256-007-0375-6
    source_license: © Springer（Skeletal Radiology、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は2007年の単施設の画像検討であり、ISSVA 分類に基づく血管奇形との鑑別や、乳児血管腫（GLUT1 陽性）とは対象が異なる。治療（切除・塞栓など）の適応は本出典の範囲外。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-E-②（血管腫、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-019
  domain: BO
  subdomain: 神経鞘腫
  assertion:
    plain_statement_ja: 神経鞘腫は末梢神経腫瘍で最も多く、被膜を有するため神経から摘出（enucleation）できることが多いが、神経束を巻き込む例も多く、その場合は摘出に伴って機能障害を来しうる。
    condition:
      population: 軟部の神経鞘腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1910
    source: 'Tang CY, Fung B, Fok M, Zhu J. Schwannoma in the upper limbs. Biomed Res Int. 2013;2013:167196（PMCID: PMC3777180）'
    doi: 10.1155/2013/167196
    pmid: '24093090'
    pmcid: null
    url: https://doi.org/10.1155/2013/167196
    source_license: CC BY
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本カードは軟部の神経鞘腫に関するもので、頭蓋内の聴神経鞘腫（前庭神経鞘腫）とは別である。腫瘍が神経に対して偏心性に発生する点は本出典の抄録で直接確認できなかったため、命題は被膜と摘出可能性に絞った。出典は上肢例8例の後方視的検討を含む総説で、症例数は少ない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-E-③（神経鞘腫、b）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-020
  domain: BO
  subdomain: グロムス腫瘍
  assertion:
    plain_statement_ja: グロムス腫瘍は手の爪下に好発する良性の血管性腫瘍で、限局した圧痛・激しい疼痛・寒冷過敏の古典的3徴を呈し、治療は完全な外科的切除である。
    condition:
      population: グロムス腫瘍患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1911
    source: 'Morey VM, Garg B, Kotwal PP. Glomus tumours of the hand: Review of literature. J Clin Orthop Trauma. 2016;7(4):286-291（PMCID: PMC5106475）'
    doi: 10.1016/j.jcot.2016.04.006
    pmid: '27857505'
    pmcid: null
    url: https://doi.org/10.1016/j.jcot.2016.04.006
    source_license: ライセンス未確認（Journal of Clinical Orthopaedics and Trauma、CC 表示を確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: Love のピンテスト、Hildreth テストなどの臨床テストや MRI の感度の数値は本出典の抄録では確認できなかったため命題に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-E-④（グロムス腫瘍、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-021
  domain: BO
  subdomain: 類腱腫
  assertion:
    plain_statement_ja: デスモイド腫瘍（デスモイド型線維腫症）は遠隔転移をしないが局所侵襲性を示す線維芽細胞性増殖で、経過は多様で予測が難しく、従来の手術を第一選択とする方針から、積極的経過観察（active surveillance）を中心とする保存的な管理へと方針が転換している。
    condition:
      population: デスモイド腫瘍患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1912
    source: 'Desmoid Tumor Working Group. The management of desmoid tumours: A joint global consensus-based guideline approach for adult and paediatric patients. Eur J Cancer. 2020;127:96-107'
    doi: 10.1016/j.ejca.2019.11.013
    pmid: '32004793'
    pmcid: null
    url: https://doi.org/10.1016/j.ejca.2019.11.013
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: active surveillance の具体的な画像間隔や、治療介入へ切り替える基準はガイドライン本文の範囲であり、本カードの抄録確認範囲を超える。家族性腺腫性ポリポーシスに伴うデスモイドは本カードの主対象（孤発性）とは経過が異なる場合がある。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-E-⑤（類腱腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-022
  domain: BO
  subdomain: 類腱腫
  assertion:
    plain_statement_ja: γセクレターゼ阻害薬ニロガセスタットは、進行性のデスモイド腫瘍の成人患者を対象とした第III相試験で、プラセボに比べて無増悪生存期間を有意に延長し（ハザード比 0.29、95%信頼区間 0.15〜0.55）、奏効率も高かった（41% 対 8%）。
    condition:
      population: 進行性デスモイド腫瘍の成人患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1913
    source: Gounder M, Ratan R, Alcindor T, et al. Nirogacestat, a γ-Secretase Inhibitor for Desmoid Tumors. N Engl J Med. 2023;388(10):898-912
    doi: 10.1056/NEJMoa2210140
    pmid: '36884323'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa2210140
    source_license: © Massachusetts Medical Society（NEJM、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤名のあるカードとしての注記：ニロガセスタットは米国で2023年に進行性デスモイド腫瘍に対して承認されたが、国内では未承認であり、日本人の成人進行性デスモイド腫瘍患者を対象とした第II相試験が進行中であることを治験登録で確認した（保険適用なし）。なお、ソラフェニブも第III相試験（NEJM 2018）で無増悪生存期間の有意な延長が示されているが、本パートでは出典枠の都合で専用カードは作らなかった。ソラフェニブのデスモイド腫瘍への使用は国内では適応外である。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-E-⑤（類腱腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-023
  domain: BO
  subdomain: 脂肪肉腫
  assertion:
    plain_statement_ja: 高分化型脂肪肉腫と脱分化型脂肪肉腫は合わせて脂肪肉腫の最大の亜群をなし、12q13-15領域（MDM2・CDK4 を含む）の高レベル増幅を共有する。高分化型は転移しないが、脱分化を起こすと局所再発・転移を来しうるより侵襲的な経過をとる。
    condition:
      population: 脂肪肉腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1914
    source: 'Thway K. Well-differentiated liposarcoma and dedifferentiated liposarcoma: An updated review. Semin Diagn Pathol. 2019;36(2):112-121'
    doi: 10.1053/j.semdp.2019.02.006
    pmid: '30852045'
    pmcid: null
    url: https://doi.org/10.1053/j.semdp.2019.02.006
    source_license: © Elsevier（Seminars in Diagnostic Pathology、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 粘液型・多形型など他の亜型の頻度と予後は本出典（高分化型・脱分化型の総説）の対象外であり命題に含めていない。脂肪肉腫全体が軟部肉腫の中で多い型であることは、BO-017 の出典（四肢の脂肪性腫瘍は最も多い軟部病変）とも整合するが、本カードでは高分化型・脱分化型に範囲を限った。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-F-①（脂肪肉腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-024
  domain: BO
  subdomain: 滑膜肉腫
  assertion:
    plain_statement_ja: 滑膜肉腫は軟部肉腫の5〜10%を占め、t(X;18) 転座による SS18:SSX 融合遺伝子を特徴とし、他の軟部肉腫より若年に発症する。治療の標準は広範切除であり、大きく深部にある病変では術前・術後の放射線治療が用いられる。
    condition:
      population: 滑膜肉腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1915
    source: 'Gazendam AM, Popovic S, Munir S, et al. Synovial Sarcoma: A Clinical Review. Curr Oncol. 2021;28(3):1909-1920（PMCID: PMC8161765）'
    doi: 10.3390/curroncol28030177
    pmid: '34069748'
    pmcid: null
    url: https://doi.org/10.3390/curroncol28030177
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 関節近傍に多いとされる発生部位の傾向や、化学療法の位置づけ（集団によって生存利益の議論がある）については抄録の範囲で定量的な確認ができなかったため命題に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-F-②（滑膜肉腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-025
  domain: BO
  subdomain: 悪性末梢神経鞘腫瘍
  assertion:
    plain_statement_ja: 悪性末梢神経鞘腫瘍の約50%は神経線維腫症1型（NF1）に合併して発生し、残りは孤発性または放射線照射後であり、予後は一般に不良で、集学的治療を行っても再発率が高い。
    condition:
      population: 悪性末梢神経鞘腫瘍患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1916
    source: 'Farid M, Demicco EG, Garcia R, et al. Malignant peripheral nerve sheath tumors. Oncologist. 2014;19(2):193-201（PMCID: PMC3926794）'
    doi: 10.1634/theoncologist.2013-0328
    pmid: '24470531'
    pmcid: null
    url: https://doi.org/10.1634/theoncologist.2013-0328
    source_license: ライセンス未確認（The Oncologist、CC 表示を確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 生存率の具体的数値は原著研究間で幅があり、本出典の抄録では単一の数値として確認できなかったため命題に含めていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-F-③（悪性末梢神経鞘腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-026
  domain: BO
  subdomain: 平滑筋肉腫
  assertion:
    plain_statement_ja: 平滑筋肉腫は平滑筋分化を示す悪性腫瘍で、子宮・後腹膜・四肢に好発し、発生部位により治療が異なるため、専門チームによる集学的管理が必須である。
    condition:
      population: 平滑筋肉腫患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1917
    source: Haddox CL, Papke DJ Jr, Serrano C. Leiomyosarcoma Therapeutic Approaches and Future Directions. Hematol Oncol Clin North Am. 2025;39(4):785-804
    doi: 10.1016/j.hoc.2025.04.007
    pmid: '40410055'
    pmcid: null
    url: https://doi.org/10.1016/j.hoc.2025.04.007
    source_license: © Elsevier Inc.（著作権表示あり・CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 血行性転移（肺転移が多いこと）やリンパ行性転移が少ないことは臨床的に知られるが、本出典の抄録では確認できなかったため命題に含めていない。子宮平滑筋肉腫の術前診断（子宮筋腫との鑑別）は本カードの範囲外。
  curriculum:
    kokushi: 医学各論 Ⅸ-9-F-④（平滑筋肉腫、c）
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: BO-027
  domain: BO
  subdomain: 軟部肉腫総論
  assertion:
    plain_statement_ja: 骨・軟部肉腫の生検では診断エラーや手技の問題が少なくなく、生検に起因する問題のために不必要な切断を余儀なくされた症例も報告されている。エラー・合併症・転帰の変更は紹介元施設で行われた生検で治療施設の2〜12倍多く、生検は最終手術を行う治療施設で、その切除計画と整合させて行うべきである。
    condition:
      population: 骨・軟部肉腫が疑われる患者
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1918
    source: Mankin HJ, Mankin CJ, Simon MA. The hazards of the biopsy, revisited. Members of the Musculoskeletal Tumor Society. J Bone Joint Surg Am. 1996;78(5):656-663
    doi: 10.2106/00004623-199605000-00004
    pmid: '8642021'
    pmcid: null
    url: https://doi.org/10.2106/00004623-199605000-00004
    source_license: © The Journal of Bone and Joint Surgery（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は1996年の米国の多施設調査であり、現在の画像ガイド下針生検の普及した状況とは前提が異なる可能性がある。軟部肉腫総論のカードとして特定の国試項目には対応づけず kokushi は null とした。広範切除の切除縁の定義や国内の骨・軟部腫瘍診療ガイドラインの推奨は、本パートでは本文を確認できる一次資料が得られなかったため専用カードを作っていない。
  curriculum:
    kokushi: null
    core_curriculum: 'PS-02-05-05 (id: JkxnuQc)'
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応の一覧

| カードID | 出題基準 | コアカリ |
|---|---|---|
| BD-001 | 医学各論 Ⅸ-7-C-①（骨粗鬆症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw) |
| BD-002 | 医学各論 Ⅸ-7-C-①（骨粗鬆症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw) |
| BD-003 | 医学各論 Ⅸ-7-C-①（骨粗鬆症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw) |
| BD-004 | 医学各論 Ⅸ-7-C-①（骨粗鬆症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw) |
| BD-005 | 医学各論 Ⅸ-7-C-①（骨粗鬆症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw) |
| BD-006 | 医学各論 Ⅸ-7-C-①（骨粗鬆症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw) |
| BD-007 | 医学各論 Ⅸ-7-C-①（骨粗鬆症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw) |
| BD-008 | 医学各論 Ⅸ-7-C-①（骨粗鬆症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw) |
| BD-009 | 医学各論 Ⅸ-7-C-①（骨粗鬆症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw) |
| BD-010 | 医学各論 Ⅸ-7-C-①（骨粗鬆症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-132 (id: Jlvnlnw) |
| BD-011 | 医学各論 Ⅸ-7-C-②（くる病、骨軟化症、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-133 (id: Jlvnln4) |
| BD-012 | 医学各論 Ⅸ-7-C-②（くる病、骨軟化症、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-133 (id: Jlvnln4) |
| BD-013 | 医学各論 Ⅸ-7-C-②（くる病、骨軟化症、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-133 (id: Jlvnln4) |
| BD-014 | 医学各論 Ⅸ-7-C-③（骨Paget病、b） | PS-02-05-05 (id: JkxnuQc) |
| BD-015 | 医学各論 Ⅸ-7-C-③（骨Paget病、b） | PS-02-05-05 (id: JkxnuQc) |
| BD-016 | 医学各論 Ⅸ-7-B-②（骨形成不全症、c） | PS-02-05-05 (id: JkxnuQc) |
| BD-017 | 医学各論 Ⅸ-7-B-②（骨形成不全症、c） | PS-02-05-05 (id: JkxnuQc) |
| BD-018 | 医学各論 Ⅸ-7-B-①（軟骨無形成症、c） | PS-02-05-05 (id: JkxnuQc) |
| BD-019 | 医学各論 Ⅸ-7-B-①（軟骨無形成症、c） | PS-02-05-05 (id: JkxnuQc) |
| BD-020 | 医学各論 Ⅸ-7-B-①（軟骨無形成症、c） | PS-02-05-05 (id: JkxnuQc) |
| OS-001 | 医学各論 Ⅸ-8-H-①（関節リウマチ、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-557 (id: JmxLo0Y) |
| OS-002 | 医学各論 Ⅸ-8-H-①（関節リウマチ、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-557 (id: JmxLo0Y) |
| OS-003 | 医学各論 Ⅸ-8-H-①（関節リウマチ、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-557 (id: JmxLo0Y) |
| OS-004 | 医学各論 Ⅸ-8-H-①（関節リウマチ、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-557 (id: JmxLo0Y) |
| OS-005 | 医学各論 Ⅸ-8-H-②（痛風、偽痛風、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE) |
| OS-006 | 医学各論 Ⅸ-8-H-②（痛風、偽痛風、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE) |
| OS-007 | 医学各論 Ⅸ-8-H-②（痛風、偽痛風、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE) |
| OS-008 | 医学各論 Ⅸ-8-H-③（滑液包炎、腱鞘炎、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-144 (id: JlvnloQ) |
| OS-009 | 医学各論 Ⅸ-8-H-③（滑液包炎、腱鞘炎、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-143 (id: JlvnloI) |
| OS-010 | 医学各論 Ⅸ-8-H-③（滑液包炎、腱鞘炎、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-143 (id: JlvnloI) |
| OS-011 | 医学各論 Ⅸ-8-I-①（変形性関節症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc) |
| OS-012 | 医学各論 Ⅸ-8-I-①（変形性関節症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc) |
| OS-013 | 医学各論 Ⅸ-8-I-②（神経病性関節症、c） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE) |
| OS-014 | 医学各論 Ⅸ-8-I-③（血友病性関節症、c） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE) |
| OS-015 | 医学各論 Ⅸ-8-J-①（ガングリオン、a） | PS-02-05-05 (id: JkxnuQc) |
| OS-016 | 医学各論 Ⅸ-8-J-②（異所性骨化、b） | PS-02-05-05 (id: JkxnuQc) |
| OS-017 | 医学各論 Ⅸ-8-J-③（腱付着部炎、c） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-142 (id: JlvnloE) |
| OS-018 | 医学各論 Ⅸ-8-G-①（Kienböck病、特発性膝骨壊死、c） | PS-02-05-05 (id: JkxnuQc) |
| OS-019 | 医学各論 Ⅸ-8-G-①（Kienböck病、特発性膝骨壊死、c） | PS-02-05-05 (id: JkxnuQc) |
| OS-020 | 医学各論 Ⅸ-8-C-①（Dupuytren拘縮、b） | PS-02-05-05 (id: JkxnuQc) |
| OS-021 | 医学各論 Ⅸ-8-C-②（強剛母指、c） | PS-02-05-05 (id: JkxnuQc) |
| OS-022 | 医学各論 Ⅸ-8-A-③（反復性脱臼、b） | PS-02-05-05 (id: JkxnuQc) |
| OS-023 | 医学各論 Ⅸ-8-A-④（胸郭出口症候群、c） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-126 (id: JlvnlpA) |
| OS-024 | 医学各論 Ⅸ-8-B-②（上腕骨外側上顆炎、b） | PS-02-05-05 (id: JkxnuQc) |
| OS-025 | 医学各論 Ⅸ-8-A-①（肩関節周囲炎、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-152 (id: JlvnlqI) |
| OS-026 | 医学各論 Ⅸ-8-A-①（肩関節周囲炎、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-152 (id: JlvnlqI) |
| OS-027 | 医学各論 Ⅸ-8-A-②（腱板断裂、a） | PS-02-05-05 (id: JkxnuQc) |
| OS-028 | 医学各論 Ⅸ-8-A-②（腱板断裂、a） | PS-02-05-05 (id: JkxnuQc) |
| OS-029 | 医学各論 Ⅸ-8-B-①（肘内障、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-150 (id: JlvnlnM) |
| OS-030 | 医学各論 Ⅸ-8-B-①（肘内障、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-150 (id: JlvnlnM) |
| OS-031 | 医学各論 Ⅸ-8-D-①（変形性股関節症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc) |
| OS-032 | 医学各論 Ⅸ-8-D-①（変形性股関節症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc) |
| OS-033 | 医学各論 Ⅸ-8-D-②（発育性股関節形成不全<先天性股関節脱臼>、b） | PS-02-05-05 (id: JkxnuQc) |
| OS-034 | 医学各論 Ⅸ-8-D-②（発育性股関節形成不全<先天性股関節脱臼>、b） | PS-02-05-05 (id: JkxnuQc) |
| OS-035 | 医学各論 Ⅸ-8-D-③（大腿骨頭すべり症、b） | PS-02-05-05 (id: JkxnuQc) |
| OS-036 | 医学各論 Ⅸ-8-D-④（特発性大腿骨頭壊死症、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-136 (id: JlvnlrA) |
| OS-037 | 医学各論 Ⅸ-8-D-④（特発性大腿骨頭壊死症、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-136 (id: JlvnlrA) |
| OS-038 | 医学各論 Ⅸ-8-D-⑤（Perthes病、c） | PS-02-05-05 (id: JkxnuQc) |
| OS-039 | 医学各論 Ⅸ-8-E-①（変形性膝関節症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc) |
| OS-040 | 医学各論 Ⅸ-8-E-①（変形性膝関節症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc) |
| OS-041 | 医学各論 Ⅸ-8-E-①（変形性膝関節症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc) |
| OS-042 | 医学各論 Ⅸ-8-E-①（変形性膝関節症、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc) |
| OS-043 | 医学各論 Ⅸ-8-E-②（Osgood-Schlatter病、b） | PS-02-05-05 (id: JkxnuQc) |
| OS-044 | 医学各論 Ⅸ-8-E-③（半月板障害、b） | PS-02-05-05 (id: JkxnuQc) |
| OS-045 | 医学各論 Ⅸ-8-F-①（外反母趾、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-147 (id: Jlvnlok) |
| OS-046 | 医学各論 Ⅸ-8-F-①（外反母趾、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-147 (id: Jlvnlok) |
| OS-047 | 医学各論 Ⅸ-8-F-②（内反足、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-135 (id: Jlvnlqw) |
| OS-048 | 医学各論 Ⅸ-8-F-③（変形性足関節症、c） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-146 (id: Jlvnloc) |
| OS-049 | 医学各論 Ⅸ-8-E-④（膝蓋軟骨軟化症、c） | PS-02-05-05 (id: JkxnuQc) |
| OS-050 | 医学各論 Ⅸ-8-E-④（膝蓋軟骨軟化症、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-001 | 医学各論 Ⅸ-9-A-①（骨軟骨腫、b） | PS-02-05-05 (id: JkxnuQc) |
| BO-002 | 医学各論 Ⅸ-9-A-②（内軟骨腫、b） | PS-02-05-05 (id: JkxnuQc) |
| BO-003 | 医学各論 Ⅸ-9-A-③（類骨骨腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-004 | 医学各論 Ⅸ-9-A-④（骨巨細胞腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-005 | 医学各論 Ⅸ-9-A-④（骨巨細胞腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-006 | 医学各論 Ⅸ-9-B-①（骨肉腫、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-638 (id: Jlvnmbo) |
| BO-007 | 医学各論 Ⅸ-9-B-①（骨肉腫、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-638 (id: Jlvnmbo) |
| BO-008 | 医学各論 Ⅸ-9-B-①（骨肉腫、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-638 (id: Jlvnmbo) |
| BO-009 | 医学各論 Ⅸ-9-B-②（軟骨肉腫、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-639 (id: Jlvnmbs) |
| BO-010 | 医学各論 Ⅸ-9-B-③（Ewing肉腫、b） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-640 (id: Jlvnmb0) |
| BO-011 | 医学各論 Ⅸ-9-B-④（脊索腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-012 | 医学各論 Ⅸ-9-C（転移性骨腫瘍、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-641 (id: Jlvnmb8) |
| BO-013 | 医学各論 Ⅸ-9-C（転移性骨腫瘍、a） | PS-02-05-05 (id: JkxnuQc)；TBL-01-00-641 (id: Jlvnmb8) |
| BO-014 | 医学各論 Ⅸ-9-D-①（単発性骨囊腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-015 | 医学各論 Ⅸ-9-D-②（動脈瘤様骨囊腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-016 | 医学各論 Ⅸ-9-D-③（線維性骨異形成、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-017 | 医学各論 Ⅸ-9-E-①（脂肪腫、b） | PS-02-05-05 (id: JkxnuQc) |
| BO-018 | 医学各論 Ⅸ-9-E-②（血管腫、b） | PS-02-05-05 (id: JkxnuQc) |
| BO-019 | 医学各論 Ⅸ-9-E-③（神経鞘腫、b） | PS-02-05-05 (id: JkxnuQc) |
| BO-020 | 医学各論 Ⅸ-9-E-④（グロムス腫瘍、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-021 | 医学各論 Ⅸ-9-E-⑤（類腱腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-022 | 医学各論 Ⅸ-9-E-⑤（類腱腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-023 | 医学各論 Ⅸ-9-F-①（脂肪肉腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-024 | 医学各論 Ⅸ-9-F-②（滑膜肉腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-025 | 医学各論 Ⅸ-9-F-③（悪性末梢神経鞘腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-026 | 医学各論 Ⅸ-9-F-④（平滑筋肉腫、c） | PS-02-05-05 (id: JkxnuQc) |
| BO-027 | なし | PS-02-05-05 (id: JkxnuQc) |

## 4. 未解決事項

- 骨Paget病の合併症のうち骨肉腫化と高拍出性心不全は、確認できた一次資料の範囲で検証できず、カードに入れていない（BD-015 の uncertainty に明記。補完候補）。ゾレドロン酸の骨Paget病への国内適応も未確認。
- コラゲナーゼ（Dupuytren 拘縮）の国内承認（2015年）は確認したが、その後の販売・供給状況は未確認（OS-020 の uncertainty に明記）。
- 指定難病の診断基準（SRC-1845）の GOV_JP 区分は、取り込み側の最終確認事項。
- 腱板断裂の身体所見（有痛弧・ドロップアーム）の診断精度、DDH の Allis/Galeazzi 徴候、変形性股関節症の関節温存手術、変形性足関節症の治療比較は、採用出典で確認できず命題化していない（各カードの uncertainty に明記。補完候補）。
- Ewing 肉腫の onion-peel 状骨膜反応、神経鞘腫の偏心性発生、平滑筋肉腫の血行性転移は、確認した一次資料に明示がなく各カードの uncertainty に記録した。
- 骨粗鬆症のガイドラインは 2025 年版（最新）を使用した。

## 5. 次回への引き継ぎ

- 欠番: なし。BD・OS・BO とも連番でそろっている。
- カードのない小項目: なし（対象56項目すべてにカードあり）。BO の軟部肉腫総論1件は kokushi null。
- 統合した重複: OARSI ガイドライン（DOI 10.1016/j.joca.2019.06.011）に SRC-1855 と SRC-1884 の2番号が付いたため、SRC-1855 に統一した。**SRC-1884 は未使用**（本回の範囲内）。
- 未使用の SRC: SRC-1870、SRC-1919〜1920（本回の範囲内。次回は第32回の範囲 SRC-1921 から使う）。
- 既存出典の再利用: SRC-927（骨粗鬆症の診断）、SRC-932（栄養性くる病）、SRC-992（ACR 痛風ガイドライン2020。source_class は出典マスターの登録どおり UNKNOWN とした）。
- 第32回は TJ・AN で第Ⅸ章の最終回。脊髄損傷では排尿障害の詳細を作らない（KX を正）。神経皮膚症候群の皮膚所見は DT 済みのため AN では中枢神経・全身の側面に絞る。下垂体腫瘍は BT 済み。
