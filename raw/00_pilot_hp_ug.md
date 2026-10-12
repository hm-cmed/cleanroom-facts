# 消化器パイロット（H. pylori関連疾患／上部消化管出血）：抽出元ホワイトリスト・カリキュラム対応表・事実票・MCQ設計図

**結論：パイロットは実施できます。** 中核は、CC BY 4.0で公開された日本の2つのガイドライン英語版です。\[1\]\[2\]一つは日本消化器病学会（JSGE）の消化性潰瘍診療ガイドライン2026英語版、もう一つは日本ヘリコバクター学会（JSHR）のH. pylori感染の診断と治療のガイドライン2024改訂版英語版です。これに原著論文の事実部分を組み合わせます。一方、ACG・JGES（日本消化器内視鏡学会）・Maastricht VI・Kyoto・Okimotoサーベイランスは、非CC、NC、またはND条件付きのライセンスです。これらは「事実（タグB）のみ抽出、文章・表は使わない」か「人間による検証参照のみ」に分けて扱うのが妥当です。

## TL;DR
- **ホワイトリストの中核はCC BY 4.0の2本です**（JSGE消化性潰瘍GL 2026、DOI 10.1007/s00535-026-02504-3／JSHR H. pylori GL 2024改訂版英語版、DOI 10.1007/s00535-026-02379-4）。JGES出血GL第2版（Wiley標準条件）、ACGの2本（©ACG）、Maastricht VI（商用再利用不可）、Kyoto（CC BY-NC 4.0）、Okimoto耐性サーベイランス（CC BY-NC-ND 4.0）は、数値・推奨の「事実」だけをタグBで自作文に落とし、文言・表・図は使いません。
- **カリキュラムの骨格はPS-02-08-05-2（胃・十二指腸疾患：消化性潰瘍、H. pylori感染症、慢性胃炎）、PS-03-04-14（胃癌を含む消化器腫瘍）、表2-7（消化器系：吐血・下血・内視鏡治療・血管内治療）です。** 国試出題基準（令和6年版）の項目番号は、厚労省PDFを自動取得できなかったため**全て要確認**です。
- **日本と欧米の推奨差は主に2点で、条件フィールドで区別します。** 1点目は除菌一次治療で、日本はボノプラザン（VPZ）ベース＋可能ならCAM感受性検査、欧州はCAM耐性率>15%等で14日ビスマス4剤を推奨します。2点目は止血後のP-CABで、JSGE 2026は弱い推奨、ESGE 2026は「合意に至らず」です。事実票38件（H. pylori 20件、UGIB 18件）、30問ブループリント、サンプルMCQ 4問を以下に示します。

---

## Key Findings

1. **ライセンス確認の結果、「オープンアクセス＝自由に構造化利用可」ではありません。** Springer（J Gastroenterol）の日本の2ガイドラインはCrossrefのライセンスメタデータでCC BY 4.0と確認できました。\[1\]\[2\]一方、JGES出血ガイドライン第2版（Digestive Endoscopy）は、CrossrefでWiley標準利用条件（termsAndConditions#vor）のみが示され、CCライセンスではありません。\[3\]Okimotoらの日本の耐性サーベイランス（Helicobacter誌）はCC BY-NC-ND 4.0です。\[4\]
2. **日本の数値の最重要アンカーは、CAM耐性率35.5%（2018–2020年）です。** AMPC耐性は2.7%、MNZ耐性は4.2%でした（Okimoto 2024）。\[4\]\[5\]\[6\]この数値はJSGE 2026（CC BY）にも引用されているため、CC BY文献経由で事実として扱えます。\[6\]\[7\]
3. **JSGE 2026の主な変更点は、VPZが消化性潰瘍とNSAID／LDA潰瘍の第一選択になったことです。** 除菌では、VPZ三剤が一次除菌で強い推奨（エビデンスA）、CAM感受性検査は可能なら一次除菌前に実施（強い推奨・A）とされました。\[7\]
4. **UGIBの数値アンカーは欧米ガイドラインの「事実」です。** GBS 0–1は外来管理、輸血閾値はHb 7 g/dL、\[8\]内視鏡は蘇生後24時間以内（12時間以内の緊急内視鏡は推奨しない）。\[9\]\[10\]ただしACG・ESGEの文言は利用しません。
5. **コアカリIDは二次情報で確定させました。** 公式GitHubリポジトリ（core-curriculum/data）のライセンスは「文部科学省ウェブサイト利用規約」に従うと明記されています。\[11\]学修目標コードは山口大学シラバスの引用で確認しましたが、\[12\]id文字列はGitHubのCSVで最終照合が必要です（要確認）。

---

## 1. 抽出元ホワイトリスト（ライセンス確認済み／未確認を明示）

### 1-A. 日本の学会ガイドライン・原著

| # | 資料 | DOI/URL | 確認したライセンス・利用条件 | 推奨タグ | 注意点 |
|---|---|---|---|---|---|
| J1 | JSGE 消化性潰瘍診療ガイドライン2026（第4版）英語版, J Gastroenterol 61:1361–1381\[7\] | 10.1007/s00535-026-02504-3 | Open access、© The Author(s) 2026。Crossrefメタデータで**CC BY 4.0**（2026-08-24発効）\[1\] | **B（主）／F（図表の翻案時）** | 英語版は25 CQ＋4 FRQで、日本語版の15 BQは含みません。\[7\]日本語本編（南江堂）は商用書籍のため抽出元にしません。 |
| J2 | JSHR H. pylori感染の診断と治療のガイドライン2024改訂版 英語版, J Gastroenterol 61:841–862\[13\] | 10.1007/s00535-026-02379-4 | Open access、© The Author(s) 2026。Crossrefで**CC BY 4.0**\[2\] | **B／F** | 日本語原本（先端医学社）は商用書籍のため、抽出元にせず人間参照のみとします。保険適用外の推奨を含みます。\[6\] |
| J3 | JSGE 消化性潰瘍診療ガイドライン2020 英語版, J Gastroenterol 56:303–322\[14\] | 10.1007/s00535-021-01769-0 | Springerで「Open access」と表示。\[7\]CCの種別は**未確認（要確認）** | B（暫定） | 2026版で置き換わった部分（VPZの位置づけ等）があるため、旧版と明示して使います。 |
| J4 | JGES 非静脈瘤性上部消化管出血における内視鏡診療ガイドライン（第2版）, Dig Endosc 37:447–469 (2025)\[15\] | 10.1111/den.15019 | Crossrefで**Wiley標準利用条件のみ（CC表示なし）**\[3\] | **人間検証参照（G要）**。推奨の存在そのものはBで最小限 | 推奨文の構造化・転載には許諾が必要と判断します。代替として、引用元のRCTを一次ソースにします。 |
| J5 | Okimoto T et al. 日本の薬剤耐性サーベイランス2018–2020, Helicobacter 2024;29:e13028\[4\] | 10.1111/hel.13028\[5\] | Crossrefで**CC BY-NC-ND 4.0**\[4\] | **B（数値のみ）** | 本文・表の翻案は不可（ND）、商用不可（NC）です。耐性率の数値は事実として自作文で使えます。 |
| J6 | Murakami K et al. VPZ三剤 第III相RCT, Gut 2016;65:1439–46\[7\]\[16\] | DOI 10.1136/gutjnl-2015-311304、PMID 26935876、PMC5036253（PubMedのコメント記事PMID 27210791とClinicalTrials.gov NCT04901663の文献リストで確認） | **未確認**（PMCで無料公開。BMJのOpen Access表示は検索スニペットでのみ確認、CCの種別は未確認） | B（数値のみ） | 数値（92.6% vs 75.9%）は二次文献とJSGE 2026の記載で裏付けを取ります。 |

### 1-B. 欧米・国際ガイドライン／コンセンサス

