# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-21T15:50:33.377436

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-21_v3/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2473 |
| Validation documents | 619 |
| Test documents | 12 |
| Train sentences | 4080 |
| Validation sentences | 927 |
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
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

**Transfer Learning**

| Property | Value |
|---|---|
| Best Batch Idx | 8 |
| Best Batch F1 | 0.31213872832369943 |
| Best Rules Serialized | [{'id': 'b3eebc61', 'name': 'post_position_names', 'description': "Matches names following 'in der Beschwerdesache' or similar, stopping before address indicators.", 'format': 'regex', 'content': '(?:in der Beschwerdesache|in der Verwaltungsstrafsache)\\s+([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*(?:\\s+(?:VetR|OSR|StR|Mag\\.|Dr\\.|Dr\\.in|Univ\\.-Prof\\.|Univ\\.-Prof\\.in|Priv\\.-Doz\\.|Priv\\.-Doz\\.in|Hon\\.-Prof\\.|Hon\\.-Prof\\. Dr\\.|PhD|ÖkR|Bakk\\. art\\. MA|BA|RgR|KommR|MSc|Mag\\.a))?\\s+[A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '0ac55225', 'name': 'role_based_identification', 'description': "Matches names following role indicators like 'Beschwerdeführer', 'Beschuldigter', etc., ensuring the name is captured fully.", 'format': 'regex', 'content': '(?:des\\s+Beschwerdeführers|der\\s+Beschwerdeführerin|des\\s+Beschuldigten|der\\s+Beschuldigten|des\\s+Schriftführers|der\\s+Schriftführerin|des\\s+Liquidators|des\\s+Masseverwalters|des\\s+Masseverwalters)(?:,|=|\\s+)([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*)(?:,\\s*(?:LLM|LLB|MSc|BEd|Mag\\.a|Dr\\.in|Dr\\.|MedR|StR|PhD|Bakk\\. art\\. MA|BA|RgR|KommR|VetR|OSR|ÖkR)?)', 'priority': 7, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '82615a08', 'name': 'academic_and_professional_titles_general', 'description': 'Matches German legal and academic titles followed by the full name, including complex titles and suffixes.', 'format': 'regex', 'content': '(?:Mag\\.|Dr\\.|Dr\\.in|Univ\\.-Prof\\.|Univ\\.-Prof\\.in|Priv\\.-Doz\\.|Priv\\.-Doz\\.in|ÖkR|Hon\\.-Prof\\.|Hon\\.-Prof\\. Dr\\.|PhD|StR|Bakk\\. art\\. MA|BA|RgR|KommR|MSc|Mag\\.a|VetR|OSR|OMedR|MedR|Ing\\.|RA|Bakk\\. rer\\. nat\\.)(?:\\s+(?:Mag\\.|Dr\\.|Dr\\.in|Univ\\.-Prof\\.|Univ\\.-Prof\\.in|Priv\\.-Doz\\.|Priv\\.-Doz\\.in|ÖkR|Hon\\.-Prof\\.|Hon\\.-Prof\\. Dr\\.|PhD|StR|Bakk\\. art\\. MA|BA|RgR|KommR|MSc|Mag\\.a|VetR|OSR|OMedR|MedR|Ing\\.|RA|Bakk\\. rer\\. nat\\.)?)*\\s+([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*)(?:,\\s*(?:LLM|LLB|MSc|BEd|Mag\\.a|Dr\\.in|Dr\\.|MedR|StR|PhD|Bakk\\. art\\. MA|BA|RgR|KommR|VetR|OSR|ÖkR|Bakk\\. rer\\. nat\\.)?)?', 'priority': 9, 'output_template': {'text': '$0', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '382e54c9', 'name': 'generic_honorifics', 'description': "Matches names preceded by 'Herr' or 'Frau', including optional suffixes like LLM, MSc, etc.", 'format': 'regex', 'content': '(?:Herr|Frau)\\s+([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*)(?:,\\s*(?:LLM|LLB|MSc|BEd|Mag\\.a|Dr\\.in|Dr\\.|MedR|StR|PhD|Bakk\\. art\\. MA|BA|RgR|KommR|VetR|OSR|ÖkR)?)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'c84a1196', 'name': 'names_after_role_context', 'description': 'Matches names appearing after specific legal case context phrases, stopping before address indicators or commas.', 'format': 'regex', 'content': '(?:in der Beschwerdesache|in der Verwaltungsstrafsache|in der Säumnisbeschwerdesache|in der Beschwerde des|in der Beschwerde der|gegen|für)\\s+([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*(?:\\s+von\\s+[A-Z][a-zäöüß]+)?)', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'f96d0da4', 'name': 'names_after_family_terms', 'description': "Matches names following family relationship terms like 'Tochter', 'Mutter', 'Vater', 'Sohn', 'Ehefrau', 'Ehemann'.", 'format': 'regex', 'content': '(?:Tochter|Mutter|Vater|Sohn|Ehefrau|Ehemann|Eltern|Kind)\\s+([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*(?:\\s+von\\s+[A-Z][a-zäöüß]+)?)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': '208000f1', 'name': 'names_in_headers', 'description': 'Matches names appearing in headers or subject lines, often after colons or hyphens.', 'format': 'regex', 'content': '(?:Betrifft|Betreff|Name|Antragsteller|Beschwerdeführer|Beschwerdeführerin)\\s*[:\\-]\\s*([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*(?:\\s+von\\s+[A-Z][a-zäöüß]+)?)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'c550a5ac', 'name': 'names_with_herr_frau', 'description': "Matches names preceded by 'Herr' or 'Frau', capturing only the name.", 'format': 'regex', 'content': '(?:Herr|Frau)\\s+([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*(?:\\s+von\\s+[A-Z][a-zäöüß]+)?)', 'priority': 8, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}, {'id': 'e66eaaf6', 'name': 'names_with_titles_general', 'description': 'Matches names with specific legal/academic titles (Dr., Mag., OStR, etc.) ensuring full name capture.', 'format': 'regex', 'content': '(?:Dr\\.|Dr\\.in|Mag\\.|Mag\\.a|OStR|OMedR|HR|Hon\\.-Prof\\.|Hon\\.-Prof\\. Dr\\.|Univ\\.-Prof\\.|Univ\\.-Prof\\.in|Priv\\.-Doz\\.|Priv\\.-Doz\\.in|Ing\\.|RA|Bakk\\. art\\. MA|BA|RgR|KommR|MSc|LLM|LLB|BEd|VetR|OSR|\\u00d6kR)\\s+([A-Z][a-zäöüß]+(?:\\s+[A-Z][a-zäöüß]+)*(?:\\s+von\\s+[A-Z][a-zäöüß]+)?)', 'priority': 9, 'output_template': {'text': '$1', 'start': '$start', 'end': '$end', 'type': 'person'}, 'output_key': 'entities'}] |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 93.9% |
| True Positives | 27 |
| False Positives | 56 |
| False Negatives | 63 |
| Total Gold Entities | 90 |
| Micro Precision | 32.5% |
| Micro Recall | 30.0% |
| Micro F1 | 31.2% |
| Macro F1 | 31.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `post_position_names` | 18.2% | 100.0% | 10.0% | 9 | 9 | 0 |
| `academic_and_professional_titles_general` | 19.5% | 47.8% | 12.2% | 23 | 11 | 12 |
| `names_with_herr_frau` | 8.0% | 40.0% | 4.4% | 10 | 4 | 6 |
| `names_after_role_context` | 16.1% | 29.4% | 11.1% | 34 | 10 | 24 |
| `names_after_family_terms` | 3.8% | 14.3% | 2.2% | 14 | 2 | 12 |
| `role_based_identification` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `generic_honorifics` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
| `names_in_headers` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `names_with_titles_general` | 0.0% | 0.0% | 0.0% | 26 | 0 | 26 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `post_position_names`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Rule ID:** `b3eebc61`  
**Description:**
Matches names following 'in der Beschwerdesache' or similar, stopping before address indicators.

**Content:**
```
(?:in der Beschwerdesache|in der Verwaltungsstrafsache)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:VetR|OSR|StR|Mag\.|Dr\.|Dr\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|PhD|ÖkR|Bakk\. art\. MA|BA|RgR|KommR|MSc|Mag\.a))?\s+[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
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

## `academic_and_professional_titles_general`

**F1:** 0.195 | **Precision:** 0.478 | **Recall:** 0.122  

**Format:** `regex`  
**Rule ID:** `82615a08`  
**Description:**
Matches German legal and academic titles followed by the full name, including complex titles and suffixes.

**Content:**
```
(?:Mag\.|Dr\.|Dr\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|ÖkR|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|PhD|StR|Bakk\. art\. MA|BA|RgR|KommR|MSc|Mag\.a|VetR|OSR|OMedR|MedR|Ing\.|RA|Bakk\. rer\. nat\.)(?:\s+(?:Mag\.|Dr\.|Dr\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|ÖkR|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|PhD|StR|Bakk\. art\. MA|BA|RgR|KommR|MSc|Mag\.a|VetR|OSR|OMedR|MedR|Ing\.|RA|Bakk\. rer\. nat\.)?)*\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)(?:,\s*(?:LLM|LLB|MSc|BEd|Mag\.a|Dr\.in|Dr\.|MedR|StR|PhD|Bakk\. art\. MA|BA|RgR|KommR|VetR|OSR|ÖkR|Bakk\. rer\. nat\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.478 | 0.122 | 0.195 | 23 | 11 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 12 | 79 |

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `BA Sozial` — no gold match — likely missing annotation
- `BA Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

**False Positives:**

- `BA Sozial` — no gold match — likely missing annotation
- `BA Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `BA Sozial` — no gold match — likely missing annotation
- `BA Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Johannes Kepler  Universität Linz`(organisation)
- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

**False Positives:**

- `BA Sozial` — no gold match — likely missing annotation
- `BA Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

</details>

---

## `names_after_role_context`

**F1:** 0.161 | **Precision:** 0.294 | **Recall:** 0.111  

**Format:** `regex`  
**Rule ID:** `c84a1196`  
**Description:**
Matches names appearing after specific legal case context phrases, stopping before address indicators or commas.

**Content:**
```
(?:in der Beschwerdesache|in der Verwaltungsstrafsache|in der Säumnisbeschwerdesache|in der Beschwerde des|in der Beschwerde der|gegen|für)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.294 | 0.111 | 0.161 | 34 | 10 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 10 | 24 | 80 |

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

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_49`)


In dieser Zeit  haben der Onkel … und seine Frau … die Kosten für Essen und Logie getragen.

**False Positives:**

- `Essen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_73`)


Sodann zog Maximiliane Sakschewsky, MA  zu einem Onkel des  Ziehvaters nach Worcester (und haben in dieser Zeit der Onkel und dessen Frau die Kosten für  Essen und Logie getragen).

**False Positives:**

- `Essen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_86`)


Der Bf. erfüllte die alternativ zu beurteilende Voraussetzung, die Unterhaltskosten für  Maximiliane Sakschewsky, MA  überwiegend zu tragen, wie oben unter Punkt 2. ausgeführt, nicht.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Betrugsbekämpfung` — partial — pred is substring of gold: `Amtes für Betrugsbekämpfung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `names_with_titles_general`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e66eaaf6`  
**Description:**
Matches names with specific legal/academic titles (Dr., Mag., OStR, etc.) ensuring full name capture.

**Content:**
```
(?:Dr\.|Dr\.in|Mag\.|Mag\.a|OStR|OMedR|HR|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Ing\.|RA|Bakk\. art\. MA|BA|RgR|KommR|MSc|LLM|LLB|BEd|VetR|OSR|\u00d6kR)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 26 | 0 | 26 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 26 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Siegfried Fenz` — partial — pred is substring of gold: `Dr. Siegfried Fenz`
- `Julius Wagner` — partial — pred is substring of gold: `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Ashley Partenfelder` — partial — pred is substring of gold: `Mag. Ashley Partenfelder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

</details>

---

## `names_after_family_terms`

**F1:** 0.038 | **Precision:** 0.143 | **Recall:** 0.022  

**Format:** `regex`  
**Rule ID:** `f96d0da4`  
**Description:**
Matches names following family relationship terms like 'Tochter', 'Mutter', 'Vater', 'Sohn', 'Ehefrau', 'Ehemann'.

**Content:**
```
(?:Tochter|Mutter|Vater|Sohn|Ehefrau|Ehemann|Eltern|Kind)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.143 | 0.022 | 0.038 | 14 | 2 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 12 | 88 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_6`)


Aufgrund eines Arbeitsauftrages vom 21.05.2021 kam es zu einer Überprüfung des  Familienbeihilfe-Anspruches der Beschwerdeführerin (=Bf.) bezüglich ihrer Tochter  Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum, da zunächst aufgrund der COVID-Pandemie  sowohl Anspruchsüberprüfungen als auch Rückforderungen ausgesetzt worden waren.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_50`)


Mit Vorlagebericht vom 26.07.2022 legte die belangte Behörde die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor und führte dazu aus:  „Sachverhalt:  Aufgrund eines Arbeitsauftrages vom 21.05.2021 sollte der Familienbeihilfe-Anspruch der  Beschwerdeführerin bezüglich ihrer Tochter Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum  überprüft werden.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_28`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die BF bezog im streitgegenständlichen Zeitraum Familienbeihilfe und Kinderabsetzbeträge für  ihre Tochter Stella Marschalk, Bakk. techn. (geboren im September 1998).

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)
- `September 1998`(date)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_9`)


Die Beschwerde wurde mit folgender Begründung erhoben:  Klarstellung: Der Zeitraum der beantragten Familienbeihilfe ist von 01.06.2019 bis 30.09.2020  für meine Tochter Maximiliane Sakschewsky, MA (Nachname wie Bf.) (geboren am … .12.2001).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

</details>

---

## `generic_honorifics`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `382e54c9`  
**Description:**
Matches names preceded by 'Herr' or 'Frau', including optional suffixes like LLM, MSc, etc.

**Content:**
```
(?:Herr|Frau)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)(?:,\s*(?:LLM|LLB|MSc|BEd|Mag\.a|Dr\.in|Dr\.|MedR|StR|PhD|Bakk\. art\. MA|BA|RgR|KommR|VetR|OSR|ÖkR)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 6 | 83 |

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

## `names_with_herr_frau`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Rule ID:** `c550a5ac`  
**Description:**
Matches names preceded by 'Herr' or 'Frau', capturing only the name.

**Content:**
```
(?:Herr|Frau)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
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

## `role_based_identification`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0ac55225`  
**Description:**
Matches names following role indicators like 'Beschwerdeführer', 'Beschuldigter', etc., ensuring the name is captured fully.

**Content:**
```
(?:des\s+Beschwerdeführers|der\s+Beschwerdeführerin|des\s+Beschuldigten|der\s+Beschuldigten|des\s+Schriftführers|der\s+Schriftführerin|des\s+Liquidators|des\s+Masseverwalters|des\s+Masseverwalters)(?:,|=|\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)(?:,\s*(?:LLM|LLB|MSc|BEd|Mag\.a|Dr\.in|Dr\.|MedR|StR|PhD|Bakk\. art\. MA|BA|RgR|KommR|VetR|OSR|ÖkR)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `names_in_headers`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `208000f1`  
**Description:**
Matches names appearing in headers or subject lines, often after colons or hyphens.

**Content:**
```
(?:Betrifft|Betreff|Name|Antragsteller|Beschwerdeführer|Beschwerdeführerin)\s*[:\-]\s*([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
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

## `academic_and_professional_titles_general`

**F1:** 0.195 | **Precision:** 0.478 | **Recall:** 0.122  

**Format:** `regex`  
**Rule ID:** `82615a08`  
**Description:**
Matches German legal and academic titles followed by the full name, including complex titles and suffixes.

**Content:**
```
(?:Mag\.|Dr\.|Dr\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|ÖkR|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|PhD|StR|Bakk\. art\. MA|BA|RgR|KommR|MSc|Mag\.a|VetR|OSR|OMedR|MedR|Ing\.|RA|Bakk\. rer\. nat\.)(?:\s+(?:Mag\.|Dr\.|Dr\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|ÖkR|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|PhD|StR|Bakk\. art\. MA|BA|RgR|KommR|MSc|Mag\.a|VetR|OSR|OMedR|MedR|Ing\.|RA|Bakk\. rer\. nat\.)?)*\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)(?:,\s*(?:LLM|LLB|MSc|BEd|Mag\.a|Dr\.in|Dr\.|MedR|StR|PhD|Bakk\. art\. MA|BA|RgR|KommR|VetR|OSR|ÖkR|Bakk\. rer\. nat\.)?)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.478 | 0.122 | 0.195 | 23 | 11 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 12 | 79 |

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `BA Sozial` — no gold match — likely missing annotation
- `BA Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

**False Positives:**

- `BA Sozial` — no gold match — likely missing annotation
- `BA Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `BA Sozial` — no gold match — likely missing annotation
- `BA Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Johannes Kepler  Universität Linz`(organisation)
- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

**False Positives:**

- `BA Sozial` — no gold match — likely missing annotation
- `BA Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `StR Tosca Knoller,  ` — positional overlap with gold: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Katrin Allram` — partial — pred is substring of gold: `Mag.Dr. Katrin Allram`

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

## `post_position_names`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Rule ID:** `b3eebc61`  
**Description:**
Matches names following 'in der Beschwerdesache' or similar, stopping before address indicators.

**Content:**
```
(?:in der Beschwerdesache|in der Verwaltungsstrafsache)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+(?:VetR|OSR|StR|Mag\.|Dr\.|Dr\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|PhD|ÖkR|Bakk\. art\. MA|BA|RgR|KommR|MSc|Mag\.a))?\s+[A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)
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

## `names_after_role_context`

**F1:** 0.161 | **Precision:** 0.294 | **Recall:** 0.111  

**Format:** `regex`  
**Rule ID:** `c84a1196`  
**Description:**
Matches names appearing after specific legal case context phrases, stopping before address indicators or commas.

**Content:**
```
(?:in der Beschwerdesache|in der Verwaltungsstrafsache|in der Säumnisbeschwerdesache|in der Beschwerde des|in der Beschwerde der|gegen|für)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.294 | 0.111 | 0.161 | 34 | 10 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 10 | 24 | 80 |

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

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Renate Brombusch` | `Renate Brombusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Juliana Bartjen` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


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

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


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

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


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

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_49`)


In dieser Zeit  haben der Onkel … und seine Frau … die Kosten für Essen und Logie getragen.

**False Positives:**

- `Essen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_73`)


Sodann zog Maximiliane Sakschewsky, MA  zu einem Onkel des  Ziehvaters nach Worcester (und haben in dieser Zeit der Onkel und dessen Frau die Kosten für  Essen und Logie getragen).

**False Positives:**

- `Essen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_86`)


Der Bf. erfüllte die alternativ zu beurteilende Voraussetzung, die Unterhaltskosten für  Maximiliane Sakschewsky, MA  überwiegend zu tragen, wie oben unter Punkt 2. ausgeführt, nicht.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Betrugsbekämpfung` — partial — pred is substring of gold: `Amtes für Betrugsbekämpfung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_6`)


Entscheidungsgründe  Verfahrensgang:  Mit Erkenntnis des Spruchsenates I-1 als Organ des Amtes für Betrugsbekämpfung als  Finanzstrafbehörde vom 2. Mai 2024 wurde der Beschwerdeführer (in der Folge kurz: Bf.) der  Finanzvergehen a) der Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG und b) der  Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG für schuldig erkannt.

**False Positives:**

- `Betrugsbekämpfung` — partial — pred is substring of gold: `Amtes für Betrugsbekämpfung`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Amtes für Betrugsbekämpfung`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_12`)


Diesen Antrag vom 25.11.2024 hat das Amt für Betrugsbekämpfung mit Bescheid vom 02.  Dezember 2024 abgewiesen.

**False Positives:**

- `Betrugsbekämpfung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_32`)


Gemäß § 212 Abs. 1 BAO kann die Abgabenbehörde auf Ansuchen des Abgabepflichtigen für  Abgaben, hinsichtlich derer ihm gegenüber auf Grund eines Rückstandsausweises (§ 229)  Einbringungsmaßnahmen für den Fall des bereits erfolgten oder späteren Eintrittes aller  Voraussetzungen hiezu in Betracht kommen, den Zeitpunkt der Entrichtung der Abgaben  hinausschieben (Stundung) oder die Entrichtung in Raten bewilligen, wenn die sofortige oder  die sofortige volle Entrichtung der Abgaben für den Abgabepflichtigen mit erheblichen Härten  verbunden wäre und die Einbringlichkeit der Abgaben durch den Aufschub nicht gefährdet  wird.

**False Positives:**

- `Abgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Wien Nr` — no gold match — likely missing annotation
- `Wien Nr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_131`)


