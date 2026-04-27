# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-27T08:21:24.462632

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-27_v2/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 400 |
| Validation documents | 101 |
| Test documents | 12 |
| Train sentences | 2755 |
| Validation sentences | 213 |
| Test sentences | 1247 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 50 |
| Refinement iterations | 10 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | False |
| Enable Prune | False |
| Critic Interval | 0 |
| Audit Interval | 0 |
| Use GREX | False |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 40 |
| Refine per batch | 1 |
| Manually annotated examples | 1584 |
| First batch with manual data | 29 |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 81.8% |
| True Positives | 105 |
| False Positives | 137 |
| False Negatives | 151 |
| Total Gold Entities | 256 |
| Micro Precision | 43.4% |
| Micro Recall | 41.0% |
| Micro F1 | 42.2% |
| Macro F1 | 42.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `company_ampersand_name` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `tax_authority_fa` | 1.6% | 100.0% | 0.8% | 2 | 2 | 0 |
| `tax_authority_fa_complex` | 1.6% | 100.0% | 0.8% | 2 | 2 | 0 |
| `tax_authority_finanzamt_complex` | 1.6% | 100.0% | 0.8% | 2 | 2 | 0 |
| `org_finanzamt_oesterreich` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `org_landespolizeidirektion` | 3.1% | 100.0% | 1.6% | 4 | 4 | 0 |
| `org_bezirksgericht` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `org_bundesfinanzgericht_genitive` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `org_bundesfinanzgerichtes` | 9.7% | 100.0% | 5.1% | 13 | 13 | 0 |
| `org_ogk` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `org_finanzamt_oesterreich_nominative` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `org_magistrat_wien_ma` | 3.8% | 100.0% | 2.0% | 5 | 5 | 0 |
| `org_magistrat_wien_genitive` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `org_verwaltungsgerichtshof_genitive` | 28.0% | 95.5% | 16.4% | 44 | 42 | 2 |
| `org_verwaltungsgerichtshof` | 38.6% | 95.4% | 24.2% | 65 | 62 | 3 |
| `org_finanzamt_oesterreich_genitive` | 3.8% | 83.3% | 2.0% | 6 | 5 | 1 |
| `org_vwgh` | 2.2% | 3.4% | 1.6% | 116 | 4 | 112 |
| `company_bankhaus` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_steuerberatung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_fa_abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_traunluftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_sudversand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hyphenated_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_raiffeisenkasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_pastl_bachle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_nordtraval` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_gmbh_co_kg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_firma_prefix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_raiffeisenbank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_camelcase_industry` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_u_and` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_nowothnig_wind` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_www_fa` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_url_prefix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_rentenversicherung_bund` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_versorgungskasse_vvag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_ampersand_plus` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_single_letter_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_versicherungsag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_da_deutsche_allgemeine` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bundesministerium_finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bhag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_cofag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_faoe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_fag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_ams_oesterreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_landesgericht` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_lg_abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_verfassungsgerichtshof` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bundesministerium_justiz_genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_eidgenoessische_invalidenversicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_schweizerische_unfallversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_gmbh_co_kg_full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_suva` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_kantonsspitals_st_gallen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_steueramt_luzern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_single_word_gmbh` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `org_frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bm_fuer_inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bmi` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_kriminalpolizei_oesterreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_easo` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bundesministerium_fuer_inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_flughafen_munchen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_oecd` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_europaeische_grenzschutzagentur` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_europaeische_grenzschutzagentur_genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_ufs` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `company_multi_word_gmbh` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `tax_authority_finanzamt_wr_neustadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_finanzpolizei` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bfh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_london_film_academy` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bundeskanzleramtes` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_finanzamt_wien_klosterneuburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_finanzstrafsenat` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_vfgh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_reinemut_smoch` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_steuerberatungs_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_zollamt_oesterreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_universitaet` | 0.0% | 0.0% | 0.0% | 9 | 0 | 9 |
| `org_fachhochschule` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_hlf` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_hla_tourismus` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_fh_abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_amtes_fuer_betrugsbekampfung` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `company_f_personalservice` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_f_personal_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_landespolizeidirektion_typo` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_henken` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_retail_chains` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_mur_alver_og` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_pva` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_svs_svb` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_sozialversicherung_bauern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bundesamt_soziales` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_psd_wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_immobilienbuero` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_oesterreichische_gesundheitskasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_law_firm_complex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_hyphenated_acronym_gmbh` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bundesministeriums_fuer_inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bundesministeriums_fuer_finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `tax_authority_finanzamt_oststeiermark` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bundesministerin_finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_erste_bank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_wko` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_bezirkshauptmannschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `company_senecura` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_obb` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `org_krankenpflegevereins_bludenz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `org_bundesfinanzgerichtes`

**F1:** 0.097 | **Precision:** 1.000 | **Recall:** 0.051  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgerichtes' (genitive case) specifically.

**Content:**
```
\bBundesfinanzgerichtes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.051 | 0.097 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 229 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_171`)


3.3. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  15 von 16 Seite 16 von 16

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_19`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

## `org_verwaltungsgerichtshof_genitive`

**F1:** 0.280 | **Precision:** 0.955 | **Recall:** 0.164  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs' (genitive forms).

**Content:**
```
\bVerwaltungsgerichtshof(es|s)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.955 | 0.164 | 0.280 | 44 | 42 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 42 | 2 | 202 |

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
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_90`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

</details>

---

## `org_verwaltungsgerichtshof`

**F1:** 0.386 | **Precision:** 0.954 | **Recall:** 0.242  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive form 'Verwaltungsgerichtshofes' or 'Verwaltungsgerichtshofs'.

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

- `Verwaltungsgerichtshof` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

</details>

---

## `org_finanzamt_oesterreich_genitive`

**F1:** 0.038 | **Precision:** 0.833 | **Recall:** 0.020  

**Format:** `regex`  
**Description:**
Matches 'Finanzamtes Österreich' (genitive case) with parenthetical suffixes.

**Content:**
```
\bFinanzamtes\s+\u00d6sterreich(?:\s*\([^)]+\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.833 | 0.020 | 0.038 | 6 | 5 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 1 | 233 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Dr.in Estelle Niederholz` (person)
- `Hon.-Prof.in OStR Tosca Knoller` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `org_vwgh`

**F1:** 0.022 | **Precision:** 0.034 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'VwGH' (Verwaltungsgerichtshof).

**Content:**
```
\bVwGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.034 | 0.016 | 0.022 | 116 | 4 | 112 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 112 | 240 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_148`)


Wie der VwGH bereits in mehreren Erkenntnissen ausfgeührt hat erfordert die berufliche  Tätigkeit eines hauptberuflichen Musikers ein musikalisches Niveau, welches nur durch  regelmäßige Arbeit am Instrument zu erreichen und zu halten ist.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_94`)


Nach der Rechtsprechung des VwGH setzt eine Zwangsläufigkeit aus sittlichen Gründen voraus,  dass sich der Steuerpflichtige nach dem Urteil billig und gerecht denkender Menschen zu der  Leistung verpflichtet halten kann.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_226`)


Auf  die einheitliche zitierte Judikatur des VwGH wird verwiesen.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_41`)


Dazu zählen beispielsweise Erkrankungen, die die Berufsausbildung auf begrenzte Zeit  unterbrechen, oder Urlaube und Schulferien (VwGH vom 16.11.1993, 90/14/0108).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_44`)


Das bloße Aufrechterhalten eines  Berufswunsches ist der tatsächlichen Ausbildung nicht gleichzuhalten (VwGH 24.9.2009,  2009/16/0088, VwGH 21.01.2004, 2003/13/0157, VwGH 14.12.1995, 93/15/0133).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 3  |  spurious: 0

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_50`)


Entscheidend ist somit lediglich, ob der Empfänger die  Beträge zu Unrecht erhalten hat (vgl. VwGH 28.10.2009, 2008/15/0329).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_56`)


Ob eine Berufsausbildung im Sinne des FLAG 1967 vorliegt, ist eine Tatfrage (vgl. VwGH  16.11.1993, 90/14/0108), welche in freier Beweiswürdigung zu beantworten ist und einer  ordentlichen Revision nicht zugänglich ist.

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

</details>

---

## `org_universitaet`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Universität' followed by a location or name (e.g., Universität Innsbruck, Karl-Franzens- Universität Graz).

**Content:**
```
\bUniversität\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 9 | 0 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 9 | 211 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler Universität Linz`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler Universität Linz (JKU Linz)`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `Universität Linz` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler Universität Linz`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Johannes Kepler Universität Linz` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler  Universität Linz`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Johannes Kepler  Universität Linz` (organisation)
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

