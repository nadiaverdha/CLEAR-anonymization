# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (manual_findok)

Generated on: 2026-05-20T09:37:59.609686

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-20_v4/config.yaml 
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
| Max samples in prompt | 200 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | True |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 3 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 100 |
| Refine per batch | 0 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

**Transfer Learning**

| Property | Value |
|---|---|
| Seeded From | findok |
| Seed Rule Count | 40 |
| New Rules Added | 2 |
| Continuation | synthesize_and_refine |
| Phase1 Train Sentences | 4080 |
| Phase1 Eval Sentences | 927 |
| Transfer Train Sentences | 188 |
| Transfer Eval Sentences | 41 |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 84.0% |
| True Positives | 20 |
| False Positives | 178 |
| False Negatives | 70 |
| Total Gold Entities | 90 |
| Micro Precision | 10.1% |
| Micro Recall | 22.2% |
| Micro F1 | 13.9% |
| Macro F1 | 13.9% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Legal_Context_Name` | 18.2% | 100.0% | 10.0% | 9 | 9 | 0 |
| `Party_Name_In_Context` | 18.2% | 100.0% | 10.0% | 9 | 9 | 0 |
| `Name_After_Genitive_Context` | 10.5% | 100.0% | 5.6% | 5 | 5 | 0 |
| `Name_After_Beschwerdesache` | 10.5% | 100.0% | 5.6% | 5 | 5 | 0 |
| `PreNominal_Title_Name` | 20.4% | 61.1% | 12.2% | 18 | 11 | 7 |
| `Name_After_Beschwerdesache_Simple` | 8.1% | 44.4% | 4.4% | 9 | 4 | 5 |
| `Name_After_Gender_Title` | 8.0% | 40.0% | 4.4% | 10 | 4 | 6 |
| `Name_After_Preposition_For` | 1.3% | 1.6% | 1.1% | 64 | 1 | 63 |
| `Judge_Richter` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Complainant_Beschwerdesache` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frau_Herr_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Person_After_Verb` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Techn_R_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `OSR_Title_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dative_Bei_Der_Name` | 0.0% | 0.0% | 0.0% | 21 | 0 | 21 |
| `Name_After_Comma_With_Address` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name_After_Verb` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name_After_Haftung` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `VetR_Title_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `StR_Title_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `HR_Title_Name` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Hon_Prof_in_Title_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gegen_Name` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Name_At_Start_Of_Text` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name_At_Start_Of_Text_Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Party_Name_In_Context_Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Legal_Context_Name_Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name_After_Comma_Flexible` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Bei_Name_Context` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Techn_R_Suffix_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gegen_Name_Full` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Name_After_Verb_Enhanced` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Priv_Doz_in_Title_Name` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Name_After_Antrag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag_a_Title_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name_With_Suffix_Generic` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name_After_Comma_Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name_After_Address_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name_After_Preposition_Generic` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `Name_After_Vertraten_Durch` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Name_In_Parentheses` | 0.0% | 0.0% | 0.0% | 69 | 0 | 69 |
| `Name_After_Gegen_Herr_Frau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Legal_Context_Name`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Description:**
Captures person names in 'in der Beschwerdesache' context. Handles names followed by comma or address.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Rechtsmittelsache|Angelegenheit)(?:\s+des)?\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?:,|\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+\d+)
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

## `Party_Name_In_Context`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Description:**
Captures person names in 'in der Beschwerdesache' context. Uses capture group to extract only the name, excluding the context prefix.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Rechtsmittelsache|Angelegenheit)(?:\s+des)?\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*,
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

## `PreNominal_Title_Name`

**F1:** 0.204 | **Precision:** 0.611 | **Recall:** 0.122  

**Format:** `regex`  
**Description:**
Captures person names preceded by complex legal/academic titles, now including suffixes like , MA, , BEd, , LLB.

**Content:**
```
\b(?:(?:Dr\.|Mag\.|Mag\.a|Mag\.Dr\.|DDr\.|Ing\.|LL\.M|BEd|M\.B\.L|MBA|MSc|Bakk\.(?:rer\.(?:nat|phil|iur|art|techn))?|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|OStR|StR|RgR|Prof\.)\s+)*(?:Dr\.|Mag\.|Mag\.a|Mag\.Dr\.|DDr\.|Ing\.|LL\.M|BEd|M\.B\.L|MBA|MSc|Bakk\.(?:rer\.(?:nat|phil|iur|art|techn))?|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|OStR|StR|RgR|Prof\.)\s*(?:in\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BEd|LLB|LL\.M|M\.B\.L|MBA|MSc|Bakk\.(?:rer\.(?:nat|phil|iur|art|techn))?|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Mag\.(?:a)?|Dr\.(?:in)?|OStR|StR|RgR|Priv\.-Doz\.|Univ\.-Prof\.|Prof\.|Ing\.|Hon\.-Prof\.)\b)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.611 | 0.122 | 0.204 | 18 | 11 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 7 | 79 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Hon.-Prof. Gotthard Clement` | `Priv.-Doz. Hon.-Prof. Gotthard Clement` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


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

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Quirin Januszis` | `Priv.-Doz. Quirin Januszis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.` (person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich` (address)
- `Amtes für Betrugsbekämpfung` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Julius Wagner` — partial — pred is substring of gold: `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Mag. Andr` — partial — pred is substring of gold: `Mag. András Péter Radics`

> overlaps gold: 1  |  likely missing annotation: 0

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

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Name_In_Parentheses`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing inside parentheses, common in legal texts for clarifications or lists.

**Content:**
```
\((?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 69 | 0 | 69 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 69 | 75 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_35`)


Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abweisung)

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_53`)


Am 31. Mai 2019 und in den folgenden Monaten, bis 3. August 2020, überwies der Bf. an die  Kindesmutter der (gemeinsamen) Töchter Maximiliane Sakschewsky, MA  und E. auf das Konto in  Großbritannien IBAN GB… 8171 € 1.000,00 (Kontoauszüge).

**False Positives:**

- `` — similar text (different position): `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

**False Positives:**

- `` — similar text (different position): `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_56`)


In den Zeiträumen 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019  sowie 17. bis 19. Februar 2020 unternahm die Tochter des Bf. in Wien Fahrten gemäß § 19  Abs. 8 FSG (Fahrtenprotokoll).

**False Positives:**

- `` — similar text (different position): `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

</details>

---

## `Name_After_Preposition_For`

**F1:** 0.013 | **Precision:** 0.016 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names following 'für' (for) or 'des' (genitive) ONLY if followed by a comma, address, or specific person markers. Excludes common nouns like 'Spruchsenates'.

**Content:**
```
(?:für\s+|des\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?:,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+\d+|\s+(?:der|die|den|dem|des|in|zu|von|gegen|über|unter|mit|auf|an|bei|nach|vor|durch|ohne|statt|wegen|trotz|während|innerhalb|außerhalb|neben|zwischen|um|bis|seit|ohne|gegenüber|entlang|laut|\.|\)|\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.016 | 0.011 | 0.013 | 64 | 1 | 63 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 63 | 86 |

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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_4`)


Am 30.09.2019 langte beim Finanzamt die Antwort der Beschwerdeführerin (in der Folge BF)  auf ein Überprüfungsschreiben des Anspruches auf Familienbeihilfe ein.

**False Positives:**

- `Anspruches` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_13`)


Ende Mai 2019 wurde meine noch minderjährige [Anmerkung: 17 ½ -jährige] Tochter aus der  Wohnung der Familie des Ziehvaters in Worcester weggewiesen.

**False Positives:**

- `Ziehvaters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Worcester`(city)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_28`)


Im Jahr 2019 bis inkl Juli 2020 ging die Tochter des Bf in Großbritannien in die Schule und  verbrachte die Sommerferien in Wien bei ihrem Vater.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Ziehvaters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_73`)


Sodann zog Maximiliane Sakschewsky, MA  zu einem Onkel des  Ziehvaters nach Worcester (und haben in dieser Zeit der Onkel und dessen Frau die Kosten für  Essen und Logie getragen).

**False Positives:**

- `Ziehvaters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

</details>

---

## `Dative_Bei_Der_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'bei der' (dative case). Excludes company names by requiring a specific name structure (e.g., two capitalized words where the second is not a known company type like IT, GmbH).

**Content:**
```
(?:bei\s+der\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?!\s+(?:IT|GmbH|AG|KG|Partnerschaft|Gesellschaft|Steuer|Wirtschaftsprüfungs|Treuhand|Steuerberater|Rechtsanwälte|Anwalts|Notar|Bf\.|Bf\.)\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 21 | 0 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 21 | 79 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Ausbildung von Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

**False Positives:**

- `Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_81`)


Unter Bedachtnahme auf das eigene Vorbringen des Bf.: ‚Ich habe monatlich € 1.000,- an  meine Ex-Gattin überwiesen, die als Schulgeld galten.‘ und den Umstand, dass diese  Überweisungen für beide Töchter erfolgt waren, bedarf es auf Basis der obigen Feststellungen  keiner weiteren Ausführungen, dass mit den Leistungen des Bf. nicht die überwiegenden  Unterhaltskosten seiner (17 ½- bis 18 ½- jährigen) Tochter Maximiliane Sakschewsky, MA, die ab Mai 2019  bei einem Onkel ihres Ziehvaters und dessen Frau (in Worcester) und sodann zeitweilig (der Bf.  spricht von 1 Monat) bei der Mutter ihres Freundes lebte, abgedeckt worden sind.

**False Positives:**

- `Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_56`)


Die Einkommens- und Vermögensverhältnisse und allfällige Sorgepflichten des Beschuldigten  sind bei der Bemessung von Geldstrafen zu berücksichtigen.

**False Positives:**

- `Bemessung von Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_57`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes handelt es sich bei der  Strafzumessung innerhalb eines gesetzlichen Strafrahmens um eine Ermessensentscheidung,  die nach den Kriterien des § 19 VStG vorzunehmen ist (vgl. VwGH 06.04.2005, 2003/04/0031,  VwGH 17.02.2015, Ra 2015/09/0008).

**False Positives:**

- `Strafzumessung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

