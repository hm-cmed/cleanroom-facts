# -*- coding: utf-8 -*-
"""事実票の定義（初版：2026-11-08、Claudeによる下書き）。

ここに書いた内容から facts/*.yaml を生成する（scripts/build_cards.py）。
レビュー後の修正は facts/*.yaml を直接編集してよい（このファイルは初版の記録として残す）。

各タプル: (fact_id, courses, topic, statement, evidence_class, grade, location/cq, conditions, review_notes)
"""

ADULT_MRSA = {"age_group": ["adult"], "infection_type": ["MRSA感染症"], "setting": ["hospital"]}
SEPSIS = {"age_group": ["adult", "pediatric"], "infection_type": ["敗血症・敗血症性ショック"], "setting": ["hospital", "ICU"]}

GROUPS = {}

# ---------------------------------------------------------------------------
# C2 バンコマイシン：AUCガイドTDM（Matsumoto 2022, CC BY）
# ---------------------------------------------------------------------------
GROUPS["C2_vancomycin_tdm_matsumoto2022"] = dict(
    source_id="MATSUMOTO_VCM_TDM_2022",
    population=ADULT_MRSA,
    expiry=["抗菌薬TDM臨床実践ガイドラインの改訂", "VCM添付文書の改訂"],
    cards=[
        ("VCM-PKPD-001", ["C2"], "VCMの有効性の指標",
         "MRSA感染症に対するVCMの有効性は、AUC/MIC（微量液体希釈法でMICを測定した場合）400以上を指標とする。",
         "guideline_recommendation", "I", "CQ6", ["MICを微量液体希釈法で測定した場合"], None),
        ("VCM-PKPD-002", ["C2"], "VCMの安全性の指標",
         "VCMによる急性腎障害（AKI）のリスクを下げるため、AUCは600 μg·h/mL以下に保つ。",
         "guideline_recommendation", "I", "CQ6", [], None),
        ("VCM-PKPD-003", ["C2"], "VCMの実用上の目標AUC",
         "実臨床でのVCMの目標AUCは400〜600 μg·h/mLとする（MICを1 μg/mLと仮定）。",
         "guideline_recommendation", "I", "CQ6", ["MIC 1 μg/mLを仮定"], None),
        ("VCM-PKPD-004", ["C2"], "MIC判明前と判明後の目標",
         "MICが判明する前の経験的治療では、MICを1 μg/mLと仮定してAUC 400以上を目標とし、MICが判明した後も目標AUCは原則として変えない。",
         "guideline_recommendation", "III-A", "CQ6", ["経験的治療の段階を含む"], None),
        ("VCM-PKPD-005", ["C2"], "Etest法でMICを測定した場合",
         "MICをEtest法で測定した場合のAUC/MICの目安は200以上とされている。",
         "guideline_recommendation", "III-A", "CQ6", ["MICをEtest法で測定した場合"],
         "学習者が微量液体希釈法との違いを誤解しないよう、提示の仕方を監修で確認"),
        ("VCM-PKPD-006", ["C2"], "トラフ値とAUCの関係",
         "VCMの投与設計では、トラフ値をAUCの代わりとして用いることは推奨されない。",
         "guideline_recommendation", "IV", "CQ2", [],
         "推奨度IVの意味（推奨しない）を原本の推奨度表で確認"),
        ("VCM-PKPD-007", ["C2"], "AUCガイドとトラフガイドの比較",
         "AUCを指標とした投与設計は、トラフ値を指標とした投与設計よりAKIのリスクを下げる傾向がある。",
         "guideline_recommendation", "III-A", "CQ2", [], "根拠となるメタ解析の数値は VCM-EVID-004 を参照"),
        ("VCM-TDM-001", ["C2"], "AUCガイドTDMの対象",
         "実施可能であれば、重症度にかかわらずVCM投与患者にはルーチンにAUCを指標とした投与設計を行うことが提案されている。",
         "guideline_recommendation", "III-A", "CQ3", [], None),
        ("VCM-TDM-002", ["C2"], "AUCガイドTDMを優先すべき患者",
         "ベイズ推定を日常的に使えない施設では、腎機能障害、ピペラシリン・タゾバクタムや利尿薬の併用、ICU入室など、AKIのリスクが高い患者を優先してAUCを指標とした投与設計を行う。",
         "guideline_recommendation", "II", "CQ3", ["ベイズ推定ソフトウェアを日常的に用いていない施設"], None),
        ("VCM-TDM-003", ["C2"], "2点採血",
         "AUCの推定には、トラフ値と投与終了1〜2時間後のピーク値の2点採血が推奨される。24時間ごとの投与でも同様である。",
         "guideline_recommendation", "II", "CQ4", [], None),
        ("VCM-TDM-004", ["C2"], "トラフ値のみによる推定",
         "12時間ごとに投与している軽症の感染症では、トラフ値1点のみでAUCを推定してもよい。",
         "guideline_recommendation", "III-A", "CQ4", ["軽症", "12時間ごとの投与"], None),
        ("VCM-TDM-005", ["C2"], "トラフ値のみで推定する場合の精度",
         "トラフ値のみからのAUC推定は、多点採血に基づく母集団薬物動態モデルを用いたベイズ推定ソフトウェアを使う場合に信頼性が高い。",
         "guideline_recommendation", "II", "CQ4", [], None),
        ("VCM-TDM-006", ["C2"], "トラフ値の採血時刻",
         "トラフ値は次回投与前30分以内に採血することが推奨されるが、ベイズ推定を用いる場合は採血時刻が前後しても実測時刻を入力すれば利用できる。",
         "guideline_recommendation", "III-A", "CQ4", [], "前半（30分以内）の推奨度を原本で確認"),
        ("VCM-TDM-007", ["C2"], "初回TDMの時期（重症・AKI高リスク）",
         "重症・複雑性感染症やAKIのリスクが高い患者では、定常状態に達する前の投与2日目にTDMを行うことを考慮する。",
         "guideline_recommendation", "III-A", "CQ5", ["重症・複雑性感染症、またはAKI高リスク"], None),
        ("VCM-TDM-008", ["C2"], "初回TDMの時期（軽症・中等症）",
         "AKIのリスクがない軽症〜中等症の感染症では、定常状態に近い投与3日目ごろまでTDMを遅らせてもよい。",
         "guideline_recommendation", "III-A", "CQ5", ["軽症〜中等症", "AKIリスクなし"], None),
        ("VCM-TDM-009", ["C2"], "集中治療患者のTDM",
         "ICUの重症患者では、より早期から頻回にTDMを行うことが推奨される。",
         "guideline_recommendation", "I", "CQ5", ["ICU入室中の重症患者"], None),
        ("VCM-TDM-010", ["C2"], "1日1回投与で2日目朝にTDMを行う場合",
         "24時間ごとの投与で投与2日目の朝にTDMを予定する場合は、2点採血が強く勧められる。",
         "guideline_recommendation", None, "CQ5", ["24時間ごとの投与"], "推奨度の記載がない項目。原本で確認"),
        ("VCM-DOSE-001", ["C2"], "負荷投与の必要性",
         "投与1〜2日目の血中濃度を早く上げるため、腎機能にかかわらずVCMの負荷投与をルーチンに行う。",
         "guideline_recommendation", "I", "CQ8", ["腎機能を問わない"], None),
        ("VCM-DOSE-002", ["C2"], "負荷投与とAKI",
         "負荷投与はAKIのリスクを増加させない。",
         "guideline_recommendation", "III-A", "CQ8", [], None),
        ("VCM-DOSE-003", ["C2"], "負荷投与量",
         "VCMの負荷投与量は実体重あたり30 mg/kgが推奨される。1回量が3 gを超える場合は注意する。",
         "guideline_recommendation", "II", "CQ9", ["実体重で計算"],
         "ガイドラインのノモグラムでは、やせた患者の過量投与を避けるため体重に応じて25〜30 mg/kgとしている点も併記するか監修で判断"),
        ("VCM-DOSE-004", ["C2"], "維持投与量（腎機能正常）",
         "腎機能が正常な場合のVCMの維持投与量は、実体重あたり20 mg/kgを12時間ごととする。1日量が4 gを超える場合は注意する。",
         "guideline_recommendation", "II", "CQ9", ["腎機能正常"], "適用条件（腎機能の範囲）を原本で確認"),
        ("VCM-DOSE-005", ["C2"], "腎クリアランス亢進時",
         "eGFRが130 mL/min/1.73 m²以上などVCMのクリアランス亢進が想定される場合は、15〜20 mg/kgを8時間ごとに投与することを考慮する。",
         "guideline_recommendation", "III-A", "CQ9", ["eGFR ≥130 mL/min/1.73 m²"], None),
        ("VCM-DOSE-006", ["C2"], "点滴時間",
         "VCMは1時間以上かけて点滴し、1回量が1 gを超える場合は0.5 gあたり30分を目安に点滴時間を延ばす。",
         "guideline_recommendation", "II", "CQ9", [], None),
        ("VCM-DOSE-007", ["C2"], "ソフトウェアによる投与設計の目標",
         "ソフトウェアで予測した投与計画は、AUC 400〜600 μg·h/mLを達成するように設定する。限られた採血点に基づくモデルでは±20%程度の誤差を見込み、AUC 500（±100）を目標とする。",
         "guideline_recommendation", "II", "CQ9", [], "後半（±20%、500±100）は推奨度III-A。カードを分けるか監修で判断"),
        ("VCM-DOSE-008", ["C2"], "2日目のAUC",
         "安全性の観点からは、定常状態のAUCより投与2日目のAUCのほうが適した指標である可能性がある。",
         "guideline_recommendation", "III-A", "CQ9", [], None),
        ("VCM-DOSE-009", ["C2"], "腎機能低下時の初期投与設計",
         "腎機能低下時は、体重とクレアチニンクリアランスに基づくノモグラムで初期投与量を決め、初期設計ではAUCの上限を400〜500に下げて過量投与を避ける。その後はベイズ推定でAUC 400〜600を目標に調整する。",
         "guideline_recommendation", "III-A", "CQ10", ["腎機能低下"], "ベイズ推定による調整の部分は推奨度II。ノモグラムの数値（表）はCC BYのため抽出予定（GAP-C2-NOMOGRAM）"),
        ("VCM-DOSE-010", ["C2"], "持続投与",
         "VCMの持続投与は、AUCガイドの間欠投与と比較したデータがないため、現時点では推奨されない。",
         "guideline_recommendation", "III-B", "CQ7", [], None),
        ("VCM-DOSE-011", ["C2"], "持続投与を行う場合の一般的な方法",
         "VCMを持続投与する場合、一般には負荷投与15〜20 mg/kgの後に維持量30〜40 mg/kgを24時間かけて投与し、定常状態濃度20〜25 μg/mLを目標とする。",
         "guideline_recommendation", "III-A", "CQ7", ["持続投与を選択した場合"], "初期版で扱うか（適用範囲）監修で判断"),
    ])

