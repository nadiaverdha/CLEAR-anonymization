# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-19T22:37:20.959559

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-05-19_v1/config.yaml 
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
| Max rules | 15 |
| Max samples in prompt | 60 |
| Refinement iterations | 0 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | True |
| Critic Interval | 10 |
| Audit Interval | 0 |
| Use GREX | True |
| Format | regex |
| Synthesis strategy | bulk |
| Sampling strategy | balanced |
| Batch size | 40 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 37.9% |
| True Positives | 2 |
| False Positives | 1787 |
| False Negatives | 88 |
| Total Gold Entities | 90 |
| Micro Precision | 0.1% |
| Micro Recall | 2.2% |
| Micro F1 | 0.2% |
| Macro F1 | 0.2% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `person_simple_name_context` | 18.2% | 100.0% | 10.0% | 9 | 9 | 0 |
| `person_after_preposition` | 0.3% | 0.2% | 1.1% | 491 | 1 | 490 |
| `person_genitive_simple` | 0.1% | 0.1% | 1.1% | 1285 | 1 | 1284 |
| `person_complex_title_in_case` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `person_after_genitive_role` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `person_title_prefix_general` | 0.0% | 0.0% | 0.0% | 21 | 0 | 21 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `person_simple_name_context`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Description:**
Captures simple names (First Last) in contexts like 'in der Beschwerdesache' where no title is present. Uses numbered capture group.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Revisionssache|Verwaltungsstrafsache|Verfahren|Sache)\s+)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s*,|\s+\n|\s+\d+|\u00d6sterreich|\s*\(|\s*\)|\s*\.|\s*"|\s*'|\s+\s|$|\s+sei|\s+ist|\s+hat|\s+war|\s+GmbH|\s+KG|\s+AG|\s+OHG|\s+UG|\s+GmbH\s*&|\s+GmbH\s*&\s*Co|\s+vertreten)
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

## `person_genitive_simple`

**F1:** 0.001 | **Precision:** 0.001 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures names following genitive markers 'der' or 'des' (e.g., 'des Hilde Lederhas'). Uses numbered capture group.

**Content:**
```
(?:des\s+|der\s+)(?:VetR\s+|StR\s+|Hon\.-Prof\.(?:in)?\s+|Priv\.-Doz\.(?:in)?\s+|Univ\.-Prof\.(?:in)?\s+|Dr\.(?:in)?\s+|Mag\.(?:in)?\s+|OStR\s+|OSR\s+|MedR\s+|Techn\s+R\s+|HR\s+|Senatsvorsitzender\s+|Senatsvorsitzende\s+|Dipl\.-Ing\.(?:in)?\s+|RgR\s+|StB\s+|Stb\s+|OMedR\s+|B\.?A\.?\s+iur\s+|Bakk\.\s+art\.\s+MA\s+|techn\.\s+|KommR\s+|KzlR\s+|Ing\.(?:in)?\s+|Dipl\.(?:in)?\s+|Bakk\.(?:in)?\s+|PhD\s+|LLB\s+|LL\.M\s+|MSc\s+|MAS\s+|DDr\.(?:in)?\s+|Prof\.(?:in)?\s+|Ri\s+|\u00d6kR\s+|HR\s+KzlR\s+|Herr\s+|Frau\s+|Herrn\s+|Frauen\s+)?([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|LLB|LL\.M|MSc|PhD|Dr\.|Mag\.|Mag\.a|Mag\.in|Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|KommR|KzlR|Ing\.|Dipl\.-Ing\.|RgR|StB|Stb|MAS|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|OMedR|MedR|Dr\.in|DDr\.in|Bakk\.\s+rer\.\s+nat\.)\s*)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.001 | 0.011 | 0.001 | 1285 | 1 | 1284 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 1284 | 89 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`
- `FA Graz` — partial — pred is substring of gold: `FA Graz-Stadt`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_4`)


Am 30.09.2019 langte beim Finanzamt die Antwort der Beschwerdeführerin (in der Folge BF)  auf ein Überprüfungsschreiben des Anspruches auf Familienbeihilfe ein.

**False Positives:**

- `Beschwerdeführerin` — no gold match — likely missing annotation
- `Folge BF` — no gold match — likely missing annotation
- `Anspruches` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Ergänzungsersuchens` — no gold match — likely missing annotation
- `Schule` — partial — pred is substring of gold: `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`
- `Zeit` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_8`)


insgesamt 1.781,80 Euro von der BF zurück.

**False Positives:**

- `BF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

**False Positives:**

- `Schule` — partial — pred is substring of gold: `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`(organisation)

</details>

---

## `person_after_preposition`

**F1:** 0.003 | **Precision:** 0.002 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures names following prepositions like 'von', 'durch', 'gegen', 'in', 'an', 'bei', 'nach', 'zu', 'auf'. Uses numbered capture group.

**Content:**
```
(?:von|durch|gegen|in|an|bei|nach|zu|auf)\s+(?:VetR\s+|StR\s+|Hon\.-Prof\.(?:in)?\s+|Priv\.-Doz\.(?:in)?\s+|Univ\.-Prof\.(?:in)?\s+|Dr\.(?:in)?\s+|Mag\.(?:in)?\s+|OStR\s+|OSR\s+|MedR\s+|Techn\s+R\s+|HR\s+|Senatsvorsitzender\s+|Senatsvorsitzende\s+|Dipl\.-Ing\.(?:in)?\s+|RgR\s+|StB\s+|Stb\s+|OMedR\s+|B\.?A\.?\s+iur\s+|Bakk\.\s+art\.\s+MA\s+|techn\.\s+|KommR\s+|KzlR\s+|Ing\.(?:in)?\s+|Dipl\.(?:in)?\s+|Bakk\.(?:in)?\s+|PhD\s+|LLB\s+|LL\.M\s+|MSc\s+|MAS\s+|DDr\.(?:in)?\s+|Prof\.(?:in)?\s+|Ri\s+|\u00d6kR\s+|HR\s+KzlR\s+|Herr\s+|Frau\s+|Herrn\s+|Frauen\s+)?([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|LLB|LL\.M|MSc|PhD|Dr\.|Mag\.|Mag\.a|Mag\.in|Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|KommR|KzlR|Ing\.|Dipl\.-Ing\.|RgR|StB|Stb|MAS|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|OMedR|MedR|Dr\.in|DDr\.in|Bakk\.\s+rer\.\s+nat\.)\s*)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.002 | 0.011 | 0.003 | 491 | 1 | 490 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 490 | 89 |

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

- `Unrecht` — no gold match — likely missing annotation
- `Familienbeihilfe` — no gold match — likely missing annotation
- `Höhe` — no gold match — likely missing annotation
- `Recht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Art` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_4`)


Am 30.09.2019 langte beim Finanzamt die Antwort der Beschwerdeführerin (in der Folge BF)  auf ein Überprüfungsschreiben des Anspruches auf Familienbeihilfe ein.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Schreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_7`)


3. Mit Bescheid vom 12.11.2019 forderte das Finanzamt die für den Zeitraum von November  2017 bis Juni 2018 bezogenen Beträge an Familienbeihilfe und Kinderabsetzbeträgen iHv.

**False Positives:**

- `November` — no gold match — likely missing annotation
- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `person_title_prefix_general`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names starting with specific titles like ÖkR, HR, Priv.-Doz. in any context. Uses numbered capture group.

**Content:**
```
(?:ÖkR|HR|Priv\.-Doz\.|Priv\.-Doz\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Dr\.|Dr\.in|DDr\.|DDr\.in|Mag\.|Mag\.a|Mag\.in|Mag\.Dr\.|Prof\.|Ri|OStR|Senatsvorsitzender|Senatsvorsitzende|Dipl\.-Ing\.|Dipl\.|Ing\.|Bakk\.|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|VetR\s+|KommR|KzlR|OMedR|MedR|OSR|StB|Stb|LLB|LL\.M|MSc|MAS|PhD|LL\.M)\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|LLB|LL\.M|MSc|PhD|Dr\.|Mag\.|Mag\.a|Mag\.in|Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|KommR|KzlR|Ing\.|Dipl\.-Ing\.|RgR|StB|Stb|MAS|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|OMedR|MedR|Dr\.in|DDr\.in|Bakk\.\s+rer\.\s+nat\.)\s*)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 21 | 0 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 21 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`
- `Gotthard Clement` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

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

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `person_complex_title_in_case`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names with complex titles (Dr., Hon.-Prof., etc.) following 'durch den Richter' or 'in der Beschwerdesache'. Uses numbered capture group for the name.

**Content:**
```
(?:durch\s+(?:den\s+Richter|die\s+Richterin)|in\s+der\s+(?:Beschwerdesache|Revisionssache|Verwaltungsstrafsache|Verfahren|Sache)\s+)(?:Hon\.-Prof\.(?:\s+Priv\.-Doz\.)?|Priv\.-Doz\.(?:\.in)?|Univ\.-Prof\.(?:\.in)?|Dr\.(?:in)?|Mag\.(?:\.in)?|OStR|OSR|MedR|Techn\s+R|HR\s+|Senatsvorsitzender|Senatsvorsitzende|Dipl\.-Ing\.|RgR|StB|Stb|OMedR|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|VetR\s+|KommR|KzlR|Ing\.|Dipl\.|Bakk\.|PhD|LLB|LL\.M|MSc|MAS|DDr\.(?:in)?|Prof\.|Ri|\u00d6kR|HR\s+KzlR|Herr|Frau|Herrn|Frauen)\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|LLB|LL\.M|MSc|PhD|Dr\.|Mag\.|Mag\.a|Mag\.in|Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|KommR|KzlR|Ing\.|Dipl\.-Ing\.|RgR|StB|Stb|MAS|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|OMedR|MedR|Dr\.in|DDr\.in|Bakk\.\s+rer\.\s+nat\.)\s*)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `person_after_genitive_role`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following genitive role markers like 'des Beschwerdeführers', 'der Antragstellerin'. Uses numbered capture group.

