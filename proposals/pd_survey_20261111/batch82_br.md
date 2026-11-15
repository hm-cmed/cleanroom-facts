# バッチ82：BR（乳腺疾患）章 12件

## 集計

- A（置き換え可）：0件
- B（裏づけ追加可）：10件（全面0・部分10）
- C（見つからない）：2件
- D（マスター区分訂正）：11出典（すべて UNKNOWN→RESTRICTED）

## 手続き注記

- 判定は2026-11-11のレポジトリ側指示（新ルール）に基づく。「抄録・添付文書・医学百科は根拠にしない」。使えるのは政府の全文文書・報告書、CC BY 全文、試験登録レコードなど全文で読める資料のみとし、抄録は数値の食い違い確認にのみ用いた。旧来の「先例に基づく A」は廃止。
- 主出典12件すべてについて、PMID・DOIを Europe PMC と Crossref で個別に照合し、マスター・カードとの不一致がないことを確認した。識別子の誤記は本バッチでは発見されなかった。マスターで PMCID が null の主出典のうち SRC-1024・SRC-1025 は Europe PMC で PMCID を持つことを個別に確認し、識別子補完候補とした。他の主出典は PMCID を持たない（StatPearls 3章は Bookshelf ID が対応物）。
- 候補はいずれも全文を実際に読んで裏づけ範囲を判定した。ライセンスは候補ごとに Crossref の版（version of record）データと Europe PMC のライセンス要素の双方で個別に確認した。
- 主出典の区分確認：SRC-1025（Obstet Gynecol Sci 2013）は Crossref・Europe PMC の双方で CC BY-NC 3.0 を確認し、現行の RESTRICTED が正しい。残り11件は UNKNOWN のまま非自由であり、RESTRICTED への訂正候補とした（区分訂正（D）候補の節参照）。SRC-1019（Keio J Med 2025）は J-STAGE で無償閲覧できるが CC 表示はなく、自由とはみなさない（バッチ75 SRC-3343 の先例と同扱い）。
- NCBI の Bookshelf ページはブラウザ・curl ともに reCAPTCHA で直接開けなかったため、StatPearls 3章と Bookshelf の対応は NCBI E-utilities（efetch の bookaccession）で個別に確認し、書籍単位のライセンス表示は同書の図版ページのウェブ検索クロールで確認した。本バッチでは API のレート制限（429）は発生しなかった。

## 明細

