# 特別回 神経消化器病（腸脳相関病・機能性消化管疾患）（NG-001〜NG-240）

- 作成日：2026-10-17
- 更新日：2026-10-18（Rome V 対応：NG-110〜125 を追加、第9節）
- 更新日：2026-10-18（原本による照合：Rome V の6章で NG-126〜177、便通異常症 GL 2023 慢性下痢症で NG-178〜185 を追加。NG-099〜108 を刊行版で照合）
- 更新日：2026-10-18（原本の追加3章：食道で NG-186〜196、胃十二指腸で NG-197〜210、基礎科学で NG-211〜215 を追加）
- 更新日：2026-10-18（小児下部消化管・胆道の章で NG-216〜231 を追加。いただいた3論点のまとめを照合、第9-5節）
- 更新日：2026-10-18（序論の章で NG-232〜240 を追加。臨床用基準の8週間を確認し、第9-5節を訂正）
- 目的：日本神経消化器病学会の広報で使う事実の土台。学会が対象とする領域を広めに見積もり、既存の事実票（ES・GD・IN）との重なりを整理したうえで、足りない命題を新しく作った。
- 事実票：240件（NG-001〜NG-240、欠番なし）。全件 `status: draft`、`verifier: null`
- 取り込み時の注意：YAMLブロックは1つだけで、アンカー・マージキー・脚注番号は使っていません。
- **新しい接頭辞 NG を使っています。** 現行の `fact.schema.json` は id と domain の接頭辞を列挙しているため、そのままでは検証を通りません。取り込みの前に、Claude Code で次の2か所に `NG` を追加してください（CLAUDE.md 第4節の表にも「NG：神経消化器病（腸脳相関病・機能性消化管疾患）、特別回」を追記）。
  - `properties.id.pattern`：`^(HP|UG|ES|GD|IN|LV|BP|AB|XS|NG)-[0-9]{3}$`
  - `properties.domain.enum`：`"NG"` を追加
  - このファイルの YAML は、上の2か所を変えたスキーマで検証済みです。

## 1. 対象範囲の定義（2026-10-17 に先生の整理した9区分で確定）

対象範囲は、先生が整理した9区分（疾患、病態生理、症状、検査、画像、分子・遺伝、診断基準・分類モデル、治療、関連診療科）で確定しました。初版で見積もった3層（中核・運動障害・基盤）は、この9区分に含まれます。下の表の記号の意味は次のとおりです。

- ◎：事実票あり（ID を記載）
- ○：一部あり
- ×：未作成。第6節の補完候補

| 区分 | 要素 | 状況と ID |
|---|---|---|
| 1 疾患・食道 | 機能性胸やけ、逆流過敏症、機能性胸痛、食道球、機能性嚥下障害 | ◎ NG-058〜063、NG-186〜196（Rome V） |
| | アカラシア、DES、ジャックハンマー食道、EGJOO | ◎ ES-025〜ES-033（Chicago v4.0、POEM） |
| 1 疾患・胃十二指腸 | 機能性ディスペプシア（PDS/EPS）、H. pylori 関連ディスペプシア | ◎ GD-001〜GD-018、NG-039〜041、NG-064、NG-197〜204（Rome V） |
| | げっぷ障害、反芻症候群、げっぷができない症候群 | ◎ NG-048〜051、NG-068、NG-208〜210 |
| | 悪心・嘔吐障害、周期性嘔吐症候群、カンナビノイド悪阻症候群 | ◎ NG-016〜018、NG-065〜067、NG-205〜207 |
| | 胃不全麻痺 | ◎ NG-011〜015、GD-007 |
| 1 疾患・小腸大腸 | IBS（病型、感染後IBS） | ◎ IN-017〜026、NG-031〜033、NG-042〜044、NG-070、NG-086〜098、NG-127〜138 |
| | 機能性便秘症（Rome V では慢性便秘症） | ◎ IN-027〜035、NG-044・045、NG-099〜108、NG-139〜142 |
| | 機能性下痢症、機能性腹部膨満症、スペクトラムの考え方 | ◎ NG-069・071・072、NG-126、NG-143〜147 |
| | 慢性下痢症（日本の便通異常症 GL） | ◎ NG-178〜185 |
| | CIPO | ◎ NG-022〜026 |
| | オピオイド誘発性便秘、麻薬性腸症候群 | ◎ NG-046、NG-073、NG-075、NG-105、NG-148、NG-156・157 |
| 1 疾患・直腸肛門 | 便失禁 | ◎ NG-019〜021、NG-159・160 |
| | 機能性直腸肛門痛、機能性排便障害（排便協調障害） | ◎ NG-077〜079、NG-106、NG-158、NG-161〜163 |
| | 直腸感覚低下・過敏（Rome V で新設） | ◎ NG-164・165 |
| 1 疾患・中枢性 | 中枢介在性腹痛症候群 | ◎ NG-074・076、NG-149〜153 |
| | 成人の腹部片頭痛（Rome V で新設） | ◎ NG-154・155 |
| 1 疾患・小児 | 乳児逆流症、乳児疝痛（Rome V では乳児苦痛症候群）、乳幼児・小児の機能性便秘、腹部片頭痛、機能性腹痛症 | ◎ NG-080〜085、NG-117〜122、NG-174〜177、NG-216〜231 |
| 1 関連 | ヒルシュスプルング病、ダンピング症候群 | ◎ NG-027〜030、GD-074〜079 |
| 2 病態生理 | 運動異常、内臓知覚過敏、過覚醒 | ◎ NG-001、NG-058 |
| | 中枢応答異常（脳機能画像） | ◎ NG-088 |
| | 粘膜微小炎症・透過性亢進、腸内細菌 | ◎ NG-087、NG-108 |
| | SIBO | ○ NG-031、NG-097（抗菌薬の機序として） |
| | ストレス・HPA軸（CRH、オキシトシン）、心理社会的因子、遺伝 | ◎ NG-086、NG-089、NG-108 |
| 3 症状 | 上部・下部・直腸肛門の各症状 | ◎ 疾患カードの定義の中で網羅（NG-058〜085）。警告症状は NG-101 |
| 4 検査 | HRM、HRIM、MII-pH | ◎ ES（Chicago、Lyon 2.0）、NG-048・050、NG-192（Rome V の判定値） |
| | EndoFLIP | ◎ NG-109 |
| | 胃排出検査 | ◎ NG-013 |
| | 大腸通過時間（X線不透過マーカー）、体外式超音波、MRI/CT、排便造影 | ◎ NG-102 |
| | 直腸肛門内圧、直腸感覚検査、バルーン排出検査 | ◎ NG-052・053、NG-078、NG-161、NG-164・165 |
| | 胃バロスタット、飲水負荷試験、TCM（粘膜透過性）、肛門筋電図 | × |
| 5 画像 | シネMRI | ○ CIPO の診断基準内（NG-024） |
| | 脳機能イメージング | ◎ NG-088 |
| | TBE | × |
| 6 分子・遺伝 | 5-HT3、5-HT4、GC-C、IBAT、μオピオイド、ACh | ◎ NG-039〜046、NG-092 |
| | CRH、オキシトシン | ◎ NG-086 |
| | 腸管神経系、カハール介在細胞、迷走・脊髄求心路、セロトニン、肥満細胞、腸内細菌 | ◎ NG-211〜215 |
| | 脳腸ペプチド（モチリン、グレリンなど）、タイトジャンクション蛋白、遺伝子多型（GNB3 など） | × |
| 7 モデル | 生物心理社会モデル、腸脳相関、Rome IV、MDCP、Chicago 分類 | ◎ NG-001〜003、NG-037・038、ES-025〜031 |
| | Rome V（分類、研究用・臨床用基準、診断質問票、FICAI） | ◎ NG-110〜125、NG-126、NG-170〜176 |
| 8 治療・薬物 | 酸分泌抑制薬 | ◎ ES（GERD） |
| | 運動機能改善薬、便秘薬、下痢薬 | ◎ NG-039〜046、NG-091・092、NG-103 |
| | 漢方薬 | ◎ NG-096、NG-104、GD（六君子湯） |
| | 神経調節薬（TCA、SSRI、SNRI、抗不安薬） | ◎ NG-059・060・061、NG-076、NG-093、NG-136、NG-153、NG-168・169 |
| | プロバイオティクス、リファキシミン | ◎ NG-034〜036、NG-047、NG-090、NG-097 |
| 8 治療・食事心理 | 低FODMAP食、食事・生活指導 | ◎ IN-023、NG-032 |
| | CBT、催眠療法、マインドフルネス、リラクセーション、バイオフィードバック | ◎ NG-032、NG-049・051、NG-076、NG-079、NG-094、NG-106、NG-138、NG-162〜164、NG-166・167 |
| | 自律訓練法、EMDR | × |
| 8 治療・高度 | POEM | ◎ ES-032・033 |
| | 仙骨神経刺激療法、結腸切除、順行性洗腸 | ◎ NG-021、NG-106 |
| | FMT | ◎ NG-054・055、NG-098 |
| | G-POEM、PEG-J | × |
| 9 診療科 | 脳神経内科（パーキンソン病） | ◎ NG-056・057、NG-098 |
| | 心療内科・精神科（心理療法の担い手） | ◎ NG-094、NG-166・167（Rome V の統合ケア3段階）。学会としての連携体制は × |
| | 小児科（乳幼児・小児の機能性消化管疾患） | ◎ NG-080〜085、NG-216〜231 |
| | 移行期医療、多職種チーム | × |

## 2. 件数のまとめ

| 区分 | 件数 |
|---|---|
| 既存カードの再利用（ES・GD・IN） | 約76件 |
| 新規（このファイル、NG-001〜NG-240） | 240件 |
| 合計 | 約316件 |

既存カードは NG に複製しません。ID の不変と重複回避の原則（CLAUDE.md 第1節）を守るためです。代わりに、横断的に引けるタグ（例：`scope_tags: [NG]`）を付けることを提案します。

## 3. 出典マスター（新規 SRC-100〜153）

| SRC | 出典 | DOI | ライセンス表示 | source_class | 使用カード数 |
|---|---|---|---|---|---|
| SRC-100 | Drossman DA, Hasler WL. Rome IV—Functional GI Disorders: Disorders of Gut-Brain Interaction. Gastroenterology 2016;150:1257-1261 | 10.1053/j.gastro.2016.03.035 | © 2016 AGA Institute（非CC） | RESTRICTED | 3 |
| SRC-101 | 日本神経消化器病学会ウェブサイト『沿革』 | — | 学会ウェブサイト（利用規約は未確認） | UNKNOWN | 2 |
| SRC-102 | Sperber AD, et al. Worldwide Prevalence and Burden of Functional Gastrointestinal Disorders, Results of Rome Foundation Global Study. Gastroenterology 2021;160:99-114 | 10.1053/j.gastro.2020.04.014 | CC BY-NC-ND（論文中の表示） | RESTRICTED | 5 |
| SRC-103 | NIDDK. Definition & Facts for Gastroparesis（最終レビュー 2018年1月） | — | 米国連邦政府著作物（NIDDK。第三者素材を除く） | GOV_US | 2 |
| SRC-104 | NIDDK. Diagnosis of Gastroparesis（最終レビュー 2018年1月） | — | 米国連邦政府著作物（NIDDK。第三者素材を除く） | GOV_US | 1 |
| SRC-105 | NIDDK. Treatment for Gastroparesis（最終レビュー 2018年1月） | — | 米国連邦政府著作物（NIDDK。第三者素材を除く） | GOV_US | 2 |
| SRC-106 | NIDDK. Definition & Facts for Cyclic Vomiting Syndrome（最終レビュー 2017年12月） | — | 米国連邦政府著作物（NIDDK。第三者素材を除く） | GOV_US | 2 |
| SRC-107 | NIDDK. Treatment for Cyclic Vomiting Syndrome（最終レビュー 2017年12月） | — | 米国連邦政府著作物（NIDDK。第三者素材を除く） | GOV_US | 1 |
| SRC-108 | NIDDK. Definition & Facts for Bowel Control Problems (Fecal Incontinence)（最終レビュー 2017年7月） | — | 米国連邦政府著作物（NIDDK。第三者素材を除く） | GOV_US | 2 |
| SRC-109 | NIDDK. Treatment for Bowel Control Problems (Fecal Incontinence)（最終レビュー 2017年7月） | — | 米国連邦政府著作物（NIDDK。第三者素材を除く） | GOV_US | 1 |
| SRC-110 | 厚生労働省 指定難病99『慢性特発性偽性腸閉塞症』概要・診断基準等 | — | 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認） | GOV_JP | 5 |
| SRC-111 | 厚生労働省 指定難病291『ヒルシュスプルング病（全結腸型又は小腸型）』概要・診断基準等 | — | 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認） | GOV_JP | 4 |
| SRC-112 | NIDDK. Symptoms & Causes of Irritable Bowel Syndrome（最終レビュー 2017年11月） | — | 米国連邦政府著作物（NIDDK。第三者素材を除く） | GOV_US | 1 |
| SRC-113 | NIDDK. Treatment for Irritable Bowel Syndrome（最終レビュー 2017年11月） | — | 米国連邦政府著作物（NIDDK。第三者素材を除く） | GOV_US | 2 |
| SRC-114 | NCCIH. Probiotics: Usefulness and Safety（最終更新 2019年8月） | — | 米国連邦政府著作物（NCCIH。第三者素材を除く） | GOV_US | 3 |
| SRC-115 | アコファイド錠100mg（アコチアミド塩酸塩水和物）添付文書 2023年8月改訂（第3版）、ゼリア新薬工業 | — | 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用） | UNKNOWN | 3 |
| SRC-116 | イリボー錠2.5μg・5μg（ラモセトロン塩酸塩）添付文書 2021年3月改訂（第2版）、アステラス製薬 | — | 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用） | UNKNOWN | 2 |
| SRC-117 | リンゼス錠0.25mg（リナクロチド）添付文書 2026年8月改訂（第3版）、アステラス製薬 | — | 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用） | UNKNOWN | 1 |
| SRC-118 | グーフィス錠5mg（エロビキシバット水和物）添付文書 2022年4月改訂（第2版）、EAファーマ | — | 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用） | UNKNOWN | 1 |
| SRC-119 | スインプロイク錠0.2mg（ナルデメジントシル酸塩）添付文書 2026年9月改訂（第3版）、塩野義製薬 | — | 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用） | UNKNOWN | 1 |
| SRC-120 | リフキシマ錠200mg（リファキシミン）添付文書 2024年3月改訂（第3版）、あすか製薬 | — | 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用） | UNKNOWN | 1 |
| SRC-121 | Carrington EV, et al. The international anorectal physiology working group (IAPWG) recommendations: Standardized testing protocol and the London classification for disorders of anorectal function. Neurogastroenterol Motil 2020;32:e13679 | 10.1111/nmo.13679 | CC BY 4.0（論文中の表示） | OPEN | 2 |
| SRC-122 | Sawada A, Fujiwara Y. Belching Disorders and Rumination Syndrome: A Literature Review. Digestion 2024;105:18-25 | 10.1159/000534092 | © 2023 S. Karger AG, All rights reserved | RESTRICTED | 4 |
| SRC-123 | FDA. Fecal Microbiota for Transplantation: Safety Communication – Risk of Serious Adverse Reactions Due to Transmission of Multi-Drug Resistant Organisms（2019-06-13、06-18更新） | — | 米国連邦政府著作物（第三者素材を除く） | GOV_US | 2 |
| SRC-124 | Frazzitta G, et al. Severe Constipation in Parkinson's Disease and in Parkinsonisms: Prevalence and Affecting Factors. Front Neurol 2019;10:621 | 10.3389/fneur.2019.00621 | CC BY（記事ページの表示） | OPEN | 2 |
| SRC-125 | Iyengar P, Chang L. The multidimensional clinical profile for disorders of gut-brain interaction. 2024（Permanyer、ISSN 2462-7011） | 10.24875/NGL.23000008 | 未確認（DOAJ収載のOA誌。抄録のみ参照） | UNKNOWN | 1 |
| SRC-126 | Rome Foundation『Special issue of Gastroenterology, May 2016』（Rome IV 特集号の章構成） | — | Rome Foundation ウェブサイト（利用規約は未確認） | UNKNOWN | 1 |
| SRC-127 | Aziz Q, et al. Functional Esophageal Disorders. Gastroenterology 2016;150:1368-1379 | 10.1053/j.gastro.2016.02.012 | © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用） | RESTRICTED | 6 |
| SRC-128 | Stanghellini V, et al. Gastroduodenal Disorders. Gastroenterology 2016;150:1380-1392 | 10.1053/j.gastro.2016.02.011 | © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用） | RESTRICTED | 5 |
| SRC-129 | Lacy BE, et al. Bowel Disorders. Gastroenterology 2016;150:1393-1407 | 10.1053/j.gastro.2016.02.031 | © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用） | RESTRICTED | 5 |
| SRC-130 | Keefer L, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2016;150:1408-1419 | 10.1053/j.gastro.2016.02.034 | © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用） | RESTRICTED | 3 |
| SRC-131 | Rao SSC, et al. Anorectal Disorders. Gastroenterology 2016;150:1430-1442 | 10.1053/j.gastro.2016.02.009 | © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用） | RESTRICTED | 3 |
| SRC-132 | Benninga MA, et al. Childhood Functional Gastrointestinal Disorders: Neonate/Toddler. Gastroenterology 2016;150:1443-1455 | 10.1053/j.gastro.2016.02.016 | © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用） | RESTRICTED | 3 |
| SRC-133 | Hyams JS, et al. Childhood Functional Gastrointestinal Disorders: Child/Adolescent. Gastroenterology 2016;150:1456-1468 | 10.1053/j.gastro.2016.02.015 | © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用） | RESTRICTED | 3 |
| SRC-134 | 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020 | — | © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認 | RESTRICTED | 13 |
| SRC-135 | 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日） | — | © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合 | RESTRICTED | 10 |
| SRC-136 | Chen JW, Rubenstein JH. Esophagogastric junction distensibility assessed using the functional lumen imaging probe. World J Gastroenterol 2017;23:1289-1297 | 10.3748/wjg.v23.i7.1289 | CC BY-NC 4.0（記事ページの表示） | RESTRICTED | 1 |
| SRC-137 | Rome Foundation『Rome V: A Global Framework for Disorders of Gut–Brain Interaction』（製品・概要ページ） | — | © 2026 Rome Foundation. All rights reserved | RESTRICTED | 6 |
| SRC-138 | Rome Foundation『Rome V, Disorders of Gut-Brain Interaction 5th Edition』（編集体制のページ） | — | © 2026 Rome Foundation. All rights reserved | RESTRICTED | 1 |
| SRC-139 | Rome Foundation『Rome V Journal Articles』（Gastroenterology 2026;170 掲載論文の一覧） | — | © 2026 Rome Foundation. All rights reserved | RESTRICTED | 1 |
| SRC-140 | Rosen R, et al. Rome V Pediatric Upper Gastrointestinal Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1347-1366 | 10.1053/j.gastro.2026.01.039 | CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）。ユーザー提供の原本で確認 | RESTRICTED | 6 |
| SRC-141 | Staller K, et al. Clin Gastroenterol Hepatol 2026（ContactME-IBS 登録データによる Rome III・IV・V の比較） | 10.1016/j.cgh.2026.07.022 | 原著は未取得。AGA の GI & Hepatology News（2026-08-20）の記事で内容を確認 | UNKNOWN | 1 |
| SRC-142 | Maev IV, et al. Rome V Criteria (2026): Continuity, innovations and major updates. Meditsinskiy sovet 2026;(8):8-21 | 10.21518/ms2026-232 | CC（記事ページの表示が BY-NC-ND と BY 4.0 で不一致。抄録のみ参照） | UNKNOWN | 2 |
| SRC-143 | Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V） | 10.1053/j.gastro.2026.02.003 | CC BY 4.0（© 2026 The Author(s)、AGA Institute） | OPEN | 23 |
| SRC-144 | Fukudo S, Aziz Q, Drossman DA, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2026;170:1283-1302（Rome V） | 10.1053/j.gastro.2025.12.038 | CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute） | RESTRICTED | 9 |
| SRC-145 | Rao SSC, Bharucha AE, Carrington EV, et al. Anorectal Disorders. Gastroenterology 2026;170:1318-1346（Rome V） | 10.1053/j.gastro.2026.01.037 | CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute） | RESTRICTED | 8 |
| SRC-146 | Elsenbruch S, Ballou S, Keefer L, et al. Biopsychosocial Aspects of Adult and Pediatric Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1205-1223（Rome V） | 10.1053/j.gastro.2026.02.009 | CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute） | RESTRICTED | 4 |
| SRC-147 | Palsson OS, Lacy BE, Benninga MA, et al. Development of the Rome V Diagnostic Questionnaires. Gastroenterology 2026;170:1408-1416 | 10.1053/j.gastro.2026.01.041 | CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute） | RESTRICTED | 7 |
| SRC-148 | 日本消化管学会編『便通異常症診療ガイドライン2023—慢性下痢症』南江堂、2023（第1刷 2023年7月13日、ISBN 978-4-524-21006-0） | — | © 日本消化管学会（非CC）。ユーザー提供の刊行版PDFで確認 | RESTRICTED | 8 |
| SRC-149 | Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V） | 10.1053/j.gastro.2026.02.005 | CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute） | RESTRICTED | 11 |
| SRC-150 | Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V） | 10.1053/j.gastro.2026.01.038 | CC BY 4.0（© 2026 The Author(s)、AGA Institute） | OPEN | 14 |
| SRC-151 | Greenwood-Van Meerveld B, Mawe GM, Beyder A, et al. Fundamentals of Neurogastroenterology: Basic Science. Gastroenterology 2026;170:1099-1113（Rome V） | 10.1053/j.gastro.2026.01.040 | CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute） | RESTRICTED | 5 |
| SRC-152 | Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V） | 10.1053/j.gastro.2026.01.036 | CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute） | RESTRICTED | 16 |
| SRC-153 | Drossman DA, Chang L, Tack J. Disorders of Gut–Brain Interaction and the Rome V Process. Gastroenterology 2026;170:1083-1098 | 10.1053/j.gastro.2026.02.014 | CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute） | RESTRICTED | 9 |

- SRC-100（Rome IV の序論）と SRC-102（Rome Foundation Global Study）は、Rome Foundation のサイトに掲載された論文 PDF を読みました。SRC-102 は論文中に CC BY-NC-ND と明記されているので `RESTRICTED` です。
- Rome IV の診断基準の本文（各疾患の基準文）は Rome Foundation の著作物で、商用利用には許諾が要ります。今回は分類の枠組みと新設・改名された疾患名だけを事実として使い、基準の文言は使っていません。
- NIDDK・NCCIH のページ（GOV_US）は 2017〜2019 年のレビューで、米国の情報です。日本の資料が見つかれば差し替えを検討してください。
- SRC-115〜120 は PMDA に掲載された医療用医薬品の添付文書です。著作権は製造販売業者にあるため `UNKNOWN` とし、効能・用量・副作用頻度などの事実だけを自作文で書いています。改訂年月をカードの source に記載しました。改訂されたら差し替えが必要です。
- SRC-127〜133 は Rome IV の各章です（Gastroenterology 2016 年5月号）。ポルトガル消化器病学会のサイトに掲載された写しで本文を確認し、出典には原誌を記載しました。基準文は転載せず、要件の骨子と数値だけを自作文で書いています。各章が引用した数値は「二次資料経由」としています。
- SRC-134 は先生から提供いただいた IBS 診療 GL 2020（日本語版、刊行物）です。英語版（SRC-049、IN-017〜026）と同じガイドラインなので、IN と重ならない CQ3-5 以降と BQ（病態）を中心に使いました。
- SRC-135 は便通異常症診療 GL 2023（慢性便秘症）です。最初は原稿段階の資料で作成しましたが、提供いただいた刊行版（第4刷）で NG-099〜108 の文言と推奨度を照合し、uncertainty に CQ・BQ 番号と頁を記録しました。内容の修正は不要でした。SRC-148 は同 GL の慢性下痢症（刊行版）です。頁は印刷された頁番号です。PDF には複製・抽出の制限がかかっているため、カードは自作文の要約にとどめ、文言は引用していません。
- SRC-137〜139 は Rome Foundation の公式ページ（Rome V の概要・編集体制・論文一覧）です。SRC-140 は Rome V 小児上部消化管の章で、ポルトガル小児科学会のサイトに掲載された写しで本文を確認しました。SRC-141（Staller ら）は原著が取得できず、AGA のニュース記事で確認したため `UNKNOWN`・二次資料経由です。SRC-142 は Rome V を概説した総説の抄録で、ページ上のライセンス表示が不一致のため `UNKNOWN` にしています。SRC-140 のライセンスは、提供いただいた原本で CC BY-NC-ND 4.0 と確認したので修正しました。SRC-143〜147 と SRC-149〜153 は提供いただいた Rome V の原本です（第9節）。小児上部消化管の章は2回目の提供分も同じ内容でした。
- 全カードの `legal_basis` は B（自作文による事実の記述）です。

## 4. 事実票 YAML

