"""Crossref・NCBI の問い合わせ（応答は .cache/ に JSON で保存し、同じ問い合わせを繰り返さない）。"""
from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache"
load_dotenv(ROOT / ".env")
EMAIL = os.environ.get("CONTACT_EMAIL", "")
NCBI_KEY = os.environ.get("NCBI_API_KEY", "")
TOOL = "cleanroom-facts"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
IDCONV = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"

_last_call: dict[str, float] = {}
_INTERVAL = {"ncbi": 0.11 if NCBI_KEY else 0.34, "crossref": 0.1, "doi": 0.2}


class Unresolved(Exception):
    """API の失敗・タイムアウト。値は推測で埋めず、レポートに unresolved として残す。"""


def _cached_get(kind: str, url: str, params: dict) -> dict | None:
    key_src = url + "?" + "&".join(f"{k}={v}" for k, v in sorted(params.items()) if k not in ("api_key", "email", "mailto", "tool"))
    path = CACHE / kind / (hashlib.sha1(key_src.encode()).hexdigest() + ".json")
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    wait = _INTERVAL[kind] - (time.time() - _last_call.get(kind, 0))
    if wait > 0:
        time.sleep(wait)
    for attempt in range(3):
        try:
            r = requests.get(url, params=params, timeout=30)
            _last_call[kind] = time.time()
            if r.status_code == 404:
                data = {"_status": 404}
                break
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            r.raise_for_status()
            data = r.json()
            break
        except (requests.RequestException, ValueError) as e:
            if attempt == 2:
                raise Unresolved(f"{url}: {e}") from e
            time.sleep(2 ** attempt)
    else:
        raise Unresolved(f"{url}: 再試行の上限")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"_query": key_src, **data} if isinstance(data, dict) else data, ensure_ascii=False), encoding="utf-8")
    return data


def _ncbi_params(extra: dict) -> dict:
    p = {"tool": TOOL, "email": EMAIL, **extra}
    if NCBI_KEY:
        p["api_key"] = NCBI_KEY
    return p


def crossref_work(doi: str) -> dict | None:
    data = _cached_get("crossref", f"https://api.crossref.org/works/{doi}", {"mailto": EMAIL})
    if data.get("_status") == 404:
        return None
    return data.get("message")


def doi_agency(doi: str) -> dict:
    """Crossref にない DOI の登録機関（JaLC・DataCite など）と、doi.org で解決できるかを返す。"""
    prefix = doi.split("/")[0]
    ra = _cached_get("doi", f"https://doi.org/ra/{prefix}", {})
    agency = ra[0].get("RA") if isinstance(ra, list) and ra else (ra.get("RA") if isinstance(ra, dict) else None)
    path = CACHE / "doi" / (hashlib.sha1(f"resolve:{doi}".encode()).hexdigest() + ".json")
    if path.exists():
        res = json.loads(path.read_text(encoding="utf-8"))
    else:
        try:
            r = requests.head(f"https://doi.org/{doi}", allow_redirects=False, timeout=30)
            res = {"status": r.status_code, "location": r.headers.get("Location")}
        except requests.RequestException as e:
            raise Unresolved(f"doi.org {doi}: {e}") from e
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(res), encoding="utf-8")
    return {"agency": agency, "resolves": res["status"] in (301, 302, 303, 307, 308), "location": res.get("location")}


def crossref_search(bibliographic: str, rows: int = 3) -> list[dict]:
    data = _cached_get("crossref", "https://api.crossref.org/works",
                       {"query.bibliographic": bibliographic, "rows": rows, "mailto": EMAIL,
                        "select": "DOI,title,container-title,issued,author,score"})
    return (data.get("message") or {}).get("items", [])


def idconv(ident: str) -> dict | None:
    data = _cached_get("ncbi", IDCONV, _ncbi_params({"ids": ident, "format": "json"}))
    recs = data.get("records") or []
    if not recs or recs[0].get("status") == "error":
        return None
    return recs[0]


def esearch_doi(doi: str) -> list[str]:
    data = _cached_get("ncbi", f"{EUTILS}/esearch.fcgi", _ncbi_params({"db": "pubmed", "term": f'"{doi}"[doi]', "retmode": "json"}))
    return (data.get("esearchresult") or {}).get("idlist", [])


def esearch(term: str, retmax: int = 5) -> list[str]:
    data = _cached_get("ncbi", f"{EUTILS}/esearch.fcgi", _ncbi_params({"db": "pubmed", "term": term, "retmode": "json", "retmax": retmax}))
    return (data.get("esearchresult") or {}).get("idlist", [])


def esummary(pmid: str) -> dict | None:
    data = _cached_get("ncbi", f"{EUTILS}/esummary.fcgi", _ncbi_params({"db": "pubmed", "id": pmid, "retmode": "json"}))
    res = data.get("result") or {}
    doc = res.get(str(pmid))
    if not doc or doc.get("error"):
        return None
    return doc
