# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-11-16T16:59:52.523464

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/person/2026-11-16_v9/config.yaml 
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
| Train sentences | 7310 |
| Validation sentences | 2144 |
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
| True Positives | 691 |
| False Positives | 459 |
| False Negatives | 923 |
| Total Gold Entities | 1614 |
| Micro Precision | 60.1% |
| Micro Recall | 42.8% |
| Micro F1 | 50.0% |
| Macro F1 | 50.0% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `OMedR Pattern` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Complex Title Combinations` | 0.6% | 100.0% | 0.3% | 5 | 5 | 0 |
| `Anonymized Names with Digits` | 0.4% | 100.0% | 0.2% | 3 | 3 | 0 |
| `Dr.in Pattern` | 2.0% | 94.1% | 1.0% | 17 | 16 | 1 |
| `Academic and Professional Titles Refined` | 40.2% | 83.6% | 26.5% | 511 | 427 | 84 |
| `Representative Context` | 1.6% | 81.2% | 0.8% | 16 | 13 | 3 |
| `Herr Name Context` | 4.1% | 75.6% | 2.1% | 45 | 34 | 11 |
| `Standalone Name in Complaint Context Refined` | 17.4% | 45.4% | 10.8% | 383 | 174 | 209 |
| `Prof. Title Pattern` | 0.5% | 44.4% | 0.2% | 9 | 4 | 5 |
| `Frau Name Context Refined` | 0.4% | 33.3% | 0.2% | 9 | 3 | 6 |
| `Mag.a Pattern` | 0.1% | 25.0% | 0.1% | 4 | 1 | 3 |
| `Anonymized Initials and Digits` | 0.6% | 22.7% | 0.3% | 22 | 5 | 17 |
| `Name with Suffix Pattern` | 0.2% | 15.4% | 0.1% | 13 | 2 | 11 |
| `Von Name Context` | 0.2% | 6.2% | 0.1% | 32 | 2 | 30 |
| `Richter/Richterin Context` | 0.1% | 3.6% | 0.1% | 28 | 1 | 27 |
| `Complex Legal Titles` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Simple First Name Only (Contextual)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Honorifics Herr/Frau Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `VetR Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Anonymous Initial Name` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `Dr.Daisy Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `MMA Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Arthur Jonas Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `VetR Prof.in Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `HR Title Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Professional Role Name` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `seitens der Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Witness Name Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag. A. Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fr.PhD Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Missed Names - Single Word` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Missed Names - Complex Titles` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Missed Names - Full Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name After Verb Context` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Herr Name Context Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name After Preposition On` | 0.0% | 0.0% | 0.0% | 16 | 0 | 16 |
| `Name After Medical Context` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Single Word Name in Case Citation Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Single Word Name in Witness Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Name with Suffix Pattern Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Standalone Name in Witness/Subject Context` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Anonymous/Initial Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Signature/End Name Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Missed Names - Single Word Refined` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Complex Title Combinations Refined` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `Single Initial Name Context` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Single Word Name in Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Anonymous Initial Names Refined` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `OMedR Pattern` 

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `fb798716`  
**Description:**
Specifically targets the medical legal title 'OMedR' followed by a full name.

**Content:**
```
\bOMedR\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 0 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_323`)


maps eine Fahrtstrecke  von 65 km in Ansatz gebracht (wie schon die Fahrt zu OMedR Emilia Kusmierz.

| Predicted | Gold |
|---|---|
| `OMedR Emilia Kusmierz` | `OMedR Emilia Kusmierz` |

</details>

---

## `Complex Title Combinations` 

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `7fadc38b`  
**Description:**
Captures names with multiple consecutive titles (e.g., 'Hon.-Prof. VetR', 'HA Dr.') and suffixes like ', MA', ', LLB', ', Bakk. techn.' ensuring the full string is captured.

**Content:**
```
\b(?:Hon\.-Prof\.|VetR|HA|RgR)\s+(?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Prof\.in|Prof\.|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|Dipl\. Kff\. StR|StR|OMedR)(?:[ ]+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:[ ]+[A-Z][a-z]+)+)+(?:,\s+(?:LLM|MSc|MBA|BSc|M\.A\.|LLB|Bakk\. iur\. |Bakk\. phil\. |Bakk\. rer\. nat\. |Bakk\. art\. |Bakk\. techn\. |LL\.B\. |LL\.M\.)+)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 0 | 1609 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `VetR OMedR Constantin Wiedewilt` | `VetR OMedR Constantin Wiedewilt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Furtgasse 15, 3204 Kirchberggegend, Österreich` (address)
- `INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Florian Rouse  in der Beschwerdesache Evamaria Watenphul,  Allhartsbergerstraße 47, 8142 Kasten, Österreich, vertreten durch Mehmet Köprücü, Puchheimgasse 14, 6234 Brandenberg, Österreich, betreffend Beschwerde  vom 21. September 2022 gegen den Haftungsbescheid des Finanzamtes Österreich vom  6. September 2022, 83-456/1644, beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Univ.-Prof. Florian Rouse` | `Hon.-Prof. Univ.-Prof. Florian Rouse` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Evamaria Watenphul` (person)
- `Allhartsbergerstraße 47, 8142 Kasten, Österreich` (address)
- `Mehmet Köprücü` (person)
- `Puchheimgasse 14, 6234 Brandenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-456/1644` (tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/144771.1`) (sent_id: `deanon_BFG_20260814_TEST/144771.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Annette Wöhrl  in der Beschwerdesache VetR Univ.-Prof. Wigand Gervais,  Lorenzen 10, 6183 Kühtai, Österreich, vertreten durch die Steuerkanzlei Holowinski  Partner KG, Hasenauerstraße  18/1/Top 2, 1190 Wien, über die Beschwerde vom 19. Juli 2023 gegen den Bescheid des  Finanzamtes Österreich vom 19. Mai 2023  betreffend Körperschaftsteuer 2020,  Steuernummer 92-114/1027, zu Recht erkannt:   I. Von der Festsetzung der Körperschaftsteuer 2020 wird gemäß § 206 lit. b BAO Abstand  genommen.

| Predicted | Gold |
|---|---|
| `VetR Univ.-Prof. Wigand Gervais` | `VetR Univ.-Prof. Wigand Gervais` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Annette Wöhrl` (person)
- `Lorenzen 10, 6183 Kühtai, Österreich` (address)
- `Steuerkanzlei Holowinski  Partner KG` (organisation)
- `Finanzamtes Österreich` (organisation)
- `92-114/1027` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/144847.1`) (sent_id: `deanon_BFG_20260814_TEST/144847.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Mag. James Thomalla  in der Beschwerdesache Jelena Ziegelmeyer,  Auer-von-Welsbach-Straße 6X, 4083 Sonnleiten, Österreich, über die Beschwerde vom 30.6.2023 gegen den Bescheid des Finanzamtes  Österreich vom 20.6.2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 den  Beschluss:   I. Der Vorlageantrag vom 22.9.2023 wird gemäß § 256 Abs 3 iVm § 264 Abs 4 lit d BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Mag. James Thomalla` | `Hon.-Prof. Mag. James Thomalla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jelena Ziegelmeyer` (person)
- `Auer-von-Welsbach-Straße 6X, 4083 Sonnleiten, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/145818.1`) (sent_id: `deanon_BFG_20260814_TEST/145818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Corinna Engenhart in der  Beschwerdesache Ilona Kiess, Breitenäckerweg 15, 3623 Bernhards, Österreich, vertreten durch RgR ÖkR Wendelin Sladezek, über die  Beschwerde vom 22. April 2024 gegen die Bescheide des Finanzamtes Österreich vom  13. Februar 2024 betreffend Einkommensteuer 2018 sowie Festsetzung von Anspruchszinsen  2018, Steuernummer 73-866/9272, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `RgR ÖkR Wendelin Sladezek` | `RgR ÖkR Wendelin Sladezek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Corinna Engenhart` (person)
- `Ilona Kiess` (person)
- `Breitenäckerweg 15, 3623 Bernhards, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `73-866/9272` (tax_number)

</details>

---

## `Anonymized Names with Digits` 

**F1:** 0.004 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `827879b2`  
**Description:**
Captures anonymized names like 'Dr. Dok1', 'Dr. F1' where the name part contains digits, ensuring they are standalone entities.

**Content:**
```
\b(?:Dr\.|Mag\.|RA\.|StB\.)\s+[A-Z][a-z]+[0-9]+(?:[ ]+[A-Z][a-z]+[0-9]+)*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.004 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 0 | 1611 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_5`)


Der Antrag  wurde rückwirkend ab März 2020 gestellt.  Dr. Dok1, Facharzt für Psychiatrie, bescheinigte dem Bf. nach der am 21. Oktober 2020 im  Sozialministeriumservice durchgeführten Untersuchung weder einen Grad der Behinderung  noch eine Erwerbsunfähigkeit, dies mit der Begründung, dass keine ausreichenden Patienten-  bzw. aufschlussreichen medizinischen Unterlagen – bis auf einen 4 Jahre alten Diabetespass –  vorgelegt worden seien.

| Predicted | Gold |
|---|---|
| `Dr. Dok1` | `Dr. Dok1` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_10`)


Der Bf. wurde am 14. April 2021 ein weiteres Mal untersucht und von Dr. Dok2, Fachärztin für  Allgemeinmedizin, folgendes Gutachten erstellt:  2 von 13 Seite 3 von 13

| Predicted | Gold |
|---|---|
| `Dr. Dok2` | `Dr. Dok2` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_16`)


Behandlung(en) / Medikamente / Hilfsmittel:  keine Therapie  Sozialanamnese:  bis Oktober sei er von PVA arbeitsunfähig geschrieben worden, neue Untersuchung hätten  noch nicht stattgefunden   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  Befunde nachgereicht.:   Einladung für Untersuchung nach dem Behinderteneinstellungsgesetz am 11.05:21 um 16 Uhr  Ordination Dr. Dok1  PVA GA DR.

| Predicted | Gold |
|---|---|
| `Dr. Dok1` | `Dr. Dok1` |

</details>

---

## `Dr.in Pattern` 🏆

**F1:** 0.020 | **Precision:** 0.941 | **Recall:** 0.010  

**Format:** `regex`  
**Rule ID:** `5c08400b`  
**Description:**
Specifically targets the feminine academic title 'Dr.in' followed by a full name.

**Content:**
```
\bDr\.in\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.941 | 0.010 | 0.020 | 17 | 16 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 16 | 1 | 1598 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_111`)


Gutachten erstellt am 31.01.2017 von Dr.in Silvia Bauer  Gutachten vidiert am 31.01.2017 von Dr.in Renate Reininger"

| Predicted | Gold |
|---|---|
| `Dr.in Renate Reininger` | `Dr.in Renate Reininger` |

**Missed by this rule (FN):**

- `Dr.in Silvia Bauer` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Manegold  über die Beschwerde des Dr.in KzlR Helge Erwied,  Unterfeichten 5, 4055 Sipbach, Österreich, vom 23. Dezember 2020, gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 17. Dezember 2020, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Dr.in Regina Manegold` | `Dr.in Regina Manegold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in KzlR Helge Erwied` (person)
- `Unterfeichten 5, 4055 Sipbach, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache Dipl. Kff. Sibylle Wahlscheid,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch Pilz + Rath Steuerberatung, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

| Predicted | Gold |
|---|---|
| `Dr.in Esra Schlink` | `Dr.in Esra Schlink` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl. Kff. Sibylle Wahlscheid` (person)
- `Gretlern 168, 3874 Gopprechts, Österreich` (address)
- `Pilz + Rath Steuerberatung` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Andrea Helbok  in der Beschwerdesache Lydia Rehnen,  Roßbergl 5, 4923 Gunzing, Österreich, vertreten durch Proxauf Meyer Zeilinger Rechtsanwälte GmbH, Etrichgasse 14,  6020 Innsbruck, über die Beschwerde vom 3.4.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 17.3.2020, SV-Nr, betr.

| Predicted | Gold |
|---|---|
| `Dr.in Andrea Helbok` | `Dr.in Andrea Helbok` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lydia Rehnen` (person)
- `Roßbergl 5, 4923 Gunzing, Österreich` (address)
- `Proxauf Meyer Zeilinger Rechtsanwälte GmbH` (organisation)
- `Finanzamtes  Innsbruck` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elmira Baintner  in der Beschwerdesache Dietmar Grießmeyer,  Stiftgasse 12, 4654 Aigen, Österreich, über die Beschwerde vom 31. Juli 2021 gegen den Bescheid des FA Steiermark Mitte  vom  26. Juli 2021 betreffend Abweisung eines Rückzahlungsantrages, Steuernummer  64-502/6730, zu Recht erkannt:   I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr.in Elmira Baintner` | `Dr.in Elmira Baintner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dietmar Grießmeyer` (person)
- `Stiftgasse 12, 4654 Aigen, Österreich` (address)
- `FA Steiermark Mitte` (organisation)
- `64-502/6730` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/136103.1`) (sent_id: `deanon_BFG_20260814_TEST/136103.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Natascha Weingarte  in der Beschwerdesache des B,  vertreten durch StB, über die Berufung vom 27. August 2012 gegen die Bescheide des  Finanzamtes X vom 10. August 2012 betreffend Einkommensteuer für die Jahre 2004 bis 2007  zu Steuernummer 46-139/2044  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Natascha Weingarte` | `Dr.in Natascha Weingarte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes` (organisation)
- `46-139/2044` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elisabeth Hafner als Vorsitzende, den  Richter Mag. Dieter Ortner sowie die fachkundigen Laienrichter Mag. Reinhard Krassnig und  Komm. Rat Max Stechauner in der Beschwerdesache Dirk Ambrose, Herrnberg 22, 5152 Schönberg, Österreich, vertreten  durch Kohlfürst, Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH, St. Veiter Ring  1A, 9020 Klagenfurt/Wörthersee, und Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010  Wien, über die Beschwerde vom 20. Dezember 2017 gegen den Bescheid des Finanzamtes  Klagenfurt (nunmehr Finanzamt Österreich) vom 23. November 2017 mit dem ein Antrag  gemäß § 303 Abs. 1 BAO vom 27. Februar 2017 auf Wiederaufnahme des Verfahrens  betreffend Einkommensteuer 2002, Steuernummer 21-063/4049, abgewiesen worden ist,  nach Durchführung einer mündlichen Verhandlung am 10. August 2022 in Anwesenheit der  Schriftführerin FOI Alexandra Dumpelnik zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Elisabeth Hafner` | `Dr.in Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dieter Ortner` (person)
- `Mag. Reinhard Krassnig` (person)
- `Komm. Rat Max Stechauner` (person)
- `Dirk Ambrose` (person)
- `Herrnberg 22, 5152 Schönberg, Österreich` (address)
- `Roth & Partner Wirtschaftsprüfung und Steuerberatung GmbH` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-063/4049` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/140410.1`) (sent_id: `deanon_BFG_20260814_TEST/140410.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr.in Elisabeth Hafner in der  Beschwerdesache Arthur Häfecker, Kompatschhof 5k, 9300 Arndorf, Österreich, über die Beschwerde vom 14. August 2017  gegen den Bescheid des Finanzamtes Klagenfurt vom 28. Juli 2017 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 Steuernummer 51-718/6521  zu Recht:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Elisabeth Hafner` | `Dr.in Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Arthur Häfecker` (person)
- `Kompatschhof 5k, 9300 Arndorf, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)
- `51-718/6521` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/142964.1`) (sent_id: `deanon_BFG_20260814_TEST/142964.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alessia Gladebeck  in der Beschwerdesache Roman Baldauf,  Georg-Aichinger-Straße 14, 4264 Helbetschlag, Österreich, über die Beschwerde vom 17. Jänner 2023 gegen den Bescheid des  Finanzamtes Österreich vom 3. Jänner 2023, Ordnungsbegriff XX1, betreffend Abweisung des  Antrages auf Familienbeihilfe ab Oktober 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Alessia Gladebeck` | `Dr.in Alessia Gladebeck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Roman Baldauf` (person)
- `Georg-Aichinger-Straße 14, 4264 Helbetschlag, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/143627.1`) (sent_id: `deanon_BFG_20260814_TEST/143627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Svetlana Ronnacker  in der Beschwerdesache der ehemals  im Firmenbuch zu FN eingetragen gewesenen, mit Beschluss des LG X am 4.7.2023 amtswegig  aus dem Firmenbuch gelöschten Franziskus Dziemballa  über deren Beschwerde vom 24. Februar 2021  gegen den Bescheid des Finanzamt Oststeiermark  vom 2. Februar 2021 betreffend Umsatzsteuerfestsetzung  06.2020 zu Steuernummer 10-349/0551  beschlossen:   I. Die Beschwerde wird als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Dr.in Svetlana Ronnacker` | `Dr.in Svetlana Ronnacker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franziskus Dziemballa` (person)
- `Finanzamt Oststeiermark` (organisation)
- `10-349/0551` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Danielle Merte  in der Beschwerdesache Mag.a Susanne Groesche Unternurpensalm 12, 5141 Moosdorf, Österreich  vertreten durch CONSULTATIO Steuerberatung GmbH & Co KG, Karl-Waldbrunner-Platz  1, 1210 Wien, über die Beschwerde vom 8. Juni 2015 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 7. Mai 2015 (jetzt Finanzamt für Großbetriebe), Steuernummer  76-369/9701, betreffend   1. Wiederaufnahme des Verfahrens zur Festsetzung der Energieabgabenvergütung für   A. 2005 – 2008,    Bäder 2005 – 2008,         Büchereien 2005 – 2008,  Bf. Kindergärten 2005 – 2008,      E. Stadion 2007,  B. Stadion 2005 – 2007,     C. Eishalle 2006, 2007,   D.Bad 2005 – 2007 und      F. Stadion 2006 und 2007  2.

| Predicted | Gold |
|---|---|
| `Dr.in Danielle Merte` | `Dr.in Danielle Merte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Susanne Groesche` (person)
- `Unternurpensalm 12, 5141 Moosdorf, Österreich` (address)
- `CONSULTATIO Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes  Wien 1/23` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `76-369/9701` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Sabrina Ternes  in der Beschwerdesache Sheila Szikorra,  Brennersee 10, 9555 St. Gandolf, Österreich, vertreten durch Auxiliaris Steuerberatung GmbH, Grazer Straße 12, 8480  Mureck, über die Beschwerde vom 11. Jänner 2019 gegen den Bescheid des Finanzamtes  Klagenfurt vom 17. Dezember 2018 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2017 zu Steuernummer 67-828/8052  zu Recht erkannt:   I. Gemäß § 279 BAO wird die Beschwerde als unbegründet abgewiesen und wird der  angefochtene Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Dr.in Sabrina Ternes` | `Dr.in Sabrina Ternes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sheila Szikorra` (person)
- `Brennersee 10, 9555 St. Gandolf, Österreich` (address)
- `Auxiliaris Steuerberatung GmbH` (organisation)
- `Finanzamtes` (organisation)
- `67-828/8052` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/146473.1`) (sent_id: `deanon_BFG_20260814_TEST/146473.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr.in Eva Mlynek  in der Beschwerdesache Günter Salfetter,  Pörlinghof/Grentnerweg 3, 3170 Gerichtsberg, Österreich, betreffend Beschwerde vom 21. April 2024 gegen den Bescheid des  Finanzamtes Österreich vom 22. März 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023 Steuernummer 79-087/2735  beschlossen:  Der Antrag auf Vorlage der Beschwerde an das Bundesfinanzgericht wird gemäß  § 264 Abs. 4 lit e BAO in Verbindung mit § 260 Abs. 1 lit. b BAO als nicht fristgerecht  eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Eva Mlynek` | `Dr.in Eva Mlynek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Günter Salfetter` (person)
- `Pörlinghof/Grentnerweg 3, 3170 Gerichtsberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `79-087/2735` (tax_number)
- `Bundesfinanzgericht` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/146537.1`) (sent_id: `deanon_BFG_20260814_TEST/146537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Dr.in Huberta Maginot  in der Beschwerdesache der  Wolensky Logistik, Knödelhütte 10, 9462 St. Peter im Lavanttal, Österreich, über die Beschwerde vom 10.Okt.2022, eingebracht am  12. Oktober 2022, gegen den zur Steuernummer 61-790/6327  ergangenen Bescheid des  Finanzamt Spittal Villach  vom 14. September 2022 betreffend Abweisung eines Antrages auf  Wiederaufnahme (§ 303 BAO) des Einkommensteuerbescheides 2018 vom 29.Jän 2020 zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Huberta Maginot` | `Dr.in Huberta Maginot` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Wolensky Logistik` (organisation)
- `Knödelhütte 10, 9462 St. Peter im Lavanttal, Österreich` (address)
- `61-790/6327` (tax_number)
- `Finanzamt Spittal Villach` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/147657.1`) (sent_id: `deanon_BFG_20260814_TEST/147657.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hemma Fieber  in der Beschwerdesache Eleonore Isenhardt,  Bachwiesenstraße 12, 6401 Inzing, Österreich, vertreten durch TPA Regio Steuerberatung GmbH, Schwedengasse 2, 3500  Krems/Donau, über die Beschwerde vom 22. Mai 2019 gegen den Bescheid des Finanzamtes  Wien 12/13/14 Purkersdorf vom 6. Mai 2019 betreffend die Wiederaufnahme des Verfahrens  gem § 303 Abs 1 BAO hinsichtlich der Einkommensteuer 2010 zu Steuernummer  94-874/0419  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Hemma Fieber` | `Dr.in Hemma Fieber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eleonore Isenhardt` (person)
- `Bachwiesenstraße 12, 6401 Inzing, Österreich` (address)
- `TPA Regio Steuerberatung GmbH` (organisation)
- `Finanzamtes  Wien 12/13/14 Purkersdorf` (organisation)
- `94-874/0419` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Lydia Stockman  in der Beschwerdesache Kaspar Sadowski,  Sankt Wendelin 50j, 3623 Elsenreith, Österreich, vertreten durch Dr. Franz Deutsch, Pfeilgasse 16/26, 1080 Wien, über die  Beschwerde vom 29. Dezember 2021 gegen den Bescheid des Finanzamtes Österreich vom  22. November 2021 betreffend Einkommensteuer 2019, Steuernummer 96-455/6800, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Lydia Stockman` | `Dr.in Lydia Stockman` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kaspar Sadowski` (person)
- `Sankt Wendelin 50j, 3623 Elsenreith, Österreich` (address)
- `Dr. Franz Deutsch` (person)
- `Finanzamtes Österreich` (organisation)
- `96-455/6800` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_111`)


Gutachten erstellt am 31.01.2017 von Dr.in Silvia Bauer  Gutachten vidiert am 31.01.2017 von Dr.in Renate Reininger"

**False Positives:**

- `Dr.in Silvia Bauer  Gutachten` — partial — gold is substring of pred: `Dr.in Silvia Bauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Silvia Bauer`(person)
- `Dr.in Renate Reininger`(person)

</details>

---

## `Academic and Professional Titles Refined` 🏆

**F1:** 0.402 | **Precision:** 0.836 | **Recall:** 0.265  

**Format:** `regex`  
**Rule ID:** `f09fb52b`  
**Description:**
Captures names preceded by academic/professional titles, explicitly handling multiple consecutive titles and ensuring full name capture including hyphenated names and suffixes. Fixes truncation issues.

**Content:**
```
\b(?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|Dipl\. Kff\. StR|Dipl\. Kfm\. StR|Dipl\. Kfm\.|Dipl\. Kff\.|StR|VetR|OMedR|RgR|HR)(?:\s+(?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Hon\.-Prof\.|Hon\.-Prof\.in|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|RA\.?|StB\.?|Gf-?))*\s+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+(?:,\s+(?:LLM|MSc|MBA|BSc|M\.A\.|LLB|Bakk\. iur\. |Bakk\. phil\. |Bakk\. rer\. nat\. |Bakk\. art\. |LL\.B\. |LL\.M\.)+)?(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.836 | 0.265 | 0.402 | 511 | 427 | 84 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 427 | 84 | 1187 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeremias Pretzel` (person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich` (address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Mag. Josef Nußbaumer` (person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Heinz Neuner` | `Dr. Heinz Neuner` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)
- `N.N.` (person)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag. Michael Nierla` | `Mag. Michael Nierla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `N.N.` (person)
- `Finanzamt für Gebühren` (organisation)
- `N.N.` (person)
- `Verwaltungsgerichtshof` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Dr. Susanne Zankl` | `Dr. Susanne Zankl` |
| `RgR Amalia Schuetzke` | `RgR Amalia Schuetzke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)
- `22-967/4918` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Saphira Blazejewicz` | `Priv.-Doz.in Saphira Blazejewicz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Jeanne Weiermann` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `Finanzamt` (organisation)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ophelia Dutschka` | `Hon.-Prof.in Ophelia Dutschka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_60`)


Der Beschwerdeführer begründet die berufliche Notwendigkeit der Teilnahme an den  gegenständlichen Kursen mit der Erlangung von Kenntnissen und Fähigkeiten zur Anwendung  Hypnosystemischer Konzepte nach Dr. Gunther Schmidt und von Kommunikationsmethoden,  wie sie im Hypnotherapeutischen Bereich zur Anwendung kämen;

| Predicted | Gold |
|---|---|
| `Dr. Gunther Schmidt` | `Dr. Gunther Schmidt` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_67`)


darüber hinaus habe  er sich bereits nach der Teilnahme am ersten von drei Kursen der „Kurzausbildung mit  Dr. Gunther Schmidt – Hypnosystemische Konzepte für Coaching, Team &  Organisationsentwicklung und Supervision“ im Herbst 2018 entschieden, sich im Laufe der Zeit  ein weiteres „Standbein“ aufzubauen, um die erworbenen Kenntnisse als  freiberuflicher/selbständiger Coach anzubieten.

| Predicted | Gold |
|---|---|
| `Dr. Gunther Schmidt` | `Dr. Gunther Schmidt` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Dr. Kurt Bartold` | `Priv.-Doz. Dr. Kurt Bartold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gruenleitner Event` (organisation)
- `Finanzamtes  Graz-Stadt` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Cassandra Witzenhause` | `Univ.-Prof.in Cassandra Witzenhause` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Mehmet Gessl  in der Beschwerdesache der  Donau-Elektro, Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich, vertreten durch Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH, Harrachgasse 26, 8010 Graz, über die Beschwerde vom 22. März 2018  gegen die Bescheide des Finanzamtes Graz-Stadt vom 16. Jänner 2018 betreffend  Umsatzsteuer und Einkommensteuer 2011 bis 2015 sowie Umsatzsteuerfestsetzung für 2- 12/2016 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Mehmet Gessl` | `Dr. Mehmet Gessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Donau-Elektro` (organisation)
- `Prof. Sinwel-Weg 16, 9560 Zingelsberg, Österreich` (address)
- `Kulmburg & Partner Wirtschaftsprüfung &  Steuerberatung GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hedwig Mackiewicz` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Dr.in Hemma Ramelow` | `Univ.-Prof.in Dr.in Hemma Ramelow` |
| `Mag. Damian Wiecher` | `Mag. Damian Wiecher` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich` (address)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Daniel Parys, Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich, vertreten durch APEX-Wirtschaftstreuhand Gesellschaft m.b.H.,  Hietzinger Hauptstraße 22/1/101, 1130 Wien, betreffend Beschwerde vom 24. April 2018  gegen den Bescheid des Finanzamtes Baden Mödling Finanzamtes Baden Mödling  Feststellungsbescheid gemäß § 92 Abs. 1 lit. c BAO (Nichtvorliegen der  Unternehmereigenschaft 2014 – 2016) vom 6. März 2018 betreffend Steuernummer xy  beschlossen:  Der Antrag auf Vorlage der Beschwerde wird gemäß § 264 Abs. 1 BAO in Verbindung mit  § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Gabriele Krafft` | `Dr. Gabriele Krafft` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Daniel Parys` (person)
- `Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Li Schukardt` | `Priv.-Doz. Li Schukardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ursula Buchholz` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Alexander Rimser` | `Mag. Alexander Rimser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OSR Corbinian Friemuth` (person)
- `Hermann` (person)
- `Magistrat der Stadt Wien` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Sven Oberstelehn` | `Hon.-Prof. Sven Oberstelehn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chantal Eligüzel` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Guntram Antepoth, Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich, über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 12. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 70-875/4351  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Guntram Antepoth` (person)
- `Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `70-875/4351` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Lilia Schöpcke` (person)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_186`)


