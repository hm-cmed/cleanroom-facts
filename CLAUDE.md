# CLAUDE.md — 消化器 事実票リポジトリ（Clean Room Fact DB）

このリポジトリは、医学教育コンテンツと評価問題を「クリーンルーム方式」で作るための中間成果物、つまり事実票（fact card）を管理する。
事実票は、著作権で保護される表現を含まない「検証可能な命題・数値」と、その出典の記録である。
Claude Code はこのリポジトリで、取り込み・照合・検証・レビュー用シートの出力を担当する。
医学的内容の最終判断は、人間（専門医）が行う。

作業環境は Windows（PowerShell）・Python 3.11 以上。コマンド例は PowerShell 構文で書くこと。

---

## 1. 絶対に守るルール（クリーンルーム原則）

1. **著作物の本文をリポジトリに入れない。**
   - 論文やガイドラインの全文・PDF・図表をダウンロードして保存しない。
   - 保存してよいのは書誌メタデータ（タイトル、雑誌、年、DOI、PMID、PMCID、ライセンスURL）だけ。
   - 照合のために一時的に取得したAPI応答は `.cache/` に置く（git管理外）。
2. **主張文（`assertion.plain_statement_ja`）と数値を、Claude Code が自分の判断で書き換えない。**
   - 修正が必要と判断したら、`proposals/` に提案ファイルを出し、人間の承認を待つ。
   - 例外は、表記ゆれ（全角・半角、空白）の機械的な正規化だけ。正規化した場合も履歴に記録する。
3. **推測で識別子を埋めない。**
   - PMID・DOI・PMCID・ライセンスは、APIの応答で確認できたものだけを書く。
   - 確認できなければ `null` にし、`uncertainty` に理由を書く。
   - 記憶にもとづく「〜の可能性」は禁止。
4. **`verifier` と `status: verified_expert` は人間だけが設定する。** Claude Code はこの2項目に値を入れない。
5. **IDは不変。**
   - 一度付けたIDは再利用しない。
   - 廃止・統合したカードは削除せず、`status: retired` と `superseded_by` を記録する。
6. **原典の文言をコピーした疑いがある場合は、作業を止めて報告する。**
   - 疑いとは、主張文と抄録などの間に長い一致文字列がある場合を指す。

---

## 2. 2つのタグ（混同しないこと）

これまで `basis_tag` という1つの欄に2つの意味が混在していた。今後は次の2欄に分ける。

### 2-1. `legal_basis`：主張文そのものの利用根拠（SOPの利用根拠A〜G）

| 値 | 意味 | 事実票での典型 |
|---|---|---|
| A | 完全な自作 | 自作の教育的整理（事実でない部分） |
| B | 非保護の事実・データ・アイデア | **ほぼ全件がこれ**（自作文で事実を記述） |
| C | 保護対象外・保護期間満了 | 法令・告示の内容など |
| D | 引用（著作権法32条） | 原則使わない |
| E | 教育例外（35条） | **事実票では使わない**（一般公開できないため） |
| F | オープンライセンス（CC等） | CC資料の表現を条件に従って翻案した場合のみ |
| G | 個別許諾・契約 | 許諾を得た場合のみ |

### 2-2. `source_class`：出典資料のライセンス区分

| 値 | 意味 | 扱い |
|---|---|---|
| OPEN | CC BY / CC0（商用・改変可） | 優先して使う |
| RESTRICTED | CC BY-NC / ND、出版社規約、©学会など | 数値と方向性だけを自作文で使う。表現・表・図は使わない |
| GOV_JP | 日本の府省・公的機関資料（政府標準利用規約・公共データ利用規約） | 出典を明記し、加工した旨を示す |
| GOV_US | 米国連邦政府著作物 | 第三者素材を除き自由 |
| UNKNOWN | ライセンスを確認できていない | RESTRICTED と同じ扱い。確認を優先課題にする |

### 2-3. 旧データの変換規則（取り込み時に適用）

- **パイロット版（HP-001〜020、UG-001〜018）**：`basis_tag` はSOPの意味で書かれている。
  - そのまま `legal_basis` に移す。
  - `source_class` は `source_license` の記載から判定する。
- **第1回 食道（ES-*）**：`basis_tag` はライセンスの意味で書かれている。次のように変換する。

  | 旧 `basis_tag` | `legal_basis` | `source_class` |
  |---|---|---|
  | A | B | OPEN |
  | B | B | RESTRICTED |
  | C | B | GOV_JP |
  | D | B | GOV_US |
  | E | B | UNKNOWN |
  | 保留 | B | UNKNOWN（`status: draft`） |

- 変換したことを `history` に記録する。