</details>

---

## `Name_After_Gender_Title`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures names preceded by 'Herr' or 'Frau' (including genitive 'Herrn'/'Frau'). Excludes non-names and ensures full capture with suffixes, stopping at punctuation.

**Content:**
```
\b(?:Herrn?|Frau)\s+(?:und\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:Bakk\.(?:rer\.(?:nat|phil|iur|art|techn)|iur|art|techn)|BA|MBA|LL\.M|LLB|M\.B\.L|MSc|BEd|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Mag\.(?:a)?|Dr\.(?:in)?|OStR|StR|RgR|Priv\.-Doz\.|Univ\.-Prof\.|Prof\.|Ing\.|Hon\.-Prof\.)?)?)\b
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

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, ` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, ` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `Name_After_Beschwerdesache_Simple`

**F1:** 0.081 | **Precision:** 0.444 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures names after 'Beschwerdesache' if not followed by an address immediately, but requires a comma or end of phrase. Fixed to exclude context words.

**Content:**
```
Beschwerdesache\s+(?:der\s+|des\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:Bakk\.(?:rer\.(?:nat|phil|iur|art|techn)|iur|art|techn)|BA|MBA|LL\.M|LLB|M\.B\.L|MSc|BEd|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Mag\.(?:a)?|Dr\.(?:in)?|OStR|StR|RgR|Priv\.-Doz\.|Univ\.-Prof\.|Prof\.|Ing\.|Hon\.-Prof\.)?)?)\s*(?:,|\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.444 | 0.044 | 0.081 | 9 | 4 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 5 | 86 |

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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


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

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Patricia Jentz, ` — partial — gold is substring of pred: `Patricia Jentz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Mathilda Eckholdt, ` — partial — gold is substring of pred: `Mathilda Eckholdt`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Renate Brombusch, ` — partial — gold is substring of pred: `Renate Brombusch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Alma Springel, ` — partial — gold is substring of pred: `Alma Springel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thassilo Averdiek`(person)
- `Alma Springel`(person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `75-059/0556`(tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Ludger Weynand,` — partial — gold is substring of pred: `Ludger Weynand`

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

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Judge_Richter`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures full person names following 'Richter' or 'Richterin', including titles like Mag., Dr., Prof., Hon.-Prof., VetR, etc.

**Content:**
```
(?:durch\s+(?:den\s+Richter|die\s+Richterin)\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:Mag\.|Dr\.|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|ÖkR|StR|VetR|BA|PhD)\s+)?[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Complainant_Beschwerdesache`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following 'in der Beschwerdesache', handling various titles and name structures.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+|Beschwerde\s+der\s+|Beschwerde\s+des\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:Mag\.|Dr\.|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|ÖkR|StR|VetR|BA|PhD)\s+)?[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Frau_Herr_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following 'Frau' or 'Herr', including titles and degree suffixes.

**Content:**
```
(?:Frau\s+|Herr\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:Mag\.|Dr\.|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|ÖkR|StR|VetR|BA|PhD)\s+)?[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:,\s*(?:LLM|LLB|MSc|BEd|Dr\.in|Dr\.|ÖkR|StR|VetR|BA|PhD|MedR|Univ\.-Prof\.in|Univ\.-Prof\.|Priv\.-Doz\.in|Priv\.-Doz\.|Mag\.|Prof\.|Prof\.in|Hon\.-Prof\.|Hon\.-Prof\. Dr\.)\b)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Person_After_Verb`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after verbs like 'hat', 'brachte', 'kündigte', 'beschloss' in legal contexts, often followed by 'an', 'ein', or a comma.

**Content:**
```
\b(?:hat|brachte|kündigte|beschloss|erkannte|fasste)\s+(?:durch\s+die\s+Richterin\s+|durch\s+den\s+Richter\s+)?([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)*)\s+(?:an|ein|,|\(|\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Techn_R_Title`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures 'Techn R' followed by a name. Updated to match the full title and name.

**Content:**
```
\bTechn\s+R\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `OSR_Title_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names preceded by the title 'OSR' (Oberster Staatsanwalt/Rechtsanwalt).

**Content:**
```
(?:OSR\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_After_Comma_With_Address`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names after a comma, strictly requiring a following address pattern (number + street) to avoid matching common nouns or titles.

**Content:**
```
,\s*([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)*)\s*,\s*[A-Z][a-zäöüß]+\s+\d+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_After_Verb`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after verbs like 'hat', 'brachte', 'kündigte', 'beschloss' in legal contexts. Excludes 'Herr' from the capture group if it appears as a title before the name.

**Content:**
```
\b(?:hat|brachte|kündigte|beschloss|erkannte|fasste)\s+(?:durch\s+die\s+Richterin\s+|durch\s+den\s+Richter\s+)?(?:Herr\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|Bakk\.\s+rer\.\s+nat\.|Bakk\.\s+phil\.|LL\.M\.|M\.B\.L\.|MBA|MSc|Bakk\.\s+iur\.)?)?)\s+(?:an|ein|,|\(|\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `VetR_Title_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names preceded by 'VetR' (Veterinär).

**Content:**
```
\bVetR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `StR_Title_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names preceded by 'StR' (Strafrecht).

**Content:**
```
\bStR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
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

## `PreNominal_Title_Name`

**F1:** 0.204 | **Precision:** 0.611 | **Recall:** 0.122  

**Format:** `regex`  
**Description:**
Captures person names preceded by complex legal/academic titles, now including suffixes like , MA, , BEd, , LLB.

**Content:**
```
\b(?:(?:Dr\.|Mag\.|Mag\.a|Mag\.Dr\.|DDr\.|Ing\.|LL\.M|BEd|M\.B\.L|MBA|MSc|Bakk\.(?:rer\.(?:nat|phil|iur|art|techn))?|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|OStR|StR|RgR|Prof\.)\s+)*(?:Dr\.|Mag\.|Mag\.a|Mag\.Dr\.|DDr\.|Ing\.|LL\.M|BEd|M\.B\.L|MBA|MSc|Bakk\.(?:rer\.(?:nat|phil|iur|art|techn))?|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Hon\.-Prof\.|Priv\.-Doz\.|Univ\.-Prof\.|OStR|StR|RgR|Prof\.)\s*(?:in\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BEd|LLB|LL\.M|M\.B\.L|MBA|MSc|Bakk\.(?:rer\.(?:nat|phil|iur|art|techn))?|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Mag\.(?:a)?|Dr\.(?:in)?|OStR|StR|RgR|Priv\.-Doz\.|Univ\.-Prof\.|Prof\.|Ing\.|Hon\.-Prof\.)\b)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.611 | 0.122 | 0.204 | 18 | 11 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 7 | 79 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Hon.-Prof. Gotthard Clement` | `Priv.-Doz. Hon.-Prof. Gotthard Clement` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


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

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Quirin Januszis` | `Priv.-Doz. Quirin Januszis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.` (person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich` (address)
- `Amtes für Betrugsbekämpfung` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


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

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Juliana Bartjen` | `Priv.-Doz.in Juliana Bartjen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Renate Brombusch` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Estelle Niederholz` | `Dr.in Estelle Niederholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in OStR Tosca Knoller` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


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

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Dagobert Nordholt` | `Dr. Dagobert Nordholt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `36-532/2242` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


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

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Julius Wagner` — partial — pred is substring of gold: `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `RgR HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Mag. Andr` — partial — pred is substring of gold: `Mag. András Péter Radics`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


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

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag.Dr` — partial — pred is substring of gold: `Mag.Dr. Katrin Allram`

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

</details>

---

## `Legal_Context_Name`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Description:**
Captures person names in 'in der Beschwerdesache' context. Handles names followed by comma or address.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Rechtsmittelsache|Angelegenheit)(?:\s+des)?\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?:,|\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+\d+)
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

## `Party_Name_In_Context`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Description:**
Captures person names in 'in der Beschwerdesache' context. Uses capture group to extract only the name, excluding the context prefix.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Rechtsmittelsache|Angelegenheit)(?:\s+des)?\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*,
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

## `Name_After_Genitive_Context`

**F1:** 0.105 | **Precision:** 1.000 | **Recall:** 0.056  

**Format:** `regex`  
**Description:**
Captures person names following genitive articles 'der/des' in legal contexts (e.g., 'der Beschwerdesache [Name]', 'des [Name] u. Mitbes.'), ensuring they are followed by a comma, specific legal markers, or end of phrase.

**Content:**
```
(?:der\s+des\s+)?(?:Beschwerdesache|Rechtssache|Angelegenheit|Revisionssache|Verfahren)(?:\s+des)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?:,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+\d+|\s+(?:über|gegen|in\s+der|vom|von|zu|\(|\.)|\s*$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.056 | 0.105 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 0 | 36 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Renate Brombusch` | `Renate Brombusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Juliana Bartjen` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


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

## `Name_After_Beschwerdesache`

**F1:** 0.105 | **Precision:** 1.000 | **Recall:** 0.056  

