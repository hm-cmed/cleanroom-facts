# 皮膚・頭頸部 第24回：その他の皮膚疾患、横断項目（SD-001〜051、HX-001〜012）

- 作成日：2026-10-28（修正版 v2）
- v2 の修正点：(1) YAML のアンカー・エイリアス（10か所）をなくし、全カードの provenance を展開形にした。(2) コアカリの不変 id の誤り4件（HX-004・005・007・009）を依頼文 §7-2 の同じ行の値に直した。あわせて全63件の id を表と機械的に突き合わせ、ほかに誤りがないことを確認した。カードの ID・SRC 番号・主張文に変更はない。
- 事実票：63件（SD 51件、HX 12件、欠番なし）。目標60〜90件の範囲内。全件 `status: draft`、`verifier: null`。HX は全件 kokushi: null。
- 新規出典：49件。照合で見つけた重複1件（弾性線維性仮性黄色腫の総説が第21回の SRC-997 と同じ文献）を既存番号に統合した。コアカリの不変 id は登録表と機械的に突き合わせ、誤り4件（すべて HX）を修正した。薬剤名のあるカードの承認注記も点検し、SD-011 に注記を追加した。
- 国試は依頼文 §7-1 の表のうち SD の46項目中44項目に専用カードがあり、レベル a の19項目はすべてカバー。専用カードのない2項目（Ⅲ-3-K-④ 硬結性紅斑、c／Ⅲ-3-S-① アミロイド苔癬、b）は、それぞれ SD-037・SD-051 の中で合わせて扱っている。
- StatPearls の章を出典にしたカードが1件ある（SD-029 ひょう疽、SRC-1183）。本回は新しい方針の決定前に着手していたため、uncertainty に「二次資料経由（StatPearls）」と明記した。次回以降は原則として一次資料のみを使う。
- DOI が null の出典は5件、PMID が null の出典は2件（理由は出典表の確認経路に記載）。SRC-1165 は PubMed・Europe PMC とも未収載（2026-10-28時点）の新しい総説で、内容は出版社サイトの全文で確認した。

## 1. 抽出元ホワイトリスト（新規出典49件）

| SRC | 出典 | DOI | PMID | ライセンス表示 | source_class | 確認経路 | 使用カード |
|---|---|---|---|---|---|---|---|
| SRC-1161 | Mathur M, Paudel S, Bhattarai N, Karki S, Regmi S. Hailey-Hailey Disease: An Updated Review With a Focus on Therapeutic Mechanisms. Health Science Reports. 2025;8:e71061. | 10.1002/hsr2.71061 | 40661732 | CC BY 4.0 | OPEN | Europe PMC と Crossref で DOI・PMID・PMCID を照合し、Crossref のライセンス欄で CC BY 4.0 を確認。抄録で内容を確認 | SD-001 |
| SRC-1162 | Has C, Bauer JW, Bodemer C, Bolling MC, Bruckner-Tuderman L, et al. Consensus reclassification of inherited epidermolysis bullosa and other disorders with skin fragility. British Journal of Dermatology. 2020;183(4):614-627. | 10.1111/bjd.18921 | 32017015 | CC BY-NC 4.0 | RESTRICTED | Europe PMC と Crossref で DOI・PMID を照合し、Crossref のライセンス欄で CC BY-NC 4.0 を確認。抄録で内容を確認 | SD-002 |
| SRC-1163 | Murrell DF, Peña S, Joly P, Marinovic B, Hashimoto T, Diaz LA, et al. Diagnosis and management of pemphigus: Recommendations of an international panel of experts. Journal of the American Academy of Dermatology. 2020;82(3):575-585.e1. | 10.1016/j.jaad.2018.02.021 | 29438767 | ライセンス表示を確認できず | UNKNOWN | Europe PMC と Crossref で DOI・PMID・PMCID を照合。全文（PMC）と抄録で診断・治療の推奨内容を確認。Crossref に CC 表示なし | SD-003、SD-004 |
| SRC-1164 | Ujiie H, Iwata H, Yamagami J, Nakama T, Aoyama Y, Ikeda S, et al. Japanese guidelines for the management of pemphigoid (including epidermolysis bullosa acquisita). The Journal of Dermatology. 2019;46(12):1102-1135. | 10.1111/1346-8138.15111 | 31646663 | 日本皮膚科学会ガイドライン（CC表示なし） | RESTRICTED | Europe PMC と Crossref で DOI・PMID を照合。抄録と本文で類天疱瘡群の定義と治療推奨を確認 | SD-005、SD-006 |
| SRC-1165 | Sivadas A, Grada A, Ho M, Bunick C. Hereditary ichthyosis subtypes: Clinical updates. JAAD Reviews. 2026;8:40-51. | 10.1016/j.jdrv.2026.02.004 | null | CC BY 4.0 | OPEN | 出版社サイトの全文を開いて内容を確認。Crossref で DOI・巻号・ページと CC BY 4.0 を確認。PubMed と Europe PMC でタイトル・DOI を検索し、2026-10-28 時点で未収載（PMID・PMCID なし）を確認したため null | SD-007、SD-009 |
| SRC-1166 | Yoneda K, Kubo A, Nomura T, Ishida-Yamamoto A, Suga Y, Akiyama M, Kanazawa N, Hashimoto T, et al. Japanese guidelines for the management of palmoplantar keratoderma. The Journal of Dermatology. 2021;48(8):e353-e367. | 10.1111/1346-8138.15850 | 34121213 | 日本皮膚科学会ガイドライン（CC表示なし） | RESTRICTED | Europe PMC と Crossref で DOI・PMID を照合。抄録で定義とガイドラインの収載内容を確認 | SD-008 |
| SRC-1167 | Kanitakis J. Porokeratoses: an update of clinical, aetiopathogenic and therapeutic features. European Journal of Dermatology. 2014;24(5):533-544. | 10.1684/ejd.2014.2402 | 25115203 | ライセンス表示を確認できず | UNKNOWN | Europe PMC と Crossref で DOI・PMID を照合。抄録で臨床型・組織所見・悪性転化の頻度を確認 | SD-010 |
| SRC-1168 | Armstrong AW, Read C. Pathophysiology, Clinical Presentation, and Treatment of Psoriasis: A Review. JAMA. 2020;323(19):1945-1960. | 10.1001/jama.2020.4006 | 32427307 | ライセンス表示を確認できず | UNKNOWN | Europe PMC と Crossref で DOI・PMID を照合。抄録で病型・外用療法・光線療法・生物学的製剤・経口全身療法を確認 | SD-011、SD-012、SD-013 |
| SRC-1169 | Weston G, Payette M. Update on lichen planus and its clinical variants. International Journal of Women's Dermatology. 2015;1(3):140-149. | 10.1016/j.ijwd.2015.04.001 | 28491978 | CC BY-NC-ND 4.0 | RESTRICTED | Europe PMC と Crossref で DOI・PMID・PMCID を照合し、Crossref のライセンス欄で CC BY-NC-ND 4.0 を確認。抄録で古典的皮疹と治療を確認 | SD-014 |
| SRC-1170 | Mahajan K, Relhan V, Relhan AK, Garg VK. Pityriasis Rosea: An Update on Etiopathogenesis and Management of Difficult Aspects. Indian Journal of Dermatology. 2016;61(4):375-384. | 10.4103/0019-5154.185699 | 27512182 | CC BY-NC-SA 3.0 | RESTRICTED | Europe PMC と Crossref で DOI・PMID・PMCID を照合。 PMC 全文のライセンス表記で CC BY-NC-SA 3.0 を確認し、本文で経過と皮疹の分布を確認 | SD-015 |
| SRC-1171 | Chairatchaneeboon M, Thanomkitti K, Kim EJ. Parapsoriasis—A Diagnosis with an Identity Crisis: A Narrative Review. Dermatology and Therapy (Heidelberg). 2022;12(5):1091-1102. | 10.1007/s13555-022-00716-y | 35426607 | CC BY-NC 4.0 | RESTRICTED | Europe PMC と Crossref で DOI・PMID・PMCID を照合。PMC 全文のライセンス表記で CC BY-NC 4.0 を確認し、本文で分類と進展リスクを確認 | SD-016 |
| SRC-1172 | Fujita H, Terui T, Hayama K, Akiyama M, Ikeda S, Mabuchi T, et al. Japanese guidelines for the management and treatment of generalized pustular psoriasis. The Journal of Dermatology. 2018;45(11):1235-1270. | 10.1111/1346-8138.14523 | 30230572 | 日本皮膚科学会ガイドライン（CC表示なし） | RESTRICTED | Europe PMC と Crossref で DOI・PMID を照合。抄録で疾患の定義とガイドラインの収載内容を確認 | SD-017 |
| SRC-1173 | Japanese Dermatological Association Palmoplantar Pustulosis Treatment Guidance Drafting Committee. Treatment Guidance for Palmoplantar Pustulosis 2022. The Journal of Dermatology. 2026;53(7):e510-e566. | 10.1111/1346-8138.70246 | 42252553 | 日本皮膚科学会ガイダンス（CC表示なし） | RESTRICTED | Europe PMC と Crossref で DOI・PMID・PMCID を照合。抄録と本文で日本の患者数推計・病巣感染・治療アルゴリズムを確認 | SD-018 |
| SRC-1174 | Paek SY, Lim HW. Chronic actinic dermatitis. Dermatologic Clinics. 2014;32(3):355-361. | 10.1016/j.det.2014.03.007 | 24891057 | ライセンス表示を確認できず | UNKNOWN | Europe PMC と Crossref で DOI・PMID を照合。抄録で皮疹の分布・治療・自然軽快の割合を確認 | SD-019 |
| SRC-1175 | Ezzedine K, Eleftheriadou V, Whitton M, van Geel N. Vitiligo. The Lancet. 2015;386(9988):74-84. | 10.1016/S0140-6736(14)60763-7 | 25596811 | ライセンス表示を確認できず | UNKNOWN | Europe PMC と Crossref で DOI・PMID を照合。抄録で有病率・病型・メラノサイト消失を確認 | SD-020 |
| SRC-1176 | Lehmann AR, McGibbon D, Stefanini M. Xeroderma pigmentosum. Orphanet J Rare Dis. 2011;6:70. | 10.1186/1750-1172-6-70 | 22044607 | CC BY 2.0 | OPEN | Crossref と PubMed で DOI・PMID を照合。ライセンスは PMC 記事ページで CC BY 2.0 を確認 | SD-021 |
| SRC-1178 | Oshima J, Sidorova JM, Monnat RJ Jr. Werner syndrome: Clinical features, pathogenesis and potential therapeutic interventions. Ageing Res Rev. 2017;33:105-114. | 10.1016/j.arr.2016.03.002 | 26993153 | © 2016 Elsevier B.V.（CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは Elsevier の TDM 利用条件のみで CC 表示なし | SD-023 |
| SRC-1179 | Coon EA, Cheshire WP Jr. Sweating Disorders. Continuum (Minneap Minn). 2020;26(1):116-137. | 10.1212/CON.0000000000000813 | 31996625 | CC表示を確認できず | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。CC ライセンスの表示は確認できなかった | SD-024 |
| SRC-1180 | Stevens DL, Bisno AL, Chambers HF, et al. Practice guidelines for the diagnosis and management of skin and soft tissue infections: 2014 update by the Infectious Diseases Society of America. Clin Infect Dis. 2014;59(2):147-159. | 10.1093/cid/ciu296 | 24947530 | © The Author 2014, Oxford University Press（CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。CC ライセンスの表示は確認できなかった | SD-025、SD-028、SD-030 |
| SRC-1181 | Raff AB, Kroshinsky D. Cellulitis: A Review. JAMA. 2016;316(3):325-337. | 10.1001/jama.2016.8825 | 27434444 | © American Medical Association（CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。CC ライセンスの表示は確認できなかった | SD-026 |
| SRC-1182 | 厚生労働省. 抗微生物薬適正使用の手引き 第四版 医科・外来編. 2026. | null | null | 政府刊行物（厚生労働省） | GOV_JP | 厚生労働省の薬剤耐性（AMR）対策ページから第四版・医科・外来編の PDF を取得し、第12章「皮膚軟部組織感染症」の本文（要旨と蜂窩織炎の項）を確認。政府刊行物であり、DOI・PMID は付与されていない | SD-027 |
| SRC-1183 | Nardi NM, McDonald EJ, Syed HA, Schaefer TJ. Felon. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2024. | null | 28613683 | © 2024 StatPearls Publishing LLC | UNKNOWN | PubMed レコードで PMID と書誌を確認。StatPearls の章には DOI が付与されていないため DOI は null | SD-029 |
| SRC-1184 | Koning S, van der Sande R, Verhagen AP, et al. Interventions for impetigo. Cochrane Database Syst Rev. 2012;(1):CD003261. | 10.1002/14651858.CD003261.pub3 | 22258953 | © The Cochrane Collaboration（CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。CC ライセンスの表示は確認できなかった | SD-031 |
| SRC-1185 | Handler MZ, Schwartz RA. Staphylococcal scalded skin syndrome: diagnosis and management in children and adults. J Eur Acad Dermatol Venereol. 2014;28(11):1418-1423. | 10.1111/jdv.12541 | 24841497 | © European Academy of Dermatology and Venereology（CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは出版社（Wiley）の利用条件のみで CC 表示なし | SD-032 |
| SRC-1186 | Stevens DL, Bryant AE. Necrotizing Soft-Tissue Infections. N Engl J Med. 2017;377(23):2253-2265. | 10.1056/NEJMra1600673 | 29211672 | © Massachusetts Medical Society（CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。CC ライセンスの表示は確認できなかった。なお本文抄録は PubMed に収載されていない | SD-033、SD-034 |
| SRC-1187 | Franco-Paredes C, Marcos LA, Henao-Martínez AF, et al. Cutaneous Mycobacterial Infections. Clin Microbiol Rev. 2019;32(1):e00069-18. | 10.1128/CMR.00069-18 | 30429139 | © American Society for Microbiology（CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは ASM の non-commercial TDM ライセンスのみで CC 表示なし | SD-035、SD-036、SD-037 |
| SRC-1188 | Caplan AS, Gold JAW, Smith DJ, Ely JW. Diagnosis and Management of Tinea Infections. Am Fam Physician. 2025;112(4):382-392. | null | 41118183 | © American Academy of Family Physicians（CC表示なし） | UNKNOWN | PubMed レコードで PMID と書誌を確認。Am Fam Physician は DOI を付与していないため DOI は null | SD-038、SD-039 |
| SRC-1189 | Leung AKC, Barankin B, Lam JM, Leong KF, Hon KL. Tinea versicolor: an updated review. Drugs Context. 2022;11:2022-9-2. | 10.7573/dic.2022-9-2 | 36452877 | CC BY-NC-ND 4.0 | RESTRICTED | Crossref と PubMed で DOI・PMID を照合。ライセンスは PMC 記事ページで CC BY-NC-ND 4.0 を確認 | SD-040 |
| SRC-1190 | Barros MBL, de Almeida Paes R, Schubach AO. Sporothrix schenckii and Sporotrichosis. Clin Microbiol Rev. 2011;24(4):633-654. | 10.1128/CMR.00007-11 | 21976602 | © American Society for Microbiology（CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは ASM の non-commercial TDM ライセンスのみで CC 表示なし | SD-041 |
| SRC-1191 | Ishii N, Asai T, Asahina A, Ishiko A, et al. Guideline for the diagnosis and treatment of scabies in Japan (third edition): Executive Committee of Guideline for the Diagnosis and Treatment of Scabies. J Dermatol. 2017;44(9):991-1014. | 10.1111/1346-8138.13896 | 28561292 | © Japanese Dermatological Association（Wiley、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは Wiley の利用条件のみで CC 表示なし | SD-042、SD-043 |
| SRC-1192 | Fatahzadeh M, Schwartz RA. Human herpes simplex virus infections: epidemiology, pathogenesis, symptomatology, diagnosis, and management. J Am Acad Dermatol. 2007;57(5):737-763. | 10.1016/j.jaad.2007.06.027 | 17939933 | © American Academy of Dermatology（Elsevier、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは Elsevier の TDM 利用条件のみで CC 表示なし | SD-044 |
| SRC-1193 | Wollenberg A, Zoch C, Wetzel S, Plewig G, et al. Predisposing factors and clinical features of eczema herpeticum: a retrospective analysis of 100 cases. J Am Acad Dermatol. 2003;49(2):198-205. | 10.1067/s0190-9622(03)00896-x | 12894065 | © American Academy of Dermatology（Elsevier、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは Elsevier の TDM 利用条件のみで CC 表示なし | SD-045 |
| SRC-1194 | Sterling JC, Gibbs S, Haque Hussain SS, Mohd Mustapa MF, et al. British Association of Dermatologists' guidelines for the management of cutaneous warts 2014. Br J Dermatol. 2014;171(4):696-712. | 10.1111/bjd.13310 | 25273231 | © British Association of Dermatologists（Wiley、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは Wiley の利用条件と TDM ライセンスのみで CC 表示なし。なお PubMed に抄録は収載されていない | SD-046 |
| SRC-1195 | Reynolds RV, Yeung H, Cheng CE, Cook-Bolden F, et al. Guidelines of care for the management of acne vulgaris. J Am Acad Dermatol. 2024;90(5):1006.e1-1006.e30. | 10.1016/j.jaad.2023.12.017 | 38300170 | © American Academy of Dermatology（Elsevier、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは Elsevier の TDM 利用条件のみで CC 表示なし | SD-047 |
| SRC-1196 | Strazzulla LC, Wang EHC, Avila L, Lo Sicco K, et al. Alopecia areata: Disease characteristics, clinical evaluation, and new perspectives on pathogenesis. J Am Acad Dermatol. 2018;78(1):1-12. | 10.1016/j.jaad.2017.04.1141 | 29241771 | © American Academy of Dermatology（Elsevier、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは Elsevier の TDM 利用条件のみで CC 表示なし | SD-048 |
| SRC-1197 | Wang J, Khachemoune A. Granuloma Annulare: A Focused Review of Therapeutic Options. Am J Clin Dermatol. 2018;19(3):333-344. | 10.1007/s40257-017-0334-5 | 29230666 | © Springer（CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは Springer の TDM 利用条件のみで CC 表示なし | SD-049 |
| SRC-1198 | Miguel D, Schliemann S, Elsner P. Treatment of Scleroedema Adultorum Buschke: A Systematic Review. Acta Derm Venereol. 2018;98(3):305-309. | 10.2340/00015555-2846 | 29136263 | © Society for Publication of Acta Dermato-Venereologica（CC表示を確認できず） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。出版社ページと Crossref で CC ライセンスの表示を確認できなかった | SD-050 |
| SRC-1199 | Fatourechi V. Pretibial myxedema: pathophysiology and treatment options. Am J Clin Dermatol. 2005;6(5):295-309. | 10.2165/00128071-200506050-00003 | 16252929 | © Adis（Springer、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref にライセンス表示なし | SD-051 |
| SRC-1200 | Ely JW, Seabury Stone M. The generalized rash: part II. Diagnostic approach. Am Fam Physician. 2010;81(6):735-739. | null | 20229972 | © American Academy of Family Physicians（CC表示なし） | UNKNOWN | PubMed レコードで PMID と書誌を確認。Am Fam Physician は DOI を付与していないため DOI は null | HX-001 |
| SRC-1201 | Dinnes J, Deeks JJ, Chuchu N, Matin RN, et al. Visual inspection and dermoscopy, alone or in combination, for diagnosing keratinocyte skin cancers in adults. Cochrane Database Syst Rev. 2018;12(12):CD011901. | 10.1002/14651858.CD011901.pub2 | 30521688 | © The Cochrane Collaboration（Wiley、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。PMC 記事ページでも CC ライセンスの表示は確認できなかった | HX-002 |
| SRC-1202 | Uter W, Aerts O, Agner T, Brans R, et al. European Society of Contact Dermatitis Guideline for Diagnostic Patch Testing - Recommendations on Best Practice. Contact Dermatitis. 2026;95(3):237-275. | 10.1111/cod.70195 | 42324086 | CC BY 4.0 | OPEN | Crossref と PubMed で DOI・PMID を照合。ライセンスは Crossref の license 欄で CC BY 4.0 を確認 | HX-003 |
| SRC-1203 | Alguire PC, Mathes BM. Skin biopsy techniques for the internist. J Gen Intern Med. 1998;13(1):46-54. | 10.1046/j.1525-1497.1998.00009.x | 9462495 | © Society of General Internal Medicine（CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref にライセンス表示なし | HX-004 |
| SRC-1204 | Ponka D, Baddar F. Microscopic potassium hydroxide preparation. Can Fam Physician. 2014;60(1):57. | null | 24452564 | © College of Family Physicians of Canada（CC表示なし） | UNKNOWN | PubMed レコードと PMC 全文で PMID と書誌を確認。Can Fam Physician の本記事には DOI が付与されていないため DOI は null | HX-005 |
| SRC-1205 | Millington GWM, Collins A, Lovell CR, Leslie TA, et al. British Association of Dermatologists' guidelines for the investigation and management of generalized pruritus in adults without an underlying dermatosis, 2018. Br J Dermatol. 2018;178(1):34-60. | 10.1111/bjd.16117 | 29357600 | © British Association of Dermatologists（Wiley、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは Wiley の利用条件と TDM ライセンスのみで CC 表示なし。なお PubMed に抄録は収載されていない | HX-006 |
| SRC-1206 | Wallace DK, Flaxel CJ, Gedde SJ, Jacobs DS, et al. Comprehensive Adult Medical Eye Evaluation Preferred Practice Pattern. Ophthalmology. 2026;133(4):P202-P236. | 10.1016/j.ophtha.2025.12.031 | 41670577 | © American Academy of Ophthalmology（Elsevier、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは Elsevier の TDM 利用条件のみで CC 表示なし | HX-007 |
| SRC-1207 | Tarnutzer AA, Strupp ML, Lehner L. An update on neuro-otology and neuro-ophthalmology - focusing on new developments in the last three years. J Neurol. 2026;273(11). | 10.1007/s00415-026-14153-w | 42859937 | CC BY 4.0 | OPEN | Crossref と PubMed で DOI・PMID を照合。ライセンスは Crossref と PMC 記事ページで CC BY 4.0 を確認 | HX-008、HX-009 |
| SRC-1208 | Tunkel DE, Anne S, Payne SC, Ishman SL, et al. Clinical Practice Guideline: Nosebleed (Epistaxis). Otolaryngol Head Neck Surg. 2020;162(1_suppl):S1-S38. | 10.1177/0194599819890327 | 31910111 | © American Academy of Otolaryngology-Head and Neck Surgery Foundation（SAGE、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは出版社の利用条件のみで CC 表示なし | HX-010 |
| SRC-1209 | Stachler RJ, Francis DO, Schwartz SR, Damask CC, et al. Clinical Practice Guideline: Hoarseness (Dysphonia) (Update). Otolaryngol Head Neck Surg. 2018;158(1_suppl):S1-S42. | 10.1177/0194599817751030 | 29494321 | © American Academy of Otolaryngology-Head and Neck Surgery Foundation（SAGE、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは出版社の利用条件のみで CC 表示なし | HX-011 |
| SRC-1210 | Pynnonen MA, Gillespie MB, Roman B, Rosenfeld RM, et al. Clinical Practice Guideline: Evaluation of the Neck Mass in Adults. Otolaryngol Head Neck Surg. 2017;157(2_suppl):S1-S30. | 10.1177/0194599817722550 | 28891406 | © American Academy of Otolaryngology-Head and Neck Surgery Foundation（SAGE、CC表示なし） | UNKNOWN | Crossref と PubMed で DOI・PMID を照合。Crossref のライセンスは出版社の利用条件のみで CC 表示なし | HX-012 |

