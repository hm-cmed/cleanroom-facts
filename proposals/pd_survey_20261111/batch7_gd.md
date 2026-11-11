# バッチ7：GD（胃・十二指腸）74件 パブリックドメイン出典確認結果

調査日：2026-11-11／対象：主出典が自由区分（OPEN・GOV_US・GOV_JP）でない GD のカード74件。判定は A 置き換え可／B 裏づけ追加／C 見つからない／D 区分の訂正。主張文と数値は変更していない。ライセンスは Crossref の version-of-record 表示と Europe PMC の license 表示で、識別子は API で確認した。

## 集計

| 判定 | 件数 |
|---|---|
| A 置き換え可（先例に基づくもの） | 5 |
| A 置き換え可（それ以外） | 0 |
| B 裏づけ追加 | 8 |
| C 見つからない | 7 |
| D 区分の訂正 | 54 |
| 合計 | 74 |

## 重要な発見

1. **D 54件は6出典に集中する。** 機能性ディスペプシア診療ガイドライン2021英語版（SRC-028、18件）、胃癌治療ガイドライン第6版・第7版の英語版（SRC-029・SRC-030、計25件）、GIST ガイドライン2022英語版（SRC-032、8件）、肝硬変診療ガイドライン2020英語版（SRC-018、1件）、Emerg Infect Dis のアニサキス全国調査（SRC-042、2件）は、いずれも Crossref と Europe PMC の両方で CC BY 4.0（EID は CC BY）と確認できた。バッチ5で見た「日本の学会ガイドラインの英語版は国際誌で CC BY になる」パターンの継続であり、74件中54件がマスターの区分訂正だけで解決する。
2. **A 5件はすべて「先例に基づく A」。** 主要試験（CheckMate 649・SPOTLIGHT・術後イマチニブ第III相・REVISE）と ESGE ガイドラインは抄録が厚く、主張の全要素＋数値まで抄録に収載されている。非先例の A は0件だった。
3. **識別子の補完候補が多数ある。** SRC-028・SRC-029・SRC-030 の PMID・PMCID、SRC-018 の DOI・PMID、SRC-032 の PMCID、SRC-042 の PMID・PMCID のほか、GD-092（SRC-045 の PMID 38875111）、GD-098（SRC-4213 の PMID 33822331）、GD-086・087・088（SRC-043 の PMID 24764778）、GD-071（SRC-039 の PMID 37401795）、GD-095（SRC-047 の PMID 42100946・PMCID）、GD-096（SRC-4211 の PMID 18810558）、GD-097（SRC-4212 の PMID 37383896・PMCID）、GD-099（SRC-4214 の PMID 31487687・PMCID）がマスター未登録である。
4. **区分の明確化の申し送り（D ではない）。** SRC-039（ENETS 2023）は CC BY-NC-ND、SRC-047（Turk J Surg）は CC BY-NC、SRC-4212（World J Clin Cases）は CC BY-NC で、いずれも RESTRICTED への明確化または現行維持が適切。SRC-044 は J-STAGE の学会誌で DOI が Crossref に登録されておらず、ライセンス未確認のため現行 UNKNOWN を維持した。
5. **数値の両値記録が1件（GD-085）。** A. simplex sensu stricto の割合は、カード 168/189匹＝88.9%（同定幼虫ベース）に対し、抄録は患者ベースで 88.4%。分母の違いによる差で、本文の集計と矛盾しない。
6. **版の申し送り（GD-044・GD-048）。** 両カードは胃癌治療ガイドライン第6版（SRC-029）出典のままである。第7版（SRC-030、同じく CC BY）がマスターにあるため、登録側で第7版への付け替え要否の確認を推奨する（数値の不一致ではない）。
7. **GD-057 は政府文書で裏づけできた。** ゾルベツキシマブの国内承認（2024年3月26日、世界初の抗CLDN18.2抗体承認）は、PMDA 審査報告書・厚労省審議結果報告書が効能・効果と「2023年10月時点で承認国なし」を明記しており、現出典（企業の適時開示）に加えて政府文書を裏づけにできる。
8. **C 7件の内訳。** 日本の内視鏡所見記載分類（GD-072）、総説本文固有の数値群（GD-086〜088・093・094）、日本の症例報告固有の所見（GD-091）が中心で、自由な資料では裏づけ経路がない。