**Content:**
```
(?:des\s+(?:Beschwerdeführers|Antragstellers|Antragstellersin|Klägers|Beteiligten|Vertreters|Stellvertreters)|der\s+(?:Beschwerdeführerin|Antragstellerin|Klägerin|Beteiligten|Vertreterin|Stellvertreterin))\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|LLB|LL\.M|MSc|PhD|Dr\.|Mag\.|Mag\.a|Mag\.in|Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|KommR|KzlR|Ing\.|Dipl\.-Ing\.|RgR|StB|Stb|MAS|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|OMedR|MedR|Dr\.in|DDr\.in|Bakk\.\s+rer\.\s+nat\.)\s*)?)
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

## `person_simple_name_context`

**F1:** 0.182 | **Precision:** 1.000 | **Recall:** 0.100  

**Format:** `regex`  
**Description:**
Captures simple names (First Last) in contexts like 'in der Beschwerdesache' where no title is present. Uses numbered capture group.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Revisionssache|Verwaltungsstrafsache|Verfahren|Sache)\s+)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)+)(?=\s*,|\s+\n|\s+\d+|\u00d6sterreich|\s*\(|\s*\)|\s*\.|\s*"|\s*'|\s+\s|$|\s+sei|\s+ist|\s+hat|\s+war|\s+GmbH|\s+KG|\s+AG|\s+OHG|\s+UG|\s+GmbH\s*&|\s+GmbH\s*&\s*Co|\s+vertreten)
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

## `person_after_preposition`

**F1:** 0.003 | **Precision:** 0.002 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures names following prepositions like 'von', 'durch', 'gegen', 'in', 'an', 'bei', 'nach', 'zu', 'auf'. Uses numbered capture group.

**Content:**
```
(?:von|durch|gegen|in|an|bei|nach|zu|auf)\s+(?:VetR\s+|StR\s+|Hon\.-Prof\.(?:in)?\s+|Priv\.-Doz\.(?:in)?\s+|Univ\.-Prof\.(?:in)?\s+|Dr\.(?:in)?\s+|Mag\.(?:in)?\s+|OStR\s+|OSR\s+|MedR\s+|Techn\s+R\s+|HR\s+|Senatsvorsitzender\s+|Senatsvorsitzende\s+|Dipl\.-Ing\.(?:in)?\s+|RgR\s+|StB\s+|Stb\s+|OMedR\s+|B\.?A\.?\s+iur\s+|Bakk\.\s+art\.\s+MA\s+|techn\.\s+|KommR\s+|KzlR\s+|Ing\.(?:in)?\s+|Dipl\.(?:in)?\s+|Bakk\.(?:in)?\s+|PhD\s+|LLB\s+|LL\.M\s+|MSc\s+|MAS\s+|DDr\.(?:in)?\s+|Prof\.(?:in)?\s+|Ri\s+|\u00d6kR\s+|HR\s+KzlR\s+|Herr\s+|Frau\s+|Herrn\s+|Frauen\s+)?([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|LLB|LL\.M|MSc|PhD|Dr\.|Mag\.|Mag\.a|Mag\.in|Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|KommR|KzlR|Ing\.|Dipl\.-Ing\.|RgR|StB|Stb|MAS|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|OMedR|MedR|Dr\.in|DDr\.in|Bakk\.\s+rer\.\s+nat\.)\s*)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.002 | 0.011 | 0.003 | 491 | 1 | 490 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 490 | 89 |

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

- `Unrecht` — no gold match — likely missing annotation
- `Familienbeihilfe` — no gold match — likely missing annotation
- `Höhe` — no gold match — likely missing annotation
- `Recht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Art` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_4`)


Am 30.09.2019 langte beim Finanzamt die Antwort der Beschwerdeführerin (in der Folge BF)  auf ein Überprüfungsschreiben des Anspruches auf Familienbeihilfe ein.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Schreiben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_7`)


3. Mit Bescheid vom 12.11.2019 forderte das Finanzamt die für den Zeitraum von November  2017 bis Juni 2018 bezogenen Beträge an Familienbeihilfe und Kinderabsetzbeträgen iHv.

**False Positives:**

- `November` — no gold match — likely missing annotation
- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_12`)


Im Zeitraum 11/17 bis 6/18 befand sich Stella Marschalk, Bakk. techn.  nicht in Berufsausbildung.“

**False Positives:**

- `Berufsausbildung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_15`)


Der Beschwerde beigelegt war eine Betätigung eines Allgemeinmediziners vom 27.11.2019,  wonach Stella Marschalk, Bakk. techn.  auf Grund einer schweren Erkrankung (Sensibilitätsdefizit untere  Extremitäten DD: Guillain-Barré-Syndrom) von Oktober 2017 bis Ende Juni 2018 nicht  arbeitsfähig gewesen sei.

**False Positives:**

- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`
- `Grund` — no gold match — likely missing annotation
- `Oktober` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_18`)


5. Mit Beschwerdevorentscheidung vom 14.07.2020 wurde die Beschwerde als unbegründet  zurückgewiesen, da keine der in § 2 Abs. 1 lit. b bis e FLAG 1967 gennannten Voraussetzungen  für die Gewährung von Familienbeihilfe erfüllt seien.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_19`)


6. Mit Schriftsatz vom 04.08.2020 stellte die BF über ihren steuerlichen Vertreter den Antrag  auf Vorlage der Bescheidbeschwerde an das Bundesfinanzgericht.

**False Positives:**

- `Vorlage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Ausbildung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Frage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Zielstrebigkeit` — no gold match — likely missing annotation
- `Stella Marschalk` — partial — pred is substring of gold: `Stella Marschalk, Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_26`)


Dem Vorlageantrag beigelegt war ein Schreiben der Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith, in dem bestätigt wurde, dass Stella Marschalk, Bakk. techn.  die Schule in  der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Schreiben` — no gold match — likely missing annotation
- `Grillenreith` — partial — pred is substring of gold: `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_29`)


Die Tochter der BF absolvierte in der Zeit vom 01.10.2016 bis 04.10.2017 die Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith.

**False Positives:**

- `Grillenreith` — partial — pred is substring of gold: `Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith`(organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_36`)


Im gegenständlichen Fall ist strittig, ob in der Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG 1967 vorliegt.

**False Positives:**

- `November` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_38`)


Nach § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG 1967) haben Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, Anspruch auf  Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_47`)


Somit ist es nicht als rechtswidrig zu befinden, wenn das Finanzamt schon auf Grund der  insoweit unstrittigen Feststellungen, die Tochter der BF habe die Krankenpflegeschule bis zum  04.10.2017 absolviert und die Ausbildung nicht fortgesetzt, zum Ergebnis gelangt ist, die  Tochter der BF sei im Streitzeitraum nicht in Berufsausbildung gestanden.

**False Positives:**

- `Grund` — no gold match — likely missing annotation
- `Berufsausbildung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_48`)


§ 26 Abs. 1 FLAG 1967 normiert eine objektive Erstattungspflicht desjenigen, der die  Familienbeihilfe zu Unrecht bezogen hat.

**False Positives:**

- `Unrecht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_50`)


Entscheidend ist somit lediglich, ob der Empfänger die  Beträge zu Unrecht erhalten hat (vgl. VwGH 28.10.2009, 2008/15/0329).

**False Positives:**

- `Unrecht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_51`)


Gemäß § 33 Abs. 3 EStG 1988 ist für zu Unrecht bezogene Kinderabsetzbeträge § 26 FLAG 1967  anzuwenden.

**False Positives:**

- `Unrecht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_52`)


Die Rückforderung der bezogenen Beträge erfolgte daher zu Recht und die Beschwerde war  spruchgemäß abzuweisen.

**False Positives:**

- `Recht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Erkenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation
- `Recht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133  Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Art` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der beschwerdegegenständliche Abweisungsbescheid wurde erlassen wie folgt:  Ihr Antrag auf Familienbeihilfe vom 07.10.2020 wird abgewiesen für:  Name des Kindes – VNR/Geb.dat.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_5`)


Daher haben Sie keinen Anspruch auf Familienbeihilfe (§ 2 Abs. 8  Familienlastenausgleichsgesetz 1967).

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Worcester` — type mismatch — same span as gold: `Worcester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_13`)


Ende Mai 2019 wurde meine noch minderjährige [Anmerkung: 17 ½ -jährige] Tochter aus der  Wohnung der Familie des Ziehvaters in Worcester weggewiesen.

**False Positives:**

- `Worcester` — type mismatch — same span as gold: `Worcester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Worcester`(city)

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `England Advanced Level` — partial — gold is substring of pred: `England`
- `Jahr` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_20`)


Gemäß obigen Ausführungen ist meine Tochter Maximiliane Sakschewsky, MA  seit Sommer 2014,  ausgenommen ferienbedingte Abwesenheiten, in Vereinigten Königreich wohnhaft.

**False Positives:**

- `Vereinigten Königreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_23`)


Die Beschwerdevorlage erfolgte mit nachstehendem Sachverhalt und Anträgen:  Sachverhalt:  Der Bf stellte einen Antrag auf Gewährung der Familienbeihilfe für seine Tochter  Maximiliane Sakschewsky, MA  ab Juni 2019.

**False Positives:**

- `Gewährung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_24`)


Er ist österreichischer Staatsbürger mit Wohnsitz in Wien und geschieden;

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_25`)


die Kindesmutter  lebt in Großbritannien.

**False Positives:**

- `Großbritannien` — type mismatch — same span as gold: `Großbritannien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Großbritannien`(country)

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_28`)


Im Jahr 2019 bis inkl Juli 2020 ging die Tochter des Bf in Großbritannien in die Schule und  verbrachte die Sommerferien in Wien bei ihrem Vater.

**False Positives:**

