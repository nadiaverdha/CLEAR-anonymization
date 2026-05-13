# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (manual_findok)

Generated on: 2026-05-14T00:19:36.281348

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-13/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2549 |
| Validation documents | 639 |
| Test documents | 1247 |
| Train sentences | 4268 |
| Validation sentences | 968 |
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
| Seed Rule Count | 110 |
| New Rules Added | 9 |
| Continuation | synthesize_and_refine |
| Phase1 Train Sentences | 4080 |
| Phase1 Eval Sentences | 927 |
| Transfer Train Sentences | 188 |
| Transfer Eval Sentences | 41 |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 81.9% |
| True Positives | 26 |
| False Positives | 279 |
| False Negatives | 64 |
| Total Gold Entities | 90 |
| Micro Precision | 8.5% |
| Micro Recall | 28.9% |
| Micro F1 | 13.2% |
| Macro F1 | 13.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `title_priv_doz_in` | 4.3% | 100.0% | 2.2% | 2 | 2 | 0 |
| `name_after_herr` | 4.3% | 100.0% | 2.2% | 2 | 2 | 0 |
| `title_mag` | 6.5% | 100.0% | 3.3% | 3 | 3 | 0 |
| `name_in_parentheses` | 8.5% | 100.0% | 4.4% | 4 | 4 | 0 |
| `name_in_beschwerdesache_tightened` | 18.2% | 100.0% | 10.0% | 9 | 9 | 0 |
| `hr_in_beschwerdesache` | 18.2% | 100.0% | 10.0% | 9 | 9 | 0 |
| `title_mag_tightened` | 6.5% | 100.0% | 3.3% | 3 | 3 | 0 |
| `title_hon_prof` | 2.2% | 50.0% | 1.1% | 2 | 1 | 1 |
| `name_after_genitive_des` | 2.2% | 50.0% | 1.1% | 2 | 1 | 1 |
| `title_dr_in_hon_prof` | 2.2% | 50.0% | 1.1% | 2 | 1 | 1 |
| `herr_frau_person` | 8.0% | 40.0% | 4.4% | 10 | 4 | 6 |
| `name_after_fuer` | 2.2% | 33.3% | 1.1% | 3 | 1 | 2 |
| `name_after_von` | 2.2% | 33.3% | 1.1% | 3 | 1 | 2 |
| `name_in_parenthetical` | 2.1% | 25.0% | 1.1% | 4 | 1 | 3 |
| `name_in_parenthetical_tightened` | 2.1% | 25.0% | 1.1% | 4 | 1 | 3 |
| `name_after_preposition_tightened` | 2.1% | 20.0% | 1.1% | 5 | 1 | 4 |
| `name_after_preposition` | 1.8% | 4.3% | 1.1% | 23 | 1 | 22 |
| `name_at_end_of_sentence` | 1.4% | 1.0% | 2.2% | 195 | 2 | 193 |
| `von_frau_person` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `title_okr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_hon_prof_dr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_hr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_univ_prof` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_dr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_vetr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_ost_r` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `title_dr_in_priv_doz_in` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_nachname_wie_bf` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_fuer_die_kinder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_an_die` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `known_person_names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `german_person_with_title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_gegen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_herrn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_in_verwaltungsstrafsache` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_in_verwaltungsstrafsache_general` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_osr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_omedr_str` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_repeated` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_univ_prof_in` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_univ_prof_complex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_hr_kzlr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_univ_prof_in_priv_doz_in` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_at_signature` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_complex_academic` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_in_genitive_with_address` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_dr_in` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_prof_in` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_hon_prof_complex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `medr_title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_prof_in_medr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_with_complex_prefix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_in_beschwerdesache_of` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_richter_in` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_kommr_repeated` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_priv_doz_univ_prof` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_role_parenthetical` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_comma_role` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_stR_fixed` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_verb_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_combined_mag_hon` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_kzlr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_hon_prof_male` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_priv_doz_male` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_hon_prof_in_complex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_priv_doz_dr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_gegenüber_herrn` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_in_followup_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_omedr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_wurde_passive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_kommr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_in_list_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_at_start_of_sentence_tightened` | 0.0% | 0.0% | 0.0% | 97 | 0 | 97 |
| `title_kommir_ing` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_herr_frau` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `title_rgr_phd` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_mag_chain` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_rgR_univ_prof_in_kommR` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_mag_a` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_ist` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `name_after_colon` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `title_herr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_omdr_techn_r` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_ing_dr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_dipl_kfm` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_prof_phd` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_richter` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_komr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_ostR` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `title_ing` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_hon_prof_in` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_mag_complex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_priv_doz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_stR_complex` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `title_prof` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `judge_name_context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_hr_full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_des_genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_rgr_dipl_kff` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_mutter` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_after_des_beschwerdesache` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_in_list` | 0.0% | 0.0% | 0.0% | 41 | 0 | 41 |
| `name_after_als` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_osr_ddr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_bakk_art` | 0.0% | 0.0% | 0.0% | 14 | 0 | 14 |
| `name_after_genitive_der` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `name_after_nominative_die_der` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_rgr_omedr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_with_suffix_general` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_dipl_ing` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_dr_in_univ_prof` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_phd` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_ddr_complex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `name_at_start_of_sentence_tightened_v2` | 0.0% | 0.0% | 0.0% | 97 | 0 | 97 |
| `name_after_fuer_das_kind` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `title_phd_ing` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_prof_dr` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_ing_with_suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `title_prof_dr_in` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `name_in_beschwerdesache_tightened`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Description:**
Captures the person name in 'in der Beschwerdesache' or 'in der Beschwerdesache des', including suffixes like BA, LLB.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+(?:des\s+)?)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+straße|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.100 | 0.182 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 9 | 0 | 81 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Willibald Endrowait` | `Willibald Endrowait` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Frauke Stuhldreher` | `Frauke Stuhldreher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Patricia Jentz` | `Patricia Jentz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Mathilda Eckholdt` | `Mathilda Eckholdt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Renate Brombusch` | `Renate Brombusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Juliana Bartjen` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

</details>

---

## `hr_in_beschwerdesache`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Description:**
Captures 'HR [Name]' specifically in the context of 'Beschwerdesache', excluding the word 'Beschwerdesache' from the match.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+)(?:HR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.100 | 0.182 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 9 | 0 | 81 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Willibald Endrowait` | `Willibald Endrowait` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Frauke Stuhldreher` | `Frauke Stuhldreher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Patricia Jentz` | `Patricia Jentz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Mathilda Eckholdt` | `Mathilda Eckholdt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Renate Brombusch` | `Renate Brombusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Juliana Bartjen` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `name_at_end_of_sentence`

**F1:** 0.014 | **Precision:** 0.010 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures names at the end of a sentence or before specific punctuation when no title is present.

**Content:**
```
(?:\n|\s|^)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s*\n|\s*\.|\s*,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.010 | 0.022 | 0.014 | 195 | 2 | 193 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 193 | 88 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Wilhelm Konetzny` | `Wilhelm Konetzny` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gabriele Friedbacher` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Priv` — positional overlap with gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`
- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`
- `Kind Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Zeitraum  November` — no gold match — likely missing annotation

> overlaps gold: 3  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Krankenpflege Grillenreith` — partial — pred is substring of gold: `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Im Zeitraum` — no gold match — likely missing annotation
- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

</details>

---

## `name_at_start_of_sentence_tightened`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names at start of sentence, excluding common non-name words, organizations, and month names. FIXED: Added 'Punkt' to exclusion list.

**Content:**
```
(?:^|\.)\s*((?!Die\s+|Verfahrensgang|Entscheidungsgr\u00fcnde|Begr\u00fcndung|Beschluss|Hinweis|Feststellung|Erw\u00e4gung|Anmerkung|Antrag|Antragsteller|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|GmbH|AG|KG|PartG|Rechtsanw\u00e4lte|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|Punkt)[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 97 | 0 | 97 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 97 | 87 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_4`)


Am 30.09.2019 langte beim Finanzamt die Antwort der Beschwerdeführerin (in der Folge BF)  auf ein Überprüfungsschreiben des Anspruches auf Familienbeihilfe ein.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_11`)


Seit 2.7.2018 absolviert sie  eine Lehre zur Steuerassistentin.

**False Positives:**

- `Seit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Im Zeitraum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_14`)


Ab November  2017 war sie aufgrund ihrer schweren Krankheit nicht arbeitsfähig.“

**False Positives:**

- `Ab November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_27`)


7. Am 12.10.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor und beantragte die Abweisung, da die Ausbildung am 04.10.2017 beendet  worden sei.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

</details>

---

## `name_at_start_of_sentence_tightened_v2`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names at start of sentence, excluding common non-name words, organizations, and month names. Strictly enforces word boundaries.

**Content:**
```
(?:^|\.)\s*((?!Die\s+|Verfahrensgang|Entscheidungsgr\u00fcnde|Begr\u00fcndung|Beschluss|Hinweis|Feststellung|Erw\u00e4gung|Anmerkung|Antrag|Antragsteller|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|GmbH|AG|KG|PartG|Rechtsanw\u00e4lte|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung)[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 97 | 0 | 97 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 97 | 87 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_4`)


Am 30.09.2019 langte beim Finanzamt die Antwort der Beschwerdeführerin (in der Folge BF)  auf ein Überprüfungsschreiben des Anspruches auf Familienbeihilfe ein.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_11`)


Seit 2.7.2018 absolviert sie  eine Lehre zur Steuerassistentin.

**False Positives:**

- `Seit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Im Zeitraum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_14`)


Ab November  2017 war sie aufgrund ihrer schweren Krankheit nicht arbeitsfähig.“

**False Positives:**

- `Ab November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_27`)


7. Am 12.10.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor und beantragte die Abweisung, da die Ausbildung am 04.10.2017 beendet  worden sei.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

</details>

---

## `name_in_list`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names in a list format, e.g., '1. Name, born...', ensuring the number is not part of the name and including suffixes.

**Content:**
```
(?:^|\n|\d+\.\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+straße|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 41 | 0 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 41 | 86 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Im Zeitraum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_14`)


Ab November  2017 war sie aufgrund ihrer schweren Krankheit nicht arbeitsfähig.“

**False Positives:**

- `Ab November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_35`)


Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abweisung)

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_10`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname wie Bf.) sind mit der Kindesmutter und  1 von 7 Seite 2 von 7

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_13`)


Ende Mai 2019 wurde meine noch minderjährige [Anmerkung: 17 ½ -jährige] Tochter aus der  Wohnung der Familie des Ziehvaters in Worcester weggewiesen.

**False Positives:**

- `Ende Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Worcester`(city)

</details>

---

## `name_after_preposition`

**F1:** 0.018 | **Precision:** 0.043 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures names following prepositions like 'von', 'aus', 'bei', 'in' in contexts where titles are absent.

**Content:**
```
(?:von\s+(?:der\s+|dem\s+|die\s+)?|aus\s+(?:der\s+|dem\s+|die\s+)?|bei\s+(?:der\s+|dem\s+|die\s+)?|in\s+(?:der\s+|dem\s+|die\s+)?)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s\n]|\s+(?:GmbH|AG|KG|OHG|UG|PartG|Rechtsanw\u00e4lte|Steuerberatung|Beratung|Consulting|GmbH\s*&\s*Co\.|\s+\d|Wirtschaftspr\u00fcfungs-|Steuerberatungsgesellschaft|mbH|\.\s*Co\.|Beschwerdesache|Finanzamt|Bundesfinanzgericht|Gericht|Beh\u00f6rde|Steuerberatungs|Talder|Stadt|Finanzamtes|Wien|Innsbruck|Tirol|Ober\u00f6sterreich|Nieder\u00f6sterreich|Salzburg|Steiermark|K\u00e4rnten|Vorarlland|Burgenland|Finanzamtes|Braunau|Ried|Sch\u00e4rding|Gmunden|V\u00f6cklabruck|Freistadt|Rohrbach|Urfahr|Wien|3/6/7/11/15|Schwechat|Gerasdorf|Tirol|Ost|Landeck|Reutte|Klagenfurt|St\.\s*Veit|Wolfsberg|Kirchdorf|Perg|Steyr|Salzburg-Land|\u00d6sterreich|Gro\u00dfbetriebe|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.043 | 0.011 | 0.018 | 23 | 1 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 22 | 89 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_68`)


Da das Studium von Viktoria Immohr  nach 4 Semester gewechselt wurde  und 1 Semester angerechnet werden konnte, beträgt die Wartezeit 3 Semester.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache  Frauke Stuhldreher` — partial — gold is substring of pred: `Frauke Stuhldreher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `England Advanced Level` — partial — gold is substring of pred: `England`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_20`)


Gemäß obigen Ausführungen ist meine Tochter Maximiliane Sakschewsky, MA  seit Sommer 2014,  ausgenommen ferienbedingte Abwesenheiten, in Vereinigten Königreich wohnhaft.

**False Positives:**

- `Vereinigten Königreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

</details>

---

## `title_bakk_art`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with academic degree 'Bakk. art.' or 'Bakk. techn.' or 'Bakk. iur.' following a name, ensuring the full name and suffix are captured.

**Content:**
```
(?:^|\s|,|\.)\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)\s*,\s*Bakk\.\s*(?:iur|art|techn)\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 14 | 0 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 14 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Kind Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_15`)


Der Beschwerde beigelegt war eine Betätigung eines Allgemeinmediziners vom 27.11.2019,  wonach Stella Marschalk, Bakk. techn.  auf Grund einer schweren Erkrankung (Sensibilitätsdefizit untere  Extremitäten DD: Guillain-Barré-Syndrom) von Oktober 2017 bis Ende Juni 2018 nicht  arbeitsfähig gewesen sei.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `name_after_ist`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'ist' (is), excluding corporate suffixes and honorifics like 'Herr' or 'Frau'.

**Content:**
```
(?:Die\s+|Der\s+|Die\s+|Das\s+)?(?<!Herr\s)(?<!Frau\s)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)\s+ist\s+(?!\s+(?:GmbH|AG|KG|OHG|UG|PartG|Rechtsanwälte|Steuerberatung|Beratung|Consulting|GmbH\s*&\s*Co\.|\s+\d|Wirtschaftsprüfungs-|Steuerberatungsgesellschaft|mbH|\.\s*Co\.|Finanzamt|Bundesfinanzgericht|Gericht|Behörde|Sachverhalt|Die\s+Beschwerdeführerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Beschwerdeführerin|Die\s+Beschwerde|Die\s+Parteien|Bundesfinanzgericht|Finanzamt|Stadt|Gericht|Behörde|Sachverhalt|Die\s+Beschwerdeführerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Beschwerdeführerin|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt\s+|Limited))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 12 | 30 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_22`)


Im Rückforderungsbetrag ist die  anteilige Geschwisterstaffel für sämtliche Kinder enthalten, für die Sie im  Rückforderungszeitraum zu Unrecht Familienbeihilfe erhalten haben (§ 8 Abs. 3  Familienlastenausgleichsgesetz 1967).“  4. Dagegen erhob die Bf. rechtzeitig die Beschwerde vom 07.10.2021 und brachte vor, dass  hierbei nur ein Wechsel des Studienortes bei gleichbleibender Studienrichtung vorliege.

**False Positives:**

- `Im Rückforderungsbetrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_23`)


Unser Mandant ist hauptberuflich Musiker (Vibraphon, Schlagwerk), seine Tätigkeiten übt er  sowohl in Form von Dienstverhältnissen (z.B. Orchester) als auch als selbständiger Musiker  (Einzelunternehmer oder Gesellschafter diverser Musikensembles) aus.

**False Positives:**

- `Unser Mandant` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_113`)


Unter Gesamtgewinn ist der Gesamtbetrag der Gewinne zuzüglich steuerfreier  Einnahmen abzüglich des Gesamtbetrags der Verluste zu verstehen.

**False Positives:**

- `Unter Gesamtgewinn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_116`)


(2) Unter Gesamtüberschuß ist der Gesamtbetrag der Überschüsse der Einnahmen über die  Werbungskosten abzüglich des Gesamtbetrags der Verluste zu verstehen.

**False Positives:**

- `Unter Gesamtüberschuß` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_41`)


Der Zinsenbescheid ist an die im Spruch des zur  Nachforderung oder Gutschrift führenden Bescheides ausgewiesene Nachforderung bzw.  Gutschrift gebunden.

**False Positives:**

- `Der Zinsenbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `name_after_genitive_der`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'der' in genitive contexts, excluding organizations and common false positives.

**Content:**
```
der\s+(?!Beschwerdesache|Rechtssache|Verfahren|Sache|Antrag|Bescheid|Urteil|Entscheidung|Klage|Rechtsmittel|Einspruch|Widerspruch|Anzeige|Strafanzeige|Verfahrenshilfe|Verfahrenshilfekosten|Verfahrenskostenhilfe|Verfahrenskosten|Verfahrensgegenstand|Verfahrensbeteiligte|Verfahrensbeteiligter|Verfahrensbeistand|Verfahrensbeist\u00e4ndin|Finanzamt|Finanzamtes|Stadt|Magistrat|Magistratsabteilung|Beh\u00f6rde|Bundesfinanzgericht|Gericht|Wirtschaftspr\u00fcfung|Steuerberatung|GmbH|AG|KG|PartG|Rechtsanw\u00e4lte|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|Wien|Nr|Gl\u00fccksspielabgabe|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|Rechtsanw\u00e4lte|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 8 | 58 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_61`)


Am 23. Oktober 2020 überwies der Bf. auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN  GB…1084 € 200,00 mit dem Verwendungszweck: Unterstützung, am 4. November 2020  € 500,00 am 25. und 30. November jeweils € 200,00.

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (JKU Linz)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Johannes Kepler Universität Linz (JKU Linz)`(organisation)
- `JKU Linz`(organisation)
- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_26`)


6. Die Bf. antwortete mit einer am 13.12.2021 bei der belangten Behörde eingelangter Eingabe  und legte ein E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  3 von 16 Seite 4 von 16

**False Positives:**

- `Johannes Kepler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)
- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz (`(organisation)

</details>

---

## `herr_frau_person`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures persons identified by 'Herr', 'Herrn', or 'Frau' followed by a full name including suffixes like LLM, MSc. Excludes the title from the match.

**Content:**
```
(?:Herr|Herrn|Frau)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+(?:\s*,\s*[A-Z]{2,4})?)(?=[,\s\n]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.400 | 0.044 | 0.080 | 10 | 4 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 6 | 79 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_53`)


Zwischen dem Bf. und Frau Delia Moebes  besteht unstrittig eine aufrechte eheliche  Gemeinschaft (vgl. Protokoll zur Verhandlung vom 1. Oktober 2025).

| Predicted | Gold |
|---|---|
| `Delia Moebes` | `Delia Moebes` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_93`)


Nach den unstrittigen Sachverhaltsfeststellungen besteht zwischen dem Bf. und Frau  Delia Moebes  eine aufrechte eheliche Gemeinschaft, wobei den Bf. gegenüber seiner Ehefrau  keine Unterhaltspflicht trifft.

| Predicted | Gold |
|---|---|
| `Delia Moebes` | `Delia Moebes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_33`)


