# バッチ37：TH（甲状腺・副甲状腺・骨代謝）32件 ― パブリックドメイン出典の裏づけ調査

- 対象：`targets.json` のうち章プレフィックス TH の32件（TH-001・002・004・007〜020・022〜033・035〜037）
- 調査日：2026-11-11
- 判定：**A 置き換え可 1件／B 裏づけ追加 17件／C 見つからない 14件／D 区分の訂正 0件**
- ルール：2026-11-11 の新ルールを適用。抄録・添付文書・医学百科は根拠にせず、政府の全文文書・報告書、CC BY の全文、試験登録レコードなど全文として読める資料のみを候補とした。A は自由な全文で主張全体を置き換えできるものだけ、部分的な裏づけは B。主張文と数値は変更していない。

## 調査方法

- 主出典24件（SRC-660・901・903・904・907〜915・921・922・927・928・932〜935・4971・4979・4980）について、Europe PMC の個別照会でライセンス表示と PMCID を確認し、DOI のある13件は Crossref の version-of-record ライセンスも確認した（一括照会のタイムアウトがあったため、判定に関わるものは curl による個別再照会で確定）。
- 候補の全文確認：NCI PDQ（cancer.gov）と NIH ODS ファクトシートはブラウザで実際に開いて読んだ。CC BY 候補は Europe PMC の全文 XML を取得し、主張の要素ごとに検索して照合した。
- 版の確認：ガイドラインの新版刊行は Web 検索で確認した。

## 特に重要な発見

1. **主出典に CC BY はゼロ件で、区分の訂正（D）はなし。** CC BY-NC-ND は SRC-913（副甲状腺機能低下症の国際診療標準）と SRC-921（原発性副甲状腺機能亢進症 Fifth Workshop）の2件、CC BY-NC-SA は SRC-922（妊娠中の甲状腺機能低下症 ATA 2025 ガイドライン）の1件、CC BY-NC は SRC-928（骨粗鬆症ガイドライン2011年版要約）の1件で、いずれもマスターの RESTRICTED と一致する。その他は Europe PMC・Crossref ともライセンス表示がなく（Elsevier・Springer の TDM 表示のみを含む）、UNKNOWN のままで妥当。関連資料として ETA 2018 バセドウ病ガイドライン（PMC6140607）は Crossref で Karger のサイトライセンスのみで CC ではなく、EUGOGO 2021（SRC-914）は Crossref にライセンス表示自体がなかった。
2. **A は1件（TH-029 腫瘍性骨軟化症）。** 主出典の総説（JCEM 2022、SRC-935）の代わりに、ブロスマブの成人向け総説（TouchREVIEWS in Endocrinology 2026、CC BY）の全文で、FGF23 過剰による病態、血液検査所見、FN1 融合遺伝子が約半数、腫瘍の局在困難、68Ga DOTA イメージング、完全切除が根治的治療であること、切除できない場合の薬物療法まで主張の全要素を確認できた。新規 SRC 候補。
3. **B の主な経路は4つ。** （1）NCI PDQ 甲状腺癌治療サマリー（GOV_US）が TH-012〜016 の5件、（2）副甲状腺疾患の欧州専門家コンセンサス（Eur J Endocrinol 2022、CC BY）が TH-019・020・022・030 の4件、（3）NIH ODS ビタミンDファクトシート（GOV_US）が TH-026・032 の2件、（4）USPSTF 甲状腺機能異常スクリーニング勧告声明（2015、GOV_US）が TH-018・037 の定義部分の2件。そのほか ATA/ETA 甲状腺眼症コンセンサス（CC BY、TH-017）、FHH の大規模コホート研究（Am J Hum Genet 2020、CC BY、TH-031）、バセドウ病の実臨床コホート論文（Endocrine 2017、CC BY、TH-001）、甲状腺炎の分類総説（Virol J 2009、CC BY、TH-009 の分類部分のみ）が各1件。
4. **PMCID の補完候補が6件**（いずれも著者稿等の収載でライセンス表示はなく、区分の変更にはつながらない）：SRC-660 → PMC2413335、SRC-911 → PMC3228182、SRC-912 → PMC4739132、SRC-922 → PMC10515122、SRC-928 → PMC3517709、SRC-932 → PMC4880117。SRC-4979（Chaker 2017）の PMCID PMC6619426 はマスター登録済みと一致し、カード側にあった「API 未照合」の点は解消した。SRC-921 は Europe PMC でも PMCID がなく、カードの null 記録と一致する。
5. **サーベイランス（版の変更）**：
   - 『骨粗鬆症の予防と治療ガイドライン2025年版』（ライフサイエンス出版、2025年8月、ISBN 978-4-89775-502-1）が刊行された。2015年版以来10年ぶりの全面改訂で、TH-023（2012年の診断基準）・TH-024・TH-025（2011年版ガイドライン要約準拠）は照合直しの対象。
   - ATA 成人分化型甲状腺癌ガイドライン2025年版（Thyroid. 2025;35(8):841-985、DOI 10.1177/10507256251363120）が刊行され、TH-013・TH-014（ATA 2015 準拠）の照合直し対象。TH-010・TH-011 の結節評価が2025年版の範囲に含まれるかは本文の確認が必要。
   - ATA 妊娠期甲状腺ガイドライン2026年版（Thyroid. 2026;36(5):481-544）も刊行されている（TH の対象カードには直接対応しないが、SRC-922 周辺の申し送りとして記録）。
