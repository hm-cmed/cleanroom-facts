# カバレッジ報告

`python scripts/validate.py --report` で自動生成。手で編集しない。

## 出典の利用区分

| 区分 | 意味 | 出典数 |
|---|---|---|
| A | 商用・改変可（CC BY等） | 11 |
| B | 改変可・継承義務（CC BY-SA） | 0 |
| C | 非営利のみ（BY-NC, BY-NC-SA） | 3 |
| D | 改変禁止（ND）：照合用のみ | 5 |
| E | 権利留保・許諾待ち：事実票の根拠にしない | 5 |

## コース別の事実票数

| コース | 事実票 | うち非営利限定（区分C） | 未解決ギャップ |
|---|---|---|---|
| C1 開始判断・薬剤選択 | 17 | 0 | 6 |
| C2 VCM初期投与・TDM | 45 | 9 | 2 |
| C3 選択と投与設計の統合 | 15 | 11 | 8 |
| C4 専門医の選択哲学 | 4 | 0 | 3 |
| C5 再評価・デエスカレーション | 4 | 0 | 4 |

## 出典別の事実票数

| 出典 | ライセンス | 区分 | 事実票 |
|---|---|---|---|
| MATSUMOTO_VCM_TDM_2022 | CC BY 4.0 | A | 28 |
| JSSCG_2024_JIC | CC BY 4.0 | A | 12 |
| HANAI_TEIC_TDM_2022 | CC BY-NC 4.0 | C | 11 |
| UK_MRSA_GL_2021 | CC BY 4.0 | A | 10 |
| TSUTSUURA_VCM_MA_2021 | CC BY 4.0 | A | 5 |
| WHO_BULLETIN_RESERVE_2025 | 要確認（WHO BulletinはCC BY 3.0 IGOのことが多い） | A | 4 |
| LIN_LZD_CONSENSUS_2022 | CC BY 4.0 | A | 1 |
| LZD_RENAL_BMCPT_2022 | CC BY 4.0 | A | 1 |
| THIROT_LZD_2024 | CC BY 4.0 | A | 1 |

## 未解決ギャップ（専門家意見・許諾等で補う項目）

| ID | コース | 項目 | 解決方法 | 優先度 |
|---|---|---|---|---|
| GAP-C1-RISK | C1 | 敗血症・重症感染症で経験的に抗MRSA薬を開始する基準 | expert_opinion | high |
| GAP-C1-EPI | C1 | 国内のMRSAの頻度 | data_retrieval | medium |
| GAP-C1-SITE | C1,C3 | 感染臓器別の抗MRSA薬の選択（国内の実情） | permission_request | high |
| GAP-C1-PNA-LZD | C1 | MRSA肺炎でのVCMとLZDの選択 | expert_opinion | medium |
| GAP-C1-BSI-DAP | C1,C3 | MRSA菌血症でのDAPの位置づけ | expert_opinion | high |
| GAP-C1-NASAL | C1,C5 | 鼻腔MRSAスクリーニング（PCR）の陰性結果の使い方 | extraction_pending | medium |
| GAP-C2-NOMOGRAM | C2 | VCMの腎機能別初期投与量ノモグラム | extraction_pending | high |
| GAP-C2-LABEL | C2,C3 | 国内の承認用法・用量 | regulatory_fact | high |
| GAP-C3-LZD | C3 | 国内でのLZDのTDMと血小板減少の管理 | expert_opinion | medium |
| GAP-C3-DAP-SAFETY | C3 | DAPのCK上昇・相互作用の管理 | expert_opinion | medium |
| GAP-C3-ABK | C3 | アルベカシン（ABK）の位置づけとTDM | expert_opinion | low |
| GAP-C3-TZD | C3 | テジゾリド（TZD）の位置づけ | expert_opinion | low |
| GAP-C3-VCM-TAZ | C3 | VCMとピペラシリン・タゾバクタム併用時の腎障害 | extraction_pending | low |
| GAP-C4-PHILOSOPHY | C4 | 専門家が重視する判断因子とその重みづけ | expert_opinion | high |
| GAP-C4-AWARE | C4 | 国内で使う抗MRSA薬のAWaRe分類 | extraction_pending | low |
| GAP-C5-STOP | C5 | 培養陰性時に抗MRSA薬を中止する時期 | expert_opinion | high |
| GAP-C5-SAB-DEF | C5 | 黄色ブドウ球菌菌血症（SAB）の複雑性・非複雑性の判定と必要な検査 | extraction_pending | high |
| GAP-C5-ORAL | C4,C5 | 経口薬への切替・外来治療への移行 | expert_opinion | medium |