# ---------------------------------------------------------------------------
# C2 バンコマイシン：メタ解析（Tsutsuura 2021, CC BY）
# ---------------------------------------------------------------------------
GROUPS["C2_vancomycin_evidence_tsutsuura2021"] = dict(
    source_id="TSUTSUURA_VCM_MA_2021",
    population=ADULT_MRSA,
    expiry=["新たな系統的レビューの公表"],
    cards=[
        ("VCM-EVID-001", ["C2"], "トラフ値とAKI",
         "VCMのトラフ値が20 μg/mL以上の場合、15〜20 μg/mLの場合と比べてAKIの発生が有意に多い（オッズ比2.39、95%信頼区間1.78〜3.20）。",
         "peer_reviewed_evidence", None, "Results", [], None),
        ("VCM-EVID-002", ["C2"], "AUC/MICと治療失敗",
         "AUC/MICが高い群（カットオフ400±15%）では、治療失敗が有意に少ない（オッズ比0.28、95%信頼区間0.18〜0.45）。",
         "peer_reviewed_evidence", None, "Results", [], None),
        ("VCM-EVID-003", ["C2"], "AUCとAKI",
         "AUCが高い群（カットオフ600±15%）では、AKIのリスクが有意に高い（オッズ比2.10、95%信頼区間1.13〜3.89）。",
         "peer_reviewed_evidence", None, "Results", [], None),
        ("VCM-EVID-004", ["C2"], "AUCガイドとトラフガイドの比較（メタ解析）",
         "4研究のメタ解析では、AUCガイドのモニタリングはトラフガイドよりAKIが少ない傾向を示したが有意ではなく（オッズ比0.54、95%信頼区間0.28〜1.01）、死亡率にも有意差はなかった。",
         "peer_reviewed_evidence", None, "Results", [], None),
        ("VCM-EVID-005", ["C2"], "MRSA菌血症でのトラフ値",
         "成人のMRSA菌血症では、VCMトラフ値15 μg/mL以上の群で治療失敗が有意に少なかった（オッズ比0.63、95%信頼区間0.47〜0.85）。",
         "peer_reviewed_evidence", None, "Results", ["成人MRSA菌血症"],
         "トラフ値を高く保つことを推奨する根拠と誤解されないよう、VCM-EVID-001（AKIの増加）と併せて提示"),
    ])

