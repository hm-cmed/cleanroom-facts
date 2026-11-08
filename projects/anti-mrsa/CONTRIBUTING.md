# 専門家レビューの手順（projects/anti-mrsa）

このフォルダは、レポジトリ本体の GitHub 監修（Issue フォーム・Actions）の対象外です。次の手順で確認します。

## 事実票の確認

1. `reports/coverage.md` で担当コースの事実票を確認します。
2. 誤り・不足があれば、Issue を作成する（タイトルの先頭に「[anti-mrsa]」）か、`facts/*.yaml` を編集して Pull Request を出してください。
3. 確認が済んだ事実票は、確認者（人間）が `review_status` を `approved` に、`reviewers` に確認者（役割と氏名またはID）、`last_reviewed_at` に日付を記入します。**Claude Code はこの3項目に値を入れません**（本体 CLAUDE.md 第1節4と同じ扱い）。
4. `review_notes` に記載された確認事項は、確認後に削除するか回答を書き込みます。
5. 主張文（`normalized_statement`）と数値を Claude Code が直す必要があると判断した場合は、本体の `proposals/` に提案を出し、人間の承認を待ちます。

## ギャップへの意見

1. `gaps/expert_input_items.yaml` の `expert_questions` に回答してください（Issue のタイトル先頭に「[anti-mrsa] 専門家の意見」）。
2. 研究者が回答を `evidence_class: expert_survey_tendency` または教育上の設計として事実票化し、【専門家の意見】等のラベルを付けます。ガイドラインの推奨としては表示しません。

## 新しい出典の追加

Issue（タイトル先頭に「[anti-mrsa] 出典の追加」）に、書誌情報・DOI・ライセンス・ライセンスを確認した場所を記入してください。ライセンスを確認するまで、その出典から事実票を作りません。DOI などの識別子は、API で照合できるまで `identifier_verification: search_only` のままにします。

## 変更の検証

変更したら `python scripts/validate.py` を実行し、エラー0件を確認してください。区分D・Eの出典を根拠にした事実票はエラーになります。
