# バッチ58（DL：分娩・産褥）パブリックドメイン出典の裏づけ調査

- 調査日：2026-11-13
- 対象：DL の22件（DL-001〜005、008〜017、019〜025。DL-006・007・018 は主出典が既に OPEN のため対象外）
- ルール：抄録・添付文書・医学百科は根拠にしない。使えるのは政府の全文文書・報告書、CC BY 全文、試験登録レコードなど、全文で読める資料のみ。抄録は数値の食い違い確認にだけ使う。カードの主張・数値は変えない。
- 出典の説明は出典マスター（sources.yaml）の記載からそのまま転記し、識別子（PMID・PMCID・DOI）は DOI／PMID で個別に再照会して確認した。

## 集計

| 判定 | 件数 | 内訳 |
|---|---|---|
| A（主出典を置き換え可） | 0 | ― |
| B（裏づけを追加可） | 17 | DL-001・002・003・004・005・008・009・010・012・013・014・015・016・020・021・024・025（うち DL-015 は全要素一致、その他は部分一致） |
| C（見つからない） | 5 | DL-011・017・019・022・023 |
| D（区分訂正、別枠） | 18出典 | いずれも UNKNOWN → RESTRICTED（下記「区分訂正（別枠）」） |

## 判定一覧

| カード | 主出典（マスター記載） | 現行区分 | 判定 | 裏づけ候補と確認内容 |
|---|---|---|---|---|
| DL-001 | SRC-3263：American College of Obstetricians and Gynecologists. First and Second Stage Labor Management: Clinical Practice Guideline No. 8. Obstet Gynecol. 2024;143(1):144-162 | UNKNOWN | B（部分） | Cate JJM et al. J Clin Med. 2024;13(16):4720（CC BY 4.0、DOI 10.3390/jcm13164720、PMID 39200862、PMC11355156）：活動期は子宮口6cmからとする再定義を明記。Mappa I et al. Healthcare. 2026;14(18):3000（CC BY 4.0、DOI 10.3390/healthcare14183000、PMID 42793539、PMC13606038）：第1期進行遷延へのオキシトシン増強を扱う系統的レビュー。潜伏期遷延のみを理由とする帝王切開回避の直接文はなし |
| DL-002 | SRC-3264：Macones GA, Hankins GDV, Spong CY, Hauth J, Moore T. The 2008 National Institute of Child Health and Human Development workshop report on electronic fetal monitoring: update on definitions, interpretation, and research guidelines. Obstet Gynecol. 2008;112(3):661-666 | UNKNOWN | B（部分） | Contraction frequency and acidemia at birth: A case–control study. Acta Obstet Gynecol Scand. 2026;105(5S)（CC BY 4.0、DOI 10.1111/aogs.70181、PMID 41782222、PMC13125349）：tachysystole の FIGO 定義「10分間に5回超、30分間の平均」を明記し、カードの NICHD 定義と実質一致。胎児心拍反応の併記と「hyperstimulation を用いない」点は未確認 |
| DL-003 | SRC-3265：Maharaj D. Assessing cephalopelvic disproportion: back to the basics. Obstet Gynecol Surv. 2010;65(6):387-395 | UNKNOWN | B（部分） | Modern Utility of Pelvimetry: a Relevant Tool or an Outdated Concept? Cureus. 2025;17(10)（CC BY 4.0、DOI 10.7759/cureus.95522、PMID 41322796、PMC12658874）：X線骨盤計測は経腟分娩成功の予測能が低く臨床的価値は限定的、臨床骨盤計測は教育・診療に残る。CPD の定義文の直接記載はなし |
| DL-004 | SRC-3266：American College of Obstetricians and Gynecologists. Mode of Term Singleton Breech Delivery: Committee Opinion No. 745. Obstet Gynecol. 2018;132(2):e60-e63 | UNKNOWN | B（部分） | Procedural Optimisation and Unmeasured Implementation in External Cephalic Version at Term: A Narrative Review of a Measurement Asymmetry. Healthcare. 2026;14(20):3452（CC BY 4.0、DOI 10.3390/healthcare14203452、PMID 42940496、PMC13704564）：禁忌がなければ ECV を提示すべきことが各学会推奨（ACOG・RANZCOG は Grade A、RCOG は37週0日から）として明記。分娩様式の決め方、緊急帝王切開可能な施設でのみ実施、計画的経腟骨盤位分娩のプロトコルと同意文書化は未確認 |
| DL-005 | SRC-3267：Hofmeyr GJ, Kulier R, West HM. External cephalic version for breech presentation at term. Cochrane Database Syst Rev. 2015;(4):CD000083 | UNKNOWN | B（部分） | 同上の Healthcare 2026 総説（CC BY 4.0）：Cochrane の無作為化試験レビューに基づき、ECV の試行は出生時の非頭位提示を減らし帝王切開も減らす（帝王切開は確実性 very low と明記）。「経腟頭位分娩の失敗」減少の直接記載はなし |
| DL-008 | SRC-3270：Sayed Ahmed WA, Hamdy MA. Optimal management of umbilical cord prolapse. Int J Womens Health. 2018;10:459-465 | RESTRICTED | B（部分） | Umbilical Cord Prolapse—Interesting CTG Traces. Diagnostics. 2022;12(11):2845（CC BY 4.0、DOI 10.3390/diagnostics12112845、PMID 36428904、PMC9689471）：発生率1〜6/1,000妊娠（＝0.1〜0.6%）、危険因子（胎位異常・早産等）、先進部の用手的挙上と膀胱充満、decision-to-incision 30分未満で転帰良好。医原性約50%の数値、膀胱充満量500〜700 mL、臍帯の過剰な触診回避は未確認。主出典は CC BY-NC 3.0 のため RESTRICTED の現行区分が正しい |
| DL-009 | SRC-3263：American College of Obstetricians and Gynecologists. First and Second Stage Labor Management: Clinical Practice Guideline No. 8. Obstet Gynecol. 2024;143(1):144-162 | UNKNOWN | B（部分） | Cate JJM et al. J Clin Med. 2024;13(16):4720（CC BY 4.0）：第1期停止の基準「6cm以上・破水後、十分な収縮で4時間／不十分ならオキシトシン6時間で変化なし」を明記しカードと一致。第2期は初産婦 pushing 3時間（硬膜外なし）を確認。経産婦2時間の閾値は未確認 |
| DL-010 | SRC-3271：American College of Obstetricians and Gynecologists. Shoulder Dystocia: Practice Bulletin No. 178. Obstet Gynecol. 2017;129(5):e123-e133 | UNKNOWN | B（部分） | Audit of Shoulder Dystocia Management and Outcomes at a Busy Hospital in the United Kingdom. Cureus. 2025;17(11)（CC BY 4.0、DOI 10.7759/cureus.97528、PMID 41446480、PMC12723310）：発生率1.32%でカードの0.2〜3%の範囲内、largely unpredictable と明記、第一選択は McRoberts＋恥骨上圧迫（症例の80.4%）。子宮底圧迫の回避は未確認 |
| DL-011 | SRC-3272：American College of Obstetricians and Gynecologists. Vaginal Birth After Cesarean Delivery: Practice Bulletin No. 205. Obstet Gynecol. 2019;133(2):e110-e127 | UNKNOWN | C | AHRQ Evidence Report No. 191（GOV_US、Bookshelf NBK44571）と NIH Consensus Statement 2010 の存在は確認したが、NCBI の reCAPTCHA で全文を開けず数値照合ができなかった。CC BY と思われた仏多施設研究は実際は CC BY-NC で使用不可。申し送り参照 |
| DL-012 | SRC-3273：American College of Obstetricians and Gynecologists. Prevention and Management of Obstetric Lacerations at Vaginal Delivery: Practice Bulletin No. 198. Obstet Gynecol. 2018;132(3):e87-e102 | UNKNOWN | B（部分） | Sultan AH et al. IUGA International Guidelines on Obstetric Anal Sphincter Injuries. Int Urogynecol J. 2026;37(8)（CC BY 4.0、DOI 10.1007/s00192-026-06642-3、PMID 42429937、PMC13486146）：OASIS は3度・4度の総称、Sultan 分類（3a/3b/3c の判別を含む）の使用を Grade A で推奨、第2期の会陰保護（温罨法を含む）で OASI リスク低下。経腟分娩の53〜79%に裂傷という割合と、温罨法が1・2度には効かないという対比は未確認 |
| DL-013 | SRC-3274：日本産科婦人科学会・日本産婦人科医会・日本周産期・新生児医学会・日本麻酔科学会・日本輸血・細胞治療学会. 産科危機的出血への対応指針 2022 | RESTRICTED | B（部分） | Hayashi S et al. JA Clin Rep. 2025（CC BY 4.0、DOI 10.1186/s40981-025-00821-9、PMID 41118068、PMC12540960）：ショック指数1.5超とフィブリノゲン149 mg/dL で危機的出血を宣言しプロトコル発動、産科DICスコア9、RBC：FFP＝4単位：4単位（1:1）、子宮内バルーンと IVR 塞栓で止血（指針2022の適用例）。圧迫縫合・子宮動脈結紮・子宮摘出は本症例では未実施 |
| DL-014 | SRC-3275：American College of Obstetricians and Gynecologists. Postpartum Hemorrhage: Practice Bulletin No. 183. Obstet Gynecol. 2017;130(4):e168-e186 | UNKNOWN | B（部分） | Shekhawat K et al. Cureus. 2026;18(9)（CC BY 4.0、DOI 10.7759/cureus.116511、PMID 42898296、PMC13677613）：PPH の ACOG 統一-定義（様式によらず24時間以内に累積1,000 mL以上、または循環血液量減少徴候を伴う出血）を明記、弛緩出血の治療の中心は子宮収縮薬・とりわけオキシトシン。経腟分娩後500 mL超を異常として原因検索という運用の直接文はなし |
| DL-015 | SRC-3276：WOMAN Trial Collaborators. Effect of early tranexamic acid administration on mortality, hysterectomy, and other morbidities in women with post-partum haemorrhage (WOMAN): an international, randomised, double-blind, placebo-controlled trial. Lancet. 2017;389(10084):2105-2116 | RESTRICTED | B | 同上の Cureus 2026 総説（CC BY 4.0）：WOMAN 試験の数値をすべて再掲しカードと一致（20,060人・193施設・21か国、TXA 1 g 静注、出血死1.5% vs 1.9%・RR 0.81、3時間以内 RR 0.69、死亡または子宮摘出の複合評価項目に有意差なし、痙攣・血栓塞栓の増加なし）。試験登録 NCT00872469 は結果未掲載のため登録レコードは使えない。主出典は CC BY-NC-ND のため RESTRICTED の現行区分が正しい |
| DL-016 | SRC-3277：Society for Maternal-Fetal Medicine; Pacheco LD, Saade G, Hankins GDV, Clark SL. Amniotic fluid embolism: diagnosis and management. Am J Obstet Gynecol. 2016;215(2):B16-B24 | UNKNOWN | B（部分） | Alves ÁLL et al. Amniotic fluid embolism Number 11 – 2026. Rev Bras Ginecol Obstet. 2026;48（FEBRASGO プロトコル、CC BY 4.0、DOI 10.61622/rbgo/2026fps11、PMID 42923891、PMC13690382）：発生率1.9〜6.1/10万分娩（カードの約2〜6と一致）、診断は臨床所見と他疾患の除外による臨床診断、管理の主目標に心肺蘇生（ACLS 準拠）。「特異的検査はない」の直接文はない |
| DL-017 | SRC-3278：Baskett TF. Acute uterine inversion: a review of 40 cases. J Obstet Gynaecol Can. 2002;24(12):953-956 | UNKNOWN | C | Baskett 2002 の単一施設の実数（125,081分娩中40件、経腟1/3,737・帝王切開1/1,860、PPH合併65%、輸血47.5%）を再掲する自由全文は見つからなかった（Cureus 2026 の症例報告は引用のみで数値の再掲なし） |
| DL-019 | SRC-3280：Hayakawa M, et al. Clinical practice guidelines for management of disseminated intravascular coagulation in Japan 2024: part 4 - trauma, burn, obstetrics, acute pancreatitis/liver failure, and others. Int J Hematol. 2025;121(5):633-652 | UNKNOWN | C | JSTH ガイドライン part 4 の産科DIC推奨（フィブリノゲン濃縮製剤・アンチトロンビン濃縮製剤・トラネキサム酸）を再掲する自由全文は見つからなかった。産科DIC改訂診断基準の検証論文（J Obstet Gynaecol Res 2026、CC BY）は診断の話であり治療推奨の裏づけにならない。主出典自体は CC BY ではなく区分訂正の対象 |
| DL-020 | SRC-3281：Sit D, Rothschild AJ, Wisner KL. A Review of Postpartum Psychosis. J Womens Health (Larchmt). 2006;15(4):352-368 | UNKNOWN | B（部分） | Jairaj C et al. Postpartum psychosis: A proposed treatment algorithm. J Psychopharmacol. 2023;37(10)（CC BY 4.0、DOI 10.1177/02698811231181573、PMID 37515460、PMC10612381）：有病率1〜2/1,000出生と明記しカードと一致、産後直後の急激な発症と感情・精神病症状を記述。発症時期の詳細（2〜3日目〜1〜4週）と産後うつ10〜13%・マタニティーブルー50〜75% の対比は未確認 |
| DL-021 | SRC-3282：American College of Obstetricians and Gynecologists. Screening and Diagnosis of Mental Health Conditions During Pregnancy and Postpartum: Clinical Practice Guideline No. 4. Obstet Gynecol. 2023;141(6):1232-1261 | UNKNOWN | B（部分） | Physiological Mechanisms in Pregnancy and Their Relevance to the Clinical Management of Perinatal Mental Illness. J Clin Med. 2026;15(12):4559（CC BY 4.0、DOI 10.3390/jcm15124559、PMID 42355727、PMC13302311）：「ACOG は全妊婦にうつ病・不安のスクリーニングを推奨」と明記。検証済みツールと実施時期、産後精神病への即時対応、抗うつ薬前の双極性障害スクリーニングは未確認で、裏づけは骨格のみ |
| DL-022 | SRC-3283：Mackeen AD, et al. Antibiotic regimens for postpartum endometritis. Cochrane Database Syst Rev. 2015;(2):CD001067 | UNKNOWN | C | Cochrane の治療失敗 RR（0.69 対セファロスポリン系、0.65 対ペニシリン系、42試験・4,240人）を再掲する自由全文は見つからなかった。検索で得た総説は慢性子宮内膜炎・不妊領域や獣医領域が中心 |
| DL-023 | SRC-3284：Society for Maternal-Fetal Medicine; Plante LA, Pacheco LD, Louis JM. SMFM Consult Series #47: Sepsis during pregnancy and the puerperium. Am J Obstet Gynecol. 2019;220(4):B2-B10 | UNKNOWN | C | SMFM Consult #47 の GRADE 文を再掲する自由全文は見つからなかった。Surviving Sepsis Campaign 2021 の ICM 版 PMC 全文は WHO の時限許可による収載で CC BY ではなく使用不可。J Clin Med 2026 の産科集中治療総説は早期認識の一般論にとどまる |
| DL-024 | SRC-1020：Mitchell KB, Johnson HM, Rodríguez JM, et al. Academy of Breastfeeding Medicine Clinical Protocol #36: The Mastitis Spectrum, Revised 2022. Breastfeed Med. 2022;17(5):360-376 | UNKNOWN | B（部分） | Douglas P. Int Breastfeed J. 2023;18（CC BY 4.0、DOI 10.1186/s13006-023-00588-8、PMID 37670315、PMC10481477）：ABM #36 の本文を多数引用し、spectrum の構成（乳管狭窄・亜急性乳腺炎と mammary dysbiosis・乳瘤）、深部マッサージは悪化要因、氷の使用、炎症性乳腺炎は抗菌薬なしで改善しうることを確認。ただし本論文は #36 への批判的論考である（フラグ参照） |
| DL-025 | SRC-3285：American College of Obstetricians and Gynecologists. Thromboembolism in Pregnancy: ACOG Practice Bulletin No. 196. Obstet Gynecol. 2018;132(1):e1-e17 | UNKNOWN | B（部分） | Raia-Barjat T et al. Front Cardiovasc Med. 2022;9:863612（CC BY 4.0、DOI 10.3389/fcvm.2022.863612、PMID 35479289、PMC9037588）：発生率1〜2/1,000妊娠、妊娠中のリスク約5倍。2025 ESC ガイドライン（Neth Heart J. 2026;34(11)、CC BY 4.0、DOI 10.1007/s12471-026-02085-z、PMID 42878989、PMC13694674）：妊娠中 VTE の章で「DOAC は妊娠中は推奨されない（クラスIII）」。約80%が静脈性、米国母体死亡の9.3%は未確認（フラグ参照） |

