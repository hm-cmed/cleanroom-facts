# 食道（第1回）事実票 完成版：未解決事項の解消結果（2026-10-10）

**結論：今回の版で、出典を照合できた中核部分の事実票は確定しました。全件を verified_sources にすることはできていません。**

- **ライセンス（Crossrefで3件確定）**：Baveno VIIにはCCの表示がなく、JGES食道ESD/EMR GLはWiley規約、KEYNOTE-590の5年追跡はCC BY-NC-ND 4.0です。
- **国内の承認・保険（4件確定）**：ARMSは2022年4月に保険収載、術後ニボルマブは2021年11月25日に承認、EoEに保険適用薬はない、静脈瘤の所見は6項目で記載する。
- **がん統計**：最新値（罹患は2023年、死亡は2024年）に更新しました。
- **PMID**：PubMedとPMCが自動アクセスを拒否（reCAPTCHA・robots）したため、NEJM掲載RCTのPMIDの多くは直接照合できませんでした。記憶由来の候補PMIDはいったん全件削除しました。そのうえで、最終の照合工程（PubMedの論評レコード、ClinicalTrials.govの文献表）で書誌との対応を確認できたものだけを復元しています。
- **未確定分**：draftのまま残し、カードごとに理由を書きました。

## TL;DR
- **確定**：JCOG1109（PMID 38876133）、KEYNOTE-590（PMID 34454674、5年OSは10.9%対3.1%）、ESGE異物GL（PMID 26862844）、ESGE静脈瘤GL 2022（PMID 36174643）、Lyon 2.0のAET閾値（6%超で確定、4%未満で生理的）、Chicago v4.0のDCI・DL閾値、ALDH2ヘテロ型の飲酒者の食道癌OR（日本・台湾の症例対照研究で3.7〜18.1、PLoS Med、CC BY）、国立がん研究センター統計（2023年罹患25,889例、2024年死亡10,638人）。
- **国内状況**：ARMSとESD-Gは「内視鏡的逆流防止粘膜切除術（K653-6、12,000点）」として2022年4月に保険収載されました。ニボルマブの食道癌術後補助療法は2021年11月25日に承認されました。EoEへのデュピルマブは、今回の調査では国内承認の記録が見つかりませんでした。局所ステロイドを含め、EoEに保険適用薬はありません（2024年時点の大学病院資料による。2026年時点は要確認）。
- **残課題（draftまたは作成保留）**：
  - CheckMate 648のPMIDと本文。García-Pagán 2010のPMIDの独立照合。
  - JSGE GERD GL 2021本文の用量とCQ。
  - Chicago v4.0の正常値データベースの人数とオピオイドの割合。
  - ACG 2020のIII型アカラシアに対する推奨。
  - 出典を取得できなかった新規疾患（裂孔ヘルニア、薬剤性、カンジダ、Plummer-Vinson、Zenker、Mallory-Weiss、EREFS）は作成を保留。
  - コアカリと国試出題基準の番号は全件要確認。

## 重要な前提（作業上の制約）
- 本セッションでは前回版のYAML本文（ES-001〜067）を参照できませんでした。そのため本版は次の3部構成です。
  - (a) 出典マスター（SRC）
  - (b) 改訂カード（ES-R01〜）。統合時に前回の該当IDを引き継ぎます。
  - (c) 新規カード（ES-069〜）
- PMIDを確定扱いにしたのは、PubMedの別レコード、ClinicalTrials.govの文献表、出版社ページのいずれかで、書誌とPMIDの対応を直接確認できたものに限ります。

## 1. 解消結果の一覧表

| 項目 | 結果 | 出典（確認経路） |
|---|---|---|
| JCOG1109 NExT | **確定**：PMID 38876133、Lancet 2024;404(10447):55-66、DOI 10.1016/S0140-6736(24)00745-1。601例（CF 199／DCF 202／CF-RT 200）。\[1\]\[2\]B | PubMed（論評 PMID 38876135 の「Comment on」欄）、Ann Surg Oncol探索的解析 |
| CheckMate 577 | DOIのみ確定。**PMIDは未照合（null）**。DFS中央値22.4対11.0か月。最終OSは有意差なし。OSの数値はASCO抄録（Kelly RJ, JCO 2025;43(16_suppl):4000, DOI 10.1200/JCO.2025.43.16_suppl.4000）で確認：中央値51.7対35.3か月、HR 0.85（95.87%CI 0.70–1.04）。5年OS 46%対41%は未確認 | Verhoeven, Int J Cancer 2026（PMC12765972）、ascopubsの抄録 |
| CheckMate 648 | **PMIDは削除**（照合不能）。draft | — |
| POEM vs LHM（Werner 2019） | **確定**：PMID 31800987、DOI 10.1056/NEJMoa1905380 | PubMed（論評 PMID 32242371 の「Comment on」欄） |
| デュピルマブ EoE（Dellon 2022） | **確定**：PMID 36546624、DOI 10.1056/NEJMoa2205982。パートAの組織学的寛解は60%（25/42）対5%（2/39） | PubMed、ClinicalTrials.gov NCT03633617 |
| Villanueva 2013 | **確定**：PMID 23281973、NEJM 2013;368(1):11-21、DOI 10.1056/NEJMoa1211801。921例（制限群461、自由群460） | PubMed、ClinicalTrials.gov NCT00414713 |
| García-Pagán 2010 | PMID 20573925 は依頼者提示の値として残します。本セッションでは独立に照合していません | — |
| KEYNOTE-590 | **確定**：原著 PMID 34454674。5年追跡は Metges JP, ESMO Open 2025;10(12):105854、**CC BY-NC-ND 4.0**→B。5年OS 10.9%対3.1%、追跡中央値58.8か月。日本人の5年追跡は PMID 42047965（PMC13319894） | ClinicalTrials.gov NCT03189719、Crossref、PubMed |
| JGES 食道ESD/EMR GL | 書誌を確定（Dig Endosc 2020;32:452-493、DOI 10.1111/den.13654、18 CQ）。**Wiley規約（CCなし）→B**。\[3\]PMIDは未取得 | Crossref |
| JSGE GERD GL 2021 | PMC8938399の本文を取得できませんでした（reCAPTCHA）。用量・CQ・RE有病率の確認は**未了** | — |
| ACG Barrett 2022／AGREE／ACG EoE 2025／Lundell 1999／Oyama 2017／食道癌GL 2022 Part 2 | **PMIDは削除**。既知のDOIとPMCIDは保持 | — |
| Baveno VII | Crossrefのライセンス欄はElsevier TDMのみで、**CC BY-NC-NDの表示はありません→B** | Crossref |
| ESGE 静脈瘤GL 2022 | **確定**：PMID 36174643、Endoscopy 2022;54(11):1094-1120、DOI 10.1055/a-1939-4887。\[4\]ライセンス未確認→E | ClinicalTrials.govの文献表 |
| W03・W06・W12〜W14・W18・W19 | 前回のホワイトリスト本文を参照できず、**未了** | — |
| Lyon 2.0 | **確定**：AET 6%超で確定、4%未満で生理的、4〜6%は判定保留。LA分類B以上で確定。\[5\]\[6\]\[7\]Gut 2024;73(2):361-371、DOI 10.1136/gutjnl-2023-330616、「Re-use permitted under CC BY-NC」→B | PMC13425011、PMC12470591、WUSTL Digital Commons |
| Chicago v4.0 | **確定**：DCIの閾値（450／100／8,000 mmHg·s·cm）。DL 4.5秒未満かつDCI 450以上で早期収縮。**正常値の人数とオピオイドの割合は未了** | PMC8034247 |
| III型アカラシアとPOEM（ACG 2020） | **未了** | — |
| ALDH2ヘテロ型 | **確定（A）**：日本・台湾の症例対照研究で、飲酒者のOR 3.7〜18.1。メタ解析ではヘテロ型のOR 3.19 | Brooks, PLoS Med 2009（CC BY）、Lewis, CEBP 2005（PMID 16103445） |
| EoEの国内承認（デュピルマブ・局所ステロイド） | 国内承認の記録なし。EoEに保険適用薬はない（2024年時点）。\[8\]draft | サノフィIF（2026年3月改訂）、慶應病院（2024年5月） |
| ARMS 保険収載 | **確定**：2022年4月新設、K653-6、12,000点 | 外保連資料、Gastroenterol Endosc 65(6) |
| 術後ニボルマブ | **確定**：2021年11月25日承認 | 小野薬品・BMSの文書 |
| 静脈瘤内視鏡所見記載基準 | **確定**：L・F・C・RC・BS・MFの6項目\[9\]\[10\] | 日消誌116(5):395、日内会誌103(5):1187 |
| 肝硬変GL 2020（英語版） | J Gastroenterol 2021;56:593-619、PMC8280040。\[11\]\[12\]CCの種別は未確認→E。2025年版は**未了** | Springer、PMC |
| がん統計 | **確定**：2023年罹患25,889例、2024年死亡10,638人\[13\] | 国立がん研究センター がん情報サービス |
| ES-068の分割 | ES-069〜089を採番。内訳は verified 11件、draft 3件、作成保留（欠番）7件 | 3-3参照 |
| コアカリ・国試出題基準 | **未了**（全件要確認） | — |