| # | 資料 | DOI/URL | ライセンス | 推奨タグ | 注意点 |
|---|---|---|---|---|---|
| W1 | Maastricht VI/Florence, Gut 2022;71:1724–1762\[17\] | 10.1136/gutjnl-2022-327745（PMID 35944925）\[17\] | PubMed表示「No commercial re-use. See rights and permissions」→\[17\] **CC BY-NC系（種別は要確認）** | **B（推奨の要旨のみ）** | NCのため、有償教材化の予定があれば文言・表は使いません。 |
| W2 | Kyoto global consensus report on H. pylori gastritis, Gut 2015;64:1353–67\[18\] | 10.1136/gutjnl-2015-309252（PMID 26187502）\[19\] | **CC BY-NC 4.0**（BMJ OA表示を転載ミラーで確認）\[20\] | B | NC条件があります。「H. pylori胃炎は感染症」という位置づけは事実として利用できます。 |
| W3 | ACG Clinical Guideline: Treatment of H. pylori Infection, Am J Gastroenterol 2024;119:1730–53\[21\] | 10.14309/ajg.0000000000002968 | **© 2024 ACG**（CC表示なし）\[22\] | **人間検証参照**、事実のみB | JCAG誌の解説論文（CC BY）に要約があり、\[23\]その解説の事実部分ならB/Fで使えます。 |
| W4 | ACG Clinical Guideline: Upper GI and Ulcer Bleeding, Am J Gastroenterol 2021;116:899–917\[24\] | 10.14309/ajg.0000000000001245（PMID 33929377）\[25\] | **© 2021 ACG**（全文は無料公開だがCCではない）\[26\] | 人間検証参照、事実のみB | 「無料で読める」ことと「再利用可」は別です。 |
| W5 | ESGE NVUGIH Guideline Update 2021, Endoscopy 53:300–332\[27\] | 10.1055/a-1369-5274（PMID 33567467）\[28\]\[29\] | **未確認**（Thieme。CC BY-NC-ND系の可能性があり要確認） | B（要旨のみ） | ライセンス確認までは事実のみ扱います。 |
| W6 | ESGE Peptic ulcer bleeding Guideline Update 2026, Endoscopy 2026\[30\] | 10.1055/a-2863-8314（PMID 42127996、訂正 10.1055/a-2881-7411）\[31\]\[32\] | **未確認** | B（要旨のみ） | 2021版を置き換えるため、最新版として優先します。\[33\]\[34\] |
| W7 | International Consensus（Barkun 2019, Ann Intern Med） | PMC7233308（NIHPA著者原稿）\[35\] | **未確認**。NIH Public Access著者原稿はCCではないのが通例 | 人間検証参照 | 疫学の数値のみBで使います。 |

### 1-C. 公的資料（日本・米国）

| # | 資料 | URL | 利用条件 | 推奨タグ | 注意点 |
|---|---|---|---|---|---|
| G1 | 医学教育モデル・コア・カリキュラム令和4年度改訂版（PDF/Excel、文科省）\[36\] | https://www.mext.go.jp/b_menu/shingi/chousa/koutou/116/toushin/mext_01280.html | 文部科学省ウェブサイト利用規約（政府標準利用規約準拠かは要確認） | F（出典表示） | 骨格として使います。 |
| G2 | core-curriculum/data（GitHub、CSV）\[37\] | https://github.com/core-curriculum/data | READMEに「文部科学省ウェブサイト利用規約に従って利用」と明記\[11\] | F | 現時点では第1章・第2章のみ掲載。id（不変）とindex（改訂で変わり得る）を併記します。\[11\] |
| G3 | 令和6年版医師国家試験出題基準（厚労省）\[38\] | https://www.mhlw.go.jp/stf/shingi2/0000128981_00001.html | 厚労省サイト利用規約（要確認） | F（項目名の参照） | 第118回試験から適用。医学各論の疾患にa/b/cレベル分類があります。\[39\]\[40\] |
| G4 | 国立がん研究センター がん情報サービス | https://ganjoho.jp/aboutus/attention/copyright.html | 改変のない原文で出典を明記すれば複製・転載・公衆送信が可能。**改変利用、意味を取り違える部分利用、原意と異なる生成AI出力は不可**（2026-06-09更新）\[41\] | **B（事実のみ）**、原文転載ならF相当 | 「改変不可」のため、自作文へのリライト素材としてAIに入力しないでください。統計値は事実として出典を明記して使います。 |
| G5 | 厚労省 患者調査（2023） | https://www.mhlw.go.jp/toukei/saikin/hw/kanja/23/index.html | 政府統計（公共データ利用規約想定、要確認） | B/F | 胃潰瘍・十二指腸潰瘍の患者数に使います（JSGE 2026経由で確認）。\[7\] |
| G6 | NIH/NCI/NIDDK の患者向け・専門家向け情報 | 各サイト | 米国連邦政府著作物は原則パブリックドメインだが、第三者画像等は除く（**今回は未確認、要確認**） | C | 個別ページの著作権表示を確認してから登録します。 |

**タグ運用のルール：** 事実票の「主張文（plain_statement_ja）」は常に自作で、タグはAかBです。provenance側には原典のライセンス（CC BY／NC／ND／©）を必ず記録し、NC・ND・©の原典からは「数値と推奨の方向性」以外を持ち込みません。

---

## 2. カリキュラム対応表

### 2-A. コアカリ（令和4年度改訂版）

| コアカリindex | 内容（要旨） | 該当テーマ | 確認状況 |
|---|---|---|---|
| PS-02-08 | 消化器系（表2-7）\[12\] | 両テーマの親 | 二次情報（山口大学シラバス） |
| **PS-02-08-05-2** | 胃・十二指腸疾患（消化性潰瘍、*H. pylori*感染症、急性胃粘膜病変、慢性胃炎、機能性ディスペプシア等）の病因・疫学・症候・検査・診断・治療を理解する\[12\] | H. pylori感染症／慢性胃炎／消化性潰瘍／除菌 | 同上。id文字列は要確認 |
| PS-02-08-05-4 | 消化管共通疾患（薬物性消化管障害等）\[12\] | NSAID・LDA潰瘍、抗血栓薬 | 同上 |
| **PS-03-04-14** | 主な消化器腫瘍（食道癌、胃癌、大腸癌等）の症候・診断・治療\[12\] | 胃癌予防 | 同上 |
| PS-03-03 | 感染症（表2-18）\[12\] | H. pylori感染症（病原体としての側面） | 該当行は要確認 |
| 表2-7 症候 | 吐血、下血、腹痛、悪心・嘔吐、胸やけ\[42\] | 上部消化管出血 | コアカリナビ（https://core-curriculum.jp/tables/TBL0207）で確認 |
| 表2-7 検査方法 | 内視鏡検査、生検・細胞診\[42\] | 両テーマ | 同上 |
| 表2-7 特異的治療法 | 内視鏡治療（止血・凝固・クリッピング・硬化療法等）、血管内治療（動脈塞栓術等）\[42\] | 内視鏡的止血、TAE | 同上 |
| （未特定） | 胃MALTリンパ腫：PS-02-08-05-2とPS-03-04-14には記載なし。血液・造血器の悪性リンパ腫の項目にある可能性 | MALT | **要確認** |
| （未特定） | 輸血、抗血栓薬・薬物療法 | 輸血閾値、抗血栓薬管理 | **要確認** |

### 2-B. 医師国家試験出題基準（令和6年版）

| 区分 | 該当が想定される項目 | 項目番号 | 原典PDF |
|---|---|---|---|
| 必修の基本的事項 | 主要症候（吐血・下血）、初期救急、輸血、主要疾患（消化性潰瘍、胃癌） | **要確認** | https://www.mhlw.go.jp/content/10803000/001079482.pdf |
| 医学総論 | 検査（内視鏡、尿素呼気試験等）、治療（輸血、薬物療法） | **要確認** | https://www.mhlw.go.jp/content/10803000/001079483.pdf |
| 医学各論（消化器） | H. pylori感染症、慢性胃炎、胃・十二指腸潰瘍、胃癌、胃MALTリンパ腫、上部消化管出血 | **要確認**（a/b/cレベルも要確認） | https://www.mhlw.go.jp/content/10803000/001079484.pdf |

**推奨：** 項目番号は索引PDF（001079485.pdf）を人間が開いて転記し、事実票の`curriculum.kokushi`フィールドに入れてください。出題基準は府省資料なので、項目名を参照するのは問題ありません。

---

