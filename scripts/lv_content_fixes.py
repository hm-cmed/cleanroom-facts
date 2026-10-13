"""Phase 3-2（LV）：肝カードの内容照合の結果を反映し、昇格する（2026-10-13）。

人間が 2026-10-13 にチャットで、第1〜3回と同じ委任を第4回にも与えた。照合の方法は GD・IN と同じ。
PubMed にない出典（JSH 肝癌診療GL 2021 英語版 PDF、JSH B型肝炎治療GL 第4版簡易版、厚労省 指定難病の PDF、
CDC、MedlinePlus、国立がん研究センター、厚労省 E型肝炎Q&A・エキノコックス事務連絡・アメーバ赤痢届出基準）は、
各ページ・PDF の本文をメモリ上で読んで照合した（保存していない）。MASLD の診断基準（LV-036）は、
論文中の図（Hepatology 版 PMC10653297 の Figure 6）をブラウザで表示して確認した。

使い方：
    .\\.venv\\Scripts\\python.exe scripts\\lv_content_fixes.py apply
    .\\.venv\\Scripts\\python.exe scripts\\verify_ids.py LV
    .\\.venv\\Scripts\\python.exe scripts\\lv_content_fixes.py promote
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gd_content_fixes import TODAY, h, has_numbers, set_path  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LV = ROOT / "data" / "facts" / "LV.yaml"
REPORT = ROOT / "reports" / "03_lv_content.md"
SCHEMA = ROOT / "schema" / "fact.schema.json"
LOG = ROOT / ".cache" / "lv_content_log.json"
DELEGATION = "人間が2026-10-13にチャットで委任"

EVIDENCE = {
    "NAFLD_GL": "JSGE NAFLD/NASH GL 2020 本文（PMC8531062）：Fig. 1（一般医による一次スクリーニング、Castera らに準拠）は FIB-4 <1.3／1.3–3.25／>3.25、Fig. 2（消化器専門医による二次スクリーニング）は <1.3／1.3–2.66／≥2.67",
    "HUMAN_FIB4": "人間（消化器内科医）のチャットでの指摘（2026-10-13）：NAFLD/MASLD の高リスクは >2.67、低リスクは <1.30（年齢調整 <2.00）、HCV では 1.45／3.25",
    "MASLD_FIG6": "Rinella ME, Hepatology 2023;78:1966-1986（PMC10653297）Figure 6 の成人の心代謝系基準（J Hepatol 版と同一内容）",
    "JSH_HCC": "JSH 肝癌診療GL 2021 英語版 PDF（第1〜3分冊）本文",
    "MOCHIDA2011": "Mochida S, Hepatol Res 2011;41:805-812（PMID 21884340）の抄録：昏睡型は発症から昏睡Ⅱ度以上まで10日以内が急性型、11〜56日が亜急性型",
    "IPH_PDF": "厚労省 指定難病92 特発性門脈圧亢進症 概要 PDF",
}

FIXES = {
    "LV-026": ({
        "assertion.plain_statement_ja": "日本のNAFLD/NASH診療ガイドライン2020は、FIB-4 indexによる線維化評価の流れ図を2つ示している。一般医による一次スクリーニングでは1.3未満を低リスク、1.3〜3.25を中間リスク、3.25を超えるものを高リスクとし、消化器専門医による二次スクリーニングでは1.3未満を低リスク、1.3〜2.66を中等度線維化の疑い、2.67以上を高度線維化の疑いとする。",
        "uncertainty": "low（GL本文で照合）。NAFLD/MASLD では高度線維化の目安として 2.67 が広く用いられ、1.45・3.25 は C 型肝炎で用いられる閾値である。65歳以上で低リスクの閾値を 2.0 とする年齢調整は、このGL本文では確認していない"},
        "調査レポート第7節4の依頼。GL本文に2つの流れ図があり閾値が異なることを確認し、一方だけを記していた主張文を両方を示す文に差し替えた。人間の指摘（NAFLD の高リスクは 2.67）とも一致",
        ["NAFLD_GL", "HUMAN_FIB4"]),
    "LV-036": ({"uncertainty": "low（論文の図で照合）"},
               "心代謝系基準の数値を論文の図で確認し、uncertainty を更新", ["MASLD_FIG6"]),
    "LV-042": ({"uncertainty": "GL の序文は非B非C型が約50%に達しつつあるとし、別の章は2015年以降の新規発症で30〜40%としており、GL内で記載に幅がある"},
               "GL本文の別の箇所との記載の幅を明記", ["JSH_HCC"]),
    "LV-038": ({"provenance.corroboration": "雑誌掲載版（要約）：Hasegawa K, et al. Hepatol Res 2023;53:383-390（PMID 36826411、DOI 10.1111/hepr.13892）"},
               "JSH 肝癌診療GL 2021 の雑誌掲載版を PubMed で特定し、関連文献として記録（調査レポート第7節2）。カードの出典は全文の PDF のまま", ["JSH_HCC"]),
    "LV-068": ({"uncertainty": "low（2011年基準の原典の抄録で照合）",
                "provenance.corroboration": "Mochida S, Hepatol Res 2011;41:805-812（PMID 21884340）"},
               "診断基準の原典を PubMed で特定し、抄録で定義（PT 40%以下または INR 1.5以上、8週以内、アルコール性などの acute-on-chronic は除外）を確認", ["MOCHIDA2011"]),
    "LV-069": ({
        "assertion.plain_statement_ja": "日本の急性肝不全は、肝性脳症のない非昏睡型と昏睡型に分けられ、昏睡型は症状出現から昏睡Ⅱ度以上の脳症までが10日以内の急性型と、11〜56日の亜急性型に分けられる。症状出現から8〜24週で、PT 40%以下またはINR 1.5以上かつ昏睡Ⅱ度以上の脳症を生じるものは遅発性肝不全（LOHF）とする。",
        "provenance.corroboration": "急性型・亜急性型の日数は Mochida S, Hepatol Res 2011;41:805-812（PMID 21884340）",
        "uncertainty": "low（日数は2011年基準の原典の抄録で照合）"},
        "調査レポート第7節5の依頼。2011年基準の原典の抄録で、急性型と亜急性型を分ける日数（10日以内／11〜56日）を確認し、主張文に加えた", ["MOCHIDA2011"]),
    "LV-091": ({"uncertainty": "出典PDFは「男女比は約7:3」と「中年女性に多発」の両方を記しており、比の向きが本文内で整合しないため、比は主張文に入れていない"},
               "調査レポート第7節10の依頼。原文を確認したが、比の向きは本文内で整合しなかったため主張文は変えず、その旨を明記", ["IPH_PDF"]),
}

HOLD: dict[str, str] = {}


def apply() -> None:
    cards = yaml.safe_load(LV.read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in cards}
    log = []
    for cid, (fields, why, evk) in FIXES.items():
        c = by_id[cid]
        changes = [p for p, v in fields.items() if set_path(c, p, v) != v]
        if changes:
            ev = "；".join(EVIDENCE[k] for k in evk)
            c["history"].append(h(f"内容照合による修正（{DELEGATION}）：{why}。変更項目：{', '.join(changes)}。根拠：{ev}"))
            log.append((cid, why, ev))
    LV.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
    LOG.write_text(json.dumps(log, ensure_ascii=False), encoding="utf-8")
    print(f"applied {len(log)}")


def promote() -> None:
    cards = yaml.safe_load(LV.read_text(encoding="utf-8"))
    log = json.loads(LOG.read_text(encoding="utf-8"))
    promoted, kept = [], []
    for c in cards:
        if c["publication_info"]["status"] != "draft":
            continue
        cid, p = c["id"], c["provenance"]
        idc = p.get("id_check") or {}
        blob = " ".join([str(c.get("uncertainty") or ""), p.get("source") or ""] + [str(v) for v in c["assertion"].values()])
        has_id = bool(p.get("doi") or p.get("pmid") or p.get("pmcid"))
        if cid in HOLD:
            kept.append((cid, HOLD[cid])); continue
        if "要確認" in blob:
            kept.append((cid, "「要確認」が残る")); continue
        if has_id and not (idc.get("doi_resolved") or idc.get("pmid_matched")):
            kept.append((cid, "識別子の照合が未了")); continue
        if has_id and idc.get("pmid_matched") is False:
            kept.append((cid, "PMID が一致しない")); continue
        basis = ("主張文の数値を出典本文で文脈とともに照合" if has_numbers(c["assertion"]["plain_statement_ja"])
                 else "数値を含まない命題。識別子・ライセンスの照合と、出典の該当箇所の確認に基づく")
        if not has_id:
            basis += "（識別子のない公的資料・学会資料は、ページ・PDF本文で確認）"
        c["publication_info"]["status"] = "verified_sources"
        c["history"].append(h(f"status draft → verified_sources（{basis}。{DELEGATION}）"))
        promoted.append(cid)
    validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    errors = [(c["id"], "/".join(map(str, e.path)), e.message) for c in cards for e in validator.iter_errors(c)]
    LV.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
    status = {}
    for c in cards:
        status[c["publication_info"]["status"]] = status.get(c["publication_info"]["status"], 0) + 1
    L = [f"# Phase 3-2：肝カードの内容照合（{TODAY}）\n",
         f"生成：`scripts/lv_content_fixes.py`。{DELEGATION}した範囲で反映した。照合の方法は GD と同じ（`reports/03_gd_content.md` 第1節）。\n",
         "## 1. 結果\n",
         f"- 修正・注記：{len(log)}件　昇格：{len(promoted)}件　draft のまま：{len(kept)}件　スキーマ違反：{len(errors)}件",
         "- ステータス別：" + "、".join(f"{k} {v}" for k, v in sorted(status.items())),
         "- 主張文を変えたのは LV-026（FIB-4 の閾値）と LV-069（急性型・亜急性型の日数の追加）の2件。そのほかの数値は全件、出典本文と一致した。\n",
         "## 2. 調査レポート第7節の依頼への回答\n",
         "| 依頼 | 結果 |", "|---|---|",
         "| 1. CC 種別 | NAFLD GL・肝硬変GL 2020（SRC-018）・急性肝不全の総説（SRC-074）は CC BY 4.0（OPEN）。MASLD 命名法は CC BY-NC-ND（RESTRICTED） |",
         "| 2. 識別子 | DOI 44件を解決し、PMID・PMCID を47件補完。JSH 肝癌GL 2021 の雑誌掲載版（要約）は Hepatol Res 2023;53:383-390（PMID 36826411）。カードの出典は全文の PDF のままとし、LV-038 に関連文献として記録 |",
         "| 3. 孫引き数値 | 対象の14件はいずれも、カードが出典とする GL・総説・公的資料の本文に同じ値で記載されていた |",
         "| 4. LV-026（FIB-4） | GL に2つの流れ図（一次：3.25、二次：2.67）があることを本文で確認。人間の指摘（NAFLD の高リスクは 2.67、3.25 は HCV の閾値）を踏まえ、両方を示す主張文に差し替えた |",
         "| 5. LV-068・069（急性肝不全） | 2011年基準の原典（Mochida 2011、PMID 21884340）の抄録で定義と日数（10日以内／11〜56日）を確認し、LV-069 に日数を追加 |",
         "| 6. LV-047（肝癌の薬物療法） | GL 2021 の記載どおりであることを確認。改訂版の確認は次回 |",
         "| 7. 国内の承認・保険 | 未照合（人間） |",
         "| 8. 出典が古いもの | 差し替えは次回の補完で検討 |",
         "| 9. 指定難病の PDF | 受給者証保持者数（令和元年度）を含め本文と一致。告示改正の版の確認は人間 |",
         "| 10. LV-091 の男女比 | 出典 PDF の中で「約7:3」と「中年女性に多発」が整合しないため、主張文は変えずに uncertainty に明記 |",
         "| 11. LV-075・077（PBC） | 移行率（10〜40%、5年で約25%）とベザフィブラート併用の記載は厚労省 PDF で確認。保険適用は未照合（人間） |",
         "\n## 3. 修正・注記の一覧\n", "| ID | 内容 | 根拠 |", "|---|---|---|"]
    L += [f"| {a} | {b} | {c} |" for a, b, c in log]
    L += ["\n## 4. verified_sources に昇格したカード\n", ", ".join(promoted)]
    L += ["\n## 5. draft に残したカード\n", "| ID | 理由 |", "|---|---|"] + ([f"| {a} | {b} |" for a, b in kept] or ["| — | なし |"])
    if errors:
        L += ["\n## スキーマ違反\n"] + [f"- {a} {b}: {m}" for a, b, m in errors]
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"promoted={len(promoted)} kept={kept} errors={len(errors)}")


if __name__ == "__main__":
    {"apply": apply, "promote": promote}[sys.argv[1]]()