```yaml
- id: NG-001
  domain: NG
  subdomain: 腸脳相関病（DGBI）の概念と分類
  assertion:
    plain_statement_ja: Rome IVは、従来の機能性消化管疾患（FGID）を「腸脳相関の障害（disorders of gut-brain interaction：DGBI）」と言い換えるのが適切だとした。症状は、腸内細菌叢の乱れ、粘膜免疫の変化、内臓知覚過敏などの腸のシグナル伝達の変化、中枢神経系による腸のシグナルと運動の調節の異常などが組み合わさって生じると説明されている。
    condition:
      criteria: Rome IV（2016）
    differential: 器質的疾患（炎症、腫瘍、構造異常）
    common_misconception: 機能性消化管疾患は気のせいで、身体的な異常はない
  provenance:
    source_ref: SRC-100
    source: 'Drossman DA, Hasler WL. Rome IV—Functional GI Disorders: Disorders of Gut-Brain Interaction. Gastroenterology 2016;150:1257-1261'
    doi: 10.1053/j.gastro.2016.03.035
    pmid: null
    pmcid: null
    url: https://old.theromefoundation.org/wp-content/uploads/gastroenterology-rome-iv-introduction.pdf
    source_license: © 2016 AGA Institute（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)；TBL-02-07-005 (id: JlAKpjg)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-002
  domain: NG
  subdomain: 腸脳相関病（DGBI）の概念と分類
  assertion:
    plain_statement_ja: Rome IVは機能性消化管疾患を、A 食道疾患、B 胃十二指腸疾患、C 腸疾患、D 中枢性に介在される消化管の痛み、E 胆嚢およびOddi括約筋の疾患、F 肛門直腸疾患、G 新生児・乳幼児の機能性消化管疾患、H 小児・思春期の機能性消化管疾患、の8群に分け、成人33、小児17の疾患を定義している。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 機能性消化管疾患はIBSと機能性ディスペプシアの2つだけである
  provenance:
    source_ref: SRC-100
    source: 'Drossman DA, Hasler WL. Rome IV—Functional GI Disorders: Disorders of Gut-Brain Interaction. Gastroenterology 2016;150:1257-1261'
    doi: 10.1053/j.gastro.2016.03.035
    pmid: null
    pmcid: null
    url: https://old.theromefoundation.org/wp-content/uploads/gastroenterology-rome-iv-introduction.pdf
    source_license: © 2016 AGA Institute（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-003
  domain: NG
  subdomain: 腸脳相関病（DGBI）の概念と分類
  assertion:
    plain_statement_ja: Rome IVはRome IIIの10年後に公表され、オピオイド誘発性便秘、麻薬性腸症候群（narcotic bowel syndrome）、カンナビノイド悪阻症候群、逆流過敏症（reflux hypersensitivity）を新たに取り上げた。機能性腹痛症候群は中枢介在性腹痛症候群に名称が変わり、Oddi括約筋機能不全のⅠ型とⅢ型は機能性消化管疾患から外された。IBSの病型分類は一般人口の基準データにもとづいて改められた。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: Rome IVはRome IIIの診断名をそのまま引き継いだ
  provenance:
    source_ref: SRC-100
    source: 'Drossman DA, Hasler WL. Rome IV—Functional GI Disorders: Disorders of Gut-Brain Interaction. Gastroenterology 2016;150:1257-1261'
    doi: 10.1053/j.gastro.2016.03.035
    pmid: null
    pmcid: null
    url: https://old.theromefoundation.org/wp-content/uploads/gastroenterology-rome-iv-introduction.pdf
    source_license: © 2016 AGA Institute（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-268 (id: Jlvnl4o)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-004
  domain: NG
  subdomain: 日本神経消化器病学会
  assertion:
    plain_statement_ja: 日本神経消化器病学会は、1998年に設立された日本国際消化管運動研究会（日本消化器病学会の関連研究会）と、2002年に設立された日本Neurogastroenterology（神経消化器病）学会が、2009年4月1日に統合して発足した。前者の前身は、日本消化器病学会の付置研究会「消化管運動研究会」である。
    condition:
      region: 日本
    differential: null
    common_misconception: 日本神経消化器病学会は2002年に単独で設立された
  provenance:
    source_ref: SRC-101
    source: 日本神経消化器病学会ウェブサイト『沿革』
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/neuro-g/history.html
    source_license: 学会ウェブサイト（利用規約は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 学会サイトの記載。利用規約は人間が確認する。広報で使う場合は学会事務局の確認を受ける
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-005
  domain: NG
  subdomain: 日本神経消化器病学会
  assertion:
    plain_statement_ja: 日本神経消化器病学会は、「神経消化器病（機能性消化管疾患）」の認定医制度を設けている。
    condition:
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-101
    source: 日本神経消化器病学会ウェブサイト『沿革』
    doi: null
    pmid: null
    pmcid: null
    url: https://plaza.umin.ac.jp/neuro-g/history.html
    source_license: 学会ウェブサイト（利用規約は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 学会サイトのメニュー表記にもとづく。制度の要件は認定医制度のページで確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-006
  domain: NG
  subdomain: DGBIの疫学
  assertion:
    plain_statement_ja: Rome Foundation Global Studyは、6大陸33か国の成人73,076人を、インターネット調査（26か国、54,127人）と対面の世帯調査（9か国、18,949人）で調べた。Rome IV基準で何らかの機能性消化管疾患をもつ人の割合は、インターネット調査で40.3%、世帯調査で20.7%だった。
    condition:
      source: Rome Foundation Global Study（2021）
    differential: 調査方法によって有病率が大きく異なる
    common_misconception: 機能性消化管疾患はまれな病気である
  provenance:
    source_ref: SRC-102
    source: Sperber AD, et al. Worldwide Prevalence and Burden of Functional Gastrointestinal Disorders, Results of Rome Foundation Global Study. Gastroenterology 2021;160:99-114
    doi: 10.1053/j.gastro.2020.04.014
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/Worldwide-Prevalence-and-Burden-of-FGlD-Results-of-RF-Global-Study.pdf
    source_license: CC BY-NC-ND（論文中の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-007
  domain: NG
  subdomain: DGBIの疫学
  assertion:
    plain_statement_ja: 同じ調査で、疾患別の有病率（インターネット調査対世帯調査）は、機能性便秘11.7%対6.6%、機能性ディスペプシア7.2%対4.8%、機能性下痢4.7%対1.2%、IBS（Rome IV）4.1%対1.5%、機能性腹部膨満3.5%対1.2%だった。
    condition:
      source: Rome Foundation Global Study（2021）
    differential: null
    common_misconception: 機能性消化管疾患で最も多いのはIBSである
  provenance:
    source_ref: SRC-102
    source: Sperber AD, et al. Worldwide Prevalence and Burden of Functional Gastrointestinal Disorders, Results of Rome Foundation Global Study. Gastroenterology 2021;160:99-114
    doi: 10.1053/j.gastro.2020.04.014
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/Worldwide-Prevalence-and-Burden-of-FGlD-Results-of-RF-Global-Study.pdf
    source_license: CC BY-NC-ND（論文中の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)；TBL-01-00-268 (id: Jlvnl4o)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-008
  domain: NG
  subdomain: DGBIの疫学
  assertion:
    plain_statement_ja: 機能性消化管疾患は女性に多く、何らかの疾患をもつ割合はインターネット調査で女性46.5%、男性34.2%（オッズ比1.7）だった。IBS（Rome IV）の女性対男性のオッズ比は1.8（インターネット）と2.0（世帯）だった。
    condition:
      source: Rome Foundation Global Study（2021）
    differential: null
    common_misconception: 機能性消化管疾患に性差はない
  provenance:
    source_ref: SRC-102
    source: Sperber AD, et al. Worldwide Prevalence and Burden of Functional Gastrointestinal Disorders, Results of Rome Foundation Global Study. Gastroenterology 2021;160:99-114
    doi: 10.1053/j.gastro.2020.04.014
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/Worldwide-Prevalence-and-Burden-of-FGlD-Results-of-RF-Global-Study.pdf
    source_license: CC BY-NC-ND（論文中の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-009
  domain: NG
  subdomain: DGBIの疫学
  assertion:
    plain_statement_ja: 機能性消化管疾患をもつ人は、身体面・精神面の生活の質（PROMIS-10）が低く、腸の症状で医師を受診した割合も高かった（インターネット調査で46.5%対27.1%）。
    condition:
      source: Rome Foundation Global Study（2021）
    differential: null
    common_misconception: 機能性消化管疾患は生活の質や受診行動に影響しない
  provenance:
    source_ref: SRC-102
    source: Sperber AD, et al. Worldwide Prevalence and Burden of Functional Gastrointestinal Disorders, Results of Rome Foundation Global Study. Gastroenterology 2021;160:99-114
    doi: 10.1053/j.gastro.2020.04.014
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/Worldwide-Prevalence-and-Burden-of-FGlD-Results-of-RF-Global-Study.pdf
    source_license: CC BY-NC-ND（論文中の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-010
  domain: NG
  subdomain: DGBIの疫学
  assertion:
    plain_statement_ja: 日本のインターネット調査（2,504人）では、何らかの機能性消化管疾患が39.4%、機能性便秘16.6%、機能性下痢5.2%、機能性ディスペプシア2.4%、IBS 2.2%（Rome III基準では9.3%）、機能性腹部膨満1.2%だった。
    condition:
      source: Rome Foundation Global Study（2021）
      region: 日本
    differential: IBSの有病率は診断基準の版で大きく変わる
    common_misconception: 日本のIBS有病率はRome IVでも約10%である
  provenance:
    source_ref: SRC-102
    source: Sperber AD, et al. Worldwide Prevalence and Burden of Functional Gastrointestinal Disorders, Results of Rome Foundation Global Study. Gastroenterology 2021;160:99-114
    doi: 10.1053/j.gastro.2020.04.014
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/Worldwide-Prevalence-and-Burden-of-FGlD-Results-of-RF-Global-Study.pdf
    source_license: CC BY-NC-ND（論文中の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: IN-017（IBS 2.2%）とIN-029（機能性便秘16.6%）はGLが引用した同じ値。本カードはその一次資料
  uncertainty: 機能性ディスペプシアは本文で2.2%、表で2.4%と不整合があり、表の値を採った
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)；TBL-01-00-268 (id: Jlvnl4o)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-011
  domain: NG
  subdomain: 胃不全麻痺
  assertion:
    plain_statement_ja: 胃不全麻痺（gastroparesis）は、胃から小腸への食物の移動が遅れたり止まったりする疾患で、胃排出遅延とも呼ばれる。米国では10万人あたり男性約10人、女性約40人にみられ、同様の症状は成人の約4人に1人にみられるとされる。
    condition:
      source: NIDDK
      region: 米国
    differential: 機能性ディスペプシア（GD-007）、機械的な幽門・十二指腸の閉塞
    common_misconception: 胃不全麻痺は男性に多い
  provenance:
    source_ref: SRC-103
    source: NIDDK. Definition & Facts for Gastroparesis（最終レビュー 2018年1月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/gastroparesis/definition-facts
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 出典の最終レビューは2018年。日本の有病率は未確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-012
  domain: NG
  subdomain: 胃不全麻痺
  assertion:
    plain_statement_ja: 胃不全麻痺の危険因子には、糖尿病、迷走神経を傷つけうる食道・胃・小腸の手術、胸部や胃のあたりへの放射線治療などのがん治療がある。
    condition:
      source: NIDDK
      region: 米国
    differential: null
    common_misconception: 胃不全麻痺の原因は糖尿病だけである
  provenance:
    source_ref: SRC-103
    source: NIDDK. Definition & Facts for Gastroparesis（最終レビュー 2018年1月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/gastroparesis/definition-facts
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)；TBL-02-07-005 (id: JlAKpjg)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-013
  domain: NG
  subdomain: 胃不全麻痺
  assertion:
    plain_statement_ja: 胃不全麻痺の診断では、放射性物質を含む食事を食べて約4時間撮影する胃排出シンチグラフィ、呼気試験（約4時間）、ワイヤレス運動カプセルで胃排出を評価する。上部消化管内視鏡や画像検査で、症状の原因となる閉塞などを調べる。
    condition:
      source: NIDDK
      region: 米国
    differential: null
    common_misconception: 胃不全麻痺は内視鏡検査だけで診断できる
  provenance:
    source_ref: SRC-104
    source: NIDDK. Diagnosis of Gastroparesis（最終レビュー 2018年1月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/gastroparesis/diagnosis
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: シンチグラフィの判定基準（残留率の閾値）は出典に記載がない
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-014
  domain: NG
  subdomain: 胃不全麻痺
  assertion:
    plain_statement_ja: 胃不全麻痺の食事療法では、1日2〜3回の多い食事より5〜6回の少量の食事を勧め、低脂肪・低繊維で柔らかく調理した食品を選び、炭酸飲料と飲酒を避ける。糖尿病がある場合は、高血糖が胃排出をさらに遅らせるため血糖管理が重要である。
    condition:
      source: NIDDK
      region: 米国
    differential: null
    common_misconception: 胃不全麻痺では食物繊維を多くとるべきである
  provenance:
    source_ref: SRC-105
    source: NIDDK. Treatment for Gastroparesis（最終レビュー 2018年1月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/gastroparesis/treatment
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-015
  domain: NG
  subdomain: 胃不全麻痺
  assertion:
    plain_statement_ja: 胃不全麻痺の薬物療法には、胃の収縮を強めるメトクロプラミドやエリスロマイシンがある。制吐薬は悪心・嘔吐を和らげるが、胃排出は改善しない。薬で症状が抑えられない糖尿病性または特発性の胃不全麻痺には、胃電気刺激療法が使われることがある。
    condition:
      source: NIDDK
      region: 米国
    differential: 日本で使える薬剤と保険適用は異なる
    common_misconception: 制吐薬で胃排出は改善する
  provenance:
    source_ref: SRC-105
    source: NIDDK. Treatment for Gastroparesis（最終レビュー 2018年1月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/gastroparesis/treatment
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 米国の情報。日本の承認・保険適用は添付文書で確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-016
  domain: NG
  subdomain: 周期性嘔吐症候群
  assertion:
    plain_statement_ja: 周期性嘔吐症候群は、激しい悪心・嘔吐の発作（エピソード）を突然繰り返す機能性消化管疾患である。発作は数時間から数日続き、発作の間隔は数週間から数か月で、その間は症状がない。米国では毎年小児10万人あたり約3人が診断される。
    condition:
      source: NIDDK
      region: 米国
    differential: 消化管閉塞、頭蓋内病変、カンナビノイド悪阻症候群（NG-003）
    common_misconception: 周期性嘔吐症候群は小児だけの病気である
  provenance:
    source_ref: SRC-106
    source: NIDDK. Definition & Facts for Cyclic Vomiting Syndrome（最終レビュー 2017年12月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/cyclic-vomiting-syndrome/definition-facts
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 成人の頻度は不明とされる。出典の最終レビューは2017年
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-017
  domain: NG
  subdomain: 周期性嘔吐症候群
  assertion:
    plain_statement_ja: 周期性嘔吐症候群は、片頭痛やその家族歴がある人、長期の大麻使用歴がある人に起こりやすい。
    condition:
      source: NIDDK
    differential: null
    common_misconception: 周期性嘔吐症候群は心因性の嘔吐と同じである
  provenance:
    source_ref: SRC-106
    source: NIDDK. Definition & Facts for Cyclic Vomiting Syndrome（最終レビュー 2017年12月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/cyclic-vomiting-syndrome/definition-facts
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-018
  domain: NG
  subdomain: 周期性嘔吐症候群
  assertion:
    plain_statement_ja: 周期性嘔吐症候群の発作中は暗く静かな部屋で休み、制吐薬を使い、脱水には点滴を行う。発作のない時期の予防には、アミトリプチリン、シプロヘプタジン、プロプラノロール、トピラマート、ゾニサミドなどが使われ、誘因を知って避けることも予防になる。
    condition:
      source: NIDDK
      region: 米国
    differential: null
    common_misconception: 周期性嘔吐症候群は発作のない時期に治療は不要
  provenance:
    source_ref: SRC-107
    source: NIDDK. Treatment for Cyclic Vomiting Syndrome（最終レビュー 2017年12月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/cyclic-vomiting-syndrome/treatment
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 日本での保険適用は添付文書で確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-019
  domain: NG
  subdomain: 便失禁
  assertion:
    plain_statement_ja: 便失禁は、固形便・液状便・粘液を意図せず肛門から漏らすことで、最も多いのは便意を我慢できない切迫性便失禁であり、気づかないうちに漏れる漏出性便失禁もある。
    condition:
      source: NIDDK
    differential: null
    common_misconception: 便失禁は高齢者の避けられない老化現象である
  provenance:
    source_ref: SRC-108
    source: NIDDK. Definition & Facts for Bowel Control Problems (Fecal Incontinence)（最終レビュー 2017年7月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/bowel-control-problems-fecal-incontinence/definition-facts
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-020
  domain: NG
  subdomain: 便失禁
  assertion:
    plain_statement_ja: 米国では、地域で暮らす成人の7〜15%、入院中の成人の18〜33%、介護施設の成人の50〜70%、小児の約2%に便失禁がみられ、65歳を超えると起こりやすくなる。
    condition:
      source: NIDDK
      region: 米国
    differential: null
    common_misconception: 便失禁はまれで、ほとんど問題にならない
  provenance:
    source_ref: SRC-108
    source: NIDDK. Definition & Facts for Bowel Control Problems (Fecal Incontinence)（最終レビュー 2017年7月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/bowel-control-problems-fecal-incontinence/definition-facts
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 出典の最終レビューは2017年。日本の有病率は未確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-021
  domain: NG
  subdomain: 便失禁
  assertion:
    plain_statement_ja: 便失禁の治療には、食事と食物繊維の調整、下痢に対する止痢薬（ロペラミドなど）、決まった時間に排便する習慣づけ、骨盤底筋訓練、バイオフィードバック療法があり、バイオフィードバックは独習の骨盤底筋訓練より効果的とされる。これで改善しない場合に、仙骨神経刺激療法や、最も多い手術である肛門括約筋形成術などが検討される。
    condition:
      source: NIDDK
      region: 米国
    differential: null
    common_misconception: 便失禁の治療は手術しかない
  provenance:
    source_ref: SRC-109
    source: NIDDK. Treatment for Bowel Control Problems (Fecal Incontinence)（最終レビュー 2017年7月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/bowel-control-problems-fecal-incontinence/treatment
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-022
  domain: NG
  subdomain: 慢性偽性腸閉塞症
  assertion:
    plain_statement_ja: 慢性特発性偽性腸閉塞症（CIPO）は、腸管を閉塞させる器質的な病変がないのに、腹部膨満、悪心・嘔吐、腹痛などの腸閉塞症状が長く続き、画像で腸管の拡張と鏡面像を示す原因不明の難病である（指定難病99）。慢性偽性腸閉塞症は、腸管自体の疾患による一次性、全身疾患や薬剤による二次性、特発性に分けられる。
    condition:
      region: 日本
    differential: 機械的腸閉塞、二次性偽性腸閉塞（膠原病、神経疾患、内分泌疾患、薬剤など）
    common_misconception: 鏡面像があれば機械的腸閉塞である
  provenance:
    source_ref: SRC-110
    source: 厚生労働省 指定難病99『慢性特発性偽性腸閉塞症』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173520.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-024 (id: JlAKpko)；TBL-02-07-018 (id: JlAKpkQ)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-023
  domain: NG
  subdomain: 慢性偽性腸閉塞症
  assertion:
    plain_statement_ja: 日本のCIPOの患者数は小児約100人、成人約1,300人とされる。病理学的に確認された例の82%は神経節細胞に異常がなかった。病変は胃20%、小腸54%、大腸49%、直腸22%と広い範囲に及ぶことが多い。
    condition:
      region: 日本
    differential: null
    common_misconception: CIPOは小腸だけの病気である
  provenance:
    source_ref: SRC-110
    source: 厚生労働省 指定難病99『慢性特発性偽性腸閉塞症』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173520.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 罹患部位の割合は出典が引用した全国調査の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-024
  domain: NG
  subdomain: 慢性偽性腸閉塞症
  assertion:
    plain_statement_ja: CIPOの診断には、①入院を要する高度の腸閉塞症状が繰り返すか持続する、②症状が新生児期発症では2か月以上、乳児期以降の発症では6か月以上続く、③画像で腸管拡張と鏡面像がある、④腸管を閉塞させる器質的病変がない、⑤全層生検で神経叢に異常がない（生検できない場合はシネMRIや内圧検査で小腸主体の運動障害を示す）、⑥小児ではMMIHSと分節性腸管拡張症を除外する、⑦二次性の偽性腸閉塞を除外する、の7項目をすべて満たす必要がある。
    condition:
      region: 日本
      criteria: 指定難病の診断基準
    differential: null
    common_misconception: CIPOは腹部X線だけで診断できる
  provenance:
    source_ref: SRC-110
    source: 厚生労働省 指定難病99『慢性特発性偽性腸閉塞症』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173520.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-024 (id: JlAKpko)；TBL-02-07-031 (id: JlAKplI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-025
  domain: NG
  subdomain: 慢性偽性腸閉塞症
  assertion:
    plain_statement_ja: CIPOに根本的な治療はなく、重症例では減圧チューブ、腸瘻、中心静脈栄養が必要になる。2001〜2010年の全国調査では52%が腸瘻を造設し、4%が小腸移植を受けた。90%以上が長期生存していたが、改善が得られた例は少なく、平均罹病期間は14.6年だった。
    condition:
      region: 日本
      year: 2001〜2010年全国調査
    differential: null
    common_misconception: CIPOは手術で治癒する
  provenance:
    source_ref: SRC-110
    source: 厚生労働省 指定難病99『慢性特発性偽性腸閉塞症』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173520.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典が引用した全国調査の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-032 (id: JlAKplM)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-026
  domain: NG
  subdomain: 慢性偽性腸閉塞症
  assertion:
    plain_statement_ja: CIPOの重症度分類では、日常生活が著しく障害され、中心静脈栄養、経管栄養、持続的な腸管減圧のいずれかを要するものを重症とする。死因には、腸内細菌の異常増殖に伴う細菌の移行による敗血症性ショックや、長期の中心静脈栄養に伴う敗血症・肝不全がある。
    condition:
      region: 日本
      criteria: 指定難病の重症度分類
    differential: null
    common_misconception: CIPOは命にかかわらない
  provenance:
    source_ref: SRC-110
    source: 厚生労働省 指定難病99『慢性特発性偽性腸閉塞症』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173520.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-032 (id: JlAKplM)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-027
  domain: NG
  subdomain: ヒルシュスプルング病
  assertion:
    plain_statement_ja: ヒルシュスプルング病は、肛門から連続して腸管壁内の神経節細胞が欠如した腸管（無神経節腸管）があるために、生後数日のうちに機能的な腸閉塞症状で見つかる疾患である。病型は直腸下部型、S状結腸型、左右結腸型、全結腸型、小腸型に分けられ、全結腸以上に及ぶものは全体の約10%である。
    condition:
      region: 日本
    differential: CIPO（神経節細胞は存在する）
    common_misconception: ヒルシュスプルング病では神経節細胞が過剰になる
  provenance:
    source_ref: SRC-111
    source: 厚生労働省 指定難病291『ヒルシュスプルング病（全結腸型又は小腸型）』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001212061.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-276 (id: Jlvnl4c)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-028
  domain: NG
  subdomain: ヒルシュスプルング病
  assertion:
    plain_statement_ja: ヒルシュスプルング病は胎便排泄の遅れと腹部膨満で発症し、短域型では慢性便秘として経過することもある。無神経節腸管が長い例を放置すると、腸炎から敗血症に至り死亡することがある。日本の患者数は約10,000人で、うち全結腸型・小腸型は約1,000人とされる。
    condition:
      region: 日本
    differential: null
    common_misconception: ヒルシュスプルング病は成人の便秘では考えなくてよい
  provenance:
    source_ref: SRC-111
    source: 厚生労働省 指定難病291『ヒルシュスプルング病（全結腸型又は小腸型）』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001212061.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-276 (id: Jlvnl4c)；TBL-02-07-021 (id: JlAKpkY)；TBL-02-07-024 (id: JlAKpko)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-029
  domain: NG
  subdomain: ヒルシュスプルング病
  assertion:
    plain_statement_ja: ヒルシュスプルング病の確定診断には、直腸粘膜生検のアセチルコリンエステラーゼ染色で神経線維の増生と神経節細胞の欠如を示すか、手術標本の全層で神経節細胞の欠如を示す必要がある。根治術は無神経節腸管を切除して肛門に吻合する手術である。
    condition:
      region: 日本
      criteria: 指定難病の診断基準
    differential: null
    common_misconception: ヒルシュスプルング病は注腸造影だけで確定できる
  provenance:
    source_ref: SRC-111
    source: 厚生労働省 指定難病291『ヒルシュスプルング病（全結腸型又は小腸型）』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001212061.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-276 (id: Jlvnl4c)；TBL-02-07-031 (id: JlAKplI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-030
  domain: NG
  subdomain: ヒルシュスプルング病
  assertion:
    plain_statement_ja: 1998〜2002年の日本の全国調査（1,103例）では、ヒルシュスプルング病の死亡率は全体で3.0%だったが、全結腸以上の型で15.8%、小腸型で35.5%と高く、無神経節腸管がTreitz靱帯から75 cm以内に及ぶ例では83.3%に達した。
    condition:
      region: 日本
      year: 1998〜2002年全国調査
    differential: null
    common_misconception: ヒルシュスプルング病は病型にかかわらず予後良好
  provenance:
    source_ref: SRC-111
    source: 厚生労働省 指定難病291『ヒルシュスプルング病（全結腸型又は小腸型）』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001212061.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 出典が引用した全国調査の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-276 (id: Jlvnl4c)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-031
  domain: NG
  subdomain: IBSと腸脳相関
  assertion:
    plain_statement_ja: IBSは腸脳相関の問題を伴い、食物が消化管を速すぎたり遅すぎたり移動したり、通常量のガスや便で痛みを感じたりする。幼少期のつらい出来事（虐待など）、うつ病・不安症・身体症状症、消化管の細菌感染、小腸内細菌異常増殖（SIBO）、食物不耐症、遺伝的要因がIBSに関わると考えられている。
    condition:
      source: NIDDK
    differential: 感染後IBS（IN-019）
    common_misconception: IBSの原因はストレスだけである
  provenance:
    source_ref: SRC-112
    source: NIDDK. Symptoms & Causes of Irritable Bowel Syndrome（最終レビュー 2017年11月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/irritable-bowel-syndrome/symptoms-causes
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 出典の最終レビューは2017年
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-005 (id: JlAKpjg)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-032
  domain: NG
  subdomain: IBSと腸脳相関
  assertion:
    plain_statement_ja: 米国のIBS治療には、食物繊維の増量、グルテン除去、低FODMAP食などの食事療法に加え、認知行動療法、腸指向性催眠療法（gut-directed hypnotherapy）、リラクセーション訓練といった心理療法がある。
    condition:
      source: NIDDK
      region: 米国
    differential: 日本のIBS診療GL 2020は低FODMAP食の優位性を明らかでないとしている（IN-023）
    common_misconception: IBSに心理療法は役に立たない
  provenance:
    source_ref: SRC-113
    source: NIDDK. Treatment for Irritable Bowel Syndrome（最終レビュー 2017年11月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/irritable-bowel-syndrome/treatment
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 出典の最終レビューは2017年
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-033
  domain: NG
  subdomain: IBSと腸脳相関
  assertion:
    plain_statement_ja: 米国では、下痢型IBSにロペラミド、リファキシミン、エルクサドリン、アロセトロン（女性に限って処方）、便秘型IBSに食物繊維補助食品、下剤、ルビプロストン、リナクロチド、プレカナチド、腹痛に鎮痙薬、低用量の三環系抗うつ薬やSSRI、腸溶性ペパーミントオイルが用いられる。
    condition:
      source: NIDDK
      region: 米国
    differential: 日本で承認されている薬剤は米国と異なる
    common_misconception: IBSの薬物療法は病型にかかわらず同じ
  provenance:
    source_ref: SRC-113
    source: NIDDK. Treatment for Irritable Bowel Syndrome（最終レビュー 2017年11月）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.niddk.nih.gov/health-information/digestive-diseases/irritable-bowel-syndrome/treatment
    source_license: 米国連邦政府著作物（NIDDK。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 米国の情報（2017年時点）。日本の承認・保険適用は添付文書で確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-022 (id: JlAKpkc)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-034
  domain: NG
  subdomain: 腸内細菌叢とプロバイオティクス
  assertion:
    plain_statement_ja: プロバイオティクスは健康効果を意図して摂取する生きた微生物で、プレバイオティクスは有用な微生物の栄養となる難消化性の食品成分、シンバイオティクスは両者を組み合わせたものである。
    condition:
      source: NCCIH
    differential: null
    common_misconception: プロバイオティクスとプレバイオティクスは同じものである
  provenance:
    source_ref: SRC-114
    source: 'NCCIH. Probiotics: Usefulness and Safety（最終更新 2019年8月）'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.nccih.nih.gov/health/probiotics-usefulness-and-safety
    source_license: 米国連邦政府著作物（NCCIH。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-035
  domain: NG
  subdomain: 腸内細菌叢とプロバイオティクス
  assertion:
    plain_statement_ja: 抗菌薬とプロバイオティクスの併用は、抗菌薬関連下痢症の起こりやすさを約半分に減らすと報告され（2017年のレビュー）、抗菌薬投与中の小児と成人でC. difficile下痢症のリスクを下げることは中等度の確実性があるとされる。一方、IBSに対しては全般症状や腹痛を改善する可能性はあるものの、効果について明確な結論は出ていない。
    condition:
      source: NCCIH
    differential: null
    common_misconception: プロバイオティクスはIBSの確立した治療である
  provenance:
    source_ref: SRC-114
    source: 'NCCIH. Probiotics: Usefulness and Safety（最終更新 2019年8月）'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.nccih.nih.gov/health/probiotics-usefulness-and-safety
    source_license: 米国連邦政府著作物（NCCIH。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 出典の最終更新は2019年。有効な菌株・用量・期間は不明とされる
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-015 (id: JlAKpkI)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-036
  domain: NG
  subdomain: 腸内細菌叢とプロバイオティクス
  assertion:
    plain_statement_ja: 重い病気や免疫不全のある人ではプロバイオティクスによる有害事象のリスクが高く、米国FDAは2023年に、早産児がこれらの製品の微生物による重い感染症を起こす危険を警告した。米国では多くのプロバイオティクスが栄養補助食品として販売され、販売前のFDA承認を必要としない。
    condition:
      source: NCCIH
      region: 米国
    differential: null
    common_misconception: プロバイオティクスは誰にとっても無害である
  provenance:
    source_ref: SRC-114
    source: 'NCCIH. Probiotics: Usefulness and Safety（最終更新 2019年8月）'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.nccih.nih.gov/health/probiotics-usefulness-and-safety
    source_license: 米国連邦政府著作物（NCCIH。第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-037
  domain: NG
  subdomain: 腸脳相関病（DGBI）の概念と分類
  assertion:
    plain_statement_ja: Rome IVは2016年5月のGastroenterology特集号として19章で公表され、各疾患群の章に加えて、神経消化器病学の基礎科学、生理・運動と知覚、腸内微小環境、薬理学、年齢・性差、多文化的側面、生物心理社会的側面、臨床試験のデザイン、成人用診断質問票の章を含む。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: Rome IVは診断基準の一覧表だけである
  provenance:
    source_ref: SRC-126
    source: Rome Foundation『Special issue of Gastroenterology, May 2016』（Rome IV 特集号の章構成）
    doi: null
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/?p=565
    source_license: Rome Foundation ウェブサイト（利用規約は未確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-038
  domain: NG
  subdomain: 腸脳相関病（DGBI）の概念と分類
  assertion:
    plain_statement_ja: 多次元臨床プロファイル（MDCP）は、DGBIを、カテゴリー診断、臨床的修飾因子、生活への影響、心理社会的修飾因子、生理学的修飾因子の5つの次元で捉え、患者ごとの病態を多面的に記述するための枠組みである。
    condition:
      criteria: Rome Foundation MDCP
    differential: null
    common_misconception: DGBIの評価はRome基準の診断名だけで十分
  provenance:
    source_ref: SRC-125
    source: Iyengar P, Chang L. The multidimensional clinical profile for disorders of gut-brain interaction. 2024（Permanyer、ISSN 2462-7011）
    doi: 10.24875/NGL.23000008
    pmid: null
    pmcid: null
    url: https://oalib-perpustakaan.upi.edu/Record/doaj_e9fbd8ef8e2342c1b1d89f204986f193/Description
    source_license: 未確認（DOAJ収載のOA誌。抄録のみ参照）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録のみ参照。各次元の評価項目は原典で確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-039
  domain: NG
  subdomain: DGBIの国内承認薬
  assertion:
    plain_statement_ja: アコチアミドは、機能性ディスペプシアの食後膨満感、上腹部膨満感、早期満腹感に適応をもつアセチルコリンエステラーゼ阻害薬で、成人に1回100 mgを1日3回食前に投与する。心窩部痛や心窩部灼熱感に対する有効性は確認されていない。
    condition:
      region: 日本
    differential: 心窩部痛症候群（EPS）型の症状には適応外
    common_misconception: アコチアミドは機能性ディスペプシアのすべての症状に効く
  provenance:
    source_ref: SRC-115
    source: アコファイド錠100mg（アコチアミド塩酸塩水和物）添付文書 2023年8月改訂（第3版）、ゼリア新薬工業
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/PmdaSearch/iyakuDetail/380077_2399015F1020_1_09
    source_license: 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-040
  domain: NG
  subdomain: DGBIの国内承認薬
  assertion:
    plain_statement_ja: アコチアミドの投与前には、上部消化管内視鏡検査などで胃癌などの器質的疾患を除外する。1か月投与しても改善しなければ中止を考え、症状が続く場合は器質的疾患の可能性を再検討する。
    condition:
      region: 日本
    differential: null
    common_misconception: 機能性ディスペプシアの診断に器質的疾患の除外は不要
  provenance:
    source_ref: SRC-115
    source: アコファイド錠100mg（アコチアミド塩酸塩水和物）添付文書 2023年8月改訂（第3版）、ゼリア新薬工業
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/PmdaSearch/iyakuDetail/380077_2399015F1020_1_09
    source_license: 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-041
  domain: NG
  subdomain: DGBIの国内承認薬
  assertion:
    plain_statement_ja: アコチアミド300 mg/日を4週間投与した国内第Ⅲ相試験では、患者が改善と評価した割合が52.2%（プラセボ34.8%）、3症状すべてが消失した割合が15.3%（同9.0%）だった。
    condition:
      region: 日本
    differential: null
    common_misconception: アコチアミドで大半の患者の症状が完全に消える
  provenance:
    source_ref: SRC-115
    source: アコファイド錠100mg（アコチアミド塩酸塩水和物）添付文書 2023年8月改訂（第3版）、ゼリア新薬工業
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/PmdaSearch/iyakuDetail/380077_2399015F1020_1_09
    source_license: 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 添付文書の臨床成績の記載。原著論文と照合する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-042
  domain: NG
  subdomain: DGBIの国内承認薬
  assertion:
    plain_statement_ja: ラモセトロンは下痢型IBSに適応をもつ5-HT3受容体拮抗薬で、排便亢進と下痢を抑え、大腸の痛覚過敏を抑制するとされる。用量は男女で異なり、男性は1日1回5 μg（最高10 μg）、女性は1日1回2.5 μg（最高5 μg）である。
    condition:
      region: 日本
    differential: ロペラミドは止痢薬で、IBS特異的な薬ではない
    common_misconception: ラモセトロンは男女とも同じ用量で使う
  provenance:
    source_ref: SRC-116
    source: イリボー錠2.5μg・5μg（ラモセトロン塩酸塩）添付文書 2021年3月改訂（第2版）、アステラス製薬
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/PmdaSearch/iyakuDetail/ResultDataSetPDF/800126_2399014F1026_1_15
    source_license: 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-043
  domain: NG
  subdomain: DGBIの国内承認薬
  assertion:
    plain_statement_ja: ラモセトロンの重大な副作用には、虚血性大腸炎と、腸閉塞などを伴いうる重篤な便秘がある。腹痛や血便が出た場合は投与を中止し、便秘や硬便が出た場合は休薬や中止を検討する。
    condition:
      region: 日本
    differential: null
    common_misconception: 下痢型IBS治療薬で便秘が起きても問題ない
  provenance:
    source_ref: SRC-116
    source: イリボー錠2.5μg・5μg（ラモセトロン塩酸塩）添付文書 2021年3月改訂（第2版）、アステラス製薬
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/PmdaSearch/iyakuDetail/ResultDataSetPDF/800126_2399014F1026_1_15
    source_license: 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-044
  domain: NG
  subdomain: DGBIの国内承認薬
  assertion:
    plain_statement_ja: リナクロチドは、便秘型IBSと慢性便秘症（器質的疾患による便秘を除く）に適応をもつグアニル酸シクラーゼC受容体作動薬で、腸管分泌と腸管輸送を促すとともに大腸の痛覚過敏を改善するとされる。成人に0.5 mgを1日1回食前に投与し、症状により0.25 mgに減量する。主な副作用は下痢（11.6%）である。
    condition:
      region: 日本
    differential: null
    common_misconception: リナクロチドは食後に服用する
  provenance:
    source_ref: SRC-117
    source: リンゼス錠0.25mg（リナクロチド）添付文書 2026年8月改訂（第3版）、アステラス製薬
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/PmdaSearch/iyakuDetail/800126_2399017F1020_1_07
    source_license: 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-045
  domain: NG
  subdomain: DGBIの国内承認薬
  assertion:
    plain_statement_ja: エロビキシバットは、回腸末端の胆汁酸トランスポーター（IBAT）を阻害して大腸内の胆汁酸を増やし、水分分泌と消化管運動を高める慢性便秘症の治療薬である。成人に1日1回10 mg（最高15 mg）を食前に投与し、主な副作用は腹痛（23.2%）と下痢（14.4%）である。
    condition:
      region: 日本
    differential: null
    common_misconception: エロビキシバットは刺激性下剤である
  provenance:
    source_ref: SRC-118
    source: グーフィス錠5mg（エロビキシバット水和物）添付文書 2022年4月改訂（第2版）、EAファーマ
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/PmdaSearch/iyakuDetail/111890_2359008F1025_1_06
    source_license: 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-046
  domain: NG
  subdomain: DGBIの国内承認薬
  assertion:
    plain_statement_ja: ナルデメジンはオピオイド誘発性便秘症に適応をもつ末梢性μオピオイド受容体拮抗薬で、成人に0.2 mgを1日1回投与する。消化管閉塞またはその既往で再発のおそれが高い患者には禁忌で、オピオイドを中止したときは本剤も中止する。主な副作用は下痢（約21%）である。
    condition:
      region: 日本
    differential: Rome IVでオピオイド誘発性便秘が新たに取り上げられた（NG-003）
    common_misconception: ナルデメジンはオピオイドの鎮痛効果も打ち消す
  provenance:
    source_ref: SRC-119
    source: スインプロイク錠0.2mg（ナルデメジントシル酸塩）添付文書 2026年9月改訂（第3版）、塩野義製薬
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/PmdaSearch/iyakuDetail/340018_2359007F1020_1_07
    source_license: 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-047
  domain: NG
  subdomain: DGBIの国内承認薬
  assertion:
    plain_statement_ja: 日本でのリファキシミン（リフキシマ）の効能・効果は「肝性脳症における高アンモニア血症の改善」だけで、IBSや小腸内細菌異常増殖（SIBO）には承認されていない。
    condition:
      region: 日本
    differential: 米国では下痢型IBSに用いられる（NG-033）
    common_misconception: 日本でもリファキシミンはIBSの保険適用がある
  provenance:
    source_ref: SRC-120
    source: リフキシマ錠200mg（リファキシミン）添付文書 2024年3月改訂（第3版）、あすか製薬
    doi: null
    pmid: null
    pmcid: null
    url: https://www.pmda.go.jp/PmdaSearch/iyakuDetail/470007_6199001F1026_1_07
    source_license: 医療用医薬品の添付文書（PMDA掲載。著作権は製造販売業者。事実のみ使用）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-048
  domain: NG
  subdomain: げっぷ障害・反芻症候群
  assertion:
    plain_statement_ja: げっぷ障害は、胃内の空気が上がってくる過剰な胃げっぷと、食道に吸い込んだ空気がすぐに吐き出される胃上部げっぷ（supragastric belching）に分けられる。診断には24時間食道インピーダンス・pHモニタリング（MII-pH）が最も信頼できる方法とされ、胃上部げっぷが24時間に13回を超えると病的とする研究がある。
    condition:
      source: Sawada & Fujiwara 2024
    differential: GERDに伴うげっぷ
    common_misconception: げっぷはすべて胃の空気によるものである
  provenance:
    source_ref: SRC-122
    source: 'Sawada A, Fujiwara Y. Belching Disorders and Rumination Syndrome: A Literature Review. Digestion 2024;105:18-25'
    doi: 10.1159/000534092
    pmid: null
    pmcid: null
    url: https://karger.com/dig/article/105/1/18/864318/Belching-Disorders-and-Rumination-Syndrome-A
    source_license: © 2023 S. Karger AG, All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 閾値は総説が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-049
  domain: NG
  subdomain: げっぷ障害・反芻症候群
  assertion:
    plain_statement_ja: 胃上部げっぷには、認知行動療法や言語療法が有効で、50〜80%の患者で症状とげっぷの回数が改善すると報告されている。
    condition:
      source: Sawada & Fujiwara 2024
    differential: null
    common_misconception: げっぷ障害の治療は酸分泌抑制薬である
  provenance:
    source_ref: SRC-122
    source: 'Sawada A, Fujiwara Y. Belching Disorders and Rumination Syndrome: A Literature Review. Digestion 2024;105:18-25'
    doi: 10.1159/000534092
    pmid: null
    pmcid: null
    url: https://karger.com/dig/article/105/1/18/864318/Belching-Disorders-and-Rumination-Syndrome-A
    source_license: © 2023 S. Karger AG, All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 総説が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-050
  domain: NG
  subdomain: げっぷ障害・反芻症候群
  assertion:
    plain_statement_ja: 反芻症候群は、食べたばかりの食物が力まずに繰り返し口まで逆流する病態である。食後の高解像度インピーダンス内圧検査（HRIM）が診断の標準とされ、逆流に先立つ胃内圧の上昇（30 mmHg超）が目安として提案されている。
    condition:
      source: Sawada & Fujiwara 2024
    differential: 嘔吐（悪心と嘔吐運動を伴う）、GERD、胃不全麻痺
    common_misconception: 反芻症候群は嘔吐と同じである
  provenance:
    source_ref: SRC-122
    source: 'Sawada A, Fujiwara Y. Belching Disorders and Rumination Syndrome: A Literature Review. Digestion 2024;105:18-25'
    doi: 10.1159/000534092
    pmid: null
    pmcid: null
    url: https://karger.com/dig/article/105/1/18/864318/Belching-Disorders-and-Rumination-Syndrome-A
    source_license: © 2023 S. Karger AG, All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 閾値は総説が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-051
  domain: NG
  subdomain: げっぷ障害・反芻症候群
  assertion:
    plain_statement_ja: 反芻症候群の第一選択は、横隔膜呼吸を用いた認知行動療法であり、バイオフィードバックと組み合わせた認知行動療法で反芻の回数が約70%減ったとの報告がある。バクロフェン（10 mgを1日3回、2週間）で回数が減ったとする比較試験もある。インターネット調査による世界の有病率は、げっぷ障害1%、反芻症候群2.8%とされる。
    condition:
      source: Sawada & Fujiwara 2024
    differential: null
    common_misconception: 反芻症候群は制吐薬で治る
  provenance:
    source_ref: SRC-122
    source: 'Sawada A, Fujiwara Y. Belching Disorders and Rumination Syndrome: A Literature Review. Digestion 2024;105:18-25'
    doi: 10.1159/000534092
    pmid: null
    pmcid: null
    url: https://karger.com/dig/article/105/1/18/864318/Belching-Disorders-and-Rumination-Syndrome-A
    source_license: © 2023 S. Karger AG, All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は総説が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-052
  domain: NG
  subdomain: 直腸肛門機能検査
  assertion:
    plain_statement_ja: 国際肛門直腸生理ワーキンググループ（IAPWG）の標準検査プロトコルは、高解像度直腸肛門内圧検査（安静時圧、随意収縮、持続収縮、咳嗽、怒責、直腸肛門抑制反射）、直腸感覚検査（初発感覚、便意、最大耐容量の各容量）、50 mLの温水を入れたバルーンの排出検査（排出までの時間）の3つで構成される。
    condition:
      source: IAPWG 2020
    differential: null
    common_misconception: 直腸肛門機能は直腸診だけで評価できる
  provenance:
    source_ref: SRC-121
    source: 'Carrington EV, et al. The international anorectal physiology working group (IAPWG) recommendations: Standardized testing protocol and the London classification for disorders of anorectal function. Neurogastroenterol Motil 2020;32:e13679'
    doi: 10.1111/nmo.13679
    pmid: null
    pmcid: PMC7497505
    url: https://discovery-pp.ucl.ac.uk/id/eprint/10080132/1/Carrington_et_al-2019-Neurogastroenterology_%26_Motility.pdf
    source_license: CC BY 4.0（論文中の表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-053
  domain: NG
  subdomain: 直腸肛門機能検査
  assertion:
    plain_statement_ja: ロンドン分類は、直腸肛門の機能障害を、Part 1 直腸肛門抑制反射の障害、Part 2 肛門の緊張と収縮力の障害、Part 3 直腸肛門の協調の障害、Part 4 直腸感覚の障害、の4部に分けて記述する。
    condition:
      source: IAPWG 2020
    differential: null
    common_misconception: 直腸肛門の機能障害は1つの病名にまとめられる
  provenance:
    source_ref: SRC-121
    source: 'Carrington EV, et al. The international anorectal physiology working group (IAPWG) recommendations: Standardized testing protocol and the London classification for disorders of anorectal function. Neurogastroenterol Motil 2020;32:e13679'
    doi: 10.1111/nmo.13679
    pmid: null
    pmcid: PMC7497505
    url: https://discovery-pp.ucl.ac.uk/id/eprint/10080132/1/Carrington_et_al-2019-Neurogastroenterology_%26_Motility.pdf
    source_license: CC BY 4.0（論文中の表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-054
  domain: NG
  subdomain: 腸内細菌叢とプロバイオティクス
  assertion:
    plain_statement_ja: 2019年、米国で同じドナーの便による糞便微生物移植（FMT）を受けた免疫不全の成人2人がESBL産生大腸菌の侵襲性感染症を起こし、1人が死亡した。ドナー便は事前にESBL産生菌の検査を受けていなかった。
    condition:
      source: FDA
      region: 米国
      year: '2019'
    differential: null
    common_misconception: 便移植は健康な人の便なので感染の危険はない
  provenance:
    source_ref: SRC-123
    source: 'FDA. Fecal Microbiota for Transplantation: Safety Communication – Risk of Serious Adverse Reactions Due to Transmission of Multi-Drug Resistant Organisms（2019-06-13、06-18更新）'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.fda.gov/safety/medwatch-safety-alerts-human-medical-products/fecal-microbiota-transplantation-safety-communication-risk-serious-adverse-reactions-due
    source_license: 米国連邦政府著作物（第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-055
  domain: NG
  subdomain: 腸内細菌叢とプロバイオティクス
  assertion:
    plain_statement_ja: これを受けて米国FDAは、FMTを研究用（治験）として扱い、ドナーへの多剤耐性菌保菌の危険因子の問診と高リスク者の除外、ESBL産生腸内細菌、VRE、CRE、MRSAなどの多剤耐性菌のドナー便検査を求めた。
    condition:
      source: FDA
      region: 米国
    differential: null
    common_misconception: FMTは確立した標準治療として自由に行える
  provenance:
    source_ref: SRC-123
    source: 'FDA. Fecal Microbiota for Transplantation: Safety Communication – Risk of Serious Adverse Reactions Due to Transmission of Multi-Drug Resistant Organisms（2019-06-13、06-18更新）'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.fda.gov/safety/medwatch-safety-alerts-human-medical-products/fecal-microbiota-transplantation-safety-communication-risk-serious-adverse-reactions-due
    source_license: 米国連邦政府著作物（第三者素材を除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-056
  domain: NG
  subdomain: 神経疾患と消化管機能
  assertion:
    plain_statement_ja: パーキンソン病とパーキンソン症候群の患者を調べた研究では、何らかの便秘がパーキンソン病の約80%、パーキンソン症候群の約92%、健常対照の約55%にみられ、重い便秘はパーキンソン症候群（20.5%）でパーキンソン病（6.8%）より多かった。
    condition:
      source: Frazzitta 2019
    differential: null
    common_misconception: パーキンソン病の便秘はまれである
  provenance:
    source_ref: SRC-124
    source: 'Frazzitta G, et al. Severe Constipation in Parkinson''s Disease and in Parkinsonisms: Prevalence and Affecting Factors. Front Neurol 2019;10:621'
    doi: 10.3389/fneur.2019.00621
    pmid: null
    pmcid: PMC6591373
    url: https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2019.00621/full
    source_license: CC BY（記事ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 単施設の研究。便秘は運動症状に先行しうるとする記載は他研究の引用
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-021 (id: JlAKpkY)；TBL-02-07-005 (id: JlAKpjg)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-057
  domain: NG
  subdomain: 神経疾患と消化管機能
  assertion:
    plain_statement_ja: 同じ研究で、パーキンソン病の便秘の重さと独立して関連したのは年齢と運動障害の重症度（UPDRS）で、歩行距離が短い患者ほど便秘が重かった。
    condition:
      source: Frazzitta 2019
    differential: null
    common_misconception: パーキンソン病の便秘は抗パーキンソン病薬だけが原因である
  provenance:
    source_ref: SRC-124
    source: 'Frazzitta G, et al. Severe Constipation in Parkinson''s Disease and in Parkinsonisms: Prevalence and Affecting Factors. Front Neurol 2019;10:621'
    doi: 10.3389/fneur.2019.00621
    pmid: null
    pmcid: PMC6591373
    url: https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2019.00621/full
    source_license: CC BY（記事ページの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-058
  domain: NG
  subdomain: 機能性食道疾患
  assertion:
    plain_statement_ja: Rome IVの機能性食道疾患は、構造的・炎症性の異常、主要な食道運動障害、病的な酸逆流がないのに食道症状が出る疾患群で、内臓知覚過敏と過覚醒（hypervigilance）が症状に関わると考えられている。いずれも症状が最近3か月続き、診断の6か月以上前に始まっていることを求め、アカラシア、EGJ通過障害、収縮消失、遠位食道痙攣、ジャックハンマー食道は除外するが、無効食道運動などの境界的な所見は除外しない。
    condition:
      criteria: Rome IV（2016）
    differential: GERD、好酸球性食道炎、主要な食道運動障害（ES-025〜031）
    common_misconception: 内視鏡で異常がなければ食道の症状は気のせいである
  provenance:
    source_ref: SRC-127
    source: Aziz Q, et al. Functional Esophageal Disorders. Gastroenterology 2016;150:1368-1379
    doi: 10.1053/j.gastro.2016.02.012
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/10-Esophageal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-059
  domain: NG
  subdomain: 機能性食道疾患
  assertion:
    plain_statement_ja: 機能性胸痛は、食道由来と考えられる説明のつかない胸骨後部痛が週1回以上繰り返すもので、心臓の原因を先に除外する。非心臓性胸痛は一般人口の19〜33%にみられ、そのうち機能性胸痛は32〜35%とされる。精神科的併存症は最大75%にみられ、治療は抗うつ薬（三環系、SSRI、SNRI、トラゾドン）が第一選択で、認知行動療法や催眠療法を併用する。
    condition:
      criteria: Rome IV（2016）
    differential: 虚血性心疾患、GERD、食道運動障害
    common_misconception: 心臓に異常がない胸痛は治療の必要がない
  provenance:
    source_ref: SRC-127
    source: Aziz Q, et al. Functional Esophageal Disorders. Gastroenterology 2016;150:1368-1379
    doi: 10.1053/j.gastro.2016.02.012
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/10-Esophageal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-060
  domain: NG
  subdomain: 機能性食道疾患
  assertion:
    plain_statement_ja: 機能性胸やけは、十分な酸分泌抑制治療で改善しない胸骨後部の灼熱感が週2回以上あり、GERD、好酸球性食道炎、組織学的異常、主要な運動障害がないものである。PPI無効例の約50%、有効例の約25%に機能性胸やけが見つかると報告されている。逆流防止手術への移行は避け、低用量の三環系抗うつ薬やSSRIが選択肢となる。
    condition:
      criteria: Rome IV（2016）
    differential: 逆流過敏症（逆流と症状が関連する）
    common_misconception: PPIが効かない胸やけには逆流防止手術を行う
  provenance:
    source_ref: SRC-127
    source: Aziz Q, et al. Functional Esophageal Disorders. Gastroenterology 2016;150:1368-1379
    doi: 10.1053/j.gastro.2016.02.012
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/10-Esophageal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 割合はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-061
  domain: NG
  subdomain: 機能性食道疾患
  assertion:
    plain_statement_ja: 逆流過敏症は、内視鏡所見と酸曝露時間が正常なのに、逆流によって胸やけや胸痛が誘発されるもので、症状は週2回以上ある。酸分泌抑制治療が効いても診断は否定されない。NERD患者329例の研究では、逆流過敏症36%、真のNERD 40%、機能性胸やけ24%だった。治療は説明と保証、PPI、疼痛調節薬（三環系、SSRI、SNRI、ガバペンチノイド）が中心である。
    condition:
      criteria: Rome IV（2016）
    differential: NERD（酸曝露が異常）、機能性胸やけ（逆流との関連なし）
    common_misconception: 逆流過敏症はPPIが効けば否定できる
  provenance:
    source_ref: SRC-127
    source: Aziz Q, et al. Functional Esophageal Disorders. Gastroenterology 2016;150:1368-1379
    doi: 10.1053/j.gastro.2016.02.012
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/10-Esophageal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 内訳はRome IVの章が引用した研究の値（二次資料経由）。逆流過敏症をGERDの一部とみなす意見もある
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-062
  domain: NG
  subdomain: 機能性食道疾患
  assertion:
    plain_statement_ja: 食道球（globus）は、甲状軟骨と胸骨切痕の間の正中に、痛みのない塊や異物の感覚が持続的または間欠的に生じ、嚥下障害や嚥下痛を伴わず、食事の合間に感じるものである。健康な人の最大46%が経験し、75%で3年以上続く。治療の中心は説明と保証で、まず4〜8週間のPPI投与を試みる。
    condition:
      criteria: Rome IV（2016）
    differential: 咽喉頭の腫瘍、頸部食道の胃粘膜異所、GERD
    common_misconception: のどの異物感はすべて心因性である
  provenance:
    source_ref: SRC-127
    source: Aziz Q, et al. Functional Esophageal Disorders. Gastroenterology 2016;150:1368-1379
    doi: 10.1053/j.gastro.2016.02.012
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/10-Esophageal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-063
  domain: NG
  subdomain: 機能性食道疾患
  assertion:
    plain_statement_ja: 機能性嚥下障害は、器質的・粘膜・運動の異常がないのに、食塊が食道を通る感覚の異常を週1回以上感じるもので、機能性食道疾患の中で最も少ない。間欠的な固形物のつかえに50〜54Fのブジーで経験的に拡張すると68〜85%が改善したとの報告がある。
    condition:
      criteria: Rome IV（2016）
    differential: 好酸球性食道炎、アカラシア、食道癌
    common_misconception: 嚥下障害は内視鏡で異常がなければ放置してよい
  provenance:
    source_ref: SRC-127
    source: Aziz Q, et al. Functional Esophageal Disorders. Gastroenterology 2016;150:1368-1379
    doi: 10.1053/j.gastro.2016.02.012
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/10-Esophageal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: Rome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-064
  domain: NG
  subdomain: 機能性ディスペプシアのRome IV分類
  assertion:
    plain_statement_ja: Rome IVの機能性ディスペプシアは、食後のもたれ感や早期飽満感が週3日以上ある食後愁訴症候群（PDS）と、心窩部痛や心窩部灼熱感が週1日以上ある心窩部痛症候群（EPS）に分けられ、両者は重なりうる。機能性ディスペプシア患者の25〜35%に胃排出遅延がある。PPIはPDSの症状には効かず、アコチアミドはPDSに有効でEPSには効かない（NNT 6）とされる。
    condition:
      criteria: Rome IV（2016）
    differential: 日本のFD診療GL 2021はRome基準の4症状に限定しない（GD-001）
    common_misconception: 機能性ディスペプシアの治療はPPIだけで十分
  provenance:
    source_ref: SRC-128
    source: Stanghellini V, et al. Gastroduodenal Disorders. Gastroenterology 2016;150:1380-1392
    doi: 10.1053/j.gastro.2016.02.011
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/11-Gastroduodenal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-065
  domain: NG
  subdomain: 悪心・嘔吐症
  assertion:
    plain_statement_ja: 慢性悪心嘔吐症候群（CNVS）は、悪心が週1日以上、または嘔吐が週1回以上あり、自己誘発性嘔吐、摂食障害、吐出、反芻を除外したものである。原因不明の嘔吐が月1回以上ある人は女性の約2%、男性の約3%とされる。
    condition:
      criteria: Rome IV（2016）
    differential: 周期性嘔吐症候群、カンナビノイド悪阻症候群、胃不全麻痺
    common_misconception: 慢性の嘔吐は必ず器質的疾患による
  provenance:
    source_ref: SRC-128
    source: Stanghellini V, et al. Gastroduodenal Disorders. Gastroenterology 2016;150:1380-1392
    doi: 10.1053/j.gastro.2016.02.011
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/11-Gastroduodenal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頻度はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-066
  domain: NG
  subdomain: 周期性嘔吐症候群
  assertion:
    plain_statement_ja: Rome IVの周期性嘔吐症候群は、急に始まり1週間未満で治まる型どおりの嘔吐発作が、1週間以上の無症状期をはさんで繰り返すものである。原因不明の悪心・嘔吐で紹介された成人の3〜14%を占め、成人では診断までに救急外来を中央値15回受診し、発症から5〜6年かかるとの報告がある。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 周期性嘔吐症候群はすぐに診断がつく
  provenance:
    source_ref: SRC-128
    source: Stanghellini V, et al. Gastroduodenal Disorders. Gastroenterology 2016;150:1380-1392
    doi: 10.1053/j.gastro.2016.02.011
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/11-Gastroduodenal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-067
  domain: NG
  subdomain: 周期性嘔吐症候群
  assertion:
    plain_statement_ja: カンナビノイド悪阻症候群は、長期間の過剰な大麻使用の後に周期性嘔吐症候群に似た発作を起こすもので、典型例は1日3〜5回の使用を2年以上続けた男性である。嘔吐期に熱いシャワーや入浴で症状が和らぎ、大麻を継続的に中止すると治まる。周期性嘔吐症候群と考えられた患者の約3分の1が大麻使用を報告している。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 大麻は嘔吐を止めるので悪化の原因にはならない
  provenance:
    source_ref: SRC-128
    source: Stanghellini V, et al. Gastroduodenal Disorders. Gastroenterology 2016;150:1380-1392
    doi: 10.1053/j.gastro.2016.02.011
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/11-Gastroduodenal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: Rome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-068
  domain: NG
  subdomain: げっぷ障害・反芻症候群
  assertion:
    plain_statement_ja: Rome IVでは、過剰で厄介なげっぷが週3日を超える場合をげっぷ障害とし、食道からの胃上部げっぷと胃からの過剰な胃げっぷに分ける。胃上部げっぷは1分間に最大20回に達することがある。反芻症候群は、えずきを伴わずに直前に食べた食物が口まで逆流し、毎食後に起こることが多く、横隔膜呼吸による習慣逆転法が主な治療で、PPIは反芻を長引かせることがある。
    condition:
      criteria: Rome IV（2016）
    differential: 嘔吐、GERD
    common_misconception: 反芻症候群にはPPIが有効である
  provenance:
    source_ref: SRC-128
    source: Stanghellini V, et al. Gastroduodenal Disorders. Gastroenterology 2016;150:1380-1392
    doi: 10.1053/j.gastro.2016.02.011
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/11-Gastroduodenal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-069
  domain: NG
  subdomain: 機能性腸疾患（Rome IV）
  assertion:
    plain_statement_ja: Rome IVは、IBS、機能性便秘、機能性下痢、機能性腹部膨満などの機能性腸疾患を、はっきり分かれた病気ではなく連続したスペクトラムととらえ、互いに大きく重なりうるとしている。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 機能性腸疾患の病名は互いに独立して重ならない
  provenance:
    source_ref: SRC-129
    source: Lacy BE, et al. Bowel Disorders. Gastroenterology 2016;150:1393-1407
    doi: 10.1053/j.gastro.2016.02.031
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/12-Bowel-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-268 (id: Jlvnl4o)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-070
  domain: NG
  subdomain: 機能性腸疾患（Rome IV）
  assertion:
    plain_statement_ja: Rome IVのIBSは、最近3か月間に平均して週1日以上の腹痛があり、排便との関連、排便頻度の変化、便形状の変化のうち2つ以上を伴うものである。病型はブリストル便形状尺度で決め、硬便（タイプ1〜2）が排便の25%を超え軟便（タイプ6〜7）が25%未満ならIBS-C、その逆ならIBS-D、どちらも25%を超えればIBS-Mとする。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: IBSの診断には大腸内視鏡で異常がないことだけで十分
  provenance:
    source_ref: SRC-129
    source: Lacy BE, et al. Bowel Disorders. Gastroenterology 2016;150:1393-1407
    doi: 10.1053/j.gastro.2016.02.031
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/12-Bowel-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-071
  domain: NG
  subdomain: 機能性腸疾患（Rome IV）
  assertion:
    plain_statement_ja: 機能性下痢は、腹痛や厄介な膨満が主でないまま、軟便・水様便が排便の25%を超えるもので、IBS-Dの基準を満たすものは除く。有病率は報告により1.5〜17%と幅がある。
    condition:
      criteria: Rome IV（2016）
    differential: IBS-D、胆汁酸性下痢、顕微鏡的大腸炎、セリアック病
    common_misconception: 腹痛のない慢性下痢もIBSと診断する
  provenance:
    source_ref: SRC-129
    source: Lacy BE, et al. Bowel Disorders. Gastroenterology 2016;150:1393-1407
    doi: 10.1053/j.gastro.2016.02.031
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/12-Bowel-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率はRome IVの章が引用した値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-072
  domain: NG
  subdomain: 機能性腸疾患（Rome IV）
  assertion:
    plain_statement_ja: 機能性腹部膨満（膨満感・腹部膨隆）は、週1日以上の膨満感や腹部膨隆が他の症状より目立ち、IBS、機能性便秘、機能性下痢、食後愁訴症候群の基準を満たさないものである。膨満感を訴える人のうち実際に腹囲の膨隆が測定されるのは約50〜60%で、米国の電話調査では成人の15.9%（女性19.2%、男性10.5%）が過去1か月に膨満を報告した。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 膨満感があれば必ず腹部が膨らんでいる
  provenance:
    source_ref: SRC-129
    source: Lacy BE, et al. Bowel Disorders. Gastroenterology 2016;150:1393-1407
    doi: 10.1053/j.gastro.2016.02.031
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/12-Bowel-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-024 (id: JlAKpko)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-073
  domain: NG
  subdomain: 機能性腸疾患（Rome IV）
  assertion:
    plain_statement_ja: オピオイド誘発性便秘は、オピオイドの開始や増量の後に新たに生じるか悪化した便秘で、Rome IVは独立した機能性腸疾患ではなくオピオイドの有害作用として扱うが、機能性便秘と重なることが多いとしている。がん以外の慢性疼痛でオピオイドを使う患者の約41%に起こると報告されている。
    condition:
      criteria: Rome IV（2016）
    differential: 治療薬はナルデメジン（NG-046）など
    common_misconception: オピオイドによる便秘は耐性ができて自然に治る
  provenance:
    source_ref: SRC-129
    source: Lacy BE, et al. Bowel Disorders. Gastroenterology 2016;150:1393-1407
    doi: 10.1053/j.gastro.2016.02.031
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/12-Bowel-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頻度はRome IVの章が引用したシステマティックレビューの値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-074
  domain: NG
  subdomain: 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: 中枢介在性腹痛症候群（CAPS）は、ほぼ持続的または頻繁に繰り返す腹痛で、食事、排便、月経などの生理的な出来事とはほとんど関係せず、仕事や家庭生活などの日常機能を一部損なうものである。症状は診断の6か月以上前に始まり、最近3か月基準を満たす必要がある。有病率は0.5〜2.1%で、女性に1.5〜2倍多く、40歳代に多い。
    condition:
      criteria: Rome IV（2016）
    differential: IBS（腹痛が排便と関連する）
    common_misconception: 中枢介在性腹痛は心因性の詐病である
  provenance:
    source_ref: SRC-130
    source: Keefer L, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2016;150:1408-1419
    doi: 10.1053/j.gastro.2016.02.034
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/13-Centrally-Mediated-Disorders-of-Gastrointestinal-Pain.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率はRome IVの章が引用した値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-075
  domain: NG
  subdomain: 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: 麻薬性腸症候群（narcotic bowel syndrome、オピオイド誘発性消化管痛覚過敏）は、高用量または長期のオピオイドで治療中の腹痛が、オピオイドの継続や増量で悪化または十分に改善せず、効果が切れると悪化し再投与で和らぐなどの特徴をもつものである。多くは経口モルヒネ換算で1日75 mg以上を使っている。
    condition:
      criteria: Rome IV（2016）
    differential: 消化管閉塞、慢性膵炎などの器質的な腹痛
    common_misconception: オピオイドで改善しない腹痛にはさらに増量すべき
  provenance:
    source_ref: SRC-130
    source: Keefer L, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2016;150:1408-1419
    doi: 10.1053/j.gastro.2016.02.034
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/13-Centrally-Mediated-Disorders-of-Gastrointestinal-Pain.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-076
  domain: NG
  subdomain: 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: 中枢介在性の消化管の痛みの治療では、神経調節薬として三環系抗うつ薬が最も研究され（IBSでの改善の相対リスク1.93）、認知行動療法、精神力動的対人関係療法、マインドフルネス、催眠療法などの心理療法が有望とされる。麻薬性腸症候群にはオピオイドの完全な離脱が勧められ、39例の7日間入院離脱プログラムでは89.7%が完了し、60%が改善した。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 慢性の腹痛にはオピオイドが最も有効である
  provenance:
    source_ref: SRC-130
    source: Keefer L, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2016;150:1408-1419
    doi: 10.1053/j.gastro.2016.02.034
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/13-Centrally-Mediated-Disorders-of-Gastrointestinal-Pain.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-077
  domain: NG
  subdomain: 機能性肛門直腸疾患
  assertion:
    plain_statement_ja: 機能性肛門直腸痛には、恥骨直腸筋の牽引で圧痛があり30分以上続く慢性・反復性の直腸痛（肛門挙筋症候群）、同じ症状で圧痛のない非特異的機能性肛門直腸痛、数秒から最長30分の突然の激しい直腸痛で間欠期に痛みのない一過性直腸痛（proctalgia fugax）がある。一過性直腸痛の有病率は8〜18%とされる。
    condition:
      criteria: Rome IV（2016）
    differential: 痔核、裂肛、肛門周囲膿瘍、直腸癌
    common_misconception: 肛門痛は必ず痔によるものである
  provenance:
    source_ref: SRC-131
    source: Rao SSC, et al. Anorectal Disorders. Gastroenterology 2016;150:1430-1442
    doi: 10.1053/j.gastro.2016.02.009
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/15-Anorectal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-078
  domain: NG
  subdomain: 機能性肛門直腸疾患
  assertion:
    plain_statement_ja: 機能性排便障害は、機能性便秘またはIBS-Cの基準を満たし、バルーン排出検査、直腸肛門内圧検査または肛門筋電図、画像による排出評価の3つのうち2つ以上で異常を示すもので、内圧検査で推進力が不十分な排便推進力不全と、推進力は十分だが排便時に骨盤底筋が不適切に収縮する排便協調障害に分けられる。
    condition:
      criteria: Rome IV（2016）
    differential: 大腸通過遅延型便秘
    common_misconception: 排便困難は下剤を増やせば解決する
  provenance:
    source_ref: SRC-131
    source: Rao SSC, et al. Anorectal Disorders. Gastroenterology 2016;150:1430-1442
    doi: 10.1053/j.gastro.2016.02.009
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/15-Anorectal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-079
  domain: NG
  subdomain: 機能性肛門直腸疾患
  assertion:
    plain_statement_ja: 排便協調障害にはバイオフィードバック療法が第一選択とされ、無作為化試験では3か月後に協調障害が改善したのはバイオフィードバック群79%、偽フィードバック群4%、標準治療群6%だった。肛門挙筋症候群でも、バイオフィードバックで87%が十分な疼痛緩和を得たとの報告がある（電気刺激45%、マッサージ22%）。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 排便協調障害に有効な治療はない
  provenance:
    source_ref: SRC-131
    source: Rao SSC, et al. Anorectal Disorders. Gastroenterology 2016;150:1430-1442
    doi: 10.1053/j.gastro.2016.02.009
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/15-Anorectal-Disorders.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: Rome IVの章が引用したRCTの値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-080
  domain: NG
  subdomain: 小児の機能性消化管疾患
  assertion:
    plain_statement_ja: 乳児の吐き戻し（乳児逆流症）は、生後3週から12か月の健康な乳児で1日2回以上の吐き戻しが3週間以上続き、えずき、吐血、誤嚥、無呼吸、体重増加不良などがないものである。生後4か月の健康な乳児の41〜67%で1日1回を超える吐き戻しがあり、約90%は12か月までに自然に治まる。PPIは乳児の吐き戻しに有効でなく、感染症などの危険があるため、不要な酸分泌抑制は避ける。
    condition:
      criteria: Rome IV（2016）
    differential: 乳児GERD、肥厚性幽門狭窄症、牛乳アレルギー
    common_misconception: 乳児の吐き戻しにはPPIを使うべきである
  provenance:
    source_ref: SRC-132
    source: 'Benninga MA, et al. Childhood Functional Gastrointestinal Disorders: Neonate/Toddler. Gastroenterology 2016;150:1443-1455'
    doi: 10.1053/j.gastro.2016.02.016
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/16-Childhood-Functional-Gastrointestinal-Disorders-Neonate-Toddler.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-081
  domain: NG
  subdomain: 小児の機能性消化管疾患
  assertion:
    plain_statement_ja: 乳児疝痛（コリック）は、生後5か月未満の乳児が明らかな原因なく長く泣き続け、養育者がなだめられない状態で、5〜19%にみられ、多くは生後3〜5か月で治まる。薬物療法の有効性は示されておらず、養育者の支援が治療の中心である。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 乳児疝痛には薬物治療が必要である
  provenance:
    source_ref: SRC-132
    source: 'Benninga MA, et al. Childhood Functional Gastrointestinal Disorders: Neonate/Toddler. Gastroenterology 2016;150:1443-1455'
    doi: 10.1053/j.gastro.2016.02.016
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/16-Childhood-Functional-Gastrointestinal-Disorders-Neonate-Toddler.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頻度はRome IVの章が引用した値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-082
  domain: NG
  subdomain: 小児の機能性消化管疾患
  assertion:
    plain_statement_ja: 乳幼児の機能性便秘は、週2回以下の排便、痛みを伴う硬い便、直腸の大きな便塊などのうち2つ以上が1か月続くもので、有病率は生後1年目で約2.9%、2年目で約10.1%とされる。治療は養育者への説明から始め、非刺激性下剤の毎日投与とトイレトレーニングの行動的な工夫を組み合わせる。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 乳幼児の便秘は浣腸だけで治療する
  provenance:
    source_ref: SRC-132
    source: 'Benninga MA, et al. Childhood Functional Gastrointestinal Disorders: Neonate/Toddler. Gastroenterology 2016;150:1443-1455'
    doi: 10.1053/j.gastro.2016.02.016
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/16-Childhood-Functional-Gastrointestinal-Disorders-Neonate-Toddler.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率はRome IVの章が引用した値（二次資料経由）。日本の小児慢性機能性便秘症診療GLは今回未参照
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-083
  domain: NG
  subdomain: 小児の機能性消化管疾患
  assertion:
    plain_statement_ja: 腹部片頭痛は、臍周囲・正中・びまん性の1時間以上続く激しい腹痛発作が2回以上あり、発作は型どおりで日常生活ができないほど強く、食欲不振、悪心、嘔吐、頭痛、光過敏、顔面蒼白のうち2つ以上を伴い、数週から数か月の無症状期をはさむものである。有病率は基準により1〜23%と幅がある。予防にはピゾチフェン、アミトリプチリン、プロプラノロール、シプロヘプタジンが使われている。
    condition:
      criteria: Rome IV（2016）
    differential: 周期性嘔吐症候群、腸回転異常症、尿路閉塞
    common_misconception: 小児の反復性腹痛はすべて心因性である
  provenance:
    source_ref: SRC-133
    source: 'Hyams JS, et al. Childhood Functional Gastrointestinal Disorders: Child/Adolescent. Gastroenterology 2016;150:1456-1468'
    doi: 10.1053/j.gastro.2016.02.015
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/17-Childhood-Functional-Gastrointestinal-Disorders-Child-Adolescent.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率はRome IVの章が引用した値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-084
  domain: NG
  subdomain: 小児の機能性消化管疾患
  assertion:
    plain_statement_ja: 小児・思春期の機能性便秘の有病率はシステマティックレビューで平均14%とされ、トイレトレーニングの時期に多い。Rome IVは症状の持続期間を2か月から1か月に短縮した。治療は便塞栓の除去と維持療法の2段階で、ポリエチレングリコールが第一選択であり、定時の排便、排便日誌、報酬などの教育も薬と同じく重要である。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 小児の便秘は成長すれば自然に治るので治療は不要
  provenance:
    source_ref: SRC-133
    source: 'Hyams JS, et al. Childhood Functional Gastrointestinal Disorders: Child/Adolescent. Gastroenterology 2016;150:1456-1468'
    doi: 10.1053/j.gastro.2016.02.015
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/17-Childhood-Functional-Gastrointestinal-Disorders-Child-Adolescent.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率はRome IVの章が引用した値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-085
  domain: NG
  subdomain: 小児の機能性消化管疾患
  assertion:
    plain_statement_ja: 小学生の35〜38%が毎週腹痛を訴えるが、機能性腹痛症の基準を満たすのはその約3分の1である。小児の機能性腹痛症の治療は行動療法・心理療法が中心で、催眠療法と認知行動療法で短期・長期の効果が示されている。思春期の抗うつ薬には、米国FDAによる自殺念慮の枠付き警告がある。
    condition:
      criteria: Rome IV（2016）
    differential: null
    common_misconception: 小児の機能性腹痛には鎮痛薬が第一選択である
  provenance:
    source_ref: SRC-133
    source: 'Hyams JS, et al. Childhood Functional Gastrointestinal Disorders: Child/Adolescent. Gastroenterology 2016;150:1456-1468'
    doi: 10.1053/j.gastro.2016.02.015
    pmid: null
    pmcid: null
    url: https://www.spg.pt/wp-content/uploads/2023/03/17-Childhood-Functional-Gastrointestinal-Disorders-Child-Adolescent.pdf
    source_license: © 2016 AGA Institute（非CC。Rome IV の基準文の転載はせず、事実のみ使用）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値はRome IVの章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-086
  domain: NG
  subdomain: IBSの病態（日本のGL）
  assertion:
    plain_statement_ja: IBSの病態にはストレスが関わる。IBS患者ではストレス負荷と消化器症状悪化の相関が健常者より強く、心理社会的ストレスで大腸運動が亢進する。ストレス反応の中心物質である副腎皮質刺激ホルモン放出ホルモン（CRH）の負荷で、IBS患者は大腸運動の亢進や扁桃体の活性化が健常者より強く、CRHと逆に働くオキシトシンは内臓知覚過敏を和らげる。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 BQ1-3、BQ1-5
    differential: null
    common_misconception: ストレスと腸の症状は無関係である
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-005 (id: JlAKpjg)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-087
  domain: NG
  subdomain: IBSの病態（日本のGL）
  assertion:
    plain_statement_ja: IBSの病態には、腸内細菌、粘膜透過性の亢進、粘膜の微小炎症が関わり、これらが神経の感作を介して中枢機能にも影響すると考えられている。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 BQ1-4
    differential: 炎症性腸疾患（明らかな粘膜炎症がある）
    common_misconception: IBSの腸粘膜は完全に正常である
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-088
  domain: NG
  subdomain: IBSの病態（日本のGL）
  assertion:
    plain_statement_ja: 脳機能画像のメタ解析では、大腸伸展刺激に対してIBS患者は前帯状回、扁桃体、中脳の信号が強まり、内側・外側前頭前野の信号が弱まると報告されている。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 BQ1-5
    differential: null
    common_misconception: IBSでは脳の反応に異常はない
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: GLが引用したメタ解析の所見（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-005 (id: JlAKpjg)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-089
  domain: NG
  subdomain: IBSの病態（日本のGL）
  assertion:
    plain_statement_ja: IBSは単一遺伝子の病気ではないが、遺伝が関わる。双生児6,060組の研究では、IBSの一致率は一卵性17.2%、二卵性8.4%だった。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 BQ1-7
    differential: null
    common_misconception: IBSは遺伝とはまったく関係がない
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: GLが引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-090
  domain: NG
  subdomain: IBSの治療（日本のGL）
  assertion:
    plain_statement_ja: 日本のIBS診療ガイドライン2020は、プロバイオティクスをIBSの治療に用いることを推奨している（強い推奨、エビデンスレベルA）。抗コリン薬は腹痛などに投与することを提案している（弱い推奨、B）。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 CQ3-5、CQ3-6
    differential: 米国NCCIHは効果について明確な結論は出ていないとしている（NG-035）
    common_misconception: プロバイオティクスはIBSに無効とされている
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-091
  domain: NG
  subdomain: IBSの治療（日本のGL）
  assertion:
    plain_statement_ja: 日本のIBS診療ガイドライン2020は、下痢型IBSに5-HT3拮抗薬を投与することを推奨している（強い推奨、エビデンスレベルA）。海外のアロセトロンは、虚血性腸炎や重い便秘の副作用のため、重症の下痢型IBSの女性に限って使われている。止痢薬は一部の下痢型IBSに提案される（弱い推奨、C）。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 CQ3-7、CQ3-8
    differential: 日本の5-HT3拮抗薬はラモセトロン（NG-042）
    common_misconception: 下痢型IBSの治療は止痢薬が第一選択である
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-092
  domain: NG
  subdomain: IBSの治療（日本のGL）
  assertion:
    plain_statement_ja: 日本のIBS診療ガイドライン2020は、便秘型IBSに粘膜上皮機能変容薬（ルビプロストン、リナクロチド）を推奨し（強い推奨、エビデンスレベルA）、胆汁酸・胆汁酸トランスポーター阻害薬、5-HT4刺激薬、非刺激性下剤の投与を提案している（いずれも弱い推奨）。刺激性下剤を使う場合は原則として頓用とする（弱い推奨、D）。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 CQ3-9〜3-13
    differential: null
    common_misconception: 便秘型IBSには刺激性下剤を毎日使う
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-093
  domain: NG
  subdomain: IBSの治療（日本のGL）
  assertion:
    plain_statement_ja: 日本のIBS診療ガイドライン2020は、三環系抗うつ薬やSSRIを病態に応じて症例を選んで投与することを提案している（弱い推奨、エビデンスレベルA）。不安が強い症例には抗不安薬を提案するが、依存性を考えて漫然とした使用は避ける。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 CQ3-14、CQ3-15
    differential: null
    common_misconception: IBSに抗うつ薬を使うのはうつ病を合併した場合だけ
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-094
  domain: NG
  subdomain: IBSの治療（日本のGL）
  assertion:
    plain_statement_ja: 日本のIBS診療ガイドライン2020は、IBSに心理療法を行うことを推奨している（強い推奨、エビデンスレベルB）。体系的な心理療法には、認知行動療法、リラクセーション、催眠療法、マインドフルネス、ストレスマネジメント、力動的精神療法があり、日常診療での傾聴・受容・支持・保証などの簡易精神療法も心理療法に含まれる。35のRCTを統合したメタ解析では、心理療法のNNTは4だった。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 CQ3-16
    differential: null
    common_misconception: IBSの心理療法は専門家しか行えない特別な治療だけを指す
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: NNTはGLが引用したメタ解析の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-095
  domain: NG
  subdomain: IBSの治療（日本のGL）
  assertion:
    plain_statement_ja: 日本のIBS診療ガイドライン2020は、一部の漢方薬をIBSに提案している（弱い推奨、エビデンスレベルC）。桂枝加芍薬湯の4週間の多施設RCT（232例）では、全般改善度（中等度以上の改善50.9%対プラセボ47.9%）に有意差はなかった。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 CQ3-17
    differential: null
    common_misconception: 漢方薬はIBSに確実な効果が証明されている
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: RCTの数値はGLが引用した値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-096
  domain: NG
  subdomain: IBSの治療（日本のGL）
  assertion:
    plain_statement_ja: 日本のIBS診療ガイドライン2020は、一部の非吸収性抗菌薬（主にリファキシミン）がIBSに有効として用いることを提案している（弱い推奨、エビデンスレベルA）が、日本ではリファキシミンにIBSの保険適用はない。ペパーミントオイルの使用も提案されている（弱い推奨、A）。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 CQ3-19、CQ3-20
    differential: 日本のリファキシミンの効能は肝性脳症の高アンモニア血症のみ（NG-047）
    common_misconception: ガイドラインで提案されていれば保険診療で使える
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-097
  domain: NG
  subdomain: IBSの治療（日本のGL）
  assertion:
    plain_statement_ja: 日本のIBS診療ガイドライン2020は、抗アレルギー薬をIBSに推奨している（強い推奨、エビデンスレベルA、合意率83%）。一方、IBSの腹痛に麻薬を使わないよう提案している（弱い推奨、C）。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 CQ3-18、CQ3-21
    differential: オピオイドは麻薬性腸症候群を起こしうる（NG-075）
    common_misconception: 強い腹痛のIBSにはオピオイドを使う
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 抗アレルギー薬の具体的な薬剤名と保険適用は本文で確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-098
  domain: NG
  subdomain: IBSの治療（日本のGL）
  assertion:
    plain_statement_ja: 日本のIBS診療ガイドライン2020は、IBSの症状をもつ人には自殺行為、炎症性腸疾患、認知症、パーキンソン病の発症リスクがあるとして、放置しないことを提案している（弱い推奨、エビデンスレベルC）。便移植は研究の途上にあり、今後の結果を待って判断するとしている。
    condition:
      region: 日本
      guideline: JSGE IBS診療GL 2020 CQ3-22、FRQ3-2
    differential: null
    common_misconception: IBSは命にかかわらないので放置してよい
  provenance:
    source_ref: SRC-134
    source: 日本消化器病学会編『機能性消化管疾患診療ガイドライン2020—過敏性腸症候群（IBS）（改訂第2版）』南江堂、2020
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化器病学会（非CC）。ユーザー提供のPDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-099
  domain: NG
  subdomain: 慢性便秘症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性便秘症の背景因子・発症リスクには、女性、身体活動の低下、精神疾患や神経疾患などの基礎疾患、腹部手術歴、一部の薬剤がある。加齢とともに有病率は増え、腸管平滑筋の収縮性や神経活動の低下、直腸知覚や便排出機能の低下、生活環境の変化が関わると考えられている。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性便秘症 BQ2-2、BQ3-4
    differential: null
    common_misconception: 便秘は若い女性だけの問題である
  provenance:
    source_ref: SRC-135
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 刊行版（第4刷）のBQ2-2（16頁）、BQ3-4（34頁）で文言・推奨度を照合済み（2026-10-18）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-100
  domain: NG
  subdomain: 慢性便秘症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性便秘症は生活の質を下げ、心血管疾患の発症・死亡リスクや、パーキンソン病・腎疾患の発症リスクの上昇に関わるため、長期予後に影響する可能性がある。一方、大腸癌の発生への関与は明らかでない。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性便秘症 BQ2-3、BQ2-4
    differential: null
    common_misconception: 便秘は大腸癌の確立した原因である
  provenance:
    source_ref: SRC-135
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 刊行版（第4刷）のBQ2-3（18頁）、BQ2-4（20頁）で文言・推奨度を照合済み（2026-10-18）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-101
  domain: NG
  subdomain: 慢性便秘症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性便秘症の警告症状・徴候には、排便習慣の急な変化、血便、6か月以内の予期しない3 kg以上の体重減少、発熱、関節痛、腹部腫瘤や直腸指診での腫瘤・血液付着などの異常な身体所見がある。二次性便秘の鑑別には、血液検査、大腸内視鏡、腹部X線・注腸X線の必要性を個別に判断する。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性便秘症 CQ4-1、BQ4-3
    differential: 大腸癌、炎症性腸疾患などの器質性便秘
    common_misconception: 便秘の患者には全例で大腸内視鏡が必要
  provenance:
    source_ref: SRC-135
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 刊行版（第4刷）のCQ4-1（55頁）、BQ4-3（53頁）で文言・推奨度を照合済み（2026-10-18）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-102
  domain: NG
  subdomain: 慢性便秘症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性便秘症の病態評価には、放射線不透過マーカー法による大腸通過時間の測定が推奨される（強い推奨、エビデンスレベルB）。体外式超音波検査やMRI/CTも提案されており（弱い推奨）、排便造影は他の機能検査と組み合わせて、直腸肛門内圧検査（バルーン排出検査を含む）とともに有用とされる。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性便秘症 CQ4-2〜4-4、BQ4-4、BQ4-5
    differential: 大腸通過時間測定のX線不透過マーカー検査は学会サイトにシェーマがある
    common_misconception: 便秘の病態は問診だけで分類できる
  provenance:
    source_ref: SRC-135
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 刊行版（第4刷）のCQ4-2（56頁）、CQ4-3（58頁、強い推奨・合意率74%・B）、CQ4-4（60頁）、BQ4-4（62頁）、BQ4-5（65頁）で文言・推奨度を照合済み（2026-10-18）。Rome V の腸疾患の章は、大腸通過時間検査を排便障害を除外した後の治療抵抗例で考慮するとしている（NG-141）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-103
  domain: NG
  subdomain: 慢性便秘症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性便秘症に浸透圧性下剤の投与が推奨されるが（強い推奨、エビデンスレベルA）、マグネシウムを含む塩類下剤を使うときは定期的に血清マグネシウムを測る。刺激性下剤は有効だが、耐性や習慣性を避けるため必要最小限とし、できるだけ頓用か短期間にとどめる。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性便秘症 CQ5-1、BQ5-5
    differential: null
    common_misconception: 酸化マグネシウムは長期に使っても検査は不要
  provenance:
    source_ref: SRC-135
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 刊行版（第4刷）のCQ5-1（77頁、強い推奨・合意率100%・A）、BQ5-5（81頁）で文言・推奨度を照合済み（2026-10-18）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-104
  domain: NG
  subdomain: 慢性便秘症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性便秘症に適応をもつ漢方薬は多いが、有効性を示す質の高い試験は少ない。大黄の成分はセンノシドが中心で、刺激性下剤に準じた副作用に注意する。大建中湯は腹部膨満などに適応があり経験的に使われるが、慢性便秘症そのものへの適応はない。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性便秘症 BQ5-7
    differential: null
    common_misconception: 漢方薬なら長期使用しても副作用はない
  provenance:
    source_ref: SRC-135
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 刊行版（第4刷）のBQ5-7（95頁）で文言・推奨度を照合済み（2026-10-18）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-105
  domain: NG
  subdomain: 慢性便秘症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: オピオイド誘発性便秘症には、浸透圧性下剤、刺激性下剤、ナルデメジン、ルビプロストンが有効とされ、安全性、費用、使っているオピオイドの種類も考えて選ぶ。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性便秘症 CQ5-4
    differential: ナルデメジンの添付文書情報（NG-046）
    common_misconception: オピオイド誘発性便秘には通常の下剤は効かない
  provenance:
    source_ref: SRC-135
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 刊行版（第4刷）のCQ5-4（101頁、推奨なし・C）で文言・推奨度を照合済み（2026-10-18）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-106
  domain: NG
  subdomain: 慢性便秘症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 骨盤底筋の協調運動障害による慢性便秘症にはバイオフィードバック療法が有効だが、専門性が高いため専門施設での治療が勧められる。保存的治療で改善しない大腸通過遅延型便秘には、基準を満たせば結腸切除術が有効であり、術前に胃排出障害と直腸の排便機能障害を評価することが重要とされる。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性便秘症 BQ5-10、BQ5-12、CQ5-5
    differential: null
    common_misconception: 難治性便秘には全例で結腸切除を行う
  provenance:
    source_ref: SRC-135
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 刊行版（第4刷）のBQ5-10（105頁）、BQ5-12（108頁）、CQ5-5（112頁、強い推奨・合意率73%・B）で文言・推奨度を照合済み（2026-10-18）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-107
  domain: NG
  subdomain: 慢性便秘症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 難治性慢性便秘症に正式な定義はないが、病態生理にもとづく適切な治療を行っても十分に改善しない慢性便秘症とするのが現時点の標準的な考え方である。病態に応じた治療を行うことが推奨される（強い推奨）。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性便秘症 FRQ1-1、CQ5-6
    differential: null
    common_misconception: 難治性便秘とは下剤が効かない便秘のことである
  provenance:
    source_ref: SRC-135
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 刊行版（第4刷）のFRQ1-1（10頁）、CQ5-6（114頁、強い推奨・合意率73%・B）で文言・推奨度を照合済み（2026-10-18）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-108
  domain: NG
  subdomain: 慢性便秘症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性便秘症の患者の多くはうつや不安のスコアが健康な人より高く、心理的異常が病態に関わると考えられている。慢性便秘症には機能性ディスペプシアやGERDが合併することがあり、腸内細菌も病態に関わる。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性便秘症 BQ3-6、CQ3-3、CQ3-4
    differential: null
    common_misconception: 便秘は大腸だけの問題である
  provenance:
    source_ref: SRC-135
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性便秘症』南江堂、2023（第1刷 2023年7月13日、第4刷 2024年8月25日）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDF（第4刷、ISBN 978-4-524-21005-3）で照合
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 刊行版（第4刷）のBQ3-6（39頁）、CQ3-3（41頁）、CQ3-4（46頁）で文言・推奨度を照合済み（2026-10-18）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-109
  domain: NG
  subdomain: 消化管機能検査
  assertion:
    plain_statement_ja: EndoFLIP（functional lumen imaging probe）は、カテーテルのバルーン内でインピーダンス平面計測法により断面積を、センサーで内圧を測り、食道胃接合部の伸展性（mm²/mmHg）を求める検査で、アカラシアの治療前後の評価や筋層切開術・噴門形成術の術中評価に使われる。40 mL充満時の伸展性は、未治療のアカラシアで1.6 mm²/mmHg以下、治療後で3.4 mm²/mmHg以上と報告されている。
    condition:
      source: Chen & Rubenstein 2017
    differential: 高解像度食道内圧検査（Chicago分類、ES-025〜031）
    common_misconception: EndoFLIPの数値は確立した診断基準値である
  provenance:
    source_ref: SRC-136
    source: Chen JW, Rubenstein JH. Esophagogastric junction distensibility assessed using the functional lumen imaging probe. World J Gastroenterol 2017;23:1289-1297
    doi: 10.3748/wjg.v23.i7.1289
    pmid: '28275309'
    pmcid: null
    url: https://wjgnet.com/1007-9327/full/v23/i7/1289.htm
    source_license: CC BY-NC 4.0（記事ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 総説が引用した値（二次資料経由）。総説自身が、検証された診断閾値ではないとしている
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-110
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome V（腸脳相関障害の第5版）は2026年に公表され、27か国の140人を超える専門家が作成に加わった。基準の要約はGastroenterology 2026年第170巻に18本の論文として掲載された。
    condition:
      criteria: Rome V（2026）
    differential: Rome IVは2016年に公表された（NG-002・NG-037）
    common_misconception: Rome IVが現在も最新の国際基準である
  provenance:
    source_ref: SRC-137
    source: 'Rome Foundation『Rome V: A Global Framework for Disorders of Gut–Brain Interaction』（製品・概要ページ）'
    doi: null
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/rome-v-a-global-framework-for-disorders-of-gut-brain-interaction/
    source_license: © 2026 Rome Foundation. All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出版日（2026年6月1日の出荷）は Rome Foundation の製品ページの記載
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-111
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vの編集は、共同上級編集者のDouglas A. DrossmanとJan Tackが務め、第1巻に8、第2巻に11の章委員会が置かれた。成人用教科書2巻のほか、小児版、プライマリケア版、質問票・表の巻、診断アルゴリズム、多次元臨床プロファイル（MDCP）が刊行物として用意されている。
    condition:
      criteria: Rome V（2026）
    differential: null
    common_misconception: Rome基準は診断基準の表だけで構成される
  provenance:
    source_ref: SRC-138
    source: Rome Foundation『Rome V, Disorders of Gut-Brain Interaction 5th Edition』（編集体制のページ）
    doi: null
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/rome-iv/rome-v-disorders-of-gut-brain-interaction-5th-edition/
    source_license: © 2026 Rome Foundation. All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-112
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Gastroenterology誌に掲載されたRome Vの18本の論文には、各疾患群の章に加えて、基礎科学、生理学と臨床、腸内微小環境、薬理学、患者体験・性・年齢・人種と健康の社会的決定要因、社会文化的側面、成人と小児の生物心理社会的側面、治療試験のデザイン、診断質問票の開発が含まれる。
    condition:
      criteria: Rome V（2026）
    differential: Rome IVの章構成（NG-037）
    common_misconception: Rome Vは診断基準の変更だけを扱う
  provenance:
    source_ref: SRC-139
    source: Rome Foundation『Rome V Journal Articles』（Gastroenterology 2026;170 掲載論文の一覧）
    doi: null
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/rome-v-a-global-framework-for-disorders-of-gut-brain-interaction/rome-v-journal-articles/
    source_license: © 2026 Rome Foundation. All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-113
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vは「機能性（functional）」という用語をできるだけ使わず、病態生理に即した表現に改めたが、機能性下痢、機能性胸痛、機能性胸やけでは用語が残された。
    condition:
      criteria: Rome V（2026）
    differential: null
    common_misconception: Rome Vでは「機能性」という語が完全に廃止された
  provenance:
    source_ref: SRC-137
    source: 'Rome Foundation『Rome V: A Global Framework for Disorders of Gut–Brain Interaction』（製品・概要ページ）'
    doi: null
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/rome-v-a-global-framework-for-disorders-of-gut-brain-interaction/
    source_license: © 2026 Rome Foundation. All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 腸疾患の章では機能性腹部膨満の名称も残っている（NG-126）。
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-114
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vは、定められた閾値と標準化された評価項目を用いる研究用の基準と、症状の煩わしさ（bothersomeness）や生活機能への影響を取り入れ、臨床判断に応じて柔軟に使える臨床用の基準を、正式に分けた。
    condition:
      criteria: Rome V（2026）
    differential: Rome IVの基準は症状の持続期間（3か月、発症6か月以上前）を一律に求めた（NG-058）
    common_misconception: Rome Vの臨床用基準も研究用と同じ期間要件を満たす必要がある
  provenance:
    source_ref: SRC-137
    source: 'Rome Foundation『Rome V: A Global Framework for Disorders of Gut–Brain Interaction』（製品・概要ページ）'
    doi: null
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/rome-v-a-global-framework-for-disorders-of-gut-brain-interaction/
    source_license: © 2026 Rome Foundation. All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 臨床用基準の具体的な要件（6か月は不要、他疾患の除外のため8週間の経過を推奨、頻度は低くてよい）は序論（NG-234）で確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-115
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vでは、IBSの診断要件に腹痛に加えて「腹部不快感」が再び含められ、症状の頻度の閾値がRome IVの週1日以上から月3日以上に下げられた。
    condition:
      criteria: Rome V（2026）
    differential: Rome IVのIBS基準（NG-070）
    common_misconception: Rome VでもIBSは週1日以上の腹痛が必要である
  provenance:
    source_ref: SRC-137
    source: 'Rome Foundation『Rome V: A Global Framework for Disorders of Gut–Brain Interaction』（製品・概要ページ）'
    doi: null
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/rome-v-a-global-framework-for-disorders-of-gut-brain-interaction/
    source_license: © 2026 Rome Foundation. All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 腸疾患の章（NG-127）で、持続痛の除外と、月経だけに限らないという補助基準を確認した
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-116
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vで新たに取り上げられた疾患には、げっぷができない症候群（逆行性輪状咽頭筋機能不全、R-CPD）、成人の腹部片頭痛、直腸肛門の感覚機能障害がある。
    condition:
      criteria: Rome V（2026）
    differential: Rome IVでは腹部片頭痛は小児の疾患だった（NG-083）
    common_misconception: 腹部片頭痛は小児だけの病気である
  provenance:
    source_ref: SRC-137
    source: 'Rome Foundation『Rome V: A Global Framework for Disorders of Gut–Brain Interaction』（製品・概要ページ）'
    doi: null
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/rome-v-a-global-framework-for-disorders-of-gut-brain-interaction/
    source_license: © 2026 Rome Foundation. All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 麻薬性腸症候群はRome IVですでに取り上げられており（NG-003、NG-075）、Rome Vの新規疾患ではない。腹部片頭痛（NG-154）と直腸肛門の感覚機能障害（NG-164）は原典で確認。げっぷができない症候群は胃十二指腸の章（NG-209）で新設の疾患として確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-117
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vの小児の基準は、年齢区分（新生児・乳幼児、小児・思春期）ではなく、解剖学的領域（上部消化管と、下部消化管・胆道）によって再編された。各章には、食事療法や行動療法を含む多職種のケアが組み込まれている。
    condition:
      criteria: Rome V（2026）
    differential: Rome IVの小児の2群（NG-002）
    common_misconception: Rome Vでも小児は年齢で分類される
  provenance:
    source_ref: SRC-137
    source: 'Rome Foundation『Rome V: A Global Framework for Disorders of Gut–Brain Interaction』（製品・概要ページ）'
    doi: null
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/rome-v-a-global-framework-for-disorders-of-gut-brain-interaction/
    source_license: © 2026 Rome Foundation. All rights reserved
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-118
  domain: NG
  subdomain: Rome V 小児上部消化管
  assertion:
    plain_statement_ja: Rome Vの小児上部消化管の腸脳相関障害は、G1 食道疾患（逆流過敏症、逆流陰性食道痛障害、食道の空気通過障害［空気嚥下症候群、胃上部げっぷ症候群］）、G2 機能性小児摂食障害（過敏性嚥下障害、予期性制限摂食、空腹調節障害［空腹感の低下・過剰］、医療に誘発された機能性摂食障害）、G3 胃十二指腸疾患（反芻症候群、周期性嘔吐症候群［カンナビノイド悪阻の亜群を含む］、慢性悪心症候群、機能性ディスペプシア［PDS、EPS］）に分けられる。
    condition:
      criteria: Rome V（2026）
    differential: null
    common_misconception: 小児の上部消化管症状は乳児逆流症と機能性ディスペプシアだけで分類できる
  provenance:
    source_ref: SRC-140
    source: Rosen R, et al. Rome V Pediatric Upper Gastrointestinal Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1347-1366
    doi: 10.1053/j.gastro.2026.01.039
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/2026/09/Rome-V-Pediatric-Upper-Gastrointestinal-Disorders-.pdf
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）。ユーザー提供の原本で確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)；TBL-02-07-025 (id: JlAKpkw)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-119
  domain: NG
  subdomain: Rome V 小児上部消化管
  assertion:
    plain_statement_ja: Rome Vの小児の基準では、嘔吐を定義から外した「慢性悪心症候群」という用語が使われる。逆流陰性食道痛障害は、成人の機能性胸やけに相当するものとされる。
    condition:
      criteria: Rome V（2026）
    differential: 成人の慢性悪心嘔吐症候群（NG-065）
    common_misconception: 小児の悪心は嘔吐を伴わなければ診断名がつかない
  provenance:
    source_ref: SRC-140
    source: Rosen R, et al. Rome V Pediatric Upper Gastrointestinal Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1347-1366
    doi: 10.1053/j.gastro.2026.01.039
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/2026/09/Rome-V-Pediatric-Upper-Gastrointestinal-Disorders-.pdf
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）。ユーザー提供の原本で確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)；TBL-02-07-025 (id: JlAKpkw)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-120
  domain: NG
  subdomain: Rome V 小児上部消化管
  assertion:
    plain_statement_ja: Rome Vの小児上部消化管の章は、回避・制限性食物摂取症（ARFID）という用語を廃止し、より正確な用語（機能性小児摂食障害の各亜型）に置き換えることを提案している。摂食障害の基準は週3回以上、1か月以上の持続を求める。
    condition:
      criteria: Rome V（2026）
    differential: null
    common_misconception: 小児の摂食の問題はすべてARFIDと診断する
  provenance:
    source_ref: SRC-140
    source: Rosen R, et al. Rome V Pediatric Upper Gastrointestinal Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1347-1366
    doi: 10.1053/j.gastro.2026.01.039
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/2026/09/Rome-V-Pediatric-Upper-Gastrointestinal-Disorders-.pdf
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）。ユーザー提供の原本で確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ARFIDの廃止は小児消化器の立場からの提案であり、精神医学の診断分類（DSM-5）との関係は原典で確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-121
  domain: NG
  subdomain: Rome V 小児上部消化管
  assertion:
    plain_statement_ja: Rome Vの小児の食後愁訴症候群は、症状の頻度が週1回から週3回以上に引き上げられ、食後の症状を食事から2時間以内に起こるものと定義した。心窩部痛症候群は週1日以上を求める。逆流過敏症、逆流陰性食道痛障害、反芻症候群、周期性嘔吐症候群は、症状が2か月以上続くことを求める。
    condition:
      criteria: Rome V（2026）
    differential: Rome IVの成人のPDSは週3日以上（NG-064）
    common_misconception: 小児の機能性ディスペプシアの基準はRome IVから変わっていない
  provenance:
    source_ref: SRC-140
    source: Rosen R, et al. Rome V Pediatric Upper Gastrointestinal Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1347-1366
    doi: 10.1053/j.gastro.2026.01.039
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/2026/09/Rome-V-Pediatric-Upper-Gastrointestinal-Disorders-.pdf
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）。ユーザー提供の原本で確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 成人の機能性ディスペプシアの変更（PDSは週2日以上、食後は2時間以内、食事関連の心窩部痛はPDSに含める）は胃十二指腸の章（NG-199）で確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-122
  domain: NG
  subdomain: Rome V 小児上部消化管
  assertion:
    plain_statement_ja: Rome Vの小児の反芻症候群の基準は年齢を問わず統一され、生後3か月以降の発症を求める。カンナビノイド悪阻の亜群では、大麻を6か月以上継続して中止した後に嘔吐が消えることを求める。空気嚥下症候群では、放屁の増加が主要基準から補助的な所見に変わった。
    condition:
      criteria: Rome V（2026）
    differential: Rome IVのカンナビノイド悪阻症候群（NG-067）
    common_misconception: 大麻の中止後すぐに嘔吐が消えなければカンナビノイド悪阻は否定できる
  provenance:
    source_ref: SRC-140
    source: Rosen R, et al. Rome V Pediatric Upper Gastrointestinal Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1347-1366
    doi: 10.1053/j.gastro.2026.01.039
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/2026/09/Rome-V-Pediatric-Upper-Gastrointestinal-Disorders-.pdf
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）。ユーザー提供の原本で確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-123
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: 英国のIBS登録（ContactME-IBS）の1,275人にRome III・IV・Vの基準を後から当てはめた研究では、基準を満たした割合はRome V 70%、Rome IV 59%、Rome III 78%だった。Rome Vを満たす人は、Rome IVだけを満たす人より軽症で（IBS-SSS平均252.6対385.0）、生活の質も高かった。
    condition:
      criteria: Rome V（2026）
      source: Staller ら 2026
    differential: null
    common_misconception: Rome Vで診断されるIBSはRome IVと同じ重症度の集団である
  provenance:
    source_ref: SRC-141
    source: Staller K, et al. Clin Gastroenterol Hepatol 2026（ContactME-IBS 登録データによる Rome III・IV・V の比較）
    doi: 10.1016/j.cgh.2026.07.022
    pmid: null
    pmcid: null
    url: https://news.gastro.org/issues/2026/august-2026/rome-v-criteria-capture-more-people-with-ibs-but-a-milder-group/
    source_license: 原著は未取得。AGA の GI & Hepatology News（2026-08-20）の記事で内容を確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 原著は未取得で、AGAのニュース記事（二次資料経由）で確認。Rome Vは持続痛の除外を明記したとされる。Rome V の基準そのものは腸疾患の章（NG-127）で確認済み
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-124
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome V の改訂を概説した総説によれば、機能性食道疾患の診断にはLyon Consensus 2.0とChicago Classification v4.0が不可欠とされ、機能性嚥下障害では機能的内腔画像（インピーダンス平面計測）が診断の特異度を高めるとされた。逆行性輪状咽頭筋機能不全（R-CPD）は、独自の診断・治療基準をもつ独立した疾患として認められた。
    condition:
      criteria: Rome V（2026）
      source: 総説（Maev ら 2026）
    differential: Rome IVの機能性食道疾患（NG-058〜063）、EndoFLIP（NG-109）
    common_misconception: 機能性食道疾患は症状だけで診断できる
  provenance:
    source_ref: SRC-142
    source: 'Maev IV, et al. Rome V Criteria (2026): Continuity, innovations and major updates. Meditsinskiy sovet 2026;(8):8-21'
    doi: 10.21518/ms2026-232
    pmid: null
    pmcid: null
    url: https://www.med-sovet.pro/jour/article/view/10201?locale=en_US
    source_license: CC（記事ページの表示が BY-NC-ND と BY 4.0 で不一致。抄録のみ参照）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 総説の抄録による（二次資料経由）。内容は食道の章（NG-186）で確認済み。本カードは corroboration として扱う
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-125
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome V の改訂を概説した総説によれば、IBSでは腹部不快感が再び導入され、症状の間欠性（持続痛でないこと）が求められるようになった。診断の感度を回復させつつ、機序の特異性を高めることが狙いとされる。
    condition:
      criteria: Rome V（2026）
      source: 総説（Maev ら 2026）
    differential: null
    common_misconception: Rome VのIBSでは持続する腹痛も含まれる
  provenance:
    source_ref: SRC-142
    source: 'Maev IV, et al. Rome V Criteria (2026): Continuity, innovations and major updates. Meditsinskiy sovet 2026;(8):8-21'
    doi: 10.21518/ms2026-232
    pmid: null
    pmcid: null
    url: https://www.med-sovet.pro/jour/article/view/10201?locale=en_US
    source_license: CC（記事ページの表示が BY-NC-ND と BY 4.0 で不一致。抄録のみ参照）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 総説の抄録による（二次資料経由）。内容は腸疾患の章（NG-127）で確認済み。本カードは corroboration として扱う
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-17'
    verifier: null
    verified_at: null
    status: draft
- id: NG-126
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vは腸疾患を、IBS、慢性便秘症、機能性下痢、機能性腹部膨満、分類不能の腸疾患、オピオイド誘発性便秘症の6つに分ける。Rome IVの機能性便秘は「慢性便秘症」に、特定不能の機能性腸疾患は「分類不能の腸疾患」に改められ、「機能性」という語を外す流れを反映している。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: Rome IVの機能性腸疾患（NG-069）
    common_misconception: Rome Vでも機能性便秘という診断名が使われる
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-127
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome VのIBSは、持続性ではない腹痛または腹部不快感が最近3か月に平均月3日以上繰り返し、排便との関連、排便頻度の変化、便形状の変化のうち2つ以上を伴うものと定義される。症状は診断の6か月以上前に始まっている必要がある。補助基準として、症状が月経の時期だけに限られないことが求められる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: Rome IVのIBS（週1日以上の腹痛、NG-070）、中枢介在性腹痛症候群（持続痛）、月経に伴う症状
    common_misconception: Rome VのIBSも週1日以上の腹痛を必要とする
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: NG-115（Rome Foundation の概要）、NG-125（総説）と同じ内容を原典で確認
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-128
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome IVでIBSの有病率が下がった主な理由は、腹痛の頻度の閾値をRome IIIの月2〜3日から週1日以上に引き上げたことで、「不快感」を外したことの影響はそれより小さかった。痛みがなく不快感だけのIBS患者が一部の国で報告されていたため、Rome Vは不快感を戻し、閾値を月3日以上に下げた。持続しない痛みという条件は中枢介在性腹痛症候群と、月経だけに限らないという条件は月経関連症状と区別するために加えられた。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: Rome IVで有病率が下がったのは主に不快感を外したためである
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 有病率低下の理由はRome Foundation Global Studyの解析による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-129
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome VのIBSの病型（便秘型、下痢型、混合型、分類不能型）は、少なくとも1回の異常な排便があった日のブリストル便形状スケールで、25%の基準によって決める。病型を確信をもって決めるには、異常な排便の日が月4日以上あることが望ましく、便通異常の治療薬を使っていない状態で評価する。臨床試験では2週間以上の毎日の排便日誌が推奨される。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: IBSの病型は下剤を飲んでいる間の便の状態で決めてよい
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-130
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vは、IBSを除外診断ではなく症状にもとづく積極的な診断として行うよう求めている。基準を満たし警告症状がなければ検査は選択的・限定的にとどめる。診断は簡潔な言葉で確信をもって伝え、腸脳相関の障害として説明することで、患者の理解と受容が深まるとしている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: IBSはあらゆる器質的疾患を検査で否定してから診断する
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-131
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vの腸疾患の章が引用したメタ解析では、CRP 0.5 mg/dL未満なら炎症性腸疾患の確率は1%未満で、便中カルプロテクチン50 μg/g以下はIBSと炎症性腸疾患の区別で陰性的中率99.8%、陽性的中率9%だった。便中カルプロテクチンは高齢、肥満、感染、PPIやNSAIDsの使用でも上がることがある。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: 便中カルプロテクチンが上がっていれば炎症性腸疾患と診断できる
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 数値は章が引用したメタ解析による（二次資料経由）。添付のまとめにあった「<100・100〜250・≥250」の区分は、腸疾患の章には記載がない
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-132
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vの腸疾患委員会は、IBSの初期評価として、小腸細菌異常増殖の呼気試験、便中エラスターゼ、スクラーゼ・イソマルターゼ欠損の検査を日常的には勧めていない。セリアック病は、IBSの3.3%で生検により確認されたとするメタ解析があり、多くのガイドラインがIgA抗組織トランスグルタミナーゼ抗体と血清IgAの測定を勧めている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: IBSの患者には全例で小腸細菌異常増殖の呼気試験を行う
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: セリアック病の頻度は章が引用したメタ解析による（二次資料経由）。日本での頻度は別に確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-133
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: 警告症状のない便秘型以外のIBSでは、大腸内視鏡の診断的な収穫は約2%で、多くは45歳を超える女性の顕微鏡的大腸炎だった。下痢型IBSが疑われて大腸内視鏡を行うときは、顕微鏡的大腸炎を除外するための生検を考える。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: IBSの大腸内視鏡では生検は不要である
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 章が引用した単一研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-022 (id: JlAKpkc)；TBL-02-07-031 (id: JlAKplI)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-134
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: IBSの発症や増悪の引き金には、感染性胃腸炎、食事、心理的要因、慢性ストレス、手術がある。急性胃腸炎の後に10%を超える人が感染後IBSを発症し、小児期または成人期の虐待歴はIBSの危険を約3倍に高める。下痢型IBSの約25%に胆汁酸吸収不良があると推定されている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: IBSは心理的な原因だけで起こる
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 数値は章が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-135
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: IBSの食事療法では、可溶性食物繊維（サイリウム）に有益性が示され（相対リスク0.83、治療必要数7）、不溶性の小麦ふすまには示されなかった。ネットワークメタ解析では低FODMAP食の根拠が最も強かった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: IBSにはどの食物繊維でも同じ効果がある
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 章が引用したメタ解析の値（二次資料経由）。低FODMAP食の3段階は小児の章に記載がある（NG-219）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-136
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: IBSに使う中枢性神経調節薬では三環系抗うつ薬が最も研究されており、ATLANTIS試験では低用量アミトリプチリン（就寝前10〜30 mg）が6か月にわたり全般症状を改善した。SSRIは腹痛への効果が示されていないが、不安や抑うつを合併する患者には有用なことがある。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: 日本のIBS診療ガイドライン2020（NG-093）
    common_misconception: SSRIはIBSの腹痛に三環系抗うつ薬と同じように効く
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-137
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: 8件の臨床試験のメタ解析では、糞便微生物移植（FMT）は12週の時点でIBSの全般症状を有意に改善せず、根拠の質は非常に低かった。現在のガイドラインは、臨床試験以外でIBSにFMTを使わないよう勧めている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: FMTの安全性（NG-054、NG-055）
    common_misconception: IBSにはFMTが確立した治療である
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-138
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: 脳腸行動療法（認知行動療法、腸指向性催眠療法、マインドフルネス、曝露療法など）のうち、IBSで有効性の根拠が最も多いのは、自己実施型や接触の少ない認知行動療法、対面の認知行動療法、腸指向性催眠療法である。ただし試験はいずれも偏りの危険が高い。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: 日本のIBS診療ガイドライン2020（NG-094）
    common_misconception: IBSの心理療法には根拠がない
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-139
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vの慢性便秘症は、いきみ、硬便・兎糞状便（ブリストル1〜2）、残便感、直腸肛門の閉塞感、用手的な排便補助のそれぞれが排便の25%を超えること、または自発排便が週3回未満であることのうち2つ以上を満たし、下剤なしでは軟便がまれで、IBSの基準を満たさないものと定義される。IBS-Cとの違いは、腹痛や不快感が主症状かどうかにある。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: 便秘型IBS、オピオイド誘発性便秘症、日本の慢性便秘症の診断基準（NG-099〜108）
    common_misconception: 慢性便秘症の患者には腹痛がまったくない
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-140
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Foundation Global Studyのインターネット調査では、機能性便秘の有病率は全体で11.7%、オーストラリアの7.7%から日本の16.6%までの幅があり、IBSより多かった。便秘の多くは時間とともに軽快し、12か月後も同じ状態にとどまるのは約3分の1とする研究がある。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: 日本の便秘の有病率は世界で最も低い
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: NG-010（日本16.6%）と同じ調査
  uncertainty: 章が引用した調査の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-141
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vの腸疾患委員会は、直腸肛門機能検査を初期評価ではなく治療に反応しない患者に行うよう勧めている（直腸指診で排便障害が強く疑われるときは早めに行う）。大腸通過時間検査は、排便障害を除外した後、治療を続けても症状が残る患者で考慮する。警告症状がなければ画像検査は一般に勧めない。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: 日本の便通異常症GL2023は放射線不透過マーカー法を推奨している（NG-102）
    common_misconception: 慢性便秘症では最初に大腸通過時間検査を行う
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-142
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vの腸疾患の章は、慢性便秘症に1日20〜30 gの食物繊維を勧め、浸透圧性下剤ではポリエチレングリコールが最もよく研究されているとする。刺激性下剤については、習慣性や大腸の構造的・機能的障害を起こすという根拠はないとしている。エロビキシバットは日本で慢性便秘症に承認されていると記載している。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: 日本の便通異常症GL2023は刺激性下剤を必要最小限・頓用にとどめるとしている（NG-103）
    common_misconception: 刺激性下剤は必ず大腸を傷める
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-143
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vの機能性下痢は、排便の25%を超える軟便・水様便があり、便秘を起こす薬を使わなければ硬便がまれで、下痢型IBSの基準を満たさないものと定義される。硬便に関する条件は、慢性便秘症の基準と揃えるために新たに加えられた。有病率はRome IV基準で4.7%とされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: Rome IVの機能性下痢（NG-071）、日本の慢性下痢症（狭義）
    common_misconception: 機能性下痢と下痢型IBSは腹痛の有無に関係なく同じ診断である
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-144
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: 機能性下痢では、腹痛が主でないため神経調節薬は初期治療にしない。マグネシウムやPPIなど下痢の原因になる薬を見直す。ロペラミドは1回2〜4 mg、1日4回まで検査なしで日常的に使える。胆汁酸吸収不良の検査ができなければ、胆汁酸吸着薬を4週間以上試すのは妥当とされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: 機能性下痢の第一選択は抗うつ薬である
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-145
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vの機能性腹部膨満は、腹部膨満感や目に見える腹部膨隆が平均週1日以上あって他の症状より目立ち、IBS、慢性便秘症、機能性下痢、食後愁訴症候群の基準を満たさないものである。軽い痛みや軽い便通異常があってもよい。有病率は3.5%とされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: Rome IVの機能性腹部膨満（NG-072）
    common_misconception: 腹部膨満は必ずガスがたまって起こる
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-024 (id: JlAKpko)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-146
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: 多くの腸脳相関障害の患者は、健康な人より腸内のガスが多いわけではない。目に見える腹部膨隆の機序の一つは腹壁横隔膜協調障害で、腸管が張ると横隔膜が異常に収縮し腹壁筋が緩む。食事で誘発される腹部膨隆の患者42人の無作為化試験では、胸腹壁運動を指標にしたバイオフィードバックで膨隆が改善した。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: 腹部膨満の患者は腸内ガスが多い
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 無作為化試験の値は章が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-024 (id: JlAKpko)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-147
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vの分類不能の腸疾患は、構造異常では説明できない煩わしい腸症状があるが、IBS、慢性便秘症、機能性下痢、機能性腹部膨満の基準を完全には満たさないものである。三次施設の研究では腸疾患の13.1%がこれに当たり、1年後も同じ診断だったのは40%で、残りは主にIBSに移行した。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: null
    common_misconception: 分類不能の腸疾患は軽症なので治療は要らない
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 頻度は章が引用した単一施設の研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-148
  domain: NG
  subdomain: Rome V 腸疾患
  assertion:
    plain_statement_ja: Rome Vのオピオイド誘発性便秘症は、オピオイドの開始・変更・増量時に新たに生じるか悪化した便秘症状で、慢性便秘症と同じ6項目のうち2つ以上を満たし、下剤なしでは軟便がまれなものである。Rome Foundation Global Studyの有病率はインターネット調査で1.6%、世帯調査で0.9%だった。治療は慢性便秘症に準じ、末梢性μオピオイド受容体拮抗薬が加わる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 腸疾患の章
    differential: Rome IVのオピオイド誘発性便秘（NG-073）、麻薬性腸症候群
    common_misconception: オピオイド誘発性便秘症とオピオイドによる腹痛の増悪は同じ病態である
  provenance:
    source_ref: SRC-143
    source: Corsetti M, Shin A, Lacy BE, et al. Bowel Disorders. Gastroenterology 2026;170:1261-1282（Rome V）
    doi: 10.1053/j.gastro.2026.02.003
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.003
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-149
  domain: NG
  subdomain: Rome V 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: Rome Vは中枢介在性の消化管の痛みとして、中枢介在性腹痛症候群（CAPS）、成人の腹部片頭痛、麻薬性腸症候群（オピオイド誘発性消化管痛覚過敏）の3つを定めている。成人の腹部片頭痛はRome Vで新たに加えられた。
    condition:
      criteria: Rome V（2026）
      source: Rome V 中枢介在性の消化管の痛みの章
    differential: Rome IVの中枢介在性の痛み（NG-074、NG-075）
    common_misconception: 腹部片頭痛は小児にしかない
  provenance:
    source_ref: SRC-144
    source: Fukudo S, Aziz Q, Drossman DA, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2026;170:1283-1302（Rome V）
    doi: 10.1053/j.gastro.2025.12.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2025.12.038
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-150
  domain: NG
  subdomain: Rome V 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: Rome VのCAPSは、持続する腹痛、生理的な出来事との関係（カテゴリーA：関係なし、カテゴリーB：食事・排便・月経・体位などと様々な程度に関係する）、日常生活の一部が痛みで制限されること、作為的でないこと、他の疾患で説明できないことのすべてを満たす。Rome IVの「ほぼ持続的」から「ほぼ」が削られ、持続痛は覚醒時の痛みを指す。
    condition:
      criteria: Rome V（2026）
      source: Rome V 中枢介在性の消化管の痛みの章
    differential: Rome IVのCAPS（NG-074）、IBS（間欠的な痛み）
    common_misconception: 食事や排便で痛みが変わればCAPSではない
  provenance:
    source_ref: SRC-144
    source: Fukudo S, Aziz Q, Drossman DA, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2026;170:1283-1302（Rome V）
    doi: 10.1053/j.gastro.2025.12.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2025.12.038
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-151
  domain: NG
  subdomain: Rome V 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: Rome IV基準のCAPSは、Rome Foundation Global Studyのインターネット調査で0.02%しか見つからず、基準が厳しすぎると判断された。生理的な出来事と関係する持続痛を含めたカテゴリーBの頻度は0.11%で、カテゴリーAの約5倍だった。両者はほぼすべての変数で似ており、専門外来に紹介される腸脳相関障害の患者では、慢性腹痛が最大約20%を占める。
    condition:
      criteria: Rome V（2026）
      source: Rome V 中枢介在性の消化管の痛みの章
    differential: null
    common_misconception: CAPSは極めてまれなので専門外来でも出会わない
  provenance:
    source_ref: SRC-144
    source: Fukudo S, Aziz Q, Drossman DA, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2026;170:1283-1302（Rome V）
    doi: 10.1053/j.gastro.2025.12.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2025.12.038
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 専門外来の割合は章が引用した報告による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-152
  domain: NG
  subdomain: Rome V 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: CAPSの患者には、痛みの訴えがあっても頻脈・血圧上昇・発汗などの自律神経反応が目立たない、適応がはっきりしない複数の手術痕がある、触診時に目を閉じて顔をしかめる（閉眼徴候）、聴診器で腹部を押すと手で押したときより痛みの反応が弱まる（聴診器徴候）といった特徴がみられる。腹壁痛との区別にはCarnett試験が役立ち、診察には直腸指診と会陰の視診を含める。
    condition:
      criteria: Rome V（2026）
      source: Rome V 中枢介在性の消化管の痛みの章
    differential: 腹壁痛（前皮神経絞扼症候群）、慢性腸間膜虚血、正中弓状靱帯症候群
    common_misconception: 閉眼徴候があれば器質的疾患は否定できる
  provenance:
    source_ref: SRC-144
    source: Fukudo S, Aziz Q, Drossman DA, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2026;170:1283-1302（Rome V）
    doi: 10.1053/j.gastro.2025.12.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2025.12.038
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: これらの所見は診断基準には含まれない
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-153
  domain: NG
  subdomain: Rome V 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: CAPSでは麻薬性鎮痛薬を避ける。第一選択は三環系抗うつ薬で、抗コリン作用の少ない二級アミン（デシプラミン、ノルトリプチリン）が好まれる。SNRI（デュロキセチン30〜60 mg/日など）も第一選択になりうる。SSRI単独は痛みには役立たないことが多い。低用量クエチアピン（25〜100 mg）は増強薬として使われる。カテゴリーAは中枢性の神経調節薬、カテゴリーBは末梢に作用する薬にも反応しうると考えられている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 中枢介在性の消化管の痛みの章
    differential: Rome IVの中枢介在性の痛みの治療（NG-076）
    common_misconception: CAPSの強い腹痛にはオピオイドを使う
  provenance:
    source_ref: SRC-144
    source: Fukudo S, Aziz Q, Drossman DA, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2026;170:1283-1302（Rome V）
    doi: 10.1053/j.gastro.2025.12.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2025.12.038
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-154
  domain: NG
  subdomain: Rome V 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: Rome Vの成人の腹部片頭痛は、1時間以上数日まで続く型どおりの激しい腹痛発作が数週から数か月の間隔で年3回以上（最近6か月で2回以上）起こり、日常生活ができなくなり、片頭痛の既往、片頭痛の家族歴、食欲不振・悪心・嘔吐、光過敏、顔面蒼白、前兆のうち2つ以上を伴うものである。痛みが主で嘔吐が繰り返さない点で周期性嘔吐症候群と区別する。
    condition:
      criteria: Rome V（2026）
      source: Rome V 中枢介在性の消化管の痛みの章
    differential: 小児の腹部片頭痛（NG-083）、周期性嘔吐症候群（NG-066）、IBS
    common_misconception: 腹部片頭痛は小児だけの病気で、成人では診断しない
  provenance:
    source_ref: SRC-144
    source: Fukudo S, Aziz Q, Drossman DA, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2026;170:1283-1302（Rome V）
    doi: 10.1053/j.gastro.2025.12.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2025.12.038
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-155
  domain: NG
  subdomain: Rome V 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: 成人の腹部片頭痛の発作は2〜72時間、平均約17時間続き、痛みは食事や排便と関係しない。患者の70%に片頭痛の既往がある。急性発作にはトリプタン、予防にはプロプラノロール、フルナリジン、シプロヘプタジン、ピゾチフェン、バルプロ酸など片頭痛の予防薬が使われ、三環系抗うつ薬やSNRI、認知行動療法も勧められる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 中枢介在性の消化管の痛みの章
    differential: null
    common_misconception: 腹部片頭痛の発作は食事で誘発される
  provenance:
    source_ref: SRC-144
    source: Fukudo S, Aziz Q, Drossman DA, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2026;170:1283-1302（Rome V）
    doi: 10.1053/j.gastro.2025.12.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2025.12.038
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 成人での治療の根拠は主に片頭痛や小児の知見からの外挿
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-156
  domain: NG
  subdomain: Rome V 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: Rome Vの麻薬性腸症候群（オピオイド誘発性消化管痛覚過敏）は、麻薬で治療されている慢性または頻回の腹痛（ほぼ毎日）が現在または過去の消化管疾患で説明できず、麻薬の継続や増量で悪化または残る、効果が切れると著しく悪化し再開で改善する、発作の頻度・持続・強さが増す、のうち2つ以上を満たすものである。地域の有病率は0.17%、定期的にオピオイドを処方されている人では3〜6%と報告されている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 中枢介在性の消化管の痛みの章
    differential: Rome IVの麻薬性腸症候群（NG-075）、オピオイド誘発性便秘症
    common_misconception: 麻薬性腸症候群はRome Vで新しく加わった疾患である
  provenance:
    source_ref: SRC-144
    source: Fukudo S, Aziz Q, Drossman DA, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2026;170:1283-1302（Rome V）
    doi: 10.1053/j.gastro.2025.12.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2025.12.038
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率は章が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-157
  domain: NG
  subdomain: Rome V 中枢介在性の消化管の痛み
  assertion:
    plain_statement_ja: 麻薬性腸症候群の患者39人に入院で約7日間の解毒を行った研究では、解毒は89.7%で成功し、60%が反応者だったが、3か月後には43.2%がオピオイドを再開していた。オピオイドをやめ続けた人は腹痛が軽かった。治療には神経調節薬、精神疾患の併存への対応、脳腸行動療法を含む統合的なケアが必要とされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 中枢介在性の消化管の痛みの章
    differential: null
    common_misconception: 麻薬性腸症候群の腹痛にはオピオイドを増やせばよい
  provenance:
    source_ref: SRC-144
    source: Fukudo S, Aziz Q, Drossman DA, et al. Centrally Mediated Disorders of Gastrointestinal Pain. Gastroenterology 2026;170:1283-1302（Rome V）
    doi: 10.1053/j.gastro.2025.12.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2025.12.038
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 単一研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-158
  domain: NG
  subdomain: Rome V 肛門直腸疾患
  assertion:
    plain_statement_ja: Rome Vの肛門直腸疾患は、便失禁、肛門直腸痛（肛門挙筋症候群、原因不明の肛門直腸痛、消散性直腸痛）、排便協調障害、肛門直腸感覚機能障害（直腸感覚低下、直腸感覚過敏）に分けられる。排便協調障害と感覚機能障害の診断には症状と生理学的検査の両方が要るが、便失禁と肛門直腸痛は症状だけで診断する。
    condition:
      criteria: Rome V（2026）
      source: Rome V 肛門直腸疾患の章
    differential: Rome IVの機能性肛門直腸疾患（NG-077〜079）
    common_misconception: 肛門直腸疾患はすべて症状だけで診断できる
  provenance:
    source_ref: SRC-145
    source: Rao SSC, Bharucha AE, Carrington EV, et al. Anorectal Disorders. Gastroenterology 2026;170:1318-1346（Rome V）
    doi: 10.1053/j.gastro.2026.01.037
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.037
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-159
  domain: NG
  subdomain: Rome V 肛門直腸疾患
  assertion:
    plain_statement_ja: Rome Vの便失禁は、制御できない便の漏れが2回以上あり、4週間の排便日誌で月1回以上確認されるものと定義される。臨床では、最近12か月に2回以上の便失禁があればよい。月1回未満の患者が55%いるという研究があり、まれな便失禁でも生活の質を下げ、バイオフィードバック療法に同様に反応するため、「反復する」という曖昧な表現が改められた。
    condition:
      criteria: Rome V（2026）
      source: Rome V 肛門直腸疾患の章
    differential: 便失禁の一般的な説明（NG-019〜021）
    common_misconception: 便失禁は週に何度もなければ治療の対象にならない
  provenance:
    source_ref: SRC-145
    source: Rao SSC, Bharucha AE, Carrington EV, et al. Anorectal Disorders. Gastroenterology 2026;170:1318-1346（Rome V）
    doi: 10.1053/j.gastro.2026.01.037
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.037
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-160
  domain: NG
  subdomain: Rome V 肛門直腸疾患
  assertion:
    plain_statement_ja: 便失禁の世界の有病率は、80研究のシステマティックレビューで8.0%（Rome基準では5.4%）で、高齢者（9.3%対4.9%）と女性（9.1%対7.4%）に多い。危険因子には加齢、女性、分娩時の損傷、下痢、胆嚢摘出術、糖尿病、神経疾患・炎症性疾患がある。患者は自分から言わないことがあるため、直接尋ねる必要がある。
    condition:
      criteria: Rome V（2026）
      source: Rome V 肛門直腸疾患の章
    differential: null
    common_misconception: 便失禁はまれで、尋ねなくても患者が訴える
  provenance:
    source_ref: SRC-145
    source: Rao SSC, Bharucha AE, Carrington EV, et al. Anorectal Disorders. Gastroenterology 2026;170:1318-1346（Rome V）
    doi: 10.1053/j.gastro.2026.01.037
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.037
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 有病率は章が引用したレビューの値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-161
  domain: NG
  subdomain: Rome V 肛門直腸疾患
  assertion:
    plain_statement_ja: Rome Vの排便協調障害は、過度のいきみ、用手的な排便、肛門直腸の閉塞感、残便感のうち1つ以上が排便の25%以上にあり、直腸肛門内圧検査（直腸肛門圧較差の低下または異常な排出パターン）、バルーン排出検査、排便造影のいずれか1つで排出障害が示されるものである。異常な検査が1つならprobable、2つ以上ならdefiniteとする。慢性便秘症やIBSの基準を満たしていてもよい。
    condition:
      criteria: Rome V（2026）
      source: Rome V 肛門直腸疾患の章
    differential: Rome IVの機能性排便障害（2つ以上の検査異常、NG-078）
    common_misconception: 排便協調障害の診断には3種類の検査すべてが必要である
  provenance:
    source_ref: SRC-145
    source: Rao SSC, Bharucha AE, Carrington EV, et al. Anorectal Disorders. Gastroenterology 2026;170:1318-1346（Rome V）
    doi: 10.1053/j.gastro.2026.01.037
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.037
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-162
  domain: NG
  subdomain: Rome V 肛門直腸疾患
  assertion:
    plain_statement_ja: 排便協調障害は、正常な排便を「忘れてしまった」後天的な行動の障害と考えられ、バイオフィードバック療法で学び直せることが多い。地域の研究では、肛門内圧検査を受けた便秘患者の47%が排便協調障害で、年齢調整発生率は女性で10万人年あたり31.8、男性で6.6だった。自宅でのバイオフィードバックは外来と同程度の成功率（68%対70%）で、費用は低い。
    condition:
      criteria: Rome V（2026）
      source: Rome V 肛門直腸疾患の章
    differential: バイオフィードバック療法（NG-079、NG-106）
    common_misconception: 排便協調障害は下剤で治す
  provenance:
    source_ref: SRC-145
    source: Rao SSC, Bharucha AE, Carrington EV, et al. Anorectal Disorders. Gastroenterology 2026;170:1318-1346（Rome V）
    doi: 10.1053/j.gastro.2026.01.037
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.037
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は章が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-163
  domain: NG
  subdomain: Rome V 肛門直腸疾患
  assertion:
    plain_statement_ja: Rome Vの肛門挙筋症候群は、30分以上続く慢性・反復性の肛門直腸痛で、恥骨直腸筋の牽引で圧痛があり、他の原因が除外されたものである。圧痛がなければ原因不明の肛門直腸痛とする。消散性直腸痛は、排便と関係なく数秒から数分続く肛門直腸の痛みで、発作の間は痛みがない。無作為化試験では、圧痛のある患者の87%がバイオフィードバックで痛みが十分に和らいだ（電気刺激45%、マッサージ22%）。
    condition:
      criteria: Rome V（2026）
      source: Rome V 肛門直腸疾患の章
    differential: Rome IVの機能性肛門直腸痛（NG-077）
    common_misconception: 肛門挙筋症候群には坐浴や筋弛緩薬が有効である
  provenance:
    source_ref: SRC-145
    source: Rao SSC, Bharucha AE, Carrington EV, et al. Anorectal Disorders. Gastroenterology 2026;170:1318-1346（Rome V）
    doi: 10.1053/j.gastro.2026.01.037
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.037
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-164
  domain: NG
  subdomain: Rome V 肛門直腸疾患
  assertion:
    plain_statement_ja: Rome Vの直腸感覚低下は、便失禁または排便協調障害の症状基準を満たし、直腸バルーン伸展で初期感覚・便意・切迫便意・最大耐容量のうち2つ以上の閾値が正常上限の2SDを超えるものである。慢性便秘症の最大25%にみられ、オピオイド、パーキンソン病、脊髄損傷、糖尿病で二次的に起こることもある。治療には、バルーン量を段階的に減らして小さな刺激を感じ取る練習をする感覚バイオフィードバックが特に有用とされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 肛門直腸疾患の章
    differential: null
    common_misconception: 便意を感じないのは便秘の結果にすぎず治療できない
  provenance:
    source_ref: SRC-145
    source: Rao SSC, Bharucha AE, Carrington EV, et al. Anorectal Disorders. Gastroenterology 2026;170:1318-1346（Rome V）
    doi: 10.1053/j.gastro.2026.01.037
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.037
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-268 (id: Jlvnl4o)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-165
  domain: NG
  subdomain: Rome V 肛門直腸疾患
  assertion:
    plain_statement_ja: Rome Vの直腸感覚過敏は、便失禁または排便協調障害の症状基準を満たし、便意・切迫便意・最大耐容量・痛みのうち1つ以上の閾値が正常下限の2SDより低いものである（初期感覚の閾値は使わない）。IBSと強く関連し、切迫感や腹痛を伴う。無作為化試験では、バロスタットで段階的に伸展する感覚順応療法がエスシタロプラムより感覚過敏と便通症状を改善した。
    condition:
      criteria: Rome V（2026）
      source: Rome V 肛門直腸疾患の章
    differential: IBSの内臓知覚過敏（NG-087）
    common_misconception: 直腸感覚過敏は検査をしなくても症状だけで診断できる
  provenance:
    source_ref: SRC-145
    source: Rao SSC, Bharucha AE, Carrington EV, et al. Anorectal Disorders. Gastroenterology 2026;170:1318-1346（Rome V）
    doi: 10.1053/j.gastro.2026.01.037
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.037
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-166
  domain: NG
  subdomain: Rome V 生物心理社会的ケア
  assertion:
    plain_statement_ja: Rome Vは心理社会的ケアの統合を3段階に整理している。レベル1では、医師が診断と第一選択の治療とともに、腸脳軸の心理教育とストレス対処・運動・食事・生活習慣のセルフマネジメントを伝える。レベル2では、訓練を受けた看護師などが脳腸行動療法を行い、医師が軽い不安や抑うつに向精神薬を処方することもある。レベル3では、消化器心理士などの精神保健の専門家が加わり、これが統合的ケアの最良の形とされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 生物心理社会的側面の章
    differential: null
    common_misconception: 心理的なケアは精神科に紹介してから始めればよい
  provenance:
    source_ref: SRC-146
    source: Elsenbruch S, Ballou S, Keefer L, et al. Biopsychosocial Aspects of Adult and Pediatric Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1205-1223（Rome V）
    doi: 10.1053/j.gastro.2026.02.009
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.009
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-005 (id: JlAKpjg)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-167
  domain: NG
  subdomain: Rome V 生物心理社会的ケア
  assertion:
    plain_statement_ja: Rome Vは、レベル1の基本的な心理社会的ケアを腸脳相関障害の診療に関わるすべての医療者が行うべきだとしている。脳腸行動療法の根拠が最も強いのは認知行動療法と腸指向性催眠療法で、成人では主にIBSで20を超える無作為化試験がある。腸指向性催眠療法は成人で6〜12回、小児で3〜6回行われる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 生物心理社会的側面の章
    differential: 日本のIBS診療ガイドライン2020の心理療法（NG-094）
    common_misconception: 心理療法は心の病気がある患者にだけ有効である
  provenance:
    source_ref: SRC-146
    source: Elsenbruch S, Ballou S, Keefer L, et al. Biopsychosocial Aspects of Adult and Pediatric Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1205-1223（Rome V）
    doi: 10.1053/j.gastro.2026.02.009
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.009
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-168
  domain: NG
  subdomain: Rome V 生物心理社会的ケア
  assertion:
    plain_statement_ja: Rome Vの生物心理社会的側面の章によれば、中枢性神経調節薬は中等症以上で生活の質の障害が大きく、第一選択の治療が十分に効かない患者に使う。成人の便秘のないIBSの痛みには三環系抗うつ薬が第一選択で、ノルトリプチリンやデシプラミンはアミトリプチリンより忍容性がよい。悪心や体重減少が問題のときや機能性ディスペプシアでは、成人に低用量ミルタザピンを加えるのが有用なことがある。
    condition:
      criteria: Rome V（2026）
      source: Rome V 生物心理社会的側面の章
    differential: null
    common_misconception: 抗うつ薬を勧めるのは症状が気のせいだと考えているからである
  provenance:
    source_ref: SRC-146
    source: Elsenbruch S, Ballou S, Keefer L, et al. Biopsychosocial Aspects of Adult and Pediatric Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1205-1223（Rome V）
    doi: 10.1053/j.gastro.2026.02.009
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.009
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-169
  domain: NG
  subdomain: Rome V 生物心理社会的ケア
  assertion:
    plain_statement_ja: Rome Foundationは、脳と腸の両方に作用する薬を「腸脳神経調節薬（gut-brain neuromodulators）」と呼び直した。薬理学的な意義と使う理由を理解しやすくし、偏見を減らし、服薬の継続を助けるためである。積極的な診断を伝えることは、患者の受容を高め、不要な侵襲的検査を防ぎ、偏見を減らすとされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 生物心理社会的側面の章
    differential: null
    common_misconception: 抗うつ薬という名前のままでも患者の受け止め方は変わらない
  provenance:
    source_ref: SRC-146
    source: Elsenbruch S, Ballou S, Keefer L, et al. Biopsychosocial Aspects of Adult and Pediatric Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1205-1223（Rome V）
    doi: 10.1053/j.gastro.2026.02.009
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.009
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-170
  domain: NG
  subdomain: Rome V 診断質問票
  assertion:
    plain_statement_ja: Rome Vの成人用診断質問票は114問で25の腸脳相関障害を評価し、Rome IV版より3つ多い（げっぷができない症候群、腹部片頭痛、麻薬性腸症候群。前の2つはRome基準に新しく加わった疾患）。心窩部痛、心窩部灼熱感、胆道痛の部位を示す解剖図が3つ加えられた。
    condition:
      criteria: Rome V（2026）
      source: Rome V 診断質問票の開発
    differential: null
    common_misconception: Rome Vで新たに加わった成人の疾患には麻薬性腸症候群が含まれる
  provenance:
    source_ref: SRC-147
    source: Palsson OS, Lacy BE, Benninga MA, et al. Development of the Rome V Diagnostic Questionnaires. Gastroenterology 2026;170:1408-1416
    doi: 10.1053/j.gastro.2026.01.041
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.041
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-171
  domain: NG
  subdomain: Rome V 診断質問票
  assertion:
    plain_statement_ja: Rome IVの質問票の9段階の頻度尺度は「月2〜3回」「週2〜3回」のように2つの頻度を1つの選択肢にまとめていたため、週3日以上などの基準の判定が不正確だった。Rome Vでは2と3を分け、週1回に「月4日」を併記した修正版の9段階尺度が採用された。0〜30日で答える尺度も試されたが、10日や15日などの切りのよい値に回答が偏ったため採用されなかった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 診断質問票の開発
    differential: null
    common_misconception: 回答を1日単位にするほど症状の頻度は正確にわかる
  provenance:
    source_ref: SRC-147
    source: Palsson OS, Lacy BE, Benninga MA, et al. Development of the Rome V Diagnostic Questionnaires. Gastroenterology 2026;170:1408-1416
    doi: 10.1053/j.gastro.2026.01.041
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.041
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-172
  domain: NG
  subdomain: Rome V 診断質問票
  assertion:
    plain_statement_ja: 日本を含む15か国の成人30,000人のインターネット調査では、Rome V基準で何らかの腸脳相関障害をもつ人は42.2%で、Rome IVの40.3%とほぼ同じだった。IBSは8.9%（Rome IVは4.1%）、便失禁は4.2%（1.6%）と、基準の変更で増えた。新しく評価された腹部片頭痛は5.3%、げっぷができない症候群は1.5%、麻薬性腸症候群は0.08%だった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 診断質問票の開発
    differential: Rome IVの世界調査（NG-006〜010）、英国の登録データの比較（NG-123）
    common_misconception: Rome Vで腸脳相関障害の有病率は大きく変わった
  provenance:
    source_ref: SRC-147
    source: Palsson OS, Lacy BE, Benninga MA, et al. Development of the Rome V Diagnostic Questionnaires. Gastroenterology 2026;170:1408-1416
    doi: 10.1053/j.gastro.2026.01.041
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.041
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: Rome IVの調査とは対象国が一部異なり、厳密な比較ではない
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-173
  domain: NG
  subdomain: Rome V 診断質問票
  assertion:
    plain_statement_ja: Rome Vでは便失禁の頻度の閾値が月2回から月1回に下げられ、質問票による便失禁の有病率はRome IVの1.6%から4.2%に上がった。オピオイド誘発性便秘症は、オピオイドの使用を本人が具体的に答える形に変えたため0.2%（Rome IVは1.6%）に下がった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 診断質問票の開発
    differential: null
    common_misconception: Rome Vの便失禁の基準はRome IVより厳しくなった
  provenance:
    source_ref: SRC-147
    source: Palsson OS, Lacy BE, Benninga MA, et al. Development of the Rome V Diagnostic Questionnaires. Gastroenterology 2026;170:1408-1416
    doi: 10.1053/j.gastro.2026.01.041
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.041
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-174
  domain: NG
  subdomain: Rome V 診断質問票
  assertion:
    plain_statement_ja: Rome Vの小児用診断質問票は保護者が答える乳児版（0〜3歳）と小児・思春期版（4〜17歳）、10〜17歳の自己記入版からなり、27の腸脳相関障害を評価する。Rome IV版より14多く、予期性制限摂食、過敏性嚥下障害、空腹調節障害（過剰・低下）、医療に誘発された摂食障害、逆流過敏症、逆流陰性食道痛障害、CAPS、カンナビノイド悪阻、乳児苦痛症候群（infant distress syndrome）、胃上部げっぷ、機能性腹部膨満、胆道痛症候群、消散性直腸痛が加わった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 診断質問票の開発
    differential: Rome IVの小児の分類（NG-080〜085）、Rome Vの小児上部消化管（NG-118）
    common_misconception: Rome Vの小児の疾患はRome IVとほぼ同じである
  provenance:
    source_ref: SRC-147
    source: Palsson OS, Lacy BE, Benninga MA, et al. Development of the Rome V Diagnostic Questionnaires. Gastroenterology 2026;170:1408-1416
    doi: 10.1053/j.gastro.2026.01.041
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.041
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 乳児苦痛症候群の診断基準は小児下部消化管・胆道の章（NG-230）で確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-175
  domain: NG
  subdomain: Rome V 診断質問票
  assertion:
    plain_statement_ja: 小児の委員会は、腸脳相関障害の重症度を頻度（Frequency）、強さ（Intensity）、慢性度（Chronicity）、子どもと家族の生活への影響（Impact）の4項目で別々に評価するFICAIを提案した。慢性便秘症ではIが失禁を表すなど、疾患により項目が置き換わる。FICAIは紹介時の情報共有や治療の判断・経過観察に使うことをめざすが、診断基準や質問票の採点には含まれない。
    condition:
      criteria: Rome V（2026）
      source: Rome V 診断質問票の開発
    differential: null
    common_misconception: FICAIはRome Vの小児の診断基準の一部である
  provenance:
    source_ref: SRC-147
    source: Palsson OS, Lacy BE, Benninga MA, et al. Development of the Rome V Diagnostic Questionnaires. Gastroenterology 2026;170:1408-1416
    doi: 10.1053/j.gastro.2026.01.041
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.041
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: FICAIはデルファイ法による提案で、まだ検証されていない
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-176
  domain: NG
  subdomain: Rome V 診断質問票
  assertion:
    plain_statement_ja: 中国、イタリア、メキシコ、米国の母親7,724人が答えた小児の調査では、Rome V基準でIBSは2.1%、慢性便秘症は17.1%、心窩部痛症候群は1.7%、食後愁訴症候群は5.5%だった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 診断質問票の開発
    differential: 小児の機能性便秘の有病率（NG-084）
    common_misconception: 小児のIBSは便秘より多い
  provenance:
    source_ref: SRC-147
    source: Palsson OS, Lacy BE, Benninga MA, et al. Development of the Rome V Diagnostic Questionnaires. Gastroenterology 2026;170:1408-1416
    doi: 10.1053/j.gastro.2026.01.041
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.041
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 母親の回答による調査で、偏りの可能性がある
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-268 (id: Jlvnl4o)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-177
  domain: NG
  subdomain: Rome V 小児上部消化管
  assertion:
    plain_statement_ja: Rome Vの小児上部消化管の章によれば、小児の逆流過敏症では酸分泌抑制薬の経験的な試験は8週間までに限り、改善しなければ内視鏡、pHインピーダンス検査などに進む。機能性悪心または食後愁訴症候群の小児57人にミルタザピンを使った報告では、反応率は82%だった。
    condition:
      criteria: Rome V（2026）
    differential: null
    common_misconception: 小児の胸やけには酸分泌抑制薬を効くまで続ける
  provenance:
    source_ref: SRC-140
    source: Rosen R, et al. Rome V Pediatric Upper Gastrointestinal Disorders of Gut–Brain Interaction. Gastroenterology 2026;170:1347-1366
    doi: 10.1053/j.gastro.2026.01.039
    pmid: null
    pmcid: null
    url: https://theromefoundation.org/wp-content/uploads/2026/09/Rome-V-Pediatric-Upper-Gastrointestinal-Disorders-.pdf
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）。ユーザー提供の原本で確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ミルタザピンの値は章が引用した後ろ向きの報告による（二次資料経由）。成人の機能性胸やけ・逆流過敏症では8週間以上の最適化した酸分泌抑制療法が要件（NG-191）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)；TBL-02-07-025 (id: JlAKpkw)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-178
  domain: NG
  subdomain: 慢性下痢症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 日本の便通異常症診療ガイドライン2023（慢性下痢症）は、下痢を「便形状が軟便あるいは水様便で、かつ排便回数が増加する状態」、慢性下痢症を「4週間以上持続または反復する下痢のために日常生活に支障をきたした病態」と定義した。排便回数が増えるだけでは下痢とはいわない。4週間としたのは、感染性の急性下痢を否定するためである。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性下痢症 CQ1-1（2頁）、BQ1-1（8頁）
    differential: Rome Vの機能性下痢（6か月以上前の発症）
    common_misconception: 1日の排便回数が多ければ下痢である
  provenance:
    source_ref: SRC-148
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性下痢症』南江堂、2023（第1刷 2023年7月13日、ISBN 978-4-524-21006-0）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-179
  domain: NG
  subdomain: 慢性下痢症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 日本の便通異常症診療ガイドライン2023は、慢性下痢症を、薬剤性、食物起因性、症候性（全身疾患性）、感染性、器質性（炎症性・腫瘍性）、胆汁酸性、機能性下痢症、下痢型IBSの8つに分類している。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性下痢症 CQ1-2（4頁）
    differential: null
    common_misconception: 慢性下痢の大半はIBSである
  provenance:
    source_ref: SRC-148
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性下痢症』南江堂、2023（第1刷 2023年7月13日、ISBN 978-4-524-21006-0）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-180
  domain: NG
  subdomain: 慢性下痢症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 日本の便通異常症診療ガイドライン2023は、機能性下痢症を日常臨床に合わせて広げたものを「慢性下痢症（狭義）」とした。Rome IVの「6か月以上前から」という期間は日本の日常診療に合わないとして4週間以上とし、機能性下痢症と下痢型IBSは連続した病態であるため、慢性下痢が主症状なら腹痛などの随伴症状は問わないとした。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性下痢症 作成の手順
    differential: Rome Vの機能性下痢は下痢型IBSの基準を満たさないことを求める
    common_misconception: 日本の慢性下痢症（狭義）はRome基準の機能性下痢と同じ定義である
  provenance:
    source_ref: SRC-148
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性下痢症』南江堂、2023（第1刷 2023年7月13日、ISBN 978-4-524-21006-0）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-181
  domain: NG
  subdomain: 慢性下痢症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性下痢症の警告症状・徴候には、予期しない体重減少、夜間の下痢、最近の抗菌薬服用、血便、大量・頻回の下痢、低栄養状態、炎症性腸疾患や大腸癌などの家族歴があるが、その有用性は明らかでない（推奨なし、エビデンスレベルC）。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性下痢症 CQ2-1（17頁）
    differential: 慢性便秘症の警告症状（NG-101）
    common_misconception: 警告症状がなければ器質的疾患は否定できる
  provenance:
    source_ref: SRC-148
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性下痢症』南江堂、2023（第1刷 2023年7月13日、ISBN 978-4-524-21006-0）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-182
  domain: NG
  subdomain: 慢性下痢症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性下痢症の鑑別では、問診と身体診察から病態を考え、血液・糞便・画像検査を個別に判断して行うことが推奨される（強い推奨、合意率90%、エビデンスレベルA）。大腸内視鏡は器質的疾患との鑑別に有用なので推奨され（強い推奨、合意率100%、A）、内視鏡で異常がなくても危険性を考えてランダム生検を行うことが提案されている。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性下痢症 CQ2-2（18頁）、CQ2-3（20頁）
    differential: null
    common_misconception: 内視鏡で異常がなければ生検は不要である
  provenance:
    source_ref: SRC-148
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性下痢症』南江堂、2023（第1刷 2023年7月13日、ISBN 978-4-524-21006-0）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)；TBL-02-07-031 (id: JlAKplI)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-183
  domain: NG
  subdomain: 慢性下痢症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 日本人の慢性下痢症（狭義）の有病率は約3〜5%で、男性に多い傾向があると推定される（エビデンスレベルB）。慢性下痢症（狭義）は生活の質や労働生産性を下げる可能性があるが（D）、長期予後に影響するという明らかな根拠はない。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性下痢症 CQ3-1（24頁）、CQ3-2（26頁）、FRQ3-1（27頁）
    differential: null
    common_misconception: 慢性下痢は女性に多い
  provenance:
    source_ref: SRC-148
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性下痢症』南江堂、2023（第1刷 2023年7月13日、ISBN 978-4-524-21006-0）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-184
  domain: NG
  subdomain: 慢性下痢症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性下痢症（狭義）の病態に関する報告はほとんどなく、連続した病態と考えられる下痢型IBSでは、水吸収の異常、微小炎症、粘膜バリア障害、胆汁酸の吸収障害、腸管運動の異常、腸内細菌の異常などが推測されている。食事内容は病態に関与するが（エビデンスレベルB）、心理的異常との関連を示す明確な根拠はなく、腸内細菌は関与している可能性がある。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性下痢症 FRQ4-1（30頁）、FRQ4-2（35頁）、CQ4-1（36頁）、FRQ4-3（38頁）
    differential: null
    common_misconception: 慢性下痢症はストレスが原因である
  provenance:
    source_ref: SRC-148
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性下痢症』南江堂、2023（第1刷 2023年7月13日、ISBN 978-4-524-21006-0）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-185
  domain: NG
  subdomain: 慢性下痢症（日本の便通異常症GL）
  assertion:
    plain_statement_ja: 慢性下痢症（狭義）には、ロペラミドが症状緩和に最もよく使われる有効な薬である（推奨なし、C）。プロバイオティクスは有効な場合があるが、菌種・量・期間の根拠ははっきりしない（C）。5-HT3受容体拮抗薬、抗コリン薬、漢方薬、心理療法、抗菌薬、ポリカルボフィルカルシウム、アドレナリン作動薬の有効性は不明で、日本でラモセトロンが保険適用なのは下痢型IBSである。
    condition:
      region: 日本
      guideline: 便通異常症診療GL 2023—慢性下痢症 CQ5-1（44頁）、CQ5-2（46頁）、FRQ5-2〜5-8（48〜54頁）
    differential: 下痢型IBSの治療（NG-091、NG-096）
    common_misconception: 慢性下痢症にはIBSと同じ薬がすべて効く
  provenance:
    source_ref: SRC-148
    source: 日本消化管学会編『便通異常症診療ガイドライン2023—慢性下痢症』南江堂、2023（第1刷 2023年7月13日、ISBN 978-4-524-21006-0）
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © 日本消化管学会（非CC）。ユーザー提供の刊行版PDFで確認
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-186
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: Rome Vの食道の腸脳相関障害（機能性胸痛、機能性胸やけ、逆流過敏症、食道球、機能性嚥下障害）は、構造的・炎症性・主要な運動の異常がないのに胸やけ、胸痛、咽喉頭の異物感、嚥下障害が起こるものである。GERDの除外はLyon Consensus 2.0、運動障害の除外はChicago分類v4.0に従う（Rome IVはLyon 1.0とChicago v3.0）。無効食道運動（IEM）は除外の理由にならない。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: Rome IVの機能性食道疾患（NG-058）、GERD、アカラシア、好酸球性食道炎
    common_misconception: 機能性食道疾患は症状だけで診断できる
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: NG-124（総説の抄録）と同じ内容を原典で確認
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-187
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: Rome Vでは、好酸球性食道炎を除外するための食道生検が重要とされ、嚥下障害、食事中の胸痛、食物のつかえがあれば生検で好酸球が高倍率視野あたり15個未満であることを確かめてから食道の腸脳相関障害を考える。機能性胸痛での生検は、Rome IVでは全例に勧められていたが、Rome Vでは食事に関連する胸痛のときに限られた。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: null
    common_misconception: 機能性胸痛では全例で食道生検が必要である
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)；TBL-02-07-031 (id: JlAKplI)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-188
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: Rome Vの機能性胸痛は、胸やけや嚥下障害を伴わない胸骨後部の痛みまたは不快感で、GERD（ロサンゼルス分類B以上の食道炎またはLyon 2.0にもとづく逆流負荷）や非逆流性の食道炎、食道胃接合部の通過障害や蠕動障害（IEMを除く）では説明できないものである。最適化した酸分泌抑制療法を8週間以上行っても週1回以上あり、最近3か月続き6か月以上前に始まっていることを要する。心臓の原因を先に除外する。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: Rome IVの機能性胸痛（NG-059）、虚血性心疾患
    common_misconception: 胸痛の原因は問診で心臓か食道かを区別できる
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-189
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: 非心臓性胸痛の約50〜60%はGERD、15〜18%は食道運動障害で、32〜35%が機能性胸痛の基準を満たす。GERDが多いため、PPIまたはP-CABを最適化して8週間試すのが簡便で費用効果が高い。非心臓性胸痛の患者の最大75%に不安、抑うつ、身体化などの精神的な併存症がある。機能性胸痛の有病率は世界の調査で1.4%とされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: null
    common_misconception: 非心臓性胸痛の多くは機能性胸痛である
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-190
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: 機能性胸痛の治療の中心は痛みの神経調節で、三環系抗うつ薬、SNRI、トラゾドンはプラセボより最大50%有効とされ、SSRIの結果は一貫しない。消化器に特化した認知行動療法は症状の頻度を減らし（相対リスク0.70）、腸指向性催眠療法や横隔膜呼吸を含むバイオフィードバックも役立つ。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: null
    common_misconception: 機能性胸痛にはPPIを増量し続ければよい
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 相対リスクはコクランレビューの値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-191
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: Rome Vの機能性胸やけは、胸骨後部の灼熱感が最適化した酸分泌抑制療法を8週間以上続けても改善せず、GERD（ロサンゼルス分類B以上またはLyon 2.0の逆流負荷）、非逆流性の食道炎、主要な運動障害（IEMを除く）がないものである。夜間平均基礎インピーダンス（MNBI）が正常であることは機能性胸やけを支持する。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: Rome IVの機能性胸やけ（NG-060）、逆流過敏症、非びらん性逆流症（NERD）
    common_misconception: PPIが効かない胸やけはすべてGERDの難治例である
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 頻度の要件は、診断基準の脚注と本文では「週1回以上」、臨床評価の節では「週2日以上」と記載が分かれている
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-192
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: PPIが効かない胸やけでは、内視鏡はできればPPIを2〜4週間中止してから行う。ロサンゼルス分類Bの食道炎はGERDの確定所見とされるようになった。逆流モニタリングはPPIを中止して行い、96時間のワイヤレスpH検査では酸曝露時間（AET）が2日以上で6%を超えればGERD、全日で4%未満かつ症状との関連が陰性ならGERDを否定する。pHインピーダンス検査ではAET 4%未満かつ逆流40回未満でGERDを否定し、MNBI 1500 Ω未満はGERDを、2500 Ωを超えれば機能性胸やけを支持する。AET 4〜6%は判定保留とする。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: null
    common_misconception: PPIを飲んだまま内視鏡をすればGERDを否定できる
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-193
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: 機能性胸やけの有病率は世界の調査でインターネット1.1%、世帯0.4%である。PPI抵抗性の逆流様症状の18〜30%が食道の腸脳相関障害に当たると考えられ、高用量PPIで改善するのは20〜30%にとどまる。2年後も3分の2は症状が続く。治療は安心させる説明、侵襲的検査の繰り返しを避けること、神経調節薬、脳腸行動療法で、逆流防止手術は避ける。内視鏡的高周波治療は偽治療と差がなかった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: null
    common_misconception: 機能性胸やけには逆流防止手術が有効である
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は章が引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-194
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: Rome Vの逆流過敏症は、内視鏡が正常で酸曝露が生理的範囲にあるのに、逆流と症状の関連が陽性（症状指数50%以上または症状関連確率95%以上）の胸やけまたは胸痛で、8週間以上の最適化した酸分泌抑制療法でも週1回以上あるものである。逆流やげっぷだけの症状は含めず、反芻症候群、胃上部げっぷ、げっぷができない症候群は除外する。シタロプラムの試験では症状が残った人が38.5%（プラセボ66.7%）だった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: Rome IVの逆流過敏症（NG-061）、機能性胸やけ（逆流との関連が陰性）
    common_misconception: 逆流過敏症は酸曝露時間が長いGERDである
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: シタロプラムの値は章が引用した試験による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-025 (id: JlAKpkw)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-195
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: Rome Vの食道球（咽喉頭異物感）は、喉の痛みのない塊や異物の感覚で、食間に起こり、嚥下障害や嚥下痛がなく、身体診察と喉頭鏡で構造的病変がないものである。食道入口部の胃粘膜異所（inlet patch）があれば腸脳相関障害とは診断しない。GERDや主要な運動障害がなく、8週間の酸分泌抑制療法の後も週1回以上あることを要する。症状は3年後に75%、7年後に50%で続き、治療は説明と行動療法を優先する。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: Rome IVの食道球（NG-062）、頭頸部腫瘍、食道入口部の胃粘膜異所
    common_misconception: 食道球には胃粘膜異所の焼灼が確立した治療である
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 経過の値は章が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-196
  domain: NG
  subdomain: Rome V 食道疾患
  assertion:
    plain_statement_ja: Rome Vの機能性嚥下障害は、固形物や液体がつかえる感覚があり、粘膜・構造の異常、GERD、非逆流性の食道炎、主要な運動障害（IEMを除く）では説明できないものである。錠剤やマシュマロを使った食道造影やFLIPが正常であることは診断を支持する。高解像度内圧検査が正常だった164人のうち約3分の1でFLIPが異常を見つけたとされ、機能性嚥下障害は最も少ない食道の腸脳相関障害と考えられている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 食道疾患の章
    differential: Rome IVの機能性嚥下障害（NG-063）、EndoFLIP（NG-109）、好酸球性食道炎
    common_misconception: 内圧検査が正常なら嚥下障害は機能性と断定できる
  provenance:
    source_ref: SRC-149
    source: Gyawali CP, Roman S, Zerbib F, et al. Functional Esophageal Disorders. Gastroenterology 2026;170:1224-1239（Rome V）
    doi: 10.1053/j.gastro.2026.02.005
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.005
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: FLIPの値は章が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-197
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vは胃十二指腸の腸脳相関障害を、機能性ディスペプシア（食後愁訴症候群・心窩部痛症候群）、悪心・嘔吐症（慢性悪心嘔吐症候群、周期性嘔吐症候群、カンナビノイド悪阻症候群）、過剰なげっぷ（胃上部げっぷ・胃げっぷ）、げっぷができない症候群（新設）、反芻症候群の5つに分ける。Rome Foundation Global Studyでは一般人口の10.6%に胃十二指腸疾患に合う症状があった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: Rome IVの胃十二指腸疾患（NG-064〜068）
    common_misconception: 胃十二指腸の腸脳相関障害は機能性ディスペプシアだけである
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-198
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vの機能性ディスペプシアは、煩わしい食後のもたれ感、早期飽満感、心窩部痛、心窩部灼熱感のうち1つ以上があり、構造的・全身的・代謝的疾患で説明できず、食後愁訴症候群（PDS）か心窩部痛症候群（EPS）、または両方の基準を満たすものである。機能性ディスペプシアは包括的な用語として残るが、PDS・EPSの用語を優先して使う。有病率は7.2%とされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: Rome IVの機能性ディスペプシア（NG-064）、二次性ディスペプシア、GD-001〜018
    common_misconception: 機能性ディスペプシアは除外診断でしか付けられない病名である
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-199
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vの食後愁訴症候群（PDS）は、日常生活に影響する食後のもたれ感、または普通の量の食事を食べきれない早期飽満感が週2日以上あるもので、Rome IVの週3日以上から下げられた。「食後」は食事から2時間以内に起こることと定義された。これらがあれば、食事で誘発・増悪する心窩部痛・灼熱感、悪心、上腹部膨満、過剰なげっぷもPDSの一部とする。悪心が主で嘔吐が続く場合はPDSとせず、慢性悪心嘔吐症候群か胃不全麻痺を考える。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: Rome IVのPDS（週3日以上、NG-064）、小児のPDS（週3回以上、NG-121）
    common_misconception: 食後の心窩部痛があれば心窩部痛症候群と診断する
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 週2日の閾値は患者のフォーカスグループで症状を煩わしいと感じる頻度にもとづく
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-200
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vの心窩部痛症候群（EPS）は、臍より上の中央に限局した煩わしい心窩部痛または灼熱感が週1日以上あり、PDSの基準を満たさないものである。排便で痛みが軽くなるなら腸疾患を考える。PDSのない患者では、食後に痛みが起こる割合が50%以上の「食事関連EPS」と50%未満の「食事非関連EPS」に分ける暫定基準が示された。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: null
    common_misconception: 心窩部痛症候群の痛みは食事と関係しない
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 食事関連・非関連の区分は暫定基準で、さらに研究が必要とされている
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-201
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: 機能性ディスペプシアの症状がある人では全員でピロリ菌の感染を調べる。警告症状がなければ上部内視鏡は必須ではない（警告症状がある場合と臨床研究では必須）。セリアック病の血清検査、十二指腸生検、画像検査、運動機能検査は日常的には勧められない。ピロリ菌胃炎は器質的疾患とみなされ、除菌は約30%に有効（治療必要数15）で、除菌後6か月以上症状が消えればピロリ菌関連ディスペプシアとする。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: ピロリ菌関連ディスペプシア（GD-001〜018）
    common_misconception: 機能性ディスペプシアの診断には全例で内視鏡が必要である
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-202
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: 機能性ディスペプシアの病態には、胃の適応性弛緩の障害（最大40%）、胃排出遅延（約30%）、内臓知覚過敏（最大30%）、十二指腸の透過性亢進と好酸球・肥満細胞の増加、胆汁酸組成の変化、感染後の発症、心理的要因が関わる。遺伝の影響は弱く、特定の遺伝子多型との関連はメタ解析で示されていない。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: null
    common_misconception: 機能性ディスペプシアは胃の運動が遅いことだけで説明できる
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 割合は章が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-203
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: 機能性ディスペプシアの治療で、PPIは標準量を1日1回4〜8週間使い、効果が不十分なら増量せず中止する（治療必要数11）。運動機能改善薬の治療必要数は12で、アコチアミドはPDSに最も有効とされる。中枢性神経調節薬の治療必要数は6だが、効果は三環系抗うつ薬と抗精神病薬（レボスルピリド）に限られ、SSRIの試験は陰性だった。体重減少にはミルタザピン、早期飽満感にはタンドスピロンやブスピロン、漢方薬では六君子湯が挙げられている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: アコチアミドの添付文書（NG-039〜041）
    common_misconception: 機能性ディスペプシアにはPPIを効くまで増量する
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 治療必要数は章が引用したメタ解析の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-204
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vの胃十二指腸委員会は、PDSの治療を、食事と生活の指導、PPI・運動機能改善薬・有効性の確立した生薬製剤のいずれか、内視鏡などの検査、第二段階の神経調節薬の順に進めることを提案している。これらに反応しないPDSで胃排出検査が遅延を示せば「胃排出遅延を伴うPDS」とし、胃不全麻痺の用語は悪心や嘔吐が主な場合に限る。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: 胃不全麻痺（NG-011〜015）
    common_misconception: 胃排出が遅ければ胃不全麻痺と診断する
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-257 (id: Jlvnl3Q)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: 医学各論 Ⅵ-2-B-①（機能性ディスペプシア、a）
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-205
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vの慢性悪心嘔吐症候群は、日常生活に影響する悪心が週2日以上あり、嘔吐は週1回以上あってもなくてもよい。自己誘発性嘔吐、摂食障害、反芻を除外し、PDSが主な場合は除外し、胃排出遅延を伴えば胃不全麻痺と診断する。有病率は0.8〜1.2%で、IBSや機能性ディスペプシアとの合併が多い。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: Rome IVの慢性悪心嘔吐症候群（NG-065）、小児の慢性悪心症候群（NG-119）
    common_misconception: 嘔吐がなければ慢性悪心嘔吐症候群とは診断しない
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-206
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vの周期性嘔吐症候群は、急に始まり最長10日続く型どおりの嘔吐発作が、前年に3回以上、最近6か月に2回以上、1週間以上の間隔で起こるもので、発作の間に軽い悪心や単発の嘔吐があってもよくなった。予防には三環系抗うつ薬（69%で改善）やトピラマート、発作時には制吐薬、NK1受容体拮抗薬、トリプタンなどが使われる。日本の有病率は1,000人あたり0.05と低い。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: Rome IVの周期性嘔吐症候群（NG-066）、NG-016〜018
    common_misconception: 発作の間に少しでも嘔吐があれば周期性嘔吐症候群ではない
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 治療効果と日本の有病率は章が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-207
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vのカンナビノイド悪阻症候群は、周期性嘔吐症候群に似た発作が、1年以上の過剰な大麻使用（週4日以上または週15回以上）の後に起こり、6か月以上または典型的な発作3回分の断麻で消えるものである。長時間の熱い入浴は補助所見とされる。治療の基本は断麻で、発作時にはカプサイシンの外用やハロペリドールが使われ、三環系抗うつ薬の予防効果は乏しい。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: Rome IVのカンナビノイド悪阻症候群（NG-067）、小児の基準（NG-122）
    common_misconception: 大麻を数日やめて嘔吐が続けばカンナビノイド悪阻症候群は否定できる
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-208
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vのげっぷ障害は、日常生活に影響するげっぷが週3日を超えるもので、食道から出る胃上部げっぷと胃から出る胃げっぷに分ける。両者は食道インピーダンス検査で区別でき、胃上部げっぷは24時間に13回を超えると過剰とされる。胃上部げっぷには言語療法（83%が改善）、認知行動療法、横隔膜呼吸訓練が有効で、ジメチコンなどは役立たない。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: Rome IVのげっぷ障害（NG-068）、NG-048〜051
    common_misconception: げっぷが多いのは空気を多く飲み込んでいるからで、消泡剤で治る
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-209
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vで新設された「げっぷができない症候群」（逆行性輪状咽頭筋機能不全）は、げっぷができない、またはしにくいことが週3日以上あり、アカラシア、噴門形成術後、食道胃接合部通過障害、GERDなどで説明できないものである。胃食道からのガスに対して上部食道括約筋が弛緩しないことが原因とされ、腹部膨満、放屁、胸や頸部のゴロゴロ音、胸痛、心窩部痛を伴うことがある。炭酸水を使った高解像度インピーダンス内圧検査が診断を支持し、治療は上部食道括約筋への50〜100単位のボツリヌス毒素注射で、効果は多くの例で6か月以上続く。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: げっぷ障害、GERD、アカラシア
    common_misconception: げっぷが出ないのは病気ではない
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 疫学は調べられておらず、過小診断と過剰診断の両方の可能性がある。食道の章は、この病態（abelchia）を定義が不十分な新しい症候群として扱っている。分類番号は胃十二指腸の章ではB4、序論の一覧ではB3c（げっぷ障害の下位）と章によって異なる
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-210
  domain: NG
  subdomain: Rome V 胃十二指腸疾患
  assertion:
    plain_statement_ja: Rome Vの反芻症候群は、食べたばかりの食物を努力なく繰り返し口に戻し、吐き出すか飲み込むもので、吐き戻しの前にえずきや悪心がないことが診断基準に移された。一般人口の有病率は3.1%である。食後に行う食道内圧・インピーダンスの同時測定が客観的診断の基準とされ、治療の中心は横隔膜呼吸などの行動療法（30〜66%で消失）である。PPIは食物の酸性化を妨げて反芻を長引かせることがある。
    condition:
      criteria: Rome V（2026）
      source: Rome V 胃十二指腸疾患の章
    differential: Rome IVの反芻症候群（NG-068）、NG-048〜051、GERD、胃不全麻痺、摂食障害
    common_misconception: 反芻症候群は嘔吐の一種で制吐薬が効く
  provenance:
    source_ref: SRC-150
    source: Törnblom H, Carbone F, Hasler WL, et al. Gastroduodenal Disorders. Gastroenterology 2026;170:1240-1260（Rome V）
    doi: 10.1053/j.gastro.2026.01.038
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.038
    source_license: CC BY 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 行動療法の効果は章が引用した症例集積の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-211
  domain: NG
  subdomain: 神経消化器病学の基礎（Rome V）
  assertion:
    plain_statement_ja: 消化管の外来性感覚神経には迷走神経性と脊髄性がある。迷走神経性の求心路は食道と胃に最も多く、小腸で減り、遠位大腸では少なく直腸にはない。栄養素、満腹感、飽満の検出に関わる。脊髄性の求心路は高い閾値の強い刺激に反応し、膨満感、不快感、けいれん痛、切迫感、痛みを伝える。
    condition:
      criteria: Rome V（2026）
      source: Rome V 基礎科学の章
    differential: null
    common_misconception: 消化管の痛みはすべて迷走神経が伝える
  provenance:
    source_ref: SRC-151
    source: 'Greenwood-Van Meerveld B, Mawe GM, Beyder A, et al. Fundamentals of Neurogastroenterology: Basic Science. Gastroenterology 2026;170:1099-1113（Rome V）'
    doi: 10.1053/j.gastro.2026.01.040
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.040
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-005 (id: JlAKpjg)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-212
  domain: NG
  subdomain: 神経消化器病学の基礎（Rome V）
  assertion:
    plain_statement_ja: 腸管神経系の神経細胞は、内在性一次求心性ニューロン（IPAN）、運動ニューロン、介在ニューロン、腸管外へ投射するニューロンの4種に分けられる。腸管神経系の細胞の半分以上は腸管グリアである。神経から平滑筋への伝達は、カハール介在細胞、PDGFRα陽性線維芽細胞様細胞、平滑筋細胞の合胞体を介し、腸の平滑筋は一酸化窒素作動性の運動ニューロンによって持続的に抑制されている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 基礎科学の章
    differential: null
    common_misconception: 腸の運動は平滑筋だけで決まる
  provenance:
    source_ref: SRC-151
    source: 'Greenwood-Van Meerveld B, Mawe GM, Beyder A, et al. Fundamentals of Neurogastroenterology: Basic Science. Gastroenterology 2026;170:1099-1113（Rome V）'
    doi: 10.1053/j.gastro.2026.01.040
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.040
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-213
  domain: NG
  subdomain: 神経消化器病学の基礎（Rome V）
  assertion:
    plain_statement_ja: 消化管には体の免疫細胞の約75%と約1億個の神経細胞がある。肥満細胞は腸管神経のそばに多く、IBSでは肥満細胞の数が腹痛や膨満と相関し、ストレスで分泌されるCRHは肥満細胞を活性化する。幼少期のストレスはIBSの危険を約2倍にし、IBS患者の2〜4%にスクラーゼ・イソマルターゼ遺伝子の病的変異があるとされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 基礎科学の章
    differential: IBSの病態（NG-086〜089）
    common_misconception: IBSは消化管の免疫とは無関係である
  provenance:
    source_ref: SRC-151
    source: 'Greenwood-Van Meerveld B, Mawe GM, Beyder A, et al. Fundamentals of Neurogastroenterology: Basic Science. Gastroenterology 2026;170:1099-1113（Rome V）'
    doi: 10.1053/j.gastro.2026.01.040
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.040
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は章が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-005 (id: JlAKpjg)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-214
  domain: NG
  subdomain: 神経消化器病学の基礎（Rome V）
  assertion:
    plain_statement_ja: 腸のセロトニン（5-HT）の大部分は上皮の腸クロム親和性細胞がトリプトファン水酸化酵素1で作り、腸管神経はトリプトファン水酸化酵素2で作る。5-HT3受容体拮抗薬は腸の運動を遅くし痛みを和らげ、5-HT4受容体作動薬は大腸の運動を高める。5-HTはセロトニン再取り込みトランスポーター（SERT）で細胞内に取り込まれて不活化される。
    condition:
      criteria: Rome V（2026）
      source: Rome V 基礎科学の章
    differential: 5-HT3拮抗薬の臨床（NG-091、NG-042・043）
    common_misconception: 体内のセロトニンの大部分は脳で作られる
  provenance:
    source_ref: SRC-151
    source: 'Greenwood-Van Meerveld B, Mawe GM, Beyder A, et al. Fundamentals of Neurogastroenterology: Basic Science. Gastroenterology 2026;170:1099-1113（Rome V）'
    doi: 10.1053/j.gastro.2026.01.040
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.040
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-004 (id: JlAKpjc)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-215
  domain: NG
  subdomain: 神経消化器病学の基礎（Rome V）
  assertion:
    plain_statement_ja: 腸内細菌は、短鎖脂肪酸、胆汁酸、トリプトファン由来のインドールなどの代謝物や迷走神経を介して腸と脳の機能に影響する。無菌マウスでは腸管神経の数や種類の分布が変わり、消化管運動が障害される。IBSなどの患者の便を動物に移植すると、内臓痛や運動障害、不安様の行動が再現されることが報告されている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 基礎科学の章
    differential: 腸内細菌叢とプロバイオティクス（NG-034〜036）
    common_misconception: 腸内細菌は消化にしか関わらない
  provenance:
    source_ref: SRC-151
    source: 'Greenwood-Van Meerveld B, Mawe GM, Beyder A, et al. Fundamentals of Neurogastroenterology: Basic Science. Gastroenterology 2026;170:1099-1113（Rome V）'
    doi: 10.1053/j.gastro.2026.01.040
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.040
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-216
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vの小児下部消化管・胆道の腸脳相関障害は、年齢区分ではなく、腹痛障害、排便・肛門直腸障害、不快感障害の3群に分けられる。機能性ディスペプシアは上部消化管の章に移った。新しく加わったのは胆道痛症候群、中枢介在性腹痛症候群、機能性腹部膨満、消散性直腸痛で、「乳児疝痛」は「乳児苦痛症候群（infant distress syndrome）」に改められた。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: Rome IVの小児の分類（NG-080〜085）、小児上部消化管（NG-118）
    common_misconception: Rome Vでも小児の腸脳相関障害は新生児・乳幼児と小児・思春期に分けて分類する
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-217
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vの小児のIBSは、間欠的な腹痛が平均月4日以上あり、排便との関連、排便頻度の変化、便形状の変化のうち1つ以上を伴い、腹痛が主な症状で、他の疾患で説明できないものである。2か月以上続くことを求め、痛みが月経の時期だけに起こる場合は除く。6歳未満のIBSの報告がないため、診断できるのは6歳からとされた。機能性便秘との区別は、便秘を先に治療して判断するのではなく、腹痛が主かどうかで行う。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: 成人のIBS（月3日以上、NG-127）、小児の機能性便秘
    common_misconception: 小児のIBSは便秘を治療して腹痛が残るかどうかで診断する
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-218
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: 小児のIBSでは、催眠療法（最長約5年の効果）と認知行動療法の無作為化試験で効果が示され、欧州・北米の小児消化器学会のガイドラインはこの2つを第一選択としている。経皮的電気神経刺激（PENFS）は米国で小児IBSに承認された。菌株を特定したプロバイオティクス（Lactobacillus rhamnosus GGなど）、腸溶性ペパーミントオイル、サイリウムも選択肢になる。アミトリプチリンの結果は一致せず、リファキシミンはプラセボに勝らなかった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: 成人のIBSの治療（NG-135〜138）
    common_misconception: 小児のIBSには抗菌薬がよく効く
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-219
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vの小児下部消化管の章は、低FODMAP食を勧める場合、制限期（4〜6週間まで）、再導入期、個別化期の3段階で行うとしている。異常な食行動や回避・制限性食物摂取症の懸念があるため、制限食には管理栄養士が関わり、できるだけ制限を緩めることを強く勧めている。欧州・北米の小児消化器学会のガイドラインは、低FODMAP食を含む制限食を小児のIBSに提案していない。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: 成人のIBSの食事療法（NG-135）
    common_misconception: 低FODMAP食は症状が消えるまで長く続けるのがよい
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 再導入期と個別化期の期間は章に記載がない
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-220
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vの小児の「特定不能の腹痛症候群」（Rome IVの特定不能の機能性腹痛）は、食事・排便・月経のときだけではない間欠的な腹痛が平均月4日以上あり、IBS、機能性ディスペプシア、腹部片頭痛、胆道痛症候群の基準を満たさないものである。2か月以上続くことを求め、持続痛の中枢介在性腹痛症候群とは区別される。有病率は1.2%とされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: 小児の機能性腹痛（NG-085）
    common_misconception: 小児の腹痛は持続か間欠かを区別しなくてよい
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-221
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vで小児に新設された胆道痛症候群は、右上腹部（心窩部を伴ってもよい）の痛みが平均月4日以上あり、急に始まって30分以上数時間続き、間隔をおいて起こり、救急受診するほど強く、胆石などの構造的異常がないものである。超音波とMRCPで胆石を除外し、胆嚢駆出率の検査は勧められない。手術の成功率は34〜100%とばらつき、胆嚢摘出は手術以外の治療が十分に試されて効かない場合に限る。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: null
    common_misconception: 小児の胆道痛には胆嚢駆出率で手術を決める
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 手術成功率は章が引用したレビューの値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-222
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vの小児の腹部片頭痛の基準はRome IVから変わらない。有病率は約1%で7〜8歳に始まり、女児に多い。周期性嘔吐症候群と症状が重なるときは、最も強い症状で主診断を決める。頻回で生活に支障がある場合は、ピゾチフェン、シプロヘプタジン、プロプラノロール、フルナリジンなどの予防薬が考慮される。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: 成人の腹部片頭痛（NG-154）、小児の腹部片頭痛（NG-083）
    common_misconception: 小児の腹部片頭痛には承認された治療薬がある
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 小児の腹部片頭痛に米国FDAが承認した薬はない
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)；TBL-02-07-018 (id: JlAKpkQ)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-223
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vは小児にも中枢介在性腹痛症候群（CAPS）を設けた。持続する腹痛が日常生活（学校、交友、家庭、スポーツ）を制限し、他の疾患で説明できないもので、2か月以上続くことを求める。小児の疫学データがないため、成人のカテゴリーA・Bは導入されなかった。家族や学校と協力した多職種のケアと脳腸療法が強く勧められている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: 成人のCAPS（NG-150）
    common_misconception: CAPSは成人だけの病気である
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-224
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vの小児の機能性便秘は、年齢で分けない1つの基準で、最近1か月に、排便が平均週2回以下、週1回以上の便失禁（トイレトレーニング後の子ども）、便をためる姿勢・いきみ・不適切な便の我慢、痛みを伴う排便や硬便、直腸の大きな便塊、太い便のうち2つ以上があり、IBSの基準を満たさないものである。「機能性」の語は、患者や家族に受け入れられているとして残された。小児の便秘の95%超は機能性と推定されている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: Rome IVの乳幼児・小児の機能性便秘（NG-082、NG-084）
    common_misconception: 小児の便秘の多くは器質的な病気が原因である
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-021 (id: JlAKpkY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-225
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: 小児の機能性便秘の治療は、教育と行動療法（定時のトイレ、排便日誌、報酬）、食事、薬物療法で、便塊の除去と維持療法を行う。欧州・北米の小児消化器学会のガイドラインは、生後6か月を超える子どもの維持療法にポリエチレングリコールを第一選択とする。小児の試験でプラセボに勝った新しい薬はリナクロチドだけで、米国では6〜17歳に1日72 μgが承認されている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: 成人の慢性便秘症の治療（NG-142）
    common_misconception: 小児の便秘には成人の新しい便秘薬がどれも使える
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-021 (id: JlAKpkY)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-226
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vの小児の非貯留性便失禁は、トイレトレーニング後の子どもが社会的に不適切な場所で排便し、便の貯留がなく、意図的でなく、他の疾患で説明できないもので、1か月以上続くことを求める。「機能性」の語は外された。有病率は0.4%とされる。下剤は効果がなく悪化させることがあり、1日3回以上のトイレの習慣づけを行う。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: null
    common_misconception: 便を漏らす子どもにはまず下剤を使う
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-227
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vの乳児排便困難症は、生後9か月未満の乳児が、軟便を出す前に10分以上いきむもので、泣く、叫ぶ、顔が真っ赤になることが補助所見として加えられた。有病率は約4%である。下剤は通常不要で、肛門刺激は避けるよう助言する。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: null
    common_misconception: 乳児がいきんで泣くのは便秘なので浣腸が必要である
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-011 (id: JlAKpj4)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-228
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vの小児の機能性下痢は、4歳未満では1日4回以上、4歳以上では1日2回を超える痛みのない排便があり、25%以上が不定形便で、生後6か月から18歳の間に始まり、機能性便秘、下痢型IBS、非貯留性便失禁の基準を満たさないものである。対象年齢が18歳まで広げられ、2か月以上続くことを求める。有病率は約2%とされる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: 成人の機能性下痢（NG-143）
    common_misconception: 小児の機能性下痢は乳幼児だけの病気である
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-022 (id: JlAKpkc)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-229
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vで小児に新設された機能性腹部膨満は、間欠的な膨満感や腹部膨隆が平均月4日以上あって他の症状より目立ち、IBS、機能性便秘、機能性下痢、空気嚥下症、食後愁訴症候群の基準を満たさないものである。消散性直腸痛も成人の基準を取り入れて小児に設けられ、思春期の有病率は1.8%と報告されている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: 成人の機能性腹部膨満（NG-145）、成人の消散性直腸痛（NG-163）
    common_misconception: 腹部膨満や直腸痛の腸脳相関障害は成人にしかない
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-024 (id: JlAKpko)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-230
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: Rome Vは「乳児疝痛（infant colic）」を「乳児苦痛症候群（infant distress syndrome）」に改めた。「疝痛」は大腸由来の痛みを示唆するが、それは証明されていないためである。臨床用の基準は、生後5か月未満で始まり、明らかな原因がなく養育者が防いだり止めたりできない長い泣きとぐずりが繰り返し、他の疾患で説明できないことである。研究用には、さらに生後6週までは1日3時間超、それ以降は2.5時間超（年齢の75パーセンタイル）の泣きが週3日以上あるか、養育者の少なくとも1人の生活と健康に重大な影響があることを求める。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: Rome IVの乳児疝痛（NG-081）
    common_misconception: 乳児の激しい泣きは大腸の痛みが原因である
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: Rome IVの「生後5か月までに症状が止まる」という条件は改められた
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-231
  domain: NG
  subdomain: Rome V 小児下部消化管・胆道
  assertion:
    plain_statement_ja: 生後3か月までの乳児のぐずりと泣きは平均1日1〜2時間とされる。発熱のない激しい泣きの乳児で器質的な原因があるのは少数で、尿の検査を行う。乳児苦痛症候群の対応の中心は、症状と親の負担を受け止め、子どもが健康で自然に治まることを説明することである。Limosilactobacillus reuteriは1日の泣きを約65分減らしたとされる。母親の不安は発症に先行し、抑うつは泣きと悪循環をつくる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 小児下部消化管・胆道の章
    differential: null
    common_misconception: 乳児の激しい泣きには胃酸を抑える薬が効く
  provenance:
    source_ref: SRC-152
    source: 'Di Lorenzo C, Saps M, Chumpitazi BP, et al. Lower and Biliary Disorders of Gut–Brain Interaction: Child and Adolescent. Gastroenterology 2026;170:1367-1387（Rome V）'
    doi: 10.1053/j.gastro.2026.01.036
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.01.036
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: プロバイオティクスの値は章が引用した研究による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-232
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vは腸脳相関障害（DGBI）を、消化管運動の障害、内臓知覚過敏、粘膜・免疫機能の変化、腸内細菌叢の変化、中枢神経系の処理の変化のいずれかの組み合わせに関係する消化管症状を特徴とする疾患群と定義している。「機能性消化管疾患（FGID）」という用語はもう使わないよう勧めている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 序論
    differential: Rome IVの概念（NG-001）
    common_misconception: 腸脳相関障害は心の問題であって、体の異常はない
  provenance:
    source_ref: SRC-153
    source: Drossman DA, Chang L, Tack J. Disorders of Gut–Brain Interaction and the Rome V Process. Gastroenterology 2026;170:1083-1098
    doi: 10.1053/j.gastro.2026.02.014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.014
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)；TBL-02-07-005 (id: JlAKpjg)；TBL-02-07-015 (id: JlAKpkI)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-233
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vは成人34、小児22の腸脳相関障害を定めている。作成には2019年に共同上級編集者が選ばれてから2026年の刊行まで7年をかけ、27か国の144人が25の委員会に参加した。
    condition:
      criteria: Rome V（2026）
      source: Rome V 序論
    differential: Rome IVの分類（成人33、小児17、NG-002）
    common_misconception: Rome Vの疾患数はRome IVと同じである
  provenance:
    source_ref: SRC-153
    source: Drossman DA, Chang L, Tack J. Disorders of Gut–Brain Interaction and the Rome V Process. Gastroenterology 2026;170:1083-1098
    doi: 10.1053/j.gastro.2026.02.014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.014
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: NG-110（Rome Foundation の概要）と同じ内容を原典で確認
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-234
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Foundationは、研究用の基準とは別に、診療で使う「臨床用基準」を定めた。Rome Vの診断基準の症状の質的な特徴を満たし、受診したり生活に支障が出たりするほど症状が煩わしければよく、頻度は従来の閾値より低くてもよい。6か月の期間は求めず、他の疾患を除外するために8週間の経過を勧める。ただし、診察で他の疾患が除外できたと判断できる場合や、周期性嘔吐症候群や消散性直腸痛のように発作がまれな疾患は例外とする。診療では研究用の基準より臨床用基準を使うよう勧めている。
    condition:
      criteria: Rome V（2026）
      source: Rome V 序論
    differential: 研究用の基準（6か月以上前の発症、最近3か月）
    common_misconception: Rome基準を満たすまで6か月待たないと腸脳相関障害と診断できない
  provenance:
    source_ref: SRC-153
    source: Drossman DA, Chang L, Tack J. Disorders of Gut–Brain Interaction and the Rome V Process. Gastroenterology 2026;170:1083-1098
    doi: 10.1053/j.gastro.2026.02.014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.014
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-235
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: 5万人を超える世界の調査では、41.4%が1つ以上の腸脳相関障害のRome基準を満たし、33.4%は消化管症状がなかった。残りの約4分の1は症状があるのに基準を満たさない「診断閾値下」の群で、症状のない人より生活の質が低く、不安・抑うつ、受診、仕事や生活の障害が多かった。臨床用基準は、こうした人を診断し治療するために設けられた。
    condition:
      criteria: Rome V（2026）
      source: Rome V 序論
    differential: null
    common_misconception: Rome基準を満たさない消化管症状は治療しなくてよい
  provenance:
    source_ref: SRC-153
    source: Drossman DA, Chang L, Tack J. Disorders of Gut–Brain Interaction and the Rome V Process. Gastroenterology 2026;170:1083-1098
    doi: 10.1053/j.gastro.2026.02.014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.014
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は序論が引用した調査による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-236
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: 3か国の成人5,931人の調査では、35%が1つの腸脳相関障害の基準を満たし、そのうち3分の1を超える人が別の部位の腸脳相関障害を1つ以上合併していた。合併が多いほど心身の生活の質が低く、治療や腹部手術を多く受けていた。5万4千人を超える調査では37.5%に心理的苦痛や身体症状があり、腸脳相関障害をもつオッズが4.45倍だった。
    condition:
      criteria: Rome V（2026）
      source: Rome V 序論
    differential: null
    common_misconception: 腸脳相関障害は1人に1つしか起こらない
  provenance:
    source_ref: SRC-153
    source: Drossman DA, Chang L, Tack J. Disorders of Gut–Brain Interaction and the Rome V Process. Gastroenterology 2026;170:1083-1098
    doi: 10.1053/j.gastro.2026.02.014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.014
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は序論が引用した調査による（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)；TBL-01-00-257 (id: Jlvnl3Q)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-237
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vの胆嚢・Oddi括約筋の委員会は、典型的な胆道痛の定義を簡素化した。胆嚢機能障害では、典型的な胆道痛のほうが胆嚢摘出術の効果をよく予測するとして、胆嚢駆出率を調べる胆道シンチグラフィーは勧めなくなった。症状が一過性なら手術ではなく経過観察を勧め、Oddi括約筋障害の補助基準から括約筋内圧測定を外した。
    condition:
      criteria: Rome V（2026）
      source: Rome V 序論
    differential: 小児の胆道痛症候群（NG-221）
    common_misconception: 胆嚢駆出率が低ければ胆嚢摘出術を行う
  provenance:
    source_ref: SRC-153
    source: Drossman DA, Chang L, Tack J. Disorders of Gut–Brain Interaction and the Rome V Process. Gastroenterology 2026;170:1083-1098
    doi: 10.1053/j.gastro.2026.02.014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.014
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 成人の胆嚢・Oddi括約筋の章そのものは未入手で、序論の要約による
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-238
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vの序論はIBSの重症度の目安を示している。軽症は約40%（IBS-SSS 75〜175）で教育、安心させる説明、食事の調整を行う。中等症は約35%（176〜300）で1〜3週間の症状日誌、症状に応じた薬、脳腸行動療法を加える。重症は約25%（300超）で、短い受診を繰り返す継続的な関係、中枢性神経調節薬、多職種の治療施設への紹介が勧められる。
    condition:
      criteria: Rome V（2026）
      source: Rome V 序論
    differential: Rome V の心理社会的ケアの3段階（NG-166）
    common_misconception: IBSの治療は重症度にかかわらず同じである
  provenance:
    source_ref: SRC-153
    source: Drossman DA, Chang L, Tack J. Disorders of Gut–Brain Interaction and the Rome V Process. Gastroenterology 2026;170:1083-1098
    doi: 10.1053/j.gastro.2026.02.014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.014
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-269 (id: Jlvnl34)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-239
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: Rome Vの序論は、治療的な医師患者関係を築くための12のステップを示している。患者中心の非指示的な面接、受診の直接の理由の把握、丁寧な身体診察、患者の病気の理解の確認と説明、現実的な期待への対応、ストレスと症状の結びつけ、一貫した限度の設定、治療への患者の参加、継続的な関係の構築などである。患者の満足度は、医師の人間味、技術、心理社会的要因への関心、情報提供と関連する。
    condition:
      criteria: Rome V（2026）
      source: Rome V 序論
    differential: null
    common_misconception: 腸脳相関障害の診療では検査を繰り返すことが患者の安心につながる
  provenance:
    source_ref: SRC-153
    source: Drossman DA, Chang L, Tack J. Disorders of Gut–Brain Interaction and the Rome V Process. Gastroenterology 2026;170:1083-1098
    doi: 10.1053/j.gastro.2026.02.014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.014
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
- id: NG-240
  domain: NG
  subdomain: Rome V（2026）
  assertion:
    plain_statement_ja: 脳は下行性の疼痛調節（ゲートコントロール）によって内臓からの痛みの信号を強めたり弱めたりし、腸脳相関障害ではこの抑制が損なわれていることが多い。この調節にはセロトニンとノルアドレナリンが関わり、三環系抗うつ薬やSNRIの標的になっている。前帯状回はIBSなどで機能異常を示すことが多い。
    condition:
      criteria: Rome V（2026）
      source: Rome V 序論
    differential: 基礎科学（NG-211〜215）、脳機能画像（NG-088）
    common_misconception: 腸の痛みの強さは腸の異常の程度だけで決まる
  provenance:
    source_ref: SRC-153
    source: Drossman DA, Chang L, Tack J. Disorders of Gut–Brain Interaction and the Rome V Process. Gastroenterology 2026;170:1083-1098
    doi: 10.1053/j.gastro.2026.02.014
    pmid: null
    pmcid: null
    url: https://doi.org/10.1053/j.gastro.2026.02.014
    source_license: CC BY-NC-ND 4.0（© 2026 The Author(s)、AGA Institute）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-02-07-005 (id: JlAKpjg)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: null
  publication_info:
    created: '2026-10-18'
    verifier: null
    verified_at: null
    status: draft
```