## 3. 事実票ドラフト（YAML、38件）

共通の約束事は次のとおりです。`verifier`は空欄、`status: draft`。`basis_tag`は主張文に対するタグ、`source_license`は原典のライセンスです。数値に不確かさがあれば`uncertainty`に「要確認」と書きます。

### 3-A. H. pylori関連疾患（HP-001〜HP-020）

```yaml
- id: HP-001
  assertion:
    plain_statement_ja: "2018〜2020年に日本国内で集めたH. pylori臨床分離株では、クラリスロマイシン耐性が35.5%、アモキシシリン耐性が2.7%、メトロニダゾール耐性が4.2%だった。"\[4\]\[5\]
    condition: {region: JP, period: "2018-08〜2020-12"}
    differential: ["CAM耐性は高く、AMPC・MNZ耐性は低い"]\[6\]
    common_misconception: "日本ではMNZ耐性が高いので二次除菌が効きにくい（誤り：MNZ耐性は低い）"
  provenance:
    source: "Okimoto T et al. Helicobacter 2024;29:e13028"
    doi: "10.1111/hel.13028"
    source_license: "CC BY-NC-ND 4.0"
    basis_tag: B
    corroboration: "JSGE PUD GL 2026 CQ-3（DOI 10.1007/s00535-026-02504-3, CC BY 4.0）"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-002
  assertion:
    plain_statement_ja: "日本の第III相二重盲検RCTでは、一次除菌（三剤）の除菌率がボノプラザン群92.6%、ランソプラゾール群75.9%だった。"\[43\]\[44\]
    condition: {region: JP, regimen: "VPZ/LPZ + AMPC + CAM, 7日"}
    common_misconception: "P-CABでもPPIでも除菌率は同じ"
  provenance:
    source: "Murakami K et al. Gut 2016;65:1439-46"
    doi: "10.1136/gutjnl-2015-311304"
    pmid: "26935876"
    pmcid: "PMC5036253"
    source_license: "未確認（PMCで無料公開、CC種別は未確認）"
    basis_tag: B
    corroboration: "Springer Adv Ther 2021 (10.1007/s12325-021-01784-w) の記載"
  uncertainty: "DOI・PMIDはPubMedのコメント記事（PMID 27210791）とClinicalTrials.gov NCT04901663の文献リストで確認。ライセンスは要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-003
  assertion:
    plain_statement_ja: "同じRCTのCAM耐性株感染例では、除菌率がボノプラザン三剤で82.0%、ランソプラゾール三剤で40.0%だった（p<0.0001）。"
    condition: {region: JP, strain: "CAM耐性（n=100 vs 115）"}
    differential: ["CAM感受性株ではVPZ三剤97.6%、LPZ三剤97.3%と差がなかった"]
  provenance:
    source: "Murakami 2016 原著本文（PMC5036253、online supplementary table S1参照）; Frontiers Pharmacol 2018 (10.3389/fphar.2018.01560)"
    source_license: "未確認"
    basis_tag: B
  uncertainty: "数値は原著本文で確認済み。ライセンスは要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-004
  assertion:
    plain_statement_ja: "JSGE 2026は、一次除菌ではPPIよりボノプラザンを含む三剤療法を用いることを強く推奨している（エビデンスA、7件のRCTのメタ解析）。"\[7\]
    condition: {region: JP, guideline: "JSGE PUD 2026 CQ-2"}
    differential: ["欧州（Maastricht VI）は経験的一次治療に14日ビスマス4剤を推奨"]\[45\]
  provenance:
    source: "JSGE PUD GL 2026"
    doi: "10.1007/s00535-026-02504-3"
    source_license: "CC BY 4.0"
    basis_tag: B
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-005
  assertion:
    plain_statement_ja: "JSGE 2026は、可能であれば一次除菌前にCAM感受性検査を行い、最も高い除菌率が見込めるレジメンを選ぶよう強く推奨している。"\[6\]\[7\]
    condition: {region: JP, guideline: "CQ-3"}
    common_misconception: "感受性検査は除菌失敗後にだけ行う"
  provenance: {source: "JSGE PUD GL 2026", doi: "10.1007/s00535-026-02504-3", source_license: "CC BY 4.0", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-006
  assertion:
    plain_statement_ja: "CAM感受性株にはVPZ＋AMPC＋CAMを、CAM耐性株にはPPIまたはVPZ＋AMPC＋MNZを用いることが推奨されている。"\[7\]
    condition: {region: JP, guideline: "CQ-4", strength: "いずれも強い推奨"}
    differential: ["耐性株にCAM含有レジメンを使い続けるのは誤り"]
  provenance: {source: "JSGE PUD GL 2026", doi: "10.1007/s00535-026-02504-3", source_license: "CC BY 4.0", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-007
  assertion:
    plain_statement_ja: "日本の二次除菌の推奨レジメンは、標準量PPIまたはVPZ 20 mg、AMPC 750 mg、MNZ 250 mgを1日2回・1週間投与するもので、PPIとVPZで除菌率は同等とされる。"\[7\]
    condition: {region: JP, line: second, guideline: "CQ-2（弱い推奨, B）"}
    common_misconception: "二次除菌でも必ずVPZでなければならない"
  provenance: {source: "JSGE PUD GL 2026", doi: "10.1007/s00535-026-02504-3", source_license: "CC BY 4.0", basis_tag: B}
  uncertainty: "用量は保険診療上の用法と照合を要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-008
  assertion:
    plain_statement_ja: "欧州のMaastricht VI/Florenceコンセンサスは、感受性が不明な場合やCAM耐性率が15%を超える地域では、経験的一次治療として14日間のビスマス4剤療法を推奨している。"\[45\]
    condition: {region: EU, guideline: "Maastricht VI"}
    differential: ["日本：VPZベース＋感受性検査（HP-004〜006）"]
  provenance:
    source: "Malfertheiner P et al. Gut 2022;71:1724-62"
    doi: "10.1136/gutjnl-2022-327745"
    pmid: "35944925"
    source_license: "No commercial re-use（CC BY-NC系、要確認）"
    basis_tag: B
  uncertainty: "推奨文の詳細は二次文献（Microbiota journal 2023 review）経由。原著で要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-009
  assertion:
    plain_statement_ja: "米国ACG 2024は、未治療例の選択肢として最適化ビスマス4剤療法を優先し、感受性が確認されない限りCAMやレボフロキサシンを含むレジメンは避けるよう求めている。"\[21\]\[46\]
    condition: {region: US, guideline: "ACG 2024"}
    differential: ["米国のCAM耐性率は22.2〜31.5%、レボフロキサシン耐性率は37.6%と記載"]\[23\]
  provenance:
    source: "Chey WD et al. Am J Gastroenterol 2024;119:1730-53（要旨はJCAG誌の解説（CC BY）経由）"
    doi: "10.14309/ajg.0000000000002968"
    source_license: "© ACG（原典）／解説記事 CC BY 4.0"
    basis_tag: B
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-010
  assertion:
    plain_statement_ja: "ACG 2024は、未治療例の選択肢として、ビスマス4剤のほか、リファブチン三剤、VPZ＋AMPC二剤、VPZ三剤（いずれも14日間）を挙げている。"\[23\]
    condition: {region: US}
    common_misconception: "米国でも日本と同じ7日間療法が標準"
  provenance: {source: "JCAG 2025 commentary（academic.oup.com/jcag/article/8/3/85/8125707）", source_license: "CC BY 4.0", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-011
  assertion:
    plain_statement_ja: "PPI服用中は尿素呼気試験、迅速ウレアーゼ試験、ペプシノゲン値の信頼性が下がるため、診断にはこれらを用いない。"\[13\]
    condition: {region: JP, guideline: "JSHR 2024 BQ"}
    differential: ["国内のモノクローナル抗体便中抗原検査は施設での検証後に使用可能", "胃液の核酸増幅検査はPPIの影響を受けない"]\[13\]
    common_misconception: "PPI内服中でも尿素呼気試験の陰性は信頼できる"
  provenance: {source: "JSHR GL 2024 英語版", doi: "10.1007/s00535-026-02379-4", source_license: "CC BY 4.0", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-012
  assertion:
    plain_statement_ja: "除菌判定の検査前には、PPIを2週間以上、ビスマスと抗菌薬を4週間以上中止し、治療終了から4週間以上あけて判定する。"\[47\]\[48\]
    condition: {region: US, guideline: "ACG 2024（要旨）"}
    differential: ["H2RAや制酸薬は判定精度に影響しないとされる", "血清抗体は除菌判定に用いない"]\[47\]
  provenance: {source: "ACG 2024（Emory大学の要約資料経由）", doi: "10.14309/ajg.0000000000002968", source_license: "© ACG", basis_tag: B}
  uncertainty: "日本のJSHR推奨期間との異同を要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-013
  assertion:
    plain_statement_ja: "尿素呼気試験のカットオフは除菌前で2.5〜3.5‰、除菌後で3.5〜4.0‰が適切とされ、除菌前に2.5‰を用いた場合の感度は96.2〜100%、特異度は83.3〜100%と報告されている。"\[13\]
    condition: {region: JP, guideline: "JSHR 2024 CQ1-1（強い推奨, B）"}
  provenance: {source: "JSHR GL 2024 英語版", doi: "10.1007/s00535-026-02379-4", source_license: "CC BY 4.0", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-014
  assertion:
    plain_statement_ja: "京都分類に基づく内視鏡所見のうち、現感染を最も強く示すのはびまん性発赤（診断オッズ比26.8）で、粘膜腫脹13.3、白濁粘液10.2、皺襞腫大8.6が続く。"\[13\]
    condition: {region: JP}
    differential: ["びまん性発赤の改善は除菌成功の指標"]\[13\]
    common_misconception: "RACが観察されれば現感染を疑う（RACはむしろ未感染の所見）"
  provenance:
    source: "Yoshii S et al. Dig Endosc 2020;32:74-83（JSHR GL 2024で引用）"
    doi: "10.1007/s00535-026-02379-4（引用元）"
    source_license: "引用元 CC BY 4.0／原著は要確認"
    basis_tag: B
  uncertainty: "RACに関する誤解例は専門医確認を要する"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-015
  assertion:
    plain_statement_ja: "JSHR 2024は、H. pylori感染症はすべて除菌の適応であるという基本方針を維持している。"\[13\]
    condition: {region: JP}
    differential: ["米国ACGも『感染が判明した全例を治療』とする"]\[48\]
  provenance: {source: "JSHR GL 2024 英語版（抄録）", doi: "10.1007/s00535-026-02379-4", source_license: "CC BY 4.0", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-016
  assertion:
    plain_statement_ja: "胃癌予防の観点からは、より若い年齢での除菌が推奨され、日本では中学生の時期での検査と除菌が予防戦略として強調されている。"\[13\]
    condition: {region: JP, population: "思春期"}
    differential: ["欧州小児ガイドラインは無症状小児へのtest-and-treatを推奨しない"]\[49\]
  provenance: {source: "JSHR GL 2024 英語版", doi: "10.1007/s00535-026-02379-4", source_license: "CC BY 4.0", basis_tag: B}
  uncertainty: "推奨の強さとエビデンスレベルは要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-017
  assertion:
    plain_statement_ja: "京都グローバルコンセンサスは、H. pylori胃炎を症状の有無にかかわらず感染症として位置づけた。"
    condition: {region: global}
    common_misconception: "無症状のH. pylori胃炎は治療対象ではない"
  provenance:
    source: "Sugano K et al. Gut 2015;64:1353-67"
    doi: "10.1136/gutjnl-2015-309252"
    pmid: "26187502"
    source_license: "CC BY-NC 4.0"
    basis_tag: B
  uncertainty: "『症状の有無にかかわらず』の表現は原著で要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-018
  assertion:
    plain_statement_ja: "日本の胃潰瘍患者数は2023年に年間19.4万人、十二指腸潰瘍は2.0万人まで減少し、40年前と比べるとそれぞれ約10分の1、約20分の1になった。"\[7\]
    condition: {region: JP, year: 2023}
    differential: ["減少の背景：除菌の保険適用拡大、VPZの導入、薬剤性潰瘍の予防"]\[7\]
  provenance:
    source: "厚労省 患者調査2023（JSGE PUD GL 2026の序論で引用）"
    url: "https://www.mhlw.go.jp/toukei/saikin/hw/kanja/23/index.html"
    source_license: "政府統計（利用規約は要確認）／引用元 CC BY 4.0"
    basis_tag: B
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-019
  assertion:
    plain_statement_ja: "H. pylori陰性かつNSAID非使用の消化性潰瘍（特発性潰瘍）と、非H. pyloriヘリコバクター（NHPH）感染による潰瘍の増加が注目されている。"\[7\]
    condition: {region: JP}
    common_misconception: "H. pylori陰性でNSAIDも使っていなければ潰瘍は起こらない"
  provenance: {source: "JSGE PUD GL 2026（抄録）", doi: "10.1007/s00535-026-02504-3", source_license: "CC BY 4.0", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: HP-020
  assertion:
    plain_statement_ja: "H. pylori陽性の限局期胃MALTリンパ腫では、除菌療法が一次治療として位置づけられている。"\[50\]\[51\]
    condition: {region: JP/EU}
    differential: ["除菌後も残存・進行する場合は放射線療法などを検討"]
  provenance:
    source: "JSHR GL 2024（除菌適応疾患の一覧）／Maastricht VI"
    source_license: "CC BY 4.0／NC"
    basis_tag: B
  uncertainty: "該当CQ番号、寛解率の数値、t(11;18)陽性例の扱いは要確認。完全寛解率の一次ソース（メタ解析PMID）は未取得"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}
```

