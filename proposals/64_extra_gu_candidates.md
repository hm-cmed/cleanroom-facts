# 第64回 対象外カード（別ファイル分離分）

第64回の登録対象（22項目）ではない2件。作り手側の担当割り当ての誤りで作成されたため、本編（64_brushup_a.md）には入れず分離した。将来の回の候補として使える。

注意：下記の ID（GU-040・GU-041）は仮のもので、本編の GU-040（包茎）・GU-041（精巣・精索水瘤）とは別物であり番号が重なっている。取り込み時は新規に採番すること。精索静脈瘤の出典 SRC-9713 は仮番号（未登録）。

## 出典

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-742 | Morris BJ, Krieger JN. Penile Inflammatory Skin Disorders and the Preventive Role of Circumcision. Int J Prev Med. 2017;8:32 | 10.4103/ijpvm.IJPVM_377_16 | 28567234 | CC BY-NC-SA 3.0（PMC 掲載ページの表示） | RESTRICTED | |
| SRC-9713 | Lomboy JR, Coward RM. The Varicocele: Clinical Presentation, Evaluation, and Surgical Management. Semin Intervent Radiol. 2016;33(3):163-169 | 10.1055/s-0036-1586143 | 27582602 | © Thieme Medical Publishers（CC の表示なし） | RESTRICTED | |

## 事実カード（YAML）

```yaml
- id: GU-040
  domain: GU
  subdomain: 亀頭包皮炎
  assertion:
    plain_statement_ja: 亀頭包皮炎は亀頭と包皮の炎症であり、亀頭のみの炎症を亀頭炎、包皮のみの炎症を包皮炎という。最も多い原因は衛生不良であり、感染性の原因では真菌（最も多い分離菌は Candida albicans）が最も多く、細菌（レンサ球菌属など）がこれに次ぐ。一部の抗菌薬、ラテックス、殺精子剤などの薬剤・物質による刺激性・アレルギー性の包皮炎もある。臨床像は、亀頭の軽い灼熱感や掻痒、腫脹、紅斑性の斑・局面・水疱、びらんした衛星膿疱、湿った凝乳様の堆積物であり、糖尿病患者や免疫不全患者では重症化しやすい。未割礼の男性に多く（有病率は未割礼で11〜13%、割礼済みで2%）、陰茎の炎症自体が後天性包茎の原因にもなりうる。治療は、非特異的な亀頭包皮炎には局所の衛生管理を行い、カンジダ性には外用抗真菌薬を用いる（再発は多く、特に包茎や糖尿病がある場合に多い）。再発予防の根治的な治療は包皮環状切除である。
    condition:
      region: 国際
      study: 陰茎の炎症性皮膚疾患と割礼の予防的役割に関する総説
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-742
    source: Morris BJ, Krieger JN. Penile Inflammatory Skin Disorders and the Preventive Role of Circumcision. Int J Prev Med. 2017;8:32
    doi: 10.4103/ijpvm.IJPVM_377_16
    pmid: '28567234'
    pmcid: PMC5439293
    url: https://doi.org/10.4103/ijpvm.IJPVM_377_16
    source_license: CC BY-NC-SA 3.0（PMC 掲載ページの表示）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 薬剤は薬剤群（外用抗真菌薬）としての記載である。国内では皮膚真菌症に対して承認・保険適用のあるイミダゾール系の外用抗真菌薬などが用いられ、個別製剤の効能・効果の範囲は添付文書による。出典マスター（SRC-742）では PMCID が未登録だが、PubMed レコードで PMC5439293 を確認したため本カードに記載した（マスター側の補完候補）。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)'
    kokushi: null
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: GU-041
  domain: GU
  subdomain: 精索静脈瘤
  assertion:
    plain_statement_ja: 精索静脈瘤は、精索の蔓状静脈叢の異常な拡張と蛇行であり、男性人口の約15%にみられ、男性因子不妊の最も多い修復可能な原因である。多くは無症状で、成人では男性不妊の評価の過程で、思春期では診察で偶然に発見されることが多く、陰嚢の不快感を訴える場合もある。診断の標準は立位での視診・触診（安静時とバルサルバ負荷時、暖かい部屋で）であり、重症度は、触知も視認もできず画像でのみ確認できるものを潜在性、バルサルバ負荷時のみ触知できるものをグレードI、立位で触知できるが視認できないものをグレードII、立位で大きく視認できるものをグレードIIIと分類する。左側に多く（左精巣静脈は抵抗の高い左腎静脈に流入するため）、孤立性の右側例や臥位で消失しない例では後腹膜病変の検索が必要である。治療を検討するのは、触知可能な静脈瘤があり、不妊のカップルが挙児を試みており、女性パートナーの妊孕性が正常または治療可能で、男性パートナーの精液所見に異常がある場合であり、触知できない潜在性の静脈瘤の治療は妊娠率を改善しない。疼痛も治療の適応となりうるが、精巣上体炎や腫瘤、ヘルニアなど他の原因の除外が前提である。思春期では、触知可能な静脈瘤に精巣容量の左右差が20%を超える場合などが治療検討の指標となる。治療は内精静脈の逆流を遮断する経皮的塞栓術・硬化療法または外科的切除であり、顕微鏡下の鼠径部・鼠径下アプローチは再発率と術後水腫の発生率が最も低い。
    condition:
      region: 米国
      study: 精索静脈瘤の臨床像・評価・外科的管理に関する総説（Seminars in Interventional Radiology、2016年）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-9713
    source: 'Lomboy JR, Coward RM. The Varicocele: Clinical Presentation, Evaluation, and Surgical Management. Semin Intervent Radiol. 2016;33(3):163-169'
    doi: 10.1055/s-0036-1586143
    pmid: '27582602'
    pmcid: PMC5005075
    url: https://doi.org/10.1055/s-0036-1586143
    source_license: © Thieme Medical Publishers（CC の表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: グレード分類は出典の表（Dubin & Amelar 分類、Table 1）から読み取り、思春期の精巣容量差20%の指標も出典の表（Table 3）から読み取った。治療後の疼痛消失率（83〜92%）は総説が引用する個別研究の値のため主張には含めていない。本カードは米国の総説に基づくものであり、国内の診療の実情とは異なる場合がある。
  curriculum:
    core_curriculum: 'PS-02-10-05 (id: JkxnuSA)；TBL-01-00-350 (id: JlvnmAI)；TBL-01-00-346 (id: Jlvnl_w)'
    kokushi: 医学各論 Ⅷ-10-B-⑤（精索静脈瘤、a）
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```