## 2. 抽出元ホワイトリスト（確定版）

| SRC | 資料 | 書誌・識別子 | ライセンス確認 | basis_tag |
|---|---|---|---|---|
| SRC-01 | Kato K, JCOG1109 | Lancet 2024;404:55-66, PMID 38876133 | 非CC | B |
| SRC-02 | Kelly RJ, CheckMate 577 | NEJM 2021;384:1191-1203, DOI 10.1056/NEJMoa2032125 | 非CC | B |
| SRC-03 | Doki Y, CheckMate 648 | NEJM 2022;386:449-462, DOI 10.1056/NEJMoa2111380 | 非CC | B |
| SRC-04 | Sun JM, KEYNOTE-590 | Lancet 2021;398:759-771, PMID 34454674 | 非CC | B |
| SRC-05 | Metges JP, KEYNOTE-590 5年 | ESMO Open 2025;10(12):105854 | CC BY-NC-ND 4.0（Crossref） | B |
| SRC-06 | Ishihara R, JGES食道ESD/EMR GL | Dig Endosc 2020;32:452-493 | Wiley規約（Crossref） | B |
| SRC-07 | de Franchis R, Baveno VII | J Hepatol 2022;76:959-974 | Elsevier TDMのみ | B |
| SRC-08 | Gralnek IM, ESGE静脈瘤GL | Endoscopy 2022;54:1094-1120, PMID 36174643 | 未確認 | E |
| SRC-09 | Birk M, ESGE異物GL | Endoscopy 2016;48:489-496, PMID 26862844 | 未確認 | E |
| SRC-10 | Gyawali CP, Lyon 2.0 | Gut 2024;73:361-371, DOI 10.1136/gutjnl-2023-330616 | CC BY-NC（WUSTLの記録） | B |
| SRC-11 | Yadlapati R, Chicago v4.0 | Neurogastroenterol Motil 2021, PMC8034247 | 未確認 | E |
| SRC-12 | Brooks PJ, Alcohol flushing response | PLoS Med 2009, DOI 10.1371/journal.pmed.1000050 | CC BY | A |
| SRC-13 | Lewis SJ, ALDH2メタ解析 | CEBP 2005;14:1967, PMID 16103445 | 非CC | B |
| SRC-14 | 国立がん研究センター がん統計 | ganjoho.jp 食道 | 元データは政府統計。サイトの規約は未確認 | C |
| SRC-15 | 診療報酬点数表 K653-6 | 令和4年度改定 | 告示原本は未閲覧 | C |
| SRC-16 | 小野薬品・BMS 適正使用文書 | 2021-11-26 | 企業資料 | B |
| SRC-17 | 門脈圧亢進症取扱い規約 第3版の記載基準 | 日消誌116(5):395、日内会誌103(5):1187 | 非CC | B |
| SRC-18 | Yoshiji H, 肝硬変GL 2020 | J Gastroenterol 2021;56:593-619, PMC8280040 | 種別は未確認 | E |
| SRC-19 | Verhoeven RHA, CheckMate 577 実臨床 | Int J Cancer 2026, PMC12765972 | 未確認 | E |
| SRC-20 | Contini S, 腐食性傷害の総説 | World J Gastroenterol 2013;19(25):3918 | CC BY-NC | B |
| SRC-21 | Cheng HT, 成人の腐食性物質摂取 | BMC Gastroenterol 2008, PMC2533005 | CC BY | A |
| SRC-22 | Boerhaave Syndrome—Narrative Review | Diagnostics 2025;15(19):2463, PMC12524210 | CC BY 4.0 | A |
| SRC-23 | HSV/CMV食道共感染の症例と文献レビュー | IDCases 2020, PMC7519373 | 未確認 | E |
| SRC-24 | HSV vs CMV食道炎の内視鏡所見 | Medicine 2019, DOI 10.1097/MD.0000000000015845 | 未確認 | E |
| SRC-25 | Werner YB, POEM vs LHM | NEJM 2019;381:2219-2229, PMID 31800987 | 非CC | B |
| SRC-26 | Dellon ES, デュピルマブ EoE | NEJM 2022;387:2317-2330, PMID 36546624 | 非CC | B |
| SRC-27 | Villanueva C, 輸血戦略 | NEJM 2013;368:11-21, PMID 23281973 | 非CC | B |
| 除外 | ニュースサイト、Medscape、Pathology Outlines、Wikipedia、病院の解説ページ | — | 数値照合の手がかりとしてのみ使用 | — |

## 3. 食道の事実票 完成版YAML

### 3-1. 変更履歴
- **ES-068**：廃止し、ES-069〜089に分割しました。このうちES-076〜078、082〜084、088は出典を取得できなかったため、**欠番（作成保留）**としました。
- **ES-R01〜R19**：前回版の該当カード（同じ出典を持つもの）を全文置換します。統合時は前回のIDを引き継ぎます。
- **全カード共通**：記憶由来の候補PMIDを削除してnullにしました。最終の照合工程で書誌との対応を確認できたもの（Werner、Dellon、Villanueva）だけを復元しています。Baveno VIIとJGES ESD GLを出典とするカードは、basis_tagをBに変更しました。
- **上記以外のES-001〜067**：provenanceをSRCの値で置換します。主張文は**変更していません**。ただし、JSGE GERD GL 2021の用量・CQ・有病率を述べるカードは、本文を確認できていないためdraftのまま据え置きます。

### 3-2. 改訂カード（全文）