**Format:** `regex`  
**Description:**
Captures person names following 'Beschwerdesache' (or similar) in various contexts. Fixed to ensure the capture group starts after the context word and excludes company names.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Rechtsmittelsache|Angelegenheit)(?:\s+des)?\s+)(?:der\s+|des\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|Bakk\.(?:rer\.(?:nat|phil|iur|art|techn)|iur|art|techn)|LL\.M|LLB|M\.B\.L|MBA|MSc|BEd|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Mag\.(?:a)?|Dr\.|Mag\.|OStR|StR|RgR|Priv\.-Doz\.|Univ\.-Prof\.|Prof\.|Ing\.|Hon\.-Prof\.)?)?)\s*(?:,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+\d+|\s+(?:über|gegen|in\s+der|vom|von|zu|\(|\.)|\s*$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.056 | 0.105 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 0 | 36 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Renate Brombusch` | `Renate Brombusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Juliana Bartjen` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


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

## `Name_After_Beschwerdesache_Simple`

**F1:** 0.081 | **Precision:** 0.444 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures names after 'Beschwerdesache' if not followed by an address immediately, but requires a comma or end of phrase. Fixed to exclude context words.

**Content:**
```
Beschwerdesache\s+(?:der\s+|des\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:Bakk\.(?:rer\.(?:nat|phil|iur|art|techn)|iur|art|techn)|BA|MBA|LL\.M|LLB|M\.B\.L|MSc|BEd|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Mag\.(?:a)?|Dr\.(?:in)?|OStR|StR|RgR|Priv\.-Doz\.|Univ\.-Prof\.|Prof\.|Ing\.|Hon\.-Prof\.)?)?)\s*(?:,|\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.444 | 0.044 | 0.081 | 9 | 4 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 5 | 86 |

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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


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

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


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

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Patricia Jentz, ` — partial — gold is substring of pred: `Patricia Jentz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Mathilda Eckholdt, ` — partial — gold is substring of pred: `Mathilda Eckholdt`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Renate Brombusch, ` — partial — gold is substring of pred: `Renate Brombusch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Alma Springel, ` — partial — gold is substring of pred: `Alma Springel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thassilo Averdiek`(person)
- `Alma Springel`(person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `75-059/0556`(tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Ludger Weynand,` — partial — gold is substring of pred: `Ludger Weynand`

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

## `Name_After_Gender_Title`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Description:**
Captures names preceded by 'Herr' or 'Frau' (including genitive 'Herrn'/'Frau'). Excludes non-names and ensures full capture with suffixes, stopping at punctuation.

**Content:**
```
\b(?:Herrn?|Frau)\s+(?:und\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:Bakk\.(?:rer\.(?:nat|phil|iur|art|techn)|iur|art|techn)|BA|MBA|LL\.M|LLB|M\.B\.L|MSc|BEd|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Mag\.(?:a)?|Dr\.(?:in)?|OStR|StR|RgR|Priv\.-Doz\.|Univ\.-Prof\.|Prof\.|Ing\.|Hon\.-Prof\.)?)?)\b
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

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, ` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Stella Marschalk, ` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Stella Marschalk, ` — similar text (different position): `Stella Marschalk, Bakk. techn.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

</details>

---

## `Name_After_Preposition_For`

**F1:** 0.013 | **Precision:** 0.016 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures person names following 'für' (for) or 'des' (genitive) ONLY if followed by a comma, address, or specific person markers. Excludes common nouns like 'Spruchsenates'.

**Content:**
```
(?:für\s+|des\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?:,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+\d+|\s+(?:der|die|den|dem|des|in|zu|von|gegen|über|unter|mit|auf|an|bei|nach|vor|durch|ohne|statt|wegen|trotz|während|innerhalb|außerhalb|neben|zwischen|um|bis|seit|ohne|gegenüber|entlang|laut|\.|\)|\s*$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.016 | 0.011 | 0.013 | 64 | 1 | 63 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 63 | 86 |

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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_4`)


Am 30.09.2019 langte beim Finanzamt die Antwort der Beschwerdeführerin (in der Folge BF)  auf ein Überprüfungsschreiben des Anspruches auf Familienbeihilfe ein.

**False Positives:**

- `Anspruches` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_13`)


Ende Mai 2019 wurde meine noch minderjährige [Anmerkung: 17 ½ -jährige] Tochter aus der  Wohnung der Familie des Ziehvaters in Worcester weggewiesen.

**False Positives:**

- `Ziehvaters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Worcester`(city)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_28`)


Im Jahr 2019 bis inkl Juli 2020 ging die Tochter des Bf in Großbritannien in die Schule und  verbrachte die Sommerferien in Wien bei ihrem Vater.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Ziehvaters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_73`)


Sodann zog Maximiliane Sakschewsky, MA  zu einem Onkel des  Ziehvaters nach Worcester (und haben in dieser Zeit der Onkel und dessen Frau die Kosten für  Essen und Logie getragen).

**False Positives:**

- `Ziehvaters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Kinderabsetzbetrages` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_22`)


Im Rückforderungsbetrag ist die  anteilige Geschwisterstaffel für sämtliche Kinder enthalten, für die Sie im  Rückforderungszeitraum zu Unrecht Familienbeihilfe erhalten haben (§ 8 Abs. 3  Familienlastenausgleichsgesetz 1967).“  4. Dagegen erhob die Bf. rechtzeitig die Beschwerde vom 07.10.2021 und brachte vor, dass  hierbei nur ein Wechsel des Studienortes bei gleichbleibender Studienrichtung vorliege.

**False Positives:**

- `Studienortes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_129`)


Kein Studienwechsel (und damit außerhalb des Anwendungsbereiches des § 17 StudFG) ist der  Wechsel der Studieneinrichtung/des Studienortes bei gleichbleibender Studienrichtung.

**False Positives:**

- `Anwendungsbereiches` — no gold match — likely missing annotation
- `Studienortes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_133`)


Im Übrigen regelt auch § 50 Abs. 2 Z 3 StudFG idF des BGBl. I Nr.  76/2000 das Erlöschen des Anspruchs auf Studienbeihilfe, wenn der Studierende „ein anderes  Studium“ aufnimmt, und lässt diese Regelung für den (auch dort vom Studienwechsel zu  unterscheidenden) Wechsel der Studieneinrichtung gelten (arg.: „dies gilt auch für den  Wechsel der in § 3 Abs. 1 genannten Einrichtungen“;

**False Positives:**

- `Anspruchs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_145`)


Ein solcher Wechsel kann jederzeit erfolgen, ohne dass  es zum Verlust des Anspruches auf Familienbeihilfe kommt.

**False Positives:**

- `Anspruches` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_149`)


Die Bf. hat daher zwar einen Studienortwechsel, aber  keinen Wechsel des Studiums vorgenommen.

**False Positives:**

- `Studiums` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_167`)


Für die Überprüfung dieser  Frage erachte es der VwGH als ausreichend, die Unterscheidung auf die Kernfächer bzw. den  Kernbereich des Studiums zu reduzieren (VwGH 7.8.2001, 97/14/0068).

**False Positives:**

- `Studiums` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_9`)


Das Verwaltungsgericht hat der Abgabenbehörde aufzutragen, innerhalb einer Frist von bis  zu drei Monaten ab Einlangen der Säumnisbeschwerde zu entscheiden und gegebenenfalls eine  Abschrift des Bescheides vorzulegen oder anzugeben, warum eine Verletzung der  Entscheidungspflicht nicht oder nicht mehr vorliegt.

**False Positives:**

- `Bescheides` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_12`)


Diesen Antrag vom 25.11.2024 hat das Amt für Betrugsbekämpfung mit Bescheid vom 02.  Dezember 2024 abgewiesen.

**False Positives:**

- `Betrugsbekämpfung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_35`)


Bei Begünstigungstatbeständen tritt die Amtswegigkeit der  Sachverhaltsermittlung gegenüber der Offenlegungspflicht des Begünstigungswerbers in den  Hintergrund.

**False Positives:**

- `Begünstigungswerbers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_39`)


Da die  Uneinbringlichkeit einer Geldstrafe ohnehin unter der Sanktion des Vollzuges der  Ersatzfreiheitsstrafe steht, kommt dem Umstand der Gefährdung der Einbringlichkeit der  aushaftenden Forderung im Falle einer Geldstrafe laut Rechtsprechung des  Verwaltungsgerichtshofes kein Gewicht zu.

**False Positives:**

- `Vollzuges` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_44`)


Ebenso trifft es allerdings zu, dass der  Ruin der wirtschaftlichen Existenz des Bestraften den mit der Bestrafung verfolgten Zweck  auch nicht sinnvoll erreicht (vgl. VwGH 24.9.2003, 2003/13/0084, ÖStZ 2004/190, ÖStZB  2004/109).

**False Positives:**

- `Bestraften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Magistrates` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_2`)


II. Gemäß § 52 Abs. 1 und 2 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei einen Beitrag zu den Kosten des Beschwerdeverfahrens in Höhe  von 11,00 Euro zu leisten.

**False Positives:**

- `Beschwerdeverfahrens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_6`)


Entscheidungsgründe  Verfahrensgang:  Das Abstellen des Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 (A) wurde   1 von 7 Seite 2 von 7

**False Positives:**

- `Kraftfahrzeuges` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_20`)


Zudem wurde gemäß § 64  Abs. 2 Verwaltungsstrafgesetz (VStG) ein Betrag von 10,00 Euro als Beitrag zu den Kosten des  Strafverfahrens auferlegt, wodurch sich der zu zahlende Gesamtbetrag auf 65,00 Euro belief.

**False Positives:**

- `Strafverfahrens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_22`)


solches in einer Kurzparkzone abstellt, müsse gemäß § 5 Abs. 2 der Wiener  Parkometerabgabeverordnung bei Beginn des Abstellens die Parkometerabgabe entrichten.

**False Positives:**

- `Abstellens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_50`)


Der Bf. bekämpft mit der gegenständlichen Beschwerde ausschließlich die mit dem  Straferkenntnis festgesetzte Strafhöhe, somit war entsprechend der ständigen Judikatur des  Verwaltungsgerichtshofes von einer Teilrechtskraft des Schuldspruches auszugehen (vgl. z.B.  VwGH 20.9.2013, 2013/17/0305).

**False Positives:**

- `Verwaltungsgerichtshofes` — type mismatch — same span as gold: `Verwaltungsgerichtshofes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_72`)


Gemäß § 52 Abs. 1 VwGVG ist in jedem Erkenntnis des Verwaltungsgerichtes, mit dem ein  Straferkenntnis bestätigt wird, auszusprechen, dass der Bestrafte einen Beitrag zu den Kosten  des Strafverfahrens zu leisten hat.

**False Positives:**

- `Strafverfahrens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_83`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

**False Positives:**

- `Beschwerdeführers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_4`)


Die Bemessungsgrundlagen und die Höhe der festgesetzten Abgaben sind den als Beilage  angeschlossenen Berechnungsblättern zu entnehmen und bilden einen Bestandteil des  Spruches dieses Erkenntnisses.

**False Positives:**

- `Spruches` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_113`)