## 事実票一覧

### C1 開始判断・薬剤選択

- `AWARE-003` 【ガイドラインに基づく推奨】VCMはWatch群に分類される。MRSA（WHO優先病原体リストの高優先度）による感染症では、Watch群のVCMが適切な選択肢となりうる。 — WHO_BULLETIN_RESERVE_2025 Main text [draft]
- `AWARE-004` 【ガイドラインに基づく推奨】2025年版WHO必須医薬品リストに収載されたReserve群の抗菌薬には、リネゾリドとテジゾリドが含まれる。 — WHO_BULLETIN_RESERVE_2025 Box / Main text [draft]
- `UK-MRSA-BSI-001` 【ガイドラインに基づく推奨】非複雑性のMRSA菌血症では、VCMの静脈内投与を用いる（英国ガイドライン）。（strong） — UK_MRSA_GL_2021 4.4 Bacteraemia [draft]
- `UK-MRSA-BSI-002` 【ガイドラインに基づく推奨】MRSA菌血症でVCMが禁忌の場合は、リネゾリドを代替の第一選択とする（英国ガイドライン）。（strong） — UK_MRSA_GL_2021 4.4 Bacteraemia [draft]
- `UK-MRSA-BSI-003` 【ガイドラインに基づく推奨】MRSA菌血症で第一選択薬が禁忌の場合は、ダプトマイシンまたはテイコプラニンを考慮する（英国ガイドライン）。（weak） — UK_MRSA_GL_2021 4.4 Bacteraemia [draft]
- `UK-MRSA-PNA-001` 【ガイドラインに基づく推奨】MRSAによる院内肺炎では、VCMまたはリネゾリドの静脈内投与を第一選択とする（英国ガイドライン。リネゾリドの優越性を確認する追加試験がないため）。（weak） — UK_MRSA_GL_2021 4.6.2 Nosocomial pneumonia [draft]
- `UK-MRSA-PNA-002` 【ガイドラインに基づく推奨】ダプトマイシンは肺サーファクタントで不活化されるため、MRSAによる院内肺炎の治療に用いない（英国ガイドライン）。（strong） — UK_MRSA_GL_2021 4.6.2 Nosocomial pneumonia [draft]
- `UK-MRSA-PNA-003` 【ガイドラインに基づく推奨】MRSAによる壊死性肺炎では、VCMまたはリネゾリドの静脈内投与を用いる（英国ガイドライン）。（strong） — UK_MRSA_GL_2021 Necrotizing pneumonia [draft]
- `UK-MRSA-SSTI-001` 【ガイドラインに基づく推奨】MRSAによる重症の蜂窩織炎・軟部組織感染症では、グリコペプチド系（VCMまたはテイコプラニン）の静脈内投与を用い、代替としてリネゾリド（経口または静注）またはダプトマイシン（静注）を用いる（英国ガイドライン）。（strong） — UK_MRSA_GL_2021 SSTI [draft]
- `UK-MRSA-UTI-001` 【ガイドラインに基づく推奨】尿からMRSAが分離された場合は、治療開始前に菌血症の有無を確認する。複雑性尿路感染症ではグリコペプチド系の静脈内投与を第一選択として考慮し、リネゾリドは腎からの排泄が少ないため推奨しない（英国ガイドライン）。（weak） — UK_MRSA_GL_2021 UTI [draft]
- `UK-MRSA-BJI-001` 【ガイドラインに基づく推奨】MRSAによる骨・関節感染症の治療は、必要に応じた手術やドレナージを含む多職種チームで行う（英国ガイドライン）。（strong） — UK_MRSA_GL_2021 Bone and joint infection [draft]
- `SEP-ABX-001` 【ガイドラインに基づく推奨】敗血症が疑われる患者では、抗菌薬投与前に少なくとも2セットの血液培養を採取する。（Good Practice Statement） — JSSCG_2024_JIC CQ1-4 [draft]
- `SEP-ABX-002` 【ガイドラインに基づく推奨】敗血症が疑われる患者では、抗菌薬投与前に感染が疑われる部位からも培養検体を採取する。（Good Practice Statement） — JSSCG_2024_JIC CQ1-4 [draft]
- `SEP-ABX-003` 【ガイドラインに基づく推奨】敗血症の経験的抗菌薬の選択にグラム染色を用いることが提案されている。（2C） — JSSCG_2024_JIC CQ2-1 [draft]
- `SEP-ABX-004` 【ガイドラインに基づく推奨】敗血症と診断したらできるだけ早く抗菌薬を開始するが、1時間以内という厳格な時間目標を設けないことが提案されている。（2C） — JSSCG_2024_JIC CQ2-2 [draft]
- `SEP-ABX-005` 【ガイドラインに基づく推奨】経験的抗菌薬は、推定される感染巣と想定される菌に基づき、患者背景、地域・施設の疫学、迅速検査、組織移行性、耐性菌のリスクを考慮して選ぶ。（Background Question） — JSSCG_2024_JIC CQ2-3 [draft]
- `SEP-ABX-006` 【ガイドラインに基づく推奨】感染巣、患者背景、微生物学的情報からMRSAの関与が疑われる場合に、経験的治療に抗MRSA薬を加える（推奨度を付さない背景情報として記載）。（Background Question） — JSSCG_2024_JIC CQ2-5 [draft]

