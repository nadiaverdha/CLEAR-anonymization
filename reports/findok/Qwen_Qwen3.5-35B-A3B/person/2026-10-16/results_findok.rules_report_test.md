# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (TEST)

Generated on: 2026-10-16T13:42:18.935370

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
| Accuracy (exact match) | 98.6% |
| True Positives | 675 |
| False Positives | 390 |
| False Negatives | 939 |
| Total Gold Entities | 1614 |
| Micro Precision | 63.4% |
| Micro Recall | 41.8% |
| Micro F1 | 50.4% |
| Macro F1 | 50.4% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Specific_Name_Trapkowski` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Dr_G_Anonymized` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Beschwerdesache_Name_Context` | 27.5% | 89.4% | 16.2% | 293 | 262 | 31 |
| `Hon_Prof_in_Name` | 9.1% | 79.6% | 4.8% | 98 | 78 | 20 |
| `Mag_Title` | 1.4% | 73.3% | 0.7% | 15 | 11 | 4 |
| `Dr_Title` | 13.8% | 66.0% | 7.7% | 188 | 124 | 64 |
| `Herrn_Name_Full` | 4.3% | 63.2% | 2.2% | 57 | 36 | 21 |
| `Priv_Dozi_Title` | 4.5% | 62.3% | 2.4% | 61 | 38 | 23 |
| `Herr_Frau_Name_Context` | 7.7% | 62.3% | 4.1% | 106 | 66 | 40 |
| `Dr_in_Title` | 2.3% | 61.3% | 1.2% | 31 | 19 | 12 |
| `Ing_Title` | 2.8% | 51.1% | 1.4% | 45 | 23 | 22 |
| `OStR_Title` | 0.1% | 50.0% | 0.1% | 2 | 1 | 1 |
| `M_Anonymized` | 1.3% | 30.6% | 0.7% | 36 | 11 | 25 |
| `Durch_Richter_Name` | 0.1% | 11.1% | 0.1% | 9 | 1 | 8 |
| `Antragsteller_Name` | 0.1% | 2.3% | 0.1% | 43 | 1 | 42 |
| `Complainant_Beschwerdesache` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Role_Followed_Name` | 0.0% | 0.0% | 0.0% | 12 | 0 | 12 |
| `Email_Header_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Representative_Dr_Mag` | 0.0% | 0.0% | 0.0% | 27 | 0 | 27 |
| `Specific_Name_Pascal_Tebbe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Lumplecker_Deych` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Gewert` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Maerkl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Joern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `RA_Mag_Start` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Anonymized_Names` | 0.0% | 0.0% | 0.0% | 5 | 0 | 5 |
| `Anonymized_Names_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Complainant_Des_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ing_Short_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Complex_Title_Combo` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Felicitas_Niedermann` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Zeno_Schickhuber` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Claire_Hilt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Adam_Safak` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Zlatan_Frauenknecht` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Niederschrift_Name` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `OMedR_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gertrude_Haidary_Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sachverständigengutachten_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Wendelin_Polmanns` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Heiko_Dwortzak` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Marilyn_Sturtzebecher` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Raphael_Venclik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Muran_Waldhans` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific_Name_Dimitri_Kozlowska` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
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
| `Beschwerdesache_Full_Name` | 0.0% | 0.0% | 0.0% | 19 | 0 | 19 |
| `KR_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gutachten_Dr_Name` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Richter_Name_Context` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frau_Name_Specific` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `VetR_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KommR_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Maga_Title` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Beschwerdesache_Standalone_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `CD_Techn_R_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frau_Name_Full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dr_Initial_Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>📋 All Rules</summary>

## `Specific_Name_Trapkowski` 

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

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
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 0 | 1612 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138435.1`) (sent_id: `deanon_BFG_20260814_TEST/138435.1_128`)


Dass die Kindesmutter den Anspruch auf die Ausgleichszahlung  hat (Art 67 VO (EU) 883/2004) und diesen mit dem Antrag vom 3.Jänner 2022 auch geltend  machte, ändert daran nichts (vgl. EuGH 22.10.2015, C-378/14 – Tomislaw Trapkowski und  VwGH 12.11.2019, Ra 2019/16/0133, je mwV).

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_35`)


44 Insoweit ist darauf hinzuweisen, dass Art. 67 der Verordnung Nr. 883/2004 den Grundsatz  festlegt, dass eine Person Anspruch auf Familienleistungen für Familienangehörige, die in einem  anderen als dem für die Gewährung dieser Leistungen zuständigen Mitgliedstaat wohnen, so  erheben kann, als würden sie in dem zuständigen Mitgliedstaat wohnen (Urteil vom 22.  Oktober 2015, Trapkowski, C-378/14, EU:C:2015:720, Rn. 35).

| Predicted | Gold |
|---|---|
| `Trapkowski` | `Trapkowski` |

</details>

---

## `Dr_G_Anonymized` 

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

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
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 2 | 0 | 1612 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_115`)


Es wurden einvernehmlich nicht nur Befunde beurteilt, sondern auch ausführliche persönliche  Gespräche mit Frau Mag. D (Neuropsychologisches Gutachten) und OA. Dr. G (Neuropädiaterin)  geführt.

| Predicted | Gold |
|---|---|
| `Dr. G` | `Dr. G` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_258`)


Zu diesem Zweck wurde, wie aus dem  Erstgutachten hervorkommt, nicht nur eine Vielzahl von bisher vorliegenden Befunden und  Untersuchungsergebnissen mitberücksichtigt, sondern wurde zusätzlich mit zwei der  behandelnden Ärztinnen, nämlich Mag. D (Neuropsychologischer Befund) und OA Dr. G  (Neuropädiaterin), ausführlich persönliche Rücksprache zur eingehenden Erhebung ua. der  anamnestischen Daten gehalten.

| Predicted | Gold |
|---|---|
| `Dr. G` | `Dr. G` |

</details>

---

## `Beschwerdesache_Name_Context` 🏆

**F1:** 0.275 | **Precision:** 0.894 | **Recall:** 0.162  

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
| 0.894 | 0.162 | 0.275 | 293 | 262 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 262 | 31 | 1352 |

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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lewis Rzehula` | `Lewis Rzehula` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Neustädterstraße 3, 9560 Wabl, Österreich` (address)
- `43-839/6567` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Siegfried Basyurt` | `Siegfried Basyurt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Cassandra Witzenhause` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129038.1`) (sent_id: `deanon_BFG_20260814_TEST/129038.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache Chen Walcker, Garelligasse 45, 3443 Rappoltenkirchen, Österreich, über die Beschwerde vom 14. Mai 2019 gegen die Bescheide des Finanzamtes Wien  12/13/14 Purkersdorf vom 6. Mai 2019 betreffend Pfändung eines Bankguthabens gemäß § 65  AbgEO und Festsetzung von Gebühren und Auslagenersätzen des Vollstreckungsverfahrens  gemäß § 26 AbgEO, Steuernummer 63-698/2600  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben und die angefochtenen Bescheide  aufgehoben.

| Predicted | Gold |
|---|---|
| `Chen Walcker` | `Chen Walcker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Garelligasse 45, 3443 Rappoltenkirchen, Österreich` (address)
- `Finanzamtes Wien  12/13/14 Purkersdorf` (organisation)
- `63-698/2600` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129004.1`) (sent_id: `deanon_BFG_20260814_TEST/129004.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Hedwig Mackiewicz, Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich, über die Beschwerde vom 17. November 2019 gegen den Bescheid  des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. November 2019 betreffend  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Oktober 2017  bis September 2019 zu Recht erkannt:   Der Beschwerde wird im Sinne der Beschwerdevorentscheidung vom 20.3.2020 gemäß   § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hedwig Mackiewicz` | `Hedwig Mackiewicz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Hans Palm-Straße 4, 8241 Hohenau am Wechsel, Österreich` (address)
- `Finanzamtes Wien 12/13/14 Purkersdorf` (organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ursula Buchholz` | `Ursula Buchholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Li Schukardt` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Chantal Eligüzel` | `Chantal Eligüzel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Sven Oberstelehn` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

| Predicted | Gold |
|---|---|
| `Sven Mitterhuber` | `Sven Mitterhuber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Mag.a Livia Korowski` (person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Roxana Dellner` | `Roxana Dellner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Anna Mechtler-Höger` (person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich` (address)
- `RA Mag. Robert Bitsche` (person)
- `Magistrats der Stadt Wien` (organisation)
- `88-034/0292` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129568.1`) (sent_id: `deanon_BFG_20260814_TEST/129568.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Laetitia Kuban, Karawankenplatz 8, 8046 Graz, Österreich, über die Beschwerde vom 16. Dezember 2020 gegen den Bescheid des Finanzamtes  Wien 2/20/21/22 vom 14. November 2019 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für das Kind x in den Zeiträumen vom 01.07.2018 bis zum 30.09.2018  sowie vom 01.07.2019 bis zum 30.09.2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Laetitia Kuban` | `Laetitia Kuban` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karawankenplatz 8, 8046 Graz, Österreich` (address)
- `Finanzamtes  Wien 2/20/21/22` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129984.1`) (sent_id: `deanon_BFG_20260814_TEST/129984.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wladimir Dammkoehler, Grolzham 15, 3123 Obermerking, Österreich, über die Beschwerde vom 24. Jänner 2020  gegen den Bescheid des Finanzamtes Baden Mödling vom 22. Jänner 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017, Steuernummer 47-339/1168, zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Wladimir Dammkoehler` | `Wladimir Dammkoehler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Grolzham 15, 3123 Obermerking, Österreich` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `47-339/1168` (tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130002.1`) (sent_id: `deanon_BFG_20260814_TEST/130002.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karin Pitzer in der Beschwerdesache  Karina Ditzler, Hochkoglweg 21, 9560 Nadling, Österreich, über die Beschwerde gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 14. Oktober 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Karina Ditzler` | `Karina Ditzler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Karin Pitzer` (person)
- `Hochkoglweg 21, 9560 Nadling, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Manuela Fischer in der  Beschwerdesache Isidor Czebulla, Eggenburger Straße 88, 9423 Pfaffendorf, Österreich, vertreten durch TPA Steuerberatung GmbH,  Praterstraße 62-64, 1020 Wien, über die Beschwerde vom 5. Dezember 2016 gegen die  Bescheide des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 7. November 2016  betreffend Dienstgeberbeitrag (DB) und Zuschlag zum Dienstgeberbeitrag (DZ) für die Jahre  2010 bis 2013   zu Recht erkannt.

| Predicted | Gold |
|---|---|
| `Isidor Czebulla` | `Isidor Czebulla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Manuela Fischer` (person)
- `Eggenburger Straße 88, 9423 Pfaffendorf, Österreich` (address)
- `TPA Steuerberatung GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Heinz Herper` | `Heinz Herper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich` (address)
- `Dr. Thomas Hofer-Zeni` (person)
- `Finanzamtes Wien 2/20/21/22` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Floriane Rötker` | `Floriane Rötker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn` (person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich` (address)
- `Heinz Neuböck Wthrd GmbH` (organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130809.1`) (sent_id: `deanon_BFG_20260814_TEST/130809.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. RR. in der Beschwerdesache Melanie Mavromatakis,  Urbanusgasse 1, 3491 Obernholz, Österreich, über die Beschwerde vom 8. Juni 2018 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 9. Mai 2018 betreffend Umsatzsteuer 2014 bis 2017, Steuernummer , zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melanie Mavromatakis` | `Melanie Mavromatakis` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Urbanusgasse 1, 3491 Obernholz, Österreich` (address)
- `Finanzamtes  Wien 1/23` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/131211.1`) (sent_id: `deanon_BFG_20260814_TEST/131211.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Caroline Schröer  in der Beschwerdesache Charlotte Beha,  Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich, gegen den Bescheid des Finanzamtes Salzburg-Stadt vom 17. Dezember 2019,  betreffend Wiederaufnahme des Verfahrens hinsichtlich Einkommensteuer 2017, zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Charlotte Beha` | `Charlotte Beha` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Caroline Schröer` (person)
- `Horndorfstraße 9, 4222 Stacherlsiedlung, Österreich` (address)
- `Finanzamtes Salzburg-Stadt` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/131265.1`) (sent_id: `deanon_BFG_20260814_TEST/131265.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Wieland Gorecki, Minnesängerplatz 17, 4772 Messenbach, Österreich, über die Beschwerde vom 25. Februar 2013  gegen den Bescheid des Finanzamtes Österreich vom 5. Februar 2013 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Wieland Gorecki` | `Wieland Gorecki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Helga Hochrieser` (person)
- `Minnesängerplatz 17, 4772 Messenbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Hartwig Simonson, Neubruchgasse 122L, 9562 Flatschach, Österreich, über die Beschwerde vom 11. Februar 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 11. Jänner 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und die Beschwerde vom 7. März 2019  gegen den Bescheid des Finanzamtes Grieskirchen Wels vom 8. Februar 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hartwig Simonson` | `Hartwig Simonson` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `Neubruchgasse 122L, 9562 Flatschach, Österreich` (address)
- `Finanzamtes` (organisation)
- `Finanzamtes` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131663.1`) (sent_id: `deanon_BFG_20260814_TEST/131663.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Kai Rüben,  Obergratschach 5, 4812 Neuhofen, Österreich, über die Beschwerde vom 4. April 2019 gegen den Bescheid des Finanzamtes  Österreich (bisher Finanzamt Wien 2/20/21/22) vom 5. März 2019 betreffend die  Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum Februar 2016  bis Juni 2017 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Kai Rüben` | `Kai Rüben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Obergratschach 5, 4812 Neuhofen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Sulamith Hördegen, Witzmannsdorf 4, 3804 Bernschlag, Österreich, vertreten durch Magistrat der Stadt Wien Wiener Kinder- und  Jugendhilfe, Gasgasse 8-10, 1150 Wien, über die Beschwerde vom 26. August 2020 gegen den  Bescheid des Finanzamtes Österreich vom 11. August 2020 betreffend Abweisung des Antrages  auf Familienbeihilfe 05.2019-07.2020 zu Recht erkannt:  Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Sulamith Hördegen` | `Sulamith Hördegen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Witzmannsdorf 4, 3804 Bernschlag, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


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

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131930.1`) (sent_id: `deanon_BFG_20260814_TEST/131930.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache Martin Kruthof, Schachet 8A, 9500 Obere Fellach, Österreich, betreffend Beschwerde vom 14. April 2010 gegen die Bescheide des FA Hollabrunn  Korneuburg Tulln vom 31. März 2010 betreffend Wiederaufnahme des Verfahrens betreffend  Umsatzsteuer 2008 und Umsatzsteuer 2008 Steuernummer beschlossen:   Die Beschwerde vom 14. April 2010 wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Martin Kruthof` | `Martin Kruthof` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Schachet 8A, 9500 Obere Fellach, Österreich` (address)
- `FA Hollabrunn  Korneuburg Tulln` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/131988.1`) (sent_id: `deanon_BFG_20260814_TEST/131988.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Dominik Moebus,  Aichach 11m, 9375 Knappenberg, Österreich, vertreten durch Magistrat der Stadt Wien, Kinder- und Jugendhilfe,  Rechtsvertretung 16,17,18,19, Kalvarienberggasse 29, 1170 Wien, betreffend die Beschwerde  vom 25. August 2020 gegen den Abweisungsbescheid des Finanzamtes Österreich (bisher  Finanzamt Wien 2/20/21/22) vom 17. Juli 2020 betreffend Familienbeihilfe ab Jänner 2016  beschlossen:   Der am 12. Jänner 2021 eingebrachte, mit 07. Jänner 2021 datierte Vorlageantrag betreffend  die am 04. Dezember 2020 zugestellte Beschwerdevorentscheidung vom 12. November 2020  wird gemäß § 264 Abs 4 lit e BAO iVm § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dominik Moebus` | `Dominik Moebus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Aichach 11m, 9375 Knappenberg, Österreich` (address)
- `Magistrat der Stadt Wien` (organisation)
- `Finanzamtes Österreich` (organisation)
- `Finanzamt Wien 2/20/21/22` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Pawel Schuwirth  in der Beschwerdesache Griselda Hälmle,  Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich, über die Beschwerde vom 24. Oktober 2018 gegen die Bescheide des  Finanzamtes Landeck Reutte (jetzt Finanzamt Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2016 und 2017, Steuernummer  49-622/1059, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Griselda Hälmle` | `Griselda Hälmle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Pawel Schuwirth` (person)
- `Dr.-Franz-Böss-Gasse 408, 3323 Berghof, Österreich` (address)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)
- `49-622/1059` (tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/132231.1`) (sent_id: `deanon_BFG_20260814_TEST/132231.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Regina Vogt in der Beschwerdesache  Madeleine Göpffarth, Robert Weiner-Straße 23, 5524 Klockau, Österreich, über die Beschwerde vom 26. März 2020 gegen den Bescheid des  Finanzamtes Österreich vom 28. Februar 2020 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum Juli 2019 bis November 2019 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen..

| Predicted | Gold |
|---|---|
| `Madeleine Göpffarth` | `Madeleine Göpffarth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Regina Vogt` (person)
- `Robert Weiner-Straße 23, 5524 Klockau, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ida Gündüz` | `Ida Gündüz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Jaden Mikulla` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


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

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/132456.1`) (sent_id: `deanon_BFG_20260814_TEST/132456.1_2`)


Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Xaver Hüttenroth, Molzbichl 501, 4084 Etzing, Österreich, über die Beschwerde vom 10. Februar 2020 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt vom 20. Jänner 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 zu Steuernummer 33 57-139/5207  zu Recht erkannt:  A) Gemäß § 279 BAO wird der Beschwerde stattgegeben, und es wird der angefochtene  Bescheid abgeändert.

| Predicted | Gold |
|---|---|
| `Xaver Hüttenroth` | `Xaver Hüttenroth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Molzbichl 501, 4084 Etzing, Österreich` (address)
- `Finanzamtes  Neunkirchen Wr. Neustadt` (organisation)
- `57-139/5207` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Gudrun Terzoglou  in der Beschwerdesache Ruprecht Berkenkämper,  Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich ,Land, über die Beschwerde vom 28. August 2016 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 26. Juli 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015, Steuernummer 98-086/6338, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ruprecht Berkenkämper` | `Ruprecht Berkenkämper` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Gudrun Terzoglou` (person)
- `Am Übungsplatz 61, 9220 Velden am Wörther See, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `98-086/6338` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


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

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


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

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/132579.1`) (sent_id: `deanon_BFG_20260814_TEST/132579.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinIBV in der Beschwerdesache Melchior Englmaier,  Ibertsberg 13, 7132 Apetlon, Österreich, über die Beschwerde vom 15. September 2020 gegen den  Abweisungsbescheid des Finanzamtes Bruck Eisenstadt Oberwart (nunmehr Finanzamt  Österreich) vom 20. August 2020 betreffend Familienbeihilfe für die Tochter TO für die  Monate April 2020 und Mai 2020 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Melchior Englmaier` | `Melchior Englmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ibertsberg 13, 7132 Apetlon, Österreich` (address)
- `Finanzamtes Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt  Österreich` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Melchior Harasymiw,  Mariensteinweg 13, 4672 Pühret, Österreich, über die Beschwerde vom 15. April 2020 gegen den Abweisungsbescheid des  Finanzamtes Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 7. April 2020  betreffend Familienbeihilfe für das Kind To, geb. 1998, für die Monate März 2020 und April  2020, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Melchior Harasymiw` | `Melchior Harasymiw` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mariensteinweg 13, 4672 Pühret, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_1`)


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

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/132834.1`) (sent_id: `deanon_BFG_20260814_TEST/132834.1_2`)


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

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Holger Buchmüller` | `Holger Buchmüller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/132902.1`) (sent_id: `deanon_BFG_20260814_TEST/132902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache James Eisenbürger, Tulzergasse 6, 5431 Garnei, Österreich, gegen den Bescheid des Finanzamtes Österreich vom 16. März 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 zu Recht erkannt:   Die Beschwerdevorentscheidung vom 12.4.2021 wird gemäß § 279 Abs. 1 BAO infolge  Unzuständigkeit der belangten Behörde ersatzlos aufgehoben.

| Predicted | Gold |
|---|---|
| `James Eisenbürger` | `James Eisenbürger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Tulzergasse 6, 5431 Garnei, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/133237.1`) (sent_id: `deanon_BFG_20260814_TEST/133237.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Pjotr Übereiter  in der Beschwerdesache Linn Gouthier,  M - Dorfplatzweg 28, 4731 Ritzing, Österreich, über die Beschwerde vom 20. November 2017 gegen den Bescheid des  Finanzamtes Graz-Stadt vom 2. November 2017 betreffend Umsatzsteuer-

| Predicted | Gold |
|---|---|
| `Linn Gouthier` | `Linn Gouthier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Pjotr Übereiter` (person)
- `M - Dorfplatzweg 28, 4731 Ritzing, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/133255.1`) (sent_id: `deanon_BFG_20260814_TEST/133255.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die RichterinRi in der Beschwerdesache Marcel Rac, Zwerchackerweg 264, 4115 Weigelsdorf, Österreich, über die Beschwerde vom 11. Mai 2020 gegen den Bescheid des Finanzamtes Wien  8/16/17 vom 5. Mai 2020, Steuernummer 42-508/7924, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019   zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Marcel Rac` | `Marcel Rac` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zwerchackerweg 264, 4115 Weigelsdorf, Österreich` (address)
- `Finanzamtes Wien  8/16/17` (organisation)
- `42-508/7924` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_1`)


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

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


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

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/133934.1`) (sent_id: `deanon_BFG_20260814_TEST/133934.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Heidemarie Winkler in der  Beschwerdesache Sven Hoerlin, Padasterjochhaus 6, 9562 Tobitsch, Österreich, gegen den Bescheid  des Finanzamtes Spittal  Villach vom 17. November 2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2013 Steuernummer 51-093/9549  folgenden Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Sven Hoerlin` | `Sven Hoerlin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Heidemarie Winkler` (person)
- `Padasterjochhaus 6, 9562 Tobitsch, Österreich` (address)
- `Finanzamtes Spittal  Villach` (organisation)
- `51-093/9549` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/134223.1`) (sent_id: `deanon_BFG_20260814_TEST/134223.1_1`)


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

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


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

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


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

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_1`)


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

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/134451.1`) (sent_id: `deanon_BFG_20260814_TEST/134451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Mag. Wladimir Beheim  in der Beschwerdesache Bruno Rüttgers,  Krumpendorfer Straße 43, 3873 Gopprechts, Österreich, vertreten durch Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG,  Kirchengasse 4, 8680 Mürzzuschlag, betreffend Beschwerde vom 2. November 2006 gegen den  Bescheid des FA Klagenfurt St. Veit Wolfsberg  vom 29. September 2006 betreffend Festsetzung von Anspruchszinsen  beschlossen:   Der Bescheid betreffend Festsetzung von Anspruchszinsen 2001 scheidet aus dem  Rechtsbestand aus.

| Predicted | Gold |
|---|---|
| `Bruno Rüttgers` | `Bruno Rüttgers` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Wladimir Beheim` (person)
- `Krumpendorfer Straße 43, 3873 Gopprechts, Österreich` (address)
- `Mag. Rothwangl & Partner Steuerberatungs GmbH & Co KG` (organisation)
- `FA Klagenfurt St. Veit Wolfsberg` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


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

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_1`)


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

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/134655.1`) (sent_id: `deanon_BFG_20260814_TEST/134655.1_1`)


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

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Janis Dührkopp, Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich, vertreten durch B O S Bilanz- Organisations- und  Steuerservice GmbH, Graben 29 A, 1010 Wien, über die Beschwerde vom 2. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 2/20/21/22 vom 31. März 2016 betreffend  Einkommensteuer 2010, 2011 und 2012 und betreffend Umsatzsteuer 2010, 2011 und 2012  sowie über die Beschwerde vom 25. Oktober 2016 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 28. September 2016 betreffend Einkommensteuer 2013 zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Janis Dührkopp` | `Janis Dührkopp` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Thomas Leitner` (person)
- `Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamtes Wien  2/20/21/22` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Ingrid Dohrmaier` | `Ingrid Dohrmaier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Hans Blasina` (person)
- `Daläus 14O, 2301 Wittau, Österreich` (address)
- `Korber & Partner WTH-Stb  GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Finanzamtes Österreich` (organisation)
- `41-654/1190` (tax_number)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Walter Guggenmoos` | `Walter Guggenmoos` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Alice Schöpfel` (person)
- `Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich` (address)
- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `79-464/0427` (tax_number)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Carla Winterkorn, Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich, über die Beschwerde vom 17. April 2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 19. März 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer 43-645/1612  zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Carla Winterkorn` | `Carla Winterkorn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Helmut Mittermayr` (person)
- `Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `43-645/1612` (tax_number)

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/135210.1`) (sent_id: `deanon_BFG_20260814_TEST/135210.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterX in der Beschwerdesache Desiree Ince, Geigergasse 49, 5324 Hintersee, Österreich, über die Beschwerde vom 19. September 2019 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf vom 6. September 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 47-822/3731  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Desiree Ince` | `Desiree Ince` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Geigergasse 49, 5324 Hintersee, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `47-822/3731` (tax_number)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Mag. Leander Hättrich  in der Beschwerdesache Edith Grotehenn,  Karlhofstraße 20, 4212 Götschka, Österreich, vertreten durch Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Operngasse 6/4/9, 1010 Wien, gegen den Bescheid des FA Wien  4/5/10 vom 05.09.2009 betreffend Körperschaftsteuer 2006 den Beschluss:  I. Die Beschwerde wird gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Edith Grotehenn` | `Edith Grotehenn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Leander Hättrich` (person)
- `Karlhofstraße 20, 4212 Götschka, Österreich` (address)
- `Crowe SOT GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `FA Wien  4/5/10` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/135373.1`) (sent_id: `deanon_BFG_20260814_TEST/135373.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Judith Daniela Herdin-Winter in der  Beschwerdesache Juri Siebgen, Josef Maurergasse 2, 5424 Riedl, Österreich, vertreten durch MITTEREGGER Steuerberatungs  GmbH, Opfergasse 12, 2630 Ternitz, über die Beschwerde vom 13. Mai 2018 gegen den  Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr Finanzamt Österreich) vom  13. April 2018 betreffend Einkommensteuer 2017 Steuernummer 35-670/1415, zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Juri Siebgen` | `Juri Siebgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Judith Daniela Herdin-Winter` (person)
- `Josef Maurergasse 2, 5424 Riedl, Österreich` (address)
- `MITTEREGGER Steuerberatungs  GmbH` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamt Österreich` (organisation)
- `35-670/1415` (tax_number)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Andreas Kuschy  in der Beschwerdesache Angelika Oligschleger,  Friedhofgasse, Rattersdorf 3, 9971 Tauer, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des Finanzamt Innsbruck  vom 29. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020,  Steuernummer 49-970/7545  nach dem Einlangen des Vorlageantrages vom 10.6.2021  beschlossen:   Der Vorlageantrag wird gem. § 264 Abs 4 lit e Bundesabgabenordnung zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Angelika Oligschleger` | `Angelika Oligschleger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof. Andreas Kuschy` (person)
- `Friedhofgasse, Rattersdorf 3, 9971 Tauer, Österreich` (address)
- `Finanzamt Innsbruck` (organisation)
- `49-970/7545` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Silvius Jaros, Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich, über die Beschwerde vom 16. Mai 2019 gegen den Bescheid des  Finanzamtes Österreich vom 16. April 2019 betreffend Einkommensteuer 2017 Steuernummer  97-301/3674  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Silvius Jaros` | `Silvius Jaros` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Astrid Binder` (person)
- `Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `97-301/3674` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/135918.1`) (sent_id: `deanon_BFG_20260814_TEST/135918.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin MMag.Dr. Ingrid Fehrer in der  Beschwerdesache Ramon Reissdorf, Paul-Abl-Straße 9, 2822 Bromberg, Österreich, vertreten durch ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, und ECA Schmidt und  Hertwich Steuer- beratungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, über die  Beschwerde vom 17. September 2021 gegen die Bescheide des Finanzamtes Österreich vom  26. August 2021, Steuernummer 86-314/1061, betreffend Abweisung des Antrages auf  Wiederaufnahme der Verfahren hinsichtlich Einkommen- und Umsatzsteuer 2017, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Ramon Reissdorf` | `Ramon Reissdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MMag.Dr. Ingrid Fehrer` (person)
- `Paul-Abl-Straße 9, 2822 Bromberg, Österreich` (address)
- `ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H.` (organisation)
- `Finanzamtes Österreich` (organisation)
- `86-314/1061` (tax_number)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Lieselotte Stiglat  in der Beschwerdesache Sibylle Roßmayr,  Sierling 20, 3632 Pernthon, Österreich, vertreten durch RSM Austria Steuerberatung GmbH, Tegetthoffstraße 7, 1010  Wien, über die Beschwerde vom 16.11.2021 gegen den Bescheid des Finanzamtes Österreich  vom 5. November 2021 betreffend Verspätungszuschlag Umsatzsteuer 4-06/2021,  Steuernummer 58-418/2406  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Sibylle Roßmayr` | `Sibylle Roßmayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Lieselotte Stiglat` (person)
- `Sierling 20, 3632 Pernthon, Österreich` (address)
- `RSM Austria Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `58-418/2406` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Björn Stover, Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich, vertreten durch ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH, Landungsplatz 5, 4864  Attersee/Attersee, über die Beschwerde vom 14. September 2021 gegen die Bescheide des  Finanzamtes Österreich vom 23. August 2021 betreffend die Festsetzung von  Verspätungszuschlägen für die Monate 12/2020, 01/2021 und 03-05/2021, Steuernummer  57-952/0912, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Björn Stover` | `Björn Stover` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich` (address)
- `ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `57-952/0912` (tax_number)

**Example 77** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Elmira Baintner  in der Beschwerdesache Dietmar Grießmeyer,  Stiftgasse 12, 4654 Aigen, Österreich, über die Beschwerde vom 31. Juli 2021 gegen den Bescheid des FA Steiermark Mitte  vom  26. Juli 2021 betreffend Abweisung eines Rückzahlungsantrages, Steuernummer  64-502/6730, zu Recht erkannt:   I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dietmar Grießmeyer` | `Dietmar Grießmeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Elmira Baintner` (person)
- `Stiftgasse 12, 4654 Aigen, Österreich` (address)
- `FA Steiermark Mitte` (organisation)
- `64-502/6730` (tax_number)

**Example 78** (doc_id: `deanon_BFG_20260814_TEST/136273.1`) (sent_id: `deanon_BFG_20260814_TEST/136273.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Klaus Krupok  in der Beschwerdesache Ernst Eschenbrenner,  Irenental 58, 4871 Tiefenbach, Österreich, über die Beschwerde vom 11. August 2016 gegen den Bescheid des Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich)vom 13. Juli  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2015 Steuernummer  80-953/9265  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Ernst Eschenbrenner` | `Ernst Eschenbrenner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Klaus Krupok` (person)
- `Irenental 58, 4871 Tiefenbach, Österreich` (address)
- `Finanzamtes  Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `80-953/9265` (tax_number)

**Example 79** (doc_id: `deanon_BFG_20260814_TEST/136300.1`) (sent_id: `deanon_BFG_20260814_TEST/136300.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Susanne Türner, Viehdorfer Straße 25, 9853 Burgwiese, Österreich, gegen die Bescheide des Finanzamtes Hollabrunn Korneuburg  Tulln vom 25. November 2011 betreffend Körperschaftsteuer und Umsatzsteuer 2007,  Steuernummer 16-353/9813  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Susanne Türner` | `Susanne Türner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Andreas Stanek` (person)
- `Viehdorfer Straße 25, 9853 Burgwiese, Österreich` (address)
- `Finanzamtes` (organisation)
- `16-353/9813` (tax_number)

**Example 80** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Wolenski  in der Beschwerdesache Siegfried Beyazit,  Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich  über die Beschwerde vom 14. Mai 2016 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. März 2016 betreffend Einheitswert des land- u. forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Siegfried Beyazit` | `Siegfried Beyazit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Jacqueline Wolenski` (person)
- `Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 81** (doc_id: `deanon_BFG_20260814_TEST/136364.1`) (sent_id: `deanon_BFG_20260814_TEST/136364.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Patrick Hübben  in der Beschwerdesache Alice Rüde,  Auhub 26, 9560 Kraß, Österreich, vertreten durch BDO Steiermark GmbH Wtp u Stb, Schubertstraße 62, 8010  Graz, über die Beschwerde vom 18. März 2019 gegen den Bescheid des FA Tirol Ost  vom  26. Februar 2019 betreffend Abweisung eines Zahlungserleichterungsansuchens zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Alice Rüde` | `Alice Rüde` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Patrick Hübben` (person)
- `Auhub 26, 9560 Kraß, Österreich` (address)
- `BDO Steiermark GmbH Wtp` (organisation)
- `FA Tirol Ost` (organisation)

**Example 82** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Nadine Hupmann  in der Beschwerdesache Joachim Kotmann,  Weinbach 15, 8454 Saggau, Österreich, über die Beschwerde vom 10. Jänner 2020 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 13. Dezember 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe und Kinderabsetzbetrag  für den Zeitraum Juli 2018 bis Februar 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Joachim Kotmann` | `Joachim Kotmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof.in Nadine Hupmann` (person)
- `Weinbach 15, 8454 Saggau, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `FA Österreich` (organisation)

**Example 83** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Lewis Fröhner, Feldgasse, Rattersdorf 6, 6731 Boden, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 25. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Lewis Fröhner` | `Lewis Fröhner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Peter Steurer` (person)
- `Feldgasse, Rattersdorf 6, 6731 Boden, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 84** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Marion Schlesing  in der Beschwerdesache des  Dimitri Seewaldt, Sonnblickweg 22, 4263 Elmberg, Österreich, über die Beschwerde vom 15. November 2018 gegen den Bescheid  des FA Judenburg Liezen (jetzt Dienststelle des Finanzamtes Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zur Steuernummer 93-757/0582  zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dimitri Seewaldt` | `Dimitri Seewaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Hon.-Prof.in Marion Schlesing` (person)
- `Sonnblickweg 22, 4263 Elmberg, Österreich` (address)
- `FA Judenburg Liezen` (organisation)
- `Finanzamtes Österreich` (organisation)
- `93-757/0582` (tax_number)

**Example 85** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dora Grobstich  in der Beschwerdesache Raul Türkkan,  Schachener Straße 122J, 3643 Nonnersdorf, Österreich, über die Beschwerde vom 10. März 2021 gegen den Bescheid des Finanzamtes  Österreich vom 4. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 24-623/5745  zu Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Raul Türkkan` | `Raul Türkkan` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Dora Grobstich` (person)
- `Schachener Straße 122J, 3643 Nonnersdorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `24-623/5745` (tax_number)

**Example 86** (doc_id: `deanon_BFG_20260814_TEST/136699.1`) (sent_id: `deanon_BFG_20260814_TEST/136699.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Mag. Niels Rustemeier  in der Beschwerdesache Nicoletta Walch,  Polheimerweg 2, 3464 Schmida, Österreich, Steuernummer 65-653/8677, gegen die von der belangten Behörde  Finanzamt Österreich am 13. April 2018 ausgefertigten Bescheide betreffend Umsatzsteuer  und Einkommensteuer für die Jahre 2015, den am 19. April 2018 ausgefertigten Bescheid  betreffend Einkommensteuer 2016 und den am 9. April 2019 ausgefertigten Bescheid  betreffend Einkommensteuervorauszahlung für 2019 und Folgejahre beschlossen:  I. Die angefochtenen Bescheide werden gemäß § 278 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Nicoletta Walch` | `Nicoletta Walch` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mag. Niels Rustemeier` (person)
- `Polheimerweg 2, 3464 Schmida, Österreich` (address)
- `65-653/8677` (tax_number)
- `Finanzamt Österreich` (organisation)

**Example 87** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Adriana Eiffler, Waldhofweg 36a, 8321 Entschendorf, Österreich, betreffend Beschwerde vom 24. Februar 2021  gegen die Bescheide des Finanzamtes Österreich vom 9. Oktober 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 78-550/2209, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Adriana Eiffler` | `Adriana Eiffler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ansgar Unterberger` (person)
- `Waldhofweg 36a, 8321 Entschendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `78-550/2209` (tax_number)

**Example 88** (doc_id: `deanon_BFG_20260814_TEST/136735.1`) (sent_id: `deanon_BFG_20260814_TEST/136735.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Hartmut Schalk, Parhamerplatz 8, 9112 Gletschach, Österreich, betreffend Beschwerde vom 31. Juli 2012 gegen die Bescheide des  FA Salzburg-Stadt (nunmehr Finanzamt Österreich) vom 29. Juli 2011 betreffend  Einkommensteuer der Jahre 2006 bis 2010, Steuernummer 16-753/5618  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hartmut Schalk` | `Hartmut Schalk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Zwilling` (person)
- `Parhamerplatz 8, 9112 Gletschach, Österreich` (address)
- `FA Salzburg-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `16-753/5618` (tax_number)

**Example 89** (doc_id: `deanon_BFG_20260814_TEST/136975.1`) (sent_id: `deanon_BFG_20260814_TEST/136975.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Severin Iwanowsky  in der Beschwerdesache Richard Joistgen,  Breitenbachstraße 15, 4794 Glatzing, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 31. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 81-572/7905  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Richard Joistgen` | `Richard Joistgen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Severin Iwanowsky` (person)
- `Breitenbachstraße 15, 4794 Glatzing, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)
- `81-572/7905` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Gruenleitner Event` — type mismatch — same span as gold: `Gruenleitner Event`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dominika Oehlerich` — partial — pred is substring of gold: `Dominika Oehlerich, BEd`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Andrea Ebner`(person)
- `Dominika Oehlerich, BEd`(person)
- `Zamberg 9, 3843 Hohenau, Österreich`(address)
- `Finanzamtes Baden Mödling`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131013.1`) (sent_id: `deanon_BFG_20260814_TEST/131013.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Susanne Haim in der Beschwerdesache  Simone Zemanek, MSc, Almbachstraße 3, 8673 Filzmoos, Österreich, über die Beschwerde vom 2. April 2020 gegen den Bescheid des  Finanzamtes Braunau Ried Schärding vom 13. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 15-763/9594  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Simone Zemanek` — partial — pred is substring of gold: `Simone Zemanek, MSc`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Susanne Haim`(person)
- `Simone Zemanek, MSc`(person)
- `Almbachstraße 3, 8673 Filzmoos, Österreich`(address)
- `Finanzamtes Braunau Ried`(organisation)
- `15-763/9594`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinBE in der Beschwerdesache Charlotte Hirschmueller Silberhumerweg 2, 9163 Bodental, Österreich,  vertreten durch HR Danielle Schochert, Haßreidterstraße 75, 8831 Raiming, Österreich, über die Beschwerde vom  21. Dezember 2018 gegen die Bescheide des FA vom 28. September 2018 betreffend  Wiederaufnahme des Verfahren betreffend Einkommensteuer 2011 bis 2014,  Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014, Steuernummer  46-246/2967, zu Recht erkannt:   I. Die Beschwerden gegen die Bescheide betreffend Wiederaufnahme des Verfahren  betreffend Einkommensteuer 2011 bis 2014 sowie Anspruchszinsen 2011 bis 2014  werden als unbegründet abgewiesen.

**False Positives:**

- `Charlotte Hirschmueller Silberhumerweg` — partial — gold is substring of pred: `Charlotte Hirschmueller`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Charlotte Hirschmueller`(person)
- `Silberhumerweg 2, 9163 Bodental, Österreich`(address)
- `HR Danielle Schochert`(person)
- `Haßreidterstraße 75, 8831 Raiming, Österreich`(address)
- `46-246/2967`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `Eleonore Sawadzki` — partial — pred is substring of gold: `Eleonore Sawadzki, Bakk. art.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Eleonore Sawadzki, Bakk. art.`(person)
- `Weintraubengasse 36, 9073 Aich, Österreich`(address)
- `Finanzamtes Österreich`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/135477.1`) (sent_id: `deanon_BFG_20260814_TEST/135477.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Waltraud Pantermühl   in der Beschwerdesache der Kindsfater Telekom, Pirquethof 3, 8662 Lutschaun, Österreich, vertreten durch SIGNUM Treuhand  Steuerberatungs-GmbH, Rohrbach 25, 6850 Dornbirn,  betreffend den Bescheid des Finanzamt Graz-Stadt  vom 14. September 2021  hinsichtlich Zwangsstrafen 2021, Steuernummer 11-834/0873,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Kindsfater Telekom` — type mismatch — same span as gold: `Kindsfater Telekom`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Waltraud Pantermühl`(person)
- `Kindsfater Telekom`(organisation)
- `Pirquethof 3, 8662 Lutschaun, Österreich`(address)
- `SIGNUM Treuhand  Steuerberatungs-GmbH`(organisation)
- `Finanzamt Graz-Stadt`(organisation)
- `11-834/0873`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/136154.1`) (sent_id: `deanon_BFG_20260814_TEST/136154.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Rut Schattel  in der Beschwerdesache des  Stanley Wachenschwanz, Bakk. rer. nat. Bf1-Adr***RA über die Beschwerde vom 19. Oktober 2016 gegen die Bescheide  des Finanzamtes X vom 28. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für die Jahre 2012 und 2013 zu Recht erkannt:     I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Stanley Wachenschwanz` — partial — pred is substring of gold: `Stanley Wachenschwanz, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Rut Schattel`(person)
- `Stanley Wachenschwanz, Bakk. rer. nat.`(person)
- `Finanzamtes`(organisation)

</details>

---

## `Hon_Prof_in_Name` 🏆

**F1:** 0.091 | **Precision:** 0.796 | **Recall:** 0.048  

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
| 0.796 | 0.048 | 0.091 | 98 | 78 | 20 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 78 | 20 | 1536 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128706.1`) (sent_id: `deanon_BFG_20260814_TEST/128706.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter  Univ.-Prof. Günter Lehwaldt  in der Beschwerdesache   Waltraud Hinterlandt, Zefferergasse 6, 4923 Hochkuchl, Österreich, vertreten durch ECA Mag. Pichler & Partner Steuerberatung GmbH,  Stampfergasse 15, 5541 Altenmarkt im Pongau,  über die Beschwerde vom 11. Mai 2017 gegen  den Bescheid des Finanzamtes Gmunden Vöcklabruck  vom 19. April 2017 betreffend  Verspätungszuschlag von der Vorauszahlung an Umsatzsteuer für den Ze itraum 10-12/2016 zu  Recht:   I. Der Beschwerde wird gemäß § 279 BAO  teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Günter Lehwaldt` | `Univ.-Prof. Günter Lehwaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Waltraud Hinterlandt` (person)
- `Zefferergasse 6, 4923 Hochkuchl, Österreich` (address)
- `ECA Mag. Pichler & Partner Steuerberatung GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Ophelia Dutschka  in der Beschwerdesache A, Diepolding 3, 3754 Trabenreith, Österreich, vertreten durch Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft, Hallerschloßstraße 1, 8010 Graz, über die Beschwerde vom  26. Juli 2018 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und  Glücksspiel vom 29. Juni 2018 betreffend Grunderwerbsteuer 20.11.2016 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ophelia Dutschka` | `Hon.-Prof.in Ophelia Dutschka` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Diepolding 3, 3754 Trabenreith, Österreich` (address)
- `Rabel & Partner GmbH Wirtschaftsprüfungs und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Cassandra Witzenhause  in der Beschwerdesache Siegfried Basyurt,  Waldrasterweg 8, 9372 Rüggen, Österreich, über die Beschwerde vom 21.12.2010 gegen den Bescheid des Finanzamtes  Kitzbühel Lienz vom 9.11.2010, StrNr, betreffend die Festsetzung von 1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Cassandra Witzenhause` | `Univ.-Prof.in Cassandra Witzenhause` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Basyurt` (person)
- `Waldrasterweg 8, 9372 Rüggen, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129334.1`) (sent_id: `deanon_BFG_20260814_TEST/129334.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Sven Oberstelehn  in der Beschwerdesache Chantal Eligüzel,  Glittstein 70, 9072 Rupertiberg, Österreich, über die Beschwerde vom 20. September 2017 gegen den Bescheid des  Finanzamtes Gmunden Vöcklabruck vom 19. September 2017 betreffend Umsatzsteuer 2016  den Beschluss:  I. Der Vorlageantrag vom 6. Februar 2018 wird gemäß § 260 Abs 1 lit a BAO iVm § 264  Abs 4 lit e BAO als unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Sven Oberstelehn` | `Hon.-Prof. Sven Oberstelehn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chantal Eligüzel` (person)
- `Glittstein 70, 9072 Rupertiberg, Österreich` (address)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130076.1`) (sent_id: `deanon_BFG_20260814_TEST/130076.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Hon.-Prof. Linn Förstle, Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich, betreffend Beschwerde vom 18. Dezember 2014 gegen die Bescheide des Finanzamtes  Hollabrunn Korneuburg Tulln vom 22. Oktober 2014 betreffend Einkommensteuer für die Jahre  2008 bis 2010 beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO iVm. § 278 Abs. 1 lit. b BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Linn Förstle` | `Hon.-Prof. Linn Förstle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Karl-Eybl-Gasse 20, 9343 Brunn (Zweinitz), Österreich` (address)
- `Finanzamtes` (organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130083.1`) (sent_id: `deanon_BFG_20260814_TEST/130083.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130231.1`) (sent_id: `deanon_BFG_20260814_TEST/130231.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130334.1`) (sent_id: `deanon_BFG_20260814_TEST/130334.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Daisy Hoopt  über die Beschwerde des Prof.in StR DDr.in Reneé Plein,  Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich, vom 14. Mai 2020, gegen die Straferkenntnisse des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 5. Mai 2020, GZlen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Daisy Hoopt` | `Univ.-Prof.in Daisy Hoopt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in StR DDr.in Reneé Plein` (person)
- `Lehnrain 67, 4171 Sankt Peter am Wimberg, Österreich` (address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130824.1`) (sent_id: `deanon_BFG_20260814_TEST/130824.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130843.1`) (sent_id: `deanon_BFG_20260814_TEST/130843.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anastasia Schraders  in der Beschwerdesache, Svenja Nowakowsky,  Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich, Deutschland, vertreten durch KommR Serge Salameh, Engeltalsiedlung 39, 2093 Kottaun, Österreich, über die  Beschwerde vom 14. Mai 2020 gegen den Bescheid des Finanzamt Amstetten Melk Scheibbs  vom 11. März 2020  betreffend die Erstattung von Vorsteuern für den Zeitraum 01-12/2019 zu Steuernummer  59-077/4638  zu Recht erkannt:  I) Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anastasia Schraders` | `Univ.-Prof.in Anastasia Schraders` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Svenja Nowakowsky` (person)
- `Zehenthöf 24, 9433 Wölzing-St. Andrä, Österreich` (address)
- `KommR Serge Salameh` (person)
- `Engeltalsiedlung 39, 2093 Kottaun, Österreich` (address)
- `Finanzamt Amstetten Melk Scheibbs` (organisation)
- `59-077/4638` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Freilinger in der  Beschwerdesache Hon.-Prof. Clemens Mooß, Petzelhofstraße 29, 5122 Unterkriebach, Österreich, vertreten durch PROCURA Steuerberatung  GmbH, Zollergasse 2 Tür 38, 1070 Wien, über die Beschwerde vom 12. März 2015 gegen die  Bescheide des Finanzamtes Gmunden Vöcklabruck vom 12. Februar 2015 betreffend  Einkommensteuer 2011, 2012 und 2013, Steuernummer 62-757/0278, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Clemens Mooß` | `Hon.-Prof. Clemens Mooß` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Wolfgang Freilinger` (person)
- `Petzelhofstraße 29, 5122 Unterkriebach, Österreich` (address)
- `PROCURA Steuerberatung  GmbH` (organisation)
- `Finanzamtes Gmunden Vöcklabruck` (organisation)
- `62-757/0278` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/131929.1`) (sent_id: `deanon_BFG_20260814_TEST/131929.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Anneliese Wäsche  in der Beschwerdesache Gernot Kirchenmayer,  Richard-Wagner-Platz 15, 4153 Stierberg, Österreich, vertreten durch Eckert Fries Carter Rechtsanwälte GmbH, Erzherzog Rainer- Ring 23, 2500 Baden, über die Beschwerde vom 24. Jänner 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 19. Dezember 2018  betreffend Verspätungszuschlag / Sonstige 2018 Steuernummer zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anneliese Wäsche` | `Univ.-Prof.in Anneliese Wäsche` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gernot Kirchenmayer` (person)
- `Richard-Wagner-Platz 15, 4153 Stierberg, Österreich` (address)
- `Eckert Fries Carter Rechtsanwälte GmbH` (organisation)
- `Finanzamtes für Gebühren` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/132140.1`) (sent_id: `deanon_BFG_20260814_TEST/132140.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/132505.1`) (sent_id: `deanon_BFG_20260814_TEST/132505.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/132916.1`) (sent_id: `deanon_BFG_20260814_TEST/132916.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Merlin Morkam  in der Beschwerdesache des  KzlR Jens Koudela, BSc, Veitschersiedlung 40, 4048 Puchenau, Österreich, über die Beschwerde vom 2. Mai 2018 gegen den Bescheid des  Finanzamt Salzburg-Stadt  vom 18. April 2018 betreffend Einkommensteuer 2016 zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Merlin Morkam` | `Hon.-Prof.in Merlin Morkam` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KzlR Jens Koudela, BSc` (person)
- `Veitschersiedlung 40, 4048 Puchenau, Österreich` (address)
- `Finanzamt Salzburg-Stadt` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/133041.1`) (sent_id: `deanon_BFG_20260814_TEST/133041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Adam Rueßbült  in den Beschwerdesachen des  Timon Reinhertz, Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich, über die Beschwerden vom 7. März 2019 gegen die Bescheide des  Finanzamtes Graz-Stadt (nunmehr Finanzamt Österreich) vom 4. März 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) für die Jahre 2014 und 2015, Steuernummer  15-325/9824, zu Recht erkannt:  Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Adam Rueßbült` | `Hon.-Prof. Adam Rueßbült` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Timon Reinhertz` (person)
- `Josef-Pöschl-Weg 3, 9701 Schwarzenbach, Österreich` (address)
- `Finanzamtes Graz-Stadt` (organisation)
- `Finanzamt Österreich` (organisation)
- `15-325/9824` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/134287.1`) (sent_id: `deanon_BFG_20260814_TEST/134287.1_1`)


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

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/135021.1`) (sent_id: `deanon_BFG_20260814_TEST/135021.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Edwin Teiwes  in der Beschwerdesache MedR Francois Distefano,  Franz Pichler-Straße 97, 4720 Güttling, Österreich, vertreten durch Huber & Huber, Rechtsanwälte, Heinrich Gruber-Straße 1,  4050 Traun, über die Beschwerde vom 14. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 19. November 2020 betreffend Einkommensteuer 2019  Steuernummer 83-092/9347  zu Recht erkannt:   I.  Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Edwin Teiwes` | `Univ.-Prof. Edwin Teiwes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Francois Distefano` (person)
- `Franz Pichler-Straße 97, 4720 Güttling, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `83-092/9347` (tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Andreas Kuschy  in der Beschwerdesache Angelika Oligschleger,  Friedhofgasse, Rattersdorf 3, 9971 Tauer, Österreich, betreffend Beschwerde vom 8. April 2021 gegen den Bescheid des Finanzamt Innsbruck  vom 29. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020,  Steuernummer 49-970/7545  nach dem Einlangen des Vorlageantrages vom 10.6.2021  beschlossen:   Der Vorlageantrag wird gem. § 264 Abs 4 lit e Bundesabgabenordnung zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Andreas Kuschy` | `Univ.-Prof. Andreas Kuschy` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Angelika Oligschleger` (person)
- `Friedhofgasse, Rattersdorf 3, 9971 Tauer, Österreich` (address)
- `Finanzamt Innsbruck` (organisation)
- `49-970/7545` (tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Verwaltungsstrafsache (§ 4 Abs. 1  Parkometergesetz 2006) hinsichtlich Hon.-Prof. Reinhard Bodewein, Klein Greinsfurth 49, 9063 Kading, Österreich, über dessen Anbringen vom  15. September 2021 in Zusammenhang mit   Strafverfügung des Magistrates der Stadt Wien, MA 67, vom 16.03.2021,   Vollstreckungsverfügung des Magistrates der Stadt Wien, MA 6 – BA 32, vom  13.09.2021,  jeweils zu GZ. MA67/Zahl1/2020, gemäß § 5 des Gesetzes über die Organisation der  Abgabenverwaltung und besondere abgabenrechtliche Bestimmungen in Wien (WAOR) sowie  § 24 Abs. 1 Satz 2 Bundesfinanzgerichtsgesetz (BFGG) in Verbindung mit (iVm) § 31 Abs. 1  Verwaltungsgerichtsverfahrensgesetz (VwGVG) den Beschluss gefasst:  I.) Beim Anbringen vom 15. September 2021 handelt es sich um keine Beschwerde im Sinne  des Art. 130 Abs. 1 Z 1 Bundes-Verfassungsgesetz (B-VG).

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Reinhard Bodewein` | `Hon.-Prof. Reinhard Bodewein` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Klein Greinsfurth 49, 9063 Kading, Österreich` (address)
- `Magistrates der Stadt Wien` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_26`)


Am 12. Oktober 2021 nahm der Magistrat der Stadt Wien folgenden  Aktenvermerk zum Akt: „Laut Telefonat … mit Herrn Hon.-Prof. Reinhard Bodewein  sind seine Schreiben anlässlich  den Erhalt der Vollstreckungsverfügung als Beschwerde zu sehen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Reinhard Bodewein` | `Hon.-Prof. Reinhard Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_43`)


Im Februar seien die Schmerzen dann unerträglich geworden, weshalb sie das KUK aufgesucht  hätte und auch bei Univ.-Prof.in Milena Büttinghausen [Anmerkung Richter: Ärztin für Allgemeinmedizin] in Behandlung  gewesen sei.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Milena Büttinghausen` | `Univ.-Prof.in Milena Büttinghausen` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/135960.1`) (sent_id: `deanon_BFG_20260814_TEST/135960.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Franziskus Grineisen  in der Beschwerdesache MedR KommR Serena Dillschneider,  Rooseveltplatz 7, 4770 Bruck, Österreich, über die Beschwerde vom 28. Dezember 2020 gegen die Bescheide des  Finanzamt Klosterneuburg  vom 25. November 2020 betreffend Einkommensteuer 2017 und Wiederaufnahme  des Verfahrens bezüglich der Einkommensteuer 2017 und den Bescheid vom 02. August 2021  betreffend die Wiederaufnahme des Verfahrens bezüglich der Einkommensteuer 2018,  Steuernummer 95-890/2122, zu Recht erkannt:   I. Die Beschwerde gegen die Wiederaufnahmebescheide wird gemäß § 279 BAO als  unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Franziskus Grineisen` | `Hon.-Prof. Franziskus Grineisen` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR KommR Serena Dillschneider` (person)
- `Rooseveltplatz 7, 4770 Bruck, Österreich` (address)
- `Finanzamt Klosterneuburg` (organisation)
- `95-890/2122` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/136119.1`) (sent_id: `deanon_BFG_20260814_TEST/136119.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Wolenski  in der Beschwerdesache Siegfried Beyazit,  Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich  über die Beschwerde vom 14. Mai 2016 gegen den Bescheid des Finanzamtes  Waldviertel vom 18. März 2016 betreffend Einheitswert des land- u. forstwirtschaftl.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Jacqueline Wolenski` | `Univ.-Prof.in Jacqueline Wolenski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegfried Beyazit` (person)
- `Heinrich-Waggerl-Straße 19, 3200 Rennersdorf, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/136364.1`) (sent_id: `deanon_BFG_20260814_TEST/136364.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Patrick Hübben  in der Beschwerdesache Alice Rüde,  Auhub 26, 9560 Kraß, Österreich, vertreten durch BDO Steiermark GmbH Wtp u Stb, Schubertstraße 62, 8010  Graz, über die Beschwerde vom 18. März 2019 gegen den Bescheid des FA Tirol Ost  vom  26. Februar 2019 betreffend Abweisung eines Zahlungserleichterungsansuchens zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Patrick Hübben` | `Hon.-Prof. Patrick Hübben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Alice Rüde` (person)
- `Auhub 26, 9560 Kraß, Österreich` (address)
- `BDO Steiermark GmbH Wtp` (organisation)
- `FA Tirol Ost` (organisation)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Nadine Hupmann  in der Beschwerdesache Joachim Kotmann,  Weinbach 15, 8454 Saggau, Österreich, über die Beschwerde vom 10. Jänner 2020 gegen den Bescheid des  Finanzamtes Innsbruck (nunmehr: FA Österreich) vom 13. Dezember 2019, SV-Nr, betreffend  die Rückforderung zu Unrecht bezogener Beträge an Familienbeihilfe und Kinderabsetzbetrag  für den Zeitraum Juli 2018 bis Februar 2019 zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Nadine Hupmann` | `Hon.-Prof.in Nadine Hupmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Joachim Kotmann` (person)
- `Weinbach 15, 8454 Saggau, Österreich` (address)
- `Finanzamtes Innsbruck` (organisation)
- `FA Österreich` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/136479.1`) (sent_id: `deanon_BFG_20260814_TEST/136479.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Marion Schlesing  in der Beschwerdesache des  Dimitri Seewaldt, Sonnblickweg 22, 4263 Elmberg, Österreich, über die Beschwerde vom 15. November 2018 gegen den Bescheid  des FA Judenburg Liezen (jetzt Dienststelle des Finanzamtes Österreich) vom 16. Oktober 2018 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 zur Steuernummer 93-757/0582  zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Marion Schlesing` | `Hon.-Prof.in Marion Schlesing` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Dimitri Seewaldt` (person)
- `Sonnblickweg 22, 4263 Elmberg, Österreich` (address)
- `FA Judenburg Liezen` (organisation)
- `Finanzamtes Österreich` (organisation)
- `93-757/0582` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/137635.1`) (sent_id: `deanon_BFG_20260814_TEST/137635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Valerius Frühmark  in der Beschwerdesache Hon.-Prof. Sven Corbin,  Stalderhaus 7, 9363 Feistritz, Österreich, über die Beschwerde vom 23. Juli 2021 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juli 2021 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum Juni 2018 bis Jänner 2019, SVNr [SVNR],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Sven Corbin` | `Hon.-Prof. Sven Corbin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Valerius Frühmark` (person)
- `Stalderhaus 7, 9363 Feistritz, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Frank Ruhleder  in der Beschwerdesache Dr. Luigi Mainholz  vertreten durch STB, über die mit Beschwerden angefochtenen Bescheide des FA Wien 1/23,  Steuernummer 61-747/1918, betreffend Einkommensteuer 2005, 2006, 2008, 2009, 2010  und 2011 zu Recht erkannt:    Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Frank Ruhleder` | `Hon.-Prof. Frank Ruhleder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Luigi Mainholz` (person)
- `FA Wien 1/23` (organisation)
- `61-747/1918` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138259.1`) (sent_id: `deanon_BFG_20260814_TEST/138259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Otto Pavlikova  in der Angelegenheit der Parteien  Oskar Wood (Beschwerdeführer) und Finanzamt Österreich als Amtspartei und als  Gesamtrechtsnachfolger des FA Niederösterreich Mitte  über die Beschwerde vom  22.6.2020 gegen den Bescheid des FA Niederösterreich Mitte  vom 22.5.2020  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019         zu Recht erkannt:  Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Otto Pavlikova` | `Univ.-Prof. Otto Pavlikova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Oskar Wood` (person)
- `Finanzamt Österreich` (organisation)
- `FA Niederösterreich Mitte` (organisation)
- `FA Niederösterreich Mitte` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/138437.1`) (sent_id: `deanon_BFG_20260814_TEST/138437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Bettina Füsslin  in der Beschwerdesache Univ.-Prof.in Anastasia Sebott,  Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich, vertreten durch Mag. jur.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Anastasia Sebott` | `Univ.-Prof.in Anastasia Sebott` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Bettina Füsslin` (person)
- `Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich` (address)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/138674.1`) (sent_id: `deanon_BFG_20260814_TEST/138674.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Kai Steinacker  in der Säumnisbeschwerdesache  Univ.-Prof. Achmed Singendonk, IZ NÖ-Süd Straße 2 a 4, 3214 Buchberg, Österreich, über die Beschwerde vom 12.11.2022, beim Bundesfinanzgericht  am 24.11.2022 eingelangt, wegen Verletzung der Entscheidungspflicht des Finanzamtes  Österreich betreffend    Erlassung einer Beschwerdevorentscheidung hinsichtlich Einkommensteuer 2021 sowie   Bescheidabänderung gemäß § 295a BAO hinsichtlich Einkommensteuer 2020   beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs 7 lit b BAO iVm § 260 Abs 1 lit a BAO als  unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Achmed Singendonk` | `Univ.-Prof. Achmed Singendonk` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Kai Steinacker` (person)
- `IZ NÖ-Süd Straße 2 a 4, 3214 Buchberg, Österreich` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamtes  Österreich` (organisation)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/138977.1`) (sent_id: `deanon_BFG_20260814_TEST/138977.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Yelec Tummascheit  in der Beschwerdesache Gerda Staigl,  Im Schwalbengrund 7y, 5583 Hintermuhr, Österreich, über die Beschwerde vom 11.08.2022 gegen den Bescheid des Finanzamtes  Österreich vom 05.08.2022, Steuernummer 64-583/4801, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021, zu Recht erkannt:  I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Yelec Tummascheit` | `Univ.-Prof. Yelec Tummascheit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gerda Staigl` (person)
- `Im Schwalbengrund 7y, 5583 Hintermuhr, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `64-583/4801` (tax_number)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/139126.1`) (sent_id: `deanon_BFG_20260814_TEST/139126.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Jan Jürn  in der Beschwerdesache Armin Klews, Bakk. art.,  Lesach 119, 3071 Untergrafendorf, Österreich, über die Beschwerde vom 28. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 20. April 2022 betreffend Abweisung des Antrages auf Gewährung von  Familienbeihilfe ab Februar 2022 zur Steuernummer 51-609/6898  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Jan Jürn` | `Hon.-Prof. Jan Jürn` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Armin Klews, Bakk. art.` (person)
- `Lesach 119, 3071 Untergrafendorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `51-609/6898` (tax_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/139406.1`) (sent_id: `deanon_BFG_20260814_TEST/139406.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Günter Möhlenfeld  in Vertretung des verhinderten  Richters Hon.-Prof. Kaspar Frantzius  in der Verwaltungsstrafsache gegen Elias Schwabeland, Josef-Schlegel-Straße 64, 3571 Thunau am Kamp, Österreich, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung iVm § 4 Abs. 1  Wiener Parkometergesetz 2006, über die Beschwerde des Beschuldigten vom 22. November  2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 67 vom  15. November 2021, GZ. MA67/Zahl/2021, nach Durchführung einer mündlichen Verhandlung  am 19. Dezember 2022, in Anwesenheit des Beschuldigten und der Schriftführerin IP, jedoch in  entschuldigter Abwesenheit einer Vertreterin/eines Vertreters der belangten Behörde, zu  Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisations- recht (WAOR) wird der Beschwerde stattgegeben, das angefochtene Straferkenntnis  aufgehoben und das Verfahren eingestellt.  Gemäß § 52 Abs. 8 VwGVG hat die beschwerdeführende Partei keinen Beitrag zu den Kosten  des Beschwerdeverfahrens zu entrichten.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Günter Möhlenfeld` | `Hon.-Prof. Günter Möhlenfeld` |
| `Hon.-Prof. Kaspar Frantzius` | `Hon.-Prof. Kaspar Frantzius` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Elias Schwabeland` (person)
- `Josef-Schlegel-Straße 64, 3571 Thunau am Kamp, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/139428.1`) (sent_id: `deanon_BFG_20260814_TEST/139428.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Brendon Spade  in der Beschwerdesache OMedR Milena Piechulik,  Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich  vertreten durch Walther Kendler, Zehenthofgasse 10/2/10, 1190 Wien, und  Arnold Rechtsanwälte GmbH, Wipplingerstraße 10, 1010 Wien, über die Beschwerden der  Abgabepflichtigen vom 28. April 2017 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2. Februar 2017, betreffend Einkommensteuer 2014, und vom 13.4.2018  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 7. Februar 2018,  betreffend Einkommensteuer 2015, alle Steuernummer 16-827/1246  beschlossen:  Die Beschwerden werden gemäß § 261 Abs. 1 lit. a BAO iVm § 278 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Brendon Spade` | `Univ.-Prof. Brendon Spade` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OMedR Milena Piechulik` (person)
- `Seidledtstraße 246, 2822 Schwarzau am Steinfeld, Österreich` (address)
- `Walther Kendler` (person)
- `Finanzamtes Wien 9/18/19  Klosterneuburg` (organisation)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `16-827/1246` (tax_number)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/139790.1`) (sent_id: `deanon_BFG_20260814_TEST/139790.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Alva Volgenandt  in der Beschwerdesache Pawel Smock,  Kongreßbad 9, 6811 Göfis, Österreich, vertreten durch Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH, Geusaugasse 39 Tür 8, 1030 Wien, 1.) über die Beschwerde vom 28.02.2014 gegen den  Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 27.01.2014 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2.) über die Beschwerde vom  28.07.2014 gegen den Bescheid des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom  30.06.2014 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2012, Steuernummer  20-852/2672, nach der am 19.10.2022 durchgeführten mündlichen Verhandlung zu Recht  erkannt:     I. Die Beschwerden werden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Alva Volgenandt` | `Hon.-Prof.in Alva Volgenandt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Pawel Smock` (person)
- `Kongreßbad 9, 6811 Göfis, Österreich` (address)
- `Rogy und Rogy Wirtschaftsprüfungs- und Steuerberatungs  GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `20-852/2672` (tax_number)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/139879.1`) (sent_id: `deanon_BFG_20260814_TEST/139879.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Wilfried Giacomello  in der Beschwerdesache Natascha Theys vertreten  durch StB über die Beschwerde vom 3. Oktober 2022 gegen den Bescheid des FA Linz  vom  9. September 2022 über die Festsetzung eines ersten Säumniszuschlages (Steuernummer  86-989/6915 ) zu Recht erkannt:     I. Die Beschwerde wird gemäß § 279 Bundesabgabeordnung (BAO) als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Wilfried Giacomello` | `Univ.-Prof. Wilfried Giacomello` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Natascha Theys` (person)
- `FA Linz` (organisation)
- `86-989/6915` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/140242.1`) (sent_id: `deanon_BFG_20260814_TEST/140242.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch die Richterin Mag. Mirha Karahodzic MA in der  Beschwerdesache Hon.-Prof. Justin Jacobeit, Gasthaus Kugelwiese 12, 3841 Markl, Österreich, vertreten durch Schmitt & Schmitt  Wirtschaftstreuhand- gesellschaft m.b.H., Strohgasse 25, 1030 Wien, über die Beschwerde vom  11. Mai 2022 gegen den Bescheid des Finanzamtes Österreich vom 28. April 2022,  Steuernummer 67-100/8891, betreffend Einkommensteuer 2019 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Justin Jacobeit` | `Hon.-Prof. Justin Jacobeit` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Mirha Karahodzic MA` (person)
- `Gasthaus Kugelwiese 12, 3841 Markl, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `67-100/8891` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/140311.1`) (sent_id: `deanon_BFG_20260814_TEST/140311.1_2`)


Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Reinhard Milschlag  in der Beschwerdesache Melanie Guidi,  Scheatlers Wies 27, 3633 Dorfstadt, Österreich, über die Beschwerde vom 12. Juni 2019 gegen den Bescheid des Finanzamtes  Wien 4/5/10 vom 5. Juni 2019 betreffend die Bewilligung einer Zahlungserleichterung zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Reinhard Milschlag` | `Univ.-Prof. Reinhard Milschlag` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melanie Guidi` (person)
- `Scheatlers Wies 27, 3633 Dorfstadt, Österreich` (address)
- `Finanzamtes  Wien 4/5/10` (organisation)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/140320.1`) (sent_id: `deanon_BFG_20260814_TEST/140320.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Jonathan Eisbrenner  in der Beschwerdesache Marion Voskuil,  Taschlgrabenrotte 9, 4190 Ortschlag, Österreich, betreffend die Beschwerde vom 30. November 2022 gegen den Bescheid des  Finanzamt Innsbruck  vom 20. Oktober 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2021, Steuernummer 86-965/4065, beschlossen:  Die Beschwerde wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Jonathan Eisbrenner` | `Hon.-Prof. Jonathan Eisbrenner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Marion Voskuil` (person)
- `Taschlgrabenrotte 9, 4190 Ortschlag, Österreich` (address)
- `Finanzamt Innsbruck` (organisation)
- `86-965/4065` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/141066.1`) (sent_id: `deanon_BFG_20260814_TEST/141066.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Hon.-Prof. Dragan Neisemeyer  über die Beschwerde der Haendl Wind GmbH, Parseier 13, 4421 Pieslwang, Österreich, vertreten durch die Puntigam Wirtschaftstreuhand und  Steuerberatung GmbH, Hauptstraße 39, 8093 St. Peter am Ottersbach, vom 29.09.2020 gegen  den Bescheid des Finanzamtes Graz-Umgebung vom 11.03.2020 betreffend Umsatzsteuer 2017  zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Dragan Neisemeyer` | `Hon.-Prof. Dragan Neisemeyer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Haendl Wind GmbH` (organisation)
- `Parseier 13, 4421 Pieslwang, Österreich` (address)
- `Puntigam Wirtschaftstreuhand und  Steuerberatung GmbH` (organisation)
- `Finanzamtes Graz` (organisation)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_1`)


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

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/141438.1`) (sent_id: `deanon_BFG_20260814_TEST/141438.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Dr. Lisa Pucher in der Beschwerdesache  Hon.-Prof.in Chantal Antepoth, Gebharts 4, 4101 Pesenbach, Österreich, über die Beschwerden vom 3. November 2019 gegen die Bescheide  des Finanzamtes Wien 2/20/21/22 (nun Finanzamt Österreich) vom 17. Oktober 2019  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis 2018, zu Steuernummer  57-731/4309, den Beschluss:  I. Die Beschwerden betreffend Einkommensteuer 2014, 2016, 2017 und 2018 werden gemäß  § 261 Abs 1 lit a BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Chantal Antepoth` | `Hon.-Prof.in Chantal Antepoth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Lisa Pucher` (person)
- `Gebharts 4, 4101 Pesenbach, Österreich` (address)
- `Finanzamtes Wien 2/20/21/22` (organisation)
- `Finanzamt Österreich` (organisation)
- `57-731/4309` (tax_number)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/141747.1`) (sent_id: `deanon_BFG_20260814_TEST/141747.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Roberta Sellerer  in der   Beschwerdesache Univ.-Prof.in Susette Teebken, Günther Benedikt-Straße 26, 8052 Graz, Österreich, vertreten durch Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020  Innsbruck, über die Beschwerde vom 29. Mai 2017 gegen die Bescheide des Finanzamtes für  Gebühren, Verkehrsteuern und Glücksspiel, nunmehr Finanzamt Österreich- Sonderzuständigkeiten, vom 3. Mai 2017,   ErfNr, betreffend 1. Aufhebung gemäß § 299 Abs. 1 BAO und 2. Festsetzung der  Grunderwerbsteuer, im fortgesetzten Verfahren zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid vom 3.5.2017 betreffend Aufhebung des      Grunderwerbsteuerbescheides vom 24.2.2017 gemäß § 299 Abs. 1 BAO wird als      unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Susette Teebken` | `Univ.-Prof.in Susette Teebken` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Roberta Sellerer` (person)
- `Günther Benedikt-Straße 26, 8052 Graz, Österreich` (address)
- `Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes für  Gebühren` (organisation)
- `Finanzamt` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/141747.1`) (sent_id: `deanon_BFG_20260814_TEST/141747.1_7`)


Mit Baurechtsvertrag vom 19.10.2016 hat die Marktgemeinde Ort1 als Baurechtsbestellerin  an den ihr gehörigen Gst1 und Gst2 in EZ1, bebautes Grundstück mit einer Gesamtfläche von  1.094 m², an die Univ.-Prof.in Susette Teebken (= Beschwerdeführerin, Bf) ein Baurecht auf die Dauer von 50  Jahren eingeräumt (Punkte III. und IV.).

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Susette Teebken` | `Univ.-Prof.in Susette Teebken` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/142581.1`) (sent_id: `deanon_BFG_20260814_TEST/142581.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Regina Mockry  in der Beschwerdesache Gablonsky&Rethlefsen Gastronomie AG&  atypisch stille Gesellschaft, vertreten durch xx GmbH Steuerberatung und Wirtschaftsprüfung,  Straße1, Ort1, über die Beschwerden der atypisch stillen Gesellschafter  1.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Regina Mockry` | `Univ.-Prof.in Regina Mockry` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Gablonsky&Rethlefsen Gastronomie AG` (organisation)
- `xx GmbH Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Wilhelmine Strigl  in der Beschwerdesache Dominik Barfusz,  Alexander-Dubček-Gasse 23, 6644 Elmen, Österreich, über die Beschwerde vom 20. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 18. März 2023, Ordnungsbegriff Nr1, betreffend Abweisung des Antrages auf  "Zuerkennung der Familienbeihilfe für den Zeitraum ab Februar 2023" zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Wilhelmine Strigl` | `Hon.-Prof.in Wilhelmine Strigl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dominik Barfusz` (person)
- `Alexander-Dubček-Gasse 23, 6644 Elmen, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/142808.1`) (sent_id: `deanon_BFG_20260814_TEST/142808.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Rupert Wedell  in der Beschwerdesache OStR OMedR Rebecca Ehrmanntraut,  Museumplatz 27, 8241 Rohrbachschlag, Österreich, über die Beschwerden vom 10. Oktober 2017 gegen die Bescheide des  FA Baden Mödling  vom 27. Juni 2017 bzw. 10. Juli 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2012 bis 2015, Steuernummer 38-848/8801, zu Recht erkannt:  I. Den Beschwerden gegen die Bescheide betreffend Einkommensteuer für die Jahre 2012 bis  2015 wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Rupert Wedell` | `Hon.-Prof. Rupert Wedell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `OStR OMedR Rebecca Ehrmanntraut` (person)
- `Museumplatz 27, 8241 Rohrbachschlag, Österreich` (address)
- `FA Baden Mödling` (organisation)
- `38-848/8801` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/143172.1`) (sent_id: `deanon_BFG_20260814_TEST/143172.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Shirley Vostrovsky  in der Beschwerdesache RgR Tanja Tihl, BSc,  Kleindorf I 13, 4661 Deising, Österreich, über die Beschwerde vom 25. April 2023 gegen den Bescheid des Finanzamtes  Österreich vom 24. April 2023, Steuernummer 58-854/9841, betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Shirley Vostrovsky` | `Univ.-Prof.in Shirley Vostrovsky` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `RgR Tanja Tihl, BSc` (person)
- `Kleindorf I 13, 4661 Deising, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `58-854/9841` (tax_number)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/143588.1`) (sent_id: `deanon_BFG_20260814_TEST/143588.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Wilfried Chaudhuri  in der Beschwerdesache des  Thorsten Rödamer, St. Marienweg 37, 9081 Reifnitz, Österreich, über die Beschwerde vom 19. Jänner 2022 gegen den Bescheid des  Finanzamtes Österreich vom 21. Dezember 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 65-515/6745, zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Wilfried Chaudhuri` | `Univ.-Prof. Wilfried Chaudhuri` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Thorsten Rödamer` (person)
- `St. Marienweg 37, 9081 Reifnitz, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `65-515/6745` (tax_number)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/143803.1`) (sent_id: `deanon_BFG_20260814_TEST/143803.1_1`)


BESCHLUSS AUFSCHIEBE NDE WIRKUNG   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Dagobert Rönnecke  in der Revisionssache PhD ÖkR Peter Stankeit,  Im Alauntal 10, 3243 Eselsteiggraben, Österreich  vertreten durch Aigner Rechtsanwalts-GmbH, Lugeck 1-2/Stiege 2/Top 12, 1010  Wien, über den Antrag des Revisionswerbers vom 2.Februar 2024, der gegen das Erkenntnis  des Bundesfinanzgerichtes vom 12.Dezember 2023, RV/5100686/2021, betreffend  Einkommensteuer 2019 und die Aufhebung des Einkommenssteuerbescheides 2019  erhobenen außerordentlichen Revision die aufschiebende Wirkung zuzuerkennen,  beschlossen:   Gemäß § 30 Abs. 2 VwGG wird dem Antrag nicht stattgegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Dagobert Rönnecke` | `Univ.-Prof. Dagobert Rönnecke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `PhD ÖkR Peter Stankeit` (person)
- `Im Alauntal 10, 3243 Eselsteiggraben, Österreich` (address)
- `Aigner Rechtsanwalts-GmbH` (organisation)
- `Bundesfinanzgerichtes` (organisation)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch Prof. Yorick Frühbis, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Ariadne Iwanowsky` | `Hon.-Prof.in Ariadne Iwanowsky` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Hon.-Prof. Denis Hoffjan` (person)
- `Camesinaweg 86, 4652 Taxlberg, Österreich` (address)
- `Prof. Yorick Frühbis` (person)
- `Finanzamt Österreich` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/144133.1`) (sent_id: `deanon_BFG_20260814_TEST/144133.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Farina Solovieva  in der Beschwerdesache der  Folmer Sanitär, Josefs-Brunnen Gasse 27, 8505 Unterjahring, Österreich, über die Beschwerde vom 27. Oktober 2022 gegen den Bescheid  des FA Bruck Eisenstadt Oberwart  vom 14. Oktober 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2021 zu Steuernummer 06-556/2153  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Farina Solovieva` | `Univ.-Prof.in Farina Solovieva` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Folmer Sanitär` (organisation)
- `Josefs-Brunnen Gasse 27, 8505 Unterjahring, Österreich` (address)
- `FA Bruck Eisenstadt Oberwart` (organisation)
- `06-556/2153` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thassilo Osipenko  in der Beschwerdesache des  Agatha Stingele, Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich, vertreten durch Mag. Hedwig Maria Weber, Ausseer Straße 32,  8940 Liezen, über die Beschwerden vom 5. August 2020 gegen die Bescheide des Finanzamtes  Österreich vom 7. Juli 2020 betreffend Festsetzung der Normverbrauchsabgabe (NoVA- Vergütung gemäß § 12a NoVAG) für   1) den Zeitraum 4 – 12/2019 und   2) den Zeitraum 1/2020,   Steuernummer 39-913/2428, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Thassilo Osipenko` | `Univ.-Prof. Thassilo Osipenko` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Agatha Stingele` (person)
- `Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich` (address)
- `Mag. Hedwig Maria Weber` (person)
- `Finanzamtes  Österreich` (organisation)
- `39-913/2428` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/145232.1`) (sent_id: `deanon_BFG_20260814_TEST/145232.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Jacqueline Traxl  in der Beschwerdesache des  Gebhard Hannig, Nußdorfer Markt 4, 4776 Antersham, Österreich, vertreten durch Mag. Paulus Maria Christoph Papst,  Bergmanngasse 15 Tür 2, 8010 Graz, über die Beschwerde vom 1. März 2023 gegen den zur  Steuernummer 97-347/7690  ergangenen Bescheid des FA Braunau Ried Schärding  vom 3. Februar 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021 zu Recht erkannt:   I. Die Beschwerde vom 1.März 2023 gegen den Einkommensteuerbescheid 2021 vom  3.Februar 2023 wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Jacqueline Traxl` | `Hon.-Prof.in Jacqueline Traxl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Gebhard Hannig` (person)
- `Nußdorfer Markt 4, 4776 Antersham, Österreich` (address)
- `Mag. Paulus Maria Christoph Papst` (person)
- `97-347/7690` (tax_number)
- `FA Braunau Ried Schärding` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/145808.1`) (sent_id: `deanon_BFG_20260814_TEST/145808.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Silvia Aust   in der Beschwerdesache des Li Süssle, Zierreit 3, 9113 Lippitzbach, Österreich, betreffend den Bescheid des  FA Wien 1/23  vom 21. April 2020   hinsichtlich Einkommensteuervorauszahlungen 2020, Steuernummer 97-936/9955,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a BAO als nicht  fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Silvia Aust` | `Univ.-Prof.in Silvia Aust` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Li Süssle` (person)
- `Zierreit 3, 9113 Lippitzbach, Österreich` (address)
- `FA Wien 1/23` (organisation)
- `97-936/9955` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/146223.1`) (sent_id: `deanon_BFG_20260814_TEST/146223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Arabella Ungeruh  in der Beschwerdesache des  Melina Kirstaedter, Olbersdorf 35, 6092 Birgitz, Österreich, über die Beschwerde vom 26. April 2024 gegen den Bescheid des  Finanzamt Braunau Ried Schärding  vom 25. April 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023  zu Steuernummer 03-867/9768  zu Recht erkannt:   I. Die Beschwerde wird gemäß als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Arabella Ungeruh` | `Univ.-Prof.in Arabella Ungeruh` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Melina Kirstaedter` (person)
- `Olbersdorf 35, 6092 Birgitz, Österreich` (address)
- `Finanzamt Braunau Ried Schärding` (organisation)
- `03-867/9768` (tax_number)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/146548.1`) (sent_id: `deanon_BFG_20260814_TEST/146548.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hagen Atar  in der Beschwerdesache Priv.-Doz.in Laura Fromader,  Oberpetersdorf 6, 4871 Egg, Österreich, über die Beschwerde vom 13. Dezember 2022 gegen den Bescheid des  FA Wien 2/20/21/22  vom 6. Dezember 2022 betreffend den Bescheid über die Abweisung des Antrags auf  Aufhebung des Einkommensteuerbescheides 2020 gem § 299 BAO zur Steuernummer  60-848/5470  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Hagen Atar` | `Hon.-Prof. Hagen Atar` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Laura Fromader` (person)
- `Oberpetersdorf 6, 4871 Egg, Österreich` (address)
- `FA Wien 2/20/21/22` (organisation)
- `60-848/5470` (tax_number)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  der Univ.-Prof. Julian Czernitzki, Faßlergasse 78L-80, 9612 Dellach, Österreich, vertreten durch Schneider Wirtschaftsprüfung und  Steuerberatung GmbH, 6845 Hohenems, Nibelungenstraße 19, über die Beschwerde vom  19.04.2019 gegen die Körperschaftsteuerbescheide 2014, 2015, 2016, gegen die  Umsatzsteuerbescheide 2014, 2015, 2016 (alle Bescheide vom 25.03.2019), gegen die  Bescheide über die Festsetzung von Umsatzsteuer für 12/2017 und 12/2018 vom jeweils  25.03.2019 (Umsatzsteuerbescheid 2017 vom 22.05.2020 und Umsatzsteuerbescheid 2018  vom 17.10.2023), sowie gegen die Haftungsbescheide Kapitalertragsteuer 01/2014, 12/2014,  12/2015, 12/2016 und 12/2017 (Bescheide jeweils vom 21.03.2019), zu Recht erkannt:  I. Der Beschwerde gegen die Körperschaftsteuerbescheide 2015 und 2016, die  Umsatzsteuerbescheide 2015, 2016, 2017 und 2018 wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Julian Czernitzki` | `Univ.-Prof. Julian Czernitzki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Ungericht` (person)
- `Faßlergasse 78L-80, 9612 Dellach, Österreich` (address)
- `Schneider Wirtschaftsprüfung und  Steuerberatung GmbH` (organisation)

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_13`)


Im Betriebsprüfungsbericht wurden folgende Feststellungen getroffen (Bericht gem. § 150 BAO  über das Ergebnis der Außenprüfung vom 27.03.2019):  „Tz. 1 "Verrechnungskonto" P.  G. ist alleiniger Gesellschafter sowie Geschäftsführer der Univ.-Prof. Julian Czernitzki, sein Vater P. deren  Prokurist.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Julian Czernitzki` | `Univ.-Prof. Julian Czernitzki` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_154`)


Die Bf. ist die Univ.-Prof. Julian Czernitzki  mit dem Sitz in der politischen Gem.A,, die am 14.05.2002 im  Firmenbuch mit dem Geschäftszweig Immobilientreuhänder, Vermögensberatung neu  eingetragen wurde.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Julian Czernitzki` | `Univ.-Prof. Julian Czernitzki` |

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_164`)


Die Feststellungen zu den Gesellschaftsverhältnissen, zum Geschäftsführer und zum  Prokuristen der Univ.-Prof. Julian Czernitzki  ergeben sich aus den vorliegenden Verfahrensakten und wurden  durch Einsichtnahme des Bundesfinanzgerichts in das Firmenbuch bestätigt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Julian Czernitzki` | `Univ.-Prof. Julian Czernitzki` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/147264.1`) (sent_id: `deanon_BFG_20260814_TEST/147264.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Nikolaus Hinterscheid  in der Beschwerdesache Penelope Tillmann,  Vogeltenn 34, 9843 Döllach, Österreich, gegen die am 24. Oktober 2024 zu Steuernummer 65-259/9307  ausgefertigten Bescheide der belangten Behörde Finanzamt Österreich betreffend Festsetzung  von Anspruchszinsen für die Jahre 2021 und 2022 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Nikolaus Hinterscheid` | `Hon.-Prof. Nikolaus Hinterscheid` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Penelope Tillmann` (person)
- `Vogeltenn 34, 9843 Döllach, Österreich` (address)
- `65-259/9307` (tax_number)
- `Finanzamt Österreich` (organisation)

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Frauke Orsini  in der Beschwerdesache Herbert Czarnezki,  Roacher Straße 40, 9241 Ragain, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 30. September 2019 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt  Österreich/FAÖ) vom 28. August 2019, Erf. Nr. Nr1,   betreffend  1. Festsetzung der Gebühren gemäß § 14 TP 2 Abs. 1 Z 1, TP 5 Abs. 1, TP 6 Abs. 1       und TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:   Der angefochtene Sammelbescheid wird abgeändert wie folgt:  1.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Frauke Orsini` | `Hon.-Prof.in Frauke Orsini` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Herbert Czarnezki` (person)
- `Roacher Straße 40, 9241 Ragain, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt  Österreich/FAÖ` (organisation)

**Example 68** (doc_id: `deanon_BFG_20260814_TEST/147395.1`) (sent_id: `deanon_BFG_20260814_TEST/147395.1_45`)


c) Weiters wurde das "Gutachten zur unionsrechtlichen Zulässigkeit bestimmter  österreichischer Meldemodalitäten für ausländische Skischulbetreiber im Rahmen des  Ausflugsverkehrs" des Univ.-Prof. Leonhard Ehegartner  vom 24.7.2017 vorgelegt, welches dieser im Auftrag  des Deutschen Skilehrerverbandes e.V. erstellt hatte.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Leonhard Ehegartner` | `Univ.-Prof. Leonhard Ehegartner` |

**Example 69** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Evamaria Fränzl  in der Beschwerdesache  Prof. Raphael Grieben, Habegg 37, 5120 Pirach, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien,   betreffend Beschwerde vom 21. Dezember 2023 gegen den Bescheid des Finanzamt Graz-Stadt  vom  30. August 2023 betreffend Vorsteuererstattung 2022 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Evamaria Fränzl` | `Hon.-Prof.in Evamaria Fränzl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof. Raphael Grieben` (person)
- `Habegg 37, 5120 Pirach, Österreich` (address)
- `BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamt Graz-Stadt` (organisation)

**Example 70** (doc_id: `deanon_BFG_20260814_TEST/148979.1`) (sent_id: `deanon_BFG_20260814_TEST/148979.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Janosch Postema  in der Beschwerdesache Juri Gübele,  Gartnerweg 4, 5145 Eisenhub, Österreich, vertreten durch Lydia Alberth, Steuerberaterin, Am Hochsteg 13, 8434  Tillmitsch, betreffend die Beschwerde vom 23.4.2025 gegen den Bescheid des Finanzamtes  Österreich vom 28.1.2025 betreffend Festsetzung einer Zwangsstrafe gemäß § 16 WiEReG iVm  § 111 BAO in Höhe von 1.000,00 Euro beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs 1 lit b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof. Janosch Postema` | `Univ.-Prof. Janosch Postema` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Juri Gübele` (person)
- `Gartnerweg 4, 5145 Eisenhub, Österreich` (address)
- `Lydia Alberth` (person)
- `Finanzamtes  Österreich` (organisation)

**Example 71** (doc_id: `deanon_BFG_20260814_TEST/149239.1`) (sent_id: `deanon_BFG_20260814_TEST/149239.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Lukas Mlnarik  in der Beschwerdesache Mathilda Neuteifl,  Adr, vertreten durch Steuerberater, über die Beschwerde vom 9.4.2015 (gem. § 248 BAO)  gegen den Bescheid des Finanzamtes Innsbruck (nunmehr Finanzamt Österreich/FAÖ) vom  12.12.2014 betreffend die Rückforderung von Familienbeihilfe und Kinderabsetzbetrag für den  Zeitraum 01/2009 bis 11/2014, SV-Nr, nach Durchführung einer mündlichen Verhandlung zu  Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Lukas Mlnarik` | `Hon.-Prof.in Lukas Mlnarik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mathilda Neuteifl` (person)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich/FAÖ` (organisation)

**Example 72** (doc_id: `deanon_BFG_20260814_TEST/149389.1`) (sent_id: `deanon_BFG_20260814_TEST/149389.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Felizia Henrichmöller  in der Beschwerdesache Friedrich Günthardt,  Thonebenstraße 8, 4722 Oberngrub, Österreich, über die Beschwerde vom 13. Oktober 2025, beim Bundesfinanzgericht am  20. Oktober 2025 eingelangt, wegen Verletzung der Entscheidungspflicht des Finanzamtes  Österreich betreffend Erlassung einer Beschwerdevorentscheidung hinsichtlich  Einkommensteuer (Arbeitnehmerveranlagung) 2024, Steuernummer 87-033/9289,  beschlossen:  Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a BAO als  unzulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Felizia Henrichmöller` | `Univ.-Prof.in Felizia Henrichmöller` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Friedrich Günthardt` (person)
- `Thonebenstraße 8, 4722 Oberngrub, Österreich` (address)
- `Bundesfinanzgericht` (organisation)
- `Finanzamtes  Österreich` (organisation)
- `87-033/9289` (tax_number)

**Example 73** (doc_id: `deanon_BFG_20260814_TEST/149321.1`) (sent_id: `deanon_BFG_20260814_TEST/149321.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Eva Oktay  in der Beschwerdesache Christina Schwabendissen,  Leckenholz 16, 6622 Berwang, Österreich, über die Beschwerde vom 19. Februar 2022 gegen den Bescheid des  Finanzamtes Österreich vom 17. Jänner 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2015 Steuernummer 28-969/9448  beschlossen:   I. Die Beschwerde wird gemäß § 278 Abs. 1 lit b BAO in Verbindung mit § 256 Abs. 3  BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Univ.-Prof.in Eva Oktay` | `Univ.-Prof.in Eva Oktay` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Christina Schwabendissen` (person)
- `Leckenholz 16, 6622 Berwang, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `28-969/9448` (tax_number)

**Example 74** (doc_id: `deanon_BFG_20260814_TEST/149565.1`) (sent_id: `deanon_BFG_20260814_TEST/149565.1_2`)


Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Timothy Eichwaldt  in der Beschwerdesache Jeannette Groborz,  Prof. Weinand-Weg 10, 9063 Arndorf, Österreich, zur Beschwerde vom 20. März 2024 gegen den Bescheid des Finanzamtes  Österreich vom 19. März 2024 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2023,  Steuernummer 92-990/8635, beschlossen:  I. Die Beschwerde wird an das vorlegende Finanzamt Österreich zurückgeleitet, da kein  Vorlageantrag eingebracht wurde.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Timothy Eichwaldt` | `Hon.-Prof. Timothy Eichwaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Jeannette Groborz` (person)
- `Prof. Weinand-Weg 10, 9063 Arndorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `92-990/8635` (tax_number)
- `Finanzamt Österreich` (organisation)

**Example 75** (doc_id: `deanon_BFG_20260814_TEST/149717.1`) (sent_id: `deanon_BFG_20260814_TEST/149717.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Antonia Thann  in der Beschwerdesache Chen Stöbermann,  Erlaufpromenade 4, 2442 Schranawand, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, betreffend Beschwerde vom 18. Juni 2024 gegen den Bescheid des  Finanzamtes Österreich vom 12. Juni 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2023 Steuernummer 92-334/0161  beschlossen:   Der Vorlageantrag vom 27.01.2025 wird gemäß § 256 Abs. 3 BAO in Verbindung mit  § 264 Abs. 4 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof.in Antonia Thann` | `Hon.-Prof.in Antonia Thann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Chen Stöbermann` (person)
- `Erlaufpromenade 4, 2442 Schranawand, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Finanzamtes Österreich` (organisation)
- `92-334/0161` (tax_number)

**Example 76** (doc_id: `deanon_BFG_20260814_TEST/149728.1`) (sent_id: `deanon_BFG_20260814_TEST/149728.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Robert Pernegger in der  Verwaltungsstrafsache gegen Hon.-Prof. Jeremias Leibolt, Ebnerwiese 46, 5211 Frauscherberg, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des  Beschuldigten vom 24. Oktober 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 16. Oktober 2025, Zahl: MA67/MA-GZ/2025 zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Hon.-Prof. Jeremias Leibolt` | `Hon.-Prof. Jeremias Leibolt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Robert Pernegger` (person)
- `Ebnerwiese 46, 5211 Frauscherberg, Österreich` (address)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130695.1`) (sent_id: `deanon_BFG_20260814_TEST/130695.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Hilde Heidorn  in der Beschwerdesache Floriane Rötker,  Pernerstorferstraße 56, 9344 Kaindorf, Österreich, vertreten durch Heinz Neuböck Wthrd GmbH 1010 Wien, Bauernmarkt 24,  über die Beschwerde vom 30.12.2010 gegen den Bescheid des Finanzamtes Wien 9/18/19  Klosterneuburg vom 2.11.2010 betreffend Haftung für die Einbehaltung und Abfuhr der  Lohnsteuer für das Jahr 2007 und 2008, Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Mag` — partial — pred is substring of gold: `Univ.-Prof.in Mag.a Hilde Heidorn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Hilde Heidorn`(person)
- `Floriane Rötker`(person)
- `Pernerstorferstraße 56, 9344 Kaindorf, Österreich`(address)
- `Heinz Neuböck Wthrd GmbH`(organisation)
- `Finanzamtes Wien 9/18/19  Klosterneuburg`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131675.1`) (sent_id: `deanon_BFG_20260814_TEST/131675.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Daisy Große-Bölting  in der Beschwerdesache Serena Leutl,  Wanderweg 7, 2763 Thal, Österreich, vertreten durch Bernhart Steuerberatungs GmbH, Alser Straße 23 Tür 27, 1080  Wien, betreffend Beschwerde vom 18. November 2020 gegen die als Bescheid bezeichnete  Erledigung des Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf vom 19. Oktober 2020  betreffend Aufhebungsantrag gemäß § 299 BAO, Steuernummer 47-306/6017,  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Daisy Große` — partial — pred is substring of gold: `Hon.-Prof.in Daisy Große-Bölting`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Daisy Große-Bölting`(person)
- `Serena Leutl`(person)
- `Wanderweg 7, 2763 Thal, Österreich`(address)
- `Bernhart Steuerberatungs GmbH`(organisation)
- `Finanzamtes Wien 3/6/7/11/15 Schwechat Gerasdorf`(organisation)
- `47-306/6017`(tax_number)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Hon.-Prof.in Constanze Neudeck  in der Beschwerdesache Felizitas Johanesson,  Aspangweg 17, 9781 Gailberg, Österreich, vertreten durch Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG, Simbach 7, 4070 Eferding/Farach, über die Beschwerde vom 21.Dezember  2018 gegen die Bescheide des Finanzamtes Graz-Stadt vom 25. August 2016 betreffend die  Erstattung von Vorsteuern für die Zeiträume 01-03/2012, 04-06/2012, 07-09/2012 und 10- 12/2012 zu Steuernummer 48-504/5908  beschlossen:  I)  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Constanze Neudeck` — partial — pred is substring of gold: `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Hon.-Prof.in Constanze Neudeck`(person)
- `Felizitas Johanesson`(person)
- `Aspangweg 17, 9781 Gailberg, Österreich`(address)
- `Holzinger & Partner Steuerberatung und Wirtschaftsprüfung  GmbH & Co KG`(organisation)
- `Finanzamtes Graz-Stadt`(organisation)
- `48-504/5908`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/133674.1`) (sent_id: `deanon_BFG_20260814_TEST/133674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Mag.a Heidrun Eifeler  in der Beschwerdesache Esra Luetje,  Schmiedbachweg 40, 4201 Schiefegg, Österreich, vertreten durch Astoria Wirtschaftstreuhand GmbH & Co KG, Wachaustraße  42-48/A/3, 3500 Krems an der Donau, I. über die Beschwerde vom 06.02.2013 gegen den Be- scheid des Finanzamtes Waldviertel vom 28.01.2013 betreffend Einkommensteuer (Arbeitneh- merveranlagung) 2011, II. über die Beschwerde vom 18.12.2013 gegen den gemäß § 200 Abs 1  BAO idgF vorläufigen Bescheid des Finanzamtes Waldviertel vom 12.12.2013 betreffend Ein- kommensteuer 2012 und III. über die Beschwerde vom 16.03.2016 gegen den Bescheid des Fi- nanzamtes Waldviertel vom 07.03.2016 betreffend Einkommensteuer (Arbeitnehmerveranla- gung) 2014 entschieden:     I. Die Beschwerde gegen den Einkommensteuerbescheid (Arbeitnehmerveranlagung) 2011  wird als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Mag` — partial — pred is substring of gold: `Univ.-Prof.in Mag.a Heidrun Eifeler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Mag.a Heidrun Eifeler`(person)
- `Esra Luetje`(person)
- `Schmiedbachweg 40, 4201 Schiefegg, Österreich`(address)
- `Astoria Wirtschaftstreuhand GmbH & Co KG`(organisation)
- `Finanzamtes Waldviertel`(organisation)
- `Finanzamtes Waldviertel`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Engelbert Voglsang  in der Beschwerdesache DDr.in Magdalena Holtzbecher, Bakk. rer. nat.,  Kefergutstraße 149, 5152 Dorfbeuern, Österreich, über die Beschwerde vom 29.3.2020 gegen den Bescheid des Finanzamtes  Wien 1/23 vom 12.3.2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) für das  Jahr 2019 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Hon.-Prof. Engelbert Voglsang` — partial — pred is substring of gold: `Mag. Hon.-Prof. Engelbert Voglsang`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Engelbert Voglsang`(person)
- `DDr.in Magdalena Holtzbecher, Bakk. rer. nat.`(person)
- `Kefergutstraße 149, 5152 Dorfbeuern, Österreich`(address)
- `Finanzamtes  Wien 1/23`(organisation)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/137569.1`) (sent_id: `deanon_BFG_20260814_TEST/137569.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache KzlR Hon.-Prof. Veit Balsottemeyer, Maria-Hirschler-Weg 3, 9062 Stallhofen, Österreich, über die Beschwerde vom 8. September 2021 gegen den Bescheid des Finanzamtes  Österreich vom 24. August 2021 betreffend Abweisung des Antrages vom 28. August 2020 auf  Auszahlung der Familienbeihilfe ohne Indexierung ab 1. Jänner 2019, Steuernummer 55-184/3803,  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Hon.-Prof. Veit Balsottemeyer` — partial — pred is substring of gold: `KzlR Hon.-Prof. Veit Balsottemeyer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `KzlR Hon.-Prof. Veit Balsottemeyer`(person)
- `Maria-Hirschler-Weg 3, 9062 Stallhofen, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `55-184/3803`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/138157.1`) (sent_id: `deanon_BFG_20260814_TEST/138157.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Sascha de Kort  in der Beschwerdesache Matthew McCarthy,  Stichlberg 18, 4742 Klinget, Österreich, über die Beschwerde vom 29. Oktober 2020 gegen den Bescheid des  Magistrats der Stadt Wien Referat Landes- und Gemeindeabgaben vom 12. Oktober 2020  betreffend Glücksspielautomatenabgabe  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Univ.-Prof.in Sascha` — partial — pred is substring of gold: `Univ.-Prof.in Sascha de Kort`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Sascha de Kort`(person)
- `Matthew McCarthy`(person)
- `Stichlberg 18, 4742 Klinget, Österreich`(address)
- `Magistrats der Stadt Wien`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr  in der Beschwerdesache Hon.-Prof.in Techn R Huberta Pauwels,  Oberapping 6, 4613 Unterholz, Österreich, betreffend Beschwerde vom 14. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 76-699/8954, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Hon.-Prof.in Mag` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`
- `Hon.-Prof.in Techn` — partial — pred is substring of gold: `Hon.-Prof.in Techn R Huberta Pauwels`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`(person)
- `Hon.-Prof.in Techn R Huberta Pauwels`(person)
- `Oberapping 6, 4613 Unterholz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `76-699/8954`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/139843.1`) (sent_id: `deanon_BFG_20260814_TEST/139843.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Priv.-Doz. Andreas Domingo  in der Beschwerdesache Univ.-Prof.in KzlR Tiffany Nowakowsky,  Thumastraße 13, 5201 Brunn, Österreich, vertreten durch "ÖBUG" DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, St.-Veit-Gasse 8, 1130 Wien, über die  Beschwerde vom 14. April 2020 gegen den Bescheid des Finanzamtes Wien 1/23 vom 2. März  2020 betreffend die Abweisung eines Zahlungserleichterungsansuchens, Steuernummer  75-144/0441, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Univ.-Prof.in Kzl` — partial — pred is substring of gold: `Univ.-Prof.in KzlR Tiffany Nowakowsky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Priv.-Doz. Andreas Domingo`(person)
- `Univ.-Prof.in KzlR Tiffany Nowakowsky`(person)
- `Thumastraße 13, 5201 Brunn, Österreich`(address)
- `DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `75-144/0441`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/140189.1`) (sent_id: `deanon_BFG_20260814_TEST/140189.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Helena von Heyl  in der Beschwerdesache des  Charlotte Buckenleib, Badeteich Bisamberg 32, 3500 Imbach, Österreich, vertreten durch StB, über die Beschwerde vom 26. Jänner 2022  gegen den Bescheid des Finanzamt Gmunden Vöcklabruck  vom 7. Jänner 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Steuernummer 20-748/3811  zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Hon.-Prof.in Helena` — partial — pred is substring of gold: `Hon.-Prof.in Helena von Heyl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Helena von Heyl`(person)
- `Charlotte Buckenleib`(person)
- `Badeteich Bisamberg 32, 3500 Imbach, Österreich`(address)
- `Finanzamt Gmunden Vöcklabruck`(organisation)
- `20-748/3811`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Hon.-Prof. David Goldvogel  in der Beschwerdesache Dr. Leroy Stras,  Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich, vertreten durch Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H., Madersbacherweg 26, 6300 Wörgl, gegen den von der belangten Behörde Finanzamt  Österreich am 7. Dezember 2022 ausgefertigten Bescheid, mit dem der Antrag des  Beschwerdeführers vom 11. November 2022 auf Wiederaufnahme des mit  Einkommensteuerbescheid 2019 abgeschlossenen Verfahrens abgewiesen wurde, zu Recht  erkannt:  I. Die Bescheidbeschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. David Goldvogel` — partial — pred is substring of gold: `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`(person)
- `Dr. Leroy Stras`(person)
- `Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich`(address)
- `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_15`)


Für steuerliche Angelegenheiten sei die  Kanzlei MedR Univ.-Prof. Karsten Döngel  als steuerlicher Vertreter zuständig.

**False Positives:**

- `Univ.-Prof. Karsten Döngel` — partial — pred is substring of gold: `MedR Univ.-Prof. Karsten Döngel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MedR Univ.-Prof. Karsten Döngel`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_89`)


Zuvor war er  für den Bf gegenüber dem Finanzamt anwaltlich nicht tätig und die steuerliche Vertretung des  Bf obliegt weiterhin der MedR Univ.-Prof. Karsten Döngel.

**False Positives:**

- `Univ.-Prof. Karsten Döngel` — partial — pred is substring of gold: `MedR Univ.-Prof. Karsten Döngel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `MedR Univ.-Prof. Karsten Döngel`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/141869.1`) (sent_id: `deanon_BFG_20260814_TEST/141869.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Mag. Theobald Rütgens  in der Beschwerdesache Dagmar Weikart,  Stockstraße 28, 9640 Krieghof, Österreich, vertreten durch UnionTax & Law Rechtsanwälte, Obere Zelgstraße 2, 8590  Romanshorn, Schweiz, wegen behaupteter Verletzung der Entscheidungspflicht durch das  Finanzamt Österreich über den Antrag vom 27.7.2022 auf Durchführung der  Arbeitnehmerveranlagung 2020, Steuernummer 50-301/3055  beschlossen:   Die Beschwerde wird gemäß § 284 Abs. 7 lit. b BAO in Verbindung mit § 260 Abs. 1 lit. a BAO  als nicht zulässig zurückgewiesen.

**False Positives:**

- `Univ.-Prof. Mag` — partial — pred is substring of gold: `Univ.-Prof. Mag. Theobald Rütgens`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Mag. Theobald Rütgens`(person)
- `Dagmar Weikart`(person)
- `Stockstraße 28, 9640 Krieghof, Österreich`(address)
- `Finanzamt Österreich`(organisation)
- `50-301/3055`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/142473.1`) (sent_id: `deanon_BFG_20260814_TEST/142473.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Wilfried Brokof  in der Beschwerdesache Hademar Haßelbach, BSc,  Engerbergstraße 2, 8642 Nechelheim, Österreich, über die Beschwerde vom 16. Juni 2022 gegen den Bescheid des Finanzamtes  Österreich vom 1. Juni 2022 betreffend Umsatzsteuer 2014 Steuernummer 59-681/6477  zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Hon.-Prof. Wilfried Brokof` — partial — pred is substring of gold: `Mag. Hon.-Prof. Wilfried Brokof`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Wilfried Brokof`(person)
- `Hademar Haßelbach, BSc`(person)
- `Engerbergstraße 2, 8642 Nechelheim, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `59-681/6477`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch Prof. Yorick Frühbis, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

**False Positives:**

- `Hon.-Prof. Denis Hoffjan` — partial — pred is substring of gold: `Mag. Hon.-Prof. Denis Hoffjan`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Denis Hoffjan`(person)
- `Hon.-Prof.in Ariadne Iwanowsky`(person)
- `Camesinaweg 86, 4652 Taxlberg, Österreich`(address)
- `Prof. Yorick Frühbis`(person)
- `Finanzamt Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/144771.1`) (sent_id: `deanon_BFG_20260814_TEST/144771.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Annette Wöhrl  in der Beschwerdesache VetR Univ.-Prof. Wigand Gervais,  Lorenzen 10, 6183 Kühtai, Österreich, vertreten durch die Steuerkanzlei Holowinski  Partner KG, Hasenauerstraße  18/1/Top 2, 1190 Wien, über die Beschwerde vom 19. Juli 2023 gegen den Bescheid des  Finanzamtes Österreich vom 19. Mai 2023  betreffend Körperschaftsteuer 2020,  Steuernummer 92-114/1027, zu Recht erkannt:   I. Von der Festsetzung der Körperschaftsteuer 2020 wird gemäß § 206 lit. b BAO Abstand  genommen.

**False Positives:**

- `Univ.-Prof. Wigand Gervais` — partial — pred is substring of gold: `VetR Univ.-Prof. Wigand Gervais`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Annette Wöhrl`(person)
- `VetR Univ.-Prof. Wigand Gervais`(person)
- `Lorenzen 10, 6183 Kühtai, Österreich`(address)
- `Steuerkanzlei Holowinski  Partner KG`(organisation)
- `Finanzamtes Österreich`(organisation)
- `92-114/1027`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/144847.1`) (sent_id: `deanon_BFG_20260814_TEST/144847.1_1`)


BESCHLUSS   Das Bundesfinanzgericht fasst durch den Richter Hon.-Prof. Mag. James Thomalla  in der Beschwerdesache Jelena Ziegelmeyer,  Auer-von-Welsbach-Straße 6X, 4083 Sonnleiten, Österreich, über die Beschwerde vom 30.6.2023 gegen den Bescheid des Finanzamtes  Österreich vom 20.6.2023 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 den  Beschluss:   I. Der Vorlageantrag vom 22.9.2023 wird gemäß § 256 Abs 3 iVm § 264 Abs 4 lit d BAO als  gegenstandslos erklärt.

**False Positives:**

- `Hon.-Prof. Mag` — partial — pred is substring of gold: `Hon.-Prof. Mag. James Thomalla`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Mag. James Thomalla`(person)
- `Jelena Ziegelmeyer`(person)
- `Auer-von-Welsbach-Straße 6X, 4083 Sonnleiten, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/146609.1`) (sent_id: `deanon_BFG_20260814_TEST/146609.1_109`)


P. erzielte bei der D. 11.532 € bzw. bei der Bf.:   D. Univ.-Prof. Julian Czernitzki  Arbeitsmarktservice gesamt Einkommen It. ESt- Bescheid  2014 11.532 € 4.200 €  15.732 € 15.540,66 €  2015  5.656 € 1.407 € 7.063 € 5.200,71 €  2016  5.941 €  5.941 € 5.486,10 €  Die Gegenüberstellung verdeutlicht, dass P. über keine ausreichen Einkünfte, die eine  durchschnittliche Lebensführung erfordert, verfügte, sehr wohl aber G.. Gerade dieser Aspekt  zeigt auf, dass in wirtschaftlicher Betrachtungsweise der in der Beschwerde erstmals  vorgetragene Einwand, die Entnahmen zum Verrechnungskonto „P.“ seien G. zuzurechnen,  auch deshalb unglaubwürdig ist, weil (trotz diesbezüglicher Anfrage) nicht aufgeklärt worden  ist, welche konkrete Verwendung die Gelder bei G. gefunden haben sollten.

**False Positives:**

- `Univ.-Prof. Julian Czernitzki  Arbeitsmarktservice` — partial — gold is substring of pred: `Univ.-Prof. Julian Czernitzki`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ.-Prof. Julian Czernitzki`(person)

</details>

---

## `Mag_Title` 🏆

**F1:** 0.014 | **Precision:** 0.733 | **Recall:** 0.007  

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
| 0.733 | 0.007 | 0.014 | 15 | 11 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 4 | 1603 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_1`)


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

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Feldkirch 1 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Josef Ungericht, den Richter Mag. Armin Treichl und die fachkundigen Laienrichter Mag.a  Patricia Kathan-Simma und Mag. Norbert Metzler in Gegenwart der Schriftführerin Isabella  Alexandra Längle in der Finanzstrafsache gegen VetR Vivian Hirtel, Litzlberger Straße 14, 8530 Kresbach, Österreich, vertreten durch Dr.  jur.

| Predicted | Gold |
|---|---|
| `Mag. Josef Ungericht` | `Mag. Josef Ungericht` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)
- `Mag. Armin Treichl` (person)
- `Mag.a  Patricia Kathan` (person)
- `Mag. Norbert Metzler` (person)
- `Isabella  Alexandra Längle` (person)
- `VetR Vivian Hirtel` (person)
- `Litzlberger Straße 14, 8530 Kresbach, Österreich` (address)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/143211.1`) (sent_id: `deanon_BFG_20260814_TEST/143211.1_279`)


Zur Heranziehung von „Angebotsmieten“ bei der Ermittlung der Marktmiete führt Mag. Martin  Pröll (in ÖSTZ 2020/107, ÖSTZ, 2020, 93 Heft 4) aus:  „Vor diesem Hintergrund ist aus „Angebotsmieten" rein gar nichts für das Beweisthema zu  gewinnen.

| Predicted | Gold |
|---|---|
| `Mag. Martin  Pröll` | `Mag. Martin  Pröll` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/143572.1`) (sent_id: `deanon_BFG_20260814_TEST/143572.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Dieter Fröhlich, den   Richter Mag. Christian Seywald, die fachkundigen Laienrichter Johannes Steiner und   Michael Kamper MSc über die Bescheidbeschwerde vom 24.07.2019 des Ulrike Ackermaier, Bakk. iur., Knödelhüttenstraße 12, 9184 Mühlbach, Österreich  vertreten durch Woditschka Steuerberatung GmbH, 2130 Mistelbach, Lanzendorfer  Hauptstraße 9/1, gegen die Umsatzsteuerbescheide für das Jahr 2017 und das Jahr 2018, vom  18.06.2019, des Finanzamtes Gänserndorf Mistelbach (nunmehr FA Österreich),  Steuernummer 75-013/8302, nach Durchführung einer mündlichen Verhandlung am 29.  Jänner 2024 in Anwesenheit des Schriftführers Dietmar Gratz  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Dieter Fröhlich` | `Mag. Dieter Fröhlich` |
| `Mag. Christian Seywald` | `Mag. Christian Seywald` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Johannes Steiner` (person)
- `Michael Kamper MSc` (person)
- `Ulrike Ackermaier, Bakk. iur.` (person)
- `Knödelhüttenstraße 12, 9184 Mühlbach, Österreich` (address)
- `Woditschka Steuerberatung GmbH` (organisation)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `FA Österreich` (organisation)
- `75-013/8302` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/143852.1`) (sent_id: `deanon_BFG_20260814_TEST/143852.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. Albert Salzmann, die  Richterin Dr. Susanne Zankl sowie die fachkundigen Laienrichter Christine Höll und Dr. Rupert  Mayr in der Beschwerdesache Ewald Lüttfrenk, Triftgasse 9, 5145 Königsaich, Österreich, vertreten durch Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG, Forstamtsgasse 6, 5580 Tamsweg, über die  Beschwerde vom 30. März 2021 gegen die Bescheide des Finanzamtes Österreich vom  4. Februar 2020 betreffend Einkommensteuer 2014, 2015, 2016 und 2017 zur Steuernummer  55-257/7759  nach Durchführung einer mündlichen Verhandlung am 5. April 2023 in  Anwesenheit der Schriftführerin Premm Helene zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Albert Salzmann` | `Mag. Albert Salzmann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Susanne Zankl` (person)
- `Christine Höll` (person)
- `Dr. Rupert  Mayr` (person)
- `Ewald Lüttfrenk` (person)
- `Triftgasse 9, 5145 Königsaich, Österreich` (address)
- `Etschbacher &  Partner Wirtschafts- und Steuerberatungs OG` (organisation)
- `Finanzamtes Österreich` (organisation)
- `55-257/7759` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hildegard Nüßgens  in der Beschwerdesache Charles Dormayr,  SET-Straße 22, 4382 Sarmingstein, Österreich, vertreten durch Christandl & Partner Rechtsanwälte, Mag. Heinz Bauer,  Elisabethstraße 50b, 8010 Graz, über die Beschwerde vom  13. Jänner 2020 gegen den  Bescheid des Finanzamtes Österreich vom  11. Dezember 2019 betreffend Grunderwerbsteuer  27.02.2019 Steuernummer 59-652/7687  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Mag. Heinz Bauer` | `Mag. Heinz Bauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr.in Hildegard Nüßgens` (person)
- `Charles Dormayr` (person)
- `SET-Straße 22, 4382 Sarmingstein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `59-652/7687` (tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/149107.1`) (sent_id: `deanon_BFG_20260814_TEST/149107.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Dr. Wiebke Peperkorn in der  Beschwerdesache Emilia Göpfardt, Hundsgrub 5, 4492 Rappersdorf, Österreich, vertreten durch Mag. Dr. Walter Ganster,  Hauptplatz 22, 9100 Völkermarkt, über die Beschwerde vom 6. Dezember 2023 gegen den  Bescheid des Finanzamtes Österreich vom 23. November 2023 betreffend Anspruchszinsen (§  205 BAO) 2021, Steuernummer 17-936/5215, zu Recht erkannt:   I. Der Beschwerde wird teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Mag. Dr. Walter Ganster` | `Mag. Dr. Walter Ganster` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Dr. Wiebke Peperkorn` (person)
- `Emilia Göpfardt` (person)
- `Hundsgrub 5, 4492 Rappersdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `17-936/5215` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/130758.1`) (sent_id: `deanon_BFG_20260814_TEST/130758.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache StR Mag. Dirk Bröders, Adresse_BF1, betreffend die Beschwerde vom 15. Jänner 2015  gegen die Bescheide des Finanzamtes Wien 12/13/14 Purkersdorf vom 11. Dezember 2014  betreffend Haftung für Lohnsteuer gemäß § 82 EStG, Festsetzung des Dienstgeberbeitrages  und des Zuschlages zum Dienstgeberbeitrag für die Jahre 2010 bis 2012, Steuernummer  77-629/3506, beschlossen:  I. Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Mag. Dirk Bröders` — partial — pred is substring of gold: `StR Mag. Dirk Bröders`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `StR Mag. Dirk Bröders`(person)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `77-629/3506`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `Mag. Heinrich Hambücher` — partial — pred is substring of gold: `PhD Mag. Heinrich Hambücher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_75`)


ihr  Geschäftsanteil wurde von der PhD Mag. Heinrich Hambücher (FN xxxxxx) übernommen;

**False Positives:**

- `Mag. Heinrich Hambücher` — partial — pred is substring of gold: `PhD Mag. Heinrich Hambücher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Mag. Heinrich Hambücher`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/144910.1`) (sent_id: `deanon_BFG_20260814_TEST/144910.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Maria Daniel über die Beschwerde der Diana Wüste,Schönangerweg 35, 4925 Gumpling, Österreich, vertreten durch Ing. Mag. Dr. Roland Erwin Hansely, Mahlerstraße 13 Tür 3,  1010 Wien, wegen behaupteter rechtswidriger Ausübung verwaltungsbehördlicher Befehls-  und Zwangsgewalt durch Organe des Zollamtes Österreich am 19.11.2023 durch Ausübung  psychischen Zwangs den Beschluss:   Die Maßnahmenbeschwerde vom 19.12.2023 wird als unzulässig zurückgewiesen.

**False Positives:**

- `Mag. Dr. Roland Erwin Hansely` — partial — pred is substring of gold: `Ing. Mag. Dr. Roland Erwin Hansely`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Maria Daniel`(person)
- `Diana Wüste`(person)
- `Schönangerweg 35, 4925 Gumpling, Österreich`(address)
- `Ing. Mag. Dr. Roland Erwin Hansely`(person)
- `Zollamtes Österreich`(organisation)

</details>

---

## `Dr_Title` 🏆

**F1:** 0.138 | **Precision:** 0.660 | **Recall:** 0.077  

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
| 0.660 | 0.077 | 0.138 | 188 | 124 | 64 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 124 | 64 | 1490 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  RgR Amalia Schuetzke, Binderholz Straße 15, 9312 Pfannhof, Österreich,  gegen den Bescheid des Finanzamtes Salzburg-Land Finanzamtes  Salzburg-Land vom 23. März 2017 betreffend Einkommensteuer (Arbeitnehmerveranlagung)  2016 Steuernummer 22-967/4918  beschlossen:  Die Beschwerde ist als unzulässig zurückzuweisen.

| Predicted | Gold |
|---|---|
| `Dr. Susanne Zankl` | `Dr. Susanne Zankl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `RgR Amalia Schuetzke` (person)
- `Binderholz Straße 15, 9312 Pfannhof, Österreich` (address)
- `Finanzamtes Salzburg-Land` (organisation)
- `Finanzamtes` (organisation)
- `22-967/4918` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_60`)


Der Beschwerdeführer begründet die berufliche Notwendigkeit der Teilnahme an den  gegenständlichen Kursen mit der Erlangung von Kenntnissen und Fähigkeiten zur Anwendung  Hypnosystemischer Konzepte nach Dr. Gunther Schmidt und von Kommunikationsmethoden,  wie sie im Hypnotherapeutischen Bereich zur Anwendung kämen;

| Predicted | Gold |
|---|---|
| `Dr. Gunther Schmidt` | `Dr. Gunther Schmidt` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_67`)


darüber hinaus habe  er sich bereits nach der Teilnahme am ersten von drei Kursen der „Kurzausbildung mit  Dr. Gunther Schmidt – Hypnosystemische Konzepte für Coaching, Team &  Organisationsentwicklung und Supervision“ im Herbst 2018 entschieden, sich im Laufe der Zeit  ein weiteres „Standbein“ aufzubauen, um die erworbenen Kenntnisse als  freiberuflicher/selbständiger Coach anzubieten.

| Predicted | Gold |
|---|---|
| `Dr. Gunther Schmidt` | `Dr. Gunther Schmidt` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128932.1`) (sent_id: `deanon_BFG_20260814_TEST/128932.1_1`)


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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Techn R Lilia Schöpcke, In der Klaus 8, 5651 Winkl, Österreich, über die Beschwerde vom 30. Jänner 2019 gegen den Bescheid des  Finanzamtes Neunkirchen Wr. Neustadt vom 16. Jänner 2019 betreffend Abweisung des  Antrages auf Familienbeihilfe und erhöhte Familienbeihilfe ab Aug.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Lilia Schöpcke` (person)
- `In der Klaus 8, 5651 Winkl, Österreich` (address)
- `Finanzamtes Neunkirchen Wr. Neustadt` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_24`)


Seit 2013 habe sie die Invaliditätspension gehabt und jetzt habe sie Rehabgeld  Ledig, lebt alleine, kein Kinder  Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  zur Untersuchung mitgebrachte Befunde:  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013:  Dg.: emotional instabile Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30.11.- 01.12.2015:  Dg.: ängstlich agitiertes paranoides Zustandsbild bei narzisstisch emotional instabiler  Persönlichkeitsakzentuierung  Befund Neurologin Dr. Mairinger 30.10.2012:  Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012:  Dg.: posttraumatische Belastungsstörung, Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013 posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  2 von 18 Seite 3 von 18

| Predicted | Gold |
|---|---|
| `Dr. Mairinger` | `Dr. Mairinger` |
| `Dr. Schlapschi` | `Dr. Schlapschi` |
| `Dr. Nöllner` | `Dr. Nöllner` |
| `Dr. Mersch` | `Dr. Mersch` |

**Missed by this rule (FN):**

- `Psych Rehab Hollenburg` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_25`)


Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung   Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  Untersuchungsbefund:  Allgemeinzustand: 34 jährige in gutem AZ  Ernährungszustand: gut  Größe: 158,00 cm Gewicht: 50,00 kg    Status (Kopf / Fußschema) - Fachstatus:  Stand und Gang: unauffällig  Sprache und Sprechen: unauffällig  Gesamtmobilität - Gangbild:  kommt frei gehend alleine zur Untersuchung, wurde von Bekannten hergebracht  Führerschein: nein  Psycho(patho)logischer Status:  Kooperativ und freundlich, gut auskunftsfähig, bewußtseinsklar, voll orientiert, leichtes  kognitiv- mnestisches Defizit, Gedankenductus: geordnet, kohärent; logorrhoisch, an  bestimmten Dankzielen haftend, Konzentration reduziert und Antrieb eher angehoben,  Stimmungslage depressiv, weinerlich, kaum afflzierbar;

| Predicted | Gold |
|---|---|
| `Dr. Mersch` | `Dr. Mersch` |
| `Dr. Mersch` | `Dr. Mersch` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_50`)


Dr. Omasits sei in Pension.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_66`)


Rehabilitation  in Hollenburg im J. 2013  Dr. Omasits, FA für Neurologie und Psychiatrie, 05.12.2005: emotional instabile  Persönlichkeitsstörung mit histrionischen Zügen, 21jährige Kosmetik und Fußpflegeschülerin  klagt über rez. Depr.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_68`)


Cipralex und Psychotherapie  Karteiausdruck Dr. Omasits 26.11.2015, 06.10.2015, 28.05.2015,14.04.2015,10.05.2015,  16.03.2007, 12.10.2006, 09.10.2006, 04.09.2006, 06.07.2006, 03.03.2006, 05.12.2005:  emotional instabile Persönlichkeitsstörung mit histrionischen Zügen   Gutachten zur Gewährung der Invaliditätspension 12.04.2016,   Dr. Omasits (Psychiatrie): paranoide Psychose, bei Untersuchung psychotisch halluziniert, IP  auf 1 Jahr wurde empfohlen;

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |
| `Dr. Omasits` | `Dr. Omasits` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_149`)


Rehabilitation  in Hollenburg im J. 2013  Dr. Omasits, FA für Neurologie und Psychiatrie, 05.12.2005: emotional instabile  Persönlichkeitsstörung mit histrionischen Zügen, 21jährige Kosmetik und Fußpflegeschülerin  klagt über rez. Depr.

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Missed by this rule (FN):**

- `FA für Neurologie und Psychiatrie` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_151`)


Cipralex und Psychotherapie   Karteiausdruck Dr. Omasits 26.11.2015, 06.10.2015, 28.05.2015,14.04.2015,10.05.2015,  16.03.2007, 12.10.2006, 09.10.2006, 04.09.2006, 06.07.2006, 03.03.2006, 05.12.2005:  9 von 18 Seite 10 von 18

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_152`)


emotional instabile Persönlichkeitsstörung mit histrionischen Zügen  Gutachten zur Gewährung der Invaliditätspension 12.04.2016, Dr. Omasits (Psychiatrie):  paranoide Psychose, bei Untersuchung psychotisch halluziniert, IP auf 1 Jahr wurde empfohlen;

| Predicted | Gold |
|---|---|
| `Dr. Omasits` | `Dr. Omasits` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_155`)


LK Baden, Psychiatrie, 16.11.2012: Anpassungsstörung, Vd. a. Persönlichkeitsstörung  Arztbrief Psych Rehab Hollenburg 08.08.-19.08.2013: Dg.: emotional instabile  Persönlichkeitsstörung, V.a. Schmerzmittelabusus  Arztbrief Psychiatrie LK Neunkirchen 30 11- 01 12 2015: Dg.: ängstlich agitiertes paranoides  Zustandsbild bei narzisstisch emotional instabiler Persönlichkeitsakzentuierung  Befund Neurologin Dr. Mairinger 30.10.2012: Dg.: Cephalgia, V.a. Persönlichkeitsstörung  Befund Psychiatrin Dr. Schlapschi 12.11.2012: Dg.: posttraumatische Belastungsstörung,  Anpassungsstörung  Befund Psychiater Dr. Nöllner 19.06.2013: posttraumatische Belastungsstörung  Befund Psychiater Dr. Mersch 09.05.2018, 20.11.2018: posttraumatische  Belastungsstörung, Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 04.12.2017, 16.01.2017 posttraumatische Belastungsstörung,  Panikstörung, histrionische Persönlichkeitsstörung  Befund Psychiater Dr. Mersch 21.09.2016: Panikstörung, paranoide Reaktionsbereitschaft  mitgebrachter Befund:  PSD Wr. Neustadt 09/2019: Diagnosen: PTSD, komb.

| Predicted | Gold |
|---|---|
| `Dr. Mairinger` | `Dr. Mairinger` |
| `Dr. Schlapschi` | `Dr. Schlapschi` |
| `Dr. Nöllner` | `Dr. Nöllner` |
| `Dr. Mersch` | `Dr. Mersch` |
| `Dr. Mersch` | `Dr. Mersch` |
| `Dr. Mersch` | `Dr. Mersch` |

**Missed by this rule (FN):**

- `Psych Rehab Hollenburg` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_186`)


Sie legte ein Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für Neurologie und  Psychiatrie vor.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_194`)


von der Bf. vorgelegten Schreiben vom 05.12.2005 von Dr. Omasits Martin, Facharzt für  Neurologie und Psychiatrie.

| Predicted | Gold |
|---|---|
| `Dr. Omasits Martin` | `Dr. Omasits Martin` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129553.1`) (sent_id: `deanon_BFG_20260814_TEST/129553.1_1`)


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

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Monika Kofler in der  Verwaltungsstrafsache gegen Techn R Tosca Häfeli, Seulbergerstraße 12, 3384 Pottschollach, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl.

| Predicted | Gold |
|---|---|
| `Dr. Monika Kofler` | `Dr. Monika Kofler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Tosca Häfeli` (person)
- `Seulbergerstraße 12, 3384 Pottschollach, Österreich` (address)
- `Stadt Wien` (organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/130635.1`) (sent_id: `deanon_BFG_20260814_TEST/130635.1_1`)


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

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_85`)


Behandlungen / Medikamente / Hilfsmittel: Efectin 225mg, Inkotan 15mg, Lasix 40mg,  Pantoprazol 20mg, PK-Merz, Pregabalin 75mg 2x1, Sirdalud 4mg 2x1, Zyprexa 2,5mg 1-2-4-0,  Copaxone Inj.lösung, etc.; FÄ-Betreuung bei Dr. Fux alle 6 Wochen.

| Predicted | Gold |
|---|---|
| `Dr. Fux` | `Dr. Fux` |

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_115`)


• Schreiben des Bezirksgerichtes Donaustadt vom 29. Juli 2013 (Verständigung gemäß §  126 AußStrG)  • Psychiatrisches Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9  Dem Ersteller des Gutachtens, Dr. Wolfgang Baischer, Facharzt für Psychiatrie und Neurologie  wurden folgende Befunde vorgelegt:  Psychiatrische Abteilung des SMZ-Ost, Aufenthalt vom 21. Oktober bis 5. November 2012:  "Chronisch-progrediente Encephalitis disseminata mit organischem Psychosyndrom, gemischte  schizoaffektive Störung.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_161`)


Beweiswürdigung:  Der als erwiesen angenommene Sachverhalt beruht auf den zwei im Wege des  Bundessozialamtes für Soziales und Behindertenwesen (Sozialministeriumservice) erstellten  Gutachten, den vom Bf. vorgelegten ärztlichem Befund der Stellungskommission Wien vom 1.  Dezember 1980, dem BASB-Gutachten vom 29. September 2009 (primär chronisch  progrediente Multiple Sklerose 100% GdB), dem Bescheid der MA 15 vom 13. November 2006  betreffend Gewährung von Pflegegeld, der Studienzeitbestätigung der Universität Wien vom  28. Juli 2016, dem Befundbericht von Prof. Maida vom 2. März 2009, dem psychiatrischen  Gutachten vom 21. Februar 2013, AZ. 38 P x/12h-9, erstellt von Dr. Wolfgang Baischer,  Facharzt für Psychiatrie und Neurologie sowie weiters dem Stellungsuntersuchungsergebnis  des Militärkommando Wien vom 28. August 2013, dem Schreiben der Pensionsversicherung  vom 28. Mai 2013 betreffend Pflegegeld, dem Schreiben des Bezirksgerichtes Donaustadt vom  29. Juli 2013 (Verständigung gemäß § 126 AußStrG), den Arztbriefen der Psychiatrischen  Abteilung des SMZ-Ost betreffend die Aufenthalte des Bf. vom 21. Oktober bis 5. November  2012 und vom 6. bis 9. November 2012.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Missed by this rule (FN):**

- `Universität Wien` (organisation)
- `Prof. Maida` (person)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_166`)


Dr. Wolfgang Baischer diagnostizierte beim Bf. im psychiatrischen Gutachten vom 21. Februar  2013 ein organisches Psychosyndrom bei Encephalitis disseminata (Anm.: multiple Sklerose)  und hielt dazu fest, dass diese degenerative neurologische Erkrankung im Sinne einer  Encephalitis disseminata (Multiple Sklerose) beim Untersuchten seit längerer Zeit bekannt sei.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Baischer` | `Dr. Wolfgang Baischer` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_207`)


Das Gutachten von Prof. Maida datiert mit 2. März  2009, das BASB-Gutachten  vom 29. September 2009, die Befunde/Arztbriefe der  Psychiatrischen Abteilung des SMZ-Ost aus 2012 und das Gutachten von Dr. Baischer vom 21.  Februar 2013.

| Predicted | Gold |
|---|---|
| `Dr. Baischer` | `Dr. Baischer` |

**Missed by this rule (FN):**

- `Prof. Maida` (person)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/130736.1`) (sent_id: `deanon_BFG_20260814_TEST/130736.1_2`)


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

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/130826.1`) (sent_id: `deanon_BFG_20260814_TEST/130826.1_1`)


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

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/131537.1`) (sent_id: `deanon_BFG_20260814_TEST/131537.1_1`)


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

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/131596.1`) (sent_id: `deanon_BFG_20260814_TEST/131596.1_1`)


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

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/131569.1`) (sent_id: `deanon_BFG_20260814_TEST/131569.1_1`)


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

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/131673.1`) (sent_id: `deanon_BFG_20260814_TEST/131673.1_1`)


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

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Siegfried Fenz` | `Dr. Siegfried Fenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `KommR Ing. Ludwig Taspinar, MA` (person)
- `Alt Lenzing 13, 4076 Karling, Österreich` (address)
- `Finanzamtes Wien 1/23` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Thassilo Wedekinn` (person)
- `Kettengasse 36, 4870 Weixlbaum, Österreich` (address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung` (organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/132024.1`) (sent_id: `deanon_BFG_20260814_TEST/132024.1_1`)


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

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |
| `Dr. Franz Kandlhofer` | `Dr. Franz Kandlhofer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Sebastian Pfeiffer, LL.M.` (person)
- `Gerald Cuny-Kreuzer` (person)
- `Christina Tiebout` (person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich` (address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH` (organisation)
- `Finanzamtes Wien 1/23` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/132514.1`) (sent_id: `deanon_BFG_20260814_TEST/132514.1_1`)


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

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Dr. Viktoria Blaser` | `Dr. Viktoria Blaser` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Sven Weichmann` (person)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich` (address)
- `Mag. Kurt Kreith` (person)
- `Finanzamtes Baden  Mödling` (organisation)
- `78-738/0573` (tax_number)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_4`)


Die Beschwerdeführerin (Bf.) Dr. Judith Glazer wurde mit Bescheid des Finanzamtes Baden  Mödling vom 20.08.2020 zur Einkommensteuer 2018 veranlagt.

| Predicted | Gold |
|---|---|
| `Dr. Judith Glazer` | `Dr. Judith Glazer` |

**Missed by this rule (FN):**

- `Finanzamtes Baden  Mödling` (organisation)

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_480`)


Die Schaffung von Kryptowährungen (am Beispiel Bitcoin) – allgemeines (Auszug aus  Domes-Hohl, Die steuerliche Behandlung von virtuellen Währungen am Beispiel von Bitcoins,  Diplomarbeit Institut für Finanzrecht Graz, Univ-Prof. Kerstin Tina Ehrke-Rabl, 2019, S. 3-27;  zum technischen Aufbau des Netzwerks siehe Gerion Entrup, Bitcoin – der Stärkere gewinnt,  2013, Bachelorarbeit, Institut für theoretische Informatik, Dr. Arne Meier):   a. Bitcoin ist eine Kryptowährung und existiert nicht in physischer Form.

| Predicted | Gold |
|---|---|
| `Dr. Arne Meier` | `Dr. Arne Meier` |

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Dr. Ashley Nagelschmidt, Hollenbach 37, 4872 Unterthumberg, Österreich, vertreten durch APP Steuerberatung GmbH,  Waidmannsdorfer Straße 10, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom  24. November 2016 gegen die Haftungs- und Abgabenbescheide gemäß § 99 Abs. 1 EStG 1988  betreffend Einkommensteuer (Abzugsteuer) für die Jahre 2013 bis 2015 des Finanzamtes für  Großbetriebe (nunmehr Finanzamt für Großbetriebe) vom 24. Oktober 2016, Steuernummer  16-165/9893  zu Recht:   Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Elisabeth Hafner` | `Dr. Elisabeth Hafner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Ashley Nagelschmidt` (person)
- `Hollenbach 37, 4872 Unterthumberg, Österreich` (address)
- `APP Steuerberatung GmbH` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `16-165/9893` (tax_number)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/134712.1`) (sent_id: `deanon_BFG_20260814_TEST/134712.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den seit 15.12.2020 zuständigen Richter Dr. Hans Blasina in  der Beschwerdesache Ingrid Dohrmaier, Daläus 14O, 2301 Wittau, Österreich, vertreten durch Korber & Partner WTH-Stb  GmbH, Grünbergstraße 31, 1120 Wien, über die Beschwerde vom 3. Juni 2015 gegen die  Bescheide des gemäß § 323b Abs 1 BAO an die Stelle des Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf getretenen Finanzamtes Österreich vom 29. April 2015 betreffend  Kapitalertragsteuer 2011 und 2013, Steuernummer 41-654/1190, zu Recht erkannt:   I. Die angefochtenen Bescheide werden gemäß § 279 BAO - ersatzlos - aufgehoben.

| Predicted | Gold |
|---|---|
| `Dr. Hans Blasina` | `Dr. Hans Blasina` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ingrid Dohrmaier` (person)
- `Daläus 14O, 2301 Wittau, Österreich` (address)
- `Korber & Partner WTH-Stb  GmbH` (organisation)
- `Finanzamtes Wien 3/6/7/11/15  Schwechat Gerasdorf` (organisation)
- `Finanzamtes Österreich` (organisation)
- `41-654/1190` (tax_number)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/135259.1`) (sent_id: `deanon_BFG_20260814_TEST/135259.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Carla Winterkorn, Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich, über die Beschwerde vom 17. April 2015 gegen die Bescheide des  Finanzamtes Braunau Ried Schärding vom 19. März 2015 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer 43-645/1612  zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Carla Winterkorn` (person)
- `Pfirsichgrabenweg 35, 2152 Wenzersdorf, Österreich` (address)
- `Finanzamtes Braunau Ried` (organisation)
- `43-645/1612` (tax_number)

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Silvius Jaros, Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich, über die Beschwerde vom 16. Mai 2019 gegen den Bescheid des  Finanzamtes Österreich vom 16. April 2019 betreffend Einkommensteuer 2017 Steuernummer  97-301/3674  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Astrid Binder` | `Dr. Astrid Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Silvius Jaros` (person)
- `Canisiusgasse 5, 3392 Pfaffing bei Mauer, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `97-301/3674` (tax_number)

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/136027.1`) (sent_id: `deanon_BFG_20260814_TEST/136027.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Björn Stover, Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich, vertreten durch ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH, Landungsplatz 5, 4864  Attersee/Attersee, über die Beschwerde vom 14. September 2021 gegen die Bescheide des  Finanzamtes Österreich vom 23. August 2021 betreffend die Festsetzung von  Verspätungszuschlägen für die Monate 12/2020, 01/2021 und 03-05/2021, Steuernummer  57-952/0912, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Björn Stover` (person)
- `Franz Defregger-Gasse 13, 8962 Unterlengdorf, Österreich` (address)
- `ATTERSEE TREUHAND  Steuerberatungs- und Wirtschaftsprüfungsgesellschaft mbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `57-952/0912` (tax_number)

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_62`)


In der Regel werden bei den Projekten der Wachsmann u. Rönnepagel Marine GmbH  die notwendigen Aufschließungsarbeiten von der S-GmbH durchgeführt (siehe  Anfragebeantwortung des Landeshauptmann-Stellvertreters Dr. Stöckl betreffend Tätigkeit der Wachsmann u. Rönnepagel Marine GmbH vom 25.03.2015, Nr. xxx der Beilagen zum stenographischen Protokoll des Salzburger  Landtages, 3. Session der 15. GP).

| Predicted | Gold |
|---|---|
| `Dr. Stöckl` | `Dr. Stöckl` |

**Missed by this rule (FN):**

- `Wachsmann u. Rönnepagel Marine GmbH` (organisation)
- `Wachsmann u. Rönnepagel Marine GmbH` (organisation)

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/136470.1`) (sent_id: `deanon_BFG_20260814_TEST/136470.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Lewis Fröhner, Feldgasse, Rattersdorf 6, 6731 Boden, Österreich, gegen den Bescheid des Finanzamtes Feldkirch (nunmehr:  Finanzamt Österreich) vom 25. November 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Peter Steurer` | `Dr. Peter Steurer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lewis Fröhner` (person)
- `Feldgasse, Rattersdorf 6, 6731 Boden, Österreich` (address)
- `Finanzamtes Feldkirch` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/136705.1`) (sent_id: `deanon_BFG_20260814_TEST/136705.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Adriana Eiffler, Waldhofweg 36a, 8321 Entschendorf, Österreich, betreffend Beschwerde vom 24. Februar 2021  gegen die Bescheide des Finanzamtes Österreich vom 9. Oktober 2019 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2017 und Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 78-550/2209, beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Adriana Eiffler` (person)
- `Waldhofweg 36a, 8321 Entschendorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `78-550/2209` (tax_number)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/136975.1`) (sent_id: `deanon_BFG_20260814_TEST/136975.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Severin Iwanowsky  in der Beschwerdesache Richard Joistgen,  Breitenbachstraße 15, 4794 Glatzing, Österreich, über die Beschwerde vom 28. April 2020 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 31. März 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018 Steuernummer 81-572/7905  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Severin Iwanowsky` | `Dr. Severin Iwanowsky` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Richard Joistgen` (person)
- `Breitenbachstraße 15, 4794 Glatzing, Österreich` (address)
- `Finanzamtes  Braunau Ried Schärding` (organisation)
- `81-572/7905` (tax_number)

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter in der Beschwerdesache  Prof.in Alma Siegers, Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 11. August 2020 gegen den Bescheid des  Finanzamtes Österreich vom 22. Juli 2020 betreffend Einkommensteuer 2014, Steuernummer  37-792/2472, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Judith Leodolter` | `Dr. Judith Leodolter` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in Alma Siegers` (person)
- `Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `37-792/2472` (tax_number)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/137043.1`) (sent_id: `deanon_BFG_20260814_TEST/137043.1_2`)


Das Bundesfinanzgericht hat durch den Richter Dr. Massimo Lewerenz  in der Angelegenheit der Parteien  - Natalie Veenema, PLZ1 Stadt1 (Beschwerdeführerin), vertreten durch „die Steuerberater GmbH“,  9020 Klagenfurt und  - Finanzamt Österreich als Amtspartei und als Gesamtrechtsnachfolger des Finanzamt Bruck Eisenstadt Oberwart  über die Beschwerde vom 21.3.2018 gegen den Bescheid des Finanzamt Bruck Eisenstadt Oberwart  vom 26.2.2018  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2016

| Predicted | Gold |
|---|---|
| `Dr. Massimo Lewerenz` | `Dr. Massimo Lewerenz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Natalie Veenema` (person)
- `Finanzamt Österreich` (organisation)
- `Finanzamt Bruck Eisenstadt Oberwart` (organisation)
- `Finanzamt Bruck Eisenstadt Oberwart` (organisation)

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/137075.1`) (sent_id: `deanon_BFG_20260814_TEST/137075.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Techn R Edwin Lamken, Steindl 32, 4076 Lengau, Österreich, vertreten durch Caroline Toifl Rechtsanwalt GmbH, Geusaugasse 17,  1030 Wien, wegen Verletzung der Entscheidungspflicht betreffend die Beschwerde gegen den  Bescheid des Finanzamtes Österreich vom 29.07.2009 betreffend Wiederaufnahme des  Verfahrens hinsichtlich Umsatzsteuer 2006 der Gammersbach&Pelstring Telekom GmbH  Steuernummer 53-479/4428  beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a iVm § 284 Abs. 7 BAO als nicht zulässig  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Techn R Edwin Lamken` (person)
- `Steindl 32, 4076 Lengau, Österreich` (address)
- `Caroline Toifl Rechtsanwalt GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `Gammersbach&Pelstring Telekom GmbH` (organisation)
- `53-479/4428` (tax_number)

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/137110.1`) (sent_id: `deanon_BFG_20260814_TEST/137110.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Harald Adriaans, Pflaster 68, 2872 Neustift am Alpenwalde, Österreich, vertreten durch Mag. Markus Wagner,  Eibenstein 39, 4261 Rainbach/Mühlkreis, über die Beschwerde vom 8. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 25. März 2021, Steuernummer 81-584/4494,  betreffend Einkommensteuer 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen   II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Dr. Ansgar Unterberger` | `Dr. Ansgar Unterberger` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Harald Adriaans` (person)
- `Pflaster 68, 2872 Neustift am Alpenwalde, Österreich` (address)
- `Mag. Markus Wagner` (person)
- `Finanzamtes Österreich` (organisation)
- `81-584/4494` (tax_number)
- `Verwaltungsgerichtshof` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/137230.1`) (sent_id: `deanon_BFG_20260814_TEST/137230.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Dr. Björn Augusto  in der Beschwerdesache Mona Reinhard,  Urschendorf 19, 4261 Kerschbaum, Österreich, vertreten durch IMMUNITAS Wirtschaftsprüfung GmbH, Schlickgasse 3 Tür 7,  1090 Wien, über die Beschwerde der beschwerdeführenden Partei vom 17.05.2022, beim  Bundesfinanzgericht eingelangt am 19.05.2022, wegen behaupteter Verletzung der  Entscheidungspflicht durch das Finanzamt für Großbetriebe betreffend Einkommen- und  Umsatzsteuer 2020 den Beschluss:   I. Das Säumnisbeschwerdeverfahren wird eingestellt.    II. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Dr. Björn Augusto` | `Dr. Björn Augusto` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mona Reinhard` (person)
- `Urschendorf 19, 4261 Kerschbaum, Österreich` (address)
- `IMMUNITAS Wirtschaftsprüfung GmbH` (organisation)
- `Bundesfinanzgericht` (organisation)
- `Finanzamt für Großbetriebe` (organisation)
- `Verwaltungsgerichtshof` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/137250.1`) (sent_id: `deanon_BFG_20260814_TEST/137250.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Anna Radschek in der Beschwerdesache  Johanna Housein, Conrad Hötzendorf-Platz 85, 4861 Raschbach, Österreich, über die Beschwerde vom 17. Mai 2021 gegen den Bescheid des  Finanzamtes Österreich vom 15. April 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Steuernummer 85-874/2370, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Anna Radschek` | `Dr. Anna Radschek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Johanna Housein` (person)
- `Conrad Hötzendorf-Platz 85, 4861 Raschbach, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-874/2370` (tax_number)

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/137369.1`) (sent_id: `deanon_BFG_20260814_TEST/137369.1_17`)


Mag. G verfügt laut den im angefochtenen Erkenntnis wiedergegebenen  Feststellungen des  Finanzamtes über folgende Berechtigungen: Hilfestellung zur Erreichung einer körperlichen  beziehungsweise energetischen Ausgewogenheit, mittels der Methode von Dr. Bach, mittels  Biofeedback oder Bioresonanz, mittels Auswahl von Farben, Düften, Lichtquellen,  Aromastoffen, Edelsteinen und Musik, unter Anwendung kinesiologischer Methoden und  mittels Interpretation der Aura unter Ausschluss jeder an einen Befähigungsnachweis  gebundenen Tätigkeit.

| Predicted | Gold |
|---|---|
| `Dr. Bach` | `Dr. Bach` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Bertha Unverich, Hinterseberweg 13D, 4742 Gewerbepark, Österreich, vertreten durch Dr. Robert Karl Galler, Viktor Keldorfer Strasse 1,  5020 Salzburg, betreffend Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 auf  Aussetzung § 212a BAO Steuernummer 92-593/4806  beschlossen:  Der Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 wird gemäß § 260 Abs 1 lit a  iVm § 278 Abs1 lit a BAO als nicht zulässig zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Susanne Zankl` | `Dr. Susanne Zankl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Bertha Unverich` (person)
- `Hinterseberweg 13D, 4742 Gewerbepark, Österreich` (address)
- `Dr. Robert Karl Galler` (person)
- `92-593/4806` (tax_number)

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/137562.1`) (sent_id: `deanon_BFG_20260814_TEST/137562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dietmar Hülsmeier  in der Beschwerdesache StR Linn Hochleitner,  Am Schlammteich 131, 4741 Perndorf, Österreich, vertreten durch Ewald Kapeller Wirtschaftstreuhand- Steuerberatung GmbH,  Ötztaler Höhe 11, 6430 Ötztal-Bahnhof, über die Beschwerde vom 31. August 2015 gegen die  Bescheide des Finanzamtes Landeck Reutte (nunmehr Finanzamt Österreich) vom 11. August  2015 betreffend Festsetzung von Anspruchszinsen (§ 205 BAO) 2012 und Einkommensteuer  2012, Steuernummer 47-841/9334,  1 ) zu Recht erkannt:   a) Der Beschwerde betr.

| Predicted | Gold |
|---|---|
| `Dr. Dietmar Hülsmeier` | `Dr. Dietmar Hülsmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `StR Linn Hochleitner` (person)
- `Am Schlammteich 131, 4741 Perndorf, Österreich` (address)
- `Ewald Kapeller Wirtschaftstreuhand- Steuerberatung GmbH` (organisation)
- `Finanzamtes Landeck Reutte` (organisation)
- `Finanzamt Österreich` (organisation)
- `47-841/9334` (tax_number)

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Julia Reittinger, Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich, vertreten durch Annemarie Entschev-Kurzmann, Mariahilfer Straße  140 Tür 10, 1150 Wien, vom 25. November 2020, gegen den Bescheid des Finanzamtes  Österreich vom 10. November 2020 betreffend Abweisung des Antrages auf Gewährung der  Familienbeihilfe und des Erhöhungsbetrages ab März 2020, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Wolfgang Pavlik` | `Dr. Wolfgang Pavlik` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Julia Reittinger` (person)
- `Hilde-Hager-Zimmermann-Straße 6, 3822 Griesbach, Österreich` (address)
- `Annemarie Entschev-Kurzmann` (person)
- `Finanzamtes  Österreich` (organisation)

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Frank Ruhleder  in der Beschwerdesache Dr. Luigi Mainholz  vertreten durch STB, über die mit Beschwerden angefochtenen Bescheide des FA Wien 1/23,  Steuernummer 61-747/1918, betreffend Einkommensteuer 2005, 2006, 2008, 2009, 2010  und 2011 zu Recht erkannt:    Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr. Luigi Mainholz` | `Dr. Luigi Mainholz` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Frank Ruhleder` (person)
- `FA Wien 1/23` (organisation)
- `61-747/1918` (tax_number)

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_39`)


Laut einem aufgefundenen Mailverkehr vom 4.12.2013 (UFS-Senat Wien 2 an den damaligen  Landesenatsvorsitzenden Hofrat Dr. Lenneis) wird festgehalten, dass eine „Aktenabtretung  zwischen den Senaten 2 und 14 nicht mehr beabsichtigt“ ist (Anmerkung: Wohl betreffend EST  3 von 8 Seite 4 von 8

| Predicted | Gold |
|---|---|
| `Dr. Lenneis` | `Dr. Lenneis` |

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_56`)


Bereits im Jahr 2002 hatte sich die steuerliche  Vertretung telefonisch und schriftlich aufgrund der anhängigen Betriebsprüfung an Hofrat Dr.  Lenneis gewandt (Thematik Grundanteil).

| Predicted | Gold |
|---|---|
| `Dr.  Lenneis` | `Dr.  Lenneis` |

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_58`)


U.a. wurde von Dr. Keppert auch die „sogenannte Lenneis-Formel“ bemängelt. Zusätzlich  verweist Dr. Keppert auf die Nichtbeachtung von zukünftigen Ertragssteigerungen durch die  Finanz (vgl. Gegenäußerung der Bf., vertreten durch Dr. Keppert, zur Gegenschrift des UFS an  den VwGH vom Juni 2014 zur Streitsache UFS vom 19.12.2012, Zl. RV/0966-W/05).

| Predicted | Gold |
|---|---|
| `Dr. Keppert` | `Dr. Keppert` |
| `Dr. Keppert` | `Dr. Keppert` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_59`)


Mehrere  Immobiliengutachten wurden vorgelegt (Immobiliengutachten von GmbH XY,  Immobiliengutachten von Dr. Keppert selbst), die höhere Bewertungsansätze aufweisen, als  vom FA angesetzt.

| Predicted | Gold |
|---|---|
| `Dr. Keppert` | `Dr. Keppert` |

**Example 64** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Helmut Mittermayr in der Beschwerdesache  Roderich Stenczel, St.-Fridolins-Gasse 7, 4931 Jagleck, Österreich, über die Beschwerde vom 20. August 2013 gegen die Bescheide  des FA Kirchdorf Perg Steyr vom 23. Juli 2013 betreffend Wiederaufnahme gemäß § 303 BAO  der Körperschaftsteuerbescheide 2008 bis 2010, Steuernummer 60-379/9146  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Helmut Mittermayr` | `Dr. Helmut Mittermayr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Roderich Stenczel` (person)
- `St.-Fridolins-Gasse 7, 4931 Jagleck, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `60-379/9146` (tax_number)

**Example 65** (doc_id: `deanon_BFG_20260814_TEST/138001.1`) (sent_id: `deanon_BFG_20260814_TEST/138001.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Astrid Binder in der Beschwerdesache  Nadine Tomczack, Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18- 20 Tür Top 6, 7100 Neusiedl/See, über die Beschwerde vom 17. Februar 2022 gegen den  Bescheid des Finanzamtes Österreich vom 17. Jänner 2022 betreffend Feststellung der  Einkünfte § 188 BAO 2020 Steuernummer 15-984/4583  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr. Astrid Binder` | `Dr. Astrid Binder` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Nadine Tomczack` (person)
- `Eibenbergsiedlung 88, 8130 Wannersdorf, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Finanzamtes Österreich` (organisation)
- `15-984/4583` (tax_number)

**Example 66** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_103`)


Dies war der Behörde bekannt, da  Dr. Kohlfürst bei Ihnen persönlich diesbezüglich vorstellig wurde.

| Predicted | Gold |
|---|---|
| `Dr. Kohlfürst` | `Dr. Kohlfürst` |

**Example 67** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_116`)


Das telefonische Vor - Aviso dieser Vorgangsweise wurde letzte Woche zwischen Dr. Kohlfürst  und Herrn Amtsdirektor V abgestimmt.

| Predicted | Gold |
|---|---|
| `Dr. Kohlfürst` | `Dr. Kohlfürst` |

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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128920.1`) (sent_id: `deanon_BFG_20260814_TEST/128920.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Dr. Kurt Bartold  in der Beschwerdesache der  Gruenleitner Event, über die Beschwerde vom 26. März 2018 gegen den Bescheid des Finanzamtes  Graz-Stadt vom 2. März 2018 betreffend Zurückweisung eines Antrages auf Aufhebung nach  § 295 Abs. 4 BAO (betreffend Einkommensteuer 2005) zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Dr. Kurt Bartold` — partial — pred is substring of gold: `Priv.-Doz. Dr. Kurt Bartold`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Dr. Kurt Bartold`(person)
- `Gruenleitner Event`(organisation)
- `Finanzamtes  Graz-Stadt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/129914.1`) (sent_id: `deanon_BFG_20260814_TEST/129914.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Maria-Luise Wohlmayr über die  Beschwerde des Günter Gopfauf, Schwarze Au Spatzenweg 36, 9411 Priel, Österreich  vertreten durch Quintax gerlich-fischer-kopp  steuerberatungsgmbh, Rainbergstraße 3A, 5020 Salzburg, vom 5. September 2018 gegen den  Bescheid des Finanzamtes Salzburg – Stadt, Aigner Straße 10, 5020 Salzburg, vom 30. Juli 2018  betreffend Wiederaufnahme des Verfahrens zur Einkommensteuer 2012 nach der am 10.  September 2020 über Antrag der Partei (§ 274 Abs. 1 Z 1 BAO) in Salzburg abgehaltenen  mündlichen Verhandlung zu Recht erkannt:  1.

**False Positives:**

- `Dr. Maria` — partial — pred is substring of gold: `Dr. Maria-Luise Wohlmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Maria-Luise Wohlmayr`(person)
- `Günter Gopfauf`(person)
- `Schwarze Au Spatzenweg 36, 9411 Priel, Österreich`(address)
- `Finanzamtes Salzburg – Stadt`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Helga Hochrieser in der  Beschwerdesache Heinz Herper, Im Mühlfeld 20n, 3205 Weinburg, Österreich, vertreten durch Dr. Thomas Hofer-Zeni,  Landstraßer Hauptstraße 82 Tür 11, 1030 Wien, über die Beschwerde vom 28. Juli 2014 gegen  den Bescheid des Finanzamtes Wien 2/20/21/22 vom 8. Juli 2014 betreffend Abweisung des  Antrags vom 2. Oktober 2013 auf Familienbeihilfe und erhöhte Familienbeihilfe ab Oktober  2012, nach Durchführung einer mündlichen Verhandlung am 28. Oktober 2020 zu Recht  erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Thomas Hofer` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Helga Hochrieser`(person)
- `Heinz Herper`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamtes Wien 2/20/21/22`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_71`)


Dr. Maida, Neurologie- und Psychiatriefachärztin.

**False Positives:**

- `Dr. Maida` — partial — pred is substring of gold: `Dr. Maida,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Maida,`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_89`)


Lebt  seit 2005 in teilbetreuter intensiver WG/Verein B. Seit ca. 2012 von Dr. Hofer-Zeni  besachwaltet.

**False Positives:**

- `Dr. Hofer` — partial — pred is substring of gold: `Dr. Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Hofer-Zeni`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_129`)


Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Laut Schreiben von Dr. Thomas Hofer-Zeni vom 10. März 2014 bezog der Bf. von seinem Vater  keinen Unterhalt.     Das Finanzamt wies die Beschwerde unter Zugrundelegung der in dem Gutachten getroffenen  Feststellungen mit Beschwerdevorentscheidung vom 9. Februar 2017 mit der Begründung ab,  dass im Gutachten des Sozialministeriumservice vom 7. Juli 2014 der Grad der Behinderung mit  100 v.H. und das Unvermögen sich den Unterhalt selbst zu verschaffen ab Jänner 2006  festgestellt worden sei.

**False Positives:**

- `Dr. Thomas Hofer` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`
- `Dr. Thomas Hofer` — similar text (different position): `Dr. Thomas Hofer-Zeni`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Thomas Hofer-Zeni`(person)
- `Dr. Thomas Hofer-Zeni`(person)
- `Finanzamt`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_149`)


Mit Beschluss des Bezirksgerichtes Donaustadt vom 15. Mai 2013, Zeichen 7 P x/13 f-16, wurde  Dr. Thomas Hofer-Zeni gemäß § 268 ABGB zum Sachwalter bestellt.  Der Bf. wohnt seit 18. Dezember 2006 in Im Mühlfeld 20n, 3205 Weinburg, Österreich /52, Verein B. Der Verein betreut  Erwachsene, Unterstützungsform: teilbetreut intensiv.

**False Positives:**

- `Dr. Thomas Hofer` — partial — pred is substring of gold: `Dr. Thomas Hofer-Zeni`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Thomas Hofer-Zeni`(person)
- `Im Mühlfeld 20n, 3205 Weinburg, Österreich`(address)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_215`)


Wenn der Sachwalter die Einvernahme von Prof. Maida als Zeugin beantragt, so erachtet das  Bundesfinanzgericht eine derartige Einvernahme als nicht zielführend, da der Bf. erstmals bei  der Neurologin Univ.Prof. Dr. Eva Maria Maida im Jahr 2006 wegen seiner Erkrankung  (Multiple Sklerose) in Behandlung war und diese somit über den Gesundheitszustand des Bf.  für einen Zeitraum, der ca. 30 Jahre zurückliegt, naturgemäß nur Vermutungen anstellen kann.

**False Positives:**

- `Dr. Eva Maria Maida` — partial — pred is substring of gold: `Neurologin Univ.Prof. Dr. Eva Maria Maida`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Maida`(person)
- `Bundesfinanzgericht`(organisation)
- `Neurologin Univ.Prof. Dr. Eva Maria Maida`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/131604.1`) (sent_id: `deanon_BFG_20260814_TEST/131604.1_1`)


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

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache PhD Mag. Heinrich Hambücher, Schlaitenerstraße 65, 9173 Freibach, Österreich, vertreten durch Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH, Theobaldgasse 19, 1060 Wien, über die  Beschwerde vom 15. Mai 2012 gegen die Bescheide des Finanzamtes Österreich vom 24. April  2012 betreffend die Wiederaufnahme des Verfahrens bezüglich Umsatzsteuer 2007 und  Umsatzsteuer 2007 zu Recht erkannt:   1.

**False Positives:**

- `Dr. Thomas Keppert` — partial — pred is substring of gold: `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `Dr. Sebastian Pfeiffer` — partial — pred is substring of gold: `Dr. Sebastian Pfeiffer, LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Dr. Sebastian Pfeiffer, LL.M.`(person)
- `Gerald Cuny-Kreuzer`(person)
- `Dr. Franz Kandlhofer`(person)
- `Christina Tiebout`(person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich`(address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/134299.1`) (sent_id: `deanon_BFG_20260814_TEST/134299.1_648`)


b. Weiters stellt sich die Frage, ob die unterschiedlichen Miningvarianten (Solomining,  Poolmining, Cloudmining) für das umsatzsteuerrechtliche Ergebnis eine Rolle spielen (Klotz  Alexander, Mining von Kryptowährungen aus der Sicht des Steuerrechts, Diplomarbeit, 2020,  Institut für Finanzrecht, Univ-Prof. Dr. Tina Ehrke-Rabel, S. 63-64).

**False Positives:**

- `Dr. Tina Ehrke` — partial — pred is substring of gold: `Univ-Prof. Dr. Tina Ehrke-Rabel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Univ-Prof. Dr. Tina Ehrke-Rabel`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/134472.1`) (sent_id: `deanon_BFG_20260814_TEST/134472.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag.Dr. Thomas Leitner in der  Beschwerdesache Janis Dührkopp, Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich, vertreten durch B O S Bilanz- Organisations- und  Steuerservice GmbH, Graben 29 A, 1010 Wien, über die Beschwerde vom 2. Mai 2016 gegen  die Bescheide des Finanzamtes Wien 2/20/21/22 vom 31. März 2016 betreffend  Einkommensteuer 2010, 2011 und 2012 und betreffend Umsatzsteuer 2010, 2011 und 2012  sowie über die Beschwerde vom 25. Oktober 2016 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 28. September 2016 betreffend Einkommensteuer 2013 zu Recht:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr. Thomas Leitner` — partial — pred is substring of gold: `Mag.Dr. Thomas Leitner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.Dr. Thomas Leitner`(person)
- `Janis Dührkopp`(person)
- `Katharine-Drexel-Straße 9, 4870 Unteralberting, Österreich`(address)
- `Finanzamtes Wien 2/20/21/22`(organisation)
- `Finanzamtes Wien  2/20/21/22`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

**False Positives:**

- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs` — partial — pred is substring of gold: `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH`

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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/135918.1`) (sent_id: `deanon_BFG_20260814_TEST/135918.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin MMag.Dr. Ingrid Fehrer in der  Beschwerdesache Ramon Reissdorf, Paul-Abl-Straße 9, 2822 Bromberg, Österreich, vertreten durch ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, und ECA Schmidt und  Hertwich Steuer- beratungsgesellschaft m.b.H., Bahnhofstraße 2, 5280 Braunau/Inn, über die  Beschwerde vom 17. September 2021 gegen die Bescheide des Finanzamtes Österreich vom  26. August 2021, Steuernummer 86-314/1061, betreffend Abweisung des Antrages auf  Wiederaufnahme der Verfahren hinsichtlich Einkommen- und Umsatzsteuer 2017, zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr. Ingrid Fehrer` — partial — pred is substring of gold: `MMag.Dr. Ingrid Fehrer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `MMag.Dr. Ingrid Fehrer`(person)
- `Ramon Reissdorf`(person)
- `Paul-Abl-Straße 9, 2822 Bromberg, Österreich`(address)
- `ECA Schmidt und Hertwich  Steuerberatungsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Österreich`(organisation)
- `86-314/1061`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_149`)


Die  Mutationen sind auch in Österreich angekommen und verschärfen die Situation deutlich", sagte  Bundeskanzler Sebastian Kurz bei einer Pressekonferenz im Bundeskanzleramt, bei der er  gemeinsam mit Gesundheitsminister Rudolf Anschober, Steiermarks Landeshauptmann  Hermann Schützenhöfer, Wiens Bürgermeister Michael Ludwig und Univ.-Prof. Dr. Oswald  Wagner, Vizerektor der MedUni Wien und Leiter des klinischen Institutes für Labormedizin, über  die Verlängerung des Lockdowns bis 8. Februar informierte.

**False Positives:**

- `Dr. Oswald  Wagner` — partial — pred is substring of gold: `Univ.-Prof. Dr. Oswald  Wagner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hermann`(person)
- `Michael Ludwig`(person)
- `Univ.-Prof. Dr. Oswald  Wagner`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/136442.1`) (sent_id: `deanon_BFG_20260814_TEST/136442.1_231`)


Der Kanzler informierte dabei  gemeinsam mit Gesundheitsminister Rudolf Anschober, dem steirischen Landeshauptmann  Hermann Schützenhöfer, dem Wiener Bürgermeister Michael Ludwig und Univ.-Prof. Dr.  Oswald Wagner, Vizerektor der Medizinischen Universität Wien und Leiter des klinischen  Institutes für Labormedizin, über die weitere Vorgehensweise in der Corona-Krise.

**False Positives:**

- `Dr.  Oswald Wagner` — partial — pred is substring of gold: `Univ.-Prof. Dr.  Oswald Wagner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Hermann`(person)
- `Michael Ludwig`(person)
- `Univ.-Prof. Dr.  Oswald Wagner`(person)
- `Universität Wien`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_5`)


Der Antrag  wurde rückwirkend ab März 2020 gestellt.  Dr. Dok1, Facharzt für Psychiatrie, bescheinigte dem Bf. nach der am 21. Oktober 2020 im  Sozialministeriumservice durchgeführten Untersuchung weder einen Grad der Behinderung  noch eine Erwerbsunfähigkeit, dies mit der Begründung, dass keine ausreichenden Patienten-  bzw. aufschlussreichen medizinischen Unterlagen – bis auf einen 4 Jahre alten Diabetespass –  vorgelegt worden seien.

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok1`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_10`)


Der Bf. wurde am 14. April 2021 ein weiteres Mal untersucht und von Dr. Dok2, Fachärztin für  Allgemeinmedizin, folgendes Gutachten erstellt:  2 von 13 Seite 3 von 13

**False Positives:**

- `Dr. Dok` — partial — pred is substring of gold: `Dr. Dok2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Dok2`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_57`)


Insbesondere der mittlerweile 2020 verstorbene  Prof. Dr. Thomas Keppert (u.a. Wirtschaftsprüfer, Steuerberater, Immobilientreuhänder und  Sachverständiger) warf mit heftigen Worten den Finanzämtern und dem UFS vor, dass  Außenprüfer und in Folge auch der UFS zu sehr durch die in mehreren Artikeln publizierten  Ansichten von Hofrat Dr. Christian Lenneis geprägt wurden (1.1.2003 bis 31.12.2013  Landessenatsvorsitzender UFS, Außenstelle Wien, später Vizepräsident bzw. Präsident des  BFG).

**False Positives:**

- `Dr. Thomas Keppert` — partial — pred is substring of gold: `Prof. Dr. Thomas Keppert`
- `Dr. Christian Lenneis` — partial — pred is substring of gold: `Hofrat Dr. Christian Lenneis`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Dr. Thomas Keppert`(person)
- `Hofrat Dr. Christian Lenneis`(person)
- `BFG`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_36`)


Nach herrschender Literaturmeinung (zB Kommentar Dr. Karl-Werner Fellner zur  Grunderwerbsteuer) könnte ein gemeiner Wert eines Gebäudes in der Regel von einem  Bausachverständigen im Wege der Schätzung erfolgen.

**False Positives:**

- `Dr. Karl` — partial — pred is substring of gold: `Dr. Karl-Werner Fellner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Karl-Werner Fellner`(person)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_12`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

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

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_14`)


Anmerkung:  Die Grundlage für das Gesetz zur Indexierung von Familienleistungen basiert auf einem "Rechts- gutachten zur Neugestaltung der Familienbeihilfe für Kinder, die im EU-Ausland leben für das  BM für Finanzen, erstattet von Univ.-Prof. Dr. Wolfgang Mazal Wien, den 20. Februar 2017".

**False Positives:**

- `Dr. Wolfgang Mazal Wien` — positional overlap with gold: `Univ.-Prof. Dr. Wolfgang Mazal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BM für Finanzen`(organisation)
- `Univ.-Prof. Dr. Wolfgang Mazal`(person)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_59`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

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

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_61`)


Anmerkung:  Die Grundlage für das Gesetz zur Indexierung von Familienleistungen basiert auf einem "Rechts- gutachten zur Neugestaltung der Familienbeihilfe für Kinder, die im EU-Ausland leben für das  BM für Finanzen, erstattet von Univ.-Prof. Dr. Wolfgang Mazal Wien, den 20. Februar 2017".

**False Positives:**

- `Dr. Wolfgang Mazal Wien` — positional overlap with gold: `Univ.-Prof. Dr. Wolfgang Mazal`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BM für Finanzen`(organisation)
- `Univ.-Prof. Dr. Wolfgang Mazal`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_10`)


In Beantwortung der Schreiben des Finanzamtes übermittelte die Bf. am 25. Juni 2020 folgende  Unterlagen betreffend ihren Sohn A.:   – Psychologisches Gutachten von Dr. Mag. E.Sch., Klinische und Gesundheitspsychologin,  allgemein beeidete und gerichtlich zertifizierte Sachverständige für Psychologie,  Psychotherapeutin, und Quirin Spillmann, LLB  Klinische und Gesundheitspsychologin, vom 26. Juni 2019   – Hörverarbeitungsscreening durch Hörtrainer N.R. vom 14. November 2019   (Ergebnis auffällig;

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamtes`(organisation)
- `Dr. Mag. E.Sch.`(person)
- `Quirin Spillmann, LLB`(person)
- `N.R.`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_11`)


Empfehlung zu weiteren Tests bzw. Beratungsgespräch)   – Schreiben der Dr. Mag. E.Sch., w.o., vom 18. Dezember 2019 (Zusammenfassung der  Ergebnisse der erfolgten Begutachtung bezüglich einer vermuteten Legasthenie)   – Schulnachricht der Klasse 6 (6. Schulstufe) der Rudolf Steiner … Freie Waldorfschule vom  14. Februar 2020 (Deutsch genügend, Mathematik nicht genügend, Englisch nicht genügend)   – Befundbericht von Univ. Prof.Charlotte Koebbe  Facharzt für Hals-, Nasen-, Ohrenheilkunde, Kopf- und  Halschirurgie, allgemein beeideter und gerichtlich zertifizierter Sachverständiger vom 27. Mai  2020 (Diagnose: Verdacht auf auditive Verarbeitungsstörung;

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mag. E.Sch.`(person)
- `Charlotte Koebbe`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_139`)


Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   Dr. Sch., klin.

**False Positives:**

- `Dr. Sch` — partial — pred is substring of gold: `Dr. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sch.`(person)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_158`)


Ritalin mit Beginn ab Einschulung ab Herbst 2020   Sozialanamnese:   lebt zuhause bei den Eltern, Bruder 12J ADHS, besucht die NMS mit Regelbeschulung   Zusammenfassung relevanter Befunde (inkl. Datumsangabe):   Dr. Sch., klin.

**False Positives:**

- `Dr. Sch` — partial — pred is substring of gold: `Dr. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sch.`(person)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_232`)


Bei der Begutachtung fand das eingangs im Punkt Verfahrensgang genannte, von der Bf.  beschaffte und im Verfahren vorgelegte psychologische Gutachten der Dr. Mag. E.Sch.,  Klinische und Gesundheitspsychologin, allgemein beeidete und gerichtlich zertifizierte  19 von 24 Seite 20 von 24

**False Positives:**

- `Dr. Mag` — partial — pred is substring of gold: `Dr. Mag. E.Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Mag. E.Sch.`(person)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_239`)


In dem Gutachten wurde das Vorliegen eines Dauerzustandes festgestellt.   Das vierte Sachverständigengutachten des Bundessozialamtes wurde auf Grund einer  Untersuchung des Sohnes der Bf. durch einen Facharzt für Kinder- und Jugendheilkunde am  31. August 2020 erstellt. Bei diesem Gutachten wurden folgende (neu dazugekommenen)  relevanten Befunde bzw. Unterlagen (vgl. die im Verfahrensgang angeführten Atteste)  berücksichtigt:   Dr. Sch., klin.

**False Positives:**

- `Dr. Sch` — partial — pred is substring of gold: `Dr. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Sch.`(person)

</details>

---

## `Herrn_Name_Full` 🏆

**F1:** 0.043 | **Precision:** 0.632 | **Recall:** 0.022  

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
| 0.632 | 0.022 | 0.043 | 57 | 36 | 21 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 36 | 21 | 1578 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_36`)


Im Ermittlungsverfahren wurde bekannt gegeben, dass das Fahrzeug Herrn Vera Schliephacke  überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_6`)


Weiters heißt es darin: „Da Herr Stavrakis im  Steuerjahr 2014 noch als in Österreich unbeschränkt Steuerpflichtiger eine Erklärung zur  Arbeitnehmerveranlagung (L1) einreichen wird, ersuchen wir Sie die unbeschränkte  Steuernummer von Herrn Stavrakis erst ab abgeschlossener Veranlagung 2014 auf eine  Steuernummer bei beschränkter Steuerpflicht abzuändern.“

| Predicted | Gold |
|---|---|
| `Stavrakis` | `Stavrakis` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_44`)


Betreffend die Beschwerdegründe verweisen wir einerseits auf die bisherigen Ausführungen in  der Beschwerde und andererseits auf die noch nicht erwähnte Auskunft von Herrn Dimitri Witkoski der  in Rücksprache mit Herrn Ruckelshaußen stand.

| Predicted | Gold |
|---|---|
| `Dimitri Witkoski` | `Dimitri Witkoski` |
| `Ruckelshaußen` | `Ruckelshaußen` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_45`)


Nach Antwort von Herrn Ruckelshaußen vom 04.08.2015 betreffend  „asymmetrische Arrondierung und Immo-Est-Befreiung“ kommt im wörtlichen Sinne die  Befreiungsbestimmung des § 30 Abs 2 Z 4 EStG immer für denjenigen zur Anwendung, bei dem  ein Grundstückstausch einen Flurbereinigungsvorgang darstellt. Wenn für einen Tauschpartner  eine Flurbereinigung gegeben ist (und auch ein Tausch und keine Veräußerung vorliegt - dh  keine Aufzahlungen über 50%), dann greift für diesen die Befreiung, wohingegen der andere  Tauschpartner steuerpflichtig ist.

| Predicted | Gold |
|---|---|
| `Ruckelshaußen` | `Ruckelshaußen` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_48`)


Einerseits bei Herrn WM ….  (IE vom 03/2014 iHv EUR 59.620,-) und andererseits bei Herrn Lisa Lindnau (IE vom 03/2014  iHv  EUR 33.154).

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_51`)


Daher ersuchen wir um Berücksichtigung der Befreiung von der ImmoESt für Herrn Lisa Lindnau,  da im gegenständlichen Tauschverhältnis nur der Rechtserwerb des Herrn Lisa Lindnau  die  Voraussetzungen eines Flurbereinigungsverfahrens erfüllt und dergestalt einen  anderslautenden Bescheid nach sich gezogen hätte.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_1`)


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  Herrn Petra Port, geb. 1980, Konventweg 36, 4613 Unterholz, Österreich, vertreten durch Burka Vitek Moser  Rechtsanwälte, Wächtergasse 1, 1010 Wien, wegen der Finanzvergehen der (teils versuchten)  Abgabenhinterziehungen und der Finanzordnungswidrigkeit gemäß §§ 13, 33 Abs. 1 und 51  Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  15. Februar 2021 gegen das Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien  9/18/19 Klosterneuburg als Organ des ehemaligen Finanzamtes Waldviertel als  Finanzstrafbehörde vom 12. November 2020, SpS, Strafnummer, nach Durchführung einer  mündlichen Verhandlung am 7. September 2021 in Anwesenheit des Beschuldigten, seines  Verteidigers Rechtsanwalt Mag. Wolfgang Moser, des Amtsbeauftragten HR A. sowie der  Schriftführerin P. zu Recht erkannt:  Der Beschwerde wird teilweise stattgegeben und das angefochtene Erkenntnis des  Spruchsenates im Ausspruch über die Strafen wie folgt abgeändert:  Über Herrn Petra Port  wird gemäß §§ 33 Abs. 5, 51 Abs. 2 FinStrG eine Geldstrafe in Höhe von  6.800,00 verhängt.

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes` (organisation)
- `Konventweg 36, 4613 Unterholz, Österreich` (address)
- `Burka Vitek Moser  Rechtsanwälte` (organisation)
- `Finanzamt Wien  9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)
- `Mag. Wolfgang Moser` (person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/134646.1`) (sent_id: `deanon_BFG_20260814_TEST/134646.1_25`)


Im Vorlagebericht wurde seitens des Finanzamtes folgende  Stellungnahme angeführt:  „Die Abgabenbehörde beantragt die Abweisung des Alleinverdienerabsetzbetrages, da Frau A.  nicht nur die von Herrn Bernett angeführten Einkünfte in Höhe von 5.118,52 Euro erzielt hat,  sondern auch eine Abfertigung von der Vorsorgekasse erhalten hat.

| Predicted | Gold |
|---|---|
| `Bernett` | `Bernett` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_8`)


Mit fristgerechter E-Mail vom 13. März 2021 (Anhang: Lenkerauskunft) nannte die  Zulassungsbesitzerin Herrn Bodewein als jene Person, der das genannte Kraftfahrzeug zum  Beanstandungszeitpunkt überlassen war.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_9`)


Mit Strafverfügung vom 16. März 2021 zu Zahl MA67/Zahl1/2020 lastete der Magistrat der  Stadt Wien, MA 67,Herrn Bodewein an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen Autonummer (A) am 16. Dezember 2020 um 10:38 Uhr in der gebührenpflichtigen  Kurzparkzone in 1020 Wien, Abstellort abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der  Stadt Wien` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_11`)


Wegen Verletzung der Rechtsvorschriften des § 5 Abs. 2  Wiener Parkometerabgabeverordung iVm § 4 Abs. 1 Wiener Parkometergesetz 2006 wurde  über Herrn Bodewein eine Geldstrafe iHv € 60,00 und für den Uneinbringlichkeitsfall eine  Ersatzfreiheitsstrafe von 14 Stunden verhängt.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_14`)


Mit Schreiben des Magistrates der Stadt Wien, MA 67 vom 21. April 2021  (Verfahrensanordnung – Nachreichung Unterschrift bzw. Vollmachtsvorlage) wurde die Firma  X_KG zur Vorlage einer Vollmacht, aus welcher das Vertetungsverhältnis zu Herrn Bodewein sowie die  Berechtigung zur Einbringung des Rechtsmittels hervorgehe, binnen zwei Wochen nach  Zustellung des Schreibens aufgefordert.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_16`)


Der Magistrat der Stadt Wien, MA 67, erließ an Herrn X einen mit 10. Mai 2021 datierten  Bescheid, mit welchem der Einspruch vom 21.03.2021 gegen die an Herrn Bodewein gerichtete  Strafverfügung vom 16.03.2021 infolge der Nichtvorlage der Vollmacht gemäß § 13 Abs. 3 AVG  als unzulässig zurückgewiesen wurde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_25`)


Der Magistrat der Stadt Wien ersuchte Herrn Bodewein um Bekanntgabe seiner Telefonnummer  zwecks Klärung des Sachverhaltes, was Herr Bodewein mit E-Mail vom 29. September 2021  beantwortete.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_39`)


Erst ein Telefonat zwischen Magistrat der Stadt Wien und Herrn Bodewein hat ergeben, dass es sich  um beim Anbringen vom 15. September 2021 um eine Beschwerde handeln solle.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_59`)


Für Herrn Bodewein geht hingegen die absolute Unzulässigkeit einer Revision gemäß § 25a Abs. 4  VwGG vor (siehe Rechtsmittelbelehrung).

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/139780.1`) (sent_id: `deanon_BFG_20260814_TEST/139780.1_26`)


Im Vorlageantrag wird ausgeführt:  „Herr B ist nach Angaben meines Mandanten erst im Sommer 2013 nach Österreich gekommen  und war ausschließlich für Herrn Mathusczyk tätig.

| Predicted | Gold |
|---|---|
| `Mathusczyk` | `Mathusczyk` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_17`)


Im Gegenteil war es so, daß  die Touristik Werkvalbach GmbH die fälligen Gebäudemieten, welche an Herrn Jeanne Kraenzlin  zu zahlen gewesen  wären, nicht bedienen konnte.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Missed by this rule (FN):**

- `Touristik Werkvalbach GmbH` (organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_54`)


Der Verzicht wurde somit vom steuerlichen  Vertreter - auch im Namen von Herrn Jeanne Kraenzlin - abgegeben.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/140633.1`) (sent_id: `deanon_BFG_20260814_TEST/140633.1_57`)


Im Übrigen wird noch darauf verwiesen, dass im Zuge der Niederschrift zur  Schlussbesprechung vom steuerlichen Vertreter erklärt wurde, dass die Kapitalertragsteuer  (KESt) von den Gesellschaftern (somit auch von Herrn Jeanne Kraenzlin) getragen wird.

| Predicted | Gold |
|---|---|
| `Jeanne Kraenzlin` | `Jeanne Kraenzlin` |

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_29`)


Und weiter: „[…]  hätte Herr Quentin Schwartkopp  diese Freimengen nicht beanspruchen dürfen, da der Sohn bereits seit  03.bbb.2013 nicht im gemeinsamen Haushalt mit Herrn Quentin Schwartkopp  lebte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_32`)


Im Bescheid II vom 20.2.2019 wurde für Herrn Quentin Schwartkopp, Adresse_Bf., gemäß § 8 Abs. 1 Z 2  AlkStG iVm. § 201 Abs. 1 und Abs. 2 Z 3 der Bundesabgabenordnung (BAO) die Alkoholsteuer  für 2016 in Höhe von € 280,00 festgesetzt.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamt` (organisation)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)


Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die Engelbert Schefe, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Engelbert Schefe` (person)
- `Retzenweg 1, 8504 Tobis, Österreich` (address)
- `Amt für Betrugsbekämpfung` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_47`)


Erst im Einspruch vom 18. März 2024 gegen die beiden Strafverfügungen vom 11. März  2024, GZ. 1) MA67/GZ1/2024 und 2) MA67/GZ2/2024, brachte der Bf. erstmals vor, dass das in  Rede stehende Fahrzeug zur jeweiligen Beanstandungszeit von Herrn Schwent gelenkt wurde.

| Predicted | Gold |
|---|---|
| `Schwent` | `Schwent` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/145004.1`) (sent_id: `deanon_BFG_20260814_TEST/145004.1_8`)


Begründung  Verlauf des Verfahrens  Mit Straferkenntnis vom 27. Dezember 2023, GZ MA67/111111/2023, hat der Magistrat der  Stadt Wien, Magistratsabteilung 67, als belangte Behörde Herrn Arthur Soyal (in weiterer Folge:  Beschwerdeführer) angelastet, er habe die Parkometerabgabe fahrlässig verkürzt, indem er  das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen W-6789 (A) am 4. August  2023 um 11:10 Uhr in einer gebührenpflichtigen Kurzparkzone in 1160 Wien, Hasnerstraße  129, abgestellt habe, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Arthur Soyal` | `Arthur Soyal` |

**Missed by this rule (FN):**

- `Magistrat der  Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_16`)


Der E-Mail vom 5. Februar 2025 war folgende Vollmacht beigelegt:   „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024 , wohnt Adr1, den  Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt  Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte Akzeptieren Sie das  Einspruch.“

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_31`)


Mit E-Mail vom 5. Februar 2025 übermittelte der Beschwerdeführer ein Schreiben des M mit  folgendem Inhalt: „hiermit bevollmächtige ich, M1 geboren, das Auto mit GZ MA67/GZ/2024,  wohnt Adr1, den Herrn Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu  Magistrat der Stadt Wien Magistratsabteilung 67 schicken, wie mit Frau C besprochen, bitte  Akzeptieren Sie das Einspruch“.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_44`)


Der belangten Behörde ist zwar zuzustimmen, dass die schriftliche Vollmacht mit  5. Februar 2025 datiert und somit erst nach der Verfahrenshandlung (Erhebung des  Einspruches) vom 10. September 2024 errichtet wurde, die Behörde lässt hierbei jedoch außer  Betracht, dass es sich sowohl bei dem Beschwerdeführer als auch bei dem Vollmachtgeber um  Personen mit offenkundig mangelnden Sprachkenntnissen handelt. Aus der gewählten  Ausdrucksweise lässt sich nach Ansicht des Bundesfinanzgerichts jedoch ableiten, dass der  Beschwerdeführer bereits vor der Verschriftlichung der Vollmacht, nämlich bereits im  Zeitpunkt der Setzung der Verfahrenshandlung am 10. September 2024 mündlich von M zur  Erhebung eines Einspruches gegen die Strafverfügung bevollmächtigt war (Arg: „[…] Herrn  Pjotr Niessl  geb. am TT.09.1981, dass einen Email als Einspruch zu Magistrat der Stadt Wien  Magistratsabteilung 67 schicken […]“).

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichts` (organisation)
- `Magistrat der Stadt Wien` (organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_16`)


Es wurde in diesem Zusammenhang auch die einschlägige  Gewerbeberechtigung bei Herrn Kaspar Sadowski  wieder als aktiv gemeldet.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_105`)


ln Ihrer Stellungnahme gaben Sie im Wesentlichen an, dass das Fahrzeug am Morgen dieses  Tages in der STRASSE-Hauptwohnsitz von Herrn Dr. YYY übernommen worden wäre und Ihnen  dieser mitgeteilt hätte, dass er einige Tage nach Ungarn fahren werde.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/132075.1`) (sent_id: `deanon_BFG_20260814_TEST/132075.1_72`)


Am 26.1.2018 (am Tag danach) seien zwei Poststücke per Einschreiben mit den  Aufgabenummern RQ … 747 und 748 versendet worden, die von Herrn Mag. Sch. auf dem  Nachhauseweg beim Postamt W. aufgegeben worden seien.

**False Positives:**

- `Sch` — partial — pred is substring of gold: `Mag. Sch.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Sch.`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_35`)


Zusätzlich  sei der Beschwerdeführerin unbedingt empfohlen worden, die OP von Herrn Dr. B einem  anerkannten Schulterspezialisten ausführen zu lassen.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_45`)


Als letzter  Versuch hätte sie auf Empfehlungen Herrn Dr. B, einen anerkannten Schulterspezialisten,  aufgesucht, welcher endlich nach einem langen Leidensweg die richtige Diagnose gestellt und  zu einer sofortigen Operation geraten hätte.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_58`)


Die streitgegenständliche Operation wurde schließlich in der Klinik Diakonissen Linz von Herrn  Dr. B durchgeführt (stationärer Aufenthalt von 15.5. bis 20.5.2019).

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_34`)


Dazu wird auch auf den Bauvertrag und die Treuhandvereinbarung verwiesen, den die Firma  MH-Bau GmbH am 5.3.2015 unterfertigt hat und der in weiterer Folge am 18.3.2015 auch von  den Käufern in der Kanzlei von Herrn Dr-F, der die treuhändige Abwicklung übernommen hatte,  unterfertigt wurde.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `MH-Bau GmbH`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_19`)


Die Überprüfung der durchgeführten Selbstberechnungen erfolgte dergestalt, als Herrn Dr. F  dem Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel einen Datenträger zur Verfügung  gestellt hat.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)
- `Finanzamt für Gebühren`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_20`)


Nach den Angaben von Herrn Dr. F sollten auf diesem Datenträger alle notwendigen  Unterlagen gespeichert sein, welche für die ordnungsgemäße Selbstberechnung notwendig  gewesen sind (siehe dazu auch die Ausführungen in der Einleitung).

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_26`)


Infolge sind von Herrn Dr. F Unterlagen - im Begleitschreiben als Gutachten bezeichnet sowie  Mietverträge - per Mail vorgelegt worden.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_116`)


Das telefonische Vor - Aviso dieser Vorgangsweise wurde letzte Woche zwischen Dr. Kohlfürst  und Herrn Amtsdirektor V abgestimmt.

**False Positives:**

- `Amtsdirektor` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Kohlfürst`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_31`)


Das Finanzamt hat dazu folgende Stellungnahme abgegeben:  „Der Mehmet Köprücü  gab am 20.04.2022 seine Vollmacht für das Haftungsverfahren  Evamaria Watenphul  bekannt und beschrieb sie wortwörtlich so:  Haftungsbescheide je vom 23.03.2022  Und:  In der außen bezeichneten Finanzsache haben die Beschwerdeführer … Evamaria Watenphul, … als  ehemalige Geschäftsführer der Özyilmaz Recycling GmbH., Herrn Mehmet Köprücü  Vollmacht erteilt,  wobei sich der gefertigte Anwalt auf diesem ihm erteilte Vollmacht beruft.

**False Positives:**

- `Mehmet Köprücü  Vollmacht` — similar text (different position): `Mehmet Köprücü`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt`(organisation)
- `Mehmet Köprücü`(person)
- `Evamaria Watenphul`(person)
- `Evamaria Watenphul`(person)
- `Özyilmaz Recycling GmbH.`(organisation)
- `Mehmet Köprücü`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_28`)


Im Zuge des Ermittlungsverfahrens wurde festgestellt, dass der aktuelle Hauptwohnsitz von  Herrn Sohn, geb. am 25.gggg.1981, seit 03.bbb.2013 in Adresse_Sohn, ist.“

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_30`)


Da diese Umstände  von Herrn Quentin Schwartkopp  nicht geändert bzw. bekannt gegeben wurden, waren die im Spruch  angeführten Abfindungsanmeldungen hinsichtlich der zugrundeliegenden Grunddaten zu  berichtigen, nachdem bei Herrn Sohn [..] keine Haushaltsangehörigkeit iSd. § 70 Abs. 3 AlkStG  vorlag bzw. vorliegt.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Quentin Schwartkopp`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_35`)


Mit  Änderungsanzeige vom 01.10.2018 wurde beim Zollamt Innsbruck, Zollstelle Kufstein, von  Herrn Sohn bekannt gegeben, am 01.mt.2011 das gegenständliche landwirtschaftliche  Anwesen samt dem einfachen Brenngerät von Herrn Quentin Schwartkopp  durch Übergabe übernommen  zu haben.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)
- `Quentin Schwartkopp`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_108`)


Im erwähnten Straferkenntnis vom  7.11.2022 hat die belangte Behörde diese Ermittlungsergebnisse auch wiedergegeben und  dazu auszugsweise wie folgt ausgeführt:  „Ermittlungen ergaben, dass für Herrn Rudolf B kein Ausweis gemäß § 29b StVO ausgestellt  wurde.

**False Positives:**

- `Rudolf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_110`)


……  Im Übrigen ist auch der lt. Anzeigeangaben im Fahrzeug nicht gut erkennbar hinter der  Windschutzscheibe eingelegte Parkausweis gemäß § 29b StVO, dessen Ausweisnummer  teilweise durch eine Postkarte verdeckt war, nicht für Herrn Rudolf B ausgestellt.“

**False Positives:**

- `Rudolf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_17`)


Mit Schreiben vom 4. März 2025 teilte die belangte Behörde dem Bf. mit, mit Lenkerauskunft  vom 03.03.2025 zur Zahl MA67/GZ1/2024 habe er Herrn Lenker1, geb. am geb, als Lenker des  Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 am 20.11.2024 um 17:06 Uhr namhaft  gemacht.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_36`)


Auch die  Tatsache, dass der Bf. im Einspruch gegen die an ihn ergangene Strafverfügung (wegen  Erteilung einer unrichtigen Lenkerauskunft) eine dritte Person, nämlich Herrn Lenker5 als  Lenker genannt habe, wohingegen der Bf. in seiner Lenkerauskunft vom 03.03.2025 Herrn  Lenker4 angeführt habe, spreche dafür, dass es sich bei der Angabe des bzw. der vom Bf.  genannten Lenker um eine reine Schutzbehauptung handle.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation
- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/148602.1`) (sent_id: `deanon_BFG_20260814_TEST/148602.1_91`)


In der fristgerecht beantworteten Lenkererhebung vom 26. Februar 2025  gab er hingegen Herrn Lenker1 als Lenker an, der zum Zeitpunkt der Auskunft wiederum  keinen Wohnsitz in Österreich hatte.

**False Positives:**

- `Lenker` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_277`)


Die Angaben von Herrn Baumeister Y X werden nicht zur Sachverhaltsfeststellung  herangezogen, weil sie nach der hier vertretenen Auffassung nicht relevant sind und jedenfalls  unzuverlässig sind, wie auch im Detail in Abschnitt 14 dargestellt wird.

**False Positives:**

- `Baumeister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Priv_Dozi_Title` 🏆

**F1:** 0.045 | **Precision:** 0.623 | **Recall:** 0.024  

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
| 0.623 | 0.024 | 0.045 | 61 | 38 | 23 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 38 | 23 | 1576 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128866.1`) (sent_id: `deanon_BFG_20260814_TEST/128866.1_1`)


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

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129198.1`) (sent_id: `deanon_BFG_20260814_TEST/129198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Li Schukardt  in der Beschwerdesache Ursula Buchholz,  Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich, über die Beschwerde vom 30. Juli 2008 gegen den Bescheid des Finanzamtes  Landeck Reutte vom 17. Juli 2008 betreffend Einkommensteuer 2007 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Li Schukardt` | `Priv.-Doz. Li Schukardt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ursula Buchholz` (person)
- `Pflegeheim Baumgarten 179, 9602 Hohenthurn, Österreich` (address)
- `Finanzamtes  Landeck Reutte` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131215.1`) (sent_id: `deanon_BFG_20260814_TEST/131215.1_1`)


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

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jaden Mikulla  in der Beschwerdesache Ida Gündüz,  Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich, über die Beschwerde vom 2. Dezember 2020 gegen den Bescheid des  Finanzamtes Österreich vom 25. November 2020 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019 Steuernummer 08 209/8427 zu Recht erkannt:   Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Jaden Mikulla` | `Priv.-Doz.in Jaden Mikulla` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ida Gündüz` (person)
- `Schloß Strelzhof 25, 2542 Kottingbrunn, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


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

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/133626.1`) (sent_id: `deanon_BFG_20260814_TEST/133626.1_2`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133923.1`) (sent_id: `deanon_BFG_20260814_TEST/133923.1_1`)


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

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/134365.1`) (sent_id: `deanon_BFG_20260814_TEST/134365.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Priv.-Doz. Timothy Oldenbüttel, Kohlreitweg 2, 4092 Winterhof, Österreich, vertreten durch EHC Wirtschaftstreuhand- gesellschaft m.b.H., Schulgasse 10, 2000  Stockerau, über die Beschwerde vom 13. April 2016 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 5. Februar 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Timothy Oldenbüttel` | `Priv.-Doz. Timothy Oldenbüttel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Kohlreitweg 2, 4092 Winterhof, Österreich` (address)
- `Finanzamtes` (organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Wieland Starnberg` | `Priv.-Doz. Wieland Starnberg` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ing. Linus Feyerherdt` (person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich` (address)
- `Christina Hildegard Stowasser` (person)
- `Finanzamtes Gänserndorf Mistelbach` (organisation)
- `Finanzamtes Österreich` (organisation)
- `98-011/6615` (tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/135969.1`) (sent_id: `deanon_BFG_20260814_TEST/135969.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Lieselotte Stiglat  in der Beschwerdesache Sibylle Roßmayr,  Sierling 20, 3632 Pernthon, Österreich, vertreten durch RSM Austria Steuerberatung GmbH, Tegetthoffstraße 7, 1010  Wien, über die Beschwerde vom 16.11.2021 gegen den Bescheid des Finanzamtes Österreich  vom 5. November 2021 betreffend Verspätungszuschlag Umsatzsteuer 4-06/2021,  Steuernummer 58-418/2406  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Lieselotte Stiglat` | `Priv.-Doz.in Lieselotte Stiglat` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Sibylle Roßmayr` (person)
- `Sierling 20, 3632 Pernthon, Österreich` (address)
- `RSM Austria Steuerberatung GmbH` (organisation)
- `Finanzamtes Österreich` (organisation)
- `58-418/2406` (tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/136592.1`) (sent_id: `deanon_BFG_20260814_TEST/136592.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dora Grobstich  in der Beschwerdesache Raul Türkkan,  Schachener Straße 122J, 3643 Nonnersdorf, Österreich, über die Beschwerde vom 10. März 2021 gegen den Bescheid des Finanzamtes  Österreich vom 4. März 2021 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 24-623/5745  zu Recht erkannt:   I. Der angefochtene Bescheid wird abgeändert.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Dora Grobstich` | `Priv.-Doz.in Dora Grobstich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Raul Türkkan` (person)
- `Schachener Straße 122J, 3643 Nonnersdorf, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `24-623/5745` (tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Christine Kralova  in der Beschwerdesache Merlin Leuprecht,  Ketten 21, 4061 Aistental, Österreich, vertreten durch Anton Fleischhacker, Goldeggasse 3/7, 1040 Wien, über die  Beschwerde vom 5. Februar 2018 gegen den Bescheid des Magistrats der Stadt Wien,  Magistratssabteilung 6,Rechnungs- und Abgabenwesen, Dezernat Abgaben und Recht, Referat  Landes- und Gemeindeabgaben vom 10. Jänner 2018 betreffend Zurückweisung eines Antrages  auf Festsetzung der Vergnügungssteuer für den Zeitraum 2012 bis 2015 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Christine Kralova` | `Priv.-Doz.in Christine Kralova` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Merlin Leuprecht` (person)
- `Ketten 21, 4061 Aistental, Österreich` (address)
- `Anton Fleischhacker` (person)
- `Magistrats der Stadt Wien` (organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/137504.1`) (sent_id: `deanon_BFG_20260814_TEST/137504.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Klaus Gerwarth  in der Beschwerdesache  ÖkR Reneé Utzmeier, Chimanigasse 6, 8312 Ottendorf an der Rittschein, Österreich, über die Beschwerde vom 28. April 2021 gegen den Bescheid des  Finanzamtes Österreich vom 19. April 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Klaus Gerwarth` | `Priv.-Doz. Klaus Gerwarth` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `ÖkR Reneé Utzmeier` (person)
- `Chimanigasse 6, 8312 Ottendorf an der Rittschein, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/137635.1`) (sent_id: `deanon_BFG_20260814_TEST/137635.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Valerius Frühmark  in der Beschwerdesache Hon.-Prof. Sven Corbin,  Stalderhaus 7, 9363 Feistritz, Österreich, über die Beschwerde vom 23. Juli 2021 gegen den Bescheid des Finanzamtes  Österreich vom 5. Juli 2021 betreffend Rückforderung von Familienbeihilfe und  Kinderabsetzbeträgen für den Zeitraum Juni 2018 bis Jänner 2019, SVNr [SVNR],  zu Recht erkannt:  I.  Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Valerius Frühmark` | `Priv.-Doz. Valerius Frühmark` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Sven Corbin` (person)
- `Stalderhaus 7, 9363 Feistritz, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/138362.1`) (sent_id: `deanon_BFG_20260814_TEST/138362.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Stephanie Dauben  in der Beschwerdesache MedR Erhard Hauprich,  Wohnpark Ager 97, 8264 Obgrün, Österreich, über die Beschwerde vom 22. Juni 2020 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer zu Recht erkannt:   I. Der Beschwerde wird Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Stephanie Dauben` | `Priv.-Doz.in Stephanie Dauben` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `MedR Erhard Hauprich` (person)
- `Wohnpark Ager 97, 8264 Obgrün, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/138437.1`) (sent_id: `deanon_BFG_20260814_TEST/138437.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Bettina Füsslin  in der Beschwerdesache Univ.-Prof.in Anastasia Sebott,  Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich, vertreten durch Mag. jur.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Bettina Füsslin` | `Priv.-Doz.in Bettina Füsslin` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Univ.-Prof.in Anastasia Sebott` (person)
- `Obere Burggräflergasse 220P, 5242 Grubmühl, Österreich` (address)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Olivia Severien  in der Beschwerdesache  Denis Öztopal, Weidenbachstraße 3, 5131 Pimbach, Österreich, vertreten durch Pschera Steuerberatung GmbH, Gösser Straße 60,  8700 Leoben, über die Beschwerde vom 20. November 2013 gegen die zur Steuernummer 68- 060/6613 ergangenen Bescheide des Finanzamt Salzburg-Stadt (nun Dienststelle des Finanzamtes Österreich)  vom 22. Oktober 2013 betreffend Umsatz- und Einkommensteuer 2000  – 2010 zu Recht  erkannt:   I. Die Berufung/Beschwerde vom 20. Nov.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Olivia Severien` | `Priv.-Doz.in Olivia Severien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Denis Öztopal` (person)
- `Weidenbachstraße 3, 5131 Pimbach, Österreich` (address)
- `Pschera Steuerberatung GmbH` (organisation)
- `Finanzamt Salzburg-Stadt` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dietlind Döbereiner  in der Beschwerdesache Siegbert Ptasnik,  Kleinseeweg 4, 6341 Ebbs, Österreich, über die Beschwerden vom 25. September 2015 gegen die Bescheide des  Finanzamtes Linz vom 20. August 2015 betreffend Einkommensteuer 2009 - 2014 und  Umsatzsteuer 2009 - 2014 sowie Einkommen- und Umsatzsteuerbescheid 2015 jeweils vom  19.07.2017 und Einkommen –und Umsatzsteuerbescheid 2016 vom 20.07.2017 zu Recht  erkannt:   I. Die Beschwerden gegen die Einkommensteuerbescheide 2009, 2010, 2011, 2015 sowie  gegen die Umsatzsteuerbescheide 2009-2016 werden gemäß § 279 BAO als unbegründet  abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Dietlind Döbereiner` | `Priv.-Doz.in Dietlind Döbereiner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Siegbert Ptasnik` (person)
- `Kleinseeweg 4, 6341 Ebbs, Österreich` (address)
- `Finanzamtes Linz` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Olivia Rodenbach  in der Beschwerdesache Veit Dworatzeck,  Zehentberg 7, 4060 Rufling, Österreich, vertreten durch Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Mariatroster Straße 36, 8043 Graz, über die Beschwerde vom  24. Mai 2011 gegen den Bescheid des Finanzamtes Österreich vom 19. April 2011 betreffend  Einkommensteuer 2009 Steuernummer 82-692/9441  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Olivia Rodenbach` | `Priv.-Doz.in Olivia Rodenbach` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Veit Dworatzeck` (person)
- `Zehentberg 7, 4060 Rufling, Österreich` (address)
- `Kanzlei Kiffmann KG Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes Österreich` (organisation)
- `82-692/9441` (tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/139653.1`) (sent_id: `deanon_BFG_20260814_TEST/139653.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Fridolin Zielke  in der Beschwerdesache Monika Tomm,  Mitteredt 3, 4776 Dobl, Österreich, betreffend Beschwerden vom 7. April 2022 gegen die Bescheide des  Finanzamtes Österreich vom 8. Juli 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2018, Einkommensteuer (Arbeitnehmerveranlagung) 2019 und  Einkommensteuer (Arbeitnehmerveranlagung) 2020, Steuernummer 98-832/4427, den  Beschluss:  I. Die Beschwerden werden als nicht fristgerecht eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Fridolin Zielke` | `Priv.-Doz. Fridolin Zielke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Monika Tomm` (person)
- `Mitteredt 3, 4776 Dobl, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `98-832/4427` (tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Imre Zeitner  in der Beschwerdesache des  Daisy Schlimme, Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich, vertreten durch Henning & Partner Steuerberatung GmbH,  Brockmanngasse 75, 8010 Graz, sowie durch Dr. Michael Kotschnigg, Franzensbrückenstraße 5,  1020 Wien, über die Beschwerde vom 15. Jänner 2016 gegen die Bescheide des Finanzamtes  Graz-Umgebung (nunmehr: Finanzamt Österreich) vom 9. Dezember 2015 betreffend   1) Wiederaufnahme der Verfahren hinsichtlich Umsatzsteuer 2009 bis 2011 sowie  2) Einkommensteuer und Umsatzsteuer je 2009 bis 2014   den BESCHLUSS gefasst:   I. Die angefochtenen Bescheide (sowie die bezüglichen Beschwerdevorentscheidungen)  werden gemäß § 278 Abs. 1 BAO unter Zurückverweisung der Sache an die Abgabenbehörde  aufgehoben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Imre Zeitner` | `Priv.-Doz. Imre Zeitner` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Daisy Schlimme` (person)
- `Schupfenhäuslweg 53, 8200 Fünfing bei Gleisdorf, Österreich` (address)
- `Henning & Partner Steuerberatung GmbH` (organisation)
- `Dr. Michael Kotschnigg` (person)
- `Finanzamtes  Graz-Umgebung` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/139958.1`) (sent_id: `deanon_BFG_20260814_TEST/139958.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Angelika Sczesni  in der Beschwerdesache Desiree Pillsticker,  Georg-Schicht-Platz 191, 4284 Stranzberg, Österreich, über die Beschwerde vom 4. Juni 2021 gegen den Bescheid des Finanzamtes  Österreich vom 21. Mai 2021 betreffend Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbetrag für den Zeitraum März 2020 bis März 2021,  Ordnungsbegriff Nr123, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Angelika Sczesni` | `Priv.-Doz.in Angelika Sczesni` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Desiree Pillsticker` (person)
- `Georg-Schicht-Platz 191, 4284 Stranzberg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Janet Köhle  in der Beschwerdesache der  Textil Bermon, Hans-Bachmann-Straße 4, 2872 Langegg, Österreich  vertreten durch RA-Vertreter, über die Beschwerde vom 31. Mai  2017 gegen die zur Steuernummer 91-124/4580  ergangenen Bescheide des FA St. Johann Tamsweg Zell am See (jetzt  Dienststelle des Finanzamtes Österreich) vom 30. März 2017 betreffend  Einkommensteuer 2009 – 2014 nach Durchführung einer mündlichen Verhandlung am  15.März 2023 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Janet Köhle` | `Priv.-Doz.in Janet Köhle` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `Textil Bermon` (organisation)
- `Hans-Bachmann-Straße 4, 2872 Langegg, Österreich` (address)
- `91-124/4580` (tax_number)
- `FA St. Johann Tamsweg Zell am See` (organisation)
- `Finanzamtes Österreich` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter als Vorsitzende, die  Richterin Mag. Andrea Proidl als beisitzende Richterin sowie Mag. Martin Saringer und Mag.  Harald  Zeller als fachkundige Laienrichter in der Beschwerdesache Priv.-Doz.in Diana Pöppel, Spitalbergweg 20, 4775 Wagholming, Österreich,  vertreten durch Baldinger & Partner Unternehmens- und Steuerberatung GmbH, Ferrogasse  35, 1180 Wien, über die Beschwerde vom 9. September 2017 gegen die Bescheide des  Finanzamtes Wien 4/5/10 vom 17. Juli 2017 betreffend Umsatzsteuer 2010-2016,  Steuernummer 56-661/5349, nach Durchführung einer mündlichen Verhandlung am 9. Juni  2023 in Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Diana Pöppel` | `Priv.-Doz.in Diana Pöppel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Judith Leodolter` (person)
- `Mag. Andrea Proidl` (person)
- `Mag. Martin Saringer` (person)
- `Mag.  Harald  Zeller` (person)
- `Spitalbergweg 20, 4775 Wagholming, Österreich` (address)
- `Baldinger & Partner Unternehmens- und Steuerberatung GmbH` (organisation)
- `Finanzamtes Wien 4/5/10` (organisation)
- `56-661/5349` (tax_number)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/142826.1`) (sent_id: `deanon_BFG_20260814_TEST/142826.1_2`)


Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Bodo Bookhold  in der Beschwerdesache Samuel Haßelbarth,  Zeilberg 4, 3233 Bühren, Österreich, über die Beschwerde vom 02.06.2021 gegen den Bescheid des Finanzamtes  Österreich vom 28.05.2021, betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2020 zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Bodo Bookhold` | `Priv.-Doz. Bodo Bookhold` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Samuel Haßelbarth` (person)
- `Zeilberg 4, 3233 Bühren, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rita Wiersbicki  in der Beschwerdesache Corvin Billmaier,  Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich, vertreten durch Mag. Aleksandar Hofstätter, Johann-Strauß-Gasse 4-6//2/5,  1040 Wien, betreffend Beschwerde vom 10. Juli 2023 gegen den Bescheid des Finanzamtes  Österreich vom 2. September 2022 betreffend Einkommensteuer 2021 Steuernummer  23-971/7442  beschlossen:   Die Beschwerde vom 10. Juli 2023 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a  BAO als nicht rechtzeitig eingebracht zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Rita Wiersbicki` | `Priv.-Doz.in Rita Wiersbicki` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Corvin Billmaier` (person)
- `Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich` (address)
- `Mag. Aleksandar Hofstätter` (person)
- `Finanzamtes  Österreich` (organisation)
- `23-971/7442` (tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden A und die Richterin   Priv.-Doz.in Annkathrin Czesielski  sowie die fachkundigen Laienrichter B und C in der Beschwerdesache Prof.in Esra Konwischer,  Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 11. August 2016 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich)  vom 25. Juli 2016, ErfNr u.a., betreffend   1. Festsetzung der Gebühren gemäß § 14 TP 6 Abs. 2 Z 1, TP 2 Abs. 1 Z 1, TP 5 Abs. 1 und        TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:   Die Beschwerde wird insgesamt als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Annkathrin Czesielski` | `Priv.-Doz.in Annkathrin Czesielski` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Prof.in Esra Konwischer` (person)
- `Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich` (address)
- `Finanzamtes für Gebühren` (organisation)
- `Finanzamt Österreich` (organisation)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Jessica Buddeus  in der Beschwerdesache Heidemarie Helwig,  Schmittengasse 288, 3160 Maierhöfen, Österreich, vertreten durch Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH, Teinfaltstraße 8-8A Tür 5.01, 1010 Wien, über die Beschwerde vom 7. Februar 2024  gegen den Bescheid des FA Purkersdorf  vom 10. Jänner 2024 betreffend Abweisung eines Antrages  auf bescheidmäßige Festsetzung des Energiekrisenbeitrag-Strom (EKB-S) für den Zeitraum  01.12.2022 bis 30.06.2023, Steuernummer 81-530/8966, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Jessica Buddeus` | `Priv.-Doz.in Jessica Buddeus` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heidemarie Helwig` (person)
- `Schmittengasse 288, 3160 Maierhöfen, Österreich` (address)
- `Zacherl Schallaböck Proksch Manak Kraft Rechtsanwälte  GmbH` (organisation)
- `FA Purkersdorf` (organisation)
- `81-530/8966` (tax_number)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/144676.1`) (sent_id: `deanon_BFG_20260814_TEST/144676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Priv.-Doz. Diego Celler  in der Beschwerdesache  Lena Dworaczyk, Johann Degen-Gasse 173, 2821 Ofenbach, Österreich, vertreten durch CERHA HEMPEL Rechtsanwälte GmbH, Parkring 2,  1010 Wien über die Beschwerde vom 17. Jänner 2024 gegen den Bescheid des Finanzamtes für  Großbetriebe vom 18. Dezember 2023 betreffend Festsetzung Energiekrisenbeitrag-Strom für  den Zeitraum Dezember 2022 bis Juni 2023 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Diego Celler` | `Priv.-Doz. Diego Celler` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Lena Dworaczyk` (person)
- `Johann Degen-Gasse 173, 2821 Ofenbach, Österreich` (address)
- `CERHA HEMPEL Rechtsanwälte GmbH` (organisation)
- `Finanzamtes für  Großbetriebe` (organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/145674.1`) (sent_id: `deanon_BFG_20260814_TEST/145674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Vivian Gastell  in der Beschwerdesache Dipl.-Ing. Tosca Toussaint,  Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 25. Mai 2023 betreffend Abweisung des Antrags vom 6. Februar 2023 auf  Erstattung des Mehrkindzuschlages auf Grund der  Verhältnisse des Jahres 2022,  Steuernummer 82-564/6636, SV-Nr. Nr., zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO stattgegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Vivian Gastell` | `Priv.-Doz.in Vivian Gastell` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dipl.-Ing. Tosca Toussaint` (person)
- `Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `82-564/6636` (tax_number)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_1`)


BESCHLUSS  Das Bundesfinanzgericht (BFG) hat durch die Richterin Priv.-Doz.in Gertrude Ortwich  in der Beschwerdesache des  RgR Florens Netzer, Furrach 6, 2184 Prinzendorf an der Zaya, Österreich, betreffend die Beschwerde vom 9. September 2021 gegen den zur  Steuernummer 34-436/7126  ergangenen Bescheid des FA Oststeiermark  vom 10. August 2021  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 beschlossen:  Der angefochtene Bescheid vom 10. August 2021 und die Beschwerdevorentscheidung vom  15. November 2021 werden gemäß § 278 Abs. 1 BAO aufgehoben und die Sache an die  Abgabenbehörde zur Erledigung zurückverwiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Gertrude Ortwich` | `Priv.-Doz.in Gertrude Ortwich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht (BFG)` (organisation)
- `RgR Florens Netzer` (person)
- `Furrach 6, 2184 Prinzendorf an der Zaya, Österreich` (address)
- `34-436/7126` (tax_number)
- `FA Oststeiermark` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/146295.1`) (sent_id: `deanon_BFG_20260814_TEST/146295.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Guntram Grüber  in der Beschwerdesache Scarlett Preuszler,  Sperlgasse 38, 8720 Rattenberg, Österreich, über die Beschwerde vom 6. Dezember 2023 gegen den Bescheid des  Finanzamtes Österreich vom 15. November 2023 betreffend Beschwerdezinsen (§ 205a BAO)  Steuernummer 78-889/2133  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Guntram Grüber` | `Priv.-Doz. Guntram Grüber` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Scarlett Preuszler` (person)
- `Sperlgasse 38, 8720 Rattenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `78-889/2133` (tax_number)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/146548.1`) (sent_id: `deanon_BFG_20260814_TEST/146548.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Hagen Atar  in der Beschwerdesache Priv.-Doz.in Laura Fromader,  Oberpetersdorf 6, 4871 Egg, Österreich, über die Beschwerde vom 13. Dezember 2022 gegen den Bescheid des  FA Wien 2/20/21/22  vom 6. Dezember 2022 betreffend den Bescheid über die Abweisung des Antrags auf  Aufhebung des Einkommensteuerbescheides 2020 gem § 299 BAO zur Steuernummer  60-848/5470  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Laura Fromader` | `Priv.-Doz.in Laura Fromader` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Hagen Atar` (person)
- `Oberpetersdorf 6, 4871 Egg, Österreich` (address)
- `FA Wien 2/20/21/22` (organisation)
- `60-848/5470` (tax_number)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/147381.1`) (sent_id: `deanon_BFG_20260814_TEST/147381.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Otto Mielniczek  in der Beschwerdesache Wendelin Deutschlender,  Altes Stampfhäusel 64, 2130 Kettlasbrunn, Österreich, gegen   a) die von der belangten Behörde Finanzamt Österreich zu Steuernummer 04-271/3224  am 18. Dezember 2019 ausgefertigten Bescheide über die Wiederaufnahme des  Verfahrens betreffend Umsatzsteuer für die Jahre 2014 bis 2016,  b) die von der belangten Behörde Finanzamt Österreich zu Steuernummer 04-271/3224  am 18. Dezember 2019 ausgefertigten Bescheide über die Wiederaufnahme des  Verfahrens betreffend Einkommensteuer für die Jahre 2014 bis 2016,  c) den von der belangten Behörde Finanzamt Österreich zu Steuernummer 04-271/3224  am 18. Dezember 2019 ausgefertigten Bescheid über die Aufhebung des  Umsatzsteuerbescheides 2017,  d) den von der belangten Behörde Finanzamt Österreich zu Steuernummer 04-271/3224  am 18. Dezember 2019 ausgefertigten Bescheid über die Aufhebung des  Einkommensteuerbescheides 2017,  e) die von der belangten Behörde Finanzamt Österreich zu Steuernummer 04-271/3224  am 18. Dezember 2019 ausgefertigten Bescheide betreffend Umsatzsteuer für die Jahre  2014 bis 2017,  f) die von der belangten Behörde Finanzamt Österreich zu Steuernummer 04-271/3224  am 18. Dezember 2019 ausgefertigten Bescheide betreffend Einkommensteuer für die  Jahre 2014 bis 2017 und  g) die von der belangten Behörde Finanzamt Österreich zu Steuernummer 04-271/3224  am 18. Dezember 2019 ausgefertigten Bescheide über die Festsetzung von  Anspruchszinsen für die Jahre 2014 und 2015  I. zu Recht erkannt:  1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Otto Mielniczek` | `Priv.-Doz. Otto Mielniczek` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Wendelin Deutschlender` (person)
- `Altes Stampfhäusel 64, 2130 Kettlasbrunn, Österreich` (address)
- `Finanzamt Österreich` (organisation)
- `04-271/3224` (tax_number)
- `Finanzamt Österreich` (organisation)
- `04-271/3224` (tax_number)
- `Finanzamt Österreich` (organisation)
- `04-271/3224` (tax_number)
- `Finanzamt Österreich` (organisation)
- `04-271/3224` (tax_number)
- `Finanzamt Österreich` (organisation)
- `04-271/3224` (tax_number)
- `Finanzamt Österreich` (organisation)
- `04-271/3224` (tax_number)
- `Finanzamt Österreich` (organisation)
- `04-271/3224` (tax_number)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/148316.1`) (sent_id: `deanon_BFG_20260814_TEST/148316.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Elfriede Gehbauer  in der Beschwerdesache Ines Linzenich,  Kriechbaumweg 19, 4912 Wiesen, Österreich, vertreten durch Raiffeisenlandesbank Kärnten - Rechenzentrum und  Revisionsverband, reg. Gen.m.b.H., Raiffeisenplatz 1, 9020 Klagenfurt/Wörthersee, über die  Beschwerde vom 21. Oktober 2024 gegen die Bescheide des Finanzamtes Österreich vom  3. Oktober 2024 über die Festsetzung eines Verspätungszuschlages betreffend Abgabe einer  Zusammenfassenden Meldung für die Zeiträume 09/2022, 10/2022, 02/2023 und 05/2023,  Steuernummer 53-564/3503, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Elfriede Gehbauer` | `Priv.-Doz.in Elfriede Gehbauer` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Ines Linzenich` (person)
- `Kriechbaumweg 19, 4912 Wiesen, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `53-564/3503` (tax_number)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/148486.1`) (sent_id: `deanon_BFG_20260814_TEST/148486.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Sandro Stoeckicht  über die Beschwerde des Zeno Bauermann,  Oisreitl 3, 9570 Rappitsch, Österreich  vom 11. April 2025, gegen das Straferkenntnis der belangten Behörde  Magistrat der Stadt Wien, Magistratsabteilung 67, als Abgabenstrafbehörde, vom 31. März  2025, GZ. MA67/GZ1/2024, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:   I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Sandro Stoeckicht` | `Priv.-Doz. Sandro Stoeckicht` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Zeno Bauermann` (person)
- `Oisreitl 3, 9570 Rappitsch, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/148482.1`) (sent_id: `deanon_BFG_20260814_TEST/148482.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Julian Stollenmeier  in der Beschwerdesache Liu Grahlow,  Greithbachweg 105U, 4153 Berging, Österreich, über die Beschwerde vom 23. Februar 2025 gegen den Bescheid des  Finanzamtes Österreich vom 23. Jänner 2025 betreffend Rückforderung von Familienbeihilfe  und Kinderabsetzbetrag für den Zeitraum Juni 2022 bis Februar 2023, Steuernummer 25-700/2352 (SVNR 2338 010446), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz. Julian Stollenmeier` | `Priv.-Doz. Julian Stollenmeier` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Liu Grahlow` (person)
- `Greithbachweg 105U, 4153 Berging, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `25-700/2352` (tax_number)
- `2338 010446` (social_security_number)

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/149310.1`) (sent_id: `deanon_BFG_20260814_TEST/149310.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Beate Gützlaf  in der Beschwerdesache Priv.-Doz.in Alina Vriesman,  Willing 25N, 2561 Pöllau, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 16. Mai 2023, Ordnungsbegriff Nr1, betreffend Abweisung des Antrages auf  Familienbeihilfe für den Zeitraum „April 2023 – September 2023“ zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Priv.-Doz.in Alina Vriesman` | `Priv.-Doz.in Alina Vriesman` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.a Beate Gützlaf` (person)
- `Willing 25N, 2561 Pöllau, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129375.1`) (sent_id: `deanon_BFG_20260814_TEST/129375.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Livia Korowski  in der Beschwerdesache Sven Mitterhuber,  Oberwiesenweg 16, 8130 Schönau, Österreich, vertreten durch Rechtsanwalt, über die Beschwerde vom 4. September 2015  gegen die Bescheide des Finanzamtes Landeck Reutte vom 6. August 2015, StrNr, betreffend  1. Normverbrauchsabgabe für den Zeitraum 05/2014;

**False Positives:**

- `Priv.-Doz.in Mag` — partial — pred is substring of gold: `Priv.-Doz.in Mag.a Livia Korowski`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Livia Korowski`(person)
- `Sven Mitterhuber`(person)
- `Oberwiesenweg 16, 8130 Schönau, Österreich`(address)
- `Finanzamtes Landeck Reutte`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/137167.1`) (sent_id: `deanon_BFG_20260814_TEST/137167.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Frederik von Gruber  in der Beschwerdesache Laila Klimenkow,  Abt Zedinek Straße 2, 9345 Kaindorf, Österreich, vertreten durch Causa Wirtschaftstreuhand GmbH, Türkenstrasse 25/8, 1090  Wien, wegen Verletzung der Entscheidungspflicht des Finanzamtes Österreich in einer  Angelegenheit betreffend Einkommen- und Umsatzsteuer 2020 den Beschluss:  I. Die Säumnisbeschwerde wird gemäß § 284 Abs. 7 lit. b BAO iVm § 260 Abs. 1 lit. a  BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Priv.-Doz. Frederik` — partial — pred is substring of gold: `Priv.-Doz. Frederik von Gruber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Frederik von Gruber`(person)
- `Laila Klimenkow`(person)
- `Abt Zedinek Straße 2, 9345 Kaindorf, Österreich`(address)
- `Causa Wirtschaftstreuhand GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_56`)


Die von Herrn Ing. Priv.-Doz.in Linda Schleglmilch zu Punkt 4 und 5 gemachten Angaben stellen für die Betriebsprüfung keine  zu akzeptierenden Argumente dar.

**False Positives:**

- `Priv.-Doz.in Linda Schleglmilch` — partial — pred is substring of gold: `Ing. Priv.-Doz.in Linda Schleglmilch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing. Priv.-Doz.in Linda Schleglmilch`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138893.1`) (sent_id: `deanon_BFG_20260814_TEST/138893.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr  in der Beschwerdesache Hon.-Prof.in Techn R Huberta Pauwels,  Oberapping 6, 4613 Unterholz, Österreich, betreffend Beschwerde vom 14. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 hinsichtlich Einkommensteuer  (Arbeitnehmerveranlagung) 2020, Steuernummer 76-699/8954, beschlossen:  Der Vorlageantrag wird gemäß § 264 Abs. 4 lit. e BAO iVm § 260 Abs. 1 lit. b BAO als nicht  fristgerecht eingebracht zurückgewiesen.

**False Positives:**

- `Priv.-Doz.in Waltraud Süßmayr` — partial — pred is substring of gold: `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Mag.a Priv.-Doz.in Waltraud Süßmayr`(person)
- `Hon.-Prof.in Techn R Huberta Pauwels`(person)
- `Oberapping 6, 4613 Unterholz, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `76-699/8954`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/139843.1`) (sent_id: `deanon_BFG_20260814_TEST/139843.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Priv.-Doz. Andreas Domingo  in der Beschwerdesache Univ.-Prof.in KzlR Tiffany Nowakowsky,  Thumastraße 13, 5201 Brunn, Österreich, vertreten durch "ÖBUG" DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, St.-Veit-Gasse 8, 1130 Wien, über die  Beschwerde vom 14. April 2020 gegen den Bescheid des Finanzamtes Wien 1/23 vom 2. März  2020 betreffend die Abweisung eines Zahlungserleichterungsansuchens, Steuernummer  75-144/0441, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz. Andreas Domingo` — partial — pred is substring of gold: `Mag. Priv.-Doz. Andreas Domingo`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Priv.-Doz. Andreas Domingo`(person)
- `Univ.-Prof.in KzlR Tiffany Nowakowsky`(person)
- `Thumastraße 13, 5201 Brunn, Österreich`(address)
- `DR. NIKOLAUS Wirtschaftstreuhand GmbH -  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `75-144/0441`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_14`)


Das Finanzamt Österreich begründete diese Vorgehensweise dergestalt, dass der  Familienbonus Plus für das Kind OStR Priv.-Doz. Theodor Voelpel  hinsichtlich der Monate September bis  Dezember sowie für das Kind Herbert Schaffarik  hinsichtlich der Monate August bis Dezember  zustehe.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Finanzamt Österreich`(organisation)
- `OStR Priv.-Doz. Theodor Voelpel`(person)
- `Herbert Schaffarik`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_20`)


Der zweite Sohn,  OStR Priv.-Doz. Theodor Voelpel, sei beim Beschwerdeführer und sei er daher auch Alleinerzieher.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_22`)


Festgestellt Sachverhalt   Der Beschwerdeführer ist Vater von OStR Priv.-Doz. Theodor Voelpel  und Herbert Schaffarik  und lebte dieser im Jahr  2020 bis zum 08. Jänner mit der Mutter der beiden Söhne, mit der der Beschwerdeführer auch  verheiratet war, sowie den beiden Kindern in einem gemeinsamen Haushalt. Am 08. Jänner zog  die Mutter zusammen mit dem Sohn Herbert Schaffarik  aus dem gemeinsamen Haushalt aus.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)
- `Herbert Schaffarik`(person)
- `Herbert Schaffarik`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_23`)


Der  Sohn OStR Priv.-Doz. Theodor Voelpel  verblieb im Haushalt des Beschwerdeführers.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_27`)


In Bezug auf das Kind OStR Priv.-Doz. Theodor Voelpel  bezog im Jahr 2020 die Mutter von Jänner bis August sowie  der Beschwerdeführer von September bis Dezember die Familienbeihilfe.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_28`)


Die Mutter der beiden Kinder machte im Rahmen ihrer Steuererklärung vom 03. März 2021  weder den Familienbonus Plus für das Kind OStR Priv.-Doz. Theodor Voelpel  noch für das Kind Herbert Schaffarik  geltend.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)
- `Herbert Schaffarik`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_95`)


Diese Voraussetzungen erfüllt der  Beschwerdeführer im vorliegenden Fall in Bezug auf den Sohn OStR Priv.-Doz. Theodor Voelpel, da der  Beschwerdeführer zum einen im Jahr 2020 durch den Auszug der ehemaligen Ehefrau am 08.  Jänner nicht mehr als sechs Monate in einer Gemeinschaft mit einem (Ehe)Partner gelebt hat.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_96`)


Zum anderen ist der Sohn OStR Priv.-Doz. Theodor Voelpel  als Kind im Sinne des § 106 Abs. 1 EStG 1988  anzusehen, wiewohl es zutrifft, dass dem Beschwerdeführer der Kinderabsetzbetrag im  Kalenderjahr 2020 infolge seines Bezugs von Familienbeihilfe für dieses Kind im Zeitraum  September bis Dezember nur für diese vier Monate zusteht.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_97`)


Dieser Umstand bedingt allerdings  nicht, dass der Sohn OStR Priv.-Doz. Theodor Voelpel  nicht als Kind im Sinne des § 106 Abs. 1 EStG 1988 gilt. § 106  Abs. 1 EStG 1988 fordert nämlich, dass entweder dem Steuerpflichtigen oder seinem (Ehe- )Partner (Abs. 3) mehr als sechs Monate im Kalenderjahr der Kinderabsetzbetrag nach § 33  Abs. 3 EStG 1988 zusteht, um von einem Kind im Sinne dieser Bestimmung sprechen zu  können.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_98`)


Wie dem Sachverhalt entnommen werden kann, war der Beschwerdeführer im Jahr  2020 von Jänner bis August mit der Mutter des Sohnes OStR Priv.-Doz. Theodor Voelpel  verheiratet und ist folglich  ebenjene diesen sechs Monate überschreitenden Zeitraum betreffend als (Ehe-)Partnerin des  Beschwerdeführers im Sinne des § 106 Abs. 3 EStG 1988 anzusehen.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_99`)


Da die Mutter für diesen  Zeitraum die Familienbeihilfe hinsichtlich den Sohn OStR Priv.-Doz. Theodor Voelpel  bezog, stand ihr als (Ehe- )Partnerin des Beschwerdeführers im Jahr 2020 für mehr als sechs Monate der  Kinderabsetzbetrag nach § 33 Abs. 3 EStG 1988 zu und ist aus diesem Grund der Sohn  OStR Priv.-Doz. Theodor Voelpel  auch aus der Sicht des Beschwerdeführers als Kind im Sinne des § 106 Abs. 1 EStG  1988 anzusehen.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`
- `Priv.-Doz. Theodor Voelpel` — similar text (different position): `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)
- `OStR Priv.-Doz. Theodor Voelpel`(person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_100`)


An dieser Beurteilung vermag auch der Umstand, dass der Mutter des Sohnes OStR Priv.-Doz. Theodor Voelpel  der  Alleinerzieherabsetzbetrag für diesen Sohn im Rahmen der Veranlagung des Kalenderjahres  2020 gewährt wurde, nichts ändern, erweist sich doch angesichts des festgestellten  Sachverhalts die Gewährung des Alleinerzieherabsetzbetrages gegenüber Mutter als  rechtsunrichtig, da ja der Sohn OStR Priv.-Doz. Theodor Voelpel  beim Vater verblieben ist und die Mutter somit  nicht mehr als sechs Monate im Jahr 2020 mit diesem Sohn in einer Gemeinschaft gelebt hat.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`
- `Priv.-Doz. Theodor Voelpel` — similar text (different position): `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)
- `OStR Priv.-Doz. Theodor Voelpel`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/140014.1`) (sent_id: `deanon_BFG_20260814_TEST/140014.1_107`)


In Bezug auf den Sohn OStR Priv.-Doz. Theodor Voelpel  gilt es sodann auszuführen, dass dieser nach dem Auszug  der Mutter am 08. Jänner 2020 im Haushalt des Beschwerdeführers verblieben ist.

**False Positives:**

- `Priv.-Doz. Theodor Voelpel` — partial — pred is substring of gold: `OStR Priv.-Doz. Theodor Voelpel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `OStR Priv.-Doz. Theodor Voelpel`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/144714.1`) (sent_id: `deanon_BFG_20260814_TEST/144714.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Mag.a Tamara Sokol  in der Beschwerdesache der  Heinrich Heckt, Manhartsbergstraße 16, 2326 Maria-Lanzendorf, Österreich, über die Beschwerde vom 19. September 2022 gegen den  Bescheid des Finanzamt Freistadt Rohrbach Urfahr  vom 23. August 2022 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2020 zu Steuernummer 87-623/8682  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Priv.-Doz.in Mag` — partial — pred is substring of gold: `Priv.-Doz.in Mag.a Tamara Sokol`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Mag.a Tamara Sokol`(person)
- `Heinrich Heckt`(organisation)
- `Manhartsbergstraße 16, 2326 Maria-Lanzendorf, Österreich`(address)
- `Finanzamt Freistadt Rohrbach Urfahr`(organisation)
- `87-623/8682`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/146743.1`) (sent_id: `deanon_BFG_20260814_TEST/146743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Priv.-Doz. Priv.-Doz. Urs Heinatzky, Feldpichl 19, 8130 Peggau, Österreich, vertreten durch Mag. Beatrix Anna Elfriede  Reiff-Zehetner, Straße der Menschenrechte 11, 2103 Langenzersdorf, über die Beschwerde  vom 30. August 2023 gegen den Bescheid des Finanzamtes Österreich vom 31. Juli 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 zur Steuernummer  51-583/1758  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Priv.-Doz. Priv` — partial — pred is substring of gold: `Priv.-Doz. Priv.-Doz. Urs Heinatzky`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Priv.-Doz. Priv.-Doz. Urs Heinatzky`(person)
- `Feldpichl 19, 8130 Peggau, Österreich`(address)
- `Mag. Beatrix Anna Elfriede  Reiff-Zehetner`(person)
- `Finanzamtes Österreich`(organisation)
- `51-583/1758`(tax_number)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/147471.1`) (sent_id: `deanon_BFG_20260814_TEST/147471.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Detlev Bauerhansl  in der Beschwerdesache des  ÖkR Priv.-Doz.in Sophie Volkenandt, Bahnhofplatz 6, 3372 Ferschnitz, Österreich, über   1) die Beschwerde vom 28. Februar 2019 gegen die Bescheide des Finanzamtes Graz- Umgebung (nunmehr: Finanzamt Österreich) vom 13. Dezember 2018 betreffend  Wiederaufnahme des Verfahrens (hinsichtlich Einkommensteuer 2008), Einkommensteuer  und Anspruchszinsen je 2008 sowie   2) die Beschwerde vom 29. Juli 2019 gegen die Bescheide des Finanzamtes Graz-Umgebung  (Finanzamt Österreich) vom 27. Juni 2019 betreffend Einkommensteuer und Anspruchszinsen  je 2009 bis 2013, Steuernummer 35-829/3184,   I. den Beschluss gefasst:  Die Beschwerde gegen den Bescheid vom 13. Dezember 2018 betreffend Wiederaufnahme  hinsichtlich Einkommensteuer 2008 wird zurückgewiesen.

**False Positives:**

- `Priv.-Doz.in Sophie Volkenandt` — partial — pred is substring of gold: `ÖkR Priv.-Doz.in Sophie Volkenandt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Detlev Bauerhansl`(person)
- `ÖkR Priv.-Doz.in Sophie Volkenandt`(person)
- `Bahnhofplatz 6, 3372 Ferschnitz, Österreich`(address)
- `Finanzamtes`(organisation)
- `Finanzamt Österreich`(organisation)
- `Finanzamtes Graz`(organisation)
- `Finanzamt Österreich`(organisation)
- `35-829/3184`(tax_number)

</details>

---

## `Herr_Frau_Name_Context` 🏆

**F1:** 0.077 | **Precision:** 0.623 | **Recall:** 0.041  

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
| 0.623 | 0.041 | 0.077 | 106 | 66 | 40 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 66 | 40 | 1548 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_8`)


Frau Basyurt erzielt selber keinerlei Einkünfte, auch keine (ausländischen) Kapitaleinkünfte.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_12`)


Der Familienwohnsitz ist in A1.  Pkw:Frau Basyurt benützt den Range Rover Sport, s. beiliegenden Zulassungsschein, dieser steht ihr  tagtäglich zur Verfügung.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_14`)


Frau Basyurt wurde darauf hingewiesen, dass der Pkw innerhalb der nächsten 3 Wochen in  Österreich angemeldet wird;

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_61`)


c) "Info-Schreiben" des Finanzamtes vom 4.11.2010, woraus hervorgeht:  "…Frau Basyurt hat am 27.7.2010 im FA vorgesprochen und machte folgende Angaben: s.  beiliegende Kopie der Niederschrift.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)


- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau Basyurt tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau Basyurt das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

| Predicted | Gold |
|---|---|
| `Basyurt` | `Basyurt` |
| `Basyurt` | `Basyurt` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_132`)


Ich war schon bei Frau Beerenbrock  da wurde mir gesagt, ich  brauche keine Befunde.

| Predicted | Gold |
|---|---|
| `Beerenbrock` | `Beerenbrock` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_40`)


Sie werden daher unter Hinweis auf Ihre Mitwirkungspﬂicht im Verwaltungsstrafverfahren,  binnen zwei Wochen ab Zustellung dieses Schreibens, aufgefordert, bekannt zu geben, wie  lange sich Herr Vera Schliephacke in Wien aufgehalten, wo er gewohnt hat und zu welchem Zweck  ihm das verfahrensgegenständliche Fahrzeug überlassen war.

| Predicted | Gold |
|---|---|
| `Vera Schliephacke` | `Vera Schliephacke` |

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_60`)


Auch gibt die Tante des Beschwerdeführers,Frau Freßdorf  an, dass sich  mit Beginn des Studiums zunehmend gegenüber seiner Umwelt verschloss und sich immer  4 von 21 Seite 5 von 21

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_63`)


Zur Untersuchung beim Bundessozialamt wurde der Beschwerdeführer von Frau Unverdroß  einer  Betreuerin der Einrichtung, in welcher der Beschwerdeführer betreut wird, begleitet.

| Predicted | Gold |
|---|---|
| `Unverdroß` | `Unverdroß` |

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Missed by this rule (FN):**

- `Unverdroß` (person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_72`)


Bei der Erstellung des fachärztlichen Sachverständigengutachtens durch das Bundessozialamt  fanden weder der Befund der Stellungskommission noch die Aussagen von Frau Unverdroß  entsprechende Berücksichtigung.

| Predicted | Gold |
|---|---|
| `Unverdroß` | `Unverdroß` |

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_108`)


Der festgestellte Grad der Behinderung wird voraussichtlich mehr als 3 Jahre andauern: ja  GdB liegt vor seit: 01/2006  Herr Heinz Herper  ist voraussichtlich dauernd außerstande, sich selbst den Unterhalt zu  verschaffen:  Anmerkung bzw. Begründung betreffend die Fähigkeit bzw. voraussichtlich dauernde  Unfähigkeit, sich selbst den Unterhalt zu verschaffen:    Die Unfähigkeit sich selbst den Unterhalt zu verschaffen ist ab 1/2006 belegbar da ab diesem  Zeitpunkt höhergradige körperliche Beeinträchtigungen vorhanden sind;

| Predicted | Gold |
|---|---|
| `Heinz Herper` | `Heinz Herper` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_140`)


In der am 28. Oktober 2020 beim Bundesfinanzgericht durchgeführten mündlichen  Verhandlung wurde Folgendes erörtert:  Der Rechtsanwalt verwies auf die Aufführungen in der Beschwerde sowie auf die beantragten  Zeugen, insbesondere auf die Tante des Beschwerdeführers (Bf.),Frau Freßdorf  die Aussagen zu dem  damaligen Gesundheitszustand des Bf. während seines Studiums treffen könne.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_200`)


Laut Sachwalter habe Frau Freßdorf (Tante des Bf.) erzählt, dass sich ihr Neffe mit Beginn des  Studiums zunehmend gegenüber seiner Umwelt verschlossen und sich immer mehr  zurückgezogen habe, was sich dadurch geäußert habe, dass er keinen Kontakt mit der Familie  haben wollte und auch gemeinsamen Familienaktivitäten ferngeblieben sei.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_218`)


Lebensjahr (bzw. dem 25. Lebensjahr) eingetreten ist,  brachte Frau Freßdorf doch nur vor, dass sich ihr Neffe mit Beginn des Studiums zunehmend  gegenüber seiner Umwelt verschlossen und sich immer mehr zurückgezogen habe, was sich  dadurch geäußert habe, dass er keinen Kontakt mit der Familie haben wollte und auch  gemeinsamen Familienaktivitäten ferngeblieben sei.

| Predicted | Gold |
|---|---|
| `Freßdorf` | `Freßdorf` |

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in Vertretung des verhinderten Richters Ri1 in  der Beschwerdesache von Frau Nina Rasem, An der Walk 32, 9560 Persching, Österreich, über die Beschwerden der  Beschuldigten und der gemäß § 9 Abs. 7 VStG zur Haftung herangezogenen Firma GmbH,  An der Walk 32, 9560 Persching, Österreich, vom 6. November 2019, beide vertreten durch Rechtsanwalt Mag. Peter  Mayerhofer, Domplatz 16, 2700 Wiener Neustadt, gegen das Straferkenntnis des Magistrates  der Stadt Wien, Magistratsabteilung 6 Abgabenstrafen vom 4. Oktober 2019, Zahl MA6,  betreffend Verwaltungsübertretungen gemäß § 1 Abs. 1 in Verbindung mit § 16 Abs. 1 und  Tarifpost D 1 des Gebrauchsabgabegesetzes (GAG) vom 8. Juli 1966, LGBl. für Wien Nr. 20, in  der Fassung der Kundmachung ABl. der Stadt Wien Nr. 52/2016, beschlossen:  I. Gemäß § 50 Abs. 1 iVm § 31 Abs. 1 Verwaltungsgerichtsverfahrensgesetz (VwGVG)  iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz (BFGG) iVm § 5 Gesetz über die  Organisation der Abgabenverwaltung und besondere abgabenrechtliche  Bestimmungen in Wien (WAOR) wird – da das Straferkenntnis von Gesetzes wegen  außer Kraft tritt – das Verwaltungsstrafverfahren gemäß § 43 Abs. 1 VwGVG  eingestellt.   Gemäß § 52 Abs. 8 VwGVG haben die beschwerdeführenden Parteien keine Kosten  des Beschwerdeverfahrens zu leisten.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `An der Walk 32, 9560 Persching, Österreich` (address)
- `Mag. Peter  Mayerhofer` (person)
- `Magistrates  der Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_4`)


Begründung  Mit Straferkenntnis des Magistrates der Stadt Wien vom 4. Oktober 2019 Zahl wurde Frau  Nina Rasem (in weiterer Folge: Beschuldigte) für schuldig befunden,  1. sie habe in Wien als handelsrechtliche Geschäftsführerin der GmbH im März 2018 vor der  oben angeführten Liegenschaft auf dem öffentlichen Gemeindegrund, der dem öffentlichen  Verkehr dient, ein Gerüst im Ausmaß von 91,00 m² aufgestellt gehabt, wobei sie hiefür bis zum  1 von 6 Seite 2 von 6

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/131942.1`) (sent_id: `deanon_BFG_20260814_TEST/131942.1_37`)


Die GmbH hafte für die mit diesem Bescheid über die zur Vertretung nach außen Berufene,  Frau Nina Rasem, verhängten Geldstrafen von € 450,00, € 450,00, € 450,00, € 450,00, € 450,00,  € 450,00, € 310,00, € 310,00, € 310,00, € 310,00, € 310,00 und € 310,00 und die  Verfahrenskosten in der Höhe von € 456,00 sowie für sonstige in Geld bemessene  Unrechtsfolgen gemäß § 9 Abs. 7 VStG zur ungeteilten Hand.

| Predicted | Gold |
|---|---|
| `Nina Rasem` | `Nina Rasem` |

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_6`)


Weiters heißt es darin: „Da Herr Stavrakis im  Steuerjahr 2014 noch als in Österreich unbeschränkt Steuerpflichtiger eine Erklärung zur  Arbeitnehmerveranlagung (L1) einreichen wird, ersuchen wir Sie die unbeschränkte  Steuernummer von Herrn Stavrakis erst ab abgeschlossener Veranlagung 2014 auf eine  Steuernummer bei beschränkter Steuerpflicht abzuändern.“

| Predicted | Gold |
|---|---|
| `Stavrakis` | `Stavrakis` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/134332.1`) (sent_id: `deanon_BFG_20260814_TEST/134332.1_16`)


1. Eigentumsübertragung: Herr WM gibt sein Grünlandgrundstück Lisa Lindnau, wobei dieses  Grundstück mit Flächen des Herrn Lisa Lindnau  arrondiert wird bzw. dieser Erwerb eine  Arrondierung darstellt.  2. Eigentumsübertragung: Herr Lisa Lindnau  gibt sein Baulandgrundstück an Herrn WM, wobei bei  Herrn WM mit diesem Erwerb keine Arrondierung verbunden ist.

| Predicted | Gold |
|---|---|
| `Lisa Lindnau` | `Lisa Lindnau` |

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_5`)


Entscheidungsgründe  Mit Erkenntnis des Spruchsenates beim ehemaligen Finanzamt Wien 9/18/19 Klosterneuburg  als Organ des ehemaligen Finanzamtes Waldviertel als Finanzstrafbehörde vom 12. November  2020, SpS, Strafnummer, wurde Herr Petra Port, geb. am 1980, schuldig erkannt, er habe im  1 von 11 Seite 2 von 11

| Predicted | Gold |
|---|---|
| `Petra Port` | `Petra Port` |

**Missed by this rule (FN):**

- `Finanzamt Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Waldviertel` (organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_22`)


Herr Bodewein brachte mit E-Mail vom 15. September 2021 unter Angabe der GZ. MA67/Zahl1/2020  folgende Eingabe beim Magistrat der Stadt Wien ein:  „ich habe eine Mahnung bekommen, dass nicht weiß, wann und wo ich bestraft wurde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_25`)


Der Magistrat der Stadt Wien ersuchte Herrn Bodewein um Bekanntgabe seiner Telefonnummer  zwecks Klärung des Sachverhaltes, was Herr Bodewein mit E-Mail vom 29. September 2021  beantwortete.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien` (organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_31`)


Herr Bodewein müsste gemäß § 14 Abs. 2 Satz 2  VwGVG in der Fassung BGBl. I 109/2021 eine Mitteilung des Magistrates der Stadt Wien über  die Vorlage der (vermeintlichen) Beschwerde an das BFG erhalten haben.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)
- `BFG` (organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/135606.1`) (sent_id: `deanon_BFG_20260814_TEST/135606.1_34`)


Das Anbringen, welches Herr Bodewein per E-Mail am 15. September 2021 beim Magistrat der Stadt  Wien eingebracht hat, ist keine Beschwerde.

| Predicted | Gold |
|---|---|
| `Bodewein` | `Bodewein` |

**Missed by this rule (FN):**

- `Magistrat der Stadt  Wien` (organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/136344.1`) (sent_id: `deanon_BFG_20260814_TEST/136344.1_4`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Joachim Kotmann (= Beschwerdeführerin, Bf) hat für die Tochter A, geb. 11/1999, laufend die  Familienbeihilfe (FB) und den Kinderabsetzbetrag (KG) bezogen.

| Predicted | Gold |
|---|---|
| `Joachim Kotmann` | `Joachim Kotmann` |

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_14`)


Herr Julia Reittinger  ist voraussichtlich dauernd außerstande sich selbst den Unterhalt zu  verschaffen: NEIN

| Predicted | Gold |
|---|---|
| `Julia Reittinger` | `Julia Reittinger` |

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_3`)


Entscheidungsgründe  I. Verfahrensablauf:  1. Mit Anträgen, eingegangen am 27.10.2020, hat Frau Franziska Fitzmann (= Beschwerde-führerin, Bf),  geb. 04/1971, die Gewährung der Familienbeihilfe (FB) für sich sowie des Erhöhungsbetrages  zur Familienbeihilfe wegen erheblicher Behinderung "ab Jänner 2015" beantragt (Eigenantrag).

| Predicted | Gold |
|---|---|
| `Franziska Fitzmann` | `Franziska Fitzmann` |

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_23`)


So hatte Frau Thyssen erst  vor wenigen Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass  der EU-Vertrag jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grund- lage der Nationalität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_74`)


So hatte Frau Thyssen erst vor wenigen  Wochen in der Antwort auf eine parlamentarische Anfrage daran erinnert, dass der EU-Vertrag  jegliche Diskriminierung - direkt oder indirekt – von Arbeitnehmern auf Grundlage der Nationa- lität verbiete.

| Predicted | Gold |
|---|---|
| `Thyssen` | `Thyssen` |

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/140063.1`) (sent_id: `deanon_BFG_20260814_TEST/140063.1_5`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien, Magistratsabteilung 67, vom  10. November 2022, Zahl: MA67/226701238674/2022, wurde Herr Katharina Bauckholt (in weiterer  Folge: Beschwerdeführer) der Begehung einer Verwaltungsübertretung nach § 2 Wiener  Parkometergesetz 2006 für schuldig erkannt und über ihn nach § 4 Abs. 2 Wiener  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Katharina Bauckholt` | `Katharina Bauckholt` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien, Magistratsabteilung 67` (organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/141230.1`) (sent_id: `deanon_BFG_20260814_TEST/141230.1_38`)


Mit Aktenvermerk vom 20. April 2023 hielt die Magistratsabteilung 67 zur gegenständlichen  Geschäftszahl fest, ein Telefonat mit PÜG Dienstführung 1,Herr Mayerer (DW TelNr) habe  ergeben, das Überwachungsorgan DNr. ANr habe am Beanstandungstag (10.11.2022) im 22.

| Predicted | Gold |
|---|---|
| `Mayerer` | `Mayerer` |

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/141361.1`) (sent_id: `deanon_BFG_20260814_TEST/141361.1_5`)


Mit Strafverfügung des Magistrates der Stadt Wien vom 29. November 2021, Zahl:  MA67/XX/2021, wurde Herr Istvan  Melniczenko (in weiterer Folge: Beschwerdeführer) der Begehung  einer Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung für  schuldig erkannt und über ihn nach § 4 Abs. 1 Wiener Parkometergesetz 2006 eine Geldstrafe  1 von 7 Seite 2 von 7

| Predicted | Gold |
|---|---|
| `Istvan  Melniczenko` | `Istvan  Melniczenko` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_4`)


Dass der Geschäftsführer der GmbH, Herr Nadine Millradt, dies bestreite, sei ihm bekannt und  derzeit Gegenstand mehrerer Verfahren.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_7`)


Herr Nadine Millradt  schulde ihm noch ausstehende Gehälter.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_12`)


Sollte Herr Nadine Millradt  die Vorsteuer zum Abzug gebracht haben, müsse sie von ihm zurückgefordert werden.

| Predicted | Gold |
|---|---|
| `Nadine Millradt` | `Nadine Millradt` |

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_24`)


In der Begründung wird dazu ausgeführt:  „Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 8,4 Liter  Alkohol unter Abfindung, wobei diese Menge als "Hausbrand" steuerfrei belassen werden  sollte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_25`)


Mit Abfindungsanmeldung […] beantragte Herr Quentin Schwartkopp  die Herstellung von 15 Liter  Alkohol unter Abfindung, wobei diese Mengen als "Hausbrand" ebenfalls steuerfrei belassen  werden sollte.“

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_29`)


Und weiter: „[…]  hätte Herr Quentin Schwartkopp  diese Freimengen nicht beanspruchen dürfen, da der Sohn bereits seit  03.bbb.2013 nicht im gemeinsamen Haushalt mit Herrn Quentin Schwartkopp  lebte.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_33`)


In der Begründung wurde ausgeführt: „Nach dem Auszug "Abfrage  Abfindungsberechtigte/Person" vom 31.08.2018 des Zollamtes Innsbruck war Herr Quentin Schwartkopp  jedenfalls als Abfindungsberechtigter ausgewiesen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_34`)


Im Rahmen des Ermittlungsverfahrens wurde festgestellt, dass Herr Quentin Schwartkopp, belegt durch  den Übergabevertrag, GZ xxx vom 17.mt.2011 — mit Wirkung vom 01.mt.2011 — das  landwirtschaftliche Anwesen in Betriebssitz, an seinen Sohn Sohn, übergeben hat.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_37`)


Mit Schreiben des Zollamtes Innsbruck vom 14.01.2019, GZ 800000/thrhtr, wurde Herr  Quentin Schwartkopp  zur Abgabe einer Stellungnahme gemäß § 115 BAO eingeladen.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Missed by this rule (FN):**

- `Zollamtes Innsbruck` (organisation)

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_38`)


Mit Schreiben vom  29.01.2019 gab Herr Quentin Schwartkopp  an, dass er nach Übergabe seines Hofes an seinen Sohn Sohn  mit diesem mündlich vereinbart habe, dass er die Obstveredelung weiterhin als  Fruchtgenussberechtigter betreiben dürfe.

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_41`)


Überdies hätte Herr Quentin Schwartkopp  auch  vor der Übertragung des land- und forstwirtschaftlichen Betriebes die Freimenge für Herrn  3 von 8 Seite 4 von 8

| Predicted | Gold |
|---|---|
| `Quentin Schwartkopp` | `Quentin Schwartkopp` |

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_142`)


Soweit der Bf. darauf verweist, dass Herr Abersfeller aus Gewerbebetrieb  erzielt bzw bei der SVA pflichtversichert sei, mag zwar richtig sein, ist aber bedeutungslos:  Aufgrund des funktionalen Verständnisses des Begriffes der Eingliederung gemäß der zitierten  Judikatur des VwGH ist es ohne Bedeutung, in welcher Weise die aus der Tätigkeit erzielten  Einkünfte zu qualifizieren wären;

| Predicted | Gold |
|---|---|
| `Abersfeller` | `Abersfeller` |

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/142611.1`) (sent_id: `deanon_BFG_20260814_TEST/142611.1_3`)


Entscheidungsgründe  I. Verfahrensgang:  1. Frau Dominik Barfusz (= Beschwerdeführerin, Bf) hat für den Sohn A, geb. 06/1997, laufend die  Familienbeihilfe (FB) bezogen.

| Predicted | Gold |
|---|---|
| `Dominik Barfusz` | `Dominik Barfusz` |

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_4`)


Begründung  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung Bereich Finanzstrafsachen  Team 6 als Finanzstrafbehörde vom 9. Oktober 2023, SpS-1, wurden  I. Herr Dieter Avemaria, geboren 1980, schuldig erkannt, er habe als Komplementär und  abgabenrechtlich Verantwortlicher der Engelbert Schefe  vorsätzlich  A. unter Verletzung einer abgabenrechtlichen Anzeige-, Offenlegungs- oder Wahrheitspflicht  eine Verkürzung an  Umsatzsteuer 2017 von € 3.609,08  Umsatzsteuer 2019 von € 23.455,92  Umsatzsteuer 2020 von € 2.187,78   1 von 8 Seite 2 von 8

| Predicted | Gold |
|---|---|
| `Dieter Avemaria` | `Dieter Avemaria` |

**Missed by this rule (FN):**

- `Amt für Betrugsbekämpfung` (organisation)
- `Engelbert Schefe` (person)

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/143900.1`) (sent_id: `deanon_BFG_20260814_TEST/143900.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. Gerhard Groschedl über die  Beschwerde von Frau Theodora Berenwinkel, Klam 26, 8673 Steinhöf, Österreich, vom 12. Februar 2024, gegen die zwei  Straferkenntnisse der belangten Behörde, Magistrat der Stadt Wien, Magistratsabteilung 67,  als Abgabenstrafbehörde (beide) vom 30. Jänner 2024, GZen 1) MA67/GZ1/2023 und 2)  MA67/GZ2/2023, beide wegen einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr.  20/2020 in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBI. für Wien Nr.  9/2006, in der Fassung LGBl. für Wien Nr. 71/2018, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  teilweise stattgegeben, als die verhängten Geldstrafen von jeweils 40,00 Euro auf jeweils  30,00 Euro und die für den Fall der Uneinbringlichkeit festgesetzten Ersatzfreiheitsstrafen von  jeweils 9 auf jeweils 7 Stunden herabgesetzt werden.

| Predicted | Gold |
|---|---|
| `Theodora Berenwinkel` | `Theodora Berenwinkel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gerhard Groschedl` (person)
- `Klam 26, 8673 Steinhöf, Österreich` (address)
- `Magistrat der Stadt Wien, Magistratsabteilung 67` (organisation)
- `Stadt Wien` (organisation)
- `Stadt Wien` (organisation)

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_34`)


Herr Corvin Billmaier  hat die Ausgaben getragen und bezahlt und Ausgaben sind bei jenem  abzugsfähig, der sie bezahlt hat und nicht bei jenem, den sie betroffen hätten.

| Predicted | Gold |
|---|---|
| `Corvin Billmaier` | `Corvin Billmaier` |

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/144841.1`) (sent_id: `deanon_BFG_20260814_TEST/144841.1_4`)


Entscheidungsgründe  Mit Strafverfügung des Magistrates der Stadt Wien vom 8. Februar 2024, GZ. MA67/GZ/2023,  wurde Frau Gudrun Joehnk (in weiterer Folge: Beschwerdeführerin) der Begehung einer  Verwaltungsübertretung nach § 5 Abs 2 Wiener Parkometerabgabeverordnung für schuldig  erkannt und über sie nach § 4 Abs 1 Wiener Parkometergesetz 2006 eine Geldstrafe in der  Höhe von 60,00 Euro verhängt und für den Fall ihrer Uneinbringlichkeit eine  Ersatzfreiheitsstrafe von 14 Stunden festgesetzt.

| Predicted | Gold |
|---|---|
| `Gudrun Joehnk` | `Gudrun Joehnk` |

**Missed by this rule (FN):**

- `Magistrates der Stadt Wien` (organisation)

**Example 50** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_38`)


Sie sehen im Anhang dass Herr Abeles damit bis 27 Dezember  gefahren ist.

| Predicted | Gold |
|---|---|
| `Abeles` | `Abeles` |

**Example 51** (doc_id: `deanon_BFG_20260814_TEST/144864.1`) (sent_id: `deanon_BFG_20260814_TEST/144864.1_41`)


Der Beschwerde waren zahlreiche Unterlagen zum Beweis dafür beigelegt, dass der Bf. nie mit  dem Kraftfahrzeug mit dem behördlichen Kennzeichen 123 gefahren sei und dass Herr Abeles bis  27. Dezember 2023 gefahren sei (bzw. an diesem Tag das Leasing Auto zurückgegeben habe).

| Predicted | Gold |
|---|---|
| `Abeles` | `Abeles` |

**Example 52** (doc_id: `deanon_BFG_20260814_TEST/144875.1`) (sent_id: `deanon_BFG_20260814_TEST/144875.1_144`)


Zur Begründung der fristgerechten Einbringung der Beschwerde wurde im  Vorlageantrag ausgeführt, die Mitarbeiterin,Frau Pöttmann  habe die Beschwerde am 30. April 2018  um ca. 17:30 Uhr persönlich in den Briefkasten des Finanzamtes eingeworfen und diese  Erledigung auch im Postbuch vermerkt.

| Predicted | Gold |
|---|---|
| `Pöttmann` | `Pöttmann` |

**Missed by this rule (FN):**

- `Finanzamtes` (organisation)

**Example 53** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_4`)


Entscheidungsgründe  Verfahrensgang:  Mit Strafverfügung vom 4. Juni 2024, GZ. MA67/GZ/2024, lastete der Magistrat der Stadt Wien,  Magistratsabteilung 67, als Verwaltungsstrafbehörde Frau Manhardt an, sie habe das  mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen 123 (A) am 4. April 2024 um  12:24 Uhr in der gebührenpflichtigen Kurzparkzone in 1020 Wien, Helenengasse zwischen  Praterstern und Hedwiggasse rechts, abgestellt, ohne für seine Kennzeichnung mit einem für  den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Missed by this rule (FN):**

- `Magistrat der Stadt Wien,  Magistratsabteilung 67` (organisation)

**Example 54** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_5`)


Demnach habe Frau Manhardt die Parkometerabgabe fahrlässig verkürzt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 55** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_8`)


Mit an die Magistratsabteilung 67 gesendeter E-Mail vom 12. Juni 2024 erstattete Herr  Jeanne Pavlovitsch (in der Folge: Beschwerdeführer) eine von der belangten Behörde als Einspruch  gegen die Strafverfügung vom 4. Juni 2024 gewertete Eingabe.

| Predicted | Gold |
|---|---|
| `Jeanne Pavlovitsch` | `Jeanne Pavlovitsch` |

**Example 56** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_9`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertetungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 57** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_39`)


Mit Schreiben vom 17. Juni 2024 (Verfahrensanordnung-Vollmachtsvorlage) forderte die  belangte Behörde den Beschwerdeführer auf, binnen zwei Wochen ab Zustellung des  Schreibens eine Vollmacht vorzulegen, aus welcher das Vertretungsverhältnis zu Frau Manhardt sowie die Berechtigung zur Einbringung eines Rechtsmittels im  Verwaltungsstrafverfahren hervorgehe.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 58** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_66`)


Nach der Aktenlage wurde der Einspruch gegen die an Frau Manhardt ergangene  Strafverfügung vom Beschwerdeführer erhoben, eine Vollmacht wurde jedoch (trotz  Aufforderung durch die belangte Behörde) nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `Manhardt` | `Manhardt` |

**Example 59** (doc_id: `deanon_BFG_20260814_TEST/145870.1`) (sent_id: `deanon_BFG_20260814_TEST/145870.1_21`)


Nach telefonischer Rücksprache mit Frau Lensen füge ich das ganze nochmals als  Anhang hinzu.“

| Predicted | Gold |
|---|---|
| `Lensen` | `Lensen` |

**Example 60** (doc_id: `deanon_BFG_20260814_TEST/146473.1`) (sent_id: `deanon_BFG_20260814_TEST/146473.1_3`)


Begründung  Am 22.03.2024 erließ das Finanzamt für Frau Günter Salfetter, Beschwerdeführerin, einen  Einkommensteuerbescheid (Arbeitnehmerveranlagung) für das Jahr 2023.

| Predicted | Gold |
|---|---|
| `Günter Salfetter` | `Günter Salfetter` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 61** (doc_id: `deanon_BFG_20260814_TEST/148423.1`) (sent_id: `deanon_BFG_20260814_TEST/148423.1_5`)


Entscheidungsgründe  Nach dem das Finanzamt in der Beschwerdevorentscheidung (BVE) vom 17.11.2023 das  Pendlerpauschale, den Pendlereuro und den Alleinerzieherabsetzbetrag antragsgemäß  steuermindernd berücksichtigt hat, ist nur mehr strittig, ob sogenannte Familienheimfahrten  von Frau Kuehnhanss (in der Folge: Beschwerdeführerin: Bf) vorliegen und als Werbungskosten zu  berücksichtigen sind.

| Predicted | Gold |
|---|---|
| `Kuehnhanss` | `Kuehnhanss` |

**Missed by this rule (FN):**

- `Finanzamt` (organisation)

**Example 62** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_14`)


Herr Kaspar Sadowski  führt ab 1.1.2018 den Betrieb „Unternehmensberatung" - der zuvor von der **  GMBH geführt wurde - nun mehr als Einzelunternehmung Kaspar Sadowski  weiter.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

**Example 63** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_20`)


Da Herr Kaspar Sadowski  immer  Alleingesellschafter der ** GMBH war, ist der Übergang des Verlustvortrages mit 100 %  vorzunehmen.

| Predicted | Gold |
|---|---|
| `Kaspar Sadowski` | `Kaspar Sadowski` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128872.1`) (sent_id: `deanon_BFG_20260814_TEST/128872.1_28`)


Betreffend die Baurechtseinlage EZ 2 KG XY) wurde mit Schreiben vom 5.4.2017 von Notar Herr  Mag. Z die Befreiung gemäß § 3 Abs. 1 Z 2 GrEStG (damals fälschlicherweise die Befreiung  gemäß § 3 Abs. 1 Z 3 GrEStG bezeichnet) beantragt.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag. Z`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Z`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) Siegfried Basyurt, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Siegfried Basyurt`(person)
- `Finanzamt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_17`)


Herr Bf benützt für seine Wochenendfahrten nach A1 einen anderen Pkw.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_18`)


Herr Bf-Gatte ist während der Woche in D-XY whft und in A1 nicht gemeldet;

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_64`)


- Herr Bf-Gatte ist Angestellter der Fa. "F-AG" in D.  - Der PKW steht Frau Basyurt tagtäglich zu Verfügung, somit ständiger Standort in Österreich  Kurz nachdem Frau Basyurt das FA verlassen hat, rief Herr Bf-Gatte aus Deutschland an, sämtliche  von der Frau gemachten Angaben seien unrichtig.

**False Positives:**

- `Bf` — no gold match — likely missing annotation
- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Basyurt`(person)
- `Basyurt`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_18`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf hat seinen Familienwohnsitz gemeinsam mit seinen Kindern (im Beschwerdejahr 8 und  12 Jahre alt) in Ungarn, wo weder er noch seine Frau Einkünfte erzielen.

**False Positives:**

- `Einkünfte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_100`)


Lebensjahr, dies wurde in dem  Gutachten von Frau Dr. 2 zwar anerkannt, aber eine Arbeitsunfähigkeit hat sie mir trotzdem  nicht attestiert.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. 2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. 2`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_131`)


Lebensjahr, dies wurde in dem Gutachten von Frau Dr. 2  zwar anerkannt, aber eine Arbeitsunfähigkeit hat sie mir trotzdem nicht attestiert....  Derzeitige Beschwerden:  Die Antragstellerin gibt an: "Ich habe das gleiche seit meiner Jugend, das sind Panikattacken,  Kopfschmerzen und eine Sozialphobie.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. 2`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. 2`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_68`)


Herr Dr. YYY hat das Fahrzeug am Morgen diesen Tages in der STRASSE-Hauptwohnsitz  übernommen und mitgeteilt, dass er einige Tage nach Ungarn fahren wird.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_149`)


Herr  Dr. YYY ist für Ärzte ohne Grenzen tätig.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_150`)


Herr Dr. YYY hat mich nach einem schweren  Insektenbiss in GEBIET, mit Lebensgefahr für mich, hervorragend behandelt. Darauf gründet  sich die Freundschaft.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_151`)


Herr Dr. YYY arbeitet in Gebieten, wo kein Mobilfunknetz vorhanden ist.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/129941.1`) (sent_id: `deanon_BFG_20260814_TEST/129941.1_385`)


Herr Dr. YYY arbeite in Gebieten, wo kein  Mobilfunknetz vorhanden sei.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. YYY`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. YYY`(person)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/130494.1`) (sent_id: `deanon_BFG_20260814_TEST/130494.1_67`)


Unstrittig war, dass die Gesellschafter-Geschäftsführerin, Frau Ges-Gf, mit 25,25% im Sinne des  § 22 Z 2 zweiter Teilstrich EStG 1988 an der Bf. wesentlich beteiligt war.

**False Positives:**

- `Ges` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_69`)


Beweis: vorzulegende Skizzen und Notizen des Beschwerdeführers   Zeugin Frau Freßdorf  p.A., 1220 Wien, Zeugin Frau Unverdroß  Behindertenbetreuerin, p.A. Wohnverbund B,  1220 Wien, L-Straße 4-6/1  Zeugin Frau Prim.

**False Positives:**

- `Unverdroß  Behindertenbetreuerin` — partial — gold is substring of pred: `Unverdroß`
- `Prim` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Freßdorf`(person)
- `Unverdroß`(person)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_122`)


Herr Bf ist im Wesentlichen in der Lage, einfache Sachverhalte zu erfassen, zeigt sich bei  komplexeren Anforderungen allerdings überfordert.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_115`)


Es wurden einvernehmlich nicht nur Befunde beurteilt, sondern auch ausführliche persönliche  Gespräche mit Frau Mag. D (Neuropsychologisches Gutachten) und OA. Dr. G (Neuropädiaterin)  geführt.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. G`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_36`)


Herr Dr. B würde nur im KH der  Diakonissen operieren;

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/137813.1`) (sent_id: `deanon_BFG_20260814_TEST/137813.1_19`)


Zum  Masseverwalter wurde Herr Mag. G H bestellt.  Gesellschafter der AB sind Herr C D und die Verlassenschaft nach E F. Geschäftsführer waren  Herr C D und bis zu seinem Tod im Jahr 2011 Herr E F.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_22`)


In einer Besprechung vom 16.1.2015 hat Herr Dr. F zu  diesem Thema ua. angegeben, dass Schätzungsgutachten sich heute nicht in seinen Akten  befinden und er zum Zeitpunkt der Selbstberechnung davon ausgegangen ist, dass der  vereinbarte Kaufpreis zumindest dem gemeinen Wert entspricht und er sich damals auf die  Auskünfte der Vertragsparteien verlassen habe, wonach der Wert (gemeint gemeiner Wert)  dem vereinbarten Kaufpreis entspricht.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_23`)


Weiter hat Herr Dr. F angegeben, dass er zu allen  betroffenen Selbstberechnungen die entsprechenden Nachweise vorlegen wird.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_24`)


Mit Mail vom 9.2.2015 teilt Herr Dr. F dem Finanzamt für Gebühren Verkehrsteuern und  Glücksspiel mit, dass sich die entsprechenden Berechnungsgrundlagen (gemeint Nachweise  über die gemeinen Werte) bei der Firma K (die Bf) befinden.

**False Positives:**

- `Dr` — partial — pred is substring of gold: `Dr. F`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. F`(person)
- `Finanzamt für Gebühren`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_105`)


Dagegen erhob die Bf. fristgerecht Beschwerde und brachte unter Anführung der  gegenständlichen Geschäftszahl begründend (wörtlich) vor:  „Betrifft: Milderung der Strafe   Sehr geehrte Herr/Frau Frau,  ich habe Ihr Bescheid erhalten und bin gezwungen um eine Milderung anzusuchen.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_126`)


Am 27. Juli 2022 teilte die Magistratsabteilung 67 (Frau Frau1) auf Nachfrage des  Bundesfinanzgerichtes mit, dass die Bf. entgegen ihren Beschwerdeausführungen bis dato  keine weitere Einzahlung zu gegenständlicher GZ. leistete.

**False Positives:**

- `Frau` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_75`)


Diagnose:   • V.a. F80 Entwicklungsstörung des Sprechens und der Sprache   • F81.0 Lese- Rechtschreibstörung   • V.a. F83 Kombinierte umschriebene Entwicklungsstörung   • V.a. F90.0 Einfache Aktivitäts- und Aufmerksamkeitsstörung   Das Schreiben der Bf. vom 2. März 2021 lautete:   …ich möchte Sie in Kenntnis setzen, dass mir der Endbefund meines Sohnes A., durchgeführt  von Fr. Mag.a SJ. (Psychologin), am 05.04.2021, vorliegen wird.

**False Positives:**

- `Mag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_14`)


Ziel der Bautätigkeit sei die Schaffung einer gemeinsamen  Wohnung für seine Familie, dh für seine Frau Prof. Engelbert Thuerrigl  verehelichte A, seine Kinder und für ihn  selbst, gewesen.

**False Positives:**

- `Engelbert Thuerrigl` — partial — pred is substring of gold: `Prof. Engelbert Thuerrigl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Engelbert Thuerrigl`(person)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_86`)


Die Fahrstrecke zu Frau DDr. Ramon Luckmeier  Psychiaterin, Adr2, O1 O, betrage hin und zurück je 21 km.

**False Positives:**

- `Ramon Luckmeier  Psychiaterin` — positional overlap with gold: `DDr. Ramon Luckmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Ramon Luckmeier`(person)

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_102`)


K1 befinde sich laut den Angaben der Bf in Behandlung von Frau DDr. Ramon Luckmeier  Fachärztin für  Psychiatrie und Psychotherapie, in der Adr.

**False Positives:**

- `Ramon Luckmeier  Fachärztin` — positional overlap with gold: `DDr. Ramon Luckmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Ramon Luckmeier`(person)

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/141874.1`) (sent_id: `deanon_BFG_20260814_TEST/141874.1_200`)


K1 befindet sich laut den Angaben der Bf in Behandlung von Frau DDr. Ramon Luckmeier  Fachärztin für  Psychiatrie und Psychotherapie, in der Adr.

**False Positives:**

- `Ramon Luckmeier  Fachärztin` — positional overlap with gold: `DDr. Ramon Luckmeier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DDr. Ramon Luckmeier`(person)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_23`)


In der Folge wurden betreffend Herrn Quentin Schwartkopp  vom Zollamt zwei Bescheide erlassen  (20.2.2019, 800000/cccc):  Zunächst wurden laut Bescheid I (für 2016) vom 20.2.2019 Abfindungsanmeldungen gemäß §  64 Abs. 3 des Alkoholsteuergesetzes (AlkStG) iVm. § 11 Abfindungsverordnung (AbfV)  dahingehend berichtigt, dass Herr Sohn, Adresse_Sohn, nicht als Haushaltsangehörige gemäß §  70 Abs. 3 AlkStG geltend gemacht werden könne.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Quentin Schwartkopp`(person)
- `Zollamt`(organisation)

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_36`)


Herr Sohn wurde zwischenzeitlich gemäß § 62 AlKStG als Abfindungsberechtigter  registriert.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_40`)


Unter Hinweis auf §§ 2 Abs. 1, 4 Abs. 2 Z 5, 8 Abs. 1 Z 2, § 9 Abs. 1 Ziffer 2, § 62 Abs. 2 Z 3, 64  Abs. 3 AlkStG betonte das Zollamt, dass durch den Übergabevertrag vom eee2011 Herr Sohn  unzweifelhaft Eigentümer an den Früchten (= alkoholbildende Stoffe) wurde; auf mündliche  Absprachen zwischen Vater und Sohn komme es nicht an.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_81`)


Herr Sohn hat seit 03.bbb.2013 seinen aktuellen  ordentlichen Wohnsitz (Hauptwohnsitz) in Adresse_Sohn.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_88`)


Wie das Zollamt auch zu diesem Beschwerdepunkt ausführlichst und zu Recht betont hat,  wurde mit der Übergabe im Jahr 2011 der Übernehmer der Liegenschaft, Herr Sohn, auch  Eigentümer an den darauf befindlichen Obstbäumen und an deren Früchte.

**False Positives:**

- `Sohn` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Zollamt`(organisation)

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_36`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Im vorliegenden Beschwerdefall hat die belangte Behörde das Strafverfahren gegen Frau Manhardt  AdresseBeschuldigte, aufgrund der ihr zur Verfügung stehenden Unterlagen als  Beschuldigte eingeleitet und ihr mit Strafverfügung vom 4. Juni 2024 eine  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4  Abs. 1 Wiener Parkometergesetz 2006 angelastet sowie eine Geldstrafe in Höhe von  60,00 Euro verhängt und im Uneinbringlichkeitsfall eine Ersatzfreiheitsstrafe von 14 Stunden  auferlegt.

**False Positives:**

- `Manhardt  Adresse` — partial — gold is substring of pred: `Manhardt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Manhardt`(person)

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_280`)


Dieses Produkt hat Herr Dr. B nicht verschrieben.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/146490.1`) (sent_id: `deanon_BFG_20260814_TEST/146490.1_304`)


Herr Dr. T ist ein Arzt.

**False Positives:**

- `Dr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_289`)


Zum Beweisantrag:  Herr Baumeister Y X war von 3. Oktober 2013 bis 7. November 2016 gewerberechtlicher  Geschäftsführer der e GmbH (vgl. BFG-Akt I Bl. 56b).

**False Positives:**

- `Baumeister` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `BFG`(organisation)

</details>

---

## `Dr_in_Title` 🏆

**F1:** 0.023 | **Precision:** 0.613 | **Recall:** 0.012  

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
| 0.613 | 0.012 | 0.023 | 31 | 19 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 19 | 12 | 1595 |

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

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134902.1`) (sent_id: `deanon_BFG_20260814_TEST/134902.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alice Schöpfel  in der Beschwerdesache Walter Guggenmoos,  Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich, vertreten durch Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH,  Winkelweg 25 Tür 1, 6070 Ampass, über die Beschwerde vom 12. August 2013 gegen die  Bescheide des Finanzamtes Innsbruck (nunmehr: Finanzamt Österreich) vom 16. Juli 2013, Str.  Nr. 79-464/0427, betreffend  1. Festsetzung der Normverbrauchsabgabe für den Zeitraum November 2011      und Verspätungszuschlag  2.

| Predicted | Gold |
|---|---|
| `Dr.in Alice Schöpfel` | `Dr.in Alice Schöpfel` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Walter Guggenmoos` (person)
- `Ferdinand Freiligrath-Gasse 10, 9322 Micheldorf, Österreich` (address)
- `Dr. Schwab Wirtschaftstreuhand Steuerberatungs-GmbH` (organisation)
- `Finanzamtes Innsbruck` (organisation)
- `Finanzamt Österreich` (organisation)
- `79-464/0427` (tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_1`)


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

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/136103.1`) (sent_id: `deanon_BFG_20260814_TEST/136103.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Natascha Weingarte  in der Beschwerdesache des B,  vertreten durch StB, über die Berufung vom 27. August 2012 gegen die Bescheide des  Finanzamtes X vom 10. August 2012 betreffend Einkommensteuer für die Jahre 2004 bis 2007  zu Steuernummer 46-139/2044  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Natascha Weingarte` | `Dr.in Natascha Weingarte` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Finanzamtes` (organisation)
- `46-139/2044` (tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138402.1`) (sent_id: `deanon_BFG_20260814_TEST/138402.1_1`)


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

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/140410.1`) (sent_id: `deanon_BFG_20260814_TEST/140410.1_1`)


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

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/141832.1`) (sent_id: `deanon_BFG_20260814_TEST/141832.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Li Lübkemann  in der   Beschwerdesache Theobald Tormöllen, Am Hora 38, 9554 Trenk, Österreich, vertreten durch Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Andreas-Hofer-Straße 43, 6020  Innsbruck, über die Beschwerde vom 2. September 2016 gegen den Bescheid des Finanzamtes  für Gebühren, Verkehrsteuern und Glücksspiel, nunmehr Finanzamt Österreich- Sonderzuständigkeiten, vom 24. August 2016, ErfNr, betreffend Grunderwerbsteuer im  fortgesetzten Verfahren   zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Dr.in Li Lübkemann` | `Dr.in Li Lübkemann` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Theobald Tormöllen` (person)
- `Am Hora 38, 9554 Trenk, Österreich` (address)
- `Marsoner + Partner GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft` (organisation)
- `Finanzamtes` (organisation)
- `Finanzamt` (organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/142964.1`) (sent_id: `deanon_BFG_20260814_TEST/142964.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Alessia Gladebeck  in der Beschwerdesache Roman Baldauf,  Georg-Aichinger-Straße 14, 4264 Helbetschlag, Österreich, über die Beschwerde vom 17. Jänner 2023 gegen den Bescheid des  Finanzamtes Österreich vom 3. Jänner 2023, Ordnungsbegriff XX1, betreffend Abweisung des  Antrages auf Familienbeihilfe ab Oktober 2022 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Alessia Gladebeck` | `Dr.in Alessia Gladebeck` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Roman Baldauf` (person)
- `Georg-Aichinger-Straße 14, 4264 Helbetschlag, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/143627.1`) (sent_id: `deanon_BFG_20260814_TEST/143627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Svetlana Ronnacker  in der Beschwerdesache der ehemals  im Firmenbuch zu FN eingetragen gewesenen, mit Beschluss des LG X am 4.7.2023 amtswegig  aus dem Firmenbuch gelöschten Franziskus Dziemballa  über deren Beschwerde vom 24. Februar 2021  gegen den Bescheid des Finanzamt Oststeiermark  vom 2. Februar 2021 betreffend Umsatzsteuerfestsetzung  06.2020 zu Steuernummer 10-349/0551  beschlossen:   I. Die Beschwerde wird als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Dr.in Svetlana Ronnacker` | `Dr.in Svetlana Ronnacker` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Franziskus Dziemballa` (person)
- `Finanzamt Oststeiermark` (organisation)
- `10-349/0551` (tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_1`)


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

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/144747.1`) (sent_id: `deanon_BFG_20260814_TEST/144747.1_1`)


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

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/146473.1`) (sent_id: `deanon_BFG_20260814_TEST/146473.1_1`)


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

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/146537.1`) (sent_id: `deanon_BFG_20260814_TEST/146537.1_1`)


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

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/147657.1`) (sent_id: `deanon_BFG_20260814_TEST/147657.1_1`)


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

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/148301.1`) (sent_id: `deanon_BFG_20260814_TEST/148301.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Hildegard Nüßgens  in der Beschwerdesache Charles Dormayr,  SET-Straße 22, 4382 Sarmingstein, Österreich, vertreten durch Christandl & Partner Rechtsanwälte, Mag. Heinz Bauer,  Elisabethstraße 50b, 8010 Graz, über die Beschwerde vom  13. Jänner 2020 gegen den  Bescheid des Finanzamtes Österreich vom  11. Dezember 2019 betreffend Grunderwerbsteuer  27.02.2019 Steuernummer 59-652/7687  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dr.in Hildegard Nüßgens` | `Dr.in Hildegard Nüßgens` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Charles Dormayr` (person)
- `SET-Straße 22, 4382 Sarmingstein, Österreich` (address)
- `Mag. Heinz Bauer` (person)
- `Finanzamtes Österreich` (organisation)
- `59-652/7687` (tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_1`)


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

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Hemma Ramelow` — partial — pred is substring of gold: `Univ.-Prof.in Dr.in Hemma Ramelow`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow`(person)
- `Mag. Damian Wiecher`(person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_111`)


Gutachten erstellt am 31.01.2017 von Dr.in Silvia Bauer  Gutachten vidiert am 31.01.2017 von Dr.in Renate Reininger"

**False Positives:**

- `Dr.in Silvia Bauer  Gutachten` — partial — gold is substring of pred: `Dr.in Silvia Bauer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Silvia Bauer`(person)
- `Dr.in Renate Reininger`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/131832.1`) (sent_id: `deanon_BFG_20260814_TEST/131832.1_2`)


Das Bundesfinanzgericht hat durch die Richterin Dr.in Regina Manegold  über die Beschwerde des Dr.in KzlR Helge Erwied,  Unterfeichten 5, 4055 Sipbach, Österreich, vom 23. Dezember 2020, gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67, vom 17. Dezember 2020, Zl. MA67/Zahl/2020, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Dr.in Kzl` — partial — pred is substring of gold: `Dr.in KzlR Helge Erwied`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Regina Manegold`(person)
- `Dr.in KzlR Helge Erwied`(person)
- `Unterfeichten 5, 4055 Sipbach, Österreich`(address)
- `Magistrates der Stadt  Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)
- `Magistrates der Stadt Wien`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/131833.1`) (sent_id: `deanon_BFG_20260814_TEST/131833.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Petra Özkanli  in der Beschwerdesache des  Betriebes gewerblicher Art Radweg A-Tal des Tourismusverbandes A B, Dornackerstraße 480, 4352 Innernstein, Österreich  vertreten durch StB, über die Beschwerden vom 16. August 2017 gegen die Bescheide des  Finanzamt Wien 2/20/21/22  vom 2. Juni 2017 betreffend Wiederaufnahme des Verfahrens hinsichtlich  Körperschaftsteuer 2016 und Körperschaftsteuer 2016 zu Recht erkannt:   I. Die Beschwerde gegen den Bescheid über die Wiederaufnahme des Verfahrens  hinsichtlich Körperschaftsteuer 2016 wird als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Petra` — partial — pred is substring of gold: `Dr.in Petra Özkanli`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Petra Özkanli`(person)
- `Dornackerstraße 480, 4352 Innernstein, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/132474.1`) (sent_id: `deanon_BFG_20260814_TEST/132474.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Violetta Colberg  in der Beschwerdesache KzlR Kurt Bätzgen,  Alte Zeile 11, 4084 Sonnleiten, Österreich, gegen den Bescheid des FAF vom 10. Mai 2013 über die Festsetzung eines  Säumniszuschlages für die Umsatzsteuer 2011 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Violetta Colberg` — partial — pred is substring of gold: `Hon.-Prof.in Dr.in Violetta Colberg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dr.in Violetta Colberg`(person)
- `KzlR Kurt Bätzgen`(person)
- `Alte Zeile 11, 4084 Sonnleiten, Österreich`(address)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134394.1`) (sent_id: `deanon_BFG_20260814_TEST/134394.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Dr.in Sieglinde Steinkaemper  in der Beschwerdesache Julian Gruening,  Litzldorfer-Gasse 83, 4893 Harpoint, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse 1 Tür  Freyung, 1010 Wien, und GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Handelskai 92, Gate 2, 7A, 1200 Wien, über die   1.

**False Positives:**

- `Dr.in Sieglinde Steinkaemper` — partial — pred is substring of gold: `Hon.-Prof.in Dr.in Sieglinde Steinkaemper`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof.in Dr.in Sieglinde Steinkaemper`(person)
- `Julian Gruening`(person)
- `Litzldorfer-Gasse 83, 4893 Harpoint, Österreich`(address)
- `Deloitte Tax Wirtschaftsprüfungs GmbH`(organisation)
- `GTU GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/139018.1`) (sent_id: `deanon_BFG_20260814_TEST/139018.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Priv.-Doz.in Dr.in Wendy Chudak  in der Beschwerdesache Susette Hadenfelt,  Burgergasse 57, 2632 St. Valentin-Landschach, Österreich, vertreten durch Huber & Rosenthal Steuerberatung KG, Stadtplatz 56, 5280  Braunau/Inn, über die Beschwerde vom 9. August 2017 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 17. Juli 2017 betreffend Einkommensteuer 2016 Steuernummer  34-724/8270  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Dr.in Priv` — partial — pred is substring of gold: `Dr.in Priv.-Doz.in Dr.in Wendy Chudak`
- `Dr.in Wendy Chudak` — partial — pred is substring of gold: `Dr.in Priv.-Doz.in Dr.in Wendy Chudak`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Priv.-Doz.in Dr.in Wendy Chudak`(person)
- `Susette Hadenfelt`(person)
- `Burgergasse 57, 2632 St. Valentin-Landschach, Österreich`(address)
- `Huber & Rosenthal Steuerberatung KG`(organisation)
- `Finanzamtes  Braunau Ried Schärding`(organisation)
- `34-724/8270`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/142596.1`) (sent_id: `deanon_BFG_20260814_TEST/142596.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Mag. VN. NN., die Richterin Dr.in  Ri.N. sowie die fachkundigen Laienrichter Lena Pahlmann und Ch,Nn. in der Beschwerdesache  Esra Voskuhle, Brandstetterweg 76k, 4682 Buchet, Österreich, vertreten durch Beratungs GmbH, Str.x, plz Stadt, über die  Beschwerde vom 26. Juni 2019 gegen den Bescheid des Finanzamtes für Gebühren,  Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich Dienststelle  Sonderzuständigkeiten) vom 27. Mai 2019 betreffend Gebühren gemäß § 33 TP 20  Gebührengesetz (GebG) 1957 nach Durchführung einer mündlichen Verhandlung am  12. Oktober 2023 in Anwesenheit des Beschwerdeführers und dessen Ehegattin A.N.G und der  Schriftführerin Vn. Nn1 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Dr.in  Ri` — partial — pred is substring of gold: `Dr.in  Ri.N.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in  Ri.N.`(person)
- `Lena Pahlmann`(person)
- `Esra Voskuhle`(person)
- `Brandstetterweg 76k, 4682 Buchet, Österreich`(address)
- `Beratungs GmbH`(organisation)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/143519.1`) (sent_id: `deanon_BFG_20260814_TEST/143519.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Dr.in Jeannine Gondrom  betreffend den Antrag des OMedR Simon Pavlicsek, Fulateia 364, 9562 Spitzenbichl, Österreich,   auf Gewährung der Verfahrenshilfe gemäß § 292 BAO im Beschwerdeverfahren zum Bescheid  des Finanzamt Graz-Stadt  vom 06.06.2023 hinsichtlich Rückforderung von Kinderabsetzbetrag und  Familienbeihilfe für vier Kinder für den Zeitraum 09.2020 – 07.2022  beschlossen:  Der Antrag auf Gewährung der Verfahrenshilfe wird abgewiesen.

**False Positives:**

- `Dr.in Jeannine Gondrom` — partial — pred is substring of gold: `Priv.-Doz.in Dr.in Jeannine Gondrom`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Dr.in Jeannine Gondrom`(person)
- `OMedR Simon Pavlicsek`(person)
- `Fulateia 364, 9562 Spitzenbichl, Österreich`(address)
- `Finanzamt Graz-Stadt`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/147903.1`) (sent_id: `deanon_BFG_20260814_TEST/147903.1_8`)


S. wurde am 23. November 2021 (Nachuntersuchung) von Dr.in Dok1 untersucht und folgendes  Gutachten erstellt:  Anamnese:  VGA, 08/2016:  kombinierter Entwicklungsrückstand mit Intelligenzminderung – 50%   1 von 16 Seite 2 von 16

**False Positives:**

- `Dr.in Dok` — partial — pred is substring of gold: `Dr.in Dok1`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr.in Dok1`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/148398.1`) (sent_id: `deanon_BFG_20260814_TEST/148398.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Esra Mathiessen  in der Beschwerdesache Liliana Wientges,  Madlens 12, 2070 Obernalb, Österreich, über die Beschwerde vom 11. November 2019 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 15. Oktober 2019 betreffend  Grunderwerbsteuer 18.08.2014 Steuernummer 78-979/4818  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Dr.in Esra Mathiessen` — partial — pred is substring of gold: `Univ.-Prof.in Dr.in Esra Mathiessen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Esra Mathiessen`(person)
- `Liliana Wientges`(person)
- `Madlens 12, 2070 Obernalb, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `78-979/4818`(tax_number)

</details>

---

## `Ing_Title` 🏆

**F1:** 0.028 | **Precision:** 0.511 | **Recall:** 0.014  

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
| 0.511 | 0.014 | 0.028 | 45 | 23 | 22 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 23 | 22 | 1591 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch in der Beschwerdesache von Herrn Dipl.-Ing. Astrid Gänsl, Heimito von Doderer-Straße 8, 2100 Stetten, Österreich, über dessen Beschwerde vom 30. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 9. August 2021 betreffend Festsetzung eines ersten Säumniszuschlages in Höhe  von € 299,40 zu Steuernummer 74-872/6854  in der Sitzung am 16. Dezember 2021 in  Anwesenheit der Schriftführerin zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und der Säumniszuschlag mit  € 249,50 festgesetzt.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Astrid Gänsl` | `Dipl.-Ing. Astrid Gänsl` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Heimito von Doderer-Straße 8, 2100 Stetten, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `74-872/6854` (tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/135393.1`) (sent_id: `deanon_BFG_20260814_TEST/135393.1_4`)


Entscheidungsgründe  Mit Bescheid des Finanzamtes Österreich vom 9. August 2021 wurde über Herrn Dipl.-Ing. Astrid Gänsl  ein  erster Säumniszuschlag (für einen Betrag an Umsatzsteuer 2015 von € 14.970,00) in Höhe von  € 299,40 festgesetzt, da die angeführte Abgabenschuldigkeit nicht bis 15. Februar 2016  entrichtet worden sei.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Astrid Gänsl` | `Dipl.-Ing. Astrid Gänsl` |

**Missed by this rule (FN):**

- `Finanzamtes Österreich` (organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/136325.1`) (sent_id: `deanon_BFG_20260814_TEST/136325.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Dipl.-Ing. Jeanne Handke, Vornbacherweg 166, 5142 Weinberg, Österreich, über die Beschwerde vom 23. August 2021 gegen den Bescheid des Finanzamtes  Österreich vom 21. Juli 2021 betreffend Grunderwerbsteuer, Steuernummer 82-448/5450,  Erfassungsnummer 2017, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Jeanne Handke` | `Dipl.-Ing. Jeanne Handke` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Vornbacherweg 166, 5142 Weinberg, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `82-448/5450` (tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/140490.1`) (sent_id: `deanon_BFG_20260814_TEST/140490.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Gabriele Grossgut-Palotás in der  Beschwerdesache Dipl.-Ing. Milena Panagiotoglou, KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich, über die Beschwerde vom 11. September 2022  gegen den Bescheid des Finanzamtes Österreich vom 6. September 2022 betreffend  Einkommensteuer 2017 (Arbeitnehmerveranlagung) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Milena Panagiotoglou` | `Dipl.-Ing. Milena Panagiotoglou` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Gabriele Grossgut-Palotás` (person)
- `KLG Hackenberg Ährengruben 58, 3653 Weiten, Österreich` (address)
- `Finanzamtes Österreich` (organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/144771.1`) (sent_id: `deanon_BFG_20260814_TEST/144771.1_26`)


Der einzige Gesellschafter, Ing. Leonie Veix,  wohnhaft in Polen, war von der Gründung im Jahr 2013 bis zur Löschung gemäß § 40 FBG  infolge Vermögenslosigkeit der Geschäftsführer der Firma.

| Predicted | Gold |
|---|---|
| `Ing. Leonie Veix` | `Ing. Leonie Veix` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/145674.1`) (sent_id: `deanon_BFG_20260814_TEST/145674.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Vivian Gastell  in der Beschwerdesache Dipl.-Ing. Tosca Toussaint,  Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich, über die Beschwerde vom 12. Juni 2023 gegen den Bescheid des Finanzamtes  Österreich vom 25. Mai 2023 betreffend Abweisung des Antrags vom 6. Februar 2023 auf  Erstattung des Mehrkindzuschlages auf Grund der  Verhältnisse des Jahres 2022,  Steuernummer 82-564/6636, SV-Nr. Nr., zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO stattgegeben.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Tosca Toussaint` | `Dipl.-Ing. Tosca Toussaint` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Vivian Gastell` (person)
- `Laboratoriumstraße 204, 3243 Brandstatt bei Oed, Österreich` (address)
- `Finanzamtes  Österreich` (organisation)
- `82-564/6636` (tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Vorsitzenden des Finanzstrafsenates 6008-6  Mag. Johann Fischerlehner in der Finanzstrafsache gegen Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich, wegen  der Finanzvergehen der Abgabenhinterziehungen gemäß § 33 Abs. 2a des Finanzstrafgesetzes  (FinStrG) über die Beschwerden der Beschuldigten vom 22.09.2023 und der Amtsbeauftragten  vom 09.10.2023 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung -  Team als Finanzstrafbehörde vom 14.07.2023 beschlossen:  Das angefochtene Erkenntnis des Spruchsenates vom 14.07.2023, Gz., Team wird gemäß § 161  Abs. 4 FinStrG aufgehoben und die Finanzstrafsache in ihrem gesamten Umfang an die  Finanzstrafbehörde zur neuerlichen Entscheidung zurückverwiesen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Johann Fischerlehner` (person)
- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)
- `Amt für Betrugsbekämpfung` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_3`)


Begründung  Verfahrensgang:  Mit Beschluss des Bezirksgerichtes BG vom TT. Februar 2023 zu Aktenzeichen Az. wurde  betreffend Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  das Schuldenregulierungsverfahren eröffnet und  Dr. Harald POHLHAMMER, Herrenstraße 29/2.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)
- `Dr. Harald POHLHAMMER` (person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_5`)


Mit Vorladung vom 22. Juni 2023 zur mündlichen Verhandlung am 14.07.2023 um 08:30 Uhr  vor dem Spruchsenat des Amtes für Betrugsbekämpfung - Bereich Finanzstrafsachen - Team als  Finanzstrafbehörde wurde Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  als Beschuldigter geladen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Amtes für Betrugsbekämpfung` (organisation)
- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_7`)


Finanzstrafbehörde wurde die Fa. NB zu Handen Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  als  Nebenbeteiligte geladen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_8`)


Mit Eingangsdatum 14.07.2023 (Poststempel Finanzamt Österreich) ging von Rechtsanwalt  Dr. Harald Pohlhammer (Masseverwalter von Dipl.-Ing. Heinz Riechels) ein Schreiben samt Übermittlung von  2 RSa Briefen ein.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Finanzamt Österreich` (organisation)
- `Dr. Harald Pohlhammer` (person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_9`)


Demnach hätte Herr Dipl.-Ing. Heinz Riechels  trotz Aufforderung des Masseverwalters die  Post nicht beim Masseverwalter abgeholt. Beigeschlossen wurden die Vorladung des  Beschuldigten Dipl.-Ing. Heinz Riechels  zur Spruchsenatsverhandlung (RSa Brief) sowie die Vorladung des  Nebenbeteiligten NB zur Spruchsenatsverhandlung (RSa Brief).

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_11`)


Festgehalten wurde, dass bei Aufruf der Sache weder der Beschuldigte Dipl.-Ing. Heinz Riechels  noch der  beschuldigte Verband NB erschienen sind.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_14`)


Der Senatsvorsitzende hat in einem Vorhalt vom 14.3.2025 die belangte Behörde aufgefordert,  binnen von vier Wochen ab Zustellung dieses Schreibens folgende Unterlagen vorzulegen:   Ladung der beschuldigten Parteien zur mündlichen Verhandlung am 14.07.2023 samt  Zustellnachweis   Auszug aus der Insolvenzdatei betreffend Dipl.-Ing. Heinz Riechels, Fuchsloch 378, 5242 Schöfeck, Österreich  Weiters wurde die belangte Behörde aufgefordert folgende Passage in der schriftlichen  Ausfertigung des angefochtenen Staferkenntnisses  (Seite 7) näher zu erläutern:  „Die Zustellung der Ladung ist ausgewiesen durch persönliche Übernahme per 27.06.2023.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Fuchsloch 378, 5242 Schöfeck, Österreich` (address)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_20`)


Unterschrift auf der gegenständlichen Beschwerde:  [...]  Zudem ist auf der Verständigung von der Hinterlegung eine Nachsendeadresse angeführt, die  jener des damaligen Insolvenzverwalters Dr. Pohlhammer des Dipl.-Ing. Heinz Riechels  entspricht.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Dr. Pohlhammer` (person)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_22`)


Die Ladungen zur Spruchsenatsverhandlung an den Beschuldigten Dipl.-Ing. Heinz Riechels  und den  nebenbeteiligten Verband NB gingen It. Eingangsstempel auf den RSa Schreiben jeweils am  27. Juni 2023 beim Masseverwalter Dr. Pohlhammer ein.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Dr. Pohlhammer` (person)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_23`)


Offensichtlich wurde seitens des Spruchsenats die Tatsache, dass die Zustellung der Ladung zur  Spruchsenatsverhandlung an Dipl.-Ing. Heinz Riechels  nachweislich mittels Nachsendeauftrag an den  Masseverwalter erfolgte (siehe Nachsendeadresse links unten im Zustellnachweis der Ladung  an Dipl.-Ing. Heinz Riechels), nicht berücksichtigt und wurde daher im Glauben, dass die Ladung rechtmäßig  an den Beschuldigten ausgefolgt worden sei und dieser Kenntnis vom Verhandlungstermin  erlangt habe, die Spruchsenatsverhandlung in Abwesenheit des Beschuldigten Dipl.-Ing. Heinz Riechels  durchgeführt.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_24`)


Mit E-Mail vom 19.07.2023 wurde der Spruchsenatsvorsitzende Mag. Lichtenegger über das  Schreiben des Insolvenzverwalters Dr. Pohlhammer betreffend die nicht abgeholten  Spruchsenats-Vorladungen informiert und ihm das Schreiben übermittelt.  Über die Beschwerde wurde erwogen:  Festgestellter Sachverhalt:  Aus den vorgelegten und nunmehr auf Grund des Vorhaltes des Senatsvorsitzenden ergänzten  Akten ergibt sich zweifelsfrei, dass die Ladungen zur mündlichen Verhandlung am 14.07.2023  um 08:30 Uhr vor dem Spruchsenat des Amtes für Betrugsbekämpfung - Bereich  Finanzstrafsachen - Team als Finanzstrafbehörde weder dem Beschuldigten Dipl.-Ing. Heinz Riechels  noch  3 von 5 Seite 4 von 5

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Mag. Lichtenegger` (person)
- `Dr. Pohlhammer` (person)
- `Amtes für Betrugsbekämpfung` (organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_26`)


Trotz Verfügung der eigenhändigen  Zustellung wurden die Poststücke an den damaligen Masseverwalter des Dipl.-Ing. Heinz Riechels  übermittelt und sind dem Beschuldigten und der Nebenbeteiligten auch tatsächlich nicht  zugekommen.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/147840.1`) (sent_id: `deanon_BFG_20260814_TEST/147840.1_50`)


Im gegenständlichen Fall hat sich herausgestellt, dass die Ladungen zur mündlichen  Verhandlung am 14.07.2023 um 08:30 Uhr vor dem Spruchsenat des Amtes für  Betrugsbekämpfung - Bereich Finanzstrafsachen - Team als Finanzstrafbehörde weder dem  Beschuldigten Dipl.-Ing. Heinz Riechels  noch dem nebenbeteiligten Verband NB zugestellt wurden.

| Predicted | Gold |
|---|---|
| `Dipl.-Ing. Heinz Riechels` | `Dipl.-Ing. Heinz Riechels` |

**Missed by this rule (FN):**

- `Amtes für  Betrugsbekämpfung` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131710.1`) (sent_id: `deanon_BFG_20260814_TEST/131710.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  KommR Ing. Ludwig Taspinar, MA, Alt Lenzing 13, 4076 Karling, Österreich, über die Beschwerden vom 8. Oktober 2020 bzw. 13. November  2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 18. September 2020 bzw. 19.  Oktober 2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018 und 2019,  Steuernummer 09 801/8427,   I. beschlossen:  Der Vorlageantrag vom 14. Dezember 2020 wird, soweit er sich gegen die  Beschwerdevorentscheidung vom 19. Oktober 2020 betreffend das Jahr 2018  richtet, gemäß § 264 Abs 4 lit e iVm § 260 Abs 1 lit b BAO als verspätet  zurückgewiesen.

**False Positives:**

- `Ing. Ludwig Taspinar` — partial — pred is substring of gold: `KommR Ing. Ludwig Taspinar, MA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Siegfried Fenz`(person)
- `KommR Ing. Ludwig Taspinar, MA`(person)
- `Alt Lenzing 13, 4076 Karling, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/132393.1`) (sent_id: `deanon_BFG_20260814_TEST/132393.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Robert Pernegger über die Beschwerde  des StR Ing. Alexandra Ebermaier, MBA, Am Sturmberg 44, 4870 Mauracherberg, Österreich, vom 21. Jänner 2021, gegen die zwei  Zurückweisungsbescheide des Magistrates der Stadt Wien, Magistratsabteilung 67, beide vom  8. Jänner 2021, GZen 1) MA67/Zahl1/2020 und 2) MA67/Zahl2/2020, zu Recht erkannt:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und die  angefochtenen Zurückweisungsbescheide bestätigt.

**False Positives:**

- `Ing. Alexandra Ebermaier` — partial — pred is substring of gold: `StR Ing. Alexandra Ebermaier, MBA`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Robert Pernegger`(person)
- `StR Ing. Alexandra Ebermaier, MBA`(person)
- `Am Sturmberg 44, 4870 Mauracherberg, Österreich`(address)
- `Magistrates der Stadt Wien, Magistratsabteilung 67`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_8`)


Die Gesellschaftsanteile werden von Dipl. Ing.Ing. Bertram Hennlein und Dipl. Ing. B gehalten.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_9`)


Als  Geschäftsführer fungierte im Streitzeitraum Dipl. Ing.Ing. Bertram Hennlein  Im Zuge einer die Jahre 2015 bis 2019 umfassenden gemeinsamen Prüfung der Lohnabgaben  (GPLA) wurden folgende, nunmehr streitgegenständlichen Feststellungen getroffen:  1 von 17 Seite 2 von 17

**False Positives:**

- `Ing. Bertram Hennlein  Im Zuge` — positional overlap with gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_39`)


Ad Geschäftsführerbezug, Diäten und GSVG-Beiträge  Im Prüfungszeitraum sei Dipl. Ing.Ing. Bertram Hennlein als Geschäftsführer der Beschwerdeführerin und Dipl.  Ing. B als Prokurist tätig gewesen.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_42`)


Dipl. Ing. B sei täglich an den Standorten W sowie Z anwesend gewesen und habe sich operativ  um die Durchführung der Geschäftsführeragenden gekümmert, während Dipl. Ing.Ing. Bertram Hennlein in  diese Tätigkeiten so gut wie gar nicht eingebunden gewesen sei.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_45`)


Dipl. Ing.Ing. Bertram Hennlein sei nur selten an den Bürostandorten körperlich anwesend gewesen und habe  daher organisatorisch gar nicht die Durchführung der originären Tätigkeiten eines  Geschäftsführers übernehmen können.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_46`)


Die Entlohnung des Dipl. Ing.Ing. Bertram Hennlein betreffe daher  ausschließlich seine Tätigkeit für die oben angeführten Projekte, für die Grenzverhandlungen  und als Sachverständiger.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_57`)


Die operativen Tätigkeiten des Gesellschafter-Geschäftsführers Dipl. Ing.Ing. Bertram Hennlein hätten in der  Abwicklung der Projekte, in Grenzverhandlungen und im Tätigwerden als Sachverständiger  bestanden.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_60`)


In den Jahren 2014-2020 seien auch alle Jahresabschlüsse vom alleinigen  Gesellschafter-Geschäftsführers Dipl. Ing.Ing. Bertram Hennlein unterzeichnet worden.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_88`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   1.1. Bezüge des wesentlich beteiligten Gesellschafter-Geschäftsführers  Dipl. Ing.Ing. Bertram Hennlein ist zu 90% an der beschwerdeführenden Gesellschaft beteiligt und vertritt diese  seit 19.11.2010 selbständig als ihr Geschäftsführer.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing.Ing. Bertram Hennlein`(person)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138134.1`) (sent_id: `deanon_BFG_20260814_TEST/138134.1_91`)


Insgesamt flossen ihm in den  Streitjahren folgende Beträge zu:  2015 2016 2017 2018 2019  26.447,13 € 37.786,37 € 36.058,96 € 52.441,49 € 54.658,22 €  Dipl. Ing.Ing. Bertram Hennlein war für die Beschwerdeführerin einerseits als Sachverständiger tätig und  andererseits mit der Abwicklung des Projektgeschäftes (z.B. Semmering Basistunnel,  Bosrucktunnel, Sensorik-Anwendungen bei der ÖBB und ASFINAG) betraut.

**False Positives:**

- `Ing. Bertram Hennlein` — partial — pred is substring of gold: `Ing.Ing. Bertram Hennlein`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ing.Ing. Bertram Hennlein`(person)
- `ÖBB`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/138223.1`) (sent_id: `deanon_BFG_20260814_TEST/138223.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Diana Sammer über die Beschwerde von  Dipl.-Ing. KzlR Otto Thiesgen, Gränzing 2, 4841 Brunau, Österreich, vom 12. Juli 2022, gegen das Straferkenntnis des Magistrates der  Stadt Wien, Magistratsabteilung 67 vom 8. Juli 2022, Zahl MA67/Zahl1/2022, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF. LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird die Beschwerde als  unbegründet abgewiesen und das angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `Dipl.-Ing. Kzl` — partial — pred is substring of gold: `Dipl.-Ing. KzlR Otto Thiesgen`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Diana Sammer`(person)
- `Dipl.-Ing. KzlR Otto Thiesgen`(person)
- `Gränzing 2, 4841 Brunau, Österreich`(address)
- `Magistrates der  Stadt Wien, Magistratsabteilung 67`(organisation)
- `Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/142817.1`) (sent_id: `deanon_BFG_20260814_TEST/142817.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Hans Blasina, die Richterin  Mag. Monika Ahorn sowie die fachkundigen Laienrichter Gerald Cuny-Kreuzer und Dipl. Ing.  Thomas Hrdinka in der Beschwerdesache Fabian Kohnke, Hammersdorfstraße 78, 4223 Lungitz, Österreich, vertreten durch Intercura  Treuhand- und Revisionsgesellschaft m.b.H., Bösendorferstraße 2, 1010 Wien, über die  Beschwerde vom 14. Dezember 2018 gegen die Bescheide des Finanzamtes Wien 1/23 vom  16. November 2018 betreffend Haftung Lohnsteuer, Festsetzung Dienstgeberbeitrag und  Zuschlag zum Dienstgeberbeitrag sowie Säumniszuschläge jeweils 2015 bis 2017  (Steuernummer 14-263/3594 ) nach Durchführung einer mündlichen Verhandlung am  21. November 2023 in Anwesenheit der Schriftführerin Asli Özdemir zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ing.  Thomas Hrdinka` — partial — pred is substring of gold: `Dipl. Ing.  Thomas Hrdinka`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Mag. Monika Ahorn`(person)
- `Gerald Cuny-Kreuzer`(person)
- `Dipl. Ing.  Thomas Hrdinka`(person)
- `Fabian Kohnke`(person)
- `Hammersdorfstraße 78, 4223 Lungitz, Österreich`(address)
- `Intercura  Treuhand- und Revisionsgesellschaft m.b.H.`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `14-263/3594`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/145207.1`) (sent_id: `deanon_BFG_20260814_TEST/145207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Senatsvorsitzende Dr. Anna Radschek, die Richterin  Mag. Sonja Stradner sowie die fachkundigen Laienrichter Manfred Fiala und Dipl.Ing. Wolfgang  Weichselbraun in der Beschwerdesache Kira Lentze, In der Krems 35, 3500 Gneixendorf, Österreich, vertreten durch Woditschka  Steuerberatung GmbH, Lanzendorfer Hauptstraße 9 Tür 1, 2130 Mistelbach, über die  Beschwerde vom 23. Februar 2023 gegen den Bescheid des Finanzamtes Österreich vom  23. Jänner 2023 betreffend Zurückweisung des Antrags auf Durchführung der  Arbeitnehmerveranlagung 2017, Steuernummer 97-126/0015, nach Durchführung einer  mündlichen Verhandlung am 3. Juli 2024 in Anwesenheit der Schriftführerin Christina Seper zu  Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ing. Wolfgang  Weichselbraun` — partial — pred is substring of gold: `Dipl.Ing. Wolfgang  Weichselbraun`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Anna Radschek`(person)
- `Mag. Sonja Stradner`(person)
- `Manfred Fiala`(person)
- `Dipl.Ing. Wolfgang  Weichselbraun`(person)
- `Kira Lentze`(person)
- `In der Krems 35, 3500 Gneixendorf, Österreich`(address)
- `Woditschka  Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `97-126/0015`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/145343.1`) (sent_id: `deanon_BFG_20260814_TEST/145343.1_2`)


Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Ralf Schatzl, den Richter Mag.  Thomas Stieger sowie die fachkundigen Laienrichter Ing. Helmut Marchhart und Mag. Christian  Berger BA MSc LL.M. in der Beschwerdesache Franziskus Schymitzek, Gössering 48, 9314 St. Martin, Österreich, vertreten durch  KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Krassnigstr 36, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom 25. Oktober 2018  gegen die Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom  28. September 2018 betreffend Anspruchszinsen (§ 205 BAO) 2016 und Einkommensteuer  (Arbeitnehmerveranlagung) 2016 in der Sitzung am 5. Juli 2024 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ing. Helmut Marchhart` — partial — pred is substring of gold: `Laienrichter Ing. Helmut Marchhart`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ralf Schatzl`(person)
- `Mag.  Thomas Stieger`(person)
- `Laienrichter Ing. Helmut Marchhart`(person)
- `Mag. Christian  Berger BA MSc LL.M.`(person)
- `Franziskus Schymitzek`(person)
- `Gössering 48, 9314 St. Martin, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_4`)


Tatsächlich hat die Bf. die „Dipl.-Ing. KzlR Juri Strube“ mit der Vertretung beauftragt und diese auch im  Antrag auf Erstattung von Vorsteuern vom 20. Juni 2023 als Zustellungsbevollmächtigte  benannt.

**False Positives:**

- `Dipl.-Ing. Kzl` — partial — pred is substring of gold: `Dipl.-Ing. KzlR Juri Strube`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. KzlR Juri Strube`(person)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_5`)


Die dagegen von der Dipl.-Ing. KzlR Juri Strube  im Namen der Bf. erhobene Beschwerde vom 21. Dezember  2023 wurde mit Beschwerdevorentscheidung vom 22. März 2024 abgewiesen.

**False Positives:**

- `Dipl.-Ing. Kzl` — partial — pred is substring of gold: `Dipl.-Ing. KzlR Juri Strube`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. KzlR Juri Strube`(person)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_6`)


Am 23. Juli 2024  stellte die Dipl.-Ing. KzlR Juri Strube  im Namen der Bf. innerhalb verlängerter Frist den Antrag auf Vorlage  der Beschwerde an das BFG.

**False Positives:**

- `Dipl.-Ing. Kzl` — partial — pred is substring of gold: `Dipl.-Ing. KzlR Juri Strube`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. KzlR Juri Strube`(person)
- `BFG`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_15`)


Da der Bescheid im Beschwerdefall nicht an den tatsächlichen Zustellungsbevollmächtigten  „Dipl.-Ing. KzlR Juri Strube“, sondern die „Hemma Bödker“ adressiert war, vermag er für die Bf. keine  Rechtswirkung zu entfalten.

**False Positives:**

- `Dipl.-Ing. Kzl` — partial — pred is substring of gold: `Dipl.-Ing. KzlR Juri Strube`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.-Ing. KzlR Juri Strube`(person)
- `Hemma Bödker`(person)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_227`)


Seitens der Bf. wurde ein Privatgutachten von Dipl.Ing. Dr. H, anonymisiert aber mit RV-Zahl,  vorgelegt.

**False Positives:**

- `Ing. Dr` — partial — pred is substring of gold: `Dipl.Ing. Dr. H`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.Ing. Dr. H`(person)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/148677.1`) (sent_id: `deanon_BFG_20260814_TEST/148677.1_240`)


Bekannt sei, dass Dipl.Ing. Dr. H mehrere Gutachten erstellt habe.

**False Positives:**

- `Ing. Dr` — partial — pred is substring of gold: `Dipl.Ing. Dr. H`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dipl.Ing. Dr. H`(person)

</details>

---

## `OStR_Title` 

**F1:** 0.001 | **Precision:** 0.500 | **Recall:** 0.001  

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
| 0.500 | 0.001 | 0.001 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 1 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Lisa Pucher in der Beschwerdesache  OStR Richarda Schönwaldt, Erich-Opitz-Weg 32, 4742 Großpoxruck, Österreich, über die Beschwerde vom 21. Juli 2023 gegen den Bescheid des  Finanzamtes Österreich vom 6. Juli 2023 betreffend die Rückforderung von Familienbeihilfe  und Kinderabsetzbeträgen für den Zeitraum November 2022 bis Juni 2023 für das Kind  Heidemarie Fitzenreiter, verbunden mit der Rückforderung der aus der Kinderstaffel (§ 8 Abs 3 FLAG  1967) resultierenden anteiligen Familienbeihilfe für die Kinder Florens Meulenkamp  und  Sara Liebreich, zu Recht:    I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `OStR Richarda Schönwaldt` | `OStR Richarda Schönwaldt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Lisa Pucher` (person)
- `Erich-Opitz-Weg 32, 4742 Großpoxruck, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `Heidemarie Fitzenreiter` (person)
- `Florens Meulenkamp` (person)
- `Sara Liebreich` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/143793.1`) (sent_id: `deanon_BFG_20260814_TEST/143793.1_2`)


Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache   DDr. OStR Ernst Brücklmaier, Elsa Dvorak-Weg 19, 4202 Hochbuchedt, Österreich  vertreten durch Beste & Partner Steuerberatung GmbH,  Perlhofgasse 2/2/8, 2372 Gießhübl, betreffend Beschwerde vom 20. September 2021 gegen  die Bescheide des Finanzamtes für Großbetriebe vom 2. September 2021 betreffend  Wiederaufnahme § 303 BAO Körperschaftsteuer der Jahre 2014-2016 sowie Wiederaufnahme  Körperschaftsteuer für das Jahr 2018, Steuernummer 87-802/5730  beschlossen:  Die Beschwerde wird gemäß § 256 Abs. 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `OStR Ernst Brücklmaier` — partial — pred is substring of gold: `DDr. OStR Ernst Brücklmaier`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `DDr. OStR Ernst Brücklmaier`(person)
- `Elsa Dvorak-Weg 19, 4202 Hochbuchedt, Österreich`(address)
- `Beste & Partner Steuerberatung GmbH`(organisation)
- `Finanzamtes für Großbetriebe`(organisation)
- `87-802/5730`(tax_number)

</details>

---

## `M_Anonymized` 🏆

**F1:** 0.013 | **Precision:** 0.306 | **Recall:** 0.007  

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
| 0.306 | 0.007 | 0.013 | 36 | 11 | 25 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 11 | 25 | 1603 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_4`)


Entscheidungsgründe  Verfahrensgang:  Am 10.08.2018 stellte die Beschwerdeführerin (Bf.) M. P., geb. xxx1983, den (Eigen)Antrag auf  Gewährung des Erhöhungsbetrages zur Familienbeihilfe wegen erheblicher Behinderung ab  dem Zeitpunkt des Eintrittes der erheblichen Behinderung, den die/der medizinische  Sachverständige feststellt im Höchstausmaß von rückwirkend fünf Jahre ab Antragstellung  (somit August 2013).

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/129550.1`) (sent_id: `deanon_BFG_20260814_TEST/129550.1_176`)


Frau M. P. ist voraussichtlich nicht dauernd außerstande, sich selbst den Unterhalt zu  verschaffen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_87`)


Sozialanamnese:  Ausbildung: HAK-Matura, Untauglichkeit bei der Stellung 12/1980 (Nervosität, M. Schermann),  BWL-Studium nicht abgeschlossen, bisher keine Erwerbstätigkeit.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_92`)


Zusammenfassung relevanter Befunde (inkl. Datumsangabe):  1.12.1980, ärztlicher Befund der Stellungskommission Wien: Nervosität, Asthenie, M.  Scheuermann.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_16`)


M. hat viele eigene Spielideen  2018-12-07 Entwicklungsneurologische Untersuchung-Allgemeine Entwicklungsstörung, B  besucht Kindergarten ohne Stützkraft, zeichnet kritzelt, schaut Bücher an, großer  Entwicklungssprung, kommuniziert über verschiedene Gesten, Lautmalereien.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/133167.1`) (sent_id: `deanon_BFG_20260814_TEST/133167.1_124`)


Die anamnestischen Angaben bestätigen eine nur leicht verzögerte motorische Entwicklung in  den ersten 2 Lebensjahren, M. sei früh und schnell gekrabbelt, habe mit 20 Monaten die ersten  freien Schritte gemacht und sei mit 23Mo längere Strecken frei gegangen.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/137637.1`) (sent_id: `deanon_BFG_20260814_TEST/137637.1_50`)


Diese Auffassung wird im Übrigen auch durch die französische Fassung als eine der beiden  Originalfassungen des OECD-Musterabkommens (vgl. zur Bedeutung der Sprachfassungen  Lang, The Interpretation of Tax Treaties and Authentic Languages, in Guglielmo Maisto, Angelo  Nikolakakis and John M. Ulmer, eds., Essays on Tax Treaties: A Tribute to David A. Ward, 2013,  15, 17, sowie Vogel, Doppelbesteuerungsabkommen5, 2008, Einl.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Missed by this rule (FN):**

- `OECD` (organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/138214.1`) (sent_id: `deanon_BFG_20260814_TEST/138214.1_40`)


Bei den vorgelegten Unterlagen handelt es sich einerseits um Mietverträge und andererseits  um Schreiben des Herrn DI J M.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_372`)


kein ÖGK-Kostenersatz oder sonstiger Nachweis der medizinischen Notwendigkeit iSd  VwGH-Judikatur;   - 742,- € M. M. für Physiotherapie/Heilmassage/osteopath.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |
| `M.` | `M.` |

**Missed by this rule (FN):**

- `ÖGK` (organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_377`)


Die Voraussetzungen für einen Abzug von Kosten des Herrn M. als außergewöhnliche  Belastung im Jahr 2018 liegen insgesamt nicht vor.

| Predicted | Gold |
|---|---|
| `M.` | `M.` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

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

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `PhD Mag. Heinrich Hambücher`(person)
- `Schlaitenerstraße 65, 9173 Freibach, Österreich`(address)
- `Prof.Dr. Thomas Keppert,  Steuerberatung- und Wirtschaftsprüfung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden Dr. Hans Blasina sowie die weiteren  Senatsmitglieder Dr. Sebastian Pfeiffer, LL.M., Gerald Cuny-Kreuzer sowie Dr. Franz Kandlhofer  in der Beschwerdesache Christina Tiebout, Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich, vertreten durch Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse 1 Tür Freyung, 1010 Wien, über die Beschwerde vom  15. September 2020 gegen die Bescheide des Finanzamtes Wien 1/23 vom 20. August 2020  betreffend Feststellungsbescheid Gruppenträger 2014, Feststellungsbescheid Gruppenträger  2015, Feststellungsbescheid Gruppenträger 2016 und Feststellungsbescheid Gruppenträger  2017   I. beschlossen:  Die Beschwerden hinsichtlich Feststellungsbescheid Gruppenträger 2014 und 2015  werden gemäß § 278 Abs. 1 lit. b BAO iVm § 256 Abs. 3 BAO als gegenstandslos  erklärt.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Dr. Sebastian Pfeiffer, LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Hans Blasina`(person)
- `Dr. Sebastian Pfeiffer, LL.M.`(person)
- `Gerald Cuny-Kreuzer`(person)
- `Dr. Franz Kandlhofer`(person)
- `Christina Tiebout`(person)
- `Hafnerplatz 17, 3465 Königsbrunn am Wagram, Österreich`(address)
- `Deloitte Tax  Wirtschaftsprüfungs GmbH`(organisation)
- `Finanzamtes Wien 1/23`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Rechtssache Romana Stavrakis, Untersameting 4, 4894 Römerhof, Österreich, vertreten durch KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft, Porzellangasse 51, 1090 Wien, über die  Beschwerde vom 04. Mai 2016 gegen den Bescheid des Finanzamtes Österreich vom 28. April  2016 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 nach Durchführung einer  öffentlichen mündlichen Verhandlung am 07.04.2021 zu Recht erkannt:   1.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Romana Stavrakis`(person)
- `Untersameting 4, 4894 Römerhof, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH  Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_61`)


Während einer dieser Ausreisen lernte der Bf. am xx.xx.2015 in Phuket  (Thailand) die am xx.xx.xxxx geborene thailändische Staatsbürgerin, M.M., kennen, die in der  Folge zeitweise auch mit dem Bf. gemeinsam im vorgenannten Apartement in MYS lebte.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_63`)


M.M. besuchte den Bf. insgesamt 3 Mal in Österreich (2 Besuche im Jahr 2016, 1 Besuch im  Rahmen ihrer Vernehmung vor dem erkennenden Gericht).

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_93`)


Übereinstimmend gaben sowohl er als auch die Zeugin M.M. weiters an, sich im Zuge einer  dieser Ausreisen am xx.xx.2015 in Phuket kennengelernt zu haben.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_96`)


Dass die Zeugin M.M. den Bf. insgesamt dreimal in Österreich, und er die Zeugin viermal nach  dem Entsendungsende in Thailand besuchte, geht einerseits aus den diversen Einreisestempel  im Reisepass des Bf. bzw. den diesbezüglichen Ausführungen der Zeugin hervor.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_118`)


Schlussendlich führte die Zeugin M.M. auf die Frage, was mit dem Zimmer im Haus  der Mutter bei Auslandsaufenthalten des Bf. passiere aus, wie folgt: „Bei Auslandsaufenthalten  meines Mannes bleibt dieses Zimmer in Untersameting 4, 4894 Römerhof, Österreich  unbenützt.“ (ZV M.M., VH-Protokoll S.  3)

**False Positives:**

- `M.` — no gold match — likely missing annotation
- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Untersameting 4, 4894 Römerhof, Österreich`(address)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_119`)


Dass der Bf.    auch heute noch davon ausgeht, nicht im Haus der Mutter wohnhaft zu sein, für den  Bezug des Arbeitslosengeldes ab 2016 aber deren Adresse unter dem Antragspunkt  „ordentlicher Wohnsitz“ angab,    im Streitjahr in Malaysien als nicht steueransässig behandelt und bis Juli 2015 dort  weder über eine Aufenthalts- noch eine Arbeitsbewilligung verfügte,    die Zeugin M.M. erst im Jahr 2015 kennenlernte und schließlich   lediglich 2 Koffer mit Kleidung nach Malaysien mitgenommen hat,  runden das Bild, wonach die Verantwortung des Bf. im Zusammenhang mit der  Wohnsitzaufgabe im Inland unglaubwürdig ist, ab.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/132815.1`) (sent_id: `deanon_BFG_20260814_TEST/132815.1_126`)


Diese Verantwortung erweist sich auch deshalb als wenig glaubhaft, als im  Gegensatz dazu die Zeugin M.M. zu diesem Beweisthema genau das Gegenteil ausführte (ZV  M.M., VH-Protokoll S. 3: „Mein Mann bzw. mein Freund hat einen Schlüssel für das Haus, ich  selbst habe keinen Schlüssel, weil ich nie alleine herumfahre.“).

**False Positives:**

- `M.` — no gold match — likely missing annotation
- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/138391.1`) (sent_id: `deanon_BFG_20260814_TEST/138391.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Richarda Blatzer, Rolfis 18, 5144 Feichten, Österreich, wegen behaupteter Verletzung der  Entscheidungspflicht des Finanzamtes Österreich betreffend die Erlassung eines  Einkommensteuerbescheides für das Veranlagungsjahr 2021 (Steuernummer 32-825/9727  ) beschlossen:   I. Die Säumnisbeschwerde vom 02.09.2022 wird gemäß § 260 Abs. 1 lit. a iVm § 284  Abs. 7 lit. b BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Richarda Blatzer`(person)
- `Rolfis 18, 5144 Feichten, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `32-825/9727`(tax_number)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Delila Frenski, Bairbach 31, 4892 Saxigen, Österreich, vertreten durch Mag. Gottfried Tazol,  Hauptplatz 24, 9100 Völkermarkt, über die Beschwerde vom 28. Dezember 2020 gegen die  Bescheide des Finanzamtes Österreich je vom 27. November 2020 betreffend  Wiederaufnahme der Verfahren Einkommensteuer 2014-2018 und Einkommensteuer  (ArbeitnehmerInnenveranlagung) 2014-2019 (Steuernummer 19-849/6261 ) zu Recht  erkannt:  I. BESCHLUSS  1.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Delila Frenski`(person)
- `Bairbach 31, 4892 Saxigen, Österreich`(address)
- `Mag. Gottfried Tazol`(person)
- `Finanzamtes Österreich`(organisation)
- `19-849/6261`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache DDr. Ali Franzel, Oberwirtsweg 5, 8562 Bubendorf, Österreich, über die Beschwerde vom 13. Juli 2021 gegen  den Bescheid des Finanzamtes Österreich vom 29. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, Steuernummer 63-470/7314  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. David Hell LL.B. LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `DDr. Ali Franzel`(person)
- `Oberwirtsweg 5, 8562 Bubendorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `63-470/7314`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/139691.1`) (sent_id: `deanon_BFG_20260814_TEST/139691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Ronja Oberth, LLM, Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich, vertreten durch Hofer Leitinger Steuerberatung  GmbH, Hauptstraße 86, 8582 Rosental/Kainach, über die Beschwerde vom 24. Juni 2022 gegen  den Bescheid des Finanzamtes Österreich vom 1. Juni 2022 betreffend Einkommensteuer 2020  (Steuernummer 59-245/3703 ) zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Ulrike Nussbaumer LL.M. M.B.L.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Ronja Oberth, LLM`(person)
- `Oberer Gleggenweg 1, 9555 Unterglanegg, Österreich`(address)
- `Hofer Leitinger Steuerberatung  GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `59-245/3703`(tax_number)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/140422.1`) (sent_id: `deanon_BFG_20260814_TEST/140422.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Klara Biallowons, Höslrein 65, 3470 Oberstockstall, Österreich, vertreten durch UnionTAX & LAW, Donau-City- Straße 7/DC Tower/30th Floor, 1220 Wien, betreffend Säumnisbeschwerde vom 10.2.2023  wegen Verletzung der Entscheidungspflicht hinsichtlich Arbeitnehmerveranlagung 2018 und  2019 durch das Finanzamt Österreich zur Sozialversicherungsnummer 5116 301100  beschlossen:  I. Die Säumnisbeschwerde gilt gemäß § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Klara Biallowons`(person)
- `Höslrein 65, 3470 Oberstockstall, Österreich`(address)
- `Finanzamt Österreich`(organisation)
- `5116 301100`(social_security_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/142740.1`) (sent_id: `deanon_BFG_20260814_TEST/142740.1_21`)


Familienbeihilfe steht bei einer ernsthaften und zielstrebigen Ausbildung zu.   Wann gilt die Ausbildung als ernsthaft und zielstrebig?   • Das Kind verwendet die volle Zeit dafür   • Das Kind tritt in angemessener Zeit zu Prüfungen an   Bei Ihrem Kind trifft das nicht zu.   Aus dem vorgelegten Abschlussbericht des AMS Niederösterreich ist ersichtlich, dass Ihr Sohn  M... in der Zeit der Ausbildung von 17.5.2021 bis 30.07.2021 aufgrund "wiederkehrender  Krankenstände die erforderlichen Anwesenheiten nicht erfüllt hat und der Kurs daher  abgebrochen wurde" -- Zitat.

**False Positives:**

- `M.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `AMS`(organisation)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/143184.1`) (sent_id: `deanon_BFG_20260814_TEST/143184.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Volkmar Bauernschmid, MBA, Lohenstein Straße 3, 3553 Mittelbergeramt, Österreich  vertreten durch Securitas Revisions- und  Treuhandgesellschaft m.b.H., Porzellangasse 51, 1090 Wien und Deloitte Tax  Wirtschaftsprüfungs GmbH, Renngasse/Freyung 1, 1013 Wien, über die Beschwerde vom 19.  Mai 2021 gegen die Bescheide des Finanzamtes für Großbetriebe je vom 25. März 2021 die  Umsatzsteuer 2012-2014 betreffend (Steuernummer 78-200/9325) nach Durchführung  einer mündlichen Verhandlung am 24. November 2023 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag.a Ulrike Nussbaumer LL.M. M.B.L.`

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

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_57`)


8. Mit Eingabe vom 7.8.2017 brachte die Bf wiederum vor, die Gebührenerhebung sei  unionsrechtswidrig, und legte ein "Gutachten zur unionsrechtlichen Zulässigkeit bestimmter  österreichischer Meldemodalitäten für ausländische Skischulbetreiber im Rahmen des  Ausflugsverkehrs" des Prof. Dr. YY, LL.M., vom 24.7.2017 vor, welches dieser im Auftrag des  Deutschen Skilehrerverbandes e.V. erstellt hatte.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Prof. Dr. YY, LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Dr. YY, LL.M.`(person)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/145343.1`) (sent_id: `deanon_BFG_20260814_TEST/145343.1_2`)


Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Ralf Schatzl, den Richter Mag.  Thomas Stieger sowie die fachkundigen Laienrichter Ing. Helmut Marchhart und Mag. Christian  Berger BA MSc LL.M. in der Beschwerdesache Franziskus Schymitzek, Gössering 48, 9314 St. Martin, Österreich, vertreten durch  KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Krassnigstr 36, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom 25. Oktober 2018  gegen die Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom  28. September 2018 betreffend Anspruchszinsen (§ 205 BAO) 2016 und Einkommensteuer  (Arbeitnehmerveranlagung) 2016 in der Sitzung am 5. Juli 2024 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Christian  Berger BA MSc LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ralf Schatzl`(person)
- `Mag.  Thomas Stieger`(person)
- `Laienrichter Ing. Helmut Marchhart`(person)
- `Mag. Christian  Berger BA MSc LL.M.`(person)
- `Franziskus Schymitzek`(person)
- `Gössering 48, 9314 St. Martin, Österreich`(address)
- `KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft`(organisation)
- `Finanzamtes Wien 1/23`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/145862.1`) (sent_id: `deanon_BFG_20260814_TEST/145862.1_1`)


VERSTÄNDIGUNG  Das Bundesfinanzgericht teilt durch den Richter Mag. David Hell LL.B. LL.M. in der Beschwerde- sache Geraldine Loeper, Bakk. techn., Südstraße 6, 6471 Leins, Österreich, zur Beschwerde vom 20. November 2023 gegen den  Bescheid des Finanzamtes Österreich vom 9. November 2023 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2022, Steuernummer 16-579/1693, mit:  Nach Auffassung des Bundesfinanzgerichts wurde in Bezug auf die Beschwerde- vorentscheidung vom 15. Jänner 2024 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) für das Jahr 2022 kein Vorlageantrag eingebracht.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. David Hell LL.B. LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `Geraldine Loeper, Bakk. techn.`(person)
- `Südstraße 6, 6471 Leins, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `16-579/1693`(tax_number)
- `Bundesfinanzgerichts`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/146743.1`) (sent_id: `deanon_BFG_20260814_TEST/146743.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Markus Knechtl LL.M. in der  Beschwerdesache Priv.-Doz. Priv.-Doz. Urs Heinatzky, Feldpichl 19, 8130 Peggau, Österreich, vertreten durch Mag. Beatrix Anna Elfriede  Reiff-Zehetner, Straße der Menschenrechte 11, 2103 Langenzersdorf, über die Beschwerde  vom 30. August 2023 gegen den Bescheid des Finanzamtes Österreich vom 31. Juli 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2022 zur Steuernummer  51-583/1758  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. Markus Knechtl LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Markus Knechtl LL.M.`(person)
- `Priv.-Doz. Priv.-Doz. Urs Heinatzky`(person)
- `Feldpichl 19, 8130 Peggau, Österreich`(address)
- `Mag. Beatrix Anna Elfriede  Reiff-Zehetner`(person)
- `Finanzamtes Österreich`(organisation)
- `51-583/1758`(tax_number)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/149829.1`) (sent_id: `deanon_BFG_20260814_TEST/149829.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache Lothar Kriwet, Gaugen 11, 9150 Draurain, Österreich, vertreten durch Spiss Steuerberatung GmbH,  Timmlerweg 16, 6580 St. Anton am Arlberg, über die Beschwerde vom 31. Oktober 2025 gegen  die Bescheide des Finanzamtes Österreich vom 15. Oktober 2025 betreffend   1. Verzinsung gemäß § 16 COFAG-NoAG (Fixkostenzuschuss I),  2.

**False Positives:**

- `M.` — partial — pred is substring of gold: `Mag. David Hell LL.B. LL.M.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `Lothar Kriwet`(person)
- `Gaugen 11, 9150 Draurain, Österreich`(address)
- `Spiss Steuerberatung GmbH`(organisation)
- `Finanzamtes Österreich`(organisation)

</details>

---

## `Durch_Richter_Name` 

**F1:** 0.001 | **Precision:** 0.111 | **Recall:** 0.001  

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
| 0.111 | 0.001 | 0.001 | 9 | 1 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 8 | 1613 |

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

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/131701.1`) (sent_id: `deanon_BFG_20260814_TEST/131701.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Elisabeth Sarigiannis,  Klesenza 7, 9587 Erlendorf, Österreich, vertreten durch gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH,  Lehmanngasse 7, 1230 Wien, über die Beschwerden vom 18. Dezember 2012 gegen die  Bescheide des Finanzamtes Österreich vom 21. November 2012 betreffend Einkommensteuer  2007 bis 2011, Steuernummer 84-729/8666, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Elisabeth Sarigiannis`(person)
- `Klesenza 7, 9587 Erlendorf, Österreich`(address)
- `gkr Wirtschaft-Steuer-Recht SteuerberatungsgesellschaftmbH`(organisation)
- `Finanzamtes Österreich`(organisation)
- `84-729/8666`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Ri in der Beschwerdesache Holger Buchmüller,  Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich, betreffend Beschwerde vom 5. Februar 2019 gegen den Bescheid des  Finanzamtes Salzburg-Land (nunmehr Finanzamt Österreich) vom 22. Jänner 2019 betreffend  Einkommensteuer 2017 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit.b BAO als nicht fristgerecht eingebracht  zurückgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Holger Buchmüller`(person)
- `Adolf-Kolping-Gasse 45, 3441 Ranzelsdorf, Österreich`(address)
- `Finanzamtes Salzburg-Land`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/139780.1`) (sent_id: `deanon_BFG_20260814_TEST/139780.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Sheila Mathusczyk, Achatzeweg 10, 5272 Mitterdorf, Österreich, über die Beschwerde vom 15. Juni 2015 gegen den Bescheid des Finanzamtes  Salzburg-Land vom 8. Juni 2015 betreffend Haftungsbescheid /  Lohnsteuer 2012 und 2013  Steuernummer 71-776/4123  zu Recht erkannt:   I. Die Beschwerde gegen den Haftungsbescheid/Lohnsteuer 2012 wird als  unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Sheila Mathusczyk`(person)
- `Achatzeweg 10, 5272 Mitterdorf, Österreich`(address)
- `Finanzamtes`(organisation)
- `71-776/4123`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/140202.1`) (sent_id: `deanon_BFG_20260814_TEST/140202.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Anneliese Lorrek, Unteres Pieslwang 34, 9423 Hofwiesen, Österreich, betreffend Beschwerde vom 22. Mai 2015 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 27. April 2015 betreffend Anspruchszinsen (§ 205 BAO) 2012  Steuernummer 69-743/7981  beschlossen:  Der Vorlageantrag vom 3. August 2015 wird gemäß § 278 Abs. 1 lit. a BAO iVm den §§ 260 Abs.  1 lit. a, 264 Abs. 4 lit. e und 264 Abs. 5 BAO als unzulässig zurückgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Anneliese Lorrek`(person)
- `Unteres Pieslwang 34, 9423 Hofwiesen, Österreich`(address)
- `Finanzamtes`(organisation)
- `69-743/7981`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/140622.1`) (sent_id: `deanon_BFG_20260814_TEST/140622.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Bodo Adamovic, Bakk. phil., Gantschenbergstraße 24, 4204 Affenberg, Österreich, betreffend Beschwerde vom 22. Mai 2015 gegen den Bescheid des Finanzamtes  Hollabrunn Korneuburg Tulln vom 27. April 2015 betreffend Einkommensteuer 2012  Steuernummer 49-425/9978  beschlossen:  Die Beschwerde wird gemäß § 261 Abs. 2 BAO als gegenstandslos erklärt.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Bodo Adamovic, Bakk. phil.`(person)
- `Gantschenbergstraße 24, 4204 Affenberg, Österreich`(address)
- `Finanzamtes`(organisation)
- `49-425/9978`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/140816.1`) (sent_id: `deanon_BFG_20260814_TEST/140816.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Lee Joser, Schafwiesenstraße 6, 8443 Goldes, Österreich, vertreten durch Mag. Antonius Falkner Rechtsanwalt GmbH, Barwies 329, 6414  Mieming, über die Beschwerde vom 23. Dezember 2019 gegen den Bescheid des Zollamtes  Feldkirch Wolfurt vom 26. November 2019 betreffend Sicherheitsleistung zur Zollabgabe,  Einfuhrumsatzsteuer und Verzugszinsen zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Lee Joser`(person)
- `Schafwiesenstraße 6, 8443 Goldes, Österreich`(address)
- `Mag. Antonius Falkner Rechtsanwalt GmbH,`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Quentin Schwartkopp, Oggau-Grünland 4, 9462 Weitenbach, Österreich, über die Beschwerde vom 11.3.2019 gegen die Bescheide des Zollamtes Innsbruck  vom 20. Februar 2019 betreffend Berichtigung der Abfindungsanmeldungen Nr. xxxx/01 und  gggg/2016, Festsetzung der Alkoholsteuer für 2016 (800000/cccc);

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Quentin Schwartkopp`(person)
- `Oggau-Grünland 4, 9462 Weitenbach, Österreich`(address)
- `Zollamtes Innsbruck`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/142557.1`) (sent_id: `deanon_BFG_20260814_TEST/142557.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Ri in der Beschwerdesache Arnold Ulmke, Mazellegasse 14, 2870 Stübegg, Österreich, vertreten durch Steuerberatung, Adresse Steuerberatung, über die Beschwerde vom  17. November 2014 gegen die Bescheide des Finanzamtes St. Johann Tamsweg Zell am See  vom 20. Oktober 2014 betreffend Dienstgeberbeitrag 2009 - 2012 und Zuschlag zum  Dienstgeberbeitrag 2009 - 2012, Steuernummer 26-962/7724  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Ri` — similar text (different position): `Bundesfinanzgericht`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Arnold Ulmke`(person)
- `Mazellegasse 14, 2870 Stübegg, Österreich`(address)
- `Finanzamtes St. Johann Tamsweg Zell`(organisation)
- `26-962/7724`(tax_number)

</details>

---

## `Antragsteller_Name` 💣

**F1:** 0.001 | **Precision:** 0.023 | **Recall:** 0.001  

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
| 0.023 | 0.001 | 0.001 | 43 | 1 | 42 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 1 | 42 | 1613 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/147944.1`) (sent_id: `deanon_BFG_20260814_TEST/147944.1_29`)


Über die Beschwerde wurde erwogen:  Sachverhalt:  Gegen die an Herrn M als Beschuldigten gerichtete Strafverfügung vom 3. September 2024,  GZ. MA67/GZ/2024, erhob mit E-Mail vom 10. September 2024 der nunmehrige  Beschwerdeführer (Pjotr Niessl) fristgerecht Einspruch.

| Predicted | Gold |
|---|---|
| `Pjotr Niessl` | `Pjotr Niessl` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/128746.1`) (sent_id: `deanon_BFG_20260814_TEST/128746.1_4`)


I. Verfahrensgang und Sachverhalt  Im Zuge der Arbeitnehmerveranlagung für das Jahr 2016 beantragte die Beschwerdeführerin  (Bf), Grabsteinkosten für ihren verstorbenen Ehegatten in Höhe von € 9.740,00 als  außergewöhnliche Belastung (ag.B.) steuerlich anzuerkennen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) Siegfried Basyurt, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Siegfried Basyurt`(person)
- `Finanzamt`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_72`)


Dazu wurde in der Berufungsschrift ua. ausgeführt, dass das Fahrzeug der  Berufungswerberin/nunmehr Beschwerdeführerin (Bf) Siegfried Basyurt  nur dann gelegentlich im  Inland zur Verwendung zur Verfügung gestanden habe, wenn sich der Ehegatte (als  Leasingnehmer des Pkw) in Österreich aufgehalten habe.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Siegfried Basyurt`(person)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129511.1`) (sent_id: `deanon_BFG_20260814_TEST/129511.1_5`)


Entscheidungsgründe  I. Verfahrensgang  In der Einkommensteuererklärung beantragte der Beschwerdeführer (Bf) unter anderem  Werbungskosten für Familienheimfahrten im Ausmaß von 1.836 Euro und die Behandlung als  unbeschränkt Steuerpflichtiger (§ 1 Abs 4 EStG).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/130681.1`) (sent_id: `deanon_BFG_20260814_TEST/130681.1_4`)


Entscheidungsgründe  Die Beschwerdeführerin (Bf) beantragte in ihrer Einkommensteuererklärung für 2017 (ANV) die  Anerkennung von katastrophenbedingten Aufwendungen iHv 1.487,59 € als außergewöhnliche  Belastung (§ 34 Abs. 6 erster Teilstrich EStG 1988).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/130986.1`) (sent_id: `deanon_BFG_20260814_TEST/130986.1_6`)


Entscheidungsgründe  I. Verfahrensgang  Bei dem in den Beschwerdejahren bei der Firma AG als Kellner beschäftigten  Beschwerdeführer (Bf) nahm das Finanzamt unter Zugrundelegung der übermittelten  Lohnzettel die Arbeitnehmerveranlagungen 2010 bis 2014 vor.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131090.1`) (sent_id: `deanon_BFG_20260814_TEST/131090.1_4`)


Entscheidungsgründe  Strittig ist im anhängigen Verfahren die Zulässigkeit der vom Beschwerdeführer (Bf) mit  Eingabe an das Finanzamt X (FA) vom 6.April 2020 beantragten Korrektur des  Einkommensteuer- (ESt-) Bescheides 2010 vom 16.Mai 2014 im Rahmen einer  Wiederaufnahme gemäß § 303 Abs. 1 BAO.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/132291.1`) (sent_id: `deanon_BFG_20260814_TEST/132291.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Strittig ist im vorliegenden Fall die Frage, ob die Aufwendungen der Beschwerdeführerin (Bf)  für Fahrten zu ihren pflegebedürftigen Eltern ins Waldviertel Werbungskosten darstellen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/132712.1`) (sent_id: `deanon_BFG_20260814_TEST/132712.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf) begehrte mit Antrag vom 25.03.2020, beim Finanzamt (FA)  eingebracht am 26.03.2020, die Zuerkennung der Familienbeihilfe ab dem Zeitpunkt „sobald es  möglich ist“, für ihre Tochter, To (geb. am 1998).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/132897.1`) (sent_id: `deanon_BFG_20260814_TEST/132897.1_3`)


Begründung  I. Verfahrenslauf und Sachverhalt  Mit Bescheid vom 22.01.2019 wurde der Beschwerdeführer (Bf) zur Einkommensteuer 2017  veranlagt, da er während des Jahres von mehreren ausbezahlenden Stellen Bezüge erhalten  hatte.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/133483.1`) (sent_id: `deanon_BFG_20260814_TEST/133483.1_4`)


Entscheidungsgründe  Verfahrensgang  Im Zuge einer GPLA stellte der Prüfer fest, dass über Auftrag des AMS von der  Beschwerdeführerin (Bf) Migranten als Lehrlinge in Deutsch unterrichtet wurden und auf eine  Lehrstelle in einem Betrieb vorbereitet wurden.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `AMS`(organisation)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/135451.1`) (sent_id: `deanon_BFG_20260814_TEST/135451.1_4`)


Begründung  Mit Bescheid des Finanzamt Innsbruck  vom 29. März 2021 wurde die Einkommensteuer 2020 gegenüber  der Beschwerdeführerin (Bf) festgesetzt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Innsbruck`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/135866.1`) (sent_id: `deanon_BFG_20260814_TEST/135866.1_3`)


Entscheidungsgründe  Der Beschwerdeführer (Bf) erzielt Einkünfte aus Vermietung und Verpachtung.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/135960.1`) (sent_id: `deanon_BFG_20260814_TEST/135960.1_38`)


Zusätzlich wurde in der Beschwerde im Falle einer Abweisung der Beschwerde gegen die  Wiederaufnahmebescheide betreffend die Einkommensteuer für die Jahre 2015-2018 (2018  richtigerweise Aufhebungsbescheid) begehrt, dass bei den Sachbescheiden Einkommensteuer  2015-2018 vom Beschwerdeführer (Vermieter) getragene Betriebskosten, wie Grundsteuer,  Hausversicherung und Reparaturfonds, erstmals als Werbungskosten berücksichtigt werden  sollten.

**False Positives:**

- `Vermieter` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/136106.1`) (sent_id: `deanon_BFG_20260814_TEST/136106.1_4`)


Laut Bescheidspruch sollte das Guthaben nach Aufrechnung mit allfälligen  Abgabenrückständen auf das Girokonto der Beschwerdeführerin (Bf) überwiesen werden.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/137084.1`) (sent_id: `deanon_BFG_20260814_TEST/137084.1_6`)


Im Rahmen des Veranlagungsverfahrens wurde die Beschwerdeführerin (Bf) mit  Ergänzungsauftrag vom 10.02.2020 bzw. vom 04.03.2020 aufgefordert, weitere Nachweise  (Rechnungen, Bezeichnung der Aufwendungen, Einzelpreise und Summe über alle  Aufwendungen, ärztliche Verordnung, erhaltende Ersätze durch Krankenkasse…) für die  beantragte außergewöhnliche Belastung (ag. B., Lerntherapiekosten) nachzubringen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_4`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang:  Die Beschwerdeführerin (Bf), eine in Tschechien wohnhafte tschechische Staatsbürgerin,  erzielte im Streitjahr 2019 in Österreich Einkünfte aus nichtselbständiger Arbeit.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/137400.1`) (sent_id: `deanon_BFG_20260814_TEST/137400.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Die Beschwerdeführerin (Bf) stellte mit Schreiben vom 27.12.2017, eingelangt beim Magistrat  der Stadt Wien am 2.1.2018, den Antrag, die Vergnügungssteuer für den Zeitraum vom  1.1.2012 bis 31.12.2015 bescheidmäßig festzusetzen, da die Bf die Rechtsansicht vertrete, dass  es aufgrund der Kollision der Rechtsnormen Glücksspielgesetz und dem Gesetz über die  Besteuerung von Vergnügen im Gebiet der Stadt Wien (Vergnügungssteuergesetz 2005) zu  einer Doppelbesteuerung komme.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat  der Stadt Wien`(organisation)
- `Stadt Wien`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_3`)


Begründung  Der Beschwerdeführer (Bf) wurde mit Urteil des Landesgerichts Salzburg vom Zahl, Datum  unter anderem schuldig gesprochen, zur Abgabenhinterziehung nach § 33 Abs 1 FinStrG und  nach § 33 Abs 2 lit a FinStrG der S. zur Steuernummer Nummer in Bezug auf die  Kapitalertragsteuer für die Jahre 2010 (€ 229,06), 2011 (€ 112,16), 2012 (€ 152,44) und 2014  (740,44), somit in Höhe von gesamt € 1.234,44 beigetragen zu haben.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Landesgerichts`(organisation)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/138362.1`) (sent_id: `deanon_BFG_20260814_TEST/138362.1_6`)


Dieser Frage ging nachstehendes Verwaltungsgeschehen voran:  Der Beschwerdeführer (Bf) reichte die Erklärung zur Duchführung der  Arbeitnehmerveranlagung ein und beantragte darin die Berücksichtigung des Familienbonus  Plus für ein Kind, den Alleinverdienerabsetzbetrag und Werbungskosten für  Familienheimfahrten.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/138674.1`) (sent_id: `deanon_BFG_20260814_TEST/138674.1_3`)


Begründung  1. Festgestellter Sachverhalt:  Am 12.11.2022 brachte der Beschwerdeführer (Bf) über FinanzOnline eine Säumnisbeschwerde  beim Finanzamt ein.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/138325.1`) (sent_id: `deanon_BFG_20260814_TEST/138325.1_28`)


Im anhängigen Verfahren ist zu klären, ob die vom Beschwerdeführer (Bf) im Zeitraum  2000 - 2010 durchgeführte Bewirtschaftung seines Immobilienbesitzes im südweststeirischen  (Ort-X) eine Vermietungstätigkeit im umsatz- und ertragsteuerlichen Sinn darstellt (Ansicht des  Bf) oder steuerlich unbeachtlich ist (Position des Finanzamtes X/FA).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamtes`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/138977.1`) (sent_id: `deanon_BFG_20260814_TEST/138977.1_6`)


Entscheidungsgründe  I. Verfahrensgang  In seiner über FinanzOnline eingereichten Erklärung zur Arbeitnehmerveranlagung 2021  beantragte der Beschwerdeführer (Bf) unter anderem die Berücksichtigung des  Pendlerpauschales in Höhe von 3.672 € und des Pendlereuros in Höhe von 150 €.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/139123.1`) (sent_id: `deanon_BFG_20260814_TEST/139123.1_4`)


Entscheidungsgründe  I. Verfahrensgang und Sachverhalt  Der Beschwerdeführer (Bf) ist ungarischer Staatsbürger, in Österreich erwerbstätig, seine  Kinder leben in Ungarn.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/139601.1`) (sent_id: `deanon_BFG_20260814_TEST/139601.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) bezog im Jahr 2009 unter anderem Einkünfte aus nichtselbständiger  Arbeit und in Folge der Insolvenz seines Arbeitgebers (BB GmbH Nfg KG) Insolvenz-Entgelt von  der Insolvenz-Entgelt-Fonds Service GmbH (IEF Service GmbH vormals IAF Service GmbH).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `IEF Service GmbH`(organisation)
- `IAF Service GmbH`(organisation)

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/139805.1`) (sent_id: `deanon_BFG_20260814_TEST/139805.1_59`)


Die Einlaufstelle hat den  Beleg dem Beschwerdeführer (Antragsteller) auf Verlangen zurückzustellen, zuvor darauf einen  deutlichen Sichtvermerk anzubringen und auf der im Akt verbleibenden Ausfertigung der  Eingabe zu bestätigen, dass die Gebührenentrichtung durch Vorlage des Zahlungsbeleges  nachgewiesen wurde.

**False Positives:**

- `Antragsteller` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/140248.1`) (sent_id: `deanon_BFG_20260814_TEST/140248.1_5`)


Entscheidungsgründe  Strittig ist im anhängigen Verfahren die steuerliche Behandlung von Einkünften aus deutschen  Einkunftsquellen (Sozialversicherungsrente, Betriebsrente und Rente eines Pensionsfonds),  welche die Beschwerdeführerin (Bf) im Verfahrenszeitraum 2009 – 2014 neben  österreichischen Pensionseinkünften bezog.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/141437.1`) (sent_id: `deanon_BFG_20260814_TEST/141437.1_5`)


Entscheidungsgründe  I. Verfahrensgang  Strittig im Verfahren ist, inwieweit vom Beschwerdeführer (Bf) geltend gemachte  außergewöhnliche Belastungen den tatbestandlichen Kriterien entsprechen, insbesondere weil  sie medizinisch notwendig seien und alternativmedizinische Produkte ärztlich verordnet  worden seien.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/141832.1`) (sent_id: `deanon_BFG_20260814_TEST/141832.1_67`)


Zusammengefasst hat sohin der VwGH sowohl der Rechtsansicht des  Bundesfinanzgerichtes (BFG), der gemeine Wert des Baurechtes sei dem gemeinen Wert des  (bebauten oder unbebauten) Grundstückes gleichzuhalten, wie auch ausdrücklich dem  Begehren der Beschwerdeführerin (Bf), der nach § 15 BewG (mit dem 18fachen) kapitalisierte  Baurechtszins sei als gemeiner Wert des Baurechts iSd § 10 BewG anzusehen, eine Absage  erteilt.  Abgesehen davon lässt der VwGH eine nähere Konkretisierung dahingehend, welche  "Ermittlungen über den gemeinen Wert eines einzuräumenden Baurechts" das BFG anstellen  sollte, vermissen.

**False Positives:**

- `Bf` — similar text (different position): `Bundesfinanzgerichtes (BFG)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes (BFG)`(organisation)
- `BFG`(organisation)

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/143172.1`) (sent_id: `deanon_BFG_20260814_TEST/143172.1_3`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Der Beschwerdeführer (Bf) beantragte im Rahmen der Arbeitnehmerveranlagung 2022 die  Berücksichtigung des Familienbonus Plus für seine drei Kinder.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/143262.1`) (sent_id: `deanon_BFG_20260814_TEST/143262.1_3`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig .  Begründung  Mit Bescheid vom 13.7.2023 wurden gegen den Beschwerdeführer (Bf) Anspruchszinsen 2021  in Höhe von 67,61 € festgesetzt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/143688.1`) (sent_id: `deanon_BFG_20260814_TEST/143688.1_4`)


I.Verfahrensgang und entscheidungsrelevanter Sachverhalt  Mit Bescheid vom 28.05.2021 wurde die Beschwerdeführerin (Bf) aufgefordert, die für P., für  die Zeit von März 2016 bis Oktober 2019 bezogene Familienbeihilfe (FB) bzw.  Kinderabsetzbetrag iHv € 16.559,40 zurückzuzahlen (siehe dazu Rückforderungsbescheid vom  28.05.2021).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_9`)


Nach einer Außenprüfung bei der Beschwerdeführerin (Bf), einer Körperschaft öffentlichen  Rechts, ergingen im wiederaufgenommenen Verfahren neue Bescheide vom 7.5.2015 zur  Festsetzung der Energieabgabenvergütung für die Jahre 2005 – 2008 für folgende Betriebe  gewerblicher Art (sowie weitere Bescheide für nicht verfahrensgegenständliche Betriebe  gewerblicher Art):  1. A.   2. Bäder     3. Büchereien      4. Bf. Kindergärten     5. E. Stadion      6. B. Stadion    7. C. Eishalle     8. D.Bad   9. F. Stadion

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/144402.1`) (sent_id: `deanon_BFG_20260814_TEST/144402.1_4`)


Entscheidungsgründe  Die Beschwerdeführerin (Bf) ist im Bereich der Stromerzeugung aus erneuerbaren Energien,  insbesondere der Windenergie, tätig.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/144847.1`) (sent_id: `deanon_BFG_20260814_TEST/144847.1_3`)


Begründung  1. Verfahrensgang/Festgestellter Sachverhalt:  Mit Bescheid vom 20.6.2023 wurde die Beschwerdeführerin (Bf) zur Einkommensteuer für das  Jahr 2022 veranlagt.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/145156.1`) (sent_id: `deanon_BFG_20260814_TEST/145156.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Strittig ist, ob die Beschwerdeführerin (Bf) im Jahr 2021 zwei oder drei volle Quartale  bestanden hat und ob sie daher Mindestkörperschaftsteuer in Höhe von 375 Euro wie von der  belangten Behörde vorgeschrieben, oder in Höhe von 250 Euro wie in der Beschwerde  beantragt zu entrichten hat.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/145232.1`) (sent_id: `deanon_BFG_20260814_TEST/145232.1_3`)


Entscheidungsgründe  Im gegenständlichen Verfahren ist zu klären, ob dem Beschwerdeführer (Bf) im Jahr 2021  erwachsene Kosten im Zusammenhang mit bzw. im Gefolge der Übersiedlung seiner  Schwägerin samt Tochter aus Afrika/Land-X nach Stadt-Y in dessen Einkommensteuer(ESt)-

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig   Begründung  Der Beschwerdeführer (Bf) begehrte in den ANV-Erklärungen 2018 (Pflichtveranlagung) bzw.  2019 (Antragsveranlagung) einerseits der Abzug diverser Werbungskosten im Zusammenhang  mit seinen nichtselbständigen Einkünften (Pendlerpauschale/ Pendlereuro, AfA für  Arbeitsmittel, Telefonkosten, Aufwand für Dienstreisen) und anderseits die Berücksichtigung  von Krankheitskosten als außergewöhnliche Belastung (§ 34 EStG 1988).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/146238.1`) (sent_id: `deanon_BFG_20260814_TEST/146238.1_6`)


Entscheidungsgründe  Ein Parkraumüberwachungsorgan traf anlässlich einer Kontrolle die Feststellung, dass das auf  den Beschwerdeführer (Bf) zugelassene mehrspurige Kraftfahrzeug mit dem Kennzeichen  abcdesfg am 8.3.2023 um 12:43 Uhr in einer gebührenpflichtigen Kurzparkzone in Wien ohne  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein abgestellt  gewesen sei, im Kraftfahrzeug sei ein bis 30.9.2023 befristeter Parkausweis gemäß § 29b StVO  1 von 11 Seite 2 von 11

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/146537.1`) (sent_id: `deanon_BFG_20260814_TEST/146537.1_3`)


Entscheidungsgründe  Zu klären ist im anhängigen Verfahren die Zulässigkeit der Ablehnung einer beantragten  Wiederaufnahme des an die Beschwerdeführerin (Bf) ergangenen Einkommensteuer (ESt)-  Bescheides 2018 vom 29.Jän 2020.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/146931.1`) (sent_id: `deanon_BFG_20260814_TEST/146931.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Der Beschwerdeführer (Bf) bezog im Streitjahr neben einer von Seiten der  Pensionsversicherungsanstalt zu Auszahlung gebrachten inländischen Alterspension (€  32.398,24 brutto) auch deutsche Renteneinkünfte in Höhe von € 2.991,00 brutto (Bescheid des  Finanzamtes Neubrandenburg/BRD vom 17.6.2022).

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pensionsversicherungsanstalt`(organisation)
- `Finanzamtes`(organisation)

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/148979.1`) (sent_id: `deanon_BFG_20260814_TEST/148979.1_3`)


Begründung  1. Verfahrensgang:  Mit als „Erinnerung" bezeichnetem Schreiben vom 5.12.2024 forderte das Finanzamt die  Beschwerdeführerin (Bf), eine in Österreich ansässige Europäische wirtschaftliche  Interessenvereinigung (EWIV), auf, die Erstmeldung oder Meldung nach Fälligkeit der  jährlichen Überprüfung der wirtschaftlichen Eigentümer gemäß § 5 WiEReG bis spätestens  27.1.2025 nachzuholen.

**False Positives:**

- `Bf` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt`(organisation)

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
| `person` | 0 | 2 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/132841.1`) (sent_id: `deanon_BFG_20260814_TEST/132841.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die RichterinR in der Beschwerdesache OSR Juliette Franzisi, Spitzesed 172, 4673 Baumgarting, Österreich, über die Beschwerde vom 17. Juli 2019 gegen den Bescheid des Finanzamtes Wien  2/20/21/22 vom 17. Juni 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2018  Steuernummer 47-760/2078  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Juliette Franzisi` — partial — pred is substring of gold: `OSR Juliette Franzisi`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Juliette Franzisi`(person)
- `Spitzesed 172, 4673 Baumgarting, Österreich`(address)
- `Finanzamtes Wien  2/20/21/22`(organisation)
- `47-760/2078`(tax_number)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/148827.1`) (sent_id: `deanon_BFG_20260814_TEST/148827.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger in der Beschwerdesache  OSR Konstanze Dockweiler, Hasenkogl 4, 3572 St. Leonhard am Hornerwald, Österreich, betreffend die am 2. August 2024 beim Finanzamt Österreich  eingelangte Beschwerde gegen die als „festgesetzte Säumniszuschläge für 2021“ bezeichneten  Bescheide beschlossen:  I.  Die Beschwerde gilt gem. § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `Konstanze Dockweiler` — partial — pred is substring of gold: `OSR Konstanze Dockweiler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `OSR Konstanze Dockweiler`(person)
- `Hasenkogl 4, 3572 St. Leonhard am Hornerwald, Österreich`(address)
- `Finanzamt Österreich`(organisation)

</details>

---

## `Role_Followed_Name` 💣

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
| 0.000 | 0.000 | 0.000 | 12 | 0 | 12 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 12 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_137`)


Zu Punkt 5 der Niederschrift   Lt. Niederschrift liegen der Behörde Unterlagen über Geldflüsse betreffende das Unternehmen  vor.

**False Positives:**

- `Niederschrift   Lt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_146`)


Zu Pkt. 6 der Niederschrift   Unbestritten   Zu Pkt. 7 der Niederschrift   Die Feststellung der Behörde, es gäbe keine laufenden Nummern bei den Ausgangsrechnungen  ist nicht richtig.

**False Positives:**

- `Niederschrift   Unbestritten   Zu Pkt` — no gold match — likely missing annotation
- `Niederschrift   Die Feststellung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_148`)


Zu Pkt. 9 der Niederschrift   Diese Rechnungsnummern wurden durch einen Irrtum bei der Rechnungsnummernvergabe  nicht vergeben.

**False Positives:**

- `Niederschrift   Diese Rechnungsnummern` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_152`)


Zu Pkt 10 der Niederschrift   Die Behauptung, dass ein Teil der Belege fehlte (offenbar 2012) kann aus unserer Sicht nicht  nachvollzogen werden.

**False Positives:**

- `Niederschrift   Die Behauptung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_162`)


Zu Pkt. 11 der Niederschrift   Es wird von der Behörde nicht schlüssig dargelegt, in welchem Zusammenhang die Unterlagen  von Herrn GM* mit dem Außenprüfungsverfahren stehen.

**False Positives:**

- `Niederschrift   Es` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_166`)


Zu Pkt. 12 der Niederschrift   Aus der behördlichen Formulierung ist nicht ersichtlich welche konkreten Vorsteuern gem. § 12  UStG nicht anerkannt werden.

**False Positives:**

- `Niederschrift   Aus` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_168`)


Zu Pkt. 13 der Niederschrift   Der Abgabepflichtige wird versuchen die Empfangsbestätigungen nachzureichen, um so die  Tatsache der Ausfuhr entsprechend zu dokumentieren.

**False Positives:**

- `Niederschrift   Der Abgabepflichtige` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/139440.1`) (sent_id: `deanon_BFG_20260814_TEST/139440.1_171`)


Zu Pkt. 14 der Niederschrift   Wir bitten im Rahmen des Rechts auf Akteneinsicht um Vorlage der Abfrageprotokolle  bezüglich der ig.

**False Positives:**

- `Niederschrift   Wir` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_64`)


Die Bekanntgabe der Inanspruchnahme gab der Bf. zudem uns, seiner  steuerlichen Vertretung, in diversen persönlichen Gesprächen, Telefonaten und E-Mail  Korrespondenz bekannt.

**False Positives:**

- `E-Mail  Korrespondenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_442`)


2.6. Stellungnahme  Am 4.12.2023 wurde eine undatierte Stellungnahme der Großbetriebsprüfung zur Beschwerde  gegen die Wiederaufnahme- und die Energieabgabenvergütungsbescheide nachgereicht.

**False Positives:**

- `Stellungnahme  Am` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/145870.1`) (sent_id: `deanon_BFG_20260814_TEST/145870.1_17`)


Ich habe bereits am 8.6.2024 per E-Mail  Einspruch eingelegt.

**False Positives:**

- `E-Mail  Einspruch` — no gold match — likely missing annotation

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
| `person` | 0 | 0 | 1614 |

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
| 0.000 | 0.000 | 0.000 | 27 | 0 | 27 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 27 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/107792.1`) (sent_id: `deanon_BFG_20260814_TEST/107792.1_0`)


GZ. RV/6100653/2015 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat durch den Richter Mag. Erich Schwaiger über die Beschwerde vom 5. Dezember 2012 des Beschwerdeführers Jeremias Pretzel ,Zwingligasse 109, 2063 Zwingendorf, Österreich , vertreten durch die mit Zustellvollmacht ausgewiesene CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG ,  1210 Wien ,  Karl-Waldbrunner-Platz 1  gegen den Bescheid des Finanzamtes Salzburg-Land, 5026 Salzburg-Aigen, Aignerstraße 10 vertreten durch Mag. Josef Nußbaumer, vom  5. November 2012  betreffend  die Festsetzung von Anspruchszinsen 2007   zu Recht erkannt: I) Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Mag. Josef Nußbaumer` — partial — gold is substring of pred: `Mag. Josef Nußbaumer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Erich Schwaiger`(person)
- `Jeremias Pretzel`(person)
- `Zwingligasse 109, 2063 Zwingendorf, Österreich`(address)
- `CONSULTATIO Revision und Treuhand Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes Salzburg-Land`(organisation)
- `Mag. Josef Nußbaumer`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_0`)


GZ. RV/7300010/2019 IM NAMEN DER REPUBLIK Der Finanzstrafsenat Wien 1 des Bundesfinanzgerichtes hat  in  der Finanzstrafsache gegen N.N., Adresse*****, vertreten durch Dr. Heinz Neuner, Rechtsanwalt, Hietzinger Kai 5/18, 1130 Wien, wegen der Finanzvergehen der Abgabenhinterziehung gemäß § 33 Abs. 1 des Finanzstrafgesetzes (FinStrG) und der Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG über die Beschwerde des Amtsbeauftragten vom  07.01.2019  gegen das Erkenntnis des Spruchsenates beim Finanzamt Wien 9/18/19 Klosterneuburg als Organ  der belangten Behörde  Finanzamt Wien 9/18/19 Klosterneuburg als Finanzstrafbehörde vom  05.12.2018 , SpS *****, nach Durchführung einer mündlichen Verhandlung am 10.09.2019 in Anwesenheit des Beschuldigten und seines Verteidigers, des Amtsbeauftragten AB sowie derr Schriftführerin  R.G.  zu Recht erkannt: Die Beschwerde des Amtsbeauftragten wird als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Dr. Heinz Neuner` — partial — gold is substring of pred: `Dr. Heinz Neuner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgerichtes`(organisation)
- `N.N.`(person)
- `Dr. Heinz Neuner`(person)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamt Wien 9/18/19 Klosterneuburg`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/126588.1`) (sent_id: `deanon_BFG_20260814_TEST/126588.1_0`)


GZ. RV/7300057/2019 IM NAMEN DER REPUBLIK Das Bundesfinanzgericht hat in der Finanzstrafsache gegen N.N., Adresse1, vertreten durch Mag. Michael Nierla, Rechtsanwalt, Annagasse 5/2 DG, 1010 Wien, wegen des Finanzvergehens der grob fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 des Finanzstrafgesetzes (FinStrG) über die Beschwerde des Beschuldigten vom  16.01.2017  gegen das Erkenntnis der belangten Behörde Finanzamt für Gebühren, Verkehrsteuern und Glücksspiel als Finanzstrafbehörde vom 05.12.2016, Strafnummer *******,    zu Recht erkannt: Die Beschwerde des Beschuldigten N.N. wird Folge gegeben, das angefochtene Erkenntnis aufgehoben und das gegen den Bf. wegen des Verdachtes der fahrlässigen Abgabenverkürzung gemäß § 34 Abs. 1 FinStrG zu Strafnummer ******* anhängige    Finanzstrafverfahren gemäß §§ 136, 157 FinStrG eingestellt. Eine Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `vertreten durch Mag. Michael Nierla` — partial — gold is substring of pred: `Mag. Michael Nierla`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `N.N.`(person)
- `Mag. Michael Nierla`(person)
- `Finanzamt für Gebühren`(organisation)
- `N.N.`(person)
- `Verwaltungsgerichtshof`(organisation)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/129134.1`) (sent_id: `deanon_BFG_20260814_TEST/129134.1_2`)


Das Bundesfinanzgericht hat durch den Richter R. über die Beschwerde des OSR Corbinian Friemuth,  BFAdresse, vertreten durch Mag. Alexander Rimser, Hermann-Bahr-Straße 18/3, 1210 Wien,  vom 10. Juli 2019, gegen das Straferkenntnis der belangten Behörde, Magistrat der Stadt Wien,  MA 67, als Abgabenstrafbehörde, vom 6. Juni 2019, MA67/000/2019, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs.  1 Wiener Parkometergesetz 2006, nach Durchführung einer mündlichen Verhandlung am 21.  Juli 2020, im Beisein der Schriftführerin I., zu Recht erkannt:   I. Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das  angefochtene Straferkenntnis bestätigt.

**False Positives:**

- `vertreten durch Mag. Alexander Rimser` — partial — gold is substring of pred: `Mag. Alexander Rimser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `OSR Corbinian Friemuth`(person)
- `Mag. Alexander Rimser`(person)
- `Hermann`(person)
- `Magistrat der Stadt Wien`(organisation)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/129704.1`) (sent_id: `deanon_BFG_20260814_TEST/129704.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Anna Mechtler-Höger in der  Beschwerdesache Roxana Dellner, Wengerhöhstraße 1, 4904 Schnötzing, Österreich, vertreten durch RA Mag. Robert Bitsche,  Nikolsdorfergasse 7-11/2, 1050 Wien, als Beschwerdeführerin über die Beschwerde vom  28. März 2017 gegen den Bescheid des Magistrats der Stadt Wien Referat Landes- und  Gemeindeabgaben vom 20. März 2017 betreffend Kommunalsteuer für den Zeitraum 2012 und  2013, Steuernummer 88-034/0292, zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `vertreten durch RA Mag. Robert Bitsche` — partial — gold is substring of pred: `RA Mag. Robert Bitsche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Anna Mechtler-Höger`(person)
- `Roxana Dellner`(person)
- `Wengerhöhstraße 1, 4904 Schnötzing, Österreich`(address)
- `RA Mag. Robert Bitsche`(person)
- `Magistrats der Stadt Wien`(organisation)
- `88-034/0292`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/131717.1`) (sent_id: `deanon_BFG_20260814_TEST/131717.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ulrich Petrag in der Beschwerdesache  Natalie Nodurft, Saileräckergasse 112, 4676 Augassen, Österreich, vertreten durch Mag. Marion Riezinger, Sonnblickstraße 6, 4614  Marchtrenk, über die Beschwerden vom 15. April 2019 gegen die Bescheide des Finanzamtes  Linz vom 15. März 2019 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2014 bis  2017 Steuernummer xxxyyyy zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Mag. Marion Riezinger` — partial — gold is substring of pred: `Mag. Marion Riezinger`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrich Petrag`(person)
- `Natalie Nodurft`(person)
- `Saileräckergasse 112, 4676 Augassen, Österreich`(address)
- `Mag. Marion Riezinger`(person)
- `Finanzamtes  Linz`(organisation)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/131799.1`) (sent_id: `deanon_BFG_20260814_TEST/131799.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ronald Kulenkampf  in der Beschwerdesache [...], [...],  vertreten durch Mag. Monika Schmalzl, Marterlweg 8, 9220 Velden, über die Beschwerde vom  22. August 2011 gegen den Bescheid des FA Wien 1/23  vom 24. Juli 2013 2011 betreffend  Körperschaftsteuer 2010, Steuernummer 06-334/4335 ,zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `vertreten durch Mag. Monika Schmalzl` — partial — gold is substring of pred: `Mag. Monika Schmalzl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ronald Kulenkampf`(person)
- `Mag. Monika Schmalzl`(person)
- `FA Wien 1/23`(organisation)
- `06-334/4335`(tax_number)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/132613.1`) (sent_id: `deanon_BFG_20260814_TEST/132613.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag.a Lukas Dimitrieff  in der Beschwerdesache Juri Marstaller,  Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich, vertreten durch   Sonja Wennemann, über die Bescheidbeschwerden vom 26.02.2018 gegen die Bescheide des  Finanzamt Klagenfurt St. Veit Wolfsberg (nunmehr Finanzamt Österreich) vom 26.01.2018 betreffend  Kapitalertragsteuer 01.2013-11.2013, Kapitalertragsteuer 01.2014-11.2014 und  Kapitalertragsteuer 01.2015-11.2015 zu Steuernummer 21-286/5389  beschlossen:  Es wird die Unzuständigkeit des Bundesfinanzgerichtes festgestellt.  Das Verfahren vor dem Bundesfinanzgericht wird eingestellt.  Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `vertreten durch   Sonja Wennemann` — partial — gold is substring of pred: `Sonja Wennemann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Lukas Dimitrieff`(person)
- `Juri Marstaller`(person)
- `Emmy-Woitsch-Weg 22, 9654 Frohn, Österreich`(address)
- `Sonja Wennemann`(person)
- `Finanzamt Klagenfurt St. Veit Wolfsberg`(organisation)
- `Finanzamt Österreich`(organisation)
- `21-286/5389`(tax_number)
- `Bundesfinanzgerichtes`(organisation)
- `Bundesfinanzgericht`(organisation)
- `Verwaltungsgerichtshof`(organisation)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `vertreten durch Mag. Kurt Kreith` — partial — gold is substring of pred: `Mag. Kurt Kreith`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Viktoria Blaser`(person)
- `Mag. Sven Weichmann`(person)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich`(address)
- `Mag. Kurt Kreith`(person)
- `Finanzamtes Baden  Mödling`(organisation)
- `78-738/0573`(tax_number)

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/134149.1`) (sent_id: `deanon_BFG_20260814_TEST/134149.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht in der Beschwerdesache  des Juliana Untermeier, C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich, vertreten durch Dr. Christoph Ganahl, Rechtsanwalt, Schwefel  93/7, 6850 Dornbirn, über die Beschwerde vom 16. Mai 2013 gegen den Bescheid des  Finanzamtes Bregenz vom 10. April 2013 betreffend Haftung gemäß § 9 iVm § 80  Bundesabgabenordnung (BAO), zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `vertreten durch Dr. Christoph Ganahl` — partial — gold is substring of pred: `Dr. Christoph Ganahl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Josef Ungericht`(person)
- `Juliana Untermeier`(person)
- `C - Birkenweg 27, 8213 Gersdorf an der Feistritz, Österreich`(address)
- `Dr. Christoph Ganahl`(person)
- `Finanzamtes`(organisation)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/135477.1`) (sent_id: `deanon_BFG_20260814_TEST/135477.1_33`)


Die Zustellung erfolgte durch  Hinterlegung, als Übernahmedatum scheint auf dem Rückschein der 5.11.2021 auf.

**False Positives:**

- `durch  Hinterlegung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/137110.1`) (sent_id: `deanon_BFG_20260814_TEST/137110.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Dr. Ansgar Unterberger in der  Beschwerdesache Harald Adriaans, Pflaster 68, 2872 Neustift am Alpenwalde, Österreich, vertreten durch Mag. Markus Wagner,  Eibenstein 39, 4261 Rainbach/Mühlkreis, über die Beschwerde vom 8. April 2021 gegen den  Bescheid des Finanzamtes Österreich vom 25. März 2021, Steuernummer 81-584/4494,  betreffend Einkommensteuer 2020 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen   II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art.  133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

**False Positives:**

- `vertreten durch Mag. Markus Wagner` — partial — gold is substring of pred: `Mag. Markus Wagner`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Ansgar Unterberger`(person)
- `Harald Adriaans`(person)
- `Pflaster 68, 2872 Neustift am Alpenwalde, Österreich`(address)
- `Mag. Markus Wagner`(person)
- `Finanzamtes Österreich`(organisation)
- `81-584/4494`(tax_number)
- `Verwaltungsgerichtshof`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/137445.1`) (sent_id: `deanon_BFG_20260814_TEST/137445.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Susanne Zankl in der Beschwerdesache  Bertha Unverich, Hinterseberweg 13D, 4742 Gewerbepark, Österreich, vertreten durch Dr. Robert Karl Galler, Viktor Keldorfer Strasse 1,  5020 Salzburg, betreffend Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 auf  Aussetzung § 212a BAO Steuernummer 92-593/4806  beschlossen:  Der Antrag gem. § 212a Bundesabgabenordnung vom 14.01.2022 wird gemäß § 260 Abs 1 lit a  iVm § 278 Abs1 lit a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `vertreten durch Dr. Robert Karl Galler` — partial — gold is substring of pred: `Dr. Robert Karl Galler`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Susanne Zankl`(person)
- `Bertha Unverich`(person)
- `Hinterseberweg 13D, 4742 Gewerbepark, Österreich`(address)
- `Dr. Robert Karl Galler`(person)
- `92-593/4806`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/137654.1`) (sent_id: `deanon_BFG_20260814_TEST/137654.1_58`)


U.a. wurde von Dr. Keppert auch die „sogenannte Lenneis-Formel“ bemängelt. Zusätzlich  verweist Dr. Keppert auf die Nichtbeachtung von zukünftigen Ertragssteigerungen durch die  Finanz (vgl. Gegenäußerung der Bf., vertreten durch Dr. Keppert, zur Gegenschrift des UFS an  den VwGH vom Juni 2014 zur Streitsache UFS vom 19.12.2012, Zl. RV/0966-W/05).

**False Positives:**

- `vertreten durch Dr. Keppert` — similar text (different position): `Dr. Keppert`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Keppert`(person)
- `Dr. Keppert`(person)
- `Dr. Keppert`(person)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/138141.1`) (sent_id: `deanon_BFG_20260814_TEST/138141.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Hemma Mauermair  in der   Beschwerdesache Franziska Fitzmann, Larchwald 7, 8850 Sankt Egidi, Österreich, vertreten durch Mag. Markus Franz Ganzer,  Anichstraße 13, 6020 Innsbruck, über die Beschwerde vom 29. Oktober 2021 gegen den  Bescheid des Finanzamtes Österreich vom 29. September 2021, Ordnungsbegriff Nr1,  betreffend Abweisung der Anträge auf Gewährung der erhöhten Familienbeihilfe ab Jänner  2015 zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Mag. Markus Franz Ganzer` — partial — gold is substring of pred: `Mag. Markus Franz Ganzer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Hemma Mauermair`(person)
- `Franziska Fitzmann`(person)
- `Larchwald 7, 8850 Sankt Egidi, Österreich`(address)
- `Mag. Markus Franz Ganzer`(person)
- `Finanzamtes Österreich`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/139382.1`) (sent_id: `deanon_BFG_20260814_TEST/139382.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Ulrike Nussbaumer LL.M. M.B.L. in der  Beschwerdesache Delila Frenski, Bairbach 31, 4892 Saxigen, Österreich, vertreten durch Mag. Gottfried Tazol,  Hauptplatz 24, 9100 Völkermarkt, über die Beschwerde vom 28. Dezember 2020 gegen die  Bescheide des Finanzamtes Österreich je vom 27. November 2020 betreffend  Wiederaufnahme der Verfahren Einkommensteuer 2014-2018 und Einkommensteuer  (ArbeitnehmerInnenveranlagung) 2014-2019 (Steuernummer 19-849/6261 ) zu Recht  erkannt:  I. BESCHLUSS  1.

**False Positives:**

- `vertreten durch Mag. Gottfried Tazol` — partial — gold is substring of pred: `Mag. Gottfried Tazol`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Ulrike Nussbaumer LL.M. M.B.L.`(person)
- `Delila Frenski`(person)
- `Bairbach 31, 4892 Saxigen, Österreich`(address)
- `Mag. Gottfried Tazol`(person)
- `Finanzamtes Österreich`(organisation)
- `19-849/6261`(tax_number)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/142762.1`) (sent_id: `deanon_BFG_20260814_TEST/142762.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Beschwerdesache Heinrich Rzeppa, LLM, Toulagasse 1, 8111 Straßengel, Österreich, vertreten durch Dr. Martin Weiser, Landstraßer  Hauptstraße 60, 1030 Wien, über die Beschwerde vom 04. März 2019 gegen den Bescheid des  Finanzamtes Wien 4/5/10 vom 31. Jänner 2019 betreffend Umsatzsteuer 2016, Steuernummer  52-580/0972  beschlossen:  I. Die Parteien werden gem. § 281a BAO formlos darüber verständigt, dass nach Auffassung des  Verwaltungsgerichts noch eine Beschwerdevorentscheidung zu erlassen ist.

**False Positives:**

- `vertreten durch Dr. Martin Weiser` — partial — gold is substring of pred: `Dr. Martin Weiser`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Karoline Windsteig`(person)
- `Heinrich Rzeppa, LLM`(person)
- `Toulagasse 1, 8111 Straßengel, Österreich`(address)
- `Dr. Martin Weiser`(person)
- `Finanzamtes Wien 4/5/10`(organisation)
- `52-580/0972`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/143207.1`) (sent_id: `deanon_BFG_20260814_TEST/143207.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter R in der Beschwerdesache Linus Frauenstein, Göllerichstraße 41, 9323 Wildbad Einöd, Österreich, vertreten durch Dr. Philip Gruber, Oberer Markt 22, 3631 Ottenschlag, über die  Beschwerde vom 21. Juli 2023 gegen die Bescheide des Finanzamtes Österreich vom 7. Juli  2023 betreffend Grunderwerbsteuer, Steuernummer 70-621/7927, Erfassungsnummer 10- 2023, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Dr. Philip Gruber` — partial — gold is substring of pred: `Dr. Philip Gruber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Linus Frauenstein`(person)
- `Göllerichstraße 41, 9323 Wildbad Einöd, Österreich`(address)
- `Dr. Philip Gruber`(person)
- `Finanzamtes Österreich`(organisation)
- `70-621/7927`(tax_number)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/143923.1`) (sent_id: `deanon_BFG_20260814_TEST/143923.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rita Wiersbicki  in der Beschwerdesache Corvin Billmaier,  Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich, vertreten durch Mag. Aleksandar Hofstätter, Johann-Strauß-Gasse 4-6//2/5,  1040 Wien, betreffend Beschwerde vom 10. Juli 2023 gegen den Bescheid des Finanzamtes  Österreich vom 2. September 2022 betreffend Einkommensteuer 2021 Steuernummer  23-971/7442  beschlossen:   Die Beschwerde vom 10. Juli 2023 wird gemäß § 260 Abs. 1 lit. b BAO iVm § 278 Abs. 1 lit. a  BAO als nicht rechtzeitig eingebracht zurückgewiesen.

**False Positives:**

- `vertreten durch Mag. Aleksandar Hofstätter` — partial — gold is substring of pred: `Mag. Aleksandar Hofstätter`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Rita Wiersbicki`(person)
- `Corvin Billmaier`(person)
- `Steinbrunn 30, 2571 Altenmarkt an der Triesting, Österreich`(address)
- `Mag. Aleksandar Hofstätter`(person)
- `Finanzamtes  Österreich`(organisation)
- `23-971/7442`(tax_number)

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/143991.1`) (sent_id: `deanon_BFG_20260814_TEST/143991.1_2`)


Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Denis Hoffjan  in der Beschwerdesache Hon.-Prof.in Ariadne Iwanowsky,  Camesinaweg 86, 4652 Taxlberg, Österreich, vertreten durch Prof. Yorick Frühbis, über die Beschwerde der  beschwerdeführenden Partei vom 05.03.2024 wegen behaupteter Verletzung der Pflicht zur  Erlassung eines Bescheides durch das Finanzamt Österreich betreffend den Antrag vom  21.08.2023 auf Durchführung der ArbeitnehmerInnenveranlagung für das Jahr 2022,  beschlossen:  I. Die Säumnisbeschwerde wird gemäß § 256 Abs 3 iVm § 284 Abs 7 lit a BAO als  gegenstandslos erklärt.

**False Positives:**

- `vertreten durch Prof. Yorick Frühbis` — partial — gold is substring of pred: `Prof. Yorick Frühbis`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Denis Hoffjan`(person)
- `Hon.-Prof.in Ariadne Iwanowsky`(person)
- `Camesinaweg 86, 4652 Taxlberg, Österreich`(address)
- `Prof. Yorick Frühbis`(person)
- `Finanzamt Österreich`(organisation)

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/144627.1`) (sent_id: `deanon_BFG_20260814_TEST/144627.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Thassilo Osipenko  in der Beschwerdesache des  Agatha Stingele, Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich, vertreten durch Mag. Hedwig Maria Weber, Ausseer Straße 32,  8940 Liezen, über die Beschwerden vom 5. August 2020 gegen die Bescheide des Finanzamtes  Österreich vom 7. Juli 2020 betreffend Festsetzung der Normverbrauchsabgabe (NoVA- Vergütung gemäß § 12a NoVAG) für   1) den Zeitraum 4 – 12/2019 und   2) den Zeitraum 1/2020,   Steuernummer 39-913/2428, zu Recht erkannt:   I. Die angefochtenen Bescheide werden abgeändert.

**False Positives:**

- `vertreten durch Mag. Hedwig Maria Weber` — partial — gold is substring of pred: `Mag. Hedwig Maria Weber`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof. Thassilo Osipenko`(person)
- `Agatha Stingele`(person)
- `Grundackerweg 11, 3263 Puchberg bei Randegg, Österreich`(address)
- `Mag. Hedwig Maria Weber`(person)
- `Finanzamtes  Österreich`(organisation)
- `39-913/2428`(tax_number)

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/145232.1`) (sent_id: `deanon_BFG_20260814_TEST/145232.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht (BFG) hat durch die Richterin Hon.-Prof.in Jacqueline Traxl  in der Beschwerdesache des  Gebhard Hannig, Nußdorfer Markt 4, 4776 Antersham, Österreich, vertreten durch Mag. Paulus Maria Christoph Papst,  Bergmanngasse 15 Tür 2, 8010 Graz, über die Beschwerde vom 1. März 2023 gegen den zur  Steuernummer 97-347/7690  ergangenen Bescheid des FA Braunau Ried Schärding  vom 3. Februar 2023  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2021 zu Recht erkannt:   I. Die Beschwerde vom 1.März 2023 gegen den Einkommensteuerbescheid 2021 vom  3.Februar 2023 wird als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Mag. Paulus Maria Christoph Papst` — partial — gold is substring of pred: `Mag. Paulus Maria Christoph Papst`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht (BFG)`(organisation)
- `Hon.-Prof.in Jacqueline Traxl`(person)
- `Gebhard Hannig`(person)
- `Nußdorfer Markt 4, 4776 Antersham, Österreich`(address)
- `Mag. Paulus Maria Christoph Papst`(person)
- `97-347/7690`(tax_number)
- `FA Braunau Ried Schärding`(organisation)

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/145369.1`) (sent_id: `deanon_BFG_20260814_TEST/145369.1_368`)


Für nachfolgende Aufwendungen fehlt es nach dem vorliegenden Ermittlungsergebnis an den  Voraussetzungen für einen Abzug als außergewöhnliche Belastung:   2018:  Behandlungs-/Therapiekosten, Medikamentenaufwand:  - 49,- € Dr-A (lt. Bf 17.2.2018): trotz FA-Anforderung vom 27.Aug.2020 kein Nachweis durch  Rechnung, Zahlungsbeleg oder ÖGK-Kostenersatz;  - 395,- € Dr-B (Zahlung 24.7.2018): trotz FA-Anforderung am 27.Aug.2020 kein Nachweis durch  Rechnung oder ÖGK-Kostenersatz ;  - 190,- € MRT Privatklinik-X (Zahlung 12.3.2018): trotz FA-Anforderung vom 27.Aug.2020 weder  Nachweis durch Rechnung/ ÖGK-Kostenersatz noch über die medizinische Notwendigkeit der  umgehenden Durchführung in einer Privateinrichtung;

**False Positives:**

- `durch  Rechnung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `ÖGK`(organisation)
- `ÖGK`(organisation)
- `ÖGK`(organisation)

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/147132.1`) (sent_id: `deanon_BFG_20260814_TEST/147132.1_313`)


Erfasst ist davon jede wirtschaftliche Tätigkeit eines EU-Unternehmens oder  einer Betriebsstätte, das bzw. die mindestens 75 % seines bzw. ihres Umsatzes durch  Extraktion, Bergbau, Erdölraffination oder die Herstellung von Kokereierzeugnissen erzielt  (Art 2 Z 17).

**False Positives:**

- `durch  Extraktion` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/147177.1`) (sent_id: `deanon_BFG_20260814_TEST/147177.1_314`)


Erfasst ist davon jede wirtschaftliche Tätigkeit eines EU-Unternehmens oder  einer Betriebsstätte, das bzw. die mindestens 75 % seines bzw. ihres Umsatzes durch  Extraktion, Bergbau, Erdölraffination oder die Herstellung von Kokereierzeugnissen erzielt  (Art 2 Z 17).

**False Positives:**

- `durch  Extraktion` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/148794.1`) (sent_id: `deanon_BFG_20260814_TEST/148794.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Lydia Stockman  in der Beschwerdesache Kaspar Sadowski,  Sankt Wendelin 50j, 3623 Elsenreith, Österreich, vertreten durch Dr. Franz Deutsch, Pfeilgasse 16/26, 1080 Wien, über die  Beschwerde vom 29. Dezember 2021 gegen den Bescheid des Finanzamtes Österreich vom  22. November 2021 betreffend Einkommensteuer 2019, Steuernummer 96-455/6800, zu  Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Dr. Franz Deutsch` — partial — gold is substring of pred: `Dr. Franz Deutsch`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Lydia Stockman`(person)
- `Kaspar Sadowski`(person)
- `Sankt Wendelin 50j, 3623 Elsenreith, Österreich`(address)
- `Dr. Franz Deutsch`(person)
- `Finanzamtes Österreich`(organisation)
- `96-455/6800`(tax_number)

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/148999.1`) (sent_id: `deanon_BFG_20260814_TEST/148999.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin R 1 in der Beschwerdesache PhD OSR Nigel Westerfeld,  Timls 1191a, 8966 Auberg, Österreich, vertreten durch Dr. Michael Kotschnigg, Steuerberater, Stadlauer Straße  39/1/Top 12, 1220 Wien, über   die Beschwerde vom 3. Dezember 2020 gegen die Bescheide des FA 1 vom 12. Oktober 2020  betreffend Umsatz- und Einkommensteuer 2015 zu Steuernummer 06-918/7336  zu Recht  erkannt:   I. Die Beschwerde gegen den Umsatzsteuerbescheid 2015 wird als unbegründet abgewiesen.

**False Positives:**

- `vertreten durch Dr. Michael Kotschnigg` — partial — gold is substring of pred: `Dr. Michael Kotschnigg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `PhD OSR Nigel Westerfeld`(person)
- `Timls 1191a, 8966 Auberg, Österreich`(address)
- `Dr. Michael Kotschnigg`(person)
- `06-918/7336`(tax_number)

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `Anonymized_Names` 

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
| 0.000 | 0.000 | 0.000 | 5 | 0 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 5 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_147`)


Die Tochter ist am X.X.2018, der Sohn ist am X.X.2020 geboren.

**False Positives:**

- `X.X.` — no gold match — likely missing annotation
- `X.X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_165`)


Sie ist vor Ostern, also vor dem 17.4.2020, wieder aus Deutschland nach  Österreich zurückgekehrt, da die Geburt ihres zweiten Kindes am X.X.2020 erfolgte.

**False Positives:**

- `X.X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_282`)


Befragt zum Verhandlungsprotokoll des LvwG Seite 1 und 3, ob sie von November bis April  2020 überwiegend in Deutschland war, gab die Bf an, dass sie 8 Wochen vor dem  Geburtstermin am X.X.2020 in Deutschland war, da sie ihrem Bruder bei der Kinderversorgung  geholfen hat.

**False Positives:**

- `X.X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_288`)


Sie ist aufgrund der Geburt des zweiten Kindes (welche am  X.X.2020 erfolgte) nach Ostern 2020, also vor dem 12.4.2020 bzw. dem 17.4.2020, wieder nach  Österreich an ihre Hauptwohnsitzadresse mit dem Bezug habenden Kraftfahrzeug  15 von 29 Seite 16 von 29

**False Positives:**

- `X.X.` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 8 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_15`)


Die Feststellungen ergeben sich im Übrigen aus dem Verwaltungsakt bzw. der folgenden  Beweiswürdigung:  Dass die betroffenen Filialen für die Bf. nicht unbenutzbar sind, ergibt sich aus der Erörterung  zwischen den Parteien am 08.03.2021 (vgl. Niederschrift Erörterungstermin).

**False Positives:**

- `Erörterungstermin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/132358.1`) (sent_id: `deanon_BFG_20260814_TEST/132358.1_20`)


Ebenso wird dies durch die Bf. im Rahmen des  Erörterungstermins bestätigt (vgl. Niederschrift Erörterungstermin vom 08.03.2021).

**False Positives:**

- `Erörterungstermin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_357`)


Zudem hat Ü, der Geschäftsführer der N, dies bestätigt (siehe  obige Niederschrift Seite 7 oben:“

**False Positives:**

- `Seite` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/135316.1`) (sent_id: `deanon_BFG_20260814_TEST/135316.1_4`)


Sachverhalt und Beweiswürdigung  Die beschwerdeführende Partei hat der Aufhebung und Neuerlassung des  Körperschaftsteuerbescheides 2006 zugestimmt (vgl. Niederschrift Erörterungstermin vom  13.10.2021).

**False Positives:**

- `Erörterungstermin` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_287`)


(siehe  Niederschrift Pkt. 1)

**False Positives:**

- `Pkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_292`)


(siehe Niederschrift Pkt. 12, 13, 18)

**False Positives:**

- `Pkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/139041.1`) (sent_id: `deanon_BFG_20260814_TEST/139041.1_403`)


Umso mehr als der Bf. selbst erklärt, dass es ganz  schnell geht diese Dateien (Impressum, Datenschutz, über mich etc.) einzufügen (siehe  Niederschrift Pkt. 18).

**False Positives:**

- `Pkt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/147387.1`) (sent_id: `deanon_BFG_20260814_TEST/147387.1_227`)


Die dauerhafte Einbringung des Fahrzeuges zum Zeitpunkt der Hauptwohnsitzmeldung ergibt  sich aus den Angaben der Bf. (siehe Niederschrift Finpol OZ 19) und ist unstrittig.

**False Positives:**

- `Finpol` — no gold match — likely missing annotation

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| 0.000 | 0.000 | 0.000 | 19 | 0 | 19 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 19 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Dr.in Hemma Ramelow  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Damian Wiecher` — partial — pred is substring of gold: `Mag. Damian Wiecher`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Univ.-Prof.in Dr.in Hemma Ramelow`(person)
- `Mag. Damian Wiecher`(person)
- `Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich`(address)
- `Finanzamt Wien 2/20/21/22`(organisation)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/131795.1`) (sent_id: `deanon_BFG_20260814_TEST/131795.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Mag. Thassilo Wedekinn, Kettengasse 36, 4870 Weixlbaum, Österreich, vertreten durch die Rittmann KG,  Steuerberatung und Wirtschaftsprüfung, Braintnerstraße 36, 2500 Baden, über die  Beschwerde vom 27. August 2019 gegen den Bescheid des Bundesministers für Finanzen vom  1. August 2019, GZ. BMF-010221/0213, mit dem ein Antrages gemäß § 48 BAO auf Beseitigung  der Doppelbesteuerung für die Jahre 2010 – 2013 (betreffend Malta) abgewiesen worden ist,  zu Recht:   Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Thassilo Wedekinn` — partial — pred is substring of gold: `Mag. Thassilo Wedekinn`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Mag. Thassilo Wedekinn`(person)
- `Kettengasse 36, 4870 Weixlbaum, Österreich`(address)
- `Rittmann KG,  Steuerberatung und Wirtschaftsprüfung`(organisation)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/132724.1`) (sent_id: `deanon_BFG_20260814_TEST/132724.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hugo Pietzak  in der Beschwerdesache Dr. Florens Weißer,  Straubingerplatz 57, 4691 Römerberg, Österreich, über die Beschwerden vom 25. November 2020 und 7. Dezember 2020 gegen  die Bescheide des ehemaligen Finanzamtes Wien 1/23 vom 18. November 2020 und 24.  November 2020 betreffend Zurückweisung der Anträge auf Aussetzung der Einhebung vom 22.  März 2020 und 18. August 2020, Steuernummer 09-64-114/4837  zu Recht erkannt:   Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Florens Weißer` — partial — pred is substring of gold: `Dr. Florens Weißer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Hugo Pietzak`(person)
- `Dr. Florens Weißer`(person)
- `Straubingerplatz 57, 4691 Römerberg, Österreich`(address)
- `Finanzamtes Wien 1/23`(organisation)
- `09-64-114/4837`(tax_number)

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch Mag. Kurt Kreith, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

**False Positives:**

- `Sven Weichmann` — partial — pred is substring of gold: `Mag. Sven Weichmann`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Viktoria Blaser`(person)
- `Mag. Sven Weichmann`(person)
- `Kellerweg 13, 9061 Ziegelsdorf, Österreich`(address)
- `Mag. Kurt Kreith`(person)
- `Finanzamtes Baden  Mödling`(organisation)
- `78-738/0573`(tax_number)

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/134354.1`) (sent_id: `deanon_BFG_20260814_TEST/134354.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Dr. Elisabeth Hafner in der  Beschwerdesache Dr. Ashley Nagelschmidt, Hollenbach 37, 4872 Unterthumberg, Österreich, vertreten durch APP Steuerberatung GmbH,  Waidmannsdorfer Straße 10, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom  24. November 2016 gegen die Haftungs- und Abgabenbescheide gemäß § 99 Abs. 1 EStG 1988  betreffend Einkommensteuer (Abzugsteuer) für die Jahre 2013 bis 2015 des Finanzamtes für  Großbetriebe (nunmehr Finanzamt für Großbetriebe) vom 24. Oktober 2016, Steuernummer  16-165/9893  zu Recht:   Der Beschwerde wird Folge gegeben.

**False Positives:**

- `Ashley Nagelschmidt` — partial — pred is substring of gold: `Dr. Ashley Nagelschmidt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Elisabeth Hafner`(person)
- `Dr. Ashley Nagelschmidt`(person)
- `Hollenbach 37, 4872 Unterthumberg, Österreich`(address)
- `APP Steuerberatung GmbH`(organisation)
- `Finanzamtes für  Großbetriebe`(organisation)
- `Finanzamt für Großbetriebe`(organisation)
- `16-165/9893`(tax_number)

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134709.1`) (sent_id: `deanon_BFG_20260814_TEST/134709.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht erkennt durch den Richter Mag. Daniel Philip Pfau in der  Beschwerdesache Prof.in Julia Mundle, Leitersdorf 2, 9344 Psein, Österreich, vertreten durch Hopmeier Wagner Kirnbauer  Rechtsanwälte OG, Rathausstraße 15, 1010 Wien, über die Beschwerde vom 13. Februar 2018  gegen den Bescheid des Finanzamtes Wien 12/13/14 Purkersdorf vom 31. Jänner 2018,  Steuernummer 23-019/8335, betreffend Aufhebung gem § 295 Abs. 4 BAO des  Einkommensteuerbescheides 2009 zu Recht:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Julia Mundle` — partial — pred is substring of gold: `Prof.in Julia Mundle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Daniel Philip Pfau`(person)
- `Prof.in Julia Mundle`(person)
- `Leitersdorf 2, 9344 Psein, Österreich`(address)
- `Hopmeier Wagner Kirnbauer  Rechtsanwälte OG`(organisation)
- `Finanzamtes Wien 12/13/14 Purkersdorf`(organisation)
- `23-019/8335`(tax_number)

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/135065.1`) (sent_id: `deanon_BFG_20260814_TEST/135065.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den RichterRi in der Beschwerdesache Prof.in Jeanne Sohns, Rosenhügelweg 5, 4870 Maurachen, Österreich, vertreten durch Gutwirth Consulting Steuerberatungs GmbH, Wilhelm-von-Exner- Straße 14, 5020 Salzburg, betreffend die Beschwerde vom 15. Jänner 2021 gegen den Bescheid  des Finanzamtes Österreich vom 9. Dezember 2020 betreffend Einkommensteuer 2018  beschlossen:  Der Vorlageantrag wird gemäß § 260 Abs. 1 lit b. BAO iVm § 264 Abs. 4 lit e BAO als verspätet  zurückgewiesen.

**False Positives:**

- `Jeanne Sohns` — partial — pred is substring of gold: `Prof.in Jeanne Sohns`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Prof.in Jeanne Sohns`(person)
- `Rosenhügelweg 5, 4870 Maurachen, Österreich`(address)
- `Gutwirth Consulting Steuerberatungs GmbH,`(organisation)
- `Finanzamtes Österreich`(organisation)

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/135647.1`) (sent_id: `deanon_BFG_20260814_TEST/135647.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Wieland Starnberg  in der Beschwerdesache Ing. Linus Feyerherdt,  Oberwies 10, 3920 Antenfeinhöfen, Österreich, vertreten durch Christina Hildegard Stowasser, Untersiebenbrunnerstraße 8,  2283 Obersiebenbrunn, vertreten durch Obf, betreffend Beschwerde vom 13. Juni 2019 gegen  die Bescheide des Finanzamtes Gänserndorf Mistelbach - nunmehr Finanzamtes Österreich -  vom 16. Mai 2019 zu Steuernummer 98-011/6615  betreffend Umsatzsteuer 2015,  Umsatzsteuer 2016 und Umsatzsteuer 2017 beschlossen:  I. Die Beschwerde gilt gemäß § 278 Abs 1 lit b iVm § 85 Abs 2 Bundesabgabenordnung  (BAO) als zurückgenommen.

**False Positives:**

- `Linus Feyerherdt` — partial — pred is substring of gold: `Ing. Linus Feyerherdt`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz. Wieland Starnberg`(person)
- `Ing. Linus Feyerherdt`(person)
- `Oberwies 10, 3920 Antenfeinhöfen, Österreich`(address)
- `Christina Hildegard Stowasser`(person)
- `Finanzamtes Gänserndorf Mistelbach`(organisation)
- `Finanzamtes Österreich`(organisation)
- `98-011/6615`(tax_number)

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/135648.1`) (sent_id: `deanon_BFG_20260814_TEST/135648.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Walter Aiglsdorfer in der  Beschwerdesache Prof. Leander Pfleumer, LLM, Am Gewerbepark 6, 9065 Niederdorf, Österreich, vertreten durch Alfred Klaus Fenzl, Am  Steinbühel 27b, 4030 Linz, über die Beschwerde vom 11. November 2020 gegen den Bescheid  des Finanzamtes Linz (nunmehr Finanzamtes Österreich ) vom 22. Oktober 2020 betreffend  Einkommensteuer (Arbeitnehmerveranlagung) 2019 Steuernummer 11-306/0925  zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Leander Pfleumer` — partial — pred is substring of gold: `Prof. Leander Pfleumer, LLM`

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

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/136415.1`) (sent_id: `deanon_BFG_20260814_TEST/136415.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den RichterR in der Beschwerdesache Dr. Valerius Somuncu, Seelache 250, 2294 Schloßhof, Österreich, vertreten durch Dr-K, Rechtsanwalt in A, über die Beschwerde vom 22. Dezember  2017 gegen den Bescheid des Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel  (nunmehr: Finanzamt Österreich) vom 23. November 2017 betreffend Grunderwerbsteuer,  Steuernummer 84-691/1997, Erfassungsnummer 10-2015, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Valerius Somuncu` — partial — pred is substring of gold: `Dr. Valerius Somuncu`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Valerius Somuncu`(person)
- `Seelache 250, 2294 Schloßhof, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)
- `84-691/1997`(tax_number)

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/136814.1`) (sent_id: `deanon_BFG_20260814_TEST/136814.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter in der Beschwerdesache  Prof.in Alma Siegers, Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich, über die Beschwerde vom 11. August 2020 gegen den Bescheid des  Finanzamtes Österreich vom 22. Juli 2020 betreffend Einkommensteuer 2014, Steuernummer  37-792/2472, zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Alma Siegers` — partial — pred is substring of gold: `Prof.in Alma Siegers`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Judith Leodolter`(person)
- `Prof.in Alma Siegers`(person)
- `Bettelwurfweg 13, 4674 Altenhof am Hausruck, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `37-792/2472`(tax_number)

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/137297.1`) (sent_id: `deanon_BFG_20260814_TEST/137297.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Mag. Hon.-Prof. Engelbert Voglsang  in der Beschwerdesache DDr.in Magdalena Holtzbecher, Bakk. rer. nat.,  Kefergutstraße 149, 5152 Dorfbeuern, Österreich, über die Beschwerde vom 29.3.2020 gegen den Bescheid des Finanzamtes  Wien 1/23 vom 12.3.2020 betreffend Einkommensteuer (Arbeitnehmerveranlagung) für das  Jahr 2019 zu Recht erkannt:   I. Der angefochtene Bescheid wird gemäß § 279 BAO abgeändert.

**False Positives:**

- `Magdalena Holtzbecher` — partial — pred is substring of gold: `DDr.in Magdalena Holtzbecher, Bakk. rer. nat.`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Hon.-Prof. Engelbert Voglsang`(person)
- `DDr.in Magdalena Holtzbecher, Bakk. rer. nat.`(person)
- `Kefergutstraße 149, 5152 Dorfbeuern, Österreich`(address)
- `Finanzamtes  Wien 1/23`(organisation)

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin IBV in der Beschwerdesache Ing. Nicoletta Papastergios,  Walchmannberg 81C, 8342 Dietersdorf am Gnasbach, Österreich  über die Beschwerde vom 12. April 2022 gegen den Bescheid des Finanzamtes  Österreich vom 31. März 2022 betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2019  Steuernummer 94-528/7027  zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

**False Positives:**

- `Nicoletta Papastergios` — partial — pred is substring of gold: `Ing. Nicoletta Papastergios`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Ing. Nicoletta Papastergios`(person)
- `Walchmannberg 81C, 8342 Dietersdorf am Gnasbach, Österreich`(address)
- `Finanzamtes  Österreich`(organisation)
- `94-528/7027`(tax_number)

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache DDr. Ali Franzel, Oberwirtsweg 5, 8562 Bubendorf, Österreich, über die Beschwerde vom 13. Juli 2021 gegen  den Bescheid des Finanzamtes Österreich vom 29. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, Steuernummer 63-470/7314  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

**False Positives:**

- `Ali Franzel` — partial — pred is substring of gold: `DDr. Ali Franzel`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. David Hell LL.B. LL.M.`(person)
- `DDr. Ali Franzel`(person)
- `Oberwirtsweg 5, 8562 Bubendorf, Österreich`(address)
- `Finanzamtes Österreich`(organisation)
- `63-470/7314`(tax_number)

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/140432.1`) (sent_id: `deanon_BFG_20260814_TEST/140432.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Priv.-Doz. Hon.-Prof. David Goldvogel  in der Beschwerdesache Dr. Leroy Stras,  Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich, vertreten durch Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H., Madersbacherweg 26, 6300 Wörgl, gegen den von der belangten Behörde Finanzamt  Österreich am 7. Dezember 2022 ausgefertigten Bescheid, mit dem der Antrag des  Beschwerdeführers vom 11. November 2022 auf Wiederaufnahme des mit  Einkommensteuerbescheid 2019 abgeschlossenen Verfahrens abgewiesen wurde, zu Recht  erkannt:  I. Die Bescheidbeschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

**False Positives:**

- `Leroy Stras` — partial — pred is substring of gold: `Dr. Leroy Stras`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr. Priv.-Doz. Hon.-Prof. David Goldvogel`(person)
- `Dr. Leroy Stras`(person)
- `Dr. Otto Scheff-Weg 2, 4791 Höcking, Österreich`(address)
- `Schrettl Herbert & Partner Steuerberatungsgesellschaft  m.b.H.`(organisation)
- `Finanzamt  Österreich`(organisation)

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/143386.1`) (sent_id: `deanon_BFG_20260814_TEST/143386.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Gabriele Bornscheid  in der Beschwerdesache   DDr. Jens Oberquelle, Obermayrfeld 7, 7302 Nikitsch, Österreich,   über die Beschwerden vom 18. Mai 2017 gegen die Bescheide des Finanzamtes Graz-Stadt vom  11. April 2017 betreffend Wiederaufnahme des Verfahrens zur Vorsteuererstattung 2012  sowie Vorsteuererstattung 2012, 2013 und 2014 zu Recht erkannt:   I. Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Jens Oberquelle` — partial — pred is substring of gold: `DDr. Jens Oberquelle`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag.a Gabriele Bornscheid`(person)
- `DDr. Jens Oberquelle`(person)
- `Obermayrfeld 7, 7302 Nikitsch, Österreich`(address)
- `Finanzamtes Graz-Stadt`(organisation)

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/143808.1`) (sent_id: `deanon_BFG_20260814_TEST/143808.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch die Richterin Dr.in Danielle Merte  in der Beschwerdesache Mag.a Susanne Groesche Unternurpensalm 12, 5141 Moosdorf, Österreich  vertreten durch CONSULTATIO Steuerberatung GmbH & Co KG, Karl-Waldbrunner-Platz  1, 1210 Wien, über die Beschwerde vom 8. Juni 2015 gegen die Bescheide des Finanzamtes  Wien 1/23 vom 7. Mai 2015 (jetzt Finanzamt für Großbetriebe), Steuernummer  76-369/9701, betreffend   1. Wiederaufnahme des Verfahrens zur Festsetzung der Energieabgabenvergütung für   A. 2005 – 2008,    Bäder 2005 – 2008,         Büchereien 2005 – 2008,  Bf. Kindergärten 2005 – 2008,      E. Stadion 2007,  B. Stadion 2005 – 2007,     C. Eishalle 2006, 2007,   D.Bad 2005 – 2007 und      F. Stadion 2006 und 2007  2.

**False Positives:**

- `Susanne Groesche Unternurpensalm` — positional overlap with gold: `Mag.a Susanne Groesche`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Dr.in Danielle Merte`(person)
- `Mag.a Susanne Groesche`(person)
- `Unternurpensalm 12, 5141 Moosdorf, Österreich`(address)
- `CONSULTATIO Steuerberatung GmbH & Co KG`(organisation)
- `Finanzamtes  Wien 1/23`(organisation)
- `Finanzamt für Großbetriebe`(organisation)
- `76-369/9701`(tax_number)

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Vorsitzenden A und die Richterin   Priv.-Doz.in Annkathrin Czesielski  sowie die fachkundigen Laienrichter B und C in der Beschwerdesache Prof.in Esra Konwischer,  Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich, vertreten durch Zachmann & Partner Rechtsanwälte, Fritzstraße 2, D-82140  Olching, über die Beschwerde vom 11. August 2016 gegen den Sammelbescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel (nunmehr: Finanzamt Österreich)  vom 25. Juli 2016, ErfNr u.a., betreffend   1. Festsetzung der Gebühren gemäß § 14 TP 6 Abs. 2 Z 1, TP 2 Abs. 1 Z 1, TP 5 Abs. 1 und        TP 14 Abs. 1 Gebührengesetz 1957 (GebG), BGBl 1957/267 idgF., sowie  2. Festsetzung der Gebührenerhöhung gemäß § 9 Abs. 1 GebG 1957  zu Recht erkannt:   Die Beschwerde wird insgesamt als unbegründet abgewiesen.

**False Positives:**

- `Esra Konwischer` — partial — pred is substring of gold: `Prof.in Esra Konwischer`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Priv.-Doz.in Annkathrin Czesielski`(person)
- `Prof.in Esra Konwischer`(person)
- `Alpe Greußings Wildmoos 198, 4925 Lungdorf, Österreich`(address)
- `Finanzamtes für Gebühren`(organisation)
- `Finanzamt Österreich`(organisation)

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/148343.1`) (sent_id: `deanon_BFG_20260814_TEST/148343.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Hon.-Prof.in Evamaria Fränzl  in der Beschwerdesache  Prof. Raphael Grieben, Habegg 37, 5120 Pirach, Österreich, vertreten durch BDO Austria GmbH Wirtschaftsprüfungs- und  Steuerberatungsgesellschaft, Am Belvedere 4, 1100 Wien,   betreffend Beschwerde vom 21. Dezember 2023 gegen den Bescheid des Finanzamt Graz-Stadt  vom  30. August 2023 betreffend Vorsteuererstattung 2022 beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit. a BAO als nicht zulässig zurückgewiesen.

**False Positives:**

- `Raphael Grieben` — partial — pred is substring of gold: `Prof. Raphael Grieben`

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `Gutachten_Dr_Name` 

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
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 1 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_287`)


Die Reduktion des Grades der Behinderung von 50% auf 30% erscheint u.a. auch an folgenden  beispielhaft herangezogenen Umständen nachvollziehbar:   - War im ersten Bundessozialamts-Gutachten vom Juni 2016, gestützt auf damals vorgelegte  relevante Befunde, im Ergebnis der durchgeführten Begutachtung u.a. Dyskalkulie angeführt  worden und daraus die angeführte Entwicklungsstörung diagnostiziert worden,   so findet sich in dem – beiden BSA-Gutachten von Oktober 2019 und vom August 2020 –  zugrunde gelegten Befund der klinischen Psychologin vom 26. Juni 2019 die ausdrückliche  Feststellung: Es liegt keine Dyskalkulie vor (aus der retrospektiven Sicht wohl: nicht mehr vor)  (vgl. die oben wiedergegebenen Gutachten).

**False Positives:**

- `Gutachten von Oktober` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Richter_Name_Context` 🔇

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

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
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 3 | 1614 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_12`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_59`)


Vergl. hierzu "Österreichische Gesellschaft für Europapolitik - Prof. Dr. Franz Leidenmühler" und  die Stellungnahme der Volksanwaltschaft - MR Dr. Heidi Pacher vom 15.01.2018 an Frau Mag.  Dr. Juliane Bogner Strauß.

**False Positives:**

- `Mag` — partial — pred is substring of gold: `Mag.  Dr. Juliane Bogner Strauß`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Österreichische Gesellschaft für Europapolitik`(organisation)
- `Prof. Dr. Franz Leidenmühler`(person)
- `MR Dr. Heidi Pacher`(person)
- `Mag.  Dr. Juliane Bogner Strauß`(person)

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/139395.1`) (sent_id: `deanon_BFG_20260814_TEST/139395.1_14`)


Ziel der Bautätigkeit sei die Schaffung einer gemeinsamen  Wohnung für seine Familie, dh für seine Frau Prof. Engelbert Thuerrigl  verehelichte A, seine Kinder und für ihn  selbst, gewesen.

**False Positives:**

- `Prof` — partial — pred is substring of gold: `Prof. Engelbert Thuerrigl`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Prof. Engelbert Thuerrigl`(person)

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

## `Maga_Title` 🔇

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

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
| `person` | 0 | 0 | 1614 |

</details>

---

</details>

---

<details>
<summary>❌ False Negatives (939, showing 50)</summary>

**Example 0** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_3`)

Entscheidungsgründe  I. Verfahrensgang  Das Finanzamt erließ am 06.07.2023 einen Bescheid an die Beschwerdeführerin (nachfolgend  „Bf“) über die Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für den Zeitraum  November 2022 bis Juni 2023 für das Kind Heidemarie Fitzenreiter, verbunden mit der Rückforderung  der aus der Kinderstaffel resultierenden anteiligen Familienbeihilfe für die Kinder **Florens Meulenkamp**  und Sara Liebreich.

- missed: `Florens Meulenkamp` (person)
- predicted in sentence: —

**Example 1** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_215`)

Wenn der Sachwalter die Einvernahme von Prof. Maida als Zeugin beantragt, so erachtet das  Bundesfinanzgericht eine derartige Einvernahme als nicht zielführend, da der Bf. erstmals bei  der **Neurologin Univ.Prof. Dr. Eva Maria Maida** im Jahr 2006 wegen seiner Erkrankung  (Multiple Sklerose) in Behandlung war und diese somit über den Gesundheitszustand des Bf.  für einen Zeitraum, der ca. 30 Jahre zurückliegt, naturgemäß nur Vermutungen anstellen kann.

- missed: `Neurologin Univ.Prof. Dr. Eva Maria Maida` (person)
- predicted in sentence: `Dr. Eva Maria Maida`

**Example 2** (doc_id: `deanon_BFG_20260814_TEST/128911.1`) (sent_id: `deanon_BFG_20260814_TEST/128911.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Gabriele Grossgut-Palotás** in der  Beschwerdesache Lewis Rzehula, Neustädterstraße 3, 9560 Wabl, Österreich, über die Beschwerde vom 4. Februar 2019  gegen den Bescheid des FA XYZ vom 22. Jänner 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2017 Steuernummer 43-839/6567  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dr. Gabriele Grossgut-Palotás` (person)
- predicted in sentence: `Dr. Gabriele Grossgut`, `Lewis Rzehula`

**Example 3** (doc_id: `deanon_BFG_20260814_TEST/145608.1`) (sent_id: `deanon_BFG_20260814_TEST/145608.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Mag. Dieter Fröhlich** über die Beschwerde  des Jeanne Pavlovitsch, Döbinggasse 9, 4153 Kirchbach, Österreich, vom 5. August 2024, gegen den Zurückweisungsbescheid des  Magistrates der Stadt Wien, Magistratsabteilung 67 vom 31. Juli 2024, GZ. MA67/GZ/2024, mit  dem der Einspruch vom 12. Juni 2024 gegen die Strafverfügung vom 4. Juni 2024, mit  derselben Geschäftszahl, gemäß § 13 Abs. 3 AVG iVm § 24 VStG 1991 zurückgewiesen wurde,  zu Recht:  Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und  wird der oben genannte, angefochtene Zurückweisungsbescheid bestätigt.

- missed: `Mag. Dieter Fröhlich` (person)
- predicted in sentence: —

**Example 4** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_15`)

Zur Berechnung der Bemessungsgrundlage der Wettgebühr enthält die Selbstanzeige folgende  Ausführungen:  „Für die Berechnung der Bemessungsgrundlage der Wettgebühr gemäß § 33 TP 17 Abs 3 GebG  für den gegenständlichen Zeitraum wurden in einem ersten Schritt Einsätze jener Kunden  herangezogen, die bei der Registrierung auf der Website https**://www.Oswald Rübberdt** .com  „Österreich“ aus einem Drop-Down Menü als Wohnsitzland ausgewählt und eine  österreichische Registrierungsadresse angegeben haben.

- missed: `://www.Oswald Rübberdt` (person)
- predicted in sentence: —

**Example 5** (doc_id: `deanon_BFG_20260814_TEST/134370.1`) (sent_id: `deanon_BFG_20260814_TEST/134370.1_12`)

**Petra Port**  hielt es ernstlich für möglich und fand sich damit ab, als Einzelunternehmer unter  Verletzung der abgabenrechtlichen Anzeige-, Offenlegungs- und Wahrheitspflicht hinsichtlich  der Einkommensteuer 2012 in der Höhe von € 7.465,00 eine Verkürzung zu bewirken.

- missed: `Petra Port` (person)
- predicted in sentence: —

**Example 6** (doc_id: `deanon_BFG_20260814_TEST/133922.1`) (sent_id: `deanon_BFG_20260814_TEST/133922.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die vorsitzende Richterin Mag. Aloisia Bergauer und die  beisitzende Richterin **Mag. Andrea Ebner** sowie die fachkundigen Laienrichter Mag. Johannes  Denk und Friedrich Nagl in der Beschwerdesache Dipl. Kfm. Rüdiger Schäffler, Anton-Dengler-Gasse 16, 8330 Krennach, Österreich, vertreten durch  BONAFIDE Treuhand- und Revisionsgesellschaft m.b.H., Berggasse 10, 1090 Wien, über die  Beschwerde vom 17. Oktober 2011 gegen die Bescheide des Finanzamtes Wien 12/13/14  Purkersdorf vom 11. Oktober 2011 betreffend Einkommensteuer für die Jahre 2006 bis 2009  nach Durchführung einer mündlichen Verhandlung beschlossen:  Die Beschwerde wird gemäß § 260 Abs. 1 lit a Bundesabgabenordnung (BAO) als nicht zulässig  zurückgewiesen.

- missed: `Mag. Andrea Ebner` (person)
- predicted in sentence: —

**Example 7** (doc_id: `deanon_BFG_20260814_TEST/131446.1`) (sent_id: `deanon_BFG_20260814_TEST/131446.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Ulrike Nussbaumer LL.M. M.B.L.** in der  Beschwerdesache Eleonore Sawadzki, Bakk. art., Weintraubengasse 36, 9073 Aich, Österreich, über die Beschwerde vom 23. Mai 2017 gegen  den Bescheid des Finanzamtes Österreich vom 22. Mai 2017 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:   1.

- missed: `Mag. Ulrike Nussbaumer LL.M. M.B.L.` (person)
- predicted in sentence: `M.`, `Eleonore Sawadzki`

**Example 8** (doc_id: `deanon_BFG_20260814_TEST/145343.1`) (sent_id: `deanon_BFG_20260814_TEST/145343.1_2`)

Das Bundesfinanzgericht hat durch den Senatsvorsitzenden Dr. Ralf Schatzl, den Richter Mag.  Thomas Stieger sowie die fachkundigen **Laienrichter Ing. Helmut Marchhart** und Mag. Christian  Berger BA MSc LL.M. in der Beschwerdesache Franziskus Schymitzek, Gössering 48, 9314 St. Martin, Österreich, vertreten durch  KPMG Alpen-Treuhand GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft,  Krassnigstr 36, 9020 Klagenfurt am Wörthersee, über die Beschwerde vom 25. Oktober 2018  gegen die Bescheide des Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom  28. September 2018 betreffend Anspruchszinsen (§ 205 BAO) 2016 und Einkommensteuer  (Arbeitnehmerveranlagung) 2016 in der Sitzung am 5. Juli 2024 zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Laienrichter Ing. Helmut Marchhart` (person)
- predicted in sentence: `Dr. Ralf Schatzl`, `Ing. Helmut Marchhart`, `M.`, `Franziskus Schymitzek`

**Example 9** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_89`)

Lebt  seit 2005 in teilbetreuter intensiver WG/Verein B. Seit ca. 2012 von **Dr. Hofer-Zeni**  besachwaltet.

- missed: `Dr. Hofer-Zeni` (person)
- predicted in sentence: `Dr. Hofer`

**Example 10** (doc_id: `deanon_BFG_20260814_TEST/143828.1`) (sent_id: `deanon_BFG_20260814_TEST/143828.1_2`)

Herrn Dieter Avemaria, geboren 1980, Retzenweg 1, 8504 Tobis, Österreich  und   2. die **Engelbert Schefe**, Retzenweg 1, 8504 Tobis, Österreich   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und 49 Abs. 1 lit. a des Finanzstrafgesetzes (FinStrG) über die Beschwerde  des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 gegen das Erkenntnis  des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde vom 9. Oktober  2023, SpS-1, beschlossen:  Die Beschwerde des Beschuldigten und des belangten Verbandes vom 16. Jänner 2024 wird  gemäß § 156 Abs. 4 FinStrG als verspätet zurückgewiesen.

- missed: `Engelbert Schefe` (person)
- predicted in sentence: `Dieter Avemaria`

**Example 11** (doc_id: `deanon_BFG_20260814_TEST/145488.1`) (sent_id: `deanon_BFG_20260814_TEST/145488.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter **Mag. Andreas Stanek** in der Beschwerdesache  der Annalena Ellinghoven, Bergerweg 62, 3474 Kollersdorf, Österreich, gegen den Bescheid des Finanzamtes Österreich vom  11. August 2020 hinsichtlich Einkommensteuer (Arbeitnehmerveranlagung) 2019,  Steuernummer 27-565/5032, beschlossen:  Der Vorlageantrag vom 25. Februar 2024 wird gemäß § 260 Abs. 1 lit. b Bundesabgabenordung  (BAO) in Verbindung mit § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht  zurückgewiesen.

- missed: `Mag. Andreas Stanek` (person)
- predicted in sentence: `Annalena Ellinghoven`

**Example 12** (doc_id: `deanon_BFG_20260814_TEST/148990.1`) (sent_id: `deanon_BFG_20260814_TEST/148990.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **MMag. Gerald Erwin Ehgartner** in der  Beschwerdesache Wolf Klavs, Steuernummer 55-681/5339, über die Beschwerde vom 9. Mai  2025 gegen den Bescheid des Finanzamtes Österreich vom 7. Mai 2025 betreffend  Einkommensteuer 2024 zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `MMag. Gerald Erwin Ehgartner` (person)
- predicted in sentence: `Wolf Klavs`

**Example 13** (doc_id: `deanon_BFG_20260814_TEST/141412.1`) (sent_id: `deanon_BFG_20260814_TEST/141412.1_7`)

Gleichzeitig mit der Beschwerde wird ein Antrag auf  Aussetzung der Einhebung gemäß § 212a BAO gestellt. Auf Seite 2 wird darauf hingewiesen,  dass der Bf „in der außen bezeichneten Finanzsache“ **Mehmet Köprücü**  Vollmacht erteilt  hat, wobei sich der gefertigte Anwalt auf die ihm erteilte Vollmacht beruft.

- missed: `Mehmet Köprücü` (person)
- predicted in sentence: —

**Example 14** (doc_id: `deanon_BFG_20260814_TEST/130252.1`) (sent_id: `deanon_BFG_20260814_TEST/130252.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Fabienne Kattner  in der Beschwerdesache Cornelia Özgür,  Hofbauer-Straße 6, 9854 Krainberg, Österreich, vertreten durch **Thomas Krampl**, Alter Platz 35 Tür 1, 9020 Klagenfurt am  Wörthersee, über die Beschwerde vom 12. Dezember 2018 gegen den Bescheid des  Finanzamtes für Gebühren, Verkehrsteuern und Glücksspiel vom 20. November 2018  betreffend Säumniszuschlag 2018 Steuernummer zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Thomas Krampl` (person)
- predicted in sentence: `Univ.-Prof.in Fabienne Kattner`

**Example 15** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_5`)

Entscheidungsgründe  I. Verfahrensgang  Mit 1.10.2018 wurde dem Zollamt bekannt gegeben, dass der Hof („Hofname“) samt einem  Brenngerät mit eee2011 von **Quentin Schwartkopp**  seinem Sohn Sohn übergeben wurde.

- missed: `Quentin Schwartkopp` (person)
- predicted in sentence: —

**Example 16** (doc_id: `deanon_BFG_20260814_TEST/139044.1`) (sent_id: `deanon_BFG_20260814_TEST/139044.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag.a Esmeralda Fietze**  in der Beschwerdesache Norbert Hummels,  Am Käferberg 232, 7425 Weinberg im Burgenland, Österreich, über die Beschwerde vom 18. Mai 2022 gegen die Bescheide des Finanzamtes  Österreich vom 25. April 2022 betreffend Gebühren 2021 sowie Gebührenerhöhung zu Recht  erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag.a Esmeralda Fietze` (person)
- predicted in sentence: `Norbert Hummels`

**Example 17** (doc_id: `deanon_BFG_20260814_TEST/129190.1`) (sent_id: `deanon_BFG_20260814_TEST/129190.1_3`)

Begründung  Aus den dem Gericht vorgelegten Unterlagen und dem elektronischen Akt ist ersichtlich, dass  die belangte Behörde (FA) am 6.3.2018 mittels Bescheid gemäß § 92 Abs. 1 lit. c BAO  feststellte, dass hinsichtlich des **Daniel Parys** (Beschwerdeführer, Bf.) im Zeitraum 2014 bis 2016  keine Unternehmereigenschaft vorlag.

- missed: `Daniel Parys` (person)
- predicted in sentence: —

**Example 18** (doc_id: `deanon_BFG_20260814_TEST/129120.1`) (sent_id: `deanon_BFG_20260814_TEST/129120.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Univ.-Prof.in Dr.in Hemma Ramelow**  in der Beschwerdesache des  Mag. Damian Wiecher, Strasshof an der Nordbahn 186, 4443 Ebersegg, Österreich, vertreten durch Hofmann - Wirtschaftstreuhand - Steuerberater  KG - Steuerbüro Specht, Kirchweg 11, 6600 Reutte, über die Beschwerde vom 17. September  2018 gegen den Bescheid des Finanzamt Wien 2/20/21/22  vom 21. August 2018 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 zu Recht erkannt:     Die Beschwerde wird als unbegründet abgewiesen.

- missed: `Univ.-Prof.in Dr.in Hemma Ramelow` (person)
- predicted in sentence: `Dr.in Hemma Ramelow`, `Damian Wiecher`

**Example 19** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Andrea Ebner in der  Beschwerdesache **Dominika Oehlerich, BEd**, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Dominika Oehlerich, BEd` (person)
- predicted in sentence: `Dominika Oehlerich`

**Example 20** (doc_id: `deanon_BFG_20260814_TEST/133620.1`) (sent_id: `deanon_BFG_20260814_TEST/133620.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Dr. Viktoria Blaser in der Beschwerdesache  Mag. Sven Weichmann, Kellerweg 13, 9061 Ziegelsdorf, Österreich, vertreten durch **Mag. Kurt Kreith**, Am Hof 5 Tür 11, 1010 Wien,  betreffend Beschwerde vom 21. September 2020 gegen den Bescheid des Finanzamtes Baden  Mödling vom 20. August 2020 zu Steuernummer 78-738/0573  betreffend  Einkommensteuer 2018 beschlossen:  Die Beschwerde gilt gemäß § 278 Abs. 1 lit. b iVm § 85 Abs. 2 BAO als zurückgenommen.

- missed: `Mag. Kurt Kreith` (person)
- predicted in sentence: `Dr. Viktoria Blaser`, `Sven Weichmann`, `vertreten durch Mag. Kurt Kreith`

**Example 21** (doc_id: `deanon_BFG_20260814_TEST/134237.1`) (sent_id: `deanon_BFG_20260814_TEST/134237.1_2`)

Das Bundesfinanzgericht hat durch den RichterR, über die Beschwerde der **Bodo Saday**, Alois Windisch-Straße 1, 5121 Hofweiden, Österreich, vom 14. Juli 2021, gegen das Straferkenntnis des Magistrates der Stadt Wien,  Magistratsabteilung 67, vom 28. Juni 2021, GZ. MA67/Zahl/2021, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Parkometerabgabeverordnung, ABl. der Stadt Wien  Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 46/2016, in Verbindung mit § 4 Abs. 1  Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, zu Recht  erkannt:    Gemäß § 50 VwGVG wird die Beschwerde als unbegründet abgewiesen und das ange- fochtene Straferkenntnis bestätigt.

- missed: `Bodo Saday` (person)
- predicted in sentence: —

**Example 22** (doc_id: `deanon_BFG_20260814_TEST/140447.1`) (sent_id: `deanon_BFG_20260814_TEST/140447.1_1`)

IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Feldkirch 1 des Bundesfinanzgerichtes hat durch den Senatsvorsitzenden  Mag. Josef Ungericht, den Richter Mag. Armin Treichl und die fachkundigen Laienrichter Mag.a  Patricia Kathan-Simma und Mag. Norbert Metzler in Gegenwart der Schriftführerin **Isabella  Alexandra Längle** in der Finanzstrafsache gegen VetR Vivian Hirtel, Litzlberger Straße 14, 8530 Kresbach, Österreich, vertreten durch Dr.  jur.

- missed: `Isabella  Alexandra Längle` (person)
- predicted in sentence: `Mag. Josef Ungericht`

**Example 23** (doc_id: `deanon_BFG_20260814_TEST/142559.1`) (sent_id: `deanon_BFG_20260814_TEST/142559.1_92`)

So bezog **Quentin Schwartkopp**  diesbezüglich auch keinerlei  Einkünfte, die den Schluss zuließen, dass er tatsächlich fruchtgenussberechtigt gewesen sein  soll.

- missed: `Quentin Schwartkopp` (person)
- predicted in sentence: —

**Example 24** (doc_id: `deanon_BFG_20260814_TEST/128950.1`) (sent_id: `deanon_BFG_20260814_TEST/128950.1_5`)

Entscheidungsgründe  I. Verfahrensgang  Mit der Beschwerdeführerin (Bf) **Siegfried Basyurt**, Beruf Hausfrau, wurde am Finanzamt X am  27.7.2010 zwecks "Feststellung des Mittelpunktes der Lebensinteressen" eine Niederschrift  folgenden Inhaltes aufgenommen:  "Frau Bf ist mit den beiden Kindern A (geb. 2003) und B (2001) mit Jänner 2010 nach Adr1,  zugezogen.

- missed: `Siegfried Basyurt` (person)
- predicted in sentence: `Bf`, `Bf`

**Example 25** (doc_id: `deanon_BFG_20260814_TEST/141600.1`) (sent_id: `deanon_BFG_20260814_TEST/141600.1_2`)

Das Bundesfinanzgericht hat durch den Richter Mag. Dieter Fröhlich über die  Bescheidbeschwerde des **Patrick Poppenheger**, Steuernummer 23-019/0780,   Str.1, O1, vertreten durch Crowe SOT GmbH Wirtschaftsprüfung- und  Steuerberatungsgesellschaft, Ruster Straße 91, 7000 Eisenstadt, vom 15.07.2020 gegen den  Einkommensteuerbescheid für das Jahr 2018 des Finanzamtes Bruck Eisenstadt Oberwart  (nunmehr FA Österreich), vom 29.06.2020, zugestellt am 02.07.2020, nach der im Beisein des  Schriftführers Dietmar Gratz am 29.06.2023 durchgeführten mündlichen Verhandlung  zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen und der  angefochtene Bescheid abgeändert.

- missed: `Patrick Poppenheger` (person)
- predicted in sentence: —

**Example 26** (doc_id: `deanon_BFG_20260814_TEST/132918.1`) (sent_id: `deanon_BFG_20260814_TEST/132918.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Andrea Müller-Dobler MBA MSc in der  Verwaltungsstrafsache gegen **Hademar Sachteleben, MSc**, Fröhlichgasse 31, 3244 Hofstetten, Österreich, über die zwei Beschwerden des  Beschuldigten gegen die nachfolgend angeführten zwei Vollstreckungsverfügungen (VVF) des  Magistrates der Stadt Wien, jeweils betreffend Zwangsvollstreckung wegen Nichtbezahlung  der rechtskräftigen Strafe auf Grund des nachfolgend angeführten Erkenntnis des  Bundesfinanzgerichtes, jeweils betreffend eine Verwaltungsübertretung nach § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006,

- missed: `Hademar Sachteleben, MSc` (person)
- predicted in sentence: —

**Example 27** (doc_id: `deanon_BFG_20260814_TEST/144910.1`) (sent_id: `deanon_BFG_20260814_TEST/144910.1_1`)

BESCHLUSS  Das Bundesfinanzgericht fasst durch die Richterin Mag. Maria Daniel über die Beschwerde der Diana Wüste,Schönangerweg 35, 4925 Gumpling, Österreich, vertreten durch **Ing. Mag. Dr. Roland Erwin Hansely**, Mahlerstraße 13 Tür 3,  1010 Wien, wegen behaupteter rechtswidriger Ausübung verwaltungsbehördlicher Befehls-  und Zwangsgewalt durch Organe des Zollamtes Österreich am 19.11.2023 durch Ausübung  psychischen Zwangs den Beschluss:   Die Maßnahmenbeschwerde vom 19.12.2023 wird als unzulässig zurückgewiesen.

- missed: `Ing. Mag. Dr. Roland Erwin Hansely` (person)
- predicted in sentence: `Mag. Dr. Roland Erwin Hansely`

**Example 28** (doc_id: `deanon_BFG_20260814_TEST/143465.1`) (sent_id: `deanon_BFG_20260814_TEST/143465.1_37`)

Auch die Bf gab in  einem von ihr ausgefüllten und am 22.06.2023 unterzeichneten Datenblatt zur Überprüfung  des Anspruches auf Familienbeihilfe an, dass ihre Tochter **Heidemarie Fitzenreiter**  ab 05.09.2022 bis  12.06.2023 am Neve College for Woman ein Seminar absolviert habe (Art der Ausbildung nach  Angabe der Bf: „Jeschiva for woman“).

- missed: `Heidemarie Fitzenreiter` (person)
- predicted in sentence: —

**Example 29** (doc_id: `deanon_BFG_20260814_TEST/144458.1`) (sent_id: `deanon_BFG_20260814_TEST/144458.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Christian Seywald** in der  Beschwerdesache Adriana Pennewitz, Warbach 17, 9122 Wasserhofen, Österreich, (Beschwerdeführerin, abgekürzt: Bf.), über die  Beschwerde der Beschwerdeführerin vom 31. Oktober 2023 gegen den  Einkommensteuerbescheid 2022 des Finanzamtes Österreich (belangte Behörde) vom  18. Oktober 2023 zu Steuernummer 92-394/6950  zu Recht erkannt:  Der Beschwerde wird stattgegeben.

- missed: `Mag. Christian Seywald` (person)
- predicted in sentence: `Adriana Pennewitz`

**Example 30** (doc_id: `deanon_BFG_20260814_TEST/138894.1`) (sent_id: `deanon_BFG_20260814_TEST/138894.1_240`)

Psychologin, 26.06.2019 (vgl. Vorgutachten): Überdurchschnittlich logisch- abstrakte Denkleistung Basisintelligenzquotient 120, durchschnittliche visuell-akustische  Reaktionsfähigkeit, Konzentration Ausdauer gerade noch durchschnittlich, Legasthenie alle  3 Teilbereiche betreffend, Defizite im Leistungsbereich F81 Schulunlust und Prüfungsangst   2019-12-18: Dr. **Mag. Sch.** Psychologin: Legasthenie, Teilleistungsstörung   2020-02-14: Waldorfschule - Zeugnis: Deutsch genügend, Mathematik nicht genügend, Englisch  nicht genügend)   2020-05-27:Emma Richardon HNO: Dg: Verdacht auf auditive Verarbeitungsstörung,  Teilleistungsschwächen   2020-06-10:Mathias Barrois Kinderpsychiater: F90.0 ADHS, Therapie: Ritalin 10mg 2-1-0   Der Untersuchungsbefund dieses Gutachtens wurde wiederum als normal beschrieben  (Allgemeinzustand: guter AZ;

- missed: `Mag. Sch.` (person)
- predicted in sentence: `Dr. Mag`

**Example 31** (doc_id: `deanon_BFG_20260814_TEST/133640.1`) (sent_id: `deanon_BFG_20260814_TEST/133640.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  **VetR Dipl. Kff. Ingrid Klockgiesser**, Etschmayerstraße 4, 4720 Baumgarten, Österreich  über die Beschwerde vom 29. März 2018 gegen den Bescheid des  Finanzamtes Bregenz vom 2. März 2018 betreffend Berichtigung des Bescheides über die  Feststellung von Einkünften gemäß § 188 BAO für das Jahr 2012 gemäß § 293b BAO zu Recht  erkannt:  I. Der angefochtene Bescheid wird - ersatzlos - aufgehoben.

- missed: `VetR Dipl. Kff. Ingrid Klockgiesser` (person)
- predicted in sentence: —

**Example 32** (doc_id: `deanon_BFG_20260814_TEST/139586.1`) (sent_id: `deanon_BFG_20260814_TEST/139586.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache **DDr. Ali Franzel**, Oberwirtsweg 5, 8562 Bubendorf, Österreich, über die Beschwerde vom 13. Juli 2021 gegen  den Bescheid des Finanzamtes Österreich vom 29. Juni 2021 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2019, Steuernummer 63-470/7314  zu Recht erkannt:   I. Die Beschwerde wird als unbegründet abgewiesen.

- missed: `DDr. Ali Franzel` (person)
- predicted in sentence: `M.`, `Ali Franzel`

**Example 33** (doc_id: `deanon_BFG_20260814_TEST/142513.1`) (sent_id: `deanon_BFG_20260814_TEST/142513.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr. Judith Leodolter als Vorsitzende, die  Richterin Mag. Andrea Proidl als beisitzende Richterin sowie Mag. Martin Saringer und **Mag.  Harald  Zeller** als fachkundige Laienrichter in der Beschwerdesache Priv.-Doz.in Diana Pöppel, Spitalbergweg 20, 4775 Wagholming, Österreich,  vertreten durch Baldinger & Partner Unternehmens- und Steuerberatung GmbH, Ferrogasse  35, 1180 Wien, über die Beschwerde vom 9. September 2017 gegen die Bescheide des  Finanzamtes Wien 4/5/10 vom 17. Juli 2017 betreffend Umsatzsteuer 2010-2016,  Steuernummer 56-661/5349, nach Durchführung einer mündlichen Verhandlung am 9. Juni  2023 in Anwesenheit des Schriftführers Dietmar Gratz zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag.  Harald  Zeller` (person)
- predicted in sentence: `Dr. Judith Leodolter`, `Priv.-Doz.in Diana Pöppel`

**Example 34** (doc_id: `deanon_BFG_20260814_TEST/135772.1`) (sent_id: `deanon_BFG_20260814_TEST/135772.1_54`)

**Oswald Rübberdt**  bietet den Kunden Einzahlungs- bzw. Willkommensboni sowie Freispiele an, wobei  die Gewährung dieser Boni besonderen von den jeweiligen Boni abhängige  Nutzungsbedingungen unterliegt (Beilage III „Boni Nutzungsbedingungen“).

- missed: `Oswald Rübberdt` (person)
- predicted in sentence: —

**Example 35** (doc_id: `deanon_BFG_20260814_TEST/147876.1`) (sent_id: `deanon_BFG_20260814_TEST/147876.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter **Mag. Josef Ungericht** in der Beschwerdesache  der Yorick Lemgen, Bürstenbachweg 2, 2295 Zwerndorf, Österreich, vertreten durch die Ernst & Young Steuerberatungsgesellschaft  m.b.H., Wagramer Straße 19, IZD-Tower (Postfach 89), 1220 Wien, über die Beschwerde vom  8. April 2025 gegen den Bescheid des Finanzamtes für Großbetriebe, Postfach 251, 1000 Wien,  vom 4. April 2025 betreffend die Festsetzung der Stabilitätsabgabe 2024 (Steuernummer xxx)  zu Recht erkannt:  Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Josef Ungericht` (person)
- predicted in sentence: `Yorick Lemgen`

**Example 36** (doc_id: `deanon_BFG_20260814_TEST/148797.1`) (sent_id: `deanon_BFG_20260814_TEST/148797.1_1`)

BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin **Mag.Dr. Birgitt Koran** über den Antrag des  Stephanie Luippold, Straße IX 48, 4153 Eschernhof, Österreich, vom 7. Mai 2025 auf Verfahrenshilfe (Beigebung eines  Verteidigers) für ein Beschwerdeverfahren gegen eine Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA 32, vom 15. April 2025, GZ.  MA67/GZ1/2024, betreffend Zwangsvollstreckung wegen Nichtbezahlung der rechtskräftigen  Strafe auf Grund des Beschlusses des Bundesfinanzgerichtes vom 4. Februar 2025, GZ.  RV/GZ2/2025, beschlossen:  I. Der Antrag auf Verfahrenshilfe (Beigebung eines Verfahrenshilfeverteidigers) wird  abgewiesen.

- missed: `Mag.Dr. Birgitt Koran` (person)
- predicted in sentence: `Dr. Birgitt Koran`

**Example 37** (doc_id: `deanon_BFG_20260814_TEST/125770.1`) (sent_id: `deanon_BFG_20260814_TEST/125770.1_40`)

------ Gegen dieses Erkenntnis des Spruchsenates richtet sich die vorliegende frist- und formgerechte Beschwerde des Amtsbeauftragten vom 7.1.2019, in der wie folgt ausgeführt wird: "Herr **N.N.**, geb. am Datum, wohnhaft in Adresse1, hat vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und Wahrheitspflicht bewirkt, dass festzusetzende Abgaben zu niedrig festgesetzt wurden sowie vorsätzlich Lohnabgaben nicht spätestens am fünften Tag nach Fälligkeit entrichtet (abgeführt).

- missed: `N.N.` (person)
- predicted in sentence: —

**Example 38** (doc_id: `deanon_BFG_20260814_TEST/146075.1`) (sent_id: `deanon_BFG_20260814_TEST/146075.1_25`)

Im Laufe des letzten Semesters von 14.02.2022 bis 01.07.2022 habe sich **Delila Hollek**  dazu entschieden, die Ausbildung vorerst zu unterbrechen.

- missed: `Delila Hollek` (person)
- predicted in sentence: —

**Example 39** (doc_id: `deanon_BFG_20260814_TEST/147494.1`) (sent_id: `deanon_BFG_20260814_TEST/147494.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Mag. Günter Narat** in der  Beschwerdesache Lea Nelder, Am Heimweg 13, 4072 Annaberg, Österreich  Steuernummer: 43-425/9538, vertreten  durch die „Die Steuerei GmbH“, Aister Straße 2, 4332 Naarn/Machlande, über die  Beschwerden vom 24. Oktober 2023 gegen die Bescheide des Finanzamtes Österreich vom 25.  September 2023 betreffend Einkommensteuer 2018 – 2020 zu Recht:  I)  Die Beschwerden werden gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Günter Narat` (person)
- predicted in sentence: `Lea Nelder`

**Example 40** (doc_id: `deanon_BFG_20260814_TEST/131939.1`) (sent_id: `deanon_BFG_20260814_TEST/131939.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Mag. Andrea Müller-Dobler MBA MSc** über die  Beschwerde des Shoshana Döllmann, U-Bahn Station Hardeggasse 15, 3383 Maxenbach, Österreich, vom 20. Oktober 2020 gegen die  Vollstreckungsverfügung des Magistrates der Stadt Wien vom 15. Oktober 2020, Zahl  MA67/Zahl/2020, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde  stattgegeben und die angefochtene Vollstreckungsverfügung aufgehoben.

- missed: `Mag. Andrea Müller-Dobler MBA MSc` (person)
- predicted in sentence: —

**Example 41** (doc_id: `deanon_BFG_20260814_TEST/144198.1`) (sent_id: `deanon_BFG_20260814_TEST/144198.1_5`)

X1-10) über die "Verkürzung von Stempel- oder Rechtsgebühren" hinsichtlich der "Meldung  des Ausflugsverkehrs" gemäß Tiroler Schischulgesetz 1995 für zehn namentlich genannte Schi-  und Snowboardlehrer (AA u.a.) durch die **Prof.in Esra Konwischer** (= Beschwerdeführerin, Bf), eine deutsche  Schneesportschule, erstellt und an das Finanzamt für Gebühren, Verkehrsteuern und  Glücksspiel, nunmehr Finanzamt Österreich, übermittelt.   Gegenstand der Gebühr waren den Befunden zufolge jeweils die Meldung des  Ausflugsverkehrs gemäß Tiroler Schischulgesetz durch die Bf aus Jänner 2016 samt Beilagen  (Prüfungszertifikat des Dten.

- missed: `Prof.in Esra Konwischer` (person)
- predicted in sentence: —

**Example 42** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_129`)

Der älteste vorgelegte Befund von **Nicola Peterhansel** datiert aber mit  7. Jänner 2019.

- missed: `Nicola Peterhansel` (person)
- predicted in sentence: —

**Example 43** (doc_id: `deanon_BFG_20260814_TEST/131808.1`) (sent_id: `deanon_BFG_20260814_TEST/131808.1_37`)

Nachdem die Rechtsvorgängerin & CoKG infolge Anwachsung der Gesellschaftsanteile nach §  142 UGB an die **PhD Mag. Heinrich Hambücher**  mit Wirksamkeit zum xx.xx.xxxx im Firmenbuch gelöscht worden  war, teilte die steuerliche Vertretung am 11.02.2020 mit, dass zur Rechtsnachfolgerin ein  aufrechtes Bevollmächtigungsverhältnis bestehe.

- missed: `PhD Mag. Heinrich Hambücher` (person)
- predicted in sentence: —

**Example 44** (doc_id: `deanon_BFG_20260814_TEST/133515.1`) (sent_id: `deanon_BFG_20260814_TEST/133515.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin **Dr. Gabriele Grossgut-Palotás** in der  Beschwerdesache Ing. OSR Julia Strutwolf, Emmat 72, 9063 Wrießnitz, Österreich, vertreten durch Böhm & Partner  Wirtschaftsprüfung- Steuerberatung-Unternehmensberatung GmbH, Hopfengasse 23, 4020  Linz, über die Beschwerde vom 20. September 2016 gegen den Bescheid des Finanzamtes  Braunau Ried Schärding vom 5. September 2016 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2014 zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

- missed: `Dr. Gabriele Grossgut-Palotás` (person)
- predicted in sentence: `Dr. Gabriele Grossgut`

**Example 45** (doc_id: `deanon_BFG_20260814_TEST/146102.1`) (sent_id: `deanon_BFG_20260814_TEST/146102.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch den Richter **Mag. Dieter Fröhlich** über die Beschwerde  des Felizitas Kobl, Zornberg 27, 4681 Watzing, Österreich, vom 10. August 2024 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 26. Juli 2024, GZ. MA67/GZ/2024, betreffend  Verwaltungsübertretung nach § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt  Wien Nr. 51/2005, idF. ABl. der Stadt Wien Nr. 20/2020 in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006, LGBI. für Wien Nr. 9/2006, in der Fassung LGBl. für Wien Nr. 71/2018,  nach Durchführung einer mündlichen Verhandlung am 24. Oktober 2024 im Beisein des  Schriftführers SF, zu Recht:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) wird der Beschwerde insoweit  Folge gegeben, als gemäß § 45 Abs. 1 Z 4 VStG von der Verhängung einer Strafe abgesehen und  dem Beschwerdeführer unter Hinweis auf die Rechtswidrigkeit seines Verhaltens eine  Ermahnung erteilt wird.

- missed: `Mag. Dieter Fröhlich` (person)
- predicted in sentence: —

**Example 46** (doc_id: `deanon_BFG_20260814_TEST/137608.1`) (sent_id: `deanon_BFG_20260814_TEST/137608.1_10`)

Der Bf. wurde am 14. April 2021 ein weiteres Mal untersucht und von **Dr. Dok2**, Fachärztin für  Allgemeinmedizin, folgendes Gutachten erstellt:  2 von 13 Seite 3 von 13

- missed: `Dr. Dok2` (person)
- predicted in sentence: `Dr. Dok`

**Example 47** (doc_id: `deanon_BFG_20260814_TEST/130371.1`) (sent_id: `deanon_BFG_20260814_TEST/130371.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin **Mag. Andrea Ebner** in der  Beschwerdesache Dominika Oehlerich, BEd, Zamberg 9, 3843 Hohenau, Österreich, über die Beschwerde vom 5. Oktober 2012  gegen den Bescheid des Finanzamtes Baden Mödling vom 21. September 2012 betreffend  Einkommensteuer für das Jahr 2011 Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

- missed: `Mag. Andrea Ebner` (person)
- predicted in sentence: `Dominika Oehlerich`

**Example 48** (doc_id: `deanon_BFG_20260814_TEST/138372.1`) (sent_id: `deanon_BFG_20260814_TEST/138372.1_1`)

IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Christian Doktor über die Beschwerde der  **Zlatan Wetterling**, Am Kochfeld 129, 4770 Oberndorf, Österreich, vom 21. November 2019, gegen den Bescheid des Finanzamtes  Gänserndorf Mistelbach vom 8. November 2019 betreffend gemäß § 8a FLAG gekürzte  Familienbeihilfe und Kinderabsetzbetrag zu Recht erkannt:   Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

- missed: `Zlatan Wetterling` (person)
- predicted in sentence: —

**Example 49** (doc_id: `deanon_BFG_20260814_TEST/130395.1`) (sent_id: `deanon_BFG_20260814_TEST/130395.1_17`)

Seit 2006 bei  **Prof. Maida** wegen MS in Behandlung.

- missed: `Prof. Maida` (person)
- predicted in sentence: —

</details>

---

