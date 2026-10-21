"""GitHub の Issue フォームで送られた監修結果を、事実カードに反映する（GitHub Actions から呼ぶ）。

    python scripts/apply_github_review.py --event "$GITHUB_EVENT_PATH" --permission write --out result.md

- 承認：送られた「版」が今のカードの版と一致するときだけ、verifier（監修者名）・verified_at・
  verified_hash を記録し、status を verified_expert にする。主張文や数値は変えない。
- 修正が必要／廃止すべき：カードは変えず、proposals/ に修正案のファイルを作る（CLAUDE.md 1-2）。
- レポジトリへの書き込み権限（write 以上）がない人の送信は反映しない。

verifier と verified_expert は、監修者（人間）がフォームに書いて送った内容を転記するだけである（CLAUDE.md 1-4）。
結果は --out のファイル（Issue へのコメント本文）と、GITHUB_OUTPUT（changed / close / labels）に書く。
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re

from review_common import ROOT, card_hash, dump, load_all, parse_form

ALLOWED = {"admin", "maintain", "write"}
JST = dt.timezone(dt.timedelta(hours=9))
ID_RE = re.compile(r"^[A-Z]{2}-\d{3}$")
VER_RE = re.compile(r"^[0-9a-f]{10}$")


def clean_name(s: str) -> str:
    s = re.sub(r"[\r\n\t]+", " ", s or "").strip()
    return s[:60]


def set_output(**kv: str) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        print(kv)
        return
    with open(path, "a", encoding="utf-8") as f:
        for k, v in kv.items():
            f.write(f"{k}={v}\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--event", required=True)
    ap.add_argument("--permission", default="")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    ev = json.loads(open(args.event, encoding="utf-8").read())
    issue = ev.get("issue") or {}
    number = issue.get("number")
    login = (ev.get("sender") or {}).get("login") or (issue.get("user") or {}).get("login") or "unknown"
    form = parse_form(issue.get("body") or "")
    msg: list[str] = []

    def finish(changed: bool, close: bool, labels: str = "") -> int:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write("\n".join(msg) + "\n")
        set_output(changed="true" if changed else "false", close="true" if close else "false", labels=labels)
        return 0

    if args.permission not in ALLOWED:
        msg.append(f"@{login} さんにはこのレポジトリへの書き込み権限がないため、監修結果は反映していません。"
                   "監修者として登録が必要な場合は、管理者に連絡してください。")
        return finish(False, False, "権限なし")

    reviewer = clean_name(form.get("監修者名", ""))
    if not reviewer:
        msg.append("監修者名が空のため、反映していません。Issue を編集して監修者名を書いてください。")
        return finish(False, False)
    if "[x]" not in form.get("確認", "").lower():
        msg.append("「確認」のチェックが入っていないため、反映していません。")
        return finish(False, False)

    # 対象カードの一覧（まとめて承認／1枚）
    targets: list[tuple[str, str]] = []
    if "まとめて承認するカード" in form:
        judge = "承認"
        for line in form["まとめて承認するカード"].splitlines():
            parts = line.strip().split()
            if not parts:
                continue
            targets.append((parts[0], parts[1] if len(parts) > 1 else ""))
    else:
        j = form.get("判定", "")
        judge = "承認" if j.startswith("承認") else "修正" if j.startswith("修正") else "廃止" if j.startswith("廃止") else ""
        targets.append((form.get("カードID", "").strip(), form.get("確認した版", "").strip()))
    if not judge or not targets:
        msg.append("判定またはカードIDが読み取れませんでした。フォームから送信してください。")
        return finish(False, False)
    if len(targets) > 100:
        msg.append("一度にまとめて承認できるのは100件までです。")
        return finish(False, False)

    all_cards = load_all()
    index = {c["id"]: (prefix, c) for prefix, cards in all_cards.items() for c in cards}
    today = dt.datetime.now(JST).date().isoformat()
    comment = re.sub(r"\s+", " ", form.get("コメント", "")).strip()[:500]
    who = f"{reviewer}（GitHub @{login}）"
    done, already, problems = [], [], []
    touched: set[str] = set()

    for cid, ver in targets:
        if not ID_RE.match(cid) or cid not in index:
            problems.append(f"`{cid}`：このIDのカードはありません")
            continue
        prefix, card = index[cid]
        pub = card.setdefault("publication_info", {})
        h = card_hash(card)
        if pub.get("status") == "retired":
            problems.append(f"`{cid}`：廃止されたカードです")
            continue
        if not VER_RE.match(ver) or ver != h:
            problems.append(f"`{cid}`：確認した版（`{ver or '空'}`）が今のカード（`{h}`）と違います。"
                            "監修ページを開き直し、最新の内容で確認してください")
            continue
        if judge == "承認":
            if pub.get("status") == "verified_expert" and pub.get("verified_hash") == h:
                already.append(cid)
                continue
            before = pub.get("status")
            pub["verifier"], pub["verified_at"], pub["status"], pub["verified_hash"] = who, today, "verified_expert", h
            note = f"GitHub の監修（Issue #{number}）で承認。status {before} → verified_expert"
            if comment:
                note += f"。コメント：{comment}"
            card.setdefault("history", []).append({"date": today, "by": f"human:{who}", "change": note})
            touched.add(prefix)
            done.append(cid + ("（出典の照合前のカード）" if before == "draft" else ""))
        else:
            fix = (form.get("修正案") or "").strip()
            path = ROOT / "proposals" / f"github_review_{cid}_issue{number}.md"
            path.parent.mkdir(exist_ok=True)
            path.write_text("\n".join([
                f"# 監修からの{'修正' if judge == '修正' else '廃止'}の提案：{cid}（Issue #{number}）", "",
                f"- 監修者：{who}", f"- 日付：{today}", f"- 確認した版：`{h}`", "",
                "## 現在の主張文", "", (card.get("assertion") or {}).get("plain_statement_ja", ""), "",
                "## 修正案", "", fix or "（記入なし）", "",
                "## コメント", "", form.get("コメント", "") or "（記入なし）", "",
                "本文は書き換えていない。反映には担当者の判断が必要（CLAUDE.md 1-2）。", ""]),
                encoding="utf-8", newline="\n")
            done.append(cid)

    for prefix in touched:
        dump(prefix, all_cards[prefix])
    changed = bool(touched) or (judge != "承認" and bool(done))

    if judge == "承認":
        if done:
            msg.append(f"{reviewer} さんの監修を記録しました（{today}）。次のカードを「監修済み」にしました：")
            msg.append("")
            msg += [f"- {x}" for x in done]
        if already:
            if msg:
                msg.append("")
            msg.append("すでに同じ内容で監修済みのカード：" + "、".join(already))
    else:
        if done:
            msg.append(f"修正案として記録しました（`proposals/github_review_{done[0]}_issue{number}.md`）。"
                       "カードの文章は変えていません。担当者が対応したら、この Issue でお知らせします。")
    if problems:
        msg.append("")
        msg.append("**反映できなかったもの**")
        msg.append("")
        msg += [f"- {p}" for p in problems]
    if not done and not already and not problems:
        msg.append("反映するものがありませんでした。")
    close = judge == "承認" and not problems
    labels = "監修済み" if close else ("修正案" if judge != "承認" and done else "要確認")
    return finish(changed, close, labels)


if __name__ == "__main__":
    raise SystemExit(main())