Unter Gesamtgewinn ist der Gesamtbetrag der Gewinne zuzüglich steuerfreier  Einnahmen abzüglich des Gesamtbetrags der Verluste zu verstehen.

**False Positives:**

- `Gesamtbetrags` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_116`)


(2) Unter Gesamtüberschuß ist der Gesamtbetrag der Überschüsse der Einnahmen über die  Werbungskosten abzüglich des Gesamtbetrags der Verluste zu verstehen.

**False Positives:**

- `Gesamtbetrags` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_144`)


In Anbetracht der Tatsache, dass der Bf. die in Rede stehende Tätigkeit 2014, aufgrund des  Rückganges der Aufträge und der Tatsache, dass es für ihn immer schwieriger wurde Aufträge  für Auftritte zu erhalten, durch seine betriebswirtschaftlich sinnvolle Entscheidung, beendet  hat und in dem gesamten Betätigungszeitraum (hier von 1975 bis 2014) ein Gesamtüberschuss  erwirtschaftet (laut BVE geht das Finanzamt nicht vom Vorliegen einer Gesamtverlustes über  den gesamten Tätigkeitszeitraum aus) wurde, kann laut Ansicht des BFG keine Liebhaberei  vorliegen.

**False Positives:**

- `Rückganges` — no gold match — likely missing annotation
- `Auftritte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

**False Positives:**

- `Bundesfinanzgericht` — type mismatch — same span as gold: `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_31`)


Dagegen brachte die Vertreterin des Bf mit Schreiben vom 25.03.2025 Beschwerde ein.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_45`)


Da der Erstbescheid des Bf zur Einkommensteuer 2021 eine Nachforderung von Euro  167.848,00 ergeben hat und dieser erst am 22.05.2024 ergangen ist (also somit nach dem  01.10.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_46`)


des dem Jahr des Entstehens des Abgabenanspruch folgenden Jahres) wurden mit  Bescheid vom 22.05.2024 Anspruchszinsen gem. § 205 BAO in der Höhe von Euro 13.809,18  festgesetzt.

**False Positives:**

- `Entstehens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_47`)


Da der Einkommensteuerbescheid aufgrund der Beschwerde des Bf mit  Beschwerdevorentscheidung vom 12.03.2025 abgeändert wurde (zugunsten des Bf) erging am  12.03.2025 der neue (bzw. weitere) Bescheid über die Festsetzung von Anspruchszinsen 2021, in  dem diesem Umstand Rechnung getragen wurde (Gutschrift Anspruchszinsen in der Höhe von  Euro 7.963,60).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_54`)


Rechtliche Beurteilung  2.1. Zu Spruchpunkt I. (Abweisung)  § 205 BAO normiert auszugsweise:  Gemäß § 205 Abs. 1 BAO sind Differenzbeträge an Einkommensteuer und Körperschaftsteuer,  die sich aus Abgabenbescheiden unter Außerachtlassung von Anzahlungen (Abs. 3), nach  Gegenüberstellung mit Vorauszahlungen oder mit der bisher festgesetzt gewesenen Abgabe  ergeben, für den Zeitraum ab 1. Oktober des dem Jahr des Entstehens des Abgabenanspruchs  folgenden Jahres bis zum Zeitpunkt der Bekanntgabe dieser Bescheide zu verzinsen  (Anspruchszinsen).

**False Positives:**

- `Entstehens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_64`)


Mit Ablauf des Zeitraumes des Abs. 2 dritter Satz sind noch nicht verrechnete und  nicht bereits gutgeschriebene Anzahlungen gutzuschreiben.

**False Positives:**

- `Zeitraumes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_94`)


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

**False Positives:**

- `Verwaltungsgerichtshofes` — type mismatch — same span as gold: `Verwaltungsgerichtshofes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_27`)


Im angeschlossenen Vorlagebericht vom selben Tag  führte die belangte Behörde ergänzend aus, dass das Kriterium der Zwangsläufigkeit, das stets  nach den Umständen des Einzelfalles zu prüfen sei, strittig sei.

**False Positives:**

- `Einzelfalles` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_44`)


Die Kosten setzen sich aus Spitalskosten in Höhe von Euro 10.340,97 abzüglich  Euro 41,84 Haushaltsersparnis für die Dauer des Spitalsaufenthalts von acht Tagen zusammen.

**False Positives:**

- `Spitalsaufenthalts` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

**False Positives:**

- `Einzelfalls` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VwGH`(organisation)

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_101`)


Die Zwangsläufigkeit des Aufwands ist stets nach den Umständen des Einzelfalls zu prüfen.

**False Positives:**

- `Einzelfalls` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Am 24.9.2015 erließ das Finanzamt einen Vorhalt an den Beschwerdeführer (Bf.), in dem es  ausführte, dass Vertreter juristischer Personen alle Pflichten des Vertretenen zu erfüllen  hätten.

**False Positives:**

- `Vertretenen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_39`)


Aus diesem Grund sei die Höhe des Haftungsbetrages vordergründig noch nicht geprüft  worden.

**False Positives:**

- `Haftungsbetrages` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_76`)


Die Behörde habe bei entsprechenden Behauptungen und diesbezüglichem  Beweisanbot die zur Entlastung des Vertreters angebotenen Beweise aufzunehmen und  erforderliche Präzisierungen abzufordern, jedenfalls aber konkrete Feststellungen über die  angebotenen Entlastungsbehauptungen zu treffen (VwGH 23.4.1998, 95/15/0145;

**False Positives:**

- `Vertreters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_80`)


In der Stellungnahme des steuerlichen Vertreters vom 27.11.2015  werde allerdings eine Nichtausübung des Ermessensspielraumes seitens des Finanzamtes  argumentiert, da der Bf. zum gegenwärtigen Zeitpunkt über kein Vermögen verfüge und eine  etwaige Haftungsinanspruchnahme keinesfalls einbringlich sei.

**False Positives:**

- `Ermessensspielraumes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `Finanzamt Kirchdorf Perg Steyr` — type mismatch — same span as gold: `Finanzamt Kirchdorf Perg Steyr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_133`)


Die  belangte Behörde sei auf die vorgebrachten Punkte hinsichtlich der wirtschaftlichen  Leistungsfähigkeit in keinster Weise eingegangen, obwohl sie auf Grund des  Amtswegigkeitsprinzips zur Ermittlung des für die korrekte Ermessensausübung erforderlichen  Sachverhalts verpflichtet gewesen wäre.

**False Positives:**

- `Amtswegigkeitsprinzips` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_135`)


Ungeachtet dessen, stelle die belangte Behörde eine  Ungleichbehandlung des Finanzamtes zu 100% fest und ziehe den Betroffenen hinsichtlich des  gesamten Betrages zur Haftung heran.

**False Positives:**

- `Finanzamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

**False Positives:**

- `Haftenden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_146`)


Selbst wenn auf Grund der derzeitigen wirtschaftlichen Situation des Beschwerdeführers die  Abgaben erschwert einbringlich seien, ließe sich daraus eine Unzumutbarkeit der  Haftungsinanspruchnahme nicht ableiten, weil es nach der Rechtsprechung nicht zutreffe, dass  die Haftung nur bis zur Höhe der aktuellen Einkünfte bzw. des aktuellen Vermögens geltend  gemacht werden dürfte (vgl. VwGH 29.

**False Positives:**

- `Beschwerdeführers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `Finanzamt Kirchdorf Perg Steyr` — type mismatch — same span as gold: `Finanzamt Kirchdorf Perg Steyr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_173`)


Gemäß § 224 Abs. 3 BAO ist die erstmalige Geltendmachung eines Abgabenanspruches  anlässlich der Erlassung eines Haftungsbescheides gemäß Abs. 1 nach Eintritt der Verjährung  des Rechtes zur Festsetzung der Abgabe nicht mehr zulässig.

**False Positives:**

- `Rechtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_203`)


Im Hinblick auf die unterlassene Behauptung und Konkretisierung des Ausmaßes der  Unzulänglichkeit der in den Fälligkeitszeitpunkten zur Verfügung gestandenen Mittel zur  13 von 15 Seite 14 von 15

**False Positives:**

- `Ausmaßes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_215`)


Dem Vorbringen des Bf. in der Vorhaltsbeantwortung vom 27.11.2015 und im  Beschwerdeschreiben vom 16.3.2016, dass der Bf. über kein Vermögen verfüge und ein  Nettoeinkommen von 1.400,- € beziehe, von dem aber kein pfändbarer Betrag übrigbleibe, das  Finanzamt daher über eine gesetzeskonforme Ermessensübung eine Haftung nicht hätte  aussprechen dürfen, ist auf die Ausführungen des Finanzamtes zu verweisen, das seine  Entscheidung im Zusammenhang mit dem Ermessen sehr wohl rechtsrichtig begründete.

**False Positives:**

- `Finanzamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_217`)


