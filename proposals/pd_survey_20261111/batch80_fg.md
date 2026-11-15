# バッチ80：FG（真菌・寄生虫）章 14件

## 集計

- A（置き換え可）：0件
- B（裏づけ追加可）：13件（部分12・全面1）
- C（見つからない）：1件
- D（マスター区分訂正）：4出典（いずれも UNKNOWN → RESTRICTED）

## 手続き注記

- 判定は2026-11-11のレポジトリ側指示（新ルール）に基づく。「抄録・添付文書・医学百科は根拠にしない」。使えるのは政府の全文文書・報告書、CC BY 全文、試験登録レコードなど全文で読める資料のみとし、抄録は数値の食い違い確認にのみ用いた。旧来の「先例に基づく A」は廃止。
- 主出典13件（FG-002とFG-004は同一出典）すべてについて、PMID・DOIを Europe PMC と Crossref で個別に照合し、マスターとの不一致がないことを確認した。識別子の誤記は本バッチでは発見されなかった。
- 候補はいずれも全文を実際に読んで裏づけ範囲を判定した。ライセンスは候補ごとに Crossref の版（version of record）データと Europe PMC のライセンス要素の双方で個別に確認した。
- 主出典の区分確認：RESTRICTED とされていた9出典（SRC-1435・2152・2153・2159・2162・2164・2165・2166・2170）は個別確認の結果いずれも正しい。SRC-2164（Open Forum Infect Dis）は刊行版が CC BY-NC-ND であり自由ではない。SRC-2159（WHO世界マラリア報告2024）は CC BY-NC-SA 3.0 IGO であり自由ではない。
- CDC DPDx ページ（FG-016の候補）の本文確認は、CDC ページのクロール済みミラーコピー（www.cdc.gov/dpdx/amebiasis/tx.html の取得コピー）で行った。明細のURLはCDCの公式URLを記載した。
- 本バッチでは API のレート制限（429）は発生しなかった。

## 明細