### 3-B. 上部消化管出血（UG-001〜UG-018）

```yaml
- id: UG-001
  assertion:
    plain_statement_ja: "救急外来を受診した上部消化管出血のうち、院内での介入または死亡の見逃し率が1%以下となる超低リスク例（例：Glasgow-Blatchfordスコア0〜1）は、入院させず外来フォローで帰宅させることが提案されている。"
    condition: {region: US, guideline: "ACG 2021（条件付き推奨, 非常に低い質）"}\[8\]\[25\]
    differential: ["GBSは内視鏡前のリスク層別化に使う。Rockallスコア（完全版）は内視鏡所見を必要とする"]\[52\]
    common_misconception: "GBS 0〜1でも全例を緊急内視鏡にすべき"
  provenance:
    source: "Laine L et al. Am J Gastroenterol 2021;116:899-917"
    doi: "10.14309/ajg.0000000000001245"
    pmid: "33929377"\[53\]
    source_license: "© ACG"
    basis_tag: B
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-002
  assertion:
    plain_statement_ja: "GBS 0の感度の点推定値は99〜100%だが、特異度は8〜22%と低い。"\[54\]
    condition: {region: US}
    common_misconception: "GBSは特異度が高いので入院適応の判定に強い"
  provenance: {source: "ACG 2021", doi: "10.14309/ajg.0000000000001245", source_license: "© ACG", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-003
  assertion:
    plain_statement_ja: "上部消化管出血の入院患者では、Hb 7 g/dLを閾値とする制限輸血が提案されている。"
    condition: {region: US, guideline: "ACG 2021（条件付き推奨, 低い質）"}\[25\]\[55\]
    differential: ["低血圧例や心血管疾患合併例では、より高い閾値を考慮する", "Villanueva 2013では、制限輸血の死亡率上の利益はChild-Pugh A/Bの肝硬変例（4% vs 12%）でみられたが、Child-Pugh C（38% vs 41%, P=0.91）ではみられなかった。急性冠症候群、脳卒中・TIA、大量出血は除外されていた（Wiki Journal Clubの要約）"]
    common_misconception: "Hb 10 g/dLを保つように輸血するほど予後が良い"
  provenance: {source: "ACG 2021", doi: "10.14309/ajg.0000000000001245", source_license: "© ACG", basis_tag: B}
  uncertainty: "心血管疾患合併例の具体的な閾値（8 g/dL等）は要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-004
  assertion:
    plain_statement_ja: "閾値7 g/dLの根拠となった上部消化管出血のRCT（単施設、n=921：制限群461例＜7 g/dL、非制限群460例＜9 g/dL）では、輸血を受けた患者の割合が制限群49%、非制限群86%（P<0.001）で、45日死亡率は5% vs 9%（HR 0.55; 95% CI 0.33–0.92）だった。"
    condition: {region: "EU(Spain, Hospital de Sant Pau, Barcelona)"}
  provenance:
    source: "Villanueva C et al. N Engl J Med 2013;368(1):11-21（ACG 2021が引用）"
    pmid: "23281973"
    doi: "要確認"
    source_license: "© ACG（引用元）"
    basis_tag: B
  uncertainty: "PMIDはPubMedの検索結果で確認。DOIは要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-005
  assertion:
    plain_statement_ja: "システマティックレビューでは、制限輸血によって輸血を受ける患者数が43%減り、臨床的に重要な転帰の悪化は認められなかった。"\[54\]
    condition: {region: global}
  provenance: {source: "ACG 2021", doi: "10.14309/ajg.0000000000001245", source_license: "© ACG", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-006
  assertion:
    plain_statement_ja: "非静脈瘤性上部消化管出血では、循環動態を安定させた後、24時間以内に上部内視鏡を行うことが推奨される。"\[9\]\[56\]\[57\]
    condition: {region: "JP/EU/US"}
    differential: ["ESGEは12時間以内の緊急内視鏡を、転帰が改善しないとして推奨していない"]\[10\]
    common_misconception: "来院後できるだけ早く（蘇生前でも）内視鏡を行うべき"
  provenance:
    source: "JGES NVUGIB GL 第2版（強い推奨）、ESGE 2021、ACG 2021"
    doi: "10.1111/den.15019; 10.1055/a-1369-5274"
    source_license: "Wiley標準条件／未確認"
    basis_tag: B
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-007
  assertion:
    plain_statement_ja: "上部消化管出血が疑われる患者に、スクリーニング目的で経鼻胃管をルーチンに挿入することは推奨されない。"\[56\]
    condition: {region: JP, guideline: "JGES第2版（弱い推奨, エビデンスC）", also: "ESGE 2021（強く非推奨）"}\[56\]
    common_misconception: "胃管吸引で血液がなければ上部出血は否定できる"
  provenance: {source: "JGES NVUGIB GL 第2版", doi: "10.1111/den.15019", source_license: "Wiley標準条件", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-008
  assertion:
    plain_statement_ja: "重症または活動性出血が続く上部消化管出血では、内視鏡の30〜120分前にエリスロマイシン250 mgを単回静注することが推奨される。"\[57\]\[58\]
    condition: {region: EU, guideline: "ESGE"}
    differential: ["ESGE 2026は、エリスロマイシンが使えない場合にメトクロプラミドの静注を提案"]\[31\]
  provenance: {source: "ESGE 2015/2021、ESGE 2026", doi: "10.1055/s-0034-1393172; 10.1055/a-2863-8314", source_license: "未確認", basis_tag: B}
  uncertainty: "日本での保険適用外使用である点を要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-009
  assertion:
    plain_statement_ja: "Forrest分類のIa（噴出性出血）、Ib（湧出性出血）、IIa（露出血管）は高リスク所見で内視鏡的止血の対象となる。IIc（平坦な色素斑）とIII（清浄潰瘍底）は再出血リスクが低く、止血処置を要しない。"\[58\]\[59\]
    condition: {region: global}
    differential: ["IIb（凝血塊付着）：ESGEは凝血塊除去を考慮、ACGは推奨なし"]\[58\]\[60\]
    common_misconception: "黒色の平坦な色素斑（IIc）にもクリップが必要"
  provenance: {source: "ESGE 2015 (10.1055/s-0034-1393172)、ACG 2021", source_license: "未確認／© ACG", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-010
  assertion:
    plain_statement_ja: "ESGE 2026は、高リスク所見（FIa・FIb）の消化性潰瘍出血に対し、再出血がより少ないことから、over-the-scope（OTS）クリップ単独を従来の併用療法に代わる一次治療として提案している。"
    condition: {region: EU, guideline: "ESGE 2026 推奨7"}
    differential: ["ソフト凝固を用いた止血鉗子の単独療法も選択肢（推奨10）", "止血剤（パウダー等）の単独での一次使用は提案しない（推奨11）"]\[32\]
  provenance: {source: "ESGE 2026（PubMed抄録 PMID 42127996）", doi: "10.1055/a-2863-8314", source_license: "未確認", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-011
  assertion:
    plain_statement_ja: "エピネフリン局注のみによる止血は不十分で、他の止血法と併用すべきである。"\[59\]
    condition: {region: global}
  provenance: {source: "ESGE 2021／ACG 2021", source_license: "未確認／© ACG", basis_tag: B}
  uncertainty: "今回取得した資料では文言を確認できていない。要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-012
  assertion:
    plain_statement_ja: "出血性潰瘍の内視鏡的止血後にPPIを投与すると、再出血、輸血量、入院期間、手術の必要性が減る。用量や投与経路による効果差は乏しいとされる。"\[7\]
    condition: {region: JP, guideline: "JSGE 2026 CQ-1（強い推奨, A）"}
  provenance: {source: "JSGE PUD GL 2026", doi: "10.1007/s00535-026-02504-3", source_license: "CC BY 4.0", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-013
  assertion:
    plain_statement_ja: "止血成功後の高リスク潰瘍では、VPZ 40 mgと高用量PPI持続静注（80 mgボーラス後8 mg/時を72時間）を比べた2つのRCTで、再出血率と死亡率に差がなかった。"\[7\]
    condition: {region: "Thailand RCT", guideline: "JSGE 2026はVPZを弱い推奨（A）"}\[7\]
    differential: ["ESGE 2026は止血後のP-CABルーチン使用について合意に至らなかった（推奨15）"]\[34\]
    common_misconception: "止血後のVPZはPPIより再出血を明確に減らす"
  provenance:
    source: "Geeratragool T et al. Gastroenterology 2024;167:778-87（JSGE 2026経由）"
    doi: "10.1007/s00535-026-02504-3（引用元）"
    source_license: "CC BY 4.0（引用元）"
    basis_tag: B
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-014
  assertion:
    plain_statement_ja: "内視鏡治療を行った高リスク潰瘍出血では、高用量PPI（1日80 mg以上）を3日間投与した後、2週間は1日2回のPPIを続けることが提案されている。"\[59\]\[61\]
    condition: {region: US, guideline: "ACG 2021"}
  provenance: {source: "ACG 2021（Emory大学の要約資料経由）", doi: "10.14309/ajg.0000000000001245", source_license: "© ACG", basis_tag: B}
  uncertainty: "原文の推奨強度は要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-015
  assertion:
    plain_statement_ja: "ESGE 2026は、再出血例にはOTSクリップでの再止血を考慮し、それも不成功なら経カテーテル動脈塞栓術（TAE）、TAEができない・不成功なら手術という順序を推奨している。"\[59\]
    condition: {region: EU, guideline: "推奨16"}\[34\]
    common_misconception: "再出血したらすぐに外科手術"
  provenance: {source: "ESGE 2026", doi: "10.1055/a-2863-8314", source_license: "未確認", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-016
  assertion:
    plain_statement_ja: "心血管疾患の二次予防として低用量アスピリンを服用中の患者が消化性潰瘍出血を起こした場合、再出血リスクが低ければ、内視鏡直後からアスピリンを再開することが推奨される。"\[58\]\[62\]
    condition: {region: EU, guideline: "ESGE 2015（2021/2026で表現は要確認）"}
    differential: ["一次予防目的のアスピリンは中止を検討"]
    common_misconception: "潰瘍出血後は抗血小板薬を数週間中止するのが安全"
  provenance: {source: "ESGE 2015", doi: "10.1055/s-0034-1393172", source_license: "未確認", basis_tag: B}
  uncertainty: "最新版での再開時期（即時／3日以内等）は要確認"
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-017
  assertion:
    plain_statement_ja: "抗凝固療法の継続が必要な患者では、血栓塞栓リスクに応じて、臨床的に可能になった時点でできるだけ早く抗凝固薬を再開することが推奨される。"\[10\]
    condition: {region: EU, guideline: "ESGE 2026 推奨17"}\[34\]
    differential: ["ワルファリン服用中の重篤出血ではFFPよりPCCが優先されるとの記載あり（二次文献、要確認）"]\[9\]\[59\]
  provenance: {source: "ESGE 2026", doi: "10.1055/a-2863-8314", source_license: "未確認", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: UG-018
  assertion:
    plain_statement_ja: "持続的な止血が得られた消化性潰瘍出血では、止血後24時間以内に経口摂取を始め、鉄欠乏や貧血があれば退院前に鉄補充を開始することが提案されている。"
    condition: {region: EU, guideline: "ESGE 2026 推奨18・19"}\[63\]
  provenance: {source: "ESGE 2026", doi: "10.1055/a-2863-8314", source_license: "未確認", basis_tag: B}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}
```