## 5. カード一覧

| ID | サブ領域 | SRC |
|---|---|---|
| NG-001 | 腸脳相関病（DGBI）の概念と分類 | SRC-100 |
| NG-002 | 腸脳相関病（DGBI）の概念と分類 | SRC-100 |
| NG-003 | 腸脳相関病（DGBI）の概念と分類 | SRC-100 |
| NG-004 | 日本神経消化器病学会 | SRC-101 |
| NG-005 | 日本神経消化器病学会 | SRC-101 |
| NG-006 | DGBIの疫学 | SRC-102 |
| NG-007 | DGBIの疫学 | SRC-102 |
| NG-008 | DGBIの疫学 | SRC-102 |
| NG-009 | DGBIの疫学 | SRC-102 |
| NG-010 | DGBIの疫学 | SRC-102 |
| NG-011 | 胃不全麻痺 | SRC-103 |
| NG-012 | 胃不全麻痺 | SRC-103 |
| NG-013 | 胃不全麻痺 | SRC-104 |
| NG-014 | 胃不全麻痺 | SRC-105 |
| NG-015 | 胃不全麻痺 | SRC-105 |
| NG-016 | 周期性嘔吐症候群 | SRC-106 |
| NG-017 | 周期性嘔吐症候群 | SRC-106 |
| NG-018 | 周期性嘔吐症候群 | SRC-107 |
| NG-019 | 便失禁 | SRC-108 |
| NG-020 | 便失禁 | SRC-108 |
| NG-021 | 便失禁 | SRC-109 |
| NG-022 | 慢性偽性腸閉塞症 | SRC-110 |
| NG-023 | 慢性偽性腸閉塞症 | SRC-110 |
| NG-024 | 慢性偽性腸閉塞症 | SRC-110 |
| NG-025 | 慢性偽性腸閉塞症 | SRC-110 |
| NG-026 | 慢性偽性腸閉塞症 | SRC-110 |
| NG-027 | ヒルシュスプルング病 | SRC-111 |
| NG-028 | ヒルシュスプルング病 | SRC-111 |
| NG-029 | ヒルシュスプルング病 | SRC-111 |
| NG-030 | ヒルシュスプルング病 | SRC-111 |
| NG-031 | IBSと腸脳相関 | SRC-112 |
| NG-032 | IBSと腸脳相関 | SRC-113 |
| NG-033 | IBSと腸脳相関 | SRC-113 |
| NG-034 | 腸内細菌叢とプロバイオティクス | SRC-114 |
| NG-035 | 腸内細菌叢とプロバイオティクス | SRC-114 |
| NG-036 | 腸内細菌叢とプロバイオティクス | SRC-114 |
| NG-037 | 腸脳相関病（DGBI）の概念と分類 | SRC-126 |
| NG-038 | 腸脳相関病（DGBI）の概念と分類 | SRC-125 |
| NG-039 | DGBIの国内承認薬 | SRC-115 |
| NG-040 | DGBIの国内承認薬 | SRC-115 |
| NG-041 | DGBIの国内承認薬 | SRC-115 |
| NG-042 | DGBIの国内承認薬 | SRC-116 |
| NG-043 | DGBIの国内承認薬 | SRC-116 |
| NG-044 | DGBIの国内承認薬 | SRC-117 |
| NG-045 | DGBIの国内承認薬 | SRC-118 |
| NG-046 | DGBIの国内承認薬 | SRC-119 |
| NG-047 | DGBIの国内承認薬 | SRC-120 |
| NG-048 | げっぷ障害・反芻症候群 | SRC-122 |
| NG-049 | げっぷ障害・反芻症候群 | SRC-122 |
| NG-050 | げっぷ障害・反芻症候群 | SRC-122 |
| NG-051 | げっぷ障害・反芻症候群 | SRC-122 |
| NG-052 | 直腸肛門機能検査 | SRC-121 |
| NG-053 | 直腸肛門機能検査 | SRC-121 |
| NG-054 | 腸内細菌叢とプロバイオティクス | SRC-123 |
| NG-055 | 腸内細菌叢とプロバイオティクス | SRC-123 |
| NG-056 | 神経疾患と消化管機能 | SRC-124 |
| NG-057 | 神経疾患と消化管機能 | SRC-124 |
| NG-058 | 機能性食道疾患 | SRC-127 |
| NG-059 | 機能性食道疾患 | SRC-127 |
| NG-060 | 機能性食道疾患 | SRC-127 |
| NG-061 | 機能性食道疾患 | SRC-127 |
| NG-062 | 機能性食道疾患 | SRC-127 |
| NG-063 | 機能性食道疾患 | SRC-127 |
| NG-064 | 機能性ディスペプシアのRome IV分類 | SRC-128 |
| NG-065 | 悪心・嘔吐症 | SRC-128 |
| NG-066 | 周期性嘔吐症候群 | SRC-128 |
| NG-067 | 周期性嘔吐症候群 | SRC-128 |
| NG-068 | げっぷ障害・反芻症候群 | SRC-128 |
| NG-069 | 機能性腸疾患（Rome IV） | SRC-129 |
| NG-070 | 機能性腸疾患（Rome IV） | SRC-129 |
| NG-071 | 機能性腸疾患（Rome IV） | SRC-129 |
| NG-072 | 機能性腸疾患（Rome IV） | SRC-129 |
| NG-073 | 機能性腸疾患（Rome IV） | SRC-129 |
| NG-074 | 中枢介在性の消化管の痛み | SRC-130 |
| NG-075 | 中枢介在性の消化管の痛み | SRC-130 |
| NG-076 | 中枢介在性の消化管の痛み | SRC-130 |
| NG-077 | 機能性肛門直腸疾患 | SRC-131 |
| NG-078 | 機能性肛門直腸疾患 | SRC-131 |
| NG-079 | 機能性肛門直腸疾患 | SRC-131 |
| NG-080 | 小児の機能性消化管疾患 | SRC-132 |
| NG-081 | 小児の機能性消化管疾患 | SRC-132 |
| NG-082 | 小児の機能性消化管疾患 | SRC-132 |
| NG-083 | 小児の機能性消化管疾患 | SRC-133 |
| NG-084 | 小児の機能性消化管疾患 | SRC-133 |
| NG-085 | 小児の機能性消化管疾患 | SRC-133 |
| NG-086 | IBSの病態（日本のGL） | SRC-134 |
| NG-087 | IBSの病態（日本のGL） | SRC-134 |
| NG-088 | IBSの病態（日本のGL） | SRC-134 |
| NG-089 | IBSの病態（日本のGL） | SRC-134 |
| NG-090 | IBSの治療（日本のGL） | SRC-134 |
| NG-091 | IBSの治療（日本のGL） | SRC-134 |
| NG-092 | IBSの治療（日本のGL） | SRC-134 |
| NG-093 | IBSの治療（日本のGL） | SRC-134 |
| NG-094 | IBSの治療（日本のGL） | SRC-134 |
| NG-095 | IBSの治療（日本のGL） | SRC-134 |
| NG-096 | IBSの治療（日本のGL） | SRC-134 |
| NG-097 | IBSの治療（日本のGL） | SRC-134 |
| NG-098 | IBSの治療（日本のGL） | SRC-134 |
| NG-099 | 慢性便秘症（日本の便通異常症GL） | SRC-135 |
| NG-100 | 慢性便秘症（日本の便通異常症GL） | SRC-135 |
| NG-101 | 慢性便秘症（日本の便通異常症GL） | SRC-135 |
| NG-102 | 慢性便秘症（日本の便通異常症GL） | SRC-135 |
| NG-103 | 慢性便秘症（日本の便通異常症GL） | SRC-135 |
| NG-104 | 慢性便秘症（日本の便通異常症GL） | SRC-135 |
| NG-105 | 慢性便秘症（日本の便通異常症GL） | SRC-135 |
| NG-106 | 慢性便秘症（日本の便通異常症GL） | SRC-135 |
| NG-107 | 慢性便秘症（日本の便通異常症GL） | SRC-135 |
| NG-108 | 慢性便秘症（日本の便通異常症GL） | SRC-135 |
| NG-109 | 消化管機能検査 | SRC-136 |
| NG-110 | Rome V（2026） | SRC-137 |
| NG-111 | Rome V（2026） | SRC-138 |
| NG-112 | Rome V（2026） | SRC-139 |
| NG-113 | Rome V（2026） | SRC-137 |
| NG-114 | Rome V（2026） | SRC-137 |
| NG-115 | Rome V（2026） | SRC-137 |
| NG-116 | Rome V（2026） | SRC-137 |
| NG-117 | Rome V（2026） | SRC-137 |
| NG-118 | Rome V 小児上部消化管 | SRC-140 |
| NG-119 | Rome V 小児上部消化管 | SRC-140 |
| NG-120 | Rome V 小児上部消化管 | SRC-140 |
| NG-121 | Rome V 小児上部消化管 | SRC-140 |
| NG-122 | Rome V 小児上部消化管 | SRC-140 |
| NG-123 | Rome V（2026） | SRC-141 |
| NG-124 | Rome V（2026） | SRC-142 |
| NG-125 | Rome V（2026） | SRC-142 |
| NG-126 | Rome V 腸疾患 | SRC-143 |
| NG-127 | Rome V 腸疾患 | SRC-143 |
| NG-128 | Rome V 腸疾患 | SRC-143 |
| NG-129 | Rome V 腸疾患 | SRC-143 |
| NG-130 | Rome V 腸疾患 | SRC-143 |
| NG-131 | Rome V 腸疾患 | SRC-143 |
| NG-132 | Rome V 腸疾患 | SRC-143 |
| NG-133 | Rome V 腸疾患 | SRC-143 |
| NG-134 | Rome V 腸疾患 | SRC-143 |
| NG-135 | Rome V 腸疾患 | SRC-143 |
| NG-136 | Rome V 腸疾患 | SRC-143 |
| NG-137 | Rome V 腸疾患 | SRC-143 |
| NG-138 | Rome V 腸疾患 | SRC-143 |
| NG-139 | Rome V 腸疾患 | SRC-143 |
| NG-140 | Rome V 腸疾患 | SRC-143 |
| NG-141 | Rome V 腸疾患 | SRC-143 |
| NG-142 | Rome V 腸疾患 | SRC-143 |
| NG-143 | Rome V 腸疾患 | SRC-143 |
| NG-144 | Rome V 腸疾患 | SRC-143 |
| NG-145 | Rome V 腸疾患 | SRC-143 |
| NG-146 | Rome V 腸疾患 | SRC-143 |
| NG-147 | Rome V 腸疾患 | SRC-143 |
| NG-148 | Rome V 腸疾患 | SRC-143 |
| NG-149 | Rome V 中枢介在性の消化管の痛み | SRC-144 |
| NG-150 | Rome V 中枢介在性の消化管の痛み | SRC-144 |
| NG-151 | Rome V 中枢介在性の消化管の痛み | SRC-144 |
| NG-152 | Rome V 中枢介在性の消化管の痛み | SRC-144 |
| NG-153 | Rome V 中枢介在性の消化管の痛み | SRC-144 |
| NG-154 | Rome V 中枢介在性の消化管の痛み | SRC-144 |
| NG-155 | Rome V 中枢介在性の消化管の痛み | SRC-144 |
| NG-156 | Rome V 中枢介在性の消化管の痛み | SRC-144 |
| NG-157 | Rome V 中枢介在性の消化管の痛み | SRC-144 |
| NG-158 | Rome V 肛門直腸疾患 | SRC-145 |
| NG-159 | Rome V 肛門直腸疾患 | SRC-145 |
| NG-160 | Rome V 肛門直腸疾患 | SRC-145 |
| NG-161 | Rome V 肛門直腸疾患 | SRC-145 |
| NG-162 | Rome V 肛門直腸疾患 | SRC-145 |
| NG-163 | Rome V 肛門直腸疾患 | SRC-145 |
| NG-164 | Rome V 肛門直腸疾患 | SRC-145 |
| NG-165 | Rome V 肛門直腸疾患 | SRC-145 |
| NG-166 | Rome V 生物心理社会的ケア | SRC-146 |
| NG-167 | Rome V 生物心理社会的ケア | SRC-146 |
| NG-168 | Rome V 生物心理社会的ケア | SRC-146 |
| NG-169 | Rome V 生物心理社会的ケア | SRC-146 |
| NG-170 | Rome V 診断質問票 | SRC-147 |
| NG-171 | Rome V 診断質問票 | SRC-147 |
| NG-172 | Rome V 診断質問票 | SRC-147 |
| NG-173 | Rome V 診断質問票 | SRC-147 |
| NG-174 | Rome V 診断質問票 | SRC-147 |
| NG-175 | Rome V 診断質問票 | SRC-147 |
| NG-176 | Rome V 診断質問票 | SRC-147 |
| NG-177 | Rome V 小児上部消化管 | SRC-140 |
| NG-178 | 慢性下痢症（日本の便通異常症GL） | SRC-148 |
| NG-179 | 慢性下痢症（日本の便通異常症GL） | SRC-148 |
| NG-180 | 慢性下痢症（日本の便通異常症GL） | SRC-148 |
| NG-181 | 慢性下痢症（日本の便通異常症GL） | SRC-148 |
| NG-182 | 慢性下痢症（日本の便通異常症GL） | SRC-148 |
| NG-183 | 慢性下痢症（日本の便通異常症GL） | SRC-148 |
| NG-184 | 慢性下痢症（日本の便通異常症GL） | SRC-148 |
| NG-185 | 慢性下痢症（日本の便通異常症GL） | SRC-148 |
| NG-186 | Rome V 食道疾患 | SRC-149 |
| NG-187 | Rome V 食道疾患 | SRC-149 |
| NG-188 | Rome V 食道疾患 | SRC-149 |
| NG-189 | Rome V 食道疾患 | SRC-149 |
| NG-190 | Rome V 食道疾患 | SRC-149 |
| NG-191 | Rome V 食道疾患 | SRC-149 |
| NG-192 | Rome V 食道疾患 | SRC-149 |
| NG-193 | Rome V 食道疾患 | SRC-149 |
| NG-194 | Rome V 食道疾患 | SRC-149 |
| NG-195 | Rome V 食道疾患 | SRC-149 |
| NG-196 | Rome V 食道疾患 | SRC-149 |
| NG-197 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-198 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-199 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-200 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-201 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-202 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-203 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-204 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-205 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-206 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-207 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-208 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-209 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-210 | Rome V 胃十二指腸疾患 | SRC-150 |
| NG-211 | 神経消化器病学の基礎（Rome V） | SRC-151 |
| NG-212 | 神経消化器病学の基礎（Rome V） | SRC-151 |
| NG-213 | 神経消化器病学の基礎（Rome V） | SRC-151 |
| NG-214 | 神経消化器病学の基礎（Rome V） | SRC-151 |
| NG-215 | 神経消化器病学の基礎（Rome V） | SRC-151 |
| NG-216 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-217 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-218 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-219 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-220 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-221 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-222 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-223 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-224 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-225 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-226 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-227 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-228 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-229 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-230 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-231 | Rome V 小児下部消化管・胆道 | SRC-152 |
| NG-232 | Rome V（2026） | SRC-153 |
| NG-233 | Rome V（2026） | SRC-153 |
| NG-234 | Rome V（2026） | SRC-153 |
| NG-235 | Rome V（2026） | SRC-153 |
| NG-236 | Rome V（2026） | SRC-153 |
| NG-237 | Rome V（2026） | SRC-153 |
| NG-238 | Rome V（2026） | SRC-153 |
| NG-239 | Rome V（2026） | SRC-153 |
| NG-240 | Rome V（2026） | SRC-153 |

