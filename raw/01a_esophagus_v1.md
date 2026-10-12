# 消化器領域 事実票 第1回：食道（ES-001〜ES-068）

第1回（食道）として68件の事実票を作りました。約3分の2は出典とライセンスを確認できた資料に基づきます（CC BY 4.0のガイドライン、または非CC原著から事実だけを抜き出したもの）。残る約3分の1（その他の食道疾患、日本独自の記載基準）はまだ出典が取れていないため、status: draftのまま補完が必要です。

**作業上の注意（2点）**
- **enrich工程は未完了です。** 原稿が文字数の上限（50,000字）を超えたため、enrich_draft（あいまいな記述を出典付きの具体値に置き換える工程）が実行できませんでした。この納品物には未実施です。
- **出典確認は途中までです。** Crossref・NCBIのレート制限で、多くのRCTのPMIDとライセンスを照合しきれていません。PMIDに「（…の可能性）」と付けたものは記憶由来の候補なので、照合が終わるまで使わないでください。

## TL;DR
- **タグA（CC BY 4.0、ライセンス確認済み）で中核に使える資料は3つです。**
  - JSGE GERD診療ガイドライン2021英語版（Crossrefで確認）
  - 日本食道学会 食道癌診療ガイドライン2022 Part 1（PMCで確認）
  - 食道癌取扱い規約 英語版11版・12版（Crossrefで確認）

  Baveno VII、AASLD 2024、Chicago分類v4.0、NEJM/LancetのRCT群は、Crossrefに出版社の標準条件しかないか、license欄が空でした。これらはタグB（数値と推奨の方向性だけを自作文で記述）で扱います。
- **日本と欧米で推奨が分かれる主な点は4つで、conditionフィールドで区別しています。**
  1. 重症逆流性食道炎の治療：日本はボノプラザンを提案。
  2. Barrett食道の定義：日本は柵状血管で接合部を決め、腸上皮化生（IM）を必須としない。米国はIM必須。
  3. 局所進行食道扁平上皮癌の術前治療：日本はJCOG1109に基づくDCF。欧米は術前CRTの後、残存病変があれば術後ニボルマブ。
  4. 静脈瘤の内視鏡治療：日本はEISも使う。欧米はEVLが標準。
- **未解決事項は3群に分けて引き継ぎます。**
  - (a) RCTのPMIDと一部ライセンスの照合
  - (b) 「その他の食道疾患」の一次出典の取得
  - (c) コアカリ・国試出題基準の番号照合

---

## 1. 第1回 抽出元ホワイトリスト

**basis_tagの定義**
- A：CC BY / CC0
- B：非CC・NC・ND。数値と方向性だけを自作文で記述し、原文の文言・表・図は使わない
- C：政府標準利用規約・公共データ利用規約
- D：米国政府著作物
- E：ライセンス未確認（当面はB扱い）
- F・G：本回は未使用

この定義が前回と一致しているかは要確認です。

| # | 抽出元 | DOI / PMID / PMCID | ライセンス確認結果 | タグ |
|---|---|---|---|---|
| W01 | JSGE GERD GL 2021（Iwakiri, J Gastroenterol 2022;57:267-85） | 10.1007/s00535-022-01861-z / 要確認 / PMC8938399 | **CC BY 4.0**（Crossrefのlicense、vor・tdmとも）。\[1\]PMC本文はreCAPTCHAで取得できず\[2\] | A |
| W02 | 日本食道学会 食道癌GL 2022 Part 1（Kitagawa, Esophagus 2023;20:343-72） | 10.1007/s10388-023-00993-2 / 36933136 / PMC10024303 | **CC BY 4.0**（PMC記事ページに明記）\[3\] | A |
| W03 | 同 Part 2 | 要確認 / PMC10235142 | 未確認 | E |
| W04 | 食道癌取扱い規約 英語版11版 Part I | 10.1007/s10388-016-0551-7 / 28111535 / PMC5222932 | **CC BY 4.0**（Crossref）\[4\]\[5\]\[6\] | A |
| W05 | 同 12版 Part I（Esophagus 2024;21:179-215） | 10.1007/s10388-024-01054-y / 38568243 / PMC11199297 | **CC BY 4.0**（Crossref） | A |
| W06 | 日本食道学会 拡大内視鏡分類（Oyama, Esophagus 2017;14:105-12） | **10.1007/s10388-016-0527-7**（依頼文の候補DOIは誤り）/ 28386209 / PMC5362661\[7\] | 未確認（PMC上はSpringerOpenの体裁） | E |
| W07 | Chicago Classification v4.0（Neurogastroenterol Motil 2021;33:e14058） | 10.1111/nmo.14058 / 33373111 / PMC8034247 | **非CC**（Wiley標準条件。PMC版はNIH著者稿）\[5\]\[8\] | B |
| W08 | Baveno VII（J Hepatol 2022;76:959-74） | 10.1016/j.jhep.2021.12.022 / 35120736 | Crossrefに出るのは**Elsevier TDM規約のみ**。\[9\]CC BY-NC-NDかどうかは未確認。正誤表あり（10.1016/j.jhep.2022.03.024）\[10\] | B |
| W09 | AASLD 門脈圧亢進症ガイダンス2024（Hepatology 79:1180-211） | 10.1097/HEP.0000000000000647 / 37870298 | Crossrefのlicense欄なし。LWWで「Free」表示（無料閲覧であってCCではない）\[11\]\[12\] | B |
| W10 | ESGE 食道胃静脈瘤GL 2022 | 要確認 | 未確認 | E |
| W11 | ACG Barrett GL 2022（Am J Gastroenterol 117:559-87） | 10.14309/ajg.0000000000001680 / 要確認 | license欄なし（非CC）\[13\] | B |
| W12 | AGREE EoE国際診断基準（Gastroenterology 2018） | 要確認 | 未確認 | E |
| W13 | ACG EoE GL 2025 | 10.14309/ajg.0000000000003194 | 未確認 | E |
| W14 | 日本人EoE 症例対照研究 | PMID 32411581 | 未確認 | E |
| W15 | JGES 食道ESD/EMR GL（Dig Endosc 2020;32:452-93） | 10.1111/den.13654 | **非CC**（Wiley、Crossref）\[14\] | B |
| W16 | JCOG1109 NExT（Kato, Lancet 2024;404:55-66） | 10.1016/S0140-6736(24)00745-1 / 要確認 | 未確認（非CCと推定） | B |
| W17 | CheckMate 577（Kelly, NEJM 2021;384:1191-203） | 10.1056/NEJMoa2032125 / 要確認 | **非CC**（NEJM利用規約、Crossref）\[15\] | B |
| W18 | CheckMate 648（Doki, NEJM 2022;386:449-62） | 10.1056/NEJMoa2111380 / 要確認 | 未確認（非CCと推定） | B |
| W19 | KEYNOTE-590（Sun, Lancet 2021;398:759-71） | 10.1016/S0140-6736(21)01234-4 / 要確認 | 未確認（非CCと推定） | B |
| W20 | POEM vs LHM RCT（Werner, NEJM 2019;381:2219-29） | 10.1056/NEJMoa1905380 / 要確認 | 未確認（非CCと推定） | B |
| W21 | デュピルマブ EoE 第3相（Dellon, NEJM 2022;387:2317-30） | 10.1056/NEJMoa2205982 / 要確認 | 未確認（非CCと推定） | B |
| W22 | 制限輸血RCT（Villanueva, NEJM 2013;368:11-21） | 10.1056/NEJMoa1211801 / 要確認 | 未確認（非CCと推定） | B |
| W23 | 早期TIPS RCT（García-Pagán, NEJM 2010;362:2370-9） | 10.1056/NEJMoa0910102 / 20573925\[16\]\[17\] | 未確認（非CCと推定） | B |
| W24 | 国立がん研究センター がん統計 | ganjoho.jp | 利用規約は要確認 | C候補 |
| W25 | 日本門脈圧亢進症学会 内視鏡所見記載基準 | 未取得 | ©学会（非CC）。項目名のみ使用 | B |

**抽出元にしなかったもの：** UpToDate、ResearchGateの転載PDF、学会や病院が再配布しているPDF、ニュースサイト（ASCO Post、OncLive等）。ニュースサイトの数値は、RCT本文と照合するための手がかりとしてだけ使いました。

---

## 2. 事実票YAML