## A 置き換え可（5件、すべて先例に基づく）

### GD-055（出典：Janjigian YY, et al. CheckMate 649. Lancet 2021;398:27-40（当該論文）の PubMed 抄録レコード）

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI 10.1016/S0140-6736(21)00797-2、PMID 34102137、PMCID PMC8436782 |
| 区分 | GOV_US |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:34102137&format=json&resultType=core |
| 裏づけ範囲 | 抄録の Methods が主要評価項目（PD-L1 CPS 5以上の集団での OS と PFS）を明記し、Findings が同集団での OS（HR 0.71）・PFS（HR 0.68）の有意な改善を収載する。対象（未治療・切除不能・HER2陽性でない胃癌／食道胃接合部癌／食道腺癌）も抄録と一致する。カードの主張の全要素が抄録に収載されている。 |
| 数値照合 | 該当なし（カードに効果量の数値はない。主要評価項目の集団設定 CPS 5以上は抄録と一致） |
| 備考 | 先例に基づく A（PubMed 抄録レコードに主張の全要素が載るケース）。抄録を置き換え出典と認めない運用では B に回る。原典（SRC-034）は Elsevier の購読論文で RESTRICTED のまま。試験登録 NCT02872116 は抄録に記載がある。 |
| 確認経路 | Europe PMC REST API（resultType=core）の抄録レコードで確認（2026-11-11） |

### GD-056（出典：Shitara K, et al. SPOTLIGHT. Lancet 2023;401:1655-1668（当該論文）の PubMed 抄録レコード）

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI 10.1016/S0140-6736(23)00620-7、PMID 37068504、PMCID なし |
| 区分 | GOV_US |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:37068504&format=json&resultType=core |
| 裏づけ範囲 | 抄録の Findings が、ゾルベツキシマブ＋mFOLFOX6 の無増悪生存期間中央値 10.61か月対プラセボ＋mFOLFOX6 の 8.67か月（HR 0.75）を収載し、対象（CLDN18.2陽性・HER2陰性・未治療の切除不能胃癌／食道胃接合部腺癌）も一致する。カードの主張の全要素が抄録に収載されている。 |
| 数値照合 | 一致（PFS 中央値：カード 10.61か月対8.67か月／抄録 10.61対8.67） |
| 備考 | 先例に基づく A（PubMed 抄録レコードに主張の全要素が載るケース）。抄録を置き換え出典と認めない運用では B に回る。原典（SRC-035）は Elsevier の購読論文で RESTRICTED のまま。試験登録 NCT03504397 は抄録に記載がある。 |
| 確認経路 | Europe PMC REST API（resultType=core）の抄録レコードで確認（2026-11-11） |

### GD-069（出典：Joensuu H, et al. Adjuvant imatinib for high-risk GI stromal tumor: analysis of a randomized trial. J Clin Oncol 2016;34:244-250（当該論文）の PubMed 抄録レコード）

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI 10.1200/JCO.2015.62.9170、PMID 26527782、PMCID なし |
| 区分 | GOV_US |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:26527782&format=json&resultType=core |
| 裏づけ範囲 | 抄録が、中央判定で GIST と確認され肉眼的転移のない部分集団で、3年投与群の5年生存率 93.4%対1年投与群 86.8%（HR 0.53）を収載する。全集団の生存延長（91.9%対85.3%、HR 0.60）も併記されている。カードの主張の全要素が抄録に収載されている。 |
| 数値照合 | 一致（5年生存率：カード 93.4%対86.8%、HR 0.53／抄録と同一） |
| 備考 | 先例に基づく A（PubMed 抄録レコードに主張の全要素が載るケース）。抄録を置き換え出典と認めない運用では B に回る。原典（SRC-033）は ASCO の購読論文で RESTRICTED のまま。 |
| 確認経路 | Europe PMC REST API（resultType=core）の抄録レコードで確認（2026-11-11） |

