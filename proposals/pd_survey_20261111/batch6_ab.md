# パブリックドメイン出典の棚卸し バッチ6（AB 79件）

- 作成日：2026-11-11
- 対象：AB 章 79 件（targets.json 掲載分：AB-001〜054、069〜074、082、083、087〜093、097、099〜104、106、116、119）
- 方法：各カードの主出典について Crossref・Europe PMC・PubMed の API／実際に開いたページでライセンスと識別子を確認し、米国政府資料（MedlinePlus・FDA ラベル・ACOG 意見書）と CC BY の一次資料（WSES 系ガイドライン等）から置き換え・裏づけ候補を照合した。**主張文と数値は変更していない。**
- 判定の見方：**A 置き換え可**＝自由に使える出典だけで主張（数値含む）を裏づけられる／**B 裏づけ追加**＝自由な資料で部分的に裏づけられる／**C 見つからない**／**D 区分の訂正**＝主出典自体が実は自由な区分。PubMed 抄録レコードに全数値・全要素が載ることによる A は「先例に基づく A」として印を付け、集計で分けて数える。

## 集計

| 判定 | 件数 | 内訳・メモ |
|---|---|---|
| A 置き換え可 | 3 | うち先例に基づく A 3（AB-072・073・099）／先例以外の A 0 |
| B 裏づけ追加 | 31 | |
| C 見つからない | 45 | うち40件が日本の急性腹症診療ガイドライン2025（書籍）固有の整理・CQ回答 |
| D 区分の訂正 | 0 | CC BY の英語版ガイドライン相当の事例は本バッチではなし（後述） |
| 計 | 79 | |

## 重要な発見

1. **英語版ガイドラインの CC BY パターンは本バッチでは不発**：対象の主出典のうち英語版の国際誌ガイドラインは HerniaSurge（SRC-158）と WSACS 合意文書（SRC-160）で、いずれも Crossref の version-of-record ライセンスと Europe PMC の表示の両方で **CC BY-NC** であり、現行の RESTRICTED が正しい（D には当たらない）。急性腹症診療ガイドライン2025の英語版はそもそも未刊行（2015年英語版は非オープンアクセス）であり、バッチ5のような UNKNOWN→OPEN の訂正候補は AB にはなかった。
2. **WSES の CC BY ガイドラインが腹壁ヘルニア7件（AB-087〜093）の強い裏づけになる**：現出典 SRC-162 は WSES ガイドラインの2020年要約版（Hernia 誌、自由でない）だが、その本体である「2017 update of the WSES guidelines for emergency repair of complicated abdominal wall hernias」（World J Emerg Surg、CC BY、PMID 28804507、PMCID PMC5545868）は推奨文とグレードがほぼ同一で、PMC 全文で直接照合できた。裏づけ出典としての新規登録を提案する（既存の出典マスターにはない）。
3. **識別子の補完候補が多数**：原典の PMID 等がマスター未登録のものが10出典分見つかった（SRC-158：PMID 29330835・PMCID PMC5809582／SRC-160：PMID 23673399・PMCID PMC3680657／SRC-162：PMID 31407109／SRC-4237：PMID 29746229／SRC-4238：PMID 32209311／SRC-4239：PMID 32199769／SRC-4240：PMID 34303806／SRC-4241：PMID 34016826／SRC-4243：PMID 31791596／SRC-4441：PMCID PMC9257997）。いずれも Europe PMC で実在を確認済み。**識別子自体の誤りは本バッチでは見つからなかった。**
4. **SRC-154（急性腹症ガイドライン2025書籍）の ISBN 未登録**：978-4-260-05773-8（NDL・日本超音波医学会掲載の前付けで確認）の補完を提案する。
5. **数値の不一致は検出されず**、確認できた数値は全て一致した（代表例 AB-099 PHOENIX-GC：登録183例、全生存期間中央値 17.7か月対15.2か月、抄録と一致）。枠組みの差として2件を両値記録した：AB-044（メトホルミン休薬：カード「検査後48時間休薬」／FDA ラベル「造影時に中止し48時間後に腎機能を再評価して再開」）、AB-045（妊婦の放射線：カード「50〜100 mGy 以下なら影響なし」／ACOG 本文の枠組み「50 mGy 未満ではリスク増加と関連しない」）。
6. **抄録に数値がないために A/B に届かない件が目立つ**：AB-069・071・074・082・083・104・119 は、主張の数値（生涯発生率、手術移行率、合併症率・死亡率、腹腔内圧の定義値、軸捻転の部位割合、大腿ヘルニアの割合）が原典の本文のみにあり、抄録レコードでは裏づけられない。数値自体は原典本文の値で、古さや改訂の問題ではない。改訂・基準変更の兆候（サーベイランス申し送り）も本バッチでは検出されなかった。

## A. 置き換え可（3件、全て先例に基づく）

