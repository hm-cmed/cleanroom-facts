# cleanroom-facts — 医学・医療者教育の事実票（クリーンルーム方式）

医学教育コンテンツと評価問題を「クリーンルーム方式」で作るための、著作権で保護される表現を含まない事実票（fact card）と、その出典の記録です。旧名 cleanroom-gi-facts。

- 消化器から始め、医師国家試験の出題基準の全分野に広げました。医療者教育と、根拠に基づく医療・研究方法の分野も入っています（分野と領域の一覧は `data/domains.yaml`）。
- 事実票は、5択問題サイト（[cleanroom-mcq](https://github.com/hm-cmed/cleanroom-mcq)）と、ナレーション入りのショート動画（`video/`）の材料になります。
- 作業のルールは [CLAUDE.md](CLAUDE.md) にあります。Claude Code はこのファイルを読んで作業します。

## 収録状況（2026-11-27）

| 分野 | 接頭辞 | 件数 | うち出典照合済み（verified_sources） |
|---|---|---|---|
| 消化器 | HP・UG・ES・GD・IN・LV・BP・AB・XS・NG・PE | 966 | 341 |
| 循環器 | AR・HF・IH・VD・MP・CH・HT・VS・CX | 303 | 0 |
| 呼吸器 | RI・RO・IL・PV・LC・PL・RX | 308 | 0 |
| 腎・泌尿器・生殖器 | GN・KT・KF・KX・UR・GU・GY・RP | 355 | 0 |
| 内分泌・代謝・栄養・乳腺 | EN・TH・DM・MT・BR・IE・EX | 201 | 0 |
| 皮膚・頭頸部 | SK・DT・SD・HX・EY・RE・OT・NL・OR・TR | 385 | 0 |
| 神経・運動器 | ST・BT・NI・ND・EP・PN・NM・SP・NX・BD・OS・BO・TJ・AN | 513 | 0 |
| 感染症 | VI・HV・CM・BA・MY・FG・IG | 167 | 0 |
| 血液・造血器 | RC・BL・ML・LY・HS・PB | 148 | 0 |
| アレルギー・膠原病・免疫 | AL・CT・VA・SA・ID | 106 | 0 |
| 周産期・先天・成長発達 | PG・DL・FT・NB・CG・GR・PD | 142 | 0 |
| 精神・心身医学 | OG・SB・SZ・MD・AX・PH・DV・PR・PX | 135 | 0 |
| 生活環境・職業性 | FP・TX・SM・OC・EV・OX | 105 | 0 |
| 医療者教育（医療系の全職種） | ME | 112 | 0 |
| 根拠に基づく医療・研究方法 | EB | 12 | 0 |
| **合計** | 108領域 | **3,958** | **341** |

- 件数は、廃止したカード（retired、40件）を除いた数です。廃止したカードも ID を残しています。
- `python scripts/validate.py` の結果は、エラー0件・警告0件です（reports/ の最新の validate_*.md）。
- 専門医の監修（`verified_expert`）はまだ0件です。監修は、動画などを作る時点で行います。
- 出典マスターは data/sources/sources.yaml（2,601件）。主出典の区分は次のとおりです（廃止を除く）。
  - 制限付き（RESTRICTED）2,726件：数値と方向性だけを自作の文で使い、表現・表・図は使いません。
  - 自由に使える資料：OPEN（CC BY・CC0）747件、日本の公的資料（GOV_JP）309件、米国連邦政府の著作物（GOV_US）161件。
  - ライセンス未確認（UNKNOWN）15件。
- 照合の経過は `reports/`（取り込み・識別子照合・内容照合・カリキュラム番号）と、各カードの `history` に記録しています。
- コアカリ（令和4年度版）と医師国家試験の出題基準（令和6年版）の表は `data/curriculum/`、番号の参照表は `docs/tasks/curriculum_reference.md`。

## フォルダ

| 場所 | 中身 |
|---|---|
| `data/facts/<接頭辞>.yaml` | 事実票の正本（領域ごとに1ファイル） |
| `data/sources/sources.yaml` | 出典マスター（書誌メタデータだけ） |
| `schema/fact.schema.json` | 事実票の JSON Schema |
| `raw/` | 調査ラウンドの成果物（手を加えない原本） |
| `scripts/validate.py` | 品質チェック |
| `reports/` `proposals/` `review/` | 照合レポート／人間の承認待ちの提案／専門医レビュー用シート |
| `docs/handover/` `docs/tasks/` | 各回の引き継ぎメモ／Claude Code の作業指示書 |
| `video/` | ショート動画の自動作成（[video/README.md](video/README.md)） |
| `docs/video/` | 動画の監修用資料 |
| `PROJECT_INSTRUCTIONS.md` | claude.ai の Project（調査ラウンド）用の指示 |

## 使い方（PowerShell）

```powershell
git clone https://github.com/hm-cmed/cleanroom-facts
cd cleanroom-facts
pip install -r requirements.txt
python scripts/validate.py
```

## 監修（GitHub で行う）

専門医による監修は、GitHub の画面だけでできます（全分野が対象）。

1. 監修者を Settings → Collaborators で招待する（書き込み権限のある人の監修だけが自動で反映されます）。
2. 監修者は [review/github/README.md](review/github/README.md) を開き、領域のページでカードを出典と照らして読む。
3. 問題がなければ「まとめて承認する」、直すべきカードは「このカードを監修する」→「修正が必要」から送信する。
4. 数分で GitHub Actions がカードに監修者・日付を記録し（status: verified_expert）、監修ページも更新されます。修正案は `proposals/` に残り、カードの文章は変わりません。
5. 問題サイト（[cleanroom-mcq](https://github.com/hm-cmed/cleanroom-mcq)）は、ここの最新版を自動で取り込みます。

Excel のレビューシート（`review/*.xlsx`、`scripts/import_review.py`）も引き続き使えます。

## 注意

- 論文やガイドラインの本文・PDF・図表は、リポジトリに入れません（CLAUDE.md 第1節）。
- 事実票は専門職向けの命題です。一般向けの文は、事実票を材料にして別の工程で書き起こし、監修を受けてから公開します。