### GD-092（出典：Cook D, et al. Stress ulcer prophylaxis during invasive mechanical ventilation (REVISE). N Engl J Med 2024（当該論文）の PubMed 抄録レコード）

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI 10.1056/NEJMoa2404245、PMID 38875111、PMCID なし |
| 区分 | GOV_US |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:38875111&format=json&resultType=core |
| 裏づけ範囲 | 抄録が、人工呼吸管理中の重症患者4,821例、パントプラゾール40 mg静注、臨床的に重要な上部消化管出血 1.0%対3.5%（HR 0.30）、90日死亡 29.1%対30.9%（HR 0.94、差なし）をすべて収載する。カードの主張の全要素が抄録に収載されている。 |
| 数値照合 | 一致（4,821例、1.0%対3.5%・HR 0.30、29.1%対30.9%・HR 0.94 のいずれも抄録と同一） |
| 備考 | 先例に基づく A（PubMed 抄録レコードに主張の全要素が載るケース）。抄録を置き換え出典と認めない運用では B に回る。原典（SRC-045）の PMID はマスター未登録（null）のため、PMID 38875111 の補完を提案する。原典は NEJM の購読論文で RESTRICTED のまま。 |
| 確認経路 | Europe PMC REST API（resultType=core）の抄録レコードで確認（2026-11-11） |

### GD-098（出典：Vanbiervliet G, Moss A, Arvanitakis M, et al. Endoscopic management of superficial nonampullary duodenal tumors: ESGE Guideline. Endoscopy 2021;53(5):522-534（当該ガイドライン論文）の PubMed 抄録レコード）

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI 10.1055/a-1442-2395、PMID 33822331、PMCID なし |
| 区分 | GOV_US |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:33822331&format=json&resultType=core |
| 裏づけ範囲 | 抄録に推奨文が番号付きで収載されている：推奨1（すべての十二指腸腺腫は内視鏡切除を検討すべき、強い推奨）、推奨5（6 mm未満の小病変にコールドスネア切除）、推奨6（大きな非乳頭部腺腫には EMR が第一選択、強い推奨）、推奨7（ESD は熟練者に限る、強い推奨）。カードの主張の全要素が抄録に収載されている。 |
| 数値照合 | 一致（6 mm未満という小病変の境界は抄録の推奨5と同一） |
| 備考 | 先例に基づく A（PubMed 抄録レコードに主張の全要素が載るケース）。抄録を置き換え出典と認めない運用では B に回る。原典（SRC-4213）の PMID はマスター未登録（null）のため、PMID 33822331 の補完を提案する。原典は Thieme の購読論文で RESTRICTED のまま。 |
| 確認経路 | Europe PMC REST API（resultType=core）の抄録レコードで確認（2026-11-11） |

## B 裏づけ追加（8件）