# ---------------------------------------------------------------------------
# C2 テイコプラニン（Hanai 2022, CC BY-NC：非営利のみ）
# ---------------------------------------------------------------------------
GROUPS["C2_teicoplanin_tdm_hanai2022"] = dict(
    source_id="HANAI_TEIC_TDM_2022",
    population=ADULT_MRSA,
    expiry=["抗菌薬TDM臨床実践ガイドラインの改訂", "TEIC添付文書の改訂"],
    cards=[
        ("TEIC-PKPD-001", ["C2", "C3"], "TEICのPK/PD指標",
         "TEICの主要なPK/PD指標はAUC/MICだが、AUCを推定するソフトウェアが使えない施設が多いため、実臨床ではトラフ値を代替指標として用いる。",
         "guideline_recommendation", "II", "CQ1", [], None),
        ("TEIC-TDM-001", ["C2", "C3"], "TEICのTDMを計画すべき患者",
         "重症感染症、急性・慢性の腎機能障害、肥満または低体重、熱傷、低アルブミン血症、小児では、TEICのTDMを計画する。",
         "guideline_recommendation", "I", "CQ2", [], None),
        ("TEIC-TDM-002", ["C2", "C3"], "TEICの初回TDMの時期",
         "TEICは半減期が長いため、初回TDMは定常状態に達する前の投与4日目に行い、その値をトラフ値の代替とする。",
         "guideline_recommendation", "II", "CQ3", [], None),
        ("TEIC-TDM-003", ["C2", "C3"], "TEICの目標トラフ値（非複雑性）",
         "非複雑性のMRSA感染症では、腎機能にかかわらずTEICの目標トラフ値を15〜30 mg/Lとする。",
         "guideline_recommendation", "I", "CQ4", ["非複雑性MRSA感染症"], None),
        ("TEIC-TDM-004", ["C2", "C3"], "TEICの目標トラフ値（複雑性・重症）",
         "心内膜炎や骨髄炎などの複雑性・重症のMRSA感染症では、TEICの目標トラフ値を20〜40 mg/Lとすることが提案されている。",
         "guideline_recommendation", "III-A", "CQ5", ["複雑性・重症MRSA感染症"], None),
        ("TEIC-DOSE-001", ["C2", "C3"], "TEICの負荷投与（腎機能正常、目標15〜30 mg/L）",
         "腎機能正常で目標トラフ値15〜30 mg/Lの場合、最初の3日間に実体重あたり10 mg/kgを5回、または12 mg/kgを4回投与する。",
         "guideline_recommendation", "II", "CQ6", ["腎機能正常", "実体重で計算"], None),
        ("TEIC-DOSE-002", ["C2", "C3"], "TEICの負荷投与（腎機能正常、目標20〜40 mg/L）",
         "腎機能正常で目標トラフ値20〜40 mg/Lの場合、最初の3日間に12 mg/kgを5回（1・2日目は1日2回、3日目は1日1回）投与する。",
         "guideline_recommendation", "II", "CQ6", ["腎機能正常"], None),
        ("TEIC-DOSE-003", ["C2", "C3"], "TEICの維持投与（腎機能正常）",
         "腎機能正常で目標トラフ値15〜30 mg/Lの場合、維持投与量は6〜6.7 mg/kgを1日1回とする。20 mg/L以上を目標とする場合はより多い維持量を考慮し、維持投与4〜5回目の前に早めにTDMを行う。",
         "guideline_recommendation", "II", "CQ6", ["腎機能正常"], "後半（高い維持量の考慮）は推奨度III-A"),
        ("TEIC-DOSE-004", ["C2", "C3"], "TEICの腎機能低下時の投与",
         "腎機能低下時も3日間の負荷投与を行い、投与量はeGFRと実体重に応じて調整する。維持投与は1回量、投与間隔またはその両方で減量し、TDMで確認する。",
         "guideline_recommendation", "II", "CQ7", ["腎機能低下"], "維持投与の減量は推奨度III-A。eGFR別の具体的レジメン（表3）を事実票に追加するか監修で判断（非営利限定）"),
        ("TEIC-DOSE-005", ["C3"], "低アルブミン血症",
         "低アルブミン血症では遊離型の割合が増えるため総濃度は低くなる。負荷投与量の変更は不要だが、低アルブミン血症の程度に応じて目標値を下げることがある。",
         "guideline_recommendation", "II", "CQ8", ["低アルブミン血症"], "負荷投与量変更不要はIII-C、目標値を下げるはIII-A"),
        ("TEIC-SAFE-001", ["C3"], "TEICの有害事象と血中濃度",
         "ガイドラインの文献レビューでは、TEICのトラフ値が40 mg/L以上で血小板減少、60 mg/L以上で腎毒性との関連が示されている。",
         "peer_reviewed_evidence", None, "CQ2 literature review", [], "推奨文ではなく文献レビュー部分の記載"),
    ])

