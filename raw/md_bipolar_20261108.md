# 双極性障害「症状・診断」新規カード下書き（2026-11-08）

## 冒頭注記（必ず読むこと）

- 本ファイルは **未登録の下書き** である。cleanroom-facts リポジトリには取り込まれておらず、正式なカード ID・SRC 番号は付いていない。
- 目的：既存の MD カードのうち双極性障害を扱うもの（MD-005〜008）は、診療ガイドラインの位置づけと治療（第一選択薬の列挙）が中心で、**症状・診断基準そのものを扱うカードが無かった**ため、「うつ病との違い」等の切り口のショート動画を作れるよう、その不足分について登録前の地ならしとして一次資料を確認し、カード形式の下書きを用意するもの。治療に関する内容は既存 MD-005〜008 の担当範囲であり、本下書きでは扱わない。
- ID は `MD-仮6` 〜 `MD-仮9` の仮表記。うつ病の下書き（2026-11-07）の仮1〜仮5が登録時に MD-009〜013 となった続きとして仮6から振った。正式な番号付けと登録はレポジトリ側の仕事であり、本下書きの番号をそのまま使わないこと。
- DSM-5-TR（書籍）は MD-009 の出典として登録済みの **SRC-4976 をそのまま使う**（重複登録の回避）。新規出典2件（Merikangas 2011、Hirschfeld 2003）は「新規（仮）」と表記した。いずれも出典マスター（origin/main の data/sources/sources.yaml）と過去の納品分に同一文献が無いことを確認済み（詳細は末尾）。
- `assertion.condition` は既存 MD カード（MD-005〜009）に合わせ、`region` と `対象` の形にした。
- `curriculum` は登録時の依頼文の表が正本であるため、本下書きでは決め打ちせず、`kokushi`・`core_curriculum` とも null とした。登録時に依頼文の表の同じ行から機械的に抜き出して転記すること（既存 MD-005〜008 では双極性障害は 医学各論 Ⅱ-2-A-②（双極性障害<躁うつ病>、a）に付いているが、それも登録時に表で照合して確定すること）。
- 各カードの主張は、出典の抄録・PMC 全文または基準の転載資料で実際に確認できた範囲に限った。確認できなかった点は各カードの `uncertainty` と末尾の「確認できなかった点・申し送り」に分けて書いた。
- 本下書きの4枚はいずれも薬剤名を扱っていない（国内承認・保険適用の注記は不要な範囲に留めた）。抗うつ薬に関連する躁の扱いに触れる箇所でも、薬剤名ではなく現象の範囲に留めた。

## 1. 出典表

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-4976（既存） | American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR). Washington, DC: American Psychiatric Association Publishing; 2022 | なし（書籍） | なし（書籍） | 表示なし（書籍） | RESTRICTED | MD-009 の出典として登録済み（書誌・ISBN は MD-009 の uncertainty に記録あり）。本下書きでの基準の構造（期間・症状数・重症度）の照合は、DSM-5 のエピソード基準の概要を Table 1 に転載した McCormick U, et al. J Am Assoc Nurse Pract. 2015（PMID 26172568、PMC5034840）の PMC 全文で行った |
| 新規（仮） | Merikangas KR, Jin R, He JP, et al. Prevalence and correlates of bipolar spectrum disorder in the world mental health survey initiative. Arch Gen Psychiatry. 2011;68(3):241-251 | 10.1001/archgenpsychiatry.2011.12 | 21383262 | CC表示なし（購読誌。PMC 収載は著者稿） | RESTRICTED | PubMed レコード（PMID 21383262）で DOI・PMCID（PMC3486639）と照合。主張の数値は抄録で確認した範囲に限定 |
| 新規（仮） | Hirschfeld RMA, Lewis L, Vornik LA. Perceptions and impact of bipolar disorder: how far have we really come? Results of the national depressive and manic-depressive association 2000 survey of individuals with bipolar disorder. J Clin Psychiatry. 2003;64(2):161-174 | 10.4088/jcp.v64n0207 | 12633125 | CC表示なし（購読誌） | RESTRICTED | PubMed レコード（PMID 12633125）で DOI と照合。主張の数値は抄録で確認した範囲に限定 |

## 2. カード（YAML）

