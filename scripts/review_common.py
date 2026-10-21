"""GitHub での監修に使う共通の部品（カードの版の計算、Issue フォームの読み取り）。"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "data" / "facts"
REPO = os.environ.get("GITHUB_REPOSITORY") or "hm-cmed/cleanroom-facts"
NO_RESPONSE = "_No response_"


def card_hash(card: dict) -> str:
    """監修の対象になる内容（主張文・条件・誤解・不確実性・出典・カリキュラム）から作る版の印（10文字）。
    この印が変わったら、監修後に内容が変わったことを意味する。"""
    p = card.get("provenance") or {}
    body = {
        "assertion": card.get("assertion"),
        "uncertainty": card.get("uncertainty"),
        "source": [p.get("source"), p.get("doi"), p.get("pmid"), p.get("url")],
        "curriculum": card.get("curriculum"),
    }
    text = json.dumps(body, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:10]


def load_domains() -> dict[str, dict]:
    path = ROOT / "data" / "domains.yaml"
    if not path.exists():
        return {}
    return {d["prefix"]: d for d in yaml.safe_load(path.read_text(encoding="utf-8")) or []}


def load_all() -> dict[str, list[dict]]:
    """接頭辞ごとのカード一覧（data/facts/<接頭辞>.yaml）。"""
    out: dict[str, list[dict]] = {}
    for path in sorted(FACTS.glob("*.yaml")):
        if path.name.startswith("_"):
            continue
        out[path.stem] = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    return out


def dump(prefix: str, cards: list[dict]) -> None:
    text = yaml.safe_dump(cards, allow_unicode=True, sort_keys=False, width=10_000, default_flow_style=False)
    (FACTS / f"{prefix}.yaml").write_text(text, encoding="utf-8", newline="\n")


def needs_review(card: dict) -> bool:
    pub = card.get("publication_info") or {}
    if pub.get("status") == "retired":
        return False
    if pub.get("status") != "verified_expert":
        return True
    return bool(pub.get("verified_hash")) and pub.get("verified_hash") != card_hash(card)


def parse_form(body: str) -> dict[str, str]:
    """Issue フォームの本文（### 見出し + 値）を {見出し: 値} にする。"""
    out: dict[str, str] = {}
    label = None
    buf: list[str] = []
    for line in (body or "").replace("\r\n", "\n").split("\n"):
        m = re.match(r"^###\s+(.+?)\s*$", line)
        if m:
            if label is not None:
                out[label] = "\n".join(buf).strip()
            label, buf = m.group(1), []
        elif label is not None:
            buf.append(line)
    if label is not None:
        out[label] = "\n".join(buf).strip()
    return {k: ("" if v == NO_RESPONSE else v) for k, v in out.items()}