既存出典の再利用：SRC-997（Germain DP. Pseudoxanthoma elasticum. Orphanet J Rare Dis. 2017）を SD-022 に使用。
未使用の SRC 番号（1161〜1250 のうち）：SRC-1211〜1250（1177 は重複のため SRC-997 に統合して未使用）。

## 2. 事実票

```yaml
- id: HX-001
  domain: HX
  subdomain: 発疹の診かた
  assertion:
    plain_statement_ja: 全身性の発疹の評価は、包括的な鑑別診断を挙げることから始め、焦点を絞った病歴聴取と皮疹の主要な臨床的特徴の観察で絞り込んでいく。病歴では旅行、環境曝露、アトピー性疾患の個人歴・家族歴などが手がかりになる。皮疹そのものについては、個々の皮疹の色、大きさ、形、鱗屑といった性状と、手掌・足底、顔面、爪、日光曝露部、四肢の屈側・伸側を含む分布と病変のない部位、痒みや痛みの有無、発熱などの全身症状、圧迫による退色やケブネル現象といった皮膚科学的徴候を記載・評価することが鑑別の助けになる。
    condition:
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1200
    source: 'Ely JW, Seabury Stone M. The generalized rash: part II. Diagnostic approach. Am Fam Physician. 2010;81(6):735-739.'
    doi: null
    pmid: '20229972'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/20229972/
    source_license: © American Academy of Family Physicians（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: Am Fam Physician は DOI を付与していないため DOI は null とし、PubMed レコードで書誌と PMID を確認した。本カードは2部構成の第2部（診断アプローチ）に基づき、個別疾患の鑑別表（第1部）は含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-02 (id: JkxnuP8)；TBL-02-03-004 (id: JlAKpaY)；TBL-02-03-005 (id: JlAKpac)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-002
  domain: HX
  subdomain: ダーモスコピー
  assertion:
    plain_statement_ja: ダーモスコピーは、光源を備えた手持ち式の拡大鏡で、表皮から真皮浅層までの構造を詳しく観察する検査である。成人の角化細胞癌（基底細胞癌・有棘細胞癌）の診断精度を検証したコクランの系統的レビューでは、対面評価において基底細胞癌の検出でダーモスコピーは肉眼観察より正確であり、特異度を80%に固定したときの感度はダーモスコピー93%に対して肉眼観察79%と推定された。一方、有棘細胞癌については結論を出すのに十分なデータがなかった。
    condition:
      region: 国際
      study: 系統的レビュー（24研究）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1201
    source: Dinnes J, Deeks JJ, Chuchu N, Matin RN, et al. Visual inspection and dermoscopy, alone or in combination, for diagnosing keratinocyte skin cancers in adults. Cochrane Database Syst Rev. 2018;12(12):CD011901.
    doi: 10.1002/14651858.CD011901.pub2
    pmid: '30521688'
    pmcid: PMC6516870
    url: https://doi.org/10.1002/14651858.CD011901.pub2
    source_license: © The Cochrane Collaboration（Wiley、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 感度・特異度の数値は出典（コクランレビュー）の抄録と本文のメタ解析結果から読み取った。本レビューの対象は角化細胞癌であり、悪性黒色腫の診断精度は同じ著者らの別レビューの範囲であるため本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-03 (id: JkxnuQA)；TBL-02-03-011 (id: JlAKpa0)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-003
  domain: HX
  subdomain: 皮膚アレルギー検査（パッチテスト）
  assertion:
    plain_statement_ja: パッチテストは、アレルギー性接触皮膚炎やその他の遅延型過敏症が疑われる患者で、接触アレルギーを診断するための検査である。欧州接触皮膚炎学会（ESCD）のガイドライン改訂版は、検査の材料と手技、判定に影響する因子、小児や職業性接触皮膚炎、薬疹といった特殊な集団、患者が持ち込んだ物質のテスト、検査の有害事象、そして結果に基づく最終評価と患者への説明まで、パッチテストの全般を扱っている。
    condition:
      region: 欧州
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1202
    source: Uter W, Aerts O, Agner T, Brans R, et al. European Society of Contact Dermatitis Guideline for Diagnostic Patch Testing - Recommendations on Best Practice. Contact Dermatitis. 2026;95(3):237-275.
    doi: 10.1111/cod.70195
    pmid: '42324086'
    pmcid: PMC13441402
    url: https://doi.org/10.1111/cod.70195
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本ガイドラインは2015年の初版を更新した改訂版であり、本カードは抄録で確認できる構成と範囲に基づく。判定基準の細目など、本文の具体的な推奨文は本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-03 (id: JkxnuQA)；TBL-02-03-009 (id: JlAKpas)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-004
  domain: HX
  subdomain: 皮膚生検と病理検査
  assertion:
    plain_statement_ja: 皮膚生検は皮膚病変の確定診断のための基本的な手技であり、病変の種類や部位に応じて適切な生検法を選び、病理診断に適した検体を採取・処理することが診断の質を左右する。Alguire と Mathes の総説は、皮膚科専門医でない内科医が診療で行う皮膚生検について、生検手技の種類と実施の要点をまとめたものである。
    condition:
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1203
    source: Alguire PC, Mathes BM. Skin biopsy techniques for the internist. J Gen Intern Med. 1998;13(1):46-54.
    doi: 10.1046/j.1525-1497.1998.00009.x
    pmid: '9462495'
    pmcid: PMC1496896
    url: https://doi.org/10.1046/j.1525-1497.1998.00009.x
    source_license: © Society of General Internal Medicine（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 1998年の総説であり、その後の手技や病理検査の進歩は反映されていない可能性がある。個別の手技の手順の詳細は本文を確認していないため、本カードは定性的な記述に限った。
  curriculum:
    core_curriculum: 'PS-02-04-03 (id: JkxnuQA)；TBL-02-03-008 (id: JlAKpao)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-005
  domain: HX
  subdomain: 真菌検査（KOH直接検鏡）
  assertion:
    plain_statement_ja: KOH直接検鏡は、臨床所見だけでは真菌感染症かどうか判断がつかないときに行うポイントオブケアの検査である。鱗屑などの検体をスライドグラスに載せ、20%水酸化カリウム（KOH）を1滴加えてカバーグラスをかけ、顕微鏡の10倍で観察し、菌糸や出芽酵母を探す。真菌感染の検出における尤度比は2.86と報告され、基準標準である培養の尤度比3.28に近い一方、培養は結果まで6週間を要するのに対し、その場で結果が得られる。KOHで陰性でも培養の実施を検討する。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1204
    source: Ponka D, Baddar F. Microscopic potassium hydroxide preparation. Can Fam Physician. 2014;60(1):57.
    doi: null
    pmid: '24452564'
    pmcid: PMC3994805
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3994805/
    source_license: © College of Family Physicians of Canada（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 尤度比などの数値は出典の本文（PMC 全文）で確認した。出典は爪真菌症の評価に関する研究を引いており、部位によって検査性能が異なる可能性がある。本記事には DOI が付与されていないため DOI は null とした。
  curriculum:
    core_curriculum: 'PS-02-04-03 (id: JkxnuQA)；TBL-02-03-010 (id: JlAKpaw)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-006
  domain: HX
  subdomain: 瘙痒の評価
  assertion:
    plain_statement_ja: 成人の全身の瘙痒のうち、原因となる皮膚疾患が見当たらないものでは、皮膚以外の背景疾患が隠れていることがあり、その精査と管理の進め方が課題になる。英国皮膚科医協会の2018年のガイドラインは、基礎にある皮膚疾患のない成人の全身性瘙痒について、精査（investigation）と管理の手順を示したものである。
    condition:
      region: 英国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1205
    source: Millington GWM, Collins A, Lovell CR, Leslie TA, et al. British Association of Dermatologists' guidelines for the investigation and management of generalized pruritus in adults without an underlying dermatosis, 2018. Br J Dermatol. 2018;178(1):34-60.
    doi: 10.1111/bjd.16117
    pmid: '29357600'
    pmcid: null
    url: https://doi.org/10.1111/bjd.16117
    source_license: © British Association of Dermatologists（Wiley、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本ガイドラインの抄録は PubMed に収載されておらず、個別の検査項目や推奨の詳細は確認していないため、本カードはガイドラインの対象と位置づけを示す定性的な記述に限った。
  curriculum:
    core_curriculum: 'PS-02-04-02 (id: JkxnuP8)；TBL-02-03-005 (id: JlAKpac)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-007
  domain: HX
  subdomain: 眼科の基本検査（視力・眼圧・眼底）
  assertion:
    plain_statement_ja: 成人の包括的な眼科評価は、米国眼科学会（American Academy of Ophthalmology）の Preferred Practice Pattern として標準化されており、視力をはじめとする自覚的・他覚的な機能評価と、眼圧の測定、前眼部から眼底までの眼球各部の診察を組み合わせて行い、全身状態や既往とあわせて総合的に評価する枠組みである。視力障害の訴えがある場合は、この基本検査の組み合わせによって障害の部位と原因を絞り込んでいく。
    condition:
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1206
    source: Wallace DK, Flaxel CJ, Gedde SJ, Jacobs DS, et al. Comprehensive Adult Medical Eye Evaluation Preferred Practice Pattern. Ophthalmology. 2026;133(4):P202-P236.
    doi: 10.1016/j.ophtha.2025.12.031
    pmid: '41670577'
    pmcid: null
    url: https://doi.org/10.1016/j.ophtha.2025.12.031
    source_license: © American Academy of Ophthalmology（Elsevier、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードは Preferred Practice Pattern の位置づけと基本検査の構成を示す定性的な記述であり、個別の検査の基準値や実施間隔など本文の細目は確認していない。
  curriculum:
    core_curriculum: 'PS-02-15-02 (id: JkxnuTI)；TBL-02-14-008 (id: JlAKpuM)；TBL-02-14-014 (id: JlAKpuk)；TBL-02-14-017 (id: JlAKpuw)；TBL-02-14-018 (id: JlAKpu0)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-008
  domain: HX
  subdomain: 聴力検査と平衡機能検査
  assertion:
    plain_statement_ja: 前庭機能の評価は、ベッドサイド検査と定量的な機器検査を組み合わせて行う。ベッドサイドでは眼振の観察、head-impulse test、体位変換手技、Romberg test など前庭系と眼球運動系の診察が基本になる。定量検査では、急性前庭症候群の患者で video head-impulse test が最初の機器による前庭機能検査として推奨され、前庭眼反射（VOR）のゲインが患側で0.7未満であることが末梢性病変のカットオフの目安とされる。聴力については、急性の聴覚障害と前庭障害が合併する症例では、聴力検査によって患者が自覚していない難聴も検出されることがある。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1207
    source: Tarnutzer AA, Strupp ML, Lehner L. An update on neuro-otology and neuro-ophthalmology - focusing on new developments in the last three years. J Neurol. 2026;273(11).
    doi: 10.1007/s00415-026-14153-w
    pmid: '42859937'
    pmcid: PMC13654878
    url: https://doi.org/10.1007/s00415-026-14153-w
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: VOR ゲインのカットオフ（0.7）などの数値は出典の本文（PMC 全文）で確認した。本出典は神経耳科学の最近の進展を扱う総説であり、純音聴力検査そのものの判定手順の詳細は主対象ではないため、本カードの聴力検査に関する記述は急性の聴覚・前庭障害の評価に関する部分に限った。
  curriculum:
    core_curriculum: 'PS-02-15-03 (id: JkxnuTM)；TBL-02-15-023 (id: JlAKpxM)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-009
  domain: HX
  subdomain: 難聴とめまいの評価
  assertion:
    plain_statement_ja: めまいを訴える患者の臨床診断は、時間経過、誘因・修飾因子、随伴症状を含む構造化された病歴と、前庭系・眼球運動系のベッドサイド検査に基づいて行われ、中枢性の眼球運動サインの有無が重視される。新たに生じた片側の難聴を伴う急性前庭症候群では、難聴そのものが重要な随伴所見となり、HINTS+（head-impulse、眼振、skewの検査に新たな片側難聴を加えた評価）の要素として、前庭神経炎などの末梢性病変と脳幹・小脳の脳卒中（前下小脳動脈領域を含む）との鑑別で考慮される。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1207
    source: Tarnutzer AA, Strupp ML, Lehner L. An update on neuro-otology and neuro-ophthalmology - focusing on new developments in the last three years. J Neurol. 2026;273(11).
    doi: 10.1007/s00415-026-14153-w
    pmid: '42859937'
    pmcid: PMC13654878
    url: https://doi.org/10.1007/s00415-026-14153-w
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 本カードは急性の聴覚・前庭症状の評価に関する出典の記載に基づく。慢性の難聴そのものの分類や補聴器適応などの評価は本出典の範囲外であり、補完候補として Michels TC らの成人難聴の総説（Am Fam Physician. 2019、PMID 31305044）がある。
  curriculum:
    core_curriculum: 'PS-02-15-03 (id: JkxnuTM)；TBL-02-15-007 (id: JlAKpwM)；TBL-02-15-010 (id: JlAKpwY)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-010
  domain: HX
  subdomain: 鼻出血の評価と初期対応
  assertion:
    plain_statement_ja: 鼻出血はありふれた問題で、米国では少なくとも60%の人が生涯に一度は経験し、医療機関を受診するのはその約6%とされる。鼻出血は救急外来受診の0.5%を占め、耳鼻咽喉科関連の救急受診の最大で3分の1に達する。米国耳鼻咽喉科・頭頸部外科学会の診療ガイドラインは、重症、持続性、反復性の出血や生活の質に影響する出血を対象とし、対応は自宅でのセルフケアから診療所・救急部門・手術室での処置まで幅広いことを前提に、評価と初期対応の推奨を示している。
    condition:
      region: 米国
      study: 診療ガイドライン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1208
    source: 'Tunkel DE, Anne S, Payne SC, Ishman SL, et al. Clinical Practice Guideline: Nosebleed (Epistaxis). Otolaryngol Head Neck Surg. 2020;162(1_suppl):S1-S38.'
    doi: 10.1177/0194599819890327
    pmid: '31910111'
    pmcid: null
    url: https://doi.org/10.1177/0194599819890327
    source_license: © American Academy of Otolaryngology-Head and Neck Surgery Foundation（SAGE、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 頻度の数値（60%、約6%、救急受診の0.5%）は出典の抄録の記載に基づく。個別の止血処置の手順や推奨の強さは本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-15-03 (id: JkxnuTM)；TBL-02-15-011 (id: JlAKpwc)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-011
  domain: HX
  subdomain: 嗄声と咽頭痛の評価
  assertion:
    plain_statement_ja: 嗄声（発声障害、dysphonia）は、声の質、高さ、大きさ、発声の努力感の変化によってコミュニケーションや生活の質が損なわれる状態で、人口のほぼ3分の1が生涯のどこかで経験する。米国耳鼻咽喉科・頭頸部外科学会の診療ガイドライン（2018年改訂）は、あらゆる年齢の発声障害患者を対象に、評価と治療に関するエビデンスに基づく推奨を示している。咽頭痛を伴う場合は、発声障害の原因となる咽喉頭の病変を念頭に評価を進める。
    condition:
      region: 米国
      study: 診療ガイドライン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1209
    source: 'Stachler RJ, Francis DO, Schwartz SR, Damask CC, et al. Clinical Practice Guideline: Hoarseness (Dysphonia) (Update). Otolaryngol Head Neck Surg. 2018;158(1_suppl):S1-S42.'
    doi: 10.1177/0194599817751030
    pmid: '29494321'
    pmcid: null
    url: https://doi.org/10.1177/0194599817751030
    source_license: © American Academy of Otolaryngology-Head and Neck Surgery Foundation（SAGE、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 経験頻度（人口のほぼ3分の1）は出典の抄録の記載に基づく。本ガイドラインの主対象は発声障害であり、咽頭痛そのものの鑑別診断（ウイルス性・細菌性咽頭炎など）は対象外のため、本カードの咽頭痛に関する記述は発声障害に伴う範囲に限った。
  curriculum:
    core_curriculum: 'PS-02-15-03 (id: JkxnuTM)；TBL-02-15-012 (id: JlAKpwg)；TBL-02-15-014 (id: JlAKpwo)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: HX-012
  domain: HX
  subdomain: 頸部腫瘤の評価
  assertion:
    plain_statement_ja: 成人の頸部腫瘤はありふれているが、その原因は容易には分からないことが多い。小児では感染が最も多いのに対し、成人の持続する頸部腫瘤の多くは腫瘍性であり、悪性腫瘍は他のどの原因よりも多い。無症状の頸部腫瘤が、扁平上皮癌、リンパ腫、甲状腺癌、唾液腺癌などの頭頸部癌の初発または唯一の臨床所見であることがある。そのため成人の頸部腫瘤は、悪性でないと証明されるまでは悪性として扱い、転移性扁平上皮癌による腫瘤では診断の遅れが病期と予後に直接影響するため、速やかな診断が重要である。
    condition:
      region: 米国
      study: 診療ガイドライン
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1210
    source: 'Pynnonen MA, Gillespie MB, Roman B, Rosenfeld RM, et al. Clinical Practice Guideline: Evaluation of the Neck Mass in Adults. Otolaryngol Head Neck Surg. 2017;157(2_suppl):S1-S30.'
    doi: 10.1177/0194599817722550
    pmid: '28891406'
    pmcid: null
    url: https://doi.org/10.1177/0194599817722550
    source_license: © American Academy of Otolaryngology-Head and Neck Surgery Foundation（SAGE、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードは出典の抄録で確認できる評価の原則に基づく。画像検査や穿刺吸引細胞診の適応など、推奨の具体的な手順は本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-15-03 (id: JkxnuTM)'
    kokushi: null
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-001
  domain: SD
  subdomain: 先天性・遺伝性水疱症
  assertion:
    plain_statement_ja: Hailey-Hailey病は、ATP2C1遺伝子の変異による常染色体優性遺伝の皮膚疾患で、頸部・腋窩・鼠径部・会陰などの摩擦部位に、慢性で有痛性のびらん性局面と亀裂を繰り返す。ATP2C1はゴルジ体の分泌経路カルシウム／マンガンATPase（hSPCA1）をコードし、病理組織では「崩れたレンガ壁」と表現される棘融解像が特徴である。根治療法はなく、管理の目的は症状の制御と再発の予防である。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1161
    source: 'Mathur M, Paudel S, Bhattarai N, Karki S, Regmi S. Hailey-Hailey Disease: An Updated Review With a Focus on Therapeutic Mechanisms. Health Science Reports. 2025;8:e71061.'
    doi: 10.1002/hsr2.71061
    pmid: '40661732'
    pmcid: PMC12257355
    url: https://doi.org/10.1002/hsr2.71061
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 主張は出典の抄録で確認できた範囲に限定した。具体的な治療薬剤の有効性の比較は抄録では確認できないため記載していない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-A-①（Hailey-Hailey病、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-002
  domain: SD
  subdomain: 先天性・遺伝性水疱症
  assertion:
    plain_statement_ja: 先天性表皮水疱症は、皮膚の脆弱性のために軽微な外力で水疱やびらんを生じる遺伝性疾患群である。国際コンセンサスによる再分類では、皮膚の剥離が起こるレベルに基づいて、単純型、接合部型、栄養障害型、Kindler症候群の4つの古典的タイプに分けられる。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1162
    source: Has C, Bauer JW, Bodemer C, Bolling MC, Bruckner-Tuderman L, et al. Consensus reclassification of inherited epidermolysis bullosa and other disorders with skin fragility. British Journal of Dermatology. 2020;183(4):614-627.
    doi: 10.1111/bjd.18921
    pmid: '32017015'
    pmcid: null
    url: https://doi.org/10.1111/bjd.18921
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は出典の抄録と分類の枠組みで確認できた範囲に限定した。各タイプの原因遺伝子の詳細は本文の表に依存するため記載していない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-A-②（先天性表皮水疱症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-003
  domain: SD
  subdomain: 自己免疫性水疱症
  assertion:
    plain_statement_ja: 天疱瘡の診断は、臨床所見だけでは不十分であり、病理組織学的検査と、直接蛍光抗体法または血清学的検査（抗デスモグレイン抗体など）を組み合わせて行うことが、国際的な専門家の合意として推奨されている。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1163
    source: 'Murrell DF, Peña S, Joly P, Marinovic B, Hashimoto T, Diaz LA, et al. Diagnosis and management of pemphigus: Recommendations of an international panel of experts. Journal of the American Academy of Dermatology. 2020;82(3):575-585.e1.'
    doi: 10.1016/j.jaad.2018.02.021
    pmid: '29438767'
    pmcid: PMC7313440
    url: https://doi.org/10.1016/j.jaad.2018.02.021
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 主張は出典の全文と抄録で確認できた範囲に限定した。日本の診断基準の細部は本出典の対象外である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-B-①（天疱瘡、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-004
  domain: SD
  subdomain: 自己免疫性水疱症
  assertion:
    plain_statement_ja: 天疱瘡の治療では、全身性コルチコステロイドと抗CD20抗体リツキシマブが第一選択の柱であり、アザチオプリンやミコフェノール酸モフェチルはステロイドの減量を目的とする補助療法として用いられる。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1163
    source: 'Murrell DF, Peña S, Joly P, Marinovic B, Hashimoto T, Diaz LA, et al. Diagnosis and management of pemphigus: Recommendations of an international panel of experts. Journal of the American Academy of Dermatology. 2020;82(3):575-585.e1.'
    doi: 10.1016/j.jaad.2018.02.021
    pmid: '29438767'
    pmcid: PMC7313440
    url: https://doi.org/10.1016/j.jaad.2018.02.021
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: リツキシマブ、アザチオプリン、ミコフェノール酸モフェチル等の個別薬剤について、国内の承認・保険適用は本担当では確認しておらず未確認である。用量や投与スケジュールは出典の推奨の細部に依存するため記載していない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-B-①（天疱瘡、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-005
  domain: SD
  subdomain: 自己免疫性水疱症
  assertion:
    plain_statement_ja: 類天疱瘡群は、表皮基底膜部に自己抗体が線状に沈着する自己免疫性表皮下水疱症の一群で、IgG自己抗体による主な病型として水疱性類天疱瘡、粘膜類天疱瘡、後天性表皮水疱症が含まれる。日本皮膚科学会のガイドラインでは、水疱性類天疱瘡の治療として全身性コルチコステロイドが標準と位置づけられている。
    condition:
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1164
    source: Ujiie H, Iwata H, Yamagami J, Nakama T, Aoyama Y, Ikeda S, et al. Japanese guidelines for the management of pemphigoid (including epidermolysis bullosa acquisita). The Journal of Dermatology. 2019;46(12):1102-1135.
    doi: 10.1111/1346-8138.15111
    pmid: '31646663'
    pmcid: null
    url: https://doi.org/10.1111/1346-8138.15111
    source_license: 日本皮膚科学会ガイドライン（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張はガイドラインの抄録と本文で確認できた範囲に限定した。コルチコステロイド等の個別薬剤について、国内の承認・保険適用の細部は本担当では確認しておらず未確認である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-B-②（水疱性類天疱瘡、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-006
  domain: SD
  subdomain: 自己免疫性水疱症
  assertion:
    plain_statement_ja: 後天性表皮水疱症は類天疱瘡群に含まれる自己免疫性表皮下水疱症であり、日本皮膚科学会のガイドラインでは、水疱性類天疱瘡の治療アルゴリズムに準じて治療され、コルヒチンが用いられることがある。
    condition:
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1164
    source: Ujiie H, Iwata H, Yamagami J, Nakama T, Aoyama Y, Ikeda S, et al. Japanese guidelines for the management of pemphigoid (including epidermolysis bullosa acquisita). The Journal of Dermatology. 2019;46(12):1102-1135.
    doi: 10.1111/1346-8138.15111
    pmid: '31646663'
    pmcid: null
    url: https://doi.org/10.1111/1346-8138.15111
    source_license: 日本皮膚科学会ガイドライン（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張はガイドラインの抄録と本文で確認できた範囲に限定した。コルヒチンの国内の承認・保険適用は本担当では確認しておらず未確認である。テトラサイクリンとニコチン酸アミドの併用や超強力外用ステロイドについては、本症への有効性の根拠がない旨がガイドラインに記載されている。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-B-③（後天性表皮水疱症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-007
  domain: SD
  subdomain: 角化症
  assertion:
    plain_statement_ja: 遺伝性魚鱗癬は、乾燥と鱗屑を特徴とする20を超える疾患の総称であり、2025年の命名法では症候性表皮分化異常症（sEDD）、非症候性表皮分化異常症（nEDD）、掌蹠表皮分化異常症（pEDD）に分類される。ステロイドサルファターゼ欠損による伴性劣性魚鱗癬は尋常性魚鱗癬に次いで多く、約5,000〜6,000人に1人とされる。常染色体劣性先天性魚鱗癬はコロジオン膜をかぶって出生し、原因遺伝子ではTGM1の変異が最も多い。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1165
    source: 'Sivadas A, Grada A, Ho M, Bunick C. Hereditary ichthyosis subtypes: Clinical updates. JAAD Reviews. 2026;8:40-51.'
    doi: 10.1016/j.jdrv.2026.02.004
    pmid: null
    pmcid: null
    url: https://doi.org/10.1016/j.jdrv.2026.02.004
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 主張は出典の全文（出版社サイト）で確認した範囲に限定し、数値は本文中の記載に基づく。本論文は2026-10-28時点でPubMedとEurope PMCに未収載であり、PMIDとPMCIDは確認できなかったためnullとした。2025年命名法は近年の再分類であり、従来の分類名との対応は本文の記載範囲に限られる。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-C-①（魚鱗癬、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-008
  domain: SD
  subdomain: 角化症
  assertion:
    plain_statement_ja: 掌蹠角化症は、手掌と足底の過角化を主症状とする角化症の総称である。日本皮膚科学会のガイドラインは、その臨床像、病態生理、診断基準、重症度判定基準と治療の推奨をまとめている。
    condition:
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1166
    source: Yoneda K, Kubo A, Nomura T, Ishida-Yamamoto A, Suga Y, Akiyama M, Kanazawa N, Hashimoto T, et al. Japanese guidelines for the management of palmoplantar keratoderma. The Journal of Dermatology. 2021;48(8):e353-e367.
    doi: 10.1111/1346-8138.15850
    pmid: '34121213'
    pmcid: null
    url: https://doi.org/10.1111/1346-8138.15850
    source_license: 日本皮膚科学会ガイドライン（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張はガイドラインの抄録で確認できた範囲に限定した。個別の病型の診断基準の細部はガイドライン本文の表に依存するため記載していない。本症はまれな疾患の集まりであり、ガイドラインの推奨の一部は委員会の意見に基づく旨が抄録に明記されている。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-C-②（掌蹠角化症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-009
  domain: SD
  subdomain: 角化症
  assertion:
    plain_statement_ja: Darier病は、ATP2A2遺伝子の常染色体優性変異による疾患で、頭皮、前額、胸部、背部などの脂漏部位に角化性丘疹と局面を生じ、紫外線、高温、多湿で悪化する。爪の白斑や爪下角化、口腔粘膜の白板症を伴うことがある。治療は対症療法が中心で、保湿剤、外用コルチコステロイド、レチノイドが用いられ、欧州集団での有病率は約26,000〜30,000人に1人と報告されている。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1165
    source: 'Sivadas A, Grada A, Ho M, Bunick C. Hereditary ichthyosis subtypes: Clinical updates. JAAD Reviews. 2026;8:40-51.'
    doi: 10.1016/j.jdrv.2026.02.004
    pmid: null
    pmcid: null
    url: https://doi.org/10.1016/j.jdrv.2026.02.004
    source_license: CC BY 4.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 主張は出典の全文（出版社サイト）で確認した範囲に限定し、有病率は本文中の欧州集団についての記載に基づく。レチノイド等の個別薬剤について、国内の承認・保険適用は本担当では確認しておらず未確認である。本論文は2026-10-28時点でPubMedとEurope PMCに未収載であり、PMIDとPMCIDは確認できなかったためnullとした。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-C-③（Darier病、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-010
  domain: SD
  subdomain: 角化症
  assertion:
    plain_statement_ja: 汗孔角化症は、角化の異常による環状または線状の角化性局面を特徴とする疾患群で、組織学的な指標は、角質層内に不全角化細胞が垂直に積み重なるcornoid lamellaである。最も多い病型は播種状表在性光線性汗孔角化症であり、病変が悪性転化（多くは有棘細胞癌）するのは10%未満とされる。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1167
    source: 'Kanitakis J. Porokeratoses: an update of clinical, aetiopathogenic and therapeutic features. European Journal of Dermatology. 2014;24(5):533-544.'
    doi: 10.1684/ejd.2014.2402
    pmid: '25115203'
    pmcid: null
    url: https://doi.org/10.1684/ejd.2014.2402
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 主張は出典の抄録で確認できた範囲に限定した。悪性転化の頻度は抄録の「10%未満」という記載に基づく。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-C-④（汗孔角化症、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-011
  domain: SD
  subdomain: 乾癬
  assertion:
    plain_statement_ja: 乾癬は慢性の炎症性皮膚疾患で、局面型の尋常性乾癬が最も多い病型である。世界で約1億2,500万人が罹患するとされ、病態にはTNF-α、IL-17、IL-23などのサイトカイン経路が関与し、これらを標的とする生物学的製剤が治療に用いられている。乾癬性関節炎、心血管代謝性疾患、うつ病などの合併症との関連が知られている。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1168
    source: 'Armstrong AW, Read C. Pathophysiology, Clinical Presentation, and Treatment of Psoriasis: A Review. JAMA. 2020;323(19):1945-1960.'
    doi: 10.1001/jama.2020.4006
    pmid: '32427307'
    pmcid: null
    url: https://doi.org/10.1001/jama.2020.4006
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 主張は出典の抄録で確認できた範囲に限定した。本カードは皮膚病変と病態を扱い、関節病変の詳細は扱わない。患者数は抄録の「世界で約1億2,500万人」という記載に基づく。本カードで触れた生物学的製剤の個別薬剤の国内承認・保険適用は未確認。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-082 (id: Jlvnlio)'
    kokushi: 医学各論 Ⅲ-3-D-①（乾癬、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-012
  domain: SD
  subdomain: 乾癬
  assertion:
    plain_statement_ja: 軽症の尋常性乾癬では外用療法が治療の中心であり、外用コルチコステロイド、ビタミンD誘導体、カルシニューリン阻害薬、角質溶解薬が用いられる。光線療法では、局面型乾癬に対してナローバンドUVBが最も一般的に処方される。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1168
    source: 'Armstrong AW, Read C. Pathophysiology, Clinical Presentation, and Treatment of Psoriasis: A Review. JAMA. 2020;323(19):1945-1960.'
    doi: 10.1001/jama.2020.4006
    pmid: '32427307'
    pmcid: null
    url: https://doi.org/10.1001/jama.2020.4006
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 主張は出典の抄録で確認できた範囲に限定した。外用薬の個別製剤や光線療法の照射条件について、国内の承認・保険適用と実施条件は本担当では確認しておらず未確認である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-082 (id: Jlvnlio)'
    kokushi: 医学各論 Ⅲ-3-D-①（乾癬、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-013
  domain: SD
  subdomain: 乾癬
  assertion:
    plain_statement_ja: 中等症から重症の尋常性乾癬では、TNF-α阻害薬、IL-12／23のp40阻害薬、IL-17阻害薬、IL-23のp19阻害薬などの生物学的製剤が第一選択の選択肢となりうる。経口の全身療法としては、メトトレキサート、アシトレチン、シクロスポリンと、ホスホジエステラーゼ4阻害薬のアプレミラストがある。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1168
    source: 'Armstrong AW, Read C. Pathophysiology, Clinical Presentation, and Treatment of Psoriasis: A Review. JAMA. 2020;323(19):1945-1960.'
    doi: 10.1001/jama.2020.4006
    pmid: '32427307'
    pmcid: null
    url: https://doi.org/10.1001/jama.2020.4006
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 主張は出典の抄録で確認できた範囲に限定した。生物学的製剤と経口薬の個別製剤について、国内の承認・保険適用は本担当では確認しておらず未確認である。本カードは皮膚病変への全身療法を扱い、関節病変への適応は扱わない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-082 (id: Jlvnlio)'
    kokushi: 医学各論 Ⅲ-3-D-①（乾癬、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-014
  domain: SD
  subdomain: 苔癬・粃糠疹類
  assertion:
    plain_statement_ja: 扁平苔癬は炎症性皮膚疾患で、典型例では、そう痒を伴う多角形で紫紅色の平坦な丘疹と局面を呈する。口腔や爪などにも病変を生じる多彩な病型があり、病理組織学的所見が診断の助けとなる。治療は症状の制御と発症から改善までの期間の短縮が目的で、外用コルチコステロイドがしばしば用いられる。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1169
    source: Weston G, Payette M. Update on lichen planus and its clinical variants. International Journal of Women's Dermatology. 2015;1(3):140-149.
    doi: 10.1016/j.ijwd.2015.04.001
    pmid: '28491978'
    pmcid: PMC5418875
    url: https://doi.org/10.1016/j.ijwd.2015.04.001
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は出典の抄録で確認できた範囲に限定した。外用コルチコステロイド等の個別薬剤について、国内の承認・保険適用は本担当では確認しておらず未確認である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-083 (id: Jlvnlis)'
    kokushi: 医学各論 Ⅲ-3-D-②（扁平苔癬、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-015
  domain: SD
  subdomain: 苔癬・粃糠疹類
  assertion:
    plain_statement_ja: Gibertばら色粃糠疹は、体幹や頸部に大きな紅斑性鱗屑性局面である原発疹（herald patch）が出現し、続いて体幹を中心に多数の小型の二次疹が皮膚の割線に沿って分布する（背部ではクリスマスツリー状）疾患である。多くは15〜30歳にみられ、通常は2〜8週で自然に改善する自己限定的な経過をとる。病因は確定していない。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1170
    source: 'Mahajan K, Relhan V, Relhan AK, Garg VK. Pityriasis Rosea: An Update on Etiopathogenesis and Management of Difficult Aspects. Indian Journal of Dermatology. 2016;61(4):375-384.'
    doi: 10.4103/0019-5154.185699
    pmid: '27512182'
    pmcid: PMC4966395
    url: https://doi.org/10.4103/0019-5154.185699
    source_license: CC BY-NC-SA 3.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は出典の全文（PMC）で確認した範囲に限定し、経過の週数は本文中の記載に基づく。単一の感染性病原体が原因であるという確定的な証拠はない旨が本文に記載されており、病因は未確定として扱った。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-084 (id: Jlvnli0)'
    kokushi: 医学各論 Ⅲ-3-D-③（Gibertばら色粃糠疹、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-016
  domain: SD
  subdomain: 苔癬・粃糠疹類
  assertion:
    plain_statement_ja: 類乾癬は、現在の分類では小型局面状類乾癬と大型局面状類乾癬を指す。皮膚リンパ腫（最も多いのは菌状息肉症）への進展リスクは小型局面状では小さいが、大型局面状では大きく高い。治療は、経過観察、または保湿剤、外用コルチコステロイド、光線療法などの外用療法が中心である。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1171
    source: 'Chairatchaneeboon M, Thanomkitti K, Kim EJ. Parapsoriasis—A Diagnosis with an Identity Crisis: A Narrative Review. Dermatology and Therapy (Heidelberg). 2022;12(5):1091-1102.'
    doi: 10.1007/s13555-022-00716-y
    pmid: '35426607'
    pmcid: PMC9110571
    url: https://doi.org/10.1007/s13555-022-00716-y
    source_license: CC BY-NC 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張は出典の全文（PMC）で確認した範囲に限定した。進展リスクの定量的な数値は出典本文で一貫した値を確認できなかったため、大小の対比のみを記載した。外用コルチコステロイド等の個別薬剤について、国内の承認・保険適用は本担当では確認しておらず未確認である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-D-④（類乾癬、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-017
  domain: SD
  subdomain: 膿疱症
  assertion:
    plain_statement_ja: 汎発性膿疱性乾癬は、発熱と全身の潮紅を伴い、無菌性膿疱が広範囲に再発性に出現するまれな疾患である。日本皮膚科学会のガイドラインには、その診断基準と重症度分類、病態、治療の推奨がまとめられている。
    condition:
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1172
    source: Fujita H, Terui T, Hayama K, Akiyama M, Ikeda S, Mabuchi T, et al. Japanese guidelines for the management and treatment of generalized pustular psoriasis. The Journal of Dermatology. 2018;45(11):1235-1270.
    doi: 10.1111/1346-8138.14523
    pmid: '30230572'
    pmcid: null
    url: https://doi.org/10.1111/1346-8138.14523
    source_license: 日本皮膚科学会ガイドライン（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 主張はガイドラインの抄録で確認できた範囲に限定した。診断基準と重症度分類の細目はガイドライン本文の表に依存するため記載していない。本症はまれで、エビデンスレベルの高い臨床試験データが少ない旨が抄録に明記されている。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-E-①（膿疱性乾癬、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-018
  domain: SD
  subdomain: 膿疱症
  assertion:
    plain_statement_ja: 掌蹠膿疱症は、手掌と足底に無菌性膿疱が繰り返し出現する疾患で、日本ではレセプトデータに基づき約14万人の患者がいると推計される。扁桃炎などの病巣感染が誘因となることが多く、日本皮膚科学会の治療ガイダンスでは、治療アルゴリズムが乾癬とは根本的に異なることが示されている。
    condition:
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1173
    source: Japanese Dermatological Association Palmoplantar Pustulosis Treatment Guidance Drafting Committee. Treatment Guidance for Palmoplantar Pustulosis 2022. The Journal of Dermatology. 2026;53(7):e510-e566.
    doi: 10.1111/1346-8138.70246
    pmid: '42252553'
    pmcid: PMC13341069
    url: https://doi.org/10.1111/1346-8138.70246
    source_license: 日本皮膚科学会ガイダンス（CC表示なし）
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 患者数の推計はガイダンス本文のレセプトデータに基づく記載による。本カードは皮膚病変を扱い、掌蹠膿疱症性骨関節炎などの骨・関節病変の詳細は範囲外とした。具体的な治療薬剤の推奨度はガイダンス本文のアルゴリズムに依存するため記載していない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-081 (id: Jlvnlic)'
    kokushi: 医学各論 Ⅲ-3-E-②（掌蹠膿疱症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-019
  domain: SD
  subdomain: 光線性皮膚疾患
  assertion:
    plain_statement_ja: 慢性光線性皮膚炎は、免疫が関与する光線過敏症で、日光露光部にそう痒性の湿疹性・苔癬化局面を生じ、眼瞼、皮膚のしわ、耳介後部は侵されにくい。内因性抗原への二次的な光感作が機序と考えられている。管理は厳密な遮光と外用コルチコステロイド、カルシニューリン阻害薬が中心で、経口プレドニゾン、シクロスポリン、アザチオプリン、ミコフェノール酸モフェチルが有効な場合がある。遮光とアレルゲンの回避により、15年間で50%が自然に軽快するとされる。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1174
    source: Paek SY, Lim HW. Chronic actinic dermatitis. Dermatologic Clinics. 2014;32(3):355-361.
    doi: 10.1016/j.det.2014.03.007
    pmid: '24891057'
    pmcid: null
    url: https://doi.org/10.1016/j.det.2014.03.007
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 主張は出典の抄録で確認できた範囲に限定し、自然軽快の割合は抄録の「15年で50%」という記載に基づく。プレドニゾン、シクロスポリン等の個別薬剤について、国内の承認・保険適用は本担当では確認しておらず未確認である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-F-①（慢性光線性皮膚炎、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-020
  domain: SD
  subdomain: 色素異常症
  assertion:
    plain_statement_ja: 尋常性白斑は、機能するメラノサイトの消失により白色斑を生じる後天性の色素異常症で、世界人口の約1%にみられると推計される。分節型と、最も多い非分節型に分けられ、両者では治療の選択肢と予後が異なるため、その鑑別が重要である。
    condition:
      region: 全世界
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1175
    source: Ezzedine K, Eleftheriadou V, Whitton M, van Geel N. Vitiligo. The Lancet. 2015;386(9988):74-84.
    doi: 10.1016/S0140-6736(14)60763-7
    pmid: '25596811'
    pmcid: null
    url: https://doi.org/10.1016/S0140-6736(14)60763-7
    source_license: ライセンス表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 主張は出典の抄録で確認できた範囲に限定し、有病率は抄録の「約1%」という推計に基づく。個別の治療法の有効性の比較は抄録では確認できないため記載していない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-115 (id: JlvnlmY)'
    kokushi: 医学各論 Ⅲ-3-G-①（尋常性白斑、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-021
  domain: SD
  subdomain: 色素性乾皮症
  assertion:
    plain_statement_ja: 色素性乾皮症は、紫外線による DNA 損傷の修復（ヌクレオチド除去修復に関わる XPA から XPG の遺伝子群）または損傷を乗り越える複製（XPV／DNA ポリメラーゼη）の欠損による常染色体劣性の疾患である。露光部に強い日焼け反応や早期の雀卵斑様色素沈着が現れ、色素の増減、皮膚の老化様変化、皮膚癌の多発を来す。発生頻度は日本で約2万人に1人とされる。根治療法はなく、厳重な紫外線防御と前癌病変・皮膚癌の早期切除が管理の中心である。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1176
    source: Lehmann AR, McGibbon D, Stefanini M. Xeroderma pigmentosum. Orphanet J Rare Dis. 2011;6:70.
    doi: 10.1186/1750-1172-6-70
    pmid: '22044607'
    pmcid: PMC3221642
    url: https://doi.org/10.1186/1750-1172-6-70
    source_license: CC BY 2.0
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 頻度（日本で約2万人に1人）は出典の抄録に記載された推計値である。一部の患者でみられる神経症状の詳細は本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-H-①（色素性乾皮症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-022
  domain: SD
  subdomain: 弾性線維性仮性黄色腫
  assertion:
    plain_statement_ja: 弾性線維性仮性黄色腫は、ABCC6 遺伝子の変異による常染色体劣性の代謝性疾患で、皮膚・眼・血管の弾性組織に異栄養性石灰化を来す。初発所見は頸部や屈曲部に生じる小さい黄色丘疹で、進行すると皮膚は弛緩し皺が増える。眼では網膜色素線条と脈絡膜新生血管により中心視力が失われ得るほか、末梢動脈疾患や間欠性跛行などの血管病変を生じる。有病率は2万5千人から10万人に1人と推定される。根治療法はなく、眼病変への抗 VEGF 療法や血管リスクの管理が対症療法の中心である。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-997
    source: Germain DP. Pseudoxanthoma elasticum. Orphanet J Rare Dis. 2017;12(1):85.
    doi: 10.1186/s13023-017-0639-8
    pmid: '28486967'
    pmcid: null
    url: https://doi.org/10.1186/s13023-017-0639-8
    source_license: CC BY 4.0（Europe PMCの表示）
    legal_basis: B
    source_class: OPEN
    corroboration: null
  uncertainty: 抗 VEGF 療法は出典で眼病変への対症療法として挙げられているが、本疾患に伴う脈絡膜新生血管に対する国内の承認・保険適用は未確認である。有病率の数値は出典の抄録の推定値である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-H-②（弾性線維性仮性黄色腫、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-023
  domain: SD
  subdomain: Werner症候群
  assertion:
    plain_statement_ja: Werner 症候群は、RECQ ファミリーの DNA ヘリカーゼをコードする WRN 遺伝子の機能喪失変異による常染色体劣性の疾患で、加速した老化に似た徴候を多臓器に呈する代表的な早老症である。WRN 蛋白は DNA の修復・組換え・複製・転写やテロメアの維持に関わり、その障害によるゲノム不安定性が老化様表現型の基盤とされる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1178
    source: 'Oshima J, Sidorova JM, Monnat RJ Jr. Werner syndrome: Clinical features, pathogenesis and potential therapeutic interventions. Ageing Res Rev. 2017;33:105-114.'
    doi: 10.1016/j.arr.2016.03.002
    pmid: '26993153'
    pmcid: PMC5025328
    url: https://doi.org/10.1016/j.arr.2016.03.002
    source_license: © 2016 Elsevier B.V.（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 皮膚の萎縮・硬化や難治性潰瘍など個別の皮膚所見の頻度は、出典の抄録に明記されていないため本カードには含めていない。治療介入は研究段階であり、確立した治療法として記載していない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-H-③（Werner症候群、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-024
  domain: SD
  subdomain: 多汗症、無汗症
  assertion:
    plain_statement_ja: 発汗障害は多汗症と無汗症（低汗症）に大別され、視床下部から脳幹・脊髄を経て交感神経節・末梢神経・エックリン汗腺へ至る発汗経路のどの部位の障害でも生じ、中枢性・末梢性の自律神経障害が背景にあることが多い。原発性多汗症は器質的には良性であるが生活の質への影響が大きい。無汗症は体温調節ができず熱中症の危険を伴い、無汗部位を代償する多汗（代償性多汗症）として現れることもある。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1179
    source: Coon EA, Cheshire WP Jr. Sweating Disorders. Continuum (Minneap Minn). 2020;26(1):116-137.
    doi: 10.1212/CON.0000000000000813
    pmid: '31996625'
    pmcid: null
    url: https://doi.org/10.1212/CON.0000000000000813
    source_license: CC表示を確認できず
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 個別の治療（外用薬、イオントフォレーシス、ボツリヌス毒素局所療法など）の選択や効果の数値は出典の抄録の範囲を超えるため含めていない。汗腺そのものの疾患による発汗異常の詳細も本カードの範囲外である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-108 (id: Jlvnlls)；TBL-01-00-109 (id: Jlvnll0)'
    kokushi: 医学各論 Ⅲ-3-I-①（多汗症、無汗症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-025
  domain: SD
  subdomain: せつ、癰
  assertion:
    plain_statement_ja: せつ（癤）は黄色ブドウ球菌による毛包とその周囲の深部感染であり、癰は複数の毛包に及んだものである。波動を触れる膿瘍を形成した場合の治療の基本は切開排膿であり、周囲に蜂窩織炎が広がる場合や全身症状・免疫不全を伴う場合には、原因菌をカバーする抗菌薬を併用する。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1180
    source: 'Stevens DL, Bisno AL, Chambers HF, et al. Practice guidelines for the diagnosis and management of skin and soft tissue infections: 2014 update by the Infectious Diseases Society of America. Clin Infect Dis. 2014;59(2):147-159.'
    doi: 10.1093/cid/ciu296
    pmid: '24947530'
    pmcid: null
    url: https://doi.org/10.1093/cid/ciu296
    source_license: © The Author 2014, Oxford University Press（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抗菌薬の個別薬剤の国内の承認・保険適用は未確認である。切開排膿の適応は出典ガイドライン本文の推奨に基づく。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-086 (id: JlvnljE)'
    kokushi: 医学各論 Ⅲ-3-J-①（せつ、癰、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-026
  domain: SD
  subdomain: 蜂巣炎<蜂窩織炎>
  assertion:
    plain_statement_ja: 蜂窩織炎は真皮深層と皮下組織の感染症で、拡大する発赤、熱感、圧痛、腫脹を呈する。診断は主に病歴と身体所見に基づいて行われ、類似した外観を呈する疾患が多い。原因菌が同定できるのは約15%で、その多くはβ溶血性レンサ球菌と黄色ブドウ球菌である。米国では年間約1,450万件が発生すると推定されている。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1181
    source: 'Raff AB, Kroshinsky D. Cellulitis: A Review. JAMA. 2016;316(3):325-337.'
    doi: 10.1001/jama.2016.8825
    pmid: '27434444'
    pmcid: null
    url: https://doi.org/10.1001/jama.2016.8825
    source_license: © American Medical Association（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 原因菌が同定できる割合（約15%）と米国の発生件数は出典の抄録に記載された値である。治療の詳細は別カード（SD-027、SD-028）に分け、本カードは診断に絞った。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-090 (id: Jlvnljk)'
    kokushi: 医学各論 Ⅲ-3-J-②（蜂巣炎<蜂窩織炎>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-027
  domain: SD
  subdomain: 蜂巣炎<蜂窩織炎>
  assertion:
    plain_statement_ja: 厚生労働省「抗微生物薬適正使用の手引き」第四版（医科・外来編）では、蜂窩織炎など深部に及ぶ皮膚軟部組織感染症に対して第1世代セファロスポリン系抗菌薬による経口治療が推奨され、重症の場合は入院の上、静注抗菌薬による治療を考慮するとされる。蜂窩織炎の治療期間は5日間程度が目安とされ、経口投与と静脈内投与で臨床的治療成功率に有意差はない。初期治療では原則として抗 MRSA 薬の投与は行わず、改善しない場合に MRSA を考慮して治療を変更する。
    condition:
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1182
    source: 厚生労働省. 抗微生物薬適正使用の手引き 第四版 医科・外来編. 2026.
    doi: null
    pmid: null
    pmcid: null
    url: https://www.mhlw.go.jp/content/10900000/001630903.pdf
    source_license: 政府刊行物（厚生労働省）
    legal_basis: B
    source_class: GOV_JP
    corroboration: null
  uncertainty: 治療期間（5日間程度）は手引き第四版・医科・外来編の本文から読み取った。セファレキシンは国内で承認・販売されている薬剤である（手引きの薬剤一覧に国内商品名の記載あり）。一方、手引きでは ST 合剤の皮膚軟部組織感染症への使用は国内の電子添文上の適応に含まれない適応外使用であることが明記されている。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-090 (id: Jlvnljk)'
    kokushi: 医学各論 Ⅲ-3-J-②（蜂巣炎<蜂窩織炎>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-028
  domain: SD
  subdomain: 蜂巣炎<蜂窩織炎>
  assertion:
    plain_statement_ja: 米国の IDSA 皮膚・軟部組織感染症ガイドライン（2014年版）では、蜂窩織炎を含む皮膚軟部組織感染症について、膿を伴う化膿性かどうかで病態を分け、経験的治療は想定される原因菌（レンサ球菌、メチシリン感受性黄色ブドウ球菌、MRSA など）をカバーするよう選択し、重症度に応じて入院治療や静注抗菌薬の要否を判断する枠組みが示されている。迅速な診断と原因菌の推定、時機を逃さない有効な治療の開始が重視される。
    condition:
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1180
    source: 'Stevens DL, Bisno AL, Chambers HF, et al. Practice guidelines for the diagnosis and management of skin and soft tissue infections: 2014 update by the Infectious Diseases Society of America. Clin Infect Dis. 2014;59(2):147-159.'
    doi: 10.1093/cid/ciu296
    pmid: '24947530'
    pmcid: null
    url: https://doi.org/10.1093/cid/ciu296
    source_license: © The Author 2014, Oxford University Press（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 米国ガイドラインに基づく記載であり、日本の薬剤選択や用量とは限らない。個別薬剤の国内の承認・保険適用は未確認である。推奨の強さの個別表記は抄録の範囲を超えるため含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-090 (id: Jlvnljk)'
    kokushi: 医学各論 Ⅲ-3-J-②（蜂巣炎<蜂窩織炎>、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-029
  domain: SD
  subdomain: ひょう疽
  assertion:
    plain_statement_ja: ひょう疽は指尖腹側の閉鎖された区画（指腹）内に生じる感染症で、腫脹により強い拍動性疼痛を来す。浮腫と膿の貯留による圧迫で周囲組織の血流が妨げられ虚血に陥る危険があり、長期化すると骨・関節・腱へ感染が波及する。切開排膿と抗菌薬による速やかな治療を行わないと、組織の破壊や感染の拡大、全身状態の悪化を来し得る。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1183
    source: 'Nardi NM, McDonald EJ, Syed HA, Schaefer TJ. Felon. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2024.'
    doi: null
    pmid: '28613683'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/28613683/
    source_license: © 2024 StatPearls Publishing LLC
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典は StatPearls の章で、DOI は付与されていない（PubMed レコードで確認）。原因菌の内訳や抗菌薬の個別薬剤・国内の承認状況は出典の抄録の範囲を超えるため含めていない。本カードは二次資料経由（StatPearls）である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-J-③（ひょう疽、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-030
  domain: SD
  subdomain: 丹毒
  assertion:
    plain_statement_ja: 丹毒は真皮の浅層と表在リンパ管に限局する皮膚感染症で、主に A 群β溶血性レンサ球菌が原因となり、周囲の正常皮膚との境界が明瞭で隆起した発赤、熱感、疼痛を呈する。治療の基本はレンサ球菌に有効なβラクタム系抗菌薬であり、皮膚軟部組織感染症のガイドラインでは蜂窩織炎と並ぶ代表的な病態として位置づけられる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1180
    source: 'Stevens DL, Bisno AL, Chambers HF, et al. Practice guidelines for the diagnosis and management of skin and soft tissue infections: 2014 update by the Infectious Diseases Society of America. Clin Infect Dis. 2014;59(2):147-159.'
    doi: 10.1093/cid/ciu296
    pmid: '24947530'
    pmcid: null
    url: https://doi.org/10.1093/cid/ciu296
    source_license: © The Author 2014, Oxford University Press（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 抗菌薬の個別薬剤の国内の承認・保険適用は未確認である。境界明瞭という所見の対比（蜂窩織炎では境界が不明瞭）は皮膚感染症の深さによる分類に基づく一般的な整理である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-088 (id: JlvnljY)'
    kokushi: 医学各論 Ⅲ-3-J-④（丹毒、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-031
  domain: SD
  subdomain: 伝染性膿痂疹
  assertion:
    plain_statement_ja: 伝染性膿痂疹は小児に多い表在性の細菌性皮膚感染症である。システマティックレビューでは、外用抗菌薬はプラセボより治癒率が高く（統合リスク比 2.24、95%信頼区間 1.61〜3.13）、ムピロシン外用とフシジン酸外用は同等の効果で、経口治療と同等かそれ以上の効果が示された。一方、消毒薬による処置の有効性を支持する根拠は乏しく、ペニシリンは他の多くの抗菌薬より効果が劣っていた。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1184
    source: Koning S, van der Sande R, Verhagen AP, et al. Interventions for impetigo. Cochrane Database Syst Rev. 2012;(1):CD003261.
    doi: 10.1002/14651858.CD003261.pub3
    pmid: '22258953'
    pmcid: PMC7025440
    url: https://doi.org/10.1002/14651858.CD003261.pub3
    source_license: © The Cochrane Collaboration（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値は出典の抄録に記載された統合リスク比である。ムピロシンやフシジン酸など個別の外用薬の国内の承認・保険適用は未確認である。広範囲な膿痂疹で外用と経口のどちらが優れるかは出典でも結論が出ていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-085 (id: JlvnljA)'
    kokushi: 医学各論 Ⅲ-3-J-⑤（伝染性膿痂疹、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-032
  domain: SD
  subdomain: ブドウ球菌性熱傷様皮膚症候群
  assertion:
    plain_statement_ja: ブドウ球菌性熱傷様皮膚症候群（SSSS）は、黄色ブドウ球菌が産生する表皮剥脱性毒素が血行性に広がって生じる疾患で、毒素はデスモグレイン1だけを切断するセリンプロテアーゼであり、表皮は顆粒層のレベルで剥離する。新生児に多く、びまん性紅斑と発熱をもって急性に発症する。診断は皮膚生検（迅速凍結標本）で確認でき、中毒性表皮壊死症との鑑別が重要である。死亡率は小児で10%未満だが、成人では抗菌薬治療を行っても40〜63%と高い。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1185
    source: 'Handler MZ, Schwartz RA. Staphylococcal scalded skin syndrome: diagnosis and management in children and adults. J Eur Acad Dermatol Venereol. 2014;28(11):1418-1423.'
    doi: 10.1111/jdv.12541
    pmid: '24841497'
    pmcid: null
    url: https://doi.org/10.1111/jdv.12541
    source_license: © European Academy of Dermatology and Venereology（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 死亡率の数値は出典の抄録に記載された値である。抗菌薬の個別薬剤の国内の承認・保険適用は未確認である。免疫グロブリン療法については入院期間の延長と関連するとの報告が出典で紹介されており、推奨として記載していない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-089 (id: Jlvnljg)'
    kokushi: 医学各論 Ⅲ-3-J-⑥（ブドウ球菌性熱傷様皮膚症候群、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-033
  domain: SD
  subdomain: 壊死性筋膜炎
  assertion:
    plain_statement_ja: 壊死性筋膜炎は、皮下組織から筋膜に沿って急速に進展する壊死性の軟部組織感染症で、複数の菌による多菌性のものと、A 群レンサ球菌など単一菌によるものとがある。強い疼痛や急速な全身状態の悪化を伴い、治療の要は早期の外科的デブリードマンと広域抗菌薬の併用であり、介入の遅れが死亡率を押し上げる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1186
    source: Stevens DL, Bryant AE. Necrotizing Soft-Tissue Infections. N Engl J Med. 2017;377(23):2253-2265.
    doi: 10.1056/NEJMra1600673
    pmid: '29211672'
    pmcid: null
    url: https://doi.org/10.1056/NEJMra1600673
    source_license: © Massachusetts Medical Society（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典（NEJM 総説）の抄録本文は PubMed に収載されておらず、主張は同総説が扱う壊死性軟部組織感染症の分類と治療の骨子に限定した。個別の抗菌薬レジメンや国内の承認・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-091 (id: Jlvnljs)'
    kokushi: 医学各論 Ⅲ-3-J-⑦（壊死性筋膜炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-034
  domain: SD
  subdomain: ガス壊疽
  assertion:
    plain_statement_ja: ガス壊疽は、ウェルシュ菌（Clostridium perfringens）をはじめとするクロストリジウム属による筋壊死（クロストリジウム性筋壊死）で、壊死性軟部組織感染症の一型である。外傷や手術創などから菌が侵入し、急速な筋壊死とガス産生、強い全身毒性を来す。治療は緊急の外科的デブリードマン（壊死組織の切除）と抗菌薬の併用が中心となる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1186
    source: Stevens DL, Bryant AE. Necrotizing Soft-Tissue Infections. N Engl J Med. 2017;377(23):2253-2265.
    doi: 10.1056/NEJMra1600673
    pmid: '29211672'
    pmcid: null
    url: https://doi.org/10.1056/NEJMra1600673
    source_license: © Massachusetts Medical Society（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典（NEJM 総説）の抄録本文は PubMed に収載されておらず、主張は同総説が扱うクロストリジウム性筋壊死の位置づけと治療の骨子に限定した。抗菌薬の個別薬剤の国内の承認・保険適用は未確認である。高圧酸素療法の位置づけは出典の抄録範囲で確認できないため含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-J-⑧（ガス壊疽、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-035
  domain: SD
  subdomain: 非結核性抗酸菌症
  assertion:
    plain_statement_ja: 皮膚の非結核性抗酸菌症では、Mycobacterium marinum がリンパ管に沿って並ぶ結節（スポロトリコイド型）を生じる代表的な原因菌であり、高度の免疫不全では M. kansasii、M. avium-intracellulare complex、M. haemophilum などが皮膚・播種性病変を来す。M. abscessus 群、M. chelonae、M. fortuitum などの迅速発育菌は、美容・外科処置に関連する皮膚感染症の原因として認識が増えている。診断の要は皮膚生検による抗酸菌染色と培養であり、菌種の同定が抗菌薬選択の前提になる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1187
    source: Franco-Paredes C, Marcos LA, Henao-Martínez AF, et al. Cutaneous Mycobacterial Infections. Clin Microbiol Rev. 2019;32(1):e00069-18.
    doi: 10.1128/CMR.00069-18
    pmid: '30429139'
    pmcid: PMC6302357
    url: https://doi.org/10.1128/CMR.00069-18
    source_license: © American Society for Microbiology（Crossref のライセンスは non-commercial TDM のみで CC 表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 菌種ごとの抗菌薬レジメンは出典で公式ガイドラインの参照とされており、本カードには含めていない。個別薬剤の国内の承認・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-093 (id: Jlvnlj4)'
    kokushi: 医学各論 Ⅲ-3-K-①（非結核性抗酸菌症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-036
  domain: SD
  subdomain: 尋常性狼瘡
  assertion:
    plain_statement_ja: 尋常性狼瘡は皮膚結核の代表的な病型の一つである。皮膚結核は、結核菌の外からの接種や、他部位の病巣からの播種など、感染の経路によって多彩な臨床病型をとり、病理組織学的所見と抗酸菌の証明（染色・培養・分子検査）が診断の助けになる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1187
    source: Franco-Paredes C, Marcos LA, Henao-Martínez AF, et al. Cutaneous Mycobacterial Infections. Clin Microbiol Rev. 2019;32(1):e00069-18.
    doi: 10.1128/CMR.00069-18
    pmid: '30429139'
    pmcid: PMC6302357
    url: https://doi.org/10.1128/CMR.00069-18
    source_license: © American Society for Microbiology（Crossref のライセンスは non-commercial TDM のみで CC 表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 尋常性狼瘡に固有の臨床所見の詳細は出典の抄録に明記されていないため、皮膚結核全体の分類と診断の枠組みに留めた。抗結核薬の個別レジメンは本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-093 (id: Jlvnlj4)'
    kokushi: 医学各論 Ⅲ-3-K-②（尋常性狼瘡、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-037
  domain: SD
  subdomain: 皮膚腺病、硬結性紅斑
  assertion:
    plain_statement_ja: 結核菌感染に伴う皮膚病変には、菌そのものが皮膚に侵入・播種して生じる病変のほか、感染に対する過敏反応として生じる病変（結核疹）がある。硬結性紅斑は過敏反応による病変に位置づけられ、皮膚腺病はリンパ節結核が拡大して皮膚へ穿破した病態である。皮膚生検の病理組織所見が、これらの病変の切り分けに役立つ。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1187
    source: Franco-Paredes C, Marcos LA, Henao-Martínez AF, et al. Cutaneous Mycobacterial Infections. Clin Microbiol Rev. 2019;32(1):e00069-18.
    doi: 10.1128/CMR.00069-18
    pmid: '30429139'
    pmcid: PMC6302357
    url: https://doi.org/10.1128/CMR.00069-18
    source_license: © American Society for Microbiology（Crossref のライセンスは non-commercial TDM のみで CC 表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 各病変の頻度や治療レジメンは出典の抄録の範囲を超えるため含めていない。皮膚腺病と硬結性紅斑の対応づけは出典の皮膚結核の分類（直接感染による病型と過敏反応による病型）に基づく。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-093 (id: Jlvnlj4)'
    kokushi: 医学各論 Ⅲ-3-K-③（皮膚腺病、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-038
  domain: SD
  subdomain: 白癬、カンジダ症
  assertion:
    plain_statement_ja: 白癬（皮膚糸状菌症）は侵される部位によって分類され、体部白癬と頭部白癬は思春期前の小児に多く、股部白癬、足白癬、爪白癬（爪真菌症の最多の型）は思春期以降に多い。臨床所見だけでは湿疹や乾癬など他の疾患と紛らわしく診断が不確実なことがあるため、検査による確認が望ましい。近年出現している新興の白癬は重症化しやすく、専門的な診断検査を要することがある。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1188
    source: Caplan AS, Gold JAW, Smith DJ, Ely JW. Diagnosis and Management of Tinea Infections. Am Fam Physician. 2025;112(4):382-392.
    doi: null
    pmid: '41118183'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/41118183/
    source_license: © American Academy of Family Physicians（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典（Am Fam Physician の総説）は DOI が付与されていない（PubMed レコードで確認）。同総説の主対象は皮膚糸状菌症であり、カンジダ症の診断手順の詳細はその範囲外のため本カードには含めていない。KOH 直接鏡検などの個別検査の感度の数値は出典の抄録に記載がなく含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-092 (id: Jlvnljw)'
    kokushi: 医学各論 Ⅲ-3-L-①（白癬、カンジダ症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-039
  domain: SD
  subdomain: 白癬、カンジダ症
  assertion:
    plain_statement_ja: 体部白癬、股部白癬、足白癬は通常、安価な外用抗真菌薬に反応する。広範囲な病変、外用で改善しない場合、免疫不全がある場合、頭部白癬のように毛包への波及がある場合には経口抗真菌薬が適応となる。経口テルビナフィンは忍容性と有効性から頭部白癬と爪真菌症の第一選択とされる。抗真菌薬と副腎皮質ステロイドの合剤は使用を避けることが、抗真菌薬スチュワードシップとして求められる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1188
    source: Caplan AS, Gold JAW, Smith DJ, Ely JW. Diagnosis and Management of Tinea Infections. Am Fam Physician. 2025;112(4):382-392.
    doi: null
    pmid: '41118183'
    pmcid: null
    url: https://pubmed.ncbi.nlm.nih.gov/41118183/
    source_license: © American Academy of Family Physicians（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典は DOI が付与されていない（PubMed レコードで確認）。テルビナフィンなど個別薬剤の国内の承認・保険適用は未確認である。カンジダ症の治療の詳細は出典の主対象の範囲外のため含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-092 (id: Jlvnljw)'
    kokushi: 医学各論 Ⅲ-3-L-①（白癬、カンジダ症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-040
  domain: SD
  subdomain: 癜風
  assertion:
    plain_statement_ja: 癜風は Malassezia 属（主に M. globosa、M. furfur、M. sympodialis）による表在性真菌症で、体幹上部、頸部、上腕に、鱗屑を伴う色素脱失斑または色素沈着斑を生じる。診断は特徴的な臨床像によることが多く、必要に応じ KOH 標本で、胞子の集簇に混じる多数の短い菌糸を確認する。治療は安全性と費用の面から外用抗真菌薬が第一選択で、経口抗真菌薬は広範囲、頻回再発、難治の場合に用い、再発を繰り返す場合は間欠的な予防投与を考慮する。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1189
    source: 'Leung AKC, Barankin B, Lam JM, Leong KF, Hon KL. Tinea versicolor: an updated review. Drugs Context. 2022;11:2022-9-2.'
    doi: 10.7573/dic.2022-9-2
    pmid: '36452877'
    pmcid: PMC9677953
    url: https://doi.org/10.7573/dic.2022-9-2
    source_license: CC BY-NC-ND 4.0
    legal_basis: B
    source_class: RESTRICTED
    corroboration: null
  uncertainty: 個別の抗真菌薬の国内の承認・保険適用は未確認である。色素異常が治癒後も残る期間などの詳細は出典の抄録の範囲を超えるため含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-092 (id: Jlvnljw)'
    kokushi: 医学各論 Ⅲ-3-L-②（癜風、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-041
  domain: SD
  subdomain: スポロトリコーシス
  assertion:
    plain_statement_ja: スポロトリコーシスは二形性真菌 Sporothrix schenckii による感染症で、菌に汚染された土壌、植物、有機物の外傷性接種によって感染し、花卉栽培や農業などの作業との関連が知られる。病変は通常、皮膚、皮下組織と近傍のリンパ管に限局する。診断のゴールドスタンダードは培養であり、ヒトとネコのいずれでも第一選択の治療はイトラコナゾールである。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1190
    source: Barros MBL, de Almeida Paes R, Schubach AO. Sporothrix schenckii and Sporotrichosis. Clin Microbiol Rev. 2011;24(4):633-654.
    doi: 10.1128/CMR.00007-11
    pmid: '21976602'
    pmcid: PMC3194828
    url: https://doi.org/10.1128/CMR.00007-11
    source_license: © American Society for Microbiology（Crossref のライセンスは non-commercial TDM のみで CC 表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: イトラコナゾールの国内の承認・保険適用は未確認である。用量と投与期間は出典の抄録に記載がなく含めていない。ネコを介する流行はブラジルでの報告が中心であり、日本の疫学とは限らない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-L-③（スポロトリコーシス、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-042
  domain: SD
  subdomain: 疥癬
  assertion:
    plain_statement_ja: 疥癬はヒト疥癬ダニの感染による疾患で、日本皮膚科学会の疥癬診療ガイドライン第3版は診断基準、通常疥癬と角化型疥癬の治療アルゴリズム、予防をまとめたものである。フェノトリン外用が2014年8月に保険適用となったことを受けて改訂され、通常疥癬の第一選択はフェノトリンローションの外用またはイベルメクチンの内服、第二選択はイオウ含有軟膏、クロタミトンクリーム、安息香酸ベンジルローションとされた。γ-BHC軟膏は臨床使用されなくなった。
    condition:
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1191
    source: 'Ishii N, Asai T, Asahina A, Ishiko A, et al. Guideline for the diagnosis and treatment of scabies in Japan (third edition): Executive Committee of Guideline for the Diagnosis and Treatment of Scabies. J Dermatol. 2017;44(9):991-1014.'
    doi: 10.1111/1346-8138.13896
    pmid: '28561292'
    pmcid: null
    url: https://doi.org/10.1111/1346-8138.13896
    source_license: © Japanese Dermatological Association（Wiley、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: フェノトリン外用が2014年8月に国内で保険適用となったことは出典（ガイドライン要約）の記載で確認した。イベルメクチンなど、その他の薬剤の国内の承認・保険適用の個別確認はしていない。診断基準の細目は要約版の範囲を超えるため本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-094 (id: Jlvnlj8)'
    kokushi: 医学各論 Ⅲ-3-M-①（疥癬、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-043
  domain: SD
  subdomain: 疥癬
  assertion:
    plain_statement_ja: 疥癬の集団発生対策では、早期の診断確定と予防が要点となる。日本皮膚科学会の疥癬診療ガイドライン第3版は、診断と治療に加えて予防（prevention）を扱う項目を含んでいる。角化型（過角化型）疥癬は免疫抑制状態の患者に生じ、多数のダニを持つため集団発生の起点となりやすく、施設等では通常疥癬とは分けて治療アルゴリズムに沿った対応と接触者の評価が必要になる。
    condition:
      region: 日本
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1191
    source: 'Ishii N, Asai T, Asahina A, Ishiko A, et al. Guideline for the diagnosis and treatment of scabies in Japan (third edition): Executive Committee of Guideline for the Diagnosis and Treatment of Scabies. J Dermatol. 2017;44(9):991-1014.'
    doi: 10.1111/1346-8138.13896
    pmid: '28561292'
    pmcid: null
    url: https://doi.org/10.1111/1346-8138.13896
    source_license: © Japanese Dermatological Association（Wiley、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 集団発生時の接触者への一斉治療の範囲や環境対策など、具体的な運用手順の詳細は本ガイドライン要約版の抄録の範囲では確認できず、本カードには含めていない。補完候補として、高齢者施設での集団発生管理を扱った White LCJ らのレビュー（Epidemiol Infect. 2016、PMID 27734781、DOI 10.1017/S0950268816001746）がある。本カードでは個別の薬剤名は挙げていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-094 (id: Jlvnlj8)'
    kokushi: 医学各論 Ⅲ-3-M-①（疥癬、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-044
  domain: SD
  subdomain: 単純ヘルペス
  assertion:
    plain_statement_ja: 単純ヘルペスウイルス（HSV）感染症は一般人口の中に大きな感染源のプールを持つ伝染性の感染症で、口唇や性器などの粘膜皮膚病変を繰り返し来す。免疫抑制状態の宿主では重篤な合併症を生じうる。Fatahzadeh と Schwartz の総説は、粘膜皮膚の HSV 感染症について疫学、病因、症状、診断の特徴と管理の方策をまとめている。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1192
    source: 'Fatahzadeh M, Schwartz RA. Human herpes simplex virus infections: epidemiology, pathogenesis, symptomatology, diagnosis, and management. J Am Acad Dermatol. 2007;57(5):737-763.'
    doi: 10.1016/j.jaad.2007.06.027
    pmid: '17939933'
    pmcid: null
    url: https://doi.org/10.1016/j.jaad.2007.06.027
    source_license: © American Academy of Dermatology（Elsevier、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードは総説の抄録で確認できる範囲の定性的な記述に限った。治療に用いられる抗ウイルス薬（アシクロビル、バラシクロビル等）の国内の承認・保険適用は未確認である。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-096 (id: JlvnlkE)'
    kokushi: 医学各論 Ⅲ-3-N-①（単純ヘルペス、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-045
  domain: SD
  subdomain: カポジ水痘様発疹症
  assertion:
    plain_statement_ja: カポジ水痘様発疹症（eczema herpeticum）は、炎症のある皮膚、とくにアトピー性皮膚炎の湿疹病変に単純ヘルペスウイルスが広範に感染した状態である。湿疹病変に一致して単調な形態のドーム状の水疱と膿疱が多発し、重い全身症状を伴うことで臨床診断される。Wollenberg らの100例の後方視的解析では、発熱とリンパ球減少が本症に関連する所見として示された。
    condition:
      region: 国際
      study: 後方視的症例解析（100例）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1193
    source: 'Wollenberg A, Zoch C, Wetzel S, Plewig G, et al. Predisposing factors and clinical features of eczema herpeticum: a retrospective analysis of 100 cases. J Am Acad Dermatol. 2003;49(2):198-205.'
    doi: 10.1067/s0190-9622(03)00896-x
    pmid: '12894065'
    pmcid: null
    url: https://doi.org/10.1067/s0190-9622(03)00896-x
    source_license: © American Academy of Dermatology（Elsevier、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 数値（100例）は出典の抄録で確認した対象数であり、発症頻度などの母集団に対する割合は出典にないため記載していない。治療の詳細は本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-096 (id: JlvnlkE)'
    kokushi: 医学各論 Ⅲ-3-N-②（カポジ水痘様発疹症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-046
  domain: SD
  subdomain: 尋常性疣贅
  assertion:
    plain_statement_ja: 尋常性疣贅をはじめとする皮膚の疣贅は、ヒト乳頭腫ウイルス（HPV）の感染による良性の角化性病変であり、自然に消退することも多い。英国皮膚科医協会（British Association of Dermatologists）の2014年のガイドラインは、皮膚疣贅の管理について、外用療法や凍結療法を含む治療選択肢とその使い分けをまとめている。
    condition:
      region: 英国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1194
    source: Sterling JC, Gibbs S, Haque Hussain SS, Mohd Mustapa MF, et al. British Association of Dermatologists' guidelines for the management of cutaneous warts 2014. Br J Dermatol. 2014;171(4):696-712.
    doi: 10.1111/bjd.13310
    pmid: '25273231'
    pmcid: null
    url: https://doi.org/10.1111/bjd.13310
    source_license: © British Association of Dermatologists（Wiley、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本ガイドラインの抄録は PubMed に収載されておらず、本文の個別の推奨の強さは確認していないため、本カードの記述はガイドラインの対象範囲に基づく定性的な内容に限った。個別の薬剤名は挙げていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-098 (id: JlvnlkQ)'
    kokushi: 医学各論 Ⅲ-3-N-③（尋常性疣贅、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-047
  domain: SD
  subdomain: 尋常性痤瘡、酒皶様皮膚炎
  assertion:
    plain_statement_ja: 尋常性痤瘡は思春期以降に広くみられる疾患で、米国皮膚科学会の診療ガイドライン（2024年）は、過酸化ベンゾイル、外用レチノイド、外用抗菌薬、ドキシサイクリン内服を強い推奨とし、重症で瘢痕を残すものや標準治療に反応しないものにはイソトレチノイン内服を強く推奨している。作用機序の異なる外用薬の併用と、全身性抗菌薬の使用を抑えることも推奨の要点である。酒皶様皮膚炎は、顔面へのステロイド外用などを契機に痤瘡様・酒皶様の変化を生じる病態を指す。
    condition:
      region: 米国
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1195
    source: Reynolds RV, Yeung H, Cheng CE, Cook-Bolden F, et al. Guidelines of care for the management of acne vulgaris. J Am Acad Dermatol. 2024;90(5):1006.e1-1006.e30.
    doi: 10.1016/j.jaad.2023.12.017
    pmid: '38300170'
    pmcid: null
    url: https://doi.org/10.1016/j.jaad.2023.12.017
    source_license: © American Academy of Dermatology（Elsevier、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本ガイドラインは米国における痤瘡の管理を対象としており、本文に名前の出る薬剤（イソトレチノイン、ドキシサイクリン、過酸化ベンゾイル、外用レチノイド等）の国内の承認・保険適用は未確認である。酒皶様皮膚炎は本ガイドラインの対象外のため、その部分は定義的な記述に限った。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)；TBL-01-00-110 (id: Jlvnll4)；TBL-01-00-111 (id: JlvnlmA)'
    kokushi: 医学各論 Ⅲ-3-O-①（尋常性痤瘡、酒皶様皮膚炎、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-048
  domain: SD
  subdomain: 円形脱毛症
  assertion:
    plain_statement_ja: 円形脱毛症は、瘢痕を残さない炎症性の脱毛症である。小さく境界明瞭な脱毛斑から、頭髪と体毛のすべてが失われるものまで病像の幅が大きい。病因は完全には解明されていないが、毛包の免疫特権の喪失と自己免疫による毛包の破壊、炎症経路の亢進が関与すると考えられている。経過は予測しがたく確立した根治療法はなく、心理的苦痛や自尊心の低下、精神科的併存症を伴いやすいことが知られている。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1196
    source: 'Strazzulla LC, Wang EHC, Avila L, Lo Sicco K, et al. Alopecia areata: Disease characteristics, clinical evaluation, and new perspectives on pathogenesis. J Am Acad Dermatol. 2018;78(1):1-12.'
    doi: 10.1016/j.jaad.2017.04.1141
    pmid: '29241771'
    pmcid: null
    url: https://doi.org/10.1016/j.jaad.2017.04.1141
    source_license: © American Academy of Dermatology（Elsevier、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 本カードは2部構成の総説の第1部（疾患の特徴、臨床評価、病因）の抄録で確認できる範囲に基づく。個別の治療薬の有効性の評価は第2部の範囲であり、本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-P-①（円形脱毛症、a）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-049
  domain: SD
  subdomain: 環状肉芽腫
  assertion:
    plain_statement_ja: 環状肉芽腫は良性の炎症性皮膚疾患で、悪性腫瘍、外傷、甲状腺疾患、糖尿病、HIV感染など多くの病態との関連が報告されている。臨床病型には限局型、汎発型、皮下型、穿孔型、斑状型がある。限局型は一般に2年以内に自然消退する一方、汎発型は慢性に経過し治療に反応しにくい。治療については小規模な症例報告や後方視研究が中心で、確立した標準治療（ゴールドスタンダード）はまだない。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1197
    source: 'Wang J, Khachemoune A. Granuloma Annulare: A Focused Review of Therapeutic Options. Am J Clin Dermatol. 2018;19(3):333-344.'
    doi: 10.1007/s40257-017-0334-5
    pmid: '29230666'
    pmcid: null
    url: https://doi.org/10.1007/s40257-017-0334-5
    source_license: © Springer（CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 自然消退までの期間（2年以内）は出典の抄録の記載に基づく。個別の治療法の有効性の比較は出典でも結論が出ておらず、本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-Q-①（環状肉芽腫、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-050
  domain: SD
  subdomain: 浮腫性硬化症
  assertion:
    plain_statement_ja: 浮腫性硬化症（scleroedema adultorum Buschke）はまれな皮膚疾患で、呼吸器感染に続発する古典的病型、感染と関連しない病型、糖尿病に伴う病型の3病型に分けられる。皮膚の肥厚と硬化が特徴で、典型的には頸部から始まる。約半数の患者では自然寛解がみられる。治療は症例報告や小規模な後方視研究に基づくものが中心で、外用・全身療法や物理療法が試みられてきたが、確立した治療はない。
    condition:
      region: 国際
      study: 系統的レビュー（1970〜2016年の報告）
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1198
    source: 'Miguel D, Schliemann S, Elsner P. Treatment of Scleroedema Adultorum Buschke: A Systematic Review. Acta Derm Venereol. 2018;98(3):305-309.'
    doi: 10.2340/00015555-2846
    pmid: '29136263'
    pmcid: null
    url: https://doi.org/10.2340/00015555-2846
    source_license: © Society for Publication of Acta Dermato-Venereologica（CC表示を確認できず）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 自然寛解の割合（約半数）は出典の抄録の記載に基づく。個別の治療法ごとの成績は出典でも多くが不成功の報告であり、本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-R-①（浮腫性硬化症、b）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
- id: SD-051
  domain: SD
  subdomain: 脛骨前粘液水腫、アミロイド苔癬
  assertion:
    plain_statement_ja: 脛骨前粘液水腫（甲状腺皮膚症）は Graves 病の自己免疫性の皮膚病変で、橋本病でもまれに起こる。病変は通常は無症状で美容上の問題にとどまるが、進行した病型は象皮症や甲状腺先端症（アクロパチー）と関連する。ほぼすべての症例に比較的重い眼症を伴い（眼症が先行することが多い）、血中の TSH 受容体抗体が高値である。結合組織の線維芽細胞が刺激されてグリコサミノグリカンが大量に産生されることが病態の中心と考えられている。アミロイド苔癬は、脛骨前などに痒みの強い苔癬様丘疹を生じ、真皮乳頭部へのアミロイド沈着を特徴とする疾患で、同じ部位に生じる病変として鑑別に挙がる。
    condition:
      region: 国際
    differential: null
    common_misconception: null
  provenance:
    source_ref: SRC-1199
    source: 'Fatourechi V. Pretibial myxedema: pathophysiology and treatment options. Am J Clin Dermatol. 2005;6(5):295-309.'
    doi: 10.2165/00128071-200506050-00003
    pmid: '16252929'
    pmcid: null
    url: https://doi.org/10.2165/00128071-200506050-00003
    source_license: © Adis（Springer、CC表示なし）
    legal_basis: B
    source_class: UNKNOWN
    corroboration: null
  uncertainty: 出典は脛骨前粘液水腫の総説であり、アミロイド苔癬についての記述は出典の範囲外であるため、定義的な内容にとどめ、数値は入れていない。脛骨前粘液水腫の治療選択肢の詳細は本カードには含めていない。
  curriculum:
    core_curriculum: 'PS-02-04-05 (id: JkxnuQI)'
    kokushi: 医学各論 Ⅲ-3-R-②（脛骨前粘液水腫、c）
  publication_info:
    created: '2026-10-28'
    verifier: null
    verified_at: null
    status: draft
```