```yaml
- id: MD-仮6
  domain: MD
  subdomain: 双極性障害
  assertion:
    plain_statement_ja: DSM-5-TR の診断基準では、躁病エピソードは、異常で持続的な気分の高揚・開放（拡張）・易怒性と、活動またはエネルギーの増加が、1日の大半、ほぼ毎日、少なくとも1週間続く期間と定義される。同じ期間に、誇大性・自尊心の肥大、睡眠欲求の減少、多弁・話し続けようとする切迫感、観念奔逸、易転導性、目標志向性活動の増加または精神運動焦燥、悪い結果を招く可能性が高い活動への過度の関与、の7症状のうち3つ以上（気分が易怒性のみの場合は4つ以上）が、それまでの状態からの明確な変化として認められることが求められる。あわせて、気分の障害が社会的・職業的機能に著しい障害を起こすか、入院を必要とするほど重いこと、または精神病性の特徴を伴うこと、そのエピソードが物質や他の身体疾患の生理学的作用では説明されないことが求められる
    condition:
      region: 国際
      対象: 躁病エピソードの診断評価を受ける人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4976
    source: 'American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR). Washington, DC: American Psychiatric Association Publishing; 2022'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 表示なし（書籍）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 書籍のため DOI・PMID はない。書誌は MD-009 登録時に奥付で確認済み（American Psychiatric Association Publishing、2022年、ISBN 978-0-89042-575-6（Hardcover）／978-0-89042-576-3（Paperback））。基準の構造（気分と活動・エネルギーの増加が少なくとも1週間、7症状のうち3つ以上・易怒性のみの場合は4つ以上、著しい障害を起こす重さ）は、DSM-5 のエピソード基準の概要を Table 1 に転載した McCormick U, et al.（J Am Assoc Nurse Pract. 2015、PMC5034840）の PMC 全文で照合した。本下書きでは書籍本文を直接照合していないため、7症状の項目レベルの文言、入院・精神病性の特徴に関する基準Cの文言、除外（基準D）の文言は、登録時に書籍本文（Bipolar and Related Disorders 章）で最終照合すること。DSM-5 から DSM-5-TR への基準変更の有無もあわせて確認すること
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-08'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: MD-仮7
  domain: MD
  subdomain: 双極性障害
  assertion:
    plain_statement_ja: DSM-5-TR の診断基準では、軽躁病エピソードは、異常で持続的な気分の高揚・開放（拡張）・易怒性と、活動またはエネルギーの増加が、1日の大半、ほぼ毎日、少なくとも4日連続で続く期間と定義される。症状の構成は躁病エピソードと同じで、7症状のうち3つ以上（気分が易怒性のみの場合は4つ以上）が求められるが、躁病エピソードと異なり、そのエピソードは普段のその人とは明確に異なる機能の変化を伴い、気分の障害と機能の変化は他者からも観察できるものでなければならない。一方で、社会的・職業的機能に著しい障害を起こしたり入院を必要としたりするほど重くはなく、精神病性の特徴を伴わない（精神病性の特徴を伴えば躁病エピソードとする）。エピソードが物質や他の身体疾患の生理学的作用では説明されないことも求められる
    condition:
      region: 国際
      対象: 軽躁病エピソードの診断評価を受ける人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4976
    source: 'American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR). Washington, DC: American Psychiatric Association Publishing; 2022'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 表示なし（書籍）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 書籍のため DOI・PMID はない。基準の構造（少なくとも4日、躁病エピソードと同じ症状構成、他者から観察できる変化、著しい障害を起こすほど重くない）は McCormick U, et al.（J Am Assoc Nurse Pract. 2015、PMC5034840）の PMC 全文（Table 1 の転載）で照合した。本下書きでは書籍本文を直接照合していないため、項目レベルの文言、「精神病性の特徴を伴えば躁病エピソードとする」という定義上の振り分け、その他の除外（他の精神病性障害との区別）の文言は、登録時に書籍本文（Bipolar and Related Disorders 章）で最終照合すること
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-08'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: MD-仮8
  domain: MD
  subdomain: 双極性障害
  assertion:
    plain_statement_ja: DSM-5-TR では、双極性障害は双極I型障害と双極II型障害に分けられる。双極I型障害は躁病エピソードによって定義され、診断には少なくとも1回の躁病エピソードの既往が必要で、大うつ病エピソードの既往は必須ではない。双極II型障害は、少なくとも1回の軽躁病エピソードと少なくとも1回の大うつ病エピソードの既往によって定義され、躁病エピソードの既往がないことが条件になる。WHO 世界精神保健調査（11か国、地域在住成人61,392人、DSM-IV 基準による面接調査）では、生涯有病率は双極I型障害0.6%、双極II型障害0.4%、閾値未満の双極性状態1.4%、これらを合わせた双極スペクトラム障害2.4%と推定された
    condition:
      region: 国際
      対象: 双極性障害の診断評価を受ける人
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-4976
    source: 'American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR). Washington, DC: American Psychiatric Association Publishing; 2022'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: 表示なし（書籍）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 類型の定義は DSM-5-TR（SRC-4976）に基づき、エピソードの組み合わせによる定義の骨格（I型には躁病エピソードが少なくとも1回必要、II型には軽躁病エピソードと大うつ病エピソードが必要）は McCormick U, et al.（J Am Assoc Nurse Pract. 2015、PMC5034840）の PMC 全文で照合した。一方、生涯有病率の数値は Merikangas KR, et al.（Arch Gen Psychiatry. 2011;68(3):241-251、PMID 21383262）の抄録で確認したもので、出典表の「新規（仮）」に別掲した。本カードは定義（書籍）と有病率（疫学調査）の複合出典になっており、登録時に、provenance をどちらに置くか、または有病率部分を別カードに分けるかを登録側で判断すること。有病率は DSM-IV 基準による11か国の統合値であり、国別の数値や DSM-5-TR 基準での再推定値は主張に含めていない
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-08'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
- id: MD-仮9
  domain: MD
  subdomain: 双極性障害
  assertion:
    plain_statement_ja: 双極性障害のうつ病エピソードは、DSM-5-TR では大うつ病性障害（単極性うつ病）の大うつ病エピソードと同じ基準で定義されるため、うつ状態の症状だけからは両者を区別できず、鑑別は過去の躁病・軽躁病エピソードの病歴を確認できるかにかかる。米国の双極性障害の当事者団体（National Depressive and Manic-Depressive Association）の2000年調査（双極性障害と診断された回答者600人）では、69%が当初誤診を受けており、最も多い誤診は単極性うつ病だった。誤診を受けた人は、正しい診断を受けるまでに平均4人の医師にかかり、3分の1を超える人が正確な診断まで10年以上を要した
    condition:
      region: 米国
      対象: 双極性障害と診断された人
    differential: null
    common_misconception: null
  provenance:
    source_ref: 新規（仮）
    source: 'Hirschfeld RMA, Lewis L, Vornik LA. Perceptions and impact of bipolar disorder: how far have we really come? Results of the national depressive and manic-depressive association 2000 survey of individuals with bipolar disorder. J Clin Psychiatry. 2003;64(2):161-174'
    doi: 10.4088/jcp.v64n0207
    pmid: '12633125'
    pmcid: null
    url: https://doi.org/10.4088/jcp.v64n0207
    source_license: CC表示なし（購読誌）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 数値（69%・平均4人・3分の1超が10年以上）は抄録で確認した範囲に限る。この調査は当事者団体の支援グループ参加者に配布された自己記入式アンケートで、最初に返送された600人を解析対象としており、回答は回顧的な自己報告に基づく。対象は2000年の米国の集団であり、日本の患者集団への当てはめには限界がある。冒頭の「うつ病エピソードの基準は単極性うつ病と同じで、区別は躁・軽躁の病歴による」という点は DSM-5-TR の基準構造（SRC-4976）に基づき、McCormick U, et al.（J Am Assoc Nurse Pract. 2015、PMC5034840）の PMC 全文でも同旨を確認した。本カードの provenance は数値の出典である Hirschfeld 2003 を主出典としており、登録時に基準構造の部分を SRC-4976 側へ分けるかは登録側で判断すること
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-08'
    verifier: null
    verified_at: null
    status: draft
    superseded_by: null
```