- `Großbritannien` — type mismatch — same span as gold: `Großbritannien`
- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_29`)


Ab September 2020 begann sie ein Studium in Großbritannien und verbrachte die Ferien laut  Angaben im Antrag wieder in Wien.

**False Positives:**

- `Studium` — no gold match — likely missing annotation
- `Großbritannien` — type mismatch — same span as gold: `Großbritannien`
- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_30`)


Bis Mai 2019 lebte die Tochter bei ihrer Mutter in Großbritannien, danach bei dem Onkel ihres  Stiefvaters (ebenfalls in GB), der in diesem Zeitpunkt auch die Unterhaltskosten getragen hat  und ab September 2020 in einem Studentenwohnheim der University of Bristol.

**False Positives:**

- `Großbritannien` — type mismatch — same span as gold: `Großbritannien`
- `GB` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `University of Bristol`(organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_37`)


Die Tragung der Kosten einer Unterkunft, Nahrung, Kleidung, etc, die in Großbritannien  mindestens auch nochmals EUR 1.000,- betragen würden, trägt demnach im Zeitraum Juni  2019 – Sept 2020 laut eigenen Angaben weder der Kindesvater noch die Kindesmutter.

**False Positives:**

- `Großbritannien` — type mismatch — same span as gold: `Großbritannien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Großbritannien`(country)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_39`)


Da die Tochter des Bf im beschwerdegegenständlichen Zeitraum teilweise noch minderjährig  war, wird davon ausgegangen, dass so ein Anspruch zumindest teilweise bestanden hätte.

**False Positives:**

- `Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_42`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname die Bf.) zogen mit Ihrer Mutter und  Ziehvater vor fünf Jahren mit meiner Zustimmung (vertraglich zugestimmt) nach  Großbritannien.

**False Positives:**

- `Großbritannien` — type mismatch — same span as gold: `Großbritannien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Worcester` — type mismatch — same span as gold: `Worcester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_53`)


Am 31. Mai 2019 und in den folgenden Monaten, bis 3. August 2020, überwies der Bf. an die  Kindesmutter der (gemeinsamen) Töchter Maximiliane Sakschewsky, MA  und E. auf das Konto in  Großbritannien IBAN GB… 8171 € 1.000,00 (Kontoauszüge).

**False Positives:**

- `Großbritannien IBAN GB` — partial — gold is substring of pred: `Großbritannien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_56`)


In den Zeiträumen 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019  sowie 17. bis 19. Februar 2020 unternahm die Tochter des Bf. in Wien Fahrten gemäß § 19  Abs. 8 FSG (Fahrtenprotokoll).

**False Positives:**

- `Wien Fahrten` — partial — gold is substring of pred: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

**False Positives:**

- `England` — type mismatch — same span as gold: `England`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_59`)


Am 11. August 2020 überwies der Bf. auf das Konto in Großbritannien IBAN GB…1114 € 500,00  E… (Nachname wie Bf.), am 14. September 2020 € 140,00.

**False Positives:**

- `Großbritannien IBAN GB` — partial — gold is substring of pred: `Großbritannien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Großbritannien`(country)

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_60`)


[Bemerkung: Streitzeitraum bis September 2020]  Am 01. und 08. Oktober 2020 überwies der Bf. auf das Konto der geschiedenen Gattin des Bf.  in Großbritannien IBAN GB… 8171 € 500,00.

**False Positives:**

- `Großbritannien IBAN GB` — partial — gold is substring of pred: `Großbritannien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Großbritannien`(country)

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_72`)


Sie lebte mit ihrer (vom Bf. geschiedenen) Mutter, deren Lebensgefährten (Ziehvater) und ihrer  Schwester bis Mai 2019 in Großbritannien.

**False Positives:**

- `Großbritannien` — type mismatch — same span as gold: `Großbritannien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Großbritannien`(country)

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_73`)


Sodann zog Maximiliane Sakschewsky, MA  zu einem Onkel des  Ziehvaters nach Worcester (und haben in dieser Zeit der Onkel und dessen Frau die Kosten für  Essen und Logie getragen).

**False Positives:**

- `Worcester` — type mismatch — same span as gold: `Worcester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_75`)


Diesen Lebensumständen stehen folgende inländische (österreichische) Anknüpfungspunkte  gegenüber: Nachweisliche Aufenthalte  - am 18. August 2019 (6-stündige Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" im Hinblick auf den beabsichtigten  Führerscheinerwerb),  vom 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019 sowie  17. bis 19. Februar 2020 (in Wien mit dem Bf. unternommene Fahrten gemäß § 19 Abs. 8 FSG;  am 20. Februar 2020 wurde vom Bf. die Überweisung von € 173,10 an die  Landespolizeidirektion Wien - Verkehrsamt vorgenommen).

**False Positives:**

- `Wien` — type mismatch — same span as gold: `Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien`(city)
- `Landespolizeidirektion Wien`(organisation)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_76`)


War das Finanzamt zur Schlussfolgerung gelangt, dass der Besuch ***TochterA.*** in den  Sommerferien und zB auch über Weihnachten eine Haushaltszugehörigkeit beim Bf. nicht  begründen, ist eine Unrichtigkeit auf Grund der obigen Ausführungen nicht zu erkennen.

**False Positives:**

- `Grund` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_80`)


- Am 20. April und 15. Mai 2020 an K. H., die Mutter ihres Freundes, jeweils € 400,00.  - Kosten, die im Zusammenhang mit den Österreich-Aufenthalten von Maximiliane Sakschewsky, MA  anfielen  (wie bspw. betreffend den Führerscheinerwerb).

**False Positives:**

- `Maximiliane Sakschewsky` — partial — pred is substring of gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_81`)


Unter Bedachtnahme auf das eigene Vorbringen des Bf.: ‚Ich habe monatlich € 1.000,- an  meine Ex-Gattin überwiesen, die als Schulgeld galten.‘ und den Umstand, dass diese  Überweisungen für beide Töchter erfolgt waren, bedarf es auf Basis der obigen Feststellungen  keiner weiteren Ausführungen, dass mit den Leistungen des Bf. nicht die überwiegenden  Unterhaltskosten seiner (17 ½- bis 18 ½- jährigen) Tochter Maximiliane Sakschewsky, MA, die ab Mai 2019  bei einem Onkel ihres Ziehvaters und dessen Frau (in Worcester) und sodann zeitweilig (der Bf.  spricht von 1 Monat) bei der Mutter ihres Freundes lebte, abgedeckt worden sind.

**False Positives:**

- `Basis` — no gold match — likely missing annotation
- `Worcester` — type mismatch — same span as gold: `Worcester`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_83`)


Zu Spruchpunkt I.  § 2 Abs. 2 Familienlastenausgleichsgesetz (FLAG) bestimmt:  Anspruch auf Familienbeihilfe für ein im Abs. 1 genanntes Kind hat die Person, zu deren  Haushalt das Kind gehört.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_84`)


Eine Person, zu deren Haushalt das Kind nicht gehört, die jedoch die  Unterhaltskosten für das Kind überwiegend trägt, hat dann Anspruch auf Familienbeihilfe,  wenn keine andere Person nach dem ersten Satz anspruchsberechtigt ist.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_87`)


Bemerkt wird abschließend, dass vom Finanzamt darauf Folgendes hingewiesen wurde:  Trotz Aufforderung einer Vorlage eines behördlichen Nachweises über den ausländischen  Bezug einer Familienleistung respektive die Nichtgewährung einer solchen, wurde so einer  nicht vorgelegt.

**False Positives:**

- `Folgendes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

**False Positives:**

- `Erkenntnis` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `SVNR` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Recht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_4`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) zulässig.

**False Positives:**

- `Art` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_17`)


Mit Bescheid vom 17.09.2021 forderte die belangte Behörde von der Beschwerdeführerin (=  „Bf.“) zu Unrecht bezogener Beiträge an Familienbeihilfe und Kinderabsetzbetrag von  insgesamt EUR 4.163,20 für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die  Kinder mit der SVNr.

**False Positives:**

- `Unrecht` — no gold match — likely missing annotation
- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `Verbindung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_20`)


Wenn ein Studienwechsel zu einem Wegfall der Familienbeihilfe führt, besteht erst wieder  Anspruch, wenn im neuen Studium so viele Semester absolviert wurden wie im vorigen (§ 2 Abs.  1 lit. b Familienlastenausgleichsgesetz 1967 in Verbindung mit § 17 Studienförderungsgesetz  1992).

**False Positives:**

- `Studienwechsel` — no gold match — likely missing annotation
- `Verbindung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `Kind Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_22`)


Im Rückforderungsbetrag ist die  anteilige Geschwisterstaffel für sämtliche Kinder enthalten, für die Sie im  Rückforderungszeitraum zu Unrecht Familienbeihilfe erhalten haben (§ 8 Abs. 3  Familienlastenausgleichsgesetz 1967).“  4. Dagegen erhob die Bf. rechtzeitig die Beschwerde vom 07.10.2021 und brachte vor, dass  hierbei nur ein Wechsel des Studienortes bei gleichbleibender Studienrichtung vorliege.

**False Positives:**

- `Unrecht Familienbeihilfe` — no gold match — likely missing annotation
- `Wechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_24`)


Ein Vergleich der Studienrichtungen werde gerade von der  Wirtschaftsuniversität angefordert und nach Erhalt nachgereicht.

**False Positives:**

- `Vergleich` — no gold match — likely missing annotation
- `Erhalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `BA Sozial` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_28`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“

**False Positives:**

- `Studium` — no gold match — likely missing annotation
- `Hinblick` — no gold match — likely missing annotation
- `Kompetenzen` — no gold match — likely missing annotation
- `Fähigkeiten` — no gold match — likely missing annotation
- `Hinblick` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 5

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_30`)


7. Mit Beschwerdevorentscheidung vom 18.03.2022 wurde die Beschwerde als unbegründet  abgewiesen und dies wie folgt begründet:  „Wenn ein Studienwechsel zu einem Wegfall der Familienbeihilfe führt, besteht erst wieder  Anspruch, wenn im neuen Studium so viele Semester absolviert wurden wie im vorigen (§ 2 Abs.  1 lit. b Familienlastenausgleichsgesetz 1967 in Verbindung mit § 17 Studienförderungsgesetz  1992).

**False Positives:**

- `Studienwechsel` — no gold match — likely missing annotation
- `Verbindung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_33`)


An der WU Wien wurde das Studium  Wirtschafts- und Sozialwissenschaften (Bachelor) betrieben, in Linz handelte es sich um das  Studium Wirtschaftswissenschaften (Bachelor).

**False Positives:**

- `Linz` — type mismatch — same span as gold: `Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WU Wien`(organisation)
- `Linz`(city)

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_34`)


