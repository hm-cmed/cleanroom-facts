"""Phase 3-2: 食道カードの内容照合の結果を反映する（2026-10-12）。

人間が 2026-10-12 にチャットで委任した範囲（docs: reports/03_es_content.md）:
- 再調査で一次資料（PubMed 抄録・PMC のオープンアクセス本文・公的資料）と照合できた修正は、
  根拠を history に記録して自動反映する（CLAUDE.md 1-2 の例外）。
- 欠番 7 件のうち出典が得られたものを起票する。
- 照合が済んだカードを verified_sources に上げる（verified_expert は人間のみ）。

主張文はすべて自作文。抄録などの文言は写さない。
各修正の根拠（どの資料のどこで確認したか）は EVIDENCE に書き、history とレポートに残す。
"""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
ES = ROOT / "data" / "facts" / "ES.yaml"
REPORT = ROOT / "reports" / "03_es_content.md"
SCHEMA = ROOT / "schema" / "fact.schema.json"
TODAY = dt.date.today().isoformat()
BY = "claude-code"
DELEGATION = "人間が2026-10-12にチャットで委任"

# ---------------------------------------------------------------- 出典（API で識別子を確認済み）
SRC = {
    "JSGE_GERD": {"source": "Iwakiri K, et al. Evidence-based clinical practice guidelines for gastroesophageal reflux disease 2021. J Gastroenterol 2022;57:267-285",
                  "doi": "10.1007/s00535-022-01861-z", "pmid": "35226174", "pmcid": "PMC8938399",
                  "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8938399/", "source_license": "CC BY 4.0（Crossref）",
                  "legal_basis": "B", "source_class": "OPEN"},
    "LUNDELL": {"doi": "10.1136/gut.45.2.172", "pmid": "10403727", "pmcid": "PMC1727604"},
    "AGREE": {"source": "Dellon ES, et al. Updated international consensus diagnostic criteria for eosinophilic esophagitis: proceedings of the AGREE conference. Gastroenterology 2018;155:1022-1033",
              "doi": "10.1053/j.gastro.2018.07.009", "pmid": "30009819", "pmcid": "PMC6174113"},
    "HIRANO": {"source": "Hirano I, et al. Endoscopic assessment of the oesophageal features of eosinophilic oesophagitis: validation of a novel classification and grading system. Gut 2013;62:489-495",
               "doi": "10.1136/gutjnl-2011-301817", "pmid": "22619364", "pmcid": None, "url": None,
               "source_license": "BMJ（CC表示は未確認）", "legal_basis": "B", "source_class": "RESTRICTED"},
    "ACG_ACHALASIA": {"source": "Vaezi MF, et al. ACG clinical guidelines: diagnosis and management of achalasia. Am J Gastroenterol 2020;115:1393-1411",
                      "doi": "10.14309/ajg.0000000000000731", "pmid": "32773454", "pmcid": "PMC9896940",
                      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9896940/", "source_license": "© ACG（PMC 著者稿、CC表示なし）",
                      "legal_basis": "B", "source_class": "RESTRICTED"},
    "CONTINI": {"doi": "10.3748/wjg.v19.i25.3918"},
    "METGES": {"pmid": "41259897"},
}

# ---------------------------------------------------------------- 根拠
EVIDENCE = {
    "PM41259897": "Metges JP, ESMO Open 2025（PMID 41259897）の抄録：5年生存率 10.6% 対 3.0%",
    "PM34454674": "Sun JM, Lancet 2021（PMID 34454674）の抄録",
    "PM33789008": "Kelly RJ, NEJM 2021（PMID 33789008）の抄録：794例（532対262）、DFS 22.4対11.0か月、HR 0.69",
    "PM35108470": "Doki Y, NEJM 2022（PMID 35108470）の抄録：970例、PD-L1≥1%と全体集団でOS延長",
    "PM38876133": "Kato K, Lancet 2024（PMID 38876133）の抄録：601例、3年OS 72.1%対62.6%、HR 0.68、CF-RTは有意差なし",
    "PM31800987": "Werner YB, NEJM 2019（PMID 31800987）の抄録：221例、83.0%対81.7%、逆流性食道炎 57/20%・44/29%、重篤AE 2.7%対7.3%",
    "PM36546624": "Dellon ES, NEJM 2022（PMID 36546624）の抄録：Part A 組織学的寛解 60%（25/42）対 5%（2/39）",
    "PM23281973": "Villanueva C, NEJM 2013（PMID 23281973）の抄録：921例、Hb 7 対 9 g/dL",
    "PM20573925": "García-Pagán JC, NEJM 2010（PMID 20573925）の抄録：63例、1年生存 86%対61%",
    "GERD_GL": "JSGE GERD GL 2021 英語版本文（PMC8938399、CC BY）",
    "JES_GL": "日本食道学会 食道癌診療GL 2022 Part 1 本文（PMC10024303、CC BY）",
    "ACG_BE": "ACG Barrett GL 2022 本文（PMC10259184）",
    "CCV4": "Chicago Classification v4.0 本文（PMC8034247、NIH著者稿）",
    "LYON2": "Lyon consensus 2.0 本文（PMC10846564、CC BY-NC）",
    "BAVENO": "Baveno VII 本文（PMC11090185、著者稿）",
    "AGREE": "AGREE 2018（PMID 30009819）の抄録",
    "HIRANO": "Hirano 2013（PMID 22619364）の抄録",
    "ACG_ACH": "ACG アカラシアGL 2020 本文（PMC9896940）の Recommendation 9",
    "K653": "診療報酬点数表（令和8年版）K653-6 12,000点（clinicalsup.jp の点数表ページ、2026-10-12 閲覧）",
    "DUPI_JP": "サノフィ デュピクセント IF（2026年3月改訂 第20版）と国内報道の検索（2026-10-12）。国内のEoE承認の記録なし",
}