```yaml
# 共通定義（YAML 1.1のmerge key `<<:` を使用。パーサーが対応していなければ展開すること）
_pub: &PUB {created: 2026-10-10, verifier: "", status: draft}
_cur:
  GERD: &C_GERD {core_curriculum: "PS-02-08-xx（要確認）", kokushi: "胃食道逆流症・逆流性食道炎（番号要確認）"}
  BE: &C_BE {core_curriculum: "要確認", kokushi: "Barrett食道"}
  EOE: &C_EOE {core_curriculum: "要確認", kokushi: "好酸球性食道炎"}
  MOT: &C_MOT {core_curriculum: "要確認", kokushi: "食道アカラシア・食道運動障害"}
  CA: &C_CA {core_curriculum: "要確認", kokushi: "食道癌"}
  VX: &C_VX {core_curriculum: "要確認", kokushi: "食道・胃静脈瘤、門脈圧亢進症"}
  OTH: &C_OTH {core_curriculum: "要確認", kokushi: "Mallory-Weiss症候群・特発性食道破裂・食道異物ほか"}
_src:
  W01: &W01 {source: "Iwakiri K, et al. JSGE GERD guidelines 2021. J Gastroenterol 2022;57:267-285", doi: "10.1007/s00535-022-01861-z", pmid: "要確認", pmcid: "PMC8938399", url: "https://link.springer.com/article/10.1007/s00535-022-01861-z", source_license: "CC BY 4.0（Crossref確認済）", basis_tag: A}
  W02: &W02 {source: "Kitagawa Y, et al. JES Esophageal cancer practice guidelines 2022 part 1. Esophagus 2023;20:343-372", doi: "10.1007/s10388-023-00993-2", pmid: "36933136", pmcid: "PMC10024303", url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC10024303/", source_license: "CC BY 4.0（PMC表示確認済）", basis_tag: A}
  W05: &W05 {source: "Japanese Classification of Esophageal Cancer 12th ed. Part I. Esophagus 2024;21:179-215", doi: "10.1007/s10388-024-01054-y", pmid: "38568243", pmcid: "PMC11199297", url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC11199297/", source_license: "CC BY 4.0（Crossref）", basis_tag: A}
  W07: &W07 {source: "Yadlapati R, et al. Chicago Classification v4.0. Neurogastroenterol Motil 2021;33:e14058", doi: "10.1111/nmo.14058", pmid: "33373111", pmcid: "PMC8034247", url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC8034247/", source_license: "非CC（Wiley; Crossref）", basis_tag: B}
  W08: &W08 {source: "de Franchis R, et al. Baveno VII. J Hepatol 2022;76:959-974", doi: "10.1016/j.jhep.2021.12.022", pmid: "35120736", pmcid: "要確認", url: "", source_license: "未確認（CrossrefはElsevier TDM規約のみ）", basis_tag: B}
  W09: &W09 {source: "Kaplan DE, et al. AASLD Practice Guidance, portal hypertension and varices. Hepatology 2024;79:1180-1211", doi: "10.1097/HEP.0000000000000647", pmid: "37870298", pmcid: "", url: "", source_license: "非CC（license欄なし）", basis_tag: B}
  W11: &W11 {source: "Shaheen NJ, et al. ACG Barrett's Esophagus guideline. Am J Gastroenterol 2022;117:559-587", doi: "10.14309/ajg.0000000000001680", pmid: "要確認", pmcid: "", url: "", source_license: "非CC（license欄なし）", basis_tag: B}
  W12: &W12 {source: "Dellon ES, et al. AGREE conference. Gastroenterology 2018", doi: "要確認", pmid: "要確認", pmcid: "", url: "", source_license: "未確認", basis_tag: E}
  W13: &W13 {source: "ACG Clinical Guideline: EoE. Am J Gastroenterol 2025", doi: "10.14309/ajg.0000000000003194", pmid: "要確認", pmcid: "", url: "", source_license: "未確認", basis_tag: E}
  W14: &W14 {source: "Clinical and endoscopic characteristics of EoE in Japan: a case-control study", doi: "要確認", pmid: "32411581", pmcid: "要確認", url: "", source_license: "未確認", basis_tag: E}
  W15: &W15 {source: "Ishihara R, et al. JGES ESD/EMR guidelines for esophageal cancer. Dig Endosc 2020;32:452-493", doi: "10.1111/den.13654", pmid: "要確認（32072683の可能性）", pmcid: "", url: "", source_license: "非CC（Wiley; Crossref）", basis_tag: B}
  W16: &W16 {source: "Kato K, et al. JCOG1109 NExT. Lancet 2024;404:55-66", doi: "10.1016/S0140-6736(24)00745-1", pmid: "要確認（38876133の可能性）", pmcid: "", url: "", source_license: "未確認（非CC推定）", basis_tag: B}
  W17: &W17 {source: "Kelly RJ, et al. CheckMate 577. N Engl J Med 2021;384:1191-1203", doi: "10.1056/NEJMoa2032125", pmid: "要確認（33789008の可能性）", pmcid: "", url: "", source_license: "非CC（NEJM規約; Crossref）", basis_tag: B}
  W18: &W18 {source: "Doki Y, et al. CheckMate 648. N Engl J Med 2022;386:449-462", doi: "10.1056/NEJMoa2111380", pmid: "要確認（35108470の可能性）", pmcid: "", url: "", source_license: "未確認（非CC推定）", basis_tag: B}
  W19: &W19 {source: "Sun JM, et al. KEYNOTE-590. Lancet 2021;398:759-771", doi: "10.1016/S0140-6736(21)01234-4", pmid: "要確認（34454674の可能性）", pmcid: "", url: "", source_license: "未確認（非CC推定）", basis_tag: B}
  W20: &W20 {source: "Werner YB, et al. POEM vs LHM. N Engl J Med 2019;381:2219-2229", doi: "10.1056/NEJMoa1905380", pmid: "要確認（31800987の可能性）", pmcid: "", url: "", source_license: "未確認（非CC推定）", basis_tag: B}
  W21: &W21 {source: "Dellon ES, et al. Dupilumab in EoE. N Engl J Med 2022;387:2317-2330", doi: "10.1056/NEJMoa2205982", pmid: "要確認（36546624の可能性）", pmcid: "", url: "", source_license: "未確認（非CC推定）", basis_tag: B}
  W22: &W22 {source: "Villanueva C, et al. N Engl J Med 2013;368:11-21", doi: "10.1056/NEJMoa1211801", pmid: "要確認（23281973の可能性）", pmcid: "", url: "", source_license: "未確認（非CC推定）", basis_tag: B}
  W23: &W23 {source: "García-Pagán JC, et al. N Engl J Med 2010;362:2370-2379", doi: "10.1056/NEJMoa0910102", pmid: "20573925", pmcid: "", url: "https://pubmed.ncbi.nlm.nih.gov/20573925/", source_license: "未確認（非CC推定）", basis_tag: B}
  PEND: &PEND {source: "一次出典未取得（要補完）", doi: "", pmid: "", pmcid: "", url: "", source_license: "未確認", basis_tag: "保留"}

# ===== 1. GERD・NERD・Barrett食道 =====
- id: ES-001
  assertion: {plain_statement_ja: "日本消化器病学会のGERD診療ガイドライン第3版（日本語版）は2021年4月に刊行され、GERDを逆流性食道炎（RE）と非びらん性逆流症（NERD）に分けた治療アルゴリズムを導入した。",\[1\] condition: {region: 日本, guideline: JSGE GERD 2021}, differential: "第2版（2015）ではP-CABの位置づけがなかった", common_misconception: "GERD＝内視鏡でびらんがある病態、と考える（NERDも含む）"}
  provenance: {<<: *W01, corroboration: "抄録"}
  uncertainty: low
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-002
  assertion: {plain_statement_ja: "日本では、P-CABのボノプラザンが2015年2月に初めて逆流性食道炎の治療薬として使えるようになった。",\[2\] condition: {region: 日本}, differential: "PPIは酸で活性化されてから不可逆的に阻害する。P-CABはK+と競合して可逆的に阻害する", common_misconception: "ボノプラザンをPPIの一種とする"}
  provenance: {<<: *W01, corroboration: "序論"}
  uncertainty: low
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-003
  assertion: {plain_statement_ja: "日本のGERDガイドライン2021は、重症逆流性食道炎（LA分類C・D）の初期治療と維持治療にボノプラザンを提案している。",\[18\]\[19\] condition: {region: 日本, population: "LA C/D"}, differential: "欧米の多くは初期治療の第一選択をPPIとしている（要確認）", common_misconception: "重症でも維持療法は不要と考える"}
  provenance: {<<: *W01, corroboration: "抄録。初期治療はボノプラザン20 mgを4週（用量は本文で要確認）"}
  uncertainty: "low（推奨の方向）／medium（用量）"
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-004
  assertion: {plain_statement_ja: "軽症逆流性食道炎（LA分類A・B）では、初期治療にボノプラザンまたはPPIを推奨している。維持治療はPPIを推奨し、ボノプラザンを提案としている。",\[19\]\[20\] condition: {region: 日本, population: "LA A/B"}, differential: "「推奨」と「提案」では推奨の強さが異なる", common_misconception: "軽症でもボノプラザンによる維持が第一推奨と考える"}
  provenance: {<<: *W01, corroboration: "抄録"}
  uncertainty: low
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-005
  assertion: {plain_statement_ja: "ロサンゼルス（LA）分類は、粘膜傷害の長さと広がりで重症度を分ける。粘膜ひだの間で連続しない5 mm以下の傷害をA、5 mm超をB、2条以上のひだにまたがり全周の75%未満のものをC、75%以上をDとする。", condition: {region: 国際}, differential: "日本で使われる改訂LA分類（星原）には、grade NとMがある", common_misconception: "CとDの境界を50%とする"}
  provenance: {source: "Lundell LR, et al. Gut 1999", doi: "要確認", pmid: "要確認", pmcid: "", url: "", source_license: "未確認（BMJ、非CC推定）", basis_tag: B, corroboration: "W01でもC・Dを重症としている"}
  uncertainty: medium
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-006
  assertion: {plain_statement_ja: "日本では、重症逆流性食道炎の基準としてLA分類のC・Dを用いる。",\[20\] condition: {region: 日本}, differential: "改訂LA分類のgrade Mは色調変化のみ", common_misconception: "grade Bを重症に含める"}
  provenance: {<<: *W01, corroboration: "Expert Opin Drug Saf 2026"}
  uncertainty: low
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-007
  assertion: {plain_statement_ja: "日本の成人における逆流性食道炎の有病率は約10%と推定されている（引用元の原典と数値は要確認）。",\[20\] condition: {region: 日本, population: 成人}, differential: "GERD症状の有病率と、内視鏡で見るREの有病率は別の指標", common_misconception: "H. pylori感染率の低下とは無関係と考える"}
  provenance: {<<: *W01, corroboration: "二次資料（Manabe 2026）がW01を引用している"}
  uncertainty: high
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-008
  assertion: {plain_statement_ja: "24時間pH・インピーダンス検査は酸逆流と非酸逆流の両方を検出できる。内視鏡で所見のないNERDやPPI抵抗性の症例で、逆流と症状の関連を評価する手段になる。", condition: {region: 国際}, differential: "機能性胸やけ、逆流過敏性食道", common_misconception: "pH検査だけで非酸逆流も評価できると考える"}
  provenance: {<<: *PEND, corroboration: "W01の該当章で要確認"}
  uncertainty: medium
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-009
  assertion: {plain_statement_ja: "Lyon consensusでは、酸曝露時間（AET）6%超を病的逆流の確定的な所見、4%未満を正常範囲とする（Lyon 2.0での数値とライセンスは要確認）。", condition: {region: 国際}, differential: "4〜6%は判定保留域", common_misconception: "AET 4%を病的閾値とする"}
  provenance: {<<: *PEND, corroboration: "一次資料で要確認"}
  uncertainty: high
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-010
  assertion: {plain_statement_ja: "PPIテスト（PPIを試しに投与し、症状が改善するかで診断する方法）は簡便だが、感度・特異度が限られる。陰性でもGERDを否定できない。", condition: {region: 国際}, differential: "P-CABを使った診断的投与（要確認）", common_misconception: "PPIテスト陽性＝GERD確定と考える"}
  provenance: {<<: *W01, corroboration: "診断に関するCQ（本文で要確認）"}
  uncertainty: medium
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-011
  assertion: {plain_statement_ja: "GERDの外科治療（腹腔鏡下噴門形成術）と内視鏡的逆流防止術（ARMS等）は、PPI・P-CABが効かない症例や、長期の薬物依存を避けたい症例で選択肢になる。適応を決める前に、pH・インピーダンス検査や内圧検査で評価しておく必要がある。", condition: {region: 日本}, differential: "術前にアカラシアなどの運動障害を除外する", common_misconception: "裂孔ヘルニアがあれば全例手術と考える"}
  provenance: {<<: *W01, corroboration: "本文、およびARMSの保険収載状況は要確認"}
  uncertainty: medium
  curriculum: *C_GERD
  publication_info: *PUB
- id: ES-012
  assertion: {plain_statement_ja: "日本では食道胃接合部を柵状血管の下端で定義し、Barrett食道を全周3 cm以上のLSBEとそれ以外のSSBEに分ける。組織学的な腸上皮化生は必須としない。", condition: {region: 日本}, differential: "米国ACGは長さ1 cm以上と腸上皮化生を必須とする（ES-013）", common_misconception: "日本でも生検で杯細胞を確認しないとBarrettと呼べないと考える"}
  provenance: {<<: *W05, corroboration: "規約本文で文言を要確認"}
  uncertainty: medium
  curriculum: *C_BE
  publication_info: *PUB
- id: ES-013
  assertion: {plain_statement_ja: "米国ACG 2022は、Barrett食道の診断に二つの条件を求める。食道胃接合部より口側の円柱上皮が1 cm以上あること、そして生検で腸上皮化生を認めることである。", condition: {region: 米国}, differential: "日本の定義（ES-012）", common_misconception: "1 cm未満の不整なZ線もサーベイランスの対象と考える"}
  provenance: {<<: *W11, corroboration: "定義の節で要確認"}
  uncertainty: medium
  curriculum: *C_BE
  publication_info: *PUB
- id: ES-014
  assertion: {plain_statement_ja: "欧米の推計では、Barrett食道の癌化率は、異形成なし（NDBE）で年0.2〜0.5%程度、低異型度異形成（LGD）で年約0.7%、高異型度異形成（HGD）で年約7%である。",\[21\] condition: {region: 欧米}, differential: "日本のSSBEの発癌率はわかっていない（ES-015）", common_misconception: "NDBEの発癌率を過大に見積もる"}
  provenance: {<<: *W11, corroboration: "ACG 2015（10.1038/ajg.2015.322、非CC）。2022年版との数値の表記揺れを要確認"}
  uncertainty: medium
  curriculum: *C_BE
  publication_info: *PUB
- id: ES-015
  assertion: {plain_statement_ja: "日本では、Barrett食道から食道癌が発生するリスクは、報告例が少ないため明らかになっていない。",\[3\] condition: {region: 日本}, differential: "欧米ではBarrett食道が腺癌の確立した前癌病変", common_misconception: "欧米の発癌率を日本にそのまま当てはめる"}
  provenance: {<<: *W02, corroboration: "本文のSummaryで確認済み"}
  uncertainty: low
  curriculum: *C_BE
  publication_info: *PUB
- id: ES-016
  assertion: {plain_statement_ja: "ACG 2022は、NDBEのサーベイランス間隔を長さで分けている。3 cm未満は5年ごと、3 cm以上は3年ごとである。",\[22\]\[23\] condition: {region: 米国, population: NDBE}, differential: "LGDは1年間6か月ごと、その後は年1回", common_misconception: "NDBEを毎年内視鏡で追う必要があると考える"}
  provenance: {<<: *W11, corroboration: "AGA Clinical Practice Update（CGH 2022）と一致"}
  uncertainty: low
  curriculum: *C_BE
  publication_info: *PUB
- id: ES-017
  assertion: {plain_statement_ja: "ACGは、Barrett食道の生検について、炎症を制御してから2 cm間隔で4方向から系統的に行う方法（Seattle protocol）を標準としている。",\[21\] condition: {region: 米国}, differential: "日本ではNBIなどを使った狙撃生検が中心の施設が多い（要確認）", common_misconception: "炎症が強い時期の生検で異形成を判定する"}
  provenance: {<<: *W11, corroboration: "ACG 2015"}
  uncertainty: low
  curriculum: *C_BE
  publication_info: *PUB

# ===== 2. 好酸球性食道炎（EoE） =====
- id: ES-018
  assertion: {plain_statement_ja: "EoEは、次の三つがそろったときに診断する。食道の機能障害による症状があること、食道生検で上皮内の好酸球が15個/HPF以上（約60個/mm²）であること、好酸球増多をきたす他の疾患を除外したことである。",\[24\]\[25\] condition: {region: 国際}, differential: "GERD、好酸球性胃腸炎、薬剤性", common_misconception: "PPIで改善した例はEoEではないと考える"}
  provenance: {<<: *W13, corroboration: "AGREEも同じ閾値"}
  uncertainty: low
  curriculum: *C_EOE
  publication_info: *PUB
- id: ES-019
  assertion: {plain_statement_ja: "現在の国際診断基準では、PPIが効くことはEoEを除外する理由にならない。PPIはEoEの治療選択肢の一つとして扱われる。", condition: {region: 国際}, differential: "2007年・2011年の旧基準では、PPIが無効であることが要件だった", common_misconception: "PPIが効いたらEoEではないと考える"}
  provenance: {<<: *W12, corroboration: "ACG 2025"}
  uncertainty: low
  curriculum: *C_EOE
  publication_info: *PUB
- id: ES-020
  assertion: {plain_statement_ja: "日本の多施設研究では、上部消化管内視鏡130,013件のうちEoEは66例（0.051%）で、約38%は健診の内視鏡で見つかった。",\[26\] condition: {region: 日本, population: "内視鏡受検者（2012〜2018年、9施設）"}, differential: "欧米の人口あたり有病率とは分母が異なる", common_misconception: "小児のアレルギー患者だけの病気と考える"}
  provenance: {<<: *W14, corroboration: "PubMedの抄録"}
  uncertainty: low
  curriculum: *C_EOE
  publication_info: *PUB
- id: ES-021
  assertion: {plain_statement_ja: "EoEの典型的な内視鏡所見は、縦走溝、輪状溝、白斑、浮腫、狭窄である。これらはEREFSで点数化する。", condition: {region: 国際}, differential: "カンジダ食道炎の白苔", common_misconception: "内視鏡所見が正常ならEoEを否定できると考える"}
  provenance: {<<: *PEND, corroboration: "ACG 2025で要確認"}
  uncertainty: medium
  curriculum: *C_EOE
  publication_info: *PUB
- id: ES-022
  assertion: {plain_statement_ja: "EoEの初期治療には、PPI、嚥下させる局所ステロイド、除去食療法の3つがある。治療目標の目安は、組織学的に好酸球15個/HPF未満である。",\[27\] condition: {region: 国際}, differential: "日本で使える局所ステロイド製剤と保険適用は要確認", common_misconception: "全身ステロイドが第一選択と考える"}
  provenance: {<<: *W13, corroboration: "15個/HPF未満を目標とする記載は確認済み"}
  uncertainty: medium
  curriculum: *C_EOE
  publication_info: *PUB
- id: ES-023
  assertion: {plain_statement_ja: "デュピルマブ300 mg週1回投与の第3相試験Part Aでは、24週時の組織学的寛解（好酸球6個/HPF以下）が60%で、プラセボは5%だった。",\[28\] condition: {region: 国際, population: "12歳以上"}, differential: "Part Bの2週ごと投与では症状は改善しなかった", common_misconception: "寛解の閾値を15個/HPFと取り違える"}
  provenance: {<<: *W21, corroboration: "Part A 25/42 vs 2/39、Part B（週1回）47/80 vs 5/79"}
  uncertainty: low
  curriculum: *C_EOE
  publication_info: *PUB
- id: ES-024
  assertion: {plain_statement_ja: "米国FDAは2022年5月、12歳以上のEoEにデュピルマブを承認した。日本での承認状況は要確認である。",\[29\] condition: {region: "米国／日本（要確認）"}, differential: "日本ですでに承認されている適応", common_misconception: "国内でもEoEに保険適用があると前提する"}
  provenance: {<<: *PEND, corroboration: "ClinicalTrials.govのNCT05247866文書に記載。FDA一次資料で要確認"}
  uncertainty: high
  curriculum: *C_EOE
  publication_info: *PUB

# ===== 3. 食道運動障害 =====
- id: ES-025
  assertion: {plain_statement_ja: "Chicago分類v4.0では、アカラシアを、IRP中央値の異常と蠕動の完全消失で定義する。そのうえで、20%以上の嚥下で食道全体の同時加圧（PEP）を示すものをII型、PEPのないものをI型とする。",\[30\] condition: {region: 国際}, differential: "EGJOO（IRPは上昇しているが蠕動が残る）", common_misconception: "I型とII型を食道拡張の程度で区別する"}
  provenance: {<<: *W07, corroboration: "PMC8034247の表"}
  uncertainty: low
  curriculum: *C_MOT
  publication_info: *PUB
- id: ES-026
  assertion: {plain_statement_ja: "III型アカラシアは、IRP中央値が異常で、20%以上の嚥下が早期・痙攣性収縮を示し、正常な蠕動を伴わないものである。",\[30\]\[31\] condition: {region: 国際}, differential: "遠位食道痙攣（IRPは正常）", common_misconception: "蠕動の一部残存を許す"}
  provenance: {<<: *W07, corroboration: "PubMed 35232920"}
  uncertainty: low
  curriculum: *C_MOT
  publication_info: *PUB
- id: ES-027
  assertion: {plain_statement_ja: "Chicago分類v4.0では、正常値データベースを健常者75人から469人に拡大した。また、判定保留例には補助検査（時限バリウム食道造影、FLIP）を併用するよう勧めている。",\[32\] condition: {region: 国際}, differential: "v3.0との違い", common_misconception: "HRMだけですべての症例を確定できると考える"}
  provenance: {<<: *W07, corroboration: "二次レビュー。原典で要確認"}
  uncertainty: medium
  curriculum: *C_MOT
  publication_info: *PUB
- id: ES-028
  assertion: {plain_statement_ja: "遠位食道痙攣は、IRP中央値が正常で、20%以上の嚥下が早期収縮を示すものである。早期収縮の目安は遠位潜時（DL）4.5秒未満である。",\[30\]\[33\] condition: {region: 国際}, differential: "III型アカラシア", common_misconception: "遠位食道痙攣とIII型アカラシアをIRPで区別しない"}
  provenance: {<<: *W07, corroboration: "DLの閾値は要確認"}
  uncertainty: medium
  curriculum: *C_MOT
  publication_info: *PUB
- id: ES-029
  assertion: {plain_statement_ja: "過収縮食道（いわゆるジャックハンマー食道）は、IRP中央値が正常で、20%以上の嚥下が過収縮を示すものである。過収縮の目安はDCI\[30\] 8,000 mmHg·s·cm超である（閾値は要確認）。", condition: {region: 国際}, differential: "遠位食道痙攣", common_misconception: "1回の過収縮だけで診断する"}
  provenance: {<<: *W07, corroboration: "DCIの閾値は要確認"}
  uncertainty: medium
  curriculum: *C_MOT
  publication_info: *PUB
- id: ES-030
  assertion: {plain_statement_ja: "無効食道運動（IEM）は、IRPが正常で、70%超の嚥下が無効、または50%以上で蠕動が欠如するものである。IRPが正常で蠕動が完全に消失しているものは、収縮欠如とする。",\[30\] condition: {region: 国際}, differential: "強皮症", common_misconception: "収縮欠如とI型アカラシアを区別しない"}
  provenance: {<<: *W07, corroboration: "PMC8034247の表"}
  uncertainty: low
  curriculum: *C_MOT
  publication_info: *PUB
- id: ES-031
  assertion: {plain_statement_ja: "III型アカラシアやEGJOOでは、オピオイドの使用との関連が報告されている。そのため、診断の前に薬剤歴を確認する必要がある。",\[32\] condition: {region: 国際}, differential: "オピオイド誘発性の食道機能障害", common_misconception: "薬剤歴を聞かずに治療を始める"}
  provenance: {<<: *W07, corroboration: "二次レビュー（III型の11〜13%、EGJOOの13〜37%）。要確認"}
  uncertainty: medium
  curriculum: *C_MOT
  publication_info: *PUB
- id: ES-032
  assertion: {plain_statement_ja: "特発性アカラシア221例のRCTでは、2年時の臨床的成功率はPOEM 83.0%、LHM＋Dor噴門形成術81.7%で、POEMはLHMに対して非劣性だった。",\[34\]\[35\]\[36\] condition: {region: 欧州}, differential: "空気圧拡張術との比較は別のRCT", common_misconception: "POEMがLHMより優れると考える（示されたのは非劣性）"}
  provenance: {<<: *W20, corroboration: "NEJMのレター（10.1056/NEJMc2000065）"}
  uncertainty: low
  curriculum: *C_MOT
  publication_info: *PUB
- id: ES-033
  assertion: {plain_statement_ja: "同じRCTでは、逆流性食道炎がPOEM群に多かった（3か月時57% vs 20%、2年時44% vs 29%）。重篤な有害事象はPOEM 2.7%、LHM 7.3%だった。",\[36\] condition: {region: 欧州}, differential: "LHMは噴門形成術を加えるため逆流が少ない", common_misconception: "POEMには逆流の問題がないと考える"}
  provenance: {<<: *W20, corroboration: "NEJMのレター"}
  uncertainty: low
  curriculum: *C_MOT
  publication_info: *PUB
- id: ES-034
  assertion: {plain_statement_ja: "III型アカラシアでは、口側まで長く筋切開できるPOEMが有利とされる（ガイドライン上の根拠は要確認）。", condition: {region: 国際}, differential: "I・II型では空気圧拡張術、LHM、POEMのいずれも選択肢", common_misconception: "病型によらず治療成績は同じと考える"}
  provenance: {<<: *PEND, corroboration: "ACG・ASGE 2020で要確認"}
  uncertainty: high
  curriculum: *C_MOT
  publication_info: *PUB

# ===== 4. 食道癌 =====
- id: ES-035
  assertion: {plain_statement_ja: "日本の食道癌の罹患率（粗率）は、2015年で男性が人口10万人あたり31.2人、女性が5.9人と推計されている。年齢調整罹患率は、男性で横ばいか減少、女性で横ばいかごく緩やかな増加である。",\[3\] condition: {region: 日本}, differential: "粗率と年齢調整率の違い", common_misconception: "男女比が1:1に近いと考える"}
  provenance: {<<: *W02, corroboration: "国立がん研究センターのデータを引用。最新値への更新が必要"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-036
  assertion: {plain_statement_ja: "2019年の日本の食道癌死亡数は11,619人（粗死亡率は人口10万人あたり9.4）で、悪性新生物による死亡の3.1%を占めた。年齢調整死亡率は男女とも低下傾向にある。",\[3\] condition: {region: 日本}, differential: "罹患と死亡では動向が異なる", common_misconception: "死亡率は上昇していると考える"}
  provenance: {<<: *W02, corroboration: "厚生労働省の人口動態統計を引用"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-037
  assertion: {plain_statement_ja: "日本食道学会の全国調査（2013年治療の8,019例）では、男女比は約5.4:1だった。占居部位は胸部中部食道が約47%で最も多く、組織型は扁平上皮癌が約86%、腺癌が約7%だった。",\[3\] condition: {region: 日本}, differential: "欧米では腺癌が半数以上", common_misconception: "日本でも腺癌が主体と考える"}
  provenance: {<<: *W02, corroboration: "60〜70歳代が約7割。部位は胸部下部28%、胸部上部12%、腹部8%、頸部5%"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-038
  assertion: {plain_statement_ja: "日本の食道扁平上皮癌の主な危険因子は喫煙と習慣的飲酒で、診断例の約9割に関わる。両者が重なるとリスクは相乗的に高まる。緑黄色野菜と果物の摂取は予防因子とされる。",\[3\] condition: {region: 日本}, differential: "腺癌の危険因子はGERD、Barrett食道、肥満", common_misconception: "飲酒単独は危険因子にならないと考える"}
  provenance: {<<: *W02, corroboration: "本文"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-039
  assertion: {plain_statement_ja: "欧米では食道癌に占める腺癌の割合が増え、現在は半数以上を占める。腺癌の発生母地は、GERDによる慢性炎症から生じるBarrett上皮である。",\[3\] condition: {region: 欧米}, differential: "日本は扁平上皮癌が約86%", common_misconception: "世界的に扁平上皮癌が主体と考える"}
  provenance: {<<: *W02, corroboration: "本文"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-040
  assertion: {plain_statement_ja: "飲酒で生じるアセトアルデヒドは、2009年にWHOの作業部会でGroup 1の発がん物質とされた。アルコールやアセトアルデヒドを代謝する能力に関わる遺伝要因（ALDH2の不活性型など）は、飲酒による発癌リスクを左右する。",\[3\] condition: {region: "東アジア／日本"}, differential: "ADH1Bの低活性型（要確認）", common_misconception: "少量の飲酒で顔が赤くなる人（フラッシャー）は安全と考える（実際は高リスク）"}
  provenance: {<<: *W02, corroboration: "ALDH2ヘテロ型でのオッズ比は要確認"}
  uncertainty: "low（方向性）／high（数値）"
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-041
  assertion: {plain_statement_ja: "食道癌には同時性・異時性の多重癌が多く、特に頭頸部癌と胃癌の合併に注意が必要である（頭頸部癌の診療で食道を調べることの推奨は要確認）。",\[3\] condition: {region: 日本}, differential: "field cancerization（領域発癌）", common_misconception: "食道癌の治療後は頭頸部を観察しなくてよいと考える"}
  provenance: {<<: *W02, corroboration: "多重癌が多いことは確認済み"}
  uncertainty: medium
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-042
  assertion: {plain_statement_ja: "ヨード染色では、正常な扁平上皮は褐色に染まり、癌や異形成は不染帯として描出される。多発ヨード不染帯は、食道癌・頭頸部癌のリスクが高いことを示す。", condition: {region: 日本}, differential: "NBIではbrownish areaとして見える", common_misconception: "濃く染まる部分が癌と考える"}
  provenance: {<<: *PEND, corroboration: "W02・W05で要確認"}
  uncertainty: medium
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-043
  assertion: {plain_statement_ja: "日本食道学会の拡大内視鏡分類では、微小血管を境界病変のType Aと癌のType Bに分ける。Type Bはさらに、ループ様構造が保たれるB1、ループが消失するB2、高度に拡張したB3に分ける。",\[37\]\[38\] condition: {region: 日本}, differential: "井上分類と有馬分類を統合した分類", common_misconception: "Type Aも癌を示すと考える"}
  provenance: {<<: *W05, corroboration: "W06（PMID 28386209）、PMID 28706424"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-044
  assertion: {plain_statement_ja: "B1はT1a-EP/LPM、B2はT1a-MM/T1b-SM1、B3はT1b-SM2以深に対応する。B1とB3の正診率は高いが、B2は深達度を深読みしやすい。",\[37\]\[39\] condition: {region: 日本}, differential: "EUSとの併用", common_misconception: "B2なら必ずSM浸潤と考える"}
  provenance: {<<: *W05, corroboration: "陽性的中率はB1 92.4%、B3 90.7%（BMC Gastroenterol 2024）"}\[40\]
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-045
  assertion: {plain_statement_ja: "表在食道扁平上皮癌の内視鏡切除は、EP/LPMにとどまる病変が良い適応である。MM/SM1は相対的適応、SM2以深は原則として外科切除か化学放射線療法の対象となる。", condition: {region: 日本}, differential: "リンパ節転移のリスクは深達度とともに上がる", common_misconception: "SM浸潤でもESDだけで根治できると考える"}
  provenance: {<<: *W02, corroboration: "W15、PMC6510875"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-046
  assertion: {plain_statement_ja: "食道ESDで全周の3/4を超える粘膜欠損が生じる場合は、術後狭窄の予防にステロイドを使うことが勧められる。長径5 cmを超える全周性病変はESDの適応外とされる。",\[41\]\[42\] condition: {region: 日本}, differential: "予防的なバルーン拡張術", common_misconception: "半周程度の切除でも全例にステロイドが必要と考える"}
  provenance: {<<: *W15, corroboration: "Clin Endosc 2022"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-047
  assertion: {plain_statement_ja: "内視鏡切除後の病理でpT1a-MMかつ脈管侵襲陽性、またはpT1b-SMだった場合は、追加治療として食道切除術か化学放射線療法を行う根拠がある。",\[43\] condition: {region: 日本}, differential: "pT1a-EP/LPMで断端陰性なら経過観察", common_misconception: "断端陰性なら深達度に関係なく経過観察でよいと考える"}
  provenance: {<<: *W02, corroboration: "二次資料経由。本文で要確認"}
  uncertainty: medium
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-048
  assertion: {plain_statement_ja: "病期分類には、日本食道学会の食道癌取扱い規約（現行12版）とUICC/AJCCのTNM分類がある。両者は異なるため、試験結果を読むときはどちらの分類のどの版を使ったかを確認する必要がある。", condition: {region: "日本／国際"}, differential: "JCOG1109はUICC第7版を使用",\[44\] common_misconception: "取扱い規約のStageとUICCのStageを同じものとみなす"}
  provenance: {<<: *W05, corroboration: "具体的な相違点は要確認"}
  uncertainty: medium
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-049
  assertion: {plain_statement_ja: "JCOG1109 NExT試験（局所進行食道扁平上皮癌601例）では、術前DCF療法がCF療法より全生存を改善した。3年全生存率はDCF 72.1%、CF 62.6%、ハザード比は0.68だった。",\[45\]\[46\] condition: {region: 日本, population: "cStage IB/II/III（T4を除く、UICC第7版）"}, differential: "術前CF＋放射線療法は、CFに比べ全生存を有意には改善しなかった（3年全生存率68.3%）",\[46\]\[47\] common_misconception: "pCR率が最も高い術前CRTが最も生存を改善すると考える"}
  provenance: {<<: *W16, corroboration: "二次資料（PMC12321551）。本文で要確認"}
  uncertainty: "low（結論）／medium（数値）"
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-050
  assertion: {plain_statement_ja: "JCOG1109の病理学的完全奏効（pCR）率は、CF＋放射線療法38.5%、DCF 19.8%、CF 2.0%だった。CRT群のpCR率の高さは全生存の改善につながらなかった。",\[48\] condition: {region: 日本}, differential: "CROSS試験", common_misconception: "pCRは常に全生存の代わりの指標になると考える"}
  provenance: {<<: *W16, corroboration: "二次資料（PMC12321551）"}
  uncertainty: medium
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-051
  assertion: {plain_statement_ja: "CheckMate 577試験（794例）の対象は、術前化学放射線療法とR0切除の後に病理学的な残存病変がある症例である。術後ニボルマブは、無病生存期間の中央値をプラセボの11.0か月から22.4か月に延長した（ハザード比0.69）。",\[49\]\[50\] condition: {region: 国際, population: "術前CRT後にR0切除され、pCRに至らなかった症例"}, differential: "日本の標準である術前化学療法後の症例は対象外", common_misconception: "全生存の改善を示した試験と考える（要確認）"}
  provenance: {<<: *W17, corroboration: "NEJMの抄録。全生存の結果はPMC12765972"}
  uncertainty: "low（無病生存）／medium（全生存）"
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-052
  assertion: {plain_statement_ja: "CheckMate 648試験（未治療の進行食道扁平上皮癌970例）では、ニボルマブ＋化学療法とニボルマブ＋イピリムマブのいずれも、化学療法単独より全生存を延長した。延長は、腫瘍細胞PD-L1 1%以上の集団と全体集団の両方で有意だった。",\[51\]\[52\] condition: {region: 国際}, differential: "無増悪生存で優越性を示したのは、ニボルマブ＋化学療法（PD-L1 1%以上）のみ",\[52\] common_misconception: "PD-L1陰性でも同じ程度の効果があると考える"}
  provenance: {<<: *W18, corroboration: "PMC11077338"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-053
  assertion: {plain_statement_ja: "KEYNOTE-590試験（749例）では、一次治療としてのペムブロリズマブ＋化学療法が全生存を延長した。扁平上皮癌かつPD-L1 CPS 10以上の集団では、全生存期間の中央値が13.9か月 vs 8.8か月、ハザード比0.57だった。",\[53\]\[54\] condition: {region: 国際}, differential: "対象には腺癌とSiewert I型の食道胃接合部腺癌も含まれる",\[55\] common_misconception: "扁平上皮癌だけを対象とした試験と考える"}
  provenance: {<<: *W19, corroboration: "日本人サブグループ解析はPMC9436840"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-054
  assertion: {plain_statement_ja: "KEYNOTE-590の5年追跡では、全体集団の5年生存率がペムブロリズマブ＋化学療法10.6%、化学療法単独3.0%だった。",\[56\]\[57\] condition: {region: 国際}, differential: "長期生存例は扁平上皮癌かつCPS 10以上に多い",\[58\] common_misconception: "多くの患者が治癒すると過大に評価する"}
  provenance: {source: "KEYNOTE-590 5-year follow-up. ESMO Open 2025", doi: "要確認", pmid: "要確認", pmcid: "", url: "", source_license: "未確認", basis_tag: E, corroboration: "ASCO Post（二次資料）"}
  uncertainty: medium
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-055
  assertion: {plain_statement_ja: "切除できない局所進行食道癌や、手術を望まない・耐えられないcStage II/IIIの症例では、根治的化学放射線療法が選択肢になる。その後に病変が遺残・再発した場合は、救済手術を検討する。", condition: {region: 日本}, differential: "救済手術は合併症のリスクが高い", common_misconception: "CRT後に遺残があれば全例緩和治療のみと考える"}
  provenance: {<<: *W02, corroboration: "治療アルゴリズム（要確認）"}
  uncertainty: medium
  curriculum: *C_CA
  publication_info: *PUB
- id: ES-056
  assertion: {plain_statement_ja: "日本食道学会のガイドラインは、76歳以上の患者に推奨を当てはめるときは注意するよう求めている。",\[3\] condition: {region: 日本, population: 高齢者}, differential: "根拠となった試験の多くは75歳以下を対象としていた",\[3\] common_misconception: "推奨は年齢に関係なく一律に適用できると考える"}
  provenance: {<<: *W02, corroboration: "本文で確認済み"}
  uncertainty: low
  curriculum: *C_CA
  publication_info: *PUB

# ===== 5. 食道静脈瘤・門脈圧亢進症 =====
- id: ES-057
  assertion: {plain_statement_ja: "臨床的に有意な門脈圧亢進症（CSPH）は、肝静脈圧較差（HVPG）10 mmHg以上で定義される。",\[59\] condition: {region: 国際}, differential: "HVPG 6〜9 mmHgはCSPHに至らない門脈圧亢進", common_misconception: "静脈瘤がなければCSPHではないと考える"}
  provenance: {<<: *W09, corroboration: "Baveno VII"}
  uncertainty: low
  curriculum: *C_VX
  publication_info: *PUB
- id: ES-058
  assertion: {plain_statement_ja: "Baveno VIIとAASLD 2024は、CSPHのある代償性肝硬変に非選択的β遮断薬（NSBB）を勧めており、カルベジロールを優先する。目的は非代償化の予防にまで及ぶ。",\[59\]\[60\] condition: {region: 欧米}, differential: "従来は高リスク静脈瘤の一次予防に限っていた", common_misconception: "NSBBの目的は出血予防だけと考える"}
  provenance: {<<: *W09, corroboration: "日本での扱いは要確認"}
  uncertainty: "low（欧米）／要確認（日本）"
  curriculum: *C_VX
  publication_info: *PUB
- id: ES-059
  assertion: {plain_statement_ja: "AASLD 2024は、門脈圧亢進症に用いるNSBBとしてカルベジロールを第一に勧め、維持量を1日6.25〜12.5 mgとしている。",\[61\] condition: {region: 米国}, differential: "プロプラノロール、ナドロール", common_misconception: "カルベジロールを心拍数55/分になるまで増量すると考える"}
  provenance: {<<: *W09, corroboration: "ガイダンスの推奨文"}
  uncertainty: low
  curriculum: *C_VX
  publication_info: *PUB
- id: ES-060
  assertion: {plain_statement_ja: "AASLD 2024は、高リスク静脈瘤の一次予防としてNSBBとEVLの両方を認めるが、NSBBを優先する。EVLは、NSBBを使えない場合に行う。",\[61\] condition: {region: 米国}, differential: "日本では内視鏡治療の比重が大きい（要確認）", common_misconception: "NSBBとEVLの併用が一次予防の標準と考える"}
  provenance: {<<: *W09, corroboration: "ガイダンス本文"}
  uncertainty: low
  curriculum: *C_VX
  publication_info: *PUB
- id: ES-061
  assertion: {plain_statement_ja: "日本の食道静脈瘤の内視鏡所見記載基準では、占居部位（L）、形態（F）、基本色調（C）、発赤所見（RC sign）、出血所見、粘膜所見を記載する。", condition: {region: 日本}, differential: "欧米は大きさ5 mmを境にしたsmall/largeの2分類が中心", common_misconception: "F1でRC陽性でも出血リスクは低いと考える"}
  provenance: {<<: *PEND, corroboration: "学会資料（©）の原典は未入手。項目名のみ使用"}
  uncertainty: medium
  curriculum: *C_VX
  publication_info: *PUB
- id: ES-062
  assertion: {plain_statement_ja: "肝硬変の急性静脈瘤出血では、血管作動薬を内視鏡の前から早期に開始して2〜5日続ける。あわせて予防的抗菌薬を投与し、12時間以内に内視鏡を行って、食道静脈瘤にはEVLを施行する。",\[62\]\[63\]\[64\] condition: {region: 欧米}, differential: "日本で使える血管作動薬の保険適用は要確認", common_misconception: "抗菌薬は感染徴候があるときだけ使うと考える"}
  provenance: {<<: *W08, corroboration: "ESGE 2022、AASLD"}
  uncertainty: low
  curriculum: *C_VX
  publication_info: *PUB
- id: ES-063
  assertion: {plain_statement_ja: "急性上部消化管出血921例のRCTでは、Hb 7 g/dL未満で輸血する制限輸血が、9 g/dL未満で輸血する非制限輸血より、45日死亡（5% vs 9%）と再出血（10% vs 16%）を減らした。",\[65\]\[66\] condition: {region: "スペイン（単施設）"}, differential: "非制限輸血群では門脈圧較差が上昇した",\[67\] common_misconception: "Hb 10 g/dL以上を目標に輸血すると考える"}
  provenance: {<<: *W22, corroboration: "NEJMの抄録"}
  uncertainty: low
  curriculum: *C_VX
  publication_info: *PUB
- id: ES-064
  assertion: {plain_statement_ja: "Baveno VIIは、出血リスクの高い症例に72時間以内（可能なら24時間以内）の先制的TIPSを勧めている。対象は、Child-Pugh\[68\]\[69\] Cで14点未満、内視鏡時に活動性出血のあるChild-Pugh Bで7点超、または出血時のHVPGが20 mmHg超の症例である。", condition: {region: 欧州}, differential: "止血できない場合などに行う救済TIPSとは別", common_misconception: "Child-Pugh 14〜15点の最重症例ほど恩恵が大きいと考える（対象外）"}
  provenance: {<<: *W08, corroboration: "ESGE 2022、PMC12296215"}
  uncertainty: low
  curriculum: *C_VX
  publication_info: *PUB
- id: ES-065
  assertion: {plain_statement_ja: "高リスク静脈瘤出血63例のRCTでは、72時間以内の早期TIPSが、薬物療法＋EVLに比べて1年生存率を改善した（86% vs 61%）。6週生存率も97% vs 67%だった。",\[16\]\[17\]\[70\] condition: {region: 欧州, population: "Child-Pugh C 10〜13点、または活動性出血を伴うChild-Pugh B"}, differential: "追試では結果が一定しない（要確認）", common_misconception: "早期TIPSで肝性脳症が大きく増えると考える"}\[70\]
  provenance: {<<: *W23, corroboration: "PubMedの抄録"}
  uncertainty: low
  curriculum: *C_VX
  publication_info: *PUB
- id: ES-066
  assertion: {plain_statement_ja: "日本では食道静脈瘤の内視鏡治療として、EVLに加え内視鏡的硬化療法（EIS）も使われる。胃静脈瘤にはB-RTOが広く行われる。一方、欧米のガイドラインはEVLを標準としている。", condition: {region: "日本 vs 欧米"}, differential: "胃静脈瘤にはシアノアクリレートやB-RTO", common_misconception: "日本でもEVLだけが標準と考える"}
  provenance: {<<: *PEND, corroboration: "JSGE肝硬変診療GL 2020英語版で要確認"}
  uncertainty: medium
  curriculum: *C_VX
  publication_info: *PUB

# ===== 6. その他（一次出典未取得：骨子のみ） =====
- id: ES-067
  assertion: {plain_statement_ja: "嘔吐を繰り返した後の吐血では、Mallory-Weiss症候群（食道胃接合部付近の粘膜裂創）を考える。多くは自然に止血する。嘔吐後に激しい胸痛、皮下気腫、縦隔気腫を伴う場合は、Boerhaave症候群（食道の全層性破裂）を疑い、緊急に対応する。", condition: {region: 国際}, differential: "粘膜だけの裂創か全層性の破裂か。心筋梗塞、大動脈解離", common_misconception: "Boerhaave症候群の診断に内視鏡を最初に行う（要確認）"}
  provenance: {<<: *PEND, corroboration: "CC資料での裏付けが必要"}
  uncertainty: medium
  curriculum: *C_OTH
  publication_info: *PUB
- id: ES-068
  assertion: {plain_statement_ja: "以下の項目は骨子のみ確定し、出典は次回以降に補う。①食道異物（ボタン電池は緊急摘出）②腐食性食道炎（嘔吐の誘発や中和は避ける）③食道裂孔ヘルニア ④薬剤性食道炎（テトラサイクリン系、ビスホスホネート、塩化カリウムなど）⑤カンジダ食道炎 ⑥ヘルペス食道炎（小さな打ち抜き潰瘍）⑦CMV食道炎（大きく浅い潰瘍）⑧Plummer-Vinson症候群 ⑨Zenker憩室。", condition: {region: 国際}, differential: "⑥と⑦では潰瘍の形態が異なる", common_misconception: "腐食性物質を誤飲したら嘔吐させると考える"}
  provenance: {<<: *PEND, corroboration: "ES-069以降に分割し、出典を付ける"}
  uncertainty: high
  curriculum: *C_OTH
  publication_info: *PUB
```