全件、PubMed 抄録レコード（米国国立医学図書館のレコード）に主張の全要素が収載されていることによる A。この先例を認めない運用では3件とも B に移る。

| カード | 候補出典（識別子） | 裏づけの範囲・数値の照合 | 備考 |
|---|---|---|---|
| AB-072 | HerniaSurge Group. International guidelines for groin hernia management. Hernia. 2018;22:1-165（当該ガイドライン論文）の PubMed 抄録レコード（DOI 10.1007/s10029-017-1668-x／PMID 29330835／PMCID PMC5809582） | 主張全体：メッシュ修復が第1選択（開腹でも腹腔鏡・内視鏡下でもよい）、資源と技術があれば腹腔鏡・内視鏡下は回復が早く慢性疼痛リスクが低く費用対効果もよい、の全てが抄録に明記されている | 先例に基づく A（PubMed 抄録レコードに主張の全要素が載るケース）。抄録を置き換え出典と認めない運用では B に回る |
| AB-073 | HerniaSurge Group. International guidelines for groin hernia management. Hernia. 2018;22:1-165（当該ガイドライン論文）の PubMed 抄録レコード（DOI 10.1007/s10029-017-1668-x／PMID 29330835／PMCID PMC5809582） | 主張全体：嵌頓・絞扼の危険因子（女性、大腿ヘルニア、鼠径部ヘルニアによる入院歴）と、大腿ヘルニアには技術があれば腹腔鏡・内視鏡下メッシュ修復を時機を逃さず行う提案、の全てが抄録に明記されている | 先例に基づく A（PubMed 抄録レコードに主張の全要素が載るケース）。抄録を置き換え出典と認めない運用では B に回る |
| AB-099 | Ishigami H, et al. Phase III trial comparing intraperitoneal and intravenous paclitaxel plus S-1 versus cisplatin plus S-1 in patients with gastric cancer with peritoneal metastasis (PHOENIX-GC). J Clin Oncol. 2018;36:1922-1929（当該論文）の PubMed 抄録レコード（DOI 10.1200/JCO.2018.77.8613／PMID 29746229） | 一致（登録183例、全生存期間中央値 17.7か月対15.2か月、ハザード比0.72、層別 log-rank P=.080 で優越性は示されなかったことが抄録に収載） | 先例に基づく A（PubMed 抄録レコードに主張の全要素が載るケース）。抄録を置き換え出典と認めない運用では B に回る。あわせて原典 SRC-4237 の PMID（29746229）はマスター未登録のため補完を提案する |

## B. 裏づけ追加（31件）