Diese Bestimmung gilt einerseits für typische Hobbytätigkeiten, wie z.B. die  Hobbymalerei, sowie andererseits auch für Tätigkeiten, die ihrer Art nach an sich typisch  erwerbswirtschaftlich sind, jedoch im Hinblick auf ihren Umfang nicht erwerbstypisch ausgeübt  werden.

**False Positives:**

- `Tätigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_144`)


In Anbetracht der Tatsache, dass der Bf. die in Rede stehende Tätigkeit 2014, aufgrund des  Rückganges der Aufträge und der Tatsache, dass es für ihn immer schwieriger wurde Aufträge  für Auftritte zu erhalten, durch seine betriebswirtschaftlich sinnvolle Entscheidung, beendet  hat und in dem gesamten Betätigungszeitraum (hier von 1975 bis 2014) ein Gesamtüberschuss  erwirtschaftet (laut BVE geht das Finanzamt nicht vom Vorliegen einer Gesamtverlustes über  den gesamten Tätigkeitszeitraum aus) wurde, kann laut Ansicht des BFG keine Liebhaberei  vorliegen.

**False Positives:**

- `Auftritte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_25`)


Dem Vorlageantrag war ein ärztlicher Befund eines Arztes für  Allgemeinmedizin vom 16. April 2024 sowie eine Bestätigung eines Facharztes für Unfall- und  Neurochirurgie vom 18. April 2024 angeschlossen.

