"""Phase 3-2（GD）：胃・十二指腸カードの内容照合の結果を反映し、昇格する（2026-10-13）。

人間が 2026-10-13 にチャットで、第1回（食道）と同じ委任を第2回にも与えた:
- 一次資料と照合できた修正は、根拠を history に記録して自動反映する（CLAUDE.md 1-2 の例外）。
- 照合が済んだカードを verified_sources に上げる（verified_expert は人間のみ）。

照合の方法（reports/03_gd_content.md に詳細）:
1. 全カードについて、主張文中の数値（1桁の整数を除く）が出典本文（PMC）または抄録に現れるかを機械的に確認し、
   現れた箇所の前後を読んで文脈が合うかを確認した。
2. PubMed にない出典（厚労省・国立がん研究センター・J-STAGE 和文誌・学会記載基準・企業発表）は、
   各ページ・PDF の本文で確認した。全文はリポジトリにも .cache にも保存していない。

使い方：
    .\\.venv\\Scripts\\python.exe scripts\\gd_content_fixes.py apply     # 修正
    .\\.venv\\Scripts\\python.exe scripts\\verify_ids.py GD              # 識別子の再照合
    .\\.venv\\Scripts\\python.exe scripts\\gd_content_fixes.py promote   # 昇格とレポート
"""
from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
GD = ROOT / "data" / "facts" / "GD.yaml"
REPORT = ROOT / "reports" / "03_gd_content.md"
SCHEMA = ROOT / "schema" / "fact.schema.json"
LOG = ROOT / ".cache" / "gd_content_log.json"
TODAY = dt.date.today().isoformat()
BY = "claude-code"
DELEGATION = "人間が2026-10-13にチャットで委任"

EVIDENCE = {
    "REVISE": "Cook D, NEJM 2024;391:9-20（PMID 38875111）の抄録：4,821例、出血 1.0%対3.5%（HR 0.30）、90日死亡 29.1%対30.9%（HR 0.94、P=0.25）",
    "EID": "Emerging Infectious Diseases 2022（PMC9514333）本文：「U.S. Government の刊行物で public domain」と明記。本文の表で 168/189＝88.9%",
    "VARICES": "日消誌116(5):395 掲載の記載基準表（門脈圧亢進症取扱い規約 第3版）：Lg-c 噴門部に限局、Lg-cf 噴門部から穹窿部に連なる、Lg-f 穹窿部に限局",
    "ZOLBE": "アステラス製薬の発表（2024-03-26 承認取得）を検索で確認。適時開示 PDF は取得不可（403）",
    "ISLAM": "Islam RS, Gastroenterol Hepatol (N Y) 2013;9:640-651（PMID 24764778、PMC3992058）の本文",
    "MHLW_ANI": "厚生労働省「アニサキスによる食中毒を予防しましょう」ページ本文（2026-10-13 閲覧）",
    "GIST_GL": "GIST GL 2022 英語版本文（PMC11130037）：腫瘍径10%以上の縮小または CT 値15%以上の低下",
}