| カード | 候補出典（識別子） | 裏づけの範囲・数値の照合 | 備考 |
|---|---|---|---|
| AB-004 | Naveed M, et al. American Society for Gastrointestinal Endoscopy guideline on the role of endoscopy in the management of acute colonic pseudo-obstruction and colonic volvulus. Gastrointest Endosc. 2020;91:228-235（当該ガイドライン論文）の PubMed 抄録レコード（DOI 10.1016/j.gie.2019.09.007／PMID 31791596） | 急性大腸偽性閉塞症（ACPO）は機械的閉塞がなく自律神経による大腸機能の調節異常で大腸が拡張する病態と抄録が述べており、「機械的な閉塞がなく機能的なもの」という中核部分は裏づけられる | 「分類上イレウスに入る」という日本の用語上の位置づけと、手術が必要になることが多いという臨床経過の部分は候補にない |
| AB-005 | Di Saverio S, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg. 2020;15:27（DOI 10.1186/s13017-020-00306-3／PMID 32295644／PMCID PMC7386163） | 単純性（uncomplicated）と複雑性（complicated）の枠組み、術中の重症度 grading（壊疽性・穿孔などを含む）、複雑性の術前判定の難しさ（misdiagnosing complicated appendicitis への言及）は同ガイドラインが扱う | 組織学的なカタル性・蜂窩織炎性・壊疽性という3分類の文言と、汎発性腹膜炎を伴うものを立てる日本の臨床分類そのものは候補にない |
| AB-015 | Sartelli M, et al. Intra-abdominal infections survival guide: a position statement by the Global Alliance for Infections in Surgery. World J Emerg Surg. 2024（DOI 10.1186/s13017-024-00552-9／PMID 38851700／PMCID PMC11161965） | 腹腔内感染・汎発性腹膜炎に対する迅速な診断と適時のソースコントロール（手術を含む）が管理の要であること、腸管虚血などへの緊急対応の枠組みは同ステートメントと整合する | 血管破裂・腹腔内出血・炎症性の急性腹症までを含む緊急手術適応の列挙そのものは候補にない（枠組み部分の裏づけ） |
| AB-018 | Sartelli M, et al. Intra-abdominal infections survival guide: a position statement by the Global Alliance for Infections in Surgery. World J Emerg Surg. 2024（DOI 10.1186/s13017-024-00552-9／PMID 38851700／PMCID PMC11161965） | 迅速で正確な診断、血行動態の安定化と臓器灌流の回復を先行させる初期対応の枠組みは同ステートメントの要（cornerstones）と一致する | 「自施設で根治治療ができない場合の転院」という日本の医療体制に即した手順と、バイタル異常の有無で分ける2段階の進め方そのものは候補にない |
| AB-019 | Sartelli M, et al. Intra-abdominal infections survival guide: a position statement by the Global Alliance for Infections in Surgery. World J Emerg Surg. 2024（DOI 10.1186/s13017-024-00552-9／PMID 38851700／PMCID PMC11161965） | 初期輸液で血圧が回復しなければ昇圧薬をできるだけ早く開始する（Statement 19：Low-quality evidence, Strong recommendation）という方向は一致する。輸液蘇生と血行動態・臓器サポートが管理の柱であることも同ステートメントが述べる | 末梢静脈から昇圧薬を開始する具体（肘窩かそれより中枢、短期間）と骨髄輸液は Surviving Sepsis Campaign 2021 由来の内容で、候補にはない（SSC 2021 本文は自由でない） |
| AB-020 | Sartelli M, et al. Intra-abdominal infections survival guide: a position statement by the Global Alliance for Infections in Surgery. World J Emerg Surg. 2024（DOI 10.1186/s13017-024-00552-9／PMID 38851700／PMCID PMC11161965） | 腹腔内感染への適切な抗菌薬療法を管理の要の一つとし、早期の適切な抗菌薬とソースコントロールを一体で進める枠組みは同ステートメントと一致する | 「できるだけ早く」という投与タイミングの推奨度（強い推奨・確実性C）そのものと、血液培養の採取手順は候補にない。なお候補は複雑性腹腔内感染では血液培養の陽性率が低い（10%未満）とも述べており、血液培養の位置づけは敗血症一般の指針（SSC）に依る部分である |
| AB-030 | Surgery for abdominal wall pain caused by cutaneous nerve entrapment in children: a review of 12 cases. Iran Red Crescent Med J. 2013（CC BY）（DOI 10.5812/ircmj.8422／PMID 23682329／PMCID PMC3652504） | 腹壁痛（皮神経絞扼 ACNES）の診断に Carnett 徴候の陽性が用いられることを同論文（小児12例、全例で Carnett 徴候陽性）が示しており、「腹壁の痛みの診断に役立つ」という用途部分は裏づけられる | 徴候の手技そのもの（仰臥位で頭を持ち上げ腹筋を緊張させる手順）と心因性腹痛への応用は候補にない |
| AB-032 | Manterola C, et al. Analgesia in patients with acute abdominal pain. Cochrane Database Syst Rev. 2011;(1):CD005660（当該レビュー）の PubMed 抄録レコード（DOI 10.1002/14651858.CD005660.pub3／PMID 21249672） | 著者結論「急性腹痛患者へのオピオイド鎮痛薬の使用は、診断エラーのリスクも治療判断のエラーのリスクも増やさない」が抄録に収載されており、オピオイドに関する中核部分は裏づけられる | アセトアミノフェンは同レビューの対象外で、「確実性A」という日本のガイドラインの格付けは候補にない |
| AB-038 | Acute mesenteric ischemia: updated guidelines of the World Society of Emergency Surgery. World J Emerg Surg. 2022;17:54（DOI 10.1186/s13017-022-00443-x／PMID 36261857／PMCID PMC9580452） | 腸間膜虚血の塞栓源として心房細動（左房由来）が挙げられ、塞栓性急性腸間膜虚血の約50%に心房細動があることが同ガイドラインに明記されており、「急性腹症で心房細動があれば腸間膜虚血を考える」部分は裏づけられる | 心窩部痛での心筋梗塞を考えた心電図の実施と、脾梗塞・腎梗塞への言及は候補にない |
| AB-040 | American College of Obstetricians and Gynecologists. Committee Opinion No. 723: Guidelines for Diagnostic Imaging During Pregnancy and Lactation（当該意見書）の PubMed 抄録レコード。補助：WSES Jerusalem ガイドライン2020（CC BY）（DOI 10.1097/AOG.0000000000002355／PMID 28937575） | 超音波と MRI はリスクと関連せず妊婦の画像検査の第一選択であることが抄録に明記されており、「特に妊婦に超音波が勧められる」部分は裏づけられる。虫垂炎等の診断で超音波・CT が必須の道具である点は Jerusalem ガイドラインとも整合する | 「急性腹症の画像検査で最初に行うのは超音波」という一般原則と、POCUS の提案（弱い推奨・確実性C）と予後改善の報告がない点は候補にない |
| AB-043 | Di Saverio S, et al. Diagnosis and treatment of acute appendicitis: 2020 update of the WSES Jerusalem guidelines. World J Emerg Surg. 2020;15:27（DOI 10.1186/s13017-020-00306-3／PMID 32295644／PMCID PMC7386163） | 造影 CT が虫垂炎を含む急性腹症の診断精度の高い検査であること、超音波・CT が必須の診断手段であることは同ガイドラインの推奨と一致する | 臓器虚血・血管性病変・膵炎の重症度・胆管炎・複雑性虫垂炎という適応の列挙と、絞扼性腸閉塞や大動脈病変で単純 CT を併せる運用は日本のガイドライン固有で、候補にない |
| AB-044 | メトホルミン米国添付文書（FDA ラベル、DailyMed 収載）のヨード造影剤に関する記載（（候補に識別子なし）） | FDA ラベルは eGFR 30〜60 の患者では造影時にメトホルミンを中止し、48時間後に eGFR を再評価して安定していれば再開すると定めており、「eGFR 30〜60 ではビグアナイドを休薬し48時間で区切る」という部分の枠組みは裏づけられる | eGFR 30 未満での輸液（生理食塩水・重曹液）と造影剤減量による腎症予防の部分は FDA ラベルになく、自由な資料では裏づけられなかった |
| AB-045 | American College of Obstetricians and Gynecologists. Committee Opinion No. 723: Guidelines for Diagnostic Imaging During Pregnancy and Lactation（当該意見書）の PubMed 抄録レコード（DOI 10.1097/AOG.0000000000002355／PMID 28937575） | 超音波と MRI がリスクと関連せず妊婦の画像検査の第一選択であることは抄録に明記されており、「超音波で確定できない妊婦の急性腹症に MRI」という方向は裏づけられる | 総胆管結石・虫垂炎疑いへの MRI の適応と、小児の発がんリスクへの言及は候補（抄録）にない |
| AB-052 | MedlinePlus Medical Encyclopedia（米国国立医学図書館）. Ectopic pregnancy（（候補に識別子なし）） | 症状として無月経・性器出血・下腹部痛が挙げられ、診断は妊娠検査と超音波で行い、hCG が一定値を超えれば子宮内に胎嚢が見えるはずで、見えなければ異所性妊娠が示唆されることが同記事に明記されており、主張の骨格は裏づけられる | 「最終月経から6週間以上」という無月経の期間の指定と、子宮外の液体貯留という所見の明記は候補にない |
| AB-069 | HerniaSurge Group. International guidelines for groin hernia management. Hernia. 2018;22:1-165（当該ガイドライン論文）の PubMed 抄録レコード（DOI 10.1007/s10029-017-1668-x／PMID 29330835／PMCID PMC5809582） | 鼠径ヘルニアの危険因子として男性が挙げられるなど、性差の方向は抄録と一致する |  |
| AB-070 | HerniaSurge Group. International guidelines for groin hernia management. Hernia. 2018;22:1-165（当該ガイドライン論文）の PubMed 抄録レコード（DOI 10.1007/s10029-017-1668-x／PMID 29330835／PMCID PMC5809582） | 「診断は身体診察のみで確認できることが大半で、超音波が必要になることはまれ」が抄録に明記されており、前半は裏づけられる | 再発ヘルニアで診察に超音波を組み合わせる推奨は抄録にない |
| AB-071 | HerniaSurge Group. International guidelines for groin hernia management. Hernia. 2018;22:1-165（当該ガイドライン論文）の PubMed 抄録レコード（DOI 10.1007/s10029-017-1668-x／PMID 29330835／PMCID PMC5809582） | 「無症状・軽度の男性鼠径ヘルニアは経過観察で管理してよい（緊急事態のリスクが低い）。ただし大半は最終的に手術を要する」が抄録に明記されており、主張の骨格は裏づけられる |  |
| AB-082 | Kirkpatrick AW, et al. Intra-abdominal hypertension and the abdominal compartment syndrome: updated consensus definitions and clinical practice guidelines from the World Society of the Abdominal Compartment Syndrome. Intensive Care Med. 2013;39:1190-1206（当該合意文書）の PubMed 抄録レコード（DOI 10.1007/s00134-013-2906-z／PMID 23673399／PMCID PMC3680657） | 腹腔内圧測定の推奨、腹腔内高血圧の持続を避けること、明らかな腹部コンパートメント症候群への減圧開腹の推奨という管理の枠組みは抄録と一致する |  |
| AB-083 | Kirkpatrick AW, et al. Intra-abdominal hypertension and the abdominal compartment syndrome: updated consensus definitions and clinical practice guidelines from the World Society of the Abdominal Compartment Syndrome. Intensive Care Med. 2013;39:1190-1206（当該合意文書）の PubMed 抄録レコード（DOI 10.1007/s00134-013-2906-z／PMID 23673399／PMCID PMC3680657） | 明らかな腹部コンパートメント症候群には減圧開腹が推奨されることは抄録に明記されており、主張の最後の要素は裏づけられる |  |
| AB-087 | Birindelli A, et al. 2017 update of the WSES guidelines for emergency repair of complicated abdominal wall hernias. World J Emerg Surg. 2017;12:37（DOI 10.1186/s13017-017-0149-y／PMID 28804507／PMCID PMC5545868） | 嵌頓ヘルニア（還納できない状態で腸閉塞を伴うことがある）と絞扼ヘルニア（内容への血流が障害された状態）の定義、腹壁ヘルニアを鼠径部ヘルニア（鼠径・大腿）と腹側ヘルニア（臍・腹壁瘢痕など）に分ける分類が同ガイドライン本文に明記されており、主張全体の骨格は裏づけられる |  |
| AB-088 | Birindelli A, et al. 2017 update of the WSES guidelines for emergency repair of complicated abdominal wall hernias. World J Emerg Surg. 2017;12:37（DOI 10.1186/s13017-017-0149-y／PMID 28804507／PMCID PMC5545868） | 腸管絞扼が疑われれば直ちに緊急手術（グレード1C）、SIRS・造影CT所見・乳酸・CPK・Dダイマーが腸管絞扼の予測に役立つ（1C）という推奨文とグレードが同ガイドラインの推奨表に明記されており、一致する | 臨床所見だけでは嵌頓から絞扼への進行を見つけるには不十分という点は、絞扼ヘルニアの診断の難しさとして本文の記述と方向は一致するが、同一の文言ではない |
| AB-089 | Birindelli A, et al. 2017 update of the WSES guidelines for emergency repair of complicated abdominal wall hernias. World J Emerg Surg. 2017;12:37（DOI 10.1186/s13017-017-0149-y／PMID 28804507／PMCID PMC5545868） | 自然に還納した絞扼性鼠径部ヘルニアで腸管の生存性確認に診断的腹腔鏡が役立つ（2B）、絞扼がなく腸切除が疑われない嵌頓ヘルニアは腹腔鏡で修復してよい（2C）という推奨が同ガイドラインに明記されている | 腸切除が疑われる場合に開腹の腹膜前到達法がよいとする細部は、推奨表の確認範囲では特定できなかった |
| AB-090 | Birindelli A, et al. 2017 update of the WSES guidelines for emergency repair of complicated abdominal wall hernias. World J Emerg Surg. 2017;12:37（DOI 10.1186/s13017-017-0149-y／PMID 28804507／PMCID PMC5545868） | 汚染のない術野（CDC創分類I）で絞扼・腸切除を伴わない嵌頓ヘルニアに合成メッシュ修復を推奨（1A）、腸内容の大量漏出がなければ創分類IIでも合成メッシュで修復でき30日以内の創合併症を増やさず再発を減らせる（1A）という推奨文が同ガイドラインに明記されており、一致する |  |
| AB-091 | Birindelli A, et al. 2017 update of the WSES guidelines for emergency repair of complicated abdominal wall hernias. World J Emerg Surg. 2017;12:37（DOI 10.1186/s13017-017-0149-y／PMID 28804507／PMCID PMC5545868） | 腸管壊死・大量漏出（創分類III）や腸穿孔による腹膜炎（IV）では、欠損が3 cm未満なら直接縫合（一次修復）を推奨（2C）、直接縫合ができなければ生体由来メッシュ、入手できなければ吸収性メッシュか創開放・後日修復、という推奨の流れが同ガイドラインに明記されている | 循環が安定している場合という条件づけの細部は推奨表の文言と完全には一致しない |
| AB-092 | Birindelli A, et al. 2017 update of the WSES guidelines for emergency repair of complicated abdominal wall hernias. World J Emerg Surg. 2017;12:37（DOI 10.1186/s13017-017-0149-y／PMID 28804507／PMCID PMC5545868） | 重症敗血症・敗血症性ショックで循環が不安定な患者では腹部コンパートメント症候群を防ぐため開腹管理を推奨し術中に腹腔内圧を測ってもよい（2C）という推奨が同ガイドラインに明記されている | 安定後の早期閉腹を目指す手順（筋膜を閉じられなければ皮膚のみ閉じて後日合成メッシュで修復、1C）の細部は本文の範囲で、推奨表の確認できた範囲では文言を特定できなかった |
| AB-093 | Birindelli A, et al. 2017 update of the WSES guidelines for emergency repair of complicated abdominal wall hernias. World J Emerg Surg. 2017;12:37（DOI 10.1186/s13017-017-0149-y／PMID 28804507／PMCID PMC5545868） | 抗菌薬は創分類Iでは短期間の予防投与（2C）、絞扼・腸切除を伴うII・IIIでは48時間の予防投与（2C）、腹膜炎（IV）では治療として投与という推奨が同ガイドラインの推奨表に明記されており、一致する。腸の壊死がない鼠径ヘルニアの緊急手術で局所麻酔が選択肢になる点も本文が扱う | 局所麻酔のグレード（1C）と「術後合併症が少ない」という効果の細部は推奨表の確認範囲では特定できなかった |
| AB-097 | Peritoneal Metastases: Evolution from a Dark Horizon to an Encouraging Present and a Promising Future. J Clin Med. 2023;12(24):7536（CC BY 総説）（DOI 10.3390/jcm12247536／PMID 38137604／PMCID PMC10743464） | 腹膜転移（播種）が消化器癌・卵巣癌などから腹腔内に広がる病態であること、予後が不良とされてきたことは同総説が扱い、M1c という分類が予後の悪さを理由に設けられた経緯も述べる | 悪性腹水・腸閉塞・疼痛という症状の列挙は同総説の確認範囲では特定できなかった。候補は二次資料（総説）のため裏づけ用途に限る |
| AB-102 | Govaerts K, et al. Appendiceal tumours and pseudomyxoma peritonei: literature review with PSOGI/EURACAN clinical practice guidelines. Eur J Surg Oncol. 2021;47:11-35（当該ガイドライン論文）の PubMed 抄録レコード（DOI 10.1016/j.ejso.2020.02.011／PMID 32199769） | 腹膜偽粘液腫が虫垂の上皮性腫瘍の穿孔に由来することが最も多いことは抄録に明記されており、発生機序の中核は裏づけられる | 粘液性腹水の貯留、CRS+HIPEC が標準治療であること、CC スコアと病理組織の悪性度が予後を規定することは抄録になく本文のみである。あわせて原典 SRC-4239 の PMID（32199769）の補完を提案する |
| AB-104 | Naveed M, et al. American Society for Gastrointestinal Endoscopy guideline on the role of endoscopy in the management of acute colonic pseudo-obstruction and colonic volvulus. Gastrointest Endosc. 2020;91:228-235（当該ガイドライン論文）の PubMed 抄録レコード（DOI 10.1016/j.gie.2019.09.007／PMID 31791596） | 大腸軸捻転は腸間膜を軸とした捻転で閉塞を来たす疾患で、S状結腸に最も多いこと、迅速な診断と介入で転帰が改善することは抄録に明記されており、主張の骨格は裏づけられる | 初期評価の手順（安定例では単純X線とCT、腹膜炎・穿孔・ショックでは緊急手術優先）の細部は抄録にない |
| AB-116 | Swallow CJ, et al. Management of primary retroperitoneal sarcoma (RPS) in the adult: an updated consensus approach from the Transatlantic Australasian RPS Working Group (TARPSWG). Ann Surg Oncol. 2021（当該合意文書）の PubMed 抄録レコード（DOI 10.1245/s10434-021-09654-z／PMID 33852100／PMCID PMC9257997） | 「この稀で複雑な悪性腫瘍は専門施設の経験ある多診療科チームで管理するのが最良」という主張の前提部分は抄録に明記されており裏づけられる | 標準治療が一括（コンパートメント）切除であることと、組織型で再発様式が異なる（脂肪肉腫は局所再発、平滑筋肉腫は遠隔転移）ことは抄録になく本文のみである。あわせて原典 SRC-4441 の PMCID（PMC9257997、マスター未登録）の補完を提案する |
| AB-119 | HerniaSurge Group. International guidelines for groin hernia management. Hernia. 2018;22:1-165（当該ガイドライン論文）の PubMed 抄録レコード（DOI 10.1007/s10029-017-1668-x／PMID 29330835／PMCID PMC5809582） | 大腿ヘルニアが嵌頓・絞扼の危険因子であること、女性であることが危険因子であること、大腿ヘルニアには時機を逃さないメッシュ修復（技術があれば腹腔鏡・内視鏡下）が提案されることは抄録に明記されており、主張の骨格は裏づけられる |  |