6. **主張チェック（数値の枠組みの相違、両値を記録）**：
   - TH-032：ビタミンD毒性の目安について、カード（国際コンセンサス）は >250 nmol/L を定義とするのに対し、NIH ODS は「典型的には >375 nmol/L（150 ng/mL）」と記載する。閾値の枠組みが異なる。
   - TH-030：重症低カルシウム血症の緊急対応の閾値について、カード（BMJ 2022）は <1.9 mmol/L、副甲状腺コンセンサス（CC BY）は <1.8 mmol/L で緊急治療（グルコン酸カルシウム静注＋心電図モニタリング）とする。
   - TH-027：日本の判定指針（欠乏 <20 ng/mL、不足 20〜30 ng/mL）と NIH ODS／FNB の区分（欠乏リスク <12 ng/mL、不足 12〜20 ng/mL、充足 ≧20 ng/mL）は枠組みが異なり、候補として使えなかった（判定は C）。
7. **薬剤の申し送り**：TH-017 のミコフェノール酸（甲状腺眼症に対する国内承認）は候補資料では確認できず、登録時の確認事項のまま（カードの uncertainty に既記）。TH-029 のブロスマブについても、国内承認範囲は PMDA の全文文書での確認を登録時の宿題とする（候補の総説は欧州承認に触れるのみ）。

## 明細

