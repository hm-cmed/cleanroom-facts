# 第61回 パート2（提案D：心臓外傷・ADHD・胎児貧血・反応性関節炎）

担当：穿通性心臓外傷（MP-040〜042）、ADHD（DV-021〜022）、胎児貧血（FT-015〜016）、反応性関節炎（SA-021〜022）の計9件。

出典の仮番号（SRC-9201〜9207）は組み立て時に正式番号（SRC-4441〜4520 の範囲）へ振り直す前提の作業用番号。Mari 2000 は既存の SRC-3348 をそのまま使う。Burlew 2012（WTA、仮 SRC-9202）は独立カードにせず未使用とした（理由は引き継ぎメモ）。

## 1. 出典表

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-3348（既存） | Mari G, Deter RL, Carpenter RL, et al.; Collaborative Group for Doppler Assessment of the Blood Velocity in Anemic Fetuses. Noninvasive diagnosis by Doppler ultrasonography of fetal anemia due to maternal red-cell alloimmunization. N Engl J Med. 2000;342(1):9-14 | 10.1056/NEJM200001063420102 | 10620643 | CC 表示なし（NEJM） | RESTRICTED | 既存登録（マスターの記載）。数値は PubMed 抄録で再確認 |
| SRC-9201 | Seamon MJ, Haut ER, Van Arendonk K, et al. An evidence-based approach to patient selection for emergency department thoracotomy: A practice management guideline from the Eastern Association for the Surgery of Trauma. J Trauma Acute Care Surg. 2015;79(1):159-173 | 10.1097/TA.0000000000000648 | 26091330 | CC 表示なし（購読誌） | RESTRICTED | PubMed 抄録で推奨文と生存率を確認。Crossref にライセンス表示なし |
| SRC-9203 | Hromalik LR Jr, Wall MJ Jr, Mattox KL, Tsai PI. Penetrating cardiac injury: a narrative review. Mediastinum. 2023;7:15 | 10.21037/med-22-18 | 37261091 | CC BY-NC-ND 4.0（本文の Open Access Statement） | RESTRICTED | PMC 全文（PMC10226890）でライセンス表示と本文を確認 |
| SRC-9204 | Ball CG, Lee A, Kaminsky M, et al. Technical considerations in the management of penetrating cardiac injury. Can J Surg. 2022;65(5):E580-E592 | 10.1503/cjs.008521 | 36302130 | CC BY-NC-ND 4.0（本文のライセンス表示） | RESTRICTED | PMC 全文（PMC9451503）でライセンス表示と本文を確認 |
| SRC-9205 | ADHDの診断・治療指針に関する研究会 編（齊藤万比古・飯田順三 編集）. 注意欠如・多動症―ADHD―の診断・治療ガイドライン 第5版. じほう. 2022年. ISBN 978-4-8407-5467-5 | なし（書籍） | なし（書籍） | CC 表示なし（書籍） | RESTRICTED | 出版社ページ・CiNii 書誌・国立国会図書館サーチで書誌と ISBN を照合。本文は未確認（主張の範囲は引き継ぎメモ参照） |
| SRC-9206 | Society for Maternal-Fetal Medicine (SMFM); Mari G, Norton ME, Stone J, et al. Society for Maternal-Fetal Medicine (SMFM) Clinical Guideline #8: the fetus at risk for anemia--diagnosis and management. Am J Obstet Gynecol. 2015;212(6):697-710 | 10.1016/j.ajog.2015.01.059 | 25824811 | CC 表示なし | RESTRICTED | PubMed 抄録で推奨文（7項目）を確認。学会の公式ページで2025年に reaffirmed と確認 |
| SRC-9207 | Schmitt SK. Reactive Arthritis. Infect Dis Clin North Am. 2017;31(2):265-277 | 10.1016/j.idc.2017.01.002 | 28292540 | CC 表示なし | RESTRICTED | PubMed 抄録で確認。Crossref のライセンスはテキストマイニング用のみ |

## 2. 事実票 YAML

