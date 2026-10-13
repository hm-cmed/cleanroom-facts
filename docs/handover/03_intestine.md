# 引き継ぎメモ：第3回 小腸・大腸（2026-10-13時点）

## 1. 現状の要約

- 原本：`raw/03_intestine.md`（claude.ai の調査ラウンド、IN-001〜088）
- 正本：`data/facts/IN.yaml`（89件：verified_sources 89。IN-089 は照合時に起票）。verified_expert は0件
- 取り込み・照合・番号・レビューシートまで完了（人間の委任 2026-10-13）。詳細は `reports/01_ingest_IN.md`、`03_id_check_IN.md`、`03_in_content.md`、`04_curriculum_IN.md`
- 専門医レビュー用シート：`review/review_IN_20261013.xlsx`

## 2. 照合で分かったこと

- 主張文の数値は全件、出典本文と一致した（数値の訂正は0件）。
- Springer の日本の学会GL（IBD、IBS、大腸ポリープ、JSCCR 2024）は CC BY 4.0（OPEN）。Karger の慢性便秘症GLは CC BY-NC、大腸憩室GLは CC BY-NC-ND。
- 調査ラウンドは国試出題基準 Ⅵ-3・Ⅵ-4 の表を取得できなかった。Claude Code が PDF から番号を付けた。次回からは `docs/tasks/curriculum_reference.md` を調査依頼に添付する。

## 3. 未解決事項

| # | 内容 | 担当 |
|---|---|---|
| 1 | 国内の承認・保険：便秘薬（IN-035）、ロボット支援手術（IN-051）、CDI 治療薬（IN-083・084）の添付文書・点数表での確認 | 人間 |
| 2 | 難病情報センター（SRC-055・056）の利用規約、ganjoho.jp の利用規約 | 人間 |
| 3 | IN-088（痔核）の出典は NIDDK の2016年レビュー。日本の資料への差し替え | 次回の補完 |
| 4 | 孫引き数値（IN-009 など19件）は GL・総説の本文と一致したが、原著とは未照合 | 必要なら次回 |
| 5 | 数値を含まない推奨・定義の言い回しは、一文ずつは照合していない | 専門医レビュー |
| 6 | 調査レポート第6節の未作成トピック（虚血性大腸炎、IBD・IBS の薬物療法の詳細、便秘薬の推奨度、大腸癌の T1 追加切除基準・補助化学療法・バイオマーカー、薬剤性腸炎、腸管ベーチェット、腸結核、小腸腫瘍、肛門疾患、日本の CDI GL、サルモネラ・腸炎ビブリオ・アメーバ赤痢） | 欠番補完ラウンド |

## 4. 第4回（肝、接頭辞 LV）への引き継ぎ

- 出力形式は `docs/tasks/round2_GD_supplement.md` 第1節。SRC 番号は SRC-065 から。
- 番号表は `docs/tasks/curriculum_reference.md` を添付する（出題基準 Ⅵ-6 肝疾患、コアカリの疾患表の肝臓の項目と id）。
- 肝硬変GL 2020（SRC-018）は ES・GD で静脈瘤の部分だけを使用済み。腹水・肝性脳症・栄養などには使ってよい。
- 門脈圧亢進症（Ⅵ-6-D-①）は、食道・胃静脈瘤の内視鏡治療を除いて第4回で扱ってよい（静脈瘤は ES-057〜066、GD-072・073 で扱い済み）。

## 5. 重複回避リスト（自動生成）

次回の調査依頼文に貼り付ける。

### 5-1. 扱い済みのトピック（領域・subdomain 別の件数）

- **HP**（20件）：H. pylori関連疾患 20
- **UG**（18件）：上部消化管出血 18
- **ES**（89件）：食道癌 22、その他の食道疾患 20、GERD・NERD・Barrett食道 18、食道運動障害 10、食道静脈瘤・門脈圧亢進症 10、好酸球性食道炎（EoE） 9
- **GD**（95件）：胃癌 29、機能性ディスペプシア 18、NSAID・LDA潰瘍の予防 9、GIST・粘膜下腫瘍 9、胃切除後症候群 7、胃アニサキス症 5、胃ポリープ 4、消化性潰瘍 3、急性胃粘膜病変 3、胃・十二指腸憩室 3、胃静脈瘤 2、酸分泌抑制薬の長期使用 1、慢性胃炎 1、胃神経内分泌腫瘍 1
- **IN**（89件）：炎症性腸疾患 16、大腸癌 14、大腸ポリープ 11、過敏性腸症候群 10、大腸憩室出血・憩室炎 10、感染性腸炎 10、慢性便秘症 9、Clostridioides difficile感染症 5、セリアック病 3、痔核 1