### C2 VCM初期投与・TDM

- `SEP-ABX-007` 【ガイドラインに基づく推奨】敗血症では、腎機能の推移、体液量の変化、腎代替療法などの体外循環の有無を踏まえて抗菌薬の投与量を調整する。（Background Question） — JSSCG_2024_JIC CQ2-6 [draft]
- `SEP-ABX-008` 【ガイドラインに基づく推奨】グリコペプチド系抗菌薬（VCMなど）では、持続投与・延長投与を行わないことが提案されている（β-ラクタム系では行うことが提案されている：2B）。（2C） — JSSCG_2024_JIC CQ2-7 [draft]
- `SEP-ABX-009` 【ガイドラインに基づく推奨】敗血症の抗菌薬治療では、TDMに基づいて投与量を調整することが提案されている。（2D） — JSSCG_2024_JIC CQ2-8 [draft]
- `TEIC-PKPD-001` 【ガイドラインに基づく推奨】TEICの主要なPK/PD指標はAUC/MICだが、AUCを推定するソフトウェアが使えない施設が多いため、実臨床ではトラフ値を代替指標として用いる。（II） — HANAI_TEIC_TDM_2022 CQ1 [draft]
- `TEIC-TDM-001` 【ガイドラインに基づく推奨】重症感染症、急性・慢性の腎機能障害、肥満または低体重、熱傷、低アルブミン血症、小児では、TEICのTDMを計画する。（I） — HANAI_TEIC_TDM_2022 CQ2 [draft]
- `TEIC-TDM-002` 【ガイドラインに基づく推奨】TEICは半減期が長いため、初回TDMは定常状態に達する前の投与4日目に行い、その値をトラフ値の代替とする。（II） — HANAI_TEIC_TDM_2022 CQ3 [draft]
- `TEIC-TDM-003` 【ガイドラインに基づく推奨】非複雑性のMRSA感染症では、腎機能にかかわらずTEICの目標トラフ値を15〜30 mg/Lとする。（I） — HANAI_TEIC_TDM_2022 CQ4 [draft]
- `TEIC-TDM-004` 【ガイドラインに基づく推奨】心内膜炎や骨髄炎などの複雑性・重症のMRSA感染症では、TEICの目標トラフ値を20〜40 mg/Lとすることが提案されている。（III-A） — HANAI_TEIC_TDM_2022 CQ5 [draft]
- `TEIC-DOSE-001` 【ガイドラインに基づく推奨】腎機能正常で目標トラフ値15〜30 mg/Lの場合、最初の3日間に実体重あたり10 mg/kgを5回、または12 mg/kgを4回投与する。（II） — HANAI_TEIC_TDM_2022 CQ6 [draft]
- `TEIC-DOSE-002` 【ガイドラインに基づく推奨】腎機能正常で目標トラフ値20〜40 mg/Lの場合、最初の3日間に12 mg/kgを5回（1・2日目は1日2回、3日目は1日1回）投与する。（II） — HANAI_TEIC_TDM_2022 CQ6 [draft]
- `TEIC-DOSE-003` 【ガイドラインに基づく推奨】腎機能正常で目標トラフ値15〜30 mg/Lの場合、維持投与量は6〜6.7 mg/kgを1日1回とする。20 mg/L以上を目標とする場合はより多い維持量を考慮し、維持投与4〜5回目の前に早めにTDMを行う。（II） — HANAI_TEIC_TDM_2022 CQ6 [draft]
- `TEIC-DOSE-004` 【ガイドラインに基づく推奨】腎機能低下時も3日間の負荷投与を行い、投与量はeGFRと実体重に応じて調整する。維持投与は1回量、投与間隔またはその両方で減量し、TDMで確認する。（II） — HANAI_TEIC_TDM_2022 CQ7 [draft]
- `VCM-EVID-001` 【研究結果に基づく知見】VCMのトラフ値が20 μg/mL以上の場合、15〜20 μg/mLの場合と比べてAKIの発生が有意に多い（オッズ比2.39、95%信頼区間1.78〜3.20）。 — TSUTSUURA_VCM_MA_2021 Results [draft]
- `VCM-EVID-002` 【研究結果に基づく知見】AUC/MICが高い群（カットオフ400±15%）では、治療失敗が有意に少ない（オッズ比0.28、95%信頼区間0.18〜0.45）。 — TSUTSUURA_VCM_MA_2021 Results [draft]
- `VCM-EVID-003` 【研究結果に基づく知見】AUCが高い群（カットオフ600±15%）では、AKIのリスクが有意に高い（オッズ比2.10、95%信頼区間1.13〜3.89）。 — TSUTSUURA_VCM_MA_2021 Results [draft]
- `VCM-EVID-004` 【研究結果に基づく知見】4研究のメタ解析では、AUCガイドのモニタリングはトラフガイドよりAKIが少ない傾向を示したが有意ではなく（オッズ比0.54、95%信頼区間0.28〜1.01）、死亡率にも有意差はなかった。 — TSUTSUURA_VCM_MA_2021 Results [draft]
- `VCM-EVID-005` 【研究結果に基づく知見】成人のMRSA菌血症では、VCMトラフ値15 μg/mL以上の群で治療失敗が有意に少なかった（オッズ比0.63、95%信頼区間0.47〜0.85）。 — TSUTSUURA_VCM_MA_2021 Results [draft]
- `VCM-PKPD-001` 【ガイドラインに基づく推奨】MRSA感染症に対するVCMの有効性は、AUC/MIC（微量液体希釈法でMICを測定した場合）400以上を指標とする。（I） — MATSUMOTO_VCM_TDM_2022 CQ6 [draft]
- `VCM-PKPD-002` 【ガイドラインに基づく推奨】VCMによる急性腎障害（AKI）のリスクを下げるため、AUCは600 μg·h/mL以下に保つ。（I） — MATSUMOTO_VCM_TDM_2022 CQ6 [draft]
- `VCM-PKPD-003` 【ガイドラインに基づく推奨】実臨床でのVCMの目標AUCは400〜600 μg·h/mLとする（MICを1 μg/mLと仮定）。（I） — MATSUMOTO_VCM_TDM_2022 CQ6 [draft]
- `VCM-PKPD-004` 【ガイドラインに基づく推奨】MICが判明する前の経験的治療では、MICを1 μg/mLと仮定してAUC 400以上を目標とし、MICが判明した後も目標AUCは原則として変えない。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ6 [draft]
- `VCM-PKPD-005` 【ガイドラインに基づく推奨】MICをEtest法で測定した場合のAUC/MICの目安は200以上とされている。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ6 [draft]
- `VCM-PKPD-006` 【ガイドラインに基づく推奨】VCMの投与設計では、トラフ値をAUCの代わりとして用いることは推奨されない。（IV） — MATSUMOTO_VCM_TDM_2022 CQ2 [draft]
- `VCM-PKPD-007` 【ガイドラインに基づく推奨】AUCを指標とした投与設計は、トラフ値を指標とした投与設計よりAKIのリスクを下げる傾向がある。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ2 [draft]
- `VCM-TDM-001` 【ガイドラインに基づく推奨】実施可能であれば、重症度にかかわらずVCM投与患者にはルーチンにAUCを指標とした投与設計を行うことが提案されている。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ3 [draft]
- `VCM-TDM-002` 【ガイドラインに基づく推奨】ベイズ推定を日常的に使えない施設では、腎機能障害、ピペラシリン・タゾバクタムや利尿薬の併用、ICU入室など、AKIのリスクが高い患者を優先してAUCを指標とした投与設計を行う。（II） — MATSUMOTO_VCM_TDM_2022 CQ3 [draft]
- `VCM-TDM-003` 【ガイドラインに基づく推奨】AUCの推定には、トラフ値と投与終了1〜2時間後のピーク値の2点採血が推奨される。24時間ごとの投与でも同様である。（II） — MATSUMOTO_VCM_TDM_2022 CQ4 [draft]
- `VCM-TDM-004` 【ガイドラインに基づく推奨】12時間ごとに投与している軽症の感染症では、トラフ値1点のみでAUCを推定してもよい。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ4 [draft]
- `VCM-TDM-005` 【ガイドラインに基づく推奨】トラフ値のみからのAUC推定は、多点採血に基づく母集団薬物動態モデルを用いたベイズ推定ソフトウェアを使う場合に信頼性が高い。（II） — MATSUMOTO_VCM_TDM_2022 CQ4 [draft]
- `VCM-TDM-006` 【ガイドラインに基づく推奨】トラフ値は次回投与前30分以内に採血することが推奨されるが、ベイズ推定を用いる場合は採血時刻が前後しても実測時刻を入力すれば利用できる。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ4 [draft]
- `VCM-TDM-007` 【ガイドラインに基づく推奨】重症・複雑性感染症やAKIのリスクが高い患者では、定常状態に達する前の投与2日目にTDMを行うことを考慮する。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ5 [draft]
- `VCM-TDM-008` 【ガイドラインに基づく推奨】AKIのリスクがない軽症〜中等症の感染症では、定常状態に近い投与3日目ごろまでTDMを遅らせてもよい。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ5 [draft]
- `VCM-TDM-009` 【ガイドラインに基づく推奨】ICUの重症患者では、より早期から頻回にTDMを行うことが推奨される。（I） — MATSUMOTO_VCM_TDM_2022 CQ5 [draft]
- `VCM-TDM-010` 【ガイドラインに基づく推奨】24時間ごとの投与で投与2日目の朝にTDMを予定する場合は、2点採血が強く勧められる。 — MATSUMOTO_VCM_TDM_2022 CQ5 [draft]
- `VCM-DOSE-001` 【ガイドラインに基づく推奨】投与1〜2日目の血中濃度を早く上げるため、腎機能にかかわらずVCMの負荷投与をルーチンに行う。（I） — MATSUMOTO_VCM_TDM_2022 CQ8 [draft]
- `VCM-DOSE-002` 【ガイドラインに基づく推奨】負荷投与はAKIのリスクを増加させない。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ8 [draft]
- `VCM-DOSE-003` 【ガイドラインに基づく推奨】VCMの負荷投与量は実体重あたり30 mg/kgが推奨される。1回量が3 gを超える場合は注意する。（II） — MATSUMOTO_VCM_TDM_2022 CQ9 [draft]
- `VCM-DOSE-004` 【ガイドラインに基づく推奨】腎機能が正常な場合のVCMの維持投与量は、実体重あたり20 mg/kgを12時間ごととする。1日量が4 gを超える場合は注意する。（II） — MATSUMOTO_VCM_TDM_2022 CQ9 [draft]
- `VCM-DOSE-005` 【ガイドラインに基づく推奨】eGFRが130 mL/min/1.73 m²以上などVCMのクリアランス亢進が想定される場合は、15〜20 mg/kgを8時間ごとに投与することを考慮する。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ9 [draft]
- `VCM-DOSE-006` 【ガイドラインに基づく推奨】VCMは1時間以上かけて点滴し、1回量が1 gを超える場合は0.5 gあたり30分を目安に点滴時間を延ばす。（II） — MATSUMOTO_VCM_TDM_2022 CQ9 [draft]
- `VCM-DOSE-007` 【ガイドラインに基づく推奨】ソフトウェアで予測した投与計画は、AUC 400〜600 μg·h/mLを達成するように設定する。限られた採血点に基づくモデルでは±20%程度の誤差を見込み、AUC 500（±100）を目標とする。（II） — MATSUMOTO_VCM_TDM_2022 CQ9 [draft]
- `VCM-DOSE-008` 【ガイドラインに基づく推奨】安全性の観点からは、定常状態のAUCより投与2日目のAUCのほうが適した指標である可能性がある。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ9 [draft]
- `VCM-DOSE-009` 【ガイドラインに基づく推奨】腎機能低下時は、体重とクレアチニンクリアランスに基づくノモグラムで初期投与量を決め、初期設計ではAUCの上限を400〜500に下げて過量投与を避ける。その後はベイズ推定でAUC 400〜600を目標に調整する。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ10 [draft]
- `VCM-DOSE-010` 【ガイドラインに基づく推奨】VCMの持続投与は、AUCガイドの間欠投与と比較したデータがないため、現時点では推奨されない。（III-B） — MATSUMOTO_VCM_TDM_2022 CQ7 [draft]
- `VCM-DOSE-011` 【ガイドラインに基づく推奨】VCMを持続投与する場合、一般には負荷投与15〜20 mg/kgの後に維持量30〜40 mg/kgを24時間かけて投与し、定常状態濃度20〜25 μg/mLを目標とする。（III-A） — MATSUMOTO_VCM_TDM_2022 CQ7 [draft]

