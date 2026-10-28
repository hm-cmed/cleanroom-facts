# 腎・泌尿器・生殖器 第19回：月経異常、女性不妊、避妊、更年期（RP-001〜062）

- 作成日：2026-10-28（初版と同日、受け入れ検査の差し戻しに対応して再提出）
- 事実票：60件（RP-001〜062 のうち RP-053・RP-057 を除く）。目標の60〜90件の下限。全件 `status: draft`、`verifier: null`。**既存カードの ID と SRC 番号は初版から一切変えていない。**

## 差し戻しへの対応（何を直したか）

1. **kokushi の付け直し（必須1）**：全カードの `curriculum.kokushi` を、依頼文 §7-1 の表の24項目だけを使って付け直した。番号・項目名・レベルは表の文字どおり。初版にあった表にない番号（「Ⅷ-8-A-⑥（sex differentiation、c）」「Ⅷ-9-A-①（避妊法、a）」など）はすべて消えた。当てはまる項目がないカードは `kokushi: null` にした（14件：RP-001、002、003、005、006、019、020、033、034、035、040、046、047、058）。付け直しの対応は §3 の一覧のとおり。
2. **レベル a の不足分（必須2）**：付け直しにより「月経前症候群（Ⅷ-8-D-①）」は RP-013〜015・018、「避妊（Ⅷ-8-F）」は RP-041〜045・060、「更年期障害（Ⅷ-9-A）」は RP-048〜050・056・059 が対応した。「不育症（Ⅷ-8-E-⑤）」は新規に **RP-061** を作った。あわせて、付け直しで空いた「下垂体性無月経（Ⅷ-8-A-②、レベル b）」にも新規に **RP-062** を作った。新規2件の出典は未使用枠の SRC-856・857 を使った。
3. **コアカリの id の誤り（必須3）**：RP-011・012・016 の TBL-02-09-010 の id を `JlAKpoU` に直した（他のカードにも同じ誤りがないことを確認済み）。
4. **RP-053（骨盤臓器脱）の扱い（確認事項）**：出題基準では Ⅷ-10-C-② で第18回 GY の範囲であり、GY-056 に同じ内容のカードがあるため、**RP-053 は削除した**（欠番として残す）。RP-057（心的外傷への配慮）も第19回の範囲外のため**削除した**（欠番）。RP-056（更年期の心身症）は更年期障害の一部として残し、Ⅷ-9-A を付けた。
5. カードのない仕様項目は、レベル b の2項目だけになった：Ⅷ-9-B-④（動脈硬化）と Ⅷ-9-B-⑤（冠動脈疾患）。RP-055（更年期の脂質・心血管）が内容に触れているが、kokushi は Ⅷ-9-B-③（脂質異常症）を付けた。

## その他の確認結果

- 出典マスター：新規 SRC-811〜870 のうち 44件を使用。未使用は SRC-824、851、853（RP-057 の削除に伴い不使用）、856〜870 のうち 858〜870（番号は詰めていない）。新規2件の出典（SRC-856・857）は、最新の出典マスターと第15〜18回の納品分に DOI・PMID で突き合わせ、重複がないことを確認した。
- 検証（こちらで実施済み）：YAML の構文解析を通過。スキーマ検証は、接頭辞 RP を検証用に加えた条件でエラー0（接頭辞の追加は取り込み側の作業）。`condition.region` は全60件に記載。全カードの kokushi が仕様の24項目のいずれか、または null であることを機械的に確認した。DOI のある出典はすべて Crossref で解決し、DOI・PMID の対応に不一致はなかった（SRC-857 は ID 変換サービスに相互リンクがないが、PubMed のレコードで DOI と PMID の組を確認した）。PMID は全出典で確認できた。DOI が null の出典は4件（いずれも StatPearls の章で、DOI が付与されていないことを確認済み）。
- 取り込み想定：YAML ブロックは1つで、アンカー・マージキー・脚注番号・`basis_tag`・仮IDは使っていない。主張文はすべて自作文である（legal_basis はすべて B）。

