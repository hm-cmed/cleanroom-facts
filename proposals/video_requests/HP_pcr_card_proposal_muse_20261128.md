# カード追加の提案：PCRによるクラリスロマイシン耐性検査（PYLO_001 の締め対応）

作成：2026-11-28（Muse）
位置づけ：レポジトリ側の検査・登録を受ける前の提案。カード番号・SRC番号は仮で、確定はレポジトリ側。

## 1. 背景

- PYLO_001 v2 の締めは「除菌では、菌の薬剤感受性を意識しましょう。」にとどめた。ユーザーの希望は「感受性が確認できるピロリ菌の PCR 検査の活用」まで踏み込むことだが、現行カード HP-001〜006 に PCR・耐性遺伝子検査の記載がなく、裏づけなしには入れられない。
- そこで、PCR によるクラリスロマイシン（CAM）耐性変異の検出と、それに基づくテーラーメイド除菌を扱うカードを1枚追加する提案を作る。追加が登録されれば、動画の締めを PCR に触れる形へ差し替えられる。

## 2. 追加カード案（仮番号 HP-010）

- assertion（自分の言葉で構成。出典の定義文・結論文の転用なし）：
  「クラリスロマイシン耐性は 23S rRNA 遺伝子の点変異と関連しており、PCR でこの変異を検出して耐性の有無を推定できる。変異の有無に応じてレジメンを選ぶテーラーメイド除菌は、通常の三剤療法より除菌率が高かった（無作為化試験で 91.2% 対 75.9%）。」
- region・対象：HP 系の既存カードに合わせる（登録時にレポジトリ側と確認）。
- uncertainty に書くこと：
  - 日本の小規模な無作為化試験（Kawai 2008、70例）では、便から抽出した DNA の PCR で変異を調べ感受性に合わせて選んだ群の除菌率が 94.3%、対照群が 71.4% だった。便検体の PCR による変異検出の精度は、培養感受性検査を基準として感度 80%・特異度 84.8% との報告がある（Osaki 2017）。
  - 国内の保険診療で算定できるピロリ菌の検査項目には核酸増幅法があり、胃液を検体として CAM 耐性遺伝子変異も検出できるとされる（この点は診療報酬上の一次資料での確認が登録時の宿題）。
  - 主出典は韓国の試験であり、レジメン・耐性率は日本の現行診療と異なる部分がある。

## 3. 出典表（案）

| SRC | 出典 | DOI | PMID | ライセンス表示 | legal_basis | source_class | 使うカード |
|---|---|---|---|---|---|---|---|
| （新規・仮） | Lee HJ, Kim JI, Cheung DY, et al. Eradication of Helicobacter pylori according to 23S ribosomal RNA point mutations associated with clarithromycin resistance. J Infect Dis. 2013;208(7):1123-1130 | 10.1093/infdis/jit287 | 23801607 | All rights reserved（OUP） | B | RESTRICTED | HP-010（主出典） |
| （新規・仮） | Kawai T, Yamagishi T, Yagi K, et al. Tailored eradication therapy based on fecal Helicobacter pylori clarithromycin sensitivities. J Gastroenterol Hepatol. 2008;23 Suppl 2:S171-S174 | 10.1111/j.1440-1746.2008.05408.x | （未確認） | All rights reserved（Wiley） | B | RESTRICTED | HP-010（裏づけ） |
| （新規・仮） | Osaki T, Mabe K, Zaman C, et al. Usefulness of detection of clarithromycin-resistant Helicobacter pylori from fecal specimens for young adults treated with eradication therapy. Helicobacter. 2017;22(5):e12396 | 10.1111/hel.12396 | 28544222 | All rights reserved（Wiley） | B | RESTRICTED | HP-010（裏づけ） |

## 4. 検証メモ（2026-11-28、Muse が原典側で確認した範囲）

- Lee 2013：OUP の抄録ページで方法・結果を確認（対象1,232人、テーラーメイド群の除菌率 91.2%（176/193）、対照 APC 75.9%・APM 79.1%、いずれも P<.001、試験登録 NCT0145303）。DOI・PMID は KoreaMed Synapse の引用表記で照合。
- Kawai 2008：論文 PDF（J Gastroenterol Hepatol 誌面）で確認（70例を無作為割付、便 DNA の nested PCR＋シークエンスで A2143G・A2144G を検出、除菌率 94.3% 対 71.4%、CAM 耐性株ではテーラーメイド群 100%）。DOI は誌面と引用文献で一致。**PMID は未確認のため空欄。登録時に --online 照合で確定すること。**
- Osaki 2017：PubMed 抄録で確認（PMID 28544222、DOI 10.1111/hel.12396、便 DNA の変異検出は感度 80%・特異度 84.8%）。
- 既存マスター・前回納品分との DOI・PMID 重複は、本案の作成時点では未照合（レポジトリ側の取り込み検査で確認する前提）。

## 5. 登録された場合の動画側の変更

- PYLO_001 の締め（場面9）を、例えば「除菌では薬剤感受性を意識しましょう。PCR で耐性を確認できる検査もあります。」の方向に差し替えた v3 を作る（文言は登録されたカードの範囲で最終調整）。
- 場面4・8 の感受性試験イラスト（sustest）はそのまま使える。必要なら PCR のイラスト追加を検討する。