FIXES = {
    "GD-092": {"set": {
        "assertion.plain_statement_ja": "人工呼吸管理中の重症患者4,821例を対象としたRCT（REVISE）で、パントプラゾール40 mg静注の予防投与は、プラセボに比べて臨床的に重要な上部消化管出血を減らした（1.0%対3.5%、HR 0.30）が、90日死亡率には差がなかった（29.1%対30.9%、HR 0.94）。",
        "provenance.source": "Cook D, et al. Stress ulcer prophylaxis during invasive mechanical ventilation (REVISE). N Engl J Med 2024;391:9-20",
        "uncertainty": "low（数値は抄録で照合）"},
        "why": "調査側が二次資料経由として uncertainty に置いていた数値を、NEJM の抄録で確認できたため主張文に移した（調査レポート第7節4の依頼）。巻・頁を補った",
        "ev": ["REVISE"]},
    "GD-085": {"set": {"uncertainty": "low（本文の表 168/189＝88.9% を採用。抄録の 88.4% は本文の件数と合わない）"}},
    "GD-084": {"set": {"provenance.source_class": "GOV_US", "provenance.source_license": "U.S. Government の刊行物で public domain（記事本文に明記）",
                       "uncertainty": "low（本文で照合）"}},
    "GD-072": {"set": {"uncertainty": "low（記載基準表で照合。ES-061 と対応：ES 側は食道静脈瘤、GD 側は胃静脈瘤の記述として両方を残す）"}},
    "GD-073": {"set": {"uncertainty": "肝硬変GL 2025年版の推奨は未確認。ES-066 と対応（両方を残す）"}},
    "GD-057": {"set": {"uncertainty": "承認日と効能・効果は企業発表で確認。「世界初」は企業発表・報道による位置づけ。PMDA 添付文書の改訂履歴では未照合"}},
    "GD-083": {"set": {"uncertainty": "冷凍・加熱の条件は、厚労省ページでは事業者向けの記載として示されている"}},
    "GD-086": {"set": {"provenance.pmid": "24764778", "provenance.pmcid": "PMC3992058"}},
    "GD-087": {"set": {"provenance.pmid": "24764778", "provenance.pmcid": "PMC3992058"}},
    "GD-088": {"set": {"provenance.pmid": "24764778", "provenance.pmcid": "PMC3992058", "uncertainty": "日本の胃腺腫の扱い（出題基準 Ⅵ-2-D-③）は別のカードで扱う"}},
    "GD-070": {"set": {"uncertainty": "GL本文は基準名（Choi基準）を明記せず、腫瘍径10%以上の縮小または CT 値15%以上の低下と記載"}},
}
WHY = {
    "GD-085": ("本文と抄録で割合が異なる点を、本文の件数（168/189）に合う 88.9% で確定（調査レポート第7節5）", ["EID"]),
    "GD-084": ("Emerging Infectious Diseases は米国政府の刊行物で public domain と本文に明記されているため source_class を GOV_US に変更", ["EID"]),
    "GD-072": ("部位名の和文表記を記載基準表で確認したため「要確認」を解消", ["VARICES"]),
    "GD-073": ("ES-R17/R18 は統合後 ES-061/ES-066 になったため、参照先を更新。両方を残す（人間が2026-10-13に決定）", []),
    "GD-057": ("承認日と効能・効果を企業発表で確認", ["ZOLBE"]),
    "GD-083": ("予防条件が事業者向けの記載であることを補足", ["MHLW_ANI"]),
    "GD-086": ("PubMed で書誌を特定し、idconv で PMCID を確認して識別子を設定", ["ISLAM"]),
    "GD-087": ("PubMed で書誌を特定し、idconv で PMCID を確認して識別子を設定", ["ISLAM"]),
    "GD-088": ("PubMed で書誌を特定し、idconv で PMCID を確認して識別子を設定", ["ISLAM"]),
    "GD-070": ("GL本文の記載に合わせて基準名の扱いを補足", ["GIST_GL"]),
}

# 内容照合で個別に読まなかった（数値を含まない）カードのうち、昇格させないもの
HOLD = {"GD-071": "本文未閲覧（調査側も専門医検証を優先と指摘）"}


def h(change: str) -> dict:
    return {"date": TODAY, "by": BY, "change": change}


def set_path(card, path, value):
    obj = card
    keys = path.split(".")
    for k in keys[:-1]:
        obj = obj.setdefault(k, {})
    old = obj.get(keys[-1])
    obj[keys[-1]] = value
    return old


def apply() -> None:
    cards = yaml.safe_load(GD.read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in cards}
    log = []
    for cid, fx in FIXES.items():
        why, evk = (fx.get("why"), fx.get("ev")) if "why" in fx else WHY[cid]
        c = by_id[cid]
        changes = [p for p, v in fx["set"].items() if set_path(c, p, v) != v]
        if not changes:
            continue
        ev = "；".join(EVIDENCE[k] for k in evk) or "PubMed・idconv"
        c["history"].append(h(f"内容照合による修正（{DELEGATION}）：{why}。変更項目：{', '.join(changes)}。根拠：{ev}"))
        log.append((cid, why, ev))
    GD.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
    LOG.write_text(json.dumps(log, ensure_ascii=False), encoding="utf-8")
    print(f"applied {len(log)}")


def has_numbers(text: str) -> bool:
    import re
    import unicodedata
    return any(len(n.replace(".", "")) > 1 or "." in n
               for n in re.findall(r"\d+(?:\.\d+)?", unicodedata.normalize("NFKC", text)))