| 対象 | 判定 | 現行出典（主出典） | 候補 | 区分 | PMID | DOI | PMCID | ライセンス根拠URL | 裏づけ範囲 | 数値照合 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FG-001 | B（部分） | SRC-1435 Pappas PG, Kauffman CA, Andes DR, et al. Clinical Practice Guideline for the Management of Candidiasis: 2016 Update by the Infectious Diseases Society of America. Clin Infect Dis. 2016;62(4):e1-e50. | Mallick DC, Kaushik N, Goyal L, Mallick L, Singh P. A Comprehensive Review of Candidemia and Invasive Candidiasis in Adults: Focus on the Emerging Multidrug-Resistant Fungal Pathogens. Diseases. 2025;13(4):93. | CC BY 4.0（OPEN） | 40277804 | 10.3390/diseases13040093 | PMC12026337 | https://creativecommons.org/licenses/by/4.0/ | 部分：2016年IDSAガイドラインの存在を明記し、それに基づくカンジダ血症・侵襲性カンジダ症の管理枠組み（初期治療・移行・治療期間）を再掲する | 数値の主張なし（ガイドラインの存在と範囲） | 主出典は RESTRICTED で確定（PMC版は非OAでライセンス表示なし）。CDCの Clinical Overview of Invasive Candidiasis ページ（GOV_US）も同ガイドライン準拠の治療を掲載するが2016年改訂自体は明記しないため、候補はCC BYレビューを採った |
| FG-002 | B（部分） | SRC-2152 Denning DW. Global incidence and mortality of severe fungal disease. Lancet Infect Dis. 2024;24(7):e428-e438. | Finkina EI, Shevchenko OV, Gerasimova AA, Fateeva SI, Balandin SV, Ovchinnikova TV. WHO Critical Priority Fungi: A Comprehensive Review of Antifungal Resistance, Emerging Therapeutic Strategies, and the Potential of Antifungal Peptides. Int J Mol Sci. 2026;27:8141. | CC BY 4.0（OPEN） | 42794569 | 10.3390/ijms27188141 | PMC13607290 | https://creativecommons.org/licenses/by/4.0/ | 部分：カンジダ血症・侵襲性カンジダ症の年間新規症例数と死亡数を主出典（Denning 2024）を引いて再掲する | 死亡数995,000人は一致。症例数は候補が「およそ150万件」と概数化（カード1,565,000件）。死亡割合63.6%は候補に記載なし | FG-004と同一候補 |
| FG-003 | B（部分） | SRC-2153 Latgé JP, Chamilos G. Aspergillus fumigatus and Aspergillosis in 2019. Clin Microbiol Rev. 2019;33(1):e00140-18. | Corrêa-Junior D, Zamith-Miranda D, Frases S, Nosanchuk JD. From the Ground to the Clinic: The Evolution and Adaptation of Fungi. J Fungi. 2025;12(1):8. | CC BY 4.0（OPEN） | 41590420 | 10.3390/jof12010008 | PMC12842708 | https://creativecommons.org/licenses/by/4.0/ | 部分：腐生性（腐敗植生）の環境生息、耐熱性（約50℃）が宿主内生存を可能にする重要な病原因子であること、肺感染・侵襲性アスペルギルス症の原因であることを再掲する | 耐熱温度（約50℃）は一致 | 「主たる生息地は土壌」の点は候補では腐敗植生・環境リザーバーとしての記載にとどまる。主出典は RESTRICTED で確定（PMC収載は著者稿でライセンス表示なし） |
| FG-004 | B（部分） | SRC-2152 Denning DW. Global incidence and mortality of severe fungal disease. Lancet Infect Dis. 2024;24(7):e428-e438. | Finkina EI, Shevchenko OV, Gerasimova AA, Fateeva SI, Balandin SV, Ovchinnikova TV. WHO Critical Priority Fungi: A Comprehensive Review of Antifungal Resistance, Emerging Therapeutic Strategies, and the Potential of Antifungal Peptides. Int J Mol Sci. 2026;27:8141. | CC BY 4.0（OPEN） | 42794569 | 10.3390/ijms27188141 | PMC13607290 | https://creativecommons.org/licenses/by/4.0/ | 部分：侵襲性アスペルギルス症の年間罹患者数（210万人超）と死亡率（85%超）を再掲する | 罹患者数・死亡率は概ね一致（カード2,113,000人超・85.2%）。死亡絶対数約1,801,000人は候補に記載なし | リスク文脈（COPD・ICU・肺がん・血液悪性腫瘍）の列挙は候補で確認できなかった。FG-002と同一候補 |
| FG-007 | C | SRC-2156 Nakamura K, Fukuda T. 2021 Epidemiological Survey of Dermatomycoses in Japan. Med Mycol J. 2023;64(4):85-94. | なし | — | — | — | — | — | 日本の全国調査（2021年）の数値（全数調査参加率62.1%、剖検例の深在性真菌症4.2%等）を再掲する自由な全文は見つからなかった | — | 主出典は区分訂正（D）の対象。下記の申し送りも参照 |
| FG-008 | B（部分） | SRC-2157 Edman JC, Kovacs JA, Masur H, Santi DV, Elwood HJ, Sogin ML. Ribosomal RNA sequence shows Pneumocystis carinii to be a member of the fungi. Nature. 1988;334(6182):519-522. | Jaramillo Cartagena A, Asowata OE, Ng D, Babady NE. An overview of the laboratory diagnosis of Pneumocystis jirovecii pneumonia. J Clin Microbiol. 2025;63(5):e00361-24. | CC BY 4.0（OPEN） | 39898657 | 10.1128/jcm.00361-24 | PMC11898755 | https://creativecommons.org/licenses/by/4.0/ | 部分：当初は原虫に分類され激しい議論があったこと、1988年に配列データにより子嚢菌類の真菌へ再分類されたこと（主出典Edman 1988を引用）、シスト（ascus）と栄養型の二型を持つことを再掲する | 再分類の年（1988年）は一致 | 生活環の「シスト内に8個の小体」の点は候補に再掲がない。主出典は区分訂正（D）の対象 |
| FG-010 | B（部分） | SRC-2159 World Health Organization. World malaria report 2024: addressing inequity in the global malaria response. Geneva: World Health Organization; 2024. ISBN 978-92-4-010444-0（電子版） | Tague C, Akilimali A, Makeda D, Yokolo H, Ekouo J, Cebweru Murhola G, Domga J, Silatchom Kamgang J, Koba Mjumbe C. Malaria Elimination in Suriname, Timor-Leste and Georgia: Strategic Lessons for Sub-Saharan Africa. J Trop Med. 2026;2026:2927281. | CC BY 4.0（OPEN） | 42688838 | 10.1155/jotm/2927281 | PMC13537102 | https://creativecommons.org/licenses/by/4.0/ | 部分：2023年の推計症例数2億6,300万件・死亡数59.7万人、アフリカ地域の割合（症例94%・死亡95%）を再掲する | 4数値とも一致 | 前年比（症例+1,100万件・死亡は横ばい）と2000年以降の回避累計（症例22億件・死亡1,270万人）は候補に再掲がない。主出典は CC BY-NC-SA 3.0 IGO のため RESTRICTED のままで正しい |
| FG-012 | B（部分） | SRC-2161 Gaitanis G, Magiatis P, Hantschke M, Bassukas ID, Velegraki A. The Malassezia genus in skin and systemic diseases. Clin Microbiol Rev. 2012;25(1):106-141. | Sellera FP, Ollhoff RD, Pogliani FC. "Malassezia" [mal″ə-sē′zhə]（Etymologia）. Emerg Infect Dis. 2025;31(10):2063. | GOV_US（OPEN、米国政府刊行物でpublic domain。本文にその旨の明記あり。Europe PMCのライセンス要素も cc by） | なし（Europe PMCレコードにPMIDなし） | 10.3201/eid3110.221743 | PMC12483015 | https://doi.org/10.3201/eid3110.221743 | 部分：この属が現在18種を含むことと、癜風（pityriasis versicolor）との関連を再掲する | 現行の種数18は主出典の「2012年時点で14種」と時点の異なる更新値であり、不一致ではない | 1996年に7種へ再整理された経緯と2012年時点の14種という数値は候補に再掲がない。主出典は区分訂正（D）の対象 |
| FG-013 | B（部分） | SRC-1190 Barros MBL, de Almeida Paes R, Schubach AO. Sporothrix schenckii and Sporotrichosis. Clin Microbiol Rev. 2011;24(4):633-654. | Cunha-E-Silva RR, Bedoya-Pacheco SJ, Vasconcelos AO, Magalhães MAFM, Dias CMG, Freitas DFS, Pereira SA, Figueiredo ABF, Reis JGD, Almeida PMP, Alzuguir CLC, Oliveira LFA, Pimentel MIF. Temporal tendencies and spatial patterns of human sporotrichosis in Rio de Janeiro State, Brazil, 2007 to 2023. Rev Inst Med Trop Sao Paulo. 2026;68:e2. | CC BY 4.0（OPEN） | 41637341 | 10.1590/s1678-9946202668002 | PMC12858175 | https://creativecommons.org/licenses/by/4.0/ | 部分：汚染された有機物の創傷性植込みによる古典的感染（「バラ園芸家の病気」）、猫の掻傷・咬傷による動物原性感染、1990年代後半以降リオデジャネイロが動物原性流行の中心であることを再掲する | 流行の症例数（ヒト2,000例超・動物3,000例超）は候補に再掲がない | 隠蔽種・種複合体の点は別のCC BY論文（Brunner-Mendoza C, et al. Cryptic Diversity and Ecological Overlap in Sporothrix schenckii. J Fungi. 2025;11(11):759. PMCID PMC12653030）が裏づける。主出典は区分訂正（D）の対象 |
| FG-014 | B（部分） | SRC-2162 Hochberg NS, Hamer DH. Anisakidosis: Perils of the deep. Clin Infect Dis. 2010;51(7):806-812. | González-Fernández J, Cuéllar C, Daschner A, Nieuwenhuizen NE. Anisakiasis: A Decade of Molecular and Diagnostic Advancements (2015-2026). Int J Mol Sci. 2026;27(14):6456. | CC BY 4.0（OPEN） | 42511799 | 10.3390/ijms27146456 | PMC13410091 | https://creativecommons.org/licenses/by/4.0/ | 部分：胃型・腸型・異所性（腹腔外）型の症候型分類とアレルギー型（胃アレルギー性アニサキス症を含む）、内視鏡的摘出が標準治療であること、合併症時の外科的切除、アニサキス特異的IgE検査を再掲する | 数値の主張なし | 「死んだ幼虫でもアレルギーを起こしうる」点は近年の文献で見解が分かれる（下記の申し送り参照）。主出典の記述を優先しカードは変更しない |
| FG-016 | B（部分） | SRC-2164 Shirley DT, Farr L, Watanabe K, Moonah S. A review of the global burden, new diagnostics, and current therapeutics for amebiasis. Open Forum Infect Dis. 2018;5(7):ofy161. | CDC DPDx "Amebiasis" Treatment Information（米国疾病予防管理センター） | GOV_US（OPEN） | — | — | — | https://www.cdc.gov/dpdx/amebiasis/tx.html | 部分：症候性の腸管疾患または肝膿瘍等の腸管外感染ではメトロニダゾールまたはチニダゾールを第一選択とし、直後にパロモマイシンまたはヨードキノールによる治療を引き継ぐ二段構えを明記する | 数値の主張なし | 「ニトロイミダゾール単独ではシストを根絶できない」理由づけはCDCページに逐語的にはない。主出典自体は刊行版が CC BY-NC-ND のため RESTRICTED で正しい |
| FG-017 | B（部分） | SRC-2165 Montoya JG, Liesenfeld O. Toxoplasmosis. Lancet. 2004;363(9425):1965-1976. | Borráz-León JI, Rantala MJ, Krams I, Maestripieri D. Wealth, health, cats and Toxoplasma gondii: An ecological correlational study of subjective well-being and self-esteem. PLoS One. 2026;21(9):e0357911. | CC BY 4.0（OPEN） | 42814692 | 10.1371/journal.pone.0357911 | PMC13626322 | https://creativecommons.org/licenses/by/4.0/ | 部分：猫の糞便中オーシストと加熱不十分な汚染食肉による感染経路、健常者では感染しても多くが無症状であること、成人の感染率（約10〜30%）を再掲する | 感染率は候補の約10〜30%で、カードの「最大で世界の成人の約3分の1」と概ね一致 | 免疫不全での再活性化による致死的脳炎の点は候補に再掲がない。妊娠時の胎児影響は候補では先天性感染のスクリーニング文脈のみ |
| FG-018 | B（部分） | SRC-2166 Dold C, Holland CV. Ascaris and ascariasis. Microbes Infect. 2011;13(7):632-637. | Wang T, Tan Q, Wu Q, Chen Y, Zhou Q, Luo X. Ascariasis in a child with recurrent gastrointestinal hemorrhage: case report and literature review. Front Pediatr. 2025;13:1712272. | CC BY 4.0（OPEN） | 41488892 | 10.3389/fped.2025.1712272 | PMC12756500 | https://creativecommons.org/licenses/by/4.0/ | 部分：世界の感染者推計（12億人、その40%が小児）と、重感染では重篤な合併症に至りうることを再掲する | 感染者数12億人は一致 | 「感染が少数の宿主に偏る過分散（偏在）」そのものは候補に記載がない |
| FG-022 | B（全面） | SRC-2170 Adam RD. Giardia duodenalis: Biology and pathogenesis. Clin Microbiol Rev. 2021;34(4):e0002419. | Bhetwal A, Stenlund E, Svärd SG. Pathogenicity and virulence of Giardia intestinalis. Virulence. 2026;17(1):2745308. | CC BY 4.0（OPEN） | 42836554 | 10.1080/21505594.2026.2745308 | PMC13671459 | https://creativecommons.org/licenses/by/4.0/ | 全面：非侵襲性の腸管寄生虫であること、無症候性保虫から急性・慢性の下痢と体重減少までの病像の幅、感染後過敏性腸症候群、小児では無症候感染でも成長・発育の障害をきたすことをいずれも再掲する | 数値の主張なし | — |