Sie legte ein Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für Neurologie und  Psychiatrie vor.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_194`)


von der Bf. vorgelegten Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für  Neurologie und Psychiatrie.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Adebiola Bayer in der  Beschwerdesache Finn van Aken, Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich, vertreten durch Mag. Musa Işlek, Achardgasse 6,  1210 Wien, über die Beschwerde vom 29. Juni 2018 gegen den Bescheid des Finanzamtes Wien  1/23 vom 28. Mai 2018 betreffend Umsatzsteuer 2016 zu Recht:   1.

| Predicted | Gold |
|---|---|
| `Dr. Adebiola Bayer` | `Dr. Adebiola Bayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finn van Aken` (person)
- `Zum Butterkreuz 13, 3150 Schwarzenbach an der Gölsen, Österreich` (address)
- `Mag. Musa Işlek` (organisation)
- `Finanzamtes Wien  1/23` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Mag.a Livia Korowski` | `Priv.-Doz.in Mag.a Livia Korowski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sven Mitterhuber` (person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `RA Mag. Robert Bitsche` | `RA Mag. Robert Bitsche` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Roxana Dellner` (person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)
- `88-034/0292` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Günter Gopfauf, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

| Predicted | Gold |
|---|---|
| `Dr. Maria-Luise Wohlmayr` | `Dr. Maria-Luise Wohlmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Günter Gopfauf` (person)
- `Schwarze Au Spatzenweg 36, 9411 Priel, Österreich` (address)
- `Finanzamtes Salzburg – Stadt` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wladimir Dammkoehler, Grolzham 15, 3123 Obermerking, Österreich, über die Beschwerde vom 24. Jänner 2020  gegen den Bescheid des Finanzamtes Baden Mödling vom 22. Jänner 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 47-339/1168, zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wladimir Dammkoehler` (person)
- `Grolzham 15, 3123 Obermerking, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `47-339/1168` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Karin Pitzer` | `Mag. Karin Pitzer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karina Ditzler` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Serena Weidlich  in der Beschwerdesache Ruprecht Pesselt,  Blons 28, 9612 Michelhofen, Österreich, betreffend Beschwerde gegen die Buchungsmitteilung  des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel zur Steuernummer 89-624/1157, betreffend  Gebühr gemäß § 17a VfGG und Gebührenerhöhung gemäß § 9 Abs.1 GebG 1957 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Serena Weidlich` | `Hon.-Prof.in Serena Weidlich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ruprecht Pesselt` (person)
- `Blons 28, 9612 Michelhofen, Österreich` (address)
- `Finanzamtes für  Gebühren` (organisation)
- `89-624/1157` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Techn R Tosca Häfeli, Seulbergerstraße 12, 3384 Pottschollach, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Tosca Häfeli` (person)
- `Seulbergerstraße 12, 3384 Pottschollach, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Babette Nimzyk` | `Hon.-Prof.in Babette Nimzyk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tamara Poertgen, LLB Bakk. techn.` (person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich` (address)
- `Martin Friedl` (person)
- `Finanzamtes` (organisation)
- `08-216/2001` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache Cornelia Özgür,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch Thomas Krampl, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Fabienne Kattner` | `Univ.-Prof.in Fabienne Kattner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Cornelia Özgür` (person)
- `Hofbauer-Straße 6, 9854 Krainberg, Österreich` (address)
- `Thomas Krampl` (person)
- `Finanzamtes für Gebühren` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Daisy Hoopt` | `Univ.-Prof.in Daisy Hoopt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in StR DDr.in Reneé Plein` (person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Andrea Ebner` | `Mag. Andrea Ebner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominika Oehlerich, BEd` (person)
- `Zamberg 9, 3843 Hohenau, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Mag. Manuela Fischer` | `Mag. Manuela Fischer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Isidor Czebulla` (person)
- `Eggenburger Straße 88, 9423 Pfaffendorf, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Waldemar Faltermeir  in der Beschwerdesache  Elias Kendziorra,  Fernblick 3, 6410 Telfs, Österreich, über die Beschwerde vom 24. Mai 2017 gegen den Bescheid des Finanzamt Waldviertel  vom 22. Mai 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016  Steuernummer 29-596/0625  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Waldemar Faltermeir` | `Dr. Waldemar Faltermeir` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Kendziorra` (person)
- `Fernblick 3, 6410 Telfs, Österreich` (address)
- `Finanzamt Waldviertel` (organisation)
- `29-596/0625` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heinz Herper` (person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich` (address)
- `Dr. Thomas Hofer-Zeni` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_115`)


• Schreiben des Bezirksgerichtes Donaustadt vom 29. Juli 2013 (Verständigung gemäß §  126 AußStrG)  • Psychiatrisches Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9  Dem Ersteller des Gutachtens, Dr. Wolfgang Baischer, Facharzt für Psychiatrie und Neurologie  wurden folgende Befunde vorgelegt:  Psychiatrische Abteilung des SMZ-Ost, Aufenthalt vom 21. Oktober bis 5. November 2012:  "Chronisch-progrediente Encephalitis disseminata mit organischem Psychosyndrom, gemischte  schizoaffektive Störung.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_161`)


Beweiswürdigung:  Der als erwiesen angenommene Sachverhalt beruht auf den zwei im Wege des  Bundessozialamtes für Soziales und Behindertenwesen (Sozialministeriumservice) erstellten  Gutachten, den vom Bf. vorgelegten ärztlichem Befund der Stellungskommission Wien vom 1.  Dezember 1980, dem BASB-Gutachten vom 29. September 2009 (primär chronisch  progrediente Multiple Sklerose 100% GdB), dem Bescheid der MA 15 vom 13. November 2006  betreffend Gewährung von Pflegegeld, der Studienzeitbestätigung der Universität Wien vom  28. Juli 2016, dem Befundbericht von Prof. Maida vom 2. März 2009, dem psychiatrischen  Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9, erstellt von Dr. Wolfgang Baischer,  Facharzt für Psychiatrie und Neurologie sowie weiters dem Stellungsuntersuchungsergebnis  des Militärkommando Wien vom 28. August 2013, dem Schreiben der Pensionsversicherung  vom 28. Mai 2013 betreffend Pflegegeld, dem Schreiben des Bezirksgerichtes Donaustadt vom  29. Juli 2013 (Verständigung gemäß § 126 AußStrG), den Arztbriefen der Psychiatrischen  Abteilung des SMZ-Ost betreffend die Aufenthalte des Bf. vom 21. Oktober bis 5. November  2012 und vom 6. bis 9. November 2012.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Missed by this rule (FN):**

- `Universität Wien` (organisation)
- `Prof. Maida` (person)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_166`)


Dr. Wolfgang Baischer diagnostizierte beim Bf. im psychiatrischen Gutachten vom 21. Februar  2013 ein organisches Psychosyndrom bei Encephalitis disseminata (Anm.: multiple Sklerose)  und hielt dazu fest, dass diese degenerative neurologische Erkrankung im Sinne einer  Encephalitis disseminata (Multiple Sklerose) beim Untersuchten seit längerer Zeit bekannt sei.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Mag.a Hilde Heidorn` | `Univ.-Prof.in Mag.a Hilde Heidorn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Floriane Rötker` (person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich` (address)
- `Heinz Neuböck Wthrd GmbH` (organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank in der Beschwerdesache  Leonhard Bianchini, Stixendorf 463, 6361 Glantersberg, Österreich,  über die Beschwerde vom 20.03.2018, eingebracht am 22. März 2018, gegen den Bescheid des  Finanzamtes Klagenfurt vom 16.02.2018, zu Steuernummer 13-665/9571, mittels welchem  der Antrag auf Wiederaufnahme der Verfahren betreffend Einkommensteuer für die Jahre  2012 bis 2015 abgewiesen wurde, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Helga Woschank` | `Dr. Helga Woschank` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Leonhard Bianchini` (person)
- `Stixendorf 463, 6361 Glantersberg, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)
- `13-665/9571` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Heidemarie Lueckemeyer  in der Verwaltungsstrafsache gegen  Amber Demirdöven, Wiedneralm 4, 4906 Feichtet, Österreich, 1.) über die Beschwerde vom 07.09.2020 gegen das Straferkennt- nis des Magistrats der Stadt Wien vom 24.08.2020, zugestellt am 28.08.2020, Gz.  MA67/206700639161/2020, und 2.) über die Beschwerde vom 07.09.2020 gegen das Strafer- kenntnis des Magistrats der Stadt Wien vom 24.08.2020, zugestellt am 28.08.2020, Gz.  MA67/206700639163/2020, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde gegen das Straferkenntnis des Magistrats der Stadt  Wien vom 24.08.2020, Geschäftszahl MA67/206700639161/2020, als unbegründet abgewie- sen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Heidemarie Lueckemeyer` | `Univ.-Prof.in Heidemarie Lueckemeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Amber Demirdöven` (person)
- `Wiedneralm 4, 4906 Feichtet, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)
- `Magistrats der Stadt Wien` (organisation)
- `Magistrats der Stadt  Wien` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anastasia Schraders  in der Beschwerdesache, Svenja Nowakowsky,  Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich, Deutschland, vertreten durch KommR Serge Salameh, Engeltalsiedlung 39, 2093 Kottaun, Österreich, über die  Beschwerde vom 14. Mai 2020 gegen den Bescheid des Finanzamt Amstetten Melk Scheibbs  vom 11. März 2020  betreffend die Erstattung von Vorsteuern für den Zeitraum 01-12/2019 zu Steuernummer  59-077/4638  zu Recht erkannt:  I) Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anastasia Schraders` | `Univ.-Prof.in Anastasia Schraders` |
| `KommR Serge Salameh` | `KommR Serge Salameh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Svenja Nowakowsky` (person)
- `Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich` (address)
- `Engeltalsiedlung 39, 2093 Kottaun, Österreich` (address)
- `Finanzamt Amstetten Melk Scheibbs` (organisation)
- `59-077/4638` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Freilinger` | `Dr. Wolfgang Freilinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Clemens Mooß` (person)
- `Petzelhofstraße 29, 5122 Unterkriebach, Österreich` (address)
- `PROCURA Steuerberatung  GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)
- `62-757/0278` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Simone Zemanek, MSc, Almbachstraße 3, 8673 Filzmoos, Österreich, über die Beschwerde vom 2. April 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 13. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 15-763/9594  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Simone Zemanek, MSc` (person)
- `Almbachstraße 3, 8673 Filzmoos, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `15-763/9594` (tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Charlotte Hirschmueller Silberhumerweg 2, 9163 Bodental, Österreich,  vertreten durch HR Danielle Schochert, Haßreidterstraße 75, 8831 Raiming, Österreich, über die Beschwerde vom  21. Dezember 2018 gegen die Bescheide des FA vom 28. September 2018 betreffend  Wiederaufnahme des Verfahren betreffend Einkommensteuer 2011 bis 2014,  Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014, Steuernummer  46-246/2967, zu Recht erkannt:   I. Die Beschwerden gegen die Bescheide betreffend Wiederaufnahme des Verfahren  betreffend Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014  werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `HR Danielle Schochert` | `HR Danielle Schochert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charlotte Hirschmueller` (person)
- `Silberhumerweg 2, 9163 Bodental, Österreich` (address)
- `Haßreidterstraße 75, 8831 Raiming, Österreich` (address)
- `46-246/2967` (tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Ada Forstner  in der Beschwerdesache des  Elias von Wnuk-Lipinski, Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich, über die Beschwerde vom 13.Mai 2020 (beim Finanzamt  eingelangt am 14.Mai 2020) gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 5. Mai 2020 betreffend  Zurückweisung eines Antrages vom 6.April 2020 auf Wiederaufnahme (§ 303 Abs. 1 BAO) des  Einkommensteuerbescheides 2010 vom 16.Mai 2014 (eingebracht am 7.April 2020 zur  Steuernummer 26-066/9346 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Ada Forstner` | `Univ.-Prof.in Ada Forstner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Elias von Wnuk-Lipinski` (person)
- `Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich` (address)
- `Finanzamt` (organisation)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `26-066/9346` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Caroline Reinwaldt  in der Beschwerdesache Manuel Fortanz,  Zielgerade 30, 4950 Schwaig, Österreich, betreffend die Beschwerde vom 5. Juli 2017 gegen die Bescheide des Finanzamt Gmunden Vöcklabruck  vom 9. Juni 2017 betreffend Umsatz- und Körperschaftsteuer 2010 bis 2015 sowie  Umsatzsteuerfestsetzung für die Zeiträume 01-03/2016, 04-06/201, 07-09/2016 und 10- 12/2016, Steuernummer , beschlossen:  Die Beschwerde wird als gegenstandslos geworden erklärt und das Verfahren eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  iVm Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Caroline Reinwaldt` | `Priv.-Doz.in Caroline Reinwaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Manuel Fortanz` (person)
- `Zielgerade 30, 4950 Schwaig, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Erich Kandler  in der Beschwerdesache Quentin Girharz als  Gruppenmitglied unter der Gruppenträgerin GT über die Beschwerde vom 23. Juni 2020 gegen  die Feststellungsbescheide Gruppenmitglied 2014 bis 2016 des FA Landeck Reutte  vom 25. Februar  2020 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Kandler` | `Mag. Erich Kandler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Quentin Girharz` (person)
- `FA Landeck Reutte` (organisation)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Helga Hochrieser` | `Mag. Helga Hochrieser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wieland Gorecki` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Eugen Burgschweiger, Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 26. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Eugen Burgschweiger` (person)
- `Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Bernarda Egli, Moosenweg 38, 5630 Harbach, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 8. September 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bernarda Egli` (person)
- `Moosenweg 38, 5630 Harbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Unger über die Beschwerde des  Susette Volmari, Carola-Blome-Straße 29, 5203 Spanswag, Österreich  vom 10.12.2020, gegen das Straferkenntnis des Magistrates der  Stadt Wien vom 24.11.2020, MA67/Zahl/2020, betreffend Verwaltungsübertretung nach § 5  Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 in Verbindung  mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der Fassung LGBl.  für Wien Nr. 71/2018, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Dr. Peter Unger` | `Dr. Peter Unger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Susette Volmari` (person)
- `Carola-Blome-Straße 29, 5203 Spanswag, Österreich` (address)
- `Magistrates der  Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Sulamith Hördegen, Witzmannsdorf 4, 3804 Bernschlag, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und  Jugendhilfe, Gasgasse 8-10, 1150 Wien, über die Beschwerde vom 26. August 2020 gegen den  Bescheid des Finanzamtes Österreich vom 11. August 2020 betreffend Abweisung des Antrages  auf Familienbeihilfe 05.2019-07.2020 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sulamith Hördegen` (person)
- `Witzmannsdorf 4, 3804 Bernschlag, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Ing. Ludwig Taspinar, MA` (person)
- `Alt Lenzing 13, 4076 Karling, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ulrich Petrag in der Beschwerdesache  Natalie Nodurft, Saileräckergasse 112, 4676 Augassen, Österreich, vertreten durch Mag. Marion Riezinger, Sonnblickstraße 6, 4614  Marchtrenk, über die Beschwerden vom 15. April 2019 gegen die Bescheide des Finanzamtes  Linz vom 15. März 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis  2017 Steuernummer xxxyyyy zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Ulrich Petrag` | `Mag. Ulrich Petrag` |
| `Mag. Marion Riezinger` | `Mag. Marion Riezinger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Natalie Nodurft` (person)
- `Saileräckergasse 112, 4676 Augassen, Österreich` (address)
- `Finanzamtes  Linz` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Ronald Kulenkampf` | `Mag. Ronald Kulenkampf` |
| `Mag. Monika Schmalzl` | `Mag. Monika Schmalzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `FA Wien 1/23` (organisation)
- `06-334/4335` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |
| `Mag. Thassilo Wedekinn` | `Mag. Thassilo Wedekinn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

| Predicted | Gold |
|---|---|
| `Mag. Peter  Mayerhofer` | `Mag. Peter  Mayerhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nina Rasem` (person)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `Magistrates  der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Techn R Volker Nissle, Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 11. Oktober 2016 betreffend Einkommensteuer 2015 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Volker Nissle` (person)
- `Andreas-Bauer-Gasse 9, 3421 Höflein an der Donau, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck` | `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Felizitas Johanesson` (person)
- `Aspangweg 17, 9781 Gailberg, Österreich` (address)
- `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `48-504/5908` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/132101.1`) (sent_id: `deanon_BFG_20260814_TEST/132101.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Basil Eberhards  in der Beschwerdesache Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich, vertreten durch PhD Nancy Prätor, gegen den am 30. August 2018 von der belangten  Behörde FA Linz, nunmehr Finanzamt Österreich, ausgefertigten Bescheid betreffend  Einkommensteuer für das Jahr 2017 zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Mag. Basil Eberhards` | `Mag. Basil Eberhards` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franz-Hinterholzer-Kai 19, 6145 Oberweg, Österreich` (address)
- `PhD Nancy Prätor` (person)
- `FA Linz` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Pawel Schuwirth  in der Beschwerdesache Griselda Hälmle,  Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich, über die Beschwerde vom 24. Oktober 2018 gegen die Bescheide des  Finanzamtes Landeck Reutte (jetzt Finanzamt Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und 2017, Steuernummer  49-622/1059, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Pawel Schuwirth` | `Hon.-Prof. Pawel Schuwirth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Griselda Hälmle` (person)
- `Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)
- `49-622/1059` (tax_number)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Mag. Regina Vogt` | `Mag. Regina Vogt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Madeleine Göpffarth` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Jaden Mikulla` | `Priv.-Doz.in Jaden Mikulla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ida Gündüz` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |
| `Dr. Sebastian Pfeiffer, LL.M.` | `Dr. Sebastian Pfeiffer, LL.M.` |
| `Dr. Franz Kandlhofer` | `Dr. Franz Kandlhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gerald Cuny-Kreuzer` (person)
- `Christina Tiebout` (person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich` (address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Robert Pernegger` | `Mag. Robert Pernegger` |
| `StR Ing. Alexandra Ebermaier, MBA` | `StR Ing. Alexandra Ebermaier, MBA` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/132474.1`) (sent_id: `deanon_BFG_20260814_TEST/132474.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Violetta Colberg  in der Beschwerdesache KzlR Kurt Bätzgen,  Alte Zeile 11, 4084 Sonnleiten, Österreich, gegen den Bescheid des FAF vom 10. Mai 2013 über die Festsetzung eines  Säumniszuschlages für die Umsatzsteuer 2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dr.in Violetta Colberg` | `Hon.-Prof.in Dr.in Violetta Colberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Kurt Bätzgen` (person)
- `Alte Zeile 11, 4084 Sonnleiten, Österreich` (address)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Gudrun Terzoglou  in der Beschwerdesache Ruprecht Berkenkämper,  Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich ,Land, über die Beschwerde vom 28. August 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 26. Juli 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, Steuernummer 98-086/6338, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Gudrun Terzoglou` | `Hon.-Prof.in Gudrun Terzoglou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ruprecht Berkenkämper` (person)
- `Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `98-086/6338` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Paolo Reppert  in der Beschwerdesache des  Wendelin Pham, Kremstal Bundesstraße 6, 4682 Thalham, Österreich, über die Beschwerden 1.) vom 17.10.2019 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 15.10.2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 sowie  2.) vom 4.5.2020 gegen den Bescheid des Finanzamtes Graz-Stadt vom 3.4.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Paolo Reppert` | `Dr. Paolo Reppert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wendelin Pham` (person)
- `Kremstal Bundesstraße 6, 4682 Thalham, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Mag.a Lukas Dimitrieff` | `Mag.a Lukas Dimitrieff` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juri Marstaller` (person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich` (address)
- `Sonja Wennemann` (person)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-286/5389` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek über die Beschwerde der  Florentin Blatner, Hetzerstraße 11, 4712 Armau, Österreich, vom 18. Jänner 2021, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 67, vom 18. Dezember 2020, Zl. MA67/Zahl/2020, wegen  der Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das angefochtene  Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Mag. Andreas Stanek` | `Mag. Andreas Stanek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentin Blatner` (person)
- `Hetzerstraße 11, 4712 Armau, Österreich` (address)
- `Magistrates  der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt  Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hugo Pietzak  in der Beschwerdesache Dr. Florens Weißer,  Straubingerplatz 57, 4691 Römerberg, Österreich, über die Beschwerden vom 25. November 2020 und 7. Dezember 2020 gegen  die Bescheide des ehemaligen Finanzamtes Wien 1/23 vom 18. November 2020 und 24.  November 2020 betreffend Zurückweisung der Anträge auf Aussetzung der Einhebung vom 22.  März 2020 und 18. August 2020, Steuernummer 09-64-114/4837  zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Hugo Pietzak` | `Priv.-Doz. Hugo Pietzak` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Florens Weißer` (person)
- `Straubingerplatz 57, 4691 Römerberg, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)
- `09-64-114/4837` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerden vom 18. Juni 2017 gegen die Bescheide des  Finanzamtes Bregenz vom 16. Juni 2017 betreffend Einkommensteuer 2015 und 2016  Steuernummer 88-412/8444  beschlossen:   Die Vorlageanträge vom 19.11.2018 gegen die Beschwerdevorentscheidungen vom 10.10.2018  werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Francois Hetkemper` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerde vom 29. Mai 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 17. Mai 2018 betreffend Einkommensteuer 2017, Steuernummer  88-412/8444  zu Recht erkannt:   Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Mag. Armin Treichl` | `Mag. Armin Treichl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Francois Hetkemper` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Merlin Morkam  in der Beschwerdesache des  KzlR Jens Koudela, BSc, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Merlin Morkam` | `Hon.-Prof.in Merlin Morkam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Jens Koudela, BSc` (person)
- `Veitschersiedlung 40, 4048 Puchenau, Österreich` (address)
- `Finanzamt Salzburg-Stadt` (organisation)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/132935.1`) (sent_id: `deanon_BFG_20260814_TEST/132935.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Esra Schlink  in der Beschwerdesache Dipl. Kff. Sibylle Wahlscheid,  Gretlern 168, 3874 Gopprechts, Österreich, vertreten durch Pilz + Rath Steuerberatung, 8200 Gleisdorf, Florianiplatz 12,  über den Vorlageantrag vom 18.06.2013 und über die Beschwerde vom 10.05.2013 gegen die  Bescheide des Finanzamtes Bruck Eisenstadt Oberwart vom 12.03.2013 über die Wiederauf- nahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2011  und Einkommensteuer (Arbeitnehmerveranlagung) 2009 bis 2012 beschlossen und entschie- den:    I. Der Vorlageantrag vom 18.06.2013 wird insoweit als nicht zulässig zurückgewiesen, als mit  ihm die Wiederaufnahme der Verfahren betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2009 bis 2011 angefochten sind.

| Predicted | Gold |
|---|---|
| `Dipl. Kff. Sibylle Wahlscheid` | `Dipl. Kff. Sibylle Wahlscheid` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Esra Schlink` (person)
- `Gretlern 168, 3874 Gopprechts, Österreich` (address)
- `Pilz + Rath Steuerberatung` (organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Univ.-Prof. Kai Menrath` | `Univ.-Prof. Univ.-Prof. Kai Menrath` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wigand Maczkiewicz, Bakk. art.` (person)
- `Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich` (address)
- `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `49-963/8463` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |
| `Mag. Sven Weichmann` | `Mag. Sven Weichmann` |
| `Mag. Kurt Kreith` | `Mag. Kurt Kreith` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich` (address)
- `Finanzamtes Baden  Mödling` (organisation)
- `78-738/0573` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_4`)


Die Beschwerdeführerin (Bf.) Dr. Judith Glazer wurde mit Bescheid des Finanzamtes Baden  Mödling vom 20.08.2020 zur Einkommensteuer 2018 veranlagt.

| Predicted | Gold |
|---|---|
| `Dr. Judith Glazer` | `Dr. Judith Glazer` |

**Missed by this rule (FN):**

- `Finanzamtes Baden  Mödling` (organisation)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Richard Schwanken  in der Beschwerdesache Alexandra Hettrich,  Kohleggweg 268, 4621 Schnarrndorf, Österreich, über die Beschwerde vom 3. Oktober 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Lilienfeld St. Pölten) vom 28. August 2020  betreffend die Abweisung einer Nachsicht von Abgabenschuldigkeiten, Steuernummer  86-148/2619, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Richard Schwanken` | `Priv.-Doz. Richard Schwanken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alexandra Hettrich` (person)
- `Kohleggweg 268, 4621 Schnarrndorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Lilienfeld St. Pölten` (organisation)
- `86-148/2619` (tax_number)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Peter Bilger` | `Mag. Peter Bilger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `VetR Dipl. Kff. Ingrid Klockgiesser` (person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Mag.a Heidrun Eifeler` | `Univ.-Prof.in Mag.a Heidrun Eifeler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Esra Luetje` (person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich` (address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/133922.1`) (sent_id: `deanon_BFG_20260814_TEST/133922.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die vorsitzende Richterin Mag. Aloisia Bergauer und die  beisitzende Richterin Mag. Andrea Ebner sowie die fachkundigen Laienrichter Mag. Johannes  Denk und Friedrich Nagl in der Beschwerdesache Dipl. Kfm. Rüdiger Schäffler, Anton-Dengler-Gasse 16, 8330 Krennach, Österreich, vertreten durch  BONAFIDE Treuhand- und Revisionsgesellschaft m.b.H., Berggasse 10, 1090 Wien, über die  Beschwerde vom 17. Oktober 2011 gegen die Bescheide des Finanzamtes Wien 12/13/14  Purkersdorf vom 11. Oktober 2011 betreffend Einkommensteuer für die Jahre 2006 bis 2009  nach Durchführung einer mündlichen Verhandlung beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Aloisia Bergauer` | `Mag. Aloisia Bergauer` |
| `Mag. Andrea Ebner` | `Mag. Andrea Ebner` |
| `Mag. Johannes  Denk` | `Mag. Johannes  Denk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Friedrich Nagl` (person)
- `Dipl. Kfm. Rüdiger Schäffler` (person)
- `Anton-Dengler-Gasse 16, 8330 Krennach, Österreich` (address)
- `Finanzamtes Wien 12/13/14  Purkersdorf` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache Sven Hoerlin, Padasterjochhaus 6, 9562 Tobitsch, Österreich, gegen den Bescheid  des Finanzamtes Spittal  Villach vom 17. November 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013 Steuernummer 51-093/9549  folgenden Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Mag. Heidemarie Winkler` | `Mag. Heidemarie Winkler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sven Hoerlin` (person)
- `Padasterjochhaus 6, 9562 Tobitsch, Österreich` (address)
- `Finanzamtes Spittal  Villach` (organisation)
- `51-093/9549` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/133923.1`) (sent_id: `deanon_BFG_20260814_TEST/133923.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Eckard Eizenhammer  in der Beschwerdesache KommR Ashley Tönisen,  Filzbergweg 63, 4924 Födering, Österreich, betreffend die Beschwerde vom 5. August 2011 gegen die Bescheide des  Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) datiert mit 22. Februar 2011  betreffend Haftung und Zahlung von Lohnsteuer sowie Festsetzung des Dienstgeberbeitrages  zum Ausgleichsfonds für Familienbeihilfen und Zuschlag zu diesem Beitrag, jeweils für die Jahre  2005 bis 2007, Steuernummer 16-543/4492,  beschlossen:    I.  Die Beschwerde wird gemäß § 260 Abs 1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Eckard Eizenhammer` | `Priv.-Doz. Eckard Eizenhammer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Ashley Tönisen` (person)
- `Filzbergweg 63, 4924 Födering, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `16-543/4492` (tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  Aloisa Antoni, Wassermanngasse 9, 4840 Vöcklabruck, Österreich  vertreten durch die Steuerfilter Steuerberatungs-GmbH,  Ischlerbahnstraße 23, 5301 Eugendorf, über die Beschwerde vom 11. Juni 2019 und 9. Oktober  2019 gegen die Bescheide des Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich)  vom 16. Mai 2019 und 2. Oktober 2019 betreffend die Wiederaufnahme der  Einkommensteuerverfahren 2013 bis 2015 zu Recht erkannt:  I)  Die Wiederaufnahmebescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Erich Schwaiger` | `Mag. Erich Schwaiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Aloisa Antoni` (person)
- `Wassermanngasse 9, 4840 Vöcklabruck, Österreich` (address)
- `Steuerfilter Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Juliana Untermeier, C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt, Schwefel  93/7, 6850 Dornbirn, über die Beschwerde vom 16. Mai 2013 gegen den Bescheid des  Finanzamtes Bregenz vom 10. April 2013 betreffend Haftung gemäß § 9 iVm § 80  Bundesabgabenordnung (BAO), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |
| `Dr. Christoph Ganahl` | `Dr. Christoph Ganahl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juliana Untermeier` (person)
- `C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Elina Hetcamp  in der Beschwerdesache Florentine Mugge,  Rodlhütte 36, 9782 Plone, Österreich, über die Beschwerde vom 5. April 2013 gegen die Bescheide des FA Kufstein  Schwaz (nunmehr Finanzamt Österreich) vom 22. März 2013, Str. Nr. 59-679/2034,  betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Februar 2012      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp` | `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Florentine Mugge` (person)
- `Rodlhütte 36, 9782 Plone, Österreich` (address)
- `FA Kufstein  Schwaz` (organisation)
- `Finanzamt Österreich` (organisation)
- `59-679/2034` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  Leopold Pichlbauer in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

| Predicted | Gold |
|---|---|
| `Mag. Marco Laudacher` | `Mag. Marco Laudacher` |
| `Mag. Susanne Haim` | `Mag. Susanne Haim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag Stefan Raab` (person)
- `Leopold Pichlbauer` (person)
- `Bettina Domigall, Bakk. iur.` (person)
- `Zickhöhe 66, 3361 Biberbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Tanja Grottenthaler` (person)

**Example 90** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Dr. Ashley Nagelschmidt, Hollenbach 37, 4872 Unterthumberg, Österreich, vertreten durch APP Steuerberatung GmbH,  Waidmannsdorfer Straße 10, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom  24. November 2016 gegen die Haftungs- und Abgabenbescheide gemäß § 99 Abs. 1 EStG 1988  betreffend Einkommensteuer (Abzugsteuer) für die Jahre 2013 bis 2015 des Finanzamtes für  Großbetriebe (nunmehr Finanzamt für Großbetriebe) vom 24. Oktober 2016, Steuernummer  16-165/9893  zu Recht:   Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |
| `Dr. Ashley Nagelschmidt` | `Dr. Ashley Nagelschmidt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hollenbach 37, 4872 Unterthumberg, Österreich` (address)
- `APP Steuerberatung GmbH` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `16-165/9893` (tax_number)

**Example 91** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

| Predicted | Gold |
|---|---|
| `Mag. Wolfgang Moser` | `Mag. Wolfgang Moser` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Petra Port` (person)
- `Konventweg 36, 4613 Unterholz, Österreich` (address)
- `Burka Vitek Moser  Rechtsanwälte` (organisation)
- `Finanzamt Wien  9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Petra Port` (person)

**Example 92** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Wladimir Beheim  in der Beschwerdesache Bruno Rüttgers,  Krumpendorfer Straße 43, 3873 Gopprechts, Österreich, vertreten durch Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG,  Kirchengasse 4, 8680 Mürzzuschlag, betreffend Beschwerde vom 2. November 2006 gegen den  Bescheid des FA Klagenfurt St. Veit Wolfsberg  vom 29. September 2006 betreffend Festsetzung von Anspruchszinsen  beschlossen:   Der Bescheid betreffend Festsetzung von Anspruchszinsen 2001 scheidet aus dem  Rechtsbestand aus.

| Predicted | Gold |
|---|---|
| `Mag. Wladimir Beheim` | `Mag. Wladimir Beheim` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bruno Rüttgers` (person)
- `Krumpendorfer Straße 43, 3873 Gopprechts, Österreich` (address)
- `Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG` (organisation)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 93** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Sieglinde Steinkaemper  in der Beschwerdesache Julian Gruening,  Litzldorfer-Gasse 83, 4893 Harpoint, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, und GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Handelskai 92, Gate 2, 7A, 1200 Wien, über die   1.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Dr.in Sieglinde Steinkaemper` | `Hon.-Prof.in Dr.in Sieglinde Steinkaemper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Julian Gruening` (person)
- `Litzldorfer-Gasse 83, 4893 Harpoint, Österreich` (address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)
- `GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)

**Example 94** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Babette Bernett, Schmalzhofen 9, 8250 Riegersbach, Österreich, über die Beschwerde vom 17. September 2020 gegen den  Bescheid des Finanzamtes Kufstein Schwaz (nunmehr Finanzamt Österreich) vom 4. September  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerdevorentscheidung vom 24. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 wird gemäß § 279 Abs. 1 BAO ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Babette Bernett` (person)
- `Schmalzhofen 9, 8250 Riegersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_215`)


Wenn der Sachwalter die Einvernahme von Prof. Maida als Zeugin beantragt, so erachtet das  Bundesfinanzgericht eine derartige Einvernahme als nicht zielführend, da der Bf. erstmals bei  der Neurologin Univ.Prof. Dr. Eva Maria Maida im Jahr 2006 wegen seiner Erkrankung  (Multiple Sklerose) in Behandlung war und diese somit über den Gesundheitszustand des Bf.  für einen Zeitraum, der ca. 30 Jahre zurückliegt, naturgemäß nur Vermutungen anstellen kann.

**False Positives:**