</details>

---

## `org_ufs`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'UFS' (Unabhängiger Finanzsenat).

**Content:**
```
\bUFS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 8 | 185 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**
- `WU` (organisation)
- `JKU` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_130`)


Allerdings ist durch die mit Einführung des UG 2002 erreichte Autonomie der Universitäten –  und damit verbunden die jeder Einrichtung mögliche individuelle Gestaltung der Studien – bei  einem Wechsel der Studieneinrichtung auch bei gleichbleibender Studienrichtung nicht in  jedem Fall eine Gleichwertigkeit gegeben (UFS 02.11.2011, RV/0289-F/11  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 96).

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_134`)


UFS 19.10.2010, RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_143`)


Die Gewährung der Familienbeihilfe  für volljährige Kinder stellt nach den näheren Regelungen des § 2 Abs. 1 lit. b FLAG ersichtlich  darauf ab, dass sich das Kind einer Berufsausbildung mit dem ernstlichen und zielstrebigen,  nach außen erkennbaren Bemühen um den Ausbildungserfolg unterzieht (UFS 19.10.2010,  RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `company_bankhaus`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bankhaus' followed by a name, a specific pattern seen in the data.

**Content:**
```
\bBankhaus\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_steuerberatung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Steuerberatungsgesellschaft' or similar professional firm names.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\s+&\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_fa_abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Fa.' followed by a company name (e.g., 'Fa. Bahrdt Digital').

**Content:**
```
\bFa\.\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\b
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
Matches 'TraunLuftfahrt' followed by 'Solutions' or other suffixes.

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

## `company_sudversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule to capture 'SüdVersand' and similar CamelCase compound names that were missed by the context rule.

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

## `company_hyphenated_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically matches hyphenated company names ending in GMBH/AG/KG to capture the full name (e.g., Kraftver-Gastronomie GMBH) before generic suffix rules.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s+(?:GmbH|AG|KG|GMBH|AG|KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_raiffeisenkasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenkasse' followed by location, ensuring full capture of the bank name including hyphenated locations.

**Content:**
```
\bRaiffeisenkasse\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_pastl_bachle`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule to capture the hyphenated/plus-sign compound name 'Pastl+Bächle Handel' which was missed by generic rules.

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

## `company_nordtraval`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule to capture 'NordTravalUmwelt AG' which was truncated by the generic CamelCase rule.

**Content:**
```
\bNordTravalUmwelt\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_gmbh_co_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches multi-word company names followed by 'GmbH & Co KG' (with variable whitespace), capturing the name part.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)\s+GmbH\s*&\s*Co\s*KG\b
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

## `org_verwaltungsgerichtshof`

**F1:** 0.386 | **Precision:** 0.954 | **Recall:** 0.242  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive form 'Verwaltungsgerichtshofes' or 'Verwaltungsgerichtshofs'.

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

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_162`)


Hier handelt es sich um keine Rechtsfragen von grundsätzlicher Bedeutung, weil das  Bundesfinanzgericht in rechtlicher Hinsicht der in der Begründung dieser Entscheidung  dargestellten Judikatur des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

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

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_94`)


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

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

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

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

- `Verwaltungsgerichtshof` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

</details>

---

## `org_verwaltungsgerichtshof_genitive`

**F1:** 0.280 | **Precision:** 0.955 | **Recall:** 0.164  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs' (genitive forms).

**Content:**
```
\bVerwaltungsgerichtshof(es|s)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.955 | 0.164 | 0.280 | 44 | 42 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 42 | 2 | 202 |

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
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_90`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_141`)


Ein Studienwechsel liegt nach der Rechtsprechung des Verwaltungsgerichtshofes dann vor,  wenn der Student das von ihm begonnene und bisher betriebene, aber noch nicht  abgeschlossene Studium nicht mehr fortsetzt und an dessen Stelle ein anderes unter den  Geltungsbereich des Studienförderungsgesetzes fallendes Studium beginnt (vgl. VwGH  08.01.2001, 2000/12/0053;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_172`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_173`)


Mit dem vorliegenden Erkenntnis folgt das Bundesfinanzgericht der zitierten einheitlichen  Rechtsprechung des Verwaltungsgerichtshofes (insbesondere VwGH 09.07.2008,  2005/13/0142).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_19`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_39`)


Da die  Uneinbringlichkeit einer Geldstrafe ohnehin unter der Sanktion des Vollzuges der  Ersatzfreiheitsstrafe steht, kommt dem Umstand der Gefährdung der Einbringlichkeit der  aushaftenden Forderung im Falle einer Geldstrafe laut Rechtsprechung des  Verwaltungsgerichtshofes kein Gewicht zu.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_52`)


Zur Unzulässigkeit der Revision  Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das  Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_50`)


Der Bf. bekämpft mit der gegenständlichen Beschwerde ausschließlich die mit dem  Straferkenntnis festgesetzte Strafhöhe, somit war entsprechend der ständigen Judikatur des  Verwaltungsgerichtshofes von einer Teilrechtskraft des Schuldspruches auszugehen (vgl. z.B.  VwGH 20.9.2013, 2013/17/0305).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_57`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes handelt es sich bei der  Strafzumessung innerhalb eines gesetzlichen Strafrahmens um eine Ermessensentscheidung,  die nach den Kriterien des § 19 VStG vorzunehmen ist (vgl. VwGH 06.04.2005, 2003/04/0031,  VwGH 17.02.2015, Ra 2015/09/0008).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_162`)


Hier handelt es sich um keine Rechtsfragen von grundsätzlicher Bedeutung, weil das  Bundesfinanzgericht in rechtlicher Hinsicht der in der Begründung dieser Entscheidung  dargestellten Judikatur des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_94`)


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_16`)


Gegen einen Beschluss des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil der Beschluss von der  Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_107`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes muss das Merkmal der  Zwangsläufigkeit auch der Höhe nach gegeben sein.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_23`)


Nach ständiger  Rechtsprechung des Verwaltungsgerichtshofes sei es Aufgabe des Vertreters, im  Verwaltungsverfahren allfällig vorliegende Gründe aufzuzeigen, die ihn daran gehindert hätten,  die Abgabenschuld am oder nach dem Fälligkeitstag zu begleichen (VwGH 23.03.2010,  2007/13/0137).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_26`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes obliege dem Vertreter der  Nachweis dafür, wie die Zahlungsmittel zur Verfügung gestanden seien und in welchem  Ausmaß die anderen Gläubiger der GmbH noch Befriedigung erlangten, zu erbringen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_87`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159) sei der Zumutbarkeit bei Heranziehung eines Haftungspflichtigen angesichts  lange verstrichener Zeit im Rahmen der behördlichen Ermessensausübung Bedeutung  beizumessen, allerdings stelle das herangezogene Erkenntnis nicht auf die zurückliegenden  Abgabenschulden ab, sondern auf den Zeitraum zwischen der Beendigung des Konkurses und  der Geltendmachung der Haftung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_205`)


Kausalität  Infolge der schuldhaften Pflichtverletzung durch den Bf. konnte die Abgabenbehörde nach der  Judikatur des Verwaltungsgerichtshofes (VwGH 17.5.2004, 2003/17/0134), auch davon  ausgehen, dass die Pflichtverletzung Ursache für die Uneinbringlichkeit der  haftungsgegenständlichen Abgaben war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_209`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_219`)


Auf die ständige Rechtsprechung des Verwaltungsgerichtshofes wird hingewiesen,  wonach einer Beschwerdevorentscheidung sowie einem Vorlagebericht Vorhaltscharakter  zukommt (vgl. VwGH vom 29.1.2020, Ra 2019/13/0071, VwGH vom 30.6.2021, Ra  2021/15/0048).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_105`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

</details>

---

## `org_bundesfinanzgerichtes`

**F1:** 0.097 | **Precision:** 1.000 | **Recall:** 0.051  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgerichtes' (genitive case) specifically.

**Content:**
```
\bBundesfinanzgerichtes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.051 | 0.097 | 13 | 13 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 0 | 229 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_171`)


3.3. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  15 von 16 Seite 16 von 16

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_19`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_74`)


sowie  zahlreiche Erkenntnisse des Bundesfinanzgerichtes).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_75`)


Wegen dieser Bindung ist der Zinsenbescheid nicht (mit Aussicht auf Erfolg) mit der  Begründung anfechtbar, der maßgebende Einkommensteuerbescheid sei inhaltlich  rechtswidrig (Ritz, BAO8, § 205 Tz 34 mit Hinweis auf die ständige Rechtsprechung des  Bundesfinanzgerichtes).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_8`)