## 区分訂正（D）候補：4出典

- SRC-2156（FG-007の主出典、Med Mycol J 2023）：UNKNOWN → RESTRICTED。Crossref にライセンス欄がなく、Europe PMC でも非OA。J-STAGE で無償閲覧できる学会誌だが CC 表示はない（マスターの license_note「Crossref に license 欄なし」と実態は整合するが、区分は RESTRICTED が実態に合う）。
- SRC-2157（FG-008の主出典、Nature 1988）：UNKNOWN → RESTRICTED。Crossref は TDM リンクのみで、CC ライセンスは付されていない。
- SRC-2161（FG-012の主出典、Clin Microbiol Rev 2012）：UNKNOWN → RESTRICTED。PMC に収載される（PMCID PMC3255962）が非OAでライセンス表示はない（ASM誌）。
- SRC-1190（FG-013の主出典、Clin Microbiol Rev 2011）：UNKNOWN → RESTRICTED。PMC に収載される（PMCID PMC3194828）が非OAでライセンス表示はない（ASM誌）。

## 識別子補完候補：6出典（いずれも PMCID を個別照会で照合済み）

- SRC-1435 → PMCID PMC4725385（PMID 26679628・DOI 10.1093/cid/civ933 の論文であることを PMCID 側からも個別確認した。PMC版は非OA・ライセンス表示なしで、区分は RESTRICTED のまま）
- SRC-2153 → PMCID PMC6860006（PMID 31722890・DOI 10.1128/cmr.00140-18 と一致。PMC収載は著者稿でライセンス表示なし）
- SRC-2161 → PMCID PMC3255962（PMID 22232373・DOI 10.1128/cmr.00021-11 と一致）
- SRC-1190 → PMCID PMC3194828（PMID 21976602・DOI 10.1128/cmr.00007-11 と一致）
- SRC-2164 → PMCID PMC6055529（PMID 30046644・DOI 10.1093/ofid/ofy161 と一致。カード側には既に記載があり、マスター側が null）
- SRC-2170 → PMCID PMC8404698（PMID 34378955・DOI 10.1128/cmr.00024-19 と一致。カード側には既に記載があり、マスター側が null）