| 対象 | 判定 | 現行出典（主出典） | 候補 | 区分 | PMID | DOI | PMCID | ライセンス根拠URL | 裏づけ範囲 | 数値照合 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BR-001 | C | SRC-1011 Miyashita M, Kumamaru H, Niikura N, et al. Annual report of the Japanese Breast Cancer Registry for 2019. Breast Cancer. 2024;31(1):16-23 | なし | — | — | — | — | — | 2019年登録の数値（98,300例・診断時年齢中央値61歳・閉経前30.6%・stage 0 15.0%・stage I 44.8%）を再掲する自由な全文は見つからなかった | — | 別年度の登録報告は CC BY で全文が読めるが（2021年報告 Konishi 2025・2018年報告 Tada 2023・2016年報告 Kubo 2020）、数値は年度ごとに異なり2019年の値の裏づけにはならない。主出典は非OAで RESTRICTED への訂正対象（D） |
| BR-002 | B（部分） | SRC-1012 Hamashima C, et al; Japanese Research Group for the Development of the Breast Cancer Screening Guidelines. The Japanese Guidelines for Breast Cancer Screening. Jpn J Clin Oncol. 2016;46(5):482-492 | Katsika L, Boureka E, Kalogiannidis I, Tsakiridis I. Screening for Breast Cancer: A Comparative Review of Guidelines. Life (Basel). 2024;14(6):777 | CC BY 4.0（OPEN） | 38929759 | 10.3390/life14060777 | PMC11204612 | https://creativecommons.org/licenses/by/4.0/ | 部分：日本のガイドラインが40歳からのマンモグラフィ開始に同意していること、超音波については精度とデータ不足への疑問が示されていることを再掲する | 乳癌死亡の相対リスク 0.75 は候補に再掲なし | 40–74歳の年齢帯、40–64歳での視触診併用の推奨、視触診単独と超音波を対策型に推奨しない点、害（被曝・偽陽性・過剰診断）は再掲なし。主出典は非OAで RESTRICTED への訂正対象（D） |
| BR-005 | B（部分） | SRC-1015 Sakai T, Kutomi G, Shien T, et al. The Japanese Breast Cancer Society Clinical Practice Guidelines for Surgical Treatment of Breast Cancer, 2022 Edition. Breast Cancer. 2024;31(1):1-7 | Yamamoto Y, Yamauchi C, Toyama T, et al. The Japanese Breast Cancer Society Clinical Practice Guidelines for Breast Cancer, 2022 Edition. Breast Cancer. 2024;31(3):340-346 | CC BY 4.0（OPEN） | 38570435 | 10.1007/s12282-024-01566-6 | PMC11045566 | https://creativecommons.org/licenses/by/4.0/ | 部分：2022年版ガイドラインの構成（治療編に外科療法を含む）と、Minds の診療ガイドライン作成マニュアルに基づく開発過程を再掲する | 数値の主張なし | 外科領域の4区分（乳房・腋窩・再建・再発転移）と術前化学療法後の腋窩マネジメントの大改訂の詳細は再掲なし。主出典は非OAで RESTRICTED への訂正対象（D） |
| BR-009 | B（部分） | SRC-1019 Seki T, Kobayashi Y, Masuda K, et al. Exploring Breast Cancer Risk Management in HBOC Patients: Image Surveillance Versus Risk-reducing Surgery. Keio J Med. 2025;74(3):130-137 | Ohashi A, Förnvik D, Bengtsson Y, Zackrisson S, et al. Advances in Risk Management and Screening for Women at Increased Risk of Breast Cancer: The Role of Magnetic Resonance Imaging. Magn Reson Med Sci. 2025;24(3):403-418；Park YH, Lee SC, Singer CF, et al. Part II: consensus statements and expert recommendations for BRCA-associated breast cancer in the Asia-Pacific region. Front Oncol. 2025;15:1507840 | CC BY 4.0（OPEN） | 41083355／40626017 | 10.2463/mrms.rev.2025-0056／10.3389/fonc.2025.1507840 | PMC12536305／PMC12230081 | https://creativecommons.org/licenses/by/4.0/ | 部分：Ohashi は BRCA1・BRCA2 の80歳までの累積生涯リスク（72%・69%）、BRCA1 ではトリプルネガティブが多く BRCA2 ではルミナルが多いこと、25歳または30歳からの年1回 MRI サーベイランスを再掲する。Park はリスク低減乳房切除によるリスク低下 90–95% を再掲する | カードの生涯リスク範囲 48–76% そのものは再掲なし（候補の 72%・69% は範囲内だが別集団・別定義の値）。リスク低減乳房切除の低下幅は候補 90–95% で、カードの「90%以上低下」と整合する | 一般集団の生涯リスク約11%と、2020年から HBOC 診療の一部が保険適用になった点は再掲なし。主出典は J-STAGE で無償閲覧できるが CC 表示がなく RESTRICTED への訂正対象（D） |
| BR-010 | B（部分） | SRC-1020 Mitchell KB, Johnson HM, Rodríguez JM, et al. Academy of Breastfeeding Medicine Clinical Protocol #36: The Mastitis Spectrum, Revised 2022. Breastfeed Med. 2022;17(5):360-376 | Douglas P. Does the Academy of Breastfeeding Medicine's Clinical Protocol #36 'The Mastitis Spectrum' promote optimal care? Int Breastfeed J. 2023;18(1):51 | CC BY 4.0（OPEN） | 37670315 | 10.1186/s13006-023-00588-8 | PMC10481477 | https://creativecommons.org/licenses/by/4.0/ | 部分：プロトコル第36番の文言を帰属明示で引用し、乳管狭窄から炎症性乳腺炎を経て細菌性乳腺炎へ進むスペクトラムの並びと、蜂窩織炎・膿瘍の位置づけを再掲する | 数値の主張なし | 候補はプロトコルへの批判的論考であり、裏づけになるのは主出典からの引用部分に限る（候補の批判的立場そのものは裏づけに含めない）。主出典は非OAで RESTRICTED への訂正対象（D） |
| BR-011 | B（部分） | SRC-1021 Li A, Kirk L. Intraductal Papilloma. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing | Rella R, Romanucci G, Arciuolo D, Scaldaferri F, et al. Multiple Papillomas of the Breast: A Review of Current Evidence and Challenges. J Imaging. 2022;8(7):198 | CC BY 4.0（OPEN） | 35877642 | 10.3390/jimaging8070198 | PMC9315766 | https://creativecommons.org/licenses/by/4.0/ | 部分：中枢型（単発・乳頭近傍、乳頭分泌を伴い血性を含む）と末梢型（多発・末梢乳管）の区別、生検での過小評価と異型の評価、切除が推奨される一方で吸引補助切除で完全除去された例では経過観察も選択肢になることを再掲する | 数値の主張なし（候補の切除後アップグレード率 3.3–10.2% は BR-017 の主出典の統合値とは別物） | 主出典は StatPearls の章。書籍全体の配布条件は CC BY-NC-ND 4.0 で自由ではなく、RESTRICTED への訂正対象（D）。マスターの license_note「ライセンス表示を確認できず」は実態と異なる（申し送り参照） |
| BR-012 | B（部分） | SRC-1022 Ajmal M, Khan M, Van Fossen K. Breast Fibroadenoma. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing | Ramala SR, Chandak S, Chandak MS, Annareddy S. A Comprehensive Review of Breast Fibroadenoma: Correlating Clinical and Pathological Findings. Cureus. 2023;15(12):e49948 | CC BY 4.0（OPEN） | 38179396 | 10.7759/cureus.49948 | PMC10765224 | https://creativecommons.org/licenses/by/4.0/ | 部分：若年女性に多いこと（好発は15–35歳）、境界明瞭で可動性のある滑らかな腫瘤という触診像、葉状腫瘍・乳癌との鑑別の考え方、小さい例では経過観察が可能で大きな・症状のある例では切除を検討することを再掲する | 数値の主張なし | 針生検を組み合わせた診断手順の細部は再掲が弱い。主出典は StatPearls の章（CC BY-NC-ND 4.0）で RESTRICTED への訂正対象（D）。license_note については申し送り参照 |
| BR-013 | B（部分） | SRC-1023 Malherbe K, Szymanski KD. Fibrocystic Breast Disease. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing | Sosnowska-Sienkiewicz P, Januszkiewicz-Lewandowska D, Małdyk J, et al. Benign and malignant breast lesions in children and adolescents - diagnostic and therapeutic approach. Front Pediatr. 2024;12:1417050 | CC BY 4.0（OPEN） | 39507494 | 10.3389/fped.2024.1417050 | PMC11537988 | https://creativecommons.org/licenses/by/4.0/ | 部分：線維嚢胞性変化が嚢胞・線維化・しこりを伴う良性変化の総称であること、乳房痛や乳頭分泌を伴いうること、画像で評価すること、多くの例で積極的治療は不要であることを再掲する | 数値の主張なし | 候補は小児・思春期を対象とする総説で、性ホルモン変動との関連の明示はない。成人女性での「画像で悪性でないことの確認が重要」「典型例では過剰介入は不要」という点は部分的な再掲にとどまる。主出典は StatPearls の章（CC BY-NC-ND 4.0）で RESTRICTED への訂正対象（D） |
| BR-014 | B（部分） | SRC-1024 Niewoehner CB, Schorer AE. Gynaecomastia and breast cancer in men. BMJ. 2008;336(7646):709-713 | Ionescu S, Nicolescu AC, Marincas M, Madge OL, et al. An Update on the General Features of Breast Cancer in Male Patients - A Literature Review. Diagnostics (Basel). 2022;12(7):1554 | CC BY 4.0（OPEN） | 35885460 | 10.3390/diagnostics12071554 | PMC9323942 | https://creativecommons.org/licenses/by/4.0/ | 部分：女性化乳房が男性乳房腫大の一般的な原因であること、エストロゲン/アンドロゲン比を変える病態が関与すること、女性化乳房と癌の鑑別が必須で疑わしい場合は画像と組織学的確認を行うことを再掲する | カードの「癌は約1%」は再掲なし（候補にある 1% は全乳癌に占める男性乳癌の割合で、別の統計） | 思春期・高齢期の生理的変化や薬剤性といった原因の列挙は再掲なし。主出典は PMC 収載（PMC2276281）だがライセンス表示がなく自由ではない（RESTRICTED への訂正対象 D、識別子補完候補あり） |
| BR-015 | B（部分） | SRC-1025 Yu JH, Kim MJ, Cho H, et al. Breast diseases during pregnancy and lactation. Obstet Gynecol Sci. 2013;56(3):143-159 | de Holanda AA, Gonçalves AK, de Medeiros RD, de Oliveira AMA, et al. Ultrasound findings of the physiological changes and most common breast diseases during pregnancy and lactation. Radiol Bras. 2016;49(6):389-396 | CC BY 4.0（OPEN） | 28057965 | 10.1590/0100-3984.2015.0076 | PMC5210035 | https://creativecommons.org/licenses/by/4.0/ | 部分：妊娠・授乳期の生理的変化のために画像診断が難しくなること、乳腺炎・膿瘍、乳瘤、授乳期腺腫といった良性疾患が多いこと、妊娠関連乳癌も生じうること、疑わしい画像所見ではマンモグラフィや生検を行うことを再掲する | 数値の主張なし | 主出典 SRC-1025 自体は CC BY-NC 3.0 で現行の RESTRICTED が正しい（Dなし）。主出典の PMCID 補完候補あり |
| BR-017 | B（部分） | SRC-1521 Zhang X, Liu W, Hai T, Li F. Upgrade Rate and Predictive Factors for Breast Benign Intraductal Papilloma Diagnosed at Biopsy: A Meta-Analysis. Ann Surg Oncol. 2021;28(13):8643-8650 | Elfgen C, Leo C, Kubik-Huch RA, et al. Third International Consensus Conference on lesions of uncertain malignant potential in the breast (B3 lesions). Virchows Arch. 2023;483(1):5-20 | CC BY 4.0（OPEN） | 37330436 | 10.1007/s00428-023-03566-x | PMC10326140 | https://creativecommons.org/licenses/by/4.0/ | 部分：乳頭腫を含む乳頭状病変のスペクトラム（異型合併例を含む）と、吸引補助切除で完全除去された乳頭状病変では画像サーベイランスが外科切除に代わりうるという管理原則を再掲する | カードの統合値（良性乳頭腫 約5.0%・異型合併 約36.0%）と予測因子（血性分泌・末梢型・触知可能・1cm以上）は再掲なし。別の CC BY データ（Heindl 2025）は乳頭腫と放射状瘢痕の混合群で 4.3% とし定義が異なるため数値の裏づけには使わない | 主出典は非OAで RESTRICTED への訂正対象（D） |
| BR-019 | C | SRC-1523 Bennett DL, Buckley A, Lee MV. Fibrocystic Change. Radiol Clin North Am. 2024;62(4):581-592 | なし | — | — | — | — | — | 嚢胞・層状石灰化など典型的良性所見では不要な経過観察・生検を避けられること、腫瘤・層状でない石灰化・構築の乱れでは針生検が必要という画像トリアージを全文で再掲する自由な資料は見つからなかった | — | 線維嚢胞性変化の画像所見に特化した CC BY 全文は見当たらず、BR-013 の候補（小児対象の総説）は石灰化・構築の乱れの判定を扱わない。主出典は非OAで RESTRICTED への訂正対象（D） |