# ---------------------------------------------------------------------------
# C1/C5 敗血症の抗菌薬治療（J-SSCG 2024 JIC版, CC BY）
# ---------------------------------------------------------------------------
GROUPS["C1_C5_sepsis_antimicrobial_jsscg2024"] = dict(
    source_id="JSSCG_2024_JIC",
    population=SEPSIS,
    expiry=["日本版敗血症診療ガイドラインの改訂"],
    cards=[
        ("SEP-ABX-001", ["C1"], "血液培養",
         "敗血症が疑われる患者では、抗菌薬投与前に少なくとも2セットの血液培養を採取する。",
         "guideline_recommendation", "Good Practice Statement", "CQ1-4", [], None),
        ("SEP-ABX-002", ["C1"], "感染巣の培養",
         "敗血症が疑われる患者では、抗菌薬投与前に感染が疑われる部位からも培養検体を採取する。",
         "guideline_recommendation", "Good Practice Statement", "CQ1-4", [], None),
        ("SEP-ABX-003", ["C1"], "グラム染色",
         "敗血症の経験的抗菌薬の選択にグラム染色を用いることが提案されている。",
         "guideline_recommendation", "2C", "CQ2-1", [], None),
        ("SEP-ABX-004", ["C1"], "抗菌薬投与開始のタイミング",
         "敗血症と診断したらできるだけ早く抗菌薬を開始するが、1時間以内という厳格な時間目標を設けないことが提案されている。",
         "guideline_recommendation", "2C", "CQ2-2", [], None),
        ("SEP-ABX-005", ["C1"], "経験的抗菌薬の選び方",
         "経験的抗菌薬は、推定される感染巣と想定される菌に基づき、患者背景、地域・施設の疫学、迅速検査、組織移行性、耐性菌のリスクを考慮して選ぶ。",
         "guideline_recommendation", "Background Question", "CQ2-3", [], None),
        ("SEP-ABX-006", ["C1"], "抗MRSA薬を経験的に加える場面",
         "感染巣、患者背景、微生物学的情報からMRSAの関与が疑われる場合に、経験的治療に抗MRSA薬を加える（推奨度を付さない背景情報として記載）。",
         "guideline_recommendation", "Background Question", "CQ2-5", [],
         "どの患者背景をMRSAのリスクとみなすかの具体的な基準はない（GAP-C1-RISK）"),
        ("SEP-ABX-007", ["C2"], "腎機能に応じた投与量調整",
         "敗血症では、腎機能の推移、体液量の変化、腎代替療法などの体外循環の有無を踏まえて抗菌薬の投与量を調整する。",
         "guideline_recommendation", "Background Question", "CQ2-6", [], None),
        ("SEP-ABX-008", ["C2"], "グリコペプチド系の持続・延長投与",
         "グリコペプチド系抗菌薬（VCMなど）では、持続投与・延長投与を行わないことが提案されている（β-ラクタム系では行うことが提案されている：2B）。",
         "guideline_recommendation", "2C", "CQ2-7", [], None),
        ("SEP-ABX-009", ["C2"], "TDMに基づく投与",
         "敗血症の抗菌薬治療では、TDMに基づいて投与量を調整することが提案されている。",
         "guideline_recommendation", "2D", "CQ2-8", [], None),
        ("SEP-ABX-010", ["C5"], "デエスカレーション",
         "培養・感受性の結果に基づいてデエスカレーションを行うことが提案されている。",
         "guideline_recommendation", "2C", "CQ2-9", [], None),
        ("SEP-ABX-011", ["C5"], "プロカルシトニンによる中止判断",
         "抗菌薬の中止判断の指標としてプロカルシトニンを用いることが提案されている。",
         "guideline_recommendation", "2A", "CQ2-11", [], None),
        ("SEP-ABX-012", ["C5"], "治療期間",
         "敗血症の抗菌薬治療では、7日以内の短期間治療が提案されている。",
         "guideline_recommendation", "2C", "CQ2-12", [],
         "黄色ブドウ球菌菌血症など長期治療が必要な病態への誤った適用を防ぐ注記が必要（UK-MRSA-BSI-004と併せて提示）"),
    ])