国試出題基準の番号は、機能性ディスペプシア（Ⅵ-2-B-①）以外は手元の番号表に該当がなく、`null` にしています。IBS・便秘・CIPO・ヒルシュスプルング病は Ⅵ-3 や小児科の項目に当たる可能性があるので、Phase 4 で PDF から対応づけてください。

## 6. なお残っている要素（第1節の ×）

今回の補完で、9区分の大半は事実票で埋まりました。残りは次の要素です。いずれも、取得できる一次資料が見つからなかったか、学会の診療体制に関わる内容です。

- 検査：胃バロスタット、飲水負荷試験、ティッシュコンダクタンスメーター（粘膜透過性）、肛門筋電図、Timed Barium Esophagram
- 分子：脳腸ペプチド（モチリン、グレリン、オレキシンなど）、タイトジャンクション蛋白、遺伝子多型（GNB3 C825T など）。カハール介在細胞は Rome V 基礎科学の章で NG-212 に入れた
- 治療：自律訓練法、EMDR、G-POEM、PEG-J
- 診療体制：心療内科・精神科との連携、移行期医療、多職種チーム

診療体制の要素は、学会の取り組み（認定医制度、市民公開講座など）を広報の側で書く内容でもあります。事実票にする場合は、学会事務局の資料を出典にするのが確実です。

