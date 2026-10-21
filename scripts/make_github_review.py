"""GitHub 上で監修するためのページ（review/github/*.md）を作る。

    python scripts/make_github_review.py

- review/github/README.md：領域ごとの進み具合（監修済み・未監修の件数）と各ページへのリンク
- review/github/<接頭辞>.md：小見出し（subdomain）ごとにカードを並べ、
  カードごとに「このカードを監修する」、10件ごとに「まとめて承認する」のリンクを付ける。
  リンクを開くと、カードIDと版が入った Issue フォームが開く。

カードの内容は書き換えない（読み出して並べるだけ）。全分野の data/facts/*.yaml を対象にする。
"""
from __future__ import annotations

import collections
import datetime as dt
from urllib.parse import quote

from review_common import REPO, ROOT, card_hash, load_all, load_domains, needs_review

OUT = ROOT / "review" / "github"
BATCH = 10
STATUS_JA = {
    "draft": "下書き（出典の照合前）",
    "verified_sources": "出典照合済み・監修待ち",
    "verified_expert": "監修済み",
    "retired": "廃止",
}


def issue_url(template: str, **fields: str) -> str:
    q = "&".join(f"{k}={quote(v, safe='')}" for k, v in fields.items())
    return f"https://github.com/{REPO}/issues/new?template={template}&{q}"


def fmt(v) -> str:
    if v is None or v == "":
        return ""
    if isinstance(v, dict):
        return "／".join(f"{k}: {fmt(x)}" for k, x in v.items() if x not in (None, ""))
    if isinstance(v, list):
        return "／".join(fmt(x) for x in v)
    return str(v).replace("\n", " ")


def card_block(c: dict) -> list[str]:
    a = c.get("assertion") or {}
    p = c.get("provenance") or {}
    pub = c.get("publication_info") or {}
    cur = c.get("curriculum") or {}
    h = card_hash(c)
    status = STATUS_JA.get(pub.get("status"), pub.get("status") or "")
    changed = pub.get("status") == "verified_expert" and pub.get("verified_hash") and pub.get("verified_hash") != h
    if pub.get("status") == "verified_expert":
        status += f"（{pub.get('verifier') or ''}、{pub.get('verified_at') or ''}）"
    if changed:
        status = "**監修後に内容が変わったため、再監修が必要**"
    L = [f"### {c['id']}　{status}", "", f"> {fmt(a.get('plain_statement_ja'))}", ""]
    for label, val in (("条件", a.get("condition")), ("鑑別・補足", a.get("differential")),
                       ("よくある誤解", a.get("common_misconception")), ("不確実性", c.get("uncertainty"))):
        if fmt(val):
            L.append(f"- {label}：{fmt(val)}")
    src = fmt(p.get("source"))
    if p.get("doi"):
        src += f"　[DOI {p['doi']}](https://doi.org/{p['doi']})"
    if p.get("pmid"):
        src += f"　[PMID {p['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{p['pmid']}/)"
    elif p.get("url") and not p.get("doi"):
        src += f"　[リンク]({p['url']})"
    L.append(f"- 出典：{src}（区分 {p.get('source_class') or '不明'}）")
    if cur.get("kokushi") or cur.get("core_curriculum"):
        L.append(f"- 出題基準：{cur.get('kokushi') or '－'}　コアカリ：{cur.get('core_curriculum') or '－'}")
    if needs_review(c):
        L.append(f"- [このカードを監修する]({issue_url('fact-review.yml', title=f'[監修] {c['id']}', card_id=c['id'], version=h)})　（版 `{h}`）")
    L.append("")
    return L


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    domains = load_domains()
    all_cards = load_all()
    today = dt.date.today().isoformat()
    index = ["# 事実カードの監修（GitHub 版）", "",
             f"更新：{today}（`python scripts/make_github_review.py` で作り直す。手で編集しない）", "",
             "## 監修のしかた", "",
             "1. 下の表から領域を選び、ページを開く。",
             "2. カードを出典と照らして読む（主張文・数値・条件・出典）。",
             "3. 問題がなければ、小見出しの最後にある「**まとめて承認する**」を開き、監修者名を書いて送信する。"
             "直すべきカードがあれば、一覧からその行を消してから送信する。",
             "4. 直すべきカードは、そのカードの「**このカードを監修する**」から「修正が必要」を選び、修正案を書いて送信する。",
             "5. 数分で自動的にカードに記録され、このページも更新される（承認したカードには監修者名と日付が付く）。", "",
             "承認したあとにカードの内容が変わると「再監修が必要」と表示され、問題サイトでも監修済みとして扱われなくなる。", "",
             "## 進み具合", "",
             "| 分野 | 接頭辞 | 領域 | 全件 | 監修済み | 未監修 | 再監修が必要 |", "|---|---|---|---|---|---|---|"]
    totals = collections.Counter()
    for prefix, cards in all_cards.items():
        live = [c for c in cards if (c.get("publication_info") or {}).get("status") != "retired"]
        done = [c for c in live if not needs_review(c)]
        changed = [c for c in live if (c.get("publication_info") or {}).get("status") == "verified_expert" and needs_review(c)]
        d = domains.get(prefix, {})
        index.append(f"| {d.get('field', '')} | {prefix} | [{d.get('name', prefix)}]({prefix}.md) | {len(live)} | {len(done)} | {len(live) - len(done) - len(changed)} | {len(changed)} |")
        totals.update(all=len(live), done=len(done), changed=len(changed))

        L = [f"# {prefix} {d.get('name', '')} の監修", "", f"[← 一覧に戻る](README.md)　更新：{today}", "",
             f"全 {len(live)} 件のうち、監修済み {len(done)} 件。", ""]
        groups: dict[str, list[dict]] = collections.OrderedDict()
        for c in live:
            groups.setdefault(c.get("subdomain") or "（小見出しなし）", []).append(c)
        for sub, cs in groups.items():
            L += [f"## {sub}", ""]
            pending: list[dict] = []
            for c in cs:
                L += card_block(c)
                if needs_review(c):
                    pending.append(c)
                if len(pending) == BATCH:
                    L += batch_link(pending)
                    pending = []
            if pending:
                L += batch_link(pending)
        (OUT / f"{prefix}.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    index.append(f"| 合計 | | | {totals['all']} | {totals['done']} | {totals['all'] - totals['done'] - totals['changed']} | {totals['changed']} |")
    (OUT / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8", newline="\n")
    print(f"review/github/ を更新しました（{len(all_cards)} 領域、{totals['all']} 件）")


def batch_link(cards: list[dict]) -> list[str]:
    lines = "\n".join(f"{c['id']} {card_hash(c)}" for c in cards)
    ids = f"{cards[0]['id']}〜{cards[-1]['id']}" if len(cards) > 1 else cards[0]["id"]
    url = issue_url("fact-batch-approve.yml", title=f"[監修] まとめて承認 {ids}", cards=lines)
    return [f"**[ここまでの {len(cards)} 件（{ids}）をまとめて承認する]({url})**", "", "---", ""]


if __name__ == "__main__":
    main()