# ---------------------------------------------------------------------------
# C1/C3/C5 MRSA感染症の病態別治療（UK 2021, CC BY）
# ---------------------------------------------------------------------------
GROUPS["C1_C5_mrsa_treatment_uk2021"] = dict(
    source_id="UK_MRSA_GL_2021",
    population={"age_group": ["adult"], "infection_type": ["MRSA感染症"], "setting": ["hospital", "community"]},
    expiry=["英国MRSA治療ガイドラインの改訂"],
    cards=[
        ("UK-MRSA-BSI-001", ["C1"], "MRSA菌血症の第一選択",
         "非複雑性のMRSA菌血症では、VCMの静脈内投与を用いる（英国ガイドライン）。",
         "guideline_recommendation", "strong", "4.4 Bacteraemia", ["非複雑性菌血症"], "英国の推奨であることを表示。日本のガイドラインとの異同は監修で確認"),
        ("UK-MRSA-BSI-002", ["C1"], "VCMが使えない場合の菌血症",
         "MRSA菌血症でVCMが禁忌の場合は、リネゾリドを代替の第一選択とする（英国ガイドライン）。",
         "guideline_recommendation", "strong", "4.4 Bacteraemia", ["VCMが禁忌"], None),
        ("UK-MRSA-BSI-003", ["C1"], "第一選択薬が使えない場合の菌血症",
         "MRSA菌血症で第一選択薬が禁忌の場合は、ダプトマイシンまたはテイコプラニンを考慮する（英国ガイドライン）。",
         "guideline_recommendation", "weak", "4.4 Bacteraemia", ["第一選択薬が禁忌"], None),
        ("UK-MRSA-BSI-004", ["C5"], "MRSA菌血症の治療期間",
         "MRSA菌血症の抗菌薬治療期間は、非複雑性で最低14日間、複雑性で最低28日間を考慮する（英国ガイドライン）。",
         "guideline_recommendation", "weak", "4.4 Bacteraemia", [], "複雑性・非複雑性の定義は別カードが必要（GAP-C5-SAB-DEF）"),
        ("UK-MRSA-PNA-001", ["C1"], "院内肺炎の第一選択",
         "MRSAによる院内肺炎では、VCMまたはリネゾリドの静脈内投与を第一選択とする（英国ガイドライン。リネゾリドの優越性を確認する追加試験がないため）。",
         "guideline_recommendation", "weak", "4.6.2 Nosocomial pneumonia", [], None),
        ("UK-MRSA-PNA-002", ["C1", "C3"], "肺炎にダプトマイシンを使わない",
         "ダプトマイシンは肺サーファクタントで不活化されるため、MRSAによる院内肺炎の治療に用いない（英国ガイドライン）。",
         "guideline_recommendation", "strong", "4.6.2 Nosocomial pneumonia", [], None),
        ("UK-MRSA-PNA-003", ["C1"], "壊死性肺炎",
         "MRSAによる壊死性肺炎では、VCMまたはリネゾリドの静脈内投与を用いる（英国ガイドライン）。",
         "guideline_recommendation", "strong", "Necrotizing pneumonia", [], None),
        ("UK-MRSA-SSTI-001", ["C1"], "重症の皮膚軟部組織感染症",
         "MRSAによる重症の蜂窩織炎・軟部組織感染症では、グリコペプチド系（VCMまたはテイコプラニン）の静脈内投与を用い、代替としてリネゾリド（経口または静注）またはダプトマイシン（静注）を用いる（英国ガイドライン）。",
         "guideline_recommendation", "strong", "SSTI", ["重症"], None),
        ("UK-MRSA-UTI-001", ["C1"], "MRSA尿路感染症",
         "尿からMRSAが分離された場合は、治療開始前に菌血症の有無を確認する。複雑性尿路感染症ではグリコペプチド系の静脈内投与を第一選択として考慮し、リネゾリドは腎からの排泄が少ないため推奨しない（英国ガイドライン）。",
         "guideline_recommendation", "weak", "UTI", [], None),
        ("UK-MRSA-BJI-001", ["C1"], "骨・関節感染症",
         "MRSAによる骨・関節感染症の治療は、必要に応じた手術やドレナージを含む多職種チームで行う（英国ガイドライン）。",
         "guideline_recommendation", "strong", "Bone and joint infection", [], None),
    ])

