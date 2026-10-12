# Phase 1：取り込みレポート（2026-10-12）

生成：`scripts/extract_yaml.py`。主張文と数値は変更していない。

## 0. 処理上の注意

- 原本の YAML には調査レポートの脚注マーカー（`\[n\]`）が混在しており、そのままでは YAML として読めない。文字列の外にあるマーカーは除去し、カードごとに番号を `history` に記録した。
- 文字列の内側にあったマーカー（2件）は、主張文を変えないよう `[n]` として残し、削除を `proposals/01_inline_citation_markers.md` で提案した。
- v1 は定義（`_pub`・`_cur`・`_src`）とカード列が同じブロックにあり、YAML として不正だったため、カード列を `_cards:` の下に入れて読み込んだ（アンカーと `<<:` は PyYAML で展開）。
- v1 の節見出し（`# ===== 1. GERD・NERD・Barrett食道 =====` など）を `subdomain` に入れた。パイロット版と v2 は `null`。
- `verifier` は原本ではすべて空文字だったため `null` にした。`created` は原本の値（2026-10-10）を保持した。
- **主張文の同一性チェック**：出力した 139 件の `plain_statement_ja` が、原本の中に一字一句そのまま存在するかを照合した（`\[`→`[` のみ許容）。不一致 0 件。

## 1. 件数

| 原本 | 抽出したカード数 |
|---|---|
| raw/00_pilot_hp_ug.md | 38 |
| raw/01a_esophagus_v1.md | 68 |
| raw/01b_esophagus_v2.md | 33 |

| 出力 | 件数 | 再読込 |
|---|---|---|
| data/facts/HP.yaml | 20 | 20 |
| data/facts/UG.yaml | 18 | 18 |
| data/facts/_staging_ES_v1.yaml | 68 | 68 |
| data/facts/_staging_ES_v2.yaml | 33 | 33 |
| data/sources/sources.yaml | 27 | — |

## 2. タグの変換

| 出力 | legal_basis | source_class | 件数 |
|---|---|---|---|
| HP.yaml | B | OPEN | 10 |
| HP.yaml | B | RESTRICTED | 6 |
| HP.yaml | B | UNKNOWN | 4 |
| UG.yaml | B | OPEN | 2 |
| UG.yaml | B | RESTRICTED | 10 |
| UG.yaml | B | UNKNOWN | 6 |
| _staging_ES_v1.yaml | B | OPEN | 24 |
| _staging_ES_v1.yaml | B | RESTRICTED | 29 |
| _staging_ES_v1.yaml | B | UNKNOWN | 15 |
| _staging_ES_v2.yaml | B | GOV_JP | 2 |
| _staging_ES_v2.yaml | B | OPEN | 5 |
| _staging_ES_v2.yaml | B | RESTRICTED | 15 |
| _staging_ES_v2.yaml | B | UNKNOWN | 11 |

### 2-1. パイロット版の source_class 判定（source_license の記載別）

判定規則：NC・ND・No commercial・©・Wiley・非CC のいずれかを含む → RESTRICTED。それ以外で「未確認」「要確認」を含む → UNKNOWN。CC BY／CC0 のみ → OPEN。

| source_license | source_class | 件数 | 該当ID |
|---|---|---|---|
| CC BY 4.0 | OPEN | 11 | HP-004, HP-005, HP-006, HP-007, HP-010, HP-011, HP-013, HP-015, HP-016, HP-019, UG-012 |
| CC BY 4.0（引用元） | OPEN | 1 | UG-013 |
| CC BY 4.0／NC | RESTRICTED | 1 | HP-020 |
| CC BY-NC 4.0 | RESTRICTED | 1 | HP-017 |
| CC BY-NC-ND 4.0 | RESTRICTED | 1 | HP-001 |
| No commercial re-use（CC BY-NC系、要確認） | RESTRICTED | 1 | HP-008 |
| Wiley標準条件 | RESTRICTED | 1 | UG-007 |
| Wiley標準条件／未確認 | RESTRICTED | 1 | UG-006 |
| © ACG | RESTRICTED | 6 | HP-012, UG-001, UG-002, UG-003, UG-005, UG-014 |
| © ACG（原典）／解説記事 CC BY 4.0 | RESTRICTED | 1 | HP-009 |
| © ACG（引用元） | RESTRICTED | 1 | UG-004 |
| 未確認／© ACG | RESTRICTED | 2 | UG-009, UG-011 |
| 引用元 CC BY 4.0／原著は要確認 | UNKNOWN | 1 | HP-014 |
| 政府統計（利用規約は要確認）／引用元 CC BY 4.0 | UNKNOWN | 1 | HP-018 |
| 未確認 | UNKNOWN | 7 | HP-003, UG-008, UG-010, UG-015, UG-016, UG-017, UG-018 |
| 未確認（PMCで無料公開、CC種別は未確認） | UNKNOWN | 1 | HP-002 |