### GD-057（出典：独立行政法人医薬品医療機器総合機構（PMDA）審査報告書・厚生労働省 審議結果報告書（ビロイ点滴静注用100mg、令和6年2月19日審査報告書・令和6年3月4日審議結果））

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI なし、PMID なし、PMCID なし |
| 区分 | GOV_JP |
| ライセンス確認根拠 | http://www.nihs.go.jp/dbcb/reviews/Zolbetuximab.pdf |
| 裏づけ範囲 | 審査報告書が効能・効果「CLDN18.2陽性の治癒切除不能な進行・再発の胃癌」を明記し、「2023年10月時点において、本薬が承認されている国又は地域はない」と記載する（世界初の抗CLDN18.2抗体承認という位置づけの前提を裏づける）。承認日 2024年3月26日は国立がん研究センターとアステラスの発表でも一致する。 |
| 数値照合 | 一致（承認日 2024年3月26日、効能・効果は審査報告書の記載と同一） |
| 備考 | 現出典（SRC-038、アステラス製薬の適時開示）は企業の公表資料で、区分は据え置く。政府文書としての裏づけ追加を提案する。PMDA 資料の利用条件（サイト方針 PDL 1.0）の扱いは先行調査で申し送ったとおり登録側の判断に委ねる。 |
| 確認経路 | PMDA 審査報告書・厚労省審議結果報告書（国立医薬品食品衛生研究所サイト掲載の PDF）を検索で特定し本文を確認、国立がん研究センターのプレスリリースでも承認日を照合（2026-11-11） |

### GD-071（出典：Gastric neuroendocrine tumors: a comprehensive analysis of clinicopathological characteristics（Arquivos Brasileiros de Cirurgia Digestiva）2025（新規登録候補））

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI なし、PMID 41983868、PMCID PMC13075655 |
| 区分 | OPEN |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41983868&format=json&resultType=core |
| 裏づけ範囲 | 全文が分類を明記する：Type I は自己免疫性萎縮性胃炎と高ガストリン血症を背景とし最も多い（70〜80%）、Type II は Zollinger-Ellison 症候群・MEN1 に伴うガストリノーマの文脈で生じる。カードの I型・II型の背景病態の区別が裏づけられる。 |
| 数値照合 | 該当なし（カードに数値なし。候補側の Type I の割合70〜80%はカードの主張外） |
| 備考 | 現出典（SRC-039、ENETS 2023）は Europe PMC で CC BY-NC-ND と確認され、マスターの UNKNOWN は RESTRICTED への明確化が適切である（D ではない申し送り）。あわせて SRC-039 の PMID 37401795 の補完を提案する（マスター未登録）。 |
| 確認経路 | Europe PMC REST API でライセンス（cc by）と PMCID を確認し、PMC 全文で Type I・II の記載を照合（2026-11-11） |

### GD-089（出典：Endoscopic findings and outcomes of gastric mucosal changes relating to potassium-competitive acid blocker and proton pump inhibitor. DEN Open 2024（新規登録候補））

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI 10.1002/deo2.400、PMID 38919514、PMCID なし |
| 区分 | OPEN |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:38919514&format=json&resultType=core |
| 裏づけ範囲 | PPI・P-CAB（ボノプラザン）長期投与に伴う胃粘膜変化（胃底腺ポリープ、過形成性ポリープ、多発性白色扁平隆起病変、敷石状変化、黒点、星屑様変化の6病変）を総説し、血清ガストリン値は休薬判断に有用でないことなど、変化の大半が休薬・中止を要しない方向の知見を整理している。カードの前半（多くの変化は休薬や中止を必要としない）は裏づけられる。 |
| 数値照合 | 該当なし |
| 備考 | 「出血を伴う過形成性ポリープがある場合は中止または H2受容体拮抗薬への変更を検討する」という具体は、候補の抄録の確認範囲に明示がなく、現出典（SRC-044、日本消化器内視鏡学会雑誌2025）の本文の範囲である。SRC-044 の DOI は Crossref に登録がなく（照会で404）、ライセンスは未確認のため現行 UNKNOWN を維持する。 |
| 確認経路 | Europe PMC REST API でライセンス（cc by）と抄録を確認（2026-11-11） |