Im Vorlageantrag vom 18.4.2016 wurde weder auf die Begründung im angefochtenen  Haftungsbescheid noch auf die Argumentation des Finanzamtes in der BVE noch auf die  Ausführungen im Vorlagebericht eingegangen.

**False Positives:**

- `Finanzamtes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_221`)


Ergebnis  Auf Grund des Vorliegens der gesetzlichen Voraussetzungen erfolgte somit die  Inanspruchnahme des Bf. als Haftungspflichtiger für die nachstehenden Abgabenschuldigkeiten  der Primärschuldnerin im Ausmaß von nunmehr 128.402,72 € zu Recht.

**False Positives:**

- `Vorliegens` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_45`)


(4) Säumniszuschläge sind für Abgabenschuldigkeiten insoweit nicht zu entrichten, als   a) ihre Einhebung gemäß § 212a ausgesetzt ist,  b) ihre Einbringung gemäß § 230 Abs. 2, 3, 5 oder 6 gehemmt ist,  c) ein Zahlungsaufschub im Sinn des § 212 Abs. 2 zweiter Satz nicht durch Ausstellung eines  Rückstandsausweises (§ 229) als beendet gilt,  d) ihre Einbringung gemäß § 231 ausgesetzt ist.

**False Positives:**

- `Abgabenschuldigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_50`)


Die  Verwirkung von Säumniszuschlägen setzt kein Verschulden des Abgabepflichtigen voraus.

**False Positives:**

- `Abgabepflichtigen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_68`)


spätestens einen Monat nach dem Tag des Erwerbs des Kfz. am 13.4.2017, also am  13.5.2017, selbst zu berechnen und abzuführen gehabt.

**False Positives:**

- `Erwerbs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_69`)


Da er dieser Verpflichtung nicht  nachgekommen ist, ist er säumig geworden und hatte er dafür Säumniszuschläge zu  entrichten.

**False Positives:**

- `Säumniszuschläge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_83`)


Mit der Verfügung des Ablaufs der Bewilligung der  Aussetzung der Einhebung gemäß § 212 a Abs. 5 BAO lag betreffend die Umsatzsteuer  (Fahrzeugeinzelbesteuerung) kein Grund mehr vor, aus dem keine Säumniszinsen festgesetzt  werden durften.

**False Positives:**

- `Ablaufs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Judge_Richter`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures full person names following 'Richter' or 'Richterin', including titles like Mag., Dr., Prof., Hon.-Prof., VetR, etc.

**Content:**
```
(?:durch\s+(?:den\s+Richter|die\s+Richterin)\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:Mag\.|Dr\.|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|ÖkR|StR|VetR|BA|PhD)\s+)?[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Complainant_Beschwerdesache`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following 'in der Beschwerdesache', handling various titles and name structures.

**Content:**
```
(?:in\s+der\s+Beschwerdesache\s+|Beschwerde\s+der\s+|Beschwerde\s+des\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:Mag\.|Dr\.|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|ÖkR|StR|VetR|BA|PhD)\s+)?[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Frau_Herr_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names following 'Frau' or 'Herr', including titles and degree suffixes.

**Content:**
```
(?:Frau\s+|Herr\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:Mag\.|Dr\.|Prof\.|Prof\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|ÖkR|StR|VetR|BA|PhD)\s+)?[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:,\s*(?:LLM|LLB|MSc|BEd|Dr\.in|Dr\.|ÖkR|StR|VetR|BA|PhD|MedR|Univ\.-Prof\.in|Univ\.-Prof\.|Priv\.-Doz\.in|Priv\.-Doz\.|Mag\.|Prof\.|Prof\.in|Hon\.-Prof\.|Hon\.-Prof\. Dr\.)\b)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Person_After_Verb`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after verbs like 'hat', 'brachte', 'kündigte', 'beschloss' in legal contexts, often followed by 'an', 'ein', or a comma.

**Content:**
```
\b(?:hat|brachte|kündigte|beschloss|erkannte|fasste)\s+(?:durch\s+die\s+Richterin\s+|durch\s+den\s+Richter\s+)?([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)*)\s+(?:an|ein|,|\(|\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Techn_R_Title`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures 'Techn R' followed by a name. Updated to match the full title and name.

**Content:**
```
\bTechn\s+R\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `OSR_Title_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names preceded by the title 'OSR' (Oberster Staatsanwalt/Rechtsanwalt).

**Content:**
```
(?:OSR\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dative_Bei_Der_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'bei der' (dative case). Excludes company names by requiring a specific name structure (e.g., two capitalized words where the second is not a known company type like IT, GmbH).

**Content:**
```
(?:bei\s+der\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*(?!\s+(?:IT|GmbH|AG|KG|Partnerschaft|Gesellschaft|Steuer|Wirtschaftsprüfungs|Treuhand|Steuerberater|Rechtsanwälte|Anwalts|Notar|Bf\.|Bf\.)\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 21 | 0 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 21 | 79 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Ausbildung von Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

**False Positives:**

- `Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_81`)


Unter Bedachtnahme auf das eigene Vorbringen des Bf.: ‚Ich habe monatlich € 1.000,- an  meine Ex-Gattin überwiesen, die als Schulgeld galten.‘ und den Umstand, dass diese  Überweisungen für beide Töchter erfolgt waren, bedarf es auf Basis der obigen Feststellungen  keiner weiteren Ausführungen, dass mit den Leistungen des Bf. nicht die überwiegenden  Unterhaltskosten seiner (17 ½- bis 18 ½- jährigen) Tochter Maximiliane Sakschewsky, MA, die ab Mai 2019  bei einem Onkel ihres Ziehvaters und dessen Frau (in Worcester) und sodann zeitweilig (der Bf.  spricht von 1 Monat) bei der Mutter ihres Freundes lebte, abgedeckt worden sind.

**False Positives:**

- `Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_56`)


Die Einkommens- und Vermögensverhältnisse und allfällige Sorgepflichten des Beschuldigten  sind bei der Bemessung von Geldstrafen zu berücksichtigen.

**False Positives:**

- `Bemessung von Geldstrafen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_57`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes handelt es sich bei der  Strafzumessung innerhalb eines gesetzlichen Strafrahmens um eine Ermessensentscheidung,  die nach den Kriterien des § 19 VStG vorzunehmen ist (vgl. VwGH 06.04.2005, 2003/04/0031,  VwGH 17.02.2015, Ra 2015/09/0008).

**False Positives:**

- `Strafzumessung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_68`)


Mit einer Geldstrafe von 55,00 Euro wird der Strafrahmen von 365,00 Euro lediglich zu rund  15% ausgeschöpft, wodurch bei der Strafbemessung allenfalls ungünstigen Einkommens- und  Vermögensverhältnissen des Bf. hinreichend Rechnung getragen wird.

**False Positives:**

- `Strafbemessung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_115`)


Wertänderungen von Grund und Boden, der zum Anlagevermögen gehört, sind nur bei der  Gewinnermittlung nach § 5 EStG 1988 anzusetzen.

**False Positives:**

- `Gewinnermittlung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_121`)


Aus dem Begriff des Einkommens bzw. konkret aus der Umschreibung der Einkünfte als  Gewinn bzw. als Überschuss der Einnahmen über die Werbungskosten wird abgeleitet, dass  nur eine Tätigkeit, die auf Dauer ein positives wirtschaftliches Gesamtergebnis erbringt, als  Einkunftsquelle in Betracht kommt und bei der Einkommensteuer zu berücksichtigen ist.

**False Positives:**

- `Einkommensteuer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_140`)


Geht man aus vorstehenden Gründen vom Vorliegen einer § 1 Abs. 1 - Betätigung aus, so ist in  weiterer Folge die Gesamtgewinnerzielungsabsicht der Beurteilungsmaßstab bei der  Liebhabereiprüfung.

**False Positives:**

- `Liebhabereiprüfung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_59`)


Die bei der Ehefrau des Bf. am 15. November 2022  durchgeführte Operation war folglich medizinisch indiziert.

**False Positives:**

- `Ehefrau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_60`)


Die Bf. war nach den unstrittigen Sachverhaltsfeststellungen Diabetikerin, sodass bei der  Schmerzmedikation entsprechend darauf Bedacht genommen werden musste (vgl.  Befundbericht vom 6. Oktober 2025).

**False Positives:**