# ---------------------------------------------------------------- 内容の修正
# id: {"set": {ドット区切りのパス: 値}, "why": 理由, "ev": [EVIDENCE のキー]}
FIXES = {
    "ES-054": {"set": {
        "assertion.plain_statement_ja": "進行食道癌の一次治療で、ペムブロリズマブ＋化学療法はプラセボ＋化学療法より全生存を改善した。追跡中央値58.8か月での5年全生存率は10.6%対3.0%だった。",
        "provenance.source": "Metges JP, et al. KEYNOTE-590 5-year extended follow-up. ESMO Open 2025;10(12):105854（原著：Sun JM, Lancet 2021;398:759-771, PMID 34454674）",
        "provenance.pmid": "41259897",
        "uncertainty": "low（5年生存率は5年追跡論文の抄録で照合）"},
        "why": "5年生存率を v2 の 10.9%対3.1% から、一次資料の 10.6%対3.0% に訂正。pmid は原著のものだったため、DOI と同じ5年追跡論文の PMID に置き換え（原著の PMID は source に記載）",
        "ev": ["PM41259897", "PM34454674"]},
    "ES-007": {"set": {
        "assertion.plain_statement_ja": "日本の成人における逆流性食道炎の有病率は約10%と推定されている。",
        "uncertainty": "low（JSGE GERD GL 2021 の疫学の記載で照合。原典はGLの引用文献）"},
        "why": "GL本文に同じ推定値の記載があることを確認したため、主張文の括弧書き「（引用元の原典と数値は要確認）」を削除",
        "ev": ["GERD_GL"]},
    "ES-003": {"set": {
        "provenance.corroboration": "GL本文：重症REの初期治療はボノプラザン20 mgを4週、維持は10 mg",
        "uncertainty": "low（推奨の方向と用量をGL本文で照合）"},
        "why": "用量をGL本文で確認", "ev": ["GERD_GL"]},
    "ES-008": {"set": {
        **{f"provenance.{k}": v for k, v in SRC["JSGE_GERD"].items()},
        "provenance.corroboration": "GL本文：多チャンネルインピーダンス・pHモニタリングで酸・非酸逆流を検出でき、治療抵抗例の病態評価に推奨",
        "uncertainty": "low（GL本文で照合）"},
        "why": "出典未取得だったカードに JSGE GERD GL 2021 を出典として設定", "ev": ["GERD_GL"]},
    "ES-010": {"set": {
        "assertion.plain_statement_ja": "PPIテスト（PPIを試験的に投与し、症状が改善するかで判断する方法）は低侵襲・低コストで実地診療に用いられるが、24時間pH検査を基準とした統合解析では感度0.78、特異度0.54と診断精度に限界がある。",
        "assertion.differential": "P-CABテスト（JSGE 2021はPPIテストより有用な可能性があるとしている）",
        "uncertainty": "low（GL本文で照合）"},
        "why": "GL本文に「陰性でも否定できない」旨の記載は確認できず、代わりに感度・特異度の数値を確認したため主張文を差し替え。P-CABテストの位置づけ（FRQ）も確認",
        "ev": ["GERD_GL"]},
    "ES-011": {"set": {
        "assertion.plain_statement_ja": "JSGE 2021は、薬物治療に抵抗するGERDで逆流と症状の関連が確認できた場合に、逆流防止手術を選択肢としている。PPI抵抗性NERDでは、多チャンネルインピーダンス・pHモニタリングで症状と逆流の因果関係が示された場合に手術を提案している（弱い推奨）。",
        "assertion.differential": "内視鏡的逆流防止術（ARMS）の保険収載は ES-093",
        "provenance.corroboration": "GL本文に ARMS の記載はない",
        "uncertainty": "low（GL本文で照合）"},
        "why": "GL本文に ARMS と「長期の薬物依存を避けたい症例」の記載がないため、GLで確認できた手術適応の記述に差し替え",
        "ev": ["GERD_GL"]},
    "ES-005": {"set": {
        **{f"provenance.{k}": v for k, v in SRC["LUNDELL"].items()},
        "uncertainty": "medium（グレードの定義はPMCでは抄録しか読めず、本文で未照合）"},
        "why": "PubMed で書誌を特定し識別子を設定", "ev": []},
    "ES-014": {"set": {
        "assertion.plain_statement_ja": "ACG 2022は、Barrett食道の癌への進展率を、異形成なし（NDBE）で年0.05〜0.2%程度、低異型度異形成（LGD）で年約0.7%と見積もっている。",
        "provenance.corroboration": "同GLの多施設コホートでは、NDBEの癌化率は3 cm未満で年0.07%、3 cm以上で年0.25%",
        "uncertainty": "low（GL本文で照合。本文の表記は「0.2%–0.05%」）"},
        "why": "2022年版の本文で確認できた数値に訂正。HGDの年約7%は2022年版本文に記載がないため削除",
        "ev": ["ACG_BE"]},
    "ES-019": {"set": {
        **{f"provenance.{k}": v for k, v in SRC["AGREE"].items()},
        "uncertainty": "low（抄録で照合）"},
        "why": "PubMed で書誌を特定し識別子を設定", "ev": ["AGREE"]},
    "ES-021": {"set": {
        **{f"provenance.{k}": v for k, v in SRC["HIRANO"].items()},
        "assertion.plain_statement_ja": "EoEの典型的な内視鏡所見は、輪状溝、縦走溝、白斑（滲出物）、浮腫で、狭窄を伴うこともある。これらはEREFSで点数化する。",
        "uncertainty": "low（抄録で照合）"},
        "why": "出典未取得だったカードに Hirano 2013 を設定。所見の列挙を出典に合わせて整理（主要4所見と追加所見の狭窄）",
        "ev": ["HIRANO"]},
    "ES-027": {"set": {
        "assertion.plain_statement_ja": "Chicago分類v4.0は、HRMで判定が確定しない例（判定保留）では、錠剤を併用した時限バリウム食道造影（TBE）やFLIPを補助検査として用いるよう勧めている。",
        "assertion.differential": "v3.0との違い（補助検査の位置づけの明確化）",
        "uncertainty": "low（本文で照合）"},
        "why": "「正常値データベースを75人から469人に拡大」は本文に記載がなく出典を確認できないため削除。補助検査の記述は本文で確認",
        "ev": ["CCV4"]},
    "ES-028": {"set": {"uncertainty": "low（本文で照合：DL 4.5秒未満かつDCI 450以上を早期収縮とする）"},
               "why": "DLの閾値を本文で確認", "ev": ["CCV4"]},
    "ES-031": {"set": {
        "assertion.plain_statement_ja": "Chicago分類v4.0は、オピオイドがIII型アカラシアと関連するとし、可能であればオピオイドを中止した状態でHRMを行うよう勧めている。EGJ流出路障害（EGJOO）の一部もオピオイド使用に関連する。",
        "uncertainty": "low（本文で照合）"},
        "why": "v2 の主張文のうち、機序（IRP上昇・DL短縮）は本文に記載がないため、本文で確認できた内容に差し替え",
        "ev": ["CCV4"]},
    "ES-034": {"set": {
        **{f"provenance.{k}": v for k, v in SRC["ACG_ACHALASIA"].items()},
        "assertion.plain_statement_ja": "ACG 2020は、III型アカラシアには空気圧拡張術（PD）より有効な治療として、筋切開長を病変に合わせて延ばしたPOEM（tailored POEM）またはLHMを推奨している。III型はLESに限った治療では成績が劣り、長い筋切開が重要と考えられている。",
        "uncertainty": "low（GL本文 Recommendation 9 で照合）"},
        "why": "出典未取得で主張文に「要確認」が残っていたカード。ACG 2020 本文で推奨を確認し、出典を設定して主張文を確定",
        "ev": ["ACG_ACH"]},
    "ES-040": {"set": {
        "assertion.differential": "ALDH2ヘテロ型の飲酒者のオッズ比は ES-092",
        "uncertainty": "low（GL本文で照合）"},
        "why": "アセトアルデヒドの Group 1 指定（2009年10月）と遺伝要因の記載をGL本文で確認。数値は ES-092 が担う",
        "ev": ["JES_GL"]},
    "ES-041": {"set": {
        "assertion.plain_statement_ja": "食道癌は、同時性・異時性の多重癌を伴うことが多い。",
        "assertion.differential": "頭頸部癌・胃癌の合併（この出典には具体的な記載がない）",
        "uncertainty": "low（GL本文で照合）"},
        "why": "GL本文で確認できたのは多重癌が多いことまで。頭頸部癌・胃癌の具体名と「要確認」の括弧書きを主張文から外した",
        "ev": ["JES_GL"]},
    "ES-073": {"set": {"provenance.doi": SRC["CONTINI"]["doi"]}, "why": "Crossref の候補（著者・誌名・年・巻が一致）から DOI を設定", "ev": []},
    "ES-075": {"set": {"provenance.doi": SRC["CONTINI"]["doi"]}, "why": "Crossref の候補（著者・誌名・年・巻が一致）から DOI を設定", "ev": []},
    "ES-093": {"set": {"uncertainty": "low（令和8年版点数表でも12,000点）"}, "why": "令和8年度改定後も点数が変わらないことを確認", "ev": ["K653"]},
    "ES-091": {"set": {"uncertainty": "low〜medium（2026年10月時点の検索でも国内のEoE承認の記録なし。PMDAの承認一覧での直接照合は未了）"},
               "why": "2026年時点の国内承認状況を再調査", "ev": ["DUPI_JP"]},
}

