# 第66回 成果物（ブラッシュアップA：感染症（Ⅻ）と呼吸器（Ⅳ））

- 依頼文：docs/tasks/round62_BRUSHUP_A.md の「第66回」（仕様 specs/round66.yaml）
- 対象：20項目（すべてレベル a）
- 件数：20件（VI-033、CM-008〜009、BA-047〜052、RI-058〜059、RO-042〜044、IL-062、PV-032、LC-055、PL-031〜033）、各項目1件
- 新規出典：15件（SRC-4881〜4895）。未使用：SRC-4896〜4960
- 既存カードは直さず、各項目に依頼文の表の「2件目に書く側面」の新しいカードを足した

## 判断・申し送り（要点）

- BA-052（ガス壊疽）は登録時の決定どおり病原性（α毒素）と病変組織の所見に限った（臨床像・治療は SD-034 が担う）。細菌学的検査所見（グラム染色・培養）は採用出典の範囲外で未カバー
- BA-050（緑膿菌感染症）で依頼表に挙がっていた悪性外耳道炎は、採用出典に記述がなく未収載（別出典での追加の余地あり）
- VI-033（ウイルス性髄膜炎）は出典本文が購読制のため、抄録と出版社ハイライトで確認できた範囲に限定した（アシクロビルの先行投与と「多くは予後良好」の経過は未確認のため入れていない）
- CM と BA の開始番号は仕様で null のため、第64回で使用済みの続き（CM-008・BA-047）からとした
- PL-032（気管食道瘻）は依頼文の見込み（ESGE 2021）が悪性瘻のステント推奨中心だったため、後天性の原因・症状・診断・治療を1文献で確認できる総説（SRC-4894）に切り替えた

## 1. 出典ホワイトリスト（この回のカードが使う出典）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-350 | 厚生労働省健康・生活衛生局感染症対策部感染症対策課. 抗微生物薬適正使用の手引き 第三版（2023年） | null | null | 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ | GOV_JP | 既存カード RI-001 の出典（出典マスター登録済み）。手引き本文 PDF を開き、感冒の定義・原因ウイルス・4病型の鑑別・インフルエンザとの区別を確認 |
| SRC-370 | Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156 | 10.1136/thorax-2023-220304 | null | © Author(s) (or their employer(s)) 2023. No commercial re-use（論文 PDF の表示） | RESTRICTED | 既存カード RI-052 の出典（出典マスター登録済み）。学会のガイドライン要約・付録ページで、片側胸水の診断の進め方と再考すべき原因を確認 |
| SRC-378 | Chalmers JD, Haworth CS, Flume P, et al. European Respiratory Society Clinical Practice Guideline for the Management of Adult Bronchiectasis (2025) | 10.1183/13993003.01126-2025 | null | 未確認 | UNKNOWN | 既存カード RO-028 の出典（出典マスター登録済み）。ERJ のガイドライン本文ページと学会の臨床サマリーで、定義・診断・原因検索の内容を確認 |
| SRC-444 | Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Respir J 2023;61(1):2200879 | 10.1183/13993003.00879-2022 | 36028254 | Publisher holds Copyright（ERS、リポジトリの表示） | RESTRICTED | 既存出典（出典マスター登録済み。第66回で再利用） |
| SRC-2081 | Burillo A, Bouza E. Chlamydophila pneumoniae. Infect Dis Clin North Am. 2010;24(1):61-71 | 10.1016/j.idc.2009.10.002 | 20171546 | CC表示なし | RESTRICTED | 既存登録（CM-001 の出典）。2026-11-01 に PubMed 抄録を再確認 |
| SRC-4881 | Wright WF, Pinto CN, Palisoc K, Baghli S. Viral (aseptic) meningitis: A review. J Neurol Sci. 2019;398:176-183 | 10.1016/j.jns.2019.01.050 | 30731305 | CC表示なし | RESTRICTED | 2026-11-01 に PubMed 抄録と出版社ページ（ハイライト）で確認。本文は購読制 |
| SRC-4882 | Waites KB, Xiao L, Liu Y, Balish MF, Atkinson TP. Mycoplasma pneumoniae from the Respiratory Tract and Beyond. Clin Microbiol Rev. 2017;30(3):747-809 | 10.1128/CMR.00114-16 | 28539503 | American Society for Microbiology（CC 表示なし） | RESTRICTED | 2026-11-01 に PMC 本文で確認（PMCID: PMC5475226） |
| SRC-4883 | Mermel LA, Allon M, Bouza E, Craven DE, Flynn P, O'Grady NP, Raad II, Rijnders BJ, Sherertz RJ, Warren DK. Clinical practice guidelines for the diagnosis and management of intravascular catheter-related infection: 2009 Update by the Infectious Diseases Society of America. Clin Infect Dis. 2009;49(1):1-45 | 10.1086/599376 | 19489710 | Infectious Diseases Society of America（CC 表示なし） | RESTRICTED | 2026-11-01 に PMC 本文で確認（PMCID: PMC4039170） |
| SRC-4884 | Russo TA, Marr CM. Hypervirulent Klebsiella pneumoniae. Clin Microbiol Rev. 2019;32(3):e00001-19 | 10.1128/CMR.00001-19 | 31092506 | American Society for Microbiology（CC 表示なし） | RESTRICTED | 2026-11-01 に PMC 本文（表1を含む）で確認（PMCID: PMC6589860） |
| SRC-4885 | Mahlen SD. Serratia infections: from military experiments to current practice. Clin Microbiol Rev. 2011;24(4):755-791 | 10.1128/CMR.00017-11 | 21976608 | © American Society for Microbiology（PMC 収載版の版権表示で確認） | RESTRICTED | PubMed レコードと PMC 全文（PMC3194826）を開いて書誌・識別子・本文（内因性耐性、AmpC、治療）を確認。出典マスターに DOI・PMID とも未登録 |
| SRC-4886 | Bassetti M, Vena A, Croxatto A, Righi E, Guery B. How to manage Pseudomonas aeruginosa infections. Drugs Context. 2018;7:212527 | 10.7573/dic.212527 | 29872449 | CC BY-NC-ND 4.0（PMC 収載版の表示で確認） | RESTRICTED | PubMed レコードと PMC 全文（PMC5978525）を開いて書誌・識別子・本文（臨床像、壊疽性膿瘡、熱傷創部感染、抗緑膿菌薬の分類と新規薬）を確認。出典マスターに DOI・PMID とも未登録 |
| SRC-4887 | Wong D, Nielsen TB, Bonomo RA, Pantapalangkoor P, Luna B, Spellberg B. Clinical and pathophysiological overview of Acinetobacter infections: a century of challenges. Clin Microbiol Rev. 2017;30(1):409-447 | 10.1128/CMR.00058-16 | 27974412 | © American Society for Microbiology（PMC 収載版の版権表示で確認） | RESTRICTED | PubMed レコードと PMC 全文（PMC5217799）を開いて書誌・識別子・本文（臨床像、環境での長期生存と伝播、治療とスルバクタムの位置づけ）を確認。出典マスターに DOI・PMID とも未登録 |
| SRC-4888 | Uzal FA, Freedman JC, Shrestha A, Theoret JR, Garcia J, Awad MM, Adams V, Moore RJ, Rood JI, McClane BA. Towards an understanding of the role of Clostridium perfringens toxins in human and animal disease. Future Microbiol. 2014;9(3):361-377 | 10.2217/fmb.13.168 | 24762309 | © 2014 Future Medicine Ltd（PMC 収載の著者原稿の表示で確認） | RESTRICTED | PubMed レコードと PMC 全文（PMC4155746、著者原稿）を開いて書誌・識別子・本文（α毒素の必須性、両毒素の作用、病変組織所見）を確認。出典マスターに DOI・PMID とも未登録 |
| SRC-4889 | Ryu JH, Myers JL, Swensen SJ. Bronchiolar disorders. Am J Respir Crit Care Med. 2003;168(11):1277-1292 | 10.1164/rccm.200301-053SO | 14644923 | CC 表示なし（購読誌） | RESTRICTED | 論文 PDF の書誌情報と PubMed の紹介記録で DOI・PMID を照合して確認。出典マスターに DOI・PMID とも登録がないことを確認。狭窄性細気管支炎の原因・HRCT 所見・経過の記述を本文で確認 |
| SRC-4890 | Hallifax R. Aetiology of Primary Spontaneous Pneumothorax. J Clin Med. 2022;11(3):490 | 10.3390/jcm11030490 | 35159942 | CC BY 4.0（論文と PMC ページの表示） | OPEN | PMC の全文（PMC8836443）を開き、ブレブとブラの定義（2.4節）と原発性自然気胸との関係を確認。出典マスターに DOI・PMID とも登録がないことを確認 |
| SRC-4891 | Suzuki Y, Suda T. Eosinophilic pneumonia: A review of the previous literature, causes, diagnosis, and management. Allergol Int. 2019;68(4):413-419 | 10.1016/j.alit.2019.05.006 | null | CC BY-NC-ND 4.0（論文の表示） | RESTRICTED | J-STAGE の全文 PDF を開き、急性・慢性の臨床像・診断・治療とライセンス表示を確認。出典マスターに DOI の登録がないことを確認。PMID は確認できなかったため null |
| SRC-4892 | Hutchinson CB, Wang E. Primary mediastinal (thymic) large B-cell lymphoma: a short review with brief discussion of mediastinal gray zone lymphoma. Arch Pathol Lab Med. 2011;135(3):394-398 | 10.5858/2009-0463-RSR.1 | 21366467 | College of American Pathologists（Archives of Pathology & Laboratory Medicine、CC 表示なし） | RESTRICTED | PubMed レコードで書誌・PMID・DOI・抄録（DLBCL の亜型、前縦隔上部の大きな腫瘤、局所浸潤・圧迫症状、結節硬化型古典的 Hodgkin リンパ腫との鑑別とグレイゾーンリンパ腫）を確認。DOI は他論文の参考文献表記とも一致。若年発症・女性優位・圧迫症状の内訳は総説本文に基づく |
| SRC-4893 | Kouritas VK, Papagiannopoulos K, Lazaridis G, et al. Pneumomediastinum. J Thorac Dis. 2015;7(Suppl 1):S44-S49 | 10.3978/j.issn.2072-1439.2015.01.11 | 25774307 | © 2015 Journal of Thoracic Disease. All rights reserved（PMC 掲載ページの表示、CC 表示なし） | RESTRICTED | PMC 全文で書誌・PMCID（PMC4332083）・Macklin 効果の機序・症状頻度（胸痛60〜100%、呼吸困難75%、咳嗽80%、頸部痛36%）・皮下気腫の合併（70%）・Hamman 徴候・保存的治療の内容を確認 |
| SRC-4894 | Kim HS, Khemasuwan D, Diaz-Mendoza J, Mehta AC. Management of tracheo-oesophageal fistula in adults. Eur Respir Rev. 2020;29(158):200094 | 10.1183/16000617.0094-2020 | 33153989 | CC BY-NC 4.0（PMC 掲載ページで確認） | RESTRICTED | PMC 全文で書誌・PMCID（PMC9488631）・後天性の原因内訳（悪性と良性がほぼ半々、悪性は食道癌が最多、良性はカフ圧迫壊死が中心で約75%が医原性）・症状頻度と Ono 徴候・造影と内視鏡による診断・ステントと手術の位置づけ・ライセンス表示を確認 |
| SRC-4895 | Wang HW, Lu CC, Chao PZ, Lee FP. Causes of Vocal Fold Paralysis. Ear Nose Throat J. 2022;101(7):NP294-NP298 | 10.1177/0145561320965212 | （未確認のため null） | 未確認（誌面・PDF で CC 表示を確認できず。© The Author(s) 2020、再利用は出版社の許可手続きによる旨の表示あり） | UNKNOWN | 出版者ページの全文で、一側性声帯麻痺の左右差（左122例69%・右56例31%）・左反回神経の長い走行と大動脈弓との関係・原因割合（手術61.3%、腫瘍性17.5%で肺癌が最多、心血管性2%）を確認。PMID は確認できず null とした |