2. Beweiswürdigung  Die Feststellungen ergeben sich eindeutig aus dem Akt des Finanzamtes und des  Bundesfinanzgerichtes und sind unstrittig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_16`)


Gegen einen Beschluss des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil der Beschluss von der  Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_105`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

## `org_magistrat_wien_ma`

**F1:** 0.038 | **Precision:** 1.000 | **Recall:** 0.020  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien' with optional 'MA 67' suffix.

**Content:**
```
\bMagistrat\s+der\s+Stadt\s+Wien(?:\s*,\s*MA\s+\d+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.020 | 0.038 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 123 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |

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

## `org_finanzamt_oesterreich_genitive`

**F1:** 0.038 | **Precision:** 0.833 | **Recall:** 0.020  

**Format:** `regex`  
**Description:**
Matches 'Finanzamtes Österreich' (genitive case) with parenthetical suffixes.

**Content:**
```
\bFinanzamtes\s+\u00d6sterreich(?:\s*\([^)]+\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.833 | 0.020 | 0.038 | 6 | 5 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 1 | 233 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Dr.in Estelle Niederholz` (person)
- `Hon.-Prof.in OStR Tosca Knoller` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

</details>

---

## `org_landespolizeidirektion`

**F1:** 0.031 | **Precision:** 1.000 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirektion' followed by location (e.g., Wien).

**Content:**
```
\bLandespolizeidirektion\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\b
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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_75`)


Diesen Lebensumständen stehen folgende inländische (österreichische) Anknüpfungspunkte  gegenüber: Nachweisliche Aufenthalte  - am 18. August 2019 (6-stündige Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" im Hinblick auf den beabsichtigten  Führerscheinerwerb),  vom 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019 sowie  17. bis 19. Februar 2020 (in Wien mit dem Bf. unternommene Fahrten gemäß § 19 Abs. 8 FSG;  am 20. Februar 2020 wurde vom Bf. die Überweisung von € 173,10 an die  Landespolizeidirektion Wien - Verkehrsamt vorgenommen).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_7`)


von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am  2. Mai 2025 um 11:09 Uhr in 1100 Wien, Gasse, beanstandet, da ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `org_finanzamt_oesterreich`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' and its genitive form 'Finanzamtes Österreich', including parenthetical suffixes like (DST12).

**Content:**
```
\bFinanzamt(?:s)?\s+\u00d6sterreich(?:\s*\([^)]+\))?\b
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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

## `org_finanzamt_oesterreich_nominative`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' (nominative case) to complement the existing genitive rule.

**Content:**
```
\bFinanzamt\s+\u00d6sterreich(?:\s*\([^)]+\))?\b
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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

## `org_vwgh`

**F1:** 0.022 | **Precision:** 0.034 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'VwGH' (Verwaltungsgerichtshof).

**Content:**
```
\bVwGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.034 | 0.016 | 0.022 | 116 | 4 | 112 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 112 | 240 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_148`)


Wie der VwGH bereits in mehreren Erkenntnissen ausfgeührt hat erfordert die berufliche  Tätigkeit eines hauptberuflichen Musikers ein musikalisches Niveau, welches nur durch  regelmäßige Arbeit am Instrument zu erreichen und zu halten ist.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_94`)


Nach der Rechtsprechung des VwGH setzt eine Zwangsläufigkeit aus sittlichen Gründen voraus,  dass sich der Steuerpflichtige nach dem Urteil billig und gerecht denkender Menschen zu der  Leistung verpflichtet halten kann.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_226`)


Auf  die einheitliche zitierte Judikatur des VwGH wird verwiesen.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_41`)


Dazu zählen beispielsweise Erkrankungen, die die Berufsausbildung auf begrenzte Zeit  unterbrechen, oder Urlaube und Schulferien (VwGH vom 16.11.1993, 90/14/0108).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_44`)


Das bloße Aufrechterhalten eines  Berufswunsches ist der tatsächlichen Ausbildung nicht gleichzuhalten (VwGH 24.9.2009,  2009/16/0088, VwGH 21.01.2004, 2003/13/0157, VwGH 14.12.1995, 93/15/0133).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 3  |  spurious: 0

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_50`)


Entscheidend ist somit lediglich, ob der Empfänger die  Beträge zu Unrecht erhalten hat (vgl. VwGH 28.10.2009, 2008/15/0329).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_56`)


Ob eine Berufsausbildung im Sinne des FLAG 1967 vorliegt, ist eine Tatfrage (vgl. VwGH  16.11.1993, 90/14/0108), welche in freier Beweiswürdigung zu beantworten ist und einer  ordentlichen Revision nicht zugänglich ist.

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_128`)


Es ist zur Klärung der Rechtsmäßigkeit der Rückforderung zunächst zu prüfen, ob ein  „Studienwechsel“ im Sinne des § 2 Abs. 1 lit. b FLAG 1967 überhaupt vorliegt, bevor auf einen  solchen Studienwechsel die Bestimmungen des § 17 StudFG angewendet werden können (BFG  26.02.2022, RV/2100101/2022 mit Verweis auf VwGH 09.07.2008, 2005/13/0142, Rechtssatz  JWR_2005130142_20080709X02).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_141`)


Ein Studienwechsel liegt nach der Rechtsprechung des Verwaltungsgerichtshofes dann vor,  wenn der Student das von ihm begonnene und bisher betriebene, aber noch nicht  abgeschlossene Studium nicht mehr fortsetzt und an dessen Stelle ein anderes unter den  Geltungsbereich des Studienförderungsgesetzes fallendes Studium beginnt (vgl. VwGH  08.01.2001, 2000/12/0053;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_150`)


Würde man die Kriterien betreffend einen  bloßen Studienortwechsel noch enger ziehen, bliebe für die vom Verwaltungsgerichtshof  gezogene Unterscheidung zwischen Studienortwechsel und Studienwechsel (VwGH  09.07.2008, 2005/13/0142) in der Praxis kein Raum, da wie bereits ausgeführt, angesichts des  Bologna-Studiensystems anders als vor Jahrzehnten wohl kaum noch zwei zu 100% identische  Studien in Österreich bzw. europaweit existieren.

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshof` (organisation)
- `Österreich` (country)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_167`)


Für die Überprüfung dieser  Frage erachte es der VwGH als ausreichend, die Unterscheidung auf die Kernfächer bzw. den  Kernbereich des Studiums zu reduzieren (VwGH 7.8.2001, 97/14/0068).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 2  |  spurious: 0

**Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 2  |  spurious: 0

**Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_173`)


Mit dem vorliegenden Erkenntnis folgt das Bundesfinanzgericht der zitierten einheitlichen  Rechtsprechung des Verwaltungsgerichtshofes (insbesondere VwGH 09.07.2008,  2005/13/0142).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_31`)


Die Gewährung von Zahlungserleichterungen für die Entrichtung von Geldstrafen und Kosten  nach dem Finanzstrafgesetz richtet sich damit nach § 212 BAO (vgl. VwGH 24.02.2011,  2010/16/0276, uHa Vorjudikatur).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_44`)


Ebenso trifft es allerdings zu, dass der  Ruin der wirtschaftlichen Existenz des Bestraften den mit der Bestrafung verfolgten Zweck  auch nicht sinnvoll erreicht (vgl. VwGH 24.9.2003, 2003/13/0084, ÖStZ 2004/190, ÖStZB  2004/109).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_50`)


Der Bf. bekämpft mit der gegenständlichen Beschwerde ausschließlich die mit dem  Straferkenntnis festgesetzte Strafhöhe, somit war entsprechend der ständigen Judikatur des  Verwaltungsgerichtshofes von einer Teilrechtskraft des Schuldspruches auszugehen (vgl. z.B.  VwGH 20.9.2013, 2013/17/0305).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_57`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes handelt es sich bei der  Strafzumessung innerhalb eines gesetzlichen Strafrahmens um eine Ermessensentscheidung,  die nach den Kriterien des § 19 VStG vorzunehmen ist (vgl. VwGH 06.04.2005, 2003/04/0031,  VwGH 17.02.2015, Ra 2015/09/0008).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 2  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_136`)


Ausschlaggebend ist daher, ob die konkrete Tätigkeit bei Anlegen eines  abstrakten Maßstabes ("typischerweise") einen Zusammenhang mit einer in der  Lebensführung begründeten Neigung aufweist, wie dies etwa bei einer nebenberuflich  betriebenen schriftstellerischen Tätigkeit zur Herausgabe eines Sachbuches, die erst auf Grund  der hobbymäßigen Beschäftigung mit jener Materie, die im Sachbuch behandelt wird, zu  bejahen ist (VwGH vom 26.4.2000, 96/14/0095).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_151`)