## 申し送り

- FG-007の主出典（SRC-2156）について、Crossref のレコードでは頁が105-114とされる一方、Europe PMC のレコードとカードの書誌は85-94で一致する。日本語版・英語版の併載の可能性があるため、正本の書誌は登録側で確認されたい（判定には影響しない）。
- FG-014の「死んだ幼虫の摂取でもアレルギーを起こしうる」という点は、近年の自由な全文でも見解が分かれている（生きた幼虫による感作が必要とする報告がある一方、耐熱性アレルゲンAni s 4は加熱後も残存しうる）。候補の裏づけはこの点で部分的にとどまる。カードの主張は主出典に基づくものであり、本棚卸しでは変更しない。
- FG-002・FG-004の主出典 Denning 2024（Lancet Infect Dis）は真菌症負荷の推計の基準文献であり、今後改訂版が出れば数値の再確認が要る（監視事項）。
- FG-010の主出典であるWHO世界マラリア報告は年次刊行のため、2025年版以降が出た時点で2023年確定値の扱いを含め再確認が要る（監視事項）。
- FG-012の候補（Emerg Infect Dis の Etymologia）は短い語誌コラムであり、裏づけは属の現行種数と癜風との関連にとどまる。1996年の再分類史を裏づける自由な全文は本バッチでは見つからなかった。
- 本バッチでは主出典・候補とも識別子の誤記は発見されなかった。