# 2回目（1回目の昇格判定で、照合済みなのに補助欄の「要確認」が残っていたもの等）
EVIDENCE.update({
    "CHENG": "Cheng HT, BMC Gastroenterol 2008（PMC2533005）の本文：Zargar の6段階分類",
    "MED2019": "Medicine 2019（PMC6571398）の本文：HSV と CMV の潰瘍形態、治療薬",
    "BOERHAAVE": "Boerhaave Syndrome—Narrative Review, Diagnostics 2025（PMC12524210、CC BY）の本文：水溶性造影剤で22〜50%の穿孔を見逃す",
})
FIXES2 = {
    "ES-003": {"set": {"assertion.differential": "軽症RE（LA分類A・B）の初期治療はPPIまたはボノプラザン（ES-004）"},
               "why": "根拠のない欧米との比較（要確認）を、同じGLで確認できる軽症REとの対比に差し替え", "ev": ["GERD_GL"]},
    "ES-017": {"set": {"assertion.differential": "NBIによる狙撃生検（ACG 2022はSeattle protocolの継続を推奨）"},
               "why": "「日本では狙撃生検が中心（要確認）」は出典がないため、GL本文で確認できる対比に差し替え", "ev": ["ACG_BE"]},
    "ES-052": {"set": {"uncertainty": "low（抄録で照合）"}, "why": "一次資料（抄録）で主張文を照合したため uncertainty を更新", "ev": ["PM35108470"]},
    "ES-058": {"set": {"uncertainty": "low（Baveno VII本文で照合。AASLD 2024は本文未照合）", "provenance.corroboration": "Baveno VII 5.14・5.15"},
               "why": "Baveno VII 本文で推奨を確認。日本の扱いはこのカードの対象外のため「要確認」を削除", "ev": ["BAVENO"]},
    "ES-062": {"set": {"assertion.differential": "非静脈瘤性の上部消化管出血の初期対応（UG領域）"},
               "why": "「日本の保険適用は要確認」はこのカードの対象外のため、鑑別の記載に差し替え", "ev": ["BAVENO"]},
    "ES-073": {"set": {"uncertainty": "medium（DOI・PMIDはAPIで確定。PMCでは抄録しか読めず、本文の記述は未照合）"},
               "why": "識別子の確定を反映し、未照合の範囲を明記", "ev": []},
    "ES-075": {"set": {"uncertainty": "medium（報告によって2bは40〜60%とする記載もあり幅がある。PMCでは抄録しか読めず本文は未照合）"},
               "why": "識別子の確定を反映し、未照合の範囲を明記", "ev": []},
}
CONTENT_VERIFIED2 = {"ES-001": "GERD_GL", "ES-037": "JES_GL", "ES-074": "CHENG", "ES-080": "MED2019",
                     "ES-081": "MED2019", "ES-086": "BOERHAAVE", "ES-003": "GERD_GL", "ES-017": "ACG_BE",
                     "ES-052": "PM35108470", "ES-058": "BAVENO", "ES-062": "BAVENO"}

