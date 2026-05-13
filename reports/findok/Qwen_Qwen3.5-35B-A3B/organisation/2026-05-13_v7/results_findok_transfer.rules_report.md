# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (manual_findok)

Generated on: 2026-05-13T22:53:24.036998

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-13_v7/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 476 |
| Validation documents | 121 |
| Test documents | 1247 |
| Train sentences | 2257 |
| Validation sentences | 711 |
| Test sentences | 1247 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 20 |
| Refinement iterations | 0 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 10 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 50 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

**Transfer Learning**

| Property | Value |
|---|---|
| Seeded From | findok |
| Seed Rule Count | 67 |
| New Rules Added | 100 |
| Continuation | synthesize_and_refine |
| Phase1 Train Sentences | 1171 |
| Phase1 Eval Sentences | 213 |
| Transfer Train Sentences | 1086 |
| Transfer Eval Sentences | 498 |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 93.6% |
| True Positives | 179 |
| False Positives | 31 |
| False Negatives | 77 |
| Total Gold Entities | 256 |
| Micro Precision | 85.2% |
| Micro Recall | 69.9% |
| Micro F1 | 76.8% |
| Macro F1 | 76.8% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `tax_authority_finanzamt` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `tax_authority_fa` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `organisation_finanzamt` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `german_fa_city_abbreviations` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `german_city_municipality_magistrat` | 4.6% | 100.0% | 2.3% | 6 | 6 | 0 |
| `german_finanzamt_single_district` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `german_court_bundesfinanzgericht` | 42.9% | 100.0% | 27.3% | 70 | 70 | 0 |
| `german_police_landespolizeidirektion` | 3.1% | 100.0% | 1.6% | 4 | 4 | 0 |
| `german_org_ogk` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `german_fa_abbreviation` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `german_org_pensionsversicherungsanstalt` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `german_org_finanzamt_local` | 1.6% | 100.0% | 0.8% | 2 | 2 | 0 |
| `organisation_finanzamt_oesterreich` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `german_legal_court_genitive` | 35.7% | 96.6% | 21.9% | 58 | 56 | 2 |
| `german_court_verwaltungsgerichtshof` | 38.6% | 95.4% | 24.2% | 65 | 62 | 3 |
| `german_legal_verwaltungsgerichtshof` | 38.6% | 95.4% | 24.2% | 65 | 62 | 3 |
| `german_finanzamt_osterreich` | 6.0% | 88.9% | 3.1% | 9 | 8 | 1 |
| `german_legal_finanzamt_osterreich` | 6.0% | 88.9% | 3.1% | 9 | 8 | 1 |
| `german_org_magistrat` | 3.1% | 80.0% | 1.6% | 5 | 4 | 1 |
| `german_universities_colleges` | 3.1% | 66.7% | 1.6% | 6 | 4 | 2 |
| `german_legal_court_abbreviations` | 12.2% | 46.2% | 7.0% | 39 | 18 | 21 |
| `company_sudversand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_raiffeisenbank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_traunluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_office_fa` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_office_finanzamt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_textil` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_keltrizor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_dlcg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_hudec` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_hendrick` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_stefansky` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_www_fa_org` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_partnership_handel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_finanzamt_salzburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_finanzamt_multi_district` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_sophie_wittmeir` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_triloglex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_zoruniglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_mittelheizung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_rosilius` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_company_yavasoglu` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `private_company_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_legal_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_specific_it` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_specific_verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_legal_organisation_1` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_wien_waldnor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_botho_mikloweit` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_fa_linz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_fa_innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_kraftver` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_gartgart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_nord_kellex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_raiffeisenkasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_klein_vorholt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_gogel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_finanzamt_st_johann` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_mur_ververzor` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_organisation_pastl_bachle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_specific_names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_rheindigital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_company_suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_depp_verkehr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_sudevent` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_innluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_lutkehans` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_dorfkraft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_obernoder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `specific_entity_talost` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_specific_org_names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_firma_name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_company_suffix_refined` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `german_fa_purkersdorf` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_tax_office` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_specific_orgs` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_specific_company_tm` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_specific_company_saxinger` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_finanzstrafsenat` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_betrugsbekampfung` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `german_bdo_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_lubomir_merschmeyer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_zollamt_osterreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_company_inet` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_court_verfassungsgerichtshof` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_bezirkshauptmannschaft_bludenz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_pva` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_senecura` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_senecura_park` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_obb` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_krankenpflegevereins` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_finanzamt_innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_steuerberater_metzler` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_wiederspan` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_mur_alver` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_retailers` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_london_film_academy` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_bundeskanzleramt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_maschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_finanzamt_wien_1_23` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_company_technik_valseekel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_company_ernst_young` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_company_deloitte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_wiener_städtische` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_allianz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_court_vfgh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_ams_osterreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_finanzamt_neunkirchen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_landespolizeidirektion` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_bundesamt_soziales` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_arbeitsgericht` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_ernst_young` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_f_personalservice` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_universitaet_st_gallen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_verwaltungsgericht_wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_court_full_with_abbrev` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_suva` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_dr_roland_gabl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_versorgungskasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_deutsche_rentenversicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_easo` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_bm_fuer_inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_kriminalpolizei` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_suva_refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_bundesministerium_fuer_inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_bundesministerium_fuer_finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_bm_finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_flughafen_münchen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_oecd` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_court_verwaltungsgerichtshof_typo` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_gesellschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_universities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_fachhochschulen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_specific_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_svs_svb` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_sozialversicherungsanstalt_bauern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_psd_wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_sozialversicherung_bauern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_psycho_wagner` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_bundesminister` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_bundesamtes` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_finanzpolizei` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_rechtsanwaelte` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_immobilienbuero` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_roelfsen_versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `organisation_bdo_austria` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_finanzamt_grossbetriebe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_gmbh_entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_erste_bank_wko` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_org_bundesministerium` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_court_lg_fuer` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `german_court_bundesfinanzgericht_with_abbrev` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_tax_authority_faö` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_lag_organisation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_eckhardt_steuerberatung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_bdo_austria` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_da_deutsche_versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_geschenkartikel_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_aved_cosmetic` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_yoga_vidya_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_specific_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_suva_and_iv` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_legal_hospitals_and_tax` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `german_court_bundesfinanzgericht`

**F1:** 0.429 | **Precision:** 1.000 | **Recall:** 0.273  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht', its genitive 'Bundesfinanzgerichtes', and the full name with abbreviation 'Bundesfinanzgericht (BFG)'.

**Content:**
```
\b(Bundesfinanzgericht(?:es?)?(?:\s*\(BFG\))?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.273 | 0.429 | 70 | 70 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 70 | 0 | 186 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_19`)


6. Mit Schriftsatz vom 04.08.2020 stellte die BF über ihren steuerlichen Vertreter den Antrag  auf Vorlage der Bescheidbeschwerde an das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_27`)


7. Am 12.10.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor und beantragte die Abweisung, da die Ausbildung am 04.10.2017 beendet  worden sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_28`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die BF bezog im streitgegenständlichen Zeitraum Familienbeihilfe und Kinderabsetzbeträge für  ihre Tochter Stella Marschalk, Bakk. techn. (geboren im September 1998).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Stella Marschalk, Bakk. techn.` (person)
- `September 1998` (date)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

</details>

---

## `german_city_municipality_magistrat`

**F1:** 0.046 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien' and variations including 'Magistrats' (genitive) and department codes (Magistratsabteilung 6, BA32, etc.).

**Content:**
```
\b(Magistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s*,\s*Magistratsabteilung\s+\d+(?:\s*-\s*[A-Z0-9]+)?|\s*,\s*MA\s*\d+|\s*,\s*Magistratsabteilung\s+\d+\s*-\s*[A-Z0-9]+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.046 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 122 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gabriele Friedbacher` (person)
- `Wilhelm Konetzny` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

## `german_legal_court_genitive`

**F1:** 0.357 | **Precision:** 0.966 | **Recall:** 0.219  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgerichts', 'Bundesfinanzgerichtes', 'Verwaltungsgerichtshofes' (genitive/dative forms).

**Content:**
```
\b(Bundesfinanzgerichts|Bundesfinanzgerichtes|Verwaltungsgerichtshofes)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.966 | 0.219 | 0.357 | 58 | 56 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 56 | 2 | 188 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_46`)


Dem ist zu entgegnen, dass nach der zitierten Judikatur des Verwaltungsgerichtshofes das  Aufrechterhalten des Berufswunsches nicht maßgeblich ist, wenn die Ausbildung nach ihrem  Abbruch nicht wieder aufgenommen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_court_verwaltungsgerichtshof`

**F1:** 0.386 | **Precision:** 0.954 | **Recall:** 0.242  

**Format:** `regex`  
**Description:**
Consolidated rule to match 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofs' and 'Verwaltungsgerichtshofes'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.954 | 0.242 | 0.386 | 65 | 62 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 62 | 3 | 192 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_46`)


Dem ist zu entgegnen, dass nach der zitierten Judikatur des Verwaltungsgerichtshofes das  Aufrechterhalten des Berufswunsches nicht maßgeblich ist, wenn die Ausbildung nach ihrem  Abbruch nicht wieder aufgenommen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_135`)


Unter  Zugrundelegung dieser Ausführungen hat der Verwaltungsgerichtshof in der Folge festgestellt,  dass nicht allein der Wechsel der Einrichtung ausschlaggebend ist.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_legal_verwaltungsgerichtshof`

**F1:** 0.386 | **Precision:** 0.954 | **Recall:** 0.242  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive form 'Verwaltungsgerichtshofes'.

**Content:**
```
\b(Verwaltungsgerichtshof(?:es)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.954 | 0.242 | 0.386 | 65 | 62 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 62 | 3 | 192 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_46`)


Dem ist zu entgegnen, dass nach der zitierten Judikatur des Verwaltungsgerichtshofes das  Aufrechterhalten des Berufswunsches nicht maßgeblich ist, wenn die Ausbildung nach ihrem  Abbruch nicht wieder aufgenommen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_135`)


Unter  Zugrundelegung dieser Ausführungen hat der Verwaltungsgerichtshof in der Folge festgestellt,  dass nicht allein der Wechsel der Einrichtung ausschlaggebend ist.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_finanzamt_osterreich`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich', 'Finanzamtes Österreich', 'Finanzamt Innsbruck', and the abbreviation 'FAÖ'.

**Content:**
```
\b(Finanzamt(?:es)?\s+(?:Österreich|Innsbruck)|FAÖ)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.889 | 0.031 | 0.060 | 9 | 8 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 1 | 230 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `85-919/9176` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `6207 150171` (social_security_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `75-059/0556` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

</details>

---

## `german_legal_finanzamt_osterreich`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches Finanzamt variants including Österreich and Bregenz.

**Content:**
```
\b(Finanzamt(?:es)?\s+(?:Österreich|Bregenz))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.889 | 0.031 | 0.060 | 9 | 8 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 1 | 230 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `85-919/9176` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `6207 150171` (social_security_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `75-059/0556` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

</details>

---

## `german_legal_court_abbreviations`

**F1:** 0.122 | **Precision:** 0.462 | **Recall:** 0.070  

**Format:** `regex`  
**Description:**
Matches court and tax authority abbreviations. Excludes 'VwGH' if it appears in parentheses immediately after 'Verwaltungsgerichtshof' to avoid redundancy in citations.

**Content:**
```
\b(?:AMS|UFS|BMF|BFH|BFG|BMI|FAG|BHAG)\b|(?<!\()\bVwGH\b(?!\s*\d)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.462 | 0.070 | 0.122 | 39 | 18 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 21 | 174 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_83`)


Mit Schreiben vom 21.8.2025, eingelangt am BFG am 22.8.2025, zog der steuerliche Vertreter  den Antrag auf mündliche Senatsverhandlung zurück.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_137`)


Entgegen der vom Finanzamt getroffenen Beurteilung vertritt das BFG die Auffassung, dass im  streitgegenständlichen Fall eine Betätigung im Sinne des § 1 Abs. 1 LVO vorliegt, weil das  künstlerische Tätigwerden des Bf. sich nicht im Rahmen einer typischen Betätigung im Sinne  des § 1 Abs. 2 Z 2 LVO bewegt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_138`)


