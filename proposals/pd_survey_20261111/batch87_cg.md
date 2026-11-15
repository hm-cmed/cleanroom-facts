# バッチ87：CG（染色体・性分化・内分泌の先天異常）章 7件

## 集計

- A（置き換え可）：0件
- B（裏づけ追加可）：7件（すべて部分）
- C（見つからない）：0件
- D（マスター区分訂正）：2出典（いずれも UNKNOWN → RESTRICTED）。ほかに SRC-1030 の区分訂正はバッチ77で提案済みのため再掲（新規計上しない）

## 手続き注記

- 判定は2026-11-11のレポジトリ側指示（新ルール）に基づく。「抄録・添付文書・医学百科は根拠にしない」。使えるのは政府の全文文書・報告書、CC BY 全文、試験登録レコードなど全文で読める資料のみとし、抄録は数値の食い違い確認にのみ用いた。旧来の「先例に基づく A」は廃止。
- 主出典6件すべてについて、DOI／PMID／PMCID をキーに Europe PMC と Crossref で個別に照合し、カード記載の識別子はすべて一致した。識別子の誤記（別論文の識別子の混入）は本バッチでは発見されなかった。マスター側では SRC-3521〜3525 の pmid・pmcid が null のものが多く、カード側に既記の値を個別照会で照合のうえ補完候補とした（識別子補完候補の節参照）。
- 候補はいずれも全文を実際に読んで裏づけ範囲を判定し、ライセンスは候補ごとに Crossref の刊行版（version of record）データ、Europe PMC のライセンス要素、PMC 全文のライセンス要素で個別に確認した（いずれも CC BY 4.0）。Cureus 2025 は Crossref にライセンス登録がないため、Europe PMC のレコードと PMC 全文のライセンス要素で CC BY 4.0 を確認した。
- 主出典の区分確認：SRC-3523 は刊行版 CC BY-NC 4.0、SRC-3524 は CC BY-NC-ND 4.0 で、いずれも自由ではなく現行 RESTRICTED が正しい。SRC-3521 は AAP の著作物で非OA・ライセンス登録なし、現行 RESTRICTED が正しい。SRC-3522 と SRC-3525 は自由なライセンスがなく RESTRICTED への訂正候補とした。SRC-1030 はバッチ77で訂正提案済み（再掲）。
- 本バッチでは API のレート制限（429）は発生しなかった。

## 明細

