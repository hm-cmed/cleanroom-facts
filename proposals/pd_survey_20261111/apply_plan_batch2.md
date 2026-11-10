# パブリックドメイン出典の裏づけ調査 バッチ2（BA・IL・VI）の取り込み側の照合（2026-11-11）

作り手の結果：`batch2_infectious.md`（A65・B32・C1・D4、102件）。カードはまだ変えていない。

## 1. 使わないもの
- A65件はすべて PubMed の抄録が根拠。抄録は出版社・著者の著作物で、同じ論文の抄録は独立した裏づけにもならない（バッチ1・BL 等と同じ判断）。→ 置き換え・裏づけとも使わない。
- B のうち抄録だけが根拠のもの、MedlinePlus 医学百科（BA-031）も同様に使わない。
- 兵庫県の公式サイト（VI-026）：都道府県のサイトは各自治体の利用規約による（政府標準利用規約とは限らない）。規約を確認するまで GOV_JP にしない。

## 2. 区分の訂正（D）4件：要確認のうえ反映
- SRC-435（ARDS 診療ガイドライン2021、J Intensive Care。IL-041〜043）：UNKNOWN → OPEN（CC BY 4.0）。BMC 系の雑誌で、作り手が PMC の表示を確認。PMID 35799288・PMCID PMC9263056 も補完候補。
- SRC-2027（JJID 2024、VI-018）：UNKNOWN → OPEN（CC BY）。作り手は投稿規程の明記を確認したとするが、取り込み側では J-STAGE の誌情報に「FREE ACCESS」の表示しか確認できなかった（無料公開は CC BY と同じではない）。投稿規程の原文 URL を作り手に求めてから反映する。
- 区分の明確化（UNKNOWN → RESTRICTED、自由化ではない）：SRC-424（CC BY-NC）、SRC-426（CC BY-NC）。

## 3. 裏づけ（B）として使える候補（政府資料・CC BY）
- ClinicalTrials.gov の結果登録：IL-007（INPULSIS）、IL-008（ASCEND）、IL-009（FIBRONEER-IPF）、IL-012（INBUILD）、IL-013（SENSCIS）、VI-027（NCT00466817）。数値の一致を記録する。
- CDC：BA-046（Emerg Infect Dis 2011、Ohnishi）、BA-047（NHSN の血流感染の定義）、VI-021（About Norovirus。潜伏期はカード 10〜51時間、CDC 12〜48時間で不一致。合う部分だけ記録）、VI-033（About Viral Meningitis、米国前提の記載）
- NHLBI：IL-019・020・022（定性的な部分のみ）
- EPA 農薬中毒マニュアル：IL-055
- 厚労省の薬価基準・中医協資料：VI-006（収載日と薬価）
- CC BY 論文：IL-018・021（J Clin Med 2023）、IL-001（Histopathology 2026 レビュー）

## 4. 識別子の補完候補（--online で照合してから入れる）
- IL-001・007・008・012〜017・019・023〜027・029〜032・038〜047・057・059・062 の PMID（一部 DOI・PMCID）、BA-003・IL-002〜006・IL-023・VI-001・VI-005 の PMCID、IL-015（SRC-421）の DOI・PMID。
- IL-062 は uncertainty に「PMID は確認できなかった」とあり、照合後に uncertainty も直す。
- SRC-538 の PMCID 未登録と著者順の不一致も、照合後に直す。