**False Positives:**

- `Allgemeinmedizin` — no gold match — likely missing annotation
- `Unfall` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_109`)


Bloße Wünsche und Vorstellungen der Betroffenen über eine bestimmte medizinische  Behandlung sowie allgemein gehaltene Befürchtungen bezüglich der vom Träger der  gesetzlichen Krankenversicherung finanzierten medizinischen Betreuung stellen noch keine  triftigen medizinischen Gründe für Aufwendungen dar, welche die durch die gesetzliche  Krankenversicherung gedeckten Kosten übersteigen.

**False Positives:**

- `Aufwendungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_95`)


Eine Ausnahme vom Gleichheitsgrundsatz bestehe für Abfuhrabgaben, wie die Lohnsteuer  (VwGH 29.6.1999, 99/14/0040;

**False Positives:**

- `Abfuhrabgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_102`)


Eine weitere Ausnahme vom Gleichheitsgrundsatz bestehe für Abfuhrabgaben, wie die  Kapitalertragsteuer (VwGH 16.2.2000, 95/15/0046).

**False Positives:**

- `Abfuhrabgaben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_182`)


Im Beschwerdefall steht sogar die Uneinbringlichkeit der haftungsgegenständlichen Abgaben,  fest, da mit Beschluss des Landesgerichtes für Zivilrechtssachen vom 12.9.2023 die  Nichteröffnung eines Insolvenzverfahrens mangels kostendeckenden Vermögens festgestellt  wurde.

**False Positives:**

- `Zivilrechtssachen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_189`)


Er hat also darzutun, weshalb er nicht dafür Sorge tragen  konnte, dass die Gesellschaft die anfallenden Abgaben rechtzeitig entrichtet hat, andernfalls  von der Abgabenbehörde eine schuldhafte Pflichtverletzung angenommen werden darf (vgl.  VwGH 16.12.2009, 2009/15/0127).

**False Positives:**

- `Sorge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_45`)


(4) Säumniszuschläge sind für Abgabenschuldigkeiten insoweit nicht zu entrichten, als   a) ihre Einhebung gemäß § 212a ausgesetzt ist,  b) ihre Einbringung gemäß § 230 Abs. 2, 3, 5 oder 6 gehemmt ist,  c) ein Zahlungsaufschub im Sinn des § 212 Abs. 2 zweiter Satz nicht durch Ausstellung eines  Rückstandsausweises (§ 229) als beendet gilt,  d) ihre Einbringung gemäß § 231 ausgesetzt ist.

**False Positives:**

- `Abgabenschuldigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_57`)


22.2.2024, RV/7100415/2023) bestehen keine Bedenken, wenn über  Beschwerden gegen Säumniszuschläge entschieden wird, obwohl über die gegen die  Stammabgabenbescheide gerichteten Beschwerden noch nicht abgesprochen wurde.

**False Positives:**

- `Säumniszuschläge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_69`)


Da er dieser Verpflichtung nicht  nachgekommen ist, ist er säumig geworden und hatte er dafür Säumniszuschläge zu  entrichten.

**False Positives:**

- `Säumniszuschläge` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_98`)


