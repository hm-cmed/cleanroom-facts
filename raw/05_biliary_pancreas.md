# 第5回 胆・膵（BP-001〜BP-068）

- 作成日：2026-10-13（2026-10-14 に再検討と補充ラウンドを行い、BP-053〜068 を追加）
- 事実票：68件（BP-001〜BP-068、欠番なし）。全件 `status: draft`、`verifier: null`
- 取り込み時の注意：YAMLブロックは1つだけで、アンカー・マージキー・脚注番号は使っていません。`fact.schema.json` での検証を通過済みです。
- 形式は `docs/tasks/round2_GD_supplement.md` 第1節、番号は `docs/tasks/curriculum_reference.md` に従いました。
- SRC 番号は SRC-087 から振りました（第4回の調査レポートで SRC-086 まで使用）。第4回の取り込みで番号がずれていれば、取り込み時に読み替えてください。

## 1. 出典マスター（新規 SRC-087〜099）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 使用カード数 |
|---|---|---|---|---|---|---|
| SRC-087 | 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF） | — | — | 学会・出版社の著作物（非CC） | RESTRICTED | 12 |
| SRC-088 | 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定） | 10.1007/s00535-022-01911-6 | — | Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認） | UNKNOWN | 10 |
| SRC-089 | Okusaka T, et al. Clinical Practice Guidelines for Pancreatic Cancer 2022 from the Japan Pancreas Society: a synopsis. Int J Clin Oncol 2023;28:493-511 | 10.1007/s10147-023-02317-x | — | Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認） | UNKNOWN | 6 |
| SRC-090 | 国立がん研究センター がん情報サービス 膵臓（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新） | — | — | 元データは政府統計。サイト利用規約は人間が確認 | GOV_JP | 2 |
| SRC-091 | 国立がん研究センター がん情報サービス 胆のう・胆管（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新） | — | — | 元データは政府統計。サイト利用規約は人間が確認 | GOV_JP | 2 |
| SRC-092 | 厚生労働省 指定難病94『原発性硬化性胆管炎』概要・診断基準等 | — | — | 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認） | GOV_JP | 4 |
| SRC-093 | 厚生労働省 指定難病300『IgG4関連疾患』概要・診断基準等 | — | — | 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認） | GOV_JP | 4 |
| SRC-094 | 日本肝胆膵外科学会ほか編『TG18新基準掲載 急性胆管炎・胆嚢炎診療ガイドライン2018（第3版）』医学図書出版、2018（Minds掲載本文PDF） | — | — | 著作権は著者・出版社に帰属（Mindsは私的利用の範囲に限ると明記） | RESTRICTED | 6 |
| SRC-095 | National Cancer Institute. Pancreatic Neuroendocrine Tumors (Islet Cell Tumors) Treatment (PDQ)–Health Professional Version（最終更新 2025-05-09） | — | — | 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く） | GOV_US | 5 |
| SRC-096 | Ohtsuka T, et al. International evidence-based Kyoto guidelines for the management of intraductal papillary mucinous neoplasm of the pancreas. Pancreatology 2024;24:255-270 | 10.1016/j.pan.2023.12.009 | 38182527 | 未確認（抄録のみ参照） | UNKNOWN | 1 |
| SRC-097 | Fujita N, et al. Evidence-based clinical practice guidelines for cholelithiasis 2021. J Gastroenterol 2023;58:801-833 | 10.1007/s00535-023-02014-6 | — | Springer OA（記事ページでライセンス表示を確認できず。Crossrefで確認） | UNKNOWN | 9 |
| SRC-098 | National Cancer Institute. Gallbladder Cancer Treatment (PDQ)–Health Professional Version | — | — | 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く） | GOV_US | 3 |
| SRC-099 | National Cancer Institute. Bile Duct Cancer (Cholangiocarcinoma) Treatment (PDQ)–Health Professional Version（最終更新 2025-03-28） | — | — | 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く） | GOV_US | 4 |

- SRC-087（急性膵炎診療GL 2021）は、日本肝胆膵外科学会サイトに掲載された日本語版の本文 PDF です。学会・出版社の著作物のため `RESTRICTED` とし、推奨の向きと数値だけを自作文で書いています。
- SRC-094（TG18 日本語版）は Minds 掲載の本文 PDF です。Minds は「私的利用の範囲」と明記しているため `RESTRICTED` です。今回読めたのは前半（背景知識）だけで、診断基準と重症度判定の表は読めませんでした。
- SRC-088（慢性膵炎 GL 2021）は、記事ページから著者・巻・頁を取得できませんでした。DOI と PMCID だけを記載しています。
- SRC-096（京都ガイドライン）は抄録だけを参照しています。
- 全カードの `legal_basis` は B（自作文による事実の記述）です。

## 2. 事実票 YAML