Auch die Tatsache, dass von abgelegten  Prüfungen im Umfang von 42 ECTS lediglich 24 ECTS anerkannt wurden, ist ein Kriterium, dass  es sich hier nicht um ein identes Studium handelt.

**False Positives:**

- `Kriterium` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_40`)


Auch wenn man die beiden Studien auf  Karriereaussichten vergleicht, ist eine Identität feststellbar!

**False Positives:**

- `Karriereaussichten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_45`)


Zumal es sich in Anbetracht obiger Ausführungen  aber um gleichwertige Studien handelt, ist im gegebenen Fall das Vorliegen eines  Studienwechsels zu verneinen und von einem durchgängigen Studium auszugehen, sodass die  Rückforderung der Familienbeihilfe für oben genannten Zeitraum nicht zu Recht erfolgt.

**False Positives:**

- `Anbetracht` — no gold match — likely missing annotation
- `Recht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `BA Sozial` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Johannes Kepler  Universität Linz`(organisation)
- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

**False Positives:**

- `Studium` — no gold match — likely missing annotation
- `Hinblick` — no gold match — likely missing annotation
- `Kompetenzen` — no gold match — likely missing annotation
- `Fähigkeiten` — no gold match — likely missing annotation
- `Hinblick` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 5

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 75** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

**False Positives:**

- `WU` — type mismatch — same span as gold: `WU`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WU`(organisation)
- `JKU`(organisation)

**Example 76** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_54`)


Aufgrund des Arbeitsauftrages wurde dann ermittelt und es stellte sich ein Studienwechsel mit  WS 19/20 heraus, vom Studium UJ033 561 Bachelorstudium Wirtschafts- und  Sozialwissenschaften an der WU Wien auf UK033 572 Bachelorstudium  Wirtschaftswissenschaften an der JKU Linz.

**False Positives:**

- `Studienwechsel` — no gold match — likely missing annotation
- `UK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 77** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_58`)


17.09.2021 ein Rückforderungsbescheid erstellt, in dem der strittige Zeitraum von 10/2019 –  01/2021 rückgefordert wurde.

**False Positives:**

- `Rückforderungsbescheid` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_64`)


Beweismittel: siehe Akteninhalt  Stellungnahme:  § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 in Verbindung mit § 17  Studienförderungsgesetz 1992 regelt die schädlichen Studienwechsel.

**False Positives:**

- `Verbindung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_66`)


Wenn ein  Studienwechsel zu einem Wegfall der Familienbeihilfe führt, besteht erst wieder Anspruch,  wenn im neuen Studium so viele Semester absolviert wurden wie im vorigen.

**False Positives:**

- `Studienwechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_69`)


Den  Anführungen der Beschwerdeführerin, dass es sich um einen reinen Studienortswechsel handle,  welcher als unschädlicher Wechsel angesehen werden würde, kann nicht zugestimmt werden,  da die beiden Studien zwar grundsätzlich ähnlich sind, allerdings aufgrund der Tatsache, dass  nur ein Teil der ECTS angerechnet wurde, nicht von demselben Studium gesprochen werden  kann.

**False Positives:**

- `Teil` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

**False Positives:**

- `Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Viktoria Immohr`(person)
- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz (`(organisation)

**Example 82** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_74`)


Weiters absolvierte die Tochter der Bf. an der JKU Linz Lehrveranstaltungen mit  31 ECTS-Punkten (ohne Berücksichtigung von Anrechnungen).

**False Positives:**

- `Anrechnungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `JKU Linz`(organisation)

**Example 83** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_84`)


Vergleicht man die beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des  Studiums, auch im Hinblick auf die Qualifikations- und Ausbildungsziele und die in Aussicht  genommenen Berufsbilder, ausgegangen werden.

**False Positives:**

- `Aussicht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Studienwechsel` — no gold match — likely missing annotation
- `Studienortwechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU)`(organisation)
- `Johannes Kepler Universität Linz (JKU)`(organisation)

**Example 85** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_88`)


Zur Beantwortung dieser Frage ist auf Sachverhaltsebene der Umfang und Inhalt der  beiden Studien zu vergleichen.

**False Positives:**

- `Sachverhaltsebene` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_94`)


In dieser Hinsicht kann ein Vergleich gezogen werden mit dem  bisherigen rechtswissenschaftlichen Diplomstudium, welches ebenfalls an mehreren  Universitätsstandorten in Österreich angeboten wurde bzw. wird (und nunmehr zusehends  durch einen Bologna-konformen Aufbau aus Bachelor und Master ersetzt wird), wobei sich  auch hier die konkreten Studienpläne bzw. –inhalte im Detail regelmäßig unterscheiden und  dennoch zum selben, als gleichartig anerkannten Ausbildungsergebnis führen sowie jeweils  Voraussetzung für die drei juristischen „Kernberufe“ Richter, Anwalt und Notar sind.

**False Positives:**

- `Vergleich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Österreich`(country)

**Example 87** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_99`)


Dies muss jedoch nicht zwangsläufig an  unterschiedlichen Ausbildungsinhalten liegen, sondern kann auch unterschiedlichen  Kursteilnahme-Voraussetzungsketten und Detailunterschieden der Studienpläne liegen, die  manche Lehrveranstaltungen entweder erst später (nach Absolvierung anderer Kurse)  anrechenbar machen bzw. die aufgrund unterschiedlicher (ECTS-)

**False Positives:**

- `Absolvierung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_101`)


Aus der nicht im gleichen Umfang erfolgten Anrechnung zum Zeitpunkt des  Studienwechsels kann daher noch kein automatischer Schluss betreffend die Vergleichbarkeit  von Studien gezogen werden.

**False Positives:**

- `Studien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_105`)


Die Studienpläne sind in Kernbereichen identisch, jedoch im Gesamten nicht gänzlich  deckungsgleich, was allerdings auch daran liegt, dass deckungsgleiche Studien an  verschiedenen Standorten aufgrund der Freiheiten und Entwicklungen des Bologna-Systems  (Spezialisierungen/Nuancierungen der Lehrinhalte im Detail, Schaffung diverser  Voraussetzungsketten bei Lehrveranstaltungs-Anmeldungen und Anrechnungen, welche auch  standortbezogen dem schnelleren Studienabschluss dienen sollen) in der Praxis nahezu  ausgeschlossen sind.

**False Positives:**

- `Kernbereichen` — no gold match — likely missing annotation
- `Lehrveranstaltungs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 90** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_107`)


Die Qualifikations- bzw. Ausbildungsziele für ein  Studium der Wirtschaftswissenschaften in Hinblick auf Kompetenzen (im Sinne eines  spezialisiertes Systems von Fähigkeiten) sowie von avisierten Lernergebnissen  (operationalisiert durch vollzogene Prüfungen) seien an beiden Universitäten in Hinblick auf  diesen beiden Programme als gleichwertig anzusehen.

**False Positives:**

- `Studium` — no gold match — likely missing annotation
- `Hinblick` — no gold match — likely missing annotation
- `Kompetenzen` — no gold match — likely missing annotation
- `Fähigkeiten` — no gold match — likely missing annotation
- `Hinblick` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 5

**Example 91** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_110`)


3. Rechtliche Beurteilung  3.1. Rechtslage  Gemäß § 2 Abs. 1 lit. b Familienlastenausgleichsgesetz 1967 idF. BGBl. I Nr. 24/2019 und Nr.  28/2020 haben Personen Anspruch auf Familienbeihilfe für volljährige Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 92** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_112`)


Bei Kindern, die eine in § 3 des Studienförderungsgesetzes 1992, BGBl.Nr. 305, genannte  Einrichtung besuchen, ist eine Berufsausbildung nur dann anzunehmen, wenn sie die  vorgesehene Studienzeit pro Studienabschnitt um nicht mehr als ein Semester oder die  vorgesehene Ausbildungszeit um nicht mehr als ein Ausbildungsjahr überschreiten.

**False Positives:**

- `Semester` — no gold match — likely missing annotation
- `Ausbildungsjahr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 93** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_113`)


Wird ein  Studienabschnitt in der vorgesehenen Studienzeit absolviert, kann einem weiteren  Studienabschnitt ein Semester zugerechnet werden.

**False Positives:**

- `Studienabschnitt` — no gold match — likely missing annotation
- `Semester` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 94** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_114`)


