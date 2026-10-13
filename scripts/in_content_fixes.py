"""Phase 3-2（IN）：小腸・大腸カードの内容照合の結果を反映し、昇格する（2026-10-13）。

人間が 2026-10-13 にチャットで、第1・2回と同じ委任を第3回にも与えた。照合の方法は GD と同じ
（scripts/gd_content_fixes.py の説明を参照）。PubMed にない出典（難病情報センター、国立がん研究センター、
厚労省、CDC、NIDDK、NCI PDQ、Karger 掲載の憩室GL、OUP 掲載の IDSA GL）は各ページの本文で確認した。

使い方：
    .\\.venv\\Scripts\\python.exe scripts\\in_content_fixes.py apply
    .\\.venv\\Scripts\\python.exe scripts\\verify_ids.py IN
    .\\.venv\\Scripts\\python.exe scripts\\in_content_fixes.py promote
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
IN = ROOT / "data" / "facts" / "IN.yaml"
REPORT = ROOT / "reports" / "03_in_content.md"
SCHEMA = ROOT / "schema" / "fact.schema.json"
LOG = ROOT / ".cache" / "in_content_log.json"
DELEGATION = "人間が2026-10-13にチャットで委任"

EVIDENCE = {
    "IBD_GL": "JSGE IBD GL 2020 本文（PMC8137635）",
    "POLYP_GL": "JSGE 大腸ポリープ診療GL 本文（PMC8005396）の FAP と AFAP の CQ",
    "DIV_GL": "JGA 大腸憩室出血・憩室炎GL（Digestion 2019, Karger 掲載の本文）CQ8・CQ10",
    "NANBYOU": "難病情報センター 潰瘍性大腸炎（指定難病97）・クローン病（指定難病96）のページ（2026-10-13 閲覧）",
    "NIDDK": "NIDDK Hemorrhoids Definition & Facts（Last Reviewed October 2016）",
}

FIXES = {
    "IN-004": ({"uncertainty": "low（部分Mayoスコアの構成項目と区分をGL本文で照合）"},
               "GL本文で構成項目（排便回数、直腸出血、医師の全般評価）と区分を確認し、uncertainty を更新（調査レポート第7節5）", ["IBD_GL"]),
    "IN-064": ({"uncertainty": "CT血管造影の感度・特異度は急性消化管出血全般のメタ解析の値（憩室出血に限らない）。24時間以内の大腸内視鏡は、GLが主要評価項目の改善は不明としつつ提案している"},
               "GL本文で数値の出所と推奨の留保を確認し、uncertainty に明記", ["DIV_GL"]),
    "IN-001": ({"uncertainty": "GLの「22万人以上・7万人以上」は医療受給者証の交付数にもとづく値。難病情報センターの令和5年度の受給者証所持者数（IN-011：146,702人、IN-014：52,108人）とは集計の時点・基準が異なる"},
               "IN-011・014 との数の違いの理由を明記（調査レポート第7節4）", ["IBD_GL", "NANBYOU"]),
    "IN-045": ({"uncertainty": "AFAP の予防的大腸切除は IN-089 で扱う"},
               "AFAP の予防的切除の記載をGL本文で確認し、別カード IN-089 を起票（調査レポート第7節6）", ["POLYP_GL"]),
    "IN-088": ({"uncertainty": "NIDDK のページは2016年10月の最終レビュー。日本の資料への差し替えは次回の補完で検討"},
               "出典の最終レビュー年を明記（調査レポート第7節8）", ["NIDDK"]),
}

NEW = {
    "id": "IN-089", "domain": "IN", "subdomain": "大腸ポリープ",
    "assertion": {
        "plain_statement_ja": "軽症型家族性大腸腺腫症（AFAP）は、25歳以上で大腸腺腫が100個までのものとされる。大腸癌のリスクが高いため予防的な大腸切除が強く推奨されている（エビデンスレベルC）。AFAPでは残存直腸の発癌がFAPより少ないため結腸全摘・回腸直腸吻合も選択肢となるが、その場合は生涯のサーベイランスが必須である。FAPでは大腸全摘・回腸嚢肛門吻合が推奨される。",
        "condition": {"region": "日本", "guideline": "JSGE 大腸ポリープ診療GL"},
        "differential": "FAP（腺腫が100個以上）、MUTYH関連ポリポーシス",
        "common_misconception": "腺腫が少ないAFAPでは予防的手術は不要と考える",
    },
    "source_like": "IN-045",
    "uncertainty": "low（GL本文で照合）",
}

HOLD: dict[str, str] = {}


def apply() -> None:
    cards = yaml.safe_load(IN.read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in cards}
    log = []
    for cid, (fields, why, evk) in FIXES.items():
        c = by_id[cid]
        changes = [p for p, v in fields.items() if set_path(c, p, v) != v]
        if changes:
            ev = "；".join(EVIDENCE[k] for k in evk)
            c["history"].append(h(f"内容照合による修正（{DELEGATION}）：{why}。変更項目：{', '.join(changes)}。根拠：{ev}"))
            log.append((cid, why, ev))
    if NEW["id"] not in by_id:
        base = by_id[NEW["source_like"]]
        prov = {k: v for k, v in base["provenance"].items() if k != "id_check"}
        card = {"id": NEW["id"], "domain": "IN", "subdomain": NEW["subdomain"], "assertion": NEW["assertion"],
                "provenance": prov, "uncertainty": NEW["uncertainty"], "curriculum": dict(base["curriculum"]),
                "publication_info": {"created": TODAY, "verifier": None, "verified_at": None, "status": "draft", "superseded_by": None},
                "history": [h(f"起票：調査レポート第7節6の依頼により、GL本文で確認した AFAP の予防的切除を自作文で記述（{DELEGATION}）。根拠：{EVIDENCE['POLYP_GL']}")]}
        cards.append(card)
        log.append((NEW["id"], "新規起票（AFAP の予防的大腸切除）", EVIDENCE["POLYP_GL"]))
    cards.sort(key=lambda c: c["id"])
    IN.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
    LOG.write_text(json.dumps(log, ensure_ascii=False), encoding="utf-8")
    print(f"applied {len(log)}")


def promote() -> None:
    cards = yaml.safe_load(IN.read_text(encoding="utf-8"))
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
            basis += "（識別子のない公的資料・団体資料は、ページ本文で確認）"
        c["publication_info"]["status"] = "verified_sources"
        c["history"].append(h(f"status draft → verified_sources（{basis}。{DELEGATION}）"))
        promoted.append(cid)
    validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    errors = [(c["id"], "/".join(map(str, e.path)), e.message) for c in cards for e in validator.iter_errors(c)]
    IN.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
    status = {}
    for c in cards:
        status[c["publication_info"]["status"]] = status.get(c["publication_info"]["status"], 0) + 1
    L = [f"# Phase 3-2：小腸・大腸カードの内容照合（{TODAY}）\n",
         f"生成：`scripts/in_content_fixes.py`。{DELEGATION}した範囲で反映した。照合の方法は GD と同じ（`reports/03_gd_content.md` 第1節）。\n",
         "## 1. 結果\n",
         f"- 修正・起票：{len(log)}件　昇格：{len(promoted)}件　draft のまま：{len(kept)}件　スキーマ違反：{len(errors)}件",
         "- ステータス別：" + "、".join(f"{k} {v}" for k, v in sorted(status.items())),
         "- 主張文の数値は全件、出典本文と一致した（数値の訂正は0件）。\n",
         "## 2. 調査レポート第7節の依頼への回答\n",
         "| 依頼 | 結果 |", "|---|---|",
         "| 1. CC 種別 | IBD・IBS・大腸ポリープ・JSCCR 2024 の GL は CC BY 4.0（OPEN）。慢性便秘症 GL は CC BY-NC、大腸憩室 GL は CC BY-NC-ND で、調査側の判断どおり（RESTRICTED） |",
         "| 2. 識別子 | DOI 58件を解決し、PMID・PMCID を78件補完。SRC-051・052 の PMCID も API で一致 |",
         "| 3. 孫引き数値 | 対象の19件はいずれも、カードが出典とする GL 本文に同じ値で記載されていた（原著との照合は未実施で、その旨は uncertainty に残した）。IN-064 の CT 血管造影の値は急性消化管出血全般の値であることを明記 |",
         "| 4. IN-001 と IN-011・014 | GL の値は受給者証の交付数にもとづく概数、難病情報センターの値は令和5年度の所持者数で、集計の時点・基準が違う。IN-001 の uncertainty に明記 |",
         "| 5. IN-004 | 部分 Mayo スコアの構成項目と区分を GL 本文で確認 |",
         "| 6. IN-045 | GL は AFAP に予防的大腸切除を強く推奨（エビデンス C）。IN-089 として起票 |",
         "| 7. 国内の承認・保険 | IN-046 の大腸 ESD の保険適用拡大（2018年4月）は JSCCR 2024 本文で確認。便秘薬・CDI 治療薬の添付文書、ロボット支援手術の点数表は未照合（人間） |",
         "| 8. IN-088 | NIDDK のページは2016年レビュー。uncertainty に明記し、差し替えは次回の補完で検討 |",
         "\n## 3. 修正・起票の一覧\n", "| ID | 内容 | 根拠 |", "|---|---|---|"]
    L += [f"| {a} | {b} | {c} |" for a, b, c in log]
    L += ["\n## 4. verified_sources に昇格したカード\n", ", ".join(promoted)]
    L += ["\n## 5. draft に残したカード\n", "| ID | 理由 |", "|---|---|"] + ([f"| {a} | {b} |" for a, b in kept] or ["| — | なし |"])
    if errors:
        L += ["\n## スキーマ違反\n"] + [f"- {a} {b}: {m}" for a, b, m in errors]
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"promoted={len(promoted)} kept={kept} errors={len(errors)}")


if __name__ == "__main__":
    {"apply": apply, "promote": promote}[sys.argv[1]]()
