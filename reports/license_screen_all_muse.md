# ライセンス未確認（UNKNOWN）出典の一括ふるい分け結果（残り全件）

実施：2026-11-24（依頼文 `request_license_screen_all.md` に基づく）。論文の本文は保存していない。

## 1. 対象の確定方法と件数

- 使用したレポジトリ：hm-cmed/cleanroom-facts 最新版、コミット `4503cb71e689b20e19a5cadc95ae62b10652ad08`（2026-11-24 00:12 UTC）。
- `data/sources/sources.yaml` の全 2,493 件中、`source_class: UNKNOWN` は 260 件。そのうち、いずれかのカードが `provenance.source_ref`（主出典）で使っているものは 246 件（主出典として未使用の 14 件＝SRC-008・019・443・445・446・581・1284・1285・1732・1760・1783・1798・3443・5129 は対象外）。
- 第1回・第2回で判定済みのものとして、自分の成果物（license_check_01.md・02.md）とレポジトリ側 reports（license_check_01_muse.md・02_muse.md）の対象を突き合わせた。最新マスターで UNKNOWN のまま残っていたのは SRC-115・SRC-116 の2件のみで、両方とも第1回判定済みのため除外した（残りは反映済みで UNKNOWN ではなくなっていた）。
- 添付文書・インタビューフォーム（製薬会社作成、UNKNOWN のまま据え置く対象）として除外したのは、SRC-117・118・119・120（PMDA 医薬品添付文書情報への URL のみで書誌未登録）、SRC-3978（フルマゼニル静注添付文書）、SRC-3983（ナロキソン塩酸塩静注添付文書）の6件（SRC-115・116 も添付文書だが、上の第1回判定済みとして数えた）。対象からの除外は合計8件。
- **判定対象は 238 件**（DOI あり 210 件、DOI なし 28 件）。

### ふるい分けの方法

- DOI があるもの：Crossref API の license 欄（content-version=vor）と、NCBI ID Converter／Europe PMC で PMC 収載の有無を確認。vor に CC 表示があるか PMC 収載があるもの（53件）は「詳しく確認」に回し、どちらもないもの（157件）は RESTRICTED とした。なお NCBI ID Converter の旧エンドポイントは移転していたため、新エンドポイントと Europe PMC で照合した。
- 「詳しく確認」：PMC 収載分は NCBI E-utilities（efetch）で PMC の XML を取得し、著者原稿（NIHMS）か刊行版か、© 表示と license 表示を確認した（著者原稿の表示は根拠にしていない）。
- DOI がないもの：1件ずつ発行元の表示を確認した。依頼文 §2 の「使い回し」表（StatPearls、American Family Physician、地方自治体の公開資料など）は調べ直さず適用した。

## 2. 集計

| 判定 | 件数 |
|---|---|
| OPEN | 1 |
| RESTRICTED | 235 |
| GOV_JP | 1 |
| GOV_US | 0 |
| 確認できず | 1 |
| 合計 | 238 |

- 「詳しく確認」に回したのは 81 件（DOI ありで PMC 収載のあった 53 件＋DOI なし 28 件）。そのうち OPEN になったのは SRC-3365（The Turkish Journal of Pediatrics）の1件のみ。
- 機械的に RESTRICTED とした 157 件は、これまでの第1回・第2回と同じく、OPEN になる要素（Crossref の CC 表示・PMC 刊行版収載）がなかったもの。

## 3. 「詳しく確認」に回したものと DOI がないものの根拠

### 3-1. PMC 収載があった DOI ありのもの（53件）