Für eine typische erwerbswirtschaftliche Betätigung spricht nach Ansicht des BFG die  hauptberufliche Ausübung der musikalischen Tätigkeit auf Grundlage der gehobenen  musikalischen Ausbildung des Bf.  11 von 14 Seite 12 von 14

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_139`)


In Anbetracht von Art und Umfang der vom Bf. ausgeübten Tätigkeit ist nach Ansicht des BFG  insbesondere aus folgenden Gründen nicht von einer hobbymäßigen Betätigung auszugehen:   der Bf. ist akademisch ausgebildeter Musiker, d.h. er verfügt demnach über eine  entsprechende profunde und einschlägige Hochschulausbildung   er hat auf mehreren Musik-CD’s mitgewirkt   er hat mit namhaften Musikern zusammengearbeitet und trat mit Jazzgrößen auf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_144`)


In Anbetracht der Tatsache, dass der Bf. die in Rede stehende Tätigkeit 2014, aufgrund des  Rückganges der Aufträge und der Tatsache, dass es für ihn immer schwieriger wurde Aufträge  für Auftritte zu erhalten, durch seine betriebswirtschaftlich sinnvolle Entscheidung, beendet  hat und in dem gesamten Betätigungszeitraum (hier von 1975 bis 2014) ein Gesamtüberschuss  erwirtschaftet (laut BVE geht das Finanzamt nicht vom Vorliegen einer Gesamtverlustes über  den gesamten Tätigkeitszeitraum aus) wurde, kann laut Ansicht des BFG keine Liebhaberei  vorliegen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_38`)


Insbesondere ist den Curricula der beiden Studien entnehmbar, dass beide Studien „dasselbe  Ausbildungsergebnis" (im Sinne der BFG-Entscheidung RV/0180-L/10) zum Ziel haben (s.  angehängte Curricula und BFG-Entscheidung).

**False Positives:**

- `BFG` — no gold match — likely missing annotation
- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `WU`(organisation)
- `JKU`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_128`)


Es ist zur Klärung der Rechtsmäßigkeit der Rückforderung zunächst zu prüfen, ob ein  „Studienwechsel“ im Sinne des § 2 Abs. 1 lit. b FLAG 1967 überhaupt vorliegt, bevor auf einen  solchen Studienwechsel die Bestimmungen des § 17 StudFG angewendet werden können (BFG  26.02.2022, RV/2100101/2022 mit Verweis auf VwGH 09.07.2008, 2005/13/0142, Rechtssatz  JWR_2005130142_20080709X02).

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_130`)


Allerdings ist durch die mit Einführung des UG 2002 erreichte Autonomie der Universitäten –  und damit verbunden die jeder Einrichtung mögliche individuelle Gestaltung der Studien – bei  einem Wechsel der Studieneinrichtung auch bei gleichbleibender Studienrichtung nicht in  jedem Fall eine Gleichwertigkeit gegeben (UFS 02.11.2011, RV/0289-F/11  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 96).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_134`)


UFS 19.10.2010, RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `german_universities_colleges`

**F1:** 0.031 | **Precision:** 0.667 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches common Austrian universities and colleges: Wirtschaftsuniversität Wien, Fachhochschule Wiener Neustadt, FH Campus Wien, FH Wiener Neustadt.

**Content:**
```
\b(?:Wirtschaftsuniversität Wien|Fachhochschule Wiener Neustadt|FH Campus Wien|FH Wiener Neustadt(?: für Wirtschaft und Technik GmbH)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.016 | 0.031 | 6 | 4 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 2 | 207 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes Kepler Universität Linz` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_124`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes Kepler Universität Linz` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_147`)


Nach unstrittigem Sachverhalt hat die Tochter der Bf. mit dem Wechsel vom Bachelorstudium  Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien nach dem  Sommersemester 2019, somit nach dem vierten Semester des seit Oktober 2017 dort  betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der Johannes  Kepler Universität Linz mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel  vorgenommen.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes  Kepler Universität Linz` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU Wien)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU Wien)`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU)`(organisation)
- `Johannes Kepler Universität Linz (JKU)`(organisation)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `company_sudversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'SüdVersand'.

**Content:**
```
\bSüdVersand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_raiffeisenbank`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Raiffeisenbank Wels Süd'.

**Content:**
```
\bRaiffeisenbank\s+Wels\s+Süd\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_traunluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'TraunLuftfahrt Solutions'.

**Content:**
```
\bTraunLuftfahrt\s+Solutions\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_office_fa`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by city/district names (e.g., FA Wien 1/23, FA Innsbruck).

**Content:**
```
\bFA\s+(?:Wien\s+\d+/\d+|Innsbruck|Schwechat\s+Gerasdorf|Amstetten\s+Melk\s+Scheibbs|Vorarlberg|Salzburg\-Land|Klosterneuburg|Gmunden\s+Vöcklabruck|Kirchdorf\s+Perg\s+Seyr)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_office_finanzamt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' followed by city/district names.

**Content:**
```
\bFinanzamt\s+(?:Wien\s+1/23|Innsbruck|Schwechat\s+Gerasdorf|Amstetten\s+Melk\s+Scheibbs|Vorarlberg|Salzburg\-Land|Klosterneuburg|Gmunden\s+Vöcklabruck|Kirchdorf\s+Perg\s+Seyr|Feldkirch|Salzburg\-Land)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_textil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Textil Steingartlog'.

**Content:**
```
\bTextil\s+Steingartlog\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_keltrizor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Keltrizor Handel'.

**Content:**
```
\bKeltrizor\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_dlcg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'DLCG Bildung'.

**Content:**
```
\bDLCG\s+Bildung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_hudec`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hudec&Christian Immobilien GMBH'.

**Content:**
```
\bHudec&Christian\s+Immobilien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_hendrick`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hendrick Recycling GMBH'.

**Content:**
```
\bHendrick\s+Recycling\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

</details>

---

<details>
<summary>📋 All Rules</summary>

## `german_court_bundesfinanzgericht`

**F1:** 0.429 | **Precision:** 1.000 | **Recall:** 0.273  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht', its genitive 'Bundesfinanzgerichtes', and the full name with abbreviation 'Bundesfinanzgericht (BFG)'.

**Content:**
```
\b(Bundesfinanzgericht(?:es?)?(?:\s*\(BFG\))?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.273 | 0.429 | 70 | 70 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 70 | 0 | 186 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_19`)


6. Mit Schriftsatz vom 04.08.2020 stellte die BF über ihren steuerlichen Vertreter den Antrag  auf Vorlage der Bescheidbeschwerde an das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_27`)


7. Am 12.10.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor und beantragte die Abweisung, da die Ausbildung am 04.10.2017 beendet  worden sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_28`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die BF bezog im streitgegenständlichen Zeitraum Familienbeihilfe und Kinderabsetzbeträge für  ihre Tochter Stella Marschalk, Bakk. techn. (geboren im September 1998).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Stella Marschalk, Bakk. techn.` (person)
- `September 1998` (date)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_41`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `The King´s School Worcester` (organisation)
- `Maximiliane Sakschewsky, MA` (person)
- `The King's  School Worcester` (organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Johannes Kepler Universität Linz` (organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_50`)


Mit Vorlagebericht vom 26.07.2022 legte die belangte Behörde die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor und führte dazu aus:  „Sachverhalt:  Aufgrund eines Arbeitsauftrages vom 21.05.2021 sollte der Familienbeihilfe-Anspruch der  Beschwerdeführerin bezüglich ihrer Tochter Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum  überprüft werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Viktoria Immohr` (person)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_63`)


Am 12.04.2022 reichte die  Beschwerdeführerin den Vorlageantrag ein, damit die Beschwerde dem Bundesfinanzgericht  zur Entscheidung vorgelegt wird und der Bescheid ersatzlos aufgehoben wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Viktoria Immohr` (person)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_86`)


Insbesondere nahm das Bundesfinanzgericht Einsicht in die vorgelegten  Studienpläne.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_108`)


Das Bundesfinanzgericht schließt sich  dieser Sichtweise an.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_171`)


3.3. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  15 von 16 Seite 16 von 16

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_173`)


Mit dem vorliegenden Erkenntnis folgt das Bundesfinanzgericht der zitierten einheitlichen  Rechtsprechung des Verwaltungsgerichtshofes (insbesondere VwGH 09.07.2008,  2005/13/0142).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_15`)


Das Finanzamt hat am 22. Oktober 2025 den säumigen Bescheid erlassen und dem  Bundesfinanzgericht eine Abschrift übermittelt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_17`)


Da der versäumte Bescheid nunmehr erlassen wurde, ging die Zuständigkeit nicht auf das  Bundesfinanzgericht über.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_19`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz. Quirin Januszis` (person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.` (person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich` (address)
- `Amtes für Betrugsbekämpfung` (organisation)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Gabriele Friedbacher` (person)
- `Wilhelm Konetzny` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_42`)


Die Magistratsabteilung 67 legte die Beschwerde samt dem bezughabenden Verwaltungsakt  dem Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 1. Oktober 2025).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Magistratsabteilung 67` (organisation)

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_62`)


Auch das Bundesfinanzgericht folgt dieser Vorgehensweise und gibt im gegebenen  Kontext jedoch auch zu bedenken, dass dadurch, dass weder der mit Organstrafverfügung  noch der mit Anonymverfügung verhängte Strafbetrag einbezahlt wurde, ein nicht  unerheblicher zusätzlicher Verwaltungsaufwand verursacht wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_63`)


Im Übrigen wird auf die  vom Bundesfinanzgericht als rechtsrichtig beurteilte Begründung der belangten Behörde im  angefochtenen Straferkenntnis (siehe obige Darstellung) verwiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_67`)


Auch das Bundesfinanzgericht folgt grundsätzlich dieser Strafpraxis.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_80`)


Gemäß § 25 Abs. 2 BFGG hat das Bundesfinanzgericht, soweit dies nicht in der BAO, im ZollR- DG oder im FinStrG geregelt ist, in seiner Entscheidung zu bestimmen, welche  Abgabenbehörde oder Finanzstrafbehörde die Entscheidung zu vollstrecken hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Juliana Bartjen` (person)
- `Renate Brombusch` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_49`)


Für den Fall der Abweisung unserer Beschwerde berufen wir uns auf die von unserer  Mandantschaft erteilte Vollmacht und stellen vorsorglich den Antrag auf Vorlage unserer  Beschwerde an das Bundesfinanzgericht und Entscheidung durch den Senat unter  Anberaumung einer mündlichen Verhandlung unter Hinzuziehung des Parteienvertreters.“

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_65`)


Am 22.02.2017 brachte der steuerliche Vertreter des Bf. einen Antrag auf Vorlage der  Beschwerde an das Bundesfinanzgericht ein.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_84`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_93`)


Diese Sachverhaltsfeststellungen ergeben sich nach Dafürhalten des Bundesfinanzgerichts aus  den vorgelegten Akten des Abgabenverfahrens, dem Vorbringen der Bf. in seiner Beschwerde  sowie den Erhebungen durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_162`)


Hier handelt es sich um keine Rechtsfragen von grundsätzlicher Bedeutung, weil das  Bundesfinanzgericht in rechtlicher Hinsicht der in der Begründung dieser Entscheidung  dargestellten Judikatur des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr.in Estelle Niederholz` (person)
- `Hon.-Prof.in OStR Tosca Knoller` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_20`)


Mit Schreiben vom 23.7.2025 stellte die steuerliche Vertretung den Antrag auf Entscheidung  über die Beschwerde (Vorlageantrag) durch das Bundesfinanzgericht betreffend den Bescheid  über Festsetzung von Anspruchszinsen für das Jahr 2021 vom 12.3.2025.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_21`)


Mit Vorlagebericht vom 8.10.2025 legte das Finanzamt die gegenständliche Beschwerde vom  25.3.2025 betreffend Festsetzung von Anspruchszinsen für das Jahr 2021 dem  Bundesfinanzgericht zur Entscheidung vor und beantragte die Abweisung im Wesentlichen wie  folgt:  „Sachverhalt:   Der Beschwerdeführer (Bf) brachte am 21.08.2023 die Einkommensteuererklärung für das Jahr  2021 ein.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_33`)


Bezüglich der Einkommensteuer sei bereits die Vorlage an das Bundesfinanzgericht  beantragt, eine Entscheidung dazu liege noch nicht vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_51`)


II. Das Bundesfinanzgericht hat erwogen:  1. Beweiswürdigung  Der vorstehende Verfahrensgang (Sachverhalt) ergibt sich aus dem gesamten Akteninhalt, dem  Vorlagebericht, den im Abgabeninformationssystem gespeicherten Daten und aus dem  Vorbringen der Parteien.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_74`)


