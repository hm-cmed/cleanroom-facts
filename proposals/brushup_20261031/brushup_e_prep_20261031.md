# 提案E（メタデータ整備）の下準備（2026-10-31）

出典マスター（2,265件、第58〜60回取り込み後）と全カード（3,644件）から、整備対象を機械的に切り分けた。データファイルは末尾に挙げる。

## 1. PMID 補完：大半はカード側から回収できる

- DOI があり PMID がマスターにない出典（カードで使用されているもの）：477件
- うち、**カード側の provenance に PMID が既にあるもの：369件**（brushup_e_pmid_harvest.json に SRC→PMID の対応）。SRC-231 で提案した補完と同じ形で、照合なしにマスターへ転記できる分がこれだけある（値はカード作成時に PubMed で確認済みのもの）
- 残り116件は PubMed での照合が必要（brushup_e_pmid_lookup.json に SRC と使用カード）

## 2. UNKNOWN ライセンス：616件

- DOI あり516件／なし100件。DOI の出版者別の内訳は Elsevier（10.1016）113件が最大で、NEJM 35件、Wolters Kluwer 34件、Springer 34件、Wiley 61件（10.1111＋10.1002）、BMJ 23件など
- Crossref のライセンスメタデータによる事前確認を別途実施中（brushup_e_license_precheck.md）。確定はレポジトリ側の照合に委ねる

## 3. kokushi が null のカード：550件（再仕分け済み）

- 接頭辞別では NG（総論）221件が突出し、AB 52件、XS 37件、KX 32件、RX 22件、CX 21件と続く
- 全件の主張文を読んで再仕分けした結果（詳細は brushup_e_null_ng_result.md と brushup_e_null_other_result.md）：
  - **各論に番号付記できるもの：167件**（NG 71件＋NG以外 96件）。うち主張の射程が項目とそのまま合うものが約118件、射程が一部に限られ付記だけでは不十分なものが49件
  - **総論として null が正しいもの：383件**（検査・手技の総論、症候アプローチ、統計・制度、出題基準に項目自体がない疾患など）
- NG の付記先は4項目に集中する：Ⅵ-3-A-② 過敏性腸症候群に40件、Ⅵ-3-A-① 便秘症に23件、Ⅹ-10-B-① アセトン血性嘔吐症に5件、Ⅸ-6-C-① 片頭痛に4件（腹部片頭痛で要判断）
- NG 以外では UG-001〜018（消化性潰瘍）、XS-009〜015（鉄欠乏性貧血）、EX の内分泌緊急症などがまとまった付記候補

## 4. region がないカード：505件

- brushup_e_region_missing.json にカード ID の一覧。初期の回の移行形式（condition が文字列）の40件を含む。地域の判定はカードの内容（国内／海外の基準か）を読む必要があり、一括では埋められない

## データファイル

- brushup_e_unknown_sources.json（UNKNOWN 616件の書誌・DOI 等）
- brushup_e_pmid_targets.json（DOI あり・PMID なし出典477件と使用カード）
- brushup_e_pmid_harvest.json（カード側から回収できる PMID 369件）
- brushup_e_pmid_lookup.json（PubMed 照合が要る116件）
- brushup_e_region_missing.json（region 欠落505件の ID）
