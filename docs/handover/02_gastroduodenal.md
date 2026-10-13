# 引き継ぎメモ：第2回 胃・十二指腸（2026-10-13時点）

## 1. 現状の要約

- 原本：`raw/02_gastroduodenal.md`（claude.ai の調査ラウンド。初回 GD-001〜073、補充 GD-074〜095）
- 正本：`data/facts/GD.yaml`（95件：verified_sources 94、draft 1）。verified_expert は0件
- 取り込み・照合・番号・レビューシートまで完了（人間の委任 2026-10-13）。詳細は `reports/01_ingest_GD.md`、`03_id_check_GD.md`、`03_gd_content.md`、`04_curriculum_GD.md`
- 専門医レビュー用シート：`review/review_GD_20261013.xlsx`

## 2. 照合で分かったこと

- 調査レポートの形式は、追加情報（`docs/tasks/round2_GD_supplement.md`）どおりで、取り込みは無修正で通った。
- 主張文中の数値は、機械照合と文脈の確認で、出典本文と全件一致した（第1回のような数値の誤りはなかった）。
- 修正は11件（REVISE の数値を主張文に移した、88.9% の確定、EID を GOV_US に変更、識別子の補完など）。
- Springer の日本の学会GL（FD、胃癌第6版・第7版、GIST）は Crossref で CC BY 4.0（OPEN）だった。
- J-STAGE 和文誌の DOI は JaLC 登録で Crossref にない。`verify_ids.py` は doi.org で登録機関と解決を確認するよう修正済み。

## 3. 未解決事項

| # | 内容 | 担当 |
|---|---|---|
| 1 | GD-071（胃 NET）：本文未閲覧のため draft | 人間（専門医）または次回の補完 |
| 2 | 数値を含まない命題（推奨・定義）は、推奨文の言い回しまで一文ずつは照合していない | 専門医レビュー |
| 3 | GD-079 アカルボースの国内適応、GD-057 の PMDA 添付文書での確認 | 人間 |
| 4 | GD-010・049・076・086・087・093・094 は GL・総説の引用値（原著は未照合） | 必要なら次回 |
| 5 | SPOTLIGHT の全生存を別カードにするか | 次回の補完 |
| 6 | 調査レポート第6節の未作成トピック（AGML の定義、GAVE・PHG、十二指腸腫瘍、SMA 症候群、好酸球性胃腸炎、MALT の病期と除菌無効例、ポリポーシス、アミロイドーシス、GIST 二次治療以降、NET III型、胃癌GL第7版の胃切除後障害・高齢者CQ） | 欠番補完ラウンド |
| 7 | ganjoho.jp の利用規約（GD-033 も該当） | 人間 |

## 4. 第3回（小腸・大腸、接頭辞 IN）への引き継ぎ

- 出力形式は `docs/tasks/round2_GD_supplement.md` 第1節を引き続き使う。SRC 番号は SRC-048 から。
- 番号表：出題基準は医学各論 Ⅵ-3（小腸・結腸疾患）・Ⅵ-4（直腸・肛門疾患）・Ⅵ-5（消化管共通疾患：ポリポーシス、NET、憩室、虚血性腸炎など）。コアカリは PS-02-08-05・PS-03-04-14 と別表2-7（下血・下痢・便秘など）。
- 境界：消化管共通疾患のうち、胃に関するものは GD で扱い済み（GIST 9件、NET 1件、憩室 3件）。小腸・大腸の GIST・NET・憩室は第3回で扱ってよい。

## 5. 重複回避リスト（自動生成）

次回の調査依頼文に貼り付ける。

### 5-1. 扱い済みのトピック（領域・subdomain 別の件数）

- **HP**（20件）：H. pylori関連疾患 20
- **UG**（18件）：上部消化管出血 18
- **ES**（89件）：食道癌 22、その他の食道疾患 20、GERD・NERD・Barrett食道 18、食道運動障害 10、食道静脈瘤・門脈圧亢進症 10、好酸球性食道炎（EoE） 9
- **GD**（95件）：胃癌 29、機能性ディスペプシア 18、NSAID・LDA潰瘍の予防 9、GIST・粘膜下腫瘍 9、胃切除後症候群 7、胃アニサキス症 5、胃ポリープ 4、消化性潰瘍 3、急性胃粘膜病変 3、胃・十二指腸憩室 3、胃静脈瘤 2、酸分泌抑制薬の長期使用 1、慢性胃炎 1、胃神経内分泌腫瘍 1

### 5-2. 使用済みの出典（SRC 番号つき。再利用するときは同じ番号を使う）

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
| SRC-037 | 厚生労働省『がん予防重点健康教育及びがん検診実施のための指針』（平成28年2月改正）／厚労省がん検診ページ | GD-034 |
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

- パイロット（HP・UG）の出典には SRC 番号を付けていない。主なもの：JSGE 消化性潰瘍 GL 2026（SRC-031 と同一）、JSHR H. pylori GL 2024、Maastricht VI、ACG 2024（H. pylori）、ACG 2021（上部消化管出血）、ESGE 2021・2026、JGES 第2版（非静脈瘤性出血）。