# ---------------------------------------------------------------- 欠番の起票
NEW_CARDS = [
    {"id": "ES-076", "subdomain": "その他の食道疾患",
     "assertion": {
         "plain_statement_ja": "食道裂孔ヘルニアで最も多いのはI型（滑脱型）で、横隔食道膜の弛緩により胃噴門部が縦隔へ脱出する。軸方向のずれが2 cmを超えれば、バリウム造影、内視鏡、内圧検査で診断できる。",
         "condition": "成人の食道裂孔ヘルニア",
         "differential": "傍食道型（II型）・混合型（III型）・他臓器を含むIV型（本出典の抄録には記載なし）",
         "common_misconception": "小さな滑脱型ヘルニアも内視鏡や造影で常に確実に診断できると考える"},
     "provenance": {"source": "Kahrilas PJ, et al. Approaches to the diagnosis and grading of hiatal hernia. Best Pract Res Clin Gastroenterol 2008;22:601-616",
                    "doi": "10.1016/j.bpg.2007.12.007", "pmid": "18656819", "pmcid": "PMC2548324",
                    "source_license": "Elsevier（PMC 著者稿）", "legal_basis": "B", "source_class": "RESTRICTED"},
     "uncertainty": "low（抄録で照合）。II〜IV型の定義は未収載",
     "ev": "Kahrilas 2008（PMID 18656819）の抄録"},
    {"id": "ES-077", "subdomain": "その他の食道疾患",
     "assertion": {
         "plain_statement_ja": "薬剤性食道炎の原因薬には、抗菌薬（テトラサイクリン系、特にドキシサイクリン）、ビスホスホネート、NSAIDs、塩化カリウム、鉄剤などがある。症状は胸骨後部痛、胸やけ、嚥下痛、嚥下障害で、多くは原因薬の中止と支持療法で改善する。",
         "condition": "内服薬による直接的な食道粘膜傷害",
         "differential": "逆流性食道炎、感染性食道炎",
         "common_misconception": "少量の水で服用してすぐ横になっても問題ないと考える"},
     "provenance": {"source": "Abdi S, et al. Drug-induced esophagitis and helpful management for healthcare providers. Gastroenterol Hepatol Bed Bench 2022;15:219-224",
                    "doi": "10.22037/ghfbb.v15i3.2591", "pmid": "36311965", "pmcid": "PMC9589134",
                    "source_license": None, "legal_basis": "B", "source_class": "UNKNOWN"},
     "uncertainty": "low（PMC本文で照合）。ライセンスは Phase 3 の照合で確定",
     "ev": "Abdi 2022（PMC9589134）の本文"},
    {"id": "ES-078", "subdomain": "その他の食道疾患",
     "assertion": {
         "plain_statement_ja": "台湾の健診受診者（HIV陰性）11,802例では、生検で確認したカンジダ食道炎は0.4%だった。多変量解析での独立した危険因子は、高齢、慢性腎臓病、飲酒、ステロイド使用だった。",
         "condition": "HIV陰性の成人（健診の上部消化管内視鏡）",
         "differential": "HIV感染者などの免疫不全者では頻度が高い。EoEの白斑との鑑別",
         "common_misconception": "カンジダ食道炎は免疫不全者にしか起こらないと考える"},
     "provenance": {"source": "Chen YH, et al. Prevalence and risk factors for Candida esophagitis among human immunodeficiency virus-negative individuals. World J Clin Cases 2022;10:10896-10905",
                    "doi": "10.12998/wjcc.v10.i30.10896", "pmid": "36338217", "pmcid": "PMC9631128",
                    "source_license": None, "legal_basis": "B", "source_class": "UNKNOWN"},
     "uncertainty": "low（抄録で照合）。単施設の健診データ",
     "ev": "Chen 2022（PMID 36338217）の抄録"},
    {"id": "ES-082", "subdomain": "その他の食道疾患",
     "assertion": {
         "plain_statement_ja": "Plummer-Vinson症候群は、嚥下障害、鉄欠乏性貧血、食道web（膜様狭窄）の三徴を示すまれな疾患で、中年の女性に多い。治療は鉄補充と、必要に応じたwebの拡張である。咽頭・食道の扁平上皮癌のリスクが高いため経過観察が必要である。",
         "condition": "鉄欠乏を伴う頸部食道のweb",
         "differential": "食道癌、好酸球性食道炎による狭窄",
         "common_misconception": "鉄欠乏を補正すれば発癌リスクの経過観察は不要と考える"},
     "provenance": {"source": "Novacek G. Plummer-Vinson syndrome. Orphanet J Rare Dis 2006;1:36",
                    "doi": "10.1186/1750-1172-1-36", "pmid": "16978405", "pmcid": "PMC1586011",
                    "source_license": None, "legal_basis": "B", "source_class": "UNKNOWN"},
     "uncertainty": "low（抄録で照合）",
     "ev": "Novacek 2006（PMID 16978405）の抄録"},
    {"id": "ES-083", "subdomain": "その他の食道疾患",
     "assertion": {
         "plain_statement_ja": "Zenker憩室は、下咽頭収縮筋の斜走部と輪状咽頭筋の間の脆弱部（Killian三角）から粘膜・粘膜下層が後方へ突出する圧出性憩室で、下咽頭憩室で最も多い。70〜80歳代の男性に多く、嚥下障害が80〜90%にみられる。治療の要点は輪状咽頭筋の切開である。",
         "condition": "高齢者の嚥下障害・未消化物の逆流",
         "differential": "食道中部の牽引性憩室、横隔膜上憩室",
         "common_misconception": "憩室を切除するだけで輪状咽頭筋を処理しなくてよいと考える"},
     "provenance": {"source": "Dell'Anna G, et al. The endoscopic management of Zenker's diverticulum: a comprehensive review. Diagnostics (Basel) 2024;14:2155",
                    "doi": "10.3390/diagnostics14192155", "pmid": "39410559", "pmcid": "PMC11475965",
                    "source_license": "CC BY 4.0（論文表示）", "legal_basis": "B", "source_class": "OPEN"},
     "uncertainty": "low（PMC本文で照合）",
     "ev": "Dell'Anna 2024（PMC11475965、CC BY）の本文"},
    {"id": "ES-084", "subdomain": "その他の食道疾患",
     "assertion": {
         "plain_statement_ja": "Mallory-Weiss症候群（嘔吐などによる食道胃接合部の粘膜裂創）は多くが自然に止血し、緊急の内視鏡治療を要しないことが多い。ドイツの全国入院データ（2010〜2019年、59,291例）では、内視鏡的止血は局注13.7%、クリップ12.8%、外科治療は0.1%で、院内死亡率は2.7%だった。",
         "condition": "嘔吐・えずきの後の吐血",
         "differential": "Boerhaave症候群（全層性破裂、ES-085〜087）、静脈瘤出血",
         "common_misconception": "Mallory-Weiss症候群は全例で内視鏡的止血が必要と考える"},
     "provenance": {"source": "Mertens A, et al. A systematic analysis of incidence, therapeutic strategies, and in-hospital mortality of Mallory-Weiss syndrome in Germany. J Clin Gastroenterol 2024;58:640-649",
                    "doi": "10.1097/MCG.0000000000001918", "pmid": "37668412", "pmcid": None,
                    "source_license": None, "legal_basis": "B", "source_class": "UNKNOWN"},
     "uncertainty": "low（抄録で照合）",
     "ev": "Mertens 2024（PMID 37668412）の抄録"},
    {"id": "ES-088", "subdomain": "好酸球性食道炎（EoE）",
     "assertion": {
         "plain_statement_ja": "EREFSは、EoEの4つの主要な内視鏡所見（浮腫、輪状溝、白斑、縦走溝）と追加所見（狭窄、crepe paper esophagus）を等級化する分類である。修正版では、主要4所見の観察者間一致はκ 0.40〜0.54と良好だった。",
         "condition": "EoEの内視鏡評価・治療効果判定",
         "differential": "カンジダ食道炎の白苔（白斑との鑑別）",
         "common_misconception": "内視鏡所見が乏しければEoEは否定できると考える"},
     "provenance": dict(SRC["HIRANO"]),
     "uncertainty": "low（抄録で照合）",
     "ev": "Hirano 2013（PMID 22619364）の抄録"},
]

