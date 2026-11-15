# 出典棚卸し 申し送りメモ（バッチ1〜100 集約）

- 対象：パブリックドメイン出典棚卸し バッチ1〜100（全2,922件）の成果物（`batch*.md` / `batch*.json`）に記録された、レポジトリ側（登録担当）への申し送り事項の集約。
- 方法：各バッチの D 判定・申し送り・備考・重要な発見から機械的に抽出し、出典（SRC）単位・項目単位に重複を整理した。「再掲」と明記されたものは二重計上せず、初出バッチを正として再掲バッチを併記した。カードの主張・数値の変更は行っていない（集約のみ）。
- 件数総括：第1節 区分訂正（正式）226件／区分の明確化申し送り 35件／現行区分の確認のみ 4件、第2節 識別子補完候補 789件（680出典）、第3節 要・正本確認 17件、第4節 監視事項 72件、第5節 license_note 更新提案 16件、第6節 再調査候補 21件（環境要因の保留 5件＋バッチ明記の再調査候補 16件）、第7節 候補側の数値の使用注意（代表例 25件＋総括）、第8節 候補の新規登録が要る件 17件。
- 注記：バッチ1〜22は旧ルール（抄録・添付文書・医学百科を根拠にしうる時代）の成果物で、それらの A 判定の大半は現行ルールでは成り立たないが、D 訂正・監視事項の申し送りは今も有効である。バッチ23以降は現行ルール（抄録・添付文書・医学百科は根拠にしない）で判定されている。

## 1. 区分訂正（D）一覧

### 1-1. 正式な区分訂正（226件、出典単位）

内訳：UNKNOWN→RESTRICTED 193件、UNKNOWN→OPEN 28件、RESTRICTED→OPEN 4件、UNKNOWN→GOV_JP 1件。再掲は初出バッチに統合し、再掲バッチ欄に併記した。

