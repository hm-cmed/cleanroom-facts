"""受け入れ検査：調査の成果物（raw の Markdown）1つを、取り込む前に検査し、「合格」か「差し戻し」かを出す。

使い方（リポジトリ直下で。成果物はレポジトリの外に置いたままでよい）:
    python scripts/accept_round.py C:\\Users\\...\\Downloads\\15_ku_a.md --spec docs/tasks/round15_KU.yaml
    python scripts/accept_round.py ... --online     # DOI・PMID・ライセンスも Crossref・NCBI で照合（PC で実行）

- 検査の中身は scripts/eval_trial.py と同じ（形式・スキーマ・ID と SRC 番号・カリキュラム・網羅・重複）。
  加えて、試行（第14回）で見つかった弱点を検査する：
  1. 薬の名前があるカードに、国内の承認・保険適用の確認状況が書かれていない
  2. 論文なのに DOI が空の出典
  3. ライセンスを UNKNOWN のままにした出典の割合
- 結果は reports/accept_<成果物の名前>.md。差し戻すときは、その「差し戻しの内容」をそのまま作り手に渡せばよい。
- データ（data/）には書き込まない。
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eval_trial import ROOT, evaluate, load_reference, online, parse  # noqa: E402
from ingest_round import null_if_dash  # noqa: E402

DRUG = re.compile(r"(マブ|ニブ|チニブ|リズマブ|シマブ|ナビル|プラチン|タキセル|ゾラミド|サルタン|プリル|スタチン|グリフロジン|グリプチン|"
                  r"ペニシリン|セフ[ァ-ヶー]+|マイシン|サイクリン|フロキサシン|コナゾール|インスリン|"
                  r"ワルファリン|ヘパリン|キサバン|ガトラン|アスピリン|クロピドグレル|[A-Za-z]+mab\b|[A-Za-z]+nib\b)")
APPROVAL = re.compile(r"承認|保険適用|保険適応|適応外|薬価|添付文書|効能")
NOT_ARTICLE = re.compile(r"(厚生労働省|消防庁|環境省|国立がん研究センター|CDC|Centers for Disease|NIH|NCI|National Cancer|ATSDR|"
                         r"WHO|World Health|PDQ|MeSH|統計|白書|通知|告示|法律|ウェブ|Web|ページ|サイト)", re.I)


def extra_checks(p: dict) -> dict:
    cards = [c for c in p["cards"] if isinstance(c, dict)]
    drug_no_note = [c.get("id") for c in cards
                    if DRUG.search(c.get("assertion", {}).get("plain_statement_ja", ""))
                    and not APPROVAL.search(str(c.get("uncertainty") or ""))
                    and not APPROVAL.search(c.get("assertion", {}).get("plain_statement_ja", ""))]
    no_doi = [f"{r['SRC']}（{(r.get('出典') or '')[:40]}…）" for r in p["srcs"]
              if not null_if_dash(r.get("DOI")) and not NOT_ARTICLE.search(r.get("出典") or "")]
    unknown = sum(1 for r in p["srcs"] if (r.get("source_class") or "").strip() == "UNKNOWN")
    return {"drug_no_note": drug_no_note, "no_doi": no_doi, "unknown": unknown, "n_src": len(p["srcs"])}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("raw")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--online", action="store_true")
    args = ap.parse_args()
    spec = yaml.safe_load(Path(args.spec).read_text(encoding="utf-8"))
    spec.setdefault("topics", [])
    spec.setdefault("target_cards", [1, 999])
    ref = load_reference()
    p = parse(Path(args.raw))
    m = evaluate("raw", p, spec, ref)
    x = extra_checks(p)
    o = online("raw", p, []) if args.online else None

    must: list[str] = []      # 直さないと取り込めない
    should: list[str] = []    # 取り込めるが、直してほしい
    if p["parse_error"] or m["issues"]:
        must += m["issues"] or [p["parse_error"]]
    if m["schema_bad"]:
        must.append(f"スキーマに合わないカード：{'、'.join(map(str, m['schema_bad']))}")
    if m["status_bad"]:
        must.append(f"status が draft でない、または verifier に値がある：{'、'.join(m['status_bad'])}")
    if m["paren_bad"]:
        must.append(f"主張文に（要確認）などの括弧書き：{'、'.join(m['paren_bad'])}。不確かな点は uncertainty に書く")
    if m["id_bad"] or m["id_dup"] or m["id_gaps"]:
        must.append(f"ID が指定と違う（範囲外 {m['id_bad']}、重複 {m['id_dup']}、欠番 {m['id_gaps']}）。欠番は理由を一覧にする")
    if m["src_out_of_range"] or m["src_missing"]:
        must.append(f"SRC 番号が指定の範囲外 {m['src_out_of_range']}、または出典表にない {m['src_missing']}")
    if m["src_dup_doi"]:
        must.append(f"既存の出典と同じ文献に新しい番号を付けた：{'、'.join(m['src_dup_doi'])}。既存の番号を再利用する")
    if m["kok_bad"] or m["core_bad"]:
        must.append(f"出題基準の番号の誤り {m['kok_bad']} 件、コアカリの番号・id の誤り：{'、'.join(m['core_bad'])}")
    miss_a = [f"{t['code']} {t['name']}" for t in spec["targets"]
              if t.get("level") == "a" and f"{t['code']} {t['name']}" in m["targets_miss"]]
    if m["targets_miss"]:
        (must if miss_a else should).append(f"カードがない対象の小項目：{'、'.join(m['targets_miss'])}")
    if m["near_dup"]:
        should.append(f"既存カードとほぼ同じ内容：{'、'.join(m['near_dup'])}")
    if x["drug_no_note"]:
        should.append(f"薬の名前があるのに、国内の承認・保険適用の確認状況が uncertainty にない：{'、'.join(map(str, x['drug_no_note']))}")
    if x["no_doi"]:
        should.append(f"論文と思われるのに DOI が空の出典：{'、'.join(x['no_doi'])}。DOI があれば書く（PMID も）")
    if x["n_src"] and x["unknown"] / x["n_src"] > 0.3:
        should.append(f"ライセンスが UNKNOWN の出典が {x['unknown']}/{x['n_src']} 件。Crossref の license 欄や出版社ページで CC BY と確認できれば OPEN にする")
    if o:
        if o["doi_ng"]:
            must.append(f"Crossref で見つからない DOI：{'、'.join(o['doi_ng'])}")
        if o["pmid_ng"]:
            must.append(f"PMID の問題：{'、'.join(o['pmid_ng'])}")
        if o["title_low"]:
            should.append(f"DOI の題名が出典表と食い違う：{'、'.join(o['title_low'])}")
        if o["lic_disagree"]:
            should.append(f"ライセンス判定が Crossref と違う：{'、'.join(o['lic_disagree'])}")

    verdict = "差し戻し" if must else "合格"
    name = Path(args.raw).stem
    L = [f"# 受け入れ検査：{name}（{dt.date.today().isoformat()}）", "",
         f"- 判定：**{verdict}**（必須の修正 {len(must)} 件、望ましい修正 {len(should)} 件）",
         f"- カード {m['n']} 件、出典 {m['n_src']} 件（DOI あり {m['src_doi']}、PMID あり {m['src_pmid']}）、"
         f"対象小項目 {len(m['targets_hit'])}/{len(spec['targets'])}、"
         f"uncertainty の記載 {m['unc']}/{m['n']}、地域の記載 {m['region']}/{m['n']}",
         f"- 照合：{'Crossref・NCBI で照合済み' if o else '未実施（PC で --online を付けて実行する）'}", ""]
    L += ["## 差し戻しの内容（作り手にそのまま渡せる）", ""]
    if must or should:
        L += ["次の点を直して、成果物全体をもう一度出してください。ID と SRC 番号は変えないでください。", ""]
        L += ["**必須**", ""] + [f"{i}. {s}" for i, s in enumerate(must, 1)] + [""] if must else []
        L += ["**できれば**", ""] + [f"{i}. {s}" for i, s in enumerate(should, 1)] + [""] if should else []
    else:
        L += ["なし。", ""]
    L += ["## 取り込み", "",
          "合格なら、成果物を `raw/` に置き、`python scripts/ingest_round.py raw/<名前>.md <接頭辞> [--append]` で取り込む。"
          "「できれば」の項目は、取り込み後に Claude Code が照合（`scripts/ncbi_crossref.py`）や補完回で対応してもよい。"]
    out = ROOT / "reports" / f"accept_{name}.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"判定：{verdict} → {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
