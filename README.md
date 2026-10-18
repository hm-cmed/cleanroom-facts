# cleanroom-gi-facts — 消化器 事実票（クリーンルーム方式）

医学教育コンテンツと評価問題を「クリーンルーム方式」で作るための、著作権で保護される表現を含まない事実票（fact card）と、その出典の記録です。
事実票を材料にして、日本神経消化器病学会の広報用ショート動画を作る仕組み（`video/`）も入っています。

作業のルールは [CLAUDE.md](CLAUDE.md) にあります。Claude Code はこのファイルを読んで作業します。

## 収録状況（2026-10-18）

| 接頭辞 | 範囲 | 件数 | 原本レポート | 状態 |
|---|---|---|---|---|
| HP・UG | パイロット | — | 未収録（raw/00_pilot_hp_ug.md を置く） | 取り込み前 |
| ES | 第1回 食道 | — | 未収録（raw/01a・01b を置く） | 取り込み前・統合待ち |
| GD | 第2回 胃・十二指腸 | 95 | raw/02_gastroduodenal.md | draft |
| IN | 第3回 小腸・大腸 | 88 | raw/03_intestine.md | draft |
| LV | 第4回 肝 | 104 | raw/04_liver.md | draft |
| BP | 第5回 胆・膵 | 68 | raw/05_biliary_pancreas.md | draft |
| AB・XS | 第6・7回 | — | — | 未着手 |
| NG | 特別回 神経消化器病（Rome V 対応） | 240 | raw/N1_neurogastroenterology.md | draft |

- 合計595件。`python scripts/validate.py` の結果はエラー0件（reports/validate_20261018.md）。
- 専門医の検証（`verified_expert`）はまだ0件です。
- 出典マスターは data/sources/sources.yaml（128件、SRC-017〜153）。食道の SRC-001〜016・019〜027 は、ES の取り込み時に追加します。

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