Bei einem Studienwechsel gelten die in § 17 Studienförderungsgesetz 1992 angeführten  Regelungen auch für den Anspruch auf Familienbeihilfe.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_118`)


Nach § 17 Abs. 2 Z 1 StudFG gelten nicht als Studienwechsel im Sinne des Abs. 1 solche, bei  welchen die gesamten Vorstudienzeiten für die Anspruchsdauer des nunmehr betriebenen  Studiums berücksichtigt werden, weil sie dem nunmehr betriebenen Studium auf Grund der  besuchten Lehrveranstaltungen und absolvierten Prüfungen nach Inhalt und Umfang der  Anforderungen gleichwertig sind.

**False Positives:**

- `Grund` — no gold match — likely missing annotation
- `Inhalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 96** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_119`)


Ein Studienwechsel im Sinne des Abs. 1 Z 2 ist gemäß Abs. 4  nicht mehr zu beachten, wenn der Studierende in dem nunmehr gewählten Studium so viele  Semester wie in dem vor dem Studienwechsel betriebenen Studium zurückgelegt hat.

**False Positives:**

- `Studienwechsel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_122`)


Nach § 26 Abs. 1 FLAG 1967 idF. BGBl. I Nr. 104/2019 hat, wer Familienbeihilfe zu Unrecht  bezogen hat, die entsprechenden Beträge zurückzuzahlen.

**False Positives:**

- `Unrecht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 98** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_128`)


Es ist zur Klärung der Rechtsmäßigkeit der Rückforderung zunächst zu prüfen, ob ein  „Studienwechsel“ im Sinne des § 2 Abs. 1 lit. b FLAG 1967 überhaupt vorliegt, bevor auf einen  solchen Studienwechsel die Bestimmungen des § 17 StudFG angewendet werden können (BFG  26.02.2022, RV/2100101/2022 mit Verweis auf VwGH 09.07.2008, 2005/13/0142, Rechtssatz  JWR_2005130142_20080709X02).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `person_genitive_simple`

**F1:** 0.001 | **Precision:** 0.001 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Captures names following genitive markers 'der' or 'des' (e.g., 'des Hilde Lederhas'). Uses numbered capture group.

**Content:**
```
(?:des\s+|der\s+)(?:VetR\s+|StR\s+|Hon\.-Prof\.(?:in)?\s+|Priv\.-Doz\.(?:in)?\s+|Univ\.-Prof\.(?:in)?\s+|Dr\.(?:in)?\s+|Mag\.(?:in)?\s+|OStR\s+|OSR\s+|MedR\s+|Techn\s+R\s+|HR\s+|Senatsvorsitzender\s+|Senatsvorsitzende\s+|Dipl\.-Ing\.(?:in)?\s+|RgR\s+|StB\s+|Stb\s+|OMedR\s+|B\.?A\.?\s+iur\s+|Bakk\.\s+art\.\s+MA\s+|techn\.\s+|KommR\s+|KzlR\s+|Ing\.(?:in)?\s+|Dipl\.(?:in)?\s+|Bakk\.(?:in)?\s+|PhD\s+|LLB\s+|LL\.M\s+|MSc\s+|MAS\s+|DDr\.(?:in)?\s+|Prof\.(?:in)?\s+|Ri\s+|\u00d6kR\s+|HR\s+KzlR\s+|Herr\s+|Frau\s+|Herrn\s+|Frauen\s+)?([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|LLB|LL\.M|MSc|PhD|Dr\.|Mag\.|Mag\.a|Mag\.in|Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|KommR|KzlR|Ing\.|Dipl\.-Ing\.|RgR|StB|Stb|MAS|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|OMedR|MedR|Dr\.in|DDr\.in|Bakk\.\s+rer\.\s+nat\.)\s*)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.001 | 0.011 | 0.001 | 1285 | 1 | 1284 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 1284 | 89 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Willibald Endrowait` — partial — gold is substring of pred: `Willibald Endrowait`
- `FA Graz` — partial — pred is substring of gold: `FA Graz-Stadt`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement`(person)
- `Willibald Endrowait`(person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_4`)


Am 30.09.2019 langte beim Finanzamt die Antwort der Beschwerdeführerin (in der Folge BF)  auf ein Überprüfungsschreiben des Anspruches auf Familienbeihilfe ein.

**False Positives:**

- `Beschwerdeführerin` — no gold match — likely missing annotation
- `Folge BF` — no gold match — likely missing annotation
- `Anspruches` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Ergänzungsersuchens` — no gold match — likely missing annotation
- `Schule` — partial — pred is substring of gold: `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`
- `Zeit` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_8`)


insgesamt 1.781,80 Euro von der BF zurück.

**False Positives:**

- `BF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

**False Positives:**

- `Schule` — partial — pred is substring of gold: `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_19`)


6. Mit Schriftsatz vom 04.08.2020 stellte die BF über ihren steuerlichen Vertreter den Antrag  auf Vorlage der Bescheidbeschwerde an das Bundesfinanzgericht.

**False Positives:**

- `Bescheidbeschwerde` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

**False Positives:**

- `Schule` — partial — pred is substring of gold: `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith`(organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_21`)


Aufgrund einer schweren  Erkrankung, die im Oktober 2017 aufgetreten ist (Guillain-Barre-Syndrom, siehe Beilage), war  Frau Stella Marschalk, Bakk. techn.  nicht in der Lage, die Ausbildung fortzusetzen und musste diese per  4.10.2017 unterbrechen (siehe Beilage).

**False Positives:**

- `Lage` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_22`)


Im Verlauf der Krankheit wurde klar, dass eine körperlich belastende Tätigkeit wie  Krankenpflege für Frau Stella Marschalk, Bakk. techn.  nicht mehr in Frage kam, sodass sich Frau  Stella Marschalk, Bakk. techn.  stattdessen zur Ausbildung zur Bürokauffrau entschloss, die sie in der  Mindestdauer von 2 Jahren am 26.6.2020 mit der Lehrabschlussprüfung abschließen konnte.

**False Positives:**

- `Krankheit` — no gold match — likely missing annotation
- `Mindestdauer` — no gold match — likely missing annotation
- `Lehrabschlussprüfung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_23`)


Die belangte Behörde hat in ihrer Beschwerdevorentscheidung nicht ausgeführt, warum die  Grundvoraussetzung für den Bezug der Familienbeihilfe ihrer Meinung nach nicht vorlag, sodass  darauf nicht weiter eingegangen werden kann.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_24`)


Tatsache ist, dass es an Zielstrebigkeit bei der  Ausbildung von Frau Stella Marschalk, Bakk. techn.  nicht gemangelt hat, Frau Stella Marschalk, Bakk. techn.  war  lediglich aus gesundheitlichen Gründen gezwungen, die ursprünglich angestrebte Berufswahl zu  revidieren.“

**False Positives:**

- `Ausbildung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stella Marschalk, Bakk. techn.`(person)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_26`)


Dem Vorlageantrag beigelegt war ein Schreiben der Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith, in dem bestätigt wurde, dass Stella Marschalk, Bakk. techn.  die Schule in  der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

**False Positives:**

- `Schule` — partial — pred is substring of gold: `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith`
- `Zeit` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith`(organisation)
- `Stella Marschalk, Bakk. techn.`(person)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_29`)


Die Tochter der BF absolvierte in der Zeit vom 01.10.2016 bis 04.10.2017 die Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith.

**False Positives:**

- `BF` — no gold match — likely missing annotation
- `Zeit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_30`)


Aufgrund der Erkrankung am Guillain-Barré-Syndrom konnte sie die Ausbildung nach dem  04.10.2017 nicht weiterführen.

**False Positives:**

- `Erkrankung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_31`)


Ab dem 02.07.2018 absolvierte sie eine Lehre zur Steuerassistentin, die sie am 26.6.2020 mit  der Lehrabschlussprüfung beendete.

**False Positives:**

- `Lehrabschlussprüfung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_36`)


Im gegenständlichen Fall ist strittig, ob in der Zeit von November 2017 bis Juni 2018 eine  Berufsausbildung im Sinne des FLAG 1967 vorliegt.

**False Positives:**

- `Zeit` — no gold match — likely missing annotation
- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

**False Positives:**

- `Judikatur` — no gold match — likely missing annotation
- `Verwaltungsgerichtshofes` — type mismatch — same span as gold: `Verwaltungsgerichtshofes`
- `Natur` — no gold match — likely missing annotation
- `Dinge` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 3

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_41`)


Dazu zählen beispielsweise Erkrankungen, die die Berufsausbildung auf begrenzte Zeit  unterbrechen, oder Urlaube und Schulferien (VwGH vom 16.11.1993, 90/14/0108).

**False Positives:**

- `Urlaube` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_45`)


Im gegenständlichen Fall bringt der steuerliche Vertreter vor, dass die Ausbildung aufgrund der  Erkrankung mit 04.10.2017 lediglich unterbrochen worden sei und erst im weiteren Verlauf der  Krankheit klar geworden sei, dass die Ausbildung nicht wieder aufgenommen werden könne.

**False Positives:**

- `Erkrankung` — no gold match — likely missing annotation
- `Krankheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_46`)


Dem ist zu entgegnen, dass nach der zitierten Judikatur des Verwaltungsgerichtshofes das  Aufrechterhalten des Berufswunsches nicht maßgeblich ist, wenn die Ausbildung nach ihrem  Abbruch nicht wieder aufgenommen wird.

**False Positives:**

- `Verwaltungsgerichtshofes` — type mismatch — same span as gold: `Verwaltungsgerichtshofes`
- `Berufswunsches` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_47`)


Somit ist es nicht als rechtswidrig zu befinden, wenn das Finanzamt schon auf Grund der  insoweit unstrittigen Feststellungen, die Tochter der BF habe die Krankenpflegeschule bis zum  04.10.2017 absolviert und die Ausbildung nicht fortgesetzt, zum Ergebnis gelangt ist, die  Tochter der BF sei im Streitzeitraum nicht in Berufsausbildung gestanden.

**False Positives:**

- `BF` — no gold match — likely missing annotation
- `BF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_50`)


Entscheidend ist somit lediglich, ob der Empfänger die  Beträge zu Unrecht erhalten hat (vgl. VwGH 28.10.2009, 2008/15/0329).

**False Positives:**

- `Empfänger` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Bundesfinanzgerichtes` — type mismatch — same span as gold: `Bundesfinanzgerichtes`
- `Lösung` — no gold match — likely missing annotation
- `Rechtsprechung` — no gold match — likely missing annotation
- `Verwaltungsgerichtshofes` — type mismatch — same span as gold: `Verwaltungsgerichtshofes`
- `Verwaltungsgerichtshofes` — similar text (different position): `Verwaltungsgerichtshofes`

> overlaps gold: 3  |  likely missing annotation: 2

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_56`)


Ob eine Berufsausbildung im Sinne des FLAG 1967 vorliegt, ist eine Tatfrage (vgl. VwGH  16.11.1993, 90/14/0108), welche in freier Beweiswürdigung zu beantworten ist und einer  ordentlichen Revision nicht zugänglich ist.

**False Positives:**

- `FLAG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

