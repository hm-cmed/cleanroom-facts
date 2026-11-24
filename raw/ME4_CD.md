# 医療者教育（ME）第3弾 CD：ME-045〜053（カード9件）

依頼文（round_ME4_request.md、2026-11-24）に基づく第3弾のうち、CD（コースディベロップメント）領域の9枚。決定事項の適用は次のとおり。

- 作業前に取得したレポジトリ：hm-cmed/cleanroom-facts 最新版、コミット `10bd46714ac6120e912b72cdb761af8d32925210`（2026-11-24）。出典マスターと既存 ME カードで DOI・PMID の重複を照合し、本ファイルの新規出典はいずれも未登録であることを確認した。
- subdomain は「コースディベロップメント」とした。教育者向けの理論・枠組みが主題のため、カリキュラム欄は空欄とし、condition.対象 を「教育者」とした。
- 新規出典は SRC-5320〜5328 を割り当てた（SRC-5329 は AS のファイルで Downing 2005 に使用済み）。
- RESTRICTED の原典（教科書・古典論文・AMEE Guide）は、主張を枠組みの骨格に限って自作の文で書き、定義文の翻訳は転載していない。CC BY の総説で同じ内容を裏づけられるものは今回の探索では特定できなかったため、原典を主出典とし、その旨を未解決事項に記した。
- 分割案からの訂正：CD-3 の出典は、分割案の著者表記（Frank, Snell, ten Cate ら）ではなく、Europe PMC で確認した定義の系統的レビュー（Frank JR ら、Med Teach. 2010;32(8):631-637）を使った。CD-7（スパイラル）の著者は、分割案の「Harden & Stamper」が正しい（論文 PDF の著者欄で確認。当初はデータベースの単著表記に基づいて Harden RM の単著として作成したが、レポジトリ側の検証で誤りと判明し訂正した。詳細は本ファイル末尾の「検証指摘への修正記録」参照）。

## 1. 出典表

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 |
|---|---|---|---|---|---|---|
| SRC-5320 | Thomas PA, Kern DE, Hughes MT, Tackett SA, Chen BY (eds). Curriculum Development for Medical Education: A Six-Step Approach. 4th ed. Johns Hopkins University Press; 2022. ISBN 9781421444093（hardcover） | なし | なし | © Johns Hopkins University Press（All rights reserved） | RESTRICTED | 版元（Johns Hopkins University Press）の書誌ページと図書館目録で版（第4版、2022年8月刊行）・編者（Tackett が追加）・ISBN を確認。目次で6段階の構成を確認 |
| SRC-5321 | Harden RM, Crosby JR, Davis MH. AMEE Guide No. 14: Outcome-based education: Part 1 — An introduction to outcome-based education. Med Teach. 1999;21(1):7-14 | 10.1080/01421599979969 | なし | © Taylor & Francis（Medical Teacher、CC表示なし） | RESTRICTED | Crossref で書誌・DOI を確認。PMID は再照合でも確認できなかった（下記 ME-046 の uncertainty 参照） |
| SRC-5322 | Frank JR, Mungroo R, Ahmad Y, Wang M, De Rossi S, Horsley T. Toward a definition of competency-based education in medicine: a systematic review of published definitions. Med Teach. 2010;32(8):631-637 | 10.3109/0142159X.2010.500898 | 20662573 | © Taylor & Francis（Medical Teacher、CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（173件の分析、4つの主題）を確認 |
| SRC-5323 | Biggs J. Enhancing teaching through constructive alignment. High Educ. 1996;32(3):347-364 | 10.1007/BF00138871 | なし | © Springer（Higher Education、CC表示なし） | RESTRICTED | Crossref で書誌・DOI を確認（PMID は確認できなかった） |
| SRC-5324 | Anderson LW, Krathwohl DR (eds). A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives. Longman; 2001. ISBN 9780321084057（hardcover, Complete ed.） | なし | なし | © Addison Wesley Longman（All rights reserved） | RESTRICTED | Google Books と大学図書館目録（Stanford SearchWorks）で版・ISBN を確認 |
| SRC-5325 | Harden RM, Sowden S, Dunn WR. Educational strategies in curriculum development: the SPICES model. Med Educ. 1984;18(4):284-297 | 10.1111/j.1365-2923.1984.tb01024.x | 6738402 | © Wiley（Medical Education、CC表示なし） | RESTRICTED | Europe PMC で書誌を確認 |
| SRC-5326 | Harden RM, Stamper N. What is a spiral curriculum? Med Teach. 1999;21(2):141-143 | 10.1080/01421599979752 | 21275727 | © Taylor & Francis（Medical Teacher、CC表示なし） | RESTRICTED | 論文 PDF の著者欄で Harden RM と Stamper N の共著を確認（Europe PMC 等のデータベースの単著表記は誤りで、分割案の「Harden & Stamper」が正しい） |
| SRC-5327 | Hafferty FW. Beyond curriculum reform: confronting medicine's hidden curriculum. Acad Med. 1998;73(4):403-407 | 10.1097/00001888-199804000-00013 | 9580717 | © Association of American Medical Colleges（CC表示なし） | RESTRICTED | Europe PMC で書誌・抄録（公式・非公式・隠れたカリキュラムの区別、検討すべき4領域）を確認 |
| SRC-5328 | Harden RM. The integration ladder: a tool for curriculum planning and evaluation. Med Educ. 2000;34(7):551-557 | 10.1046/j.1365-2923.2000.00697.x | 10886638 | © Wiley（Medical Education、CC表示なし） | RESTRICTED | Europe PMC で書誌を確認（抄録の公開なし） |