## 区分訂正（別枠）

カード判定とは別枠で、出典マスターの source_class の訂正が18出典に必要である。いずれも現行 UNKNOWN → RESTRICTED。根拠は DOI ごとに Crossref と Europe PMC で個別に確認した。

| SRC | 出典（マスター記載） | 現行 | 訂正後 | 根拠 |
|---|---|---|---|---|
| SRC-1020 | Mitchell KB, Johnson HM, Rodríguez JM, et al. Academy of Breastfeeding Medicine Clinical Protocol #36: The Mastitis Spectrum, Revised 2022. Breastfeed Med. 2022;17(5):360-376 | UNKNOWN | RESTRICTED | 出版社（Liebert）の TDM ライセンスのみ。Europe PMC で isOpenAccess: N |
| SRC-3263 | American College of Obstetricians and Gynecologists. First and Second Stage Labor Management: Clinical Practice Guideline No. 8. Obstet Gynecol. 2024;143(1):144-162 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。OA・CC ライセンスなし |
| SRC-3264 | Macones GA, Hankins GDV, Spong CY, Hauth J, Moore T. The 2008 National Institute of Child Health and Human Development workshop report on electronic fetal monitoring: update on definitions, interpretation, and research guidelines. Obstet Gynecol. 2008;112(3):661-666 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。OA・CC ライセンスなし |
| SRC-3265 | Maharaj D. Assessing cephalopelvic disproportion: back to the basics. Obstet Gynecol Surv. 2010;65(6):387-395 | UNKNOWN | RESTRICTED | Wolters Kluwer の購読制文献。OA・CC ライセンスなし |
| SRC-3266 | American College of Obstetricians and Gynecologists. Mode of Term Singleton Breech Delivery: Committee Opinion No. 745. Obstet Gynecol. 2018;132(2):e60-e63 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。OA・CC ライセンスなし |
| SRC-3267 | Hofmeyr GJ, Kulier R, West HM. External cephalic version for breech presentation at term. Cochrane Database Syst Rev. 2015;(4):CD000083 | UNKNOWN | RESTRICTED | PMC 全文（PMC6505738）に「Copyright © 2019 The Cochrane Collaboration. Published by John Wiley & Sons, Ltd.」と明記され CC ライセンスではない |
| SRC-3271 | American College of Obstetricians and Gynecologists. Shoulder Dystocia: Practice Bulletin No. 178. Obstet Gynecol. 2017;129(5):e123-e133 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。OA・CC ライセンスなし |
| SRC-3272 | American College of Obstetricians and Gynecologists. Vaginal Birth After Cesarean Delivery: Practice Bulletin No. 205. Obstet Gynecol. 2019;133(2):e110-e127 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。OA・CC ライセンスなし |
| SRC-3273 | American College of Obstetricians and Gynecologists. Prevention and Management of Obstetric Lacerations at Vaginal Delivery: Practice Bulletin No. 198. Obstet Gynecol. 2018;132(3):e87-e102 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。OA・CC ライセンスなし |
| SRC-3275 | American College of Obstetricians and Gynecologists. Postpartum Hemorrhage: Practice Bulletin No. 183. Obstet Gynecol. 2017;130(4):e168-e186 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。OA・CC ライセンスなし |
| SRC-3277 | Society for Maternal-Fetal Medicine; Pacheco LD, Saade G, Hankins GDV, Clark SL. Amniotic fluid embolism: diagnosis and management. Am J Obstet Gynecol. 2016;215(2):B16-B24 | UNKNOWN | RESTRICTED | Elsevier 誌の購読制文献。Crossref は TDM ライセンスのみ |
| SRC-3278 | Baskett TF. Acute uterine inversion: a review of 40 cases. J Obstet Gynaecol Can. 2002;24(12):953-956 | UNKNOWN | RESTRICTED | Elsevier 誌の購読制文献。Crossref は TDM ライセンスのみ |
| SRC-3280 | Hayakawa M, et al. Clinical practice guidelines for management of disseminated intravascular coagulation in Japan 2024: part 4 - trauma, burn, obstetrics, acute pancreatitis/liver failure, and others. Int J Hematol. 2025;121(5):633-652 | UNKNOWN | RESTRICTED | Europe PMC で isOpenAccess: N。Crossref は TDM ライセンスのみで CC BY ではないことを個別に確認 |
| SRC-3281 | Sit D, Rothschild AJ, Wisner KL. A Review of Postpartum Psychosis. J Womens Health (Larchmt). 2006;15(4):352-368 | UNKNOWN | RESTRICTED | 出版社（Liebert）の TDM ライセンスのみ。PMC3109493 は著者原稿で CC ライセンス表示なし |
| SRC-3282 | American College of Obstetricians and Gynecologists. Screening and Diagnosis of Mental Health Conditions During Pregnancy and Postpartum: Clinical Practice Guideline No. 4. Obstet Gynecol. 2023;141(6):1232-1261 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。OA・CC ライセンスなし |
| SRC-3283 | Mackeen AD, et al. Antibiotic regimens for postpartum endometritis. Cochrane Database Syst Rev. 2015;(2):CD001067 | UNKNOWN | RESTRICTED | PMC 全文（PMC7050613）に「Copyright © 2015 The Cochrane Collaboration」と明記され CC ライセンスではない |
| SRC-3284 | Society for Maternal-Fetal Medicine; Plante LA, Pacheco LD, Louis JM. SMFM Consult Series #47: Sepsis during pregnancy and the puerperium. Am J Obstet Gynecol. 2019;220(4):B2-B10 | UNKNOWN | RESTRICTED | Elsevier 誌の購読制文献。Crossref は TDM ライセンスのみ |
| SRC-3285 | American College of Obstetricians and Gynecologists. Thromboembolism in Pregnancy: ACOG Practice Bulletin No. 196. Obstet Gynecol. 2018;132(1):e1-e17 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。OA・CC ライセンスなし |

