# バッチ92：OG（症状性を含む器質性精神障害）6件

- 実施日：2026-11-15
- 対象：OG 章の対象カード全6件（OG-001・OG-002・OG-003・OG-004・OG-005・OG-007）
- ルール：2026-11-11 のレポジトリ側指示に基づく新ルール（抄録・添付文書・医学百科は根拠にしない。使えるのは政府の全文文書・報告書、CC BY 全文、試験登録レコードなど全文で読める資料のみ。旧来の「先例に基づく A」は廃止）を適用。
- 方法：各カードの主出典（マスター SRC）の刊行版ライセンスを Crossref の版（version of record）データと Europe PMC の個別レコードで1件ずつ確認し、必要に応じて PMC 全文のライセンス要素でも照合した。候補は CC BY 全文を実際に読んで裏づけ範囲を判定し、ライセンスは候補ごとに個別確認した。識別子（PMID・PMCID・DOI・巻・ページ）は一括照会の値を使わず、DOI キーと PMID キーの個別照会で相互に確かめた。出典の説明はマスター（repo_current2 の sources.yaml）の記載からそのまま取った。Crossref が途中でレート制限（429）を返したため、候補の Crossref 照会は見送り、Europe PMC の個別レコードと PMC 全文のライセンス要素で代替確認した（申し送り参照）。

## 集計

- A：1件（OG-003。主出典自体が刊行版で CC BY 4.0）
- B：5件（すべて部分）
- C：0件
- D（マスターの区分訂正）：新規1出典（UNKNOWN → RESTRICTED）、再掲1出典（UNKNOWN → OPEN、バッチ7・10で提案済み）

## 明細