| 対象 | 判定 | 現行出典（主出典） | 候補 | 区分 | PMID | DOI | PMCID | ライセンス根拠URL | 裏づけ範囲 | 数値照合 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CG-001 | B（部分） | SRC-3521 Bull MJ, Trotter T, Santoro SL, et al; Council on Genetics. Health Supervision for Children and Adolescents With Down Syndrome. Pediatrics. 2022;149(5):e2022057010 | Suárez-Mantilla SN, Africano-Leon ML, Mora-Bautista VM, Vergara-Arenas DC, Bustos-López AT, Serrano-Gomez S. Adherence to the American Academy of Pediatrics Health Supervision Guidelines for Children With Down Syndrome in a Tertiary Care Institution in Northeastern Colombia. Cureus. 2025;17(9):e93426 | CC BY 4.0（OPEN） | 41164047 | 10.7759/cureus.93426 | PMC12564101 | https://creativecommons.org/licenses/by/4.0/ | 部分：AAP の健康管理ガイドラインが年齢帯ごとに評価項目を定めるスケジュールであること、その中で新生児期（生後1か月以内）に先天性心疾患の評価として心エコーを行うこと、甲状腺機能は出生時の確認に加えて生後6か月・12か月に TSH を測定することを、ガイドラインへの遵守度を検証する表の形で再掲する。候補は同ガイドラインが2022年に最新改訂されたことにも触れている | 数値の主張はスケジュール項目のみ。候補の表は2011年版から改作されており、年齢帯は1か月未満・1〜12か月・1〜5歳・5〜12歳（13〜21歳の区分への言及あり）で、カードの2022年版の年齢帯（出生〜1か月、1か月〜1歳、1〜5歳、5〜12歳、12〜21歳）と大枠で一致する。12か月以降の毎年の甲状腺測定は候補の表に再掲なし（毎年の記載があるのは血算） | 主出典は American Academy of Pediatrics の著作物で、Europe PMC で非OA・全文収載なし、Crossref にライセンス登録はなく、現行 RESTRICTED が正しいことを個別確認した。マスターの pmid は null で、カード側に既記の PMID 35490285 を補完候補とした（識別子補完候補の節参照） |
| CG-002 | B（部分） | SRC-3522 Antonarakis SE, Skotko BG, Rafii MS, et al. Down syndrome. Nat Rev Dis Primers. 2020;6(1):9 | Izzo A, Mollo N, Nitti M, Paladino S, Calì G, Genesio R, Bonfiglio F, Cicatiello R, Barbato M, Sarnataro V, Conti A, Nitsch L. Mitochondrial dysfunction in down syndrome: molecular mechanisms and therapeutic targets. Mol Med. 2018;24(1):4 | CC BY 4.0（OPEN） | 30134785 | 10.1186/s10020-018-0004-y | PMC6016872 | https://creativecommons.org/licenses/by/4.0/ | 部分：21トリソミーが「出生後に生存可能な常染色体異数性の中で最も頻度が高い（the most common autosomal aneuploidy compatible with postnatal survival）」ことを再掲する。知的障害を含む複雑な表現型という位置づけも一致する | 候補は有病率を新生児700人に1人とし、カードに有病率の数値はないため競合しない。「21番染色体にはタンパク質をコードする遺伝子が200を超えて存在し、その過剰が臨床像の背景となる」という要素は候補に再掲なし（候補は21番染色体遺伝子の過剰発現が病態に関わることは述べるが、遺伝子数の記載はない） | 主出典は PMC に著者稿全文（PMC8428796）があるが非OAでライセンス表示はなく、Crossref の刊行版ライセンスもテキストマイニング用のみで CC ではないため自由とはみなさない。現行 UNKNOWN は RESTRICTED への訂正対象（区分訂正の節参照）。識別子補完候補あり（PMID・PMCID） |
| CG-003 | B（部分） | SRC-3523 Gravholt CH, Andersen NH, Christin-Maitre S, et al; International Turner Syndrome Consensus Group. Clinical practice guidelines for the care of girls and women with Turner syndrome. Eur J Endocrinol. 2024;190(6):G53-G151 | Turner HE, Johannsen EB, Smyth A, Orchard E, Gravholt CH. Approach to the Patient With Turner Syndrome. J Clin Endocrinol Metab. 2025;111(1):dgaf517 | CC BY 4.0（OPEN） | 40971503 | 10.1210/clinem/dgaf517 | PMC12712970 | https://creativecommons.org/licenses/by/4.0/ | 部分：Turner症候群が全ライフステージを通じて心血管異常、自己免疫疾患、骨格異常、代謝機能障害、神経認知面など複数の臓器・領域に影響し、管理には複数の専門領域の連携が関わることを再掲する。候補は国際ガイドラインに基づく合併症とモニタリングの表を備え、主出典（2024年版ガイドライン）の枠組みに沿った内容である | 有病率は候補では「出生女児2,000〜2,500人に1人」（100,000人あたり40〜50人）と幅で示され、カードの「女性100,000人あたり50人」はその上限と一致する。点値としての一致ではないため、裏づけ登録時は幅のある値として扱うこと。2024年版ガイドラインの8領域という構成そのものは候補に再掲なし | 主出典の刊行版ライセンスは CC BY-NC 4.0（Crossref・Europe PMC の双方で個別確認）で自由ではなく、現行 RESTRICTED が正しい。マスターの pmid・pmcid は null で、カード側に既記の値を補完候補とした（識別子補完候補の節参照） |
| CG-004 | B（部分） | SRC-3523 Gravholt CH, Andersen NH, Christin-Maitre S, et al; International Turner Syndrome Consensus Group. Clinical practice guidelines for the care of girls and women with Turner syndrome. Eur J Endocrinol. 2024;190(6):G53-G151 | Turner HE, Johannsen EB, Smyth A, Orchard E, Gravholt CH. Approach to the Patient With Turner Syndrome. J Clin Endocrinol Metab. 2025;111(1):dgaf517 | CC BY 4.0（OPEN） | 40971503 | 10.1210/clinem/dgaf517 | PMC12712970 | https://creativecommons.org/licenses/by/4.0/ | 部分：低身長への成長ホルモン治療が小児期・思春期の治療の柱であること、卵巣機能不全に対してエストロゲンによる思春期の誘導と性ホルモン補充が行われること、心血管異常を含む合併症が全生涯を通じて生じ、評価と継続的なモニタリング・管理が長期フォローアップの必須要素であることを再掲する | 数値の主張なし（枠組みのカード）。成長ホルモンの開始年齢の具体値（候補の症例では10歳開始）はカードの主張ではない | カードが述べる「成長」「思春期とエストロゲン治療」「心血管の健康」というガイドラインの領域立てそのものは候補に再掲がないが、各要素の実質は候補に再掲がある。主出典の区分・識別子補完候補は CG-003 の行と共通（SRC-3523） |
| CG-005 | B（部分） | SRC-3524 Zitzmann M, Aksglaede L, Corona G, et al. European Academy of Andrology guidelines on Klinefelter Syndrome. Andrology. 2021;9(1):145-167 | Anaforoğlu İ. Klinefelter syndrome beyond hypogonadism: multisystem manifestations and a framework for clinical surveillance. Front Endocrinol (Lausanne). 2026;17:1848181 | CC BY 4.0（OPEN） | 42422432 | 10.3389/fendo.2026.1848181 | PMC13341453 | https://creativecommons.org/licenses/by/4.0/ | 部分：Klinefelter症候群（47,XXY）が高ゴナドトロピン性性腺機能低下症、不妊、精巣機能の障害と関連すること、生殖機能にとどまらず心血管・代謝・骨・神経認知など多系統にわたる包括的な評価とサーベイランスが必要であることを再掲する。候補は主出典である欧州アンドロロジー学会の2021年ガイドラインを参照文献として位置づけている | 候補は有病率を男児出生450〜600人に1人、最大で75%が生涯未診断のままであるとし、カードの「有病率に比べて診断率はなお低い」という定性的主張と整合する。候補は「無精子症」という語自体は用いておらず、精子形成の障害は精巣形成不全・不妊の記述と、モザイク型では精子形成が比較的保たれるという対比から示される。ライディッヒ細胞の機能障害という表現そのものも候補に再掲なし。主出典が本症候群に対する初の国際ガイドラインであるという位置づけも候補に再掲なし | 主出典の刊行版ライセンスは CC BY-NC-ND 4.0（Crossref・Europe PMC の双方で個別確認）で自由ではなく、現行 RESTRICTED が正しい。マスターの pmid は null で、カード側に既記の PMID 32959490 を補完候補とした（識別子補完候補の節参照）。主出典は Europe PMC でも PMCID を持たない |
| CG-006 | B（部分） | SRC-3525 Carey JC. Perspectives on the care and advances in the management of children with trisomy 13 and 18. Am J Med Genet C Semin Med Genet. 2016;172(3):249-250 | Caggiano S, Persia S, D'Amore F, Macchiaiolo M, Fornari M, Clemente V, Paglietti MG, Schiavino A, Butera G, Filippelli S, Zucaro L, Cutrera R. Survival in infants with trisomy 18, palliative care and ethical reflections: a single center considerations. Ital J Pediatr. 2026;52(1) | CC BY 4.0（OPEN） | 41485045 | 10.1186/s13052-025-02181-7 | PMC12866181 | https://creativecommons.org/licenses/by/4.0/ | 部分：18トリソミーについて、先天異常を伴い従来は致死的な診断とみなされ、米国小児科学会も新生児蘇生の差し控えを検討するよう勧めていた時代があったこと、その後、心臓手術を含む治療的介入の増加とともに1年を超えて生存する児が増え（介入内容により3〜25%）、現在は明確な判断基準がなく、過剰治療と治療放棄の双方を避ける症例ごとの検討が課題であることを再掲する。これはカードの「一律の差し控えではなく、緩和ケア中心の対応と積極的介入の双方を症例ごとに検討する議論が進んでいる」という主張の骨格と一致する | カードに数値の主張はない。候補の生存割合（3〜25%）は介入内容に依存する幅のある値で、カードの主張の裏づけとしては用いない | 候補は18トリソミーのみを対象とし、13トリソミーと、生存した年長児における著明な認知・運動発達の障害については再掲がない。主出典は Wiley の利用条件のみで CC ではなく、現行 UNKNOWN は RESTRICTED への訂正対象（区分訂正の節参照）。識別子補完候補あり（PMID） |
| CG-010 | B（部分） | SRC-1030 Speiser PW, Arlt W, Auchus RJ, et al. Congenital Adrenal Hyperplasia Due to Steroid 21-Hydroxylase Deficiency: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2018;103(11):4043-4088 | Cera G, Corsello A, Novizio R, Di Donna V, Locantore P, Paragliola RM. Severe Hyperandrogenism in 46,XX Congenital Adrenal Hyperplasia: Molecular Physiopathology, Late Diagnoses, and Personalized Management. Int J Mol Sci. 2024;25(21):11779 | CC BY 4.0（OPEN） | 39519330 | 10.3390/ijms252111779 | PMC11545884 | https://creativecommons.org/licenses/by/4.0/ | 部分：先天性副腎皮質過形成の最も多い型が21-水酸化酵素欠損症であること、新生児スクリーニングが17-ヒドロキシプロゲステロン（17-OHP）の測定に基づくこと、塩喪失型ではミネラルコルチコイド作用の欠如により出生前後に副腎クリーゼを起こすリスクがあること、46,XX では外性器の男性化（Prader 分類の病期を含む）が性分化の評価と出生時の性別判定に関わることを再掲する | 数値の主張なし。副腎クリーゼの具体像（脱水・電解質異常・循環不全）の三徴そのものは候補に列挙がなく、裏づけは「ミネラルコルチコイド欠乏による副腎クリーゼのリスク」の範囲にとどまる。Endocrine Society の2018年ガイドラインがスクリーニングによる早期発見を前提に診療を組み立てているという位置づけ自体も候補に再掲なし | 主出典 SRC-1030 は IE 章と共有し、区分訂正（UNKNOWN→RESTRICTED）と PMCID 補完候補（PMC6456929）はバッチ77で提案済みのため本バッチでは再掲とする（二重計上しないこと）。バッチ77で IE-005・IE-006 に用いた候補（Fanis 2026）は新生児スクリーニングと塩喪失型の存在は扱うが、副腎クリーゼと46,XX の外性器男性化は扱わないため、本カードでは Cera 2024 を候補とした |