- **SRC-412**（RESTRICTED）：PMC 刊行版（PMC5803655）に「© 2013 by the American Thoracic Society」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC5803655/
- **SRC-428**（RESTRICTED）：PMC（PMC3576042）の収載は著者原稿（NIHMS180732）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC3576042/
- **SRC-542**（RESTRICTED）：PMC 刊行版（PMC1061212）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC1061212/
- **SRC-598**（RESTRICTED）：PMC 刊行版（PMC1720564）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC1720564/
- **SRC-603**（RESTRICTED）：PMC 刊行版（PMC2994083）に「© 2010 by the American Society of Nephrology」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC2994083/
- **SRC-661**（RESTRICTED）：PMC 刊行版（PMC4491294）に「© 2015 by the American Society of Nephrology」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC4491294/
- **SRC-747**（RESTRICTED）：PMC 刊行版（PMC5332236）に「© 2017 Canadian Urological Association or its licensors」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC5332236/
- **SRC-790**（RESTRICTED）：PMC 刊行版（PMC6019344）に「© 2018 Joule Inc. or its licensors」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC6019344/
- **SRC-822**（RESTRICTED）：PMC 刊行版（PMC7073417）に「© 2013 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd.」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC7073417/
- **SRC-836**（RESTRICTED）：PMC 刊行版（PMC7057272）に「© 2019 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd.」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC7057272/
- **SRC-839**（RESTRICTED）：PMC（PMC4175743）の収載は著者原稿（NIHMS619893）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 収載原稿中の権利表示：© 2014 Massachusetts Medical Society.。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC4175743/
- **SRC-842**（RESTRICTED）：PMC 刊行版（PMC4212440）に「© The Author(s), 2014」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC4212440/
- **SRC-846**（RESTRICTED）：PMC（PMC4890704）の収載は著者原稿（NIHMS789275）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC4890704/
- **SRC-950**（RESTRICTED）：PMC（PMC1370926）の収載は著者原稿（NIHMS5217）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC1370926/
- **SRC-951**（RESTRICTED）：PMC（PMC8697255）の収載は著者原稿（NIHMS1735229）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC8697255/
- **SRC-967**（RESTRICTED）：PMC 刊行版（PMC5393479）に「© 2014 by The Endocrine Society」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC5393479/
- **SRC-968**（RESTRICTED）：PMC 刊行版（PMC6174196）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC6174196/
- **SRC-982**（RESTRICTED）：PMC 刊行版（PMC6283429）に「© 2017 by the Endocrine Society」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC6283429/
- **SRC-993**（RESTRICTED）：PMC 刊行版（PMC3512229）に「© 2012 by The American Society of Hematology」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC3512229/
- **SRC-1108**（RESTRICTED）：PMC 刊行版（PMC3022978）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC3022978/
- **SRC-1114**（RESTRICTED）：PMC（PMC5978683）の収載は著者原稿（NIHMS964138）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC5978683/
- **SRC-1124**（RESTRICTED）：PMC（PMC5548388）の収載は著者原稿（NIHMS889795）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC5548388/
- **SRC-1178**（RESTRICTED）：PMC（PMC5025328）の収載は著者原稿（NIHMS771235）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC5025328/
- **SRC-1184**（RESTRICTED）：PMC 刊行版（PMC7025440）に「© 2015 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd.」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC7025440/
- **SRC-1271**（RESTRICTED）：PMC 刊行版（PMC5475221）の license 表示は「All Rights Reserved」、© 2017 American Society for Microbiology。CC 表示なし → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC5475221/
- **SRC-1272**（RESTRICTED）：PMC（PMC8526627）の収載は著者原稿（NIHMS1695223）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC8526627/
- **SRC-1283**（RESTRICTED）：PMC（PMC4422053）の収載は著者原稿（NIHMS677065）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 収載原稿中の権利表示：© 2015 Massachusetts Medical Society.。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC4422053/
- **SRC-1294**（RESTRICTED）：PMC 刊行版（PMC5710547）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC5710547/
- **SRC-1305**（RESTRICTED）：PMC（PMC5462106）の収載は著者原稿（NIHMS862580）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC5462106/
- **SRC-1312**（RESTRICTED）：PMC（PMC8935739）の収載は著者原稿（NIHMS1775274）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC8935739/
- **SRC-1313**（RESTRICTED）：PMC（PMC9073858）の収載は著者原稿（NIHMS1694798）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC9073858/
- **SRC-1387**（RESTRICTED）：PMC 刊行版（PMC6671929）に「© 2019 Cold Spring Harbor Laboratory Press; all rights reserved」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC6671929/
- **SRC-1437**（RESTRICTED）：PMC（PMC4478082）の収載は著者原稿（NIHMS695420）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC4478082/
- **SRC-1677**（RESTRICTED）：PMC（PMC3729880）の収載は著者原稿（NIHMS464952）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC3729880/
- **SRC-1679**（RESTRICTED）：PMC 刊行版（PMC8106615）に「© 2020 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd.」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC8106615/
- **SRC-1706**（RESTRICTED）：PMC 刊行版（PMC4409581）に「© 2015 American Academy of Neurology」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC4409581/
- **SRC-1710**（RESTRICTED）：PMC 刊行版（PMC4749120）に「© American Epilepsy Society」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC4749120/
- **SRC-1733**（RESTRICTED）：PMC 刊行版（PMC1545152）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC1545152/
- **SRC-1802**（RESTRICTED）：PMC 刊行版（PMC6440254）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC6440254/
- **SRC-1890**（RESTRICTED）：PMC 刊行版（PMC3528062）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC3528062/
- **SRC-1892**（RESTRICTED）：PMC 刊行版（PMC2690733）に「© The Association of Bone and Joint Surgeons 2008」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC2690733/
- **SRC-3168**（RESTRICTED）：PMC 刊行版（PMC8094626）に「© 2020 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd.」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC8094626/
- **SRC-3171**（RESTRICTED）：PMC（PMC10176440）の収載は著者原稿（NIHMS1822679）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC10176440/
- **SRC-3252**（RESTRICTED）：PMC 刊行版（PMC12690181）に © 2025 by the American Diabetes Association と、ADA の独自ライセンス（出典明記・無改変を条件に教育・非商用利用のみ）へのリンク表示がある。CC ライセンスではないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC12690181/
- **SRC-3256**（RESTRICTED）：PMC 刊行版（PMC6880896）に「© 2019 by The American Society of Hematology」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC6880896/
- **SRC-3433**（RESTRICTED）：PMC 刊行版（PMC6494160）に「© 2018 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd.」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC6494160/
- **SRC-3439**（RESTRICTED）：PMC（PMC2799187）の収載は著者原稿（NIHMS161274）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC2799187/
- **SRC-3445**（RESTRICTED）：PMC 刊行版（PMC1702305）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC1702305/
- **SRC-3739**（RESTRICTED）：PMC 刊行版（PMC6794707）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC6794707/
- **SRC-4377**（RESTRICTED）：PMC 刊行版（PMC3693028）が収載されているが、CC ライセンスの表示はなく、Crossref の vor license 欄にも CC はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC3693028/
- **SRC-4398**（RESTRICTED）：PMC 刊行版（PMC2572665）に「© 2008 Canadian Medical Association」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC2572665/
- **SRC-4624**（RESTRICTED）：PMC（PMC3596108）の収載は著者原稿（NIHMS446406）のみで、刊行版の CC 表示は Crossref・PMC のいずれでも確認できない。著者原稿の表示は根拠にしないため RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC3596108/
- **SRC-4968**（RESTRICTED）：PMC 刊行版（PMC3342598）に「©2012 Baishideng Publishing Group Co., Limited. All rights reserved.」の表示があり、CC ライセンスの表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC3342598/

