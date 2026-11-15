# バッチ99：OX（生活環境・職業性の横断項目）2件

- 実施日：2026-11-15
- 対象：OX 章の対象カード全2件（OX-001・OX-002）
- ルール：2026-11-11 のレポジトリ側指示に基づく新ルール（抄録・添付文書・医学百科は根拠にしない。使えるのは政府の全文文書・報告書、CC BY 全文、試験登録レコードなど全文で読める資料のみ。旧来の「先例に基づく A」は廃止）を適用。
- 方法：各カードの主出典（マスター SRC、本バッチでは SRC-4140・SRC-4141 の2出典）の刊行版ライセンスを個別に確認した。SRC-4141 は Crossref の版（version of record）データ、Europe PMC の個別レコード、PMC 全文のライセンス要素の3経路で CC BY-NC 4.0 と特定した。SRC-4140 は Crossref の版データ照会が当該 DOI で2回ともレート制限（429）を返したため見送り、Europe PMC の個別レコード（非 OA・ライセンス表示なし）、NCBI E-utilities（efetch、db=pmc）で取得した PMC 収載コピーのフロントマター（ライセンス要素・permissions の記載がなく、出版社が XML 形式の全文ダウンロードを許可していない旨の注記がある）、Unpaywall・OpenAlex（いずれも OA の所在は PMC のリポジトリコピーのみでライセンス記録なし）で代替確認した。候補は CC BY 全文を実際に読んで裏づけ範囲を判定し、ライセンスは候補ごとに Crossref の版データ、Europe PMC の個別レコード、PMC 全文のライセンス要素で個別確認した。識別子（PMID・PMCID・DOI）は一括照会の値を使わず、DOI キー・PMID キー・PMCID キーの個別照会（NCBI esummary・Europe PMC）で相互に確かめた。出典の説明はマスター（repo_current2 の sources.yaml）の記載からそのまま取った。

## 集計

- A：0件
- B：2件（すべて部分）
- C：0件
- D（マスターの区分訂正）：新規1出典（SRC-4140：UNKNOWN→RESTRICTED）

## 明細