# ES-067（Mallory-Weiss と Boerhaave、出典未取得）は、ES-084 と ES-085 で置き換えて廃止する
RETIRE = {"ES-067": "ES-084, ES-085"}

# 内容を一次資料と照合できたカード（verified_sources に上げる候補）
CONTENT_VERIFIED = {
    "ES-002": "GERD_GL", "ES-003": "GERD_GL", "ES-004": "GERD_GL", "ES-006": "GERD_GL", "ES-007": "GERD_GL",
    "ES-008": "GERD_GL", "ES-009": "LYON2", "ES-010": "GERD_GL", "ES-011": "GERD_GL",
    "ES-013": "ACG_BE", "ES-014": "ACG_BE", "ES-015": "JES_GL", "ES-016": "ACG_BE", "ES-017": "ACG_BE",
    "ES-018": "AGREE", "ES-019": "AGREE", "ES-021": "HIRANO", "ES-023": "PM36546624",
    "ES-027": "CCV4", "ES-028": "CCV4", "ES-029": "CCV4", "ES-030": "CCV4", "ES-031": "CCV4",
    "ES-032": "PM31800987", "ES-033": "PM31800987", "ES-034": "ACG_ACH",
    "ES-038": "JES_GL", "ES-039": "JES_GL", "ES-040": "JES_GL", "ES-041": "JES_GL", "ES-047": "JES_GL",
    "ES-049": "PM38876133", "ES-051": "PM33789008", "ES-052": "PM35108470", "ES-053": "PM34454674",
    "ES-054": "PM41259897", "ES-055": "JES_GL", "ES-056": "JES_GL", "ES-057": "BAVENO", "ES-058": "BAVENO",
    "ES-062": "BAVENO", "ES-063": "PM23281973", "ES-064": "BAVENO", "ES-065": "PM20573925",
}
CONTENT_VERIFIED.update(CONTENT_VERIFIED2)
NEW_VERIFIED = {"ES-076", "ES-077", "ES-078", "ES-082", "ES-083", "ES-084", "ES-088"}

