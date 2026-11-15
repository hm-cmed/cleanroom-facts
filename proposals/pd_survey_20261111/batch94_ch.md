# バッチ94：CH（先天性心疾患）5件

- 実施日：2026-11-15
- 対象：CH 章の対象カード全5件（CH-002・CH-003・CH-004・CH-005・CH-013）
- ルール：2026-11-11 のレポジトリ側指示に基づく新ルール（抄録・添付文書・医学百科は根拠にしない。使えるのは政府の全文文書・報告書、CC BY 全文、試験登録レコードなど全文で読める資料のみ。旧来の「先例に基づく A」は廃止）を適用。
- 方法：各カードの主出典（マスター SRC、本バッチでは SRC-272 と SRC-234 の2出典）の刊行版ライセンスを Crossref の版（version of record）データと Europe PMC の個別レコードで1件ずつ確認し、SRC-234 については刊行版 PDF のライセンス表示そのものでも照合した。候補は CC BY 全文または政府機関の全文文書を実際に読んで裏づけ範囲を判定し、ライセンスは候補ごとに個別確認した。識別子（PMID・PMCID・DOI）は一括照会の値を使わず、DOI キーと PMID キーの個別照会で相互に確かめた。出典の説明はマスター（repo_current2 の sources.yaml）の記載からそのまま取った。本バッチでは Crossref のレート制限（429）には当たらなかった。出版社サイト（erp.bioscientifica.com）はこの環境から直接取得できなかった（error 525）ため、SRC-234 の刊行版は大学リポジトリ所蔵の刊行版 PDF で確認した（申し送り参照）。

## 集計

- A：0件
- B：5件（すべて部分）
- C：0件
- D（マスターの区分訂正）：新規0出典（主出典2出典とも現行 RESTRICTED が正しいことを確認。SRC-234 はバッチ48 と同結論の再確認）

## 明細