- `Dr. Eva Maria Maida` — partial — pred is substring of gold: `Neurologin Univ.Prof. Dr. Eva Maria Maida`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Maida`(person)
- `Bundesfinanzgericht`(organisation)
- `Neurologin Univ.Prof. Dr. Eva Maria Maida`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Sawadzki, Bakk. art.`(person)
- `Weintraubengasse 36, 9073 Aich, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

**False Positives:**

- `KommR Ing. Ludwig Taspinar` — partial — pred is substring of gold: `KommR Ing. Ludwig Taspinar, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `KommR Ing. Ludwig Taspinar, MA`(person)
- `Alt Lenzing 13, 4076 Karling, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`
- `Dr. Thomas Keppert` — partial — pred is substring of gold: `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/132622.1`) (sent_id: `deanon_BFG_20260814_TEST/132622.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache RgR VetR Cassandra Sczech, Hainbuchen 119, 3423 Wördern, Österreich, betreffend Beschwerde vom 22. September 2020 gegen die Bescheide  2015/2016/2017/2018 des Finanzamtes Gänserndorf Mistelbach beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `VetR Cassandra Sczech` — partial — pred is substring of gold: `RgR VetR Cassandra Sczech`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `RgR VetR Cassandra Sczech`(person)
- `Hainbuchen 119, 3423 Wördern, Österreich`(address)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Romana Stavrakis, Untersameting 4, 4894 Römerhof, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 04. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 28. April  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 nach Durchführung einer  öffentlichen mündlichen Verhandlung am 07.04.2021 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Ulrike Nussbaumer` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Romana Stavrakis`(person)
- `Untersameting 4, 4894 Römerhof, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  VetR Dipl. Kff. Ingrid Klockgiesser, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

**False Positives:**

- `Dipl. Kff. Ingrid Klockgiesser` — partial — pred is substring of gold: `VetR Dipl. Kff. Ingrid Klockgiesser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Peter Bilger`(person)
- `VetR Dipl. Kff. Ingrid Klockgiesser`(person)
- `Etschmayerstraße 4, 4720 Baumgarten, Österreich`(address)
- `Finanzamtes`(organisation)

</details>

---

## `Representative Context` 🏆

**F1:** 0.016 | **Precision:** 0.812 | **Recall:** 0.008  

**Format:** `regex`  
**Rule ID:** `f0ec9a87`  
**Description:**
Captures names of representatives mentioned after 'vertreten durch', strictly requiring a title or full name pattern and excluding generic terms.

**Content:**
```
(?:vertreten durch)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z][a-z]+(?:gmbH|KG|AG)|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.812 | 0.008 | 0.016 | 16 | 13 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 13 | 3 | 1601 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Martin Friedl` | `Martin Friedl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Babette Nimzyk` (person)
- `Tamara Poertgen, LLB Bakk. techn.` (person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich` (address)
- `Finanzamtes` (organisation)
- `08-216/2001` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache Cornelia Özgür,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch Thomas Krampl, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Thomas Krampl` | `Thomas Krampl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Fabienne Kattner` (person)
- `Cornelia Özgür` (person)
- `Hofbauer-Straße 6, 9854 Krainberg, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Sonja Wennemann` | `Sonja Wennemann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Lukas Dimitrieff` (person)
- `Juri Marstaller` (person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich` (address)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-286/5389` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Christina Hildegard Stowasser` | `Christina Hildegard Stowasser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Wieland Starnberg` (person)
- `Ing. Linus Feyerherdt` (person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich` (address)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `Finanzamtes Österreich` (organisation)
- `98-011/6615` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Prof. Leander Pfleumer, LLM, Am Gewerbepark 6, 9065 Niederdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 11. November 2020 gegen den Bescheid  des Finanzamtes Linz (nunmehr Finanzamtes Österreich ) vom 22. Oktober 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 11-306/0925  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alfred Klaus Fenzl` | `Alfred Klaus Fenzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Walter Aiglsdorfer` (person)
- `Prof. Leander Pfleumer, LLM` (person)
- `Am Gewerbepark 6, 9065 Niederdorf, Österreich` (address)
- `Finanzamtes Linz` (organisation)
- `Finanzamtes Österreich` (organisation)
- `11-306/0925` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/137369.1`) (sent_id: `deanon_BFG_20260814_TEST/137369.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Delila Holsträter, Bakk. iur. BEd, Ziegelsdorf 25, 4723 Unterhörzing, Österreich, vertreten durch Harald Andreas Rumpler, Mattersburgerstraße 70, 7022 Schattendorf,  über die Beschwerde vom 24. September 2018 gegen den Bescheid des Finanzamtes  Österreich vom 22. August 2018 betreffend Einkommensteuer 2016 Steuernummer  76-140/9765  zu Recht erkannt:   Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Harald Andreas Rumpler` | `Harald Andreas Rumpler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Delila Holsträter, Bakk. iur. BEd` (person)
- `Ziegelsdorf 25, 4723 Unterhörzing, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `76-140/9765` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Christine Kralova  in der Beschwerdesache Merlin Leuprecht,  Ketten 21, 4061 Aistental, Österreich, vertreten durch Anton Fleischhacker, Goldeggasse 3/7, 1040 Wien, über die  Beschwerde vom 5. Februar 2018 gegen den Bescheid des Magistrats der Stadt Wien,  Magistratssabteilung 6,Rechnungs- und Abgabenwesen, Dezernat Abgaben und Recht, Referat  Landes- und Gemeindeabgaben vom 10. Jänner 2018 betreffend Zurückweisung eines Antrages  auf Festsetzung der Vergnügungssteuer für den Zeitraum 2012 bis 2015 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Anton Fleischhacker` | `Anton Fleischhacker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Christine Kralova` (person)
- `Merlin Leuprecht` (person)
- `Ketten 21, 4061 Aistental, Österreich` (address)
- `Magistrats der Stadt Wien` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Walther Kendler` | `Walther Kendler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Brendon Spade` (person)
- `OMedR Milena Piechulik` (person)
- `Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich` (address)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `16-827/1246` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/142114.1`) (sent_id: `deanon_BFG_20260814_TEST/142114.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Gerhard Konrad in der Beschwerdesache  Flora Tahir, Sommeregg 24, 9634 Oberbuchach, Österreich, vertreten durch Renate Dolezal, Speisinger Str 50-52 Tür 18, 1130  Wien, über die Beschwerde vom 5. Oktober 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. September 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016, Steuernummer 20-636/7581, beschlossen:  I. Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Renate Dolezal` | `Renate Dolezal` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Konrad` (person)
- `Flora Tahir` (person)
- `Sommeregg 24, 9634 Oberbuchach, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `20-636/7581` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/147296.1`) (sent_id: `deanon_BFG_20260814_TEST/147296.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Erwin Nikolasen  in der Beschwerdesache Doris Weierstahl,  Minibandlweg 18, 9473 Wunderstätten, Österreich, vertreten durch Kirstin Ever, Minibandlweg 18, 9473 Wunderstätten, Österreich, über die Beschwerde vom  21. Mai 2019 gegen den Bescheid des Finanzamtes Salzburg-Land (nun Finanzamt Österreich)  vom 9. Mai 2019 betreffend Säumniszuschlag 2018, Steuernummer 57-656/9365, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kirstin Ever` | `Kirstin Ever` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Erwin Nikolasen` (person)
- `Doris Weierstahl` (person)
- `Minibandlweg 18, 9473 Wunderstätten, Österreich` (address)
- `Minibandlweg 18, 9473 Wunderstätten, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)
- `57-656/9365` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_51`)


Daraus folgt, dass der Einspruch gegen die Strafverfügung vom 3. September 2024 des M,  vertreten durch Pjotr Niessl, wieder unerledigt ist und die belangte Behörde darüber zu  entscheiden hat.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/148979.1`) (sent_id: `deanon_BFG_20260814_TEST/148979.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Janosch Postema  in der Beschwerdesache Juri Gübele,  Gartnerweg 4, 5145 Eisenhub, Österreich, vertreten durch Lydia Alberth, Steuerberaterin, Am Hochsteg 13, 8434  Tillmitsch, betreffend die Beschwerde vom 23.4.2025 gegen den Bescheid des Finanzamtes  Österreich vom 28.1.2025 betreffend Festsetzung einer Zwangsstrafe gemäß § 16 WiEReG iVm  § 111 BAO in Höhe von 1.000,00 Euro beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Lydia Alberth` | `Lydia Alberth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Janosch Postema` (person)
- `Juri Gübele` (person)
- `Gartnerweg 4, 5145 Eisenhub, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/149201.1`) (sent_id: `deanon_BFG_20260814_TEST/149201.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Sven Pertsch  in der Beschwerdesache Hugo Ossiander,  Streit 58, 5204 Hochfeld, Österreich, vertreten durch Vlado Jovic, Meilstraße 7 Tür 5, 6170 Zirl, betreffend  Beschwerde vom 19. November 2024 gegen den Bescheid des Finanzamt Linz  vom 26. September  2024 betreffend Feststellung der Einkünfte § 188 BAO 2023, Steuernummer 75-331/1938,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO iVm. § 278 Abs. 1 lit a BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vlado Jovic` | `Vlado Jovic` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Sven Pertsch` (person)
- `Hugo Ossiander` (person)
- `Streit 58, 5204 Hochfeld, Österreich` (address)
- `Finanzamt Linz` (organisation)
- `75-331/1938` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/143628.1`) (sent_id: `deanon_BFG_20260814_TEST/143628.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Jaroslaw Hoecker  in der Beschwerdesache Valerius Sülzbrück,  Mariazellerstraße 82, 4210 Unterweitrag, Österreich  nunmehr vertreten durch Steuerberaterin Danielle Tafelmeir, Andelberggasse 58, 4760 Niederham, Österreich, über die  Beschwerde vom 5. Oktober 2017 (Postaufgabetag) gegen den Bescheid des ehemaligen  Finanzamtes Wien 12/13/14 Purkersdorf vom 19. September 2017 betreffend Abweisung eines  Zahlungserleichterungsansuchens, Steuernummer 26-264/5699, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberaterin Danielle Tafelmeir` — partial — gold is substring of pred: `Danielle Tafelmeir`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Jaroslaw Hoecker`(person)
- `Valerius Sülzbrück`(person)
- `Mariazellerstraße 82, 4210 Unterweitrag, Österreich`(address)
- `Danielle Tafelmeir`(person)
- `Andelberggasse 58, 4760 Niederham, Österreich`(address)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `26-264/5699`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/143769.1`) (sent_id: `deanon_BFG_20260814_TEST/143769.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Elena Sladek, Metnitztalweg 11, 9572 Gantschach, Österreich, vertreten durch Steuerberaterin Allegra Paulenz, Dornblüthstraße 2, 01277 Dresden,  über die Beschwerde vom 20. Juli 2020 gegen den Bescheid des Finanzamtes Österreich vom  22. Juni 2020 betreffend Feststellungsbescheid über die Nichtveranlagung zur Umsatzsteuer  2019 Steuernummer 61-618/5776  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Steuerberaterin Allegra Paulenz` — partial — gold is substring of pred: `Allegra Paulenz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Elena Sladek`(person)
- `Metnitztalweg 11, 9572 Gantschach, Österreich`(address)
- `Allegra Paulenz`(person)
- `Finanzamtes Österreich`(organisation)
- `61-618/5776`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/148995.1`) (sent_id: `deanon_BFG_20260814_TEST/148995.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Nicola Fedrich, Fresachergasse 7, 5142 Unterhaunsberg, Österreich  vertreten durch Name Erwachsenenvertreter,  Adresse, (gerichtlicher Erwachsenenvertreter) betreffend die Beschwerde vom 9. Jänner 2023  gegen den Bescheid des Finanzamtes Österreich vom 16. Dezember 2022 betreffend  Aufforderung zur Einreichung von Abgabenerklärungen für das Jahr 2021 zu Steuernummer  54-293/0065  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Name Erwachsenenvertreter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Johann Fischerlehner`(person)
- `Nicola Fedrich`(person)
- `Fresachergasse 7, 5142 Unterhaunsberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `54-293/0065`(tax_number)

</details>

---

## `Herr Name Context` 🏆

**F1:** 0.041 | **Precision:** 0.756 | **Recall:** 0.021  

**Format:** `regex`  
**Rule ID:** `1c0bac7e`  
**Description:**
Captures names following 'Herr' or 'des Herrn', ensuring the name is followed by a space, punctuation, or end of string, but NOT by another capitalized word (to avoid 'Hus Es').

**Content:**
```
(?:des Herrn|Herr)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.756 | 0.021 | 0.041 | 45 | 34 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 34 | 11 | 1580 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_40`)


Sie werden daher unter Hinweis auf Ihre Mitwirkungspﬂicht im Verwaltungsstrafverfahren,  binnen zwei Wochen ab Zustellung dieses Schreibens, aufgefordert, bekannt zu geben, wie  lange sich Herr Vera Schliephacke in Wien aufgehalten, wo er gewohnt hat und zu welchem Zweck  ihm das verfahrensgegenständliche Fahrzeug überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_108`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 01/2006  Herr Heinz Herper  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:    Die Unfähigkeit sich selbst den Unterhalt zu verschaffen ist ab 1/2006 belegbar da ab diesem  Zeitpunkt höhergradige körperliche Beeinträchtigungen vorhanden sind;

| Predicted | Gold |
|---|---|
| `Heinz Herper` | `Heinz Herper` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_6`)


Weiters heißt es darin: „Da Herr Stavrakis im  Steuerjahr 2014 noch als in Österreich unbeschränkt Steuerpflichtiger eine Erklärung zur  Arbeitnehmerveranlagung (L1) einreichen wird, ersuchen wir Sie die unbeschränkte  Steuernummer von Herrn Stavrakis erst ab abgeschlossener Veranlagung 2014 auf eine  Steuernummer bei beschränkter Steuerpflicht abzuändern.“

| Predicted | Gold |
|---|---|
| `Stavrakis` | `Stavrakis` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_51`)


Daher ersuchen wir um Berücksichtigung der Befreiung von der ImmoESt für Herrn Lisa Lindnau,  da im gegenständlichen Tauschverhältnis nur der Rechtserwerb des Herrn Lisa Lindnau  die  Voraussetzungen eines Flurbereinigungsverfahrens erfüllt und dergestalt einen  anderslautenden Bescheid nach sich gezogen hätte.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_5`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Organ des ehemaligen Finanzamtes Waldviertel als Finanzstrafbehörde vom 12. November  2020, SpS, Strafnummer, wurde Herr Petra Port, geb. am 1980, schuldig erkannt, er habe im  1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_22`)


Herr Bodewein brachte mit E-Mail vom 15. September 2021 unter Angabe der GZ. MA67/Zahl1/2020  folgende Eingabe beim Magistrat der Stadt Wien ein:  „ich habe eine Mahnung bekommen, dass nicht weiß, wann und wo ich bestraft wurde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_25`)


Der Magistrat der Stadt Wien ersuchte Herrn Bodewein um Bekanntgabe seiner Telefonnummer  zwecks Klärung des Sachverhaltes, was Herr Bodewein mit E-Mail vom 29. September 2021  beantwortete.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_31`)


Herr Bodewein müsste gemäß § 14 Abs. 2 Satz 2  VwGVG in der Fassung BGBl. I 109/2021 eine Mitteilung des Magistrates der Stadt Wien über  die Vorlage der (vermeintlichen) Beschwerde an das BFG erhalten haben.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `BFG` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_34`)


Das Anbringen, welches Herr Bodewein per E-Mail am 15. September 2021 beim Magistrat der Stadt  Wien eingebracht hat, ist keine Beschwerde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_14`)


Herr Julia Reittinger  ist voraussichtlich dauernd außerstande sich selbst den Unterhalt zu  verschaffen: NEIN

| Predicted | Gold |
|---|---|
| `Julia Reittinger` | `Julia Reittinger` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_5`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  10. November 2022, Zahl: MA67/226701238674/2022, wurde Herr Katharina Bauckholt (in weiterer  Folge: Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Katharina Bauckholt` | `Katharina Bauckholt` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_38`)


Mit Aktenvermerk vom 20. April 2023 hielt die Magistratsabteilung 67 zur gegenständlichen  Geschäftszahl fest, ein Telefonat mit PÜG Dienstführung 1,Herr Mayerer (DW TelNr) habe  ergeben, das Überwachungsorgan DNr. ANr habe am Beanstandungstag (10.11.2022) im 22.

| Predicted | Gold |
|---|---|
| `Mayerer` | `Mayerer` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_5`)


Mit Strafverfügung des Magistrates der Stadt Wien vom 29. November 2021, Zahl:  MA67/XX/2021, wurde Herr Istvan  Melniczenko (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Istvan  Melniczenko` | `Istvan  Melniczenko` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_4`)


Dass der Geschäftsführer der GmbH, Herr Nadine Millradt, dies bestreite, sei ihm bekannt und  derzeit Gegenstand mehrerer Verfahren.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_7`)


Herr Nadine Millradt  schulde ihm noch ausstehende Gehälter.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_12`)


Sollte Herr Nadine Millradt  die Vorsteuer zum Abzug gebracht haben, müsse sie von ihm zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_24`)


In der Begründung wird dazu ausgeführt:  „Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 8,4 Liter  Alkohol unter Abfindung, wobei diese Menge als "Hausbrand" steuerfrei belassen werden  sollte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_25`)


Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 15 Liter  Alkohol unter Abfindung, wobei diese Mengen als "Hausbrand" ebenfalls steuerfrei belassen  werden sollte.“

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_29`)


Und weiter: „[…]  hätte Herr Quentin Schwartkopp  diese Freimengen nicht beanspruchen dürfen, da der Sohn bereits seit  03.bbb.2013 nicht im gemeinsamen Haushalt mit Herrn Quentin Schwartkopp  lebte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_33`)


In der Begründung wurde ausgeführt: „Nach dem Auszug "Abfrage  Abfindungsberechtigte/Person" vom 31.08.2018 des Zollamtes Innsbruck war Herr Quentin Schwartkopp  jedenfalls als Abfindungsberechtigter ausgewiesen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_34`)


Im Rahmen des Ermittlungsverfahrens wurde festgestellt, dass Herr Quentin Schwartkopp, belegt durch  den Übergabevertrag, GZ xxx vom 17.mt.2011 — mit Wirkung vom 01.mt.2011 — das  landwirtschaftliche Anwesen in Betriebssitz, an seinen Sohn Sohn, übergeben hat.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_37`)


Mit Schreiben des Zollamtes Innsbruck vom 14.01.2019, GZ 800000/thrhtr, wurde Herr  Quentin Schwartkopp  zur Abgabe einer Stellungnahme gemäß § 115 BAO eingeladen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_38`)


Mit Schreiben vom  29.01.2019 gab Herr Quentin Schwartkopp  an, dass er nach Übergabe seines Hofes an seinen Sohn Sohn  mit diesem mündlich vereinbart habe, dass er die Obstveredelung weiterhin als  Fruchtgenussberechtigter betreiben dürfe.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_41`)


Überdies hätte Herr Quentin Schwartkopp  auch  vor der Übertragung des land- und forstwirtschaftlichen Betriebes die Freimenge für Herrn  3 von 8 Seite 4 von 8

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_142`)


Soweit der Bf. darauf verweist, dass Herr Abersfeller aus Gewerbebetrieb  erzielt bzw bei der SVA pflichtversichert sei, mag zwar richtig sein, ist aber bedeutungslos:  Aufgrund des funktionalen Verständnisses des Begriffes der Eingliederung gemäß der zitierten  Judikatur des VwGH ist es ohne Bedeutung, in welcher Weise die aus der Tätigkeit erzielten  Einkünfte zu qualifizieren wären;

| Predicted | Gold |
|---|---|
| `Abersfeller` | `Abersfeller` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_4`)


Begründung  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung Bereich Finanzstrafsachen  Team 6 als Finanzstrafbehörde vom 9. Oktober 2023, SpS-1, wurden  I. Herr Dieter Avemaria, geboren 1980, schuldig erkannt, er habe als Komplementär und  abgabenrechtlich Verantwortlicher der Engelbert Schefe  vorsätzlich  A. unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspflicht  eine Verkürzung an  Umsatzsteuer 2017 von € 3.609,08  Umsatzsteuer 2019 von € 23.455,92  Umsatzsteuer 2020 von € 2.187,78   1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Amt für Betrugsbekämpfung` (organisation)
- `Engelbert Schefe` (person)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_34`)


Herr Corvin Billmaier  hat die Ausgaben getragen und bezahlt und Ausgaben sind bei jenem  abzugsfähig, der sie bezahlt hat und nicht bei jenem, den sie betroffen hätten.

| Predicted | Gold |
|---|---|
| `Corvin Billmaier` | `Corvin Billmaier` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_38`)


Sie sehen im Anhang dass Herr Abeles damit bis 27 Dezember  gefahren ist.

| Predicted | Gold |
|---|---|
| `Abeles` | `Abeles` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_41`)


Der Beschwerde waren zahlreiche Unterlagen zum Beweis dafür beigelegt, dass der Bf. nie mit  dem Kraftfahrzeug mit dem behördlichen Kennzeichen 123 gefahren sei und dass Herr Abeles bis  27. Dezember 2023 gefahren sei (bzw. an diesem Tag das Leasing Auto zurückgegeben habe).

| Predicted | Gold |
|---|---|
| `Abeles` | `Abeles` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_8`)


Mit an die Magistratsabteilung 67 gesendeter E-Mail vom 12. Juni 2024 erstattete Herr  Jeanne Pavlovitsch (in der Folge: Beschwerdeführer) eine von der belangten Behörde als Einspruch  gegen die Strafverfügung vom 4. Juni 2024 gewertete Eingabe.

| Predicted | Gold |
|---|---|
| `Jeanne Pavlovitsch` | `Jeanne Pavlovitsch` |

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_14`)


Herr Kaspar Sadowski  führt ab 1.1.2018 den Betrieb „Unternehmensberatung" - der zuvor von der **  GMBH geführt wurde - nun mehr als Einzelunternehmung Kaspar Sadowski  weiter.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_20`)


Da Herr Kaspar Sadowski  immer  Alleingesellschafter der ** GMBH war, ist der Übergang des Verlustvortrages mit 100 %  vorzunehmen.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_17`)


Herr Bf benützt für seine Wochenendfahrten nach A1 einen anderen Pkw.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_18`)


Herr Bf-Gatte ist während der Woche in D-XY whft und in A1 nicht gemeldet;

**False Positives:**

- `Bf-Gatte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)


- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau Basyurt tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau Basyurt das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

**False Positives:**

- `Bf-Gatte` — no gold match — likely missing annotation
- `Bf-Gatte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Basyurt`(person)
- `Basyurt`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_122`)


Herr Bf ist im Wesentlichen in der Lage, einfache Sachverhalte zu erfassen, zeigt sich bei  komplexeren Anforderungen allerdings überfordert.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Quentin Schwartkopp`(person)
- `Zollamt`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_36`)


Herr Sohn wurde zwischenzeitlich gemäß § 62 AlKStG als Abfindungsberechtigter  registriert.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_40`)


Unter Hinweis auf §§ 2 Abs. 1, 4 Abs. 2 Z 5, 8 Abs. 1 Z 2, § 9 Abs. 1 Ziffer 2, § 62 Abs. 2 Z 3, 64  Abs. 3 AlkStG betonte das Zollamt, dass durch den Übergabevertrag vom eee2011 Herr Sohn  unzweifelhaft Eigentümer an den Früchten (= alkoholbildende Stoffe) wurde; auf mündliche  Absprachen zwischen Vater und Sohn komme es nicht an.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_81`)


Herr Sohn hat seit 03.bbb.2013 seinen aktuellen  ordentlichen Wohnsitz (Hauptwohnsitz) in Adresse_Sohn.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_88`)


Wie das Zollamt auch zu diesem Beschwerdepunkt ausführlichst und zu Recht betont hat,  wurde mit der Übergabe im Jahr 2011 der Übernehmer der Liegenschaft, Herr Sohn, auch  Eigentümer an den darauf befindlichen Obstbäumen und an deren Früchte.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_289`)


Zum Beweisantrag:  Herr Baumeister Y X war von 3. Oktober 2013 bis 7. November 2016 gewerberechtlicher  Geschäftsführer der e GmbH (vgl. BFG-Akt I Bl. 56b).

**False Positives:**