### 3-2. DOI がないもの（28件）

- **SRC-126**（RESTRICTED）：財団（Rome Foundation）のウェブサイトのページで、CC ライセンスの表示はない。ページからリンクされる Rome IV 論文は Gastroenterology 誌の掲載版。 根拠：https://theromefoundation.org/?p=565
- **SRC-357**（GOV_JP）：札幌市保健所の公開資料。地方自治体の公開資料は GOV_JP とする決定（2026-11-24）による。 根拠：—（マスターに URL 登録なし）
- **SRC-380**（RESTRICTED）：OMIM は Johns Hopkins University が著作権を持ち、利用は個人・教育・研究目的に限られ、再配布にはライセンスが必要（OMIM の Legal Statement）。米国連邦政府の著作物ではない。 根拠：https://www.ncbi.nlm.nih.gov/books/NBK21108/pdf/Bookshelf_NBK21108.pdf
- **SRC-425**（RESTRICTED）：PMID 15613668 から DOI 10.1001/jama.292.24.2997 を同定。Crossref の license 欄に CC はなく、ID Converter でも PMC 収載なし → RESTRICTED。 根拠：https://api.crossref.org/works/10.1001/jama.292.24.2997
- **SRC-432**（RESTRICTED）：題名・誌名・巻ページから論文を同定。Crossref の vor license 欄と PMC 刊行版（PMC10870872）の表示が CC BY-NC-ND 4.0 → RESTRICTED。 根拠：https://api.crossref.org/works/10.1164/rccm.202303-0558WS
- **SRC-433**（RESTRICTED）：PMID 10793162 から DOI を同定。Crossref に CC はなく PMC 収載もない → RESTRICTED。 根拠：https://api.crossref.org/works/10.1056/NEJM200005043421801
- **SRC-471**（RESTRICTED）：『がんの統計／Cancer Statistics in Japan』は公益財団法人 がん研究振興財団の刊行物で、府省・地方自治体の資料には当たらず、CC 表示もない → RESTRICTED。 根拠：https://www.fpcr.or.jp/pdf/pamphlet/cancer_statistics_2025.pdf
- **SRC-534**（RESTRICTED）：PMID 27162815 から PMC 刊行版（PMC4771236）を同定。刊行版の表示は © 2013 Trauma Research Center, Shiraz University of Medical Sciences で、CC 表示はない → RESTRICTED。 根拠：https://pmc.ncbi.nlm.nih.gov/articles/PMC4771236/
- **SRC-728**（RESTRICTED）：Minerva Urol Nefrol は購読誌で、PMC 収載も CC 表示もない → RESTRICTED。 根拠：https://pubmed.ncbi.nlm.nih.gov/26583595/
- **SRC-814**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://www.ncbi.nlm.nih.gov/books/NBK441996/
- **SRC-815**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://www.ncbi.nlm.nih.gov/books/NBK470216/
- **SRC-823**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://www.ncbi.nlm.nih.gov/books/NBK549822/
- **SRC-978**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://www.ncbi.nlm.nih.gov/books/NBK526080/
- **SRC-989**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://www.ncbi.nlm.nih.gov/books/NBK493187/
- **SRC-994**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://www.ncbi.nlm.nih.gov/books/NBK441835/
- **SRC-995**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://www.ncbi.nlm.nih.gov/books/NBK537339/
- **SRC-1104**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://pubmed.ncbi.nlm.nih.gov/29261940/
- **SRC-1105**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://pubmed.ncbi.nlm.nih.gov/29763149/
- **SRC-1106**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://pubmed.ncbi.nlm.nih.gov/31424869/
- **SRC-1123**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://pubmed.ncbi.nlm.nih.gov/30335343/
- **SRC-1183**（RESTRICTED）：StatPearls（NCBI Bookshelf）の章。第1回・第2回で確認済みの使い回し（章ページの表示が CC BY-NC-ND 4.0）→ RESTRICTED。 根拠：https://pubmed.ncbi.nlm.nih.gov/28613683/
- **SRC-1547**（RESTRICTED）：PMC 収載も CC 表示もない → RESTRICTED。 根拠：https://pubmed.ncbi.nlm.nih.gov/15847102/
- **SRC-1871**（RESTRICTED）：American Family Physician は第1回・第2回で確認済みの使い回し（全号 PDF のフッターに © AAFP、私的・非商用の利用のみ）→ RESTRICTED。 根拠：https://pubmed.ncbi.nlm.nih.gov/30811157/
- **SRC-1882**（RESTRICTED）：PMC 収載も CC 表示もない → RESTRICTED。 根拠：https://pubmed.ncbi.nlm.nih.gov/15466720/
- **SRC-2486**（RESTRICTED）：『Haemovigilance by JRCS 2024』は日本赤十字社（特殊法人）の年報で、府省・地方自治体の資料には当たらず、PDF に CC 表示はない → RESTRICTED。 根拠：https://www.jrc.or.jp/mr/relate/info/pdf/Haemovigilance%20by%20JRCS%202024-2.pdf
- **SRC-2488**（RESTRICTED）：『日本における造血細胞移植／細胞治療 2025年度全国調査報告書』は一般社団法人 日本造血細胞移植データセンターと学会の報告書で、政府資料には当たらず、CC 表示もない → RESTRICTED。 根拠：http://www.jdchct.or.jp/data/report/2025/0.pdf
- **SRC-3365**（OPEN）：The Turkish Journal of Pediatrics の公式サイトの Open Access Statement は「全論文を CC BY 4.0 で公開」とし、1958年以降のバックファイルの論文ページにも「distributed under the Creative Commons Attribution License (CC BY)」の表示がある。本論文（1998;40(1):35-44）も同誌のバックファイルとして同サイトで公開されている → OPEN。 根拠：https://turkjpediatr.org/about
- **SRC-3444**（確認できず）：Journal of the Pakistan Medical Association の公式 Open Access ページは CC BY 4.0 を掲げるが、現行ページのみで、2016年刊行の本論文自体にライセンス表示があるか、方針が当時から適用されていたかを確認できなかった。推定で OPEN にはせず「確認できず」とする。 根拠：https://jpma.org.pk/index.php/public_html/Files/ER/OpenAccess