## 3. カリキュラム対応の一覧

| カード | 出題基準 | コアカリ |
|---|---|---|
| HX-001 | null | PS-02-04-02 (id: JkxnuP8)；TBL-02-03-004 (id: JlAKpaY)；TBL-02-03-005 (id: JlAKpac) |
| HX-002 | null | PS-02-04-03 (id: JkxnuQA)；TBL-02-03-011 (id: JlAKpa0) |
| HX-003 | null | PS-02-04-03 (id: JkxnuQA)；TBL-02-03-009 (id: JlAKpas) |
| HX-004 | null | PS-02-04-03 (id: JkxnuQA)；TBL-02-03-008 (id: JlAKpao) |
| HX-005 | null | PS-02-04-03 (id: JkxnuQA)；TBL-02-03-010 (id: JlAKpaw) |
| HX-006 | null | PS-02-04-02 (id: JkxnuP8)；TBL-02-03-005 (id: JlAKpac) |
| HX-007 | null | PS-02-15-02 (id: JkxnuTI)；TBL-02-14-008 (id: JlAKpuM)；TBL-02-14-014 (id: JlAKpuk)；TBL-02-14-017 (id: JlAKpuw)；TBL-02-14-018 (id: JlAKpu0) |
| HX-008 | null | PS-02-15-03 (id: JkxnuTM)；TBL-02-15-023 (id: JlAKpxM) |
| HX-009 | null | PS-02-15-03 (id: JkxnuTM)；TBL-02-15-007 (id: JlAKpwM)；TBL-02-15-010 (id: JlAKpwY) |
| HX-010 | null | PS-02-15-03 (id: JkxnuTM)；TBL-02-15-011 (id: JlAKpwc) |
| HX-011 | null | PS-02-15-03 (id: JkxnuTM)；TBL-02-15-012 (id: JlAKpwg)；TBL-02-15-014 (id: JlAKpwo) |
| HX-012 | null | PS-02-15-03 (id: JkxnuTM) |
| SD-001 | 医学各論 Ⅲ-3-A-①（Hailey-Hailey病、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-002 | 医学各論 Ⅲ-3-A-②（先天性表皮水疱症、c） | PS-02-04-05 (id: JkxnuQI) |
| SD-003 | 医学各論 Ⅲ-3-B-①（天疱瘡、a） | PS-02-04-05 (id: JkxnuQI) |
| SD-004 | 医学各論 Ⅲ-3-B-①（天疱瘡、a） | PS-02-04-05 (id: JkxnuQI) |
| SD-005 | 医学各論 Ⅲ-3-B-②（水疱性類天疱瘡、a） | PS-02-04-05 (id: JkxnuQI) |
| SD-006 | 医学各論 Ⅲ-3-B-③（後天性表皮水疱症、c） | PS-02-04-05 (id: JkxnuQI) |
| SD-007 | 医学各論 Ⅲ-3-C-①（魚鱗癬、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-008 | 医学各論 Ⅲ-3-C-②（掌蹠角化症、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-009 | 医学各論 Ⅲ-3-C-③（Darier病、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-010 | 医学各論 Ⅲ-3-C-④（汗孔角化症、c） | PS-02-04-05 (id: JkxnuQI) |
| SD-011 | 医学各論 Ⅲ-3-D-①（乾癬、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-082 (id: Jlvnlio) |
| SD-012 | 医学各論 Ⅲ-3-D-①（乾癬、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-082 (id: Jlvnlio) |
| SD-013 | 医学各論 Ⅲ-3-D-①（乾癬、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-082 (id: Jlvnlio) |
| SD-014 | 医学各論 Ⅲ-3-D-②（扁平苔癬、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-083 (id: Jlvnlis) |
| SD-015 | 医学各論 Ⅲ-3-D-③（Gibertばら色粃糠疹、b） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-084 (id: Jlvnli0) |
| SD-016 | 医学各論 Ⅲ-3-D-④（類乾癬、c） | PS-02-04-05 (id: JkxnuQI) |
| SD-017 | 医学各論 Ⅲ-3-E-①（膿疱性乾癬、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-018 | 医学各論 Ⅲ-3-E-②（掌蹠膿疱症、b） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-081 (id: Jlvnlic) |
| SD-019 | 医学各論 Ⅲ-3-F-①（慢性光線性皮膚炎、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-020 | 医学各論 Ⅲ-3-G-①（尋常性白斑、b） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-115 (id: JlvnlmY) |
| SD-021 | 医学各論 Ⅲ-3-H-①（色素性乾皮症、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-022 | 医学各論 Ⅲ-3-H-②（弾性線維性仮性黄色腫、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-023 | 医学各論 Ⅲ-3-H-③（Werner症候群、c） | PS-02-04-05 (id: JkxnuQI) |
| SD-024 | 医学各論 Ⅲ-3-I-①（多汗症、無汗症、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-108 (id: Jlvnlls)；TBL-01-00-109 (id: Jlvnll0) |
| SD-025 | 医学各論 Ⅲ-3-J-①（せつ、癰、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-086 (id: JlvnljE) |
| SD-026 | 医学各論 Ⅲ-3-J-②（蜂巣炎<蜂窩織炎>、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-090 (id: Jlvnljk) |
| SD-027 | 医学各論 Ⅲ-3-J-②（蜂巣炎<蜂窩織炎>、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-090 (id: Jlvnljk) |
| SD-028 | 医学各論 Ⅲ-3-J-②（蜂巣炎<蜂窩織炎>、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-090 (id: Jlvnljk) |
| SD-029 | 医学各論 Ⅲ-3-J-③（ひょう疽、a） | PS-02-04-05 (id: JkxnuQI) |
| SD-030 | 医学各論 Ⅲ-3-J-④（丹毒、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-088 (id: JlvnljY) |
| SD-031 | 医学各論 Ⅲ-3-J-⑤（伝染性膿痂疹、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-085 (id: JlvnljA) |
| SD-032 | 医学各論 Ⅲ-3-J-⑥（ブドウ球菌性熱傷様皮膚症候群、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-089 (id: Jlvnljg) |
| SD-033 | 医学各論 Ⅲ-3-J-⑦（壊死性筋膜炎、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-091 (id: Jlvnljs) |
| SD-034 | 医学各論 Ⅲ-3-J-⑧（ガス壊疽、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-035 | 医学各論 Ⅲ-3-K-①（非結核性抗酸菌症、b） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-093 (id: Jlvnlj4) |
| SD-036 | 医学各論 Ⅲ-3-K-②（尋常性狼瘡、c） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-093 (id: Jlvnlj4) |
| SD-037 | 医学各論 Ⅲ-3-K-③（皮膚腺病、c） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-093 (id: Jlvnlj4) |
| SD-038 | 医学各論 Ⅲ-3-L-①（白癬、カンジダ症、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-092 (id: Jlvnljw) |
| SD-039 | 医学各論 Ⅲ-3-L-①（白癬、カンジダ症、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-092 (id: Jlvnljw) |
| SD-040 | 医学各論 Ⅲ-3-L-②（癜風、b） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-092 (id: Jlvnljw) |
| SD-041 | 医学各論 Ⅲ-3-L-③（スポロトリコーシス、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-042 | 医学各論 Ⅲ-3-M-①（疥癬、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-094 (id: Jlvnlj8) |
| SD-043 | 医学各論 Ⅲ-3-M-①（疥癬、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-094 (id: Jlvnlj8) |
| SD-044 | 医学各論 Ⅲ-3-N-①（単純ヘルペス、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-096 (id: JlvnlkE) |
| SD-045 | 医学各論 Ⅲ-3-N-②（カポジ水痘様発疹症、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-096 (id: JlvnlkE) |
| SD-046 | 医学各論 Ⅲ-3-N-③（尋常性疣贅、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-098 (id: JlvnlkQ) |
| SD-047 | 医学各論 Ⅲ-3-O-①（尋常性痤瘡、酒皶様皮膚炎、a） | PS-02-04-05 (id: JkxnuQI)；TBL-01-00-110 (id: Jlvnll4)；TBL-01-00-111 (id: JlvnlmA) |
| SD-048 | 医学各論 Ⅲ-3-P-①（円形脱毛症、a） | PS-02-04-05 (id: JkxnuQI) |
| SD-049 | 医学各論 Ⅲ-3-Q-①（環状肉芽腫、c） | PS-02-04-05 (id: JkxnuQI) |
| SD-050 | 医学各論 Ⅲ-3-R-①（浮腫性硬化症、b） | PS-02-04-05 (id: JkxnuQI) |
| SD-051 | 医学各論 Ⅲ-3-R-②（脛骨前粘液水腫、c） | PS-02-04-05 (id: JkxnuQI) |

