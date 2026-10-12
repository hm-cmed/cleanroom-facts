# Phase 0：環境構築レポート（2026-10-12）

## 実施内容

| 項目 | 結果 |
|---|---|
| git リポジトリ | `git init -b main` で作成 |
| Python | 3.11.9（`py` ランチャーが無いため `python3.11` で venv を作成） |
| venv | `.venv/`（git管理外） |
| パッケージ | pyyaml, jsonschema, requests, python-dotenv, pandas, openpyxl, pdfplumber, rapidfuzz（依存込みで `requirements.txt` に固定） |
| `.gitignore` | `.venv/` `.cache/` `.env` `__pycache__/` |
| `.gitattributes` | `* text=auto eol=lf`（追加。下記参照） |
| `.env` | 既存。`CONTACT_EMAIL` と `NCBI_API_KEY` は値が入っていることだけ確認（値は読んでいない）。git管理外 |
| `raw/` | 3ファイルを配置済み |

## 指示書との差分・注意点

1. **raw ファイル名を修正した。** 配置時のファイル名が `*.md.md` になっていたため、指示書どおり `00_pilot_hp_ug.md`、`01a_esophagus_v1.md`、`01b_esophagus_v2.md` に改名した。中身は変更していない。
2. **pandas を 2.3.3 に固定した。** 最新の 3.0.6 は、Windows の Smart App Control（強制モード）によって拡張モジュール `indexing` の DLL 読み込みがブロックされた。セキュリティ設定は変更せず、ブロックされない 2.3.3 を採用した。`requirements.txt` は 2.3.3 で固定済み。
   - 同様のブロックが初回に `rpds`（jsonschema の依存）でも一度発生したが、再試行で読み込めた。今後スクリプト実行時に同じエラーが出た場合は、まず再実行を試す。
3. **`.gitattributes` を追加した（指示書に無い項目）。** グローバル設定 `core.autocrlf` により、チェックアウト時に `raw/` が CRLF に変換されるのを防ぐため、作業ツリーを LF に固定した。
4. **リポジトリが OneDrive 配下にある。** `.venv/` や `.cache/` も同期対象になる。同期による遅延やファイルロックが問題になる場合は、OneDrive の対象から外すことを検討してほしい（人間の判断事項）。

## 完了条件の確認

- [x] venv が作成され、全パッケージの import が通る
- [x] `raw/` に 3 ファイルがある
- [x] 初回コミット済み