これらには ID を割り当てていないため、欠番は生じていません。

## 7. Claude Code での照合時に重点的に確認する点

1. **スキーマと CLAUDE.md の更新**：NG の追加（上記）。人間の承認を得てからコミットする。
2. **識別子**：SRC-100・102 の PMID・PMCID を DOI から取得する。ライセンスを Crossref で確認する（SRC-102 は CC BY-NC-ND の表示あり）。
3. **孫引き数値**（uncertainty に「二次資料経由」と記載）：NG-023・NG-025・NG-030・NG-048・NG-049・NG-050・NG-051・NG-059・NG-060・NG-061・NG-062・NG-063・NG-064・NG-065・NG-066・NG-067・NG-071・NG-072・NG-073・NG-074・NG-076・NG-077・NG-079・NG-080・NG-081・NG-082・NG-083・NG-084・NG-085・NG-088・NG-089・NG-094・NG-095・NG-109・NG-123・NG-124・NG-125・NG-128・NG-131・NG-132・NG-133・NG-134・NG-135・NG-140・NG-146・NG-147・NG-151・NG-156・NG-157・NG-160・NG-162・NG-177・NG-189・NG-190・NG-193・NG-194・NG-195・NG-196・NG-202・NG-203・NG-206・NG-210・NG-213・NG-221・NG-231・NG-235・NG-236。指定難病の資料が引用した全国調査の値なので、原典の報告書と照合する。
4. **NG-010 と IN-017・IN-029**：同じ数値の一次資料と二次資料の関係。corroboration に記録済み。IN 側の uncertainty（二次資料経由）を「NG-010 で一次資料を確認済み」に更新する提案を `proposals/` に出す。
5. **NG-004・005（学会の沿革）**：広報で使うので、学会事務局に事実確認を依頼する。
6. **便通異常症 GL 2023 のカード**：NG-099〜108 は刊行版で照合済み（uncertainty に頁を記録）。history にも照合の記録を残す。NG-178〜185（慢性下痢症）の頁は印刷頁。
7. **IBS 診療 GL 2020 日本語版と英語版の関係**：NG-086〜098（SRC-134）と IN-017〜026（SRC-049）は同じガイドラインの別の版。sources.yaml で関連づける。NG-097 の抗アレルギー薬の具体的な薬剤名を本文で確認する。
8. **添付文書のカード**：NG-039〜047 は改訂年月を source に記載した。改訂があれば差し替えを提案する。NG-041 の臨床成績は原著論文と照合する。
9. **米国の情報のカード**：NG-011〜015（胃不全麻痺）、NG-016〜018（周期性嘔吐症候群）、NG-019〜021（便失禁）、NG-031〜033（IBS）、NG-034〜036（プロバイオティクス）、NG-054・055（FMT）。日本の承認・保険適用は添付文書で確認し、日本の資料への差し替えを補完ラウンドで検討する。

