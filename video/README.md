# ショート動画の自動作成（試作）

`video/scripts/` に置いた原稿（JSON）を、まとめてナレーション入りの縦型動画にします。
根拠の照合には、リポジトリの事実カード（`data/facts/*.yaml`）を直接使います。

## 準備（Windows、最初の1回だけ）

1. Python 3 を入れる（インストール時に「Add python.exe to PATH」にチェックを入れる）。
2. PowerShell で次を実行する。
   ```powershell
   winget install Gyan.FFmpeg
   pip install -r requirements.txt
   ```
3. 日本語の音声が入っているか確認する（設定 > 時刻と言語 > 言語 > 日本語 > 音声）。

## 使い方

- `video\run_all_windows.bat` をダブルクリックすると、`scripts/` の原稿がすべて動画になる。
- 出力は `video/out/<原稿名>/` に入る（git管理外）。
  - `<原稿名>.mp4`：動画
  - `check.json`：照合結果
  - `still_N.png`：監修用の静止画
- `video/out/summary.json` に全体の一覧が出る。
  - 照合で不合格の原稿は作らずに飛ばし、理由を表示する。
  - 作成済みで、原稿が変わっていないものは飛ばす。
- 作り直すときは `run_all_windows.bat --force` を実行する。
- 音声なしで流れだけ確かめるときは `python make_all.py --tts dummy` を実行する。

## 1本ごとの流れ

1. 照合（根拠カード・数字・禁止表現）
2. 場面ごとの音声合成（`speech` 欄を読む）
3. 音声の長さで場面の長さを決める（前0.4秒＋音声＋後0.5秒）
4. 照合（全体30〜60秒・字幕の速さ）
5. 映像に音声を重ねて MP4 にする

## 原稿の書き方（見本：`scripts/IBS_RomeV_001.json`）

| 欄 | 内容 |
|---|---|
| `narration` | 画面の字幕 |
| `speech` | 読み上げ用の文（例：Rome V → ローマ・ファイブ） |
| `cards` | 根拠のカードID。字幕の数字は、カードにある数字でなければ不合格 |
| `visual` | 絵の種類。現在は question / gutbrain / calendar / check / doctor の5種類（`render.py` の `ILL`） |

## ファイル

| ファイル | 役割 |
|---|---|
| `make_all.py` | 一括作成 |
| `render.py` | 映像 |
| `check.py` | 照合 |
| `tools/tts_windows.ps1` | Windows の音声合成 |
| `tools/select_cards.py` | 一般向けに使えるカードの候補を選ぶ |

## 今後の課題

- 音声を Google Cloud Text-to-Speech などに替える。替えるのは `make_all.py` の音声合成の部分だけ。そうすると GitHub Actions で自動実行できる。
- カードから原稿（JSON）を AI で作る段階を作る。監修者の承認後に `scripts/` へ置く運用を想定。
- 絵の種類を増やす。