---

## 3. カリキュラム対応（番号はすべて要確認）

| サブ領域 | 事実票ID | コアカリ | 国試出題基準（項目名） |
|---|---|---|---|
| GERD・Barrett食道 | ES-001〜017 | PS-02-08-xx | 胃食道逆流症、Barrett食道 |
| EoE | ES-018〜024 | PS-02-08-xx | 好酸球性食道炎 |
| 運動障害 | ES-025〜034 | PS-02-08-xx | 食道アカラシア、びまん性食道痙攣 |
| 食道癌 | ES-035〜056 | PS-02-08-xx | 食道癌 |
| 静脈瘤 | ES-057〜066 | PS-02-08-xx（第4回「肝」と調整） | 食道・胃静脈瘤 |
| その他 | ES-067〜068 | PS-02-08-xx | Mallory-Weiss症候群、特発性食道破裂ほか |

症候との対応（第7回への入力）：嚥下障害、胸やけ、吐血、胸痛。

---

## 4. 未解決事項・要確認リストと、第2回への引き継ぎ

### 4-1. 要確認
1. **RCTのPMIDとライセンス。** W16〜W23のPMIDと、W03・W06・W10・W12〜W14・W18・W19のライセンスを照合する。レート制限で今回は照合できなかった。
2. **Baveno VIIのライセンス。** CC BY-NC-NDかどうかを出版社のページで確認する。
3. **W01の本文。** 用量、診断・外科治療に関するCQ、REの有病率を本文で確認する。
4. **個別の数値。** ES-009（AETの閾値）、ES-029（DCIの閾値）、ES-031（オピオイドの割合）、ES-034（III型へのPOEM）、ES-040（ALDH2のオッズ比）を原典で確認する。
5. **日本の承認状況。** ES-011・ES-022・ES-024・ES-051について、PMDAの添付文書で確認する。
6. **日本独自の基準。** ES-061（門脈圧亢進症学会の記載基準）とES-066（JSGE肝硬変GL 2020）を確認する。
7. **件数の補充。** ES-068をES-069〜080に分割し、目標の80件に近づける。
8. **がん統計の更新。** 国立がん研究センターの最新値に差し替える。