## 区分訂正（D）候補：2出典（いずれも UNKNOWN → RESTRICTED）＋再掲1出典

- SRC-3522（CG-002 の主出典）：Nat Rev Dis Primers（Springer Nature）。Crossref の刊行版ライセンスはテキストマイニング用リンクのみで CC ではない。PMC 収載分（PMC8428796）は著者稿で非OA、ライセンス表示なし。マスターの license_note は null で、実態は CC 表示なし
- SRC-3525（CG-006 の主出典）：Am J Med Genet C（Wiley）。Crossref の刊行版ライセンスは Wiley の利用条件（termsAndConditions#vor）のみで CC ではない。Europe PMC でも非OA・全文収載なし。マスターの license_note は null で、カード側の「表示なし」と実態は一致する
- SRC-1030（CG-010 の主出典、再掲）：バッチ77（IE-005・IE-006 と主出典を共有）で提案済みのため、ここでは再掲とし新規に計上しない。J Clin Endocrinol Metab（Endocrine Society）。Crossref にライセンス登録なし。PMC 収載分（PMC6456929）は非OAでライセンス表示なし
- 訂正対象でない主出典：SRC-3521 は AAP の著作物で Europe PMC で非OA、Crossref にライセンス登録がなく現行 RESTRICTED が正しい。SRC-3523 は刊行版 CC BY-NC 4.0、SRC-3524 は CC BY-NC-ND 4.0 で、いずれも現行 RESTRICTED が正しい（Crossref・Europe PMC の双方で個別確認）

