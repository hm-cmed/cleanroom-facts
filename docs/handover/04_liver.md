# 引き継ぎメモ：第4回 肝（2026-10-13時点）

## 1. 現状の要約

- 原本：`raw/04_liver.md`（claude.ai の調査ラウンド、LV-001〜104）
- 正本：`data/facts/LV.yaml`（104件：verified_sources 104）。verified_expert は0件
- 取り込み・照合・番号・レビューシートまで完了（人間の委任 2026-10-13）。詳細は `reports/01_ingest_LV.md`、`03_id_check_LV.md`、`03_lv_content.md`
- 専門医レビュー用シート：`review/review_LV_20261013.xlsx`

## 2. 照合で分かったこと

- **LV-026（FIB-4）**：NAFLD GL 2020 には流れ図が2つあり、一次（一般医）は 3.25、二次（専門医）は 2.67 を高リスクの閾値としている。カードは一次だけを記していたため、両方を示す文に差し替えた。人間の指摘（NAFLD/MASLD の高リスクは 2.67、1.45・3.25 は HCV の閾値）と一致。
- **LV-069**：急性肝不全 2011年基準の原典（Mochida 2011）で、急性型（10日以内）と亜急性型（11〜56日）の日数を確認して追加した。
- そのほかの数値は全件、出典本文と一致した。CDC・JSH の PDF・厚労省の PDF・MASLD 論文の図など、PubMed にない出典も本文・図で確認した。
- 肝硬変GL 2020（SRC-018）は Crossref で CC BY 4.0（OPEN）と確定した（第1回から「未確認」だった点の解消）。
- 調査ラウンドの §8 は「第5回の SRC 番号は SRC-076 から」としていたが誤り。今回 SRC-086 まで使ったので、**第5回は SRC-087 から**。

## 3. 未解決事項

| # | 内容 | 担当 |
|---|---|---|
| 1 | 国内の承認・保険：トルバプタン（LV-011）、ルストロンボパグ（LV-018）、SGLT2 阻害薬・GLP-1 受容体作動薬の NAFLD への適用（LV-029）、PBC のベザフィブラート（LV-077） | 人間 |
| 2 | 出典が古いもの：MedlinePlus（LV-066・067・093・094）、エキノコックス事務連絡（2014年、LV-073）、WJG 2008 の DILI 総説（LV-095〜097） | 次回の補完 |
| 3 | 指定難病 PDF の版（告示改正の時点）と、受給者証保持者数が令和元年度の値であること | 人間 |
| 4 | LV-042：GL 内で非B非C型の割合の記載に幅（約50%と30〜40%） | 専門医レビュー |
| 5 | LV-091：出典 PDF 内で男女比の向きが整合しない | 人間（原典の確認） |
| 6 | 肝癌診療GL の改訂版・追補（LV-047 の薬物療法） | 次回 |
| 7 | 数値を含まない推奨・定義の言い回しは、一文ずつは照合していない | 専門医レビュー |
| 8 | 調査レポート第6節の未作成トピック（アルコール性肝障害、細菌性肝膿瘍、日本住血吸虫症、肝内胆管癌・転移性肝癌・肝血管腫・肝嚢胞、肝外門脈閉塞症、DILI の日本の疫学と DDW-J の配点、肝切除の ICG 基準・放射線治療・新しい薬物療法、肝炎ウイルス検査と医療費助成） | 欠番補完ラウンド |

## 4. 第5回（胆・膵、接頭辞 BP）への引き継ぎ

- 出力形式は `docs/tasks/round2_GD_supplement.md` 第1節、番号は `docs/tasks/curriculum_reference.md`（出題基準 Ⅵ-7 胆道疾患・Ⅵ-8 膵疾患を収載）。**SRC 番号は SRC-087 から。**
- 原発性硬化性胆管炎（Ⅵ-7-B-③）は第5回で扱う。膵・胆管合流異常症（Ⅵ-7-A-①）、膵神経内分泌腫瘍（Ⅵ-8-B-③）も第5回。
- 調査環境の制約（調査レポート §8）：PubMed や一部の出版社ページが調査側から読めないことがある。リポジトリ側では PMC・公的機関の本文で照合できるので、数値は「どの資料のどこに書いてあったか」を uncertainty に残してもらうと照合が速い。

## 5. 重複回避リスト（自動生成）

次回の調査依頼文に貼り付ける。

### 5-1. 扱い済みのトピック（領域・subdomain 別の件数）