**False Positives:**

- `Verwaltungsgerichtshofes` — type mismatch — same span as gold: `Verwaltungsgerichtshofes`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache  Frauke Stuhldreher, Dr. ` — partial — gold is substring of pred: `Frauke Stuhldreher`
- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Österreich`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `Frauke Stuhldreher`(person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `85-919/9176`(tax_number)

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der beschwerdegegenständliche Abweisungsbescheid wurde erlassen wie folgt:  Ihr Antrag auf Familienbeihilfe vom 07.10.2020 wird abgewiesen für:  Name des Kindes – VNR/Geb.dat.

**False Positives:**

- `Kindes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_4`)


– Zeitraum von – bis  (Nachname die Bf.) Maximiliane Sakschewsky, MA … 1201 ab Juli 2019  Begründung  Der Mittelpunkt der Lebensinteressen ihrer bereits volljährigen Tochter liegt nicht in  Österreich.

**False Positives:**

- `Lebensinteressen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Österreich`(country)

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_6`)


Was ist der Mittelpunkt der Lebensinteressen?

**False Positives:**

- `Mittelpunkt` — no gold match — likely missing annotation
- `Lebensinteressen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_9`)


Die Beschwerde wurde mit folgender Begründung erhoben:  Klarstellung: Der Zeitraum der beantragten Familienbeihilfe ist von 01.06.2019 bis 30.09.2020  für meine Tochter Maximiliane Sakschewsky, MA (Nachname wie Bf.) (geboren am … .12.2001).

**False Positives:**

- `Begründung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_10`)


Meine Töchter Maximiliane Sakschewsky, MA  und E… (Nachname wie Bf.) sind mit der Kindesmutter und  1 von 7 Seite 2 von 7

**False Positives:**

- `Kindesmutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_13`)


Ende Mai 2019 wurde meine noch minderjährige [Anmerkung: 17 ½ -jährige] Tochter aus der  Wohnung der Familie des Ziehvaters in Worcester weggewiesen.

**False Positives:**

- `Wohnung` — no gold match — likely missing annotation
- `Familie` — no gold match — likely missing annotation
- `Ziehvaters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Worcester`(city)

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_14`)


Es wurde Ihr jedwede weitere  Unterstützung seitens der Kindesmutter und Ziehvater verwehrt.

**False Positives:**

- `Kindesmutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

**False Positives:**

- `Matura` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)
- `King's School`(organisation)

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_23`)


Die Beschwerdevorlage erfolgte mit nachstehendem Sachverhalt und Anträgen:  Sachverhalt:  Der Bf stellte einen Antrag auf Gewährung der Familienbeihilfe für seine Tochter  Maximiliane Sakschewsky, MA  ab Juni 2019.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_26`)


Die Tochter studiert an der University of Bristol bis voraussichtlich Juli 2023.

**False Positives:**

- `University` — partial — pred is substring of gold: `University of Bristol`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `University of Bristol`(organisation)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_28`)


Im Jahr 2019 bis inkl Juli 2020 ging die Tochter des Bf in Großbritannien in die Schule und  verbrachte die Sommerferien in Wien bei ihrem Vater.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)
- `Wien`(city)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_30`)


Bis Mai 2019 lebte die Tochter bei ihrer Mutter in Großbritannien, danach bei dem Onkel ihres  Stiefvaters (ebenfalls in GB), der in diesem Zeitpunkt auch die Unterhaltskosten getragen hat  und ab September 2020 in einem Studentenwohnheim der University of Bristol.

**False Positives:**

- `University` — partial — pred is substring of gold: `University of Bristol`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Großbritannien`(country)
- `University of Bristol`(organisation)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_31`)


Für ihr Chemiestudium erhält die Tochter einen Studentenkredit, wovon 9.250,00 Pfund an die  Universität gezahlt werden, womit die Studiumskosten abdeckt sind, und 9.302,00 Pfund erhält  die Tochter des Bf für etwaige Lebenserhaltungskosten.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_34`)


Siehe Inhaltsverzeichnis  Stellungnahme:  In seiner Beschwerde verzichtete der Bf ausdrücklich auf das Erlassen einer  Beschwerdevorentscheidung gem § 262 Abs 2 BAO und stellte zudem klar, dass er  Familienbeihilfe für den Zeitraum Juni 2019 – September 2020 beantragt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_35`)


Der Besuch in den Sommerferien und zB auch über Weihnachten begründen keine  Haushaltszugehörigkeit, weswegen zu prüfen ist, ob der Bf die überwiegenden  Unterhaltskosten seiner Tochter trägt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_37`)


Die Tragung der Kosten einer Unterkunft, Nahrung, Kleidung, etc, die in Großbritannien  mindestens auch nochmals EUR 1.000,- betragen würden, trägt demnach im Zeitraum Juni  2019 – Sept 2020 laut eigenen Angaben weder der Kindesvater noch die Kindesmutter.

**False Positives:**

- `Kosten` — no gold match — likely missing annotation
- `Kindesvater` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Großbritannien`(country)

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_39`)


Da die Tochter des Bf im beschwerdegegenständlichen Zeitraum teilweise noch minderjährig  war, wird davon ausgegangen, dass so ein Anspruch zumindest teilweise bestanden hätte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_48`)


Nach dem Rausschmiss aus dieser Wohnung [laut vorstehendem Absatz: im Mai 2019] ist die  Maximiliane Sakschewsky, MA  zu einem Onkel des Ziehvaters nach Worcester …. gezogen.

**False Positives:**

- `Ziehvaters` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_49`)


In dieser Zeit  haben der Onkel … und seine Frau … die Kosten für Essen und Logie getragen.

**False Positives:**

- `Onkel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_52`)


(Vorhaltsbeantwortung des Bf. vom 03. Jänner 2021).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_53`)


Am 31. Mai 2019 und in den folgenden Monaten, bis 3. August 2020, überwies der Bf. an die  Kindesmutter der (gemeinsamen) Töchter Maximiliane Sakschewsky, MA  und E. auf das Konto in  Großbritannien IBAN GB… 8171 € 1.000,00 (Kontoauszüge).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Großbritannien`(country)

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_54`)


Am 18. August 2019 wurde der Tochter des Bf. die Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" gemäß §6 der Führerscheingesetz- Durchführungsverordnung von 1997, in der Dauer von sechs Stunden bestätigt.

**False Positives:**

- `Tochter` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation
- `Führerscheingesetz` — no gold match — likely missing annotation
- `Dauer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

**False Positives:**

- `Tochter` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_56`)


In den Zeiträumen 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019  sowie 17. bis 19. Februar 2020 unternahm die Tochter des Bf. in Wien Fahrten gemäß § 19  Abs. 8 FSG (Fahrtenprotokoll).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Wien`(city)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `England`(organisation)

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_59`)


Am 11. August 2020 überwies der Bf. auf das Konto in Großbritannien IBAN GB…1114 € 500,00  E… (Nachname wie Bf.), am 14. September 2020 € 140,00.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Großbritannien`(country)

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_60`)


[Bemerkung: Streitzeitraum bis September 2020]  Am 01. und 08. Oktober 2020 überwies der Bf. auf das Konto der geschiedenen Gattin des Bf.  in Großbritannien IBAN GB… 8171 € 500,00.

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Großbritannien`(country)

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_61`)


Am 23. Oktober 2020 überwies der Bf. auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN  GB…1084 € 200,00 mit dem Verwendungszweck: Unterstützung, am 4. November 2020  € 500,00 am 25. und 30. November jeweils € 200,00.

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_62`)


Am 09. Dezember 2020 überwies der Bf.  - auf das Konto der Tochter Maximiliane Sakschewsky, MA  IBAN GB…1084 (Maximiliane Sakschewsky, MA  Unterstützung)  € 300,00 und  - auf das Konto K. H., IBAN GB…1233 [vgl. oben: 20.04 und 15.05.2020] € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Tochter Maximiliane Sakschewsky` — positional overlap with gold: `Maximiliane Sakschewsky, MA`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)
- `Maximiliane Sakschewsky, MA`(person)

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_64`)


Am 19. Dezember 2020 überwies der Bf. auf das Konto K. H., IBAN GB…1233 € 300,00  (Maximiliane Sakschewsky, MA).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_65`)


Am 13. Jänner 2021 ersuchte das Finanzamt den Bf. um den „Nachweis der Überweisungen der  Alimente an ihre Tochter bzw. an die Kindesmutter ab Juni 2019 lfd.“.

**False Positives:**

- `Alimente` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_66`)


Am 11. Dezember 2020 bestätigte die University of Bristol, that Miss Maximiliane Sakschewsky, MA (Tochter  des Bf.) student no.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `University of Bristol`(organisation)
- `Maximiliane Sakschewsky, MA`(person)

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_70`)


Die Tochter des Bf. Maximiliane Sakschewsky, MA  war im beschwerdegegenständlichen Zeitraum nicht  zugehörig zum Haushalt des Bf.

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_71`)


Diese Feststellung beruht auf folgenden Umständen:  Maximiliane Sakschewsky, MA  war vom September 2014 bis Juli 2020 Schülerin der King's School Worcester,  Großbritannien.

**False Positives:**

- `King` — partial — pred is substring of gold: `King's School Worcester`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `King's School Worcester`(organisation)
- `Großbritannien`(country)

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_73`)


Sodann zog Maximiliane Sakschewsky, MA  zu einem Onkel des  Ziehvaters nach Worcester (und haben in dieser Zeit der Onkel und dessen Frau die Kosten für  Essen und Logie getragen).

**False Positives:**

- `Ziehvaters` — no gold match — likely missing annotation
- `Onkel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_74`)


Im September 2020 nahm Maximiliane Sakschewsky, MA  an der University of  Bristol ein full time- Studium auf.

**False Positives:**