- `Baumeister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

</details>

---

## `Standalone Name in Complaint Context Refined` 🏆

**F1:** 0.174 | **Precision:** 0.454 | **Recall:** 0.108  

**Format:** `regex`  
**Rule ID:** `4a2abaac`  
**Description:**
Captures full names appearing after 'in der Beschwerdesache' or 'des/der' when no title is present, strictly excluding generic terms like 'Stadt', 'Bf', 'Beschuldigten', and addresses.

**Content:**
```
(?:in der Beschwerdesache|des|der)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z][a-z]+(?:gmbH|KG|AG)|$)(?!.*(?:Stadt.*Wien|Beschuldigten|Bf.*[,:]|Beschwerdeführerin))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.454 | 0.108 | 0.174 | 383 | 174 | 209 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 174 | 209 | 1440 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Waltraud Hinterlandt` | `Waltraud Hinterlandt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Günter Lehwaldt` (person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich` (address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Saphira Blazejewicz  in der Beschwerdesache des  Jeanne Weiermann, Versorgungshausstraße 5, 4963 Hagenau, Österreich, vertreten durch DSG - WirtschaftstreuhandgmbH, Heinrichstraße  97, 8010 Graz, über die Beschwerde vom 28.Okt.2015, beim Finanzamt X eingelangt am  2. November 2015 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 29. September 2015 betreffend  Einkommensteuer 2013 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Jeanne Weiermann` | `Jeanne Weiermann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Priv.-Doz.in Saphira Blazejewicz` (person)
- `Versorgungshausstraße 5, 4963 Hagenau, Österreich` (address)
- `Finanzamt` (organisation)
- `FA Kirchdorf Perg Steyr` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Siegfried Basyurt` | `Siegfried Basyurt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

| Predicted | Gold |
|---|---|
| `Chen Walcker` | `Chen Walcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- `63-698/2600` (tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hedwig Mackiewicz` | `Hedwig Mackiewicz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Krafft in der Beschwerdesache  Daniel Parys, Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich, vertreten durch APEX-Wirtschaftstreuhand Gesellschaft m.b.H.,  Hietzinger Hauptstraße 22/1/101, 1130 Wien, betreffend Beschwerde vom 24. April 2018  gegen den Bescheid des Finanzamtes Baden Mödling Finanzamtes Baden Mödling  Feststellungsbescheid gemäß § 92 Abs. 1 lit. c BAO (Nichtvorliegen der  Unternehmereigenschaft 2014 – 2016) vom 6. März 2018 betreffend Steuernummer xy  beschlossen:  Der Antrag auf Vorlage der Beschwerde wird gemäß § 264 Abs. 1 BAO in Verbindung mit  § 260  Abs. 1 lit. b BAO als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Daniel Parys` | `Daniel Parys` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Krafft` (person)
- `Prof. J. W. Zieglergasse 2, 4901 Oberkienberg, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamtes Baden Mödling` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ursula Buchholz` | `Ursula Buchholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Li Schukardt` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  Guntram Antepoth, Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich, über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid  des Finanzamtes Wien 2/20/21/22 vom 12. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 70-875/4351  zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

| Predicted | Gold |
|---|---|
| `Guntram Antepoth` | `Guntram Antepoth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Sterneckstraße 49, 4752 Bayrisch-Habach, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `70-875/4351` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

| Predicted | Gold |
|---|---|
| `Sven Mitterhuber` | `Sven Mitterhuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Mag.a Livia Korowski` (person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Laetitia Kuban, Karawankenplatz 8, 8046 Graz, Österreich, über die Beschwerde vom 16. Dezember 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 14. November 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für das Kind x in den Zeiträumen vom 01.07.2018 bis zum 30.09.2018  sowie vom 01.07.2019 bis zum 30.09.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Laetitia Kuban` | `Laetitia Kuban` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karawankenplatz 8, 8046 Graz, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129790.1`) (sent_id: `deanon_BFG_20260814_TEST/129790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin MMag. Elisabeth Brunner über die  Beschwerde der Serge Pechert, Texing 43, 3143 Oberloitzenberg, Österreich, vertreten durch Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH, Zieglergasse 27/2/9, 1070  Wien, gegen die Bescheide des Finanzamtes Wien 2/20/21/22 vom 10. Juli 2012 betreffend  Umsatzsteuer 2009, Körperschaftsteuer 2009 sowie Festsetzung von Kapitalertragsteuer für  den Zeitraum 2009 zu Recht:  Die Beschwerde gegen den Bescheid betreffend Körperschaftsteuer 2009 wird als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Serge Pechert` | `Serge Pechert` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag. Elisabeth Brunner` (person)
- `Texing 43, 3143 Oberloitzenberg, Österreich` (address)
- `Gosteco Goworek  Steuerberatungs-, Wirtschaftsprüfungs- und Consulting GmbH` (organisation)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Karina Ditzler` | `Karina Ditzler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Serena Weidlich  in der Beschwerdesache Ruprecht Pesselt,  Blons 28, 9612 Michelhofen, Österreich, betreffend Beschwerde gegen die Buchungsmitteilung  des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel zur Steuernummer 89-624/1157, betreffend  Gebühr gemäß § 17a VfGG und Gebührenerhöhung gemäß § 9 Abs.1 GebG 1957 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Ruprecht Pesselt` | `Ruprecht Pesselt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Serena Weidlich` (person)
- `Blons 28, 9612 Michelhofen, Österreich` (address)
- `Finanzamtes für  Gebühren` (organisation)
- `89-624/1157` (tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Waldemar Faltermeir  in der Beschwerdesache  Elias Kendziorra,  Fernblick 3, 6410 Telfs, Österreich, über die Beschwerde vom 24. Mai 2017 gegen den Bescheid des Finanzamt Waldviertel  vom 22. Mai 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016  Steuernummer 29-596/0625  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO abgewiesen.

| Predicted | Gold |
|---|---|
| `Elias Kendziorra` | `Elias Kendziorra` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Waldemar Faltermeir` (person)
- `Fernblick 3, 6410 Telfs, Österreich` (address)
- `Finanzamt Waldviertel` (organisation)
- `29-596/0625` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr. Helga Woschank in der Beschwerdesache  Leonhard Bianchini, Stixendorf 463, 6361 Glantersberg, Österreich,  über die Beschwerde vom 20.03.2018, eingebracht am 22. März 2018, gegen den Bescheid des  Finanzamtes Klagenfurt vom 16.02.2018, zu Steuernummer 13-665/9571, mittels welchem  der Antrag auf Wiederaufnahme der Verfahren betreffend Einkommensteuer für die Jahre  2012 bis 2015 abgewiesen wurde, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Leonhard Bianchini` | `Leonhard Bianchini` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helga Woschank` (person)
- `Stixendorf 463, 6361 Glantersberg, Österreich` (address)
- `Finanzamtes Klagenfurt` (organisation)
- `13-665/9571` (tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. RR. in der Beschwerdesache Melanie Mavromatakis,  Urbanusgasse 1, 3491 Obernholz, Österreich, über die Beschwerde vom 8. Juni 2018 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 9. Mai 2018 betreffend Umsatzsteuer 2014 bis 2017, Steuernummer , zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melanie Mavromatakis` | `Melanie Mavromatakis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Urbanusgasse 1, 3491 Obernholz, Österreich` (address)
- `Finanzamtes  Wien 1/23` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Charlotte Beha` | `Charlotte Beha` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Caroline Schröer` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Caroline Reinwaldt  in der Beschwerdesache Manuel Fortanz,  Zielgerade 30, 4950 Schwaig, Österreich, betreffend die Beschwerde vom 5. Juli 2017 gegen die Bescheide des Finanzamt Gmunden Vöcklabruck  vom 9. Juni 2017 betreffend Umsatz- und Körperschaftsteuer 2010 bis 2015 sowie  Umsatzsteuerfestsetzung für die Zeiträume 01-03/2016, 04-06/201, 07-09/2016 und 10- 12/2016, Steuernummer , beschlossen:  Die Beschwerde wird als gegenstandslos geworden erklärt und das Verfahren eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  iVm Abs. 9 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Manuel Fortanz` | `Manuel Fortanz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Caroline Reinwaldt` (person)
- `Zielgerade 30, 4950 Schwaig, Österreich` (address)
- `Finanzamt Gmunden Vöcklabruck` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Eugen Burgschweiger, Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr: Finanzamt  Österreich) vom 26. November 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2018 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Eugen Burgschweiger` | `Eugen Burgschweiger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Vöglerbrand 9, 8510 Ettendorf bei Stainz, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Bernarda Egli, Moosenweg 38, 5630 Harbach, Österreich, gegen den Bescheid des Finanzamtes Bregenz (nunmehr: Finanzamt  Österreich) vom 8. September 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Bernarda Egli` | `Bernarda Egli` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Moosenweg 38, 5630 Harbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Serena Leutl` | `Serena Leutl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Daisy Große-Bölting` (person)
- `Wanderweg 7, 2763 Thal, Österreich` (address)
- `Bernhart Steuerberatungs GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-306/6017` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ulrich Petrag in der Beschwerdesache  Natalie Nodurft, Saileräckergasse 112, 4676 Augassen, Österreich, vertreten durch Mag. Marion Riezinger, Sonnblickstraße 6, 4614  Marchtrenk, über die Beschwerden vom 15. April 2019 gegen die Bescheide des Finanzamtes  Linz vom 15. März 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis  2017 Steuernummer xxxyyyy zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Natalie Nodurft` | `Natalie Nodurft` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ulrich Petrag` (person)
- `Saileräckergasse 112, 4676 Augassen, Österreich` (address)
- `Mag. Marion Riezinger` (person)
- `Finanzamtes  Linz` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Elisabeth Sarigiannis,  Klesenza 7, 9587 Erlendorf, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH,  Lehmanngasse 7, 1230 Wien, über die Beschwerden vom 18. Dezember 2012 gegen die  Bescheide des Finanzamtes Österreich vom 21. November 2012 betreffend Einkommensteuer  2007 bis 2011, Steuernummer 84-729/8666, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Elisabeth Sarigiannis` | `Elisabeth Sarigiannis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Klesenza 7, 9587 Erlendorf, Österreich` (address)
- `gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `84-729/8666` (tax_number)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131930.1`) (sent_id: `deanon_BFG_20260814_TEST/131930.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Martin Kruthof, Schachet 8A, 9500 Obere Fellach, Österreich, betreffend Beschwerde vom 14. April 2010 gegen die Bescheide des FA Hollabrunn  Korneuburg Tulln vom 31. März 2010 betreffend Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer 2008 und Umsatzsteuer 2008 Steuernummer beschlossen:   Die Beschwerde vom 14. April 2010 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Martin Kruthof` | `Martin Kruthof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schachet 8A, 9500 Obere Fellach, Österreich` (address)
- `FA Hollabrunn  Korneuburg Tulln` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anneliese Wäsche  in der Beschwerdesache Gernot Kirchenmayer,  Richard-Wagner-Platz 15, 4153 Stierberg, Österreich, vertreten durch Eckert Fries Carter Rechtsanwälte GmbH, Erzherzog Rainer- Ring 23, 2500 Baden, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 19. Dezember 2018  betreffend Verspätungszuschlag / Sonstige 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Gernot Kirchenmayer` | `Gernot Kirchenmayer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Anneliese Wäsche` (person)
- `Richard-Wagner-Platz 15, 4153 Stierberg, Österreich` (address)
- `Eckert Fries Carter Rechtsanwälte GmbH` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Felizitas Johanesson` | `Felizitas Johanesson` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck` (person)
- `Aspangweg 17, 9781 Gailberg, Österreich` (address)
- `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)
- `48-504/5908` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Christina Tiebout` | `Christina Tiebout` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Dr. Sebastian Pfeiffer, LL.M.` (person)
- `Gerald Cuny-Kreuzer` (person)
- `Dr. Franz Kandlhofer` (person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich` (address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Paolo Reppert  in der Beschwerdesache des  Wendelin Pham, Kremstal Bundesstraße 6, 4682 Thalham, Österreich, über die Beschwerden 1.) vom 17.10.2019 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 15.10.2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 sowie  2.) vom 4.5.2020 gegen den Bescheid des Finanzamtes Graz-Stadt vom 3.4.2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Wendelin Pham` | `Wendelin Pham` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Paolo Reppert` (person)
- `Kremstal Bundesstraße 6, 4682 Thalham, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Juri Marstaller` | `Juri Marstaller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Lukas Dimitrieff` (person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich` (address)
- `Sonja Wennemann` (person)
- `Finanzamt Klagenfurt St. Veit Wolfsberg` (organisation)
- `Finanzamt Österreich` (organisation)
- `21-286/5389` (tax_number)
- `Bundesfinanzgerichtes` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melchior Englmaier` | `Melchior Englmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melchior Harasymiw` | `Melchior Harasymiw` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


IM NAMEN DER REPUBLI K  I. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerden vom 18. Juni 2017 gegen die Bescheide des  Finanzamtes Bregenz vom 16. Juni 2017 betreffend Einkommensteuer 2015 und 2016  Steuernummer 88-412/8444  beschlossen:   Die Vorlageanträge vom 19.11.2018 gegen die Beschwerdevorentscheidungen vom 10.10.2018  werden als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Francois Hetkemper` | `Francois Hetkemper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


II. Das Bundesfinanzgericht hat durch den Richter Mag. Armin Treichl in der Beschwerdesache  Francois Hetkemper, Fürwagstraße 19v, 3900 Stögersbach, Österreich, über die Beschwerde vom 29. Mai 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 17. Mai 2018 betreffend Einkommensteuer 2017, Steuernummer  88-412/8444  zu Recht erkannt:   Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Francois Hetkemper` | `Francois Hetkemper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Armin Treichl` (person)
- `Fürwagstraße 19v, 3900 Stögersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `88-412/8444` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adam Rueßbült  in den Beschwerdesachen des  Timon Reinhertz, Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich, über die Beschwerden vom 7. März 2019 gegen die Bescheide des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 4. März 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015, Steuernummer  15-325/9824, zu Recht erkannt:  Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Timon Reinhertz` | `Timon Reinhertz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Adam Rueßbült` (person)
- `Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `15-325/9824` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

| Predicted | Gold |
|---|---|
| `Linn Gouthier` | `Linn Gouthier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Pjotr Übereiter` (person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marcel Rac` | `Marcel Rac` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)
- `42-508/7924` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Andrea Helbok  in der Beschwerdesache Lydia Rehnen,  Roßbergl 5, 4923 Gunzing, Österreich, vertreten durch Proxauf Meyer Zeilinger Rechtsanwälte GmbH, Etrichgasse 14,  6020 Innsbruck, über die Beschwerde vom 3.4.2020 gegen den Bescheid des Finanzamtes  Innsbruck vom 17.3.2020, SV-Nr, betr.

| Predicted | Gold |
|---|---|
| `Lydia Rehnen` | `Lydia Rehnen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Andrea Helbok` (person)
- `Roßbergl 5, 4923 Gunzing, Österreich` (address)
- `Proxauf Meyer Zeilinger Rechtsanwälte GmbH` (organisation)
- `Finanzamtes  Innsbruck` (organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Richard Schwanken  in der Beschwerdesache Alexandra Hettrich,  Kohleggweg 268, 4621 Schnarrndorf, Österreich, über die Beschwerde vom 3. Oktober 2020 gegen den Bescheid des  Finanzamtes Österreich (vormals Finanzamt Lilienfeld St. Pölten) vom 28. August 2020  betreffend die Abweisung einer Nachsicht von Abgabenschuldigkeiten, Steuernummer  86-148/2619, zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabenordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Alexandra Hettrich` | `Alexandra Hettrich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Richard Schwanken` (person)
- `Kohleggweg 268, 4621 Schnarrndorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Lilienfeld St. Pölten` (organisation)
- `86-148/2619` (tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Esra Luetje` | `Esra Luetje` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Mag.a Heidrun Eifeler` (person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich` (address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  Aloisa Antoni, Wassermanngasse 9, 4840 Vöcklabruck, Österreich  vertreten durch die Steuerfilter Steuerberatungs-GmbH,  Ischlerbahnstraße 23, 5301 Eugendorf, über die Beschwerde vom 11. Juni 2019 und 9. Oktober  2019 gegen die Bescheide des Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich)  vom 16. Mai 2019 und 2. Oktober 2019 betreffend die Wiederaufnahme der  Einkommensteuerverfahren 2013 bis 2015 zu Recht erkannt:  I)  Die Wiederaufnahmebescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Aloisa Antoni` | `Aloisa Antoni` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Erich Schwaiger` (person)
- `Wassermanngasse 9, 4840 Vöcklabruck, Österreich` (address)
- `Steuerfilter Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Juliana Untermeier, C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt, Schwefel  93/7, 6850 Dornbirn, über die Beschwerde vom 16. Mai 2013 gegen den Bescheid des  Finanzamtes Bregenz vom 10. April 2013 betreffend Haftung gemäß § 9 iVm § 80  Bundesabgabenordnung (BAO), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Juliana Untermeier` | `Juliana Untermeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich` (address)
- `Dr. Christoph Ganahl` (person)
- `Finanzamtes` (organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Univ.-Prof.in Elina Hetcamp  in der Beschwerdesache Florentine Mugge,  Rodlhütte 36, 9782 Plone, Österreich, über die Beschwerde vom 5. April 2013 gegen die Bescheide des FA Kufstein  Schwaz (nunmehr Finanzamt Österreich) vom 22. März 2013, Str. Nr. 59-679/2034,  betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum Februar 2012      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Florentine Mugge` | `Florentine Mugge` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Univ.-Prof.in Elina Hetcamp` (person)
- `Rodlhütte 36, 9782 Plone, Österreich` (address)
- `FA Kufstein  Schwaz` (organisation)
- `Finanzamt Österreich` (organisation)
- `59-679/2034` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Lisa Lindnau, Rosenbergen 12, 3430 Mollersdorf, Österreich, vertreten durch Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft,  Schulrat-Stöckler-Straße 19, 4320 Perg, über die Beschwerde vom 15. November 2019 gegen  den Bescheid des Finanzamtes Kirchdorf Perg Steyr vom 17. Oktober 2019 betreffend  Abweisung des Antrags gemäß § 293b BAO auf Berichtigung des Einkommensteuerbescheides  2014 vom 5.9.2016, Steuernummer 35-287/7417  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Rosenbergen 12, 3430 Mollersdorf, Österreich` (address)
- `Kastler Wirtschaftstreuhand GmbH Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Kirchdorf Perg Steyr` (organisation)
- `35-287/7417` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Sieglinde Steinkaemper  in der Beschwerdesache Julian Gruening,  Litzldorfer-Gasse 83, 4893 Harpoint, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, und GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Handelskai 92, Gate 2, 7A, 1200 Wien, über die   1.

| Predicted | Gold |
|---|---|
| `Julian Gruening` | `Julian Gruening` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Dr.in Sieglinde Steinkaemper` (person)
- `Litzldorfer-Gasse 83, 4893 Harpoint, Österreich` (address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH` (organisation)
- `GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Babette Bernett, Schmalzhofen 9, 8250 Riegersbach, Österreich, über die Beschwerde vom 17. September 2020 gegen den  Bescheid des Finanzamtes Kufstein Schwaz (nunmehr Finanzamt Österreich) vom 4. September  2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019, zu Recht erkannt:   Die Beschwerdevorentscheidung vom 24. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 wird gemäß § 279 Abs. 1 BAO ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `Babette Bernett` | `Babette Bernett` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Schmalzhofen 9, 8250 Riegersbach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (im Folgenden: BFG) hat durch den RichterRi in der Beschwerdesache  Anita Imkeller, Zum Roten Kreuzl 13, 4741 Penesedt, Österreich, betreffend Beschwerde vom 29. März 2021 gegen den Bescheid  des Finanzamt Niederösterreich Mitte  vom 4. Februar 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2019 Steuernummer 50-932/4879  beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Anita Imkeller` | `Anita Imkeller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `BFG` (organisation)
- `Zum Roten Kreuzl 13, 4741 Penesedt, Österreich` (address)
- `Finanzamt Niederösterreich Mitte` (organisation)
- `50-932/4879` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Lewis Rzehula` — partial — gold is substring of pred: `Lewis Rzehula`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lewis Rzehula`(person)
- `Neustädterstraße 3, 9560 Wabl, Österreich`(address)
- `43-839/6567`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Gruenleitner Event` — type mismatch — same span as gold: `Gruenleitner Event`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_25`)


Anbot eines deutschen Fahrzeughändlers) zum Pkw der Marke Land Rover, Typ Range Rover  Sport 3,0 TdV6 HSE (Diesel, Motorleistung 180 kW, CO2-Emission 243 g/km), wonach der  Neupreis eines solchen Fahrzeuges zwischen rund (brutto) € 75.000 bis rund € 78.000 beträgt.

**False Positives:**

- `Marke Land Rover` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Corbinian Friemuth`(person)
- `Mag. Alexander Rimser`(person)
- `Hermann`(person)
- `Magistrat der Stadt Wien`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_71`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung  der Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für  das Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer  Abgabe vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem  Muster der Anlagen oder elektronische Parkscheine zu verwenden.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_75`)


Dieses wird durch  die Verordnung des Wiener Gemeinderates, mit der für das Abstellen von mehrspurigen  Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben wird  (Parkometerabgabeverordnung), festgesetzt.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129260.1`) (sent_id: `deanon_BFG_20260814_TEST/129260.1_128`)


Auf Grund dieser Ausführungen des Verfassungsgerichtshofes hat das Bundesfinanzgericht  keine verfassungsrechtlichen Bedenken gegen die Bestimmungen Parkraumbewirtschaftung  der Stadt Wien, soweit sie im gegenständlichen Fall zur Anwendung gelangen.

**False Positives:**

- `Stadt Wien` — type mismatch — same span as gold: `Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Verfassungsgerichtshofes`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Stadt Wien`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_83`)


Im Akt erliegen mehrere Internet-Abfragen des Finanzamtes (zu Angeboten bei  gebrauchtwagen.at, mobile.de) vom Juli 2015 zu vergleichbaren Pkw der Marke Ford Mustang,  Gebrauchtwagen, Benziner, Bj. 2005 oder 2006, Motorleistung 151 kW (= 205 PS) oder 154 kW,  4 von 29 Seite 5 von 29

**False Positives:**

- `Marke Ford Mustang` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_124`)


Im Ergänzungsersuchen vom 17.3.2016 hat das Finanzamt zunächst festgehalten, dass der  Bf seit Mai 2008 nahezu durchgehend in Österreich beschäftigt und mit Wohnsitz gemeldet  gewesen sei und hat vom Bf eine Vielzahl an Unterlagen – darunter Nachweise zu deutschen  Mietzahlungen, zum Verkauf des Ford Mustang, Service- und Reparaturrechnungen der  Fahrzeuge, zu einem allfälligen deutschen Handyvertrag und Girokonto - , die zum  Gegenbeweis dienen könnten, angefordert.

**False Positives:**

- `Ford Mustang` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wladimir Dammkoehler, Grolzham 15, 3123 Obermerking, Österreich, über die Beschwerde vom 24. Jänner 2020  gegen den Bescheid des Finanzamtes Baden Mödling vom 22. Jänner 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 47-339/1168, zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Wladimir Dammkoehler` — partial — gold is substring of pred: `Wladimir Dammkoehler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Wladimir Dammkoehler`(person)
- `Grolzham 15, 3123 Obermerking, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)
- `47-339/1168`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_8`)


Entscheidungsgründe  Mit Schreiben des Magistrates der Stadt Wien, Magistratsabteilung 67,  Parkraumüberwachung, wurde VN-F NN als Zulassungsbesitzerin gemäß § 2 Parkometergesetz  2006, LBGl. für Wien Nr. 9/2006 in der geltenden Fassung aufgefordert, bekanntzugeben, wem  1 von 28 Seite 2 von 28

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_85`)


Das Magistrat der Stadt Wien, Magistratsabteilung 67, erließ am 6.11.2019 ein Straferkenntnis,  Zahl GESCHÄFTSZAHL, in welchem die dem Bf. zur Last gelegte Verwaltungsübertretung als  erwiesen angesehen wurde.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_391`)


Gemäß § 5 Abs. 2 der Verordnung des Wiener Gemeinderates, mit der für das Abstellen von  mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe vorgeschrieben  wird (Parkometerabgabeverordnung) idgF sind zur Entrichtung der Abgabe der Lenker, der  Besitzer und der Zulassungsbesitzer zur ungeteilten Hand verpflichtet.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Babette Nimzyk  in der Beschwerdesache Tamara Poertgen, LLB Bakk. techn.,  Schnerichweg 23q, 4676 Himmelreich, Österreich, vertreten durch Martin Friedl, Marktplatz 2, 4650 Lambach, über die  Beschwerde vom 14. Februar 2018 gegen den Bescheid des Finanzamtes Grieskirchen Wels  vom 9. Februar 2018 betreffend Säumniszuschlag 2018, Steuernummer 08-216/2001, zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Tamara Poertgen` — partial — pred is substring of gold: `Tamara Poertgen, LLB Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Babette Nimzyk`(person)
- `Tamara Poertgen, LLB Bakk. techn.`(person)
- `Schnerichweg 23q, 4676 Himmelreich, Österreich`(address)
- `Martin Friedl`(person)
- `Finanzamtes`(organisation)
- `08-216/2001`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

**False Positives:**

- `Stadt  Wien` — partial — pred is substring of gold: `Magistrates der Stadt  Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Daisy Hoopt`(person)
- `Prof.in StR DDr.in Reneé Plein`(person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_12`)


Zu 1) MA67/196701153394/2019  Mit Lenkerauskunftsersuchen vom 23. Jänner 2020, MA67/196701153394 (§ 2 Wiener  Parkometergesetz 2006) wurde die Zulassungsbesitzerin vom Magistrat der Stadt Wien,  Magistratsabteilung 67, unter Angabe der unter 1) näher bezeichneten Daten zur  Lenkerauskunft binnen zwei Wochen ab Zustellung des Schreibens aufgefordert.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_34`)


Zu 2) MA67/1967011579971/2019  Mit Lenkerauskunftsersuchen vom 23. Jänner 2020, MA67/1967011579971 (§ 2 Wiener  Parkometergesetz 2006) wurde die Zulassungsbesitzerin vom Magistrat der Stadt Wien,  Magistratsabteilung 67, unter Angabe der unter 2) näher bezeichneten Daten zur  Lenkerauskunft binnen zwei Wochen ab Zustellung des Schreibens aufgefordert.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien,  Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien,  Magistratsabteilung 67`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Dominika Oehlerich` — positional overlap with gold: `Dominika Oehlerich, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Ebner`(person)
- `Dominika Oehlerich, BEd`(person)
- `Zamberg 9, 3843 Hohenau, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

**False Positives:**

- `Beschwerdesache Isidor Czebulla` — partial — gold is substring of pred: `Isidor Czebulla`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Manuela Fischer`(person)
- `Isidor Czebulla`(person)
- `Eggenburger Straße 88, 9423 Pfaffendorf, Österreich`(address)
- `TPA Steuerberatung GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Heinz Herper` — partial — gold is substring of pred: `Heinz Herper`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Heinz Herper`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_146`)


Zusammengefasst ergibt sich aus der Anamnese, dass der Bf. laut eigenen Angaben die  Handelsakademie besuchte und anschließend BWL studierte (kein Abschluss) und an der  Universität Wien vom Sommersemester 1989 bis Wintersemester 1995 in der Studienrichtung  Soziologie, geisteswissenschaftliche Stzw Politikwissenschaft inskribiert war  (Studienzeitbestätigung der Universität Wien vom 28. Juli 2016).

**False Positives:**

- `Studienrichtung  Soziologie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Universität Wien`(organisation)
- `Universität Wien`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_164`)


Laut Studienzeitbestätigung der Universität Wien vom 28. Juli 2016 war der Bf. in der  Studienrichtung Soziologie, geisteswissenschaftliche Stzw Politikwissenschaft vom  Sommersemester 1989 bis Wintersemester 1995 inskribiert.

**False Positives:**

- `Studienrichtung Soziologie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Universität Wien`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130681.1`) (sent_id: `deanon_BFG_20260814_TEST/130681.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri über die Beschwerde der Cathleen Gröneweg, Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich, vom 2. April 2019 gegen den Bescheid des Finanzamtes Klagenfurt, dieses vertreten  durch ORätin AmtsV BA MA, vom 15. März 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes Klagenfurt` — type mismatch — same span as gold: `Finanzamtes Klagenfurt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Cathleen Gröneweg`(person)
- `Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich`(address)
- `Finanzamtes Klagenfurt`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/130692.1`) (sent_id: `deanon_BFG_20260814_TEST/130692.1_2`)


in der Verwaltungsstrafsache gegen  Detlev Griessmer, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich, über die Beschwerde vom 8. April 2020 gegen das Straferkenntnis  des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 26. März 2020, Geschäftszahl MA  67/196701206198/2019, uRecht erkannt:    I. Detlev Griessmer, Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich  wird eine Ermahnung erteilt. Das Straferkenntnis wird aufgeho- ben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Detlev Griessmer`(person)
- `Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Detlev Griessmer`(person)
- `Franz-Kreitler-Straße 4, 9346 Tschröschen, Österreich`(address)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_3`)


Am Ausspruch des Magistrats der Stadt Wien, dass der Beschwerdeführer gem. § 64 Abs. 2  VStG 1991 einen Beitrag zu den Kosten des erstinstanzlichen Strafverfahrens zu zahlen hat, tritt  keine Änderung ein.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrats der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrats der Stadt Wien`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_137`)


Weiters sind nach der Rechtsprechung des Verwaltungsgerichthofes Zahlungen, die schlechthin  strittige Ansprüche aller Art abgelten, nicht etwa gleich Abfertigungen für die Beendigung eines  Dienstverhältnisses typisch (VwGH 20.11.2012, 2008/13/0252;

**False Positives:**

- `Verwaltungsgerichthofes Zahlungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `Beschwerdesache Eleonore Sawadzki` — positional overlap with gold: `Eleonore Sawadzki, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Sawadzki, Bakk. art.`(person)
- `Weintraubengasse 36, 9073 Aich, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Beschwerdesache Wieland Gorecki` — partial — gold is substring of pred: `Wieland Gorecki`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Wieland Gorecki`(person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_7`)


Entscheidungsgründe  Verfahrensgang:  Dem Beschwerdeführer wurde von der belangten Behörde, unter Zugrundelegung der Anzeige  eines Kontrollorganes der Landespolizeidirektion Wien, Abteilung für Parkraumüberwachung,  mit Strafverfügung vom 12.10.2020, MA67/Zahl/2020, angelastet, er habe das Fahrzeug mit  dem behördlichen Kennzeichen 123 (A) am 12.8.2020 um 11:40 Uhr in der gebührenpflichtigen  Kurzparkzone in 1150 Wien, Zinckgasse 25, abgestellt, ohne für seine Kennzeichnung mit  einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Landespolizeidirektion Wien` — type mismatch — same span as gold: `Landespolizeidirektion Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Landespolizeidirektion Wien`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Hartwig Simonson, Neubruchgasse 122L, 9562 Flatschach, Österreich, über die Beschwerde vom 11. Februar 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 11. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und die Beschwerde vom 7. März 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 8. Februar 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Beschwerdesache Hartwig Simonson` — partial — gold is substring of pred: `Hartwig Simonson`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Hartwig Simonson`(person)
- `Neubruchgasse 122L, 9562 Flatschach, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamtes`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_75`)


Der Bf. befindet sich seit 16.05.2019 im Krisenzentrum Pleischlgasse, einer  sozialpädagogischen Einrichtung der Stadt Wien, und erzielte seit Ende September 2019 eine  Lehrlingsentschädigung.

**False Positives:**

- `Stadt Wien` — type mismatch — same span as gold: `Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Stadt Wien`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_51`)


§ 26a Abs. 4 StVO 1960 idF ab 01.06.2019 normiert:  "Die Lenker  1. von Fahrzeugen der Österreichischen Post Aktiengesellschaft und der Telekom Austria  Aktiengesellschaft,  2. von Fahrzeugen sonstiger Post-, Paket-, Telekommunikations- oder Fernmeldedienstanbieter,  […]  5. von Fahrzeugen, die im Auftrag eines der unter Z 1 bis 3 genannten Dienstanbieter fahren,  sind bei der Zustellung und Abholung von Postsendungen, bei der Instandhaltung von Tele- kommunikations- oder Fernmeldeeinrichtungen, bei der Zustellung und Abholung von Bargeld  oder Edelmetallen sowie bei Einsätzen der Funküberwachung an Halte- und Parkverbote nicht  gebunden, sofern dies der Betriebseinsatz erfordert und der übrige Verkehr dadurch nicht  wesentlich beeinträchtigt wird."

**False Positives:**

- `Telekom Austria  Aktiengesellschaft` — partial — pred is substring of gold: `Österreichischen Post Aktiengesellschaft und der Telekom Austria  Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichischen Post Aktiengesellschaft und der Telekom Austria  Aktiengesellschaft`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_17`)


Am 15. Oktober 2020 erließ der Magistrat der Stadt Wien, Magistratsabteilung 6, die  beschwerdegegenständliche Vollstreckungsverfügung, Zahl MA67/Zahl/2020 mit folgendem  Wortlaut:  Die mit der Strafverfügung vom 28. August 2020, Zahl MA67/Zahl/2020, verhängte  rechtskräftige Strafe sei bis heute nicht bezahlt worden.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_38`)


Am 6. November 2019 langte die Beschwerde der Beschuldigten und der Haftenden beim  Magistrat der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen ein.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, Magistratsabteilung 6`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien, Magistratsabteilung 6`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Dominik Moebus,  Aichach 11m, 9375 Knappenberg, Österreich, vertreten durch Magistrat der Stadt Wien, Kinder- und Jugendhilfe,  Rechtsvertretung 16,17,18,19, Kalvarienberggasse 29, 1170 Wien, betreffend die Beschwerde  vom 25. August 2020 gegen den Abweisungsbescheid des Finanzamtes Österreich (bisher  Finanzamt Wien 2/20/21/22) vom 17. Juli 2020 betreffend Familienbeihilfe ab Jänner 2016  beschlossen:   Der am 12. Jänner 2021 eingebrachte, mit 07. Jänner 2021 datierte Vorlageantrag betreffend  die am 04. Dezember 2020 zugestellte Beschwerdevorentscheidung vom 12. November 2020  wird gemäß § 264 Abs 4 lit e BAO iVm § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dominik Moebus`(person)
- `Aichach 11m, 9375 Knappenberg, Österreich`(address)
- `Magistrat der Stadt Wien`(organisation)
- `Finanzamtes Österreich`(organisation)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_34`)


Im vorgelegten Akt befinden sich noch folgende Unterlagen:  Vereinbarung der vollen Erziehung vom 24.02.2016, Antrag auf Betrauung mit der  Vermögensverwaltung vom 09.03.2020, Vereinbarung über den Kostenersatz vom 10.03.2016  und Schriftsatz des Magistrates der Stadt Wien, Rechtsvertretung 17,18,19, vom 01.02.2016.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Robert Pernegger`(person)
- `StR Ing. Alexandra Ebermaier, MBA`(person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_9`)


Entscheidungsgründe  Mit Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67,  Parkraumüberwachung vom 25. Februar 2021, Zahl MA67/Zahl1/2020, wurde über den  Beschwerdeführer eine Geldstrafe in Höhe von 60,00 Euro, im Fall der Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden verhängt, weil er das mehrspurige Kraftfahrzeug mit dem  behördlichen Kennzeichen 123 (A) am 21. Juli 2020 um 15:19 Uhr in einer gebührenpflichtigen  Kurzparkzone in 1160 Wien, Paltaufgasse 6, abgestellt habe ohne für seine Kennzeichnung mit  einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien, Magistratsabteilung 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/132651.1`) (sent_id: `deanon_BFG_20260814_TEST/132651.1_54`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das  Abstellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Romana Stavrakis, Untersameting 4, 4894 Römerhof, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 04. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 28. April  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 nach Durchführung einer  öffentlichen mündlichen Verhandlung am 07.04.2021 zu Recht erkannt:   1.

**False Positives:**

- `Rechtssache Romana Stavrakis` — partial — gold is substring of pred: `Romana Stavrakis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Romana Stavrakis`(person)
- `Untersameting 4, 4894 Römerhof, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Hademar Sachteleben, MSc, Fröhlichgasse 31, 3244 Hofstetten, Österreich, über die zwei Beschwerden des  Beschuldigten gegen die nachfolgend angeführten zwei Vollstreckungsverfügungen (VVF) des  Magistrates der Stadt Wien, jeweils betreffend Zwangsvollstreckung wegen Nichtbezahlung  der rechtskräftigen Strafe auf Grund des nachfolgend angeführten Erkenntnis des  Bundesfinanzgerichtes, jeweils betreffend eine Verwaltungsübertretung nach § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006,

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrates der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Müller-Dobler MBA MSc`(person)
- `Hademar Sachteleben, MSc`(person)
- `Fröhlichgasse 31, 3244 Hofstetten, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Bundesfinanzgerichtes`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_11`)


• Nach Auskunft der Stadt Graz, Gewerbeamt wurde bei dem Abgabenpflichtigen am  05.07.2017 kein Gewerbe gelöscht.

**False Positives:**

- `Stadt Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache Wigand Maczkiewicz, Bakk. art.,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Wigand Maczkiewicz` — partial — pred is substring of gold: `Wigand Maczkiewicz, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Univ.-Prof. Kai Menrath`(person)
- `Wigand Maczkiewicz, Bakk. art.`(person)
- `Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich`(address)
- `Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `49-963/8463`(tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_15`)


Mit Straferkenntnis vom 13. Jänner 2021, MA67/Zahl/2020, wurde der Bf. vom Magistrat der  Stadt Wien, MA 67, wegen der bereits näher bezeichneten Verwaltungsübertretung für  schuldig befunden und wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1  Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  von € 60,00 sowie für den Fall der Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 14 Stunden  festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der  Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der  Stadt Wien`(organisation)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/133509.1`) (sent_id: `deanon_BFG_20260814_TEST/133509.1_43`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache Sven Hoerlin, Padasterjochhaus 6, 9562 Tobitsch, Österreich, gegen den Bescheid  des Finanzamtes Spittal  Villach vom 17. November 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013 Steuernummer 51-093/9549  folgenden Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Beschwerdesache Sven Hoerlin` — partial — gold is substring of pred: `Sven Hoerlin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Heidemarie Winkler`(person)
- `Sven Hoerlin`(person)
- `Padasterjochhaus 6, 9562 Tobitsch, Österreich`(address)
- `Finanzamtes Spittal  Villach`(organisation)
- `51-093/9549`(tax_number)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_14`)


Mit Straferkenntnis vom 28. Juni 2021 wurde die Bf. vom Magistrat der Stadt Wien, MA 67,  wegen der bereits näher bezeichneten Verwaltungsübertretung für schuldig erkannt und  wegen Verletzung der Rechtsvorschriften des § 5 Abs. 1 Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe von € 60,00 und für den Fall der Unein- bringlichkeit 14 Stunden Ersatzfreiheitsstrafe festgesetzt.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_54`)


Nach § 1 Wiener Kontrolleinrichtungenverordnung sind als Hilfsmittel zur Überwachung der  Einhaltung der Vorschriften der Verordnung des Wiener Gemeinderates, mit der für das Ab- stellen von mehrspurigen Kraftfahrzeugen in Kurzparkzonen die Entrichtung einer Abgabe  vorgeschrieben wird (Parkometerabgabeverordnung), Parkscheine nach dem Muster der  Anlagen oder elektronische Parkscheine zu verwenden.

**False Positives:**

- `Wiener Gemeinderates` — type mismatch — same span as gold: `Wiener Gemeinderates`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wiener Gemeinderates`(organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Marco Laudacher, die  Richterin Mag. Susanne Haim, sowie die fachkundigen Laienrichter Mag Stefan Raab und  Leopold Pichlbauer in der Beschwerdesache Bettina Domigall, Bakk. iur., Zickhöhe 66, 3361 Biberbach, Österreich  vom 19. November  2019, vertreten durch Shamiyeh & Reiser Rechtsanwälte GmbH, Rainerstraße 6-8, 4020 Linz,  gegen die Bescheide des Finanzamtes Österreich, Dienststelle Linz, vom 7. August 2019  betreffend Umsatzsteuer 2017 und 2018 sowie Festsetzung Umsatzsteuer 1-4/2019 nach  Durchführung einer mündlichen Verhandlung am 18. August 2021 in Anwesenheit der  Schriftführerin Tanja Grottenthaler

**False Positives:**

- `Bettina Domigall` — partial — pred is substring of gold: `Bettina Domigall, Bakk. iur.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Marco Laudacher`(person)
- `Mag. Susanne Haim`(person)
- `Mag Stefan Raab`(person)
- `Leopold Pichlbauer`(person)
- `Bettina Domigall, Bakk. iur.`(person)
- `Zickhöhe 66, 3361 Biberbach, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `Tanja Grottenthaler`(person)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_15`)