### 4-2. 第2回（胃・十二指腸）への引き継ぎ
- **重複の回避。** HP-001〜020とUG-001〜018は扱わない。食道静脈瘤出血は今回扱ったので、第2回では胃静脈瘤、GAVE、門脈圧亢進症性胃症に限る。
- **食道胃接合部癌。** 第2回では胃癌側の扱いに限り、ES-048・ES-053と相互参照する。
- **運用ルール。** YAMLのmerge keyに取り込み側が対応していなければ、展開版で納品する。basis_tagのA〜Gは前回の定義と照合して統一する。

## 出典

1. <https://api.crossref.org/works/10.1007/s00535-022-01861-z>
2. [Checking your browser - reCAPTCHA](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8938399/)
3. [Esophageal cancer practice guidelines 2022 edited by the Japan esophageal society: part 1 - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10024303/)
4. <https://api.crossref.org/works/10.1007/s10388-016-0551-7>
5. <https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles?ids=10.1007/s10388-024-01054-y,10.1007/s10388-016-0551-7,10.1111/nmo.14058&format=json>
6. <https://api.crossref.org/works/10.1007/s10388-024-01054-y>
7. [Prediction of the invasion depth of superficial squamous cell carcinoma based on microvessel morphology: magnifying endoscopic classification of the Japan Esophageal Society - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5362661)
8. <https://api.crossref.org/works/10.1111/nmo.14058>
9. <https://api.crossref.org/works/10.1016/j.jhep.2021.12.022>
10. [Corrigendum to ‘Baveno VII](https://mayoclinic.elsevierpure.com/en/publications/corrigendum-to-baveno-vii-renewing-consensus-in-portal-hypertensi)
11. <https://api.crossref.org/works/10.1097/HEP.0000000000000647>
12. [AASLD Practice Guidance on risk stratification and... : Hepatology](https://journals.lww.com/hep/fulltext/2024/05000/aasld_practice_guidance_on_risk_stratification_and.22.aspx)
13. <https://api.crossref.org/works/10.14309/ajg.0000000000001680>
14. <https://api.crossref.org/works/10.1111/den.13654>
15. <https://api.crossref.org/works/10.1056/NEJMoa2032125>
16. [Early Use of TIPS in Patients with Cirrhosis and Variceal Bleeding](https://www.nejm.org/doi/full/10.1056/NEJMoa0910102)
17. [Early use of TIPS in patients with cirrhosis and variceal bleeding - PubMed](https://pubmed.ncbi.nlm.nih.gov/20573925/)
18. [九州大学学術情報リポジトリ Kyushu University Institutional Repository](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7161620/7161620.pdf)
19. [Evidence-based clinical practice guidelines for gastroesophageal reflux disease 2021](https://link.springer.com/article/10.1007/s00535-022-01861-z)
20. [Expert Opinion on Drug Safety](https://www.tandfonline.com/doi/pdf/10.1080/14740338.2026.2612982)
21. [ACG Clinical Guideline: Diagnosis and Management of Barrett’s Esophagus](https://journals.lww.com/ajg/fulltext/10.1038/ajg.2015.322~acg-clinical-guideline-diagnosis-and-management-of-barretts)
22. [Guideline-2022-ACG-barretts.pdf](https://www.giboardreview.com/wp-content/uploads/2022/04/Guideline-2022-ACG-barretts.pdf)
23. [Diagnosis and Management of Barrett’s Esophagus: An Updated ACG Guideline](https://med.emory.edu/departments/medicine/_documents/veeramachaneni_acg-barretts-esophagus.pdf)
24. [Updated International Consensus Diagnostic Criteria for Eosinophilic Esophagitis: Proceedings of the AGREE Conference - Gastroenterology](<https://www.gastrojournal.org/article/S0016-5085(18)34763-2/fulltext>)
25. [ACG Clinical Guideline: Diagnosis and Management of Eosinophilic Esophagitis](https://journals.lww.com/ajg/fulltext/10.14309/ajg.0000000000003194~acg-clinical-guideline-diagnosis-and-management-of)
26. [Clinical and endoscopic characteristics of eosinophilic esophagitis in Japan: a case-control study - PubMed](https://pubmed.ncbi.nlm.nih.gov/32411581/)
27. [ACG Clinical Guideline: Diagnosis and Management of... : Official journal of the American College of Gastroenterology](https://journals.lww.com/ajg/fulltext/2025/01000/acg_clinical_guideline__diagnosis_and_management.16.aspx)
28. [Dupilumab in Adults and Adolescents with Eosinophilic Esophagitis](https://www.nejm.org/doi/full/10.1056/NEJMoa2205982)
29. [Efficacy of Dupilumab on Facilitated Food Introduction in Eosinophilic Esophagitis](https://cdn.clinicaltrials.gov/large-docs/66/NCT05247866/Prot_SAP_000.pdf)
30. [ESOPHAGEAL MOTILITY DISORDERS ON HIGH RESOLUTION MANOMETRY: CHICAGO CLASSIFICATION VERSION 4.0© - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8034247/)
31. [\[Chicago Classification ver. 4.0: Diagnosis of Achalasia and Esophagogastric Junction Outflow Obstruction\] - PubMed](https://pubmed.ncbi.nlm.nih.gov/35232920/)
32. [Chicago Classification Version 4.0 and Its Impact on Current Clinical Practice - Gastroenterology & Hepatology](https://www.gastroenterologyandhepatology.net/archives/october-2021/chicago-classification-version-4-0-and-its-impact-on-current-clinical-practice/)
33. [Esophageal Motility Disorders: A Concise Review on Classification, Diagnosis, and Management - Mayo Clinic Proceedings](https://www.mayoclinicproceedings.org/article/S0025-6196%252824%252900621-9/fulltext)
34. [Endoscopic or Surgical Myotomy in Patients with Idiopathic Achalasia](https://www.nejm.org/doi/full/10.1056/NEJMoa1905380)
35. [Endoscopic or Surgical Myotomy in Achalasia](https://www.nejm.org/doi/10.1056/NEJMc2000065)
36. [POEM vs Surgical Myotomy for Achalasia -Randomized Trial](https://gutsandgrowth.com/2019/12/20/poem-vs-surgical-myotomy-for-achalasia-randomized-trial/)
37. [Japanese Classification of Esophageal Cancer, 12th Edition: Part I](https://link.springer.com/article/10.1007/s10388-024-01054-y)
38. [Japanese Classification of Esophageal Cancer, 12th Edition: Part I - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11199297/)
39. [The sub‐classification of type B2 vessels according to the magnifying endoscopic classification of the Japan Esophageal Society - Tanaka - 2020 - Digestive Endoscopy - Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1111/den.13459)
40. [Evaluating the usefulness of considering the size and morphological type of type B2 vessel area based on Japan Esophageal Society classification in estimating tumor invasion depth in superficial esophageal squamous cell carcinomas: study protocol for a prospective observational study (Japan BEES study)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10811940/)
41. [Prevention of stricture after endoscopic submucosal dissection for esophageal cancer: intralesional steroid infusion using a spray tube](https://www.e-ce.org/journal/view.php?doi=10.5946%2Fce.2022.164)
42. [Predictive factors for esophageal stenosis in patients receiving prophylactic steroid therapy after endoscopic submucosal dissection for esophageal squamous cell carcinoma](https://link.springer.com/article/10.1186/s12876-024-03135-9)
43. [Treatment strategy for early-stage esophageal cancer](https://link.springer.com/article/10.1007/s11604-024-01547-x)
44. [A randomized controlled phase III trial comparing two chemotherapy regimen and chemoradiotherapy regimen as neoadjuvant treatment for locally advanced esophageal cancer, JCOG1109 NExT study.](https://ascopubs.org/doi/10.1200/JCO.2022.40.4_suppl.238)
45. [Preoperative radiotherapy in patients with locally advanced esophageal squamous cell carcinoma: a narrative review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12321551/)
46. [Doublet chemotherapy, triplet chemotherapy, or doublet chemotherapy combined with radiotherapy as neoadjuvant treatment for locally advanced oesophageal cancer (JCOG1109 NExT): a randomised, controlled, open-label, phase 3 trial.](https://www.bjsacademy.com/bjs-academy/randomized-clinical-trials/doublet-chemotherapy-triplet-chemotherapy-or-doublet-chemotherapy-combined-with-radiotherapy-as-neoadjuvant-treatment-for-locally-advanced-oesophageal-cancer-jcog1109-next-a-randomised-controlled-open-label-phase-3-trial)
47. [Esophageal Cancer Neoadjuvant Triplet or Doublet Chemotherapy With or Without Radiotherapy - The ASCO Post](https://ascopost.com/news/june-2024/esophageal-cancer-neoadjuvant-triplet-or-doublet-chemotherapy-with-or-without-radiotherapy/)
48. [Preoperative radiotherapy in patients with locally advanced esophageal squamous cell carcinoma: a narrative review - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12321551)
49. [Nivolumab Improves Outcomes in Esophageal/GEJ Cancer](https://www.targetedonc.com/view/nivolumab-improves-outcomes-in-esophageal-gej-cancer)
50. [Adjuvant Nivolumab in Resected Esophageal or... : New England Journal of Medicine](https://www.ovid.com/journals/nejm/fulltext/10.1056/nejmoa2032125~adjuvant-nivolumab-in-resected-esophageal-or)
51. [Nivolumab in Esophageal Squamous-Cell Carcinoma](https://www.nejm.org/doi/abs/10.1056/NEJMc2202880)
52. [Nivolumab plus chemotherapy or ipilimumab versus chemotherapy in patients with advanced esophageal squamous cell carcinoma (CheckMate 648): 29‐month follow‐up from a randomized, open‐label, phase III trial](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11077338/)
53. [Pembrolizumab plus chemotherapy versus chemotherapy alone for first-line treatment of advanced oesophageal cancer (KEYNOTE-590): a randomised, placebo-controlled, phase 3 study - The Lancet](<https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(21)01234-4/abstract>)
54. [Pembrolizumab Plus Chemotherapy Combination Improves Survival in Esophageal Squamous Cell Carcinoma](https://www.cancernetwork.com/view/pembrolizumab-chemotherapy-combination-improves-survival-in-esophageal-squamous-cell-carcinoma)
55. [First-line pembrolizumab + chemotherapy in Japanese patients with advanced/metastatic esophageal cancer from KEYNOTE-590](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9436840/)
56. [Long-Term Follow-up Affirms Benefit of Pembrolizumab Plus Chemotherapy in Advanced Esophageal Cancer - The ASCO Post](https://ascopost.com/issues/march-10-2024/long-term-follow-up-affirms-benefit-of-pembrolizumab-plus-chemotherapy-in-advanced-esophageal-cancer/)
57. [Long-Term Follow-up of KEYNOTE-590 Benefit of Pembrolizumab Plus Chemotherapy Affirmed in Advanced Esophageal Cancer - The ASCO Post](https://ascopost.com/news/january-2024/long-term-follow-up-of-keynote-590-benefit-of-pembrolizumab-plus-chemotherapy-affirmed-in-advanced-esophageal-cancer/)
58. [Pembrolizumab plus chemotherapy versus chemotherapy for advanced esophageal cancer: 5-year extended follow-up for the randomized phase III KEYNOTE-590 study - ESMO Open](<https://www.esmoopen.com/article/S2059-7029(25)01723-5/fulltext>)
59. [New AASLD Guidance Suggests Major Changes for Portal Hypertension Management - DDW News](https://news.ddw.org/news/new-aasld-guidance-suggests-major-changes-for-portal-hypertension-management/)
60. [Advances in the management of complications from cirrhosis](https://academic.oup.com/gastro/article/doi/10.1093/gastro/goae072/7727525)
61. [AASLD Practice Guidance on risk stratification and management of portal hypertension and varices in cirrhosis](https://journals.lww.com/hep/fulltext/10.1097/hep.0000000000000647~aasld-practice-guidance-on-risk-stratification-and)
62. [Early TIPS - Wiki Journal Club](https://www.wikijournalclub.org/wiki/Early_TIPS)
63. [#55 Cirrhosis and Variceal GI Bleeds — Critical Care Time](https://www.criticalcaretime.com/episodes/variceal-gi-bleed)
64. [Medline ® Abstracts for References 22,32 of 'Overview of the management of patients with variceal bleeding' - UpToDate](https://www.uptodate.com/contents/1254/abstract/22,32)
65. [Villanuev](https://criticalcarereviews.com/foundational-trials/villanuev)
66. [Google Scholar](https://scholar.google.com/scholar_lookup?title=Transfusion+for+acute+upper+gastrointestinal+bleeding.&publication_year=2013&author=C+Villanueva&author=A+Colomo&author=A+Bosch)
67. [Villanueva](https://www.thebottomline.org.uk/summaries/icm/villanueva/)
68. [Preemptive Transjugular Intrahepatic Portosystemic Shunt in Variceal Bleeding: A Real-World Study in a Tertiary Hospital - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12296215/)
69. [Endoscopic diagnosis and management of esophagogastric](https://www.esge.com/assets/downloads/pdfs/guidelines/2022_a-1939-4887.pdf)
70. [Early TIPS in cirrhosis and variceal bleeding \[Classics Series\]](https://www.2minutemedicine.com/early-tips-in-cirrhosis-and-variceal-bleeding-classics-series/)
