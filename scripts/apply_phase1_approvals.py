"""Phase 1 の取り込み後に人間が承認した変更を、staging ファイルに反映する。

承認内容（2026-10-12、チャットで人間が承認）:
  1. proposals/01_inline_citation_markers.md：主張文内の脚注マーカーを削除する（ES-029、ES-064）
  2. v2 で status: verified_sources だったカードを draft に戻す（Phase 3 の API 照合後に再判定）

extract_yaml.py を再実行した場合は、このスクリプトも続けて実行すること。何度実行しても結果は同じ。
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "data" / "facts"
APPROVED_ON = "2026-10-12"
BY = "claude-code"

MARKER_IDS = {"ES-029", "ES-064"}
MARKER_RE = re.compile(r"(\[\d+\])+")


def load(name):
    return yaml.safe_load((FACTS / name).read_text(encoding="utf-8"))


def dump(name, data):
    text = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=10_000, default_flow_style=False)
    (FACTS / name).write_text(text, encoding="utf-8", newline="\n")


def main():
    v1 = load("_staging_ES_v1.yaml")
    n1 = 0
    for c in v1:
        if c["id"] not in MARKER_IDS:
            continue
        before = c["assertion"]["plain_statement_ja"]
        after = MARKER_RE.sub("", before)
        if after != before:
            refs = "".join(re.findall(r"\[\d+\]", before))
            c["assertion"]["plain_statement_ja"] = after
            c["history"].append({"date": APPROVED_ON, "by": BY,
                                 "change": f"主張文内の脚注マーカー {refs} を削除（proposals/01_inline_citation_markers.md、人間が {APPROVED_ON} に承認）"})
            n1 += 1
    dump("_staging_ES_v1.yaml", v1)

    v2 = load("_staging_ES_v2.yaml")
    n2 = 0
    for c in v2:
        if c["publication_info"]["status"] == "verified_sources":
            c["publication_info"]["status"] = "draft"
            c["history"].append({"date": APPROVED_ON, "by": BY,
                                 "change": f"status verified_sources → draft（原本の値は claude.ai 調査ラウンドの判定で、本リポジトリのAPI照合が未実施のため。Phase 3 で再判定。人間が {APPROVED_ON} に承認）"})
            n2 += 1
    dump("_staging_ES_v2.yaml", v2)
    print(f"markers removed: {n1}, status reverted: {n2}")


if __name__ == "__main__":
    main()