## 識別子補完候補：6出典8項目（いずれも個別照会で照合済み、うち SRC-1030 はバッチ77で提案済みの再掲）

- SRC-3521：pmid 35490285。DOI 10.1542/peds.2022-057010 の Europe PMC 個別レコードで当該論文（Bull 2022、Pediatrics）の PMID であることを確認。マスターの pmid は null で、カード側には既記
- SRC-3522：pmid 32029743。DOI 10.1038/s41572-019-0143-7 の Europe PMC 個別レコードで当該論文（Antonarakis 2020）の PMID であることを確認。マスターの pmid は null で、カード側には既記
- SRC-3522：pmcid PMC8428796。同 DOI の Europe PMC 個別レコードで当該論文の PMCID であることを確認。マスターの pmcid は null で、カード側には既記。PMC 収載分は非OAでライセンス表示はなく、区分は RESTRICTED（区分訂正の対象）
- SRC-3523：pmid 38748847。DOI 10.1093/ejendo/lvae050 の Europe PMC 個別レコードで当該論文（Gravholt 2024）の PMID であることを確認。マスターの pmid は null で、カード側には既記
- SRC-3523：pmcid PMC11759048。同 DOI の Europe PMC 個別レコードで当該論文の PMCID であることを確認。マスターの pmcid は null で、カード側には既記
- SRC-3524：pmid 32959490。DOI 10.1111/andr.12909 の Europe PMC 個別レコードで当該論文（Zitzmann 2021）の PMID であることを確認。マスターの pmid は null で、カード側には既記。Europe PMC でも PMCID は持たない
- SRC-3525：pmid 27643592。DOI 10.1002/ajmg.c.31527 の Europe PMC 個別レコードで当該論文（Carey 2016）の PMID であることを確認。マスターの pmid は null で、カード側には既記。Europe PMC でも PMCID は持たない
- SRC-1030：pmcid PMC6456929（再掲）。バッチ77で提案済みのため二重に計上しないこと。マスターの pmcid は null。DOI 10.1210/jc.2018-01865 の Europe PMC 個別レコードで確認した。PMC 収載分は非OAでライセンス表示はなく、区分は RESTRICTED（区分訂正の対象）