## 2. 事実カード（YAML）

```yaml
- id: VI-033
  domain: VI
  subdomain: ウイルス性髄膜炎
  assertion:
    plain_statement_ja: ウイルス性髄膜炎は、髄膜の炎症に急性の髄膜症状と発熱を伴い、髄液の細胞増多を認めるが通常の細菌培養では菌が発育しない病態である。原因ウイルスは年齢や地域で異なり、非ポリオエンテロウイルスが最も多く、ムンプスウイルス、リンパ球性脈絡髄膜炎ウイルス、ヘルペスウイルス属などが知られる。髄液の核酸増幅検査の導入で病原体の検出が進み、不必要な抗菌薬投与や入院の削減につながっている。特異的治療のないウイルスが多く、治療の中心は支持療法であり、原因の一部はワクチンで予防できる。
    condition:
      region: 国際
      対象: 一般
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4881
    source: 'Wright WF, Pinto CN, Palisoc K, Baghli S. Viral (aseptic) meningitis: A review. J Neurol Sci. 2019;398:176-183'
    doi: 10.1016/j.jns.2019.01.050
    pmid: '30731305'
    pmcid: null
    url: https://doi.org/10.1016/j.jns.2019.01.050
    source_license: CC表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本文は購読制のため、主張は抄録と出版社ページのハイライトで確認できた範囲に限った。ヘルペスウイルスが否定できない場合の抗ウイルス薬の扱いや予後の具体的数値は確認範囲に含まれないため主張に入れていない。髄液所見の型と細菌性髄膜炎との対比は既存カード NI-008 が担う。
  curriculum:
    kokushi: 医学各論 Ⅻ-1-A-⑱（ウイルス性髄膜炎、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: CM-008
  domain: CM
  subdomain: クラミジア肺炎
  assertion:
    plain_statement_ja: Chlamydophila pneumoniae 感染症の診断は、鼻咽頭検体の培養、血清抗体価の測定、分子生物学的手法によるが、結果は発症や治療開始の時点から遅れて得られることが多く、正確で標準化された迅速診断法は確立していない。治療の第一選択はエリスロマイシン、テトラサイクリン、ドキシサイクリンであり、北米のガイドラインは急性の C. pneumoniae 呼吸器感染症への抗菌薬治療を推奨している。ただし非定型病原体による市中肺炎への治療が転帰を改善するかについては否定的な報告もある。
    condition:
      region: 国際
      対象: 一般
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2081
    source: Burillo A, Bouza E. Chlamydophila pneumoniae. Infect Dis Clin North Am. 2010;24(1):61-71
    doi: 10.1016/j.idc.2009.10.002
    pmid: '20171546'
    pmcid: null
    url: https://doi.org/10.1016/j.idc.2009.10.002
    source_license: CC表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: エリスロマイシン、テトラサイクリン、ドキシサイクリンはいずれも国内で承認された抗菌薬である。ドキシサイクリンは国内の添付文書でクラミジア属を適応菌種に含み肺炎への適応があることを PMDA の資料で確認した。他の2剤の適応菌種の範囲は製剤ごとの添付文書による。出典は2010年の総説で、主張は抄録で確認した範囲に限った。集団発生の側面は抄録では確認できず、主張に入れていない。
  curriculum:
    kokushi: 医学各論 Ⅻ-2-A-①（クラミジア肺炎、a）
    core_curriculum: 'PS-01-03-06 (id: JkxnuLQ)；PS-03-03-01 (id: JkxnuUg)；TBL-01-00-592 (id: JlvnmXc)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: CM-009
  domain: CM
  subdomain: マイコプラズマ肺炎
  assertion:
    plain_statement_ja: 肺炎マイコプラズマ感染症は学童期から青年期に多く、最も多い病像は気管気管支炎で、乾性咳嗽や粘液性の痰を伴う咳嗽が数週間にわたり遷延することが特徴である。潜伏期は約3週間と長く、家庭内など濃厚接触の場で緩やかに広がる。中枢神経系をはじめとする肺外症状を伴うことがある。診断は核酸増幅検査が中心的な方法で、血清診断では発症後2週間以上あけて採取したペア血清で4倍以上の抗体価上昇が最も確実であり、単一検体では偽陰性・偽陽性がありうる。治療はマクロライド系抗菌薬が第一選択で、マクロライド耐性や無効例ではテトラサイクリン系（ミノサイクリン、ドキシサイクリン）やフルオロキノロン系（レボフロキサシンなど）が代替薬となる。
    condition:
      region: 国際
      対象: 一般
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4882
    source: Waites KB, Xiao L, Liu Y, Balish MF, Atkinson TP. Mycoplasma pneumoniae from the Respiratory Tract and Beyond. Clin Microbiol Rev. 2017;30(3):747-809
    doi: 10.1128/CMR.00114-16
    pmid: '28539503'
    pmcid: PMC5475226
    url: https://doi.org/10.1128/CMR.00114-16
    source_license: American Society for Microbiology（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ミノサイクリンとレボフロキサシンは、国内の添付文書で肺炎マイコプラズマ（マイコプラズマ・ニューモニエ）を適応菌種に含み肺炎への適応があることを PMDA の添付文書で確認した。同じテトラサイクリン系でもドキシサイクリンは国内の添付文書の適応菌種にマイコプラズマを含まないため、本症への使用は適応外となる。マクロライド耐性率は地域と時期で大きく異なり、日本の耐性率の推移そのものは既存カード CM-002 が担う。
  curriculum:
    kokushi: 医学各論 Ⅻ-2-A-③（マイコプラズマ肺炎、a）
    core_curriculum: 'PS-01-03-06 (id: JkxnuLQ)；PS-03-03-04 (id: JkxnuUs)；TBL-01-00-592 (id: JlvnmXc)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BA-047
  domain: BA
  subdomain: 表皮ブドウ球菌感染症
  assertion:
    plain_statement_ja: コアグラーゼ陰性ブドウ球菌はカテーテル関連血流感染の最も多い原因菌であると同時に、血液培養で最も多いコンタミネーションの原因でもあるため、陽性となった場合の解釈が重要になる。血液培養が1セットのみ陽性の場合は、抗菌薬の開始やカテーテル抜去の前に、カテーテル採血と末梢静脈採血による追加培養で真の血流感染かどうかを確認する。カテーテル関連血流感染の確定診断には、末梢血培養とカテーテル先端培養で同一菌が発育すること、またはカテーテル採血の培養陽性化が末梢血より2時間以上早いこと（陽性化時間差）などが用いられる。本菌の多くはメチシリン耐性であり、経験的治療にはバンコマイシンが推奨される。合併症のない例では、カテーテルを抜去した場合は5〜7日間、温存する場合は抗菌薬ロック療法を併用して10〜14日間の治療を行い、感染性心内膜炎、化膿性血栓性静脈炎、適切な治療でも72時間を超えて持続する菌血症がある場合はカテーテルを抜去する。
    condition:
      region: 国際
      対象: 血管内カテーテル留置患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4883
    source: 'Mermel LA, Allon M, Bouza E, Craven DE, Flynn P, O''Grady NP, Raad II, Rijnders BJ, Sherertz RJ, Warren DK. Clinical practice guidelines for the diagnosis and management of intravascular catheter-related infection: 2009 Update by the Infectious Diseases Society of America. Clin Infect Dis. 2009;49(1):1-45'
    doi: 10.1086/599376
    pmid: '19489710'
    pmcid: PMC4039170
    url: https://doi.org/10.1086/599376
    source_license: Infectious Diseases Society of America（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: バンコマイシンは国内で承認されており、添付文書の適応菌種にメチシリン耐性コアグラーゼ陰性ブドウ球菌（MRCNS）を含み、敗血症や感染性心内膜炎などへの保険適用があることを PMDA の添付文書で確認した。出典は IDSA の2009年ガイドラインで、人工物感染としては血管内デバイスを中心に扱っており、人工関節・人工弁など他のデバイス感染の診断・治療の詳細は対象外のため主張に含めていない。なお同ガイドラインでは Staphylococcus lugdunensis は黄色ブドウ球菌と同様に扱うとしている。
  curriculum:
    kokushi: 医学各論 Ⅻ-2-B-⑤（表皮ブドウ球菌感染症、a）
    core_curriculum: 'PS-01-03-04 (id: JkxnuLI)；PS-03-03-02 (id: JkxnuUk)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BA-048
  domain: BA
  subdomain: クレブシエラ感染症
  assertion:
    plain_statement_ja: クレブシエラ・ニューモニエの古典株は主に医療機関で、基礎疾患や免疫抑制のある患者、体内デバイスの留置や手術創などバリアの破綻がある患者に感染を起こす日和見病原体である。一方、過毒力株はアジア太平洋地域に多く、基礎疾患のない人にも市中感染を起こし、胆道疾患のない肝膿瘍を代表的な病像として、複数部位への播種や眼内炎・髄膜炎などの転移性感染を来すことがある。糖尿病は過毒力株感染の危険因子とされ、血糖管理不良は転移性合併症の増加と関連する。治療は感受性結果が判明するまでは効果が予測できる抗菌薬を経験的に選び、判明後に狭域化すること、膿瘍ではドレナージなどのソースコントロールを併用することが原則である。ESBL 産生株は第3世代セフェムなどに耐性を示し、カルバペネマーゼ産生株はカルバペネムを含む広範な β-ラクタムに耐性を示す。カルバペネマーゼ産生株に対してはセフタジジム・アビバクタム、コリスチン、チゲサイクリンが試験管内で活性を示すが、メタロ-β-ラクタマーゼ産生株はセフタジジム・アビバクタムの対象外である。
    condition:
      region: 国際
      対象: 一般
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4884
    source: Russo TA, Marr CM. Hypervirulent Klebsiella pneumoniae. Clin Microbiol Rev. 2019;32(3):e00001-19
    doi: 10.1128/CMR.00001-19
    pmid: '31092506'
    pmcid: PMC6589860
    url: https://doi.org/10.1128/CMR.00001-19
    source_license: American Society for Microbiology（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: セフタジジム・アビバクタム（ザビセフタ）は2024年6月に国内で製造販売承認され、カルバペネム耐性腸内細菌目細菌による感染症に用いられるが、メタロ-β-ラクタマーゼ産生株には有効でなく、国内で最も多い IMP 型の産生株ではアズトレオナムとの併用が推奨されていることを厚生労働省の通知で確認した。コリスチンとチゲサイクリンも国内で承認されているが、多剤耐性菌による感染症への使用には適正使用上の制約がある。過毒力株の治療には対照試験がなく、治療の考え方は出典の総説が示す経験的な原則に拠った。
  curriculum:
    kokushi: 医学各論 Ⅻ-2-B-⑭（クレブシエラ感染症、a）
    core_curriculum: 'PS-03-03-02 (id: JkxnuUk)；PS-03-03-04 (id: JkxnuUs)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BA-049
  domain: BA
  subdomain: セラチア感染症
  assertion:
    plain_statement_ja: セラチア感染症は成人では主として医療関連感染としてみられ、尿路感染症、肺炎、血流感染などを起こし、院内アウトブレイクの原因にもなる。Serratia marcescens はペニシリンG、アンピシリン、アモキシシリン・クラブラン酸、セフロキシムを含む狭域のセファロスポリン、コリスチン、ニトロフラントインに内因性耐性を示す。染色体性の誘導型 AmpC 型β-ラクタマーゼを持つため、第3世代セファロスポリンによる治療中に脱抑制変異株が出現して耐性化することがあり、治療は感受性結果に応じて調整する。経験的治療にはピペラシリン・タゾバクタム、フルオロキノロン系薬、アミノグリコシド系薬、カルバペネム系薬などが用いられ、カルバペネム系薬には原則として感性を示す（カルバペネマーゼ産生株の報告はある）。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4885
    source: 'Mahlen SD. Serratia infections: from military experiments to current practice. Clin Microbiol Rev. 2011;24(4):755-791.'
    doi: 10.1128/CMR.00017-11
    pmid: '21976608'
    pmcid: PMC3194826
    url: https://doi.org/10.1128/CMR.00017-11
    source_license: © American Society for Microbiology（PMC 収載版の版権表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤の国内承認：ピペラシリン・タゾバクタム、フルオロキノロン系薬（シプロフロキサシン、レボフロキサシン）、アミノグリコシド系薬（アミカシンなど）、カルバペネム系薬（メロペネム、イミペネム・シラスタチン）はいずれも国内承認薬である。コリスチン（コリスチンメタンスルホン酸ナトリウム、販売名オルドレブ）は2015年に国内承認されたが、セラチア属は添付文書上も抗菌活性を示さない菌種とされており、本菌感染症の治療薬にはならない。
  curriculum:
    kokushi: 医学各論 Ⅻ-2-B-⑮（セラチア感染症、a）
    core_curriculum: 'PS-01-03-04 (id: JkxnuLI)；PS-03-03-02 (id: JkxnuUk)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BA-050
  domain: BA
  subdomain: 緑膿菌感染症
  assertion:
    plain_statement_ja: 緑膿菌は、重症患者や免疫不全患者における院内感染の主要な原因菌の一つである。臨床像は菌血症、肺炎（人工呼吸器関連肺炎を含む）、尿路感染症、皮膚・軟部組織感染症など多様で、好中球減少患者の菌血症では壊疽性膿瘡（皮膚の壊死性病変）を伴うことがある。熱傷創部感染では、感受性が判明するまで抗緑膿菌薬の経験的併用療法を行い、デブリードマンが適応となる場合がある。治療は、ピペラシリン・タゾバクタム、セフタジジム、セフエピム、カルバペネム系薬、アズトレオナムなどのβ-ラクタム系薬、シプロフロキサシンやレボフロキサシンなどのフルオロキノロン系薬、アミノグリコシド系薬の中から感受性に応じて選択し、重症例では併用療法が検討される。薬剤耐性株に対してはセフトロザン・タゾバクタムやセフタジジム・アビバクタムが選択肢となる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4886
    source: Bassetti M, Vena A, Croxatto A, Righi E, Guery B. How to manage Pseudomonas aeruginosa infections. Drugs Context. 2018;7:212527.
    doi: 10.7573/dic.212527
    pmid: '29872449'
    pmcid: PMC5978525
    url: https://doi.org/10.7573/dic.212527
    source_license: CC BY-NC-ND 4.0（PMC 収載版の表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 依頼表で臨床像に挙げられた悪性外耳道炎は本出典では扱われておらず、本カードには含めていない。薬剤の国内承認：ピペラシリン・タゾバクタム、セフタジジム、セフエピム、イミペネム・シラスタチン、メロペネム、シプロフロキサシン、レボフロキサシン、アズトレオナム、アミノグリコシド系薬（トブラマイシン、アミカシンなど）はいずれも国内承認薬である。セフトロザン・タゾバクタム（販売名ザバクサ）は2019年に国内承認され、適応菌種に緑膿菌を含む。セフタジジム・アビバクタム（販売名ザビセフタ）は2024年6月に国内承認された（カルバペネム耐性菌感染症を中心に適正使用を求める通知がある）。コリスチン（販売名オルドレブ）は2015年に国内承認され適応菌種に緑膿菌を含むが、他の抗菌薬に耐性を示した菌株に限られる。
  curriculum:
    kokushi: 医学各論 Ⅻ-2-B-⑱（緑膿菌感染症、a）
    core_curriculum: 'PS-03-03-02 (id: JkxnuUk)；PS-03-03-04 (id: JkxnuUs)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BA-051
  domain: BA
  subdomain: アシネトバクター感染症
  assertion:
    plain_statement_ja: アシネトバクター感染症は主として院内感染であり、誤嚥性肺炎（人工呼吸器関連肺炎を含む）とカテーテル関連血流感染が代表的で、皮膚軟部組織感染や尿路感染症も起こす。集中治療室での発生が多く、本菌は乾燥に強く環境表面で長期間生存するため、環境表面や医療従事者の手指を介した伝播によりアウトブレイクの原因となる。広範囲薬剤耐性株による感染では死亡率が高く、有効な抗菌薬による初期治療が予後を左右する。治療では、スルバクタムが本菌に対して直接の抗菌活性を持つことを踏まえ、カルバペネム系薬やスルバクタムを軸とする併用療法が検討され、コリスチン、チゲサイクリン、ミノサイクリンなどが代替の選択肢となる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4887
    source: 'Wong D, Nielsen TB, Bonomo RA, Pantapalangkoor P, Luna B, Spellberg B. Clinical and pathophysiological overview of Acinetobacter infections: a century of challenges. Clin Microbiol Rev. 2017;30(1):409-447.'
    doi: 10.1128/CMR.00058-16
    pmid: '27974412'
    pmcid: PMC5217799
    url: https://doi.org/10.1128/CMR.00058-16
    source_license: © American Society for Microbiology（PMC 収載版の版権表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本出典は2017年の総説であり、スルバクタム・デュロバクタムなどの新しい配合剤は扱われていない。薬剤の国内承認：メロペネム、イミペネム・シラスタチン、ミノサイクリンは国内承認薬である。スルバクタムは国内ではアンピシリンとの配合剤（販売名ユナシン-Sなど）として承認されているが、適応菌種にアシネトバクター属は含まれず、本菌感染症への使用は適応外となる。コリスチン（販売名オルドレブ）は2015年に国内承認され、適応菌種にアシネトバクター属を含むが、他の抗菌薬に耐性を示した菌株に限られる。チゲサイクリン（販売名タイガシル）は2012年に国内承認され、適応菌種にアシネトバクター属を含むが、他の抗菌薬に耐性を示した菌株に限られ、適応症は深在性皮膚感染症や腹腔内感染症などである。
  curriculum:
    kokushi: 医学各論 Ⅻ-2-B-⑲（アシネトバクター感染症、a）
    core_curriculum: 'PS-03-03-02 (id: JkxnuUk)；PS-03-03-04 (id: JkxnuUs)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: BA-052
  domain: BA
  subdomain: ガス壊疽
  assertion:
    plain_statement_ja: ウェルシュ菌（Clostridium perfringens）A型によるガス壊疽（クロストリジウム性筋壊死）の病原性の中心は、染色体にコードされるα毒素とパーフリンゴリジンOである。α毒素はホスホリパーゼCとスフィンゴミエリナーゼの活性を持つ酵素で、α毒素を欠く変異株は筋壊死を起こさないことから、筋壊死の成立に必須の毒素である。α毒素の作用により組織壊死と血栓形成が生じ、感染部位への多形核白血球の浸潤が欠如する。パーフリンゴリジンOは単独では必須ではないが、α毒素と協調して白血球の血管内停留を来し、血流を障害して壊死の進展に関与する。病変組織の顕微鏡所見では、筋線維の壊死と、好中球が血管内に停留する一方で血管外の組織への浸潤が乏しい像がみられる。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4888
    source: Uzal FA, Freedman JC, Shrestha A, Theoret JR, Garcia J, Awad MM, Adams V, Moore RJ, Rood JI, McClane BA. Towards an understanding of the role of Clostridium perfringens toxins in human and animal disease. Future Microbiol. 2014;9(3):361-377.
    doi: 10.2217/fmb.13.168
    pmid: '24762309'
    pmcid: PMC4155746
    url: https://doi.org/10.2217/fmb.13.168
    source_license: © 2014 Future Medicine Ltd（PMC 収載の著者原稿の表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 臨床像・治療は SD-034 が担うため本カードでは扱わない（登録時の決定による）。検査所見として収載したのは病変組織の顕微鏡所見の範囲であり、創部滲出液のグラム染色や培養などの細菌学的検査所見は本出典では扱われていない。出典の PMC 収載版は著者原稿で、版元版は Future Microbiology 誌の掲載版である。
  curriculum:
    kokushi: 医学各論 Ⅻ-2-B-⑳（ガス壊疽、a）
    core_curriculum: 'PS-01-03-03 (id: JkxnuLE)；TBL-01-00-595 (id: JlvnmXw)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: RI-058
  domain: RI
  subdomain: 感冒<かぜ症候群>、上気道炎
  assertion:
    plain_statement_ja: 感冒（かぜ症候群）は、鼻症状・咽頭症状・下気道症状の3系統の症状が同時に、同程度に存在するウイルス性の急性気道感染症で、非特異的上気道炎・普通感冒と同義である。厚生労働省の手引きによれば、急性気道感染症の原因微生物の約9割はライノウイルスやコロナウイルスなどのウイルスである。同手引きは急性気道感染症を感冒・急性鼻副鼻腔炎・急性咽頭炎・急性気管支炎の4病型に分けて鑑別する枠組みを示し、インフルエンザは全身症状が比較的強く、発症後早期から咳が多い点で感冒と区別される。感冒の治療は対症療法が中心である。
    condition:
      region: 日本
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-350
    source: 厚生労働省健康・生活衛生局感染症対策部感染症対策課. 抗微生物薬適正使用の手引き 第三版（2023年）
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10900000/001169116.pdf
    source_license: 政府標準利用規約（第2.0版）に準拠する厚生労働省のコンテンツ
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 対症療法に用いる解熱鎮痛薬（アセトアミノフェン等）は、国内で解熱・鎮痛の効能・効果で承認されている。手引きは感冒に使われる対症療法薬の多くで有効性の根拠が限られる点にも触れており、個別の薬剤の推奨は主張に含めていない。既存の RI-001 が経過と「感冒に抗菌薬を投与しない」推奨を担うため、本カードは定義・原因・鑑別と治療の位置づけに絞った
  curriculum:
    kokushi: 医学各論 Ⅳ-1-A-①（感冒<かぜ症候群>、上気道炎、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-204 (id: JlvnlxA)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: RI-059
  domain: RI
  subdomain: 胸膜炎
  assertion:
    plain_statement_ja: 胸水を来す原因は多岐にわたり、感染（肺炎随伴性・結核性など）、悪性腫瘍、心不全、肺塞栓などが代表的である。英国胸部学会（BTS）の2023年ガイドラインが示す片側胸水の診断の進め方では、注意深い病歴聴取と身体診察が最も重要な第一歩とされ、胸部X線と胸部超音波による評価に続いて診断のための胸腔穿刺を行う。さらに胸膜の評価を含む造影CTを行い、それでも原因が判明しない場合は画像ガイド下の胸膜生検や胸腔鏡検査を検討する。原因が分からない場合は、肺塞栓・結核・慢性心不全・リンパ腫など治療可能な原因を見落としていないか再考することが求められる。
    condition:
      region: 英国
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-370
    source: Roberts ME, Rahman NM, Maskell NA, et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78:1143-1156
    doi: 10.1136/thorax-2023-220304
    pmid: null
    pmcid: null
    url: https://thorax.bmj.com/content/78/11/1143
    source_license: © Author(s) (or their employer(s)) 2023. No commercial re-use（論文 PDF の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原因・病型の代表例と診断の進め方に絞った。胸水の漏出性・滲出性の判定（Light の基準）は症候側の既存カード RX-003 が、肺炎随伴性胸水・胸膜感染症のドレナージの閾値は既存の RI-052 が担う。結核性胸膜炎に特化した診断（胸水中の ADA 測定など）は、本ガイドラインで確認した範囲には含まれないため主張に入れていない
  curriculum:
    kokushi: 医学各論 Ⅳ-1-G-①（胸膜炎、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-213 (id: Jlvnlx4)；TBL-01-00-240 (id: Jlvnl08)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: RO-042
  domain: RO
  subdomain: 気管支拡張症
  assertion:
    plain_statement_ja: 気管支拡張症は、気管支の永続的な拡張と、それに伴う特徴的な臨床症候群によって定義され、診断は高分解能CTで拡張した気管支を確認することによる。背景となる病態は幅広く、感染、免疫異常、自己免疫・アレルギー性の病態、遺伝性疾患などが関わりうる。欧州呼吸器学会（ERS）の2025年ガイドラインは、新規に診断されたすべての患者について、血清免疫グロブリン（IgG・IgM・IgA）の測定による免疫不全の検索、アレルギー性気管支肺アスペルギルス症の検索（総IgE、アスペルギルス特異的IgG・IgE、血中好酸球数）、非結核性抗酸菌の検索（抗酸菌の顕微鏡検査と培養）を行うことを示している。
    condition:
      region: 欧州
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-378
    source: Chalmers JD, Haworth CS, Flume P, et al. European Respiratory Society Clinical Practice Guideline for the Management of Adult Bronchiectasis (2025)
    doi: 10.1183/13993003.01126-2025
    pmid: null
    pmcid: null
    url: https://dzl.de/guidelines/european-respiratory-society-clinical-practice-guideline-for-the-management-of-adult-bronchiectasis/
    source_license: 未確認
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 定義・原因・診断に絞り、治療の推奨は既存の RO-028 が担う。内容は ERJ のガイドライン本文ページと学会の臨床サマリーで確認した。特発性の症例が占める割合などの数値は二次的な解説で見られたものであるため、主張に含めていない。出典のライセンス表示は既存登録（SRC-378）のとおり未確認である
  curriculum:
    kokushi: 医学各論 Ⅳ-2-A-①（気管支拡張症、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-234 (id: Jlvnl0U)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: RO-043
  domain: RO
  subdomain: 閉塞性細気管支炎
  assertion:
    plain_statement_ja: 閉塞性細気管支炎（狭窄性細気管支炎）は、細気管支の線維化による狭窄・閉塞で閉塞性換気障害を来す病態である。原因は多様で、有毒ガスの吸入（二酸化窒素によるサイロ充填者肺が古典的とされる）、薬剤、呼吸器感染の後遺症（アデノウイルス感染後など）、膠原病、同種造血幹細胞移植や肺移植後の合併症（閉塞性細気管支炎症候群）などがある。進行性の呼吸困難と咳嗽を呈し、胸部X線は正常か非特異的な所見にとどまることが多い。診断では呼気相の高分解能CTが重要で、モザイク状の低吸収域と血管影の減少、呼気相で強調されるエアトラッピングが特徴的である。多くの場合、副腎皮質ステロイドへの反応に乏しく進行性で、気流制限が進めば呼吸不全に至る。移植後の症例では免疫抑制の増強がしばしば無効で、再移植の検討が必要になることがある。
    condition:
      region: null
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4889
    source: Ryu JH, Myers JL, Swensen SJ. Bronchiolar disorders. Am J Respir Crit Care Med. 2003;168(11):1277-1292
    doi: 10.1164/rccm.200301-053SO
    pmid: '14644923'
    pmcid: null
    url: https://doi.org/10.1164/rccm.200301-053SO
    source_license: CC 表示なし（購読誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 原因は分類の水準で記し、個別の薬剤名は主張に入れていない。副腎皮質ステロイドと免疫抑制薬への言及は、国内で承認のある薬剤の分類名による経過・反応性の記述であり、治療の推奨ではない。既存の RO-031 は用語集による定義のみで原因別の記述を含まないため、本カードは総説に基づき原因・病像・診断・経過を補う
  curriculum:
    kokushi: 医学各論 Ⅳ-2-A-③（閉塞性細気管支炎、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: RO-044
  domain: RO
  subdomain: 気腫性囊胞<ブラ、ブレブ>
  assertion:
    plain_statement_ja: ブレブは、臓側胸膜の内・外弾性板の間に空気が入って生じる胸膜の膨らみで、通常は直径1 cm未満である。ブラは、壁の厚さが1 mm以下の薄い壁で明瞭に境された、直径1 cmを超える含気腔である。原発性自然気胸は、既知の肺疾患のない若年者に典型的に起こり、胸膜直下のブレブやブラの破裂によって空気が胸腔内に漏れることが原因と考えられている。
    condition:
      region: null
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4890
    source: Hallifax R. Aetiology of Primary Spontaneous Pneumothorax. J Clin Med. 2022;11(3):490
    doi: 10.3390/jcm11030490
    pmid: '35159942'
    pmcid: PMC8836443
    url: https://doi.org/10.3390/jcm11030490
    source_license: CC BY 4.0（論文と PMC ページの表示で確認）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 定義と気胸との関係は本文（2.4節）で確認した。同論文は、ブレブやブラが破裂していない状態で見つかることも多く、胸膜の多孔性（pleural porosity）という別の機序も紹介しているため、破裂が確立した唯一の機序ではない。既存の RO-034 は巨大ブラと気胸との鑑別や外科治療を担い、本カードは定義の区別と原発性自然気胸との関係に絞った
  curriculum:
    kokushi: 医学各論 Ⅳ-2-B-①（気腫性囊胞<ブラ、ブレブ>、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-216 (id: JlvnlyM)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: IL-062
  domain: IL
  subdomain: 好酸球性肺炎
  assertion:
    plain_statement_ja: 好酸球性肺炎は、肺組織や気管支肺胞洗浄（BAL）液への好酸球の著明な集積を特徴とする疾患群で、主要な病型は急性好酸球性肺炎（AEP）と慢性好酸球性肺炎（CEP）である。AEP は喫煙の開始・再開・増量といった喫煙習慣の変化や、粉塵などの吸入曝露と関連することが多く、発熱・咳嗽・呼吸困難が急性に出現して数日で進み、低酸素血症や呼吸不全を来しうる。初診時の末梢血好酸球増多は約3割の症例にとどまる一方、BAL では好酸球が通常40%を超え、診断には BAL 好酸球25%超などが目安とされる。画像では両側のすりガラス影と浸潤影、小葉間隔壁の肥厚がみられ、胸水を伴うことが多い。副腎皮質ステロイドに速やかに反応し、軽度の低酸素血症の症例では自然軽快もみられ、禁煙すれば再発は通常ない。CEP は数か月にわたり咳嗽や呼吸困難が遷延する病型で、女性に多く（男性の約2倍）、アレルギー疾患の合併が半数を超える。末梢血好酸球増多と IgE の上昇が多くの症例でみられ、BAL の好酸球は平均40〜60%で、画像では末梢側に優位な浸潤影が特徴的である。治療の中心は副腎皮質ステロイドで、プレドニゾロン換算で体重1 kgあたり0.5 mg程度から開始し6〜12か月かけて漸減するが、自然軽快は1割未満とまれで、再発が頻繁にみられる。両病型とも、薬剤や寄生虫・真菌などの感染といった既知の原因による二次性の好酸球性肺炎を除外して診断する。
    condition:
      region: null
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4891
    source: 'Suzuki Y, Suda T. Eosinophilic pneumonia: A review of the previous literature, causes, diagnosis, and management. Allergol Int. 2019;68(4):413-419'
    doi: 10.1016/j.alit.2019.05.006
    pmid: null
    pmcid: null
    url: https://doi.org/10.1016/j.alit.2019.05.006
    source_license: CC BY-NC-ND 4.0（論文の表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 副腎皮質ステロイド（プレドニゾロン）は国内で承認されている薬剤だが、添付文書の効能・効果に好酸球性肺炎の明記は確認しておらず、本疾患への投与が適応外使用として位置づけられる可能性がある。用量と漸減期間は出典（Suzuki & Suda 2019）の記載に基づく。PMID は本作業では確認できなかったため null とした（DOI で文献は一意に特定できる）。既存の IL-026 は単一コホートの疫学のみであり、本カードは疾患の一般像を担う
  curriculum:
    kokushi: 医学各論 Ⅳ-3-A-③（好酸球性肺炎、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-229 (id: Jlvnlzw)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: PV-032
  domain: PV
  subdomain: 左心系疾患に伴う肺高血圧症
  assertion:
    plain_statement_ja: 左心系疾患に伴う肺高血圧症（臨床分類の第2群）は毛細血管後性で、血行動態の定義は平均肺動脈圧20 mmHg超かつ肺動脈楔入圧15 mmHg超であり、肺血管抵抗2 Wood単位以下を孤立性毛細血管後性、2 Wood単位を超える場合を混合性毛細血管後性として区別する。管理の基本は基礎にある左心疾患の治療を最適化することであり（推奨クラスI、エビデンスレベルA）、肺動脈性肺高血圧症に承認された薬剤は本群には推奨されない（クラスIII、レベルA）。
    condition:
      region: 国際
      対象: 左心系疾患に伴う肺高血圧症の成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-444
    source: Humbert M, Kovacs G, Hoeper MM, et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Respir J 2023;61(1):2200879
    doi: 10.1183/13993003.00879-2022
    pmid: '36028254'
    pmcid: null
    url: https://doi.org/10.1183/13993003.00879-2022
    source_license: Publisher holds Copyright（ERS、リポジトリの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 閾値（平均肺動脈圧・肺動脈楔入圧・肺血管抵抗）と推奨クラスは ESC/ERS 2022 ガイドライン本文（第8章の定義と推奨表22A）から読み取り。PV-020 が「楔入圧・肺血管抵抗の閾値は本文で確認してからカードを追加する」としていた血行動態の定義を本カードで補った。薬剤について、主張は肺動脈性肺高血圧症の承認薬というクラス単位の記述で個別の薬剤名は含まない。これらの薬剤は国内では肺動脈性肺高血圧症（第1群）に承認されており、左心系疾患に伴う肺高血圧症（第2群）への適応はない。心不全そのものの治療内容は循環器のカードが担う。
  curriculum:
    kokushi: 医学各論 Ⅳ-5-C-①（左心系疾患に伴う肺高血圧症、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: LC-055
  domain: LC
  subdomain: 悪性リンパ腫
  assertion:
    plain_statement_ja: 縦隔原発のリンパ腫の代表は、胸腺に発生する原発性縦隔（胸腺）大細胞型B細胞リンパ腫と古典的Hodgkinリンパ腫である。原発性縦隔大細胞型B細胞リンパ腫はびまん性大細胞型B細胞リンパ腫の亜型で非Hodgkinリンパ腫の約5%を占め、若年成人（発症年齢の中央値30〜40歳）に多く、女性が男性の約2倍である。前縦隔上部の大きな腫瘤として現れ、局所浸潤・圧迫による呼吸困難、咳嗽、胸痛、嚥下困難、嗄声や、上大静脈症候群をはじめとする静脈閉塞の症状を生じ、胸水や心囊水を伴うことがある。結節硬化型の古典的Hodgkinリンパ腫との鑑別が問題となり、両者の中間的な像を示すものは縦隔グレイゾーンリンパ腫とされる。診断は組織の採取（生検）と免疫組織化学による。
    condition:
      region: 国際
      対象: 縦隔腫瘤を呈する若年成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4892
    source: 'Hutchinson CB, Wang E. Primary mediastinal (thymic) large B-cell lymphoma: a short review with brief discussion of mediastinal gray zone lymphoma. Arch Pathol Lab Med. 2011;135(3):394-398'
    doi: 10.5858/2009-0463-RSR.1
    pmid: '21366467'
    pmcid: null
    url: https://doi.org/10.5858/2009-0463-RSR.1
    source_license: College of American Pathologists（Archives of Pathology & Laboratory Medicine、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 臨床像（若年発症、女性優位、圧迫症状の内訳）は総説本文に基づく。非Hodgkinリンパ腫に占める割合（約5%）は本総説の記載で、他の資料では2〜4%とするものもある。書誌・PMID・DOI は PubMed レコードで確認し、DOI は他論文の参考文献の表記とも一致した。治療（化学療法のレジメンなど）は本カードでは扱わず、悪性リンパ腫の他のカードが担う。個別の薬剤名は主張に含まない。
  curriculum:
    kokushi: 医学各論 Ⅳ-6-C-①（悪性リンパ腫、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: PL-031
  domain: PL
  subdomain: 縦隔気腫、皮下気腫
  assertion:
    plain_statement_ja: 自然縦隔気腫は、肺胞の破裂で漏れた空気が気管支・肺血管周囲の鞘に沿って縦隔へ入り込むこと（Macklin効果）で生じ、若年に多く、男性が約76%を占める。症状は胸痛が中心で頻度は60〜100%（胸骨後の痛みで頸部や背部へ放散する）、呼吸困難75%、咳嗽80%、頸部痛36%を伴い、空気が頸部や皮下へ広がった皮下気腫を約70%に認める。心拍に同期して前胸部に捻髪音様の所見を聴く Hamman 徴候が手がかりとなる。経過は多くは良好で、安静、鎮痛、鎮咳などの保存的治療で軽快し、酸素投与は空気の吸収を助ける。
    condition:
      region: 国際
      対象: 自然縦隔気腫の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4893
    source: Kouritas VK, Papagiannopoulos K, Lazaridis G, et al. Pneumomediastinum. J Thorac Dis. 2015;7(Suppl 1):S44-S49
    doi: 10.3978/j.issn.2072-1439.2015.01.11
    pmid: '25774307'
    pmcid: PMC4332083
    url: https://doi.org/10.3978/j.issn.2072-1439.2015.01.11
    source_license: © 2015 Journal of Thoracic Disease. All rights reserved（PMC 掲載ページの表示、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 症状・所見の頻度は総説が集計した自然縦隔気腫の症例報告・症例シリーズに基づく数値で、報告により幅があり（胸痛60〜100%など）、総説本文から読み取り。外傷性や食道破裂などに伴う二次性縦隔気腫の管理は本カードでは扱わない。個別の薬剤名は主張に含まない（鎮痛・鎮咳は保存的治療の要素としての記述）。
  curriculum:
    kokushi: 医学各論 Ⅳ-7-B-①（縦隔気腫、皮下気腫、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)；TBL-01-00-242 (id: Jlvnl1U)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: PL-032
  domain: PL
  subdomain: 気管食道瘻、食道気管瘻
  assertion:
    plain_statement_ja: 成人の後天性気管食道瘻は悪性と良性がほぼ半々を占める。悪性では食道癌が最も多く（207例の集積では77%）、次いで肺癌で、放射線治療や化学療法による腫瘍の壊死で瘻が生じることもある。良性の最多の原因は気管挿管・気管切開チューブのカフによる圧迫壊死で、良性例の約75%が医原性とされる。臨床像は咳嗽56%、誤嚥37%、発熱25%、嚥下困難19%、肺炎5%などで、嚥下で咳嗽が悪化する Ono 徴候が既知例の81%にみられ、反復する肺炎の原因となる。診断は食道造影（約70%で欠損が描出される）と、気管支鏡・上部消化管内視鏡による直接の確認を組み合わせる。治療は、悪性ではステント留置が緩和的治療の中心となり、良性では根治的手術が可能で、ステントは手術までの橋渡しに用いられる。
    condition:
      region: 国際
      対象: 成人の後天性気管食道瘻の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4894
    source: Kim HS, Khemasuwan D, Diaz-Mendoza J, Mehta AC. Management of tracheo-oesophageal fistula in adults. Eur Respir Rev. 2020;29(158):200094
    doi: 10.1183/16000617.0094-2020
    pmid: '33153989'
    pmcid: PMC9488631
    url: https://doi.org/10.1183/16000617.0094-2020
    source_license: CC BY-NC 4.0（PMC 掲載ページで確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 症状の頻度は総説本文が引用する Burt らの200例を超える集積（悪性が中心）に基づく数値で、本文から読み取り。依頼文が見込みとしていた ESGE 2021 は悪性瘻へのステント推奨が中心のため採用せず、後天性の原因・臨床像・診断・治療を通して確認できる本総説を単独の出典とした。悪性例の生存期間の中央値は診断後3か月未満と本文にあるが、予後は本カードの主張には含めていない。先天性（食道閉鎖に伴うもの）は小児の領域のため扱わない。個別の薬剤名は主張に含まない。
  curriculum:
    kokushi: 医学各論 Ⅳ-7-B-②（気管食道瘻、食道気管瘻、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: PL-033
  domain: PL
  subdomain: 反回神経麻痺
  assertion:
    plain_statement_ja: 一側性の声帯麻痺は左側に多く、台湾の3次施設の後方視研究（原因の確定した194例のうち一側性178例）では左側が122例（69%）で右側56例（31%）の約2倍であった。これは、左反回神経が胸腔内を下行して大動脈弓の下を回ってから上行する長い走行をとり、障害を受ける区間が長いためと説明される。原因全体では手術が61.3%と最多である一方、胸部領域の原因として腫瘍性病変が17.5%を占め、その内訳では肺癌（15例）が最も多く、15例中14例が左側であった。心血管疾患によるものも2%あり、大動脈弓近傍での神経の圧迫（Ortner 症候群）が機序となる。
    condition:
      region: 国際
      対象: 一側性声帯麻痺の成人患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4895
    source: Wang HW, Lu CC, Chao PZ, Lee FP. Causes of Vocal Fold Paralysis. Ear Nose Throat J. 2022;101(7):NP294-NP298
    doi: 10.1177/0145561320965212
    pmid: null
    pmcid: null
    url: https://doi.org/10.1177/0145561320965212
    source_license: 未確認（誌面・PDF で CC 表示を確認できず。© The Author(s) 2020、再利用は出版社の許可手続きによる旨の表示あり）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 割合は台湾の3次施設の後方視研究（2010〜2019年、原因の確定した194例）の集計で、原著の表から読み取り。単施設の集計のため、施設・地域による偏りがありうる。項目の側面に挙がる大動脈瘤・左房拡大などの個別の心血管性原因は、本出典では内訳が示されなかったため主張には含めていない（心血管性は全体の2%であることのみ確認した）。PMID は作成時点で確認できず null とした（文献は DOI で特定できる）。ライセンスは CC 表示を確認できなかったため UNKNOWN とし、取り込み時の確認に委ねる。頸部の手術・腫瘍など原因の大勢と評価の進め方は既存カード OT-042 が担う。
  curriculum:
    kokushi: 医学各論 Ⅳ-7-B-④（反回神経麻痺、a）
    core_curriculum: 'PS-02-07-05 (id: JkxnuRE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
```