## 3. 出典マスター（SRC）と source_ref

SRC表の ID は `SRC-01` 形式だったため、スキーマの `^SRC-[0-9]{3}$` に合わせて `SRC-001` 形式に正規化した（`legacy_id` に旧IDを保持）。

| 照合方法 | 件数 |
|---|---|
| none | 51 |
| keyword | 18 |
| identifier | 32 |

- identifier：カードの DOI・PMID・PMCID が SRC表の識別子と一致。
- keyword：識別子が一致せず、出典名のキーワード（スクリプト内 `SRC_KEYWORDS`）で1件に決まった。**人間の確認を推奨。**
- none：SRC表に該当がない（v1 の W番号の出典など）。source_ref は null。

| 原本 | ID | source_ref | 照合方法 | 他の候補 | source |
|---|---|---|---|---|---|
| 01a | ES-001 | — | none | — | Iwakiri K, et al. JSGE GERD guidelines 2021. J Gastroenterol 2022;57:2 |
| 01a | ES-002 | — | none | — | Iwakiri K, et al. JSGE GERD guidelines 2021. J Gastroenterol 2022;57:2 |
| 01a | ES-003 | — | none | — | Iwakiri K, et al. JSGE GERD guidelines 2021. J Gastroenterol 2022;57:2 |
| 01a | ES-004 | — | none | — | Iwakiri K, et al. JSGE GERD guidelines 2021. J Gastroenterol 2022;57:2 |
| 01a | ES-005 | — | none | — | Lundell LR, et al. Gut 1999 |
| 01a | ES-006 | — | none | — | Iwakiri K, et al. JSGE GERD guidelines 2021. J Gastroenterol 2022;57:2 |
| 01a | ES-007 | — | none | — | Iwakiri K, et al. JSGE GERD guidelines 2021. J Gastroenterol 2022;57:2 |
| 01a | ES-008 | — | none | — | 一次出典未取得（要補完） |
| 01a | ES-009 | — | none | — | 一次出典未取得（要補完） |
| 01a | ES-010 | — | none | — | Iwakiri K, et al. JSGE GERD guidelines 2021. J Gastroenterol 2022;57:2 |
| 01a | ES-011 | — | none | — | Iwakiri K, et al. JSGE GERD guidelines 2021. J Gastroenterol 2022;57:2 |
| 01a | ES-012 | — | none | — | Japanese Classification of Esophageal Cancer 12th ed. Part I. Esophagu |
| 01a | ES-013 | — | none | — | Shaheen NJ, et al. ACG Barrett's Esophagus guideline. Am J Gastroenter |
| 01a | ES-014 | — | none | — | Shaheen NJ, et al. ACG Barrett's Esophagus guideline. Am J Gastroenter |
| 01a | ES-015 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-016 | — | none | — | Shaheen NJ, et al. ACG Barrett's Esophagus guideline. Am J Gastroenter |
| 01a | ES-017 | — | none | — | Shaheen NJ, et al. ACG Barrett's Esophagus guideline. Am J Gastroenter |
| 01a | ES-018 | — | none | — | ACG Clinical Guideline: EoE. Am J Gastroenterol 2025 |
| 01a | ES-019 | — | none | — | Dellon ES, et al. AGREE conference. Gastroenterology 2018 |
| 01a | ES-020 | — | none | — | Clinical and endoscopic characteristics of EoE in Japan: a case-contro |
| 01a | ES-021 | — | none | — | 一次出典未取得（要補完） |
| 01a | ES-022 | — | none | — | ACG Clinical Guideline: EoE. Am J Gastroenterol 2025 |
| 01a | ES-023 | SRC-026 | keyword | — | Dellon ES, et al. Dupilumab in EoE. N Engl J Med 2022;387:2317-2330 |
| 01a | ES-024 | — | none | — | 一次出典未取得（要補完） |
| 01a | ES-025 | SRC-011 | identifier(SRC-011:pmcid) | — | Yadlapati R, et al. Chicago Classification v4.0. Neurogastroenterol Mo |
| 01a | ES-026 | SRC-011 | identifier(SRC-011:pmcid) | — | Yadlapati R, et al. Chicago Classification v4.0. Neurogastroenterol Mo |
| 01a | ES-027 | SRC-011 | identifier(SRC-011:pmcid) | — | Yadlapati R, et al. Chicago Classification v4.0. Neurogastroenterol Mo |
| 01a | ES-028 | SRC-011 | identifier(SRC-011:pmcid) | — | Yadlapati R, et al. Chicago Classification v4.0. Neurogastroenterol Mo |
| 01a | ES-029 | SRC-011 | identifier(SRC-011:pmcid) | — | Yadlapati R, et al. Chicago Classification v4.0. Neurogastroenterol Mo |
| 01a | ES-030 | SRC-011 | identifier(SRC-011:pmcid) | — | Yadlapati R, et al. Chicago Classification v4.0. Neurogastroenterol Mo |
| 01a | ES-031 | SRC-011 | identifier(SRC-011:pmcid) | — | Yadlapati R, et al. Chicago Classification v4.0. Neurogastroenterol Mo |
| 01a | ES-032 | SRC-025 | keyword | — | Werner YB, et al. POEM vs LHM. N Engl J Med 2019;381:2219-2229 |
| 01a | ES-033 | SRC-025 | keyword | — | Werner YB, et al. POEM vs LHM. N Engl J Med 2019;381:2219-2229 |
| 01a | ES-034 | — | none | — | 一次出典未取得（要補完） |
| 01a | ES-035 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-036 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-037 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-038 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-039 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-040 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-041 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-042 | — | none | — | 一次出典未取得（要補完） |
| 01a | ES-043 | — | none | — | Japanese Classification of Esophageal Cancer 12th ed. Part I. Esophagu |
| 01a | ES-044 | — | none | — | Japanese Classification of Esophageal Cancer 12th ed. Part I. Esophagu |
| 01a | ES-045 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-046 | SRC-006 | keyword | — | Ishihara R, et al. JGES ESD/EMR guidelines for esophageal cancer. Dig  |
| 01a | ES-047 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-048 | — | none | — | Japanese Classification of Esophageal Cancer 12th ed. Part I. Esophagu |
| 01a | ES-049 | SRC-001 | keyword | — | Kato K, et al. JCOG1109 NExT. Lancet 2024;404:55-66 |
| 01a | ES-050 | SRC-001 | keyword | — | Kato K, et al. JCOG1109 NExT. Lancet 2024;404:55-66 |
| 01a | ES-051 | SRC-002 | identifier(SRC-002:doi) | — | Kelly RJ, et al. CheckMate 577. N Engl J Med 2021;384:1191-1203 |
| 01a | ES-052 | SRC-003 | identifier(SRC-003:doi) | — | Doki Y, et al. CheckMate 648. N Engl J Med 2022;386:449-462 |
| 01a | ES-053 | SRC-004 | keyword | — | Sun JM, et al. KEYNOTE-590. Lancet 2021;398:759-771 |
| 01a | ES-054 | SRC-005 | keyword | — | KEYNOTE-590 5-year follow-up. ESMO Open 2025 |
| 01a | ES-055 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-056 | — | none | — | Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part |
| 01a | ES-057 | — | none | — | Kaplan DE, et al. AASLD Practice Guidance, portal hypertension and var |
| 01a | ES-058 | — | none | — | Kaplan DE, et al. AASLD Practice Guidance, portal hypertension and var |
| 01a | ES-059 | — | none | — | Kaplan DE, et al. AASLD Practice Guidance, portal hypertension and var |
| 01a | ES-060 | — | none | — | Kaplan DE, et al. AASLD Practice Guidance, portal hypertension and var |
| 01a | ES-061 | — | none | — | 一次出典未取得（要補完） |
| 01a | ES-062 | SRC-007 | keyword | — | de Franchis R, et al. Baveno VII. J Hepatol 2022;76:959-974 |
| 01a | ES-063 | SRC-027 | keyword | — | Villanueva C, et al. N Engl J Med 2013;368:11-21 |
| 01a | ES-064 | SRC-007 | keyword | — | de Franchis R, et al. Baveno VII. J Hepatol 2022;76:959-974 |
| 01a | ES-065 | — | none | — | García-Pagán JC, et al. N Engl J Med 2010;362:2370-2379 |
| 01a | ES-066 | — | none | — | 一次出典未取得（要補完） |
| 01a | ES-067 | — | none | — | 一次出典未取得（要補完） |
| 01a | ES-068 | — | none | — | 一次出典未取得（要補完） |
| 01b | ES-R01 | SRC-001 | identifier(SRC-001:pmid) | — | Kato K, et al. JCOG1109 NExT. Lancet 2024;404(10447):55-66 |
| 01b | ES-R02 | SRC-002 | identifier(SRC-002:doi) | — | Kelly RJ, et al. CheckMate 577. NEJM 2021;384:1191-1203。OS: JCO 2025;4 |
| 01b | ES-R03 | SRC-003 | identifier(SRC-003:doi) | — | Doki Y, et al. CheckMate 648. NEJM 2022;386:449-462 |
| 01b | ES-R04 | SRC-004 | identifier(SRC-004:pmid) | SRC-005 | Sun JM, Lancet 2021;398:759-771。Metges JP, ESMO Open 2025;10(12):10585 |
| 01b | ES-R05 | SRC-016 | keyword | — | 小野薬品工業・BMS 食道癌適正使用委員会 文書（2021-11-26） |
| 01b | ES-R06 | SRC-025 | identifier(SRC-025:pmid) | — | Werner YB, et al. NEJM 2019;381:2219-2229 |
| 01b | ES-R07 | SRC-026 | identifier(SRC-026:pmid) | — | Dellon ES, et al. NEJM 2022;387:2317-2330 |
| 01b | ES-R08 | — | none | — | デュピクセント 医薬品インタビューフォーム（2026年3月改訂 第20版）、サノフィ国内申請報道 |
| 01b | ES-R09 | — | none | — | 慶應義塾大学病院 KOMPAS 好酸球性消化管疾患（2024年5月） |
| 01b | ES-R10 | SRC-027 | identifier(SRC-027:pmid) | — | Villanueva C, et al. NEJM 2013;368(1):11-21 |
| 01b | ES-R11 | — | none | — | García-Pagán JC, et al. NEJM 2010 |
| 01b | ES-R12 | SRC-010 | identifier(SRC-010:doi) | — | Gyawali CP, et al. Updates to the modern diagnosis of GERD: Lyon conse |
| 01b | ES-R13 | SRC-011 | identifier(SRC-011:pmcid) | — | Yadlapati R, et al. Chicago Classification v4.0. Neurogastroenterol Mo |
| 01b | ES-R14 | SRC-011 | identifier(SRC-011:pmcid) | — | Chicago Classification v4.0（PMC8034247） |
| 01b | ES-R15 | SRC-012 | identifier(SRC-012:doi) | — | Brooks PJ, et al. The alcohol flushing response. PLoS Med 2009;6(3):e1 |
| 01b | ES-R16 | SRC-014 | keyword | — | 国立がん研究センター がん情報サービス 食道（罹患2026年3月23日更新、死亡2026年1月7日更新） |
| 01b | ES-R17 | SRC-017 | keyword | — | 日本門脈圧亢進症学会 門脈圧亢進症取扱い規約 第3版（記載基準表を日消誌116(5):395、日内会誌103(5):1187で確認） |
| 01b | ES-R18 | SRC-018 | identifier(SRC-018:pmcid) | — | Yoshiji H, et al. Evidence-based clinical practice guidelines for Live |
| 01b | ES-R19 | SRC-015 | keyword | — | 診療報酬点数表 K653-6（令和4年新設） |
| 01b | ES-069 | SRC-009 | identifier(SRC-009:pmid) | — | Birk M, et al. ESGE Clinical Guideline. Endoscopy 2016;48:489-496（推奨7） |
| 01b | ES-070 | SRC-009 | identifier(SRC-009:pmid) | — | ESGE異物GL 2016（推奨7・10） |
| 01b | ES-071 | SRC-009 | identifier(SRC-009:pmid) | — | ESGE異物GL 2016（推奨11） |
| 01b | ES-072 | SRC-009 | identifier(SRC-009:pmid) | — | ESGE異物GL 2016（推奨8） |
| 01b | ES-073 | SRC-020 | keyword | — | Contini S, Scarpignato C. Caustic injury of the upper GI tract: a comp |
| 01b | ES-074 | SRC-021 | identifier(SRC-021:pmcid) | — | Cheng HT, et al. Caustic ingestion in adults. BMC Gastroenterol 2008（表 |
| 01b | ES-075 | SRC-020 | keyword | — | Contini 2013 WJG |
| 01b | ES-079 | SRC-023 | identifier(SRC-023:pmcid) | — | Esophageal CMV and HSV co-infection: case report and review. IDCases 2 |
| 01b | ES-080 | SRC-024 | identifier(SRC-024:doi) | — | Can endoscopists differentiate CMV esophagitis from HSV esophagitis? M |
| 01b | ES-081 | SRC-024 | identifier(SRC-024:doi) | — | Medicine 2019（確定診断後の治療薬） |
| 01b | ES-085 | SRC-022 | identifier(SRC-022:pmcid) | — | Boerhaave Syndrome—Narrative Review. Diagnostics 2025;15(19):2463 |
| 01b | ES-086 | SRC-022 | identifier(SRC-022:pmcid) | — | Diagnostics 2025;15(19):2463 |
| 01b | ES-087 | SRC-022 | identifier(SRC-022:pmcid) | — | Diagnostics 2025;15(19):2463 |
| 01b | ES-089 | SRC-006 | keyword | — | 要確認（JGES食道ESD/EMR GL 2020＝B、本文の該当CQを未照合） |