| 対象 | 判定 | 現行出典（主出典） | 候補 | 区分 | PMID | DOI | PMCID | ライセンス根拠URL | 裏づけ範囲 | 数値照合 | 備考 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| OG-001 | B（部分） | SRC-1684：Galvin R, Bråthen G, Ivashynka A, et al. EFNS guidelines for diagnosis, therapy and prevention of Wernicke encephalopathy. Eur J Neurol. 2010;17(12):1408-1418 | Li S, Xing C, et al. Wernicke encephalopathy: a mini review of the clinical spectrum, atypical manifestations, and diagnostic challenges. Front Neurol. 2025;16:1566366 | OPEN | 40740851 | 10.3389/fneur.2025.1566366 | PMC12307376 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補は EFNS 2010 の診断基準を「(1) 食事欠乏、(2) 眼徴候、(3) 小脳機能障害、(4) 精神状態の異常または記憶障害」の4項目として列挙し「4項目のうち少なくとも2つを満たせば疑いが高まる」と再掲する。治療についても EFNS 推奨として「静注ビタミンB1 200 mg を1日3回」「炭水化物の使用前に補充する」を再掲し、古典的三徴への依存による見逃し・診断の遅れと剖検での有病率（0.4〜2.8%）にも触れる。推奨レベル（診断はレベルB、チアミン投与はレベルC）の格付け自体は再掲されない | 一致：4徴のうち2つ以上、チアミン静注200 mg・1日3回、炭水化物投与前という要素はいずれも候補の再掲と一致 | 主出典の刊行版ライセンスは Crossref で Wiley の利用条件のみ、Europe PMC でも非 OA・ライセンス表示なしのため、UNKNOWN → RESTRICTED への区分訂正を提案する（区分訂正の節参照）。カード自体は廃止済みで ND-037 に統合されているが、targets.json の対象として棚卸しした。候補のライセンスは Europe PMC の個別レコード（cc by）と PMC 全文のライセンス要素（CC BY 4.0）で個別確認した（Crossref は 429 のため見送り、申し送り参照） |
| OG-002 | B（部分） | SRC-1666：日本神経学会（監修）, 「パーキンソン病診療ガイドライン」作成委員会（編）. パーキンソン病診療ガイドライン2018. 医学書院; 2018 | Seppi K, Ray Chaudhuri K, Coelho M, Fox SH, Katzenschlager R, Perez Lloret S, Weintraub D, Sampaio C, et al.; Movement Disorder Society Evidence-Based Medicine Committee. Update on treatments for nonmotor symptoms of Parkinson's disease—an evidence-based medicine review. Mov Disord. 2019;34(2):180-198 | OPEN | 30653247 | 10.1002/mds.27602 | PMC6916382 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補（国際運動障害学会の根拠に基づく医療レビュー）は、非運動症状のうち神経精神症状として、うつ・不安、無為、精神病、衝動制御障害、認知症、認知機能障害を証拠レビューの対象範囲として明示し、これらの症状の「高い有病率と悪影響」、非運動症状が「パーキンソン病の病的状態の全体的な負担を増す」ことを述べる。精神病については Parkinson 病精神病の幻覚・妄想への言及があり、管理は「誘因・寄与因子の評価と、現在の抗パーキンソン病治療の厳密な見直し」に基づくとされる。せん妄との鑑別、認知症との鑑別の進め方そのものと、日本のガイドライン2018 の位置づけは再掲されない | 数値なし（症状の範囲と位置づけで照合した） | 主出典は書籍（医学書院）で、現行 RESTRICTED が正しい。候補のライセンスは Europe PMC の個別レコード（cc by）と PMC 全文のライセンス要素（CC BY 4.0）で個別確認した（Crossref は 429 のため見送り、申し送り参照） |
| OG-003 | A（主出典自体が自由） | SRC-018：Yoshiji H, et al. Evidence-based clinical practice guidelines for Liver Cirrhosis 2020. J Gastroenterol 2021;56:593-619 | 主出典自体（刊行版が CC BY 4.0 で公開） | OPEN | 34231046 | 10.1007/s00535-021-01788-x | PMC8280040 | https://creativecommons.org/licenses/by/4.0/ | 全面：主出典の刊行版自体が CC BY 4.0 で公開されており、ガイドライン本文は肝性脳症を肝硬変の合併症の一つとして診断と治療を扱うことを明記する。カードの主張（肝性脳症の位置づけと病像の幅）はその全文に直接基づく。置き換え候補の追加ではなく、主出典の区分訂正で足りる | 数値なし（カードの主張は主出典全文と対応する） | 刊行版ライセンスを3経路で個別確認した：Crossref の版データに CC BY 4.0（version of record）、Europe PMC の個別レコードで license: cc by、PMC 全文（PMC8280040）のライセンス要素に Creative Commons Attribution 4.0 の明記。カード側の provenance は既に OPEN・CC BY と記載されており、マスター側の区分訂正（UNKNOWN → OPEN）と識別子補完（DOI・PMID）はバッチ7（GD）・バッチ10（LV）で提案済みのため再掲とし、二重計上しない |
| OG-004 | B（部分） | SRC-3611：Bertsias GK, Ioannidis JP, Aringer M, et al. EULAR recommendations for the management of systemic lupus erythematosus with neuropsychiatric manifestations: report of a task force of the EULAR standing committee for clinical affairs. Ann Rheum Dis. 2010;69(12):2074-2082 | El Natour D, Makkieh Y, El Shaar T, El Natour H. Updates in Neuropsychiatric Systemic Lupus Erythematosus: Advances in Pathogenesis, Diagnosis, and Therapies. Cureus. 2026;18(10):e117661 | OPEN | 43001103 | 10.7759/cureus.117661 | PMC13744614 | https://creativecommons.org/licenses/by/4.0/ | 部分：候補は精神神経SLEの19の症候群（ACR 分類）を中枢・末梢別に列挙し、脳血管障害、けいれん、認知機能障害、気分障害、精神病、急性錯乱状態を含むこと、主な臨床像として頭痛・気分障害・けいれん・認知機能障害・脳血管障害を挙げる。診断については「他の病因・二次的原因を厳密に除外した後に初めて精神神経SLEに帰属させる」「感染症・代謝異常・薬剤性の模倣病態を除外することが診断の中心」と再掲し、SLE でない原因との鑑別を進める進め方を裏づける。カードの頻度区分（累積頻度5%超と1〜5%の切り分け）そのものは再掲されない | 頻度区分（5%超：脳血管障害・けいれん、1〜5%：重度の認知機能障害・大うつ病・急性錯乱状態・精神病）は自由な全文で再掲されず照合できない。候補の有病率（前向き研究44.5%、回顧的研究17.6%）は別の指標であり、カードの頻度区分の裏づけとして登録しないこと | 主出典の刊行版ライセンスは Crossref で Elsevier の OA ユーザーライセンス（open-access/userlicense/1.0）とテキストマイニング用ライセンスのみで CC ではなく（バッチ72 の先例どおり Elsevier OA ユーザーライセンスは自由とみなさない）、Europe PMC でも非 OA・ライセンス表示なしのため、現行 RESTRICTED が正しい。候補のライセンスは Europe PMC の個別レコード（cc by）と PMC 全文のライセンス要素（CC BY 4.0）で個別確認した（Crossref は 429 のため見送り、申し送り参照） |
| OG-005 | B（部分） | SRC-3612：Oh ES, Fong TG, Hshieh TT, Inouye SK. Delirium in Older Persons: Advances in Diagnosis and Treatment. JAMA. 2017;318(12):1161-1174 | Jeyakanthan J, Corso G, Woldetsadik B, Kotilo S, Esan O. Delirium in Hospitalized Older Adults: A Narrative Review. Cureus. 2026;18(5):e109991／Bellelli G, Morandi A, Davis DH, et al. Validation of the 4AT, a new instrument for rapid delirium screening: a study in 234 hospitalised older people. Age Ageing. 2014;43(4):496-502（既登録 SRC-3613、OPEN） | OPEN／OPEN | 42382898／24590568 | 10.7759/cureus.109991／10.1093/ageing/afu021 | PMC13318095／PMC4066613 | https://creativecommons.org/licenses/by/4.0/／https://creativecommons.org/licenses/by/3.0/ | 部分：Cureus 2026 総説は、せん妄を「注意・意識・認知の急性の障害」と定義し、死亡率上昇を含む重篤な転帰と関連すること、臨床現場で認識されにくい（特に低活動型）ことを再掲する。管理については「多面的で主に非薬理学的なアプローチ」が基盤であり、HELP が認知機能障害・不動・脱水・感覚喪失・睡眠障害の修正可能なリスク因子を対象とすることを述べ、抗精神病薬は「患者や他者への差し迫ったリスクがある重度の興奮」に限り最終手段として慎重に使うべきとする。SRC-3613（4AT 検証研究、既登録 OPEN）は、短時間の評価ツールとしての 4AT の要素を担う。3分間診断評価（3D-CAM）、家族による評価（FAM-CAM）、重症度尺度（CAM-S）の個別の整備状況は自由な全文で再掲されない | 数値なし（定義・管理の骨格で照合した） | 主出典の刊行版は Crossref でライセンス登録がなく、PMC 収載コピー（PMC5717753、著者稿）のライセンス要素もテキストマイニングとフェアユースへの言及にとどまり CC ではないため、現行 RESTRICTED が正しい。候補のライセンスは Europe PMC の個別レコード（いずれも cc by）と PMC 全文のライセンス要素（CC BY 4.0／CC BY 3.0）で個別確認した（Crossref は 429 のため見送り、申し送り参照） |
| OG-007 | B（部分） | SRC-3614：Inouye SK, Bogardus ST Jr, Charpentier PA, et al. A multicomponent intervention to prevent delirium in hospitalized older patients. N Engl J Med. 1999;340(9):669-676 | Strijbos MJ, Steunenberg B, van der Mast RC, Inouye SK, Schuurmans MJ. Design and methods of the Hospital Elder Life Program (HELP), a multicomponent targeted intervention to prevent delirium in hospitalized older patients: efficacy and cost-effectiveness in Dutch health care. BMC Geriatr. 2013;13:78 | OPEN | 23879226 | 10.1186/1471-2318-13-78 | PMC3724594 | https://creativecommons.org/licenses/by/2.0/ | 部分：候補（HELP の実施プロトコル論文）は、HELP が「せん妄の6つの重要なリスク因子を対象とする標準化されたプロトコル」を提供し、その6因子が認知機能障害、睡眠不足、不動、視覚障害、聴覚障害、脱水であることをカードと同一の構成で再掲する。原著の試験数値（対象852人、発症9.9%対15.0%、マッチドオッズ比0.60、せん妄の総日数とエピソード数の有意な減少）は再掲されない | 原著の数値（852人、9.9%対15.0%、オッズ比0.60）は自由な全文で再掲されず照合できない。候補が引く HELP の効果量（絶対率低下14.4%、相対リスク低下35.3%）は別の HELP 報告に基づく値であり、カードの数値の裏づけとして登録しないこと | 主出典の刊行版は Crossref でライセンス登録がなく、Europe PMC でも非 OA・ライセンス表示なしのため、現行 RESTRICTED が正しい。候補のライセンスは Europe PMC の個別レコード（cc by）と PMC 全文のライセンス要素（CC BY 2.0）で個別確認した（Crossref は 429 のため見送り、申し送り参照） |