IMPORT_NOTE_RE = re.compile(r"｜?［取り込み時］[^｜]*")


def h(change: str) -> dict:
    return {"date": TODAY, "by": BY, "change": change}


def set_path(card: dict, path: str, value) -> object:
    obj = card
    keys = path.split(".")
    for k in keys[:-1]:
        obj = obj.setdefault(k, {})
    old = obj.get(keys[-1])
    obj[keys[-1]] = value
    return old


def has_pending(card: dict) -> bool:
    texts = [str(card.get("uncertainty") or ""), card["provenance"].get("source") or ""]
    texts += [str(v) for v in card["assertion"].values()]
    return any("要確認" in t or "未取得" in t for t in texts)


def main(stage: str) -> None:
    """stage=apply：修正・起票・廃止。stage=promote：verify_ids.py の再実行後に昇格とレポート。"""
    cards = yaml.safe_load(ES.read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in cards}
    log = []
    if stage == "promote":
        return promote(cards)
    if stage == "apply2":
        log = json.loads((ROOT / ".cache" / "es_content_log.json").read_text(encoding="utf-8"))
        for cid, fx in FIXES2.items():
            c = by_id[cid]
            changes = [p for p, v in fx["set"].items() if set_path(c, p, v) != v]
            if not changes:
                continue
            ev = "；".join(EVIDENCE[k] for k in fx["ev"]) or "PubMed・Crossref の書誌"
            c["history"].append(h(f"内容照合による修正（{DELEGATION}）：{fx['why']}。変更項目：{', '.join(changes)}。根拠：{ev}"))
            log.append((cid, "修正", fx["why"], ev))
        ES.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
        (ROOT / ".cache" / "es_content_log.json").write_text(json.dumps(log, ensure_ascii=False), encoding="utf-8")
        print(f"applied round 2: {len(FIXES2)}")
        return

    for cid, fx in FIXES.items():
        c = by_id[cid]
        changes = []
        for path, val in fx["set"].items():
            old = set_path(c, path, val)
            if old != val:
                changes.append(path)
        ev = "；".join(EVIDENCE[k] for k in fx["ev"]) or "PubMed・Crossref の書誌"
        c["history"].append(h(f"内容照合による修正（{DELEGATION}）：{fx['why']}。変更項目：{', '.join(changes)}。根拠：{ev}"))
        log.append((cid, "修正", fx["why"], ev))

    for nc in NEW_CARDS:
        if nc["id"] in by_id:
            raise SystemExit(f"{nc['id']} は既に存在します")
        prov = {"source_ref": None, "url": None, "pmcid": None, **{k: v for k, v in nc["provenance"].items()}}
        card = {
            "id": nc["id"], "domain": "ES", "subdomain": nc["subdomain"], "assertion": nc["assertion"],
            "provenance": prov, "uncertainty": nc["uncertainty"],
            "curriculum": {"core_curriculum": None, "kokushi": None},
            "publication_info": {"created": TODAY, "verifier": None, "verified_at": None, "status": "draft", "superseded_by": None},
            "history": [h(f"起票：欠番補完（{DELEGATION}）。出典を再調査し、自作文で作成。根拠：{nc['ev']}")],
        }
        cards.append(card)
        by_id[card["id"]] = card
        log.append((nc["id"], "新規", "欠番の起票", nc["ev"]))

    for cid, succ in RETIRE.items():
        c = by_id[cid]
        c["publication_info"]["status"] = "retired"
        c["publication_info"]["superseded_by"] = succ
        c["history"].append(h(f"廃止：{succ} に統合（出典未取得のカードを、出典のある新カードで置き換え。{DELEGATION}）"))
        log.append((cid, "廃止", f"superseded_by={succ}", ""))

    # 識別子が埋まった後に残っている取り込み時の注記を整理
    for c in cards:
        u = c.get("uncertainty")
        if isinstance(u, str) and "［取り込み時］" in u:
            p = c["provenance"]
            if p.get("pmid") or p.get("doi"):
                new = IMPORT_NOTE_RE.sub("", u).strip("｜ ") or None
                if new != u:
                    c["uncertainty"] = new
                    c["history"].append(h("uncertainty から取り込み時の識別子の注記を削除（Phase 3 で API により識別子を確定したため）"))

    cards.sort(key=lambda c: c["id"])
    ES.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
    (ROOT / ".cache" / "es_content_log.json").write_text(json.dumps(log, ensure_ascii=False), encoding="utf-8")
    print(f"applied: fixes={len(FIXES)} new={len(NEW_CARDS)} retired={len(RETIRE)}")