## 申し送り

- 主出典6件すべての PMID・DOI・PMCID を、Europe PMC と Crossref で DOI／PMID／PMCID ごとに個別に再照会し、マスター・カードの記載と照合した。識別子の誤記（別論文の識別子の混入）は本バッチでは発見されなかった。マスター側で pmid・pmcid が null の出典が多く、カード側に既記の値を個別照合のうえ補完候補とした（識別子補完候補の節参照）。
- SRC-1030 は IE 章の IE-005・IE-006 と主出典を共有し、その区分訂正（UNKNOWN→RESTRICTED）と PMCID 補完候補（PMC6456929）はバッチ77で提案済みである。本バッチでは再掲とし、登録側の申し送りメモで二重に計上しないこと。
- CG-001 の候補（Cureus 2025）の遵守度表は AAP ガイドラインの2011年版から改作されたもので、2022年版の個別項目（12か月以降の毎年の甲状腺測定、12〜21歳帯の構成そのもの）は再掲がない。裏づけは年齢帯別の評価スケジュールの骨格、新生児期の心エコー、生後6か月・12か月の TSH 測定にとどまる。
- CG-002 の「21番染色体にはタンパク質をコードする遺伝子が200を超えて存在する」という要素は、今回確認した自由な全文のいずれにも再掲がなかった。候補（Izzo 2018）の裏づけは「出生後に生存可能な常染色体異数性の中で最も頻度が高い」という要素にとどまる。
- CG-003 の数値の扱い：候補（Turner 2025）は有病率を「出生女児2,000〜2,500人に1人」（100,000人あたり40〜50人）と幅で示し、カードの「女性100,000人あたり50人」はその上限と一致する。候補が点値としての50人を再掲しているわけではないため、裏づけ登録時は幅のある値として扱うこと。
- CG-005 の候補（Anaforoğlu 2026）は「無精子症」という語自体は用いておらず、精子形成の障害は精巣形成不全・不妊と、モザイク型では精子形成が比較的保たれるという対比から示される。また主出典（EAA ガイドライン2021）が本症候群に対する初の国際ガイドラインであるという位置づけは候補に再掲がない。
- CG-006 の候補（Caggiano 2026）は18トリソミーのみを対象とし、13トリソミーと、生存した年長児の認知・運動発達の障害については再掲がない。裏づけは18トリソミーに関する範囲（多発先天異常のパターン、死亡率の高さと介入による変化、差し控えから症例ごとの検討への移行）にとどまる。
- 「要・正本確認」に相当する、カードの値と主出典の食い違いは本バッチでは発見されなかった。監視事項（主出典の後継版）に相当するものも本バッチではない（CG-001 の主出典は2022年版が現行、CG-003・CG-004 の主出典は2024年版が現行であることを確認した）。
- 本バッチでは API のレート制限（429）は発生しなかった。主出典・候補はいずれも DOI・PMID・PMCID ごとの個別照会で確認した。
- 本バッチの判定は以上で完結しており、カードの主張・数値の変更は一切行っていない。