Im vorliegenden Fall wäre  hinsichtlich der Ermessensausübung insbesondere die wirtschaftliche Leistungsfähigkeit (vgl  Ritz, BAO5 § 9 Rz 28 mwN) vom Bf. bei der Haftungsinanspruchnahme zu beachten: Herr  Dieter Leufkes  verfüge zum gegenwärtigen Zeitpunkt über kein Vermögen.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_34`)


Seit 1.11.2015 sei Herr  Dieter Leufkes  wieder angestellt und beziehe ein Nettogehalt von ca. 1.400 €/Monat Von diesem  Einkommen könne ein Betrag von ca. 356 €/Monat gepfändet werden, jedoch sei dieser Betrag  bereits in Pfändung.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `title_okr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'ÖkR' followed by full name, including preceding titles like 'Dr.in'.

**Content:**
```
(?:Dr\.in\s+)?ÖkR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_hon_prof_dr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Hon.-Prof. Dr.' followed by name.

**Content:**
```
Hon\.-Prof\.\s+Dr\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_hr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'HR' or 'Techn R HR' followed by full name, including suffixes, excluding trailing commas.

**Content:**
```
(?:Techn\s+R\s+)?HR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.\s*iur\.|MBA|MSc|LLM|Dr\.\s*|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+\w+straße|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_univ_prof`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Univ.-Prof.' (including repeated titles) followed by name.

**Content:**
```
(?:Univ\.-Prof\.\s+)+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_dr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Dr.' followed by full name, ensuring umlauts are included and matching stops at punctuation, including 'von'.

**Content:**
```
Dr\.(?:\s+)?([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.\s*(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+\w+straße|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_vetr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'KommR VetR' or 'VetR' followed by full name.

**Content:**
```
(?:KommR\s+)?VetR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_dr_in_priv_doz_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with compound title 'Dr.in Priv.-Doz.in' followed by full name.

**Content:**
```
Dr\.in\s+Priv\.-Doz\.in\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_nachname_wie_bf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names immediately following the specific legal marker '(Nachname wie Bf.)'.

**Content:**
```
\(Nachname wie Bf\.\)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_fuer_die_kinder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures bare names following 'für die Kinder' (for the children), common in family benefit cases.

**Content:**
```
für\s+die\s+Kinder\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `known_person_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known person entities from the training data to ensure high recall for these specific cases.

**Content:**
```
(?:Larissa Gmelich|Benjamin Dittke|Dr\.in Olga Arai|Veronika Zeitlhuber|Dr\. Dr\. Erich Papadakis|Kirstin Hänßen|Lucia Norkeit|Olivia Püttmanns|Meinrad Kühnken)
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

## `name_in_beschwerdesache_tightened`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Description:**
Captures the person name in 'in der Beschwerdesache' or 'in der Beschwerdesache des', including suffixes like BA, LLB.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+(?:des\s+)?)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+straße|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.100 | 0.182 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 9 | 0 | 81 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Willibald Endrowait` | `Willibald Endrowait` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Frauke Stuhldreher` | `Frauke Stuhldreher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Patricia Jentz` | `Patricia Jentz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Mathilda Eckholdt` | `Mathilda Eckholdt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Renate Brombusch` | `Renate Brombusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Juliana Bartjen` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Alma Springel` | `Alma Springel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Österreich` (organisation)
- `75-059/0556` (tax_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Oleg Dell` | `Oleg Dell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Katrin Allram` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `80-738/9953` (tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `36-532/2242` (tax_number)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Ludger Weynand` | `Ludger Weynand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)
- `Finanzamtes Österreich` (organisation)

</details>

---

## `hr_in_beschwerdesache`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Description:**
Captures 'HR [Name]' specifically in the context of 'Beschwerdesache', excluding the word 'Beschwerdesache' from the match.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+)(?:HR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.100 | 0.182 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 9 | 0 | 81 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Willibald Endrowait` | `Willibald Endrowait` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Frauke Stuhldreher` | `Frauke Stuhldreher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Patricia Jentz` | `Patricia Jentz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Mathilda Eckholdt` | `Mathilda Eckholdt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Renate Brombusch` | `Renate Brombusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Juliana Bartjen` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Alma Springel` | `Alma Springel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Österreich` (organisation)
- `75-059/0556` (tax_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Oleg Dell` | `Oleg Dell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Katrin Allram` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `80-738/9953` (tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `36-532/2242` (tax_number)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Ludger Weynand` | `Ludger Weynand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)
- `Finanzamtes Österreich` (organisation)

</details>

---

## `name_in_parentheses`

**F1:** 0.085 | **Precision:** 1.000 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures names appearing in parentheses, often with a role description (e.g., 'als Bf bezeichnet').

**Content:**
```
\(([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*\)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.044 | 0.085 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 0 | 35 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `5966 230804` (social_security_number)
- `4740150943` (social_security_number)
- `RgR HR Reneé Schrammek` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_7`)


Die  Auszahlung der Familienbeihilfe war bereits mit 01/2021 eingestellt worden, da laut  Studiendatenübermittlungsauskunft das Studium der Tochter der Bf. (Viktoria Immohr) nur bis  14.12.2020 betrieben wurde und die Tochter mit 01.01.2021 eine Teilzeitbeschäftigung  begonnen hatte.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `5966 230804` (social_security_number)
- `4740150943` (social_security_number)
- `RgR HR Reneé Schrammek` (person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

</details>

---

## `herr_frau_person`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures persons identified by 'Herr', 'Herrn', or 'Frau' followed by a full name including suffixes like LLM, MSc. Excludes the title from the match.

**Content:**
```
(?:Herr|Herrn|Frau)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+(?:\s*,\s*[A-Z]{2,4})?)(?=[,\s\n]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.400 | 0.044 | 0.080 | 10 | 4 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 6 | 79 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_53`)


Zwischen dem Bf. und Frau Delia Moebes  besteht unstrittig eine aufrechte eheliche  Gemeinschaft (vgl. Protokoll zur Verhandlung vom 1. Oktober 2025).

| Predicted | Gold |
|---|---|
| `Delia Moebes` | `Delia Moebes` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_93`)


Nach den unstrittigen Sachverhaltsfeststellungen besteht zwischen dem Bf. und Frau  Delia Moebes  eine aufrechte eheliche Gemeinschaft, wobei den Bf. gegenüber seiner Ehefrau  keine Unterhaltspflicht trifft.

| Predicted | Gold |
|---|---|
| `Delia Moebes` | `Delia Moebes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_33`)


Im vorliegenden Fall wäre  hinsichtlich der Ermessensausübung insbesondere die wirtschaftliche Leistungsfähigkeit (vgl  Ritz, BAO5 § 9 Rz 28 mwN) vom Bf. bei der Haftungsinanspruchnahme zu beachten: Herr  Dieter Leufkes  verfüge zum gegenwärtigen Zeitpunkt über kein Vermögen.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_34`)


Seit 1.11.2015 sei Herr  Dieter Leufkes  wieder angestellt und beziehe ein Nettogehalt von ca. 1.400 €/Monat Von diesem  Einkommen könne ein Betrag von ca. 356 €/Monat gepfändet werden, jedoch sei dieser Betrag  bereits in Pfändung.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `title_mag`

**F1:** 0.065 | **Precision:** 1.000 | **Recall:** 0.033  

**Format:** `regex`  
**Description:**
Captures persons with title 'Mag.' or 'Mag.a' followed by name, including suffixes like ', Bakk. rer. nat.' or 'LL.M.'

**Content:**
```
Mag\.(?:in)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:Bakk\.(?:rer\.\s*nat\.|iur|art|techn)|LL\.M\.|LLB|BEd|MBA|MSc|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.|Mag\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.033 | 0.065 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 0 | 38 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Mag. Ashley Partenfelder` | `Mag. Ashley Partenfelder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gabriele Friedbacher` | `Mag. Gabriele Friedbacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wilhelm Konetzny` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ludger Weynand` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)
- `Finanzamtes Österreich` (organisation)

</details>

---

## `title_mag_tightened`

**F1:** 0.065 | **Precision:** 1.000 | **Recall:** 0.033  

**Format:** `regex`  
**Description:**
Captures 'Mag.' or 'Mag.a' followed by name, excluding organization names (GmbH, AG, etc.).

**Content:**
```
Mag\.(?:in)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?!\s+(?:GmbH|AG|KG|PartG|OG|Wirtschafts|Steuer|Beratung|Treuhand|Rechtsanwalts|Sozial|Finanz|Bundes|Stadt|Magistrat|Gesellschaft|Dienstleistung|Unternehmen|Service|Institute|Firma|Büro|Consulting|Group|Holdings|Corporation|Ltd|Inc|SRL|SpA|SA|NV|AB|A/S|Oy|Ltd\.))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.033 | 0.065 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 0 | 38 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Mag. Ashley Partenfelder` | `Mag. Ashley Partenfelder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Gabriele Friedbacher` | `Mag. Gabriele Friedbacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wilhelm Konetzny` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ludger Weynand` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)
- `Finanzamtes Österreich` (organisation)

</details>

---

## `title_priv_doz_in`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures persons with title 'Priv.-Doz.in' followed by name. FIXED: Now captures full match including title.

**Content:**
```
Priv\.-Doz\.in\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.022 | 0.043 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 0 | 22 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Farina Kohlstrunk` | `Priv.-Doz.in Farina Kohlstrunk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Juliana Bartjen` | `Priv.-Doz.in Juliana Bartjen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Renate Brombusch` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

</details>

---

## `name_after_herr`

**F1:** 0.043 | **Precision:** 1.000 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures names following 'Herr' (Mr.) in legal contexts.

**Content:**
```
\bHerr\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=\s*[,\-\s]|\s*$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.022 | 0.043 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 0 | 2 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_33`)


Im vorliegenden Fall wäre  hinsichtlich der Ermessensausübung insbesondere die wirtschaftliche Leistungsfähigkeit (vgl  Ritz, BAO5 § 9 Rz 28 mwN) vom Bf. bei der Haftungsinanspruchnahme zu beachten: Herr  Dieter Leufkes  verfüge zum gegenwärtigen Zeitpunkt über kein Vermögen.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_34`)


Seit 1.11.2015 sei Herr  Dieter Leufkes  wieder angestellt und beziehe ein Nettogehalt von ca. 1.400 €/Monat Von diesem  Einkommen könne ein Betrag von ca. 356 €/Monat gepfändet werden, jedoch sei dieser Betrag  bereits in Pfändung.

| Predicted | Gold |
|---|---|
| `Dieter Leufkes` | `Dieter Leufkes` |

</details>

---

## `title_hon_prof`

**F1:** 0.022 | **Precision:** 0.500 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures persons with compound title 'Dr. Hon.-Prof.' or 'Hon.-Prof.' followed by name.

**Content:**
```
(?:Dr\.\s+)?Hon\.-Prof\.(?:\s+Ing\.)?\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.011 | 0.022 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 1 | 89 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thassilo Averdiek` | `Hon.-Prof. Thassilo Averdiek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Österreich` (organisation)
- `75-059/0556` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Gotthard Clement` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `name_after_genitive_des`

**F1:** 0.022 | **Precision:** 0.500 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures names following 'des' in genitive contexts, excluding organizations and common false positives.

**Content:**
```
des\s+(?!Beschwerdesache|Rechtssache|Verfahren|Sache|Antrag|Bescheid|Urteil|Entscheidung|Klage|Rechtsmittel|Einspruch|Widerspruch|Anzeige|Strafanzeige|Verfahrenshilfe|Verfahrenshilfekosten|Verfahrenskostenhilfe|Verfahrenskosten|Verfahrensgegenstand|Verfahrensbeteiligte|Verfahrensbeteiligter|Verfahrensbeistand|Verfahrensbeist\u00e4ndin|Finanzamt|Finanzamtes|Stadt|Magistrat|Magistratsabteilung|Beh\u00f6rde|Bundesfinanzgericht|Gericht|Wirtschaftspr\u00fcfung|Steuerberatung|GmbH|AG|KG|PartG|Rechtsanw\u00e4lte|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|Wien|Nr|Gl\u00fccksspielabgabe|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|Rechtsanw\u00e4lte|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.011 | 0.022 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 1 | 20 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Wilhelm Konetzny` | `Wilhelm Konetzny` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gabriele Friedbacher` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Jennifer Papenhagen` — partial — pred is substring of gold: `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

</details>

---

## `title_dr_in_hon_prof`

**F1:** 0.022 | **Precision:** 0.500 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures persons with combined titles 'Dr.in Hon.-Prof.in' or 'Dr.in Hon.-Prof.' followed by name.

**Content:**
```
(?:Dr\.in\s+)?(?:Hon\.-Prof\.(?:in)?\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.011 | 0.022 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 1 | 89 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thassilo Averdiek` | `Hon.-Prof. Thassilo Averdiek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Österreich` (organisation)
- `75-059/0556` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Gotthard Clement` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `name_after_fuer`

**F1:** 0.022 | **Precision:** 0.333 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names following the preposition 'für' (for).

**Content:**
```
für\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=,|\s+\d|\s+\n|\s+(?:Straß|Gasse|Weg|Platz|Allee|Ring|Boulevard|Nr\.|Hausnummer)|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.011 | 0.022 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 2 | 80 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_86`)


Der Bf. erfüllte die alternativ zu beurteilende Voraussetzung, die Unterhaltskosten für  Maximiliane Sakschewsky, MA  überwiegend zu tragen, wie oben unter Punkt 2. ausgeführt, nicht.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

</details>

---

## `name_after_von`

**F1:** 0.022 | **Precision:** 0.333 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names following 'von' (from) or 'von der/dem' (from the), excluding organizations and month names. FIXED: Ensures full name capture.

**Content:**
```
(?:von\s+(?:der\s+|dem\s+|die\s+)?)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s\n]|\s+(?:GmbH|AG|KG|OHG|UG|PartG|Rechtsanw\u00e4lte|Steuerberatung|Beratung|Consulting|GmbH\s*&\s*Co\.|\s+\d|Wirtschaftspr\u00fcfungs-|Steuerberatungsgesellschaft|mbH|\.\s*Co\.|Beschwerdesache|Finanzamt|Bundesfinanzgericht|Gericht|Beh\u00f6rde|Steuerberatungs|Talder|Stadt|Finanzamtes|Wien|Innsbruck|Tirol|Ober\u00f6sterreich|Nieder\u00f6sterreich|Salzburg|Steiermark|K\u00e4rnten|Vorarlland|Burgenland|Finanzamtes|Braunau|Ried|Sch\u00e4rding|Gmunden|V\u00f6cklabruck|Freistadt|Rohrbach|Urfahr|Wien|3/6/7/11/15|Schwechat|Gerasdorf|Tirol|Ost|Landeck|Reutte|Klagenfurt|St\.\s*Veit|Wolfsberg|Kirchdorf|Perg|Steyr|Salzburg-Land|\u00d6sterreich|Gro\u00dfbetriebe|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.011 | 0.022 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 2 | 78 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_68`)


Da das Studium von Viktoria Immohr  nach 4 Semester gewechselt wurde  und 1 Semester angerechnet werden konnte, beträgt die Wartezeit 3 Semester.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

</details>

---

## `name_in_parenthetical`

**F1:** 0.021 | **Precision:** 0.250 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures names in parenthetical contexts like '(Bf.)' or '(Beschwerdeführerin)' following a name.

**Content:**
```
([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)\s*\(.*?(?:Bf\.|Beschwerdeführer|Beschwerdeführerin|Kläger|Klägerin|Antragsteller|Antragstellerin)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.011 | 0.021 | 4 | 1 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 3 | 34 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU)`(organisation)
- `Johannes Kepler Universität Linz (JKU)`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am Konservatorium  der Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz-Abteilung.

**False Positives:**

- `Verfahrensgang  Der Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Musikhochschule Wien`(organisation)
- `Konservatorium  der Stadt Wien`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) erzielte im Streitjahr 2022 Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Verfahrensgang  Der Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `name_in_parenthetical_tightened`

**F1:** 0.021 | **Precision:** 0.250 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures names in parenthetical contexts, ensuring only the name is extracted, not preceding nouns. Excludes court names and role-based phrases like 'Die Beschwerdeführerin'.

**Content:**
```
(?:Techn\s+R\s+|VetR\s+|StR\s+|HR\s+|Mag\.|Dr\.|Dr\.in\s+|Prof\.in\s+|Univ\.-Prof\.(?:in)?\s+|Hon\.-Prof\.(?:in)?\s+|KommR\s+|RgR\s+|Priv\.-Doz\.(?:in)?\s+|OStR\s+|MedR\s+|OMedR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)\s*\(.*?(?:Bf\.|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Kl\u00e4ger|Kl\u00e4gerin|Antragsteller|Antragstellerin)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.011 | 0.021 | 4 | 1 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 3 | 34 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU)`(organisation)
- `Johannes Kepler Universität Linz (JKU)`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am Konservatorium  der Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz-Abteilung.

**False Positives:**

- `Verfahrensgang  Der Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Musikhochschule Wien`(organisation)
- `Konservatorium  der Stadt Wien`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) erzielte im Streitjahr 2022 Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Verfahrensgang  Der Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `name_after_preposition_tightened`

**F1:** 0.021 | **Precision:** 0.200 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures names following prepositions like 'für', 'von', 'gegen' in contexts where a person is likely, including optional suffixes. Excludes 'von' if followed by 'Herrn'.

**Content:**
```
(?:f\u00fcr\s+|von\s+|gegen\s+)(?!Herrn\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+(?:Stra\u00dfe|Gasse|Weg|Platz|Allee|Ring|Boulevard|Nr\.|Hausnummer)|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.200 | 0.011 | 0.021 | 5 | 1 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 4 | 80 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_86`)


Der Bf. erfüllte die alternativ zu beurteilende Voraussetzung, die Unterhaltskosten für  Maximiliane Sakschewsky, MA  überwiegend zu tragen, wie oben unter Punkt 2. ausgeführt, nicht.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

</details>

---

## `name_after_preposition`

**F1:** 0.018 | **Precision:** 0.043 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures names following prepositions like 'von', 'aus', 'bei', 'in' in contexts where titles are absent.

**Content:**
```
(?:von\s+(?:der\s+|dem\s+|die\s+)?|aus\s+(?:der\s+|dem\s+|die\s+)?|bei\s+(?:der\s+|dem\s+|die\s+)?|in\s+(?:der\s+|dem\s+|die\s+)?)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s\n]|\s+(?:GmbH|AG|KG|OHG|UG|PartG|Rechtsanw\u00e4lte|Steuerberatung|Beratung|Consulting|GmbH\s*&\s*Co\.|\s+\d|Wirtschaftspr\u00fcfungs-|Steuerberatungsgesellschaft|mbH|\.\s*Co\.|Beschwerdesache|Finanzamt|Bundesfinanzgericht|Gericht|Beh\u00f6rde|Steuerberatungs|Talder|Stadt|Finanzamtes|Wien|Innsbruck|Tirol|Ober\u00f6sterreich|Nieder\u00f6sterreich|Salzburg|Steiermark|K\u00e4rnten|Vorarlland|Burgenland|Finanzamtes|Braunau|Ried|Sch\u00e4rding|Gmunden|V\u00f6cklabruck|Freistadt|Rohrbach|Urfahr|Wien|3/6/7/11/15|Schwechat|Gerasdorf|Tirol|Ost|Landeck|Reutte|Klagenfurt|St\.\s*Veit|Wolfsberg|Kirchdorf|Perg|Steyr|Salzburg-Land|\u00d6sterreich|Gro\u00dfbetriebe|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.043 | 0.011 | 0.018 | 23 | 1 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 22 | 89 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_68`)