Weiters gab das Gericht der Bf Gelegenheit, sich hiezu zu binnen 2 Wochen ab Zustellung des  Vorhaltes zu äußern, innerhalb derer sie die Möglichkeit hatte, darzulegen und durch  Unterlagen nachzuweisen, warum die Beschwerdefrist entgegen dem dargestellten  Sachverhalt nicht am 4.2.2021 zu laufen begonnen und am 4.3.2021 geendet hat.

**False Positives:**

- `Bf Gelegenheit` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

**False Positives:**

- `Beschwerdesache Ingrid Dohrmaier` — partial — gold is substring of pred: `Ingrid Dohrmaier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Ingrid Dohrmaier`(person)
- `Daläus 14O, 2301 Wittau, Österreich`(address)
- `Korber & Partner WTH-Stb  GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf`(organisation)
- `Finanzamtes Österreich`(organisation)
- `41-654/1190`(tax_number)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde der Michael Klingsohr, Hochburg 78, 4363 Pabneukirchen, Österreich, vom 09. Dezember  2016 gegen den Bescheid des Magistrats der Stadt Wien, Magistratisches Bezirksamt für den  13./14.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrats der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Michael Klingsohr`(person)
- `Hochburg 78, 4363 Pabneukirchen, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_9`)


Diese  Beschwerde wurde vom Magistrat der Stadt Wien, Magistratisches Bezirksamt für den  13./14.

**False Positives:**

- `Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_17`)


(2) Wird mit Bescheidbeschwerde die Einreihung einer Ware in den Zolltarif angefochten, so  sind der Bescheidbeschwerde Muster, Abbildungen oder Beschreibungen, aus denen die für die  Einreihung maßgeblichen Merkmale der Ware hervorgehen, beizugeben.

**False Positives:**

- `Bescheidbeschwerde Muster` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Prof. Title Pattern` 

**F1:** 0.005 | **Precision:** 0.444 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `8ae71578`  
**Description:**
Specifically targets the academic title 'Prof.' followed by a full name, handling cases where there is no space between the title and the first name (e.g., 'Prof.Bernadette').

**Content:**
```
\b(?:Prof\.|Univ\.-Prof\.|Univ\.-Prof\.in)\s*[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.444 | 0.002 | 0.005 | 9 | 4 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 4 | 5 | 1610 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_8`)


Mit Schriftsatz vom 12.04.2022 brachte der Bf dagegen Beschwerde ein, da seine damalige  Lebenspartnerin und jetzige Ehefrau Prof. Engelbert Thuerrigl  verehelichte A, im Jahr 2019 für den  gemeinsamen Sohn, K A geboren am 3/19, ab März sowohl die Familienbeihilfe als auch den  Kinderabsetzbetrag erhalten habe.

| Predicted | Gold |
|---|---|
| `Prof. Engelbert Thuerrigl` | `Prof. Engelbert Thuerrigl` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_14`)


Ziel der Bautätigkeit sei die Schaffung einer gemeinsamen  Wohnung für seine Familie, dh für seine Frau Prof. Engelbert Thuerrigl  verehelichte A, seine Kinder und für ihn  selbst, gewesen.

| Predicted | Gold |
|---|---|
| `Prof. Engelbert Thuerrigl` | `Prof. Engelbert Thuerrigl` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Evamaria Fränzl  in der Beschwerdesache  Prof. Raphael Grieben, Habegg 37, 5120 Pirach, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien,   betreffend Beschwerde vom 21. Dezember 2023 gegen den Bescheid des Finanzamt Graz-Stadt  vom  30. August 2023 betreffend Vorsteuererstattung 2022 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Prof. Raphael Grieben` | `Prof. Raphael Grieben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Evamaria Fränzl` (person)
- `Habegg 37, 5120 Pirach, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Graz-Stadt` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_3`)


Begründung  Am 30. August 2023 erließ das Finanzamt Österreich einen „Bescheid über die Erstattung von  Vorsteuern für 01-12/2022“, der an die Bf. „Prof. Raphael Grieben, z.H. Hemma Bödker“ adressiert war.

| Predicted | Gold |
|---|---|
| `Prof. Raphael Grieben` | `Prof. Raphael Grieben` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)
- `Hemma Bödker` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_480`)


Die Schaffung von Kryptowährungen (am Beispiel Bitcoin) – allgemeines (Auszug aus  Domes-Hohl, Die steuerliche Behandlung von virtuellen Währungen am Beispiel von Bitcoins,  Diplomarbeit Institut für Finanzrecht Graz, Univ-Prof. Kerstin Tina Ehrke-Rabl, 2019, S. 3-27;  zum technischen Aufbau des Netzwerks siehe Gerion Entrup, Bitcoin – der Stärkere gewinnt,  2013, Bachelorarbeit, Institut für theoretische Informatik, Dr. Arne Meier):   a. Bitcoin ist eine Kryptowährung und existiert nicht in physischer Form.

**False Positives:**

- `Prof. Kerstin Tina Ehrke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Arne Meier`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_659`)


Domes-Hohl, Die steuerliche Behandlung  von virtuellen Währungen am Beispiel von Bitcoins, Diplomarbeit Institut für Finanzrecht Graz,  Univ-Prof. Kerstin Tina Ehrke-Rabl, 2019, S. 143-144: Es kann sehr wohl ein unmittelbarer  Zusammenhang zwischen dem Ressourceneinsatz des Miners und den aus dem mit Erfolg  betriebenen Mining lukrierten Bitcoins bestehen).

**False Positives:**

- `Prof. Kerstin Tina Ehrke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_661`)


In weiterer Folge ist zu untersuchen, ob der Miner eine wirtschaftliche Tätigkeit gemäß Art  9 MwStSystRL ausübt bzw gemäß § 2 Abs 1 UStG unternehmerisch tätig wird (Klotz, aaO, S. 70),  also eine steuerbare Dienstleistung gegen Entgelt gegeben ist (Domes-Hohl, Die steuerliche  Behandlung von virtuellen Währungen am Beispiel von Bitcoins, Diplomarbeit Institut für  Finanzrecht Graz, Univ-Prof. Kerstin Tina Ehrke-Rabl, 2019, S. 137).

**False Positives:**

- `Prof. Kerstin Tina Ehrke` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Prof. Leander Pfleumer, LLM, Am Gewerbepark 6, 9065 Niederdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 11. November 2020 gegen den Bescheid  des Finanzamtes Linz (nunmehr Finanzamtes Österreich ) vom 22. Oktober 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 11-306/0925  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Prof. Leander Pfleumer` — partial — pred is substring of gold: `Prof. Leander Pfleumer, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Walter Aiglsdorfer`(person)
- `Prof. Leander Pfleumer, LLM`(person)
- `Am Gewerbepark 6, 9065 Niederdorf, Österreich`(address)
- `Alfred Klaus Fenzl`(person)
- `Finanzamtes Linz`(organisation)
- `Finanzamtes Österreich`(organisation)
- `11-306/0925`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_11`)


Empfehlung zu weiteren Tests bzw. Beratungsgespräch)   – Schreiben der Dr. Mag. E.Sch., w.o., vom 18. Dezember 2019 (Zusammenfassung der  Ergebnisse der erfolgten Begutachtung bezüglich einer vermuteten Legasthenie)   – Schulnachricht der Klasse 6 (6. Schulstufe) der Rudolf Steiner … Freie Waldorfschule vom  14. Februar 2020 (Deutsch genügend, Mathematik nicht genügend, Englisch nicht genügend)   – Befundbericht von Univ. Prof.Charlotte Koebbe  Facharzt für Hals-, Nasen-, Ohrenheilkunde, Kopf- und  Halschirurgie, allgemein beeideter und gerichtlich zertifizierter Sachverständiger vom 27. Mai  2020 (Diagnose: Verdacht auf auditive Verarbeitungsstörung;

**False Positives:**

- `Prof.Charlotte Koebbe  Facharzt` — partial — gold is substring of pred: `Charlotte Koebbe`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mag. E.Sch.`(person)
- `Charlotte Koebbe`(person)

</details>

---

## `Frau Name Context Refined` 

**F1:** 0.004 | **Precision:** 0.333 | **Recall:** 0.002  

**Format:** `regex`  
**Rule ID:** `4d4ca947`  
**Description:**
Captures names following 'Frau' (e.g., 'Frau Tatjana Löper'), ensuring full name capture including potential suffixes and single-word surnames.

**Content:**
```
\bFrau\s+((?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|RA\.|StB\.|Prof\.in|Prof\.|VetR|Hon\.-Prof\.|Hon\.-Prof\.in|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|OMedR)\s+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+|[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+|[A-Z][a-z]{2,})(?:,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.002 | 0.004 | 9 | 3 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 3 | 6 | 1611 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_37`)


Die GmbH hafte für die mit diesem Bescheid über die zur Vertretung nach außen Berufene,  Frau Nina Rasem, verhängten Geldstrafen von € 450,00, € 450,00, € 450,00, € 450,00, € 450,00,  € 450,00, € 310,00, € 310,00, € 310,00, € 310,00, € 310,00 und € 310,00 und die  Verfahrenskosten in der Höhe von € 456,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_36`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Im vorliegenden Beschwerdefall hat die belangte Behörde das Strafverfahren gegen Frau Manhardt  AdresseBeschuldigte, aufgrund der ihr zur Verfügung stehenden Unterlagen als  Beschuldigte eingeleitet und ihr mit Strafverfügung vom 4. Juni 2024 eine  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 angelastet sowie eine Geldstrafe in Höhe von  60,00 Euro verhängt und im Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von 14 Stunden  auferlegt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/149321.1`) (sent_id: `deanon_BFG_20260814_TEST/149321.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Frau Christina Schwabendissen, Beschwerdeführerin, reichte ihre Erklärung zur Arbeitnehmerveranlagung  2015 am 7.12.2020 am Finanzamt ein.

| Predicted | Gold |
|---|---|
| `Christina Schwabendissen` | `Christina Schwabendissen` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

**False Positives:**

- `Nina` — partial — pred is substring of gold: `Nina Rasem`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Nina Rasem`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Joachim Kotmann (= Beschwerdeführerin, Bf) hat für die Tochter A, geb. 11/1999, laufend die  Familienbeihilfe (FB) und den Kinderabsetzbetrag (KG) bezogen.

**False Positives:**

- `Joachim` — partial — pred is substring of gold: `Joachim Kotmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Joachim Kotmann`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Mit Anträgen, eingegangen am 27.10.2020, hat Frau Franziska Fitzmann (= Beschwerde-führerin, Bf),  geb. 04/1971, die Gewährung der Familienbeihilfe (FB) für sich sowie des Erhöhungsbetrages  zur Familienbeihilfe wegen erheblicher Behinderung "ab Jänner 2015" beantragt (Eigenantrag).

**False Positives:**

- `Franziska` — partial — pred is substring of gold: `Franziska Fitzmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Franziska Fitzmann`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_105`)


Dagegen erhob die Bf. fristgerecht Beschwerde und brachte unter Anführung der  gegenständlichen Geschäftszahl begründend (wörtlich) vor:  „Betrifft: Milderung der Strafe   Sehr geehrte Herr/Frau Frau,  ich habe Ihr Bescheid erhalten und bin gezwungen um eine Milderung anzusuchen.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Dominik Barfusz (= Beschwerdeführerin, Bf) hat für den Sohn A, geb. 06/1997, laufend die  Familienbeihilfe (FB) bezogen.

**False Positives:**

- `Dominik` — partial — pred is substring of gold: `Dominik Barfusz`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dominik Barfusz`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien vom 8. Februar 2024, GZ. MA67/GZ/2023,  wurde Frau Gudrun Joehnk (in weiterer Folge: Beschwerdeführerin) der Begehung einer  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über sie nach § 4 Abs 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von 60,00 Euro verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

**False Positives:**

- `Gudrun` — partial — pred is substring of gold: `Gudrun Joehnk`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien`(organisation)
- `Gudrun Joehnk`(person)

</details>

---

## `Mag.a Pattern` 

**F1:** 0.001 | **Precision:** 0.250 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `06100001`  
**Description:**
Specifically targets the feminine academic title 'Mag.a' followed by a full name.

**Content:**
```
\bMag\.a\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.001 | 0.001 | 4 | 1 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 3 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Feldkirch 1 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Josef Ungericht, den Richter Mag. Armin Treichl und die fachkundigen Laienrichter Mag.a  Patricia Kathan-Simma und Mag. Norbert Metzler in Gegenwart der Schriftführerin Isabella  Alexandra Längle in der Finanzstrafsache gegen VetR Vivian Hirtel, Litzlberger Straße 14, 8530 Kresbach, Österreich, vertreten durch Dr.  jur.

| Predicted | Gold |
|---|---|
| `Mag.a  Patricia Kathan` | `Mag.a  Patricia Kathan` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)
- `Mag. Josef Ungericht` (person)
- `Mag. Armin Treichl` (person)
- `Mag. Norbert Metzler` (person)
- `Isabella  Alexandra Längle` (person)
- `VetR Vivian Hirtel` (person)
- `Litzlberger Straße 14, 8530 Kresbach, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr  in der Beschwerdesache Hon.-Prof.in Techn R Huberta Pauwels,  Oberapping 6, 4613 Unterholz, Österreich, betreffend Beschwerde vom 14. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 76-699/8954, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Mag.a Priv` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`(person)
- `Hon.-Prof.in Techn R Huberta Pauwels`(person)
- `Oberapping 6, 4613 Unterholz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `76-699/8954`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/144771.1`) (sent_id: `deanon_BFG_20260814_TEST/144771.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Annette Wöhrl  in der Beschwerdesache VetR Univ.-Prof. Wigand Gervais,  Lorenzen 10, 6183 Kühtai, Österreich, vertreten durch die Steuerkanzlei Holowinski  Partner KG, Hasenauerstraße  18/1/Top 2, 1190 Wien, über die Beschwerde vom 19. Juli 2023 gegen den Bescheid des  Finanzamtes Österreich vom 19. Mai 2023  betreffend Körperschaftsteuer 2020,  Steuernummer 92-114/1027, zu Recht erkannt:   I. Von der Festsetzung der Körperschaftsteuer 2020 wird gemäß § 206 lit. b BAO Abstand  genommen.

**False Positives:**

- `Mag.a Annette` — partial — pred is substring of gold: `Mag.a Annette Wöhrl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Annette Wöhrl`(person)
- `VetR Univ.-Prof. Wigand Gervais`(person)
- `Lorenzen 10, 6183 Kühtai, Österreich`(address)
- `Steuerkanzlei Holowinski  Partner KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `92-114/1027`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/149310.1`) (sent_id: `deanon_BFG_20260814_TEST/149310.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Beate Gützlaf  in der Beschwerdesache Priv.-Doz.in Alina Vriesman,  Willing 25N, 2561 Pöllau, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 16. Mai 2023, Ordnungsbegriff Nr1, betreffend Abweisung des Antrages auf  Familienbeihilfe für den Zeitraum „April 2023 – September 2023“ zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag.a Beate` — partial — pred is substring of gold: `Mag.a Beate Gützlaf`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Beate Gützlaf`(person)
- `Priv.-Doz.in Alina Vriesman`(person)
- `Willing 25N, 2561 Pöllau, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

</details>

---

## `Anonymized Initials and Digits` 🏆

**F1:** 0.006 | **Precision:** 0.227 | **Recall:** 0.003  

**Format:** `regex`  
**Rule ID:** `adf88ce2`  
**Description:**
Captures anonymized names like 'Dr. F.', 'Dr. Dok2', 'Mag. VV', ensuring they are standalone entities and not part of a full name pattern.

**Content:**
```
\b(?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|RA\.|StB\.)\s+([A-Z]\.?|[A-Z][a-z]+[0-9]+|[A-Z]{2,})(?=,|;|:|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.227 | 0.003 | 0.006 | 22 | 5 | 17 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 5 | 17 | 1609 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_29`)


Dazu wurde eine "Gutachterliche Stellungnahme" des Univ. Prof. Dr. F, Institut für  Humangenetik, vom 27.3.2020 vorgelegt, demnach bei B die Mikrodeletion mit motorischer  und geistiger Entwicklungsstörung seit Geburt vorliege, was sich in dokumentierten  Auffälligkeiten zeige.

| Predicted | Gold |
|---|---|
| `Dr. F` | `Dr. F` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_33`)


"… Zusammenfassung relevanter Befunde …:  2018-01-17 Entwicklungsneurologischer Befund Dr. G  Sie ist viel und schnell gekrabbelt. Der Gehbeginn war verspätet, freies Gehen über längere  Strecken mit 23 LM, erste freie Schritte mit 20 LM.

| Predicted | Gold |
|---|---|
| `Dr. G` | `Dr. G` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_51`)


…  ad 5) Verdeckte Ausschüttung:  Stellungnahme Dr. J:  Der Geschäftsführer gibt bekannt, dass die Miet- bzw. Kostenbeiträge von Herrn D und Herr F  im Jahr 2009 und 2010 ausschließlich deswegen erfolgte, da Investitionen vorgenommen  wurden (wie aus dem AVZ 2009 und 2010 zu ersehen ist).

| Predicted | Gold |
|---|---|
| `Dr. J` | `Dr. J` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_26`)


Infolge sind von Herrn Dr. F Unterlagen - im Begleitschreiben als Gutachten bezeichnet sowie  Mietverträge - per Mail vorgelegt worden.

| Predicted | Gold |
|---|---|
| `Dr. F` | `Dr. F` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_368`)


12.12.2017 11,70 Dr. G FK 7,14  Das Finanzamt beantragt in diesem Punkt die Stattgabe.

| Predicted | Gold |
|---|---|
| `Dr. G` | `Dr. G` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_27`)


Dauerzustand  Gutachten erstellt am 12.3.2020 von Dr.in C  Gutachten vidiert am 13.3.2020 von Dr. E"  4.

**False Positives:**

- `Dr.in C` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_50`)


2018-01-17 Entwicklungspsychologische Untersuchung 3 Jahre 2 Monate:   Mag. D Kognition: B zeigt ein Verständnis für ihr Tun und was sie damit bewirkt.

**False Positives:**

- `Mag. D` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_90`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern:  ja   GdB liegt vor seit: 01/2018  GdB 40 liegt vor seit: 11/2015  Dauerzustand …  Gutachten erstellt am 11.05.2020 von Dr.in C  Gutachten vidiert am 13.05.2020 von Dr. E"  6.

**False Positives:**

- `Dr.in C` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_45`)


Als letzter  Versuch hätte sie auf Empfehlungen Herrn Dr. B, einen anerkannten Schulterspezialisten,  aufgesucht, welcher endlich nach einem langen Leidensweg die richtige Diagnose gestellt und  zu einer sofortigen Operation geraten hätte.

**False Positives:**

- `Dr. B` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Zum Zeitpunkt der Erlassung der beschwerdegegenständlichen Bescheide war über die  Beschwerdeführerin (im Folgenden abgekürzt: Bf) das Konkursverfahren eröffnet  (Masseverwalter: Rechtsanwalt Mag. G H).

**False Positives:**

- `Mag. G` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_19`)


Zum  Masseverwalter wurde Herr Mag. G H bestellt.  Gesellschafter der AB sind Herr C D und die Verlassenschaft nach E F. Geschäftsführer waren  Herr C D und bis zu seinem Tod im Jahr 2011 Herr E F.

**False Positives:**

- `Mag. G` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_15`)


Die Unterlagen [des Bf.] befanden sich in St. Marein,  die Unterlagen von Frau DM bei ihrem Steuerberater, Mag. H, in Graz.

**False Positives:**

- `Mag. H` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_104`)


Im Gesamtaufwand sind folgende Teilpositionen enthalten:   08.03.2017 5,85  Dr. B Notfall Vitamin Cverschreibung FK 7,14   Das Finanzamt beantragt die Stattgabe bezüglich der € 5,85 + € 7,14 = € 12,99.

**False Positives:**

- `Dr. B` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_106`)


€ 12,99 sind eine ag Bel.   10.03.2017 17,45 Dr. B Augentropfen FK 7,14   Das Finanzamt beantragt die Stattgabe für € 6,50 (lt. Beleg Siccaforte).

**False Positives:**

- `Dr. B` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_113`)


20. Apr 0 Dr. B FK 7,14 (Rezept vom 20.04.17, Pilocarpin as u. a.

**False Positives:**

- `Dr. B` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_162`)


Es seien auf der vorgelegten Unterlage „Dr. B  Befunde Lipidwerte und Thrombopenie“ vermerkt.

**False Positives:**

- `Dr. B` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_190`)


23.05.2017 0,00 Dr. W Röntgenüberweisung FK 7,14 (Rezept am 2.05. ausgestellt)

**False Positives:**

- `Dr. W` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_195`)


24.05.2017 0,00 Dr. M Röntgen FK 7,14  Das Finanzamt beantragt die Stattgabe.

**False Positives:**

- `Dr. M` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_198`)


06.07.2017 0,00 Dr. W Physio-Überweisung FK 7,14  Das Finanzamt beantragt die Abweisung, weil die Fahrtkosten doppelt geltend gemacht und an  diesem Tag bei der Ehegattin berücksichtigt werden.

**False Positives:**

- `Dr. W` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_222`)


16.10.2017 0,00 Dr. Dr. E Augenverletzung Leistungsbl.

**False Positives:**

- `Dr. E` — partial — pred is substring of gold: `Dr. Dr. E`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dr. E`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_309`)


23.05.2017 0,00 Dr. W ÜW FK 7,14   24.08.2017 0,00 Dr. W ÜW FK 7,14  14.11.2017 0,00 Dr. W ÜW FK 7,14  06.07.2017 0,00 Dr. W FK 7,14   20.07.2017 0,00 Dr. W ÜW FK 7,14   Das Finanzamt beantragt die Stattgabe.

**False Positives:**

- `Dr. W` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_227`)


Seitens der Bf. wurde ein Privatgutachten von Dipl.Ing. Dr. H, anonymisiert aber mit RV-Zahl,  vorgelegt.

**False Positives:**

- `Dr. H` — partial — pred is substring of gold: `Dipl.Ing. Dr. H`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.Ing. Dr. H`(person)

</details>

---

## `Name with Suffix Pattern` 💣

**F1:** 0.002 | **Precision:** 0.154 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `9f2317f4`  
**Description:**
Captures full names followed by academic/professional suffixes like ', LLM', ', MSc', ', Bakk.', ', LL.B.', ', LL.M.' which are often missed by title-based rules. Ensures the match starts with a capitalized letter.

**Content:**
```
\b[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+(?:,\s+(?:LLM|MSc|MBA|Bakk\. iur\. |Bakk\. phil\. |Bakk\. rer\. nat\. |Bakk\. art\. |LL\.B\. |LL\.M\.))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.154 | 0.001 | 0.002 | 13 | 2 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 11 | 1612 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen Hademar Sachteleben, MSc, Fröhlichgasse 31, 3244 Hofstetten, Österreich, über die zwei Beschwerden des  Beschuldigten gegen die nachfolgend angeführten zwei Vollstreckungsverfügungen (VVF) des  Magistrates der Stadt Wien, jeweils betreffend Zwangsvollstreckung wegen Nichtbezahlung  der rechtskräftigen Strafe auf Grund des nachfolgend angeführten Erkenntnis des  Bundesfinanzgerichtes, jeweils betreffend eine Verwaltungsübertretung nach § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006,

| Predicted | Gold |
|---|---|
| `Hademar Sachteleben, MSc` | `Hademar Sachteleben, MSc` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andrea Müller-Dobler MBA MSc` (person)
- `Fröhlichgasse 31, 3244 Hofstetten, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)
- `Bundesfinanzgerichtes` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/148878.1`) (sent_id: `deanon_BFG_20260814_TEST/148878.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter RI in der Verwaltungsstrafsache gegen  Stephanie Bermann, LLM, Tomandlried 83, 9111 Niedertrixen, Österreich, über die Beschwerde vom 20. März 2025 gegen den  Zurückweisungsbescheid des Magistrates der Stadt Wien vom 17. März 2025, Zahl:  MA67/111111/2024, mit dem der Einspruch vom 18. Februar 2025 gegen die Strafverfügung  vom 12. November 2024 mit derselben Geschäftszahl gemäß § 49 Abs. 1 VStG als verspätet  zurückgewiesen wurde, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  der angefochtene Zurückweisungsbescheid bestätigt.

| Predicted | Gold |
|---|---|
| `Stephanie Bermann, LLM` | `Stephanie Bermann, LLM` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tomandlried 83, 9111 Niedertrixen, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Simone Zemanek, MSc, Almbachstraße 3, 8673 Filzmoos, Österreich, über die Beschwerde vom 2. April 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 13. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 15-763/9594  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache  Simone Zemanek, MSc` — partial — gold is substring of pred: `Simone Zemanek, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Susanne Haim`(person)
- `Simone Zemanek, MSc`(person)
- `Almbachstraße 3, 8673 Filzmoos, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)
- `15-763/9594`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/136154.1`) (sent_id: `deanon_BFG_20260814_TEST/136154.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Rut Schattel  in der Beschwerdesache des  Stanley Wachenschwanz, Bakk. rer. nat. Bf1-Adr***RA über die Beschwerde vom 19. Oktober 2016 gegen die Bescheide  des Finanzamtes X vom 28. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für die Jahre 2012 und 2013 zu Recht erkannt:     I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Stanley Wachenschwanz, Bakk. rer. nat. ` — partial — gold is substring of pred: `Stanley Wachenschwanz, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Rut Schattel`(person)
- `Stanley Wachenschwanz, Bakk. rer. nat.`(person)
- `Finanzamtes`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Günter Narat über die Beschwerde  vom 7. Mai 2021 der Beschwerdeführerin Liu Maackens, LLM Bakk. techn., Alfons-Petzold-Hof 4, 2042 Grund, Österreich  vertreten durch die mit  Zustellvollmacht ausgewiesene WTGL Wirtschaftstreuhand – Steuerberatungs-GmbH & Co KG,  Blumauerstraße 35, 4020 Linz, gegen den Bescheid des Finanzamtes Österreich vom 8. April  2021 betreffend Abweisung des Antrages auf Wiedereinsetzung in den vorigen Stand gem. §  308 BAO betreffend Erklärung des Widerrufs des Regelbesteuerungsantrages gem. § 6 Abs 3  UStG 1994  zu Recht:    I)  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Liu Maackens, LLM` — partial — pred is substring of gold: `Liu Maackens, LLM Bakk. techn.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Günter Narat`(person)
- `Liu Maackens, LLM Bakk. techn.`(person)
- `Alfons-Petzold-Hof 4, 2042 Grund, Österreich`(address)
- `WTGL Wirtschaftstreuhand – Steuerberatungs-GmbH & Co KG`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Ronja Oberth, LLM, Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich, vertreten durch Hofer Leitinger Steuerberatung  GmbH, Hauptstraße 86, 8582 Rosental/Kainach, über die Beschwerde vom 24. Juni 2022 gegen  den Bescheid des Finanzamtes Österreich vom 1. Juni 2022 betreffend Einkommensteuer 2020  (Steuernummer 59-245/3703 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Beschwerdesache Ronja Oberth, LLM` — partial — gold is substring of pred: `Ronja Oberth, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ronja Oberth, LLM`(person)
- `Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich`(address)
- `Hofer Leitinger Steuerberatung  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `59-245/3703`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/142762.1`) (sent_id: `deanon_BFG_20260814_TEST/142762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Beschwerdesache Heinrich Rzeppa, LLM, Toulagasse 1, 8111 Straßengel, Österreich, vertreten durch Dr. Martin Weiser, Landstraßer  Hauptstraße 60, 1030 Wien, über die Beschwerde vom 04. März 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 31. Jänner 2019 betreffend Umsatzsteuer 2016, Steuernummer  52-580/0972  beschlossen:  I. Die Parteien werden gem. § 281a BAO formlos darüber verständigt, dass nach Auffassung des  Verwaltungsgerichts noch eine Beschwerdevorentscheidung zu erlassen ist.

**False Positives:**

- `Beschwerdesache Heinrich Rzeppa, LLM` — partial — gold is substring of pred: `Heinrich Rzeppa, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karoline Windsteig`(person)
- `Heinrich Rzeppa, LLM`(person)
- `Toulagasse 1, 8111 Straßengel, Österreich`(address)
- `Dr. Martin Weiser`(person)
- `Finanzamtes Wien 4/5/10`(organisation)
- `52-580/0972`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Volkmar Bauernschmid, MBA, Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich  vertreten durch Securitas Revisions- und  Treuhandgesellschaft m.b.H., Porzellangasse 51, 1090 Wien und Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 19.  Mai 2021 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 25. März 2021 die  Umsatzsteuer 2012-2014 betreffend (Steuernummer 78-200/9325) nach Durchführung  einer mündlichen Verhandlung am 24. November 2023 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Beschwerdesache Volkmar Bauernschmid, MBA` — partial — gold is substring of pred: `Volkmar Bauernschmid, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Volkmar Bauernschmid, MBA`(person)
- `Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich`(address)
- `Securitas Revisions- und  Treuhandgesellschaft m.b.H.`(organisation)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `78-200/9325`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_1`)


IM NAMEN DER REPUBLI K  A) Das Bundesfinanzgericht hat durch den Richter Mag. Christian Seywald in der  Beschwerdesache Olga Kendziora, Bakk. rer. nat. (Beschwerdeführerin, abgekürzt: Bf.), Im Biofeld 5, 6650 Gramais, Österreich  vertreten  durch Stb1, AdrStb1, über die Beschwerde der Bf. vom 16. März 2017 gegen folgende  Bescheide des Finanzamtes Wien99 (ursprünglich belangte Behörde) zu Steuernummer  56-003/0284    Umsatzsteuerbescheid 2014 vom 23. September 2016,   Körperschaftsteuerbescheid 2014 vom 23. September 2016,   Bescheid über die Festsetzung von Anspruchszinsen 2014 vom 23. September 2016,   Haftungsbescheid für den Zeitraum 2014 betreffend Kapitalertragsteuer vom  22. September 2016,   Körperschaftsteuervorauszahlungsbescheid 2016 vom 23. September 2016,  nach Durchführung der beantragten mündlichen Verhandlung am 25. April 2025 in  Anwesenheit des Schriftführers F  a) zu Recht erkannt:  Der Beschwerde wird, soweit sie gegen den Körperschaftsteuerbescheid 2014 vom  23. September 2016 gerichtet ist, Folge gegeben.

**False Positives:**

- `Beschwerdesache Olga Kendziora, Bakk. rer. nat. ` — partial — gold is substring of pred: `Olga Kendziora, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Christian Seywald`(person)
- `Olga Kendziora, Bakk. rer. nat.`(person)
- `Im Biofeld 5, 6650 Gramais, Österreich`(address)
- `Finanzamtes`(organisation)
- `56-003/0284`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_13`)


Die beschwerdeführende Olga Kendziora, Bakk. rer. nat. (Beschwerdeführerin, abgekürzt: Bf.),  Firmenbuchnummer FN 1, hat Frau A als alleinige Geschäftsführerin und Frau C B als alleinige  Gesellschafterin (Firmenbuchauszug: BFG-Akt I zu GZ. RV/7102163/2018, Bl. 107)  2)

**False Positives:**