### C3 選択と投与設計の統合

- `TEIC-DOSE-005` 【ガイドラインに基づく推奨】低アルブミン血症では遊離型の割合が増えるため総濃度は低くなる。負荷投与量の変更は不要だが、低アルブミン血症の程度に応じて目標値を下げることがある。（II） — HANAI_TEIC_TDM_2022 CQ8 [draft]
- `TEIC-SAFE-001` 【研究結果に基づく知見】ガイドラインの文献レビューでは、TEICのトラフ値が40 mg/L以上で血小板減少、60 mg/L以上で腎毒性との関連が示されている。 — HANAI_TEIC_TDM_2022 CQ2 literature review [draft]
- `LZD-TDM-001` 【研究結果に基づく知見】中国の専門家コンセンサスでは、リネゾリドのTDMを推奨し、目標トラフ値を2〜8 mg/Lとしている。 — LIN_LZD_CONSENSUS_2022 Expert panel recommendations (1)(2) [draft]
- `LZD-SAFE-001` 【研究結果に基づく知見】リネゾリドとその主な代謝物は約65%が腎以外の経路で排泄されるため、腎機能低下時の用量調節は通常不要とされるが、腎機能低下患者では血液毒性の頻度が高いことが報告されている。 — LZD_RENAL_BMCPT_2022 Background / Conclusion [draft]
- `LZD-SAFE-002` 【研究結果に基づく知見】63治療例の多変量解析で、治療期間10日以上とトラフ値8 mg/L超が血小板減少の独立した危険因子であった。 — THIROT_LZD_2024 Results [draft]