| 対象 | 判定 | 現行出典（主出典） | 候補 | 区分 | PMID | DOI | PMCID | ライセンス根拠URL | 裏づけ範囲 | 数値照合 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CH-002 | B（部分） | SRC-272：日本循環器学会ほか合同ガイドライン. 成人先天性心疾患診療ガイドライン（2017年改訂版）（班長：市田蕗子）. 2018年3月23日発行（日本語版） | 赤木禎治. 我が国における成人先天性心疾患患者数の推移と必要とされる医療体制に関する研究. 令和3年度厚生労働科学研究費補助金 難治性疾患等政策研究事業 分担研究報告書／Blanca-Jover E, Contreras-Chova F, Jerez-Calero A, et al. Congenital Heart Disease and Pulmonary Arterial Hypertension: Current Perspectives. Rev Cardiovasc Med. 2026;27(3) | GOV_JP／OPEN | －／41923748 | －／10.31083/rcm48337 | －／PMC13036531 | https://mhlw-grants.niph.go.jp/system/files/report_pdf/202199006A-buntan3_19.pdf／https://creativecommons.org/licenses/by/4.0/ | 部分：候補1（厚生労働科学研究費補助金の分担研究報告書、政府の全文文書）は、カードの推計の根拠となった疫学データそのものを再掲する。先天性心疾患の発生数を出生の1%として推計する前提、1997年時点の国内患者数（15歳未満30万人・15歳以上31万人）によって成人患者数が小児とほぼ同数になったこと、その後も成人患者が増え続けていること（同報告書は2007年を40万人、2022年を57万人と更新推計する）。候補2（CC BY 総説）は「先天性心疾患で生まれた小児の90%超が成人に達する」を再掲する。年約1万300人という年間の発生数、2012年の約45万人、年4〜5%増というカードの値は、いずれの自由な全文でもその値では再掲されない | 部分一致：出生の約1%と1997年ごろの小児・成人の同数は候補1の根拠データ（1%の前提、1997年に小児30万人・成人31万人）と一致。カードの約95%（成人到達）は候補2の「90%超」とは一致しない。候補1の更新推計（2007年40万人・2022年57万人）と候補2の90%超は、カードの値（2012年約45万人・年4〜5%増・約95%）の裏づけとして登録しないこと | 主出典（SRC-272）は「無断転載を禁ずる」の表示で CC 表示はなく、現行 RESTRICTED が正しい。監視事項：主出典の2025年改訂版が刊行済みで、カードの uncertainty にも明記されている。次回改訂時に新しい推計で再照合すること（申し送り参照）。候補2のライセンスは Europe PMC の個別レコード（cc by）と PMC 全文のライセンス要素（CC BY 4.0）で個別確認した |
| CH-003 | B（部分） | SRC-272：日本循環器学会ほか合同ガイドライン. 成人先天性心疾患診療ガイドライン（2017年改訂版）（班長：市田蕗子）. 2018年3月23日発行（日本語版） | Blanca-Jover E, Contreras-Chova F, Jerez-Calero A, et al. Congenital Heart Disease and Pulmonary Arterial Hypertension: Current Perspectives. Rev Cardiovasc Med. 2026;27(3)／Borsani O, Varettoni M, Riccaboni G, Rumi E. Erythrocytosis in congenital heart defects: hints for diagnosis and therapy from a clinical case. Front Med (Lausanne). 2024;11:1419092 | OPEN／OPEN | 41923748／39188884 | 10.31083/rcm48337／10.3389/fmed.2024.1419092 | PMC13036531／PMC11345742 | https://creativecommons.org/licenses/by/4.0/ | 部分（ほぼ全面）：候補1は Eisenmenger 症候群について「妊娠は絶対的禁忌」とする節を置き、瀉血については「ルーチンの瀉血は強く禁忌であり、ヘマトクリット65%超で過粘稠症候群を来し得る。瀉血は過粘稠の急性症状がある場合に限り、等容量の補液を伴って行う」と再掲し、抗凝固については「ルーチンの抗凝固は推奨されず、心房細動・奇異性塞栓の既往・広範な肺血栓が確認された場合に限る」と再掲する。候補2は、赤血球増加は代償性であり瀉血は過粘稠の症状がある場合に限ること、慢性的な瀉血は鉄欠乏・小球性化を招くことを再掲する。カードの「抗凝固は生存の改善が示されていない」という表現そのものは自由な全文で再掲されない | 一致：ヘマトクリット65%超という瀉血の目安は候補1の記載と一致する。それ以外の数値的主張はカードにない | 主出典の区分は CH-002 行のとおり RESTRICTED が正しい。候補のライセンスはいずれも Europe PMC の個別レコード（cc by）と PMC 全文のライセンス要素（CC BY）で個別確認した |
| CH-004 | B（部分） | SRC-272：日本循環器学会ほか合同ガイドライン. 成人先天性心疾患診療ガイドライン（2017年改訂版）（班長：市田蕗子）. 2018年3月23日発行（日本語版） | Blanca-Jover E, Contreras-Chova F, Jerez-Calero A, et al. Congenital Heart Disease and Pulmonary Arterial Hypertension: Current Perspectives. Rev Cardiovasc Med. 2026;27(3)／Borsani O, Varettoni M, Riccaboni G, Rumi E. Erythrocytosis in congenital heart defects: hints for diagnosis and therapy from a clinical case. Front Med (Lausanne). 2024;11:1419092 | OPEN／OPEN | 41923748／39188884 | 10.31083/rcm48337／10.3389/fmed.2024.1419092 | PMC13036531／PMC11345742 | https://creativecommons.org/licenses/by/4.0/ | 部分（定性的のみ）：候補1は Eisenmenger 症候群の全身合併症として喀血・痛風・脳血管イベント・脳膿瘍・腎障害を列挙し、候補2も痛風と腎機能障害に触れる。合併症の顔ぶれはカードと重なるが、日本の調査に基づく頻度（喀血16%・痛風9%・脳梗塞8%・慢性腎不全7%・過粘稠症候群6%・脳膿瘍4%・感染性心内膜炎4%）と、SpO2 85%でヘモグロビン20 g/dL程度が必要で14 g/dLでは鉄欠乏を疑うという値は、自由な全文で再掲されない | 一致する数値なし（候補はいずれも頻度・ヘモグロビン値を再掲しない）。海外の登録研究には異なる頻度が示されるものがあるが、値がカードと異なるため候補にしない | 主出典の区分は CH-002 行のとおり RESTRICTED が正しい。候補のライセンスはいずれも Europe PMC の個別レコード（cc by）と PMC 全文のライセンス要素（CC BY）で個別確認した |
| CH-005 | B（部分） | SRC-272：日本循環器学会ほか合同ガイドライン. 成人先天性心疾患診療ガイドライン（2017年改訂版）（班長：市田蕗子）. 2018年3月23日発行（日本語版） | Jarasvaraparn C, Schooler GR, González IA, Ginde S, Mavis A. Long-Term Care in Fontan Circulation: Surveillance and Management of Fontan-Associated Liver Disease and Protein-Losing Enteropathy. Curr Cardiol Rep. 2026;28(1) | OPEN | 42154163 | 10.1007/s11886-026-02378-0 | PMC13186934 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補（Fontan 循環の長期管理の総説、CC BY）は、長期合併症として単心室機能低下による心不全、蛋白漏出性胃腸症、不整脈、Fontan 関連肝疾患（肝うっ血を含む）を挙げ、カードの原因の顔ぶれ（心室機能の低下・蛋白漏出性胃腸症・肝うっ血・心房性不整脈）と定性的に重なる。肺血管抵抗の上昇による前負荷の不足と洞不全の明記、心不全の有病率が成人期に約50%へ増えるという値は再掲されない | 不一致（対象が異なる）：候補の10年生存率は「2001年以降の手術例で90〜95%超」であり、カードの「おおむね80%を超える」（時代を問わない一般値）とは対象が異なり一致しない。候補の数値をカードの裏づけとして登録しないこと。心不全の有病率（術後早期10〜20%から成人期約50%）は候補に再掲がない | カードには既存の裏づけ CH-018（指定難病の資料の Fontan 術後症候群）があり、本候補は追加の裏づけである。主出典の区分は CH-002 行のとおり RESTRICTED が正しい。監視事項：主出典の2025年改訂版が刊行済み（申し送り参照）。候補のライセンスは Europe PMC の個別レコード（cc by）と PMC 全文のライセンス要素（CC BY 4.0）で個別確認した |
| CH-013 | B（部分） | SRC-234：Zaidi A, Oxborough D, Augustine DX, et al. Echocardiographic assessment of the tricuspid and pulmonary valves: a practical guideline from the British Society of Echocardiography. Echo Res Pract 2020;7:G95-G122 | Zhou Z, Huang Y, Han L, et al. Right ventricular dilatation score: a new assessment to right ventricular dilatation in adult patients with repaired tetralogy of Fallot. BMC Cardiovasc Disord. 2023;23(1) | OPEN | 37710173 | 10.1186/s12872-023-03487-2 | PMC10500856 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補（Fallot 四徴症修復後の右室拡大の研究、CC BY）は、心臓MRIによる右室容積が肺動脈弁置換の介入判断の基準になることと、ガイドラインの閾値として右室拡張末期容積係数160 mL/m²以上を再掲する。心臓MRIで逆流率40%超を重症とする肺動脈弁逆流の重症度分類と、微量の肺動脈弁逆流が健常者の最大75%にみられるという値は、自由な全文で再掲されない | 部分一致：右室拡張末期容積係数160 mL/m²は候補の再掲と一致する。右室収縮末期容積係数は、候補が閾値を80 mL/m²とするのに対しカードは82 mL/m²超であり一致しない。候補の80をカードの82の裏づけとして登録しないこと。別の CC BY の系統的レビュー（Slouha E, et al. Cureus. 2023;15(11):e49577）にも近傍値（収縮末期容積係数82未満で正常化、拡張末期容積係数158・165等）が散在するが、カードの「160超・82超」の組そのものの再掲ではない | 主出典（SRC-234）の刊行版ライセンスは CC BY-NC-ND 4.0 で、現行 RESTRICTED が正しい（区分訂正の節参照。Crossref は CC BY 4.0 を記録するが刊行版を優先する）。カードの uncertainty「刊行版の表記は未確認」は本バッチで解消した（申し送り参照）。識別子補完候補あり（SRC-234 の PMID・PMCID）。候補のライセンスは Europe PMC の個別レコード（cc by）と PMC 全文のライセンス要素（CC BY 4.0）で個別確認した |