sowie  zahlreiche Erkenntnisse des Bundesfinanzgerichtes).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_75`)


Wegen dieser Bindung ist der Zinsenbescheid nicht (mit Aussicht auf Erfolg) mit der  Begründung anfechtbar, der maßgebende Einkommensteuerbescheid sei inhaltlich  rechtswidrig (Ritz, BAO8, § 205 Tz 34 mit Hinweis auf die ständige Rechtsprechung des  Bundesfinanzgerichtes).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_89`)


(Hinweis: Es erging keine Vorlage der Beschwerde gegen  den Einkommensteuerbescheid 2021 an das Bundesfinanzgericht).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_94`)


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Österreich` (organisation)
- `75-059/0556` (tax_number)

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_8`)


2. Beweiswürdigung  Die Feststellungen ergeben sich eindeutig aus dem Akt des Finanzamtes und des  Bundesfinanzgerichtes und sind unstrittig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_16`)


Gegen einen Beschluss des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil der Beschluss von der  Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag.Dr. Katrin Allram` (person)
- `Oleg Dell` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `80-738/9953` (tax_number)

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_24`)


Mit Eingabe vom 21. Mai 2024 beantragte der Bf. innerhalb verlängerter Frist die Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht sowie die Durchführung einer  mündlichen Verhandlung.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_26`)


Am 13. Juni 2024 legte die belangte Behörde die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_31`)


Am 1. Oktober 2025 fand die beantragte mündliche Verhandlung vor dem Bundesfinanzgericht  statt, in der insbesondere das Vorliegen bzw. Nichtvorliegen von triftigen medizinischen  Gründen diskutiert wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_36`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. bezieht im Streitjahr 2022 Einkünfte aus nichtselbständiger Arbeit.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_63`)


Das Bundesfinanzgericht kommt aus den nachstehenden Gründen im Rahmen der freien  Beweiswürdigung zum Ergebnis, dass die nach der höchstgerichtlichen Rechtsprechung  geforderten triftigen medizinischen Gründe nicht vorliegen:  Zunächst steht unstrittig fest, dass in keinem öffentlichen Krankenhaus eine Terminanfrage  betreffend die Bandscheibenoperation der Ehefrau des Bf. gestellt wurde (vgl. Protokoll zur  Verhandlung vom 1. Oktober 2025 sowie Befundberichte vom 6. und 8. Oktober 2025).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Dagobert Nordholt` (person)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `36-532/2242` (tax_number)

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_137`)


Für den Fall, dass der Beschwerde im Zuge der Beschwerdevorentscheidung nicht Rechnung  getragen werde, werde die Vorlage der Beschwerde an das Bundesfinanzgericht  (Vorlageantrag gem. § 264 BAO).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_157`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Peter Bilger` (person)
- `Ludger Weynand` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)
- `Finanzamtes Österreich` (organisation)

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_14`)


Die Beschwerde sei nachweislich erst am 18.12.2024 vom  zuständigen Sachbearbeiter an das Bundesfinanzgericht vorgelegt worden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_22`)


5. Am 3.4.2025 stellte der Bf. durch seine steuerliche Vertretung den Antrag auf Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_23`)


6. Am 21.5.2025 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht vor und  beantragte, die Beschwerde als unbegründet abzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_25`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_33`)


Diese Sachverhaltsfeststellungen erfolgen aufgrund der dem Bundesfinanzgericht  vorliegenden Akten des Finanzamtes.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_105`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

</details>

---

## `german_court_verwaltungsgerichtshof`

**F1:** 0.386 | **Precision:** 0.954 | **Recall:** 0.242  

**Format:** `regex`  
**Description:**
Consolidated rule to match 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofs' and 'Verwaltungsgerichtshofes'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.954 | 0.242 | 0.386 | 65 | 62 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 62 | 3 | 192 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_46`)


Dem ist zu entgegnen, dass nach der zitierten Judikatur des Verwaltungsgerichtshofes das  Aufrechterhalten des Berufswunsches nicht maßgeblich ist, wenn die Ausbildung nach ihrem  Abbruch nicht wieder aufgenommen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133  Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_90`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_4`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_132`)


So unterscheidet der Verwaltungsgerichtshof zu § 2  Abs. 1 lit. b vorletzter Satz FLAG ausdrücklich zwischen dem Wechsel der Einrichtung und dem  Wechsel des Studiums.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_141`)


Ein Studienwechsel liegt nach der Rechtsprechung des Verwaltungsgerichtshofes dann vor,  wenn der Student das von ihm begonnene und bisher betriebene, aber noch nicht  abgeschlossene Studium nicht mehr fortsetzt und an dessen Stelle ein anderes unter den  Geltungsbereich des Studienförderungsgesetzes fallendes Studium beginnt (vgl. VwGH  08.01.2001, 2000/12/0053;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_150`)


Würde man die Kriterien betreffend einen  bloßen Studienortwechsel noch enger ziehen, bliebe für die vom Verwaltungsgerichtshof  gezogene Unterscheidung zwischen Studienortwechsel und Studienwechsel (VwGH  09.07.2008, 2005/13/0142) in der Praxis kein Raum, da wie bereits ausgeführt, angesichts des  Bologna-Studiensystems anders als vor Jahrzehnten wohl kaum noch zwei zu 100% identische  Studien in Österreich bzw. europaweit existieren.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Österreich` (country)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_172`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_173`)


Mit dem vorliegenden Erkenntnis folgt das Bundesfinanzgericht der zitierten einheitlichen  Rechtsprechung des Verwaltungsgerichtshofes (insbesondere VwGH 09.07.2008,  2005/13/0142).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_19`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_20`)


Im gegenständlichen Fall ist eine ordentliche Revision an den Verwaltungsgerichtshof nicht  zulässig, weil sich die Rechtsfolge der Einstellung des Säumnisbeschwerdeverfahrens  unmittelbar aus § 284 Abs. 2 BAO ergibt und somit keine Rechtsfrage von grundsätzlicher  Bedeutung zu lösen war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_5`)


III. Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_39`)


Da die  Uneinbringlichkeit einer Geldstrafe ohnehin unter der Sanktion des Vollzuges der  Ersatzfreiheitsstrafe steht, kommt dem Umstand der Gefährdung der Einbringlichkeit der  aushaftenden Forderung im Falle einer Geldstrafe laut Rechtsprechung des  Verwaltungsgerichtshofes kein Gewicht zu.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_48`)


Im Rahmen eines zu Gunsten des Bf. ausgeübten Ermessens erscheinen die im Spruch  festgesetzten Raten noch geeignet - unter Einhaltung der vom Verwaltungsgerichtshof  judizierten Prämissen - einerseits dem Strafzweck ausreichend Rechnung zu tragen und  andererseits die Entrichtung der Geldstrafe in noch angemessener First zu gewährleisten.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_52`)


Zur Unzulässigkeit der Revision  Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das  Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_50`)


Der Bf. bekämpft mit der gegenständlichen Beschwerde ausschließlich die mit dem  Straferkenntnis festgesetzte Strafhöhe, somit war entsprechend der ständigen Judikatur des  Verwaltungsgerichtshofes von einer Teilrechtskraft des Schuldspruches auszugehen (vgl. z.B.  VwGH 20.9.2013, 2013/17/0305).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_57`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes handelt es sich bei der  Strafzumessung innerhalb eines gesetzlichen Strafrahmens um eine Ermessensentscheidung,  die nach den Kriterien des § 19 VStG vorzunehmen ist (vgl. VwGH 06.04.2005, 2003/04/0031,  VwGH 17.02.2015, Ra 2015/09/0008).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_83`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_5`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_153`)


An der in diesen beiden Erkenntnis zum Ausdruck gebrachten Rechtsansicht hat der  Verwaltungsgerichtshof in seinem einen Berufsmusiker und Mitglied der Wiener  Philharmoniker betreffenden, Erkenntnis vom 21. September 2005, 2001/13/0241,  festgehalten und sie vertieft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Wiener  Philharmoniker` (organisation)

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_162`)


Hier handelt es sich um keine Rechtsfragen von grundsätzlicher Bedeutung, weil das  Bundesfinanzgericht in rechtlicher Hinsicht der in der Begründung dieser Entscheidung  dargestellten Judikatur des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_94`)


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_95`)


Die Revision an den  Verwaltungsgerichtshof ist daher unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_3`)


II. Eine ordentliche Revision an den Verwaltungsgerichtshof ist nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_16`)


Gegen einen Beschluss des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil der Beschluss von der  Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_107`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes muss das Merkmal der  Zwangsläufigkeit auch der Höhe nach gegeben sein.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_123`)


Zum anderen handelt es sich bei der  Frage, ob triftige medizinische Gründe vorliegen oder nicht, um eine solche der  Beweiswürdigung, zu deren Überprüfung der Verwaltungsgerichtshof als Rechtsinstanz  grundsätzlich nicht berufen ist (vgl. VwGH 10.5.2021, Ra 2021/15/0031 und 5.10.2021,  Ra 2021/15/0059).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_3`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_23`)


Nach ständiger  Rechtsprechung des Verwaltungsgerichtshofes sei es Aufgabe des Vertreters, im  Verwaltungsverfahren allfällig vorliegende Gründe aufzuzeigen, die ihn daran gehindert hätten,  die Abgabenschuld am oder nach dem Fälligkeitstag zu begleichen (VwGH 23.03.2010,  2007/13/0137).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_26`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes obliege dem Vertreter der  Nachweis dafür, wie die Zahlungsmittel zur Verfügung gestanden seien und in welchem  Ausmaß die anderen Gläubiger der GmbH noch Befriedigung erlangten, zu erbringen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_87`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159) sei der Zumutbarkeit bei Heranziehung eines Haftungspflichtigen angesichts  lange verstrichener Zeit im Rahmen der behördlichen Ermessensausübung Bedeutung  beizumessen, allerdings stelle das herangezogene Erkenntnis nicht auf die zurückliegenden  Abgabenschulden ab, sondern auf den Zeitraum zwischen der Beendigung des Konkurses und  der Geltendmachung der Haftung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_205`)


Kausalität  Infolge der schuldhaften Pflichtverletzung durch den Bf. konnte die Abgabenbehörde nach der  Judikatur des Verwaltungsgerichtshofes (VwGH 17.5.2004, 2003/17/0134), auch davon  ausgehen, dass die Pflichtverletzung Ursache für die Uneinbringlichkeit der  haftungsgegenständlichen Abgaben war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_209`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_219`)


Auf die ständige Rechtsprechung des Verwaltungsgerichtshofes wird hingewiesen,  wonach einer Beschwerdevorentscheidung sowie einem Vorlagebericht Vorhaltscharakter  zukommt (vgl. VwGH vom 29.1.2020, Ra 2019/13/0071, VwGH vom 30.6.2021, Ra  2021/15/0048).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_4`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_105`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_107`)


Die (ordentliche) Revision an den Verwaltungsgerichtshof ist daher unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_135`)


Unter  Zugrundelegung dieser Ausführungen hat der Verwaltungsgerichtshof in der Folge festgestellt,  dass nicht allein der Wechsel der Einrichtung ausschlaggebend ist.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_legal_verwaltungsgerichtshof`

**F1:** 0.386 | **Precision:** 0.954 | **Recall:** 0.242  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive form 'Verwaltungsgerichtshofes'.

**Content:**
```
\b(Verwaltungsgerichtshof(?:es)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.954 | 0.242 | 0.386 | 65 | 62 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 62 | 3 | 192 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_46`)


Dem ist zu entgegnen, dass nach der zitierten Judikatur des Verwaltungsgerichtshofes das  Aufrechterhalten des Berufswunsches nicht maßgeblich ist, wenn die Ausbildung nach ihrem  Abbruch nicht wieder aufgenommen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133  Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_90`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_4`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_132`)


So unterscheidet der Verwaltungsgerichtshof zu § 2  Abs. 1 lit. b vorletzter Satz FLAG ausdrücklich zwischen dem Wechsel der Einrichtung und dem  Wechsel des Studiums.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_141`)


Ein Studienwechsel liegt nach der Rechtsprechung des Verwaltungsgerichtshofes dann vor,  wenn der Student das von ihm begonnene und bisher betriebene, aber noch nicht  abgeschlossene Studium nicht mehr fortsetzt und an dessen Stelle ein anderes unter den  Geltungsbereich des Studienförderungsgesetzes fallendes Studium beginnt (vgl. VwGH  08.01.2001, 2000/12/0053;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_150`)


