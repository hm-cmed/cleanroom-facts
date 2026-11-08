# 依頼：自由に使える出典への置き換え候補の調査（BL・GR・HF・PV）

作成：2026-11-08（登録側＝Claude）／依頼者：三原弘／作業：Muse
対象：BL（血液・造血の横断）14件、GR（成長・発達）3件、HF（心不全・心原性ショック）30件、PV（肺循環）32件、計79件

## 1. 背景と目的

- 事実票の有効カード3,821件のうち、出典が自由に使える区分（OPEN・GOV_JP・GOV_US）のものは約27%です。上の4領域は**自由に使える出典が1件もありません**（出典は RESTRICTED か UNKNOWN だけ）。
- 事実（数値・研究結果・推奨の向き）は著作権の対象外で、現在のカードも利用根拠 B で作っています。今回の目的は、それをさらに固めることです。**同じ事実を、著作権の及ばない資料や自由に使える資料でも裏づけ、可能なら主出典をそちらに置き換えます。**
- **主張文と数値は変えません。** 今回の成果物は「出典の候補」だけです。主張の修正が必要だと思われる点は、別欄に書いてください。

## 2. 探す資料（優先順）

1. **米国連邦政府の資料（GOV_US）**
   - ClinicalTrials.gov の結果登録（Results posted のもの）：試験の主要評価項目の数値。HF の大規模試験（PARADIGM-HF、DAPA-HF、EMPEROR-Preserved、RALES、CARE-HF、SHOCK、IABP-SHOCK II、CULPRIT-SHOCK、DanGer Shock など）と PV の試験（PEITHO、CHEST-1、AMBITION、STELLAR など）は、まずここを確認する。
   - FDA：添付文書（Drugs@FDA の Label）と審査資料（Medical/Statistical Review）。
   - NIH（NHLBI、NCI、NLM の MedlinePlus など）、CDC、AHRQ のエビデンスレポート。
   - 注意：連邦政府の資料でも、中に転載された第三者の図表・文章は自由ではありません（その部分は使わない）。NCBI Bookshelf の収載書籍（StatPearls、GeneReviews など）は政府著作物ではありません。個別のライセンスを確認してください。
2. **日本の公的資料（GOV_JP）**
   - 厚生労働省（通知、検討会資料、患者調査・人口動態統計など）、e-Stat、国立感染症研究所。法令・告示・通知は著作権の対象外です。その他は政府標準利用規約（出典を明記し、加工した旨を示す）で使えます。
   - PMDA の審査報告書・添付文書は、PMDA のサイト利用規約を確認し、確認結果を書いてください（これまで添付文書は UNKNOWN として扱っています）。
   - 公的機関の名前があっても、財団や学会が運営するサイト（難病情報センターなど）は GOV_JP にしません。
3. **CC BY・CC0 の論文（OPEN）**
   - PMC の Open Access Subset などで、ライセンスが CC BY または CC0 と明示されているもの。CC BY-NC・ND は RESTRICTED です。
4. **現在の出典の再確認**
   - 現在 UNKNOWN の出典（下表の区分を参照）の中には、実際には CC BY のものがあるかもしれません（例：SRC-2481 Ann Ib Postgrad Med）。出版社ページや PMC の表示で確認してください。OPEN と分かれば、それも成果に含めてください。

## 3. 判定と書き方

カードごとに次のどれかで判定してください。

| 判定 | 意味 |
|---|---|
| A 置き換え可 | 自由に使える資料だけで、主張文の全体（数値を含む）が裏づけられる。主出典をその資料に差し替える候補 |
| B 裏づけ追加 | 主張の一部（例：試験の主要評価項目の数値だけ）が裏づけられる。主出典はそのままにして、corroboration に記録する候補 |
| C 見つからない | 探した範囲では見つからなかった。何を探したかを1行で書く |
| D 区分の訂正 | 現在の出典自体が実は OPEN・GOV だった（ライセンス表示の根拠を書く） |

必ず守ること：
- **数値は一致を確認する。** 試験登録の数値は、論文と解析対象や追跡期間が違うことがあります。違えば「不一致」と書き、両方の数値と違う理由（分かれば）を書いてください。カードに合わせて丸めたり、選んだりしないでください。
- **推奨の強さ・向きは、資料の記載どおり。** 強めたり弱めたりしない。
- **識別子（NCT 番号、DOI、PMID、PMCID）は、そのページで確認できたものだけ。** 確認できなければ空欄にする。
- **文章を写さない。** 成果物に書くのは、書誌・識別子・ライセンスの根拠 URL・数値と、どの部分を裏づけるかの短い説明だけ。
- 読み込んだ PDF は、出典台帳の手順どおり Google ドライブの cleanroom-sources に保存し、INTAKE_LOG.md に IN 番号を付けてください。