---

## 3. ステータス

| 値 | 意味 | 誰が設定するか |
|---|---|---|
| draft | 出典・数値の照合が未完了 | Claude Code / 人間 |
| verified_sources | 識別子とライセンスをAPIで照合済み。数値が出典の記載と一致することも確認済み | Claude Code（照合結果にもとづく） |
| verified_expert | 専門医が内容を確認済み | **人間のみ** |
| retired | 廃止・統合済み（`superseded_by` 必須） | 人間の承認後 |

`verified_sources` は「出典が実在し、書誌が合っている」という意味にとどまる。医学的に正しいことの保証ではない。

---

## 4. IDの規則

| 接頭辞 | 範囲 | 回 |
|---|---|---|
| HP | H. pylori関連疾患 | パイロット |
| UG | 上部消化管出血 | パイロット |
| ES | 食道 | 第1回 |
| GD | 胃・十二指腸（HP・UG以外） | 第2回 |
| IN | 小腸・大腸 | 第3回 |
| LV | 肝 | 第4回 |
| BP | 胆・膵 | 第5回 |
| AB | 腹膜・腹壁・急性腹症 | 第6回 |
| XS | 症候・検査・栄養の横断項目 | 第7回 |
| NG | 神経消化器病（腸脳相関病・機能性消化管疾患）、Rome V 対応 | 特別回（日本神経消化器病学会の広報用） |

- 形式は `接頭辞-3桁連番`（例：`ES-012`）。
- 欠番は欠番のまま残し、詰めない。

---

## 5. ディレクトリ構成

```
cleanroom-gi-facts/
  CLAUDE.md                  ← このファイル
  PROJECT_INSTRUCTIONS.md    ← claude.ai のProject用（調査ラウンドで使う）
  schema/fact.schema.json    ← 事実票のJSON Schema
  data/
    facts/<接頭辞>.yaml      ← 正本（領域ごとに1ファイル）
    sources/sources.yaml     ← 出典マスター（SRC-xxx）
    curriculum/              ← コアカリCSV等（利用規約に従い出典を明記）
  raw/                       ← 調査レポートのMarkdown（手を加えない原本）
  proposals/                 ← Claude Codeの提案（人間の承認待ち）
  reports/                   ← 検証・照合のレポート
  review/                    ← 専門医レビュー用シート（CSV/XLSX）
  scripts/                   ← Pythonスクリプト
  docs/handover/             ← 各回の引き継ぎメモ
  docs/tasks/                ← Claude Code向け作業指示書
  docs/video/                ← ショート動画の監修用資料
  video/                     ← 事実カードからナレーション入りショート動画を作る仕組み（video/README.md）
  .cache/                    ← API応答キャッシュ（git管理外）
  .env                       ← NCBI_API_KEY, CONTACT_EMAIL（git管理外）
```

---

## 6. 外部APIの使い方

- **Crossref**：`https://api.crossref.org/works/{DOI}`
  - 取得するもの：書誌と `license`（URL・開始日・content-version）。
  - `mailto` パラメータに `CONTACT_EMAIL` を付ける。
- **NCBI**
  - ID変換：`https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=...&format=json`
  - E-utilities：`esearch`（`{DOI}[doi]` 検索）、`esummary`
  - `tool` と `email` を付ける。APIキーなしは毎秒3回まで、キーありは毎秒10回まで。
- 応答は `.cache/` にJSONで保存し、同じ問い合わせを繰り返さない。
- 失敗やタイムアウトの扱い：その項目を `unresolved` としてレポートに残す。値を推測で埋めない。

---

## 7. 作業の進め方

- 具体的な手順は `docs/tasks/claude_code_tasks.md` に従う。
- 着手時は、まず最新の `docs/handover/*.md` を読む。
- 作業の最後に `python scripts/validate.py` を実行し、エラー0件を確認する。
- 1つのフェーズが終わるたびに次のことを行い、次のフェーズに進む前に人間の確認を求める。
  - `reports/` に結果を出す。
  - 変更内容を要約する。
  - gitでコミットする（メッセージは日本語可）。

---

## 8. ショート動画（video/）での注意

- 動画の原稿（`video/scripts/*.json`）の各場面は、必ず `data/facts/` のカードIDを根拠に持つ。根拠のない文・カードにない数字は `video/check.py` が不合格にする。
- 一般向けの動画では薬剤名を出さない。実在の人物のアバターは使わない。AIで作成したことを表示する。
- CC BY-NC-ND の出典の図表は動画に使わない。収益化もしない。
- 公開は、監修者が承認したものに限る。生成した動画（`video/out/`）はリポジトリに入れない。