### GD-090（出典：Sugimoto M, et al. Evidence-based clinical practice guidelines for peptic ulcer disease 2026. J Gastroenterol 2026（既存 SRC-031、OPEN））

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI 10.1007/s00535-026-02504-3、PMID なし、PMCID なし |
| 区分 | OPEN |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1007/s00535-026-02504-3%22&format=json&resultType=core |
| 裏づけ範囲 | 消化性潰瘍診療ガイドラインの薬剤性潰瘍の枠組み（NSAID 潰瘍の予防・対策として、最低有効量・最短期間、H. pylori 除菌、PPI 併用、COX-2 選択的阻害薬の使用）が、カードの対策部分と整合する。2020年版英語版（PMID 33620586、CC BY）の抄録でも薬剤性潰瘍が独立の章立てであることを確認した。 |
| 数値照合 | 該当なし |
| 備考 | 傷害の好発部位（前庭部から幽門部の潰瘍・びらん・出血）という内視鏡所見の具体は現出典（SRC-044）固有で、候補では裏づけられない。候補は既存の SRC-031（消化性潰瘍ガイドライン2026、OPEN 登録済み）を裏づけとして使う形を提案する。 |
| 確認経路 | 出典マスターで SRC-031（OPEN）を確認し、Europe PMC で2020年版英語版のライセンス（cc by）と章立てを確認（2026-11-11） |

### GD-095（出典：Ergüder E, et al. Lemmel syndrome: a single-center cohort and diagnostic considerations. Turk J Surg 2026;42(2):214-219（当該論文）の PubMed 抄録レコード）

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI 10.47717/turkjsurg.2026.2025-11-25、PMID 42100946、PMCID PMC13237573 |
| 区分 | GOV_US |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42100946&format=json&resultType=core |
| 裏づけ範囲 | 抄録が定義そのもの（総胆管結石がないのに乳頭周囲十二指腸憩室が総胆管を外から圧排して閉塞性黄疸を起こす）を明記し、MRCP が診断の鍵であること、ERCP が診断と治療の両方に使われたことを収載する。カードの主張の骨格が裏づけられる。 |
| 数値照合 | 該当なし |
| 備考 | 「ERCPは診断と治療の標準とされる」という位置づけの強さは抄録の記述（診断・治療に使用）よりやや強いため A ではなく B とした。区分の明確化：原典（SRC-047）は Europe PMC で CC BY-NC と確認され、マスターの UNKNOWN は RESTRICTED への明確化が適切である（D ではない申し送り）。あわせてマスター未登録の PMID 42100946・PMCID PMC13237573 の補完を提案する。 |
| 確認経路 | Europe PMC REST API（resultType=core）で抄録とライセンスを確認（2026-11-11） |

### GD-096（出典：Acute superior mesenteric artery syndrome in a young adult: case report. Annals of Medicine and Surgery 2025（CC BY）（補助：現出典 SRC-4211 の PubMed 抄録レコード））

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI なし、PMID 42866742、PMCID なし |
| 区分 | OPEN |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42866742&format=json&resultType=core |
| 裏づけ範囲 | CC BY 症例報告の抄録が「急激な体重減少と後腹膜脂肪（fat pad）の減少に続いて、大動脈と上腸間膜動脈の間で十二指腸が圧迫される」機序を明記し、現出典（Merrett 2009）の抄録も「十二指腸第3部が上腸間膜動脈に圧迫され、急激な体重減少が大動脈・上腸間膜動脈角を狭くする」と記載する。カードの病態（圧迫による閉塞＋腸間膜脂肪の減少が代表的誘因）が裏づけられる。 |
| 数値照合 | 該当なし |
| 備考 | 現出典（SRC-4211）の PMID はマスター未登録（null）のため、PMID 18810558 の補完を提案する。候補は症例報告であり、裏づけ用途に限る。 |
| 確認経路 | Europe PMC REST API で両論文の抄録とライセンス（cc by）を確認（2026-11-11） |