### C4 専門医の選択哲学

- `AWARE-001` 【ガイドラインに基づく推奨】WHOのAWaRe分類は、抗菌薬をAccess、Watch、Reserveの3群に分け、薬剤耐性への影響を考慮した適正使用と使用量のモニタリングを支援するための枠組みである。 — WHO_BULLETIN_RESERVE_2025 Introduction [draft]
- `AWARE-002` 【ガイドラインに基づく推奨】Reserve群の抗菌薬は多剤耐性菌感染症に対する最後の手段であり、他の選択肢が無効または不適切な場合に限って使用する。 — WHO_BULLETIN_RESERVE_2025 Definition [draft]

### C5 再評価・デエスカレーション

- `UK-MRSA-BSI-004` 【ガイドラインに基づく推奨】MRSA菌血症の抗菌薬治療期間は、非複雑性で最低14日間、複雑性で最低28日間を考慮する（英国ガイドライン）。（weak） — UK_MRSA_GL_2021 4.4 Bacteraemia [draft]
- `SEP-ABX-010` 【ガイドラインに基づく推奨】培養・感受性の結果に基づいてデエスカレーションを行うことが提案されている。（2C） — JSSCG_2024_JIC CQ2-9 [draft]
- `SEP-ABX-011` 【ガイドラインに基づく推奨】抗菌薬の中止判断の指標としてプロカルシトニンを用いることが提案されている。（2A） — JSSCG_2024_JIC CQ2-11 [draft]
- `SEP-ABX-012` 【ガイドラインに基づく推奨】敗血症の抗菌薬治療では、7日以内の短期間治療が提案されている。（2C） — JSSCG_2024_JIC CQ2-12 [draft]
