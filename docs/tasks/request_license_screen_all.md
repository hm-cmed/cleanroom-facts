# ライセンス未確認（UNKNOWN）の出典の一括ふるい分けの依頼（残り全件）

依頼者：三原弘（2026-11-24）。結果は1つの Markdown（license_screen_all.md）にまとめてください。

## 1. 今回のやり方（第1回・第2回からの変更点）

- **対象は作り手が自分で選んでください。** hm-cmed/cleanroom-facts の最新版を取得し、`data/sources/sources.yaml` で `source_class: UNKNOWN` の出典のうち、いずれかのカードが `provenance.source_ref` で使っているものをすべて対象にします（2026-11-24 時点で約230件）。次のものは除きます。
  - 添付文書・インタビューフォーム（製薬会社の作成。CLAUDE.md §2-2 により UNKNOWN のまま据え置く）
  - 第1回・第2回で判定済みのもの（reports/license_check_01_muse.md・license_check_02_muse.md）
- 1件ずつ出版社のページまで見に行く必要はありません。**まず機械的にふるい分け、OPEN の可能性があるものだけを詳しく確かめてください。**
  1. DOI があるもの：Crossref の license 欄（content-version が vor のもの）と、PMC の収載の有無（ID Converter）を確かめる。
     - license 欄に CC BY・CC0 がある、または PMC に刊行版が収載されている → 「詳しく確認」に回す。
     - どちらもない → **RESTRICTED（CC 表示なし）** と判定してよい。これまでの100件では、この条件で OPEN になったものは1件もありませんでした。
  2. 「詳しく確認」に回したもの：これまでと同じく、出版社のページか PMC の刊行版ページで表示を確かめる（著者原稿の表示は使わない）。CC BY・CC0 なら OPEN、CC BY-NC・ND・SA 系なら RESTRICTED。
  3. DOI がないもの（ウェブページ、政府資料、書籍など）：1件ずつ発行元の表示を確かめる。日本の府省・公的機関・地方自治体の資料なら GOV_JP、米国連邦政府なら GOV_US の候補として、根拠を書く（CLAUDE.md §2-2 の決まりを参照）。

## 2. すでに分かっていることは使い回してください

調べ直さなくてよいものです（第1回・第2回と、ほかの照合で確認済み）。

| 対象 | 区分 | 根拠 |
|---|---|---|
| StatPearls（NCBI Bookshelf）の章 | RESTRICTED | 章ページの表示が CC BY-NC-ND 4.0 |
| American Family Physician | RESTRICTED | 全号の PDF のフッターに © AAFP。私的・非商用の利用だけを認める |
| Elsevier の「open-access user license 1.0」 | RESTRICTED | CC ではない |
| Wiley の termsAndConditions#vor、Springer Nature の TDM 用ライセンス | RESTRICTED | CC ではない |
| WHO の 2010〜2011 年ごろの刊行物 | RESTRICTED | © WHO、All rights reserved |
| NICE のガイドライン | RESTRICTED | © NICE、Notice of rights |
| 難病情報センターの掲載物 | RESTRICTED | CLAUDE.md §2-2（2026-11-13 の決定） |
| 厚労科研データベース（mhlw-grants.niph.go.jp）の報告書で権利表記がないもの | GOV_JP | CLAUDE.md §2-2（2026-11-15・11-24 の決定） |
| 地方自治体の公開資料 | GOV_JP | CLAUDE.md §2-2（2026-11-24 の決定） |

同じ雑誌でも、論文によって CC BY のもの（オープンアクセスで出た論文）があります。雑誌名だけで決めず、上の1の手順で Crossref を確かめてください。

## 3. 結果の書き方

1. 集計（OPEN・RESTRICTED・GOV_JP・GOV_US・確認できず の件数）
2. 「詳しく確認」に回したものと、DOI がないものの根拠（1件ずつ、根拠の URL と表示の要約）
3. 最後に機械可読の一覧表（全件）

| SRC | 判定 | ライセンスの表示 | 根拠の URL | 備考 |
|---|---|---|---|---|

- 機械的に RESTRICTED と判定したものは、「ライセンスの表示」に「Crossref に CC なし・PMC 刊行版なし」と書き、根拠の URL は Crossref の API の URL にしてください。
- 書誌や識別子の食い違い、補完できる識別子に気づいたら、備考に書いてください。
- 論文の本文は保存しないでください。