## 8. 広報で使うときの注意

- 事実票は専門職向けの命題です。一般向けの広報文は、事実票を材料に別の工程で書き起こしてください。その際も各文にカードIDを付けておくと、監修と訂正が容易になります。
- 先生ご自身が関わったガイドライン（機能性ディスペプシアなど）を出典とするカードを広報に使う場合は、利益相反の表示を学会の規程に沿って付けてください。
- 次の SRC 番号は SRC-154 からです（第6回 AB も SRC-154 から振る）。

## 9. Rome V への対応（2026-10-18、NG-110〜125、NG-126〜177、NG-186〜240）

Rome V は 2026年6月に公表され、要約論文が Gastroenterology 2026;170 に掲載されました。対応は2段階で行いました。

- **第1段階（NG-110〜125）**：いただいた改訂のまとめを、Rome Foundation の公式ページ、小児上部消化管の章、二次資料で照合した。
- **第2段階（NG-126〜177）**：先生から提供いただいた原本6本で照合・追加した。対象は腸疾患（SRC-143）、中枢介在性の痛み（SRC-144）、肛門直腸疾患（SRC-145）、生物心理社会的側面（SRC-146）、診断質問票（SRC-147）、小児上部消化管（SRC-140、補足）。
- **第3段階（NG-186〜215）**：追加で提供いただいた食道（SRC-149）、胃十二指腸（SRC-150）、基礎科学（SRC-151）の3章で照合・追加した。
- **第4段階（NG-216〜231）**：小児下部消化管・胆道（SRC-152）の章で照合・追加した。同時にいただいた腸疾患と質問票の章は、前回と同じ内容でした。
- **第5段階（NG-232〜240）**：序論（SRC-153）で照合・追加した。