## 4. 成果物の形式

ファイル名：`free_sources_BL_GR_HF_PV_result.md`（JSON 版も同名の .json で）

1. 判定表

| カード | 判定 | 候補資料（書誌） | 識別子 | 区分（GOV_US など）とライセンスの根拠 URL | 裏づける部分 | 数値の照合（一致／不一致と両方の値） | 備考 |
|---|---|---|---|---|---|---|---|

2. 新規出典表（これまでの登録依頼と同じ形式。SRC 番号は「新規（仮）」。既存マスターとの重複は DOI・PMID・NCT 番号で確認）
3. 主張文の修正が必要と思われる点（あれば。修正案ではなく、理由と根拠だけ）
4. 集計（判定ごとの件数、領域ごとの件数）

## 5. 対象カード一覧（2026-11-08 時点、origin/main）

| カード | 主張文（冒頭） | 現在の主出典（区分） | DOI |
|---|---|---|---|
| HF-001 | JCS/JHFS 2025年版は心不全の国際的な定義・分類に合わせ、左室駆出率40%以下をHFrEF、41〜49%をHFmrEF、50%以上をHFpEFとする。初回40%以下だった駆出率が10ポイント以上改善して40%を… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| HF-002 | JCS/JHFS 2025年版は、心不全のステージA（心不全のリスクがある）とステージB（前心不全）の説明を拡充し、ステージAの危険因子に慢性腎臓病を加えた。日本の疫学研究では、ステージCの69%、ステージDの51%がH… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| HF-003 | 佐渡市の左室機能障害の有病率と人口推計をもとにした研究では、日本の左室機能障害の外来患者は2005年に約97.9万人で、高齢化により2030年には約130万人に達すると予測された。 | SRC-186（UNKNOWN）Okura Y, Ramadan MM, Ohno Y, et al. Impending epidemic: future project… | 10.1253/circj.72.489 |
| HF-004 | 宮崎県延岡市の地域住民を対象とした研究（3年間、初回の心不全入院406件、平均82歳）では、心不全による初回入院の発生率は人口10万人年あたり129で、2015年の日本の人口で年齢調整すると105であった。発生率に男女差… | SRC-187（RESTRICTED）Marume K, Ogata S, Kaichi R, et al. Incidence Rate of Hospitalization … | 10.1253/circrep.CR-21-0142 |
| HF-005 | 心不全の診断または除外のためにBNPまたはNT-proBNPを測定すべきとされ（クラスI、レベルA）、日本心不全学会は心不全を除外する目安としてBNP 35 pg/mL未満、NT-proBNP 125 pg/mL未満を示… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| HF-006 | 救急外来を急性の呼吸困難で受診した1,586人の研究では、BNPは病歴・身体所見・他の検査より正確に心不全を見分け、100 pg/mLをカットオフとした診断精度は83.4%、50 pg/mL未満の陰性的中率は96%であっ… | SRC-188（RESTRICTED）Maisel AS, Krishnaswamy P, Nowak RM, et al. Rapid measurement of B-typ… | 10.1056/NEJMoa020233 |
| HF-007 | 急性の呼吸困難患者1,256人の国際共同解析では、NT-proBNPの年齢別のカットオフ（50歳未満450、50〜75歳900、75歳超1,800 pg/mL）が急性心不全の診断に有用で、感度90%、特異度84%であった… | SRC-189（RESTRICTED）Januzzi JL Jr, van Kimmenade R, Lainchbury J, et al. NT-proBNP testing… | 10.1093/eurheartj/ehi631 |
| HF-008 | 心不全で入院した452人の研究では、うっ血と低灌流の有無で4群（A：うっ血も低灌流もない、B：うっ血あり・灌流は保たれる、C：うっ血と低灌流がある、L：うっ血はなく低灌流がある）に分けると予後を予測でき、BとCは死亡また… | SRC-190（RESTRICTED）Nohria A, Tsang SW, Fang JC, et al. Clinical assessment identifies hem… | 10.1016/S0735-1097(03)00309-7 |
| HF-009 | 急性心不全の発症早期（受診後6〜12時間）の対応には、初期の収縮期血圧と症状で5つに分けるクリニカルシナリオ（CS）が提案されている。CS1は収縮期血圧140 mmHg超、CS2は100〜140 mmHg、CS3は100… | SRC-191（RESTRICTED）Mebazaa A, Gheorghiade M, Piña IL, et al. Practical recommendations fo… | 10.1097/01.CCM.0000296274.51933.4C |
| HF-010 | 急性非代償性心不全で体液貯留がある場合は、うっ血症状を和らげるためループ利尿薬を静注すべきとされる（クラスI、レベルC-EO）。初回の利尿薬に反応が乏しい場合は、増量またはトルバプタンやサイアザイド系利尿薬の併用を考慮で… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| HF-011 | 急性心不全で呼吸不全（呼吸数25/分超、SpO2 90%未満）がある場合は、呼吸困難を和らげ気管挿管を避けるためにNPPVを速やかに始めるべきとされる（クラスI、レベルA）。SpO2 90%未満またはPaO2 60 mm… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| HF-012 | 急性非代償性心不全では、ドブタミンは肺うっ血に低心拍出・組織低灌流を伴う場合に（クラスIIa、レベルC-LD）、ノルアドレナリンは十分な輸液後もショックや低血圧が続く場合に（IIa、B-R）考慮できる。低心拍出・低灌流・… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| HF-013 | 左室駆出率40%以下の心不全（HFrEF）では、禁忌がなければACE阻害薬（クラスI、レベルA）、β遮断薬（カルベジロールまたはビソプロロール、I、A）、ミネラルコルチコイド受容体拮抗薬（NYHA II〜IV度、I、A）… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| HF-014 | NYHA II〜IV度で駆出率40%以下の心不全患者8,442人を対象としたPARADIGM-HF試験では、サクビトリル・バルサルタン（ARNI）はエナラプリルに比べ、心血管死または心不全入院を減らし（21.8%対26.… | SRC-192（RESTRICTED）McMurray JJV, Packer M, Desai AS, et al. Angiotensin-neprilysin inhibi… | 10.1056/NEJMoa1409077 |
| HF-015 | 駆出率40%以下の心不全患者4,744人を対象としたDAPA-HF試験では、ダパグリフロジン10 mgはプラセボに比べ、心不全の悪化または心血管死を減らした（16.3%対21.2%、ハザード比0.74）。効果は糖尿病の有… | SRC-193（RESTRICTED）McMurray JJV, Solomon SD, Inzucchi SE, et al. Dapagliflozin in Patient… | 10.1056/NEJMoa1911303 |
| HF-016 | 駆出率35%以下の重症心不全患者1,663人を対象としたRALES試験では、スピロノラクトン25 mgの追加で死亡が46%から35%に減り（相対リスク0.70）、心不全悪化による入院も減った。男性の10%に女性化乳房また… | SRC-194（RESTRICTED）Pitt B, Zannad F, Remme WJ, et al. The effect of spironolactone on mor… | 10.1056/NEJM199909023411001 |
| HF-017 | 左室駆出率50%以上の症候性心不全（HFpEF）では、SGLT2阻害薬（エンパグリフロジンまたはダパグリフロジン）が心血管死または心不全入院を減らすため推奨され（クラスI、レベルA）、うっ血には利尿薬を使う（I、C-LD… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| HF-018 | 駆出率40%を超える心不全患者5,988人を対象としたEMPEROR-Preserved試験では、エンパグリフロジンはプラセボに比べ、心血管死または心不全入院を減らした（13.8%対17.1%、ハザード比0.79）。主に… | SRC-195（RESTRICTED）Anker SD, Butler J, Filippatos G, et al. Empagliflozin in Heart Failur… | 10.1056/NEJMoa2107038 |
| HF-019 | NYHA III〜IV度で心臓の同期不全がある心不全患者813人を対象としたCARE-HF試験では、心臓再同期療法（CRT）の追加で、死亡または主要な心血管イベントによる入院が55%から39%に減り（ハザード比0.63）… | SRC-196（RESTRICTED）Cleland JGF, Daubert JC, Erdmann E, et al. The effect of cardiac resyn… | 10.1056/NEJMoa050496 |
| HF-020 | 心原性ショックの患者は、機械的循環補助を管理できるICU・CCUに移すべきとされ（クラスI、レベルC-EO）、体液過剰の所見がなければ生理食塩液またはリンゲル液200 mL以上を15〜30分で投与することを考慮できる（I… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| HF-021 | SCAI分類は心原性ショックの重症度をA（リスクあり）、B（始まり）、C（典型的）、D（悪化）、E（極限）の5段階に分ける。BとCの違いは低灌流の有無で、Dは最初の治療を少なくとも30分行っても安定せず灌流が回復しない状… | SRC-197（RESTRICTED）Baran DA, Grines CL, Bailey S, et al. SCAI clinical expert consensus s… | 10.1002/ccd.28329 |
| HF-022 | 急性心筋梗塞に伴う心原性ショック患者302人を対象としたSHOCK試験では、緊急血行再建は初期の内科的安定化と比べて30日死亡率に有意差はなかった（46.7%対56.0%）が、6か月死亡率は低かった（50.3%対63.1… | SRC-198（RESTRICTED）Hochman JS, Sleeper LA, Webb JG, et al. Early revascularization in acu… | 10.1056/NEJM199908263410901 |
| HF-023 | 早期の血行再建を予定した急性心筋梗塞による心原性ショック患者600人を対象としたIABP-SHOCK II試験では、大動脈内バルーンパンピング（IABP）は30日死亡率を下げなかった（39.7%対41.3%）。 | SRC-199（RESTRICTED）Thiele H, Zeymer U, Neumann FJ, et al. Intraaortic balloon support for… | 10.1056/NEJMoa1208410 |
| HF-024 | 多枝病変のある急性心筋梗塞による心原性ショック患者706人を対象としたCULPRIT-SHOCK試験では、責任病変だけのPCIは即時の多枝PCIより、30日以内の死亡または腎代替療法を要する腎不全が少なかった（45.9%… | SRC-200（RESTRICTED）Thiele H, Akin I, Sandri M, et al. PCI Strategies in Patients with Acu… | 10.1056/NEJMoa1710261 |
| HF-025 | ST上昇型心筋梗塞による心原性ショック患者360人を対象としたDanGer Shock試験では、経皮的微小軸流ポンプ（Impella CP）の追加で180日死亡が58.5%から45.8%に減った（ハザード比0.74）が、… | SRC-201（RESTRICTED）Møller JE, Engstrøm T, Jensen LO, et al. Microaxial Flow Pump or Stand… | 10.1056/NEJMoa2312572 |
| HF-027 | 米国心臓協会の科学声明では、右心不全の原因は、右室心筋症などの右室自体の障害、右室の虚血と梗塞、先天性心疾患や弁膜症による容量負荷、肺動脈弁狭窄や肺高血圧（左心疾患に伴うものを含む）による圧負荷に整理される。 | SRC-4380（RESTRICTED）Konstam MA, et al. Circulation. 2018;137(20):e578-e622. | 10.1161/CIR.0000000000000560 |
| HF-028 | 右心不全の臨床像は、体静脈うっ血による徴候が主体であり、頸静脈怒張、肝腫大、腹水、下腿浮腫が中心となる。左心不全で中心となる肺うっ血の徴候には乏しいことが多い。 | SRC-4380（RESTRICTED）Konstam MA, et al. Circulation. 2018;137(20):e578-e622. | 10.1161/CIR.0000000000000560 |
| HF-029 | 慢性右心不全の管理の軸は、利尿薬による体液量の管理と原因疾患の治療であり、右室機能そのものを特異的に改善する確立した薬物療法はない。右室の大きさと機能の評価には心臓MRIが標準的な方法とされる。 | SRC-4380（RESTRICTED）Konstam MA, et al. Circulation. 2018;137(20):e578-e622. | 10.1161/CIR.0000000000000560 |
| HF-030 | 右心不全は、心臓の構造的または機能的な障害により、右室の充満や右室から前方への血液の拍出が障害される臨床症候群である。原因として最も頻度が高いのは左心不全による後方障害（左心疾患に伴う肺高血圧症）であり、そのほか機序別に… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| HF-031 | 右心不全の治療は原因となる病態生理によって異なり、体うっ血がある場合には特に利尿薬を用い、うっ血がない場合には慎重に輸液を行う。末梢の低灌流や持続する低血圧がある場合には強心薬を用い、それでも改善しなければ腎代替療法や右… | SRC-185（RESTRICTED）Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosi… | 10.1253/circj.CJ-25-0002 |
| PV-001 | ERS/ATS の2017年の非侵襲的換気ガイドラインは、心原性肺水腫による急性呼吸不全に、バイレベル NIV または CPAP のいずれかを使うことを強く推奨した（エビデンスの確実性は中等度）。心原性ショックと急性冠症… | SRC-439（RESTRICTED）Rochwerg B, Brochard L, Elliott MW, et al. Official ERS/ATS clinical p… | — |
| PV-002 | 2026年の AHA/ACC ほかの急性肺血栓塞栓症ガイドラインは、従来の「広範型」「亜広範型」に代えて、A（無症状・偶発的）、B（症状があり臨床重症度スコアが低い）、C（臨床重症度スコアが高い）、D（心肺不全の初期）、… | SRC-440（UNKNOWN）Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCA… | 10.1161/CIR.0000000000001415 |
| PV-003 | 2026年の AHA/ACC ほかのガイドラインでは、症状があり臨床重症度スコアが低い（PESI I〜II、sPESI 0、Hestia 0 など）カテゴリー B の急性肺血栓塞栓症は一般に早期退院が可能とし、カテゴリー… | SRC-440（UNKNOWN）Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCA… | 10.1161/CIR.0000000000001415 |
| PV-004 | 2026年の AHA/ACC ほかのガイドラインでは、カテゴリー E1（持続する低血圧）には血栓溶解などの高度治療が妥当とされ、カテゴリー D1〜D2（正常血圧のショックなど心肺不全の初期）では考慮してよいとされた。肺塞… | SRC-440（UNKNOWN）Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCA… | 10.1161/CIR.0000000000001415 |
| PV-005 | 2026年の AHA/ACC ほかのガイドラインは、肺血栓塞栓症の検査前確率を問診と身体診察で評価することを推奨し（COR 1、LOE A）、確率が高い（50%超）か D ダイマーが上昇している場合に画像検査を行うことを… | SRC-440（UNKNOWN）Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCA… | 10.1161/CIR.0000000000001415 |
| PV-006 | 2026年の AHA/ACC ほかのガイドラインでは、検査前確率が低〜中等度（50%未満）の患者で、年齢調整 D ダイマー（年齢×10 μg/L FEU）が閾値未満であれば肺血栓塞栓症を除外することが妥当とされた（COR… | SRC-440（UNKNOWN）Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCA… | 10.1161/CIR.0000000000001415 |
| PV-007 | 2026年の AHA/ACC ほかのガイドラインは、急性肺血栓塞栓症の確定には換気血流シンチグラフィより CT 肺動脈造影を推奨し（COR 1、LOE B-R）、CT 肺動脈造影の陽性か換気血流シンチグラフィの高確率所見… | SRC-440（UNKNOWN）Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCA… | 10.1161/CIR.0000000000001415 |
| PV-008 | 2026年の AHA/ACC ほかのガイドラインは、肺血栓塞栓症の診断を確定または否定する目的で心エコーを使うことは推奨しない（COR 3：利益なし）とした。 | SRC-440（UNKNOWN）Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCA… | 10.1161/CIR.0000000000001415 |
| PV-009 | 2026年の AHA/ACC ほかのガイドラインは、急性肺血栓塞栓症の初期の非経口抗凝固薬として未分画ヘパリンより低分子ヘパリンを、経口抗凝固薬としてはワルファリンなどのビタミン K 拮抗薬より直接経口抗凝固薬を推奨した… | SRC-440（UNKNOWN）Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCA… | 10.1161/CIR.0000000000001415 |
| PV-010 | 2026年の AHA/ACC ほかのガイドラインは、大きな可逆的危険因子のない初回の肺血栓塞栓症や、危険因子が持続する場合には、抗凝固療法を3〜6か月で終えずに継続することとした。 | SRC-440（UNKNOWN）Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCA… | 10.1161/CIR.0000000000001415 |
| PV-011 | PEITHO 試験で、右室機能障害とトロポニン陽性を伴う正常血圧の中間リスク肺血栓塞栓症にテネクテプラーゼを加えると、7日以内の死亡または血行動態の破綻は減った（2.6% 対 5.6%）が、30日死亡率には差がなかった（… | SRC-441（UNKNOWN）Meyer G, Vicaut E, Danays T, et al（PEITHO Investigators）. Fibrinolysis… | 10.1056/NEJMoa1302097 |
| PV-012 | PEITHO 試験で、テネクテプラーゼ群は頭蓋外出血（6.3% 対 1.2%）と脳卒中（2.4% 対 0.2%、多くは出血性）が多かった。 | SRC-441（UNKNOWN）Meyer G, Vicaut E, Danays T, et al（PEITHO Investigators）. Fibrinolysis… | 10.1056/NEJMoa1302097 |
| PV-013 | 急性肺血栓塞栓症の患者を追跡した前向き研究で、症候性の慢性血栓塞栓性肺高血圧症の累積発生率は6か月で1.0%、1年で3.1%、2年で3.8%で、2年以降の発生はなかった。 | SRC-442（UNKNOWN）Pengo V, Lensing AWA, Prins MH, et al. Incidence of Chronic Thromboemb… | — |
| PV-014 | 急性肺血栓塞栓症後の慢性血栓塞栓性肺高血圧症の発生には、肺血栓塞栓症の既往、特発性の肺血栓塞栓症、血流欠損が大きいこと、若い年齢が関連した。 | SRC-442（UNKNOWN）Pengo V, Lensing AWA, Prins MH, et al. Incidence of Chronic Thromboemb… | — |
| PV-015 | 2026年の AHA/ACC ほかのガイドラインは、肺血栓塞栓症の患者には少なくとも1年間、受診のたびに症状と機能の制限を尋ね、慢性血栓塞栓性肺疾患を見逃さないようにすることとした。 | SRC-440（UNKNOWN）Creager MA, Barnes GD, Giri J, et al. 2026 AHA/ACC/ACCP/ACEP/CHEST/SCA… | 10.1161/CIR.0000000000001415 |
| PV-016 | 2022年の ESC/ERS ガイドラインは、3か月以上の抗凝固療法後も症状があり、換気血流のミスマッチと慢性の器質化血栓の所見がある状態を、肺高血圧の有無にかかわらず慢性血栓塞栓性肺疾患（CTEPD）という概念で扱った… | SRC-444（RESTRICTED）Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the… | 10.1183/13993003.00879-2022 |
| PV-017 | 2022年の ESC/ERS ガイドラインでは、慢性血栓塞栓性肺高血圧症の治療は手術（肺動脈血栓内膜摘除術）、肺高血圧症治療薬、バルーン肺動脈形成術を組み合わせて行い、抗凝固療法は生涯続ける。 | SRC-444（RESTRICTED）Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the… | 10.1183/13993003.00879-2022 |
| PV-018 | 手術不能の慢性血栓塞栓性肺高血圧症、または肺動脈血栓内膜摘除術後も残存・再発した肺高血圧症の患者261人を対象とした CHEST-1 試験で、可溶性グアニル酸シクラーゼ刺激薬リオシグアトは16週の6分間歩行距離をプラセボ… | SRC-443（UNKNOWN）Ghofrani HA, D'Armini AM, Grimminger F, et al（CHEST-1 Study Group）. Ri… | — |
| PV-019 | 2022年の ESC/ERS ガイドラインは、肺高血圧症を安静時の平均肺動脈圧20 mmHg 超と定義し、肺動脈性肺高血圧症ではさらに肺血管抵抗2 WU 超と肺動脈楔入圧15 mmHg 以下を満たすこととした。 | SRC-444（RESTRICTED）Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the… | 10.1183/13993003.00879-2022 |
| PV-020 | 左心系疾患に伴う肺高血圧症は臨床分類の第2群にあたり、肺動脈楔入圧の上昇を伴う毛細血管後性の肺高血圧症である。 | SRC-444（RESTRICTED）Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the… | 10.1183/13993003.00879-2022 |
| PV-021 | 治療歴のない WHO 機能分類 II〜III 度の肺動脈性肺高血圧症500人を対象とした AMBITION 試験で、アンブリセンタンとタダラフィルの初期併用は、各単剤（合算）と比べて臨床的失敗の発生を半減させた（18% … | SRC-445（UNKNOWN）Galiè N, Barberà JA, Frost AE, et al（AMBITION Investigators）. Initial … | 10.1056/NEJMoa1413687 |
| PV-022 | 2022年の ESC/ERS ガイドラインでは、肺動脈性肺高血圧症の治療は、リスク評価・併存症・治療目標にもとづいて進め、初期からの併用療法と経過観察時の治療強化が標準とされた。 | SRC-444（RESTRICTED）Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the… | 10.1183/13993003.00879-2022 |
| PV-023 | 既存の治療を続けている WHO 機能分類 II〜III 度の肺動脈性肺高血圧症を対象とした STELLAR 試験で、アクチビンシグナル阻害薬ソタテルセプトの3週ごとの皮下注射は、24週の6分間歩行距離をプラセボより延ばし… | SRC-446（UNKNOWN）Hoeper MM, Badesch DB, Ghofrani HA, et al（STELLAR Trial Investigators）… | 10.1056/NEJMoa2213558 |
| PV-024 | 2022年の ESC/ERS ガイドラインでは、肺高血圧症の妊婦は多職種のそろった肺高血圧症センターで管理し、エンドセリン受容体拮抗薬・リオシグアト・セレキシパグは中止するとされた。 | SRC-444（RESTRICTED）Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the… | 10.1183/13993003.00879-2022 |
| PV-025 | 右心カテーテルで確認した間質性肺疾患に伴う肺高血圧症326人を対象とした INCREASE 試験で、トレプロスチニル吸入は16週の6分間歩行距離をプラセボより31.12 m 延ばし、臨床的な悪化を減らした（22.7% 対… | SRC-447（UNKNOWN）Waxman A, Restrepo-Jaramillo R, Thenappan T, et al. Inhaled Treprostin… | 10.1056/NEJMoa2008470 |
| PV-026 | 2022年の ESC/ERS ガイドラインは、肺疾患に伴う肺高血圧症（第3群）に初めて薬物療法の推奨を設けた。治療はまず肺疾患の最適化から始め、重症の間質性肺疾患に伴う肺高血圧症では、肺高血圧症センターで個別に判断したう… | SRC-444（RESTRICTED）Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the… | 10.1183/13993003.00879-2022 |
| PV-027 | 英国 MRC の試験（1981年）で、慢性気管支炎・肺気腫による慢性の低酸素性肺性心（高度の低酸素血症と CO2 貯留、うっ血性心不全の既往）の70歳未満の患者87人に、1日15時間以上の在宅酸素療法を行うと、5年間の死… | SRC-448（UNKNOWN）Medical Research Council Working Party. Long term domiciliary oxygen t… | 10.1016/S0140-6736(81)91970-X |
| PV-028 | 英国 MRC の在宅酸素療法の試験では、死亡は動脈血 CO2 分圧と赤血球量を組み合わせた指標で一部予測され、酸素療法は呼吸不全の増悪による入院日数や就労には影響しなかった。 | SRC-448（UNKNOWN）Medical Research Council Working Party. Long term domiciliary oxygen t… | 10.1016/S0140-6736(81)91970-X |
| PV-029 | 2020年の第2版国際 HHT ガイドラインは、遺伝性出血性毛細血管拡張症（HHT）の、またはその可能性がある無症状の小児に、診断時に胸部 X 線とパルスオキシメトリ、または経胸壁コントラスト心エコーで肺動静脈奇形のスク… | SRC-449（UNKNOWN）Faughnan ME, Mager JJ, Hetts SW, et al. Second International Guideline… | 10.7326/M20-1443 |
| PV-030 | 2020年の第2版国際 HHT ガイドラインは、小児の大きな肺動静脈奇形や酸素飽和度の低下を伴うものを治療して重い合併症を防ぐことを強く推奨し、流入動脈の径が3 mm 以上のものは塞栓術の対象とした。 | SRC-449（UNKNOWN）Faughnan ME, Mager JJ, Hetts SW, et al. Second International Guideline… | 10.7326/M20-1443 |
| PV-031 | 2020年の第2版国際 HHT ガイドラインの補足資料は、無症状の肺動静脈奇形の妊娠中のスクリーニングを妊娠12〜20週に行い、症状のあるものはすぐに塞栓術を行うとし、生理食塩水による経胸壁コントラスト心エコーは妊娠中も… | SRC-449（UNKNOWN）Faughnan ME, Mager JJ, Hetts SW, et al. Second International Guideline… | 10.7326/M20-1443 |
| PV-032 | 左心系疾患に伴う肺高血圧症（臨床分類の第2群）は毛細血管後性で、血行動態の定義は平均肺動脈圧20 mmHg超かつ肺動脈楔入圧15 mmHg超であり、肺血管抵抗2 Wood単位以下を孤立性毛細血管後性、2 Wood単位を超… | SRC-444（RESTRICTED）Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the… | 10.1183/13993003.00879-2022 |
| BL-001 | 造血幹細胞は多能性と自己複製能を併せ持つ細胞で、すべての機能的な血液細胞に分化することができ、短命な成熟血球を生涯にわたって補充し続ける | SRC-2478（RESTRICTED）Seita J, Weissman IL. Hematopoietic stem cell: self-renewal versus dif… | 10.1002/wsbm.86 |
| BL-002 | 貧血の評価では赤血球指数を含む血算が診断の手がかりとなり、網赤血球数は溶血または失血のスクリーニングとして有用である | SRC-2479（RESTRICTED）Cascio MJ, DeLoughery TG. Anemia: Evaluation and Diagnostic Tests. Med… | 10.1016/j.mcna.2016.09.003 |
| BL-003 | 成人の貧血の鑑別診断は、平均赤血球容積（MCV）に基づいて小球性・正球性・大球性に細分類することで大幅に絞り込むことができるが、この分類は診断の出発点であって絶対的なものではない | SRC-2480（RESTRICTED）Tefferi A. Anemia in adults: a contemporary approach to diagnosis. May… | 10.4065/78.10.1274 |
| BL-004 | 末梢血塗抹は、自動血球計数や分子生物学的技術が進歩した現在でも重要な診断検査であり、その所見は患者の臨床像と合わせて解釈する必要がある | SRC-2481（UNKNOWN）Adewoyin AS, Nwogoh B. Peripheral blood film - a review. Ann Ib Postgr… | — |
| BL-005 | 日本の診断基準では、溶血性貧血は、貧血と黄疸を前提として、ヘモグロビン低下・網赤血球増加・間接ビリルビン上昇・ウロビリン体増加・ハプトグロビン低下・骨髄赤芽球増加のうち4項目以上を満たすことで診断する | SRC-2482（UNKNOWN）特発性造血障害に関する調査研究班『自己免疫性溶血性貧血診療の参照ガイド 令和4年度改訂版』（2023年3月） | — |
| BL-006 | 炎症がない状況では血清フェリチンは鉄欠乏の最も特異的な検査であり、15 µg/L 未満は貯蔵鉄の欠如、30 µg/L 未満は体内の鉄貯蔵が低い状態を示し、トランスフェリン飽和度20%未満は鉄制限の指標となる | SRC-164（RESTRICTED）Snook J, Bhala N, Beales ILP, et al. British Society of Gastroenterolo… | 10.1136/gutjnl-2021-325210 |
| BL-007 | 日本では、厚生労働省の『血液製剤の使用指針』『輸血療法の実施に関する指針』『血液製剤保管管理マニュアル』の3指針が2026年3月24日付の通知で廃止され、日本輸血・細胞治療学会の『輸血療法実践ガイド』に整理・統合された | SRC-2483（RESTRICTED）日本輸血・細胞治療学会『輸血療法実践ガイド』（2026年6月、学会発行） | — |
| BL-008 | 成人の赤血球輸血では、制限的な輸血閾値（典型的にヘモグロビン7〜8 g/dL）は自由な輸血閾値（9〜10 g/dL）と比べて患者の重要なアウトカムを悪化させないとする中等度の質のエビデンスがある（ランダム化比較試験45件… | SRC-2475（RESTRICTED）Carson JL, et al. Red Blood Cell Transfusion: 2023 AABB International … | 10.1001/jama.2023.12914 |
| BL-009 | 輸血関連急性肺障害（TRALI）は2019年の国際的な専門家の合意で再定義され、「possible TRALI」の用語は廃止されて、ARDS の危険因子がない例を TRALI Type I、危険因子がある例を Type … | SRC-2484（RESTRICTED）Vlaar APJ, Toy P, Fung M, et al. A consensus redefinition of transfusi… | 10.1111/trf.15311 |
| BL-010 | 輸血関連循環過負荷（TACO）には国際輸血学会・国際ヘモビジランスネットワーク・AABB が策定し検証した改訂版サーベイランス定義があり、TACO は輸血体制の整った国々で輸血関連の罹患・死亡の主要因の一つである | SRC-2485（RESTRICTED）Wiersum-Osselton JC, et al. Revised international surveillance case de… | 10.1016/S2352-3026(19)30080-8 |
| BL-011 | 日本で2024年に医療機関から日本赤十字社へ報告された輸血副作用・感染症は計3,140件で、このうち溶血性副作用は26件（即時性11件・遅発性15件、うち重篤19件）であった | SRC-2486（UNKNOWN）日本赤十字社. Haemovigilance by JRCS 2024（日本赤十字社公式 PDF） | — |
| BL-012 | 重症外傷の大量輸血で血漿・血小板・赤血球を1対1対1の比で投与しても、1対1対2の比と比べて24時間および30日の死亡率に有意な差はなかったが、失血による死亡は1対1対1の群で有意に少なかった | SRC-2487（RESTRICTED）Holcomb JB, Tilley BC, Baraniuk S, et al. Transfusion of plasma, plate… | 10.1001/jama.2015.12 |
| BL-013 | 日本における2024年の造血細胞移植は自家移植と同種移植を合わせて5,333件で、前年より約450件減少し、減少の主因はリンパ腫・形質細胞腫瘍に対する自家移植の減少であった | SRC-2488（UNKNOWN）日本造血細胞移植データセンター／日本造血・免疫細胞療法学会『日本における造血細胞移植/細胞治療．2025年度 全国調査報告書』 | — |
| BL-014 | プロトロンビン時間（PT）と活性化部分トロンボプラスチン時間（APTT）は最も頻繁に測定される凝固検査で、抗凝固療法のモニタリングや出血の初期評価に用いられ、延長がみられた場合は結果に影響する因子を踏まえて系統的に評価す… | SRC-2489（RESTRICTED）Kamal AH, Tefferi A, Pruthi RK. How to interpret and pursue an abnorma… | 10.4065/82.7.864 |
| GR-001 | 小児の成長の評価では、病歴と身体所見に加えて、身長・体重などの計測値を成長曲線上で経時的に追う評価（オークソロジー）が最も重要な方法である。低身長は小児内分泌医への紹介理由として最も頻度が高く、単一時点の身長だけでなく、… | SRC-1027（UNKNOWN）Collett-Solberg PF, Ambler G, Backeljauw PF, et al. Diagnosis, Genetic… | 10.1159/000502231 |
| GR-002 | 低身長・成長障害の鑑別では、成長ホルモン分泌不全症（GHD）、特発性低身長症（ISS）、原発性IGF-I欠損症（PIGFD）の3つの病態の区別がしばしば困難である。小児内分泌学会のガイドライン（2016）はこの3病態を対… | SRC-1026（UNKNOWN）Grimberg A, DiVall SA, Polychronakos C, et al. Guidelines for Growth H… | 10.1159/000452150 |
| GR-003 | 発達の遅れの早期発見では、すべての健診の機会に発達サーベイランスを行い、標準化された発達スクリーニング検査を生後9か月・18か月・30か月の健診で実施する体制が、米国小児科学会の臨床報告（2020）で示されている。サーベ… | SRC-3529（RESTRICTED）Lipkin PH, Macias MM; Council on Children With Disabilities. Promoting… | 10.1542/peds.2019-3449 |