**追加候補（一次ソース未取得のため事実票化を保留、要確認）：** トラネキサム酸の大規模RCT（HALT-IT, Lancet 2020）と、GBS高値例での6時間以内の緊急内視鏡と24時間以内の早期内視鏡の比較RCT（Lau, NEJM 2020）。どちらもPMID/DOIとライセンスを確認したうえで追加してください。

---

## 4. MCQ出題設計図（30問）

### 4-A. マトリクス（学習目標 × 認知レベル × 事実票ID）

| 学習目標（コアカリ） | 想起 | 解釈 | 問題解決 | 小計 | 主な事実票 |
|---|---|---|---|---|---|
| PS-02-08-05-2 H. pylori診断 | 1 | 2 | 1 | 4 | HP-011, 012, 013, 014 |
| PS-02-08-05-2 除菌療法・耐性 | 1 | 2 | 3 | 6 | HP-001〜010 |
| PS-02-08-05-2 胃炎・潰瘍の疫学と病態 | 1 | 1 | 1 | 3 | HP-015, 017, 018, 019 |
| PS-03-04-14／（要確認）胃癌予防・MALT | 1 | 1 | 1 | 3 | HP-016, 020 |
| 表2-7 吐血・下血：リスク層別化 | 1 | 2 | 1 | 4 | UG-001, 002 |
| （要確認）輸血 | 0 | 1 | 1 | 2 | UG-003〜005 |
| 表2-7 内視鏡治療：タイミング・止血法 | 1 | 2 | 2 | 5 | UG-006〜011, 015 |
| PS-02-08-05-4 酸分泌抑制・抗血栓薬 | 0 | 1 | 2 | 3 | UG-012〜014, 016〜018 |
| **合計** | **6（20%）** | **12（40%）** | **12（40%）** | **30** | |