- **HP**（20件）：H. pylori関連疾患 20
- **UG**（18件）：上部消化管出血 18
- **ES**（89件）：食道癌 22、その他の食道疾患 20、GERD・NERD・Barrett食道 18、食道運動障害 10、食道静脈瘤・門脈圧亢進症 10、好酸球性食道炎（EoE） 9
- **GD**（95件）：胃癌 29、機能性ディスペプシア 18、NSAID・LDA潰瘍の予防 9、GIST・粘膜下腫瘍 9、胃切除後症候群 7、胃アニサキス症 5、胃ポリープ 4、消化性潰瘍 3、急性胃粘膜病変 3、胃・十二指腸憩室 3、胃静脈瘤 2、酸分泌抑制薬の長期使用 1、慢性胃炎 1、胃神経内分泌腫瘍 1
- **IN**（89件）：炎症性腸疾患 16、大腸癌 14、大腸ポリープ 11、過敏性腸症候群 10、大腸憩室出血・憩室炎 10、感染性腸炎 10、慢性便秘症 9、Clostridioides difficile感染症 5、セリアック病 3、痔核 1
- **LV**（104件）：肝硬変とその合併症 22、ウイルス性肝炎 19、NAFLD/NASH・MASLD 15、肝細胞癌 14、自己免疫性肝疾患 10、代謝性肝疾患 5、体質性黄疸 4、急性肝不全 4、肝の血管性疾患 4、薬物性肝障害 3、寄生虫性肝疾患 2、肝膿瘍 2

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
| SRC-018 | Yoshiji H, 肝硬変GL 2020 | ES-066〜LV-022（24件） |
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
| SRC-065 | Tokushige K, et al. Evidence-based clinical practice guidelines for no | LV-023〜LV-034（12件） |
| SRC-066 | Rinella ME, et al. A multisociety Delphi consensus statement on new fa | LV-035〜LV-037（3件） |
| SRC-067 | 日本肝臓学会 Clinical Practice Guidelines for Hepatocellular Carcinoma 2021（ | LV-038〜LV-049（12件） |
| SRC-068 | 国立がん研究センター がん情報サービス 肝臓（罹患2026-03-23更新、死亡2026-01-07更新、生存率2026-07-22更新） | LV-050〜LV-051（2件） |
| SRC-069 | CDC. Clinical Overview of Hepatitis A（2025-08-29更新） | LV-052〜LV-054（3件） |
| SRC-070 | CDC. Clinical Overview of Hepatitis B（2025-08-29更新） | LV-055〜LV-058（4件） |
| SRC-071 | CDC. Clinical Overview of Hepatitis C（2025-08-29更新） | LV-059〜LV-062（4件） |
| SRC-072 | 厚生労働省『E型肝炎に関するQ&A』 | LV-063〜LV-065（3件） |
| SRC-073 | MedlinePlus Genetics. Gilbert syndrome（最終更新 2012-02-01） | LV-066〜LV-067（2件） |
| SRC-074 | Sugawara K, Nakayama N, Mochida S. Acute liver failure in Japan: defin | LV-068〜LV-071（4件） |
| SRC-075 | 厚生労働省健康局結核感染症課 事務連絡『愛知県における犬のエキノコックス症感染事例について（情報提供）』（平成26年4月8日） | LV-072〜LV-073（2件） |
| SRC-076 | 厚生労働省 指定難病93『原発性胆汁性胆管炎』概要・診断基準等 | LV-074〜LV-078（5件） |
| SRC-077 | 厚生労働省 指定難病95『自己免疫性肝炎』概要・診断基準等 | LV-079〜LV-083（5件） |
| SRC-078 | 厚生労働省 指定難病171『ウィルソン病』概要・診断基準等 | LV-084〜LV-086（3件） |
| SRC-079 | 厚生労働省 指定難病91『バッド・キアリ症候群』概要・診断基準等 | LV-089〜LV-090（2件） |
| SRC-080 | 厚生労働省 指定難病92『特発性門脈圧亢進症』概要・診断基準等 | LV-091〜LV-092（2件） |
| SRC-081 | MedlinePlus Genetics. Hereditary hemochromatosis（最終更新 2019-02-01） | LV-087〜LV-088（2件） |
| SRC-082 | MedlinePlus Genetics. Dubin-Johnson syndrome（最終更新 2018-08-01） | LV-093 |
| SRC-083 | MedlinePlus Genetics. Rotor syndrome（最終更新 2013-03-01） | LV-094 |
| SRC-084 | Tajiri K, Shimizu Y. Practical guidelines for diagnosis and early mana | LV-095〜LV-097（3件） |
| SRC-085 | 日本肝臓学会 肝炎診療ガイドライン作成委員会編『B型肝炎治療ガイドライン（第4版）簡易版』2022年6月 | LV-098〜LV-102（5件） |
| SRC-086 | 厚生労働省 感染症法に基づく医師の届出基準『五類感染症 アメーバ赤痢』と発生届様式 | LV-103〜LV-104（2件） |

- パイロット（HP・UG）の出典には SRC 番号を付けていない（主なものは `docs/handover/02_gastroduodenal.md` 第5節）。