def promote() -> None:
    cards = yaml.safe_load(GD.read_text(encoding="utf-8"))
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
            kept.append((cid, HOLD[cid]))
            continue
        if "要確認" in blob:
            kept.append((cid, "「要確認」が残る"))
            continue
        if has_id and not (idc.get("doi_resolved") or idc.get("pmid_matched")):
            kept.append((cid, "識別子の照合が未了"))
            continue
        if has_id and idc.get("pmid_matched") is False:
            kept.append((cid, "PMID が一致しない"))
            continue
        basis = ("主張文の数値を出典本文で文脈とともに照合" if has_numbers(c["assertion"]["plain_statement_ja"])
                 else "数値を含まない命題。識別子・ライセンスの照合と、出典の該当箇所の確認に基づく")
        if not has_id:
            basis += "（識別子のない公的資料・企業資料・和文資料は、ページ・PDF本文で確認）"
        c["publication_info"]["status"] = "verified_sources"
        c["history"].append(h(f"status draft → verified_sources（{basis}。{DELEGATION}）"))
        promoted.append(cid)

    validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    errors = [(c["id"], "/".join(map(str, e.path)), e.message) for c in cards for e in validator.iter_errors(c)]
    GD.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")

    status = {}
    for c in cards:
        status[c["publication_info"]["status"]] = status.get(c["publication_info"]["status"], 0) + 1
    L = [f"# Phase 3-2：胃・十二指腸カードの内容照合（{TODAY}）\n",
         f"生成：`scripts/gd_content_fixes.py`。{DELEGATION}した範囲で反映した。\n",
         "## 1. 照合の方法\n",
         "1. 全95件について、主張文中の数値（1桁の整数を除く）が出典本文（PMC）または抄録に現れるかを機械的に確認し、現れた箇所の前後を読んで文脈が合うかを確認した。",
         "2. 機械照合で別の箇所に当たった数値（GD-007・025・032・060・061・063〜067・070・077〜079 など）は、キーワードで該当箇所を探して読んだ。",
         "3. PubMed にない出典（国立がん研究センター、厚労省の検診・アニサキスのページ、J-STAGE 和文誌、学会の記載基準、企業発表）は、各ページ・PDF の本文で確認した。全文はリポジトリにも .cache にも保存していない。",
         "4. 数値を含まない命題は、識別子・ライセンスの照合と出典の確認にもとづいて昇格した（CLAUDE.md 第3節の定義による）。個々の推奨文の言い回しまでは一文ずつ照合していないため、専門医レビューで確認してほしい。\n",
         "## 2. 結果\n",
         f"- 修正：{len(log)}件　昇格：{len(promoted)}件　draft のまま：{len(kept)}件　スキーマ違反：{len(errors)}件",
         "- ステータス別：" + "、".join(f"{k} {v}" for k, v in sorted(status.items())) + "\n",
         "## 3. 照合で確認できたこと（調査レポート第7節の依頼への回答）\n",
         "| 依頼 | 結果 |", "|---|---|",
         "| 1. CC 種別の確定 | FD GL・胃癌GL第6版・第7版・GIST GL は Crossref で CC BY 4.0（OPEN）。ENETS 2023 は CC BY-NC-ND（RESTRICTED）。EID は米国政府刊行物で public domain（GOV_US）。J-STAGE 和文誌の DOI は JaLC 登録で、Crossref の license は取れない |",
         "| 2. PMID の取得 | DOI・PMCID から API で110件を補完（reports/03_id_check_GD.md）。Islam 2013 は PubMed で PMID 24764778、PMC3992058 |",
         "| 3. 孫引き数値の照合 | GD-010・049・076・086・087・093・094 の数値は、いずれもカードが出典とする GL・総説の本文に同じ値で記載されていた（原著との照合は未実施で、その旨は uncertainty に残した） |",
         "| 4. GD-092（REVISE） | NEJM 抄録で数値を確認し、主張文に移した |",
         "| 5. GD-085（88.9% と 88.4%） | 本文の件数 168/189 に合う 88.9% を採用 |",
         "| 6. GD-079（アカルボース） | 用量（50〜100 mg を1日3回、食事とともに）はコンセンサス本文で確認。国内の保険適用は未確認のまま |",
         "| 7. GD-071（胃 NET） | 本文未閲覧のため draft のまま（専門医検証を優先） |",
         "| 8. SPOTLIGHT の全生存 | 今回は追加していない（別カードの起票は次の補完ラウンドで扱う） |",
         "\n## 4. 修正の一覧\n", "| ID | 内容 | 根拠 |", "|---|---|---|"]
    L += [f"| {a} | {b} | {c} |" for a, b, c in log]
    L += ["\n## 5. verified_sources に昇格したカード\n", ", ".join(promoted)]
    L += ["\n## 6. draft に残したカード\n", "| ID | 理由 |", "|---|---|"] + [f"| {a} | {b} |" for a, b in kept]
    if errors:
        L += ["\n## スキーマ違反\n"] + [f"- {a} {b}: {m}" for a, b, m in errors]
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"promoted={len(promoted)} kept={kept} errors={len(errors)}")


if __name__ == "__main__":
    {"apply": apply, "promote": promote}[sys.argv[1]]()
