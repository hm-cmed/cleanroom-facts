# 分割案（第1陣・EB1）：「根拠に基づく医療・研究方法」の事実票

作成日：2026-11-26／作成：モコ（Muse 側）／段階：分割案（提案書）。カード本文は未作成。
取り扱いは従来どおり、レポジトリ側の検査・登録→ユーザー承認→作成の順とする。本書は raw Markdown のみで渡し、レポジトリへは直接入れない。
動画側の候補リストは `~/workspace/video_studio/EBM_VIDEO_QUEUE.md`（全28テーマ、第1陣12テーマ確定済み）。

## 1. 全体像と今回の位置づけ

- 新シリーズ「根拠に基づく医療・研究方法」は、EBM・レビュー論文作成・診療ガイドライン作成・患者市民参画を扱う、既存の医療知識（疾患別）・医療者教育（ME）とは別のシリーズである。再生リストも同名で別に作る（初回公開時に作成）。
- 動画テーマは全28本を棚卸し済みで、そのうち第1陣12本が確定している（2026-11-26、EB_019＝EtD を含めることをユーザーが決定）。
- 本書は第1陣12テーマに対応する**根拠カード12枚（仮番号 EB-001〜EB-012）**の分割案である。原則として動画1テーマ＝カード1枚とし、分割が必要になりうるものは §3 に明記した。
- カードの接頭辞「EB」と番号帯は仮置きである。既存の接頭辞（ME 等）と衝突しないか、登録時にレポジトリ側の確定を受ける（§4-1）。
- 出典は一次の方法論文・公式ハンドブック・公式ステートメントの全文に限る。抄録・医学百科・StatPearls 等の二次解説は根拠にしない。RESTRICTED の出典も、本文・図表を転載せず事実を出典明示で自分の言葉で述べる範囲で扱う（従来方針どおり）。

## 2. 第1陣12枚（出典特定済み）

書誌は 2026-11-26 に PubMed（E-utilities）で照合して確定した。ライセンス区分は見立てであり、確定は登録時の照合に従う。出典マスターとの重複照合の記録は §5。