Würde man die Kriterien betreffend einen  bloßen Studienortwechsel noch enger ziehen, bliebe für die vom Verwaltungsgerichtshof  gezogene Unterscheidung zwischen Studienortwechsel und Studienwechsel (VwGH  09.07.2008, 2005/13/0142) in der Praxis kein Raum, da wie bereits ausgeführt, angesichts des  Bologna-Studiensystems anders als vor Jahrzehnten wohl kaum noch zwei zu 100% identische  Studien in Österreich bzw. europaweit existieren.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Österreich` (country)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_172`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_173`)


Mit dem vorliegenden Erkenntnis folgt das Bundesfinanzgericht der zitierten einheitlichen  Rechtsprechung des Verwaltungsgerichtshofes (insbesondere VwGH 09.07.2008,  2005/13/0142).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_19`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_20`)


Im gegenständlichen Fall ist eine ordentliche Revision an den Verwaltungsgerichtshof nicht  zulässig, weil sich die Rechtsfolge der Einstellung des Säumnisbeschwerdeverfahrens  unmittelbar aus § 284 Abs. 2 BAO ergibt und somit keine Rechtsfrage von grundsätzlicher  Bedeutung zu lösen war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_5`)


III. Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_39`)


Da die  Uneinbringlichkeit einer Geldstrafe ohnehin unter der Sanktion des Vollzuges der  Ersatzfreiheitsstrafe steht, kommt dem Umstand der Gefährdung der Einbringlichkeit der  aushaftenden Forderung im Falle einer Geldstrafe laut Rechtsprechung des  Verwaltungsgerichtshofes kein Gewicht zu.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_48`)


Im Rahmen eines zu Gunsten des Bf. ausgeübten Ermessens erscheinen die im Spruch  festgesetzten Raten noch geeignet - unter Einhaltung der vom Verwaltungsgerichtshof  judizierten Prämissen - einerseits dem Strafzweck ausreichend Rechnung zu tragen und  andererseits die Entrichtung der Geldstrafe in noch angemessener First zu gewährleisten.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_52`)


Zur Unzulässigkeit der Revision  Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das  Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_50`)


Der Bf. bekämpft mit der gegenständlichen Beschwerde ausschließlich die mit dem  Straferkenntnis festgesetzte Strafhöhe, somit war entsprechend der ständigen Judikatur des  Verwaltungsgerichtshofes von einer Teilrechtskraft des Schuldspruches auszugehen (vgl. z.B.  VwGH 20.9.2013, 2013/17/0305).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_57`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes handelt es sich bei der  Strafzumessung innerhalb eines gesetzlichen Strafrahmens um eine Ermessensentscheidung,  die nach den Kriterien des § 19 VStG vorzunehmen ist (vgl. VwGH 06.04.2005, 2003/04/0031,  VwGH 17.02.2015, Ra 2015/09/0008).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_83`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_5`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_153`)


An der in diesen beiden Erkenntnis zum Ausdruck gebrachten Rechtsansicht hat der  Verwaltungsgerichtshof in seinem einen Berufsmusiker und Mitglied der Wiener  Philharmoniker betreffenden, Erkenntnis vom 21. September 2005, 2001/13/0241,  festgehalten und sie vertieft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Wiener  Philharmoniker` (organisation)

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_162`)


Hier handelt es sich um keine Rechtsfragen von grundsätzlicher Bedeutung, weil das  Bundesfinanzgericht in rechtlicher Hinsicht der in der Begründung dieser Entscheidung  dargestellten Judikatur des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_94`)


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_95`)


Die Revision an den  Verwaltungsgerichtshof ist daher unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_3`)


II. Eine ordentliche Revision an den Verwaltungsgerichtshof ist nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_16`)


Gegen einen Beschluss des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil der Beschluss von der  Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_107`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes muss das Merkmal der  Zwangsläufigkeit auch der Höhe nach gegeben sein.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_123`)


Zum anderen handelt es sich bei der  Frage, ob triftige medizinische Gründe vorliegen oder nicht, um eine solche der  Beweiswürdigung, zu deren Überprüfung der Verwaltungsgerichtshof als Rechtsinstanz  grundsätzlich nicht berufen ist (vgl. VwGH 10.5.2021, Ra 2021/15/0031 und 5.10.2021,  Ra 2021/15/0059).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_3`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_23`)


Nach ständiger  Rechtsprechung des Verwaltungsgerichtshofes sei es Aufgabe des Vertreters, im  Verwaltungsverfahren allfällig vorliegende Gründe aufzuzeigen, die ihn daran gehindert hätten,  die Abgabenschuld am oder nach dem Fälligkeitstag zu begleichen (VwGH 23.03.2010,  2007/13/0137).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_26`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes obliege dem Vertreter der  Nachweis dafür, wie die Zahlungsmittel zur Verfügung gestanden seien und in welchem  Ausmaß die anderen Gläubiger der GmbH noch Befriedigung erlangten, zu erbringen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_87`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159) sei der Zumutbarkeit bei Heranziehung eines Haftungspflichtigen angesichts  lange verstrichener Zeit im Rahmen der behördlichen Ermessensausübung Bedeutung  beizumessen, allerdings stelle das herangezogene Erkenntnis nicht auf die zurückliegenden  Abgabenschulden ab, sondern auf den Zeitraum zwischen der Beendigung des Konkurses und  der Geltendmachung der Haftung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_205`)


Kausalität  Infolge der schuldhaften Pflichtverletzung durch den Bf. konnte die Abgabenbehörde nach der  Judikatur des Verwaltungsgerichtshofes (VwGH 17.5.2004, 2003/17/0134), auch davon  ausgehen, dass die Pflichtverletzung Ursache für die Uneinbringlichkeit der  haftungsgegenständlichen Abgaben war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_209`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_219`)


Auf die ständige Rechtsprechung des Verwaltungsgerichtshofes wird hingewiesen,  wonach einer Beschwerdevorentscheidung sowie einem Vorlagebericht Vorhaltscharakter  zukommt (vgl. VwGH vom 29.1.2020, Ra 2019/13/0071, VwGH vom 30.6.2021, Ra  2021/15/0048).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_4`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_105`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_107`)


Die (ordentliche) Revision an den Verwaltungsgerichtshof ist daher unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_135`)


Unter  Zugrundelegung dieser Ausführungen hat der Verwaltungsgerichtshof in der Folge festgestellt,  dass nicht allein der Wechsel der Einrichtung ausschlaggebend ist.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_legal_court_genitive`

**F1:** 0.357 | **Precision:** 0.966 | **Recall:** 0.219  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgerichts', 'Bundesfinanzgerichtes', 'Verwaltungsgerichtshofes' (genitive/dative forms).

**Content:**
```
\b(Bundesfinanzgerichts|Bundesfinanzgerichtes|Verwaltungsgerichtshofes)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.966 | 0.219 | 0.357 | 58 | 56 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 56 | 2 | 188 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_46`)


Dem ist zu entgegnen, dass nach der zitierten Judikatur des Verwaltungsgerichtshofes das  Aufrechterhalten des Berufswunsches nicht maßgeblich ist, wenn die Ausbildung nach ihrem  Abbruch nicht wieder aufgenommen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_90`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_141`)


Ein Studienwechsel liegt nach der Rechtsprechung des Verwaltungsgerichtshofes dann vor,  wenn der Student das von ihm begonnene und bisher betriebene, aber noch nicht  abgeschlossene Studium nicht mehr fortsetzt und an dessen Stelle ein anderes unter den  Geltungsbereich des Studienförderungsgesetzes fallendes Studium beginnt (vgl. VwGH  08.01.2001, 2000/12/0053;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_171`)


3.3. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  15 von 16 Seite 16 von 16

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_172`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_173`)


Mit dem vorliegenden Erkenntnis folgt das Bundesfinanzgericht der zitierten einheitlichen  Rechtsprechung des Verwaltungsgerichtshofes (insbesondere VwGH 09.07.2008,  2005/13/0142).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_19`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_39`)


Da die  Uneinbringlichkeit einer Geldstrafe ohnehin unter der Sanktion des Vollzuges der  Ersatzfreiheitsstrafe steht, kommt dem Umstand der Gefährdung der Einbringlichkeit der  aushaftenden Forderung im Falle einer Geldstrafe laut Rechtsprechung des  Verwaltungsgerichtshofes kein Gewicht zu.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_52`)


Zur Unzulässigkeit der Revision  Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das  Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_50`)


Der Bf. bekämpft mit der gegenständlichen Beschwerde ausschließlich die mit dem  Straferkenntnis festgesetzte Strafhöhe, somit war entsprechend der ständigen Judikatur des  Verwaltungsgerichtshofes von einer Teilrechtskraft des Schuldspruches auszugehen (vgl. z.B.  VwGH 20.9.2013, 2013/17/0305).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_57`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes handelt es sich bei der  Strafzumessung innerhalb eines gesetzlichen Strafrahmens um eine Ermessensentscheidung,  die nach den Kriterien des § 19 VStG vorzunehmen ist (vgl. VwGH 06.04.2005, 2003/04/0031,  VwGH 17.02.2015, Ra 2015/09/0008).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_93`)


Diese Sachverhaltsfeststellungen ergeben sich nach Dafürhalten des Bundesfinanzgerichts aus  den vorgelegten Akten des Abgabenverfahrens, dem Vorbringen der Bf. in seiner Beschwerde  sowie den Erhebungen durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_162`)


Hier handelt es sich um keine Rechtsfragen von grundsätzlicher Bedeutung, weil das  Bundesfinanzgericht in rechtlicher Hinsicht der in der Begründung dieser Entscheidung  dargestellten Judikatur des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_74`)


sowie  zahlreiche Erkenntnisse des Bundesfinanzgerichtes).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_75`)


Wegen dieser Bindung ist der Zinsenbescheid nicht (mit Aussicht auf Erfolg) mit der  Begründung anfechtbar, der maßgebende Einkommensteuerbescheid sei inhaltlich  rechtswidrig (Ritz, BAO8, § 205 Tz 34 mit Hinweis auf die ständige Rechtsprechung des  Bundesfinanzgerichtes).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_94`)


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_8`)


2. Beweiswürdigung  Die Feststellungen ergeben sich eindeutig aus dem Akt des Finanzamtes und des  Bundesfinanzgerichtes und sind unstrittig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_16`)


Gegen einen Beschluss des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil der Beschluss von der  Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_107`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes muss das Merkmal der  Zwangsläufigkeit auch der Höhe nach gegeben sein.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_23`)


Nach ständiger  Rechtsprechung des Verwaltungsgerichtshofes sei es Aufgabe des Vertreters, im  Verwaltungsverfahren allfällig vorliegende Gründe aufzuzeigen, die ihn daran gehindert hätten,  die Abgabenschuld am oder nach dem Fälligkeitstag zu begleichen (VwGH 23.03.2010,  2007/13/0137).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_26`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes obliege dem Vertreter der  Nachweis dafür, wie die Zahlungsmittel zur Verfügung gestanden seien und in welchem  Ausmaß die anderen Gläubiger der GmbH noch Befriedigung erlangten, zu erbringen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_87`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159) sei der Zumutbarkeit bei Heranziehung eines Haftungspflichtigen angesichts  lange verstrichener Zeit im Rahmen der behördlichen Ermessensausübung Bedeutung  beizumessen, allerdings stelle das herangezogene Erkenntnis nicht auf die zurückliegenden  Abgabenschulden ab, sondern auf den Zeitraum zwischen der Beendigung des Konkurses und  der Geltendmachung der Haftung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_205`)


Kausalität  Infolge der schuldhaften Pflichtverletzung durch den Bf. konnte die Abgabenbehörde nach der  Judikatur des Verwaltungsgerichtshofes (VwGH 17.5.2004, 2003/17/0134), auch davon  ausgehen, dass die Pflichtverletzung Ursache für die Uneinbringlichkeit der  haftungsgegenständlichen Abgaben war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_209`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_219`)


Auf die ständige Rechtsprechung des Verwaltungsgerichtshofes wird hingewiesen,  wonach einer Beschwerdevorentscheidung sowie einem Vorlagebericht Vorhaltscharakter  zukommt (vgl. VwGH vom 29.1.2020, Ra 2019/13/0071, VwGH vom 30.6.2021, Ra  2021/15/0048).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_105`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_legal_court_abbreviations`