```yaml
- id: ES-R01
  assertion:
    plain_statement_ja: "切除可能な局所進行食道扁平上皮癌の術前療法として、ドセタキセルを加えた3剤併用（DCF）はシスプラチン＋5-FU（CF）より全生存を改善した。CFに放射線を加えた群（CF-RT）はCFに対する生存上の優越性を示さなかった。登録は601例（2012年12月〜2018年7月、1:1:1割付）。"\[2\]\[14\]\[15\]
    condition: "cStage IB〜III（UICC第7版）の切除可能な食道扁平上皮癌"
    differential: "術前化学放射線療法（欧米の標準）"
    common_misconception: "放射線を加えれば必ず生存が延びるわけではない"
  provenance:
    source: "Kato K, et al. JCOG1109 NExT. Lancet 2024;404(10447):55-66"
    doi: "10.1016/S0140-6736(24)00745-1"
    pmid: "38876133"
    pmcid: null
    url: "https://pubmed.ncbi.nlm.nih.gov/38876135/"
    source_license: "非CC（Elsevier）"
    basis_tag: B
    corroboration: "Matsuda S, Ann Surg Oncol（JCOG1109探索的解析）"
  uncertainty: "有害事象の割合はニュース照合のみのため主張文に含めない"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R02
  assertion:
    plain_statement_ja: "術前化学放射線療法と切除の後に病理学的残存病変がある食道癌・食道胃接合部癌で、術後ニボルマブはプラセボに比べて無病生存期間を延長した（中央値22.4か月対11.0か月）。最終解析の全生存は統計学的有意差に達しなかった。"\[16\]\[17\]
    condition: "術前CRT後に病理学的完全奏効が得られなかった切除例"
    differential: "日本の標準である術前化学療法（DCF）後の症例は対象外"
    common_misconception: "DFSの改善がそのまま全生存の有意な延長を意味するわけではない"
  provenance:
    source: "Kelly RJ, et al. CheckMate 577. NEJM 2021;384:1191-1203。OS: JCO 2025;43(16_suppl):4000"
    doi: "10.1056/NEJMoa2032125"
    pmid: null
    pmcid: null
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12765972"
    source_license: "非CC"
    basis_tag: B
    corroboration: "Verhoeven RHA, Int J Cancer 2026"
  uncertainty: "PMIDは照合不能のため削除。OSの数値はASCO抄録（Kelly RJ, JCO 2025;43(16_suppl):4000, DOI 10.1200/JCO.2025.43.16_suppl.4000）で確認：中央値51.7対35.3か月、HR 0.85（95.87%CI 0.70–1.04）。5年OS 46%対41%は未確認"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R03
  assertion:
    plain_statement_ja: "切除不能な進行・再発食道扁平上皮癌の一次治療で、ニボルマブ＋化学療法とニボルマブ＋イピリムマブは、化学療法単独に比べて全生存を延長した。"
    condition: "未治療の進行食道扁平上皮癌"
    differential: "KEYNOTE-590（ペムブロリズマブ＋化学療法）"
    common_misconception: "腫瘍PD-L1の発現にかかわらず効果が同じというわけではない"
  provenance:
    source: "Doki Y, et al. CheckMate 648. NEJM 2022;386:449-462"
    doi: "10.1056/NEJMoa2111380"
    pmid: null
    pmcid: null
    url: null
    source_license: "非CC"
    basis_tag: B
    corroboration: null
  uncertainty: "一次資料を閲覧できず、主張文全体が要確認。PMIDは削除"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: ES-R04
  assertion:
    plain_statement_ja: "進行食道癌の一次治療で、ペムブロリズマブ＋化学療法はプラセボ＋化学療法より全生存を改善した。追跡中央値58.8か月での5年全生存率は10.9%対3.1%だった。"\[18\]
    condition: "未治療の進行・転移性食道癌（扁平上皮癌、腺癌、Siewert I型の食道胃接合部腺癌）"
    differential: "CheckMate 648"
    common_misconception: "5年時点でも生存者は少数であり、長期生存の確率が上がったという意味にとどまる"
  provenance:
    source: "Sun JM, Lancet 2021;398:759-771。Metges JP, ESMO Open 2025;10(12):105854"
    doi: "10.1016/j.esmoop.2025.105854"
    pmid: "34454674"
    pmcid: null
    url: "https://www.esmoopen.com/article/S2059-7029(25)01723-5/fulltext"
    source_license: "原著は非CC。5年追跡はCC BY-NC-ND 4.0（Crossref）"
    basis_tag: B
    corroboration: "Kato K, Esophagus 2026（日本人5年、PMID 42047965）"
  uncertainty: "5年追跡論文のPMIDは未取得（pmid欄は原著のもの）"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R05
  assertion:
    plain_statement_ja: "日本では、ニボルマブの「食道癌における術後補助療法」の効能・効果が2021年11月25日に承認された。"\[19\]\[20\]
    condition: "国内の薬事承認"
    differential: "根治切除不能な進行・再発食道癌への適応（2020年2月）"\[21\]
    common_misconception: "術前化学療法（DCF）後の症例への有効性は、CheckMate 577では直接検証されていない"
  provenance:
    source: "小野薬品工業・BMS 食道癌適正使用委員会 文書（2021-11-26）"
    doi: null
    pmid: null
    pmcid: null
    url: "https://www.esophagus.jp/files/opdivo_20211201.pdf"
    source_license: "企業資料（非CC）"
    basis_tag: B
    corroboration: "BMS・小野薬品プレスリリース 2021-11-25"
  uncertainty: "PMDA添付文書の改訂履歴での確認は未実施"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R06
  assertion:
    plain_statement_ja: "アカラシアでは、POEMは腹腔鏡下Heller筋層切開＋Dor噴門形成術に対して2年時の治療成功で非劣性を示した。逆流性食道炎はPOEM群で多かった。"
    condition: "症候性アカラシア"
    differential: "空気圧拡張術"
    common_misconception: "POEMは逆流を起こさない手技ではない"
  provenance:
    source: "Werner YB, et al. NEJM 2019;381:2219-2229"
    doi: "10.1056/NEJMoa1905380"
    pmid: "31800987"
    pmcid: null
    url: null
    source_license: "非CC"
    basis_tag: B
    corroboration: "PubMedの論評 PMID 32242371 の「Comment on」欄で書誌とPMIDを照合"
  uncertainty: "本文未閲覧のため数値は主張文に含めない"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: ES-R07
  assertion:
    plain_statement_ja: "12歳以上の好酸球性食道炎で、デュピルマブ300mgの週1回皮下投与は、プラセボに比べ24週時の組織学的寛解率を高め、嚥下障害の症状スコアを改善した。"\[22\]
    condition: "生検で確定したEoE（好酸球15/HPF以上）"\[22\]
    differential: "PPI、局所ステロイド、食物除去"
    common_misconception: "隔週投与でも同等の症状改善が示されたわけではない"
  provenance:
    source: "Dellon ES, et al. NEJM 2022;387:2317-2330"
    doi: "10.1056/NEJMoa2205982"
    pmid: "36546624"
    pmcid: null
    url: null
    source_license: "非CC"
    basis_tag: B
    corroboration: "PubMed、ClinicalTrials.gov NCT03633617：パートAの組織学的寛解60%（25/42）対5%（2/39）。パートBの隔週投与群は60%（49/81）"
  uncertainty: "本文未閲覧。症状スコアの数値は未確認"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: ES-R08
  assertion:
    plain_statement_ja: "デュピルマブは米国FDAで2022年5月20日に12歳以上（体重40kg以上）のEoEに承認され、2024年1月に1〜11歳（体重15kg以上）へ適応が拡大された。日本では今回の調査でEoEへの承認の記録を確認できなかった。"
    condition: "国内の薬事承認状況"
    differential: "国内で既承認のアトピー性皮膚炎、喘息、COPDなど"\[23\]
    common_misconception: "海外で承認されていても国内で保険適用されるとは限らない"
  provenance:
    source: "デュピクセント 医薬品インタビューフォーム（2026年3月改訂 第20版）、サノフィ国内申請報道"
    doi: null
    pmid: null
    pmcid: null
    url: "https://pro.campus.sanofi/dam/jcr:59fc0e22-fb30-4a68-84c8-25bae10089cf/dupixent_if.pdf"
    source_license: "企業資料（非CC）"
    basis_tag: B
    corroboration: "慶應義塾大学病院 KOMPAS（2024年5月）、サノフィプレスリリース（2022-05-20）"
  uncertainty: "PMDA添付文書の効能・効果欄を全文照合していない。FDA承認日は企業発表で確認したもので、米国政府資料では未照合"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: ES-R09
  assertion:
    plain_statement_ja: "日本では、局所ステロイド（嚥下するブデソニドやフルチカゾン）を含め、EoEを効能とする保険適用薬は2024年時点で存在しない。"\[8\]
    condition: "国内の保険診療"
    differential: "PPI（EoEの初期治療として用いられる）"\[8\]
    common_misconception: "吸入ステロイドの嚥下による使用は適応外使用である"
  provenance:
    source: "慶應義塾大学病院 KOMPAS 好酸球性消化管疾患（2024年5月）"
    doi: null
    pmid: null
    pmcid: null
    url: "https://kompas.hosp.keio.ac.jp/presentation/202405/"
    source_license: "未確認"
    basis_tag: E
    corroboration: "厚労科研 好酸球性消化管疾患 総括研究報告書（2019）"
  uncertainty: "2026年時点の状況は要確認"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: ES-R10
  assertion:
    plain_statement_ja: "急性上部消化管出血では、Hb 7 g/dL未満で輸血する制限的輸血戦略が、9 g/dL未満で輸血する自由輸血戦略より転帰が良かった。"
    condition: "急性上部消化管出血（静脈瘤出血を含む）"
    differential: "虚血性心疾患合併例"
    common_misconception: "出血例では高いHbを目標にすべきとは限らない"
  provenance:
    source: "Villanueva C, et al. NEJM 2013;368(1):11-21"
    doi: "10.1056/NEJMoa1211801"
    pmid: "23281973"
    pmcid: null
    url: null
    source_license: "非CC"
    basis_tag: B
    corroboration: "ClinicalTrials.gov NCT00414713：921例（制限群461、自由群460）"
  uncertainty: "本文未閲覧。転帰の数値は主張文に含めない"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R11
  assertion:
    plain_statement_ja: "急性静脈瘤出血を起こした高リスクの肝硬変（Child-Pugh C 10〜13点、またはBで活動性出血）では、72時間以内の早期TIPSが標準治療に比べ生存を改善した。"
    condition: "高リスクの急性静脈瘤出血"
    differential: "救済（rescue）TIPS"
    common_misconception: "全例に早期TIPSが適応になるわけではない"
  provenance:
    source: "García-Pagán JC, et al. NEJM 2010"
    doi: null
    pmid: "20573925"
    pmcid: null
    url: null
    source_license: "非CC"
    basis_tag: B
    corroboration: null
  uncertainty: "PMIDは依頼者提示の値で、本セッションでは独立に照合していない"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: ES-R12
  assertion:
    plain_statement_ja: "Lyon consensus 2.0では、酸分泌抑制薬を中止して行う逆流モニタリングで、酸曝露時間（AET）が6%を超えればGERDの確定的根拠、4%未満なら生理的範囲、4〜6%は判定保留とする。内視鏡ではLA分類B以上の逆流性食道炎も確定的根拠とされた。"\[5\]\[7\]\[24\]
    condition: "24時間pH（・インピーダンス）検査、または延長ワイヤレスpH検査（2日以上で基準を満たす）"\[5\]\[25\]
    differential: "逆流過敏性食道、機能性胸やけ"
    common_misconception: "LA分類Aは単独ではGERDの確定根拠にならない"\[7\]
  provenance:
    source: "Gyawali CP, et al. Updates to the modern diagnosis of GERD: Lyon consensus 2.0. Gut 2024;73(2):361-371"
    doi: "10.1136/gutjnl-2023-330616"
    pmid: null
    pmcid: null
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC13425011/"
    source_license: "CC BY-NC（WUSTL Digital Commonsの記録「Re-use permitted under CC BY-NC」）"
    basis_tag: B
    corroboration: "PMC12470591、PMID 39694203（ワイヤレスpHの検証）"
  uncertainty: "アジアでAET 4%超を確定閾値とする提案は、Wong & Chen, Gut Liver 2025（PMID 40905050）およびAliment Pharmacol Ther誌のレター（DOI 10.1111/apt.70755）による。Lyon 2.0本体のPMIDは未取得"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R13
  assertion:
    plain_statement_ja: "Chicago分類v4.0では、DCIが450〜8,000 mmHg·s·cmを正常収縮、100以上450未満を弱収縮、100未満を失敗収縮、8,000超を過収縮とする。遠位潜時（DL）が4.5秒未満でDCIが450以上の収縮を早期（攣縮性）収縮とする。"\[26\]\[27\]
    condition: "高解像度食道内圧検査（HRM）"
    differential: "遠位食道攣縮、III型アカラシア"
    common_misconception: "DL 4.5秒未満でもDCIが450未満なら早期収縮ではなく無効収縮に分類される"\[28\]
  provenance:
    source: "Yadlapati R, et al. Chicago Classification v4.0. Neurogastroenterol Motil 2021"
    doi: null
    pmid: null
    pmcid: "PMC8034247"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC8034247/"
    source_license: "PMC著者稿、CC表示は未確認"
    basis_tag: E
    corroboration: "Myers, Annals of Esophagus（III型アカラシアの定義：早期収縮が20%以上）"\[29\]
  uncertainty: "なし（閾値は本文で確認）"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R14
  assertion:
    plain_statement_ja: "オピオイドの使用は、IRPの上昇やDLの短縮を介して、EGJ流出路障害、遠位食道攣縮、III型アカラシアに似た内圧所見を生じうる。Chicago分類v4.0はオピオイド誘発性食道機能障害に注意を促している。"\[30\]\[31\]
    condition: "オピオイド使用中のHRM"
    differential: "原発性アカラシア"
    common_misconception: "内圧所見だけで原発性アカラシアと断定しない"
  provenance:
    source: "Chicago Classification v4.0（PMC8034247）"
    doi: null
    pmid: null
    pmcid: "PMC8034247"
    url: null
    source_license: "未確認"
    basis_tag: E
    corroboration: "総説の二次引用：オピオイド使用66例中83%に異常（遠位食道攣縮45%、EGJOO 27%、III型11%）。原著は未特定"\[29\]
  uncertainty: "割合の原著と正常値データベースの人数は未確認"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: ES-R15
  assertion:
    plain_statement_ja: "ALDH2の低活性ヘテロ型の人が飲酒すると、食道扁平上皮癌のリスクが大きく上がる。日本と台湾の症例対照研究では、飲酒量で調整したオッズ比は3.7〜18.1だった。日本人男性で中等量以上飲酒するヘテロ型の人がすべて少量飲酒にとどまれば、食道扁平上皮癌の53%を予防できる可能性があると試算されている。"\[32\]
    condition: "東アジア人の飲酒者"
    differential: "ALDH2*2ホモ型（飲酒量が少なく、リスクはむしろ低い）"\[33\]
    common_misconception: "フラッシング（顔面紅潮）がある人ほど安全なわけではない。ヘテロ型の目印になる"\[34\]
  provenance:
    source: "Brooks PJ, et al. The alcohol flushing response. PLoS Med 2009;6(3):e1000050"
    doi: "10.1371/journal.pmed.1000050"
    pmid: null
    pmcid: null
    url: "https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.1000050"
    source_license: "CC BY（PLoS）"
    basis_tag: A
    corroboration: "Lewis SJ, CEBP 2005（PMID 16103445）：ヘテロ型OR 3.19、*2/*2型OR 0.36（95%CI 0.16–0.80）"\[35\]
  uncertainty: "53%は試算値（仮定に基づく推計）"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R16
  assertion:
    plain_statement_ja: "日本の食道癌は、2023年に25,889例（男性20,977例、女性4,912例）が診断され、2024年に10,638人（男性8,572人、女性2,066人）が死亡した。罹患・死亡とも男性が約4倍多い。"\[13\]
    condition: "全国がん登録（罹患）、人口動態統計（死亡）"
    differential: "胃癌（2023年罹患104,864例）"\[36\]
    common_misconception: "予測値（2025年の罹患予測26,900例）と実測値を混同しない"\[37\]
  provenance:
    source: "国立がん研究センター がん情報サービス 食道（罹患2026年3月23日更新、死亡2026年1月7日更新）"\[13\]
    doi: null
    pmid: null
    pmcid: null
    url: "https://ganjoho.jp/reg_stat/statistics/stat/cancer/4_esophagus.html"
    source_license: "元データは政府統計。サイトの利用規約は未確認"
    basis_tag: C
    corroboration: "日本対がん協会（2024年の全がん死亡384,111人が一致）"\[38\]
  uncertainty: "ganjoho.jpの利用規約の確認が残る（数値の利用のみ）"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R17
  assertion:
    plain_statement_ja: "日本の食道・胃静脈瘤内視鏡所見記載基準は、占居部位（L）、形態（F）、色調（C）、発赤所見（RC）、出血所見（BS）、粘膜所見（MF）の6項目で記載する。食道ではLs・Lm・Li、F0〜F3、Cw・Cb、RC0〜3（ミミズ腫れ・チェリーレッドスポット・血マメ）を用いる。"\[9\]\[10\]\[39\]
    condition: "門脈圧亢進症取扱い規約 第3版（2013年）"\[39\]
    differential: "胃静脈瘤の部位分類（Lg-c、Lg-cf、Lg-f）"\[9\]
    common_misconception: "F0でも発赤所見があればRC1〜3で記載する"\[10\]
  provenance:
    source: "日本門脈圧亢進症学会 門脈圧亢進症取扱い規約 第3版（記載基準表を日消誌116(5):395、日内会誌103(5):1187で確認）"
    doi: null
    pmid: null
    pmcid: null
    url: "https://www.jstage.jst.go.jp/article/nisshoshi/116/5/116_395/_pdf"
    source_license: "非CC"
    basis_tag: B
    corroboration: "日内会誌103(5):1187（出血所見と粘膜所見E・Ul・S）"\[39\]
  uncertainty: "取扱い規約の最新版（第4版の有無）は要確認"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R18
  assertion:
    plain_statement_ja: "日本の肝硬変診療ガイドライン2020では、食道静脈瘤の初回出血予防にEVLとNSBBがともに有用とされる。再発予防ではEVLとEISの両方が提案されている。胃静脈瘤にはB-RTOが有用とされ、国内研究ではNBCAによるEISより再出血の予防に優れていた。"\[11\]\[40\]\[41\]
    condition: "肝硬変に伴う食道・胃静脈瘤"
    differential: "Baveno VII（カルベジロールを優先する国際コンセンサス）"
    common_misconception: "日本ではEISが今も選択肢であり、EVLに一本化されているわけではない"
  provenance:
    source: "Yoshiji H, et al. Evidence-based clinical practice guidelines for Liver Cirrhosis 2020. J Gastroenterol 2021;56:593-619"
    doi: "10.1007/s00535-021-01788-x"
    pmid: null
    pmcid: "PMC8280040"
    url: "https://link.springer.com/article/10.1007/s00535-021-01788-x"
    source_license: "Springer OA（CC種別は未確認）"
    basis_tag: E
    corroboration: "Hepatol Res 2021版（DOI 10.1111/hepr.13678）"
  uncertainty: "2025年版の推奨は未確認"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-R19
  assertion:
    plain_statement_ja: "薬物抵抗性GERDに対するARMSとESD-Gは、2022年4月の診療報酬改定で「内視鏡的逆流防止粘膜切除術」（K653-6、12,000点）として保険収載された。"\[42\]\[43\]\[44\]
    condition: "国内の保険診療"
    differential: "腹腔鏡下噴門形成術（Nissen法・Toupet法）、ARMA（APC焼灼）"\[45\]
    common_misconception: "ARMAが同じ点数で収載されているかは別途確認が必要"
  provenance:
    source: "診療報酬点数表 K653-6（令和4年新設）"
    doi: null
    pmid: null
    pmcid: null
    url: "https://www.jstage.jst.go.jp/article/gee/65/6/65_1085/_html/-char/ja"
    source_license: "告示は政府標準利用規約。照合したJ-STAGE論文は非CC"
    basis_tag: C
    corroboration: "外保連ニュース（2022年3月）、JGES附置研究会抄録（2024年）"\[46\]\[47\]
  uncertainty: "告示の原本は未閲覧（二次資料3件で一致）"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}
```

