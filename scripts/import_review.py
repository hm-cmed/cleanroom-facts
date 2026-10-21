"""Phase 6: 専門医が記入したレビューシートを取り込む。

使い方（リポジトリ直下で）:
    .\\.venv\\Scripts\\python.exe scripts\\import_review.py review\\review_ES_20261012.xlsx          # 確認だけ（書き込まない）
    .\\.venv\\Scripts\\python.exe scripts\\import_review.py review\\review_ES_20261012.xlsx --apply  # 反映する

- 判定 OK   → verifier・verified_at に「説明」シートの確認者・確認日を記録し、verified_expert に昇格。
- 判定 修正 → proposals/review_fixes_<領域>_<日付>.md に修正案として出す。本文は書き換えない。
- 判定 削除 → 同じファイルに廃止の提案として出す。カードは変更しない。
- 空欄      → 何もしない。

verifier と verified_expert は、ここでは専門医の記入内容を転記するだけ（CLAUDE.md 1-4：設定するのは人間）。
確認者・確認日が空なら、何も反映しない。
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

import yaml
from openpyxl import load_workbook

sys.path.insert(0, str(Path(__file__).resolve().parent))
from review_common import card_hash  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "data" / "facts"
PROPOSALS = ROOT / "proposals"
REPORTS = ROOT / "reports"


def cell_str(v) -> str:
    if v is None:
        return ""
    if isinstance(v, (dt.date, dt.datetime)):
        return v.strftime("%Y-%m-%d")
    return str(v).strip()


def main(argv: list[str]) -> None:
    path = Path(argv[0])
    apply = "--apply" in argv
    m = re.match(r"review_([A-Z]{2})_(\d{8})", path.stem)
    if not m:
        raise SystemExit("ファイル名は review_<接頭辞>_<YYYYMMDD>.xlsx の形式にしてください")
    prefix = m.group(1)
    wb = load_workbook(path, data_only=True)
    reviewer = cell_str(wb["説明"]["B2"].value)
    reviewed_on = cell_str(wb["説明"]["B3"].value)
    if not reviewer or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", reviewed_on):
        raise SystemExit("「説明」シートの確認者（B2）と確認日（B3, YYYY-MM-DD）を記入してください")

    ws = wb["review"]
    head = [cell_str(c.value) for c in ws[1]]
    col = {name: i for i, name in enumerate(head)}
    entries = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        cid = cell_str(row[col["ID"]])
        if not cid:
            continue
        entries.append({"id": cid, "judge": cell_str(row[col["判定"]]), "fix": cell_str(row[col["修正案"]]),
                        "comment": cell_str(row[col["コメント"]]), "statement": cell_str(row[col["主張文"]])})

    facts_path = FACTS / f"{prefix}.yaml"
    cards = yaml.safe_load(facts_path.read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in cards}
    ok, fixes, deletes, unknown, errors = [], [], [], [], []
    for e in entries:
        c = by_id.get(e["id"])
        if c is None:
            errors.append(f"{e['id']}: 正本にない ID")
            continue
        if e["statement"] != c["assertion"]["plain_statement_ja"]:
            errors.append(f"{e['id']}: シート出力後に主張文が変わっている。最新のシートで確認し直す必要がある")
            continue
        j = e["judge"]
        if j == "OK":
            ok.append((c, e))
        elif j == "修正":
            if not e["fix"]:
                errors.append(f"{e['id']}: 判定が「修正」だが修正案が空")
            fixes.append((c, e))
        elif j == "削除":
            deletes.append((c, e))
        elif j:
            errors.append(f"{e['id']}: 判定「{j}」は OK／修正／削除 のいずれでもない")

    by = f"human:{reviewer}"
    ok_drafts = [c["id"] for c, _ in ok if c["publication_info"]["status"] == "draft"]
    if apply and not errors:
        for c, e in ok:
            pub = c["publication_info"]
            before = pub["status"]
            pub["verifier"], pub["verified_at"], pub["status"] = reviewer, reviewed_on, "verified_expert"
            pub["verified_hash"] = card_hash(c)  # 監修した版を記録（その後に内容が変わったら再監修の対象になる）
            note = f"専門医レビューで OK（{path.name}）。status {before} → verified_expert"
            if e["comment"]:
                note += f"。コメント：{e['comment']}"
            c.setdefault("history", []).append({"date": reviewed_on, "by": by, "change": note})
        facts_path.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
        if fixes or deletes:
            L = [f"# 専門医レビューからの提案（{prefix}、{reviewed_on}、確認者 {reviewer}）\n",
                 f"取り込み元：`{path.as_posix()}`。本文は書き換えていない。反映には人間の承認が必要。\n",
                 "| ID | 判定 | 現在の主張文 | 修正案 | コメント | 承認 |", "|---|---|---|---|---|---|"]
            for c, e in fixes + deletes:
                L.append(f"| {c['id']} | {e['judge']} | {c['assertion']['plain_statement_ja']} | {e['fix'].replace('|', '／')} | {e['comment'].replace('|', '／')} | |")
            (PROPOSALS / f"review_fixes_{prefix}_{reviewed_on.replace('-', '')}.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")

    R = [f"# 専門医レビューの取り込み（{prefix}、{dt.date.today().isoformat()}）\n",
         f"- シート：`{path.as_posix()}`、確認者：{reviewer}、確認日：{reviewed_on}",
         f"- モード：{'反映' if apply and not errors else '確認のみ（書き込みなし）'}",
         f"- OK：{len(ok)}件、修正：{len(fixes)}件、削除：{len(deletes)}件、未記入：{len(entries) - len(ok) - len(fixes) - len(deletes) - len(unknown)}件\n"]
    if errors or unknown:
        R += ["## 要対応（エラーがあると何も反映しない）\n"] + [f"- {x}" for x in errors + unknown]
    if ok:
        R += ["\n## OK（verified_expert）\n", ", ".join(c["id"] for c, _ in ok)]
        if ok_drafts:
            R += [f"\n注：出典照合が未了（draft）のまま OK になったカード：{', '.join(ok_drafts)}"]
    out = REPORTS / f"review_import_{prefix}_{reviewed_on.replace('-', '')}.md"
    out.write_text("\n".join(R) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(R))


if __name__ == "__main__":
    main(sys.argv[1:])