## 3. 確認できなかった点・申し送り

- **出典の重複確認**：最新の出典マスター（origin/main の data/sources/sources.yaml）を DOI・PMID・著者名で検索し、過去の納品分（ワークスペース内の納品 Markdown）も DOI・PMID で検索した。DSM-5-TR は MD-009 の出典として SRC-4976 が登録済みだったため新規登録せず再利用した。Merikangas 2011（DOI 10.1001/archgenpsychiatry.2011.12、PMID 21383262）と Hirschfeld 2003（DOI 10.4088/jcp.v64n0207、PMID 12633125）は、いずれも同一文献の登録が無く、新規出典として扱った。照合に使った McCormick 2015 は出典としては登録せず、基準照合の経路として各カードの uncertainty にのみ記した（Tolentino & Schmidt 2018 を MD-009 で照合経路として扱った前例と同じ）。
- **DSM-5-TR 本文の直接照合は未了**：MD-仮6・仮7 の基準の構造（期間・症状数の閾値・重症度の考え方）は McCormick 2015 の Table 1（DSM-5 基準の概要転載）で照合したが、7症状の項目レベルの文言、基準C・Dの正確な文言、軽躁病の「精神病性の特徴を伴えば躁病エピソードとする」振り分けは、書籍本文そのものでは照合していない。登録時に書籍（Bipolar and Related Disorders 章）で最終照合すること。DSM-5 から DSM-5-TR への基準変更の有無もあわせて確認すること。
- **躁病エピソードの期間の例外**：DSM-5 系の基準では、躁病エピソードの期間について「入院を必要とする場合は期間を問わない」という趣旨の括弧書きがあるとされるが、本下書きでは転載資料で直接確認できなかったため、MD-仮6 の主張には入れていない。登録時に書籍本文で確認し、必要なら追記すること。
- **抗うつ薬に関連する躁の扱い**：DSM-5 以降、抗うつ薬に関連して出現した躁が躁病エピソードとして扱われうることは、ICD-11 と DSM-5 の比較表（Cerbo AD. Turk Psikiyatri Derg. 2021;32(4):293-295、PMID 34964106）で「Antidepressant-related mania qualifies as a manic episode: DSM-5 = Yes」と確認できた。しかし「治療の生理学的作用を超えて完全に持続する場合」という条件の文言までは転載で照合できなかったため、MD-仮6 の主張には含めていない。薬剤名は出さず現象の範囲で、登録時に書籍本文の Note を確認してから必要なら追記すること。
- **MD-仮8 は複合出典**：類型の定義（DSM-5-TR、SRC-4976）と生涯有病率（Merikangas 2011、新規（仮））を1枚に含めた。登録時に provenance の置き方（定義側に統一／有病率を別カード化）を判断すること。有病率は DSM-IV 基準・11か国の統合値で、日本単独の数値は本下書きでは確認していない（日本の疫学調査の数値を入れる場合は別途一次資料の確認が要る）。
- **MD-仮9 と既存 MD-013 との関係**：MD-013 は「うつ病の診断評価には躁・軽躁の既往確認（双極性障害との区別）が含まれる」という枠組みを CANMAT 2023 から主張するカード。MD-仮9 は、うつ病エピソードの基準が単極性と同一であることと、誤診・診断遅延の実測値（Hirschfeld 2003）を主張するもので、主張の中心は異なる。重複ではなく補完と判断したが、最終判定は登録側に委ねる。
- **curriculum は空欄**：kokushi・core_curriculum とも null。登録依頼文の表から、番号と同じ行の不変 id を機械的に抜き出して転記すること（既存 MD-005〜008 は 医学各論 Ⅱ-2-A-②（双極性障害<躁うつ病>、a）に付いているが、決め打ちはしない）。
- **今回見送った候補**：双極性障害のスクリーニング尺度（MDQ 等）の診断性能、急速交代型・混合特徴などの特定用語（スペシファイア）の基準、児童・青年期の双極性障害、ICD-11 との基準の差異（Cerbo 2021 で一部確認できたが、本下書きの範囲外とした）。いずれも登録側の判断材料として申し送る。
- **動画との関係**：本下書きは、双極性障害の動画（症状・うつ病との違いの切り口）の根拠カード候補である。登録が済むまでは動画の根拠に使わないこと。治療については既存 MD-005〜008 が根拠になる。