## D（マスターの区分訂正）：新規1出典＋再掲1出典

- SRC-1684（OG-001 の主出典）：UNKNOWN → RESTRICTED。Eur J Neurol（Wiley）。Crossref の刊行版（version of record）ライセンスは Wiley の利用条件（termsAndConditions#vor）のみで CC ではない。Europe PMC の個別レコードでも非 OA（isOpenAccess: N）・ライセンス表示なし、PMC 未収載。マスターの license_note は null で実態との食い違いはない
- SRC-018（OG-003 の主出典）：UNKNOWN → OPEN。J Gastroenterol（Springer）。刊行版ライセンスを3経路で個別確認し、いずれも CC BY 4.0：Crossref の版データに CC BY 4.0（version of record、2021-07-07 開始）、Europe PMC の個別レコードで license: cc by、PMC 全文（PMC8280040）のライセンス要素に Creative Commons Attribution 4.0 International License の明記（著作権表示は © The Author(s) 2021）。マスターの license_note「種別は未確認」は実態と異なるため、あわせて更新を提案する（これもバッチ7・10の申し送りと同一）

- 訂正対象でない主出典の確認：SRC-1666（OG-002）は書籍（医学書院、2018）で現行 RESTRICTED が正しい。SRC-3611（OG-004）は Crossref の刊行版ライセンスが Elsevier の OA ユーザーライセンスとテキストマイニング用ライセンスのみで CC ではなく（バッチ72 の先例どおり）、現行 RESTRICTED が正しい。SRC-3612（OG-005）は Crossref でライセンス登録がなく、PMC 収載コピー（著者稿）のライセンス要素もテキストマイニングとフェアユースへの言及にとどまるため、現行 RESTRICTED が正しい。SRC-3614（OG-007）は Crossref でライセンス登録がなく Europe PMC でも非 OA のため、現行 RESTRICTED が正しい。マスターの license_note は SRC-018 を除き実態との食い違いはない