## D（マスターの区分訂正）：新規0出典

- 本バッチでは新規の区分訂正はない。対象5件の主出典は2出典（SRC-272・SRC-234）で、いずれも現行の RESTRICTED が正しいことを確認した。
- SRC-272（CH-002〜CH-005 の主出典）：学会合同ガイドライン（成人先天性心疾患診療ガイドライン 2017年改訂版、日本語版）。マスターの license_note のとおり「無断転載を禁ずる」の表示で CC 表示はなく、RESTRICTED が正しい。マスターの license_note と実態の食い違いはない。
- SRC-234（CH-013 の主出典）：刊行版（version of record）自体に「© The British Society of Echocardiography. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.」の表示があることを刊行版 PDF で確認した。Europe PMC の個別レコードのライセンス表示も cc by-nc-nd で、PMC 収載コピー（PMC8052586、著者稿）も CC BY-NC-ND である。一方、Crossref の版データは CC BY 4.0 を記録しており食い違うが、刊行版を優先する原則により RESTRICTED が正しい。これはバッチ48 で「Crossref だけで OPEN に反転させない」とした結論と同一であり、新規の訂正ではなく再確認（再掲）として記録する。マスターの license_note「CC BY-NC-ND 4.0（リポジトリの表示。著者最終稿）」については、刊行版自体にも同じライセンス表示があることが分かったため、注記の文言の更新候補として申し送る（区分自体は不変）。