## 3. カリキュラム対応表

| カード | subdomain | kokushi | コアカリ |
|---|---|---|---|
| VI-033 | ウイルス性髄膜炎 | 医学各論 Ⅻ-1-A-⑱（ウイルス性髄膜炎、a） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-033 (id: Jlvnlcw) |
| CM-008 | クラミジア肺炎 | 医学各論 Ⅻ-2-A-①（クラミジア肺炎、a） | PS-01-03-06 (id: JkxnuLQ)；PS-03-03-01 (id: JkxnuUg)；TBL-01-00-592 (id: JlvnmXc) |
| CM-009 | マイコプラズマ肺炎 | 医学各論 Ⅻ-2-A-③（マイコプラズマ肺炎、a） | PS-01-03-06 (id: JkxnuLQ)；PS-03-03-04 (id: JkxnuUs)；TBL-01-00-592 (id: JlvnmXc) |
| BA-047 | 表皮ブドウ球菌感染症 | 医学各論 Ⅻ-2-B-⑤（表皮ブドウ球菌感染症、a） | PS-01-03-04 (id: JkxnuLI)；PS-03-03-02 (id: JkxnuUk) |
| BA-048 | クレブシエラ感染症 | 医学各論 Ⅻ-2-B-⑭（クレブシエラ感染症、a） | PS-03-03-02 (id: JkxnuUk)；PS-03-03-04 (id: JkxnuUs) |
| BA-049 | セラチア感染症 | 医学各論 Ⅻ-2-B-⑮（セラチア感染症、a） | PS-01-03-04 (id: JkxnuLI)；PS-03-03-02 (id: JkxnuUk) |
| BA-050 | 緑膿菌感染症 | 医学各論 Ⅻ-2-B-⑱（緑膿菌感染症、a） | PS-03-03-02 (id: JkxnuUk)；PS-03-03-04 (id: JkxnuUs) |
| BA-051 | アシネトバクター感染症 | 医学各論 Ⅻ-2-B-⑲（アシネトバクター感染症、a） | PS-03-03-02 (id: JkxnuUk)；PS-03-03-04 (id: JkxnuUs) |
| BA-052 | ガス壊疽 | 医学各論 Ⅻ-2-B-⑳（ガス壊疽、a） | PS-01-03-03 (id: JkxnuLE)；TBL-01-00-595 (id: JlvnmXw) |
| RI-058 | 感冒<かぜ症候群>、上気道炎 | 医学各論 Ⅳ-1-A-①（感冒<かぜ症候群>、上気道炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-204 (id: JlvnlxA) |
| RI-059 | 胸膜炎 | 医学各論 Ⅳ-1-G-①（胸膜炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-213 (id: Jlvnlx4)；TBL-01-00-240 (id: Jlvnl08) |
| RO-042 | 気管支拡張症 | 医学各論 Ⅳ-2-A-①（気管支拡張症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-234 (id: Jlvnl0U) |
| RO-043 | 閉塞性細気管支炎 | 医学各論 Ⅳ-2-A-③（閉塞性細気管支炎、a） | PS-02-07-05 (id: JkxnuRE) |
| RO-044 | 気腫性囊胞<ブラ、ブレブ> | 医学各論 Ⅳ-2-B-①（気腫性囊胞<ブラ、ブレブ>、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-216 (id: JlvnlyM) |
| IL-062 | 好酸球性肺炎 | 医学各論 Ⅳ-3-A-③（好酸球性肺炎、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-229 (id: Jlvnlzw) |
| PV-032 | 左心系疾患に伴う肺高血圧症 | 医学各論 Ⅳ-5-C-①（左心系疾患に伴う肺高血圧症、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-226 (id: JlvnlzQ) |
| LC-055 | 悪性リンパ腫 | 医学各論 Ⅳ-6-C-①（悪性リンパ腫、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-646 (id: JlvnmcY) |
| PL-031 | 縦隔気腫、皮下気腫 | 医学各論 Ⅳ-7-B-①（縦隔気腫、皮下気腫、a） | PS-02-07-05 (id: JkxnuRE)；TBL-01-00-242 (id: Jlvnl1U) |
| PL-032 | 気管食道瘻、食道気管瘻 | 医学各論 Ⅳ-7-B-②（気管食道瘻、食道気管瘻、a） | PS-02-07-05 (id: JkxnuRE) |
| PL-033 | 反回神経麻痺 | 医学各論 Ⅳ-7-B-④（反回神経麻痺、a） | PS-02-07-05 (id: JkxnuRE) |

