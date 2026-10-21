"""品質チェック（docs/tasks/claude_code_tasks.md Phase 5 の基本部分）。
実行: python scripts/validate.py   → reports/validate_YYYYMMDD.md を出す。問題があれば終了コード1。
"""
import collections, datetime, glob, json, os, re, sys

import yaml
from jsonschema import Draft202012Validator

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_common import card_hash  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
schema = json.load(open(os.path.join(ROOT, "schema", "fact.schema.json"), encoding="utf-8"))
V = Draft202012Validator(schema)
sources = {s["id"] for s in yaml.safe_load(open(os.path.join(ROOT, "data", "sources", "sources.yaml"), encoding="utf-8"))}

errors, warn, counts, ids = [], [], {}, collections.Counter()
needs_check, lengths, status = [], [], collections.Counter()
for path in sorted(glob.glob(os.path.join(ROOT, "data", "facts", "*.yaml"))):
    name = os.path.basename(path)
    if name.startswith("_"): continue
    cards = yaml.safe_load(open(path, encoding="utf-8")) or []
    counts[name] = len(cards)
    for c in cards:
        cid = c.get("id", "?"); ids[cid] += 1
        for e in V.iter_errors(c):
            errors.append(f"{cid}: スキーマ違反 {'/'.join(map(str, e.path))} {e.message[:120]}")
        if not cid.startswith(name[:-5]):
            errors.append(f"{cid}: ファイル {name} と接頭辞が違う")
        p = c.get("provenance", {}); pub = c.get("publication_info", {})
        status[pub.get("status")] += 1
        if p.get("legal_basis") == "E": errors.append(f"{cid}: legal_basis E は使わない")
        lic = (p.get("source_license") or "").upper()
        if p.get("source_class") == "OPEN" and re.search(r"NC|ND", lic): errors.append(f"{cid}: OPEN なのに NC/ND")
        if pub.get("status") == "verified_expert" and not pub.get("verifier"): errors.append(f"{cid}: verified_expert なのに verifier が空")
        if pub.get("status") == "verified_expert" and pub.get("verified_hash") and pub.get("verified_hash") != card_hash(c): warn.append(f"{cid}: 監修後に内容が変わっている（再監修が必要）")
        ref = p.get("source_ref")
        if ref and ref not in sources: warn.append(f"{cid}: source_ref {ref} が sources.yaml にない")
        if "要確認" in json.dumps(c, ensure_ascii=False): needs_check.append(cid)
        lengths.append((len(c["assertion"]["plain_statement_ja"]), cid))

for cid, n in ids.items():
    if n > 1: errors.append(f"{cid}: ID が {n} 回重複")
gaps = []
by_prefix = collections.defaultdict(list)
for cid in ids:
    m = re.match(r"([A-Z]+)-(\d{3})$", cid)
    if m: by_prefix[m.group(1)].append(int(m.group(2)))
for pfx, nums in sorted(by_prefix.items()):
    miss = sorted(set(range(1, max(nums) + 1)) - set(nums))
    if miss: gaps.append(f"{pfx}: " + ", ".join(f"{pfx}-{x:03d}" for x in miss))

lens = sorted(x[0] for x in lengths)
today = datetime.date.today().strftime("%Y%m%d")
L = [f"# 品質チェック {today}", "", "## 件数", "", "| ファイル | 件数 |", "|---|---|"]
L += [f"| {k} | {v} |" for k, v in counts.items()] + [f"| 合計 | {sum(counts.values())} |", ""]
L += ["## ステータス", ""] + [f"- {k}: {v}" for k, v in status.items()] + [""]
L += [f"## エラー（{len(errors)}件）", ""] + ([f"- {e}" for e in errors] or ["なし"]) + [""]
L += [f"## 警告（{len(warn)}件）", ""] + ([f"- {e}" for e in warn] or ["なし"]) + [""]
L += ["## 欠番", ""] + (gaps or ["なし"]) + [""]
L += [f"## 「要確認」を含むカード（{len(needs_check)}件）", "", ", ".join(needs_check) or "なし", ""]
if lens:
    L += ["## 主張文の文字数", "", f"最小 {lens[0]}・中央値 {lens[len(lens)//2]}・最大 {lens[-1]}", "",
          "長い順10件（分割の候補）: " + ", ".join(f"{cid}（{n}字）" for n, cid in sorted(lengths, reverse=True)[:10]), ""]
os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
out = os.path.join(ROOT, "reports", f"validate_{today}.md")
open(out, "w", encoding="utf-8").write("\n".join(L))
print(f"{sum(counts.values())}件 / エラー {len(errors)} / 警告 {len(warn)} → {os.path.relpath(out, ROOT)}")
sys.exit(1 if errors else 0)