## 1. 抽出元ホワイトリスト（出典マスター、新規 SRC）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 使用カード |
|---|---|---|---|---|---|---|---|
| SRC-811 | Jain V, Munro MG, Critchley HOD. Contemporary evaluation of women and girls with abnormal uterine bleeding: FIGO Systems 1 and 2. Int J Gynaecol Obstet. 2023;162 Suppl 2:29-42. | 10.1002/ijgo.14946 | 37538019 | CC BY 4.0（PMC掲載ページの表示） | OPEN | PMC全文ページで書誌・PMID・PMCID・CC BY 4.0表示と、FIGO System 1の定義（周期24〜38日、慢性AUBの定義、旧用語の廃止）を確認 | RP-001, RP-008, RP-010, RP-017 |
| SRC-812 | Mikhael S, Punjala-Patel A, Gavrilova-Jordan L. Hypothalamic-Pituitary-Ovarian Axis Disorders Impacting Female Fertility. Biomedicines. 2019;7(1):5. | 10.3390/biomedicines7010005 | 30621143 | CC BY 4.0（出版社ページ・PMCの表示） | OPEN | PubMedレコードとPMCページで書誌・DOI・PMID・PMCID・CC BY表示を確認。抄録でWHO排卵障害分類（I〜III群）を確認 | RP-002 |
| SRC-813 | Critchley HOD, Maybin JA, Armstrong GM, Williams ARW. Physiology of the Endometrium and Regulation of Menstruation. Physiol Rev. 2020;100(3):1149-1179. | 10.1152/physrev.00031.2019 | 32031903 | ライセンス表示を確認できず | UNKNOWN | PubMedレコードで書誌・DOI・PMIDを確認。抄録でプロゲステロン消退が月経の引き金であること、AUBが生殖年齢女性の4人に1人に影響することを確認。CC表示は確認できなかった | RP-003 |
| SRC-814 | Holesh JE, Bass AN, Lord M. Physiology, Ovulation. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK441996. | null | 28723025 | NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず | UNKNOWN | PubMedレコードで書誌・PMID・Bookshelf IDを確認。同レコードにDOIの記載がないことを確認したためDOIはnull。抄録（抜粋）で排卵が月経の約14日前に起こることを確認 | RP-004 |
| SRC-815 | Lacroix AE, Gondal H, Shumway KR, Langaker MD. Physiology, Menarche. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK470216. | null | 29261991 | NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず | UNKNOWN | NCBI Bookshelfの章ページで著者・本文（初経は通常10〜16歳、平均12.4歳、初期の周期は無排卵が多い）を確認。PMIDは引用文献リストで照合。DOIの記載がないことを確認したためDOIはnull | RP-005 |
| SRC-816 | Nawaz G, Rogol AD, Jenkins SM. Amenorrhea. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK482168. | null | 29489290 | NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず | UNKNOWN | PubMedレコードで書誌・PMID・Bookshelf IDを確認。抜粋で原発性無月経（15歳または乳房発育開始から3年）と続発性無月経（規則的周期で3か月以上、不規則で6か月以上）の定義を確認。DOIの記載がないためDOIはnull | RP-006, RP-007 |
| SRC-817 | Gordon CM, Ackerman KE, Berga SL, Kaplan JR, Mastorakos G, Misra M, Murad MH, Santoro NF, Warren MP. Functional Hypothalamic Amenorrhea: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2017;102(5):1413-1439. | 10.1210/jc.2017-00131 | 28368518 | Endocrine Societyのガイドライン。CC表示を確認できず | UNKNOWN | ガイドライン全文PDFと要約で書誌・DOIを確認し、PMIDは索引情報で照合。初回内分泌評価の検査項目（TSH、遊離T4、プロラクチン、LH、FSH、エストラジオール、AMH）と評価開始の目安（周期45日超の持続、3か月以上の無月経）を確認 | RP-019 |
| SRC-818 | Munro MG, Critchley HOD, Fraser IS; FIGO Menstrual Disorders Committee. The two FIGO systems for normal and abnormal uterine bleeding symptoms and classification of causes of abnormal uterine bleeding in the reproductive years: 2018 revisions. Int J Gynaecol Obstet. 2018;143(3):393-408. | 10.1002/ijgo.12666 | 30198563 | ライセンス表示を確認できず | UNKNOWN | PubMedレコードで書誌・DOI・PMIDを確認。PALM-COEINの構成は同論文を引用する複数の文献と照合。CC表示は確認できなかった | RP-009 |
| SRC-819 | Burnett M, Lemyre M. No. 345-Primary Dysmenorrhea Consensus Guideline. J Obstet Gynaecol Can. 2017;39(7):585-595. | 10.1016/j.jogc.2016.12.023 | 28625286 | カナダ産科婦人科学会（SOGC）ガイドライン。CC表示なし | RESTRICTED | 索引情報と引用文献リストで書誌・DOI・PMIDを照合。2025年に改訂版（Guideline No. 345）が出ていることは別途確認し、本カードは2017年版に基づく旨をuncertaintyに記載 | RP-011 |
| SRC-820 | American College of Obstetricians and Gynecologists. Dysmenorrhea and Endometriosis in the Adolescent. ACOG Committee Opinion No. 760. Obstet Gynecol. 2018;132(6):e249-e258. | 10.1097/AOG.0000000000002978 | 30461694 | ACOG文書（All rights reserved） | RESTRICTED | 抄録全文で、続発性月経困難症の定義、思春期では子宮内膜症が主因であること、治療開始後3〜6か月で改善しなければ続発性原因を検索することを確認。書誌・DOI・PMIDは引用文献リストでも照合 | RP-012 |
| SRC-821 | Yonkers KA, Simoni MK. Premenstrual disorders. Am J Obstet Gynecol. 2018;218(1):68-74. | 10.1016/j.ajog.2017.05.045 | 28571724 | ライセンス表示を確認できず | UNKNOWN | NCBIの文献データベースの掲載情報で書誌・DOI・PMIDを照合。月経前障害の定義（黄体期に出現し月経開始後に消失する症状）については同分野の総説抄録とも整合を確認。CC表示は確認できなかった | RP-013, RP-014, RP-018 |
| SRC-822 | Marjoribanks J, Brown J, O'Brien PMS, Wyatt K. Selective serotonin reuptake inhibitors for premenstrual syndrome. Cochrane Database Syst Rev. 2013;(6):CD001396. | 10.1002/14651858.CD001396.pub3 | 23744611 | Copyright © The Cochrane Collaboration（PMC掲載ページの表示）。CC表示なし | UNKNOWN | PubMedレコードとPMCページで書誌・DOI・PMID・PMCIDを確認。抄録の結論（SSRIは黄体期限定投与・連日投与のいずれでも月経前症状を軽減する。有害作用は用量依存的）を確認。2024年に改訂版（pub4）がある | RP-015 |
| SRC-823 | Brott NR, Le JK. Mittelschmerz. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK549822. | null | 31747229 | NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず | UNKNOWN | PubMedレコードで書誌・PMID・Bookshelf IDを確認。抜粋で排卵痛が生殖年齢女性の40%以上にみられること、周期中日（7〜24日）に起こること、LHピークと一致することを確認。DOIの記載がないためDOIはnull | RP-016 |
| SRC-825 | Broekmans FJ, Soules MR, Fauser BC. Ovarian aging: mechanisms and clinical consequences. Endocr Rev. 2009;30(5):465-493. | 10.1210/er.2009-0006 | 19589949 | ライセンス表示を確認できず | UNKNOWN | PubMedレコードで書誌・DOI・PMIDを確認。抄録で卵胞数の減少が周期の不規則化と月経停止を決めること、AMH低下が胞状卵胞コホートの縮小を最もよく反映することを確認。CC表示は確認できなかった | RP-020 |
| SRC-826 | Teede HJ, Tay CT, Laven J, et al. Recommendations from the 2023 International Evidence-based Guideline for the Assessment and Management of Polycystic Ovary Syndrome. Human Reproduction. 2023;38(9):1655-1679. | 10.1093/humrep/dead156 | 37580037 | CC BY-NC 4.0 | RESTRICTED | Crossref と PMC 本文（PMC10477934）で書誌・ライセンス・診断基準と治療推奨を確認 | RP-022, RP-023 |
| SRC-827 | Panay N, Anderson RA, Bennie A, et al. Evidence-based guideline: premature ovarian insufficiency. Human Reproduction Open. 2024;2024(4):hoae065. | 10.1093/hropen/hoae065 | 39660328 | CC BY 4.0 | OPEN | Crossref と PMC 本文（PMC11631070）で書誌・ライセンス・診断基準（FSH 25 IU/L超）・有病率を確認 | RP-024 |
| SRC-828 | Melmed S, Casanueva FF, Hoffman AR, et al. Diagnosis and Treatment of Hyperprolactinemia: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2011;96(2):273-288. | 10.1210/jc.2010-1692 | 21296991 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID を照合。推奨文（ドパミン作動薬の第一選択治療、カベルゴリンの優先）はガイドライン本文の該当節で確認 | RP-025 |
| SRC-829 | Practice Committee of the American Society for Reproductive Medicine. Diagnosis and treatment of luteal phase deficiency: a committee opinion. Fertility and Sterility. 2021;115(6):1416-1423. | 10.1016/j.fertnstert.2021.02.010 | 33827766 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID・抄録（黄体期10日以下の定義、原因としての証明なし）を確認 | RP-026 |
| SRC-830 | Practice Committee of the American Society for Reproductive Medicine. Diagnostic evaluation of the infertile female: a committee opinion. Fertility and Sterility. 2015;103(6):e44-e50. | 10.1016/j.fertnstert.2015.03.019 | 25936238 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID・抄録を確認。評価開始時期（12か月、35歳以上は6か月）は同学会の委員会意見の結論部で確認 | RP-028, RP-030, RP-038, RP-039 |
| SRC-831 | Practice Committee of the American Society for Reproductive Medicine. Role of tubal surgery in the era of assisted reproductive technology: a committee opinion. Fertility and Sterility. 2021;115(5):1143-1150. | 10.1016/j.fertnstert.2021.01.051 | 33642065 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID・抄録を確認。結論部（卵管造影が第一選択、留水症への卵管切除等で IVF 妊娠率改善）は本文の結論で確認 | RP-029 |
| SRC-832 | Ovarian Stimulation TEGGO, Bosch E, Broer S, et al. ESHRE guideline: ovarian stimulation for IVF/ICSI. Human Reproduction Open. 2020;2020(2):hoaa009. | 10.1093/hropen/hoaa009 | 32395637 | CC BY-NC 4.0 | RESTRICTED | Crossref と Europe PMC で DOI・PMID・ライセンス・抄録（AFC/AMH の強い推奨、アンタゴニスト法の強い推奨）を確認 | RP-031 |
| SRC-833 | Ethics Committee of the American Society for Reproductive Medicine. Planned oocyte cryopreservation for women seeking to preserve future reproductive potential: an Ethics Committee opinion. Fertility and Sterility. 2018;110(6):1022-1028. | 10.1016/j.fertnstert.2018.08.027 | 30396539 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID・抄録（倫理的に許容されうること、不確実性の説明の必要性）を確認 | RP-032 |
| SRC-834 | Todd CS, Lorenzetti L, Mussa A, et al. Drug-drug interactions between antiretrovirals and hormonal contraception: an updated systematic review. Contraception. 2024;138:110490. | 10.1016/j.contraception.2024.110490 | 38762199 | CC BY 4.0 | OPEN | Crossref（ライセンス CC BY 4.0 を含む）と Europe PMC で DOI・PMID・抄録（エファビレンツとの相互作用）を確認 | RP-034 |
| SRC-835 | Kuhl H. Pharmacology of estrogens and progestogens: influence of different routes of administration. Climacteric. 2005;8(Suppl 1):3-63. | 10.1080/13697130500148875 | 16112947 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID・抄録（エストロゲン・プロゲスチンの薬理と投与経路の影響）を確認 | RP-033 |
| SRC-836 | Bofill Rodriguez M, Lethaby A, Grigore M, et al. Endometrial resection and ablation techniques for heavy menstrual bleeding. Cochrane Database of Systematic Reviews. 2019;(1):CD001501. | 10.1002/14651858.CD001501.pub5 | 30667064 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID を照合し、抄録の主要結果（第2世代と第1世代の効果同等、28試験4287人）を確認 | RP-035 |
| SRC-837 | Hughes IA. Disorders of sex development: a new definition and classification. Best Practice & Research Clinical Endocrinology & Metabolism. 2008;22(1):119-134. | 10.1016/j.beem.2007.11.001 | 18279784 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID・抄録（DSD の定義と核型による分類）を確認 | RP-036 |
| SRC-838 | Balen AH, Morley LC, Misso M, et al. The management of anovulatory infertility in women with polycystic ovary syndrome: an analysis of the evidence to support the development of global WHO guidance. Human Reproduction Update. 2016;22(6):687-708. | 10.1093/humupd/dmw025 | 27511809 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID・抄録（無排卵性不妊の約80%が PCOS、段階的治療）を確認 | RP-021, RP-027 |
| SRC-839 | Legro RS, Brzyski RG, Diamond MP, et al. Letrozole versus clomiphene for infertility in the polycystic ovary syndrome. New England Journal of Medicine. 2014;371(2):119-129. | 10.1056/NEJMoa1313517 | 25006718 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID・抄録（出生率27.5%対19.1%、排卵率61.7%対48.3%）を確認 | RP-037 |
| SRC-840 | Krassas GE, Poppe K, Glinoer D. Thyroid function and human reproductive health. Endocrine Reviews. 2010;31(5):702-755. | 10.1210/er.2009-0041 | 20573783 | 未確認 | UNKNOWN | Crossref と Europe PMC で DOI・PMID・抄録（甲状腺中毒症では過少・頻発月経、機能低下症では希発月経）を確認 | RP-040 |
| SRC-841 | Trussell J. Contraceptive failure in the United States. Contraception. 2011;83(5):397-404. | 10.1016/j.contraception.2011.01.021 | 21477680 | 出版社ページ・Crossref に CC ライセンスの表示なし（PMC 収載は著者原稿） | UNKNOWN | Crossref と PubMed で DOI・PMID・PMCID を照合し、抄録で完全使用と典型使用の区別を確認 | RP-041、RP-045 |
| SRC-842 | Brynhildsen J. Combined hormonal contraceptives: prescribing patterns, compliance, and benefits versus risks. Therapeutic Advances in Drug Safety. 2014;5(5):201-213. | 10.1177/2042098614548857 | 25360241 | PMC ページで CC ライセンスの版を確認できず | UNKNOWN | Crossref と PubMed で DOI・PMID・PMCID を照合し、抄録で利益（卵巣癌・子宮内膜癌・大腸癌リスク低下、過多月経・月経困難症への効果）とリスク（静脈血栓塞栓症等）を確認 | RP-042 |
| SRC-843 | American College of Obstetricians and Gynecologists. Practice Bulletin No. 186: Long-Acting Reversible Contraception: Implants and Intrauterine Devices. Obstetrics & Gynecology. 2017;130(5):e251-e269. | 10.1097/AOG.0000000000002400 | 29064972 | 学会刊行物で CC ライセンスの表示なし | UNKNOWN | Crossref と PubMed で DOI・PMID を照合し、抄録で LARC が最も有効な可逆的避妊法であることと除去後の妊孕性回復を確認 | RP-043 |
| SRC-844 | American College of Obstetricians and Gynecologists. Practice Bulletin No. 152: Emergency Contraception. Obstetrics & Gynecology. 2015;126(3):e1-e11. | 10.1097/AOG.0000000000001047 | 26287787 | 学会刊行物で CC ライセンスの表示なし | UNKNOWN | Crossref と PubMed で DOI・PMID を照合し、抄録で緊急避妊の方法（経口製剤と銅付加 IUD）を確認 | RP-044 |
| SRC-845 | Harlow SD, Gass M, Hall JE, et al. Executive summary of the Stages of Reproductive Aging Workshop + 10: addressing the unfinished agenda of staging reproductive aging. Menopause. 2012;19(4):387-395. | 10.1097/gme.0b013e31824d8f40 | 22343510 | PMC 収載は著者原稿で CC ライセンスの表示なし | UNKNOWN | Crossref と PubMed で DOI・PMID・PMCID を照合し、PMC 本文で閉経の判定（最終月経後12か月）と後期移行期の基準（60日以上の無月経）を確認 | RP-046、RP-047、RP-058 |
| SRC-846 | Santoro N, Epperson CN, Mathews SB. Menopausal Symptoms and Their Management. Endocrinology and Metabolism Clinics of North America. 2015;44(3):497-515. | 10.1016/j.ecl.2015.05.001 | 26316239 | 出版社ページ・Crossref に CC ライセンスの表示なし（PMC 収載は著者原稿） | UNKNOWN | Crossref と PubMed で DOI・PMID・PMCID を照合し、抄録で血管運動症状・腟乾燥・睡眠障害・気分変化の位置づけを確認 | RP-048 |
| SRC-847 | The North American Menopause Society. The 2022 hormone therapy position statement of The North American Menopause Society. Menopause. 2022;29(7):767-794. | 10.1097/GME.0000000000002028 | 35797481 | 学会誌掲載で CC ライセンスの表示なし | UNKNOWN | Crossref と PubMed で DOI・PMID を照合し、抄録で HRT の位置づけ（血管運動症状・GSM への有効性、開始時期による利益・リスク比の違い）を確認 | RP-049、RP-050、RP-055 |
| SRC-848 | Rossouw JE, Anderson GL, Prentice RL, et al. Risks and Benefits of Estrogen Plus Progestin in Healthy Postmenopausal Women: Principal Results From the Women's Health Initiative Randomized Controlled Trial. JAMA. 2002;288(3):321-333. | 10.1001/jama.288.3.321 | 12117397 | 出版社ページ・Crossref に CC ライセンスの表示なし | UNKNOWN | Crossref と PubMed で DOI・PMID を照合し、抄録でハザード比と1万人・年あたりの絶対リスク差を確認 | RP-050 |
| SRC-849 | Eastell R, Rosen CJ, Black DM, et al. Pharmacological Management of Osteoporosis in Postmenopausal Women: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2019;104(5):1595-1622. | 10.1210/jc.2019-00221 | 30907953 | 学会ガイドラインで CC ライセンスの表示なし | UNKNOWN | Crossref と PubMed で DOI・PMID を照合し、抄録で骨折リスク評価に基づく治療判断と栄養・生活習慣・転倒予防の併用という原則を確認 | RP-051、RP-052 |
| SRC-850 | The North American Menopause Society. The 2020 genitourinary syndrome of menopause position statement of The North American Menopause Society. Menopause. 2020;27(9):976-992. | 10.1097/GME.0000000000001609 | 32852449 | 学会誌掲載で CC ライセンスの表示なし | UNKNOWN | Crossref と PubMed で DOI・PMID を照合し、抄録で有病割合（27〜84%）と治療の段階（潤滑剤・保湿剤から低用量腟エストロゲン等）を確認 | RP-054 |
| SRC-852 | Maki PM, Kornstein SG, Joffe H, et al. Guidelines for the evaluation and treatment of perimenopausal depression: summary and recommendations. Menopause. 2018;25(10):1069-1085. | 10.1097/GME.0000000000001174 | 30179986 | 学会誌掲載で CC ライセンスの表示なし | UNKNOWN | Crossref と PubMed で DOI・PMID を照合し、抄録で閉経移行期がうつ病の脆弱期であることと抗うつ薬・精神療法が第一選択であることを確認 | RP-056 |
| SRC-854 | The North American Menopause Society. The 2023 nonhormone therapy position statement of The North American Menopause Society. Menopause. 2023;30(6):573-590. | 10.1097/GME.0000000000002200 | 37252752 | 学会誌掲載で CC ライセンスの表示なし | UNKNOWN | Crossref と PubMed で DOI・PMID を照合し、抄録で推奨される非ホルモン療法（認知行動療法、SSRI/SNRI、ガバペンチン、フェゾリネタント等）を確認 | RP-059 |
| SRC-855 | Yoshida H, Sakamoto H, Leslie A, Takahashi O, Tsuboi S, Kitamura K. Contraception in Japan: Current trends. Contraception. 2016;93(6):475-477. | 10.1016/j.contraception.2016.02.006 | 26872717 | 出版社ページ・Crossref に CC ライセンスの表示なし | UNKNOWN | Crossref と PubMed で DOI・PMID を照合し、抄録で2014年のコンドーム使用83.4%・経口避妊薬使用3.0%を確認 | RP-060 |
| SRC-856 | ESHRE Guideline Group on RPL; Bender Atik R, Christiansen OB, Elson J, et al. ESHRE guideline: recurrent pregnancy loss: an update in 2022. Human Reproduction Open. 2023;2023(1):hoad002. | 10.1093/hropen/hoad002 | 36873081 | CC BY-NC 4.0 | RESTRICTED | Crossref で書誌とライセンス（CC BY-NC 4.0）を照合し、NCBI の ID 変換で PMID・PMCID を照合。PMC 本文で定義（2回以上の妊娠喪失、異所性妊娠・胞状奇胎を除く、カップルの約1〜2%）、検査項目の範囲（遺伝的要因・血栓性素因・代謝内分泌異常のスクリーニング、腺筋症除外のための2D超音波の追加）と治療の推奨（甲状腺機能正常かつ甲状腺抗体陽性の女性へのレボチロキシン投与は行わない、腟プロゲステロンの条件付き推奨、年齢と妊娠歴に基づく予後推定）を確認 | RP-061 |
| SRC-857 | Fleseriu M, Hashim IA, Karavitaki N, et al. Hormonal Replacement in Hypopituitarism in Adults: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2016;101(11):3888-3921. | 10.1210/jc.2016-2118 | 27736313 | ライセンス表示を確認できず（著者稿は All rights reserved） | UNKNOWN | Crossref で書誌を照合し、PubMed で DOI から PMID を照合。ガイドラインの推奨文で、希発月経・無月経におけるエストラジオール・FSH・LH の測定（推奨1.14）、GnRH 負荷試験は有用な情報をもたらさないこと（1.15）、閉経後女性では FSH・LH の高値がないことがゴナドトロープ機能障害の診断根拠になること（1.16）、中枢性甲状腺機能低下の評価は遊離T4とTSHによること（1.6）を確認 | RP-062 |

## 2. 事実票 YAML

