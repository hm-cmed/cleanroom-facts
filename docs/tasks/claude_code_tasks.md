# Claude Code 作業指示書

前提：`CLAUDE.md` のルールを常に優先する。各フェーズの終わりにレポートを出してコミットし、人間の確認を受けてから次へ進む。

---

## Phase 0：環境構築

### 0-1. リポジトリとPython環境（PowerShell）

```powershell
cd cleanroom-gi-facts
git init
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pyyaml jsonschema requests python-dotenv pandas openpyxl pdfplumber rapidfuzz
pip freeze > requirements.txt
```

### 0-2. `.gitignore` と `.env`

`.gitignore` に次を書く。

```
.venv/
.cache/
.env
__pycache__/
```

`.env` を作成する（値は人間が入れる）。

```
CONTACT_EMAIL=
NCBI_API_KEY=
```

### 0-3. 原本の配置（人間が行う）

`raw/` に次のMarkdownを保存する。中身は claude.ai の調査レポートを、そのままコピーする。

| ファイル名 | 中身 |
|---|---|
| `raw/00_pilot_hp_ug.md` | パイロット報告（HP-001〜020、UG-001〜018、ホワイトリスト、MCQ設計図） |
| `raw/01a_esophagus_v1.md` | 第1回 食道の初版（ES-001〜068） |
| `raw/01b_esophagus_v2.md` | 第1回 食道の完成版（ES-R01〜R19、ES-069〜089、SRC表） |

**完了条件**：venvが有効になり、`raw/` に3ファイルがあり、初回コミットが済んでいる。

---

## Phase 1：取り込み（`scripts/extract_yaml.py`）