全カードの condition に `criteria: Rome V（2026）` を入れています。腸疾患と胃十二指腸の章は **CC BY 4.0** なので `OPEN`、ほかの章は CC BY-NC-ND 4.0 なので `RESTRICTED` です。基準文は転載せず、要件の骨子と数値を自作文で書いています。

### 9-1. 既存カード（Rome IV）の扱い

ID 不変の原則に従い、Rome IV のカードは書き換えていません。Rome IV の基準として正しい命題なので、condition（`criteria: Rome IV（2016）`）で区別して残します。Claude Code では次の対応関係を `proposals/` に出し、各カードの `differential` か `related` に Rome V 側の ID を加えることを提案してください。

| Rome IV のカード | 内容 | Rome V での変更 | 対応する新カード |
|---|---|---|---|
| NG-001〜003 | DGBI の概念、8群の分類、新設疾患 | DGBI の定義、成人34・小児22疾患、「機能性」の扱い、研究用と臨床用の基準、新規疾患 | NG-113、114、116、126、232〜234 |
| NG-037 | Rome IV の章構成 | 18本の論文構成 | NG-110〜112 |
| NG-006〜010 | Rome IV の世界調査 | Rome V の15か国調査（全体 42.2%、IBS 8.9%） | NG-172、173 |
| NG-058〜063 | 機能性食道疾患 | Lyon 2.0・Chicago v4.0 との正式な統合、8週間の最適化した酸分泌抑制療法の要件、機能性胸痛の生検は食事関連時のみ、胃粘膜異所があれば食道球としない、FLIP の位置づけ | NG-124、186〜196 |
| NG-064 | FD の PDS・EPS | PDS は週2日以上（Rome IV は週3日）、食後は2時間以内、PDS がある場合の食後の心窩部痛は PDS に含める、食事関連 EPS の暫定基準 | NG-121、197〜204 |
| NG-065〜067 | 慢性悪心嘔吐症候群、周期性嘔吐症候群、カンナビノイド悪阻 | 悪心は週2日以上、周期性嘔吐の発作間の軽い症状を許容、大麻の使用量の基準と6か月以上の断麻 | NG-119、122、205〜207 |
| NG-068 | げっぷ障害・反芻 | げっぷができない症候群の新設、反芻は悪心・えずきがないことを基準に移動 | NG-116、118、122、170、208〜210 |
| NG-069 | 機能性腸疾患の分類 | 6群に再編、機能性便秘→慢性便秘症、特定不能→分類不能 | NG-126 |
| NG-070 | IBS の基準（週1日以上の腹痛） | 腹部不快感の復活、月3日以上、持続痛の除外、月経の補助基準 | NG-127〜129 |
| NG-071 | 機能性下痢 | 「便秘薬なしでは硬便がまれ」の条件を追加 | NG-143、144 |
| NG-072 | 機能性腹部膨満 | 基準の骨子は同じ（週1日以上、PDS を除外） | NG-145、146 |
| NG-073 | オピオイド誘発性便秘 | 6項目のうち2つ以上、下剤なしでは軟便がまれ | NG-148 |
| NG-074・076 | CAPS とその治療 | 「ほぼ」を削除、カテゴリーA・Bの新設、身体所見 | NG-150〜153 |
| NG-075 | 麻薬性腸症候群 | Rome IV から既存。基準を3項目のうち2つ以上に整理 | NG-156、157 |
| NG-077〜079 | 機能性肛門直腸痛、機能性排便障害 | 「機能性」を削除、排便協調障害は検査1つで probable・2つで definite、感覚機能障害の新設 | NG-158、161〜165 |
| NG-019〜021 | 便失禁（米国 NIDDK） | 2回以上・月1回以上（4週間の日誌）、臨床では12か月に2回以上 | NG-159、160、173 |
| NG-080〜085 | 小児の機能性消化管疾患（年齢区分） | 解剖学的領域による再編、小児上部の G1〜G3、小児下部の3群（腹痛・排便・不快感）、乳児疝痛→乳児苦痛症候群、胆道痛症候群・CAPS・機能性腹部膨満・消散性直腸痛の新設、小児 IBS は月4日以上・6歳から | NG-117〜122、174〜177、216〜231 |
| NG-083 | 小児の腹部片頭痛 | 成人の腹部片頭痛の新設 | NG-116、154、155 |
| NG-093・094 | 日本の IBS GL の神経調節薬・心理療法 | 統合ケアの3段階、腸脳神経調節薬という呼び方 | NG-136、138、166〜169 |
| IN-017〜026、NG-086〜098 | 日本の IBS 診療 GL（Rome IV を採用） | GL の改訂までは Rome IV 基準のまま | NG-127（参考） |