## 区分訂正（D）候補

- SRC-1011（BR-001、現行 UNKNOWN → RESTRICTED）：Crossref にはテキストマイニング用リンクのみでライセンス表示がなく、Europe PMC でも非OA。無償で読める全文は確認できなかった。
- SRC-1012（BR-002、現行 UNKNOWN → RESTRICTED）：ライセンス表示がなく非OA。
- SRC-1015（BR-005、現行 UNKNOWN → RESTRICTED）：Crossref はテキストマイニング用リンクのみ、Europe PMC でも非OA。
- SRC-1019（BR-009、現行 UNKNOWN → RESTRICTED）：Unpaywall・OpenAlex では J-STAGE で無償閲覧できる（いわゆる diamond OA）とされるが、誌面・J-STAGE のいずれにもライセンス表示がない。無償閲覧可でも CC 表示がなければ自由とはみなさない。
- SRC-1020（BR-010、現行 UNKNOWN → RESTRICTED）：Crossref はテキストマイニング用リンクのみ、非OA。
- SRC-1021（BR-011、現行 UNKNOWN → RESTRICTED）：StatPearls 書籍（Bookshelf NBK519539 に対応）は書籍単位で CC BY-NC-ND 4.0 の表示があり自由ではない。マスターの license_note「ライセンス表示を確認できず」は実態と異なるため、注記の更新もあわせて提案する。
- SRC-1022（BR-012、現行 UNKNOWN → RESTRICTED）：同上（Bookshelf NBK535345 に対応、書籍単位で CC BY-NC-ND 4.0）。
- SRC-1023（BR-013、現行 UNKNOWN → RESTRICTED）：同上（Bookshelf NBK551609 に対応、書籍単位で CC BY-NC-ND 4.0）。
- SRC-1024（BR-014、現行 UNKNOWN → RESTRICTED）：PMC に収載される（PMC2276281）がライセンス表示がなく、Europe PMC でも非OA扱いで自由ではない。
- SRC-1521（BR-017、現行 UNKNOWN → RESTRICTED）：Crossref はテキストマイニング用リンクのみ、非OA。
- SRC-1523（BR-019、現行 UNKNOWN → RESTRICTED）：Elsevier 誌で STM・テキストマイニング用リンクのみ、ライセンス表示なし。
- SRC-1025（BR-015）は Crossref・Europe PMC の双方で CC BY-NC 3.0 を確認し、現行の RESTRICTED が正しいため訂正対象に含めない。