**F1:** 0.122 | **Precision:** 0.462 | **Recall:** 0.070  

**Format:** `regex`  
**Description:**
Matches court and tax authority abbreviations. Excludes 'VwGH' if it appears in parentheses immediately after 'Verwaltungsgerichtshof' to avoid redundancy in citations.

**Content:**
```
\b(?:AMS|UFS|BMF|BFH|BFG|BMI|FAG|BHAG)\b|(?<!\()\bVwGH\b(?!\s*\d)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.462 | 0.070 | 0.122 | 39 | 18 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 18 | 21 | 174 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_83`)


Mit Schreiben vom 21.8.2025, eingelangt am BFG am 22.8.2025, zog der steuerliche Vertreter  den Antrag auf mündliche Senatsverhandlung zurück.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_137`)


Entgegen der vom Finanzamt getroffenen Beurteilung vertritt das BFG die Auffassung, dass im  streitgegenständlichen Fall eine Betätigung im Sinne des § 1 Abs. 1 LVO vorliegt, weil das  künstlerische Tätigwerden des Bf. sich nicht im Rahmen einer typischen Betätigung im Sinne  des § 1 Abs. 2 Z 2 LVO bewegt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_138`)


Für eine typische erwerbswirtschaftliche Betätigung spricht nach Ansicht des BFG die  hauptberufliche Ausübung der musikalischen Tätigkeit auf Grundlage der gehobenen  musikalischen Ausbildung des Bf.  11 von 14 Seite 12 von 14

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_139`)


In Anbetracht von Art und Umfang der vom Bf. ausgeübten Tätigkeit ist nach Ansicht des BFG  insbesondere aus folgenden Gründen nicht von einer hobbymäßigen Betätigung auszugehen:   der Bf. ist akademisch ausgebildeter Musiker, d.h. er verfügt demnach über eine  entsprechende profunde und einschlägige Hochschulausbildung   er hat auf mehreren Musik-CD’s mitgewirkt   er hat mit namhaften Musikern zusammengearbeitet und trat mit Jazzgrößen auf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_144`)


In Anbetracht der Tatsache, dass der Bf. die in Rede stehende Tätigkeit 2014, aufgrund des  Rückganges der Aufträge und der Tatsache, dass es für ihn immer schwieriger wurde Aufträge  für Auftritte zu erhalten, durch seine betriebswirtschaftlich sinnvolle Entscheidung, beendet  hat und in dem gesamten Betätigungszeitraum (hier von 1975 bis 2014) ein Gesamtüberschuss  erwirtschaftet (laut BVE geht das Finanzamt nicht vom Vorliegen einer Gesamtverlustes über  den gesamten Tätigkeitszeitraum aus) wurde, kann laut Ansicht des BFG keine Liebhaberei  vorliegen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_148`)


Wie der VwGH bereits in mehreren Erkenntnissen ausfgeührt hat erfordert die berufliche  Tätigkeit eines hauptberuflichen Musikers ein musikalisches Niveau, welches nur durch  regelmäßige Arbeit am Instrument zu erreichen und zu halten ist.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_14`)


Der Antragsteller hat  daraufhin eine Entscheidung über diese Beschwerde durch einen Vorlageantrag an das BFG  beantragt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_27`)


Darüber wurde folgendermaßen entschieden:   - die Beschwerde gegen den ESt-Bescheid 2020 wurde mit Beschwerdevorentscheidung (BVE)  vom 12.3.2025 (Anm. laut BFG richtig: 11.03.2025) abgewiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_78`)


es erfolgt daher keine Abänderung des ursprünglichen  Zinsenbescheides (Ritz, BAO8, § 205 Tz 35 mit Hinweis auf VwGH 28.5.2009, 2006/15/0316,  VwGH 31.1.2019, Ro 2018/15/0005; sowie zahlreiche Erkenntnisse des BFG).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_82`)


Der Antragsteller hat daraufhin eine Entscheidung über diese Beschwerde durch einen  Vorlageantrag an das BFG beantragt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_84`)


Festgehalten wird, dass die vom Vertreter des Bf. genannte Beschwerdevorentscheidung vom  11.3.2025 nicht die Einkommensteuer für das Jahr 2021, sondern die Einkommensteuer für das  Jahr 2020 betrifft (Die Beschwerde gegen den Einkommensteuerbescheid 2020 wurde dem  BFG zur Entscheidung vorgelegt, die noch unerledigt ist, RV/5100771/2025).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_90`)


Unabhängig vom Ausgang der eingebrachten Beschwerde gegen den  Einkommensteuerbescheid für das Jahr 2020 (und der Vorlage an das BFG) ist die Beschwerde  vom 25.3.2025 gegen den Bescheid vom 12.3.2025 betreffend Festsetzung von  Anspruchszinsen (§ 205 BAO) für das Jahr 2021 als unbegründet abzuweisen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_94`)


Nach der Rechtsprechung des VwGH setzt eine Zwangsläufigkeit aus sittlichen Gründen voraus,  dass sich der Steuerpflichtige nach dem Urteil billig und gerecht denkender Menschen zu der  Leistung verpflichtet halten kann.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_155`)


Im Zuge einer Akteneinsicht vor dem BFG wurde die Sach- und Rechtslage mit dem Bf., der  mittlerweile steuerlich nicht mehr vertreten ist, eingehend erörtert.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_158`)


Der oben wiedergegebene Verfahrensablauf wird von den Parteien nicht bestritten, findet im  Akteninhalt Deckung und wird somit vom BFG zum festgestellten Sachverhalt erhoben.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_161`)


Der Sachverhalt und auch die rechtliche Situation wurden dem Bf. anlässlich mehrerer  Telefonate mit ihm und auch im Rahmen der von ihm vorgenommenen Akteneinsicht durch  das BFG erörtert und von ihm zur Kenntnis genommen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_226`)


Auf  die einheitliche zitierte Judikatur des VwGH wird verwiesen.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_38`)


Insbesondere ist den Curricula der beiden Studien entnehmbar, dass beide Studien „dasselbe  Ausbildungsergebnis" (im Sinne der BFG-Entscheidung RV/0180-L/10) zum Ziel haben (s.  angehängte Curricula und BFG-Entscheidung).

**False Positives:**

- `BFG` — no gold match — likely missing annotation
- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `WU`(organisation)
- `JKU`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_128`)


Es ist zur Klärung der Rechtsmäßigkeit der Rückforderung zunächst zu prüfen, ob ein  „Studienwechsel“ im Sinne des § 2 Abs. 1 lit. b FLAG 1967 überhaupt vorliegt, bevor auf einen  solchen Studienwechsel die Bestimmungen des § 17 StudFG angewendet werden können (BFG  26.02.2022, RV/2100101/2022 mit Verweis auf VwGH 09.07.2008, 2005/13/0142, Rechtssatz  JWR_2005130142_20080709X02).

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_130`)


Allerdings ist durch die mit Einführung des UG 2002 erreichte Autonomie der Universitäten –  und damit verbunden die jeder Einrichtung mögliche individuelle Gestaltung der Studien – bei  einem Wechsel der Studieneinrichtung auch bei gleichbleibender Studienrichtung nicht in  jedem Fall eine Gleichwertigkeit gegeben (UFS 02.11.2011, RV/0289-F/11  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 96).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_134`)


UFS 19.10.2010, RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_143`)


Die Gewährung der Familienbeihilfe  für volljährige Kinder stellt nach den näheren Regelungen des § 2 Abs. 1 lit. b FLAG ersichtlich  darauf ab, dass sich das Kind einer Berufsausbildung mit dem ernstlichen und zielstrebigen,  nach außen erkennbaren Bemühen um den Ausbildungserfolg unterzieht (UFS 19.10.2010,  RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_160`)


BFG 05.07.2016, RV/5100209/2012;

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Österreich`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_164`)


vgl. auch UFS  16.02.2007, RV/0189-G/06).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_167`)


Für die Überprüfung dieser  Frage erachte es der VwGH als ausreichend, die Unterscheidung auf die Kernfächer bzw. den  Kernbereich des Studiums zu reduzieren (VwGH 7.8.2001, 97/14/0068).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_41`)


Der Bf. erhob gegen das Straferkenntnis mit Anbringen vom 5. September 2025 (fristgerecht)  Beschwerde, führte aus wie im oben angeführten Einspruch gegen die Strafverfügung vom  30. Juni 2025 mit dem Ersuchen, die im Straferkenntnis festgelegte Geldstrafe in Höhe von  65,00 Euro [Anmerkung BFG, gemeint: Geldstrafe in Höhe von 55,00 Euro] herabzusetzen.

**False Positives:**

- `BFG` — partial — pred is substring of gold: `BFG,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG,`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Magistrat der Stadt Wien`(organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_26`)


Von einer Liebhabereitätigkeit kann ja wohl nur dann gesprochen werden, wenn jemand,  dessen Hauptberuf sich von seinem Hobby, dem er aus besonderer Neigung nachgeht (siehe  UFS 27.11.2003, RV/0509-L/02), unterscheidet, und dieses Hobby zu steuerlich unbeachtlichen  Gesamtverlusten führt.

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_219`)


Auf die ständige Rechtsprechung des Verwaltungsgerichtshofes wird hingewiesen,  wonach einer Beschwerdevorentscheidung sowie einem Vorlagebericht Vorhaltscharakter  zukommt (vgl. VwGH vom 29.1.2020, Ra 2019/13/0071, VwGH vom 30.6.2021, Ra  2021/15/0048).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_47`)


BFG  2.10.2024, RV/6100259/2023).

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_56`)


BFG 16.12.2021,  RV/7102723/2021;

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_finanzamt_osterreich`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich', 'Finanzamtes Österreich', 'Finanzamt Innsbruck', and the abbreviation 'FAÖ'.