配分の考え方：国試は臨床実地問題の比重が大きいため、解釈と問題解決に80%を割り当てました。日本と欧米で推奨が異なる論点（HP-004/008、UG-013）は、問題解決レベルで「日本の診療環境で」と条件を明示して出題します。

### 4-B. 誤答選択肢の生成元フィールドの例

| 事実票 | 鑑別（differential）→ 誤答の種 | よくある誤解（common_misconception）→ 誤答の種 |
|---|---|---|
| HP-011 | 便中抗原・胃液の核酸増幅検査はPPIの影響を受けにくい | 「PPI内服中の尿素呼気試験陰性で除菌成功と判定」 |
| HP-006 | 耐性株にCAMを使い続けるのは誤り | 「CAM耐性でもVPZなら同じCAMレジメンで十分」 |
| UG-001 | Rockall（完全版）は内視鏡所見が必要 | 「GBS 0でも緊急内視鏡」 |
| UG-009 | IIbへの対応は学会間で異なる | 「IIcにクリップ」 |
| UG-013 | ESGEは合意に至らず | 「VPZはPPIより再出血を明確に減らす」 |

### 4-C. サンプルMCQ（事実票から独立に作成した架空症例）

**Q1（問題解決／HP-001, 005, 006）**
52歳の男性。健診の内視鏡で、萎縮性胃炎とびまん性発赤を指摘された。迅速ウレアーゼ試験は陽性で、同時に採取した胃液の遺伝子検査で23S rRNAの点変異（クラリスロマイシン耐性）が検出された。薬剤アレルギーはない。日本のガイドラインに沿った一次除菌として最も適切なのはどれか。
a. ボノプラザン＋アモキシシリン＋クラリスロマイシン 7日間
b. ボノプラザン＋アモキシシリン＋メトロニダゾール 7日間
c. ランソプラゾール＋アモキシシリン＋クラリスロマイシン 7日間
d. 経過観察し、1年後に再検査
e. PPI単剤 8週間
**正答：b**（HP-006）。a：耐性株にCAMを用いる誤解（HP-003）。c：PPIかつCAM含有。d：全感染者が除菌適応（HP-015）。e：除菌にならない。

**Q2（解釈／HP-011）**
45歳の女性。逆流症状のためエソメプラゾールを3か月内服中である。外来で受けた尿素呼気試験は陰性だった。この結果の解釈として正しいのはどれか。
a. 感染は否定できる
b. 偽陰性の可能性があり、判定には不十分である
c. 偽陽性の可能性が高い
d. 血清抗体価の低下も同時に起きている
e. 除菌成功を意味する
**正答：b**（HP-011）。

**Q3（問題解決／UG-001, 002）**
24歳の男性。前夜の飲酒後に少量の黒色便が1回あり、受診した。意識清明、脈拍76/分、血圧124/78 mmHg。Hb 15.1 g/dL、BUN 14 mg/dLで、既往歴と内服薬はない。Glasgow-Blatchfordスコアは0点だった。対応として最も適切なのはどれか。
a. 緊急輸血
b. 2時間以内の緊急内視鏡
c. 外来での経過観察と後日の内視鏡予約
d. 腹部血管造影
e. 入院のうえPPI持続静注
**正答：c**（UG-001）。b：GBS 0でも緊急内視鏡とする誤解。e：超低リスクでの過剰な入院。
*注：GBSの点数配分（BUN・Hb・収縮期血圧・脈拍・黒色便・失神・肝疾患・心不全）を設問の根拠に使う場合は、原著（Blatchford 2000, Lancet）のライセンスとスコア表の扱いを確認してください（要確認）。*

**Q4（解釈／UG-009）**
68歳の男性。吐血で入院し、蘇生後10時間で上部内視鏡を行った。胃角部に潰瘍があり、潰瘍底には平坦な黒色の色素斑のみを認め、露出血管や凝血塊はない。この所見に対する方針として最も適切なのはどれか。
a. クリップ止血
b. 純エタノール局注
c. 内視鏡的止血は行わず、酸分泌抑制薬で治療する
d. TAE
e. 緊急手術
**正答：c**（UG-009：Forrest IIc）。

---

## 5. 留意点

### 5-A. 使えない、または要許諾の資料と代替手段

| 資料 | 理由 | 代替 |
|---|---|---|
| JGES出血ガイドライン第2版（英語・日本語） | Wiley標準条件で、CCではない\[3\] | 推奨の根拠になったRCTを一次ソースにする。推奨の存在はタグBで最小限の言及にとどめる。転載・構造化には学会・出版社の許諾（G）が必要 |
| JSGE・JSHRの日本語版書籍（南江堂・先端医学社） | 商用出版物 | CC BY 4.0の英語版（J1、J2）を抽出元にする |
| ACG（H. pylori 2024、UGIB 2021） | © ACG | 事実（閾値・方向性）のみBで扱う。CC BYの解説論文（JCAG）を補助に使う |
| Maastricht VI、Kyoto | NC | 無償の教育用途に限定。有償化する場合は事実のみB |
| Okimotoサーベイランス | ND・NC\[4\] | 数値のみB。表の再構成はしない |
| がん情報サービス | 改変不可、原意と異なる生成AI出力は不可\[41\] | AIに入力せず、統計の数値だけを出典明記で使う |
| ESGE 2021/2026 | ライセンス未確認 | Thiemeの記事ページで確認するまで、事実のみ扱う |

### 5-B. パイロットの評価指標