- `Schmerzmedikation` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_123`)


Zum anderen handelt es sich bei der  Frage, ob triftige medizinische Gründe vorliegen oder nicht, um eine solche der  Beweiswürdigung, zu deren Überprüfung der Verwaltungsgerichtshof als Rechtsinstanz  grundsätzlich nicht berufen ist (vgl. VwGH 10.5.2021, Ra 2021/15/0031 und 5.10.2021,  Ra 2021/15/0059).

**False Positives:**

- `Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_15`)


Die genannten Beträge seien bei der GmbH als uneinbringlich anzusehen.

**False Positives:**

- `Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_28`)


der Nichterbringung dieser Nachweise müsse das Finanzamt davon ausgehen, dass der Bf. die  ihm obliegende Verpflichtung, die fällig gewordenen Abgaben aus den verwaltenden Mitteln  zu entrichten, schuldhaft verletzt habe, und diese Pflichtverletzung auch ursächlich für den  Abgabenausfall bei der GmbH sei.

**False Positives:**

- `Gmb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_33`)


Im vorliegenden Fall wäre  hinsichtlich der Ermessensausübung insbesondere die wirtschaftliche Leistungsfähigkeit (vgl  Ritz, BAO5 § 9 Rz 28 mwN) vom Bf. bei der Haftungsinanspruchnahme zu beachten: Herr  Dieter Leufkes  verfüge zum gegenwärtigen Zeitpunkt über kein Vermögen.

**False Positives:**

- `Haftungsinanspruchnahme` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dieter Leufkes`(person)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_36`)


In diesem Zusammenhang sei bei der  Ermessensausübung auch der Grundsatz der Sparsamkeit, Wirtschaftlichkeit und  Zweckmäßigkeit der Vollziehung (Art 126b (5) B-VG) zu beachten - insbesondere in Hinblick auf  die Kosten der Vollstreckungsversuche, die aus oben genannten Gründen erfolglos verlaufen  würden.

**False Positives:**

- `Ermessensausübung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_37`)


Unabhängig davon lägen die gegenständlichen Abgabenschulden schon lange Zeit zurück - ein  Umstand der It. stRsp bei der Ermessensausübung ebenfalls berücksichtigt werden müsse (vgl  Ritz, BAO5 § 9 Rz 28 mwN).

**False Positives:**

- `Ermessensausübung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_86`)


Weiters gehe aus der Stellungnahme hervor, dass bei der Ermessensentscheidung auch  berücksichtigt werden müsse, dass die gegenständlichen Abgabenschulden schon lange Zeit  zurücklägen.

**False Positives:**

- `Ermessensentscheidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_127`)


Aus dem auf die Hereinbringung der Abgabenschuld beim Haftenden gerichteten  Besicherungszweck der Haftungsnorm folge, dass die Geltendmachung der Haftung in der  Regel dann ermessenskonform sei, wenn die betreffenden Abgaben bei der Primärschuldnerin  uneinbringlich seien.

**False Positives:**

- `Primärschuldnerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_144`)


Im vorliegenden Fall sei unbestritten,  dass die betreffenden Abgabenforderungen bei der Primärschuldnerin uneinbringlich seien.

**False Positives:**

- `Primärschuldnerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_211`)


Die erschwerte Einbringlichkeit der haftungsgegenständlichen Abgaben bei der  Primärschuldnerin stand im Zeitpunkt der Eröffnung des Insolvenzverfahrens, somit am  tt.5.2013, fest.

**False Positives:**

- `Primärschuldnerin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name_After_Comma_With_Address`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names after a comma, strictly requiring a following address pattern (number + street) to avoid matching common nouns or titles.

**Content:**
```
,\s*([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)*)\s*,\s*[A-Z][a-zäöüß]+\s+\d+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_After_Verb`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after verbs like 'hat', 'brachte', 'kündigte', 'beschloss' in legal contexts. Excludes 'Herr' from the capture group if it appears as a title before the name.

**Content:**
```
\b(?:hat|brachte|kündigte|beschloss|erkannte|fasste)\s+(?:durch\s+die\s+Richterin\s+|durch\s+den\s+Richter\s+)?(?:Herr\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|Bakk\.\s+rer\.\s+nat\.|Bakk\.\s+phil\.|LL\.M\.|M\.B\.L\.|MBA|MSc|Bakk\.\s+iur\.)?)?)\s+(?:an|ein|,|\(|\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_After_Haftung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'Haftung des' (liability of) to catch cases like 'Haftung des Felix Stukenbröker'.

**Content:**
```
\bHaftung\s+des\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 2 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_67`)


Bei Verletzung des Gleichbehandlungsgrundsatzes erstrecke sich die Haftung des Vertreters  nur auf jenen Betrag, um den bei gleichmäßiger Behandlung sämtlicher Gläubiger die  Abgabenbehörde mehr erlangt hätte, als sie infolge des pflichtwidrigen Verhaltens des  Vertreters tatsächlich bekommen habe.

**False Positives:**

- `Vertreters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_204`)


Erfüllung der vollen Abgabenverbindlichkeiten kommt eine Beschränkung der Haftung des Bf.  bloß auf einen Teil der von der Haftung betroffenen Abgabenschulden nicht in Betracht (VwGH  21.1.1991, 90/15/0055).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `VetR_Title_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names preceded by 'VetR' (Veterinär).

**Content:**
```
\bVetR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `StR_Title_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names preceded by 'StR' (Strafrecht).

**Content:**
```
\bStR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `HR_Title_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names preceded by 'HR' (Hofrat).

**Content:**
```
\bHR\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 39 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `HR Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

</details>

---

## `Hon_Prof_in_Title_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names preceded by 'Hon.-Prof.in'.