Da das Studium von Viktoria Immohr  nach 4 Semester gewechselt wurde  und 1 Semester angerechnet werden konnte, beträgt die Wartezeit 3 Semester.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache  Frauke Stuhldreher` — partial — gold is substring of pred: `Frauke Stuhldreher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `England Advanced Level` — partial — gold is substring of pred: `England`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_20`)


Gemäß obigen Ausführungen ist meine Tochter Maximiliane Sakschewsky, MA  seit Sommer 2014,  ausgenommen ferienbedingte Abwesenheiten, in Vereinigten Königreich wohnhaft.

**False Positives:**

- `Vereinigten Königreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_56`)


In den Zeiträumen 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019  sowie 17. bis 19. Februar 2020 unternahm die Tochter des Bf. in Wien Fahrten gemäß § 19  Abs. 8 FSG (Fahrtenprotokoll).

**False Positives:**

- `Wien Fahrten` — partial — gold is substring of pred: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Beschwerdesache Patricia Jentz` — partial — gold is substring of pred: `Patricia Jentz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `Kind Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Farina Kohlstrunk` — partial — pred is substring of gold: `Priv.-Doz.in Farina Kohlstrunk`
- `Beschwerdesache Mathilda Eckholdt` — partial — gold is substring of pred: `Mathilda Eckholdt`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Farina Kohlstrunk`(person)
- `Mathilda Eckholdt`(person)
- `Kleingassen 3, 4150 Reith, Österreich`(address)
- `Mag. András Péter Radics`(person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See`(address)
- `Bundesfinanzgericht`(organisation)
- `Finanzamt Österreich`(organisation)
- `69-575/0475`(tax_number)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_36`)


Der eine Begünstigung in Anspruch Nehmende hat also selbst einwandfrei und  unter Ausschluss jeden Zweifels das Vorliegen all jener Umstände darzulegen, auf die die  abgabenrechtliche Begünstigung gestützt werden kann.

**False Positives:**

- `Anspruch Nehmende` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Juliana Bartjen` — partial — pred is substring of gold: `Priv.-Doz.in Juliana Bartjen`
- `Beschwerdesache Renate Brombusch` — partial — gold is substring of pred: `Renate Brombusch`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Estelle Niederholz` — partial — pred is substring of gold: `Dr.in Estelle Niederholz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_49`)


In diesem wurde darüber hinaus der Änderung der Einkommensteuer (Stammabgabe) in der  Beschwerdevorentscheidung Rechnung getragen.

**False Positives:**

- `Beschwerdevorentscheidung Rechnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Beschwerdesache Alma Springel` — partial — gold is substring of pred: `Alma Springel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thassilo Averdiek`(person)
- `Alma Springel`(person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `75-059/0556`(tax_number)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache  Oleg Dell` — partial — gold is substring of pred: `Oleg Dell`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Oleg Dell`(person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH`(organisation)
- `Hegelgasse 8, 1010 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `80-738/9953`(tax_number)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_111`)


Will ein Steuerpflichtiger Aufwendungen als außergewöhnliche Belastung berücksichtigt  wissen, hat er selbst alle Umstände darzulegen, auf welche die abgabenrechtliche  Begünstigung gestützt werden kann (vgl. VwGH 22.12.2004, 2001/15/0116).

**False Positives:**

- `Steuerpflichtiger Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Dieter Leufkes` — partial — gold is substring of pred: `Dieter Leufkes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dagobert Nordholt`(person)
- `Dieter Leufkes`(person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich`(address)
- `FA Kirchdorf Perg Steyr`(organisation)
- `36-532/2242`(tax_number)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Beschwerdesache  Ludger Weynand` — partial — gold is substring of pred: `Ludger Weynand`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `Ludger Weynand`(person)
- `Plestätten 139Y, 4923 Reintal, Österreich`(address)
- `27-924/8149`(tax_number)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `name_at_end_of_sentence`

**F1:** 0.014 | **Precision:** 0.010 | **Recall:** 0.022  

**Format:** `regex`  
**Description:**
Captures names at the end of a sentence or before specific punctuation when no title is present.

**Content:**
```
(?:\n|\s|^)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s*\n|\s*\.|\s*,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.010 | 0.022 | 0.014 | 195 | 2 | 193 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 193 | 88 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Wilhelm Konetzny` | `Wilhelm Konetzny` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gabriele Friedbacher` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Priv` — positional overlap with gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`
- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`
- `Kind Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Zeitraum  November` — no gold match — likely missing annotation

> overlaps gold: 3  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Krankenpflege Grillenreith` — partial — pred is substring of gold: `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Im Zeitraum` — no gold match — likely missing annotation
- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_14`)


Ab November  2017 war sie aufgrund ihrer schweren Krankheit nicht arbeitsfähig.“

**False Positives:**

- `Ab November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_15`)


Der Beschwerde beigelegt war eine Betätigung eines Allgemeinmediziners vom 27.11.2019,  wonach Stella Marschalk, Bakk. techn.  auf Grund einer schweren Erkrankung (Sensibilitätsdefizit untere  Extremitäten DD: Guillain-Barré-Syndrom) von Oktober 2017 bis Ende Juni 2018 nicht  arbeitsfähig gewesen sei.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Ende Juni` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Frau  Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_26`)


Dem Vorlageantrag beigelegt war ein Schreiben der Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith, in dem bestätigt wurde, dass Stella Marschalk, Bakk. techn.  die Schule in  der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_28`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die BF bezog im streitgegenständlichen Zeitraum Familienbeihilfe und Kinderabsetzbeträge für  ihre Tochter Stella Marschalk, Bakk. techn. (geboren im September 1998).

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)
- `September 1998`(date)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_35`)


Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abweisung)

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Richter Dr` — positional overlap with gold: `Dr. Siegfried Fenz`
- `Beschwerdesache  Frauke Stuhldreher` — partial — gold is substring of pred: `Frauke Stuhldreher`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_4`)


– Zeitraum von – bis  (Nachname die Bf.) Maximiliane Sakschewsky, MA … 1201 ab Juli 2019  Begründung  Der Mittelpunkt der Lebensinteressen ihrer bereits volljährigen Tochter liegt nicht in  Österreich.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Österreich`(country)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_9`)


Die Beschwerde wurde mit folgender Begründung erhoben:  Klarstellung: Der Zeitraum der beantragten Familienbeihilfe ist von 01.06.2019 bis 30.09.2020  für meine Tochter Maximiliane Sakschewsky, MA (Nachname wie Bf.) (geboren am … .12.2001).

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_10`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname wie Bf.) sind mit der Kindesmutter und  1 von 7 Seite 2 von 7

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Protokoll Ri  Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_12`)


Dort besuchte Maximiliane Sakschewsky, MA  ab Herbst 2014 das King's School.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `King's School`(organisation)

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_13`)


Ende Mai 2019 wurde meine noch minderjährige [Anmerkung: 17 ½ -jährige] Tochter aus der  Wohnung der Familie des Ziehvaters in Worcester weggewiesen.

**False Positives:**

- `Ende Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Worcester`(city)

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_15`)


Unbeschadet dieses  Umstandes habe ich sämtliche Unterhaltskosten für meine Tochter Maximiliane Sakschewsky, MA, wie  bereits seit Ihren Aufenthaltswechsel im Jahr 2014 in das Vereinigte Königreich, im  Antragszeitraum noch EU-Mitgliedstaat, weiter getragen.

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`
- `Vereinigte Königreich` — type mismatch — same span as gold: `Vereinigte Königreich`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Vereinigte Königreich`(country)

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_20`)


Gemäß obigen Ausführungen ist meine Tochter Maximiliane Sakschewsky, MA  seit Sommer 2014,  ausgenommen ferienbedingte Abwesenheiten, in Vereinigten Königreich wohnhaft.

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_23`)


Die Beschwerdevorlage erfolgte mit nachstehendem Sachverhalt und Anträgen:  Sachverhalt:  Der Bf stellte einen Antrag auf Gewährung der Familienbeihilfe für seine Tochter  Maximiliane Sakschewsky, MA  ab Juni 2019.

**False Positives:**

- `Tochter  Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_28`)


Im Jahr 2019 bis inkl Juli 2020 ging die Tochter des Bf in Großbritannien in die Schule und  verbrachte die Sommerferien in Wien bei ihrem Vater.

**False Positives:**

- `Im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_29`)


Ab September 2020 begann sie ein Studium in Großbritannien und verbrachte die Ferien laut  Angaben im Antrag wieder in Wien.

**False Positives:**

- `Ab September` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_30`)


Bis Mai 2019 lebte die Tochter bei ihrer Mutter in Großbritannien, danach bei dem Onkel ihres  Stiefvaters (ebenfalls in GB), der in diesem Zeitpunkt auch die Unterhaltskosten getragen hat  und ab September 2020 in einem Studentenwohnheim der University of Bristol.

**False Positives:**

- `Bis Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `University of Bristol`(organisation)

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_34`)


Siehe Inhaltsverzeichnis  Stellungnahme:  In seiner Beschwerde verzichtete der Bf ausdrücklich auf das Erlassen einer  Beschwerdevorentscheidung gem § 262 Abs 2 BAO und stellte zudem klar, dass er  Familienbeihilfe für den Zeitraum Juni 2019 – September 2020 beantragt.

**False Positives:**

- `Zeitraum Juni` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_37`)


Die Tragung der Kosten einer Unterkunft, Nahrung, Kleidung, etc, die in Großbritannien  mindestens auch nochmals EUR 1.000,- betragen würden, trägt demnach im Zeitraum Juni  2019 – Sept 2020 laut eigenen Angaben weder der Kindesvater noch die Kindesmutter.

**False Positives:**

- `Zeitraum Juni` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_41`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.

**False Positives:**

- `Sachverhalt   Am` — no gold match — likely missing annotation
- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `The King´s School Worcester`(organisation)
- `Maximiliane Sakschewsky, MA`(person)
- `The King's  School Worcester`(organisation)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_43`)


Im Mai 2019 wurde Maximiliane Sakschewsky, MA  nach einem Streit mit dem Ziehvater aus der  gemeinsamen Wohnung gewiesen.

**False Positives:**

- `Im Mai` — no gold match — likely missing annotation
- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_53`)


Am 31. Mai 2019 und in den folgenden Monaten, bis 3. August 2020, überwies der Bf. an die  Kindesmutter der (gemeinsamen) Töchter Maximiliane Sakschewsky, MA  und E. auf das Konto in  Großbritannien IBAN GB… 8171 € 1.000,00 (Kontoauszüge).

**False Positives:**

- `Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

**False Positives:**

- `Führerschein Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_61`)


Am 23. Oktober 2020 überwies der Bf. auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN  GB…1084 € 200,00 mit dem Verwendungszweck: Unterstützung, am 4. November 2020  € 500,00 am 25. und 30. November jeweils € 200,00.

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_66`)


Am 11. Dezember 2020 bestätigte die University of Bristol, that Miss Maximiliane Sakschewsky, MA (Tochter  des Bf.) student no.

**False Positives:**

- `Miss Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `University of Bristol`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_68`)


Miss Maximiliane Sakschewsky, MA … started at the University of Bristol on 28 September 2020 and is  expected to complete her course on 9 June 2023.

**False Positives:**

- `Miss Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of Bristol`(organisation)

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_70`)


Die Tochter des Bf. Maximiliane Sakschewsky, MA  war im beschwerdegegenständlichen Zeitraum nicht  zugehörig zum Haushalt des Bf.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_71`)


Diese Feststellung beruht auf folgenden Umständen:  Maximiliane Sakschewsky, MA  war vom September 2014 bis Juli 2020 Schülerin der King's School Worcester,  Großbritannien.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`
- `School Worcester` — partial — pred is substring of gold: `King's School Worcester`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `King's School Worcester`(organisation)
- `Großbritannien`(country)

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_73`)


Sodann zog Maximiliane Sakschewsky, MA  zu einem Onkel des  Ziehvaters nach Worcester (und haben in dieser Zeit der Onkel und dessen Frau die Kosten für  Essen und Logie getragen).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_74`)


Im September 2020 nahm Maximiliane Sakschewsky, MA  an der University of  Bristol ein full time- Studium auf.

**False Positives:**

- `Im September` — no gold match — likely missing annotation
- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of  Bristol`(organisation)

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_77`)


2.  Eine überwiegende Unterhaltstragung betreffend Maximiliane Sakschewsky, MA  durch den Bf. kann nicht  erkannt werden.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_79`)


Der Bf. leistete im beschwerdegegenständlichen Zeitraum Unterhalt wie folgt:  - Für beide Töchter – Maximiliane Sakschewsky, MA  und E. – insgesamt monatlich € 1.000,00 (am 11. August  2020 überwies der Bf. für seine Tochter E. € 500,00, am 14. September 2020 € 140,00 und am  01. Oktober 2020 € 500,00).

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation
- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_81`)


Unter Bedachtnahme auf das eigene Vorbringen des Bf.: ‚Ich habe monatlich € 1.000,- an  meine Ex-Gattin überwiesen, die als Schulgeld galten.‘ und den Umstand, dass diese  Überweisungen für beide Töchter erfolgt waren, bedarf es auf Basis der obigen Feststellungen  keiner weiteren Ausführungen, dass mit den Leistungen des Bf. nicht die überwiegenden  Unterhaltskosten seiner (17 ½- bis 18 ½- jährigen) Tochter Maximiliane Sakschewsky, MA, die ab Mai 2019  bei einem Onkel ihres Ziehvaters und dessen Frau (in Worcester) und sodann zeitweilig (der Bf.  spricht von 1 Monat) bei der Mutter ihres Freundes lebte, abgedeckt worden sind.

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_82`)


3. Rechtliche Beurteilung  3.1.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_84`)


Eine Person, zu deren Haushalt das Kind nicht gehört, die jedoch die  Unterhaltskosten für das Kind überwiegend trägt, hat dann Anspruch auf Familienbeihilfe,  wenn keine andere Person nach dem ersten Satz anspruchsberechtigt ist.

**False Positives:**

- `Eine Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_85`)


Wie oben unter Punkt ausgeführt, erfüllt der Bf. die Voraussetzung, die Person zu sein, zu  deren Haushalt Maximiliane Sakschewsky, MA  gehört, nicht.

**False Positives:**

- `Haushalt Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_86`)


Der Bf. erfüllte die alternativ zu beurteilende Voraussetzung, die Unterhaltskosten für  Maximiliane Sakschewsky, MA  überwiegend zu tragen, wie oben unter Punkt 2. ausgeführt, nicht.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation
- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Richter Mag` — positional overlap with gold: `Mag. Ashley Partenfelder`
- `Beschwerdesache Patricia Jentz` — partial — gold is substring of pred: `Patricia Jentz`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation
- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU Wien)`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU Wien)`(organisation)

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (JKU Linz)`
- `Bachelorstudium Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Johannes Kepler Universität Linz (JKU Linz)`(organisation)
- `JKU Linz`(organisation)
- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_14`)


 Abgangsbescheinigung der JKU Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften (Studienplan 2018W)

**False Positives:**

- `Bachelorstudium  Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU Linz`(organisation)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_26`)


6. Die Bf. antwortete mit einer am 13.12.2021 bei der belangten Behörde eingelangter Eingabe  und legte ein E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  3 von 16 Seite 4 von 16

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation
- `Johannes Kepler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_33`)


An der WU Wien wurde das Studium  Wirtschafts- und Sozialwissenschaften (Bachelor) betrieben, in Linz handelte es sich um das  Studium Wirtschaftswissenschaften (Bachelor).

**False Positives:**

- `Studium Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `WU Wien`(organisation)
- `Linz`(city)

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_60`)


Im Dezember 2021 langte dann noch eine Bestätigung der JKU  Linz ein, die die beiden Studien „grundsätzlich gleichwertig“ ansah.

**False Positives:**

- `Im Dezember` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU  Linz`(organisation)

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`
- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)
- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz (`(organisation)

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_76`)


Die beiden genannten Bachelor-Studien sind an der jeweiligen Universität jeweils die  „klassischen“ bzw. typischen wirtschaftswissenschaftlichen Bachelor-Studien, umfassen jeweils  einen Aufwand von 180 ECTS-Punkten bei 6 Semestern Mindeststudiendauer.

**False Positives:**

- `Semestern Mindeststudiendauer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU)`
- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (JKU)`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU)`(organisation)
- `Johannes Kepler Universität Linz (JKU)`(organisation)

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_89`)


Beide Bachelorstudien sind nach § 2 der jeweiligen Curricula ein sozial- und  wirtschaftswissenschaftliches Studium im Sinne des § 54 Abs. 1 Universitätsgesetz 2002 und  umfassen jeweils einen Arbeitsumfang von 180 ECTS-Punkten, 6 Semester  Mindeststudiendauer, die Absolvierung einer Studieneingangsphase und die Abfassung einer  Bachelorarbeit.

**False Positives:**

- `Semester  Mindeststudiendauer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_106`)


Die Bf. legte eine Bestätigung der JKU Linz vor, wonach - vergleicht man die  Qualifikationsprofile der beiden Studien - von einer grundsätzlichen Gleichwertigkeit der  beiden Studien ausgegangen werden könne.

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU Linz`(organisation)

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_110`)


3. Rechtliche Beurteilung  3.1. Rechtslage  Gemäß § 2 Abs. 1 lit. b Familienlastenausgleichsgesetz 1967 idF. BGBl. I Nr. 24/2019 und Nr.  28/2020 haben Personen Anspruch auf Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_112`)


Bei Kindern, die eine in § 3 des Studienförderungsgesetzes 1992, BGBl.Nr. 305, genannte  Einrichtung besuchen, ist eine Berufsausbildung nur dann anzunehmen, wenn sie die  vorgesehene Studienzeit pro Studienabschnitt um nicht mehr als ein Semester oder die  vorgesehene Ausbildungszeit um nicht mehr als ein Ausbildungsjahr überschreiten.

**False Positives:**

- `Bei Kindern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_123`)


3.2. Zu Spruchpunkt I. (Stattgabe)  Die Bf. absolvierte im ersten Studienjahr erfolgreich die Studieneingangs- und  Orientierungsphase (StEOP).

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_126`)


Die Bf. hält dem entgegen, es handle sich nicht um einen Wechsel des Studiums, sondern  lediglich der "Einrichtung", weshalb kein studienbehilfeschädlicher Studienwechsel vorliege  und daher auch keine Rückforderung der ab dem Wechsel ausbezahlten Studienbehilfe zu  erfolgen habe.

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_129`)