### 3-3. 新規カード（ES-068の分割）

欠番（作成保留）は次の7件です。いずれも出典を取得できなかったため、方針に従い主張文を作っていません。第2回の開始前に出典を取得してから起票します。
- ES-076：裂孔ヘルニアI〜IV型
- ES-077：薬剤性食道炎
- ES-078：カンジダ食道炎
- ES-082：Plummer-Vinson症候群
- ES-083：Zenker憩室
- ES-084：Mallory-Weissの自然止血
- ES-088：EREFS

```yaml
- id: ES-069
  assertion:
    plain_statement_ja: "食道を完全に閉塞した異物、食道内の鋭的異物、食道内の電池は、緊急（できれば2時間以内、遅くとも6時間以内）に内視鏡で摘出する。"\[48\]\[49\]
    condition: "成人の上部消化管異物"
    differential: "胃内にある異物（24時間以内の準緊急）"\[50\]
    common_misconception: "症状が軽いボタン電池でも待機してはならない"
  provenance:
    source: "Birk M, et al. ESGE Clinical Guideline. Endoscopy 2016;48:489-496（推奨7）"
    doi: "10.1055/s-0042-100456"
    pmid: "26862844"
    pmcid: null
    url: "https://pubmed.ncbi.nlm.nih.gov/26862844/"
    source_license: "未確認"
    basis_tag: E
    corroboration: "Thieme誌ページ（表3）"
  uncertainty: "小児はESPGHANなど別のGLの対象"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-070
  assertion:
    plain_statement_ja: "完全閉塞のない食道異物は24時間以内に摘出する。胃内の鋭的異物、磁石、電池、大きい・長い異物も24時間以内の内視鏡摘出が推奨される。"\[49\]
    condition: "成人の上部消化管異物"
    differential: "小さく鈍的な無症状の異物（経過観察）"\[50\]
    common_misconception: "磁石は1個だけに見えても準緊急で摘出する"\[48\]
  provenance:
    source: "ESGE異物GL 2016（推奨7・10）"
    doi: "10.1055/s-0042-100456"
    pmid: "26862844"
    pmcid: null
    url: "https://pubmed.ncbi.nlm.nih.gov/26862844/"
    source_license: "未確認"
    basis_tag: E
    corroboration: "Thieme誌ページ"
  uncertainty: "なし"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-071
  assertion:
    plain_statement_ja: "鋭的異物を内視鏡で摘出するときは、食道・胃・咽頭の損傷と誤嚥を防ぐため保護具（オーバーチューブやフード）を使う。"\[50\]
    condition: "鋭的異物の摘出"
    differential: "鈍的異物"
    common_misconception: "把持して引き抜くだけで安全なわけではない"
  provenance:
    source: "ESGE異物GL 2016（推奨11）"
    doi: "10.1055/s-0042-100456"
    pmid: "26862844"
    pmcid: null
    url: "https://pubmed.ncbi.nlm.nih.gov/26862844/"
    source_license: "未確認"
    basis_tag: E
    corroboration: null
  uncertainty: "なし"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-072
  assertion:
    plain_statement_ja: "食道の食物塊嵌頓は、内視鏡で胃内へ静かに押し込む方法が提案されている。食物塊嵌頓の背景には食道の基礎疾患（EoE、狭窄など）があることが多い。"\[50\]\[51\]
    condition: "食物塊嵌頓"
    differential: "EoE、ペプチック狭窄、食道癌"
    common_misconception: "摘出して終わりにせず、基礎疾患の検索（生検を含む）が必要"
  provenance:
    source: "ESGE異物GL 2016（推奨8）"
    doi: "10.1055/s-0042-100456"
    pmid: "26862844"
    pmcid: null
    url: "https://www.thieme-connect.com/products/ejournals/html/10.1055/s-0042-100456"
    source_license: "未確認"
    basis_tag: E
    corroboration: "同GL本文（基礎疾患の頻度は75%超）"\[51\]
  uncertainty: "75%超の数値は同GL本文の記載で、原著は未確認"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-073
  assertion:
    plain_statement_ja: "腐食性物質を飲み込んだときは、嘔吐を誘発しない。胃洗浄もしない（再曝露で食道傷害が増える）。弱酸・弱アルカリによる中和は発熱反応で傷害を悪化させるおそれがあり推奨されない。"\[52\]
    condition: "酸・アルカリの誤飲・自殺企図"
    differential: "非腐食性の中毒（活性炭の適応を検討）"
    common_misconception: "牛乳や活性炭は後の内視鏡の観察を妨げるため使わない"\[52\]
  provenance:
    source: "Contini S, Scarpignato C. Caustic injury of the upper GI tract: a comprehensive review. World J Gastroenterol 2013;19(25):3918"
    doi: null
    pmid: null
    pmcid: null
    url: "https://www.wjgnet.com/1007-9327/full/v19/i25/3918.htm"
    source_license: "CC BY-NC"
    basis_tag: B
    corroboration: null
  uncertainty: "DOIとPMIDは未照合"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-074
  assertion:
    plain_statement_ja: "腐食性食道傷害の重症度はZargar分類で評価する。0（正常）、1（浮腫・発赤）、2a（表在性潰瘍・びらん・滲出物）、2b（2aに加え深い限局性または全周性の潰瘍）、3a（限局性壊死）、3b（広範な壊死）に分ける。"\[52\]\[53\]\[54\]
    condition: "受傷後早期の上部内視鏡"
    differential: "CTによる重症度評価"
    common_misconception: "grade 4（穿孔）を加えた改変版もある"\[52\]
  provenance:
    source: "Cheng HT, et al. Caustic ingestion in adults. BMC Gastroenterol 2008（表1）"
    doi: null
    pmid: null
    pmcid: "PMC2533005"
    url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2533005/"
    source_license: "CC BY（BMC）"
    basis_tag: A
    corroboration: "Contini 2013 WJG（表3）"
  uncertainty: "Zargar原著（Gastrointest Endosc 1991）は未閲覧"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-075
  assertion:
    plain_statement_ja: "腐食性食道傷害後の狭窄は、Zargar 2bで約71%、3でほぼ100%と報告されている。重症度が高いほど狭窄のリスクが高い。"\[52\]\[54\]
    condition: "腐食性食道傷害の晩期合併症"
    differential: "腐食性傷害後の食道癌（長期の合併症）"\[55\]
    common_misconception: "急性期を乗り切っても狭窄の経過観察が必要"
  provenance:
    source: "Contini 2013 WJG"
    doi: null
    pmid: null
    pmcid: null
    url: "https://www.wjgnet.com/1007-9327/full/v19/i25/3918.htm"
    source_license: "CC BY-NC"
    basis_tag: B
    corroboration: "Chang CM ほか（PMC4137736）：2bと3で70〜100%"\[56\]
  uncertainty: "報告によって2bは40〜60%とする記載もあり、幅がある"\[57\]
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-079
  assertion:
    plain_statement_ja: "ヘルペス（HSV）食道炎では、ウイルス性の細胞変化（多核化、核の圧排、すりガラス状の核、Cowdry A型封入体）は潰瘍辺縁の扁平上皮に見られるため、辺縁から生検する。CMV食道炎の変化は潰瘍底の内皮細胞・間質細胞に見られるため、底部から生検する。"\[58\]\[59\]
    condition: "免疫不全者の食道潰瘍"
    differential: "カンジダ食道炎、薬剤性食道炎"
    common_misconception: "潰瘍の同じ部位を生検すれば両方が診断できるわけではない"
  provenance:
    source: "Esophageal CMV and HSV co-infection: case report and review. IDCases 2020"
    doi: null
    pmid: null
    pmcid: "PMC7519373"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC7519373"
    source_license: "未確認"
    basis_tag: E
    corroboration: "Medicine 2019（DOI 10.1097/MD.0000000000015845）"
  uncertainty: "なし（2資料で一致）"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-080
  assertion:
    plain_statement_ja: "内視鏡所見では、HSV食道炎は孤立性の潰瘍、小水疱、辺縁の隆起した（shouldered）潰瘍が多い。CMV食道炎は深い打ち抜き様の潰瘍、蛇行状の潰瘍、全周性の分布が多い。"\[60\]
    condition: "ウイルス性食道炎"
    differential: "カンジダ（白苔）"
    common_misconception: "肉眼所見だけで確定せず、病理・免疫染色で確認する"
  provenance:
    source: "Can endoscopists differentiate CMV esophagitis from HSV esophagitis? Medicine 2019"
    doi: "10.1097/MD.0000000000015845"
    pmid: null
    pmcid: null
    url: "https://doi.org/10.1097/MD.0000000000015845"
    source_license: "未確認"
    basis_tag: E
    corroboration: null
  uncertainty: "単一の後ろ向き研究"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-081
  assertion:
    plain_statement_ja: "HSV食道炎の治療薬はアシクロビル、CMV食道炎の治療薬はガンシクロビル（または経口のバルガンシクロビル）である。"\[58\]\[60\]\[61\]
    condition: "ウイルス性食道炎"
    differential: "アシクロビル耐性HSV（ホスカルネット）"\[62\]
    common_misconception: "アシクロビルはCMVに十分な効果がない"
  provenance:
    source: "Medicine 2019（確定診断後の治療薬）"
    doi: "10.1097/MD.0000000000015845"
    pmid: null
    pmcid: null
    url: "https://doi.org/10.1097/MD.0000000000015845"
    source_license: "未確認"
    basis_tag: E
    corroboration: "IDCases 2020（PMC7519373）"
  uncertainty: "投与期間は未確認"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-085
  assertion:
    plain_statement_ja: "Boerhaave症候群（特発性食道破裂）が疑われるとき、経口造影剤を併用した造影CTが優先される検査であり、感度は92〜100%と報告されている。CTでは縦隔気腫、縦隔の液体貯留、胸水、縦隔炎の評価もできる。"\[63\]\[64\]
    condition: "激しい嘔吐の後の胸痛・縦隔気腫"
    differential: "急性冠症候群、大動脈解離、特発性縦隔気腫"
    common_misconception: "胸部単純X線で異常がなくても否定できない"\[65\]
  provenance:
    source: "Boerhaave Syndrome—Narrative Review. Diagnostics 2025;15(19):2463"
    doi: null
    pmid: null
    pmcid: "PMC12524210"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12524210/"
    source_license: "CC BY 4.0（MDPI）"
    basis_tag: A
    corroboration: "J Med Case Rep 2026：CTで90%超に縦隔外の空気を検出"\[66\]
  uncertainty: "感度は総説が引用した値で、原著は未確認"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-086
  assertion:
    plain_statement_ja: "食道破裂を疑って食道造影を行う場合は、バリウムが縦隔に漏れると重い縦隔炎を起こすため、水溶性造影剤を使う。水溶性造影剤では22〜50%の穿孔を見逃すことがあるため、陰性でも否定はできない。"\[64\]\[67\]
    condition: "食道穿孔の疑い"
    differential: "誤嚥の危険がある例"
    common_misconception: "造影が陰性でも穿孔は否定できない"\[68\]
  provenance:
    source: "Diagnostics 2025;15(19):2463"
    doi: null
    pmid: null
    pmcid: "PMC12524210"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12524210/"
    source_license: "CC BY 4.0（MDPI）"
    basis_tag: A
    corroboration: "PMC13256309（修復後の水溶性造影で偽陰性になった症例）"\[68\]
  uncertainty: "なし"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: verified_sources}

- id: ES-087
  assertion:
    plain_statement_ja: "Boerhaave症候群の治療は、穿孔の早期の閉鎖・制御と感染（縦隔・胸腔）のドレナージが原則である。現在は、外科的修復に加え、ステントや内視鏡的陰圧閉鎖療法などの低侵襲治療を組み合わせる。"\[66\]\[69\]
    condition: "特発性食道破裂"
    differential: "医原性穿孔"
    common_misconception: "治療の遅れは死亡率を大きく高める"\[70\]
  provenance:
    source: "Diagnostics 2025;15(19):2463"
    doi: null
    pmid: null
    pmcid: "PMC12524210"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12524210/"
    source_license: "CC BY 4.0（MDPI）"
    basis_tag: A
    corroboration: null
  uncertainty: "治療の選択基準と死亡率の数値は未確認"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}

- id: ES-089
  assertion:
    plain_statement_ja: "ヨード（ルゴール）染色では、グリコーゲンを含む正常な扁平上皮が褐色に染まり、扁平上皮癌や異形成は不染帯となる。多発する不染帯（まだら食道）は食道癌の高リスクの指標となる。"
    condition: "食道扁平上皮癌のスクリーニング・範囲診断"
    differential: "NBI拡大観察（JES分類）"
    common_misconception: "不染帯がすべて癌というわけではない"
  provenance:
    source: "要確認（JGES食道ESD/EMR GL 2020＝B、本文の該当CQを未照合）"
    doi: "10.1111/den.13654"
    pmid: null
    pmcid: null
    url: null
    source_license: "Wiley規約（非CC）"
    basis_tag: B
    corroboration: null
  uncertainty: "該当箇所の照合が未了"
  curriculum: {core_curriculum: "要確認", kokushi: "要確認"}
  publication_info: {created: 2026-10-10, verifier: "", status: draft}
```

