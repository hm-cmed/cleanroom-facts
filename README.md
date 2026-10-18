# cleanroom-gi-facts — 消化器 事実票（クリーンルーム方式）

医学教育コンテンツと評価問題を「クリーンルーム方式」で作るための、著作権で保護される表現を含まない事実票（fact card）と、その出典の記録です。
事実票を材料にして、日本神経消化器病学会の広報用ショート動画を作る仕組み（`video/`）も入っています。

作業のルールは [CLAUDE.md](CLAUDE.md) にあります。Claude Code はこのファイルを読んで作業します。

## 収録状況（2026-10-18）

| 接頭辞 | 範囲 | 件数 | 原本レポート | 状態 |
|---|---|---|---|---|
| HP・UG | パイロット | 20・18 | raw/00_pilot_hp_ug.md | draft（照合前） |
| ES | 第1回 食道 | 93 | raw/01a・01b（v1・v2 を統合済み） | verified_sources 55、draft 34、retired 4 |
| GD | 第2回 胃・十二指腸 | 95 | raw/02_gastroduodenal.md | verified_sources 94、draft 1 |
| IN | 第3回 小腸・大腸 | 89 | raw/03_intestine.md | verified_sources 89（IN-089 は照合時に起票） |
| LV | 第4回 肝 | 104 | raw/04_liver.md | verified_sources 104 |
| BP | 第5回 胆・膵 | 68 | raw/05_biliary_pancreas.md | draft（取り込み済み、照合は保留） |
| AB | 第6回 腹膜・腹壁・急性腹症 | 86 | raw/06_abdomen.md | draft（取り込み済み、照合前） |
| XS | 第7回 横断項目 | — | — | 未着手 |
| NG | 特別回 神経消化器病（Rome V 対応） | 240 | raw/N1_neurogastroenterology.md | draft（照合前） |

- 合計813件。`python scripts/validate.py` の結果はエラー0件（reports/validate_20261018.md）。
- 専門医の検証（`verified_expert`）はまだ0件です。専門医レビュー用シートは `review/`。
- 出典マスターは data/sources/sources.yaml（161件、SRC-001〜161）。
- 照合の経過は `reports/`（取り込み・識別子照合・内容照合・カリキュラム番号）と各カードの `history` に記録しています。
- コアカリ（令和4年度版）の CSV は `data/curriculum/`、番号の参照表は `docs/tasks/curriculum_reference.md`。

## フォルダ

| 場所 | 中身 |
|---|---|
| `data/facts/<接頭辞>.yaml` | 事実票の正本（領域ごとに1ファイル） |
| `data/sources/sources.yaml` | 出典マスター（書誌メタデータだけ） |
| `schema/fact.schema.json` | 事実票の JSON Schema |
| `raw/` | claude.ai の調査レポート（手を加えない原本） |
| `scripts/validate.py` | 品質チェック |
| `reports/` `proposals/` `review/` | 照合レポート／人間の承認待ちの提案／専門医レビュー用シート |
| `docs/handover/` `docs/tasks/` | 各回の引き継ぎメモ／Claude Code の作業指示書 |
| `video/` | ショート動画の自動作成（[video/README.md](video/README.md)） |
| `docs/video/` | 動画の監修用資料 |
| `PROJECT_INSTRUCTIONS.md` | claude.ai の Project（調査ラウンド）用の指示 |

## 使い方（PowerShell）

```powershell
git clone https://github.com/hm-cmed/cleanroom-gi-facts
cd cleanroom-gi-facts
pip install -r requirements.txt
python scripts/validate.py
```

## 注意

- 論文やガイドラインの本文・PDF・図表は、リポジトリに入れません（CLAUDE.md 第1節）。
- 事実票は専門職向けの命題です。一般向けの文は、事実票を材料にして別の工程で書き起こし、監修を受けてから公開します。