| SRC | 現行区分 | 訂正後区分 | 根拠（ライセンス等の個別確認結果） | 初出バッチ | 再掲バッチ |
|---|---|---|---|---|---|
| SRC-2027 | UNKNOWN | OPEN | CC BY を確認 | 2 | — |
| SRC-435 | UNKNOWN | OPEN | CC BY を確認（Europe PMC） | 2 | — |
| SRC-049 | UNKNOWN | OPEN | CC BY を確認（バッチ3の重要な発見1で提案、バッチ5で D として再掲） | 3 | 5 |
| SRC-141 | UNKNOWN | OPEN | CC BY を確認（NG-123 の主出典） | 4 | — |
| SRC-048 | UNKNOWN | OPEN | CC BY を確認 | 5 | — |
| SRC-051 | UNKNOWN | OPEN | CC BY を確認 | 5 | — |
| SRC-052 | UNKNOWN | OPEN | CC BY を確認 | 5 | — |
| SRC-018 | UNKNOWN | OPEN | J Gastroenterol（Springer）。刊行版ライセンスを3経路で個別確認し、いずれも CC BY 4.0：Crossref の版データに CC BY 4.0（version of record、2021-07-07 開始）、Europe PMC の個別レコードで license: cc by、PMC 全文… | 7 | 10・92 |
| SRC-028 | UNKNOWN | OPEN | CC BY を確認 | 7 | — |
| SRC-029 | UNKNOWN | OPEN | CC BY を確認 | 7 | — |
| SRC-030 | UNKNOWN | OPEN | CC BY を確認 | 7 | — |
| SRC-032 | UNKNOWN | OPEN | CC BY を確認 | 7 | — |
| SRC-042 | UNKNOWN | OPEN | CC BY を確認 | 7 | — |
| SRC-074 | UNKNOWN | OPEN | CC BY を確認 | 10 | — |
| SRC-088 | UNKNOWN | OPEN | CC BY を確認 | 12 | — |
| SRC-089 | UNKNOWN | OPEN | CC BY を確認 | 12 | — |
| SRC-097 | UNKNOWN | OPEN | CC BY を確認 | 12 | — |
| SRC-4231 | RESTRICTED | OPEN | CC BY を確認 | 12 | — |
| SRC-4303 | UNKNOWN | OPEN | CC BY を確認 | 28 | — |
| SRC-4310 | RESTRICTED | OPEN | CC BY を確認 | 28 | — |
| SRC-371 | UNKNOWN | OPEN | CC BY 4.0 を Crossref・Europe PMC の両経路で確認（COPD ガイドライン第7版の英語サマリー） | 29 | — |
| SRC-383 | UNKNOWN | OPEN | CC BY 4.0 を Crossref・Europe PMC の両経路で確認 | 29 | — |
| SRC-385 | UNKNOWN | OPEN | CC BY を Europe PMC・PMC 全文の表示で確認 | 29 | — |
| SRC-649 | UNKNOWN | OPEN | CC BY を確認（Yamamoto 2017） | 34 | 36 |
| SRC-243 | UNKNOWN | GOV_JP | PMDA の審査報告書そのもの（同種の政府文書 SRC-417 が GOV_JP の先例） | 39 | — |
| SRC-254 | UNKNOWN | OPEN | CC BY 4.0 を Crossref・Europe PMC の両方で確認（Sports Med 2023） | 39 | — |
| SRC-367 | UNKNOWN | OPEN | CC BY を確認（Emerg Infect Dis 2016） | 46 | — |
| SRC-238 | UNKNOWN | RESTRICTED | Crossref の version-of-record ライセンスは NEJM Group の利用条件（http://www.nejmgroup.org/legal/terms-of-use.htm）で、CC ライセンスではないことを DOI 10.1056/NEJMoa1814052 で個別に確認した（2026-1… | 48 | — |
| SRC-239 | UNKNOWN | RESTRICTED | Crossref の version-of-record ライセンスは NEJM Group の利用条件で、CC ライセンスではないことを DOI 10.1056/NEJMoa2209051 で個別に確認した（2026-11-12）。SRC-238 と同型で、出版社著作物と確定できる | 48 | — |
| SRC-4393 | UNKNOWN | RESTRICTED | Crossref（DOI 10.1038/nrcardio.2016.57）のライセンスは text-and-data-mining 用の権利のみで CC ライセンスはなく、Nature Reviews Cardiology の © Springer Nature の総説であることを個別に確認した（2026-11-12… | 48 | — |
| SRC-1632 | UNKNOWN | RESTRICTED | SRC-1632（NI-002 の主出典、Berger et al. PML diagnostic criteria, Neurology 2013）：UNKNOWN → RESTRICTED。Europe PMC の個別レコードで、PMC3662270 に著者原稿が収載されるものの isOpenAccess は N … | 49 | — |
| SRC-1633 | UNKNOWN | RESTRICTED | SRC-1633（NI-003 の主出典、Antinori et al. Updated research nosology for HIV-associated neurocognitive disorders, Neurology 2007）：UNKNOWN → RESTRICTED。PMC4472366 に著者原… | 49 | — |
| SRC-1635 | UNKNOWN | RESTRICTED | SRC-1635（NI-005 の主出典、Zerr et al. Updated clinical diagnostic criteria for sporadic Creutzfeldt-Jakob disease, Brain 2009）：UNKNOWN → RESTRICTED。Europe PMC の個別レコー… | 49 | — |
| SRC-1647 | UNKNOWN | RESTRICTED | SRC-1647（NI-022 の主出典、Leowattana et al. Tuberculosis of the spine, World J Orthop 2023）：UNKNOWN → RESTRICTED。Europe PMC の個別レコードでライセンスは CC BY-NC 4.0 と確認した（PMC1025… | 49 | — |
| SRC-692 | UNKNOWN | RESTRICTED | Europe PMC の個別レコードでライセンスは cc by-nc（PMC 掲載版は CC BY-NC 4.0）。オープンアクセスだが NC のため自由利用にはならず、UNKNOWN から RESTRICTED への訂正が必要 | 51 | — |
| SRC-693 | UNKNOWN | RESTRICTED | Journal of Urology 1996年の出版社の著作物。Europe PMC でオープンアクセスの表示がなく、PMC にも収載がなく、ライセンス表示はない。UNKNOWN から RESTRICTED への訂正が必要 | 51 | — |
| SRC-698 | UNKNOWN | RESTRICTED | NEJM 2014年。PMC に著者原稿が収載される（PMC4137319）がライセンス表示はなく、Europe PMC でもオープンアクセスではない。UNKNOWN から RESTRICTED への訂正が必要 | 51 | — |
| SRC-709 | UNKNOWN | RESTRICTED | Journal of Pediatric Surgery 1992年の出版社の著作物。オープンアクセスの表示はなく、ライセンス表示も確認できない。UNKNOWN から RESTRICTED への訂正が必要 | 51 | — |
| SRC-711 | UNKNOWN | RESTRICTED | Journal of Urology 2002年の出版社の著作物。オープンアクセスの表示はなく、ライセンス表示も確認できない。UNKNOWN から RESTRICTED への訂正が必要 | 51 | — |
| SRC-1455 | UNKNOWN | RESTRICTED | Journal of Burn Care & Research（Oxford University Press）の総説。Europe PMC の個別レコードでライセンス表示がなくオープンアクセスではなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1456 | UNKNOWN | RESTRICTED | Wilderness Medical Society の学会ガイドライン（Wilderness & Environmental Medicine、SAGE）。Crossref の出版版ライセンスはテキストマイニング用のみで、Europe PMC でもライセンス表示がなくオープンアクセスではない。UNKNOWN から R… | 54 | — |
| SRC-1457 | UNKNOWN | RESTRICTED | Journal of Burn Care & Research のレビュー。PMC に著者原稿が収載される（PMC5179293）がライセンス表示はなく、Europe PMC でもオープンアクセスではない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1459 | UNKNOWN | RESTRICTED | Eye（Springer Nature）の総説。Crossref の出版版ライセンスはテキストマイニング用のみで、PMC に収載がある（PMC7002428）もののライセンス表示はなくオープンアクセスではない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1461 | UNKNOWN | RESTRICTED | Otolaryngologic Clinics of North America（Elsevier）の総説。Europe PMC でライセンス表示がなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1462 | UNKNOWN | RESTRICTED | Laryngoscope（Wiley）の前向き研究。Europe PMC でライセンス表示がなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1464 | UNKNOWN | RESTRICTED | The Surgeon（Elsevier）の総説。Europe PMC でライセンス表示がなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1465 | UNKNOWN | RESTRICTED | International Journal of Oral and Maxillofacial Surgery（Elsevier）の系統的レビュー。Europe PMC でライセンス表示がなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1472 | UNKNOWN | OPEN | Balkan Medical Journal の総説。Europe PMC の個別レコードでライセンスが cc by であり、PMC 全文（PMC5635626）が CC BY で公開されている。主出典自体が自由利用できるため、UNKNOWN から OPEN への訂正が必要 | 54 | — |
| SRC-1473 | UNKNOWN | RESTRICTED | Clinics in Perinatology（Elsevier）の総説。Europe PMC でライセンス表示がなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1474 | UNKNOWN | RESTRICTED | Critical Care Clinics（Elsevier）の総説。Europe PMC でライセンス表示がなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1475 | UNKNOWN | RESTRICTED | International Journal of Nursing Studies（Elsevier）の系統的レビュー。Europe PMC でライセンス表示がなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1478 | UNKNOWN | RESTRICTED | Ophthalmology Clinics of North America（Elsevier）の総説。Europe PMC でライセンス表示がなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1480 | UNKNOWN | RESTRICTED | Laryngoscope（Wiley）のメタ解析。Europe PMC でライセンス表示がなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1481 | UNKNOWN | RESTRICTED | Tidsskrift for den Norske Laegeforening の総説。Europe PMC でライセンス表示がなく、PMC にも収載がない。UNKNOWN から RESTRICTED への訂正が必要 | 54 | — |
| SRC-1896 | UNKNOWN | RESTRICTED | Arch Bone Jt Surg 2016。PMC（PMC4733230）の permissions は「© BY THE ARCHIVES OF BONE AND JOINT SURGERY 2016, Mashhad University of Medical Sciences」という著作権表示のみで CC ライ… | 57 | — |
| SRC-1900 | UNKNOWN | RESTRICTED | J Cancer Res Ther 2018。Crossref にライセンス情報の配列がなく、Europe PMC でも Open Access ではない（isOpenAccess N）。CC の根拠がないため自由利用とは扱えない。 | 57 | — |
| SRC-1901 | UNKNOWN | RESTRICTED | Oncologist 2008。Crossref の VoR ライセンスは OUP の標準出版モデル（CHORUS）であり、CC ではない。 | 57 | — |
| SRC-1911 | UNKNOWN | RESTRICTED | J Clin Orthop Trauma 2016。PMC（PMC5106475）の permissions は「© 2016 Delhi Orthopedic Association. All rights reserved.」であり、Crossref は TDM 用途のみ。CC 表示はない。 | 57 | — |
| SRC-1916 | UNKNOWN | RESTRICTED | Oncologist 2014。PMC（PMC3926794）の permissions は © AlphaMed Press 2014 の表示で、Crossref も標準出版モデルのため CC ではない。 | 57 | — |
| SRC-1020 | UNKNOWN | RESTRICTED | 出版社（Mary Ann Liebert）の TDM ライセンスのみ。Europe PMC で isOpenAccess: N。CC ライセンス表示なし | 58 | 82 |
| SRC-3263 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。Crossref・Europe PMC の個別照会で OA・CC ライセンスなし | 58 | — |
| SRC-3264 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。個別照会で OA・CC ライセンスなし | 58 | — |
| SRC-3265 | UNKNOWN | RESTRICTED | Wolters Kluwer の購読制文献。個別照会で OA・CC ライセンスなし | 58 | — |
| SRC-3266 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。個別照会で OA・CC ライセンスなし | 58 | — |
| SRC-3267 | UNKNOWN | RESTRICTED | PMC 全文（PMC6505738）のページに「Copyright © 2019 The Cochrane Collaboration. Published by John Wiley & Sons, Ltd.」と明記され、CC ライセンスではない | 58 | — |
| SRC-3271 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。個別照会で OA・CC ライセンスなし | 58 | — |
| SRC-3272 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。個別照会で OA・CC ライセンスなし | 58 | — |
| SRC-3273 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。個別照会で OA・CC ライセンスなし | 58 | — |
| SRC-3275 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。個別照会で OA・CC ライセンスなし | 58 | — |
| SRC-3277 | UNKNOWN | RESTRICTED | Elsevier 誌の購読制文献。Crossref は TDM ライセンスのみで CC ライセンスなし | 58 | — |
| SRC-3278 | UNKNOWN | RESTRICTED | Elsevier 誌の購読制文献。Crossref は TDM ライセンスのみ | 58 | — |
| SRC-3280 | UNKNOWN | RESTRICTED | Europe PMC で isOpenAccess: N。Crossref は TDM ライセンスのみで、CC BY ではないことを個別に確認 | 58 | — |
| SRC-3281 | UNKNOWN | RESTRICTED | 出版社（Liebert）の TDM ライセンスのみ。PMC3109493 は著者原稿で CC ライセンス表示なし | 58 | — |
| SRC-3282 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。個別照会で OA・CC ライセンスなし | 58 | — |
| SRC-3283 | UNKNOWN | RESTRICTED | PMC 全文（PMC7050613）のページに「Copyright © 2015 The Cochrane Collaboration」と明記され、CC ライセンスではない | 58 | — |
| SRC-3284 | UNKNOWN | RESTRICTED | Elsevier 誌の購読制文献。Crossref は TDM ライセンスのみ | 58 | — |
| SRC-3285 | UNKNOWN | RESTRICTED | ACOG 誌の購読制文献。個別照会で OA・CC ライセンスなし | 58 | — |
| SRC-1371 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Elsevier のテキストマイニング用のみで、Europe PMC でも非OA・購読扱いである。PubMed 掲載ページに「Copyright © 2017 Elsevier Inc. All rights reserved.」と表示され、自由ライセンスは確認できない。 | 59 | — |
| SRC-1372 | UNKNOWN | RESTRICTED | Europe PMC で非OA であり、マスターの license_note どおり © American Academy of Family Physicians で自由ライセンスの表示はない。DOI は PubMed・Europe PMC のいずれにも登録がなく、マスターの null が正しい。 | 59 | — |
| SRC-1374 | UNKNOWN | RESTRICTED | Crossref にライセンス情報がなく、Europe PMC でも非OA・購読扱いで PMC の OA サブセットに収載されていない。要約版の関連レコードには「© 2020, International Rhinologic Society. All rights reserved.」の表示があり、誌サイトでの無料ダ… | 59 | — |
| SRC-1377 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Springer のテキストマイニング用のみで、Europe PMC でも非OA・購読扱いである。マスターの license_note どおり © Springer で CC 表示はない。 | 59 | — |
| SRC-1378 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスはテキストマイニング用のみで、Europe PMC でも非OA・購読扱いである。マスターの license_note どおり © Nature Portfolio で CC 表示はない。 | 59 | — |
| SRC-1379 | UNKNOWN | RESTRICTED | Europe PMC で非OA であり、マスターの license_note どおり © American Academy of Family Physicians で自由ライセンスの表示はない。なお Europe PMC レコードの doi 欄には無関係な DOI が混入しているため、識別子の補完には使わない（フラグ… | 59 | — |
| SRC-1380 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Elsevier のテキストマイニング用のみ（著者原稿版の Elsevier OA ユーザーライセンスは CC ではない）で、Europe PMC でも非OA・購読扱いである。 | 59 | — |
| SRC-1381 | UNKNOWN | RESTRICTED | Crossref に CC ライセンスはなく、Europe PMC でも非OA・購読扱いである。マスターの license_note どおり © BMJ Publishing Group である。 | 59 | — |
| SRC-1382 | UNKNOWN | RESTRICTED | Crossref の刊行版の利用条件は CC BY ではなく、Europe PMC でも非OA・購読扱いである。マスターの license_note どおり © American Cancer Society で CC 表示はない。 | 59 | — |
| SRC-1384 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Elsevier のテキストマイニング用のみで、Europe PMC でも非OA・購読扱いである。マスターの license_note どおり © Elsevier で CC 表示はない。 | 59 | — |
| SRC-1385 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Elsevier のテキストマイニング用と Elsevier OA ユーザーライセンス1.0で、いずれも CC BY ではなく、Europe PMC でも非OA・購読扱いである。 | 59 | — |
| SRC-2825 | UNKNOWN | RESTRICTED | Crossref にライセンス情報がなく、J-STAGE 掲載版にも CC 等の自由ライセンス表示はない（学会誌の著作物）。J-STAGE で無料で読めることはオープンライセンスの付与ではない。 | 59 | 60 |
| SRC-2812 | UNKNOWN | RESTRICTED | Crossref の VoR ライセンスは Wiley の利用条件のみで、Europe PMC でも非OA・購読扱い。CC 表示はない | 60 | — |
| SRC-2814 | UNKNOWN | RESTRICTED | Crossref の VoR ライセンスは Wiley の利用条件のみで、Europe PMC でも非OA・購読扱い。CC 表示はない | 60 | — |
| SRC-2815 | UNKNOWN | RESTRICTED | Crossref にライセンス情報がなく、Europe PMC でも非OA。JAMA の購読論文で CC 表示はない | 60 | — |
| SRC-2818 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Elsevier の TDM ライセンスのみで、Europe PMC でも非OA | 60 | — |
| SRC-2819 | UNKNOWN | RESTRICTED | Crossref にライセンス情報がなく、Europe PMC でも非OA。NEJM の購読論文で CC 表示はない | 60 | — |
| SRC-2821 | UNKNOWN | RESTRICTED | Crossref の VoR ライセンスは Wiley の利用条件のみで、Europe PMC でも非OA・購読扱い。CC 表示はない | 60 | — |
| SRC-2824 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Elsevier の TDM ライセンスと著者原稿の Elsevier OA ユーザーライセンスのみ（いずれも CC ではない）で、Europe PMC でも非OA。刊行版には「© 2025 Japanese Society of Otorhinolaryngology-Head… | 60 | — |
| SRC-2826 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Elsevier の TDM ライセンスのみで、Europe PMC でも非OA | 60 | — |
| SRC-2829 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Elsevier の TDM ライセンスのみで、Europe PMC でも非OA | 60 | — |
| SRC-2904 | UNKNOWN | RESTRICTED | Europe PMC で非OA・ライセンス表示なし。The Journal of Rheumatology の購読論文で CC 表示はない | 61 | — |
| SRC-2906 | UNKNOWN | RESTRICTED | Crossref の VoR ライセンスは Wiley の利用条件のみ。PMC に著者原稿（PMC6827566）はあるがライセンス表示がなく、自由利用の対象ではない | 61 | — |
| SRC-2907 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Elsevier の TDM ライセンスと著者原稿用の Elsevier OA ユーザーライセンスのみで、いずれも CC ではない。Europe PMC でも非OA | 61 | — |
| SRC-2908 | UNKNOWN | RESTRICTED | Crossref にライセンス情報がなく、Europe PMC でも非OA。NEJM の購読論文で CC 表示はない | 61 | — |
| SRC-2909 | UNKNOWN | RESTRICTED | Crossref のライセンスは Elsevier の TDM 用ライセンス等のみで、Europe PMC でも非OA。CC 表示はない | 61 | — |
| SRC-2910 | UNKNOWN | RESTRICTED | Crossref にライセンス情報がなく、Europe PMC でも非OA。CC 表示はない | 61 | — |
| SRC-2911 | UNKNOWN | RESTRICTED | Crossref のライセンスは Elsevier の TDM 用ライセンスのみで、Europe PMC でも非OA。CC 表示はない | 61 | — |
| SRC-2913 | UNKNOWN | RESTRICTED | Crossref の VoR ライセンスは Wiley の利用条件のみで、Europe PMC でも非OA。CC 表示はない | 61 | — |
| SRC-2916 | UNKNOWN | RESTRICTED | Europe PMC で非OA・ライセンス表示なし。The Journal of Rheumatology の購読論文で CC 表示はない | 61 | — |
| SRC-291 | UNKNOWN | RESTRICTED | Crossref の VoR ライセンスは Springer Nature の TDM 条件のみで CC 表示はなく、Europe PMC でも非OA（isOpenAccess=N、ライセンス表示なし）。Hypertens Res. 2025;48(10):2500-2511 の購読論文。マスターの license_n… | 62 | — |
| SRC-295 | UNKNOWN | RESTRICTED | Europe PMC の個別レコードでライセンスは CC BY-NC（cc by-nc）。J Bras Pneumol. 2017;43(5):373-379 は SciELO の CC BY-NC 刊行で自由区分（CC BY）には当たらず、Crossref にも CC BY の表示はない。マスターの license_… | 62 | — |
| SRC-1799 | UNKNOWN | RESTRICTED | Crossref の VoR ライセンスは Elsevier の OA ユーザーライセンス（open-access/userlicense/1.0）で CC ではなく、Europe PMC でも非OA・PMCID なし。機関リポジトリに CC BY 表記の著者稿記録があるが、刊行版に CC 表示はないため刊行版を優先し… | 63 | — |
| SRC-2991 | UNKNOWN | RESTRICTED | Crossref の VoR ライセンスは Elsevier の TDM ライセンスのみで CC 表示はなく、Europe PMC でも非OA（isOpenAccess=N、ライセンス表示なし）。Lancet. 2017;390(10089):73-84 の購読論文 | 63 | — |
| SRC-2992 | UNKNOWN | RESTRICTED | Crossref のライセンスは Elsevier の TDM と STM ポリシーのみで CC 表示はなく、Europe PMC でも非OA。Ann Rheum Dis. 2011;70(1):25-31 の購読論文 | 63 | — |
| SRC-2993 | UNKNOWN | RESTRICTED | Crossref の VoR ライセンスは Wiley の利用条件（termsAndConditions#vor）のみで CC 表示はなく、Europe PMC でも非OA。Arthritis Rheum. 2006;54(8):2665-2673 の購読論文 | 63 | — |
| SRC-2994 | UNKNOWN | RESTRICTED | Europe PMC の個別レコードでライセンスは CC BY-NC（cc by-nc、PMC11103320）。自由区分（CC BY）には当たらない。カード記載の「BMJ の OA ユーザーライセンス表示のみ」は CC BY-NC と特定できた | 63 | — |
| SRC-2995 | UNKNOWN | RESTRICTED | Crossref の VoR は OUP の標準刊行モデル（standard_publication_model）で CC ではなく、Europe PMC でも非OA。Mod Rheumatol. 2022;32(4):665-674 の購読論文 | 63 | — |
| SRC-2998 | UNKNOWN | RESTRICTED | Crossref の VoR ライセンスは ERS の user licence（CC ではない）で、Europe PMC でも非OA。カード記載の「ERS の user licence（CC ではない）」と一致する | 63 | — |
| SRC-2999 | UNKNOWN | RESTRICTED | Crossref のライセンスは Elsevier の TDM のみで CC 表示はなく、Europe PMC でも非OA。Semin Arthritis Rheum. 2016;46(3):319-329 の購読論文 | 63 | — |
| SRC-3000 | UNKNOWN | RESTRICTED | Crossref に CC 表示はなく（Elsevier の TDM のみ）、Europe PMC でも非OA。ARD のサイトで無料公開されているがライセンス表示はなく、自由区分には当たらない | 63 | — |
| SRC-3001 | UNKNOWN | RESTRICTED | Crossref のライセンスは Elsevier の TDM のみで CC 表示はなく、Europe PMC でも非OA。Best Pract Res Clin Rheumatol. 2023;37(1):101867 の購読論文 | 63 | — |
| SRC-3002 | UNKNOWN | RESTRICTED | Crossref にライセンス表示はなく（Informa UK / Taylor & Francis）、Europe PMC でも非OA。Amyloid. 2022;29(4):213-219 の購読論文 | 63 | — |
| SRC-3004 | UNKNOWN | RESTRICTED | Crossref にライセンス表示はなく（Wolters Kluwer / AHA）、Europe PMC でも非OA。Circulation. 2015;131(20):1806-1818 の購読論文 | 63 | — |
| SRC-979 | UNKNOWN | RESTRICTED | Crossref のライセンスは Elsevier の TDM のみで CC 表示はなく、Europe PMC でも非OA。マスターの license_note「ライセンス表示を確認できず」は購読論文と確定した | 63 | — |
| SRC-487 | UNKNOWN | RESTRICTED | Europe PMC の個別レコードで非 OA・PMC 未収載・ライセンス表示なし。PMID 7442324 はマスターと一致し、DOI はレコードに存在しない。自由区分の根拠はないため RESTRICTED への訂正を提案する | 65 | — |
| SRC-4895 | UNKNOWN | RESTRICTED | Crossref と Europe PMC のいずれも CC BY-NC 4.0 と記録する。マスターのライセンス備考のとおり刊行版の誌面・PDF では CC 表示を確認できず（© The Author(s) 2020、再利用は出版社の許可手続きによる旨の表示）、どちらの読みでも自由区分にはならない。あわせて PMID… | 65 | — |
| SRC-491 | UNKNOWN | RESTRICTED | Crossref の版ライセンスは null（出版者 Ovid／Wolters Kluwer）、Europe PMC の個別レコードでも非 OA でライセンス表示なし。あわせて PMID 28030502 と DOI 10.1097/TA.0000000000001350 の補完候補がある（識別子補完候補の節参照） | 65 | — |
| SRC-498 | UNKNOWN | RESTRICTED | Crossref のライセンスは Elsevier のテキスト・データマイニング用のみで、自由ライセンスではない。PMID 2499228 と DOI 10.1016/s0196-0644(89)80515-3 はマスターと一致する | 65 | — |
| SRC-567 | UNKNOWN | RESTRICTED | PMC に全文（PMC5045849）があるが、Europe PMC レコードは isOA=N・ライセンス null、Crossref もライセンスなし、NCBI の収載テキストにも ©2016 Annals of Thoracic and Cardiovascular Surgery の表示のみでライセンス文がない。… | 65 | — |
| SRC-570 | UNKNOWN | RESTRICTED | ライセンスは CC BY-NC-ND 4.0 と特定した（Europe PMC レコードと Crossref の版データが一致）。自由区分ではないため RESTRICTED への訂正を提案する。あわせて PMID 30509855 と DOI 10.1016/j.pulmoe.2018.10.008 の補完候補がある | 65 | — |
| SRC-1618 | RESTRICTED | OPEN | Crossref の版（VoR）ライセンスが CC BY 4.0、Europe PMC の個別レコードも isOA=Y・ライセンス cc by、PMC 全文（PMC10113344）にも CC BY 4.0 のライセンス文があり、三者が一致する。刊行版は CC BY であり、マスターの RESTRICTED は誤りのた… | 66 | — |
| SRC-874 | UNKNOWN | RESTRICTED | Crossref の版ライセンスは Springer Nature のテキスト・データマイニング用のみで、マスターのライセンス備考（TDM のみ）とも一致する。Europe PMC の個別レコードでも非 OA・PMC 未収載でライセンス表示なし。自由区分の根拠はないため RESTRICTED への訂正を提案する | 66 | — |
| SRC-877 | UNKNOWN | RESTRICTED | JAMA（American Medical Association）。Crossref にライセンス表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載。自由区分の根拠はないため RESTRICTED への訂正を提案する | 66 | — |
| SRC-884 | UNKNOWN | RESTRICTED | Wiley。Crossref の版ライセンスは Wiley の刊行版利用条件への参照のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載。自由区分の根拠はないため RESTRICTED への訂正を提案する | 66 | — |
| SRC-2946 | UNKNOWN | RESTRICTED | BMJ（Annals of the Rheumatic Diseases）。Crossref の版ライセンスはテキスト・データマイニング用リンクと Elsevier のオープンアクセス利用ライセンス（CC ではない）への参照のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載。マス… | 67 | — |
| SRC-2948 | UNKNOWN | RESTRICTED | BMJ（Annals of the Rheumatic Diseases）。Crossref の版ライセンスは TDM リンクと非 CC の利用ライセンスへの参照のみで、Europe PMC の個別レコードでも非 OA・PMC 未収載。マスターのライセンス備考とも一致する。自由区分の根拠はないため RESTRICTED… | 67 | — |
| SRC-2951 | UNKNOWN | RESTRICTED | 刊行版のライセンスは CC BY-NC 2.0 であることを、Europe PMC の個別レコードのライセンス欄と PMC 全文（PMC3298664）のライセンス文で確認した。CC BY ではないため自由区分には当たらない。マスターのライセンス備考（Crossref は TDM リンクのみ）は刊行版の実際のライセンス… | 67 | — |
| SRC-2953 | UNKNOWN | RESTRICTED | BMJ（Annals of the Rheumatic Diseases）。Crossref の版ライセンスは TDM リンクと非 CC の利用ライセンスへの参照のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載。自由区分の根拠はないため RESTRICTED への訂正を提案する | 67 | — |
| SRC-2954 | UNKNOWN | RESTRICTED | Wiley（Arthritis & Rheumatology）。Crossref の版ライセンスは Wiley の刊行版利用条件への参照のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA。PMC 収載分（PMC12323812）は著者稿でライセンス表示はない。自由区分の根拠はないため RESTR… | 67 | — |
| SRC-2955 | UNKNOWN | RESTRICTED | Wiley（Arthritis & Rheumatism）。Crossref の版ライセンスは Wiley の刊行版利用条件への参照のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載。自由区分の根拠はないため RESTRICTED への訂正を提案する | 67 | — |
| SRC-420 | UNKNOWN | RESTRICTED | Wiley（Arthritis & Rheumatology）。Crossref の版ライセンスは Wiley の刊行版利用条件への参照のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載。自由区分の根拠はないため RESTRICTED への訂正を提案する | 67 | — |
| SRC-421 | UNKNOWN | RESTRICTED | Wiley（Arthritis & Rheumatology）。Crossref の版ライセンスは Wiley の刊行版利用条件への参照のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載。自由区分の根拠はないため RESTRICTED への訂正を提案する | 67 | — |
| SRC-597 | UNKNOWN | RESTRICTED | Lippincott Williams & Wilkins（Medicine）。Crossref のレコードにライセンス欄はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載。マスターのライセンス備考（表示を確認できず）と一致する。自由区分の根拠はないため RESTRICTED への訂正を提案する | 67 | — |
| SRC-3836 | UNKNOWN | RESTRICTED | Elsevier（Pediatric Neurology）。Crossref の版ライセンスは Elsevier のテキスト・データマイニング用ライセンスのみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。カード側の uncertainty に記録されていた「Crossre… | 68 | — |
| SRC-3081 | UNKNOWN | RESTRICTED | Springer Nature（Nature Reviews Disease Primers）。Crossref の版ライセンスは Springer Nature のテキスト・データマイニング案内のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため … | 69 | — |
| SRC-3084 | UNKNOWN | RESTRICTED | Elsevier（The Journal of Allergy and Clinical Immunology: In Practice）。Crossref の版ライセンスは Elsevier のテキスト・データマイニング用ライセンスのみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未… | 69 | — |
| SRC-3085 | UNKNOWN | RESTRICTED | Wiley（British Journal of Haematology）。Crossref の版ライセンスは Wiley の利用条件へのリンクのみで CC 表示はなく、Europe PMC の個別レコードでも非 OA（PMC 収載分 PMC7612067 は著者稿でライセンス表示なし）である。自由区分の根拠はないため… | 69 | — |
| SRC-3087 | UNKNOWN | RESTRICTED | Springer Nature（Nature Reviews Disease Primers）。Crossref の版ライセンスはテキスト・データマイニング案内のみで CC 表示はなく、PMC 収載分（PMC4900471）は著者稿でライセンス表示がなく Europe PMC で非 OA である。自由区分の根拠はないた… | 69 | — |
| SRC-3095 | UNKNOWN | RESTRICTED | Ferrata Storti Foundation（Haematologica）。Crossref にライセンス登録がなく、Europe PMC の個別レコードでも非 OA で、PMC 全文には © Ferrata Storti Foundation の表示のみで CC 表示はない。同誌の現行の OA ライセンスは C… | 69 | — |
| SRC-2731 | UNKNOWN | RESTRICTED | Thieme（Thrombosis and Haemostasis）。Crossref にライセンス登録がなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため RESTRICTED への訂正を提案する | 70 | — |
| SRC-2732 | UNKNOWN | RESTRICTED | Elsevier（Blood Reviews）。Crossref の版ライセンスは Elsevier のテキスト・データマイニング用ライセンスのみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため RESTRICTED への訂正を提案する | 70 | — |
| SRC-2733 | UNKNOWN | RESTRICTED | 日本小児科学会の学会文書。学会サイトで無償公開されているが CC 表示はなく、政府の文書（GOV_JP）にも当たらない。自由区分の根拠はないため RESTRICTED への訂正を提案する | 70 | — |
| SRC-2735 | UNKNOWN | RESTRICTED | Elsevier（The Lancet）。Crossref の版ライセンスは Elsevier の TDM ライセンスとポリシーのみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため RESTRICTED への訂正を提案する | 70 | — |
| SRC-2738 | UNKNOWN | RESTRICTED | Wiley（British Journal of Haematology）。Crossref の版ライセンスは Wiley の利用条件へのリンクのみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため RESTRICTED への訂正を提案する | 70 | — |
| SRC-2739 | UNKNOWN | RESTRICTED | American Society of Hematology（Blood）。Crossref にライセンス登録がなく、Europe PMC の個別レコードでも非 OA・PMC 未収載（同誌の他論文にみられる著者稿の PMC 収載も本論文にはない）である。自由区分の根拠はないため RESTRICTED への訂正を提案する | 70 | — |
| SRC-2740 | UNKNOWN | RESTRICTED | Elsevier（The Lancet Haematology）。Crossref の版ライセンスは Elsevier の TDM ライセンス等のみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため RESTRICTED への訂正を提案する | 70 | — |
| SRC-2741 | UNKNOWN | RESTRICTED | Wiley（British Journal of Haematology）。Crossref の版ライセンスは Wiley の利用条件へのリンクのみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため RESTRICTED への訂正を提案する | 70 | — |
| SRC-2742 | UNKNOWN | RESTRICTED | 書籍（金原出版）。CC 表示はなく、DOI・PMID も存在しない。自由区分の根拠はないため RESTRICTED への訂正を提案する | 70 | — |
| SRC-2743 | UNKNOWN | RESTRICTED | ASCO（Journal of Clinical Oncology）。Crossref にライセンス登録がなく、PMC 収載分（PMC4979194）は著者稿でライセンス表示がなく Europe PMC で非 OA である。自由区分の根拠はないため RESTRICTED への訂正を提案する | 70 | — |
| SRC-501 | UNKNOWN | RESTRICTED | European Respiratory Society（Eur Respir J）。Crossref の版ライセンスは ERS の user licence へのリンクのみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため RESTRICTED への… | 71 | — |
| SRC-502 | UNKNOWN | RESTRICTED | American Thoracic Society（Am J Respir Crit Care Med）。Crossref の版ライセンスは版元（OUP）の標準再利用条件へのリンクのみで CC 表示はない。PMC 収載分（PMC4408724）は著者稿でライセンス表示がなく、Europe PMC でも非 OA である。… | 71 | — |
| SRC-504 | UNKNOWN | OPEN | BioMed Central（Respiratory Research）。Europe PMC の個別レコードでライセンス「cc by」・OA 区分を確認し、PMC 全文（PMC3655828）のライセンス文（Creative Commons Attribution License）でも CC BY を確認した。主出典… | 71 | — |
| SRC-505 | UNKNOWN | RESTRICTED | BMJ（Thorax）。本体（O'Driscoll ら 2017、DOI 10.1136/thoraxjnl-2016-209729）は Crossref にライセンス登録がなく、Europe PMC の個別レコードでも非 OA・PMC 未収載で、出版社のページにも CC 表示はなく再利用は RightsLink 経由… | 71 | — |
| SRC-1742 | UNKNOWN | RESTRICTED | Neurology（American Academy of Neurology）。Crossref にライセンス登録がなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため RESTRICTED への訂正を提案する | 73 | — |
| SRC-1745 | UNKNOWN | RESTRICTED | Cochrane Database of Systematic Reviews（Wiley）。PMC 収載分（PMC6464149）の本文に「Copyright © 2016 The Cochrane Collaboration」の表示があり CC 表示はなく、Europe PMC でも非 OA、Crossref にラ… | 73 | — |
| SRC-1746 | UNKNOWN | RESTRICTED | European Journal of Neurology（Wiley）。Crossref の版ライセンスは Wiley の利用条件へのリンクのみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため RESTRICTED への訂正を提案する | 73 | — |
| SRC-1749 | UNKNOWN | RESTRICTED | Journal of the Peripheral Nervous System（Wiley）。Crossref の版ライセンスは Wiley の利用条件へのリンクのみで CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載である。自由区分の根拠はないため RESTRICTED への訂正を… | 73 | — |
| SRC-1754 | UNKNOWN | RESTRICTED | Journal of the American Academy of Orthopaedic Surgeons。PMC 収載分（PMC11928260）のライセンス表示はテキストマイニング・フェアユースの注記のみで CC 表示はなく、Europe PMC でも非 OA、Crossref にライセンス登録はない。自由区分… | 73 | — |
| SRC-1755 | UNKNOWN | RESTRICTED | Current Reviews in Musculoskeletal Medicine（Springer）。PMC 収載分（PMC4896870）の本文に「© Springer Science+Business Media New York 2016」の表示があり CC 表示はなく、Europe PMC でも非 OA、… | 73 | — |
| SRC-3343 | UNKNOWN | RESTRICTED | Hayashi M, et al. J Nippon Med Sch. 2012;79(1):60-68（FT-003 の主出典）。Crossref にライセンス登録がなく、Europe PMC の個別レコードで非 OA・PMC 未収載。掲載誌は J-STAGE で無償閲覧できるが著作権は日本医科大学医学会にあり CC… | 75 | — |
| SRC-3351 | UNKNOWN | OPEN | Moise KJ Jr, et al. JAMA Netw Open. 2025;8(11):e2544649（FT-011 の主出典）。同誌は全面オープンアクセスで、DOI の個別照会で Unpaywall と OpenAlex のいずれもが出版社の刊行版（publishedVersion）のライセンスを CC BY… | 75 | — |
| SRC-1026 | UNKNOWN | RESTRICTED | Horm Res Paediatr（Karger）。本バッチで個別に再確認した：Crossref の版データのライセンスは Karger のサイトライセンスへのリンクのみ（vor・tdm とも）で CC 表示はなく、Europe PMC の個別レコードでも非 OA・PMC 未収載。マスターの license_note（… | 77 | 98 |
| SRC-1027 | UNKNOWN | RESTRICTED | Horm Res Paediatr（Karger）。本バッチで個別に再確認した：Crossref の版（version of record）データと Europe PMC の個別レコードの双方で刊行版ライセンスは CC BY-NC-ND 4.0 で、自由区分には当たらない。PMC 収載コピー（PMC6979443）の著… | 77 | 98 |
| SRC-1030 | UNKNOWN | RESTRICTED | バッチ77（IE-005・IE-006 と主出典を共有）で提案済みの再掲。二重計上しないこと。J Clin Endocrinol Metab（Endocrine Society）。Crossref にライセンス登録なし。PMC 収載分（PMC6456929）は非OAでライセンス表示なし | 77 | 87 |
| SRC-1031 | UNKNOWN | RESTRICTED | Lancet Diabetes Endocrinol（Elsevier）。Crossref は TDM ライセンスのみ、Europe PMC の個別レコードで非 OA | 77 | — |
| SRC-1032 | UNKNOWN | RESTRICTED | J Pediatr Gastroenterol Nutr（Wiley）。Crossref は Wiley の利用条件へのリンクのみ、Europe PMC の個別レコードで非 OA | 77 | — |
| SRC-1034 | UNKNOWN | RESTRICTED | World J Gastroenterol（Baishideng）。Crossref にライセンス登録なし。PMC ページ自体（PMC4146814）に「©2007 Baishideng Publishing Group Inc. All rights reserved」とあり CC 表示なし | 77 | — |
| SRC-1036 | UNKNOWN | RESTRICTED | Nat Rev Dis Primers（Nature Portfolio）。Crossref は TDM リンクのみ、Europe PMC の個別レコードで非 OA | 77 | — |
| SRC-1037 | UNKNOWN | RESTRICTED | Rheumatology (Oxford)（Oxford University Press）。Crossref にライセンス登録なし、Europe PMC の個別レコードで非 OA | 77 | — |
| SRC-1039 | UNKNOWN | RESTRICTED | J Inherit Metab Dis（Wiley／SSIEM）。Crossref は Wiley の利用条件へのリンクのみ、Europe PMC の個別レコードで非 OA。同誌のガイドラインには CC BY で刊行されたものもあるが、本論文は異なる | 77 | — |
| SRC-4970 | UNKNOWN | RESTRICTED | J Pediatr Gastroenterol Nutr（Wiley）。Crossref は Wiley の利用条件へのリンクのみ、Europe PMC の個別レコードで非 OA、PMCID なし。カード（IE-018）側の uncertainty にあった「オープンアクセスの表記があるが CC の種別を確認できない」… | 77 | — |
| SRC-2481 | UNKNOWN | RESTRICTED | Ann Ib Postgrad Med（Association of Resident Doctors, UCH, Ibadan）。PMC 全文（PMC4415389）のライセンス要素に「© Association of Resident Doctors, UCH, Ibadan 2014」の表示と CC BY-NC … | 79 | — |
| SRC-1190 | UNKNOWN | RESTRICTED | PMCに収載される（PMCID PMC3194828）が非OAでライセンス表示はない（ASM誌） | 80 | — |
| SRC-2156 | UNKNOWN | RESTRICTED | Crossrefにライセンス欄がなく、Europe PMCでも非OA。J-STAGEで無償閲覧できる学会誌だがCC表示はない | 80 | — |
| SRC-2157 | UNKNOWN | RESTRICTED | CrossrefはTDMリンクのみでCCライセンスは付されていない | 80 | — |
| SRC-2161 | UNKNOWN | RESTRICTED | PMCに収載される（PMCID PMC3255962）が非OAでライセンス表示はない（ASM誌） | 80 | — |
| SRC-1011 | UNKNOWN | RESTRICTED | Crossref にはテキストマイニング用リンクのみでライセンス表示がなく、Europe PMC でも非OA | 82 | — |
| SRC-1012 | UNKNOWN | RESTRICTED | ライセンス表示がなく非OA | 82 | — |
| SRC-1015 | UNKNOWN | RESTRICTED | Crossref はテキストマイニング用リンクのみ、Europe PMC でも非OA | 82 | — |
| SRC-1019 | UNKNOWN | RESTRICTED | J-STAGE で無償閲覧できるが、誌面・J-STAGE のいずれにもライセンス表示がない。無償閲覧可でも CC 表示がなければ自由とはみなさない | 82 | — |
| SRC-1021 | UNKNOWN | RESTRICTED | StatPearls 書籍（Bookshelf NBK519539 に対応）は書籍単位で CC BY-NC-ND 4.0。マスターの license_note「ライセンス表示を確認できず」は実態と異なるため注記の更新も提案 | 82 | — |
| SRC-1022 | UNKNOWN | RESTRICTED | StatPearls 書籍（Bookshelf NBK535345 に対応）は書籍単位で CC BY-NC-ND 4.0。license_note の更新も提案 | 82 | — |
| SRC-1023 | UNKNOWN | RESTRICTED | StatPearls 書籍（Bookshelf NBK551609 に対応）は書籍単位で CC BY-NC-ND 4.0。license_note の更新も提案 | 82 | — |
| SRC-1024 | UNKNOWN | RESTRICTED | PMC に収載される（PMC2276281）がライセンス表示がなく、Europe PMC でも非OA扱いで自由ではない | 82 | — |
| SRC-1521 | UNKNOWN | RESTRICTED | Crossref はテキストマイニング用リンクのみ、非OA | 82 | — |
| SRC-1523 | UNKNOWN | RESTRICTED | Elsevier 誌で STM・テキストマイニング用リンクのみ、ライセンス表示なし | 82 | — |
| SRC-4116 | UNKNOWN | RESTRICTED | 学会発行の単行ガイドラインで DOI・PMID はなく、CC 表示もない。無償で読める全文は確認できなかった | 83 | — |
| SRC-4122 | UNKNOWN | RESTRICTED | Crossref にライセンス表示がなく、Europe PMC でも非OA（購読誌） | 83 | — |
| SRC-4125 | UNKNOWN | RESTRICTED | Crossref のライセンスはテキストマイニング用のみで、Europe PMC でも非OA | 83 | — |
| SRC-4126 | UNKNOWN | RESTRICTED | PMC に収載される（PMC3863169）が、PMC 版の著作権表示は All rights reserved で CC 表示がなく、Crossref の刊行版ライセンスは Elsevier の OA ユーザーライセンス（CC ではない） | 83 | — |
| SRC-4127 | UNKNOWN | RESTRICTED | Europe PMC で非OA。BioOne に無償PDFがあるが CC 表示はない | 83 | — |
| SRC-4128 | UNKNOWN | RESTRICTED | 指針本文の著作権表示は「© 2013 Health Physics Society、無断複写は禁止」で、Crossref にもライセンス表示がない | 83 | — |
| SRC-1047 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは NEJM の利用規約のみで CC 表示はなく、Europe PMC でも非OA | 84 | — |
| SRC-1048 | UNKNOWN | RESTRICTED | © 2021 American Academy of Family Physicians で非OA。DOI は付与されていない（Europe PMC の個別照会でも DOI なし） | 84 | — |
| SRC-1049 | UNKNOWN | RESTRICTED | 刊行版は CC BY-NC-ND 4.0（Crossref の刊行版データと PMC 全文のライセンス表示で確認）。自由ではない。あわせてマスターの license_note「ライセンス表示を確認できず」は実態と異なるため注記の更新を提案 | 84 | — |
| SRC-1054 | UNKNOWN | RESTRICTED | Crossref のライセンスは Elsevier のテキストマイニング用のみで、Europe PMC でも非OA | 84 | — |
| SRC-1057 | UNKNOWN | RESTRICTED | Crossref のライセンスは Elsevier のテキストマイニング用のみで、Europe PMC でも非OA | 84 | — |
| SRC-1058 | UNKNOWN | RESTRICTED | 刊行版は CC BY-NC-ND 4.0（Crossref の刊行版データ・Europe PMC・Unpaywall で確認）。自由ではない。あわせてマスターの license_note「ライセンス表示を確認できず」は実態と異なるため注記の更新を提案 | 84 | — |
| SRC-1200 | UNKNOWN | RESTRICTED | Europe PMC で非OA・全文収載なし。Crossref にライセンス登録はなく、著作権は © American Academy of Family Physicians。マスターの license_note（CC表示なし）と一致する | 86 | — |
| SRC-1201 | UNKNOWN | RESTRICTED | PMC 全文（PMC6516870）の著作権表示は「Copyright © 2018 The Cochrane Collaboration. Published by John Wiley & Sons, Ltd.」で CC ライセンス要素はない。Crossref にもライセンス登録はない。マスターの license_… | 86 | — |
| SRC-1203 | UNKNOWN | RESTRICTED | PMC 全文（PMC1496896）の著作権表示は「1998 by the Society of General Internal Medicine」で CC 表示はない。Crossref にライセンス登録はない。マスターの license_note と一致する | 86 | — |
| SRC-1204 | UNKNOWN | RESTRICTED | PMC 全文（PMC3994805）の著作権表示は「Copyright © the College of Family Physicians of Canada」で CC 表示はない。DOI は付与されていない。マスターの license_note と一致する | 86 | — |
| SRC-1205 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは Wiley の利用条件（content-version: vor）とテキストマイニング用ライセンスのみで CC ではない。Europe PMC でも非OA。マスターの license_note と一致する | 86 | — |
| SRC-1206 | UNKNOWN | RESTRICTED | Crossref のライセンスは Elsevier のテキストマイニング用ライセンスのみで CC ではない。Europe PMC でも非OA。マスターの license_note と一致する | 86 | — |
| SRC-1208 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは利用条件のみで CC ではない。Europe PMC でも非OA。マスターの license_note（© American Academy of Otolaryngology-Head and Neck Surgery Foundation、CC表示なし）と一致する | 86 | — |
| SRC-1209 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは利用条件のみで CC ではない。Europe PMC でも非OA。マスターの license_note と一致する | 86 | — |
| SRC-1210 | UNKNOWN | RESTRICTED | Crossref の刊行版ライセンスは利用条件のみで CC ではない。Europe PMC でも非OA。マスターの license_note と一致する | 86 | — |
| SRC-3522 | UNKNOWN | RESTRICTED | Nat Rev Dis Primers（Springer Nature）。Crossref の刊行版ライセンスはテキストマイニング用リンクのみで CC ではない。PMC 収載分（PMC8428796）は著者稿で非OA、ライセンス表示なし。マスターの license_note は null で、実態は CC 表示なし | 87 | — |
| SRC-3525 | UNKNOWN | RESTRICTED | Am J Med Genet C（Wiley）。Crossref の刊行版ライセンスは Wiley の利用条件（termsAndConditions#vor）のみで CC ではない。Europe PMC でも非OA・全文収載なし。マスターの license_note は null で、カード側の「表示なし」と実態は一致… | 87 | — |
| SRC-3538 | RESTRICTED | OPEN | BJOG（Wiley）に掲載された WHO 声明。Crossref の刊行版（version of record）ライセンスは CC BY 3.0 IGO（https://creativecommons.org/licenses/by/3.0/igo/legalcode）。Europe PMC の個別レコードでも is… | 88 | — |
| SRC-4038 | UNKNOWN | RESTRICTED | Lancet（Elsevier）。Crossref の刊行版ライセンスはテキストマイニング用ライセンス（Elsevier TDM）と STM ポリシーのみで CC ではない。PMC 収載コピー（PMC2493390）は著者稿で、そのライセンス要素は Elsevier の著者稿再配布条件への言及にとどまり、著作権表示は … | 91 | — |
| SRC-4039 | UNKNOWN | RESTRICTED | Br J Clin Pharmacol（Wiley）。Crossref の刊行版ライセンスは Wiley の利用条件（termsAndConditions#vor）のみで CC ではない。Europe PMC の個別レコードで非 OA（isOpenAccess: N）・ライセンス表示なし。PMC 収載コピー（PMC32… | 91 | — |
| SRC-4048 | UNKNOWN | OPEN | J Occup Health（Oxford University Press／日本産業衛生学会）。Crossref の刊行版（version of record）ライセンスに CC BY 4.0（2025-05-20 開始）が登録され、Europe PMC の個別レコードでも license: cc by、PMC 全文… | 91 | — |
| SRC-4050 | UNKNOWN | RESTRICTED | Curr Dermatol Rep（Springer）。Crossref の刊行版ライセンスはテキストマイニング用ライセンスのみで CC ではない。PMC 収載コピー（PMC8439371）のライセンス要素は、WHO の宣言期間に限って再利用を認める期間限定の許可であり CC ではなく、著作権表示は © The Aut… | 91 | — |
| SRC-1684 | UNKNOWN | RESTRICTED | Eur J Neurol（Wiley）。Crossref の刊行版（version of record）ライセンスは Wiley の利用条件（termsAndConditions#vor）のみで CC ではない。Europe PMC の個別レコードでも非 OA（isOpenAccess: N）・ライセンス表示なし、PM… | 92 | — |
| SRC-4031 | UNKNOWN | RESTRICTED | GHM Open（国立国際医療研究センター）。Crossref にライセンス登録がなく、Europe PMC の個別レコードでもライセンス表示なし・非 OA。PMC 収載コピー（PMC11933966）の権限表示は「© 2021, National Center for Global Health and Medici… | 93 | — |
| SRC-4801 | UNKNOWN | RESTRICTED | Cochrane Database of Systematic Reviews（Wiley）。Crossref にライセンス登録がなく、Europe PMC の個別レコードでも非 OA・ライセンス表示なし。PMC 収載コピー（PMC13097252）の権限表示は「Copyright © 2026 The Cochran… | 93 | — |
| SRC-4140 | UNKNOWN | RESTRICTED | Zellner et al., Dtsch Arztebl Int 2019（Deutscher Ärzte-Verlag）。Europe PMC の個別レコードでは非 OA でライセンス表示がなく、PMC 収載コピー（PMC6620762）のフロントマターにもライセンス要素・permissions の記載がない（出版… | 99 | — |