| 対象 | 判定 | 現行出典（SRC） | 候補 | 区分 | PMID | DOI | PMCID | ライセンス根拠URL | 裏づけ範囲 | 数値照合 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TH-001 | B | ATA 甲状腺機能亢進症ガイドライン2016（SRC-901） | Hussain YS et al. Epidemiology, management and outcomes of Graves' disease-real life data. Endocrine. 2017 | OPEN | 28478488 | 10.1007/s12020-017-1306-5 | PMC5435772 | https://europepmc.org/article/MED/28478488 | TRAb が病態の駆動力であること、甲状腺中毒症の臨床・生化学所見に TRAb 上昇・眼症・びまん性取り込み増加が加わればバセドウ病の診断が確定すること | 数値なし（該当なし） | カードの「びまん性甲状腺腫」は候補では「びまん性取り込み増加」として記載され完全一致ではないため B。ETA 2018 ガイドライン（PMC6140607）は Karger のサイトライセンスのみで CC ではないため不採用 |
| TH-002 | C | バセドウ病診療の実態調査（SRC-904、Endocr J 2023） | なし | — | — | — | — | — | — | — | 主出典は ©日本内分泌学会でライセンス表示なし。全国調査固有の数値（TSH受容体抗体陽性率、心房細動の合併）を置き換える自由な全文は見つからない |
| TH-004 | C | 甲状腺クリーゼ診療ガイドライン2016 の刊行紹介（SRC-903、Endocr J 2016） | なし | — | — | — | — | — | — | — | Burch–Wartofsky スコアと JTA カテゴリー、死亡率10〜30%を再掲する CC BY・政府全文は見つからない。主出典はライセンス表示なし |
| TH-007 | C | Winters SJ et al. 橋本病総説（SRC-907、Lancet 系総説） | なし | — | — | — | — | — | — | — | 候補として全文確認した CC BY 総説（Front Immunol 2021、PMC8049926）は病態のみで「最も多い自己免疫性甲状腺疾患・ヨウ素充足地域での主因」「レボチロキシン治療」の記載がなく、別総説（PMC4426893）も抗体所見のみで不十分 |
| TH-008 | C | 亜急性甲状腺炎のコホート（SRC-908、Mayo Clin Proc 2000） | なし | — | — | — | — | — | — | — | CC BY の亜急性甲状腺炎総説（J Clin Med 2021、PMC8096888）の全文を確認したが、Olmsted の数値（年4.9/10万人、疼痛96%、永続性低下症15%）は含まれていなかった。コホート固有の数値は抄録以外に自由な裏づけがない |
| TH-009 | B | 甲状腺炎の診断と治療のガイドライン（SRC-909、Endocr J 2003） | Desailloud R, Hober D. Viruses and thyroiditis: an update. Virol J. 2009 | OPEN | 19138419 | 10.1186/1743-422X-6-5 | PMC2654877 | https://europepmc.org/article/MED/19138419 | 無痛性（silent）甲状腺炎が慢性橋本病の亜型（variant form）として自己免疫性甲状腺疾患に分類されること | 数値なし（該当なし） | 三相性の経過（中毒症期→機能低下期→回復）の記述は候補になく、その部分は裏づけられないため B |
| TH-010 | C | ATA 甲状腺結節・分化癌ガイドライン2015（SRC-910） | なし | — | — | — | — | — | — | — | 甲状腺腫・結節の評価手順と分類を再掲する自由な全文は見つからない（PDQ は癌の範囲）。ATA 2025年版の結節評価範囲は本文未確認 |
| TH-011 | C | ATA 甲状腺結節・分化癌ガイドライン2015（SRC-910） | なし | — | — | — | — | — | — | — | 超音波所見別の FNA 適応と細胞診分類は ATA 2015 固有の内容で、自由な全文の候補は見つからない |
| TH-012 | B | ESMO 甲状腺癌ガイドライン2019（SRC-911） | NCI PDQ Thyroid Cancer Treatment (Health Professional Version) | GOV_US | — | — | — | https://www.cancer.gov/types/thyroid/hp/thyroid-treatment-pdq | 濾胞腺腫と濾胞癌は被膜浸潤（および血管浸潤）の有無で鑑別されるという中核部分 | 数値なし（該当なし） | 「境界型」腫瘍の区分や免疫染色の位置づけは PDQ の範囲外のため B。主出典 SRC-911 に PMCID PMC3228182 の補完候補あり |
| TH-013 | B | ATA 甲状腺結節・分化癌ガイドライン2015（SRC-912） | NCI PDQ Thyroid Cancer Treatment (Health Professional Version) | GOV_US | — | — | — | https://www.cancer.gov/types/thyroid/hp/thyroid-treatment-pdq | 診断評価として頸部超音波検査と穿刺吸引細胞診が位置づけられること | 数値なし（該当なし） | 分子マーカーの位置づけと超音波パターン別の FNA 閾値は PDQ の範囲外のため B。ATA 2025年版が刊行され照合直しの対象（サーベイランス参照）。主出典 SRC-912 に PMCID PMC4739132 の補完候補あり |
| TH-014 | B | ATA 甲状腺結節・分化癌ガイドライン2015（SRC-912） | NCI PDQ Thyroid Cancer Treatment (Health Professional Version) | GOV_US | — | — | — | https://www.cancer.gov/types/thyroid/hp/thyroid-treatment-pdq | 甲状腺全摘後のサイロキシンによる TSH 抑制（程度は再発リスクに依存すること）と、サイログロブリン値の上昇が再発と強く相関すること | 数値なし（該当なし） | リスク別の TSH 目標値や放射性ヨウ素の適応区分の詳細は PDQ の範囲外のため B。ATA 2025年版での照合直し対象 |
| TH-015 | B | ESMO 甲状腺癌ガイドライン2019（SRC-911） | NCI PDQ Thyroid Cancer Treatment (Health Professional Version) | GOV_US | — | — | — | https://www.cancer.gov/types/thyroid/hp/thyroid-treatment-pdq | 濾胞癌は血管に浸潤しやすく、リンパ行性よりも血行性に肺・骨へ転移すること | 遠隔転移率 <10% と組織型別10年生存率（98%・80%）は PDQ に記載がなく照合できていない | 数値部分が候補にないため B |
| TH-016 | B | ESMO 甲状腺癌ガイドライン2019（SRC-911） | NCI PDQ Thyroid Cancer Treatment (Health Professional Version) | GOV_US | — | — | — | https://www.cancer.gov/types/thyroid/hp/thyroid-treatment-pdq | 4つの主要組織型の分類、髄様癌が傍濾胞細胞（C細胞）由来でカルシトニンが腫瘍マーカーとなること、未分化癌が侵襲性で予後不良であること | 数値なし（該当なし） | ESMO の3区分（分化型・髄様・未分化）の厳密な再掲ではないため B |
| TH-017 | B | EUGOGO 甲状腺眼症ガイドライン2021（SRC-914） | Burch HB et al. Management of Thyroid Eye Disease: A Consensus Statement by the ATA and the ETA. Thyroid. 2022 | OPEN | 36480280 | 10.1089/thy.2022.0251 | PMC9807259 | https://europepmc.org/article/MED/36480280 | 静注グルココルチコイドが活動性中等症〜重症の優先治療であること、IVMP の標準 regimen（累積4.5 g：0.5 g/週×6週＋0.25 g/週×6週）、EUGOGO 2021 が IVMP＋ミコフェノール酸を第一選択として推奨したことがコンセンサス本文に記録されていること | 累積 4.5 g の regimen はカードと一致 | EUGOGO 推奨の再掲はコンセンサス側の留保つき引用で、候補自体の一律の第一選択化ではないため B。ミコフェノール酸の国内承認は候補で確認できず登録時の確認事項（カードの uncertainty に既記） |
| TH-018 | B | ETA 潜在性甲状腺機能亢進症ガイドライン2017（SRC-915） | USPSTF Final Recommendation Statement: Thyroid Dysfunction: Screening (2015) | GOV_US | — | — | — | https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/thyroid-dysfunction-screening | 定義（TSH が基準下限未満で FT4・FT3 が正常）という部分 | 数値なし（該当なし） | 軽症/重症の層別、年齢別の原因、顕性化のリスク因子は候補の範囲外のため B（定義のみ） |
| TH-019 | B | 原発性副甲状腺機能亢進症 Fifth Workshop 2022（SRC-921） | Bollerslev J et al. European Expert Consensus on Practical Management of Specific Aspects of Parathyroid Disorders in Adults and in Pregnancy. Eur J Endocrinol. 2022 | OPEN | 34863037 | 10.1530/EJE-21-1044 | PMC8789028 | https://europepmc.org/article/MED/34863037 | 正カルシウム性 PHPT の定義と二次性の原因除外を要すること、診断の確認にアルブミン補正カルシウムと PTH の再測定を用いること | 数値なし（該当なし） | 「2回・約2週間間隔」「3〜6か月」の具体的な測定スケジュールは候補になく、その部分は裏づけられないため B。主出典は CC BY-NC-ND で RESTRICTED が正しい（D なし） |
| TH-020 | B | 原発性副甲状腺機能亢進症 Fifth Workshop 2022（SRC-921） | Bollerslev J et al. （TH-019 と同一のコンセンサス） | OPEN | 34863037 | 10.1530/EJE-21-1044 | PMC8789028 | https://europepmc.org/article/MED/34863037 | 非手術例でのシナカルセトと骨保護薬による保存的管理、副甲状腺摘出が根治的治療であること | 尿中カルシウムの参照値（女 >250 mg/日・男 >300 mg/日）は候補の高カルシウム尿症の定義として一致 | 手術適応の数値リスト（血清 Ca 上限+1 mg/dL、Tスコア −2.5、eGFR 60 未満、50歳未満、椎体骨折）は候補に再掲がなく、その部分は裏づけられないため B |
| TH-022 | B | 原発性副甲状腺機能亢進症 Fifth Workshop 2022（SRC-921） | Bollerslev J et al. （TH-019 と同一のコンセンサス） | OPEN | 34863037 | 10.1530/EJE-21-1044 | PMC8789028 | https://europepmc.org/article/MED/34863037 | intact PTH による PTH 依存性の切り分け（PHPT の確認手順）と、家族性低カルシウム尿性高カルシウム血症との鑑別が候補の主題であること | 数値なし（該当なし） | 悪性腫瘍（PTHrP）・肉芽腫性疾患など PTH 非依存性の側は候補の範囲外のため B |
| TH-023 | C | 原発性骨粗鬆症の診断基準2012年度改訂版（SRC-927） | なし | — | — | — | — | — | — | — | 日本の診断基準（脆弱性骨折の有無と骨密度 YAM 80%・70%）を全文で読める政府文書・CC BY 資料は見つからない。『骨粗鬆症の予防と治療ガイドライン2025年版』刊行により照合直しの対象（サーベイランス参照） |
| TH-024 | C | 骨粗鬆症の予防と治療ガイドライン2011年版の要約（SRC-928） | なし | — | — | — | — | — | — | — | FRAX の介入閾値（10年間の骨折確率15%・腸骨骨折3%）は日本のガイドライン固有で、自由な全文の候補は見つからない。主出典は CC BY-NC で RESTRICTED が正しい（D なし）。PMCID PMC3517709 の補完候補あり。2025年版での照合直し対象 |
| TH-025 | C | 骨粗鬆症の予防と治療ガイドライン2011年版の要約（SRC-928） | なし | — | — | — | — | — | — | — | ステロイド性骨粗鬆症の頻度（長期使用者の約50%）と薬物治療の開始基準を再掲する CC BY・政府全文は見つからない（ACR 2022 ガイドラインは CC ではない）。2025年版での照合直し対象 |
| TH-026 | B | くる病・骨軟化症の診断指針（SRC-932、日本内分泌学会・日本小児内分泌学会） | NIH Office of Dietary Supplements. Vitamin D Fact Sheet for Health Professionals | GOV_US | — | — | — | https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/ | 乳児のビタミンD必要量 400 IU/日（0〜12か月の Adequate Intake）がカードのくる病予防投与量と一致すること | 400 IU/日は一致 | 治療用量（天然型ビタミンD 2000 IU/日・カルシウム 500 mg/日）と、くる病の定義・診断手順は ODS の範囲外のため B。主出典 SRC-932 に PMCID PMC4880117 の補完候補あり |
| TH-027 | C | ビタミンD不足・欠乏の判定指針（SRC-933、日本内分泌学会・日本骨代謝学会） | なし | — | — | — | — | — | — | 日本の判定区分（欠乏 <20 ng/mL、不足 20〜30 ng/mL）は NIH ODS／FNB の区分（欠乏リスク <12、不足 12〜20、充足 ≧20 ng/mL）と枠組みが異なり裏づけに使えない。日本の指針自体の自由な全文も見つからない | 両枠組みの数値を備考に記録（左記のとおり） |
| TH-028 | C | 悪性腫瘍に伴う高カルシウム血症の Endocrine Society ガイドライン2022（SRC-934） | なし | — | — | — | — | — | — | — | 治療ラダー（補液・カルシトニン・骨吸収抑制薬の順序と重症度別の位置づけ）を再掲する CC BY・政府全文は見つからない（検索で得られたのは症例報告のみ）。主出典は Europe PMC でライセンス表示なし |
| TH-029 | A | 腫瘍性骨軟化症の総説（SRC-935、JCEM 2022） | Black S, Keen R, Bubbear J. Burosumab for X-linked Hypophosphataemia and Tumour-induced Osteomalacia in Adults. TouchREVIEWS in Endocrinology. 2026 | OPEN | 42273000 | 10.17925/EE.2026.22.1.6 | PMC13249216 | https://europepmc.org/article/MED/42273000 | 主張全体：FGF23 過剰分泌による腎性リン排泄・低リン血症性骨軟化症という病態、血液検査所見（低リン、FGF23 高値または不適切正常、1,25(OH)2D 低値〜低正常）、FN1-FGFR1／FN1-FGF1 融合遺伝子が間葉系腫瘍の約半数、腫瘍は小さく緩徐で局在が難しいこと、68Ga DOTA イメージングの感度、完全切除が根治的治療であること、同定・切除できない場合のブロスマブを含む薬物療法 | FN1 融合「約半数」は候補の "approximately half" と一致。候補は「35〜40%の腫瘍は局在できない」とも記載（カードに該当数値なし、矛盾なし） | 新規 SRC 候補。ブロスマブの国内承認範囲は PMDA の全文文書での確認を登録時の宿題とする（カードの uncertainty に既記） |
| TH-030 | B | 低カルシウム血症の総説（SRC-660、BMJ 2018） | Bollerslev J et al. （TH-019 と同一のコンセンサス） | OPEN | 34863037 | 10.1530/EJE-21-1044 | PMC8789028 | https://europepmc.org/article/MED/34863037 | PTH 分泌不全型ではカルシトリオール／アルファカルシジオールが標準治療であること、急性の症候性低カルシウム血症ではグルコン酸カルシウム静注と心電図モニタリングを要すること、術後低カルシウム血症への経口カルシウム＋活性型ビタミンD | 主張チェック：緊急対応の閾値はカード <1.9 mmol/L に対し候補は <1.8 mmol/L（両値を記録） | 中核であるアルブミン補正式（係数 0.02）と原因の頻度順位は候補になく、その部分は裏づけられないため B。主出典 SRC-660 に PMCID PMC2413335 の補完候補あり |
| TH-031 | B | 妊娠中の甲状腺機能低下症 ATA ガイドライン2025（SRC-922、FHH の鑑別記述の出典） | Dershem R et al. Familial Hypocalciuric Hypercalcemia Type 1 and Autosomal-Dominant Hypocalcemia Type 1. Am J Hum Genet. 2020 | OPEN | 32386559 | 10.1016/j.ajhg.2020.04.006 | PMC7273533 | https://europepmc.org/article/MED/32386559 | カルシウム・クレアチニンクリアランス比 <0.01 が FHH の約80%・原発性副甲状腺機能亢進症の20%未満という切り分け、鑑別が不要な副甲状腺手術の回避につながること、FHH には介入が不要であること | CCCR <0.01 の分布（約80% vs 20%未満）はカードと一致 | カードの「PHPT では比 >0.02 が多い」は候補にその形の記載がないため B。主出典 SRC-922 は CC BY-NC-SA で RESTRICTED が正しく（D なし）、PMCID PMC10515122 の補完候補あり |
| TH-032 | B | くる病・骨軟化症の診断指針（SRC-932） | NIH Office of Dietary Supplements. Vitamin D Fact Sheet for Health Professionals | GOV_US | — | — | — | https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/ | FNB の区分（≧50 nmol/L で充足、30〜50 で不足の可能性、<30 で欠乏リスク）がカードのコンセンサス分類と実質的に一致すること | 主張チェック：毒性の目安はカード >250 nmol/L（コンセンサス定義）に対し ODS は「典型的には >375 nmol/L（150 ng/mL）」と記載し、枠組みが異なる（両値を記録） | 治療と経過観察の部分は候補の範囲外のため B |
| TH-033 | C | 橋本病の総説（SRC-4971、Endocr Pract 2014） | なし | — | — | — | — | — | — | — | 診断の構成（抗TPO抗体・抗Tg抗体と超音波の低エコー所見の組み合わせ）を再掲する自由な全文は見つからない。確認した CC BY 総説（PMC8049926・PMC4426893）は病態と抗体所見のみで、超音波所見と診断の組み立ては含まれなかった |
| TH-035 | C | 甲状腺機能低下症の総説（SRC-4979、Chaker 2017、Lancet Diabetes Endocrinol） | なし | — | — | — | — | — | — | — | 代表症状のリストを再掲する自由な全文は見つからない（USPSTF のエビデンスレビューにも症状リストはない）。主出典の PMCID PMC6619426 はマスター登録済みと一致 |
| TH-036 | C | Colorado 甲状腺疾患有病率調査（SRC-4980、Canaris 2000） | なし | — | — | — | — | — | — | — | コホート固有の結果。カードの uncertainty が裏づけ候補として挙げる Carlé 2014（Eur J Endocrinol、PMID 25305308、DOI 10.1530/EJE-14-0481）は Europe PMC でライセンス表示がなく自由に使えないため、候補化できない |
| TH-037 | B | 甲状腺機能低下症の総説（SRC-4979、Chaker 2017） | USPSTF Final Recommendation Statement: Thyroid Dysfunction: Screening (2015) | GOV_US | — | — | — | https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/thyroid-dysfunction-screening | 顕性（TSH 高値＋FT4 低値）と潜在性（TSH 高値＋FT4 正常）の生化学的定義、甲状腺機能低下症の治療がレボチロキシン（経口 T4）単剤であること | 数値なし（該当なし） | TSH 目標の年齢別の目安（若年は下半分、高齢は上半分）は候補の範囲外のため B |

## 補足

- 試験が主出典のカードは TH にはなかったため、ClinicalTrials.gov の経路は今回使っていない。
- 主出典24件の DOI・PMID はすべて Europe PMC の個別レコードと一致し、誤りは見つからなかった。同一文献の二重登録も TH の範囲では見つからなかった。
- 本バッチの候補で新規 SRC として登録が考えられるのは TH-029 の1件（ブロスマブ総説）。その他の B 候補は、既存の裏づけ（corroboration）としての追加を想定する。