## 識別子補完候補

- SRC-1024：PMCID = PMC2276281（マスターは null）。PMCID をキーに個別照会し、PMID 18369226・DOI 10.1136/bmj.39511.493391.BE の当該論文であることを確認した。PMC 版はライセンス表示なしで、区分は RESTRICTED への訂正対象のままである。
- SRC-1025：PMCID = PMC3784111（マスターは null）。PMCID をキーに個別照会し、PMID 24327995・DOI 10.5468/ogs.2013.56.3.143 の当該論文であることを確認した。刊行版は CC BY-NC 3.0 で区分は RESTRICTED のままである。

## 申し送り

- StatPearls 3章（SRC-1021・1022・1023）のマスター license_note は「ライセンス表示を確認できず」とされているが、Bookshelf 上の StatPearls 書籍には書籍単位で CC BY-NC-ND 4.0 の表示がある。区分は RESTRICTED が妥当であり、license_note の更新を提案する。なお StatPearls は従来ルールでも原則として出典にしない二次資料であり、BR-011・BR-012・BR-013 の主出典そのものの付け替えはレポジトリ側の判断事項として残る。
- BR-001 は C とした。別年度の乳癌登録報告（2021年報告 Konishi 2025 など）は CC BY で全文が読めるが、登録数・病期分布は年度ごとに異なるため、カードの2019年の数値の裏づけには使えない。
- BR-014 の候補（Ionescu 2022）にある「1%」は全乳癌に占める男性乳癌の割合であり、カードの「男性乳房腫大のうち癌は約1%」とは別の統計である。混同しないよう明細に明記した。
- BR-010 の候補（Douglas 2023）は主出典であるプロトコル第36番への批判的論考だが、プロトコルの文言を帰属明示で引用しており、その引用範囲がカードのスペクトラム記述を再掲する。裏づけとして使う場合は引用部分に限ること。
- BR-017 のカードの統合値（5.0%・36.0%）と予測因子の組を再掲する CC BY 全文は見つからなかった。裏づけは B3 病変コンセンサス（Elfgen 2023）の管理原則にとどまる。
- 主出典12件すべての PMID・DOI を個別照会し、マスター・カードとの不一致はなかった。SRC-1521 もマスターに PMID・DOI の登録があり、個別照会の値と一致した。本バッチでは主出典・候補とも識別子の誤記は発見されなかった。
- NCBI の Bookshelf ページは reCAPTCHA のため直接開けず、StatPearls 3章の Bookshelf ID の対応は NCBI E-utilities で確認した。本バッチでは API のレート制限（429）は発生しなかった。
- 本バッチの判定は以上で完結しており、カードの主張・数値の変更は一切行っていない。