# ---------------------------------------------------------------------------
# C1/C4 AWaRe分類（WHO）
# ---------------------------------------------------------------------------
GROUPS["C1_C4_aware_who2025"] = dict(
    source_id="WHO_BULLETIN_RESERVE_2025",
    population={"age_group": ["adult", "pediatric"], "infection_type": ["細菌感染症全般"], "setting": ["all"]},
    expiry=["WHO AWaRe分類の改訂（隔年）", "WHO必須医薬品リストの改訂"],
    cards=[
        ("AWARE-001", ["C4"], "AWaRe分類の目的",
         "WHOのAWaRe分類は、抗菌薬をAccess、Watch、Reserveの3群に分け、薬剤耐性への影響を考慮した適正使用と使用量のモニタリングを支援するための枠組みである。",
         "guideline_recommendation", None, "Introduction", [], "出典ライセンス要確認（WHO Bulletin）。WHO_AWARE_CLASSIFICATION_2025 でも確認できる内容"),
        ("AWARE-002", ["C4"], "Reserve群の位置づけ",
         "Reserve群の抗菌薬は多剤耐性菌感染症に対する最後の手段であり、他の選択肢が無効または不適切な場合に限って使用する。",
         "guideline_recommendation", None, "Definition", [], None),
        ("AWARE-003", ["C1", "C4"], "VCMはWatch群",
         "VCMはWatch群に分類される。MRSA（WHO優先病原体リストの高優先度）による感染症では、Watch群のVCMが適切な選択肢となりうる。",
         "guideline_recommendation", None, "Main text", [], None),
        ("AWARE-004", ["C1", "C4"], "リネゾリド・テジゾリドはReserve群",
         "2025年版WHO必須医薬品リストに収載されたReserve群の抗菌薬には、リネゾリドとテジゾリドが含まれる。",
         "guideline_recommendation", None, "Box / Main text", [], "ダプトマイシン・テイコプラニンの分類はWHO原表で照合（GAP-C4-AWARE）"),
    ])