### 5-2. 使用済みの出典（再利用するときは同じ SRC 番号を使う）

| SRC | 出典 | 使用カード |
|---|---|---|
| SRC-001 | Kato K, JCOG1109 | ES-049〜ES-050（2件） |
| SRC-002 | Kelly RJ, CheckMate 577 | ES-051 |
| SRC-003 | Doki Y, CheckMate 648 | ES-052 |
| SRC-004 | Sun JM, KEYNOTE-590 | ES-053〜ES-054（2件） |
| SRC-005 | Metges JP, KEYNOTE-590 5年 | — |
| SRC-006 | Ishihara R, JGES食道ESD/EMR GL | ES-046〜ES-089（2件） |
| SRC-007 | de Franchis R, Baveno VII | ES-062〜ES-064（2件） |
| SRC-008 | Gralnek IM, ESGE静脈瘤GL | — |
| SRC-009 | Birk M, ESGE異物GL | ES-069〜ES-072（4件） |
| SRC-010 | Gyawali CP, Lyon 2.0 | ES-009 |
| SRC-011 | Yadlapati R, Chicago v4.0 | ES-025〜ES-031（7件） |
| SRC-012 | Brooks PJ, Alcohol flushing response | ES-092 |
| SRC-013 | Lewis SJ, ALDH2メタ解析 | — |
| SRC-014 | 国立がん研究センター がん統計 | ES-035 |
| SRC-015 | 診療報酬点数表 K653-6 | ES-093 |
| SRC-016 | 小野薬品・BMS 適正使用文書 | ES-090 |
| SRC-017 | 門脈圧亢進症取扱い規約 第3版の記載基準 | ES-061〜GD-072（2件） |
| SRC-018 | Yoshiji H, 肝硬変GL 2020 | ES-066〜GD-073（2件） |
| SRC-019 | Verhoeven RHA, CheckMate 577 実臨床 | — |
| SRC-020 | Contini S, 腐食性傷害の総説 | ES-073〜ES-075（2件） |
| SRC-021 | Cheng HT, 成人の腐食性物質摂取 | ES-074 |
| SRC-022 | Boerhaave Syndrome—Narrative Review | ES-085〜ES-087（3件） |
| SRC-023 | HSV/CMV食道共感染の症例と文献レビュー | ES-079 |
| SRC-024 | HSV vs CMV食道炎の内視鏡所見 | ES-080〜ES-081（2件） |
| SRC-025 | Werner YB, POEM vs LHM | ES-032〜ES-033（2件） |
| SRC-026 | Dellon ES, デュピルマブ EoE | ES-023 |
| SRC-027 | Villanueva C, 輸血戦略 | ES-063 |
| SRC-028 | Miwa H, et al. Evidence-based clinical practice guidelines for functio | GD-001〜GD-018（18件） |
| SRC-029 | Japanese Gastric Cancer Association. Japanese Gastric Cancer Treatment | GD-044〜GD-048（2件） |
| SRC-030 | Japanese Gastric Cancer Association. Japanese gastric cancer treatment | GD-035〜GD-080（23件） |
| SRC-031 | Sugimoto M, et al. Evidence-based clinical practice guidelines for pep | GD-019〜GD-032（14件） |
| SRC-032 | Hirota S, et al. English version of Japanese Clinical Practice Guideli | GD-062〜GD-070（8件） |
| SRC-033 | Joensuu H, et al. Adjuvant imatinib for high-risk GI stromal tumor: an | GD-069 |
| SRC-034 | Janjigian YY, et al. CheckMate 649. Lancet 2021;398:27-40 | GD-055 |
| SRC-035 | Shitara K, et al. SPOTLIGHT. Lancet 2023;401:1655-1668 | GD-056 |
| SRC-036 | 国立がん研究センター がん情報サービス 胃（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新） | GD-033 |
| SRC-037 | 厚生労働省『がん予防重点健康教育及びがん検診実施のための指針』（平成28年2月改正）／厚労省がん検診ページ | GD-034〜IN-056（2件） |
| SRC-038 | アステラス製薬 適時開示（2024-07-29）：ゾルベツキシマブ 欧州CHMP販売承認勧告（国内承認日の記載あり） | GD-057 |
| SRC-039 | Panzuto F, et al. ENETS 2023 guidance paper for gastroduodenal neuroen | GD-071 |
| SRC-040 | Scarpellini E, et al. International consensus on the diagnosis and man | GD-074〜GD-079（6件） |
| SRC-041 | 厚生労働省『アニサキスによる食中毒を予防しましょう』 | GD-081〜GD-083（3件） |
| SRC-042 | Sugiyama H, et al. Anisakiasis annual incidence and causative species, | GD-084〜GD-085（2件） |
| SRC-043 | Islam RS, et al. Gastric polyps: a review on clinical, endoscopic, his | GD-086〜GD-088（3件） |
| SRC-044 | 岩室雅也. 薬剤起因性胃粘膜病変の内視鏡診断. 日本消化器内視鏡学会雑誌 2025;67(4):281-288 | GD-089〜GD-091（3件） |
| SRC-045 | Cook D, et al. Stress ulcer prophylaxis during invasive mechanical ven | GD-092 |
| SRC-046 | Rizwan MM, et al. Duodenal diverticulum and associated pancreatitis: c | GD-093〜GD-094（2件） |
| SRC-047 | Ergüder E, et al. Lemmel syndrome: a single-center cohort and diagnost | GD-095 |
| SRC-048 | Nakase H, et al. Evidence-based clinical practice guidelines for infla | IN-001〜IN-010（10件） |
| SRC-049 | Fukudo S, et al. Evidence-based clinical practice guidelines for irrit | IN-017〜IN-026（10件） |
| SRC-050 | Ihara E, et al. Evidence-Based Clinical Guidelines for Chronic Constip | IN-027〜IN-035（9件） |
| SRC-051 | Tanaka S, et al. Evidence-based clinical practice guidelines for manag | IN-036〜IN-089（11件） |
| SRC-052 | Kinugasa Y, et al. Japanese Society for Cancer of the Colon and Rectum | IN-046〜IN-053（8件） |
| SRC-053 | 国立がん研究センター がん情報サービス 大腸（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新） | IN-054〜IN-055（2件） |
| SRC-054 | National Cancer Institute. Genetics of Colorectal Cancer (PDQ)–Health  | IN-057〜IN-059（3件） |
| SRC-055 | 難病情報センター『潰瘍性大腸炎（指定難病97）』（情報更新 令和7年11月） | IN-011〜IN-013（3件） |
| SRC-056 | 難病情報センター『クローン病（指定難病96）』（情報更新 令和7年11月） | IN-014〜IN-016（3件） |
| SRC-057 | Nagata N, et al. Guidelines for Colonic Diverticular Bleeding and Colo | IN-060〜IN-069（10件） |
| SRC-058 | 厚生労働省『腸管出血性大腸菌Q&A』（最終改訂 令和3年12月17日） | IN-070〜IN-073（4件） |
| SRC-059 | 厚生労働省『カンピロバクター食中毒予防について（Q&A）』（最終改訂 令和8年5月27日） | IN-074〜IN-075（2件） |
| SRC-060 | 厚生労働省『ノロウイルスに関するQ&A』（最終改定 令和3年11月19日） | IN-076〜IN-079（4件） |
| SRC-061 | CDC. C. diff: Facts for Clinicians（2026-04-13更新） | IN-080〜IN-083（4件） |
| SRC-062 | Johnson S, et al. IDSA/SHEA 2021 Focused Update Guidelines on Manageme | IN-084 |
| SRC-063 | NIDDK. Definition & Facts for Celiac Disease（最終レビュー 2020年10月） | IN-085〜IN-087（3件） |
| SRC-064 | NIDDK. Definition & Facts of Hemorrhoids（最終レビュー 2016年10月） | IN-088 |

- パイロット（HP・UG）の出典には SRC 番号を付けていない（主なものは `docs/handover/02_gastroduodenal.md` 第5節）。