| 指標 | 定義 | 合格基準（提案） |
|---|---|---|
| 類似性監査の合格率 | 各事実票・MCQについて、原典との最長一致n-gram（文字13-gram等）と埋め込み類似度を、出典PDF・既存国試PDF（厚労省公開分）・手元の問題集（人間が照合）と比較する | 事実票は最長一致15文字未満が100%、MCQは既存問題との類似度閾値（例：cos 0.85）超過が0件 |
| 専門医検証での誤り率 | 消化器専門医2名が独立に検証し、事実誤り（重大／軽微）を判定。不一致は第3者が裁定 | 重大な誤りは2%未満、「要確認」項目の解消率は90%以上 |
| 出典整合率 | 数値が出典の該当箇所と一致するか | 100%（不一致は差し戻し） |
| 項目分析 | 医学部4〜6年生（例：n≥60）で試行し、難易度p値、識別指数（上位27%−下位27%）、点双列相関、誤答選択肢の選択率を算出 | p 0.3〜0.8、点双列相関≥0.2、選択率5%未満の誤答は改訂 |
| 信頼性 | 30問全体のKR-20 | ≥0.7（30問なので目安） |

**次のアクション（優先順）：**
1. 出題基準の項目番号を索引PDFから転記する。
2. ESGE 2021/2026、JSGE 2020、Murakami 2016、Barkun 2019のライセンスをThieme・Springer・PMCの記事ページで確認する。
3. 事実票のうち「要確認」付きの9件（HP-002, 003, 008, 012, 016, 017, 020, UG-004, 011）を優先して専門医検証にかける。
4. 胃MALTリンパ腫について、オープンアクセスのメタ解析を一次ソースとして追加する。

---

## Caveats

- 2026年版の資料（JSGE 2026、ESGE 2026、JSHR英語版2026）は公開から日が浅く、訂正が出る可能性があります。ESGE 2026にはすでに訂正（10.1055/a-2881-7411）があります。\[31\]
- コアカリのindexは二次情報（大学シラバス）で確認したもので、GitHub CSVのid文字列は未照合です。
- Murakami 2016のCAM耐性株の除菌率（82.0% vs 40.0%）は原著本文（PMC5036253）で、Villanueva RCTの輸血率（49% vs 86%）はPMID 23281973とWiki Journal Clubの要約で確認しました。ACG 2024のPPI中止期間は二次文献経由です。いずれも、ライセンスと原著での確認が済むまでは、事実票を`status: draft`のままにしてください。
- 「オープンアクセス」と表示されていてもCCの種別は様々です。本表で「未確認」とした資料は、確認が済むまでAIへの入力に使わないでください。

## 出典