# ---------------------------------------------------------------------------
# C3 リネゾリド（CC BY）
# ---------------------------------------------------------------------------
GROUPS["C3_linezolid_tdm"] = dict(
    source_id=None,  # cards specify their own source
    population=ADULT_MRSA,
    expiry=["リネゾリドTDMに関する国内ガイドラインの公表"],
    cards=[
        ("LZD-TDM-001", ["C3"], "リネゾリドの目標トラフ値（海外コンセンサス）",
         "中国の専門家コンセンサスでは、リネゾリドのTDMを推奨し、目標トラフ値を2〜8 mg/Lとしている。",
         "peer_reviewed_evidence", None, "Expert panel recommendations (1)(2)", [],
         "LIN_LZD_CONSENSUS_2022。国内の推奨ではないことを明示。日本での目標値は専門家意見で確認（GAP-C3-LZD）"),
        ("LZD-SAFE-001", ["C3"], "リネゾリドの排泄と腎機能",
         "リネゾリドとその主な代謝物は約65%が腎以外の経路で排泄されるため、腎機能低下時の用量調節は通常不要とされるが、腎機能低下患者では血液毒性の頻度が高いことが報告されている。",
         "peer_reviewed_evidence", None, "Background / Conclusion", ["腎機能低下"],
         "LZD_RENAL_BMCPT_2022。安全なトラフ値の目安（6〜7 μg/mL以下）を併記するか監修で判断"),
        ("LZD-SAFE-002", ["C3"], "リネゾリドによる血小板減少の危険因子",
         "63治療例の多変量解析で、治療期間10日以上とトラフ値8 mg/L超が血小板減少の独立した危険因子であった。",
         "peer_reviewed_evidence", None, "Results", [], "THIROT_LZD_2024"),
    ])
CARD_SOURCES = {"LZD-TDM-001": "LIN_LZD_CONSENSUS_2022",
                "LZD-SAFE-001": "LZD_RENAL_BMCPT_2022",
                "LZD-SAFE-002": "THIROT_LZD_2024"}