Solcherart kann der Mittelpunkt der Tätigkeit einer Konzertpianistin nach der  Verkehrsauffassung an dem Ort angenommen werden, an dem sie die überwiegende Zeit an  ihrem Instrument verbringt, im Beschwerdefall in dem in Rede stehenden Arbeitszimmer  (VwGH vom 24. Juni 2004, 2001/15/0052).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_65`)


Anspruchszinsen im Sinne des § 205 BAO sind eine objektive Rechtsfolge, um mögliche  Zinsvorteile oder Zinsnachteile auszugleichen, die sich aus unterschiedlichen Zeitpunkten der  Abgabenfestsetzung ergeben (VwGH 24.9.2008, 2007/15/0175).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_67`)


Eine rechtskräftige Einkommen- oder  Körperschaftsteuerfestsetzung wird vom Gesetz nicht verlangt (VwGH 27.3.2008,  2008/13/0036).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_72`)


Der Zinsenbescheid ist an die im Spruch des zur Nachforderung oder Gutschrift führenden  Bescheides ausgewiesene Nachforderung bzw. Gutschrift gebunden (Ritz, BAO8, § 205 mit  Hinweis auf VwGH 27.2.2008, 2005/13/0039;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_73`)


VwGH 27.3.2008, 2008/13/0036;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_78`)


es erfolgt daher keine Abänderung des ursprünglichen  Zinsenbescheides (Ritz, BAO8, § 205 Tz 35 mit Hinweis auf VwGH 28.5.2009, 2006/15/0316,  VwGH 31.1.2019, Ro 2018/15/0005; sowie zahlreiche Erkenntnisse des BFG).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 2  |  spurious: 0

**Gold Entities:**
- `BFG` (organisation)

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_62`)


Ob solche triftigen  Gründe vorliegen oder nicht, ist eine Frage der Beweiswürdigung (vgl. VwGH 5.10.2021,  Ra 2021/15/0059).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

**False Positives:**

- `VwGH` — type mismatch (gold: `VwGH`)

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `VwGH` (organisation)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_99`)


Eine allgemeine sittliche  Pflicht, Dritten beizustehen, besteht hingegen nicht (vgl. VwGH 27.9.1995, 92/15/0214).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_104`)


Auch Aufwendungen, die nicht von der  gesetzlichen Krankenversicherung getragen werden, können dem Steuerpflichtigen  zwangsläufig erwachsen, wenn sie aus triftigen Gründen medizinisch geboten sind (vgl. VwGH  11.2.2016, 2013/13/0064 mwN).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_108`)


Dabei ist zu beachten, dass triftige  medizinische Gründe auch höhere Aufwendungen als die von Sozialversicherungsträgern  finanzierten zwangsläufig erscheinen lassen (vgl. VwGH 11.2.2022, Ra 2020/13/0062).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_110`)


Die triftigen medizinischen Gründe  müssen vielmehr in feststehenden oder sich konkret abzeichnenden ernsthaften  gesundheitlichen Nachteilen bestehen, welche ohne die mit höheren Kosten verbundene  medizinische Betreuung eintreten würden (vgl. VwGH 13.5.1986, 85/14/0181).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_111`)


Will ein Steuerpflichtiger Aufwendungen als außergewöhnliche Belastung berücksichtigt  wissen, hat er selbst alle Umstände darzulegen, auf welche die abgabenrechtliche  Begünstigung gestützt werden kann (vgl. VwGH 22.12.2004, 2001/15/0116).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_123`)


Zum anderen handelt es sich bei der  Frage, ob triftige medizinische Gründe vorliegen oder nicht, um eine solche der  Beweiswürdigung, zu deren Überprüfung der Verwaltungsgerichtshof als Rechtsinstanz  grundsätzlich nicht berufen ist (vgl. VwGH 10.5.2021, Ra 2021/15/0031 und 5.10.2021,  Ra 2021/15/0059).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshof` (organisation)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_23`)


Nach ständiger  Rechtsprechung des Verwaltungsgerichtshofes sei es Aufgabe des Vertreters, im  Verwaltungsverfahren allfällig vorliegende Gründe aufzuzeigen, die ihn daran gehindert hätten,  die Abgabenschuld am oder nach dem Fälligkeitstag zu begleichen (VwGH 23.03.2010,  2007/13/0137).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_29`)


Unter diesen Umständen hafte er für die uneinbringlichen  Abgabenschuldigkeiten im vollen Ausmaß (z.B. VwGH 22.12.2005, 2005/15/0114).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_30`)


Werde der Nachweis einer Gläubigergleichbehandlung nicht in nachvollziehbarer Weise  erbracht, liege es im Ermessen des Finanzamtes, die Haftung für die genannten  Abgabenbeträge auszusprechen, bei Benachteiligung des Abgabengläubigers im Ausmaß der  nachgewiesenen Benachteiligung der Abgabenschuldigkeiten gegenüber den anderen  Verbindlichkeiten der GmbH (z.B. VwGH 29.1.2004, 2000/15/0168).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_31`)


Da der öffentliche Auftrag  zur Ergreifung aller Mittel, vollstreckbare Abgaben einzubringen, bei einer vorzuwerfenden  Pflichtverletzung allfällige Einzelinteressen verdränge (z.B. VwGH 10.10.2005, 2004/14/0112),  sähe sich das Finanzamt veranlasst, die gesetzliche Vertreterhaftung im erforderlichen Ausmaß  geltend zu machen.

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_52`)


Die Haftung gem. § 9 BAO sei eine Ausfallshaftung (VwGH 24.2.2004,  99/14/0278).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_53`)


Voraussetzung sei die objektive Uneinbringlichkeit der betreffenden Abgaben im  Zeitpunkt der Inanspruchnahme des Haftenden (VwGH 31.3.2004, 2003/13/0153).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_55`)


Zur Verletzung abgabenrechtlicher Pflichten des Vertreters führte das Finanzamt weiters aus,  dass es haftungsrelevant nur sei, wenn sich die Uneinbringlichkeit aus der Verletzung  abgabenrechtlicher Pflichten ergebe (VwGH 18.10.1995, 91/13/0038).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_56`)


Zu den abgabenrechtlichen Pflichten würden insbesondere gehören:  die Abgabenentrichtung aus den Mitteln, die der Vertreter verwalte,  die Führung gesetzlicher Aufzeichnungen (VwGH 30.5.1989, 89/14/0043),  die zeitgerechte Einreichung von Abgabenerklärungen (VwGH 29.5.2001, 2000/14/0006).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 2  |  spurious: 0

**Gold Entities:**

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_57`)


Die Pflicht des Vertreters, die vom Vertretenen geschuldeten Abgaben zu entrichten, bestehe  nur insoweit, als hierfür liquide Mittel vorhanden seien (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_58`)


Der Zeitpunkt, für den zu beurteilen sei, ob der Primärschuldnerin die für die  Abgabenentrichtung erforderlichen Mittel zur Verfügung standen, bestimme sich danach,  wann die Abgaben bei Beachtung der abgabenrechtlichen Vorschriften zu entrichten gewesen  wären (VwGH 27.4.2000, 98/15/0003;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_59`)


VwGH 31.10.2000, 95/15/0137).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_64`)


Er dürfe hierbei  Abgabenschulden nicht schlechter behandeln als die übrigen Schulden (VwGH 27.05.1998,  95/13/0170;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_65`)


VwGH 17.08.1998, 97/17/0096, 29.03.2001, 2000/16/0149).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_66`)


Er sei jedoch nicht verpflichtet, den Abgabengläubiger besser als die übrigen Gläubiger zu  behandeln (VwGH 17.8.1998, 98/17/0038).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_68`)


(VwGH 22.9.1999, 96/15/0049;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_69`)


VwGH 24.10.2000,  95/14/0090;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_70`)


VwGH 29.3.2001, 2000/14/0149).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_72`)


vielmehr habe der Vertreter das Fehlen ausreichender Mittel nachzuweisen   (VwGH 26.9.2000, 99/13/0090;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_73`)


VwGH 9.8.2001, 98/16/0348).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_74`)


Gelinge ein solcher Nachweis   nicht, könne die Haftung für den gesamten uneinbringlichen Abgabenrückstand geltend  gemacht werden (VwGH 27.9.2000, 95/14/0056, VwGH 29.3.2001, 2000/14/0149).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 2  |  spurious: 0

**Gold Entities:**

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_76`)


Die Behörde habe bei entsprechenden Behauptungen und diesbezüglichem  Beweisanbot die zur Entlastung des Vertreters angebotenen Beweise aufzunehmen und  erforderliche Präzisierungen abzufordern, jedenfalls aber konkrete Feststellungen über die  angebotenen Entlastungsbehauptungen zu treffen (VwGH 23.4.1998, 95/15/0145;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_77`)


VwGH  20.4.1999, 94/14/0147).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_85`)