Kein Studienwechsel (und damit außerhalb des Anwendungsbereiches des § 17 StudFG) ist der  Wechsel der Studieneinrichtung/des Studienortes bei gleichbleibender Studienrichtung.

**False Positives:**

- `Kein Studienwechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_149`)


Die Bf. hat daher zwar einen Studienortwechsel, aber  keinen Wechsel des Studiums vorgenommen.

**False Positives:**

- `Die Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Richterin Priv` — positional overlap with gold: `Priv.-Doz.in Farina Kohlstrunk`
- `Beschwerdesache Mathilda Eckholdt` — partial — gold is substring of pred: `Mathilda Eckholdt`
- `Obere Hauptstraße` — partial — pred is substring of gold: `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See`
- `Tür Top` — partial — pred is substring of gold: `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Farina Kohlstrunk`(person)
- `Mathilda Eckholdt`(person)
- `Kleingassen 3, 4150 Reith, Österreich`(address)
- `Mag. András Péter Radics`(person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See`(address)
- `Bundesfinanzgericht`(organisation)
- `Finanzamt Österreich`(organisation)
- `69-575/0475`(tax_number)

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_5`)


§ 284 BAO lautet auszugsweise:  (1) Wegen Verletzung der Entscheidungspflicht kann die Partei Beschwerde  (Säumnisbeschwerde) beim Verwaltungsgericht erheben, wenn ihr Bescheide der  Abgabenbehörden nicht innerhalb von sechs Monaten nach Einlangen der Anbringen oder nach  1 von 3 Seite 2 von 3

**False Positives:**

- `Partei Beschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Richter Priv` — positional overlap with gold: `Priv.-Doz. Quirin Januszis`
- `Jennifer Papenhagen` — partial — pred is substring of gold: `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 75** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Richterin Mag` — positional overlap with gold: `Mag. Gabriele Friedbacher`
- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, MA 67`
- `Wiener Parkometerabgabeverordnung` — no gold match — likely missing annotation
- `Stadt Wien Nr` — no gold match — likely missing annotation
- `Stadt Wien Nr` — no gold match — likely missing annotation
- `Wiener Parkometergesetz` — no gold match — likely missing annotation
- `Wien Nr` — no gold match — likely missing annotation
- `Wien Nr` — no gold match — likely missing annotation
- `Wiener  Abgabenorganisationsrecht` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 7

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 76** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_7`)


von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am  2. Mai 2025 um 11:09 Uhr in 1100 Wien, Gasse, beanstandet, da ein gültiger Parkschein fehlte.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `1100 Wien`(address)

**Example 77** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_11`)


Wegen dieser Verwaltungsübertretung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung  iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 wurde über den Bf. eine Geldstrafe in Höhe von  75,00 Euro verhängt bzw. im Falle der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 17  Stunden auferlegt.

**False Positives:**

- `Wiener Parkometergesetz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_12`)


Der Bf. erhob Online am 9. Juli 2025 (fristgerecht) Einspruch gegen diese Strafverfügung und  brachte begründend vor: „Am 02.05.2025, versah ich, BF1, geb geb., meinen Dienst in der dem  Tatort nächstgelegenen Dienststelle der Dienststelle (Dienststelle1).

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

**False Positives:**

- `Wiener  Parkometergesetz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 80** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_23`)


Die Abgabe sei mit der ordnungsgemäßen Entwertung des Parkscheins (der Parkscheine) oder  mit der Bestätigung der Abstellanmeldung bei Verwendung eines elektronischen Parkscheines  entrichtet (§ 5 Abs. 1 Parkometerabgabeverordnung kundgemacht im Amtsblatt der Stadt  Wien vom 22.12.2005, Heft Nr. 51).

**False Positives:**

- `Heft Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien`(city)

**Example 81** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_24`)


Abgabepflichtige, die ein mehrspuriges Fahrzeug in einer Kurzparkzone abstellen, hätten dafür  zu sorgen, dass es während der Dauer seiner Abstellung mit einem richtig angebrachten und  richtig entwerteten Parkschein gekennzeichnet oder ein elektronischer Parkschein aktiviert sei  (§§ 3 Abs. 1 und 7 Abs. 1 der Kontrolleinrichtungenverordnung, Amtsblatt der Stadt Wien  Nr. 33/2008).

**False Positives:**

- `Stadt Wien  Nr` — partial — gold is substring of pred: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 82** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_30`)


Ein Rechtfertigungsgrund, also eine Norm, die das tatbestandsmäßige Verhalten  ausnahmsweise erlaube bzw. welche die Strafbarkeit aufheben würde, liege im  gegenständlichen Fall nicht vor.

**False Positives:**

- `Ein Rechtfertigungsgrund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_33`)


Nach § 4 Abs. 1 des Parkometergesetzes 2006 genüge zur Strafbarkeit des dort umschriebenen  Verhaltens Fahrlässigkeit.

**False Positives:**

- `Verhaltens Fahrlässigkeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_37`)


Weiters enthält das Straferkenntnis die maßgeblichen Bestimmungen für die Strafbemessung  (§ 4 Abs. 1 Wiener Parkometergesetz 2006, § 19 Verwaltungsstrafgesetz 1991), erläutert diese  näher und führt die für den vorliegenden Fall maßgeblichen Strafzumessungsgründe an (hier:  Einkommens- und Vermögensverhältnisse sowie allfällige Sorgepflichten des Bf. seien, soweit  diese der Behörde bekannt gewesen seien, berücksichtigt worden.

**False Positives:**

- `Wiener Parkometergesetz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_41`)


Der Bf. erhob gegen das Straferkenntnis mit Anbringen vom 5. September 2025 (fristgerecht)  Beschwerde, führte aus wie im oben angeführten Einspruch gegen die Strafverfügung vom  30. Juni 2025 mit dem Ersuchen, die im Straferkenntnis festgelegte Geldstrafe in Höhe von  65,00 Euro [Anmerkung BFG, gemeint: Geldstrafe in Höhe von 55,00 Euro] herabzusetzen.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG,`(organisation)

**Example 86** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_42`)


Die Magistratsabteilung 67 legte die Beschwerde samt dem bezughabenden Verwaltungsakt  dem Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 1. Oktober 2025).

**False Positives:**

- `Die Magistratsabteilung` — positional overlap with gold: `Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistratsabteilung 67`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 87** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_44`)


Der Bf. war der Lenker des auf ihn zugelassenen tatgegenständlichen Kraftfahrzeuges.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_49`)


Der Abstellort, der Beanstandungszeitpunkt und die Lenkereigenschaft des Bf. wurden vom Bf.  im gegenständlichen Fall nicht bestritten.

**False Positives:**

- `Der Abstellort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_50`)


Der Bf. bekämpft mit der gegenständlichen Beschwerde ausschließlich die mit dem  Straferkenntnis festgesetzte Strafhöhe, somit war entsprechend der ständigen Judikatur des  Verwaltungsgerichtshofes von einer Teilrechtskraft des Schuldspruches auszugehen (vgl. z.B.  VwGH 20.9.2013, 2013/17/0305).

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 90** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_51`)


Rechtsgrundlage und rechtliche Würdigung:    Gemäß § 4 Abs. 1 Wiener Parkometergesetz 2006 sind Handlungen und Unterlassungen, durch  die die Abgabe hinterzogen oder fahrlässig verkürzt wird, als Verwaltungsübertretungen mit  Geldstrafen bis zu 365 Euro zu bestrafen.

**False Positives:**

- `Wiener Parkometergesetz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_58`)


Der Bf. hat das öffentliche Interesse an der Rationierung des in Wien vorhandenen Parkraums  dadurch geschädigt, dass er das Kraftfahrzeug ohne Parkschein in einer Kurzparkzone  abgestellt hat.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien`(city)

**Example 92** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_64`)


Wie bereits ausgeführt, sind Verwaltungsübertretungen wie die vorliegende, nämlich die  fahrlässige Verkürzung der Parkometerabgabe gemäß § 4 Abs. 1 Wiener Parkometergesetz  2006, mit Geldstrafen bis zu 365,00 Euro zu bestrafen.

**False Positives:**

- `Wiener Parkometergesetz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Richterin Priv` — positional overlap with gold: `Priv.-Doz.in Juliana Bartjen`
- `Beschwerdesache Renate Brombusch` — partial — gold is substring of pred: `Renate Brombusch`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 94** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Franz Josefskai` — partial — pred is substring of gold: `Franz Josefskai 53/2/10, 1010 Wien`
- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 9/18/19 Klosterneuburg`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Franz Josefskai 53/2/10, 1010 Wien`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `94-300/0486`(tax_number)

**Example 95** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf.) studierte an der Musikhochschule Wien und am Konservatorium  der Stadt Wien klassisches Schlagwerk sowie Theorie und Komposition an der Jazz-Abteilung.

**False Positives:**

- `Verfahrensgang  Der Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Musikhochschule Wien`(organisation)
- `Konservatorium  der Stadt Wien`(organisation)

**Example 96** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_7`)


Ein Jahr lang erhielt er in Ort, in den Vereinigten Staaten, eine Ausbildung in Marimba und  Percussion.

**False Positives:**

- `Vereinigten Staaten` — type mismatch — same span as gold: `Vereinigten Staaten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Vereinigten Staaten`(country)

**Example 97** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_8`)


Der Bf. ist als Musiker sowohl selbständig als auch nichtselbständig tätig.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_72`)


Der Bf. habe seine hauptberufliche Tätigkeit als Musiker unverändert,  von Beginn an in der gleichen Art und Weise im Bereich Vibraphon/Schlagwerk ausgeübt.

**False Positives:**

- `Der Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `von_frau_person`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons identified by 'von Frau' followed by a full name (First and Last).

**Content:**
```
von Frau\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 79 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `title_okr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'ÖkR' followed by full name, including preceding titles like 'Dr.in'.

**Content:**
```
(?:Dr\.in\s+)?ÖkR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_hon_prof_dr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Hon.-Prof. Dr.' followed by name.

**Content:**
```
Hon\.-Prof\.\s+Dr\.\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_hr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'HR' or 'Techn R HR' followed by full name, including suffixes, excluding trailing commas.

**Content:**
```
(?:Techn\s+R\s+)?HR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.\s*iur\.|MBA|MSc|LLM|Dr\.\s*|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+\w+straße|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_univ_prof`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Univ.-Prof.' (including repeated titles) followed by name.

**Content:**
```
(?:Univ\.-Prof\.\s+)+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_dr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Dr.' followed by full name, ensuring umlauts are included and matching stops at punctuation, including 'von'.

**Content:**
```
Dr\.(?:\s+)?([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.\s*(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+\w+straße|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_vetr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'KommR VetR' or 'VetR' followed by full name.

**Content:**
```
(?:KommR\s+)?VetR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_ost_r`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'OStR' followed by full name, including suffixes.

**Content:**
```
OStR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.\s*iur\.|MBA|MSc|LLM|Dr\.\s*|Mag\.|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)(?=[,\s\n]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 15 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `OStR Tosca Knoller, ` — positional overlap with gold: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 1  |  likely missing annotation: 0

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

## `title_dr_in_priv_doz_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with compound title 'Dr.in Priv.-Doz.in' followed by full name.

**Content:**
```
Dr\.in\s+Priv\.-Doz\.in\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_nachname_wie_bf`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names immediately following the specific legal marker '(Nachname wie Bf.)'.

**Content:**
```
\(Nachname wie Bf\.\)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_fuer_die_kinder`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures bare names following 'für die Kinder' (for the children), common in family benefit cases.

**Content:**
```
für\s+die\s+Kinder\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_an_die`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'an die', strictly excluding company names and organizations.

**Content:**
```
an\s+die\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?!\s+(?:GmbH|AG|KG|OHG|UG|PartG|Rechtsanwälte|Steuerberatung|Beratung|Consulting|GmbH\s*&\s*Co\.|\s+\d|Wirtschaftsprüfungs-|Steuerberatungsgesellschaft|Talder|Stadt|Finanzamt|Bundesfinanzgericht|Gericht|Behörde|Kantonalbank|Bank|GmbH\s*&\s*Co\.))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 60 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_75`)


