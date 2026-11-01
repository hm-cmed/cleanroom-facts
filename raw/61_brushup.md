# 第61回（ブラッシュアップ：見送り分・宿題・版の書き換え）成果物

- 対象15項目、26件（IN-111〜113、LV-111、AB-116、MP-040〜042、DV-021〜022、FT-015〜016、SA-021〜022、HF-030〜031、PE-038〜040、NL-022、SK-033、ND-057〜061）
- 新規出典は10件（SRC-4441〜4450）。未使用は SRC-4451〜4520
- 書き換え3件（NL-022・SK-033・ND-057〜061）は新カードで、旧カード（NL-004・SK-013・ND-050）は取り込み側で retired にし、superseded_by に新カードを記録する想定
- 小腸癌（IN-112）は登録出典 SRC-4214（Benson Version 1.2020）の範囲に限定した。現行 Version 2.2026 の免疫療法の拡大は主張に入れず、uncertainty に明記した
- NL-022（花粉症の疫学）には抗原回避の文を入れていない。出典（SRC-2825、疫学調査）では裏づけられず、回避は NL-003（鼻アレルギー診療ガイドライン2024年版）が担う
- FT-016 は既存の FT-008 と同じ Mari 2000（SRC-3348）を出典とし、感度・偽陽性率の結論は FT-008 と重なるため症例内訳と信頼区間に絞った。重複と判断されれば FT-008 への統合が妥当（その場合は25件になる）
- ADHD の2件（DV-021・022）は書籍本文を直接確認できていないため、学会の公開資料で確認できた枠組みの範囲に限定し、確認経路と限界を各カードの uncertainty に明記した
- 穿通性心臓外傷で候補に挙げた WTA 2012（Burlew）は独立カードにせず、救急室開胸は EAST 2015 の MP-041 に一本化したため、出典登録はしていない

## 1. 抽出元ホワイトリスト

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-185 | Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J. 2025;89:1278-1444 | 10.1253/circj.CJ-25-0002 | 40159241 | CC BY-NC-ND 4.0 | RESTRICTED | 出典マスター登録済み（第60回 HF-026 で使用）。日本語版全文 PDF（日本循環器学会公式サイト）で第2章§3.2「右心不全」の本文を確認 |
| SRC-2825 | 松原篤、坂下雅文、後藤穣、ほか. 2019年全国疫学調査（鼻アレルギー）. 日本耳鼻咽喉科学会会報. 2020;123:485-490 | ― | ― | 未確認（日本語誌） | UNKNOWN | 既存登録（出典マスターで確認）。疫学数値は原著抄録（J-STAGE）と公表資料で確認 |
| SRC-3092 | Vázquez DO, Giavina-Bianchi P, Josviack D, et al. The 2025 WAO Guidelines for the classification, diagnosis, and treatment of hereditary angioedema, with consideration of worldwide disparities. World Allergy Organ J. 2026;19(5):101335 | 10.1016/j.waojou.2026.101335 | 42165046 | CC BY-NC-ND 4.0（Crossref で確認） | RESTRICTED | 既存登録（出典マスターで確認）。書誌・PMID・PMCID は PubMed で確認し、推奨は PMC 本文で確認 |
| SRC-3348 | Mari G, Deter RL, Carpenter RL, et al.; Collaborative Group for Doppler Assessment of the Blood Velocity in Anemic Fetuses. Noninvasive diagnosis by Doppler ultrasonography of fetal anemia due to maternal red-cell alloimmunization. N Engl J Med. 2000;342(1):9-14 | 10.1056/NEJM200001063420102 | 10620643 | CC 表示なし（NEJM） | RESTRICTED | 既存登録（マスターの記載）。数値は PubMed 抄録で再確認 |
| SRC-4214 | Benson AB, Venook AP, Al-Hawary MM, et al. Small Bowel Adenocarcinoma, Version 1.2020, NCCN Clinical Practice Guidelines in Oncology. J Natl Compr Canc Netw. 2019;17(9):1109-1133. | 10.6004/jnccn.2019.0043 | 31487687 | CC表示なし（購読誌） | RESTRICTED | 出典マスター登録済み（SRC-4214）。PMID は PubMed で確認（マスター側は null で、補完候補）。本文は PMC の著者原稿（PMC10191182）で Version 1.2020 の推奨範囲を照合 |
| SRC-4215 | Theis VS, Sripadam R, Ramani V, Lal S. Chronic radiation enteritis. Clin Oncol (R Coll Radiol). 2010;22(1):70-83. | 10.1016/j.clon.2009.10.003 | 19897345 | CC表示なし（購読誌） | RESTRICTED | 出典マスター登録済み（SRC-4215）。PMID は PubMed で DOI から確認（マスター側は null で、補完候補）。主張は抄録と総説の範囲で照合 |
| SRC-4226 | Gerson LB, Fidler JL, Cave DR, Leighton JA. ACG Clinical Guideline: Diagnosis and Management of Small Bowel Bleeding. Am J Gastroenterol. 2015;110(9):1265-1287. | 10.1038/ajg.2015.246 | 26303132 | CC表示なし（学会ガイドライン・購読誌） | RESTRICTED | 出典マスター登録済み（SRC-4226）。PMID は PubMed で確認（マスター側は null で、補完候補）。主張は抄録とガイドラインの推奨要約で照合 |
| SRC-4227 | European Association for the Study of the Liver. EASL Clinical Practice Guidelines on the management of cystic liver diseases. J Hepatol. 2022;77(4):1083-1108. | 10.1016/j.jhep.2022.06.002 | 35728731 | CC表示なし（学会ガイドライン・購読誌） | RESTRICTED | 出典マスター登録済み（SRC-4227）。PMID は PubMed で確認（マスター側は null で、補完候補）。推奨文はガイドライン本文（J Hepatol 誌サイト）で照合 |
| SRC-4433 | Montalban X, Lebrun-Frénay C, Oh J, et al. Diagnosis of multiple sclerosis: 2024 revisions of the McDonald criteria. Lancet Neurol. 2025;24(10):850-865 | 10.1016/S1474-4422(25)00270-4 | 40975101 | 購読誌（CC 表示なし） | RESTRICTED | 既存登録（提案B で登録）。書誌・DOI・PMID は PubMed で確認。追加カードの細部は抄録と解説で確認（各カードの uncertainty に明記） |
| SRC-4441 | Swallow CJ, Strauss DC, Bonvalot S, et al. Management of Primary Retroperitoneal Sarcoma (RPS) in the Adult: An Updated Consensus Approach from the Transatlantic Australasian RPS Working Group. Ann Surg Oncol. 2021;28(12):7873-7888. | 10.1245/s10434-021-09654-z | 33852100 | テキストマイニング用ライセンスのみで CC 表示なし（Crossref の license 欄で確認） | RESTRICTED | 新規出典。PubMed で書誌・DOI・PMID・PMCID（PMC9257997）を確認し、本文は PMC で照合。仮番号 SRC-9101 を使用（組み立て時に SRC-4441 以降へ振り直す） |
| SRC-4442 | Hromalik LR Jr, Wall MJ Jr, Mattox KL, Tsai PI. Penetrating cardiac injury: a narrative review. Mediastinum. 2023;7:15 | 10.21037/med-22-18 | 37261091 | CC BY-NC-ND 4.0（本文の Open Access Statement） | RESTRICTED | PMC 全文（PMC10226890）でライセンス表示と本文を確認 |
| SRC-4443 | Seamon MJ, Haut ER, Van Arendonk K, et al. An evidence-based approach to patient selection for emergency department thoracotomy: A practice management guideline from the Eastern Association for the Surgery of Trauma. J Trauma Acute Care Surg. 2015;79(1):159-173 | 10.1097/TA.0000000000000648 | 26091330 | CC 表示なし（購読誌） | RESTRICTED | PubMed 抄録で推奨文と生存率を確認。Crossref にライセンス表示なし |
| SRC-4444 | Ball CG, Lee A, Kaminsky M, et al. Technical considerations in the management of penetrating cardiac injury. Can J Surg. 2022;65(5):E580-E592 | 10.1503/cjs.008521 | 36302130 | CC BY-NC-ND 4.0（本文のライセンス表示） | RESTRICTED | PMC 全文（PMC9451503）でライセンス表示と本文を確認 |
| SRC-4445 | ADHDの診断・治療指針に関する研究会 編（齊藤万比古・飯田順三 編集）. 注意欠如・多動症―ADHD―の診断・治療ガイドライン 第5版. じほう. 2022年. ISBN 978-4-8407-5467-5 | なし（書籍） | なし（書籍） | CC 表示なし（書籍） | RESTRICTED | 出版社ページ・CiNii 書誌・国立国会図書館サーチで書誌と ISBN を照合。本文は未確認（主張の範囲は引き継ぎメモ参照） |
| SRC-4446 | Society for Maternal-Fetal Medicine (SMFM); Mari G, Norton ME, Stone J, et al. Society for Maternal-Fetal Medicine (SMFM) Clinical Guideline #8: the fetus at risk for anemia--diagnosis and management. Am J Obstet Gynecol. 2015;212(6):697-710 | 10.1016/j.ajog.2015.01.059 | 25824811 | CC 表示なし | RESTRICTED | PubMed 抄録で推奨文（7項目）を確認。学会の公式ページで2025年に reaffirmed と確認 |
| SRC-4447 | Schmitt SK. Reactive Arthritis. Infect Dis Clin North Am. 2017;31(2):265-277 | 10.1016/j.idc.2017.01.002 | 28292540 | CC 表示なし | RESTRICTED | PubMed 抄録で確認。Crossref のライセンスはテキストマイニング用のみ |
| SRC-4448 | Dingemann C, Eaton S, Aksnes G, et al. ERNICA Consensus Conference on the Management of Patients with Esophageal Atresia and Tracheoesophageal Fistula: Follow-up and Framework. Eur J Pediatr Surg. 2020;30(6):475-482 | 10.1055/s-0039-3400284 | 31777030 | 購読誌（CC 表示なし） | RESTRICTED | PubMed・Crossref で書誌とライセンス表示を確認。抄録で合意の範囲を確認 |
| SRC-4449 | Krishnan U, Mousa H, Dall'Oglio L, et al. ESPGHAN-NASPGHAN Guidelines for the Evaluation and Treatment of Gastrointestinal and Nutritional Complications in Children With Esophageal Atresia-Tracheoesophageal Fistula. J Pediatr Gastroenterol Nutr. 2016;63(5):550-570 | 10.1097/MPG.0000000000001401 | 27579697 | 購読誌（CC 表示なし） | RESTRICTED | PubMed・Crossref で書誌とライセンス表示を確認。抄録で臨床課題の範囲を確認 |
| SRC-4450 | Takehara H, Yakabe S, Kameoka K. Laparoscopic percutaneous extraperitoneal closure for inguinal hernia in children: clinical outcome of 972 repairs done in 3 pediatric surgical institutions. J Pediatr Surg. 2006;41(12):1999-2003 | 10.1016/j.jpedsurg.2006.08.032 | 17161191 | 購読誌（CC 表示なし） | RESTRICTED | PubMed・Crossref で書誌とライセンス表示を確認。抄録で成績を確認 |