**Content:**
```
\bHon\.-Prof\.in\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:in|der|von)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gegen_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'gegen' (against). Handles titles and standalone names. Uses capture group to extract only the name.

**Content:**
```
(?:gegen\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 0 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_57`)


22.2.2024, RV/7100415/2023) bestehen keine Bedenken, wenn über  Beschwerden gegen Säumniszuschläge entschieden wird, obwohl über die gegen die  Stammabgabenbescheide gerichteten Beschwerden noch nicht abgesprochen wurde.

**False Positives:**

- `Säumniszuschläge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name_At_Start_Of_Text`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures a person name at the very beginning of the text, followed by a comma and address. Handles cases like 'René Kalcher, ...'.

**Content:**
```
^([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)*)\s*,\s*[A-Z][a-zäöüß]+\s+\d+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_At_Start_Of_Text_Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures a person name at the start with suffixes, followed by comma and address.

**Content:**
```
^([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)*(?:\s*,\s*[A-Z][a-zäöüß]+(?:\s+\.)?)+)\s*,\s*[A-Z][a-zäöüß]+\s+\d+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Party_Name_In_Context_Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names in genitive context with suffixes, followed by a comma.

**Content:**
```
(?:des\s+|der\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+\.)?)+)\s*,
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Legal_Context_Name_Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names in 'in der Beschwerdesache' context with suffixes, followed by a comma. Uses capture group to extract only the name.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Rechtssache|Verwaltungsstrafsache|Rechtsmittelsache|Angelegenheit)(?:\s+des)?\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+\.)?)+)\s*,
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_After_Comma_Flexible`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after a comma, followed by a verb, preposition, or end of sentence. Excludes addresses and common nouns. Handles genitive articles.

**Content:**
```
,\s*(?:der\s+|des\s+|die\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:in|der|von|zu)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s+(?:erwähnt|beurteilen|darstellen|gewesen|sein|hat|ist|wurde|wird|kündigte|beschloss|erkannte|gegen|an|ein|\(|\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 24 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_77`)


Sie erfordern die  Absolvierung einer vergleichbaren Studieneingangsphase, die Abfassung einer Bachelorarbeit  und vermitteln grundsätzlich gleiche Qualifikationsprofile und Karriereaussichten.

**False Positives:**

- `Abfassung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_89`)


Beide Bachelorstudien sind nach § 2 der jeweiligen Curricula ein sozial- und  wirtschaftswissenschaftliches Studium im Sinne des § 54 Abs. 1 Universitätsgesetz 2002 und  umfassen jeweils einen Arbeitsumfang von 180 ECTS-Punkten, 6 Semester  Mindeststudiendauer, die Absolvierung einer Studieneingangsphase und die Abfassung einer  Bachelorarbeit.

**False Positives:**

- `Absolvierung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bei_Name_Context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'bei' (dative case), common in legal texts for service of process or location.

**Content:**
```
\bbei\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s+(?:sonstige|Einnahmen|aus|in|der|die|das|ist|war|wurde|hat|sein|gewesen|verbleibt|verbleiben)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 2 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_58`)


Der Zeitpunkt, für den zu beurteilen sei, ob der Primärschuldnerin die für die  Abgabenentrichtung erforderlichen Mittel zur Verfügung standen, bestimme sich danach,  wann die Abgaben bei Beachtung der abgabenrechtlichen Vorschriften zu entrichten gewesen  wären (VwGH 27.4.2000, 98/15/0003;

**False Positives:**

- `Beachtung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Techn_R_Suffix_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures 'Techn R' followed by a name and potential academic suffixes (BEd, Bakk, etc.).

**Content:**
```
\bTechn\s+R\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BEd|Bakk\.\s+rer\.\s+nat\.|Bakk\.\s+phil\.|LL\.M\.|M\.B\.L\.|MBA|MSc|Bakk\.\s+iur\.|Bakk\.\s+art\.)?)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gegen_Name_Full`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'gegen' (against). Handles titles and standalone names. Uses capture group to extract only the name.

**Content:**
```
\bgegen\s+(?:Dr\.|Mag\.|OStR\.|Priv\.-Doz\.|Univ\.-Prof\.|Techn\s+R\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 0 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_57`)


22.2.2024, RV/7100415/2023) bestehen keine Bedenken, wenn über  Beschwerden gegen Säumniszuschläge entschieden wird, obwohl über die gegen die  Stammabgabenbescheide gerichteten Beschwerden noch nicht abgesprochen wurde.

**False Positives:**

- `Säumniszuschläge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name_After_Verb_Enhanced`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after verbs like 'hat', 'brachte', 'kündigte', 'beschloss' in legal contexts. Excludes 'Herr' from the capture group if it appears as a title before the name.

**Content:**
```
\b(?:hat|brachte|k\u00fcndigte|beschloss|erkannte|fasste|gab\s+bekannt|stellte\s+fest)\s+(?:durch\s+die\s+Richterin\s+|durch\s+den\s+Richter\s+)?(?:Herr\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|Bakk\.\s+rer\.\s+nat\.|Bakk\.\s+phil\.|LL\.M\.|M\.B\.L\.|MBA|MSc|Bakk\.\s+iur\.)?)?)\s+(?:an|ein|,|\(|\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Priv_Doz_in_Title_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names preceded by 'Priv.-Doz.in'.

**Content:**
```
\bPriv\.-Doz\.in\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+(?:in|der|von)\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 24 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Priv.-Doz.in Farina` — partial — pred is substring of gold: `Priv.-Doz.in Farina Kohlstrunk`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Priv.-Doz.in Juliana` — partial — pred is substring of gold: `Priv.-Doz.in Juliana Bartjen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

</details>

---

## `Name_After_Antrag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after 'Antrag des' or 'Antrag der', requiring a comma or specific context to avoid false positives.

**Content:**
```
(?:Antrag\s+des\s+|Antrag\s+der\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mag_a_Title_Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names preceded by 'Mag.a' (female Magister) as a standalone title or after other titles.

**Content:**
```
\bMag\.a\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_With_Suffix_Generic`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names followed by academic/professional suffixes. Excludes context words like 'Beschwerdesache' by requiring the name to be a proper noun pattern and suffix to be a degree.

**Content:**
```
\b([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*,\s*(?:Bakk\.(?:rer\.(?:nat|phil|iur|art|techn)|iur|art|techn)|BA|MBA|LL\.M|LLB|M\.B\.L|MSc|BEd|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Mag\.(?:a)?|Dr\.(?:in)?|OStR|StR|RgR|Priv\.-Doz\.|Univ\.-Prof\.|Prof\.|Ing\.|Hon\.-Prof\.)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_After_Comma_Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names after a comma, including specific academic suffixes, strictly requiring a following address pattern (number + street) to avoid matching common nouns or titles.

**Content:**
```
,\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|Bakk\.(?:rer\.(?:nat|phil|iur|art|techn)|iur|art|techn)|LL\.M|LLB|M\.B\.L|MBA|MSc|BEd|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Mag\.a|Dr\.|Mag\.|OStR|StR|RgR|Priv\.-Doz\.|Univ\.-Prof\.|Prof\.|Ing\.|Hon\.-Prof\.)?)?)\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+\d+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_After_Address_Context`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing after a comma, followed by a street name and number (address pattern), to catch names without suffixes like 'Elfriede Billmeyer'.

**Content:**
```
,\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\s*,\s*[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+\s+\d+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Name_After_Preposition_Generic`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names after common prepositions ONLY if followed by a comma and address pattern. Fixed to exclude context words from the capture group.

**Content:**
```
\b(?:von|bei|durch|zu|in)\s+(?:der\s+|des\s+|die\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00fc\u00df]+)*)\s*,\s*[A-Z][a-z\u00e4\u00fc\u00df]+\s+\d+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 5 | 41 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Beschwerdesache Mathilda Eckholdt` — partial — gold is substring of pred: `Mathilda Eckholdt`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Beschwerdesache Renate Brombusch` — partial — gold is substring of pred: `Renate Brombusch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


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

## `Name_After_Vertraten_Durch`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names after 'vertreten durch'. Excludes job titles and company names. Requires a name pattern (Capitalized word) immediately following.

**Content:**
```
\bvertreten\s+durch\s+(?:Dr\.|Mag\.|Mag\.a|RgR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:Bakk\.(?:rer\.(?:nat|phil|iur|art|techn)|iur|art|techn)|BA|MBA|LL\.M|LLB|M\.B\.L|MSc|BEd|VetR|\u00d6kR|OMedR|HR|KzlR|KommR|Techn\s+R|OSR|MedR|Mag\.(?:a)?|Dr\.(?:in)?|OStR|StR|RgR|Priv\.-Doz\.|Univ\.-Prof\.|Prof\.|Ing\.|Hon\.-Prof\.)?)?)\s*(?!\s+(?:GmbH|AG|KG|Partnerschaft|Gesellschaft|Steuer|Wirtschaftsprüfungs|Treuhand|Steuerberater|Rechtsanwälte|Anwalts|Notar|Bf\.|Bf\.)|\s*$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 24 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. András Péter Radics`

> overlaps gold: 1  |  likely missing annotation: 0

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Anwälte Mandl` — partial — pred is substring of gold: `Anwälte Mandl & Mitterbauer GmbH`

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

## `Name_In_Parentheses`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names appearing inside parentheses, common in legal texts for clarifications or lists.

**Content:**
```
\((?:[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)\)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 69 | 0 | 69 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 69 | 75 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_35`)


Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abweisung)

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_53`)


Am 31. Mai 2019 und in den folgenden Monaten, bis 3. August 2020, überwies der Bf. an die  Kindesmutter der (gemeinsamen) Töchter Maximiliane Sakschewsky, MA  und E. auf das Konto in  Großbritannien IBAN GB… 8171 € 1.000,00 (Kontoauszüge).

**False Positives:**

- `` — similar text (different position): `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

**False Positives:**

- `` — similar text (different position): `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_56`)


In den Zeiträumen 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019  sowie 17. bis 19. Februar 2020 unternahm die Tochter des Bf. in Wien Fahrten gemäß § 19  Abs. 8 FSG (Fahrtenprotokoll).

**False Positives:**

- `` — similar text (different position): `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_72`)


Sie lebte mit ihrer (vom Bf. geschiedenen) Mutter, deren Lebensgefährten (Ziehvater) und ihrer  Schwester bis Mai 2019 in Großbritannien.

**False Positives:**

- `` — similar text (different position): `Großbritannien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Großbritannien`(country)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `` — similar text (different position): `5966 230804`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_7`)


Die  Auszahlung der Familienbeihilfe war bereits mit 01/2021 eingestellt worden, da laut  Studiendatenübermittlungsauskunft das Studium der Tochter der Bf. (Viktoria Immohr) nur bis  14.12.2020 betrieben wurde und die Tochter mit 01.01.2021 eine Teilzeitbeschäftigung  begonnen hatte.

**False Positives:**

- `` — partial — pred is substring of gold: `Viktoria Immohr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

**False Positives:**

- `` — similar text (different position): `Viktoria Immohr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `` — similar text (different position): `5966 230804`
- `` — similar text (different position): `5966 230804`
- `` — similar text (different position): `5966 230804`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_33`)


An der WU Wien wurde das Studium  Wirtschafts- und Sozialwissenschaften (Bachelor) betrieben, in Linz handelte es sich um das  Studium Wirtschaftswissenschaften (Bachelor).

**False Positives:**

- `` — similar text (different position): `WU Wien`
- `` — similar text (different position): `WU Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `WU Wien`(organisation)
- `Linz`(city)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

**False Positives:**

- `` — similar text (different position): `WU Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)
- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz (`(organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_123`)


3.2. Zu Spruchpunkt I. (Stattgabe)  Die Bf. absolvierte im ersten Studienjahr erfolgreich die Studieneingangs- und  Orientierungsphase (StEOP).

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_171`)


3.3. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  15 von 16 Seite 16 von 16

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_5`)


§ 284 BAO lautet auszugsweise:  (1) Wegen Verletzung der Entscheidungspflicht kann die Partei Beschwerde  (Säumnisbeschwerde) beim Verwaltungsgericht erheben, wenn ihr Bescheide der  Abgabenbehörden nicht innerhalb von sechs Monaten nach Einlangen der Anbringen oder nach  1 von 3 Seite 2 von 3

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_4`)


Für den Fall, dass zu einem  Ratentermin keine Zahlung in der festgesetzten Höhe erfolgt (Terminverlust), erlischt die  Bewilligung und sind Vollstreckungsmaßnahmen zulässig (§ 175 FinStrG).

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_19`)


Um diese finanziell ohnedies sehr „bescheidene Liquiditätsperiode“ bestmöglich zu  überstehen, habe ich erklärt, dass ich selbstverständlich zahlungswillig bin, die offene Schuld  jedoch nicht in einem Zuge (Vollzahlung) begleichen kann.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_28`)


Gemäß § 185 Abs. 5 FinStrG obliegt die Einhebung, Sicherung und Einbringung der Kosten,  ausgenommen jener für den Vollzug einer Freiheitsstrafe (Ersatzfreiheitsstrafe), den  Finanzstrafbehörden.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_32`)


Gemäß § 212 Abs. 1 BAO kann die Abgabenbehörde auf Ansuchen des Abgabepflichtigen für  Abgaben, hinsichtlich derer ihm gegenüber auf Grund eines Rückstandsausweises (§ 229)  Einbringungsmaßnahmen für den Fall des bereits erfolgten oder späteren Eintrittes aller  Voraussetzungen hiezu in Betracht kommen, den Zeitpunkt der Entrichtung der Abgaben  hinausschieben (Stundung) oder die Entrichtung in Raten bewilligen, wenn die sofortige oder  die sofortige volle Entrichtung der Abgaben für den Abgabepflichtigen mit erheblichen Härten  verbunden wäre und die Einbringlichkeit der Abgaben durch den Aufschub nicht gefährdet  wird.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_46`)


Wie  vom Bf. in seinem Antrag auf Zahlungserleichterung vom 25.11.2024 ausgeführt, wurde das  Insolvenzverfahren (Schuldenregulierungsverfahren) eröffnet.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_50`)


Für den Fall, dass zu einem Ratentermin keine  Zahlung in der festgesetzten Höhe erfolgt (Terminverlust), erlischt die Bewilligung und sind  Vollstreckungsmaßnahmen zulässig (vgl. § 230 Abs. 5 BAO, §§ 175 ff FinStrG).

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

**False Positives:**

- `` — similar text (different position): `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_107`)


(2) Innerhalb der ersten drei Kalenderjahre (Wirtschaftsjahre) ab Beginn einer Betätigung (zB  Eröffnung eines Betriebes) im Sinn des § 1 Abs. 1, längstens jedoch innerhalb der ersten fünf  Kalenderjahre (Wirtschaftsjahre) ab dem erstmaligen Anfallen von Aufwendungen (Ausgaben)  für diese Betätigung liegen jedenfalls Einkünfte vor (Anlaufzeitraum).

**False Positives:**

- `` — no gold match — likely missing annotation
- `` — no gold match — likely missing annotation
- `` — no gold match — likely missing annotation
- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_111`)


Ein Anlaufzeitraum im Sinn des ersten Satzes darf nicht  angenommen werden, wenn nach den Umständen des Einzelfalls damit zu rechnen ist, daß die  Betätigung vor dem Erzielen eines Gesamtgewinnes (Gesamtüberschusses) beendet wird.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_114`)


Steuerfreie Einnahmen sind  nur insoweit anzusetzen, als sie nicht zu einer Kürzung von Aufwendungen (Ausgaben) führen.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_119`)


