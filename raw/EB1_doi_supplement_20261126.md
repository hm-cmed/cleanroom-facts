# EB1 補完メモ：受け入れ検査「できれば」1件（DOIが空の出典4件）への調査結果

作成：2026-11-26夜／対象：EB1_evidence_methods.md（受け入れ検査 合格、必須修正0件、望ましい修正1件）
検査レポートの指摘「論文と思われるのに DOI が空の出典：SRC-5500・5501・5510・5515。DOI があれば書く」について、Crossref で追加調査した結果。

## 結論

| SRC | DOI の有無 | 対応 |
|---|---|---|
| SRC-5501（Richardson 1995） | **あった**：`10.7326/acpjc-1995-123-3-a12` | 成果物への反映を推奨（下記） |
| SRC-5500（Cochrane Handbook） | 章 DOI は2019年書籍版のもののみ（Ch.2：10.1002/9781119536604.ch2、Ch.8：10.1002/9781119536604.ch8）。カードが引用したのはオンライン版 version 6.5（2024）で、書籍版 DOI を付けると版の同一性を誤らせる | 現行どおり null を推奨。付けるかどうかは取り込み側の判断 |
| SRC-5510（GRADE Handbook） | Crossref 検索で該当なし（オンライン版のみ） | null のまま |
| SRC-5515（AMED ガイドブック） | DOI なし（機関刊行物） | null のまま |

## SRC-5501 の検証記録

- Crossref（api.crossref.org/works/10.7326/acpjc-1995-123-3-a12）で 2026-11-26 に確認：題名 "The well-built clinical question: a key to evidence-based decisions"、誌名 ACP Journal Club、刊行 1995-11-01 で、成果物の書誌と一致。
- 成果物作成時の調査では「PMID・DOI なし」としていたが、DOI は後年に付与されていたもの。PMID は引き続きなし。

## 反映する場合の変更箇所（EB1_evidence_methods.md、3か所）

1. §1 出典表、SRC-5501 の行：DOI 列「なし」→ `10.7326/acpjc-1995-123-3-a12`
2. EB-001 の uncertainty：「Richardson 1995 には PMID・DOI が付与されていないため、題名・誌名・年で登録した。」→「Richardson 1995 には PMID が付与されていないため、DOI と題名・誌名・年で登録した。」（趣旨）
3. §3 未解決事項には Richardson の DOI に関する記載はないため変更不要。§5 の検証記録は当時の調査結果としてそのまま残し、本メモを正とする。
