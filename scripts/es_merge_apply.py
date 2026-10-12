"""Phase 2-3: 承認済みの対応表（proposals/es_merge_map.csv）に従い、食道 v1／v2 を data/facts/ES.yaml に統合する。

使い方（リポジトリ直下で）:
    .\\.venv\\Scripts\\python.exe scripts\\es_merge_apply.py

- 置換：v1 の ID を残し、本文（assertion・provenance・uncertainty）を v2 の内容で置き換える。
- 新規：置換先のない R カードに ES-090 以降を付ける。
- 廃止：approved_retire_v1_ids の v1 カードと ES-068 を status: retired にし、superseded_by を記録する。
- 欠番（ES-076〜078、082〜084、088）は作らない。
- 終了後、staging ファイルを削除する（内容は git の履歴に残る）。
"""
from __future__ import annotations

import copy
import csv
import datetime as dt
import json
import re
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "data" / "facts"
V1 = FACTS / "_staging_ES_v1.yaml"
V2 = FACTS / "_staging_ES_v2.yaml"
OUT = FACTS / "ES.yaml"
CSV = ROOT / "proposals" / "es_merge_map.csv"
REPORT = ROOT / "reports" / "02_es_merge.md"
SCHEMA = ROOT / "schema" / "fact.schema.json"

TODAY = dt.date.today().isoformat()
BY = "claude-code"
FIRST_NEW_ID = 90
SPLIT_FROM_068 = "ES-068"

# 新規IDのカードの subdomain（v1 の節見出しに合わせる）
NEW_SUBDOMAIN = {
    "ES-R05": "食道癌",
    "ES-R09": "好酸球性食道炎（EoE）",
    "ES-R15": "食道癌",
    "ES-R19": "GERD・NERD・Barrett食道",
}
OTHER_SUBDOMAIN = "その他の食道疾患"


def load(path: Path) -> list[dict]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump(path: Path, data) -> None:
    text = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=10_000, default_flow_style=False)
    path.write_text(text, encoding="utf-8", newline="\n")


def h(change: str) -> dict:
    return {"date": TODAY, "by": BY, "change": change}


def is_placeholder_curriculum(cur: dict | None) -> bool:
    return not cur or all((v is None or str(v).strip() in ("", "要確認")) for v in cur.values())


def main() -> None:
    if not (V1.exists() and V2.exists()):
        raise SystemExit("staging ファイルがありません（統合済みの可能性）")
    v1 = {c["id"]: c for c in load(V1)}
    v2 = load(V2)
    with CSV.open(encoding="utf-8-sig", newline="") as f:
        rows = {r["R_id"]: r for r in csv.DictReader(f)}

    result: dict[str, dict] = {cid: copy.deepcopy(c) for cid, c in v1.items()}
    trace_v1: dict[str, str] = {cid: "存続（変更なし）" for cid in v1}
    trace_v2: dict[str, str] = {}
    next_new = FIRST_NEW_ID

    for r in v2:
        rid = r["id"]
        row = rows.get(rid)
        if row is None:
            raise SystemExit(f"対応表に {rid} の行がありません")
        card = copy.deepcopy(r)
        if rid.startswith("ES-R"):
            target = row["approved_v1_id"].strip()
            if not target:
                raise SystemExit(f"{rid} の approved_v1_id が空です")
            if target == "new":
                new_id = f"ES-{next_new:03d}"
                next_new += 1
                card["id"] = new_id
                card["subdomain"] = NEW_SUBDOMAIN.get(rid)
                card["history"].append(h(f"統合：v2 の {rid}（raw/01b_esophagus_v2.md）に新規ID {new_id} を付与（proposals/es_merge_map.csv、{row.get('decided_by', '')}）"))
                result[new_id] = card
                trace_v2[rid] = f"{new_id}（新規）"
            else:
                old = result[target]
                card["id"] = target
                card["subdomain"] = old.get("subdomain")
                card["publication_info"]["created"] = old["publication_info"]["created"]
                if is_placeholder_curriculum(card.get("curriculum")) and not is_placeholder_curriculum(old.get("curriculum")):
                    card["curriculum"] = old["curriculum"]
                card["history"] = (old.get("history") or []) + card["history"] + [
                    h(f"統合：本文を v2 の {rid}（raw/01b_esophagus_v2.md）で全文置換。ID は v1 の {target} を引き継ぐ。"
                      f"置換前の v1 本文は git 履歴の data/facts/_staging_ES_v1.yaml にある（proposals/es_merge_map.csv、{row.get('decided_by', '')}）")]
                result[target] = card
                trace_v1[target] = f"{rid} の内容で置換"
                trace_v2[rid] = f"{target}（置換）"
            successor = card["id"]
        else:
            card["subdomain"] = card.get("subdomain") or OTHER_SUBDOMAIN
            card["history"].append(h("統合：v2 の新規カード（ES-068 の分割）として ID をそのまま採用"))
            result[rid] = card
            trace_v2[rid] = f"{rid}（v2 の ID のまま）"
            successor = rid

        for old_id in [x.strip() for x in re.split(r"[;,、]", row.get("approved_retire_v1_ids", "")) if x.strip()]:
            old = result[old_id]
            old["publication_info"]["status"] = "retired"
            old["publication_info"]["superseded_by"] = successor
            old.setdefault("history", []).append(h(f"廃止：{successor} に統合（proposals/es_merge_map.csv、{row.get('decided_by', '')}）"))
            trace_v1[old_id] = f"廃止 → {successor}"

    split_ids = sorted(c["id"] for c in v2 if not c["id"].startswith("ES-R"))
    c68 = result[SPLIT_FROM_068]
    c68["publication_info"]["status"] = "retired"
    c68["publication_info"]["superseded_by"] = ", ".join(split_ids)
    c68.setdefault("history", []).append(h(f"廃止：v2 で ES-069〜089 に分割（欠番 ES-076〜078、082〜084、088 は作成保留）。superseded_by={', '.join(split_ids)}"))
    trace_v1[SPLIT_FROM_068] = f"廃止 → {', '.join(split_ids)}"

    cards = [result[k] for k in sorted(result)]
    ids = [c["id"] for c in cards]
    assert len(ids) == len(set(ids)), "ID が重複しています"

    validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    errors = [(c["id"], "/".join(map(str, e.path)), e.message) for c in cards for e in validator.iter_errors(c)]

    dump(OUT, cards)
    V1.unlink()
    V2.unlink()
    write_report(cards, trace_v1, trace_v2, rows, errors)
    print(f"ES.yaml: {len(cards)} cards, schema errors: {len(errors)}")