## 2. 事実票

```yaml
- id: IN-111
  domain: IN
  subdomain: 放射線性腸炎
  assertion:
    plain_statement_ja: 慢性放射線性腸炎は、狭窄、瘻孔、穿孔、出血、吸収不良などの合併症を来し、評価では原疾患である悪性腫瘍の再発の除外が重要である。治療は栄養管理を含む対症療法が中心で、手術は閉塞・穿孔・瘻孔などの合併症例に限られるが、術後合併症や再手術の頻度が高い。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4215
    source: Theis VS, Sripadam R, Ramani V, Lal S. Chronic radiation enteritis. Clin Oncol (R Coll Radiol). 2010;22(1):70-83.
    doi: 10.1016/j.clon.2009.10.003
    pmid: '19897345'
    pmcid: null
    url: https://doi.org/10.1016/j.clon.2009.10.003
    source_license: CC表示なし（購読誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 2010年の総説に基づく記述で、同総説も治療のエビデンスは限定的としている。本カードは小腸病変の合併症と管理が中心で、放射線性直腸炎は扱っていない。病態と経過は IN-090 が担当する。
  curriculum:
    kokushi: 医学各論 Ⅵ-3-B-⑥（放射線性腸炎、c）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: IN-112
  domain: IN
  subdomain: 小腸癌
  assertion:
    plain_statement_ja: 小腸腺癌の治療は、限局例では外科切除が基本であり、進行例の初回全身療法には FOLFOX や CAPEOX などのオキサリプラチン併用レジメンが用いられる。ミスマッチ修復欠損（dMMR）またはマイクロサテライト不安定性が高い（MSI-H）進行例では、後方ラインの選択肢としてペムブロリズマブなどの抗PD-1療法が位置づけられている。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4214
    source: Benson AB, Venook AP, Al-Hawary MM, et al. Small Bowel Adenocarcinoma, Version 1.2020, NCCN Clinical Practice Guidelines in Oncology. J Natl Compr Canc Netw. 2019;17(9):1109-1133.
    doi: 10.6004/jnccn.2019.0043
    pmid: '31487687'
    pmcid: PMC10191182
    url: https://doi.org/10.6004/jnccn.2019.0043
    source_license: CC表示なし（購読誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 出典は NCCN ガイドライン Version 1.2020（2019年公表）で、現行は Version 2.2026 であり、現行版では免疫療法の位置づけが拡大している（初回治療を含む位置づけの追加、治療ラインを問わないチェックポイント阻害薬の表の新設など）。本カードの主張は Version 1.2020 の範囲に限る。ペムブロリズマブは国内で「がん化学療法後に増悪した進行・再発のMSI-Hを有する固形癌（標準的な治療が困難な場合に限る）」の適応で承認されている。一方、FOLFOX・CAPEOX の構成薬（オキサリプラチン、フルオロウラチル、カペシタビンなど）は結腸・直腸癌などでは承認されているが、小腸癌は国内の適応に含まれず、保険適用上は適応外使用にあたる。疾患の概要と MMR・MSI 検査の推奨は IN-094 が担当する。
  curriculum:
    kokushi: 医学各論 Ⅵ-3-C-③（小腸癌、c）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；PS-03-04-14 (id: JkxnuYE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: IN-113
  domain: IN
  subdomain: 毛細血管拡張症
  assertion:
    plain_statement_ja: 小腸の血管拡張（angioectasia）による出血では、出血源が同定され貧血や活動性出血が続く場合に、バルーン内視鏡などを用いた内視鏡的治療（アルゴンプラズマ凝固やクリップによる止血など）を行う。大動脈弁狭窄症に血管拡張を合併するHeyde症候群で出血が持続する場合は、大動脈弁置換を検討することが条件付きで推奨される。
    condition:
      region: 米国
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4226
    source: 'Gerson LB, Fidler JL, Cave DR, Leighton JA. ACG Clinical Guideline: Diagnosis and Management of Small Bowel Bleeding. Am J Gastroenterol. 2015;110(9):1265-1287.'
    doi: 10.1038/ajg.2015.246
    pmid: '26303132'
    pmcid: null
    url: https://doi.org/10.1038/ajg.2015.246
    source_license: CC表示なし（学会ガイドライン・購読誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 内視鏡的治療の具体的手技（アルゴンプラズマ凝固、クリップなど）はガイドライン本文の記載による。Heyde症候群への大動脈弁置換は条件付き推奨（中等度の質のエビデンス）で、適応判断は専門施設での評価による。本カードは後天性の血管拡張に限り、遺伝性出血性毛細血管拡張症（HHT）は対象外（疾患像は IN-117 が担当する）。
  curriculum:
    kokushi: 医学各論 Ⅵ-5-E-②（毛細血管拡張症<angioectasia>、c）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: LV-111
  domain: LV
  subdomain: 肝囊胞
  assertion:
    plain_statement_ja: 有症状で胆管との交通のない単純性肝囊胞には、穿刺吸引・硬化療法や腹腔鏡下囊胞開窓術など、施設で実施可能な最良の囊胞減量治療を行う（強い推奨）。囊胞感染には、フルオロキノロン系薬または第3世代セフェム系薬を経験的治療の第一選択とし、4〜6週間投与する（強い推奨）。
    condition:
      region: 欧州
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4227
    source: European Association for the Study of the Liver. EASL Clinical Practice Guidelines on the management of cystic liver diseases. J Hepatol. 2022;77(4):1083-1108.
    doi: 10.1016/j.jhep.2022.06.002
    pmid: '35728731'
    pmcid: null
    url: https://doi.org/10.1016/j.jhep.2022.06.002
    source_license: CC表示なし（学会ガイドライン・購読誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 抗菌薬はガイドライン本文が例示するシプロフロキサシン（フルオロキノロン系）をはじめ、レボフロキサシン、セフトリアキソン（第3世代セフェム系）などはいずれも国内で承認されている抗菌薬である。ただし、添付文書の効能・効果に肝囊胞感染は含まれておらず、保険適用上は適応外使用にあたる。減量治療の手技の使い分けは施設の体制により、ガイドラインは施設で最良の方法を推奨している。診断と無症状例の扱いは LV-105 が担当する。
  curriculum:
    kokushi: 医学各論 Ⅵ-6-A-①（肝囊胞、c）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: AB-116
  domain: AB
  subdomain: 後腹膜腫瘍
  assertion:
    plain_statement_ja: 原発性後腹膜肉腫の治療は、専門施設で多診療科チームのもとに行うことが前提で、標準治療は腫瘍と癒着・近接する臓器を含めた一括（コンパートメント）切除である。再発様式は組織型で異なり、脂肪肉腫では局所再発が中心で死因ともなり、平滑筋肉腫では遠隔転移のリスクが高い。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4441
    source: 'Swallow CJ, Strauss DC, Bonvalot S, et al. Management of Primary Retroperitoneal Sarcoma (RPS) in the Adult: An Updated Consensus Approach from the Transatlantic Australasian RPS Working Group. Ann Surg Oncol. 2021;28(12):7873-7888.'
    doi: 10.1245/s10434-021-09654-z
    pmid: '33852100'
    pmcid: PMC9257997
    url: https://doi.org/10.1245/s10434-021-09654-z
    source_license: テキストマイニング用ライセンスのみで CC 表示なし（Crossref の license 欄で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: TARPSWG コンセンサス（Ann Surg Oncol 2021）の範囲の記述で、海外の専門施設の体制を前提とする。鑑別にはリンパ腫が含まれ、生検でリンパ腫と判明した場合は化学療法が治療の主体となる。疾患像と診断は AB-115 が担当する。
  curriculum:
    kokushi: 医学各論 Ⅵ-9-C-④（後腹膜腫瘍、c）
    core_curriculum: 'PS-02-08-05 (id: JkxnuRY)；PS-03-04-14 (id: JkxnuYE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: MP-040
  domain: MP
  subdomain: 心臓外傷
  assertion:
    plain_statement_ja: 穿通性心臓外傷はまれだが致死的な外傷で、民間では銃創と刺創が主な原因であり、医療行為に伴うものもある。いずれの心腔の損傷でも、心膜腔への出血が急速に心タンポナーデを来たして死因になりうる一方、心膜が血液を封じ込めれば病院到着まで生存しうる。臨床像はタンポナーデによる血行動態の不安定が中心で、Beck の三徴（心音減弱、頸静脈怒張、低血圧）がそろうのはタンポナーデ例の約10%にとどまる。初期診断の標準は心エコーで心囊液（心囊内出血）を確認することであり、精度は96〜97%、感度と特異度はほぼ100%と報告される。心エコーが使えない場合は剣状突起下心膜開窓や心囊穿刺が選択肢になるが、時間を要する。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4442
    source: 'Hromalik LR Jr, Wall MJ Jr, Mattox KL, Tsai PI. Penetrating cardiac injury: a narrative review. Mediastinum. 2023;7:15'
    doi: 10.21037/med-22-18
    pmid: '37261091'
    pmcid: PMC10226890
    url: https://doi.org/10.21037/med-22-18
    source_license: CC BY-NC-ND 4.0（本文の Open Access Statement で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 穿通性心臓外傷を包括する診療ガイドラインはなく、本カードは総説に基づく。海外の集積は銃器損傷の比率が高く、刺創の比率が高い日本の実情とは受傷機転の構成が異なる。損傷部位別の頻度は、総説の中で単一の数値としては確認できなかったため主張に入れていない。
  curriculum:
    kokushi: 医学各論 Ⅴ-6-G-①（心臓外傷、c）
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；PS-03-05-12 (id: Jkxir3g)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: MP-041
  domain: MP
  subdomain: 心臓外傷
  assertion:
    plain_statement_ja: EAST の診療ガイドラインは、重症外傷後に脈拍を触れない患者への救急室開胸について、GRADE に基づく推奨を示している。穿通性胸部外傷後に脈拍を触れず生命徴候がある患者では救急室開胸を強く推奨し、生命徴候がない場合も条件付きで推奨する。根拠となった集積（救急室開胸10,238例）では、穿通性胸部外傷で生命徴候があった群の生存率は21.3%、なかった群では8.3%だった。鈍的外傷後に脈拍を触れず生命徴候もない患者では、救急室開胸を条件付きで推奨しないとされる。
    condition:
      region: 米国
      対象: 外傷後に脈拍を触れない患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4443
    source: 'Seamon MJ, Haut ER, Van Arendonk K, et al. An evidence-based approach to patient selection for emergency department thoracotomy: A practice management guideline from the Eastern Association for the Surgery of Trauma. J Trauma Acute Care Surg. 2015;79(1):159-173'
    doi: 10.1097/TA.0000000000000648
    pmid: '26091330'
    pmcid: null
    url: https://doi.org/10.1097/TA.0000000000000648
    source_license: CC 表示なし（購読誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本ガイドラインの射程は救急室開胸の患者選択に限られ、穿通性心臓外傷全体の管理を包括するガイドラインはない。集積は海外の外傷センターのもので、銃器損傷の比率が高く日本の実情とは受傷機転の構成が異なる。WTA の Critical Decisions（2012年）も受傷機転と生命徴候から開胸適応を決めるアルゴリズムを示すが、本カードの出典は EAST ガイドラインのみとし、WTA は独立カードにしなかった。
  curriculum:
    kokushi: 医学各論 Ⅴ-6-G-①（心臓外傷、c）
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；PS-03-05-12 (id: Jkxir3g)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: MP-042
  domain: MP
  subdomain: 心臓外傷
  assertion:
    plain_statement_ja: 穿通性心臓外傷の修復では、まず指による圧迫で出血を抑え、複数の裂傷には皮膚ステープルによる一時的な止血も使われる。大きな欠損には、Foley カテーテルのバルーンを心腔内で膨らませて壁に押し当て、内側から閉塞する方法があるが、牽引が強すぎると裂傷が拡大するため注意を要する。心室の修復はプレジェット付き水平マットレス縫合が基本であり、心房の欠損は血管鉗子で把持して連続縫合で閉じる。冠動脈に近い損傷にはステープルは使えず、冠動脈損傷と心筋虚血の評価が要る。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4444
    source: Ball CG, Lee A, Kaminsky M, et al. Technical considerations in the management of penetrating cardiac injury. Can J Surg. 2022;65(5):E580-E592
    doi: 10.1503/cjs.008521
    pmid: '36302130'
    pmcid: PMC9451503
    url: https://doi.org/10.1503/cjs.008521
    source_license: CC BY-NC-ND 4.0（本文のライセンス表示で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは手術手技の総説に基づく整理で、穿通性心臓外傷を包括する診療ガイドラインはない。海外の集積は銃器損傷の比率が高く日本の実情とは受傷機転の構成が異なる。大きな心室欠損で上下大静脈をクランプして心拍を落としてから縫合する手順など、個別手技の細部は本カードに含めていない。
  curriculum:
    kokushi: 医学各論 Ⅴ-6-G-①（心臓外傷、c）
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；PS-03-05-12 (id: Jkxir3g)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: DV-021
  domain: DV
  subdomain: 注意欠如多動性障害<注意欠如多動症><ADHD>
  assertion:
    plain_statement_ja: 国内の診断・治療ガイドライン第5版（2022年）では、注意欠如・多動症（ADHD）の診断は DSM-5 の診断基準に準拠し、不注意と多動性・衝動性の2つの症状領域について、症状の数、6か月以上の持続、12歳以前からの存在、家庭や学校など2つ以上の状況での出現、社会的・学業的機能の障害を確認する枠組みである。診断は、生育歴・発達歴の聴取と行動観察、学校などからの情報をあわせ、他の病態を除外しながら総合的に行う。
    condition:
      region: 日本
      対象: 小児および成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4445
    source: ADHDの診断・治療指針に関する研究会 編（齊藤万比古・飯田順三 編集）. 注意欠如・多動症―ADHD―の診断・治療ガイドライン 第5版. じほう. 2022年. ISBN 978-4-8407-5467-5
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: CC 表示なし（書籍）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本カードは書籍本文を直接確認できていない。書誌は出版社のページ、CiNii 書誌、国立国会図書館サーチで照合し、診断の枠組みは、日本小児精神神経学会の公開資料（同ガイドラインを参考文献に挙げ、DSM の基準に準じた診断手順を示すもの）で実際に確認できた範囲に限った。評価尺度の個別の推奨や診断手順の細部は本文未確認のため含めていない。既存の DV-010 は DSM-5-TR の診断基準 A〜E の項目そのものを扱っており、本カードは国内ガイドラインの枠組みを示すもので、一部に重なりがある。
  curriculum:
    kokushi: 医学各論 Ⅱ-5-E（注意欠如多動性障害<注意欠如多動症><ADHD>、a）
    core_curriculum: 'PS-02-17-05 (id: JkxnuT8)；PS-02-12-04 (id: Jli53IM)；TBL-01-00-550 (id: Juyv-TM)；TBL-01-00-435 (id: JlvnmII)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: DV-022
  domain: DV
  subdomain: 注意欠如多動性障害<注意欠如多動症><ADHD>
  assertion:
    plain_statement_ja: 国内の診断・治療ガイドライン第5版に基づく注意欠如・多動症（ADHD）の治療・支援は、心理社会的治療から開始することが原則であり、環境調整、保護者へのガイダンスとペアレントトレーニング、学校など関係機関との連携、本人の特性に応じた療育や認知行動療法を含む。症状が強く周囲との関係が悪化する場合や、二次障害の恐れがある場合には、薬物療法を組み合わせる。国内で用いられる治療薬は、メチルフェニデート徐放錠、アトモキセチン、グアンファシン塩酸塩徐放錠、リスデキサンフェタミンの4剤である。
    condition:
      region: 日本
      対象: 小児および成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4445
    source: ADHDの診断・治療指針に関する研究会 編（齊藤万比古・飯田順三 編集）. 注意欠如・多動症―ADHD―の診断・治療ガイドライン 第5版. じほう. 2022年. ISBN 978-4-8407-5467-5
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: CC 表示なし（書籍）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: メチルフェニデート徐放錠、アトモキセチン、グアンファシン塩酸塩徐放錠、リスデキサンフェタミンはいずれも国内で注意欠如・多動症を適応として承認され、保険適用がある。このうちメチルフェニデート徐放錠とリスデキサンフェタミンは、ADHD 適正流通管理システムに登録した医師のみが処方できる。年齢による適応の範囲は薬剤ごとに異なるが、個別の年齢適応は本カードでは確認していない。本カードは書籍本文を直接確認できておらず、治療の枠組みは学会の公開資料で実際に確認できた範囲に限る。
  curriculum:
    kokushi: 医学各論 Ⅱ-5-E（注意欠如多動性障害<注意欠如多動症><ADHD>、a）
    core_curriculum: 'PS-02-17-05 (id: JkxnuT8)；PS-02-12-04 (id: Jli53IM)；TBL-01-00-550 (id: Juyv-TM)；TBL-01-00-435 (id: JlvnmII)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: FT-015
  domain: FT
  subdomain: 胎児貧血
  assertion:
    plain_statement_ja: 米国母体胎児医学会のガイドライン
    condition:
      region: 米国
      対象: 胎児貧血のリスクがある妊婦
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4446
    source: 'Society for Maternal-Fetal Medicine (SMFM); Mari G, Norton ME, Stone J, et al. Society for Maternal-Fetal Medicine (SMFM) Clinical Guideline #8: the fetus at risk for anemia--diagnosis and management. Am J Obstet Gynecol. 2015;212(6):697-710'
    doi: 10.1016/j.ajog.2015.01.059
    pmid: '25824811'
    pmcid: null
    url: https://doi.org/10.1016/j.ajog.2015.01.059
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 本ガイドラインは米国の学会のものであり、日本の産科ガイドラインで同じ閾値（MCA-PSV が中央値の1.5倍超）がどう位置づけられているかは別途の確認が要る。2015年の公表で、学会は2025年に現行として再確認（reaffirmed）している。推奨文には、妊娠週数が進み分娩のリスクが手技のリスクを下回る場合は分娩を優先する旨の留保がある。羊水の ΔOD450 は胎児貧血の診断に用いないことも同ガイドラインの推奨である。
  curriculum:
    kokushi: 医学各論 Ⅰ-3-A-④（胎児貧血、b）
    core_curriculum: 'PS-02-11-05 (id: JkxnuSU)；PS-02-11-03 (id: JkxnuSM)；TBL-02-10-013 (id: JlAKpqo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: FT-016
  domain: FT
  subdomain: 胎児貧血
  assertion:
    plain_statement_ja: 母体赤血球同種免疫で胎児貧血のリスクがある妊娠111例を対象に、中大脳動脈収縮期最大血流速度（MCA-PSV）と、臍帯穿刺で得た胎児ヘモグロビン値を比較した原著研究では、貧血のない例が41例、軽症が35例、中等症が4例、重症が31例（うち胎児水腫12例）だった。中等症と重症の貧血に対する MCA-PSV 上昇の感度は、水腫のない例でも100%（95%信頼区間 86〜100%）であり、偽陽性率は12%だった。正常胎児265例では、胎児ヘモグロビン値は妊娠週数とともに増加した。
    condition:
      region: 国際
      対象: 母体赤血球同種免疫のある妊婦
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-3348
    source: Mari G, Deter RL, Carpenter RL, et al.; Collaborative Group for Doppler Assessment of the Blood Velocity in Anemic Fetuses. Noninvasive diagnosis by Doppler ultrasonography of fetal anemia due to maternal red-cell alloimmunization. N Engl J Med. 2000;342(1):9-14
    doi: 10.1056/NEJM200001063420102
    pmid: '10620643'
    pmcid: null
    url: https://doi.org/10.1056/NEJM200001063420102
    source_license: CC 表示なし（NEJM）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 既存の FT-008 は同じ原著について「MCA-PSV の上昇は中等度・重度の胎児貧血を感度100%で予測し、偽陽性率は12%」という結論を既に扱っており、本カードは症例の内訳と推定の精度（信頼区間）を補う位置づけで、重複と判断されれば FT-008 への統合が望ましい。対象は同種免疫による貧血であり、他の原因による胎児貧血への外挿は本研究では検証されていない。管理の閾値である中央値の1.5倍という数値は本論文の抄録にはなく、FT-015（SMFM ガイドライン
  curriculum:
    kokushi: 医学各論 Ⅰ-3-A-④（胎児貧血、b）
    core_curriculum: 'PS-02-11-05 (id: JkxnuSU)；PS-02-11-03 (id: JkxnuSM)；TBL-02-10-013 (id: JlAKpqo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: SA-021
  domain: SA
  subdomain: 反応性関節炎
  assertion:
    plain_statement_ja: 反応性関節炎は、感染を契機として生じる炎症性関節炎であり、脊椎関節炎の一群に分類される。発症には、宿主の感受性と病原体の相互作用が関わると考えられている。診断は、先行する感染の後に生じる関節炎という合致する臨床症候群と、起因病原体の微生物学的確認に基づいて行う。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4447
    source: Schmitt SK. Reactive Arthritis. Infect Dis Clin North Am. 2017;31(2):265-277
    doi: 10.1016/j.idc.2017.01.002
    pmid: '28292540'
    pmcid: null
    url: https://doi.org/10.1016/j.idc.2017.01.002
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 反応性関節炎に特化した診療ガイドラインは、国際的にも国内にも存在せず、本カードは総説に基づく。起因病原体の個別の頻度や、HLA-B27 との関連の強さは、総説の抄録では確認できなかったため主張に入れていない。
  curriculum:
    kokushi: 医学各論 Ⅺ-2-B-②（末梢性脊椎関節炎、b）
    core_curriculum: 'PS-03-02-05 (id: JnGUA2s)；PS-01-03-28 (id: JkxnuM0)；TBL-01-00-576 (id: JlvnmVI)；TBL-02-17-009 (id: JlAKp10)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: SA-022
  domain: SA
  subdomain: 反応性関節炎
  assertion:
    plain_statement_ja: 反応性関節炎の治療では、クラミジアを契機とする例では抗菌薬が有用とされる一方、腸管病原体を契機とする例では抗菌薬の役割は明確でない。腫瘍壊死因子（TNF）阻害薬の位置づけは、まだ定まっていない。経過は数か月で収束する例が多いが、関節外の病変を伴ったり、経過が遷延したりする例もある。
    condition:
      region: 国際
      対象: 成人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4447
    source: Schmitt SK. Reactive Arthritis. Infect Dis Clin North Am. 2017;31(2):265-277
    doi: 10.1016/j.idc.2017.01.002
    pmid: '28292540'
    pmcid: null
    url: https://doi.org/10.1016/j.idc.2017.01.002
    source_license: CC 表示なし
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 反応性関節炎に特化した診療ガイドラインは存在せず、本カードは総説に基づく。抗 TNF 薬は国内では反応性関節炎を適応として承認されておらず、抗菌薬の使用は起因病原体ごとの感染症としての国内承認の範囲による。NSAIDs など対症療法の個別の位置づけは、総説の抄録では確認できなかったため本カードには含めていない。
  curriculum:
    kokushi: 医学各論 Ⅺ-2-B-②（末梢性脊椎関節炎、b）
    core_curriculum: 'PS-03-02-05 (id: JnGUA2s)；PS-01-03-28 (id: JkxnuM0)；TBL-01-00-576 (id: JlvnmVI)；TBL-02-17-009 (id: JlAKp10)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: HF-030
  domain: HF
  subdomain: 右心不全
  assertion:
    plain_statement_ja: 右心不全は、心臓の構造的または機能的な障害により、右室の充満や右室から前方への血液の拍出が障害される臨床症候群である。原因として最も頻度が高いのは左心不全による後方障害（左心疾患に伴う肺高血圧症）であり、そのほか機序別に、後負荷の増大（肺血栓塞栓症、慢性血栓塞栓性肺高血圧症、肺動脈性肺高血圧症、慢性肺疾患など）、収縮機能の低下（右室梗塞、心筋炎、不整脈原性右室心筋症など）、前負荷の異常（心タンポナーデ、左右シャント、三尖弁閉鎖不全など）、心膜疾患、調律の異常が挙げられる。症状・徴候は、前方障害による低灌流症状（全身倦怠感、運動耐容能の低下）と、後方障害による体うっ血（四肢の浮腫、腹部膨満、食欲低下、頸静脈圧の上昇、肝腫大、腹水など）に分けられる。
    condition:
      region: 日本
      対象: 右心不全の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J. 2025;89:1278-1444.
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 登録出典（英語版）の日本語版全文 PDF で確認した範囲であり、出典内の位置は第2章§3.2「右心不全」（25〜26頁）。原因の機序別分類と症状・徴候は同節の表9・表10から読み取った。肺高血圧症そのものの診断・治療の詳細は本カードの範囲外である。
  curriculum:
    kokushi: 医学各論 Ⅴ-2-A-②（右心不全、a）
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-157 (id: Jlvnlro)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: HF-031
  domain: HF
  subdomain: 右心不全
  assertion:
    plain_statement_ja: 右心不全の治療は原因となる病態生理によって異なり、体うっ血がある場合には特に利尿薬を用い、うっ血がない場合には慎重に輸液を行う。末梢の低灌流や持続する低血圧がある場合には強心薬を用い、それでも改善しなければ腎代替療法や右室補助人工心臓（RVAD）を含む機械的サポートを考慮する。
    condition:
      region: 日本
      対象: 右心不全の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-185
    source: Kitai T, Kohsaka S, Kato T, et al. JCS/JHFS 2025 Guideline on Diagnosis and Treatment of Heart Failure. Circ J. 2025;89:1278-1444.
    doi: 10.1253/circj.CJ-25-0002
    pmid: '40159241'
    pmcid: null
    url: https://doi.org/10.1253/circj.CJ-25-0002
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 登録出典（英語版）の日本語版全文 PDF で確認した範囲であり、出典内の位置は第2章§3.2「右心不全」（25〜26頁）。本カードの薬剤は利尿薬・強心薬という薬剤クラスの範囲の記述であり、当該節では個別の薬剤名は特定されていないため、個別薬剤の国内承認・保険適用の注記は行っていない。用量や薬剤の選択は原因疾患ごとの治療に委ねられる。
  curriculum:
    kokushi: 医学各論 Ⅴ-2-A-②（右心不全、a）
    core_curriculum: 'PS-02-06-05 (id: JkxnuQw)；TBL-01-00-157 (id: Jlvnlro)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: PE-038
  domain: PE
  subdomain: 先天性食道閉鎖症
  assertion:
    plain_statement_ja: 欧州の専門家コンセンサス（ERNICA）のフォローアップに関する合意では、先天性食道閉鎖症・気管食道瘻の術後は学際的なフォローアッププログラムで経過をみることが基本とされ、フォローアップで扱う25項目について合意が形成された（うち17項目は ESPGHAN-NASPGHAN の声明と一致）。体制面では、症例の集約化、多職種によるアプローチ、患者団体の関与が基本的な枠組みとされた。
    condition:
      region: 欧州
      対象: 小児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4448
    source: 'Dingemann C, Eaton S, Aksnes G, et al. ERNICA Consensus Conference on the Management of Patients with Esophageal Atresia and Tracheoesophageal Fistula: Follow-up and Framework. Eur J Pediatr Surg. 2020;30(6):475-482.'
    doi: 10.1055/s-0039-3400284
    pmid: '31777030'
    pmcid: null
    url: https://doi.org/10.1055/s-0039-3400284
    source_license: 購読誌（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 専門家コンセンサス文書であり、合意項目の根拠のエビデンスレベルは低いものが多い。主張は抄録で確認した合意の範囲に限り、個別項目の詳細は本文未確認のため含めていない。登録済みの ERNICA の診断・手術編（SRC-4395）とは別文献である。
  curriculum:
    kokushi: 医学各論 Ⅵ-12-A-①（先天性食道閉鎖症、b）
    core_curriculum: 'PS-02-12-04 (id: Jli53IM)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: PE-039
  domain: PE
  subdomain: 先天性食道閉鎖症
  assertion:
    plain_statement_ja: 食道閉鎖症・気管食道瘻の小児では、術後の長期合併症として胃食道逆流、嚥下障害、吻合部狭窄、哺乳・摂食の困難などがみられ、ESPGHAN-NASPGHAN のガイドラインはこれらの消化器・栄養面の合併症の評価と治療を36の臨床課題として扱っている。症状のある例では好酸球性食道炎や合併する消化管奇形を除外することも求められ、生活の質への配慮と、成人診療への系統的な移行も課題に含まれる。
    condition:
      region: 国際
      対象: 小児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4449
    source: Krishnan U, Mousa H, Dall'Oglio L, et al. ESPGHAN-NASPGHAN Guidelines for the Evaluation and Treatment of Gastrointestinal and Nutritional Complications in Children With Esophageal Atresia-Tracheoesophageal Fistula. J Pediatr Gastroenterol Nutr. 2016;63(5):550-570.
    doi: 10.1097/MPG.0000000000001401
    pmid: '27579697'
    pmcid: null
    url: https://doi.org/10.1097/MPG.0000000000001401
    source_license: 購読誌（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガイドラインの文献検索は2014年3月までであり、それ以降の改訂版は確認できなかったため、現行の最新版として扱った。主張は抄録で確認した臨床課題の範囲に限り、個別の推奨の強さや治療の細目は本文未確認のため含めていない。
  curriculum:
    kokushi: 医学各論 Ⅵ-12-A-①（先天性食道閉鎖症、b）
    core_curriculum: 'PS-02-12-04 (id: Jli53IM)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: PE-040
  domain: PE
  subdomain: 鼠径ヘルニア
  assertion:
    plain_statement_ja: 小児の鼠径ヘルニアに対する腹腔鏡下経皮的腹膜外閉鎖法（LPEC）は、臍部から腹腔鏡を挿入し、専用の針で内鼠径輪を腹膜外に周回縫合して閉鎖する手技である。日本の3施設で生後18日から19歳の711例・972件に行われた報告では、手術時間は片側・両側とも10〜30分で、術中合併症はなく、経過観察5か月〜10年での再発率は0.73%であり、術後の精索水腫・精巣萎縮もみられなかった。
    condition:
      region: 日本
      対象: 小児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4450
    source: 'Takehara H, Yakabe S, Kameoka K. Laparoscopic percutaneous extraperitoneal closure for inguinal hernia in children: clinical outcome of 972 repairs done in 3 pediatric surgical institutions. J Pediatr Surg. 2006;41(12):1999-2003.'
    doi: 10.1016/j.jpedsurg.2006.08.032
    pmid: '17161191'
    pmcid: null
    url: https://doi.org/10.1016/j.jpedsurg.2006.08.032
    source_license: 購読誌（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 開発施設を含む日本の3施設の症例集積であり、比較試験ではないため、他の術式との優劣はこの出典からは言えない。数値は抄録で確認した範囲である。
  curriculum:
    kokushi: 医学各論 Ⅵ-12-G-①（鼠径ヘルニア、a）
    core_curriculum: 'PS-02-12-04 (id: Jli53IM)；TBL-01-00-425 (id: JlvnmHI)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: NL-022
  domain: NL
  subdomain: 鼻炎
  assertion:
    plain_statement_ja: 花粉症は、花粉抗原による季節性アレルギー性鼻炎であり、アレルギー性結膜炎を合併することが多い。2019年の全国疫学調査では、アレルギー性鼻炎全体の有病率は49.2%で、2008年の39.4%から増加した。花粉症全体の有病率は42.5%、スギ花粉症は38.8%であり、スギ花粉症は1998年の16.2%、2008年の26.5%から増加が続いている。年齢別では、5歳以上のすべての年齢層でスギ花粉症が最も多く、0〜4歳でのみ通年性アレルギー性鼻炎が最多である。
    condition:
      region: 日本
      対象: 一般住民
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-2825
    source: 松原篤、坂下雅文、後藤穣、ほか. 2019年全国疫学調査（鼻アレルギー）. 日本耳鼻咽喉科学会会報. 2020;123:485-490.
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 未確認（日本語誌）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値は2019年全国疫学調査（松原ほか、2020）の抄録と公表資料で確認した値で、質問紙調査に基づく。旧カード（NL-004）にあった年齢別の記述（通年性アレルギー性鼻炎は若年層に多く、スギ花粉症は中年層に多い）は2019年調査の結果と合わないため引き継いでいない。2020年以降の全国調査による有病率の更新は未確認である。
  curriculum:
    kokushi: 医学各論 Ⅲ-9-A-②（鼻炎、a）
    core_curriculum: 'PS-02-16-05 (id: JkxnuTo)；TBL-01-00-511 (id: JlvnmQA)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: SK-033
  domain: SK
  subdomain: 遺伝性血管性浮腫
  assertion:
    plain_statement_ja: 遺伝性血管性浮腫のうち、C1インヒビターの欠損または機能不全によるものは HAE-C1-INH と分類され、従来の1型・2型はこの分類に統合された。C1インヒビターが正常な型は HAE-nC1-INH として整理される。WAO の2025年ガイドラインでは、発作に対しては静脈内C1インヒビター製剤、イカチバント、または経口のセベトラルスタットによる早期のオンデマンド治療が第一選択とされ、早期に治療するほど速やかに改善する。エカランタイドも有効な発作時治療薬とされる。上気道に及ぶ発作は特に速やかな治療を要する。長期予防の第一選択としては、皮下C1インヒビター製剤、ラナデルマブ、ベロトラルスタット、ガラダシマブ、ドニダロルセンが選択肢となり、治療目標は完全な疾患コントロールとされる。
    condition:
      region: 国際
      対象: 遺伝性血管性浮腫の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-3092
    source: Vázquez DO, Giavina-Bianchi P, Josviack D, et al. The 2025 WAO Guidelines for the classification, diagnosis, and treatment of hereditary angioedema, with consideration of worldwide disparities. World Allergy Organ J. 2026;19(5):101335.
    doi: 10.1016/j.waojou.2026.101335
    pmid: '42165046'
    pmcid: PMC13184495
    url: https://doi.org/10.1016/j.waojou.2026.101335
    source_license: CC BY-NC-ND 4.0（Crossref で確認）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: ガラダシマブ（アナエブリ）は2025年2月20日に、セベトラルスタット（エクテリー錠300mg）は2025年12月22日に国内承認され、セベトラルスタットは2026年3月18日に薬価収載・発売された。セベトラルスタットの国内の承認用量は1回300mg（2時間以上あけて追加300mgまで）で、WAO 2025 本文の用量表記（600mg）とは異なる。ドニダロルセンは米国・EUで承認済みだが国内では未承認（開発中）である。エカランタイドは国内未承認である。静脈内および皮下のC1インヒビター製剤、イカチバント、ラナデルマブ、ベロトラルスタットは国内で承認されている。HAE-nC1-INH の遺伝子型ごとの細目は本カードには含めていない。
  curriculum:
    kokushi: 医学各論 Ⅲ-1-B-①（血管性浮腫、a）
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ND-057
  domain: ND
  subdomain: 多発性硬化症
  assertion:
    plain_statement_ja: 2024年改訂McDonald基準では、典型的な clinically isolated syndrome を呈し空間的多発が臨床的またはMRIで示される患者では、髄液特異的オリゴクローナルバンドの存在、またはκ遊離軽鎖指数の陽性をもって時間的多発を代替し、多発性硬化症と診断できる。
    condition:
      region: 国際
      対象: clinically isolated syndromeを呈する患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4433
    source: 'Montalban X, Lebrun-Frénay C, Oh J, et al. Diagnosis of multiple sclerosis: 2024 revisions of the McDonald criteria. Lancet Neurol. 2025;24(10):850-865.'
    doi: 10.1016/S1474-4422(25)00270-4
    pmid: '40975101'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(25)00270-4
    source_license: 購読誌（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 旧カード（ND-050、2017年改訂基準）の主張は2024年改訂でも維持され、髄液陽性の定義にκ遊離軽鎖指数が加わった形で書き換えた。κ遊離軽鎖指数の具体的なカットオフ値など細部は、基準論文の本文（購読制）で確認できていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-4-H-①（多発性硬化症、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-036 (id: JlvnldE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ND-058
  domain: ND
  subdomain: 多発性硬化症
  assertion:
    plain_statement_ja: 2024年改訂McDonald基準では、空間的多発の評価部位に視神経が第5の部位として加わった。空間的多発は、脳室周囲、皮質・皮質近傍、テント下、脊髄、視神経の5部位のうち2部位以上に病変が示されることで満たされる。視神経病変は、眼窩MRI、光干渉断層撮影（OCT）、視覚誘発電位（VEP）で評価できる。
    condition:
      region: 国際
      対象: 多発性硬化症が疑われる患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4433
    source: 'Montalban X, Lebrun-Frénay C, Oh J, et al. Diagnosis of multiple sclerosis: 2024 revisions of the McDonald criteria. Lancet Neurol. 2025;24(10):850-865.'
    doi: 10.1016/S1474-4422(25)00270-4
    pmid: '40975101'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(25)00270-4
    source_license: 購読誌（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 視神経を第5の部位とすることと評価法（MRI・OCT・VEP）は、基準論文の抄録と解説で確認した。評価法ごとの判定の細部は基準論文の本文（購読制）で確認できていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-4-H-①（多発性硬化症、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-036 (id: JlvnldE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ND-059
  domain: ND
  subdomain: 多発性硬化症
  assertion:
    plain_statement_ja: 2024年改訂McDonald基準では、診断経路が拡張された。典型的な臨床像で空間的多発の5部位中4部位以上に病変がある場合は、時間的多発の証明なしに多発性硬化症と診断できる。clinically isolated syndrome では、髄液陽性と central vein sign、髄液陽性と paramagnetic rim lesion、時間的多発と central vein sign、時間的多発と paramagnetic rim lesion の各組み合わせでも、再発寛解型多発性硬化症と診断できる。
    condition:
      region: 国際
      対象: 多発性硬化症が疑われる患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4433
    source: 'Montalban X, Lebrun-Frénay C, Oh J, et al. Diagnosis of multiple sclerosis: 2024 revisions of the McDonald criteria. Lancet Neurol. 2025;24(10):850-865.'
    doi: 10.1016/S1474-4422(25)00270-4
    pmid: '40975101'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(25)00270-4
    source_license: 購読誌（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 4部位以上の場合に時間的多発を要しないことは基準論文の抄録で確認した。各組み合わせの適用条件の細部は解説・総説で確認した範囲であり、基準論文の本文（購読制）の照合はしていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-4-H-①（多発性硬化症、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-036 (id: JlvnldE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ND-060
  domain: ND
  subdomain: 多発性硬化症
  assertion:
    plain_statement_ja: 2024年改訂McDonald基準では、放射線学的孤立症候群（radiologically isolated syndrome）でも多発性硬化症と診断できるようになった。空間的多発を満たしたうえで、central vein sign、髄液陽性（オリゴクローナルバンドまたはκ遊離軽鎖指数の陽性）、時間的多発のいずれかを伴う場合に診断できる。
    condition:
      region: 国際
      対象: 放射線学的孤立症候群の患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4433
    source: 'Montalban X, Lebrun-Frénay C, Oh J, et al. Diagnosis of multiple sclerosis: 2024 revisions of the McDonald criteria. Lancet Neurol. 2025;24(10):850-865.'
    doi: 10.1016/S1474-4422(25)00270-4
    pmid: '40975101'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(25)00270-4
    source_license: 購読誌（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 放射線学的孤立症候群で診断できることと付帯条件の組み合わせは、基準論文の抄録と解説で確認した。central vein sign の個数の基準など適用条件の細部は解説経由の確認であり、基準論文の本文（購読制）の照合はしていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-4-H-①（多発性硬化症、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-036 (id: JlvnldE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
- id: ND-061
  domain: ND
  subdomain: 多発性硬化症
  assertion:
    plain_statement_ja: 2024年改訂McDonald基準では、central vein sign と paramagnetic rim lesions が、多発性硬化症の特異度を高める補助所見として位置づけられた。central vein sign の陽性は、中心静脈を伴う病変が6個以上あること（Select-6）で判定する。
    condition:
      region: 国際
      対象: 多発性硬化症が疑われる患者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4433
    source: 'Montalban X, Lebrun-Frénay C, Oh J, et al. Diagnosis of multiple sclerosis: 2024 revisions of the McDonald criteria. Lancet Neurol. 2025;24(10):850-865.'
    doi: 10.1016/S1474-4422(25)00270-4
    pmid: '40975101'
    pmcid: null
    url: https://doi.org/10.1016/S1474-4422(25)00270-4
    source_license: 購読誌（CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 補助所見としての位置づけは基準論文の抄録と解説で確認した。Select-6 の「6個以上」という判定の数値は解説経由の確認であり、基準論文の本文（購読制）の照合はしていない。
  curriculum:
    kokushi: 医学各論 Ⅸ-4-H-①（多発性硬化症、b）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-036 (id: JlvnldE)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応の一覧

| カードID | 出題基準 | コアカリ |
|---|---|---|
| IN-111 | 医学各論 Ⅵ-3-B-⑥（放射線性腸炎、c） | PS-02-08-05 (id: JkxnuRY) |
| IN-112 | 医学各論 Ⅵ-3-C-③（小腸癌、c） | PS-02-08-05 (id: JkxnuRY)；PS-03-04-14 (id: JkxnuYE) |
| IN-113 | 医学各論 Ⅵ-5-E-②（毛細血管拡張症<angioectasia>、c） | PS-02-08-05 (id: JkxnuRY) |
| LV-111 | 医学各論 Ⅵ-6-A-①（肝囊胞、c） | PS-02-08-05 (id: JkxnuRY) |
| AB-116 | 医学各論 Ⅵ-9-C-④（後腹膜腫瘍、c） | PS-02-08-05 (id: JkxnuRY)；PS-03-04-14 (id: JkxnuYE) |
| MP-040 | 医学各論 Ⅴ-6-G-①（心臓外傷、c） | PS-02-06-05 (id: JkxnuQw)；PS-03-05-12 (id: Jkxir3g) |
| MP-041 | 医学各論 Ⅴ-6-G-①（心臓外傷、c） | PS-02-06-05 (id: JkxnuQw)；PS-03-05-12 (id: Jkxir3g) |
| MP-042 | 医学各論 Ⅴ-6-G-①（心臓外傷、c） | PS-02-06-05 (id: JkxnuQw)；PS-03-05-12 (id: Jkxir3g) |
| DV-021 | 医学各論 Ⅱ-5-E（注意欠如多動性障害<注意欠如多動症><ADHD>、a） | PS-02-17-05 (id: JkxnuT8)；PS-02-12-04 (id: Jli53IM)；TBL-01-00-550 (id: Juyv-TM)；TBL-01-00-435 (id: JlvnmII) |
| DV-022 | 医学各論 Ⅱ-5-E（注意欠如多動性障害<注意欠如多動症><ADHD>、a） | PS-02-17-05 (id: JkxnuT8)；PS-02-12-04 (id: Jli53IM)；TBL-01-00-550 (id: Juyv-TM)；TBL-01-00-435 (id: JlvnmII) |
| FT-015 | 医学各論 Ⅰ-3-A-④（胎児貧血、b） | PS-02-11-05 (id: JkxnuSU)；PS-02-11-03 (id: JkxnuSM)；TBL-02-10-013 (id: JlAKpqo) |
| FT-016 | 医学各論 Ⅰ-3-A-④（胎児貧血、b） | PS-02-11-05 (id: JkxnuSU)；PS-02-11-03 (id: JkxnuSM)；TBL-02-10-013 (id: JlAKpqo) |
| SA-021 | 医学各論 Ⅺ-2-B-②（末梢性脊椎関節炎、b） | PS-03-02-05 (id: JnGUA2s)；PS-01-03-28 (id: JkxnuM0)；TBL-01-00-576 (id: JlvnmVI)；TBL-02-17-009 (id: JlAKp10) |
| SA-022 | 医学各論 Ⅺ-2-B-②（末梢性脊椎関節炎、b） | PS-03-02-05 (id: JnGUA2s)；PS-01-03-28 (id: JkxnuM0)；TBL-01-00-576 (id: JlvnmVI)；TBL-02-17-009 (id: JlAKp10) |
| HF-030 | 医学各論 Ⅴ-2-A-②（右心不全、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-157 (id: Jlvnlro) |
| HF-031 | 医学各論 Ⅴ-2-A-②（右心不全、a） | PS-02-06-05 (id: JkxnuQw)；TBL-01-00-157 (id: Jlvnlro) |
| PE-038 | 医学各論 Ⅵ-12-A-①（先天性食道閉鎖症、b） | PS-02-12-04 (id: Jli53IM) |
| PE-039 | 医学各論 Ⅵ-12-A-①（先天性食道閉鎖症、b） | PS-02-12-04 (id: Jli53IM) |
| PE-040 | 医学各論 Ⅵ-12-G-①（鼠径ヘルニア、a） | PS-02-12-04 (id: Jli53IM)；TBL-01-00-425 (id: JlvnmHI) |
| NL-022 | 医学各論 Ⅲ-9-A-②（鼻炎、a） | PS-02-16-05 (id: JkxnuTo)；TBL-01-00-511 (id: JlvnmQA) |
| SK-033 | 医学各論 Ⅲ-1-B-①（血管性浮腫、a） | PS-02-04-05 (id: JkxnuQI) |
| ND-057 | 医学各論 Ⅸ-4-H-①（多発性硬化症、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-036 (id: JlvnldE) |
| ND-058 | 医学各論 Ⅸ-4-H-①（多発性硬化症、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-036 (id: JlvnldE) |
| ND-059 | 医学各論 Ⅸ-4-H-①（多発性硬化症、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-036 (id: JlvnldE) |
| ND-060 | 医学各論 Ⅸ-4-H-①（多発性硬化症、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-036 (id: JlvnldE) |
| ND-061 | 医学各論 Ⅸ-4-H-①（多発性硬化症、b） | PS-02-03-05 (id: JkxnuP0)；TBL-01-00-036 (id: JlvnldE) |

## 4. 未解決事項

- IN-111（放射線性腸炎）：手術の合併症・再手術の頻度は出典の抄録に数値がなく、主張には入れていない（総説本文の記述のみ）
- IN-112（小腸癌）：登録出典は Version 1.2020 で現行は Version 2.2026。現行版の内容までカードに含めるかは登録側の判断事項。マスターの SRC-4214 は PMID が null で、カード側には PubMed で確認した 31487687 を記載した（ほかの既存出典も同様：SRC-4215 は 19897345、SRC-4226 は 26303132、SRC-4227 は 35728731、SRC-3092 は 42165046、SRC-3348 は 10620643、SRC-4395 は 31266084。いずれも DOI 一致で確認した値で、マスター補完の候補）
- DV-021・022（ADHD）：ガイドライン第5版の書籍本文の直接確認ができていない。書籍で照合できれば、主張の範囲を広げられる
- ND-058〜061（McDonald 2024 の追加カード）：論文本文（購読制）は未照合で、κ遊離軽鎖指数のカットオフ値と追加カードの適用条件の細部は確定できていない。確認経路は各カードの uncertainty に記載した
- PE-038・039（食道閉鎖症フォローアップ）：抄録で確認した範囲に限定した。個別推奨の細目（噴門形成の適応等）と気管軟化症の管理は本文確認後の拡張候補
- HF-031（右心不全の治療）：出典の当該節は薬剤名を特定していないため、薬剤クラスの範囲の記述とし、個別の承認注記は行っていない旨を uncertainty に明記した

## 5. 次回への引き継ぎ

- 旧カードとの対応：NL-022 は NL-004 の、SK-033 は SK-013 の、ND-057 は ND-050 の書き換え（ND-058〜061 は同じ項目の追加カード）。旧カードの廃止と superseded_by の記録は取り込み側で行う想定
- HF-030・031（右心不全）は HF-026 と主題が重なる。HF-026 を廃止するかは取り込み側の判断（依頼文の登録時決定5）。なお HF-030・031 の主題は HF-027〜029（AHA 科学声明）とも重なるが、出典は異なる
- PE-037 の uncertainty には Takehara 2006 への言及があり、PE-040 ができたため参照への書き換えを検討されたい
- 穿通性心臓外傷の WTA 2012（Burlew）は今回出典登録しなかった。開胸の判断を別の角度で追加する場合は MP-043 としての追加が可能
- 追加を見送った McDonald 2024 の新要素（50歳以上での追加の裏付け、統一フレームワーク、進行型での脊髄病変の扱い）は、総説レベルの確認にとどまったため作らなかった。本文照合ができれば追加候補になる
- 扱った出典：新規10件（SRC-4441〜4450）と既存9件（SRC-4215・4214・4226・4227・3348・185・2825・3092・4433）。ERNICA のフォローアップ編（SRC-4448）は、登録済みの診断・手術編（SRC-4395）とは別文献