- `University` — partial — pred is substring of gold: `University of  Bristol`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `University of  Bristol`(organisation)

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_76`)


War das Finanzamt zur Schlussfolgerung gelangt, dass der Besuch ***TochterA.*** in den  Sommerferien und zB auch über Weihnachten eine Haushaltszugehörigkeit beim Bf. nicht  begründen, ist eine Unrichtigkeit auf Grund der obigen Ausführungen nicht zu erkennen.

**False Positives:**

- `Besuch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_79`)


Der Bf. leistete im beschwerdegegenständlichen Zeitraum Unterhalt wie folgt:  - Für beide Töchter – Maximiliane Sakschewsky, MA  und E. – insgesamt monatlich € 1.000,00 (am 11. August  2020 überwies der Bf. für seine Tochter E. € 500,00, am 14. September 2020 € 140,00 und am  01. Oktober 2020 € 500,00).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_81`)


Unter Bedachtnahme auf das eigene Vorbringen des Bf.: ‚Ich habe monatlich € 1.000,- an  meine Ex-Gattin überwiesen, die als Schulgeld galten.‘ und den Umstand, dass diese  Überweisungen für beide Töchter erfolgt waren, bedarf es auf Basis der obigen Feststellungen  keiner weiteren Ausführungen, dass mit den Leistungen des Bf. nicht die überwiegenden  Unterhaltskosten seiner (17 ½- bis 18 ½- jährigen) Tochter Maximiliane Sakschewsky, MA, die ab Mai 2019  bei einem Onkel ihres Ziehvaters und dessen Frau (in Worcester) und sodann zeitweilig (der Bf.  spricht von 1 Monat) bei der Mutter ihres Freundes lebte, abgedeckt worden sind.

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation
- `Mutter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 4

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)
- `Worcester`(city)

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_85`)


Wie oben unter Punkt ausgeführt, erfüllt der Bf. die Voraussetzung, die Person zu sein, zu  deren Haushalt Maximiliane Sakschewsky, MA  gehört, nicht.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maximiliane Sakschewsky, MA`(person)

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

**False Positives:**

- `Bundesfinanzgerichtes` — type mismatch — same span as gold: `Bundesfinanzgerichtes`
- `Lösung` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_90`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

**False Positives:**

- `Rechtsprechung` — no gold match — likely missing annotation
- `Verwaltungsgerichtshofes` — type mismatch — same span as gold: `Verwaltungsgerichtshofes`
- `Verwaltungsgerichtshofes` — similar text (different position): `Verwaltungsgerichtshofes`

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_91`)


Diese Voraussetzungen sind im vorliegenden auf der Sachverhaltsebene zu lösenden Fall nicht  gegeben.

**False Positives:**

- `Sachverhaltsebene` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

**False Positives:**

- `Beschwerdesache Patricia Jentz` — partial — gold is substring of pred: `Patricia Jentz`
- `Finanzamtes` — partial — pred is substring of gold: `Finanzamtes Österreich`
- `Familienbeihilfe` — no gold match — likely missing annotation
- `Kinderabsetzbetrages` — no gold match — likely missing annotation
- `Beschwerdeführerin` — no gold match — likely missing annotation
- `SVNr` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 4

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ashley Partenfelder`(person)
- `Patricia Jentz`(person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `6207 150171`(social_security_number)

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_6`)


Aufgrund eines Arbeitsauftrages vom 21.05.2021 kam es zu einer Überprüfung des  Familienbeihilfe-Anspruches der Beschwerdeführerin (=Bf.) bezüglich ihrer Tochter  Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum, da zunächst aufgrund der COVID-Pandemie  sowohl Anspruchsüberprüfungen als auch Rückforderungen ausgesetzt worden waren.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation
- `Beschwerdeführerin` — no gold match — likely missing annotation
- `COVID` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_7`)


Die  Auszahlung der Familienbeihilfe war bereits mit 01/2021 eingestellt worden, da laut  Studiendatenübermittlungsauskunft das Studium der Tochter der Bf. (Viktoria Immohr) nur bis  14.12.2020 betrieben wurde und die Tochter mit 01.01.2021 eine Teilzeitbeschäftigung  begonnen hatte.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation
- `Tochter` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_8`)


Die belangte Behörde (Finanzamt) ersuchte mit Schreiben vom 19.07.2021 die Bf. um  Übermittlung eines Anrechnungsbescheides für Viktoria Immohr (Tochter der Bf.) über die  1 von 16 Seite 2 von 16

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Viktoria Immohr`(person)

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

**False Positives:**

- `Wirtschaftsuniversität Wien` — type mismatch — same span as gold: `Wirtschaftsuniversität Wien`
- `Johannes Kepler Universität Linz` — type mismatch — same span as gold: `Johannes Kepler Universität Linz`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 75** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU Wien)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU Wien)`(organisation)

**Example 76** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_11`)


 Abgangsbescheinigung der WU Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- und Sozialwissenschaften, aus welcher unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten sowie der Abschluss der Studieneingangs- und  Orientierungsphase mit 07.03.2018 hervorgeht:    [...]

**False Positives:**

- `WU Wien` — type mismatch — same span as gold: `WU Wien`
- `Abschluss` — no gold match — likely missing annotation
- `Studieneingangs` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 2

**Gold Entities:**

- `WU Wien`(organisation)

**Example 77** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

**False Positives:**

- `Johannes Kepler Universität Linz` — partial — pred is substring of gold: `Johannes Kepler Universität Linz (JKU Linz)`
- `Fassung` — no gold match — likely missing annotation
- `JKU Linz` — similar text (different position): `Johannes Kepler Universität Linz (JKU Linz)`
- `WU Wien` — type mismatch — same span as gold: `WU Wien`
- `JKU Linz` — similar text (different position): `Johannes Kepler Universität Linz (JKU Linz)`

> overlaps gold: 4  |  likely missing annotation: 1

**Gold Entities:**

- `Johannes Kepler Universität Linz (JKU Linz)`(organisation)
- `JKU Linz`(organisation)
- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 78** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_14`)


 Abgangsbescheinigung der JKU Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften (Studienplan 2018W)

**False Positives:**

- `JKU Linz` — type mismatch — same span as gold: `JKU Linz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `JKU Linz`(organisation)

**Example 79** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_16`)


 Studienerfolgsnachweis der Hamburger Fern-Hochschule betreffend den Studiengang  Betriebswirtschaft für HAK-Absolventen betreffend im Jahr 2021 absolvierte Prüfungen  vom 02.08.2021  3.

**False Positives:**

- `Hamburger Fern` — partial — pred is substring of gold: `Hamburger Fern-Hochschule`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hamburger Fern-Hochschule`(organisation)

**Example 80** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_17`)


Mit Bescheid vom 17.09.2021 forderte die belangte Behörde von der Beschwerdeführerin (=  „Bf.“) zu Unrecht bezogener Beiträge an Familienbeihilfe und Kinderabsetzbetrag von  insgesamt EUR 4.163,20 für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die  Kinder mit der SVNr.

**False Positives:**

- `Beschwerdeführerin` — no gold match — likely missing annotation
- `SVNr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 81** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_20`)


Wenn ein Studienwechsel zu einem Wegfall der Familienbeihilfe führt, besteht erst wieder  Anspruch, wenn im neuen Studium so viele Semester absolviert wurden wie im vorigen (§ 2 Abs.  1 lit. b Familienlastenausgleichsgesetz 1967 in Verbindung mit § 17 Studienförderungsgesetz  1992).

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation
- `Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 82** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_22`)


Im Rückforderungsbetrag ist die  anteilige Geschwisterstaffel für sämtliche Kinder enthalten, für die Sie im  Rückforderungszeitraum zu Unrecht Familienbeihilfe erhalten haben (§ 8 Abs. 3  Familienlastenausgleichsgesetz 1967).“  4. Dagegen erhob die Bf. rechtzeitig die Beschwerde vom 07.10.2021 und brachte vor, dass  hierbei nur ein Wechsel des Studienortes bei gleichbleibender Studienrichtung vorliege.

**False Positives:**

- `Studienortes` — no gold match — likely missing annotation
- `Studienrichtung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 83** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_23`)


Es  handle sich somit nicht um einen Studienwechsel und führe in der Folge nicht zum Wegfall der  Familienbeihilfe.

**False Positives:**

- `Folge` — no gold match — likely missing annotation
- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 84** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_24`)


Ein Vergleich der Studienrichtungen werde gerade von der  Wirtschaftsuniversität angefordert und nach Erhalt nachgereicht.

**False Positives:**

- `Studienrichtungen` — no gold match — likely missing annotation
- `Wirtschaftsuniversität` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 85** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_25`)


5. Die belangte Behörde ersuchte mit Schreiben vom 02.12.2021 die Bf. um die in der  Beschwerde angekündigte Nachreichung der Unterlagen der WU Wien (Vergleich der  Studienrichtungen).

**False Positives:**

- `Beschwerde` — no gold match — likely missing annotation
- `Unterlagen` — no gold match — likely missing annotation
- `WU Wien` — type mismatch — same span as gold: `WU Wien`
- `Studienrichtungen` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 3

**Gold Entities:**

- `WU Wien`(organisation)

**Example 86** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_26`)


6. Die Bf. antwortete mit einer am 13.12.2021 bei der belangten Behörde eingelangter Eingabe  und legte ein E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  3 von 16 Seite 4 von 16

**False Positives:**

- `Zulassungsservices Lehr` — no gold match — likely missing annotation
- `Johannes Kepler` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 87** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `WU  Wien` — type mismatch — same span as gold: `WU  Wien`
- `JKU` — type mismatch — same span as gold: `JKU`
- `Studiums` — no gold match — likely missing annotation

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

**Example 88** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_28`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“

**False Positives:**

- `Wirtschaftswissenschaften` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_29`)


Die von der belangten Behörde angeforderten Angaben der WU Wien wurden mit diesem  Schreiben jedoch nicht vorgelegt.