| 対象 | 判定 | 現行出典（主出典） | 候補 | 区分 | PMID | DOI | PMCID | ライセンス根拠URL | 裏づけ範囲 | 数値照合 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| OX-001 | B（部分） | SRC-4140：Zellner T, Prasa D, Färber E, et al. The Use of Activated Charcoal to Treat Intoxications. Dtsch Arztebl Int. 2019;116(18):311-317 | Albertson TE, Owen KP, Sutter ME, Chan AL. Gastrointestinal decontamination in the acutely poisoned patient. Int J Emerg Med. 2011;4:65 | OPEN | 21992527 | 10.1186/1865-1380-4-65 | PMC3207879 | https://creativecommons.org/licenses/by/2.0/ | 部分：候補（CC BY 総説）は、米国臨床中毒学会（AACT）と欧州毒物センター・臨床中毒学会（EAPCCT）のポジションペーパーを引いて、単回活性炭は投与するなら摂取後1時間以内が最も利益が大きく、効果は時間とともに低下すると述べ、カードの「摂取後できるだけ速やかに、原則として1時間以内」の骨格と一致する。また下剤について、ポジションステートメントが活性炭とのルーチンの併用を支持しないことを再掲し、カードの「下剤とのルーチンの併用は推奨されない」と一致する。複数回活性炭は保護された／無傷の気道の患者に限るとし、気道確保と誤嚥リスクの枠組みにも触れる。活性炭に十分に結合しない物質として電解質・金属を挙げる（全腸洗浄の文脈）。ただし、適応の重症度（中等症から生命を脅かす中毒）、用量（成人50 g・小児0.5〜1 g/kg）、徐放性製剤では6時間までとする窓、無効ないし不十分な物質の列挙（酸・アルカリ、アルコール類、有機溶剤、無機塩類、金属）の全体、単回投与で気道が確保されていない意識障害を禁忌とする明示は、候補に再掲がない | カードの数値のうち「1時間以内」は候補の再掲（最も利益が大きい時間枠）と一致する。用量（成人50 g・小児0.5〜1 g/kg・毒物量の10〜40倍）と「徐放性製剤では6時間まで」は候補に再掲がなく照合できない（候補側に矛盾する数値はない） | 主出典 SRC-4140 の区分訂正（UNKNOWN→RESTRICTED）が新規にある（区分訂正の節参照）。候補のライセンスは Crossref の版データ（CC BY 2.0）・Europe PMC の個別レコード・PMC 全文のライセンス要素（CC BY 2.0）の3経路で個別確認した。StatPearls の活性炭の章は二次資料のため候補にしていない |
| OX-002 | B（部分） | SRC-4141：Kim K, Kim J. A work-relatedness assessment in epidemiological case investigation of occupational cancers: I. Principles. Ann Occup Environ Med. 2020;32:e30 | Kim EA, Lee E, Kang SK, Jeong M. Probability of causation for occupational cancer after exposure to ionizing radiation. Ann Occup Environ Med. 2018;30:3／Song J, Woo KH, Kim YH. Guidelines for recognition of occupational cancers in Korea: the results of scientific review by Korean Society of Occupational and Environmental Medicine (2013–2016). Ann Occup Environ Med. 2018;30:12／Kim HR, Kim B, Jo BS, Lee JW. Silica exposure and work-relatedness evaluation for occupational cancer in Korea. Ann Occup Environ Med. 2018;30:4 | OPEN／OPEN／OPEN | 29435338／29456866／29423227 | 10.1186/s40557-018-0220-5／10.1186/s40557-018-0223-2／10.1186/s40557-018-0216-1 | PMC5791729／PMC5809845／PMC5791359 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補1（CC BY、放射線による職業性がんの原因確率（probability of causation、PC／assigned share）の総説）は、職業性がんの因果関係が確率的に推定されるものであること、補償の判断に確率的な基準（概ね PC 50%超）が使われることを述べ、カードの「因果関係の判断は決定的ではなく確率的に行われる」の要素を放射線領域で再掲する。また、客観的な曝露レベルのデータがないために業務起因性を判断できなかった症例を挙げ、カードの困難要因のうち「客観的な職歴資料の喪失」と重なる。候補2（CC BY、韓国の職業性がん認定ガイドライン特集の総説）は、迅速で公正な補償には認定基準が必要である一方、発がん要因についての情報（曝露の期間・濃度など）が十分でないことを述べ、評価の困難さの要素を裏づける。候補3（CC BY、結晶シリカの業務起因性評価）は、個別の肺がん症例が症例ごとに疫学調査の対象となる運用と、疫学知見の不整合（シリカと胃がんの関連について研究間で結論が異なること）を述べ、「疑わしい症例については個別の詳細な検討が必要」と「疫学知見の不整合」の要素をシリカ領域で裏づける。ただし、評価の順序そのもの（疾患の診断を確定し、次に曝露を評価し、そのうえで業務起因性を評価する）、「絶対的な判断基準は存在しない」という表明、発症機序の未確立・症例の複雑さという困難要因の列挙は、いずれの候補にも再掲がない | 数値的主張はカードにない。候補1の「PC 50%超」は放射線領域の補償運用の閾値であり、カードの主張の数値として裏づけ登録しないこと（申し送り参照） | 主出典 SRC-4141 は刊行版ライセンスが CC BY-NC 4.0（Crossref の版データ・Europe PMC の個別レコード・PMC 全文のライセンス要素で個別確認）で、現行 RESTRICTED が正しい（区分訂正なし）。カード側の source_license「CC BY-NC 4.0」の記載も実態と一致する。同じ Ann Occup Environ Med でも 2018年の候補3件は刊行版が CC BY 4.0 であり、誌単位ではなく論文ごとにライセンスを確認した。主出典の続編（Part II. Practice、PMC7533287）は刊行版が CC BY-NC 4.0 のため候補にしていない |

## D（マスターの区分訂正）：新規1出典