**Content:**
```
\b(Finanzamt(?:es)?\s+(?:Österreich|Innsbruck)|FAÖ)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.889 | 0.031 | 0.060 | 9 | 8 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 1 | 230 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `85-919/9176` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `6207 150171` (social_security_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `75-059/0556` (tax_number)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Katrin Allram` (person)
- `Oleg Dell` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `80-738/9953` (tax_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Ludger Weynand` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

</details>

---

## `german_legal_finanzamt_osterreich`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches Finanzamt variants including Österreich and Bregenz.

**Content:**
```
\b(Finanzamt(?:es)?\s+(?:Österreich|Bregenz))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.889 | 0.031 | 0.060 | 9 | 8 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 1 | 230 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `85-919/9176` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `6207 150171` (social_security_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `75-059/0556` (tax_number)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Katrin Allram` (person)
- `Oleg Dell` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `80-738/9953` (tax_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Ludger Weynand` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

</details>

---

## `german_city_municipality_magistrat`

**F1:** 0.046 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien' and variations including 'Magistrats' (genitive) and department codes (Magistratsabteilung 6, BA32, etc.).

**Content:**
```
\b(Magistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s*,\s*Magistratsabteilung\s+\d+(?:\s*-\s*[A-Z0-9]+)?|\s*,\s*MA\s*\d+|\s*,\s*Magistratsabteilung\s+\d+\s*-\s*[A-Z0-9]+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.046 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 122 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gabriele Friedbacher` (person)
- `Wilhelm Konetzny` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

## `german_police_landespolizeidirektion`

**F1:** 0.031 | **Precision:** 1.000 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirektion Wien'.

**Content:**
```
\b(Landespolizeidirektion\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.016 | 0.031 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 222 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Maximiliane Sakschewsky, MA` (person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_75`)


Diesen Lebensumständen stehen folgende inländische (österreichische) Anknüpfungspunkte  gegenüber: Nachweisliche Aufenthalte  - am 18. August 2019 (6-stündige Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" im Hinblick auf den beabsichtigten  Führerscheinerwerb),  vom 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019 sowie  17. bis 19. Februar 2020 (in Wien mit dem Bf. unternommene Fahrten gemäß § 19 Abs. 8 FSG;  am 20. Februar 2020 wurde vom Bf. die Überweisung von € 173,10 an die  Landespolizeidirektion Wien - Verkehrsamt vorgenommen).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Wien` (city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_7`)


von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am  2. Mai 2025 um 11:09 Uhr in 1100 Wien, Gasse, beanstandet, da ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `1100 Wien` (address)

</details>

---

## `german_org_magistrat`

**F1:** 0.031 | **Precision:** 0.800 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt [City]' or 'Magistrats der Stadt [City]'.

**Content:**
```
\bMagistrat(?:s)? der Stadt [A-Z][a-z]+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.800 | 0.016 | 0.031 | 5 | 4 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 1 | 124 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, MA 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

</details>

---

## `german_universities_colleges`

**F1:** 0.031 | **Precision:** 0.667 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches common Austrian universities and colleges: Wirtschaftsuniversität Wien, Fachhochschule Wiener Neustadt, FH Campus Wien, FH Wiener Neustadt.

**Content:**
```
\b(?:Wirtschaftsuniversität Wien|Fachhochschule Wiener Neustadt|FH Campus Wien|FH Wiener Neustadt(?: für Wirtschaft und Technik GmbH)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.016 | 0.031 | 6 | 4 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 2 | 207 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes Kepler Universität Linz` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_124`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes Kepler Universität Linz` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_147`)


Nach unstrittigem Sachverhalt hat die Tochter der Bf. mit dem Wechsel vom Bachelorstudium  Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien nach dem  Sommersemester 2019, somit nach dem vierten Semester des seit Oktober 2017 dort  betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der Johannes  Kepler Universität Linz mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel  vorgenommen.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes  Kepler Universität Linz` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU Wien)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU Wien)`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU)`(organisation)
- `Johannes Kepler Universität Linz (JKU)`(organisation)

</details>

---

## `tax_authority_finanzamt`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches full names of tax authorities starting with 'Finanzamt' or 'FA' followed by specific known location names.

**Content:**
```
\b(?:Finanzamt|FA)\s+(?:Steiermark\s+Mitte|Vorarlberg|Gmunden\s+V\u00f6cklabruck|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Schwechat\s+Gerasdorf|Waldviertel|Purkersdorf|Spittal\s+Villach|Freistadt\s+Rohrbach\s+Urfahr)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.012 | 0.023 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 31 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `36-532/2242` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

</details>

---

## `organisation_finanzamt`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches tax authorities with known full location names. Updated to include Linz, Innsbruck, and ensure Oststeiermark/Judenburg Liezen are covered.

**Content:**
```
\b(?:Finanzamt|FA)\s+(?:Steiermark\s+Mitte|Vorarlberg|Gmunden\s+V\u00f6cklabruck|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Spittal\s+Villach|Schwechat\s+Gerasdorf|Waldviertel|Purkersdorf|Freistadt\s+Rohrbach\s+Urfahr|Amstetten\s+Melk\s+Scheibbs|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Innsbruck|Klosterneuburg|Salzburg\-Land|Linz|Oststeiermark|Salzburg\-Stadt|Bruck\s+Eisenstadt\s+Oberwart|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Tirol\s+Ost|Nieder\u00f6sterreich\s+Mitte)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.012 | 0.023 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 31 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `36-532/2242` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

</details>

---

## `organisation_finanzamt_oesterreich`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' and its genitive 'Finanzamts Österreich'.

**Content:**
```
\b(?:Finanzamts|Finanzamt)\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.012 | 0.023 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 149 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

## `german_org_finanzamt_local`

**F1:** 0.016 | **Precision:** 1.000 | **Recall:** 0.008  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' followed by specific known city names to avoid partial matches of multi-word names.

**Content:**
```
\bFinanzamt\s+(?:Hollabrunn|Korneuburg|Tulln|Braunau\s+Ried\s+Sch\u00e4rding|Steiermark\s+Mitte|Vorarlberg|Gmunden\s+V\u00f6cklabruck|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Spittal\s+Villach|Schwechat\s+Gerasdorf|Waldviertel|Purkersdorf|Freistadt\s+Rohrbach\s+Urfahr|Amstetten\s+Melk\s+Scheibbs|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Innsbruck|Klosterneuburg|Salzburg\-Land|Linz|Oststeiermark|Salzburg\-Stadt|Bruck\s+Eisenstadt\s+Oberwart|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Tirol\s+Ost|Nieder\u00f6sterreich\s+Mitte)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.008 | 0.016 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 26 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

</details>

---

## `tax_authority_fa`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches abbreviated tax authorities starting with 'FA' followed by specific known location names.

**Content:**
```
\bFA\s+(?:Steiermark\s+Mitte|Vorarlberg|Gmunden\s+Vöcklabruck|Braunau\s+Ried\s+Schärding|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Spittal\s+Villach|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 33 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `36-532/2242` (tax_number)

</details>

---

## `german_fa_city_abbreviations`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'FA' abbreviations and full 'Finanzamt' names for specific regions. Refined to prevent matching dates or partial city names.

**Content:**
```
\b(?:FA\s+(?:Steiermark\s+Mitte|Vorarlberg|Gmunden\s+V\u00f6cklabruck|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Spittal\s+Villach|Schwechat\s+Gerasdorf|Waldviertel|Purkersdorf|Freistadt\s+Rohrbach\s+Urfahr|Amstetten\s+Melk\s+Scheibbs|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Innsbruck|Klosterneuburg|Salzburg\-Land|Linz|Oststeiermark|Salzburg\-Stadt|Bruck\s+Eisenstadt\s+Oberwart|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Tirol\s+Ost|Nieder\u00f6sterreich\s+Mitte)|Finanzamt\s+(?:Tirol\s+Ost|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Purkersdorf|Linz|Waldviertel))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 33 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `36-532/2242` (tax_number)

</details>

---

## `german_finanzamt_single_district`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Updated to correctly match 'Finanzamt Wien 2/20/21/22' and other complex district suffixes with multiple slashes.

**Content:**
```
\b(?:Finanzamts|Finanzamt|FA)\s+(?:Neunkirchen\s+(?:Wiener\s+Neustadt|Wr\.\s+Neustadt)|Wien\s+\d+(?:/\d+)+\s+Klosterneuburg|Innsbruck|Klosterneuburg|Salzburg\-Land|Vorarlberg|Amstetten\s+Melk\s+Scheibbs|Gmunden\s+V\u00f6cklabruck|Kirchdorf\s+Perg\s+Seyr|Schwechat\s+Gerasdorf|Waldviertel|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Steiermark\s+Mitte|Wien\s+\d+/\d+|Salzburg\-Stadt|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Bruck\s+Eisenstadt\s+Oberwart|Grieskirchen\s+Wels|Freistadt\s+Rohrbach\s+Urfahr|Spittal\s+Villach|Graz\-Stadt|Graz\-\s+Stadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 255 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `Stella Marschalk, Bakk. techn.` (person)

</details>

---

## `german_org_ogk`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 49 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_22`)


Der Kostenersatz der ÖGK sei auf der Rechnung ersichtlich,  weitere Ersatzleistungen habe es nicht gegeben.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `german_fa_abbreviation`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'FA' or 'Fa.' followed by specific known city names to avoid partial matches.

**Content:**
```
\b(?:FA|Fa\.?)\s+(?:Steiermark\s+Mitte|Vorarlberg|Gmunden\s+V\u00f6cklabruck|Braunau\s+Ried\s+Sch\u00e4rding|Landeck\s+Reutte|Wien\s+8/16/17|Kirchdorf\s+Perg\s+Steyr|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Spittal\s+Villach|Schwechat\s+Gerasdorf|Waldviertel|Purkersdorf|Freistadt\s+Rohrbach\s+Urfahr|Amstetten\s+Melk\s+Scheibbs|Judenburg\s+Liezen|Baden\s+M\u00f6dling|Innsbruck|Klosterneuburg|Salzburg\-Land|Linz|Oststeiermark|Salzburg\-Stadt|Bruck\s+Eisenstadt\s+Oberwart|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Tirol\s+Ost|Nieder\u00f6sterreich\s+Mitte|Hollabrunn|Korneuburg|Tulln)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 33 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `36-532/2242` (tax_number)

</details>

---

## `german_org_pensionsversicherungsanstalt`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Pensionsversicherungsanstalt'.

**Content:**
```
\bPensionsversicherungsanstalt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 44 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

## `company_sudversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'SüdVersand'.

**Content:**
```
\bSüdVersand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_raiffeisenbank`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Raiffeisenbank Wels Süd'.

**Content:**
```
\bRaiffeisenbank\s+Wels\s+Süd\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_traunluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'TraunLuftfahrt Solutions'.

**Content:**
```
\bTraunLuftfahrt\s+Solutions\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_office_fa`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by city/district names (e.g., FA Wien 1/23, FA Innsbruck).

**Content:**
```
\bFA\s+(?:Wien\s+\d+/\d+|Innsbruck|Schwechat\s+Gerasdorf|Amstetten\s+Melk\s+Scheibbs|Vorarlberg|Salzburg\-Land|Klosterneuburg|Gmunden\s+Vöcklabruck|Kirchdorf\s+Perg\s+Seyr)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_office_finanzamt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' followed by city/district names.

**Content:**
```
\bFinanzamt\s+(?:Wien\s+1/23|Innsbruck|Schwechat\s+Gerasdorf|Amstetten\s+Melk\s+Scheibbs|Vorarlberg|Salzburg\-Land|Klosterneuburg|Gmunden\s+Vöcklabruck|Kirchdorf\s+Perg\s+Seyr|Feldkirch|Salzburg\-Land)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_textil`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Textil Steingartlog'.

**Content:**
```
\bTextil\s+Steingartlog\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_keltrizor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Keltrizor Handel'.

**Content:**
```
\bKeltrizor\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_dlcg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'DLCG Bildung'.

**Content:**
```
\bDLCG\s+Bildung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_hudec`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hudec&Christian Immobilien GMBH'.

**Content:**
```
\bHudec&Christian\s+Immobilien\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_hendrick`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Hendrick Recycling GMBH'.

**Content:**
```
\bHendrick\s+Recycling\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_stefansky`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Stefansky Bau GMBH'.

**Content:**
```
\bStefansky\s+Bau\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_www_fa_org`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific web URL variant 'www.FA Salzburg-Stadt'.

**Content:**
```
www\.FA\s+Salzburg\-Stadt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_partnership_handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches legal partnership structures like 'Name + Name Handel' observed in 'Reinemut + Smoch Handel'.

**Content:**
```
([A-Z][a-z]+)\s*\+\s*([A-Z][a-z]+)\s+Handel
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_finanzamt_salzburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Salzburg-Stadt' or 'FA Salzburg-Stadt' as a single entity.

**Content:**
```
\b(?:Finanzamt|FA)\s+Salzburg\-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_finanzamt_multi_district`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt with multiple district names (e.g., Deutschlandsberg Leibnitz Voitsberg, Bruck Eisenstadt Oberwart).

**Content:**
```
\b(?:Finanzamt|FA)\s+(?:Deutschlandsberg\s+Leibnitz\s+Voitsberg|Bruck\s+Eisenstadt\s+Oberwart|Oststeiermark|Nieder\u00f6sterreich\s+Mitte|Tirol\s+Ost)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_sophie_wittmeir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Sophie Wittmeir' which appears as an organisation in the training data.

**Content:**
```
\bSophie\s+Wittmeir\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_triloglex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Triloglex GMBH'.

**Content:**
```
\bTriloglex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_zoruniglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Zoruniglanz'.

**Content:**
```
\bZoruniglanz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_mittelheizung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'MittelHeizung Werke AG'.

**Content:**
```
\bMittelHeizung\s+Werke\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_rosilius`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Rosilius Pflege AG'.

**Content:**
```
\bRosilius\s+Pflege\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_company_yavasoglu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Yavasoglu Analyse AG'.

**Content:**
```
\bYavasoglu\s+Analyse\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `private_company_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches private companies ending in GMBH, excluding Finanzamt patterns.

**Content:**
```
\b(?:(?:Tschermack\s+Pharma|Klusner\&P\u00e4ffgen\s+Bildung|TalVerverwerkGarten|ZFGQ\s+Pharma)\s+GMBH|S\u00fcd\-Landwirtschaft|Henken)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_legal_entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known organisations from training data that lack standard suffixes or have unique structures.

**Content:**
```
\b(?:Gr\u00f6nemeier&H\u00f6velberndt\s+E\u2011Commerce|Annemie\s+Bott|Milan\s+H\u00e4ndlein|Krolitzki\s+Beratung|Manfredo\s+Herrschmann|FA\s+Grieskirchen\s+Wels|Finanzamt\s+Grieskirchen\s+Wels)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_specific_it`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific IT companies found in training data: Lexdon IT, Tritri-IT.

**Content:**
```
\b(?:Lexdon\s+IT|Tritri\-IT)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_specific_verlag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific Verlag companies found in training data: Dorfcon-Verlag.

**Content:**
```
\bDorfcon\-Verlag\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_legal_organisation_1`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known legal entities: Trafenfen Automotive, DrauFinanzen, Kelgart-Druck, Bezirksgericht Zell am See.

**Content:**
```
\b(?:Trafenfen\s+Automotive|DrauFinanzen|Kelgart\-Druck|Bezirksgericht\s+Zell\s+am\s+See)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_wien_waldnor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Wien Waldnor KG' which was being truncated.

**Content:**
```
\bWien\s+Waldnor\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_botho_mikloweit`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Botho Mikloweit' which is a person acting as an organisation in this context.

**Content:**
```
\bBotho\s+Mikloweit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_fa_linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Linz' which was missing from the general Finanzamt rule.

**Content:**
```
\bFA\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_fa_innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Innsbruck' which was missing from the general Finanzamt rule.

**Content:**
```
\bFA\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_kraftver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kraftver-Gastronomie GMBH' with hyphen handling.

**Content:**
```
\bKraftver-Gastronomie\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_gartgart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gartgart Dienstleistungen GMBH'.

**Content:**
```
\bGartgart\s+Dienstleistungen\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_nord_kellex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Nord Kellex'.

**Content:**
```
\bNord\s+Kellex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_raiffeisenkasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenkasse Retz-Pulkautal'.

**Content:**
```
\bRaiffeisenkasse\s+Retz-Pulkautal\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_klein_vorholt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Klein-Vorholt KI GMBH'.

**Content:**
```
\bKlein-Vorholt\s+KI\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_gogel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gogel Daten GMBH'.

**Content:**
```
\bGogel\s+Daten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_finanzamt_st_johann`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt St. Johann Tamsweg Zell am See'.

**Content:**
```
\bFinanzamt\s+St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_mur_ververzor`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mur Ververzor Betriebe'.

**Content:**
```
\bMur\s+Ververzor\s+Betriebe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_organisation_pastl_bachle`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Pastl+Bächle Handel'.

**Content:**
```
\bPastl\+Bächle\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_specific_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known entity names that were missing: Norconheim, Oppert Elektro, Nexdorf-Metall, Zimmerhackel Bau, Bezirksgericht Neunkirchen, Raiffeisenbank Rion Vöcklabruck.

**Content:**
```
\b(?:Norconheim|Oppert\s+Elektro|Nexdorf\-Metall|Zimmerhackel\s+Bau|Bezirksgericht\s+Neunkirchen|Raiffeisenbank\s+Rion\s+V\u00f6cklabruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_rheindigital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known organisation names that do not follow standard suffix patterns, like RheinDigital.

**Content:**
```
\bRheinDigital\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_company_suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches German corporate entities with suffixes (AG, GMBH, KG, etc.) ensuring the suffix is the end of the entity. Handles 'AG GmbH' typos by matching 'AG' and stopping before 'GmbH'.

**Content:**
```
\b([A-Z][A-Za-z0-9\s&+\-]+(?:\s+(?:und|\+|\&)[A-Z][A-Za-z0-9\s&+\-]+)*)\s+(AG|GMBH|KG|UG|OHG|Partnerschaft|Steuerberatungsgesellschaft|Wirtschaftsprüfungsgesellschaft)(?=\s*(?:GmbH|AG|KG|UG|OHG|Partnerschaft|Steuerberatungsgesellschaft|Wirtschaftsprüfungsgesellschaft|,|\.|\)|\]|:|$|\s+\d))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_depp_verkehr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Depp Versand'.