**False Positives:**

- `WU Wien` — type mismatch — same span as gold: `WU Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WU Wien`(organisation)

**Example 90** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_30`)


7. Mit Beschwerdevorentscheidung vom 18.03.2022 wurde die Beschwerde als unbegründet  abgewiesen und dies wie folgt begründet:  „Wenn ein Studienwechsel zu einem Wegfall der Familienbeihilfe führt, besteht erst wieder  Anspruch, wenn im neuen Studium so viele Semester absolviert wurden wie im vorigen (§ 2 Abs.  1 lit. b Familienlastenausgleichsgesetz 1967 in Verbindung mit § 17 Studienförderungsgesetz  1992).

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation
- `Anspruch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 91** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_33`)


An der WU Wien wurde das Studium  Wirtschafts- und Sozialwissenschaften (Bachelor) betrieben, in Linz handelte es sich um das  Studium Wirtschaftswissenschaften (Bachelor).

**False Positives:**

- `WU Wien` — type mismatch — same span as gold: `WU Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `WU Wien`(organisation)
- `Linz`(city)

**Example 92** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

**False Positives:**

- `Zulassungsservices Lehr` — no gold match — likely missing annotation
- `Johannes Kepler Universität Linz` — type mismatch — same span as gold: `Johannes Kepler Universität Linz`

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Johannes Kepler Universität Linz`(organisation)

**Example 93** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

**False Positives:**

- `Studien BA Sozial` — no gold match — likely missing annotation
- `WU Wien` — type mismatch — same span as gold: `WU Wien`
- `JKU Linz` — type mismatch — same span as gold: `JKU Linz`

> overlaps gold: 2  |  likely missing annotation: 1

**Gold Entities:**

- `WU Wien`(organisation)
- `JKU Linz`(organisation)

**Example 94** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_38`)


Insbesondere ist den Curricula der beiden Studien entnehmbar, dass beide Studien „dasselbe  Ausbildungsergebnis" (im Sinne der BFG-Entscheidung RV/0180-L/10) zum Ziel haben (s.  angehängte Curricula und BFG-Entscheidung).

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_42`)


Außerdem geht aus dem Curriculum hervor, dass es gemäß § 54 Abs 1 UG der Gruppe der  sozial- und wirtschaftswissenschaftlichen Studien zuzuordnen ist.

**False Positives:**

- `Gruppe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_43`)


Richtig mag sein, dass es sich - wie das Finanzamt in der Beschwerdevorentscheidung ausführt -  um kein „identes“ Studium handelt.

**False Positives:**

- `Beschwerdevorentscheidung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_44`)


Ein solches ist nach der Judikatur der Höchstgerichte zu  diesem Themenkreis jedoch nicht erforderlich.

**False Positives:**

- `Judikatur` — no gold match — likely missing annotation
- `Höchstgerichte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 98** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_45`)


Zumal es sich in Anbetracht obiger Ausführungen  aber um gleichwertige Studien handelt, ist im gegebenen Fall das Vorliegen eines  Studienwechsels zu verneinen und von einem durchgängigen Studium auszugehen, sodass die  Rückforderung der Familienbeihilfe für oben genannten Zeitraum nicht zu Recht erfolgt.

**False Positives:**

- `Familienbeihilfe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 99** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

**False Positives:**

- `Zulassungsservices Lehr` — no gold match — likely missing annotation
- `Johannes Kepler  Universität Linz` — type mismatch — same span as gold: `Johannes Kepler  Universität Linz`
- `WU  Wien` — type mismatch — same span as gold: `WU  Wien`
- `JKU` — type mismatch — same span as gold: `JKU`
- `Studiums` — no gold match — likely missing annotation

> overlaps gold: 3  |  likely missing annotation: 2

**Gold Entities:**

- `Johannes Kepler  Universität Linz`(organisation)
- `Viktoria Immohr`(person)
- `WU  Wien`(organisation)
- `JKU`(organisation)

</details>

---

## `person_complex_title_in_case`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names with complex titles (Dr., Hon.-Prof., etc.) following 'durch den Richter' or 'in der Beschwerdesache'. Uses numbered capture group for the name.

**Content:**
```
(?:durch\s+(?:den\s+Richter|die\s+Richterin)|in\s+der\s+(?:Beschwerdesache|Revisionssache|Verwaltungsstrafsache|Verfahren|Sache)\s+)(?:Hon\.-Prof\.(?:\s+Priv\.-Doz\.)?|Priv\.-Doz\.(?:\.in)?|Univ\.-Prof\.(?:\.in)?|Dr\.(?:in)?|Mag\.(?:\.in)?|OStR|OSR|MedR|Techn\s+R|HR\s+|Senatsvorsitzender|Senatsvorsitzende|Dipl\.-Ing\.|RgR|StB|Stb|OMedR|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|VetR\s+|KommR|KzlR|Ing\.|Dipl\.|Bakk\.|PhD|LLB|LL\.M|MSc|MAS|DDr\.(?:in)?|Prof\.|Ri|\u00d6kR|HR\s+KzlR|Herr|Frau|Herrn|Frauen)\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|LLB|LL\.M|MSc|PhD|Dr\.|Mag\.|Mag\.a|Mag\.in|Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|KommR|KzlR|Ing\.|Dipl\.-Ing\.|RgR|StB|Stb|MAS|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|OMedR|MedR|Dr\.in|DDr\.in|Bakk\.\s+rer\.\s+nat\.)\s*)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `person_after_genitive_role`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names following genitive role markers like 'des Beschwerdeführers', 'der Antragstellerin'. Uses numbered capture group.

**Content:**
```
(?:des\s+(?:Beschwerdeführers|Antragstellers|Antragstellersin|Klägers|Beteiligten|Vertreters|Stellvertreters)|der\s+(?:Beschwerdeführerin|Antragstellerin|Klägerin|Beteiligten|Vertreterin|Stellvertreterin))\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|LLB|LL\.M|MSc|PhD|Dr\.|Mag\.|Mag\.a|Mag\.in|Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|KommR|KzlR|Ing\.|Dipl\.-Ing\.|RgR|StB|Stb|MAS|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|OMedR|MedR|Dr\.in|DDr\.in|Bakk\.\s+rer\.\s+nat\.)\s*)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `person_title_prefix_general`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures names starting with specific titles like ÖkR, HR, Priv.-Doz. in any context. Uses numbered capture group.

**Content:**
```
(?:ÖkR|HR|Priv\.-Doz\.|Priv\.-Doz\.in|Univ\.-Prof\.|Univ\.-Prof\.in|Hon\.-Prof\.|Hon\.-Prof\.in|Dr\.|Dr\.in|DDr\.|DDr\.in|Mag\.|Mag\.a|Mag\.in|Mag\.Dr\.|Prof\.|Ri|OStR|Senatsvorsitzender|Senatsvorsitzende|Dipl\.-Ing\.|Dipl\.|Ing\.|Bakk\.|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|VetR\s+|KommR|KzlR|OMedR|MedR|OSR|StB|Stb|LLB|LL\.M|MSc|MAS|PhD|LL\.M)\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+(?:\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)*(?:\s*,\s*(?:BA|LLB|LL\.M|MSc|PhD|Dr\.|Mag\.|Mag\.a|Mag\.in|Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|KommR|KzlR|Ing\.|Dipl\.-Ing\.|RgR|StB|Stb|MAS|B\.?A\.?\s+iur|Bakk\.\s+art\.\s+MA|techn\.|OMedR|MedR|Dr\.in|DDr\.in|Bakk\.\s+rer\.\s+nat\.)\s*)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 21 | 0 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 21 | 90 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`
- `Gotthard Clement` — partial — pred is substring of gold: `Priv.-Doz. Hon.-Prof. Gotthard Clement`

> overlaps gold: 2  |  likely missing annotation: 0

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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bezirksgericht Purkersdorf`(organisation)
- `Worcester`(city)
- `Vereinigtes Königreich`(country)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


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

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_2`)


5966 230804 (Viktoria Immohr) und  4740150943 (RgR HR Reneé Schrammek) zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_18`)


5966 230804 (Viktoria Immohr) und 4740150943  (RgR HR Reneé Schrammek) gemäß § 26 Abs. 1 FLAG 1967 (Familienlastenausgleichsgesetz) in Verbindung  mit § 33 Abs. 3 EStG 1988 (Einkommensteuergesetz) zurück.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `5966 230804`(social_security_number)
- `Viktoria Immohr`(person)
- `4740150943`(social_security_number)
- `RgR HR Reneé Schrammek`(person)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_21`)


Zu RgR HR Reneé Schrammek:  Sie haben für mehr als ein Kind Familienbeihilfe bezogen.

**False Positives:**

- `Rene` — partial — pred is substring of gold: `RgR HR Reneé Schrammek`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RgR HR Reneé Schrammek`(person)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

**False Positives:**

- `Quirin Januszis` — partial — pred is substring of gold: `Priv.-Doz. Quirin Januszis`
- `Bakk` — partial — pred is substring of gold: `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Quirin Januszis`(person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.`(person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich`(address)
- `Amtes für Betrugsbekämpfung`(organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


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

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

**False Positives:**

- `Juliana Bartjen` — partial — pred is substring of gold: `Priv.-Doz.in Juliana Bartjen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Juliana Bartjen`(person)
- `Renate Brombusch`(person)
- `Langaberg 10, 5071 Himmelreich, Österreich`(address)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Estelle Niederholz` — partial — pred is substring of gold: `Dr.in Estelle Niederholz`
- `OStR Tosca Knoller` — partial — pred is substring of gold: `Hon.-Prof.in OStR Tosca Knoller`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Estelle Niederholz`(person)
- `Hon.-Prof.in OStR Tosca Knoller`(person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich`(address)
- `Anwälte Mandl & Mitterbauer GmbH`(organisation)
- `Wiesnerstraße 2, 4950  Altheim`(address)
- `01-700/4800`(tax_number)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


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

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


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

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


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

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


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