### 1-2. 区分の明確化申し送り（35件）

UNKNOWN のままでは実態と異なるが、各バッチが「自由区分への訂正ではない」として D に数えなかったもの。いずれも訂正後の区分は RESTRICTED。

| SRC | 根拠（個別確認結果） | バッチ |
|---|---|---|
| SRC-424 | CC BY-NC を Europe PMC で確認（過敏性肺炎GL、IL-023〜025 の主出典） | 2 |
| SRC-426 | CC BY-NC を確認（ISHAM-ABPA、IL-027〜029 の主出典） | 2 |
| SRC-1943 | ©ASIA・All rights reserved を PMC 全文で確認（ISNCSCI 2019） | 8 |
| SRC-1957 | ©BMJ・商用再利用不可（PEACE & LOVE） | 8 |
| SRC-096 | CC BY-NC-ND（IPMN 京都ガイドライン 2024、Europe PMC で確認） | 12 |
| SRC-1262 | CC BY-NC-ND 4.0（IC3D 角膜ジストロフィ分類 第3版。Crossref・Europe PMC の両方で確認） | 13 |
| SRC-1697 | CC BY-NC-ND 4.0（NMOSD 国際診断基準、Europe PMC で確認） | 14 |
| SRC-1880 | CC BY-NC（Fukushima 2010、Europe PMC で確認） | 17 |
| SRC-3174 | Crossref の version-of-record が Wiley の利用条件で CC ではない（RCOG Green-top Guideline No. 27a 第5版） | 18 |
| SRC-3257 | CC BY-NC-ND（EULAR 妊娠・授乳の抗リウマチ薬推奨 2024年改訂。Crossref・Europe PMC で確認） | 18 |
| SRC-1341 | CC BY-NC 4.0（Crossref・Europe PMC の両方で確認） | 19 |
| SRC-1352 | CC BY-NC-ND 4.0（Crossref・Europe PMC の両方で確認） | 19 |
| SRC-1441 | CC BY-NC-ND 4.0（Anales de Pediatría。Crossref・Europe PMC の双方で確認） | 22 |
| SRC-953 | CC BY-NC-ND 4.0（FITTER 勧告。Crossref・Europe PMC の双方で確認） | 23 |
| SRC-957 | CC BY-NC-ND 4.0（メトホルミン関連乳酸アシドーシスの総説。同上） | 23 |
| SRC-945 | SRC-965 と同一文献の二重登録で、SRC-965 は RESTRICTED。統一に伴い RESTRICTED への明確化が適切 | 23 |
| SRC-290 | 同誌の他記事が CC BY-NC-ND 4.0 で本ガイドラインも同条件の可能性が高いが、一次表示で確定できなかった（確定できれば RESTRICTED への明確化が適切、という条件付きの申し送り） | 24 |
| SRC-4523 | Crossref の version-of-record が Elsevier の open-access userlicense 1.0 で、オープンアクセスだが CC BY ではない（ESVS 2021） | 26 |
| SRC-1083 | PMC に全文があるが、ライセンスは著者から Springer への exclusive licence で CC 表示なし | 26 |
| SRC-023 | CC BY-NC-ND 4.0（IDCases 2020。Crossref・Europe PMC の双方で確定） | 27 |
| SRC-024 | CC BY-NC 4.0（Medicine 2019。同上） | 27 |
| SRC-374 | CC BY-NC-ND 4.0（JGL2021 英語要約。Crossref・Europe PMC の双方で確認） | 29 |
| SRC-384 | CC BY-NC（West J Emerg Med 2013、Europe PMC で確認）。マスターの記録「CC BY のアイコン表示はあるが版の表示なし」は実態と異なる（第5節にも関連） | 29 |
| SRC-4728 | Crossref・Europe PMC・PMC 掲載ページのいずれでも CC ライセンスの表示を確認できず（© S. Karger AG の表示のみ）。「CC 条件は付いていないものとして扱うのが妥当」という申し送り | 31 |
| SRC-988 | Crossref の version-of-record が Wiley の利用条件（CC ではない）で Europe PMC でも非OA（BCSH コバラミン・葉酸ガイドライン 2014） | 36 |
| SRC-253 | OA でなくライセンス表示もない（Templin ら NEJM 2015） | 39 |
| SRC-167 | Crossref・Europe PMC の両経路で CC ライセンスの表示がなく（VoR は Wiley の利用条件のみ）、出版社の著作物であることを確認（ESGE 質指標） | 40 |
| SRC-169 | 同上（Elsevier の TDM 表示のみ。ESPEN 外科栄養） | 40 |
| SRC-979 | Crossref の VoR は Elsevier の TDM ライセンスのみで Europe PMC でも非オープンアクセス（Wechalekar 2016） | 42 |
| SRC-2650 | Crossref・Europe PMC のいずれにもライセンス表示がなく、PMC の本文表示も「© 2018 by The American Society of Hematology」のみ（ASH 2018 HIT ガイドライン） | 43 |
| SRC-449 | ライセンス表示が両経路になく、Annals of Internal Medicine の著作物（HHT 国際ガイドライン第2版） | 43 |
| SRC-1278 | CC BY-NC-SA（Indian J Ophthalmol、Europe PMC で確認） | 44 |
| SRC-3363 | Crossref が Springer の TDM のみで、PMC の著者稿にもライセンス表示がない（J Perinatol 2021） | 45 |
| SRC-3444 | 掲載誌（J Pak Med Assoc）の OA 方針ページは著者が CC BY 4.0 で権利を保持する旨を謳うが、Crossref・Europe PMC のいずれでも論文単位のライセンス表示は確認できず、2016年の論文への適用も確かめられない（方向未確定のまま申し送り） | 45 |
| SRC-352 | CC BY-NC-ND 4.0（成人肺炎診療ガイドライン2024の英語版。Crossref・Europe PMC の双方で確認） | 46 |