## 2. 事実カード（YAML）

```yaml
- id: ME-045
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: Kern の6段階は、医学教育のカリキュラム開発を段階的に進めるための枠組みである。第1段階は問題の把握と一般的なニーズ評価、第2段階は対象とする学習者のニーズ評価、第3段階は目標と到達目標の設定、第4段階は教育方略の選択、第5段階は実施、第6段階は評価とフィードバックである。評価は最後に一度行うものではなく、結果をフィードバックしてカリキュラムの維持・改善につなげる循環として位置づけられる。新しいカリキュラムの新設だけでなく、既存のカリキュラムの改訂にも同じ手順が使われる。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5320
    source: 'Thomas PA, Kern DE, Hughes MT, Tackett SA, Chen BY (eds). Curriculum Development for Medical Education: A Six-Step Approach. 4th ed. Johns Hopkins University Press; 2022'
    doi: null
    pmid: null
    pmcid: null
    url: https://www.press.jhu.edu/books/title/12470/curriculum-development-medical-education
    source_license: © Johns Hopkins University Press（All rights reserved）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 6段階の名称と順序は第4版の目次で確認し、自作の文で記載した。各段階の進め方の細部は本文（書籍）の範囲のため含めていない。出典は現行の第4版（2022年刊行）とした。第4版では編者に Tackett SA が加わっている。ISBN は hardcover 版の 9781421444093 で、版元の情報で確認した。6段階の名称は第3版から変わっていない。6段階を同じ内容で裏づける CC BY の総説は今回の探索では特定できなかった。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-046
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: アウトカム基盤型教育（OBE）は、教育の設計を、学習者が修了時にできるようになること（アウトカム）から始める考え方である。まず卒業時点で到達すべき成果を明示し、そこから逆向きに、教育内容、教育方法、評価方法を決めていく。教える内容の網羅を起点に組み立てる従来型の計画と異なり、到達の明確化が設計の起点になるため、評価はアウトカムへの到達を測るものとして位置づけられ、学習者には到達すべき姿があらかじめ示される。医学教育では、専門職に求められる能力をアウトカムとして定める動きと結びついて広がった。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5321
    source: 'Harden RM, Crosby JR, Davis MH. AMEE Guide No. 14: Outcome-based education: Part 1 — An introduction to outcome-based education. Med Teach. 1999;21(1):7-14'
    doi: 10.1080/01421599979969
    pmid: null
    pmcid: null
    url: https://doi.org/10.1080/01421599979969
    source_license: © Taylor & Francis（Medical Teacher、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 書誌と DOI は Crossref で確認した。PMID は DOI 検索・題名検索とも PubMed と Europe PMC で照合した。AMEE Guide No. 14 のうち PubMed に収載されているのは Part 5（PMID 21281173）のみで、本カードの Part 1 は未収載であり、後付けの PMID も存在しないことを確認したため、null のままとした。主張は OBE の設計原理の骨格に限定した。AMEE Guide No. 14 は全5部からなり、本カードは第1部（入門）を出典とする。ME-001（コア・カリキュラム）・ME-005（臨床研修の到達目標）は、この考え方で設計された日本の制度側の内容を扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-047
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: コンピテンシー基盤型教育（CBME）は、履修した時間ではなく、学習者が到達した能力（コンピテンシー）を単位として教育を設計・評価する枠組みである。定義を集めた系統的レビュー（173件の資料を分析）では、CBME を特徴づける主題として、能力を組織化する枠組み、その根拠、時間との対比（時間で区切る従来型の養成との違い）、実装の進め方、の4つが整理された。その下位の要素として、アウトカムを先に定めること、能力で編んだカリキュラム、到達が実演可能であること、評価、学習者中心であること、社会のニーズに応えることが挙げられている。これらをもとに、修了時の能力に向けて方向づけられ、社会と患者のニーズの分析から導いたコンピテンシーを中心に組み立てられ、時間を基準とする養成の比重を下げる教育、という作業定義が提案されている。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5322
    source: 'Frank JR, Mungroo R, Ahmad Y, Wang M, De Rossi S, Horsley T. Toward a definition of competency-based education in medicine: a systematic review of published definitions. Med Teach. 2010;32(8):631-637'
    doi: 10.3109/0142159X.2010.500898
    pmid: '20662573'
    pmcid: null
    url: https://doi.org/10.3109/0142159X.2010.500898
    source_license: © Taylor & Francis（Medical Teacher、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 分析件数（173件）と、4つの主題（organizing framework、rationale、contrast with time、implementing CBE）と6つの下位主題の整理は抄録で確認した。作業定義は翻訳転載せず、構成要素の説明に留めた。分割案にあった著者表記（Snell、ten Cate ら）は国際ワーキンググループの定義論文側のもので、本カードでは定義の系統的レビューである本論文を出典とした。ME-007（EPA）は CBME の中での「任せられる活動」という実装の概念を扱い、本カードは枠組み全体を扱う。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-048
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: 構成的整合性（constructive alignment）は、意図した学習成果、学習活動、評価の3つを互いに整合させることを教育設計の原則とする考え方である。学習は、学習者が活動を通じて意味を構成する過程（構成的）と捉えられ、設計者は、到達してほしい成果の水準に合った活動を用意し、その成果をそのまま測る評価を置く。評価の方式は学習者の実際の学習行動を強く規定するため（評価が学習を駆動する）、成果と評価の対応が整合の出発点になる。成果・活動・評価のいずれかがずれていると、学習者は評価に受かるための学習に流れ、意図した学びが実現しにくくなる。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5323
    source: 'Biggs J. Enhancing teaching through constructive alignment. High Educ. 1996;32(3):347-364'
    doi: 10.1007/BF00138871
    pmid: null
    pmcid: null
    url: https://doi.org/10.1007/BF00138871
    source_license: © Springer（Higher Education、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 書誌と DOI は Crossref で確認した。PMID は確認できず null とした。原著は高等教育一般を対象とした論文で、医学教育に限ったものではない。主張は原則の骨格に限定し、Biggs と Tang の教科書（Teaching for Quality Learning at University）で展開された細部は含めていない。CC BY の総説での裏づけは今回の探索では特定できなかった。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-049
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: Bloom の分類の改訂版は、学習目標を2つの軸で整理する枠組みである。一つは認知過程の軸で、記憶する、理解する、応用する、分析する、評価する、創造する、の6つの水準からなる。もう一つは知識の軸で、事実的知識、概念的知識、手続き的知識、メタ認知的知識の4種を区別する。目標をこの2軸の表（タキソノミー・テーブル）に位置づけることで、目標・学習活動・評価の対応を点検でき、目標記述の動詞の選択を通じて、求める理解の深さを揃える共通言語として使われる。原版（1956年）からの改訂で、認知過程の最上位に「創造する」が置かれた。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5324
    source: 'Anderson LW, Krathwohl DR (eds). A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom''s Taxonomy of Educational Objectives. Longman; 2001'
    doi: null
    pmid: null
    pmcid: null
    url: null
    source_license: © Addison Wesley Longman（All rights reserved）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 書誌と ISBN（9780321084057、hardcover の Complete ed.）は Google Books と大学図書館目録で確認した。略版（abridged ed.）の ISBN は 9780801319037 で、版により異なる。6つの認知過程と4種の知識は分類の概念名として記載した。医学教育での利用を述べた CC BY 論文は多数あるが、分類そのものを裏づける単独の総説は今回特定しなかった。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-050
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: SPICES モデルは、カリキュラムの特徴を6つの連続体（スペクトラム）で表し、カリキュラム開発の方向づけを検討するためのモデルである。6つとは、学生中心か教師中心か（Student-centred/Teacher-centred）、問題基盤か情報収集基盤か（Problem-based/Information-gathering）、統合されているか教科別か（Integrated/Discipline-based）、地域基盤か病院基盤か（Community-based/Hospital-based）、選択制か一律か（Elective/Uniform）、系統的か見習い的か（Systematic/Apprenticeship-based）であり、頭文字をとって SPICES と呼ばれる。各カリキュラムは両極の間のどこかに位置づけられ、どちらか一方が常に優れるのではなく、自校の状況に応じた位置を検討する道具として使われる。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5325
    source: 'Harden RM, Sowden S, Dunn WR. Educational strategies in curriculum development: the SPICES model. Med Educ. 1984;18(4):284-297'
    doi: 10.1111/j.1365-2923.1984.tb01024.x
    pmid: '6738402'
    pmcid: null
    url: https://doi.org/10.1111/j.1365-2923.1984.tb01024.x
    source_license: © Wiley（Medical Education、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 書誌は Europe PMC で確認した。6つの連続体の名称はモデルの概念名として記載した。原著は抄録が公開されておらず、各連続体の議論の細部は含めていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-051
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: スパイラル・カリキュラムは、同じ主題を、学年や段階が上がるにつれて深さと複雑さを増しながら繰り返し学ぶカリキュラム設計である。初めは基本的な形で学んだ内容に後の段階で再び出会い、以前の学習と結びつけながら、より難しい課題への適用へ進む。再訪のたびに難易度が上がること、既習内容との関連づけが明示されること、学習の到達度に応じて次の段階へ進むことが、単なる繰り返しと区別する条件になる。基礎と臨床を学年をまたいで繰り返し扱う医学教育のカリキュラム設計で用いられる考え方である。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5326
    source: 'Harden RM, Stamper N. What is a spiral curriculum? Med Teach. 1999;21(2):141-143'
    doi: 10.1080/01421599979752
    pmid: '21275727'
    pmcid: null
    url: https://doi.org/10.1080/01421599979752
    source_license: © Taylor & Francis（Medical Teacher、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 著者は Harden RM と Stamper N の共著である（論文 PDF の著者欄で確認した。Europe PMC 等のデータベースでは Harden RM の単著と表示されるが、本文の著者表記に従った）。原著は短い解説で抄録が公開されておらず、主張は設計の骨格に限定した。PMID は後年に付与されたもの。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-052
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: 隠れたカリキュラムとは、公式のカリキュラム（教育課程として明示された内容）とは別に、組織の文化や現場の慣行を通じて学習者が学び取る規範や価値観のことをいう。医学教育の改革が教育課程の改訂だけでは実を結ばなかった背景として、医学校を「何を教えるか」ではなく「学習者が何を学び取るか」の観点から、学習環境として捉え直す必要があると指摘された。学習環境には、公式カリキュラム、非公式カリキュラム（学習者同士や教員との日常的なやり取り）、隠れたカリキュラムの3つが区別される。自校の隠れたカリキュラムを明らかにするには、組織の方針、評価の活動、資源配分の決め方、組織内で使われる言葉遣い、の4つの領域を検討することが提案されている。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5327
    source: 'Hafferty FW. Beyond curriculum reform: confronting medicine''s hidden curriculum. Acad Med. 1998;73(4):403-407'
    doi: 10.1097/00001888-199804000-00013
    pmid: '9580717'
    pmcid: null
    url: https://doi.org/10.1097/00001888-199804000-00013
    source_license: © Association of American Medical Colleges（Academic Medicine、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は抄録で確認した範囲（3つのカリキュラムの区別、学習環境としての捉え直し、検討すべき4領域）に基づく。分割案で裏づけ候補とした Lawrence らのスコーピングレビュー（Acad Med. 2019）は、今回の API 照合で書誌を確定できなかったため出典に含めていない。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
- id: ME-053
  domain: ME
  subdomain: コースディベロップメント
  assertion:
    plain_statement_ja: 統合のはしご（integration ladder）は、カリキュラムの統合の程度を段階で表す枠組みである。教科ごとに隔絶して教える段階から始まり、教科間で内容を意識し合う段階、時間割をそろえる段階、主題を中心に複数教科が共同で教える段階を経て、複数教科の境界を越えて学際的に統合する段階、最終的には学習者が自ら知識を統合する段階へと、統合が深まっていく様子を11の段で表す。カリキュラムの現状を位置づけ、統合をどこまで進めるかを計画・評価する際の道具として使われる。統合の深さそのものが目的ではなく、段階ごとに必要な準備や教員間の調整の量が異なる点に注意が要る。
    condition:
      region: 国際
      対象: 教育者
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-5328
    source: 'Harden RM. The integration ladder: a tool for curriculum planning and evaluation. Med Educ. 2000;34(7):551-557'
    doi: 10.1046/j.1365-2923.2000.00697.x
    pmid: '10886638'
    pmcid: null
    url: https://doi.org/10.1046/j.1365-2923.2000.00697.x
    source_license: © Wiley（Medical Education、CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 書誌は Europe PMC で確認した。原著は抄録が公開されておらず、11段の個別の名称の全列挙はせず、段階の幅と使い方の骨格に限定して記載した。各段の正確な名称は原著本文で確認されたい。
  curriculum:
    kokushi: null
    core_curriculum: null
  publication_info:
    created: '2026-11-24'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応表

| カード | kokushi | コアカリ |
|---|---|---|
| ME-045 | （空欄：教育者向け理論のため付けない） | （空欄） |
| ME-046 | （空欄：同上） | （空欄） |
| ME-047 | （空欄：同上） | （空欄） |
| ME-048 | （空欄：同上） | （空欄） |
| ME-049 | （空欄：同上） | （空欄） |
| ME-050 | （空欄：同上） | （空欄） |
| ME-051 | （空欄：同上） | （空欄） |
| ME-052 | （空欄：同上） | （空欄） |
| ME-053 | （空欄：同上） | （空欄） |

## 4. 未解決事項

1. CD の各原典（SRC-5320〜5328）は全て RESTRICTED のままとした。Kern の6段階、構成的整合性、SPICES、統合のはしごについて、同じ内容を裏づける CC BY の総説は今回の探索（Europe PMC のライセンス検索）では特定できなかった。見つかれば主出典の差し替えを検討されたい。
2. CD-2（ME-046）：PMID は再照合の結果、存在しないことを確認した（PubMed・Europe PMC とも Part 1 は未収載で、収載されているのは Part 5 のみ）。null のままとする（DOI は Crossref で確認）。
3. CD-4（ME-048）：PMID は確認できず null とした。原著は医学教育に限らない高等教育の論文である。
4. CD-7（ME-051）：著者は Harden & Stamper の共著が正しい（分割案どおり）。当初、データベースの単著表記に基づいて「分割案の誤りを訂正した」と記したが、それ自体が誤りであり、論文 PDF の著者欄の確認により共著に訂正した。CD-9（ME-053）：11段の個別名称は原著本文で未確認のため、主張では段階の幅の説明に留めた。
5. CD-8（ME-052）：裏づけ候補の Lawrence ら（2019）のスコーピングレビューは書誌を確定できず出典に含めていない。

## 5. 引き継ぎメモ

- 新規出典は9件（SRC-5320〜5328）。出典マスター全体と DOI・PMID で照合し、いずれも未登録であることを確認した。SRC-5329 は AS のファイルで使用したため、本ファイルでは使っていない。
- 書籍2件（SRC-5320、SRC-5324）の ISBN は、NLM Catalog・Google Books・大学図書館目録で確認した。provenance に ISBN の欄がないため、出典表と uncertainty に記載した。
- 第3弾の他の領域は別ファイル（TL：ME-026〜034、AS：ME-035〜044、EM：ME-054〜061、IT：ME-062〜071）。

## 6. 検証指摘への修正記録（2026-11-24）

レポジトリ側の検証（書誌・数値・ファイル間整合の確認）で指摘された点について、本ファイルでは次の修正を行った。

1. ME-051（スパイラル）：著者を「Harden RM 単著」から「Harden RM, Stamper N の共著」に訂正した（冒頭・出典表・provenance・uncertainty・未解決事項）。論文 PDF の著者欄では R.M. Harden & N. Stamper が正しく、データベースの単著表記が誤りだった。当初の「分割案の著者表記を訂正した（単著）」という記述自体が誤りであり、分割案の表記が正しかった。
2. ME-045（Kern）：出典を第3版（2016年）から現行の第4版（2022年）に差し替えた（出典表・provenance・uncertainty・URL）。第4版では編者に Tackett SA が加わり、ISBN は 9781421444093（hardcover）。6段階の名称は変わっていないため主張文はそのまま使える。
3. ME-047（CBME）：主張文が出典表の「4つの主題」とずれていた（下位主題を中核要素として6つ並べていた）ため、抄録を確認し、4主題（能力の枠組み・根拠・時間との対比・実装）に合わせて書き直した。6つの要素は下位主題として位置づけた。
4. ME-046：PMID の再照合を行った。PubMed・Europe PMC とも AMEE Guide No. 14 の Part 1 は未収載で（収載は Part 5 のみ、PMID 21281173）、後付けの PMID は存在しないことを確認した。PMID は null のまま（出典表・uncertainty・未解決事項に記録）。
5. ME-047：主張文の最後にあった「到達するまで学習期間が変わりうる点が特徴」は抄録の4主題・6下位主題のいずれにもない推論のため削除し、抄録で提案されている作業定義の構成要素（修了時の能力への方向づけ、社会と患者のニーズから導いたコンピテンシー、時間を基準とする養成の比重の低下）に置き換えた。
6. カードの uncertainty 欄・出典表の確認経路欄に入っていた修正経緯の記述を外し、経緯は本節に集約した（uncertainty には確かさに関わる事実だけを残す）。対象：ME-045・ME-046・ME-047・ME-051・出典表 SRC-5320。