```yaml
- id: BP-001
  domain: BP
  subdomain: 胆石症・胆道感染症
  assertion:
    plain_statement_ja: 胆石は一般人口の約10%にあると推定されている。急性胆管炎・胆嚢炎診療ガイドライン2018は、無症状または軽い症状の胆石保有者のうち5〜10年で約40%（年1〜3%）が有症状化するという報告を挙げている。
    condition:
      region: 日本
      guideline: 急性胆管炎・胆嚢炎診療GL 2018（TG18）
    differential: 胆石症診療GL 2021はより低い有症状化率を挙げている（BP-054）
    common_misconception: 無症状胆石の多くは数年以内に胆嚢炎を起こす
  provenance:
    source_ref: SRC-094
    source: 日本肝胆膵外科学会ほか編『TG18新基準掲載 急性胆管炎・胆嚢炎診療ガイドライン2018（第3版）』医学図書出版、2018（Minds掲載本文PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00467/
    source_license: 著作権は著者・出版社に帰属（Mindsは私的利用の範囲に限ると明記）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: GLが引用した研究の値（二次資料経由）。日本の報告では有症状化率に15.5〜51%と幅がある。同GLは急性胆管炎0.3〜1.6%、急性胆嚢炎3.8〜12%という値も挙げるが、分母（全胆石保有者か有症状化例か）が本文から読み取れないため主張文に入れていない。胆石症GL 2021の値（10年で10〜20%）と食い違うため、人間が原典で確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-299 (id: Jlvnl5M)；TBL-01-00-300 (id: Jlvnl5U)；TBL-01-00-301 (id: Jlvnl5Y)'
    kokushi: 医学各論 Ⅵ-7-D-①（胆石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-002
  domain: BP
  subdomain: 胆石症・胆道感染症
  assertion:
    plain_statement_ja: 急性胆管炎・胆嚢炎診療ガイドライン2018は、2000年以降の報告で急性胆管炎の死亡率は約10%、急性胆嚢炎の死亡率は概ね1%未満としている。
    condition:
      region: 日本
      guideline: 急性胆管炎・胆嚢炎診療GL 2018（TG18）
    differential: null
    common_misconception: 急性胆嚢炎の方が急性胆管炎より致死的である
  provenance:
    source_ref: SRC-094
    source: 日本肝胆膵外科学会ほか編『TG18新基準掲載 急性胆管炎・胆嚢炎診療ガイドライン2018（第3版）』医学図書出版、2018（Minds掲載本文PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00467/
    source_license: 著作権は著者・出版社に帰属（Mindsは私的利用の範囲に限ると明記）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: GLが引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-301 (id: Jlvnl5Y)；TBL-01-00-300 (id: Jlvnl5U)'
    kokushi: 医学各論 Ⅵ-7-B-②（胆管炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-003
  domain: BP
  subdomain: 胆石症・胆道感染症
  assertion:
    plain_statement_ja: 急性胆管炎は、胆管内の細菌の著しい増加と、胆管内圧の上昇による細菌やエンドトキシンの血中への逆流の2つがそろって起こる。
    condition:
      region: 日本
      guideline: 急性胆管炎・胆嚢炎診療GL 2018（TG18）
    differential: 胆管閉塞だけでは胆管炎にならない
    common_misconception: 胆管炎は胆管閉塞がなくても起こる
  provenance:
    source_ref: SRC-094
    source: 日本肝胆膵外科学会ほか編『TG18新基準掲載 急性胆管炎・胆嚢炎診療ガイドライン2018（第3版）』医学図書出版、2018（Minds掲載本文PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00467/
    source_license: 著作権は著者・出版社に帰属（Mindsは私的利用の範囲に限ると明記）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-301 (id: Jlvnl5Y)；TBL-02-07-023 (id: JlAKpks)'
    kokushi: 医学各論 Ⅵ-7-B-②（胆管炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-004
  domain: BP
  subdomain: 胆石症・胆道感染症
  assertion:
    plain_statement_ja: Charcot三徴（発熱、黄疸、右上腹部痛）は急性胆管炎の50〜70%にしかそろわない。Murphy徴候の急性胆嚢炎に対する感度は50〜70%、特異度は79〜96%と報告されている。
    condition:
      region: 日本
      guideline: 急性胆管炎・胆嚢炎診療GL 2018（TG18）
    differential: 急性胆嚢炎が急性胆管炎と誤診されることもある
    common_misconception: Charcot三徴がなければ急性胆管炎は否定できる
  provenance:
    source_ref: SRC-094
    source: 日本肝胆膵外科学会ほか編『TG18新基準掲載 急性胆管炎・胆嚢炎診療ガイドライン2018（第3版）』医学図書出版、2018（Minds掲載本文PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00467/
    source_license: 著作権は著者・出版社に帰属（Mindsは私的利用の範囲に限ると明記）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: GLが引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-301 (id: Jlvnl5Y)；TBL-01-00-300 (id: Jlvnl5U)；TBL-02-07-017 (id: JlAKpkM)；TBL-02-07-023 (id: JlAKpks)'
    kokushi: 医学各論 Ⅵ-7-B-②（胆管炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-005
  domain: BP
  subdomain: 胆石症・胆道感染症
  assertion:
    plain_statement_ja: 急性胆管炎の重症度は、臓器障害を伴い集中治療と緊急の胆道ドレナージを要する重症、臓器障害に進むおそれがあり緊急ないし早期の胆道ドレナージを要する中等症、保存的治療で対応できる軽症の3段階に分けられる。
    condition:
      region: 日本
      guideline: 急性胆管炎・胆嚢炎診療GL 2018（TG18）
    differential: null
    common_misconception: 急性胆管炎は全例で緊急ドレナージが必要
  provenance:
    source_ref: SRC-094
    source: 日本肝胆膵外科学会ほか編『TG18新基準掲載 急性胆管炎・胆嚢炎診療ガイドライン2018（第3版）』医学図書出版、2018（Minds掲載本文PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00467/
    source_license: 著作権は著者・出版社に帰属（Mindsは私的利用の範囲に限ると明記）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 各重症度の具体的な判定項目と閾値（TG18の表）は今回の取得範囲になく未確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-301 (id: Jlvnl5Y)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-7-B-②（胆管炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-006
  domain: BP
  subdomain: 胆石症・胆道感染症
  assertion:
    plain_statement_ja: 急性胆嚢炎の病理学的な経過は、発症後2〜4日が浮腫性、3〜5日が壊死性、7〜10日が化膿性の時期とされる。重症度は重症・中等症・軽症の3段階で、中等症は重い局所合併症を伴い、早期の胆嚢摘出術またはドレナージが必要とされる。
    condition:
      region: 日本
      guideline: 急性胆管炎・胆嚢炎診療GL 2018（TG18）
    differential: null
    common_misconception: 急性胆嚢炎の手術は炎症が完全に治まるまで待つべき
  provenance:
    source_ref: SRC-094
    source: 日本肝胆膵外科学会ほか編『TG18新基準掲載 急性胆管炎・胆嚢炎診療ガイドライン2018（第3版）』医学図書出版、2018（Minds掲載本文PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://minds.jcqhc.or.jp/summary/c00467/
    source_license: 著作権は著者・出版社に帰属（Mindsは私的利用の範囲に限ると明記）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 重症度の判定項目の閾値（TG18の表）は今回未確認
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-300 (id: Jlvnl5U)'
    kokushi: 医学各論 Ⅵ-7-B-①（胆囊炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-007
  domain: BP
  subdomain: 原発性硬化性胆管炎
  assertion:
    plain_statement_ja: 原発性硬化性胆管炎（PSC）は、肝内外の胆管に線維性狭窄を生じる進行性の慢性炎症性疾患で、二次性硬化性胆管炎やIgG4関連硬化性胆管炎は除外する。令和元年度の医療受給者証保持者数は892人で、発症年齢は30歳代と60歳代の二峰性を示す。
    condition:
      region: 日本
      year: 令和元年度
    differential: IgG4関連硬化性胆管炎、二次性硬化性胆管炎
    common_misconception: PSCは高齢女性に多い自己免疫疾患である
  provenance:
    source_ref: SRC-092
    source: 厚生労働省 指定難病94『原発性硬化性胆管炎』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173515.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-293 (id: Jlvnl7Q)'
    kokushi: 医学各論 Ⅵ-7-B-③（原発性硬化性胆管炎、c）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-008
  domain: BP
  subdomain: 原発性硬化性胆管炎
  assertion:
    plain_statement_ja: 日本のPSCでは潰瘍性大腸炎の合併が40%、胆管癌の合併が7.1%と報告されている。約半数は無症状で診断され、初発症状で最も多いのは黄疸（19%）である。
    condition:
      region: 日本
      year: 2015年全国調査
    differential: 原発性胆汁性胆管炎（LV-074〜078）
    common_misconception: PSCは必ず症状を伴って見つかる
  provenance:
    source_ref: SRC-092
    source: 厚生労働省 指定難病94『原発性硬化性胆管炎』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173515.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-293 (id: Jlvnl7Q)；TBL-02-07-023 (id: JlAKpks)'
    kokushi: 医学各論 Ⅵ-7-B-③（原発性硬化性胆管炎、c）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-009
  domain: BP
  subdomain: 原発性硬化性胆管炎
  assertion:
    plain_statement_ja: PSCの胆管像では、輪状・膜状・帯状の狭窄や、憩室様の突出、数珠状の所見が特徴的で、病型は肝内型、肝外型、肝内外型に分けられる。IgG4関連硬化性胆管炎では、下部胆管に狭窄の主座があることが多く、自己免疫性膵炎を合併し、ステロイドがよく効く。
    condition:
      region: 日本
    differential: null
    common_misconception: PSCとIgG4関連硬化性胆管炎は治療反応性が同じ
  provenance:
    source_ref: SRC-092
    source: 厚生労働省 指定難病94『原発性硬化性胆管炎』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173515.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-293 (id: Jlvnl7Q)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: 医学各論 Ⅵ-7-B-③（原発性硬化性胆管炎、c）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-010
  domain: BP
  subdomain: 原発性硬化性胆管炎
  assertion:
    plain_statement_ja: PSCに対してウルソデオキシコール酸やベザフィブラートは胆道系酵素を下げるが、予後の改善は不明である。進行例では肝移植が唯一の救命法で、日本では生体肝移植が主に行われ、移植後の再発率は比較的高い。肝移植を行わない場合の5年生存率は75%と報告されている。
    condition:
      region: 日本
    differential: null
    common_misconception: PSCはウルソデオキシコール酸で治癒する
  provenance:
    source_ref: SRC-092
    source: 厚生労働省 指定難病94『原発性硬化性胆管炎』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001173515.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-293 (id: Jlvnl7Q)'
    kokushi: 医学各論 Ⅵ-7-B-③（原発性硬化性胆管炎、c）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-011
  domain: BP
  subdomain: 胆道癌
  assertion:
    plain_statement_ja: 日本で2023年に胆のう・胆管癌と診断されたのは20,926例（男性11,451例、女性9,475例）で、2024年の死亡数は17,232人（男性9,205人、女性8,027人）だった。
    condition:
      region: 日本
      year: 罹患2023年、死亡2024年
    differential: null
    common_misconception: 胆道癌はまれで年間数千例程度
  provenance:
    source_ref: SRC-091
    source: 国立がん研究センター がん情報サービス 胆のう・胆管（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新）
    doi: null
    pmid: null
    pmcid: null
    url: https://ganjoho.jp/reg_stat/statistics/stat/cancer/9_gallbladder.html
    source_license: 元データは政府統計。サイト利用規約は人間が確認
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: ganjoho.jp の利用規約は人間が確認する
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)'
    kokushi: 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-012
  domain: BP
  subdomain: 胆道癌
  assertion:
    plain_statement_ja: 日本で2018年に胆のう・胆管癌と診断された人の5年相対生存率は24.8%（男性27.5%、女性21.7%）である。
    condition:
      region: 日本
      year: 2018年診断例
    differential: null
    common_misconception: 胆道癌の予後は膵癌より悪い
  provenance:
    source_ref: SRC-091
    source: 国立がん研究センター がん情報サービス 胆のう・胆管（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新）
    doi: null
    pmid: null
    pmcid: null
    url: https://ganjoho.jp/reg_stat/statistics/stat/cancer/9_gallbladder.html
    source_license: 元データは政府統計。サイト利用規約は人間が確認
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: ganjoho.jp の利用規約は人間が確認する
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)'
    kokushi: 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-013
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 日本の急性膵炎の診断基準では、①上腹部の急性腹痛発作と圧痛、②血中または尿中の膵酵素の上昇、③超音波・CT・MRIでの急性膵炎に伴う膵の異常所見、の3項目のうち2項目以上を満たし、他の膵疾患と急性腹症を除外したものを急性膵炎とする。慢性膵炎の急性増悪も急性膵炎に含める。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: 消化管穿孔、胆嚢炎など他の急性腹症
    common_misconception: 急性膵炎の診断には画像所見が必須
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-014
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 急性膵炎の診断のための血液検査では、血中リパーゼの測定が推奨される（強い推奨、エビデンスの確実性：中）。測定が難しい場合は血中アミラーゼを用いる。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: null
    common_misconception: 膵酵素の値が高いほど急性膵炎は重症である
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-015
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 日本の急性膵炎の重症度判定では、予後因子9項目（BE≦−3 mEq/Lまたはショック、PaO2≦60 mmHgまたは呼吸不全、BUN≧40 mg/dLまたはCr≧2 mg/dLまたは乏尿、LDH≧基準値上限の2倍、血小板≦10万/mm³、総Ca≦7.5 mg/dL、CRP≧15 mg/dL、SIRS診断基準の陽性項目≧3、年齢≧70歳）を各1点とし、3点以上か造影CT Grade 2以上を重症とする。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: 国際的には改訂アトランタ分類（臓器不全の持続48時間超）が用いられる
    common_misconception: アミラーゼ値で重症度を判定する
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-016
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 急性膵炎の造影CT Gradeは、炎症の膵外進展（0〜2点）と膵の造影不良域（0〜2点）の合計で判定する。重症度は、診断時、24時間以内、24〜48時間の各時点で繰り返し評価することが推奨される（強い推奨）。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: null
    common_misconception: 重症度は入院時に1回判定すれば十分
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-017
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 急性膵炎の初期治療では積極的な輸液療法が提案され、過剰輸液を避けるためモニタリングを行う。輸液は膠質液より晶質液、0.9%食塩液より緩衝液（細胞外液）が提案されている（いずれも弱い推奨）。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: 高齢者、心不全、腎不全では綿密な管理が必要
    common_misconception: 急性膵炎の輸液は少なめが安全
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-018
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 軽症の急性膵炎に予防的抗菌薬を投与しないことが推奨される（強い推奨、エビデンスの確実性：高）。重症急性膵炎や壊死性膵炎でも、予防的抗菌薬による生命予後や感染性合併症の改善効果は証明されていない。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: null
    common_misconception: 急性膵炎には全例に予防的抗菌薬を投与する
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-019
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 急性膵炎では、入院後48時間以内に少量からでも経腸栄養を開始することが推奨される（強い推奨、エビデンスの確実性：高）。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: null
    common_misconception: 急性膵炎では長期の絶食と中心静脈栄養が原則
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)；TBL-02-07-032 (id: JlAKplM)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-020
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 胆石性膵炎で、胆管炎を合併している例、または黄疸や胆管拡張などの胆汁うっ滞があり画像で総胆管内に結石・胆泥を認める例には、早期のERCP／内視鏡的乳頭括約筋切開術（EST）が推奨される（強い推奨、エビデンスの確実性：高）。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: null
    common_misconception: 胆石性膵炎は全例で緊急ERCPを行う
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)；TBL-01-00-299 (id: Jlvnl5M)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-021
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 軽症の胆石性膵炎では、早期の胆嚢摘出術が推奨される（強い推奨）。膵周囲の液体貯留や膵壊死を伴う重症例では、液体貯留が消える時期、または発症から4〜6週以降の待機的手術が提案される（弱い推奨）。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: null
    common_misconception: 胆石性膵炎の胆嚢摘出は数か月後でよい
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)；TBL-01-00-299 (id: Jlvnl5M)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-022
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 感染性膵壊死に対しては、全身状態が保たれていれば、被包化が起こる時期（通常は発症4週以降）に内視鏡的または経皮的ドレナージを行い、必要に応じてネクロセクトミーへ進むステップアップ・アプローチが提案される。内視鏡で到達できない部位では外科的アプローチの併用を考慮する。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: 被包化壊死（WON）と仮性嚢胞
    common_misconception: 感染性膵壊死には早期の開腹ネクロセクトミーが標準
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-023
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 日本の全国調査では、急性膵炎全体の致命率は2011年の2.6%から2016年の1.8%に、重症急性膵炎の致命率は10.1%から6.1%に低下した。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: null
    common_misconception: 重症急性膵炎の致命率は現在も30%を超える
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: GLが引用した全国調査の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-024
  domain: BP
  subdomain: 急性膵炎
  assertion:
    plain_statement_ja: 急性膵炎の診療では、重症度の繰り返し評価、重症例の診断後3時間以内の転送の検討、3時間以内の成因の鑑別、胆道通過障害が疑われる胆石性膵炎での早期ERCP＋ESTの検討、造影可能な重症例での3時間以内の造影CTなどからなるPancreatitis Bundlesの遵守が推奨される（強い推奨）。
    condition:
      region: 日本
      guideline: 急性膵炎診療GL 2021（第5版）
    differential: null
    common_misconception: 急性膵炎の初期対応は施設ごとに任意でよい
  provenance:
    source_ref: SRC-087
    source: 急性膵炎診療ガイドライン改訂出版委員会（改訂出版責任者 高田忠敬）『急性膵炎診療ガイドライン2021（第5版）』2021年12月（日本肝胆膵外科学会サイト掲載PDF）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.jshbps.jp/huge/gl2021.pdf
    source_license: 学会・出版社の著作物（非CC）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: バンドル遵守で致命率が下がったという全国調査の値は二次資料経由
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-305 (id: Jlvnl7k)'
    kokushi: 医学各論 Ⅵ-8-A-①（急性膵炎、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-025
  domain: BP
  subdomain: 慢性膵炎
  assertion:
    plain_statement_ja: 慢性膵炎の画像診断の感度・特異度は、腹部超音波で感度67%、CTで75%・91%、MRCPで78%・96%、EUS（Rosemont分類）で81%・97%と報告されている。診断にはMRI/MRCPとEUSが提案される（いずれも弱い推奨、エビデンスレベルB）。
    condition:
      guideline: JSGE 慢性膵炎GL 2021
      region: 日本
    differential: null
    common_misconception: 慢性膵炎は腹部単純X線の膵石だけで診断する
  provenance:
    source_ref: SRC-088
    source: 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定）
    doi: 10.1007/s00535-022-01911-6
    pmid: null
    pmcid: PMC9522716
    url: https://link.springer.com/article/10.1007/s00535-022-01911-6
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 感度・特異度はGLが引用したメタ解析の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-306 (id: Jlvnl7o)；TBL-02-07-029 (id: JlAKplA)'
    kokushi: 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-026
  domain: BP
  subdomain: 慢性膵炎
  assertion:
    plain_statement_ja: 日本の慢性膵炎臨床診断基準2019では早期慢性膵炎の概念があり、早期慢性膵炎と診断された例のうち確診・準確診に進んだのは約5%と報告されている。
    condition:
      guideline: JSGE 慢性膵炎GL 2021
      region: 日本
    differential: null
    common_misconception: 早期慢性膵炎の大半は数年で確診例に進む
  provenance:
    source_ref: SRC-088
    source: 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定）
    doi: 10.1007/s00535-022-01911-6
    pmid: null
    pmcid: PMC9522716
    url: https://link.springer.com/article/10.1007/s00535-022-01911-6
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 早期慢性膵炎の診断項目の詳細はGL本文で確認が必要
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-306 (id: Jlvnl7o)'
    kokushi: 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-027
  domain: BP
  subdomain: 慢性膵炎
  assertion:
    plain_statement_ja: アルコール性急性膵炎の後に慢性膵炎へ進む割合は、完全禁酒で13.6%、節酒で23.3%、飲酒量が変わらない場合は40.9%と報告されている。喫煙は慢性膵炎の発症リスクを高め（相対危険2.29）、発症後5年以内の禁煙は膵石灰化のリスクを下げる。
    condition:
      guideline: JSGE 慢性膵炎GL 2021
      region: 日本
    differential: null
    common_misconception: 慢性膵炎の危険因子は飲酒だけである
  provenance:
    source_ref: SRC-088
    source: 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定）
    doi: 10.1007/s00535-022-01911-6
    pmid: null
    pmcid: PMC9522716
    url: https://link.springer.com/article/10.1007/s00535-022-01911-6
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: GLが引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-306 (id: Jlvnl7o)'
    kokushi: 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-028
  domain: BP
  subdomain: 慢性膵炎
  assertion:
    plain_statement_ja: 慢性膵炎の患者には禁煙指導が推奨される（強い推奨、エビデンスレベルC）。発症後の禁煙で疼痛の再燃が減ると報告されている。
    condition:
      guideline: JSGE 慢性膵炎GL 2021
      region: 日本
    differential: null
    common_misconception: 禁煙は慢性膵炎の経過に影響しない
  provenance:
    source_ref: SRC-088
    source: 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定）
    doi: 10.1007/s00535-022-01911-6
    pmid: null
    pmcid: PMC9522716
    url: https://link.springer.com/article/10.1007/s00535-022-01911-6
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-306 (id: Jlvnl7o)'
    kokushi: 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-029
  domain: BP
  subdomain: 慢性膵炎
  assertion:
    plain_statement_ja: 慢性膵炎の疼痛には、NSAIDが無効な場合に弱オピオイドが推奨される（弱い推奨、エビデンスレベルC）。内視鏡治療で疼痛が改善しない場合には外科手術が推奨される（強い推奨、エビデンスレベルB）。
    condition:
      guideline: JSGE 慢性膵炎GL 2021
      region: 日本
    differential: null
    common_misconception: 慢性膵炎の疼痛には最初から強オピオイドを使う
  provenance:
    source_ref: SRC-088
    source: 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定）
    doi: 10.1007/s00535-022-01911-6
    pmid: null
    pmcid: PMC9522716
    url: https://link.springer.com/article/10.1007/s00535-022-01911-6
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-306 (id: Jlvnl7o)；TBL-02-07-017 (id: JlAKpkM)'
    kokushi: 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-030
  domain: BP
  subdomain: 慢性膵炎
  assertion:
    plain_statement_ja: 慢性膵炎の脂肪便や体重減少にはパンクレリパーゼによる膵消化酵素補充療法が推奨される（強い推奨、エビデンスレベルA）。一方、疼痛の軽減を目的とした消化酵素補充は推奨されない。
    condition:
      guideline: JSGE 慢性膵炎GL 2021
      region: 日本
    differential: null
    common_misconception: 消化酵素薬は慢性膵炎の痛みに有効
  provenance:
    source_ref: SRC-088
    source: 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定）
    doi: 10.1007/s00535-022-01911-6
    pmid: null
    pmcid: PMC9522716
    url: https://link.springer.com/article/10.1007/s00535-022-01911-6
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-306 (id: Jlvnl7o)；TBL-02-07-009 (id: JlAKpjw)'
    kokushi: 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-031
  domain: BP
  subdomain: 慢性膵炎
  assertion:
    plain_statement_ja: 非代償期の慢性膵炎では一律の脂肪制限は推奨されず（強い推奨）、脂肪摂取量は1日40〜70 gが勧められる。膵性糖尿病でも一律のカロリー制限は低栄養と低血糖の危険があるため推奨されない。
    condition:
      guideline: JSGE 慢性膵炎GL 2021
      region: 日本
    differential: null
    common_misconception: 慢性膵炎では脂肪を厳しく制限すべき
  provenance:
    source_ref: SRC-088
    source: 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定）
    doi: 10.1007/s00535-022-01911-6
    pmid: null
    pmcid: PMC9522716
    url: https://link.springer.com/article/10.1007/s00535-022-01911-6
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-306 (id: Jlvnl7o)'
    kokushi: 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-032
  domain: BP
  subdomain: 慢性膵炎
  assertion:
    plain_statement_ja: インスリン依存状態の膵性糖尿病にはインスリン治療が推奨される（強い推奨、エビデンスレベルC）。日本の調査では、慢性膵炎に伴う糖尿病患者の66.7%がインスリンを使用していた。
    condition:
      guideline: JSGE 慢性膵炎GL 2021
      region: 日本
    differential: 2型糖尿病と異なり、グルカゴン分泌も低下し低血糖を起こしやすい
    common_misconception: 膵性糖尿病は経口血糖降下薬で十分にコントロールできる
  provenance:
    source_ref: SRC-088
    source: 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定）
    doi: 10.1007/s00535-022-01911-6
    pmid: null
    pmcid: PMC9522716
    url: https://link.springer.com/article/10.1007/s00535-022-01911-6
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 使用率はGLが引用した調査の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-306 (id: Jlvnl7o)'
    kokushi: 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-033
  domain: BP
  subdomain: 慢性膵炎
  assertion:
    plain_statement_ja: 症状のある膵仮性嚢胞には内視鏡的ドレナージが第一選択として推奨される（強い推奨、エビデンスレベルC）。無症状の慢性膵炎に対する内視鏡治療（ESWLを含む）は推奨されない。
    condition:
      guideline: JSGE 慢性膵炎GL 2021
      region: 日本
    differential: null
    common_misconception: 膵石があれば無症状でも内視鏡治療を行う
  provenance:
    source_ref: SRC-088
    source: 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定）
    doi: 10.1007/s00535-022-01911-6
    pmid: null
    pmcid: PMC9522716
    url: https://link.springer.com/article/10.1007/s00535-022-01911-6
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-306 (id: Jlvnl7o)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-034
  domain: BP
  subdomain: 慢性膵炎
  assertion:
    plain_statement_ja: 慢性膵炎の患者506例を追跡した研究では、中央値5.6年で19例（3.7%）に膵癌が発生した（標準化罹患比11.8）。膵癌の発生をとらえるためのスクリーニング法は確立していない。
    condition:
      guideline: JSGE 慢性膵炎GL 2021
      region: 日本
    differential: null
    common_misconception: 慢性膵炎は膵癌のリスクにならない
  provenance:
    source_ref: SRC-088
    source: 日本消化器病学会. Evidence-based clinical practice guidelines for chronic pancreatitis 2021. J Gastroenterol 2022（著者・巻・頁はCrossrefで確定）
    doi: 10.1007/s00535-022-01911-6
    pmid: null
    pmcid: PMC9522716
    url: https://link.springer.com/article/10.1007/s00535-022-01911-6
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: GLが引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-306 (id: Jlvnl7o)；TBL-01-00-655 (id: JlvnmdQ)'
    kokushi: 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-035
  domain: BP
  subdomain: 自己免疫性膵炎・IgG4関連疾患
  assertion:
    plain_statement_ja: IgG4関連疾患は、血中IgG4高値と、IgG4陽性形質細胞の浸潤と線維化を特徴とし、全身の複数臓器に腫大や結節・肥厚性病変を生じる疾患で、日本から提唱された概念である。自己免疫性膵炎と涙腺・唾液腺炎（Mikulicz病）が典型で、硬化性胆管炎では閉塞性黄疸、後腹膜線維症では水腎症が多い。患者数は約8,000人とされる。
    condition:
      region: 日本
    differential: 膵癌、胆管癌、悪性リンパ腫
    common_misconception: IgG4関連疾患は膵臓だけの病気である
  provenance:
    source_ref: SRC-093
    source: 厚生労働省 指定難病300『IgG4関連疾患』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001175041.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-307 (id: Jlvnl7w)'
    kokushi: 医学各論 Ⅵ-8-A-③（自己免疫性膵炎、b）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-036
  domain: BP
  subdomain: 自己免疫性膵炎・IgG4関連疾患
  assertion:
    plain_statement_ja: IgG4関連疾患の包括診断基準では、血清IgG4 135 mg/dL以上と、組織でのIgG4/IgG陽性細胞比40%以上かつIgG4陽性形質細胞10/HPF超を用い、臨床所見と両方を満たせば確診、臨床所見と病理所見で準確診、臨床所見と血清IgG4で疑診とする。臓器ごとの診断基準もある。
    condition:
      region: 日本
      criteria: 指定難病の診断基準
    differential: null
    common_misconception: 血清IgG4高値だけでIgG4関連疾患と確定できる
  provenance:
    source_ref: SRC-093
    source: 厚生労働省 指定難病300『IgG4関連疾患』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001175041.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-307 (id: Jlvnl7w)；TBL-02-07-031 (id: JlAKplI)'
    kokushi: 医学各論 Ⅵ-8-A-③（自己免疫性膵炎、b）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-037
  domain: BP
  subdomain: 自己免疫性膵炎・IgG4関連疾患
  assertion:
    plain_statement_ja: 自己免疫性膵炎は膵癌や胆管癌と誤診されやすく、悪性腫瘍が疑われる場合はEUS-FNAによる細胞診まで行うことが望ましい。病理学的に悪性を除外しないままステロイドを投与して治療的に診断することは避ける。
    condition:
      region: 日本
    differential: null
    common_misconception: ステロイドが効けば膵癌は否定できる
  provenance:
    source_ref: SRC-093
    source: 厚生労働省 指定難病300『IgG4関連疾患』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001175041.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-307 (id: Jlvnl7w)；TBL-02-07-031 (id: JlAKplI)'
    kokushi: 医学各論 Ⅵ-8-A-③（自己免疫性膵炎、b）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-038
  domain: BP
  subdomain: 自己免疫性膵炎・IgG4関連疾患
  assertion:
    plain_statement_ja: IgG4関連疾患の治療はステロイドが第一選択で、比較的高用量で導入した後に維持療法を1〜3年行い、寛解が続けば中止してよいとされる。多くはステロイドが効くが、減量や中止で約半数が再発する。初回投与量（0.5〜0.6 mg/kg）で6か月治療しても寛解しないものをステロイド抵抗性とする。
    condition:
      region: 日本
    differential: null
    common_misconception: IgG4関連疾患はステロイドで完治し再発しない
  provenance:
    source_ref: SRC-093
    source: 厚生労働省 指定難病300『IgG4関連疾患』概要・診断基準等
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10905000/001175041.pdf
    source_license: 厚労省 指定難病の概要・診断基準等（政府標準利用規約準拠と想定、原文は人間が確認）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-307 (id: Jlvnl7w)'
    kokushi: 医学各論 Ⅵ-8-A-③（自己免疫性膵炎、b）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-039
  domain: BP
  subdomain: 膵癌
  assertion:
    plain_statement_ja: 日本の膵癌診療ガイドライン2022は、新規発症や増悪した糖尿病、慢性膵炎、IPMN、膵癌の家族歴を膵癌のリスクとして扱い、これらの患者には精査や経過観察を提案している（いずれも弱い推奨、エビデンスレベルC）。
    condition:
      guideline: 日本膵臓学会 膵癌診療GL 2022
      region: 日本
    differential: null
    common_misconception: 糖尿病の悪化は膵癌と無関係
  provenance:
    source_ref: SRC-089
    source: 'Okusaka T, et al. Clinical Practice Guidelines for Pancreatic Cancer 2022 from the Japan Pancreas Society: a synopsis. Int J Clin Oncol 2023;28:493-511'
    doi: 10.1007/s10147-023-02317-x
    pmid: null
    pmcid: PMC10066137
    url: https://link.springer.com/10.1007/s10147-023-02317-x
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-655 (id: JlvnmdQ)'
    kokushi: 医学各論 Ⅵ-8-B-①（膵癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-040
  domain: BP
  subdomain: 膵癌
  assertion:
    plain_statement_ja: 膵癌の診断では、最初に腹部超音波検査を行うことが提案される（弱い推奨、エビデンスレベルB）。EUSは他の画像検査より感度が高いとされ、膵腫瘤の病理診断にはEUS-FNAや生検が提案される。PETは膵癌の診断目的には推奨されない。
    condition:
      guideline: 日本膵臓学会 膵癌診療GL 2022
      region: 日本
    differential: null
    common_misconception: 膵癌の診断にはPETが最も有用
  provenance:
    source_ref: SRC-089
    source: 'Okusaka T, et al. Clinical Practice Guidelines for Pancreatic Cancer 2022 from the Japan Pancreas Society: a synopsis. Int J Clin Oncol 2023;28:493-511'
    doi: 10.1007/s10147-023-02317-x
    pmid: null
    pmcid: PMC10066137
    url: https://link.springer.com/10.1007/s10147-023-02317-x
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-655 (id: JlvnmdQ)；TBL-02-07-029 (id: JlAKplA)；TBL-02-07-031 (id: JlAKplI)'
    kokushi: 医学各論 Ⅵ-8-B-①（膵癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-041
  domain: BP
  subdomain: 膵癌
  assertion:
    plain_statement_ja: 切除可能膵癌には、術前補助化学療法としてゲムシタビン＋S-1療法が提案される（弱い推奨、エビデンスレベルC）。肉眼的に治癒切除した後の術後補助化学療法が推奨され、S-1単独療法が強く推奨される（強い推奨、エビデンスレベルA）。
    condition:
      guideline: 日本膵臓学会 膵癌診療GL 2022
      region: 日本
    differential: null
    common_misconception: 切除できれば術後化学療法は不要
  provenance:
    source_ref: SRC-089
    source: 'Okusaka T, et al. Clinical Practice Guidelines for Pancreatic Cancer 2022 from the Japan Pancreas Society: a synopsis. Int J Clin Oncol 2023;28:493-511'
    doi: 10.1007/s10147-023-02317-x
    pmid: null
    pmcid: PMC10066137
    url: https://link.springer.com/10.1007/s10147-023-02317-x
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-655 (id: JlvnmdQ)'
    kokushi: 医学各論 Ⅵ-8-B-①（膵癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-042
  domain: BP
  subdomain: 膵癌
  assertion:
    plain_statement_ja: 遠隔転移のある膵癌の一次化学療法として、FOLFIRINOX療法とゲムシタビン＋ナブパクリタキセル療法が推奨される（いずれも強い推奨、エビデンスレベルA）。
    condition:
      guideline: 日本膵臓学会 膵癌診療GL 2022
      region: 日本
    differential: null
    common_misconception: 転移性膵癌に有効な化学療法はない
  provenance:
    source_ref: SRC-089
    source: 'Okusaka T, et al. Clinical Practice Guidelines for Pancreatic Cancer 2022 from the Japan Pancreas Society: a synopsis. Int J Clin Oncol 2023;28:493-511'
    doi: 10.1007/s10147-023-02317-x
    pmid: null
    pmcid: PMC10066137
    url: https://link.springer.com/10.1007/s10147-023-02317-x
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-655 (id: JlvnmdQ)'
    kokushi: 医学各論 Ⅵ-8-B-①（膵癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-043
  domain: BP
  subdomain: 膵癌
  assertion:
    plain_statement_ja: 生殖細胞系列のBRCA1/2病的バリアントをもつ膵癌では、白金製剤を含むレジメンや、オラパリブによる維持療法が提案される。MSI-highの膵癌にはペムブロリズマブ単剤療法が提案される（いずれも弱い推奨、エビデンスレベルC）。
    condition:
      guideline: 日本膵臓学会 膵癌診療GL 2022
      region: 日本
    differential: null
    common_misconception: 膵癌では遺伝子検査は治療選択に関係しない
  provenance:
    source_ref: SRC-089
    source: 'Okusaka T, et al. Clinical Practice Guidelines for Pancreatic Cancer 2022 from the Japan Pancreas Society: a synopsis. Int J Clin Oncol 2023;28:493-511'
    doi: 10.1007/s10147-023-02317-x
    pmid: null
    pmcid: PMC10066137
    url: https://link.springer.com/10.1007/s10147-023-02317-x
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-655 (id: JlvnmdQ)'
    kokushi: 医学各論 Ⅵ-8-B-①（膵癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-044
  domain: BP
  subdomain: 膵癌
  assertion:
    plain_statement_ja: 膵癌手術で予防的にリンパ節や神経叢を拡大郭清しても生存期間の延長は示されておらず、推奨されない（強い推奨、エビデンスレベルA）。
    condition:
      guideline: 日本膵臓学会 膵癌診療GL 2022
      region: 日本
    differential: null
    common_misconception: 拡大郭清ほど予後がよくなる
  provenance:
    source_ref: SRC-089
    source: 'Okusaka T, et al. Clinical Practice Guidelines for Pancreatic Cancer 2022 from the Japan Pancreas Society: a synopsis. Int J Clin Oncol 2023;28:493-511'
    doi: 10.1007/s10147-023-02317-x
    pmid: null
    pmcid: PMC10066137
    url: https://link.springer.com/10.1007/s10147-023-02317-x
    source_license: Open access、© The Author(s)（記事ページにCC種別の表示なし。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-655 (id: JlvnmdQ)'
    kokushi: 医学各論 Ⅵ-8-B-①（膵癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-045
  domain: BP
  subdomain: 膵癌
  assertion:
    plain_statement_ja: 日本で2023年に膵癌と診断されたのは47,540例（男性23,761例、女性23,779例）で、2024年の膵癌による死亡数は41,235人（男性20,371人、女性20,864人）だった。
    condition:
      region: 日本
      year: 罹患2023年、死亡2024年
    differential: null
    common_misconception: 膵癌の罹患数は死亡数よりはるかに多い
  provenance:
    source_ref: SRC-090
    source: 国立がん研究センター がん情報サービス 膵臓（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新）
    doi: null
    pmid: null
    pmcid: null
    url: https://ganjoho.jp/reg_stat/statistics/stat/cancer/10_pancreas.html
    source_license: 元データは政府統計。サイト利用規約は人間が確認
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: ganjoho.jp の利用規約は人間が確認する
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-655 (id: JlvnmdQ)'
    kokushi: 医学各論 Ⅵ-8-B-①（膵癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-046
  domain: BP
  subdomain: 膵癌
  assertion:
    plain_statement_ja: 日本で2018年に膵癌と診断された人の5年相対生存率は13.2%（男性13.6%、女性12.8%）である。
    condition:
      region: 日本
      year: 2018年診断例
    differential: 胆のう・胆管癌は24.8%（BP-012）、肝癌は35.2%（LV-051）
    common_misconception: 膵癌の5年生存率は30%を超える
  provenance:
    source_ref: SRC-090
    source: 国立がん研究センター がん情報サービス 膵臓（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新）
    doi: null
    pmid: null
    pmcid: null
    url: https://ganjoho.jp/reg_stat/statistics/stat/cancer/10_pancreas.html
    source_license: 元データは政府統計。サイト利用規約は人間が確認
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: ganjoho.jp の利用規約は人間が確認する
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-655 (id: JlvnmdQ)'
    kokushi: 医学各論 Ⅵ-8-B-①（膵癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-047
  domain: BP
  subdomain: 膵嚢胞性腫瘍
  assertion:
    plain_statement_ja: 2024年の京都ガイドラインは、2017年の国際コンセンサスを改訂してIPMNの新しい管理アルゴリズムを示し、high-risk stigmataとworrisome featuresの評価にEUS所見とEUS-FNAの細胞診を加えた。5年間変化のない小さな分枝型IPMNでは、サーベイランスを終了するか、併存膵癌に備えて継続するかの2つの選択肢を示している。
    condition:
      guideline: Kyoto IPMN guidelines 2024
    differential: MCN（女性の膵体尾部に多い）
    common_misconception: 分枝型IPMNは生涯にわたり同じ間隔で検査を続けなければならない
  provenance:
    source_ref: SRC-096
    source: Ohtsuka T, et al. International evidence-based Kyoto guidelines for the management of intraductal papillary mucinous neoplasm of the pancreas. Pancreatology 2024;24:255-270
    doi: 10.1016/j.pan.2023.12.009
    pmid: '38182527'
    pmcid: null
    url: https://pure.fujita-hu.ac.jp/en/publications/international-evidence-based-kyoto-guidelines-for-the-management-/
    source_license: 未確認（抄録のみ参照）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抄録のみ参照。high-risk stigmata・worrisome featuresの具体的な項目は未取得
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-654 (id: JlvnmdM)'
    kokushi: 医学各論 Ⅵ-8-B-②（膵囊胞性腫瘍、b）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-048
  domain: BP
  subdomain: 膵神経内分泌腫瘍
  assertion:
    plain_statement_ja: 膵神経内分泌腫瘍は膵悪性腫瘍の2%未満で、機能性腫瘍にはガストリノーマ、インスリノーマ、グルカゴノーマ、ソマトスタチノーマ、VIPomaがある。
    condition:
      source: NCI PDQ
      region: 米国
    differential: null
    common_misconception: 膵神経内分泌腫瘍は膵癌の大半を占める
  provenance:
    source_ref: SRC-095
    source: National Cancer Institute. Pancreatic Neuroendocrine Tumors (Islet Cell Tumors) Treatment (PDQ)–Health Professional Version（最終更新 2025-05-09）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/pancreatic/hp/pnet-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 米国のデータ。日本の頻度や機能性・非機能性の割合は今回は確認していない
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-653 (id: JlvnmdE)'
    kokushi: 医学各論 Ⅵ-8-B-③（膵神経内分泌腫瘍、b）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-049
  domain: BP
  subdomain: 膵神経内分泌腫瘍
  assertion:
    plain_statement_ja: インスリノーマは悪性より良性のことがはるかに多く（悪性は約10%）、約1割は多発する。外因性インスリンがないのに空腹時低血糖（40 mg/dL未満）とインスリン高値を示すことが特徴的である。
    condition:
      source: NCI PDQ
    differential: インスリン自己投与、スルホニル尿素薬による低血糖
    common_misconception: インスリノーマの多くは悪性である
  provenance:
    source_ref: SRC-095
    source: National Cancer Institute. Pancreatic Neuroendocrine Tumors (Islet Cell Tumors) Treatment (PDQ)–Health Professional Version（最終更新 2025-05-09）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/pancreatic/hp/pnet-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-653 (id: JlvnmdE)'
    kokushi: 医学各論 Ⅵ-8-B-③（膵神経内分泌腫瘍、b）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-050
  domain: BP
  subdomain: 膵神経内分泌腫瘍
  assertion:
    plain_statement_ja: ガストリノーマ（Zollinger-Ellison症候群）は消化性潰瘍の1%未満の原因で、15〜35%がMEN1に伴い、最大50%が悪性である。85%はいわゆるガストリノーマ三角に見つかり、膵実質内は15%にとどまる。
    condition:
      source: NCI PDQ
    differential: H. pylori・NSAIDによる通常の消化性潰瘍
    common_misconception: ガストリノーマは膵実質内に発生することが多い
  provenance:
    source_ref: SRC-095
    source: National Cancer Institute. Pancreatic Neuroendocrine Tumors (Islet Cell Tumors) Treatment (PDQ)–Health Professional Version（最終更新 2025-05-09）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/pancreatic/hp/pnet-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-653 (id: JlvnmdE)；TBL-01-00-672 (id: Jlvnme4)'
    kokushi: 医学各論 Ⅵ-8-B-③（膵神経内分泌腫瘍、b）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-051
  domain: BP
  subdomain: 膵神経内分泌腫瘍
  assertion:
    plain_statement_ja: グルカゴノーマは約75%が悪性で、血清グルカゴン1,000 pg/mL超で診断が確定する。VIPomaは水様下痢・低カリウム血症・無酸症（WDHA症候群）を起こし、血清VIP 200 pg/mL超で診断される。
    condition:
      source: NCI PDQ
    differential: null
    common_misconception: VIPomaは便秘を起こす
  provenance:
    source_ref: SRC-095
    source: National Cancer Institute. Pancreatic Neuroendocrine Tumors (Islet Cell Tumors) Treatment (PDQ)–Health Professional Version（最終更新 2025-05-09）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/pancreatic/hp/pnet-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-653 (id: JlvnmdE)'
    kokushi: 医学各論 Ⅵ-8-B-③（膵神経内分泌腫瘍、b）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-052
  domain: BP
  subdomain: 膵神経内分泌腫瘍
  assertion:
    plain_statement_ja: MEN1は11q13のMEN1遺伝子による常染色体顕性（優性）遺伝の症候群で、患者の85%に膵内分泌腫瘍、90%に副甲状腺機能亢進症、65%に下垂体腫瘍がみられる。膵神経内分泌腫瘍の治療は外科切除が唯一の根治法である。
    condition:
      source: NCI PDQ
    differential: null
    common_misconception: MEN1の膵腫瘍は散発例と同様に切除で治癒しやすい
  provenance:
    source_ref: SRC-095
    source: National Cancer Institute. Pancreatic Neuroendocrine Tumors (Islet Cell Tumors) Treatment (PDQ)–Health Professional Version（最終更新 2025-05-09）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/pancreatic/hp/pnet-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-653 (id: JlvnmdE)；TBL-01-00-672 (id: Jlvnme4)'
    kokushi: 医学各論 Ⅵ-8-B-③（膵神経内分泌腫瘍、b）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-053
  domain: BP
  subdomain: 胆石症
  assertion:
    plain_statement_ja: ビリルビンカルシウム石の主な原因は胆道感染である。コレステロール石は胆汁のコレステロール過飽和、結晶化、胆嚢の収縮能低下と関係し、黒色石は非抱合型ビリルビンの過剰と関係して肝硬変でもみられる。
    condition:
      region: 日本
      guideline: JSGE 胆石症GL 2021
    differential: 肝内結石はビリルビンカルシウム石が多い
    common_misconception: 胆石はすべてコレステロール石である
  provenance:
    source_ref: SRC-097
    source: Fujita N, et al. Evidence-based clinical practice guidelines for cholelithiasis 2021. J Gastroenterol 2023;58:801-833
    doi: 10.1007/s00535-023-02014-6
    pmid: null
    pmcid: PMC10423145
    url: https://link.springer.com/article/10.1007/s00535-023-02014-6
    source_license: Springer OA（記事ページでライセンス表示を確認できず。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: GL本文のBQ1-2の要旨。石の種類別の頻度は今回未取得
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-299 (id: Jlvnl5M)'
    kokushi: 医学各論 Ⅵ-7-D-①（胆石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-054
  domain: BP
  subdomain: 胆石症
  assertion:
    plain_statement_ja: 胆嚢結石の約70%は無症状で見つかり、多くは無症状のまま経過する。無症状胆嚢結石の10年間の累積有症状化率は約10〜20%、診断から1年以内の有症状化は2〜4%と推定されている。
    condition:
      region: 日本
      guideline: JSGE 胆石症GL 2021
    differential: 急性胆管炎・胆嚢炎診療GL 2018はより高い有症状化率を挙げている（BP-001）
    common_misconception: 無症状胆石の大半は数年で症状が出る
  provenance:
    source_ref: SRC-097
    source: Fujita N, et al. Evidence-based clinical practice guidelines for cholelithiasis 2021. J Gastroenterol 2023;58:801-833
    doi: 10.1007/s00535-023-02014-6
    pmid: null
    pmcid: PMC10423145
    url: https://link.springer.com/article/10.1007/s00535-023-02014-6
    source_license: Springer OA（記事ページでライセンス表示を確認できず。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: GLが引用した研究の値（二次資料経由）。BP-001の値と食い違うため、人間が原典で確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-299 (id: Jlvnl5M)'
    kokushi: 医学各論 Ⅵ-7-D-①（胆石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-055
  domain: BP
  subdomain: 胆石症
  assertion:
    plain_statement_ja: 無症状胆嚢結石から起こる合併症のリスクは、急性胆嚢炎0.3%、閉塞性黄疸0.2%、急性膵炎0.04〜1.5%と報告されている。
    condition:
      region: 日本
      guideline: JSGE 胆石症GL 2021
    differential: null
    common_misconception: 無症状胆石は高率に急性膵炎を起こす
  provenance:
    source_ref: SRC-097
    source: Fujita N, et al. Evidence-based clinical practice guidelines for cholelithiasis 2021. J Gastroenterol 2023;58:801-833
    doi: 10.1007/s00535-023-02014-6
    pmid: null
    pmcid: PMC10423145
    url: https://link.springer.com/article/10.1007/s00535-023-02014-6
    source_license: Springer OA（記事ページでライセンス表示を確認できず。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: GLが引用した研究の値（二次資料経由）。観察期間はGL本文で確認する
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-299 (id: Jlvnl5M)；TBL-01-00-300 (id: Jlvnl5U)；TBL-01-00-305 (id: Jlvnl7k)'
    kokushi: 医学各論 Ⅵ-7-D-①（胆石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-056
  domain: BP
  subdomain: 胆石症
  assertion:
    plain_statement_ja: 無症状胆嚢結石に対する予防的胆嚢摘出術は一般には勧められない。ただし、3 cmを超える結石、10 mmを超えるポリープ、陶器様胆嚢、胆嚢壁の肥厚、胆嚢内に結石が充満している例など、胆嚢癌の高リスク例では胆嚢摘出術を考慮する（弱い推奨、エビデンスレベルC）。
    condition:
      region: 日本
      guideline: JSGE 胆石症GL 2021
    differential: null
    common_misconception: 胆石があれば全例に胆嚢摘出術を行う
  provenance:
    source_ref: SRC-097
    source: Fujita N, et al. Evidence-based clinical practice guidelines for cholelithiasis 2021. J Gastroenterol 2023;58:801-833
    doi: 10.1007/s00535-023-02014-6
    pmid: null
    pmcid: PMC10423145
    url: https://link.springer.com/article/10.1007/s00535-023-02014-6
    source_license: Springer OA（記事ページでライセンス表示を確認できず。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-299 (id: Jlvnl5M)；TBL-01-00-651 (id: Jlvnmc4)'
    kokushi: 医学各論 Ⅵ-7-D-①（胆石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-057
  domain: BP
  subdomain: 胆石症
  assertion:
    plain_statement_ja: 胆嚢結石が胆嚢癌の危険因子であるという明確な根拠はないとされる（推奨なし、エビデンスレベルD）。胆石保有者からの胆嚢癌の発生は約0.1〜0.5%と報告されている。
    condition:
      region: 日本
      guideline: JSGE 胆石症GL 2021
    differential: 胆嚢癌患者には高率に胆石がみられる
    common_misconception: 胆石は胆嚢癌の確立した原因である
  provenance:
    source_ref: SRC-097
    source: Fujita N, et al. Evidence-based clinical practice guidelines for cholelithiasis 2021. J Gastroenterol 2023;58:801-833
    doi: 10.1007/s00535-023-02014-6
    pmid: null
    pmcid: PMC10423145
    url: https://link.springer.com/article/10.1007/s00535-023-02014-6
    source_license: Springer OA（記事ページでライセンス表示を確認できず。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 胆嚢癌患者の胆石保有率はGL本文の中で69〜96%と40〜70%の2つの値が示されており不整合があるため主張文に入れていない
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-299 (id: Jlvnl5M)；TBL-01-00-651 (id: Jlvnmc4)'
    kokushi: 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-058
  domain: BP
  subdomain: 胆石症
  assertion:
    plain_statement_ja: 総胆管結石が疑われ、急性胆管炎の症状がある場合はERCPが推奨される。他の画像検査で判断がつかない場合は、ERCPの前にEUSを行うことが提案される（弱い推奨、エビデンスレベルB）。EUSの総胆管結石の診断能は、メタ解析で感度0.94、特異度0.95と報告されている。
    condition:
      region: 日本
      guideline: JSGE 胆石症GL 2021
    differential: null
    common_misconception: 総胆管結石の疑いがあれば全例にまず診断的ERCPを行う
  provenance:
    source_ref: SRC-097
    source: Fujita N, et al. Evidence-based clinical practice guidelines for cholelithiasis 2021. J Gastroenterol 2023;58:801-833
    doi: 10.1007/s00535-023-02014-6
    pmid: null
    pmcid: PMC10423145
    url: https://link.springer.com/article/10.1007/s00535-023-02014-6
    source_license: Springer OA（記事ページでライセンス表示を確認できず。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 感度・特異度はGLが引用したメタ解析の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-299 (id: Jlvnl5M)；TBL-01-00-301 (id: Jlvnl5Y)；TBL-02-07-030 (id: JlAKplE)'
    kokushi: 医学各論 Ⅵ-7-D-①（胆石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-059
  domain: BP
  subdomain: 胆石症
  assertion:
    plain_statement_ja: 肝内結石は肝内胆管癌の強い危険因子であり、肝内結石の患者では肝内胆管癌のリスク評価のために腫瘍マーカーの測定が勧められる。
    condition:
      region: 日本
      guideline: JSGE 胆石症GL 2021
    differential: null
    common_misconception: 肝内結石は良性疾患で癌との関係はない
  provenance:
    source_ref: SRC-097
    source: Fujita N, et al. Evidence-based clinical practice guidelines for cholelithiasis 2021. J Gastroenterol 2023;58:801-833
    doi: 10.1007/s00535-023-02014-6
    pmid: null
    pmcid: PMC10423145
    url: https://link.springer.com/article/10.1007/s00535-023-02014-6
    source_license: Springer OA（記事ページでライセンス表示を確認できず。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-299 (id: Jlvnl5M)；TBL-01-00-651 (id: Jlvnmc4)；TBL-02-07-028 (id: JlAKpk8)'
    kokushi: 医学各論 Ⅵ-7-D-①（胆石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-060
  domain: BP
  subdomain: 胆石症
  assertion:
    plain_statement_ja: 胆石発作の予防にはウルソデオキシコール酸の内服が選択肢となる。体外衝撃波結石破砕療法（ESWL）や経口胆石溶解療法は、かつて行われたが近年はほとんど行われていない。
    condition:
      region: 日本
      guideline: JSGE 胆石症GL 2021
    differential: null
    common_misconception: 胆嚢結石の標準治療は経口溶解療法である
  provenance:
    source_ref: SRC-097
    source: Fujita N, et al. Evidence-based clinical practice guidelines for cholelithiasis 2021. J Gastroenterol 2023;58:801-833
    doi: 10.1007/s00535-023-02014-6
    pmid: null
    pmcid: PMC10423145
    url: https://link.springer.com/article/10.1007/s00535-023-02014-6
    source_license: Springer OA（記事ページでライセンス表示を確認できず。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-299 (id: Jlvnl5M)'
    kokushi: 医学各論 Ⅵ-7-D-①（胆石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-061
  domain: BP
  subdomain: 胆石症
  assertion:
    plain_statement_ja: 内視鏡的乳頭括約筋切開術（EST）やバルーン拡張術は乳頭機能を損なう可能性があるのに対し、腹腔鏡下総胆管探査は乳頭機能を保つため、とくに若年者で適切な選択肢と考えられている。
    condition:
      region: 日本
      guideline: JSGE 胆石症GL 2021
    differential: null
    common_misconception: 総胆管結石の治療は内視鏡治療以外に選択肢がない
  provenance:
    source_ref: SRC-097
    source: Fujita N, et al. Evidence-based clinical practice guidelines for cholelithiasis 2021. J Gastroenterol 2023;58:801-833
    doi: 10.1007/s00535-023-02014-6
    pmid: null
    pmcid: PMC10423145
    url: https://link.springer.com/article/10.1007/s00535-023-02014-6
    source_license: Springer OA（記事ページでライセンス表示を確認できず。Crossrefで確認）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: GLのコラムの記述で、推奨文ではない
  curriculum:
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；TBL-01-00-299 (id: Jlvnl5M)；TBL-02-07-033 (id: JlAKplQ)'
    kokushi: 医学各論 Ⅵ-7-D-①（胆石症、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-062
  domain: BP
  subdomain: 胆道癌
  assertion:
    plain_statement_ja: 胆石症の患者のうち胆嚢癌を発症するのは1%未満である。胆嚢摘出術で偶然見つかった粘膜内の胆嚢癌は80%を超える例で治癒するが、術前から癌が疑われる有症状例で治癒できるのは5%未満である。偶然見つかったⅠ期の5年生存率はほぼ100%とされる。
    condition:
      source: NCI PDQ
      region: 米国
    differential: null
    common_misconception: 胆嚢癌は発見時期にかかわらず予後不良である
  provenance:
    source_ref: SRC-098
    source: National Cancer Institute. Gallbladder Cancer Treatment (PDQ)–Health Professional Version
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/gallbladder/hp/gallbladder-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 出典ページの最終更新日は今回確認できなかった
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)；TBL-01-00-299 (id: Jlvnl5M)'
    kokushi: 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-063
  domain: BP
  subdomain: 胆道癌
  assertion:
    plain_statement_ja: 偶然見つかった胆嚢癌の再切除では、遺残病変がT1bで12%（リンパ節転移）、T2で57%、T3で77%にみられたと報告されている。T2以上では、肝部分切除と肝門部リンパ節郭清を伴う拡大切除が選択肢になる。
    condition:
      source: NCI PDQ
    differential: null
    common_misconception: 胆嚢摘出術で偶然見つかった癌は追加治療が不要
  provenance:
    source_ref: SRC-098
    source: National Cancer Institute. Gallbladder Cancer Treatment (PDQ)–Health Professional Version
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/gallbladder/hp/gallbladder-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQが引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)'
    kokushi: 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-064
  domain: BP
  subdomain: 胆道癌
  assertion:
    plain_statement_ja: 切除不能の胆道癌では、ゲムシタビン＋シスプラチンがゲムシタビン単独より全生存期間を延ばし（中央値11.7か月対8.1か月、HR 0.64）、これに免疫チェックポイント阻害薬（デュルバルマブまたはペムブロリズマブ）を加えることが標準治療とされる。
    condition:
      source: NCI PDQ
      region: 米国
    differential: null
    common_misconception: 切除不能胆道癌に有効な薬物療法はない
  provenance:
    source_ref: SRC-098
    source: National Cancer Institute. Gallbladder Cancer Treatment (PDQ)–Health Professional Version
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/gallbladder/hp/gallbladder-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 数値はPDQが引用したRCTの値（二次資料経由）。TOPAZ-1とKEYNOTE-966の生存期間の値は原著で照合してから別カードにする。日本での承認状況は添付文書で確認する
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)'
    kokushi: 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-065
  domain: BP
  subdomain: 胆道癌
  assertion:
    plain_statement_ja: 胆管癌は、肝門部領域に約50%、遠位胆管に約40%、肝内に約10%が発生し、多くは多発性で切除できないことが多い。危険因子には原発性硬化性胆管炎、潰瘍性大腸炎、先天性胆道拡張症（総胆管嚢腫）、肝吸虫（Clonorchis sinensis）感染がある。
    condition:
      source: NCI PDQ
    differential: 膵頭部癌による遠位胆管閉塞
    common_misconception: 胆管癌の多くは肝内に発生する
  provenance:
    source_ref: SRC-099
    source: National Cancer Institute. Bile Duct Cancer (Cholangiocarcinoma) Treatment (PDQ)–Health Professional Version（最終更新 2025-03-28）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/liver/hp/bile-duct-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)；TBL-01-00-293 (id: Jlvnl7Q)'
    kokushi: 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-066
  domain: BP
  subdomain: 胆道癌
  assertion:
    plain_statement_ja: 遠位胆管癌の25〜30%は完全切除が可能で、より肝門側の腫瘍ほど切除率は低い。肝門部胆管癌に積極的な手術を行った場合の5年生存率は20〜50%と報告されている。
    condition:
      source: NCI PDQ
    differential: null
    common_misconception: 胆管癌は全例で切除可能
  provenance:
    source_ref: SRC-099
    source: National Cancer Institute. Bile Duct Cancer (Cholangiocarcinoma) Treatment (PDQ)–Health Professional Version（最終更新 2025-03-28）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/liver/hp/bile-duct-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: PDQが引用した研究の値（二次資料経由）
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)；TBL-02-07-023 (id: JlAKpks)'
    kokushi: 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-067
  domain: BP
  subdomain: 胆道癌
  assertion:
    plain_statement_ja: 胆道癌の完全切除後に補助療法としてカペシタビンと経過観察を比べたRCT（BILCAP、447例）では、全生存期間の中央値は49.6か月対36.1か月で、有意差はなかった（調整HR 0.84、95%CI 0.67〜1.06）。それでもカペシタビンは補助療法の標準として位置づけられている。
    condition:
      source: NCI PDQ
      region: 米国
    differential: null
    common_misconception: BILCAP試験でカペシタビンは全生存期間を有意に延長した
  provenance:
    source_ref: SRC-099
    source: National Cancer Institute. Bile Duct Cancer (Cholangiocarcinoma) Treatment (PDQ)–Health Professional Version（最終更新 2025-03-28）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/liver/hp/bile-duct-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: 数値はPDQが引用した値（二次資料経由）。日本の標準は胆道癌診療GLで確認する
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)'
    kokushi: 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
- id: BP-068
  domain: BP
  subdomain: 胆道癌
  assertion:
    plain_statement_ja: AJCC第8版では、遠位胆管癌のT分類を胆管壁への浸潤の深さで決め、5 mm未満をT1、5〜12 mmをT2、12 mmを超えるものをT3とする。肝内胆管癌では、脈管侵襲のない単発で5 cm以下をT1a、5 cmを超えるものをT1bとする。
    condition:
      source: NCI PDQ
      staging: AJCC 第8版
    differential: null
    common_misconception: 胆管癌のT分類は腫瘍径だけで決まる
  provenance:
    source_ref: SRC-099
    source: National Cancer Institute. Bile Duct Cancer (Cholangiocarcinoma) Treatment (PDQ)–Health Professional Version（最終更新 2025-03-28）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.cancer.gov/types/liver/hp/bile-duct-treatment-pdq
    source_license: 米国連邦政府著作物（PDQは原則パブリックドメイン。第三者の図表は除く）
    legal_basis: B
    source_class: GOV_US
    corroboration: null
  uncertainty: null
  curriculum:
    core_curriculum: 'PS-03-04-14 (id: JkxnuYE)；TBL-01-00-651 (id: Jlvnmc4)'
    kokushi: 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a）
  publication_info:
    created: '2026-10-13'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カード一覧（ID・出典・国試出題基準）

| ID | サブ領域 | SRC | 国試出題基準 |
|---|---|---|---|
| BP-001 | 胆石症・胆道感染症 | SRC-094 | 医学各論 Ⅵ-7-D-①（胆石症、a） |
| BP-002 | 胆石症・胆道感染症 | SRC-094 | 医学各論 Ⅵ-7-B-②（胆管炎、a） |
| BP-003 | 胆石症・胆道感染症 | SRC-094 | 医学各論 Ⅵ-7-B-②（胆管炎、a） |
| BP-004 | 胆石症・胆道感染症 | SRC-094 | 医学各論 Ⅵ-7-B-②（胆管炎、a） |
| BP-005 | 胆石症・胆道感染症 | SRC-094 | 医学各論 Ⅵ-7-B-②（胆管炎、a） |
| BP-006 | 胆石症・胆道感染症 | SRC-094 | 医学各論 Ⅵ-7-B-①（胆囊炎、a） |
| BP-007 | 原発性硬化性胆管炎 | SRC-092 | 医学各論 Ⅵ-7-B-③（原発性硬化性胆管炎、c） |
| BP-008 | 原発性硬化性胆管炎 | SRC-092 | 医学各論 Ⅵ-7-B-③（原発性硬化性胆管炎、c） |
| BP-009 | 原発性硬化性胆管炎 | SRC-092 | 医学各論 Ⅵ-7-B-③（原発性硬化性胆管炎、c） |
| BP-010 | 原発性硬化性胆管炎 | SRC-092 | 医学各論 Ⅵ-7-B-③（原発性硬化性胆管炎、c） |
| BP-011 | 胆道癌 | SRC-091 | 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a） |
| BP-012 | 胆道癌 | SRC-091 | 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a） |
| BP-013 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-014 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-015 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-016 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-017 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-018 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-019 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-020 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-021 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-022 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-023 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-024 | 急性膵炎 | SRC-087 | 医学各論 Ⅵ-8-A-①（急性膵炎、a） |
| BP-025 | 慢性膵炎 | SRC-088 | 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a） |
| BP-026 | 慢性膵炎 | SRC-088 | 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a） |
| BP-027 | 慢性膵炎 | SRC-088 | 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a） |
| BP-028 | 慢性膵炎 | SRC-088 | 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a） |
| BP-029 | 慢性膵炎 | SRC-088 | 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a） |
| BP-030 | 慢性膵炎 | SRC-088 | 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a） |
| BP-031 | 慢性膵炎 | SRC-088 | 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a） |
| BP-032 | 慢性膵炎 | SRC-088 | 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a） |
| BP-033 | 慢性膵炎 | SRC-088 | 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a） |
| BP-034 | 慢性膵炎 | SRC-088 | 医学各論 Ⅵ-8-A-②（慢性膵炎・膵石症、a） |
| BP-035 | 自己免疫性膵炎・IgG4関連疾患 | SRC-093 | 医学各論 Ⅵ-8-A-③（自己免疫性膵炎、b） |
| BP-036 | 自己免疫性膵炎・IgG4関連疾患 | SRC-093 | 医学各論 Ⅵ-8-A-③（自己免疫性膵炎、b） |
| BP-037 | 自己免疫性膵炎・IgG4関連疾患 | SRC-093 | 医学各論 Ⅵ-8-A-③（自己免疫性膵炎、b） |
| BP-038 | 自己免疫性膵炎・IgG4関連疾患 | SRC-093 | 医学各論 Ⅵ-8-A-③（自己免疫性膵炎、b） |
| BP-039 | 膵癌 | SRC-089 | 医学各論 Ⅵ-8-B-①（膵癌、a） |
| BP-040 | 膵癌 | SRC-089 | 医学各論 Ⅵ-8-B-①（膵癌、a） |
| BP-041 | 膵癌 | SRC-089 | 医学各論 Ⅵ-8-B-①（膵癌、a） |
| BP-042 | 膵癌 | SRC-089 | 医学各論 Ⅵ-8-B-①（膵癌、a） |
| BP-043 | 膵癌 | SRC-089 | 医学各論 Ⅵ-8-B-①（膵癌、a） |
| BP-044 | 膵癌 | SRC-089 | 医学各論 Ⅵ-8-B-①（膵癌、a） |
| BP-045 | 膵癌 | SRC-090 | 医学各論 Ⅵ-8-B-①（膵癌、a） |
| BP-046 | 膵癌 | SRC-090 | 医学各論 Ⅵ-8-B-①（膵癌、a） |
| BP-047 | 膵嚢胞性腫瘍 | SRC-096 | 医学各論 Ⅵ-8-B-②（膵囊胞性腫瘍、b） |
| BP-048 | 膵神経内分泌腫瘍 | SRC-095 | 医学各論 Ⅵ-8-B-③（膵神経内分泌腫瘍、b） |
| BP-049 | 膵神経内分泌腫瘍 | SRC-095 | 医学各論 Ⅵ-8-B-③（膵神経内分泌腫瘍、b） |
| BP-050 | 膵神経内分泌腫瘍 | SRC-095 | 医学各論 Ⅵ-8-B-③（膵神経内分泌腫瘍、b） |
| BP-051 | 膵神経内分泌腫瘍 | SRC-095 | 医学各論 Ⅵ-8-B-③（膵神経内分泌腫瘍、b） |
| BP-052 | 膵神経内分泌腫瘍 | SRC-095 | 医学各論 Ⅵ-8-B-③（膵神経内分泌腫瘍、b） |
| BP-053 | 胆石症 | SRC-097 | 医学各論 Ⅵ-7-D-①（胆石症、a） |
| BP-054 | 胆石症 | SRC-097 | 医学各論 Ⅵ-7-D-①（胆石症、a） |
| BP-055 | 胆石症 | SRC-097 | 医学各論 Ⅵ-7-D-①（胆石症、a） |
| BP-056 | 胆石症 | SRC-097 | 医学各論 Ⅵ-7-D-①（胆石症、a） |
| BP-057 | 胆石症 | SRC-097 | 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a） |
| BP-058 | 胆石症 | SRC-097 | 医学各論 Ⅵ-7-D-①（胆石症、a） |
| BP-059 | 胆石症 | SRC-097 | 医学各論 Ⅵ-7-D-①（胆石症、a） |
| BP-060 | 胆石症 | SRC-097 | 医学各論 Ⅵ-7-D-①（胆石症、a） |
| BP-061 | 胆石症 | SRC-097 | 医学各論 Ⅵ-7-D-①（胆石症、a） |
| BP-062 | 胆道癌 | SRC-098 | 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a） |
| BP-063 | 胆道癌 | SRC-098 | 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a） |
| BP-064 | 胆道癌 | SRC-098 | 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a） |
| BP-065 | 胆道癌 | SRC-099 | 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a） |
| BP-066 | 胆道癌 | SRC-099 | 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a） |
| BP-067 | 胆道癌 | SRC-099 | 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a） |
| BP-068 | 胆道癌 | SRC-099 | 医学各論 Ⅵ-7-C-②（胆囊癌、胆管癌、a） |

## 4. 重複回避と境界の確認

- PBC・自己免疫性肝炎は第4回（LV）で扱い済みです。今回は PSC と IgG4 関連疾患（自己免疫性膵炎・IgG4 関連硬化性胆管炎）を扱いました。
- 十二指腸憩室と Lemmel 症候群は GD-093〜095 で扱い済みのため作っていません。
- 急性腹症としての胆嚢炎・膵炎の初期鑑別は、第6回（AB）で症候の側から扱ってください。

## 5. 再検討と補充ラウンド（2026-10-14）

### 5-1. 既存カードの修正（ID は変えていない）

| ID | 修正内容 |
|---|---|
| BP-001 | 胆石症 GL 2021（BP-054）の有症状化率（10年で10〜20%）と食い違うことが分かった。どちらの GL の記述かが分かる書き方にし、食い違いを uncertainty に明記した。分母が読み取れない急性胆管炎・胆嚢炎の発生率は主張文から外した |
| BP-002 | 出典 GL の記述であることを明記した |
| BP-005 | 中等症の胆道ドレナージを「早期」から「緊急ないし早期」に直した（出典の表現に合わせた） |
| BP-008 | 出典にない differential（PBC と IBD の関係）を削除した |
| BP-019・041 | 出典にない differential（米国 GL・欧米の補助療法との比較）を削除した |
| BP-022 | 出典にない「同じ入院中の」を削除した |

### 5-2. 追加分（BP-053〜068）

| トピック | ID | 出典 |
|---|---|---|
| 胆石症（成因、自然史、予防的胆嚢摘出の適応、胆嚢癌との関係、総胆管結石の診断、肝内結石、内科治療、乳頭機能） | BP-053〜061 | SRC-097（胆石症 GL 2021） |
| 胆嚢癌（偶発癌の予後、再切除、切除不能例の薬物療法） | BP-062〜064 | SRC-098（NCI PDQ） |
| 胆管癌（部位、危険因子、切除率、BILCAP、AJCC 第8版の T 分類） | BP-065〜068 | SRC-099（NCI PDQ） |

## 6. なお未作成のトピック（欠番補完ラウンドで扱う）

- **TG18 の診断基準と重症度判定基準の表**：Wiley の英語版は今回も取得エラーでした。Minds 掲載の日本語版 PDF は、表の載っている後半を読めませんでした。J-STAGE の PDF は robots.txt で取得が禁止されています。Claude Code で Minds の PDF（`https://minds.jcqhc.or.jp/common/summary/pdf/c00467.pdf`）を `.cache/` に取得し、pdfplumber で第Ⅴ・Ⅵ章（診断基準・重症度判定、p.57・p.85 付近）を抽出してから、人間が別カードを起こす方法を勧めます。
- 胆道癌診療 GL 2019 英語版（Wiley、DOI 10.1002/jhbp.870）の本文。日本の補助療法、胆道ドレナージ
- 膵・胆管合流異常、先天性胆道拡張症（J-STAGE の総説は抄録しか読めず、数値がなかった）
- 胆嚢ポリープの扱い（10 mm 超を胆嚢癌の高リスクとする記述だけ BP-056 に入れた）、胆嚢腺筋腫症
- IPMN・MCN の具体的な基準（京都ガイドラインは抄録のみ）
- 総胆管結石の内視鏡治療の比較（EST、EPBD、EPLBD）、総胆管結石除去後の胆嚢摘出の時期