なお、SRC-3270（CC BY-NC 3.0）、SRC-3276（CC BY-NC-ND）、SRC-3274（日本語学会指針）は現行の RESTRICTED が正しく、訂正は不要である。

## フラグ

- **DL-025（数値の部分的食い違い）**：裏づけ候補の VTE 発生率は1〜2/1,000妊娠で、カードの下限0.5/1,000 を含まない。母体死亡に占める割合も、カードは米国の9.3%、候補総説は先進地域の13.8% と集計が異なる。次回改訂時に主出典（ACOG Practice Bulletin No. 196）との再照合を推奨する。
- **DL-011（申し送り）**：AHRQ Evidence Report No. 191（GOV_US）は実在するが、本調査環境では NCBI の reCAPTCHA により全文照合ができず C とした。レポジトリ側の PC で全文を確認すれば B に転じる可能性がある。
- **DL-024（概念の論争）**：ABM Protocol #36 の mastitis spectrum 概念自体に批判的論考（Int Breastfeed J 2023）が存在する。今回の裏づけは #36 の内容の再掲として記録したものであり、概念の妥当性の判断はレポジトリ側に委ねる。
- **DL-012（新しい国際ガイドライン）**：IUGA の OASIS 国際ガイドラインが2026年に刊行され、Sultan 分類の運用が国際的に再確認された。カードの「経腟分娩の53〜79%に裂傷」という割合は自由全文では未確認のままである（食い違いではない）。
- **DL-013（裏づけの性質）**：裏づけ候補は指針2022を適用した症例報告であり、指針本文そのものの自由版は存在しない。主出典の RESTRICTED は妥当である。
- **DL-023（YAML 表記の注意）**：「SMFM Consult Series #47」をプレーンな YAML 値に書く場合は「 #」を含むため引用符が必須である（既知の組み立てルールの再掲）。