**Content:**
```
\bDepp\s+Versand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_sudevent`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'SüdEvent AG'.

**Content:**
```
\bSüdEvent\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_innluftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'InnLuftfahrt GMBH'.

**Content:**
```
\bInnLuftfahrt\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_lutkehans`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Lütkehans Event GMBH'.

**Content:**
```
\bLütkehans\s+Event\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_dorfkraft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Dorfkraft-Sanitär AG'.

**Content:**
```
\bDorfkraft-Sanitär\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_obernoder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Obernöder+Küsbert Touristik GMBH'.

**Content:**
```
\bObernöder\+Küsbert\s+Touristik\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `specific_entity_talost`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Talost GMBH'.

**Content:**
```
\bTalost\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_specific_org_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known organization names that are not covered by generic patterns, including those with 'und', '&', or specific suffixes.

**Content:**
```
\b(?:Schneppensieper\s+&\s+Bültbrunne\s+Touristik|Strohsack\s+und\s+Dresbeimdieke\s+Versand|Hagdorn\s+Robotik|Enns-Software|Gernot\s+Hirschkorn|WaldTouristik\s+Technologien|Liefeith\s+Immobilien|TalPflege|Valbruckzor-Energie|Raiffeisenbank\s+Karnische\s+Rion\s+Bankstelle\s+St\.Stefan|Unter\s+Gartglanz\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_firma_name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Firma' followed by a company name, capturing the name part only. Stops at suffixes or non-name characters.

**Content:**
```
\bFirma\s+([A-Z][A-Za-z0-9\s&+\-]+(?:\s+(?:und|\+|\&)[A-Z][A-Za-z0-9\s&+\-]+)*)\s*(?=AG|GMBH|KG|UG|OHG|Partnerschaft|Steuerberatungsgesellschaft|Wirtschaftsprüfungsgesellschaft|\s+im\s+|\s+am\s+|\s+in\s+|\s+vom\s+|\s+des\s+|\s+der\s+|\s+des\s+|\s+der\s+|\s+\d|\s+\.|\s+\)|\s+\]|:|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_company_suffix_refined`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches German corporate entities with suffixes, improved to handle 'und' and longer names.

**Content:**
```
(?<!\w)([A-Z][A-Za-z0-9\s&+\-]+(?:\s+(?:und|\+|\&)[A-Z][A-Za-z0-9\s&+\-]+)*)\s+(GmbH\s*&\s*Co\s*KG|GMBH|KG|UG|OHG|Partnerschaft|Steuerberatungsgesellschaft|Wirtschaftsprüfungsgesellschaft)(?=\s*(?:GmbH|AG|KG|UG|OHG|Partnerschaft|Steuerberatungsgesellschaft|Wirtschaftsprüfungsgesellschaft|,|\.|\)|\]|:|$|\s+\d|\s+\w|\s+im\s+|\s+am\s+|\s+in\s+|\s+vom\s+|\s+des\s+|\s+der\s+))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 190 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_42`)


Außerdem geht aus dem Curriculum hervor, dass es gemäß § 54 Abs 1 UG der Gruppe der  sozial- und wirtschaftswissenschaftlichen Studien zuzuordnen ist.

**False Positives:**

- `Abs 1 UG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_fa_purkersdorf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically matches FA Purkersdorf which might be missed by general patterns due to specific context.

**Content:**
```
\bFA\s+Purkersdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_tax_office`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific German tax office entities (Finanzamt/FA) with known district names found in training data.

**Content:**
```
\b(Finanzamt\s+(?:Oststeiermark|Amstetten\s+Melk\s+Scheibbs|Judenburg\s+Liezen)|FA\s+Judenburg\s+Liezen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_specific_orgs`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company and court names that failed in training: Chen Setzekorn, Ostgart AG, Istvan Gerart, InnMarine GMBH, HochLebensmittel Holding GMBH, Bezirksgericht Silz, LG Innsbruck, Landesgericht Innsbruck.

**Content:**
```
\b(?:Chen\s+Setzekorn|Ostgart\s+AG|Istvan\s+Gerart|InnMarine\s+GMBH|HochLebensmittel\s+Holding\s+GMBH|Bezirksgericht\s+Silz|LG\s+Innsbruck|Landesgericht\s+Innsbruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_specific_company_tm`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'T & M TRAUNSTEINER U. MITTERER KG'.

**Content:**
```
\bT\s*&\s*M\s+TRAUNSTEINER\s+U\.\s+MITTERER\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_specific_company_saxinger`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Saxinger Chalupsky & Partner Rechtsanwälte GmbH'.

**Content:**
```
\bSaxinger\s+Chalupsky\s*&\s*Partner\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_finanzstrafsenat`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzstrafsenat Wien 2'.

**Content:**
```
\b(Finanzstrafsenat\s+Wien\s+\d)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_betrugsbekampfung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Amt für Betrugsbekämpfung als Finanzstrafbehörde' and its genitive 'Amtes für Betrugsbekämpfung als Finanzstrafbehörde'.

**Content:**
```
\b(Amtes?\s+für\s+Betrugsbekämpfung\s+als\s+Finanzstrafbehörde)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 136 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` — partial — gold is substring of pred: `Amtes für Betrugsbekämpfung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_6`)


Entscheidungsgründe  Verfahrensgang:  Mit Erkenntnis des Spruchsenates I-1 als Organ des Amtes für Betrugsbekämpfung als  Finanzstrafbehörde vom 2. Mai 2024 wurde der Beschwerdeführer (in der Folge kurz: Bf.) der  Finanzvergehen a) der Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG und b) der  Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG für schuldig erkannt.

**False Positives:**

- `Amtes für Betrugsbekämpfung als  Finanzstrafbehörde` — partial — gold is substring of pred: `Amtes für Betrugsbekämpfung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Amtes für Betrugsbekämpfung`(organisation)

</details>

---

## `german_bdo_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BDO Austria GmbH WP- u. StBges.'.

**Content:**
```
\b(BDO\s+Austria\s+GmbH\s+WP-\s+u\.\s+StBges\.)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_lubomir_merschmeyer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Lubomir Merschmeyer'.

**Content:**
```
\b(Lubomir\s+Merschmeyer)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_zollamt_osterreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Zollamt Österreich'.

**Content:**
```
\b(Zollamt\s+Österreich)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_company_inet`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically matches INET company names which often have double spaces or specific suffixes.