## 4. カリキュラム対応表（確定版）

| 領域 | 該当カード | コアカリ（令和4年度改訂版） | 国試出題基準（令和6年版） |
|---|---|---|---|
| GERD・検査（pH・インピーダンス、HRM） | ES-R12〜R14、R19 | 要確認 | 要確認 |
| 食道運動障害（アカラシア） | ES-R06、R13、R14 | 要確認 | 要確認 |
| 食道癌（疫学・危険因子・治療） | ES-R01〜R05、R15、R16、ES-089 | 要確認 | 要確認 |
| 食道・胃静脈瘤 | ES-R10、R11、R17、R18 | 要確認 | 要確認 |
| EoE | ES-R07〜R09 | 要確認 | 要確認 |
| 異物・腐食・破裂 | ES-069〜075、085〜087 | 要確認 | 要確認 |
| 感染性食道炎 | ES-079〜081 | 要確認 | 要確認 |

番号を特定するには、core-curriculum/data のCSVと、厚労省が公表している国試出題基準のPDFを直接照合する必要があります。今回はどちらも取得できなかったため、推測で番号を割り当てることはしていません。

## 5. 第2回（胃・十二指腸）への引き継ぎ事項
1. **PMIDの照合手順を変える**：この環境ではPubMedとPMCが自動アクセスを拒否します。次の経路を使ってください。
   - Crossref API（DOIからライセンスと書誌を取得）
   - ClinicalTrials.govの文献表
   - PubMedの論評レコードの「Comment on」欄

   照合できないものは、最初から pmid: null とします。