1. <https://api.crossref.org/works/10.1007/s00535-026-02504-3>
2. <https://api.crossref.org/works/10.1007/s00535-026-02379-4>
3. <https://api.crossref.org/works/10.1111/den.15019>
4. <https://api.crossref.org/works/10.1111/hel.13028>
5. [Antimicrobial‐resistant Helicobacter pylori in Japan: Report of nationwide surveillance for 2018–2020 - Okimoto - 2024 - Helicobacter - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1111/hel.13028)
6. [Guidelines for the management of Helicobacter pylori infection in Japan: 2024 revised edition - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13283202/)
7. [Evidence-based clinical practice guidelines for peptic ulcer disease 2026 - Journal of Gastroenterology](https://link.springer.com/article/10.1007/s00535-026-02504-3)
8. [Upper Gastrointestinal and Ulcer Bleeding Guideline](https://www.mdcalc.com/guidelines/10362/acg/upper-gastrointestinal-ulcer-bleeding)
9. [Non-Variceal Upper Gastrointestinal Bleeding: A Retrospective Cohort of 364 Cases, Historical Comparison, and Updated Management Algorithm](https://www.mdpi.com/2075-1729/15/8/1320)
10. [\[PDF\] Endoscopic diagnosis and management of nonvariceal upper gastrointestinal hemorrhage (NVUGIH): European Society of Gastrointestinal Endoscopy (ESGE) Guideline](https://www.semanticscholar.org/paper/Endoscopic-diagnosis-and-management-of-nonvariceal-Gralnek-Stanley/2b37c8a98652b8e0d3347928f98996415beb429f)
11. [GitHub - core-curriculum/data: 医学教育モデル・コア・カリキュラム（令和4年度改訂版）の電子データ](https://github.com/core-curriculum/data)
12. [臨床病理学2｜eYUME](https://eyume.med.yamaguchi-u.ac.jp/2025/curriculums/detailUnit/j040549)
13. [Guidelines for the management of Helicobacter pylori infection in Japan: 2024 revised edition](https://link.springer.com/article/10.1007/s00535-026-02379-4)
14. [Evidence-based clinical practice guidelines for peptic ulcer disease 2020 - Tohoku University](https://tohoku.elsevierpure.com/en/publications/evidence-based-clinical-practice-guidelines-for-peptic-ulcer-dise/)
15. [JGES Guidelines](https://www.jges.net/english/publication/guideline)
16. [Vonoprazan-based triple therapy is effective for Helicobacter pylori eradication irrespective of clarithromycin susceptibility](https://link.springer.com/article/10.1007/s00535-020-01723-6)
17. [Management of Helicobacter pylori infection: the Maastricht VI/Florence consensus report - PubMed](https://pubmed.ncbi.nlm.nih.gov/35944925/)
18. [Kyoto global consensus report on Helicobacter pylori gastritis - Keio University](https://keio.elsevierpure.com/en/publications/kyoto-global-consensus-report-on-helicobacter-pylori-gastritis/)
19. [Optimization of Vonoprazan-based Dual Therapy for Helicobacter Pylori](https://clinicaltrials.gov/study/NCT05649540)
20. [Kyoto global consensus report on Helicobacter pylori gastritis](https://www.cureus.com/pmc_articles/462139)
21. [2024 American College Gastroenterology H. pylori Guidelines](https://www.pharmacy.umn.edu/2024-american-college-gastroenterology-h-pylori-guidelines)
22. [ACG Clinical Guideline: Treatment of Helicobacter pylori Infection](https://www.ovid.com/jnls/ajg/abstract/10.14309/ajg.0000000000002968~acg-clinical-guideline-treatment-of-helicobacter-pylori?redirectionsource=fulltextview)
23. [Do the new ACG Helicobacter pylori treatment guidelines have implications for Canada?](https://academic.oup.com/jcag/article/8/3/85/8125707)
24. [The Effect of Using Preendoscopic Proton Pump Inhibitors in Upper Gastrointestinal System Bleeding on Patient Prognosis](https://clinicaltrials.gov/study/NCT05467358)
25. [ACG Upper Gastrointestinal and Ulcer Bleeding Guideline Summary - Guideline Central](https://www.guidelinecentral.com/guideline/325721/)
26. [ACG Clinical Guideline: Upper Gastrointestinal and Ulcer ...](https://www.darmzentrum-bern.ch/fileadmin/darmzentrum/Education/Bible_Class/2022/upper_GI_bleeding/ACG_-_Upper_GI_Bleed_2021.pdf)
27. [Endoscopic diagnosis and management of nonvariceal upper gastrointestinal hemorrhage (NVUGIH): European Society of Gastrointestinal Endoscopy (ESGE) Guideline - Update 2021 - University of Southern Denmark](https://portal.findresearcher.sdu.dk/en/publications/endoscopic-diagnosis-and-management-of-nonvariceal-upper-gastroin/)
28. [Early Esophagogastroduodenoscopy Performed Bedside Using Single-use Disposable Endoscope](https://clinicaltrials.gov/study/NCT07033286)
29. [Hemostatic powder’s battle against a spurting bleeding ulcer: can it win?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12202128/)
30. [(PDF) Diagnosis and management of nonvariceal upper gastrointestinal hemorrhage: European Society of Gastrointestinal Endoscopy (ESGE) Guideline](https://www.researchgate.net/publication/282779044_Diagnosis_and_management_of_nonvariceal_upper_gastrointestinal_hemorrhage_European_Society_of_Gastrointestinal_Endoscopy_ESGE_Guideline)
31. [Thieme E-Journals - Endoscopy / Abstract](https://www.thieme-connect.de/products/ejournals/abstract/10.1055/a-2863-8314)
32. [Endoscopic diagnosis and management of peptic ulcer bleeding: European Society of Gastrointestinal Endoscopy (ESGE) Guideline - Update 2026 - PubMed](https://pubmed.ncbi.nlm.nih.gov/42127996/)
33. [Endoscopic diagnosis and management of nonvariceal upper gastrointestinal hemorrhage (NVUGIH): European Society of Gastrointestinal Endoscopy (ESGE) Guideline](https://www.researchgate.net/publication/349205389_Endoscopic_diagnosis_and_management_of_nonvariceal_upper_gastrointestinal_hemorrhage_NVUGIH_European_Society_of_Gastrointestinal_Endoscopy_ESGE_Guideline_-_Update_2021)
34. [Endoscopic diagnosis and management of peptic ulcer bleeding: European Society of Gastrointestinal Endoscopy (ESGE) Guideline - Update 2026.](https://www.lifescience.net/publications/2017800/endoscopic-diagnosis-and-management-of-peptic-ulce/)
35. [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7233308)
36. [医学教育モデル・コア・カリキュラム関連：文部科学省](https://www.mext.go.jp/a_menu/koutou/iryou/mext_00005.html)
37. [医学教育モデル・コア・カリキュラム（令和4年度改訂版）を踏まえた「ICT活用教育」の必要性と課題](https://www.jstage.jst.go.jp/article/jjphe/8/0/8_2024-029/_html/-char/ja)
38. [ホーム\> 政策について\> 審議会・研究会等\> 医道審議会(医師分科会医師国家試験出題基準改定部会)\> 令和6年版医師国家試験出題基準について](https://www.mhlw.go.jp/stf/shingi2/0000128981_00001.html)
39. [厚生労働科学研究費補助金（政策科学総合研究事業（臨床研究等ICT 基盤構築･人工知能実装研究事業））](https://mhlw-grants.niph.go.jp/system/files/report_pdf/03-1.%E7%A0%94%E7%A9%B63%E3%80%90%E3%83%8F%E3%82%9A%E3%83%BC%E3%83%88%EF%BC%91%E3%80%91_%E5%A0%B1%E5%91%8A%E6%9B%B8ver.1.1_0.pdf)
40. [一般財団法人厚生労働統計協会｜国民衛生の動向、厚生労働統計情報を提供 - 医師国家試験に出る国民衛生の動向](https://www.hws-kyokai.or.jp/publishing/eisei-ishishiken-main.html)
41. [著作権について：\[国立がん研究センター がん情報サービス 一般の方へ\]](https://ganjoho.jp/aboutus/attention/copyright.html)
42. [表2-7. 消化器系 | モデルコアカリキュラム](https://core-curriculum.jp/tables/TBL0207)
43. [Impact of Vonoprazan Triple-Drug Blister Packs on H. pylori Eradication Rates in Japan: Interrupted Time Series Analysis](https://link.springer.com/article/10.1007/s12325-021-01784-w)
44. [Second-line triple therapy in failures with vonoprazan-based triple therapy for eradication of Helicobacter pylori - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6036823)
45. [Review](https://www.microbiotajournal.com/wp-content/uploads/sites/7/2023/10/e917.pdf)
46. [ACG Recommends Bismuth Quadruple Therapy for H. Pylori Treatment](https://www.physiciansweekly.com/post/management-of-h-pylori-infection-through-acgs-latest-guidelines)
47. [ACG Clinical Guideline: Treatment of Helicobacter Pylori ...](https://med.emory.edu/departments/medicine/_documents/hein-acg-h-pylori-infection-guideline.pdf)
48. [ACG GUIDELINE Highlights](https://gi.org/wp-content/uploads/2025/01/ACG-Hpylori-Guidelines-Highlights-2024-FINAL.pdf.pdf)
49. [(PDF) The Updated JSPGHAN Guidelines for the Management of Helicobacter pylori Infection in Childhood](https://www.researchgate.net/publication/342897701_The_Updated_JSPGHAN_Guidelines_for_the_Management_of_Helicobacter_pylori_Infection_in_Childhood)
50. [Helicobacter pylori陽性胃MALTリンパ腫の除菌治療後に異時性のt（11；18）（q21；q21）転座陽性MALTリンパ腫を認めた１例](https://www.jstage.jst.go.jp/article/gee/63/7/63_1351/_html/-char/ja)
51. [医師国家試験 - 過去問チャート](https://medical-illustration.club/kakomon-chart/med/110_a/19)
52. [ACG Clinical Guideline: Upper Gastrointestinal and Ulcer Bleeding](https://www.researchgate.net/publication/351256020_ACG_Clinical_Guideline_Upper_Gastrointestinal_and_Ulcer_Bleeding)
53. [ACG Clinical Guideline: Upper Gastrointestinal and Ulcer Bleeding - PubMed](https://pubmed.ncbi.nlm.nih.gov/33929377/?ff=20210501114250&v=2.14.4)
54. [ACG Clinical Guideline: Upper Gastrointestinal and Ulcer... : Official journal of the American College of Gastroenterology](https://journals.lww.com/ajg/fulltext/2021/05000/acg_clinical_guideline__upper_gastrointestinal_and.14.aspx)
55. [ACG Clinical Guideline: Upper Gastrointestinal and Ulcer Bleeding](https://journals.lww.com/ajg/fulltext/10.14309/ajg.0000000000001245~acg-clinical-guideline-upper-gastrointestinal-and-ulcer)
56. [Guidelines for endoscopic management of nonvariceal upper gastrointestinal bleeding (second edition) - Fujishiro - 2025 - Digestive Endoscopy - Wiley Online Library](https://onlinelibrary.wiley.com/doi/10.1111/den.15019)
57. [update on the management of non-variceal upper gastrointestinal bleeding](https://academic.oup.com/gastro/article/doi/10.1093/gastro/goad011/7081277)
58. [Thieme E-Journals - Endoscopy / Abstract](https://thieme-connect.com/products/all/doi/10.1055/s-0034-1393172)
59. [Endoscopic management of upper non-variceal and lower gastrointestinal bleeding: Where do we stand?](https://www.wjgnet.com/1948-5190/full/v17/i5/105580.htm)
60. [Management of Non-Variceal Upper Gastrointestinal Bleeding - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12997055/)
61. [ACG Clinical Guideline: Upper Gastrointestinal and Ulcer Bleeding](https://med.emory.edu/departments/medicine/_documents/obineme-acg-clinical-guideline--ugib.pdf)
62. <https://link.springer.com/article/10.1007/s00535-021-01769-0>
63. [Endoscopic diagnosis and management of peptic ulcer bleeding: European Society of Gastrointestinal Endoscopy (ESGE) Guideline - Update 2026.](https://read.qxmd.com/read/42127996/endoscopic-diagnosis-and-management-of-peptic-ulcer-bleeding-european-society-of-gastrointestinal-endoscopy-esge-guideline-update-2026?gs=0&token=k3%2FXnPe6snt5K%2Fk8sYs%2BCjm%2BK0W2VrJ%2B6YXlCH4qZRz4vpE6usfZ7RjUQa5kryaIE9vAO%2FmuN431tHMIN6ClKnp3q%2FXxUBEszGA%2BXr3IBXDGkov%2F4%2FdYolcXckSM8AHrNdDcdmI6HsEsUajiHsVPbAnTJlI7bEk0Tz6GNxRxRIaqTTx0bvFVRnyNa3yVL3E9IiNHmpJX4sSbm6kb88F0v5PSw4sCr0lcUsVpAdloooezIiePWyNUxrZ%2B69DrM56esjYAtC8Qf3Xv1xzsC421K%2FuLQSAu%2Fv%2FInpeXrZWahU9fq6JDuVPOOTNfD4PGbnZXRJjFhBoZ6BW%2FhwGN22jCbIISXxgE9D2ytTd4PKSIigZ94uF6IwLYzZ7yizJ%2BWRvANa3%2BzsmwaApP74byHNeD4yExCENzmCqN6KrZbJ9jv%2FHZsFrSFXOZv39O1VDTi3%2B2)