### 1-3. 現行区分の確認のみ（訂正なし、4件）

- SRC-234（バッチ48・94）：Crossref は CC BY と表示するが、刊行版自体は CC BY-NC-ND であり、現行 RESTRICTED が正しいことを再確認した（バッチ94は再掲扱い）。Crossref の表示だけで OPEN に反転させないこと。
- SRC-272（バッチ94）：現行 RESTRICTED が正しいことを確認。
- SRC-4141（バッチ99）：CC BY-NC 4.0 のため現行 RESTRICTED が正しい（訂正ではない）。
- SRC-4976（バッチ100）：DSM-5-TR 書籍。現行 RESTRICTED が正しいことを確認。

## 2. 識別子補完候補一覧（789件、679出典）

出典マスターに未登録で、各バッチが個別照会（Europe PMC・Crossref・NCBI 等）で実在とタイトル・著者の一致を確認した補完候補。再掲は初出バッチに統合した。PMCID の補完候補は、登録側の PC での `--online` 照合を経てから登録する保留扱い（従来の運用どおり）。PH-016 の PMID 誤りのような「誤値の訂正」は本節ではなく第3節に置いた。

| SRC | 識別子 | 値 | 初出バッチ | 再掲バッチ |
|---|---|---|---|---|
| SRC-538 | PMCID | PMC5946555 | 2 | — |
| SRC-547 | PMID | 42425779 | 2 | 42 |
| SRC-140 | PMCID | PMC13202739 | 4 | — |
| SRC-140 | PMID | 41713704 | 4 | — |
| SRC-141 | PMID | 42532244 | 4 | — |
| SRC-144 | PMID | 41692277 | 4 | — |
| SRC-145 | PMID | 41713710 | 4 | — |
| SRC-146 | PMID | 42031440 | 4 | — |
| SRC-147 | PMID | 41713709 | 4 | — |
| SRC-149 | PMID | 42031441 | 4 | — |
| SRC-151 | PMCID | PMC13549701 | 4 | — |
| SRC-151 | PMID | 42031436 | 4 | — |
| SRC-152 | PMID | 41713707 | 4 | — |
| SRC-153 | PMID | 42031435 | 4 | — |
| SRC-050 | PMCID | PMC11825134 | 5 | — |
| SRC-057 | PMID | 30625484 | 5 | — |
| SRC-062 | PMID | 34164674 | 5 | — |
| SRC-4968 | PMCID | PMC3342598 | 5 | — |
| SRC-158 | PMCID | PMC5809582 | 6 | — |
| SRC-158 | PMID | 29330835 | 6 | — |
| SRC-160 | PMCID | PMC3680657 | 6 | — |
| SRC-160 | PMID | 23673399 | 6 | — |
| SRC-162 | PMID | 31407109 | 6 | — |
| SRC-4237 | PMID | 29746229 | 6 | — |
| SRC-4238 | PMID | 32209311 | 6 | — |
| SRC-4239 | PMID | 32199769 | 6 | — |
| SRC-4240 | PMID | 34303806 | 6 | — |
| SRC-4241 | PMID | 34016826 | 6 | — |
| SRC-4243 | PMID | 31791596 | 6 | — |
| SRC-4441 | PMCID | PMC9257997 | 6 | — |
| SRC-039 | PMID | 37401795 | 7 | — |
| SRC-043 | PMID | 24764778 | 7 | — |
| SRC-045 | PMID | 38875111 | 7 | — |
| SRC-047 | PMID | 42100946 | 7 | — |
| SRC-4211 | PMID | 18810558 | 7 | — |
| SRC-4212 | PMID | 37383896 | 7 | — |
| SRC-4213 | PMID | 33822331 | 7 | — |
| SRC-4214 | PMID | 31487687 | 7 | — |
| SRC-1925 | PMCID | PMC11402187 | 8 | — |
| SRC-1943 | PMCID | PMC8152171 | 8 | — |
| SRC-1946 | PMCID | PMC5686915 | 8 | — |
| SRC-1952 | PMCID | PMC4464690 | 8 | — |
| SRC-1958 | PMCID | PMC3082940 | 8 | — |
| SRC-1959 | PMCID | PMC4117866 | 8 | — |
| SRC-1965 | PMCID | PMC4071472 | 8 | — |
| SRC-1975 | PMCID | PMC149439 | 8 | — |
| SRC-1979 | PMCID | PMC3553934 | 8 | — |
| SRC-1980 | PMCID | PMC3528023 | 8 | — |
| SRC-1982 | PMCID | PMC3509775 | 8 | — |
| SRC-1985 | PMCID | PMC7017598 | 8 | — |
| SRC-1986 | PMCID | PMC6488749 | 8 | — |
| SRC-1988 | PMCID | PMC2914601 | 8 | — |
| SRC-4810 | PMCID | PMC7462174 | 8 | — |
| SRC-1543 | PMCID | PMC11696709 | 9 | — |
| SRC-811 | PMCID | PMC10952771 | 9 | — |
| SRC-822 | PMCID | PMC7073417 | 9 | — |
| SRC-826 | PMCID | PMC10477934 | 9 | — |
| SRC-832 | PMCID | PMC7203749 | 9 | — |
| SRC-836 | PMCID | PMC7057272 | 9 | — |
| SRC-839 | PMCID | PMC4175743 | 9 | — |
| SRC-841 | PMCID | PMC3638209 | 9 | — |
| SRC-842 | PMCID | PMC4212440 | 9 | — |
| SRC-845 | PMCID | PMC3340903 | 9 | — |
| SRC-846 | PMCID | PMC4890704 | 9 | — |
| SRC-856 | PMCID | PMC9982362 | 9 | — |
| SRC-018 | DOI | 10.1007/s00535-021-01788-x | 10 | 27・92 |
| SRC-066 | PMID | 37364790 | 10 | — |
| SRC-074 | PMCID | PMC3423565 | 10 | — |
| SRC-074 | PMID | 22825549 | 10 | — |
| SRC-084 | PMCID | PMC2773872 | 10 | — |
| SRC-084 | PMID | 19058303 | 10 | — |
| SRC-3974 | PMCID | PMC11040545 | 10 | 78 |
| SRC-3974 | PMID | 38174913 | 10 | 78 |
| SRC-1163 | PMCID | PMC7313440 | 11 | — |
| SRC-1169 | PMCID | PMC5418875 | 11 | — |
| SRC-1170 | PMCID | PMC4966395 | 11 | — |
| SRC-1171 | PMCID | PMC9110571 | 11 | — |
| SRC-1173 | PMCID | PMC13341069 | 11 | — |
| SRC-1178 | PMCID | PMC5025328 | 11 | — |
| SRC-1184 | PMCID | PMC7025440 | 11 | — |
| SRC-1187 | PMCID | PMC6302357 | 11 | — |
| SRC-1188 | PMCID | PMC12707599 | 11 | — |
| SRC-1189 | PMCID | PMC9677953 | 11 | — |
| SRC-1190 | PMCID | PMC3194828 | 11 | 80 |
| SRC-088 | PMCID | PMC9522716 | 12 | — |
| SRC-088 | PMID | 35994093 | 12 | — |
| SRC-089 | PMCID | PMC10066137 | 12 | — |
| SRC-089 | PMID | 36920680 | 12 | — |
| SRC-097 | PMCID | PMC10423145 | 12 | — |
| SRC-097 | PMID | 37452855 | 12 | — |
| SRC-4230 | PMID | 22722902 | 12 | — |
| SRC-4231 | PMCID | PMC9038818 | 12 | — |
| SRC-4231 | PMID | 34918177 | 12 | — |
| SRC-4232 | PMCID | PMC4814619 | 12 | — |
| SRC-4232 | PMID | 26902131 | 12 | — |
| SRC-1252 | PMCID | PMC5143802 | 13 | — |
| SRC-1257 | PMCID | PMC5710829 | 13 | — |
| SRC-1260 | PMCID | PMC8170279 | 13 | — |
| SRC-1262 | PMCID | PMC10906208 | 13 | — |
| SRC-1277 | PMCID | PMC5398733 | 13 | 19 |
| SRC-1301 | PMCID | PMC10701408 | 13 | — |
| SRC-1304 | PMCID | PMC10655158 | 13 | — |
| SRC-1305 | PMCID | PMC5462106 | 13 | — |
| SRC-1307 | PMCID | PMC3702240 | 13 | — |
| SRC-1308 | PMCID | PMC4108143 | 13 | — |
| SRC-1315 | PMCID | PMC9672712 | 13 | — |
| SRC-4373 | PMCID | PMC5784757 | 13 | — |
| SRC-4375 | PMCID | PMC1039895 | 13 | — |
| SRC-1651 | PMCID | PMC11350039 | 14 | — |
| SRC-1655 | PMCID | PMC10352931 | 14 | — |
| SRC-1660 | PMCID | PMC3714437 | 14 | — |
| SRC-1663 | PMCID | PMC3170532 | 14 | — |
| SRC-1664 | PMCID | PMC3059138 | 14 | — |
| SRC-1668 | PMCID | PMC4643396 | 14 | — |
| SRC-1669 | PMCID | PMC3325428 | 14 | — |
| SRC-1671 | PMCID | PMC7905302 | 14 | 56 |
| SRC-1672 | PMCID | PMC5516529 | 14 | — |
| SRC-1673 | PMCID | PMC3590050 | 14 | — |
| SRC-1674 | PMCID | PMC6530552 | 14 | — |
| SRC-1677 | PMCID | PMC3729880 | 14 | — |
| SRC-1679 | PMCID | PMC8106615 | 14 | — |
| SRC-1697 | PMCID | PMC4515040 | 14 | 47 |
| SRC-1698 | PMCID | PMC5363978 | 14 | — |
| SRC-1564 | PMCID | PMC5345109 | 15 | — |
| SRC-1565 | PMCID | PMC3906609 | 15 | — |
| SRC-1566 | PMCID | PMC9389452 | 15 | — |
| SRC-1572 | PMCID | PMC1835889 | 15 | — |
| SRC-1589 | PMCID | PMC4067036 | 15 | — |
| SRC-1590 | PMCID | PMC3714437 | 15 | — |
| SRC-1593 | PMCID | PMC2932446 | 15 | — |
| SRC-1594 | PMCID | PMC3552515 | 15 | — |
| SRC-1600 | PMCID | PMC4119885 | 15 | — |
| SRC-1602 | PMCID | PMC6724157 | 15 | — |
| SRC-1603 | PMCID | PMC9357455 | 15 | — |
| SRC-753 | PMCID | PMC4483306 | 16 | — |
| SRC-757 | PMCID | PMC7147428 | 16 | — |
| SRC-759 | PMCID | PMC7677067 | 16 | — |
| SRC-760 | PMCID | PMC10885559 | 16 | — |
| SRC-761 | PMCID | PMC9746481 | 16 | — |
| SRC-762 | PMCID | PMC9298213 | 16 | — |
| SRC-768 | PMCID | PMC2834395 | 16 | — |
| SRC-769 | PMCID | PMC10482588 | 16 | — |
| SRC-770 | PMCID | PMC11651366 | 16 | — |
| SRC-773 | PMCID | PMC8262231 | 16 | — |
| SRC-780 | PMCID | PMC10627755 | 16 | — |
| SRC-784 | PMCID | PMC10964840 | 16 | — |
| SRC-788 | PMCID | PMC2841791 | 16 | — |
| SRC-790 | PMCID | PMC6019344 | 16 | — |
| SRC-795 | PMCID | PMC8951218 | 16 | — |
| SRC-800 | PMCID | PMC4174312 | 16 | — |
| SRC-801 | PMCID | PMC9568645 | 16 | — |
| SRC-805 | PMCID | PMC3355691 | 16 | — |
| SRC-1850 | PMCID | PMC10529191 | 17 | — |
| SRC-1852 | PMCID | PMC12671840 | 17 | — |
| SRC-1856 | PMCID | PMC3161273 | 17 | — |
| SRC-1858 | PMCID | PMC2682407 | 17 | — |
| SRC-1862 | PMCID | PMC4293480 | 17 | — |
| SRC-1867 | PMCID | PMC1633771 | 17 | — |
| SRC-1875 | PMCID | PMC6483272 | 17 | — |
| SRC-1880 | PMCID | PMC2939331 | 17 | — |
| SRC-1885 | PMCID | PMC9258606 | 17 | — |
| SRC-1890 | PMCID | PMC3528062 | 17 | — |
| SRC-1892 | PMCID | PMC2690733 | 17 | — |
| SRC-992 | PMCID | PMC10563586 | 17 | 33 |
| SRC-3162 | PMID | 38311315 | 18 | — |
| SRC-3163 | PMID | 29470343 | 18 | — |
| SRC-3164 | PMCID | PMC6437668 | 18 | — |
| SRC-3164 | PMID | 29874535 | 18 | — |
| SRC-3166 | PMID | 12057549 | 18 | — |
| SRC-3168 | PMCID | PMC8094626 | 18 | — |
| SRC-3168 | PMID | 33368142 | 18 | — |
| SRC-3169 | PMCID | PMC5987201 | 18 | — |
| SRC-3169 | PMID | 29157866 | 18 | — |
| SRC-3170 | PMCID | PMC2803083 | 18 | — |
| SRC-3170 | PMID | 18753646 | 18 | — |
| SRC-3171 | PMCID | PMC10176440 | 18 | — |
| SRC-3171 | PMID | 37164498 | 18 | — |
| SRC-3172 | PMID | 29079144 | 18 | — |
| SRC-3173 | PMID | 30461695 | 18 | — |
| SRC-3174 | PMCID | PMC13485456 | 18 | — |
| SRC-3174 | PMID | 42374711 | 18 | — |
| SRC-3175 | PMID | 34011891 | 18 | — |
| SRC-3176 | PMID | 31513365 | 18 | — |
| SRC-3177 | PMID | 32080050 | 18 | — |
| SRC-3178 | PMID | 28742673 | 18 | — |
| SRC-3180 | PMID | 29422210 | 18 | — |
| SRC-3181 | PMID | 31348224 | 18 | — |
| SRC-3182 | PMID | 25050770 | 18 | 45 |
| SRC-3183 | PMID | 30048635 | 18 | — |
| SRC-3184 | PMID | 24176162 | 18 | — |
| SRC-3185 | PMID | 28742677 | 18 | — |
| SRC-3186 | PMID | 42131961 | 18 | — |
| SRC-3252 | PMCID | PMC12690181 | 18 | — |
| SRC-3252 | PMID | 41358885 | 18 | — |
| SRC-3255 | PMID | 42219800 | 18 | — |
| SRC-3256 | PMCID | PMC6880896 | 18 | — |
| SRC-3256 | PMID | 31770441 | 18 | — |
| SRC-3257 | PMID | 40287311 | 18 | — |
| SRC-3258 | PMCID | PMC5446003 | 18 | — |
| SRC-3258 | PMID | 27457513 | 18 | — |
| SRC-3259 | PMID | 38141870 | 18 | — |
| SRC-3260 | PMID | 34116035 | 18 | — |
| SRC-1353 | PMCID | PMC13035016 | 19 | — |
| SRC-1356 | PMCID | PMC5675031 | 19 | — |
| SRC-1363 | PMCID | PMC6492910 | 19 | — |
| SRC-1386 | PMCID | PMC5894487 | 19 | — |
| SRC-1387 | PMCID | PMC6671929 | 19 | — |
| SRC-4624 | PMCID | PMC3596108 | 19 | — |
| SRC-4625 | PMCID | PMC13509011 | 19 | — |
| SRC-4626 | PMCID | PMC8913909 | 19 | — |
| SRC-1101 | PMCID | PMC12936304 | 20 | — |
| SRC-1103 | PMCID | PMC5220204 | 20 | — |
| SRC-1108 | PMCID | PMC3022978 | 20 | — |
| SRC-1114 | PMCID | PMC5978683 | 20 | — |
| SRC-1119 | PMCID | PMC12255292 | 20 | — |
| SRC-1121 | PMCID | PMC11967268 | 20 | — |
| SRC-1124 | PMCID | PMC5548388 | 20 | — |
| SRC-1528 | PMCID | PMC5816307 | 20 | — |
| SRC-4524 | PMCID | PMC8630439 | 20 | — |
| SRC-1705 | PMCID | PMC2924476 | 21 | — |
| SRC-1706 | PMCID | PMC4409581 | 21 | — |
| SRC-1710 | PMCID | PMC4749120 | 21 | — |
| SRC-1711 | PMCID | PMC7098487 | 21 | — |
| SRC-1720 | PMCID | PMC6696822 | 21 | — |
| SRC-1723 | PMCID | PMC6620826 | 21 | — |
| SRC-1733 | PMCID | PMC1545152 | 21 | — |
| SRC-1432 | PMCID | PMC3964366 | 22 | — |
| SRC-1434 | PMCID | PMC12584420 | 22 | — |
| SRC-1435 | PMCID | PMC4725385 | 22 | 80 |
| SRC-1437 | PMCID | PMC4478082 | 22 | — |
| SRC-1439 | PMCID | PMC7108032 | 22 | — |
| SRC-1442 | PMCID | PMC4028525 | 22 | — |
| SRC-1444 | PMCID | PMC7944998 | 22 | — |
| SRC-4633 | PMCID | PMC4273169 | 22 | — |
| SRC-941 | PMCID | PMC4025242 | 23 | — |
| SRC-942 | PMCID | PMC4020724 | 23 | — |
| SRC-944 | PMCID | PMC7378414 | 23 | — |
| SRC-945 | PMCID | PMC11635034 | 23 | — |
| SRC-946 | PMCID | PMC11291844 | 23 | — |
| SRC-947 | PMCID | PMC10804889 | 23 | — |
| SRC-948 | PMCID | PMC9434589 | 23 | — |
| SRC-949 | PMCID | PMC5217949 | 23 | — |
| SRC-950 | PMCID | PMC1370926 | 23 | — |
| SRC-951 | PMCID | PMC8697255 | 23 | — |
| SRC-952 | PMCID | PMC12436038 | 23 | — |
| SRC-956 | PMCID | PMC11272983 | 23 | — |
| SRC-958 | PMCID | PMC11635029 | 23 | — |
| SRC-959 | PMCID | PMC6977405 | 23 | — |
| SRC-960 | PMCID | PMC5402875 | 23 | — |
| SRC-963 | PMCID | PMC11635050 | 23 | — |
| SRC-967 | PMCID | PMC5393479 | 23 | — |
| SRC-968 | PMCID | PMC6174196 | 23 | — |
| SRC-969 | PMCID | PMC6839734 | 23 | — |
| SRC-4390 | PMID | 38093915 | 24 | — |
| SRC-575 | PMCID | PMC7325726 | 25 | — |
| SRC-577 | PMCID | PMC9115617 | 25 | — |
| SRC-582 | PMCID | PMC2762083 | 25 | — |
| SRC-585 | PMCID | PMC4455140 | 25 | — |
| SRC-589 | PMCID | PMC4364860 | 25 | — |
| SRC-595 | PMCID | PMC3137658 | 25 | 67 |
| SRC-598 | PMCID | PMC1720564 | 25 | — |
| SRC-603 | PMCID | PMC2994083 | 25 | — |
| SRC-604 | PMCID | PMC5502308 | 25 | — |
| SRC-1073 | PMCID | PMC9365318 | 26 | — |
| SRC-1076 | PMCID | PMC9968263 | 26 | — |
| SRC-1078 | PMCID | PMC9023902 | 26 | — |
| SRC-1079 | PMCID | PMC10796623 | 26 | — |
| SRC-1083 | PMCID | PMC7938036 | 26 | — |
| SRC-001 | DOI | 10.1016/S0140-6736(24 | 27 | — |
| SRC-002 | PMID | 33789008 | 27 | — |
| SRC-003 | PMID | 35108470 | 27 | — |
| SRC-004 | DOI | 10.1016/S0140-6736(21 | 27 | — |
| SRC-007 | DOI | 10.1016/j.jhep.2021.12.022 | 27 | — |
| SRC-010 | PMCID | PMC10846564 | 27 | — |
| SRC-010 | PMID | 37734911 | 27 | — |
| SRC-011 | DOI | 10.1111/nmo.14058 | 27 | — |
| SRC-011 | PMID | 33373111 | 27 | — |
| SRC-018 | PMID | 34231046 | 27 | 92 |
| SRC-020 | DOI | 10.3748/wjg.v19.i25.3918 | 27 | — |
| SRC-020 | PMCID | PMC3703178 | 27 | — |
| SRC-020 | PMID | 23840136 | 27 | — |
| SRC-023 | DOI | 10.1016/j.idcr.2020.e00925 | 27 | — |
| SRC-023 | PMID | 33005566 | 27 | — |
| SRC-024 | PMCID | PMC6571398 | 27 | — |
| SRC-024 | PMID | 31169688 | 27 | — |
| SRC-025 | DOI | 10.1056/NEJMoa1905380 | 27 | — |
| SRC-026 | DOI | 10.1056/NEJMoa2205982 | 27 | — |
| SRC-027 | DOI | 10.1056/NEJMoa1211801 | 27 | — |
| SRC-4966 | PMID | 40114631 | 27 | — |
| SRC-4303 | PMCID | PMC7063389 | 28 | — |
| SRC-4303 | PMID | 31229958 | 28 | — |
| SRC-4310 | PMID | 40268118 | 28 | — |
| SRC-374 | PMID | 36959028 | 29 | — |
| SRC-377 | PMCID | PMC4222924 | 29 | — |
| SRC-377 | PMID | 25383202 | 29 | — |
| SRC-378 | PMID | 41016738 | 29 | — |
| SRC-379 | PMCID | PMC6464977 | 29 | — |
| SRC-379 | PMID | 25618845 | 29 | — |
| SRC-383 | PMCID | PMC12996173 | 29 | — |
| SRC-383 | PMID | 41859138 | 29 | — |
| SRC-384 | DOI | 10.5811/westjem.2013.3.16276 | 29 | — |
| SRC-385 | PMCID | PMC4104740 | 29 | — |
| SRC-385 | PMID | 24980209 | 29 | — |
| SRC-534 | PMCID | PMC4771236 | 29 | — |
| SRC-878 | PMCID | PMC4525003 | 30 | — |
| SRC-886 | PMCID | PMC2386281 | 30 | — |
| SRC-887 | PMCID | PMC4525003 | 30 | — |
| SRC-889 | PMCID | PMC4880116 | 30 | 84 |
| SRC-890 | PMCID | PMC11180513 | 30 | — |
| SRC-898 | PMCID | PMC5678742 | 30 | — |
| SRC-4727 | PMCID | PMC1949079 | 31 | — |
| SRC-4728 | PMCID | PMC5436019 | 31 | — |
| SRC-721 | PMCID | PMC5936048 | 31 | — |
| SRC-722 | PMCID | PMC5972549 | 31 | — |
| SRC-724 | PMCID | PMC7181180 | 31 | — |
| SRC-735 | PMCID | PMC4418931 | 31 | — |
| SRC-736 | PMCID | PMC8215888 | 31 | — |
| SRC-737 | PMCID | PMC3818885 | 31 | — |
| SRC-738 | PMCID | PMC8140030 | 31 | — |
| SRC-739 | PMCID | PMC5008168 | 31 | — |
| SRC-742 | PMCID | PMC5439293 | 31 | — |
| SRC-743 | PMCID | PMC4124057 | 31 | — |
| SRC-747 | PMCID | PMC5332236 | 31 | — |
| SRC-748 | PMCID | PMC7642136 | 31 | — |
| SRC-473 | PMCID | PMC4356534 | 32 | — |
| SRC-475 | PMCID | PMC4513953 | 32 | — |
| SRC-477 | PMCID | PMC3476611 | 32 | — |
| SRC-478 | PMID | 25085985 | 32 | — |
| SRC-479 | PMCID | PMC8794420 | 32 | — |
| SRC-485 | DOI | 10.1136/thorax-2023-220304 | 32 | — |
| SRC-550 | PMCID | PMC8280089 | 32 | — |
| SRC-552 | PMCID | PMC9015199 | 32 | — |
| SRC-554 | PMCID | PMC10036605 | 32 | — |
| SRC-565 | PMCID | PMC5900094 | 32 | — |
| SRC-1000 | PMCID | PMC4772032 | 33 | — |
| SRC-1533 | PMCID | PMC7379941 | 33 | — |
| SRC-971 | PMCID | PMC11150976 | 33 | — |
| SRC-972 | PMCID | PMC10164595 | 33 | — |
| SRC-982 | PMCID | PMC6283429 | 33 | — |
| SRC-986 | PMCID | PMC9710417 | 33 | — |
| SRC-993 | PMCID | PMC3512229 | 33 | — |
| SRC-653 | DOI | 10.12659/msm.881937 | 34 | — |
| SRC-661 | PMCID | PMC4491294 | 34 | — |
| SRC-440 | PMID | 41712677 | 35 | — |
| SRC-441 | PMID | 24716681 | 35 | — |
| SRC-442 | DOI | 10.1056/NEJMoa032274 | 35 | — |
| SRC-443 | DOI | 10.1056/NEJMoa1209657 | 35 | — |
| SRC-448 | PMID | 6110912 | 35 | — |
| SRC-449 | PMID | 32894695 | 35 | 43 |
| SRC-164 | PMCID | PMC8515119 | 36 | 40・79 |
| SRC-164 | PMID | 34497146 | 36 | 40・79 |
| SRC-2468 | PMCID | PMC4425443 | 36 | — |
| SRC-2469 | PMCID | PMC4086808 | 36 | — |
| SRC-4979 | PMCID | PMC6619426 | 37 | — |
| SRC-660 | PMCID | PMC2413335 | 37 | — |
| SRC-911 | PMCID | PMC3228182 | 37 | — |
| SRC-912 | PMCID | PMC4739132 | 37 | — |
| SRC-922 | PMCID | PMC10515122 | 37 | — |
| SRC-928 | PMCID | PMC3517709 | 37 | — |
| SRC-932 | PMCID | PMC4880117 | 37 | 74 |
| SRC-187 | PMCID | PMC8901245 | 38 | — |
| SRC-4380 | PMID | 29650544 | 38 | — |
| SRC-251 | PMID | 11999637 | 39 | — |
| SRC-252 | PMID | 26853248 | 39 | — |
| SRC-253 | PMID | 26332547 | 39 | — |
| SRC-254 | PMCID | PMC10356869 | 39 | — |
| SRC-254 | PMID | 37382827 | 39 | — |
| SRC-4383 | PMID | 34305070 | 39 | — |
| SRC-4384 | PMCID | PMC3415273 | 39 | — |
| SRC-4384 | PMID | 21463150 | 39 | — |
| SRC-4385 | PMID | 36027563 | 39 | — |
| SRC-4386 | PMCID | PMC1860601 | 39 | — |
| SRC-4386 | PMID | 17098886 | 39 | — |
| SRC-4388 | PMID | 23114485 | 39 | — |
| SRC-4442 | PMCID | PMC10226890 | 39 | — |
| SRC-4444 | PMCID | PMC9451503 | 39 | — |
| SRC-163 | PMID | 30792244 | 40 | — |
| SRC-165 | PMCID | PMC8355884 | 40 | — |
| SRC-165 | PMID | 34362780 | 40 | — |
| SRC-167 | PMCID | PMC5415221 | 40 | — |
| SRC-167 | PMID | 28507745 | 40 | — |
| SRC-168 | PMID | 30181091 | 40 | — |
| SRC-169 | DOI | 10.1016/j.clnu.2021.03.031 | 40 | — |
| SRC-204 | PMCID | PMC7263833 | 41 | — |
| SRC-209 | PMCID | PMC6593641 | 41 | — |
| SRC-211 | PMCID | PMC2895332 | 41 | — |
| SRC-2572 | PMCID | PMC11488644 | 42 | — |
| SRC-2577 | PMCID | PMC11702892 | 42 | — |
| SRC-2581 | PMCID | PMC3901044 | 42 | — |
| SRC-2584 | PMCID | PMC4846284 | 42 | — |
| SRC-2588 | PMCID | PMC6436818 | 42 | — |
| SRC-2643 | PMCID | PMC13696133 | 43 | — |
| SRC-2651 | DOI | 10.2491/jjsth.29.288 | 43 | — |
| SRC-2659 | PMCID | PMC7805326 | 43 | — |
| SRC-2660 | PMCID | PMC7327664 | 43 | — |
| SRC-2666 | PMCID | PMC11034817 | 43 | — |
| SRC-1271 | PMCID | PMC5475221 | 44 | — |
| SRC-1272 | PMCID | PMC8526627 | 44 | — |
| SRC-1278 | PMCID | PMC11232864 | 44 | — |
| SRC-1283 | PMCID | PMC4422053 | 44 | — |
| SRC-1294 | PMCID | PMC5710547 | 44 | — |
| SRC-1312 | PMCID | PMC8935739 | 44 | — |
| SRC-1313 | PMCID | PMC9073858 | 44 | — |
| SRC-4376 | PMCID | PMC7182575 | 44 | — |
| SRC-4376 | PMID | 32313173 | 44 | — |
| SRC-4377 | PMCID | PMC3693028 | 44 | — |
| SRC-4377 | PMID | 23826541 | 44 | — |
| SRC-1028 | PMCID | PMC9887297 | 45 | 77 |
| SRC-3355 | PMID | 41122887 | 45 | — |
| SRC-3356 | PMID | 26393460 | 45 | — |
| SRC-3359 | PMID | 31856124 | 45 | — |
| SRC-3360 | PMCID | PMC13038240 | 45 | — |
| SRC-3360 | PMID | 41802129 | 45 | — |
| SRC-3361 | PMCID | PMC10751720 | 45 | — |
| SRC-3361 | PMID | 37353207 | 45 | — |
| SRC-3362 | PMCID | PMC10990371 | 45 | — |
| SRC-3362 | PMID | 38576961 | 45 | — |
| SRC-3363 | PMCID | PMC11867197 | 45 | — |
| SRC-3363 | PMID | 32753712 | 45 | — |
| SRC-3364 | PMID | 16707748 | 45 | — |
| SRC-3365 | PMID | 9673527 | 45 | — |
| SRC-3431 | PMID | 35927462 | 45 | — |
| SRC-3432 | PMID | 29906300 | 45 | — |
| SRC-3433 | PMCID | PMC6494160 | 45 | — |
| SRC-3433 | PMID | 29551014 | 45 | — |
| SRC-3434 | PMID | 21357346 | 45 | — |
| SRC-3436 | PMID | 30455342 | 45 | — |
| SRC-3437 | PMID | 31285392 | 45 | — |
| SRC-3438 | PMID | 35190810 | 45 | — |
| SRC-3439 | PMCID | PMC2799187 | 45 | — |
| SRC-3439 | PMID | 19816235 | 45 | — |
| SRC-3440 | PMID | 25109786 | 45 | — |
| SRC-3441 | PMCID | PMC12708991 | 45 | — |
| SRC-3441 | PMID | 41415326 | 45 | — |
| SRC-3443 | PMCID | PMC8487591 | 45 | — |
| SRC-3443 | PMID | 33382931 | 45 | — |
| SRC-3444 | PMID | 27812060 | 45 | — |
| SRC-3445 | PMID | 413500 | 45 | — |
| SRC-367 | PMCID | PMC4880076 | 46 | — |
| SRC-367 | PMID | 27191735 | 46 | — |
| SRC-370 | PMID | 37553157 | 46 | 65・71 |
| SRC-1783 | PMCID | PMC4464797 | 47 | — |
| SRC-1788 | PMCID | PMC2576513 | 47 | — |
| SRC-1792 | PMCID | PMC3913566 | 47 | — |
| SRC-1797 | PMCID | PMC12410088 | 47 | — |
| SRC-1802 | PMCID | PMC6440254 | 47 | — |
| SRC-4817 | PMCID | PMC2697338 | 47 | — |
| SRC-606 | PMCID | PMC12406467 | 50 | — |
| SRC-621 | PMCID | PMC6296208 | 50 | — |
| SRC-622 | PMCID | PMC3616759 | 50 | — |
| SRC-623 | PMCID | PMC5657490 | 50 | — |
| SRC-627 | PMCID | PMC6233707 | 50 | — |
| SRC-630 | PMCID | PMC8092065 | 50 | — |
| SRC-4726 | PMCID | PMC10837653 | 51 | — |
| SRC-692 | PMCID | PMC5131734 | 51 | — |
| SRC-694 | PMCID | PMC5934505 | 51 | — |
| SRC-695 | PMCID | PMC9846865 | 51 | — |
| SRC-698 | PMCID | PMC4137319 | 51 | — |
| SRC-699 | PMCID | PMC2672131 | 51 | — |
| SRC-704 | PMCID | PMC2880271 | 51 | — |
| SRC-715 | PMCID | PMC4251068 | 51 | — |
| SRC-717 | PMCID | PMC6483329 | 51 | — |
| SRC-719 | PMCID | PMC3825963 | 51 | — |
| SRC-181 | PMCID | PMC8339126 | 52 | — |
| SRC-4378 | PMID | 20404258 | 52 | — |
| SRC-4379 | PMCID | PMC11317726 | 52 | — |
| SRC-4379 | PMID | 39139890 | 52 | — |
| SRC-1762 | PMCID | PMC7884987 | 53 | — |
| SRC-1763 | PMCID | PMC5189669 | 53 | — |
| SRC-1769 | PMCID | PMC5736307 | 53 | 61 |
| SRC-1770 | PMCID | PMC7003613 | 53 | — |
| SRC-1771 | PMCID | PMC5869704 | 53 | — |
| SRC-1772 | PMCID | PMC7251505 | 53 | — |
| SRC-1773 | PMCID | PMC6294540 | 53 | — |
| SRC-1774 | PMCID | PMC6814415 | 53 | — |
| SRC-1775 | PMCID | PMC5867231 | 53 | — |
| SRC-1776 | PMCID | PMC7711326 | 53 | — |
| SRC-1454 | PMCID | PMC13430245 | 54 | — |
| SRC-1457 | PMCID | PMC5179293 | 54 | — |
| SRC-1458 | PMCID | PMC5098472 | 54 | — |
| SRC-1459 | PMCID | PMC7002428 | 54 | — |
| SRC-1460 | PMCID | PMC5820813 | 54 | — |
| SRC-1466 | PMCID | PMC5556798 | 54 | — |
| SRC-1469 | PMCID | PMC6750779 | 54 | — |
| SRC-1471 | PMCID | PMC7575916 | 54 | — |
| SRC-1472 | PMCID | PMC5635626 | 54 | — |
| SRC-1476 | PMCID | PMC11090237 | 54 | — |
| SRC-668 | PMCID | PMC4688452 | 55 | — |
| SRC-669 | PMCID | PMC11303840 | 55 | — |
| SRC-672 | PMCID | PMC4741037 | 55 | — |
| SRC-673 | PMCID | PMC5443345 | 55 | — |
| SRC-677 | PMCID | PMC6311976 | 55 | — |
| SRC-678 | PMCID | PMC5738929 | 55 | — |
| SRC-679 | PMCID | PMC12611495 | 55 | — |
| SRC-1989 | PMCID | PMC12091269 | 56 | — |
| SRC-1996 | PMCID | PMC3770179 | 56 | — |
| SRC-2001 | PMCID | PMC1735122 | 56 | — |
| SRC-2005 | PMCID | PMC3749068 | 56 | — |
| SRC-2007 | PMCID | PMC2744281 | 56 | — |
| SRC-2008 | DOI | 10.1111/j.1469-8749.2007.tb12610.x | 56 | — |
| SRC-2010 | PMCID | PMC6779591 | 56 | — |
| SRC-1893 | PMCID | PMC8045119 | 57 | — |
| SRC-1896 | PMCID | PMC4733230 | 57 | — |
| SRC-1899 | PMCID | PMC4979196 | 57 | — |
| SRC-1904 | PMCID | PMC5444408 | 57 | — |
| SRC-1911 | PMCID | PMC5106475 | 57 | — |
| SRC-1916 | PMCID | PMC3926794 | 57 | — |
| SRC-3263 | PMID | 38096556 | 58 | — |
| SRC-3264 | PMID | 18757666 | 58 | — |
| SRC-3265 | PMID | 20633305 | 58 | — |
| SRC-3266 | PMID | 30045211 | 58 | — |
| SRC-3267 | PMCID | PMC6505738 | 58 | — |
| SRC-3267 | PMID | 25828903 | 58 | — |
| SRC-3270 | PMCID | PMC6109652 | 58 | — |
| SRC-3270 | PMID | 30174462 | 58 | — |
| SRC-3271 | PMID | 28426618 | 58 | — |
| SRC-3272 | PMID | 30681543 | 58 | — |
| SRC-3273 | PMID | 30134424 | 58 | — |
| SRC-3275 | PMID | 28937571 | 58 | — |
| SRC-3276 | PMCID | PMC5446563 | 58 | — |
| SRC-3276 | PMID | 28456509 | 58 | — |
| SRC-3277 | PMID | 26987420 | 58 | — |
| SRC-3278 | PMID | 12464994 | 58 | — |
| SRC-3280 | PMID | 39890756 | 58 | — |
| SRC-3281 | PMCID | PMC3109493 | 58 | — |
| SRC-3281 | PMID | 16724884 | 58 | — |
| SRC-3282 | PMID | 37486660 | 58 | — |
| SRC-3283 | PMCID | PMC7050613 | 58 | — |
| SRC-3283 | PMID | 25922861 | 58 | — |
| SRC-3284 | PMID | 30684460 | 58 | — |
| SRC-3285 | PMID | 29939938 | 58 | — |
| SRC-1375 | PMCID | PMC7770314 | 59 | — |
| SRC-1383 | PMCID | PMC6331298 | 59 | — |
| SRC-2825 | DOI | 10.3950/jibiinkoka.123.485 | 59 | 60 |
| SRC-4627 | PMCID | PMC9479471 | 59 | — |
| SRC-424 | DOI | 10.1164/rccm.202005-2032ST | 60 | — |
| SRC-424 | PMCID | PMC7397797 | 60 | — |
| SRC-424 | PMID | 32706311 | 60 | — |
| SRC-426 | PMCID | PMC10991853 | 60 | — |
| SRC-426 | PMID | 38423624 | 60 | — |
| SRC-293 | PMID | 40811497 | 62 | — |
| SRC-294 | PMID | 40658480 | 62 | — |
| SRC-295 | DOI | 10.1590/S1806-37562016000000190 | 62 | — |
| SRC-295 | PMCID | PMC5790661 | 62 | — |
| SRC-295 | PMID | 28767770 | 62 | — |
| SRC-297 | PMID | 28286246 | 62 | 64 |
| SRC-4381 | PMID | 41476123 | 62 | — |
| SRC-4382 | PMID | 33637192 | 62 | — |
| SRC-2991 | PMID | 28110981 | 63 | — |
| SRC-2992 | PMID | 21109520 | 63 | — |
| SRC-2993 | PMID | 16871531 | 63 | — |
| SRC-2994 | PMCID | PMC11103320 | 63 | — |
| SRC-2994 | PMID | 38499325 | 63 | — |
| SRC-2995 | PMID | 34967407 | 63 | — |
| SRC-2997 | PMID | 40234174 | 63 | — |
| SRC-2998 | PMID | 34140301 | 63 | — |
| SRC-2999 | PMID | 27916278 | 63 | — |
| SRC-3000 | PMID | 27377815 | 63 | — |
| SRC-3001 | PMID | 37839908 | 63 | — |
| SRC-3002 | PMID | 36420821 | 63 | — |
| SRC-3003 | PMID | 33274670 | 63 | — |
| SRC-3004 | PMID | 25908771 | 63 | — |
| SRC-423 | PMCID | PMC7159433 | 63 | — |
| SRC-423 | PMID | 32293205 | 63 | — |
| SRC-4974 | PMCID | PMC6240444 | 63 | — |
| SRC-309 | PMID | 19228821 | 64 | — |
| SRC-310 | PMID | 19228822 | 64 | — |
| SRC-311 | PMID | 25559473 | 64 | — |
| SRC-4893 | PMCID | PMC4332083 | 65 | — |
| SRC-4894 | PMCID | PMC9488631 | 65 | — |
| SRC-4895 | PMID | 33090900 | 65 | — |
| SRC-491 | DOI | 10.1097/TA.0000000000001350 | 65 | — |
| SRC-491 | PMID | 28030502 | 65 | — |
| SRC-567 | PMCID | PMC5045849 | 65 | — |
| SRC-570 | DOI | 10.1016/j.pulmoe.2018.10.008 | 65 | — |
| SRC-570 | PMID | 30509855 | 65 | — |
| SRC-1611 | PMCID | PMC8328013 | 66 | — |
| SRC-1613 | PMCID | PMC5820703 | 66 | — |
| SRC-1614 | PMCID | PMC5170873 | 66 | — |
| SRC-1617 | PMCID | PMC8972311 | 66 | — |
| SRC-1618 | PMCID | PMC10113344 | 66 | — |
| SRC-1620 | PMCID | PMC8563316 | 66 | — |
| SRC-1621 | PMCID | PMC6954440 | 66 | — |
| SRC-1623 | PMCID | PMC10619142 | 66 | — |
| SRC-1624 | PMCID | PMC3151370 | 66 | — |
| SRC-2951 | PMCID | PMC3298664 | 67 | — |
| SRC-2954 | PMCID | PMC12323812 | 67 | — |
| SRC-420 | PMID | 35106964 | 67 | — |
| SRC-421 | DOI | 10.1002/art.41983 | 67 | — |
| SRC-421 | PMID | 35106973 | 67 | — |
| SRC-422 | PMID | 35110334 | 67 | — |
| SRC-3833 | PMID | 34700345 | 68 | — |
| SRC-3835 | PMCID | PMC6850610 | 68 | — |
| SRC-3835 | PMID | 30671947 | 68 | — |
| SRC-3836 | PMID | 18358406 | 68 | — |
| SRC-3838 | PMID | 31843864 | 68 | — |
| SRC-3841 | PMCID | PMC7067282 | 68 | — |
| SRC-3841 | PMID | 31570648 | 68 | — |
| SRC-3843 | PMID | 31249310 | 68 | — |
| SRC-3845 | PMID | 25724675 | 68 | — |
| SRC-3847 | PMID | 22759682 | 68 | — |
| SRC-3848 | PMCID | PMC3687212 | 68 | — |
| SRC-3848 | PMID | 23773662 | 68 | — |
| SRC-3849 | PMID | 27806867 | 68 | — |
| SRC-3850 | PMID | 34544592 | 68 | — |
| SRC-3081 | PMID | 27189259 | 69 | — |
| SRC-3082 | PMCID | PMC7388344 | 69 | — |
| SRC-3082 | PMID | 32743511 | 69 | — |
| SRC-3083 | PMCID | PMC6439403 | 69 | — |
| SRC-3083 | PMID | 30937141 | 69 | — |
| SRC-3084 | PMID | 27836054 | 69 | — |
| SRC-3085 | PMCID | PMC7612067 | 69 | — |
| SRC-3085 | PMID | 30864154 | 69 | — |
| SRC-3087 | PMCID | PMC4900471 | 69 | — |
| SRC-3087 | PMID | 27189754 | 69 | — |
| SRC-3088 | PMCID | PMC10501739 | 69 | — |
| SRC-3088 | PMID | 37254856 | 69 | — |
| SRC-3089 | PMID | 32643199 | 69 | — |
| SRC-3090 | PMCID | PMC5821468 | 69 | — |
| SRC-3090 | PMID | 28593997 | 69 | — |
| SRC-3092 | PMCID | PMC13184495 | 69 | — |
| SRC-3092 | PMID | 42165046 | 69 | — |
| SRC-3093 | PMCID | PMC2952982 | 69 | — |
| SRC-3093 | PMID | 20930072 | 69 | — |
| SRC-3095 | PMCID | PMC4281323 | 69 | — |
| SRC-3095 | PMID | 25344526 | 69 | — |
| SRC-3096 | PMID | 24098001 | 69 | — |
| SRC-3097 | PMID | 34481993 | 69 | — |
| SRC-3098 | PMCID | PMC4751577 | 69 | — |
| SRC-3098 | PMID | 26611557 | 69 | — |
| SRC-2734 | PMCID | PMC9345633 | 70 | — |
| SRC-2736 | PMCID | PMC12144679 | 70 | — |
| SRC-2743 | PMCID | PMC4979194 | 70 | — |
| SRC-501 | PMID | 34949706 | 71 | — |
| SRC-502 | DOI | 10.1164/rccm.9120-11st | 71 | — |
| SRC-502 | PMCID | PMC4408724 | 71 | — |
| SRC-503 | PMID | 20864792 | 71 | — |
| SRC-504 | PMCID | PMC3655828 | 71 | — |
| SRC-504 | PMID | 23663438 | 71 | — |
| SRC-505 | DOI | 10.1136/thoraxjnl-2016-209729 | 71 | — |
| SRC-507 | PMID | 28860265 | 71 | — |
| SRC-508 | DOI | 10.1164/rccm.202306-1066st | 71 | — |
| SRC-508 | PMCID | PMC10449064 | 71 | — |
| SRC-1810 | PMCID | PMC3232636 | 72 | — |
| SRC-1814 | PMCID | PMC6340385 | 72 | — |
| SRC-1745 | PMCID | PMC6464149 | 73 | — |
| SRC-1754 | PMCID | PMC11928260 | 73 | — |
| SRC-1755 | PMCID | PMC4896870 | 73 | — |
| SRC-1759 | PMCID | PMC4493167 | 73 | — |
| SRC-1832 | PMCID | PMC2267485 | 74 | — |
| SRC-3341 | PMID | 40966736 | 75 | 88 |
| SRC-3342 | PMID | 26433401 | 75 | — |
| SRC-3343 | PMID | 22398791 | 75 | — |
| SRC-3344 | PMID | 10645517 | 75 | — |
| SRC-3345 | PMID | 39029545 | 75 | — |
| SRC-3346 | PMID | 26909664 | 75 | — |
| SRC-3348 | PMID | 10620643 | 75 | — |
| SRC-3349 | PMID | 20410781 | 75 | — |
| SRC-3350 | PMID | 28325581 | 75 | — |
| SRC-3351 | PMID | 41284292 | 75 | — |
| SRC-3352 | PMID | 35592929 | 75 | — |
| SRC-3353 | PMCID | PMC13344273 | 75 | — |
| SRC-3353 | PMID | 42596935 | 75 | — |
| SRC-3354 | PMID | 32080052 | 75 | — |
| SRC-2048 | PMCID | PMC5381807 | 76 | — |
| SRC-2049 | PMCID | PMC4067812 | 76 | — |
| SRC-2057 | PMCID | PMC4569751 | 76 | — |
| SRC-2066 | PMCID | PMC7537588 | 76 | — |
| SRC-2067 | PMCID | PMC7745181 | 76 | — |
| SRC-2068 | PMCID | PMC7383595 | 76 | — |
| SRC-2069 | PMCID | PMC3651993 | 76 | — |
| SRC-2071 | PMCID | PMC6481355 | 76 | — |
| SRC-2073 | PMCID | PMC4861986 | 76 | — |
| SRC-2074 | PMCID | PMC10680050 | 76 | — |
| SRC-1027 | PMCID | PMC6979443 | 77 | 98 |
| SRC-1029 | PMCID | PMC8001676 | 77 | — |
| SRC-1030 | PMCID | PMC6456929 | 77 | 87 |
| SRC-1033 | PMCID | PMC11891912 | 77 | — |
| SRC-1034 | PMCID | PMC4146814 | 77 | — |
| SRC-1040 | PMCID | PMC8252715 | 77 | — |
| SRC-3616 | PMID | 32511109 | 78 | 95 |
| SRC-3971 | PMID | 35985955 | 78 | — |
| SRC-3973 | PMID | 25427113 | 78 | — |
| SRC-3977 | PMCID | PMC3657020 | 78 | — |
| SRC-3977 | PMID | 23404347 | 78 | — |
| SRC-3979 | PMCID | PMC1725608 | 78 | — |
| SRC-3979 | PMID | 11435353 | 78 | — |
| SRC-3980 | PMID | 3784839 | 78 | — |
| SRC-3981 | PMID | 37552484 | 78 | — |
| SRC-3982 | PMID | 25986310 | 78 | — |
| SRC-3984 | PMCID | PMC4688551 | 78 | — |
| SRC-3984 | PMID | 23372174 | 78 | — |
| SRC-3985 | PMCID | PMC11458184 | 78 | — |
| SRC-3985 | PMID | 38320504 | 78 | — |
| SRC-3986 | PMID | 18456329 | 78 | — |
| SRC-2478 | PMCID | PMC2950323 | 79 | — |
| SRC-2484 | PMCID | PMC6850655 | 79 | — |
| SRC-2487 | PMCID | PMC4374744 | 79 | — |
| SRC-2153 | PMCID | PMC6860006 | 80 | — |
| SRC-2161 | PMCID | PMC3255962 | 80 | — |
| SRC-2164 | PMCID | PMC6055529 | 80 | — |
| SRC-2170 | PMCID | PMC8404698 | 80 | — |
| SRC-1024 | PMCID | PMC2276281 | 82 | — |
| SRC-1025 | PMCID | PMC3784111 | 82 | — |
| SRC-4122 | PMID | 25502048 | 83 | — |
| SRC-4125 | PMID | 37833187 | 83 | — |
| SRC-4126 | PMCID | PMC3863169 | 83 | — |
| SRC-4126 | PMID | 24376971 | 83 | — |
| SRC-4127 | PMID | 22171960 | 83 | — |
| SRC-4128 | PMID | 30522251 | 83 | — |
| SRC-4129 | PMID | 33555169 | 83 | — |
| SRC-4131 | PMID | 33084394 | 83 | — |
| SRC-4133 | PMCID | PMC12451064 | 83 | — |
| SRC-4133 | PMID | 40989537 | 83 | — |
| SRC-4134 | PMID | 25384489 | 83 | — |
| SRC-4139 | PMID | 30956268 | 83 | — |
| SRC-1046 | PMCID | PMC6987775 | 84 | — |
| SRC-1049 | PMCID | PMC6850662 | 84 | — |
| SRC-1050 | PMCID | PMC3441105 | 84 | — |
| SRC-2191 | ページ | 1-13 | 85 | — |
| SRC-1201 | PMCID | PMC6516870 | 86 | — |
| SRC-1203 | PMCID | PMC1496896 | 86 | — |
| SRC-1204 | PMCID | PMC3994805 | 86 | — |
| SRC-3521 | PMID | 35490285 | 87 | — |
| SRC-3522 | PMCID | PMC8428796 | 87 | — |
| SRC-3522 | PMID | 32029743 | 87 | — |
| SRC-3523 | PMCID | PMC11759048 | 87 | — |
| SRC-3523 | PMID | 38748847 | 87 | — |
| SRC-3524 | PMID | 32959490 | 87 | — |
| SRC-3525 | PMID | 27643592 | 87 | — |
| SRC-3531 | PMID | 34011889 | 88 | — |
| SRC-3532 | PMID | 26443610 | 88 | — |
| SRC-3535 | PMID | 32804883 | 88 | — |
| SRC-3538 | PMCID | PMC5034743 | 88 | — |
| SRC-3538 | PMID | 26681211 | 88 | — |
| SRC-3539 | PMID | 26580836 | 88 | — |
| SRC-3856 | PMID | 40495096 | 89 | — |
| SRC-3858 | PMID | 23944116 | 89 | — |
| SRC-3862 | PMID | 24529036 | 89 | — |
| SRC-3863 | PMCID | PMC3584580 | 89 | — |
| SRC-3863 | PMID | 23459093 | 89 | — |
| SRC-3865 | PMID | 26052687 | 89 | — |
| SRC-3866 | PMID | 9606102 | 89 | — |
| SRC-2083 | PMCID | PMC9148753 | 90 | — |
| SRC-2086 | PMCID | PMC5217791 | 90 | — |
| SRC-4882 | PMCID | PMC5475226 | 90 | — |
| SRC-4035 | PMCID | PMC13612910 | 91 | — |
| SRC-4035 | PMID | 42798716 | 91 | — |
| SRC-4038 | PMCID | PMC2493390 | 91 | — |
| SRC-4038 | PMID | 17706760 | 91 | — |
| SRC-4039 | PMCID | PMC3243009 | 91 | — |
| SRC-4039 | PMID | 21615775 | 91 | — |
| SRC-4047 | PMCID | PMC1741012 | 91 | — |
| SRC-4047 | PMID | 15837849 | 91 | — |
| SRC-4048 | PMCID | PMC12127028 | 91 | — |
| SRC-4048 | PMID | 40392119 | 91 | — |
| SRC-4050 | PMCID | PMC8439371 | 91 | — |
| SRC-4050 | PMID | 34540358 | 91 | — |
| SRC-3611 | PMID | 20724309 | 92 | — |
| SRC-3612 | PMCID | PMC5717753 | 92 | — |
| SRC-3612 | PMID | 28973626 | 92 | — |
| SRC-3613 | PMCID | PMC4066613 | 92 | — |
| SRC-3613 | PMID | 24590568 | 92 | — |
| SRC-3614 | PMID | 10053175 | 92 | — |
| SRC-4026 | PMCID | PMC9616535 | 93 | — |
| SRC-4026 | PMID | 35643228 | 93 | — |
| SRC-4030 | PMCID | PMC9050565 | 93 | — |
| SRC-4030 | PMID | 35279265 | 93 | — |
| SRC-4031 | PMCID | PMC11933966 | 93 | — |
| SRC-4031 | PMID | 40145071 | 93 | — |
| SRC-4033 | PMID | 36115418 | 93 | — |
| SRC-4801 | PMCID | PMC13097252 | 93 | — |
| SRC-4801 | PMID | 42011820 | 93 | — |
| SRC-234 | PMCID | PMC8052586 | 94 | — |
| SRC-234 | PMID | 33339003 | 94 | — |
| SRC-3617 | PMID | 8329970 | 95 | — |
| SRC-3618 | PMID | 16968349 | 95 | — |
| SRC-3620 | PMID | 31346179 | 95 | — |
| SRC-2149 | PMCID | PMC4332564 | 96 | — |
| SRC-3851 | PMID | 39482953 | 97 | — |
| SRC-3852 | PMCID | PMC7199382 | 97 | — |
| SRC-3852 | PMID | 32368793 | 97 | — |
| SRC-3854 | PMID | 19217077 | 97 | — |
| SRC-3855 | PMID | 32452729 | 97 | — |
| SRC-3529 | PMID | 31843861 | 98 | — |
| SRC-4140 | PMCID | PMC6620762 | 99 | — |
| SRC-4140 | PMID | 31219028 | 99 | — |
| SRC-4141 | PMCID | PMC7533286 | 99 | — |
| SRC-4141 | PMID | 33072341 | 99 | — |

## 3. 要・正本確認一覧（17件）

カード側の値・書誌表記、または出典マスター側の記録が、主出典・実在の出典と食い違う疑いの件。いずれも棚卸しではカードを変更せず、両値を記録して申し送ったもの。

| 対象 | 食い違いの内容 | バッチ |
|---|---|---|
| ML-012 | カードは「高リスク 2.35%/年」とするが、主出典（Barbui 2012）の 2.35% は中リスクの値で、高リスクは 3.56%/年。ラベルの取り違えの疑い（スコア自体は一致） | 81 |
| PX-001 | カードの書誌表記（題名・著者・49(6):595-599）が実在の論文と一致しない。カードの DOI・PMID はマスターの出典（Daza ら "Mapping the Mental Status Examination", 49(4):355-364）を正しく指している | 89 |
| PX-012 | カードの書誌表記（…2S-33S）が実在の出典と一致しない。実際の AACAP パラメータは 4S-20S。DOI・PMID は正しい | 89 |
| PX-005 | カードの章題の文言がガイドライン・マスターと細部で異なる | 89 |
| SM-002 | 巻号：マスター・カードは 167 だが、PubMed・Crossref・Europe PMC はいずれも 165（DOI・PMID・ページは一致） | 93 |
| TJ-032 | カードは Chance 型を B2 とするが、原典（Vaccaro 2013／AO 分類）は B1 | 8 |
| SRC-2481 | マスターとカードの双方に登録された PMCID PMC7127472 は別論文（Tefferi 2005、PMID 16007898）のもの。正しい PMCID は PMC4415389（区分訂正・license_note は第1節・第5節） | 79 |
| FT-015 | 登録済みカードの plain_statement_ja が手元の控えでは文の途中で途切れて見える（納品下書きには全文あり） | 75 |
| PN-024 | カード側の source_class が UNKNOWN、マスター（SRC-1721）は RESTRICTED で不一致 | 73 |
| AL-022・AL-023 | カード側の source_class が UNKNOWN、マスターは RESTRICTED で不一致 | 60 |
| PH-016 | マスターの PMID 26414986 は誤り（Auger 2015 の概日リズムガイドラインを指す）。Sateia 2017（不眠症薬物療法）の正しい PMID は 27998379 | 1 |
| PH-013 | 登録済みの DOI 10.5664/jcsm.11836 は無関係のレター論文、PMID 41059796 は無関係の論文（ドライアイ、後に撤回）を指す。出典同定自体の再確認が必要 | 1 |
| PH-018 | カードの「PLMD にもガバペンチノイドが強い推奨」は、AASM 2025 ガイドライン抄録の PLMD 推奨（条件付き反対2件のみ）に見当たらない。本文での確認が必要 | 1 |
| SD-059 | カードの「サリチル酸の治癒率は平均49%」の 49% は、pooled analysis（PMID 21219294）では凍結療法の値。サリチル酸は 52%（プラセボ 23% は一致） | 11 |
| ND-051 | カードの国内承認 DMD リストにオクレリズマブが含まれるが、ガイドライン自身の英語概要（PMID 39182455）の国内承認リストには含まれず、国内総説も「日本未承認」と明記。逆にグラチラマー酢酸塩がカードのリストにない。ガイドライン2023本文での再確認を要する | 14 |
| RO-016 | 喘息死亡率：カードは人口10万対 0.94 とするが、厚労省・人口動態統計の公表値は 0.9（分母の人口推計の取り方の違いによる値と考えられ、両値を記録） | 29 |
| FG-007 | 主出典のページが Crossref（105-114）と Europe PMC・カード（85-94）で異なる。並行出版の可能性があり、正本確認は登録側に委ねられた | 80 |

## 4. 監視事項一覧（72件）

主出典の後継版・後継文書が刊行済み、または承認・制度の変更でカードの前提が変わった件。次回改訂時の照合直し対象。

| 対象 | 後継・変更の内容 | バッチ |
|---|---|---|
| PH-010 | 令和8年度（2026年6月）診療報酬改定で CPAP 基準が AHI 15（PSG）／30（簡易）に変更済み。カードの 20／40 は改定前の基準 | 1 |
| NG 章（リナクロチドのカード） | DailyMed の現行ラベルで小児の対象が2歳以上に拡大（カードの6〜17歳は Rome V 刊行時点では正しい） | 4 |
| TJ-004 | 頭部外傷治療・管理ガイドライン第5版が2026-10-12に刊行 | 8 |
| RP-022・023・027・037 | PCOS の呼称が PMOS へ改称される動き（2026年国際コンセンサス） | 9 |
| BP-039〜044 | 膵癌診療ガイドライン2025年版（第7版）が刊行 | 12 |
| BP-069・070 | 膵・胆管合流異常診療ガイドライン改訂第2版（2024年9月）が刊行 | 12 |
| EY-019 | 円錐角膜グローバルコンセンサス第2版が公表 | 13 |
| EY-017 | TFOS DEWS III（2025年）がドライアイの定義を改訂（PMID 40451408）。カードは DEWS II 定義 | 13 |
| ND-003 | 『認知症疾患診療ガイドライン2026』が2026年5月に刊行（カードは2017年版への帰属を明示しており誤りではない） | 14 |
| ND-064 | ERC-ESICM の心停止後体温管理ガイドライン（2022年）が2021年版の体温管理の推奨を置き換え。カード後段の「32〜36℃を少なくとも24時間維持」は2021年版のまま | 14 |
| GY-015 | 子宮頸がん検診の指針に HPV 検査単独法が2024年4月に追加 | 16 |
| GY-016 | HPV ワクチンのキャッチアップ接種は2025年3月で終了し、2026年4月からは9価のみ | 16 |
| OS-020 | コラゲナーゼ（ザイアフレックス）は2020年に米国外で撤退し、国内では使用不可 | 17 |
| OS-019 | SONK が SIFK へ再定義された（用語の変更） | 17 |
| PG-047 | GBS スクリーニングの時期が産科編2026で36〜37週に変更 | 18 |
| DT-030・031・045 | 皮膚リンパ腫診療ガイドライン2025が刊行（英語サマリー PMID 41204060） | 20 |
| EP-035 | アトゲパントの急性期適応追加が2025年12月に申請 | 21 |
| EP-010 | セノバメートが2026年9月に国内承認 | 21 |
| EP-013〜016 | ジアゼパム点鼻液が2025年6月に承認 | 21 |
| OR 章（GAS 咽頭炎のカード） | IDSA の GAS 咽頭炎ガイドライン 2025年更新（Part 1）が公表 | 22 |
| DM-002・005・009・011・013・015・019 | 糖尿病診療ガイドライン2024が刊行（主出典 SRC-944 の7件は照合直しの対象） | 23 |
| DM-006・025・030・031・033 | ADA Standards of Care 2026 が公表 | 23 |
| VS-042〜046 | 肺血栓塞栓症診療ガイドライン2025（JCS/JPCPHS）が刊行 | 24 |
| GN-007・008・009 | KDIGO 2025 IgAN/IgAV ガイドラインが KDIGO 2021 の IgAN 章を更新 | 25 |
| GN-005・006・028 | KDIGO 2024 ANCA 関連血管炎ガイドライン（KDIGO 2021 の AAV 章の focused update。同ガイドライン自体は CC BY-NC-ND で根拠には使えない） | 25 |
| GN-036〜038 | Alport 症候群の2024年専門家ガイドラインが公表（CC BY） | 25 |
| GN-021 | 糖尿病性腎症の病期分類が2023年に改称 | 25 |
| SK-013 | WAO の遺伝性血管性浮腫ガイドライン2025年版で分類が再編 | 26 |
| RO-005・006・008・009・010・012・013 | 『COPD 診断と治療のためのガイドライン 第7版』（2026年3月）が刊行。主出典は第6版サマリー | 29 |
| RO-025 | 咳嗽・喀痰の診療ガイドライン2025年版が刊行（主出典は2019年版の英語ダイジェスト） | 29 |
| RO-016 | 成人喘息の JGL2024 が刊行（主出典は JGL2021 の英語要約） | 29 |
| EN-023・024／EX-014 | 原発性アルドステロン症診療ガイドライン2025年版が刊行され、2016年版を置き換え（DOI 10.1210/clinem/dgaf284、CC 表示なし）。カードの2016年基準は再照合が必要 | 30・84 |
| EN-016 | 尿崩症の呼称が AVP 欠損症／抵抗症（AVP-D／AVP-R）へ2022年に正式改称 | 30 |
| GU-043 | EAU の尿路外傷ガイドライン2026年版が全面再構成で刊行 | 31 |
| LC-048 | TNM 分類 第9版が運用開始 | 32 |
| MT-004 | ESC/EAS の脂質異常症 2025 Focused Update が公表 | 33 |
| MT-024〜026 | 痛風診療ガイドライン第3版の2022年追補版が公表 | 33 |
| MT-016 | AAP の2023年版ガイドラインが公表 | 33 |
| RC-028／KF-021・022 | 腎性貧血診療ガイドライン2025（JSDT）が刊行 | 36 |
| 腎性貧血関連カード | KDIGO の CKD 貧血ガイドライン2026が刊行 | 36 |
| RC-025 | 指定難病の診断基準が令和9年4月1日に一部改正予定 | 36 |
| TH-023・024・025 | 『骨粗鬆症の予防と治療ガイドライン2025年版』（2025年8月）が刊行。TH-023 は2012年の診断基準、TH-024・025 は2011年版準拠 | 37 |
| TH-013・014 | ATA 成人分化型甲状腺癌ガイドライン2025年版が刊行（Thyroid. 2025;35(8):841-985）。カードは ATA 2015 準拠 | 37 |
| HF-001 | Universal Definition（心不全の普遍的定義）第2版が2026年に刊行。固定の LVEF カットオフの見直しを提起（JCS/JHFS 2025 は第1版準拠） | 38 |
| HF-017 | フィネレノン（ケレンディア）が2025年12月に慢性心不全（LVEF 40%以上）の追加適応で国内承認。カードの uncertainty（国内承認状況は未確認）は PMDA 文書で解消できる | 38 |
| HF-025 | Impella は国内で「心原性ショック等の薬物療法抵抗性の急性心不全」を適応として承認済み。カードの uncertainty（国内での保険適用の条件は未確認）は解消できる見込み | 38 |
| XS-031〜033 | GLIM 基準の5年アップデートが2025年に公表（Clin Nutr 版は CC BY） | 40 |
| IH 章（ACS のカード） | 2025 ACC/AHA の ACS ガイドラインが刊行され、2013年 STEMI／2014年 NSTE-ACS を置き換え | 41 |
| IH 章（川崎病のカード） | AHA の川崎病ステートメント2024が公表 | 41 |
| IH 章（心筋梗塞の定義のカード） | 心筋梗塞の普遍的定義 第5版が2026年に刊行（CC BY） | 41 |
| NB-012 | 新生児慢性肺疾患について厚労科研班の新分類案（2023年）が公表 | 45 |
| SP-007 | 主出典（Thoomes 2018）の後継となる系統的レビュー2026年版が公表（CC BY、範囲はやや広い） | 47 |
| VD 章 | 2025 ESC/EACTS 弁膜症ガイドラインが刊行（MR の分類を機序ベースに再編等）。本章の基盤は JCS 2020 と ACC/AHA 2020 | 48 |
| VD-027〜032 | 感染性心内膜炎で Duke-ISCVID 基準（2023年）と ESC 2023 ガイドラインが刊行され、修正 Duke 基準は置き換わりつつある。カードは JCS 2017（修正 Duke 基準の時代）の内容 | 48 |
| NI-016・017 | 結核性髄膜炎の国際診療ガイドラインが刊行（Lancet Infect Dis. 2026、CC BY）。両カードの基盤（2010年コンセンサス／2004年 NEJM 試験）は旧い | 49 |
| NI-004 | HTLV-1関連脊髄症（HAM）診療ガイドライン2025が刊行（診断基準自体は現行基準と一致） | 49 |
| AR-020・022・029・030・031・032・034・035 | JCS/JHRS 2024 Guideline Focused Update on Management of Cardiac Arrhythmias が刊行（J Arrhythm. 2025;41(3):e70033）。主出典 SRC-181 は2019年版 | 52 |
| AR-011 | エドキサバン15mg の減量の用法・用量追加が2021年8月に国内承認済み。カードの uncertainty（国内承認の条件は未確認）は解消可能 | 52 |
| NM-011・012 | 多発性筋炎・皮膚筋炎診療ガイドライン2025の正式版が刊行 | 53 |
| AL-017 | 蕁麻疹の国際ガイドライン2026年版が刊行され CC BY（Allergy 2026;81(8):2582-2632）。次回改訂時に主出典の OPEN 化を推奨 | 60 |
| SA-017 | アミロイドーシスの ISA 命名法2024年版が刊行（カードは2022年版に基づく） | 63 |
| ID-015 | 後継の人口ベース研究（Haematologica 2025、CC BY-NC）が刊行。次回改訂時の置き換え候補 | 69 |
| BD-001 | 骨粗鬆症ガイドライン2025年版で診断基準の章が改訂されたかは未確認（TH 章の TH-023〜025 の照合直しとあわせて確認） | 74 |
| HV-011 | 後継の USPHS ガイドライン2025年版が刊行され、刊行版は CC BY。カードの骨格は不変で、次回改訂時の OPEN 化候補 | 76 |
| IE-002（SRC-1027 の後継） | Linglart ら 2026 の ISS 国際コンセンサス（CC BY）が SRC-1027 の後継文書。OPEN 化の候補（GR 章でも再掲） | 77・98 |
| FG-002・004 | 主出典（Denning 2024）の改訂版が出れば再照合の対象 | 80 |
| FG-010 | WHO 世界マラリア報告は年次更新されるため、数値の時点確認が要る | 80 |
| IG-017 | 後継調査（Chea ら 2026、NEJM）が刊行 | 85 |
| OG-004 | EULAR の SLE 推奨2023年更新版が刊行（自由利用ではない） | 92 |
| SM-004 | 禁煙治療手順書の現行版は第8.1版（2021年9月）。カードは第7版に基づいており、本文の照合直しが残る | 93 |
| CH-002〜005 | 成人先天性心疾患診療ガイドライン2025年改訂版が刊行（主出典 SRC-272 は2017年版） | 94 |
| MY-001 | WHO 結核ファクトシートが2026-11-12に2025年データへ更新（GTR 2026：発症1,060万人・死亡113万人・うち HIV 陽性13.7万人）。カードの値（発症1,070万人・死亡123万人）は引用した版（2024年データ、GTR 2025）と一致しており誤りではないが、次回改訂時は2025年データでの再照合が要る | 96 |


## 5. license_note 更新提案一覧（16件）

区分は変わらない（または区分訂正と連動する）が、出典マスターの注記文言が実態と異なる件。

| SRC | マスターの現行注記 | 実態 | バッチ |
|---|---|---|---|
| SRC-1027 | 「CC表示なし」 | 刊行版ライセンスは CC BY-NC-ND 4.0（区分訂正 第1-1節と連動） | 77（98で再掲） |
| SRC-2481 | 「未確認」 | CC BY-NC 3.0（区分訂正 第1-1節と連動） | 79 |
| SRC-1021 | 「ライセンス表示を確認できず」 | StatPearls の書籍レベルで CC BY-NC-ND 4.0 の表示がある（区分 RESTRICTED は正しい） | 82 |
| SRC-1022 | 「ライセンス表示を確認できず」 | 同上 | 82 |
| SRC-1023 | 「ライセンス表示を確認できず」 | 同上 | 82 |
| SRC-1049 | 「ライセンス表示を確認できず」 | 刊行版は CC BY-NC-ND 4.0 | 84 |
| SRC-1058 | 「ライセンス表示を確認できず」 | 刊行版は CC BY-NC-ND 4.0 | 84 |
| SRC-2196 | 「CCライセンス表示なし」 | 実際は CC BY-NC-ND 4.0 | 85 |
| SRC-3538 | カード側の source_license が「CC 表示なし」 | 実際は CC BY 3.0 IGO（WHO ステートメント。区分訂正 RESTRICTED→OPEN と連動） | 88 |
| SRC-4048 | カード側の source_license が「未確認」 | 実際は CC BY 4.0（区分訂正 UNKNOWN→OPEN と連動） | 91 |
| SRC-018 | 「種別は未確認」 | 刊行版は CC BY 4.0（区分訂正の再掲と連動） | 92（初出は7・10） |
| SRC-4801 | 「未確認」 | PMC 収載コピーは © Cochrane で CC の要素はない（区分訂正 UNKNOWN→RESTRICTED と連動） | 93 |
| SRC-234 | 注記が「著者最終稿」前提の文言 | 刊行版自体が CC BY-NC-ND。カードの uncertainty の「刊行版の表記は未確認」もあわせて解消できる | 94（48でも確認） |
| SRC-3092 | license_note が空欄 | CC BY-NC-ND 4.0 を Crossref の version-of-record で確認（WAO HAE 2025。区分 RESTRICTED は正しく、注記の補完提案） | 26 |
| SRC-384 | 「CC BY のアイコン表示はあるが版の表示なし」 | 実際は CC BY-NC（区分の明確化 第1-2節と連動） | 29 |
| SRC-628 | 注記のライセンス種別が実態と異なる | 実際は CC BY-NC-SA（注記の精緻化） | 50 |

## 6. 再調査候補一覧（21件）

### 6-1. 本文確認が環境要因でできず判定が保留になった件（5件）

| 対象 | 保留の内容 | バッチ |
|---|---|---|
| DL-011 | AHRQ Evidence Report No. 191 は実在するが、NCBI 側の reCAPTCHA で全文の確認ができず C とした。登録側で本文を確認できれば B に上がりうる | 58 |
| PX-011 | AHRQ Evidence Synthesis No. 201（Bookshelf NBK554654、GOV_US）は本文未確認のため候補に数えなかった。登録側で MMSE のプール値を確認できれば B に上がりうる | 89 |
| SB-003 | AHRQ Evidence Synthesis No. 171（NBK534916）は本文で AUDIT のカバー範囲を確認できず、候補に数えなかった | 95 |
| PH 章（Evidence Synthesis No. 223、NBK592805） | 米国政府著作物の public domain 表示がボット遮断で未目視のため留保した（MD-011 の尺度数値の裏づけ自体は確認済み） | 1 |
| PH-022〜024 の候補（Feltner 2022） | public domain の表示は検索インデックスの写しで確認したが、Bookshelf 本体は reCAPTCHA で遮断された。登録時に表示の目視再確認を推奨 | 100 |

### 6-2. 各バッチが再調査候補として明記した件（16件）

| 対象 | 理由の要約 | バッチ |
|---|---|---|
| VA-002・VA-012 | 候補の全文確認が尽くせず判定を持ち越した | 67 |
| VA-010 | 同上 | 67 |
| DV-003 | AAIDD の FAQ が定義を全文再掲するが自由なライセンスではないため、運用次第で再調査 | 68 |
| DV-016 | 候補の確認が尽くせず判定を持ち越した | 68 |
| ID-013 | 同上 | 69 |
| PB-003 | 学会文書が自由に読める形で公開されており、扱いの再調査候補 | 70 |
| RX-012 | 候補の確認が尽くせず判定を持ち越した | 71 |
| NX-008 | 同上 | 72 |
| BD-001・002・003・010 | 骨粗鬆症ガイドライン2025年版での診断基準の改訂有無が未確認で、確認後に再調査 | 74 |
| FT-001 | 主出典（ACOG 2025）がごく最近の刊行で、自由な全文の追随を待って再調査 | 75 |
| FT-003 | 同上 | 75 |
| FT-013 | 主出典（SMFM 2026）がごく最近の刊行で再調査候補 | 75 |
| HV-007 | 候補の確認が尽くせず判定を持ち越した | 76 |
| TX-019 | 同上 | 78 |
| BL-004 | 同上 | 79 |
| PD-003（FT-001 と同一出典 SRC-3341） | バッチ75の FT-001 と同じ主出典で、C の継続。再調査候補として再掲 | 88 |

## 7. 候補側の数値の使用注意

裏づけ登録の際に、候補側の数値をカードの値の裏づけとして使ってはいけないと各バッチで明記された件は、ほぼ全バッチに存在する（各バッチの明細表「数値照合」欄が正本）。典型は次の3型である。(1) 候補の値が別の集団・別の枠組み・別の時点の値で、方向は一致してもカードの点推定値の再掲ではないもの。(2) 登録レコード（ClinicalTrials.gov 等）の集計値が主出典の公表値と異なるもの。(3) 候補側の転記・要約の誤りの疑いがあり、カード（主出典）の値が正しいと確認されたもの。以下は代表例（25件）で、網羅的な一覧は各バッチの明細表と申し送りを参照されたい。

| 対象 | 使ってはいけない候補側の値・内容 | バッチ |
|---|---|---|
| VA-003・VA-011 | 候補（Takano ら 2026、CC BY）の基準表に転記誤り：MPA の cANCA/PR3 と好酸球の配点が原典と入れ替わり、高安動脈炎の腹部大動脈病変の配点も原典と異なる（原典＝カードの値が正しい）。該当セルを使わないこと | 67 |
| DV-013 | 候補の有病率 2〜2.5% はカードの約3% と厳密には一致しない。主出典の値が正 | 68 |
| RX-019 | 候補（Zimnoch ら 2025）の推奨要約表の「抜管後呼吸不全の予防・高リスク患者」の行は主出典（ERS/ATS 2017）と食い違う。カードは主出典どおりで正しく、該当行を使わないこと | 71 |
| NX-013 | 初圧の正常範囲が候補（10〜20 cmH2O＝100〜200 mmH2O）とカード（70〜180 mmH2O、主出典の値）で異なる。初圧の数値を使わないこと | 72 |
| BD-006 | FREEDOM の登録症例数：登録レコード 7,808例 vs カード（主出典 NEJM）7,868人。桁の転倒の疑いがあり主出典が正。登録レコードの症例数を使わないこと | 74 |
| BD-007 | 高カルシウム血症の頻度は定義が異なる（カードは臨床検査基準、登録レコードは有害事象ベース）。頻度の値を使わないこと | 74 |
| FT-014 | 候補（2024年）の2021年の死産率 5.73/1,000出生（約175件に1件）は、カードの「160件に1件」（ACOG 2020 の米国の値）と年次が異なる | 75 |
| TX-004 | 候補（Cureus 総説）の死亡率「最大20%」は未治療の文脈の値で、カードの「最大で約4%」とは枠組みが異なる | 78 |
| TX-001 | 第1段階の境界（50 mg/dL）の属する側が候補の表と主出典の対応表で異なる。カードは主出典どおりで正 | 78 |
| ML-004 | 登録レコードの HR 0.58・完全奏効 38.8% はカードの 0.66・36.7% と異なる | 81 |
| BR-014 | 候補の「1%」は別の統計量で、カードの値を裏づけない | 82 |
| EV-011 | 候補（CDC の ARS ページ）の線量区分の帯は主出典と大きく異なる（脳血管型：CDC は約50 Gy超、主出典は10〜20 Gy）。CDC 側の線量帯の数値を使わないこと | 83 |
| IG-006 | 候補の「3%以下」とカードの「3%未満」は境界の扱いが異なる | 85 |
| HX-010 | 候補の「受診200件に1件」は一般の受診を母数とする値で、カードの「救急外来受診の0.5%」とは枠組みが異なる | 86 |
| PD-002 | 候補の BPS 細分値（羊水ポケットによる細分）はカードの ACOG 式の閾値の裏づけに使わないこと | 88 |
| CM-004 | 候補の約190万人は視覚障害者数で、カードの「失明180万人」とは指標が異なる | 90 |
| OG-007 | 候補（Strijbos 2013）が引く HELP の効果量は別の HELP 報告に基づく値で、カードの原著数値とは異なる | 92 |
| SM-006 | GBD 2019 の COPD 有病者数（2億1,230万人）など、主出典と異なる値はカードの裏づけとして登録しないこと | 93 |
| CH-002・005・013 | 厚労科研の更新推計（2007年40万人・2022年57万人）、候補の10年生存率 90〜95%超、右室収縮末期容積係数 80 mL/m² は、いずれもカードの値と対象または値が異なる | 94 |
| SB-003・004 | SB-003 候補の感度90%・特異度80% は別の出典の値。SB-004 候補の「一般人口の2〜3倍」は別の枠組み | 95 |
| MY-001 | CDC の「未治療では10人に1人」は潜在性感染を分母とする別の枠組みで、カードの発症割合 5〜10% の裏づけにしないこと | 96 |
| GR-002 | 候補（特発性低身長の国際コンセンサス2026）の GH 刺激試験の閾値は候補側の値で、主出典の数値として登録しないこと | 98 |
| CT-013 | EULAR 全身性強皮症推奨の件数：カード・主出典は22件、候補（Front Immunol 2024）は21件。数え方の違いを含め、次回改訂時に主出典で再照合を推奨 | 61 |
| TR-018 | 前頭洞骨折のサーベイランス CT の時点の枠組みが現在の欧州のガイダンスとカードで異なる（両値を記録） | 54 |
| AX-018 | CC BY レビュー（Cureus 2023）の主要徴候の特異度は 86〜100% で、カードの 64〜100%（Daum 2014 の全徴候レンジ）とは下限が異なる | 1 |

## 8. 候補の新規登録が要る件（17件）

出典マスター未登録の候補で、新規 SRC 登録が見込まれるもの。採番は登録側で行う（バッチ1の方法注記のとおり、未登録候補は新規登録候補として扱い、棚卸し側では番号を付けていない）。

| 候補 | 備考 | バッチ |
|---|---|---|
| Feltner ら、AHRQ Evidence Synthesis No. 212（Bookshelf NBK578988、GOV_US／public domain） | SRC-4986 見込み。Bookshelf 版には PMID 35344311 がある（2026-11-11 の提案メモの「PMID なし」はこの点で訂正）。JAMA 版の PMID 35289875・DOI 10.1001/jama.2022.1807 は ©AMA 版のもので、候補に付けないこと。DOI・PMCID はない | 100 |
| WSES/EANS の脊髄損傷ガイドライン 2024（PMID 38238783） | 新規 SRC 登録候補として提案 | 47 |
| Pereira 2015 の WSES ポジションペーパー | 同上 | 47 |
| Uchida 2025（TJ-039 の候補） | 新規 SRC を提案 | 8 |
| Ferullo ら 2024（Brain Sci、CC BY） | ND-044 の裏づけ。新規 SRC 登録を提案 | 14 |
| ACOG Committee Opinion No. 797（PMID 31977793） | PG-047 の B 候補。新規登録の提案7件のうちの1件 | 18 |
| ATA 2026／RCOG 2025 の解説論文（Case Rep Womens Health 2026、CC BY、PMID 42698877） | PG-038 の B 候補 | 18 |
| 膜性判定の超音波研究（BMC Pregnancy Childbirth 2025、CC BY、PMID 40457254） | PG-020 の B 候補 | 18 |
| 妊婦貧血の Fiji 症例対照研究（BMC Pregnancy Childbirth 2026、CC BY、PMID 42410385） | PG-036 の B 候補 | 18 |
| ACOG Practice Bulletin No. 142（PMID 24451674） | PG-008 の B 候補 | 18 |
| Metoki 2022 の総説（PMID 35726086） | PG-009 の B 候補 | 18 |
| 厚生労働省告示第226号（GOV_JP） | PG-043 の B 候補 | 18 |
| EID 論文（PMID 21192886） | 出典マスター未登録を確認。新規登録候補 | 2 |
| NHSN プロトコル | 出典マスター未登録。新規登録候補 | 2 |
| Awad 2001 | 出典マスター未登録。新規登録候補 | 2 |
| Ohnishi 2011 | 出典マスター未登録。新規登録候補 | 2 |
| 厚生労働省のページ（RI-028 の候補） | 既登録の SRC-356（GOV_JP）の後継にあたる。差し替えとして扱うか新規登録かは登録側の判断に委ねられた | 46 |

## 集約中に気づいた不整合・留意点

- **区分訂正の方向の矛盾はなかった。** 全226件を通じ、同一 SRC に対して逆方向の訂正提案は存在しない。複数バッチで重なった提案（SRC-1020 がバッチ58・82、SRC-2825 がバッチ59・60、SRC-1026・1027 がバッチ77・98、SRC-1030 がバッチ77・87）はいずれも同じ方向の再掲だった。
- **SRC-018 は提案→反映→再掲の経過が追える。** バッチ7・10で UNKNOWN→OPEN を提案し、バッチ27の時点ではマスターに OPEN として反映済みであることを確認、バッチ92で再掲された。本メモでは初出をバッチ7として一本化した。
- **識別子の値の競合は1件（SRC-164 の PMCID）。** バッチ40の発見の併記順からは PMC8355884 が SRC-164 に帰属しうるが、同バッチの補完候補リストとバッチ79の個別照会で、SRC-164 の PMCID は PMC8515119、PMC8355884 は SRC-165 のものであることが確定している。第2節の表は確定値のみを掲載した。
- **Crossref のライセンス表示と刊行版の実態が食い違う例が複数ある**（SRC-234：Crossref は CC BY、刊行版は CC BY-NC-ND。バッチ48・94で一致した結論）。区分の判定は刊行版の表示を優先する従来の運用を、本メモでも前提とした。
- **明確化のうち3件は方向が未確定のままの申し送りである**（SRC-290 は同誌他記事からの推測段階、SRC-3444 は誌の方針と論文単位の表示が食い違う、SRC-4728 は CC 表示自体が存在しない）。第1-2節にその旨を明記して掲載した。
- **各バッチの D 件数の数え方に注意。** バッチ1〜47の成果物では、D 件数を「カード単位」で数えたバッチと「出典単位」が混在する（例：バッチ29の「D 7件」は7カード・3出典、バッチ39の「D 3件」は3カード・2出典）。本メモの第1節は出典単位に統一したため、各バッチの見出し件数とは一致しない場合がある。
- 本メモは集約のみを行い、カードの主張・数値および出典マスターへの変更は一切行っていない。