| 仮番号 | 対応動画 | 仮タイトル | 主張の要旨（案） | 根拠出典 | 確認状態 |
|---|---|---|---|---|---|
| EB-001 | EB_001 | PICO：臨床疑問の構造化 | 臨床疑問を Patient／Intervention／Comparison／Outcome に構造化すると、そのまま検索式の部品とレビューの適格基準になる。疑問の型（治療・診断・予後等）で要素の置き方が変わる | Cochrane Handbook for Systematic Reviews of Interventions（現行版、Ch.2「Determining the scope」・Ch.5 相当）／起源論文 Richardson WS et al. The well-built clinical question. ACP J Club. 1995（PMID・DOI なし、起源の位置づけは uncertainty に書く） | Handbook は公式サイトで版を確認してから作成する。Richardson は書誌のみ確認／ライセンス：Handbook は要確認 |
| EB-002 | EB_002 | 無作為割付が交絡を均す仕組み | 無作為割付は、既知・未知を問わず交絡因子を群間で期待値として均等にする唯一の割付方法であり、割付順序の隠蔽（allocation concealment）と併せて選択バイアスを防ぐ | Sterne JAC et al. RoB 2: a revised tool for assessing risk of bias in randomised trials. BMJ. 2019. PMID 31462531／DOI 10.1136/bmj.l4898（EB-007 と共用） | 確認済み（PubMed）／ライセンス：OPEN（CC BY）の見立て |
| EB-003 | EB_003 | p値の正しい読み方（ASA声明） | p値は「帰無仮説が正しい確率」でも「効果の大きさ」でもない。ASA 2016年声明は6原則を示し、閾値（0.05等）だけで科学的結論を決めることを戒めた | Wasserstein RL, Lazar NA. The ASA Statement on p-Values: Context, Process, and Purpose. Am Stat. 2016. DOI 10.1080/00031305.2016.1154108（PMID なし） | 確認済み（DOI で特定）／ライセンス：RESTRICTED の見立て |
| EB-004 | EB_009 | PRISMA 2020：報告の27項目とフロー図 | PRISMA 2020 はシステマティックレビューの報告を標準化する声明で、27項目のチェックリストと、特定から採用までの流れと除外理由を残すフロー図からなる。報告規範であり、実施の質そのものの評価ではない | Page MJ et al. The PRISMA 2020 statement. BMJ. 2021. PMID 33782057／PMCID PMC8005924／DOI 10.1136/bmj.n71 | 確認済み（PubMed）／ライセンス：OPEN（CC BY）の見立て |
| EB-005 | EB_010 | 文献検索の報告と査読（PRISMA-S／PRESS） | 検索の報告には PRISMA-S（16項目）があり、検索式の第三者査読には PRESS（2015）がある。検索の漏れは後の統計処理では取り戻せないため、検索過程そのものが再現性の対象になる | Rethlefsen ML et al. PRISMA-S. Syst Rev. 2021. PMID 33499930／DOI 10.1186/s13643-020-01542-z ＋ McGowan J et al. PRESS Peer Review of Electronic Search Strategies: 2015 Guideline Statement. J Clin Epidemiol. 2016. PMID 27005575／DOI 10.1016/j.jclinepi.2016.01.021 | 確認済み（PubMed、2件とも）／ライセンス：PRISMA-S は OPEN（CC BY）、PRESS は RESTRICTED の見立て |
| EB-006 | EB_011 | スクリーニングの二重化と単独実施の見落とし | 研究選択を1人で行う単独スクリーニングは、2人の従来型と比べて採用すべき研究の見落としが生じうることが方法論的レビューで示されており、Cochrane は独立した2人による選択を標準とする | Waffenschmidt S et al. Single screening versus conventional double screening for study selection in systematic reviews: a methodological systematic review. BMC Med Res Methodol. 2019. PMID 31253092／DOI 10.1186/s12874-019-0782-0 ＋ Cochrane Handbook Ch.4 | 確認済み（PubMed）／ライセンス：OPEN（CC BY）の見立て。見落としの具体的な数値は作成時に本文で確定させる |
| EB-007 | EB_012 | RoB 2：ドメインで判定するバイアス評価 | RoB 2 はランダム化試験の特定の「結果」ごとに、5ドメイン（無作為化過程、割り付けられた介入からの逸脱、欠測、測定、報告結果の選択）でバイアスのリスクを判定する道具で、合計点は付けない | Sterne JAC et al. BMJ. 2019. PMID 31462531／DOI 10.1136/bmj.l4898（EB-002 と共用）＋ RoB 2 公式文書（riskofbias.info、現行版） | 確認済み（PubMed）／ライセンス：OPEN（CC BY）の見立て。公式文書の版は作成時に確認 |
| EB-008 | EB_017 | GRADE：エビデンスの確実性の4段階 | GRADE ではアウトカムごとにエビデンスの確実性を高・中・低・非常に低の4段階で評価し、RCTは高から、観察研究は低から出発して、バイアス・非一貫性・非直接性・不精確さ・出版バイアスで下げ、大きな効果等で上げる | Guyatt GH et al. GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. BMJ. 2008. PMID 18436948／DOI 10.1136/bmj.39489.470347.AD ＋ GRADE Handbook（現行版） | 確認済み（PubMed）／ライセンス：BMJ 論文は OPEN（CC BY 系）の見立て、Handbook は要確認 |
| EB-009 | EB_018 | 推奨の方向と強さの決まり方 | 推奨の方向と強さ（強い／条件付き）は、確実性だけでなく、利益と害のバランス、価値観と選好、資源利用で決まる。そのため確実性が低くても強い推奨になる場合（およびその逆）が、限定された条件で起こりうる | Andrews JC et al. GRADE guidelines: 15. Going from evidence to recommendation — determinants of a recommendation's direction and strength. J Clin Epidemiol. 2013. PMID 23570745／DOI 10.1016/j.jclinepi.2013.02.003 | 確認済み（PubMed）／ライセンス：RESTRICTED の見立て |
| EB-010 | EB_019 | EtD（Evidence to Decision）フレームワーク | EtD は、問題の優先度、利益と害、確実性、価値観、資源、公平性、受容可能性、実行可能性を項目ごとに判断して表に残し、エビデンスから推奨への移行を透明にする枠組みである | Alonso-Coello P et al. GRADE Evidence to Decision (EtD) frameworks: 2: Clinical practice guidelines. BMJ. 2016. PMID 27365494／DOI 10.1136/bmj.i2089（ companion の 1: Health system and public health decisions と対） | 確認済み（PubMed）／ライセンス：OPEN（CC BY）の見立て |
| EB-011 | EB_024 | 患者市民参画の報告と評価（GRIPP2） | 患者市民参画（PPI）の報告には GRIPP2 チェックリストがあり、参画の目的・方法・結果（研究や決定への影響）・反省を書く。参画の評価は参加の有無ではなく、どの決定がどう変わったかで見る | Staniszewska S et al. GRIPP2 reporting checklists. BMJ. 2017. PMID 28768629／PMCID PMC5539518／DOI 10.1136/bmj.j3453 | 確認済み（PubMed）／ライセンス：OPEN（CC BY）の見立て |
| EB-012 | EB_025 | 患者市民参画（PPI）とは何か | PPI は「患者・市民と共に（with）、または患者・市民によって（by）行われる研究」であり、患者が研究の対象（参加者）になることとは区別される。参画は研究の各段階（課題設定から普及まで）で起こりうる | NIHR／INVOLVE 公式ガイダンス（Briefing notes for researchers、定義文書。PMID・DOI なし） | 公式文書の存在と定義は確認済み。採用する版・文書の特定は作成時に行う／ライセンス：UK 公的機関資料、区分は登録時に確認。日本の制度として断定しない旨を uncertainty に書く |