(VwGH 25.6.1990,  89/15/0067).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_87`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159) sei der Zumutbarkeit bei Heranziehung eines Haftungspflichtigen angesichts  lange verstrichener Zeit im Rahmen der behördlichen Ermessensausübung Bedeutung  beizumessen, allerdings stelle das herangezogene Erkenntnis nicht auf die zurückliegenden  Abgabenschulden ab, sondern auf den Zeitraum zwischen der Beendigung des Konkurses und  der Geltendmachung der Haftung.

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_92`)


Ihm als Vertreter der GmbH sei der Nachweis oblegen, welcher Betrag bei Gleichbehandlung  sämtlicher Gläubiger bezogen auf die jeweiligen Fälligkeitszeitpunkte einerseits und das  Vorhandensein liquider Mittel andererseits - an die Abgabenbehörde zu entrichten gewesen  wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_95`)


Eine Ausnahme vom Gleichheitsgrundsatz bestehe für Abfuhrabgaben, wie die Lohnsteuer  (VwGH 29.6.1999, 99/14/0040;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_96`)


VwGH 22.2.2001, 2000/15/0227).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_99`)


die auf den gekürzten Lohnbetrag  entfallende Lohnsteuer sei zur Gänze zu entrichten (VwGH 16.2.2000, 95/15/0046).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_102`)


Eine weitere Ausnahme vom Gleichheitsgrundsatz bestehe für Abfuhrabgaben, wie die  Kapitalertragsteuer (VwGH 16.2.2000, 95/15/0046).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_104`)


Die Pflicht zur Einbehaltung und Abfuhr der Kapitalertragsteuer (§§ 95, 96 EstG 1998) hätten  unter der Sanktion des § 9 Abs. 1 BAO die Vertreter der juristischen Personen zu erfüllen  (VwGH 3.7.2003, 2000/15/0043).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_105`)


Dies gelte auch für die Kapitalertragsteuer aus verdeckten  Gewinnausschüttungen (VwGH 16.11.2006, 2002/14/0010).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_107`)


Eine bestimmte Schuldform sei hierfür nicht erforderlich  (VwGH 22.2.2000, 96/14/0158;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_108`)


VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_109`)


Daher reiche leichte  Fahrlässigkeit (VwGH 18.10.1995, 91/13/0037, VwGH 31.10.2000, 95/15/0137).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 2  |  spurious: 0

**Gold Entities:**

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_110`)


Der Vertreter habe dazutun, weshalb er nicht dafür habe Sorge getragen habe, dass der  Vertretene die Abgaben entrichtet habe, widrigenfalls von der Abgabenbehörde eine  schuldhafte Pflichtverletzung angenommen werden dürfe (VwGH 31.10.2000, 95/15/0137;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_111`)


VwGH 29.5.2001, 99/14/0277;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_112`)


VwGH 9.8.2001, 98/16/0348).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_113`)


In der Regel werde nämlich nur  der Vertreter jenen ausreichenden Einblick in die Gebarung des Vertretenen haben, der ihm  entsprechende Behauptungen und Nachweise ermögliche (VwGH 19.11.1998, 97/15/0115;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_114`)


VwGH 29.6.1999, 99/14/0128).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_115`)


Der Vertreter habe für die Möglichkeit des Nachweises seines  pflichtgemäßen Verhaltens vorzusorgen (VwGH 7.9.1990, 89/14/0132).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_116`)


Ihm obliege kein  negativer Beweis, sondern die konkrete (schlüssige) Darstellung der Gründe, die etwa der  rechtzeitigen Abgabenentrichtung entgegengestanden seien (VwGH 4.4.1990, 89/13/0212).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_121`)


Bei schuldhafter  Pflichtverletzung dürfe die Abgabenbehörde mangels dagegensprechender Umstände  annehmen, dass die Pflichtverletzung Ursache der Uneinbringlichkeit sei (VwGH 16.12.1999,  97/15/0051;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_122`)


VwGH 20.6.2000, 98/15/0084).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_141`)


Dazu führte das Finanzamt in der Begründung aus, dass die Geltendmachung einer Haftung in  das Ermessen der Abgabenbehörde gestellt sei (VwGH 23.1.1997, 95/15/0173), wobei die  Ermessensentscheidung im Sinne des § 20 BAO innerhalb der vom Gesetz gezogenen Grenzen  nach Billigkeit und Zweckmäßigkeit unter Berücksichtigung aller in Betracht kommenden  Umstände zu treffen sei.

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 75** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_143`)


Aus dem auf die Hereinbringung der Abgabenschuld beim Haftenden gerichteten  Besicherungszweck der Haftungsnorm folge, dass die Geltendmachung der Haftung in der  Regel ermessenskonform sei, wenn die betreffende Abgabe beim Primärschuldner  uneinbringlich sei (vgl. VwGH 25.6.1990, 89/15/0067).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 76** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 77** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_146`)


Selbst wenn auf Grund der derzeitigen wirtschaftlichen Situation des Beschwerdeführers die  Abgaben erschwert einbringlich seien, ließe sich daraus eine Unzumutbarkeit der  Haftungsinanspruchnahme nicht ableiten, weil es nach der Rechtsprechung nicht zutreffe, dass  die Haftung nur bis zur Höhe der aktuellen Einkünfte bzw. des aktuellen Vermögens geltend  gemacht werden dürfte (vgl. VwGH 29.

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 78** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_148`)


Wie bereits im Haftungsbescheid vom 11.01.2016 ausgeführt, obliege dem Vertreter der GmbH  der Nachweis, welcher Betrag bei Gleichbehandlung sämtlicher Gläubiger bezogen auf die  jeweiligen Fälligkeitszeitpunkte einerseits und das Vorhandensein liquider Mittel andererseits  an die Abgabenbehörde zu entrichten gewesen wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 79** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 80** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 81** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_189`)


Er hat also darzutun, weshalb er nicht dafür Sorge tragen  konnte, dass die Gesellschaft die anfallenden Abgaben rechtzeitig entrichtet hat, andernfalls  von der Abgabenbehörde eine schuldhafte Pflichtverletzung angenommen werden darf (vgl.  VwGH 16.12.2009, 2009/15/0127).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 82** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_190`)


Wird eine Abgabe nicht entrichtet, weil der Vertretene überhaupt keine liquiden Mittel hat, so  verletzt der Vertreter dadurch keine abgabenrechtliche Pflicht (VwGH 20.9.1996, 94/17/0420;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 83** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_191`)


VwGH 28.5.2008, 2006/15/0089).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 84** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_192`)


Der Geschäftsführer haftet für nicht entrichtete Abgaben der Gesellschaft auch dann, wenn die  Mittel, die ihm für die Entrichtung aller Verbindlichkeiten zur Verfügung gestanden sind, hierzu  nicht ausreichen; es sei denn, er weist nach, dass er diese Mittel anteilig für die Begleichung  aller Verbindlichkeiten verwendet, die Abgabenschulden daher im Verhältnis nicht schlechter  behandelt hat als andere Verbindlichkeiten (VwGH 19.5.2015, 2013/16/0016).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 85** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_195`)


Am Bf., dem als Geschäftsführer der Primärschuldnerin ausreichend Einblick in die Gebarung  zustand, war es gelegen, das Ausmaß der quantitativen Unzulänglichkeit der in den  Fälligkeitszeitpunkten der Abgaben zur Verfügung stehenden Mittel nachzuweisen (VwGH  19.11.1998, 97/15/0115), da nicht die Abgabenbehörde das Ausreichen der Mittel zur  Abgabenentrichtung nachzuweisen hat, sondern der zur Haftung herangezogene  Geschäftsführer das Fehlen ausreichender Mittel (VwGH 23.4.1998, 95/15/0145).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 2  |  spurious: 0

**Gold Entities:**

**Example 86** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_197`)


Tritt der Vertreter diesen  Nachweis nicht an, dann kann ihm die uneinbringliche Abgabe zur Gänze vorgeschrieben  werden (VwGH 28.9.2004, 2001/14/0176).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 87** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 88** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_199`)


VwGH 2.7.2015, 2013/16/0220;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 89** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_200`)