2. **食道の残課題**：
   - CheckMate 577とCheckMate 648のPMID
   - García-Pagán 2010のPMIDの独立照合
   - JSGE GERD GL 2021本文（用量、PPIテスト、CQ、RE有病率）
   - ACG 2020アカラシアGL
   - Chicago v4.0の正常値データベースの人数
   - 欠番7件の出典取得と起票
   - ES-089の照合
   - コアカリと国試の番号
3. **胃・十二指腸と重なる事項**：
   - KEYNOTE-590とCheckMate 577は食道胃接合部腺癌を含むため、第2回で再利用します（SRC-02、04、05）。
   - ARMSのK653-6は、点数表上「胃、十二指腸」の款に置かれています。
   - 静脈瘤の記載基準（胃静脈瘤のLg分類）と肝硬変GL 2020のB-RTOは、第2回の胃静脈瘤カードに移します。
4. **ライセンスの扱い**：
   - Elsevier誌のOA論文でも、CrossrefにCCの表示がなければBとして扱います。
   - ESMO OpenはCC BY-NC-NDなのでBです。
   - PLoS、BMC、MDPIはCC BYなのでAとし、優先的に使います。
5. **国内承認の監視**：第2回の開始時に、次の2点を再確認します。
   - デュピルマブのEoEへの国内申請・承認の有無
   - 2026年度診療報酬改定でK653-6が変更されたかどうか