Zu Spruchpunkt I. (Stattgabe)  Strittig ist im gegenständlichen Verfahren, ob die künstlerische Tätigkeit des Bf. als Musiker in  den Jahren 2012 bis 2014 eine steuerlich anzuerkennende Einkunftsquelle darstellt oder ob es  sich aus steuerlicher Sicht um eine sog.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_10`)


Nach Gegenüberstellung mit dem bisher vorgeschriebenen Betrag ergibt sich eine Gutschrift  (Differenzbetrag) von -96.796,00 €.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_20`)


Mit Schreiben vom 23.7.2025 stellte die steuerliche Vertretung den Antrag auf Entscheidung  über die Beschwerde (Vorlageantrag) durch das Bundesfinanzgericht betreffend den Bescheid  über Festsetzung von Anspruchszinsen für das Jahr 2021 vom 12.3.2025.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_21`)


Mit Vorlagebericht vom 8.10.2025 legte das Finanzamt die gegenständliche Beschwerde vom  25.3.2025 betreffend Festsetzung von Anspruchszinsen für das Jahr 2021 dem  Bundesfinanzgericht zur Entscheidung vor und beantragte die Abweisung im Wesentlichen wie  folgt:  „Sachverhalt:   Der Beschwerdeführer (Bf) brachte am 21.08.2023 die Einkommensteuererklärung für das Jahr  2021 ein.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_24`)


Die dabei  getroffenen Feststellungen wurden entsprechend in den Einkommensteuerbescheiden der Jahre  2020 und 2021, ergangen am 22.05.2024, berücksichtigt (Erstbescheid).

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_43`)


Erweist sich der genannte Stammabgabenbescheid nachträglich als rechtswidrig und wird er  entsprechend abgeändert (oder aufgehoben), so wird diesem Umstand mit einem an den  Abänderungsbescheid (Aufhebungsbescheid) gebundenen Zinsenbescheid Rechnung getragen.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_49`)


In diesem wurde darüber hinaus der Änderung der Einkommensteuer (Stammabgabe) in der  Beschwerdevorentscheidung Rechnung getragen.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_51`)


II. Das Bundesfinanzgericht hat erwogen:  1. Beweiswürdigung  Der vorstehende Verfahrensgang (Sachverhalt) ergibt sich aus dem gesamten Akteninhalt, dem  Vorlagebericht, den im Abgabeninformationssystem gespeicherten Daten und aus dem  Vorbringen der Parteien.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_54`)


Rechtliche Beurteilung  2.1. Zu Spruchpunkt I. (Abweisung)  § 205 BAO normiert auszugsweise:  Gemäß § 205 Abs. 1 BAO sind Differenzbeträge an Einkommensteuer und Körperschaftsteuer,  die sich aus Abgabenbescheiden unter Außerachtlassung von Anzahlungen (Abs. 3), nach  Gegenüberstellung mit Vorauszahlungen oder mit der bisher festgesetzt gewesenen Abgabe  ergeben, für den Zeitraum ab 1. Oktober des dem Jahr des Entstehens des Abgabenanspruchs  folgenden Jahres bis zum Zeitpunkt der Bekanntgabe dieser Bescheide zu verzinsen  (Anspruchszinsen).

**False Positives:**

- `` — no gold match — likely missing annotation
- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_76`)


Erweist sich der Stammabgabenbescheid nachträglich als rechtswidrig und wird er  entsprechend abgeändert (oder aufgehoben), so wird diesem Umstand mit einem an den  Abänderungsbescheid (Aufhebungsbescheid) gebundenen Zinsenbescheid Rechnung getragen  (z.B. Gutschriftszinsen als Folge des Wegfalles einer rechtswidrigen Nachforderung).

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

**False Positives:**

- `` — partial — pred is substring of gold: `Pensionsversicherungsanstalt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pensionsversicherungsanstalt`(organisation)

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_80`)


Zu Spruchpunkt I. (Abweisung)  § 34 Einkommensteuergesetz 1988 (EStG 1988), BGBl. Nr. 400/1988 idF BGBl. I Nr. 103/2019,  lautet auszugsweise wie folgt:  (1) Bei der Ermittlung des Einkommens (§ 2 Abs. 2) eines unbeschränkt Steuerpflichtigen sind  nach Abzug der Sonderausgaben (§ 18) außergewöhnliche Belastungen abzuziehen.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_20`)


In dieser  Aufstellung müssten alle damaligen Gläubiger der GmbH (auch die zu Gänze bezahlten) sowie  die auf einzelne Verbindlichkeiten (Gläubiger) geleisteten Zahlungen (Quoten) enthalten sein.

**False Positives:**

- `` — no gold match — likely missing annotation
- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_63`)


Reichen die Mittel der Primärschuldnerin nicht aus, die offenen Schuldigkeiten zur Gänze zu  entrichten, so sei der Vertreter grundsätzlich zur Befriedigung der Schulden im gleichen  Verhältnis (anteilig) verpflichtet (Gleichbehandlungsgrundsatz).

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `` — similar text (different position): `Bundesfinanzgerichtes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_3`)


Es wird folgender Säumniszuschlag festgesetzt:    Abgabe Betrag Säumniszuschlag 2%  Umsatzsteuer (Fahrzeugeinzelbesteuerung) 14.218,49 € 284,37 €

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_6`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt gegenüber dem Beschwerdeführer (Bf.)  Normverbrauchsabgabe (NoVA) in Höhe von 11.785,71 Euro und Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro für ein Kraftfahrzeug der Marke  Porsche Cayenne Diesel Platinum Edition (in der Folge: Kfz.) fest.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_8`)


1 und 2 der Bundesabgabenordnung (BAO) in Höhe von jeweils 2 % bzw. 235,71 Euro für die  NoVA und 265,92 Euro für die Umsatzsteuer (Fahrzeugeinzelbesteuerung), insgesamt somit  501,63 Euro.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_10`)


3. In der gegen diesen Bescheid rechtzeitig erhobenen Beschwerde wandte der Bf. durch seine  steuerliche Vertretung ein, die Normverbrauchsabgabe in Höhe von 11.785,71 Euro und die  Umsatzsteuer (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro seien noch nicht  rechtskräftig festgestellt worden und es liege auch noch keine Beschwerdeerledigung vor,  sodass diese Beträge nach wie vor von der Aussetzung der Einhebung gemäß § 212a BAO  umfasst seien.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_17`)


Zur Begründung führte es aus, die Festsetzung der Umsatzsteuer für den  Erwerb neuer Fahrzeuge (Fahrzeugeinzelbesteuerung) 04/2017 in Höhe von 13.295,77 Euro  (Fälligkeitstag 26.05.2017) sei am 30.8.2024 und die Festsetzung der NOVA 04/2017 iHv.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

**False Positives:**

- `` — similar text (different position): `Finanzamt Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Österreich`(organisation)

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_28`)


3. Der Antrag auf Aussetzung der Einhebung der Umsatzsteuer (Fahrzeugeinzelbesteuerung)  wurde mit Bescheid vom 16.10.2024 bewilligt.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_34`)


3. Rechtliche Beurteilung  3.1. Zu Spruchpunkt I. (Abänderung)  1.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_58`)


7. Im Beschwerdefall wurde mit Bescheiden vom 30.8.2024 Normverbrauchsabgabe in Höhe  von 11.785,71 Euro und Umsatzsteuer (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49  4 von 7 Seite 5 von 7

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_61`)


8. Bei der Fahrzeugeinzelbesteuerung hat der Erwerber spätestens bis zum Ablauf eines  Monats, nach dem die Steuerschuld entstanden ist (Fälligkeitstag), eine Steuererklärung  abzugeben, in der er die zu entrichtende Steuer selbst zu berechnen hat.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_64`)


9. Bei der Normverbrauchsabgabe hat in den Fällen des innergemeinschaftlichen Erwerbs  durch Private der Abgabenschuldner spätestens einen Monat ab der Zulassung bzw. dem Tag  des Erwerbs (Fälligkeitstag) eine Anmeldung einzureichen, in der er den zu entrichtenden  Betrag selbst zu berechnen hat (§ 11 Abs. 3 NoVAG 1991;

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_77`)


Säumniszuschlagsverhindernde Gründe im Sinne des § 217 Abs. 4 BAO liegen im Fall der  Festsetzung der Umsatzsteuer (Fahrzeugeinzelbesteuerung) nicht vor.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_78`)


Der Bf. hat gleichzeitig  mit den Beschwerden gegen die Bescheide über die Festsetzung von Normverbrauchsabgabe  und Umsatzsteuer (Fahrzeugeinzelbesteuerung) die Aussetzung dieser Abgaben beantragt.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_83`)


Mit der Verfügung des Ablaufs der Bewilligung der  Aussetzung der Einhebung gemäß § 212 a Abs. 5 BAO lag betreffend die Umsatzsteuer  (Fahrzeugeinzelbesteuerung) kein Grund mehr vor, aus dem keine Säumniszinsen festgesetzt  werden durften.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_103`)


Der Beschwerde war daher teilweise Folge zu leisten und Säumniszinsen nur für die  Umsatzsteuer (Fahrzeugeinzelbesteuerung) in Höhe von 284,37 Euro festzusetzen.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_104`)


3.2. Zu Spruchpunkt II. (Revision)  1.

**False Positives:**

- `` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name_After_Gegen_Herr_Frau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures person names after 'gegen Herrn' or 'gegen Frau' (or 'gegen der/die' with name). Handles cases where the name is not followed immediately by an address.

**Content:**
```
\b(?:gegen\s+Herrn?\s+|gegen\s+Frau\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*(?:\s+von\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00df]+)*)
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