VwGH 24.1.2013, 2012/16/0100), womit dieser  klarstellte, dass eine Betrachtung der Gläubigergleichbehandlung zum jeweiligen  Fälligkeitszeitpunkt zu erfolgen hatte, wurde mit dem Erkenntnis vom 28.6.2022, Ra  2020/13/0067, aufgegeben:  "Dabei kommt es für den Nachweis der Gläubigergleichbehandlung nicht nur auf die  liquiden Mittel zum Fälligkeitstag an, die den an diesem einen Tag jeweilig fälligen  Verbindlichkeiten gegenüberzustellen sind, weil eine derartige Betrachtung für nur einen  einzigen Tag im Monat ohne Berücksichtigung der vorhandenen liquiden Mittel für die  Zeiträume nach der Fälligkeit der Abgaben keinen Nachweis über eine  Gläubigergleichbehandlung geben kann."

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 90** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_204`)


Erfüllung der vollen Abgabenverbindlichkeiten kommt eine Beschränkung der Haftung des Bf.  bloß auf einen Teil der von der Haftung betroffenen Abgabenschulden nicht in Betracht (VwGH  21.1.1991, 90/15/0055).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 91** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_205`)


Kausalität  Infolge der schuldhaften Pflichtverletzung durch den Bf. konnte die Abgabenbehörde nach der  Judikatur des Verwaltungsgerichtshofes (VwGH 17.5.2004, 2003/17/0134), auch davon  ausgehen, dass die Pflichtverletzung Ursache für die Uneinbringlichkeit der  haftungsgegenständlichen Abgaben war.

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 92** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_208`)


Aus dem auf die  Hereinbringung der Abgabenschuld beim Haftenden gerichteten Besicherungszweck der  Haftungsnorm folgt, dass die Geltendmachung der Haftung in der Regel ermessenskonform ist,  wenn die betreffende Abgabe beim Primärschuldner uneinbringlich ist (VwGH  25.6.1990, 89/15/0067).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 93** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_209`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 94** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_210`)


VwGH 16.10.2014, Ro 2014/16/0066) ist dem Element der Zumutbarkeit der  Heranziehung eines Haftungspflichtigen angesichts langer verstrichener Zeit im Rahmen der  behördlichen Ermessensübung besondere Bedeutung beizumessen.

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

**Example 95** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_219`)


Auf die ständige Rechtsprechung des Verwaltungsgerichtshofes wird hingewiesen,  wonach einer Beschwerdevorentscheidung sowie einem Vorlagebericht Vorhaltscharakter  zukommt (vgl. VwGH vom 29.1.2020, Ra 2019/13/0071, VwGH vom 30.6.2021, Ra  2021/15/0048).

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*
- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 2  |  spurious: 0

**Gold Entities:**
- `Verwaltungsgerichtshofes` (organisation)

**Example 96** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_46`)


2. Der Säumniszuschlag ist eine „Sanktion eigener Art“ (zB VwGH 21.4.1983, 83/16/0016;

**False Positives:**

- `VwGH` — no gold match — missing annotation *(seen as TP elsewhere)*

> partial: 0  |  likely missing annotation: 1  |  spurious: 0

**Gold Entities:**

</details>

---

## `tax_authority_fa`

**F1:** 0.016 | **Precision:** 1.000 | **Recall:** 0.008  

**Format:** `regex`  
**Description:**
Matches 'FA' followed by location including numbers. Updated to exclude trailing words like 'In', 'An', 'Der' using negative lookahead.

**Content:**
```
\bFA\s+(?:St\.?\s+)?[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+\d+(?:/\s*\d+)+)?(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?!\s+(?:In|An|Der|Die|Das|Dem|Den|Von|Zu|Mit|Auf|Bei|Für|Ohne|Gegen|Über|Unter|Vor|Nach|Seit|Wegen|Trotz|Statt|Durch|Ohne|Neben|Hinter|Vor|Zwischen|Über|Unter|Vor|Nach|Seit|Wegen|Trotz|Statt|Durch|Ltd|GmbH|AG|KG|\.com|\.org|\.net))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.008 | 0.016 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 254 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

</details>

---

## `tax_authority_fa_complex`

**F1:** 0.016 | **Precision:** 1.000 | **Recall:** 0.008  

**Format:** `regex`  
**Description:**
Matches 'FA' with complex locations including 'am' and multi-word names. Updated to ensure full capture.

**Content:**
```
\bFA\s+(?:St\.?\s+)?[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+am\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+\d+(?:/\s*\d+)+)?(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?!\s+(?:Ltd|GmbH|AG|KG|\.com|\.org|\.net))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.008 | 0.016 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 254 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

</details>

---

## `tax_authority_finanzamt_complex`

**F1:** 0.016 | **Precision:** 1.000 | **Recall:** 0.008  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' followed by location including numbers like '1/23'. Updated to ensure full capture and handle specific multi-word locations like 'Braunau Ried Schärding'.

**Content:**
```
\bFinanzamt\s+(?:St\.?\s+)?[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+am\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+\d+(?:/\s*\d+)+)?(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?!\s+(?:Revision|Erhebung|Antrag|Bescheid|Verfahren|Sache|Fall|Entscheidung|Urteil|Bemerkung|Hinweis|Beweis|Klage|Rechtsmittel|Wiederaufnahme|Berufung|Revisionsbeschluss|Revisionsverfahren|Revisionsentscheidung|Revisionsurteil|Revisionsbescheid|Revisionsantrag|Revisionsanrufung|Revisionsvorlage|Revisionsvorbringen|Revisionsgr\u00fcnde|Revisionsbegr\u00fcndung|Revisionsantwort|Revisionsverhandlung|Ltd|GmbH|AG|KG|\.com|\.org|\.net))\b
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

## `company_ampersand_name`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches company names containing '&' with suffixes, now including 'OG' to prevent truncation.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\s+&\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?:GmbH|GMBH|AG|KG|Rechtsanw\u00e4lte|OG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 83 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Anwälte Mandl & Mitterbauer GmbH` | `Anwälte Mandl & Mitterbauer GmbH` |

</details>

---

## `org_bezirksgericht`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Bezirksgericht' followed by a location name (e.g., Bezirksgericht Silz).

**Content:**
```
\bBezirksgericht\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 234 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Purkersdorf` | `Bezirksgericht Purkersdorf` |

</details>

---

## `org_bundesfinanzgericht_genitive`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgerichts' (genitive case) specifically.

**Content:**
```
\bBundesfinanzgerichts\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 99 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_93`)


Diese Sachverhaltsfeststellungen ergeben sich nach Dafürhalten des Bundesfinanzgerichts aus  den vorgelegten Akten des Abgabenverfahrens, dem Vorbringen der Bf. in seiner Beschwerde  sowie den Erhebungen durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

</details>

---

## `org_ogk`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\b\u00d6GK\b
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

## `org_magistrat_wien_genitive`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Magistrates der Stadt Wien' (genitive form).

**Content:**
```
\bMagistrates\s+der\s+Stadt\s+Wien(?:\s*,\s*MA\s+\d+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 127 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

</details>

---

## `company_bankhaus`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bankhaus' followed by a name, a specific pattern seen in the data.

**Content:**
```
\bBankhaus\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_steuerberatung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Steuerberatungsgesellschaft' or similar professional firm names.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\s+&\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_fa_abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Fa.' followed by a company name (e.g., 'Fa. Bahrdt Digital').

**Content:**
```
\bFa\.\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\b
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
Matches 'TraunLuftfahrt' followed by 'Solutions' or other suffixes.

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

## `company_sudversand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule to capture 'SüdVersand' and similar CamelCase compound names that were missed by the context rule.

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

## `company_hyphenated_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specifically matches hyphenated company names ending in GMBH/AG/KG to capture the full name (e.g., Kraftver-Gastronomie GMBH) before generic suffix rules.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s+(?:GmbH|AG|KG|GMBH|AG|KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_raiffeisenkasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Raiffeisenkasse' followed by location, ensuring full capture of the bank name including hyphenated locations.

**Content:**
```
\bRaiffeisenkasse\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_pastl_bachle`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule to capture the hyphenated/plus-sign compound name 'Pastl+Bächle Handel' which was missed by generic rules.

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

## `company_nordtraval`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule to capture 'NordTravalUmwelt AG' which was truncated by the generic CamelCase rule.

**Content:**
```
\bNordTravalUmwelt\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_gmbh_co_kg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches multi-word company names followed by 'GmbH & Co KG' (with variable whitespace), capturing the name part.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)\s+GmbH\s*&\s*Co\s*KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_firma_prefix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Firma' followed by a company name. Updated to ensure the capture group ($1) contains only the company name, excluding the prefix 'Firma', and handles single-word names correctly.

**Content:**
```
\bFirma\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+\+\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\b
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
Matches 'Raiffeisenbank' followed by location or name parts, including 'Bankstelle' and subsequent location identifiers. Updated to handle multi-word locations after Bankstelle.