1. `raw/*.md` から ` ```yaml ` ブロックをすべて抽出する。
2. PyYAMLで読み込む。マージキー `<<:` とアンカーは展開する。先頭が `_` のキー（`_pub`、`_cur`、`_src`）は定義用なので、カードとしては扱わない。
3. 各カードをスキーマの形に正規化する。
   - `domain` は ID の接頭辞から付ける。
   - 旧 `basis_tag` は、`CLAUDE.md` 2-3 の変換規則で `legal_basis` と `source_class` に分ける。どちらの規則を使うかは、取り込み元のファイルで決める。
   - 古い `publication_info.created` は保持する。
   - `history` に「取り込み：raw/xxx.md から」を記録する。
4. `raw/01b` の SRC表は `data/sources/sources.yaml` に変換し、対応する SRC番号を各カードの `source_ref` に入れる。
5. 出力先：
   - パイロット分は `data/facts/HP.yaml` と `data/facts/UG.yaml`
   - 食道は、統合が終わるまで `data/facts/_staging_ES_v1.yaml` と `data/facts/_staging_ES_v2.yaml` に分けて置く
6. `reports/01_ingest.md` を出す。中身は件数、変換できなかった項目、スキーマ違反の一覧。

**完了条件**：HP と UG がスキーマ検証を通る。ES の2つの staging ファイルが読める。

---

## Phase 2：食道 v1 と v2 の統合（最重要。人間の承認が必要）

背景：v2 の改訂カード（ES-R01〜R19）は、v1 のどのIDを置き換えるのかが未確定のまま作られた。

1. **対応表の案を作る**（`scripts/es_merge_map.py`）
   - v1 の各カードと ES-R の各カードを比べる。比べる観点は、DOI・PMID・出典名の一致と、主張文の類似度（rapidfuzz）。
   - 置き換え先の候補を最大3件まで挙げる。
   - `proposals/es_merge_map.csv` に出す。列は次のとおり。
     `R_id, candidate_v1_ids, match_basis, score, proposed_action(replace/new/split), note`
   - 1つのRカードが複数のv1カードにまたがる場合（例：ES-R01 と v1 の ES-049・ES-050）は、`split` として提案する。
2. **人間の承認**
   - 人間が CSV の `approved_v1_id` 列を埋める。
   - Claude Code はこの列を自分で埋めない。
3. **適用**（`scripts/es_merge_apply.py`）
   - 承認された対応に従い、v1 のIDを残したまま、本文を v2 の内容で置き換える。
   - 置き換え先のないRカードには、ES-090 以降の新しいIDを付ける。
   - ES-068 は `status: retired` とし、`superseded_by` に分割後のIDを列挙する。
   - 欠番（ES-076〜078、082〜084、088）は作らない。
   - 結果を `data/facts/ES.yaml` に書き、staging ファイルは削除する（gitの履歴に残る）。
4. `reports/02_es_merge.md` を出す。中身は置換・新規・廃止の件数と、全件の対応表。

**完了条件**：`ES.yaml` がスキーマ検証を通る。ID の重複がない。v1・v2 のどのカードも、統合後のどこに行ったかを追跡できる。

---

## Phase 3：識別子とライセンスの照合（`scripts/verify_ids.py`）

すべての `data/facts/*.yaml` を対象とする。

1. **DOI があるカード**
   - Crossref から次を取得する：タイトル、雑誌、年、巻・ページ、`license` 配列。
   - NCBI の idconv、または `esearch` の `"{DOI}"[doi]` 検索で PMID と PMCID を取得する。
2. **PMID だけあるカード**
   - `esummary` で書誌を取得し、`source` の記載（著者・雑誌・年）と照合する。
3. **どちらもないカード**
   - `source` の文字列から、Crossref の `query.bibliographic` で候補を最大3件取得する。
   - 結果は `proposals/id_candidates.csv` に出すだけにする（**自動では書き込まない**）。
4. **判定と書き込み**
   - 既存値とAPIの結果が一致したら、`id_check` を記録する。
   - 既存値が空で、DOI 経由で一意に確定したら、`pmid` と `pmcid` に書き込み、`history` に記録する。
   - 既存値とAPIの結果が**食い違う**場合は、書き換えずに `reports/03_id_conflicts.md` に記録する。
   - Crossref の license URL から `source_class` を判定する。既存値と食い違う場合はレポートに出す。判定基準は次のとおり。
     - `creativecommons.org/licenses/by/` または `publicdomain/zero` → OPEN
     - `by-nc`・`by-nd` を含むもの、出版社独自規約 → RESTRICTED
     - license 情報なし → 現在の値を維持し、notes に「Crossrefに記載なし」と書く
5. **ステータスの昇格**
   - 識別子とライセンスの照合が通ったカードは、`draft` から `verified_sources` に上げる候補になる。
   - ただし `uncertainty` に「要確認」が残るカードは上げない。
   - 昇格は、一覧を `reports/03_promotions.md` に出し、人間が承認してから行う。
6. **重点的に解決すべき既知の残課題**（食道）
   - CheckMate 577：DOI 10.1056/NEJMoa2032125
   - CheckMate 648：DOI 10.1056/NEJMoa2111380
   - García-Pagán 2010：PMID 20573925 の独立照合
   - ACG Barrett 2022：DOI 10.14309/ajg.0000000000001680
   - Lyon 2.0：DOI 10.1136/gutjnl-2023-330616
   - Oyama 2017：DOI 10.1007/s10388-016-0527-7
   - JGES 食道ESD/EMR GL：DOI 10.1111/den.13654
   - JSGE GERD GL 2021：DOI 10.1007/s00535-022-01861-z
   - ESGE 異物GL：DOI 10.1055/s-0042-100456
   - ESGE 静脈瘤GL：DOI 10.1055/a-1939-4887
   - 肝硬変GL 2020：DOI 10.1007/s00535-021-01788-x

   以上の PMID・PMCID・ライセンスを確定する。

**完了条件**：全カードに `id_check` が記録されている。食い違いと未解決の一覧がレポートにある。

---

## Phase 4：カリキュラム番号（`scripts/map_curriculum.py`）

1. **コアカリ**
   - GitHub の `core-curriculum/data`（令和4年度改訂版）の CSV を `data/curriculum/` に取得する。
   - 出典と取得日を `data/curriculum/README.md` に記録する（利用条件：文部科学省ウェブサイト利用規約）。
   - CSV の列構成を確認し、`id`（不変）と `index`（表示番号）を区別して扱う。
2. **国試出題基準**
   - 令和6年版医師国家試験出題基準の PDF（厚生労働省）を `.cache/` に取得する。
   - pdfplumber でテキストを抽出し、索引から項目番号を引けるようにする。
   - PDF 本体はリポジトリに入れない。
3. **候補の提示**
   - 各カードの主張文と `subdomain` から、キーワード照合で候補を最大3件挙げる。
   - `proposals/curriculum_map.csv` に出す。
4. **人間の承認後に書き込む**
   - 書式は `core_curriculum: "PS-02-08-05-2 (id: xxxx)"` とする。

**完了条件**：全カードに承認済みの番号、または「該当なし」が入っている。

---

## Phase 5：品質チェック（`scripts/validate.py`）

毎回の作業の最後に必ず実行する。次の項目を確認し、`reports/validate_YYYYMMDD.md` に出す。

1. JSON Schema による検証。
2. ID の重複と、欠番の一覧。
3. 整合性チェック
   - `legal_basis: E` が存在しないこと。
   - `source_class: OPEN` なのに license に NC・ND を含むものがないこと。
   - `status: verified_expert` なのに `verifier` が空のものがないこと。
4. 「要確認」を含むカードの一覧。
5. 主張文の文字数の分布。長すぎるものは分割の候補として挙げる。
6. **表現の流用チェック（任意・推奨）**
   - 照合時に取得した抄録（`.cache/` のみ。リポジトリには保存しない）と主張文を比較する。
   - 抄録の多くは英文なので、和文の主張文との比較では、数値の並びと固有名詞の一致だけを見る。
   - 和文資料を出典とするカードについては、文字 13-gram 以上の一致を警告する。

---

## Phase 6：専門医レビュー用シート（`scripts/export_review.py`）

- `review/review_<接頭辞>_YYYYMMDD.xlsx` を出す。
  - 列：ID、主張文、条件、出典（DOI・PMIDのリンク付き）、source_class、uncertainty、判定（OK／修正／削除）、修正案、コメント
- Excel で文字化けしないよう、CSV で出す場合は UTF-8 BOM 付きにする。
- 人間が記入したシートを取り込むスクリプト（`scripts/import_review.py`）も作る。
  - 判定が OK のカード：`verifier` と `verified_at` を記入し、`verified_expert` に昇格する。
  - 判定が「修正」のカード：`proposals/` に修正案として出し、本文は自動で書き換えない。

---

## 以降の回（第2〜7回）の定型手順

1. 人間が claude.ai の Project で調査を実行し、レポートを `raw/0N_<領域>.md` に保存する。
2. Phase 1 の取り込みを実行する（新しい回は最初から `legal_basis` と `source_class` の形式で書かれている想定）。
3. Phase 3、4、5 を実行する。
4. Phase 6 で、レビュー用シートを人間に渡す。
5. `docs/handover/0N_<領域>.md` を作成する。
   - 中身：件数、未解決の一覧、次の回への引き継ぎ事項。
   - 次の調査ラウンドの依頼文に貼り付ける「重複回避リスト」（既存の主要な出典と、扱い済みのトピック）を、末尾に自動生成する。