Denn  gemäß § 217 Abs. 4 BAO sind Säumniszuschläge für Abgabenschuldigkeiten nur insoweit nicht  zu entrichten, als die in den Absätzen 1-4 leg. cit.

**False Positives:**

- `Abgabenschuldigkeiten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `names_with_herr_frau`

**F1:** 0.080 | **Precision:** 0.400 | **Recall:** 0.044  

**Format:** `regex`  
**Rule ID:** `c550a5ac`  
**Description:**
Matches names preceded by 'Herr' or 'Frau', capturing only the name.

**Content:**
```
(?:Herr|Frau)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
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

## `names_after_family_terms`

**F1:** 0.038 | **Precision:** 0.143 | **Recall:** 0.022  

**Format:** `regex`  
**Rule ID:** `f96d0da4`  
**Description:**
Matches names following family relationship terms like 'Tochter', 'Mutter', 'Vater', 'Sohn', 'Ehefrau', 'Ehemann'.

**Content:**
```
(?:Tochter|Mutter|Vater|Sohn|Ehefrau|Ehemann|Eltern|Kind)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.143 | 0.022 | 0.038 | 14 | 2 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 12 | 88 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_6`)


Aufgrund eines Arbeitsauftrages vom 21.05.2021 kam es zu einer Überprüfung des  Familienbeihilfe-Anspruches der Beschwerdeführerin (=Bf.) bezüglich ihrer Tochter  Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum, da zunächst aufgrund der COVID-Pandemie  sowohl Anspruchsüberprüfungen als auch Rückforderungen ausgesetzt worden waren.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_50`)


Mit Vorlagebericht vom 26.07.2022 legte die belangte Behörde die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor und führte dazu aus:  „Sachverhalt:  Aufgrund eines Arbeitsauftrages vom 21.05.2021 sollte der Familienbeihilfe-Anspruch der  Beschwerdeführerin bezüglich ihrer Tochter Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum  überprüft werden.

| Predicted | Gold |
|---|---|
| `Viktoria Immohr` | `Viktoria Immohr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_28`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die BF bezog im streitgegenständlichen Zeitraum Familienbeihilfe und Kinderabsetzbeträge für  ihre Tochter Stella Marschalk, Bakk. techn. (geboren im September 1998).

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)
- `September 1998`(date)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_9`)