## 識別子補完候補：新規1出典2項目（いずれも DOI・PMID キーの個別照会で照合済み）

- SRC-234：PMID 33339003、PMCID PMC8052586

新規分はいずれもマスター・カードとも null の欄への補完候補である。DOI（10.1530/ERP-20-0033）キーと PMID（33339003）キーの個別照会が互いに一致し、当該論文の識別子であることを確認した（Europe PMC のライセンス表示 cc by-nc-nd も刊行版の確認と整合する）。SRC-272 には DOI・PMID・PMCID が存在しない（和文ガイドライン）ため補完候補はない。

## 申し送り

- SRC-234 のライセンスの食い違い（再掲確認）：Crossref の版データは CC BY 4.0 を返すが、刊行版は CC BY-NC-ND 4.0 である。今後も Crossref の記録だけで SRC-234 を OPEN に反転させないこと（バッチ48 と同結論）。
- CH-013 のカードの uncertainty「著者最終稿で確認した。刊行版の表記は未確認」は本バッチで解消した。刊行版自体に CC BY-NC-ND 4.0 の表示がある。カード・マスターの source_license／license_note の文言（「リポジトリの表示。著者最終稿」）は、刊行版で確認済みの表記への更新を登録側に提案する（区分 RESTRICTED は不変）。
- 監視事項：CH-002〜CH-005 の主出典（SRC-272、成人先天性心疾患診療ガイドライン 2017年改訂版）には2025年改訂版が刊行済みであり、各カードの uncertainty にも明記されている。本バッチの裏づけは2025年版との本体照合の代替にはならないため、次回改訂時に再照合すること。
- 候補側の数値の扱い：CH-002 の厚生労働科学研究費補助金報告書の更新推計（2007年40万人・2022年57万人）と Rev Cardiovasc Med 総説の「90%超」、CH-005 候補の10年生存率（2001年以降の手術例で90〜95%超）、CH-013 候補の右室収縮末期容積係数80 mL/m²は、いずれもカードの値とは対象または値が異なるため、裏づけ登録時にカードの値の裏づけとして使わないこと。
- CH-005 には既存の裏づけ CH-018（指定難病の資料の Fontan 術後症候群）がある。本バッチの候補は追加の裏づけであり、既存の裏づけの置換えではない。
- 方法上の注記：出版社サイト（erp.bioscientifica.com）はこの環境から直接取得できず（error 525）、SRC-234 の刊行版ライセンスは大学リポジトリに所蔵された刊行版 PDF の表示と Europe PMC・PMC の記録で確認した。Europe PMC の REST は断続的にエラーを返したが、再試行と個別照会で全件完了した。本バッチでは Crossref のレート制限（429）には当たらなかった。
- 主出典・候補とも識別子の誤記（別論文の混入）は本バッチでは発見されなかった。主出典2出典と候補の識別子は DOI キー・PMID キーの個別照会で相互に照合した。
- 本バッチの判定は以上で完結しており、カードの主張・数値の変更は一切行っていない。