**Content:**
```
\bRaiffeisenbank\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+Bankstelle\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_camelcase_industry`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches CamelCase compound names followed by industry terms. Added 'Marine', 'Transport', 'Digital' to the list of industry terms.

**Content:**
```
\b[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\s+(?:Robotik|Software|Immobilien|Touristik|Versand|Handel|Technologien|Energie|Maschinenbau|Luftfahrt|Versicherung|Verlag|IT|Wirtschaftspr\u00fcfung|Steuerberatung|Marine|Transport|Digital)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_u_and`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names containing 'u.' (und) followed by a suffix like GMBH/AG. Updated to capture the full name including the suffix.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+u\.\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s+(?:GmbH|GMBH|AG|KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_nowothnig_wind`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule to capture 'Nowothnig Wind' which is a two-word proper noun without a suffix.

**Content:**
```
\bNowothnig\s+Wind\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_www_fa`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule to capture 'www.FA...' patterns which are often missed or truncated by the standard FA rule.

**Content:**
```
\bwww\.FA\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?!\s+\.com)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_url_prefix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches URLs or protocols preceding organization names (e.g., '://www.Donau Furtkraftwald AG').

**Content:**
```
\b(?:https?://|://)www\.[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_rentenversicherung_bund`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Deutschen Rentenversicherung Bund' specifically.

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

## `org_versorgungskasse_vvag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Versorgungskasse Deutscher Unternehmen VVaG' specifically.

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

## `company_ampersand_plus`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names containing '+' or '&' with suffixes, specifically handling the '+' operator which was previously truncated. Ensures the full name including the '+' part is captured.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+\+\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)\s+(?:GmbH|GMBH|AG|KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_single_letter_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names starting with a single letter followed by a hyphen and suffix (e.g., A-GmbH, B-GmbH).