## 識別子補完候補：新規4出典6項目＋再掲1出典2項目（いずれも DOI・PMID キーの個別照会で照合済み）

- SRC-3611：PMID 20724309
- SRC-3612：PMID 28973626、PMCID PMC5717753
- SRC-3614：PMID 10053175
- SRC-3613（OG-006 の主出典、本バッチでは OG-005 の候補として使用）：PMID 24590568、PMCID PMC4066613
- SRC-018：DOI 10.1007/s00535-021-01788-x、PMID 34231046

新規分はいずれもマスター側で null の欄への補完候補であり、カード側には既記。個別照合で当該論文の識別子であることを確認した。

## 申し送り

- OG-001 のカード自体は廃止済み（status: retired、ND-037 に統合）で、主出典 SRC-1684 は ND-019・ND-037 とも共有する。本バッチの区分訂正（UNKNOWN → RESTRICTED）は同出典を使う全カードに効く。なおバッチ14（ND、旧ルール）では ND-037 を PubMed 抄録レコードによる「先例に基づく A」としていたが、新ルールでは抄録は根拠にならないため、その判定は維持されない。本バッチの候補（Front Neurol 2025 総説）は ND-037 の裏づけ候補にもなりうる。
- OG-004 の頻度区分（累積頻度5%超：脳血管障害・けいれん、1〜5%：重度の認知機能障害・大うつ病・急性錯乱状態・精神病）は自由な全文で再掲されなかった。候補 Cureus 2026 の有病率（前向き研究44.5%等）は別の指標であり、カードの頻度区分の裏づけとして登録しないこと。
- OG-004 の主出典の後継文書として EULAR の SLE 推奨2023年更新版（Ann Rheum Dis、PMID 37827694）が刊行済みであることを確認した（非 OA・ライセンス表示なしで自由ではない）。精神神経症状を含む推奨の改訂であり、監視事項として次回改訂時に考慮すること。
- OG-007 の候補 Strijbos 2013 が引く HELP の効果量（絶対率低下14.4%、相対リスク低下35.3%）は別の HELP 報告に基づく値で、カードの原著数値（852人、9.9%対15.0%、マッチドオッズ比0.60）とは異なる。裏づけ登録時に候補側の効果量をカードの数値の裏づけとして使わないこと。
- Crossref は本バッチの途中でレート制限（429）を返したため、候補6件の Crossref 個別照会は見送った（4件で 429 を確認、残り2件は未実施）。候補のライセンスは Europe PMC の個別レコード（license: cc by）と PMC 全文のライセンス要素で個別確認した（代替経路での確認。バッチ74・78 の先例と同扱い）。主出典6件のうち SRC-1684・SRC-018・SRC-3611・SRC-3612・SRC-3614 の Crossref 照会は 429 の発生前に完了している。
- Europe PMC の全文 XML が PMC5717753・PMC12307376 で HTTP 500 を返したため、該当する PMC 全文（ライセンス要素を含む）は NCBI E-utilities（efetch）で代替確認した（バッチ65・83・88 の先例と同扱い）。
- 主出典・候補とも識別子の誤記（別論文の混入）は本バッチでは発見されなかった。主出典6件すべての PMID・DOI・PMCID は DOI キー・PMID キーの個別照会で相互に照合した。
- 本バッチの判定は以上で完結しており、カードの主張・数値の変更は一切行っていない。