Diesen Lebensumständen stehen folgende inländische (österreichische) Anknüpfungspunkte  gegenüber: Nachweisliche Aufenthalte  - am 18. August 2019 (6-stündige Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" im Hinblick auf den beabsichtigten  Führerscheinerwerb),  vom 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019 sowie  17. bis 19. Februar 2020 (in Wien mit dem Bf. unternommene Fahrten gemäß § 19 Abs. 8 FSG;  am 20. Februar 2020 wurde vom Bf. die Überweisung von € 173,10 an die  Landespolizeidirektion Wien - Verkehrsamt vorgenommen).

**False Positives:**

- `Landespolizeidirektion Wien` — similar text (different position): `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)
- `Landespolizeidirektion Wien`(organisation)

</details>

---

## `known_person_names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known person entities from the training data to ensure high recall for these specific cases.

**Content:**
```
(?:Larissa Gmelich|Benjamin Dittke|Dr\.in Olga Arai|Veronika Zeitlhuber|Dr\. Dr\. Erich Papadakis|Kirstin Hänßen|Lucia Norkeit|Olivia Püttmanns|Meinrad Kühnken)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `german_person_with_title`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
DELETED: This rule was too broad and matched almost any capitalized word sequence.

**Content:**
```

```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_gegen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following 'gegen' (against) in legal contexts, excluding organizations.

**Content:**
```
(?:in\s+der\s+Finanzstrafsache\s+gegen\s+|in\s+der\s+Beschwerdesache\s+gegen\s+|gegen\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=[,\s\n]|$)(?!\s+(?:GmbH|AG|KG|OHG|UG|PartG|Rechtsanw\u00e4lte|Steuerberatung|Beratung|Consulting|GmbH\s*&\s*Co\.|\s+\d|Wirtschaftspr\u00fcfungs-|Steuerberatungsgesellschaft|mbH|\.\s*Co\.|Beschwerdesache|Finanzamt|Bundesfinanzgericht|Gericht|Beh\u00f6rde|Sachverhalt|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Beschwerdef\u00fchrerin|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt\s+|Stadt|Gericht|Beh\u00f6rde|Sachverhalt|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Beschwerdef\u00fchrerin|Die\s+Beschwerde|Die\s+Parteien|Bundesfinanzgericht|Finanzamt|Stadt|Gericht|Beh\u00f6rde|Sachverhalt|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Beschwerdef\u00fchrerin|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt\s+|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_herrn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'Herrn', including those with titles like OSR. Excludes 'Herrn' from the output.

**Content:**
```
Herrn\s+(?:OSR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+(?:\s*,\s*[A-Z]{2,4})?)(?=[,\s\n]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_in_verwaltungsstrafsache`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures the person name in 'in der Verwaltungsstrafsache gegen [Name], [Address]'. Excludes titles like 'Herrn'.

**Content:**
```
in\s+der\s+Verwaltungsstrafsache\s+gegen\s+(?!Herrn\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=,|\s+\d)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_in_verwaltungsstrafsache_general`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures the person name in 'in der Verwaltungsstrafsache gegen [Name]' where the name might have a title or not.

**Content:**
```
in\s+der\s+Verwaltungsstrafsache\s+gegen\s+(?:Mag\.|Dr\.|Priv\.-Doz\.|Univ\.-Prof\.|Hon\.-Prof\.|R\.\s*|KommR\s+KzlR|Ing\.|RgR\s+HR)?\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=,|\s+\d)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_osr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'OSR' (Oberster Staatsanwalt) followed by name and optional suffixes like MA, BA.

**Content:**
```
OSR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_omedr_str`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'OMedR StR' followed by name.

**Content:**
```
OMedR\s+StR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_repeated`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with repeated titles like 'Priv.-Doz. Priv.-Doz.' or 'Dr. Dr.', including 'von'.

**Content:**
```
(?:Priv\.-Doz\.(?:\s+Priv\.-Doz\.)?|\u00d6kR\s+\u00d6kR|Univ\.-Prof\.(?:\s+Univ\.-Prof\.)?|Dr\.(?:\s+Dr\.)?|Mag\.(?:\s+Mag\.)?)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?)(?:\s*,\s*[A-Z]{2,4})?(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_univ_prof_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Univ.-Prof.in' followed by full name.

**Content:**
```
Univ\.-Prof\.in\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_univ_prof_complex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Univ.-Prof.' or 'Univ.-Prof.in' combined with 'OMedR' and 'Dr.', including hyphenated names and 'von'.

**Content:**
```
(?:Univ\.-Prof\.(?:in)?(?:\s+OMedR\s+)?(?:Dr\.)?|OMedR\s+Dr\.)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.\s*(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+\w+straße|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_hr_kzlr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with the specific title 'HR KzlR' followed by a full name.

**Content:**
```
HR\s+KzlR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_univ_prof_in_priv_doz_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures the specific complex title 'Univ.-Prof.in Priv.-Doz.in' followed by name.

**Content:**
```
Univ\.-Prof\.in\s+Priv\.-Doz\.in\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_at_signature`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names at the end of a text block, typically after 'Grüßen' or similar closing phrases.

**Content:**
```
(?:Grüßen|Mit\s+freundlichen\s+Grüßen|Hochachtungsvoll|Mit\s+den\s+besten\s+Grüßen)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=\s*\.|\s*$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_complex_academic`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with complex academic titles like 'Dipl.-Ing. Dr.in', 'Mag. Dr.', 'Univ.-Prof.in' followed by full name.

**Content:**
```
(?:Dipl\.-Ing\.\s+Dr\.in|Mag\.\s+Dr\.|Univ\.-Prof\.in|Dr\.in\s+Dipl\.-Ing\.|Dr\.in\s+Mag\.|Dr\.in\s+Priv\.-Doz\.|Priv\.-Doz\.(?:in)?\s+Dr\.|Dr\.(?:in)?\s+Dipl\.-Ing\.|Dr\.(?:in)?\s+Mag\.|Dr\.(?:in)?\s+Priv\.-Doz\.|Hon\.-Prof\.(?:in)?\s+Dr\.|Dr\.(?:in)?\s+Hon\.-Prof\.(?:in)?|DDr\.)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*[A-Z]{2,4})?(?=,|\s+\d|\s+\n|\s+(?:Straße|Gasse|Weg|Platz|Allee|Ring|Boulevard|Nr\.|Hausnummer)|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_in_genitive_with_address`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names in genitive case followed by an address (comma + number), which is a strong indicator of a person.

**Content:**
```
(?:des|der)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=,\s+\d)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_dr_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Dr.in' (including repeated 'Dr.in Dr.in') followed by name.

**Content:**
```
(?:Dr\.in\s+){1,2}([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_prof_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Prof.in' (without Univ.-) followed by full name.

**Content:**
```
(?<!Univ\.-)Prof\.in\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_hon_prof_complex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with complex title chains including 'Priv.-Doz.in', 'Mag.a', 'Mag. Priv.-Doz.', etc., including 'von'.

**Content:**
```
(?:Mag\.(?:\s+Univ\.-Prof\.(?:in)?|\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?\s+Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.|Dr\.in|DDr\.)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.\s*(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+\w+straße|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `medr_title`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'OMedR' or 'MedR' or 'PhD MedR' followed by name, including 'von' and suffixes, excluding trailing punctuation.

**Content:**
```
(?:PhD\s+)?(?:OMedR\s+)?MedR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)?(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_prof_in_medr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Prof.in MedR' followed by full name.

**Content:**
```
Prof\.in\s+MedR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_with_complex_prefix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with prefixes like 'MedR', 'VetR', 'Bakk.', 'Techn R' including repeated titles and suffixes, including 'von'.

**Content:**
```
(?:Techn\s+R\s+)?(?:MedR\s+|VetR(?:\s+VetR)?\s+|Bakk\.\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.\s*iur\.|MBA|MSc|LLM|Dr\.\s*|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+straße|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_in_beschwerdesache_of`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'in der Beschwerdesache der/des' (genitive) to handle cases like 'der Ali Litwinov', excluding 'Frau' and organizations.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+der\s+|in\s+der\s+Beschwerdesache\s+des\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)(?=,|\s+\d|\s+\n|\s+\w+straße|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_richter_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'durch den Richter' or 'durch die Richterin', extracting only the name/title part.

**Content:**
```
(?:durch\s+den\s+Richter|durch\s+die\s+Richterin)\s+(?:Mag\.|Dr\.|Dr\.in|DDr\.in|Priv\.-Doz\.(?:in)?|Univ\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|R\.\s*|KommR\s+KzlR|Ing\.|RgR\s+HR|OMedR\s+|Mag\.(?:\s+Mag\.)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.|DDr\.|StR\s+|KommR\s+|RgR\s+|VetR\s+|Techn\s+R\s+)?([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=[,\s\n]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_kommr_repeated`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with repeated titles like 'KommR KommR' or 'KommR KzlR'.

**Content:**
```
(?:KommR\s+KommR|KommR\s+KzlR|KzlR\s+KommR)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_priv_doz_univ_prof`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with combined titles 'Priv.-Doz. Univ.-Prof.' or 'Univ.-Prof. Priv.-Doz.'.

**Content:**
```
(?:Priv\.-Doz\.(?:\s+Univ\.-Prof\.(?:in)?)|Univ\.-Prof\.(?:in)?(?:\s+Priv\.-Doz\.(?:in)?))\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_role_parenthetical`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'des/der [Role] ([Abbrev])' pattern, e.g., 'des Beschwerdeführers (Bf) Name'.

**Content:**
```
(?:des\s+der\s+)(?:Beschwerdeführer|Beschwerdeführerin|Antragsteller|Antragstellerin|Kläger|Klägerin|Beteiligte)\s*\(.*?\)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_comma_role`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures bare names following a role description and a comma (e.g., 'Eigentümer, Titus Kurbjun').

**Content:**
```
(?:Eigent\u00fcmer|Verkaufender|K\u00e4ufer|Verk\u00e4ufer|Grundst\u00fcckseigent\u00fcmer|Betriebseigent\u00fcmer|Partei|Parteien|Antragsteller|Antragstellerin|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.)\s*,\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_stR_fixed`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures 'StR' (Strafverteidiger) but excludes 'OStR' using word boundaries, updated to not conflict with complex titles.

**Content:**
```
(?<!O)(?<!\w)StR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_verb_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following verbs like 'hat', 'ist', 'war' in specific legal contexts (e.g., 'hat durch den Richter [Name]').

**Content:**
```
(?:hat\s+durch\s+den\s+Richter|hat\s+durch\s+die\s+Richterin)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_combined_mag_hon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures combined titles like 'Mag.a Hon.-Prof.in' or 'Mag. Prof.' or 'Hon.-Prof.in' followed by name.

**Content:**
```
(?:Mag\.(?:a\s+)?(?:Hon\.-Prof\.(?:in)?\s+|Prof\.(?:\s+)?|\s+Prof\.)?|Hon\.-Prof\.(?:in)?\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.\s*iur\.|MBA|MSc|LLM|Dr\.\s*|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+\w+stra\u00dfe|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_kzlr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'KzlR' (Kanzleirat) followed by name, including the title in the match.

**Content:**
```
(?:"\s*)?KzlR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*"|,|\s+\d|\s+\n|\s+(?:Stra\u00dfe|Gasse|Weg|Platz|Allee|Ring|Boulevard|Nr\.|Hausnummer)|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_hon_prof_male`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Hon.-Prof.' (male) followed by name.

**Content:**
```
Hon\.-Prof\.(?:\s+in)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=,|\s+\d|\s+\n|\s+(?:Stra\u00dfe|Gasse|Weg|Platz|Allee|Ring|Boulevard|Nr\.|Hausnummer)|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_priv_doz_male`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Priv.-Doz.' (male) followed by name.

**Content:**
```
Priv\.-Doz\.(?:\s+in)?\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=,|\s+\d|\s+\n|\s+(?:Straße|Gasse|Weg|Platz|Allee|Ring|Boulevard|Nr\.|Hausnummer)|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_hon_prof_in_complex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures complex titles like 'Mag.a Priv.-Doz.in Hon.-Prof.in' followed by name.

**Content:**
```
(?:Mag\.a\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_priv_doz_dr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with compound title 'Priv.-Doz. Dr.' or 'Dr. Priv.-Doz.' followed by name, including 'von'. Excludes street addresses.

**Content:**
```
(?:Priv\.-Doz\.(?:\s+Dr\.)?|Dr\.(?:\s+Priv\.-Doz\.)?)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?)(?=,|\s+\d|\s+\n|\s+(?:Stra\u00dfe|Gasse|Weg|Platz|Allee|Ring|Boulevard|Nr\.|Hausnummer)|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_gegenüber_herrn`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'gegenüber Herrn' or 'gegenüber der' (genitive) to handle cases like 'gegenüber Herrn Rudolf Magerhans'.

**Content:**
```
(?:gegenüber\s+Herrn\s+|gegenüber\s+der\s+|gegenüber\s+des\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=,|\s+\d|\s+\n|\s+\w+straße|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_in_followup_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names appearing in 'in der Folge kurz mit Bf.' or similar contexts where the name precedes the abbreviation.

**Content:**
```
(?:wurde\s+|gegenüber\s+|in\s+der\s+Beschwerdesache\s+|in\s+der\s+Rechtssache\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*in\s+der\s+Folge\s+kurz\s+mit\s+Bf\.|\s*,\s*(?:Bf\.|Beschwerdeführer|Beschwerdeführerin))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_omedr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'OMedR' or 'Techn R OMedR' or 'VetR OMedR' followed by name.

**Content:**
```
(?:Techn\s+R\s+|VetR\s+)?OMedR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=,|\s+\d|\s+\n|\s+(?:Straße|Gasse|Weg|Platz|Allee|Ring|Boulevard|Nr\.|Hausnummer)|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_wurde_passive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names appearing after 'wurde' in passive constructions, e.g., 'wurde Yorick Hütther, in der Folge...'.

**Content:**
```
(?:wurde\s+|wurden\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*in\s+der\s+Folge|\s*,\s*(?:Bf\.|Beschwerdeführer|Beschwerdeführerin))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_kommr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Priv.-Doz.in KommR' or 'Kfm. StR' followed by name, ensuring full title is captured.

**Content:**
```
(?:Priv\.-Doz\.(?:in)?\s+KommR|Kfm\.\s+StR)(?:\s+[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*MBA)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_in_list_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following phrases like 'nannte der Bf die folgenden Namen:' or similar list introductions.

**Content:**
```
(?:nannte\s+der\s+Bf\s+die\s+folgenden\s+Namen:|die\s+folgenden\s+Namen:|die\s+Namen:|die\s+Namen\s+der\s+Personen:)(?:\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_at_start_of_sentence_tightened`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names at start of sentence, excluding common non-name words, organizations, and month names. FIXED: Added 'Punkt' to exclusion list.

**Content:**
```
(?:^|\.)\s*((?!Die\s+|Verfahrensgang|Entscheidungsgr\u00fcnde|Begr\u00fcndung|Beschluss|Hinweis|Feststellung|Erw\u00e4gung|Anmerkung|Antrag|Antragsteller|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|GmbH|AG|KG|PartG|Rechtsanw\u00e4lte|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|Punkt)[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 97 | 0 | 97 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 97 | 87 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_4`)


Am 30.09.2019 langte beim Finanzamt die Antwort der Beschwerdeführerin (in der Folge BF)  auf ein Überprüfungsschreiben des Anspruches auf Familienbeihilfe ein.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_11`)


Seit 2.7.2018 absolviert sie  eine Lehre zur Steuerassistentin.

**False Positives:**

- `Seit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Im Zeitraum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_14`)


Ab November  2017 war sie aufgrund ihrer schweren Krankheit nicht arbeitsfähig.“

**False Positives:**

- `Ab November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_27`)


7. Am 12.10.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor und beantragte die Abweisung, da die Ausbildung am 04.10.2017 beendet  worden sei.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_35`)


Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abweisung)

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_58`)


Linz, am 2. Dezember 2020

**False Positives:**

- `Linz` — type mismatch — same span as gold: `Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Linz`(city)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_10`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname wie Bf.) sind mit der Kindesmutter und  1 von 7 Seite 2 von 7

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_13`)


Ende Mai 2019 wurde meine noch minderjährige [Anmerkung: 17 ½ -jährige] Tochter aus der  Wohnung der Familie des Ziehvaters in Worcester weggewiesen.

**False Positives:**

- `Ende Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Worcester`(city)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_28`)


Im Jahr 2019 bis inkl Juli 2020 ging die Tochter des Bf in Großbritannien in die Schule und  verbrachte die Sommerferien in Wien bei ihrem Vater.

**False Positives:**

- `Im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_29`)


Ab September 2020 begann sie ein Studium in Großbritannien und verbrachte die Ferien laut  Angaben im Antrag wieder in Wien.

**False Positives:**

- `Ab September` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_30`)


Bis Mai 2019 lebte die Tochter bei ihrer Mutter in Großbritannien, danach bei dem Onkel ihres  Stiefvaters (ebenfalls in GB), der in diesem Zeitpunkt auch die Unterhaltskosten getragen hat  und ab September 2020 in einem Studentenwohnheim der University of Bristol.

**False Positives:**

- `Bis Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `University of Bristol`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_43`)


Im Mai 2019 wurde Maximiliane Sakschewsky, MA  nach einem Streit mit dem Ziehvater aus der  gemeinsamen Wohnung gewiesen.

**False Positives:**

- `Im Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_53`)


Am 31. Mai 2019 und in den folgenden Monaten, bis 3. August 2020, überwies der Bf. an die  Kindesmutter der (gemeinsamen) Töchter Maximiliane Sakschewsky, MA  und E. auf das Konto in  Großbritannien IBAN GB… 8171 € 1.000,00 (Kontoauszüge).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_54`)


Am 18. August 2019 wurde der Tochter des Bf. die Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" gemäß §6 der Führerscheingesetz- Durchführungsverordnung von 1997, in der Dauer von sechs Stunden bestätigt.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_59`)


Am 11. August 2020 überwies der Bf. auf das Konto in Großbritannien IBAN GB…1114 € 500,00  E… (Nachname wie Bf.), am 14. September 2020 € 140,00.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_61`)


Am 23. Oktober 2020 überwies der Bf. auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN  GB…1084 € 200,00 mit dem Verwendungszweck: Unterstützung, am 4. November 2020  € 500,00 am 25. und 30. November jeweils € 200,00.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_64`)


Am 19. Dezember 2020 überwies der Bf. auf das Konto K. H., IBAN GB…1233 € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_65`)


Am 13. Jänner 2021 ersuchte das Finanzamt den Bf. um den „Nachweis der Überweisungen der  Alimente an ihre Tochter bzw. an die Kindesmutter ab Juni 2019 lfd.“.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_66`)


Am 11. Dezember 2020 bestätigte die University of Bristol, that Miss Maximiliane Sakschewsky, MA (Tochter  des Bf.) student no.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `University of Bristol`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_68`)


Miss Maximiliane Sakschewsky, MA … started at the University of Bristol on 28 September 2020 and is  expected to complete her course on 9 June 2023.

**False Positives:**

- `Miss Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of Bristol`(organisation)

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_69`)


2. Beweiswürdigung  1.

**False Positives:**

- `Beweiswürdigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_70`)


Die Tochter des Bf. Maximiliane Sakschewsky, MA  war im beschwerdegegenständlichen Zeitraum nicht  zugehörig zum Haushalt des Bf.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_74`)


Im September 2020 nahm Maximiliane Sakschewsky, MA  an der University of  Bristol ein full time- Studium auf.

**False Positives:**

- `Im September` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of  Bristol`(organisation)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_82`)


3. Rechtliche Beurteilung  3.1.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_84`)


Eine Person, zu deren Haushalt das Kind nicht gehört, die jedoch die  Unterhaltskosten für das Kind überwiegend trägt, hat dann Anspruch auf Familienbeihilfe,  wenn keine andere Person nach dem ersten Satz anspruchsberechtigt ist.

**False Positives:**

- `Eine Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_92`)


Wien, am 17. August 2021

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_56`)


Am 09.08.2021 langte dann die Vorhaltsbeantwortung ein mit den  Studienerfolgsnachweisen der beiden Studien aus der eine Anrechnung von 24 ECTS erkennbar  war.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_59`)


Am 07.10.2021 langte dann eine Beschwerde ein, mit der  Begründung, dass es sich nicht um einen schädlichen Studienwechsel handle, sondern nur um  einen Wechsel des Studienortes.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_60`)


Im Dezember 2021 langte dann noch eine Bestätigung der JKU  Linz ein, die die beiden Studien „grundsätzlich gleichwertig“ ansah.

**False Positives:**

- `Im Dezember` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU  Linz`(organisation)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_63`)


Am 12.04.2022 reichte die  Beschwerdeführerin den Vorlageantrag ein, damit die Beschwerde dem Bundesfinanzgericht  zur Entscheidung vorgelegt wird und der Bescheid ersatzlos aufgehoben wird.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

**False Positives:**

- `Studienschwerpunkte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/`(website)
- `WU`(organisation)
- `JKU`(organisation)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_110`)


3. Rechtliche Beurteilung  3.1. Rechtslage  Gemäß § 2 Abs. 1 lit. b Familienlastenausgleichsgesetz 1967 idF. BGBl. I Nr. 24/2019 und Nr.  28/2020 haben Personen Anspruch auf Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_112`)


Bei Kindern, die eine in § 3 des Studienförderungsgesetzes 1992, BGBl.Nr. 305, genannte  Einrichtung besuchen, ist eine Berufsausbildung nur dann anzunehmen, wenn sie die  vorgesehene Studienzeit pro Studienabschnitt um nicht mehr als ein Semester oder die  vorgesehene Ausbildungszeit um nicht mehr als ein Ausbildungsjahr überschreiten.

**False Positives:**

- `Bei Kindern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_129`)


Kein Studienwechsel (und damit außerhalb des Anwendungsbereiches des § 17 StudFG) ist der  Wechsel der Studieneinrichtung/des Studienortes bei gleichbleibender Studienrichtung.

**False Positives:**

- `Kein Studienwechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_155`)


Studium, welches ebenfalls an mehreren Universitätsstandorten in Österreich angeboten wird,  wobei sich auch hier die konkreten Studienpläne bzw. –inhalte im Detail regelmäßig  unterscheiden und dennoch zum selben, als gleichartig anerkannten Ausbildungsergebnis  führen sowie jeweils Voraussetzung für die drei juristischen „Kernberufe“ Richter, Anwalt und  Notar sind.

**False Positives:**

- `Studium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_176`)


Linz, am 29. November 2022

**False Positives:**

- `Linz` — type mismatch — same span as gold: `Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Linz`(city)

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_22`)


Wien, am 29. Oktober 2025

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Bezirk` — partial — pred is substring of gold: `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_53`)


Feldkirch, am 30. September 2025

**False Positives:**

- `Feldkirch` — type mismatch — same span as gold: `Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Feldkirch`(city)

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_24`)


Abgabepflichtige, die ein mehrspuriges Fahrzeug in einer Kurzparkzone abstellen, hätten dafür  zu sorgen, dass es während der Dauer seiner Abstellung mit einem richtig angebrachten und  richtig entwerteten Parkschein gekennzeichnet oder ein elektronischer Parkschein aktiviert sei  (§§ 3 Abs. 1 und 7 Abs. 1 der Kontrolleinrichtungenverordnung, Amtsblatt der Stadt Wien  Nr. 33/2008).

**False Positives:**

- `Abgabepflichtige` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien`(city)

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_30`)


Ein Rechtfertigungsgrund, also eine Norm, die das tatbestandsmäßige Verhalten  ausnahmsweise erlaube bzw. welche die Strafbarkeit aufheben würde, liege im  gegenständlichen Fall nicht vor.

**False Positives:**

- `Ein Rechtfertigungsgrund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_49`)


Der Abstellort, der Beanstandungszeitpunkt und die Lenkereigenschaft des Bf. wurden vom Bf.  im gegenständlichen Fall nicht bestritten.

**False Positives:**

- `Der Abstellort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_85`)


Wien, am 20. Oktober 2025  7 von 7

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_36`)


Nur, weil es insbesondere in den letzten Jahren der  selbständigen Tätigkeit unseres Mandanten zu dem einen oder anderen Verlustjahr gekommen  ist - dies auch bedingt durch die Tatsache, dass junge Konkurrenz nachwuchs und unser  Mandant dadurch nicht mehr so einfach an Aufträge kam, weiters die Gagenhöhe im Bereich  der Jazzmusik laufend gesunken ist und viele Veranstalter vermehrt auf modischere Diskjockeys  zurückgegriffen haben - kann nicht ohne weitere Prüfung des Gesamterfolges einer Tätigkeit  von Liebhaberei ausgegangen werden.

**False Positives:**

- `Nur` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_65`)


Am 22.02.2017 brachte der steuerliche Vertreter des Bf. einen Antrag auf Vorlage der  Beschwerde an das Bundesfinanzgericht ein.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_89`)


Ab 1982 war der Bf. als 1. Perkussionist des Orchesters nichtselbständig beschäftigt.

**False Positives:**

- `Ab` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_105`)


Verhältnis der Verluste zu den Gewinnen oder Überschüssen,  3. Ursachen, auf Grund deren im Gegensatz zu vergleichbaren Betrieben, Tätigkeiten oder  Rechtsverhältnissen kein Gewinn oder Überschuß erzielt wird,  4. marktgerechtes Verhalten im Hinblick auf angebotene Leistungen,  5. marktgerechtes Verhalten im Hinblick auf die Preisgestaltung,  6.

**False Positives:**

- `Ursachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_109`)


Nach  9 von 14 Seite 10 von 14

**False Positives:**

- `Nach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_143`)


Gesamtgewinn (§ 3 Abs. 1 LVO) ist das Gesamtergebnis von der Begründung der Tätigkeit bis  zu deren Beendigung.

**False Positives:**

- `Gesamtgewinn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_164`)