## 申し送り（識別子の補完候補）

出典マスターでは SRC-3263〜3285 の pmid が全件 null（カード側には記載あり）である。以下はいずれも DOI で Europe PMC を個別に照会し、DOI と PMID・PMCID の対応を確認した補完候補である。登録はレポジトリ側が PC で --online 照合した後に行う前提とする。

- PMID 補完候補（19件）：SRC-3263 → 38096556／SRC-3264 → 18757666／SRC-3265 → 20633305／SRC-3266 → 30045211／SRC-3267 → 25828903／SRC-3270 → 30174462／SRC-3271 → 28426618／SRC-3272 → 30681543／SRC-3273 → 30134424／SRC-3275 → 28937571／SRC-3276 → 28456509／SRC-3277 → 26987420／SRC-3278 → 12464994／SRC-3280 → 39890756／SRC-3281 → 16724884／SRC-3282 → 37486660／SRC-3283 → 25922861／SRC-3284 → 30684460／SRC-3285 → 29939938
- PMCID 補完候補（5件）：SRC-3267 → PMC6505738／SRC-3270 → PMC6109652／SRC-3276 → PMC5446563／SRC-3281 → PMC3109493／SRC-3283 → PMC7050613
- SRC-3274 は日本語学会指針で PMID・PMCID は存在しない。SRC-1020 の PMID（35576513）はマスターに登録済みである。

## 方法メモ

- 主出典のライセンスは、DOI ごとに Crossref の version-of-record 情報と Europe PMC の収載・ライセンス表示を個別に照合した。PMC に全文があってもライセンス表示がなければ自由利用とは扱っていない（Cochrane 2件は PMC ページの著作権表示で RESTRICTED を確定）。
- 裏づけ候補は、PMC 全文 XML または PMC ページで本文を実際に読み、カードの数値・文言と突き合わせて matched／not_confirmed を分けて記録した。候補のライセンスは全文中の CC BY 表示と Europe PMC の license 欄の双方で確認した。
- 使用しなかった候補の例：FIGO の産後出血推奨 2022（CC BY-NC）、Surviving Sepsis Campaign 2021 の ICM 版（WHO の時限許可で CC BY ではない）、ASH 2018 の妊娠 VTE ガイドライン（OA ではない）、Douglas の乳腺炎総説 2022（CC BY-NC）、仏 TOLAC 多施設研究（CC BY-NC）。WOMAN 試験の登録レコード（NCT00872469）は結果未掲載のため根拠に使えない。
- 本バッチの判定は以上で完結しており、カードの主張・数値の変更は一切行っていない。