## 4. 未解決事項

- ライセンス UNKNOWN の出典が複数ある（出版社・学会の著作権表示のみで CC 表示を確認できなかったもの）。SRC-1198（Acta Derm Venereol）はオープンアクセス誌だが本記事の CC 表示を確認できず UNKNOWN とした。取り込み側での再確認を希望する（担当：取り込み側）。
- 薬剤を含むカードの国内承認・保険適用は、確認できたもの（SD-027 の厚労省手引きに基づく記載、SD-043 など）は uncertainty に記載し、それ以外は「未確認」と明記した（担当：取り込み側）。
- SD-029（ひょう疽）は StatPearls の章が出典のまま残っている。一次資料への差し替え候補があれば次回以降のやり直し対象に加えられたい。
- SD-038・039 の出典は皮膚糸状菌症が主対象で、カンジダ症の診断・治療の詳細は範囲外。カンジダ症を主対象とする出典での補完が望ましい。
- SD-051 のアミロイド苔癬の部分は定義的な記述にとどまる。アミロイド苔癬そのものの出典は別途必要。
- HX-004 の出典は1998年の総説で、現行の標準と異なる可能性がある。HX-008・009 は純音聴力検査の判定手順などが共用出典の範囲外。
- SD-033・034 の出典（総説）は抄録本文が未収載のため、主張を分類と治療の骨子に限定した。

## 5. 次回への引き継ぎ

- 第25回は EY・RE、SRC-1251〜1340。眼の構造・機能と網膜・眼底疾患。糖尿病網膜症は DM-028 が正で、RE は眼科的な詳細のみ。Basedow 眼症は TH-017 が正で、EY は眼窩評価の側面のみ。
- 本回の欠番：なし（SD・HX とも連番）。