Wien, am 27. August 2025

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_22`)


Im Jahr 2024 wurde beim Bf von der Abgabenbehörde eine Außenprüfung  2 von 7 Seite 3 von 7

**False Positives:**

- `Im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_54`)


Rechtliche Beurteilung  2.1. Zu Spruchpunkt I. (Abweisung)  § 205 BAO normiert auszugsweise:  Gemäß § 205 Abs. 1 BAO sind Differenzbeträge an Einkommensteuer und Körperschaftsteuer,  die sich aus Abgabenbescheiden unter Außerachtlassung von Anzahlungen (Abs. 3), nach  Gegenüberstellung mit Vorauszahlungen oder mit der bisher festgesetzt gewesenen Abgabe  ergeben, für den Zeitraum ab 1. Oktober des dem Jahr des Entstehens des Abgabenanspruchs  folgenden Jahres bis zum Zeitpunkt der Bekanntgabe dieser Bescheide zu verzinsen  (Anspruchszinsen).

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_56`)


Anspruchszinsen, die den Betrag von 50 Euro nicht erreichen, sind nicht festzusetzen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_96`)


Linz, am 5. Dezember 2025

**False Positives:**

- `Linz` — type mismatch — same span as gold: `Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Linz`(city)

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_11`)


Rechtliche Beurteilung (Spruchpunkt I.)  Gemäß § 256 Abs 3 BAO ist eine Beschwerde mit Beschwerdevorentscheidung (§ 262) oder mit  Beschluss (§ 278) als gegenstandslos zu erklären, wenn sie zurückgenommen wird.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_19`)


Wien, am 19. November 2025

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Michael` — partial — pred is substring of gold: `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Oleg Dell`(person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH`(organisation)
- `Hegelgasse 8, 1010 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `80-738/9953`(tax_number)

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_5`)


Am 31. Oktober 2023 erging ein Ergänzungsersuchen an den Bf. betreffend die geltend  gemachten Behandlungskosten in Höhe von Euro 10.299,13.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_7`)


Am 30. Dezember 2023 gab der Bf. bekannt, dass die Kosten für die Operation seiner Gattin  angefallen seien.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_17`)


Am 13. Februar 2024 erging ein weiteres Ergänzungsersuchen.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_26`)


Am 13. Juni 2024 legte die belangte Behörde die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_31`)


Am 1. Oktober 2025 fand die beantragte mündliche Verhandlung vor dem Bundesfinanzgericht  statt, in der insbesondere das Vorliegen bzw. Nichtvorliegen von triftigen medizinischen  Gründen diskutiert wurde.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_33`)


Am 3. November 2025 reichte der Bf. die beiden ergänzenden Befundberichte nach.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_34`)


Am 6. November 2025 fand die fortgesetzte mündliche Verhandlung statt.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_64`)


Dieser  4 von 8 Seite 5 von 8

**False Positives:**

- `Dieser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_74`)


Zur  Frage, wie lange ein Zuwarten auf einen Operationstermin ohne erhebliche medizinische  Nachteile möglich gewesen wäre, wird allgemein ausgeführt, dass ein Abwarten konkreter  motorischer Schwächen, um dann erst die Operation vorzunehmen, sicherlich nicht der  optimale Verlauf wäre und zudem (wiederum allgemein) angemerkt, dass eine zu späte  operative Versorgung zu bleibenden Wurzelschäden und motorischen Schwächen führen kann.

**False Positives:**

- `Zur  Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_79`)


3. Rechtliche Beurteilung  3.1.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_102`)


Bloße Wünsche, Befürchtungen oder Standesrücksichten der Betroffenen reichen nicht, um die  Zwangsläufigkeit zu rechtfertigen.

**False Positives:**

- `Bloße Wünsche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_104`)


Auch Aufwendungen, die nicht von der  gesetzlichen Krankenversicherung getragen werden, können dem Steuerpflichtigen  zwangsläufig erwachsen, wenn sie aus triftigen Gründen medizinisch geboten sind (vgl. VwGH  11.2.2016, 2013/13/0064 mwN).

**False Positives:**

- `Auch Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_125`)


Wien, am 17. November 2025  8 von 8

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 77** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_27`)


Im Fall  2 von 15 Seite 3 von 15

**False Positives:**

- `Im Fall` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_32`)


Am 30.11.2015 langte eine Vorhaltsbeantwortung des (damaligen) steuerlichen Vertreters ein,  in der vorgebracht wurde, dass hinsichtlich der Inanspruchnahme zur Haftung gem. § 9 iVm  § 80 BAO ein Ermessensspielraum des Finanzamtes bestehe.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_34`)


Seit 1.11.2015 sei Herr  Dieter Leufkes  wieder angestellt und beziehe ein Nettogehalt von ca. 1.400 €/Monat Von diesem  Einkommen könne ein Betrag von ca. 356 €/Monat gepfändet werden, jedoch sei dieser Betrag  bereits in Pfändung.

**False Positives:**

- `Seit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dieter Leufkes`(person)

**Example 80** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_40`)


Mit Datum 11.1.2016 erging der nunmehr angefochtenen Haftungsbescheid.

**False Positives:**

- `Mit Datum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_58`)


Der Zeitpunkt, für den zu beurteilen sei, ob der Primärschuldnerin die für die  Abgabenentrichtung erforderlichen Mittel zur Verfügung standen, bestimme sich danach,  wann die Abgaben bei Beachtung der abgabenrechtlichen Vorschriften zu entrichten gewesen  wären (VwGH 27.4.2000, 98/15/0003;

**False Positives:**

- `Der Zeitpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_60`)


Bei Selbstbemessungsabgaben (wie der Lohnsteuer und der Umsatzsteuer) sei maßgeblich,  wann die Abgaben bei ordnungsgemäßer Selbstberechnung abzuführen gewesen wären.

**False Positives:**

- `Bei Selbstbemessungsabgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_88`)


Im Jahr 2011 seien € 2.161.230,45, im Jahr 2012 wurden € 1.118.380,19 und im Jahr 2013  wurden € 593.447,25 an Umsätzen erzielt worden.

**False Positives:**

- `Im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_129`)


Am 22.3.2016 langte eine Beschwerde, eingebracht vom damaligen steuerlichen Vertreter des  Bf., gegen den erlassenen Haftungsbescheid ein.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_140`)


Am 4.4.2016 erging eine Beschwerdevorentscheidung (BVE), mit der die Beschwerde  abgewiesen wurde.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

**False Positives:**

- `Zum Hinweis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 87** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_165`)


Rechtliche Beurteilung  3.1.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_227`)


Graz, am 3. Dezember 2025

**False Positives:**

- `Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_22`)


5. Am 3.4.2025 stellte der Bf. durch seine steuerliche Vertretung den Antrag auf Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 90** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_23`)


6. Am 21.5.2025 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht vor und  beantragte, die Beschwerde als unbegründet abzuweisen.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 91** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_29`)


Am 4.11.2024 wurde der Ablauf der Bewilligung  dieser Aussetzung „infolge Beschwerdeerledigung“ verfügt.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_31`)


5. Am 9.1.2025 erfolgte die Festsetzung der Säumniszuschläge in Höhe von 235,71 Euro für die  Normverbrauchsabgabe und in Höhe von 265,92 Euro für die Umsatzsteuer.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_32`)


2. Beweiswürdigung  1.

**False Positives:**

- `Beweiswürdigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_34`)


3. Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abänderung)  1.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_65`)


Haller,  Normverbrauchsabgabegesetz2, § 11 Tz 10).

**False Positives:**

- `Haller` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_108`)


Feldkirch, am 12. Dezember 2025

**False Positives:**

- `Feldkirch` — type mismatch — same span as gold: `Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Feldkirch`(city)

</details>

---

## `title_kommir_ing`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with the specific title 'KommR Ing.' followed by a full name, handling cases where it appears as a subject or object, including 'Limited'.

**Content:**
```
KommR\s+Ing\.\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?=[,\s\n]|$|\s+Limited|\s+GmbH|\s+AG|\s+KG)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_herr_frau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures full names following 'Herr' or 'Frau', ensuring at least two words are captured and allowing for suffixes like ', BSc', 'BA LLB', 'BEd'. Excludes list markers.

**Content:**
```
(?:^|\s)(?:Herr|Frau)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 5 | 82 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `title_rgr_phd`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'RgR' followed by 'PhD' and name, or just 'RgR' and name.

**Content:**
```
RgR\s+(?:PhD\s+)?([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_mag_chain`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures 'Mag. Mag.' followed by name.

**Content:**
```
Mag\.\s+Mag\.\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_rgR_univ_prof_in_kommR`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures the specific complex title 'RgR Univ.-Prof.in KommR' followed by a name.

**Content:**
```
RgR\s+Univ\.-Prof\.in\s+KommR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_mag_a`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Mag.a' followed by full name, ensuring the full string is captured.

**Content:**
```
Mag\.a\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_ist`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'ist' (is), excluding corporate suffixes and honorifics like 'Herr' or 'Frau'.

**Content:**
```
(?:Die\s+|Der\s+|Die\s+|Das\s+)?(?<!Herr\s)(?<!Frau\s)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)\s+ist\s+(?!\s+(?:GmbH|AG|KG|OHG|UG|PartG|Rechtsanwälte|Steuerberatung|Beratung|Consulting|GmbH\s*&\s*Co\.|\s+\d|Wirtschaftsprüfungs-|Steuerberatungsgesellschaft|mbH|\.\s*Co\.|Finanzamt|Bundesfinanzgericht|Gericht|Behörde|Sachverhalt|Die\s+Beschwerdeführerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Beschwerdeführerin|Die\s+Beschwerde|Die\s+Parteien|Bundesfinanzgericht|Finanzamt|Stadt|Gericht|Behörde|Sachverhalt|Die\s+Beschwerdeführerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Beschwerdeführerin|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt\s+|Limited))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 12 | 30 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_22`)


Im Rückforderungsbetrag ist die  anteilige Geschwisterstaffel für sämtliche Kinder enthalten, für die Sie im  Rückforderungszeitraum zu Unrecht Familienbeihilfe erhalten haben (§ 8 Abs. 3  Familienlastenausgleichsgesetz 1967).“  4. Dagegen erhob die Bf. rechtzeitig die Beschwerde vom 07.10.2021 und brachte vor, dass  hierbei nur ein Wechsel des Studienortes bei gleichbleibender Studienrichtung vorliege.

**False Positives:**

- `Im Rückforderungsbetrag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_23`)


Unser Mandant ist hauptberuflich Musiker (Vibraphon, Schlagwerk), seine Tätigkeiten übt er  sowohl in Form von Dienstverhältnissen (z.B. Orchester) als auch als selbständiger Musiker  (Einzelunternehmer oder Gesellschafter diverser Musikensembles) aus.

**False Positives:**

- `Unser Mandant` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_113`)


Unter Gesamtgewinn ist der Gesamtbetrag der Gewinne zuzüglich steuerfreier  Einnahmen abzüglich des Gesamtbetrags der Verluste zu verstehen.

**False Positives:**

- `Unter Gesamtgewinn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_116`)


(2) Unter Gesamtüberschuß ist der Gesamtbetrag der Überschüsse der Einnahmen über die  Werbungskosten abzüglich des Gesamtbetrags der Verluste zu verstehen.

**False Positives:**

- `Unter Gesamtüberschuß` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_41`)


Der Zinsenbescheid ist an die im Spruch des zur  Nachforderung oder Gutschrift führenden Bescheides ausgewiesene Nachforderung bzw.  Gutschrift gebunden.

**False Positives:**

- `Der Zinsenbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_72`)


Der Zinsenbescheid ist an die im Spruch des zur Nachforderung oder Gutschrift führenden  Bescheides ausgewiesene Nachforderung bzw. Gutschrift gebunden (Ritz, BAO8, § 205 mit  Hinweis auf VwGH 27.2.2008, 2005/13/0039;

**False Positives:**

- `Der Zinsenbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_87`)


Die Belastung ist außergewöhnlich, soweit sie höher ist als jene, die der Mehrzahl der  Steuerpflichtigen gleicher Einkommensverhältnisse, gleicher Vermögensverhältnisse erwächst.

**False Positives:**

- `Die Belastung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

**False Positives:**

- `Das Bundesfinanzgericht` — partial — gold is substring of pred: `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_207`)


Wesentliches  Ermessenskriterium ist die Vermeidung eines endgültigen Abgabenausfalles.

**False Positives:**

- `Wesentliches  Ermessenskriterium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_46`)


2. Der Säumniszuschlag ist eine „Sanktion eigener Art“ (zB VwGH 21.4.1983, 83/16/0016;

**False Positives:**

- `Der Säumniszuschlag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_63`)


Die Steuer ist spätestens am Fälligkeitstag zu entrichten (Art.  21 Abs. 2 UStG-BMR).

**False Positives:**

- `Die Steuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_97`)


Die Abgabenbehörde ist aber nicht gehindert, den Säumniszuschlag mit einem neuen  Bescheid festzusetzen, sobald und sofern die Voraussetzungen dafür gegeben sind.

**False Positives:**

- `Die Abgabenbehörde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `name_after_colon`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing immediately after a colon, ensuring it looks like a name (at least two capitalized words) and excluding articles.

**Content:**
```
:\s*(?<!Die\s)(?<!Der\s)(?<!Die\s)(?<!Der\s)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*[A-Z]{2,4})?(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 5 | 60 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

**False Positives:**

- `Führerschein Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_71`)


Diese Feststellung beruht auf folgenden Umständen:  Maximiliane Sakschewsky, MA  war vom September 2014 bis Juli 2020 Schülerin der King's School Worcester,  Großbritannien.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `King's School Worcester`(organisation)
- `Großbritannien`(country)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_21`)


Mit Vorlagebericht vom 8.10.2025 legte das Finanzamt die gegenständliche Beschwerde vom  25.3.2025 betreffend Festsetzung von Anspruchszinsen für das Jahr 2021 dem  Bundesfinanzgericht zur Entscheidung vor und beantragte die Abweisung im Wesentlichen wie  folgt:  „Sachverhalt:   Der Beschwerdeführer (Bf) brachte am 21.08.2023 die Einkommensteuererklärung für das Jahr  2021 ein.

**False Positives:**

- `Der Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_3`)


Es wird folgender Säumniszuschlag festgesetzt:    Abgabe Betrag Säumniszuschlag 2%  Umsatzsteuer (Fahrzeugeinzelbesteuerung) 14.218,49 € 284,37 €

**False Positives:**

- `Abgabe Betrag Säumniszuschlag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `title_herr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Hr.' or 'Herr' followed by name, extracting only the name. Excludes 'von' context.

**Content:**
```
(?:^|\s)(?:von\s+)?(?:Hr\.|Herr\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_omdr_techn_r`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with combined titles 'OMedR Techn R' or 'VetR Techn R' followed by name.

**Content:**
```
(?:OMedR\s+|VetR\s+)?Techn\s+R\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_ing_dr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Ing. Dr.' followed by name.

**Content:**
```
Ing\.\s+Dr\.\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_dipl_kfm`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Dipl. Kfm.' followed by name.

**Content:**
```
Dipl\.\s+Kfm\.\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_prof_phd`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Prof. PhD' followed by name.

**Content:**
```
Prof\.\s+PhD\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_richter`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'Richter' or 'Richterin' with titles like 'Mag.', 'Dr.', 'Univ.-Prof.', etc.

**Content:**
```
(?:Richter|Richterin)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn|rer\.\s*nat|phil)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+straße|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_komr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'KommR' followed by name.

**Content:**
```
KommR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_ostR`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'OStR' (Obersteueranwalt) followed by name.

**Content:**
```
OStR\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 15 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `OStR Tosca Knoller` — partial — pred is substring of gold: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 1  |  likely missing annotation: 0

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

## `title_ing`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Ing.' (Ingenieur) followed by full name, handling addresses.

**Content:**
```
Ing\.(?:in)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_hon_prof_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Hon.-Prof.in' (including complex chains like Mag.a Priv.-Doz.in Hon.-Prof.in) followed by full name.

**Content:**
```
(?:Mag\.a\s+Priv\.-Doz\.in\s+Hon\.-Prof\.in|Hon\.-Prof\.in)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_mag_complex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with complex Mag titles like 'Mag. Mag. Hon.-Prof.' or 'Mag.a Priv.-Doz.in Hon.-Prof.in'.

**Content:**
```
(?:Mag\.(?:\s+Mag\.)?\s+Hon\.-Prof\.(?:in)?|Mag\.a\s+Priv\.-Doz\.in\s+Hon\.-Prof\.in)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_priv_doz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Priv.-Doz.' (including Dr. Dr. chains and complex title chains) followed by name, including 'von' and suffixes.

**Content:**
```
(?:Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Dr\.\s+Priv\.-Doz\.(?:in)?|Priv\.-Doz\.(?:in)?|Dr\.\s+Dr\.|Univ\.-Prof\.(?:in)?\s+Hon\.-Prof\.(?:in)?\s+Priv\.-Doz\.(?:in)?|Hon\.-Prof\.(?:in)?\s+Priv\.-Doz\.(?:in)?|Priv\.-Doz\.(?:in)?)(?:\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)?)?(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_stR_complex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures complex titles including 'Priv.-Doz.in DDr.in StR', 'DDr.in StR', 'StR', 'Kfm. StR', 'Priv.-Doz.in KommR', 'OStR', and 'VetR OMedR' (if not caught by omedr).

**Content:**
```
(?:Priv\.-Doz\.(?:in)?\s+DDr\.(?:in)?\s+StR|DDr\.(?:in)?\s+StR|StR|Kfm\.\s+StR|Priv\.-Doz\.(?:in)?\s+KommR|OStR|VetR\s+OMedR)(?:\s+[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)?(?:\s*,\s*MBA)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 15 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `OStR Tosca Knoller` — partial — pred is substring of gold: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 1  |  likely missing annotation: 0

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

## `title_prof`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Univ.-Prof.' or 'Univ.-Prof.in' or 'Prof.' followed by name. FIXED: Now captures full match including title.

**Content:**
```
(?:Univ\.-Prof\.(?:in)?|Prof\.(?:in)?)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof. Gotthard Clement` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Prof. Thassilo Averdiek` — partial — pred is substring of gold: `Hon.-Prof. Thassilo Averdiek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thassilo Averdiek`(person)
- `Alma Springel`(person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `75-059/0556`(tax_number)

</details>

---

## `judge_name_context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names of judges following 'durch den Richter' or 'durch die Richterin', including optional titles and suffixes.

**Content:**
```
(?:durch\s+den\s+Richter|durch\s+die\s+Richterin)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\.\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)?(?=,|\s+\d|\s+\n|\s+\w+stra\u00dfe|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_hr_full`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures 'HR' followed by full name, including preceding titles like 'Dipl.-Ing.', 'VetR', 'RgR', etc.

**Content:**
```
(?:Dipl\.-Ing\.|VetR|Techn\s+R\s+|RgR\s+Dipl\.\s+Kff\.|RgR|Priv\.-Doz\.|Mag\.|Dr\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Kfm\.)?\s*HR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+\w+stra\u00dfe|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_des_genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'des' in genitive contexts like 'Beschwerdesache des [Name]', extracting only the name.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+des\s+|in\s+der\s+Rechtssache\s+des\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*[A-Z]{2,4}(?:\s+\.)?)*(?=,|\s+\d|\s+\n|\s+straße|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_rgr_dipl_kff`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'RgR Dipl. Kff.' followed by name.

**Content:**
```
RgR\s+Dipl\.\s+Kff\.(?:in)?\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_mutter`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'Mutter' (Mother).

**Content:**
```
Mutter\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_after_des_beschwerdesache`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'in der Beschwerdesache des' or 'in der Rechtssache des', extracting only the name.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+des\s+|in\s+der\s+Rechtssache\s+des\s+)(?:(?:Mag\.(?:in)?|Priv\.-Doz\.(?:in)?|VetR|OMedR|OStR|Univ\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Dr\.(?:in)?|Kfm\.)\s+)?([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*[A-Z]{2,4})?(?=,|\s+\d|\s+\n|\s+\w+straße|\s+\w+weg|\s+\w+platz|\s+\w+allee|\s+\w+ring|\s+\w+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_in_list`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names in a list format, e.g., '1. Name, born...', ensuring the number is not part of the name and including suffixes.

**Content:**
```
(?:^|\n|\d+\.\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+straße|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 41 | 0 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 41 | 86 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Im Zeitraum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_14`)


Ab November  2017 war sie aufgrund ihrer schweren Krankheit nicht arbeitsfähig.“

**False Positives:**

- `Ab November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_35`)


Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abweisung)

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_10`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname wie Bf.) sind mit der Kindesmutter und  1 von 7 Seite 2 von 7

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_13`)


Ende Mai 2019 wurde meine noch minderjährige [Anmerkung: 17 ½ -jährige] Tochter aus der  Wohnung der Familie des Ziehvaters in Worcester weggewiesen.

**False Positives:**

- `Ende Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Worcester`(city)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_28`)


Im Jahr 2019 bis inkl Juli 2020 ging die Tochter des Bf in Großbritannien in die Schule und  verbrachte die Sommerferien in Wien bei ihrem Vater.

**False Positives:**

- `Im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_29`)