## 4. 未解決事項

- SRC-4891（Suzuki & Suda 2019、好酸球性肺炎）の PMID は確認できず null（DOI で一意に特定可能）
- SRC-4895（Wang 2022、反回神経麻痺）の PMID は確認できず null、ライセンス表示も確認できず UNKNOWN。PL-033 では大動脈瘤・左房拡大は出典の内訳がなく未収載
- IL-062 のプレドニゾロンについて、効能・効果への「好酸球性肺炎」の明記は未確認で適応外使用の可能性を uncertainty に明記した（PMDA 添付文書での確定が宿題）
- SRC-378（ERS 気管支拡張症 GL）のライセンスは既存登録どおり未確認（UNKNOWN）。RO-042 の内容は ERJ 本文で確認した
- RI-059（胸膜炎）は結核性胸膜炎の詳細（胸水 ADA 等）に踏み込んでいない（採用出典の確認範囲外）
- CM-008（クラミジア肺炎）は依頼表の側面の「集団発生」を出典抄録で確認できず未カバー。BA-047（表皮ブドウ球菌）は人工関節・人工弁など血管内デバイス以外の人工物感染の詳細が未カバー
- BA-048（クレブシエラ）は古典株の代表的病像の列挙が採用出典（過毒力株の総説）の確認範囲になく、日和見感染の観点の記述にとどめた
- 未使用の SRC 番号：SRC-4896〜4960（この回では使わない）