## 3. 分割・統合の選択肢

- **EB-002 と EB-007 の分離維持**：どちらも RoB 2 論文を共用するが、EB-002 は「無作為割付という仕組みがなぜ効くか」、EB-007 は「RoB 2 という道具でどう判定するか」で切り口が異なるため分ける。台本・カード同士で主張が重複しないよう、EB-002 の主張は割付の仕組みに限り、ドメイン判定には踏み込まない。
- **EB-008 の分割可能性**：確実性の「下げる5要因」と「上げる3要因」まで1枚に入れると過密になる場合は、作成時に EB-008a／b への分割をレポジトリ側と相談する。本案ではまず1枚とする。
- **EB-005 の統合維持**：PRISMA-S（報告）と PRESS（査読）は役割が違うが、「検索過程の透明性」という1テーマとして統合した。分ける場合は EB-005 を検索報告とし、査読側を別カード（EB-013 として新設）にする形になる。
- **EB-011 と EB-012 の分離維持**：GRIPP2 は「報告と評価」、INVOLVE 定義は「概念そのもの」。動画でも2本に分かれているため、カードも分ける。

## 4. 未決事項（レポジトリ側に確認すべき点）

1. **接頭辞と番号帯**：「EB」の接頭辞と EB-001 からの採番でよいか。既存シリーズとの衝突確認をお願いしたい。
2. **Cochrane Handbook の扱い**：オンライン版（現行版）を出典とするカード（EB-001・EB-006）の、版の固定方法（参照日・章番号の記録）とライセンス区分の確定。
3. **PMID・DOI のない出典2件**：Richardson 1995（EB-001 の起源論文）と NIHR／INVOLVE 文書（EB-012）は識別子がない。登録方法（URL・文書名での登録）の可否を確認したい。
4. **ASA 声明（EB-003）**：PMID がなく DOI のみの出典である。統計学側の声明を医学系マスターに登録する扱いでよいか。
5. **GRADE Handbook の版**：EB-008・EB-009 で参照する Handbook／guidance series の版のそろえ方。
6. **第1陣の依頼単位**：12枚を1回の依頼とするか、分野別（A：EB-001〜003／B：EB-004〜007／C：EB-008〜010／D：EB-011〜012）に分けるか。ME2 の前例（出典確認済みの陣を先行）に従えば一括も可能だが、レポジトリ側の検査容量に合わせる。
7. **動画との対応**：カードが draft のままでも動画化時点の監修で公開できる既定方針（ME と同じ）を、本シリーズにも適用してよいか。

## 5. 確認作業の記録

- 書誌照合：2026-11-26、PubMed（E-utilities API）で以下を照合し、タイトル・誌名・年・DOI を確定した。
  - Sterne et al. 2019（PMID 31462531）、Page et al. 2021（PMID 33782057）、Rethlefsen et al. 2021（PMID 33499930）、McGowan et al. 2016（PMID 27005575）、Waffenschmidt et al. 2019（PMID 31253092）、Guyatt et al. 2008（PMID 18436948）、Andrews et al. 2013（PMID 23570745）、Alonso-Coello et al. 2016（PMID 27365494）、Staniszewska et al. 2017（PMID 28768629）
  - Wasserstein & Lazar 2016（ASA 声明）は PubMed 未収載のため DOI（10.1080/00031305.2016.1154108）で特定した。
- 重複照合：2026-11-26、上記10件の DOI を手元の出典マスター・スナップショット（sources_master_current.yaml ほか）で検索し、**いずれも既存登録なし**。ただしスナップショットは最新の納品分まで伸びていない可能性があるため、登録時にマスター全体での再照合をお願いしたい（第53回の教訓：照合範囲は最新の納品分まで伸ばす）。
- 数値の扱い：EB-006 の見落とし率など、本書で数値を主張に入れなかった項目は、作成時に本文で確定させてから書く。
- 動画キューとの対応：12テーマすべてに仮番号を1対1で対応付けた。対応表は §2 の「対応動画」欄が正である。
