# 第65回 別ファイル分離分：EP-046（欠神発作の治療）

欠神発作の治療として起案したが、治療成績の内容が既存の EP-007・EP-008（医学各論 Ⅸ-6-A-②、小児欠神てんかんの Glauser ら 2010 の比較試験）と実質的に重なるため、本編（65_brushup_a.md）には入れなかった。分野をまたぐ項目の扱いに照らした本来の形は、EP-007・EP-008 へ Ⅸ-11-C-② の番号を追加することであり、その判断材料として本起案を残す。出典は既存の SRC-1705（再利用）で、新規の SRC 番号は使っていない。

## 事実カード（YAML）

```yaml
- id: EP-046
  domain: EP
  subdomain: 欠神発作
  assertion:
    plain_statement_ja: 新たに小児欠神てんかんと診断された小児453例を対象とした二重盲検無作為化比較試験では、16週時点の治療失敗なしの割合はエトスクシミド53%、バルプロ酸58%で、ラモトリギン29%より高かった。注意機能の障害はバルプロ酸で49%とエトスクシミドの33%より多く、この結果から欠神発作の初期治療ではエトスクシミドが第一選択と位置づけられる。
    condition:
      region: 国際
      対象: 新たに小児欠神てんかんと診断された小児
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1705
    source: Glauser TA, Cnaan A, Shinnar S, et al. Ethosuximide, valproic acid, and lamotrigine in childhood absence epilepsy. N Engl J Med. 2010;362(9):790-799
    doi: 10.1056/NEJMoa0902014
    pmid: '20200383'
    pmcid: null
    url: https://doi.org/10.1056/NEJMoa0902014
    source_license: © Massachusetts Medical Society（New England Journal of Medicine、CC 表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値は抄録で確認。エトスクシミドは国内で定型欠神発作（小発作）の適応で承認されている。バルプロ酸は国内でてんかんの適応で承認されているが、催奇形性のため妊娠可能な女性への使用には制約がある。ラモトリギンも国内でてんかんの適応で承認されている。SRC-1705 の PMCID は PMC2924476 が候補（マスターでは null のため本カードも null とし、補完は取り込み側の照合に委ねる）。
  curriculum:
    kokushi: 医学各論 Ⅸ-11-C-②（欠神発作<全般非運動発作>、a）
    core_curriculum: 'PS-02-03-05 (id: JkxnuP0)；TBL-01-00-053 (id: Jlvnleo)'
  publication_info:
    created: '2026-11-01'
    verifier: null
    verified_at: null
    status: draft
```
