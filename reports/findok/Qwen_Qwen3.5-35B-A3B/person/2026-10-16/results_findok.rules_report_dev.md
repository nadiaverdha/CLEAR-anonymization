# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-10-16T13:41:18.307688

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-10-16/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 3148 |
| Validation documents | 787 |
| Dev documents | 492 |
| Test documents | 495 |
| Train sentences | 6092 |
| Validation sentences | 2680 |
| Dev sentences | 61673 |
| Test sentences | 61001 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 10 |
| Max samples in prompt | 150 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | True |
| Enable Prune | False |
| Critic Interval | 20 |
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

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 98.4% |
| True Positives | 750 |
| False Positives | 429 |
| False Negatives | 1101 |
| Total Gold Entities | 1851 |
| Micro Precision | 63.6% |
| Micro Recall | 40.5% |
| Micro F1 | 49.5% |
| Macro F1 | 49.5% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Specific_Name_Trapkowski` | 1.3% | 100.0% | 0.6% | 12 | 12 | 0 |
| `Dr_G_Anonymized` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Beschwerdesache_Name_Context` | 25.6% | 92.3% | 14.9% | 298 | 275 | 23 |
| `OStR_Title` | 1.2% | 91.7% | 0.6% | 12 | 11 | 1 |
| `Priv_Dozi_Title` | 3.3% | 83.8% | 1.7% | 37 | 31 | 6 |
| `Mag_Title` | 1.1% | 83.3% | 0.5% | 12 | 10 | 2 |
| `Hon_Prof_in_Name` | 8.5% | 79.8% | 4.5% | 104 | 83 | 21 |
| `Herr_Frau_Name_Context` | 11.1% | 73.0% | 6.0% | 152 | 111 | 41 |
| `M_Anonymized` | 6.3% | 60.4% | 3.3% | 101 | 61 | 40 |
| `Herrn_Name_Full` | 3.6% | 58.6% | 1.8% | 58 | 34 | 24 |
| `Dr_Title` | 9.8% | 54.6% | 5.4% | 183 | 100 | 83 |
| `Dr_in_Title` | 1.4% | 44.8% | 0.7% | 29 | 13 | 16 |
| `Durch_Richter_Name` | 0.3% | 27.3% | 0.2% | 11 | 3 | 8 |
| `Ing_Title` | 0.5% | 11.6% | 0.3% | 43 | 5 | 38 |
| `Complainant_Beschwerdesache` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Role_Followed_Name` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Email_Header_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Representative_Dr_Mag` | 0.0% | 0.0% | 0.0% | 41 | 0 | 41 |
| `Specific_Name_Pascal_Tebbe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Lumplecker_Deych` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Gewert` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Maerkl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Joern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `RA_Mag_Start` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Anonymized_Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Anonymized_Names_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Complainant_Des_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ing_Short_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Complex_Title_Combo` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Felicitas_Niedermann` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Zeno_Schickhuber` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Claire_Hilt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Adam_Safak` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Zlatan_Frauenknecht` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Niederschrift_Name` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `OMedR_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gertrude_Haidary_Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sachverständigengutachten_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Wendelin_Polmanns` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Heiko_Dwortzak` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Marilyn_Sturtzebecher` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Raphael_Venclik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Muran_Waldhans` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Dimitri_Kozlowska` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Antragsteller_Name` | 0.0% | 0.0% | 0.0% | 57 | 0 | 57 |
| `MMag_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Marilyn_Frankenberger` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Zacharias_Herzbruch` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Esra_Lindacher` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Mehmet_Bonberg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Felix_Asenkerschbaumer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Viola_Hinterwaelder` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Rupert_Bernhardz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Evelyn_StrasserR` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Chomenko` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_R_H` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Dr_in_Nicoletta_Huberle` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Beschwerdesache_Full_Name` | 0.0% | 0.0% | 0.0% | 13 | 0 | 13 |
| `KR_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gutachten_Dr_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Richter_Name_Context` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Frau_Name_Specific` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `VetR_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KommR_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Maga_Title` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Beschwerdesache_Standalone_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `CD_Techn_R_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frau_Name_Full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dr_Initial_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Specific_Name_Trapkowski` 🏆

**F1:** 0.013 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `0311e882`  
**Description:**
Explicitly captures 'Trapkowski' (case-insensitive context) to ensure recall in citations.

**Content:**
```
\bTrapkowski\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.013 | 12 | 12 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 12 | 0 | 1839 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_36`)


10. 2015, C-378/14,  Tomislaw Trapkowski;

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_29`)


Im Urteil vom 22.10.2015, C-378/14 (Tomisiaw Trapkowski) hat der Gerichtshof der  Europäischen Union dazu folgende Rechtsansicht vertreten:   Art. 60 Abs. 1 Satz 2 der Verordnung (EG) Nr. 987/2009 des Europäischen Parlaments und des  Rates vom 16. September 2009 zur Festlegung der Modalitäten für die Durchführung der  Verordnung (EG) Nr. 883/2004 über die Koordinierung der Systeme der sozialen Sicherheit ist  dahin auszulegen, dass die in dieser Bestimmung vorgesehene Fiktion dazu führen kann, dass  3 von 33 Seite 4 von 33

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Missed by this rule (FN):**

- `Europäischen Union` (organisation)
- `Europäischen Parlaments` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_226`)


Diese Auffassung ist spätestens seit den Urteilen EuGH 11.9.2014, C-394/13, B, und EuGH  22.10.2015, C-378/14, Tomisław Trapkowski, als überholt anzusehen (vgl. BFG 7.2.2017,  RV/7106469/2016).

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_227`)


In seinem Erkenntnis VwGH 22.11.2016, Ro 2014/16/0067, hat der Verwaltungsgerichtshof  (ohne Bezug auf die Urteile EuGH 11.9.2014, C-394/13, B, und EuGH 22.10.2015, C-378/14,  Tomisław Trapkowski) klargestellt, dass im Anwendungsbereich des Unionsrechts die  Wohnortklauseln des FLAG 1967 nicht anzuwenden sind:   „14 Sowohl die Mitbeteiligte als auch deren Sohn und dessen leiblicher Vater hatten im  Streitzeitraum nach den Feststellungen im angefochtenen Erkenntnis ihren Wohnort in Ungarn  und sie sind nach dem Revisionsvorbringen sowie dem Akteninhalt ungarische  Staatsangehörige, sodass für sie die Verordnung Nr. 883/2004 gemäß deren Art. 2 Abs. 1 gilt.   15 Daher finden die auf Wohnortklauseln beruhenden Bestimmungen des § 2 Abs. 1 FLAG,  welche den Familienbeihilfenbezug auf den Wohnort im Bundesgebiet abstellt, des § 2 Abs. 8  FLAG, welche auf den wesentlich durch den Wohnort bestimmten Mittelpunkt der  Lebensinteressen im Bundesgebiet abstellt, und des § 5 Abs. 3 FLAG, das einen vom Wohnort  abhängigen Ausschluss der Familienbeihilfe bei ständigem Aufenthalt des Kindes im Ausland  vorsieht, zufolge des Art. 7 der Verordnung Nr. 883/2004 und dessen Anwendungsvorrangs  insoweit keine Anwendung.

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshof` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_276`)


10. 2015, C- 378/14, Tomisław Trapkowski, ECLI:EU:C:2015:720, entschieden, dass der  Familienbeihilfeanspruch auch einer Person, die nicht im Mitgliedstaat der Antragstellung  wohnt, zustehen kann.

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_391`)


10. 2015, C-378/14, Tomisław Trapkowski, ECLI:EU:C:2015:720, Rn. 38).

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_394`)


10. 2015, C-378/14, Tomisław Trapkowski,  ECLI:EU:C:2015:720, Rn. 41).

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138081.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138081.1_76`)


44      Insoweit ist darauf hinzuweisen, dass Art. 67 der Verordnung Nr. 883/2004 den Grundsatz  festlegt, dass eine Person Anspruch auf Familienleistungen für Familienangehörige, die in einem  anderen als dem für die Gewährung dieser Leistungen zuständigen Mitgliedstaat wohnen, so  erheben kann, als würden sie in dem zuständigen Mitgliedstaat wohnen (Urteil vom 22.  Oktober 2015, Trapkowski, C‑378/14, EU:C:2015:720, Rn. 35).

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_168`)


(vgl EuGH 18.09.2019, C-32/18, Michael Moser, EuGH 22.1.2015, C- 378/14, Omislaw Trapkowski, EuGH 14.10.2010, C-16/09, Schwemmer, BFG 27.06.2023,  RV/7105857/2017)

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_175`)


(vgl EuGH 22.10.2015, C-378/14,  Tomislaw Trapkowski, BFG 27.06.2023, RV/7105857/2017)

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_177`)


(vgl VwGH 24.06.2021, Ro 2018/16/0040, unter Hinweis auf EuGH  18.09.2019, C-32/18, Michael Moser, Rn 44 und EuGH 22.10.2015, C-378/14, Tomislaw  Trapkowski, Rn 39 bis 41)

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/144009.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144009.1_183`)


(Vgl EuGH 22.10.2015, C-378/14, Tomislaw Trapkowski, VwGH  24.06.2021, Ro 2018/16/0040, BFG 27.06.2023, RV/7105857/2017)

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Missed by this rule (FN):**

- `BFG` (organisation)

</details>

---

## `Dr_G_Anonymized` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `1de8f8b6`  
**Description:**
Captures anonymized doctor names like 'Dr. G' or 'Dr. G.' in legal contexts, ensuring the pattern is followed by a comma, space, or end of sentence to avoid partial matches.

**Content:**
```
\bDr\.(?:\s+G|\s+G\.)\b(?=,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1850 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_85`)


Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   09.02.2021: Dr. G, AM, SV-GA FLAG: 2. Befund Schielambulanz, Universitäts-Augenklinik Ort3,  vom 17.11.2015: - angeborene Hornhauttrübung BA - Hornhautvaskularisation BA 3.

| Predicted | Gold |
|---|---|
| `Dr. G` | `Dr. G` |

</details>

---

## `Beschwerdesache_Name_Context` 🏆

**F1:** 0.256 | **Precision:** 0.923 | **Recall:** 0.149  

**Format:** `regex`  
**Rule ID:** `65c42e44`  
**Description:**
Captures person names following 'in der Beschwerdesache' or 'in der Verwaltungsstrafsache', ensuring only the name is extracted, including suffixes like Bakk. phil., LL.M., MA, etc.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Verwaltungsstrafsache)\s+)(?:des\s+|der\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+LL\.M\.|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)(?=,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.923 | 0.149 | 0.256 | 298 | 275 | 23 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 275 | 23 | 1576 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Elisabeth Schafstall, Leithagürtel 20, 4251 Steinwald, Österreich, über die Beschwerde vom 22. Jänner 2020 gegen den  Bescheid des Finanzamtes Wien 2/20/21/22 vom 9. Jänner 2020, betreffend die Festsetzung  eines ersten Säumniszuschlages gemäß § 217 BAO, zu Recht:      I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elisabeth Schafstall` | `Elisabeth Schafstall` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mirha Karahodzic MA` (person)
- `Leithagürtel 20, 4251 Steinwald, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Pipers` | `Kai Pipers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Dietlind Mahlstädt` (person)
- `Gottaweg 58, 9130 Annamischl, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamt Tirol Ost` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin RI in der Beschwerdesache James Hainig,  Winterhalde 90, 9103 Wandelitzen, Österreich, über die Beschwerde vom 19. Jänner 2017 gegen den Bescheid des  Finanzamtes **** vom 21. Dezember 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und 2015 Steuernummer 85-229/2263  zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Winterhalde 90, 9103 Wandelitzen, Österreich` (address)
- `Finanzamtes` (organisation)
- `85-229/2263` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Christine Höffert` | `Christine Höffert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Adalbert Köseoglu` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Emmerich Frydrychowski` | `Emmerich Frydrychowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Walter Summersberger` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129047.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129047.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin R in der Beschwerdesache Ali Jäckle, Unterburger Straße 9T, 4972 Rabenfurt, Österreich, betreffend die Beschwerde vom 17. Dezember 2015 gegen den Bescheid des  Finanzamtes Wien 2/20/21/22 vom 3. Dezember 2015 zu Steuernummer xxxxxxxxxxxx,  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014, beschlossen:  Der Vorlageantrag vom 9. August 2016 wird gemäß § 85 Abs. 2 BAO als zurückgenommen  erklärt.

| Predicted | Gold |
|---|---|
| `Ali Jäckle` | `Ali Jäckle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Unterburger Straße 9T, 4972 Rabenfurt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129048.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129048.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Marion Endrulat, Am Schulgarten 43, 9312 Eixendorf, Österreich, über die Beschwerde vom 15. September 2019 gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 5. September 2019 betreffend Abweisung des Antrages vom 5.  April 2019 auf Gewährung der Familienbeihilfe für I.F. ab April 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marion Endrulat` | `Marion Endrulat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Schulgarten 43, 9312 Eixendorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sabine Tiedicke` | `Sabine Tiedicke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ritterhof 8, 4280 Harlingsedt, Österreich` (address)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Juri Pfluegler, Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich, über die Beschwerde vom 11. März 2019 gegen den Bescheid des Finanzamtes Wien  4/5/10 vom 27. Februar 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Pfluegler` | `Juri Pfluegler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Grund 3, 9371 St. Ulrich am Johannserberg, Österreich` (address)
- `Finanzamtes Wien  4/5/10` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_2`)


Das Bundesfinanzgericht hat durch den RichterR, in der Beschwerdesache Basil Staerk, Stampflweg 28, 4861 Raschbach, Österreich, vertreten durch WP, betreffend Beschwerde vom 18. Dezember 2013 gegen die  Bescheide des Finanzamtes X vom 09.12.2013    betreffend Einkommensteuer für das Jahr 2003 und    über die Festsetzung von Anspruchszinsen 2003,  Steuernummer 60-450/8034  beschlossen:  Der Antrag auf Entscheidung über die Beschwerde durch das Verwaltungsgericht  (Vorlageantrag) wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stampflweg 28, 4861 Raschbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `60-450/8034` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Charles Rybalka` | `Charles Rybalka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Eduard Lembrechts` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Florentin Pawils` | `Florentin Pawils` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Alva Jodgalweit` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Thomas Mevis` | `Thomas Mevis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Anna Radschek` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129491.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129491.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.DDr. Hedwig Bavenek-Weber in der  Beschwerdesache Merlin Feucht, Alte Straße 2, 8114 Unterfriesach, Österreich, über die Beschwerde vom 12. Dezember 2011  gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 14.  November 2011, Steuernummer 57-396/6782, betreffend die Festsetzung der ermäßigten  Glücksspielabgabe gemäß § 58 Abs. 3 GSpG für Glücksspiele im Rahmen von Gewinnspielen  (Preisausschreiben), zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Merlin Feucht` | `Merlin Feucht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.DDr. Hedwig Bavenek-Weber` (person)
- `Alte Straße 2, 8114 Unterfriesach, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `57-396/6782` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Sieglinde Kießerling, Stockenhuberweg 62, 2732 Raglitz, Österreich, vertreten durch MITTEREGGER Steuerberatungs GmbH,  Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 31. August 2019 gegen den Bescheid  des Finanzamtes Waldviertel vom 1. August 2019 betreffend Einkommensteuer 2017  Steuernummer 27-927/6451  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Sieglinde Kießerling` | `Sieglinde Kießerling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Stockenhuberweg 62, 2732 Raglitz, Österreich` (address)
- `MITTEREGGER Steuerberatungs GmbH` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `27-927/6451` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Stiller` | `Elias Stiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Michaela Dehnert` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Leroy Sitterle` | `Leroy Sitterle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Univ.-Prof.in Ada Schaeferlein` (person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich` (address)
- `Astoria Stb GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/129845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129845.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hermine Roj  in der Beschwerdesache Corinna Farke,  Millenniumsstraße 12, 4730 Sittling, Österreich, über die Beschwerde vom 12. April 2015 gegen den Bescheid des Finanzamt Linz  vom 12. März 2015 betreffend Beschwerdezinsen gemäß § 205a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Corinna Farke` | `Corinna Farke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Hermine Roj` (person)
- `Millenniumsstraße 12, 4730 Sittling, Österreich` (address)
- `Finanzamt Linz` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Josefine Frikel` | `Josefine Frikel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Huberta Hammers` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Hermine Ruprich` | `Hermine Ruprich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Rosamunde Galanidis` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Mag. Wolfgang Moser` (person)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wolfgang Tiwald` (person)
- `Egererweg 9, 5760 Niederhaus, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130360.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Fridolin Rummler  in der Beschwerdesache Annemarie Goncalves,  Unter Trift 7, 4904 Reichering, Österreich, über die Beschwerde vom 26. August 2019 gegen die Bescheide des Finanzamt Judenburg Liezen  vom 8. August 2019 betreffend Pfändung einer Geldforderung sowie die Festsetzung von  Gebühren und Auslagenersätzen des Vollstreckungsverfahrens zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Annemarie Goncalves` | `Annemarie Goncalves` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Fridolin Rummler` (person)
- `Unter Trift 7, 4904 Reichering, Österreich` (address)
- `Finanzamt Judenburg Liezen` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Zarin Eckartz  in der Beschwerdesache Volkmar Oortwyn,  Steg 1944 48, 4890 Röth, Österreich, über die Beschwerde vom 19. Februar 2020 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020 betreffend  Gebühren 2020 Steuernummer 72-008/7613  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Volkmar Oortwyn` | `Volkmar Oortwyn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Zarin Eckartz` (person)
- `Steg 1944 48, 4890 Röth, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `72-008/7613` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/130473.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj in der Beschwerdesache  Vera Matyschek, Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich, über die Beschwerde vom 23. März 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 12. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Vera Matyschek` | `Vera Matyschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Oskar-Grissemann-Straße 16, 9560 Goggau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sean Herdling` | `Sean Herdling` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `J. Heiser-Straße 3, 8361 Hatzendorf, Österreich` (address)
- `NÖ Landesverein für Erwachsenenschutz` (organisation)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/130592.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Imre Annecke, Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich, über die Beschwerde vom 18. Juni 2020 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 2. Juni 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Imre Annecke` | `Imre Annecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter-Zeman-Gasse 24, 3650 Dietsam, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/130599.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130599.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Othmar Feuerbaum  in der Beschwerdesache Ingeborg Kollaczek,  Hufgasse 10, 9062 Gabriel, Österreich, vertreten durch Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft, Dresdner Straße 87 Tür A21, 1200 Wien, über die Beschwerde  vom 23. November 2011 gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom  14. November 2011 betreffend Festsetzung von ersten Säumniszuschlägen, Steuernummer 09- 47-554/2547, Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die angefochtenen  Bescheide wie folgt abgeändert:   Der Säumniszuschlag zur Lohnsteuer 2006 wird mit € 660,05 anstatt bisher € 673,07,   der Säumniszuschlag zum DB 2006 mit € 64,04 anstatt bisher € 75,55,  der Säumniszuschlag zur Lohnsteuer 2007 mit € 776,27 anstatt bisher € 861,05 und   der Säumniszuschlag zum DB 2007 mit € 74,43 anstatt bisher € 104,34 festgesetzt.

| Predicted | Gold |
|---|---|
| `Ingeborg Kollaczek` | `Ingeborg Kollaczek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Othmar Feuerbaum` (person)
- `Hufgasse 10, 9062 Gabriel, Österreich` (address)
- `Veltzé, Mares & Partner KG Wirtschaftstreuhand- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `47-554/2547` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melina Bankratz  in der Beschwerdesache Lars Huesgen,  Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich, vertreten durch RA, gegen die Bescheide des Finanzamtes Salzburg-Land vom  16. Mai 2019, betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013  und Einkommensteuer 2013, die Bescheide des Finanzamtes Salzburg-Land vom 17. Mai 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2014, 2015 und  Einkommensteuer 2014, 2015, und die vermeintlichen Bescheide des Finanzamtes Salzburg- Land, betreffend Festsetzung von Anspruchszinsen 2013, 2014, 2015, beschlossen:  1.

| Predicted | Gold |
|---|---|
| `Lars Huesgen` | `Lars Huesgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Melina Bankratz` (person)
- `Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Rudolf Bogdanowic, Am Gehrn 3, 9312 Gaming, Österreich, über die Beschwerde vom 9. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 9. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 90-074/8383  nach Durchführung einer  mündlichen Verhandlung am 4. Dezember 2019 und 16. Oktober 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rudolf Bogdanowic` | `Rudolf Bogdanowic` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Am Gehrn 3, 9312 Gaming, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `90-074/8383` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/130799.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Rosemarie Schan, SDL Augustinerwald 45, 4573 Tambergau, Österreich, über die Beschwerde vom 28. Dezember 2018 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 28. November 2018 betreffend Abweisung  des Antrages auf Gewährung von Familienbeihilfe und des Erhöhungsbetrages zur  Familienbeihilfe für den Zeitraum Mai 2016 bis Oktober 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Schan` | `Rosemarie Schan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `SDL Augustinerwald 45, 4573 Tambergau, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/130979.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130979.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Susette Bertnik, Ehrenbachweg 31, 9322 Hirt, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes Wien 1/23 vom 16. Juli  2019 betreffend Einkommensteuer 2018 Steuernummer 32-807/7639  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susette Bertnik` | `Susette Bertnik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ehrenbachweg 31, 9322 Hirt, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `32-807/7639` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Ottfried Ficici, Wilfersdorf 3, 4890 Asten, Österreich, über die Beschwerden vom 19. April 2018 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 17. April 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 und 2013 Steuernummer 51-452/2856  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ottfried Ficici` | `Ottfried Ficici` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Wilfersdorf 3, 4890 Asten, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `51-452/2856` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/131159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131159.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Roderich Determann,  Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich, über die Beschwerde vom 28. Jänner 2020 gegen den Bescheid des  Finanzamtes Salzburg-Stadt vom 8. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 80-721/3378, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Roderich Determann` | `Roderich Determann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leopold-Hanninger-Gasse 20B, 4115 Edwiese, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `80-721/3378` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Jacqueline Dittus, Sausal 90O, 4911 Schönfeld, Österreich, vertreten durch Dkfm. Anton Lammer  Wirtschaftstreuhand GmbH, Oskar-Kokoschka-Straße 8, 3380 Pöchlarn, über die Beschwerde  vom 17. September 2014 gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  5. September 2014 betreffend Einkommensteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jacqueline Dittus` | `Jacqueline Dittus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Freilinger` (person)
- `Sausal 90O, 4911 Schönfeld, Österreich` (address)
- `Anton Lammer  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Titus Ohlmer` | `Titus Ohlmer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich` (address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-234/9874` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Edwin Pfaefflin, Steinwiese 17, 3683 Nächst Altenmarkt, Österreich, betreffend Beschwerde vom 24. Jänner 2020  gegen die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 8. März 2017 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und vom 23.1.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 35-514/8431,  beschlossen:   Die Vorlageanträge vom 4.5.2020 gegen die Beschwerdevorentscheidung (BVE) 2016 vom  6.2.2020 und vom 8.5.2020 gegen die BVE 2017 werden gemäß § 260 Abs. 1 BAO in  Verbindung mit § 264 Abs. 4 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Edwin Pfaefflin` | `Edwin Pfaefflin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Steinwiese 17, 3683 Nächst Altenmarkt, Österreich` (address)
- `Finanzamtes` (organisation)
- `35-514/8431` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Maximiliane Kotenbeutel, Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich, über die Beschwerde vom 24. September 2014 gegen den Bescheid des Finanzamtes  Österreich vom 8. August 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013, Steuernummer 69-367/5691, zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Maximiliane Kotenbeutel` | `Maximiliane Kotenbeutel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hinterer Bahnweg 75, 9500 Oberwollanig, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `69-367/5691` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Kirstin Matiascheck  in der Beschwerdesache   Annemarie Schwinge, Rametzhofen 15, 3392 Hohenwarth, Österreich, über die Beschwerde vom 12. August 2015 gegen den Bescheid des  Finanzamtes Österreich vom 5. August 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014, Steuernummer 32-672/7699, zu Recht erkannt:   Der Beschwerde wird im Ausmaß der Beschwerdevorentscheidung vom 03. Mai 2016 teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Annemarie Schwinge` | `Annemarie Schwinge` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Kirstin Matiascheck` (person)
- `Rametzhofen 15, 3392 Hohenwarth, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-672/7699` (tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Achmed Karolzak  in der Beschwerdesache Lilia Löffelmann,  Karl Heinschild-Weg 29, 4980 Hübing, Österreich, vertreten durch M. Thaler Steuerberatung Kufstein GmbH, Prof. Sinwel-Weg 4,  6330 Kufstein, über die Beschwerde vom 5. September 2018 gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 8. August 2018 betreffend Wiederaufnahme der Verfahren  hinsichtlich Einkommensteuer für die Jahre 2012 bis 2015 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lilia Löffelmann` | `Lilia Löffelmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Achmed Karolzak` (person)
- `Karl Heinschild-Weg 29, 4980 Hübing, Österreich` (address)
- `M.` (person)
- `Finanzamtes` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Olivia Ziegeler  in der Beschwerdesache Mike Reislehner,  Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich, über die Beschwerde vom 21. März 2017 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 15. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 Steuernummer 44-773/5557  zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mike Reislehner` | `Mike Reislehner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Olivia Ziegeler` (person)
- `Girtenhofweg 1, 7511 Rohrbach an der Teich, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `44-773/5557` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Gregor Klocksin` | `Gregor Klocksin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Unterguntschach 85, 3525 Armschlag, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

| Predicted | Gold |
|---|---|
| `Chiara Duchan` | `Chiara Duchan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich` (address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marceline Flory  in der Beschwerdesache Stephan Zeitlhuber,  Ödgegend 6, 4230 Selker, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die Beschwerden vom  9. November 2020 und vom 27. November 2020 gegen die Bescheide des Finanzamtes Wien  1/23 vom 6. Oktober 2020, Steuernummer 55-544/4748, betreffend  Energieabgabenvergütung für 2-12/2011 und für 2012 und über die Beschwerden vom  27. November 2020 gegen die Bescheide vom 2. November 2020 betreffend  Energieabgabenvergütung für 1-9/2013 und für 10/2013–9/2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Stephan Zeitlhuber` | `Stephan Zeitlhuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Marceline Flory` (person)
- `Ödgegend 6, 4230 Selker, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien  1/23` (organisation)
- `55-544/4748` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131981.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131981.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Susette Glaeßel  in der Beschwerdesache des  Karl Morgenbesser, Am Saffenfeld 29, 9714 Kreuzen, Österreich, über die Beschwerde vom 1. Oktober 2012 gegen die Bescheide  des Finanzamtes Innsbruck vom 21. September 2012 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer 2010, Einkommensteuer 2010 und Anspruchszinsen  2010 zu Steuernummer zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Einkommensteuer 2010 wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Karl Morgenbesser` | `Karl Morgenbesser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Susette Glaeßel` (person)
- `Am Saffenfeld 29, 9714 Kreuzen, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Frauke Galleithner` | `Frauke Galleithner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich` (address)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Heike Lehmensieck` | `Heike Lehmensieck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- `Höllstein 11, 9852 Neuschitz, Österreich` (address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christoph Hasenfraz  in der Beschwerdesache Olivia Sahlmüller,  Zinöck 26, 5134 Sengthal, Österreich, gegen den am 9. April 2018 ausgefertigten Bescheid der belangten Behörde  FA Grieskirchen Wels, nunmehr Finanzamt Österreich, betreffend Einkommensteuer für das Jahr 2017 und  den am 12. März 2019 von derselben Behörde ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Olivia Sahlmüller` | `Olivia Sahlmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Christoph Hasenfraz` (person)
- `Zinöck 26, 5134 Sengthal, Österreich` (address)
- `FA Grieskirchen Wels` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

| Predicted | Gold |
|---|---|
| `Gebhard Klutentreter` | `Gebhard Klutentreter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Pfiferweg 136, 4906 Feichtet, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_3`)


in der Beschwerdesache Kimberly Jeworski, Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51, 1090 Wien,  betreffend Beschwerde vom 31. August 2015 gegen die Bescheide des Finanzamtes Graz-Stadt  vom 9. Juni 2015 betreffend Umsatzsteuer 2011, 2012 und 2013, Steuernummer beschlossen:   Die Beschwerde vom 31. August 2015 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Kimberly Jeworski` | `Kimberly Jeworski` |

**Missed by this rule (FN):**

- `Stadtfeldstraße 23, 5134 Siebenmaiern, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Sandra Fenn, Myrbachgasse 59, 8403 Ragnitz, Österreich, vertreten durch Mag. Manuela Meyerhofer, Handlirschgasse 11, 1170 Wien, über die  Beschwerde vom 18. Jänner 2016 gegen den Bescheid des Finanzamtes Bruck Eisenstadt  Oberwart vom 15. Dezember 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2014, Steuernummer 49-433/1564, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sandra Fenn` | `Sandra Fenn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Myrbachgasse 59, 8403 Ragnitz, Österreich` (address)
- `Mag. Manuela Meyerhofer` (person)
- `Finanzamtes Bruck Eisenstadt  Oberwart` (organisation)
- `49-433/1564` (tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Verwaltungsstrafsache Aron Pommeränke,  Seenplattenweg 7, 4190 Oberstiftung, Österreich, betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit §  16 Abs. 1 und Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für  Wien Nr. 20, in der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, über die  Beschwerde des Beschuldigten vom 26. Jänner 2021 gegen das Erkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 29. Dezember 2020, GZ. MA6/2019,  beschlossen:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 28 Abs. 1  VwGVG, § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG), § 13 Allgemeines  Verwaltungsverfahrensgesetz 1991 (AVG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird das Beschwerdeverfahren eingestellt.  II. Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

| Predicted | Gold |
|---|---|
| `Aron Pommeränke` | `Aron Pommeränke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Seenplattenweg 7, 4190 Oberstiftung, Österreich` (address)
- `Stadt Wien` (organisation)
- `Magistrates der  Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/132944.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132944.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Sandmüller, Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich, über die Beschwerde vom 21. November 2018 gegen den Bescheid des FA vom  14. November 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht  erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Sandmüller` | `Lisa Sandmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erich-Landgrebe-Straße 38, 3205 Edlitz, Österreich` (address)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Jonas Gutkauf, Auvorstadtgasse 59, 8184 Floing, Österreich, über die Beschwerden vom 10. März 2021 gegen  die Bescheide des Finanzamtes Österreich vom 10. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 und Einkommensteuer (Arbeitnehmerveranlagung) 2018  sowie vom 23. Februar 2021 gegen den Bescheid des Finanzamtes Österreich vom 19. Februar  2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Jonas Gutkauf` | `Jonas Gutkauf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Adebiola Bayer` (person)
- `Auvorstadtgasse 59, 8184 Floing, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich, über die Beschwerde vom 18. Mai 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-300/4861  beschlossen:  Der Vorlageantrag vom 14.10.2020 gegen die Beschwerdevorentscheidung vom 31.07.2020  betreffend Einkommensteuer 2018 wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Fiona Buedenbender` | `Fiona Buedenbender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich  über die Beschwerde vom 10. August 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 30. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 92-300/4861  zu Recht erkannt:  Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Fiona Buedenbender` | `Fiona Buedenbender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich` (address)
- `Finanzamtes` (organisation)
- `92-300/4861` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl, in der Beschwerdesache  Tristan Potente, Hürth 5, 4362 Schönfichten, Österreich, vertreten durch E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Bergmannstraße 7, 6850 Dornbirn, betreffend den Vorlageantrag vom  31. Oktober 2017 gegen die Beschwerdevorentscheidung des Finanzamtes Bregenz 12.  September 2017 betreffend Einkommensteuer 2009 Steuernummer 61-467/9522  beschlossen:  Der Vorlageantrag wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Tristan Potente` | `Tristan Potente` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Hürth 5, 4362 Schönfichten, Österreich` (address)
- `E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)
- `61-467/9522` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. René Neuendorf  in der Beschwerdesache Kevin Damiani,  Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich, gegen  1. den am 12. Jänner 2016 ausgefertigten Bescheid der belangten Behörde Finanzamt Oststeiermark,  nunmehr Finanzamt Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2013 und  2. den am 1. Februar 2018 ausgefertigten Bescheid der belangten Behörde FA Oststeiermark,  nunmehr FA Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2014  zu Recht erkannt  I. Die angefochtenen Bescheide betreffend Körperschaftsteuer für die Jahre 2013 und 2014  werden abgeändert.

| Predicted | Gold |
|---|---|
| `Kevin Damiani` | `Kevin Damiani` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. René Neuendorf` (person)
- `Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich` (address)
- `Finanzamt Oststeiermark` (organisation)
- `Finanzamt Oststeiermark` (organisation)
- `FA Oststeiermark` (organisation)
- `FA Oststeiermark` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Timothy Overlaender, Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich, über die Beschwerde vom 18. Dezember 2018 gegen den Bescheid  des Finanzamtes Graz-Stadt vom 22. November 2018 betreffend Umsatzsteuer 2015 und  Umsatzsteuer 2016 Steuernummer 51-515/5009  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Timothy Overlaender` | `Timothy Overlaender` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Alois Pichler` (person)
- `Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `51-515/5009` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Fatima Eichmayr, Wieskapellenweg 10, 8047 Graz, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in 5020 Salzburg, Hellbrunner Straße 5,  über die Beschwerde vom 8. Jänner 2010 gegen die Bescheide des Finanzamtes Salzburg-Stadt  (nunmehr: Finanzamt Österreich) vom 12. November 2009 betreffend Haftung für  Kapitalertragsteuer für 2004 bis 2008, Steuernummer 67-455/2359, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Fatima Eichmayr` | `Fatima Eichmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieskapellenweg 10, 8047 Graz, Österreich` (address)
- `Dr. Klaus Plätzer,` (person)
- `Finanzamtes Salzburg-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `67-455/2359` (tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lee Kubbig` | `Lee Kubbig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/134083.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134083.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinI. in der Beschwerdesache Violetta Bailmann, Schlosserfeld 35, 9632 Hochwart, Österreich, vertreten durch Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG, Olympiastraße 17, 6020 Innsbruck, über die Beschwerde vom 20. Oktober 2016 gegen  die Bescheide des Finanzamtes Spittal Villach vom 22. September 2016 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012 (Steuernummer  82-877/4906 ) zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Violetta Bailmann` | `Violetta Bailmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schlosserfeld 35, 9632 Hochwart, Österreich` (address)
- `Vogelsberger Hoffmann Wacker & Partner Steuerberatungs GmbH &  Co KG` (organisation)
- `Finanzamtes Spittal Villach` (organisation)
- `82-877/4906` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Bernhard Maximowa` | `Bernhard Maximowa` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wienergraben 7, 2870 Inneraigen, Österreich` (address)
- `Mag. Robert Dax` (person)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Erwin Döpkemeier` | `Erwin Döpkemeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvia Gebhart` (person)
- `Minithal 3, 5360 Markt, Österreich` (address)
- `Mag Kerstin Friedrich` (person)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamt  Österreich` (organisation)
- `02-365/4052` (tax_number)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

| Predicted | Gold |
|---|---|
| `Dora Szczepanowski` | `Dora Szczepanowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Markus Knechtl LL.M.` (person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich` (address)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Moses Dannebohm  in der Beschwerdesache Ruperta Schluckner,  Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich, vertreten durch WINKEL STEINER WAIBEL Steuerberater GmbH, Schweizer  Straße 77, 6845 Hohenems, über die Beschwerde vom 18. Februar 2019 gegen die Bescheide  des Finanzamtes Feldkirch vom 23. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 bis 2017 zu Recht erkannt:   I. Die angefochtenen Bescheide werden im Umfang der Einkommensteuerbescheide  (Beschwerdevorentscheidungen) 2015 bis 2017 vom 9. Dezember 2019 abgeändert.

| Predicted | Gold |
|---|---|
| `Ruperta Schluckner` | `Ruperta Schluckner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Moses Dannebohm` (person)
- `Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich` (address)
- `WINKEL STEINER WAIBEL Steuerberater GmbH` (organisation)
- `Finanzamtes Feldkirch` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Petra Schippan  in der Beschwerdesache Judith Kapelle,  Saßbergweg 17, 4860 Haid, Österreich, betreffend Beschwerde vom 2. September 2012 gegen den Bescheid des FA  Waldviertel vom 3. August 2012 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2011 Steuernummer 31-042/8347  beschlossen:     Der Vorlageantrag vom 30.11.2012 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264  Abs. 4 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Judith Kapelle` | `Judith Kapelle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Petra Schippan` (person)
- `Saßbergweg 17, 4860 Haid, Österreich` (address)
- `FA  Waldviertel` (organisation)
- `31-042/8347` (tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/134561.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134561.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache James Jantschke,  Oberpeilstein 6, 3205 Grub, Österreich, betreffend Beschwerde vom 18. Februar 2021 gegen die  Umsatzsteuerbescheide 2017 und 2018 des Finanzamtes Österreich vom 22. Jänner 2021  beschlossen:  Die mit 27.05.2021 datierten und am 28.05.2021 eingebrachten Vorlageanträge betreffend die  Beschwerdevorentscheidungen vom 22.03.2021 werden gemäß § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `James Jantschke` | `James Jantschke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberpeilstein 6, 3205 Grub, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR. in der Beschwerdesache August Cernyj, Lusthausstraße 569, 4901 Bruckmühl, Österreich, vertreten durch Casapicola & Gross Wirtschafts- prüfungs- und Steuerberatungs  GmbH, Gluckgasse 3 Tür 15, 1010 Wien, über die Beschwerde vom 19. Juni 2019 gegen die  Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt für Großbetriebe) datiert jeweils  vom 30. April 2019 betreffend Umsatzsteuer für die Jahre 2013 bis 2016 und  Körperschaftsteuer für die Jahre 2013 – 2015 , Steuernummer 12-317/0890  zu Recht  erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `August Cernyj` | `August Cernyj` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lusthausstraße 569, 4901 Bruckmühl, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `12-317/0890` (tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Miranda Weissert` | `Miranda Weissert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Maurice Bettenhäuser` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Nancy Stuckenschneider  in der Beschwerdesache des  Bruno Karahasan, Ludowikaweg 5, 3602 Bacharnsdorf, Österreich, über die Beschwerde vom 2. Juli 2019 gegen den Bescheid des  FA St. Johann Tamsweg Zell am See  vom 26. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zur Steuernummer 12-630/0045  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Bruno Karahasan` | `Bruno Karahasan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Priv.-Doz.in Nancy Stuckenschneider` (person)
- `Ludowikaweg 5, 3602 Bacharnsdorf, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `12-630/0045` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Rauner, die RichterinR  sowie die fachkundigen Laienrichter Gregor Ableidinger und Dr. Franz Kandlhofer in der  Beschwerdesache Lieselotte Schluessel, Hannakstraße 205, 5121 Wimm, Österreich, über die Beschwerde vom 22. Februar 2016  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 10. Februar 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Lieselotte Schluessel` | `Lieselotte Schluessel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Rauner` (person)
- `Gregor Ableidinger` (person)
- `Dr. Franz Kandlhofer` (person)
- `Hannakstraße 205, 5121 Wimm, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Walter Monheim  in der Beschwerdesache Enrico Steudtle,  Assing 21, 9071 Wurdach, Österreich, vertreten durch GEYER & GEYER Wirtschaftstreuhand GmbH, Rudolf von Alt- Platz 1, 1030 Wien, hinsichtlich der Beschwerde vom 23. November 2011 gegen die Bescheide  des Finanzamtes Wien 2/20/21/22 - nunmehr Finanzamtes Österreich - vom 25. Oktober 2011  betreffend Festsetzung der Kapitalertragsteuer 2007 bis 2010, Steuernummer  10-940/7308, den Beschluss:   I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als  unzulässig geworden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Enrico Steudtle` | `Enrico Steudtle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Walter Monheim` (person)
- `Assing 21, 9071 Wurdach, Österreich` (address)
- `GEYER & GEYER Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Österreich` (organisation)
- `10-940/7308` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Laurin Überschar  in der Beschwerdesache Albert Theiselmann,  Hochmark 31g, 8323 Unterbuch, Österreich, vertreten durch Radike, Hammerl & Partner Steuerberatung GmbH,  Bisamberger Straße 2/1/8, 2100 Korneuburg, betreffend Beschwerde vom 17. Juni 2021 gegen  die Bescheide des Finanzamtes Österreich vom 20. Mai 2021 betreffend Einkommensteuer  2015 und 2016, Steuernummer 15-781/1702, den Beschluss:   I. Die Beschwerde wird gemäß § 256 Abs 3 Bundesabgabenordnung (BAO) als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Albert Theiselmann` | `Albert Theiselmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Laurin Überschar` (person)
- `Hochmark 31g, 8323 Unterbuch, Österreich` (address)
- `Radike, Hammerl & Partner Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `15-781/1702` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Ri, die Richterin Mag. Riin sowie  die fachkundigen Laienrichter A und B, in der Beschwerdesache Karina Schliekau, Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich,  vertreten durch die Kanzlei, über die Beschwerde vom 15. Februar 2018 gegen den Bescheid  des Finanzamtes Österreich, vormals Finanzamt Wien 3/6/7/11/15 Schwechat und Gerasdorf,  vom 1. Februar 2018 betreffend Feststellung der Einkünfte § 188 BAO 2016, nach  Durchführung einer mündlichen Verhandlung am 17. November 2021 in Anwesenheit der  Schriftführerin C, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Karina Schliekau` | `Karina Schliekau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Riin` (person)
- `Dr.H.Bantleon-Weg 44, 4121 Wollmannsberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Wien 3/6/7/11/15` (organisation)

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/135460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Hugo Engelsmann, Erlach 22, 3921 Kleinpertholz, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich vom 20. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-631/7208  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hugo Engelsmann` | `Hugo Engelsmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Erlach 22, 3921 Kleinpertholz, Österreich` (address)
- `Alfred Klaus Fenzl` (person)
- `Finanzamtes Österreich` (organisation)
- `83-631/7208` (tax_number)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Armin Heckemanns, Nabuccogasse 10, 2630 Ternitz, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, (im  Beschwerdeverfahren nicht eingeschritten), über die Beschwerde vom 10. Februar 2020 gegen  den Einkommensteuerbescheid 2018 des Finanzamtes Baden Mödling vom 10. Jänner 2020  (und gemäß § 253 Satz 1 BAO auch gegen den Einkommensteuerbescheid 2018 vom  18. September 2020) zu Steuernummer 75-597/1615  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Armin Heckemanns` | `Armin Heckemanns` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nabuccogasse 10, 2630 Ternitz, Österreich` (address)
- `Dr. Silvia Gredenberg` (person)
- `Finanzamtes Baden Mödling` (organisation)
- `75-597/1615` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi als Vorsitzenden, den Richter Ri2 als  beisitzender Richter, SenLR1 als fachkundiger Laienrichter und SenLR2 als fachkundiger  Laienrichter in der Beschwerdesache Alois Kleynsteuber, Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich, vertreten durch Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien,  über die Beschwerde vom 14. September 2012 gegen den Bescheid des FA Wien 9/18/19  Klosterneuburg vom 6. September 2012, StNr. 79-708/0061, betreffend Einkommensteuer  2008 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alois Kleynsteuber` | `Alois Kleynsteuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ferdinand Kuchelbacher-Gasse 31, 9342 Reichenhaus, Österreich` (address)
- `Hallas &  Partner Wirtschaftsprüfung und Steuerberatung GmbH & Co KG` (organisation)
- `FA Wien 9/18/19  Klosterneuburg` (organisation)
- `79-708/0061` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/135727.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135727.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Dimitri Isakova, Hörgattern 37, 3244 Kühberg, Österreich, über die Beschwerde vom 1. Juni 2017 gegen  den Bescheid des Finanzamtes Österreich vom 15. Mai 2017 betreffend Familienbeihilfe  01.2016-12.2016 Steuernummer 93-163/8536  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, dass dieser betreffend T1 hinsichtlich der Monate April, August und  September 2016 ersatzlos aufgehoben wird.

| Predicted | Gold |
|---|---|
| `Dimitri Isakova` | `Dimitri Isakova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Hörgattern 37, 3244 Kühberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `93-163/8536` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/135941.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135941.1_1`)


BESCHLUSS   Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Frederike Lipienski  in der Beschwerdesache des  Hademar Rüstow, Eck 124T, 2214 Auersthal, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des  FA Amstetten Melk Scheibbs (FA) vom 10. März 2021 über die Abweisung eines Antrages auf Wiederaufnahme §  303 BAO /  ESt 2017 zur Steuernummer 71-651/2158  beschlossen:   Der Vorlageantrag vom 29.Sept.2021 wird gemäß § 260 Abs. 1 lit. a iVm § 264 Abs. 4 lit e und  Abs. 5 BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hademar Rüstow` | `Hademar Rüstow` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Frederike Lipienski` (person)
- `Eck 124T, 2214 Auersthal, Österreich` (address)
- `FA Amstetten Melk Scheibbs` (organisation)
- `71-651/2158` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/135983.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135983.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den SenatsvorsitzendenRichter1, den RichterRichter2 sowie  die fachkundigen Laienrichter TitelRichter3 Richter3 und Richter4 in der Beschwerdesache  Gabriele Kuehberger, Wieser 53, 8341 Puch, Österreich, vertreten durch Steuerberatungsgesellschaft, über die Beschwerde  vom 19. Februar 2019 gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom  16. Januar 2019 zu St.Nr. Steuernummer über die Festsetzung einer Zwangsstrafe, nach  Durchführung einer mündlichen Verhandlung am 7. März 2022 in Anwesenheit der  Schriftführerin Schriftführerin1 zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Gabriele Kuehberger` | `Gabriele Kuehberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieser 53, 8341 Puch, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dietmar Kachelmuss` | `Dietmar Kachelmuss` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Christian Lemanowitz` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Sulamith Jedwillat, Brandenbergweg 15, 8353 Pichla, Österreich, vertreten durch Mag. Michael Payr, Albertgasse 6/14, 1080 Wien, über die  Beschwerde vom 25. Oktober 2018 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf, nunmehr Finanzamt Österreich, vom 19. September 2018 betreffend  Körperschaftsteuer 2014, Steuernummer 41-852/7395, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sulamith Jedwillat` | `Sulamith Jedwillat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Brandenbergweg 15, 8353 Pichla, Österreich` (address)
- `Mag. Michael Payr` (person)
- `Finanzamtes Wien 12/13/14  Purkersdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `41-852/7395` (tax_number)

**Example 82** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sheila Nonnmacher  in der Beschwerdesache Sieglinde Semertzidou,  Bürgerspitalstraße 8, 9361 Judendorf, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, über  die Beschwerde vom 20.03.2017 gegen die Umsatzsteuerbescheide 2007 bis 2008 „aufgrund  der BP“, Steuernummer 76-265/6028, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Sieglinde Semertzidou` | `Sieglinde Semertzidou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Sheila Nonnmacher` (person)
- `Bürgerspitalstraße 8, 9361 Judendorf, Österreich` (address)
- `Dr. Silvia Gredenberg` (person)
- `76-265/6028` (tax_number)

**Example 83** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karina von Wnuck-Lipinski  in der Beschwerdesache Rosemarie Fortwängler,  Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich, über die Beschwerde vom 4. Oktober 2019 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 26. September 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe (FB) und  Kinderabsetzbetrag (KG) für den Zeitraum Oktober 2017 bis Feber 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rosemarie Fortwängler` | `Rosemarie Fortwängler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Karina von Wnuck-Lipinski` (person)
- `Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `FA Österreich` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mag. Yorick Schlenbäcker  in der Beschwerdesache Kordula Arlov,  Stranitzkygasse 33, 8251 Karnerviertel, Österreich, über die Beschwerde vom 19.6.2018 gegen den Bescheid des Finanzamtes  Oststeiermark vom 8.6.2018 betreffend Einkommensteuer 2014 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO entsprechend der  Beschwerdevorentscheidung vom 10.9.2018 abgeändert.

| Predicted | Gold |
|---|---|
| `Kordula Arlov` | `Kordula Arlov` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Mag. Yorick Schlenbäcker` (person)
- `Stranitzkygasse 33, 8251 Karnerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 85** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Peter Steurer, die Richterin  Mag. Natascha Gassner, die fachkundige Laienrichterin Mag. Renate Burtscher und den  fachkundigen Laienrichter Bernd Feldkircher in der Beschwerdesache Vincent Kohlstruk, Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich,  vertreten durch die Bischof-Fuchs Steuerberatungs GmbH, Dorf Rieden 12, 6900 Bregenz,  gegen den Bescheid des Finanzamtes Bregenz vom 6. Juni 2018 betreffend Einkommensteuer  2017 nach Durchführung einer mündlichen Verhandlung am 21. April 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen;

| Predicted | Gold |
|---|---|
| `Vincent Kohlstruk` | `Vincent Kohlstruk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Mag. Natascha Gassner` (person)
- `Mag. Renate Burtscher` (person)
- `Bernd Feldkircher` (person)
- `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich` (address)
- `Bischof-Fuchs Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 86** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ludger Endel, Kleinsierning 2, 5114 Mittergöming, Österreich, betreffend Beschwerde vom 15. Dezember 2021  gegen den Bescheid des Finanzamtes Österreich vom 2. Februar 2022 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 63-868/1042,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ludger Endel` | `Ludger Endel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Kleinsierning 2, 5114 Mittergöming, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `63-868/1042` (tax_number)

**Example 87** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Claire Wienhues, Hörweix 62, 3140 Pottenbrunn, Österreich, vertreten durch TPA Steuerberatung GmbH, Wiedner Gürtel 13 Tür  Turm 24, 1100 Wien, wegen behaupteter Verletzung der Entscheidungspflicht durch das  Finanzamt VG betreffend Körperschaftsteuer 2010 Steuernummer 61-469/1778  zu Recht  erkannt:   I. Der Säumnisbeschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Claire Wienhues` | `Claire Wienhues` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helmut Mittermayr` (person)
- `Hörweix 62, 3140 Pottenbrunn, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamt` (organisation)
- `61-469/1778` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jeanne Stockhorst, Fridrichallee 42, 4084 Scheiblberg, Österreich  über die Beschwerde vom 5. Dezember 2006  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten vom 17. November 2006 betreffend  Einkommensteuer 2000, Steuernummer 22-242/2984, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Jeanne Stockhorst` | `Jeanne Stockhorst` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Fridrichallee 42, 4084 Scheiblberg, Österreich` (address)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `22-242/2984` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_VALIDATE/136985.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136985.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Tanja Fützenreiter, Dr.-Adolf-Schärf-Gasse 23, 3123 Mittermerking, Österreich, über die Beschwerde der Beschwerdeführerin  (Bf.) vom 29. März 2021 gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) für  2019 des Finanzamtes Österreich vom 17. März 2021 zur Steuernummer 90-161/7779  zu  Recht erkannt:   Gemäß § 279 BAO wird der Beschwerde teilweise stattgegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Tanja Fützenreiter` | `Tanja Fützenreiter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Christian Seywald` (person)
- `Dr.-Adolf-Schärf-Gasse 23, 3123 Mittermerking, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `90-161/7779` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

**False Positives:**

- `Saligergasse` — partial — pred is substring of gold: `Saligergasse 1, 3300 Haag Dorf, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Hedwig Bavenek-Weber`(person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Eugen Volchert Hochraingasse` — partial — gold is substring of pred: `Eugen Volchert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Lieselotte Akdas`(person)
- `Eugen Volchert`(person)
- `Hochraingasse 28, 4076 Valtau, Österreich`(address)
- `FA Baden Mödling`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

**False Positives:**

- `Kelderber Beratung Technologien` — type mismatch — same span as gold: `Kelderber Beratung Technologien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Silvia Gebhart`(person)
- `Kelderber Beratung Technologien`(organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich`(address)
- `Dr Vana Dr Kolbitsch Mag Breitenecker`(person)
- `Mag Tatjana Kovacic`(person)
- `Dr  Heinrich Vana,`(person)
- `Finanzamtes Wien 8/16/17`(organisation)
- `7867 150654`(social_security_number)
- `Europäischen Parlaments`(organisation)
- `Gerichtshof der Europäischen Union`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129956.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129956.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Theodora Urbanova, Bakk. iur., St. Johann 20, 4982 Kirchdorf am Inn, Österreich, über die Beschwerde vom 12. April 2018 gegen  den Bescheid des Finanzamtes Baden Mödling vom 21. März 2018 betreffend  Einkommensteuer 2016, Steuernummer 54-205/5010, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Theodora Urbanova` — partial — pred is substring of gold: `Theodora Urbanova, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Theodora Urbanova, Bakk. iur.`(person)
- `St. Johann 20, 4982 Kirchdorf am Inn, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)
- `54-205/5010`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Tamara Steinmüller  in der Beschwerdesache der  Gueldner Garten, Wöberstraße 8, 4873 Arbing, Österreich, über die Beschwerde vom 15. Juli 2019 gegen den Bescheid des  FA Deutschlandsberg Leibnitz Voitsberg  vom 12. Juli 2019 betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Gueldner Garten` — type mismatch — same span as gold: `Gueldner Garten`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Tamara Steinmüller`(person)
- `Gueldner Garten`(organisation)
- `Wöberstraße 8, 4873 Arbing, Österreich`(address)
- `FA Deutschlandsberg Leibnitz Voitsberg`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Raimund Diedering` — partial — pred is substring of gold: `Raimund Diedering, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Bianca Gerasimczuk`(person)
- `Raimund Diedering, Bakk. iur.`(person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich`(address)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132439.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132439.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Josepha Peifers Jägerberg 5, 9062 Bärndorf, Österreich  über die Beschwerde vom 17. August 2020 gegen den Bescheid  des Finanzamtes Kitzbühel Lienz vom 27. Juli 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Josepha Peifers Jägerberg` — partial — gold is substring of pred: `Josepha Peifers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Josepha Peifers`(person)
- `Jägerberg 5, 9062 Bärndorf, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Oberweissburg 52, 4081 Hartkirchen, Österreich, vertreten durch Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, über die Beschwerde vom 27. Oktober 2014  gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 30. September 2014 betreffend  Einkommensteuer 2009 und 2010 sowie Anspruchszinsen (§ 205 BAO) 2009 und 2010,  Steuernummer 73-948/8864, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Oberweissburg 52, 4081 Hartkirchen, Österreich`(address)
- `Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH`(organisation)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `73-948/8864`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Vorsitzende R1 und die weiteren Senatsmitglieder R2,  LB1 und LB2 in der Beschwerdesache Inn Trikraftglanz, Torricelligasse 3, 9335 Lölling Sonnseite, Österreich, vertreten durch Audit  Partner Austria Wirtschafts- prüfer GmbH, Wagramer Straße 19/8.

**False Positives:**

- `Inn Trikraftglanz` — type mismatch — same span as gold: `Inn Trikraftglanz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Inn Trikraftglanz`(organisation)
- `Torricelligasse 3, 9335 Lölling Sonnseite, Österreich`(address)
- `Audit  Partner Austria Wirtschafts- prüfer GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Stephan in der Beschwerdesache  Valentin Joebges, LLM, Bärngarten 17, 9713 Hochegg, Österreich, über die Beschwerde vom 23.08.2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Braunau Ried Schärding) vom 11. August 2020  betreffend Abweisung der Wiederaufnahmeanträge betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016, 2017 und 2018 Steuernummer 84-167/9727  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Valentin Joebges` — partial — pred is substring of gold: `Valentin Joebges, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Stephan`(person)
- `Valentin Joebges, LLM`(person)
- `Bärngarten 17, 9713 Hochegg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Braunau Ried Schärding`(organisation)
- `84-167/9727`(tax_number)

</details>

---

## `OStR_Title` 🏆

**F1:** 0.012 | **Precision:** 0.917 | **Recall:** 0.006  

**Format:** `regex`  
**Rule ID:** `73b9f694`  
**Description:**
Captures names with the title 'OStR' (Obersteueranwalt) followed by a name.

**Content:**
```
\bOStR\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.917 | 0.006 | 0.012 | 12 | 11 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 1 | 1840 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OStR Cassandra Schmedtje,  Lettenmayrhof 1, 9556 Karlsberg, Österreich, vertreten durch Helga Kraus, Johann Vollnhofer-Straße 1/Stg.

| Predicted | Gold |
|---|---|
| `OStR Cassandra Schmedtje` | `OStR Cassandra Schmedtje` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lettenmayrhof 1, 9556 Karlsberg, Österreich` (address)
- `Helga Kraus` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Mit Bescheid vom 04.06.2019 wurde die nunmehrige Beschwerdeführerin als  Haftungspflichtige gemäß § 9 iVm §§ 80 ff BAO für aushaftende Abgabenschuldigkeiten der  OStR Serena Hammoudi  im Ausmaß von EUR 43.032,85 in Anspruch genommen.

| Predicted | Gold |
|---|---|
| `OStR Serena Hammoudi` | `OStR Serena Hammoudi` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_11`)


Die Beschwerdeführerin war seit 01.07.2009 bis zur Löschung im Firmenbuch am tt.07.2019  eingetragene handelsrechtliche Geschäftsführerin der OStR Serena Hammoudi  (Primärschuldnerin).

| Predicted | Gold |
|---|---|
| `OStR Serena Hammoudi` | `OStR Serena Hammoudi` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_14`)


Die  Beschwerdeführerin war im Zeitraum vom 01.07.2009 bis tt.07.2019 zur Geschäftsführerin und  damit zur Vertreterin der abgabenschuldnerischen Firma OStR Serena Hammoudi  bestellt und daher gemäß § 18 GmbHG zur Vertretung der Gesellschaft berufen.

| Predicted | Gold |
|---|---|
| `OStR Serena Hammoudi` | `OStR Serena Hammoudi` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_15`)


Mit Beschluss des Handelsgerichtes Wien vom 01.08.2013 AZ 6 S 129/13g wurde über das  Vermögen der OStR Serena Hammoudi  das Sanierungsverfahren eröffnet.

| Predicted | Gold |
|---|---|
| `OStR Serena Hammoudi` | `OStR Serena Hammoudi` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_20`)


Demnach waren 70 % der Abgabenforderungen, die im Sanierungsverfahren zu den  Konkursforderungen einzuordnen waren, bei der Firma OStR Serena Hammoudi  nicht  mehr einbringlich.

| Predicted | Gold |
|---|---|
| `OStR Serena Hammoudi` | `OStR Serena Hammoudi` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_29`)


Aus dem Firmenbuchauszug der OStR Serena Hammoudi  geht hervor, dass die  Beschwerdeführerin vom 01.07.2009 bis tt.07.2019 Geschäftsführer der  OStR Serena Hammoudi  war und diese am tt.07.2019 gemäß § 40 FBG infolge von  Vermögenslosigkeit im Firmenbuch gelöscht wurde.

| Predicted | Gold |
|---|---|
| `OStR Serena Hammoudi` | `OStR Serena Hammoudi` |
| `OStR Serena Hammoudi` | `OStR Serena Hammoudi` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_36`)


Im gegenständlichen Fall steht die Uneinbringlichkeit der haftungsgegenständlichen Abgaben  (Lohnsteuer 2008 bis 2018 laut Aufstellung) bei der Primärschuldnerin unbestritten fest, da die  OStR Serena Hammoudi  am tt.07.2019 wegen Vermögenslosigkeit im Firmenbuch  gemäß § 40 FBG amtswegig gelöscht wurde.

| Predicted | Gold |
|---|---|
| `OStR Serena Hammoudi` | `OStR Serena Hammoudi` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_39`)


Die Beschwerdeführerin fungierte vom  01.07.2009 bis tt.07.2019 als handelsrechtliche Geschäftsführerin der  OStR Serena Hammoudi.

| Predicted | Gold |
|---|---|
| `OStR Serena Hammoudi` | `OStR Serena Hammoudi` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/148790.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148790.1_46`)


Der Beschwerdeführerin oblag daher als vertretungsberechtigtes Organ der  OStR Serena Hammoudi  die Erfüllung der abgabenrechtlichen Pflichten der  Gesellschaft.

| Predicted | Gold |
|---|---|
| `OStR Serena Hammoudi` | `OStR Serena Hammoudi` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/145832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache StR OSR OStR Torsten Schlichtenmeier, Untere Waldalpe 2, 5204 Voglhub, Österreich, (Beschwerdeführerin, abgekürzt: Bf.), über  deren Beschwerde vom 25. Jänner 2024 gegen den Einkommensteuerbescheid 2022 des  Finanzamtes Österreich vom 11. Jänner 2024 zu Steuernummer 20-897/4296  zu Recht  erkannt:  Der Beschwerde wird teilweise stattgegeben und der angefochtene Bescheid gemäß § 279  Abs. 1 BAO abgeändert.

**False Positives:**

- `OStR Torsten Schlichtenmeier` — partial — pred is substring of gold: `StR OSR OStR Torsten Schlichtenmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Seywald`(person)
- `StR OSR OStR Torsten Schlichtenmeier`(person)
- `Untere Waldalpe 2, 5204 Voglhub, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `20-897/4296`(tax_number)

</details>

---

## `Priv_Dozi_Title` 🏆

**F1:** 0.033 | **Precision:** 0.838 | **Recall:** 0.017  

**Format:** `regex`  
**Rule ID:** `e70b3f73`  
**Description:**
Captures 'Priv.-Doz.' or 'Priv.-Doz.in' followed by full names, ensuring full name capture.

**Content:**
```
\bPriv\.-Doz\.(?:in)?\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+LL\.M\.|\s+LLM|\s+MA|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.838 | 0.017 | 0.033 | 37 | 31 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 31 | 6 | 1820 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129143.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Helge Göppele  in der Beschwerdesache der  GDJJ Versand, Keplergasse 1, 4312 Oberzirking, Österreich, betreffend die Beschwerde vom 13. Mai 2020 gegen die Bescheide  des Finanzamtes Graz-Umgebung vom 24. April 2020 betreffend Abweisung von Anträgen auf  Aufhebung der Einkommensteuerbescheide 2015 bis 2018 beschlossen:  Die angefochtenen Abweisungsbescheide (und die entsprechenden  Beschwerdevorentscheidungen) werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der  Sache an die Abgabenbehörde aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Helge Göppele` | `Priv.-Doz. Helge Göppele` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `GDJJ Versand` (organisation)
- `Keplergasse 1, 4312 Oberzirking, Österreich` (address)
- `Finanzamtes Graz` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129435.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129435.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Jodgalweit  in der Beschwerdesache des  Florentin Pawils, Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich, betreffend den Antrag vom 9.7.2020 auf Wiedereinsetzung in den  vorigen Stand beschlossen:    Der Antrag auf Wiedereinsetzung in den vorigen Stand wird abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alva Jodgalweit` | `Priv.-Doz.in Alva Jodgalweit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Pawils` (person)
- `Rudolf-Fischer-Stiege 15, 3242 Dachsberg, Österreich` (address)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Rosamunde Galanidis` | `Priv.-Doz.in Rosamunde Galanidis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hermine Ruprich` (person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich` (address)
- `Mag. Wolfgang Moser` (person)
- `Finanzamt Kirchdorf Perg Steyr` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130463.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130463.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Zarin Eckartz  in der Beschwerdesache Volkmar Oortwyn,  Steg 1944 48, 4890 Röth, Österreich, über die Beschwerde vom 19. Februar 2020 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 16. Jänner 2020 betreffend  Gebühren 2020 Steuernummer 72-008/7613  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Zarin Eckartz` | `Priv.-Doz.in Zarin Eckartz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Volkmar Oortwyn` (person)
- `Steg 1944 48, 4890 Röth, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `72-008/7613` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130651.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130651.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Melina Bankratz  in der Beschwerdesache Lars Huesgen,  Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich, vertreten durch RA, gegen die Bescheide des Finanzamtes Salzburg-Land vom  16. Mai 2019, betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2013  und Einkommensteuer 2013, die Bescheide des Finanzamtes Salzburg-Land vom 17. Mai 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2014, 2015 und  Einkommensteuer 2014, 2015, und die vermeintlichen Bescheide des Finanzamtes Salzburg- Land, betreffend Festsetzung von Anspruchszinsen 2013, 2014, 2015, beschlossen:  1.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Melina Bankratz` | `Priv.-Doz.in Melina Bankratz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lars Huesgen` (person)
- `Hinterbach 3, 8643 Allerheiligen im Mürztal, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/133128.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133128.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Dragan Carstens  in der Beschwerdesache StR Milena Neidig,  Dimbachreith 11, 3233 Niederhofen, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 20. November 2019  betreffend Einkommensteuer 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dragan Carstens` | `Priv.-Doz. Dragan Carstens` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Milena Neidig` (person)
- `Dimbachreith 11, 3233 Niederhofen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Zoltan Dabrowski  in der Beschwerdesache der Frau  OMedR Prof. Hartmut Szardemings, Reuttener Straße 33u, 5090 Faistau, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  15. März 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom 22. Jänner 2019  betreffend Einkommensteuer 2017 zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Zoltan Dabrowski` | `Priv.-Doz. Zoltan Dabrowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Prof. Hartmut Szardemings` (person)
- `Reuttener Straße 33u, 5090 Faistau, Österreich` (address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/134486.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134486.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Petra Schippan  in der Beschwerdesache Judith Kapelle,  Saßbergweg 17, 4860 Haid, Österreich, betreffend Beschwerde vom 2. September 2012 gegen den Bescheid des FA  Waldviertel vom 3. August 2012 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2011 Steuernummer 31-042/8347  beschlossen:     Der Vorlageantrag vom 30.11.2012 wird gemäß § 256 Abs. 3 BAO in Verbindung mit § 264  Abs. 4 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Petra Schippan` | `Priv.-Doz.in Petra Schippan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Judith Kapelle` (person)
- `Saßbergweg 17, 4860 Haid, Österreich` (address)
- `FA  Waldviertel` (organisation)
- `31-042/8347` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/134982.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134982.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Nancy Stuckenschneider  in der Beschwerdesache des  Bruno Karahasan, Ludowikaweg 5, 3602 Bacharnsdorf, Österreich, über die Beschwerde vom 2. Juli 2019 gegen den Bescheid des  FA St. Johann Tamsweg Zell am See  vom 26. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  zur Steuernummer 12-630/0045  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Nancy Stuckenschneider` | `Priv.-Doz.in Nancy Stuckenschneider` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Bruno Karahasan` (person)
- `Ludowikaweg 5, 3602 Bacharnsdorf, Österreich` (address)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `12-630/0045` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/137039.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137039.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Susanne Rohrauer  in der Beschwerdesache der  StadtHandel Planung, Sebastianplatz 18, 3441 Dietersdorf, Österreich  vertreten durch StB, über die Beschwerde vom 7. April 2021 gegen  den Bescheid des FA Salzburg-Stadt  vom 25. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Steuernummer 89-257/7642  zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Susanne Rohrauer` | `Priv.-Doz.in Susanne Rohrauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StadtHandel Planung` (organisation)
- `Sebastianplatz 18, 3441 Dietersdorf, Österreich` (address)
- `FA Salzburg-Stadt` (organisation)
- `89-257/7642` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138131.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Herbert Lindermayer  in der Beschwerdesache Anneliese Dreschmann,  Nußbacher Straße 43, 3650 Kehrbach, Österreich, vertreten durch Schwaiger & Partner Steuerberatung, Anton-Eder-Straße 5,  6020 Innsbruck, über die Beschwerde vom 19. Jänner 2021 gegen den Bescheid des FA Graz-Stadt  vom 13. Jänner 2021 betreffend Energieabgabenvergütung 2015 Steuernummer  60-855/1189  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Herbert Lindermayer` | `Priv.-Doz. Herbert Lindermayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anneliese Dreschmann` (person)
- `Nußbacher Straße 43, 3650 Kehrbach, Österreich` (address)
- `Schwaiger & Partner Steuerberatung` (organisation)
- `FA Graz-Stadt` (organisation)
- `60-855/1189` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138500.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138500.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Priv.-Doz.in Gertrude Kreutl  über die Beschwerden der  Caroline Hesselmann, Mondseeberg 30, 8413 Haslach an der Stiefing, Österreich, vertreten durch die Allgemeine Revisions- und Treuhandgesellschaft  m. b. H. Wirtschaftsprüfungs- und Steuerberatungsgesellschaft in Graz, Brückenkopfgasse 1,  8020 Graz, vom 09.04.2019 gegen die Bescheide des Finanzamtes Graz-Stadt vom 07.03.2019  betreffend Feststellung Gruppenträger 2016 sowie gegen die Bescheide des Finanzamtes Graz- Stadt vom 12.03.2019 betreffend Feststellung Gruppenträger 2014 und 2015 zu Recht erkannt:    Die Beschwerde gegen den Bescheid betreffend Feststellung Gruppenträger 2014 wird als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Gertrude Kreutl` | `Priv.-Doz.in Gertrude Kreutl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Caroline Hesselmann` (person)
- `Mondseeberg 30, 8413 Haslach an der Stiefing, Österreich` (address)
- `Allgemeine Revisions- und Treuhandgesellschaft  m. b. H. Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamtes` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/139596.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Laetitia Weckerlin  in der Beschwerdesache Zdenko Graucop,  Lisztpromenade 31, 9170 Zell-Oberwinkel, Österreich, über die Beschwerde vom 25. Mai 2022 gegen den Bescheid des Finanzamtes  Österreich vom 10. Mai 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020  Steuernummer 11-005/1241  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Laetitia Weckerlin` | `Priv.-Doz.in Laetitia Weckerlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zdenko Graucop` (person)
- `Lisztpromenade 31, 9170 Zell-Oberwinkel, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `11-005/1241` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/139695.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Deborah Stöbesand  in der Beschwerdesache des  Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke, Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich, über die Beschwerde vom 9. Juli 2022 gegen den Bescheid des  FA Waldviertel  vom 7. Juli 2022 betreffend Abweisung eines Antrages auf Wiederaufnahme der  Verfahren hinsichtlich Einkommensteuer für die Jahre 2017 bis 2019 zu Steuernummer  37-369/8758  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Deborah Stöbesand` | `Priv.-Doz.in Deborah Stöbesand` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke` (person)
- `Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich` (address)
- `FA Waldviertel` (organisation)
- `37-369/8758` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/142266.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142266.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Kimberly Willomeit  in der Beschwerdesache des  Christoph Hermsen, Krehmen 64, 4760 Riedlhof, Österreich, über die Beschwerde vom 14. Juli 2022 gegen den Bescheid des  FA Gmunden Vöcklabruck  vom 22. Juni 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021  zu Steuernummer 53-856/2225  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Kimberly Willomeit` | `Priv.-Doz.in Kimberly Willomeit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christoph Hermsen` (person)
- `Krehmen 64, 4760 Riedlhof, Österreich` (address)
- `FA Gmunden Vöcklabruck` (organisation)
- `53-856/2225` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/142398.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142398.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Imre Plönnes  in der Beschwerdesache  Jason Oberbüscher, Joseph-von-Wörndle-Weg 23, 4342 Kolbing, Österreich, über die Beschwerde vom 11. April 2023 gegen den Bescheid des  Finanzamtes Österreich vom 13. März 2023 betreffend Einkommensteuervorauszahlungen  2023 und Folgejahre, Steuernummer 88-942/0644, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Imre Plönnes` | `Priv.-Doz. Imre Plönnes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jason Oberbüscher` (person)
- `Joseph-von-Wörndle-Weg 23, 4342 Kolbing, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `88-942/0644` (tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/142502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Gloria Rejngardt   in der Beschwerdesache des Estelle Klaffer, Moosscheibe 14, 4942 Außerguggenberg, Österreich,   betreffend den Bescheid des Finanzamt Schwechat Gerasdorf  vom 24. März 2020   hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2019, Steuernummer  88-435/1011,   zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Gloria Rejngardt` | `Priv.-Doz.in Gloria Rejngardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Estelle Klaffer` (person)
- `Moosscheibe 14, 4942 Außerguggenberg, Österreich` (address)
- `Finanzamt Schwechat Gerasdorf` (organisation)
- `88-435/1011` (tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/143077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143077.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Alva Hörth  in der Beschwerdesache  Erhard Goebel,  Hauning 24N, 8225 Köppelreith, Österreich  über die Beschwerde vom 6. März 2023 gegen den Bescheid des Finanzamtes  Österreich vom 1. März 2023 betreffend Abweisung eines Zahlungserleichterungsansuchens,  Steuernummer 59-827/7719  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alva Hörth` | `Priv.-Doz.in Alva Hörth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erhard Goebel` (person)
- `Hauning 24N, 8225 Köppelreith, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `59-827/7719` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/144197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Lukas Escherle  in der Verwaltungsstrafsache gegen  Kirsten Schneppensiefen, Poppenreithstraße 26, 7461 Goberling, Österreich, vertreten durch Albert Höferlin  wegen der  Verwaltungsübertretung gemäß § 16 Abs 1 des Gebrauchsabgabegesetz, über die Beschwerde  der Beschuldigten vom 31.7.2023 gegen das Straferkenntnis des Magistrats der Stadt Wien  vom 14.7.2023 zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  Geldstrafe auf je € 20,00 (also EUR 100,00) herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Lukas Escherle` | `Priv.-Doz. Lukas Escherle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kirsten Schneppensiefen` (person)
- `Poppenreithstraße 26, 7461 Goberling, Österreich` (address)
- `Albert Höferlin` (person)
- `Magistrats der Stadt Wien` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/144516.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144516.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Calvin Liechtenstein  in der Beschwerdesache KommR Thorsten Voelkerling,  Kirchenbühl 12, 4463 Brunnbach, Österreich, vertreten durch Rechtsanwalt Dr. Gahleithner & Partner OG, Schottengasse 7  Tür 6, 1010 Wien, über die Beschwerde vom 25. September 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 11. September 2019 betreffend den Ablauf der Aussetzung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Calvin Liechtenstein` | `Priv.-Doz. Calvin Liechtenstein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Thorsten Voelkerling` (person)
- `Kirchenbühl 12, 4463 Brunnbach, Österreich` (address)
- `Dr. Gahleithner & Partner OG` (organisation)
- `Finanzamtes Wien 4/5/10` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/145639.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145639.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Engelbert Jakubec  in der Säumnisbeschwerdesache  Finn Lautel, Spiegelweg 1, 4451 Saaß, Österreich, über die Beschwerde vom 26.8.2024, beim Bundesfinanzgericht  am 29.8.2024 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht durch das  Finanzamt Österreich betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023  beschlossen:  I. Das Säumnisbeschwerdeverfahren wird eingestellt.  II. Eine Revision an den Verwaltungsgerichtshof ist nach Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Engelbert Jakubec` | `Priv.-Doz. Engelbert Jakubec` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finn Lautel` (person)
- `Spiegelweg 1, 4451 Saaß, Österreich` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt Österreich` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/145821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145821.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Miroslav Sandfuchs  in der Beschwerdesache Jörg Dargusch,  Bärlauchweg 26, 4291 Elz, Österreich, über die Beschwerde vom 22. April 2024 gegen den Bescheid des FA Amstetten Melk Scheibbs  vom 13. März 2024 über die Abweisung eines Zahlungserleichterungsansuchens,  Steuernummer 82-228/8876, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Miroslav Sandfuchs` | `Priv.-Doz. Miroslav Sandfuchs` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jörg Dargusch` (person)
- `Bärlauchweg 26, 4291 Elz, Österreich` (address)
- `FA Amstetten Melk Scheibbs` (organisation)
- `82-228/8876` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/146104.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146104.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Georg Kunstmann  in der Beschwerdesache Gerhard Weinbergs,  Löwengrub 29, 8680 Hönigsberg, Österreich, vertreten durch Damian Eccardt, Unterort 18, 4673 Bernhartsdorf, Österreich, über die Beschwerde vom 8.  Mai 2023 gegen den Bescheid des Finanzamtes Österreich vom 4. April 2023 betreffend  Umsatzsteuer 2013 sowie über die Beschwerden vom 23. August 2023 gegen die Bescheide  des Finanzamtes Österreich vom 4. August 2023 betreffend Umsatzsteuer 2014, 2015, 2016  und 2017 zu Steuernummer 50-546/1107  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Georg Kunstmann` | `Priv.-Doz. Georg Kunstmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gerhard Weinbergs` (person)
- `Löwengrub 29, 8680 Hönigsberg, Österreich` (address)
- `Damian Eccardt` (person)
- `Unterort 18, 4673 Bernhartsdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)
- `50-546/1107` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/146179.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146179.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Aurelia Frässdorf  in der Beschwerdesache Janet Giesendorf,  Am Teich 47z, 7322 Lackenbach, Österreich, über die Beschwerde vom 21. Oktober 2023 gegen den Bescheid des  Finanzamtes Österreich vom 26. September 2023, Ordnungsbegriff Nr1, betreffend Abweisung  des Antrages auf den Erhöhungsbetrag zur Familienbeihilfe für den Zeitraum April 2019 –  September 2022   zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Aurelia Frässdorf` | `Priv.-Doz.in Aurelia Frässdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janet Giesendorf` (person)
- `Am Teich 47z, 7322 Lackenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/146483.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146483.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Daphne Cofalla  in der Beschwerdesache Xenia Rieffers, Bakk. techn.,  Almersberg 23, 5440 Voregg, Österreich, betreffend Beschwerde vom 16. Oktober 2023 gegen den Bescheid des  Finanzamtes Österreich vom 6. September 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022   Steuernummer  *** beschlossen:     Die Parteien werden gemäß § 281a BAO formlos in Kenntnis gesetzt, dass nach Auffassung des  Bundesfinanzgerichts in Bezug auf die gegenständliche Beschwerde vom 16. Oktober 2023  gegen den Bescheid vom 6. September 2023 ein Vorlageantrag nicht eingebracht wurde.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Daphne Cofalla` | `Priv.-Doz.in Daphne Cofalla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Xenia Rieffers, Bakk. techn.` (person)
- `Almersberg 23, 5440 Voregg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Bundesfinanzgerichts` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/146667.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146667.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Istvan  Kempfer  in der Beschwerdesache Anselm Arnhölter,  Neufahrner Straße 6, 3744 Mold, Österreich, vertreten durch TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH &  Co KG, Muthgasse 109, 1190 Wien, über die Beschwerde vom 6. Juni 2024 gegen den Bescheid  des Finanzamtes Österreich vom 26. Mai 2023 betreffend Einkommensteuer 2022 zu  Steuernummer 17-947/8635  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Istvan  Kempfer` | `Priv.-Doz. Istvan  Kempfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anselm Arnhölter` (person)
- `Neufahrner Straße 6, 3744 Mold, Österreich` (address)
- `TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH &  Co KG` (organisation)
- `Finanzamtes Österreich` (organisation)
- `17-947/8635` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/147002.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Franz Quapp  in der Beschwerdesache  Elvira Mathis, Claudiastraße 7, 2061 Hadres, Österreich, vertreten durch Wladimir Kreissl, Seibersdorf 3, 8141 Bierbaum, Österreich,  über die Beschwerde vom 13. Mai 2015 gegen den Bescheid des (damaligen) Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf, nunmehr Finanzamt Österreich, vom 9. April 2015  betreffend Säumniszuschlag 2015 Steuernummer 98-983/4004  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Franz Quapp` | `Priv.-Doz. Franz Quapp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elvira Mathis` (person)
- `Claudiastraße 7, 2061 Hadres, Österreich` (address)
- `Wladimir Kreissl` (person)
- `Seibersdorf 3, 8141 Bierbaum, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `98-983/4004` (tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/147165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147165.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Priv.-Doz.in Antonia Ramdani  in der Beschwerdesache Hedwig Schadek,  Adelsdorf 68, 8755 Feistritzgraben, Österreich, vertreten durch RPW Tulln Steuerberatung GmbH, Franz-Schubert-Straße 8,  3430 Tulln/Donau, betreffend Beschwerde vom 3. Juli 2024 gegen den Bescheid des  Finanzamtes Österreich vom 10. Mai 2024 betreffend Säumniszuschlag 2024, Steuernummer  95-051/7682, den Beschluss:  I. Der Vorlageantrag wird gemäß § 260 Abs. 1 lit. b BAO iVm § 264 Abs. 4 lit. e BAO als  nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Antonia Ramdani` | `Priv.-Doz.in Antonia Ramdani` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hedwig Schadek` (person)
- `Adelsdorf 68, 8755 Feistritzgraben, Österreich` (address)
- `RPW Tulln Steuerberatung GmbH,` (organisation)
- `Finanzamtes Österreich` (organisation)
- `95-051/7682` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/147744.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147744.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Martha Swiatek  in der Beschwerdesache Roland Gelfuß,  Geyreggerweg 19, 9851 Lurnbichl, Österreich, über die Beschwerde vom 18. März 2021 gegen den Bescheid des Finanzamtes  Österreich vom 23. Februar 2021 über die Abweisung einer Nachsicht von  Abgabenschuldigkeiten gemäß § 236 BAO betreffend Steuernummer 06-247/1161  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Martha Swiatek` | `Priv.-Doz.in Martha Swiatek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Roland Gelfuß` (person)
- `Geyreggerweg 19, 9851 Lurnbichl, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `06-247/1161` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/148639.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148639.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Enrico Kroneberg  in der Beschwerdesache Viola Teise,  Am Fünfkirchenweg 39, 6691 Jungholz, Österreich, über die Beschwerde vom 25. Juli 2023, eingelangt am 28. Juli 2023, gegen den  Bescheid des FA Landeck Reutte  vom 5. Juli 2023 zu Steuernummer 40-770/7977  betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2021 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Enrico Kroneberg` | `Priv.-Doz. Enrico Kroneberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Viola Teise` (person)
- `Am Fünfkirchenweg 39, 6691 Jungholz, Österreich` (address)
- `FA Landeck Reutte` (organisation)
- `40-770/7977` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/149372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Frederik Grossmayer  über die Beschwerde des Jonathan Gagarin,  Paul Has-Gasse 2, 5251 Aigertsham, Österreich, vom 4. Juli 2025, gegen die zwei Zurückweisungsbescheide des Magistrates der  Stadt Wien, Magistratsabteilung 67, beide vom 3. Juli 2025, GZen 1) MA67/GZ1/2025 und 2)  MA67/GZ2/2025, zu Recht erkannt:  Gem. § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und werden die zwei  angefochtenen Zurückweisungsbescheide bestätigt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Frederik Grossmayer` | `Priv.-Doz. Frederik Grossmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jonathan Gagarin` (person)
- `Paul Has-Gasse 2, 5251 Aigertsham, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Mag. Yorick Schlenbäcker  in der Beschwerdesache Kordula Arlov,  Stranitzkygasse 33, 8251 Karnerviertel, Österreich, über die Beschwerde vom 19.6.2018 gegen den Bescheid des Finanzamtes  Oststeiermark vom 8.6.2018 betreffend Einkommensteuer 2014 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO entsprechend der  Beschwerdevorentscheidung vom 10.9.2018 abgeändert.

**False Positives:**

- `Priv.-Doz. Mag` — partial — pred is substring of gold: `Priv.-Doz. Mag. Yorick Schlenbäcker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Mag. Yorick Schlenbäcker`(person)
- `Kordula Arlov`(person)
- `Stranitzkygasse 33, 8251 Karnerviertel, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/140806.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140806.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Moritz Bonnert  in der Beschwerdesache PhD MedR Romana Hupp,  Süßenberger Straße 7, 5270 Vorbuch, Österreich, vertreten durch Marsoner + Partner GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020 Innsbruck, über die Beschwerde  vom 26. Juli 2013 gegen den Bescheid des FA Salzburg-Land  vom 25. Juni 2013 betreffend  Umsatzsteuer 2011, Steuernummer 16-160/7509, zu Recht erkannt:     I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Priv.-Doz. Moritz Bonnert` — partial — pred is substring of gold: `Dr. Priv.-Doz. Moritz Bonnert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Moritz Bonnert`(person)
- `PhD MedR Romana Hupp`(person)
- `Süßenberger Straße 7, 5270 Vorbuch, Österreich`(address)
- `Marsoner + Partner GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `FA Salzburg-Land`(organisation)
- `16-160/7509`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/143138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143138.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Priv.-Doz.in Li van Clev, Rabenfurter Straße 9, 4770 Schärdingerau, Österreich, über die Beschwerde vom 22. Jänner 2023  gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2023 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2021 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Priv.-Doz.in Li` — partial — pred is substring of gold: `Priv.-Doz.in Li van Clev`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Priv.-Doz.in Li van Clev`(person)
- `Rabenfurter Straße 9, 4770 Schärdingerau, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/144450.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144450.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Mag. Priv.-Doz. Karl Schultenjohann  über die Beschwerde der MittelPflege Entwicklung GmbH, Lirkgasse 23, 8412 Sukdull, Österreich, vertreten durch die SBF Steuerberatung OG, Wielandgasse 35, 8010  Graz, vom 12.03.2024 gegen den Bescheid des Finanzamtes Österreich vom 09.02.2024  betreffend Festsetzung eines ersten Säumniszuschlages zu Recht erkannt:  Die Bescheidbeschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz. Karl Schultenjohann` — partial — pred is substring of gold: `Mag. Priv.-Doz. Karl Schultenjohann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Priv.-Doz. Karl Schultenjohann`(person)
- `MittelPflege Entwicklung GmbH`(organisation)
- `Lirkgasse 23, 8412 Sukdull, Österreich`(address)
- `SBF Steuerberatung OG`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/145816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Priv.-Doz. Lars Tezlow  in der Beschwerdesache Ilona Sadowske,  Laaer-Wald-Straße 254, 4040 Asberg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater KG -  Steuerbüro Specht, Kirchweg 11, 6600 Reutte, gegen den von der belangten Behörde  Finanzamt Österreich am 24. April 2023 zu Steuernummer 48-791/6345  ausgefertigten  Bescheid betreffend Einkommensteuer 2021 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 Abs. 1 BAO abgeändert.

**False Positives:**

- `Priv.-Doz. Lars Tezlow` — partial — pred is substring of gold: `Univ.-Prof. Priv.-Doz. Lars Tezlow`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Priv.-Doz. Lars Tezlow`(person)
- `Ilona Sadowske`(person)
- `Laaer-Wald-Straße 254, 4040 Asberg, Österreich`(address)
- `Hofmann - Wirtschaftstreuhand - Steuerberater KG -  Steuerbüro Specht`(organisation)
- `Finanzamt Österreich`(organisation)
- `48-791/6345`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/147361.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147361.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Emmerich Malert  betreffend den Vorlageantrag der  Florens Schitterle, Heidebahn 164, 2443 Deutsch-Brodersdorf, Österreich, vom 31. Dezember 2020 in einer Familienbeihilfenangelegenheit  (Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Mai 2013 bis  Dezember 2014, Bescheid des Finanzamtes Österreich vom 24. März 2020)  beschlossen:  I.  Der Vorlageantrag wird gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit a BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `Priv.-Doz. Priv` — partial — pred is substring of gold: `Priv.-Doz. Priv.-Doz. Emmerich Malert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Priv.-Doz. Emmerich Malert`(person)
- `Florens Schitterle`(person)
- `Heidebahn 164, 2443 Deutsch-Brodersdorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `Mag_Title` 🏆

**F1:** 0.011 | **Precision:** 0.833 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `4b62eaa1`  
**Description:**
Captures 'Mag.' followed by full names, ensuring the match does not include company suffixes like 'GmbH' or 'Steuerberatung'.

**Content:**
```
\bMag\.(?:\s+Dr\.)?\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+LL\.M\.|\s+LLM|\s+MA|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?(?=,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.833 | 0.005 | 0.011 | 12 | 10 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 10 | 2 | 1841 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch durch den Senatsvorsitzenden Dr. Michael Rauscher und  die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Claudia Schmölzer über die Beschwerden der Heike Dorrenbach,  Schröttenhofweg 38, 4624 Hölking, Österreich  vertreten durch die LBG Steiermark Steuerberatung GmbH, Rathausplatz 3, 8940  Liezen vom 16.08.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom  02.08.2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und  Körperschaftsteuer 2014 bis 2016 zu Recht erkannt:   Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Franz Glashüttner` | `Mag. Franz Glashüttner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Michael Rauscher` (person)
- `Dr. Christian Haid` (person)
- `Mag. Bruno  Sundl` (person)
- `Heike Dorrenbach` (person)
- `Schröttenhofweg 38, 4624 Hölking, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Peter Steurer, die Richterin  Mag. Natascha Gassner, die fachkundige Laienrichterin Mag. Renate Burtscher und den  fachkundigen Laienrichter Bernd Feldkircher in der Beschwerdesache Vincent Kohlstruk, Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich,  vertreten durch die Bischof-Fuchs Steuerberatungs GmbH, Dorf Rieden 12, 6900 Bregenz,  gegen den Bescheid des Finanzamtes Bregenz vom 6. Juni 2018 betreffend Einkommensteuer  2017 nach Durchführung einer mündlichen Verhandlung am 21. April 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen;

| Predicted | Gold |
|---|---|
| `Mag. Natascha Gassner` | `Mag. Natascha Gassner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Mag. Renate Burtscher` (person)
- `Bernd Feldkircher` (person)
- `Vincent Kohlstruk` (person)
- `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich` (address)
- `Bischof-Fuchs Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Günter Jedamczik  in der Beschwerdesache ÖkR Tobias Schönyan,  Kreuzerleitenweg 34, 5273 Hofing, Österreich, vertreten durch Herrn Mag. Gernot Thonhauser, Steuerberater,  Wernersdorf 111, 8551 Wies, über die Beschwerde vom 15.3.2022 gegen den Bescheid des  Finanzamtes Österreich vom 22.2.2022 betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Gernot Thonhauser` | `Mag. Gernot Thonhauser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Günter Jedamczik` (person)
- `ÖkR Tobias Schönyan` (person)
- `Kreuzerleitenweg 34, 5273 Hofing, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/142867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142867.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden MMag. Gerald Erwin Ehgartner und die  weiteren Senatsmitglieder Mag. Elisabeth Traxler, Mag. Harald Zeller und Christian Ringseis in  der Beschwerdesache Muran Iossifidis, Birken-Siedlung 22, 4715 Unterstetten, Österreich, vertreten durch KPMG Alpen-Treuhand  GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien,  über die Beschwerde vom 30. August 2023 gegen den Bescheid des Finanzamtes für  Großbetriebe vom 11. Juli 2023 betreffend Beschwerdezinsen (§ 205a BAO) nach  Durchführung einer mündlichen Verhandlung am 29. November 2023 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Elisabeth Traxler` | `Mag. Elisabeth Traxler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Gerald Erwin Ehgartner` (person)
- `Mag. Harald Zeller` (person)
- `Christian Ringseis` (person)
- `Muran Iossifidis` (person)
- `Birken-Siedlung 22, 4715 Unterstetten, Österreich` (address)
- `KPMG Alpen-Treuhand  GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/143822.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143822.1_2`)


Das Bundesfinanzgericht hat durch den Senat 6008-1 besetzt mit dem Senatsvorsitzenden  Mag. Johann Fischerlehner, der beisitzenden Richterin Maga. Ulrike Stephan, sowie den  fachkundigen Laienrichtern Michael Hinterreiter, LL.B. und Leopold Pichlbauer in der  Beschwerdesache Philippa Aufheimer, Teichschloßweg 11, 8162 Haufenreith, Österreich, vertreten durch Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH, Bahnhofstraße 13, 4400 Steyr, über die Beschwerde vom 9. März  2023 gegen den Bescheid des Finanzamtes Österreich vom 22. Februar 2023 mit dem der  Antrag gemäß § 299 Abs. 1 Bundesabgabenordnung vom 29.07.2022, eingebracht am  29.07.2022, betreffend den Bescheid über die Wiederaufnahme des Verfahrens gemäß  § 303  Abs. 1 BAO vom 21.12.2021 abgewiesen wurde, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben und der angefochtene  Bescheid dahingehend abgeändert, dass der Bescheid vom 21. Dezember 2021, mit  dem die belangte Behörde zu Einheitswertaktenzeichen EW-AZ die  Wiederaufnahme des Verfahrens gemäß § 303 Abs. 1 BAO des mit Bescheid vom  13.12.2016 abgeschlossenen Verfahrens betreffend die Zurechnungsfortschreibung  gemäß § 21 Abs. 4 BeWG zum 01.01.2015 verfügt hat, aufgehoben wird.

| Predicted | Gold |
|---|---|
| `Mag. Johann Fischerlehner` | `Mag. Johann Fischerlehner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Michael Hinterreiter, LL.B.` (person)
- `Leopold Pichlbauer` (person)
- `Philippa Aufheimer` (person)
- `Teichschloßweg 11, 8162 Haufenreith, Österreich` (address)
- `Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/144427.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144427.1_51`)


Die Feststellungen zur Erkrankung, zum Krankheitsverlauf und zu den  diesbezüglichen Folgen auf die Berufsausbildung stützen sich insbesondere auf das  psychiatrische Gutachten von Mag. Name, Psychologin und Psychotherapeutin.

| Predicted | Gold |
|---|---|
| `Mag. Name` | `Mag. Name` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Armin Treichl, den Richter Dr.  Roman Galehr sowie die fachkundigen Laienrichter Mag. Eva-Maria Düringer und Mag. Tino  Ricker in der Beschwerdesache Dirk Hironymus, Am See IV 25, 3071 Hinterholz, Österreich (vormals: RHO Pharma), vertreten  durch Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG, Alpstraße  23, 6890 Lustenau über die Beschwerde vom 05. Oktober 2016 gegen die Bescheide des  Finanzamtes Feldkirch (nunmehr Finanzamt Österreich, Postfach 260, 1000 Wien) vom 12.  September 2016 betreffend Umsatzsteuer 2012, Bescheid über die Wiederaufnahme des  Verfahrens 2012 und vom 09. September 2016 betreffend Umsatzsteuer 2015 Steuernummer  63-114/3997  in Anwesenheit der Schriftführerin Isabella Längle zu Recht erkannt:     I. Die Beschwerde gegen die Wiederaufnahme des Verfahrens Umsatzsteuer 2012  wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.  Roman Galehr` (person)
- `Mag. Eva-Maria Düringer` (person)
- `Mag. Tino  Ricker` (person)
- `Dirk Hironymus` (person)
- `Am See IV 25, 3071 Hinterholz, Österreich` (address)
- `RHO Pharma` (organisation)
- `Winkler & Partner Wirtschaftstreuhand und Steuerberatungs GmbH & Co KG` (organisation)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt Österreich` (organisation)
- `63-114/3997` (tax_number)
- `Isabella Längle` (person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_306`)


„Guten Tag Mag. Ungericht,  betreffend der RHO Pharma, Steuernummer 63-114/3997, wollte ich kurz mitteilen, dass von  den beantragten Einfuhrumsatzsteuerbeträgen iHv 89.252,70 € (2012) und 106.576,01 € (2015)  an die einzelnen ausländischen Gesellschaften im Jahr 2012 in Summe Einfuhrumsatzsteuern  von 79.380,00 € und im Jahr 2015 von 82.824,00 € erstattet wurden.

| Predicted | Gold |
|---|---|
| `Mag. Ungericht` | `Mag. Ungericht` |

**Missed by this rule (FN):**

- `RHO Pharma` (organisation)
- `63-114/3997` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_25`)


Seit 2023 wurde die Kanzlei von Mag. Roland Schmidt, Kerstin Graf MSc (WU)  und Isabella Hauer MA gemeinsam als Partner fortgeführt.

| Predicted | Gold |
|---|---|
| `Mag. Roland Schmidt` | `Mag. Roland Schmidt` |

**Missed by this rule (FN):**

- `Kerstin Graf MSc (WU)` (person)
- `Isabella Hauer MA` (person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/147955.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147955.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christian Soltendieck  in der Beschwerdesache des Dr. MV  als Masseverwalter (MV) im Insolvenzverfahren der Berthold Grosshans, Gruisla 3Q, 3231 Linsberg, Österreich  vertreten durch  die Berthold Grosshans, Seetal 31, 4661 Altmanning, Österreich  nunmehr vertreten durch Rechtsanwalt Mag. Gregor  Kohlbacher, Keesgasse 11, 8010 Graz, betreffend die Beschwerde vom 12. Oktober 2020 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 15. Mai 2020 über die Zurückweisung eines  Antrages auf Wiedereinsetzung in den vorigen Stand (hinsichtlich Umsatzsteuer 2014 bis 2017  und Umsatzsteuer 1-11/2018), Steuernummer 59-309/9934, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Gregor  Kohlbacher` | `Mag. Gregor  Kohlbacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Christian Soltendieck` (person)
- `Berthold Grosshans` (person)
- `Gruisla 3Q, 3231 Linsberg, Österreich` (address)
- `Berthold Grosshans` (person)
- `Seetal 31, 4661 Altmanning, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `59-309/9934` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/139070.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139070.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht fasst durch den Richter Mag. Günter Narat in der Revisionssache  Ferdinand Janßon, Robert-Musil-Gasse 10, 4631 Achleiten, Österreich  Steuernummer: 02-858/2848, vertreten durch den RA Mag.  Wolfgang Kempf, Bürgerstraße 41, 4020 Linz, über den Antrag der Revisionswerberin vom 18.  August, der gegen den Beschluss des Bundesfinanzgerichtes vom 5. Juli 2022,  RV/5100264/2021 (belangte Behörde: Finanzamt Österreich), betreffend die  Umsatzsteuerbescheide 2010 – 2017, erhobenen außerordentlichen Revision die  aufschiebende Wirkung zuzuerkennen, den Beschluss:   I)  Gem.

**False Positives:**

- `Mag.  Wolfgang Kempf` — partial — pred is substring of gold: `RA Mag.  Wolfgang Kempf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Ferdinand Janßon`(person)
- `Robert-Musil-Gasse 10, 4631 Achleiten, Österreich`(address)
- `02-858/2848`(tax_number)
- `RA Mag.  Wolfgang Kempf`(person)
- `Bundesfinanzgerichtes`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Saphira Schnaak, Kürschner Allee 44, 9300 Mail, Österreich, vertreten durch Ing. Mag. Hamza Ovacin,  Stadtstraße 33, Top 303, 6850 Dornbirn, betreffend Beschwerde vom 2. November 2022 gegen  die Bescheide des Finanzamtes Österreich vom 4. Oktober 2022 betreffend Körperschaftsteuer  2016 und Körperschaftsteuer 2017 zur Steuernummer 50-980/9446  beschlossen:  I. Der Vorlageantrag wird gem. § 278 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e BAO als  unzulässig zurückgewiesen.

**False Positives:**

- `Mag. Hamza Ovacin` — partial — pred is substring of gold: `Ing. Mag. Hamza Ovacin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Saphira Schnaak`(person)
- `Kürschner Allee 44, 9300 Mail, Österreich`(address)
- `Ing. Mag. Hamza Ovacin`(person)
- `Finanzamtes Österreich`(organisation)
- `50-980/9446`(tax_number)

</details>

---

## `Hon_Prof_in_Name` 🏆

**F1:** 0.085 | **Precision:** 0.798 | **Recall:** 0.045  

**Format:** `regex`  
**Rule ID:** `bc5a6e36`  
**Description:**
Captures names with 'Hon.-Prof.in' or 'Univ.-Prof.in' titles, including repeated titles like 'Univ.-Prof. Univ.-Prof.'.

**Content:**
```
\b(?:Hon\.-Prof\.(?:in)?\s+|Univ\.-Prof\.(?:in)?\s+)+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.798 | 0.045 | 0.085 | 104 | 83 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 83 | 21 | 1768 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_20`)


Seite 3 von 15 Erst anlässlich der mit Bericht vom 27.12.2010 abgeschlossenen Betriebsprüfung wurde die Ungewissheit, ob Liebhaberei im Zusammenhang mit der Vermietung des Objektes in Univ.-Prof.in Miriam Ungruh  vorliegt, beseitigt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_69`)


Die ersten Monate bis zur Erlangung der Aufenthalts- und Arbeitsbewilligung für Russland und bis mein Büro bei AG Russland und meine Dienstwohnung bezugsbereit waren, habe ich ausschließlich von Univ.-Prof.in Miriam Ungruh  aus gearbeitet.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_74`)


Sie haben mit mir in Univ.-Prof.in Miriam Ungruh  deren Strategie und Marktauftritt in Russland besprochen (z.B. DivFirmen DivFirmen uvm.).

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_75`)


o Ich habe russische Kunden, die Wien besuchten, von Univ.-Prof.in Miriam Ungruh  aus betreut;

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_76`)


sie nach Univ.-Prof.in Miriam Ungruh  zu Besprechungen und Workshops eingeladen (z.B. DivFirmen DivFirmen; uvm.) o In allen Fällen war ausschlaggebend, dass ich in Univ.-Prof.in Miriam Ungruh (Österreich) für „Westler“ leichter erreichbar war, ohne dass die Leute ein Visum besorgen und den teuren Aufenthalt in Moskau bezahlen mussten, um mich zu sehen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_81`)


o Um mir diese Arbeit in Univ.-Prof.in Miriam Ungruh  und in Österreich zu erleichtern, teilte mir AG zwei Dienstwägen zu: einen in Univ.-Prof.in Miriam Ungruh  und einen in Moskau. In Russland war ich ebenfalls rund um die Uhr im Einsatz: 14 Büros, 14 direkt berichtende Manager, 1200 Mitarbeiter, eine Forschungsstätte, eine PC Fabrik und diverse zusätzliche Infrastruktur wie Service Center, 2000 Partner Firmen, Partnerschaften mit über 100 Universitäten und über 2 Millionen Kunden im Jahr müssen eben betreut werden.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_101`)


Das Büro in Univ.-Prof.in Miriam Ungruh  war auch im Interesse meines Arbeitgebers.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Miriam Ungruh` | `Univ.-Prof.in Miriam Ungruh` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/128786.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128786.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adalbert Köseoglu  in der Beschwerdesache Christine Höffert,  Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich, über die Beschwerde vom 16. Februar 2016 gegen den Bescheid des Zollamtes  Salzburg vom 1. Februar 2016, 600000/00000/2016, betreffend Festsetzung einer  Abgabenerhöhung gemäß § 108 Abs. 1 ZollR-DG zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Adalbert Köseoglu` | `Hon.-Prof. Adalbert Köseoglu` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christine Höffert` (person)
- `Luggauer Weg 9, 7474 Sankt Kathrein im Burgenland, Österreich` (address)
- `Zollamtes  Salzburg` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Lieselotte Akdas  in der Beschwerdesache des  Eugen Volchert Hochraingasse 28, 4076 Valtau, Österreich StB über die Beschwerde vom 12. Juni 2017 gegen den Bescheid des  FA Baden Mödling  vom 7. Juni 2017 betreffend Normverbrauchsabgabe 04.2017 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Lieselotte Akdas` | `Univ.-Prof.in Lieselotte Akdas` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eugen Volchert` (person)
- `Hochraingasse 28, 4076 Valtau, Österreich` (address)
- `FA Baden Mödling` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129213.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129213.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eduard Lembrechts  in der Beschwerdesache Charles Rybalka,  Krumfeldener Straße 15, 9212 Töpriach, Österreich, über die Beschwerde vom 12.04.2011 gegen den Bescheid des Finanzamtes  Baden Mödling vom 25.03.2011 betreffend Umsatzsteuer 2009 Steuernummer *** zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Eduard Lembrechts` | `Hon.-Prof. Eduard Lembrechts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charles Rybalka` (person)
- `Krumfeldener Straße 15, 9212 Töpriach, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Michaela Dehnert  in der Beschwerdesache Elias Stiller,  Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich, über die Beschwerde vom 7. Februar 2013 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 8. Jänner 2013 betreffend E  ***/2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Michaela Dehnert` | `Hon.-Prof.in Michaela Dehnert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Stiller` (person)
- `Ritter-von-Gersdorff-Straße 8, 3141 Katzenberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Univ.-Prof.in Shoshana Leuther, Hagleithen 8, 3345 Strohmarkt, Österreich, über die Beschwerde vom 22. Mai 2020  (Einbringungsdatum) gegen den Bescheid des Finanzamtes Wien 2/20/21/22 vom 14. April  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer  12 80-897/7654  zu Recht erkannt:  A) Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Shoshana Leuther` | `Univ.-Prof.in Shoshana Leuther` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Christian Seywald` (person)
- `Hagleithen 8, 3345 Strohmarkt, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `80-897/7654` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/130288.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130288.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thomas Hutching  in der Beschwerdesache Hon.-Prof. Ruprecht Hauswerth,  Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich, Ungarn, über die Beschwerde gegen den Bescheid des FA Klosterneuburg  vom 27. März  2018, Steuernummer 26-476/7368, betreffend Einkommensteuer 2017 zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Thomas Hutching` | `Hon.-Prof. Thomas Hutching` |
| `Hon.-Prof. Ruprecht Hauswerth` | `Hon.-Prof. Ruprecht Hauswerth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Fahrbachgasse 13, 3130 St. Andrä an der Traisen, Österreich` (address)
- `FA Klosterneuburg` (organisation)
- `26-476/7368` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Achmed Karolzak  in der Beschwerdesache Lilia Löffelmann,  Karl Heinschild-Weg 29, 4980 Hübing, Österreich, vertreten durch M. Thaler Steuerberatung Kufstein GmbH, Prof. Sinwel-Weg 4,  6330 Kufstein, über die Beschwerde vom 5. September 2018 gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 8. August 2018 betreffend Wiederaufnahme der Verfahren  hinsichtlich Einkommensteuer für die Jahre 2012 bis 2015 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Achmed Karolzak` | `Univ.-Prof. Achmed Karolzak` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lilia Löffelmann` (person)
- `Karl Heinschild-Weg 29, 4980 Hübing, Österreich` (address)
- `M.` (person)
- `Finanzamtes` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Marceline Flory  in der Beschwerdesache Stephan Zeitlhuber,  Ödgegend 6, 4230 Selker, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die Beschwerden vom  9. November 2020 und vom 27. November 2020 gegen die Bescheide des Finanzamtes Wien  1/23 vom 6. Oktober 2020, Steuernummer 55-544/4748, betreffend  Energieabgabenvergütung für 2-12/2011 und für 2012 und über die Beschwerden vom  27. November 2020 gegen die Bescheide vom 2. November 2020 betreffend  Energieabgabenvergütung für 1-9/2013 und für 10/2013–9/2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Marceline Flory` | `Univ.-Prof.in Marceline Flory` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Stephan Zeitlhuber` (person)
- `Ödgegend 6, 4230 Selker, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Wien  1/23` (organisation)
- `55-544/4748` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hon.-Prof.in Elvira Thielsen, Gainfeldweg 91, 5231 Äpfelberg, Österreich, vertreten durch Weiß Rechtsanwälte, Walfischgasse 8/13, 1010  Wien, gegen die Bescheide des Finanzamtes Österreich betreffend Umsatzsteuer und  Einkommensteuer für die Jahre 1999 bis 2001 vom 11.9.2008 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Elvira Thielsen` | `Hon.-Prof.in Elvira Thielsen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Gainfeldweg 91, 5231 Äpfelberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dominik Mehlig` | `Hon.-Prof. Dominik Mehlig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Edith Schifferdecker` (person)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Marion Weßalowski  in der Beschwerdesache OMedR Leonhard Hestermeyer,  Sägerweg 5, 5450 Reitsam, Österreich, über die Beschwerde vom 7.12.2020 gegen den Bescheid des Finanzamtes  Österreich vom 2. Dezember 2020 betreffend Umsatzsteuer 01.2020-03.2020 Steuernummer  68- 52-932/8889  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` | `Univ.-Prof.in Univ.-Prof.in Marion Weßalowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Leonhard Hestermeyer` (person)
- `Sägerweg 5, 5450 Reitsam, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `52-932/8889` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132454.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christoph Hasenfraz  in der Beschwerdesache Olivia Sahlmüller,  Zinöck 26, 5134 Sengthal, Österreich, gegen den am 9. April 2018 ausgefertigten Bescheid der belangten Behörde  FA Grieskirchen Wels, nunmehr Finanzamt Österreich, betreffend Einkommensteuer für das Jahr 2017 und  den am 12. März 2019 von derselben Behörde ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Christoph Hasenfraz` | `Hon.-Prof. Christoph Hasenfraz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Olivia Sahlmüller` (person)
- `Zinöck 26, 5134 Sengthal, Österreich` (address)
- `FA Grieskirchen Wels` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Esra Nowy  über die Beschwerde vom   31.3.2014   der Jeremias Stuck , vertreten durch die Glatzhofer & Matschek Steuerberatungsgesellschaft mbH,  9020 Klagenfurt , gegen die Bescheide des Finanzamt Vorarlberg  vom 23.1.2014 betreffend  Festsetzung  Dienstgeberbeitrag und des Zuschlages zum Dienstgeberbeitrag 2010-2012           zu Recht erkannt:  Die bekämpften Bescheide werden aufgehoben (§ 279 Abs 1 BAO).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Esra Nowy` | `Hon.-Prof. Esra Nowy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Stuck` (person)
- `Glatzhofer & Matschek Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamt Vorarlberg` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/134359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134359.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Moses Dannebohm  in der Beschwerdesache Ruperta Schluckner,  Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich, vertreten durch WINKEL STEINER WAIBEL Steuerberater GmbH, Schweizer  Straße 77, 6845 Hohenems, über die Beschwerde vom 18. Februar 2019 gegen die Bescheide  des Finanzamtes Feldkirch vom 23. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 bis 2017 zu Recht erkannt:   I. Die angefochtenen Bescheide werden im Umfang der Einkommensteuerbescheide  (Beschwerdevorentscheidungen) 2015 bis 2017 vom 9. Dezember 2019 abgeändert.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Moses Dannebohm` | `Univ.-Prof. Moses Dannebohm` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ruperta Schluckner` (person)
- `Emmi-Freundlich-Gasse 51, 4713 Thongraben, Österreich` (address)
- `WINKEL STEINER WAIBEL Steuerberater GmbH` (organisation)
- `Finanzamtes Feldkirch` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/134640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134640.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Maurice Bettenhäuser  in der Beschwerdesache Miranda Weissert,  Teesdorferstraße 13, 9313 Unterlatschach, Österreich, über die Beschwerde vom 28.11.2020 gegen die Bescheide des Finanzamtes  Judenburg Liezen vom 29.10.2020 betreffend Einkommensteuer für das Jahr 2018 und  Umsatzsteuer für das Jahr 2018 beschlossen:  I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Maurice Bettenhäuser` | `Hon.-Prof. Maurice Bettenhäuser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Miranda Weissert` (person)
- `Teesdorferstraße 13, 9313 Unterlatschach, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/135129.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135129.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Walter Monheim  in der Beschwerdesache Enrico Steudtle,  Assing 21, 9071 Wurdach, Österreich, vertreten durch GEYER & GEYER Wirtschaftstreuhand GmbH, Rudolf von Alt- Platz 1, 1030 Wien, hinsichtlich der Beschwerde vom 23. November 2011 gegen die Bescheide  des Finanzamtes Wien 2/20/21/22 - nunmehr Finanzamtes Österreich - vom 25. Oktober 2011  betreffend Festsetzung der Kapitalertragsteuer 2007 bis 2010, Steuernummer  10-940/7308, den Beschluss:   I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als  unzulässig geworden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Walter Monheim` | `Hon.-Prof. Walter Monheim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Enrico Steudtle` (person)
- `Assing 21, 9071 Wurdach, Österreich` (address)
- `GEYER & GEYER Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Österreich` (organisation)
- `10-940/7308` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/135132.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135132.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Vanessa Nowikoff  in der Beschwerdesache des  KommR Lee Ponsard, Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich, über die Beschwerde vom 30. Juli 2020 gegen den Bescheid des  Finanzamtes X. (FA, jetzt Dienststelle des Finanzamt Freistadt Rohrbach Urfahr ) vom 10. Juli 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zur Steuernummer 63-102/2061  zu  Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 (1) BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Vanessa Nowikoff` | `Hon.-Prof.in Vanessa Nowikoff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `KommR Lee Ponsard` (person)
- `Bürmooser Landesstraße 3, 8522 Gussendorf, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `63-102/2061` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/135941.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135941.1_1`)


BESCHLUSS   Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Frederike Lipienski  in der Beschwerdesache des  Hademar Rüstow, Eck 124T, 2214 Auersthal, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des  FA Amstetten Melk Scheibbs (FA) vom 10. März 2021 über die Abweisung eines Antrages auf Wiederaufnahme §  303 BAO /  ESt 2017 zur Steuernummer 71-651/2158  beschlossen:   Der Vorlageantrag vom 29.Sept.2021 wird gemäß § 260 Abs. 1 lit. a iVm § 264 Abs. 4 lit e und  Abs. 5 BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Frederike Lipienski` | `Hon.-Prof.in Frederike Lipienski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hademar Rüstow` (person)
- `Eck 124T, 2214 Auersthal, Österreich` (address)
- `FA Amstetten Melk Scheibbs` (organisation)
- `71-651/2158` (tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/136077.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136077.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Univ.-Prof. Christian Lemanowitz  in der Beschwerdesache Dietmar Kachelmuss,  Reitschachersiedlung 7, 4925 Ecklham, Österreich, betreffend Beschwerden vom 31. Dezember 2021 und 12. Jänner 2022 gegen  die Bescheide des Finanzamtes Neunkirchen Wr. Neustadt vom 26. Juni 2019 betreffend  Einkommensteuer 2016, vom 04. September 2019 betreffend Einkommensteuer 2018 und vom  09. September 2020 betreffend Einkommensteuer 2019 den Beschluss:  I. Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Christian Lemanowitz` | `Univ.-Prof. Christian Lemanowitz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dietmar Kachelmuss` (person)
- `Reitschachersiedlung 7, 4925 Ecklham, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Günter Jedamczik  in der Beschwerdesache ÖkR Tobias Schönyan,  Kreuzerleitenweg 34, 5273 Hofing, Österreich, vertreten durch Herrn Mag. Gernot Thonhauser, Steuerberater,  Wernersdorf 111, 8551 Wies, über die Beschwerde vom 15.3.2022 gegen den Bescheid des  Finanzamtes Österreich vom 22.2.2022 betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Günter Jedamczik` | `Univ.-Prof. Günter Jedamczik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Tobias Schönyan` (person)
- `Kreuzerleitenweg 34, 5273 Hofing, Österreich` (address)
- `Mag. Gernot Thonhauser` (person)
- `Finanzamtes Österreich` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/137296.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137296.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dominika Juhass  in der Beschwerdesache  Ludmilla Hühnerfuß, Bakk. techn., Singham 20, 3465 Unterstockstall, Österreich,   über die Beschwerde vom 27. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom  12. Juni 2019 betreffend Vorsteuererstattung 2018 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dominika Juhass` | `Hon.-Prof.in Dominika Juhass` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ludmilla Hühnerfuß, Bakk. techn.` (person)
- `Singham 20, 3465 Unterstockstall, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Penelope Splettstösser  in der Beschwerdesache Wilhelm Schöbel,  Leopoldgasse 23, 8674 Grubbauer, Österreich, über die Beschwerde vom 10. Februar 2022 gegen den Bescheid des  Finanzamtes Österreich vom 3. Februar 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 32-896/6207  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Penelope Splettstösser` | `Univ.-Prof.in Penelope Splettstösser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wilhelm Schöbel` (person)
- `Leopoldgasse 23, 8674 Grubbauer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-896/6207` (tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Massimo Friedhoff  in der Beschwerdesache Jaden Grothmann  vertreten  durch RA1, über die Beschwerde gegen den Bescheid des Finanzamt Wien 1/23  vom 16. Jänner 2019,  Steuernummer 32-847/2958, über die Festsetzung einer Zwangsstrafe (Stichtag  16.01.2019) nach Durchführung einer mündlichen Verhandlung am 14. April 2022, im Beisein  des Schriftführers SF, zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Massimo Friedhoff` | `Univ.-Prof. Massimo Friedhoff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jaden Grothmann` (person)
- `Finanzamt Wien 1/23` (organisation)
- `32-847/2958` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/137626.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137626.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Barbara Schwalb  in der Beschwerdesache Annalena Mlynarcik,  Ledochowskastraße 5, 4040 Kammerschlag, Österreich, über die Beschwerde vom 02.03.2017 gegen die Bescheide des Finanzamtes  Österreich vom 28. Februar 2017 betreffend Abweisung des Antrages auf Wiederaufnahme des  Verfahrens hinsichtlich Einkommensteuer für die Jahre Wiederaufnahme § 303 BAO /  ESt 2011  -2013 Steuernummer 09-012/5071  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Barbara Schwalb` | `Hon.-Prof.in Barbara Schwalb` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annalena Mlynarcik` (person)
- `Ledochowskastraße 5, 4040 Kammerschlag, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `09-012/5071` (tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/138184.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Gernot Schellhaas  in der Beschwerdesache Guntram Garweg,  Umspannwerkstraße 21, 3912 Kleinnondorf, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des Finanzamtes  Österreich vom 16. März 2020 betreffend Erhöhungsbetrag zur Familienbeihilfe wegen  erheblicher Behinderung für den Zeitraum September 2015 bis Jänner 2019, Steuernummer  92-268/1285,  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Univ.-Prof. Gernot Schellhaas` | `Univ.-Prof. Univ.-Prof. Gernot Schellhaas` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Guntram Garweg` (person)
- `Umspannwerkstraße 21, 3912 Kleinnondorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `92-268/1285` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/138353.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138353.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hubert Wunderlin  in der Beschwerdesache Friedhelm Fomin,  Riedlbachstraße 8, 3970 Oberbrühl, Österreich, vertreten durch ECOVIS Austria Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H., Postfach 257, 1061 Wien Postfach, über die Beschwerde  vom 15. August 2021 gegen den Bescheid des Finanzamtes Österreich vom 13. Juli 2021  betreffend Covid-19 Zahlungserleichterung, Steuernummer 25-245/7156, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Hubert Wunderlin` | `Hon.-Prof. Hubert Wunderlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Friedhelm Fomin` (person)
- `Riedlbachstraße 8, 3970 Oberbrühl, Österreich` (address)
- `ECOVIS Austria Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)
- `25-245/7156` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/138513.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138513.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Univ.-Prof.in Verena Sobzig  über die Beschwerde des  Peter Scheidhauer, Klimaweg 103, 8232 Untersafen, Österreich, vom 31.05.2022 gegen den Bescheid des Finanzamtes Österreich vom  26.04.2022 betreffend Abweisung eines Antrages auf Nachsicht zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Verena Sobzig` | `Univ.-Prof.in Verena Sobzig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Peter Scheidhauer` (person)
- `Klimaweg 103, 8232 Untersafen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Christine Gäbelt  in der Beschwerdesache Verena Piechura,  Nußöd 5, 2014 Breitenwaida, Österreich, über die Beschwerde vom 7. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 13. Juni 2022, Ordnungsbegriff Nr1, betreffend die Rückforderung zu Unrecht  bezogener Beträge   1. an Familienbeihilfe und Kinderabsetzbetrag für den Zeitraum Oktober 2021 bis        Juni 2022 für den Sohn B  2.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Christine Gäbelt` | `Univ.-Prof.in Christine Gäbelt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Verena Piechura` (person)
- `Nußöd 5, 2014 Breitenwaida, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/138725.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138725.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. David Eckerlin  in der Beschwerdesache Margarete Wasmeir,  Voglstraße 19, 4902 Schlaugenham, Österreich, vertreten durch Mag. Kurt Caspari Steuerberatungs KG, Hirnreit 173, 5771  Leogang, über die Beschwerde vom 29. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 11. Juli 2022 betreffend Säumniszuschlag 2022 Steuernummer 09-312/4413  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. David Eckerlin` | `Univ.-Prof. David Eckerlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Margarete Wasmeir` (person)
- `Voglstraße 19, 4902 Schlaugenham, Österreich` (address)
- `Mag. Kurt Caspari Steuerberatungs KG` (organisation)
- `Finanzamtes  Österreich` (organisation)
- `09-312/4413` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/139502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ludmilla Achmiller   in der Beschwerdesache des Harald Köbbe, Hammerfeldstraße 64, 4707 Fürth, Österreich,  betreffend die Bescheide des FA Amstetten Melk Scheibbs  vom 24. September 2021  hinsichtlich Abweisung von Anträgen auf Wiederaufnahme § 303 BAO /  ESt 2018 und ESt 2019  Steuernummer, 50-782/0766,   zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ludmilla Achmiller` | `Hon.-Prof.in Ludmilla Achmiller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Köbbe` (person)
- `Hammerfeldstraße 64, 4707 Fürth, Österreich` (address)
- `FA Amstetten Melk Scheibbs` (organisation)
- `50-782/0766` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Zlatan Tegtmeier  in der Angelegenheit der Parteien  Dipl. Kfm. VetR Gerhard Stranz (Beschwerdeführerin), vertreten durch die   Confida Wolfsberg  Steuerberatungsgesellschaft m.b.H., 9400 Wolfsberg  und Finanzamt Oststeiermark, 1000 Wien, PF 251  als  Amtspartei über die Beschwerden vom 12.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Zlatan Tegtmeier` | `Hon.-Prof. Zlatan Tegtmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kfm. VetR Gerhard Stranz` (person)
- `Confida Wolfsberg  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamt Oststeiermark` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/139538.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139538.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Rebecca Altemüller  in der Beschwerdesache Theodor Strohmeier,  Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich  über die Beschwerde vom 1. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 18. Juli 2019 betreffend Abweisung des Antrags vom 20.  März 2019 auf Gewährung der Familienbeihilfe und des Kinderabsetzbetrages ohne Vornahme  einer Indexierung gemäß § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Rebecca Altemüller` | `Hon.-Prof.in Rebecca Altemüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Theodor Strohmeier` (person)
- `Bruggenfeldstraße 16, 8933 Bergerviertel, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/139968.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139968.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Marianne Oberscheidt  in der Beschwerdesache Dipl. Kff. Aurelia Riem,  Sappl - Keuschpeter 68, 5233 Irnstötten, Österreich  über die Beschwerde vom 20. Dezember 2019 gegen den Bescheid des  Finanzamtes Bruck Eisenstadt Oberwart vom 29. November 2019 betreffend Abweisung des  Antrags vom 5. März 2019 auf Gewährung der Familienbeihilfe und des Kinderabsetzbetrages  ohne Vornahme einer Indexierung gemäß § 8a Familienlastenausgleichsgesetz 1967 (FLAG  1967), SV-Nr. Nr., zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Marianne Oberscheidt` | `Hon.-Prof.in Marianne Oberscheidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kff. Aurelia Riem` (person)
- `Sappl - Keuschpeter 68, 5233 Irnstötten, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/140642.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140642.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Emanuel Gentner  in der Beschwerdesache Alva Selmayr,  Hatscheksiedlung 9, 8524 Gamsgebirg, Österreich, vertreten durch at reutte Steuerberatungs GmbH, Unterdorf 1, 6600  Lechaschau, gegen den von der belangten Behörde Finanzamt Österreich am 30. September  2022 zu Steuernummer 35-106/4702  ausgefertigten Einkommensteuerbescheid 2019 zu  Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 Abs. 1 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Emanuel Gentner` | `Univ.-Prof. Emanuel Gentner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alva Selmayr` (person)
- `Hatscheksiedlung 9, 8524 Gamsgebirg, Österreich` (address)
- `at reutte Steuerberatungs GmbH` (organisation)
- `Finanzamt Österreich` (organisation)
- `35-106/4702` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Chiara Wälte  in der Beschwerdesache Dagobert Duewel,  Karl Schäfer-Gasse 25, 2161 Poysbrunn, Österreich, über die Beschwerde vom 18. Oktober 2022 gegen die Bescheide des  Finanzamtes Österreich vom 12. September 2022, Ordnungsbegriff Nr1, betreffend Abweisung  der Anträge auf Familienbeihilfe und Erhöhungsbetrag für den Zeitraum ab Juni 2022 zu Recht  erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Chiara Wälte` | `Hon.-Prof.in Chiara Wälte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dagobert Duewel` (person)
- `Karl Schäfer-Gasse 25, 2161 Poysbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/140767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140767.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 14. Dezember 2021 der Beschwerdeführerin Hon.-Prof. Igor Rockermair, Myrthengasse 17, 9121 Hungerrain, Österreich  Steuernummer:  95-241/7343, vertreten durch die FUSSEIS Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H., Bahnhofstraße 63, 4910 Ried im Innkreis, gegen die  Bescheide des Finanzamtes Österreich vom 30. November 2021 betreffend Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2018 – 2020  zu Recht:  I)  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Igor Rockermair` | `Hon.-Prof. Igor Rockermair` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Günter Narat` (person)
- `Myrthengasse 17, 9121 Hungerrain, Österreich` (address)
- `95-241/7343` (tax_number)
- `FUSSEIS Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/140867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140867.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Philipp Nosalek  in der Beschwerdesache Merlin Buechner,  Am Waldfriedhof 19-24, 4714 Gferet, Österreich, vertreten durch Dr. Martin Eisenberger, Muchargasse 30, 8010 Graz, über die  Beschwerde vom 17. Mai 2017 gegen den Bescheid des Zollamtes Österreich vom 11. April  2017, Zl. 700000/03287/2017, betreffend Aussetzungszinsen zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Philipp Nosalek` | `Hon.-Prof. Philipp Nosalek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Merlin Buechner` (person)
- `Am Waldfriedhof 19-24, 4714 Gferet, Österreich` (address)
- `Dr. Martin Eisenberger` (person)
- `Zollamtes Österreich` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/141100.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141100.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait  in der Beschwerdesache   Prof. Ing. Eduard Skroblies, Forchetweg 18, 4692 Albertsham, Österreich,   über die Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf (nunmehr Finanzamt Österreich) vom 10. November 2014 betreffend  Körperschaftsteuer 2011, vom 19. November 2014 betreffend Körperschaftsteuer 2012 und  2013 sowie die Beschwerde vom 12. Juli 2016 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 7. Juli 2016 betreffend Körperschaftsteuer 2014   I. beschlossen:  Der Vorlageantrag betreffend Körperschaftsteuer 2011 wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait` | `Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof. Ing. Eduard Skroblies` (person)
- `Forchetweg 18, 4692 Albertsham, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/141142.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141142.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Felizia Marschinke  in der Beschwerdesache Sven Hoepfl,  Kelterweg 7, 8382 Mogersdorf, Österreich, über die Beschwerde vom 25. Juli 2022 gegen den Bescheid des Finanzamtes  Österreich vom 22. Juli 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021  Steuernummer 12-858/0237  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Felizia Marschinke` | `Hon.-Prof.in Felizia Marschinke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sven Hoepfl` (person)
- `Kelterweg 7, 8382 Mogersdorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `12-858/0237` (tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/141195.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141195.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paula Tschann  in der Beschwerdesache Merlin Dankwort,  Urtelgasse 9y, 8232 Stambach, Österreich  vertreten durch Valerian Stamataki, Schanze 29 12, 3661 Unterthalheim, Österreich, über die Beschwerde vom  6. September 2022 gegen den Bescheid des Finanzamtes Österreich vom 9. August 2022  betreffend Festsetzung eines ersten Säumniszuschlages, Steuernummer 88-049/5894  nach  Durchführung einer mündlichen Verhandlung zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Paula Tschann` | `Univ.-Prof.in Paula Tschann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Merlin Dankwort` (person)
- `Urtelgasse 9y, 8232 Stambach, Österreich` (address)
- `Valerian Stamataki` (person)
- `Schanze 29 12, 3661 Unterthalheim, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `88-049/5894` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/141269.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141269.1_15`)


II. Über die Beschwerde wurde erwogen:  1. Sachverhalt   Die Bf. bezieht im Streitjahr 2022 Einkünfte aus nichtselbständiger Arbeit und für die beiden  minderjährigen Kinder Familienbeihilfe (Silvius Groenenwald; Hon.-Prof. Friedhelm Matauscheck).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Friedhelm Matauscheck` | `Hon.-Prof. Friedhelm Matauscheck` |

**Missed by this rule (FN):**

- `Silvius Groenenwald` (person)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Svenja Kieble  in der Beschwerdesache Vera Henssel, Bakk. rer. nat.,  Lärchenhofweg 43, 4073 Dörnbach, Österreich, über die Beschwerde vom 3. März 2022 gegen die Bescheide des Finanzamtes  Österreich vom 7. Februar 2022, Ordnungsbegriff Nr1, betreffend Abweisung der Anträge auf  Familienbeihilfe und Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung für  den Zeitraum ab August 2021 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Svenja Kieble` | `Hon.-Prof.in Svenja Kieble` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vera Henssel, Bakk. rer. nat.` (person)
- `Lärchenhofweg 43, 4073 Dörnbach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/142523.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142523.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Geraldine Matuschefski  in der Beschwerdesache der Demircan Metall AG&  atypisch stille Gesellschaft, vertreten durch xx Steuerberatung und Wirtschaftsprüfung,  Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafterinnen  1.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Geraldine Matuschefski` | `Hon.-Prof.in Geraldine Matuschefski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Demircan Metall AG` (organisation)
- `xx Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/142556.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142556.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Juliette Burgmann  in der Beschwerdesache Ibrahim Hofler,  Sennstraße 7, 4084 Scharzeredt, Österreich, betreffend Beschwerde vom 23. August 2021 gegen den Bescheid des  Finanzamtes Österreich vom 4. August 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 Steuernummer 26-497/2277  beschlossen:  Der eingebrachte Vorlageantrag vom 5. Mai 2022 wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Juliette Burgmann` | `Hon.-Prof.in Juliette Burgmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibrahim Hofler` (person)
- `Sennstraße 7, 4084 Scharzeredt, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `26-497/2277` (tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/142680.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142680.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Moritz Lindstaedt  in der Beschwerdesache Samuel Rattai,  Hilzing 64, 2880 Kranichberg, Österreich, vertreten durch Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH, Lehargasse 3A Tür 14, 1060 Wien, über die Beschwerde vom  7. September 2023 gegen den Bescheid des Finanzamtes Österreich vom 30. August 2023  betreffend Zahlungserleichterungen gem. § 212 BAO, Steuernummer 30-750/1577, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Moritz Lindstaedt` | `Hon.-Prof. Moritz Lindstaedt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Samuel Rattai` (person)
- `Hilzing 64, 2880 Kranichberg, Österreich` (address)
- `Dr. Peter Wolf Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `30-750/1577` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/142831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Denise Hatwiger  in der Beschwerdesache Svenja Gelonek,  Leutschacher Straße 37, 9344 Wullroß, Österreich, über die Beschwerden gegen die Bescheide des Finanzamt Oststeiermark (jetzt Finanzamt  Österreich) betreffend Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2013 bis  2017 sowie Anspruchszinsen 2014 und 2015, Steuernummer 46-265/1377, zu Recht erkannt:   I. Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Denise Hatwiger` | `Univ.-Prof.in Denise Hatwiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Svenja Gelonek` (person)
- `Leutschacher Straße 37, 9344 Wullroß, Österreich` (address)
- `Finanzamt Oststeiermark` (organisation)
- `Finanzamt  Österreich` (organisation)
- `46-265/1377` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/144086.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144086.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ruperta Wengrzinek  in der Beschwerdesache Ali Oberste,  Wolfsedt 11, 4211 Lindach, Österreich, Steuernummer 03-949/9780  über die Beschwerde vom 7. August 2019  gegen den Bescheid des Finanzamtes Feldkirch vom 30. Juli 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ruperta Wengrzinek` | `Hon.-Prof.in Ruperta Wengrzinek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ali Oberste` (person)
- `Wolfsedt 11, 4211 Lindach, Österreich` (address)
- `03-949/9780` (tax_number)
- `Finanzamtes Feldkirch` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/144195.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144195.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Gottfried Dimitriou  in der Beschwerdesache RgR Adam Lenk,  Prüfing 9, 5451 Wimm, Österreich, betreffend die Beschwerden vom 20. November 2023 gegen die Bescheide des  Finanzamtes Österreich vom 22. August 2023 betreffend Einkommensteuer 2020 und 2021 zu  Steuernummer 47-369/1528  beschlossen:  Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Gottfried Dimitriou` | `Hon.-Prof. Gottfried Dimitriou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `RgR Adam Lenk` (person)
- `Prüfing 9, 5451 Wimm, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `47-369/1528` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/144853.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144853.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Samir Holeweg  in der Beschwerdesache Kassandra Lensler,  Südweg III 40, 6346 Eiberg, Österreich, über die Beschwerde vom 9. Februar 2022 gegen den Bescheid des Finanzamt Baden Mödling  vom 31. Jänner 2022 betreffend Zahlungserleichterungen § 212 BAO 2022 Steuernummer  57-603/5979  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Samir Holeweg` | `Univ.-Prof. Samir Holeweg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kassandra Lensler` (person)
- `Südweg III 40, 6346 Eiberg, Österreich` (address)
- `Finanzamt Baden Mödling` (organisation)
- `57-603/5979` (tax_number)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_193`)


Die Vertreterin des Finanzamtes beantragt die teilweise Stattgabe der Beschwerde, und zwar  die Anerkennung der Beträge laut BVE und zusätzlich der Fahrtkosten zu Univ.-Prof. Massimo Brokmeyer(€ 25,20)), im  Übrigen die Abweisung der Beschwerde.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Massimo Brokmeyer` | `Univ.-Prof. Massimo Brokmeyer` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/145657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145657.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Gotthard Peerbooms  in der Beschwerdesache Elmar Wawczyniak,  Laurentius-Weg 77q, 8740 Farrach, Österreich, über die Beschwerde vom 13. Jänner 2022 gegen den Bescheid des FA Klagenfurt St. Veit Wolfsberg  vom 7. Jänner 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020  Steuernummer *** zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Gotthard Peerbooms` | `Hon.-Prof. Gotthard Peerbooms` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elmar Wawczyniak` (person)
- `Laurentius-Weg 77q, 8740 Farrach, Österreich` (address)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/145836.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145836.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Gerda Höfelmair  in der Beschwerdesache des  Ingolf Hillbig, über die Beschwerde vom 11. Jänner 2023 gegen den Bescheid des FA Wien 2/20/21/22  vom  15. Dezember 2022 betreffend Einkommensteuer 2021 zu Steuernummer 92-987/6769  nach der  mündlichen Verhandlung am 5. September 2024 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Gerda Höfelmair` | `Univ.-Prof.in Gerda Höfelmair` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ingolf Hillbig` (person)
- `FA Wien 2/20/21/22` (organisation)
- `92-987/6769` (tax_number)

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/145892.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145892.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karin Gebhardi  in der Beschwerdesache Gotthard Sträßner,  Schmidsdorf Straße 31, 3142 Gunnersdorf, Österreich, Ungarn, über die Beschwerde vom 4. Dezember 2017 gegen die Bescheide des  FA Spittal Villach (nunmehr Finanzamt Österreich) vom 10. November 2017, zu Steuernummer  09-485/6394, betreffend die Abweisung des Antrags vom 14. Oktober 2017 auf  Wiederaufnahme der Verfahren hinsichtlich Einkommensteuer 2014 und 2015 zu Recht  erkannt:   I. Die angefochtenen Bescheide vom 10. November 2017, mit denen der in eventu  eingebrachte Antrag auf Wiederaufnahme der Verfahren betreffend  Einkommensteuer 2014 und 2015 abgewiesen wurde, werden wegen  Unzuständigkeit aufgehoben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Karin Gebhardi` | `Univ.-Prof.in Karin Gebhardi` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gotthard Sträßner` (person)
- `Schmidsdorf Straße 31, 3142 Gunnersdorf, Österreich` (address)
- `FA Spittal Villach` (organisation)
- `Finanzamt Österreich` (organisation)
- `09-485/6394` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/146422.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146422.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Elmira Walkenbach  in der Beschwerdesache der  JLFT Robotik, Hptm.-Kluibenschedl-Straße 16, 2262 Grub an der March, Österreich, über die am 8.August 2023 eingebrachte Beschwerde gegen den  zur Steuernummer 38-455/9315  ergangenen Bescheid des FA Innsbruck  vom 31. Juli 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Elmira Walkenbach` | `Hon.-Prof.in Elmira Walkenbach` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `JLFT Robotik` (organisation)
- `Hptm.-Kluibenschedl-Straße 16, 2262 Grub an der March, Österreich` (address)
- `38-455/9315` (tax_number)
- `FA Innsbruck` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/146319.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146319.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Univ.-Prof. Wladimir Schaeffer  in der Beschwerdesache  Scarlett Ever, Felle 6, 4264 Unterrauchenödt, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8/5.01, 1010 Wien, über die Beschwerde vom  10. Oktober 2024 gegen den Bescheid des Finanzamtes für Großbetriebe vom 18. September  2024 betreffend Festsetzung des Energiekrisenbeitrag- Strom (EKB-S) für den Zeitraum 1. Juli  2023 bis 31. Dezember 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Wladimir Schaeffer` | `Univ.-Prof. Wladimir Schaeffer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Scarlett Ever` (person)
- `Felle 6, 4264 Unterrauchenödt, Österreich` (address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH` (organisation)
- `Finanzamtes für Großbetriebe` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/146532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146532.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Martin Hartig  in der Beschwerdesache Valentina Schleifert,  Walleckstraße 613, 2126 Pürstendorf, Österreich, über die Beschwerde vom 24.7.2023 gegen den Bescheid des Finanzamtes  Österreich vom 13.7.2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Martin Hartig` | `Univ.-Prof. Martin Hartig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Valentina Schleifert` (person)
- `Walleckstraße 613, 2126 Pürstendorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/146652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146652.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Niklas Hussung  in der Beschwerdesache Univ.-Prof. Oliver Ruhsbüldt,  Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich, vertreten durch Gattringer Steuerberatung GmbH, Sonnensteinstraße 12, 4040  Linz, über die Beschwerde vom 31. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 16. Mai 2023 betreffend Einkommensteuer 2021 Steuernummer 26-058/9655  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Oliver Ruhsbüldt` | `Univ.-Prof. Oliver Ruhsbüldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Niklas Hussung` (person)
- `Heachgassweg, Oberau 13, 3452 Tautendorf, Österreich` (address)
- `Gattringer Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `26-058/9655` (tax_number)

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/147055.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147055.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Karl Konstandin  in der Beschwerdesache Barbara West,  Josef-Steinberger-Weg 26, 4623 Au bei Hischmannsberg, Österreich, vertreten durch BEURLE Rechtsanwälte GmbH & Co KG, Landstraße 9, 4020  Linz, über die Beschwerde vom 27.11.2024 gegen den Bescheid des Finanzamtes Österreich  vom 6.11.2024 betreffend Abweisung eines Antrages auf bescheidmäßige Festsetzung des  Energiekrisenbeitrages-Strom (EKB-S) für den Zeitraum Jänner 2024 bis Juni 2024 zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Karl Konstandin` | `Univ.-Prof. Karl Konstandin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Barbara West` (person)
- `Josef-Steinberger-Weg 26, 4623 Au bei Hischmannsberg, Österreich` (address)
- `BEURLE Rechtsanwälte GmbH & Co KG` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/147654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147654.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Univ.-Prof.in Maja Lauers  in der Säumnisbeschwerdesache  Univ.-Prof. Mehmet Klasema, Labon 67, 4861 Looh, Österreich  vertreten durch Jonathan Goessl, über die Beschwerde vom 8. Jänner  2025 wegen behaupteter Verletzung der Entscheidungspflicht durch das Finanzamt Österreich  betreffend Bescheidbeschwerde vom 12. April 2024 gegen den Bescheid betreffend die  Abweisung des Antrages auf Wiederaufnahme des Verfahrens gemäß § 303 BAO  (Körperschaftsteuer 2021) vom 13. März 2024, Steuernummer 85-153/1153, den Beschluss:  I. Das Säumnisbeschwerdeverfahren wird eingestellt.  II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 in Verbindung mit  Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Maja Lauers` | `Univ.-Prof.in Maja Lauers` |
| `Univ.-Prof. Mehmet Klasema` | `Univ.-Prof. Mehmet Klasema` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Labon 67, 4861 Looh, Österreich` (address)
- `Jonathan Goessl` (person)
- `Finanzamt Österreich` (organisation)
- `85-153/1153` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/147654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147654.1_2`)


Begründung  1. Festgestellter Sachverhalt und Beweiswürdigung  Die Univ.-Prof. Mehmet Klasema  stellte mit Eingabe vom 27. Februar 2024 den Antrag auf Wiederaufnahme des  Verfahrens gemäß § 303 Bundesabgabenordnung (BAO) und Erlassung des  Körperschaftsteuerbescheides 2021 unter Berücksichtigung der beigelegten korrigierten  Körperschaftsteuererklärung für 2021.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Mehmet Klasema` | `Univ.-Prof. Mehmet Klasema` |

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/147955.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147955.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Christian Soltendieck  in der Beschwerdesache des Dr. MV  als Masseverwalter (MV) im Insolvenzverfahren der Berthold Grosshans, Gruisla 3Q, 3231 Linsberg, Österreich  vertreten durch  die Berthold Grosshans, Seetal 31, 4661 Altmanning, Österreich  nunmehr vertreten durch Rechtsanwalt Mag. Gregor  Kohlbacher, Keesgasse 11, 8010 Graz, betreffend die Beschwerde vom 12. Oktober 2020 gegen  den Bescheid des Finanzamtes Graz-Stadt vom 15. Mai 2020 über die Zurückweisung eines  Antrages auf Wiedereinsetzung in den vorigen Stand (hinsichtlich Umsatzsteuer 2014 bis 2017  und Umsatzsteuer 1-11/2018), Steuernummer 59-309/9934, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Christian Soltendieck` | `Hon.-Prof. Christian Soltendieck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Berthold Grosshans` (person)
- `Gruisla 3Q, 3231 Linsberg, Österreich` (address)
- `Berthold Grosshans` (person)
- `Seetal 31, 4661 Altmanning, Österreich` (address)
- `Mag. Gregor  Kohlbacher` (person)
- `Finanzamtes Graz-Stadt` (organisation)
- `59-309/9934` (tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/147920.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Irmgard Rockner  in der Beschwerdesache Samuel Klimasz,  Lorbeerweg 6A, 2202 Enzersfeld im Weinviertel, Österreich, über die Beschwerde vom 16. Mai 2019 gegen den Bescheid des Finanzamtes  Baden Mödling vom 24. April 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 Steuernummer 24-613/0227  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Irmgard Rockner` | `Univ.-Prof.in Irmgard Rockner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Samuel Klimasz` (person)
- `Lorbeerweg 6A, 2202 Enzersfeld im Weinviertel, Österreich` (address)
- `Finanzamtes  Baden Mödling` (organisation)
- `24-613/0227` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/147990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147990.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Leila Garnschröder  in der Beschwerdesache  RgR Corbinian Baranowskij, Schwamingstraße 19, 5452 Reitsam, Österreich, über die Beschwerde vom 6. März 2025 gegen den Bescheid des  Finanzamtes Österreich vom 6. Februar 2025 betreffend Zwangsstrafen 2023 Steuernummer  15-984/7137  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und die Zwangsstrafen mit  150,00 Euro für die Körperschaftssteuererklärung und mit 150,00 Euro für die  Umsatzsteuererklärung (insgesamt somit mit 300,00 Euro) festgesetzt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Leila Garnschröder` | `Univ.-Prof.in Leila Garnschröder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `RgR Corbinian Baranowskij` (person)
- `Schwamingstraße 19, 5452 Reitsam, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `15-984/7137` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/148001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paulina Borisowa  in der Beschwerdesache Ilhan Feldmeier, Bakk. rer. nat.,  Sittenbergstraße 9, 4294 Stampfendorf, Österreich, vertreten durch Mag. Benno Elmar Di Gaspero, Unterer Platz 7, 9372  Eberstein, über die Beschwerde vom 14. Juni 2024 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juni 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023  Steuernummer 14-548/3314  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Paulina Borisowa` | `Univ.-Prof.in Paulina Borisowa` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ilhan Feldmeier, Bakk. rer. nat.` (person)
- `Sittenbergstraße 9, 4294 Stampfendorf, Österreich` (address)
- `Mag. Benno Elmar Di Gaspero` (person)
- `Finanzamtes  Österreich` (organisation)
- `14-548/3314` (tax_number)

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/148387.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148387.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Miklos Backhaus  in der Beschwerdesache Donald Wiesemeier,  Funkgasse 177, 3761 Grub, Österreich, über die Beschwerde vom 24. Oktober 2023 gegen den Bescheid des  Finanzamtes Österreich vom 12. Oktober 2023 betreffend Zahlungserleichterungen,  Steuernummer 78-871/6103, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Miklos Backhaus` | `Hon.-Prof. Miklos Backhaus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Donald Wiesemeier` (person)
- `Funkgasse 177, 3761 Grub, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `78-871/6103` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/148554.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148554.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Koolen  in der Beschwerdesache   Univ.-Prof. Brian Salemi, Ulrichskirchen 3, 4184 Neuschlag, Österreich, Philippinen, Steuernummer 63-391/9556  über die Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamt Grieskirchen Wels  vom 1. Februar  2018 betreffend Vorsteuererstattung 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Brian Salemi` | `Univ.-Prof. Brian Salemi` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Regina Koolen` (person)
- `Ulrichskirchen 3, 4184 Neuschlag, Österreich` (address)
- `63-391/9556` (tax_number)
- `Finanzamt Grieskirchen Wels` (organisation)

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/148554.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148554.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin, die Univ.-Prof. Brian Salemi (im Folgenden kurz: Bf.) ist ein  Telekommunikationsunternehmen auf den Philippinen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Brian Salemi` | `Univ.-Prof. Brian Salemi` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/149185.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149185.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Hon.-Prof.in Alice Siemglüß  in der Beschwerdesache   Wendy Schuch, Sörg 19, 5441 Erlfeld, Österreich,   betreffend Beschwerde vom 29. August 2024 gegen den Bescheid des Finanzamtes Österreich  vom 1. August 2024 betreffend Umsatzsteuer 2023 beschlossen:    I. Dem Gerichtshof der Europäischen Union werden gemäß Artikel 267 AEUV die Fragen  zur Vorabentscheidung vorgelegt, die die Auslegung der Richtlinie 2006/112/EG des  Rates vom 28. November 2006 über das gemeinsame Mehrwertsteuersystem (in der  Folge MwSt-Richtlinie) und der Achten Richtlinie 79/1072/EWG des Rates vom  6. Dezember 1979 betreffen:   1. Ist die Bekanntgabe einer MwSt-Identifikationsnummer eines anderen  Mitgliedstaates als des Mitgliedstaates, in dem die Versendung oder  Beförderung eines Gegenstandes beginnt, gemäß Art 138 Abs. 1 Buchst.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Hon.-Prof.in Alice Siemglüß` | `Hon.-Prof.in Hon.-Prof.in Alice Siemglüß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wendy Schuch` (person)
- `Sörg 19, 5441 Erlfeld, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Gerichtshof der Europäischen Union` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Shakira Unterbusch  in der Beschwerdesache Norbert Seybt,  Harzhausergasse 66, 8362 Ruppersdorf, Österreich, über die Beschwerde vom 12. November 2024 gegen den Bescheid des  Finanzamt Freistadt Rohrbach Urfahr  vom 11. November 2024 betreffend Abweisung des Antrags auf Familienbeihilfe für  den Zeitraum ab 11/2024 vom 30.10.2024, eingebracht am 30.10.2024, sowie gegen den  Bescheid des Finanzamtes Österreich betreffend Abweisung des Antrags auf Erhöhungsbetrag  wegen erheblicher Behinderung für den Zeitraum ab 11/2024 vom 31.10.2024, eingebracht am  31.10.2024, Steuernummer 22-872/9827, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Shakira Unterbusch` | `Univ.-Prof.in Shakira Unterbusch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Norbert Seybt` (person)
- `Harzhausergasse 66, 8362 Ruppersdorf, Österreich` (address)
- `Finanzamt Freistadt Rohrbach Urfahr` (organisation)
- `Finanzamtes Österreich` (organisation)
- `22-872/9827` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Piedro Klingebiel  in der Beschwerdesache 1. der  Tamara Gottschalch  und 2. der Heidemarie Egghart, beide in ***Bf1 und Bf2-Adr***, beide steuerlich vertreten  durch Allgäuer & Partner - Wirtschaftsprüfungs und Steuerberatungs GmbH, Schloßgraben 10,  6800 Feldkirch, über die Beschwerde vom 22.05.2018 gegen den Bescheid des Finanzamtes  Feldkirch vom 12. März 2018 betreffend Feststellungsbescheid Gruppenmitglied 2015  Tamara Gottschalch 22-144/9009  nach Durchführung einer mündlichen Verhandlung, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Piedro Klingebiel` | `Univ.-Prof. Piedro Klingebiel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tamara Gottschalch` (person)
- `Heidemarie Egghart` (person)
- `Allgäuer & Partner - Wirtschaftsprüfungs und Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Tamara Gottschalch` (person)
- `22-144/9009` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/149853.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149853.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Bodo Stocklauser  in der Beschwerdesache des  Kirstin Nitschner, Fabjan-Hafner-Passage 11, 5274 Alharting, Österreich, betreffend die Beschwerde vom 27. Februar 2024 (bzw. den  ebenfalls als „Beschwerde“ bezeichneten Vorlageantrag vom 7. Juni 2024) gegen den Bescheid  des Finanzamtes Österreich vom 14. Februar 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023, Steuernummer 77-148/0749, beschlossen:  Der Vorlageantrag vom 7. Juni 2024 wird gemäß § 264 Abs. 4 lit. e iVm. § 260 Abs. 1 lit. b BAO  als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Bodo Stocklauser` | `Univ.-Prof. Bodo Stocklauser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kirstin Nitschner` (person)
- `Fabjan-Hafner-Passage 11, 5274 Alharting, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `77-148/0749` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/149850.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149850.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Univ.-Prof. Ludwig Bäumcker  in der Beschwerdesache  Anneliese Plogmacher, Kamlweg 67, 4843 Wörmansedt, Österreich, vertreten durch SFB Alber & Co Steuerberatungs- gesellschaft für  freie Berufe OG, Weihburggasse 4/2/29, 1010 Wien, über die Beschwerde vom 1. Oktober  2025 gegen den Bescheid des Finanzamtes Österreich vom 2. September 2025, Steuernummer  49-630/0606, betreffend Zwangsstrafen 2025 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Ludwig Bäumcker` | `Univ.-Prof. Ludwig Bäumcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anneliese Plogmacher` (person)
- `Kamlweg 67, 4843 Wörmansedt, Österreich` (address)
- `SFB Alber & Co Steuerberatungs- gesellschaft` (organisation)
- `Finanzamtes Österreich` (organisation)
- `49-630/0606` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Mag.a Univ.-Prof.in Ada Schaeferlein  in der Beschwerdesache Leroy Sitterle,  Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich, vertreten durch Astoria Stb GmbH & Co KG, Wachaustraße 42/A/3, 3500  Krems an der Donau, über die Beschwerde vom 22. Dezember 2016 gegen die  Berichtigungsbescheide des Finanzamtes Waldviertel vom 22. November 2016 betreffend  Energieabgabenvergütung 2011, 2012 und 2013 nach Durchführung einer mündlichen  Verhandlung am 16.7.2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof.in Ada Schaeferlein` — partial — pred is substring of gold: `Mag.a Univ.-Prof.in Ada Schaeferlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Univ.-Prof.in Ada Schaeferlein`(person)
- `Leroy Sitterle`(person)
- `Fabjan-Hafner-Passage 109, 9065 Radsberg, Österreich`(address)
- `Astoria Stb GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130787.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130787.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Mirha Karahodzic MA über den Antrag  des Hon.-Prof. Thassilo Schoenrock, LLM, Hochscharten 126D, 5122 Dorfen, Österreich, vom 25. Juli 2020 auf Gewährung der Verfahrenshilfe im  Beschwerdeverfahren betreffend seine Beschwerde vom 3. Jänner 2020 gegen den Bescheid  des Finanzamtes Wien 8/16/17 vom 6. Dezember 2019 betreffend Abweisung eines Antrages  auf Aussetzung der Einhebung gemäß § 212a BAO zu Steuernummer 06-88-920/2630  den  Beschluss:    I. Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

**False Positives:**

- `Hon.-Prof. Thassilo Schoenrock` — partial — pred is substring of gold: `Hon.-Prof. Thassilo Schoenrock, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Mirha Karahodzic MA`(person)
- `Hon.-Prof. Thassilo Schoenrock, LLM`(person)
- `Hochscharten 126D, 5122 Dorfen, Österreich`(address)
- `Finanzamtes Wien 8/16/17`(organisation)
- `06-88-920/2630`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache StR Univ.-Prof. Alvin Paulikat, Christine-Touaillon-Straße 1, 4682 Piesing, Österreich, vertreten durch Dr Christian Burghardt, Am Hof  13/18, 1010 Wien, betreffend Beschwerde vom 29. April 2017 gegen die Bescheide des  Finanzamtes Wien 2/20/21/22 vom 8. März 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 und Einkommensteuer (Arbeitnehmerveranlagung) 2015 den  Beschluss:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Alvin Paulikat` — partial — pred is substring of gold: `StR Univ.-Prof. Alvin Paulikat`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Heidemarie Winkler`(person)
- `StR Univ.-Prof. Alvin Paulikat`(person)
- `Christine-Touaillon-Straße 1, 4682 Piesing, Österreich`(address)
- `Dr Christian Burghardt`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133263.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133263.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Laurence Vasylenko  in der Beschwerdesache X, Adresse,  über die Beschwerde vom 12. Juni 2019 gegen den Bescheid des Finanzamtes Graz-Umgebung  vom 13. Mai 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 02-410/2351  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof.in Laurence Vasylenko` — partial — pred is substring of gold: `Dr.in Hon.-Prof.in Laurence Vasylenko`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hon.-Prof.in Laurence Vasylenko`(person)
- `Finanzamtes Graz`(organisation)
- `02-410/2351`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/133428.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133428.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. René Neuendorf  in der Beschwerdesache Kevin Damiani,  Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich, gegen  1. den am 12. Jänner 2016 ausgefertigten Bescheid der belangten Behörde Finanzamt Oststeiermark,  nunmehr Finanzamt Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2013 und  2. den am 1. Februar 2018 ausgefertigten Bescheid der belangten Behörde FA Oststeiermark,  nunmehr FA Oststeiermark, betreffend Körperschaftsteuer für das Jahr 2014  zu Recht erkannt  I. Die angefochtenen Bescheide betreffend Körperschaftsteuer für die Jahre 2013 und 2014  werden abgeändert.

**False Positives:**

- `Univ.-Prof. Ren` — partial — pred is substring of gold: `Univ.-Prof. René Neuendorf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. René Neuendorf`(person)
- `Kevin Damiani`(person)
- `Matthias-Altmann-Straße 3, 8102 Thoneben, Österreich`(address)
- `Finanzamt Oststeiermark`(organisation)
- `Finanzamt Oststeiermark`(organisation)
- `FA Oststeiermark`(organisation)
- `FA Oststeiermark`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/135348.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135348.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Laurin Überschar  in der Beschwerdesache Albert Theiselmann,  Hochmark 31g, 8323 Unterbuch, Österreich, vertreten durch Radike, Hammerl & Partner Steuerberatung GmbH,  Bisamberger Straße 2/1/8, 2100 Korneuburg, betreffend Beschwerde vom 17. Juni 2021 gegen  die Bescheide des Finanzamtes Österreich vom 20. Mai 2021 betreffend Einkommensteuer  2015 und 2016, Steuernummer 15-781/1702, den Beschluss:   I. Die Beschwerde wird gemäß § 256 Abs 3 Bundesabgabenordnung (BAO) als  gegenstandslos erklärt.

**False Positives:**

- `Hon.-Prof. Laurin` — partial — pred is substring of gold: `Hon.-Prof. Laurin Überschar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Laurin Überschar`(person)
- `Albert Theiselmann`(person)
- `Hochmark 31g, 8323 Unterbuch, Österreich`(address)
- `Radike, Hammerl & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `15-781/1702`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/136211.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Karina von Wnuck-Lipinski  in der Beschwerdesache Rosemarie Fortwängler,  Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich, über die Beschwerde vom 4. Oktober 2019 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 26. September 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe (FB) und  Kinderabsetzbetrag (KG) für den Zeitraum Oktober 2017 bis Feber 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Karina` — partial — pred is substring of gold: `Univ.-Prof.in Karina von Wnuck-Lipinski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Karina von Wnuck-Lipinski`(person)
- `Rosemarie Fortwängler`(person)
- `Dr.-Alfred-Besenböck-Straße 11, 8544 Gasselsdorf, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)
- `FA Österreich`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137199.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137199.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hon.-Prof.in Hilde Hassenzahl  in der Beschwerdesache des  Gwendolin Rittmüller, Matzlröth 29, 3970 Reinprechts, Österreich, vertreten durch StB, über die Beschwerde vom 14. Dezember 2020  gegen den Bescheid des FA Bruck Eisenstadt Oberwart  vom 30. November 2020 betreffend Umsatzsteuer 2013 zu  Steuernummer 10-920/5174  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof.in Hilde Hassenzahl` — partial — pred is substring of gold: `Dr.in Hon.-Prof.in Hilde Hassenzahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Hon.-Prof.in Hilde Hassenzahl`(person)
- `Gwendolin Rittmüller`(person)
- `Matzlröth 29, 3970 Reinprechts, Österreich`(address)
- `FA Bruck Eisenstadt Oberwart`(organisation)
- `10-920/5174`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/137857.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137857.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Univ.-Prof. Aron Nierenberger  in der Beschwerdesache DDr.in VetR Rosemarie Srama,  Hollgasse 53, 3244 Riegers, Österreich, gegen die Bescheide des Finanzamtes Österreich vom 10. Februar 2020  betreffend Einkommensteuer 2014 bis 2018 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

**False Positives:**

- `Univ.-Prof. Aron Nierenberger` — partial — pred is substring of gold: `Dr. Univ.-Prof. Aron Nierenberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Univ.-Prof. Aron Nierenberger`(person)
- `DDr.in VetR Rosemarie Srama`(person)
- `Hollgasse 53, 3244 Riegers, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Günter Salahi  in der Beschwerdesache Jaden Knauss,  Dossenweg 3, 4132 Atzesberg, Österreich  über die Beschwerde vom 8. Jänner 2021 gegen den Bescheid des Finanzamtes  Österreich vom 3. Dezember 2020 Rückzahlung gemäß § 239 BAO, Steuernummer  15-678/4603  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Günter Salahi` — partial — pred is substring of gold: `Mag. Hon.-Prof. Günter Salahi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Günter Salahi`(person)
- `Jaden Knauss`(person)
- `Dossenweg 3, 4132 Atzesberg, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `15-678/4603`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/139220.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139220.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Mag.a Univ.-Prof.in Konstanze Lukass  in der Beschwerdesache Selma Katirci,  Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich  vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/Tür  10, 1060 Wien, über die Beschwerde vom 11. November 2019 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 7. Oktober 2019 betreffend Abweisung des  Antrags vom 23. September 2019 auf Gewährung der Familienbeihilfe und des  Kinderabsetzbetrages ohne Vornahme einer Indexierung  gemäß  § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof.in Konstanze Lukass` — partial — pred is substring of gold: `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`(person)
- `Selma Katirci`(person)
- `Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich`(address)
- `Brehm & Sahinol Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/139260.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139260.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin R. in der Verwaltungsstrafsache Univ.-Prof. RgR Werner Burkholdt,  Am Thalbach 7, 6075 Tulfes, Österreich, über die Beschwerde des Beschuldigten vom 21. November 2022 gegen die  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 5. Oktober  2022, GZlen.

**False Positives:**

- `Univ.-Prof. Rg` — partial — pred is substring of gold: `Univ.-Prof. RgR Werner Burkholdt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. RgR Werner Burkholdt`(person)
- `Am Thalbach 7, 6075 Tulfes, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_34`)


dazu wurde der betreffende E-Mail- Verkehr mit dem SMS sowie die Stellungnahme des Univ.-Prof. Dr. F, Klinik Ort2, v. 23.3.2022  vorgelegt.

**False Positives:**

- `Univ.-Prof. Dr` — partial — pred is substring of gold: `Univ.-Prof. Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Dr. F`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/141080.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141080.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Abigail Dausener  in der Beschwerdesache HR OSR Samir Fatthauer,  Viehdorferstraße 27, 4192 Steinschild, Österreich, über die Beschwerde vom 16. Februar 2023 gegen die Bescheide des FA Wien 2/20/21/22  vom 11. Jänner 2023 betreffend Abweisung von Anträgen auf Wiederaufnahme der Verfahren  hinsichtlich Umsatz- und Einkommensteuer 2016 zu Recht erkannt:   I.)

**False Positives:**

- `Hon.-Prof.in Mag` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Abigail Dausener`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Abigail Dausener`(person)
- `HR OSR Samir Fatthauer`(person)
- `Viehdorferstraße 27, 4192 Steinschild, Österreich`(address)
- `FA Wien 2/20/21/22`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/141586.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Jaromir Hendl  in der Beschwerdesache KommR Univ.-Prof. Leander Wehe,  Mahlhofweg 9, 8863 Mitterberg, Österreich, über die Beschwerde vom 23. März 2023 gegen den Bescheid des FA Graz-Stadt  vom 9. März 2023 betreffend Säumniszuschlag 2023 Steuernummer 61-179/3197  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof. Leander Wehe` — partial — pred is substring of gold: `KommR Univ.-Prof. Leander Wehe`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Jaromir Hendl`(person)
- `KommR Univ.-Prof. Leander Wehe`(person)
- `Mahlhofweg 9, 8863 Mitterberg, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `61-179/3197`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/142648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Dora Woditzka  in der Beschwerdesache Bettina Wütherich,  Außerwald 11Y, 6791 Gortipohl, Österreich, über die Beschwerden vom 5. September 2022 gegen die Bescheide des  Finanzamtes Österreich vom 29. August 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 und 2021 Steuernummer 64-696/3269  zu Recht erkannt:   I. Den Beschwerden wird - im Umfang der Beschwerdevorentscheidungen vom 03.02.2023 -  teilweise Folge gegeben.

**False Positives:**

- `Hon.-Prof.in Mag` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Dora Woditzka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Dora Woditzka`(person)
- `Bettina Wütherich`(person)
- `Außerwald 11Y, 6791 Gortipohl, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `64-696/3269`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/147517.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147517.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Priv.-Doz.in Mag.a Melissa Jungvogel  in der Beschwerdesache Marion Scharnetzky,  Heinrich-Finder-Straße 10M, 8160 Regerstätten, Österreich, vertreten durch Ernst & Young Steuerberatungsgesellschaft m.b.H., Wagramer  Straße 19, 1220 Wien, Steuernummer 93-573/8261, über die Beschwerde vom  29. Dezember 2023 gegen die Bescheide des Finanzamtes für Großbetriebe vom 20. Dezember  2022 über die Festsetzung der Stabilitätsabgabe 2017 bis 2020 bzw vom 20. November 2023  über die Festsetzung der Stabilitätsabgabe 2021 und 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Priv` — partial — pred is substring of gold: `Univ.-Prof.in Priv.-Doz.in Mag.a Melissa Jungvogel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Priv.-Doz.in Mag.a Melissa Jungvogel`(person)
- `Marion Scharnetzky`(person)
- `Heinrich-Finder-Straße 10M, 8160 Regerstätten, Österreich`(address)
- `Ernst & Young Steuerberatungsgesellschaft m.b.H.`(organisation)
- `93-573/8261`(tax_number)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/148962.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148962.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Univ.-Prof. Ramon Löther  in der Beschwerdesache Axel Pommeränke,  Zum Hauptplatz 2, 4030 Linz, Österreich, vertreten durch Mag. Niki Zaar, Babenbergerstraße 9/1/8, 1010 Wien,  betreffend die Vorlage der Bescheide des Finanzamtes Österreich vom 9. Oktober 2023 über  die Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2018 und 2019 im Wege  des Vorlageberichtes vom 21. November 2024 zur Steuernummer 14-979/7189  den  Beschluss:  Das Verfahren wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `Univ.-Prof. Ramon Löther` — partial — pred is substring of gold: `Priv.-Doz. Univ.-Prof. Ramon Löther`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Univ.-Prof. Ramon Löther`(person)
- `Axel Pommeränke`(person)
- `Zum Hauptplatz 2, 4030 Linz, Österreich`(address)
- `Mag. Niki Zaar`(person)
- `Finanzamtes Österreich`(organisation)
- `14-979/7189`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Univ.-Prof. Jonas Nußer  in der Beschwerdesache Dr.in Flora Lallemand,  Rochusplatz 224, 9530 Bad Bleiberg, Österreich, über die Beschwerde vom 5. November 2024 gegen die Bescheide des  FA Graz-Stadt  vom 27. August 2024 über den Ablauf einer Aussetzung der Einhebung, über die  Festsetzung von Aussetzungszinsen und vom 1. Oktober 2024 über die Abweisung eines  Aussetzungsantrags, Steuernummer 29-953/8923, zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Univ.-Prof. Jonas Nußer` — partial — pred is substring of gold: `Priv.-Doz. Univ.-Prof. Jonas Nußer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Univ.-Prof. Jonas Nußer`(person)
- `Dr.in Flora Lallemand`(person)
- `Rochusplatz 224, 9530 Bad Bleiberg, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `29-953/8923`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/149812.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149812.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Detlev Bodenmüller  in der Beschwerdesache Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.,  Pux 4, 8753 Paßhammer, Österreich  vertreten durch Mag. Thomas Gell, Am Rosenhof 4, 8063 Eggersdorf bei Graz,  über die Beschwerde vom 28. April 2025 gegen den Bescheid des Finanzamtes Österreich vom  31. März 2025 betreffend Abgabenerhöhung nach § 29 Abs 6 FinStrG zu Steuernummer 72-997/9457  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof.in Eva Gund` — partial — pred is substring of gold: `Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Detlev Bodenmüller`(person)
- `Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.`(person)
- `Pux 4, 8753 Paßhammer, Österreich`(address)
- `Mag. Thomas Gell`(person)
- `Finanzamtes Österreich`(organisation)
- `72-997/9457`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Alessia von Bauer  in der Beschwerdesache  Dimitri Seelos, geb. am 19. November 1987  und Dipl.-Ing. Luna Goedecken, BEd MA, geb. am 12. April 1988  als Erben  des Reneé Keles, verstorben am 3. November 1972  über die Beschwerde vom 15. Dezember 2020  gegen die Bescheide des Finanzamtes Österreich vom 27. November 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2015 bis 2019;

**False Positives:**

- `Univ.-Prof.in Alessia` — partial — pred is substring of gold: `Univ.-Prof.in Alessia von Bauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Alessia von Bauer`(person)
- `Dimitri Seelos`(person)
- `19. November 1987`(date)
- `Dipl.-Ing. Luna Goedecken, BEd MA`(person)
- `12. April 1988`(date)
- `Reneé Keles`(person)
- `3. November 1972`(date)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `Herr_Frau_Name_Context` 🏆

**F1:** 0.111 | **Precision:** 0.730 | **Recall:** 0.060  

**Format:** `regex`  
**Rule ID:** `11c9bc9c`  
**Description:**
Captures person names following 'Herr' or 'Frau' (including 'Herrn'/'Fr.'), ensuring full name capture with titles if present.

**Content:**
```
\b(?:Herr|Herrn|Frau|Fr\.)\s+(?:Hon\.-Prof\.(?:in)?\s+|Dr\.(?:in)?\s+|Priv\.-Doz\.(?:in)?\s+|Mag\.(?:Dr\.)?\s+|Univ\.-Prof\.(?:in)?\s+|Bakk\.(?:\s+rer\.\s+nat\.|\s+rer\.\s+art\.|\s+rer\.\s+techn\.|\s+rer\.\s+jur\.)?\s+|Ing\.(?:\s+Dipl\.)?\s+|Mag\.a\s+|Prof\.in\s+|Prof\.(?:in)?\s+|RA\s+Mag\.(?:in)?\s+|DDr\.(?:in)?\s+|MedR\.(?:in)?\s+|RgR\.(?:in)?\s+|KzlR\.(?:in)?\s+|VetR\.(?:in)?\s+|KommR\.(?:in)?\s+|OMedR\s+|OStR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+LL\.M\.|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.730 | 0.060 | 0.111 | 152 | 111 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 111 | 41 | 1740 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_7`)


Mit Schreiben vom 23.11.2016 legte die Beschwerdeführerin eine Bestätigung ihres  Dienstgebers vor, mit dem folgenden Wortlaut:  "Betreff: Bestätigung: Zur Geltendmachung des Werbungskostenpauschbetrages, gemäß der  Verordnung zu § 17 Abs 6 EStG und Rz 406 LStR 2002, bestätigen wir, dass Frau Hainig  ausschließlich ihre Tätigkeit als Anzeigenverkäuferin (Vertreterin) im Außendienst vom  03.03.2014 bis 31.12.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_10`)


Mit Schreiben vom 28.11.2016 legte die Beschwerdeführerin, eine beim AG GmbH angestellte  Anzeigenverkäuferin, eine Bestätigung ihres Dienstgebers vor, mit dem folgenden Wortlaut:   "Betreff: Bestätigung: Zur Geltendmachung des Werbungskostenpauschbetrages, gemäß der  Verordnung zu § 17 Abs 6 EStG und Rz 406 LStR 2002, bestätigen wir, dass Frau Hainig überwiegend  ihre Tätigkeit, als Anzeigenverkäuferin (Vertreterin) zu 51 % im Außendienst und 49 % im Büro  vom 01.01.2015 bis 31.12.2015 ohne Unterbrechung ausgeübt hat."

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_11`)


Weiters legte die Beschwerdeführerin den Dienstvertrag vom 12.03.2014 vor, mit dem  folgenden entscheidungsrelevanten Inhalt:   "DIENSTVEREINBARUNG abgeschlossen zwischen DG als Dienstgeber und Frau James Hainig,  Adr.**** als Dienstnehmerin.

| Predicted | Gold |
|---|---|
| `James Hainig` | `James Hainig` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_12`)


Frau Hainig  ist ab 3. März 2014 als Anzeigenberaterin für die DG  tätig.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_13`)


Frau Hainig  hat als Dienstort Stadt und Stadt1 und wird zu nachstehenden Bedingungen  ganztags angestellt: Kollektivvertrag: kfm, (nichtjournalistische) Angestellte;

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_19`)


Frau Hainig  verrechnet die ersten drei Monate Spesen und Kilometergeld  nach Bedarf, wobei diese mittels Spesenabrechnung und Kilometerbuch abzurechnen und zu  belegen sind.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_21`)


Mit Frau Hainig  wird vorerst ein  befristetes Dienstverhältnis bis 2. Juni 2014 vereinbart, wobei der erste Monat als Probemonat  gilt. Als Dienstort wird vornehmlich Stadt vereinbart, wobei es dem Dienstgeber vorbehalten ist,  die Dienstnehmerin auch an anderen Betriebsstätten des Unternehmens niederösterreichweit  vorübergehend oder dauernd einzusetzen.

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/128640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128640.1_50`)


Die  am 28.11.2016 vorgelegte Bestätigung der DG (im Folgenden kurz: *** Verlagsges.m.b.H.) hat  folgenden Inhalt: „Zur Geltendmachung des Werbungskostenpauschbetrages, gemäß der  Verordnung § 17 Abs. 6 EStG und Rz 406 LStR 2002, bestätigen wir, dass Frau Hainig überwiegend  ihre Tätigkeit als Anzeigenverkäuferin (Vertreterin) zu 51 % im Außendienst und 49 % im Büro  vom Ol. 01.2015 bis 31.12.2015 ohne Unterbrechung ausgeübt hat."

| Predicted | Gold |
|---|---|
| `Hainig` | `Hainig` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_71`)


…“ Auch ein  Passus im vorgelegten TÜV-Bericht über den Prüftermin am 24.6.2019 steht damit in Einklang:  „Sehr geehrter Herr Volchert  an Ihrem Fahrzeug wurden zum Zeitpunkt der Untersuchung keine  Mängel festgestellt. …“.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_99`)


…Herr Volchert ist hauptberuflich Angestellter der AG in d_Ort_2.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_105`)


Herr Eugen Volchert  ist polizeilich in der Adr, Plz_1  d_Ort_1 gemeldet und deshalb ist sein Fahrzeug auch in d_Ort_1 zugelassen.

| Predicted | Gold |
|---|---|
| `Eugen Volchert` | `Eugen Volchert` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_4`)


Entscheidungsgründe  Beschwerdeführerin (Bf) ist Frau Basil Staerk.

| Predicted | Gold |
|---|---|
| `Basil Staerk` | `Basil Staerk` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_303`)


12 In der Rs Aldewereld hat der Generalanwalt in seinen Schlussanträgen Ausführungen  dahingehend getätigt, dass es sachverhaltsbezogen darauf ankam, dass Herr Aldewereld von  seinem Arbeitgeber sogleich bzw unmittelbar in den Drittstaat entsendet worden war  (Schlussanträge Rn 1 und 12).

| Predicted | Gold |
|---|---|
| `Aldewereld` | `Aldewereld` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_69`)


Herr Frikel ist ebenso Gesellschafter.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Kirsten Renneissen – ist Malermeister und betreibt ein  Einzelunternehmen.

| Predicted | Gold |
|---|---|
| `Kirsten Renneissen` | `Kirsten Renneissen` |

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/131032.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131032.1_84`)


Prima Abo 10,00  Gesamt 431,27  Arbeitsmittel:  1. 1. CD Herr Riese und sein Garten 21,00  5 von 26 Seite 6 von 26

| Predicted | Gold |
|---|---|
| `Riese` | `Riese` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_7`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ des  Finanzamtes Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom 30. Jänner 2017, SpS  16, Strafnummer 007, wurde Herr Albert Sengeisen (in weiterer Folge: Beschuldigter), geboren 1970,  Geschäftsführer, schuldig erkannt, vorsätzlich im Bereich des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf als damaliger Geschäftsführer der Starnberg Beratung GmbH  1.) durch die Abgabe einer unrichtigen Körperschaftsteuererklärung für das Jahr 2012 somit  unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspﬂicht  bewirkt zu haben, dass eine bescheidmäßig festzusetzende Abgaben, nämlich  Körperschaftsteuer 2012 in der Höhe von € 25.076,00 zu gering festgesetzt und dadurch  verkürzt worden sei, sowie  2.) durch die Nichtabfuhr und Nichtmeldung von Kapitalerträgen betreffend das Jahr 2012  binnen einer Woche nach jeweiligem Zuﬂießen, somit unter Verletzung einer  abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspﬂicht und zwar dadurch, indem  Abgaben, die selbst zu berechnen seien, ganz oder teilweise nicht entrichtet (abgeführt)  worden seien, folgende Abgabenverkürzung bewirkt habe, und zwar Kapitalertragsteuer 2012  in der Höhe von € 29.397,54  3) unter Verletzung der Verpﬂichtung zur Abgabe von dem § 21 UStG 1994 entsprechenden  Voranmeldungen eine Verkürzung selbst zu berechnender Abgaben, nämlich  Umsatzsteuervorauszahlungen 2/2014 in der Höhe von € 777,36, 3/2014 in der Höhe von  € 433,00 sowie 6, 12/2014 in der Höhe von € 2.500,00 bewirkt und dies nicht nur für möglich,  sondern für gewiss gehalten zu haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Starnberg Beratung GmbH` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_154`)


Tz. 5 Subunternehmen  G. GmbH; C. GmbH;Burglechner Touristik GmbH & Co KG  Bei - niederschriftlich festgehaltener - Befragung am 31.03.2014 zu den Geschäftskontakten  mit den vermeintlichen Fremdleistungsfirmen gab der Geschäftsführer der Firma M. Bau und  Projekt GmbH, Herr Albert Sengeisen, sinngemäß zu allen drei (3) Fremdleistungsfirmen mehr oder  weniger gleichlautend an, dass er sich der Namen seiner Geschäftspartner, Kontaktpersonen,  Vorarbeiter, Hilfs- und Facharbeiter nicht entsinnen könne, darüber keine Aufzeichnungen  habe und nichts zu deren Identität angeben könne.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `GmbH;Burglechner Touristik GmbH & Co KG` (organisation)
- `M.` (person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_216`)


Trotz der räumlichen Nähe und bequemen Erreichbarkeit will der Geschäftsführer der Firma Starnberg Beratung GmbH  Herr Albert Sengeisen, seinen bedeutsamen Geschäftspartner niemals an dessen  Geschäftsadresse aufgesucht haben.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_268`)


Konkret war seitens der Betriebsprüfung (wie auch schon bei früheren Amtshandlungen) der  Gesellschafter/Geschäftsführer Herr Albert Sengeisen, geboren 1970, als maßgebliche Person in der  Firma Starnberg Beratung GmbH wahrzunehmen.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Starnberg Beratung GmbH` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_269`)


Herr Albert Sengeisen  ist nach eigenen Angaben für das  Geschäftskonto der M. bei der Bank allein zeichnungsberechtigt.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `M.` (person)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_271`)


Barauszahlungen an Fremdleister wurden, so seine Angaben dazu, von ihm abgewickelt. Bei  drei Außenprüfungen ist stets Herr Albert Sengeisen  als Machthaber über die Gesellschaft  aufgetreten.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/131206.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131206.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 28. Mai 2020, Zahl:  MA67/206700146315/2020, wurde Herr Bernhard Habdank (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine Ersatzfreiheitsstrafe von  14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Bernhard Habdank` | `Bernhard Habdank` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_34`)


Mit Lenkerauskunft des rechtsfreundlichen Vertreters der Zulassungsbesitzerin vom  1) 12.05.2020, 2) bis 5) 26.03.2020 und 6) 20.03.2020 wurde mitgeteilt, dass Verantwortlicher  für das Taxi- und Mietwagengewerbe Herr Russbüldt  geb. Herrgeb, AdrHerr, sei.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_35`)


Die Auskunft könne Herr Russbüldt als verantwortlicher Fuhrparkleiter erteilen und es wäre die Auskunft an diesen zu  richten.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_36`)


In weiterer Folge wurde Herr Russbüldt von der Behörde angeschrieben und um Bekanntgabe des  Fahrzeuglenkers ersucht.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_40`)


In dem durch Ihren Rechtsvertreter dagegen erhobenen Einspruch wurde im Wesentlichen  eingewendet, dass Herr Russbüldt  geb. Herrgeb, AdrHerr der einzige und alleinige Verantwortliche  4 von 22 Seite 5 von 22

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_53`)


Dagegen erhoben Sie mit E-Mail vom 2) und 6) 31.08.2020, 3) und 4) 07.09.2020, 5) 04.09.2020  Einspruch und wiederholten, dass Herr Russbüldt der verantwortliche Fuhrparkleiter gewesen sei.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_58`)


Zum Beweis dafür wurde ein  Dokument vom 27.11.2018 vorgelegt, worin die Firmen Firma1 und Firma2 vereinbaren, dass Herr Russbüldt als Fuhrparkleiter für beide angeführten Firmen ab dem 01.12.2018 beauftragt wird.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_71`)


Aufgrund der Aktenlage ist daher davon auszugehen, dass Herr Russbüldt nicht verantwortlicher  Beauftragter gemäß § 9 Abs. 2 VStG ist.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_81`)


Aufgrund des Umstandes, dass trotz mehrfacher Aufforderung durch die Behörde bis dato  weder in diesem Verfahren noch in anderen bei der Behörde gegen Sie anhängigen Verfahren  ein Dokument vorgelegt wurde, das die nachweisliche Zustimmung des Herrn Angelstein zur  Bestellung als verantwortlicher Beauftragter gemäß § 9 Abs. 2 VtG beurkundet, geht die  erkennende Behörde davon aus, dass eine derartige Zustimmung nicht vorliegt und deswegen  als erwiesen anzusehen ist, dass Herr Russbüldt nicht verantwortlicher Beauftragter gemäß § 9 Abs.  2 VStG ist.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Missed by this rule (FN):**

- `Angelstein` (person)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_105`)


Darin hat der Beschwerdeführer dargelegt, dass der  Beschwerdeführer die verlangte Auskunft nicht erteilen kann, sondern Herr Russbüldt  geb. Herrgeb,  AdrHerr, Verantwortlicher gemäß § 9 VStG.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_110`)


Verantwortlich gemäß § 9 VStG für das Taxi- und  Mietwagengewerbe ist einzig und allein Herr Russbüldt  geb. Herrgeb, AdrHerr.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_112`)


Dieser Aufforderung ist Herr Russbüldt nicht nachgekommen und musste  gegen ihn Anzeige erstattet werden.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_117`)


Tatsächlich ist Herr Russbüldt mit Bestellungsurkunde vom 27.11.2018 zum Fuhrparkleiter der  Firma1 und der hier nicht in Rede stehenden Firma2 bestellt worden.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_157`)


Mit Schreiben vom 04.06.2020 erhob der rechtsfreundliche Vertreter von Herrn Angelstein einen  Sammeleinspruch gegen die Strafverfügungen 2) bis 6) und weitere, nicht gegenständliche  Strafverfügungen und gab dieser bekannt, dass Herr Russbüldt zu den angeführten Kennzeichen zu  relevierten Tatzeitpunkten nachweislich nicht verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Missed by this rule (FN):**

- `Angelstein` (person)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_169`)


Verantwortlich gemäß § 9 VStG für das Taxi- und  Mietwagengewerbe ist einzig und allein Herr Russbüldt  geb. Herrgeb, AdrHerr.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_171`)


Dieser Aufforderung ist Herr Russbüldt nicht nachgekommen und musste gegen ihn Anzeige erstattet werden.

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_238`)


2) bis 6) vom 14.07.2020, wonach Herr Russbüldt als Fuhrparkleiter für die Dr.in Ing. Viktoria Weigart  für die Fahrzeuge verantwortlich gewesen sei, wird Folgendes festgestellt:  Gemäß § 9 Abs. 4 VStG kann verantwortlicher Beauftragter nur eine Person sein, die (unter  anderem) ihrer Bestellung nachweislich zugestimmt hat und der für den ihrer Verantwortung  18 von 22 Seite 19 von 22

| Predicted | Gold |
|---|---|
| `Russbüldt` | `Russbüldt` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/133064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133064.1_3`)


Begründung  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom  29. Dezember 2020, GZ. MA6/2019, wurde Herr Aron Pommeränke (in weiterer Folge: Beschuldigter)  als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H., nunmehr Logzor-Event GmbH in Liquidation) für schuldig befunden,   1. er habe als handelsrechtlicher Geschäftsführer der MittelMarine Planung GmbH (vormals B Gesellschaft m.b.H.,  nunmehr Logzor-Event GmbH in Liquidation) im Juni 2018 vor der Liegenschaft in Wien, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, eine Baustofflagerung im  Ausmaß von 115 m2 vorgenommen gehabt, wobei er hiefür bis zum 11. Oktober 2018 weder  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `Aron Pommeränke` | `Aron Pommeränke` |

**Missed by this rule (FN):**

- `Magistrats der Stadt Wien, Magistratsabteilung 6` (organisation)
- `MittelMarine Planung GmbH` (organisation)
- `Logzor-Event GmbH` (organisation)
- `MittelMarine Planung GmbH` (organisation)
- `Logzor-Event GmbH` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_21`)


Da der Gutachter Herr Karina Burfeindt selber sagte, wenn wir auch einen ärztlichen Befund haben, ändert es die ganzen Prozente,  und das haben wir jetzt.

| Predicted | Gold |
|---|---|
| `Karina Burfeindt` | `Karina Burfeindt` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_24`)


Frau Baues ist die Liquidatorin.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_45`)


Zu den vereinbarten Einkaufskonditionen gab Herr Inn Trikraftglanz  zu Protokoll, dass es eine Vereinbarung  gegeben habe, dass die Fa. e. um € 1,00 je 100 Liter billiger anbieten müsse als die Fa. „F. KG“,  was auch regelmäßig geschah.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_228`)


Unabhängig davon ist zu der mehrfach angeführten „Belehrung" festzuhalten, dass diese unter  Beisein der steuerlichen Vertreterin -Frau Borisowa- erfolgte und sich im Wesentlichen darauf  beschränkte, dass man Herrn Inn Trikraftglanz mitteilte, dass er „besser aufpassen muss".

| Predicted | Gold |
|---|---|
| `Borisowa` | `Borisowa` |

**Missed by this rule (FN):**

- `Inn Trikraftglanz` (person)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_244`)


6. Zum Vorwurf Verwechselung K.  Die diesbezüglichen Ausführungen sind sehr verkürzt: Konkret hat Herr Inn Trikraftglanz ausgesagt, dass er  nur im Erstgespräch über die Funktion von Herrn K. geirrt hat.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_405`)


Frau Baues als Vertreterin der Beschwerdeführerin gibt bekannt, dass die Diesellieferungen 2 bis 3  Mal pro Woche stattgefunden haben.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_415`)


Die Anfrage beim Finanzamt deute vielmehr darauf hin,  dass Herr Inn Trikraftglanz  selbst Zweifel an der Seriosität der in Rede stehenden Lieferanten gehabt habe  und möglicherweise auch ein Naheverhältnis.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_609`)


Der Vollständigkeit halber wird abschließend Folgendes festgehalten:  Beweisanträge auf Einvernahme von Frau Baues sowie Frau AB.:  Betreffend dieser Anträge ist festzuhalten, dass Frau Baues als Vertreterin der Bf. und Frau Borisowa als  ehemalige Steuerberaterin an der Verhandlung teilgenommen haben, eine Einvernahme als  Zeuginnen damit erübrigt hat.

| Predicted | Gold |
|---|---|
| `Baues` | `Baues` |
| `Baues` | `Baues` |
| `Borisowa` | `Borisowa` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_6`)


Entscheidungsgründe  I. Verfahrensgang  1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Beschwerdeführerin (kurz Bf) ist eine GmbH, deren alleinige Gesellschafterin Frau Schneppensiefen ist.

| Predicted | Gold |
|---|---|
| `Schneppensiefen` | `Schneppensiefen` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/135722.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135722.1_4`)


Mit Schreiben vom 24. Mai 2012 informierte das Finanzamt Salzburg-Land das Finanzamt  9/18/19 Klosterneuburg darüber, dass Herr Alois Kleynsteuber (im Folgenden kurz Beschwerdeführerin  = Bf.) € 102.094,62 nachzuversteuern habe.

| Predicted | Gold |
|---|---|
| `Alois Kleynsteuber` | `Alois Kleynsteuber` |

**Missed by this rule (FN):**

- `Finanzamt Salzburg-Land` (organisation)
- `Finanzamt` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_3`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg  als Finanzstrafbehörde vom 11. März 2019, SpS, Strafnummer 001, Geschäftszahl FV, wurde  Herr Harald Hilderink, geboren am 1965, schuldig erkannt, er habe als der für die  abgabenrechtlichen Belange verantwortliche Geschäftsführer und Entscheidungsträger der  „ARGE" (kurz: ARGE) vorsätzlich Abgaben, die selbst zu berechnen sind, nicht spätestens am  fünften Tag nach Fälligkeit entrichtet oder abgeführt und auch der zuständigen  Abgabenbehörde bis zu diesem Zeitpunkt nicht die Höhe des geschuldeten Betrages  bekanntgegeben, und zwar hinsichtlich   1 von 14 Seite 2 von 14

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_20`)


In einem weiteren Schriftverkehr mit der  steuerlichen Vertretung wurde durch diese bekannt gegeben, dass der zuständige  Geschäftsführer, Herr Harald Hilderink, die Abgabenforderungen aus Umsatzsteuern in der 45.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_32`)


In dem eingeleiteten Finanzstrafverfahren wurde Herr Harald Hilderink  jedoch beschuldigt,  vorsätzlich die Abgabe und Zahlung der Umsatzsteuervoranmeldungen unterlassen zu haben  und zu einer Geldstrafe von EUR 10.000,00 verurteilt. Gegen diese Straffestsetzung richtet sich  die vorliegende Beschwerde und geben wir als Begründung an:   Die ARGE wurde von einem Steuerberater vertreten, der mit der Abgabe der  Umsatzsteuervoranmeldungen beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_33`)


Herr Harald Hilderink  konnte daher davon  ausgehen, dass alle Meldungen ordnungsgemäß und fristgerecht abgegeben werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_34`)


 Herr Harald Hilderink  ist zwar handelsrechtlicher Geschäftsführer österreichischer  Kapitalgesellschaften, jedoch besteht ein Unterschied zwischen einer GmbH und einer  ARGE, weshalb er sich steuerlichen Rat durch eine Steuerberatungsgesellschaft suchte  und diese mit der Buchführung beauftragte.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_38`)


Auf die Einhaltung von Fristen war Herr  Harald Hilderink  daher auf seine steuerliche Vertretung angewiesen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_40`)


Herr Harald Hilderink  ist nicht alleine dafür  verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 58** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_42`)


 Während des aufrechten Finanzstrafverfahrens und der abgabenbehördlichen  Erhebung gem. § 143 BAO wurde Herr Harald Hilderink  von der steuerlichen Vertretung  darauf hingewiesen, dass die Prüfung und das Finanzstrafverfahren erledigt seien,  weshalb Herr Harald Hilderink  auch keine Stellungnahme zu dem Finanzstrafverfahren abgab.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |
| `Harald Hilderink` | `Harald Hilderink` |

**Example 59** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_53`)


Da Herr Harald Hilderink  mit seinen Unternehmen an öffentlichen Ausschreibungen teilnimmt ist es  für ihn wichtig, finanzstrafrechtlich unbescholten zu sein.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 60** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_78`)


In einer E-Mail der steuerlichen Vertretung vom 7. November 2018 an Herrn R. vom  zuständigen BV-Team der Abgabenbehörde wurde als verantwortlicher Geschäftsführer der  ARGE Herr Harald Hilderink  genannt.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 61** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_79`)


Herr Harald Hilderink  ist außerdem der Geschäftsführer der P-GmbH, welche im Tatzeitraum  Vertreter nach § 81 BAO der ARGE ist.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 62** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_81`)


Herr Harald Hilderink  ist verantwortlicher Geschäftsführer der ARGE.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 63** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_89`)


Zum Beschwerdevorbringen, „Herr Harald Hilderink  war auf die Einhaltung von Fristen auf seine  steuerliche Vertretung angewiesen, die mit der Abgabe der Umsatzsteuervoranmeldungen  beauftragt war.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 64** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_90`)


Herr Sahin konnte daher davon ausgehen, dass alle Meldungen  ordnungsgemäß und fristgerecht abgegeben werden bzw. die verspätete Abgabe der  Umsatzsteuervoranmeldungen war nicht vorsätzlich!

| Predicted | Gold |
|---|---|
| `Sahin` | `Sahin` |

**Example 65** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_95`)


Herr Harald Hilderink  ist nicht alleine dafür verantwortlich, dass alle Abgaben fristgerecht gezahlt werden.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 66** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 3. September 2021, Zahl:  MA67/216700658355/2021, wurde Herr Roland Rößle (in weiterer Folge: Beschwerdeführer) der  Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung für schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Roland Rößle` | `Roland Rößle` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_3`)


Begründung  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 25. Februar  2022, Zahl MA67/Zahl/2021, wurde über Frau Waiser nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_4`)


Im Nachhang zu dieser Strafverfügung erließ der Magistrat der Stadt Wien (MA 6 – BA 32) an Frau Waiser die beschwerdegegenständliche, mit 18.05.2022 datierte  Vollstreckungsverfügung, Zahl MA67/Zahl/2021, mit welcher zur Einbringung des zu zahlenden  Gesamtbetrages in Höhe von € 65,00 (inkl Mahngebühr iHv € 5,00) gemäß § 3 VVG und § 10  VVG die Zwangsvollstreckung verfügt wurde.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 69** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_11`)


Unter Bezugnahme auf obige Ausführungen ist festzuhalten, dass Frau Waiser die  exklusive (einzige) Adressatin der Vollstreckungsverfügung vom 18. Mai 2022 ist, die hier aber  von jemandem anderen bekämpft wird.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Example 70** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_15`)


Im vorliegenden Fall hat jedoch nicht die Adressatin der verfahrensgegenständlichen  Vollstreckungsverfügung, nämlich Frau Waiser  sondern FirmaBfInhaberLautFirmenbuch,  Firmenbuchnummer FN im eigenen Namen Beschwerde erhoben.

| Predicted | Gold |
|---|---|
| `Waiser` | `Waiser` |

**Example 71** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_26`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung – direkt oder indirekt – von Arbeitnehmern auf  Grundlage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 72** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_26`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt - von Arbeitnehmern auf  Grundlage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 73** (doc_id: `deanon_BFG_20260814_VALIDATE/138507.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138507.1_7`)


Im Zuge der Überprüfung des Familienbeihilfenanspruches der Frau Verena Piechura (=  Beschwerdeführerin, Bf) im Dezember 2021 ua. für den Sohn B, geb. 03/1999, wurden  Studienbestätigungen der Universität Ort1 vorgelegt, wonach der Sohn B im Wintersemester  (WS) 2021/2022 im Bachelorstudium Lehramt für Bewegung und Sport sowie Französisch (KZ  UC 198 452 459;

| Predicted | Gold |
|---|---|
| `Verena Piechura` | `Verena Piechura` |

**Example 74** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_37`)


Im  Allgemeinen gibt Frau Reifgerste an, dass sich ihre Tochter überwiegend „falsch“ fühle und in sozialen  Situationen sich sehr verunsichert fühle, da sie nicht wisse wie sie sich verhalten solle.

| Predicted | Gold |
|---|---|
| `Reifgerste` | `Reifgerste` |

**Example 75** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung des Magistrates der Stadt Wien vom 4. Oktober 2022, Zahl  MA67/Zahl/2022, wurde Herr Annette Preußing (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  in der Höhe von € 60,00 verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Annette Preußing` | `Annette Preußing` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_VALIDATE/140714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140714.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Dagobert Duewel (= Beschwerdeführerin, Bf) hat mit Anträgen Beih100 und Beih3 vom  11.8.2022 für den Enkelsohn A, geb. 05/2004, ab Juni 2022 die Familienbeihilfe (FB) und den  FB-Erhöhungsbetrag wegen erheblicher Behinderung, konkret "Autismus-Spektrum-Störung  Asperger-Syndrom", beantragt.

| Predicted | Gold |
|---|---|
| `Dagobert Duewel` | `Dagobert Duewel` |

**Example 77** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_165`)


In der Bestätigung der AG1 (Adr2) wurde durch den Geschäftsführer GF, bestätigt, dass Herr Luethgarth (geb. am Geb.) die Funktion eines Geschäftsführers in diesem Unternehmen innegehabt  habe.

| Predicted | Gold |
|---|---|
| `Luethgarth` | `Luethgarth` |

**Example 78** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_167`)


In der Bestätigung der AG2 (Adr3 / FN 1234) wurde durch den Geschäftsführer Gf2, bestätigt,  dass Herr Luethgarth (geb. am Geb.) als Geschäftsführer der AG2 tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `Luethgarth` | `Luethgarth` |

**Example 79** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Frau Olivia Trienes (= Beschwerdeführerin, Bf) bezieht für den Sohn A, geb. 06/1997, laufend  die Familienbeihilfe (FB).

| Predicted | Gold |
|---|---|
| `Olivia Trienes` | `Olivia Trienes` |

**Example 80** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_7`)


Nach erfolgter Lenkererhebung vom 13. März 2023 teilte die Bezirkshauptmannschaft Ort mit  Schreiben vom 16. März 2023 der belangten Behörde aufgrund einer Anfrage mit, dass der  Parkausweis mit der Nummer Nr1 (Nr2) am 22. März 2002 von der BH Ort an Herrn Isenmann  geb.  Herrgeb, AdrHerr, ausgegeben worden sei und dass Herr Ballschmieder laut ZMR mit Datum verstorben  sei.

| Predicted | Gold |
|---|---|
| `Ballschmieder` | `Ballschmieder` |

**Missed by this rule (FN):**

- `Isenmann` (person)

**Example 81** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_45`)


Der Parkausweis Nr. Nr1 (Nr2) wurde am 22. März 2002 von der Bezirkshauptmannschaft Ort  an Herrn Isenmann  geb. Herrgeb, AdrHerr, ausgestellt.Herr Ballschmieder ist laut ZMR mit Datum  verstorben.

| Predicted | Gold |
|---|---|
| `Ballschmieder` | `Ballschmieder` |

**Missed by this rule (FN):**

- `Isenmann` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_65`)


Gleiches trifft auf die Ehegattin des Bf. zu.  Erkrankung der Ehegattin und des Bf.:  Im Vorlageantrag wurde erstmalig vorgebracht, ein Umzug nach Österreich sei nicht möglich,  weil seine Frau Krebs hat;

**False Positives:**

- `Krebs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_10`)


Ein weiterer ärztlicher Befundbericht von Fr. Dr. **** und Herrn Dr. **** lagen ebenfalls dem  Antrag bei.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/133821.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133821.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Zoltan Dabrowski  in der Beschwerdesache der Frau  OMedR Prof. Hartmut Szardemings, Reuttener Straße 33u, 5090 Faistau, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  15. März 2019 gegen den Bescheid des Finanzamtes Graz-Stadt vom 22. Jänner 2019  betreffend Einkommensteuer 2017 zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `OMedR Prof. Hartmut Szardemings`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Zoltan Dabrowski`(person)
- `OMedR Prof. Hartmut Szardemings`(person)
- `Reuttener Straße 33u, 5090 Faistau, Österreich`(address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuer- beratungsgesellschaft`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_77`)


Alleinige Gesellschafter- Geschäftsführerin ist Frau Schneppensiefen   Gegenstand des Unternehmens ist laut Gesellschaftsvertrag vom 30.12.2003 „die Vermietung,  Verpachtung und Beteiligung, sowie der An- und Verkauf von Liegenschaften im Rahmen der  Verwaltung eigenen Vermögens und die Verwaltung eigenen Vermögens“.

**False Positives:**

- `Schneppensiefen   Gegenstand` — partial — gold is substring of pred: `Schneppensiefen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Schneppensiefen`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_123`)


Im rechtzeitigen Vorlageantrag brachte der steuerliche Vertreter der Bf. vor, dass Frau bfb und  Herr BfA die betreffende Liegenschaft und folglich die Einkunftsquelle im Jahr 1997 aufgrund  einer Erbschaft (Einantwortungsbeschluss vom26.6.1997) unentgeltlich erworben hätten.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_137`)


Herr BfA sei damals persönlich  beim damals zuständigen Finanzamt Wien 6/7/15 vorstellig geworden.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Wien 6/7/15`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_140`)


Tatsache sei, dass Herr  BfA seinerzeit persönlich bei der damals zuständigen Abgabenbehörde die AfA-

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_304`)


Der Anteil an den Einkünften für Herrn BfA beträgt: Euro 10.081,85  Der Anteil an den Einkünften für Frau BfB beträgt: Euro 10.081,84

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_30`)


Am 18.12.2002 kam die Bf. weiters mit dem (vormaligen) Landesgendarmeriekommando für  Kärnten dahingehend überein, dass Frau MartinmüllerA den in der strittigen Liegenschaft befindlichen  Gendarmerieposten - infolge Pensionierung der dort tätigen Raumpflegerin - mit Wirksamkeit  zum 1.1.2003 mitreinigen wird (vgl. Präambel zum Vertrag vom 18.12.2002).

**False Positives:**

- `Martinmüller` — partial — pred is substring of gold: `MartinmüllerA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MartinmüllerA`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_52`)


Wie eine Einsicht in den im Rahmen der Betriebsprüfung vorgelegten (undatierten)  „Dienstvertrag-Änderung“ zeigt, stand Frau MartinmüllerA seit Jänner 1993 in einem aufrechten  Vertragsverhältnis zur Bf..

**False Positives:**

- `Martinmüller` — partial — pred is substring of gold: `MartinmüllerA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MartinmüllerA`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_55`)


Die in concreto erfolgten Verrechnungen bzw. die buchhalterische Erfassung der  verfahrensgegenständlichen Leistungen basieren auf den Angaben der Bf. im Zuge der  mündlichen Verhandlung (vgl. Ausführungen Herr GundelachB, VH-Protokoll S. 9f).

**False Positives:**

- `Gundelach` — partial — pred is substring of gold: `GundelachB`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `GundelachB`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_31`)


4) Geldannahme Bestätigung vom 23. Juli 2021, in der Herr Herr2 den Erhalt von € 10.000,00  für die Übernahme von fünf Autos vom Bf. bestätigt.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_3`)


Begründung  1.a. Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 11. März  2021, Zahl: MA67/216700111216/2021, wurde Frau MedR Uwe Vaculik (in weiterer Folge:   Beschwerdeführerin) der Begehung einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener  Parkometerabgabeverordnung 2006 für schuldig erkannt und über sie nach § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in der Höhe von € 60,00 verhängt und für den Fall ihrer   Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Med` — partial — pred is substring of gold: `MedR Uwe Vaculik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `MedR Uwe Vaculik`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_8`)


FirmenwortlautBf  xStrasse  Ort  ATU UID-Nr  Herr Herr1  Herr Herr2.“

**False Positives:**

- `Herr` — no gold match — likely missing annotation
- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_84`)


Nachdem im § 37 Abs. 5 Z 3 EStG keine zeitliche Frist normiert ist, stellt  die ungeplante Wideraufnahme der gerichtlichen Sachverständigentätigkeit keine schädliche  Erwerbstätigkeit dar.“   < Schreiben BG A vom 23.7.2019:  „Herr Beschwerdeführer hat die Austragung aus der Liste der Sachverständigen mit 30.6.2016  entsprechend an die Präsidentin des Landesgerichtes W kommuniziert.

**False Positives:**

- `Beschwerdeführer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichtes`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_64`)


Beweis: Person4, als Zeuge, Person3  Folgender Mailverkehr wurde in der mündlichen Verhandlung seitens der Bf. vorgelegt, im  Wesentlichen:  STB2 an BMF1 (BMF Abteilung III/12), gesendet 5. Oktober 2021:  S.g. Herr Ministerialrat, wie schon kürzlich tel.

**False Positives:**

- `Ministerialrat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BMF`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_20`)


Im Einspruch wendeten Sie im Wesentlichen ein, nicht mehr für diese Firma zu arbeiten, sowie,  dass der Halter des Fahrzeuges, Herr Herr3, den Plan, welche Person das Fahrzeug gefahren  hat, besitzen würde.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_25`)


Ebenso könne Herr Herr2, der die  Mitarbeitereinsatzplanung mit Herrn Herr3 vorbereitet bezeugen, dass Ihnen das Fahrzeug als  Verantwortlicher übergeben wurde.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `M_Anonymized` 🏆

**F1:** 0.063 | **Precision:** 0.604 | **Recall:** 0.033  

**Format:** `regex`  
**Rule ID:** `3f943e7c`  
**Description:**
Captures the specific anonymized initial 'M.' as a person, ensuring it is followed by a period and space or end of string to distinguish from other uses.

**Content:**
```
\bM\.(?=\s|$|,|\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.604 | 0.033 | 0.063 | 101 | 61 | 40 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 61 | 40 | 1790 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_728`)


M. Wagner,  Welche Aufzeichnungen sind zu führen? in Endfellner/Puchinger, BAO, 41), weil diese nämlich  stets (nach § 184 Abs.1) voraussetzt, dass die Abgabenbemessungsgrundlagen nicht ermittelt  oder berechnet werden können, was im Hinblick auf die Vorlage der Ausdrucke (statt der  Datenträger) nicht der Fall ist.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_154`)


Tz. 5 Subunternehmen  G. GmbH; C. GmbH;Burglechner Touristik GmbH & Co KG  Bei - niederschriftlich festgehaltener - Befragung am 31.03.2014 zu den Geschäftskontakten  mit den vermeintlichen Fremdleistungsfirmen gab der Geschäftsführer der Firma M. Bau und  Projekt GmbH, Herr Albert Sengeisen, sinngemäß zu allen drei (3) Fremdleistungsfirmen mehr oder  weniger gleichlautend an, dass er sich der Namen seiner Geschäftspartner, Kontaktpersonen,  Vorarbeiter, Hilfs- und Facharbeiter nicht entsinnen könne, darüber keine Aufzeichnungen  habe und nichts zu deren Identität angeben könne.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `GmbH;Burglechner Touristik GmbH & Co KG` (organisation)
- `Albert Sengeisen` (person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_166`)


Unterschriften auf den von der Firma M. vorgelegten Kassa-Eingang-Belegen, die überdies nur  in Schwarz-Weiß-Kopien vorgelegt wurden.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_215`)


Firmensitz Das ist vom damaligen Standort der Firma M. und Projekte GmbH 2,2 Kilometer  entfernt, bzw. mit der U-Bahn zwei (2) Stationen oder 21 Gehminuten zu Fuß.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_236`)


Es ist angesichts des vermeintlichen Umfangs der gegenseitigen Geschäftsbeziehungen und der  Nähe der beiderseitigen Geschäftssitze absolut unglaubwürdig, wenn der Geschäftsführer der  M. behauptet, er hätte kein einziges Mal die N. an ihrer Geschäftsanschrift aufgesucht.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_261`)


Konkret ist anzunehmen, dass auf den Baustellen der Bauträger über die Firma M. vermittelte  Arbeiter zum Einsatz kamen, deren Löhne zum Nettowert kalkuliert wurde.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_269`)


Herr Albert Sengeisen  ist nach eigenen Angaben für das  Geschäftskonto der M. bei der Bank allein zeichnungsberechtigt.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Albert Sengeisen` (person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_289`)


Es besteht hierzu der  sich allgemein aufdrängende Verdacht, dass die Früchte aus mannigfaltigen Malversationen  (Scheinrechnungen, Organisation von Schwarzarbeit) nicht bloß den Betreibern der M. frommt,  sondern systematisch an übergelagerte Nutznießer durchgereicht werden (Durchreichung in  einem mehrstufigen Betrugsmodell).

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_298`)


Wobei auch 3 dieses Versäumnis spätere Gestaltungsmöglichkeiten weit offen hält.  Infolge einer amtswegigen Umsatzsteuerfestsetzung für den Zeitraum 01-08/2013 musste die  M. zur Beschwerdeführung für diesen Zeitraum eine Buchhaltung anfertigen lassen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_299`)


Offenbar  lagen der Geschäftsführung zu diesem Zeitpunkt in 12/2013 für 01-04/2013 keine  verwertbaren "Fremdleistungsrechnungen" vor, was nun die Folge hatte, dass die Firma M. in  diesem Zeitraum 01-04/2013 fakturierte Bauleistungen in Höhe von € 90.570,80 auswies, ohne  über Eigen- oder Fremdkapazitäten zur Ausführung dieser Arbeiten zu verfügen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_302`)


Auch bei der Firma M. wurden schließlich keine  entsprechenden Eingangsrechnungen vorgefunden.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_308`)


Die andere Person wiederum ist dem Kreis jener Unternehmen zuzuordnen, welche entweder  von unlauteren Machenschaften auf Ebene der Subfirma M. profitiert, oder zumindest aus  Eigennutz das Auge davor verschließt.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_330`)


Darin hat die  Firma M. in diesem Zeitraum 01-04/2013 fakturierte Bauleistungen in Höhe von € 90.570,80  ausgewiesen, ohne über Eigen- oder Fremdkapazitäten zur Ausführung dieser Arbeiten zu  23 von 29 Seite 24 von 29

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_334`)


Die M. hatte ab März 2012 keine eigenen Arbeiter, bediente sich daher Subfirmen, die  beauftragt wurden, für die Aufträge entsprechende Leistungen mit entsprechendem Personal  zu erbringen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131608.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Achmed Karolzak  in der Beschwerdesache Lilia Löffelmann,  Karl Heinschild-Weg 29, 4980 Hübing, Österreich, vertreten durch M. Thaler Steuerberatung Kufstein GmbH, Prof. Sinwel-Weg 4,  6330 Kufstein, über die Beschwerde vom 5. September 2018 gegen die Bescheide des  Finanzamtes Kufstein Schwaz vom 8. August 2018 betreffend Wiederaufnahme der Verfahren  hinsichtlich Einkommensteuer für die Jahre 2012 bis 2015 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Achmed Karolzak` (person)
- `Lilia Löffelmann` (person)
- `Karl Heinschild-Weg 29, 4980 Hübing, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_22`)


In ihrer Sachverhaltswürdigung kommt der angefochtene Bescheid zum Ergebnis, die erste  Lieferung in der Reihe sei die „bewegte“, weil der erste (M. GmbH) oder der zweite  Unternehmer (Bf.) in der Reihe den Transport durchführt oder beauftragt.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_24`)


Sie habe bei  den oa. Geschäftsvorgängen unabhängig von der tatsächlichen Warenbewegung und  unabhängig vom Ort der Beendigung der Warenbewegung (Bestimmungsland) ihrem  Lieferanten (M. GmbH) jeweils die österreichische UID-Nummer bekanntgegeben.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_143`)


Für die in der  Ergänzung vom 28.9.2016 zum Vorlageantrag vom 1.6.2016 aufgestellten nicht näher  substantiierten Prozessbehauptungen des Vorliegens einer „gebrochenen Lieferungen“ in  einem von der Bf. angemieteten Lager bei der Firma M. finden sich keine ausreichenden  Hinweise auf bezahlte Lagermieten.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132670.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132670.1_148`)


Die M. sei verantwortlich für die Lagerung und Inventar aller Rohmaterialien  und Produkte, die im Eigentum der Bf. seien.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_436`)


Der Vorhaltsbeantwortung waren fünf Anlagen angeschlossen:  Anlage 1:  1/1: Letter of confirmation vom 26.8.2020  1/2: Bestätigungsschreiben (beglaubigte Übersetzung aus dem Englischen vom 17.9.2020) vom  26.8.2020  1/3: Letter of confirmation vom 26.8.2020  1/4: CMR 80722597 an ZL vom 13.6.2016  Anlage 2:  2/1: Letter of confirmation vom 26.8.2020  2/2: CMR 80265439 an F.B. vom 17.3.2015  2/3: CMR 80828354 an F.B. vom 27.9.2015  2/4: CMR 80914347 an R.U. vom 5.12.2016  2/5: CMR 80914350 an R.U. vom 2.12.2016  Anlage 3:  3/1: This Document has been issud on the request of vom 27.8.2020  3/2: Dieses Dokument wird ausgestellt auf Ansuchen vom 27.8.2020 (Übersetzung vom  29.9.2020)  3/3: This Document has been issud on the request of vom 27.8.2020  3/4: Invoice der Bf. an N. vom 12.10.15  3/5: Invoice der Bf. an N. vom 26.9.16  3/6: CMR an CL vom 9.10.2015  3/7: Purchase Order vom 1.10.2015 (N. an CL)  3/8: Purchase Order vom 20.9.2016 (N. an CL)  3/9: CMR JBL an CL vom 26.9.2016  3/10: CMR 80409868 an K. (Polska) vom 7.8.2015  3/11: CMR 80423569 an K. (Polska) vom 26.8.2015  3/12: CMR 80236735 an Ko. (N.L.) vom 10.2.2015  3/13: CMR 80392557 an Ko. (Polska) vom 21.7.2015  3/14: CMR 80388656 an M. (Polska) vom 24.7.2015  3/15: CMR 80320800 an M. (Polska) vom 8.5.2015  3/16: CMR 80257940 an S. (Polska) vom 6.3.2015  3/17: CMR 80323928 an S. (Polska) vom 18.5.2015  3/18: CMR 80265443 an S. (Polska) vom 18.3.2015  3/19: CMR 80423566 an S. (Polska) vom 24.8.2015  3/20: CMR 80673863 an Ko. (Polska) vom 22.4.2016  29 von 59 Seite 30 von 59

| Predicted | Gold |
|---|---|
| `M.` | `M.` |
| `M.` | `M.` |

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_43`)


Auch habe ihm M. die Gesprächsinhalte nicht übersetzt oder ihn um eine Entscheidung gefragt.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_44`)


bf. habe ihn anfangs für eine Hilfskraft oder den Chauffeur von M. gehalten.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_203`)


Oiltrade GmbH (Beilage 1)  o Auszug aus dem Gewerberegister (18.11.2013)  o Firmenbuchauszug (27.5.2013)  O Kopien der übergebenen Visitenkarten Hr. K., Hr. M., Hr. X.  O Passkopie Hr. K.  O 1 Bild eines Geschäftsmeetings mit Hr. bf. und Hr. K.  O 3 Bilder betreffend den Geschäftssitz der Gesellschaft (Tafel neben Klingel, Tafel  Eingangstüre)  O Bescheid über die Erteilung der UlD -Nummer (31.7.2013)  O Bestätigung über die Gültigkeit der UID-Nummer (15.04.2014)  o Bescheid über die Registrierung als Empfänger für Mineralöl  O Rahmenvertrag über die Lieferung von Erdöl (3.3.2014)  D. GmbH (Beilage 2)  o Auszug Gewerberegister (4.9.2013)  o Firmenbuchauszug (4.9.2013)  O Angebot vom 26.9.2013  o Passkopie Hr. d.  O Rückstandsbescheinigungen Finanzamt (31 .10.2013,25.11 .2013, 6.12.2013)  Protokoll über Beschuldigteneinvernahme von bf. vom 1.3.2017 (Beilage 3)  2.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_274`)


Es ist dann jemand von der Firma, nämlich ein Herr M. gemeinsam mit Herrn K. zu mir  gekommen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_275`)


Frage: Haben Sie nachgefragt bei Herrn M., wer die zweite anwesende Person (gemeint ist der  kein Wort deutsch sprechende Herr K., der Geschäftsführer der e.) ist?

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_277`)


Antwort: Herr M. hat sich bei mir als Geschäftsführer vorgestellt. Herr K. sollte der „Big Boss"  sein.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_281`)


Antwort: Diese Vereinbarung wurde mit Herrn M. geschlossen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_282`)


Diese Vereinbarung wurde  Herrn K. durch Herrn M. übersetzt.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_295`)


Herr K. und Herr M. waren da auch  anwesend.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_337`)


Ich habe mehrere Angebote eingeholt, diese habe ich dann Herrn M. mitgeteilt und er hat mir  dann mitgeteilt, ob er günstiger anbieten kann oder nicht.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_374`)


Niederschrift vom 26. November 2014 mit bf. (ArBg. S 141f)  „….  Frage: lt. Angaben des ehemaligen Mitarbeiters der Fa. e. Herrn Alexander X. hatten Sie eine  Vereinbarung mit der Fa. e., dass die Fa. e. ihnen Mineralöl um € 1,00 je 100 Liter billiger  verkauft, als Ihnen die Fa. F. ihre Ware anbietet (Ausdruck Mail von X. an M. vom 16.05.2014  wird vorgelegt).

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Alexander X.` (person)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_378`)


Ich habe die Preisverhandlungen mit Herrn M. geführt und ich habe  von M. diesen Preis verlangt, da ich bei der e. immer gleich bezahlen musste mit  Eilüberweisung, bei der Fa.F. hatte ich aber ein Zahlungsziel von 30 Tagen vereinbart.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |
| `M.` | `M.` |

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_397`)


3 bei meinem Besuch ausgesehen hat, gebe ich an:  Es war noch nicht viel in dem Büro, weil es erst eingerichtet werden musste, zumindest hat mir  M. dies so gesagt.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_399`)


Bei diesem Besuch waren anwesend: ich, Herr Z, Herr K., Herr M. und die Buchhalterin  gemacht.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_518`)


Aktenkundig ist, dass die Bf. in folgende Unterlagen Einsicht genommen hat bzw.  Überprüfungshandlungen gesetzt hat:  Fa. c:   Auszug aus dem Gewerberegister (13.6.2013)   Bescheid über die Erteilung der UID -Nummer (26. Juni 2013)   Bescheid vom 8. Juli 2013 Zollamt Wien (Registrierung-Identifizierung von  Wirtschaftsbeteiligten, Zuteilung einer EORI-Nummer)   Bescheid vom 1. August 2013 (Bewilligung zum Bezug von Mineralöl)  Fa. e.   Auszug aus dem Gewerberegister (18.11.2013)   Firmenbuchauszug (27.5.2013)   Kopien der übergebenen Visitenkarten Hr. K., Hr. M., Hr. X.   Passkopie Hr. K.   1 Bild eines Geschäftsmeetings mit Hr. bf. und Hr. K.   3 Bilder betreffend den Geschäftssitz der Gesellschaft (Tafel neben Klingel, Tafel   Eingangstüre)   Bescheid über die Erteilung der UID -Nummer (31.7.2013)   Bestätigung über die Gültigkeit der UID-Nummer (15.04.2014)   Bescheid über die Registrierung als Empfänger für Mineralöl   Rahmenvertrag über die Lieferung von Erdöl (3.3.2014)  D. GmbH    Auszug Gewerberegister (4.9.2013)   Firmenbuchauszug (4.9.2013)   Angebot vom 26.9.2013   Passkopie Hr. d.   Rückstandsbescheinigungen Finanzamt (31.10.2013,25.11 .2013, 6.12.2013)  Darüberhinaus hat der Gf. der Bf.  – wie dem Protokoll vom 1. März 2017 mit Herrn Inn Trikraftglanz  zu  entnehmen ist - nach der Außenprüfung (betreffend die Jahre 2010-2012) und Belehrung  (26.9.2013) folgende Schritte geändert bzw genauer beachtet und freiwillig zusätzliche  Maßnahmen gesetzt wie regelmäßige Abfrage der UID Nummern, regelmäßige Anforderung  von Rückstandsbescheinigungen, keine Barzahlungen, Zahlung ausschließlich auf  österreichische Konten, ausschließlich Lieferbeziehungen zu österreichischen Gesellschaften.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Zollamt Wien` (organisation)
- `Finanzamt` (organisation)
- `Inn Trikraftglanz` (person)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_22`)


Der Beschwerde beigelegt wurde eine ärztliche Bestätigung des Psychiaters M. vom  07.12.2021, die wie folgt lautet:   „Frau H. steht bei mir in regelmäßiger Betreuung bei F33.-Rezidivierende depressive Störung.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf) stellte am 6. März 2020 für ihre Tochter M., geb. 1992, einen  Antrag auf Gewährung der Familienbeihilfe und des Erhöhungsbetrages wegen erheblicher  Behinderung (Asperger Syndrom, Spezifische Phobie) und legte folgenden psychologischen  Kurzbefund der X Privatklinik, psychologische Universitätsambulanz, bei:  „… Untersuchungsdatum: 06.11.2019;

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_5`)


Frau F. M. kommt  an die psychologische Universitätsambulanz der X Privatuniversität um eine  Autismusdiagnostik durchführen zu lassen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_108`)


13.11.2019,22.11.2019, 6.12.2019 (Mutter), 11.12.2019,  20.12.2019 (Mutter), 08.01.2019  Frau F. M. kommt an die psychologische Universitätsambulanz der X Privatuniversität um eine  Autismusdiagnostik durchführen zu lassen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_138`)


M. wurde auf Grund der Beschwerde am 6. November 2021 ein weiteres Mal untersucht und  von Dr. Dok2 folgendes Gutachten erstellt:  "Anamnese:  letzte Begutachtung 7-2020 mit 30% wegen Asperger Syndrom  Nun Einspruch da sich ihr Zustand verschlechtert hätte  Schwangerschaft und Geburt unauffällig, nach der Geburt Unruhe und weinen aufgefallen, sie  hätte viel geweint.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Dr. Dok2` (person)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_168`)


Anhand des (Fach) Ärztlichen Gutachtens des Bundesamtes für Soziales und Behindertenwesen  (Sozialministeriumservice) vom 8.07.2020 beträgt der Grad der Behinderung für Ihre Tochter F.  M. 30% ab dem 1.11.2019.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Bundesamtes für Soziales und Behindertenwesen` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_215`)


M. ist ledig und lebt in einem eigenen Haushalt.  Im Zuge des Antrags- und Beschwerdeverfahrens wurden seitens des Sozialministeriumservice  zwei Gutachten erstellt.  Im Gutachten vom 8. Juli 2020 stellte Dr.in Dok1, Ärztin für Allgemeinmedizin, die Diagnose  Asperger Syndrom und reihte die Erkrankung unter die Pos.Nr. 03.04.01 der  Einschätzungsverordnung mit einem Grad der Behinderung von 30 vH. rückwirkend ab  November 2019 (= Austestung).

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Dr.in Dok1` (person)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_294`)


Dieser Befund aus 2019 befasst sich ausschließlich mit dem Zustand von M. zum Zeitpunkt der  Untersuchungen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_295`)


Festgestellt wurde, dass bei M. in Zusammenschau der Ergebnisse der  Anamnese, der Informationen der Mutter, der Verhaltensbeobachtung während des  Untersuchungsverlaufs sowie der Information, welche über die standardisierten diagno- stischen Verfahren ADOS und ADI gewonnen wurden, auf das Vorliegen einer Autismusspek- trumstörung geschlossen werden könne.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_299`)


Festgehalten wird, dass bei M. auf Grund ihrer Erkrankung am Asperger-Syndrom zweifellos  psychosoziale Beeinträchtigungen, welche sich auf verschiedenste Lebensbereiche, so auch  den beruflichen Lebensbereich erstrecken, bestehen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_9`)


Über Lenkererhebung vom 7. August 2023 teilte die Zulassungsbesitzerin des Fahrzeuges, A.  M., der Behörde mit, dass das Fahrzeug zur Beanstandungszeit Desiree Hannecken (Beschwerdeführer,  kurz: Bf.) überlassen gewesen sei.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `Desiree Hannecken` (person)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_15`)


Der Bf. brachte in seiner Stellungnahme vom 11. September 2023 vor, dass er bei der  Ausweisinhaberin M. als persönlicher Assistent (Verweis auf beiliegende Lohnbestätigung)  angestellt sei.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_16`)


Da seine Schwester, Frau M. seit ihrem 12.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_18`)


Am besagten Tag habe er M. zu  verschiedenen Örtlichkeiten gefahren.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_30`)


Im Zuge des Verfahrens habe festgestellt werden können, dass der Parkausweis gemäß § 29b  StVO mit der Nr. 123 vom Sozialministeriumservice, Landesstelle Wien, für Frau M., geb. 1980,  wohnhaft 1230 Wien, Str2, ausgestellt worden sei.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_32`)


In seiner schriftlichen Rechtfertigung habe der Bf. die Abstellung des Fahrzeuges an genannter  Örtlichkeit nicht in Abrede gestellt und im Wesentlichen vorgebracht, dass seine Schwester M.  seit ihrem 12.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_35`)


Dies sei auch an besagtem Tag so gewesen und könne es M. auch gerne bestätigen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_59`)


M. ist die Zulassungsbesitzerin des Fahrzeuges.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/142577.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142577.1_62`)


Beweiswürdigung:  Der Sachverhalt ergibt sich aus den eigenen Wahrnehmungen und Anzeigedaten des  Kontrollorgans der Parkraumüberwachung, den zur Beanstandungszeit angefertigten Fotos,  den Angaben der Zulassungsbesitzerin, der Auskunft des Sozialministeriumservice betreffend  den auf M. ausgestellten Parkausweis.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/143870.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143870.1_59`)


Der BF erzielte im Beschwerdejahr 2021 vom 24.03.2021 bis 24.06.2021 Einkünfte aus  nichtselbständiger Arbeit von der Fa. R und vom 01.07.2021 bis 03.12.2021 Einkünfte aus  nichtselbständiger Arbeit von der Fa. M.   Der BF erzielte im Jahr 2021 Einkünfte von der BUAK.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_373`)


kein  ÖGK-Kostenersatz oder sonstiger Nachweis der medizinischen Notwendigkeit iSd  VwGH-Judikatur;   - 742,- € M. M. für Physiotherapie/Heilmassage/osteopath.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |
| `M.` | `M.` |

**Missed by this rule (FN):**

- `ÖGK` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_378`)


Die Voraussetzungen für einen Abzug von der Kosten des Herrn M. als außergewöhnliche  Belastung im Jahr 2018 liegen insgesamt nicht vor.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 57** (doc_id: `deanon_BFG_20260814_VALIDATE/145731.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145731.1_420`)


Die hohen Kosten bei Handynutzung im Drittland kann man auch noch anhand der derzeitigen  Preise erkennen, so ist auf der Homepage von A. bzw. M. ersichtlich, dass ein abgehendes  29 von 65 Seite 30 von 65

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich`(address)
- `Maximilian Jasper`(person)
- `Wetzles 9, 3243 Lunzen, Österreich`(address)
- `Prof. Dr. Thomas Keppert`(person)
- `Leroy Kusznierz`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/131738.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131738.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Chiara Duchan, Vorsteherweg 116, 4912 Baumbach, Österreich, vertreten durch Maggi Brandl Kathollnig  RechtsanwaltsGmbH, St. Veiter Ring 21A, 9020 Klagenfurt, betreffend Beschwerde vom  25. August 2017 gegen den Bescheid des Finanzamtes Österreich vom 12. März 2015  betreffend Haftung gemäß § 9 Bundesabgabenordnung (BAO) beschlossen:  I. Der angefochtene Bescheid vom 12.03.2015 sowie die Beschwerdevorentscheidung  vom 07.09.2017, werden unter Zurückverweisung an die Abgabenbehörde  aufgehoben (§ 278 Abs. 1 BAO).

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Chiara Duchan`(person)
- `Vorsteherweg 116, 4912 Baumbach, Österreich`(address)
- `Maggi Brandl Kathollnig  RechtsanwaltsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132391.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Heike Lehmensieck, Höllstein 11, 9852 Neuschitz, Österreich, vertreten durch PwC PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH, Donau City Strasse 7, 1220 Wien, über die  Beschwerde vom 09. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 21. März  2016 betreffend Einkommensteuer 2013 zu Recht erkannt:   1.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Heike Lehmensieck`(person)
- `Höllstein 11, 9852 Neuschitz, Österreich`(address)
- `PricewaterhouseCoopers  Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_115`)


x Dauerzustand   Gutachten erstellt am 21.05.2020 von Dr. … E.-M.   Gutachten vidiert am 25.05.2020 von Janet Aspenleitner  8 von 16 Seite 9 von 16

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Janet Aspenleitner`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/134347.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134347.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Dora Szczepanowski, Max Schrems-Gasse 33, 9570 Ostriach, Österreich, betreffend die Säumnisbeschwerden vom  23.8.2021 wegen  1.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Dora Szczepanowski`(person)
- `Max Schrems-Gasse 33, 9570 Ostriach, Österreich`(address)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/134334.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134334.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Martin Yüksekkaya, Bonnleiten 21S, 4724 Aigen, Österreich  vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 31. März 2014 gegen den Bescheid des Finanzamtes für Großbetriebe vom  23. Jänner 2014 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2012  (Steuernummer 68-939/1151 ) nach Durchführung einer mündlichen Verhandlung am  06.07.2021 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Martin Yüksekkaya`(person)
- `Bonnleiten 21S, 4724 Aigen, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `68-939/1151`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/134372.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134372.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Wendelin Kasprowitz, Oberwinden 31, 8820 Kulm am Zirbitz, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 6. Oktober 2016 gegen die Bescheide des Finanzamtes für Großbetriebe je  vom 13. September 2016 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag  2013-2015 (Steuernummer 01-056/7050 ) nach Durchführung einer mündlichen  Verhandlung zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Dienstgeberbeitrag und Zuschlag zum  Dienstgeberbeitrag 2013 wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Wendelin Kasprowitz`(person)
- `Oberwinden 31, 8820 Kulm am Zirbitz, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `01-056/7050`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/134442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Brian Nieclaassen, Eiblweg 116, 4893 Brandstatt, Österreich, vertreten durch Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 29.08.2016 gegen die Bescheide des Finanzamtes für Großbetriebe vom  8. August 2016 betreffend Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag 2013-

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Brian Nieclaassen`(person)
- `Eiblweg 116, 4893 Brandstatt, Österreich`(address)
- `Glatzhofer & Matschek  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/135796.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135796.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache KommR Nicola Sturzbecher, Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich, vertreten durch Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H., Hans-Gasser-Platz 6c, 9500 Villach, über die  Beschwerde vom 03. Oktober 2013 gegen die Bescheide des Finanzamtes Österreich vom  3. Juli 2013 und 25.April 2017 bezüglich Wiederaufnahme des Verfahrens Umsatzsteuer 2009  bis 2011 und Umsatzsteuer 2009 bis 2012 (Steuernummer 19-116/5774 ) beschlossen bzw.  nach Durchführung einer mündlichen Verhandlung am 04.Oktober 2021 zu Recht erkannt:   I. BESCHLUSS  1.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `KommR Nicola Sturzbecher`(person)
- `Karl Schwaighofer-Straße 100, 8943 Sallaberg, Österreich`(address)
- `Arnulf R.Lagler Wirtschaftstreuhand-  & Steuerberatungs-Gesellschaft m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `19-116/5774`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/137362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137362.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Robert Derici, Exlgasse 12, 9623 Karnitzen, Österreich, vertreten durch Erich Allbrand,  betreffend Vorlageerinnerung zur Steuernummer 12-876/0077  beschlossen:  I. Die Vorlageerinnerung wird gem § 278 Abs 1 BAO iVm § 260 BAO als nicht zulässig  zurückgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Robert Derici`(person)
- `Exlgasse 12, 9623 Karnitzen, Österreich`(address)
- `Erich Allbrand`(person)
- `12-876/0077`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Cornelia Reifgerste, Scherzergütl 18K, 9622 Golz, Österreich, vertreten durch Freimüller Rechtsanwalts GmbH, 1010 Wien,  Kleeblattgasse 13/11A, vom 26. August 2020, gegen den Bescheid des Finanzamtes Österreich  vom 28. Juli 2020, betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für M. F. ab November 2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Pavlik`(person)
- `Cornelia Reifgerste`(person)
- `Scherzergütl 18K, 9622 Golz, Österreich`(address)
- `Freimüller Rechtsanwalts GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `M. F.`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_114`)


Frau M. F. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde Unfähi- gkeit, sich selbst den Unterhalt zu verschaffen: nach Art und Ausprägung: Kein Leiden welches  eine Erwerbsunfähigkeit begründet.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_157`)


Frau M. F. ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu verschaffen:  NEIN  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:  Es liegt keine zweifelsfrei dokumentierte Gesundheitsschädigung vor, die die dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen, zur Folge hat.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_173`)


Aufgrund  ihres Asperger-Syndroms sei M. F. sowohl im organisatorischen als auch im sozialen Bereich  regelmäßig überfordert und sei auch der Abschluss ihres begonnenen Studiums völlig offen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_177`)


Mit Beschwerdevorentscheidung vom 06.09.2021 verweise die belangte Behörde auf die  beiden fachärztlichen Gutachten des Bundesamtes für Soziales und Behindertenwesen vom  8. Juli 2020 und vom 6. November 2021, laut derer der Grad der Behinderung für M. F. 30 % ab  dem 01.11.2019 betrage und keine dauernde Erwerbsunfähigkeit vorliege.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesamtes für Soziales und Behindertenwesen`(organisation)
- `M. F.`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_184`)


Aufgrund jenes Befundes sei festgestellt worden, dass die  sozialen Interaktionen von M. F. stark eingeschränkt und starke soziale Unsicherheiten  verbunden mit sozialem Rückzug erkennbar seien.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_186`)


Um den beiden mangelhaften Vorgutachten zusätzlich inhaltlich entgegenzutreten, habe die  Antragstellerin ein Privatgutachten des allgemein beeideten und gerichtlich zertifizierten  Sachverständigen für Nerven- und Geisteskrankheiten Irene Pfleger …, eingeholt und lägen  demnach sowohl der Grad der Behinderung als auch die Minderung der Erwerbstätigkeit von  M. F. deutlich über 50 %.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Irene Pfleger`(person)
- `M. F.`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_188`)


Zwar betreibe M. F. ein Studium und ginge auch teilweise einer geringfügigen beruflichen  Tätigkeit nach, beides sei jedoch nur aufgrund massiver und dauernder familiärer  Unterstützung möglich.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_194`)


Es sei somit davon  auszugehen, dass M. F. dauerhaft nicht in der Lage sein werde, ihren eigenen Unterhalt  selbstständig erwirtschaften zu können.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_196`)


Zusätzlich bestünden weitere psychische Störungen (Angststörungen,  Zwangsstörungen, depressive Störungen), die über eine Begleitsymptomatik hinausgehen  würden wie auch somatische, also den körperlichen Zustand von M. F. umfassende,  Krankheitsbilder (vgl. 8. Diagnosen;

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_202`)


M. F.  sei neben dem beruflichen Bereich auch in Ihrem sonstigen sozialen Umfeld auf ständige  familiäre Hilfe und Unterstützung angewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_208`)


Hinsichtlich der gesetzlichen Voraussetzungen zur Gewährung erhöhter Familienbeihilfe seien  jene gutachterlichen Erhebungen wie folgt zu bewerten:  Nach Zitierung der §§ § 8 Abs 4 FLAG 1967 und 10 Abs 3 FLAG 1967 führte die Bf weiters aus,  dass die tiefgreifenden neuropsychologischen Entwicklungsstörungen von M. F. als dauerhaft  anzusehen seien und jedenfalls über einen zukünftigen dreijährigen Zeitraum hinausgehen  würden.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_210`)


Es könne zum jetzigen Zeitpunkt als  ausgeschlossen betrachtet werden, dass M. F. ohne familiäre Unterstützung für ihren eigenen  Unterhalt sorgen wird können.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M. F.`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_213`)


Das Bundesfinanzgericht hat erwogen  Feststellungen:  Die Tochter der Bf, M. F., geb.  1992, besuchte die Volksschule („Alternativ-Schule“),  Mittelschule, wechselte auf ein Realgymnasium, legte im Jahr 2011 die Matura erfolgreich ab  und studiert(e) laut Aktenlage (psychologischer Kurzbefund der X Privatklinik aus 2019,  Gutachten des Sozialministeriumservice) an der Universität Wien Geschichte.

**False Positives:**

- `M.` — partial — pred is substring of gold: `M. F.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `M. F.`(person)
- `Universität Wien`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/141031.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141031.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Maga. Ulrike Nussbaumer LL.M.  M.B.L., die Richterin Drin. Elisabeth Hafner, sowie die fachkundigen Laienrichter Eva Maiwald- Wanderer und Mag. Maximilian Turrini in der Beschwerdesache Anton Schwingschlögl, Rappelweg 12, 4724 Mäusburg, Österreich  vertreten durch CENTURION Wirtschaftsprüfungs- und Steuerberatungs GmbH, Hegelgasse 8  Tür 14, 1010 Wien, über die Beschwerden je vom 23. August 2022 gegen die Bescheide des  Finanzamtes Österreich vom 19. und 20. Juli 2022 die Berichtigung des  Einkommensteuerbescheides 2016 vom 03. Mai 2018 gemäß § 293b BAO und die  Einkommensteuer 2017 betreffend (Steuernummer 79-281/4180) nach Durchführung einer  mündlichen Verhandlung am 12. Mai 2023 zu Recht erkannt:  I. Der Beschwerde gegen den Bescheid vom 20. Juli 2022 die Berichtigung des  Einkommensteuerbescheides 2016 vom 03. Mai 2018 betreffend wird gemäß § 279  BAO Folge gegeben.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Eva Maiwald- Wanderer`(person)
- `Mag. Maximilian Turrini`(person)
- `Anton Schwingschlögl`(person)
- `Rappelweg 12, 4724 Mäusburg, Österreich`(address)
- `CENTURION Wirtschaftsprüfungs- und Steuerberatungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `79-281/4180`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/141688.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141688.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Saphira Schnaak, Kürschner Allee 44, 9300 Mail, Österreich, vertreten durch Ing. Mag. Hamza Ovacin,  Stadtstraße 33, Top 303, 6850 Dornbirn, betreffend Beschwerde vom 2. November 2022 gegen  die Bescheide des Finanzamtes Österreich vom 4. Oktober 2022 betreffend Körperschaftsteuer  2016 und Körperschaftsteuer 2017 zur Steuernummer 50-980/9446  beschlossen:  I. Der Vorlageantrag wird gem. § 278 Abs. 1 lit. a BAO iVm § 264 Abs. 4 lit. e BAO als  unzulässig zurückgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Saphira Schnaak`(person)
- `Kürschner Allee 44, 9300 Mail, Österreich`(address)
- `Ing. Mag. Hamza Ovacin`(person)
- `Finanzamtes Österreich`(organisation)
- `50-980/9446`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/142564.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142564.1_1`)


BESCHLUSS  Das Bundesfinanzgericht beschließt durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache Igor Rolfmeier, Dußwaldweg 41, 3171 Außerhalbach, Österreich, vertreten durch Lenfeld | Leys | Sonderegger -  Rechtsanwälte (GesbR), Malserstraße 19, 6500 Landeck, betreffend Beschwerde vom  19. Oktober 2018 gegen die Bescheide des Finanzamtes Innsbruck vom 4. April 2018  betreffend Wiederaufnahme der Einkommensteuerverfahren für die Jahre 2014 bis 2016,  Steuernummer 06-230/8922:  I. Die Beschwerde wird als verspätet zurückgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. David Hell LL.B. LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `Igor Rolfmeier`(person)
- `Dußwaldweg 41, 3171 Außerhalbach, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)
- `06-230/8922`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/143290.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143290.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Leopold Dobertin, Dr.Julius-Kugy-Straße 130, 5071 Wals, Österreich, über die Beschwerden gegen Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg   vom 30. Oktober 2015 gegen den Bescheid vom 9. Oktober 2015 betreffend Festsetzung von  zweiten Säumniszuschlägen,  vom 2. März 2016 gegen den Bescheid vom 11. Jänner 2016 betreffend Festsetzung von dritten  Säumniszuschlägen und  vom 2.1.2020 gegen den Bescheid vom 13.12.2019 betreffend Aufhebung/Abänderung von  Nebengebühren  nach der am 4.12.2023 am Bundesfinanzgericht in Wien über Antrag der Partei (§ 78 BAO  i.V.m. § 274 Abs. 1 Z 1 BAO) in Abwesenheit der Beschwerdeführerin bzw ihrer Vertretung und  in Anwesenheit von Mag. Martin Holzapfel und Mag. Sebastian Rivo-Wastl, BA für die belangte  Behörde durchgeführten mündlichen Verhandlung zur Steuernummer 38-992/7403  zu  Recht erkannt:   I. Der Beschwerde vom 30.10.2015 wird teilweise Folge gegeben und zweite  Säumniszuschläge in Höhe von 5.739,66 € festgesetzt.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Leopold Dobertin`(person)
- `Dr.Julius-Kugy-Straße 130, 5071 Wals, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Mag. Martin Holzapfel`(person)
- `Mag. Sebastian Rivo-Wastl, BA`(person)
- `38-992/7403`(tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/143814.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143814.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Othmar Garbe, Bf. Adresse, Ort in Kärnten, vertreten durch Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH, Bahnhofstraße 45, 9020 Klagenfurt/Wörthersee,  über die Beschwerde vom 6. Oktober 2016 gegen die Bescheide des Finanzamtes für  Großbetriebe vom 14. September 2016 betreffend Dienstgeberbeitrag und Zuschlag zum  Dienstgeberbeitrag 2013 – 2015 (Steuernummer 29-838/1383) zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Othmar Garbe`(person)
- `Glatzhofer &  Matschek Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes für  Großbetriebe`(organisation)
- `29-838/1383`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_95`)


Die Auszahlung der Familienbeihilfe an W.B. ist daher W.M., als Anspruchsberechtigte  zuzurechnen.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/146522.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146522.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Francois Roeder, Josef-Gauby-Gasse 7, 8762 Unterzeiring, Österreich, über die Beschwerde vom 12. Juni 2023 gegen  den Bescheid des Finanzamtes Österreich vom 9. Mai 2023 betreffend Säumniszuschlag 2023  nach der am 22.11.2024 am Bundesfinanzgericht in Wien über Antrag der Partei abgehaltenen  mündlichen Verhandlung in Abwesenheit des Beschwerdeführers und in Anwesenheit von  Bernadette Pommer BA MA für das Finanzamt sowie der Schriftführerin Mag. Magdalena  Preslmayr zur Steuernummer 48-847/1680  zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Festsetzung eines ersten  Säumniszuschlages vom 9.5.2023 in Höhe von € 148,00 wird gemäß § 279 BAO als  unbegründet abgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Francois Roeder`(person)
- `Josef-Gauby-Gasse 7, 8762 Unterzeiring, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Bernadette Pommer`(person)
- `Finanzamt`(organisation)
- `Mag. Magdalena  Preslmayr`(person)
- `48-847/1680`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_150`)


Das Kriterium der Fremdüblichkeit sei somit erfüllt.   Nach der Beurteilung des Sachverhalts durch die Betriebsprüfung entspreche das an das Paar  M.M. vermietete Hauptgebäude in Größe und Ausstattung keiner üblichen Mietwohnung.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_169`)


Die Fam. M.M. würde somit (ohne Kfz-Einstellplätze und das in Bau befindliche Saunahaus) ca.  82% der Nutzfläche (Wohn- und Kellerräume) benützen.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_203`)


M.M. diene und von diesen auch  zur Gänze genutzt werde (siehe Betriebsbesichtigung v. 18.06.2015 Tz 3) wie folgt begründet:   1)

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_234`)


Selbst bei fiktiver Annahme des Nichtvorliegens von Liebhaberei sei in Hinblick auf die  besondere Ausstattung der an die Fam. M.M. vermieteten Wohnungen von einem nicht  marktüblichen Mietpreis auszugehen.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_299`)


Der Einzug der Familie M.M. in Top 1 und 3 sei am 1.11.2012 insoweit frühzeitig gewesen, als  diese Wohnungen zu diesem Zeitpunkt noch nicht bezugsfertig gewesen wären und wegen des  früher als erwartet abgewickelten Verkaufs des bis dahin bewohnten Hauses mangels  Alternativen zu beziehen gewesen wären.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_342`)


Von den zwei getrennt auf der Liegenschaft errichteten Wohngebäude samt Saunahaus dient  das Gebäude (1) Hauptgebäude in Form eines Eigenheimes mit insgesamt 3 Wohnungen den  Wohnbedürfnissen der Familienmitglieder der Fam. M.M. und wird von diesen auch zur Gänze  genutzt.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/146866.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Gerald Bährensmann, Adr. zu Handen Mag. Thomas Kollaczia-Putz, Annagasse 3-3A,  1010 Wien über die Beschwerde vom 22. Oktober 2018 gegen die Bescheide des Finanzamtes  Gmunden Vöcklabruck vom 25. September 2018, Steuernummer 04-246/1421  betreffend  Körperschaftsteuer 2014, Körperschaftsteuer 2015, Körperschaftsteuer 2016, Umsatzsteuer  2014, Umsatzsteuer 2015 und Umsatzsteuer 2016 nach Durchführung einer mündlichen  Verhandlung am 9. Jänner 2025 in Beisein des Schriftführers Markus Blöchl LL.B. LL.M. zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Markus Blöchl LL.B. LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Gerald Bährensmann`(person)
- `Mag. Thomas Kollaczia-Putz`(person)
- `Finanzamtes  Gmunden Vöcklabruck`(organisation)
- `04-246/1421`(tax_number)
- `Markus Blöchl LL.B. LL.M.`(person)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/147714.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147714.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Maga. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Claire Dummert, Rachenbach 10, 4352 Niederkalmberg, Österreich  vertreten durch Pickerle + Tengg  Wirtschaftsprüfungs- und SteuerberatungsgesmbH, Bahnhofstraße 8, 9500 Villach, über die  Beschwerden vom 25. November 2022 und 28. März 2023 gegen die Bescheide des  Finanzamtes Österreich vom 25. Oktober 2022 und 28. Feber 2023 die Wiederaufnahme der  Einkommensteuerverfahren 2016-2019 und die Einkommensteuer 2016-2020 beschlossen  (Steuernummer 47-092/4894):  I. Gemäß § 278 Abs. 1 BAO werden die angefochtenen Bescheide sowie die in weiterer  Folge erlassenen Beschwerdevorentscheidungen, letztere jeweils datierend mit 11.  April 2023, aufgehoben und die Sache zur Erledigung an die Abgabenbehörde  zurückverwiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Claire Dummert`(person)
- `Rachenbach 10, 4352 Niederkalmberg, Österreich`(address)
- `Pickerle + Tengg  Wirtschaftsprüfungs- und SteuerberatungsgesmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `47-092/4894`(tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/149367.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149367.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Jeffrey Stubenrauch, Adalbert-Schreyer-Straße 4S, 4364 Thomasreit, Österreich  vertreten durch Aviso Wirtschaftstreuhand- und  Steuerberatungs GmbH, Mosetiggasse 1, 1230 Wien, über die Beschwerde vom 31.10.2024  gegen die Bescheide des Finanzamtes Österreich je vom 30.08.2024 die Wiederaufnahme der  Verfahren betreffend Umsatzsteuer 2018-2021, sowie Umsatzsteuer 2018-2022  (Steuernummer 05-888/5257) nach Durchführung einer mündlichen Verhandlung am  10.10.2025   I. beschlossen:  Die Beschwerde vom 31.10.2024 gegen den Umsatzsteuerbescheid 2022 vom 30.  August 2024 wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Jeffrey Stubenrauch`(person)
- `Adalbert-Schreyer-Straße 4S, 4364 Thomasreit, Österreich`(address)
- `Aviso Wirtschaftstreuhand- und  Steuerberatungs GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `05-888/5257`(tax_number)

</details>

---

## `Herrn_Name_Full` 🏆

**F1:** 0.036 | **Precision:** 0.586 | **Recall:** 0.018  

**Format:** `regex`  
**Rule ID:** `fcb4a905`  
**Description:**
Captures full names following 'Herrn' (accusative), including titles like RgR, OMedR, Mag., Dr., etc., ensuring the full name is captured.

**Content:**
```
\bHerrn\s+(?:Hon\.-Prof\.(?:in)?\s+|Dr\.(?:in)?\s+|Priv\.-Doz\.(?:in)?\s+|Mag\.(?:Dr\.)?\s+|Univ\.-Prof\.(?:in)?\s+|Bakk\.(?:\s+rer\.\s+nat\.|\s+rer\.\s+art\.|\s+rer\.\s+techn\.|\s+rer\.\s+jur\.)?\s+|Ing\.(?:\s+Dipl\.)?\s+|Mag\.a\s+|Prof\.in\s+|Prof\.(?:in)?\s+|RA\s+Mag\.(?:in)?\s+|DDr\.(?:in)?\s+|MedR\.(?:in)?\s+|RgR\.(?:in)?\s+|KzlR\.(?:in)?\s+|VetR\.(?:in)?\s+|KommR\.(?:in)?\s+|OMedR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+LL\.M\.|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.586 | 0.018 | 0.036 | 58 | 34 | 24 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 34 | 24 | 1817 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129064.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129064.1_98`)


Z1 wurde laut der vorgelegten Protokollsabschrift am 11.6.2018 an der Polizeiinspektion  d_Ort_1 vernommen und gab unter anderem an: „Seit Mitte dem Jahr 2016 bin ich als  Steuerberater für …Herrn Volchert tätig.

| Predicted | Gold |
|---|---|
| `Volchert` | `Volchert` |

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_71`)


Im Rahmen der Firmengründung wurde von Herrn Frikel ein  Fahrzeug als sein Beitrag bzw. als Einlage eingebracht.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_73`)


Dieses Kfz wurde von Herrn Frikel selber angeschafft, wo und zu welchen  Bedingungen kann ich nicht angeben.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_75`)


Ich selber war dann in der Folge mehrmals in Österreich bei Herrn Frikel  wenn ich  mit dem Flugzeug anreiste, konnte ich dann den Audi verwenden (so ca. 15 mal pro Jahr) und  damit Kundenbesuche etc. erledigen.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_80`)


Die Bilanz für 2010 ist noch nicht  erstellt. In Deutschland an meinem Wohnsitz bzw. am Firmensitz konnte ich somit nicht  permanent über das KFZ Audi A6 verfügen, es befand sich des öfteren im Besitz des Herrn Frikel in  A/Adr1 und somit an diesem Standort.

| Predicted | Gold |
|---|---|
| `Frikel` | `Frikel` |

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Albert Sengeisen, Wallnerfeld 8, 3751 Sigmundsherberg, Österreich, vertreten durch gfk Gartner Furherr Karandi Rechtsanwälte,  Westbahnstraße 5/11, 1070 Wien, wegen der Finanzvergehen der Abgabenhinterziehungen  gemäß § 33 Abs. 1 und Abs. 2 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des  Beschuldigten vom 21. April 2017 gegen das Erkenntnis des Spruchsenates beim Finanzamt  Wien 9/18/19 Klosterneuburg als Organ des Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. Jänner 2017, SpS 16, Strafnummer 007 in Abwesenheit des  Beschuldigte und seines Verteidigers, jedoch in Anwesenheit des Amtsbeauftragten sowie der  Schriftführerin zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates wie folgt abgeändert:  Das beim Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde zur Strafnummer  007 geführte Finanzstrafverfahren wegen des Verdachts der Abgabenhinterziehung gemäß §  33 Abs. 2 lit. a FinStrG betreffend Umsatzsteuervorauszahlungen 03/2014 in Höhe von €  433,00 und 07-11/2014 von € 1.785,72 wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG  eingestellt.  Über Albert Sengeisen  wird für die verbleibenden Finanzvergehen gemäß § 33 Abs. 5 FinStrG eine  Geldstrafe in Höhe von € 20.600,00 Tage verhängt.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Wallnerfeld 8, 3751 Sigmundsherberg, Österreich` (address)
- `Finanzamt  Wien 9/18/19` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130996.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130996.1_270`)


Bedeutsame  Firmenunterlagen - Rechnungslegungen - sind von durchwegs von Herrn Albert Sengeisen  approbiert.

| Predicted | Gold |
|---|---|
| `Albert Sengeisen` | `Albert Sengeisen` |

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/131506.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131506.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde vom 24.06.2020 des Herrn Raimund Ladwig, Birkenring 18, 8451 Pernitsch, Österreich, Deutschland  wohnhaft, gegen den Bescheid des Finanzamtes Bruck Eisenstadt Oberwart, vom 10.07.2020,  Antragsnummer: ***, betreffend Abweisung des Antrages vom 3.3.2020 auf Rückzahlung von  Abzugssteuer (Lohnsteuer 2019) auf Grund des Artikel 27 des Doppelbesteuerungsabkommens  mit Deutschland  zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben und antragsgemäß die im Jahr 2019  entrichtete Lohnsteuer in Höhe von Euro 1.366,80 gemäß § 240a BAO und Art. 15 Abs. 6 i.V.m.  Art 27 DBA-Deutschland erstattet.

| Predicted | Gold |
|---|---|
| `Raimund Ladwig` | `Raimund Ladwig` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Fröhlich` (person)
- `Birkenring 18, 8451 Pernitsch, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_37`)


1) Mit Schreiben vom 13.05.2020 wurde von Herrn Angelstein mitgeteilt, dass er weder  Geschäftsführer der Firma sei noch mit dem Fahrzeug gefahren sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_38`)


Mit Schreiben vom 02.06.2020 wurde durch die Rechtsanwälte des Herrn Angelstein mitgeteilt, dass  dieser keine Lenkerauskunft erteilen könne, da er lediglich für das Fahrzeug mit dem amtlichen  Kennzeichen Auto3 (Anmerkung BFG: nicht gegenständlich) verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_50`)


Mit Schreiben vom 04.06.2020 teilte die rechtsfreundliche Vertretung des Herrn Angelstein  mit, dass der Genannte über das gegenständliche Fahrzeug zum Beanstandungszeitpunkt nicht  verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_51`)


Mit Schreiben vom 18.06.2020 wurde die Zulassungsbesitzerin des gegenständlichen  Fahrzeuges aufgefordert die erteilte Lenkerauskunft durch Vorlage entsprechender  Beweismittel (Unterlagen über die Bestellung des Herrn Angelstein als verantwortlicher Beauftragter  gemäß § 9 Abs. 2 Verwaltungsstrafgesetz 1991) glaubhaft zu machen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_57`)


In der E-Mail Ihres rechtsfreundlichen Vertreters vom 01.10.2020 wurde zum gegenständlich  angelasteten Sachverhalt vorgebracht, die Zulassungsbesitzerin und deren handelsrechtliches  Organ habe der Aufforderung der Behörde zur Lenkerauskunft gesetzestreu entsprochen, zumal  dargelegt worden sei, dass die verlangte Auskunft von Herrn Angelstein  geb. Herrgeb, AdrHerr, 1030  Wien, als Verantwortlicher gemäß § 9 VStG erteilt werden könne.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_60`)


Weiters  wurde die Herbeischaffung des Aktes der WKStA zur AZ: AktWKStA, dessen Inhalt die  Übertragung der Meldepflicht gemäß § 9 VStG auf Herrn Angelstein beweisen soll, beantragt.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_81`)


Aufgrund des Umstandes, dass trotz mehrfacher Aufforderung durch die Behörde bis dato  weder in diesem Verfahren noch in anderen bei der Behörde gegen Sie anhängigen Verfahren  ein Dokument vorgelegt wurde, das die nachweisliche Zustimmung des Herrn Angelstein zur  Bestellung als verantwortlicher Beauftragter gemäß § 9 Abs. 2 VtG beurkundet, geht die  erkennende Behörde davon aus, dass eine derartige Zustimmung nicht vorliegt und deswegen  als erwiesen anzusehen ist, dass Herr Russbüldt nicht verantwortlicher Beauftragter gemäß § 9 Abs.  2 VStG ist.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)
- `Dr.in Ing. Viktoria Weigart` (person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_154`)


In Beantwortung der nunmehr an Herrn Angelstein gerichteten (sechs) Lenkererhebungen der  belangten Behörde bestritt dieser seine Auskunftspflicht mit den Worten   1) bis 5) „dass ich weder ein Geschäftsführer dieser Firma noch mit diesem Fahrzeug gefahren  bin.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_156`)


6) Ich bin nie mit diesem Auto gefahren.“  2) bis 6): Mit fünf Strafverfügungen vom 20.05.2020 wurde Herrn Angelstein angelastet, er habe als §  9 VStG verantwortlich Beauftragter der Zulassungsbesitzerin Firma1 der mehrspurigen  Fahrzeuge mit den (jeweils oben genannten) behördlichen Kennzeichen den (jeweils)  ordnungsgemäß zugestellten Verlangen der Behörde, innerhalb von zwei Wochen ab  Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug überlassen gehabt habe, sodass  es (jeweils) zu oben genannten Zeiten an oben genannten Orten gestanden sei, nicht  entsprochen, da er keine konkrete Person als Lenker bekannt gegeben habe.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_157`)


Mit Schreiben vom 04.06.2020 erhob der rechtsfreundliche Vertreter von Herrn Angelstein einen  Sammeleinspruch gegen die Strafverfügungen 2) bis 6) und weitere, nicht gegenständliche  Strafverfügungen und gab dieser bekannt, dass Herr Russbüldt zu den angeführten Kennzeichen zu  relevierten Tatzeitpunkten nachweislich nicht verfügungsberechtigt gewesen sei.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Russbüldt` (person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `Dr.in Ing. Viktoria Weigart` (person)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_174`)


3. Zulässigkeit des Einspruches:  …  4. Gründe des Einspruches:  Der Vorwurf, der Einschreiter hätte als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin der Firma1 des Fahrzeuges mit dem behördlichen Kennzeichen Auto4  [Anmerkung BFG: nicht gegenständlich] dem ordnungsgemäß zugestellten Verlangen der MA  67 vom 28.01.2020, innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er  dieses Fahrzeug überlassen gehabt hat, sodass dieser zur in der Strafverfügung angegebenen  Tatzeit und Tatort gelenkt hat bzw. vor diesem Zeitpunkt abgestellt hat nicht entsprochen zu  haben und somit die Rechtsvorschriften des § 103 Abs 2 KFG [Anmerkung BFG, gemeint: § 2  (Wiener) Parkometerabgabeverordnung iVm § 4 Abs. 2 Parkometergesetz 2006] trifft nicht zu,  dies aus folgenden Gründen: Es wurde - wie oben erwähnt - vom Einschreiter die Übertragung  der Meldepflicht auf Herrn Angelstein  geb. Herrgeb, übertragen.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Missed by this rule (FN):**

- `BFG` (organisation)
- `BFG` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_191`)


Darin hat die Einschreiterin  und deren handelsrechtliches Organ dargelegt, dass die verlangte Auskunft nicht erteilt werden  kann, sondern von Herrn Angelstein  geb. Herrgeb, AdrHerr, 1030 Wien als Verantwortlichen gemäß  § 9 VStG.

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_213`)


Darin hat die Einschreiterin und deren handelsrechtliches Organ dargelegt, dass die verlangte  Auskunft nicht erteilt werden kann, sondern von Herrn Angelstein  geb. Herrgeb, AdrHerr, als  Verantwortlichen gemäß § 9 VStG.  16 von 22 Seite 17 von 22

| Predicted | Gold |
|---|---|
| `Angelstein` | `Angelstein` |

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_228`)


Unabhängig davon ist zu der mehrfach angeführten „Belehrung" festzuhalten, dass diese unter  Beisein der steuerlichen Vertreterin -Frau Borisowa- erfolgte und sich im Wesentlichen darauf  beschränkte, dass man Herrn Inn Trikraftglanz mitteilte, dass er „besser aufpassen muss".

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Borisowa` (person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_409`)


Es ist auch darauf hinzuweisen, dass beim Mineralölhandel nur sehr kleine Gewinnspannen  möglich sind, es hätte daher für die Bf. fragwürdig sein müssen, wieso neue Anbieter billiger  sein können, wie alt eingesessene große Mineralöllieferanten wie die g. oder H.. Fraglich sei  auch, wieso die Bf. bei den anderen Lieferanten kein Skonto in Anspruch genommen hat,  obwohl dies nach Angabe von Herrn Inn Trikraftglanz möglich gewesen wäre.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_424`)


Ein Naheverhältnis zwischen Herrn Inn Trikraftglanz und den gegenständlichen  Lieferanten hat es nicht gegeben.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_425`)


Frau AB.: Herr d. wäre einverstanden gewesen, dass Herr Inn Trikraftglanz  die Umsatzsteuer direkt auf das  Finanzamtskonto einzahlt. Das war für Herrn Inn Trikraftglanz  ein Indiz, dass die Fa. d. eine redliche Firma ist.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_518`)


Aktenkundig ist, dass die Bf. in folgende Unterlagen Einsicht genommen hat bzw.  Überprüfungshandlungen gesetzt hat:  Fa. c:   Auszug aus dem Gewerberegister (13.6.2013)   Bescheid über die Erteilung der UID -Nummer (26. Juni 2013)   Bescheid vom 8. Juli 2013 Zollamt Wien (Registrierung-Identifizierung von  Wirtschaftsbeteiligten, Zuteilung einer EORI-Nummer)   Bescheid vom 1. August 2013 (Bewilligung zum Bezug von Mineralöl)  Fa. e.   Auszug aus dem Gewerberegister (18.11.2013)   Firmenbuchauszug (27.5.2013)   Kopien der übergebenen Visitenkarten Hr. K., Hr. M., Hr. X.   Passkopie Hr. K.   1 Bild eines Geschäftsmeetings mit Hr. bf. und Hr. K.   3 Bilder betreffend den Geschäftssitz der Gesellschaft (Tafel neben Klingel, Tafel   Eingangstüre)   Bescheid über die Erteilung der UID -Nummer (31.7.2013)   Bestätigung über die Gültigkeit der UID-Nummer (15.04.2014)   Bescheid über die Registrierung als Empfänger für Mineralöl   Rahmenvertrag über die Lieferung von Erdöl (3.3.2014)  D. GmbH    Auszug Gewerberegister (4.9.2013)   Firmenbuchauszug (4.9.2013)   Angebot vom 26.9.2013   Passkopie Hr. d.   Rückstandsbescheinigungen Finanzamt (31.10.2013,25.11 .2013, 6.12.2013)  Darüberhinaus hat der Gf. der Bf.  – wie dem Protokoll vom 1. März 2017 mit Herrn Inn Trikraftglanz  zu  entnehmen ist - nach der Außenprüfung (betreffend die Jahre 2010-2012) und Belehrung  (26.9.2013) folgende Schritte geändert bzw genauer beachtet und freiwillig zusätzliche  Maßnahmen gesetzt wie regelmäßige Abfrage der UID Nummern, regelmäßige Anforderung  von Rückstandsbescheinigungen, keine Barzahlungen, Zahlung ausschließlich auf  österreichische Konten, ausschließlich Lieferbeziehungen zu österreichischen Gesellschaften.

| Predicted | Gold |
|---|---|
| `Inn Trikraftglanz` | `Inn Trikraftglanz` |

**Missed by this rule (FN):**

- `Zollamt Wien` (organisation)
- `M.` (person)
- `Finanzamt` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Harald Hilderink, geboren am 1965, Schmetterlingstraße 12, 4224 Ruhstetten, Österreich  vertreten durch Koch & Partner  SteuerberatungsgmbH, IZ Nö Süd, Str. 7, Obj.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Schmetterlingstraße 12, 4224 Ruhstetten, Österreich` (address)
- `Koch & Partner  SteuerberatungsgmbH` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_50`)


Eine Straffestsetzung von EUR 10.000,00 ist daher unangemessen  und unverhältnismäßig!   Die Abgabe der Umsatzsteuervoranmeldungen wurde von Herrn Harald Hilderink  irrtümlich  im Vertrauen auf die steuerliche Vertretung übersehen.

| Predicted | Gold |
|---|---|
| `Harald Hilderink` | `Harald Hilderink` |

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_7`)


Nach erfolgter Lenkererhebung vom 13. März 2023 teilte die Bezirkshauptmannschaft Ort mit  Schreiben vom 16. März 2023 der belangten Behörde aufgrund einer Anfrage mit, dass der  Parkausweis mit der Nummer Nr1 (Nr2) am 22. März 2002 von der BH Ort an Herrn Isenmann  geb.  Herrgeb, AdrHerr, ausgegeben worden sei und dass Herr Ballschmieder laut ZMR mit Datum verstorben  sei.

| Predicted | Gold |
|---|---|
| `Isenmann` | `Isenmann` |

**Missed by this rule (FN):**

- `Ballschmieder` (person)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_45`)


Der Parkausweis Nr. Nr1 (Nr2) wurde am 22. März 2002 von der Bezirkshauptmannschaft Ort  an Herrn Isenmann  geb. Herrgeb, AdrHerr, ausgestellt.Herr Ballschmieder ist laut ZMR mit Datum  verstorben.

| Predicted | Gold |
|---|---|
| `Isenmann` | `Isenmann` |

**Missed by this rule (FN):**

- `Ballschmieder` (person)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/141237.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141237.1_54`)


Dass der (Original)Ausweis gemäß § 29b StVO 1960 mit der Nr. Nr1 (Nr2) an Herrn Isenmann  geb.  Herrgeb, ausgestellt wurde und dass Herr Ballschmieder laut ZMR mit Datum verstorben ist, ergibt sich  aus dem Schreiben der Bezirkshauptmannschaft Ort vom 16. März 2023.

| Predicted | Gold |
|---|---|
| `Isenmann` | `Isenmann` |

**Missed by this rule (FN):**

- `Ballschmieder` (person)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/143044.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143044.1_20`)


Das FA wies auf die Meldebestätigung  betreffend die Bf und Ihrem Partner/Lebensgefährten Herrn Schäperjans und auf den ESt- bescheid 2016 vom 1.9.2017 an den Partner der Bf hin.

| Predicted | Gold |
|---|---|
| `Schäperjans` | `Schäperjans` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131553.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131553.1_10`)


Ein weiterer ärztlicher Befundbericht von Fr. Dr. **** und Herrn Dr. **** lagen ebenfalls dem  Antrag bei.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133816.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133816.1_374`)


Niederschrift vom 26. November 2014 mit bf. (ArBg. S 141f)  „….  Frage: lt. Angaben des ehemaligen Mitarbeiters der Fa. e. Herrn Alexander X. hatten Sie eine  Vereinbarung mit der Fa. e., dass die Fa. e. ihnen Mineralöl um € 1,00 je 100 Liter billiger  verkauft, als Ihnen die Fa. F. ihre Ware anbietet (Ausdruck Mail von X. an M. vom 16.05.2014  wird vorgelegt).

**False Positives:**

- `Alexander` — partial — pred is substring of gold: `Alexander X.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alexander X.`(person)
- `M.`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_138`)


Nur weil das Finanzamt  diese Unterlagen nicht mehr im Akt finde, wie in der Bescheidbegründung der BVE behauptet,  heiße das nicht, dass die Behauptung von Herrn BfA unwahr sei.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_186`)


Knackpunkt für das Finanzamt sei, dass keine Nachweise  hinsichtlich einer Vorsprache Herrn BfAs sowie hinsichtlich einer mit diesem getroffenen  Einigung im Akt des FA enthalten sei.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/135318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135318.1_304`)


Der Anteil an den Einkünften für Herrn BfA beträgt: Euro 10.081,85  Der Anteil an den Einkünften für Frau BfB beträgt: Euro 10.081,84

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_17`)


Es würden mit Herrn Ing. K. (Geschäftsführer der Fa. X.  2 von 9 Seite 3 von 9

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/138294.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138294.1_19`)


Die Entlehnung des Kfz gehe auf ein privates Ersuchen des Herrn Ing. K. zurück.

**False Positives:**

- `Ing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)


Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der Jeremias Kierstan, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_4`)


Dieser Bescheid war an die Jeremias Kierstan  gerichtet und wurde Herrn Vertreter als  Zustellungsbevollmächtigten am 03.09.2015 zugestellt.  Gegen diesen Bescheid wurde mit Schreiben vom 09.09.2015, beim Magistrat eingelangt am  11.09.2015, von der Heimwerk GmbH, vertreten durch Herrn Vertreter, im eigenen Namen  Beschwerde erhoben und ausgeführt, die Behörde habe in keiner Weise dargelegt, wie die von  ihr angenommenen Nichteinleitungsmenge ermittelt worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation
- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Heimwerk GmbH`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_9`)


Mit Beschwerdevorentscheidung vom 05.11.2015, gerichtet an die Jeremias Kierstan, zu Handen  Herrn Vertreter, wurde die Beschwerde als unbegründet abgewiesen, wobei die belangte  Behörde davon ausging, dass die Beschwerde von der Jeremias Kierstan, erhoben worden sei.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Jeremias Kierstan`(person)
- `Jeremias Kierstan`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_10`)


Mit Eingabe vom 03.12.2015 stellte die Heimwerk GmbH  vertreten durch Herrn Vertreter, den Antrag,  die Beschwerde dem Bundesfinanzgericht zur Entscheidung vorzulegen.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Bundesfinanzgericht`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_28`)


Der angefochtene Bescheid vom 17.07.2015, mit welchem über den Antrag der Heimwerk GmbH auf  Herabsetzung der Abwassergebühr für 2013 abgesprochen wurde, ist an die Jeremias Kierstan  als  Partei ergangen und an deren Zustellbevollmächtigten, Herrn Vertreter zugestellt worden.

**False Positives:**

- `Vertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heimwerk GmbH`(organisation)
- `Jeremias Kierstan`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_24`)


Sie wären am  besagten Tag mit Herrn Herr1 unterwegs gewesen.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/138762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138762.1_25`)


Ebenso könne Herr Herr2, der die  Mitarbeitereinsatzplanung mit Herrn Herr3 vorbereitet bezeugen, dass Ihnen das Fahrzeug als  Verantwortlicher übergeben wurde.

**False Positives:**

- `Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_65`)


Gegen den Zurückweisungsbescheid der belangten Behörde vom 22. März 2023 erhob der  Beschwerdeführer fristgerecht Beschwerde und führte aus, er übersende noch einmal alle  Geschäftszahlen die bis einschließlich 31.03.2023 von Herrn Lenker2 verschuldet worden seien.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_66`)


Er habe die Behörde schon mehrmals gebeten alle (folgenden) Anonymverfügungen direkt an  Herrn Lenker2 zu senden, die für das gegenständliche Kraftfahrzeug mit dem behördlichen  Kennzeichen Kennz1 ausgestellt wurden;

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_72`)


Gegen den Zurückweisungsbescheid der belangten Behörde vom 22. März 2023 erhob der  Beschwerdeführer fristgerecht Beschwerde und führte aus, er übersende noch einmal alle  Geschäftszahlen die bis einschließlich 31.03.2023 von Herrn Lenker2 verschuldet worden seien.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_74`)


Herrn Lenker2 zu senden, die für das gegenständliche Kraftfahrzeug mit dem behördlichen  Kennzeichen Kennz1 ausgestellt wurden.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/142210.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142210.1_142`)


Herrn StR Sabine Lenertz, St.Nr. …, betr.

**False Positives:**

- `St` — partial — pred is substring of gold: `StR Sabine Lenertz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `StR Sabine Lenertz`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/144462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144462.1_67`)


Über die diesbezügliche Rücksprache mit der belangten Behörde sei vom steuerlichen  Vertreter am 7. August 2001 ein Aktenvermerk angelegt worden, welchen folgenden Inhalt  habe:  ….“Haben dies mit Herrn Mag. ***, FA Feldkirch am 7. August 2001 nochmals besprochen und  um einen Lösungsvorschlag gebeten: Nach Mag. *** soll die liechtensteinische FA Spittal Villach  eine  Proformarechnung an die RHO Pharma  ausstellen, somit wird die RHO Pharma  zum "Proforma  Verfügungsberechtigten" und kann die abgeführte Einfuhrumsatzsteuer problemlos als  Vorsteuer geltend machen.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `FA Feldkirch`(organisation)
- `FA Spittal Villach`(organisation)
- `RHO Pharma`(organisation)
- `RHO Pharma`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_27`)


Mit Vorlageantrag vom 16.07.2024 wurde die Entscheidung über die Beschwerde durch das  Bundesfinanzgericht beantragt und ergänzend wie folgt begründet:  „[…] Ergänzend zur Beschwerde vom 15.02.2024 wird vorgebracht, dass Herrn Luna Fruechtenicht  Seitens der Pensionsversicherungsanstalt zwischenzeitlich eine Waisenpension zugesprochen  wurde und entsprechend die Erwerbsunfähigkeit infolge Krankheit oder Gebrechens ab der  Kindheit über das 18.

**False Positives:**

- `Luna Fruechtenicht  Seitens` — partial — gold is substring of pred: `Luna Fruechtenicht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Luna Fruechtenicht`(person)
- `Pensionsversicherungsanstalt`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_144`)


Die Wohnverhältnisse von Frau Heumann und Herrn Bf2 waren sowohl vor dem Kauf als auch nach  dem Kauf so gestaltet, dass das erworbene Objekt nicht für eigene Wohnzwecke angedacht  war.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Heumann`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/149391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149391.1_109`)


Zudem wurde vom Geschäftsführer, Herrn Gf., bei der Schlussbesprechung gem § 149 Abs  1 BAO am 12.12.2017 mitgeteilt, dass in Peru keine steuerliche Erfassung der Betriebsstätte  erfolgte, dies wurde auch im Schreiben vom 22.12.2017 bestätigt.

**False Positives:**

- `Gf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Dr_Title` 🏆

**F1:** 0.098 | **Precision:** 0.546 | **Recall:** 0.054  

**Format:** `regex`  
**Rule ID:** `939fe42e`  
**Description:**
Captures 'Dr.' followed by full names, ensuring full name capture including suffixes.

**Content:**
```
\bDr\.(?:in)?\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+LL\.M\.|\s+LLM|\s+MA|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.546 | 0.054 | 0.098 | 183 | 100 | 83 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 100 | 83 | 1751 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/126778.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/126778.1_0`)


GZ. RV/5101724/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht erkennt durch den Richter Dr. Elias Derneden  in der Beschwerdesache über die Beschwerde vom 14.01.2019 gegen den Bescheid der belangten Behörde vom 04.01.2019 betreffend Familienbeihilfe für den Zeitraum ab März 2018 zu Recht: 1.Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elias Derneden` | `Dr. Elias Derneden` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/111123.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/111123.1_0`)


GZ. RV/7101987/2011 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Alexander Hajicek, die Richterin Mag. Helga Hochrieser und die weiteren Senatsmitglieder Mag. Michael Franz und  Mag. Franz Josef Großin der Beschwerdesache des Bf., Adr., gegen die Bescheide des Finanzamtes Baden Mödling vom 12.1.2011, betreffend Einkommensteuer 2000 bis 2008 nach Durchführung einer mündlichen Verhandlung am 21.6.2016 zu Recht erkannt:    Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Alexander Hajicek` | `Dr. Alexander Hajicek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Mag. Michael Franz` (person)
- `Mag. Franz Josef Großin` (person)
- `Finanzamtes Baden Mödling` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/128756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Walter Summersberger in der  Beschwerdesache Emmerich Frydrychowski, Wassertheuer 21, 9112 Gletschach, Österreich, vertreten durch RA Vertreter, über die  Beschwerde vom 16. Juni 2014 gegen den Bescheid des Zollamtes Innsbruck vom 8. Mai 2014  betreffend Aussetzung § 212a BAO zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Walter Summersberger` | `Dr. Walter Summersberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Emmerich Frydrychowski` (person)
- `Wassertheuer 21, 9112 Gletschach, Österreich` (address)
- `Zollamtes Innsbruck` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Thomas Mevis, Lindenhang 30, 4591 Ramsau, Österreich, vertreten durch Sera Trust GmbH, Gablenzgasse 11, 4.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thomas Mevis` (person)
- `Lindenhang 30, 4591 Ramsau, Österreich` (address)
- `Sera Trust GmbH` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Sieglinde Kießerling, Stockenhuberweg 62, 2732 Raglitz, Österreich, vertreten durch MITTEREGGER Steuerberatungs GmbH,  Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 31. August 2019 gegen den Bescheid  des Finanzamtes Waldviertel vom 1. August 2019 betreffend Einkommensteuer 2017  Steuernummer 27-927/6451  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sieglinde Kießerling` (person)
- `Stockenhuberweg 62, 2732 Raglitz, Österreich` (address)
- `MITTEREGGER Steuerberatungs GmbH` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `27-927/6451` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129723.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129723.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  HR OSR Leonie Ercklentz, Karnitzen 135, 9635 Kronhof, Österreich, vertreten durch LKP Steuerberatung OG, Otto Sagmeister-Gasse 3,  2700 Wiener Neustadt, über die Beschwerde vom 22. Mai 2020 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 15. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `HR OSR Leonie Ercklentz` (person)
- `Karnitzen 135, 9635 Kronhof, Österreich` (address)
- `LKP Steuerberatung OG` (organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/129918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in den  Verwaltungsstrafsachen gegen Flora Thierry, Loferstein 65, 3130 Unterwinden, Österreich, wegen den  Verwaltungsübertretungen gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Flora Thierry` (person)
- `Loferstein 65, 3130 Unterwinden, Österreich` (address)
- `Stadt  Wien` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130546.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130546.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Dagmar Gärttner, Bakk. art., Ögererweg 89, 9341 Dielach, Österreich, über die Beschwerde vom  5. November 2019 gegen den Bescheid Zahl MA MA-Zahl1 vom 25.10.2019 betreffend  Verfügung der Zwangsvollstreckung wegen Nichtbezahlung einer rechtskräftig mit  Strafverfügung vom 2.4.2019 verhängten Strafe zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der angefochtene  Bescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dagmar Gärttner, Bakk. art.` (person)
- `Ögererweg 89, 9341 Dielach, Österreich` (address)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Rudolf Bogdanowic, Am Gehrn 3, 9312 Gaming, Österreich, über die Beschwerde vom 9. Februar 2018 gegen den Bescheid des  Finanzamtes Wien 8/16/17 vom 9. Jänner 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 Steuernummer 90-074/8383  nach Durchführung einer  mündlichen Verhandlung am 4. Dezember 2019 und 16. Oktober 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rudolf Bogdanowic` (person)
- `Am Gehrn 3, 9312 Gaming, Österreich` (address)
- `Finanzamtes Wien 8/16/17` (organisation)
- `90-074/8383` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin Mag. Katharina Moravec zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |
| `Dr. Wolfgang Aigner` | `Dr. Wolfgang Aigner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erwin Agneter` (person)
- `Mag. Belinda  Maria Eder` (person)
- `Xaver Plaumert, BEd` (person)
- `Hinterzeile 24, 3483 Wagram am Wagram, Österreich` (address)
- `Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Mag. Katharina Moravec` (person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130918.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch durch den Senatsvorsitzenden Dr. Michael Rauscher und  die weiteren Senatsmitglieder Mag. Franz Glashüttner, Dr. Christian Haid und Mag. Bruno  Sundl im Beisein der Schriftführerin Claudia Schmölzer über die Beschwerden der Heike Dorrenbach,  Schröttenhofweg 38, 4624 Hölking, Österreich  vertreten durch die LBG Steiermark Steuerberatung GmbH, Rathausplatz 3, 8940  Liezen vom 16.08.2019 gegen die Bescheide des Finanzamtes Judenburg Liezen vom  02.08.2019 betreffend Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und  Körperschaftsteuer 2014 bis 2016 zu Recht erkannt:   Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Michael Rauscher` | `Dr. Michael Rauscher` |
| `Dr. Christian Haid` | `Dr. Christian Haid` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Franz Glashüttner` (person)
- `Mag. Bruno  Sundl` (person)
- `Heike Dorrenbach` (person)
- `Schröttenhofweg 38, 4624 Hölking, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/131304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131304.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Jacqueline Dittus, Sausal 90O, 4911 Schönfeld, Österreich, vertreten durch Dkfm. Anton Lammer  Wirtschaftstreuhand GmbH, Oskar-Kokoschka-Straße 8, 3380 Pöchlarn, über die Beschwerde  vom 17. September 2014 gegen den Bescheid des Finanzamtes Amstetten Melk Scheibbs vom  5. September 2014 betreffend Einkommensteuer 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jacqueline Dittus` (person)
- `Sausal 90O, 4911 Schönfeld, Österreich` (address)
- `Anton Lammer  Wirtschaftstreuhand GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131419.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131419.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Joachim Annanias  in der Beschwerdesache VetR Burkhard Krautschenko,  Geizersgraben 6, 2823 Leiding, Österreich, vertreten durch Mag. Susanne Pöltenstein-Rosenegger, als Masseverwalterin,  Schulerstraße 18, 1010 Wien, und JUNIA Wirtschaftstreuhand-Steuerberatungs KG, Hofgasse  18/4, 2361 Laxenburg, als steuerliche Vertretung, betreffend Beschwerde vom 18.04.2018  gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom    26.01.2018, betreffend Haftung Kapitalertragsteuer 2013,   29.01.2018, betreffend Körperschaftsteuer sowie Umsatzsteuer 2013 und 2014, sowie   31.01.2018, betreffend Körperschaftsteuer und Umsatzsteuer 2015  den Beschluss:  I. Die Beschwerde wird gemäß § 278 Abs. 1 lit. a iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Joachim Annanias` | `Dr. Joachim Annanias` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Burkhard Krautschenko` (person)
- `Geizersgraben 6, 2823 Leiding, Österreich` (address)
- `Mag. Susanne Pöltenstein-Rosenegger` (person)
- `JUNIA Wirtschaftstreuhand-Steuerberatungs KG` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Titus Ohlmer` (person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich` (address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-234/9874` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/131454.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131454.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Edwin Pfaefflin, Steinwiese 17, 3683 Nächst Altenmarkt, Österreich, betreffend Beschwerde vom 24. Jänner 2020  gegen die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 8. März 2017 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und vom 23.1.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 35-514/8431,  beschlossen:   Die Vorlageanträge vom 4.5.2020 gegen die Beschwerdevorentscheidung (BVE) 2016 vom  6.2.2020 und vom 8.5.2020 gegen die BVE 2017 werden gemäß § 260 Abs. 1 BAO in  Verbindung mit § 264 Abs. 4 BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Edwin Pfaefflin` (person)
- `Steinwiese 17, 3683 Nächst Altenmarkt, Österreich` (address)
- `Finanzamtes` (organisation)
- `35-514/8431` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/131441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131441.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der Beschwerde- sache KzlR Diethard Ringhand, Unterrans 14, 9821 Unterwolliggen, Österreich, vertreten durch WTIV Steuerberatungsgesellschaft m.b.H.,  Dorfstraße 68, 6364 Brixen/Thale, über die Beschwerden vom 17. September 2015 gegen die  Bescheide des Finanzamtes Braunau Ried Schärding vom 21. August 2015 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer für die Jahre 2009, 2010,  2011, 2012 und 2013 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Diethard Ringhand` (person)
- `Unterrans 14, 9821 Unterwolliggen, Österreich` (address)
- `WTIV Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Braunau Ried` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132098.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132098.1_25`)


Nach dem vorliegenden Beschluss des Bezirksgerichtes Innere Stadt vom 26.11.2010 wurde der  Rechtsanwalt Dr. Burghardt zum Sachwalter gemäß § 268 Abs. 3 Z 2 ABGB bestellt. Der  Sachwalter wurde u.a. für das Aufgabengebiet zur Vertretung vor Ämter und Behörden  bestellt. Die Sachwalterbestellung wirkt insofern konstitutiv, als ab ihrer Wirksamkeit die  Prozess- und Handlungsfähigkeit im dort umschriebenen Ausmaß für den Bf. keinesfalls mehr  gegeben war (VwGH 27.2.2006, 2004/05/0326).

| Predicted | Gold |
|---|---|
| `Dr. Burghardt` | `Dr. Burghardt` |

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132230.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz über die Beschwerde des  Harald Schwalbach, Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich, vom 19. November 2020, gegen die Vollstreckungsverfügung der  belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 6, vom 19. Juni 2019, GZ.  MA67/Zahl/2018, betreffend Zwangsvollstreckung wegen Nichtzahlung der rechtskräftigen  Strafe auf Grund der Strafverfügung vom 4. Dezember 2018, GZ. MA67/Zahl/2018, den  Beschluss gefasst:  I. Die Beschwerde vom 19. November 2020 wird gemäß § 31 iVm §§ 28 und 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Schwalbach` (person)
- `Georg Gottschall-Gasse 14, 4772 Sonnleiten, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 6` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/132442.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Bf, Oberweissburg 52, 4081 Hartkirchen, Österreich, vertreten durch Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH, Raiffeisenplatz 2, 2136 Laa an der Thaya, über die Beschwerde vom 27. Oktober 2014  gegen die Bescheide des Finanzamtes Lilienfeld St. Pölten vom 30. September 2014 betreffend  Einkommensteuer 2009 und 2010 sowie Anspruchszinsen (§ 205 BAO) 2009 und 2010,  Steuernummer 73-948/8864, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oberweissburg 52, 4081 Hartkirchen, Österreich` (address)
- `Krebs & Rudorfer Wirtsch.- u. Stb.  GmbH` (organisation)
- `Finanzamtes Lilienfeld St. Pölten` (organisation)
- `73-948/8864` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/133278.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133278.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Jonas Gutkauf, Auvorstadtgasse 59, 8184 Floing, Österreich, über die Beschwerden vom 10. März 2021 gegen  die Bescheide des Finanzamtes Österreich vom 10. März 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 und Einkommensteuer (Arbeitnehmerveranlagung) 2018  sowie vom 23. Februar 2021 gegen den Bescheid des Finanzamtes Österreich vom 19. Februar  2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Dr. Adebiola Bayer` | `Dr. Adebiola Bayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jonas Gutkauf` (person)
- `Auvorstadtgasse 59, 8184 Floing, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/133143.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133143.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Timothy Overlaender, Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich, über die Beschwerde vom 18. Dezember 2018 gegen den Bescheid  des Finanzamtes Graz-Stadt vom 22. November 2018 betreffend Umsatzsteuer 2015 und  Umsatzsteuer 2016 Steuernummer 51-515/5009  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timothy Overlaender` (person)
- `Kardinal-Innitzer-Straße 57, 9560 Kaidern, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `51-515/5009` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/134767.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134767.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Rauner, die RichterinR  sowie die fachkundigen Laienrichter Gregor Ableidinger und Dr. Franz Kandlhofer in der  Beschwerdesache Lieselotte Schluessel, Hannakstraße 205, 5121 Wimm, Österreich, über die Beschwerde vom 22. Februar 2016  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 10. Februar 2016  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Hans Rauner` | `Dr. Hans Rauner` |
| `Dr. Franz Kandlhofer` | `Dr. Franz Kandlhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gregor Ableidinger` (person)
- `Lieselotte Schluessel` (person)
- `Hannakstraße 205, 5121 Wimm, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Groschedl in der  Beschwerdesache Mittel-Verlag, Am Rothenbühl 45, 4690 Ennsberg, Österreich  vertreten durch Dr. Stephan Riel als  Insolvenzverwalter, Landstraßer Hauptstraße 1 Tür 2, 1030 Wien, über die Beschwerde der  Abgabepflichtigen vom 25. Mai 2021 gegen den Bescheid des Finanzamtes Österreich vom  20. April 2021 betreffend Pfändung einer Geldforderung zur Steuernummer 44-993/1626  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Stephan Riel` | `Dr. Stephan Riel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Mittel-Verlag` (organisation)
- `Am Rothenbühl 45, 4690 Ennsberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `44-993/1626` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/136021.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136021.1_22`)


Insolvenzverwalter ist Dr. Stephan Riel.

| Predicted | Gold |
|---|---|
| `Dr. Stephan Riel` | `Dr. Stephan Riel` |

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/136186.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136186.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Rauner über die Beschwerde des  Pjotr Astore, Karl-Ahrer-Straße 11, 3593 Franzen, Österreich, vom 02. Dezember 2021, gegen das Straferkenntnis der belangten  Behörde, Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde vom 18. November 2021,  Zahl MA67/Zahl1/2021, wegen der Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4  Abs. 2 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr.  71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Rauner` | `Dr. Hans Rauner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pjotr Astore` (person)
- `Karl-Ahrer-Straße 11, 3593 Franzen, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/136197.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina über die Beschwerde des  Juliana Fassmer, Tillisweg 11, 8773 Sparsbach, Österreich, vom 10. Februar 2022, gegen die Straferkenntnisse des  Magistrates der Stadt Wien, Magistratsabteilung 67, vom 31. Jänner 2022, Zlen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juliana Fassmer` (person)
- `Tillisweg 11, 8773 Sparsbach, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Peter Steurer, die Richterin  Mag. Natascha Gassner, die fachkundige Laienrichterin Mag. Renate Burtscher und den  fachkundigen Laienrichter Bernd Feldkircher in der Beschwerdesache Vincent Kohlstruk, Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich,  vertreten durch die Bischof-Fuchs Steuerberatungs GmbH, Dorf Rieden 12, 6900 Bregenz,  gegen den Bescheid des Finanzamtes Bregenz vom 6. Juni 2018 betreffend Einkommensteuer  2017 nach Durchführung einer mündlichen Verhandlung am 21. April 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen;

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Natascha Gassner` (person)
- `Mag. Renate Burtscher` (person)
- `Bernd Feldkircher` (person)
- `Vincent Kohlstruk` (person)
- `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich` (address)
- `Bischof-Fuchs Steuerberatungs GmbH` (organisation)
- `Finanzamtes` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/136694.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136694.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Claire Wienhues, Hörweix 62, 3140 Pottenbrunn, Österreich, vertreten durch TPA Steuerberatung GmbH, Wiedner Gürtel 13 Tür  Turm 24, 1100 Wien, wegen behaupteter Verletzung der Entscheidungspflicht durch das  Finanzamt VG betreffend Körperschaftsteuer 2010 Steuernummer 61-469/1778  zu Recht  erkannt:   I. Der Säumnisbeschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Claire Wienhues` (person)
- `Hörweix 62, 3140 Pottenbrunn, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamt` (organisation)
- `61-469/1778` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/136966.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136966.1_78`)


Ich konnte hierzu noch die Anamnese (Aufnahmeabt.) vom 26.03.2018 Dr. Ilka Danev ausheben  lassen und lege diesen meinem diesem Schreiben ebenfalls bei.

| Predicted | Gold |
|---|---|
| `Dr. Ilka Danev` | `Dr. Ilka Danev` |

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/137251.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137251.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Roland Rößle, Gablitzer Steig 11, 3465 Königsbrunn am Wagram, Österreich, über die Beschwerde des  Beschuldigten vom 7. April 2022 gegen den Zurückweisungsbescheid des Magistrates der Stadt  Wien vom 5. April 2022, Zahl: MA67/216700658355/2021, mit dem der Einspruch vom 18.  Februar 2022 gegen die Strafverfügung vom 3. September 2021 mit derselben Geschäftszahl  gemäß § 49 Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Sebastian Pfeiffer LL.M.` | `Dr. Sebastian Pfeiffer LL.M.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Roland Rößle` (person)
- `Gablitzer Steig 11, 3465 Königsbrunn am Wagram, Österreich` (address)
- `Magistrates der Stadt  Wien` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/137330.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137330.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Juri Boyarzyn, Franz-Xaver-Müller-Straße 146, 3342 Thann, Österreich, vom 28. Juli 2020, gegen den Bescheid des Finanzamtes Österreich  vom 16. Juli 2020, betreffend Familienbeihilfe 01.2019-01.2021, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juri Boyarzyn` (person)
- `Franz-Xaver-Müller-Straße 146, 3342 Thann, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Anton Böckamp, Bakk. techn., Leopold Kunschak Gasse 25, 9343 Dielach, Österreich, über die Beschwerde vom 8. Dezember 2020 gegen den Bescheid  des Finanzamtes Österreich (vormals Finanzamt Gänserndorf Mistelbach, § 323b BAO) vom  25. November 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 84-669/5568  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO im Sinne des Beschwerdebegehrens  abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Anton Böckamp, Bakk. techn.` (person)
- `Leopold Kunschak Gasse 25, 9343 Dielach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Gänserndorf Mistelbach` (organisation)
- `84-669/5568` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/137535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Julian Egiede, Theras 97, 4565 Haselbäckau, Österreich, vertreten durch Mag. Grün  Steuerberatungsgesellschaft mbH, Stiegengasse 1, 9300 St. Veit an der Glan, über die  Beschwerde vom 08. Juni 2018 gegen den Bescheid des Finanzamtes Klagenfurt (nunmehr  Finanzamt Österreich, vertreten durch Mag. Michael Sablatnik, vom 16. Mai 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 Steuernummernummer 88-033/6865  zu Recht:   Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Julian Egiede` (person)
- `Theras 97, 4565 Haselbäckau, Österreich` (address)
- `Mag. Grün  Steuerberatungsgesellschaft mbH` (organisation)
- `Finanzamtes Klagenfurt` (organisation)
- `Finanzamt Österreich` (organisation)
- `Mag. Michael Sablatnik` (person)
- `88-033/6865` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_13`)


Schreiben des Rechtsanwaltes Dr. Karl RA1 (NÖ) an das FA (23. Dezember 2018):  Da das Unternehmensserviceportal für uns dzt nicht zugänglich ist, erlauben wir uns auf diesem  Wege den wirtschaftlichen Eigentümer der Dario Kobben  mit Dr. Karl RA1 bekanntzugeben.

| Predicted | Gold |
|---|---|
| `Dr. Karl` | `Dr. Karl` |
| `Dr. Karl` | `Dr. Karl` |

**Missed by this rule (FN):**

- `Dario Kobben` (person)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_24`)


Da die Einführung des  Unternehmensserviceportals ohne entsprechende Begleitmaßnahmen, wie Information und  Schulung, dessen Bedienung dem Rechtssuchenden vorgesetzt wurde, ein Zugang und eine  Bedienung ohne Hilfe der Finanzbehörden nicht möglich ist und war, wurde mit  rekommandierten Schreiben vom 23.12.2018 dem FA Wien 1/23  bekanntgegeben, dass der  wirtschaftliche Eigentümer der Dario Kobben  Dr. Karl RA1 ist (siehe beigeschlossenes Schreiben  2 von 16 Seite 3 von 16

| Predicted | Gold |
|---|---|
| `Dr. Karl` | `Dr. Karl` |

**Missed by this rule (FN):**

- `FA Wien 1/23` (organisation)
- `Dario Kobben` (person)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_36`)


Zur gemeinsamen mündlichen Verhandlung (Streitsachen: 1. und 2. Zwangsstrafe) erscheinen  zwei Rechtanwälte, Herr Dr. Karl RA1, der auch als Geschäftsführer der Bf. eingetragen ist, und  Herr RA2.

| Predicted | Gold |
|---|---|
| `Dr. Karl` | `Dr. Karl` |

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_40`)


Anmerkungen: Ein „Dr. Karl RA1“ mit Adresse in NÖ ist dem Postzusteller unbekannt ist.

| Predicted | Gold |
|---|---|
| `Dr. Karl` | `Dr. Karl` |

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_41`)


Die  Ladung zur Verhandlung, adressiert an Dr. Karl RA1, mit der Adresse in NÖ wurde von der Post  nicht als verzogen, sondern als unbekannt zurückgestellt. Ein RA Dr. Karl RA1 in NÖ brachte die  Beschwerden zur ersten und zweiten Zwangsstrafe ein (8.2.2019 und 28.5.2019).

| Predicted | Gold |
|---|---|
| `Dr. Karl` | `Dr. Karl` |

**Missed by this rule (FN):**

- `RA Dr. Karl` (person)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_44`)


Auf dem Ausweis von RA1, ausgestellt von der RA-Kammer, wird ein Dr. Karl  RA1 ausgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Karl` | `Dr. Karl` |

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_48`)


Im zentralen  Melderegister scheint ein Dr. Karl RA1 ab 2010 mit der Adresse AdresseWien auf (mit  3 von 16 Seite 4 von 16

| Predicted | Gold |
|---|---|
| `Dr. Karl` | `Dr. Karl` |

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_82`)


Von STB2, gesendet Mittwoch, 6. Oktober 2021:   S.g. Herr BMF2, mit Dank für Ihre Hilfsbereitschaft möchte ich als ehemaliger Mitarbeiter der  FV und Freund des früheren Sektionschefs Dr. Nolz doch festhalten: Das von wem immer  erzwungene WiEReg ist nicht ganz gelungen!

| Predicted | Gold |
|---|---|
| `Dr. Nolz` | `Dr. Nolz` |

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_195`)


Mit Schreiben des RA Dr. Karl RA1 in NÖ vom 23. Dezember 2018 an das FA wurde von der Bf.  in Briefform bekannt gegeben, dass der wirtschaftlicher Eigentümer der Bf. „Dr. Karl RA1“ ist.

| Predicted | Gold |
|---|---|
| `Dr. Karl` | `Dr. Karl` |

**Missed by this rule (FN):**

- `RA Dr. Karl` (person)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_238`)


Anzumerken ist, dass ein Dr. Karl RA1  (Jahrgang XYZ) zumindest seit 1981 mit diversen Haupt- und Nebenwohnsitzen im  Melderegister aufscheint, ab 2010 mit der Adresse AdresseWien als Hauptwohnsitz.

| Predicted | Gold |
|---|---|
| `Dr. Karl` | `Dr. Karl` |

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Volkmar Quadfasel, Forstbergstraße 5, 4144 Zanklbach, Österreich, vertreten durch Dr. Sebastian Mariano Volkmar Lenz,  Laurenzerberg 1, 1010 Wien, vom 25. April 2021, gegen den Bescheid des Finanzamtes  Österreich vom 26. März 2021, betreffend Abweisung des Antrages auf Gewährung des  Erhöhungsbetrages zur Familienbeihilfe ab Dezember 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Volkmar Quadfasel` (person)
- `Forstbergstraße 5, 4144 Zanklbach, Österreich` (address)
- `Dr. Sebastian Mariano Volkmar Lenz` (person)
- `Finanzamtes  Österreich` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/137810.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137810.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Alois Pichler in der Beschwerdesache  Maximiliane Gasparetti, Gschwandtkopf 12, 9330 Althofen, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH, Porzellangasse 51,  1030 Wien, über die Beschwerde vom 23. Dezember 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 17. November 2016 betreffend  1.

| Predicted | Gold |
|---|---|
| `Dr. Alois Pichler` | `Dr. Alois Pichler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Maximiliane Gasparetti` (person)
- `Gschwandtkopf 12, 9330 Althofen, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/138073.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138073.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Richard Reithmayer, Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Bundesstraße  36, 6923 Lauterach, gegen die Bescheide des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) betreffend Einkommensteuer 2015 und 2016 sowie Festsetzung von  Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Richard Reithmayer` (person)
- `Siegfried-Fußenegger-Straße 21, 8132 Kirchdorf, Österreich` (address)
- `Mag. Ghesla Steuerberater GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/138386.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138386.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank  in der Beschwerdesache Nicoletta Nipshagen, Obergrafendorfer Straße 11, 9141 Oberburg, Österreich,  über die Beschwerde vom 1. Mai 2021 gegen den Einkommensteuerbescheid  (Arbeitnehmerveranlagung) für das Jahr 2020 des Finanzamtes Österreich vom 26. April 2021,  Steuernummer 02-339/1714, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Helga Woschank` | `Dr. Helga Woschank` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nicoletta Nipshagen` (person)
- `Obergrafendorfer Straße 11, 9141 Oberburg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `02-339/1714` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/138952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138952.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Paolo Blasenbreu, Ernst-Ludwig-Gasse 176, 7461 Allersgraben, Österreich, gegen die Bescheide des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019, 64-737/5163, beschlossen:   Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Paolo Blasenbreu` (person)
- `Ernst-Ludwig-Gasse 176, 7461 Allersgraben, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)
- `64-737/5163` (tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Cornelia Reifgerste, Scherzergütl 18K, 9622 Golz, Österreich, vertreten durch Freimüller Rechtsanwalts GmbH, 1010 Wien,  Kleeblattgasse 13/11A, vom 26. August 2020, gegen den Bescheid des Finanzamtes Österreich  vom 28. Juli 2020, betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe für M. F. ab November 2019, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cornelia Reifgerste` (person)
- `Scherzergütl 18K, 9622 Golz, Österreich` (address)
- `Freimüller Rechtsanwalts GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `M. F.` (person)

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/139657.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139657.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek über die Beschwerde des  Lubomir Vaist, Sulzbachfelderstraße 3, 9361 Judendorf, Österreich, vom 4. Jänner 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 12. Oktober 2022, GZ. MA67/Zahl/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lubomir Vaist` (person)
- `Sulzbachfelderstraße 3, 9361 Judendorf, Österreich` (address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/140157.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Dr. Sebastian Pfeiffer LL.M. in der  Verwaltungsstrafsache gegen Annette Preußing, Am Neufeldersee 40, 3385 Uttendorf, Österreich, über die Beschwerde des  Beschuldigten vom 23. Jänner 2023 gegen den Zurückweisungsbescheid des Magistrates der  Stadt Wien vom 18. Jänner 2023, Zahl MA67/Zahl/2022, mit dem der Einspruch vom 6. Jänner  2023  gegen die Strafverfügung vom 4. Oktober 2022 mit derselben Geschäftszahl gemäß § 49  Abs. 1 VStG als verspätet zurückgewiesen wurde, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und der  angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Sebastian Pfeiffer LL.M.` | `Dr. Sebastian Pfeiffer LL.M.` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annette Preußing` (person)
- `Am Neufeldersee 40, 3385 Uttendorf, Österreich` (address)
- `Magistrates der  Stadt Wien` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/141318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141318.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Lara Blaßl, Singsdorf 15, 9622 St. Lorenzen im Gitschtal, Österreich, vertreten durch Dr. Michl Münzker, Landskrongasse 5 Tür 4, 1010  Wien, über die Beschwerde vom 24. Juni 2021 gegen den Bescheid des Finanzamtes Österreich  vom 17. Juni 2021 betreffend Festsetzung einer Zwangsstrafe, Steuernummer  54-324/8831, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lara Blaßl` (person)
- `Singsdorf 15, 9622 St. Lorenzen im Gitschtal, Österreich` (address)
- `Dr. Michl Münzker` (person)
- `Finanzamtes Österreich` (organisation)
- `54-324/8831` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/141414.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141414.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Dr.in Mag.a Elisabeth Wiedenhöfft, LLM, Hirschberg 29, 2870 Guggendorf, Österreich, über die Beschwerde vom 11. November 2021 gegen den Bescheid  des Finanzamtes Österreich vom 5. Oktober 2021 betreffend Antrag auf Bewilligung der  Aussetzung § 212a BAO 2021, Steuernummer 16-471/8115  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Susanne Zankl` | `Dr. Susanne Zankl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Mag.a Elisabeth Wiedenhöfft, LLM` (person)
- `Hirschberg 29, 2870 Guggendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `16-471/8115` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/141710.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Barbara Straka in der Verwaltungsstraf- sache gegen Imre Bschorer, Karchham 233Q, 2733 Hornungstal, Österreich, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006, über die  Beschwerde des Beschuldigten vom 26. Juli 2023 gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 24. Juli 2023, GZ. MA67/Zahl/2023, zu Recht  erkannt:  Der Beschwerde wird gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24  Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorgani- sationsrecht (WAOR) insoweit Folge gegeben, als die verhängte Geldstrafe von 60,00 € auf  36,00 € und die für den Fall der Uneinbringlichkeit mit 14 Stunden festgesetzte Ersatzfreiheits- strafe auf 8 Stunden herabgesetzt wird.

| Predicted | Gold |
|---|---|
| `Dr. Barbara Straka` | `Dr. Barbara Straka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Imre Bschorer` (person)
- `Karchham 233Q, 2733 Hornungstal, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/142233.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142233.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Silke Czejka, Oberes Heustadelwasser 23N, 2033 Kleinsierndorf, Österreich, vom 01. September 2022 gegen den Bescheid des Finanzamtes  Österreich vom 30. August 2022 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbetrag für den Monat Mai 2022, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silke Czejka` (person)
- `Oberes Heustadelwasser 23N, 2033 Kleinsierndorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 1. April 2022 zuständigen Richter Dr. Hans Blasina  in der Beschwerdesache Uwe Gudian, Tschrestal 27, 4150 Rohrbach, Österreich, über die Berufungen (nunmehr  Beschwerden, § 323 Abs 38 BAO) (1.) vom 15. Jänner 2013 gegen die Bescheide des FA Wien  9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich, § 323b BAO) vom 20. Dezember 2012  betreffend Feststellung und Nichtfeststellung von Einkünften 2009-2010 und gegen die  „Bescheide“ vom 19. Dezember 2012 betreffend Feststellung und Nichtfeststellung von  Einkünften sowie (2.) vom 24. Juli 2013 gegen den Bescheid des FA Wien 9/18/19  Klosterneuburg (nunmehr Finanzamt Österreich, § 323b BAO) vom 20. Juni 2013 betreffend  Feststellung und Nichtfeststellung von Einkünften 2011 und gegen den „Bescheid“ vom 27. Juni  2013 betreffend Feststellung von Einkünften 2011, Steuernummer 37-861/1218  zu Recht  erkannt:   I. zu Recht erkannt: Die angefochtenen Bescheide vom 20. Dezember 2012 sowie jener vom 20.  Juni 2013 werden gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Uwe Gudian` (person)
- `Tschrestal 27, 4150 Rohrbach, Österreich` (address)
- `FA Wien  9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Österreich` (organisation)
- `FA Wien 9/18/19  Klosterneuburg` (organisation)
- `Finanzamt Österreich` (organisation)
- `37-861/1218` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/106919.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/106919.1_0`)


GZ. RV/7105376/2014 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Hedwig Bavenek-Weber in der Beschwerdesache Saligergasse 1, 3300 Haag Dorf, Österreich, gegen den Bescheid des Finanzamtes Baden Mödling vom 8. Oktober 2014 über die Zurücknahme der Beschwerde (vom 2. August 2014) zu Recht erkannt: Der Zurücknahmebescheid (vom 8. Oktober 2014) und der Mängelbehebungsauftrag  (vom 29. August 2014) werden (ersatzlos) aufgehoben.

**False Positives:**

- `Dr. Hedwig Bavenek` — partial — pred is substring of gold: `Mag.Dr. Hedwig Bavenek-Weber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Hedwig Bavenek-Weber`(person)
- `Saligergasse 1, 3300 Haag Dorf, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Dr. Thomas Keppert Steuerberatung` — positional overlap with gold: `Prof. Dr. Thomas Keppert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich`(address)
- `Maximilian Jasper`(person)
- `Wetzles 9, 3243 Lunzen, Österreich`(address)
- `Prof. Dr. Thomas Keppert`(person)
- `Leroy Kusznierz`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Titus Ohlmer, Gaisruckdorf 2, 3950 Kleineibenstein, Österreich, vertreten durch ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft, St Veit-Gasse 8, 1130 Wien, über die Beschwerde der  beschwerdeführenden Partei vom 9.4.2018 wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf betreffend  Umsatzsteuer 2015 und 2016, Steuernummer 20-234/9874, beschlossen:  Die Säumnisbeschwerde wird unter analoger Anwendung des § 261 Abs 1 BAO für  gegenstandlos erklärt und das Säumnisbeschwerdeverfahren eingestellt.  Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) unzulässig.

**False Positives:**

- `Dr. Nikolaus` — partial — pred is substring of gold: `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Titus Ohlmer`(person)
- `Gaisruckdorf 2, 3950 Kleineibenstein, Österreich`(address)
- `ÖBUG Dr. Nikolaus WT KG  Steuerberatungsgesellschaft`(organisation)
- `Finanzamt Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `20-234/9874`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131751.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131751.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Gregor Klocksin, Unterguntschach 85, 3525 Armschlag, Österreich, über die Beschwerde vom 8. Jänner 2019 gegen  die Bescheide des Finanzamtes Amstetten Melk Scheibbs vom 11. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (§ 303 BAO) hinsichtlich Einkommensteuer 2012 und  Anspruchszinsen (§ 205 BAO) 2012 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Gregor Klocksin`(person)
- `Unterguntschach 85, 3525 Armschlag, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Frauke Galleithner, Hovenweg 222, 5412 Hinterwiestal, Österreich, über die Beschwerde vom 13. Mai 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 25. April 2016 betreffend  Umsatzsteuer und Einkommensteuer 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Frauke Galleithner`(person)
- `Hovenweg 222, 5412 Hinterwiestal, Österreich`(address)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132366.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132366.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Timon Thoennißen, Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in  Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF.  LGBl. für Wien Nr. 71/2018, über die Beschwerde des Beschuldigten vom 24. Februar 2021  gegen das Erkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom 26. Jänner  2021, Zahl MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insofern  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 iVm § 45 Abs. 1 letzter Satz VStG von der Verhängung  einer Strafe abgesehen und der Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit  seines Verhaltens eine Ermahnung erteilt wird.

**False Positives:**

- `Dr. Adam Müller` — partial — pred is substring of gold: `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Timon Thoennißen`(person)
- `Dr. Adam Müller-Guttenbrunn-Straße 41, 4822 Steeg, Österreich`(address)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde von Lieselotte Reinicker, Raingasse 32, 9552 Ossiachberg, Österreich  vertreten durch Dr. X, Adr. vom 10. Dezember  2020 gegen die Bescheide des Finanzamtes Salzburg - Stadt (nunmehr FA Österreich) vom 6.  November 2020 betreffend Einkommensteuer 2015 bis 2018 beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b der Bundesabgabenordnung (BAO) als verspätet  zurückgewiesen.

**False Positives:**

- `Dr. Maria` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Lieselotte Reinicker`(person)
- `Raingasse 32, 9552 Ossiachberg, Österreich`(address)
- `Dr. X`(person)
- `Finanzamtes`(organisation)
- `FA Österreich`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/134001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lee Kubbig, Kleinnondorf 6, 4843 Innerleiten, Österreich, über die Beschwerde vom 10. Februar 2019  gegen den Bescheid des Finanzamtes Österreich vom 31. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lee Kubbig`(person)
- `Kleinnondorf 6, 4843 Innerleiten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_146`)


An der EnnsTouristik Consulting GmbH waren im Streitzeitraum beteiligt:  28.000…..HGesellschaft BFK Baugesellschaft mbH & Co KG  (jedenf. 1.1.08-27.9.11)  25.900…..BFK Holding GmbH ab 28.9.2011  3.500……..Dr. Christian W1 (1.1.2008-31.7.2011)  3.500……..Dr. Christian W2 (1.1.2008-31.7.2011)  7.000..……zweiter Stratege ( jedenfalls ab 1.8.2011-27.9.2011)  10 von 38 Seite 11 von 38

**False Positives:**

- `Dr. Christian` — no gold match — likely missing annotation
- `Dr. Christian` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `EnnsTouristik Consulting GmbH`(organisation)
- `BFK Baugesellschaft mbH & Co KG`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_145`)


Ein Gespräch mit Hern OA Dr.  Bieber bezüglich des weiteren psychotherapeutischen Procedere wurde vor der Entlassung  durchgeführt.“

**False Positives:**

- `Dr.  Bieber` — partial — pred is substring of gold: `OA Dr.  Bieber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OA Dr.  Bieber`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/136451.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136451.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Peter Steurer, die Richterin  Mag. Natascha Gassner, die fachkundige Laienrichterin Mag. Renate Burtscher und den  fachkundigen Laienrichter Bernd Feldkircher in der Beschwerdesache Vincent Kohlstruk, Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich,  vertreten durch die Bischof-Fuchs Steuerberatungs GmbH, Dorf Rieden 12, 6900 Bregenz,  gegen den Bescheid des Finanzamtes Bregenz vom 6. Juni 2018 betreffend Einkommensteuer  2017 nach Durchführung einer mündlichen Verhandlung am 21. April 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen;

**False Positives:**

- `Dr. Mehes` — partial — pred is substring of gold: `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Peter Steurer`(person)
- `Mag. Natascha Gassner`(person)
- `Mag. Renate Burtscher`(person)
- `Bernd Feldkircher`(person)
- `Vincent Kohlstruk`(person)
- `Dr. Mehes-Gasse 50, 7202 Pöttsching, Österreich`(address)
- `Bischof-Fuchs Steuerberatungs GmbH`(organisation)
- `Finanzamtes`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/136638.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136638.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ludger Endel, Kleinsierning 2, 5114 Mittergöming, Österreich, betreffend Beschwerde vom 15. Dezember 2021  gegen den Bescheid des Finanzamtes Österreich vom 2. Februar 2022 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 63-868/1042,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ludger Endel`(person)
- `Kleinsierning 2, 5114 Mittergöming, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `63-868/1042`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/136792.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136792.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Jeanne Stockhorst, Fridrichallee 42, 4084 Scheiblberg, Österreich  über die Beschwerde vom 5. Dezember 2006  gegen den Bescheid des Finanzamtes Lilienfeld St. Pölten vom 17. November 2006 betreffend  Einkommensteuer 2000, Steuernummer 22-242/2984, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Jeanne Stockhorst`(person)
- `Fridrichallee 42, 4084 Scheiblberg, Österreich`(address)
- `Finanzamtes Lilienfeld St. Pölten`(organisation)
- `22-242/2984`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/137293.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137293.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi über die am 25. Mai 2022 eingebrachte  Beschwerde von Elvira Akcakaya, Dr. Ludwig-Straße 12, 4184 Neuling, Österreich, Firmenbuchnummer FN gegen die an  Beschuldigte gerichtete Vollstreckungsverfügung des Magistrates der Stadt Wien (MA 6 – BA  32) vom 18. Mai 2022, Zahl MA67/Zahl/2021, beschlossen:  Gemäß § 50 in Verbindung mit (iVm) § 31 Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm  § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) wird  die Beschwerde als unzulässig zurückgewiesen.

**False Positives:**

- `Dr. Ludwig` — partial — pred is substring of gold: `Dr. Ludwig-Straße 12, 4184 Neuling, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Elvira Akcakaya`(person)
- `Dr. Ludwig-Straße 12, 4184 Neuling, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_14`)


Vergl. hierzu “Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Dr. Franz Leidenmühler` — partial — pred is substring of gold: `Prof. Dr. Franz Leidenmühler`
- `Dr. Heidi Pacher` — partial — pred is substring of gold: `MR Dr. Heidi Pacher`
- `Dr. Juliane Bogner Strauß` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_16`)


Anmerkung:   Die Grundlage für das Gesetz zur Indexierung von Familienleistungen basiert auf einem  “Rechtsgutachten zur Neugestaltung der Familienbeihilfe für Kinder, die im EU-Ausland leben  für das BM für Finanzen, erstattet von Univ.-Prof. Dr. Wolfgang Mazal Wien, den 20. Februar  2017”.

**False Positives:**

- `Dr. Wolfgang Mazal Wien` — positional overlap with gold: `Univ.-Prof. Dr. Wolfgang Mazal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BM für Finanzen`(organisation)
- `Univ.-Prof. Dr. Wolfgang Mazal`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/137536.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137536.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Gisbert Löhberg, Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich, vertreten durch Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH, Freistädter Straße 307, 4040 Linz, über die Beschwerde vom  11. Februar 2019 gegen den Bescheid des Finanzamtes Linz (nunmehr Finanzamtes Österreich )  vom 14. Jänner 2019 betreffend Einkommensteuer 2015 Steuernummer 73-737/2281  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Josef Schlager  Wirtschaftstreuhand Gmb` — partial — pred is substring of gold: `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Walter Aiglsdorfer`(person)
- `Gisbert Löhberg`(person)
- `Conrad-von-Hötzendorf-Straße 2, 9341 Gunzenberg, Österreich`(address)
- `Prof. Dr. Josef Schlager  Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Linz`(organisation)
- `Finanzamtes Österreich`(organisation)
- `73-737/2281`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_41`)


Die  Ladung zur Verhandlung, adressiert an Dr. Karl RA1, mit der Adresse in NÖ wurde von der Post  nicht als verzogen, sondern als unbekannt zurückgestellt. Ein RA Dr. Karl RA1 in NÖ brachte die  Beschwerden zur ersten und zweiten Zwangsstrafe ein (8.2.2019 und 28.5.2019).

**False Positives:**

- `Dr. Karl` — similar text (different position): `Dr. Karl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Karl`(person)
- `RA Dr. Karl`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_42`)


Ein RA Dr.  Carl RA1 mit identer Adresse in NÖ und identer Handynummer brachte hingegen für die Bf. die  Vorlageanträge (1.4.2019 und 16.8.2019) ein.

**False Positives:**

- `Dr.  Carl` — partial — pred is substring of gold: `RA Dr.  Carl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr.  Carl`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_43`)


Sowohl RA Dr. Carl RA1 als auch RA Dr. Karl RA1  verweisen in ihren Eingaben auf die jeweils nach § 8 RAO erteilte Vollmacht (ohne  Einschränkungen).

**False Positives:**

- `Dr. Carl` — partial — pred is substring of gold: `RA Dr. Carl`
- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. Carl`(person)
- `RA Dr. Karl`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_45`)


Im Internet scheint sowohl ein RA Dr. Karl RA1 als auch ein RA Dr. Carl RA1  mit der Adresse „AdresseKurz“ in Wien auf.

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`
- `Dr. Carl` — partial — pred is substring of gold: `RA Dr. Carl`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. Karl`(person)
- `RA Dr. Carl`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_195`)


Mit Schreiben des RA Dr. Karl RA1 in NÖ vom 23. Dezember 2018 an das FA wurde von der Bf.  in Briefform bekannt gegeben, dass der wirtschaftlicher Eigentümer der Bf. „Dr. Karl RA1“ ist.

**False Positives:**

- `Dr. Karl` — similar text (different position): `RA Dr. Karl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. Karl`(person)
- `Dr. Karl`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_233`)


Solchen Parteienvertretern und allfälligen hilfeleistenden Ansprechpersonen (wie im  BMF/Registerbehörde) müssen aber seitens der Bf. korrekte Auskünfte über wahrscheinliche  Datenprobleme bei Einträgen geben werden, wie den unterschiedlichen Erfassungen und  Schreibweisen der Vornamen Karl und Carl, unter denen u.a. Eingaben an das FA getätigt  wurden (vgl. angeführte Beschwerdeschriften und Vorlageanträge der Bf., abwechselnd  eingebracht durch RA Dr. Karl RA1 und RA Dr. Carl RA1, u.a. mit identer Adresse in NÖ, identer  Handynummer im Briefkopf, identen Bankverbindungen und identer Kurzparaphe) oder  13 von 16 Seite 14 von 16

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`
- `Dr. Carl` — partial — pred is substring of gold: `RA Dr. Carl`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `BMF/Registerbehörde`(organisation)
- `RA Dr. Karl`(person)
- `RA Dr. Carl`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_235`)


Auch im Internet  scheint sowohl ein RA Dr. Karl RA1 als auch ein RA Dr. Carl RA1 mit identen Adresse an der  Adresse der Bf. auf (AdresseKurz).

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`
- `Dr. Carl` — partial — pred is substring of gold: `RA Dr. Carl`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. Karl`(person)
- `RA Dr. Carl`(person)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/137544.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137544.1_252`)


RA Dr. Karl RA1 (Personenidentität: Berufsmäßiger Parteienvertreter der Bf., Geschäftsführer  der Bf. und wirtschaftlicher Eigentümer der Bf.) verwies in der Beschwerdeschrift (mit damalig  angegebener Adresse in NÖ, Adresse nicht mehr aktuell laut Bekanntgabe in mündlicher  Verhandlung) auf die nach § 8 RAO erteilte Vollmacht (ohne ersichtliche Einschränkungen).

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `RA Dr. Karl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `RA Dr. Karl`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_4`)


Dr. Dok1, Fachgebiet Allgemeinmedizin, erstellte nach Untersuchung von S. am 2. März 2021  folgendes Gutachten:  Anamnese:  Schwangerschaft und Geburt unauffällig  TE und Paukenröhrchen;

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_79`)


Die Bf. brachte am 25. August 2021 folgenden Vorlageantrag ein:  „In der Beschwerdevorentscheidung vom 20.07.2021 wird unter Zugrundelegung des  Sachverständigengutachtens von Dr. Dok1, der Allgemeinmediziner ist, davon ausgegangen,  dass bei S. X. keine Behinderung vorliegt: Der Sachverständige kommt zum Schluss, dass „kein  Grad der Behinderung zu ermitteln" wäre.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_85`)


Entgegen der Schlussfolgerung im Sachverständigengutachten von Dr. Dok1 ist der Umstand,  dass keine Therapien und keine ärztliche Verlaufsdokumentation vorgelegt wurden, nicht  geeignet darauf zu schließen, dass keine Behinderung vorliegt!

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_91`)


Entgegen den Ausführungen im Sachverständigengutachten von Dr. Dok1 haben sehr wohl  Therapien stattgefunden.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_92`)


Es wird auch darauf hingewiesen, dass die diagnostizierte Erkrankung  einen Dauer- bzw. Endzustand darstellt und daher das Ergebnis des  Sachverständigengutachtens von Dr. Dok1, dass die Diagnose nicht vorliege und auch kein Grad  der Behinderung gegeben wäre, in einem diametralen Widerspruch (den es im Ermitt- lungsverfahren aufzuklären gilt) zur klinisch fachspezifischen Diagnose steht.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_109`)


Im Gutachten vom 2. März 2021 stellte Dr. Dok1, Fachgebiet Allgemeinmedizin, keinen Grad  der Behinderung fest.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_167`)


Erst im Vorschulalter fallen Schwierigkeiten auf (u. a.  Kontaktprobleme, wiederkehrende Verhaltensmuster, Missachten von Regeln beim Spielen  etc.) (https://focus-arztsuche.de/magazin/krankheiten/psychische-erkrankungen/was-ist-das- asperger-syndrom-und-wie-erkennt-man-es )  Im Gutachten vom 2. März 2021 stellte Dr. Dok1, Fachgebiet Allgemeinmedizin, keinen Grad  der Behinderung fest, dies mit der Begründung, dass zwar gutachterliche Diagnosen gestellt  worden seien, jedoch mangels Inanspruchnahme adäquater Therapien, eine, für die  Beurteilung alltagsrelevanter, anhaltender Einschränkungen erforder-liche, ärztliche  Verlaufsdokumentation, nicht vorhanden sei.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_14`)


Vergl. hierzu “österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Dr. Franz Leidenmühler` — partial — pred is substring of gold: `Prof. Dr. Franz Leidenmühler`
- `Dr. Heidi Pacher` — partial — pred is substring of gold: `MR Dr. Heidi Pacher`
- `Dr. Juliane Bogner Strauß` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_16`)


Anmerkung:   Die Grundlage für das Gesetz zur Indexierung von Familienleistungen basiert auf einem  “Rechtsgutachten zur Neugestaltung der Familienbeihilfe für Kinder, die im EU-Ausland leben  für das BM für Finanzen, erstattet von Univ.-Prof. Dr. Wolfgang  Mazal Wien, den 20. Februar  2017”.

**False Positives:**

- `Dr. Wolfgang  Mazal Wien` — positional overlap with gold: `Univ.-Prof. Dr. Wolfgang  Mazal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BM für Finanzen`(organisation)
- `Univ.-Prof. Dr. Wolfgang  Mazal`(person)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/138662.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138662.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Maurice Kämpfel, Leuzendorfgasse 8, 5660 Eschenau, Österreich, betreffend Beschwerden vom 9. März 2022  gegen die Bescheide des Finanzamtes Österreich vom 21. Oktober 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2018 und Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 93-599/8471  beschlossen:  Die Beschwerden werden gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Maurice Kämpfel`(person)
- `Leuzendorfgasse 8, 5660 Eschenau, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `93-599/8471`(tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_138`)


M. wurde auf Grund der Beschwerde am 6. November 2021 ein weiteres Mal untersucht und  von Dr. Dok2 folgendes Gutachten erstellt:  "Anamnese:  letzte Begutachtung 7-2020 mit 30% wegen Asperger Syndrom  Nun Einspruch da sich ihr Zustand verschlechtert hätte  Schwangerschaft und Geburt unauffällig, nach der Geburt Unruhe und weinen aufgefallen, sie  hätte viel geweint.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)
- `Dr. Dok2`(person)

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_219`)


Im Gutachten vom 6. November 2020 stellte Dr. Dok2, Arzt für Allgemeinmedizin, ebenfalls die  Diagnose Asperger Syndrom und reihte die Erkrankung unter die Pos.Nr. 03.04.01 mit einem  Grad der Behinderung von 30 vH.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok2`(person)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_220`)


Dr. Dok2 wählte, wie schon Dr. Dok1, 2 Stufen über dem unteren Rahmensatz, da eine mäßige  Einschränkung der sozialen Fähigkeiten und die Absolvierung eines Studiums möglich sei.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`
- `Dr. Dok` — similar text (different position): `Dr. Dok2`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok2`(person)
- `Dr. Dok1`(person)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_282`)


Dem mit dem zweiten Gutachten betrauten Sachverständigen, Dr. Dok2, Arzt für Allge- meinmedizin, lagen bei der Erstellung seines Gutachtens vom 6. November 2020 folgende  Befunde bzw. Unterlagen vor:  2020-11 Mag.a P., Psychologin: es liegt ein Befund für eine Autismus Spektrum Störung vor,  erhöhte Belastung und Stresssymptomatik, Angstreaktionen und depressive Symptomatik als  Konsequenz, bei mir in psychotherapeutischer Behandlung.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok2`(person)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_289`)


akustische Differen- zierungsschwäche  Dr. Dok2 reihte die Erkrankung, übereinstimmend mit Dr. Dok1, unter die Pos.Nr. 03.04.01 mit  einem Grad der Behinderung von 30 vH. und bescheinigte ebenfalls keine Erwerbsunfähigkeit,  dies mit der Begründung, dass keine zweifelsfrei dokumentierte Gesundheitsschädigung  vorliege, die die dauernde Unfähigkeit, sich selbst den Unterhalt zu verschaffen, zur Folge  habe.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`
- `Dr. Dok` — similar text (different position): `Dr. Dok2`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok2`(person)
- `Dr. Dok1`(person)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/139620.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139620.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch Dr. Mag. Elmar Ebertz  in der Beschwerdesache Karlheinz Abke,  Schindlauerweg 53, 2392 Dornbach, Österreich  vertreten durch MedR Anneliese Naupert, Bakk. art., über die Beschwerde vom 30. Mai 2022 gegen den  Bescheid des Finanzamtes Österreich vom 27. April 2022, mit dem das Stundungsansuchen  vom 29. März 2022 abgewiesen wurde, Steuernummer 69-865/2288, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. Elmar Ebertz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Mag. Elmar Ebertz`(person)
- `Karlheinz Abke`(person)
- `Schindlauerweg 53, 2392 Dornbach, Österreich`(address)
- `MedR Anneliese Naupert, Bakk. art.`(person)
- `Finanzamtes Österreich`(organisation)
- `69-865/2288`(tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/139621.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139621.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Silvana Hellfritz, Reibersweg 24, 8144 Unterpremstätten, Österreich, betreffend Beschwerde vom 31. Jänner 2021  gegen den Bescheid des Finanzamtes Österreich vom 12. Jänner 2021 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 69-424/6198  beschlossen:   Der Vorlageantrag wird gemäß § 264 Abs 4 lit e Bundesabgabenordnung (BAO) in Verbindung  mit § 260 Abs 1 lit b BAO als verspätet zurückgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Silvana Hellfritz`(person)
- `Reibersweg 24, 8144 Unterpremstätten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `69-424/6198`(tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/140324.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140324.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Friedhelm Sutor, Taggergasse 3, 3873 Thaures, Österreich, vertreten durch LeitnerLeitner GmbH  Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32, 4040 Linz, über die Beschwerde  vom 12. Jänner 2021 gegen den Bescheid des Finanzamtes für Großbetriebe vom  16. Dezember 2020 betreffend Normverbrauchsabgabe 06.2015-12.2019 Steuernummer  11-766/4596  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Friedhelm Sutor`(person)
- `Taggergasse 3, 3873 Thaures, Österreich`(address)
- `LeitnerLeitner GmbH  Wirtschaftsprüfer und Steuerberater`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `11-766/4596`(tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/140460.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140460.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ali Brücklmayer  in der Beschwerdesache Ulrike Kudlacek,  Nörsach 15, 4223 Standorf, Österreich, vertreten durch Dr. Klaus Gaig Wirtschaftsprüfung und Steuerberatung GmbH,  Wagnastraße 1, 8430 Leibnitz, über die Beschwerde vom 31. Oktober 2019 gegen den Bescheid  des Finanzamtes Deutschlandsberg Leibnitz Voitsberg vom 2. Oktober 2019 betreffend  Aufhebung § 299 BAO /  ESt 2015 Steuernummer 26-799/5403  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Klaus Gaig Wirtschaftsprüfung` — partial — pred is substring of gold: `Dr. Klaus Gaig Wirtschaftsprüfung und Steuerberatung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ali Brücklmayer`(person)
- `Ulrike Kudlacek`(person)
- `Nörsach 15, 4223 Standorf, Österreich`(address)
- `Dr. Klaus Gaig Wirtschaftsprüfung und Steuerberatung GmbH`(organisation)
- `Finanzamtes`(organisation)
- `26-799/5403`(tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/140529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140529.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Li Megerlein, Tungassingerstraße 18, 5061 Gfalls, Österreich, über die Beschwerde vom 5. April 2019 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 4. April 2019, Steuernummer  89-939/3728, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Katrin Allram` — partial — pred is substring of gold: `Mag.Dr. Katrin Allram`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Li Megerlein`(person)
- `Tungassingerstraße 18, 5061 Gfalls, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `89-939/3728`(tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/141269.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141269.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Miriam Stauffenberg, Armensündergraben 17, 4776 Mayberg, Österreich, über die Beschwerde vom 17. März 2023 gegen  den Bescheid des Finanzamtes Österreich vom 16. März 2023, Steuernummer  78-665/1920, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 zu Recht:   I. Der angefochtene Bescheid wird im Sinne der Beschwerdevorentscheidung vom  2. Mai 2023 abgeändert.

**False Positives:**

- `Dr. Katrin Allram` — partial — pred is substring of gold: `Mag.Dr. Katrin Allram`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Miriam Stauffenberg`(person)
- `Armensündergraben 17, 4776 Mayberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `78-665/1920`(tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/141441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141441.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dr. Finn Rosen  in der Beschwerdesache Dragan Ohlff,  vertreten durch Dr. Sven Rudolf Thorstensen LLM, Neustiftgasse 3/7, 1070 Wien, über die  Beschwerde vom 23. Juli 2019 gegen den Bescheid des Finanzamtes Baden Mödling vom  10. Juli 2019 betreffend den Bescheid über den Ablauf einer Aussetzung der Einhebung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Finn Rosen` — partial — pred is substring of gold: `Hon.-Prof. Dr. Finn Rosen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Dr. Finn Rosen`(person)
- `Dragan Ohlff`(person)
- `Dr. Sven Rudolf Thorstensen LLM`(person)
- `Finanzamtes Baden Mödling`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_26`)


In dem vor dem Gerichtskommissär Dr. Robert AUSTALLER, öffentlicher Notar in St. Pantaleon,  vor Einantwortung des Nachlasses abgeschlossenen Erbübereinkommen vom 29.1.2016 haben  die Miterbinnen vereinbart, dass:  a) die erbl.

**False Positives:**

- `Dr. Robert` — partial — pred is substring of gold: `Dr. Robert AUSTALLER`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Robert AUSTALLER`(person)

</details>

---

## `Dr_in_Title` 💣

**F1:** 0.014 | **Precision:** 0.448 | **Recall:** 0.007  

**Format:** `regex`  
**Rule ID:** `41722b28`  
**Description:**
Captures names with the title 'Dr.in' (female doctor) which was missing.

**Content:**
```
\bDr\.in\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.448 | 0.007 | 0.014 | 29 | 13 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 13 | 16 | 1838 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Dietlind Mahlstädt  in der Beschwerdesache  Kai Pipers, Gottaweg 58, 9130 Annamischl, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs-und  Steuerberatungsgesellschaft, Kudlichstraße 41-43, 4020 Linz, über die Beschwerde vom  30. April 2013 gegen den Bescheid des Finanzamt Tirol Ost  vom 12. März 2013 betreffend zu Recht:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Dietlind Mahlstädt` | `Dr.in Dietlind Mahlstädt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kai Pipers` (person)
- `Gottaweg 58, 9130 Annamischl, Österreich` (address)
- `KPMG Alpen-Treuhand GmbH` (organisation)
- `Finanzamt Tirol Ost` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129868.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129868.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Huberta Hammers  in der Beschwerdesache Josefine Frikel,  Eberhardgasse 20, 4213 Hattmannsdorf, Österreich, über die Beschwerde vom 29.9.2010 gegen den Bescheid des Finanzamtes  Kufstein Schwaz vom 2.9.2010 betreffend Festsetzung der Normverbrauchsabgabe für den  Zeitraum November 2008 und Verspätungszuschlag,  StrNr, zu Recht erkannt:     Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Huberta Hammers` | `Dr.in Huberta Hammers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Josefine Frikel` (person)
- `Eberhardgasse 20, 4213 Hattmannsdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/131027.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ute Gspan  in der Beschwerdesache des  OMedR Ottfried Theißl, Hadersdorferweg 3, 9560 Glabegg, Österreich, vertreten durch StB, über die Beschwerde vom 4. September 2019  gegen den Bescheid des FA Wien 8/16/17  vom 5. August 2019 betreffend  Einkommensteuervorauszahlungen 2019 zu Recht erkannt:     Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Ute Gspan` | `Dr.in Ute Gspan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Ottfried Theißl` (person)
- `Hadersdorferweg 3, 9560 Glabegg, Österreich` (address)
- `FA Wien 8/16/17` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/131574.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131574.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Kirstin Matiascheck  in der Beschwerdesache   Annemarie Schwinge, Rametzhofen 15, 3392 Hohenwarth, Österreich, über die Beschwerde vom 12. August 2015 gegen den Bescheid des  Finanzamtes Österreich vom 5. August 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014, Steuernummer 32-672/7699, zu Recht erkannt:   Der Beschwerde wird im Ausmaß der Beschwerdevorentscheidung vom 03. Mai 2016 teilweise  Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Kirstin Matiascheck` | `Dr.in Kirstin Matiascheck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Annemarie Schwinge` (person)
- `Rametzhofen 15, 3392 Hohenwarth, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `32-672/7699` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Edith Lohhausen  in der Beschwerdesache der  Schmalohr + Kiekebusch Möbel, Reitermühlweg 72, 3923 Bernhards, Österreich, vertreten durch Michael Haberl, Winkler Straße 516 Tür 1, 8962  Gröbming, über die Beschwerde vom 20. Mai 2020 gegen den Bescheid des Finanzamtes XY  (jetzt Dienststelle des Finanzamt Judenburg Liezen ) vom 5. März 2020 betreffend Umsatzsteuer 2017 zur  Steuernummer 71-763/1501  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Edith Lohhausen` | `Dr.in Edith Lohhausen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Schmalohr + Kiekebusch Möbel` (organisation)
- `Reitermühlweg 72, 3923 Bernhards, Österreich` (address)
- `Michael Haberl` (person)
- `Finanzamtes` (organisation)
- `Finanzamt Judenburg Liezen` (organisation)
- `71-763/1501` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sheila Nonnmacher  in der Beschwerdesache Sieglinde Semertzidou,  Bürgerspitalstraße 8, 9361 Judendorf, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, über  die Beschwerde vom 20.03.2017 gegen die Umsatzsteuerbescheide 2007 bis 2008 „aufgrund  der BP“, Steuernummer 76-265/6028, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Sheila Nonnmacher` | `Dr.in Sheila Nonnmacher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sieglinde Semertzidou` (person)
- `Bürgerspitalstraße 8, 9361 Judendorf, Österreich` (address)
- `Dr. Silvia Gredenberg` (person)
- `76-265/6028` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/136462.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136462.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Linn Wolek  in der Verwaltungsstrafsache  MedR Uwe Vaculik, Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich, über die Eingabe der Beschuldigten vom 3. Februar 2022 den  Beschluss gefasst:  I. Gemäß § 28 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 31 VwGVG  und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) wird die Unzuständigkeit  des Bundesfinanzgerichtes festgestellt und das Beschwerdeverfahren betreffend die Eingabe  vom 3. Februar 2022 eingestellt.  II. Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach  Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG kraft Gesetzes nicht zulässig.

| Predicted | Gold |
|---|---|
| `Dr.in Linn Wolek` | `Dr.in Linn Wolek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Uwe Vaculik` (person)
- `Edramsberger Straße 23, 2135 Neudorf im Weinviertel, Österreich` (address)
- `Bundesfinanzgerichtes` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/138485.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138485.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Elisabeth Hafner in der  Beschwerdesache Janina Gruenaeugl, Geiereckstraße 27, 4720 Güttling, Österreich, Schweden, vertreten durch die Ernst & Young  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b. H., Wagramer Straße 19, 1220  Wien, über die Beschwerde vom 9. Jänner 2017 gegen den Bescheid des Finanzamtes für  Großbetriebe (vormals Bruck Eisenstadt Oberwart) vom 13. April 2015 betreffend Abweisung  eines Antrages auf Rückzahlung Österreichischer Lohnsteuer,Einkommensteuer 2012  Steuernummer 65-008/8295  zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Elisabeth Hafner` | `Dr.in Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Janina Gruenaeugl` (person)
- `Geiereckstraße 27, 4720 Güttling, Österreich` (address)
- `Ernst & Young  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b. H.` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `65-008/8295` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Chen Kruczyk  in der Beschwerdesache Olivia Trienes,  Kleingerharts 28, 4972 Dann, Österreich, über die Beschwerde vom 13. Mai 2022 gegen den Bescheid des Finanzamtes  Österreich vom 5. Mai 2022, Ordnungsbegriff X1, betreffend Abweisung des Antrages auf den  Erhöhungsbetrag zur Familienbeihilfe für den Zeitraum ab März 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Chen Kruczyk` | `Dr.in Chen Kruczyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Olivia Trienes` (person)
- `Kleingerharts 28, 4972 Dann, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/141329.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141329.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Ingeborg Brockmayer  in der Beschwerdesache des  Timothy Penzlin, Ötzeltgasse 264, 6252 Kleinsöll, Österreich, betreffend die Beschwerde vom 25. Jänner 2017 gegen den  Haftungsbescheid des FA Innsbruck  vom 21. Dezember 2016 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Ingeborg Brockmayer` | `Dr.in Ingeborg Brockmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timothy Penzlin` (person)
- `Ötzeltgasse 264, 6252 Kleinsöll, Österreich` (address)
- `FA Innsbruck` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/147542.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147542.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Anneliese Furtmeier  in der Beschwerdesache Werner Kachelek,  Heideweg-Siedlung 7, 4030 Linz, Österreich, vertreten durch Eugen Josef Bertsch, Sportplatzweg 11, 6811 Göfis, betreffend  Beschwerde vom 22. August 2019 gegen den Bescheid des FA Spittal Villach (nunmehr Finanzamt  Österreich) vom 29. Juli 2019 über die Abweisung eines Antrages auf Nachsicht gemäß § 236  BAO, Steuernummer 85-278/4119, beschlossen:  Der Vorlageantrag vom 30. September 2019 wird gemäß § 256 Abs. 3 BAO in Verbindung mit  § 264 Abs. 4 lit. d BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Dr.in Anneliese Furtmeier` | `Dr.in Anneliese Furtmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Werner Kachelek` (person)
- `Heideweg-Siedlung 7, 4030 Linz, Österreich` (address)
- `Eugen Josef Bertsch` (person)
- `FA Spittal Villach` (organisation)
- `Finanzamt  Österreich` (organisation)
- `85-278/4119` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/148554.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148554.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Koolen  in der Beschwerdesache   Univ.-Prof. Brian Salemi, Ulrichskirchen 3, 4184 Neuschlag, Österreich, Philippinen, Steuernummer 63-391/9556  über die Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamt Grieskirchen Wels  vom 1. Februar  2018 betreffend Vorsteuererstattung 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Regina Koolen` | `Dr.in Regina Koolen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Brian Salemi` (person)
- `Ulrichskirchen 3, 4184 Neuschlag, Österreich` (address)
- `63-391/9556` (tax_number)
- `Finanzamt Grieskirchen Wels` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_32`)


Der Substanzwert ist  der niedrigste für Gesellschaftsanteile an der Dr.in Flora Lallemand  anzusetzende Wert, selbst wenn man  das gesamte Potential an Mehrwertsteuerrückforderungen durch das Finanzamt berücksichtigt  (Gutachten von Mag. H., gerichtlich beeideter Sachverständiger ON 35 u 48).

| Predicted | Gold |
|---|---|
| `Dr.in Flora Lallemand` | `Dr.in Flora Lallemand` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)
- `Mag. H.` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/131820.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131820.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Bianca Gerasimczuk  in der Beschwerdesache des  Raimund Diedering, Bakk. iur., Isonzogasse 16, 4742 Irringsdorf, Österreich, über die Beschwerde vom 8. Juli 2009 gegen den Bescheid des FA  vom 9. Juni 2009 betreffend Umsatzsteuer und Einkommensteuer 2005 zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Bianca Gerasimczuk` — partial — pred is substring of gold: `Priv.-Doz.in Dr.in Bianca Gerasimczuk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Bianca Gerasimczuk`(person)
- `Raimund Diedering, Bakk. iur.`(person)
- `Isonzogasse 16, 4742 Irringsdorf, Österreich`(address)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_40`)


S. wurde am 1. Juli 2021 von Dr.in Dok3 untersucht und folgendes Gutachten erstellt:  Anamnese:  Siehe auch Vorgutachten vom 2.3.2021  Es wurde kein Grad der Behinderung ermittelt. Da zwar gutachterliche Diagnosen gestellt  wurden, jedoch mangels an Anspruchnahme adäquater Therapien eine für die Beurteilung  alltags relevante anhaltende Einschränkung erforderliche ärztliche Verlaufsdokumentation  nicht vorhanden ist.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_93`)


Dr.in Dok3, Fachgebiet: Ärztin für Allgemein-medizin, erstellte am 31. Jänner 2022 folgendes  Aktengutachten:  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  Mag. W. klinische und Gesundheitspsychologin allgemein beeidigte und gerichtlich zertifizierte  Sachverständige klinisch psychologisches Privatgutachten vom 5.10.2021  Es liegt eine Asperger-Autismus-Störung vor, die zum Teil widersprüchlichen Ergebnisse,  insbesondere die Selbstbeurteilung des Mj sowie einige seiner Leistungstestergebnisse, welche  deutlich besser ausgefallen sind als es bei einer Person mit Asperger-Autismus zu erwarten  gewesen wäre, lässt sich dahingehend klären, dass der Mj wahrscheinlich auch mitbedingt  durch seine hohe Intelligenz-sich über Jahre hinweg sehr vielen sozialen Kompetenzen kognitiv  erschlossen hat und somit auf heuristischer Basis agieren kann sofern er das vorliegende soziale  Muster schnell und unbeeinträchtigt von Störvariablen erkennt.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_111`)


Im Gutachten vom 1. Juli 2021 stellte Dr.in Dok3 ebenfalls keinen Grad der Behinderung fest.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_112`)


Im Aktengutachten vom 31. Jänner 2022 wurde das (inzwischen vorgelegte) Privatgutachten  von MMag. W., MSc, vom 5. Oktober 2021 berücksichtigt und von Dr.in Dok3 die Erkrankung  von S. unter die Pos.Nr. 03.04.01 der Einschätzungsverordnung mit einem Gesamtgrad der  Behinderung von 30 vH rückwirkend ab Oktober 2021 eingereiht.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_168`)


Im Gutachten vom 1. Juli 2021 stellte Dr.in Dok3 erneut keinen Grad der Behinderung fest, dies  mit der Begründung, dass keine aktuellen Befunde beigebracht worden seien.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_170`)


Bei der Erstellung des Aktengutachtens vom 31. Jänner 2022 lag der Sachverständigen Dr.in  Dok3 das Privatgutachten von MMag. W., MSc, vom 5. Oktober 2021 vor.

**False Positives:**

- `Dr.in  Dok` — partial — pred is substring of gold: `Dr.in  Dok3`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in  Dok3`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_179`)


Unter Einbeziehung der von MMag. W., MSc, in ihrem Gutachten getroffenen Diagnose reihte  Dr.in Dok3X.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok3X`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok3X`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_89`)


Die Tochter der Bf wurde im Zuge des Antragsverfahrens am 8. Juli 2020 im Sozialministerium- service von Dr.in Dok1, Ärztin für Allgemeinmedizin, begutachtet und folgendes Gutachten  erstellt:  "Anamnese:   Asperger Syndrom, F40.2. Spezifische Phobie  Derzeitige Beschwerden:   Laut Auskunft der Mutter: Vor einem Jahr ist meine Dok2 darauf gekommen, dass sie eventuell  ein Asperger Syndrom haben könnte.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok1`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_215`)


M. ist ledig und lebt in einem eigenen Haushalt.  Im Zuge des Antrags- und Beschwerdeverfahrens wurden seitens des Sozialministeriumservice  zwei Gutachten erstellt.  Im Gutachten vom 8. Juli 2020 stellte Dr.in Dok1, Ärztin für Allgemeinmedizin, die Diagnose  Asperger Syndrom und reihte die Erkrankung unter die Pos.Nr. 03.04.01 der  Einschätzungsverordnung mit einem Grad der Behinderung von 30 vH. rückwirkend ab  November 2019 (= Austestung).

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `M.`(person)
- `Dr.in Dok1`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_279`)


Dr.in Dok1, Ärztin für Allgemeinmedizin, lag bei der Erstellung des Gutachtens vom 8. Juli 2020  der Psychologische Kurz-Befund der X Privatuniversität aus 2019 vor.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok1`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_280`)


Dr.in Dok1 reihte die Erkrankung unter die Pos.Nr. 03.04.01 der Einschätzungsverordnung mit  einem Grad der Behinderung von 30 vH.

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok1`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/139220.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139220.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Mag.a Univ.-Prof.in Konstanze Lukass  in der Beschwerdesache Selma Katirci,  Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich  vertreten durch Brehm & Sahinol Rechtsanwälte OG, Linke Wienzeile 124/Tür  10, 1060 Wien, über die Beschwerde vom 11. November 2019 gegen den Bescheid des  Finanzamtes Wien 12/13/14 Purkersdorf vom 7. Oktober 2019 betreffend Abweisung des  Antrags vom 23. September 2019 auf Gewährung der Familienbeihilfe und des  Kinderabsetzbetrages ohne Vornahme einer Indexierung  gemäß  § 8a Familienlastenausgleichsgesetz 1967 (FLAG 1967), SV-Nr. Zahl, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr.in Mag` — partial — pred is substring of gold: `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Mag.a Univ.-Prof.in Konstanze Lukass`(person)
- `Selma Katirci`(person)
- `Vestenöttingerstraße 6, 8822 Jakobsberg, Österreich`(address)
- `Brehm & Sahinol Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/141414.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141414.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Dr.in Mag.a Elisabeth Wiedenhöfft, LLM, Hirschberg 29, 2870 Guggendorf, Österreich, über die Beschwerde vom 11. November 2021 gegen den Bescheid  des Finanzamtes Österreich vom 5. Oktober 2021 betreffend Antrag auf Bewilligung der  Aussetzung § 212a BAO 2021, Steuernummer 16-471/8115  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Mag` — partial — pred is substring of gold: `Dr.in Mag.a Elisabeth Wiedenhöfft, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Dr.in Mag.a Elisabeth Wiedenhöfft, LLM`(person)
- `Hirschberg 29, 2870 Guggendorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `16-471/8115`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/142360.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142360.1_17`)


Die Bf. legte im Zuge der Beschwerde folgende Unterlagen vor:  Schreiben von Mag. Dr.in Carina B., Psychotherapeutin:  T. befindet sich seit 12. April 2022 auf Grund ihrer psychischen Erkrankung in einer  regelmäßigen ambulanten Psychotherapie bei ihr.

**False Positives:**

- `Dr.in Carina` — partial — pred is substring of gold: `Mag. Dr.in Carina B.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Dr.in Carina B.`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_15`)


Mit Beschluss vom 24.10.2024 bewilligt der Verwaltungsgerichtshof der Dr.in Flora Lallemand  Verfahrenshilfe für die außerordentliche Revision gegen das Erkenntnis des  Bundesfinanzgerichts Außenstelle Linz vom 20.08.2024, RV/7100825/2024, betreffend  Umsatzsteuer und Körperschaftsteuer 2015.

**False Positives:**

- `Dr.in Flora Lallemand  Verfahrenshilfe` — partial — gold is substring of pred: `Dr.in Flora Lallemand`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)
- `Dr.in Flora Lallemand`(person)
- `Bundesfinanzgerichts`(organisation)

</details>

---

## `Durch_Richter_Name` 💣

**F1:** 0.003 | **Precision:** 0.273 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `a2c71d48`  
**Description:**
Captures person names following 'durch den Richter' or 'durch die Richterin' when the name might not have a title immediately following, or to ensure full name capture including suffixes.

**Content:**
```
(?:durch\s+den\s+Richter|durch\s+die\s+Richterin)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+LL\.M\.|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)(?=\s+in\s+der|\s+\.|,|\s+\d)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.273 | 0.002 | 0.003 | 11 | 3 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 8 | 1848 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache der  Kelderber Beratung Technologien, Mirtlweg 6, 2473 Deutsch-Haslau, Österreich, vertreten durch Dr Vana Dr Kolbitsch Mag Breitenecker,  Taborstraße 10 Tür Stg 2, 1020 Wien, diese vertreten durch Mag Tatjana Kovacic und Dr  Heinrich Vana, über die Beschwerden vom 29. September 2017 und vom 20. August 2018  gegen die Bescheide des Finanzamtes Wien 8/16/17 vom 6. September 2017 und vom 9.  August 2018, SVN 7867 150654, betreffend Abweisung der in Verbindung mit der Verordnung  (EG) Nr 883/2004 des Europäischen Parlaments und des Rates vom 29.4.2004 zur  Koordinierung der Systeme der sozialen Sicherheit, ABlEU L 166 vom 30.4.2004, (in der Folge:  VO 883/2004, neue Koordinierung oder Grundverordnung) gestellten Anträge ab Oktober 2016  für die Kinder K1 (geb xx.xx.2011), K2 (geb yy.yy.2015) und ab Dezember 2017 weiters für das  Kind K3 (geb zz.zz.2017) auf Gewährung der Familienbeihilfe gemäß § 8 Abs 3 und 4  Familienlastenausgleichsgesetz und des Kinderabsetzbetrages gemäß § 33 Abs 3 Satz 1  Einkommensteuergesetz und jeweils alternativ in Verbindung mit § 13  Entwicklungshelfergesetz nach ausschließlich österreichischen Rechtsvorschriften gestellten  Anträge, gemäß § 290 Abs 1 Bundesabgabenordnung beschlossen:  I. Dem Gerichtshof der Europäischen Union werden gemäß Art 267 AEUV folgende  Fragen mit dem Ersuchen um Vorabentscheidung vorgelegt:  Frage 1:  Ist Art 11 Abs 3 Buchstabe e) VO 883/2004 dahin auszulegen, dass darunter eine Situation  einer Arbeitnehmerin mit Staatsbürgerschaft eines Mitgliedstaates, in dem sie und die Kinder  auch ihren Wohnort haben, die mit einem Arbeitgeber mit Sitz in einem anderen Mitgliedstaat  ein Beschäftigungsverhältnis als Entwicklungshelferin eingeht, das nach den Rechtsvorschriften  des Sitzstaates dem Pflichtversicherungssystem unterfällt, und von dem Arbeitgeber zwar nicht  unmittelbar nach Einstellung, jedoch nach Absolvierung einer Vorbereitungszeit und nach  Rückkehr für Zeiten der Reintegration im Sitzstaat, in einen Drittstaat entsendet wird, fällt?

| Predicted | Gold |
|---|---|
| `Silvia Gebhart` | `Silvia Gebhart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kelderber Beratung Technologien` (organisation)
- `Mirtlweg 6, 2473 Deutsch-Haslau, Österreich` (address)
- `Dr Vana Dr Kolbitsch Mag Breitenecker` (person)
- `Mag Tatjana Kovacic` (person)
- `Dr  Heinrich Vana,` (person)
- `Finanzamtes Wien 8/16/17` (organisation)
- `7867 150654` (social_security_number)
- `Europäischen Parlaments` (organisation)
- `Gerichtshof der Europäischen Union` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Silvia Gebhart in der Beschwerdesache  Erwin Döpkemeier, Minithal 3, 5360 Markt, Österreich, vertreten durch Mag Kerstin Friedrich, Kornplatz 9, 2550  Langenlois, als Verlassenschaftskuratorin, über die Beschwerde vom 8. Februar 2018 gegen  den Bescheid des Finanzamtes Waldviertel vom 5. Jänner 2018, nunmehr Finanzamt  Österreich), betreffend Abweisung des Antrages auf Familienbeihilfe und erhöhte  Familienbeihilfe ab November 2012, Steuernummer 02-365/4052, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silvia Gebhart` | `Silvia Gebhart` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Erwin Döpkemeier` (person)
- `Minithal 3, 5360 Markt, Österreich` (address)
- `Mag Kerstin Friedrich` (person)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamt  Österreich` (organisation)
- `02-365/4052` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/143846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143846.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Rüdiger Tormählen  in der Beschwerdesache  Melina Weingartz, KLG Aus eigener Kraft 31, 3830 Vestenpoppen, Österreich, über die Beschwerde vom 20. Oktober 2023 gegen den Bescheid  des Finanzamtes Österreich vom 14. September 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 Steuernummer 77-866/9586  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Rüdiger Tormählen` | `Rüdiger Tormählen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melina Weingartz` (person)
- `KLG Aus eigener Kraft 31, 3830 Vestenpoppen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `77-866/9586` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129122.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129122.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sabine Tiedicke, Ritterhof 8, 4280 Harlingsedt, Österreich, über die Beschwerde vom 5. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 25. Juni 2019, betreffend die Abweisung des Antrages auf Ausgleichszahlung  für das Kind x - mangels Festlegung eines Endzeitpunktes - im Zeitraum vom 01.02.2016 bis  zum 30.06.2019 sowie für das Kind y - mangels Festlegung eines Endzeitpunktes - im Zeitraum  vom 01.02.2018 bis zum 30.06.2019 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sabine Tiedicke`(person)
- `Ritterhof 8, 4280 Harlingsedt, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Fatima Eichmayr, Wieskapellenweg 10, 8047 Graz, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in 5020 Salzburg, Hellbrunner Straße 5,  über die Beschwerde vom 8. Jänner 2010 gegen die Bescheide des Finanzamtes Salzburg-Stadt  (nunmehr: Finanzamt Österreich) vom 12. November 2009 betreffend Haftung für  Kapitalertragsteuer für 2004 bis 2008, Steuernummer 67-455/2359, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Fatima Eichmayr`(person)
- `Wieskapellenweg 10, 8047 Graz, Österreich`(address)
- `Dr. Klaus Plätzer,`(person)
- `Finanzamtes Salzburg-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)
- `67-455/2359`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/139346.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139346.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Muran Grönewald, Jane-Tilden-Gasse 2, 3153 Rotheau, Österreich, vertreten durch Pallauf Meißnitzer Staindl & Partner, Rechtsanwälte,  Petersbrunnstraße 13, 5020 Salzburg, über die Beschwerden vom 19. Dezember 2019 gegen  die Bescheide des Finanzamtes Salzburg-Stadt (nunmehr Finanzamt Österreich) vom  11. Dezember 2019 betreffend Wiederaufnahme § 303 BAO /  ESt 2013 sowie vom 12.12.2019  betreffend Wiederaufnahme § 303 / ESt 2014 und betreffend Wiederaufnahme § 303 / ESt  2015 zu Steuernummer 87-098/9833  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Muran Grönewald`(person)
- `Jane-Tilden-Gasse 2, 3153 Rotheau, Österreich`(address)
- `Pallauf Meißnitzer Staindl & Partner`(organisation)
- `Finanzamtes Salzburg-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)
- `87-098/9833`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/139401.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139401.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Dr. Dipl.-Ing. Laurence Goetke,  Unterernsthofen 11, 9311 Leiten, Österreich, vertreten durch STB, Adr1, über die Beschwerde vom 10. Dezember 2019  gegen den Bescheid des A vom 12. November 2019 betreffend Umsatzsteuer 2012,  Steuernummer 42-698/5318, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dipl.-Ing. Laurence Goetke`(person)
- `Unterernsthofen 11, 9311 Leiten, Österreich`(address)
- `42-698/5318`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/141545.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141545.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache OStR Cassandra Schmedtje,  Lettenmayrhof 1, 9556 Karlsberg, Österreich, vertreten durch Helga Kraus, Johann Vollnhofer-Straße 1/Stg.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OStR Cassandra Schmedtje`(person)
- `Lettenmayrhof 1, 9556 Karlsberg, Österreich`(address)
- `Helga Kraus`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/142193.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142193.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Meinrad Andreis, Rueberstraße 14, 2451 Au am Leithaberge, Österreich, vertreten durch PKF Corti & Partner GmbH Wirtschaftsprüfer und Steuerberater, Peter  Tunner-Straße 7, 8700 Leoben, über die Beschwerde vom 14. August 2018 gegen den Bescheid  des Finanzamtes St. Johann Tamsweg Zell am See vom 16. Juli 2018 betreffend  Haftungsbescheid /  Lohnsteuer 2013, 2014, 2015, 2016 und 2017, Steuernummer  04-607/8099  zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Meinrad Andreis`(person)
- `Rueberstraße 14, 2451 Au am Leithaberge, Österreich`(address)
- `PKF Corti & Partner GmbH Wirtschaftsprüfer und Steuerberater`(organisation)
- `Finanzamtes St. Johann Tamsweg Zell`(organisation)
- `04-607/8099`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/142384.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142384.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Thassilo Bergsträsser,  Alois Blumauer-Gasse 1o, 4152 Unternreith, Österreich, vertreten durch VICTORIA Wirtschaftstreuhand GmbH, Prinz-Eugen-Straße  16/1/6, 1040 Wien über die Beschwerde vom 4. August 2021 gegen den Bescheid des  Finanzamtes Österreich vom 19. Juli 2021 betreffend Einkommensteuer 2019 Steuernummer  68-027/9886  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Thassilo Bergsträsser`(person)
- `Alois Blumauer-Gasse 1o, 4152 Unternreith, Österreich`(address)
- `VICTORIA Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `68-027/9886`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/145854.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145854.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Charles Ossmann,  Karl Lill-Straße 36, 4725 Edern, Österreich, vertreten durch VertretungsNetz - Erwachsenenvertretung,  Patientenanwaltschaft, Bewohnervertretung, Gruberstraße 6/1.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Charles Ossmann`(person)
- `Karl Lill-Straße 36, 4725 Edern, Österreich`(address)

</details>

---

## `Ing_Title` 💣

**F1:** 0.005 | **Precision:** 0.116 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `62071b1a`  
**Description:**
Captures names with 'Ing.' or 'Dipl.-Ing.' or 'ÖkR Ing.' or 'OSR Ing.', ensuring the full title sequence is matched.

**Content:**
```
\b(?:ÖkR\s+|OSR\s+)?(?:Dipl\.-)?Ing\.(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*)+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.116 | 0.003 | 0.005 | 43 | 5 | 38 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 38 | 1846 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Dipl.-Ing. Melinda Herrwerth, Dürergasse 7, 4872 Windbichl, Österreich, Steuernummer 40-459/9630   1.) betreffend die Beschwerde vom 3. Juni 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 27. Mai 2020, mit dem der  Antrag vom 28. Februar 2020 auf erhöhte Familienbeihilfe für Lubomir Nakajima  für den  Zeitraum ab Mai 2018 abgewiesen wurde, beschlossen:   Der Vorlageantrag vom 1. März 2021, insoweit damit die Vorlage der Beschwerde vom 3. Juni  2020 beantragt wird, wird gemäß § 260 Abs. 1 lit. b Bundesabgabenordnung (BAO) in  Verbindung mit § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Melinda Herrwerth` | `Dipl.-Ing. Melinda Herrwerth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dürergasse 7, 4872 Windbichl, Österreich` (address)
- `40-459/9630` (tax_number)
- `Finanzamtes  Wien 2/20/21/22` (organisation)
- `Finanzamt Österreich` (organisation)
- `Lubomir Nakajima` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_162`)


Geschäftsführer dieser GmbH sind der zweite Stratege und Ing. Michael FG2 (beide jedenfalls  seit 1.1.2008-heute).

| Predicted | Gold |
|---|---|
| `Ing. Michael` | `Ing. Michael` |

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_167`)


Geschäftsführer dieser GmbH waren der erste Stratege (jedenfalls 1.1.2008 –12.2021) und Ing.  Eduard FG4 (jedenfalls seit 1.1.2008-heute).

| Predicted | Gold |
|---|---|
| `Ing.  Eduard` | `Ing.  Eduard` |

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch der Richter R. in der Beschwerdesache Dipl.-Ing. Emma Chatzistamatis, Senden 22, 4673 Unterbergham, Österreich, über die Beschwerde vom 13. August 2019 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln, nunmehr Finanzamt Österreich, vom 17. Juli 2019 betreffend  Abweisung des Antrages auf Gewährung der vollen nichtindexierten Ausgleichszahlung der  Familienbeihilfe ab Jänner 2019, Steuernummer 59-959/5444, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Emma Chatzistamatis` | `Dipl.-Ing. Emma Chatzistamatis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Senden 22, 4673 Unterbergham, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `59-959/5444` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/147373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147373.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Friedhelm Weigmann  in der Beschwerdesache Dipl.-Ing. Sibylle Leichnam,  Anton-Hölzl-Hof 173, 4890 Ziegelstadl, Österreich, über die Beschwerde vom 16. März 2023 gegen den Bescheid des FA Baden Mödling  vom 15. März 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022,  Steuernummer 10-035/7116, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Sibylle Leichnam` | `Dipl.-Ing. Sibylle Leichnam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Friedhelm Weigmann` (person)
- `Anton-Hölzl-Hof 173, 4890 Ziegelstadl, Österreich` (address)
- `FA Baden Mödling` (organisation)
- `10-035/7116` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Priv.-Doz. Dipl.-Ing. Theobald Brauckhof, Gaden 76, 8250 Zeil-Pöllau, Österreich, über die Beschwerde vom 02.04.2019 gegen den Bescheid des Finanzamtes A vom  26.03.2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dipl.-Ing. Theobald Brauckhof` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `Gaden 76, 8250 Zeil-Pöllau, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Dipl.-Ing. Theobald Brauckhof` — partial — pred is substring of gold: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `SeeAutomotive AG`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache   1. Ing. StR Samuel Fraesdorff, Schöntalweg 6, 9162 Rabenberg, Österreich   2. Maximilian Jasper, Wetzles 9, 3243 Lunzen, Österreich  diese vertreten durch Prof. Dr. Thomas Keppert Steuerberatung  und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien,   beide als Rechtsnachfolger der Leroy Kusznierz  und   3.

**False Positives:**

- `Ing. St` — partial — pred is substring of gold: `Ing. StR Samuel Fraesdorff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Schöntalweg 6, 9162 Rabenberg, Österreich`(address)
- `Maximilian Jasper`(person)
- `Wetzles 9, 3243 Lunzen, Österreich`(address)
- `Prof. Dr. Thomas Keppert`(person)
- `Leroy Kusznierz`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_26`)


Nachdem die Leroy Kusznierz  infolge Anwachsung der Gesellschaftsanteile nach § 142 UGB an die  Firma4 mit Wirksamkeit zum xx.xx.2020 im Firmenbuch gelöscht worden war, wurde die  steuerliche Vertretung mit verfahrensleitender Verfügung vom 27.01.2020 aufgefordert  mitzuteilen, ob 1. zu Ing. StR Samuel Fraesdorff (in der Folge kurz: ErstBf.), 2. zur Maximilian Jasper (in der Folge kurz:  ZweitBf.) und 3. zur Gustav Nowak.

**False Positives:**

- `Ing. St` — partial — pred is substring of gold: `Ing. StR Samuel Fraesdorff`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Leroy Kusznierz`(person)
- `Ing. StR Samuel Fraesdorff`(person)
- `Maximilian Jasper`(person)
- `Gustav Nowak`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_14`)


Entscheidungsgründe  Mit den sechs (im Spruch dieses Erkenntnisses angeführten) angefochtenen Straferkenntnissen  hat der Magistrat der Stadt Wien, Magistratsabteilung 67, als belangte Behörde dem  Beschwerdeführer (Bf.) jeweils angelastet, er habe als zur Vertretung nach außen berufene  Person der Zulassungsbesitzerin,Dr.in Ing. Viktoria Weigart mit Sitz in AdrFirma1, der Fahrzeuge mit den  behördlichen Kennzeichen zu   GZ. 1) Auto1 (A),    GZ. 2) Auto2 (A),    GZ. 3) Auto1 (A),    GZ. 4) Auto2 (A),    GZ. 5) Auto1 (A)    GZ 6) Auto1 (A)   den ordnungsgemäß zugestellten Verlangen der Behörde vom    zu 1) 07.05.2020,    zu 2) 17.03.2020,    zu 3) 17.03.2020,    zu 4) 17.03.2020    zu 5) 17.03.2020 und    zu 6) 27.02.2020  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er die mehrspurigen  Kraftfahrzeuge mit den näher genannten behördlichen Kennzeichen zu näher bezeichneten  Zeitpunkten überlassen gehabt habe, sodass sie in näher bezeichneten gebührenpflichtigen  Kurzparkzonen abgestellt waren, nicht entsprochen, da    2 von 22 Seite 3 von 22

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_20`)


2) bis 6): Die Dr.in Ing. Viktoria Weigart hafte für die mit diesen Bescheiden über die (den zur Vertretung  nach außen Berufenen Bf.) verhängten Geldstrafen und Verfahrenskosten sowie für sonstige in  Geld bemessene Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_65`)


Angemerkt wird noch, dass eine Anfrage beim zuständigen Arbeitsinspektorat Wien Wien  ergeben hat, dass von der Dr.in Ing. Viktoria Weigart kein verantwortlich Beauftragter gemäß § 9 VStG  gemeldet wurde, wie Ihnen bereits im Zuge anderer gegen Sie anhängiger Verfahren zur  Kenntnis gebracht wurde.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_108`)


In den betreffenden Einsprüchen hat der Beschwerdeführer dargelegt, dass er nur  handelsrechtlicher Geschäftsführer der Dr.in Ing. Viktoria Weigart ist.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_144`)


Über die Beschwerde wurde erwogen:  Aus dem Verwaltungsakt ergibt sich folgender Sachverhalt:  Die mehrspurigen Kraftfahrzeuge mit den behördlichen Kennzeichen 1) Auto1 (A), 2) Auto2 (A),  3) Auto1 (A), 4) Auto2 (A) und 5) Auto1 (A) waren zur jeweiligen Beanstandungszeit auf die Dr.in Ing. Viktoria Weigart  AdrFirma1, zugelassen.

**False Positives:**

- `Ing. Viktoria Weigart  Adr` — positional overlap with gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_145`)


Die Dr.in Ing. Viktoria Weigart wurde von der belangten Behörde mit (sechs) Schreiben als  Zulassungsbesitzerin aufgefordert, innerhalb einer Frist von zwei Wochen ab Zustellung  darüber Auskunft zu erteilen, wem sie das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen  1) Auto1 (A) überlassen gehabt habe, sodass es am 17.12.2019 um 10:15 Uhr in 1060 Wien,  Garbergasse 12, abgestellt gewesen sei (Schreiben vom 07.05.2020, GZ. MA67/Zahl1/2019).

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)


Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der Dr.in Ing. Viktoria Weigart  den  die (jeweilige) Auskunft treffe.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`
- `Ing. Viktoria Weigart` — similar text (different position): `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)
- `Angelstein`(person)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_161`)


Die Dr.in Ing. Viktoria Weigart wurde daraufhin von der Behörde mit fünf Schreiben vom 18.06.2020 an den  rechtsfreundlichen Vertreter unter Setzung einer zweiwöchigen Frist aufgefordert, Unterlagen  über den Umfang der Bevollmächtigung von Herrn Angelstein gem. § 9 Abs. 2 VStG vorzulegen, sowie  eine entsprechende Anordnungsbefugnis samt Zustimmungserklärung.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)
- `Angelstein`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_162`)


Dem Verlangen der Behörde wurde von der Dr.in Ing. Viktoria Weigart nicht entsprochen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_163`)


Mit sechs Strafverfügungen, eine zu 1) vom 05.06.2020 und fünf zu 2) bis 6) vom 14.07.2020  wurde dem Bf. jeweils angelastet, er habe als zur Vertretung nach außen berufene Person der  Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der genannten Fahrzeuge dem jeweils ordnungsgemäß  zugestellten Verlangen der Behörde innerhalb von zwei Wochen ab Zustellung Auskunft zu  geben, wem er das jeweils genannte Fahrzeug mit dem jeweils näher genannten behördlichen  Kennzeichen zu näher bezeichneten Zeitpunkten überlassen gehabt habe, sodass sie jeweils in  näher bezeichneten gebührenpflichtigen Kurzparkzonen abgestellt waren, nicht entsprochen.

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_168`)


Sachverhalt:  Der Einschreiter ist Geschäftsführer der Dr.in Ing. Viktoria Weigart  Dieses Unternehmen betreibt unter  anderem ein Taxi und Mietwagengewerbe.

**False Positives:**

- `Ing. Viktoria Weigart  Dieses Unternehmen` — positional overlap with gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_224`)


Die Behörde ging in den sechs angefochtenen Straferkenntnissen davon aus, der Bf. habe als  zur Vertretung nach außen berufene Person der Zulassungsbesitzerin Dr.in Ing. Viktoria Weigart der oben  genannten Fahrzeuge jeweils dem ordnungsgemäß zugestellten Verlangen der Behörde  innerhalb von zwei Wochen ab Zustellung Auskunft zu geben, wem er das jeweilige Fahrzeug  mit den vorher genannten behördlichen Kennzeichen zu einem näher bezeichneten Zeitpunkt  überlassen gehabt habe, sodass sie in bezeichneten gebührenpflichtigen Kurzparkzonen  abgestellt waren, jeweils nicht entsprochen, da zu  1) eine unrichtige Auskunft erteilt worden sei;

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_238`)


2) bis 6) vom 14.07.2020, wonach Herr Russbüldt als Fuhrparkleiter für die Dr.in Ing. Viktoria Weigart  für die Fahrzeuge verantwortlich gewesen sei, wird Folgendes festgestellt:  Gemäß § 9 Abs. 4 VStG kann verantwortlicher Beauftragter nur eine Person sein, die (unter  anderem) ihrer Bestellung nachweislich zugestimmt hat und der für den ihrer Verantwortung  18 von 22 Seite 19 von 22

**False Positives:**

- `Ing. Viktoria Weigart` — partial — pred is substring of gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Russbüldt`(person)
- `Dr.in Ing. Viktoria Weigart`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_244`)


Der Bf. ist die zur Vertretung nach außen berufene Person der Zulassungsbesitzerin, der Dr.in Ing. Viktoria Weigart  Somit traf ihn die Auskunftspflicht.

**False Positives:**

- `Ing. Viktoria Weigart  Somit` — positional overlap with gold: `Dr.in Ing. Viktoria Weigart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Ing. Viktoria Weigart`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/133518.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133518.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Dipl. Kfm. Ing. Ing. Jonas Thumberger, Paullehnerweg 72, 9584 Höfling, Österreich, vertreten durch UNICONSULT Steuerberatungs GmbH & Co KG,  Bahnhofstraße 35a, 4910 Ried im Innkreis, über die Beschwerde vom 7. Juni 2013 gegen den  Bescheid des FA Braunau Ried Schärding vom 28.9.2018 betreffend Umsatzsteuer 2012,  Steuernummer xxxx zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing. Ing` — partial — pred is substring of gold: `Dipl. Kfm. Ing. Ing. Jonas Thumberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karin Pitzer`(person)
- `Dipl. Kfm. Ing. Ing. Jonas Thumberger`(person)
- `Paullehnerweg 72, 9584 Höfling, Österreich`(address)
- `UNICONSULT Steuerberatungs GmbH & Co KG`(organisation)
- `FA Braunau Ried Schärding`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_161`)


An der Traver-Planung GmbH waren beteiligt:    26.600 €…Holding (jedenf. 1.1.2008-12.4.2010)  25.900 €… Holding (13.4.2010-8.2.2015)  26.600 €….Holding (9.2.2015-10.9.2019)  8.400 €……Ing. Michael FG2 (jedenfalls. 1.1.2008-12.4.2010)  9.100 €……Ing. Michael FG2 (13.4.2010-8.2.2015)  8.400 €……Ing. Michael FG2 9.2.2015  35.000 €….Summe

**False Positives:**

- `Ing. Michael` — no gold match — likely missing annotation
- `Ing. Michael` — no gold match — likely missing annotation
- `Ing. Michael` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Gold Entities:**

- `Traver-Planung GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/134154.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134154.1_166`)


8.400 €……Ing. Eduard FG4 (jedenf. 1.1.2008-12.4.2010)  9.100 €……Ing. Eduard FG4 (13.4.2010-25.1.2015)  8.400 €……Ing. Eduard FG4 (ab 26.1.2015)  35.000 € …Summe

**False Positives:**

- `Ing. Eduard` — no gold match — likely missing annotation
- `Ing. Eduard` — no gold match — likely missing annotation
- `Ing. Eduard` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/139401.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139401.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Dr. Dipl.-Ing. Laurence Goetke,  Unterernsthofen 11, 9311 Leiten, Österreich, vertreten durch STB, Adr1, über die Beschwerde vom 10. Dezember 2019  gegen den Bescheid des A vom 12. November 2019 betreffend Umsatzsteuer 2012,  Steuernummer 42-698/5318, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dipl.-Ing. Laurence Goetke` — partial — pred is substring of gold: `Dr. Dipl.-Ing. Laurence Goetke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Dipl.-Ing. Laurence Goetke`(person)
- `Unterernsthofen 11, 9311 Leiten, Österreich`(address)
- `42-698/5318`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/139695.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Deborah Stöbesand  in der Beschwerdesache des  Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke, Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich, über die Beschwerde vom 9. Juli 2022 gegen den Bescheid des  FA Waldviertel  vom 7. Juli 2022 betreffend Abweisung eines Antrages auf Wiederaufnahme der  Verfahren hinsichtlich Einkommensteuer für die Jahre 2017 bis 2019 zu Steuernummer  37-369/8758  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dipl.-Ing. Laurence Wiebecke` — partial — pred is substring of gold: `Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Deborah Stöbesand`(person)
- `Hon.-Prof.in Dipl.-Ing. Laurence Wiebecke`(person)
- `Joseph-Spring-Straße 16, 3110 Pultendorf, Österreich`(address)
- `FA Waldviertel`(organisation)
- `37-369/8758`(tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/141100.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141100.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait  in der Beschwerdesache   Prof. Ing. Eduard Skroblies, Forchetweg 18, 4692 Albertsham, Österreich,   über die Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf (nunmehr Finanzamt Österreich) vom 10. November 2014 betreffend  Körperschaftsteuer 2011, vom 19. November 2014 betreffend Körperschaftsteuer 2012 und  2013 sowie die Beschwerde vom 12. Juli 2016 gegen den Bescheid des Finanzamtes Wien  12/13/14 Purkersdorf vom 7. Juli 2016 betreffend Körperschaftsteuer 2014   I. beschlossen:  Der Vorlageantrag betreffend Körperschaftsteuer 2011 wird zurückgewiesen.

**False Positives:**

- `Ing. Eduard Skroblies` — partial — pred is substring of gold: `Prof. Ing. Eduard Skroblies`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Univ.-Prof.in Ariadne Jurkait`(person)
- `Prof. Ing. Eduard Skroblies`(person)
- `Forchetweg 18, 4692 Albertsham, Österreich`(address)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `Finanzamtes Wien  12/13/14 Purkersdorf`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/144141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Ing. Marion Kloefkorn, Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich, vertreten durch Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG, Innsbrucker Bundesstraße 83A, 5020 Salzburg, über die Beschwerde vom  25.3.2022 gegen den Bescheid des Finanzamtes Österreich vom 3.3.2022 betreffend  Einkommensteuer 2018 zur Steuernummer 40-620/0106  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing. Carl Paulitschky` — partial — pred is substring of gold: `Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Ing. Marion Kloefkorn`(person)
- `Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich`(address)
- `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `40-620/0106`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_190`)


Zu Vitamin B verwies  sie auf die Verschreibung von Neurobin durch Fr.Dipl.-Ing. Joseph Szwarz Dieses enthalte so viele andere  Zusatzstoffe.

**False Positives:**

- `Dipl.-Ing. Joseph Szwarz Dieses` — positional overlap with gold: `Fr.Dipl.-Ing. Joseph Szwarz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Fr.Dipl.-Ing. Joseph Szwarz`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/146212.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146212.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Daniela Regina Denk über die  Beschwerde der Dipl.-Ing. Mag.a Andrea Johanningmeyer, Tenniszeile 8, 5424 Rengerberg, Österreich, vertreten durch Susanne Neuhäuser, Hartiggasse  22/23, 2700 Wiener Neustadt, vom 12. Dezember 2019 gegen den Bescheid des Finanzamt Schwechat Gerasdorf  vom  26. November 2019 betreffend Zwangsstrafen 2019 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dipl.-Ing. Mag` — partial — pred is substring of gold: `Dipl.-Ing. Mag.a Andrea Johanningmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Daniela Regina Denk`(person)
- `Dipl.-Ing. Mag.a Andrea Johanningmeyer`(person)
- `Tenniszeile 8, 5424 Rengerberg, Österreich`(address)
- `Susanne Neuhäuser`(person)
- `Finanzamt Schwechat Gerasdorf`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/146212.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146212.1_7`)


An diese E-Mail- Adresse antwortete die WiEReG-Behörde mit einem E-Mail an die zum damaligen Zeitpunkt  geschäftsführende Gesellschafterin, datiert mit 25.05.2019, worin Folgendes mitgeteilt wurde:  "Bezugnehmend auf Ihr Schreiben betreffend die Meldebefreiung der Dipl.-Ing. Mag.a Andrea Johanningmeyer  darf ich Ihnen  mitteilen, dass die Meldebefreiung nach § 6 WiEReG nur dann greift, sofern ausschließlich  1 von 8 Seite 2 von 8

**False Positives:**

- `Dipl.-Ing. Mag` — partial — pred is substring of gold: `Dipl.-Ing. Mag.a Andrea Johanningmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. Mag.a Andrea Johanningmeyer`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/146212.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146212.1_23`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   An der Dipl.-Ing. Mag.a Andrea Johanningmeyer  sind ***Gesellschafterin unbeschr1*** als unbeschränkt haftende  Gesellschafterin und der Verein „***“ als Kommanditist im verfahrensgegenständlichen  Zeitraum beteiligt.

**False Positives:**

- `Dipl.-Ing. Mag` — partial — pred is substring of gold: `Dipl.-Ing. Mag.a Andrea Johanningmeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dipl.-Ing. Mag.a Andrea Johanningmeyer`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_41`)


XXX/2 und XXX/4 per E-Mail an w.p. @ ...at  übermittelt.   Am 12.08.2010 wurde die Übergabe des Grundstücks EZ xxx Grundbuch A-Ort, A-Platz, A-Ort in  der Konkurssache Fa. A-KG von Anwalt StR Ing. Hedwig Mendle als Masseverwalter der KG an die Bf.,  vertreten durch M.M.A., als Käufer auf der Grundlage des Kaufvertrags vom 28.04.2010  protokolliert.

**False Positives:**

- `Ing. Hedwig Mendle` — partial — pred is substring of gold: `StR Ing. Hedwig Mendle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `StR Ing. Hedwig Mendle`(person)
- `M.M.A.`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/149204.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149204.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag.a Dipl.-Ing. Leya Mentzel, MSc, Spitzerbergstraße 29, 6858 Bildstein, Österreich, vertreten durch Bernhart Steuerberatungs  GmbH, Albertgasse 35/15, 1080 Wien, über die Beschwerde vom 28. Juli 2022 gegen die  Bescheide des Finanzamtes Österreich vom 1. Juli 2022 betreffend Einkommensteuer 2018 und  Umsatzsteuer 2018 bis 2021, Steuernummer 14-471/3359, zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dipl.-Ing. Leya Mentzel` — partial — pred is substring of gold: `Mag.a Dipl.-Ing. Leya Mentzel, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag.a Dipl.-Ing. Leya Mentzel, MSc`(person)
- `Spitzerbergstraße 29, 6858 Bildstein, Österreich`(address)
- `Bernhart Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `14-471/3359`(tax_number)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Alessia von Bauer  in der Beschwerdesache  Dimitri Seelos, geb. am 19. November 1987  und Dipl.-Ing. Luna Goedecken, BEd MA, geb. am 12. April 1988  als Erben  des Reneé Keles, verstorben am 3. November 1972  über die Beschwerde vom 15. Dezember 2020  gegen die Bescheide des Finanzamtes Österreich vom 27. November 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2015 bis 2019;

**False Positives:**

- `Dipl.-Ing. Luna Goedecken` — partial — pred is substring of gold: `Dipl.-Ing. Luna Goedecken, BEd MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Alessia von Bauer`(person)
- `Dimitri Seelos`(person)
- `19. November 1987`(date)
- `Dipl.-Ing. Luna Goedecken, BEd MA`(person)
- `12. April 1988`(date)
- `Reneé Keles`(person)
- `3. November 1972`(date)
- `Finanzamtes Österreich`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_25`)


Mit 3. November 1972  verstarb der Bf. Mit Einantwortungsbeschluss des Bezirksgerichtes  Mattighofen vom 06.06.2023 wurde die Verlassenschaften den erblichen Kindern Dimitri Seelos  und Dipl.-Ing. Luna Goedecken, BEd MA  nach Abgabe einer unbedingten Erbserklärung eingeantwortet.

**False Positives:**

- `Dipl.-Ing. Luna Goedecken` — partial — pred is substring of gold: `Dipl.-Ing. Luna Goedecken, BEd MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `3. November 1972`(date)
- `Dimitri Seelos`(person)
- `Dipl.-Ing. Luna Goedecken, BEd MA`(person)

</details>

---

## `Complainant_Beschwerdesache` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1c1c43df`  
**Description:**
Captures person names following 'in der Beschwerdesache', ensuring the name starts with a capitalized letter, includes titles if present, and captures full name with suffixes like BEd, Bakk. phil., LL.M.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Verwaltungsstrafsache)\s+)(?:des\s+|der\s+)?(?:Hon\.-Prof\.(?:in)?\s+|Dr\.(?:in\s+Dipl\.(?:Kff\.)?\s+|in)?\s+|Priv\.-Doz\.(?:in)?\s+|Mag\.(?:Dr\.)?\s+|Univ\.-Prof\.(?:in)?\s+|Bakk\.(?:\s+rer\.\s+nat\.|\s+rer\.\s+art\.|\s+rer\.\s+techn\.|\s+rer\.\s+jur\.|\s+phil\.|\s+iur\.|\s+techn\.)?\s+|Ing\.(?:\s+Dipl\.)?\s+|Mag\.a\s+|Prof\.in\s+|Prof\.(?:in)?\s+|RA\s+Mag\.(?:in)?\s+|DDr\.(?:in)?\s+|MedR\.(?:in)?\s+|RgR\.(?:in)?\s+|KzlR\.(?:in)?\s+|VetR\.(?:in)?\s+|KommR\.(?:in)?\s+|OSR\s+|\u00d6kR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)(?=,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137581.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache OSR Eugenia Balikci, Richardisweg 14, 5134 Ginshöring, Österreich, vertreten durch Wiener Kinder-und Jugendhilfe  2,20, Dresdner Straße 43, 1200 Wien, über die Beschwerde vom 20. März 2020 gegen den  Bescheid des Finanzamtes Österreich vom 25. Februar 2020 betreffend Familienbeihilfe ab  Jänner 2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Eugenia Balikci` — partial — pred is substring of gold: `OSR Eugenia Balikci`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `OSR Eugenia Balikci`(person)
- `Richardisweg 14, 5134 Ginshöring, Österreich`(address)
- `Wiener Kinder-und Jugendhilfe`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/147552.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147552.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Jörg Novakowski  in der Beschwerdesache OSR Samantha Schaffroth,  Kaltenbach 71, 3353 Biberbach, Österreich, über die Beschwerde vom 16. September 2020 gegen den Bescheid des  FA Niederösterreich Mitte  vom 21. August 2022, mit welchen der Antrag auf Wiederaufnahme der Verfahren  betreffend Einkommensteuer für die Jahr 2015 bis 2017 gem. § 303 BAO abgewiesen wurde, zu  Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Samantha Schaffroth` — partial — pred is substring of gold: `OSR Samantha Schaffroth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Jörg Novakowski`(person)
- `OSR Samantha Schaffroth`(person)
- `Kaltenbach 71, 3353 Biberbach, Österreich`(address)
- `FA Niederösterreich Mitte`(organisation)

</details>

---

## `Role_Followed_Name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `58fa76b7`  
**Description:**
Captures person names immediately following legal roles like 'Beschuldigte', 'Verteidiger', 'Zeuge', 'Anwalt', 'Klient', 'Prüferin', 'Prüfer', 'Steuerberater', 'Sachverständiger', 'Vertreter', 'Vertreterin', ensuring full title and name.

**Content:**
```
(?:Beschuldigte|Verteidiger|Zeuge|Anwalt|Klient|Prüferin|Prüfer|Steuerberater|Sachverständiger|Vertreter|Vertreterin|E-Mail|Niederschrift|Stellungnahme|Verteidiger des|Verteidigerin des|Verteidigerin)\b(?:\s+(?:Hon\.-Prof\.|Dr\.|Mag\.|RA\s+Mag\.|Ing\.|Bakk\.|Priv\.-Doz\.|Univ\.-Prof\.|MedR\.|RgR\.|KzlR\.|VetR\.|KommR\.|DDr\.|Mag\.a\s+|Prof\.in\s+|Prof\.|OSR\s+|OMedR\s+)?\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/141221.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141221.1_68`)


Beweiswürdigung:  Der Sachverhalt ergibt sich aus dem Verwaltungsakt und den Daten des umfangreichen E-Mail  Verkehrs zwischen dem Bf. und der belangten Behörde.

**False Positives:**

- `E-Mail  Verkehrs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_96`)


Auch die  Werthaltigkeit der einzelnen baulichen Maßnahmen zum Zeitpunkt der Veräußerung hat die  Beschwerdeführerin im Zuge des Erörterungstermins eingestanden (siehe Niederschrift  Erörterungstermin vom 23.9.2024 unter Verweis auf Parallelverfahren).

**False Positives:**

- `Niederschrift  Erörterungstermin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_107`)


Richtig ist, was die Parteien ohnedies außer Streit stellten (siehe Niederschrift  Erörterungstermin vom 23.9.2024), dass zum Zeitpunkt der Zustellung der strittigen Bescheide  das im Rahmen der Amtssignatur verwendete Zwischeninstanzzertifikat „a-sign-corporoate-07“  nicht in der Zwischeninstanzzertifikatsdatenbank der Firma A-Trust veröffentlicht war.

**False Positives:**

- `Niederschrift  Erörterungstermin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Email_Header_Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `495ef954`  
**Description:**
Captures names in email headers like 'E-Mail [Date] [Name] an [Name]'.

**Content:**
```
(?:E-Mail|E-Mail-Verkehr)\s+(?:\d{1,2}\.\s*\d{1,2}\.\s*\d{2,4}|\d{1,2}\.\s*\w+\.\s*\d{4}|\d{1,2}\.\s*\w+\.\s*\d{4})\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*)\s+(?:an|von)\s+(?:den|der|dem|die|Herrn|Frau|Beschuldigten|Beschuldigte|Anwalt|Verteidiger|Klient|Zeuge|Prüfer|Steuerberater|Sachverständiger|Vertreter|Vertreterin|Mag\.\s+|Dr\.\s+|RA\s+Mag\.\s+|Ing\.\s+|Bakk\.\s+|Priv\.-Doz\.\s+|Univ\.-Prof\.\s+|Hon\.-Prof\.\s+|MedR\.\s+|RgR\.\s+|KzlR\.\s+|VetR\.\s+|KommR\.\s+|DDr\.\s+)?[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Representative_Dr_Mag` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b8dad841`  
**Description:**
Captures person names following 'vertreten durch' or 'durch', ensuring the match does not include company suffixes like 'GmbH'.

**Content:**
```
(?:vertreten\s+durch|durch)\s+(?:Hon\.-Prof\.(?:in)?|Dr\.(?:in\s+Dipl\.(?:Kff\.)?|in)?|Priv\.-Doz\.(?:in)?|Mag\.(?:Dr\.)?|Univ\.-Prof\.(?:in)?|Bakk\.|Ing\.|Mag\.a\s+|Prof\.in\s+|Prof\.|RA\s+Mag\.|OSR\s+|OMedR\s+)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)(?=,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 41 | 0 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 41 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/127198.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/127198.1_0`)


GZ. RV/6100630/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter    Mag. Erich Schwaiger    über die Beschwerde    vom 4. September 2017    des Beschwerdeführers Jeannette Neuschwender   , Zum Kogl 12, 4441 Penz, Österreich, vertreten durch die mit Zustellvollmacht ausgewiesene zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH, 5020 Salzburg, Mildenburggasse 4a,    gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg, Aignerstraße 10 vertreten durch Mag. Peter Staudinger, vom 10. August 2017 betreffend Einkommensteuer 2015 zu Recht erkannt: I) Der Einkommensteuerbescheid 2015 wird abgeändert.

**False Positives:**

- `vertreten durch Mag. Peter Staudinger` — partial — gold is substring of pred: `Mag. Peter Staudinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `Jeannette Neuschwender`(person)
- `Zum Kogl 12, 4441 Penz, Österreich`(address)
- `zobl.bauer Salzburg Steuerberatung und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `Mag. Peter Staudinger`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch Mag. Manfred Frühwirth, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

**False Positives:**

- `vertreten durch Mag. Manfred Frühwirth` — partial — gold is substring of pred: `Mag. Manfred Frühwirth`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Reneé Dreyssig`(person)
- `Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich`(address)
- `Mag. Manfred Frühwirth`(person)
- `Finanzamtes Linz`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rosamunde Galanidis  in der Beschwerdesache Hermine Ruprich,  Riedmarkstraße 219, 4175 Felsleiten, Österreich, vertreten durch Mag. Wolfgang Moser, Wächtergasse 1, 1010 Wien, über die  Beschwerde vom 20. September 2018 gegen die Bescheide des Finanzamt Kirchdorf Perg Steyr  vom 10. September  2018 betreffend  1) Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36;

**False Positives:**

- `vertreten durch Mag. Wolfgang Moser` — partial — gold is substring of pred: `Mag. Wolfgang Moser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Rosamunde Galanidis`(person)
- `Hermine Ruprich`(person)
- `Riedmarkstraße 219, 4175 Felsleiten, Österreich`(address)
- `Mag. Wolfgang Moser`(person)
- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_283`)


Mit der Übernahme des aufgezeigten Schwunds und Personalverbrauchs, obwohl "keine  Aufzeichnungen" hinsichtlich Schwund und Personalverbrauch vorgelegt werden konnten,  seien die konkreten Unterlagen, die nach Ansicht der Betriebsprüfung hinsichtlich des durch  Verlust, Verderb, Malversationen (allgemein: Schwund) herbeigeführten Warenabgangs  vorgelegt werden hätten sollen, zu hinterfragen.

**False Positives:**

- `durch  Verlust` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/131107.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131107.1_67`)


Der behauptete Wegfall des Hauptauftraggebers bzw. das Nichteinhalten von Zusagen durch  Hotelbetriebe (Vorbringen im Vorlageantrag) mögen zu einer schlechten Ertragslage beitragen,  jedoch konnte das Bundesfinanzgericht mangels Vorlage der Ausgangsrechnungen und  mangels Nachweises, wann welche Leistungen an wen erbracht wurden, das Gewicht dieses  Vorbringens in Hinblick auf die konkrete Ertragslage der Beschwerdeführerin nicht beurteilen.

**False Positives:**

- `durch  Hotelbetriebe` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/132145.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132145.1_81`)


Im beschwerdegegenständlichen Fall erfolgte die Fruchtgenussvereinbarung durch  Notariatsakt, sodass das Publizitätserfordernis jedenfalls erfüllt ist.

**False Positives:**

- `durch  Notariatsakt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/132823.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132823.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Sandra Fenn, Myrbachgasse 59, 8403 Ragnitz, Österreich, vertreten durch Mag. Manuela Meyerhofer, Handlirschgasse 11, 1170 Wien, über die  Beschwerde vom 18. Jänner 2016 gegen den Bescheid des Finanzamtes Bruck Eisenstadt  Oberwart vom 15. Dezember 2015 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2014, Steuernummer 49-433/1564, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Mag. Manuela Meyerhofer` — partial — gold is substring of pred: `Mag. Manuela Meyerhofer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sandra Fenn`(person)
- `Myrbachgasse 59, 8403 Ragnitz, Österreich`(address)
- `Mag. Manuela Meyerhofer`(person)
- `Finanzamtes Bruck Eisenstadt  Oberwart`(organisation)
- `49-433/1564`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc über die  Beschwerde des Evelyn Antwerber, Hertzstraße 25, 5134 Spieglern, Österreich, vertreten durch Dr. Farid Rifaad, Schmerlingplatz  3/6, 1010 Wien, vom 14. Dezember 2020 gegen die nachfolgend angeführten sechs  Straferkenntnisse des Magistrates der Stadt Wien, Magistratsabteilung 67,

**False Positives:**

- `vertreten durch Dr. Farid Rifaad` — partial — gold is substring of pred: `Dr. Farid Rifaad`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Evelyn Antwerber`(person)
- `Hertzstraße 25, 5134 Spieglern, Österreich`(address)
- `Dr. Farid Rifaad`(person)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Fatima Eichmayr, Wieskapellenweg 10, 8047 Graz, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in 5020 Salzburg, Hellbrunner Straße 5,  über die Beschwerde vom 8. Jänner 2010 gegen die Bescheide des Finanzamtes Salzburg-Stadt  (nunmehr: Finanzamt Österreich) vom 12. November 2009 betreffend Haftung für  Kapitalertragsteuer für 2004 bis 2008, Steuernummer 67-455/2359, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `vertreten durch Dr. Klaus Plätzer` — positional overlap with gold: `Dr. Klaus Plätzer,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Fatima Eichmayr`(person)
- `Wieskapellenweg 10, 8047 Graz, Österreich`(address)
- `Dr. Klaus Plätzer,`(person)
- `Finanzamtes Salzburg-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)
- `67-455/2359`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/134323.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134323.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Bernhard Maximowa, Wienergraben 7, 2870 Inneraigen, Österreich, vertreten durch Mag. Robert Dax, Schöpfstraße 39 Tür Top 3, 6020 Innsbruck, gegen  die Bescheide des Finanzamtes Gmunden Vöcklabruck vom 9. November 2015 zu  Steuernummer Bf1StNr über die Festsetzung von  Anspruchszinsen 2010, 2011, 2012, und 2013  beschlossen:  Der Vorlageantrag gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `vertreten durch Mag. Robert Dax` — partial — gold is substring of pred: `Mag. Robert Dax`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bernhard Maximowa`(person)
- `Wienergraben 7, 2870 Inneraigen, Österreich`(address)
- `Mag. Robert Dax`(person)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_231`)


Lebensjahres war, ist weder  durch zeitnahe noch durch zeitferne medizinisch-diagnostische Unterlagen, allenfalls durch  Rückschluss, belegt.

**False Positives:**

- `durch  Rückschluss` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/134539.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134539.1_29`)


Die Nominierung kann durch  Trafikanten, Mitarbeiter, aber auch D.-MA vorgenommen werden, und wird durch die jeweilige  Jury bewertet.

**False Positives:**

- `durch  Trafikanten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/135526.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135526.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Armin Heckemanns, Nabuccogasse 10, 2630 Ternitz, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, (im  Beschwerdeverfahren nicht eingeschritten), über die Beschwerde vom 10. Februar 2020 gegen  den Einkommensteuerbescheid 2018 des Finanzamtes Baden Mödling vom 10. Jänner 2020  (und gemäß § 253 Satz 1 BAO auch gegen den Einkommensteuerbescheid 2018 vom  18. September 2020) zu Steuernummer 75-597/1615  zu Recht erkannt:  Gemäß § 279 BAO wird der Beschwerde teilweise Folge gegeben und der angefochtene  Bescheid abgeändert.

**False Positives:**

- `vertreten durch Dr. Silvia Gredenberg` — partial — gold is substring of pred: `Dr. Silvia Gredenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Armin Heckemanns`(person)
- `Nabuccogasse 10, 2630 Ternitz, Österreich`(address)
- `Dr. Silvia Gredenberg`(person)
- `Finanzamtes Baden Mödling`(organisation)
- `75-597/1615`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/136097.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136097.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Sulamith Jedwillat, Brandenbergweg 15, 8353 Pichla, Österreich, vertreten durch Mag. Michael Payr, Albertgasse 6/14, 1080 Wien, über die  Beschwerde vom 25. Oktober 2018 gegen den Bescheid des Finanzamtes Wien 12/13/14  Purkersdorf, nunmehr Finanzamt Österreich, vom 19. September 2018 betreffend  Körperschaftsteuer 2014, Steuernummer 41-852/7395, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `vertreten durch Mag. Michael Payr` — partial — gold is substring of pred: `Mag. Michael Payr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sulamith Jedwillat`(person)
- `Brandenbergweg 15, 8353 Pichla, Österreich`(address)
- `Mag. Michael Payr`(person)
- `Finanzamtes Wien 12/13/14  Purkersdorf`(organisation)
- `Finanzamt Österreich`(organisation)
- `41-852/7395`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/136304.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136304.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sheila Nonnmacher  in der Beschwerdesache Sieglinde Semertzidou,  Bürgerspitalstraße 8, 9361 Judendorf, Österreich, vertreten durch Dr. Silvia Gredenberg, Hagenberggasse 29, 1130 Wien, über  die Beschwerde vom 20.03.2017 gegen die Umsatzsteuerbescheide 2007 bis 2008 „aufgrund  der BP“, Steuernummer 76-265/6028, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

**False Positives:**

- `vertreten durch Dr. Silvia Gredenberg` — partial — gold is substring of pred: `Dr. Silvia Gredenberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Sheila Nonnmacher`(person)
- `Sieglinde Semertzidou`(person)
- `Bürgerspitalstraße 8, 9361 Judendorf, Österreich`(address)
- `Dr. Silvia Gredenberg`(person)
- `76-265/6028`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/137535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137535.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Julian Egiede, Theras 97, 4565 Haselbäckau, Österreich, vertreten durch Mag. Grün  Steuerberatungsgesellschaft mbH, Stiegengasse 1, 9300 St. Veit an der Glan, über die  Beschwerde vom 08. Juni 2018 gegen den Bescheid des Finanzamtes Klagenfurt (nunmehr  Finanzamt Österreich, vertreten durch Mag. Michael Sablatnik, vom 16. Mai 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 Steuernummernummer 88-033/6865  zu Recht:   Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `vertreten durch Mag. Michael Sablatnik` — partial — gold is substring of pred: `Mag. Michael Sablatnik`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Julian Egiede`(person)
- `Theras 97, 4565 Haselbäckau, Österreich`(address)
- `Mag. Grün  Steuerberatungsgesellschaft mbH`(organisation)
- `Finanzamtes Klagenfurt`(organisation)
- `Finanzamt Österreich`(organisation)
- `Mag. Michael Sablatnik`(person)
- `88-033/6865`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  Volkmar Quadfasel, Forstbergstraße 5, 4144 Zanklbach, Österreich, vertreten durch Dr. Sebastian Mariano Volkmar Lenz,  Laurenzerberg 1, 1010 Wien, vom 25. April 2021, gegen den Bescheid des Finanzamtes  Österreich vom 26. März 2021, betreffend Abweisung des Antrages auf Gewährung des  Erhöhungsbetrages zur Familienbeihilfe ab Dezember 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Dr. Sebastian Mariano Volkmar Lenz` — partial — gold is substring of pred: `Dr. Sebastian Mariano Volkmar Lenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Pavlik`(person)
- `Volkmar Quadfasel`(person)
- `Forstbergstraße 5, 4144 Zanklbach, Österreich`(address)
- `Dr. Sebastian Mariano Volkmar Lenz`(person)
- `Finanzamtes  Österreich`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_143`)


Sie legt auch eine Liste mit Problemen vor: Kommunikation, soziale Situation deuten, Sonnen- lichtempfindlichkeit, Lärmempfindlichkeit, Geruchsempfindlichkeit, Überlastung u.a. durch  Reizüberflutung, Sinneswahrnehmungen, Migräne, Ängste (Spinnen, Flugreisen, Schiffe, Feuer,  unkontrollierbare Situationen, Aufzüge, Tunnel) Konzentrationsprobleme, Rechtschreib- schwäche, Schlafprobleme, va.

**False Positives:**

- `durch  Reizüberflutung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/139596.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139596.1_30`)


Wird bei getrenntlebenden Elternteilen die gesetzliche Unterhaltsverpflichtung durch  Naturalunterhalt (Sachleistung) erfüllt, steht der unterhaltsverpflichteten Person der  Unterhaltsabsetzbetrag zu.  Die Bf. hat nachgewiesen, dass sie ihren gesetzlichen Unterhaltsverpflichtungen in vollem  Umfang nachgekommen ist.

**False Positives:**

- `durch  Naturalunterhalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/140216.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140216.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache RgR Denise Symang, Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich, vertreten durch Mag. Robert Bitsche,  Rechtsanwalt, Nikolsdorfergasse 7-11/15, 1050 Wien, über die Beschwerde vom 9. Oktober  2019 gegen die Bescheide des Finanzamtes Wien 4/5/10 (nunmehr Finanzamt Österreich) vom  11. September 2019 sowie vom 23. September 2019 betreffend Wiederaufnahme  Körperschaftsteuer 2015 bis 2017, Steuernummer 60-977/8084, nach Durchführung einer  mündlichen Verhandlung am 19. Dezember 2022, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Mag. Robert Bitsche` — partial — gold is substring of pred: `Mag. Robert Bitsche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `RgR Denise Symang`(person)
- `Matthäus-Schili-Straße 5, 8262 Buchberg bei Ilz, Österreich`(address)
- `Mag. Robert Bitsche`(person)
- `Finanzamtes Wien 4/5/10`(organisation)
- `Finanzamt Österreich`(organisation)
- `60-977/8084`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/140867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140867.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Philipp Nosalek  in der Beschwerdesache Merlin Buechner,  Am Waldfriedhof 19-24, 4714 Gferet, Österreich, vertreten durch Dr. Martin Eisenberger, Muchargasse 30, 8010 Graz, über die  Beschwerde vom 17. Mai 2017 gegen den Bescheid des Zollamtes Österreich vom 11. April  2017, Zl. 700000/03287/2017, betreffend Aussetzungszinsen zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `vertreten durch Dr. Martin Eisenberger` — partial — gold is substring of pred: `Dr. Martin Eisenberger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Philipp Nosalek`(person)
- `Merlin Buechner`(person)
- `Am Waldfriedhof 19-24, 4714 Gferet, Österreich`(address)
- `Dr. Martin Eisenberger`(person)
- `Zollamtes Österreich`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/141318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141318.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Lara Blaßl, Singsdorf 15, 9622 St. Lorenzen im Gitschtal, Österreich, vertreten durch Dr. Michl Münzker, Landskrongasse 5 Tür 4, 1010  Wien, über die Beschwerde vom 24. Juni 2021 gegen den Bescheid des Finanzamtes Österreich  vom 17. Juni 2021 betreffend Festsetzung einer Zwangsstrafe, Steuernummer  54-324/8831, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Dr. Michl Münzker` — partial — gold is substring of pred: `Dr. Michl Münzker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Lara Blaßl`(person)
- `Singsdorf 15, 9622 St. Lorenzen im Gitschtal, Österreich`(address)
- `Dr. Michl Münzker`(person)
- `Finanzamtes Österreich`(organisation)
- `54-324/8831`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/141441.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141441.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dr. Finn Rosen  in der Beschwerdesache Dragan Ohlff,  vertreten durch Dr. Sven Rudolf Thorstensen LLM, Neustiftgasse 3/7, 1070 Wien, über die  Beschwerde vom 23. Juli 2019 gegen den Bescheid des Finanzamtes Baden Mödling vom  10. Juli 2019 betreffend den Bescheid über den Ablauf einer Aussetzung der Einhebung zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Dr. Sven Rudolf Thorstensen LLM` — partial — gold is substring of pred: `Dr. Sven Rudolf Thorstensen LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Dr. Finn Rosen`(person)
- `Dragan Ohlff`(person)
- `Dr. Sven Rudolf Thorstensen LLM`(person)
- `Finanzamtes Baden Mödling`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/141846.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141846.1_19`)


Falls der Beschwerdeführer einen Zustellmangel  geltend machen wolle, habe er innerhalb der gleichen Frist die Möglichkeit, diesen durch  Belege (Reiserechnungen, Namhaftmachung von Zeugen, etc.) glaubhaft zu machen.

**False Positives:**

- `durch  Belege` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/141990.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141990.1_2`)


Das Bundesfinanzgericht hat durch die Senatsvorsitzende R1, den RichterR2, sowie die  fachkundigen Laienrichter R3 und R4, in der Beschwerdesache VetR Maja Waatsack, Sarottla 115, 8522 Sulzhof, Österreich,  vertreten durch Mag. Wolfgang Schranz, Mahlerstraße 11 Tür 4, 1010 Wien, über die  Beschwerde vom 28. Oktober 2016 gegen die Bescheide des Finanzamtes Wien 8/16/17 vom  25. Juli 2016 betreffend Umsatzsteuer sowie Feststellung der Einkünfte gemäß § 188 BAO für  2009, sowie vom 24. August 2016 betreffend Umsatzsteuer und Feststellung der Einkünfte  gemäß § 188 BAO für die Jahre 2010 bis 2015, Steuernummer 31-345/4688, in der Sitzung  vom 30. August 2023 nach Durchführung einer mündlichen Verhandlung am 30. August 2023 in  Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Mag. Wolfgang Schranz` — partial — gold is substring of pred: `Mag. Wolfgang Schranz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `VetR Maja Waatsack`(person)
- `Sarottla 115, 8522 Sulzhof, Österreich`(address)
- `Mag. Wolfgang Schranz`(person)
- `Finanzamtes Wien 8/16/17`(organisation)
- `31-345/4688`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/142019.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142019.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache KzlR Techn R RgR Wigand Beinhorn, Salfeldstraße 54, 9500 Oberwollanig, Österreich, vertreten durch Dr. Robert Austaller, Wildshut 16, 5120 St. Pantaleon, über die  Beschwerde vom 3. März 2021 gegen den Bescheid des Finanzamtes Österreich vom  11. Februar 2021 betreffend Rechtsgebühr, Steuernummer 98-325/7724,  Erfassungsnummer 10-2021, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `vertreten durch Dr. Robert Austaller` — partial — gold is substring of pred: `Dr. Robert Austaller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `KzlR Techn R RgR Wigand Beinhorn`(person)
- `Salfeldstraße 54, 9500 Oberwollanig, Österreich`(address)
- `Dr. Robert Austaller`(person)
- `Finanzamtes Österreich`(organisation)
- `98-325/7724`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/142259.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin I. in der Beschwerdesache Laurin Borchardt, Untertweng-Gartenstraße 24, 4085 Saulehen, Österreich, vertreten durch Dr. Leopold Boyer, Hauptstr 23-25, 2225 Zistersdorf, über die  Beschwerde vom 27. Jänner 2014 gegen den Bescheid des Finanzamtes Klagenfurt vom  20. Dezember 2013 betreffend Umsatzsteuer 1998 bis 2011 sowie Feststellung von Einkünften  1999 bis 2011 zu Steuernummer 05-890/5761  nach der am 27.07.2023 im Beisein der  Schriftführerin *** durchgeführten mündlichen Verhandlung zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `vertreten durch Dr. Leopold Boyer` — partial — gold is substring of pred: `Dr. Leopold Boyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Laurin Borchardt`(person)
- `Untertweng-Gartenstraße 24, 4085 Saulehen, Österreich`(address)
- `Dr. Leopold Boyer`(person)
- `Finanzamtes Klagenfurt`(organisation)
- `05-890/5761`(tax_number)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/143074.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143074.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Joachim Sakarya, Augenbrünnl-Gasse 32, 9131 Tainacherfeld, Österreich, vertreten durch Dr. Robert Karl Galler, Viktor-Keldorfer-Straße 1,  5020 Salzburg, über die Beschwerde vom 14. Jänner 2022 gegen den Bescheid des Finanzamtes  Österreich vom 13. Dezember 2021 betreffend Abweisung eines Aussetzungsantrages gem. §  212a BAO, Steuernummer 94-841/9471  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Dr. Robert Karl Galler` — partial — gold is substring of pred: `Dr. Robert Karl Galler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Joachim Sakarya`(person)
- `Augenbrünnl-Gasse 32, 9131 Tainacherfeld, Österreich`(address)
- `Dr. Robert Karl Galler`(person)
- `Finanzamtes  Österreich`(organisation)
- `94-841/9471`(tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/143673.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Sebastian Kötters  in der Beschwerdesache Agnes Hundorf,  Bischofsberg 23, 9123 Unterkrain, Österreich, vertreten durch Mag. Helmut Hirsch Rechtsanwalt, Josef-Krainer-Straße 46/I,  8074 Raaba, über die Beschwerde vom 2. August 2013 gegen den Bescheid des Finanzamt Judenburg Liezen  vom  4. Juli 2013 betreffend Pfändung einer Geldforderung zu Steuernummer 65-832/4960  zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `vertreten durch Mag. Helmut Hirsch Rechtsanwalt` — partial — gold is substring of pred: `Mag. Helmut Hirsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Sebastian Kötters`(person)
- `Agnes Hundorf`(person)
- `Bischofsberg 23, 9123 Unterkrain, Österreich`(address)
- `Mag. Helmut Hirsch`(person)
- `Finanzamt Judenburg Liezen`(organisation)
- `65-832/4960`(tax_number)

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/143791.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143791.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Erhard Gruetter  in der Beschwerdesache René Kleser,  Dauerkleingärten 17M, 5112 Gresenberg, Österreich, vertreten durch Mag. Andreas Schnegg, Kalkofenstraße 24, 6425 Haiming, über  die Beschwerde vom 19. Februar 2022 gegen den Bescheid des FA Wien 8/16/17  vom 21. Jänner 2022  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016, Steuernummer  85-777/9690, zu Recht erkannt:  I. Der Beschwerde wird teilweise Folge gegeben.

**False Positives:**

- `vertreten durch Mag. Andreas Schnegg` — partial — gold is substring of pred: `Mag. Andreas Schnegg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Erhard Gruetter`(person)
- `René Kleser`(person)
- `Dauerkleingärten 17M, 5112 Gresenberg, Österreich`(address)
- `Mag. Andreas Schnegg`(person)
- `FA Wien 8/16/17`(organisation)
- `85-777/9690`(tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/143819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143819.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Rauscher und Mag. Glashüttner  als Richter sowie Mag. Aust und Dr. Haid als fachkundige Laienrichter im Beisein des  Schriftführers FOI Dawkins über die Beschwerden der Marion Füchtmann, Hofhaimerplatz 90, 8663 Großveitsch, Österreich, vertreten durch  Dr. Alma Goerts, Primus-Lessiak Weg 6H, 9343 Dielach, Österreich, vom 13.03.2023 gegen den (Sammel-)Bescheid des  Finanzamtes Österreich vom 21.02.2023 betreffend Abweisung von Anträgen auf  Wiedereinsetzung in den vorigen Stand nach mündlicher Verhandlung zu Recht erkannt:  Die Beschwerden werden als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch  Dr. Alma Goerts` — partial — gold is substring of pred: `Alma Goerts`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Rauscher`(person)
- `Mag. Glashüttner`(person)
- `Mag. Aust`(person)
- `Dr. Haid`(person)
- `Marion Füchtmann`(person)
- `Hofhaimerplatz 90, 8663 Großveitsch, Österreich`(address)
- `Alma Goerts`(person)
- `Primus-Lessiak Weg 6H, 9343 Dielach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_369`)


Für nachfolgende Aufwendungen fehlt es nach dem vorliegenden Ermittlungsergebnis an den  Voraussetzungen für einen Abzug als außergewöhnliche Belastung:   2018:  Behandlungs-/Therapiekosten, Medikamentenaufwand:  - 49,- € Dr-A (lt. Bf 17.2.2018): trotz FA-Anforderung vom 27.Aug.2020 kein Nachweis durch  Rechnung, Zahlungsbeleg oder ÖGK-Kostenersatz;  - 395,- € Dr-B (Zahlung 24.7.2018): trotz FA-Anforderung am 27.Aug.2020 kein Nachweis durch  Rechnung oder ÖGK-Kostenersatz ;  - 190,- € MRT Privatklinik-X (Zahlung 12.3.2018): trotz FA-Anforderung vom 27.Aug.2020 weder  Nachweis durch Rechnung/ ÖGK-Kostenersatz noch über die medizinische Notwendigkeit der  umgehenden Durchführung in einer Privateinrichtung;

**False Positives:**

- `durch  Rechnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `ÖGK`(organisation)
- `ÖGK`(organisation)
- `ÖGK`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/145502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145502.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor in der Beschwerdesache  Lilia Kientze, Techtlgasse 1, 4720 Niederleithen, Österreich, vertreten durch Mag. Magdalena Anna Katharina Ferner, Hernalser  Hauptstrasse 35/14+15, 1170 Wien, über die Beschwerde vom 16. März 2022 gegen den  Bescheid des Finanzamtes Österreich vom 24. Februar 2022 betreffend Abweisung eines  Antrages auf Ausgleichzahlung Familienbeihilfe 08.2020  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `vertreten durch Mag. Magdalena Anna Katharina Ferner` — partial — gold is substring of pred: `Mag. Magdalena Anna Katharina Ferner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Doktor`(person)
- `Lilia Kientze`(person)
- `Techtlgasse 1, 4720 Niederleithen, Österreich`(address)
- `Mag. Magdalena Anna Katharina Ferner`(person)
- `Finanzamtes Österreich`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/145762.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145762.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Bruno Hübscher in der Beschwerdesache  Anton Brouwers, Waldenstein 10, 9821 Söbriach, Österreich, vertreten durch Dr. Maria Brandstetter, Stephansplatz 4/VIII, 1010  Wien, über die Beschwerden vom 21. Februar 2013 und vom 4. März 2013 gegen folgende  Bescheide des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr:  Finanzamt Österreich), ergangen zu Steuernummer 75-923/4499,  1.

**False Positives:**

- `vertreten durch Dr. Maria Brandstetter` — partial — gold is substring of pred: `Dr. Maria Brandstetter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Bruno Hübscher`(person)
- `Anton Brouwers`(person)
- `Waldenstein 10, 9821 Söbriach, Österreich`(address)
- `Dr. Maria Brandstetter`(person)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)
- `75-923/4499`(tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/145807.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145807.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Roxana Massott, Gottschallalmstraße 37, 4792 Ficht, Österreich, vertreten durch Mag. Fatma Islekoglu, Rechtsanwältin,  Landstraße 13, 6971 Hard, über die Beschwerde vom 22. März 2024 gegen den Bescheid des  Finanzamtes Österreich vom 22. Februar 2024 betreffend Festsetzung der  Normverbrauchsabgabe (Berechnungsstichtag 02.06.2022), zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Mag. Fatma Islekoglu` — partial — gold is substring of pred: `Mag. Fatma Islekoglu`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Roxana Massott`(person)
- `Gottschallalmstraße 37, 4792 Ficht, Österreich`(address)
- `Mag. Fatma Islekoglu`(person)
- `Finanzamtes Österreich`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_239`)


Mit der Beschwerde wurde die Ersetzung der Umsatzsteuerbescheide 2011 bis 2015 durch  Bescheide, die den angeführten Beschwerdegründen Rechnung tragen, [und die Aufhebung  der übrigen angefochtenen Festsetzungsbescheide] beantragt.

**False Positives:**

- `durch  Bescheide` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/147137.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147137.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache RgR Shirley Ribler, Kraftwerk Ottensheim-Wilhering 18, 2722 Emmerberg, Österreich, vertreten durch Dr. Christian Lind,  Am Ausblick 17, 3110 Neidling, über die Beschwerde vom 2. Jänner 2023 gegen die Bescheide  des Finanzamtes Österreich vom 1. Dezember 2022 betreffend Anspruchszinsen (§ 205 BAO)  2016, 2017 und 2018, Steuernummer 64-511/1773, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Dr. Christian Lind` — partial — gold is substring of pred: `Dr. Christian Lind`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `RgR Shirley Ribler`(person)
- `Kraftwerk Ottensheim-Wilhering 18, 2722 Emmerberg, Österreich`(address)
- `Dr. Christian Lind`(person)
- `Finanzamtes Österreich`(organisation)
- `64-511/1773`(tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/148001.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Paulina Borisowa  in der Beschwerdesache Ilhan Feldmeier, Bakk. rer. nat.,  Sittenbergstraße 9, 4294 Stampfendorf, Österreich, vertreten durch Mag. Benno Elmar Di Gaspero, Unterer Platz 7, 9372  Eberstein, über die Beschwerde vom 14. Juni 2024 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juni 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023  Steuernummer 14-548/3314  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `vertreten durch Mag. Benno Elmar Di Gaspero` — partial — gold is substring of pred: `Mag. Benno Elmar Di Gaspero`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Paulina Borisowa`(person)
- `Ilhan Feldmeier, Bakk. rer. nat.`(person)
- `Sittenbergstraße 9, 4294 Stampfendorf, Österreich`(address)
- `Mag. Benno Elmar Di Gaspero`(person)
- `Finanzamtes  Österreich`(organisation)
- `14-548/3314`(tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/148962.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148962.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Univ.-Prof. Ramon Löther  in der Beschwerdesache Axel Pommeränke,  Zum Hauptplatz 2, 4030 Linz, Österreich, vertreten durch Mag. Niki Zaar, Babenbergerstraße 9/1/8, 1010 Wien,  betreffend die Vorlage der Bescheide des Finanzamtes Österreich vom 9. Oktober 2023 über  die Wiederaufnahme des Verfahrens betreffend Einkommensteuer 2018 und 2019 im Wege  des Vorlageberichtes vom 21. November 2024 zur Steuernummer 14-979/7189  den  Beschluss:  Das Verfahren wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `vertreten durch Mag. Niki Zaar` — partial — gold is substring of pred: `Mag. Niki Zaar`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Univ.-Prof. Ramon Löther`(person)
- `Axel Pommeränke`(person)
- `Zum Hauptplatz 2, 4030 Linz, Österreich`(address)
- `Mag. Niki Zaar`(person)
- `Finanzamtes Österreich`(organisation)
- `14-979/7189`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/149721.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149721.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Mag.a Gerda Hellvogt  in der Beschwerdesache Tatjana Wolnik,  Am Teich 13, 5113 Sankt Georgen bei Salzburg, Österreich, vertreten durch Mag. Ursula Zimmerl, Sternwartestraße 82, 1180 Wien, über  die Beschwerde vom 14. Juli 2025 gegen den Bescheid des Finanzamtes Österreich vom 10. Juli  2025 betreffend Zwangsstrafen 2025, Steuernummer 36-865/6597, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Mag. Ursula Zimmerl` — partial — gold is substring of pred: `Mag. Ursula Zimmerl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Mag.a Gerda Hellvogt`(person)
- `Tatjana Wolnik`(person)
- `Am Teich 13, 5113 Sankt Georgen bei Salzburg, Österreich`(address)
- `Mag. Ursula Zimmerl`(person)
- `Finanzamtes Österreich`(organisation)
- `36-865/6597`(tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/149812.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149812.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Detlev Bodenmüller  in der Beschwerdesache Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.,  Pux 4, 8753 Paßhammer, Österreich  vertreten durch Mag. Thomas Gell, Am Rosenhof 4, 8063 Eggersdorf bei Graz,  über die Beschwerde vom 28. April 2025 gegen den Bescheid des Finanzamtes Österreich vom  31. März 2025 betreffend Abgabenerhöhung nach § 29 Abs 6 FinStrG zu Steuernummer 72-997/9457  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `vertreten durch Mag. Thomas Gell` — partial — gold is substring of pred: `Mag. Thomas Gell`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Detlev Bodenmüller`(person)
- `Univ.-Prof.in Eva Gund, Bakk. techn. Bakk. rer. nat.`(person)
- `Pux 4, 8753 Paßhammer, Österreich`(address)
- `Mag. Thomas Gell`(person)
- `Finanzamtes Österreich`(organisation)
- `72-997/9457`(tax_number)

</details>

---

## `Specific_Name_Pascal_Tebbe` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `df7525be`  
**Description:**
Explicitly captures 'Pascal Tebbe' to ensure recall in contexts where titles are missing.

**Content:**
```
\bPascal\s+Tebbe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Lumplecker_Deych` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `553ebbfc`  
**Description:**
Explicitly captures 'Elina Lumplecker' and 'Florentine Deych' to ensure recall.

**Content:**
```
\b(?:Elina\s+Lumplecker|Florentine\s+Deych)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Gewert` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2d9751d0`  
**Description:**
Explicitly captures 'Zeno Gewert' to ensure recall.

**Content:**
```
\bZeno\s+Gewert\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Maerkl` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cf0314b2`  
**Description:**
Explicitly captures 'Saphira Maerkl' to ensure recall.

**Content:**
```
\bSaphira\s+Maerkl\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Joern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ae0cf5e4`  
**Description:**
Explicitly captures 'PhD Isaak Joern' to ensure recall.

**Content:**
```
\bPhD\s+Isaak\s+Joern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `RA_Mag_Start` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cc433b30`  
**Description:**
Captures 'RA Mag.' names at the start of a sentence or after punctuation, handling the specific 'RA Mag. Posawetz' pattern.

**Content:**
```
(?:^|\.)\s*(RA\s+Mag\.[\s\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00dfA-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Anonymized_Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `26d7b80a`  
**Description:**
Captures anonymized names like 'N.N.' or 'M.M.A.' which are common in legal texts.

**Content:**
```
\b(?:N\.N\.|M\.M\.A\.|X\.X\.)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Anonymized_Names_Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3a620612`  
**Description:**
Captures anonymized names like 'M.M.A.', 'N.N.', 'X.X.' when preceded by prepositions like 'von', 'und', 'des', 'der', 'dem', 'die' to ensure they are treated as persons.

**Content:**
```
(?:von|und|des|der|dem|die)\s+(?:M\.M\.A\.|N\.N\.|X\.X\.)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Complainant_Des_Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `878b77f4`  
**Description:**
Captures person names following 'des' or 'der' in the context of 'Beschwerdesache' when no title is present, ensuring the name is followed by an address or comma, including suffixes.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Verwaltungsstrafsache)\s+)(?:des\s+|der\s+)([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)(?=,|\s+\d)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Ing_Short_Title` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `637c2de7`  
**Description:**
Captures short-form engineering titles like 'Ing KB' or 'Ing FT' which are common in legal texts.

**Content:**
```
\bIng\s+[A-Z]{2,3}\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Complex_Title_Combo` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a98e7390`  
**Description:**
Captures names with multiple academic titles like 'Dipl.-Ing. DDr.in' or 'Dipl.-Ing. Univ.-Prof.' or 'Dr.in Ing.' ensuring full match.

**Content:**
```
\b(?:Dipl\.-)?Ing\.(?:\s+DDr\.(?:in)?\s+|Univ\.-Prof\.(?:in)?\s+|Hon\.-Prof\.(?:in)?\s+|Priv\.-Doz\.(?:in)?\s+|Dr\.(?:in)?\s+)?[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+MSc|\s+BSc|\s+PhD)?(?:,\s*(?:Bakk\.|MSc|BSc|MA|BA|LLM|LL\.M\.|PhD|Dr\.|Dipl\.|Ing\.|Univ\.-Prof\.|Mag\.|Prof\.|Hon\.-Prof\.|Priv\.-Doz\.|KommR\s+|VetR\s+|KzlR\s+|MedR\s+|RgR\s+|MRICS|SV|MG|Bf\.)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Felicitas_Niedermann` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `162cba3d`  
**Description:**
Explicitly captures 'Felicitas Niedermann' to ensure recall in contexts where titles are missing.

**Content:**
```
\bFelicitas\s+Niedermann\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Zeno_Schickhuber` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8b481eff`  
**Description:**
Explicitly captures 'Zeno Schickhuber' to ensure recall.

**Content:**
```
\bZeno\s+Schickhuber\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Claire_Hilt` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d4d0a4b4`  
**Description:**
Explicitly captures 'Claire Hilt' to ensure recall.

**Content:**
```
\bClaire\s+Hilt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Adam_Safak` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `28ff60f8`  
**Description:**
Explicitly captures 'Adam Safak' to ensure recall.

**Content:**
```
\bAdam\s+Safak\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Zlatan_Frauenknecht` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9bf0d900`  
**Description:**
Explicitly captures 'Zlatan Frauenknecht' to ensure recall.

**Content:**
```
\bZlatan\s+Frauenknecht\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Niederschrift_Name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f6c8aa43`  
**Description:**
Captures person names following 'Niederschrift' in contexts like 'Niederschrift [Name], Gattin'.

**Content:**
```
Niederschrift\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 4 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133681.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133681.1_305`)


Im Rahmen der Prüfung sei  ausdrücklich zum Ausdruck gebracht worden, dass der Bruder des Beschwerdeführers der  Verwalter des Gutes gewesen sei (siehe Niederschrift Außenprüfung).

**False Positives:**

- `Außenprüfung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/145807.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145807.1_57`)


Er selbst habe jedoch angegeben, das Kfz um  zwischen Österreich und der Türkei hin und her zu fahren zu verwenden (unter Hinweis auf die  „Niederschrift Zoll, S 5“).

**False Positives:**

- `Zoll` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_225`)


Weiters hat das Ermittlungsverfahren ergeben, dass für  die Begleichung der strittigen Maßnahmen auch nicht rückzahlbare Förderungen verwendet  wurden (siehe Niederschrift Erörterungstermin vom 23.9.2024).

**False Positives:**

- `Erörterungstermin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/146249.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146249.1_227`)


Schließlich negiert die  Beschwerdeführerin mit den Ausführungen zum Bestand des engeren Zusammenhangs auch,  dass zur Finanzierung der verfahrensgegenständlichen Aufwendungen in jenen Fällen  Fremdkapital (zB Bankdarlehen) herangezogen wurde, in denen die für das betreffende Objekt  zur Verfügung stehenden EVB-Mittel zur Abdeckung der anfallenden Kosten nicht ausreichten  (siehe Niederschrift Erörterungstermin vom 23.9.2024 unter Verweis auf das  Parallelverfahren).

**False Positives:**

- `Erörterungstermin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `OMedR_Title` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a288d169`  
**Description:**
Captures names with the specific legal title 'OMedR' (Obermedizinalrat) followed by a name, ensuring full match.

**Content:**
```
\bOMedR\s+Dr\.(?:in)?\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Gertrude_Haidary_Specific` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c8aeccb3`  
**Description:**
Explicitly captures 'Gertrude Haidary' to handle cases where titles are missing or context is ambiguous (e.g., followed by .com, Limited).

**Content:**
```
\bGertrude\s+Haidary\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Sachverständigengutachten_Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c01884e2`  
**Description:**
Captures the name of the expert following 'Sachverständigengutachten', ensuring only the name is captured and not the document title.

**Content:**
```
Sachverständigengutachten\s+([A-Z][a-zäöüÄÖÜß]+(?:\s+[A-Z][a-zäöüÄÖÜß]+)*(?:\s+-(?:[A-Z][a-zäöüÄÖÜß]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+MSc|\s+BSc|\s+PhD)?)(?=\s+Fachgebiet|,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Wendelin_Polmanns` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `54704a0b`  
**Description:**
Explicitly captures 'Wendelin Polmanns' to ensure recall in contexts where titles are missing.

**Content:**
```
\bWendelin\s+Polmanns\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Heiko_Dwortzak` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `aa01dc8d`  
**Description:**
Explicitly captures 'Heiko Dwortzak' to ensure recall.

**Content:**
```
\bHeiko\s+Dwortzak\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Marilyn_Sturtzebecher` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a6fcb79b`  
**Description:**
Explicitly captures 'Marilyn Sturtzebecher' to ensure recall.

**Content:**
```
\bMarilyn\s+Sturtzebecher\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Raphael_Venclik` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `127d77e2`  
**Description:**
Explicitly captures 'Raphael Venclik' to ensure recall.

**Content:**
```
\bRaphael\s+Venclik\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Muran_Waldhans` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0360b213`  
**Description:**
Explicitly captures 'Muran Waldhans' to ensure recall.

**Content:**
```
\bMuran\s+Waldhans\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Dimitri_Kozlowska` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f3b03de1`  
**Description:**
Explicitly captures 'Dimitri Kozlowska' to ensure recall.

**Content:**
```
\bDimitri\s+Kozlowska\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Antragsteller_Name` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3482f424`  
**Description:**
Captures person names in parentheses following 'Antragsteller' or similar roles, e.g., '(Olaf Vasiliadis)'.

**Content:**
```
(?:Antragsteller|Beschwerdeführer|Beschwerdeführerin|Beteiligte|Beteiligter|Beteiligte)\s*\(\s*([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*)\s*\)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 57 | 0 | 57 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 57 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/128684.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/128684.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) erklärte in seiner Einkommensteuererklärung für das Jahr 1999  neben weiteren Einkünften auch Einkünfte aus Gewerbebetrieb als Mitunternehmer aufgrund  von Beteiligungen (Kommanditist).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129331.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129331.1_4`)


Entscheidungsgründe  Beschwerdeführerin (Bf) ist Frau Basil Staerk.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Basil Staerk`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/129608.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129608.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) ist Musiklehrer und machte in seiner Arbeitnehmerveranlagung  unter anderem Kosten für ein im Wohnungsverband gelegenes Arbeitszimmer und einen Teil  des Wohnzimmers, in dem sich ein Flügel befindet, geltend.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/129600.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129600.1_18`)


Das Ersuchen ergeht im Rahmen eines Rechtsstreits wegen Gewährung der österreichischen  Familienbeihilfe und des Kinderabsetzbetrages zwischen der Beschwerdeführerin (Bf) und dem  Finanzamt 8/16/17 als zuständigem Träger wegen ihrer Zugehörigkeit zum österreichischen  Pflichtversicherungssystem für die Zeit ihres Beschäftigungsverhältnisses mit einer  österreichischen Entwicklungshilfeorganisation in der Zeit vom 6. September 2016 bis  15. September 2019, weil sie ihre Beschäftigung fast ausschließlich in einem Drittstaat ausübte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/129652.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129652.1_4`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Die Beschwerdeführerin (Bf) betreibt in Form einer KG eine Biogasanlage zur Stromerzeugung.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/129987.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129987.1_4`)


Entscheidungsgründe  Sachverhalt  Am 10.9.2018 ergingen an den Beschwerdeführer (Bf) nachstehende drei Bescheide:  1) Bescheid über die Festsetzung eines ersten Säumniszuschlages in Höhe von 175,36 €, weil  die Einkommensteuer 07-09/2018 nicht bis 16.8.2018 entrichtet wurde;

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Kirsten Renneissen – ist Malermeister und betreibt ein  Einzelunternehmen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kirsten Renneissen`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr Priv.-Doz. Dipl.-Ing. Theobald Brauckhof – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof`(person)
- `SeeAutomotive AG`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/130713.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130713.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Nachdem der Beschwerdeführer (Bf) der Aufforderung, eine Einkommensteuererklärung  abzugeben, nicht nachgekommen war, schätzte die belangte Behörde die  Bemessungsgrundlagen, wobei sie die vorliegenden Lohnzettel zugrunde legte und neben  Pauschbeträgen für Werbungskosten und Sonderausgaben einen Freibetrag gemäß § 35 Abs 3  EStG berücksichtigte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/131159.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131159.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) beantragte in seiner Erklärung zur ArbeitnehmerInnenveranlagung  2018 unter dem Titel „Wohnraumschaffung und –sanierung“ (Kz 456) Sonderausgaben in Höhe  von 4.905,72 Euro.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/131432.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131432.1_2`)


Begründung  Mit 9.4.2018 hat die Beschwerdeführerin (Bf) Säumnisbeschwerde erhoben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/131654.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131654.1_5`)


Dieser Frage ging nachstehendes Verwaltungsgeschehen voran:  Die Beschwerdeführerin (Bf) reichte die Erklärung zur Durchführung der  Arbeitnehmerveranlagung ein und beantragte darin die Berücksichtigung des  Alleinverdienerabsetzbetrages.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/131904.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131904.1_3`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Über die Berufung der Beschwerdeführerin (Bf) betreffend Energieabgabenvergütung 2011  entschied der Unabhängige Finanzsenat, dass der Bf als Dienstleistungsunternehmen die  Energieabgabenvergütung letztmalig für Jänner 2011 zusteht (UFS 31.8.2012, RV/2441-W/12).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/132287.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132287.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf), ein deutscher Unternehmer, brachte rechtzeitig einen  elektronischen Antrag auf Vorsteuererstattung für 1-3/2020 ein idHv.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/133832.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133832.1_6`)


Entscheidungsgründe  I. Verfahrensgang  1 Außenprüfung  Im Zuge einer den beschwerdegegenständlichen Zeitraum umfassenden abgabenbehördlichen  Außenprüfung bei der Beschwerdeführerin (Bf) wurden im Wesentlichen folgende  Feststellungen getroffen:   Die Beschwerdeführerin (kurz Bf) ist eine GmbH, deren alleinige Gesellschafterin Frau Schneppensiefen ist.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Schneppensiefen`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/134256.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134256.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Der NÖ Landesverein für Sachwalterschaft und Bewohnervertretung beantragte namens der  1960 geborenen Beschwerdeführerin (Bf) mit den amtlichen Formularen Beih1 und Beih3 vom  29.11.2017 rückwirkend die Familienbeihilfe und die erhöhte Familienbeihilfe infolge Verlustes  der Selbsterhaltungsfähigkeit vor dem 21. bzw 25.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_5`)


Entscheidungsgründe  Strittig sind im anhängigen Verfahren die umsatzsteuerlichen Konsequenzen aus der  Beendigung der unternehmerischen Tätigkeit der Beschwerdeführerin (Bf) in Österreich.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/136377.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136377.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  Der Beschwerdeführer (Bf), der hör- und gehbehindert ist (Grad der Behinderung: 70%),  machte in seiner am 9.2.2018 auf elektronischem Weg eingebrachten Erklärung zur  Durchführung der Arbeitnehmerveranlagung 2014 Aufwendungen in Höhe von 2.083,42 Euro  als außergewöhnliche Belastung ohne Selbstbehalt geltend.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  Mit Erinnerungsschreiben vom 30.12.2021 forderte das Finanzamt die Beschwerdeführerin  (Bf), bei der es sich um eine in Österreich ansässige GmbH handelt, dazu auf, die „Erstmeldung  oder Meldung nach Fälligkeit der jährlichen Überprüfung der wirtschaftlichen Eigentümer  entsprechend den Bestimmungen des § 5 Wirtschaftliche Eigentümer Registergesetz (WiEReG)"  bis spätestens 21.2.2022 nachzuholen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/137330.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137330.1_4`)


Entscheidungsgründe  Verfahrensgang  Der Beschwerdeführer (Bf) ist ungarischer Staatsbürger und lebt mit seiner Partnerin in  Lebensgemeinschaft.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/137351.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137351.1_5`)


Dieser Frage ging folgendes Verwaltungsgeschehen voraus:  Die Beschwerdeführerin (Bf) beantragte die Durchführung der Arbeitnehmerveranlagung.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/137502.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137502.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf) beantragt unter Berufung auf von ihr nicht näher bezeichnete  unionsrechtliche Vorschriften, den Familienbonus plus für ihre beiden Kinder, den sie jeweils  zur Hälfte beansprucht hat, in voller diesbezüglicher Höhe und nicht indexangepasst zu  berücksichtigen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137519.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137519.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Beschwerdeführerin (Bf) ist eine Gesellschaft mit beschränkter Haftung, die im Jahr 2017  errichtet und ins Firmenbuch eingetragen wurde.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/137519.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137519.1_37`)


Folgender Sachverhalt wird der Entscheidung zu Grunde gelegt:  Beschwerdeführerin (Bf) ist eine Gesellschaft mit beschränkter Haftung, die mit Erklärung vom  29.03.2017 errichtet und am 15.04.2017 neu in das Firmenbuch eingetragen wurde.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf) stellte am 30. November 2020, eingelangt beim Finanzamt am  17. Dezember 2020, für ihren Sohn S., geb. xx.xx.2004, einen Antrag auf Gewährung des  Erhöhungsbetrages zur Familienbeihilfe wegen Asperger Syndrom.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/138183.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138183.1_3`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Die Beschwerdeführerin (Bf) bezog für Ihre Tochter S. laufend Familienbeihilfe (FB).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf) stellte am 6. März 2020 für ihre Tochter M., geb. 1992, einen  Antrag auf Gewährung der Familienbeihilfe und des Erhöhungsbetrages wegen erheblicher  Behinderung (Asperger Syndrom, Spezifische Phobie) und legte folgenden psychologischen  Kurzbefund der X Privatklinik, psychologische Universitätsambulanz, bei:  „… Untersuchungsdatum: 06.11.2019;

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `M.`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/139279.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139279.1_4`)


Begründung  Ablauf des Verfahrens:  BP-Bericht des Finanzamtes (FA) vom 6.5.2021  TZ 1:  Die Beschwerdeführerin (Bf) vermietete der Fertighaushaus Gesellschaft m b H (Mieterin)   (Fertighaus GmbH) „Fertighaus“ Musterhäuser.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/139596.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139596.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit Schreiben vom 28.02.2022 wurde die Beschwerdeführerin (Bf) aufgefordert eine Erklärung  zur Arbeitnehmerveranlagung abzugeben, da ihr Arbeitgeber den Familienbonus Plus  steuermindernd berücksichtigt hatte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_49`)


Beschwerdesache ist der Anspruch der Beschwerdeführerin (Bf) Olivia Trienes  auf den  Erhöhungsbetrag zur Familienbeihilfe für den Sohn A, geb.   .6.1997, wg. erheblicher  Behinderung, konkret wg. "Diabetes Mellitus Typ I", iSd § 8 Abs. 5 f. FLAG 1967 idgF "ab März  2022" strittig.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Olivia Trienes`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/140867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140867.1_5`)


Entscheidungsgründe  1. Sachverhalt   Mit „Sammelbescheid“ des Zollamtes Graz vom 5. November 2015, Zl. 700000/09864/19/2013,  wurden für die Beschwerdeführerin (Bf) Altlastenbeiträge und Nebenabgaben in Höhe von  € 1.284.553,92 für die Jahre 2010 bis 2013 festgesetzt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamtes Graz`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/141318.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141318.1_15`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Beschwerdeführerin (Bf) ist eine GmbH, deren Alleingesellschafterin wiederum eine GmbH  ist.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/141414.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141414.1_4`)


Nach einer Verurteilung durch das Landesgericht Salzburg als Strafgericht am Datum zu Zahl  wurde der Beschwerdeführer (Bf) mit Bescheid vom 06.11.2019 gem. § 11  Bundesabgabenordnung (BAO) zur Haftung betreffend die hinterzogenen Abgaben der GmbH  herangezogen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgericht Salzburg`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/141648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141648.1_43`)


Beschwerdesache ist der Anspruch der Beschwerdeführerin (Bf) A auf Familienbeihilfe  sowie den Erhöhungsbetrag zur Familienbeihilfe für den Sohn B, geb. … .7.1998, wg. erheblicher  Behinderung, konkret wg. angeborener "Blindheit zu 100 %", iSd § 2 Abs. 1 lit c und h iVm § 8  Abs. 5 f. FLAG 1967 "ab August 2021" (= nach beendetem Schulbesuch) strittig.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/142233.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142233.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf) bezog für das Kind K., geb. 2020, für den Zeitraum Februar 2022  bis Mai 2022 Familienbeihilfe, da es sich von 17. Jänner 2022 bis 5. Mai 2022 in ihrer Pflege  befand.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/142384.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142384.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) war im Streitjahr mit Hauptwohnsitz in Österreich gemeldet und  beantragte im Rahmen der elektronisch eingelangten Einkommensteuererklärung für das Jahr  2019 die Berücksichtigung des Alleinverdienerabsetzbetrages, den ganzen Familienbonus Plus  für zwei Kinder und bestätigte, die Familienbeihilfe zu beziehen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/142396.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142396.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf) ist eine KG, deren Komplementärin einen Kapitalmarktprospekt  zur Finanzierung von Startups aufgelegt hat.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/142648.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142648.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) beantragte für die Jahre 2020 und 2021 jeweils den ganzen  Familienbonus Plus für seine drei leiblichen Kinder sowie für seine Stieftochter.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/142867.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/142867.1_5`)


Dieser Frage liegt folgendes Verwaltungsgeschehen zu Grunde:  Die Beschwerdeführerin (Bf) hat die beschwerdegegenständlichen Kalenderjahre (2000-2003)  betreffend den DB entrichtet.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/143044.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143044.1_8`)


Entscheidungsgründe  Mit Einkommensteuererklärung (ESt-Erklärung) 2016 vom 19.2.2018 begehrte die  Beschwerdeführerin (Bf) insbesondere den Alleinerzieherabsetzbetrag.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/143074.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143074.1_3`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Mit Haftungsbescheid vom 19.10.2021 wurde der Beschwerdeführer (Bf) infolge des Urteils  des Landesgerichtes Salzburg vom Datum,Zahl zur Haftung gem. § 11 Bundesabgabenordnung  (BAO) betreffend die Abgabenschulden der GmbH (in Folge kurz: GmbH) herangezogen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichtes`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/143315.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143315.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin (Bf) bezog für ihre Tochter T., geb. 2003, Familienbeihilfe samt  Kinderabsetzbeträge.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/143736.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143736.1_4`)


Dagegen erhob der Beschwerdeführer (Bf) mit Eingabe vom 5.2.2023 wiederum elektronisch  Beschwerde mit der Begründung, dass lt Abgabenänderungsgesetz 2022 Rz 631c ff die von der  AHV FL gewährte IV-Rente 2020 dem Jahr 2020 zuzurechnen sei und nicht 2021.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/144086.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144086.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) reichte am 28.7.2019 seine Einkommensteuererklärung  (Arbeitnehmerveranlagung) 2018 elektronisch beim Finanzamt ein.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/144427.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144427.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Im Zuge der Überprüfung der Anspruchsvoraussetzungen für die weitere Gewährung der  Familienbeihilfe für Sohn N, wurde die Beschwerdeführerin (Bf) aufgefordert, bis spätestens  27.06.2023 die Schulbesuchsbestätigung für den Sohn vorzulegen sowie dessen  Schulausbildungsdauer bekannt zu geben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/144516.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144516.1_4`)


Entscheidungsgründe  1. Sachverhalt   Mit Bescheid des Finanzamtes Wien 4/5/10 vom 28. Mai 2015, Abgabenkontonummer:  31-324/9083, erfolgte für den Beschwerdeführer (Bf) die Festsetzung einer  Kapitalertragsteuer in Höhe von € 282.641,70 für den Zeitraum 2011 bis Juni 2013.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes Wien 4/5/10`(organisation)
- `31-324/9083`(tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/145411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145411.1_3`)


Begründung  Sachverhalt:  Am 17.2.2021 stellte der Beschwerdeführer (Bf) einen Antrag auf Arbeitnehmerveranlagung  für das Jahr 2020.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/145350.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145350.1_3`)


Begründung  Der Beschwerdeführer (Bf) begehrte in den ANV-Erklärungen 2018 (Pflichtveranlagung) bzw.  2019 (Antragsveranlagung) einerseits der Abzug diverser Werbungskosten im Zusammenhang  mit seinen nichtselbständigen Einkünften (Pendlerpauschale/ Pendlereuro, AfA für  Arbeitsmittel, Telefonkosten, Aufwand für Dienstreisen) und anderseits die Berücksichtigung  von Krankheitskosten als außergewöhnliche Belastung (§ 34 EStG 1988).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/146422.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146422.1_5`)


Entscheidungsgründe  Strittig ist im anhängigen Verfahren die Berücksichtigung des Familienbonus Plus (nachfolgend  Fabo+) für die im Februar 2007 geborene Tochter der Beschwerdeführerin (Bf) aus  geschiedener Ehe bei der Arbeitnehmerveranlagung (ANV) 2022.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/146433.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146433.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf) hat für ihre Enkelin W.B. aufgrund eines gemeinsamen Haushaltes  seit Februar 2016 durchgehend bis März 2024 die Familienbeihilfe (FB, sowie  Kinderabsetzbetrag, KG) bezogen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_VALIDATE/146532.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146532.1_3`)


Begründung  1. Festgestellter Sachverhalt:  Mit Bescheid des Finanzamtes vom 9.8.2022 wurde der Beschwerdeführer (Bf) zur  Einkommensteuer für das Jahr 2021 veranlagt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_VALIDATE/147055.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147055.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  Bei der Beschwerdeführerin (Bf) handelt es sich um eine Gesellschaft mit beschränkter  Haftung, die im Bereich der Stromerzeugung aus erneuerbaren Energien tätig ist.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_BFG_20260814_VALIDATE/147193.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147193.1_5`)


Sachverhalt  Gegen den Einkommensteuerbescheid 2022 vom 28.4.2023 hat der Beschwerdeführer (Bf) am  4.5.2023 über FinanzOnline Beschwerde erhoben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_BFG_20260814_VALIDATE/147967.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147967.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit Eingabe vom 25. Juni 2022 reichte die Beschwerdeführerin (Vermietungsgemeinschaft) die  Erklärung betreffend Feststellung der Einkünfte für das Jahr 2021 auf elektronischem Weg  beim zuständigen Finanzamt ein.

**False Positives:**

- `Vermietungsgemeinschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_VALIDATE/149156.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149156.1_4`)


Entscheidungsgründe  Die Beschwerdeführerin (Bf) hat die Kommunalsteuer 2020 (laufend und vollumfänglich)  entrichtet.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_BFG_20260814_VALIDATE/149253.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149253.1_2`)


Begründung  1. Festgestellter Sachverhalt:  Mit Bescheid vom 20.6.2024 wies das Finanzamt den Antrag der Beschwerdeführerin (Bf) vom  28.12.2023 auf Erlassung eines Gutschriftsbescheides gemäß § 202 BAO betreffend Lohnsteuer  ab.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_VALIDATE/149482.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149482.1_29`)


Es wurde in  zwei Gutachten keine dauernde Erwerbsunfähigkeit festgestellt.   Sachverhalt: Die Beschwerdeführerin (Bf) stellte am 31.10.2024 einen Antrag auf erhöhte  Familienbeihilfe für den Sohn, der in ihrem Haushalt lebt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `MMag_Title` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `35a506fb`  
**Description:**
Captures names with the specific title 'MMag.Dr.' which was missing in previous patterns.

**Content:**
```
\bMMag\.Dr\.\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Marilyn_Frankenberger` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `52cb102a`  
**Description:**
Explicitly captures 'Mag.a Marilyn Frankenberger' to ensure recall in contexts where titles are present.

**Content:**
```
\bMag\.a\s+Marilyn\s+Frankenberger\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Zacharias_Herzbruch` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `d641f59f`  
**Description:**
Explicitly captures 'Zacharias Herzbruch' to ensure recall.

**Content:**
```
\bZacharias\s+Herzbruch\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Esra_Lindacher` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8ee810a7`  
**Description:**
Explicitly captures 'Esra Lindacher' to ensure recall.

**Content:**
```
\bEsra\s+Lindacher\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Mehmet_Bonberg` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b495d844`  
**Description:**
Explicitly captures 'Mehmet Bonberg' to ensure recall.

**Content:**
```
\bMehmet\s+Bonberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Felix_Asenkerschbaumer` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `87d91551`  
**Description:**
Explicitly captures 'Felix Asenkerschbaumer' to ensure recall in contexts where titles are missing.

**Content:**
```
\bFelix\s+Asenkerschbaumer\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Viola_Hinterwaelder` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1735b4f4`  
**Description:**
Explicitly captures 'Viola Hinterwaelder' to ensure recall in contexts where titles are missing or context is ambiguous.

**Content:**
```
\bViola\s+Hinterwaelder\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Rupert_Bernhardz` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `02bd78d8`  
**Description:**
Explicitly captures 'Rupert Bernhardz, Bakk. phil.B.' to ensure recall.

**Content:**
```
\bRupert\s+Bernhardz,\s+Bakk\.\s+phil\.B\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Evelyn_StrasserR` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `89aeb04a`  
**Description:**
Explicitly captures 'Evelyn SträsserR.' to ensure recall.

**Content:**
```
\bEvelyn\s+Str\u00e4sserR\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Chomenko` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4d2d05db`  
**Description:**
Explicitly captures 'ChomenkoH.' and 'Chomenko' to ensure recall.

**Content:**
```
\bChomenkoH\.|\bChomenko\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_R_H` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `eff3ee32`  
**Description:**
Explicitly captures 'R. H.' to ensure recall.

**Content:**
```
\bR\.\s+H\.
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Specific_Name_Dr_in_Nicoletta_Huberle` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f4241d6f`  
**Description:**
Explicitly captures 'Dr.in Nicoletta Huberle' to ensure recall.

**Content:**
```
\bDr\.in\s+Nicoletta\s+Huberle\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Beschwerdesache_Full_Name` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `91c55e2b`  
**Description:**
Captures person names following 'in der Beschwerdesache' including suffixes like Bakk. phil., LL.M., MA, etc.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Verwaltungsstrafsache)\s+)(?:des\s+|der\s+)?(?:Hon\.-Prof\.(?:in)?\s+|Dr\.(?:in\s+Dipl\.(?:Kff\.)?\s+|in)?\s+|Priv\.-Doz\.(?:in)?\s+|Mag\.(?:Dr\.)?\s+|Univ\.-Prof\.(?:in)?\s+|Bakk\.(?:\s+rer\.\s+nat\.|\s+rer\.\s+art\.|\s+rer\.\s+techn\.|\s+rer\.\s+jur\.|\s+phil\.|\s+iur\.|\s+techn\.)?\s+|Ing\.(?:\s+Dipl\.)?\s+|Mag\.a\s+|Prof\.in\s+|Prof\.(?:in)?\s+|RA\s+Mag\.(?:in)?\s+|DDr\.(?:in)?\s+|MedR\.(?:in)?\s+|RgR\.(?:in)?\s+|KzlR\.(?:in)?\s+|VetR\.(?:in)?\s+|KommR\.(?:in)?\s+|\u00d6kR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+LL\.M\.|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)(?=,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 13 | 0 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 13 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/129066.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Ing. Sascha Hilcker, Zum Sportzentrum 15, 3721 Limberg, Österreich, über die Beschwerde vom 30. August 2019 gegen den Bescheid des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf vom 21. August 2019 betreffend Abweisung des  (Eigen)Antrages vom 6. April 2019 auf Gewährung der Familienbeihilfe ab September 2018 zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Sascha Hilcker` — partial — pred is substring of gold: `Ing. Sascha Hilcker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing. Sascha Hilcker`(person)
- `Zum Sportzentrum 15, 3721 Limberg, Österreich`(address)
- `Finanzamtes Wien  3/6/7/11/15`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/129165.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129165.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Dr.in Laurin Morgenschweis, Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich Bf2-Adr***, und Fatima Beringschmidt, Kleinkamp 13 Tür  1, 3911 Rappottenstein, über die Beschwerde vom 21. Juli 2016 gegen den Bescheid des  Finanzamtes Waldviertel vom 31. Mai 2016 betreffend Einheitswert des land- u.  forstwirtschaftl.

**False Positives:**

- `Laurin Morgenschweis` — partial — pred is substring of gold: `Dr.in Laurin Morgenschweis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Dr.in Laurin Morgenschweis`(person)
- `Albert-Nöckl-Platz 225O, 3042 Pöding, Österreich`(address)
- `Fatima Beringschmidt`(person)
- `Finanzamtes Waldviertel`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/132275.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132275.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Dominik Mehlig  in der Beschwerdesache Ing. Edith Schifferdecker,  Pirusgasse 30, 4984 Hinterweintal, Österreich, betreffend die Beschwerden vom 23. September 2019 gegen die Bescheide  des Finanzamtes Innsbruck vom 26. Juli 2019 betreffend Festsetzung des Zuschlages zum  Dienstgeberbeitrag für die Jahre 2013 bis 2017  beschlossen:  I.  Die Beschwerden werden gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Edith Schifferdecker` — partial — pred is substring of gold: `Ing. Edith Schifferdecker`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Dominik Mehlig`(person)
- `Ing. Edith Schifferdecker`(person)
- `Pirusgasse 30, 4984 Hinterweintal, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/134067.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134067.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Martin Kuprian in der Beschwerdesache  Ing. Werner Böltl, Rydlweg 234, 3860 Dietweis, Österreich, über die Beschwerde vom  17. September 2019 gegen den Bescheid des Finanzamtes Innsbruck (nunmehr: Finanzamt  Österreich) vom 5. September 2019 betreffend Abweisung eines Antrages auf den  Erhöhungsbetrag zur Familienbeihilfe wegen erheblicher Behinderung vom 6. Mai 2019  zu Recht erkannt:  I.   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Werner Böltl` — partial — pred is substring of gold: `Ing. Werner Böltl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Martin Kuprian`(person)
- `Ing. Werner Böltl`(person)
- `Rydlweg 234, 3860 Dietweis, Österreich`(address)
- `Finanzamtes Innsbruck`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/136693.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136693.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Günter Jedamczik  in der Beschwerdesache ÖkR Tobias Schönyan,  Kreuzerleitenweg 34, 5273 Hofing, Österreich, vertreten durch Herrn Mag. Gernot Thonhauser, Steuerberater,  Wernersdorf 111, 8551 Wies, über die Beschwerde vom 15.3.2022 gegen den Bescheid des  Finanzamtes Österreich vom 22.2.2022 betreffend Festsetzung einer Zwangsstrafe gemäß § 16  WiEReG iVm § 111 BAO zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Tobias Schönyan` — partial — pred is substring of gold: `ÖkR Tobias Schönyan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Günter Jedamczik`(person)
- `ÖkR Tobias Schönyan`(person)
- `Kreuzerleitenweg 34, 5273 Hofing, Österreich`(address)
- `Mag. Gernot Thonhauser`(person)
- `Finanzamtes Österreich`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/137861.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache ÖkR Istvan  Thiebaud, Ziakpark 78, 3213 Hollenstein, Österreich, vertreten durch ECOVIS Scholler & Partner, Wirtschaftstreuhand GmbH,  Schmalzhofgase 4, Tür 12, 1060 Wien, über die Beschwerden vom 28. Juli 2017 gegen den  Bescheid des Finanzamtes Wien 4/5/10, nunmehr Finanzamt Österreich, vom 29. Juni 2017  betreffend Einkommensteuer 2015, Steuernummer 04-368/0800, sowie vom 23. Jänner 2020  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf, nunmehr Finanzamt  Österreich, vom 25. November 2019 betreffend Einkommensteuer der Jahre 2016 und 2017  sowie Anspruchszinsen 2016 und 2017, Steuernummer ****, nach der am 12. Mai 2022 in  Hintere Zollamtsstraße 2b, 1030 Wien, durchgeführten mündlichen Verhandlung im Beisein  der Schriftführerin S   1.) zu Recht erkannt:   Die Beschwerden gegen die Einkommensteuerbescheide der Jahre 2015 und 2016 sowie gegen  den Anspruchszinsenbescheid des Jahres 2016 wird gemäß § 279 BAO als unbegründet  abgewiesen  2.) beschlossen:  Die Beschwerden gegen den Einkommensteuerbescheid des Jahres 2017 sowie gegen den  Anspruchszinsenbescheid des Jahres 2017 wird gemäß § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Istvan  Thiebaud` — partial — pred is substring of gold: `ÖkR Istvan  Thiebaud`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `ÖkR Istvan  Thiebaud`(person)
- `Ziakpark 78, 3213 Hollenstein, Österreich`(address)
- `ECOVIS Scholler & Partner, Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Wien 4/5/10`(organisation)
- `Finanzamt Österreich`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/140831.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140831.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Stella Hornscheidt  in der Beschwerdesache Ing. Jaden Stoelzl,  Singham 49, 4274 Straß, Österreich, über die Beschwerden vom 1. Juni 2021 gegen die Bescheide des Finanzamtes  Österreich vom 31. Mai 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016,  2017 und 2018 Steuernummer 25-717/7817  zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Jaden Stoelzl` — partial — pred is substring of gold: `Ing. Jaden Stoelzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Stella Hornscheidt`(person)
- `Ing. Jaden Stoelzl`(person)
- `Singham 49, 4274 Straß, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `25-717/7817`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/144141.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Albert Salzmann in der Beschwerdesache  Ing. Marion Kloefkorn, Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich, vertreten durch Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG, Innsbrucker Bundesstraße 83A, 5020 Salzburg, über die Beschwerde vom  25.3.2022 gegen den Bescheid des Finanzamtes Österreich vom 3.3.2022 betreffend  Einkommensteuer 2018 zur Steuernummer 40-620/0106  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Marion Kloefkorn` — partial — pred is substring of gold: `Ing. Marion Kloefkorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Albert Salzmann`(person)
- `Ing. Marion Kloefkorn`(person)
- `Ing. Carl Paulitschky-Gasse 13, 3851 Brunn, Österreich`(address)
- `Hoffmann Reitsammer & Partner Steuerberatung  GmbH & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `40-620/0106`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/144397.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144397.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Mag. Dario Hukauf, Ober-Eisendorf 54, 3610 Weißenkirchen in der Wachau, Österreich, vertreten durch ALTHUBER SPORNBERGER &  PARTNER Rechtsanwälte GmbH, Doblhoffgasse 9 Tür Top 14, 1010 Wien, über die Beschwerde  vom 3. Jänner 2020 gegen die Bescheide des Finanzamtes Bruck Eisenstadt Oberwart  (nunmehr Finanzamtes für Großbetriebe ) vom 28. November 2019 betreffend Rückforderung  gem. § 241a BAO von Kapitalertragsteuer 2010 bis 2012 (Evidenznummern ***, ***, ***, ***,  ***, ***, ***, ***), Steuernummer 45-917/5183, zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dario Hukauf` — partial — pred is substring of gold: `Mag. Dario Hukauf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Mag. Dario Hukauf`(person)
- `Ober-Eisendorf 54, 3610 Weißenkirchen in der Wachau, Österreich`(address)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `45-917/5183`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/145051.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145051.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Aloisia Bergauer in der Beschwerdesache  Ing. Christian Marckwordt, Kaplan-Bonetti-Weg 15, 4502 Tiestling, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom  8. Februar 2024 gegen den Bescheid des Finanzamtes Österreich vom 18. Jänner 2024  betreffend Festsetzung Energiekrisenbeitrag Strom für den Zeitraum 1.12.2022-30.06.2023,  Steuernummer 22-821/5972, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Christian Marckwordt` — partial — pred is substring of gold: `Ing. Christian Marckwordt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Aloisia Bergauer`(person)
- `Ing. Christian Marckwordt`(person)
- `Kaplan-Bonetti-Weg 15, 4502 Tiestling, Österreich`(address)
- `Zacherl Schallaböck Proksch Manak Kraft  Rechtsanwälte GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `22-821/5972`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/146116.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146116.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Thomas Bäckert  in der Beschwerdesache Dr. Quentin Tessier,  Krottenhofweg 115, 4364 Großmaseldorf, Österreich, betreffend Beschwerde vom 18. Juni 2023 gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 15. Mai 2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022  Steuernummer 71-981/5443  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Quentin Tessier` — partial — pred is substring of gold: `Dr. Quentin Tessier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Thomas Bäckert`(person)
- `Dr. Quentin Tessier`(person)
- `Krottenhofweg 115, 4364 Großmaseldorf, Österreich`(address)
- `FA St. Johann Tamsweg Zell am See`(organisation)
- `71-981/5443`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/147555.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/147555.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag.Dr. Katrin Allram in der  Beschwerdesache Ing. Dagobert Almasri, Übersbachgasse 50, 2100 Langenzersdorf, Österreich, vertreten durch Sera Trust GmbH,  Gablenzgasse 11/4.

**False Positives:**

- `Dagobert Almasri` — partial — pred is substring of gold: `Ing. Dagobert Almasri`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Katrin Allram`(person)
- `Ing. Dagobert Almasri`(person)
- `Übersbachgasse 50, 2100 Langenzersdorf, Österreich`(address)
- `Sera Trust GmbH`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/149640.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149640.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Univ.-Prof. Jonas Nußer  in der Beschwerdesache Dr.in Flora Lallemand,  Rochusplatz 224, 9530 Bad Bleiberg, Österreich, über die Beschwerde vom 5. November 2024 gegen die Bescheide des  FA Graz-Stadt  vom 27. August 2024 über den Ablauf einer Aussetzung der Einhebung, über die  Festsetzung von Aussetzungszinsen und vom 1. Oktober 2024 über die Abweisung eines  Aussetzungsantrags, Steuernummer 29-953/8923, zu Recht erkannt:    I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

**False Positives:**

- `Flora Lallemand` — partial — pred is substring of gold: `Dr.in Flora Lallemand`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Univ.-Prof. Jonas Nußer`(person)
- `Dr.in Flora Lallemand`(person)
- `Rochusplatz 224, 9530 Bad Bleiberg, Österreich`(address)
- `FA Graz-Stadt`(organisation)
- `29-953/8923`(tax_number)

</details>

---

## `KR_Title` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ad7e1c6a`  
**Description:**
Captures names with the title 'KR' (Kammerrat) which was missing.

**Content:**
```
\bKR\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Gutachten_Dr_Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a7ab0365`  
**Description:**
Captures 'Dr. [Name]' following 'Gutachten von' or 'Sachverständigen' to ensure the doctor is identified as a person.

**Content:**
```
(?:Gutachten\s+von|Sachverst\u00e4ndigen)\s+(?:Dr\.(?:in)?\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*)(?=,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Richter_Name_Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b643b98b`  
**Description:**
Captures person names following 'durch den Richter' or 'durch die Richterin', ensuring full name capture including titles like Maga., CD@, and suffixes.

**Content:**
```
(?:durch\s+den\s+Richter|durch\s+die\s+Richterin)\s+(?:CD@Techn\s+R\s+Techn\s+R\s+|Maga\.(?:in)?\s+)?(?:Hon\.-Prof\.(?:in)?\s+|Dr\.(?:in)?\s+|Priv\.-Doz\.(?:in)?\s+|Mag\.(?:Dr\.)?\s+|Univ\.-Prof\.(?:in)?\s+|Bakk\.(?:\s+rer\.\s+nat\.|\s+rer\.\s+art\.|\s+rer\.\s+techn\.|\s+rer\.\s+jur\.)?\s+|Ing\.(?:\s+Dipl\.)?\s+|Mag\.a\s+|Prof\.in\s+|Prof\.(?:in)?\s+|RA\s+Mag\.(?:in)?\s+|DDr\.(?:in)?\s+|MedR\.(?:in)?\s+|RgR\.(?:in)?\s+|KzlR\.(?:in)?\s+|VetR\.(?:in)?\s+|KommR\.(?:in)?\s+|\u00d6kR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+LL\.M\.|\s+LLM|\s+MA|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)(?=,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/130336.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130336.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Wolfgang Tiwald, in der Beschwerdesache  Kirsten Renneissen, Egererweg 9, 5760 Niederhaus, Österreich, vertreten durch Stb, über die Beschwerde vom 25.07.2014 gegen  die Bescheide des Finanzamtes X vom 26.06.2014,   über die Festsetzung des Dienstgeberbeitrages (DB) für die Jahre 2010 bis 2012,    über die Festsetzung des Zuschlages zum Dienstgeberbeitrag (DZ) für die Jahre 2010 bis  2012 und    betreffend Haftung für Lohnsteuer gemäß § 82 EStG 1988 für die Jahre 2010 bis 2012,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `durch den Richter Mag. Wolfgang Tiwald` — partial — gold is substring of pred: `Mag. Wolfgang Tiwald`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Wolfgang Tiwald`(person)
- `Kirsten Renneissen`(person)
- `Egererweg 9, 5760 Niederhaus, Österreich`(address)
- `Finanzamtes`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/133359.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133359.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl, in der Beschwerdesache  Tristan Potente, Hürth 5, 4362 Schönfichten, Österreich, vertreten durch E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH, Bergmannstraße 7, 6850 Dornbirn, betreffend den Vorlageantrag vom  31. Oktober 2017 gegen die Beschwerdevorentscheidung des Finanzamtes Bregenz 12.  September 2017 betreffend Einkommensteuer 2009 Steuernummer 61-467/9522  beschlossen:  Der Vorlageantrag wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

**False Positives:**

- `durch den Richter Mag. Armin Treichl` — partial — gold is substring of pred: `Mag. Armin Treichl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Armin Treichl`(person)
- `Tristan Potente`(person)
- `Hürth 5, 4362 Schönfichten, Österreich`(address)
- `E. Igerz & Co Wirtschaftsprüfungs- und  Steuerberatungs GmbH`(organisation)
- `Finanzamtes`(organisation)
- `61-467/9522`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dieter Brennscheid, Bakk. rer. nat. in der Beschwerdesache Ines Gora,  Thunhausweg 19, 8311 Wetzawinkel, Österreich, über die Beschwerde vom 30. September 2016 gegen die Bescheide des  Finanzamtes Österreich vom 12. Juli 2016 betreff a) Umsatzsteuer für die Jahre 2011 bis 2015,  b) Festsetzung von ersten Säumniszuschlägen vom 09.08.2016,  c) Festsetzung von  Stundungszinsen vom 09.09.2016, Steuernummer 68-68-ZZZZZ (ehemals  18-383/0472 )  nach Durchführung einer mündlichen Verhandlung am 26.11.2024 zu Recht erkannt:      I. Der Beschwerde gegen die Umsatzsteuerbescheide für die Jahre 2011 bis 2015 wird gemäß        § 279 BAO Folge gegeben.

**False Positives:**

- `durch den Richter Dieter Brennscheid` — positional overlap with gold: `Dieter Brennscheid, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dieter Brennscheid, Bakk. rer. nat.`(person)
- `Ines Gora`(person)
- `Thunhausweg 19, 8311 Wetzawinkel, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `18-383/0472`(tax_number)

</details>

---

## `Frau_Name_Specific` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `058f2097`  
**Description:**
Captures person names following 'Frau' or 'Fr.', ensuring a name follows and excluding the title itself.

**Content:**
```
(?:Fr\.|Frau)\s+([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/137501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137501.1_14`)


Vergl. hierzu “Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_14`)


Vergl. hierzu “österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

</details>

---

## `VetR_Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `95a0f03f`  
**Description:**
Captures names with 'VetR' title followed by name and suffixes.

**Content:**
```
\bVetR\.(?:in)?\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+LL\.M\.|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `KommR_Title` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6f17d534`  
**Description:**
Captures names with the title 'KommR' (Kommerzialrat) followed by a name, ensuring full match.

**Content:**
```
\bKommR\.(?:in)?\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+LL\.M\.|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Maga_Title` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `98693032`  
**Description:**
Captures names with the specific title 'Maga.' (Magistra) which was missing, ensuring full name capture.

**Content:**
```
\bMaga\.(?:in)?\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+LL\.M\.|\s+LLM|\s+MA|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?(?=,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1851 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/143822.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143822.1_2`)


Das Bundesfinanzgericht hat durch den Senat 6008-1 besetzt mit dem Senatsvorsitzenden  Mag. Johann Fischerlehner, der beisitzenden Richterin Maga. Ulrike Stephan, sowie den  fachkundigen Laienrichtern Michael Hinterreiter, LL.B. und Leopold Pichlbauer in der  Beschwerdesache Philippa Aufheimer, Teichschloßweg 11, 8162 Haufenreith, Österreich, vertreten durch Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH, Bahnhofstraße 13, 4400 Steyr, über die Beschwerde vom 9. März  2023 gegen den Bescheid des Finanzamtes Österreich vom 22. Februar 2023 mit dem der  Antrag gemäß § 299 Abs. 1 Bundesabgabenordnung vom 29.07.2022, eingebracht am  29.07.2022, betreffend den Bescheid über die Wiederaufnahme des Verfahrens gemäß  § 303  Abs. 1 BAO vom 21.12.2021 abgewiesen wurde, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben und der angefochtene  Bescheid dahingehend abgeändert, dass der Bescheid vom 21. Dezember 2021, mit  dem die belangte Behörde zu Einheitswertaktenzeichen EW-AZ die  Wiederaufnahme des Verfahrens gemäß § 303 Abs. 1 BAO des mit Bescheid vom  13.12.2016 abgeschlossenen Verfahrens betreffend die Zurechnungsfortschreibung  gemäß § 21 Abs. 4 BeWG zum 01.01.2015 verfügt hat, aufgehoben wird.

**False Positives:**

- `Maga. Ulrike Stephan` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Michael Hinterreiter, LL.B.`(person)
- `Leopold Pichlbauer`(person)
- `Philippa Aufheimer`(person)
- `Teichschloßweg 11, 8162 Haufenreith, Österreich`(address)
- `Schwarz Kallinger Zwettler   Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `Beschwerdesache_Standalone_Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `42fef827`  
**Description:**
Captures person names in 'in der Beschwerdesache' context when no title is present, to catch names like 'Karsten Sofka'.

**Content:**
```
(?:in\s+der\s+(?:Beschwerdesache|Verwaltungsstrafsache)\s+)(?:des\s+|der\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*)(?=,|\s+\d|\s+\(|\s+\.)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `CD_Techn_R_Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9c99e76b`  
**Description:**
Explicitly captures the specific 'CD@Techn R' pattern found in the training data.

**Content:**
```
\bCD@Techn\s+R\s+Techn\s+R\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Frau_Name_Full` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a3923cfb`  
**Description:**
Captures full names following 'Frau' or 'Fr.', including titles like RgR, OMedR, Mag., Dr., etc., ensuring the full name is captured.

**Content:**
```
(?:Fr\.|Frau)\s+(?:Hon\.-Prof\.(?:in)?\s+|Dr\.(?:in)?\s+|Priv\.-Doz\.(?:in)?\s+|Mag\.(?:Dr\.)?\s+|Univ\.-Prof\.(?:in)?\s+|Bakk\.(?:\s+rer\.\s+nat\.|\s+rer\.\s+art\.|\s+rer\.\s+techn\.|\s+rer\.\s+jur\.)?\s+|Ing\.(?:\s+Dipl\.)?\s+|Mag\.a\s+|Prof\.in\s+|Prof\.(?:in)?\s+|RA\s+Mag\.(?:in)?\s+|DDr\.(?:in)?\s+|MedR\.(?:in)?\s+|RgR\.(?:in)?\s+|KzlR\.(?:in)?\s+|VetR\.(?:in)?\s+|KommR\.(?:in)?\s+|OMedR\s+)?([A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+(?:\s+[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)*(?:\s+-(?:[A-Z][a-z\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df]+)+)*(?:\s+MA|\s+LLB|\s+LLM|\s+LL\.M\.|\s+MSc|\s+BSc|\s+PhD|\s+BEd|\s+Bakk\.\s+phil\.|\s+Bakk\.\s+iur\.|\s+Bakk\.\s+techn\.)?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

## `Dr_Initial_Name` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `26572e1a`  
**Description:**
Captures anonymized doctor names like 'Dr. B.' or 'Dr. G.' to ensure recall in contexts where only initials are used.

**Content:**
```
\bDr\.(?:\s+[A-Z]\.)\b(?=,|\s+\d|\s+\(|\s+\.|\s+in\s+der|\s+von|\s+und)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1851 |

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (1101, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_VALIDATE/133529.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133529.1_6`)

Diese Bescheide wurden an den Bf. adressiert und an Dr. X als Erwachsenenvertreter des Bf. in  dessen Databox zugestellt. **Dr. X** war vom Bezirksgericht Salzburg im Jahr 2004 als Sachwalter  (nunmehr: Erwachsenenvertreter) zur Einkommensverwaltung des Bf. sowie zu dessen  Vertretung vor Ämtern und Behörden bestellt worden.

- missed: `Dr. X` (person)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_VALIDATE/130362.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130362.1_5`)

Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) – Herr **Priv.-Doz. Dipl.-Ing. Theobald Brauckhof** – erzielte im Streitjahr 2018 aus seiner Tätigkeit  als Vertreter bei der Firma SeeAutomotive AG Österreich Einkünfte aus nichtselbständiger Arbeit.

- missed: `Priv.-Doz. Dipl.-Ing. Theobald Brauckhof` (person)
- predicted in sentence: `Bf`, `Dipl.-Ing. Theobald Brauckhof`

**Example 2** (doc_id: `deanon_BFG_20260814_VALIDATE/140391.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140391.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Susanne Haim** in der Beschwerdesache  Rebecca Klaprodt, Edt bei Heitzing 6, 4150 Gintersberg, Österreich, vertreten durch DOCUMENTA-Treuhand WP und Stb. GmbH,  Edisonstraße 2, 4600 Wels, über die Beschwerde vom 8. Jänner 2020 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 13. Dezember 2019 betreffend Einkommensteuer  2016 Steuernummer 17-096/4990  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Susanne Haim` (person)
- predicted in sentence: `Rebecca Klaprodt`

**Example 3** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_283`)

2020-10 **Mike Staengel**  praktischer Arzt: seit Geburt Zeichen eines Aspergersyndroms mit thera- pieresistenten Schlafstörungen, Ruhelosigkeit, stereotypen Bewegungen (Stampfen mit dem  Fuß), Rückzug in eine eigene Welt, was im Kindergarten und in der Schule aufgefallen ist.

- missed: `Mike Staengel` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_VALIDATE/138745.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138745.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R. über die Beschwerde des **Chantal Franzk**,  Feldererweg 14 - 20, 5166 Rudersberg, Österreich, vom 14. Juni 2022, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 31. Mai 2022, GZ MA 67/Z2/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung in Verbindung mit §  4 Abs. 1 Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018,  nach Durchführung einer mündlichen Berufungsverhandlung am 19. September 2022, im  Beisein der Schriftführerin IP, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

- missed: `Chantal Franzk` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_VALIDATE/135765.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/135765.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Edith Lohhausen  in der Beschwerdesache der  Schmalohr + Kiekebusch Möbel, Reitermühlweg 72, 3923 Bernhards, Österreich, vertreten durch **Michael Haberl**, Winkler Straße 516 Tür 1, 8962  Gröbming, über die Beschwerde vom 20. Mai 2020 gegen den Bescheid des Finanzamtes XY  (jetzt Dienststelle des Finanzamt Judenburg Liezen ) vom 5. März 2020 betreffend Umsatzsteuer 2017 zur  Steuernummer 71-763/1501  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Michael Haberl` (person)
- predicted in sentence: `Dr.in Edith Lohhausen`

**Example 6** (doc_id: `deanon_BFG_20260814_VALIDATE/133326.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133326.1_1`)

IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter **Mag. Armin Treichl** in der Beschwerdesache  Fiona Buedenbender, Karl Peyfuß-Platz 24, 2023 Oberstinkenbrunn, Österreich, über die Beschwerde vom 18. Mai 2020 gegen den Bescheid des  Finanzamtes Bregenz vom 11. Mai 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 92-300/4861  beschlossen:  Der Vorlageantrag vom 14.10.2020 gegen die Beschwerdevorentscheidung vom 31.07.2020  betreffend Einkommensteuer 2018 wird als verspätet zurückgewiesen.

- missed: `Mag. Armin Treichl` (person)
- predicted in sentence: `Fiona Buedenbender`

**Example 7** (doc_id: `deanon_BFG_20260814_VALIDATE/132756.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132756.1_152`)

Der rechtsfreundliche Vertreter der Dr.in Ing. Viktoria Weigart nannte der Behörde in Beantwortung der  sechs Lenkererhebungen Herrn Angelstein als verantwortlichen Fuhrparkleiter der **Dr.in Ing. Viktoria Weigart**  den  die (jeweilige) Auskunft treffe.

- missed: `Dr.in Ing. Viktoria Weigart` (person)
- predicted in sentence: `Ing. Viktoria Weigart`, `Angelstein`, `Ing. Viktoria Weigart`

**Example 8** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_41`)

XXX/2 und XXX/4 per E-Mail an w.p. @ ...at  übermittelt.   Am 12.08.2010 wurde die Übergabe des Grundstücks EZ xxx Grundbuch A-Ort, A-Platz, A-Ort in  der Konkurssache Fa. A-KG von Anwalt StR Ing. Hedwig Mendle als Masseverwalter der KG an die Bf.,  vertreten durch **M.M.A.**, als Käufer auf der Grundlage des Kaufvertrags vom 28.04.2010  protokolliert.

- missed: `M.M.A.` (person)
- predicted in sentence: `Ing. Hedwig Mendle`

**Example 9** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_484`)

Zur Beschwerde erklärte der steuerliche Vertreter, dass die Bf. das Rechtsmittel im Sinne der  bisherigen Ausführungen und des Erkenntnisses des Verwaltungsgerichtshofes vom 22.07.2015  (2012/13/0037) vollumfänglich aufrecht halte, und beantragte weiters die mündliche  Gutachtenserörterung durch die Sachverständigen Iris Preining von der B-Anstalt und **M.M.B.**  von der C-Anstalt, zum Beweis der Richtigkeit des jeweiligen Gutachtens, den Ablauf bei der  Probenentnahme und Erstellung des jeweiligen Gutachtens und damit der Unrichtigkeit der  Kalkulationsgrundlagen der Behörde sowie die Einvernahme des Geschäftsführers der Lemost-Handel GmbH  E.St., zum Beweis für die tatsächlich gelieferte Fleischqualität im Prüfungszeitraum und  damit zur Höhe des tatsächlichen Fleischabschnitts un der Fleischmenge, die verkaufbar  gewesen wäre.

- missed: `M.M.B.` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_VALIDATE/130411.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130411.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Wolfgang Pavlik, den Richter  Dr. Wolfgang Aigner sowie die fachkundigen Laienrichter Erwin Agneter und Mag. Belinda  Maria Eder über die Beschwerde der Xaver Plaumert, BEd, Hinterzeile 24, 3483 Wagram am Wagram, Österreich, vertreten durch Fa Witago  Wirtschaftsprüfungs- und Steuerberatungs Ges.m.b.H, Friedlgasse 25/3/17, 1190 Wien, gegen  die Bescheide des Finanzamtes Wien 9/18/19 Klosterneuburg betreffend   - Wiederaufnahme des Verfahrens gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die  Jahre 2002 bis 2004 und Körperschaftsteuer für die Jahre 2003 bis 2004,  - Umsatzsteuer für die Jahre 2002 bis 2005,   - Körperschaftsteuer für die Jahre 2003 bis 2005,   - Kapitalertragsteuer für die Jahre 2003 bis 2005,   nach Durchführung einer mündlichen Verhandlung am 17.09.2020 in Anwesenheit der  Schriftführerin **Mag. Katharina Moravec** zu Recht erkannt:   Die Beschwerde gegen die Bescheide betreffend Wiederaufnahme des Verfahrens  gemäß § 303 Abs. 4 BAO hinsichtlich Umsatzsteuer für die Jahre 2002 bis 2004 und hinsichtlich  Körperschaftsteuer für die Jahre 2003 und 2004, wird als unbegründet abgewiesen.

- missed: `Mag. Katharina Moravec` (person)
- predicted in sentence: `Dr. Wolfgang Pavlik`, `Dr. Wolfgang Aigner`

**Example 11** (doc_id: `deanon_BFG_20260814_VALIDATE/133135.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133135.1_2`)

2.) über die Beschwerde vom 2. November 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22, nunmehr Finanzamt Österreich, vom 6. Oktober 2020 betreffend  Abweisung des Antrages vom 3. Juni 2020 auf erhöhte Familienbeihilfe für **Lubomir Nakajima**  für den Zeitraum September 2015 bis April 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Lubomir Nakajima` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_3`)

Begründung  Verfahrensgang  Mit Bescheid vom 17.07.2015 wurde dem Antrag der **Jeremias Kierstan**, vertreten durch Herrn  Vertreter, auf Herabsetzung der Abwassergebühr für den Zeitraum 01.01.2013 bis 31.12.2013  stattgegeben, eine Nichteinleitungsmenge von 172 m3 anerkannt und die Abwassergebühr von  4.813,83 € auf 4.488,75 € herabgesetzt.

- missed: `Jeremias Kierstan` (person)
- predicted in sentence: `Vertreter`

**Example 13** (doc_id: `deanon_BFG_20260814_VALIDATE/138965.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138965.1_148`)

2020-10 **Mike Staengel**  praktischer Arzt: seit Geburt Zeichen eines Aspergersyndroms mit thera- pieresistenten Schlafstörungen, Ruhelosigkeit, stereotypen Bewegungen (Stampfen mit dem  Fuß), Rückzug in eine eigene Welt, was im Kindergarten und in der Schule aufgefallen ist.

- missed: `Mike Staengel` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_VALIDATE/148131.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/148131.1_33`)

Als  Mitglied des Heidrun Schweinebraden  ist sie der **Dorothea Hasslocher**  als Zentralinstitut angeschlossen und  damit gemäß § 27a BWG verpflichtet, zur Sicherung der Finanzmarktstabilität an einem System  des gemeinsamen Liquiditätsausgleichs teilzunehmen (Liquiditätsverbund).

- missed: `Dorothea Hasslocher` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_VALIDATE/130535.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130535.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Regina Vogt** in der Beschwerdesache  Sean Herdling, J. Heiser-Straße 3, 8361 Hatzendorf, Österreich, vertreten durch NÖ Landesverein für Erwachsenenschutz,  Wienerstrasse 2/2/2, 2340 Mödling, über die Beschwerde vom 6. November 2019 gegen den  Bescheid des Finanzamtes Neunkirchen Wr. Neustadt vom 8. Oktober 2019 betreffend  Rückforderung von Familienbeihilfe für den Zeitraum April 2018 bis März 2019 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Regina Vogt` (person)
- predicted in sentence: `Sean Herdling`

**Example 16** (doc_id: `deanon_BFG_20260814_VALIDATE/137842.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137842.1_14`)

Vergl. hierzu “österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler” und  die Stellungnahme der Volksanwaltschaft - **MR Dr. Heidi Pacher** vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

- missed: `MR Dr. Heidi Pacher` (person)
- predicted in sentence: `Dr. Franz Leidenmühler`, `Dr. Heidi Pacher`, `Mag`, `Dr. Juliane Bogner Strauß`

**Example 17** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_6`)

Der Geschäftsführende Alleingesellschafter ist der Ehegatte von **M.M.B.**: M.M.A..  Die Stammeinlage von 35.000 € wurde zur Gänze einbezahlt. Der Bilanzstichtag ist der  28. Februar.

- missed: `M.M.B.` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_VALIDATE/138558.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138558.1_28`)

Der angefochtene Bescheid vom 17.07.2015, mit welchem über den Antrag der Heimwerk GmbH auf  Herabsetzung der Abwassergebühr für 2013 abgesprochen wurde, ist an die **Jeremias Kierstan**  als  Partei ergangen und an deren Zustellbevollmächtigten, Herrn Vertreter zugestellt worden.

- missed: `Jeremias Kierstan` (person)
- predicted in sentence: `Vertreter`

**Example 19** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_144`)

Dr. W F K 7,14  16.04.2013 - **Dr. W** FK 7,14  10 von 43 Seite 11 von 43

- missed: `Dr. W` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_VALIDATE/140644.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140644.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Anna Mechtler-Höger** in der  Verwaltungsstrafsache gegen Susette Jungabel, Ziegelfeldstraße 71, 5141 Puttenhausen, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz  2006, über die Beschwerde des Beschuldigten vom 17. März 2023 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 27. Februar 2023, GZ.  MA67/Zahl/2022,zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

- missed: `Mag. Anna Mechtler-Höger` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_VALIDATE/129024.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/129024.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Marco Laudacher in der Beschwerdesache  Reneé Dreyssig, Anton Afritsch-Gasse 40, 4073 Lohnharting, Österreich  vertreten durch **Mag. Manfred Frühwirth**, Wirtschaftstreuhand –  und Steuerberatung GmbH, Ferihumerstraße 29, Tür 12, 4040 Linz, vom 30. August 2017,  gegen den Bescheid des Finanzamtes Linz vom 31. Mai 2017 betreffend Körperschaftsteuer  2011

- missed: `Mag. Manfred Frühwirth` (person)
- predicted in sentence: `vertreten durch Mag. Manfred Frühwirth`

**Example 22** (doc_id: `deanon_BFG_20260814_VALIDATE/137076.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137076.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Ulrike Stephan** in der Beschwerdesache  Valentin Joebges, LLM, Bärngarten 17, 9713 Hochegg, Österreich, über die Beschwerde vom 23.08.2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Braunau Ried Schärding) vom 11. August 2020  betreffend Abweisung der Wiederaufnahmeanträge betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, 2016, 2017 und 2018 Steuernummer 84-167/9727  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Ulrike Stephan` (person)
- predicted in sentence: `Valentin Joebges`

**Example 23** (doc_id: `deanon_BFG_20260814_VALIDATE/146587.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146587.1_42`)

Die im Firmenbuchregister am 27.06.2017 von Amts wegen gemäß § 30/2 UGB gelöschte KG,  FN 2i, war eine Gesellschaft im Geschäftszweig „Bewirtschaftung und Verwaltung von eigenen  Immobilien“ mit Komplementär O.W.1 und der Rechtsanwältin **Jakob BatheW.** als Kommanditistin.

- missed: `Jakob BatheW.` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_VALIDATE/143052.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143052.1_182`)

Im Antrag wurde ausgeführt, dass die  Geschäftsführung der A.-AG-FL von Herrn X. (Geschäftsführer der **Madeleine Jahns**, gleichzeitig auch  Geschäftsführer der B.-GmbH und Verwaltungsrat der A.-AG-FL) wahrgenommen und  Managementgebühren verrechnet werden sollten.

- missed: `Madeleine Jahns` (person)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_VALIDATE/136882.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/136882.1_6`)

Aufgrund des Inhaltes der Straf- und Veranlagungsakten wird im  Zusammenhalt mit der Verantwortung des Beschuldigten nachstehender Sachverhalt als  erwiesen festgestellt:  Der am 1965 geborene **Harald Hilderink**  ist österreichischer Staatsbürger und gilt als  finanzbehördlich unbescholten.

- missed: `Harald Hilderink` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_VALIDATE/138417.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/138417.1_57`)

Am 28.09.2020 beantragte das **Jaden Knauss**  die Rückzahlung eines Betrages von € 2.274.683,82.

- missed: `Jaden Knauss` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_VALIDATE/143044.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143044.1_2`)

Das Bundesfinanzgericht hat durch den Richter Mag. Bodo Heumaier  in der Angelegenheit der Parteien  **KzlR HR Lothar Schoeberl**, PLZ1 Stadt1 (Beschwerdeführerin), und FA Braunau Ried Schärding  als Amtspartei über die  Beschwerde vom 25.8.2022   gegen den Bescheid des Finanzamtes vom 4.8.2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016   zu Recht erkannt:  Der bekämpfte Bescheid wird abgeändert.

- missed: `KzlR HR Lothar Schoeberl` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_VALIDATE/133138.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133138.1_4`)

Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 25. Februar 2021, Zahl MA67/Zahl,  wurde der nunmehrige Beschwerdeführer (Bf.) **Ivan Thöner**, Landlerweg 28, 4273 Kaltenberg, Österreich, bestraft, weil er das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 02.11.2020 um  10:38 Uhr in der gebührenpflichtigen Kurzparkzone in 1170 Wien, Beheimgasse gegenüber 32  abgestellt habe, ohne für seine Kennzeichnung mit einem für den Beanstandungszeitpunkt  gültigen Parkschein gesorgt zu haben.

- missed: `Ivan Thöner` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_89`)

Der Bf. verwies auf:  Auszug aus überreichten Infoblättern Dr. B („**Dr. B**“):   „... Eine Veränderung im Gen, welches für den Homocysteinabbau verantwortlich ist, kann zu  einer Erhöhung des Homocysteinspiegels führen.

- missed: `Dr. B` (person)
- predicted in sentence: —

**Example 30** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_2`)

Saskia Sinnwell, Wien1  beide vertreten durch **Christoph Zitz MBA**, murtax Steuerberatungs GmbH Kuenburgstraße 10,  5580 Tamsweg  wegen des Finanzvergehens der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a des  Finanzstrafgesetzes (FinStrG), beim Verband gemäß § 28a Abs. 2 FinStrG, über die Beschwerde  des Amtsbeauftragten vom 17. September 2019 (gemeint wohl richtig: 3. Dezember 2020)  gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19  Klosterneuburg als Organ des ehemaligen Finanzamtes Wien 9/18/19 Klosterneuburg als  Finanzstrafbehörde vom 30. September 2020, SpS 2000, in der Sitzung am 27. Mai 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:  Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Christoph Zitz MBA` (person)
- predicted in sentence: —

**Example 31** (doc_id: `deanon_BFG_20260814_VALIDATE/143925.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143925.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Irene Kohler** in der  Verwaltungsstrafsache gegen Bodo Nöth, Lipizzaner-Gasse 13, 4113 Oberhart, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 11. Jänner 2024 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  11. Dezember 2023, GZ. MA67/Zahl/2023, zu Recht erkannt:  Der Beschwerde wird Folge gegeben, das angefochtene Straferkenntnis aufgehoben und das  Strafverfahren gemäß § 45 Abs. 1 Z 1 VStG eingestellt.  Gemäß § 52 Abs. 8 VwGVG hat der Beschwerdeführer keinen Beitrag zu den Kosten des  Beschwerdeverfahrens zu leisten.

- missed: `Mag. Irene Kohler` (person)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_VALIDATE/143501.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/143501.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter **Mag. Dimitri Usslar**  in der Beschwerdesache Jessica Abdulkarim,  vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien,  gegen den Bescheid des Finanzamtes Österreich vom 15. Mai 2023 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2021 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

- missed: `Mag. Dimitri Usslar` (person)
- predicted in sentence: `Jessica Abdulkarim`

**Example 33** (doc_id: `deanon_BFG_20260814_VALIDATE/139845.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139845.1_14`)

Das Bundesfinanzgericht stellt auf Basis des oben geschilderten Verwaltungsgeschehens, der  aktenkundigen Unterlagen, des Vorbringens der Parteien sowie der schriftlich eingeholten  Zeugenaussage von Dipl. Kff. Sara Füßgen  folgenden entscheidungswesentlichen Sachverhalt fest:  Der Bf. und **Dipl. Kff. Sara Füßgen**  waren bis 13.01.2014 verheiratet.

- missed: `Dipl. Kff. Sara Füßgen` (person)
- predicted in sentence: —

**Example 34** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_24`)

meritorisch verwies die **Leroy Kusznierz**  auf die Darlegungen in der  Beschwerde, die unverändert aufrechterhalten wurden.

- missed: `Leroy Kusznierz` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_470`)

Zur Akne-/Narbenbehandlung  07.02.2013 € 43,74 3 * Teebaum Medicamo24 Dr.S   31.05.2013 € 43,74 3* Teebaum Medicamo24 **Theodora Hartzheim, BA Bakk. phil.**  Ansicht FA:  Es liegt eine zeitnahe ärztliche Verordnung vom 25.3.2013 vor (Anm.: von Theodora Hartzheim, BA Bakk. phil. mit dem  Vermerk „Akne, Fructoseintoleranz, Zöliakie, Milchunverträglichkeit“).

- missed: `Theodora Hartzheim, BA Bakk. phil.` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_VALIDATE/149865.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/149865.1_4`)

Entscheidungsgründe  I. Verfahrensgang  Das Beschwerdeverfahren betrifft die Einkommensteuer für die Jahre 2015 bis 2019 des  mittlerweile am 3. November 1972  verstorbenen **Reneé Keles** (im Folgenden als Beschwerdeführer  bezeichnet).

- missed: `Reneé Keles` (person)
- predicted in sentence: —

**Example 37** (doc_id: `deanon_BFG_20260814_VALIDATE/134373.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/134373.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Andrea Müller-Dobler MBA MSc** über die  Beschwerde des Hilde Schorpp, Wandschaml 94, 4625 Grub, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67, vom 21. Dezember 2020, Zahl MA67/Zahl/2020,  betreffend Übertretung der Rechtsvorschrift des § 2 in Verbindung mit § 4 Abs. 2  Parkometergesetz 2006, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z 2 VStG eingestellt.  II. Gemäß § 52 Abs. 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

- missed: `Mag. Andrea Müller-Dobler MBA MSc` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_VALIDATE/145109.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/145109.1_38`)

3,99 Lesebrille Geschäft 1 („Geschäft 1“)  7,14   0 Dr. W („**Dr. W**“)

- missed: `Dr. W` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_VALIDATE/132418.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132418.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Helga Hochrieser** in der  Beschwerdesache Gebhard Klutentreter, Pfiferweg 136, 4906 Feichtet, Österreich, über die Beschwerde vom 17. Jänner 2017  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2017 betreffend Abweisung des  Antrags auf Ausgleichszahlung (Familienbeihilfe) ab Juli 2016 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 Bundesabgabenordnung (BAO) abgewiesen.

- missed: `Mag. Helga Hochrieser` (person)
- predicted in sentence: `Gebhard Klutentreter`

**Example 40** (doc_id: `deanon_BFG_20260814_VALIDATE/141031.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/141031.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Maga. Ulrike Nussbaumer LL.M.  M.B.L., die Richterin Drin. Elisabeth Hafner, sowie die fachkundigen Laienrichter Eva Maiwald- Wanderer und **Mag. Maximilian Turrini** in der Beschwerdesache Anton Schwingschlögl, Rappelweg 12, 4724 Mäusburg, Österreich  vertreten durch CENTURION Wirtschaftsprüfungs- und Steuerberatungs GmbH, Hegelgasse 8  Tür 14, 1010 Wien, über die Beschwerden je vom 23. August 2022 gegen die Bescheide des  Finanzamtes Österreich vom 19. und 20. Juli 2022 die Berichtigung des  Einkommensteuerbescheides 2016 vom 03. Mai 2018 gemäß § 293b BAO und die  Einkommensteuer 2017 betreffend (Steuernummer 79-281/4180) nach Durchführung einer  mündlichen Verhandlung am 12. Mai 2023 zu Recht erkannt:  I. Der Beschwerde gegen den Bescheid vom 20. Juli 2022 die Berichtigung des  Einkommensteuerbescheides 2016 vom 03. Mai 2018 betreffend wird gemäß § 279  BAO Folge gegeben.

- missed: `Mag. Maximilian Turrini` (person)
- predicted in sentence: `M.`, `Anton Schwingschlögl`

**Example 41** (doc_id: `deanon_BFG_20260814_VALIDATE/144218.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/144218.1_1`)

BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch die Richterin Dr. Maria Grohe in der Revisionssache  **Torsten Vorholt**, Steinleitenweg 55, 9544 Untersee, Österreich, vertreten durch Dr. Schmalzl und Dkfm. Vogler  Steuerberatungsgesellschaft m.b.H., Roseggerstraße 4, 2500 Baden, über den Antrag der  Revisionswerberin vom 8. März 2024, der Revision vom 8. März 2024 gegen das Erkenntnis des  Bundesfinanzgerichtes vom 23. Jänner 2024, GZ. RV/7101341/2020, betreffend  Körperschaftsteuer 2014 - 2017 erhobenen Ordentlichen Revision die aufschiebende Wirkung  zuzuerkennen, beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

- missed: `Torsten Vorholt` (person)
- predicted in sentence: `Dr. Maria Grohe`, `Dr. Schmalzl`

**Example 42** (doc_id: `deanon_BFG_20260814_VALIDATE/137606.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/137606.1_85`)

Entgegen der Schlussfolgerung im Sachverständigengutachten von **Dr. Dok1** ist der Umstand,  dass keine Therapien und keine ärztliche Verlaufsdokumentation vorgelegt wurden, nicht  geeignet darauf zu schließen, dass keine Behinderung vorliegt!

- missed: `Dr. Dok1` (person)
- predicted in sentence: `Dr. Dok`

**Example 43** (doc_id: `deanon_BFG_20260814_VALIDATE/131952.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/131952.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter[...] in der Verwaltungsstrafsache gegen  **Niklas Radschweit**, Kaiserfeld 4, 8673 Steinhöf, Österreich, wegen der Verwaltungsübertretungen gemäß § 16 Abs. 1 des  Wiener Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBI. für Wien Nr. 20, in der  Fassung des LGBI. Nr. 71/2018 in der Fassung des LGBl für Wien Nr. 50/2013 in Verbindung mit  § 1 Abs. 1 GAG und Tarifposten B 1 und B 8 über die Beschwerde der Beschuldigten vom  15.11.2020 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6 -  Abgabenstrafen, vom 20.10.2020, Zahl: MA6/[...], zu Recht erkannt:  I.) Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde stattgegeben, das angefochtene  Straferkenntnis aufgehoben und das Verfahren nach § 45 Abs. 1 Z. 2 VStG eingestellt.   II.) Gemäß § 52 Abs. 1 und 8 VwGVG i. V. m. § 24 Abs. 1 BFGG und § 5 WAOR hat die  beschwerdeführende Partei keine Kosten des verwaltungsgerichtlichen Strafverfahrens zu  tragen.

- missed: `Niklas Radschweit` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_VALIDATE/130819.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/130819.1_28`)

Fristgerecht teilte der Vertreter mit, dass er von der ZweitBf. und der **Gustav Nowak**  mit der  Vertretung in den gegenständlichen Beschwerdesachen beauftragt worden sei und berief sich  in einem auf die ihm erteilte mündliche Bevollmächtigung.

- missed: `Gustav Nowak` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_VALIDATE/139070.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/139070.1_1`)

BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht fasst durch den Richter **Mag. Günter Narat** in der Revisionssache  Ferdinand Janßon, Robert-Musil-Gasse 10, 4631 Achleiten, Österreich  Steuernummer: 02-858/2848, vertreten durch den RA Mag.  Wolfgang Kempf, Bürgerstraße 41, 4020 Linz, über den Antrag der Revisionswerberin vom 18.  August, der gegen den Beschluss des Bundesfinanzgerichtes vom 5. Juli 2022,  RV/5100264/2021 (belangte Behörde: Finanzamt Österreich), betreffend die  Umsatzsteuerbescheide 2010 – 2017, erhobenen außerordentlichen Revision die  aufschiebende Wirkung zuzuerkennen, den Beschluss:   I)  Gem.

- missed: `Mag. Günter Narat` (person)
- predicted in sentence: `Mag.  Wolfgang Kempf`

**Example 46** (doc_id: `deanon_BFG_20260814_VALIDATE/140858.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/140858.1_140`)

Da zudem - wie bereits dargelegt - die Stellungnahme des **Dr. F**  nunmehr in die Begutachtung miteinbezogen wurde, die Gutachterin aber dennoch in  Bestätigung der Vorgutachten zum selben Ergebnis gelangt ist, kann nach dem Vorgesagten  insgesamt nicht davon gesprochen werden, dass den Gutachten mehrere Mängel anhaften  würden bzw. ist jedenfalls davon auszugehen, dass diese allfälligen Mängel mittlerweile  behoben sind.

- missed: `Dr. F` (person)
- predicted in sentence: —

**Example 47** (doc_id: `deanon_BFG_20260814_VALIDATE/132636.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/132636.1_3`)

über die Beschwerde der **Balthasar Brendtke**, Jaro Schmied-Straße 6, 4152 Lämmerstorf, Österreich, vom 17. März 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67 vom 12. März 2021, Zl. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 2 in Verbindung mit § 4 Abs. 2 Parkometergesetz 2006, LGBl.  für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

- missed: `Balthasar Brendtke` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_VALIDATE/133257.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/133257.1_46`)

Da das Beschwerdeverfahren gegen Frau A B als Geschäftsführerin der **Saskia Sinnwell**  und somit  als Entscheidungsträgerin iSd § 3 Abs. 2 VbVG kein rechtswidriges oder schuldhaftes Verhalten  ergeben hat, liegen die Voraussetzungen für die Verhängung einer Geldbuße über die  Saskia Sinnwell  als belangten Verband nicht vor.

- missed: `Saskia Sinnwell` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_VALIDATE/146818.1`) (sent_id: `deanon_BFG_20260814_VALIDATE/146818.1_343`)

Das Finanzamt ging davon aus, dass die Einnahme und Besorgung dieses Mittels  ohne ärztliche Anordnung bzw. Absprache mit **Dr. W** getätigt wurde.

- missed: `Dr. W` (person)
- predicted in sentence: —

</details>

---