どのカードからも参照されなかった SRC：SRC-008, SRC-013, SRC-019

## 4. 識別子の null 化

| ID | 内容 |
|---|---|
| UG-004 | DOIは原本で「要確認」のためnull |
| ES-001 | PMIDは原本で「要確認」のためnull |
| ES-002 | PMIDは原本で「要確認」のためnull |
| ES-003 | PMIDは原本で「要確認」のためnull |
| ES-004 | PMIDは原本で「要確認」のためnull |
| ES-005 | DOIは原本で「要確認」のためnull／PMIDは原本で「要確認」のためnull |
| ES-006 | PMIDは原本で「要確認」のためnull |
| ES-007 | PMIDは原本で「要確認」のためnull |
| ES-010 | PMIDは原本で「要確認」のためnull |
| ES-011 | PMIDは原本で「要確認」のためnull |
| ES-013 | PMIDは原本で「要確認」のためnull |
| ES-014 | PMIDは原本で「要確認」のためnull |
| ES-016 | PMIDは原本で「要確認」のためnull |
| ES-017 | PMIDは原本で「要確認」のためnull |
| ES-018 | PMIDは原本で「要確認」のためnull |
| ES-019 | DOIは原本で「要確認」のためnull／PMIDは原本で「要確認」のためnull |
| ES-020 | DOIは原本で「要確認」のためnull／PMCIDは原本で「要確認」のためnull |
| ES-022 | PMIDは原本で「要確認」のためnull |
| ES-023 | PMIDは未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除） |
| ES-032 | PMIDは未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除） |
| ES-033 | PMIDは未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除） |
| ES-046 | PMIDは未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除） |
| ES-049 | PMIDは未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除） |
| ES-050 | PMIDは未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除） |
| ES-051 | PMIDは未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除） |
| ES-052 | PMIDは未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除） |
| ES-053 | PMIDは未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除） |
| ES-054 | DOIは原本で「要確認」のためnull／PMIDは原本で「要確認」のためnull |
| ES-062 | PMCIDは原本で「要確認」のためnull |
| ES-063 | PMIDは未照合のためnull（原本の記憶由来の候補値は CLAUDE.md 1-3 により削除） |
| ES-064 | PMCIDは原本で「要確認」のためnull |