### GD-097（出典：Superior Mesenteric Artery Syndrome Across Adulthood: A Retrospective Clinicoradiological Study. Medicina 2025（CC BY）（新規登録候補））

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI 10.3390/medicina62091812、PMID 42796418、PMCID なし |
| 区分 | OPEN |
| ライセンス確認根拠 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42796418&format=json&resultType=core |
| 裏づけ範囲 | 造影CT で大動脈・上腸間膜動脈角（実測10〜25°）と両血管の距離（実測3〜8 mm）を計測し、十二指腸第3部の圧迫と口側の拡張を症状と合わせて診断する枠組みが、カードの診断裏づけ（角度・距離の閾値と口側の胃十二指腸拡張）と整合する。腹臥位などの体位による軽減は、現出典（SRC-4212）の抄録が体位変換を初期治療として挙げる範囲で方向が一致する。 |
| 数値照合 | 両値を記録する：カード 角度25度未満・距離8〜10 mm未満／候補コホートの実測範囲は角度10〜25°・距離3〜8 mm。候補は閾値そのものの明記ではなく診断確定例の実測範囲であり、カードの閾値と矛盾しないが、閾値の直接の裏づけは現出典本文に依る。 |
| 備考 | 現出典（SRC-4212、World J Clin Cases 2023）は Europe PMC で CC BY-NC と確認され、RESTRICTED のままが正しい。あわせてマスター未登録の PMID 37383896・PMCID PMC10294176 の補完を提案する。 |
| 確認経路 | Europe PMC REST API で抄録とライセンス（cc by）を確認（2026-11-11） |

### GD-099（出典：National Cancer Institute (NCI). Small Intestine Cancer Treatment (PDQ®) – Health Professional Version（米国政府））

| 項目 | 内容 |
|---|---|
| 候補の識別子 | DOI なし、PMID なし、PMCID なし |
| 区分 | GOV_US |
| ライセンス確認根拠 | https://www.cancer.gov/types/small-intestine/hp/small-intestine-treatment-pdq |
| 裏づけ範囲 | PDQ は「切除可能な場合は外科切除が主要な治療であり、治癒は完全切除の可否にかかる」とし、切除可能な原発腺癌には根治的外科切除を挙げる。十二指腸腫瘍では膵頭十二指腸切除または分節的十二指腸切除が選択肢となることも PDQ の治療方針と整合する。カードの「限局例では外科切除が基本、十二指腸原発では膵頭十二指腸切除または部分切除」は裏づけられる。 |
| 数値照合 | 該当なし |
| 備考 | 現出典は NCCN ガイドライン（SRC-4214）で RESTRICTED のまま。裏づけは NCI PDQ（GOV_US）による。あわせて SRC-4214 の PMID 31487687・PMCID PMC10191182 の補完を提案する（バッチ5でも同一出典について補完を報告済み）。 |
| 確認経路 | NCI PDQ（Health Professional Version）の本文を Kaiser Permanente 掲載の NCI 版と検索結果で照合（2026-11-11） |

## C 見つからない（7件）