## C. 見つからない（45件）

| カード | 備考 |
|---|---|
| AB-001 | 定義（発症1週間以内）は日本のガイドライン固有の定義。2015年版の英語版（JJR 等）は存在するが Europe PMC でオープンアクセスでなく、抄録にも定義の記載はない。現出典は日本のガイドライン2025（書籍、SRC-154）の固有の整理・推奨であり、同内容を載せる自由な資料は本調査で確認できなかった。なお出典マスター SRC-154 には ISBN が未登録で、978-4-260-05773-8（NDL・日本超音波医学会掲載の前付けで確認）の補完を提案する |
| AB-002 | 痛みの病態の4分類は日本のガイドライン独自の整理で、同じ枠組みを載せる自由な資料は確認できなかった。現出典は日本のガイドライン2025（書籍、SRC-154）の固有の整理・推奨であり、同内容を載せる自由な資料は本調査で確認できなかった |
| AB-003 | 日本語の用語法（腸閉塞症とイレウスの区別、ileus の誤訳）に関する主張で、日本固有の事情のため外国の自由な資料では裏づけられない |
| AB-006 | 原因疾患の頻度の並びは日本のガイドラインの集約で、同じ順位・構成を示す自由な資料は確認できなかった |
| AB-007 | 日本の DPC データ（2009〜2011年）に基づく数値で、日本の行政・研究データ固有のため自由な公的資料に同じ集計はない |
| AB-008 | 日本の手術症例1,456例の検討という国内データ固有の数値で、裏づけられる自由な資料はない |
| AB-009 | 救急受診の5〜10%、致死的0.5%未満、入院20〜40%などの集積値はガイドラインが引用する文献の集約で、本調査で確認できた自由な資料のいずれにも同じ値の収載はなかった（不一致ではなく未収載） |
| AB-010 | 初診時診断率約7割・非特異的腹痛約3割という値はガイドライン引用文献の集約で、自由な資料では確認できなかった |
| AB-011 | 予後因子（心血管系病変、SOFA スコア、高齢）の集約は日本のガイドラインの総括文であり、単一の自由な資料では裏づけられない |
| AB-012 | 穿孔部位別の死亡率の比較（食道・下部消化管＞胃・十二指腸）はガイドラインの集約で、同じ比較を示す自由な資料は確認できなかった |
| AB-013 | 施設の症例数と診断率・予後の関係という医療提供体制の主張で、自由な資料では裏づけられない |
| AB-014 | 日本の医療訴訟の傾向という国内事情固有の主張で、裏づけ対象となる自由な資料はない |
| AB-016 | ショックを伴う腹部中央の激痛で鑑別すべき疾患の列挙は日本のガイドラインの合成文で、この集合をそのまま示す自由な資料は確認できなかった |
| AB-017 | 緊急内視鏡・血管造影/IVR の適応の詳細な列挙は日本のガイドライン固有の整理で、自由な資料では裏づけられない |
| AB-021 | 病歴聴取の項目と SAMPLE という枠組みは教育資料（AMLS 等）由来で自由でなく、日本のガイドラインの整理を裏づける自由な資料は確認できなかった |
| AB-022 | 身体診察の進め方の総論で、特定の一次資料に基づく主張ではなく、自由な資料での裏づけは確認できなかった |
| AB-023 | 頻呼吸・頻脈・低血圧・発熱と重症度・予後の関連（確実性の格付け付き）は日本のガイドラインの CQ 回答で、同じ格付けを示す自由な資料はない |
| AB-024 | 視診所見と腸閉塞の可能性の関係は診断精度研究の集約で、自由な資料では確認できなかった |
| AB-025 | 聴診の意義が限られるという評価と根拠は日本のガイドラインの CQ 回答で、自由な資料では確認できなかった |
| AB-026 | 小腸閉塞50例の単一報告の数値（蠕動音亢進50%、減弱・消失24%）で、自由な資料に同じ値はない |
| AB-027 | 腹膜刺激徴候の手技の整理と「打診痛が陽性なら反跳痛をあえて誘発する必要はない」という運用は日本のガイドラインの記述で、自由な資料では確認できなかった |
| AB-028 | 高齢の腹膜炎患者で筋性防御・板状硬が34%という報告の数値を含み、自由な資料では確認できなかった |
| AB-029 | 腸腰筋・閉鎖筋テストの特異度、Howship-Romberg 徴候、腹水の診察所見の有用性はいずれも診断精度文献の集約（確実性の格付け付き）で、自由な資料では確認できなかった |
| AB-031 | 直腸診・内診のルーチン実施の意義が限られるという評価は日本のガイドラインの CQ 回答で、自由な資料では確認できなかった |
| AB-033 | 鎮痛薬の選択と使い分け（アセトアミノフェン静注を常に、鎮痙薬は補助、NSAIDs の位置づけ）は日本のガイドラインの推奨文そのもので、自由な資料では裏づけられない |
| AB-034 | 「検査は偽陰性になることがあるため総合的に判断する」という総論的主張で、裏づけとなる特定の自由な資料は確認できなかった |
| AB-035 | プロカルシトニンの用途列挙と乳酸値の位置づけ（推奨度・確実性の格付け付き）は日本のガイドラインの CQ 回答で、自由な資料では確認できなかった |
| AB-036 | 複雑性虫垂炎へのプロカルシトニン・CRP・NLR の有用性と「約20%は白血球・CRP が正常、約10%は両方とも正常」という数値は日本のガイドライン引用文献の集約で、自由な資料では確認できなかった。WSES Jerusalem ガイドライン2020（CC BY）はバイオマーカーの補助的役割を論じるが、この数値自体は載らない |
| AB-037 | リパーゼ測定の有用性が急性膵炎に限られるという評価は日本のガイドラインの CQ 回答。ACG 膵炎ガイドラインの抄録（PMID 23896955）を確認したが、リパーゼ優先の明記は抄録の確認範囲になく、裏づけとして使えなかった |
| AB-039 | 妊娠反応・尿検査・尿中ポルホビリノゲンの使い分けは検査項目の列挙で、単一の自由な資料では裏づけられない |
| AB-041 | POCUS の診断精度が部位ごとに50例程度の経験で専門家と同等になるという数値は日本のガイドライン引用文献固有で、自由な資料にはない |
| AB-042 | 腹部単純X線の診断能が限られるという評価は各ガイドラインに通じるが、本調査で確認した自由な資料に明示的な裏づけ文は特定できなかった |
| AB-046 | 腹痛の部位別の鑑別疾患の整理は日本のガイドラインの総括表で、同じ整理を示す自由な資料は確認できなかった |
| AB-047 | 急性腹症と紛らわしい腹腔外病態の総論で、裏づけとなる特定の自由な資料は確認できなかった |
| AB-048 | 高齢者の急性腹症の特徴（所見が病状を反映しない、死亡率が年齢とともに高い、CT が有用）は総論として各資料に通じるが、本調査で確認できた自由な資料（高齢者の急性腹症 CT の総説等）は主張の核となる死亡率の内訳まで裏づけなかった |
| AB-049 | 免疫不全・麻痺・認知症の患者での診断の注意点は日本のガイドラインの総括文で、単一の自由な資料では裏づけられない |
| AB-050 | 手術歴のある患者・透析患者での鑑別疾患の列挙は日本のガイドライン固有の整理で、自由な資料では裏づけられない |
| AB-051 | 妊婦の急性腹症の鑑別疾患の列挙（妊娠関連と非関連）は日本のガイドラインの整理で、この集合を示す自由な資料は確認できなかった |
| AB-053 | 学童期の腹痛の原因の順位と IgA 血管炎の頻度、まれな致死的疾患の列挙は日本のガイドラインの集約。自由な資料として小児の急性腹痛の CC BY 研究（Cureus 2025、PMID 40656413）を確認したが単施設の後ろ向き研究で主張と対応せず、裏づけに使えなかった |
| AB-054 | 尿管結石を示唆する所見の列挙と STONE・CHOKAI スコアの提案は日本のガイドラインの CQ 回答で、スコアの原著はいずれも自由でなく、自由な資料では裏づけられない |
| AB-074 | 待機・緊急手術の合併症率・死亡率のプール解析値（待機 約8%・0.2〜0.5%、緊急 約32%・4〜5.5%）は原典（SRC-158）の本文のみで、抄録に収載がなく、他に裏づける自由な資料も確認できなかった |
| AB-100 | 原典（SRC-4238、PSOGI/EURACAN ガイドライン）の PubMed レコードには抄録自体が収載されておらず、腹膜中皮腫について同じ内容（アスベスト関連の弱さ、腹腔鏡下生検と免疫染色による診断）を裏づける CC BY の総説も本調査では特定できなかった。あわせて SRC-4238 の PMID（32209311）の補完を提案する |
| AB-101 | 原典（SRC-4238）には抄録がなく、CRS+HIPEC の適応選択と切除不能例の全身化学療法を裏づける自由な資料は本調査では特定できなかった（EJSO の系統的レビュー等は自由でない） |
| AB-103 | 原典（SRC-4240、ESMO ガイドライン）の PubMed レコードには抄録自体が収載されていない。後腹膜肉腫のコンセンサス（SRC-4441）の抄録は専門施設の多診療科チームという枠組みのみで、代表的組織型・無症状で巨大化・経腹膜経路を避けるコア針生検という主張の核は裏づけられない。あわせて SRC-4240 の PMID（34303806）の補完を提案する |
| AB-106 | 盲腸軸捻転で内視鏡的整復を行わず区域切除が標準という内容は原典 ASGE ガイドライン（SRC-4243）本文の記述で、抄録には大腸軸捻転一般の総論しかなく、自由な資料では裏づけられなかった。あわせて SRC-4243 の PMID（31791596）の補完を提案する |

## D. 区分の訂正（0件）

該当なし。ただし区分の確認結果として、SRC-158（HerniaSurge）と SRC-160（WSACS）は英語の国際誌ガイドラインでありながら CC BY-NC であり、現行の RESTRICTED が正しい（バッチ5の英語版ガイドライン＝CC BY のパターンとは異なる）。SRC-162・SRC-4237〜4243 はいずれもオープンアクセスでないことを Europe PMC で確認した。SRC-4441（TARPSWG）の PMC 収載コピー（PMC9257997）は著者原稿でライセンス表示がなく、OPEN には当たらない。

## 補足

- AB-087〜093 の裏づけ候補（WSES 2017、CC BY）は出典マスター未登録のため、裏づけとして使う場合は新規 SRC の登録が必要。
- AB-004 と AB-104 は、候補出典として同じ ASGE ガイドライン（SRC-4243）の抄録レコードと ASCRS ガイドライン（SRC-4241）の内容を用いた（いずれもカード側の現出典とは別出典の抄録レコードによる部分的裏づけ）。