Die Beschwerde wurde mit folgender Begründung erhoben:  Klarstellung: Der Zeitraum der beantragten Familienbeihilfe ist von 01.06.2019 bis 30.09.2020  für meine Tochter Maximiliane Sakschewsky, MA (Nachname wie Bf.) (geboren am … .12.2001).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_15`)


Unbeschadet dieses  Umstandes habe ich sämtliche Unterhaltskosten für meine Tochter Maximiliane Sakschewsky, MA, wie  bereits seit Ihren Aufenthaltswechsel im Jahr 2014 in das Vereinigte Königreich, im  Antragszeitraum noch EU-Mitgliedstaat, weiter getragen.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Vereinigte Königreich`(country)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_20`)


Gemäß obigen Ausführungen ist meine Tochter Maximiliane Sakschewsky, MA  seit Sommer 2014,  ausgenommen ferienbedingte Abwesenheiten, in Vereinigten Königreich wohnhaft.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_23`)


Die Beschwerdevorlage erfolgte mit nachstehendem Sachverhalt und Anträgen:  Sachverhalt:  Der Bf stellte einen Antrag auf Gewährung der Familienbeihilfe für seine Tochter  Maximiliane Sakschewsky, MA  ab Juni 2019.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_61`)


Am 23. Oktober 2020 überwies der Bf. auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN  GB…1084 € 200,00 mit dem Verwendungszweck: Unterstützung, am 4. November 2020  € 500,00 am 25. und 30. November jeweils € 200,00.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_81`)