- `Olga Kendziora, Bakk. rer. nat. ` — partial — gold is substring of pred: `Olga Kendziora, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Olga Kendziora, Bakk. rer. nat.`(person)
- `BFG`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_26`)


In dieser Niederschrift sagt Herr X aus, dass es sich bei den  gelegten Rechnungen an Olga Kendziora, Bakk. rer. nat.  um Scheinrechnungen handelt.  ´...Die mir vorgelegten Rechnungen an die Olga Kendziora, Bakk. rer. nat.  wurden von mir auf Wunsch der  Olga Kendziora, Bakk. rer. nat., Frau B, ausgestellt. Ich habe die angeführten Leistungen nicht erbracht, es handelt  sich um Scheinrechnungen.´“  Anm.: Die Höhe der KESt wurde seitens des Finanzamtes später neuberechnet (BFG-Akt I  Bl. 137; vgl. auch Abschnitt 8/1 betr.

**False Positives:**

- `Olga Kendziora, Bakk. rer. nat. ` — partial — gold is substring of pred: `Olga Kendziora, Bakk. rer. nat.`
- `Olga Kendziora, Bakk. rer. nat. ` — similar text (different position): `Olga Kendziora, Bakk. rer. nat.`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Olga Kendziora, Bakk. rer. nat.`(person)
- `Olga Kendziora, Bakk. rer. nat.`(person)
- `Olga Kendziora, Bakk. rer. nat.`(person)
- `Finanzamtes`(organisation)
- `BFG`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/148878.1`) (sent_id: `deanon_BFG_20260814_TEST/148878.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 12.  November 2024, Zahl: MA67/111111/2024, wurde über die beschwerdeführende Partei  Stephanie Bermann, LLM  wegen einer Verwaltungsübertretung nach § 3 Abs. 1 Wiener  Kontrolleinrichtungenverordnung in Verbindung mit § 4 Abs. 3 Wiener Parkometergesetz 2006  eine Geldstrafe in der Höhe von € 75,00 und eine Ersatzfreiheitsstrafe von 17 Stunden  verhängt.

**False Positives:**

- `Partei  Stephanie Bermann, LLM` — partial — gold is substring of pred: `Stephanie Bermann, LLM`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stephanie Bermann, LLM`(person)

</details>

---

## `Von Name Context` 💣

**F1:** 0.002 | **Precision:** 0.062 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `c3b3c998`  
**Description:**
Captures names following the preposition 'von' (e.g., 'von [Name]'), ensuring full name capture including titles if present.

**Content:**
```
\bvon\s+((?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|RA\.|StB\.|Prof\.in|Prof\.|VetR|Hon\.-Prof\.|Hon\.-Prof\.in|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|OMedR|Univ\.-Prof\.|Univ\.-Prof\.in)\s+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+|[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.062 | 0.001 | 0.002 | 32 | 2 | 30 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 30 | 1612 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_116`)


Laut vorgelegtem Gutachten von Nicola Peterhansel  Fachärztin für Psychiatrie, vom 7. Jänner 2019, leidet  der Bf. an einer Intelligenzminderung mit einer ausgeprägten Lese- und Rechenschwäche und  kann auf Grund des vorliegenden Krankheitsbildes weder Vertragsinhalte richtig erfassen,  11 von 13 Seite 12 von 13

| Predicted | Gold |
|---|---|
| `Nicola Peterhansel` | `Nicola Peterhansel` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_26`)


Der Sohn der Bf. wurde am 22. Februar 2023 von Annette Weutscheck  Fachärztin für Neurologie,  untersucht und folgendes Gutachten erstellt:  Anamnese:  Intelligenzminderung, ADHS   Die letzte Begutachtung erfolgte am 23.11.2021, da keine aktuellen Befunde vorgelegt wurden,  konnte kein GdB ermittelt werden.

| Predicted | Gold |
|---|---|
| `Annette Weutscheck` | `Annette Weutscheck` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_28`)


Betreffend die Baurechtseinlage EZ 2 KG XY) wurde mit Schreiben vom 5.4.2017 von Notar Herr  Mag. Z die Befreiung gemäß § 3 Abs. 1 Z 2 GrEStG (damals fälschlicherweise die Befreiung  gemäß § 3 Abs. 1 Z 3 GrEStG bezeichnet) beantragt.

**False Positives:**

- `Notar Herr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Z`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_90`)


Die Bf ist von Beruf Hausfrau, bezieht keine eigenen Einkünfte und  verfügte über ein Haushaltsgeld vom Ehegatten von mtl. rund € 1.200, womit sie die  Lebenshaltungskosten für sich und die beiden Kinder bestritten hat.

**False Positives:**

- `Beruf Hausfrau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_37`)


erstellt am 2014-07-07 von Matulla Bettina  Facharzt für Neurologie  zugestimmt am 2014-07-07  Leitender Arzt: Fürthaler Wolfgang"

**False Positives:**

- `Matulla Bettina` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_119`)


30.4.2003, 99/13/0251)  schließt sich das Bundesfinanzgericht der vom Finanzamt in der Beschwerdevorentscheidung  vertretenen Auffassung bezüglich der Kosten für Literatur, in Bezug auf das Arbeitszimmer  (anteilige Kosten für Strom und Telefon) sowie der sonstigen beantragten Werbungskosten  (Deko, Eimer, DVDs, Kreditkartenetui, Privatanteil von Microsoft Office, Tinten Canon..) an.

**False Positives:**

- `Microsoft Office` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Finanzamt`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

**False Positives:**

- `Frau Nina Rasem` — partial — gold is substring of pred: `Nina Rasem`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Nina Rasem`(person)
- `An der Walk 32, 9560 Persching, Österreich`(address)
- `An der Walk 32, 9560 Persching, Österreich`(address)
- `Mag. Peter  Mayerhofer`(person)
- `Magistrates  der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_44`)


Betreffend die Beschwerdegründe verweisen wir einerseits auf die bisherigen Ausführungen in  der Beschwerde und andererseits auf die noch nicht erwähnte Auskunft von Herrn Dimitri Witkoski der  in Rücksprache mit Herrn Ruckelshaußen stand.

**False Positives:**

- `Herrn Dimitri` — positional overlap with gold: `Dimitri Witkoski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dimitri Witkoski`(person)
- `Ruckelshaußen`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_86`)


Bei diesen Pooled Jackpot-Varianten kommt noch hinzu, dass der Jackpot nur einem Kunden,  der bei einem einzigen Internet Gaming Provider (z.B Oswald Rübberdt) registriert ist, ausbezahlt wird,  wohingegen die Jackpot Einzahlungen durch eine Mehrzahl von Internet Gaming Providern  erfolgen.

**False Positives:**

- `Internet Gaming` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Oswald Rübberdt`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_97`)


Ich möchte das mit einem starken und kompetenten Team tun und  ich freue mich daher, dass ich mit Martin Kocher einen zusätzlichen Topexperten für unser  Team gewinnen konnte", sagte Bundeskanzler Sebastian Kurz bei der Präsentation des  Nachfolgers von Arbeitsministerin Christine Aschbacher im Bundeskanzleramt.

**False Positives:**

- `Arbeitsministerin Christine` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_14`)


Die nachfolgenden Ausgaben (€ 45.491,87) wurden vom Bf. im Zusammenhang mit seiner als  Gewerbebetrieb angegebenen Tätigkeit 2009-2016 geltend gemacht:   2009  Buch/CD von Wim Luijpers  Seminarkosten inkl. Flüge, Fahrtkosten, Hotel, Diäten, Anzahlungen  2010  Seminarkosten inkl. Fahrtkosten, Hotel und Diäten   Ausbildungsgebühr, Hotel, Fahrtkosten, Diäten  Mp3-Player (gebraucht)

**False Positives:**

- `Wim Luijpers` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_54`)


Der Verzicht wurde somit vom steuerlichen  Vertreter - auch im Namen von Herrn Jeanne Kraenzlin - abgegeben.

**False Positives:**

- `Herrn Jeanne` — positional overlap with gold: `Jeanne Kraenzlin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeanne Kraenzlin`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_57`)


Im Übrigen wird noch darauf verwiesen, dass im Zuge der Niederschrift zur  Schlussbesprechung vom steuerlichen Vertreter erklärt wurde, dass die Kapitalertragsteuer  (KESt) von den Gesellschaftern (somit auch von Herrn Jeanne Kraenzlin) getragen wird.

**False Positives:**

- `Herrn Jeanne` — positional overlap with gold: `Jeanne Kraenzlin`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Jeanne Kraenzlin`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_51`)


In ihrer Anwortnote vom 14.2.2023 führt die belangte Behörde u.a. aus:  „Nachschauergebnis:  Im Rahmen der Nachschau wurden die mittlerweile rechtskräftig gewordenen  Umsatzsteuerbescheide der Jahre 2015 und 2016 von Wien Consud AG abgefragt.

**False Positives:**

- `Wien Consud` — partial — pred is substring of gold: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_59`)


Diese konnten mit den von Wien Consud AG erklärten Beträgen  abgestimmt werden und ergaben deren korrekte Erfassung in der KZ029.

**False Positives:**

- `Wien Consud` — partial — pred is substring of gold: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_63`)


Im Zusammenhang zum gegenständlichen fortgesetzten Verfahren führte die steuerliche  Vertreterin u.a. Folgendes aus:  „…  Bezugnehmend auf Ihre Email vom 4.1.2023 können wir Sie nach Rücksprache mit unserer  Mandantschaft wie folgt informieren:  Nach Maßgabe des Urteils des VwGH vom 19.10.2022, Ro 2021/15/0034 wurde das Erkenntnis  des BFG zur Gänze wegen Rechtswidrigkeit des Inhalts aufgehoben, sodass nun die  ursprüngliche Rechtslage nach der vom Finanzamt ausgestellten Bescheide für die Jahre 2015  und 2016 wieder gilt. Die Rechtslage aufgrund dieser Bescheide des Finanzamts, in welchen die  Feststellungen der Betriebsprüfung eingearbeitet wurden, ist dergestalt, dass der  Vorsteuerabzug aus den Rechnungen von Wien Consud AG gewährt und auch nicht von der Behörde  beanstandet wurde und fiktive innergemeinschaftliche Erwerbe (ohne Vorsteuerabzug)  aufgrund der Verwendung der österreichischen UID-Nummer festgesetzt wurden.

**False Positives:**

- `Wien Consud` — partial — pred is substring of gold: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Finanzamt`(organisation)
- `Wien Consud AG`(organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_64`)


Die gegen  diese Rechtauffassung eingebrachte Beschwerde richtete sich gegen die Festsetzung der  fiktiven innergemeinschaftlichen Erwerbe, da diese – wie nun auch vom VwGH unter  Bezugnahme auf die Rechtsprechung des EuGH bestätigt – rechtswidrig war, weil die  Lieferungen von Wien Consud AG nicht steuerbefreit waren.

**False Positives:**

- `Wien Consud` — partial — pred is substring of gold: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_66`)


Wenn nunmehr das BFG – obwohl weder von der  belangten Behörde noch von der Beschwerdeführerin beanstandet – die Rechtsmeinung  vertritt, dass der Vorsteuerabzug aus den Eingangsrechnungen von Wien Consud AG zu verneinen sei und  insoweit eine Verböserung vornimmt, ist seitens der Beschwerdeführerin beabsichtigt, den  Instanzenzug zu beschreiten, und zwar aus folgenden Gründen:  Anders als in ihrer Email angeführt ist der Entscheidung des VwGH an keiner Stelle zu  5 von 18 Seite 6 von 18

**False Positives:**

- `Wien Consud` — partial — pred is substring of gold: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG`(organisation)
- `Wien Consud AG`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_67`)


entnehmen, dass die Rechtsansicht, wonach der Vorsteuerabzug aus den Eingangsrechnungen  von Wien Consud AG zu versagen sei, geteilt wird.

**False Positives:**

- `Wien Consud` — partial — pred is substring of gold: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_68`)


Auch hat der VwGH oder der EuGH bisher zu einem wie  dem hier vorliegenden Sachverhalt, bei dem einerseits eine innergemeinschaftliche Lieferung  aufgrund der Mitteilung einer inländischen UID-Nummer als steuerpflichtig behandelt wurde  (bzw. werden musste) und andererseits ein fiktiver ig Erwerb vorgeschrieben wurde, nicht  explizit zur Frage des Vorsteuerabzuges für die als steuerpflichtig behandelte Lieferung  geurteilt, sodass genau zu dieser Frage einschlägige Rechtsprechung durch den VwGH und  EuGH fehlt. Denn auch wenn es sich bei den Lieferungen von Wien Consud AG (A) um  innergemeinschaftliche Lieferungen handelt, die bei Vorliegen aller Voraussetzungen  grundsätzlich hätten steuerbefreit sein können, bedeutet dies nicht, dass diese im konkreten  auch steuerbefreit waren und somit zu Unrecht österreichische Umsatzsteuer von Wien Consud AG in  Rechnung gestellt wurde, für die kein Recht auf Vorsteuerabzug besteht.

**False Positives:**

- `Wien Consud` — partial — pred is substring of gold: `Wien Consud AG`
- `Wien Consud` — similar text (different position): `Wien Consud AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)
- `Wien Consud AG`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/141058.1`) (sent_id: `deanon_BFG_20260814_TEST/141058.1_76`)


Wie oben bereits ausgeführt, wurde gegen die Festsetzung der sog. fiktiven ig Erwerbe  Beschwerde eingebracht und wurde die der Beschwerde zugrundeliegende Ansicht, dass eine  Festsetzung im vorliegenden Sachverhalt (bei der die Lieferungen von Wien Consud AG nicht steuerbefreit  wurden) nicht rechtmäßig ist, vom VwGH bestätigt.

**False Positives:**

- `Wien Consud` — partial — pred is substring of gold: `Wien Consud AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wien Consud AG`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/141300.1`) (sent_id: `deanon_BFG_20260814_TEST/141300.1_26`)


Der Bf. wiederholt in seiner Beschwerde vom 26. Mai 2023 (E-Mail) sein Einspruchsvorbringen  und übermittelte erneut eine Bestätigung von Langeheinrich Holz GmbH  wonach der Bf. am Beanstandungstag  um 21:21 Uhr an der Adresse 1230 Wien, Gasse, mit dem Ausliefern von Paketen im Auftrag  von Amazon beschäftigt war.

**False Positives:**

- `Langeheinrich Holz` — partial — pred is substring of gold: `Langeheinrich Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Langeheinrich Holz GmbH`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_28`)


Im Zuge des Ermittlungsverfahrens wurde festgestellt, dass der aktuelle Hauptwohnsitz von  Herrn Sohn, geb. am 25.gggg.1981, seit 03.bbb.2013 in Adresse_Sohn, ist.“

**False Positives:**

- `Herrn Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

**False Positives:**

- `Herrn Quentin` — positional overlap with gold: `Quentin Schwartkopp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Quentin Schwartkopp`(person)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

**False Positives:**

- `Herrn Quentin` — positional overlap with gold: `Quentin Schwartkopp`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Zollamt`(organisation)
- `Quentin Schwartkopp`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Groschedl über die  Beschwerde von Frau Theodora Berenwinkel, Klam 26, 8673 Steinhöf, Österreich, vom 12. Februar 2024, gegen die zwei  Straferkenntnisse der belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67,  als Abgabenstrafbehörde (beide) vom 30. Jänner 2024, GZen 1) MA67/GZ1/2023 und 2)  MA67/GZ2/2023, beide wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für Wien Nr.  9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise stattgegeben, als die verhängten Geldstrafen von jeweils 40,00 Euro auf jeweils  30,00 Euro und die für den Fall der Uneinbringlichkeit festgesetzten Ersatzfreiheitsstrafen von  jeweils 9 auf jeweils 7 Stunden herabgesetzt werden.

**False Positives:**

- `Frau Theodora Berenwinkel` — partial — gold is substring of pred: `Theodora Berenwinkel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gerhard Groschedl`(person)
- `Theodora Berenwinkel`(person)
- `Klam 26, 8673 Steinhöf, Österreich`(address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_46`)


Zum Audi:  „Ich lege der Beschwerde den Kaufvertrag vom 23.1.2020, den Zulassungsschein, den  Datenauszug von Porsche Austria, die Ausweiskopie des Käufers aus Ungarn, 9 Fotos des  Fahrzeuges beim Kauf und beim Verladen auf den in Ungarn zugelassenen Anhänger des  Käufers und 2 Fotos des Fahrzeuges im jetzigen Zustand bei.

**False Positives:**

- `Porsche Austria` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_76`)


Der Tochter wurden für den 1. Studienabschnitt am 5.10.2017 € 945,-- als  Multimedia Pauschale für die Medienkoffer „Privatrecht I“, „Öffentliches Recht I“, „Römisches  Recht“, „Rechtsgeschichte“ und Strafrecht I“ von Multimediale Studienmaterialien GmbH in  Rechnung gestellt.   2. Beweiswürdigung  Die Feststellungen hinsichtlich der Erwerbsminderung, des Bezuges der erhöhten Familien- beihilfe und der Pflegegeldstufe betreffend die Tochter sind unstrittig und konnte sich das  Bundesfinanzgericht diesen Ansichten bedenkenlos anschließen.

**False Positives:**

- `Multimediale Studienmaterialien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_429`)


Zur Verrechenbarkeit und Absetzbarkeit von Investitionen  Der Behauptung der beschwerdeführenden Partei, eine mangelnde Verrechenbarkeit mit  verbundenen Unternehmen und die Regelung des § 4 EKBSG (zur Absetzbarkeit von  Investitionen) sei realitätsfern, muss entgegnet werden, dass die beschwerdeführende Partei  nicht substantiiert dargelegt hat, welche unterschiedlich hohen Investitions- und  Betriebskosten die beschwerdeführende Partei im Vergleich zu anderen Stromerzeugern  benachteiligen.

**False Positives:**

- `Investitionen  Der` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_429`)


Zur Verrechenbarkeit und Absetzbarkeit von Investitionen  Der Behauptung der beschwerdeführenden Partei, eine mangelnde Verrechenbarkeit mit  verbundenen Unternehmen und die Regelung des § 4 EKBSG (zur Absetzbarkeit von  Investitionen) sei realitätsfern, muss entgegnet werden, dass die beschwerdeführende Partei  nicht substantiiert dargelegt hat, welche unterschiedlich hohen Investitions- und  Betriebskosten die beschwerdeführende Partei im Vergleich zu anderen Stromerzeugern  benachteiligen.

**False Positives:**

- `Investitionen  Der` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_277`)


Die Angaben von Herrn Baumeister Y X werden nicht zur Sachverhaltsfeststellung  herangezogen, weil sie nach der hier vertretenen Auffassung nicht relevant sind und jedenfalls  unzuverlässig sind, wie auch im Detail in Abschnitt 14 dargestellt wird.

**False Positives:**

- `Herrn Baumeister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Richter/Richterin Context` 💣

**F1:** 0.001 | **Precision:** 0.036 | **Recall:** 0.001  

**Format:** `regex`  
**Rule ID:** `dce24f2a`  
**Description:**
Targets judges mentioned after 'durch den Richter' or 'durch die Richterin', explicitly allowing hyphenated surnames and specific titles.

**Content:**
```
(?:durch den Richter|durch die Richterin)\s+((?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|Univ\.-Prof\.|Univ\.-Prof\.in|Priv\.-Doz\.|Priv\.-Doz\.in|Prof\.in|Prof\.|VetR|Hon\.-Prof\.|Hon\.-Prof\.in|MedR|KommR|Ing\.|Bakk\. iur\.|LLM|MBA|RA\.?|StB\.?|Gf-?|\u00d6kR|Dipl\.-Ing\.|Dipl\. Kff\. StR|StR|OMedR|KR\s+Ing\.|Techn\s+R)(?:[ ]+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:[ ]+[A-Z][a-z]+)+)+|[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:[ ]+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.036 | 0.001 | 0.001 | 28 | 1 | 27 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 27 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125880.1`) (sent_id: `deanon_BFG_20260814_TEST/125880.1_2`)


Das Bundesfinanzgericht hat durch den Richter Alexander Schnelldorfer in der Beschwerde-sache A-KG, vertreten durch C, gegen den am 7. Juni 2010 ausgefertigten Bescheid der belangten Behörde Finanzamt B betreffend Umsatzsteuer 2008 und den von derselben Behörde mit gleichem Datum ausgefertigten Bescheid über die Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2008 zu Recht erkannt:  I.     Der Bescheid betreffend Umsatzsteuer 2008 wird abgeändert.

| Predicted | Gold |
|---|---|
| `Alexander Schnelldorfer` | `Alexander Schnelldorfer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamt` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Lewis Rzehula`(person)
- `Neustädterstraße 3, 9560 Wabl, Österreich`(address)
- `43-839/6567`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Roxana Dellner`(person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich`(address)
- `RA Mag. Robert Bitsche`(person)
- `Magistrats der Stadt Wien`(organisation)
- `88-034/0292`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130379.1`) (sent_id: `deanon_BFG_20260814_TEST/130379.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache VetR OMedR Constantin Wiedewilt, Furtgasse 15, 3204 Kirchberggegend, Österreich, vertreten durch INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft m.b.H., Hauptplatz 7, 3430 Tulln, über  die Beschwerden gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg Tulln  betreffend Umsatzsteuer 2014 bis 2016 und über den Vorlageantrag vom 24. Juli 2019  betreffend Umsatzsteuer 2013 und 2017, Steuernummer ,   I. zu Recht erkannt:   Den Beschwerden gegen die Bescheide betreffend Umsatzsteuer 2014 bis 2016 wird gemäß  § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `VetR OMedR Constantin Wiedewilt`(person)
- `Furtgasse 15, 3204 Kirchberggegend, Österreich`(address)
- `INTER-TREUHAND PRACHNER  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Hollabrunn Korneuburg Tulln`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache StR Mag. Dirk Bröders, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `StR Mag. Dirk Bröders`(person)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `77-629/3506`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag.a Caroline Schr` — partial — pred is substring of gold: `Mag.a Caroline Schröer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Caroline Schröer`(person)
- `Charlotte Beha`(person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich`(address)
- `Finanzamtes Salzburg-Stadt`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Hartwig Simonson, Neubruchgasse 122L, 9562 Flatschach, Österreich, über die Beschwerde vom 11. Februar 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 11. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und die Beschwerde vom 7. März 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 8. Februar 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Hartwig Simonson`(person)
- `Neubruchgasse 122L, 9562 Flatschach, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamtes`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Ing. OSR Julia Strutwolf`(person)
- `Emmat 72, 9063 Wrießnitz, Österreich`(address)
- `Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/134752.1`) (sent_id: `deanon_BFG_20260814_TEST/134752.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch die Richterin Mag. Anna Mechtler-Höger im  Beschwerdeverfahren über die Beschwerde der Michael Klingsohr, Hochburg 78, 4363 Pabneukirchen, Österreich, vom 09. Dezember  2016 gegen den Bescheid des Magistrats der Stadt Wien, Magistratisches Bezirksamt für den  13./14.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Michael Klingsohr`(person)
- `Hochburg 78, 4363 Pabneukirchen, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

**False Positives:**

- `Dr.in Alice Sch` — partial — pred is substring of gold: `Dr.in Alice Schöpfel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Alice Schöpfel`(person)
- `Walter Guggenmoos`(person)
- `Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich`(address)
- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH`(organisation)
- `Finanzamtes Innsbruck`(organisation)
- `Finanzamt Österreich`(organisation)
- `79-464/0427`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Revisionssache  Basil Vanak, Oberhof 221, 8345 Trössing, Österreich, über den Antrag des Finanzamtes für Großbetriebe, der zur Zahl  RR/7100124/2021 protokollierten außerordentlichen Revision gegen das Erkenntnis des BFG  vom 24.08.2021, RV/7101805/2021, betreffend   KESt-Rückzahlung gemäß § 21 Abs. 1 Z. 1a KStG 1988 die aufschiebende Wirkung  zuzuerkennen, beschlossen:  Dem Antrag der Revisionswerberin wird stattgegeben und die aufschiebende Wirkung  gemäß § 30 Abs. 2 VwGG zuerkannt.

**False Positives:**

- `Mag. Dieter Fr` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Basil Vanak`(person)
- `Oberhof 221, 8345 Trössing, Österreich`(address)
- `Finanzamtes für Großbetriebe`(organisation)
- `BFG`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Juri Siebgen, Josef Maurergasse 2, 5424 Riedl, Österreich, vertreten durch MITTEREGGER Steuerberatungs  GmbH, Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 13. Mai 2018 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich) vom  13. April 2018 betreffend Einkommensteuer 2017 Steuernummer 35-670/1415, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Judith Daniela Herdin` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Juri Siebgen`(person)
- `Josef Maurergasse 2, 5424 Riedl, Österreich`(address)
- `MITTEREGGER Steuerberatungs  GmbH`(organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Österreich`(organisation)
- `35-670/1415`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/135477.1`) (sent_id: `deanon_BFG_20260814_TEST/135477.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Waltraud Pantermühl   in der Beschwerdesache der Kindsfater Telekom, Pirquethof 3, 8662 Lutschaun, Österreich, vertreten durch SIGNUM Treuhand  Steuerberatungs-GmbH, Rohrbach 25, 6850 Dornbirn,  betreffend den Bescheid des Finanzamt Graz-Stadt  vom 14. September 2021  hinsichtlich Zwangsstrafen 2021, Steuernummer 11-834/0873,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Mag.a Waltraud Panterm` — partial — pred is substring of gold: `Mag.a Waltraud Pantermühl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Waltraud Pantermühl`(person)
- `Kindsfater Telekom`(organisation)
- `Pirquethof 3, 8662 Lutschaun, Österreich`(address)
- `SIGNUM Treuhand  Steuerberatungs-GmbH`(organisation)
- `Finanzamt Graz-Stadt`(organisation)
- `11-834/0873`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/137635.1`) (sent_id: `deanon_BFG_20260814_TEST/137635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Valerius Frühmark  in der Beschwerdesache Hon.-Prof. Sven Corbin,  Stalderhaus 7, 9363 Feistritz, Österreich, über die Beschwerde vom 23. Juli 2021 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juli 2021 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum Juni 2018 bis Jänner 2019, SVNr [SVNR],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz. Valerius Fr` — partial — pred is substring of gold: `Priv.-Doz. Valerius Frühmark`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Valerius Frühmark`(person)
- `Hon.-Prof. Sven Corbin`(person)
- `Stalderhaus 7, 9363 Feistritz, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Gotthard Kirchhoffs, Unterriese 2, 7432 Oberschützen, Österreich, vertreten durch WWV-GROUP  SteuerberatungsGmbH, Bahnhofstraße 4, 3950 Gmünd, über die Beschwerde vom  28. September 2021 gegen die Bescheide des Finanzamtes Österreich vom 7. Juli 2021  betreffend Haftung für Lohnsteuer, Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag  für die Jahre 2015 bis 2019, Steuernummer 19-927/9012, zu Recht erkannt:   I. Der Beschwerde gegen die Bescheide betreffend Festsetzung des Zuschlags zum  Dienstgeberbeitrag 2015 bis 2019 wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Gotthard Kirchhoffs`(person)
- `Unterriese 2, 7432 Oberschützen, Österreich`(address)
- `WWV-GROUP  SteuerberatungsGmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `19-927/9012`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Philippa Beßerdich  in der Beschwerdesache des DI  Simone Philipzig, Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich, vertreten durch Hofer Leitinger Steuerberatung GmbH,  Geidorfgürtel 20, 8010 Graz, über die Beschwerde vom 8. September 2021 gegen den Bescheid  des FA Kirchdorf Perg Steyr  vom 9. Juli 2021 betreffend Einkommensteuer 2019 zur Steuernummer  59-060/2086  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag.a Philippa Be` — partial — pred is substring of gold: `Mag.a Philippa Beßerdich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Mag.a Philippa Beßerdich`(person)
- `Simone Philipzig`(person)
- `Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich`(address)
- `Hofer Leitinger Steuerberatung GmbH`(organisation)
- `FA Kirchdorf Perg Steyr`(organisation)
- `59-060/2086`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/140490.1`) (sent_id: `deanon_BFG_20260814_TEST/140490.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Dipl.-Ing. Milena Panagiotoglou, KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich, über die Beschwerde vom 11. September 2022  gegen den Bescheid des Finanzamtes Österreich vom 6. September 2022 betreffend  Einkommensteuer 2017 (Arbeitnehmerveranlagung) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Dipl.-Ing. Milena Panagiotoglou`(person)
- `KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/140602.1`) (sent_id: `deanon_BFG_20260814_TEST/140602.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der Ver- waltungsstrafsache gegen StR Frederike Dalek, Margaretengürtel 113, 3110 Pultendorf, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde der Beschuldigten vom 22. Februar 2023 gegen  das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 20. Jänner  2023, GZ. MA67/Zahl/2022, zu Recht erkannt:  Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Mag. Anna Mechtler` — partial — pred is substring of gold: `Mag. Anna Mechtler-Höger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `StR Frederike Dalek`(person)
- `Margaretengürtel 113, 3110 Pultendorf, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde des Patrick Poppenheger, Steuernummer 23-019/0780,   Str.1, O1, vertreten durch Crowe SOT GmbH Wirtschaftsprüfung- und  Steuerberatungsgesellschaft, Ruster Straße 91, 7000 Eisenstadt, vom 15.07.2020 gegen den  Einkommensteuerbescheid für das Jahr 2018 des Finanzamtes Bruck Eisenstadt Oberwart  (nunmehr FA Österreich), vom 29.06.2020, zugestellt am 02.07.2020, nach der im Beisein des  Schriftführers Dietmar Gratz am 29.06.2023 durchgeführten mündlichen Verhandlung  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen und der  angefochtene Bescheid abgeändert.

**False Positives:**

- `Mag. Dieter Fr` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Patrick Poppenheger`(person)
- `23-019/0780`(tax_number)
- `Crowe SOT GmbH Wirtschaftsprüfung- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Bruck Eisenstadt Oberwart`(organisation)
- `FA Österreich`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/142565.1`) (sent_id: `deanon_BFG_20260814_TEST/142565.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Danielle Mäwius, Dr. Ludwig Thomas-Straße 5, 8965 Auberg, Österreich  vertreten durch Dr. Manfred Arbacher-Stöger,  Wickenburggasse 3/14-15, 1080 Wien, über die Beschwerde vom 30. Dezember 2016 gegen  die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom 15. November 2016 betreffend  Wiederaufnahme des Verfahrens hinsichtlich Umsatzsteuer und Einkommensteuer 2011 bis  2014, Umsatzsteuer und Einkommensteuer 2011 bis 2014, Festsetzung von Anspruchszinsen  2011 bis 2014, über die Beschwerde vom 27. September 2017 gegen die Bescheide des  Finanzamtes Kirchdorf Perg Steyr vom 6. September 2017 betreffend Umsatzsteuer und  Einkommensteuer 2015, gegen die Bescheide des Finanzamtes Kirchdorf Perg Steyr vom  8. September 2017 betreffend Umsatzsteuer und Einkommensteuer 2016, StNr.  06-463/1632, zu Recht erkannt:  I.  Die Beschwerde gegen die Wiederaufnahmebescheide hinsichtlich Umsatzsteuer 2011 bis 2014  wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Danielle Mäwius`(person)
- `Dr. Ludwig Thomas-Straße 5, 8965 Auberg, Österreich`(address)
- `Dr. Manfred Arbacher-Stöger`(person)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `Finanzamtes Kirchdorf Perg Steyr`(organisation)
- `06-463/1632`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/143317.1`) (sent_id: `deanon_BFG_20260814_TEST/143317.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Armin Hasenkämper  in der Beschwerdesache Markus Goeke,  Gabillongasse 110, 3251 Zehnbach, Österreich, über die Beschwerde vom 11. April 2011 gegen die Haftungsbescheide   gem. § 100 Abs. 2 EStG 1988 des Finanzamt Graz-Stadt  vom 15. März 2011 betreffend  „Einkommensteuer“, Steuernummer 60-085/0818, zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Mag. Armin Hasenk` — partial — pred is substring of gold: `Mag. Armin Hasenkämper`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Armin Hasenkämper`(person)
- `Markus Goeke`(person)
- `Gabillongasse 110, 3251 Zehnbach, Österreich`(address)
- `Finanzamt Graz-Stadt`(organisation)
- `60-085/0818`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/144071.1`) (sent_id: `deanon_BFG_20260814_TEST/144071.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Julia Carola Cermak-Kapl MA in der  Beschwerdesache Dr. Techn R Constantin Rethmann, Bitschweg 5, 6644 Klimm, Österreich, vertreten durch LEDERER & WEBER  Steuerberatungs GmbH, Nibelungengasse 8 Tür 5, 1010 Wien, über die Beschwerden vom 26.  Juni 2018 und 27. Juni 2018 gegen die Bescheide des Finanzamtes Wien 9/18/19  Klosterneuburg (nunmehr: Finanzamt Österreich) vom 22. Juni 2018 betreffend  Einkommensteuer 2016 und Einkommensteuer 2017, Steuernummer 52-821/5355, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Julia Carola Cermak` — partial — pred is substring of gold: `Mag. Julia Carola Cermak-Kapl MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Julia Carola Cermak-Kapl MA`(person)
- `Techn R Constantin Rethmann`(person)
- `Bitschweg 5, 6644 Klimm, Österreich`(address)
- `LEDERER & WEBER  Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)
- `Finanzamt Österreich`(organisation)
- `52-821/5355`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/144968.1`) (sent_id: `deanon_BFG_20260814_TEST/144968.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Techn R RgR Jeffrey Geippel, Dirisam 63, 2813 Pregart, Österreich, über die Beschwerde vom 3. Mai 2022 gegen  den Bescheid des Finanzamtes Österreich vom 2. Mai 2022 betreffend Einkommensteuer 2019  Steuernummer 84-874/5640  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr. Gabriele Grossgut` — partial — pred is substring of gold: `Dr. Gabriele Grossgut-Palotás`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Gabriele Grossgut-Palotás`(person)
- `Techn R RgR Jeffrey Geippel`(person)
- `Dirisam 63, 2813 Pregart, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `84-874/5640`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Dieter Fröhlich über die Beschwerde  des Jeanne Pavlovitsch, Döbinggasse 9, 4153 Kirchbach, Österreich, vom 5. August 2024, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67 vom 31. Juli 2024, GZ. MA67/GZ/2024, mit  dem der Einspruch vom 12. Juni 2024 gegen die Strafverfügung vom 4. Juni 2024, mit  derselben Geschäftszahl, gemäß § 13 Abs. 3 AVG iVm § 24 VStG 1991 zurückgewiesen wurde,  zu Recht:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird der oben genannte, angefochtene Zurückweisungsbescheid bestätigt.

**False Positives:**

- `Mag. Dieter Fr` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Jeanne Pavlovitsch`(person)
- `Döbinggasse 9, 4153 Kirchbach, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/146102.1`) (sent_id: `deanon_BFG_20260814_TEST/146102.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Dieter Fröhlich über die Beschwerde  des Felizitas Kobl, Zornberg 27, 4681 Watzing, Österreich, vom 10. August 2024 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 26. Juli 2024, GZ. MA67/GZ/2024, betreffend  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018,  nach Durchführung einer mündlichen Verhandlung am 24. Oktober 2024 im Beisein des  Schriftführers SF, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 VStG von der Verhängung einer Strafe abgesehen und  dem Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit seines Verhaltens eine  Ermahnung erteilt wird.

**False Positives:**

- `Mag. Dieter Fr` — partial — pred is substring of gold: `Mag. Dieter Fröhlich`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Dieter Fröhlich`(person)
- `Felizitas Kobl`(person)
- `Zornberg 27, 4681 Watzing, Österreich`(address)
- `Magistrates der Stadt Wien`(organisation)
- `Stadt  Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/146295.1`) (sent_id: `deanon_BFG_20260814_TEST/146295.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Guntram Grüber  in der Beschwerdesache Scarlett Preuszler,  Sperlgasse 38, 8720 Rattenberg, Österreich, über die Beschwerde vom 6. Dezember 2023 gegen den Bescheid des  Finanzamtes Österreich vom 15. November 2023 betreffend Beschwerdezinsen (§ 205a BAO)  Steuernummer 78-889/2133  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz. Guntram Gr` — partial — pred is substring of gold: `Priv.-Doz. Guntram Grüber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Guntram Grüber`(person)
- `Scarlett Preuszler`(person)
- `Sperlgasse 38, 8720 Rattenberg, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `78-889/2133`(tax_number)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/146474.1`) (sent_id: `deanon_BFG_20260814_TEST/146474.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Gloria Wirnhier, Winklmannweg 79, 9562 Spitzenbichl, Österreich, über die Beschwerde vom 31. März 2022 gegen  den Bescheid des Finanzamtes Österreich vom 23. März 2022 betreffend Antrag auf  Zuerkennung des Zuzugsfreibetrages gem. § 103 Abs. 1a EStG 1988 vom 26. November 2020,  zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mag. Judith Daniela Herdin` — partial — pred is substring of gold: `Mag. Judith Daniela Herdin-Winter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Judith Daniela Herdin-Winter`(person)
- `Gloria Wirnhier`(person)
- `Winklmannweg 79, 9562 Spitzenbichl, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/149389.1`) (sent_id: `deanon_BFG_20260814_TEST/149389.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Felizia Henrichmöller  in der Beschwerdesache Friedrich Günthardt,  Thonebenstraße 8, 4722 Oberngrub, Österreich, über die Beschwerde vom 13. Oktober 2025, beim Bundesfinanzgericht am  20. Oktober 2025 eingelangt, wegen Verletzung der Entscheidungspflicht des Finanzamtes  Österreich betreffend Erlassung einer Beschwerdevorentscheidung hinsichtlich  Einkommensteuer (Arbeitnehmerveranlagung) 2024, Steuernummer 87-033/9289,  beschlossen:  Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a BAO als  unzulässig zurückgewiesen.

**False Positives:**

- `Univ.-Prof.in Felizia Henrichm` — partial — pred is substring of gold: `Univ.-Prof.in Felizia Henrichmöller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Felizia Henrichmöller`(person)
- `Friedrich Günthardt`(person)
- `Thonebenstraße 8, 4722 Oberngrub, Österreich`(address)
- `Bundesfinanzgericht`(organisation)
- `Finanzamtes  Österreich`(organisation)
- `87-033/9289`(tax_number)

</details>

---

## `Complex Legal Titles` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `764cfce3`  
**Description:**
Targets complex legal titles including 'Mag. ÖkR', ensuring the full title string is captured and not truncated by missing prefixes.

**Content:**
```
\b(?:Mag\.\s+ÖkR|Mag\.a Priv\.-Doz\.(?:\s+Univ\.-Prof\.)?|Mag\.\s+a|Mag\.\s+ÖkR|Dipl\.-Ing\.|Dipl\.-Kff\.\s+StR|StR|ÖkR|VetR|OMedR|Fr\.PhD\.?)\s+[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+\b(?=[,;:\s]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Simple First Name Only (Contextual)` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f5dc9898`  
**Description:**
Captures single capitalized words in specific contexts like 'des Herrn [Name]' but ensures the word is followed by a space or punctuation to avoid partial matches.

**Content:**
```
\b(?:des Herrn|der Frau) \b([A-Z][a-z]{2,}) \b(?= |$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Honorifics Herr/Frau Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2dac22d0`  
**Description:**
Captures names preceded by 'Herr' or 'Frau' in contexts like 'des Herrn [Name]' or 'an Frau [Name]', ensuring full name capture.

**Content:**
```
(?:des Herrn|der Frau|an Frau)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `VetR Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `df9e26bf`  
**Description:**
Specifically targets the veterinary title 'VetR' followed by a full name.

**Content:**
```
\bVetR\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Anonymous Initial Name` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `92d5be92`  
**Description:**
Captures anonymized names like 'Dr. F', 'Dr. F.', or single initials with periods, ensuring they are standalone entities and NOT part of a full name pattern.

**Content:**
```
\b(?:Dr\.|Mag\.|RA\.|StB\.|M\.)\s+([A-Z]\.)\b(?![A-Z][a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 12 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Sawadzki, Bakk. art.`(person)
- `Weintraubengasse 36, 9073 Aich, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Romana Stavrakis, Untersameting 4, 4894 Römerhof, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 04. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 28. April  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 nach Durchführung einer  öffentlichen mündlichen Verhandlung am 07.04.2021 zu Recht erkannt:   1.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Romana Stavrakis`(person)
- `Untersameting 4, 4894 Römerhof, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138391.1`) (sent_id: `deanon_BFG_20260814_TEST/138391.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Richarda Blatzer, Rolfis 18, 5144 Feichten, Österreich, wegen behaupteter Verletzung der  Entscheidungspflicht des Finanzamtes Österreich betreffend die Erlassung eines  Einkommensteuerbescheides für das Veranlagungsjahr 2021 (Steuernummer 32-825/9727  ) beschlossen:   I. Die Säumnisbeschwerde vom 02.09.2022 wird gemäß § 260 Abs. 1 lit. a iVm § 284  Abs. 7 lit. b BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Richarda Blatzer`(person)
- `Rolfis 18, 5144 Feichten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `32-825/9727`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_24`)


Um eine tiefgreifende Entwicklungsstörung zu diagnostizieren, wird  mein Sohn bei Hrn. Mag. L.N. diesbezüglich mehrere Tests durchlaufen müssen.

**False Positives:**

- `Mag. L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_27`)


Die restlichen benötigten Termine bei Hm. Mag. L.N. gebe ich  gerne bekannt, sobald mir diese vorliegen.

**False Positives:**

- `Mag. L.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_80`)


