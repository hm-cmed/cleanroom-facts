# 引き継ぎメモ：内分泌・代謝・栄養・乳腺の開始（2026-10-28）

## 1. これまでの分野の現状

- 消化器 857件、循環器 266件、呼吸器 299件、腎・泌尿器・生殖器 335件（計 1,757件、全件 draft。消化器の一部は verified_sources）。
- 腎・泌尿器・生殖器（第15〜19回）は Muse が作り、受け入れ検査を通して取り込んだ（`reports/01_ingest_KU_summary.md`）。
- 出題基準の表（Ⅳ・Ⅴ・Ⅵ・Ⅷ・Ⅹ）は厚生労働省 PDF のテキスト層と突き合わせ済み（`reports/kokushi_text_check_20261028.md`）。

## 2. 内分泌・代謝・栄養・乳腺（第20〜22回）

- 分割は Muse の案（`proposals/20_endocrine_division_proposal.md` 第2版）を検査して登録（`reports/plan_check_20.md`）。
- 依頼文：`docs/tasks/round20_EN.md`。受け入れ検査の仕様：`docs/tasks/specs/round20〜22.yaml`。
- 接頭辞：第20回 EN・TH、第21回 DM・MT、第22回 BR・IE・EX。
- SRC 番号：第20回 SRC-871〜940、第21回 941〜1010、第22回 1011〜1070（4桁可）。
- 原本の保存名：`raw/20_en_a.md`〜`raw/22_en_c.md`。取り込みは `python scripts/ingest_round.py raw/20_en_a.md EN,TH` のように行う。

## 3. 作り手への注意（これまでの回の教訓）

- 出題基準・コアカリの番号は表からそのまま写す（第19回の差し戻し）。
- 出典の重複確認は出典マスター全体と照らす（第18回）。