Unter Bedachtnahme auf das eigene Vorbringen des Bf.: ‚Ich habe monatlich € 1.000,- an  meine Ex-Gattin überwiesen, die als Schulgeld galten.‘ und den Umstand, dass diese  Überweisungen für beide Töchter erfolgt waren, bedarf es auf Basis der obigen Feststellungen  keiner weiteren Ausführungen, dass mit den Leistungen des Bf. nicht die überwiegenden  Unterhaltskosten seiner (17 ½- bis 18 ½- jährigen) Tochter Maximiliane Sakschewsky, MA, die ab Mai 2019  bei einem Onkel ihres Ziehvaters und dessen Frau (in Worcester) und sodann zeitweilig (der Bf.  spricht von 1 Monat) bei der Mutter ihres Freundes lebte, abgedeckt worden sind.

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

</details>

---

## `role_based_identification`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0ac55225`  
**Description:**
Matches names following role indicators like 'Beschwerdeführer', 'Beschuldigter', etc., ensuring the name is captured fully.

**Content:**
```
(?:des\s+Beschwerdeführers|der\s+Beschwerdeführerin|des\s+Beschuldigten|der\s+Beschuldigten|des\s+Schriftführers|der\s+Schriftführerin|des\s+Liquidators|des\s+Masseverwalters|des\s+Masseverwalters)(?:,|=|\s+)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)(?:,\s*(?:LLM|LLB|MSc|BEd|Mag\.a|Dr\.in|Dr\.|MedR|StR|PhD|Bakk\. art\. MA|BA|RgR|KommR|VetR|OSR|ÖkR)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `generic_honorifics`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `382e54c9`  
**Description:**
Matches names preceded by 'Herr' or 'Frau', including optional suffixes like LLM, MSc, etc.

**Content:**
```
(?:Herr|Frau)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*)(?:,\s*(?:LLM|LLB|MSc|BEd|Mag\.a|Dr\.in|Dr\.|MedR|StR|PhD|Bakk\. art\. MA|BA|RgR|KommR|VetR|OSR|ÖkR)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 6 | 83 |

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

## `names_in_headers`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `208000f1`  
**Description:**
Matches names appearing in headers or subject lines, often after colons or hyphens.

**Content:**
```
(?:Betrifft|Betreff|Name|Antragsteller|Beschwerdeführer|Beschwerdeführerin)\s*[:\-]\s*([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `names_with_titles_general`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e66eaaf6`  
**Description:**
Matches names with specific legal/academic titles (Dr., Mag., OStR, etc.) ensuring full name capture.

**Content:**
```
(?:Dr\.|Dr\.in|Mag\.|Mag\.a|OStR|OMedR|HR|Hon\.-Prof\.|Hon\.-Prof\. Dr\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Ing\.|RA|Bakk\. art\. MA|BA|RgR|KommR|MSc|LLM|LLB|BEd|VetR|OSR|\u00d6kR)\s+([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+von\s+[A-Z][a-zäöüß]+)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 26 | 0 | 26 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 26 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Siegfried Fenz` — partial — pred is substring of gold: `Dr. Siegfried Fenz`
- `Julius Wagner` — partial — pred is substring of gold: `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Ashley Partenfelder` — partial — pred is substring of gold: `Mag. Ashley Partenfelder`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `Sozial` — no gold match — likely missing annotation
- `Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

**False Positives:**

- `Sozial` — no gold match — likely missing annotation
- `Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `Sozial` — no gold match — likely missing annotation
- `Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Johannes Kepler  Universität Linz`(organisation)
- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

**False Positives:**

- `Sozial` — no gold match — likely missing annotation
- `Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

**False Positives:**

- `Farina Kohlstrunk` — partial — pred is substring of gold: `Priv.-Doz.in Farina Kohlstrunk`
- `Andr` — partial — pred is substring of gold: `Mag. András Péter Radics`

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

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Quirin Januszis` — partial — pred is substring of gold: `Priv.-Doz. Quirin Januszis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Gabriele Friedbacher` — partial — pred is substring of gold: `Mag. Gabriele Friedbacher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Juliana Bartjen` — partial — pred is substring of gold: `Priv.-Doz.in Juliana Bartjen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Estelle Niederholz` — partial — pred is substring of gold: `Dr.in Estelle Niederholz`
- `Tosca Knoller` — partial — pred is substring of gold: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Thassilo Averdiek` — partial — pred is substring of gold: `Hon.-Prof. Thassilo Averdiek`

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

- `Katrin Allram` — partial — pred is substring of gold: `Mag.Dr. Katrin Allram`

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

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dagobert Nordholt` — partial — pred is substring of gold: `Dr. Dagobert Nordholt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dagobert Nordholt`(person)
- `Dieter Leufkes`(person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich`(address)
- `FA Kirchdorf Perg Steyr`(organisation)
- `36-532/2242`(tax_number)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

**False Positives:**

- `Peter Bilger` — partial — pred is substring of gold: `Mag. Peter Bilger`

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