## 5. 引き継ぎメモ

- 薬剤の国内承認で当初の想定と違った点（添付文書・承認通知で確認し、各カードの uncertainty に薬剤名を特定して記載）：セフタジジム・アビバクタムは2024年6月に国内承認済み。コリスチンは2015年承認で適応菌種に緑膿菌・アシネトバクター属を含む一方、セラチア属は抗菌活性を示さない菌種として明記されている。スルバクタムの国内適応菌種にアシネトバクター属はなく適応外、チゲサイクリンの適応菌種にはアシネトバクター属を含む
- CM-009 のドキシサイクリンはマイコプラズマ肺炎に適応外（ミノサイクリンとレボフロキサシンは肺炎マイコプラズマが適応菌種内）で、uncertainty に明記した
- RO-043（閉塞性細気管支炎）の出典選定：Barker 2014 は抄録範囲で HRCT 所見を確認できず不採用とし、原因・画像・経過まで本文で確認できた Ryu 2003（SRC-4889）を採用した。Ryu が挙げる原因薬剤の個別名は分類水準にとどめた
- LC-055 の「NHL の約5%」は採用総説自身の数値（他資料では2〜4%）で、uncertainty に明記した
- 薬剤名のあるカードはすべて uncertainty に薬剤名を特定した国内承認・適応の注記を入れた