## 4. 機械可読の一覧表（全件）

| SRC | 判定 | ライセンスの表示 | 根拠の URL | 備考 |
|---|---|---|---|---|
| SRC-125 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.24875/NGL.23000008 |  |
| SRC-126 | RESTRICTED | Rome Foundation 公式サイトのページ。CC 表示なし（掲載論文自体は Gastroenterology 誌掲載版） | https://theromefoundation.org/?p=565 |  |
| SRC-186 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1253/circj.72.489 |  |
| SRC-208 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1253/circj.CJ-13-1482 |  |
| SRC-357 | GOV_JP | 札幌市保健所（地方自治体）の公開ページ | —（マスターに URL 登録なし） |  |
| SRC-376 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.resinv.2021.01.007 |  |
| SRC-380 | RESTRICTED | © Johns Hopkins University。個人・教育・研究目的の利用のみで、再配布・商用利用は大学のライセンスが必要 | https://www.ncbi.nlm.nih.gov/books/NBK21108/pdf/Bookshelf_NBK21108.pdf |  |
| SRC-411 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1183/13993003.00158-2025 | PMID候補 40774805（Europe PMC で確認、マスター未登録） |
| SRC-412 | RESTRICTED | PMC 刊行版に © 2013 by the American Thoracic Society の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC5803655/ | PMCID候補 PMC5803655（マスター未登録） |
| SRC-414 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa1402584 | PMID候補 24836310（Europe PMC で確認、マスター未登録） |
| SRC-415 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa1402582 | PMID候補 24836312（Europe PMC で確認、マスター未登録） |
| SRC-416 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa2414108 |  |
| SRC-418 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa1908681 | PMID候補 31566307（Europe PMC で確認、マスター未登録） |
| SRC-419 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa1903076 | PMID候補 31112379（Europe PMC で確認、マスター未登録） |
| SRC-425 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1001/jama.292.24.2997 | DOI候補 10.1001/jama.292.24.2997（Europe PMC で確認、マスター未登録） |
| SRC-428 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS180732）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC3576042/ | PMCID候補 PMC3576042（マスター未登録）。PMID候補 20171521（Europe PMC で確認、マスター未登録） |
| SRC-432 | RESTRICTED | CC BY-NC-ND 4.0 | https://api.crossref.org/works/10.1164/rccm.202303-0558WS | DOI候補 10.1164/rccm.202303-0558WS、PMID候補 37487152、PMCID候補 PMC10870872（いずれも Crossref・Europe PMC で確認、マスター未登録） |
| SRC-433 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJM200005043421801 | DOI候補 10.1056/NEJM200005043421801（Europe PMC で確認、マスター未登録） |
| SRC-434 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa1214103 | PMID候補 23688302（Europe PMC で確認、マスター未登録） |
| SRC-447 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa2008470 |  |
| SRC-471 | RESTRICTED | 公益財団法人がん研究振興財団の刊行物。CC 表示なし | https://www.fpcr.or.jp/pdf/pamphlet/cancer_statistics_2025.pdf |  |
| SRC-476 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa1913662 | PMID候補 31751012（Europe PMC で確認、マスター未登録） |
| SRC-530 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1093/clinids/7.2.200 |  |
| SRC-531 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.48095/ccrvch2024502 |  |
| SRC-534 | RESTRICTED | PMC 刊行版に © 2013 Trauma Research Center, Shiraz University of Medical Sciences の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC4771236/ | PMCID候補 PMC4771236（マスター未登録） |
| SRC-539 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1148/rg.243045005 |  |
| SRC-542 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC1061212/ | PMCID候補 PMC1061212（マスター未登録） |
| SRC-569 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa2404873 | PMID候補 39268857（Europe PMC で確認、マスター未登録） |
| SRC-574 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1681/ASN.2008010092 |  |
| SRC-580 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1053/j.ajkd.2016.10.032 |  |
| SRC-586 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1007/s10157-025-02636-5 |  |
| SRC-596 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1093/ndt/16.5.953 |  |
| SRC-598 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC1720564/ | PMCID候補 PMC1720564（マスター未登録） |
| SRC-603 | RESTRICTED | PMC 刊行版に © 2010 by the American Society of Nephrology の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC2994083/ | PMCID候補 PMC2994083（マスター未登録） |
| SRC-661 | RESTRICTED | PMC 刊行版に © 2015 by the American Society of Nephrology の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC4491294/ | PMCID候補 PMC4491294（マスター未登録） |
| SRC-728 | RESTRICTED | 出版社（Minerva Medica）の購読誌。CC 表示なし | https://pubmed.ncbi.nlm.nih.gov/26583595/ |  |
| SRC-747 | RESTRICTED | PMC 刊行版に © 2017 Canadian Urological Association or its licensors の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC5332236/ | PMCID候補 PMC5332236（マスター未登録） |
| SRC-771 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1093/jnci/djx214 |  |
| SRC-790 | RESTRICTED | PMC 刊行版に © 2018 Joule Inc. or its licensors の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC6019344/ | PMCID候補 PMC6019344（マスター未登録） |
| SRC-813 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1152/physrev.00031.2019 |  |
| SRC-814 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://www.ncbi.nlm.nih.gov/books/NBK441996/ |  |
| SRC-815 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://www.ncbi.nlm.nih.gov/books/NBK470216/ |  |
| SRC-818 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1002/ijgo.12666 |  |
| SRC-822 | RESTRICTED | PMC 刊行版に © 2013 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd. の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC7073417/ | PMCID候補 PMC7073417（マスター未登録） |
| SRC-823 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://www.ncbi.nlm.nih.gov/books/NBK549822/ |  |
| SRC-825 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1210/er.2009-0006 |  |
| SRC-829 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.fertnstert.2021.02.010 |  |
| SRC-831 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.fertnstert.2021.01.051 |  |
| SRC-833 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.fertnstert.2018.08.027 |  |
| SRC-835 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1080/13697130500148875 |  |
| SRC-836 | RESTRICTED | PMC 刊行版に © 2019 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd. の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC7057272/ | PMCID候補 PMC7057272（マスター未登録） |
| SRC-837 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.beem.2007.11.001 |  |
| SRC-839 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS619893）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC4175743/ | PMCID候補 PMC4175743（マスター未登録） |
| SRC-840 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1210/er.2009-0041 |  |
| SRC-842 | RESTRICTED | PMC 刊行版に © The Author(s), 2014 の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC4212440/ | PMCID候補 PMC4212440（マスター未登録） |
| SRC-843 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/AOG.0000000000002400 |  |
| SRC-844 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/AOG.0000000000001047 |  |
| SRC-846 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS789275）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC4890704/ | PMCID候補 PMC4890704（マスター未登録） |
| SRC-848 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1001/jama.288.3.321 |  |
| SRC-850 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/GME.0000000000001609 |  |
| SRC-852 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/GME.0000000000001174 |  |
| SRC-854 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/GME.0000000000002200 |  |
| SRC-855 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.contraception.2016.02.006 |  |
| SRC-857 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1210/jc.2016-2118 |  |
| SRC-872 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1542/peds.2008-1783 |  |
| SRC-882 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1530/EJE-17-0009 |  |
| SRC-883 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1210/jc.2011-0179 |  |
| SRC-894 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1038/nrdp.2016.78 |  |
| SRC-901 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMra1510030 |  |
| SRC-904 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1507/endocrj.EJ21-0238 |  |
| SRC-907 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.beem.2019.101367 |  |
| SRC-908 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1210/jc.2002-021799 |  |
| SRC-909 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMra021194 |  |
| SRC-915 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S0140-6736(11)60276-6 |  |
| SRC-950 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS5217）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC1370926/ | PMCID候補 PMC1370926（マスター未登録） |
| SRC-951 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS1735229）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC8697255/ | PMCID候補 PMC8697255（マスター未登録） |
| SRC-967 | RESTRICTED | PMC 刊行版に © 2014 by The Endocrine Society の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC5393479/ | PMCID候補 PMC5393479（マスター未登録） |
| SRC-968 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC6174196/ | PMCID候補 PMC6174196（マスター未登録） |
| SRC-973 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1093/eurheartj/ehz455 |  |
| SRC-974 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa1615664 |  |
| SRC-975 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1253/circj.66.987 |  |
| SRC-976 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa2032183 |  |
| SRC-978 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://www.ncbi.nlm.nih.gov/books/NBK526080/ |  |
| SRC-980 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa1805689 |  |
| SRC-981 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.pan.2020.06.005 |  |
| SRC-982 | RESTRICTED | PMC 刊行版に © 2017 by the Endocrine Society の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC6283429/ | PMCID候補 PMC6283429（マスター未登録） |
| SRC-989 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://www.ncbi.nlm.nih.gov/books/NBK493187/ |  |
| SRC-993 | RESTRICTED | PMC 刊行版に © 2012 by The American Society of Hematology の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC3512229/ | PMCID候補 PMC3512229（マスター未登録） |
| SRC-994 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://www.ncbi.nlm.nih.gov/books/NBK441835/ |  |
| SRC-995 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://www.ncbi.nlm.nih.gov/books/NBK537339/ |  |
| SRC-996 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1002/ajmg.c.31552 |  |
| SRC-999 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1007/BF00861588 |  |
| SRC-1104 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://pubmed.ncbi.nlm.nih.gov/29261940/ | Bookshelf ID がマスターに未登録のため根拠 URL は PubMed |
| SRC-1105 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://pubmed.ncbi.nlm.nih.gov/29763149/ | Bookshelf ID がマスターに未登録のため根拠 URL は PubMed |
| SRC-1106 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://pubmed.ncbi.nlm.nih.gov/31424869/ | Bookshelf ID がマスターに未登録のため根拠 URL は PubMed |
| SRC-1108 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC3022978/ | PMCID候補 PMC3022978（マスター未登録） |
| SRC-1110 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.jaci.2015.08.034 |  |
| SRC-1111 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1007/s10147-007-0751-1 |  |
| SRC-1113 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1111/j.1365-2133.2008.08713.x |  |
| SRC-1114 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS964138）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC5978683/ | PMCID候補 PMC5978683（マスター未登録） |
| SRC-1117 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa1805131 |  |
| SRC-1123 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://pubmed.ncbi.nlm.nih.gov/30335343/ | Bookshelf ID がマスターに未登録のため根拠 URL は PubMed |
| SRC-1124 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS889795）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC5548388/ | PMCID候補 PMC5548388（マスター未登録） |
| SRC-1125 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1200/JCO.2010.28.7078 |  |
| SRC-1126 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1001/jama.292.22.2771 |  |
| SRC-1167 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1684/ejd.2014.2402 |  |
| SRC-1174 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.det.2014.03.007 |  |
| SRC-1175 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S0140-6736(14)60763-7 |  |
| SRC-1178 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS771235）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC5025328/ | PMCID候補 PMC5025328（マスター未登録） |
| SRC-1179 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1212/CON.0000000000000813 |  |
| SRC-1181 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1001/jama.2016.8825 |  |
| SRC-1183 | RESTRICTED | CC BY-NC-ND 4.0（StatPearls 章ページの表示） | https://pubmed.ncbi.nlm.nih.gov/28613683/ | Bookshelf ID がマスターに未登録のため根拠 URL は PubMed |
| SRC-1184 | RESTRICTED | PMC 刊行版に © 2015 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd. の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC7025440/ | PMCID候補 PMC7025440（マスター未登録） |
| SRC-1193 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1067/s0190-9622(03)00896-x |  |
| SRC-1195 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.jaad.2023.12.017 |  |
| SRC-1196 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.jaad.2017.04.1141 |  |
| SRC-1197 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1007/s40257-017-0334-5 |  |
| SRC-1198 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.2340/00015555-2846 |  |
| SRC-1199 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.2165/00128071-200506050-00003 |  |
| SRC-1253 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.survophthal.2016.03.005 |  |
| SRC-1259 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.jtos.2017.05.008 |  |
| SRC-1261 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/ICO.0000000000000408 |  |
| SRC-1263 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.survophthal.2021.02.013 |  |
| SRC-1267 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1001/jama.2020.21899 |  |
| SRC-1268 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.ophtha.2004.03.029 |  |
| SRC-1271 | RESTRICTED | PMC 刊行版に © 2017 American Society for Microbiology・All Rights Reserved 表示 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5475221/ | PMCID候補 PMC5475221（マスター未登録） |
| SRC-1272 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS1695223）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC8526627/ | PMCID候補 PMC8526627（マスター未登録） |
| SRC-1275 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S1474-4422(22)00200-9 |  |
| SRC-1279 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1038/s41572-020-0158-0 |  |
| SRC-1280 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1001/jama.2022.6290 |  |
| SRC-1281 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S0161-6420(03)00475-5 |  |
| SRC-1282 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.ophtha.2018.04.007 |  |
| SRC-1283 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS677065）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC4422053/ | PMCID候補 PMC4422053（マスター未登録） |
| SRC-1286 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1161/STR.0000000000000366 |  |
| SRC-1287 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S0140-6736(07)60198-6 |  |
| SRC-1289 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/ICU.0b013e32835f8e6b |  |
| SRC-1290 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S0140-6736(12)60282-7 |  |
| SRC-1291 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa054481 |  |
| SRC-1293 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/IAE.0000000000000349 |  |
| SRC-1294 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC5710547/ | PMCID候補 PMC5710547（マスター未登録） |
| SRC-1297 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S0039-6257(97)84041-6 |  |
| SRC-1298 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1136/bjophthalmol-2018-313356 |  |
| SRC-1305 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS862580）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC5462106/ | PMCID候補 PMC5462106（マスター未登録） |
| SRC-1309 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.ophtha.2011.07.013 |  |
| SRC-1310 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.3109/08820538.2013.825276 |  |
| SRC-1312 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS1775274）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC8935739/ | PMCID候補 PMC8935739（マスター未登録） |
| SRC-1313 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS1694798）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC9073858/ | PMCID候補 PMC9073858（マスター未登録） |
| SRC-1314 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.ajo.2015.01.022 |  |
| SRC-1343 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1177/0194599813517083 |  |
| SRC-1344 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1177/0194599816671491 |  |
| SRC-1346 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.anl.2025.02.001 |  |
| SRC-1347 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/MAO.0000000000003160 |  |
| SRC-1358 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1055/s-2006-945518 |  |
| SRC-1361 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/MAO.0b013e3181ca843d |  |
| SRC-1362 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1159/000490277 |  |
| SRC-1369 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S0030-6665(03)00172-5 |  |
| SRC-1387 | RESTRICTED | PMC 刊行版に © 2019 Cold Spring Harbor Laboratory Press; all rights reserved の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC6671929/ | PMCID候補 PMC6671929（マスター未登録） |
| SRC-1388 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1001/jama.2020.17647 |  |
| SRC-1431 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1111/j.1529-8019.2010.01320.x |  |
| SRC-1437 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS695420）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC4478082/ | PMCID候補 PMC4478082（マスター未登録） |
| SRC-1438 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1111/odi.12646 |  |
| SRC-1443 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S0140-6736(19)30956-0 |  |
| SRC-1445 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1002/lary.23843 |  |
| SRC-1447 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.otc.2015.10.005 |  |
| SRC-1448 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1200/JCO.21.00449 |  |
| SRC-1449 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1177/0003489416665194 |  |
| SRC-1451 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1056/NEJMoa1506007 |  |
| SRC-1452 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.clp.2018.07.012 |  |
| SRC-1453 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.otohns.2010.02.026 |  |
| SRC-1524 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.ad.2018.05.005 |  |
| SRC-1526 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S0022-3476(97)70249-X |  |
| SRC-1527 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1542/peds.2014-3673 |  |
| SRC-1534 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.3949/ccjm.83a.15061 |  |
| SRC-1537 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1136/jmg.2009.072785 |  |
| SRC-1546 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1001/jama.241.25.2731 |  |
| SRC-1547 | RESTRICTED | 購読誌（Int J Tissue React）。CC 表示なし | https://pubmed.ncbi.nlm.nih.gov/15847102/ |  |
| SRC-1548 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.36849/JDD.10209 |  |
| SRC-1676 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1038/nrdp.2015.5 |  |
| SRC-1677 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS464952）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC3729880/ | PMCID候補 PMC3729880（マスター未登録） |
| SRC-1678 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1038/nrneurol.2015.86 |  |
| SRC-1679 | RESTRICTED | PMC 刊行版に © 2020 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd. の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC8106615/ | PMCID候補 PMC8106615（マスター未登録） |
| SRC-1683 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1111/ajad.12372 |  |
| SRC-1700 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1177/1060028016657553 |  |
| SRC-1701 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1111/epi.12550 |  |
| SRC-1706 | RESTRICTED | PMC 刊行版に © 2015 American Academy of Neurology の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC4409581/ | PMCID候補 PMC4409581（マスター未登録） |
| SRC-1709 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1111/epi.13121 |  |
| SRC-1710 | RESTRICTED | PMC 刊行版に © American Epilepsy Society の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC4749120/ | PMCID候補 PMC4749120（マスター未登録） |
| SRC-1733 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC1545152/ | PMCID候補 PMC1545152（マスター未登録） |
| SRC-1782 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1177/0269215514540919 |  |
| SRC-1785 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.spinee.2017.08.241 |  |
| SRC-1791 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/PEP.0000000000001114 |  |
| SRC-1794 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/BRS.0b013e3181354501 |  |
| SRC-1796 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1177/03635465241264804 |  |
| SRC-1802 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC6440254/ | PMCID候補 PMC6440254（マスター未登録） |
| SRC-1803 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/01.wco.0000200547.22292.11 |  |
| SRC-1804 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1212/wnl.59.4.499 |  |
| SRC-1871 | RESTRICTED | © AAFP（American Family Physician の定型表示） | https://pubmed.ncbi.nlm.nih.gov/30811157/ |  |
| SRC-1873 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.jse.2009.04.006 |  |
| SRC-1879 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1007/s00132-013-2226-6 |  |
| SRC-1882 | RESTRICTED | 購読誌（J Bone Joint Surg Am）。CC 表示なし | https://pubmed.ncbi.nlm.nih.gov/15466720/ |  |
| SRC-1883 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1007/s00774-009-0080-8 |  |
| SRC-1887 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/MOP.0000000000000842 |  |
| SRC-1890 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC3528062/ | PMCID候補 PMC3528062（マスター未登録） |
| SRC-1891 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1542/peds.113.2.376 |  |
| SRC-1892 | RESTRICTED | PMC 刊行版に © The Association of Bone and Joint Surgeons 2008 の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC2690733/ | PMCID候補 PMC2690733（マスター未登録） |
| SRC-1939 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1097/JTN.0000000000000392 |  |
| SRC-1974 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1136/bjsports-2017-098106 |  |
| SRC-1983 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/S1726-4901(10)70088-5 |  |
| SRC-2474 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.20452/pamw.3985 |  |
| SRC-2486 | RESTRICTED | 日本赤十字社の年報。CC 表示なし | https://www.jrc.or.jp/mr/relate/info/pdf/Haemovigilance%20by%20JRCS%202024-2.pdf |  |
| SRC-2488 | RESTRICTED | 一般社団法人日本造血細胞移植データセンター／学会の報告書。CC 表示なし | http://www.jdchct.or.jp/data/report/2025/0.pdf |  |
| SRC-3165 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.14390/jsshp.HRP2018-014 |  |
| SRC-3168 | RESTRICTED | PMC 刊行版に © 2020 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd. の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC8094626/ | PMCID候補 PMC8094626（マスター未登録）。PMID候補 33368142（Europe PMC で確認、マスター未登録） |
| SRC-3171 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS1822679）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC10176440/ | PMCID候補 PMC10176440（マスター未登録）。PMID候補 37164498（Europe PMC で確認、マスター未登録） |
| SRC-3252 | RESTRICTED | PMC 刊行版に © 2025 American Diabetes Association と ADA 独自ライセンス（教育・非商用目的のみ）表示。CC ではない | https://pmc.ncbi.nlm.nih.gov/articles/PMC12690181/ | PMCID候補 PMC12690181（マスター未登録）。PMID候補 41358885（Europe PMC で確認、マスター未登録） |
| SRC-3255 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1177/10507256261445624 | PMID候補 42219800（Europe PMC で確認、マスター未登録） |
| SRC-3256 | RESTRICTED | PMC 刊行版に © 2019 by The American Society of Hematology の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC6880896/ | PMCID候補 PMC6880896（マスター未登録）。PMID候補 31770441（Europe PMC で確認、マスター未登録） |
| SRC-3259 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.ajog.2023.12.023 | PMID候補 38141870（Europe PMC で確認、マスター未登録） |
| SRC-3260 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1016/j.ajog.2021.06.008 | PMID候補 34116035（Europe PMC で確認、マスター未登録） |
| SRC-3365 | OPEN | CC BY 4.0 | https://turkjpediatr.org/about | 誌のサイトはバックファイル（1958年以降の全号）を含む全論文を CC BY 4.0 で公開すると明示し、バックファイルの論文ページにも CC BY の表示がある。本論文（1998年）の個別表示は未確認のため、取り込み時に論文ページで再確認されたい |
| SRC-3432 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1111/ped.13635 | PMID候補 29906300（Europe PMC で確認、マスター未登録） |
| SRC-3433 | RESTRICTED | PMC 刊行版に © 2018 The Cochrane Collaboration. Published by John Wiley &amp; Sons, Ltd. の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC6494160/ | PMCID候補 PMC6494160（マスター未登録）。PMID候補 29551014（Europe PMC で確認、マスター未登録） |
| SRC-3434 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1542/peds.2010-3851 | PMID候補 21357346（Europe PMC で確認、マスター未登録） |
| SRC-3436 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1542/peds.2018-2894 | PMID候補 30455342（Europe PMC で確認、マスター未登録） |
| SRC-3437 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1542/peds.2019-1881 | PMID候補 31285392（Europe PMC で確認、マスター未登録） |
| SRC-3438 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1542/peds.2021-056036 | PMID候補 35190810（Europe PMC で確認、マスター未登録） |
| SRC-3439 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS161274）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC2799187/ | PMCID候補 PMC2799187（マスター未登録）。PMID候補 19816235（Europe PMC で確認、マスター未登録） |
| SRC-3440 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1111/jpc.12698 | PMID候補 25109786（Europe PMC で確認、マスター未登録） |
| SRC-3444 | 確認できず | 誌の現行 OA 方針は CC BY 4.0 とするが、2016年の本論文自体の表示と方針の適用開始時期を確認できない | https://jpma.org.pk/index.php/public_html/Files/ER/OpenAccess |  |
| SRC-3445 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC1702305/ | PMCID候補 PMC1702305（マスター未登録）。PMID候補 5431080（Europe PMC で確認、マスター未登録） |
| SRC-3739 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC6794707/ | PMCID候補 PMC6794707（マスター未登録）。PMID候補 31554544（Europe PMC で確認、マスター未登録） |
| SRC-3745 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1253/circj.CJ-23-0489 | PMID候補 39183026（Europe PMC で確認、マスター未登録） |
| SRC-4377 | RESTRICTED | PMC 刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC3693028/ | PMCID候補 PMC3693028（マスター未登録）。PMID候補 23826541（Europe PMC で確認、マスター未登録）。マスターの DOI（10.3980/j.issn.2222-3959.2013.03.27）は Crossref に登録がなく 404。Europe PMC では PMID 23826541・PMC3693028 と対応 |
| SRC-4383 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1253/circj.CJ-20-0910 | PMID候補 34305070（Europe PMC で確認、マスター未登録） |
| SRC-4398 | RESTRICTED | PMC 刊行版に © 2008 Canadian Medical Association の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC2572665/ | PMCID候補 PMC2572665（マスター未登録）。PMID候補 18981440（Europe PMC で確認、マスター未登録） |
| SRC-4399 | RESTRICTED | Crossref に CC なし・PMC 刊行版なし | https://api.crossref.org/works/10.1007/s10029-025-03561-y | PMID候補 41493600（Europe PMC で確認、マスター未登録） |
| SRC-4624 | RESTRICTED | PMC 収載は著者原稿のみ（NIHMS446406）。刊行版に CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC3596108/ | PMCID候補 PMC3596108（マスター未登録） |
| SRC-4968 | RESTRICTED | PMC 刊行版に ©2012 Baishideng Publishing Group Co., Limited. All rights reserved. の表示。CC 表示なし | https://pmc.ncbi.nlm.nih.gov/articles/PMC3342598/ | PMCID候補 PMC3342598（マスター未登録） |