| カード | 所見 |
|---|---|
| GD-072 | 胃静脈瘤の占居部位の記載分類（Lg-c・Lg-cf・Lg-f）は日本の内視鏡所見記載基準固有の文言で、自由な資料に同じ分類はない。肝硬変診療ガイドライン2020英語版（SRC-018）の PMC 全文を検索したが Lg 分類の記載はなく、裏づけにならない。現出典（SRC-017、日消誌・日内会誌）は RESTRICTED のまま。 |
| GD-086 | 数値群（PPI 使用者23%対非使用者12%、家族性大腸腺腫症での頻度20〜100%・異形成25〜41%、散発例の悪性化1%未満）は現出典（Islam 2013）本文由来で、同論文の抄録は総論的な記述のみで数値はない。Jalving 2006 の抄録は PPI 長期使用と胃底腺ポリープのリスク上昇（オッズ比）を示すが、23%・12% という値自体は抄録の確認範囲になく、確認できた CC BY 資料にも数値群の収載はなかった。 あわせて、現出典（SRC-043）の PMID はマスター未登録（null）のため、PMID 24764778 の補完を提案する。 |
| GD-087 | 除菌後の退縮率（約80%）、異形成1.9〜19%、腺癌0.6〜2.1% の数値は現出典（Islam 2013）本文が集約した研究値で、抄録になく、確認できた自由な資料にも収載はなかった。 |
| GD-088 | 胃腺腫が真の腫瘍で前駆病変であること、完全切除が勧められること、2 cm超・絨毛成分での腫瘍化リスク上昇を一体で載せる自由な資料は確認できなかった。現出典（Islam 2013）の抄録にも個別の記載はない。 |
| GD-091 | 酢酸亜鉛内服による胃体部の白苔を伴うびらん・発赤という所見は日本の報告固有で、自由な資料に同じ所見の記載はない。CC BY の粘膜変化総説（DEN Open 2024）が扱う6病変にも含まれない。 |
| GD-093 | 検査法別の頻度（上部消化管造影1〜6%、内視鏡12〜27%、剖検15〜22%）と乳頭周囲70〜75% という数値は現出典（Rizwan 2011）の総説本文の集約値で、同論文の抄録は膵炎を伴う症例報告が中心で数値はない。確認できた CC BY 資料は症例報告が中心で、この頻度表を載せるものはなかった。 |
| GD-094 | 合併症の列挙や「治療は症状のある憩室に限る」という方針自体は一般論として整合する資料があるが、主張の核である十二指腸憩室穿孔45例・全体死亡率31% という数値を載せる自由な資料はなく、C とした（バッチ5 IN-066 と同じ扱い）。現出典の抄録にも穿孔・死亡率の記載はない。 |

## D 区分の訂正（54件）

いずれも現出典の source_class が UNKNOWN で、Crossref の version-of-record ライセンスと Europe PMC の license 表示で CC BY 4.0（SRC-042 は CC BY）と確認できた。OPEN への訂正を提案する。

### SRC-028 機能性ディスペプシア診療ガイドライン2021（J Gastroenterol、DOI 10.1007/s00535-021-01843-7、PMID 35061057・PMCID PMC8831363 の補完も提案）

対象カード：GD-001、GD-002、GD-003、GD-004、GD-005、GD-006、GD-007、GD-008、GD-009、GD-010、GD-011、GD-012、GD-013、GD-014、GD-015、GD-016、GD-017、GD-018

### SRC-029 胃癌治療ガイドライン第6版（Gastric Cancer、DOI 10.1007/s10120-022-01331-8、PMID 36342574・PMCID PMC9813208 の補完も提案）

対象カード：GD-044、GD-048

### SRC-030 胃癌治療ガイドライン第7版（Gastric Cancer、DOI 10.1007/s10120-025-01698-4、PMID 41569370・PMCID PMC12956939 の補完も提案）

対象カード：GD-035、GD-036、GD-037、GD-038、GD-039、GD-040、GD-041、GD-042、GD-043、GD-045、GD-046、GD-047、GD-049、GD-050、GD-051、GD-052、GD-053、GD-054、GD-058、GD-059、GD-060、GD-061、GD-080

### SRC-032 GIST ガイドライン2022英語版（Int J Clin Oncol、DOI 10.1007/s10147-024-02488-1、PMCID PMC11130037 の補完も提案。PMID 38609732 は登録済み）

対象カード：GD-062、GD-063、GD-064、GD-065、GD-066、GD-067、GD-068、GD-070

### SRC-018 肝硬変診療ガイドライン2020（J Gastroenterol、DOI 10.1007/s00535-021-01788-x・PMID 34231046 の補完も提案。PMCID は登録済み）

対象カード：GD-073

### SRC-042 アニサキス全国調査（Emerg Infect Dis、DOI 10.3201/eid2810.220627、PMID 36148963・PMCID PMC9514333 の補完も提案）

対象カード：GD-084、GD-085