def write_report(cards, trace_v1, trace_v2, rows, errors) -> None:
    n = len(cards)
    retired = [c for c in cards if c["publication_info"]["status"] == "retired"]
    replaced = [k for k, v in trace_v1.items() if v.endswith("で置換")]
    new = [v for v in trace_v2.values() if v.endswith("（新規）")]
    nums = sorted(int(c["id"][3:]) for c in cards)
    gaps = [f"ES-{i:03d}" for i in range(nums[0], nums[-1] + 1) if i not in nums]
    L = [f"# Phase 2：食道 v1／v2 の統合（{TODAY}）\n",
         "生成：`scripts/es_merge_apply.py`。対応表は `proposals/es_merge_map.csv`。",
         "対応づけは、2026-10-12 に人間がチャットで「Claude の推奨で確定」と委任したため、Claude Code が決定した（`scripts/es_merge_decide.py`）。\n",
         "## 1. 件数\n",
         "| 項目 | 件数 |", "|---|---|",
         f"| ES.yaml のカード総数 | {n} |",
         f"| うち有効（retired 以外） | {n - len(retired)} |",
         f"| 置換（v1 の ID を引き継ぎ） | {len(replaced)} |",
         f"| 新規（ES-090〜） | {len(new)} |",
         f"| v2 の ID のまま採用（ES-069〜） | {sum(1 for v in trace_v2.values() if 'v2 の ID のまま' in v)} |",
         f"| 廃止（retired） | {len(retired)} |",
         f"| 欠番 | {len(gaps)}（{', '.join(gaps)}） |",
         f"| スキーマ違反 | {len(errors)} |",
         f"| ID の重複 | 0 |\n"]
    if errors:
        L.append("### スキーマ違反\n")
        L += [f"- {cid} {path}: {msg}" for cid, path, msg in errors]
        L.append("")
    L.append("## 2. v2 のカードの行き先と決定理由\n")
    L.append("| v2 | 統合後 | 廃止した v1 | 理由 |\n|---|---|---|---|")
    for rid, dest in trace_v2.items():
        row = rows[rid]
        L.append(f"| {rid} | {dest} | {row.get('approved_retire_v1_ids') or '—'} | {row.get('decision_reason', '')} |")
    L.append("\n## 3. v1 のカードの行き先\n")
    L.append("| v1 | 統合後 |\n|---|---|")
    for cid in sorted(trace_v1):
        L.append(f"| {cid} | {trace_v1[cid]} |")
    L.append("\n## 4. 補足\n")
    L.append("- 置換したカードの `created`・`subdomain`・`history` は v1 から引き継いだ。`curriculum` は v2 側が「要確認」だけの場合に限り v1 の値を残した。")
    L.append("- provenance は統合では変更していない（識別子は Phase 3 の API 照合で確定する）。")
    L.append("- ES-067（Mallory-Weiss と Boerhaave、出典未取得）は存続。欠番の ES-084（Mallory-Weiss）を起票した後に扱いを決める。")
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