**Content:**
```
\bINET\s+(?:Internet\s+Service|System\s+Informations)\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_verlag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches publishing houses ending in 'Verlag' or 'Verlag GmbH'.

**Content:**
```
\b([A-Z][a-zA-Z0-9\s&\-]+(?:\s+[A-Z][a-zA-Z0-9\s&\-]+)*)\s+Verlag(?:\s+GmbH)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_court_verfassungsgerichtshof`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Verfassungsgerichtshof' and its genitive form 'Verfassungsgerichtshofes'.

**Content:**
```
\b(Verfassungsgerichtshof(?:es)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_bezirkshauptmannschaft_bludenz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bezirkshauptmannschaft Bludenz'.

**Content:**
```
\bBezirkshauptmannschaft\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_pva`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'PVA' as an organization.

**Content:**
```
\bPVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_senecura`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'SeneCura' and its variations with location suffixes (Laurentius Park, Bludenz) and case variations (SENECURA, Senecura).

**Content:**
```
\bS(?:ENECURA|eneCura|enecura)(?:\s+(?:Laurentius\s+Park(?:\s+Bludenz)?|Bludenz))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_senecura_park`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'SeneCura Laurentius-Park Bludenz'.

**Content:**
```
\bSeneCura\s+Laurentius-Park\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_obb`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'ÖBB' (Austrian Federal Railways) as an organization.

**Content:**
```
\bÖBB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_krankenpflegevereins`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Krankenpflegevereins Bludenz' and its variations.

**Content:**
```
\bKrankenpflegevereins\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_finanzamt_innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamtes Innsbruck' and 'Finanzamt Innsbruck'.

**Content:**
```
\b(Finanzamt(?:es)?\s+Innsbruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_steuerberater_metzler`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Steuerberater Metzler & Adelsberger OG'.

**Content:**
```
\b(Steuerberater Metzler & Adelsberger OG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_wiederspan`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Wiederspan Beratung GMBH'.

**Content:**
```
\b(Wiederspan Beratung GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_mur_alver`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mur Alver OG'.

**Content:**
```
\b(Mur Alver OG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_retailers`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches common retail organizations: Ikea, Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz, Quelle.at.

**Content:**
```
\b(?:Ikea|Obi|Leiner|Möbelix|MömaX|Otto\.de|xxxLutz|Quelle\.at)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_london_film_academy`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'London Film Academy' and its typo variant 'London Film Acadamy'.

**Content:**
```
\b(London Film (?:Academy|Acadamy))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_bundeskanzleramt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundeskanzleramt' and its genitive form 'Bundeskanzleramtes'.

**Content:**
```
\b(Bundeskanzleramt(?:es)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_maschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches companies ending in 'Maschinenbau', strictly excluding preceding articles, prepositions, or context like 'der', 'die', 'das', 'bei', 'von', 'in', 'des', 'der', 'Gesamtrechtsnachfolger'.

**Content:**
```
(?<![A-Za-zäöüßÄÖÜ])\b([A-Z][a-zA-Z0-9\s&+\-]+(?:\s+[A-Z][a-zA-Z0-9\s&+\-]+)*)\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches companies ending in 'Luftfahrt', strictly excluding preceding articles, prepositions, or context like 'der', 'die', 'das', 'bei', 'von', 'in', 'des', 'der', 'Gesamtrechtsnachfolger'.

**Content:**
```
(?<![A-Za-zäöüßÄÖÜ])\b([A-Z][a-zA-Zäöüß\-]+(?:\s+[A-Z][a-zA-Zäöüß\-]+)*)\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_finanzamt_wien_1_23`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Wien 1/23' and its genitive form 'Finanzamtes Wien 1/23'.

**Content:**
```
\b(Finanzamt(?:es)?\s+Wien\s+1/23)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_company_technik_valseekel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Technik Valseekel GMBH'.

**Content:**
```
\bTechnik\s+Valseekel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_company_ernst_young`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Ernst & Young Steuerberatungsgesellschaft m.b.H.'.

**Content:**
```
\bErnst\s+&\s+Young\s+Steuerberatungsgesellschaft\s+m\.b\.H\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_company_deloitte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Deloitte Tax Wirtschaftsprüfungs GmbH'.

**Content:**
```
\bDeloitte\s+Tax\s+Wirtschaftsprüfungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_wiener_städtische`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Wiener Städtische'.

**Content:**
```
\bWiener\s+Städtische\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_allianz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Allianz'.

**Content:**
```
\bAllianz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific insurance company names ending in 'Versicherung' with strict context to avoid generic matches.

**Content:**
```
\b(?:Wiener Städtischen Versicherung|Allianz Versicherung|Wiener Städtische Versicherung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_court_vfgh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'VfGH' (Verfassungsgerichtshof) which was missing.

**Content:**
```
\bVfGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_ams_osterreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'AMS Österreich' and 'Arbeitsmarktservice'.

**Content:**
```
\b(?:AMS\s+Österreich|Arbeitsmarktservice)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_finanzamt_neunkirchen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamtes Neunkirchen Wr. Neustadt' (genitive) and 'Finanzamt Neunkirchen Wr. Neustadt'.

**Content:**
```
\bFinanzamt(?:es)?\s+Neunkirchen\s+Wr\.\s+Neustadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_landespolizeidirektion`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirketion Tirol' (preserving training data typo).

**Content:**
```
\b(Landespolizeidirketion\s+Tirol)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_bundesamt_soziales`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen' and genitive 'Bundesamts für Soziales und Behindertenwesen'.

**Content:**
```
\b(Bundesamts?\s+für\s+Soziales\s+und\s+Behindertenwesen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_arbeitsgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Arbeits- und Sozialgericht' and 'Arbeits- und Sozialgericht Wien'.

**Content:**
```
\b(Arbeits-\s+und\s+Sozialgericht(?:\s+Wien)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_ernst_young`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Ernst & Young Steuerberatungs-GmbH'.

**Content:**
```
\b(Ernst\s+&\s+Young\s+Steuerberatungs\-GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_f_personalservice`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'F Personalservice GmbH' and 'F Personal GmbH' variations found in training data.

**Content:**
```
\bF\s+(?:Personalservice\s+GmbH|Personal\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_universitaet_st_gallen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Universität St. Gallen' and 'Universität in St. Gallen'.

**Content:**
```
\bUniversit\u00e4t(?:\s+in\s+)?St\.\s+Gallen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_verwaltungsgericht_wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgericht Wien'.

**Content:**
```
\bVerwaltungsgericht\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_court_full_with_abbrev`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht (BFG)' and 'Verwaltungsgerichtshofes (VwGH)' as full entities.

**Content:**
```
\b(Bundesfinanzgericht(?:es)?\s*\(BFG\)|Verwaltungsgerichtshof(?:es)?\s*\(VwGH\))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_suva`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Schweizerische Unfallversicherungsanstalt (SUVA)' and 'SUVA'. Prioritizes full name to avoid split matches.

**Content:**
```
\bSchweizerische\s+Unfallversicherungsanstalt\s*\(SUVA\)\b|\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_dr_roland_gabl`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft'.

**Content:**
```
\bDr\.\s+Roland\s+Gabl\s+Rechtsanwalts\-\s+Kommandit\-Partnerschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_versorgungskasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Versorgungskasse Deutscher Unternehmen VVaG'.

**Content:**
```
\bVersorgungskasse\s+Deutscher\s+Unternehmen\s+VVaG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_deutsche_rentenversicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Deutschen Rentenversicherung Bund'.

**Content:**
```
\bDeutschen\s+Rentenversicherung\s+Bund\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_frontex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Frontex' and 'Europäische Grenzschutzagentur Frontex'.

**Content:**
```
\b(?:Europäische\s+Grenzschutzagentur\s+)?Frontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_easo`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'EASO'.

**Content:**
```
\bEASO\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_bm_fuer_inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BM für Inneres'.

**Content:**
```
\bBM\s+für\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_kriminalpolizei`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kriminalpolizei in Österreich'.

**Content:**
```
\bKriminalpolizei\s+in\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_suva_refined`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'SUVA' or full name, but excludes 'SUVA' when followed by hyphen and word (e.g. SUVA-Rente).

**Content:**
```
\b(?:Schweizerische\s+Unfallversicherungsanstalt\s*\(SUVA\)|SUVA)(?!\s*-\s*\w)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_bundesministerium_fuer_inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerium für Inneres' and its genitive form 'Bundesministeriums für Inneres'.

**Content:**
```
\b(Bundesministerium(?:s)?\s+für\s+Inneres)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_bundesministerium_fuer_finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerium für Finanzen' and its genitive form 'Bundesministeriums für Finanzen'.

**Content:**
```
\b(Bundesministerium(?:s)?\s+für\s+Finanzen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_bm_finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BM für Finanzen' and 'BM für Inneres'.

**Content:**
```
\b(BM\s+für\s+(?:Finanzen|Inneres))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_flughafen_münchen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Flughafen München' and 'Flughafen  München' (double space).

**Content:**
```
\b(Flughafen\s+München)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_oecd`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'OECD'.

**Content:**
```
\b(OECD)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_court_verwaltungsgerichtshof_typo`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the typo 'Verwaltungsgerichshofes' (missing 't').

**Content:**
```
\b(Verwaltungsgerichshofes)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_gesellschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Gesellschaft für ...' patterns (e.g., Österreichische Gesellschaft für Europapolitik).

**Content:**
```
\b([A-Z][a-z]+\s+Gesellschaft\s+für\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_universities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific university names: Universität Wien, Pädagogische Hochschule Wien (both forms), Uni Wien.

**Content:**
```
\b(?:Universität\s+Wien|Pädagogische\s+Hochschule\s+Wien|Uni\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_fachhochschulen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Fachhochschule and FH abbreviations for Kärnten.

**Content:**
```
\b(?:Fachhochschule\s+Kärnten|FH\s+Kärnten)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_specific_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific GmbH firm found in training data.

**Content:**
```
\bPaugger\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_svs_svb`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'SVS/SVB' as an organization.

**Content:**
```
\bSVS/SVB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_sozialversicherungsanstalt_bauern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherungsanstalt der Bauern'.

**Content:**
```
\bSozialversicherungsanstalt\s+der\s+Bauern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_psd_wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'PSD Wien'.

**Content:**
```
\bPSD Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_sozialversicherung_bauern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherung der Bauern'.

**Content:**
```
\bSozialversicherung der Bauern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_psycho_wagner`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Psychiatrie Otto Wagner Spital-'.

**Content:**
```
\bPsychiatrie Otto Wagner Spital-\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_bundesminister`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministers für Arbeit, Soziales und Konsumentenschutz' and its genitive form.

**Content:**
```
\bBundesministers für Arbeit, Soziales und Konsumentenschutz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_bundesamtes`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesamtes für Soziales und Behindertenwesen' (genitive) and 'Bundesamt für Soziales und Behindertenwesen' (nominative).

**Content:**
```
\bBundes(?:amtes|amt) für Soziales und Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_finanzpolizei`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzpolizei [City]'.

**Content:**
```
\bFinanzpolizei [A-Z][a-z]+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_rechtsanwaelte`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Rechtsanwälte [Name]' or 'Rechtsanwältin [Name]'.

**Content:**
```
\b(?:Rechtsanwälte|Rechtsanwältin) [A-Z][a-z]+(?:,\s*[A-Z][a-z]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_immobilienbuero`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Immobilienbüro [Name]'.

**Content:**
```
\bImmobilienbüro [A-Z][a-z]+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_roelfsen_versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Roelfsen Versicherung'.

**Content:**
```
\bRoelfsen\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `organisation_bdo_austria`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'BDO Austria GmbH WP- u. StBges.'.

**Content:**
```
\bBDO\s+Austria\s+GmbH\s+WP-\s+u\.\s+StBges\.\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_finanzamt_grossbetriebe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt für Großbetriebe' and its abbreviation 'FAG'.

**Content:**
```
\b(Finanzamt\s+für\s+Großbetriebe|FAG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_gmbh_entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific GmbH entities like 'A-GmbH' and 'Hausverwaltung-GmbH'.

**Content:**
```
\b(?:A-GmbH|Hausverwaltung-GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_erste_bank_wko`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Erste Bank' and 'WKO' which were missing in training.

**Content:**
```
\b(?:Erste\s+Bank|WKO)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_org_bundesministerium`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministeriums für Justiz' and similar ministry names.

**Content:**
```
\bBundesministerium(?:s)?\s+für\s+Justiz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_court_lg_fuer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'LG für [Location]' patterns like 'LG für ZRS Wien'.

**Content:**
```
\bLG\s+für\s+[A-ZäöüÄÖÜß]+(?:\s+[A-ZäöüÄÖÜß]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 29 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_50`)


Dieses Verfahren beim LG für  ZRS X, GZ 40S 35/13 i, sei am tt.08.2013 gem. § 152b IO aufgehoben worden.

**False Positives:**

- `LG für  ZRS X` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `german_court_bundesfinanzgericht_with_abbrev`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht (BFG)' as a single entity.

**Content:**
```
\b(Bundesfinanzgericht\s+\(BFG\))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_tax_authority_faö`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'FAÖ' as a standalone organization.

**Content:**
```
\b(FAÖ)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_lag_organisation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'LAG' as an organization (Landesabgabenbehörde or similar context).

**Content:**
```
\b(LAG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_eckhardt_steuerberatung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Eckhardt SteuerberatungsgmbH'.

**Content:**
```
\b(Eckhardt SteuerberatungsgmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_bdo_austria`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BDO Austria GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft'.

**Content:**
```
\b(BDO Austria GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_da_deutsche_versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'DA Deutsche Allgemeine Versicherung AG'.

**Content:**
```
\b(DA\s+Deutsche\s+Allgemeine\s+Versicherung\s+AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_geschenkartikel_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Geschenkartikel GmbH'.

**Content:**
```
\b(Geschenkartikel\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_aved_cosmetic`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'AVED cosmetic'.

**Content:**
```
\b(AVED\s+cosmetic)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_yoga_vidya_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Yoga Vidya GmbH'.

**Content:**
```
\b(Yoga\s+Vidya\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_specific_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Mag. Ghesla Steuerberater GmbH'.

**Content:**
```
\bMag\.\s+Ghesla\s+Steuerberater\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_suva_and_iv`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches SUVA and Eidgenössischen Invalidenversicherung, handling hyphenation in text.

**Content:**
```
\b(?:Schweizer(?:i-?\s*)?n\s+Unfallversicherungsanstalt\s*\(SUVA\)|SUVA|Eidgenössischen\s+Invalidenver-?\s*sicherung\s*\(IV\)|Eidgenössischen\s+Invalidenversicherung\s*\(IV\))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_legal_hospitals_and_tax`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches generic hospital and cantonal tax authority names like 'Kantonsspitals' and 'Steueramt des Kantons'.

**Content:**
```
\b(?:Steueramt\s+des\s+Kantons\s+[A-Za-z]+|Kantonsspitals\s+[A-Za-z\.\s]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

</details>

---