- SRC-4140（OX-001 の主出典）：UNKNOWN→RESTRICTED。Zellner et al., Dtsch Arztebl Int 2019（Deutscher Ärzte-Verlag）。Europe PMC の個別レコードでは非 OA でライセンス表示がなく、PMC 収載コピー（PMC6620762）のフロントマターにもライセンス要素・permissions の記載がない（出版社は XML 形式の全文ダウンロードを許可していない）。Unpaywall・OpenAlex でも OA の所在は PMC のリポジトリコピーのみで、ライセンスの記録はない。刊行版に CC BY 等の自由なライセンスは確認できないため、RESTRICTED が妥当である。カード側の source_license「全文は PMC で公開されているが、CC ライセンス表示は確認できなかった」という記載はこの確認結果と一致し、これで決着する。マスターの license_note は null で、実態と食い違う記載はない。なお Crossref の版データ照会は当該 DOI で2回とも 429（レート制限）を返したため見送った（申し送り参照）。
- SRC-4141（OX-002 の主出典）：現行 RESTRICTED が正しい（区分訂正なし）。Kim & Kim, Ann Occup Environ Med 2020。刊行版ライセンスは CC BY-NC 4.0 と Crossref の版データ・Europe PMC の個別レコード・PMC 全文のライセンス要素の3経路で特定でき、自由区分には当たらない。マスターの license_note は null で、食い違う記載はない。

## 識別子補完候補：新規2出典4項目（DOI・PMID・PMCID キーの個別照会で照合済み）

- SRC-4140：PMID 31219028、PMCID PMC6620762（いずれもマスターは null、カード側には記録済み。NCBI esummary の PMID キー照会で、同一レコードに DOI 10.3238/arztebl.2019.0311 と書誌（Dtsch Arztebl Int. 2019;116(18):311-317）が収載されることを確認し、Europe PMC の DOI キー個別照会でも PMID・PMCID が一致した。識別子を補っても区分は RESTRICTED のまま）
- SRC-4141：PMID 33072341、PMCID PMC7533286（いずれもマスターは null、カード側には記録済み。NCBI esummary の PMID キー照会で、同一レコードに DOI 10.35371/aoem.2020.32.e30 と書誌（Ann Occup Environ Med. 2020;32:e30）が収載されることを確認した）

## 申し送り

- OX-001 の裏づけの性格：候補（Albertson et al. 2011）は AACT／EAPCCT ポジションペーパーの引用を通じた骨格（1時間以内の投与、下剤のルーチン併用の不支持、気道保護の枠組み）の裏づけであり、用量（成人50 g・小児0.5〜1 g/kg）、適応の重症度（中等症から生命を脅かす中毒）、徐放性製剤での6時間の窓、無効な物質の列挙の全体は自由な全文に再掲がない。主出典の後継版に当たる監視事項は本バッチでは見つからなかった。
- OX-002 の裏づけの性格：候補3件はいずれも主出典と同じ Ann Occup Environ Med の2018年特集の論文で、要素別の裏づけ（確率的な因果判断、客観的資料の欠如による判断困難、個別症例の疫学調査、疫学知見の不整合）にとどまり、評価の3段階の順序そのものの再掲ではない。候補1の PC 50%超という値は放射線領域の補償運用の閾値であり、主出典の数値として登録しないこと。主出典の続編 Part II（Practice）は刊行版が CC BY-NC 4.0 のため候補に使えない。
- 方法上の注記：(1) Crossref の版データ照会は SRC-4140 の DOI（10.3238/arztebl.2019.0311）で2回とも HTTP 429 を返したため見送り、Europe PMC の個別レコード、PMC 収載コピーのフロントマター、Unpaywall、OpenAlex で代替確認した（候補4件と SRC-4141 の Crossref 照会は完了している）。(2) Europe PMC の全文 XML は PMC6620762 で HTTP 500 を返したため、同コピーの確認は NCBI E-utilities（efetch、db=pmc）で代替した。(3) Europe PMC の検索 API が一時的に HTTP 503・空応答を返したため、一部の照会は再試行と NCBI esummary で代替した。
- 主出典・候補とも識別子の誤記（別論文の識別子の混入）は本バッチでは発見されなかった。主出典2出典の書誌（誌名・年・巻・号・ページ）は NCBI・Crossref・Europe PMC の個別レコードの値とすべて一致し、要・正本確認に当たる食い違いはない。
- 本バッチの判定は以上で完結しており、カードの主張・数値の変更は一切行っていない。