def promote(cards) -> None:
    log = json.loads((ROOT / ".cache" / "es_content_log.json").read_text(encoding="utf-8"))
    promoted, kept = [], []
    for c in cards:
        if c["publication_info"]["status"] != "draft":
            continue
        cid = c["id"]
        if cid not in CONTENT_VERIFIED and cid not in NEW_VERIFIED:
            continue
        idc = c["provenance"].get("id_check") or {}
        ids_ok = bool(idc.get("doi_resolved")) and idc.get("pmid_matched") is not False
        if not ids_ok or has_pending(c):
            kept.append((cid, "識別子の照合が未了" if not ids_ok else "「要確認」「未取得」が残る"))
            continue
        c["publication_info"]["status"] = "verified_sources"
        ev = EVIDENCE.get(CONTENT_VERIFIED.get(cid, ""), "起票時に照合した一次資料")
        c["history"].append(h(f"status draft → verified_sources（識別子・ライセンスを API で照合済み、主張文の数値・推奨を一次資料と照合：{ev}。{DELEGATION}）"))
        promoted.append(cid)

    cards.sort(key=lambda c: c["id"])
    validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    errors = [(c["id"], "/".join(map(str, e.path)), e.message) for c in cards for e in validator.iter_errors(c)]
    ES.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
    all_promoted = [c["id"] for c in cards if c["publication_info"]["status"] == "verified_sources"]
    write_report(cards, log, all_promoted, kept, errors)
    print(f"promoted={len(promoted)} kept={len(kept)} schema_errors={len(errors)}")