Ab September 2020 begann sie ein Studium in Großbritannien und verbrachte die Ferien laut  Angaben im Antrag wieder in Wien.

**False Positives:**

- `Ab September` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_30`)


Bis Mai 2019 lebte die Tochter bei ihrer Mutter in Großbritannien, danach bei dem Onkel ihres  Stiefvaters (ebenfalls in GB), der in diesem Zeitpunkt auch die Unterhaltskosten getragen hat  und ab September 2020 in einem Studentenwohnheim der University of Bristol.

**False Positives:**

- `Bis Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `University of Bristol`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_41`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.

**False Positives:**

- `1. Sachverhalt   Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `The King´s School Worcester`(organisation)
- `Maximiliane Sakschewsky, MA`(person)
- `The King's  School Worcester`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_43`)


Im Mai 2019 wurde Maximiliane Sakschewsky, MA  nach einem Streit mit dem Ziehvater aus der  gemeinsamen Wohnung gewiesen.

**False Positives:**

- `Im Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_68`)


Miss Maximiliane Sakschewsky, MA … started at the University of Bristol on 28 September 2020 and is  expected to complete her course on 9 June 2023.

**False Positives:**

- `Miss Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of Bristol`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_74`)


Im September 2020 nahm Maximiliane Sakschewsky, MA  an der University of  Bristol ein full time- Studium auf.

**False Positives:**

- `Im September` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of  Bristol`(organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_82`)


3. Rechtliche Beurteilung  3.1.

**False Positives:**

- `3. Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_84`)


Eine Person, zu deren Haushalt das Kind nicht gehört, die jedoch die  Unterhaltskosten für das Kind überwiegend trägt, hat dann Anspruch auf Familienbeihilfe,  wenn keine andere Person nach dem ersten Satz anspruchsberechtigt ist.

**False Positives:**

- `Eine Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_60`)


Im Dezember 2021 langte dann noch eine Bestätigung der JKU  Linz ein, die die beiden Studien „grundsätzlich gleichwertig“ ansah.

**False Positives:**

- `Im Dezember` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU  Linz`(organisation)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_110`)


3. Rechtliche Beurteilung  3.1. Rechtslage  Gemäß § 2 Abs. 1 lit. b Familienlastenausgleichsgesetz 1967 idF. BGBl. I Nr. 24/2019 und Nr.  28/2020 haben Personen Anspruch auf Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `3. Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_112`)


Bei Kindern, die eine in § 3 des Studienförderungsgesetzes 1992, BGBl.Nr. 305, genannte  Einrichtung besuchen, ist eine Berufsausbildung nur dann anzunehmen, wenn sie die  vorgesehene Studienzeit pro Studienabschnitt um nicht mehr als ein Semester oder die  vorgesehene Ausbildungszeit um nicht mehr als ein Ausbildungsjahr überschreiten.

**False Positives:**

- `Bei Kindern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_129`)


Kein Studienwechsel (und damit außerhalb des Anwendungsbereiches des § 17 StudFG) ist der  Wechsel der Studieneinrichtung/des Studienortes bei gleichbleibender Studienrichtung.

**False Positives:**

- `Kein Studienwechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_30`)


Ein Rechtfertigungsgrund, also eine Norm, die das tatbestandsmäßige Verhalten  ausnahmsweise erlaube bzw. welche die Strafbarkeit aufheben würde, liege im  gegenständlichen Fall nicht vor.

**False Positives:**

- `Ein Rechtfertigungsgrund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_42`)


Die Magistratsabteilung 67 legte die Beschwerde samt dem bezughabenden Verwaltungsakt  dem Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 1. Oktober 2025).

**False Positives:**

- `Die Magistratsabteilung` — positional overlap with gold: `Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistratsabteilung 67`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_49`)


Der Abstellort, der Beanstandungszeitpunkt und die Lenkereigenschaft des Bf. wurden vom Bf.  im gegenständlichen Fall nicht bestritten.

**False Positives:**

- `Der Abstellort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_22`)


Im Jahr 2024 wurde beim Bf von der Abgabenbehörde eine Außenprüfung  2 von 7 Seite 3 von 7

**False Positives:**

- `Im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_54`)


Rechtliche Beurteilung  2.1. Zu Spruchpunkt I. (Abweisung)  § 205 BAO normiert auszugsweise:  Gemäß § 205 Abs. 1 BAO sind Differenzbeträge an Einkommensteuer und Körperschaftsteuer,  die sich aus Abgabenbescheiden unter Außerachtlassung von Anzahlungen (Abs. 3), nach  Gegenüberstellung mit Vorauszahlungen oder mit der bisher festgesetzt gewesenen Abgabe  ergeben, für den Zeitraum ab 1. Oktober des dem Jahr des Entstehens des Abgabenanspruchs  folgenden Jahres bis zum Zeitpunkt der Bekanntgabe dieser Bescheide zu verzinsen  (Anspruchszinsen).

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_11`)


Rechtliche Beurteilung (Spruchpunkt I.)  Gemäß § 256 Abs 3 BAO ist eine Beschwerde mit Beschwerdevorentscheidung (§ 262) oder mit  Beschluss (§ 278) als gegenstandslos zu erklären, wenn sie zurückgenommen wird.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_74`)


Zur  Frage, wie lange ein Zuwarten auf einen Operationstermin ohne erhebliche medizinische  Nachteile möglich gewesen wäre, wird allgemein ausgeführt, dass ein Abwarten konkreter  motorischer Schwächen, um dann erst die Operation vorzunehmen, sicherlich nicht der  optimale Verlauf wäre und zudem (wiederum allgemein) angemerkt, dass eine zu späte  operative Versorgung zu bleibenden Wurzelschäden und motorischen Schwächen führen kann.

**False Positives:**

- `Zur  Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_79`)


3. Rechtliche Beurteilung  3.1.

**False Positives:**

- `3. Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_102`)


Bloße Wünsche, Befürchtungen oder Standesrücksichten der Betroffenen reichen nicht, um die  Zwangsläufigkeit zu rechtfertigen.

**False Positives:**

- `Bloße Wünsche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_104`)


Auch Aufwendungen, die nicht von der  gesetzlichen Krankenversicherung getragen werden, können dem Steuerpflichtigen  zwangsläufig erwachsen, wenn sie aus triftigen Gründen medizinisch geboten sind (vgl. VwGH  11.2.2016, 2013/13/0064 mwN).

**False Positives:**

- `Auch Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_27`)


Im Fall  2 von 15 Seite 3 von 15

**False Positives:**

- `Im Fall` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_40`)


Mit Datum 11.1.2016 erging der nunmehr angefochtenen Haftungsbescheid.

**False Positives:**

- `Mit Datum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_45`)


Die Lohnabgaben 05/2012  bis 03/2013 sei gemeldet worden, die Lohnabgaben 2011 sei mittels Bescheides festgesetzt  worden.

**False Positives:**

- `Die Lohnabgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_58`)


Der Zeitpunkt, für den zu beurteilen sei, ob der Primärschuldnerin die für die  Abgabenentrichtung erforderlichen Mittel zur Verfügung standen, bestimme sich danach,  wann die Abgaben bei Beachtung der abgabenrechtlichen Vorschriften zu entrichten gewesen  wären (VwGH 27.4.2000, 98/15/0003;

**False Positives:**

- `Der Zeitpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_60`)


Bei Selbstbemessungsabgaben (wie der Lohnsteuer und der Umsatzsteuer) sei maßgeblich,  wann die Abgaben bei ordnungsgemäßer Selbstberechnung abzuführen gewesen wären.

**False Positives:**

- `Bei Selbstbemessungsabgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_88`)


Im Jahr 2011 seien € 2.161.230,45, im Jahr 2012 wurden € 1.118.380,19 und im Jahr 2013  wurden € 593.447,25 an Umsätzen erzielt worden.

**False Positives:**

- `Im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

**False Positives:**

- `Zum Hinweis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_165`)


Rechtliche Beurteilung  3.1.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_176`)


Die  Lohnabgaben 05/2012 bis 03/2013 wurden ebenso gemeldet, die Lohnabgaben 2011 sind  mittels Bescheides festgesetzt worden.

**False Positives:**

- `Die  Lohnabgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_34`)


3. Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abänderung)  1.

**False Positives:**

- `3. Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_49`)


3. Die Gründe, die zum Zahlungsverzug geführt haben, sind grundsätzlich unbeachtlich.

**False Positives:**

- `3. Die Gründe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `name_after_als`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'als' (as) in contexts like 'als Bf bezeichnet'.

**Content:**
```
als\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+straße|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_osr_ddr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'OSR DDr.' or 'DDr.' followed by name.

**Content:**
```
(?:OSR\s+)?DDr\.\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_bakk_art`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with academic degree 'Bakk. art.' or 'Bakk. techn.' or 'Bakk. iur.' following a name, ensuring the full name and suffix are captured.

**Content:**
```
(?:^|\s|,|\.)\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)\s*,\s*Bakk\.\s*(?:iur|art|techn)\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 14 | 0 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 14 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Kind Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_15`)


Der Beschwerde beigelegt war eine Betätigung eines Allgemeinmediziners vom 27.11.2019,  wonach Stella Marschalk, Bakk. techn.  auf Grund einer schweren Erkrankung (Sensibilitätsdefizit untere  Extremitäten DD: Guillain-Barré-Syndrom) von Oktober 2017 bis Ende Juni 2018 nicht  arbeitsfähig gewesen sei.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Frau  Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`
- `Frau Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_26`)


Dem Vorlageantrag beigelegt war ein Schreiben der Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith, in dem bestätigt wurde, dass Stella Marschalk, Bakk. techn.  die Schule in  der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_28`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die BF bezog im streitgegenständlichen Zeitraum Familienbeihilfe und Kinderabsetzbeträge für  ihre Tochter Stella Marschalk, Bakk. techn. (geboren im September 1998).

**False Positives:**

- `Tochter Stella Marschalk` — positional overlap with gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)
- `September 1998`(date)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Jennifer Papenhagen` — partial — pred is substring of gold: `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

</details>

---

## `name_after_genitive_der`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'der' in genitive contexts, excluding organizations and common false positives.

**Content:**
```
der\s+(?!Beschwerdesache|Rechtssache|Verfahren|Sache|Antrag|Bescheid|Urteil|Entscheidung|Klage|Rechtsmittel|Einspruch|Widerspruch|Anzeige|Strafanzeige|Verfahrenshilfe|Verfahrenshilfekosten|Verfahrenskostenhilfe|Verfahrenskosten|Verfahrensgegenstand|Verfahrensbeteiligte|Verfahrensbeteiligter|Verfahrensbeistand|Verfahrensbeist\u00e4ndin|Finanzamt|Finanzamtes|Stadt|Magistrat|Magistratsabteilung|Beh\u00f6rde|Bundesfinanzgericht|Gericht|Wirtschaftspr\u00fcfung|Steuerberatung|GmbH|AG|KG|PartG|Rechtsanw\u00e4lte|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|Wien|Nr|Gl\u00fccksspielabgabe|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|Rechtsanw\u00e4lte|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 8 | 58 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_61`)


Am 23. Oktober 2020 überwies der Bf. auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN  GB…1084 € 200,00 mit dem Verwendungszweck: Unterstützung, am 4. November 2020  € 500,00 am 25. und 30. November jeweils € 200,00.

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (JKU Linz)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Johannes Kepler Universität Linz (JKU Linz)`(organisation)
- `JKU Linz`(organisation)
- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_26`)


6. Die Bf. antwortete mit einer am 13.12.2021 bei der belangten Behörde eingelangter Eingabe  und legte ein E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  3 von 16 Seite 4 von 16

**False Positives:**

- `Johannes Kepler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)
- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz (`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (JKU)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU)`(organisation)
- `Johannes Kepler Universität Linz (JKU)`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_7`)


von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am  2. Mai 2025 um 11:09 Uhr in 1100 Wien, Gasse, beanstandet, da ein gültiger Parkschein fehlte.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `1100 Wien`(address)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_6`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt gegenüber dem Beschwerdeführer (Bf.)  Normverbrauchsabgabe (NoVA) in Höhe von 11.785,71 Euro und Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro für ein Kraftfahrzeug der Marke  Porsche Cayenne Diesel Platinum Edition (in der Folge: Kfz.) fest.

**False Positives:**

- `Marke  Porsche Cayenne Diesel Platinum Edition` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `name_after_nominative_die_der`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'Die' or 'Der' in nominative contexts, excluding role words like 'Beschwerdeführer'.

**Content:**
```
(?:^|\s)(?:Die|Der|Die\s+|Der\s+)(?!Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Partei|Parteien|Beh\u00f6rde|Gericht|Magistrat|Finanzamt|Bundesfinanzgericht|Sachverhalt|Verfahren|Bescheid|Urteil|Entscheidung|Antrag|Antragsteller|Klage|Rechtsmittel|Einspruch|Widerspruch|Anzeige|Strafanzeige|Verfahrenshilfe|Verfahrenshilfekosten|Verfahrenskostenhilfe|Verfahrenskosten|Verfahrensgegenstand|Verfahrensbeteiligte|Verfahrensbeteiligter|Verfahrensbeistand|Verfahrensbeist\u00e4ndin|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s+war|\s+ist|\s+hat|\s+konnte|\s+wurde|\s+\.|\s+\n|\s+\()
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_rgr_omedr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with titles like 'RgR OMedR' followed by name.

**Content:**
```
(?:RgR\s+OMedR|OMedR\s+RgR)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_with_suffix_general`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
DELETED: Too broad, matches streets, cities, and organizations.

**Content:**
```

```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_dipl_ing`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'Dipl.-Ing.' followed by name.

**Content:**
```
Dipl\.-Ing\.(?:in)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_dr_in_univ_prof`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with combined titles 'Dr.in Univ.-Prof.in' or 'Dr.in Prof.' or 'Univ.-Prof.in' followed by name. Stops at comma.

**Content:**
```
(?:Dr\.in\s+)?(?:Univ\.-Prof\.(?:in)?|Prof\.(?:in)?)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_phd`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with title 'PhD' followed by name.

**Content:**
```
PhD\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_ddr_complex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with compound titles like 'DDr.', 'Univ.-Prof.in', 'Hon.-Prof.in' followed by name and optional suffixes.

**Content:**
```
(?:DDr\.|Univ\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Dr\.\s+Dr\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)?(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `name_at_start_of_sentence_tightened_v2`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names at start of sentence, excluding common non-name words, organizations, and month names. Strictly enforces word boundaries.

**Content:**
```
(?:^|\.)\s*((?!Die\s+|Verfahrensgang|Entscheidungsgr\u00fcnde|Begr\u00fcndung|Beschluss|Hinweis|Feststellung|Erw\u00e4gung|Anmerkung|Antrag|Antragsteller|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung|GmbH|AG|KG|PartG|Rechtsanw\u00e4lte|Textil|Gesellschaft|Treuhand|Partner|OG|Wirtschafts|Steuer|Beratung|Treuhand|Partei|Parteien|Beschwerdef\u00fchrer|Beschwerdef\u00fchrerin|Bf|Bf\.|Bisheriger|Die\s+Beschwerdef\u00fchrerin|Die\s+Parteien|Die\s+Beschwerde|Die\s+Parteien|Im\s+Mietvertrag|Das\s+Bundesfinanzgericht|der\s+Parteien|FA\s+|Finanzamt|Spruchsenates|Finanzamtes|Magistrat|Magistratsabteilung|Universit\u00e4t|Sachverhalt|Stadt|Finanzamtes|Januar|Februar|M\u00e4rz|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|J\u00e4nner|P\u00f6lten|Einhebung|Kraftfahrzeugsteuerbescheide|Zahl|Als\s+Begr\u00fcndung)[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)?)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 97 | 0 | 97 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 97 | 87 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_4`)


Am 30.09.2019 langte beim Finanzamt die Antwort der Beschwerdeführerin (in der Folge BF)  auf ein Überprüfungsschreiben des Anspruches auf Familienbeihilfe ein.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_11`)


Seit 2.7.2018 absolviert sie  eine Lehre zur Steuerassistentin.

**False Positives:**

- `Seit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Im Zeitraum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_14`)


Ab November  2017 war sie aufgrund ihrer schweren Krankheit nicht arbeitsfähig.“

**False Positives:**

- `Ab November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_27`)


7. Am 12.10.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor und beantragte die Abweisung, da die Ausbildung am 04.10.2017 beendet  worden sei.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_35`)


Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abweisung)

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_58`)


Linz, am 2. Dezember 2020

**False Positives:**

- `Linz` — type mismatch — same span as gold: `Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Linz`(city)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_10`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname wie Bf.) sind mit der Kindesmutter und  1 von 7 Seite 2 von 7

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_13`)


Ende Mai 2019 wurde meine noch minderjährige [Anmerkung: 17 ½ -jährige] Tochter aus der  Wohnung der Familie des Ziehvaters in Worcester weggewiesen.

**False Positives:**

- `Ende Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Worcester`(city)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_28`)


Im Jahr 2019 bis inkl Juli 2020 ging die Tochter des Bf in Großbritannien in die Schule und  verbrachte die Sommerferien in Wien bei ihrem Vater.

**False Positives:**

- `Im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_29`)


Ab September 2020 begann sie ein Studium in Großbritannien und verbrachte die Ferien laut  Angaben im Antrag wieder in Wien.

**False Positives:**

- `Ab September` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_30`)