```yaml
- id: RP-001
  domain: RP
  subdomain: 月経異常の分類と評価（総論）
  assertion:
    plain_statement_ja: "月経異常（異常子宮出血）は、FIGOのSystem 1で頻度・持続期間・規則性・出血量の4つのパラメータで記述する。正常周期は24〜38日で、出血期間は8日以内が正常範囲とされる。慢性の異常子宮出血は、出血量・規則性・タイミングのいずれかが異常な状態が過去6か月の大半にわたって存在することと定義される。原因の分類にはFIGO System 2（PALM-COEIN）を用い、まず妊娠を除外し、鉄欠乏と貧血の有無を出血の評価と並行して調べる。"
    condition:
      region: 国際
      study: FIGO分類に基づく総説（2023年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-811
    source: "Jain V, Munro MG, Critchley HOD. Contemporary evaluation of women and girls with abnormal uterine bleeding: FIGO Systems 1 and 2. Int J Gynaecol Obstet. 2023;162 Suppl 2:29-42."
    doi: 10.1002/ijgo.14946
    pmid: "37538019"
    pmcid: PMC10952771
    url: https://doi.org/10.1002/ijgo.14946
    source_license: CC BY 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "FIGOの定義は国際的な合意に基づくものであり、日本の診療で用いられる月経異常の定義（日本産科婦人科学会の用語集など）と細部が異なる可能性がある。日本の定義との対応は本調査では未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-021 (id: JlAKppQ)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-002
  domain: RP
  subdomain: 視床下部・下垂体・卵巣系の調節
  assertion:
    plain_statement_ja: "視床下部・下垂体・卵巣（HPO）系は、視床下部のGnRHパルス分泌、下垂体のLH・FSH分泌、卵巣の性ステロイドとインヒビンによるフィードバックで構成される緊密に調節された系であり、排卵と月経周期を制御する。この系の機能障害による排卵障害はWHOにより3群に分類される。第I群は視床下部性（性腺刺激ホルモン低下性）の障害、第II群は性腺機能が保たれた状態での内分泌異常に伴うもの（多嚢胞性卵巣症候群など）、第III群は卵巣機能の枯渇によるもの（性腺刺激ホルモン上昇性）である。"
    condition:
      region: 国際
      study: 総説（2019年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-812
    source: "Mikhael S, Punjala-Patel A, Gavrilova-Jordan L. Hypothalamic-Pituitary-Ovarian Axis Disorders Impacting Female Fertility. Biomedicines. 2019;7(1):5."
    doi: 10.3390/biomedicines7010005
    pmid: "30621143"
    pmcid: PMC6466056
    url: https://doi.org/10.3390/biomedicines7010005
    source_license: CC BY 4.0（出版社ページ・PMCの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "WHOの排卵障害分類は不妊診療の文脈で用いられる分類であり、月経異常の原因分類（PALM-COEINのAUB-Oなど）とは目的が異なる。GnRHパルス頻度の具体的な数値は出典の抄録では確認できなかったため主張に含めていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-003
  domain: RP
  subdomain: 子宮内膜の周期性変化
  assertion:
    plain_statement_ja: "子宮内膜は、卵胞期のエストロゲン作用による増殖、黄体期のプロゲステロン作用による分泌期変化と脱落膜化を周期的に繰り返す。妊娠が成立しなければ黄体が退縮し、プロゲステロンの消退が月経の引き金となり、機能層が剥離する。剥離した内膜は速やかに修復され、瘢痕を残さない。月経と内膜修復の過程は、炎症と組織修復の生体内モデルでもある。異常子宮出血は生殖年齢女性の4人に1人に影響するとされる。"
    condition:
      region: 国際
      study: 総説（2020年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-813
    source: "Critchley HOD, Maybin JA, Armstrong GM, Williams ARW. Physiology of the Endometrium and Regulation of Menstruation. Physiol Rev. 2020;100(3):1149-1179."
    doi: 10.1152/physrev.00031.2019
    pmid: "32031903"
    pmcid: null
    url: https://doi.org/10.1152/physrev.00031.2019
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "「4人に1人」は出典の抄録に記載された異常子宮出血の影響範囲の概数であり、定義や調査集団により変動する。内膜の厚さなどの具体的数値は出典の抄録では確認できなかったため主張に含めていない。ライセンス表示は出版社ページで確認できなかった。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-004
  domain: RP
  subdomain: 排卵の機序
  assertion:
    plain_statement_ja: "排卵は、卵巣の主席卵胞が破裂して卵子を腹腔内に放出する過程であり、卵管の采部に取り込まれる。卵胞期にエストロゲンが上昇し、周期中期に下垂体からのLHサージ（とFSHの上昇）が起こることが排卵の引き金となる。排卵は月経周期の長さにかかわらず、次回月経の約14日前に起こり、その後に黄体期が続く。排卵後の卵胞は黄体となり、プロゲステロンを分泌する。"
    condition:
      region: 米国
      study: 教科書章（StatPearls）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-814
    source: "Holesh JE, Bass AN, Lord M. Physiology, Ovulation. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK441996."
    doi: null
    pmid: "28723025"
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/28723025/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "StatPearlsの章にはDOIが付与されておらず、PubMedレコードにもDOIの記載がないことを確認したためDOIはnullとした。LHサージ開始から排卵までの時間などの詳細な数値は、確認した抜粋の範囲に含まれなかったため主張に含めていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-021 (id: JlAKppQ)"
    kokushi: 医学各論 Ⅷ-8-D-③（無排卵、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-005
  domain: RP
  subdomain: 思春期と初経
  assertion:
    plain_statement_ja: "初経は思春期の後半に起こる最初の月経であり、通常10〜16歳の間に発来し、平均年齢は12.4歳とされる。初経の時期は遺伝、栄養状態、全身の健康状態、運動などの影響を受ける。初経直後の周期は、視床下部・下垂体・卵巣系のエストロゲン陽性フィードバックが未熟なため、無排卵で周期の長さや出血量が不規則であることが多い。二次性徴の進行と並行して、やがて排卵周期が確立する。"
    condition:
      region: 米国
      study: 教科書章（StatPearls）。平均初経年齢は米国のデータに基づく記述
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-815
    source: "Lacroix AE, Gondal H, Shumway KR, Langaker MD. Physiology, Menarche. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK470216."
    doi: null
    pmid: "29261991"
    pmcid: null
    url: https://www.ncbi.nlm.nih.gov/books/NBK470216/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "平均初経年齢12.4歳は米国のデータに基づく教科書的記述であり、日本人集団の平均値ではない。日本の初経年齢の平均は本調査では未確認である。StatPearlsの章にはDOIの記載がないためDOIはnullとした。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-006
  domain: RP
  subdomain: 原発性無月経
  assertion:
    plain_statement_ja: "原発性無月経は、15歳までに月経の発来がない場合、または乳房発育の開始から3年を経ても月経がない場合に評価の対象となる。乳房発育がなく13歳で月経がない場合は、思春期遅発の観点からより早期の評価が勧められる。主な原因は、染色体異常に伴う卵巣機能不全（ターナー症候群など）と、ミュラー管の形成異常などの解剖学的異常である。評価では妊娠の除外に加え、LH、FSH、プロラクチン、TSHなどの血清ホルモンと骨盤の解剖の確認を系統的に行う。"
    condition:
      region: 米国
      study: 教科書章（StatPearls）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-816
    source: "Nawaz G, Rogol AD, Jenkins SM. Amenorrhea. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK482168."
    doi: null
    pmid: "29489290"
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/29489290/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "評価開始年齢の基準は米国の教科書的基準であり、日本の診療指針における基準との一致は本調査では未確認である。StatPearlsの章にはDOIの記載がないためDOIはnullとした。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-021 (id: JlAKppQ)；TBL-02-09-022 (id: JlAKppU)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-007
  domain: RP
  subdomain: 続発性無月経
  assertion:
    plain_statement_ja: "続発性無月経は、それまで規則的だった月経が3か月以上停止した場合、または不規則だった月経が6か月以上停止した場合をいう。原因の多くは、多嚢胞性卵巣症候群、視床下部性無月経、高プロラクチン血症、卵巣機能不全で説明できる。評価ではまず妊娠を除外し、血清LH、FSH、プロラクチン、TSHを測定する。視床下部性無月経の患者では摂食障害の有無を評価し、骨密度低下のリスクに注意する。"
    condition:
      region: 米国
      study: 教科書章（StatPearls）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-816
    source: "Nawaz G, Rogol AD, Jenkins SM. Amenorrhea. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK482168."
    doi: null
    pmid: "29489290"
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/29489290/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "無月経の期間の定義は出典（米国の教科書）のものであり、日本の定義との細部の一致は未確認である。各原因の頻度の順位は集団によって異なる可能性がある。StatPearlsの章にはDOIの記載がないためDOIはnullとした。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU)"
    kokushi: 医学各論 Ⅷ-8-A-①（視床下部性無月経、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-008
  domain: RP
  subdomain: 月経周期異常（頻発・希発月経）
  assertion:
    plain_statement_ja: "FIGOの定義では、正常の月経周期（頻度）は24〜38日である。周期が24日未満の場合を頻発月経、38日を超える場合を希発月経といい、いずれも異常子宮出血の頻度の異常として扱う。また、連続する周期の長さのばらつきが大きい場合は規則性の異常として評価する。頻度や規則性の異常は排卵障害（AUB-O）を反映することが多く、思春期と閉経移行期には生理的にも起こりやすい。"
    condition:
      region: 国際
      study: FIGO分類に基づく総説（2023年）。閾値はFIGO System 1の定義表から読み取り
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-811
    source: "Jain V, Munro MG, Critchley HOD. Contemporary evaluation of women and girls with abnormal uterine bleeding: FIGO Systems 1 and 2. Int J Gynaecol Obstet. 2023;162 Suppl 2:29-42."
    doi: 10.1002/ijgo.14946
    pmid: "37538019"
    pmcid: PMC10952771
    url: https://doi.org/10.1002/ijgo.14946
    source_license: CC BY 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "周期の閾値（24日・38日）はFIGO System 1の定義表から読み取った値である。従来日本で用いられてきた頻発月経・希発月経の定義（周期25〜38日を正常とする等）とは境界が異なる可能性があり、日本の定義との対応は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-021 (id: JlAKppQ)"
    kokushi: 医学各論 Ⅷ-8-B-①（希発月経、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-009
  domain: RP
  subdomain: 過多月経と異常子宮出血の分類（PALM-COEIN）
  assertion:
    plain_statement_ja: "過多月経は、患者の身体面・社会面・情緒面・経済面の生活の質を損なう過剰な月経血喪失と定義される。生殖年齢の非妊娠女性における異常子宮出血の原因は、FIGOのPALM-COEIN分類で整理される。PALMは画像や病理で確認できる構造的原因（ポリープ、子宮腺筋症、子宮筋腫、悪性腫瘍と子宮内膜増殖症）、COEINは非構造的原因（凝固障害、排卵障害、子宮内膜性、医原性、その他未分類）であり、複数の原因が併存することもある。"
    condition:
      region: 国際
      study: FIGO分類の2018年改訂文書
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-818
    source: "Munro MG, Critchley HOD, Fraser IS; FIGO Menstrual Disorders Committee. The two FIGO systems for normal and abnormal uterine bleeding symptoms and classification of causes of abnormal uterine bleeding in the reproductive years: 2018 revisions. Int J Gynaecol Obstet. 2018;143(3):393-408."
    doi: 10.1002/ijgo.12666
    pmid: "30198563"
    pmcid: null
    url: https://doi.org/10.1002/ijgo.12666
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "過多月経の定義は患者の生活の質への影響に基づくものであり、客観的な出血量（従来の80mL超など）の基準とは異なる。PALM-COEINの各項目の詳細な下位分類は本カードでは扱っていない。出典のライセンス表示は確認できなかった。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-016 (id: JlAKpo4)；TBL-02-09-021 (id: JlAKppQ)"
    kokushi: 医学各論 Ⅷ-8-B-②（過多月経、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-010
  domain: RP
  subdomain: 過少月経
  assertion:
    plain_statement_ja: "過少月経は、月経血量が通常より少ない状態であり、FIGO System 1では出血量は患者本人の感じ方に基づいて多い・正常・少ないと記述される。出血量の減少は、ホルモン避妊法の使用、子宮内の癒着、甲状腺機能異常や高プロラクチン血症などの内分泌異常、卵巣機能の低下など様々な原因で起こりうるため、出血量の異常として頻度・規則性・持続期間と併せて評価する。妊娠可能な年齢では、月経様出血の減少や消失に際して妊娠の可能性も考慮する。"
    condition:
      region: 国際
      study: FIGO分類に基づく総説（2023年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-811
    source: "Jain V, Munro MG, Critchley HOD. Contemporary evaluation of women and girls with abnormal uterine bleeding: FIGO Systems 1 and 2. Int J Gynaecol Obstet. 2023;162 Suppl 2:29-42."
    doi: 10.1002/ijgo.14946
    pmid: "37538019"
    pmcid: PMC10952771
    url: https://doi.org/10.1002/ijgo.14946
    source_license: CC BY 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "FIGOの枠組みでは出血量は主観的評価に基づくため、過少月経に客観的な出血量の閾値は設定されていない。原因として挙げた項目は異常子宮出血全般の原因分類に基づく一般論であり、過少月経に特化した疫学的頻度は出典では確認できなかった。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-021 (id: JlAKppQ)"
    kokushi: 医学各論 Ⅷ-8-B-③（過少月経、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-011
  domain: RP
  subdomain: 原発性月経困難症
  assertion:
    plain_statement_ja: "原発性月経困難症は、骨盤内に痛みの原因となる病変がないにもかかわらず起こる月経痛であり、排卵周期の確立とともにみられるようになる。月経時の子宮内膜でのプロスタグランジン産生の増加が子宮の過剰な収縮と虚血を引き起こし、痛みを生じると説明される。治療の第一選択はNSAIDsであり、避妊を兼ねる場合やNSAIDsで不十分な場合にはホルモン療法（経口避妊薬など）が用いられる。治療で改善しない場合は、器質性（続発性）の原因を検索する。"
    condition:
      region: カナダ
      study: 学会コンセンサスガイドライン（2017年版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-819
    source: "Burnett M, Lemyre M. No. 345-Primary Dysmenorrhea Consensus Guideline. J Obstet Gynaecol Can. 2017;39(7):585-595."
    doi: 10.1016/j.jogc.2016.12.023
    pmid: "28625286"
    pmcid: null
    url: https://doi.org/10.1016/j.jogc.2016.12.023
    source_license: カナダ産科婦人科学会（SOGC）ガイドライン。CC表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "本カードは2017年版ガイドラインに基づいており、2025年に改訂版が公表されている。推奨の細部は改訂版で変わっている可能性がある。NSAIDsと経口避妊薬（低用量エストロゲン・プロゲスチン配合薬）については、日本での月経困難症に対する承認・保険適用の状況を本調査では個別に確認していない（一般に保険適用があることは知られているが、製剤ごとの適応は未確認）。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-010 (id: JlAKpoU)"
    kokushi: 医学各論 Ⅷ-8-C-①（機能性月経困難症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-012
  domain: RP
  subdomain: 器質性月経困難症
  assertion:
    plain_statement_ja: "続発性（器質性）月経困難症は、子宮内膜症、子宮腺筋症、子宮筋腫、骨盤内炎症などの骨盤病変や医学的疾患によって生じる月経痛である。思春期では子宮内膜症が続発性月経困難症の主な原因とされる。月経困難症の治療を開始して3〜6か月以内に臨床的な改善が得られない場合は、治療の遵守状況の確認とともに、続発性の原因を検索すべきである。特に、ホルモン療法とNSAIDsで改善しない持続的な月経痛では子宮内膜症を考慮する。"
    condition:
      region: 米国
      study: 学会委員会意見（2018年）。対象は主として思春期
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-820
    source: "American College of Obstetricians and Gynecologists. Dysmenorrhea and Endometriosis in the Adolescent. ACOG Committee Opinion No. 760. Obstet Gynecol. 2018;132(6):e249-e258."
    doi: 10.1097/AOG.0000000000002978
    pmid: "30461694"
    pmcid: null
    url: https://doi.org/10.1097/AOG.0000000000002978
    source_license: ACOG文書（All rights reserved）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "出典は思春期を対象とした委員会意見であり、「子宮内膜症が主因」「3〜6か月で改善しなければ検索」という記述は思春期の文脈のものである。成人における続発性月経困難症の原因頻度は異なる可能性がある。本文中で言及されるホルモン療法薬・NSAIDsの日本での承認・保険適用の状況は、製剤ごとに本調査では未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-010 (id: JlAKpoU)"
    kokushi: 医学各論 Ⅷ-8-C-②（器質性月経困難症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-013
  domain: RP
  subdomain: 月経前症候群（PMS）の診断
  assertion:
    plain_statement_ja: "月経前症候群（PMS）は、黄体期（月経前の約2週間）に出現し、月経開始後まもなく消失する身体症状と精神症状の組み合わせによって、日常生活や社会生活に支障をきたす状態である。症状が周期的に現れることを確認するために、患者自身による前向きな症状記録（日誌）が診断に有用である。月経前障害は生殖年齢女性の最大で約12%に影響するとの報告があり、他の精神疾患や身体疾患との鑑別には症状の周期的パターンの確認が重要である。"
    condition:
      region: 米国
      study: 総説（2018年）。有病割合は総説で引用された報告に基づく
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-821
    source: "Yonkers KA, Simoni MK. Premenstrual disorders. Am J Obstet Gynecol. 2018;218(1):68-74."
    doi: 10.1016/j.ajog.2017.05.045
    pmid: "28571724"
    pmcid: null
    url: https://doi.org/10.1016/j.ajog.2017.05.045
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "有病割合（最大約12%）は同分野の総説抄録で示された値であり、定義や集団によって大きく変動する。日本の診断基準（日本産科婦人科学会の定義）との細部の対応は本調査では未確認である。出典のライセンス表示は確認できなかった。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-D-①（月経前症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-014
  domain: RP
  subdomain: 月経前不快気分障害（PMDD）
  assertion:
    plain_statement_ja: "月経前不快気分障害（PMDD）は月経前症候群の重症型であり、抑うつ気分、易怒性、情緒不安定などの精神症状が主体で、社会的・職業的機能に著しい障害をもたらす。症状は黄体期に出現し、月経開始後1週間以内に軽快することが特徴で、DSM-5では抑うつ障害群の一つとして位置づけられている。診断には、少なくとも2周期にわたる前向きな毎日の症状評価による周期的パターンの確認が求められる。"
    condition:
      region: 米国
      study: 総説（2018年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-821
    source: "Yonkers KA, Simoni MK. Premenstrual disorders. Am J Obstet Gynecol. 2018;218(1):68-74."
    doi: 10.1016/j.ajog.2017.05.045
    pmid: "28571724"
    pmcid: null
    url: https://doi.org/10.1016/j.ajog.2017.05.045
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "DSM-5の診断基準の項目数などの詳細は出典の書誌確認の範囲では逐一照合していないため、主張は基準の骨格にとどめた。日本の診療ではICD-10等との使い分けがあり、国内での診断運用の詳細は未確認である。出典のライセンス表示は確認できなかった。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-D-①（月経前症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-015
  domain: RP
  subdomain: PMS・PMDDの治療
  assertion:
    plain_statement_ja: "月経前症候群の薬物治療では、選択的セロトニン再取り込み阻害薬（SSRI）が第一選択の一つであり、黄体期のみの間欠投与でも連日投与でも月経前症状の軽減に有効であることが、ランダム化比較試験のシステマティックレビューで示されている。有害作用は比較的頻度が高く、悪心と無力感が多く、用量依存的に増える。経口避妊薬やカルシウム補充も選択肢となりうるが、治療は症状と機能障害の程度に応じて個別化する。"
    condition:
      region: 国際
      study: コクラン・システマティックレビュー（2013年版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-822
    source: "Marjoribanks J, Brown J, O'Brien PMS, Wyatt K. Selective serotonin reuptake inhibitors for premenstrual syndrome. Cochrane Database Syst Rev. 2013;(6):CD001396."
    doi: 10.1002/14651858.CD001396.pub3
    pmid: "23744611"
    pmcid: PMC7073417
    url: https://doi.org/10.1002/14651858.CD001396.pub3
    source_license: Copyright © The Cochrane Collaboration（PMC掲載ページの表示）。CC表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "本レビューには2024年の改訂版（CD001396.pub4）が存在し、結論が更新されている可能性がある。SSRI各製剤について、日本では月経前症候群・月経前不快気分障害への適応承認がない製剤もあり、国内の承認・保険適用の状況は製剤ごとに未確認である（適応外使用となる場合がある点に注意）。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-D-①（月経前症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-016
  domain: RP
  subdomain: 排卵痛・排卵期出血
  assertion:
    plain_statement_ja: "排卵痛（Mittelschmerz）は、排卵期に起こる良性の片側性の下腹部痛であり、周期の中間期（周期7〜24日）に、発育する卵胞のある側に生じる。血中LHピークの時期と一致して起こり、生殖年齢女性の40%以上にみられるとされる。通常は治療を要さず、痛みが強い場合は鎮痛薬で対処する。下腹部痛の訴えでは、虫垂炎や卵巣嚢胞の破裂・茎捻転、異所性妊娠などの他の原因との鑑別が重要である。排卵期には少量の性器出血（排卵期出血）を伴うこともある。"
    condition:
      region: 米国
      study: 教科書章（StatPearls）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-823
    source: "Brott NR, Le JK. Mittelschmerz. In: StatPearls. Treasure Island (FL): StatPearls Publishing; Bookshelf ID: NBK549822."
    doi: null
    pmid: "31747229"
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/31747229/
    source_license: NCBI Bookshelf収載。章ページのライセンス表示はアクセス制限のため確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "「40%以上」という頻度と発生日（7〜24日）は出典の抜粋に記載された値である。排卵期出血そのものの頻度や機序は出典の抜粋では確認できなかったため、主張では定性的に触れるにとどめた。StatPearlsの章にはDOIの記載がないためDOIはnullとした。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-010 (id: JlAKpoU)"
    kokushi: 医学各論 Ⅷ-8-D-②（機能性子宮出血、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-017
  domain: RP
  subdomain: 漏出性出血・機能性子宮出血
  assertion:
    plain_statement_ja: "月経周期の途中に出る出血は月経間期出血として記述され、排卵期の少量の出血のほか、ホルモン避妊法の使用中に起こる予定外の出血（破綻出血）も含まれる。かつて器質的原因のない子宮出血を指して用いられた「機能性子宮出血」という用語は、FIGOの分類体系では廃止され、menorrhagiaやmetrorrhagiaなどの旧用語とともに使わないこととされた。原因はPALM-COEIN分類に沿って、凝固障害・排卵障害・子宮内膜性などのカテゴリーで具体的に示すのが現在の標準である。"
    condition:
      region: 国際
      study: FIGO分類に基づく総説（2023年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-811
    source: "Jain V, Munro MG, Critchley HOD. Contemporary evaluation of women and girls with abnormal uterine bleeding: FIGO Systems 1 and 2. Int J Gynaecol Obstet. 2023;162 Suppl 2:29-42."
    doi: 10.1002/ijgo.14946
    pmid: "37538019"
    pmcid: PMC10952771
    url: https://doi.org/10.1002/ijgo.14946
    source_license: CC BY 4.0（PMC掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "日本の国家試験や診療では「機能性子宮出血」「漏出性出血」の用語が依然として用いられる場面があり、FIGOの用語整理と日本の用語運用との対応関係は本調査では未確認である。ホルモン避妊薬使用中の破綻出血の頻度は製剤により異なり、出典では確認できなかったため主張に含めていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-016 (id: JlAKpo4)"
    kokushi: 医学各論 Ⅷ-8-D-②（機能性子宮出血、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-018
  domain: RP
  subdomain: 月経随伴症状（総論）
  assertion:
    plain_statement_ja: "月経随伴症状とは、月経周期に連動して周期的に現れる身体症状と精神症状の総称であり、代表的なものに乳房痛、腹部膨満、頭痛、浮腫などの身体症状と、易怒性、抑うつ気分、情緒不安定などの精神症状がある。症状は黄体期に出現して月経開始後まもなく消失するパターンをとることが特徴で、この周期性が、うつ病や不安障害などの持続的な疾患との鑑別点となる。程度が軽いものは多くの女性にみられるが、日常生活に支障をきたす場合は月経前症候群として治療の対象となる。"
    condition:
      region: 米国
      study: 総説（2018年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-821
    source: "Yonkers KA, Simoni MK. Premenstrual disorders. Am J Obstet Gynecol. 2018;218(1):68-74."
    doi: 10.1016/j.ajog.2017.05.045
    pmid: "28571724"
    pmcid: null
    url: https://doi.org/10.1016/j.ajog.2017.05.045
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "出典は月経前障害に焦点を当てた総説であり、月経時そのものに随伴する症状（月経痛に伴う症状など）の全体像は扱っていない。各症状の頻度は出典では確認できなかったため主張に含めていない。出典のライセンス表示は確認できなかった。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-D-①（月経前症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-019
  domain: RP
  subdomain: 月経異常のホルモン検査と解釈
  assertion:
    plain_statement_ja: "無月経や月経異常の内分泌評価では、まず妊娠を除外したうえで、血清TSH、遊離T4、プロラクチン、LH、FSH、エストラジオール、抗ミュラー管ホルモン（AMH）の測定が初期評価として推奨される。FSHが高値であれば卵巣性（卵巣機能不全）、FSHとLHが低値〜正常でエストラジオールが低値であれば視床下部・下垂体性を考える。機能性視床下部性無月経は器質的疾患を除外したうえでの除外診断であり、周期間隔が45日を超える状態が続く場合や3か月以上の無月経では診断的評価を行うことが勧められる。臨床的に男性化徴候がある場合はテストステロンやDHEA-Sの測定を追加する。"
    condition:
      region: 米国
      study: 内分泌学会診療ガイドライン（2017年、機能性視床下部性無月経）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-817
    source: "Gordon CM, Ackerman KE, Berga SL, Kaplan JR, Mastorakos G, Misra M, Murad MH, Santoro NF, Warren MP. Functional Hypothalamic Amenorrhea: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2017;102(5):1413-1439."
    doi: 10.1210/jc.2017-00131
    pmid: "28368518"
    pmcid: null
    url: https://doi.org/10.1210/jc.2017-00131
    source_license: Endocrine Societyのガイドライン。CC表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "出典は機能性視床下部性無月経に特化したガイドラインであり、初期検査の項目立てはその文脈に基づく。月経異常全般に対する日本の検査指針との対応は未確認である。各ホルモンの基準値や測定のタイミング（周期何日目か）の詳細は主張に含めていない。AMHなどの検査の日本での保険適用の状況は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-020
  domain: RP
  subdomain: 卵巣の構造と加齢変化（基礎）
  assertion:
    plain_statement_ja: "卵巣の加齢変化の中心は、卵胞数の年齢依存的な減少である。胎生期に形成された卵胞プールは排卵と閉鎖によって一方向性に減少し、卵胞数の減少が月経周期の不規則化と最終的な月経停止（閉経）の時期を決める。併行して卵子の質も低下し、妊孕性が漸減する。胞状卵胞の数が減るとインヒビンなどの負のフィードバックが弱まり、FSHが徐々に上昇する。抗ミュラー管ホルモン（AMH）の低下は、胞状卵胞コホートの縮小を最もよく反映する指標とされる。閉経年齢には個人差が大きい。"
    condition:
      region: 国際
      study: 総説（2009年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-825
    source: "Broekmans FJ, Soules MR, Fauser BC. Ovarian aging: mechanisms and clinical consequences. Endocr Rev. 2009;30(5):465-493."
    doi: 10.1210/er.2009-0006
    pmid: "19589949"
    pmcid: null
    url: https://doi.org/10.1210/er.2009-0006
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "卵胞数の具体的な数（出生時・思春期・閉経時の残存数）は出典の抄録では確認できなかったため主張に含めていない。卵巣予備能検査による自然妊娠や閉経年齢の予測精度には限界があることが出典でも指摘されている。出典のライセンス表示は確認できなかった。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-021
  domain: RP
  subdomain: 排卵障害
  assertion:
    plain_statement_ja: "排卵障害は無排卵や希発排卵として現れ、無月経・希発月経などの月経異常の主要な原因である。無排卵性不妊に占める多嚢胞性卵巣症候群（PCOS）の割合は約80%とされ、排卵障害の評価では原因の鑑別が中心となる。治療は段階的に行い、肥満がある場合は生活習慣への介入を先行させ、薬物による排卵誘発、さらに体外受精へと進む。"
    condition:
      region: 国際
      study: WHO ガイダンス策定のためのエビデンス分析（2016年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-838
    source: "Balen AH, Morley LC, Misso M, et al. The management of anovulatory infertility in women with polycystic ovary syndrome: an analysis of the evidence to support the development of global WHO guidance. Human Reproduction Update. 2016;22(6):687-708."
    doi: 10.1093/humupd/dmw025
    pmid: "27511809"
    pmcid: null
    url: https://doi.org/10.1093/humupd/dmw025
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "本出典は PCOS による無排卵を中心に扱っており、視床下部性や高プロラクチン血症など他の排卵障害の分類の詳細は本文で確認していないため、主張は PCOS 中心の範囲に限った。排卵誘発薬の国内承認・保険適用は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)"
    kokushi: 医学各論 Ⅷ-8-D-③（無排卵、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-022
  domain: RP
  subdomain: 多嚢胞性卵巣症候群
  assertion:
    plain_statement_ja: "多嚢胞性卵巣症候群（PCOS）は生殖年齢女性の10〜13%にみられる。成人の診断はアルゴリズムに沿って行い、不規則な月経周期（排卵障害）と高アンドロゲン血症（臨床的または生化学的）の両方がある場合は、超音波検査なしで診断できる。どちらか一方のみの場合は、多嚢胞性卵巣形態を超音波検査（片側卵巣あたりの卵胞数20個以上、または卵巣容積10ml以上）か、成人に限って血清AMHで確認する。他の疾患の除外も必要である。"
    condition:
      region: 国際
      study: 国際エビデンスに基づくガイドライン（2023年版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-826
    source: "Teede HJ, Tay CT, Laven J, et al. Recommendations from the 2023 International Evidence-based Guideline for the Assessment and Management of Polycystic Ovary Syndrome. Human Reproduction. 2023;38(9):1655-1679."
    doi: 10.1093/humrep/dead156
    pmid: "37580037"
    pmcid: PMC10477934
    url: https://doi.org/10.1093/humrep/dead156
    source_license: CC BY-NC 4.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "日本の診断基準（国内の学会基準）との差異は本調査では未確認である。思春期では超音波検査や AMH による多嚢胞性卵巣形態の判定は推奨されておらず、主張の基準値は成人を対象としたものである。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY)"
    kokushi: 医学各論 Ⅷ-8-D-⑥（多囊胞性卵巣症候群<PCOS>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-023
  domain: RP
  subdomain: 多嚢胞性卵巣症候群
  assertion:
    plain_statement_ja: "PCOS の管理では、健康的な生活習慣がすべての患者で基盤となる。不妊治療では、他の不妊因子のない無排卵の女性に対する排卵誘発の第一選択薬はレトロゾールで、クロミフェン（メトホルミンとの併用を含む）も用いられる。ゴナドトロピン療法や卵巣手術は主に第二選択、体外受精は第三選択と位置づけられる。あわせて、心血管リスク因子や糖代謝の評価を診断時に行うことが求められる。"
    condition:
      region: 国際
      study: 国際エビデンスに基づくガイドライン（2023年版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-826
    source: "Teede HJ, Tay CT, Laven J, et al. Recommendations from the 2023 International Evidence-based Guideline for the Assessment and Management of Polycystic Ovary Syndrome. Human Reproduction. 2023;38(9):1655-1679."
    doi: 10.1093/humrep/dead156
    pmid: "37580037"
    pmcid: PMC10477934
    url: https://doi.org/10.1093/humrep/dead156
    source_license: CC BY-NC 4.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "レトロゾールは排卵誘発の目的では多くの国で適応外使用とされており、日本での承認・保険適用の状況は本調査では未確認である。クロミフェン、メトホルミン、ゴナドトロピン製剤についても、国内の承認・保険適用は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)"
    kokushi: 医学各論 Ⅷ-8-D-⑥（多囊胞性卵巣症候群<PCOS>、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-024
  domain: RP
  subdomain: 早発卵巣不全
  assertion:
    plain_statement_ja: "早発卵巣不全（POI）は、40歳未満で月経周期の異常と卵巣機能低下の生化学的確認を伴う卵巣機能の喪失であり、有病率は3.5%とされる。2024年の国際ガイドラインでは、診断には FSH が25 IU/Lを超える上昇が1回確認されれば足りるとされ、診断が不確実な場合には FSH の再検や AMH 測定が用いられる。エストロゲン欠乏により骨、心血管、認知機能などへの影響が生じ、ホルモン療法がその軽減に用いられる。"
    condition:
      region: 国際
      study: 国際ガイドライン（2024年版、ESHRE・ASRM 等）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-827
    source: "Panay N, Anderson RA, Bennie A, et al. Evidence-based guideline: premature ovarian insufficiency. Human Reproduction Open. 2024;2024(4):hoae065."
    doi: 10.1093/hropen/hoae065
    pmid: "39660328"
    pmcid: PMC11631070
    url: https://doi.org/10.1093/hropen/hoae065
    source_license: CC BY 4.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "ホルモン療法の具体的な製剤・用量と、それらの国内承認・保険適用は未確認である。原因検索（遺伝学的検査を含む）の詳細はガイドライン本文の一部のみ確認したため、主張には含めていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ)"
    kokushi: 医学各論 Ⅷ-8-A-③（卵巣性無月経、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-025
  domain: RP
  subdomain: 高プロラクチン血症
  assertion:
    plain_statement_ja: "高プロラクチン血症は性腺機能低下を来し、無月経や希発月経、無排卵による不妊、乳汁漏出の原因となる。評価では、薬剤性のものを含む原因の鑑別が重要である。プロラクチン分泌腺腫（プロラクチノーマ）に対しては、ドパミン作動薬がプロラクチン値の低下、腫瘍の縮小、性腺機能の回復を目的とする治療の第一選択であり、有効性の高いカベルゴリンが他のドパミン作動薬より優先される。"
    condition:
      region: 国際
      study: 学会診療ガイドライン（2011年、Endocrine Society）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-828
    source: "Melmed S, Casanueva FF, Hoffman AR, et al. Diagnosis and Treatment of Hyperprolactinemia: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2011;96(2):273-288."
    doi: 10.1210/jc.2010-1692
    pmid: "21296991"
    pmcid: null
    url: https://doi.org/10.1210/jc.2010-1692
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "カベルゴリンとブロモクリプチンの国内承認・保険適用（適応症の範囲を含む）は本調査では未確認である。用量や正常化率などの数値は確認した範囲を超えるため主張には含めていない。2011年のガイドラインであり、その後の改訂の有無は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ)"
    kokushi: 医学各論 Ⅷ-8-D-⑤（高プロラクチン血症、乳汁漏出症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-026
  domain: RP
  subdomain: 黄体機能不全
  assertion:
    plain_statement_ja: "黄体機能不全（黄体期欠乏）は、黄体期の長さが10日以下と短い状態を指す臨床診断であり、プロゲステロンの分泌期間や量の不足、子宮内膜のプロゲステロンへの反応性低下が機序として挙げられる。ただし、黄体機能不全が不妊や反復流産の独立した原因であることは証明されておらず、診断に提案されてきた各種測定の妥当性や、治療が転帰を改善するかどうかについても結論は一致していない。健康で月経が正常な妊娠可能な女性にもみられることがある。"
    condition:
      region: 米国
      study: 学会委員会意見（2021年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-829
    source: "Practice Committee of the American Society for Reproductive Medicine. Diagnosis and treatment of luteal phase deficiency: a committee opinion. Fertility and Sterility. 2021;115(6):1416-1423."
    doi: 10.1016/j.fertnstert.2021.02.010
    pmid: "33827766"
    pmcid: null
    url: https://doi.org/10.1016/j.fertnstert.2021.02.010
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "個別の診断法（子宮内膜生検やプロゲステロン値の閾値など）の評価は抄録で確認した範囲を超えるため、主張には含めていない。プロゲステロン製剤を用いる場合の国内承認・保険適用は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ)"
    kokushi: 医学各論 Ⅷ-8-D-④（黄体機能不全、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-027
  domain: RP
  subdomain: 卵胞発育障害
  assertion:
    plain_statement_ja: "卵胞発育障害は排卵障害の一形態であり、PCOS では卵胞の発育が成熟に至らず無排卵となることが多く、無排卵性不妊の約80%は PCOS による。治療は段階的で、肥満がある場合は生活習慣への介入を先行させ、薬物による排卵誘発（クロミフェンやレトロゾール）を行い、第二選択としてゴナドトロピン療法や腹腔鏡下卵巣手術、その他の不妊因子がある場合や治療が不成功の場合には体外受精が検討される。"
    condition:
      region: 国際
      study: WHO ガイダンス策定のためのエビデンス分析（2016年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-838
    source: "Balen AH, Morley LC, Misso M, et al. The management of anovulatory infertility in women with polycystic ovary syndrome: an analysis of the evidence to support the development of global WHO guidance. Human Reproduction Update. 2016;22(6):687-708."
    doi: 10.1093/humupd/dmw025
    pmid: "27511809"
    pmcid: null
    url: https://doi.org/10.1093/humupd/dmw025
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "本出典は PCOS に伴う卵胞発育障害が中心であり、早発卵巣不全や視床下部性の卵胞発育障害は対象外である。排卵誘発薬やゴナドトロピン製剤の国内承認・保険適用は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)"
    kokushi: 医学各論 Ⅷ-8-E-①（女性不妊症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-028
  domain: RP
  subdomain: 子宮内膜因子
  assertion:
    plain_statement_ja: "子宮内膜を含む子宮因子は女性不妊の評価対象の一つであり、不妊の評価では、子宮の形態や内腔の異常を含め、すべての関連因子を系統的に同定することが求められる。評価は、頻度の高い原因の検出に向け、侵襲の少ない方法から迅速かつ費用対効果の高い進め方で行うことが原則である。"
    condition:
      region: 米国
      study: 学会委員会意見（2015年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-830
    source: "Practice Committee of the American Society for Reproductive Medicine. Diagnostic evaluation of the infertile female: a committee opinion. Fertility and Sterility. 2015;103(6):e44-e50."
    doi: 10.1016/j.fertnstert.2015.03.019
    pmid: "25936238"
    pmcid: null
    url: https://doi.org/10.1016/j.fertnstert.2015.03.019
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "子宮内膜の厚さの基準値や、内膜発育不良に対する個別治療（ホルモン製剤等）の有効性は出典の抄録では確認できず、主張には含めていない。関連する薬剤の国内承認・保険適用は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY)"
    kokushi: 医学各論 Ⅷ-8-E-①（女性不妊症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-029
  domain: RP
  subdomain: 卵管因子
  assertion:
    plain_statement_ja: "卵管通過性の評価には子宮卵管造影が標準的な第一選択の検査である。近位部の卵管閉塞には卵管カニュレーションが有効な選択肢となりうる。卵管留水症がある場合は、体外受精の妊娠率を改善するため、修復不能な卵管に対して腹腔鏡下卵管切除術または近位部卵管閉塞術を行うことが支持されている。卵管の修復手術と体外受精のどちらを選ぶかは、年齢、卵管障害の程度、他の不妊因子の有無などを考慮して決める。"
    condition:
      region: 米国
      study: 学会委員会意見（2021年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-831
    source: "Practice Committee of the American Society for Reproductive Medicine. Role of tubal surgery in the era of assisted reproductive technology: a committee opinion. Fertility and Sterility. 2021;115(5):1143-1150."
    doi: 10.1016/j.fertnstert.2021.01.051
    pmid: "33642065"
    pmcid: null
    url: https://doi.org/10.1016/j.fertnstert.2021.01.051
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "国内での卵管手術の実施体制や保険適用（卵管鏡下卵管形成術など国内で用いられる術式の位置づけ）は本調査では未確認である。妊娠率の具体的な数値は出典の結論部で確認した範囲を超えるため主張には含めていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY)"
    kokushi: 医学各論 Ⅷ-8-E-①（女性不妊症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-030
  domain: RP
  subdomain: 子宮頸管因子
  assertion:
    plain_statement_ja: "子宮頸管因子は女性不妊の原因の一つであるが、頻度の高い原因ではない。不妊の初期評価では、排卵障害、卵管因子、子宮因子、男性因子など頻度の高い原因を優先し、侵襲の少ない方法から系統的かつ効率的に評価を進める中で、頸管因子も含めて関連因子を漏れなく同定することが求められる。"
    condition:
      region: 米国
      study: 学会委員会意見（2015年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-830
    source: "Practice Committee of the American Society for Reproductive Medicine. Diagnostic evaluation of the infertile female: a committee opinion. Fertility and Sterility. 2015;103(6):e44-e50."
    doi: 10.1016/j.fertnstert.2015.03.019
    pmid: "25936238"
    pmcid: null
    url: https://doi.org/10.1016/j.fertnstert.2015.03.019
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "性交後試験など頸管因子の個別検査の現在の位置づけは、出典の抄録では確認できず主張には含めていない。頸管因子の頻度の具体的数値も確認できていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-E-①（女性不妊症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-031
  domain: RP
  subdomain: 体外受精
  assertion:
    plain_statement_ja: "体外受精の調節卵巣刺激では、刺激への反応（高反応・低反応）の予測に、胞状卵胞数（AFC）または血清AMHを用いることが強く推奨される。一般の体外受精・顕微授精を受ける集団では、有効性が同等で安全性が高いことから、GnRHアンタゴニスト法が GnRHアゴニスト法より強く推奨され、低反応が予測される場合には両法が同等に推奨される。メトホルミン、成長ホルモン、テストステロン、アスピリンなどの補助療法は、有効性や安全性を高める目的では推奨されていない。"
    condition:
      region: 欧州
      study: 学会ガイドライン（2020年、ESHRE）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-832
    source: "Ovarian Stimulation TEGGO, Bosch E, Broer S, et al. ESHRE guideline: ovarian stimulation for IVF/ICSI. Human Reproduction Open. 2020;2020(2):hoaa009."
    doi: 10.1093/hropen/hoaa009
    pmid: "32395637"
    pmcid: PMC7203749
    url: https://doi.org/10.1093/hropen/hoaa009
    source_license: CC BY-NC 4.0（Crossref のライセンス表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "ゴナドトロピン製剤や GnRH アナログ製剤の国内承認・保険適用、および生殖補助医療の保険適用の範囲（年齢・回数の要件を含む）は本調査では未確認である。2025年に改訂版ガイドラインが公表されており、本カードは2020年版に基づく。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY)"
    kokushi: 医学各論 Ⅷ-8-E-①（女性不妊症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-032
  domain: RP
  subdomain: 卵子凍結
  assertion:
    plain_statement_ja: "計画的卵子凍結（将来の妊娠に備えてあらかじめ卵子を凍結保存すること）は、新しく発展途上の手技であるが、将来の不妊を避ける助けになりうるものとして倫理的に許容されうるとされる。ただし、有効性や長期的な影響には不確実性が残るため、検討する女性にはその不確実性について十分に情報提供することが不可欠である。"
    condition:
      region: 米国
      study: 学会倫理委員会意見（2018年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-833
    source: "Ethics Committee of the American Society for Reproductive Medicine. Planned oocyte cryopreservation for women seeking to preserve future reproductive potential: an Ethics Committee opinion. Fertility and Sterility. 2018;110(6):1022-1028."
    doi: 10.1016/j.fertnstert.2018.08.027
    pmid: "30396539"
    pmcid: null
    url: https://doi.org/10.1016/j.fertnstert.2018.08.027
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "本出典は医学的適応によらない計画的凍結が対象であり、がん治療前などの医学的妊孕性温存の詳細は扱っていない。年齢や凍結卵子数による出生率の具体的数値は抄録で確認できず主張には含めていない。国内での実施体制や費用負担（保険適用の有無を含む）は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-E-①（女性不妊症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-033
  domain: RP
  subdomain: ホルモン製剤
  assertion:
    plain_statement_ja: "婦人科で用いるホルモン製剤の中心は、エストロゲン製剤とプロゲスチン（黄体ホルモン）製剤である。エストロゲンには天然型と合成型があり、プロゲスチンには構造や受容体への結合特性、代謝物の活性が異なる多様な種類がある。経口、経皮、腟内、子宮内など投与経路によって薬物動態やホルモン作用、代謝が変わるため、治療目的に応じて製剤の種類と投与経路を使い分ける。"
    condition:
      region: 国際
      study: 薬理学総説（2005年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-835
    source: "Kuhl H. Pharmacology of estrogens and progestogens: influence of different routes of administration. Climacteric. 2005;8(Suppl 1):3-63."
    doi: 10.1080/13697130500148875
    pmid: "16112947"
    pmcid: null
    url: https://doi.org/10.1080/13697130500148875
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "個別製剤の国内承認・保険適用と用量は未確認である。2005年の総説であり、その後に開発・発売された製剤（新しいプロゲスチン等）は含まれていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-034
  domain: RP
  subdomain: 薬物相互作用
  assertion:
    plain_statement_ja: "ホルモン避妊薬は併用薬との薬物相互作用により効果が減弱することがある。抗レトロウイルス薬との相互作用を対象とした系統的レビュー（49論文を含む）では、エファビレンツとプロゲスチンインプラント、緊急避妊薬、腟リングの併用を調べた研究の多くで、妊娠率の上昇、排卵を示唆する黄体期プロゲステロン値、プロゲスチン血中濃度の低下が報告された。一方で、多くの抗レトロウイルス薬とホルモン避妊薬は安全かつ有効に併用できると結論されている。"
    condition:
      region: 国際
      study: 系統的レビュー（2024年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-834
    source: "Todd CS, Lorenzetti L, Mussa A, et al. Drug-drug interactions between antiretrovirals and hormonal contraception: an updated systematic review. Contraception. 2024;138:110490."
    doi: 10.1016/j.contraception.2024.110490
    pmid: "38762199"
    pmcid: null
    url: https://doi.org/10.1016/j.contraception.2024.110490
    source_license: CC BY 4.0（Crossref のライセンス表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: "本出典の対象は抗レトロウイルス薬との相互作用に限られ、抗てんかん薬やリファンピシン系抗菌薬など他の酵素誘導薬との相互作用は扱っていないため、主張はその範囲に限った。国内のホルモン避妊薬の承認・保険適用の状況は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-035
  domain: RP
  subdomain: 手術療法
  assertion:
    plain_statement_ja: "過多月経に対する手術療法の一つに、子宮を温存する子宮内膜アブレーション（内膜の切除・破壊）がある。28件のランダム化比較試験（4287人）をまとめたレビューでは、第2世代の手技は第1世代（子宮鏡下）の手技と比べて無月経率や出血の改善が同等であり、手術時間が短く、局所麻酔で行われることが多かった。子宮摘出は確実な治療であるが費用が高くリスクも伴うため、薬物療法で十分な改善が得られない場合の選択肢としてアブレーションが位置づけられる。"
    condition:
      region: 国際
      study: 系統的レビュー（2019年、Cochrane）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-836
    source: "Bofill Rodriguez M, Lethaby A, Grigore M, et al. Endometrial resection and ablation techniques for heavy menstrual bleeding. Cochrane Database of Systematic Reviews. 2019;(1):CD001501."
    doi: 10.1002/14651858.CD001501.pub5
    pmid: "30667064"
    pmcid: PMC7057272
    url: https://doi.org/10.1002/14651858.CD001501.pub5
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "レビューの対象は、腔外の3cm未満の筋腫を除き既知の子宮病変のない過多月経であり、器質的疾患がある場合は適応が異なる。国内での子宮内膜アブレーションの実施状況や保険適用は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-036
  domain: RP
  subdomain: 性分化疾患
  assertion:
    plain_statement_ja: "性分化は、染色体、性腺、内・外性器の性が段階的に決まっていく過程であり、その過程のいずれかに非典型的な点がある状態は性分化疾患（DSD）と総称される。現在の分類では核型を接頭辞として用い、46,XY DSD、46,XX DSD、性染色体 DSD などと分類し、従来の「男性仮性半陰陽」「女性仮性半陰陽」などの用語は用いられなくなった。出生時に外性器が染色体や性腺と比べて非典型的な場合は、この枠組みで原因を評価する。"
    condition:
      region: 国際
      study: 総説（2008年、国際コンセンサスに基づく分類）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-837
    source: "Hughes IA. Disorders of sex development: a new definition and classification. Best Practice & Research Clinical Endocrinology & Metabolism. 2008;22(1):119-134."
    doi: 10.1016/j.beem.2007.11.001
    pmid: "18279784"
    pmcid: null
    url: https://doi.org/10.1016/j.beem.2007.11.001
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "個別の原因疾患（アンドロゲン不応症や先天性副腎過形成など）の頻度や診断手順の詳細は、抄録で確認した範囲を超えるため主張には含めていない。2008年の総説であり、その後の遺伝子診断の進歩は反映されていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)"
    kokushi: 医学各論 Ⅷ-8-A-④（子宮性無月経、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-037
  domain: RP
  subdomain: 排卵誘発
  assertion:
    plain_statement_ja: "PCOS による無排卵性不妊に対する排卵誘発について、750人を対象とした多施設二重盲検ランダム化比較試験では、レトロゾール群がクロミフェン群より累積出生率（27.5%対19.1%）と累積排卵率（61.7%対48.3%）が高かった。先天異常の頻度には有意な差はみられなかった。"
    condition:
      region: 米国
      study: 多施設ランダム化比較試験（2014年、対象は PCOS）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-839
    source: "Legro RS, Brzyski RG, Diamond MP, et al. Letrozole versus clomiphene for infertility in the polycystic ovary syndrome. New England Journal of Medicine. 2014;371(2):119-129."
    doi: 10.1056/NEJMoa1313517
    pmid: "25006718"
    pmcid: PMC4175743
    url: https://doi.org/10.1056/NEJMoa1313517
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "レトロゾールの排卵誘発目的での国内承認・保険適用は未確認であり、国内では適応外使用となる可能性がある（取り込み側で添付文書・PMDA の確認が必要）。クロミフェンの国内承認状況も未確認である。対象は PCOS に限られ、他の原因による排卵障害へそのまま一般化はできない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ)"
    kokushi: 医学各論 Ⅷ-8-D-③（無排卵、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-038
  domain: RP
  subdomain: 女性不妊総論
  assertion:
    plain_statement_ja: "女性不妊の原因は、排卵障害、卵管障害、子宮や子宮内膜の異常、子宮内膜症など多岐にわたり、男性因子や、検査で原因が特定できない原因不明不妊も存在する。不妊の診断的評価は、関連するすべての因子を同定するために、頻度の高い原因から侵襲の少ない方法で、系統的かつ効率的に行うことが原則である。"
    condition:
      region: 米国
      study: 学会委員会意見（2015年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-830
    source: "Practice Committee of the American Society for Reproductive Medicine. Diagnostic evaluation of the infertile female: a committee opinion. Fertility and Sterility. 2015;103(6):e44-e50."
    doi: 10.1016/j.fertnstert.2015.03.019
    pmid: "25936238"
    pmcid: null
    url: https://doi.org/10.1016/j.fertnstert.2015.03.019
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "各原因が占める割合の具体的数値は、出典の抄録では確認できず（地域や対象集団によっても異なるため）、主張には数値を含めていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-E-①（女性不妊症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-039
  domain: RP
  subdomain: 不妊症の評価
  assertion:
    plain_statement_ja: "不妊の評価は、避妊をしない定期的な性交を12か月続けても妊娠が成立しない場合に開始し、女性が35歳以上の場合は6か月を目安に開始する。不妊の原因となる病態が既往などから明らかな場合は、期間を待たずに評価を始める。評価は病歴聴取と身体所見から始め、排卵機能、卵管通過性、子宮の形態など、頻度の高い原因を侵襲の少ない方法から系統的に調べる。"
    condition:
      region: 米国
      study: 学会委員会意見（2015年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-830
    source: "Practice Committee of the American Society for Reproductive Medicine. Diagnostic evaluation of the infertile female: a committee opinion. Fertility and Sterility. 2015;103(6):e44-e50."
    doi: 10.1016/j.fertnstert.2015.03.019
    pmid: "25936238"
    pmcid: null
    url: https://doi.org/10.1016/j.fertnstert.2015.03.019
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "評価開始時期の基準は米国の学会意見に基づくもので、日本の診療での運用や、不妊治療の保険適用の要件（年齢・回数など）は本調査では未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY)"
    kokushi: 医学各論 Ⅷ-8-E-①（女性不妊症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-040
  domain: RP
  subdomain: 甲状腺機能異常
  assertion:
    plain_statement_ja: "甲状腺機能異常は月経異常の原因となる。甲状腺中毒症（機能亢進）では主に過少月経と頻発月経（多月経）が、甲状腺機能低下症では主に希発月経がみられる。甲状腺機能異常は妊孕性の低下とも関連しており、月経異常や不妊の評価では甲状腺機能の確認が対象となる。"
    condition:
      region: 国際
      study: 総説（2010年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-840
    source: "Krassas GE, Poppe K, Glinoer D. Thyroid function and human reproductive health. Endocrine Reviews. 2010;31(5):702-755."
    doi: 10.1210/er.2009-0041
    pmid: "20573783"
    pmcid: null
    url: https://doi.org/10.1210/er.2009-0041
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "甲状腺ホルモン製剤や抗甲状腺薬の国内承認・保険適用は未確認である。TSH などの基準値や、自己免疫性甲状腺疾患と不妊治療成績の関係の数値は、確認した範囲を超えるため主張には含めていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-041
  domain: RP
  subdomain: 避妊法の総論
  assertion:
    plain_statement_ja: "避妊法の有効性は、正しく継続して使う完全使用と、実際の一般的な使い方である典型使用とで分けて評価され、両者の妊娠率の差は、その方法が使用者の不正確な使用にどれだけ影響されるかを示す。使用者自身の継続的な努力を必要としない方法ほど、典型使用でも妊娠率は低く保たれる。"
    condition:
      region: 米国
      study: 米国の避妊失敗率の推計を更新した総説（2011年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-841
    source: "Trussell J. Contraceptive failure in the United States. Contraception. 2011;83(5):397-404."
    doi: 10.1016/j.contraception.2011.01.021
    pmid: "21477680"
    pmcid: PMC3638209
    url: https://doi.org/10.1016/j.contraception.2011.01.021
    source_license: 出版社ページ・Crossref に CC ライセンスの表示なし（PMC 収載は著者原稿）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "方法ごとの個別の妊娠率の数値は抄録に含まれず、本文の表を確認していないため主張文には入れていない。推計は米国のデータに基づき、日本の使用実態とは異なる可能性がある。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-F（避妊、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-042
  domain: RP
  subdomain: 経口避妊薬
  assertion:
    plain_statement_ja: "低用量経口避妊薬（混合型経口避妊薬）は理想的に使用すれば妊娠防止効果は高いが、飲み忘れなどにより実際の使用での有効性は低くなり、継続率の低さが課題である。リスクとして静脈血栓塞栓症の増加が最もよく知られ、動脈血栓症のリスク上昇も報告される。一方で、卵巣癌・子宮内膜癌・大腸癌のリスク低下、過多月経や月経困難症、多毛や痤瘡への効果といった避妊以外の利益もある。処方時には利益とリスクのバランスを個別に説明することが重要である。"
    condition:
      region: 欧米
      study: 混合型ホルモン避妊薬の処方実態と利益・リスクに関する総説（2014年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-842
    source: "Brynhildsen J. Combined hormonal contraceptives: prescribing patterns, compliance, and benefits versus risks. Therapeutic Advances in Drug Safety. 2014;5(5):201-213."
    doi: 10.1177/2042098614548857
    pmid: "25360241"
    pmcid: PMC4212440
    url: https://doi.org/10.1177/2042098614548857
    source_license: PMC ページで CC ライセンスの版を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "静脈血栓塞栓症などの個別のリスクの大きさは抄録に数値がなく、主張文には入れていない。日本における低用量ピルの避妊目的での承認状況や、月経困難症に対する LEP 製剤の保険適用の詳細は、本出典では確認しておらず未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-F（避妊、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-043
  domain: RP
  subdomain: 子宮内避妊具・長時間作用型避妊法
  assertion:
    plain_statement_ja: "子宮内避妊具（IUD）と皮下インプラントからなる長時間作用型の可逆的避妊法（LARC）は、最も有効な可逆的避妊法である。装着後は使用者の継続的な努力を必要としないことが大きな利点で、除去すれば妊孕性は速やかに回復する。"
    condition:
      region: 米国
      study: 米国産科婦人科学会の診療指針（2017年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-843
    source: "American College of Obstetricians and Gynecologists. Practice Bulletin No. 186: Long-Acting Reversible Contraception: Implants and Intrauterine Devices. Obstetrics & Gynecology. 2017;130(5):e251-e269."
    doi: 10.1097/AOG.0000000000002400
    pmid: "29064972"
    pmcid: null
    url: https://doi.org/10.1097/AOG.0000000000002400
    source_license: 学会刊行物で CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "本出典は米国の指針であり、日本で使用できる製剤の範囲（皮下インプラントの国内での扱いを含む）は確認しておらず、国内の承認状況は未確認である。銅付加 IUD とレボノルゲストレル放出子宮内システムの個別の妊娠率の数値は抄録になく、主張文には入れていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-F（避妊、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-044
  domain: RP
  subdomain: 緊急避妊
  assertion:
    plain_statement_ja: "緊急避妊は、避妊しなかった性交や避妊の失敗（コンドームの破損、経口避妊薬の飲み忘れなど）の後に妊娠を防ぐために用いる方法である。方法には、エストロゲン・プロゲスチン併用、黄体ホルモン単独、選択的プロゲステロン受容体修飾薬の経口投与と、銅付加子宮内避妊具の挿入がある。"
    condition:
      region: 米国
      study: 米国産科婦人科学会の診療指針（2015年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-844
    source: "American College of Obstetricians and Gynecologists. Practice Bulletin No. 152: Emergency Contraception. Obstetrics & Gynecology. 2015;126(3):e1-e11."
    doi: 10.1097/AOG.0000000000001047
    pmid: "26287787"
    pmcid: null
    url: https://doi.org/10.1097/AOG.0000000000001047
    source_license: 学会刊行物で CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "各方法の有効性の数値や使用可能時間の詳細は抄録になく、主張文には入れていない。日本におけるレボノルゲストレル緊急避妊薬の承認・入手方法（処方箋の要否など）の現行制度は本出典では確認しておらず未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-F（避妊、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-045
  domain: RP
  subdomain: バリア法・自然法・外科的避妊
  assertion:
    plain_statement_ja: "コンドームなどのバリア法や基礎体温などを用いる自然法は、使用のたびの正確な実践が必要で、完全使用と典型使用の妊娠率の差が大きい方法群である。卵管結紮や精管切除などの外科的避妊は、使用者依存性がなく効果が持続する一方で、原則として永久避妊として扱われる。"
    condition:
      region: 米国
      study: 米国の避妊失敗率の推計を更新した総説（2011年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-841
    source: "Trussell J. Contraceptive failure in the United States. Contraception. 2011;83(5):397-404."
    doi: 10.1016/j.contraception.2011.01.021
    pmid: "21477680"
    pmcid: PMC3638209
    url: https://doi.org/10.1016/j.contraception.2011.01.021
    source_license: 出版社ページ・Crossref に CC ライセンスの表示なし（PMC 収載は著者原稿）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "方法ごとの個別の妊娠率の数値は抄録に含まれず本文の表を確認していないため、主張文には定性的な表現にとどめた。外科的避妊の再疎通の可否や日本での実施状況は本出典では確認していない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-F（避妊、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-046
  domain: RP
  subdomain: 閉経の定義
  assertion:
    plain_statement_ja: "閉経は、最終月経の後に12か月間月経がないことをもって、遡って判定される。生殖加齢の段階分類（STRAW+10）では、この12か月の経過をもって閉経期（パリメノポーズ）の終了とされる。診断は原則として臨床的に行い、段階の判定には月経のパターンと内分泌の変化が用いられる。"
    condition:
      region: 国際
      study: 生殖加齢の段階分類に関する国際ワークショップの合意文書（STRAW+10、2012年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-845
    source: "Harlow SD, Gass M, Hall JE, et al. Executive summary of the Stages of Reproductive Aging Workshop + 10: addressing the unfinished agenda of staging reproductive aging. Menopause. 2012;19(4):387-395."
    doi: 10.1097/gme.0b013e31824d8f40
    pmid: "22343510"
    pmcid: PMC3340903
    url: https://doi.org/10.1097/gme.0b013e31824d8f40
    source_license: PMC 収載は著者原稿で CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "日本産科婦人科学会による閉経の定義の文言そのものは本出典では確認しておらず、STRAW+10 の枠組みに基づく記述である。若年での無月経など、ホルモン測定を要する場面の詳細は扱っていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-047
  domain: RP
  subdomain: 更年期の生理
  assertion:
    plain_statement_ja: "更年期への移行期には、視床下部・下垂体・卵巣系の変化により月経周期が変動し、FSH は上昇する。後期移行期は60日以上の無月経が出現することで特徴づけられる。卵巣の指標としては抗ミュラー管ホルモン（AMH）やインヒビン B の低下、胞状卵胞数の減少が加齢に伴う変化として用いられ、最終月経の前後でホルモンの変動は急激になる。"
    condition:
      region: 国際
      study: 生殖加齢の段階分類に関する国際ワークショップの合意文書（STRAW+10、2012年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-845
    source: "Harlow SD, Gass M, Hall JE, et al. Executive summary of the Stages of Reproductive Aging Workshop + 10: addressing the unfinished agenda of staging reproductive aging. Menopause. 2012;19(4):387-395."
    doi: 10.1097/gme.0b013e31824d8f40
    pmid: "22343510"
    pmcid: PMC3340903
    url: https://doi.org/10.1097/gme.0b013e31824d8f40
    source_license: PMC 収載は著者原稿で CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "各ホルモンの具体的な数値基準は本文の段階表に依存し、本カードでは確認した範囲（月経基準と変化の方向）にとどめた。各段階の持続期間の詳細は入れていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-048
  domain: RP
  subdomain: 更年期障害の病態と症状
  assertion:
    plain_statement_ja: "更年期の移行に伴う症状のうち最も多く報告されるのは、ほてりやのぼせなどの血管運動症状である。これに加えて、腟の乾燥と性交痛、睡眠の困難、気分の悪化が更年期に近づくにつれて増悪し、互いに影響し合って生活の質を下げる。閉経後の認知の変化は、ホルモンよりも加齢と関連することが多いとされる。"
    condition:
      region: 国際
      study: 更年期症状とその管理に関する総説（2015年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-846
    source: "Santoro N, Epperson CN, Mathews SB. Menopausal Symptoms and Their Management. Endocrinology and Metabolism Clinics of North America. 2015;44(3):497-515."
    doi: 10.1016/j.ecl.2015.05.001
    pmid: "26316239"
    pmcid: PMC4890704
    url: https://doi.org/10.1016/j.ecl.2015.05.001
    source_license: 出版社ページ・Crossref に CC ライセンスの表示なし（PMC 収載は著者原稿）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "各症状の有病率の数値は抄録になく、主張文には入れていない。日本の更年期障害の診断で用いられる評価尺度（簡略更年期指数など）は本出典では扱っておらず未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-9-A（更年期障害、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-049
  domain: RP
  subdomain: ホルモン補充療法の適応
  assertion:
    plain_statement_ja: "ホルモン補充療法（HRT）は血管運動症状と閉経後泌尿生殖器症候群に対する最も有効な治療であり、骨量減少と骨折の予防効果も示されている。リスクは製剤の種類、用量、投与期間、投与経路、開始時期、黄体ホルモンの併用の有無で異なる。60歳未満、または閉経後10年以内で禁忌のない女性では、煩わしい血管運動症状の治療と骨量減少の予防について利益・リスク比は良好とされ、治療は個別化し、継続の利益とリスクを定期的に再評価する。"
    condition:
      region: 国際
      study: 北米閉経学会のホルモン療法に関する声明（2022年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-847
    source: "The North American Menopause Society. The 2022 hormone therapy position statement of The North American Menopause Society. Menopause. 2022;29(7):767-794."
    doi: 10.1097/GME.0000000000002028
    pmid: "35797481"
    pmcid: null
    url: https://doi.org/10.1097/GME.0000000000002028
    source_license: 学会誌掲載で CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "個別の製剤の用量や投与レジメンの詳細は抄録になく、主張文には入れていない。日本で使用できるエストロゲン・黄体ホルモン製剤の種類と、それぞれの国内承認・保険適用の状況は本出典では確認しておらず未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-9-A（更年期障害、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-050
  domain: RP
  subdomain: ホルモン補充療法のリスクとベネフィット
  assertion:
    plain_statement_ja: "閉経後女性を対象とした大規模な無作為化試験（Women's Health Initiative）では、結合型エストロゲンとメドロキシプロゲステロン酢酸エステルの併用により、冠動脈疾患（ハザード比1.29）、脳卒中（1.41）、肺塞栓症（2.13）、浸潤性乳癌（1.26）のリスクが増加し、大腸癌（0.63）と股関節骨折（0.66）のリスクが低下した。絶対数では、1万人・年あたり冠動脈疾患7件、脳卒中8件、肺塞栓症8件、浸潤性乳癌8件の増加と、大腸癌6件、股関節骨折5件の減少に相当した。リスクが利益を上回るとして試験は平均5.2年の追跡で中止された。"
    condition:
      region: 米国
      study: 子宮のある閉経後女性16,608人を対象とした無作為化比較試験（2002年報告）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-848
    source: "Rossouw JE, Anderson GL, Prentice RL, et al. Risks and Benefits of Estrogen Plus Progestin in Healthy Postmenopausal Women: Principal Results From the Women's Health Initiative Randomized Controlled Trial. JAMA. 2002;288(3):321-333."
    doi: 10.1001/jama.288.3.321
    pmid: "12117397"
    pmcid: null
    url: https://doi.org/10.1001/jama.288.3.321
    source_license: 出版社ページ・Crossref に CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "数値は抄録で確認した当該併用レジメン（結合型エストロゲン0.625mg/日＋メドロキシプロゲステロン酢酸エステル2.5mg/日）の結果であり、経皮製剤や他の黄体ホルモン製剤、日本で用いられる用量への外挿はできない。これらの製剤の国内承認・保険適用の状況は本出典では確認しておらず未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-9-A（更年期障害、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-051
  domain: RP
  subdomain: 閉経後骨粗鬆症の診断
  assertion:
    plain_statement_ja: "閉経後女性では、将来の骨折リスクを国ごとに整備された骨折リスク評価ツールを用いて評価し、その結果を治療開始の判断に結びつけることが、薬物療法ガイドラインの原則とされている。評価には骨密度測定による骨の状態の把握が含まれ、患者の希望も治療計画に反映させる。栄養・生活習慣への介入と転倒予防は、すべての薬物療法に併用される。"
    condition:
      region: 国際
      study: 米国内分泌学会の閉経後骨粗鬆症の薬物療法ガイドライン（2019年）の管理原則
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-849
    source: "Eastell R, Rosen CJ, Black DM, et al. Pharmacological Management of Osteoporosis in Postmenopausal Women: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2019;104(5):1595-1622."
    doi: 10.1210/jc.2019-00221
    pmid: "30907953"
    pmcid: null
    url: https://doi.org/10.1210/jc.2019-00221
    source_license: 学会ガイドラインで CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "骨密度の T スコアによる診断閾値などの個別の数値基準は抄録に含まれず本文で確認していないため、主張文には入れていない。日本骨粗鬆症学会の診断基準（脆弱性骨折の有無と骨密度による判定）は本出典とは別体系であり、未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-9-B-①（骨粗鬆症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-052
  domain: RP
  subdomain: 閉経後骨粗鬆症の治療
  assertion:
    plain_statement_ja: "閉経後骨粗鬆症の薬物療法には、骨折リスクのある女性で骨折率を低下させ、利益・リスク比と安全性が許容できる薬剤が複数ある。治療の選択では患者の希望を取り入れ、栄養・生活習慣への介入と転倒予防をすべての薬物療法に併用することが原則とされる。"
    condition:
      region: 国際
      study: 米国内分泌学会の閉経後骨粗鬆症の薬物療法ガイドライン（2019年）の管理原則
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-849
    source: "Eastell R, Rosen CJ, Black DM, et al. Pharmacological Management of Osteoporosis in Postmenopausal Women: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2019;104(5):1595-1622."
    doi: 10.1210/jc.2019-00221
    pmid: "30907953"
    pmcid: null
    url: https://doi.org/10.1210/jc.2019-00221
    source_license: 学会ガイドラインで CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "個別の薬剤（ビスホスホネート、デノスマブ、ロモソズマブなど）の推奨順位や骨折抑制効果の数値は抄録になく、主張文には入れていない。各薬剤の日本における承認・保険適用の状況は本出典では確認しておらず未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-9-B-①（骨粗鬆症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-054
  domain: RP
  subdomain: 閉経後泌尿生殖器症候群
  assertion:
    plain_statement_ja: "閉経後泌尿生殖器症候群（GSM）は閉経後女性の約27〜84%にみられるとされ、外陰腟の萎縮に伴う乾燥や性交痛、尿路症状などを含み、性生活と生活の質を損なうが、見逃されやすく治療を受けていないことも多い。軽症では市販の潤滑剤や保湿剤が用いられ、中等症以上では低用量の腟エストロゲン、腟内 DHEA、全身ホルモン療法、オスペミフェンが有効とされる。低用量腟エストロゲンなど腟局所療法では黄体ホルモンの併用は不要とされる。"
    condition:
      region: 米国・カナダ
      study: 北米閉経学会の GSM に関する声明（2020年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-850
    source: "The North American Menopause Society. The 2020 genitourinary syndrome of menopause position statement of The North American Menopause Society. Menopause. 2020;27(9):976-992."
    doi: 10.1097/GME.0000000000001609
    pmid: "32852449"
    pmcid: null
    url: https://doi.org/10.1097/GME.0000000000001609
    source_license: 学会誌掲載で CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "有病割合27〜84%は研究により対象や定義が異なり幅が大きい値である。腟内 DHEA やオスペミフェンなど、日本で使用できない製剤が含まれており、各製剤の国内承認・保険適用の状況は本出典では確認しておらず未確認である。腟局所療法の1年を超える子宮内膜への安全性は確立していないと声明に記載がある。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-019 (id: JlAKppE)；TBL-02-09-020 (id: JlAKppI)"
    kokushi: 医学各論 Ⅷ-9-B-②（萎縮性腟炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-055
  domain: RP
  subdomain: 更年期と心血管リスク
  assertion:
    plain_statement_ja: "ホルモン療法の心血管系を含むリスクは開始時期によって異なり、閉経後10年以上経過してから、または60歳を超えてから開始した場合、冠動脈疾患、脳卒中、静脈血栓塞栓症、認知症の絶対リスクが大きくなり、利益・リスク比は不利になるとされる。閉経移行そのものが脂質代謝の悪化など心血管リスクの変化と重なる時期であり、更年期の健康管理では心血管リスクの評価が重要になる。"
    condition:
      region: 国際
      study: 北米閉経学会のホルモン療法に関する声明（2022年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-847
    source: "The North American Menopause Society. The 2022 hormone therapy position statement of The North American Menopause Society. Menopause. 2022;29(7):767-794."
    doi: 10.1097/GME.0000000000002028
    pmid: "35797481"
    pmcid: null
    url: https://doi.org/10.1097/GME.0000000000002028
    source_license: 学会誌掲載で CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "脂質プロファイル（LDL コレステロールや中性脂肪）の個別の変化量は本出典の抄録になく、主張文には入れていない。心血管リスクに関する個別の推奨（スタチン等の使用）は扱っておらず、各薬剤の国内承認・保険適用も未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-9-B-③（脂質異常症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-056
  domain: RP
  subdomain: 閉経移行期のうつ病
  assertion:
    plain_statement_ja: "閉経移行期と閉経後早期は、抑うつ症状と大うつ病エピソードの発症に対する脆弱性の窓である。この時期に大うつ病を発症する女性の多くは、過去にうつ病エピソードを経験している。症状は古典的な抑うつ症状に、血管運動症状や睡眠障害などの更年期症状と中年期の心理社会的課題が重なって現れる。治療の第一選択は、抗うつ薬や精神療法など、うつ病に対して有効性が証明された治療であり、エストロゲン療法は閉経移行期うつ病の治療としては承認されていない。"
    condition:
      region: 国際
      study: 閉経移行期うつ病の評価と治療に関する専門家ガイドライン（2018年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-852
    source: "Maki PM, Kornstein SG, Joffe H, et al. Guidelines for the evaluation and treatment of perimenopausal depression: summary and recommendations. Menopause. 2018;25(10):1069-1085."
    doi: 10.1097/GME.0000000000001174
    pmid: "30179986"
    pmcid: null
    url: https://doi.org/10.1097/GME.0000000000001174
    source_license: 学会誌掲載で CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "本カードは出題基準の「心身症」の観点から、更年期に重なる精神症状として閉経移行期うつ病を扱ったもので、心身症そのものの定義や分類は扱っていない。個別の抗うつ薬の選択や用量は抄録になく、日本における各薬剤の承認・保険適用の状況は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-9-A（更年期障害、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-058
  domain: RP
  subdomain: 女性のライフステージ
  assertion:
    plain_statement_ja: "女性の生殖に関する加齢は、生殖期の後期、更年期への移行期、閉経後という段階を通して進み、STRAW+10 の段階分類は月経のパターンと内分泌・卵巣の指標によってこれらを定義する。この分類は年齢、民族、体格、生活習慣にかかわらず適用できるとされ、ライフステージに応じた健康評価や研究の比較の基盤になる。"
    condition:
      region: 国際
      study: 生殖加齢の段階分類に関する国際ワークショップの合意文書（STRAW+10、2012年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-845
    source: "Harlow SD, Gass M, Hall JE, et al. Executive summary of the Stages of Reproductive Aging Workshop + 10: addressing the unfinished agenda of staging reproductive aging. Menopause. 2012;19(4):387-395."
    doi: 10.1097/gme.0b013e31824d8f40
    pmid: "22343510"
    pmcid: PMC3340903
    url: https://doi.org/10.1097/gme.0b013e31824d8f40
    source_license: PMC 収載は著者原稿で CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "本出典が扱うのは思春期以降の生殖加齢の段階であり、小児期や妊娠・産褥を含むライフステージ全体の健康課題は扱っていない。各段階の持続期間の詳細は入れていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-059
  domain: RP
  subdomain: 更年期障害の非ホルモン療法
  assertion:
    plain_statement_ja: "血管運動症状に対する非ホルモン療法のうち、根拠に基づき推奨されるのは、認知行動療法、臨床催眠、SSRI・SNRI、ガバペンチン、フェゾリネタントで、ほかにオキシブチニンや体重減少などが条件付きで挙げられる。対照的に、ハーブやサプリメント、鍼、冷却や運動・ヨガなどの多くは推奨されないと整理されている。ホルモン療法が最も有効な治療であることに変わりはなく、非ホルモン療法は禁忌がある場合や本人が希望しない場合の選択肢となる。"
    condition:
      region: 国際
      study: 北米閉経学会の非ホルモン療法に関する声明（2023年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-854
    source: "The North American Menopause Society. The 2023 nonhormone therapy position statement of The North American Menopause Society. Menopause. 2023;30(6):573-590."
    doi: 10.1097/GME.0000000000002200
    pmid: "37252752"
    pmcid: null
    url: https://doi.org/10.1097/GME.0000000000002200
    source_license: 学会誌掲載で CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "各治療の効果の大きさの数値は抄録になく、主張文には入れていない。フェゾリネタントを含む各薬剤の日本における承認・保険適用の状況（更年期症状への適応の有無を含む）は本出典では確認しておらず未確認である。漢方薬は本声明の評価対象の整理には含まれておらず、日本での位置づけは未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-9-A（更年期障害、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-060
  domain: RP
  subdomain: 日本の避妊の現状とカウンセリング
  assertion:
    plain_statement_ja: "日本では避妊法としてコンドームの使用が突出して多く、経口避妊薬の使用は少ない。全国調査のデータでは、2014年に避妊を実践する女性のうちコンドーム使用は83.4%、経口避妊薬使用は3.0%であり、経口避妊薬の使用率は国の承認の前後でも有意には変わらなかった。先進諸国との差は大きく、生殖年齢の女性が各避妊法の選択肢とその利益を知ることができるよう、医療者が適切な知識を提供することの重要性が指摘されている。"
    condition:
      region: 日本
      study: 日本の全国代表調査（1950〜2014年）に基づく避妊使用の推移の分析
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-855
    source: "Yoshida H, Sakamoto H, Leslie A, Takahashi O, Tsuboi S, Kitamura K. Contraception in Japan: Current trends. Contraception. 2016;93(6):475-477."
    doi: 10.1016/j.contraception.2016.02.006
    pmid: "26872717"
    pmcid: null
    url: https://doi.org/10.1016/j.contraception.2016.02.006
    source_license: 出版社ページ・Crossref に CC ライセンスの表示なし
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "数値は2014年時点の調査に基づくもので、その後の変化（緊急避妊薬の入手方法の見直しや子宮内システムの普及など）は反映されていない。カウンセリングの具体的な手順は本出典では扱っていない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-F（避妊、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-061
  domain: RP
  subdomain: 不育症
  assertion:
    plain_statement_ja: "不育症（反復流産）は、異所性妊娠と胞状奇胎を除く2回以上の妊娠喪失と定義され、カップルの約1〜2%にみられる。原因の評価では、両親の染色体異常などの遺伝的要因、抗リン脂質抗体症候群を含む血栓性素因、甲状腺機能異常などの代謝・内分泌異常、子宮形態異常を調べ、子宮腺筋症の除外には2D超音波が推奨に加えられた。次回妊娠の予後は、女性の年齢と、流産回数・出生歴とその順序を含む妊娠歴全体に基づいて見積もる。治療では、甲状腺抗体が陽性でも甲状腺機能が正常な女性にレボチロキシンを投与すべきではなく、腟プロゲステロンは3回以上の流産歴があり今回の妊娠で性器出血がある女性で出生率を改善する可能性がある。"
    condition:
      region: 欧州
      study: ガイドライン（ESHRE、2022年改訂版・2023年公表）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-856
    source: "ESHRE Guideline Group on RPL; Bender Atik R, Christiansen OB, Elson J, et al. ESHRE guideline: recurrent pregnancy loss: an update in 2022. Human Reproduction Open. 2023;2023(1):hoad002."
    doi: 10.1093/hropen/hoad002
    pmid: "36873081"
    pmcid: PMC9982362
    url: https://doi.org/10.1093/hropen/hoad002
    source_license: CC BY-NC 4.0（PMC ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: "定義と頻度は欧州のガイドラインに基づく。日本の診療指針における不育症の定義（反復流産・習慣流産の区別を含む）や推奨検査項目との照合は未実施である。抗リン脂質抗体症候群に対する低用量アスピリンとヘパリンの併用など個別の治療の詳細は、2022年改訂で変更されなかった2017年版の推奨事項であり、本調査では補足表まで確認していないため主張文には入れていない。レボチロキシンとプロゲステロン製剤の国内承認・保険適用（不育症への適応の有無を含む）は未確認である。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)"
    kokushi: 医学各論 Ⅷ-8-E-⑤（不育症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: RP-062
  domain: RP
  subdomain: 下垂体性無月経
  assertion:
    plain_statement_ja: "下垂体前葉の障害によってゴナドトロピン（LH・FSH）の分泌が低下すると、エストロゲンが低下しているにもかかわらずFSH・LHが上昇しない低ゴナドトロピン性の性腺機能低下となり、無月経を呈する。原因は下垂体の炎症・梗塞・外傷、手術や放射線治療の影響、分娩後の大量出血に伴う下垂体壊死（Sheehan症候群）などであり、他の下垂体ホルモンの欠落を伴うことが多い。評価では血清エストラジオール、FSH、LHを測定し、あわせて朝のコルチゾール、遊離T4とTSH、プロラクチンなど他の下垂体軸も評価する。GnRH負荷試験は診断に有用な情報をもたらさない。閉経後女性では、FSH・LHが高値になっていないこと自体がゴナドトロープ機能障害の診断根拠になる。"
    condition:
      region: 米国
      study: ガイドライン（Endocrine Society、2016年版）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-857
    source: "Fleseriu M, Hashim IA, Karavitaki N, et al. Hormonal Replacement in Hypopituitarism in Adults: An Endocrine Society Clinical Practice Guideline. The Journal of Clinical Endocrinology & Metabolism. 2016;101(11):3888-3921."
    doi: 10.1210/jc.2016-2118
    pmid: "27736313"
    pmcid: null
    url: https://doi.org/10.1210/jc.2016-2118
    source_license: ライセンス表示を確認できず（著者稿は All rights reserved の表示）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: "高プロラクチン血症そのものは別の項目で扱うため本カードの対象外とし、プロラクチンは他軸の評価項目としてのみ挙げた。無月経では妊娠の除外と、甲状腺疾患など排卵障害の他原因の除外が前提になる（ガイドライン推奨1.14）。病因ごとの頻度や下垂体MRIの所見などは本ガイドラインの推奨文で確認した範囲を超えるため主張文には入れていない。本カードには薬剤名は含まれない。"
  curriculum:
    core_curriculum: "PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU)；TBL-02-09-021 (id: JlAKppQ)"
    kokushi: 医学各論 Ⅷ-8-A-②（下垂体性無月経、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応の一覧

| カードID | 出題基準 | コアカリ |
|---|---|---|
| RP-001 | null | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-021 (id: JlAKppQ) |
| RP-002 | null | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU) |
| RP-003 | null | PS-02-10-05 (id: JkxnuSA) |
| RP-004 | 医学各論 Ⅷ-8-D-③（無排卵、b） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-021 (id: JlAKppQ) |
| RP-005 | null | PS-02-10-05 (id: JkxnuSA) |
| RP-006 | null | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-021 (id: JlAKppQ)；TBL-02-09-022 (id: JlAKppU) |
| RP-007 | 医学各論 Ⅷ-8-A-①（視床下部性無月経、a） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU) |
| RP-008 | 医学各論 Ⅷ-8-B-①（希発月経、a） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-021 (id: JlAKppQ) |
| RP-009 | 医学各論 Ⅷ-8-B-②（過多月経、a） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-016 (id: JlAKpo4)；TBL-02-09-021 (id: JlAKppQ) |
| RP-010 | 医学各論 Ⅷ-8-B-③（過少月経、a） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-021 (id: JlAKppQ) |
| RP-011 | 医学各論 Ⅷ-8-C-①（機能性月経困難症、b） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-010 (id: JlAKpoU) |
| RP-012 | 医学各論 Ⅷ-8-C-②（器質性月経困難症、b） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-010 (id: JlAKpoU) |
| RP-013 | 医学各論 Ⅷ-8-D-①（月経前症候群、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-014 | 医学各論 Ⅷ-8-D-①（月経前症候群、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-015 | 医学各論 Ⅷ-8-D-①（月経前症候群、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-016 | 医学各論 Ⅷ-8-D-②（機能性子宮出血、a） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-010 (id: JlAKpoU) |
| RP-017 | 医学各論 Ⅷ-8-D-②（機能性子宮出血、a） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-016 (id: JlAKpo4) |
| RP-018 | 医学各論 Ⅷ-8-D-①（月経前症候群、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-019 | null | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU) |
| RP-020 | null | PS-02-10-05 (id: JkxnuSA) |
| RP-021 | 医学各論 Ⅷ-8-D-③（無排卵、b） | PS-02-10-05 (id: JkxnuSA)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ)；ホルモン測定 TBL-02-09-022 (id: JlAKppU) |
| RP-022 | 医学各論 Ⅷ-8-D-⑥（多囊胞性卵巣症候群<PCOS>、b） | PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY) |
| RP-023 | 医学各論 Ⅷ-8-D-⑥（多囊胞性卵巣症候群<PCOS>、b） | PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU) |
| RP-024 | 医学各論 Ⅷ-8-A-③（卵巣性無月経、b） | PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ) |
| RP-025 | 医学各論 Ⅷ-8-D-⑤（高プロラクチン血症、乳汁漏出症、b） | PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ) |
| RP-026 | 医学各論 Ⅷ-8-D-④（黄体機能不全、b） | PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ) |
| RP-027 | 医学各論 Ⅷ-8-E-①（女性不妊症、a） | PS-02-10-05 (id: JkxnuSA)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY)；ホルモン測定 TBL-02-09-022 (id: JlAKppU) |
| RP-028 | 医学各論 Ⅷ-8-E-①（女性不妊症、a） | PS-02-10-05 (id: JkxnuSA)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY) |
| RP-029 | 医学各論 Ⅷ-8-E-①（女性不妊症、a） | PS-02-10-05 (id: JkxnuSA)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY) |
| RP-030 | 医学各論 Ⅷ-8-E-①（女性不妊症、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-031 | 医学各論 Ⅷ-8-E-①（女性不妊症、a） | PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY) |
| RP-032 | 医学各論 Ⅷ-8-E-①（女性不妊症、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-033 | null | PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU) |
| RP-034 | null | PS-02-10-05 (id: JkxnuSA) |
| RP-035 | null | PS-02-10-05 (id: JkxnuSA)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ) |
| RP-036 | 医学各論 Ⅷ-8-A-④（子宮性無月経、b） | PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU) |
| RP-037 | 医学各論 Ⅷ-8-D-③（無排卵、b） | PS-02-10-05 (id: JkxnuSA)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ) |
| RP-038 | 医学各論 Ⅷ-8-E-①（女性不妊症、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-039 | 医学各論 Ⅷ-8-E-①（女性不妊症、a） | PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；骨盤内臓器と腫瘍の画像診断 TBL-02-09-023 (id: JlAKppY) |
| RP-040 | null | PS-02-10-05 (id: JkxnuSA)；ホルモン測定 TBL-02-09-022 (id: JlAKppU)；月経周期の異常 TBL-02-09-021 (id: JlAKppQ) |
| RP-041 | 医学各論 Ⅷ-8-F（避妊、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-042 | 医学各論 Ⅷ-8-F（避妊、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-043 | 医学各論 Ⅷ-8-F（避妊、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-044 | 医学各論 Ⅷ-8-F（避妊、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-045 | 医学各論 Ⅷ-8-F（避妊、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-046 | null | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU) |
| RP-047 | null | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU) |
| RP-048 | 医学各論 Ⅷ-9-A（更年期障害、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-049 | 医学各論 Ⅷ-9-A（更年期障害、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-050 | 医学各論 Ⅷ-9-A（更年期障害、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-051 | 医学各論 Ⅷ-9-B-①（骨粗鬆症、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-052 | 医学各論 Ⅷ-9-B-①（骨粗鬆症、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-054 | 医学各論 Ⅷ-9-B-②（萎縮性腟炎、b） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-019 (id: JlAKppE)；TBL-02-09-020 (id: JlAKppI) |
| RP-055 | 医学各論 Ⅷ-9-B-③（脂質異常症、b） | PS-02-10-05 (id: JkxnuSA) |
| RP-056 | 医学各論 Ⅷ-9-A（更年期障害、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-058 | null | PS-02-10-05 (id: JkxnuSA) |
| RP-059 | 医学各論 Ⅷ-9-A（更年期障害、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-060 | 医学各論 Ⅷ-8-F（避妊、a） | PS-02-10-05 (id: JkxnuSA) |
| RP-061 | 医学各論 Ⅷ-8-E-⑤（不育症、c） | PS-02-10-05 (id: JkxnuSA) |
| RP-062 | 医学各論 Ⅷ-8-A-②（下垂体性無月経、b） | PS-02-10-05 (id: JkxnuSA)；TBL-02-09-022 (id: JlAKppU)；TBL-02-09-021 (id: JlAKppQ) |

## 4. 未解決事項

- スキーマと接頭辞（担当：取り込み側）：接頭辞 RP は手元のスキーマと domains.yaml に未追加。取り込み時に追加が必要。
- カードのない仕様項目（いずれもレベル b）：Ⅷ-9-B-④（動脈硬化）、Ⅷ-9-B-⑤（冠動脈疾患）。閉経後の心血管リスクとして RP-055 が触れているが、専用カードはない。補完は統合側の判断で次回以降に回せる。
- ライセンス UNKNOWN（担当：取り込み側で出版社ページを再確認）：UNKNOWN が多い（36件。うち StatPearls の章4件は章ページが開けず表示未確認）。OPEN と確認できたのは SRC-812、820、827、834 の4件だけである。
- 薬剤の国内承認・保険適用（担当：取り込み側で PMDA 確認）：RP-011、012、015、023、025、033、034、037、042〜044、049、050、052、054、056、059、061 など薬の名前が出るカードは、各カードの uncertainty に「未確認」と明記した。特にレトロゾールの排卵誘発目的の使用（RP-023・037）と SSRI の PMS・PMDD への使用（RP-015）は、国内では適応外となる可能性を明記した。生殖補助医療の保険適用範囲（RP-031・032）も未確認。
- 版の古さ：RP-011 は SOGC ガイドライン2017年版（2025年改訂版あり）、RP-015 はコクランレビュー2013年版（2024年改訂版あり）、RP-031 は ESHRE 卵巣刺激ガイドライン2020年版（2025年改訂版あり）に基づく。差分の確認は取り込み側。
- 日本の定義・基準との照合が未実施のもの：FIGO の月経周期の閾値、無月経の評価開始年齢、初経の平均年齢（米国データ）、日本の骨粗鬆症の診断基準（RP-051 は薬物療法ガイドラインの管理原則に基づく構成）、日本の避妊の使用率（RP-060 は2014年時点の調査）、日本の診療指針における不育症の定義と推奨検査（RP-061 は ESHRE ガイドライン2022年改訂版に基づく）。
- 数値を入れなかった項目：GnRH のパルス頻度、子宮内膜の厚さ、年齢別の卵胞数、プロラクチンの正常化率、卵管手術後の妊娠率、卵子凍結の年齢別出生率、不妊原因の割合、方法別の個別妊娠率、血栓症リスクの大きさ、HRT の用量、薬剤別の骨折抑制効果、下垂体性無月経の病因ごとの頻度などは、確認できた一次資料の範囲になく、定性的な記述にとどめた（各カードの uncertainty に明記）。

## 5. 次回への引き継ぎ

- 欠番：RP-053（骨盤臓器脱。第18回 GY-056 と重なるため削除）、RP-057（心的外傷への配慮。第19回の範囲外のため削除）。ID と SRC 番号は詰めていない。未使用 SRC：SRC-824、851、853、858〜870。
- これで腎・泌尿器・生殖器（第15〜19回）は一通りそろった。第15回68件、第16回72件、第17回73件、第18回62件、第19回60件の合計335件。
- 残る補完候補：Ⅷ-9-B-④・⑤ の専用カード化、卵巣癌の外科治療（第18回 GY-038 の補完）、子宮頸がん検診・HPV ワクチンの日本の最新制度の確認（第18回 GY-015・016）。
- 扱った出典の中心：FIGO の月経異常の分類、ESHRE・ASRM・ACOG・Endocrine Society の指針、国際 PCOS ガイドライン、WHI、コクランレビュー。