## Caveats
- CheckMate 577の5年OS（46%対41%）は、まだニュースサイトでしか照合できていません。方針に従い、要確認と明記しています。
- 「国内で承認されていない」という主張は、承認の記録が見つからなかったことに基づく推定です。確定させるには、添付文書の効能欄を全文照合する必要があります。
- 前回版のID対応表がないため、ES-R番号を前回のIDに割り当てる作業は、統合時に手作業で行う必要があります。

## 出典

1. [Neoadjuvant therapy for oesophageal cancer: refining the armamentarium - PubMed](https://pubmed.ncbi.nlm.nih.gov/38876135/)
2. [Prognostic Impact of Thoracic Duct Resection in Patients Who Underwent Transthoracic Esophagectomy Following Neoadjuvant Therapy for Esophageal Squamous Cell Carcinoma: Exploratory Analysis of JCOG1109](https://link.springer.com/article/10.1245/s10434-024-16303-8)
3. <https://api.crossref.org/works/10.1111/den.13654>
4. [Topical Application of Sucralfate in Promoting Healing of Esophageal Ulcers After Esophageal Varices Ligation](https://clinicaltrials.gov/study/NCT07679191)
5. [Gastroesophageal Reflux Disease and Reflux-like Phenotypes: Using Lyon Consensus 2.0 to Guide Clinical Approach - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13425011/)
6. [Can the Mean Nocturnal Baseline Impedance/Acid Exposure Time Ratio Serve as a Novel Parameter for the Definitive Diagnosis of Pathological Reflux?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12470591/)
7. [Updated Lyon Consensus and other updates - Medizinonline](https://medizinonline.com/en/updated-lyon-consensus-and-other-updates/)
8. [好酸球性消化管疾患（EGID）～アレルギーセンターの取り組み～](https://kompas.hosp.keio.ac.jp/presentation/202405/)
9. [今月のテーマ （総 説） 門脈圧亢進症 up to date 門脈圧亢進症に対する内視鏡的治療 日 高 央 魚 嶋 晴 紀 １） 國 分 茂 博 ２）](https://www.jstage.jst.go.jp/article/nisshoshi/116/5/116_395/_pdf)
10. [コラム11-3-11 食道・胃静脈瘤内視鏡所見記載の意義](https://www.asakura.co.jp/lp/naikagaku12ed/digitalappendix/src/e%E3%82%B3%E3%83%A9%E3%83%A011-3-11_%E9%A3%9F%E9%81%93%E3%83%BB%E8%83%83%E9%9D%99%E8%84%88%E7%98%A4%E5%86%85%E8%A6%96%E9%8F%A1%E6%89%80%E8%A6%8B%E8%A8%98%E8%BC%89%E3%81%AE%E6%84%8F%E7%BE%A9.html)
11. [Evidence-based clinical practice guidelines for Liver Cirrhosis 2020](https://link.springer.com/article/10.1007/s00535-021-01788-x)
12. [Evidence-based clinical practice guidelines for Liver Cirrhosis 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8280040/)
13. [食道：\[国立がん研究センター がん統計\] - がん情報サービス](https://ganjoho.jp/reg_stat/statistics/stat/cancer/4_esophagus.html)
14. [Esophageal Cancer Neoadjuvant Triplet or Doublet Chemotherapy With or Without Radiotherapy - The ASCO Post](https://ascopost.com/news/june-2024/esophageal-cancer-neoadjuvant-triplet-or-doublet-chemotherapy-with-or-without-radiotherapy/)
15. [Neoadjuvant and Adjuvant Therapy](https://link.springer.com/chapter/10.1007/978-981-92-2611-5_15)
16. [Adjuvant nivolumab after chemoradiotherapy and resection for patients with esophageal cancer: A real‐world matched comparison of overall survival](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12765972/)
17. [CheckMate 577 Final Results: Adjuvant Nivolumab Sustains Disease-Free Survival Benefit in Resected Esophageal and Gastroesophageal Junction Cancer - OncoDaily](https://oncodaily.com/oncolibrary/checkmate-577)
18. [Pembrolizumab plus chemotherapy versus chemotherapy for advanced esophageal cancer: 5-year extended follow-up for the randomized phase III KEYNOTE-590 study - ESMO Open](<https://www.esmoopen.com/article/S2059-7029(25)01723-5/fulltext>)
19. [2021 年11 月26 日 医療関係者各位 食道癌適正使用委員会 小野薬品工業株式会社／ブリストル・マイヤーズ スクイブ株式会社](https://www.esophagus.jp/files/opdivo_20211201.pdf)
20. [2021 年11 月25 日 各位 小野薬品工業株式会社 ブリストル･マイヤーズ スクイブ株式会社](https://www.bms.com/assets/bms/japan/pressrelease/20211125.pdf)
21. [オプジーボ、「根治切除不能な進行・再発の食道がん」と「治癒切除不能な進行・再発のMSI-Highを有する結腸・直腸がん」へ適応追加](https://oncolo.jp/news/20200225kn_2)
22. [デュピルマブ、12歳以上の好酸球性食道炎にも有効／NEJM｜医師向け医療ニュースはケアネット](https://www.carenet.com/news/journal/carenet/55710)
23. [COPD初の生物学的製剤デュピルマブへの期待／サノフィ｜医師向け医療ニュースはケアネット](https://www.carenet.com/news/general/carenet/60853)
24. [Editorial: Do We Need to Adapt GERD Metrics Based on the Population Being Evaluated? - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13419277/)
25. [Updates to the Modern Diagnosis of GERD: Lyon Consensus 2.0 By Jason Nasser, MD](https://med.emory.edu/departments/medicine/_documents/nasser.gerd.lyon.pdf)
26. [ESOPHAGEAL MOTILITY DISORDERS ON HIGH RESOLUTION MANOMETRY: CHICAGO CLASSIFICATION VERSION 4.0© - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8034247/)
27. [Understanding the Chicago Classification: From Tracings to Patients](https://www.jnmjournal.org/journal/view.html?doi=10.5056%2Fjnm17026)
28. [The Chicago Classification of esophageal motility A comparison of v3.0 and v4.0](https://www.medtronic.com/content/dam/medtronic-wide/public/western-europe/products/digestive-gastrointestinal/motility-testing/chicago-classification-comparison-brochure-en-gb.pdf)
29. [Achalasia subtypes are front and center of the Chicago classification—strategies to overcome limitations in clinical application - Myers - Annals of Esophagus](https://aoe.amegroups.org/article/view/5407/html)
30. [Evaluation of Esophageal Motility and Lessons from Chicago](https://escholarship.org/content/qt4899k46f/qt4899k46f_noSplash_16c46b85ced9ac20644e97b5c0522b43.pdf?t=s2m3kl)
31. [UC San Diego UC San Diego Previously Published Works Title](https://escholarship.org/content/qt4899k46f/qt4899k46f.pdf)
32. [The Alcohol Flushing Response: An Unrecognized Risk Factor for Esophageal Cancer from Alcohol Consumption](https://journals.plos.org/plosmedicine/article?id=10.1371%2Fjournal.pmed.1000050)
33. [Alcohol, ALDH2, and Esophageal Cancer: A Meta-analysis Which Illustrates the Potentials and Limitations of a Mendelian Randomization Approach](https://aacrjournals.org/cebp/article/14/8/1967/258224/Alcohol-ALDH2-and-Esophageal-Cancer-A-Meta)
34. [The Alcohol Flushing Response: An Unrecognized Risk ...](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pmed.1000050&type=printable)
35. [Alcohol, ALDH2, and esophageal cancer: a meta-analysis which illustrates the potentials and limitations of a Mendelian randomization approach - PubMed](https://pubmed.ncbi.nlm.nih.gov/16103445/)
36. [胃：\[国立がん研究センター がん統計\] - がん情報サービス](https://ganjoho.jp/reg_stat/statistics/stat/cancer/5_stomach.html)
37. [2025年のがん統計予測：\[国立がん研究センター がん統計\]](https://ganjoho.jp/reg_stat/statistics/stat/short_pred.html)
38. [がんの部位別統計](https://www.jcancer.jp/information/statistics/)
39. [1187 日本内科学会雑誌 第103巻 第5 号・平成26年5 月10日 食道・胃静脈瘤治療への内科的アプローチ 林 量司 1） 國分 茂博 2） 浅野 朗](https://www.jstage.jst.go.jp/article/naika/103/5/103_1187/_pdf)
40. [Evidence‐based clinical practice guidelines for liver cirrhosis 2020 - Yoshiji - 2021 - Hepatology Research - Wiley Online Library](https://onlinelibrary.wiley.com/doi/full/10.1111/hepr.13678)
41. [(PDF) Evidence-based clinical practice guidelines for Liver Cirrhosis 2020](https://www.researchgate.net/publication/353049755_Evidence-based_clinical_practice_guidelines_for_Liver_Cirrhosis_2020)
42. [3．先進内視鏡治療に潜むリスクとそのマネジメント（2）内視鏡的逆流防止粘膜切除術 (臨牀消化器内科 38巻1号)](https://webview.isho.jp/journal/detail/abs/10.19020/CG.0000002485)
43. [胃食道逆流症に対する内視鏡診断と治療の現状と課題](https://www.jstage.jst.go.jp/article/gee/65/6/65_1085/_html/-char/ja)
44. [Ｋ６５３－６ 内視鏡的逆流防止粘膜切除術](https://www.mfeesw.com/?page_id=2200057)
45. [GERDの内視鏡治療―ARMS/ARMA― (消化器内視鏡 35巻5号)](https://webview.isho.jp/journal/detail/abs/10.24479/endo.0000000741)
46. [■第2 回 GERD に対する 内視鏡治療研究会 附 置 研 究 会 1](https://www.jges.net/wp-content/uploads/2024/05/66_1105.pdf)
47. [1 Japanese Health Insurance Federation for Surgery (JHIFS) Extra](https://www.gaihoren.jp/gaihoren/public/doc/news_extra220331.pdf?v=20220404)
48. [Removal of foreign bodies in the upper gastrointestinal tract in ...](https://www.thieme-connect.com/products/ejournals/html/10.1055/s-0042-100456)
49. [Google Scholar](https://scholar.google.com/scholar_lookup?doi=10.1055%2Fs-0042-100456&amp=&pmid=26862844)
50. [Removal of foreign bodies in the upper gastrointestinal tract in adults: European Society of Gastrointestinal Endoscopy (ESGE) Clinical Guideline - PubMed](https://pubmed.ncbi.nlm.nih.gov/26862844/)
51. [Removal of foreign bodies in the upper gastrointestinal ...](https://www.esge.com/assets/downloads/pdfs/guidelines/2016_s_0042_100456.pdf)
52. [Caustic injury of the upper gastrointestinal tract: A comprehensive review](https://www.wjgnet.com/1007-9327/full/v19/i25/3918.htm)
53. [Caustic ingestion in adults: The role of endoscopic classification in predicting outcome](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2533005/)
54. [Zargar Classification of Caustic Esophageal Injury](https://www.otoscape.com/eponyms/zargar-classification-of-caustic-esophageal-injury.html)
55. [Caustic ingestion](https://en.wikipedia.org/wiki/Caustic_ingestion)
56. [Predicting the Progress of Caustic Injury to Complicated Gastric Outlet Obstruction and Esophageal Stricture, Using Modified Endoscopic Mucosal Injury Grading Scale](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4137736/)
57. [Endoscopic classification of corrosive injuries according to Zargar et...](https://www.researchgate.net/figure/Endoscopic-classification-of-corrosive-injuries-according-to-Zargar-et-al-8_tbl1_51587376)
58. [HSV Esophagitis](https://www.patientcareonline.com/view/hsv-esophagitis)
59. [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7519373)
60. [Can endoscopists differentiate cytomegalovirus esophagitis from herpes simplex virus esophagitis based on gross endoscopic findings?](https://doi.org/10.1097/MD.0000000000015845)
61. [Esophageal Cytomegalovirus and Herpes Simplex virus co-infection in an immunocompromised patient: Case report and review of literature - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S221425092030233X)
62. [Pathology Outlines - HSV esophagitis](https://www.pathologyoutlines.com/topic/esophagusHSV.html)
63. [Boerhaave Syndrome—Narrative Review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12524210/?utm=)
64. [Boerhaave Syndrome—Narrative Review](https://www.mdpi.com/2075-4418/15/19/2463)
65. [Boerhaave's syndrome](https://www.appliedradiology.com/Articles/boerhaave39s-syndrome)
66. [Successful multistage surgical management of Boerhaave syndrome: a case report and review of the literature](https://link.springer.com/article/10.1186/s13256-026-06078-9)
67. [Boerhaave Syndrome (Spontaneous Esophageal Perforation) Workup: Approach Considerations, Laboratory Studies, Imaging Studies](https://emedicine.medscape.com/article/171683-workup)
68. [Negative Contrast Esophagography Does Not Exclude Dehiscence After Boerhaave Repair: Complementary Low-Insufflation Carbon Dioxide Endoscopy - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13256309/)
69. [Boerhaave Syndrome: An Updated Review with an Emphasison Endoscopic Treatments - Practical Gastro](https://practicalgastro.com/2026/04/01/boerhaave-syndrome-an-updated-review-with-an-emphasison-endoscopic-treatments/)
70. [A Case of a Successfully Treated Patient With a Delayed Diagnosis of Boerhaave’s Syndrome and Severe Complications - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11658894/)
