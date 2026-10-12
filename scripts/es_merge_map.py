"""Phase 2-1: 食道 v1（ES-001〜068）と v2（ES-R01〜R19、ES-069〜）の対応表の案を作る。

使い方（リポジトリ直下で）:
    .\\.venv\\Scripts\\python.exe scripts\\es_merge_map.py

出力: proposals/es_merge_map.csv（UTF-8 BOM付き。Excel でそのまま開ける）
`approved_v1_id` 列は人間が埋める。このスクリプトは空欄のまま出力する。
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

import yaml
from rapidfuzz import fuzz

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "data" / "facts"
OUT = ROOT / "proposals" / "es_merge_map.csv"

V1 = FACTS / "_staging_ES_v1.yaml"
V2 = FACTS / "_staging_ES_v2.yaml"

# ES-068 は v2 で廃止・分割が決まっているため、置換先の候補にしない
EXCLUDE_V1 = {"ES-068"}
MAX_CANDIDATES = 3
# 主張文の類似度は文字バイグラムの Dice 係数（0〜100）。和文の言い換えでは値が低めに出るため、
# 出典の一致（LINK_BONUS）と組み合わせて判定する。
LINK_BONUS = 15.0
MIN_SCORE = 12.0   # 候補として挙げる最低スコア
STRONG = 18.0      # replace／split の候補とみなすスコア
KEEP_OVERLAP = 20.0  # ES-069〜 と v1 の重複を注記するスコア

TERM_RE = re.compile(r"[A-Za-z][A-Za-z0-9\-\.]*[A-Za-z0-9]|\d+(?:\.\d+)?")
STOP_TERMS = {"vs", "et", "al", "of", "the", "and"}


def load(path: Path) -> list[dict]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def terms(text: str) -> set[str]:
    return {t.lower() for t in TERM_RE.findall(text or "") if t.lower() not in STOP_TERMS}


def first_author(source: str) -> str | None:
    m = re.match(r"\s*([A-Z][A-Za-z\-À-ÿ]+)\s+[A-Z]{1,3}\b", source or "")
    return m.group(1).lower() if m else None


def source_link(a: dict, b: dict) -> str | None:
    """出典の一致の根拠を返す（なければ None）。"""
    pa, pb = a["provenance"], b["provenance"]
    if pa.get("source_ref") and pa["source_ref"] == pb.get("source_ref"):
        return f"source_ref={pa['source_ref']}"
    for key in ("doi", "pmid", "pmcid"):
        if pa.get(key) and pa[key] == pb.get(key):
            return f"{key}={pa[key]}"
    fa, fb = first_author(pa.get("source")), first_author(pb.get("source"))
    if fa and fa == fb:
        return f"first_author={fa}"
    return None


PUNCT_RE = re.compile(r"[\s、。，．（）()「」・:：;；/／\-]")


def bigrams(text: str) -> set[str]:
    s = PUNCT_RE.sub("", text or "")
    return {s[i:i + 2] for i in range(len(s) - 1)}


def text_similarity(a: str, b: str) -> float:
    """文字バイグラムの Dice 係数。分かち書きのない和文でも語順の違いに強い。"""
    A, B = bigrams(a), bigrams(b)
    return 200.0 * len(A & B) / (len(A) + len(B)) if A and B else 0.0


def score(r: dict, v: dict) -> tuple[float, dict]:
    sa, sb = r["assertion"]["plain_statement_ja"], v["assertion"]["plain_statement_ja"]
    ts = text_similarity(sa, sb)
    ta, tb = terms(sa), terms(sb)
    tj = 100.0 * len(ta & tb) / len(ta | tb) if ta | tb else 0.0
    link = source_link(r, v)
    total = ts + 0.1 * tj + (LINK_BONUS if link else 0.0)
    return round(total, 1), {"text": round(ts, 1), "terms": round(tj, 1), "link": link,
                             "ratio": round(fuzz.ratio(sa, sb), 1), "shared_terms": sorted(ta & tb)}


def propose(r: dict, v1: list[dict]) -> dict:
    scored = []
    for v in v1:
        if v["id"] in EXCLUDE_V1:
            continue
        s, detail = score(r, v)
        if s >= MIN_SCORE:
            scored.append((s, v["id"], detail))
    scored.sort(key=lambda x: (-x[0], x[1]))
    top = scored[:MAX_CANDIDATES]

    strong = [t for t in top if t[0] >= STRONG]
    # 2件目以降は、1件目と同じ出典で、スコアが1件目の6割以上あるものだけを「またがり」とみなす
    spans = [t for t in strong[1:] if t[2]["link"] and strong[0][2]["link"] and t[0] >= 0.6 * strong[0][0]]
    if strong and spans:
        action = "split"
    elif strong:
        action = "replace"
    else:
        action = "new"

    basis = []
    for s, vid, d in top:
        parts = [f"dice={d['text']}", f"terms={d['terms']}"]
        if d["link"]:
            parts.append(d["link"])
        basis.append(f"{vid}: " + ", ".join(parts))
    return {
        "candidates": [vid for _, vid, _ in top],
        "scores": [s for s, _, _ in top],
        "basis": " / ".join(basis),
        "action": action,
        "details": top,
    }


def numbers(text: str) -> set[str]:
    return set(re.findall(r"\d+(?:\.\d+)?", text or ""))


def main() -> None:
    v1 = load(V1)
    v2 = load(V2)
    v1_by_id = {c["id"]: c for c in v1}
    rows = []
    for r in v2:
        is_r = r["id"].startswith("ES-R")
        p = propose(r, v1)
        notes = []
        if not is_r:
            # ES-069〜 は v2 で ID が確定済み（ES-068 の分割）。置換ではなく、v1 との重複の確認用に候補を出す
            action = "keep"
            for s, vid, _ in p["details"]:
                if s >= KEEP_OVERLAP:
                    notes.append(f"v1 の {vid} と内容が重なる可能性（score {s}）。重複なら v1 側を retired（superseded_by={r['id']}）にするか判断が必要")
        else:
            action = p["action"]
            if action == "split":
                notes.append("複数の v1 カードにまたがる。どの v1 ID を引き継ぎ、残りをどう扱うか（retired か存続か）の判断が必要")
            if action == "new":
                notes.append("置換先の候補が弱い。新規ID（ES-090〜）の付与を想定")
            if p["details"] and action != "new":
                top = p["details"][0][0]
                for s, vid, d in p["details"][1:]:
                    if s >= 30.0 and s >= 0.7 * top and action != "split":
                        notes.append(f"{vid} とも内容が重なる（score {s}、出典一致{'あり' if d['link'] else 'なし'}）")
        # 数値の食い違いの注意喚起（v1 候補にあって v2 にない数値）
        nr = numbers(r["assertion"]["plain_statement_ja"])
        for i, (s, vid, d) in enumerate(p["details"]):
            # 1位の候補と、出典が一致する候補だけを見る（無関係な候補の数値差は注記しない）
            if s < STRONG or not (i == 0 or d["link"]):
                continue
            nv = numbers(v1_by_id[vid]["assertion"]["plain_statement_ja"])
            only_v1 = sorted(nv - nr, key=float)
            if only_v1 and nr & nv:
                notes.append(f"{vid} にだけある数値：{', '.join(only_v1)}")
        rows.append({
            "R_id": r["id"],
            "candidate_v1_ids": ";".join(p["candidates"]),
            "match_basis": p["basis"],
            "score": ";".join(str(s) for s in p["scores"]),
            "proposed_action": action,
            "note": "／".join(notes),
            "approved_v1_id": "",
            "approved_retire_v1_ids": "",
            "R_statement": r["assertion"]["plain_statement_ja"],
            "candidate_statements": " ‖ ".join(f"{vid}: {v1_by_id[vid]['assertion']['plain_statement_ja']}" for vid in p["candidates"]),
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fields = ["R_id", "candidate_v1_ids", "match_basis", "score", "proposed_action", "note",
              "approved_v1_id", "approved_retire_v1_ids", "R_statement", "candidate_statements"]
    with OUT.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    for row in rows:
        print(f"{row['R_id']:7} {row['proposed_action']:8} {row['candidate_v1_ids']:24} {row['score']:18} {row['note'][:60]}")


if __name__ == "__main__":
    main()
