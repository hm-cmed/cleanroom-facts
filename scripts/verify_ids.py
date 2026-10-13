"""Phase 3: 識別子（DOI・PMID・PMCID）とライセンスを Crossref・NCBI で照合する。

使い方（リポジトリ直下で）:
    .\\.venv\\Scripts\\python.exe scripts\\verify_ids.py            # data/facts/*.yaml 全部
    .\\.venv\\Scripts\\python.exe scripts\\verify_ids.py ES         # 接頭辞を指定

書き込み規則（docs/tasks/claude_code_tasks.md Phase 3）:
- 既存値と API が一致 → id_check に記録。
- 既存値が空で、DOI 経由で一意に確定 → pmid・pmcid を書き込み、history に記録。
- 既存値と API が食い違う → 書き換えず reports/03_id_conflicts.md に記録。
- PMID・PMCID だけのカード → esummary の書誌が source と合えば、API が返した DOI 等を補う。
- 識別子のないカード → Crossref の候補を proposals/id_candidates.csv に出すだけ（書き込まない）。
- license URL から source_class を判定。既存値と食い違えばレポートに出す。
  ES は人間の委任（2026-10-12）により判定値を反映する。HP・UG はレポートのみ。
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
import unicodedata
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ncbi_crossref import (Unresolved, crossref_search, crossref_work, doi_agency, esearch_doi,  # noqa: E402
                           esummary, idconv)

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "data" / "facts"
REPORTS = ROOT / "reports"
PROPOSALS = ROOT / "proposals"
TODAY = dt.date.today().isoformat()
BY = "claude-code"
APPLY_LICENSE_CLASS = {"ES", "GD", "IN"}  # source_class の判定値を反映する領域（人間の委任：ES 2026-10-12、GD・IN 2026-10-13）


def h(change: str) -> dict:
    return {"date": TODAY, "by": BY, "change": change}


def split_dois(value) -> list[str]:
    if not value:
        return []
    return [d.strip().rstrip(".") for d in re.split(r"[;,\s]+", str(value)) if d.strip().startswith("10.")]


def fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(ch for ch in s if not unicodedata.combining(ch)).lower()


def classify_license(licenses: list[dict]) -> tuple[str | None, str | None]:
    """Crossref の license 配列から (source_class, 代表URL) を返す。情報がなければ (None, None)。"""
    if not licenses:
        return None, None
    # 公開版（vor）の記載を優先
    ordered = sorted(licenses, key=lambda l: 0 if l.get("content-version") == "vor" else 1)
    urls = [l.get("URL", "") for l in ordered]
    for u in urls:
        lu = u.lower()
        if "creativecommons.org" in lu and ("by-nc" in lu or "by-nd" in lu):
            return "RESTRICTED", u
    for u in urls:
        lu = u.lower()
        if re.search(r"creativecommons\.org/licenses/by/", lu) or "publicdomain/zero" in lu:
            return "OPEN", u
    return "RESTRICTED", urls[0]


def bib_from_crossref(w: dict) -> dict:
    issued = (w.get("issued") or {}).get("date-parts") or [[None]]
    authors = w.get("author") or []
    return {
        "title": (w.get("title") or [""])[0],
        "journal": (w.get("container-title") or [""])[0],
        "short_journal": (w.get("short-container-title") or [""])[0],
        "year": str(issued[0][0]) if issued and issued[0] and issued[0][0] else None,
        "volume": w.get("volume"),
        "page": w.get("page") or w.get("article-number"),
        "first_author": authors[0].get("family") if authors else None,
    }


def bib_matches_source(bib: dict, source: str) -> tuple[bool, str]:
    """source の文字列と書誌が矛盾しないか（年と、著者名か雑誌名のどちらか）。"""
    src = fold(source)
    reasons = []
    # オンライン先行公開と冊子体で年が1年ずれることがあるため ±1 年を許容
    y = bib.get("year")
    year_ok = bool(y) and y.isdigit() and any(str(int(y) + d) in src for d in (0, 1, -1))
    title_words = [w for w in re.findall(r"[a-z0-9]+", fold(bib.get("title") or "")) if len(w) > 3]
    title_ok = bool(title_words) and sum(w in src for w in title_words) >= 0.5 * len(title_words)
    if title_ok:
        return True, ""
    if not year_ok:
        reasons.append(f"年 {bib.get('year')} が source にない")
    who = bib.get("first_author")
    author_ok = bool(who) and fold(who) in src
    journal_ok = False
    for j in (bib.get("journal"), bib.get("short_journal")):
        if j and len(j) > 2:
            words = [w for w in re.findall(r"[a-z]+", fold(j)) if len(w) > 2 and w not in ("the", "and", "journal", "of")]
            if words and sum(w[:5] in src for w in words) >= max(1, len(words) // 2):
                journal_ok = True
    vol_ok = bool(bib.get("volume")) and re.search(rf"(?<!\d){re.escape(str(bib['volume']))}(?!\d)", src) is not None
    if not (author_ok or journal_ok or vol_ok):
        reasons.append(f"著者 {who}・雑誌 {bib.get('journal')}・巻 {bib.get('volume')} のいずれも source にない")
    ok = year_ok and (author_ok or journal_ok or vol_ok)
    return ok, "；".join(reasons)


def bib_from_esummary(doc: dict) -> dict:
    ids = {a["idtype"]: a["value"] for a in doc.get("articleids", [])}
    authors = doc.get("authors") or []
    first = authors[0]["name"].split(" ")[0] if authors else None
    return {
        "title": doc.get("title"),
        "journal": doc.get("fulljournalname"),
        "short_journal": doc.get("source"),
        "year": (doc.get("pubdate") or "")[:4] or None,
        "volume": doc.get("volume"),
        "page": doc.get("pages"),
        "first_author": first,
        "doi": ids.get("doi"),
        "pmc": ids.get("pmc"),
    }


class Checker:
    def __init__(self):
        self.conflicts: list[tuple] = []
        self.unresolved: list[tuple] = []
        self.class_diffs: list[tuple] = []
        self.filled: list[tuple] = []
        self.candidates: list[dict] = []
        self.summary: list[dict] = []
        self.validated: dict[str, str] = {}  # 書誌照合が通った DOI → 最初のカードID

    def check(self, card: dict, domain: str) -> None:
        p = card["provenance"]
        cid = card["id"]
        notes: list[str] = []
        idc = {"checked_at": TODAY, "doi_resolved": False, "pmid_matched": None,
               "license_from_crossref": None, "notes": None}
        dois = split_dois(p.get("doi"))
        if len(dois) > 1:
            notes.append(f"DOI が複数（{', '.join(dois)}）。先頭を主たる DOI として照合")
        try:
            if dois:
                self._by_doi(card, dois[0], idc, notes, domain)
            elif p.get("pmid"):
                self._by_pmid(card, idc, notes)
            elif p.get("pmcid"):
                self._by_pmcid(card, idc, notes)
            else:
                self._no_ids(card, notes)
        except Unresolved as e:
            notes.append(f"unresolved：{e}")
            self.unresolved.append((cid, str(e)))
        idc["notes"] = "／".join(notes) or None
        p["id_check"] = idc
        self.summary.append({"id": cid, **idc, "status": card["publication_info"]["status"]})

    # --- DOI があるカード
    def _by_doi(self, card, doi, idc, notes, domain):
        p, cid = card["provenance"], card["id"]
        w = crossref_work(doi)
        if w is None:
            ag = doi_agency(doi)
            if ag["agency"] and ag["agency"] != "Crossref" and ag["resolves"]:
                # JaLC・DataCite などに登録された DOI。実在は doi.org で確認、ライセンスは Crossref からは取れない
                idc["doi_resolved"] = True
                notes.append(f"DOI は {ag['agency']} 登録（Crossref の対象外）。doi.org で解決を確認（{ag['location']}）。license は未確認（source_class は現状維持）")
                rec = idconv(doi)
                self._reconcile(card, "pmid", rec.get("pmid") if rec else None, idc, notes, via=f"DOI {doi}")
                self._reconcile(card, "pmcid", rec.get("pmcid") if rec else None, idc, notes, via=f"DOI {doi}")
                return
            notes.append(f"Crossref で DOI {doi} が見つからない（登録機関：{ag['agency']}、doi.org での解決：{ag['resolves']}）")
            self.conflicts.append((cid, "doi", doi, "Crossref 404", "DOI が実在しない可能性"))
            return
        idc["doi_resolved"] = True
        bib = bib_from_crossref(w)
        ok, why = bib_matches_source(bib, p.get("source") or "")
        if not ok and doi.lower() in self.validated:
            ok = True
            notes.append(f"source は略記。同じ DOI を {self.validated[doi.lower()]} で書誌照合済み")
        if ok:
            self.validated.setdefault(doi.lower(), cid)
        if not ok:
            notes.append(f"Crossref の書誌と source が合わない：{why}（{bib['first_author']}, {bib['journal']} {bib['year']}）")
            self.conflicts.append((cid, "doi→書誌", doi, f"{bib['first_author']}; {bib['title'][:80]}; {bib['journal']} {bib['year']}", why))

        cls, url = classify_license(w.get("license") or [])
        idc["license_from_crossref"] = url
        if cls is None:
            notes.append("Crossrefに license の記載なし（source_class は現状維持）")
        elif cls != p.get("source_class"):
            self.class_diffs.append((cid, p.get("source_class"), cls, url))
            if domain in APPLY_LICENSE_CLASS:
                card["history"].append(h(f"source_class {p.get('source_class')} → {cls}（Crossref の license：{url}）"))
                p["source_class"] = cls

        rec = idconv(doi)
        api_pmid = rec.get("pmid") if rec else None
        api_pmcid = rec.get("pmcid") if rec else None
        if not api_pmid:
            hits = esearch_doi(doi)
            if len(hits) == 1:
                api_pmid = hits[0]
            elif len(hits) > 1:
                notes.append(f"esearch で PMID が複数（{', '.join(hits)}）。書き込まない")
        if api_pmid and not api_pmcid:
            rec2 = idconv(api_pmid)
            api_pmcid = rec2.get("pmcid") if rec2 else None
        self._reconcile(card, "pmid", api_pmid, idc, notes, via=f"DOI {doi}")
        self._reconcile(card, "pmcid", api_pmcid, idc, notes, via=f"DOI {doi}")
        if api_pmid is None:
            notes.append("PubMed に DOI の登録なし（PMID なし）")

    def _reconcile(self, card, key, api_value, idc, notes, via):
        p, cid = card["provenance"], card["id"]
        cur = p.get(key)
        if key == "pmid":
            if cur and api_value:
                idc["pmid_matched"] = (str(cur) == str(api_value))
            elif cur and not api_value:
                idc["pmid_matched"] = None
        if api_value is None:
            return
        if cur is None:
            p[key] = str(api_value)
            card["history"].append(h(f"{key} を {api_value} に設定（{via} から API で一意に確定）"))
            self.filled.append((cid, key, api_value, via))
            if key == "pmid":
                idc["pmid_matched"] = True
        elif str(cur) != str(api_value):
            self.conflicts.append((cid, key, cur, api_value, f"{via} から得た値と既存値が異なる。書き換えていない"))
            notes.append(f"{key} 食い違い：既存 {cur}／API {api_value}")

    # --- PMID だけのカード
    def _by_pmid(self, card, idc, notes):
        p, cid = card["provenance"], card["id"]
        doc = esummary(p["pmid"])
        if doc is None:
            notes.append(f"esummary で PMID {p['pmid']} が見つからない")
            self.conflicts.append((cid, "pmid", p["pmid"], "esummary なし", "PMID が実在しない可能性"))
            idc["pmid_matched"] = False
            return
        bib = bib_from_esummary(doc)
        ok, why = bib_matches_source(bib, p.get("source") or "")
        idc["pmid_matched"] = ok
        if not ok:
            notes.append(f"PubMed の書誌と source が合わない：{why}")
            self.conflicts.append((cid, "pmid→書誌", p["pmid"], f"{bib['first_author']}; {bib['title'][:80]}; {bib['short_journal']} {bib['year']}", why))
            return
        if bib.get("doi"):
            self._reconcile(card, "doi", bib["doi"], idc, notes, via=f"PMID {p['pmid']} の esummary")
            if p.get("doi") == bib["doi"]:
                # DOI が確定したので、Crossref でライセンスを確認する
                self._by_doi(card, bib["doi"], idc, notes, card["domain"])
                return
        if bib.get("pmc"):
            self._reconcile(card, "pmcid", bib["pmc"], idc, notes, via=f"PMID {p['pmid']} の esummary")

    # --- PMCID だけのカード
    def _by_pmcid(self, card, idc, notes):
        p, cid = card["provenance"], card["id"]
        rec = idconv(p["pmcid"])
        if rec is None:
            notes.append(f"idconv で {p['pmcid']} が見つからない")
            self.conflicts.append((cid, "pmcid", p["pmcid"], "idconv なし", "PMCID が実在しない可能性"))
            return
        if rec.get("pmid"):
            doc = esummary(rec["pmid"])
            bib = bib_from_esummary(doc) if doc else {}
            ok, why = bib_matches_source(bib, p.get("source") or "") if bib else (False, "esummary なし")
            if not ok and (rec.get("doi") or "").lower() in self.validated:
                ok = True
                notes.append(f"source は略記。同じ文献（DOI {rec['doi']}）を {self.validated[rec['doi'].lower()]} で書誌照合済み")
            if not ok:
                notes.append(f"PMCID {p['pmcid']} の書誌と source が合わない：{why}")
                self.conflicts.append((cid, "pmcid→書誌", p["pmcid"], f"{bib.get('first_author')}; {(bib.get('title') or '')[:80]}; {bib.get('short_journal')} {bib.get('year')}", why))
                return
            self._reconcile(card, "pmid", rec["pmid"], idc, notes, via=f"PMCID {p['pmcid']}")
        if rec.get("doi"):
            self._reconcile(card, "doi", rec["doi"], idc, notes, via=f"PMCID {p['pmcid']}")
            if p.get("doi") == rec["doi"]:
                self._by_doi(card, rec["doi"], idc, notes, card["domain"])

    # --- 識別子のないカード
    def _no_ids(self, card, notes):
        p = card["provenance"]
        src = p.get("source") or ""
        if p.get("source_class") in ("GOV_JP", "GOV_US") or not re.search(r"[A-Za-z]{3,}", src) or "一次出典未取得" in src:
            notes.append("識別子なし（公的資料・企業資料・和文資料、または出典未取得）。Crossref 検索の対象外")
            return
        items = crossref_search(src)
        for it in items[:3]:
            issued = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
            self.candidates.append({
                "id": card["id"], "source": src, "candidate_doi": it.get("DOI"),
                "title": (it.get("title") or [""])[0], "journal": (it.get("container-title") or [""])[0],
                "year": issued, "first_author": ((it.get("author") or [{}])[0]).get("family"),
                "crossref_score": it.get("score"), "approved": "",
            })
        notes.append(f"識別子なし。Crossref の候補 {len(items[:3])} 件を proposals/id_candidates.csv に出力")


def main(prefixes: list[str]) -> None:
    files = sorted(FACTS.glob("*.yaml"))
    files = [f for f in files if not f.name.startswith("_") and (not prefixes or f.stem in prefixes)]
    ck = Checker()
    for f in files:
        cards = yaml.safe_load(f.read_text(encoding="utf-8"))
        for c in cards:
            if c["publication_info"]["status"] == "retired":
                continue
            ck.check(c, f.stem)
        f.write_text(yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000), encoding="utf-8", newline="\n")
        print(f"{f.name}: checked")
    write_outputs(ck, [f.stem for f in files])


def write_outputs(ck: Checker, domains: list[str]) -> None:
    tag = "_".join(domains)
    L = [f"# Phase 3：識別子とライセンスの照合（{TODAY}、対象 {', '.join(domains)}）\n",
         "生成：`scripts/verify_ids.py`。API 応答は `.cache/`（git 管理外）。\n",
         "## 1. 概要\n",
         f"- 照合したカード：{len(ck.summary)} 件（retired を除く）",
         f"- DOI を Crossref で解決：{sum(1 for s in ck.summary if s['doi_resolved'])} 件",
         f"- 識別子を API で補完：{len(ck.filled)} 件",
         f"- 食い違い：{len(ck.conflicts)} 件",
         f"- source_class の判定差：{len(ck.class_diffs)} 件",
         f"- unresolved（API 失敗）：{len(ck.unresolved)} 件",
         f"- 識別子なしで候補を出したもの：{len({c['id'] for c in ck.candidates})} 件\n",
         "## 2. 食い違い（書き換えていない）\n",
         "| ID | 項目 | 既存値 | API の値 | 内容 |", "|---|---|---|---|---|"]
    L += [f"| {a} | {b} | {c} | {d} | {e} |" for a, b, c, d, e in ck.conflicts] or ["| — | | | | なし |"]
    L += ["\n## 3. source_class の判定差\n", "| ID | 既存 | Crossref の判定 | license URL |", "|---|---|---|---|"]
    L += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in ck.class_diffs] or ["| — | | | なし |"]
    L.append("\nES・GD・IN は人間の委任により判定値を反映済み。HP・UG はレポートのみ。\n")
    L += ["## 4. API で補完した識別子\n", "| ID | 項目 | 値 | 経路 |", "|---|---|---|---|"]
    L += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in ck.filled] or ["| — | | | なし |"]
    L += ["\n## 5. unresolved\n"]
    L += [f"- {a}: {b}" for a, b in ck.unresolved] or ["なし"]
    L += ["\n## 6. カードごとの結果\n", "| ID | DOI解決 | PMID一致 | license | notes |", "|---|---|---|---|---|"]
    for s in ck.summary:
        L.append(f"| {s['id']} | {s['doi_resolved']} | {s['pmid_matched']} | {s['license_from_crossref'] or '—'} | {(s['notes'] or '').replace('|', '／')} |")
    (REPORTS / f"03_id_check_{tag}.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    if ck.candidates:
        with (PROPOSALS / f"id_candidates_{tag}.csv").open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(ck.candidates[0].keys()))
            w.writeheader()
            w.writerows(ck.candidates)


if __name__ == "__main__":
    main(sys.argv[1:])