これらには ID を割り当てていないため、欠番は生じていません。

## 7. Claude Code での照合時に重点的に確認する点

1. **CC 種別の確定**：SRC-088・089 は Crossref の license 欄で確定する。SRC-096 は Elsevier の license 欄を確認する。
2. **書誌の補完**：SRC-088 の著者・巻・頁を Crossref から取得する。PMCID（SRC-088：PMC9522716、SRC-089：PMC10066137）は検索結果の記事名との一致で付けたものなので、API で照合する。
3. **GL からの孫引き数値**（uncertainty に「二次資料経由」と記載）：BP-001・BP-002・BP-004・BP-023・BP-024・BP-025・BP-027・BP-032・BP-034・BP-054・BP-055・BP-058・BP-063・BP-064・BP-066・BP-067。原著抄録と照合し、合わなければ `proposals/` に修正案を出す。
4. **BP-015（急性膵炎の予後因子）**：GL 本文の表と、項目と閾値が完全に一致するかを人間が確認する。
5. **BP-005・006（TG18 の重症度）**：判定項目の閾値は今回未取得。補充ラウンドで TG18 の表から別カードを起こす。
6. **国内の承認・保険**：BP-043（オラパリブ、ペムブロリズマブ）を添付文書で確認する。
7. **米国データのカード**：BP-048〜052（NCI PDQ の膵 NET）、BP-062〜068（NCI PDQ の胆嚢癌・胆管癌）。日本の資料（膵・消化管 NEN 診療 GL、胆道癌診療 GL）に差し替えられるかを検討する。
8. **BP-001 と BP-054 の食い違い**：無症状胆石の有症状化率が GL によって異なる（5〜10年で約40%と、10年で10〜20%）。両 GL の引用元を原著で照合し、どちらを残すかを人間が決める。
9. **SRC-097（胆石症 GL 2021）**：記事ページでライセンス表示を確認できなかった。Crossref で確定する。SRC-098 は最終更新日を確認する。
10. **BP-064（切除不能胆道癌）**：日本でのデュルバルマブ・ペムブロリズマブの承認状況を添付文書で確認する。

## 8. 第6回（腹膜・腹壁・急性腹症、接頭辞 AB）への引き継ぎ

- SRC 番号は SRC-100 から。
- 急性腹症診療ガイドライン 2025 は本プロジェクトの関係者が作成に関わっているため、利益相反の記載と、出典にする版（日本語版・英語版）の本文の範囲を明確にする。
- 第5回の未作成トピックを補充するときは、許可の確認に答えられる状態で実行すると、Wiley・Springer の記事ページを読める見込みがある。