```yaml
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
    source_ref: SRC-9203
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
    source_ref: SRC-9201
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
    source_ref: SRC-9204
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
    source_ref: SRC-9205
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
    source_ref: SRC-9205
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
    plain_statement_ja: 米国母体胎児医学会のガイドライン #8 では、胎児貧血を検出する第一の手段は中大脳動脈収縮期最大血流速度（MCA-PSV）のドプラ計測であり、計測は中大脳動脈の起始部近くで、角度を0度に近づけ、角度補正をせずに行う。MCA-PSV が中央値の1.5倍を超える場合、または胎児水腫を認める場合は、重症胎児貧血の可能性が高いとして、子宮内輸血の準備をしたうえで胎児採血を行い、侵襲的胎児治療の専門施設へ紹介する。2回目の子宮内輸血の時期の判断にも MCA-PSV を用いることができ、胎児貧血のリスクが高い妊娠は、ほかに適応がなければ妊娠37〜38週で分娩とする。
    condition:
      region: 米国
      対象: 胎児貧血のリスクがある妊婦
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-9206
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
  uncertainty: 既存の FT-008 は同じ原著について「MCA-PSV の上昇は中等度・重度の胎児貧血を感度100%で予測し、偽陽性率は12%」という結論を既に扱っており、本カードは症例の内訳と推定の精度（信頼区間）を補う位置づけで、重複と判断されれば FT-008 への統合が望ましい。対象は同種免疫による貧血であり、他の原因による胎児貧血への外挿は本研究では検証されていない。管理の閾値である中央値の1.5倍という数値は本論文の抄録にはなく、FT-015（SMFM ガイドライン #8）の範囲である。
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
    source_ref: SRC-9207
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
    source_ref: SRC-9207
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
```

## 3. 引き継ぎメモ

- **件数**：9件（MP 3件、DV 2件、FT 2件、SA 2件）。
- **仮番号の対応**：SRC-9201＝Seamon 2015、SRC-9203＝Hromalik 2023、SRC-9204＝Ball 2022、SRC-9205＝ADHD ガイドライン第5版、SRC-9206＝SMFM #8、SRC-9207＝Schmitt 2017。組み立て時に SRC-4441〜4520 の正式番号へ振り直すこと。
- **SRC-9202（Burlew 2012、WTA）は未使用**：救急室開胸は EAST（Seamon 2015）のカード MP-041 に一本化した（1カード1文献の原則と、両者の推奨枠組みがほぼ重なるため）。WTA を独立カードにする場合は MP-043 として追加できる。
- **ライセンス確定**：Hromalik 2023 と Ball 2022 は PMC 全文で本文表示を確認し、いずれも CC BY-NC-ND 4.0 であったため source_class は RESTRICTED とした（当初案の UNKNOWN ではない）。
- **FT-016 の重複注意**：既存の FT-008（同じ Mari 2000、SRC-3348）が感度・偽陽性率の結論を既に扱っている。FT-016 は症例内訳（111例の重症度分布）と95%信頼区間を補う範囲に絞ったが、受け入れ検査で重複と判断されれば FT-008 への統合または FT-016 の見送りが妥当。その場合、胎児貧血パートは FT-015 の1件になる。
- **DV の重複注意**：DV-010 は DSM-5-TR の診断基準 A〜E そのものを扱う。DV-021 は国内ガイドライン第5版の「枠組み」（症状領域・経過・場面の要件と総合的評価）に絞り、症状項目数（9項目中6つ以上）などの数値は DV-021 に入れなかった。
- **ADHD 本の制約**：書籍本文は直接確認できていない。主張は、日本小児精神神経学会の公開資料（第5版を参考文献に挙げる文書を実際に開いて確認）の範囲に限定し、その旨を両カードの uncertainty に明記した。評価尺度の推奨度など本文の細部は未確認。
- **SMFM の地域**：FT-015 の region は米国とした。日本の産科ガイドラインでの MCA-PSV 閾値の位置づけは未確認で、uncertainty にその旨を書いた。
- **薬剤の注記**：薬剤名のあるカードは DV-022（4剤の国内承認・保険適用・流通管理の別）と SA-022（抗 TNF 薬は反応性関節炎の適応では国内未承認、抗菌薬は感染症としての承認範囲による）。MP・FT のカードに薬剤名はない。
- **数値の確認範囲**：MP-041 の生存率（21.3%・8.3%）と対象数（10,238例）、FT-016 の感度・偽陽性率・症例内訳は、いずれも PubMed 抄録で確認した。MP-040 の心エコーの精度（96〜97%）と Beck の三徴の頻度（約10%）は PMC 全文で確認した。