Bis Mai 2019 lebte die Tochter bei ihrer Mutter in Großbritannien, danach bei dem Onkel ihres  Stiefvaters (ebenfalls in GB), der in diesem Zeitpunkt auch die Unterhaltskosten getragen hat  und ab September 2020 in einem Studentenwohnheim der University of Bristol.

**False Positives:**

- `Bis Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `University of Bristol`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Meine Töchter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_43`)


Im Mai 2019 wurde Maximiliane Sakschewsky, MA  nach einem Streit mit dem Ziehvater aus der  gemeinsamen Wohnung gewiesen.

**False Positives:**

- `Im Mai` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_53`)


Am 31. Mai 2019 und in den folgenden Monaten, bis 3. August 2020, überwies der Bf. an die  Kindesmutter der (gemeinsamen) Töchter Maximiliane Sakschewsky, MA  und E. auf das Konto in  Großbritannien IBAN GB… 8171 € 1.000,00 (Kontoauszüge).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_54`)


Am 18. August 2019 wurde der Tochter des Bf. die Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" gemäß §6 der Führerscheingesetz- Durchführungsverordnung von 1997, in der Dauer von sechs Stunden bestätigt.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_59`)


Am 11. August 2020 überwies der Bf. auf das Konto in Großbritannien IBAN GB…1114 € 500,00  E… (Nachname wie Bf.), am 14. September 2020 € 140,00.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_61`)


Am 23. Oktober 2020 überwies der Bf. auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN  GB…1084 € 200,00 mit dem Verwendungszweck: Unterstützung, am 4. November 2020  € 500,00 am 25. und 30. November jeweils € 200,00.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_64`)


Am 19. Dezember 2020 überwies der Bf. auf das Konto K. H., IBAN GB…1233 € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_65`)


Am 13. Jänner 2021 ersuchte das Finanzamt den Bf. um den „Nachweis der Überweisungen der  Alimente an ihre Tochter bzw. an die Kindesmutter ab Juni 2019 lfd.“.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_66`)


Am 11. Dezember 2020 bestätigte die University of Bristol, that Miss Maximiliane Sakschewsky, MA (Tochter  des Bf.) student no.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `University of Bristol`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_68`)


Miss Maximiliane Sakschewsky, MA … started at the University of Bristol on 28 September 2020 and is  expected to complete her course on 9 June 2023.

**False Positives:**

- `Miss Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of Bristol`(organisation)

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_69`)


2. Beweiswürdigung  1.

**False Positives:**

- `Beweiswürdigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_70`)


Die Tochter des Bf. Maximiliane Sakschewsky, MA  war im beschwerdegegenständlichen Zeitraum nicht  zugehörig zum Haushalt des Bf.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_74`)


Im September 2020 nahm Maximiliane Sakschewsky, MA  an der University of  Bristol ein full time- Studium auf.

**False Positives:**

- `Im September` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of  Bristol`(organisation)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_82`)


3. Rechtliche Beurteilung  3.1.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_84`)


Eine Person, zu deren Haushalt das Kind nicht gehört, die jedoch die  Unterhaltskosten für das Kind überwiegend trägt, hat dann Anspruch auf Familienbeihilfe,  wenn keine andere Person nach dem ersten Satz anspruchsberechtigt ist.

**False Positives:**

- `Eine Person` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_92`)


Wien, am 17. August 2021

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_56`)


Am 09.08.2021 langte dann die Vorhaltsbeantwortung ein mit den  Studienerfolgsnachweisen der beiden Studien aus der eine Anrechnung von 24 ECTS erkennbar  war.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_59`)


Am 07.10.2021 langte dann eine Beschwerde ein, mit der  Begründung, dass es sich nicht um einen schädlichen Studienwechsel handle, sondern nur um  einen Wechsel des Studienortes.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_60`)


Im Dezember 2021 langte dann noch eine Bestätigung der JKU  Linz ein, die die beiden Studien „grundsätzlich gleichwertig“ ansah.

**False Positives:**

- `Im Dezember` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU  Linz`(organisation)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_63`)


Am 12.04.2022 reichte die  Beschwerdeführerin den Vorlageantrag ein, damit die Beschwerde dem Bundesfinanzgericht  zur Entscheidung vorgelegt wird und der Bescheid ersatzlos aufgehoben wird.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

**False Positives:**

- `Studienschwerpunkte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/`(website)
- `WU`(organisation)
- `JKU`(organisation)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_110`)


3. Rechtliche Beurteilung  3.1. Rechtslage  Gemäß § 2 Abs. 1 lit. b Familienlastenausgleichsgesetz 1967 idF. BGBl. I Nr. 24/2019 und Nr.  28/2020 haben Personen Anspruch auf Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_112`)


Bei Kindern, die eine in § 3 des Studienförderungsgesetzes 1992, BGBl.Nr. 305, genannte  Einrichtung besuchen, ist eine Berufsausbildung nur dann anzunehmen, wenn sie die  vorgesehene Studienzeit pro Studienabschnitt um nicht mehr als ein Semester oder die  vorgesehene Ausbildungszeit um nicht mehr als ein Ausbildungsjahr überschreiten.

**False Positives:**

- `Bei Kindern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_129`)


Kein Studienwechsel (und damit außerhalb des Anwendungsbereiches des § 17 StudFG) ist der  Wechsel der Studieneinrichtung/des Studienortes bei gleichbleibender Studienrichtung.

**False Positives:**

- `Kein Studienwechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_155`)


Studium, welches ebenfalls an mehreren Universitätsstandorten in Österreich angeboten wird,  wobei sich auch hier die konkreten Studienpläne bzw. –inhalte im Detail regelmäßig  unterscheiden und dennoch zum selben, als gleichartig anerkannten Ausbildungsergebnis  führen sowie jeweils Voraussetzung für die drei juristischen „Kernberufe“ Richter, Anwalt und  Notar sind.

**False Positives:**

- `Studium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_176`)


Linz, am 29. November 2022

**False Positives:**

- `Linz` — type mismatch — same span as gold: `Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Linz`(city)

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_22`)


Wien, am 29. Oktober 2025

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Bezirk` — partial — pred is substring of gold: `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_53`)


Feldkirch, am 30. September 2025

**False Positives:**

- `Feldkirch` — type mismatch — same span as gold: `Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Feldkirch`(city)

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_24`)


Abgabepflichtige, die ein mehrspuriges Fahrzeug in einer Kurzparkzone abstellen, hätten dafür  zu sorgen, dass es während der Dauer seiner Abstellung mit einem richtig angebrachten und  richtig entwerteten Parkschein gekennzeichnet oder ein elektronischer Parkschein aktiviert sei  (§§ 3 Abs. 1 und 7 Abs. 1 der Kontrolleinrichtungenverordnung, Amtsblatt der Stadt Wien  Nr. 33/2008).

**False Positives:**

- `Abgabepflichtige` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien`(city)

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_30`)


Ein Rechtfertigungsgrund, also eine Norm, die das tatbestandsmäßige Verhalten  ausnahmsweise erlaube bzw. welche die Strafbarkeit aufheben würde, liege im  gegenständlichen Fall nicht vor.

**False Positives:**

- `Ein Rechtfertigungsgrund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_49`)


Der Abstellort, der Beanstandungszeitpunkt und die Lenkereigenschaft des Bf. wurden vom Bf.  im gegenständlichen Fall nicht bestritten.

**False Positives:**

- `Der Abstellort` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_85`)


Wien, am 20. Oktober 2025  7 von 7

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_36`)


Nur, weil es insbesondere in den letzten Jahren der  selbständigen Tätigkeit unseres Mandanten zu dem einen oder anderen Verlustjahr gekommen  ist - dies auch bedingt durch die Tatsache, dass junge Konkurrenz nachwuchs und unser  Mandant dadurch nicht mehr so einfach an Aufträge kam, weiters die Gagenhöhe im Bereich  der Jazzmusik laufend gesunken ist und viele Veranstalter vermehrt auf modischere Diskjockeys  zurückgegriffen haben - kann nicht ohne weitere Prüfung des Gesamterfolges einer Tätigkeit  von Liebhaberei ausgegangen werden.

**False Positives:**

- `Nur` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_65`)


Am 22.02.2017 brachte der steuerliche Vertreter des Bf. einen Antrag auf Vorlage der  Beschwerde an das Bundesfinanzgericht ein.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_89`)


Ab 1982 war der Bf. als 1. Perkussionist des Orchesters nichtselbständig beschäftigt.

**False Positives:**

- `Ab` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_105`)


Verhältnis der Verluste zu den Gewinnen oder Überschüssen,  3. Ursachen, auf Grund deren im Gegensatz zu vergleichbaren Betrieben, Tätigkeiten oder  Rechtsverhältnissen kein Gewinn oder Überschuß erzielt wird,  4. marktgerechtes Verhalten im Hinblick auf angebotene Leistungen,  5. marktgerechtes Verhalten im Hinblick auf die Preisgestaltung,  6.

**False Positives:**

- `Ursachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_109`)


Nach  9 von 14 Seite 10 von 14

**False Positives:**

- `Nach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_143`)


Gesamtgewinn (§ 3 Abs. 1 LVO) ist das Gesamtergebnis von der Begründung der Tätigkeit bis  zu deren Beendigung.

**False Positives:**

- `Gesamtgewinn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_164`)


Wien, am 27. August 2025

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_22`)


Im Jahr 2024 wurde beim Bf von der Abgabenbehörde eine Außenprüfung  2 von 7 Seite 3 von 7

**False Positives:**

- `Im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_54`)


Rechtliche Beurteilung  2.1. Zu Spruchpunkt I. (Abweisung)  § 205 BAO normiert auszugsweise:  Gemäß § 205 Abs. 1 BAO sind Differenzbeträge an Einkommensteuer und Körperschaftsteuer,  die sich aus Abgabenbescheiden unter Außerachtlassung von Anzahlungen (Abs. 3), nach  Gegenüberstellung mit Vorauszahlungen oder mit der bisher festgesetzt gewesenen Abgabe  ergeben, für den Zeitraum ab 1. Oktober des dem Jahr des Entstehens des Abgabenanspruchs  folgenden Jahres bis zum Zeitpunkt der Bekanntgabe dieser Bescheide zu verzinsen  (Anspruchszinsen).

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_56`)


Anspruchszinsen, die den Betrag von 50 Euro nicht erreichen, sind nicht festzusetzen.

**False Positives:**

- `Anspruchszinsen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_96`)


Linz, am 5. Dezember 2025

**False Positives:**

- `Linz` — type mismatch — same span as gold: `Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Linz`(city)

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_11`)


Rechtliche Beurteilung (Spruchpunkt I.)  Gemäß § 256 Abs 3 BAO ist eine Beschwerde mit Beschwerdevorentscheidung (§ 262) oder mit  Beschluss (§ 278) als gegenstandslos zu erklären, wenn sie zurückgenommen wird.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_19`)


Wien, am 19. November 2025

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Michael` — partial — pred is substring of gold: `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Oleg Dell`(person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH`(organisation)
- `Hegelgasse 8, 1010 Wien`(address)
- `Finanzamtes Österreich`(organisation)
- `80-738/9953`(tax_number)

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_5`)


Am 31. Oktober 2023 erging ein Ergänzungsersuchen an den Bf. betreffend die geltend  gemachten Behandlungskosten in Höhe von Euro 10.299,13.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_7`)


Am 30. Dezember 2023 gab der Bf. bekannt, dass die Kosten für die Operation seiner Gattin  angefallen seien.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_17`)


Am 13. Februar 2024 erging ein weiteres Ergänzungsersuchen.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_26`)


Am 13. Juni 2024 legte die belangte Behörde die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_31`)


Am 1. Oktober 2025 fand die beantragte mündliche Verhandlung vor dem Bundesfinanzgericht  statt, in der insbesondere das Vorliegen bzw. Nichtvorliegen von triftigen medizinischen  Gründen diskutiert wurde.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_33`)


Am 3. November 2025 reichte der Bf. die beiden ergänzenden Befundberichte nach.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_34`)


Am 6. November 2025 fand die fortgesetzte mündliche Verhandlung statt.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_64`)


Dieser  4 von 8 Seite 5 von 8

**False Positives:**

- `Dieser` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_74`)


Zur  Frage, wie lange ein Zuwarten auf einen Operationstermin ohne erhebliche medizinische  Nachteile möglich gewesen wäre, wird allgemein ausgeführt, dass ein Abwarten konkreter  motorischer Schwächen, um dann erst die Operation vorzunehmen, sicherlich nicht der  optimale Verlauf wäre und zudem (wiederum allgemein) angemerkt, dass eine zu späte  operative Versorgung zu bleibenden Wurzelschäden und motorischen Schwächen führen kann.

**False Positives:**

- `Zur  Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_79`)


3. Rechtliche Beurteilung  3.1.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_102`)


Bloße Wünsche, Befürchtungen oder Standesrücksichten der Betroffenen reichen nicht, um die  Zwangsläufigkeit zu rechtfertigen.

**False Positives:**

- `Bloße Wünsche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_104`)


Auch Aufwendungen, die nicht von der  gesetzlichen Krankenversicherung getragen werden, können dem Steuerpflichtigen  zwangsläufig erwachsen, wenn sie aus triftigen Gründen medizinisch geboten sind (vgl. VwGH  11.2.2016, 2013/13/0064 mwN).

**False Positives:**

- `Auch Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_125`)


Wien, am 17. November 2025  8 von 8

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 77** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_27`)


Im Fall  2 von 15 Seite 3 von 15

**False Positives:**

- `Im Fall` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_32`)


Am 30.11.2015 langte eine Vorhaltsbeantwortung des (damaligen) steuerlichen Vertreters ein,  in der vorgebracht wurde, dass hinsichtlich der Inanspruchnahme zur Haftung gem. § 9 iVm  § 80 BAO ein Ermessensspielraum des Finanzamtes bestehe.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_34`)


Seit 1.11.2015 sei Herr  Dieter Leufkes  wieder angestellt und beziehe ein Nettogehalt von ca. 1.400 €/Monat Von diesem  Einkommen könne ein Betrag von ca. 356 €/Monat gepfändet werden, jedoch sei dieser Betrag  bereits in Pfändung.

**False Positives:**

- `Seit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dieter Leufkes`(person)

**Example 80** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_40`)


Mit Datum 11.1.2016 erging der nunmehr angefochtenen Haftungsbescheid.

**False Positives:**

- `Mit Datum` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_58`)


Der Zeitpunkt, für den zu beurteilen sei, ob der Primärschuldnerin die für die  Abgabenentrichtung erforderlichen Mittel zur Verfügung standen, bestimme sich danach,  wann die Abgaben bei Beachtung der abgabenrechtlichen Vorschriften zu entrichten gewesen  wären (VwGH 27.4.2000, 98/15/0003;

**False Positives:**

- `Der Zeitpunkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_60`)


Bei Selbstbemessungsabgaben (wie der Lohnsteuer und der Umsatzsteuer) sei maßgeblich,  wann die Abgaben bei ordnungsgemäßer Selbstberechnung abzuführen gewesen wären.

**False Positives:**

- `Bei Selbstbemessungsabgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_88`)


Im Jahr 2011 seien € 2.161.230,45, im Jahr 2012 wurden € 1.118.380,19 und im Jahr 2013  wurden € 593.447,25 an Umsätzen erzielt worden.

**False Positives:**

- `Im Jahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_129`)


Am 22.3.2016 langte eine Beschwerde, eingebracht vom damaligen steuerlichen Vertreter des  Bf., gegen den erlassenen Haftungsbescheid ein.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_140`)


Am 4.4.2016 erging eine Beschwerdevorentscheidung (BVE), mit der die Beschwerde  abgewiesen wurde.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

**False Positives:**

- `Zum Hinweis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 87** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_165`)


Rechtliche Beurteilung  3.1.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_227`)


Graz, am 3. Dezember 2025

**False Positives:**

- `Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_22`)


5. Am 3.4.2025 stellte der Bf. durch seine steuerliche Vertretung den Antrag auf Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 90** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_23`)


6. Am 21.5.2025 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht vor und  beantragte, die Beschwerde als unbegründet abzuweisen.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 91** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_29`)


Am 4.11.2024 wurde der Ablauf der Bewilligung  dieser Aussetzung „infolge Beschwerdeerledigung“ verfügt.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_31`)


5. Am 9.1.2025 erfolgte die Festsetzung der Säumniszuschläge in Höhe von 235,71 Euro für die  Normverbrauchsabgabe und in Höhe von 265,92 Euro für die Umsatzsteuer.

**False Positives:**

- `Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_32`)


2. Beweiswürdigung  1.

**False Positives:**

- `Beweiswürdigung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_34`)


3. Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abänderung)  1.

**False Positives:**

- `Rechtliche Beurteilung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_65`)


Haller,  Normverbrauchsabgabegesetz2, § 11 Tz 10).

**False Positives:**

- `Haller` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_108`)


Feldkirch, am 12. Dezember 2025

**False Positives:**

- `Feldkirch` — type mismatch — same span as gold: `Feldkirch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Feldkirch`(city)

</details>

---

## `name_after_fuer_das_kind`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following 'für das Kind' or 'für seine Kinder' (singular and possessive), common in family benefit cases.

**Content:**
```
(?:für\s+(?:das\s+Kind|seine\s+Kinder)\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `title_phd_ing`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with the compound title 'PhD Ing.' followed by name.

**Content:**
```
PhD\s+Ing\.(?:in)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_prof_dr`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures persons with 'Prof. Dr.' or 'Dr. Prof.' followed by name.

**Content:**
```
(?:Prof\.\s+Dr\.|Dr\.\s+Prof\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_ing_with_suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures 'Ing.' or 'Ing. Mag.' followed by name, handling suffixes like ', BEd' and excluding orgs.

**Content:**
```
(?:Ing\.(?:in)?(?:\s+Mag\.(?:in)?)?)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)(?:\s*,\s*(?:BA|LLB|BEd|Bakk\.(?:iur|art|techn)|MBA|MSc|LLM|Dr\.|Mag\.|OStR|Univ\.-Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|Dr\.\s+Dr\.|Dr\.\s+Priv\.-Doz\.|Dr\.\s+Mag\.|Mag\.\s+Dr\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.|Dr\.\s+Dr\.\s+Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Priv\.-Doz\.(?:in)?\s+Hon\.-Prof\.(?:in)?|\s+Mag\.)?Hon\.-Prof\.(?:in)?|Hon\.-Prof\.(?:in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:\s+Dr\.)?|Dr\.)?)*(?=,|\s+\d|\s+\n|\s+stra\u00dfe|\s+weg|\s+platz|\s+allee|\s+ring|\s+boulevard|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `title_prof_dr_in`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures 'Dr.in Univ.-Prof.in' or similar complex female academic titles.

**Content:**
```
(?:Dr\.in\s+Univ\.-Prof\.in|Univ\.-Prof\.in\s+Dr\.in|Dr\.\s+Univ\.-Prof\.in|Univ\.-Prof\.in\s+Dr\.)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)+)
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

