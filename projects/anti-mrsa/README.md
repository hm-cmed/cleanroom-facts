# projects/anti-mrsa：抗MRSA薬 Web教材研究の事実票（下書き）

架空症例で抗MRSA薬の選択・投与設計を学ぶWeb教育コンテンツ（札幌医科大学、研究責任者 福土将秀）の、医学的内容の根拠を管理するフォルダです。
ガイドラインや論文から医学的事実を抽出し、原文を転載せずに独自の表現で「事実票」（evidence card）にしています。

- 事実票の根拠には、**Creative Commons等で二次利用が認められた資料**（区分A〜C）だけを使います。
- 教育に必要だが事実票がない部分は「ギャップ」として登録し、**専門家の意見**・学会への許諾・添付文書の規制情報などで補います。専門家の意見は【専門家の意見】等のラベルで表示し、ガイドラインの推奨と混同しません。
- すべての事実票は `review_status: draft` から始まり、専門家の確認を経て `approved` になったものだけを教育コンテンツに使います。
- 教育専用です。実際の患者の診療には使用しません（`clinical_use_prohibited: true`）。

## レポジトリ本体（data/facts）との関係

このフォルダは、本体の事実票（`data/facts/*.yaml`、`schema/fact.schema.json`）とは**別のスキーマで管理する下書き置き場**です。

- 本体の `scripts/validate.py` と GitHub での監修（`review/github/`、Issue フォーム、Actions）は、このフォルダを対象にしません。問題サイト（cleanroom-mcq）にも取り込まれません。
- 本体 CLAUDE.md 第1節のクリーンルーム原則は、このフォルダにもそのまま適用します（本文・PDFを入れない、主張文を Claude Code が勝手に書き換えない、推測で識別子を埋めない、確認者欄は人間だけが書く）。
- **識別子は未照合です。** `sources/registry.yaml` の DOI は検索結果・出版社ページで見ただけで、Crossref・NCBI API での照合はまだ行っていません（`identifier_verification: search_only`）。
- ライセンスの確認状況は `license_verification_status` に記録しています（verified／verified_secondary／needs_check）。

### 本体へ移すときの手順（案）

1. 本体 CLAUDE.md 第6節の手順で、DOI・PMID・PMCID・ライセンスを API で照合する。確認できないものは `null` にし、理由を記録する。
2. 本体の出典マスター（`data/sources/sources.yaml`）に SRC 番号で登録する。
3. 事実票を本体のスキーマに変換する。接頭辞は既存の IG（感染症の総論：抗菌薬）を第一候補とし、新しい接頭辞にする場合は人間が決める（本体 CLAUDE.md 第4節）。
4. ライセンス区分の対応は次のとおり（`legal_basis` はいずれも B：自作文で事実を記述）。

   | このフォルダの区分 | 本体の `source_class` |
   |---|---|
   | A（CC BY 4.0 など） | OPEN |
   | A（日本の府省・公的機関の資料） | GOV_JP |
   | B（CC BY-SA） | RESTRICTED（本体の OPEN は CC BY／CC0 に限るため） |
   | C（CC BY-NC など） | RESTRICTED |
   | D（ND など：照合用のみ） | RESTRICTED |
   | E（権利留保・許諾待ち） | RESTRICTED（ライセンス未確認なら UNKNOWN） |

5. 本体の既存カードと重複する内容は統合する。現時点で関連するのは BA（JANIS の MRSA 分離率）と IG（MRSA 菌血症による死亡の推計）のカード。

## 構成

| パス | 内容 |
|---|---|
| `sources/registry.yaml` | 出典台帳。ライセンス、確認場所、確認日、利用区分（A〜E）、識別子の照合状況 |
| `facts/*.yaml` | 事実票。コース（C1〜C5）・出典ごとのファイル |
| `gaps/expert_input_items.yaml` | 事実票でカバーできない項目と、専門家への質問案 |
| `schemas/` | 事実票・出典台帳・ギャップのスキーマ（knowledge package v1.0 を拡張。出典台帳は v1.2） |
| `scripts/validate.py` | スキーマ検証と `reports/coverage.md` の生成 |
| `scripts/build_cards.py` `scripts/card_defs.py` | 初版の事実票を作ったスクリプト（初版作成後は `facts/*.yaml` を直接編集する） |
| `reports/coverage.md` | コース別・出典別のカバレッジ（自動生成） |
| `docs/knowledge_package_v1/` | 情報源管理・表示ラベル・著作権・安全境界の規程 v1.0 |
| `docs/anti_mrsa_project_handoff.md` | 引き継ぎメモ |
| `LICENSE_POLICY.md` | 利用区分と帰属表示のルール |
| `CONTRIBUTING.md` | 専門家レビューの手順 |

## 学習コース

| ID | コース |
|---|---|
| C1 | 抗MRSA薬の開始判断・薬剤選択 |
| C2 | VCMの初期投与・TDM設計 |
| C3 | 薬剤選択と投与設計の統合 |
| C4 | 専門医の選択哲学 |
| C5 | 再評価・デエスカレーション |

## 現状（2026-11-08 初版）

出典24件（うち事実票の根拠にできる区分A〜C：14件）、事実票73件、ギャップ19件。すべて下書き（draft）です。詳細は `reports/coverage.md`。

主な根拠資料（CC BY）：日本化学療法学会・日本TDM学会のVCM TDMガイドライン英語版（Matsumoto 2022）、そのメタ解析（Tsutsuura 2021）、日本版敗血症診療ガイドライン2024英語版（J Intensive Care版）、英国MRSA治療ガイドライン2021。
非営利限定（CC BY-NC）：TEIC TDMガイドライン英語版（Hanai 2022）、WHO AWaRe。

## 使い方（PowerShell）

```powershell
cd projects/anti-mrsa
pip install pyyaml jsonschema
python scripts/validate.py            # 検証
python scripts/validate.py --report   # 検証＋カバレッジ報告の更新
```

## 注意

- このフォルダ独自の文書（スキーマ・規程・スクリプト）のライセンスは【要確認】（案：CC BY 4.0）。事実票は各出典のライセンス条件（`LICENSE_POLICY.md`）に従います。
- 非営利限定（区分C）の出典に由来する事実票を含むため、教育コンテンツを商用提供する場合は区分Cの事実票を除外してビルドしてください。
- 専門家の意見を、研究として体系的に収集・分析・公表する場合（専門医アンケート等）は、別途倫理審査が必要です。