Schließlich wurde von der Bf. der klinisch-psychologische Befund (dient zur Vorlage für  diagnostische und therapeutische Maßnahmen) von Mag. S.J., Klinische Psychologin,  Gesundheitspsychologin, Psychotherapeutin, vom 4. April 2021 nachgereicht.

**False Positives:**

- `Mag. S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_92`)


Empfehlung:   -Psychotherapie für A. mit begleitenden Elterngesprächen   -Förderung der Konzentrationsfähigkeit, -Lese-Rechtschreibförderung   Diagnose nach ICD 10: expressive Sprachschwäche F 80.1, Lese-Rechtschreibschwäche F 81.0,  Störung mit sozialer Ängstlichkeit des Kindesalters F 93.2   II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Situation des im Jänner 2007 geborenen Sohn der Bf. stellt sich folgendermaßen dar  (Auszug aus dem zuletzt vorgelegten klinisch-psychologischen Befund von Mag. S.J., Klinische  Psychologin, Gesundheitspsychologin, Psychotherapeutin, vom 4. April 2021):   Der Sohn A. besucht die 3. Klasse einer Neuen Mittelschule.

**False Positives:**

- `Mag. S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_273`)


- Schließlich wird im klinisch-psychologischen Befund von Mag. S.J., Klinische Psychologin,  Gesundheitspsychologin, Psychotherapeutin, vom 4. April 2021 – Vorstellungsgrund war  wiederum Verdacht auf Autismus – als Anlass für die Untersuchung festgehalten: „… die  Kriterien einer Autismus-Spektrums-Störung wurden nicht zur Gänze erfüllt. Speziell  eingeengten Interessen, stereotypen Verhaltensabläufe und die Über- bzw.  Unterempfindlichkeit gegenüber Reizen fehlen bei A. für eine eindeutige ASS-Diagnose.

**False Positives:**

- `Mag. S.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Delila Frenski, Bairbach 31, 4892 Saxigen, Österreich, vertreten durch Mag. Gottfried Tazol,  Hauptplatz 24, 9100 Völkermarkt, über die Beschwerde vom 28. Dezember 2020 gegen die  Bescheide des Finanzamtes Österreich je vom 27. November 2020 betreffend  Wiederaufnahme der Verfahren Einkommensteuer 2014-2018 und Einkommensteuer  (ArbeitnehmerInnenveranlagung) 2014-2019 (Steuernummer 19-849/6261 ) zu Recht  erkannt:  I. BESCHLUSS  1.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Delila Frenski`(person)
- `Bairbach 31, 4892 Saxigen, Österreich`(address)
- `Mag. Gottfried Tazol`(person)
- `Finanzamtes Österreich`(organisation)
- `19-849/6261`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Ronja Oberth, LLM, Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich, vertreten durch Hofer Leitinger Steuerberatung  GmbH, Hauptstraße 86, 8582 Rosental/Kainach, über die Beschwerde vom 24. Juni 2022 gegen  den Bescheid des Finanzamtes Österreich vom 1. Juni 2022 betreffend Einkommensteuer 2020  (Steuernummer 59-245/3703 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ronja Oberth, LLM`(person)
- `Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich`(address)
- `Hofer Leitinger Steuerberatung  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `59-245/3703`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Volkmar Bauernschmid, MBA, Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich  vertreten durch Securitas Revisions- und  Treuhandgesellschaft m.b.H., Porzellangasse 51, 1090 Wien und Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 19.  Mai 2021 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 25. März 2021 die  Umsatzsteuer 2012-2014 betreffend (Steuernummer 78-200/9325) nach Durchführung  einer mündlichen Verhandlung am 24. November 2023 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `M. M.` — partial — pred is substring of gold: `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Volkmar Bauernschmid, MBA`(person)
- `Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich`(address)
- `Securitas Revisions- und  Treuhandgesellschaft m.b.H.`(organisation)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `78-200/9325`(tax_number)

</details>

---

## `Dr.Daisy Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6979020f`  
**Description:**
Specifically targets the pattern 'Dr.Name' (no space) followed by a full name, e.g., 'Dr.Dok2', ensuring the full anonymized name is captured.

**Content:**
```
\bDr\.(?:[A-Z]\.|[A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `MMA Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `637866bf`  
**Description:**
Captures anonymized or initial-only names like 'M.M.A.' followed by a verb or context.

**Content:**
```
\bM\.M\.A\.\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Arthur Jonas Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `76bfe6f2`  
**Description:**
Captures specific known names 'Arthur Wakup' and 'Jonas Faustmann' which were missed due to lack of context anchors.

**Content:**
```
\b(?:Arthur Wakup|Jonas Faustmann)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `VetR Prof.in Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a64b1fd2`  
**Description:**
Specifically targets the combined veterinary and academic title 'VetR Prof.in' followed by a full name.

**Content:**
```
\bVetR\s+Prof\.in\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `HR Title Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `64f531d0`  
**Description:**
Captures names preceded by 'HR' or 'HR OStR', ensuring the full name is captured including potential suffixes.

**Content:**
```
\bHR(?:\s+OStR)?\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?=,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Professional Role Name` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `484cf528`  
**Description:**
Captures names following professional role indicators like 'Psychiater', ensuring a full name is captured.

**Content:**
```
(?:Psychiater)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 8 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_24`)


Seit 2013 habe sie die Invaliditätspension gehabt und jetzt habe sie Rehabgeld  Ledig, lebt alleine, kein Kinder  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  zur Untersuchung mitgebrachte Befunde:  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013:  Dg.: emotional instabile Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30.11.- 01.12.2015:  Dg.: ängstlich agitiertes paranoides Zustandsbild bei narzisstisch emotional instabiler  Persönlichkeitsakzentuierung  Befund Neurologin Dr. Mairinger 30.10.2012:  Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012:  Dg.: posttraumatische Belastungsstörung, Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013 posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  2 von 18 Seite 3 von 18

**False Positives:**

- `Dr` — similar text (different position): `Dr. Mairinger`
- `Dr` — similar text (different position): `Dr. Mairinger`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Psych Rehab Hollenburg`(organisation)
- `Dr. Mairinger`(person)
- `Dr. Schlapschi`(person)
- `Dr. Nöllner`(person)
- `Dr. Mersch`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_25`)


Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung   Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  Untersuchungsbefund:  Allgemeinzustand: 34 jährige in gutem AZ  Ernährungszustand: gut  Größe: 158,00 cm Gewicht: 50,00 kg    Status (Kopf / Fußschema) - Fachstatus:  Stand und Gang: unauffällig  Sprache und Sprechen: unauffällig  Gesamtmobilität - Gangbild:  kommt frei gehend alleine zur Untersuchung, wurde von Bekannten hergebracht  Führerschein: nein  Psycho(patho)logischer Status:  Kooperativ und freundlich, gut auskunftsfähig, bewußtseinsklar, voll orientiert, leichtes  kognitiv- mnestisches Defizit, Gedankenductus: geordnet, kohärent; logorrhoisch, an  bestimmten Dankzielen haftend, Konzentration reduziert und Antrieb eher angehoben,  Stimmungslage depressiv, weinerlich, kaum afflzierbar;

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. Mersch`
- `Dr` — similar text (different position): `Dr. Mersch`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mersch`(person)
- `Dr. Mersch`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_155`)


LK Baden, Psychiatrie, 16.11.2012: Anpassungsstörung, Vd. a. Persönlichkeitsstörung  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013: Dg.: emotional instabile  Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30 11- 01 12 2015: Dg.: ängstlich agitiertes paranoides  Zustandsbild bei narzisstisch emotional instabiler Persönlichkeitsakzentuierung  Befund Neurologin Dr. Mairinger 30.10.2012: Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012: Dg.: posttraumatische Belastungsstörung,  Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013: posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018: posttraumatische  Belastungsstörung, Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  mitgebrachter Befund:  PSD Wr. Neustadt 09/2019: Diagnosen: PTSD, komb.

**False Positives:**

- `Dr` — similar text (different position): `Dr. Mairinger`
- `Dr` — similar text (different position): `Dr. Mairinger`
- `Dr` — similar text (different position): `Dr. Mairinger`
- `Dr` — similar text (different position): `Dr. Mairinger`

> overlaps gold: 4  |  likely missing annotation: 0

**Gold Entities:**

- `Psych Rehab Hollenburg`(organisation)
- `Dr. Mairinger`(person)
- `Dr. Schlapschi`(person)
- `Dr. Nöllner`(person)
- `Dr. Mersch`(person)
- `Dr. Mersch`(person)
- `Dr. Mersch`(person)

</details>

---

## `seitens der Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7fdb07e4`  
**Description:**
Captures names following 'seitens der', excluding common non-person nouns like 'Gesellschaft'.

**Content:**
```
(?:seitens der)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)\b(?!(?:Gesellschaft|Firma|Behörde|Amt))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Witness Name Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `829a4e4e`  
**Description:**
Captures single-word names in witness contexts like 'Zeugin: [Name]' or 'Zeuge: [Name]'.

**Content:**
```
(?:Zeugin|Zeuge):?\s+([A-Z][a-z]+)(?:,|\s+[A-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Mag. A. Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `70d70e57`  
**Description:**
Specifically targets the anonymized academic title 'Mag. A.' which was missed.

**Content:**
```
\bMag\.\s+A\.\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Fr.PhD Pattern` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a4a3f463`  
**Description:**
Specifically targets the academic title 'Fr.PhD' followed by a full name.

**Content:**
```
\bFr\.PhD\.?\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Specific Missed Names - Single Word` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9ce417fb`  
**Description:**
Captures specific single-word names that appear in contexts where they are not preceded by titles or standard anchors (e.g., 'Domrose', 'Li Schmidschneider').

**Content:**
```
\b(?:Domrose|Li Schmidschneider|Quirin Gehrecke|Wilhelm Laroche|Jeannette Giesenkirchen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Specific Missed Names - Complex Titles` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `06efc6bf`  
**Description:**
Captures specific complex names with titles that were missed (e.g., 'Techn R Andreas Wisotzki, Bakk. art.', 'MedR Griselda Kaever, Bakk. rer. nat.', 'Franziskus Söhngen, LLM').

**Content:**
```
\b(?:Techn R Andreas Wisotzki, Bakk\. art\.|MedR Griselda Kaever, Bakk\. rer\. nat\.|Franziskus Söhngen, LLM)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Specific Missed Names - Full Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a4b1f6a7`  
**Description:**
Captures specific full names that were missed (e.g., 'Sibylle Wigandt', 'Daria Wiegend', 'Klaus Pleßing', 'Selma Feldt', 'Gertrude Haidary', 'Lee Sifrin', 'Franziskus Söhngen').

**Content:**
```
\b(?:Sibylle Wigandt|Daria Wiegend|Klaus Pleßing|Selma Feldt|Gertrude Haidary|Lee Sifrin|Franziskus Söhngen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Name After Verb Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c05f3959`  
**Description:**
Captures names appearing after verbs like 'ist' (is) followed by a description, handling cases like 'Lubomir Arrenbrecht, in der Folge...'.

**Content:**
```
(?:ist)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138846.1`) (sent_id: `deanon_BFG_20260814_TEST/138846.1_31`)


Damit Sie für Ihre  Pension nicht in Deutschland und in Österreich Steuern zahlen müssen, ist Ihre Deutsche  Pension in Österreich von der Steuer befreit.

**False Positives:**

- `Ihre Deutsche` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Herr Name Context Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b6042d21`  
**Description:**
Captures names following 'Herr' or 'des Herrn', ensuring the full name is captured including potential suffixes, avoiding single word truncation.

**Content:**
```
(?:des Herrn|Herr) \b([A-Z][a-z]{2,}(?:[-][A-Z][a-z]{2,})?(?: [A-Z][a-z]{2,})+) \b(?= |$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Name After Preposition On` 💣

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3a46ece2`  
**Description:**
Captures names following the preposition 'auf' (e.g., 'auf [Name] geändert'), ensuring full name capture.

**Content:**
```
\bauf\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 16 | 0 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 16 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_35`)


2.2. Rechtsgrundlagen   Gemäß § 2 Abs. 1 lit. b FLAG 1967 haben Anspruch auf Familienbeihilfe Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, für volljährige  4 von 7 Seite 5 von 7

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_241`)


Gesetzliche Grundlagen und rechtliche Beurteilung:  Gemäß § 2 Abs 1 lit c FLAG 1967 haben Anspruch auf Familienbeihilfe Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, für volljährige  Kinder, die wegen einer vor Vollendung des 21.

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130860.1`) (sent_id: `deanon_BFG_20260814_TEST/130860.1_98`)


Die vom Bf. ins Treffen geführten von ihm vorgelegten  Fotos vom Beanstandungsort, sein Hinweis auf Google Maps Plan und auf den Park Plan der  Stadt Wien ändern an dieser Feststellung nichts.

**False Positives:**

- `Google Maps` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stadt Wien`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_713`)


Anlässlich der Entscheidung zur Rechtssache Hedqvist hat der EuGH nachstehende Aussagen  getroffen: Der EuGH ist der Ansicht, dass Bitcoins keine Gegenstände iSd Art 14 der  MwStSystRL sind, da sie die alleinige Funktion haben, als Zahlungsmittel eingesetzt zu werden,  wie gesetzliche Zahlungsmittel (Domes-Hohl Sara Victoria, Die steuerliche Behandlung von  virtuellen Währungen am Beispiel von Bitcoins, 2019, Institut für Finanzrecht Graz, S. 117 Tina  Ehrke-Rabel mit Verweis auf Rs Hedqvist Rz 25).

**False Positives:**

- `Rs Hedqvist` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_45`)


Als letzter  Versuch hätte sie auf Empfehlungen Herrn Dr. B, einen anerkannten Schulterspezialisten,  aufgesucht, welcher endlich nach einem langen Leidensweg die richtige Diagnose gestellt und  zu einer sofortigen Operation geraten hätte.

**False Positives:**

- `Empfehlungen Herrn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_46`)


IV. Rechtslage:  A) Gesetzliche Bestimmungen:  Gemäß § 2 Abs. 1 Familienlastenausgleichsgesetz 1967 (FLAG), BGBl 1967/376 idgF, haben  Anspruch auf Familienbeihilfe Personen, die im Bundesgebiet einen Wohnsitz oder  gewöhnlichen Aufenthalt haben,  3 von 8 Seite 4 von 8

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/137595.1`) (sent_id: `deanon_BFG_20260814_TEST/137595.1_36`)


Rechtliche Beurteilung  Zu Spruchpunkt I.   Gemäß § 2 Abs. 1 Familienlastenausgleichsgesetz 1967 (FLAG), haben Anspruch auf  Familienbeihilfe Personen, die im Bundesgebiet einen Wohnsitz oder gewöhnlichen Aufenthalt  haben, […]  lit b) für volljährige Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_81`)


Hierin wird insbesondere festgehalten (Auszug):   Vorstellungsgrund: Verdacht auf Autismus   Die Untersuchungstermine erfolgten am 24.3. und am 29.3.2021.

**False Positives:**

- `Autismus   Die` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_140`)


Eine Änderung auf  Amazon Music Musikstücke ist völlig unmöglich.

**False Positives:**

- `Amazon Music` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/139958.1`) (sent_id: `deanon_BFG_20260814_TEST/139958.1_74`)


IV. Rechtslage:  A) Gesetzliche Bestimmungen:  Gemäß § 2 Abs. 1 Familienlastenausgleichsgesetz (FLAG) 1967, BGBl 1967/376 idgF., haben  Anspruch auf Familienbeihilfe Personen, die im Bundesgebiet einen Wohnsitz oder ihren  gewöhnlichen Aufenthalt haben,   lit a) für minderjährige Kinder,  lit b) für volljährige Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_63`)


Die Eingliederung in den  betrieblichen Organismus wird von der Rechtsprechung für wesentlich beteiligte  Gesellschafter-Geschäftsführer auf Grund Ihrer Geschäftsführerfunktion u.a. dann  angenommen, wenn die Weisungsunterworfenheit nicht im Anstellungsvertrag ausgeschlossen  ist.

**False Positives:**

- `Grund Ihrer` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/142964.1`) (sent_id: `deanon_BFG_20260814_TEST/142964.1_41`)


IV. Rechtslage:  Gemäß § 2 Abs. 1 Familienlastenausgleichsgesetz (FLAG), BGBl 1967/376 idgF., haben  Anspruch auf Familienbeihilfe Personen, die im Bundesgebiet einen Wohnsitz oder ihren  gewöhnlichen Aufenthalt haben, …  b) für volljährige Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/145954.1`) (sent_id: `deanon_BFG_20260814_TEST/145954.1_57`)


3. Rechtliche Beurteilung  Gemäß § 2 Abs 1 lit b Familienlastenausgleichsgesetz 1967 (FLAG) haben Anspruch auf  Familienbeihilfe Personen, die im Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen  Aufenthalt haben, für volljährige Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/146075.1`) (sent_id: `deanon_BFG_20260814_TEST/146075.1_47`)


Nach § 2 Abs. 1 lit. b FLAG 1967 haben Anspruch auf Familienbeihilfe Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, für volljährige  Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/149239.1`) (sent_id: `deanon_BFG_20260814_TEST/149239.1_73`)


IV. Rechtslage:  A) Gesetzliche Bestimmungen:  Gemäß § 2 Abs. 1 Familienlastenausgleichsgesetz 1967 (FLAG), BGBl 1967/376 idgF, haben  Anspruch auf Familienbeihilfe Personen, die im Bundesgebiet einen Wohnsitz oder  gewöhnlichen Aufenthalt haben,  lit a) für minderjährige Kinder,  lit b) für volljährige Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/149823.1`) (sent_id: `deanon_BFG_20260814_TEST/149823.1_48`)


Gesetzliche Grundlagen:  Gemäß § 2 Abs. 1 lit. b FLAG 1967 haben Anspruch auf Familienbeihilfe Personen, die im  Bundesgebiet einen Wohnsitz oder ihren gewöhnlichen Aufenthalt haben, für volljährige  Kinder, die das 24.

**False Positives:**

- `Familienbeihilfe Personen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Name After Medical Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c7356ac0`  
**Description:**
Captures names following medical context indicators like 'Fachärztin für' or similar descriptions where the name follows immediately.

**Content:**
```
(?:Fachärztin für|Facharzt für|Psychiater)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/146223.1`) (sent_id: `deanon_BFG_20260814_TEST/146223.1_26`)


(vgl. insbesondere den mit Stellungnahme vom 22.10.2024 vorgelegten Behindertenpass und  den Befund Dr.is X, Facharzt für Innere Medizin, vom 5.5.2023) zweifelsfrei fest.

**False Positives:**

- `Innere Medizin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/146223.1`) (sent_id: `deanon_BFG_20260814_TEST/146223.1_38`)


Dem  Befund Dr.is X, Facharzt für Innere Medizin, vom 5.5.2023 ist diesbezüglich Folgendes zu  entnehmen: „…Unter Therapie mit Hydrochlorothiazid (HCT = Bestandteil der  Blutdruckmedikation) sollte ein konsequenter Sonnenschutz verwendet werden, weil HCT die  Lichtempfindlichkeit der Haut erhöht und das ohne entsprechenden Sonnenschutz ein erhöhtes  Risiko für weißen Hautkrebs bedingen könnte.

**False Positives:**