**Content:**
```
\b[A-Z]\s*-\s*(?:GmbH|GMBH|AG|KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_versicherungsag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'VersicherungsAG' (no space) or 'Versicherungs-AG'.

**Content:**
```
\b[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\s+Versicherungs(?:AG|\-AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_da_deutsche_allgemeine`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'DA Deutsche Allgemeine Versicherung AG' pattern (Initial + Name + AG).

**Content:**
```
\bDA\s+Deutsche\s+Allgemeine\s+Versicherung\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bundesministerium_finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerium für Finanzen'.

**Content:**
```
\bBundesministerium\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bhag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific acronym BHAG (Bundesheer-Haftungs- und Abwicklungs-Gesellschaft or similar context).

**Content:**
```
\bBHAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_cofag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific acronym COFAG (Central Office for the Settlement of Claims).

**Content:**
```
\bCOFAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_faoe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'FAÖ' for Finanzamt Österreich.

**Content:**
```
\bFA\u00d6\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_fag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'FAG' for Finanzamt für Großbetriebe.

**Content:**
```
\bFAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_ams_oesterreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'AMS Österreich' and 'Arbeitsmarktservice (AMS)'.

**Content:**
```
\b(AMS\s+Österreich|Arbeitsmarktservice\s*\(\s*AMS\s*\))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_landesgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Landesgericht' followed by a location name (e.g., Landesgericht Innsbruck).

**Content:**
```
\bLandesgericht\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_lg_abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'LG' followed by a location or specific court identifier (e.g., LG Innsbruck, LG für ZRS Wien).

**Content:**
```
\bLG\s+(?:f\u00fcr\s+)?[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_verfassungsgerichtshof`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Verfassungsgerichtshof' and its genitive form 'Verfassungsgerichtshofes'.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bundesministerium_justiz_genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministeriums für Justiz' (genitive case).

**Content:**
```
\bBundesministeriums\s+f\u00fcr\s+Justiz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_eidgenoessische_invalidenversicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Eidgenössischen Invalidenversicherung' and optionally '(IV)'.

**Content:**
```
\bEidgen\u00f6ssischen\s+Invalidenversicherung(?:\s*\(\s*IV\s*\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_schweizerische_unfallversicherungsanstalt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Schweizerischen Unfallversicherungsanstalt' and optionally '(SUVA)'.

**Content:**
```
\bSchweizeri-?schen\s+Unfallversicherungsanstalt(?:\s*\(\s*SUVA\s*\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_gmbh_co_kg_full`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches full company names ending in 'GmbH & Co KG' including the name part, ensuring the whole string is captured as one entity. Updated to handle multi-word names with '&' and 'und'.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+&\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+u\.\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+und\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s+GmbH\s*&\s*Co\s*KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_suva`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'SUVA' (Schweizerische Unfallversicherungsanstalt).

**Content:**
```
\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_kantonsspitals_st_gallen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kantonsspitals St. Gallen' (genitive) and 'Kantonsspital St. Gallen' (nominative).

**Content:**
```
\bKantonsspital(?:s)?\s+St\.?\s+Gallen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_steueramt_luzern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Steueramt des Kantons Luzern' and its genitive form 'Steueramtes des Kantons Luzern'.

**Content:**
```
\bSteueramt(?:s)?\s+des\s+Kantons\s+Luzern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_single_word_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches single-word company names followed by GMBH/AG/KG. Lowered priority to ensure multi-word rules (including acronyms) take precedence.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]*[A-Z]?|[A-Z])\s+(?:GmbH|GMBH|AG|KG)\b(?!\s*&\s*Co\s*KG)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 108 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Steuerberatung  GmbH` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**
- `Franz Josefskai 53/2/10, 1010 Wien` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `94-300/0486` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mitterbauer GmbH` — partial — pred ⊂ gold: `Anwälte Mandl & Mitterbauer GmbH`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Dr.in Estelle Niederholz` (person)
- `Hon.-Prof.in OStR Tosca Knoller` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

</details>

---

## `org_frontex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Frontex' (European Border and Coast Guard Agency).

**Content:**
```
\bFrontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bm_fuer_inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BM für Inneres' (Federal Ministry of the Interior).

**Content:**
```
\bBM\s+f\u00fcr\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bmi`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'BMI' (Bundesministerium für Inneres).

**Content:**
```
\bBMI\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_kriminalpolizei_oesterreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kriminalpolizei in Österreich'.

**Content:**
```
\bKriminalpolizei\s+in\s+\u00d6sterreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_easo`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'EASO' (European Asylum Support Office).

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

## `org_bundesministerium_fuer_inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerium für Inneres'.

**Content:**
```
\bBundesministerium\s+f\u00fcr\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_flughafen_munchen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Flughafen München'.

**Content:**
```
\bFlughafen\s+M\u00fcnchen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_oecd`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'OECD'.

**Content:**
```
\bOECD\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_europaeische_grenzschutzagentur`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Europäische Grenzschutzagentur Frontex' and its genitive form.

**Content:**
```
\bEurop\u00e4ische\s+Grenzschutzagentur\s+Frontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_europaeische_grenzschutzagentur_genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Europäischen Grenzschutzagentur Frontex' (genitive).

**Content:**
```
\bEurop\u00e4ischen\s+Grenzschutzagentur\s+Frontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_ufs`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'UFS' (Unabhängiger Finanzsenat).

**Content:**
```
\bUFS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 8 | 185 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**
- `WU` (organisation)
- `JKU` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_130`)


Allerdings ist durch die mit Einführung des UG 2002 erreichte Autonomie der Universitäten –  und damit verbunden die jeder Einrichtung mögliche individuelle Gestaltung der Studien – bei  einem Wechsel der Studieneinrichtung auch bei gleichbleibender Studienrichtung nicht in  jedem Fall eine Gleichwertigkeit gegeben (UFS 02.11.2011, RV/0289-F/11  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 96).

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_134`)


UFS 19.10.2010, RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_143`)


Die Gewährung der Familienbeihilfe  für volljährige Kinder stellt nach den näheren Regelungen des § 2 Abs. 1 lit. b FLAG ersichtlich  darauf ab, dass sich das Kind einer Berufsausbildung mit dem ernstlichen und zielstrebigen,  nach außen erkennbaren Bemühen um den Ausbildungserfolg unterzieht (UFS 19.10.2010,  RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_164`)


vgl. auch UFS  16.02.2007, RV/0189-G/06).

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_26`)


Von einer Liebhabereitätigkeit kann ja wohl nur dann gesprochen werden, wenn jemand,  dessen Hauptberuf sich von seinem Hobby, dem er aus besonderer Neigung nachgeht (siehe  UFS 27.11.2003, RV/0509-L/02), unterscheidet, und dieses Hobby zu steuerlich unbeachtlichen  Gesamtverlusten führt.

**False Positives:**

- `UFS` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**

</details>

---

## `company_multi_word_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches multi-word company names ending in GmbH/AG/KG. Updated to allow the first word to be an all-caps acronym (e.g., KQPC) to prevent splitting 'KQPC Versand GMBH'.

**Content:**
```
\b([A-Z]{2,}\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+|[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)\s+(?:GmbH|GMBH|AG|KG)\b(?!\s*&\s*Co\s*KG)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 108 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Wirtschaftsprüfung Steuerberatung  GmbH` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**
- `Franz Josefskai 53/2/10, 1010 Wien` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `94-300/0486` (tax_number)

</details>

---

## `tax_authority_finanzamt_wr_neustadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule for 'Finanzamt Neunkirchen Wr. Neustadt' to handle spacing and abbreviations, including cases with double spaces.

**Content:**
```
\bFinanzamt(?:s)?\s+Neunkirchen\s+Wr\.?\s+Neustadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_finanzpolizei`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzpolizei' followed by a location name.

**Content:**
```
\bFinanzpolizei\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bfh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'BFH' (Bundesfinanzhof).

**Content:**
```
\bBFH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_london_film_academy`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'London Film Academy' and the typo 'London Film Acadamy'.

**Content:**
```
\bLondon\s+Film\s+(?:Academy|Acadamy)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bundeskanzleramtes`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundeskanzleramtes' (genitive case).

**Content:**
```
\bBundeskanzleramtes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_finanzamt_wien_klosterneuburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamtes Wien 9/18/19 Klosterneuburg' specifically to handle the complex location with numbers.

**Content:**
```
\bFinanzamt(?:s)?\s+Wien\s+\d+/\d+/\d+\s+Klosterneuburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_finanzstrafsenat`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzstrafsenat' followed by location (e.g., Wien 2).

**Content:**
```
\bFinanzstrafsenat\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+\d+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_vfgh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'VfGH' (Verwaltungsgerichtshof).

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

## `company_reinemut_smoch`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule to capture 'Reinemut + Smoch Handel' which was missed by generic rules.

**Content:**
```
\bReinemut\s+\+\s+Smoch\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_steuerberatungs_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Steuerberatungs GmbH' (singular 'Steuerberatungs' instead of 'Steuerberatungsgesellschaft').

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+&\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s+Steuerberatungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_zollamt_oesterreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Zollamt Österreich'.

**Content:**
```
\bZollamt\s+\u00d6sterreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_universitaet`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Universität' followed by a location or name (e.g., Universität Innsbruck, Karl-Franzens- Universität Graz).

**Content:**
```
\bUniversität\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 9 | 0 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 9 | 211 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler Universität Linz`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler Universität Linz (JKU Linz)`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `Universität Linz` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler Universität Linz`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Johannes Kepler Universität Linz` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler  Universität Linz`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Johannes Kepler  Universität Linz` (organisation)
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler Universität Linz (`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler Universität Linz (JKU)`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_124`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes Kepler Universität Linz`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz` (organisation)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_147`)


Nach unstrittigem Sachverhalt hat die Tochter der Bf. mit dem Wechsel vom Bachelorstudium  Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien nach dem  Sommersemester 2019, somit nach dem vierten Semester des seit Oktober 2017 dort  betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der Johannes  Kepler Universität Linz mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel  vorgenommen.

**False Positives:**

- `Universität Linz` — partial — pred ⊂ gold: `Johannes  Kepler Universität Linz`

> partial: 1  |  likely missing annotation: 0  |  spurious: 0

**Gold Entities:**
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes  Kepler Universität Linz` (organisation)

</details>

---

## `org_fachhochschule`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Fachhochschule' followed by a location or name (e.g., Fachhochschule Kärnten).

**Content:**
```
\bFachhochschule\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_hlf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'HLF' (Höhere Lehranstalt für) followed by a location (e.g., HLF Krems/Donau).

**Content:**
```
\bHLF\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:/[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_hla_tourismus`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Höhere Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit' and its variations.

**Content:**
```
\bH\u00f6here\s+Lehranstalt\s+f\u00fcr\s+Tourismus(?:,\s+Eventmanagement)?(?:,\s+Sport\s+und\s+Freizeit)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_fh_abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FH' followed by a location (e.g., FH Kärnten).

**Content:**
```
\bFH\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_amtes_fuer_betrugsbekampfung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Amt für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung'.

**Content:**
```
\bAmt(?:s)?\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 132 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_12`)


Diesen Antrag vom 25.11.2024 hat das Amt für Betrugsbekämpfung mit Bescheid vom 02.  Dezember 2024 abgewiesen.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — missing annotation

> partial: 0  |  likely missing annotation: 0  |  spurious: 1

**Gold Entities:**

</details>

---

## `company_f_personalservice`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'F Personalservice GmbH' and similar patterns where a single letter prefix is part of the company name.

**Content:**
```
\bF\s+Personalservice\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_f_personal_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'F Personal GmbH' pattern.

**Content:**
```
\bF\s+Personal\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_landespolizeidirektion_typo`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific typo 'Landespolizeidirketion Tirol' found in the data.

**Content:**
```
\bLandespolizeidirketion\s+Tirol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_henken`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule for 'Henken' which appears as an organization in the training data.

**Content:**
```
\bHenken\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_retail_chains`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific retail chains found in the training data: Ikea, Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz, Quelle.at.

**Content:**
```
\b(Ikea|Obi|Leiner|M\u00f6belix|M\u00f6maX|Otto\.de|xxxLutz|Quelle\.at)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_mur_alver_og`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Mur Alver OG' which was missed by generic rules.

**Content:**
```
\bMur\s+Alver\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_pva`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'PVA' (Pensionsversicherungsanstalt).

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

## `org_svs_svb`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'SVS/SVB' (Sozialversicherung der Bauern).

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

## `org_sozialversicherung_bauern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherung der Bauern' and 'Sozialversicherungsanstalt der Bauern'.

**Content:**
```
\bSozialversicherung(?:sanstalt)?\s+der\s+Bauern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bundesamt_soziales`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen' and its variant 'Sozialministeriumservice'.

**Content:**
```
\bBundesamt\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen(?:\s+Sozialministeriumservice)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_psd_wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'PSD Wien Ambulatorium Landstraße'.

**Content:**
```
\bPSD\s+Wien\s+Ambulatorium\s+Landstra\u00dfe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_immobilienbuero`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Immobilienbüro' followed by a name.

**Content:**
```
\bImmobilienb\u00fcro\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_oesterreichische_gesundheitskasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Österreichischen Gesundheitskasse' (genitive) and 'Österreichische Gesundheitskasse' (nominative).

**Content:**
```
\b(\u00d6sterreichische|\u00d6sterreichischen)\s+Gesundheitskasse\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_law_firm_complex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches complex law firm names with multiple surnames and 'Rechtsanwälte GmbH'.

**Content:**
```
\b[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:,\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\s+Rechtsanw\u00e4lte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_hyphenated_acronym_gmbh`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches hyphenated names followed by an acronym and GMBH (e.g., Klein-Vorholt KI GMBH).

**Content:**
```
\b[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+-[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+[A-Z]{2,}\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bundesministeriums_fuer_inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministeriums für Inneres' (genitive case).

**Content:**
```
\bBundesministeriums\s+f\u00fcr\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bundesministeriums_fuer_finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministers für Finanzen' (genitive case).

**Content:**
```
\bBundesministers\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `tax_authority_finanzamt_oststeiermark`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamtes Oststeiermark' (genitive case) specifically.

**Content:**
```
\bFinanzamtes\s+Oststeiermark\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bundesministerin_finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerin für Finanzen' (Federal Minister of Finance).

**Content:**
```
\bBundesministerin\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_erste_bank`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Erste Bank' specifically as seen in training data.

**Content:**
```
\bErste\s+Bank\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_wko`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'WKO' (Wirtschaftskammer Österreich).

**Content:**
```
\bWKO\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_bezirkshauptmannschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bezirkshauptmannschaft' followed by a location name.

**Content:**
```
\bBezirkshauptmannschaft\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `company_senecura`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'SeneCura', 'Senecura', 'SENECURA' and their multi-word variations with 'Laurentius', 'Park', 'Bludenz' with flexible spacing/hyphens.

**Content:**
```
\b(SeneCura|Senecura|SENECURA)(?:\s+(?:Laurentius(?:\s+)?(?:Park(?:\s+)?Bludenz|Bludenz|Park))|\s+Laurentius(?:\s+)?(?:Park(?:\s+)?Bludenz|Bludenz|Park))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `org_obb`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Austrian Federal Railways acronym 'ÖBB'.

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

## `org_krankenpflegevereins_bludenz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Krankenpflegevereins Bludenz' specifically.

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

</details>

---