### 9-2. 国際基準（Rome V）と日本のガイドラインの違い

広報や教材で「現在の基準」と書くときは、次の違いを明示してください。どちらも誤りではなく、対象と目的が違います。

| 論点 | Rome V（2026） | 日本の便通異常症 GL 2023 |
|---|---|---|
| 刺激性下剤 | 習慣性や大腸の障害の根拠はない（NG-142） | 必要最小限・頓用・短期間にとどめる（NG-103） |
| 大腸通過時間検査 | 排便障害を除外した後、治療抵抗例で考慮（NG-141） | 放射線不透過マーカー法を推奨（強い推奨、NG-102） |
| 慢性下痢の期間 | 機能性下痢は発症6か月以上・最近3か月（NG-143） | 慢性下痢症は4週間以上（NG-178、NG-180） |
| 下痢型 IBS との関係 | 機能性下痢は下痢型 IBS の基準を満たさない | 慢性下痢症（狭義）は腹痛などの随伴症状を問わない（NG-180） |
| IBS の頻度 | 月3日以上、不快感を含む（NG-127） | IBS 診療 GL 2020 は Rome IV（週1日以上の腹痛） |

### 9-3. いただいたまとめとの照合結果

**一次資料と異なっていた点（5点）**

1. **「機能性」の完全な廃止**：用語はできるだけ改められましたが、機能性下痢・機能性胸痛・機能性胸やけ・機能性腹部膨満には残っています（NG-113、NG-126）。
2. **麻薬性腸症候群の新規追加**：Rome IV ですでに定義されていました（NG-003、NG-075）。質問票の論文も、新たに評価対象になっただけで新規疾患ではないと明記しています（NG-170）。
3. **成人の「食道の空気通過障害」**：成人の新規疾患は「げっぷができない症候群（逆行性輪状咽頭筋機能不全）」で、食道ではなく胃十二指腸の章で定義されています（NG-209）。食道の章はこれを「定義が不十分な新しい症候群（abelchia）」として扱っています。「空気通過障害」は小児上部の分類名です（NG-118）。
4. **直腸肛門の感覚機能障害の欠落**：Rome V で新設されていますが、まとめにはありませんでした（NG-164、165）。
5. **便中カルプロテクチンのカットオフ（<100・100〜250・≥250）**：腸疾患の章にこの区分はなく、記載は「50 μg/g 以下で陰性的中率 99.8%」です（NG-131）。

**原本で確認できた点（カード化済み）**

- 段階的ケア（Level 1〜3）と肯定的診断の推奨（NG-130、166、167）
- CAPS のカテゴリーA・B、身体所見（聴診器徴候、閉眼徴候、多数の手術痕、自律神経反応の乏しさ）（NG-150〜152）
- 排便協調障害の probable・definite の区別（NG-161）
- 便失禁の閾値の月1回以上への引き下げ（NG-159、173）
- IBS の「月経だけに限られない」補助基準（NG-127）
- 9段階の頻度尺度の修正、解剖図（ピクトグラム）の採用（NG-170、171）
- FICAI（NG-175）、Infant Distress Syndrome の名称（NG-174）と診断基準（NG-230）
- 臨床用基準（煩わしさ、低い頻度の許容、6か月不要・8週間の経過）（NG-234）
- 低 FODMAP 食の3段階と管理栄養士の関与（小児の章、NG-219）
- 小児でのミルタザピンの反応率 82%（NG-177、二次資料経由）
- 機能性胸痛・機能性胸やけ・逆流過敏症・食道球の「8週間以上の最適化した PPI・P-CAB 療法」の要件（NG-188、191、194、195）
- 成人 FD で、PDS がある場合の食後の心窩部痛を PDS に含める変更（NG-199）。ただし PDS のない「食事関連 EPS」は EPS に残り、暫定基準で区別する（NG-200）

**なお確認できていない点**

いただいたまとめ（2回分）の論点は、原典ですべて照合を終えました。Rome V の要約論文で未入手なのは、成人の胆嚢・Oddi 括約筋の章などです。序論の要約は NG-237 に入れました。

中枢介在性の痛みの章（NG-149〜157）は福土審先生が筆頭（共同筆頭）です。学会の広報では、会員が国際基準の作成に関わった例として紹介できます。

### 9-4. Claude Code での確認点（Rome V）

1. SRC-140〜147 の PMID・PMCID を DOI から取得する。SRC-141 は原著（CGH 2026）を入手し、NG-123 の数値を照合する。
2. NG-124・125 は総説の抄録による二次資料。それぞれ食道の章（NG-186）と腸疾患の章（NG-127）で内容を確認済みなので、corroboration として扱う。
3. 第3節 sec の「二次資料経由」カードのうち、Rome V の章が引用した数値（NG-128、131〜135、140、146、147、151、156、157、160、162、177、189、190、193〜196、202、203、206、210、213、221、231、235、236）は、引用元の原著で照合する。
4. 腸疾患の章（SRC-143）と胃十二指腸の章（SRC-150）は CC BY 4.0 なので、図表の改変利用も表示条件を守れば可能。ほかの章は CC BY-NC-ND 4.0 で、改変・商用利用はできない。
5. NG-191 の機能性胸やけの頻度は、食道の章の中で「週1回以上」（診断基準の脚注）と「週2日以上」（臨床評価の節）に分かれている。カードは診断基準の脚注に従った。
6. 胃十二指腸の章の共著者に鈴木秀和先生（東海大学）が入っている。中枢介在性の痛みの章の福土先生と合わせ、日本からの参画として広報に使える。

### 9-5. いただいた3論点のまとめ（2026-10-18）の照合

| 論点 | まとめの記載 | 原典での確認結果 | カード |
|---|---|---|---|
| 臨床用基準の期間 | 過去8週間の持続で診断できる臨床用基準が導入された | **確認できた（序論、Table 3）**。前回の報告では「確認できず」としましたが、序論に記載がありました。訂正します。要件は次の4つです：Rome V の症状の質的な特徴を満たす、受診や生活に支障が出るほど煩わしい、頻度は閾値より低くてよい、6か月は不要で他疾患の除外のため8週間の経過を勧める。周期性嘔吐症候群などのまれな発作性の疾患は例外とし、診療では研究用の基準より臨床用基準を使うよう勧めている。まとめの説明はおおむね原典に沿っています | NG-234（NG-114 も更新） |
| Infant Distress Syndrome | 臨床用3項目と研究用の追加基準 | **確認できた**。研究用の基準のうち、まとめにある「生後7週〜5か月は2.5時間以上」は、原典では「それより年長の子どもは2.5時間超」と書かれており、5か月という上限はありません | NG-230、231 |
| 低 FODMAP 食の3段階 | 制限期2〜6週間、再導入期6〜8週間、個別化期。管理栄養士の関与 | **一部確認**。3段階と管理栄養士の関与は小児下部の章にあります。ただし原典の期間は「制限期は4〜6週間まで」だけで、「2〜6週間」「再導入期6〜8週間」の記載はありません。成人の腸疾患の章には3段階の記載がありません。欧州・北米の小児消化器学会のガイドラインは、小児 IBS に低 FODMAP 食などの制限食を提案していない点にも注意してください | NG-219 |

まとめには引用番号［1］〜［12］がありますが、引用元の資料は添付されていませんでした。カードは原典で確認できた範囲だけで作成しています。