## 5. 人間の確認が必要な項目

| ID | 内容 |
|---|---|
| HP-009 | source_license が複合記載（原典と引用元が混在）。source_class の判定を人間が確認 |
| HP-014 | source_license が複合記載（原典と引用元が混在）。source_class の判定を人間が確認 |
| HP-018 | source_license が複合記載（原典と引用元が混在）。source_class の判定を人間が確認 |
| HP-020 | source_license が複合記載（原典と引用元が混在）。source_class の判定を人間が確認 |
| UG-004 | source_license が複合記載（原典と引用元が混在）。source_class の判定を人間が確認 |
| UG-006 | source_license が複合記載（原典と引用元が混在）。source_class の判定を人間が確認 |
| UG-009 | source_license が複合記載（原典と引用元が混在）。source_class の判定を人間が確認 |
| UG-011 | source_license が複合記載（原典と引用元が混在）。source_class の判定を人間が確認 |
| UG-013 | source_license が複合記載（原典と引用元が混在）。source_class の判定を人間が確認 |
| ES-029 | 文字列内に脚注マーカー [30] が残っている（proposals/01_inline_citation_markers.md） |
| ES-064 | 文字列内に脚注マーカー [68][69] が残っている（proposals/01_inline_citation_markers.md） |
| ES-R01 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R02 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R04 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R05 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R10 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R12 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R13 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R15 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R16 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R17 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R18 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-R19 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-069 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-070 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-071 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-072 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-073 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-074 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-075 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-079 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-080 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-081 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-085 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| ES-086 | 原本（claude.ai 調査ラウンド）で status: verified_sources。本リポジトリのAPI照合（Phase 3）は未実施 |
| UG-006 | doi に複数の値「10.1111/den.15019; 10.1055/a-1369-5274」。Phase 3 の照合前に主たる DOI を決める必要がある |
| UG-008 | doi に複数の値「10.1055/s-0034-1393172; 10.1055/a-2863-8314」。Phase 3 の照合前に主たる DOI を決める必要がある |

## 6. スキーマ違反

### HP.yaml（0件）

なし

### UG.yaml（0件）

なし

### _staging_ES_v1.yaml（0件）

なし

### _staging_ES_v2.yaml（19件）

| 違反の種類 | 件数 |
|---|---|
| id: '…' does not match '…' | 19 |

<details><summary>全件</summary>

- ES-R01: id: 'ES-R01' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R02: id: 'ES-R02' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R03: id: 'ES-R03' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R04: id: 'ES-R04' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R05: id: 'ES-R05' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R06: id: 'ES-R06' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R07: id: 'ES-R07' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R08: id: 'ES-R08' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R09: id: 'ES-R09' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R10: id: 'ES-R10' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R11: id: 'ES-R11' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R12: id: 'ES-R12' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R13: id: 'ES-R13' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R14: id: 'ES-R14' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R15: id: 'ES-R15' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R16: id: 'ES-R16' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R17: id: 'ES-R17' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R18: id: 'ES-R18' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'
- ES-R19: id: 'ES-R19' does not match '^(HP|UG|ES|GD|IN|LV|BP|AB|XS)-[0-9]{3}$'

</details>