def write_report(cards, log, promoted, kept, errors) -> None:
    status = {}
    for c in cards:
        status[c["publication_info"]["status"]] = status.get(c["publication_info"]["status"], 0) + 1
    L = [f"# Phase 3-2：食道カードの内容照合（{TODAY}）\n",
         f"生成：`scripts/es_content_fixes.py`。{DELEGATION}した範囲で、一次資料と照合できた修正を反映した。\n",
         "## 1. 結果\n",
         "| 項目 | 件数 |", "|---|---|",
         f"| 主張文・出典の修正 | {sum(1 for x in log if x[1] == '修正')} |",
         f"| 欠番の起票 | {sum(1 for x in log if x[1] == '新規')} |",
         f"| 廃止 | {sum(1 for x in log if x[1] == '廃止')} |",
         f"| verified_sources に昇格 | {len(promoted)} |",
         f"| スキーマ違反 | {len(errors)} |\n",
         "ステータス別：" + "、".join(f"{k} {v}" for k, v in sorted(status.items())) + "\n",
         "## 2. 修正・起票・廃止の一覧\n", "| ID | 種別 | 内容 | 根拠 |", "|---|---|---|---|"]
    L += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in log]
    L += ["\n## 3. verified_sources に昇格したカード\n", ", ".join(promoted) or "なし"]
    L += ["\n## 4. 照合済みでも draft に残したカード\n", "| ID | 理由 |", "|---|---|"]
    L += [f"| {a} | {b} |" for a, b in kept] or ["| — | なし |"]
    drafts = [c for c in cards if c["publication_info"]["status"] == "draft"]
    L += ["\n## 5. draft のまま残っているカード（今後の課題）\n", "| ID | 主張文（冒頭） | uncertainty |", "|---|---|---|"]
    for c in drafts:
        L.append(f"| {c['id']} | {c['assertion']['plain_statement_ja'][:40]}… | {str(c.get('uncertainty') or '').replace('|', '／')[:80]} |")
    if errors:
        L += ["\n## スキーマ違反\n"] + [f"- {a} {b}: {c}" for a, b, c in errors]
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "apply")