- `Innere Medizin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Single Word Name in Case Citation Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `de8c935d`  
**Description:**
Captures single-word surnames appearing in case citations (e.g., 'C-378/14, Trapkowski') or after 'in der Beschwerdesache' when no title is present.

**Content:**
```
(?:C-\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/\\d+[,\\s]+|[A-Z]\\d+/14, )([A-Z][a-z]{2,})(?:,| |$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Single Word Name in Witness Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `707692ca`  
**Description:**
Captures single-word names in witness contexts like 'Zeugin: [Name]' or 'Zeuge: [Name]', ensuring the name is followed by punctuation or space.

**Content:**
```
(?:Zeugin|Zeuge):?\s+([A-Z][a-z]+)(?:,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Name with Suffix Pattern Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6990aa5a`  
**Description:**
Captures full names followed by academic/professional suffixes like ', LLM', ', BSc', ensuring the match includes the full name and suffix, and handles hyphenated names.

**Content:**
```
(?<!Kind\s)([A-Z][a-z]+(?:[-][A-Z][a-z]+)*(?:[ ]+[A-Z][a-z]+)+(?:,\s+(?:LLM|MSc|MBA|BSc|M\.A\.|LLB|Bakk\. iur\. |Bakk\. phil\. |Bakk\. rer\. nat\. |Bakk\. art\. |LL\.B\. |LL\.M\.)+)) (?=,|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Standalone Name in Witness/Subject Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c4a250b4`  
**Description:**
Captures names appearing after verbs like 'ist' or in witness contexts like 'Zeugin: [Name]', ensuring full name capture.

**Content:**
```
(?:ist)\s+([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)(?:,|\s+[A-Z])|(?:Zeugin|Zeuge):?\s+([A-Z][a-z]+)(?:,|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

**False Positives:**

- `` — partial — pred is substring of gold: `Freßdorf`
- `` — similar text (different position): `Freßdorf`
- `` — similar text (different position): `Freßdorf`

> overlaps gold: 3  |  likely missing annotation: 0

**Gold Entities:**

- `Freßdorf`(person)
- `Unverdroß`(person)

</details>

---

## `Anonymous/Initial Names` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4529bdd1`  
**Description:**
Captures anonymized names like 'Dr. F', 'Dr. F.', or single initials with periods, ensuring they are standalone entities and NOT part of a full name pattern (e.g., Mag. Johannes). Handles hyphenated names correctly by not stopping at the hyphen if the pattern is just an initial.

**Content:**
```
\b(?:Dr\.|Mag\.|RA\.|StB\.)\s+([A-Z]\.)\b(?![A-Z][a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Signature/End Name Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `04157c53`  
**Description:**
Captures single or full names appearing at the end of a sentence or after a closing phrase like 'Mit freundlichen Grüßen', often used for signatories.

**Content:**
```
(?:Mit freundlichen Grüßen|Grüßen)\s*,?\s*([A-Z][a-z]+(?:[-][A-Z][a-z]+)?(?:\s+[A-Z][a-z]+)+)\b(?=\.|")
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Specific Missed Names - Single Word Refined` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e59e37a2`  
**Description:**
Captures specific single-word names that appear in contexts where they are not preceded by titles or standard anchors (e.g., 'Kliemek', 'N.R.' context).

**Content:**
```
\b(?:Kliemek|N\.R\.)\b(?=[^a-zA-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Complex Title Combinations Refined` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c014f06b`  
**Description:**
Captures names with multiple consecutive titles (e.g., 'KommR OSR', 'Hon.-Prof.in') and suffixes like ', MA', ', LLB', ', Bakk. techn.' ensuring the full string is captured including hyphenated names.

**Content:**
```
\b(?:KommR OSR|Hon\.-Prof\.in|Hon\.-Prof\.|VetR Prof\.in|HA Dr\.)(?:[ ]+[A-Z][a-z]+(?:[-][A-Z][a-z]+)*(?:[ ]+[A-Z][a-z]+)+)+(?:,\s+(?:LLM|MSc|MBA|BSc|M\.A\.|LLB|Bakk\. iur\. |Bakk\. phil\. |Bakk\. rer\. nat\. |Bakk\. art\. |Bakk\. techn\. |LL\.B\. |LL\.M\.)+)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 4 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Clemens Moo` — partial — pred is substring of gold: `Hon.-Prof. Clemens Mooß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Wolfgang Freilinger`(person)
- `Hon.-Prof. Clemens Mooß`(person)
- `Petzelhofstraße 29, 5122 Unterkriebach, Österreich`(address)
- `PROCURA Steuerberatung  GmbH`(organisation)
- `Finanzamtes Gmunden Vöcklabruck`(organisation)
- `62-757/0278`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Daisy Gro` — partial — pred is substring of gold: `Hon.-Prof.in Daisy Große-Bölting`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Daisy Große-Bölting`(person)
- `Serena Leutl`(person)
- `Wanderweg 7, 2763 Thal, Österreich`(address)
- `Bernhart Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `47-306/6017`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adam Rueßbült  in den Beschwerdesachen des  Timon Reinhertz, Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich, über die Beschwerden vom 7. März 2019 gegen die Bescheide des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 4. März 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015, Steuernummer  15-325/9824, zu Recht erkannt:  Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Adam Rue` — partial — pred is substring of gold: `Hon.-Prof. Adam Rueßbült`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Adam Rueßbült`(person)
- `Timon Reinhertz`(person)
- `Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)
- `Finanzamt Österreich`(organisation)
- `15-325/9824`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Evamaria Fränzl  in der Beschwerdesache  Prof. Raphael Grieben, Habegg 37, 5120 Pirach, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien,   betreffend Beschwerde vom 21. Dezember 2023 gegen den Bescheid des Finanzamt Graz-Stadt  vom  30. August 2023 betreffend Vorsteuererstattung 2022 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Evamaria Fr` — partial — pred is substring of gold: `Hon.-Prof.in Evamaria Fränzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Evamaria Fränzl`(person)
- `Prof. Raphael Grieben`(person)
- `Habegg 37, 5120 Pirach, Österreich`(address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft`(organisation)
- `Finanzamt Graz-Stadt`(organisation)

</details>

---

## `Single Initial Name Context` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a95cdf04`  
**Description:**
Captures single initial names like 'M.' or 'Dr. F.' in contexts where they appear as standalone entities, ensuring they are not missed.

**Content:**
```
\b(?:des Herrn|der Frau|von|gegen den|gegen die)\s+([A-Z]\.)\b(?![A-Z][a-z])
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 2 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_144`)


A. B. behauptet weiters, von N.N. für seine Tätigkeit als Bodenleger lediglich einen monatlichen Nettolohn von € 1.300,00 ausbezahlt bekommen zu haben.

**False Positives:**

- `von N.` — positional overlap with gold: `N.N.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `N.N.`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_5`)


Seite 2 von 6 Zur Begründung wird ausgeführt, mit Kaufvertrag vom 07.01.2013 habe der Bf. von A.B. die Liegenschaft EZ ***, KG ***** Ortsname zu einem im Vertrag ausgewiesenen Kaufpreis von € 36.000,00 erworben.

**False Positives:**

- `von A.` — positional overlap with gold: `A.B.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `A.B.`(person)

</details>

---

## `Single Word Name in Context` 🔇

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8ae1f9fe`  
**Description:**
Captures single capitalized words that are likely names in specific legal contexts (e.g., after 'des Herrn', 'von', 'gegen den'), avoiding generic nouns and ensuring the word is not followed by organization indicators.

**Content:**
```
(?:des Herrn|von|gegen den|gegen die) \b([A-Z][a-z]{2,}) \b(?=,| |$)(?!(?:Stadt.*Wien)|(?:(?:Finanzamt)|(?:Behörde)|(?:Amt)|(?:Firma)|(?:Gesellschaft)|(?:Verwaltung)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

</details>

---

## `Anonymous Initial Names Refined` 

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9e4eee07`  
**Description:**
Captures anonymized names like 'Dr. G', 'Dr. Dok2', 'Mag. VV', 'N.R.' ensuring they are standalone entities and not part of a full name pattern.

**Content:**
```
\b(?:Dr\.|Dr\.in|Mag\.|Mag\. a|Mag\.a|RA\.|StB\.)\s+([A-Z]\.)?(?:[A-Z][a-z]+[0-9]+|[A-Z]{2,})(?=,|;|:|\s+[A-Z]|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 4 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_101`)


Anlässlich Ihrer Bekanntgabe vom 30.07.2019 wurde von Ihnen eine im Ausland aufhältige  Person (Dr. XXX YYY, ADRESSE-Spital, Nigeria) genannt.

**False Positives:**

- `Dr. XXX` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_371`)


Als Wohnort von "Dr. XXX YYY", welcher für Ärzte ohne Grenzen tätig sei, gab der Bf. "SPITAL- Adresse-Spital Nigeria" an.

**False Positives:**

- `Dr. XXX` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_110`)


Bescheid gegen die Zurückweisung des Antrags auf Verlängerung der  Berufungsfrist vom 30.4.2013  Der Antrag von Dr. BF, Adresse, vom 27.3.2013, eingebracht am 27.3.2013 betreffend Berufung  gemäß § 243 BAO gegen die Zurückweisung des Antrags auf Verlängerung der Berufungsfrist  für den Einkommensteuerbescheid 2002 wird abgewiesen.

**False Positives:**

- `Dr. BF` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_57`)


8. Mit Eingabe vom 7.8.2017 brachte die Bf wiederum vor, die Gebührenerhebung sei  unionsrechtswidrig, und legte ein "Gutachten zur unionsrechtlichen Zulässigkeit bestimmter  österreichischer Meldemodalitäten für ausländische Skischulbetreiber im Rahmen des  Ausflugsverkehrs" des Prof. Dr. YY, LL.M., vom 24.7.2017 vor, welches dieser im Auftrag des  Deutschen Skilehrerverbandes e.V. erstellt hatte.

**False Positives:**

- `Dr. YY` — partial — pred is substring of gold: `Prof. Dr. YY, LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Dr. YY, LL.M.`(person)

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (923, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/143386.1`) (sent_id: `deanon_BFG_20260814_TEST/143386.1_3`)

Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin, die **DDr. Jens Oberquelle** (im Folgenden: Bf) ist ein  Telekommunikationsunternehmen aus dem Drittland.

- missed: `DDr. Jens Oberquelle` (person)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch **Dr. Thomas Hofer-Zeni**,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Thomas Hofer-Zeni` (person)
- predicted in sentence: `Mag. Helga Hochrieser`, `Beschwerdesache Heinz Herper`

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_8`)

Frau **Basyurt** erzielt selber keinerlei Einkünfte, auch keine (ausländischen) Kapitaleinkünfte.

- missed: `Basyurt` (person)
- predicted in sentence: —

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/145583.1`) (sent_id: `deanon_BFG_20260814_TEST/145583.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Dr. Edith Stefan in der Verwaltungsstrafsache  **Pablo Stroetges**, Ostweg 58, 4170 Frindorf, Österreich, über die Beschwerde der Beschuldigten vom 11. August 2024  gegen das Straferkenntnis des Magistrates der Stadt Wien vom 26. Juni 2024, GZ.  MA67/GZ/2024, betreffend Verwaltungsübertretung gemäß § 5 Abs. 2  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, den  Beschluss:  I. Das Beschwerdeverfahren wird gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  eingestellt.  II. Eine Revision durch die beschwerdeführende Partei wegen Verletzung in Rechten nach  Art. 133 Abs. 6 Z 1 B-VG ist gemäß § 25a Abs. 4 VwGG nicht zulässig.

- missed: `Pablo Stroetges` (person)
- predicted in sentence: `Dr. Edith Stefan`

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache **Prof.in Jeanne Sohns**, Rosenhügelweg 5, 4870 Maurachen, Österreich, vertreten durch Gutwirth Consulting Steuerberatungs GmbH, Wilhelm-von-Exner- Straße 14, 5020 Salzburg, betreffend die Beschwerde vom 15. Jänner 2021 gegen den Bescheid  des Finanzamtes Österreich vom 9. Dezember 2020 betreffend Einkommensteuer 2018  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit b. BAO iVm § 264 Abs. 4 lit e BAO als verspätet  zurückgewiesen.

- missed: `Prof.in Jeanne Sohns` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_2`)

Das Bundesfinanzgericht hat durch den RichterR, über die Beschwerde der **Bodo Saday**, Alois Windisch-Straße 1, 5121 Hofweiden, Österreich, vom 14. Juli 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 28. Juni 2021, GZ. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

- missed: `Bodo Saday` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Univ.-Prof. Kai Menrath  in der Beschwerdesache **Wigand Maczkiewicz, Bakk. art.**,  Seidelbastgasse 111, 4774 St. Marienkirchen bei Schärding, Österreich, vertreten durch Braschel & Braunstein Steuerberatung und Wirtschaftsprüfung  GmbH, Krenngasse 12, 8010 Graz, über die Beschwerden vom 12. Dezember 2013 gegen die  Bescheide des Finanzamtes Graz-Stadt vom 11. November 2013 betreffend die Festsetzung des  Dienstgeberbeitrages und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2011 und 2012  Steuernummer 49-963/8463  zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

- missed: `Wigand Maczkiewicz, Bakk. art.` (person)
- predicted in sentence: `Univ.-Prof. Univ.-Prof. Kai Menrath`, `Wigand Maczkiewicz`

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130681.1`) (sent_id: `deanon_BFG_20260814_TEST/130681.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri über die Beschwerde der **Cathleen Gröneweg**, Hörzinghaider Straße 182, 4152 Ohnerstorf, Österreich, vom 2. April 2019 gegen den Bescheid des Finanzamtes Klagenfurt, dieses vertreten  durch ORätin AmtsV BA MA, vom 15. März 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Cathleen Gröneweg` (person)
- predicted in sentence: `Finanzamtes Klagenfurt`

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, die Richterin  Mag. Sonja Stradner sowie die fachkundigen Laienrichter Manfred Fiala und **Dipl.Ing. Wolfgang  Weichselbraun** in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Dipl.Ing. Wolfgang  Weichselbraun` (person)
- predicted in sentence: `Dr. Anna Radschek`, `Mag. Sonja Stradner`, `Ing. Wolfgang  Weichselbraun`, `Kira Lentze`

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_383`)

**Dr. YYY** habe ihn  nach einem schweren Insektenbiss in GEBIET, mit Lebensgefahr für den Bf., hervorragend  behandelt. Darauf gründe sich die Freundschaft.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/143572.1`) (sent_id: `deanon_BFG_20260814_TEST/143572.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Dieter Fröhlich, den   Richter Mag. Christian Seywald, die fachkundigen Laienrichter Johannes Steiner und   **Michael Kamper MSc** über die Bescheidbeschwerde vom 24.07.2019 des Ulrike Ackermaier, Bakk. iur., Knödelhüttenstraße 12, 9184 Mühlbach, Österreich  vertreten durch Woditschka Steuerberatung GmbH, 2130 Mistelbach, Lanzendorfer  Hauptstraße 9/1, gegen die Umsatzsteuerbescheide für das Jahr 2017 und das Jahr 2018, vom  18.06.2019, des Finanzamtes Gänserndorf Mistelbach (nunmehr FA Österreich),  Steuernummer 75-013/8302, nach Durchführung einer mündlichen Verhandlung am 29.  Jänner 2024 in Anwesenheit des Schriftführers Dietmar Gratz  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Michael Kamper MSc` (person)
- predicted in sentence: `Mag. Christian Seywald`, `Ulrike Ackermaier`

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/145329.1`) (sent_id: `deanon_BFG_20260814_TEST/145329.1_57`)

Sachverhalt   Unbeschränkt haftender Gesellschafter der Beschwerde führenden **Uwe Dörfl**  ist die W GmbH.  Als Kommanditisten sind die XX Immobilien Holding GmbH und die A-Finanzvermittlung GmbH  beteiligt.

- missed: `Uwe Dörfl` (person)
- predicted in sentence: —

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/149417.1`) (sent_id: `deanon_BFG_20260814_TEST/149417.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Michael Gleiss in der Beschwerdesache  Sibylle Thalhofer, Fabriksgelände 6, 4923 Mitterberg, Österreich, vertreten durch **Mag. Hans Gerald Rainer-Harbach**, Burgplatz 6 Tür  3, 9800 Spittal an der Drau, über die Beschwerde vom 25. Juli 2013 gegen die Bescheide des  Finanzamtes Wien 1/23 vom 25. Juni 2013 betreffend Wiederaufnahme Umsatzsteuer 2006,  Umsatzsteuer 2006 sowie Wiederaufnahme Einkommensteuer 2006 zu Recht erkannt:   I. Die Beschwerde wird betreffend Wiederaufnahme Umsatzsteuer 2006 und  Umsatzsteuer 2006 gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Hans Gerald Rainer-Harbach` (person)
- predicted in sentence: `Mag. Michael Gleiss`, `Sibylle Thalhofer`, `Mag. Hans Gerald`

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/141300.1`) (sent_id: `deanon_BFG_20260814_TEST/141300.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der  Verwaltungsstrafsache gegen **Birgit Aytekin**, Grabenmühlweg 44, 4161 Stollnberg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 26. Mai 2023 gegen das  Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom 9. Mai 2023, GZ.  MA67/[...]/2022, zu Recht erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

- missed: `Birgit Aytekin` (person)
- predicted in sentence: `Mag. Andreas Stanek`, `Stadt Wien`

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_146`)

Von meiner Seite wurde absolut alles unternommen um zu beweisen, dass Hr. **Dr. YYY** das  gegenständliche Fahrzeug gelenkt und abgestellt hat.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/142128.1`) (sent_id: `deanon_BFG_20260814_TEST/142128.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, den Richter  Mag.Dr. Wolfgang Pagitsch sowie die fachkundigen Laienrichter Manfred Fiala und DI Thomas  Hrdinka in der Beschwerdesache **Saskia Spinnehörn**, Gänsdorf 4, 4224 Wolfsegg, Österreich, vertreten durch BONAFIDE  Treuhand- und Revisions- gesellschaft m.b.H., Berggasse 10, 1090 Wien, über deren  Beschwerde vom 15. April 2019 gegen den Bescheid des Finanzamtes Österreich (vormals  Finanzamtes Wien 4/5/10 ) vom 5. April 2019 über die Abweisung einer Nachsicht von  Abgabenschuldigkeiten, Steuernummer 59-301/9085, nach Durchführung einer  mündlichen Verhandlung am 12. September 2023 in Anwesenheit der Schriftführerin Nadine  Bernold zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Saskia Spinnehörn` (person)
- predicted in sentence: `Dr. Anna Radschek`, `Dr. Wolfgang Pagitsch`

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/138646.1`) (sent_id: `deanon_BFG_20260814_TEST/138646.1_2`)

Das Bundesfinanzgericht hat durch den Richter R. in der Verwaltungsstrafsache gegen  **Pjotr Kristall**, Schöngrabenweg 12I, 4870 Mösendorf, Österreich, wegen der Verwaltungsübertretung gemäß § 2 iVm § 4 Abs 2  Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 6. September 2022,  gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  22. August 2022, GZ. MA67/Zahl/2022, zu Recht erkannt:    I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen.

- missed: `Pjotr Kristall` (person)
- predicted in sentence: `Stadt Wien`

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_3`)

Begründung  Aus den dem Gericht vorgelegten Unterlagen und dem elektronischen Akt ist ersichtlich, dass  die belangte Behörde (FA) am 6.3.2018 mittels Bescheid gemäß § 92 Abs. 1 lit. c BAO  feststellte, dass hinsichtlich des **Daniel Parys** (Beschwerdeführer, Bf.) im Zeitraum 2014 bis 2016  keine Unternehmereigenschaft vorlag.

- missed: `Daniel Parys` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)

- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau Basyurt tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau **Basyurt** das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

- missed: `Basyurt` (person)
- predicted in sentence: `Bf-Gatte`, `Bf-Gatte`

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_306`)

Wenn **Dr. YYY** nach Wien  kommt stelle ich ihm ein Kraftfahrzeug zur freien Verfügung.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/132902.1`) (sent_id: `deanon_BFG_20260814_TEST/132902.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache **James Eisenbürger**, Tulzergasse 6, 5431 Garnei, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 16. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerdevorentscheidung vom 12.4.2021 wird gemäß § 279 Abs. 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

- missed: `James Eisenbürger` (person)
- predicted in sentence: —

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_250`)

Abgesehen davon verfügt **Amanda Zacharek** als Fachärztin für Kinder- und Jugendheilkunde daneben  ohnehin über eine Zusatzqualifikation in dem – von der Bf monierten - Fach "Humangenetik"  und ist als langjährige Ambulanzleiterin, darunter der Ambulanz für Klinische Genetik, ua. auch  mit der Betreuung von Patienten mit einer – wie hier - seltenen Erkrankung befasst.

- missed: `Amanda Zacharek` (person)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_109`)

Dem  Beschwerdeführer steht daher für den Zeitraum Jänner bis Dezember als  Familienbeihilfenberechtigter für diesen Sohn gem. § 33 Abs. 3a Z 3 lit. a EStG 1988 sowie auch  im Fall eines Zustehens eines Unterhaltsabsetzbetrages gem. § 33 Abs. 3a Z 3 lit b EStG 1988  der Familienbonus Plus zu.  Aber auch betreffend den Sohn **Herbert Schaffarik**  steht dem Beschwerdeführer gem. § 33 Abs. 3a Z  3 lit. b EStG 1988 der Familienbonus Plus für die Monate Jänner bis Dezember zu, da der  Beschwerdeführer in diesem Zeitraum Unterhalt für diesen Sohn geleistet hat und ihm  infolgedessen, wie bereits unter Punkt 2 dargestellt, für diesen Zeitraum der  Unterhaltsabsetzbetrag zusteht.

- missed: `Herbert Schaffarik` (person)
- predicted in sentence: —

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)

Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn **Quentin Schwartkopp**  durch Übergabe übernommen  zu haben.

- missed: `Quentin Schwartkopp` (person)
- predicted in sentence: `Herrn Quentin`

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_14`)

Frau **Basyurt** wurde darauf hingewiesen, dass der Pkw innerhalb der nächsten 3 Wochen in  Österreich angemeldet wird;

- missed: `Basyurt` (person)
- predicted in sentence: —

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_39`)

Ergänzend wurde vom Finanzamt vorgebracht, dass sich **Mehmet Köprücü**  geweigert habe,  U/E Bescheide anzunehmen, sei keine unzulässige Einschränkung im Sinne des § 103 Abs 2  3 von 8 Seite 4 von 8

- missed: `Mehmet Köprücü` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132509.1`) (sent_id: `deanon_BFG_20260814_TEST/132509.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi über die am 09. März 2021 eingebrachte  Beschwerde des **Rocco Choudhury**, Wachtelgasse 7, 9543 Stadt, Österreich, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 25. Februar 2021, Zahl MA67/Zahl1/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 in der geltenden Fassung, in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, in der geltenden Fassung, zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird der Beschwerde insoweit stattgegeben, als die  verhängte Geldstrafe von € 60,00 auf € 36,00 und die für den Fall der Uneinbringlichkeit  festgesetzte Ersatzfreiheitsstrafe von 14 Stunden auf 9 Stunden herabgesetzt wird.

- missed: `Rocco Choudhury` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/144507.1`) (sent_id: `deanon_BFG_20260814_TEST/144507.1_55`)

Vom Bundessozialamt für Soziales und Behindertenwesen (Sozialministeriumservice) wurde in  der Folge der Gutachter **Dr. 2** mit der Erstellung eines neuen Gutachtens beauftragt.

- missed: `Dr. 2` (person)
- predicted in sentence: —

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_7`)

Die Bf brachte vor, dass ihre Tochter **Heidemarie Fitzenreiter**  während ihres Schulbesuches in Israel  nicht erwerbstätig und ledig gewesen sei, weshalb sie einen Unterhaltsanspruch gehabt habe.

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)

Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch **Prof. Yorick Frühbis**, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

- missed: `Prof. Yorick Frühbis` (person)
- predicted in sentence: `Mag. Hon.-Prof. Denis Hoffjan`, `Hon.-Prof.in Ariadne Iwanowsky`

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Mag.a Philippa Beßerdich  in der Beschwerdesache des DI  **Simone Philipzig**, Perovaweg 819, 8843 Feistritz am Kammersberg, Österreich, vertreten durch Hofer Leitinger Steuerberatung GmbH,  Geidorfgürtel 20, 8010 Graz, über die Beschwerde vom 8. September 2021 gegen den Bescheid  des FA Kirchdorf Perg Steyr  vom 9. Juli 2021 betreffend Einkommensteuer 2019 zur Steuernummer  59-060/2086  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Simone Philipzig` (person)
- predicted in sentence: `Mag.a Philippa Be`

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Merlin Morkam  in der Beschwerdesache des  **KzlR Jens Koudela, BSc**, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

- missed: `KzlR Jens Koudela, BSc` (person)
- predicted in sentence: `Hon.-Prof.in Merlin Morkam`

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_12`)

Begründend wurde wie folgt ausgeführt:  Sachverhalt:  Ihr Sohn **StR Armin Dürrwaechter**, geboren am 29. Januar 2024, studierte im Zeitraum vom Wintersemester  2020 bis inklusive Wintersemester 2021 "A033 630 Biologie" an der Universität Wien.

- missed: `StR Armin Dürrwaechter` (person)
- predicted in sentence: —

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142128.1`) (sent_id: `deanon_BFG_20260814_TEST/142128.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, den Richter  Mag.Dr. Wolfgang Pagitsch sowie die fachkundigen Laienrichter Manfred Fiala und **DI Thomas  Hrdinka** in der Beschwerdesache Saskia Spinnehörn, Gänsdorf 4, 4224 Wolfsegg, Österreich, vertreten durch BONAFIDE  Treuhand- und Revisions- gesellschaft m.b.H., Berggasse 10, 1090 Wien, über deren  Beschwerde vom 15. April 2019 gegen den Bescheid des Finanzamtes Österreich (vormals  Finanzamtes Wien 4/5/10 ) vom 5. April 2019 über die Abweisung einer Nachsicht von  Abgabenschuldigkeiten, Steuernummer 59-301/9085, nach Durchführung einer  mündlichen Verhandlung am 12. September 2023 in Anwesenheit der Schriftführerin Nadine  Bernold zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `DI Thomas  Hrdinka` (person)
- predicted in sentence: `Dr. Anna Radschek`, `Dr. Wolfgang Pagitsch`

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/135304.1`) (sent_id: `deanon_BFG_20260814_TEST/135304.1_1`)

BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich in der Revisionssache  **Basil Vanak**, Oberhof 221, 8345 Trössing, Österreich, über den Antrag des Finanzamtes für Großbetriebe, der zur Zahl  RR/7100124/2021 protokollierten außerordentlichen Revision gegen das Erkenntnis des BFG  vom 24.08.2021, RV/7101805/2021, betreffend   KESt-Rückzahlung gemäß § 21 Abs. 1 Z. 1a KStG 1988 die aufschiebende Wirkung  zuzuerkennen, beschlossen:  Dem Antrag der Revisionswerberin wird stattgegeben und die aufschiebende Wirkung  gemäß § 30 Abs. 2 VwGG zuerkannt.

- missed: `Basil Vanak` (person)
- predicted in sentence: `Mag. Dieter Fr`, `Revisionssache  Basil Vanak`

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_21`)

Dazu führte die belangte Behörde in der Stellungnahme vom 1. April 2024 aus, das Schreiben  des Masseverwalters **Dr. Pohlhammer** bezüglich nicht abgeholter Post langte am 14.07.2023,  dem selben Tag, an dem auch die Spruchsenatsverhandlung stattfand, beim Finanzamt  Österreich ein und konnte somit der Umstand der vom Beschuldigten nicht abgeholten  Poststücke in der Spruchsenatsverhandlung nicht berücksichtigt werden.

- missed: `Dr. Pohlhammer` (person)
- predicted in sentence: —

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_13`)

Die beschwerdeführende **Olga Kendziora, Bakk. rer. nat.** (Beschwerdeführerin, abgekürzt: Bf.),  Firmenbuchnummer FN 1, hat Frau A als alleinige Geschäftsführerin und Frau C B als alleinige  Gesellschafterin (Firmenbuchauszug: BFG-Akt I zu GZ. RV/7102163/2018, Bl. 107)  2)

- missed: `Olga Kendziora, Bakk. rer. nat.` (person)
- predicted in sentence: `Olga Kendziora, Bakk. rer. nat. `

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_141`)

Dieser hat im Zuge der gleichzeitig stattfindenden GPLA-Prüfung niederschriftlich bekanntgegeben, dass die Firmengründung in Slowenien nur deshalb erfolgte, weil **N.N.** dies so wollte, weil er sich für A., der in Wirklichkeit während des gesamten Prüfungszeitraumes (2012 - 2015) als Dienstnehmer für ihn beschäftigt war, die Lohn- und Sozialabgaben ersparen wollte.

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/145862.1`) (sent_id: `deanon_BFG_20260814_TEST/145862.1_5`)

Der beantragte Familienbonus Plus für das Kind KzlR Frederik Schreinemachers,  geboren am **Hagen Averhof**, wurde vollständig berücksichtigt.

- missed: `Hagen Averhof` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_8`)

Mit Eingangsdatum 14.07.2023 (Poststempel Finanzamt Österreich) ging von Rechtsanwalt  Dr. Harald Pohlhammer (Masseverwalter von **Dipl.-Ing. Heinz Riechels**) ein Schreiben samt Übermittlung von  2 RSa Briefen ein.

- missed: `Dipl.-Ing. Heinz Riechels` (person)
- predicted in sentence: `Dr. Harald Pohlhammer`

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/131231.1`) (sent_id: `deanon_BFG_20260814_TEST/131231.1_3`)

Das Einkommen des Gruppenmitgliedes **Cathleen Gottschlag**  im Jahr 2014 wird mit 2.678.126,39 Euro  festgesetzt.

- missed: `Cathleen Gottschlag` (person)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_1`)

BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rita Wiersbicki  in der Beschwerdesache Corvin Billmaier,  Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich, vertreten durch **Mag. Aleksandar Hofstätter**, Johann-Strauß-Gasse 4-6//2/5,  1040 Wien, betreffend Beschwerde vom 10. Juli 2023 gegen den Bescheid des Finanzamtes  Österreich vom 2. September 2022 betreffend Einkommensteuer 2021 Steuernummer  23-971/7442  beschlossen:   Die Beschwerde vom 10. Juli 2023 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a  BAO als nicht rechtzeitig eingebracht zurückgewiesen.

- missed: `Mag. Aleksandar Hofstätter` (person)
- predicted in sentence: `Priv.-Doz.in Rita Wiersbicki`, `Corvin Billmaier`

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache **Adriana Eiffler**, Waldhofweg 36a, 8321 Entschendorf, Österreich, betreffend Beschwerde vom 24. Februar 2021  gegen die Bescheide des Finanzamtes Österreich vom 9. Oktober 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 78-550/2209, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

- missed: `Adriana Eiffler` (person)
- predicted in sentence: `Dr. Ansgar Unterberger`, `Beschwerdesache Adriana Eiffler`

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Univ.-Prof.in Ada Forstner  in der Beschwerdesache des  **Elias von Wnuk-Lipinski**, Kolo-Moser-Weg 3, 4190 Affetschlag, Österreich, über die Beschwerde vom 13.Mai 2020 (beim Finanzamt  eingelangt am 14.Mai 2020) gegen den Bescheid des FA St. Johann Tamsweg Zell am See  vom 5. Mai 2020 betreffend  Zurückweisung eines Antrages vom 6.April 2020 auf Wiederaufnahme (§ 303 Abs. 1 BAO) des  Einkommensteuerbescheides 2010 vom 16.Mai 2014 (eingebracht am 7.April 2020 zur  Steuernummer 26-066/9346 ) zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Elias von Wnuk-Lipinski` (person)
- predicted in sentence: `Univ.-Prof.in Ada Forstner`

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/132841.1`) (sent_id: `deanon_BFG_20260814_TEST/132841.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache **OSR Juliette Franzisi**, Spitzesed 172, 4673 Baumgarting, Österreich, über die Beschwerde vom 17. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 17. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 47-760/2078  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `OSR Juliette Franzisi` (person)
- predicted in sentence: —

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/145954.1`) (sent_id: `deanon_BFG_20260814_TEST/145954.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache **Christoph Stofmeel**, Hasibederstraße 60, 3972 Scheiben, Österreich, über die Beschwerde vom 10. Mai 2023 gegen  den Bescheid des Finanzamtes Österreich vom 26. April 2023 betreffend  Rückforderungsbescheid vom 26. April 2023 betreffend Familienbeihilfe und  Kinderabsetzbetrag für V Y sowie Familienbeihilfe betreffend E X-P  für Oktober 2022 bis März  2023 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Christoph Stofmeel` (person)
- predicted in sentence: `Mag. Helga Hochrieser`, `Beschwerdesache Christoph Stofmeel`

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_149`)

Die  Mutationen sind auch in Österreich angekommen und verschärfen die Situation deutlich", sagte  Bundeskanzler Sebastian Kurz bei einer Pressekonferenz im Bundeskanzleramt, bei der er  gemeinsam mit Gesundheitsminister Rudolf Anschober, Steiermarks Landeshauptmann  Hermann Schützenhöfer, Wiens Bürgermeister **Michael Ludwig** und Univ.-Prof. Dr. Oswald  Wagner, Vizerektor der MedUni Wien und Leiter des klinischen Institutes für Labormedizin, über  die Verlängerung des Lockdowns bis 8. Februar informierte.

- missed: `Michael Ludwig` (person)
- predicted in sentence: `Univ.-Prof. Dr. Oswald  Wagner`

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_304`)

Dort habe ich die lebensrettenden Behandlung durch **Dr. YYY** erhalten.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache **Gotthard Kirchhoffs**, Unterriese 2, 7432 Oberschützen, Österreich, vertreten durch WWV-GROUP  SteuerberatungsGmbH, Bahnhofstraße 4, 3950 Gmünd, über die Beschwerde vom  28. September 2021 gegen die Bescheide des Finanzamtes Österreich vom 7. Juli 2021  betreffend Haftung für Lohnsteuer, Dienstgeberbeitrag und Zuschlag zum Dienstgeberbeitrag  für die Jahre 2015 bis 2019, Steuernummer 19-927/9012, zu Recht erkannt:   I. Der Beschwerde gegen die Bescheide betreffend Festsetzung des Zuschlags zum  Dienstgeberbeitrag 2015 bis 2019 wird gemäß § 279 BAO Folge gegeben.

- missed: `Gotthard Kirchhoffs` (person)
- predicted in sentence: `Mag. Anna Mechtler`, `Beschwerdesache Gotthard Kirchhoffs`

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_338`)

**Dr. YYY** ist  außerdem hauptsächlich bei Krankenbesuchen im Buschland unterwegs, also nicht im  eigentlichen Krankenhaus.

- missed: `Dr. YYY` (person)
- predicted in sentence: —

</details>

---

