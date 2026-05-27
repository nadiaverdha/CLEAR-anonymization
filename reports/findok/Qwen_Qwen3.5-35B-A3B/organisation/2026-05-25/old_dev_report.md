# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-05-26T07:35:52.872490

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-25/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 678 |
| Validation documents | 171 |
| Test documents | 477 |
| Train sentences | 2189 |
| Validation sentences | 563 |
| Test sentences | 20774 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 200 |
| Refinement iterations | 6 |
| Seed | 42 |
| Agentic | False |
| Enable Critic | False |
| Enable Prune | False |
| Critic Interval | 0 |
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

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 96.3% |
| True Positives | 20 |
| False Positives | 628 |
| False Negatives | 379 |
| Total Gold Entities | 399 |
| Micro Precision | 3.1% |
| Micro Recall | 5.0% |
| Micro F1 | 3.8% |
| Macro F1 | 3.8% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Hyphenated Company Names` | 1.0% | 40.0% | 0.5% | 5 | 2 | 3 |
| `Gesellschaft mbH Pattern` | 1.0% | 25.0% | 0.5% | 8 | 2 | 6 |
| `Generic GmbH Entity` | 6.7% | 11.4% | 4.8% | 167 | 19 | 148 |
| `Company Name Without Suffix` | 5.6% | 6.7% | 4.8% | 284 | 19 | 265 |
| `Federal Tax Court` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Administrative Court` | 0.0% | 0.0% | 0.0% | 7 | 0 | 7 |
| `Tax Authority Austria` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ministry of Finance` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Administrative Court Acronym` | 0.0% | 0.0% | 0.0% | 19 | 0 | 19 |
| `Federal Tax Court Acronym BFG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UFS Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `University Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Social Ministry` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS Acronym` | 0.0% | 0.0% | 0.0% | 3 | 0 | 3 |
| `Local Tax Office` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bank and Other Org` | 0.0% | 0.0% | 0.0% | 41 | 0 | 41 |
| `Specific Retailer Billa` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Amazon Transport GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Post and Telekom Austria` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Police Directorate` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finance Court Senate` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Roelfsen Versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Houdek Maschinenbau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schmeltz Luftfahrt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dorfcon-Verlag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lexdon IT` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SeneCura Full Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Lubomir Merschmeyer` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Vienna Magistrate` | 0.0% | 0.0% | 0.0% | 9 | 0 | 9 |
| `Tax Office Acronym FAÖ` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Constitutional Court` | 0.0% | 0.0% | 0.0% | 29 | 0 | 29 |
| `Constitutional Court Acronym` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `Gözcü Getränke` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Labor Court Vienna` | 0.0% | 0.0% | 0.0% | 28 | 0 | 28 |
| `Bank Full Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Court with Location` | 0.0% | 0.0% | 0.0% | 48 | 0 | 48 |
| `FAÖ Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tax Office Full Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bankhaus Denzel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Cervenka&Neunübel Telekom AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PSD Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SVS/SVB` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Pensionsversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `Psychiatrie Otto Wagner Spital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schweizerischen Unfallversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ÖGK` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesamtes für Soziales und Behindertenwesen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PSD Wien Full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SUVA` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Städtische` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Allianz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verwaltungsgerichtshof Genitive` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
| `Bundesfinanzgericht Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verwaltungsgericht Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FH Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Karl-Franzens-Universität Graz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BMI` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ernst & Young` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sozialversicherungsanstalt der Bauern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `University St Gallen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `University Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `University Vienna` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fachhochschule Wiener Neustadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzpolizei` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM für Inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `OECD` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `EASO` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kriminalpolizei` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Airport Munich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Law Firm GmbH` | 0.0% | 0.0% | 0.0% | 4 | 0 | 4 |
| `Tax Office Acronym FA` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KQPC Versand GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Event Sudkraftlex GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sudver Handel Services GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Glanznorost Institut GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Städtischen Versicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Federal Administrative Court Acronym FAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `COFAG Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BHAG Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `District Court Pattern` | 0.0% | 0.0% | 0.0% | 133 | 0 | 133 |
| `Regional Court Pattern` | 0.0% | 0.0% | 0.0% | 90 | 0 | 90 |
| `Magistrate City Pattern` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |
| `Law Firm GmbH/OG` | 0.0% | 0.0% | 0.0% | 13 | 0 | 13 |
| `Frontex Full Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Swiss Invalid Insurance` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Swiss Accident Insurance Full` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kantonsspitals St. Gallen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steueramt Kanton` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Higher Technical School` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Real Estate Office` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Federal Ministry of Justice` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Austrian Society for European Politics` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Retailers List` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Tax Office Acronym FAÖ (Full)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tax Office Acronym FAÖ (Genitive)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tax Office Acronym FAG (Full)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tax Office Acronym FAG (Genitive)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Erste Bank` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `German Federal Tax Court Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Merkur Treuhand Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tax Authority Austria with Code` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WKO Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UFS with Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tax Office Full Name with Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Amtes für Betrugsbekämpfung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific GmbH Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrate Genitive` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Limited Suffix` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Law Firm KG` | 0.0% | 0.0% | 0.0% | 10 | 0 | 10 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Generic GmbH Entity`

**F1:** 0.067 | **Precision:** 0.114 | **Recall:** 0.048  

**Format:** `regex`  
**Rule ID:** `0d4e88c9`  
**Description:**
Matches company names ending in GmbH, AG, KG, etc., with strict word boundaries and context to prevent capturing partial names or legal context.

**Content:**
```
(?i)(?<![a-zäöüß\s])(?<!\w)([A-Z][a-zäöüß0-9]+(?:\s+[A-Z][a-zäöüß0-9]+)*(?:\s+&\s+[A-Z][a-zäöüß0-9]+)*(?:\s+\-[A-Z][a-zäöüß0-9]+)*\s+(?:GmbH|AG|KG|OG|GesmbH|Aktiengesellschaft|m\.b\.H\.?|GmbH\s*&\s*Co\s*KG|Limited))(?=\s|,|\.|\(|\)|;|:|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.114 | 0.048 | 0.067 | 167 | 19 | 148 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 148 | 380 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_4`)


BergCloud GmbH, Polterauergasse 24, 5204 Neuhofen, Österreich, vertreten durch Singer Fössl, Rechtsanwälte OG in Wien, 2.

| Predicted | Gold |
|---|---|
| `BergCloud GmbH` | `BergCloud GmbH` |

**Missed by this rule (FN):**

- `Polterauergasse 24, 5204 Neuhofen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_5`)


West Berfenval GmbH, Hinterhagweg 6, 8591 Niedergößnitz, Österreich, vertreten durch Dr. Peter Mair, Rechtsanwalt in Bad Ischl, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `West Berfenval GmbH` | `West Berfenval GmbH` |

**Missed by this rule (FN):**

- `Hinterhagweg 6, 8591 Niedergößnitz, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_6`)


Waldzor Luftfahrt GmbH, Sonnenberger Straße 6, 9220 Velden am Wörther See, Österreich, vertreten durch Dr. Peter Lindinger und Dr. Andreas Pramer, Rechtsanwälte in Linz, 2.

| Predicted | Gold |
|---|---|
| `Waldzor Luftfahrt GmbH` | `Waldzor Luftfahrt GmbH` |

**Missed by this rule (FN):**

- `Sonnenberger Straße 6, 9220 Velden am Wörther See, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/1Ob213_15b`) (sent_id: `deanon_TRAIN/1Ob213_15b_4`)


MittelMedien Institut GmbH, Andreas Hofer-Zeile 1052, 3595 Brunn an der Wild, Österreich, vertreten durch Mag. Wolfgang Vinatzer, Rechtsanwalt in Wien, und 2. Kretzmar Pharma AG, St.-Elisabeth-Platz 6, 4775 Brunedt, Österreich, vertreten durch die Widter Mayrhauser Wolf Rechtsanwälte OG, Wien, wegen Gerichtserlags nach § 1425 ABGB, über den außerordentlichen Revisionsrekurs der Erstantragsgegnerin gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 29. September 2015, GZ 12 R 91/15p-14, mit dem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 27. Juli 2015, GZ 61 Nc 3/15y-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `MittelMedien Institut GmbH` | `MittelMedien Institut GmbH` |

**Missed by this rule (FN):**

- `Andreas Hofer-Zeile 1052, 3595 Brunn an der Wild, Österreich` (address)
- `Kretzmar Pharma AG` (organisation)
- `St.-Elisabeth-Platz 6, 4775 Brunedt, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/8Ob4_18y`) (sent_id: `deanon_TRAIN/8Ob4_18y_4`)


Vossbrinck Wind AG, Flurnsbach 9, 4722 Untwüsten, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte GmbH in Wien, und 2. Steinheim-Cloud Limited, Anlauftalstraße 23, 4623 Kalchau, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.141,02 EUR, über die Revision der erstbeklagten Partei gegen das Teilurteil des Handelsgerichts Wien als Berufungsgericht vom 18. September 2017, GZ 60 R 20/17x-29, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 3. Jänner 2017, GZ 20 C 529/15p-24, in der Hauptsache hinsichtlich der erstbeklagten Partei bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vossbrinck Wind AG` | `Vossbrinck Wind AG` |

**Missed by this rule (FN):**

- `Flurnsbach 9, 4722 Untwüsten, Österreich` (address)
- `Steinheim-Cloud Limited` (organisation)
- `Anlauftalstraße 23, 4623 Kalchau, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/7Ob203_24i`) (sent_id: `deanon_TRAIN/7Ob203_24i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei PhD Lara Scharpwinkel, vertreten durch Mag. Martin Wabra, Rechtsanwalt in Gmünd, gegen die beklagte Partei Fenbach-IT AG, Linn Zemlik, vertreten durch die MUSEY rechtsanwalt gmbH in Salzburg, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Oktober 2024, GZ 5 R 144/24v-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `IT AG` — partial — pred is substring of gold: `Fenbach-IT AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Lara Scharpwinkel`(person)
- `Fenbach-IT AG`(organisation)
- `Linn Zemlik`(person)

**Example 1** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_6`)


Text Entscheidungsgründe: Mit Bescheid vom 26. 4. 2010 lehnte die beklagte Partei den Antrag des Klägers auf Gewährung der Kostenerstattung für die Inanspruchnahme der Alpen-KI GmbH (im Folgenden kurz: GmbH) laut Rechnungen vom 2. 10. 2009 und 6. 11. 2009 in Höhe von insgesamt 540 EUR ab.

**False Positives:**

- `KI GmbH` — partial — pred is substring of gold: `Alpen-KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alpen-KI GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_9`)


Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH in Anspruch genommen und dafür insgesamt 540 EUR bezahlt.

**False Positives:**

- `Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_13`)


Dem für die GmbH tätigen Team gehörten renommierte Fachärzte für medizinische Unfallchirurgie sowie Sportärzte an.

**False Positives:**

- `Dem für die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_30`)


Zwischen der GmbH und der beklagten Partei besteht kein Vertragsverhältnis.

**False Positives:**

- `Zwischen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Company Name Without Suffix`

**F1:** 0.056 | **Precision:** 0.067 | **Recall:** 0.048  

**Format:** `regex`  
**Rule ID:** `c8608e27`  
**Description:**
Matches company names that do not end in a standard suffix like GmbH/AG but are clearly organizations (e.g., 'Kilincarslan Metall'), ensuring the industry term is part of the match.

**Content:**
```
(?i)(?<![a-zäöüß\s])(?<!\w)([A-Z][a-zäöüß0-9]+(?:\s+[A-Z][a-zäöüß0-9]+)*(?:\s+&\s+[A-Z][a-zäöüß0-9]+)*)\s+(Metall|Maschinenbau|Luftfahrt|Forschung|Handel|Dienstleistungen|Verlag|Software|Cloud|Transport|Immobilien|Versicherung|Gastronomie|Medien|Planung|Bau|Energie|Automotive|Gesellschaft|Institut|Gruppe|Werke|Holding|Bank|Telekom|Post|Versand|Logistik|Touristik|Pharma|Sanitär|Getränke|Lebensmittel|Elekro|Elektronik|Druck|Medizin|Klinik|Spital|Krankenhaus|Schule|Universität|Hochschule|Firma|Unternehmen|Betrieb|Konzern|AG|GmbH|KG|OG|Limited|GesmbH|Aktiengesellschaft)(?=\s|,|\.|\(|\)|;|:|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.067 | 0.048 | 0.056 | 284 | 19 | 265 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 265 | 380 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_4`)


BergCloud GmbH, Polterauergasse 24, 5204 Neuhofen, Österreich, vertreten durch Singer Fössl, Rechtsanwälte OG in Wien, 2.

| Predicted | Gold |
|---|---|
| `BergCloud GmbH` | `BergCloud GmbH` |

**Missed by this rule (FN):**

- `Polterauergasse 24, 5204 Neuhofen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_5`)


West Berfenval GmbH, Hinterhagweg 6, 8591 Niedergößnitz, Österreich, vertreten durch Dr. Peter Mair, Rechtsanwalt in Bad Ischl, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `West Berfenval GmbH` | `West Berfenval GmbH` |

**Missed by this rule (FN):**

- `Hinterhagweg 6, 8591 Niedergößnitz, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_6`)


Waldzor Luftfahrt GmbH, Sonnenberger Straße 6, 9220 Velden am Wörther See, Österreich, vertreten durch Dr. Peter Lindinger und Dr. Andreas Pramer, Rechtsanwälte in Linz, 2.

| Predicted | Gold |
|---|---|
| `Waldzor Luftfahrt GmbH` | `Waldzor Luftfahrt GmbH` |

**Missed by this rule (FN):**

- `Sonnenberger Straße 6, 9220 Velden am Wörther See, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/1Ob213_15b`) (sent_id: `deanon_TRAIN/1Ob213_15b_4`)


MittelMedien Institut GmbH, Andreas Hofer-Zeile 1052, 3595 Brunn an der Wild, Österreich, vertreten durch Mag. Wolfgang Vinatzer, Rechtsanwalt in Wien, und 2. Kretzmar Pharma AG, St.-Elisabeth-Platz 6, 4775 Brunedt, Österreich, vertreten durch die Widter Mayrhauser Wolf Rechtsanwälte OG, Wien, wegen Gerichtserlags nach § 1425 ABGB, über den außerordentlichen Revisionsrekurs der Erstantragsgegnerin gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 29. September 2015, GZ 12 R 91/15p-14, mit dem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 27. Juli 2015, GZ 61 Nc 3/15y-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `MittelMedien Institut GmbH` | `MittelMedien Institut GmbH` |

**Missed by this rule (FN):**

- `Andreas Hofer-Zeile 1052, 3595 Brunn an der Wild, Österreich` (address)
- `Kretzmar Pharma AG` (organisation)
- `St.-Elisabeth-Platz 6, 4775 Brunedt, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/8Ob4_18y`) (sent_id: `deanon_TRAIN/8Ob4_18y_4`)


Vossbrinck Wind AG, Flurnsbach 9, 4722 Untwüsten, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte GmbH in Wien, und 2. Steinheim-Cloud Limited, Anlauftalstraße 23, 4623 Kalchau, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.141,02 EUR, über die Revision der erstbeklagten Partei gegen das Teilurteil des Handelsgerichts Wien als Berufungsgericht vom 18. September 2017, GZ 60 R 20/17x-29, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 3. Jänner 2017, GZ 20 C 529/15p-24, in der Hauptsache hinsichtlich der erstbeklagten Partei bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vossbrinck Wind AG` | `Vossbrinck Wind AG` |

**Missed by this rule (FN):**

- `Flurnsbach 9, 4722 Untwüsten, Österreich` (address)
- `Steinheim-Cloud Limited` (organisation)
- `Anlauftalstraße 23, 4623 Kalchau, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/7Ob203_24i`) (sent_id: `deanon_TRAIN/7Ob203_24i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei PhD Lara Scharpwinkel, vertreten durch Mag. Martin Wabra, Rechtsanwalt in Gmünd, gegen die beklagte Partei Fenbach-IT AG, Linn Zemlik, vertreten durch die MUSEY rechtsanwalt gmbH in Salzburg, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Oktober 2024, GZ 5 R 144/24v-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `IT AG` — partial — pred is substring of gold: `Fenbach-IT AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Lara Scharpwinkel`(person)
- `Fenbach-IT AG`(organisation)
- `Linn Zemlik`(person)

**Example 1** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_6`)


Text Entscheidungsgründe: Mit Bescheid vom 26. 4. 2010 lehnte die beklagte Partei den Antrag des Klägers auf Gewährung der Kostenerstattung für die Inanspruchnahme der Alpen-KI GmbH (im Folgenden kurz: GmbH) laut Rechnungen vom 2. 10. 2009 und 6. 11. 2009 in Höhe von insgesamt 540 EUR ab.

**False Positives:**

- `KI GmbH` — partial — pred is substring of gold: `Alpen-KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alpen-KI GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_9`)


Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH in Anspruch genommen und dafür insgesamt 540 EUR bezahlt.

**False Positives:**

- `Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_13`)


Dem für die GmbH tätigen Team gehörten renommierte Fachärzte für medizinische Unfallchirurgie sowie Sportärzte an.

**False Positives:**

- `Dem für die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_30`)


Zwischen der GmbH und der beklagten Partei besteht kein Vertragsverhältnis.

**False Positives:**

- `Zwischen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `District Court Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4a197a40`  
**Description:**
Matches Bezirksgericht followed by location, handling 'BG' abbreviation.

**Content:**
```
(?i)\b(?:Bezirksgericht\s+([A-Za-zäöüÄÖÜ]+|\w+)|BG\s+Bezirksgericht\s+([A-Za-zäöüÄÖÜ]+|\w+))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 133 | 0 | 133 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 133 | 396 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und den Hofräten Hon.-Prof. Dr. Höllwerth und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei VetR Nadja Kovalskiy, vertreten durch Dr. Günther Ledolter, Rechtsanwalt in Graz, gegen die beklagte Partei Kraftfenheim AG, Kordelia Weinmeister, LLB, vertreten durch Dr. Matthias Bacher, Rechtsanwalt in Wien, wegen 3.849,91 EUR sA und Feststellung, AZ 11 C 688/19b des Bezirksgerichts Leopoldstadt, infolge Delegierungsantrags der klagenden Partei den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Leopoldstadt zurückgestellt.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Nadja Kovalskiy`(person)
- `Kraftfenheim AG`(organisation)
- `Kordelia Weinmeister, LLB`(person)

**Example 1** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_5`)


Er brachte die Klage zunächst beim Bezirksgericht Graz-Ost ein, welches die Klage wegen örtlicher Unzuständigkeit zurück- und infolge Überweisungsantrags des Klägers an das Bezirksgericht Leopoldstadt überwies.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation
- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 2** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_7`)


Der Kläger stellte den Antrag auf Delegierung der Rechtssache an das Bezirksgericht Graz-Ost.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_8`)


Das Bezirksgericht Leopoldstadt legte den Akt – entgegen § 31 Abs 3 JN – ohne Äußerung und vor Erledigung der von der Beklagten erhobenen Unzuständigkeitseinrede vor.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_9`)


Der erkennende Senat stellte die Akten dem Bezirksgericht Leopoldstadt ohne Entscheidung über den Delegierungsantrag zurück und führte aus, dass eine Entscheidung über diesen Antrag erst nach rechtskräftiger Entscheidung über die Stattgebung oder Ablehnung der Unzuständigkeitseinrede erfolgen könne (RS0046338; RS0109369).

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Regional Court Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8426a1d3`  
**Description:**
Matches Landesgericht (LG) followed by location.

**Content:**
```
(?i)\b(Landesgericht\s+([A-Za-zäöüÄÖÜ]+|\w+)|LG\s+([A-Za-zäöüÄÖÜ]+|\w+))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 90 | 0 | 90 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 90 | 391 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob167_22y`) (sent_id: `deanon_TRAIN/1Ob167_22y_7`)


[2] Das Landesgericht Leoben als Berufungsgericht hob das erstinstanzliche Urteil zur neuerlichen Entscheidung nach allfälliger Verfahrensergänzung auf.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/1Ob167_22y`) (sent_id: `deanon_TRAIN/1Ob167_22y_15`)


Mit dem angefochtenen Beschluss hat das Landesgericht Leoben nicht im Berufungsverfahren, sondern im Rekursverfahren den Rekurs sowie weitere Anträge der Klägerin gegen seinen Aufhebungsbeschluss zurückgewiesen (vgl 3 Ob 156/83 = SZ 57/5 = JBl 1984, 617).

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/1Ob167_22y`) (sent_id: `deanon_TRAIN/1Ob167_22y_26`)


Da somit gegen einen – hier vorliegenden – aufhebenden Beschluss des Berufungsgerichts gemäß § 519 Abs 1 Z 2 ZPO nur dann ein Rekurs an den Obersten Gerichtshof erhoben werden könnte, wenn das Berufungsgericht ausgesprochen hätte, dass (der Wert des Entscheidungsgegenstands 5.000 EUR übersteigt [vgl 4 Ob 206/08k mwN] und) der Rekurs wegen Vorliegens einer erheblichen Rechtsfrage zulässig wäre, hier aber ein solcher Ausspruch nicht vorliegt, hat das Landesgericht Leoben zutreffend in sinngemäßer Anwendung des § 523 ZPO das unzulässige Rechtsmittel und (mangels Rechtsgrundlage) die Anträge auf „Ausspruch der Zulässigkeit des (Revisions-)Rekurses“ und „Abänderung des Ausspruchs über die Zulässigkeit“ zurückgewiesen.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Nc12_11p`) (sent_id: `deanon_TRAIN/10Nc12_11p_6`)


Text Begründung: Die Klägerin brachte beim Landesgericht Innsbruck eine Klage ein, mit der sie die Bezahlung von (ausgedehnt) 52.827,98 EUR sA an Schadenersatz wegen eines beim Reitunterricht in der vom Beklagten betriebenen Reitschule erlittenen Reitunfalls verlangt;

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/9Nc16_11v`) (sent_id: `deanon_TRAIN/9Nc16_11v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Dr. Hopf und Mag. Ziegelbauer als weitere Richter in der Arbeitsrechtssache der klagenden Partei Senta Moshack, vertreten durch Berchtold & Kollerics, Rechtsanwälte in Graz, gegen die beklagte Partei Anton Reinerth, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17-19, wegen Feststellung (Streitwert: 69.000 EUR), über den Delegierungsantrag beider Parteien den Beschluss gefasst:  Spruch Der Akt wird dem Landesgericht für Zivilrechtssachen Graz als Arbeits- und Sozialgericht zur Entscheidung nach § 31a JN zurückgestellt.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Senta Moshack`(person)
- `Anton Reinerth`(person)

</details>

---

## `Court with Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `971aef3b`  
**Description:**
Matches court names followed by location suffixes like 'Außenstelle Linz'.

**Content:**
```
(?i)\b((?:Bundesfinanzgericht|Verwaltungsgerichtshof|Verfassungsgerichtshof)(?:s?)(?:,\s+Außenstelle\s+[A-Za-z]+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 48 | 0 | 48 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 48 | 396 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_93`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_151`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_162`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 3** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_163`)


Nach einhelliger Rechtsprechung steht den Parteien eines Gerichtsverfahrens kein Recht auf Antragstellung hinsichtlich einer Befassung des Verfassungsgerichtshofs zu.

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_167`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bank and Other Org`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `53220dfe`  
**Description:**
Matches specific bank names and other organizations like 'Reinemut + Smoch Handel' that don't fit GmbH/AG patterns.

**Content:**
```
(?i)\b((?:Raiffeisenbank\s+[A-Za-z]+|Reinemut\s+\+\s+Smoch\s+Handel|SENECURA|SeneCura|ÖBB|PVA|Bezirkshauptmannschaft\s+[A-Za-z]+|Versorgungskasse\s+Deutscher\s+Unternehmen\s+VVaG|Deutschen\s+Rentenversicherung\s+Bund|Pensionsversicherungsanstalt\s+Wien|Krankenpflegevereins\s+Bludenz|Imre\s+\&\s+Schaffer\s+Rechtsanwälte\s+OG|TAXCOACH\s+Wirtschaftsprüfung\s+und\s+Steuerberatung\s+GmbH\s*&\s*Co\s*KG|BKS\s+Steuerberatung\s+GmbH\s*&\s*Co\s*KG|Dr\.\s+Roland\s+Gabl\s+Rechtsanwalts-\s+Kommandit-Partnerschaft|\u201e\u00d6BUG\u201c\s+DR\.\s+Nikolaus\s+Wirtschaftstreuhand\s+GmbH\s*-\s+Wirtschaftsprüfungs-\s+und\s+Steuerberatungsgesellschaft|How\s+to\s+spend\s+it\s+Verlag\s+GmbH|INET\s+Internet\s+Service\s+GmbH|INET\s+System\s+Informations\s+GmbH|Talwerk\s+Logistik\s+Holding\s+GMBH|InnMarine\s+GMBH|Mittel\s+Unisyn\s+GMBH|Bärs\s+\&\s+Walterscheidt\s+Handel\s+GMBH|Ober\s+Lemostnor\s+AG|Vennes\s+Recycling\s+AG|HPS\s+Hergovits,\s+Pinkel\s+\&\s+Schnabl\s+Steuerberatungs\s+GmbH|Reinemut\s+\+\s+Smoch\s+Handel|Zollamt\s+Österreich|Amt\s+für\s+Betrugsbekämpfung\s+als\s+Finanzstrafbehörde|Verfassungsgerichtshof))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 41 | 0 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 41 | 396 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_93`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_151`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_162`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 3** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_167`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob62_17s`) (sent_id: `deanon_TRAIN/10Ob62_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache der mj Traude Coelsch, geboren am 8. Februar 1982, vertreten durch das Land Salzburg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft St. Johann im Pongau, 5600 St. Johann im Pongau, Hauptstraße 1), wegen Herabsetzung von Unterhaltsvorschüssen, infolge des Revisionsrekurses des Kindes gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 9. Februar 2017, GZ 21 R 457/16a-31, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 13. Oktober 2016, GZ 38 PU 154/15a-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Rekursgericht mit dem Auftrag zurückgestellt, eine Gleichschrift des Revisionsrekurses des Kindes dem Bund zur allfälligen Erstattung einer Revisionsrekursbeantwortung binnen 14 Tagen zuzustellen.

**False Positives:**

- `Bezirkshauptmannschaft St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Traude Coelsch`(person)
- `8. Februar 1982`(date)

</details>

---

## `Constitutional Court`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0bbc25f5`  
**Description:**
Matches Verfassungsgerichtshof and its genitive form.

**Content:**
```
(?i)\b(Verfassungsgerichtshof(?:es)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 29 | 0 | 29 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 29 | 396 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_93`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_151`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_162`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 3** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_167`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_32`)


Mit Beschluss vom 30. März 2016 hat der Oberste Gerichtshof zu 4 Ob 31/16m ua in sechs verbundenen Verfahren, denen Sachverhalte zugrundelagen, die mit jenem dieses Verfahrens vergleichbar sind, die dort näher bezeichneten Bestimmungen des Glücksspielgesetzes und des NÖ Spielautomatengesetzes 2011 (hilfsweise die genannten Gesetze zur Gänze) beim Verfassungsgerichtshof als verfassungswidrig angefochten.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Labor Court Vienna`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dee27985`  
**Description:**
Matches Arbeits- und Sozialgericht Wien and variations.

**Content:**
```
(?i)\b(Arbeits-\s+und\s+Sozialgericht(?:\s+Wien)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 28 | 0 | 28 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 28 | 376 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9Nc16_11v`) (sent_id: `deanon_TRAIN/9Nc16_11v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Dr. Hopf und Mag. Ziegelbauer als weitere Richter in der Arbeitsrechtssache der klagenden Partei Senta Moshack, vertreten durch Berchtold & Kollerics, Rechtsanwälte in Graz, gegen die beklagte Partei Anton Reinerth, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17-19, wegen Feststellung (Streitwert: 69.000 EUR), über den Delegierungsantrag beider Parteien den Beschluss gefasst:  Spruch Der Akt wird dem Landesgericht für Zivilrechtssachen Graz als Arbeits- und Sozialgericht zur Entscheidung nach § 31a JN zurückgestellt.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Senta Moshack`(person)
- `Anton Reinerth`(person)

**Example 1** (doc_id: `deanon_TRAIN/9Nc16_11v`) (sent_id: `deanon_TRAIN/9Nc16_11v_5`)


Nach Einbringung der Klage, jedoch noch vor Anberaumung einer mündlichen Streitverhandlung in erster Instanz, beantragten die Parteien einvernehmlich die Delegierung der Arbeitsrechtssache an das Landesgericht Linz als Arbeits- und Sozialgericht.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/8ObS6_23z`) (sent_id: `deanon_TRAIN/8ObS6_23z_4`)


Gabriele Svirak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei RgR Maurice Fredekind, Bakk. phil., vertreten durch Burkowski Rechtsanwälte in Linz, gegen die beklagte Partei IEF Service GmbH, 1150 Wien, Linke Wienzeile 246, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, wegen 166 EUR, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 23. Oktober 2023, GZ 11 Rs 65/23t-11.3, mit welchem das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 24. Mai 2023, GZ 11 Cgs 24/23v-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `RgR Maurice Fredekind, Bakk. phil.`(person)

**Example 3** (doc_id: `deanon_TRAIN/8ObA10_12x`) (sent_id: `deanon_TRAIN/8ObA10_12x_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Kuras und Mag. Ziegelbauer sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Manuela Majeranowski als weitere Richter in der Arbeitsrechtssache der klagenden Partei Priv.-Doz.in HR OSR Larissa Abbate, vertreten durch Hasch & Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Bachbach-Marine Gesellschaft mbH, Floreweg 8, 9103 Bösenort, Österreich, vertreten durch Mag. Klaus F. Lughofer LLM, Rechtsanwalt in Linz, wegen Feststellung (Streitwert: 30.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. November 2011, GZ 11 Ra 92/11w-10, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 31. August 2011, GZ 11 Cga 101/11d-5, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in HR OSR Larissa Abbate`(person)
- `Bachbach-Marine Gesellschaft mbH`(organisation)
- `Floreweg 8, 9103 Bösenort, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ostrovska`(person)

</details>

---

## `Administrative Court Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3edf6158`  
**Description:**
Matches VwGH acronym, but only when it appears as a standalone entity reference, not as part of a date citation if the full name is present, and avoids false positives in generic contexts.

**Content:**
```
(?i)\b(VwGH)\b(?![\s]*[0-9]{2}\.?[0-9]{2}\.?[0-9]{2,4})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 19 | 0 | 19 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 19 | 369 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob161_10k`) (sent_id: `deanon_TRAIN/6Ob161_10k_36`)


Die dem Enteigneten gebührende Entschädigung muss alle durch die Enteignung verursachten vermögensrechtlichen Nachteile erfassen, wobei bei ihrer Bemessung auch auf sämtliche bestehende wirtschaftliche Möglichkeiten bedacht zu nehmen ist (VwGH 28.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/1Ob4_20z`) (sent_id: `deanon_TRAIN/1Ob4_20z_41`)


Mit der Bestellung zum Organ der Straßenaufsicht gemäß § 97 StVO werden dem Betroffenen hoheitliche Befugnisse übertragen, weil er unter den Voraussetzungen der Abs 4 und 5a leg cit Anordnungen und Aufforderungen betreffend die Benützung der Straße erteilen kann (VwGH Ra 2016/11/0177;Pürstl, StVO15.00§ 97 E 6/1).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/9Ob31_22g`) (sent_id: `deanon_TRAIN/9Ob31_22g_52`)


2.3… Unter die Gewerbeberechtigung für das Gastgewerbe fällt auch die Lieferung und damit der Verkauf von angerichteten kalten Platten, kalten oder warmen Buffets sowie sonstigen warmen Speisen und Menüs ohne Nebenleistungen (vgl VwGH 10.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/2Ob47_25p`) (sent_id: `deanon_TRAIN/2Ob47_25p_58`)


Die Kundmachung der – im Übrigen entgegen § 48 Abs 2 StVO nur am linken Straßenrand aufgestellten (vgl VwGH 85/02/0240 und 88/17/0139) – Verbotszeichen nach § 52 lit a Z 1 StVO war nicht durch die Verordnung der Bezirkshauptmannschaft gedeckt, die nur einbeschränktesFahrverbot mit entsprechender Zusatztafel („Zufahrt bis zur Baustelle gestattet“) verfügt hatte.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/1Ob79_17z`) (sent_id: `deanon_TRAIN/1Ob79_17z_64`)


Lfg 2014], Rz 7 f zu § 19 Abs 1a UStG), den Begriff des Bauwerks – und damit den der Bauleistung – weit auszulegen (VwGH 2011/15/0049).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Law Firm GmbH/OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ce418579`  
**Description:**
Matches law firms ending in Rechtsanwälte GmbH/OG with names, ensuring no preceding context is included.

**Content:**
```
(?i)(?<![a-zäöüß\s])(?<!\w)([A-Z][a-zäöüÄÖÜ]+(?:\s+[A-Z][a-zäöüÄÖÜ]+)*(?:\s+&\s+[A-Z][a-zäöüÄÖÜ]+)*\s+Rechtsanwälte\s+(?:GmbH|OG))(?=\s|,|\.|\(|\)|;|:|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 13 | 0 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 13 | 351 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9ObA141_19d`) (sent_id: `deanon_TRAIN/9ObA141_19d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshof Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Peter Zeitler (aus dem Kreis der Arbeitnehmer) und Angela Taschek (aus dem Kreis der Arbeitgeber) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Adelheid Haaf, LLB, vertreten durch Dr. Thomas Krankl, Rechtsanwalt in Wien, gegen die beklagte Partei Nossack Analyse AG, Sascha Steinke, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 1.397.481,32 EUR netto sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. Oktober 2019, GZ 9 Ra 14/19y-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Adelheid Haaf, LLB`(person)
- `Nossack Analyse AG`(organisation)
- `Sascha Steinke`(person)

**Example 1** (doc_id: `deanon_TRAIN/8Ob4_18y`) (sent_id: `deanon_TRAIN/8Ob4_18y_4`)


Vossbrinck Wind AG, Flurnsbach 9, 4722 Untwüsten, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte GmbH in Wien, und 2. Steinheim-Cloud Limited, Anlauftalstraße 23, 4623 Kalchau, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.141,02 EUR, über die Revision der erstbeklagten Partei gegen das Teilurteil des Handelsgerichts Wien als Berufungsgericht vom 18. September 2017, GZ 60 R 20/17x-29, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 3. Jänner 2017, GZ 20 C 529/15p-24, in der Hauptsache hinsichtlich der erstbeklagten Partei bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vossbrinck Wind AG`(organisation)
- `Flurnsbach 9, 4722 Untwüsten, Österreich`(address)
- `Steinheim-Cloud Limited`(organisation)
- `Anlauftalstraße 23, 4623 Kalchau, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michael Puhm (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Hermine Thom, vertreten durch Dr. Markus Orgler, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Mur Brucktridon AG, Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat., vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 4.200,83 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 17. Oktober 2019, GZ 13 Ra 41/15z-30, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hermine Thom`(person)
- `Mur Brucktridon AG`(organisation)
- `Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat.`(person)

**Example 3** (doc_id: `deanon_TRAIN/7Ob11_22a`) (sent_id: `deanon_TRAIN/7Ob11_22a_6`)


IT Sudtraver GmbH, Wald-Marine, und 2. Tal Seewil GmbH, Grappaweg 1, 5310 Hof, Österreich, beide vertreten durch die DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Herausgabe und Feststellung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2021, GZ 4 R 149/21s-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Tessbach Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `IT Sudtraver GmbH`(organisation)
- `Wald-Marine`(organisation)
- `Tal Seewil GmbH`(organisation)
- `Grappaweg 1, 5310 Hof, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/5Ob202_09f`) (sent_id: `deanon_TRAIN/5Ob202_09f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Danzl als Vorsitzenden sowie die Hofrätinnen/Hofräte des Obersten Gerichtshofs Dr. Hurch, Dr. Lovrek, Dr. Höllwerth und Dr. Tarmann-Prentner als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Kadzimirsz Sicherheit GmbH, Rottenmannerstraße 19, 3231 Wieden, Österreich, vertreten durch Dr. Karl Grigkar, Rechtsanwalt in Wien, wider den Antragsgegner Herbert Dietmaier, vertreten durch Hule Bachmayr-Heyda Nordberg Rechtsanwälte GmbH in Wien, wegen § 12a iVm § 46 Abs 2 MRG, über den Revisionsrekurs der Antragstellerin gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. Mai 2009, GZ 39 R 2/09z-17, womit infolge Rekurses der Antragstellerin der Sachbeschluss des Bezirksgerichts Innere Stadt Wien vom 27. Oktober 2008, GZ 48 Msch 9/08v-11, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Heyda Nordberg Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kadzimirsz Sicherheit GmbH`(organisation)
- `Rottenmannerstraße 19, 3231 Wieden, Österreich`(address)
- `Herbert Dietmaier`(person)

</details>

---

## `Magistrate City Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5b8b1658`  
**Description:**
Matches Magistrat der Stadt followed by city name, including genitive forms and department codes.

**Content:**
```
(?i)\bMagistrat(?:s)?\s+der\s+Stadt\s+([A-Za-zäöüÄÖÜ]+(?:\s+MA\s+\d+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 392 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_4`)


Claire Al-Hakim, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Rechtsvertretung Bezirk 21, 1210 Wien, Franz-Jonas-Platz 12), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 22. November 2024, GZ 45 R 496/24k-26, mit dem der Beschluss des Bezirksgerichts Floridsdorf vom 2. August 2024, GZ 16 Pu 19/24a-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Claire Al-Hakim`(person)

**Example 1** (doc_id: `deanon_TRAIN/7Ob119_18b`) (sent_id: `deanon_TRAIN/7Ob119_18b_4`)


Matzka als weitere Richter in der Pflegschaftssache der Minderjährigen Silke Wieging, geboren am 20. März 2010, 12. September 1996, vertreten durch das Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 12, 13, 23, 1230 Wien, Rößlergasse 15, Mutter Fiona Wenzlick, Vater Viola Peiniger, vertreten durch Dr. Tassilo Wallentin LL.M, Rechtsanwalt in Wien, wegen Unterhalt, infolge Revisionsrekurses des Vaters gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. Mai 2018, GZ 44 R 104/18x-180, womit der Rekurs des Vaters gegen den Beschluss des Bezirksgerichts Meidling vom 25. Jänner 2018, GZ 1 Pu 73/10b-173, teilweise zurückgewiesen und ihm im Übrigen nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Silke Wieging`(person)
- `20. März`(date)
- `12. September 1996`(date)
- `Fiona Wenzlick`(person)
- `Viola Peiniger`(person)

**Example 2** (doc_id: `deanon_TRAIN/8Ob1_20k`) (sent_id: `deanon_TRAIN/8Ob1_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn, den Hofrat Dr. Stefula und die Hofrätin Mag. Wessely-Kristöfel als weitere Richter in der Pflegschaftssache der mj Niklas Chomicz, geboren am 6. Oktober 2009, 17. Mai 2000, vertreten durch den Magistrat der Stadt Wien, Wiener Kinder- und Jugendhilfe, Rechtsvertretung für den Bezirk 10, 1100 Wien, Alfred-Adler-Straße 12, wegen Unterhalt, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 15. Oktober 2019, GZ 45 R 363/19v-47, mit dem der Beschluss des Bezirksgerichts Favoriten vom 5. Juni 2019, GZ 8 Pu 52/10k-40, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Niklas Chomicz`(person)
- `6. Oktober`(date)
- `17. Mai 2000`(date)

**Example 3** (doc_id: `deanon_TRAIN/10Ob26_18y`) (sent_id: `deanon_TRAIN/10Ob26_18y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und durch die Hofrätinnen und Hofräte Dr. Fichtenau, Dr. Grohmann, Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Pflegschaftssache des minderjährigen VetR Lee Rietze, geboren am 11. November 2014, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger (Magistrat der Stadt Linz, Abteilung für Soziales, Jugend und Familie, 4040 Linz, Hauptstraße 1–5), wegen Unterhalt und Unterhaltsvorschuss, über den Revisionsrekurs des Vaters und Unterhaltsverpflichteten Dipl.-Ing. Mercedes Rheinfeldt (bei Frau Marion Pinschmidt ), Rumänien, vertreten durch Mag. Michael Schenk, Rechtsanwalt in Linz, gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 23. Jänner 2017, GZ 15 R 273/16x, 15 R 274/16v-62, womit die Beschlüsse des Bezirksgerichts Linz vom 15. Dezember 2015, GZ 24 PU 504/14a-36 und -37, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Magistrat der Stadt Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Lee Rietze`(person)
- `11. November`(date)
- `Dipl.-Ing. Mercedes Rheinfeldt`(person)
- `Marion Pinschmidt`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob82_10x`) (sent_id: `deanon_TRAIN/10Ob82_10x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des mj Dimitri Ratzenböck, geboren am 6. August 1956, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, MA 11 Amt für Jugend und Familie, Rechtsvertretung für den 3. und 11.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dimitri Ratzenböck`(person)
- `6. August 1956`(date)

</details>

---

## `Law Firm KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8e2afccb`  
**Description:**
Matches law firms ending in KG, excluding GmbH & Co KG patterns.

**Content:**
```
(?i)(?<![a-zäöüß\s])(?<!\w)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+&\s+[A-Z][a-zäöüß]+)*\s+KG)(?=\s|,|\.|\(|\)|;|:|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 377 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_7`)


TraunChemie GmbH & Co KG, Badeteich Bisamberg 16, 4625 Kronberg, Österreich, vertreten durch Siemer-Siegl-Füreder & Partner, Rechtsanwälte OG in Wien, wegen 59.104,03 EUR sA, über die außerordentlichen Revisionsrekurse der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 2. Mai 2011, GZ 2 R 182/10p-50, womit über Rekurs der klagenden Partei der Beschluss des Landesgerichts Steyr vom 23. August 2010, GZ 4 Cg 154/08t-34, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentlichen Revisionsrekurse werden gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `TraunChemie GmbH & Co KG` — partial — gold is substring of pred: `TraunChemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunChemie GmbH`(organisation)
- `Badeteich Bisamberg 16, 4625 Kronberg, Österreich`(address)

**Example 1** (doc_id: `deanon_TRAIN/7Ob65_15g`) (sent_id: `deanon_TRAIN/7Ob65_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Hofrätin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Nortri-Umwelt GmbH & Co KG, Piberberg 8, 4720 Unternfurth, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in Salzburg, gegen die beklagte Partei Anton Adil Versicherungs-Aktiengesellschaft, Am Kastanienhof 90, 6162 Mutters, Österreich, vertreten durch Dr. Johannes Kirschner, Rechtsanwalt in Wels, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 19. Jänner 2015, GZ 1 R 198/14i-14, womit das Urteil des Landesgerichts Wels vom 29. September 2014, GZ 2 Cg 65/14g-10, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Umwelt GmbH & Co KG` — positional overlap with gold: `Nortri-Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nortri-Umwelt GmbH`(organisation)
- `Piberberg 8, 4720 Unternfurth, Österreich`(address)
- `Anton Adil`(person)
- `Am Kastanienhof 90, 6162 Mutters, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_6`)


Die KG wurde aufgelöst und der Geschäftsbetrieb eingestellt.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_9`)


Die Beklagte informierte die Kunden der KG, dass sie alle Geschäfte der KG mit allen Rechten und Pflichten übernehme.

**False Positives:**

- `Die Beklagte informierte die Kunden der KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_11`)


Die KG habe nämlich dahingehend beraten, dass der Schweinestall der Klägerin aufgrund von Mängeln komplett zu sanieren sei.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Federal Tax Court`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `afa5684f`  
**Description:**
Matches Bundesfinanzgericht and all its case endings, including optional (BFG) suffix.

**Content:**
```
(?i)\b(Bundesfinanzgericht(?:es|s|en)?s?)(?:\s*\(BFG\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Tax Authority Austria`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c2a31ff0`  
**Description:**
Matches Finanzamt Österreich and variations including genitive and optional parenthetical codes.

**Content:**
```
(?i)\b(Finanzamt(?:es)?\s+Österreich(?:\s*\([^)]+\))?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ministry of Finance`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4b2c511e`  
**Description:**
Matches Bundesministerium für Finanzen and BMF.

**Content:**
```
(?i)\b(Bundesministeriums?\s+für\s+Finanzen|BMF)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Federal Tax Court Acronym BFG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7abd2887`  
**Description:**
Matches BFG acronym, ensuring it's not part of a date citation.

**Content:**
```
(?i)\b(BFG)\b(?![\s]*[0-9]{2}\.?[0-9]{2}\.?[0-9]{2,4})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `UFS Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9eb79492`  
**Description:**
Matches UFS acronym, ensuring it's not part of a date citation.

**Content:**
```
(?i)\b(UFS)\b(?![\s]*[0-9]{2}\.?[0-9]{2}\.?[0-9]{2,4})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `University Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6da0d398`  
**Description:**
Matches Universität Wien

**Content:**
```
(?i)\b(Universität\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Social Ministry`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `03b8a937`  
**Description:**
Matches Bundesamt für Soziales und Behindertenwesen

**Content:**
```
(?i)\b(Bundesamt(?:s)?\s+für\s+Soziales\s+und\s+Behindertenwesen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Local Tax Office`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ecab04b8`  
**Description:**
Matches Finanzamt followed by city names, strictly excluding Bundesfinanzgericht and stopping before dates.

**Content:**
```
(?i)\b(Finanzamt(?:s)?\s+(?:Wien\s+(?:9/18/19|1/23|\d+)?|Neunkirchen\s+(?:Wr\.\s*Neustadt|Wiener\s*Neustadt)?|Oststeiermark|Stallhofen|Landeck\s+Reutte|Klosterneuburg|Österreich))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Retailer Billa`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2e3b0511`  
**Description:**
Matches the specific retailer Billa.

**Content:**
```
(?i)\b(Billa)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Amazon Transport GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1bc983f5`  
**Description:**
Matches Amazon Transport GmbH specifically.

**Content:**
```
(?i)\b(Amazon\s+Transport\s+GmbH)\b
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

## `Generic GmbH Entity`

**F1:** 0.067 | **Precision:** 0.114 | **Recall:** 0.048  

**Format:** `regex`  
**Rule ID:** `0d4e88c9`  
**Description:**
Matches company names ending in GmbH, AG, KG, etc., with strict word boundaries and context to prevent capturing partial names or legal context.

**Content:**
```
(?i)(?<![a-zäöüß\s])(?<!\w)([A-Z][a-zäöüß0-9]+(?:\s+[A-Z][a-zäöüß0-9]+)*(?:\s+&\s+[A-Z][a-zäöüß0-9]+)*(?:\s+\-[A-Z][a-zäöüß0-9]+)*\s+(?:GmbH|AG|KG|OG|GesmbH|Aktiengesellschaft|m\.b\.H\.?|GmbH\s*&\s*Co\s*KG|Limited))(?=\s|,|\.|\(|\)|;|:|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.114 | 0.048 | 0.067 | 167 | 19 | 148 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 148 | 380 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_4`)


BergCloud GmbH, Polterauergasse 24, 5204 Neuhofen, Österreich, vertreten durch Singer Fössl, Rechtsanwälte OG in Wien, 2.

| Predicted | Gold |
|---|---|
| `BergCloud GmbH` | `BergCloud GmbH` |

**Missed by this rule (FN):**

- `Polterauergasse 24, 5204 Neuhofen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_5`)


West Berfenval GmbH, Hinterhagweg 6, 8591 Niedergößnitz, Österreich, vertreten durch Dr. Peter Mair, Rechtsanwalt in Bad Ischl, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `West Berfenval GmbH` | `West Berfenval GmbH` |

**Missed by this rule (FN):**

- `Hinterhagweg 6, 8591 Niedergößnitz, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_6`)


Waldzor Luftfahrt GmbH, Sonnenberger Straße 6, 9220 Velden am Wörther See, Österreich, vertreten durch Dr. Peter Lindinger und Dr. Andreas Pramer, Rechtsanwälte in Linz, 2.

| Predicted | Gold |
|---|---|
| `Waldzor Luftfahrt GmbH` | `Waldzor Luftfahrt GmbH` |

**Missed by this rule (FN):**

- `Sonnenberger Straße 6, 9220 Velden am Wörther See, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/1Ob213_15b`) (sent_id: `deanon_TRAIN/1Ob213_15b_4`)


MittelMedien Institut GmbH, Andreas Hofer-Zeile 1052, 3595 Brunn an der Wild, Österreich, vertreten durch Mag. Wolfgang Vinatzer, Rechtsanwalt in Wien, und 2. Kretzmar Pharma AG, St.-Elisabeth-Platz 6, 4775 Brunedt, Österreich, vertreten durch die Widter Mayrhauser Wolf Rechtsanwälte OG, Wien, wegen Gerichtserlags nach § 1425 ABGB, über den außerordentlichen Revisionsrekurs der Erstantragsgegnerin gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 29. September 2015, GZ 12 R 91/15p-14, mit dem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 27. Juli 2015, GZ 61 Nc 3/15y-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `MittelMedien Institut GmbH` | `MittelMedien Institut GmbH` |

**Missed by this rule (FN):**

- `Andreas Hofer-Zeile 1052, 3595 Brunn an der Wild, Österreich` (address)
- `Kretzmar Pharma AG` (organisation)
- `St.-Elisabeth-Platz 6, 4775 Brunedt, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/8Ob4_18y`) (sent_id: `deanon_TRAIN/8Ob4_18y_4`)


Vossbrinck Wind AG, Flurnsbach 9, 4722 Untwüsten, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte GmbH in Wien, und 2. Steinheim-Cloud Limited, Anlauftalstraße 23, 4623 Kalchau, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.141,02 EUR, über die Revision der erstbeklagten Partei gegen das Teilurteil des Handelsgerichts Wien als Berufungsgericht vom 18. September 2017, GZ 60 R 20/17x-29, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 3. Jänner 2017, GZ 20 C 529/15p-24, in der Hauptsache hinsichtlich der erstbeklagten Partei bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vossbrinck Wind AG` | `Vossbrinck Wind AG` |

**Missed by this rule (FN):**

- `Flurnsbach 9, 4722 Untwüsten, Österreich` (address)
- `Steinheim-Cloud Limited` (organisation)
- `Anlauftalstraße 23, 4623 Kalchau, Österreich` (address)

**Example 5** (doc_id: `deanon_TRAIN/7Ob11_22a`) (sent_id: `deanon_TRAIN/7Ob11_22a_6`)


IT Sudtraver GmbH, Wald-Marine, und 2. Tal Seewil GmbH, Grappaweg 1, 5310 Hof, Österreich, beide vertreten durch die DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Herausgabe und Feststellung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2021, GZ 4 R 149/21s-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `IT Sudtraver GmbH` | `IT Sudtraver GmbH` |

**Missed by this rule (FN):**

- `Wald-Marine` (organisation)
- `Tal Seewil GmbH` (organisation)
- `Grappaweg 1, 5310 Hof, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `RheinPharma Services AG` | `RheinPharma Services AG` |

**Missed by this rule (FN):**

- `Unterhillinglah 5, 9853 Dornbach, Österreich` (address)

**Example 7** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_6`)


Glöckler Daten AG, Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Glöckler Daten AG` | `Glöckler Daten AG` |

**Missed by this rule (FN):**

- `Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich` (address)

**Example 8** (doc_id: `deanon_TRAIN/6Ob86_20w`) (sent_id: `deanon_TRAIN/6Ob86_20w_6`)


Solar Bruckstein GmbH, Scherrers Getränke, 2. SüdDerveruniMaschinenbau AG, Untere Hofäcker 14, 5771 Sinning, Österreich, beide vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 27.758,24 EUR sA, über die Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 5. März 2020, GZ 1 R 4/20w-44, mit dem das Urteil des Landesgerichts St. Pölten vom 28. Oktober 2019, GZ 3 Cg 62/17m-40, bestätigt wurde, den Beschluss gefasst:  Spruch Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `Solar Bruckstein GmbH` | `Solar Bruckstein GmbH` |

**Missed by this rule (FN):**

- `Scherrers Getränke` (organisation)
- `SüdDerveruniMaschinenbau AG` (organisation)
- `Untere Hofäcker 14, 5771 Sinning, Österreich` (address)

**Example 9** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_5`)


Maschinenbau Heimfurtcon GmbH, Fretzschner Medien, 2.

| Predicted | Gold |
|---|---|
| `Maschinenbau Heimfurtcon GmbH` | `Maschinenbau Heimfurtcon GmbH` |

**Missed by this rule (FN):**

- `Fretzschner Medien` (organisation)

**Example 10** (doc_id: `deanon_TRAIN/10Ob85_19a`) (sent_id: `deanon_TRAIN/10Ob85_19a_6`)


OberTratraSoftware Dienstleistungen AG, Prägrader Weg 43, 8616 Gasen, Österreich, Deutschland, vertreten durch Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen Vertragsaufhebung (5.000 EUR) und 11.561,86 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 2. Oktober 2019, GZ 2 R 140/19z-30, mit dem das Urteil des Landesgerichts Wels vom 22. Juli 2019, GZ 26 Cg 66/18m-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch I. Das Verfahren wird bis zur Entscheidung des Europäischen Gerichtshofs über den vom Obersten Gerichtshof am 17.

| Predicted | Gold |
|---|---|
| `OberTratraSoftware Dienstleistungen AG` | `OberTratraSoftware Dienstleistungen AG` |

**Missed by this rule (FN):**

- `Prägrader Weg 43, 8616 Gasen, Österreich` (address)

**Example 11** (doc_id: `deanon_TRAIN/6Ob207_18m`) (sent_id: `deanon_TRAIN/6Ob207_18m_4`)


Balnuweit Technik GmbH, sowie 2. Ost Werkmon GmbH, alle Am Waidfeld 8, 5211 Gstöckat, Österreich, alle vertreten durch Dr. Peter Zöchbauer, Rechtsanwalt in Wien, wegen (zuletzt) Widerrufs, Veröffentlichung und Zahlung von 9.000 EUR, über die Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 30. Mai 2018, GZ 5 R 39/18v-27, womit über Berufung der beklagten Parteien das Urteil des Handelsgerichts Wien vom 24. Jänner 2018, GZ 39 Cg 26/17t-23, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Balnuweit Technik GmbH` | `Balnuweit Technik GmbH` |

**Missed by this rule (FN):**

- `Ost Werkmon GmbH` (organisation)
- `Am Waidfeld 8, 5211 Gstöckat, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/7Ob203_24i`) (sent_id: `deanon_TRAIN/7Ob203_24i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei PhD Lara Scharpwinkel, vertreten durch Mag. Martin Wabra, Rechtsanwalt in Gmünd, gegen die beklagte Partei Fenbach-IT AG, Linn Zemlik, vertreten durch die MUSEY rechtsanwalt gmbH in Salzburg, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Oktober 2024, GZ 5 R 144/24v-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `IT AG` — partial — pred is substring of gold: `Fenbach-IT AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Lara Scharpwinkel`(person)
- `Fenbach-IT AG`(organisation)
- `Linn Zemlik`(person)

**Example 1** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_6`)


Text Entscheidungsgründe: Mit Bescheid vom 26. 4. 2010 lehnte die beklagte Partei den Antrag des Klägers auf Gewährung der Kostenerstattung für die Inanspruchnahme der Alpen-KI GmbH (im Folgenden kurz: GmbH) laut Rechnungen vom 2. 10. 2009 und 6. 11. 2009 in Höhe von insgesamt 540 EUR ab.

**False Positives:**

- `KI GmbH` — partial — pred is substring of gold: `Alpen-KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alpen-KI GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_9`)


Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH in Anspruch genommen und dafür insgesamt 540 EUR bezahlt.

**False Positives:**

- `Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_13`)


Dem für die GmbH tätigen Team gehörten renommierte Fachärzte für medizinische Unfallchirurgie sowie Sportärzte an.

**False Positives:**

- `Dem für die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_30`)


Zwischen der GmbH und der beklagten Partei besteht kein Vertragsverhältnis.

**False Positives:**

- `Zwischen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_31`)


Die GmbH verfügt auch über keine Bewilligung als Krankenanstalt bzw selbständiges Ambulatorium im Sinne des WrKAG und über keinen ärztlichen Leiter.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_33`)


Anhand dieser Vorgaben werden die von der GmbH entwickelten speziellen Trainingsmethoden angewandt.

**False Positives:**

- `Anhand dieser Vorgaben werden die von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_39`)


Der Geschäftsführer der GmbH ist diplomierter Sportlehrer.

**False Positives:**

- `Der Geschäftsführer der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_140`)


Handelt es sich bei den von der GmbH angebotenen Trainings um Leistungen anderer Gesundheitsberufe, die nicht in § 135 Abs 1 ASVG aufgelistet sind, ist eine Analogie ausgeschlossen (siehe oben Pkt 1.1.).

**False Positives:**

- `Handelt es sich bei den von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/4Ob244_18p`) (sent_id: `deanon_TRAIN/4Ob244_18p_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Wehrstedt Metall GmbH, Holger Heldwein, vertreten durch Dr. Franz Gütlbauer und andere Rechtsanwälte in Wels, gegen die beklagte Partei Ostwilzor-Metall gesellschaft mbH, Schilchergasse 5, 8230 Oberlungitz, Österreich, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH in Ried im Innkreis, wegen 44.635,70 EUR sA und Feststellung (Streitwert 8.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Oktober 2018, GZ 1 R 86/18z-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Wehrstedt Metall GmbH` — partial — gold is substring of pred: `Wehrstedt Metall GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wehrstedt Metall GmbH`(organisation)
- `Holger Heldwein`(person)
- `Ostwilzor-Metall gesellschaft mbH`(organisation)
- `Schilchergasse 5, 8230 Oberlungitz, Österreich`(address)

**Example 10** (doc_id: `deanon_TRAIN/1Ob167_22y`) (sent_id: `deanon_TRAIN/1Ob167_22y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Unitradon-Telekom GmbH, Leila Chatzifotiou, vertreten durch Mag. Dr. Maria Lisa Aidin, Rechtsanwältin in Salzburg, gegen die beklagte Partei Maurice Scheinert, vertreten durch Dr. Thomas Mondl, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 8.000 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Landesgerichts Leoben vom 25. Juli 2022, GZ 1 R 94/22y-48, mit dem der Rekurs gegen den Beschluss des Landesgerichts Leoben als Berufungsgericht vom 9. Mai 2022, GZ 1 R 94/22z-37, sowie Anträge auf „Ausspruch der Zulässigkeit des Revisionsrekurses“ und „Abänderung des Ausspruchs über die Zulässigkeit“ zurückgewiesen wurden, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Telekom GmbH` — partial — pred is substring of gold: `Unitradon-Telekom GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unitradon-Telekom GmbH`(organisation)
- `Leila Chatzifotiou`(person)
- `Maurice Scheinert`(person)

**Example 11** (doc_id: `deanon_TRAIN/8ObS5_19x`) (sent_id: `deanon_TRAIN/8ObS5_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Ingomar Stuper (aus dem Kreis der Arbeitgeber) und Günter Hintersteiner (aus dem Kreis der Arbeitnehmer) in der Sozialrechtssache der klagenden Partei Mag. Simon Ascioglu, gegen die beklagte Partei IEF-Service GmbH, Geschäftsstelle Graz, 8020 Graz, Europaplatz 12, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, wegen 19.146 EUR, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. April 2019, GZ 7 Rs 81/18p-13, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Service GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Simon Ascioglu`(person)

**Example 12** (doc_id: `deanon_TRAIN/8ObS5_19x`) (sent_id: `deanon_TRAIN/8ObS5_19x_29`)


Die Vollmacht des Klägers (im Innenverhältnis) war auf die Vertretung der Inn-Energie GmbH beim Abschluss eines Beteiligungsvertrags mit einer bestimmten Investorin in der Generalversammlung am 1. 2. 2018, als der Kläger selbst noch gar nicht Minderheitsgesellschafter der Kleinkurt Sicherheit GmbH war, beschränkt.

**False Positives:**

- `Energie GmbH` — partial — pred is substring of gold: `Inn-Energie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn-Energie GmbH`(organisation)
- `Kleinkurt Sicherheit GmbH`(organisation)

**Example 13** (doc_id: `deanon_TRAIN/4Ob31_22w`) (sent_id: `deanon_TRAIN/4Ob31_22w_4`)


Matzka sowie die Hofrätin Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei UTZ Textil Betriebe GmbH, Vincent Clasen, vertreten durch Mag. Lukas Leszkovics, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Kelsyn-Metall GmbH, Barbara Nüssler, vertreten durch Mag. Oliver Simoncic, Rechtsanwalt in St. Pölten, wegen 772.775,54 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 13. Jänner 2022, GZ 5 R 126/21t-72, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Metall GmbH` — partial — pred is substring of gold: `Kelsyn-Metall GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UTZ Textil Betriebe GmbH`(organisation)
- `Vincent Clasen`(person)
- `Kelsyn-Metall GmbH`(organisation)
- `Barbara Nüssler`(person)

**Example 14** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_7`)


TraunChemie GmbH & Co KG, Badeteich Bisamberg 16, 4625 Kronberg, Österreich, vertreten durch Siemer-Siegl-Füreder & Partner, Rechtsanwälte OG in Wien, wegen 59.104,03 EUR sA, über die außerordentlichen Revisionsrekurse der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 2. Mai 2011, GZ 2 R 182/10p-50, womit über Rekurs der klagenden Partei der Beschluss des Landesgerichts Steyr vom 23. August 2010, GZ 4 Cg 154/08t-34, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentlichen Revisionsrekurse werden gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `TraunChemie GmbH & Co KG` — partial — gold is substring of pred: `TraunChemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunChemie GmbH`(organisation)
- `Badeteich Bisamberg 16, 4625 Kronberg, Österreich`(address)

**Example 15** (doc_id: `deanon_TRAIN/1Ob213_15b`) (sent_id: `deanon_TRAIN/1Ob213_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Erlagssache der Antragstellerin Versicherung Tristein GmbH, Admont 97, 4701 Müllerberg, Österreich, vertreten durch Dr. Markus Andréewitch und andere Rechtsanwälte in Wien, gegen die Antragsgegner 1.

**False Positives:**

- `Rennhofer als weitere Richter in der Erlagssache der Antragstellerin Versicherung Tristein GmbH` — partial — gold is substring of pred: `Versicherung Tristein GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Versicherung Tristein GmbH`(organisation)
- `Admont 97, 4701 Müllerberg, Österreich`(address)

**Example 16** (doc_id: `deanon_TRAIN/5Ob200_24h`) (sent_id: `deanon_TRAIN/5Ob200_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Ing. Harald Josepeit, vertreten durch die Wutte-Lang Rechtsanwalts GmbH in Klagenfurt, und der Nebenintervenientin auf Seiten der klagenden Partei MMag.

**False Positives:**

- `Lang Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Harald Josepeit`(person)

**Example 17** (doc_id: `deanon_TRAIN/3Ob248_19w`) (sent_id: `deanon_TRAIN/3Ob248_19w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Rechtssache der klagenden Partei Leikauf Daten AG, Mag.a Erna Leitgen, vertreten durch Widter Mayrhauser Wolf Rechtsanwälte OG in Wien, gegen die beklagten Parteien 1. Marine Furtlog GmbH, 2. Dipl.-Ing. Viola Schöndube, beide vertreten durch Mag. Wolfgang Vinatzer, Rechtsanwalt in Wien, wegen 1.241.906,55 EUR sA, über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Oktober 2019, GZ 1 R 126/19k-31, den Beschluss gefasst:  Spruch I.Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Kristöfel als weitere Richter in der Rechtssache der klagenden Partei Leikauf Daten AG` — partial — gold is substring of pred: `Leikauf Daten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Leikauf Daten AG`(organisation)
- `Mag.a Erna Leitgen`(person)
- `Marine Furtlog GmbH`(organisation)
- `Dipl.-Ing. Viola Schöndube`(person)

**Example 18** (doc_id: `deanon_TRAIN/7Ob150_17k`) (sent_id: `deanon_TRAIN/7Ob150_17k_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Getränke Uniallog AG, Elisabeth Ehredt, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Zorsudfen Handel GmbH, Lena Stumbra, vertreten durch Dr. Alexander Katholnig, MBL, Rechtsanwalt in Kitzbühel, wegen 8.037,65 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 14. Juni 2017, GZ 77 R 57/17y-20, mit dem das Urteil des Bezirksgerichts Kitzbühel vom 2. März 2017, GZ 2 C 834/16a-16, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Getränke Uniallog AG` — partial — gold is substring of pred: `Getränke Uniallog AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Getränke Uniallog AG`(organisation)
- `Elisabeth Ehredt`(person)
- `Zorsudfen Handel GmbH`(organisation)
- `Lena Stumbra`(person)

**Example 19** (doc_id: `deanon_TRAIN/18OCg4_20t`) (sent_id: `deanon_TRAIN/18OCg4_20t_5`)


Die Beklagte ist eine Aktiengesellschaft mit Sitz in Italien.

**False Positives:**

- `Die Beklagte ist eine Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/4Ob59_17f`) (sent_id: `deanon_TRAIN/4Ob59_17f_4`)


Matzka als weitere Richter in der Rechtssache der Klägerin Alpen Logkel GmbH, Dorrekstraße 17, 4812 Großkufhaus, Österreich, vertreten durch Knoflach, Kroker, Tonini & Partner, Rechtsanwälte in Innsbruck, gegen die Beklagte Pavlovic und Robbertz Technik Gesellschaft mbH, Krenntal 7, 9470 Loschental, Österreich, vertreten durch Dr. Bernd Roßkothen, Rechtsanwalt in Salzburg, wegen Unterlassung (Streitwert im Sicherungsverfahren 43.200 EUR), über den außerordentlichen Revisionsrekurs der Beklagten gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 13. Februar 2017, GZ 4 R 14/17g-17, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der Klägerin Alpen Logkel GmbH` — partial — gold is substring of pred: `Alpen Logkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alpen Logkel GmbH`(organisation)
- `Dorrekstraße 17, 4812 Großkufhaus, Österreich`(address)
- `Pavlovic und Robbertz Technik Gesellschaft mbH`(organisation)
- `Krenntal 7, 9470 Loschental, Österreich`(address)

**Example 21** (doc_id: `deanon_TRAIN/9ObA141_19d`) (sent_id: `deanon_TRAIN/9ObA141_19d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshof Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Peter Zeitler (aus dem Kreis der Arbeitnehmer) und Angela Taschek (aus dem Kreis der Arbeitgeber) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Adelheid Haaf, LLB, vertreten durch Dr. Thomas Krankl, Rechtsanwalt in Wien, gegen die beklagte Partei Nossack Analyse AG, Sascha Steinke, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 1.397.481,32 EUR netto sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. Oktober 2019, GZ 9 Ra 14/19y-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Adelheid Haaf, LLB`(person)
- `Nossack Analyse AG`(organisation)
- `Sascha Steinke`(person)

**Example 22** (doc_id: `deanon_TRAIN/6Ob23_18b`) (sent_id: `deanon_TRAIN/6Ob23_18b_25`)


Die gegenständliche Sammelklage wird von einer Prozessfinanzierungs AG (gegen ein Entgelt von 20 % des Erlöses) und mit PR-Unterstützung einer Agentur betrieben.

**False Positives:**

- `Die gegenständliche Sammelklage wird von einer Prozessfinanzierungs AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/7Ob143_19h`) (sent_id: `deanon_TRAIN/7Ob143_19h_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Donau Furttalsyn GmbH, Hugo Fasters, vertreten durch Urbanek & Rudolph Rechtsanwälte OG in Wien, gegen die beklagte Partei Mentele Touristik AG, Friedrich Klingfuss, vertreten durch Handler Rechtsanwalt GmbH in Deutschlandsberg, wegen 55.505,74 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Juni 2019, GZ 1 R 65/19i-43, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Donau Furttalsyn GmbH` — partial — gold is substring of pred: `Donau Furttalsyn GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donau Furttalsyn GmbH`(organisation)
- `Hugo Fasters`(person)
- `Mentele Touristik AG`(organisation)
- `Friedrich Klingfuss`(person)

**Example 24** (doc_id: `deanon_TRAIN/8ObS6_23z`) (sent_id: `deanon_TRAIN/8ObS6_23z_8`)


Der Kläger war bei der mittlerweile insolventen Allember-Wind GmbH als Lkw-Fahrer beschäftigt und erlitt am 9.

**False Positives:**

- `Wind GmbH` — partial — pred is substring of gold: `Allember-Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Allember-Wind GmbH`(organisation)

**Example 25** (doc_id: `deanon_TRAIN/8Ob4_18y`) (sent_id: `deanon_TRAIN/8Ob4_18y_4`)


Vossbrinck Wind AG, Flurnsbach 9, 4722 Untwüsten, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte GmbH in Wien, und 2. Steinheim-Cloud Limited, Anlauftalstraße 23, 4623 Kalchau, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.141,02 EUR, über die Revision der erstbeklagten Partei gegen das Teilurteil des Handelsgerichts Wien als Berufungsgericht vom 18. September 2017, GZ 60 R 20/17x-29, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 3. Jänner 2017, GZ 20 C 529/15p-24, in der Hauptsache hinsichtlich der erstbeklagten Partei bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Cloud Limited` — partial — pred is substring of gold: `Steinheim-Cloud Limited`
- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Vossbrinck Wind AG`(organisation)
- `Flurnsbach 9, 4722 Untwüsten, Österreich`(address)
- `Steinheim-Cloud Limited`(organisation)
- `Anlauftalstraße 23, 4623 Kalchau, Österreich`(address)

**Example 26** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michael Puhm (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Hermine Thom, vertreten durch Dr. Markus Orgler, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Mur Brucktridon AG, Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat., vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 4.200,83 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 17. Oktober 2019, GZ 13 Ra 41/15z-30, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hermine Thom`(person)
- `Mur Brucktridon AG`(organisation)
- `Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat.`(person)

**Example 27** (doc_id: `deanon_TRAIN/7Ob60_18a`) (sent_id: `deanon_TRAIN/7Ob60_18a_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Ariadne Kieble, vertreten durch Dr. Josef Sailer, Rechtsanwalt in Bruck an der Leitha, gegen die beklagte Partei Seeglanz-Umwelt AG, Volkmar Heinbichner, LLB Bakk. iur., vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2018, GZ 1 R 127/17d-15, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Umwelt AG` — partial — pred is substring of gold: `Seeglanz-Umwelt AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ariadne Kieble`(person)
- `Seeglanz-Umwelt AG`(organisation)
- `Volkmar Heinbichner, LLB Bakk. iur.`(person)

**Example 28** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_8`)


B./II./ am 13. November 2009 in Poysdorf als Zeugin in einem Ermittlungsverfahren nach der Strafprozessordnung vor der Kriminalpolizei bei ihrer förmlichen Vernehmung zur Sache falsch ausgesagt, indem sie wahrheitswidrig behauptete, die an sie bezahlten 22.800 Euro seien das Entgelt für LKW-Vermietungen an die Ost Lextal GmbH gewesen, wobei sie tatsächlich das Geld ausbezahlt bekam, ohne dafür an die genannte Gesellschaft eine Gegenleistung erbracht zu haben.

**False Positives:**

- `Vermietungen an die Ost Lextal GmbH` — partial — gold is substring of pred: `Ost Lextal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ost Lextal GmbH`(organisation)

**Example 29** (doc_id: `deanon_TRAIN/7Ob126_09v`) (sent_id: `deanon_TRAIN/7Ob126_09v_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei MAYK Garten GmbH, Bartholomäus Iffläender, BA, vertreten durch Dr. Gerhard Mitterböck, Rechtsanwalt in Wien, gegen die beklagte Partei Schneiderlin+Balles Transport GmbH, Carla Havlikova, vertreten durch Walch & Zehetbauer Rechtsanwälte OEG in Wien, wegen 14.018,90 EUR, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Februar 2009, GZ 4 R 210/08v-49, mit dem infolge Berufung der beklagten Partei das Urteil des Landes- als Handelsgerichts Korneuburg vom 22. Juli 2008, GZ 4 Cg 135/07d-39, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch Der Revision wird nicht Folge gegeben.

**False Positives:**

- `Balles Transport GmbH` — partial — pred is substring of gold: `Schneiderlin+Balles Transport GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MAYK Garten GmbH`(organisation)
- `Bartholomäus Iffläender, BA`(person)
- `Schneiderlin+Balles Transport GmbH`(organisation)
- `Carla Havlikova`(person)

**Example 30** (doc_id: `deanon_TRAIN/7Ob48_15g`) (sent_id: `deanon_TRAIN/7Ob48_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Raphael Pabstmann, vertreten durch Dr. Herbert Laimböck, Rechtsanwalt in Wien, gegen die beklagte Partei Altunkaynak&Teifel Analyse AG, Arabella Frommke, vertreten durch Dr. Herbert Salficky, Rechtsanwalt in Wien, wegen 29.769,46 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Jänner 2015, GZ 1 R 193/14f-53, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Teifel Analyse AG` — partial — pred is substring of gold: `Altunkaynak&Teifel Analyse AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Raphael Pabstmann`(person)
- `Altunkaynak&Teifel Analyse AG`(organisation)
- `Arabella Frommke`(person)

**Example 31** (doc_id: `deanon_TRAIN/3Ob203_19b`) (sent_id: `deanon_TRAIN/3Ob203_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Rechtssache der klagenden Partei Samir Golabek, vertreten durch Mag. Barbara Loipetsberger, Rechtsanwältin in Vöcklabruck, gegen die beklagte Partei Norsud-Energie AG, Knut Petschock, vertreten durch Mag. Jürgen Lappi, Rechtsanwalt in Vöcklabruck, wegen Unzulässigerklärung einer Exekution (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 3. Juli 2019, GZ 22 R 172/19d-22, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Energie AG` — partial — pred is substring of gold: `Norsud-Energie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Samir Golabek`(person)
- `Norsud-Energie AG`(organisation)
- `Knut Petschock`(person)

**Example 32** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 33** (doc_id: `deanon_TRAIN/4Ob24_20p`) (sent_id: `deanon_TRAIN/4Ob24_20p_5`)


Nord-Sanitär GmbH, Kraftkel-Event, 2. Dickmänken+Schaunsland Heizung GmbH, F.-Kogler-Weg 18, 4084 Sattlberg, Österreich, beide vertreten durch Partnerschaft SCHUPPICH SPORN & WINISCHHOFER Rechtsanwälte in Wien, gegen die beklagte Partei Hinterholzner Recycling GmbH, KzlR Egon Litvine, BSc, vertreten durch PISTOTNIK & KRILYSZYN Rechtsanwälte in Wien, und die Nebenintervenientin auf Seiten der beklagten Partei Wien Furtseetra GmbH, Arnold Wöbbe, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen zuletzt 4.264.783,18 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. November 2019, GZ 129 R 91/19d-367, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Sanitär GmbH` — partial — pred is substring of gold: `Nord-Sanitär GmbH`
- `Schaunsland Heizung GmbH` — partial — pred is substring of gold: `Dickmänken+Schaunsland Heizung GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Nord-Sanitär GmbH`(organisation)
- `Kraftkel-Event`(organisation)
- `Dickmänken+Schaunsland Heizung GmbH`(organisation)
- `F.-Kogler-Weg 18, 4084 Sattlberg, Österreich`(address)
- `Hinterholzner Recycling GmbH`(organisation)
- `KzlR Egon Litvine, BSc`(person)
- `Wien Furtseetra GmbH`(organisation)
- `Arnold Wöbbe`(person)

**Example 34** (doc_id: `deanon_TRAIN/7Ob11_22a`) (sent_id: `deanon_TRAIN/7Ob11_22a_6`)


IT Sudtraver GmbH, Wald-Marine, und 2. Tal Seewil GmbH, Grappaweg 1, 5310 Hof, Österreich, beide vertreten durch die DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Herausgabe und Feststellung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2021, GZ 4 R 149/21s-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Tessbach Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `IT Sudtraver GmbH`(organisation)
- `Wald-Marine`(organisation)
- `Tal Seewil GmbH`(organisation)
- `Grappaweg 1, 5310 Hof, Österreich`(address)

**Example 35** (doc_id: `deanon_TRAIN/7Ob65_15g`) (sent_id: `deanon_TRAIN/7Ob65_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Hofrätin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Nortri-Umwelt GmbH & Co KG, Piberberg 8, 4720 Unternfurth, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in Salzburg, gegen die beklagte Partei Anton Adil Versicherungs-Aktiengesellschaft, Am Kastanienhof 90, 6162 Mutters, Österreich, vertreten durch Dr. Johannes Kirschner, Rechtsanwalt in Wels, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 19. Jänner 2015, GZ 1 R 198/14i-14, womit das Urteil des Landesgerichts Wels vom 29. September 2014, GZ 2 Cg 65/14g-10, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Umwelt GmbH & Co KG` — positional overlap with gold: `Nortri-Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nortri-Umwelt GmbH`(organisation)
- `Piberberg 8, 4720 Unternfurth, Österreich`(address)
- `Anton Adil`(person)
- `Am Kastanienhof 90, 6162 Mutters, Österreich`(address)

**Example 36** (doc_id: `deanon_TRAIN/5Ob202_09f`) (sent_id: `deanon_TRAIN/5Ob202_09f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Danzl als Vorsitzenden sowie die Hofrätinnen/Hofräte des Obersten Gerichtshofs Dr. Hurch, Dr. Lovrek, Dr. Höllwerth und Dr. Tarmann-Prentner als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Kadzimirsz Sicherheit GmbH, Rottenmannerstraße 19, 3231 Wieden, Österreich, vertreten durch Dr. Karl Grigkar, Rechtsanwalt in Wien, wider den Antragsgegner Herbert Dietmaier, vertreten durch Hule Bachmayr-Heyda Nordberg Rechtsanwälte GmbH in Wien, wegen § 12a iVm § 46 Abs 2 MRG, über den Revisionsrekurs der Antragstellerin gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. Mai 2009, GZ 39 R 2/09z-17, womit infolge Rekurses der Antragstellerin der Sachbeschluss des Bezirksgerichts Innere Stadt Wien vom 27. Oktober 2008, GZ 48 Msch 9/08v-11, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Prentner als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Kadzimirsz Sicherheit GmbH` — partial — gold is substring of pred: `Kadzimirsz Sicherheit GmbH`
- `Heyda Nordberg Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Kadzimirsz Sicherheit GmbH`(organisation)
- `Rottenmannerstraße 19, 3231 Wieden, Österreich`(address)
- `Herbert Dietmaier`(person)

**Example 37** (doc_id: `deanon_TRAIN/4Ob26_15z`) (sent_id: `deanon_TRAIN/4Ob26_15z_4`)


Beate Feuchte GmbH, Untere Öfnerstraße 36, 2852 Burgerschlag, Österreich, 2. Etzelsdorf 10, 5232 Wendling, Österreich, 3. Selker 4, 4134 Pernersdorf, Österreich, 4. Dr. Janis Böckenkämper, Italien, 5. Keberlein+Kubank Telekom AG, Karl Heinschild-Weg 3, 8273 Ebersdorf, Österreich, Italien, alle vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, wegen 213.977,45 EUR sA (erstbeklagte Partei) und Kosten (zweit- bis fünftbeklagte Parteien), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 18. Dezember 2014, GZ 2 R 199/14b-130, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Beate Feuchte GmbH` — partial — gold is substring of pred: `Beate Feuchte`
- `Kubank Telekom AG` — partial — pred is substring of gold: `Keberlein+Kubank Telekom AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Beate Feuchte`(person)
- `Untere Öfnerstraße 36, 2852 Burgerschlag, Österreich`(address)
- `Etzelsdorf 10, 5232 Wendling, Österreich`(address)
- `Selker 4, 4134 Pernersdorf, Österreich`(address)
- `Dr. Janis Böckenkämper`(person)
- `Keberlein+Kubank Telekom AG`(organisation)
- `Karl Heinschild-Weg 3, 8273 Ebersdorf, Österreich`(address)

**Example 38** (doc_id: `deanon_TRAIN/4Ob26_15z`) (sent_id: `deanon_TRAIN/4Ob26_15z_15`)


3. In der von den Vorinstanzen ihrer Schadensberechnung nach § 273 ZPO zugrundeliegenden Methode, den Deckungsbeitrag des halben Umsatzes der Valwald-Finanzen GmbH mit den Kunden der klagenden Partei („gemeinsame Kunden“) heranzuziehen, ist jedenfalls keine krasse Ermessensüberschreitung zu erblicken, die einer höchstgerichtlichen Korrektur bedarf.

**False Positives:**

- `Finanzen GmbH` — partial — pred is substring of gold: `Valwald-Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valwald-Finanzen GmbH`(organisation)

**Example 39** (doc_id: `deanon_TRAIN/9Ob67_09g`) (sent_id: `deanon_TRAIN/9Ob67_09g_5`)


Babette Wienkemeier, 3. HR Dario Litwinowa, 4. Eigenbrod Versicherung GmbH & Co KG, Dr. Franz Stumpf-Straße 48, 2002 Ottendorf, Österreich, 5. Dr. David Alswede, 6. Dipl.-Ing. Manuela Himmel, vertreten durch die Gassauer-Fleissner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Ing. Felizia Tscherning, vertreten durch Mag. Markus Adam, Rechtsanwalt in Wien, wegen Räumung (Streitwert 8.954,16 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 16. Juni 2009, GZ 41 R 98/09d-12, womit das Urteil des Bezirksgerichts Innere Stadt Wien vom 26. Februar 2009, GZ 30 C 200/08y-7, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Fleissner Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Babette Wienkemeier`(person)
- `HR Dario Litwinowa`(person)
- `Eigenbrod Versicherung GmbH`(organisation)
- `Dr. Franz Stumpf-Straße 48, 2002 Ottendorf, Österreich`(address)
- `Dr. David Alswede`(person)
- `Dipl.-Ing. Manuela Himmel`(person)
- `Ing. Felizia Tscherning`(person)

**Example 40** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ulm Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Janet Henken`(person)
- `Elvira Nossal`(person)

**Example 41** (doc_id: `deanon_TRAIN/3Ob170_20a`) (sent_id: `deanon_TRAIN/3Ob170_20a_7`)


Das Rekursgericht ließ den Revisionsrekurs zur Frage zu, ob zugewartet werden müsse, bis der selbständig erwerbstätige (an einer GmbH beteiligte und als Abwickler einer anderen Gesellschaft tätige) Antragsgegner das Wirtschaftsjahr 2017 „abschließt“, oder ob sein Einkommen anhand der letzten drei Wirtschaftsjahre ermittelt werden könne.

**False Positives:**

- `an einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/3Ob92_12v`) (sent_id: `deanon_TRAIN/3Ob92_12v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie durch den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Joachim Dammann, MBA, als Masseverwalter im Konkurs über das Vermögen der Furtheimheim-Getränke GmbH, Trefferweg 4, 4632 Franzing, Österreich, wider die beklagte Partei „ EBK Umwelt Solutions “-***** GmbH, Andreas-Hofer-Gasse 70, 4310 Marbach, Österreich, vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen 16.877,09 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Jänner 2012, GZ 2 R 266/11v-14, womit infolge Berufung der klagenden Partei das Urteil des Handelsgerichts Wien vom 14. Oktober 2011, GZ 43 Cg 35/11m-10, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Getränke GmbH` — partial — pred is substring of gold: `Furtheimheim-Getränke GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Joachim Dammann, MBA`(person)
- `Furtheimheim-Getränke GmbH`(organisation)
- `Trefferweg 4, 4632 Franzing, Österreich`(address)
- `EBK Umwelt Solutions`(organisation)
- `Andreas-Hofer-Gasse 70, 4310 Marbach, Österreich`(address)

**Example 43** (doc_id: `deanon_TRAIN/1Ob79_17z`) (sent_id: `deanon_TRAIN/1Ob79_17z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Scherg und Kintzli Holz GmbH, Ramon Reynert, vertreten durch die Saxinger Chalupsky & Partner Rechtsanwälte GmbH, Linz, gegen die beklagte Partei Wagenlöhner Versand GmbH, Maurice Schwoob, vertreten durch die Schneider Rechtsanwalts KG, Wien, wegen 6.239,26 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 30. September 2016, GZ 21 R 125/16d-26, mit dem das Urteil des Bezirksgerichts Hollabrunn vom 14. April 2016, GZ 1 C 335/15k-20, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt und beschlossen:  Spruch

**False Positives:**

- `Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Scherg und Kintzli Holz GmbH` — partial — gold is substring of pred: `Scherg und Kintzli Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Scherg und Kintzli Holz GmbH`(organisation)
- `Ramon Reynert`(person)
- `Wagenlöhner Versand GmbH`(organisation)
- `Maurice Schwoob`(person)

**Example 44** (doc_id: `deanon_TRAIN/12Os49_20b`) (sent_id: `deanon_TRAIN/12Os49_20b_8`)


Danach hat er mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz Nachgenannte „gewerbsmäßig (§ 70 StGB)“ durch Täuschung über Tatsachen zu Handlungen verleitet, die diese am Vermögen schädigten, wobei er bei den einzelnen Angriffen überwiegend einen 5.000 Euro, insgesamt jedoch 300.000 Euro nicht übersteigenden Schaden herbeiführte und herbeizuführen beabsichtigte, und zwar A./ am 5. Juni 2012 in Betty-Fischer-Weg 1, 2662 Graben, Österreich im bewussten und gewollten Zusammenwirken mit einer Mittäterin Verfügungsberechtigten der Wilsuduni-Textil GmbH durch die Vorspiegelung, ein redlicher Vertragspartner zu sein, insbesondere die von ihm als Darlehensnehmer zu leistenden Raten vertragsgemäß zu bedienen und mit dem zur Besicherung des Darlehens belehnten Pkw Audi A6 vertragskonform zu disponieren, zur Auszahlung eines Darlehensbetrags von 6.500 Euro;

**False Positives:**

- `Textil GmbH` — partial — pred is substring of gold: `Wilsuduni-Textil GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Betty-Fischer-Weg 1, 2662 Graben, Österreich`(address)
- `Wilsuduni-Textil GmbH`(organisation)

**Example 45** (doc_id: `deanon_TRAIN/11Os151_21x`) (sent_id: `deanon_TRAIN/11Os151_21x_26`)


[12] Fallbezogen ist aber von einer Vertretung des Beschwerdeführers durch einen Rechtsanwalt ohnedies auszugehen, weil nach dem Deckblatt der Beschwerdeschrift („vertreten durch“, „Vollmacht erteilt“) die – zulässig und wirksam (§ 21e RAO) – bevollmächtigte Di Inn-Medien Rechtsanwalts GmbH eingeschritten ist, in welcher (unwiderlegt) ein neben dem Beschwerdeführer vertretungsbefugter weiterer Gesellschafter mit der Vertretung (§ 8 Abs 1 RAO) befasst war.

**False Positives:**

- `Medien Rechtsanwalts GmbH` — positional overlap with gold: `Inn-Medien`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn-Medien`(organisation)

**Example 46** (doc_id: `deanon_TRAIN/8ObA43_16f`) (sent_id: `deanon_TRAIN/8ObA43_16f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn sowie die fachkundigen Laienrichter Dr. Christoph Kainz und Mag. Canan Aytekin-Yildirim als weitere Richter in der Arbeitsrechtssache der klagenden Partei HR Charlotte Hiemer, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_Innen GmbH in Wien, gegen die beklagte Partei WaldTelekom Betriebe AG, Selina Dorpmanns, BA, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 16.482,15 EUR brutto sA und Feststellung (Streitwert 2.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 28. April 2016, GZ 10 Ra 113/15h-61, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Charlotte Hiemer`(person)
- `WaldTelekom Betriebe AG`(organisation)
- `Selina Dorpmanns, BA`(person)

**Example 47** (doc_id: `deanon_TRAIN/7Ob30_10b`) (sent_id: `deanon_TRAIN/7Ob30_10b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Hoch Verval GmbH, Andreas Bluemke, vertreten durch Piaty Müller-Mezin Schoeller Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Härtkorn Versicherung Versicherung AG, Teurniastraße 17, 4063 Aistental, Österreich, vertreten durch Christandl Rechtsanwalt GmbH in Graz, wegen 18.409,80 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 4. Juni 2009, GZ 4 R 47/09b-33, womit das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 10. Dezember 2008, GZ 14 Cg 195/05f-26, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Mezin Schoeller Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hoch Verval GmbH`(organisation)
- `Andreas Bluemke`(person)
- `Härtkorn Versicherung`(organisation)
- `Teurniastraße 17, 4063 Aistental, Österreich`(address)

**Example 48** (doc_id: `deanon_TRAIN/3Ob70_20w`) (sent_id: `deanon_TRAIN/3Ob70_20w_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Hon.-Prof. PD Dr. Rassi, die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek und den Hofrat Dr. Stefula als weitere Richter in der Rechtssache der klagenden Partei NiederE‑Commerce Werke gesmbH, Dagmar Saroglou, vertreten durch Dr. Zsizsik & Dr. Prattes Rechtsanwälte OG in Bruck an der Mur, und der auf ihrer Seite beigetretenen Nebenintervenientin NiederBau GmbH, Silvaraweg 26, 8162 Amstein, Österreich, vertreten durch Reif und Partner Rechtsanwälte OG in Kapfenberg, gegen die beklagte Partei Drau-Verlag GesmbH, Denise Sedelmeyr, vertreten durch Dr. Klaus Kollmann und andere Rechtsanwälte in Graz, wegen 260.830,48 EUR sA, über den Rekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht vom 31. Jänner 2020, GZ 2 R 149/19b-19, womit das Urteil des Landesgerichts Leoben vom 8. Juli 2019, GZ 26 Cg 104/18i-15, aufgehoben wurde, den Beschluss gefasst:  Spruch Der Rekurs wird zurückgewiesen.

**False Positives:**

- `Commerce Werke gesmbH` — partial — pred is substring of gold: `NiederE‑Commerce Werke gesmbH`
- `Verlag GesmbH` — partial — pred is substring of gold: `Drau-Verlag GesmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `NiederE‑Commerce Werke gesmbH`(organisation)
- `Dagmar Saroglou`(person)
- `NiederBau GmbH`(organisation)
- `Silvaraweg 26, 8162 Amstein, Österreich`(address)
- `Drau-Verlag GesmbH`(organisation)
- `Denise Sedelmeyr`(person)

**Example 49** (doc_id: `deanon_TRAIN/6Ob16_20a`) (sent_id: `deanon_TRAIN/6Ob16_20a_52`)


Aus der Unternehmereigenschaft der GmbH kraft Rechtsform (§ 2 UGB) könne nicht geschlossen werden, dass die GmbH auch ein Unternehmen betreibe.

**False Positives:**

- `Aus der Unternehmereigenschaft der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_TRAIN/6Ob16_20a`) (sent_id: `deanon_TRAIN/6Ob16_20a_58`)


Überdies spreche die Bestimmung von der „Veräußerung eines Unternehmens“ und nicht von der „Veräußerung von Geschäftsanteilen an GmbH oder Aktien“.

**False Positives:**

- `Veräußerung von Geschäftsanteilen an GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_4`)


Matzka als weitere Richter in der Rechtssache der Klägerin Drenker Landwirtschaft GmbH, Hörgasstraße 35, 4152 Eilmannsberg, Österreich, vertreten durch Hofbauer & Nokaj Rechtsanwalts GmbH in Ybbs/Donau, gegen die Beklagte Guggemos u. Kirchmann Möbel GmbH Aigeln 23, 2136 Neudorf im Weinviertel, Österreich, vertreten durch Dr. Stefan Gloss, Rechtsanwalt in St. Pölten, wegen 768.674,16 EUR sA, über die außerordentlicheRevision der Klägerin gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. April 2018, GZ 5 R 22/18v-37,den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der Klägerin Drenker Landwirtschaft GmbH` — partial — gold is substring of pred: `Drenker Landwirtschaft GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Drenker Landwirtschaft GmbH`(organisation)
- `Hörgasstraße 35, 4152 Eilmannsberg, Österreich`(address)
- `Guggemos u. Kirchmann Möbel GmbH`(organisation)
- `Aigeln 23, 2136 Neudorf im Weinviertel, Österreich`(address)

**Example 52** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_6`)


Die KG wurde aufgelöst und der Geschäftsbetrieb eingestellt.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_9`)


Die Beklagte informierte die Kunden der KG, dass sie alle Geschäfte der KG mit allen Rechten und Pflichten übernehme.

**False Positives:**

- `Die Beklagte informierte die Kunden der KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_11`)


Die KG habe nämlich dahingehend beraten, dass der Schweinestall der Klägerin aufgrund von Mängeln komplett zu sanieren sei.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_24`)


Die KG sei im Zusammenhang mit der Pensionierung ihres Komplementärs aufgelöst worden, eine Willenseinigung zwischen der KG und der beklagten GmbH über die Übernahme von Vermögenswerten sei den erstgerichtlichen Feststellungen nicht zu entnehmen.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG` — partial — gold is substring of pred: `DKZ Solar GesmbH`
- `Sanitär Services GesmbH & Co KG` — positional overlap with gold: `Stadt-Sanitär Services GesmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Beinicke`(person)
- `Wentzlick`(person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich`(address)
- `DKZ Solar GesmbH`(organisation)
- `Schueßler`(person)
- `HochForschung GmbH`(organisation)
- `Stadt-Sanitär Services GesmbH`(organisation)

**Example 57** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_8`)


Nach den wesentlichen Feststellungen (US 3 bis 6) befand sich die See-Maschinenbau GmbH in der zweiten Jahreshälfte 2008 in erheblichen Zahlungsschwierigkeiten.

**False Positives:**

- `Maschinenbau GmbH` — partial — pred is substring of gold: `See-Maschinenbau GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `See-Maschinenbau GmbH`(organisation)

**Example 58** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_11`)


„Nachdem“ es für die Wilken E‑Commerce GmbH notwendig geworden war, für die Aufnahme des Rennbetriebs 35.000 Euro in das Fahrzeug zu investieren, konnte aufgrund dessen schlechten Zustands kein Rennen erfolgreich beendet werden.

**False Positives:**

- `Commerce GmbH` — partial — pred is substring of gold: `Wilken E‑Commerce GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wilken E‑Commerce GmbH`(organisation)

**Example 59** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_23`)


Auch diesen Aspekt nimmt die Staatsanwaltschaft in der Rechtsrüge (Z 9 lit a) ausreichend in den Blick, indem sie auf - in Richtung der Erfüllung auch der objektiven Tatbestandsmerkmale der §§ 146, 147 Abs 3 StGB weisende - Beweisergebnisse zum vorliegenden Vertragsab-schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH hinweist.

**False Positives:**

- `schluss trotz mangelnder finanzieller Ausstattung und Absicherung der Inn Dorfdersee GmbH` — partial — gold is substring of pred: `Inn Dorfdersee GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn Dorfdersee GmbH`(organisation)

**Example 60** (doc_id: `deanon_TRAIN/8ObA14_12k`) (sent_id: `deanon_TRAIN/8ObA14_12k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, den Hofrat Hon.-Prof. Dr. Kuras, die Hofrätin Dr. Tarmann-Prentner sowie die fachkundigen Laienrichter Dr. Josef Schleinzer und AR Angelika Neuhauser als weitere Richter in der Arbeitsrechtssache der klagenden Partei Linn Hüwelhans, vertreten durch Kosch & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Dertra-Daten GmbH, Techn R Prof.in Elina Lemmerth, vertreten durch Fellner Wratzfeld & Partner Rechtsanwälte GmbH in Wien, wegen Feststellung und Rechnungslegung (Streitwert 7.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 16. Dezember 2011, GZ 10 Ra 81/11x-21, mit dem das Teilurteil des Arbeits- und Sozialgerichts Wien vom 17. Dezember 2010, GZ 5 Cga 69/10t-17, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Daten GmbH` — partial — pred is substring of gold: `Dertra-Daten GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Linn Hüwelhans`(person)
- `Dertra-Daten GmbH`(organisation)
- `Techn R Prof.in Elina Lemmerth`(person)

**Example 61** (doc_id: `deanon_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_TRAIN/15Os66_19y_15Os67_19w__10`)


für die dadurch zugefügte Kränkung wurde die Antragsgegnerin UWFZ Telekom GmbH nach § 6 Abs 1 MedienG zur Zahlung einer Entschädigung sowie nach § 8a Abs 6 MedienG iVm § 34 Abs 1 MedienG zur Urteilsveröffentlichung verpflichtet.

**False Positives:**

- `für die dadurch zugefügte Kränkung wurde die Antragsgegnerin UWFZ Telekom GmbH` — partial — gold is substring of pred: `UWFZ Telekom GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UWFZ Telekom GmbH`(organisation)

**Example 62** (doc_id: `deanon_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_TRAIN/15Os66_19y_15Os67_19w__42`)


Voraussetzung für die geltend gemachte Haftung der Antragsgegnerin Pohlschmidt und Josef Digital GmbH nach § 6 Abs 1 MedienG ist, dass im Medium „Website“ (§ 1 Abs 1 Z 5a lit b MedienG) der objektive Tatbestand der üblen Nachrede hergestellt wurde.

**False Positives:**

- `Voraussetzung für die geltend gemachte Haftung der Antragsgegnerin Pohlschmidt und Josef Digital GmbH` — partial — gold is substring of pred: `Pohlschmidt und Josef Digital GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Pohlschmidt und Josef Digital GmbH`(organisation)

**Example 63** (doc_id: `deanon_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_TRAIN/15Os66_19y_15Os67_19w__62`)


Da sich diese Gesetzesverletzung nicht zum Nachteil der Antragsgegnerin Lexfen GmbH, der als Medieninhaberin die Rechte des Angeklagten zukommen (§ 41 Abs 6 zweiter Satz MedienG), auswirkt, kommt ein Vorgehen nach § 292 letzter Satz StPO nicht in Betracht und hat es mit der Feststellung des Gesetzesverstoßes sein Bewenden.

**False Positives:**

- `Da sich diese Gesetzesverletzung nicht zum Nachteil der Antragsgegnerin Lexfen GmbH` — partial — gold is substring of pred: `Lexfen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Lexfen GmbH`(organisation)

**Example 64** (doc_id: `deanon_TRAIN/1Ob19_15y`) (sent_id: `deanon_TRAIN/1Ob19_15y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in den verbundenen Rechtssachen der klagenden Partei Heimlexnex-Energie Aktiengesellschaft, Griepenkerlgasse 19, 3211 Hammerlmühlgegend, Österreich, vertreten durch Dr. Wilhelm Schlein Rechtsanwalt GmbH, Wien, gegen die beklagte Partei Pfistner & Oppert Maschinenbau GmbH, Adolf Halm, vertreten durch Eckert Fries Prokopp Rechtsanwälte GmbH, Baden, jeweils wegen Aufkündigung (58 C 547/11p und 58 C 153/12y), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 19. November 2014, GZ 38 R 120/14z-88, mit dem das Urteil des Bezirksgerichts Innere Stadt Wien vom 27. Februar 2014, GZ 58 C 547/11p-83, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Energie Aktiengesellschaft` — partial — pred is substring of gold: `Heimlexnex-Energie Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Heimlexnex-Energie Aktiengesellschaft`(organisation)
- `Griepenkerlgasse 19, 3211 Hammerlmühlgegend, Österreich`(address)
- `Pfistner & Oppert Maschinenbau GmbH`(organisation)
- `Adolf Halm`(person)

**Example 65** (doc_id: `deanon_TRAIN/6Ob145_21y`) (sent_id: `deanon_TRAIN/6Ob145_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden, den Hofrat Dr. Nowotny, die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Faber und den Hofrat Mag. Pertmayr als weitere Richter in der Rechtssache der gefährdeten Partei Dipl.-Ing. Kirstin Iseler, MA Bakk. rer. nat., vertreten durch DORDA Rechtsanwälte GmbH in Wien, wider die Gegnerin der gefährdeten Partei Wilfried Pawell, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, über den Rekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. Mai 2021, GZ 47 R 99/21p-19, womit aus Anlass des Rekurses der Gegnerin der gefährdeten Partei die einstweilige Verfügung des Bezirksgerichts Favoriten vom 3. April 2021, GZ 56 C 107/21m-2, als nichtig aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wirdFolge gegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dipl.-Ing. Kirstin Iseler, MA Bakk. rer. nat.`(person)
- `Wilfried Pawell`(person)

**Example 66** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_15`)


[4] Zu FN FN110230q ist im Firmenbuch des Handelsgerichts Wien die Seetra-Recycling GmbH (in der Folge „Bauvereinigung“) mit einem Stammkapital von 6.033.342,30 EUR eingetragen.

**False Positives:**

- `Recycling GmbH` — partial — pred is substring of gold: `Seetra-Recycling GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `FN110230q`(business_register_number)
- `Seetra-Recycling GmbH`(organisation)

**Example 67** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_29`)


diese sei eine gemeinnützige Bauvereinigung in der Rechtsform einer GmbH.

**False Positives:**

- `diese sei eine gemeinnützige Bauvereinigung in der Rechtsform einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_31`)


Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG wäre hinsichtlich § 14 Abs 3 FBG sachlich nicht gerechtfertigt.

**False Positives:**

- `Eine Unterscheidung zwischen der Rechtsform der Genossenschaft und jener der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_33`)


Diese Gesetzeslücke sei durch eine analoge Anwendung des § 14 Abs 3 FBG auf gemeinnützige Bauvereinigungen in sämtlichen möglichen Rechtsformen (also auch in der Rechtsform einer GmbH oder AG) anzuwenden.

**False Positives:**

- `also auch in der Rechtsform einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_66`)


Die Bestimmung sei daher analog auch auf gemeinnützige Bauvereinigungen in der Rechtsform der GmbH oder AG anzuwenden.

**False Positives:**

- `Die Bestimmung sei daher analog auch auf gemeinnützige Bauvereinigungen in der Rechtsform der GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_86`)


Auch bei Bauvereinigungen in der Rechtsform der Gesellschaft mit beschränkter Haftung oder der Aktiengesellschaft hat die Prüfung diesen Vorschriften zu entsprechen.

**False Positives:**

- `Auch bei Bauvereinigungen in der Rechtsform der Gesellschaft mit beschränkter Haftung oder der Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_107`)


Wenn nun kraft ausdrücklicher gesetzlicher Vorschrift gemeinnützige Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG erlaubt sind (§ 1 Abs 1 WGG) und gleichzeitig auch für diese die Pflicht statuiert wird, einem Revisionsverband anzugehören (§ 5 Abs 1 WGG), so ist auch für eine in der Rechtsform einer GmbH oder AG bestehende Bauvereinigung der Revisionsverband als „zuständig“ im Sinn von § 14 Abs 3 FBG und demgemäß insoweit als Amtspartei anzusehen.

**False Positives:**

- `Wenn nun kraft ausdrücklicher gesetzlicher Vorschrift gemeinnützige Bauvereinigungen auch in den Rechtsformen einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_111`)


Es muss daher davon ausgegangen werden, dass sowohl der Gesetzgeber des FBG als auch der mehrfache (Novellen-)Gesetzgeber des WGG die Zuständigkeit des Revisionsverbands für Bauvereinigungen in der Rechtsform einer GmbH oder AG übersehen hat.

**False Positives:**

- `Gesetzgeber des WGG die Zuständigkeit des Revisionsverbands für Bauvereinigungen in der Rechtsform einer GmbH oder AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie den Senatspräsidenten Dr. Veith, die Hofräte Hon.-Prof. Dr. Höllwerth, Hon.-Prof. PD Dr. Rassi und Mag. Painsi als weitere Richter in der Schiedsrechtssache der Antragstellerin (schiedsbeklagte Partei) See-Versand Werke GmbH, Robert Leis, gegen die Antragsgegnerin (schiedsklagende Partei) Dargatz+Boedewig Telekom GmbH, ÖkR Nikolaus Buksbaum, vertreten durch Dr. Horst Pechar, Rechtsanwalt in Weiz, wegen § 602 ZPO, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der an den Obersten Gerichtshof gerichtete Antrag vom 7. 1. 2021 wird, soweit er sich an den Obersten Gerichtshof richtet, zurückgewiesen.

**False Positives:**

- `Versand Werke GmbH` — partial — pred is substring of gold: `See-Versand Werke GmbH`
- `Boedewig Telekom GmbH` — partial — pred is substring of gold: `Dargatz+Boedewig Telekom GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `See-Versand Werke GmbH`(organisation)
- `Robert Leis`(person)
- `Dargatz+Boedewig Telekom GmbH`(organisation)
- `ÖkR Nikolaus Buksbaum`(person)

**Example 75** (doc_id: `deanon_TRAIN/1Ob173_11i`) (sent_id: `deanon_TRAIN/1Ob173_11i_14`)


Die Beklagte gewährte daraufhin der GmbH den gewünschten Überbrückungskredit.

**False Positives:**

- `Die Beklagte gewährte daraufhin der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/1Ob173_11i`) (sent_id: `deanon_TRAIN/1Ob173_11i_19`)


Von der wirtschaftlich schlechten Situation der GmbH hatte der Kläger erstmals wenige Tage vor der Konkurseröffnung erfahren.

**False Positives:**

- `Von der wirtschaftlich schlechten Situation der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/1Ob173_11i`) (sent_id: `deanon_TRAIN/1Ob173_11i_32`)


Dieser sei sich auch der wirtschaftlichen Lage der GmbH voll bewusst gewesen.

**False Positives:**

- `Dieser sei sich auch der wirtschaftlichen Lage der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_TRAIN/1Ob173_11i`) (sent_id: `deanon_TRAIN/1Ob173_11i_39`)


Die vom Kläger zu stellende Sicherheit sei für alle Beteiligten erkennbar stets dergestalt mit der Kreditierung der Beklagten an die GmbH verbunden gewesen, dass ohne Sicherheit der Kredit nicht eingeräumt und ohne Kreditierung die Sicherheit nicht erforderlich würde.

**False Positives:**

- `Die vom Kläger zu stellende Sicherheit sei für alle Beteiligten erkennbar stets dergestalt mit der Kreditierung der Beklagten an die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_TRAIN/9ObA1_24y`) (sent_id: `deanon_TRAIN/9ObA1_24y_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Mag. Ziegelbauer als Vorsitzenden, den Hofrat Dr. Hargassner und die Hofrätin Dr. Wallner-Friedl sowie die fachkundigen Laienrichter Helmut Purker (aus dem Kreis der Arbeitgeber) und Gerald Fida (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei ÖkR Wolf Nicolas, vertreten durch HAIDER | OBEREDER | PILZ Rechtsanwält:innen GmbH in Wien, gegen die beklagte Partei SXI Bildung Gruppe GmbH, StR Ada Kuipers, LLB, vertreten durch Mag. Filip Frank, Rechtsanwalt in Wien, wegen (zuletzt) 10.049,39 EUR brutto sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Oktober 2023, GZ 9 Ra 35/23t-38, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `innen GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `ÖkR Wolf Nicolas`(person)
- `SXI Bildung Gruppe GmbH`(organisation)
- `StR Ada Kuipers, LLB`(person)

**Example 80** (doc_id: `deanon_TRAIN/4Ob54_12p`) (sent_id: `deanon_TRAIN/4Ob54_12p_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel, Dr. Jensik, Dr. Musger und Dr. Schwarzenbacher als weitere Richter in der Rechtssache der klagenden Partei Rheinlaender&Horeischy Handel AG, Mag. Valerian Matyasek, vertreten durch Mag. Dr. Lothar Wiltschek und andere Rechtsanwälte in Wien, gegen die beklagte Partei Weipprecht Sicherheit Gesellschaft mbH, Reichhub 87, 4793 Kössldorf, Österreich, vertreten durch Mayer & Hermann Rechtsanwälte in Wien, wegen Unterlassung und Urteilsveröffentlichung (Streitwert im Sicherungsverfahren 60.000 EUR), über den außerordentlichen Revisionsrekurs der beklagten Partei gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 28. Februar 2012, GZ 1 R 292/11k-12, den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen (§ 528a iVm § 510 Abs 3 ZPO).

**False Positives:**

- `Horeischy Handel AG` — partial — pred is substring of gold: `Rheinlaender&Horeischy Handel AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Rheinlaender&Horeischy Handel AG`(organisation)
- `Mag. Valerian Matyasek`(person)
- `Weipprecht Sicherheit Gesellschaft mbH`(organisation)
- `Reichhub 87, 4793 Kössldorf, Österreich`(address)

**Example 81** (doc_id: `deanon_TRAIN/6Ob2_20t`) (sent_id: `deanon_TRAIN/6Ob2_20t_6`)


Da trotz entsprechenden Verbesserungsauftrags nicht alle Gesellschafter der GmbH ein Vermögensverzeichnis vorlegten, wurde der Verfahrenshilfeantrag abgewiesen.

**False Positives:**

- `Da trotz entsprechenden Verbesserungsauftrags nicht alle Gesellschafter der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_TRAIN/6Ob2_20t`) (sent_id: `deanon_TRAIN/6Ob2_20t_7`)


In der Folge zedierte die GmbH 2016 die Klagsforderungen an den 1996 geborenen vermögenslosen Kläger mit einem damaligen unselbstständigen monatlichen Bruttoeinkommen von 2.200 bis 2.300 EUR.

**False Positives:**

- `In der Folge zedierte die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_TRAIN/6Ob2_20t`) (sent_id: `deanon_TRAIN/6Ob2_20t_9`)


In weiterer Folge wurde ein Antrag auf Eröffnung eines Insolvenzverfahrens gegen die GmbH mangels kostendeckenden Vermögens abgewiesen.

**False Positives:**

- `In weiterer Folge wurde ein Antrag auf Eröffnung eines Insolvenzverfahrens gegen die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_TRAIN/6Ob2_20t`) (sent_id: `deanon_TRAIN/6Ob2_20t_22`)


Nach ständiger zweitinstanzlicher Judikatur gehören in aller Regel auch die Gesellschafter einer GmbH zu den wirtschaftlich Beteiligten (OLG Wien HS 15.063 = WR 33;

**False Positives:**

- `Nach ständiger zweitinstanzlicher Judikatur gehören in aller Regel auch die Gesellschafter einer GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_TRAIN/6Ob2_20t`) (sent_id: `deanon_TRAIN/6Ob2_20t_30`)


Diesfalls hätte die GmbH das Kostenrisiko des anzustrengenden Verfahrens nicht gehabt.

**False Positives:**

- `Diesfalls hätte die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_TRAIN/5Ob118_19t`) (sent_id: `deanon_TRAIN/5Ob118_19t_4`)


DI Meinrad Assfalk, vertreten durch Dr. Karl Klein, Rechtsanwalt in Wien, 3. Dr. Corinna Jensson, vertreten durch Dr. Bertram Broesigke, Rechtsanwalt in Wien, sowie die Nebenintervenientin auf Seiten der erstbeklagten Partei Kraftcondon-IT GmbH, Eduard Schlagdenhauffen, vertreten durch Nusterer & Mayer Rechtsanwälte OG in St. Pölten, wegen 242.451,30 EUR, Zahlung einer Rente (Streitwert 43.884 EUR) und Feststellung (Streitwert 10.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 27. Mai 2019, GZ 13 R 29/19h-61, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `IT GmbH` — partial — pred is substring of gold: `Kraftcondon-IT GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Meinrad Assfalk`(person)
- `Dr. Corinna Jensson`(person)
- `Kraftcondon-IT GmbH`(organisation)
- `Eduard Schlagdenhauffen`(person)

**Example 87** (doc_id: `deanon_TRAIN/8Nc21_10w`) (sent_id: `deanon_TRAIN/8Nc21_10w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Kuras und die Hofrätin Dr. Tarmann-Prentner als weitere Richter in der Rechtssache der klagenden Partei StadtEnergie Werke AG, Wilhelmine Hrncirik, vertreten durch Dr. Hartmut Ramsauer, Rechtsanwalt in Salzburg, gegen die beklagte Partei RgR Isabel Rövekamp, vertreten durch Frimmel/Anetter Rechtsanwaltsgesellschaft mbH in Klagenfurt am Wörthersee, wegen 4.696,20 EUR sA, über den Delegierungsantrag der beklagten Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag, an Stelle des Landesgerichts Salzburg als Arbeits- und Sozialgericht das Landesgericht Klagenfurt als Arbeits- und Sozialgericht zur Verhandlung und Entscheidung über die vorliegende Arbeitsrechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Prentner als weitere Richter in der Rechtssache der klagenden Partei StadtEnergie Werke AG` — partial — gold is substring of pred: `StadtEnergie Werke AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `StadtEnergie Werke AG`(organisation)
- `Wilhelmine Hrncirik`(person)
- `RgR Isabel Rövekamp`(person)

**Example 88** (doc_id: `deanon_TRAIN/8Ob19_24p`) (sent_id: `deanon_TRAIN/8Ob19_24p_13`)


Die Beklagte sei die Muttergesellschaft eines Fahrzeugkonzerns, dem auch die von der Beklagten als 100 %-Eigentümerin kontrollierte Mur Nexlog AG als Herstellerin des Klagsfahrzeugs angehöre.

**False Positives:**

- `Eigentümerin kontrollierte Mur Nexlog AG` — partial — gold is substring of pred: `Mur Nexlog AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mur Nexlog AG`(organisation)

**Example 89** (doc_id: `deanon_TRAIN/8Ob19_24p`) (sent_id: `deanon_TRAIN/8Ob19_24p_23`)


zudem sei allgemein bekannt, dass Fahrzeuge der Marke Nexkel-Transport nicht von der Beklagten, sondern von der Mur-Marine Vertrieb AG hergestellt würden.

**False Positives:**

- `Marine Vertrieb AG` — partial — pred is substring of gold: `Mur-Marine Vertrieb AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nexkel-Transport`(organisation)
- `Mur-Marine Vertrieb AG`(organisation)

</details>

---

## `Company Name Without Suffix`

**F1:** 0.056 | **Precision:** 0.067 | **Recall:** 0.048  

**Format:** `regex`  
**Rule ID:** `c8608e27`  
**Description:**
Matches company names that do not end in a standard suffix like GmbH/AG but are clearly organizations (e.g., 'Kilincarslan Metall'), ensuring the industry term is part of the match.

**Content:**
```
(?i)(?<![a-zäöüß\s])(?<!\w)([A-Z][a-zäöüß0-9]+(?:\s+[A-Z][a-zäöüß0-9]+)*(?:\s+&\s+[A-Z][a-zäöüß0-9]+)*)\s+(Metall|Maschinenbau|Luftfahrt|Forschung|Handel|Dienstleistungen|Verlag|Software|Cloud|Transport|Immobilien|Versicherung|Gastronomie|Medien|Planung|Bau|Energie|Automotive|Gesellschaft|Institut|Gruppe|Werke|Holding|Bank|Telekom|Post|Versand|Logistik|Touristik|Pharma|Sanitär|Getränke|Lebensmittel|Elekro|Elektronik|Druck|Medizin|Klinik|Spital|Krankenhaus|Schule|Universität|Hochschule|Firma|Unternehmen|Betrieb|Konzern|AG|GmbH|KG|OG|Limited|GesmbH|Aktiengesellschaft)(?=\s|,|\.|\(|\)|;|:|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.067 | 0.048 | 0.056 | 284 | 19 | 265 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 265 | 380 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_4`)


BergCloud GmbH, Polterauergasse 24, 5204 Neuhofen, Österreich, vertreten durch Singer Fössl, Rechtsanwälte OG in Wien, 2.

| Predicted | Gold |
|---|---|
| `BergCloud GmbH` | `BergCloud GmbH` |

**Missed by this rule (FN):**

- `Polterauergasse 24, 5204 Neuhofen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_5`)


West Berfenval GmbH, Hinterhagweg 6, 8591 Niedergößnitz, Österreich, vertreten durch Dr. Peter Mair, Rechtsanwalt in Bad Ischl, gegen die beklagten Parteien 1.

| Predicted | Gold |
|---|---|
| `West Berfenval GmbH` | `West Berfenval GmbH` |

**Missed by this rule (FN):**

- `Hinterhagweg 6, 8591 Niedergößnitz, Österreich` (address)

**Example 2** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_6`)


Waldzor Luftfahrt GmbH, Sonnenberger Straße 6, 9220 Velden am Wörther See, Österreich, vertreten durch Dr. Peter Lindinger und Dr. Andreas Pramer, Rechtsanwälte in Linz, 2.

| Predicted | Gold |
|---|---|
| `Waldzor Luftfahrt GmbH` | `Waldzor Luftfahrt GmbH` |

**Missed by this rule (FN):**

- `Sonnenberger Straße 6, 9220 Velden am Wörther See, Österreich` (address)

**Example 3** (doc_id: `deanon_TRAIN/1Ob213_15b`) (sent_id: `deanon_TRAIN/1Ob213_15b_4`)


MittelMedien Institut GmbH, Andreas Hofer-Zeile 1052, 3595 Brunn an der Wild, Österreich, vertreten durch Mag. Wolfgang Vinatzer, Rechtsanwalt in Wien, und 2. Kretzmar Pharma AG, St.-Elisabeth-Platz 6, 4775 Brunedt, Österreich, vertreten durch die Widter Mayrhauser Wolf Rechtsanwälte OG, Wien, wegen Gerichtserlags nach § 1425 ABGB, über den außerordentlichen Revisionsrekurs der Erstantragsgegnerin gegen den Beschluss des Oberlandesgerichts Wien als Rekursgericht vom 29. September 2015, GZ 12 R 91/15p-14, mit dem der Beschluss des Landesgerichts für Zivilrechtssachen Wien vom 27. Juli 2015, GZ 61 Nc 3/15y-9, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen.

| Predicted | Gold |
|---|---|
| `MittelMedien Institut GmbH` | `MittelMedien Institut GmbH` |

**Missed by this rule (FN):**

- `Andreas Hofer-Zeile 1052, 3595 Brunn an der Wild, Österreich` (address)
- `Kretzmar Pharma AG` (organisation)
- `St.-Elisabeth-Platz 6, 4775 Brunedt, Österreich` (address)

**Example 4** (doc_id: `deanon_TRAIN/8Ob4_18y`) (sent_id: `deanon_TRAIN/8Ob4_18y_4`)


Vossbrinck Wind AG, Flurnsbach 9, 4722 Untwüsten, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte GmbH in Wien, und 2. Steinheim-Cloud Limited, Anlauftalstraße 23, 4623 Kalchau, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.141,02 EUR, über die Revision der erstbeklagten Partei gegen das Teilurteil des Handelsgerichts Wien als Berufungsgericht vom 18. September 2017, GZ 60 R 20/17x-29, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 3. Jänner 2017, GZ 20 C 529/15p-24, in der Hauptsache hinsichtlich der erstbeklagten Partei bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Vossbrinck Wind AG` | `Vossbrinck Wind AG` |

**Missed by this rule (FN):**

- `Flurnsbach 9, 4722 Untwüsten, Österreich` (address)
- `Steinheim-Cloud Limited` (organisation)
- `Anlauftalstraße 23, 4623 Kalchau, Österreich` (address)

**Example 5** (doc_id: `deanon_TRAIN/7Ob11_22a`) (sent_id: `deanon_TRAIN/7Ob11_22a_6`)


IT Sudtraver GmbH, Wald-Marine, und 2. Tal Seewil GmbH, Grappaweg 1, 5310 Hof, Österreich, beide vertreten durch die DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Herausgabe und Feststellung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2021, GZ 4 R 149/21s-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `IT Sudtraver GmbH` | `IT Sudtraver GmbH` |

**Missed by this rule (FN):**

- `Wald-Marine` (organisation)
- `Tal Seewil GmbH` (organisation)
- `Grappaweg 1, 5310 Hof, Österreich` (address)

**Example 6** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_5`)


RheinPharma Services AG, Unterhillinglah 5, 9853 Dornbach, Österreich, vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, und 3.

| Predicted | Gold |
|---|---|
| `RheinPharma Services AG` | `RheinPharma Services AG` |

**Missed by this rule (FN):**

- `Unterhillinglah 5, 9853 Dornbach, Österreich` (address)

**Example 7** (doc_id: `deanon_TRAIN/2Ob85_11f`) (sent_id: `deanon_TRAIN/2Ob85_11f_6`)


Glöckler Daten AG, Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich, vertreten durch Dr. Walter Heel, Rechtsanwalt in Innsbruck, wegen 62.404,99 EUR sA und Feststellung (Streitinteresse: 10.000 EUR), über die Revisionen der klagenden, der erstbeklagten und der zweitbeklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Jänner 2011, GZ 4 R 250/10m-85, womit infolge der Berufungen der klagenden, der erstbeklagten und der zweitbeklagten Partei das Urteil des Landesgerichts Innsbruck vom 25. August 2010, GZ 5 Cg 160/08w-74, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Sämtliche Revisionen werden zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Glöckler Daten AG` | `Glöckler Daten AG` |

**Missed by this rule (FN):**

- `Arbeiterstrandbadstraße 492, 8680 Pernreit, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/7Ob203_24i`) (sent_id: `deanon_TRAIN/7Ob203_24i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Solé als Vorsitzende und die Hofrätinnen und Hofräte Mag. Dr. Wurdinger, Mag. Malesich, Dr. Weber und Mag. Fitz als weitere Richter in der Rechtssache der klagenden Partei PhD Lara Scharpwinkel, vertreten durch Mag. Martin Wabra, Rechtsanwalt in Gmünd, gegen die beklagte Partei Fenbach-IT AG, Linn Zemlik, vertreten durch die MUSEY rechtsanwalt gmbH in Salzburg, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 24. Oktober 2024, GZ 5 R 144/24v-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `IT AG` — partial — pred is substring of gold: `Fenbach-IT AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `PhD Lara Scharpwinkel`(person)
- `Fenbach-IT AG`(organisation)
- `Linn Zemlik`(person)

**Example 1** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_6`)


Text Entscheidungsgründe: Mit Bescheid vom 26. 4. 2010 lehnte die beklagte Partei den Antrag des Klägers auf Gewährung der Kostenerstattung für die Inanspruchnahme der Alpen-KI GmbH (im Folgenden kurz: GmbH) laut Rechnungen vom 2. 10. 2009 und 6. 11. 2009 in Höhe von insgesamt 540 EUR ab.

**False Positives:**

- `KI GmbH` — partial — pred is substring of gold: `Alpen-KI GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alpen-KI GmbH`(organisation)

**Example 2** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_9`)


Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH in Anspruch genommen und dafür insgesamt 540 EUR bezahlt.

**False Positives:**

- `Nach Erhalt von Bewilligungen der beklagten Partei für physikalische Behandlungen habe er entsprechende Leistungen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_13`)


Dem für die GmbH tätigen Team gehörten renommierte Fachärzte für medizinische Unfallchirurgie sowie Sportärzte an.

**False Positives:**

- `Dem für die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_30`)


Zwischen der GmbH und der beklagten Partei besteht kein Vertragsverhältnis.

**False Positives:**

- `Zwischen der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_31`)


Die GmbH verfügt auch über keine Bewilligung als Krankenanstalt bzw selbständiges Ambulatorium im Sinne des WrKAG und über keinen ärztlichen Leiter.

**False Positives:**

- `Die GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_33`)


Anhand dieser Vorgaben werden die von der GmbH entwickelten speziellen Trainingsmethoden angewandt.

**False Positives:**

- `Anhand dieser Vorgaben werden die von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_39`)


Der Geschäftsführer der GmbH ist diplomierter Sportlehrer.

**False Positives:**

- `Der Geschäftsführer der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_53`)


Das Institut sei daher nicht einer Hilfsperson gleichzuhalten, die nach den genauen Anordnungen des Arztes und unter seiner ständigen Aufsicht handle.

**False Positives:**

- `Das Institut` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_58`)


Die von der beklagten Partei erteilte Bewilligung habe sich nicht auf ein bestimmtes Institut bezogen, sondern nur auf eine bestimmte Therapie.

**False Positives:**

- `Die von der beklagten Partei erteilte Bewilligung habe sich nicht auf ein bestimmtes Institut` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_77`)


Das Institut verfüge über keinen ärztlichen Leiter; der Geschäftsführer jener Abteilung, in der der Kläger trainiert worden sei bzw der den Kläger auch selbst trainiert habe, sei diplomierter Sportlehrer und verfüge wie seine Mitarbeiter über keine medizinische Ausbildung.

**False Positives:**

- `Das Institut` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_83`)


Unbestrittenermaßen verfüge aber weder die Gesellschaft noch der das Training durchführende Geschäftsführer über eine Berufsberechtigung nach dem MTD-Gesetz.

**False Positives:**

- `Unbestrittenermaßen verfüge aber weder die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_84`)


Die Gesellschaft verfüge auch über keine Bewilligung als Krankenanstalt oder selbständiges Ambulatorium gemäß dem WrKAG.

**False Positives:**

- `Die Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_138`)


Obwohl das vom Kläger besuchte Institut unbestritten über keine Bewilligung als Krankenanstalt (§ 4 Abs 1 des Wiener Krankenanstaltengesetzes 1987 [WrKAG 1987]) verfügt und dessen Geschäftsführer, der das Training geleitet hat, nicht die gemäß § 7 des MTD-Gesetzes zur freiberuflichen Ausübung des physiotherapeutischen Dienstes bzw des ergotherapeutischen Dienstes notwendige Befugnis besitzt, möchte der Kläger dennoch einen Kostenersatz erreichen.

**False Positives:**

- `Obwohl das vom Kläger besuchte Institut` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_140`)


Handelt es sich bei den von der GmbH angebotenen Trainings um Leistungen anderer Gesundheitsberufe, die nicht in § 135 Abs 1 ASVG aufgelistet sind, ist eine Analogie ausgeschlossen (siehe oben Pkt 1.1.).

**False Positives:**

- `Handelt es sich bei den von der GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_148`)


Allein dass die in dem Institut angewandten Trainingspläne von Ärzten entwickelt wurden, kann nicht das Erfordernis substituieren, einen Arzt jederzeit und sofort zu erreichen und den Behandlungsvorgang unverzüglich an Veränderungen in der ärztlich verordneten Therapie anzupassen.

**False Positives:**

- `Allein dass die in dem Institut` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/4Ob23_24x`) (sent_id: `deanon_TRAIN/4Ob23_24x_6`)


Die Klägerin hat eine auf den Handel mit Medizinprodukten eingeschränkte Gewerbeberechtigung nach § 94 Z 33 GewO.

**False Positives:**

- `Die Klägerin hat eine auf den Handel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/4Ob23_24x`) (sent_id: `deanon_TRAIN/4Ob23_24x_13`)


Beides sei den Inhabern einer Gewerbeberechtigung für den Handel mit Medizinprodukten (§ 94 Z 33 GewO) vorbehalten.

**False Positives:**

- `Beides sei den Inhabern einer Gewerbeberechtigung für den Handel` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/4Ob244_18p`) (sent_id: `deanon_TRAIN/4Ob244_18p_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Wehrstedt Metall GmbH, Holger Heldwein, vertreten durch Dr. Franz Gütlbauer und andere Rechtsanwälte in Wels, gegen die beklagte Partei Ostwilzor-Metall gesellschaft mbH, Schilchergasse 5, 8230 Oberlungitz, Österreich, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH in Ried im Innkreis, wegen 44.635,70 EUR sA und Feststellung (Streitwert 8.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Oktober 2018, GZ 1 R 86/18z-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Wehrstedt Metall GmbH` — partial — gold is substring of pred: `Wehrstedt Metall GmbH`
- `Metall gesellschaft` — partial — pred is substring of gold: `Ostwilzor-Metall gesellschaft mbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Wehrstedt Metall GmbH`(organisation)
- `Holger Heldwein`(person)
- `Ostwilzor-Metall gesellschaft mbH`(organisation)
- `Schilchergasse 5, 8230 Oberlungitz, Österreich`(address)

**Example 19** (doc_id: `deanon_TRAIN/1Ob167_22y`) (sent_id: `deanon_TRAIN/1Ob167_22y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Musger als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Mag. Wessely-Kristöfel und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei Unitradon-Telekom GmbH, Leila Chatzifotiou, vertreten durch Mag. Dr. Maria Lisa Aidin, Rechtsanwältin in Salzburg, gegen die beklagte Partei Maurice Scheinert, vertreten durch Dr. Thomas Mondl, Rechtsanwalt in Wien, wegen Unterlassung (Streitwert 8.000 EUR), über den Rekurs der klagenden Partei gegen den Beschluss des Landesgerichts Leoben vom 25. Juli 2022, GZ 1 R 94/22y-48, mit dem der Rekurs gegen den Beschluss des Landesgerichts Leoben als Berufungsgericht vom 9. Mai 2022, GZ 1 R 94/22z-37, sowie Anträge auf „Ausspruch der Zulässigkeit des Revisionsrekurses“ und „Abänderung des Ausspruchs über die Zulässigkeit“ zurückgewiesen wurden, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Telekom GmbH` — partial — pred is substring of gold: `Unitradon-Telekom GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Unitradon-Telekom GmbH`(organisation)
- `Leila Chatzifotiou`(person)
- `Maurice Scheinert`(person)

**Example 20** (doc_id: `deanon_TRAIN/8ObS5_19x`) (sent_id: `deanon_TRAIN/8ObS5_19x_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Mag. Dr. Ingomar Stuper (aus dem Kreis der Arbeitgeber) und Günter Hintersteiner (aus dem Kreis der Arbeitnehmer) in der Sozialrechtssache der klagenden Partei Mag. Simon Ascioglu, gegen die beklagte Partei IEF-Service GmbH, Geschäftsstelle Graz, 8020 Graz, Europaplatz 12, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, wegen 19.146 EUR, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 11. April 2019, GZ 7 Rs 81/18p-13, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Service GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Simon Ascioglu`(person)

**Example 21** (doc_id: `deanon_TRAIN/8ObS5_19x`) (sent_id: `deanon_TRAIN/8ObS5_19x_28`)


Ob und unter welchen Voraussetzungen eine Generalvollmacht einem Bevollmächtigten dennoch beherrschenden Einfluss auf eine Gesellschaft im Sinne des § 1 Abs 6 Z 2 IESG vermitteln könnte, braucht im vorliegenden Fall nicht geklärt zu werden.

**False Positives:**

- `Ob und unter welchen Voraussetzungen eine Generalvollmacht einem Bevollmächtigten dennoch beherrschenden Einfluss auf eine Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/8ObS5_19x`) (sent_id: `deanon_TRAIN/8ObS5_19x_29`)


Die Vollmacht des Klägers (im Innenverhältnis) war auf die Vertretung der Inn-Energie GmbH beim Abschluss eines Beteiligungsvertrags mit einer bestimmten Investorin in der Generalversammlung am 1. 2. 2018, als der Kläger selbst noch gar nicht Minderheitsgesellschafter der Kleinkurt Sicherheit GmbH war, beschränkt.

**False Positives:**

- `Energie GmbH` — partial — pred is substring of gold: `Inn-Energie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Inn-Energie GmbH`(organisation)
- `Kleinkurt Sicherheit GmbH`(organisation)

**Example 23** (doc_id: `deanon_TRAIN/4Ob31_22w`) (sent_id: `deanon_TRAIN/4Ob31_22w_4`)


Matzka sowie die Hofrätin Mag. Istjan, LL.M., als weitere Richter in der Rechtssache der klagenden Partei UTZ Textil Betriebe GmbH, Vincent Clasen, vertreten durch Mag. Lukas Leszkovics, LL.M., Rechtsanwalt in Wien, gegen die beklagte Partei Kelsyn-Metall GmbH, Barbara Nüssler, vertreten durch Mag. Oliver Simoncic, Rechtsanwalt in St. Pölten, wegen 772.775,54 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 13. Jänner 2022, GZ 5 R 126/21t-72, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Metall GmbH` — partial — pred is substring of gold: `Kelsyn-Metall GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `UTZ Textil Betriebe GmbH`(organisation)
- `Vincent Clasen`(person)
- `Kelsyn-Metall GmbH`(organisation)
- `Barbara Nüssler`(person)

**Example 24** (doc_id: `deanon_TRAIN/6Ob210_22h`) (sent_id: `deanon_TRAIN/6Ob210_22h_26`)


Die wechselseitige Regulierung der Dienstleistungen ist somit in Österreich im Gewerberecht verortet.

**False Positives:**

- `Die wechselseitige Regulierung der Dienstleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/8Ob59_12b`) (sent_id: `deanon_TRAIN/8Ob59_12b_15`)


Daraufhin wurden diese Arbeiten von einem dritten Unternehmen ausgeführt.

**False Positives:**

- `Daraufhin wurden diese Arbeiten von einem dritten Unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_7`)


TraunChemie GmbH & Co KG, Badeteich Bisamberg 16, 4625 Kronberg, Österreich, vertreten durch Siemer-Siegl-Füreder & Partner, Rechtsanwälte OG in Wien, wegen 59.104,03 EUR sA, über die außerordentlichen Revisionsrekurse der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 2. Mai 2011, GZ 2 R 182/10p-50, womit über Rekurs der klagenden Partei der Beschluss des Landesgerichts Steyr vom 23. August 2010, GZ 4 Cg 154/08t-34, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentlichen Revisionsrekurse werden gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `TraunChemie GmbH & Co KG` — partial — gold is substring of pred: `TraunChemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunChemie GmbH`(organisation)
- `Badeteich Bisamberg 16, 4625 Kronberg, Österreich`(address)

**Example 27** (doc_id: `deanon_TRAIN/10Ob15_16b`) (sent_id: `deanon_TRAIN/10Ob15_16b_35`)


Ohne konkrete Anhaltspunkte sind solche Schritte vom Gericht nicht zu unternehmen (10 Ob 67/11t;NeumayrinSchwimann/Kodek, ABGB4§ 11 UVG Rz 10 ff).

**False Positives:**

- `Ohne konkrete Anhaltspunkte sind solche Schritte vom Gericht nicht zu unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/1Ob213_15b`) (sent_id: `deanon_TRAIN/1Ob213_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Erlagssache der Antragstellerin Versicherung Tristein GmbH, Admont 97, 4701 Müllerberg, Österreich, vertreten durch Dr. Markus Andréewitch und andere Rechtsanwälte in Wien, gegen die Antragsgegner 1.

**False Positives:**

- `Rennhofer als weitere Richter in der Erlagssache der Antragstellerin Versicherung Tristein GmbH` — partial — gold is substring of pred: `Versicherung Tristein GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Versicherung Tristein GmbH`(organisation)
- `Admont 97, 4701 Müllerberg, Österreich`(address)

**Example 29** (doc_id: `deanon_TRAIN/5Ob200_24h`) (sent_id: `deanon_TRAIN/5Ob200_24h_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Mag. Wurzer als Vorsitzenden sowie die Hofrätinnen und Hofräte Mag. Painsi, Dr. Weixelbraun-Mohr, Dr. Steger und Dr. Pfurtscheller als weitere Richter in der Rechtssache der klagenden Partei Ing. Harald Josepeit, vertreten durch die Wutte-Lang Rechtsanwalts GmbH in Klagenfurt, und der Nebenintervenientin auf Seiten der klagenden Partei MMag.

**False Positives:**

- `Lang Rechtsanwalts GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ing. Harald Josepeit`(person)

**Example 30** (doc_id: `deanon_TRAIN/1Ob119_19k`) (sent_id: `deanon_TRAIN/1Ob119_19k_12`)


Es sei auch kein Schaden in Höhe der für die vermittelte Versicherung zu bezahlenden (Gesamt-)Prämien entstanden, sondern nur insoweit, als Prämienanteile auf die doppelt versicherten Gegenstände entfallen.

**False Positives:**

- `Es sei auch kein Schaden in Höhe der für die vermittelte Versicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/3Ob248_19w`) (sent_id: `deanon_TRAIN/3Ob248_19w_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Hofrat Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Rechtssache der klagenden Partei Leikauf Daten AG, Mag.a Erna Leitgen, vertreten durch Widter Mayrhauser Wolf Rechtsanwälte OG in Wien, gegen die beklagten Parteien 1. Marine Furtlog GmbH, 2. Dipl.-Ing. Viola Schöndube, beide vertreten durch Mag. Wolfgang Vinatzer, Rechtsanwalt in Wien, wegen 1.241.906,55 EUR sA, über die außerordentliche Revision der beklagten Parteien gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Oktober 2019, GZ 1 R 126/19k-31, den Beschluss gefasst:  Spruch I.Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Kristöfel als weitere Richter in der Rechtssache der klagenden Partei Leikauf Daten AG` — partial — gold is substring of pred: `Leikauf Daten AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Leikauf Daten AG`(organisation)
- `Mag.a Erna Leitgen`(person)
- `Marine Furtlog GmbH`(organisation)
- `Dipl.-Ing. Viola Schöndube`(person)

**Example 32** (doc_id: `deanon_TRAIN/3Ob248_19w`) (sent_id: `deanon_TRAIN/3Ob248_19w_9`)


Sie reklamieren vorvertragliche Aufklärungspflichten der klagenden Bank im Zusammenhang mit der Kreditgewährung zur (vorläufigen) Aufrechterhaltung des Geschäftsbetriebs der Erstbeklagten während der Anhängigkeit eines Gerichtsverfahrens auf Zahlung einer hohen Werklohnforderung aus dem Umstand, dass die Klägerin damals an jener Gesellschaft, der gegenüber die Erstbeklagte diese – der Klägerin zur Besicherung der Kreditforderung verpfändete – Forderung geltend machte, ganz geringfügig (zu rund 0,6 %) beteiligt war.

**False Positives:**

- `Sie reklamieren vorvertragliche Aufklärungspflichten der klagenden Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/7Ob150_17k`) (sent_id: `deanon_TRAIN/7Ob150_17k_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Getränke Uniallog AG, Elisabeth Ehredt, vertreten durch Themmer, Toth & Partner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Zorsudfen Handel GmbH, Lena Stumbra, vertreten durch Dr. Alexander Katholnig, MBL, Rechtsanwalt in Kitzbühel, wegen 8.037,65 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Innsbruck als Berufungsgericht vom 14. Juni 2017, GZ 77 R 57/17y-20, mit dem das Urteil des Bezirksgerichts Kitzbühel vom 2. März 2017, GZ 2 C 834/16a-16, abgeändert wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Getränke Uniallog AG` — partial — gold is substring of pred: `Getränke Uniallog AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Getränke Uniallog AG`(organisation)
- `Elisabeth Ehredt`(person)
- `Zorsudfen Handel GmbH`(organisation)
- `Lena Stumbra`(person)

**Example 34** (doc_id: `deanon_TRAIN/10Ob106_18p`) (sent_id: `deanon_TRAIN/10Ob106_18p_47`)


Dass das Unternehmen nach Ablauf der in den Klauseln aufgestellten Fristen leistungsfrei werde, entbehre einer sachlichen Rechtfertigung.

**False Positives:**

- `Dass das Unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/10Ob106_18p`) (sent_id: `deanon_TRAIN/10Ob106_18p_91`)


Die mit den Gutscheinen vermittelten Waren oder Dienstleistungen hätten regelmäßig einen wesentlich höheren Wert als der Kunde im Gegenzug für den Gutschein bezahle.

**False Positives:**

- `Die mit den Gutscheinen vermittelten Waren oder Dienstleistungen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_TRAIN/18OCg4_20t`) (sent_id: `deanon_TRAIN/18OCg4_20t_5`)


Die Beklagte ist eine Aktiengesellschaft mit Sitz in Italien.

**False Positives:**

- `Die Beklagte ist eine Aktiengesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_TRAIN/4Ob59_17f`) (sent_id: `deanon_TRAIN/4Ob59_17f_4`)


Matzka als weitere Richter in der Rechtssache der Klägerin Alpen Logkel GmbH, Dorrekstraße 17, 4812 Großkufhaus, Österreich, vertreten durch Knoflach, Kroker, Tonini & Partner, Rechtsanwälte in Innsbruck, gegen die Beklagte Pavlovic und Robbertz Technik Gesellschaft mbH, Krenntal 7, 9470 Loschental, Österreich, vertreten durch Dr. Bernd Roßkothen, Rechtsanwalt in Salzburg, wegen Unterlassung (Streitwert im Sicherungsverfahren 43.200 EUR), über den außerordentlichen Revisionsrekurs der Beklagten gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 13. Februar 2017, GZ 4 R 14/17g-17, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der außerordentliche Revisionsrekurs wird gemäß §§ 78, 402 Abs 4 EO iVm § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der Klägerin Alpen Logkel GmbH` — partial — gold is substring of pred: `Alpen Logkel GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Alpen Logkel GmbH`(organisation)
- `Dorrekstraße 17, 4812 Großkufhaus, Österreich`(address)
- `Pavlovic und Robbertz Technik Gesellschaft mbH`(organisation)
- `Krenntal 7, 9470 Loschental, Österreich`(address)

**Example 38** (doc_id: `deanon_TRAIN/1Ob30_13p`) (sent_id: `deanon_TRAIN/1Ob30_13p_21`)


Liegen die erforderlichen behördlichen Genehmigungen zur Errichtung und zum Betrieb einer Tankanlage vor, ist aber ein Mitverschulden ihres Eigentümers/Betreibers in der Regel zu verneinen (RIS-Justiz RS0088981 [T2]).

**False Positives:**

- `Liegen die erforderlichen behördlichen Genehmigungen zur Errichtung und zum Betrieb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_29`)


Selbst im Fall einer Unionsrechtswidrigkeit des Glücksspielmonopols könnte weder der Beklagte noch die slowakische Betreiberin aufgrund des verbleibenden nationalen Regelungstorsos eine Konzession zur Durchführung von Ausspielungen oder eine Bewilligung zum Betrieb von Spielautomaten erhalten (Nichteinhaltung der Mindestkapitalvorschriften).

**False Positives:**

- `Selbst im Fall einer Unionsrechtswidrigkeit des Glücksspielmonopols könnte weder der Beklagte noch die slowakische Betreiberin aufgrund des verbleibenden nationalen Regelungstorsos eine Konzession zur Durchführung von Ausspielungen oder eine Bewilligung zum Betrieb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/1Ob131_16w`) (sent_id: `deanon_TRAIN/1Ob131_16w_8`)


Die Auswahl der Schule für ein Kind sei eine wichtige Angelegenheit, die die gemeinsam obsorgeberechtigten Eltern im Sinne des § 137 Abs 2 ABGB tunlichst einvernehmlich wahrzunehmen hätten.

**False Positives:**

- `Die Auswahl der Schule` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/1Ob131_16w`) (sent_id: `deanon_TRAIN/1Ob131_16w_10`)


Die einvernehmlich erfolgte Auswahl der Schule durch die gemeinsam obsorgeberechtigten Eltern und die damit zusammenhängende Vereinbarung über die Tragung der Schulkosten könne nicht einseitig widerrufen werden.

**False Positives:**

- `Die einvernehmlich erfolgte Auswahl der Schule` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/9ObA141_19d`) (sent_id: `deanon_TRAIN/9ObA141_19d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshof Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Peter Zeitler (aus dem Kreis der Arbeitnehmer) und Angela Taschek (aus dem Kreis der Arbeitgeber) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Adelheid Haaf, LLB, vertreten durch Dr. Thomas Krankl, Rechtsanwalt in Wien, gegen die beklagte Partei Nossack Analyse AG, Sascha Steinke, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 1.397.481,32 EUR netto sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. Oktober 2019, GZ 9 Ra 14/19y-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Adelheid Haaf, LLB`(person)
- `Nossack Analyse AG`(organisation)
- `Sascha Steinke`(person)

**Example 43** (doc_id: `deanon_TRAIN/17Os34_15a`) (sent_id: `deanon_TRAIN/17Os34_15a_59`)


Zur Gänze bedingte Nachsicht kam mit Blick auf die in den zur Last liegenden Taten zum Ausdruck kommende erhebliche kriminelle Energie aus spezial- und generalpräventiven Gründen nicht in Betracht.

**False Positives:**

- `Zur Gänze bedingte Nachsicht kam mit Blick auf die in den zur Last liegenden Taten zum Ausdruck kommende erhebliche kriminelle Energie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/6Ob180_12g`) (sent_id: `deanon_TRAIN/6Ob180_12g_5`)


Bestätigt die Zweitbank das unwiderrufliche Akkreditiv aufgrund einer Ermächtigung oder eines Auftrags der eröffnenden Bank, so begründet dies grundsätzlich die eigene Haftung der Bestätigungsbank.

**False Positives:**

- `Bestätigt die Zweitbank das unwiderrufliche Akkreditiv aufgrund einer Ermächtigung oder eines Auftrags der eröffnenden Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_TRAIN/6Ob180_12g`) (sent_id: `deanon_TRAIN/6Ob180_12g_28`)


Zwar hat die Bank, wenn sie vor Honorierung des Akkreditivs von anderer Seite als vom angeblichen Aussteller erfährt, dass ein Akkreditivdokument gefälscht sein soll, einem Fälschungsverdacht nachzugehen (ApathyinApathy/Iro/Koziol, Österreichisches Bankvertragsrecht2V Rz 1/124 f).

**False Positives:**

- `Zwar hat die Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_TRAIN/6Ob23_18b`) (sent_id: `deanon_TRAIN/6Ob23_18b_25`)


Die gegenständliche Sammelklage wird von einer Prozessfinanzierungs AG (gegen ein Entgelt von 20 % des Erlöses) und mit PR-Unterstützung einer Agentur betrieben.

**False Positives:**

- `Die gegenständliche Sammelklage wird von einer Prozessfinanzierungs AG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/7Ob143_19h`) (sent_id: `deanon_TRAIN/7Ob143_19h_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Donau Furttalsyn GmbH, Hugo Fasters, vertreten durch Urbanek & Rudolph Rechtsanwälte OG in Wien, gegen die beklagte Partei Mentele Touristik AG, Friedrich Klingfuss, vertreten durch Handler Rechtsanwalt GmbH in Deutschlandsberg, wegen 55.505,74 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Juni 2019, GZ 1 R 65/19i-43, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Matzka als weitere Richter in der Rechtssache der klagenden Partei Donau Furttalsyn GmbH` — partial — gold is substring of pred: `Donau Furttalsyn GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Donau Furttalsyn GmbH`(organisation)
- `Hugo Fasters`(person)
- `Mentele Touristik AG`(organisation)
- `Friedrich Klingfuss`(person)

**Example 48** (doc_id: `deanon_TRAIN/8ObS6_23z`) (sent_id: `deanon_TRAIN/8ObS6_23z_8`)


Der Kläger war bei der mittlerweile insolventen Allember-Wind GmbH als Lkw-Fahrer beschäftigt und erlitt am 9.

**False Positives:**

- `Wind GmbH` — partial — pred is substring of gold: `Allember-Wind GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Allember-Wind GmbH`(organisation)

**Example 49** (doc_id: `deanon_TRAIN/8Ob4_18y`) (sent_id: `deanon_TRAIN/8Ob4_18y_4`)


Vossbrinck Wind AG, Flurnsbach 9, 4722 Untwüsten, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte GmbH in Wien, und 2. Steinheim-Cloud Limited, Anlauftalstraße 23, 4623 Kalchau, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.141,02 EUR, über die Revision der erstbeklagten Partei gegen das Teilurteil des Handelsgerichts Wien als Berufungsgericht vom 18. September 2017, GZ 60 R 20/17x-29, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 3. Jänner 2017, GZ 20 C 529/15p-24, in der Hauptsache hinsichtlich der erstbeklagten Partei bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Cloud Limited` — partial — pred is substring of gold: `Steinheim-Cloud Limited`
- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Vossbrinck Wind AG`(organisation)
- `Flurnsbach 9, 4722 Untwüsten, Österreich`(address)
- `Steinheim-Cloud Limited`(organisation)
- `Anlauftalstraße 23, 4623 Kalchau, Österreich`(address)

**Example 50** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michael Puhm (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Hermine Thom, vertreten durch Dr. Markus Orgler, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Mur Brucktridon AG, Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat., vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 4.200,83 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 17. Oktober 2019, GZ 13 Ra 41/15z-30, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hermine Thom`(person)
- `Mur Brucktridon AG`(organisation)
- `Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat.`(person)

**Example 51** (doc_id: `deanon_TRAIN/1Ob48_24a`) (sent_id: `deanon_TRAIN/1Ob48_24a_34`)


Sein spanisches Unternehmen beabsichtige, mit dem Verkaufserlös wiederum eine Liegenschaft anzukaufen, zu entwickeln, zwischenzeitlich zu vermieten und mit Gewinn zu veräußern.

**False Positives:**

- `Sein spanisches Unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_TRAIN/1Ob48_24a`) (sent_id: `deanon_TRAIN/1Ob48_24a_56`)


Die Veräußerung der Liegenschaft durch das vom Mann beherrschte spanische Unternehmen sei für den Ausgleichsanspruch nicht relevant.

**False Positives:**

- `Die Veräußerung der Liegenschaft durch das vom Mann beherrschte spanische Unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_TRAIN/1Ob48_24a`) (sent_id: `deanon_TRAIN/1Ob48_24a_58`)


Dass sein spanisches Unternehmen aus betriebswirtschaftlichen Gründen gezwungen gewesen wäre, die Liegenschaft (und nicht etwa die andere) zu veräußern, behaupte er nicht.

**False Positives:**

- `Dass sein spanisches Unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_TRAIN/7Ob60_18a`) (sent_id: `deanon_TRAIN/7Ob60_18a_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Dr. Ariadne Kieble, vertreten durch Dr. Josef Sailer, Rechtsanwalt in Bruck an der Leitha, gegen die beklagte Partei Seeglanz-Umwelt AG, Volkmar Heinbichner, LLB Bakk. iur., vertreten durch Mag. Wolfgang Weilguni, Rechtsanwalt in Wien, wegen Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 25. Jänner 2018, GZ 1 R 127/17d-15, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Umwelt AG` — partial — pred is substring of gold: `Seeglanz-Umwelt AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Dr. Ariadne Kieble`(person)
- `Seeglanz-Umwelt AG`(organisation)
- `Volkmar Heinbichner, LLB Bakk. iur.`(person)

**Example 55** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_8`)


B./II./ am 13. November 2009 in Poysdorf als Zeugin in einem Ermittlungsverfahren nach der Strafprozessordnung vor der Kriminalpolizei bei ihrer förmlichen Vernehmung zur Sache falsch ausgesagt, indem sie wahrheitswidrig behauptete, die an sie bezahlten 22.800 Euro seien das Entgelt für LKW-Vermietungen an die Ost Lextal GmbH gewesen, wobei sie tatsächlich das Geld ausbezahlt bekam, ohne dafür an die genannte Gesellschaft eine Gegenleistung erbracht zu haben.

**False Positives:**

- `Vermietungen an die Ost Lextal GmbH` — partial — gold is substring of pred: `Ost Lextal GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Ost Lextal GmbH`(organisation)

**Example 56** (doc_id: `deanon_TRAIN/7Ob126_09v`) (sent_id: `deanon_TRAIN/7Ob126_09v_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei MAYK Garten GmbH, Bartholomäus Iffläender, BA, vertreten durch Dr. Gerhard Mitterböck, Rechtsanwalt in Wien, gegen die beklagte Partei Schneiderlin+Balles Transport GmbH, Carla Havlikova, vertreten durch Walch & Zehetbauer Rechtsanwälte OEG in Wien, wegen 14.018,90 EUR, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 16. Februar 2009, GZ 4 R 210/08v-49, mit dem infolge Berufung der beklagten Partei das Urteil des Landes- als Handelsgerichts Korneuburg vom 22. Juli 2008, GZ 4 Cg 135/07d-39, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch Der Revision wird nicht Folge gegeben.

**False Positives:**

- `Balles Transport GmbH` — partial — pred is substring of gold: `Schneiderlin+Balles Transport GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `MAYK Garten GmbH`(organisation)
- `Bartholomäus Iffläender, BA`(person)
- `Schneiderlin+Balles Transport GmbH`(organisation)
- `Carla Havlikova`(person)

**Example 57** (doc_id: `deanon_TRAIN/7Ob126_09v`) (sent_id: `deanon_TRAIN/7Ob126_09v_28`)


Ein etwa zwei Wochen davor von der Beklagten auftrags der Klägerin durchgeführter Transport von drei baugleichen und ebenso verpackten Schaltschränken verlief schadenfrei.

**False Positives:**

- `Ein etwa zwei Wochen davor von der Beklagten auftrags der Klägerin durchgeführter Transport` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/7Ob126_09v`) (sent_id: `deanon_TRAIN/7Ob126_09v_52`)


Der Transport einer sichtbar unzureichend verpackten und falsch verladenen kopflastigen Maschine sei grob fahrlässig.

**False Positives:**

- `Der Transport` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_TRAIN/7Ob126_09v`) (sent_id: `deanon_TRAIN/7Ob126_09v_118`)


Wegen der hohen Kippgefahr bei ungesichertem Transport ohne Veränderung der Verpackung war der Eintritt des vorliegenden Schadens angesichts der bei einem ordnungsgemäßen Transport üblicherweise zu erwartenden äußeren Einwirkungen (insbesonders durch die Fliehkraft) auch nicht nur für möglich zu halten, sondern mit hoher Wahrscheinlichkeit zu erwarten.

**False Positives:**

- `Wegen der hohen Kippgefahr bei ungesichertem Transport ohne Veränderung der Verpackung war der Eintritt des vorliegenden Schadens angesichts der bei einem ordnungsgemäßen Transport` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/7Ob48_15g`) (sent_id: `deanon_TRAIN/7Ob48_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Raphael Pabstmann, vertreten durch Dr. Herbert Laimböck, Rechtsanwalt in Wien, gegen die beklagte Partei Altunkaynak&Teifel Analyse AG, Arabella Frommke, vertreten durch Dr. Herbert Salficky, Rechtsanwalt in Wien, wegen 29.769,46 EUR sA und Feststellung, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 28. Jänner 2015, GZ 1 R 193/14f-53, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Teifel Analyse AG` — partial — pred is substring of gold: `Altunkaynak&Teifel Analyse AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Raphael Pabstmann`(person)
- `Altunkaynak&Teifel Analyse AG`(organisation)
- `Arabella Frommke`(person)

**Example 61** (doc_id: `deanon_TRAIN/7Ob48_15g`) (sent_id: `deanon_TRAIN/7Ob48_15g_12`)


Nichts anderes gilt für die vorliegenden Besonderen Bedingungen für die Versicherung von Wohn- und Bürogebäuden, Fassung 2007, der Beklagten.

**False Positives:**

- `Nichts anderes gilt für die vorliegenden Besonderen Bedingungen für die Versicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_TRAIN/3Ob203_19b`) (sent_id: `deanon_TRAIN/3Ob203_19b_3`)


Kopf Der Oberste Gerichtshof hat durch den Hofrat des Obersten Gerichtshofs Dr. Roch als Vorsitzenden sowie den Hofrat Priv.-Doz. Dr. Rassi und die Hofrätinnen Dr. Weixelbraun-Mohr, Dr. Kodek und Mag. Wessely-Kristöfel als weitere Richter in der Rechtssache der klagenden Partei Samir Golabek, vertreten durch Mag. Barbara Loipetsberger, Rechtsanwältin in Vöcklabruck, gegen die beklagte Partei Norsud-Energie AG, Knut Petschock, vertreten durch Mag. Jürgen Lappi, Rechtsanwalt in Vöcklabruck, wegen Unzulässigerklärung einer Exekution (§ 35 EO), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Landesgerichts Wels als Berufungsgericht vom 3. Juli 2019, GZ 22 R 172/19d-22, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Energie AG` — partial — pred is substring of gold: `Norsud-Energie AG`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Samir Golabek`(person)
- `Norsud-Energie AG`(organisation)
- `Knut Petschock`(person)

**Example 63** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 64** (doc_id: `deanon_TRAIN/10Ob47_18m`) (sent_id: `deanon_TRAIN/10Ob47_18m_6`)


Der Geschäftsführer der klagenden Gesellschaft und seine Lebensgefährtin kauften im Februar 2012 bei der Beklagten ein dunkelrotes Ledersofa.

**False Positives:**

- `Der Geschäftsführer der klagenden Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_TRAIN/4Ob24_20p`) (sent_id: `deanon_TRAIN/4Ob24_20p_5`)


Nord-Sanitär GmbH, Kraftkel-Event, 2. Dickmänken+Schaunsland Heizung GmbH, F.-Kogler-Weg 18, 4084 Sattlberg, Österreich, beide vertreten durch Partnerschaft SCHUPPICH SPORN & WINISCHHOFER Rechtsanwälte in Wien, gegen die beklagte Partei Hinterholzner Recycling GmbH, KzlR Egon Litvine, BSc, vertreten durch PISTOTNIK & KRILYSZYN Rechtsanwälte in Wien, und die Nebenintervenientin auf Seiten der beklagten Partei Wien Furtseetra GmbH, Arnold Wöbbe, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen zuletzt 4.264.783,18 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. November 2019, GZ 129 R 91/19d-367, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Sanitär GmbH` — partial — pred is substring of gold: `Nord-Sanitär GmbH`
- `Schaunsland Heizung GmbH` — partial — pred is substring of gold: `Dickmänken+Schaunsland Heizung GmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Nord-Sanitär GmbH`(organisation)
- `Kraftkel-Event`(organisation)
- `Dickmänken+Schaunsland Heizung GmbH`(organisation)
- `F.-Kogler-Weg 18, 4084 Sattlberg, Österreich`(address)
- `Hinterholzner Recycling GmbH`(organisation)
- `KzlR Egon Litvine, BSc`(person)
- `Wien Furtseetra GmbH`(organisation)
- `Arnold Wöbbe`(person)

**Example 66** (doc_id: `deanon_TRAIN/9ObA49_23f`) (sent_id: `deanon_TRAIN/9ObA49_23f_10`)


Der Oberste Gerichtshof hat zur Auslegung der auch hier verfahrensgegenständlichen Regelungen des Pensionskassenmodells des Kollektivvertrags für das Bordpersonal der DCR Druck und Jeremias Langnes, BA („OS-KV Bord“) bereits in der Entscheidung 8 ObA 58/16m Stellung genommen.

**False Positives:**

- `Der Oberste Gerichtshof hat zur Auslegung der auch hier verfahrensgegenständlichen Regelungen des Pensionskassenmodells des Kollektivvertrags für das Bordpersonal der DCR Druck` — partial — gold is substring of pred: `DCR Druck`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DCR Druck`(organisation)
- `Jeremias Langnes, BA`(person)

**Example 67** (doc_id: `deanon_TRAIN/4Ob64_18t`) (sent_id: `deanon_TRAIN/4Ob64_18t_8`)


Eine Bank, die Effektengeschäfte ausführt, haftet im Allgemeinen nicht für die mangelhafte Beratung ihrer Kunden durch ein von diesen beigezogenes („kundennäheres“) Wertpapierdienstleistungsunternehmen.

**False Positives:**

- `Eine Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/4Ob64_18t`) (sent_id: `deanon_TRAIN/4Ob64_18t_10`)


Eine grundsätzlich dem Anleger gegenüber bestehende selbstständige Beratungspflicht der Bank ist Voraussetzung für die (und nicht Folge der) Zurechnung eines selbstständigen Beraters (vgl RIS-Justiz RS0128476 [T13]).

**False Positives:**

- `Eine grundsätzlich dem Anleger gegenüber bestehende selbstständige Beratungspflicht der Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/4Ob64_18t`) (sent_id: `deanon_TRAIN/4Ob64_18t_11`)


Eine Effektengeschäfte ausführende Bank hat daher nach § 1313a ABGB für die mangelhafte Beratung eines Beraters einzustehen, wenn dieser in ihrem Pflichtenkreis tätig wird und sie sich zur Erfüllung ihrer Pflichten gegenüber dem Kunden eines Beraters bedient, der derart in ihre Interessenverfolgung eingebunden ist, dass es an einem legitimen Vertrauen auf eine objektive Beratung durch einen Dritten fehlt (vgl RIS-Justiz RS0128476 [insb T3, T13, T15]).

**False Positives:**

- `Eine Effektengeschäfte ausführende Bank` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/10Ob13_22t`) (sent_id: `deanon_TRAIN/10Ob13_22t_6`)


Die Klägerin beauftragte die Beklagte mit der Planung und Lieferung einer aus mehreren Komponenten bestehenden Nasskiesaufbereitungsanlage um insgesamt 550.000 EUR.

**False Positives:**

- `Die Klägerin beauftragte die Beklagte mit der Planung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_TRAIN/10Ob13_22t`) (sent_id: `deanon_TRAIN/10Ob13_22t_8`)


[…] Der Kunde ist im Falle der Geltendmachung von Gewährleistungsansprüchen verpflichtet, Mur-Textil Gruppe zur Verbesserung eine Frist von zumindest sechs Wochen ab der Übergabe des/der Geräte bzw. dem Beginn der Mängelbehebung vor Ort einzuräumen.

**False Positives:**

- `Textil Gruppe` — partial — pred is substring of gold: `Mur-Textil Gruppe`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mur-Textil Gruppe`(organisation)

**Example 72** (doc_id: `deanon_TRAIN/10Ob13_22t`) (sent_id: `deanon_TRAIN/10Ob13_22t_22`)


Ihr Anspruch auf Ersatz der durch die mangelhafte Planung und Montage der Anlage durch die Beklagte entstandenen „Kostenüberschreitungen“ bzw „nachträglichen Investitionen“ und des entgangenen Gewinns sowie auf Rückersatz von bezahlten, tatsächlich aber nicht erbrachten Planungsleistungen werde durch die AVB daher nicht tangiert.

**False Positives:**

- `Ihr Anspruch auf Ersatz der durch die mangelhafte Planung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_TRAIN/7Ob11_22a`) (sent_id: `deanon_TRAIN/7Ob11_22a_6`)


IT Sudtraver GmbH, Wald-Marine, und 2. Tal Seewil GmbH, Grappaweg 1, 5310 Hof, Österreich, beide vertreten durch die DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Herausgabe und Feststellung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2021, GZ 4 R 149/21s-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Tessbach Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `IT Sudtraver GmbH`(organisation)
- `Wald-Marine`(organisation)
- `Tal Seewil GmbH`(organisation)
- `Grappaweg 1, 5310 Hof, Österreich`(address)

**Example 74** (doc_id: `deanon_TRAIN/7Ob65_15g`) (sent_id: `deanon_TRAIN/7Ob65_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Hofrätin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Nortri-Umwelt GmbH & Co KG, Piberberg 8, 4720 Unternfurth, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in Salzburg, gegen die beklagte Partei Anton Adil Versicherungs-Aktiengesellschaft, Am Kastanienhof 90, 6162 Mutters, Österreich, vertreten durch Dr. Johannes Kirschner, Rechtsanwalt in Wels, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 19. Jänner 2015, GZ 1 R 198/14i-14, womit das Urteil des Landesgerichts Wels vom 29. September 2014, GZ 2 Cg 65/14g-10, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Umwelt GmbH & Co KG` — positional overlap with gold: `Nortri-Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nortri-Umwelt GmbH`(organisation)
- `Piberberg 8, 4720 Unternfurth, Österreich`(address)
- `Anton Adil`(person)
- `Am Kastanienhof 90, 6162 Mutters, Österreich`(address)

**Example 75** (doc_id: `deanon_TRAIN/7Ob65_15g`) (sent_id: `deanon_TRAIN/7Ob65_15g_15`)


Unter die Versicherung gemäß Art. 1 AHVB fallen insbesondere nicht 1.1 Ansprüche aus Gewährleistung für Mängel und/oder Ansprüche wegen Schäden, die an den vom Versicherungsnehmer (oder in seinem Auftrag oder für seine Rechnung von Dritten) hergestellten oder gelieferten Arbeiten oder Sachen, auch infolge einer in der Herstellung, Lieferung oder Montage liegenden Ursache entstehen;

**False Positives:**

- `Unter die Versicherung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/5Ob202_09f`) (sent_id: `deanon_TRAIN/5Ob202_09f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Danzl als Vorsitzenden sowie die Hofrätinnen/Hofräte des Obersten Gerichtshofs Dr. Hurch, Dr. Lovrek, Dr. Höllwerth und Dr. Tarmann-Prentner als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Kadzimirsz Sicherheit GmbH, Rottenmannerstraße 19, 3231 Wieden, Österreich, vertreten durch Dr. Karl Grigkar, Rechtsanwalt in Wien, wider den Antragsgegner Herbert Dietmaier, vertreten durch Hule Bachmayr-Heyda Nordberg Rechtsanwälte GmbH in Wien, wegen § 12a iVm § 46 Abs 2 MRG, über den Revisionsrekurs der Antragstellerin gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. Mai 2009, GZ 39 R 2/09z-17, womit infolge Rekurses der Antragstellerin der Sachbeschluss des Bezirksgerichts Innere Stadt Wien vom 27. Oktober 2008, GZ 48 Msch 9/08v-11, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Prentner als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Kadzimirsz Sicherheit GmbH` — partial — gold is substring of pred: `Kadzimirsz Sicherheit GmbH`
- `Heyda Nordberg Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 1  |  likely missing annotation: 1

**Gold Entities:**

- `Kadzimirsz Sicherheit GmbH`(organisation)
- `Rottenmannerstraße 19, 3231 Wieden, Österreich`(address)
- `Herbert Dietmaier`(person)

**Example 77** (doc_id: `deanon_TRAIN/5Ob202_09f`) (sent_id: `deanon_TRAIN/5Ob202_09f_16`)


Liege eine solche bindende Entscheidung vor und werde das Unternehmen innerhalb der Jahresfrist veräußert, könne der Vermieter den Hauptmietzins nur bis zu der vom Gericht bzw der Gemeinde festgesetzten Höhe anheben.

**False Positives:**

- `Liege eine solche bindende Entscheidung vor und werde das Unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_TRAIN/5Ob202_09f`) (sent_id: `deanon_TRAIN/5Ob202_09f_21`)


Veräußert der Hauptmieter einer Geschäftsräumlichkeit das von ihm im Mietgegenstand betriebene Unternehmen zur Fortführung in diesen Räumen, so tritt nach § 12a Abs 1 MRG der Erwerber des Unternehmens anstelle des bisherigen Hauptmieters in das Hauptmietverhältnis ein.

**False Positives:**

- `Veräußert der Hauptmieter einer Geschäftsräumlichkeit das von ihm im Mietgegenstand betriebene Unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_TRAIN/10Nc38_19y`) (sent_id: `deanon_TRAIN/10Nc38_19y_27`)


Bei der Beklagten handle es sich um ein Unternehmen mit Sitz in der Türkei, ihr allgemeiner Gerichtsstand sei daher in der Türkei.

**False Positives:**

- `Bei der Beklagten handle es sich um ein Unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_TRAIN/4Ob26_15z`) (sent_id: `deanon_TRAIN/4Ob26_15z_4`)


Beate Feuchte GmbH, Untere Öfnerstraße 36, 2852 Burgerschlag, Österreich, 2. Etzelsdorf 10, 5232 Wendling, Österreich, 3. Selker 4, 4134 Pernersdorf, Österreich, 4. Dr. Janis Böckenkämper, Italien, 5. Keberlein+Kubank Telekom AG, Karl Heinschild-Weg 3, 8273 Ebersdorf, Österreich, Italien, alle vertreten durch Dr. Harald Burmann und andere Rechtsanwälte in Innsbruck, wegen 213.977,45 EUR sA (erstbeklagte Partei) und Kosten (zweit- bis fünftbeklagte Parteien), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 18. Dezember 2014, GZ 2 R 199/14b-130, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Beate Feuchte GmbH` — partial — gold is substring of pred: `Beate Feuchte`
- `Kubank Telekom AG` — partial — pred is substring of gold: `Keberlein+Kubank Telekom AG`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Beate Feuchte`(person)
- `Untere Öfnerstraße 36, 2852 Burgerschlag, Österreich`(address)
- `Etzelsdorf 10, 5232 Wendling, Österreich`(address)
- `Selker 4, 4134 Pernersdorf, Österreich`(address)
- `Dr. Janis Böckenkämper`(person)
- `Keberlein+Kubank Telekom AG`(organisation)
- `Karl Heinschild-Weg 3, 8273 Ebersdorf, Österreich`(address)

**Example 81** (doc_id: `deanon_TRAIN/4Ob26_15z`) (sent_id: `deanon_TRAIN/4Ob26_15z_15`)


3. In der von den Vorinstanzen ihrer Schadensberechnung nach § 273 ZPO zugrundeliegenden Methode, den Deckungsbeitrag des halben Umsatzes der Valwald-Finanzen GmbH mit den Kunden der klagenden Partei („gemeinsame Kunden“) heranzuziehen, ist jedenfalls keine krasse Ermessensüberschreitung zu erblicken, die einer höchstgerichtlichen Korrektur bedarf.

**False Positives:**

- `Finanzen GmbH` — partial — pred is substring of gold: `Valwald-Finanzen GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Valwald-Finanzen GmbH`(organisation)

**Example 82** (doc_id: `deanon_TRAIN/10Ob46_19s`) (sent_id: `deanon_TRAIN/10Ob46_19s_17`)


Das Geschäftslokal sei ausdrücklich zum Betrieb einer Vinothek angemietet worden.

**False Positives:**

- `Das Geschäftslokal sei ausdrücklich zum Betrieb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_TRAIN/10Ob46_19s`) (sent_id: `deanon_TRAIN/10Ob46_19s_18`)


Im dazu von der Klägerin angestrengten Betriebsanlagengenehmigungs-verfahren habe der Beklagte Einwendungen gegen die für den Betrieb der Vinothek erforderliche Genehmigung erhoben.

**False Positives:**

- `verfahren habe der Beklagte Einwendungen gegen die für den Betrieb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_TRAIN/10Ob46_19s`) (sent_id: `deanon_TRAIN/10Ob46_19s_38`)


Der Betrieb einer Gastronomie hätte eine Änderung des Mietvertrags bedeutet.

**False Positives:**

- `Der Betrieb einer Gastronomie` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_TRAIN/10Ob46_19s`) (sent_id: `deanon_TRAIN/10Ob46_19s_39`)


Danach sei lediglich der Betrieb einer Vinothek vereinbart gewesen, wogegen sich der Beklagte nicht ausgesprochen habe.

**False Positives:**

- `Danach sei lediglich der Betrieb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_TRAIN/9Ob67_09g`) (sent_id: `deanon_TRAIN/9Ob67_09g_5`)


Babette Wienkemeier, 3. HR Dario Litwinowa, 4. Eigenbrod Versicherung GmbH & Co KG, Dr. Franz Stumpf-Straße 48, 2002 Ottendorf, Österreich, 5. Dr. David Alswede, 6. Dipl.-Ing. Manuela Himmel, vertreten durch die Gassauer-Fleissner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Ing. Felizia Tscherning, vertreten durch Mag. Markus Adam, Rechtsanwalt in Wien, wegen Räumung (Streitwert 8.954,16 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 16. Juni 2009, GZ 41 R 98/09d-12, womit das Urteil des Bezirksgerichts Innere Stadt Wien vom 26. Februar 2009, GZ 30 C 200/08y-7, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Fleissner Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Babette Wienkemeier`(person)
- `HR Dario Litwinowa`(person)
- `Eigenbrod Versicherung GmbH`(organisation)
- `Dr. Franz Stumpf-Straße 48, 2002 Ottendorf, Österreich`(address)
- `Dr. David Alswede`(person)
- `Dipl.-Ing. Manuela Himmel`(person)
- `Ing. Felizia Tscherning`(person)

**Example 87** (doc_id: `deanon_TRAIN/8ObA10_12x`) (sent_id: `deanon_TRAIN/8ObA10_12x_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Kuras und Mag. Ziegelbauer sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Manuela Majeranowski als weitere Richter in der Arbeitsrechtssache der klagenden Partei Priv.-Doz.in HR OSR Larissa Abbate, vertreten durch Hasch & Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Bachbach-Marine Gesellschaft mbH, Floreweg 8, 9103 Bösenort, Österreich, vertreten durch Mag. Klaus F. Lughofer LLM, Rechtsanwalt in Linz, wegen Feststellung (Streitwert: 30.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. November 2011, GZ 11 Ra 92/11w-10, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 31. August 2011, GZ 11 Cga 101/11d-5, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Marine Gesellschaft` — partial — pred is substring of gold: `Bachbach-Marine Gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in HR OSR Larissa Abbate`(person)
- `Bachbach-Marine Gesellschaft mbH`(organisation)
- `Floreweg 8, 9103 Bösenort, Österreich`(address)

**Example 88** (doc_id: `deanon_TRAIN/8ObA10_12x`) (sent_id: `deanon_TRAIN/8ObA10_12x_55`)


Hat ein Unternehmen - wie hier die Beklagte - mehrere Betriebsstätten, so kann Dienstort des Angestellten im Sinn des KV nur das Tätigkeits- bzw Gemeindegebiet betreffend jene Betriebsstätte(n) sein, in der/denen der Angestellte vereinbarungsgemäß seine Arbeitstätigkeit erbringt.

**False Positives:**

- `Hat ein Unternehmen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ulm Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Janet Henken`(person)
- `Elvira Nossal`(person)

**Example 90** (doc_id: `deanon_TRAIN/3Ob170_20a`) (sent_id: `deanon_TRAIN/3Ob170_20a_7`)


Das Rekursgericht ließ den Revisionsrekurs zur Frage zu, ob zugewartet werden müsse, bis der selbständig erwerbstätige (an einer GmbH beteiligte und als Abwickler einer anderen Gesellschaft tätige) Antragsgegner das Wirtschaftsjahr 2017 „abschließt“, oder ob sein Einkommen anhand der letzten drei Wirtschaftsjahre ermittelt werden könne.

**False Positives:**

- `an einer GmbH beteiligte und als Abwickler einer anderen Gesellschaft` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_TRAIN/3Ob92_12v`) (sent_id: `deanon_TRAIN/3Ob92_12v_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie durch den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Joachim Dammann, MBA, als Masseverwalter im Konkurs über das Vermögen der Furtheimheim-Getränke GmbH, Trefferweg 4, 4632 Franzing, Österreich, wider die beklagte Partei „ EBK Umwelt Solutions “-***** GmbH, Andreas-Hofer-Gasse 70, 4310 Marbach, Österreich, vertreten durch Dr. Hubert Simon, Rechtsanwalt in Wien, wegen 16.877,09 EUR sA, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht vom 26. Jänner 2012, GZ 2 R 266/11v-14, womit infolge Berufung der klagenden Partei das Urteil des Handelsgerichts Wien vom 14. Oktober 2011, GZ 43 Cg 35/11m-10, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Getränke GmbH` — partial — pred is substring of gold: `Furtheimheim-Getränke GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Joachim Dammann, MBA`(person)
- `Furtheimheim-Getränke GmbH`(organisation)
- `Trefferweg 4, 4632 Franzing, Österreich`(address)
- `EBK Umwelt Solutions`(organisation)
- `Andreas-Hofer-Gasse 70, 4310 Marbach, Österreich`(address)

**Example 92** (doc_id: `deanon_TRAIN/9Ob31_22g`) (sent_id: `deanon_TRAIN/9Ob31_22g_20`)


Der Betrieb eines Take-away bzw ein Lieferservice seien nicht Geschäftsgegenstand einer Gastwirtschaft bzw eines Restaurants.

**False Positives:**

- `Der Betrieb` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_TRAIN/1Ob79_17z`) (sent_id: `deanon_TRAIN/1Ob79_17z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Scherg und Kintzli Holz GmbH, Ramon Reynert, vertreten durch die Saxinger Chalupsky & Partner Rechtsanwälte GmbH, Linz, gegen die beklagte Partei Wagenlöhner Versand GmbH, Maurice Schwoob, vertreten durch die Schneider Rechtsanwalts KG, Wien, wegen 6.239,26 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 30. September 2016, GZ 21 R 125/16d-26, mit dem das Urteil des Bezirksgerichts Hollabrunn vom 14. April 2016, GZ 1 C 335/15k-20, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt und beschlossen:  Spruch

**False Positives:**

- `Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Scherg und Kintzli Holz GmbH` — partial — gold is substring of pred: `Scherg und Kintzli Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Scherg und Kintzli Holz GmbH`(organisation)
- `Ramon Reynert`(person)
- `Wagenlöhner Versand GmbH`(organisation)
- `Maurice Schwoob`(person)

</details>

---

## `Hyphenated Company Names`

**F1:** 0.010 | **Precision:** 0.400 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `5fc6cd92`  
**Description:**
Specifically targets hyphenated company names that might be split by the generic rule, ensuring the full hyphenated name is captured.

**Content:**
```
(?i)(?<![a-zäöüß\s])(?<!\w)([A-Z][a-zäöüß0-9]+\-[A-Z][a-zäöüß0-9]+(?:\s+[A-Z][a-zäöüß0-9]+)*(?:\s+&\s+[A-Z][a-zäöüß0-9]+)*\s+(?:GmbH|AG|KG|OG|GesmbH|Aktiengesellschaft|Limited))(?=\s|,|\.|\(|\)|;|:|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.400 | 0.005 | 0.010 | 5 | 2 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 3 | 374 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/4Ob24_20p`) (sent_id: `deanon_TRAIN/4Ob24_20p_5`)


Nord-Sanitär GmbH, Kraftkel-Event, 2. Dickmänken+Schaunsland Heizung GmbH, F.-Kogler-Weg 18, 4084 Sattlberg, Österreich, beide vertreten durch Partnerschaft SCHUPPICH SPORN & WINISCHHOFER Rechtsanwälte in Wien, gegen die beklagte Partei Hinterholzner Recycling GmbH, KzlR Egon Litvine, BSc, vertreten durch PISTOTNIK & KRILYSZYN Rechtsanwälte in Wien, und die Nebenintervenientin auf Seiten der beklagten Partei Wien Furtseetra GmbH, Arnold Wöbbe, vertreten durch Mag. Dr. Dirk Just, Rechtsanwalt in Wien, wegen zuletzt 4.264.783,18 EUR sA, über die außerordentliche Revision der beklagten Partei gegen das Teilurteil des Oberlandesgerichts Wien als Berufungsgericht vom 29. November 2019, GZ 129 R 91/19d-367, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Nord-Sanitär GmbH` | `Nord-Sanitär GmbH` |

**Missed by this rule (FN):**

- `Kraftkel-Event` (organisation)
- `Dickmänken+Schaunsland Heizung GmbH` (organisation)
- `F.-Kogler-Weg 18, 4084 Sattlberg, Österreich` (address)
- `Hinterholzner Recycling GmbH` (organisation)
- `KzlR Egon Litvine, BSc` (person)
- `Wien Furtseetra GmbH` (organisation)
- `Arnold Wöbbe` (person)

**Example 1** (doc_id: `deanon_TRAIN/2Ob116_20b`) (sent_id: `deanon_TRAIN/2Ob116_20b_4`)


Bruckgart-Daten GmbH, Paulina Kleisz, vertreten durch Rudeck-Schlager Rechtsanwalts KG in Wien, 2.

| Predicted | Gold |
|---|---|
| `Bruckgart-Daten GmbH` | `Bruckgart-Daten GmbH` |

**Missed by this rule (FN):**

- `Paulina Kleisz` (person)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob213_15b`) (sent_id: `deanon_TRAIN/1Ob213_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Erlagssache der Antragstellerin Versicherung Tristein GmbH, Admont 97, 4701 Müllerberg, Österreich, vertreten durch Dr. Markus Andréewitch und andere Rechtsanwälte in Wien, gegen die Antragsgegner 1.

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Erlagssache der Antragstellerin Versicherung Tristein GmbH` — partial — gold is substring of pred: `Versicherung Tristein GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Versicherung Tristein GmbH`(organisation)
- `Admont 97, 4701 Müllerberg, Österreich`(address)

**Example 1** (doc_id: `deanon_TRAIN/1Ob140_14s`) (sent_id: `deanon_TRAIN/1Ob140_14s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer und Mag. Dr. Wurdinger sowie die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft, Meidlinger Hauptstraße 19, 5233 Erlach, Österreich, vertreten durch die Walch & Zehetbauer Rechtsanwälte OG, Wien, gegen die beklagte Partei Republik Österreich, vertreten durch die Finanzprokuratur in Wien, wegen 344.011,19 EUR und Feststellung (Streitwert 50.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Teilurteil des Oberlandesgerichts Innsbruck als Berufungsgericht vom 10. Juni 2014, GZ 4 R 202/13g-54, mit dem das Teilzwischenurteil des Landesgerichts Feldkirch vom 2. August 2013, GZ 8 Cg 143/11y-46, teilweise bestätigt und teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird zurückgewiesen.

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Tracondon Aktiengesellschaft` — partial — gold is substring of pred: `Tracondon Aktiengesellschaft`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Tracondon Aktiengesellschaft`(organisation)
- `Meidlinger Hauptstraße 19, 5233 Erlach, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/1Ob79_17z`) (sent_id: `deanon_TRAIN/1Ob79_17z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Hon.-Prof. Dr. Sailer als Vorsitzenden sowie die Hofräte Univ.-Prof. Dr. Bydlinski, Mag. Wurzer, Mag. Dr. Wurdinger und die Hofrätin Dr. Hofer-Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Scherg und Kintzli Holz GmbH, Ramon Reynert, vertreten durch die Saxinger Chalupsky & Partner Rechtsanwälte GmbH, Linz, gegen die beklagte Partei Wagenlöhner Versand GmbH, Maurice Schwoob, vertreten durch die Schneider Rechtsanwalts KG, Wien, wegen 6.239,26 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Landesgerichts Korneuburg als Berufungsgericht vom 30. September 2016, GZ 21 R 125/16d-26, mit dem das Urteil des Bezirksgerichts Hollabrunn vom 14. April 2016, GZ 1 C 335/15k-20, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt und beschlossen:  Spruch

**False Positives:**

- `Zeni-Rennhofer als weitere Richter in der Rechtssache der klagenden Partei Scherg und Kintzli Holz GmbH` — partial — gold is substring of pred: `Scherg und Kintzli Holz GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Scherg und Kintzli Holz GmbH`(organisation)
- `Ramon Reynert`(person)
- `Wagenlöhner Versand GmbH`(organisation)
- `Maurice Schwoob`(person)

</details>

---

## `Gesellschaft mbH Pattern`

**F1:** 0.010 | **Precision:** 0.250 | **Recall:** 0.005  

**Format:** `regex`  
**Rule ID:** `220b9f20`  
**Description:**
Matches entities ending in 'gesellschaft mbH' or 'Gesellschaft mbH' which are common in German legal texts, ensuring the full phrase is captured.

**Content:**
```
(?i)(?<![a-zäöüß\s])(?<!\w)([A-Z][a-zäöüß0-9]*(?:\s+[A-Z][a-zäöüß0-9]*)*(?:\s+&\s+[A-Z][a-zäöüß0-9]*)*\s+gesellschaft\s+mbH)(?=\s|,|\.|\(|\)|;|:|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.250 | 0.005 | 0.010 | 8 | 2 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 6 | 392 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob1_18w`) (sent_id: `deanon_TRAIN/3Ob1_18w_4`)


RheinPlanung gesellschaft mbH, Maulpertschstraße 55, 5145 Kammerleiten, Österreich, 2. Buddéus + Röslhuber Medien -gesellschaft mbH, Hochkoglweg 229x, 4081 Knieparz unter der Leithen, Österreich, 3.

| Predicted | Gold |
|---|---|
| `RheinPlanung gesellschaft mbH` | `RheinPlanung gesellschaft mbH` |

**Missed by this rule (FN):**

- `Maulpertschstraße 55, 5145 Kammerleiten, Österreich` (address)
- `Buddéus + Röslhuber Medien` (organisation)
- `Hochkoglweg 229x, 4081 Knieparz unter der Leithen, Österreich` (address)

**Example 1** (doc_id: `deanon_TRAIN/3Ob1_18w`) (sent_id: `deanon_TRAIN/3Ob1_18w_5`)


Doncon gesellschaft mbH, Rosenthalerstraße 1, 4595 Großmengersdorf, Österreich, alle vertreten durch Dr. Nikolaus Kraft, Rechtsanwalt in Wien, wegen Unzulässigkeitserklärung einer Exekution (§ 36 EO), über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 19. September 2017, GZ 47 R 281/17x-41, womit das Urteil des Bezirksgerichts Meidling vom 20. Juni 2016, GZ 5 C 1/15w-37, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Doncon gesellschaft mbH` | `Doncon gesellschaft mbH` |

**Missed by this rule (FN):**

- `Rosenthalerstraße 1, 4595 Großmengersdorf, Österreich` (address)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/4Ob244_18p`) (sent_id: `deanon_TRAIN/4Ob244_18p_4`)


Matzka als weitere Richter in der Rechtssache der klagenden Partei Wehrstedt Metall GmbH, Holger Heldwein, vertreten durch Dr. Franz Gütlbauer und andere Rechtsanwälte in Wels, gegen die beklagte Partei Ostwilzor-Metall gesellschaft mbH, Schilchergasse 5, 8230 Oberlungitz, Österreich, vertreten durch die Puttinger Vogl Rechtsanwälte GmbH in Ried im Innkreis, wegen 44.635,70 EUR sA und Feststellung (Streitwert 8.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 23. Oktober 2018, GZ 1 R 86/18z-49, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Metall gesellschaft mbH` — partial — pred is substring of gold: `Ostwilzor-Metall gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wehrstedt Metall GmbH`(organisation)
- `Holger Heldwein`(person)
- `Ostwilzor-Metall gesellschaft mbH`(organisation)
- `Schilchergasse 5, 8230 Oberlungitz, Österreich`(address)

**Example 1** (doc_id: `deanon_TRAIN/8ObA10_12x`) (sent_id: `deanon_TRAIN/8ObA10_12x_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Kuras und Mag. Ziegelbauer sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Manuela Majeranowski als weitere Richter in der Arbeitsrechtssache der klagenden Partei Priv.-Doz.in HR OSR Larissa Abbate, vertreten durch Hasch & Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Bachbach-Marine Gesellschaft mbH, Floreweg 8, 9103 Bösenort, Österreich, vertreten durch Mag. Klaus F. Lughofer LLM, Rechtsanwalt in Linz, wegen Feststellung (Streitwert: 30.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. November 2011, GZ 11 Ra 92/11w-10, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 31. August 2011, GZ 11 Cga 101/11d-5, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Marine Gesellschaft mbH` — partial — pred is substring of gold: `Bachbach-Marine Gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Priv.-Doz.in HR OSR Larissa Abbate`(person)
- `Bachbach-Marine Gesellschaft mbH`(organisation)
- `Floreweg 8, 9103 Bösenort, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/8Ob96_12v`) (sent_id: `deanon_TRAIN/8Ob96_12v_4`)


Rechtsanwälte Gesellschaft mbH in Wien, wegen Räumung und Unterlassung, über die außerordentlichen Revisionen der klagenden und der beklagten Partei gegen das Urteil des Landesgerichts Wiener Neustadt als Berufungsgericht vom 28. Juni 2012, GZ 18 R 48/12f-63, den Beschluss gefasst:  Spruch Die außerordentlichen Revisionen der klagenden und der beklagten Partei werden gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen (§ 510 Abs 3 ZPO).

**False Positives:**

- `Rechtsanwälte Gesellschaft mbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/9ObA96_13b`) (sent_id: `deanon_TRAIN/9ObA96_13b_4`)


Brigitte Augustin und Mag. Andreas Hach als weitere Richter in der Arbeitsrechtssache der klagenden Partei DI Anita Crämer, vertreten durch Dr. Gerhard Hiebler und Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei, GQG E‑Commerce Gesellschaft mbH, Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich, vertreten durch Siemer-Siegel-Füreder & Partner, Rechtsanwälte in Wien, wegen Feststellung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. April 2013, GZ 6 Ra 18/13h-10, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 7. November 2012, GZ 23 Cga 115/12x-6, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Commerce Gesellschaft mbH` — partial — pred is substring of gold: `GQG E‑Commerce Gesellschaft mbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `DI Anita Crämer`(person)
- `GQG E‑Commerce Gesellschaft mbH`(organisation)
- `Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/3Ob182_11b`) (sent_id: `deanon_TRAIN/3Ob182_11b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Dr. Prückner als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Neumayr, die Hofrätin Dr. Lovrek und die Hofräte Dr. Jensik und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Nord Seederfurt gesellschaft mbH, Kaiser Franz Joseph-Ring 259, 2602 Schönau an der Triesting, Österreich, vertreten durch Dr. Maximilian Gumpoldsberger, Rechtsanwalt in Wels, und der Nebenintervenientin auf Seiten der klagenden Partei Wald-Technik Gesellschaft mbH, Hussenreith 78, 8152 Michlbach, Österreich, vertreten durch Dr. Lydia Friedle, Rechtsanwältin in Mannersdorf am Leithagebirge, gegen die beklagte Partei Bratherig u. Wilibald Medien GmbH, Marceline Girtner, vertreten durch Dr. Franz Gütlbauer, Dr. Siegfried Sieghartsleitner und Dr. Michael Pichlmair, Rechtsanwälte in Wels, sowie der Nebenintervenientin auf Seiten der beklagten Partei Condorffurt-Landwirtschaft Gesellschaft mbH, Obermarkersdorf 29, 4775 Jechtenham, Österreich, vertreten durch Mag. Thomas Braun, Rechtsanwalt in Wien, wegen restlich 52.596,75 EUR sA, infolge Revision der klagenden Partei gegen das Endurteil des Oberlandesgerichts Linz als Berufungsgericht vom 4. Juli 2011, GZ 4 R 108/11x-47, womit infolge Berufung der klagenden Partei das Endurteil des Landesgerichts Wels vom 14. März 2011, GZ 6 Cg 17/09w-42, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Technik Gesellschaft mbH` — partial — pred is substring of gold: `Wald-Technik Gesellschaft mbH`
- `Landwirtschaft Gesellschaft mbH` — partial — pred is substring of gold: `Condorffurt-Landwirtschaft Gesellschaft mbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Nord Seederfurt gesellschaft mbH`(organisation)
- `Kaiser Franz Joseph-Ring 259, 2602 Schönau an der Triesting, Österreich`(address)
- `Wald-Technik Gesellschaft mbH`(organisation)
- `Hussenreith 78, 8152 Michlbach, Österreich`(address)
- `Bratherig u. Wilibald Medien GmbH`(organisation)
- `Marceline Girtner`(person)
- `Condorffurt-Landwirtschaft Gesellschaft mbH`(organisation)
- `Obermarkersdorf 29, 4775 Jechtenham, Österreich`(address)

</details>

---

## `Federal Tax Court`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `afa5684f`  
**Description:**
Matches Bundesfinanzgericht and all its case endings, including optional (BFG) suffix.

**Content:**
```
(?i)\b(Bundesfinanzgericht(?:es|s|en)?s?)(?:\s*\(BFG\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Administrative Court`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cbaa7335`  
**Description:**
Matches Verwaltungsgerichtshof and all its case endings, including optional (VwGH) suffix.

**Content:**
```
(?i)\b(Verwaltungsgerichtshof(?:es|s|en)?s?)(?:\s*\(VwGH\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 7 | 0 | 7 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 7 | 394 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/4Ob23_24x`) (sent_id: `deanon_TRAIN/4Ob23_24x_31`)


Der Verwaltungsgerichtshof definiert „Handel“ als eine auf den Warenaustausch zwischen den einzelnen Wirtschaftsgliedern gerichtete gewerbsmäßige Tätigkeit (83/04/0257;

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_46`)


2. Auch der Verwaltungsgerichtshof befasste sich inzwischen eingehend mit der Rechtsprechung des Gerichtshofs der Europäischen Union und der unionsrechtlichen Zulässigkeit von Beschränkungen der Glücksspieltätigkeiten durch das GSpG (Ro 2015/17/0022).

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_47`)


Auch der Verwaltungsgerichtshof verneinte eine Unionsrechtswidrigkeit der einschlägigen glücksspielrechtlichen Bestimmungen.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_50`)


3. Auch in der Zusammenschau mit der zitierten Entscheidung des Verwaltungsgerichtshofs erachtet der Senat durch die inhaltliche Entscheidung des Verfassungsgerichtshofs die unions- und verfassungsrechtlichen Fragen als hinreichend geklärt.

**False Positives:**

- `Verwaltungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob7_11v`) (sent_id: `deanon_TRAIN/10Ob7_11v_36`)


3. Erstmals im Rekurs hatten die Minderjährigen vorgebracht, es sei ihrem Vater durchaus zumutbar, in sein Heimatland zurückzukehren und dort zu arbeiten, zumal vor dem Verwaltungsgerichtshof ein „Ausweisungsverfahren“ anhängig sei und er ohnehin jederzeit mit der Abschiebung bzw Ausweisung rechnen müsse.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Ob7_11v`) (sent_id: `deanon_TRAIN/10Ob7_11v_39`)


Ein entsprechendes Vorbringen ist dem Rekurs der Minderjährigen jedoch nicht zu entnehmen, sodass die dort erstmals aufgestellte Behauptung zur Zumutbarkeit der Rückkehr nach Bosnien bereits vor Abschluss des vor dem Verwaltungsgerichtshof anhängigen Verfahrens, eine nicht zulässige Neuerung darstellte.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10Ob7_11v`) (sent_id: `deanon_TRAIN/10Ob7_11v_42`)


Nach den Umständen des vorliegenden Einzelfalls ließen sich nicht nur die beim Antragsgegner festgestellte geistige Behinderung als derartig berücksichtigungswürdiger Grund ins Treffen führen, sondern auch die - schon vom Rekursgericht ins Auge gefasste - Möglichkeit, dass er in dem vor dem Verwaltungsgerichtshof anhängigen Verfahren obsiegen und dann wieder über einen gültigen Aufenthaltstitel verfügen könnte.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Tax Authority Austria`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c2a31ff0`  
**Description:**
Matches Finanzamt Österreich and variations including genitive and optional parenthetical codes.

**Content:**
```
(?i)\b(Finanzamt(?:es)?\s+Österreich(?:\s*\([^)]+\))?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ministry of Finance`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4b2c511e`  
**Description:**
Matches Bundesministerium für Finanzen and BMF.

**Content:**
```
(?i)\b(Bundesministeriums?\s+für\s+Finanzen|BMF)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Administrative Court Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3edf6158`  
**Description:**
Matches VwGH acronym, but only when it appears as a standalone entity reference, not as part of a date citation if the full name is present, and avoids false positives in generic contexts.

**Content:**
```
(?i)\b(VwGH)\b(?![\s]*[0-9]{2}\.?[0-9]{2}\.?[0-9]{2,4})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 19 | 0 | 19 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 19 | 369 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/6Ob161_10k`) (sent_id: `deanon_TRAIN/6Ob161_10k_36`)


Die dem Enteigneten gebührende Entschädigung muss alle durch die Enteignung verursachten vermögensrechtlichen Nachteile erfassen, wobei bei ihrer Bemessung auch auf sämtliche bestehende wirtschaftliche Möglichkeiten bedacht zu nehmen ist (VwGH 28.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/1Ob4_20z`) (sent_id: `deanon_TRAIN/1Ob4_20z_41`)


Mit der Bestellung zum Organ der Straßenaufsicht gemäß § 97 StVO werden dem Betroffenen hoheitliche Befugnisse übertragen, weil er unter den Voraussetzungen der Abs 4 und 5a leg cit Anordnungen und Aufforderungen betreffend die Benützung der Straße erteilen kann (VwGH Ra 2016/11/0177;Pürstl, StVO15.00§ 97 E 6/1).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/9Ob31_22g`) (sent_id: `deanon_TRAIN/9Ob31_22g_52`)


2.3… Unter die Gewerbeberechtigung für das Gastgewerbe fällt auch die Lieferung und damit der Verkauf von angerichteten kalten Platten, kalten oder warmen Buffets sowie sonstigen warmen Speisen und Menüs ohne Nebenleistungen (vgl VwGH 10.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/2Ob47_25p`) (sent_id: `deanon_TRAIN/2Ob47_25p_58`)


Die Kundmachung der – im Übrigen entgegen § 48 Abs 2 StVO nur am linken Straßenrand aufgestellten (vgl VwGH 85/02/0240 und 88/17/0139) – Verbotszeichen nach § 52 lit a Z 1 StVO war nicht durch die Verordnung der Bezirkshauptmannschaft gedeckt, die nur einbeschränktesFahrverbot mit entsprechender Zusatztafel („Zufahrt bis zur Baustelle gestattet“) verfügt hatte.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/1Ob79_17z`) (sent_id: `deanon_TRAIN/1Ob79_17z_64`)


Lfg 2014], Rz 7 f zu § 19 Abs 1a UStG), den Begriff des Bauwerks – und damit den der Bauleistung – weit auszulegen (VwGH 2011/15/0049).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/1Ob79_17z`) (sent_id: `deanon_TRAIN/1Ob79_17z_68`)


Werden im Zusammenhang mit Bauleistungen unselbständige Nebenleistungen erbracht, teilen sie das steuerrechtliche Schicksal der Hauptleistung (vgl nur VwGH 2011/15/0049, der allerdings den Fall der Warenlieferung als Hauptleistung und deren Montage als Nebenleistung behandelt; vgl dazuSchlager, SWK 32/2013, 1404).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/1Ob79_17z`) (sent_id: `deanon_TRAIN/1Ob79_17z_81`)


Dabei wird vor allem zu beachten sein, dass der Begriff der „Bauleistungen“ im Sinne des verfolgten Gesetzeszwecks weit auszulegen und auf die Qualifikation der Hauptleistung abzustellen ist (VwGH 2011/15/0049).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/1Ob41_18p`) (sent_id: `deanon_TRAIN/1Ob41_18p_99`)


VwGH 2011/21/0244).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_43`)


§ 330a ASVG sei nach der Rsp des VwGH auch auf solche Wohnformen anzuwenden.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_131`)


Allerdings führte der Oberste Gerichtshof ergänzend aus, dass der Sozialhilfeträger nicht zwischen öffentlich- und privatrechtlicher Handlungsform wählen könne, wenn das Gesetz bei Bestehen eines Rechtsanspruchs die Gewährung von Hilfe in hoheitlicher Handlungsform vorsehe (ebenso VwGH 99/11/0367 für das nö SHG).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_142`)


(c) Die Nichtberücksichtigung des Vermögens entspricht im Übrigen der Rechtsprechung des VwGH, wonach auch „besondere Wohnformen“ bei entsprechender Pflege und Betreuung unter das Verbot des Pflegeregresses fallen (VwGH Ra 2018/10/0062).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 11** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_151`)


Es kann daher offen bleiben, ob ein Sozialhilfeträger, der keinen Bescheid erlassen hat, sich aus Sozialhilferecht ergebende Kostenbeiträge für faktisch gewährte Hilfe tatsächlich auf dem Rechtsweg geltend machen kann (so 1 Ob 2302/96b, 9 Ob 126/00w) oder ob nicht zumindest im konkreten Fall die Pflicht zur Erlassung eines Bescheides über den Einsatz eigener Mittel (§ 25 oöSHG) den Rechtsweg ausschließt (vgl VwGH 99/11/0367 für das nöSHG).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/8Ob56_20y`) (sent_id: `deanon_TRAIN/8Ob56_20y_36`)


Der Verlesung der Angebote, deren Zweck die Transparenz des Vergabeverfahrens und die Vorbeugung von Manipulationen war (vgl VwGH 2004/04/0100;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/8Ob56_20y`) (sent_id: `deanon_TRAIN/8Ob56_20y_59`)


Die Regelung des § 334 BVergG 2018 ist – wie die Revisionsrekurswerberin zutreffend bemerkt – abschließend (vgl VwGH 2012/04/0133).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/8Ob56_20y`) (sent_id: `deanon_TRAIN/8Ob56_20y_65`)


Nicht gesondert anfechtbare Entscheidungen sind gemeinsam mit der nachfolgend gesondert anfechtbaren Entscheidung anzufechten (vgl VwGH 2012/04/0154;Heid/RinginHeid/Reisner/Deutschmann, BVergG 2018 § 2 Rz 48 mwN).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/8Ob56_20y`) (sent_id: `deanon_TRAIN/8Ob56_20y_66`)


Zur alten Rechtslage hat der VwGH etwa bereits ausgesprochen, dass die Unterlassung von verpflichtenden Verlesungen bei der Angebotsöffnung zur Nichtigerklärung der Zuschlagserteilung führen kann (VwGH 2004/04/0100;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 16** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__10`)


VwGH Ro 2014/03/0045).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Federal Tax Court Acronym BFG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7abd2887`  
**Description:**
Matches BFG acronym, ensuring it's not part of a date citation.

**Content:**
```
(?i)\b(BFG)\b(?![\s]*[0-9]{2}\.?[0-9]{2}\.?[0-9]{2,4})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `UFS Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9eb79492`  
**Description:**
Matches UFS acronym, ensuring it's not part of a date citation.

**Content:**
```
(?i)\b(UFS)\b(?![\s]*[0-9]{2}\.?[0-9]{2}\.?[0-9]{2,4})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `University Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6da0d398`  
**Description:**
Matches Universität Wien

**Content:**
```
(?i)\b(Universität\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Social Ministry`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `03b8a937`  
**Description:**
Matches Bundesamt für Soziales und Behindertenwesen

**Content:**
```
(?i)\b(Bundesamt(?:s)?\s+für\s+Soziales\s+und\s+Behindertenwesen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AMS Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ab1bdb91`  
**Description:**
Matches AMS acronym for Arbeitsmarktservice

**Content:**
```
(?i)\b(AMS)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 3 | 0 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 3 | 269 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9ObA50_21z`) (sent_id: `deanon_TRAIN/9ObA50_21z_6`)


Sie wird vom AMS im Rahmen von dessen Förderschiene „gemeinnütziges Beschäftigungsprojekt“ finanziert.

**False Positives:**

- `AMS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/3Ob222_17v`) (sent_id: `deanon_TRAIN/3Ob222_17v_8`)


Danach meldete er sich beim AMS als arbeitssuchend.

**False Positives:**

- `AMS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/9Ob22_18b`) (sent_id: `deanon_TRAIN/9Ob22_18b_20`)


2. am 20. 1. 2016 1.108,24 EUR vom AMS Wien an Arbeitslosengeld für die Zeit Ende Dezember 2014/Anfang Jänner 2015;

**False Positives:**

- `AMS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Local Tax Office`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ecab04b8`  
**Description:**
Matches Finanzamt followed by city names, strictly excluding Bundesfinanzgericht and stopping before dates.

**Content:**
```
(?i)\b(Finanzamt(?:s)?\s+(?:Wien\s+(?:9/18/19|1/23|\d+)?|Neunkirchen\s+(?:Wr\.\s*Neustadt|Wiener\s*Neustadt)?|Oststeiermark|Stallhofen|Landeck\s+Reutte|Klosterneuburg|Österreich))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bank and Other Org`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `53220dfe`  
**Description:**
Matches specific bank names and other organizations like 'Reinemut + Smoch Handel' that don't fit GmbH/AG patterns.

**Content:**
```
(?i)\b((?:Raiffeisenbank\s+[A-Za-z]+|Reinemut\s+\+\s+Smoch\s+Handel|SENECURA|SeneCura|ÖBB|PVA|Bezirkshauptmannschaft\s+[A-Za-z]+|Versorgungskasse\s+Deutscher\s+Unternehmen\s+VVaG|Deutschen\s+Rentenversicherung\s+Bund|Pensionsversicherungsanstalt\s+Wien|Krankenpflegevereins\s+Bludenz|Imre\s+\&\s+Schaffer\s+Rechtsanwälte\s+OG|TAXCOACH\s+Wirtschaftsprüfung\s+und\s+Steuerberatung\s+GmbH\s*&\s*Co\s*KG|BKS\s+Steuerberatung\s+GmbH\s*&\s*Co\s*KG|Dr\.\s+Roland\s+Gabl\s+Rechtsanwalts-\s+Kommandit-Partnerschaft|\u201e\u00d6BUG\u201c\s+DR\.\s+Nikolaus\s+Wirtschaftstreuhand\s+GmbH\s*-\s+Wirtschaftsprüfungs-\s+und\s+Steuerberatungsgesellschaft|How\s+to\s+spend\s+it\s+Verlag\s+GmbH|INET\s+Internet\s+Service\s+GmbH|INET\s+System\s+Informations\s+GmbH|Talwerk\s+Logistik\s+Holding\s+GMBH|InnMarine\s+GMBH|Mittel\s+Unisyn\s+GMBH|Bärs\s+\&\s+Walterscheidt\s+Handel\s+GMBH|Ober\s+Lemostnor\s+AG|Vennes\s+Recycling\s+AG|HPS\s+Hergovits,\s+Pinkel\s+\&\s+Schnabl\s+Steuerberatungs\s+GmbH|Reinemut\s+\+\s+Smoch\s+Handel|Zollamt\s+Österreich|Amt\s+für\s+Betrugsbekämpfung\s+als\s+Finanzstrafbehörde|Verfassungsgerichtshof))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 41 | 0 | 41 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 41 | 396 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_93`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_151`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_162`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 3** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_167`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob62_17s`) (sent_id: `deanon_TRAIN/10Ob62_17s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache der mj Traude Coelsch, geboren am 8. Februar 1982, vertreten durch das Land Salzburg als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft St. Johann im Pongau, 5600 St. Johann im Pongau, Hauptstraße 1), wegen Herabsetzung von Unterhaltsvorschüssen, infolge des Revisionsrekurses des Kindes gegen den Beschluss des Landesgerichts Salzburg als Rekursgericht vom 9. Februar 2017, GZ 21 R 457/16a-31, womit der Beschluss des Bezirksgerichts St. Johann im Pongau vom 13. Oktober 2016, GZ 38 PU 154/15a-26, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Rekursgericht mit dem Auftrag zurückgestellt, eine Gleichschrift des Revisionsrekurses des Kindes dem Bund zur allfälligen Erstattung einer Revisionsrekursbeantwortung binnen 14 Tagen zuzustellen.

**False Positives:**

- `Bezirkshauptmannschaft St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Traude Coelsch`(person)
- `8. Februar 1982`(date)

**Example 5** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_32`)


Mit Beschluss vom 30. März 2016 hat der Oberste Gerichtshof zu 4 Ob 31/16m ua in sechs verbundenen Verfahren, denen Sachverhalte zugrundelagen, die mit jenem dieses Verfahrens vergleichbar sind, die dort näher bezeichneten Bestimmungen des Glücksspielgesetzes und des NÖ Spielautomatengesetzes 2011 (hilfsweise die genannten Gesetze zur Gänze) beim Verfassungsgerichtshof als verfassungswidrig angefochten.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_34`)


Mit Beschluss vom 15. Oktober 2016 zu G 103 – 104/2016-49 ua wies der Verfassungsgerichtshof die Anträge des Obersten Gerichtshofs und anderer Gerichte als unzulässig zurück.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_39`)


1. Mit Erkenntnis vom 15. Oktober 2016 zu E 945/2016-24 ua wies der Verfassungsgerichtshof mehrere Beschwerden ab, die gegen die gesetzliche Beschränkung des Glücksspiels gerichtet waren.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_41`)


Der Verfassungsgerichtshof ging inhaltlich davon aus, dass die Bestimmungen des GSpG allen vom EuGH aufgezeigten Vorgaben des Unionsrechts entsprechen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_51`)


Ungeachtet der Zurückweisung der Anträge des Senats aus formalen Gründen ging der Verfassungsgerichtshof im Erkenntnis über die Beschwerden umfassend auf die Vorgaben des EuGH zur Unionsrechtskonformität von Glücksspielrechtsnormen und auch auf die vom Senat gegen die österreichische Rechtslage geäußerten Bedenken ein.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `ÖBB` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 11** (doc_id: `deanon_TRAIN/4Ob74_21t`) (sent_id: `deanon_TRAIN/4Ob74_21t_65`)


Schon deswegen ist seiner Anregung, eine Prüfung des § 2 NWG (der gar nicht die Entschädigung betrifft) durch den Verfassungsgerichtshof zu veranlassen, nicht zu folgen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/9Ob31_22g`) (sent_id: `deanon_TRAIN/9Ob31_22g_76`)


[17] Darauf, dass die sachliche Rechtfertigung von S 2 und 3 leg cit aus Anlass der Pandemie Gegenstand einer breiten literarischen Kontroverse und eines vor dem Verfassungsgerichtshof anhängigen Gesetzesprüfungsverfahrens (G 279/2021) wurde, ist im gegenwärtigen Verfahrensstadium nicht Bedacht zu nehmen, weil nach dem Vorbringen der Streitteile nicht erkennbar ist, ob hier ein Miet- oder ein Pachtverhältnis vorliegt (in den Schriftsätzen beider Parteien wurden – ebenso wie in den Parteienaussagen – beide Begriffe verwendet;

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/2Ob47_25p`) (sent_id: `deanon_TRAIN/2Ob47_25p_9`)


Nach einer Verordnung der zuständigen Bezirkshauptmannschaft sollte das Befahren der Bundesstraße in beiden Richtungen „mit der Zusatztafel ‚Zufahrt bis zur Baustelle gestattet‘“ verboten sein.

**False Positives:**

- `Bezirkshauptmannschaft sollte` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/2Ob47_25p`) (sent_id: `deanon_TRAIN/2Ob47_25p_10`)


Für Fahrzeuge über 3,5 Tonnen verordnete die Bezirkshauptmannschaft ein Fahrverbot mit der Zusatztafel „ausgenommenen Linienbusse und Müllabfuhr sowie Ziel und Quellverkehr in den Gemeinden Tatjana Single und Ronald Gehroldt “.

**False Positives:**

- `Bezirkshauptmannschaft ein` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tatjana Single`(person)
- `Ronald Gehroldt`(person)

**Example 15** (doc_id: `deanon_TRAIN/2Ob47_25p`) (sent_id: `deanon_TRAIN/2Ob47_25p_58`)


Die Kundmachung der – im Übrigen entgegen § 48 Abs 2 StVO nur am linken Straßenrand aufgestellten (vgl VwGH 85/02/0240 und 88/17/0139) – Verbotszeichen nach § 52 lit a Z 1 StVO war nicht durch die Verordnung der Bezirkshauptmannschaft gedeckt, die nur einbeschränktesFahrverbot mit entsprechender Zusatztafel („Zufahrt bis zur Baustelle gestattet“) verfügt hatte.

**False Positives:**

- `Bezirkshauptmannschaft gedeckt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_26`)


[7]2.2.Von diesen Grundsätzen abzugehen, besteht hier kein Anlass: [8]3.1.Der Verfassungsgerichtshof hat die Behandlung des von der Klägerin im vorliegenden Verfahren gemäß Art 140a B-VG gestellten Antrags zur Prüfung der Verfassungsmäßigkeit von Art III Abschn 9 und Art VIII Abschn 19 und 20 Amtssitzabk sowie Art XV Statuten abgelehnt (VfGH 15.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_29`)


Der Verfassungsgerichtshof hielt dafür, dass vor dem Hintergrund von Art XIX Abschn 50 lit a Amtssitzabk sowie der – von der Klägerin und Antragstellerin nicht bestrittenen – Möglichkeit, Beschwerde an das Verwaltungsgericht der Internationalen Arbeitsorganisation zu erheben (VfGH 29.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_35`)


[10]3.3.Vor diesem Hintergrund sieht sich auch der Oberste Gerichtshof durch die Rechtsprechung des Verfassungsgerichtshofs und von ihm zitierte EGMR-Judikatur referierenden Revisionsrekurs nicht veranlasst, die Verfassungsgemäßheit von Amtssitzabk und Statut als bindende Staatsverträge in Frage zu stellen (vgl Art 89 Abs 1 und 2 B-VG): Die Beklagte sieht ein mehrstufiges Beschwerdeverfahren vor, zu dem bereits sowohl der EGMR (6. 1. 2015, 415/07, Klausecker, Rz 70 ff) als auch der Verfassungsgerichtshof (29. 9. 2022, SV 1/2021, Pkt IV.2.6 aE) darauf hingewiesen haben, dass auch die Beschwerdemöglichkeit letztlich an das – von der Klägerin erneut als ungenügend vermeinte – Verwaltungsgericht der Internationalen Arbeitsorganisation bzw die Möglichkeit eines Schiedsverfahrens nach dessen Regeln ein hinreichender angemessener alternativer Streitbeilegungsmechanismus wäre.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/10Nc32_14h`) (sent_id: `deanon_TRAIN/10Nc32_14h_5`)


Das Land Steiermark als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Liezen) vertritt das Kind zur Durchsetzung dessen Unterhaltsansprüche.

**False Positives:**

- `Bezirkshauptmannschaft Liezen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_85`)


Nur in diesem Fall wäre auch zu prüfen, ob § 330a ASVG unmittelbar anzuwenden wäre oder nicht vielmehr eine Anfechtung beim Verfassungsgerichtshof zu erfolgen hätte.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/10Ob14_18h`) (sent_id: `deanon_TRAIN/10Ob14_18h_65`)


1.2.2 Wie die Beklagte in ihrer Revisionsbeantwortung vorbringt, ist § 4a VZKG bereits Gegenstand eines im November 2017 von der Beklagten gemeinsam mit anderen Kreditunternehmen beim Verfassungsgerichtshof eingebrachten Individualantrags gemäß Art 140 Abs 1 Z 1 lit c B-VG, der dort zu G 293/2017 anhängig ist.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/10Ob14_18h`) (sent_id: `deanon_TRAIN/10Ob14_18h_66`)


Unter einem regt die Beklagte an, auch der Oberste Gerichtshof möge § 4 Abs 2 und § 4a VZKG nF dem Verfassungsgerichtshof zur Überprüfung gemäß Art 140 Abs 1 Z 1 lit a B-VG vorlegen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_25`)


Die darin geltend gemachten Verfassungswidrigkeiten wurden vom Verfassungsgerichtshof im Hinblick auf sein Erkenntnis vom 12.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_27`)


Hervorzuheben ist insbesondere, dass der Verfassungsgerichtshof offensichtlich auch den Umstand, dass die Beklagte nicht im Allein-, sondern im (indirekten) Mehrheitseigentum des Landes Niederösterreich steht, nicht als ausreichendes Differenzierungskriterium für eine weitere Prüfung erachtet hat.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_28`)


Auch die Ausführungen des Klägers zu einem Verstoß gegen das rechtsstaatliche Prinzip und zur mangelnden Kompetenz des Landesgesetzgebers veranlassten den Verfassungsgerichtshof nicht zur Prüfung der angefochtenen Norm.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_31`)


Zu deren Maßgeblichkeit nahm der Verfassungsgerichtshof bereits im erwähnten Erkenntnis vom 12.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/9Ob82_21f`) (sent_id: `deanon_TRAIN/9Ob82_21f_30`)


[9] Allerdings hat schon der Verfassungsgerichtshof (Beschluss vom 30. 9. 2021, V178/2021-12) zu der dort behaupteten Verletzung in den verfassungsgesetzlich gewährleisteten Rechten auf Datenschutz (§ 1 DSG) und im Recht auf Achtung des Privat- und Familienlebens (Art 8 EMRK) ausgeführt, das Vorbringen lasse die behaupteten Rechtsverletzungen als so wenig wahrscheinlich erkennen, dass der Antrag keine Aussicht auf Erfolg habe.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_79`)


Der Verfassungsgerichtshof hat bereits ausgesprochen, dass das verfassungsrechtliche Gebot der (zureichenden) steuerlichen Entlastung von Unterhaltslasten auch im Weg einer gesetzlichen Pauschalierung erfolgen kann.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_81`)


Wenn der Gesetzgeber auf die Vorgaben durch den Verfassungsgerichtshof reagiert und den Familienbonus Plus mit der Zielsetzung eingeführt hat, dass die Unterhaltspflichtigen die Unterhaltslasten zukünftig aus ihrem unversteuerten Einkommen leisten können und nicht eine darauf leistende Steuer dazuverdienen müssen, besteht das Ziel der in Rede stehenden steuergesetzlichen Maßnahme darin, das Einkommen des Geldunterhaltspflichtigen, aus dem der Unterhalt geleistet wird, im Einklang mit den Vorgaben durch den Verfassungsgerichtshof steuerlich zu entlasten.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 30** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_103`)


Da der Gesetzgeber bis 31. Dezember 2018 weder die vom Verfassungsgerichtshof im Erkenntnis zu B 1285/00 in den Raum gestellte pauschalierende Entlastung noch eine andere sachliche Regelung umgesetzt hat, um den verfassungsrechtlichen Vorgaben zu entsprechen, hat sich der Oberste Gerichtshof in seiner Rechtsprechung an der Ansicht des Verfassungsgerichtshofs orientiert.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_125`)


Die vom Verfassungsgerichtshof vorgegebene pauschalierende steuerliche Entlastung, die im Weg des Unterhaltsabsetzbetrags bisher noch nicht ausreichend erreicht wurde, ist durch die Einführung des Familienbonus Plus nunmehr als ausreichend gewährleistet anzusehen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/10Ob7_11v`) (sent_id: `deanon_TRAIN/10Ob7_11v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hradil als Vorsitzenden und die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache der minderjährigen Meinrad Vandame, geboren am 19. Februar 1978 und des minderjährigen Univ.-Prof. Prof. Anatol Nißl, geboren am 26. Januar 1974, beide wohnhaft bei der Mutter in Pia Feichtmayer, vertreten durch den Jugendwohlfahrtsträger Land Kärnten, dieser vertreten durch die Bezirkshauptmannschaft Spittal an der Drau, Bereich 6-Soziales, Jugend und Familie, wegen Befreiung des Vaters der Minderjährigen von der Unterhaltspflicht, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 18. November 2010, GZ 3 R 176/10g-46, womit der Beschluss des Bezirksgerichts Spittal an der Drau vom 19. Juli 2010, GZ 3 PU 180/09k-42, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird mangels der Voraussetzungen des § 62 Abs 1 AußStrG zurückgewiesen (§ 71 Abs 3 AußStrG).

**False Positives:**

- `Bezirkshauptmannschaft Spittal` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Meinrad Vandame`(person)
- `19. Februar 1978`(date)
- `Univ.-Prof. Prof. Anatol Nißl`(person)
- `26. Januar 1974`(date)
- `Pia Feichtmayer`(person)

**Example 33** (doc_id: `deanon_TRAIN/10Ob33_17a`) (sent_id: `deanon_TRAIN/10Ob33_17a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann sowie den Hofrat Mag. Ziegelbauer als weitere Richter in der Pflegschaftssache des mj Leonhard Huperz, geboren am 27. April 2001, vertreten durch das Land Kärnten als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Klagenfurt-Land, Jugendwohlfahrt, 9021 Klagenfurt, Völkermarkter Ring 19), wegen Unterhaltsvorschuss, infolge Revisionsrekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Graz, gegen den Beschluss des Landesgerichts Klagenfurt als Rekursgericht vom 17. März 2017, GZ 4 R 70/17m-54, womit der Beschluss des Bezirksgerichts Klagenfurt vom 26. Jänner 2017, GZ 1 Pu 220/11d-47, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Bezirkshauptmannschaft Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Leonhard Huperz`(person)
- `27. April`(date)

**Example 34** (doc_id: `deanon_TRAIN/10Ob33_17a`) (sent_id: `deanon_TRAIN/10Ob33_17a_12`)


Text Begründung: Mit einer vor der Bezirkshauptmannschaft Klagenfurt-Land, Bereich Jugend und Familie zur Zahl V 45/07-9 abgeschlossenen Unterhaltsvereinbarung vom 26.

**False Positives:**

- `Bezirkshauptmannschaft Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/10Ob33_17a`) (sent_id: `deanon_TRAIN/10Ob33_17a_18`)


Auch diese Vereinbarung wurde vor der Bezirkshauptmannschaft Klagenfurt-Land, Bereich Jugend und Familie abgeschlossen.

**False Positives:**

- `Bezirkshauptmannschaft Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_TRAIN/10Ob33_17a`) (sent_id: `deanon_TRAIN/10Ob33_17a_21`)


Als Unterhaltstitel wird in dem Antrag die mit dem Unterhaltsschuldner vor der Bezirkshauptmannschaft Klagenfurt-Land als Kinder- und Jugendhilfeträger am 5.

**False Positives:**

- `Bezirkshauptmannschaft Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_TRAIN/10Ob23_14a`) (sent_id: `deanon_TRAIN/10Ob23_14a_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des minderjährigen Aurelia von der Lei, geboren am 10. September 1997, in Pflege und Erziehung der Mutter Univ.-Prof.in Marceline Siladji, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger (Bezirkshauptmannschaft Gmunden, 4810 Gmunden, Esplanade 10), wegen Unterhaltsvorschuss, über den Revisionsrekurs des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Linz, gegen den Beschluss des Landesgerichts Wels als Rekursgericht vom 15. Jänner 2014, GZ 21 R 298/13t-38, womit der Beschluss des Bezirksgerichts Gmunden vom 18. Oktober 2013, GZ 1 Pu 223/09k-33, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Bezirkshauptmannschaft Gmunden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Aurelia von der Lei`(person)
- `Univ.-Prof.in Marceline Siladji`(person)

</details>

---

## `Specific Retailer Billa`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `2e3b0511`  
**Description:**
Matches the specific retailer Billa.

**Content:**
```
(?i)\b(Billa)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Amazon Transport GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1bc983f5`  
**Description:**
Matches Amazon Transport GmbH specifically.

**Content:**
```
(?i)\b(Amazon\s+Transport\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Post and Telekom Austria`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fc40d449`  
**Description:**
Matches Österreichischen Post Aktiengesellschaft and Telekom Austria Aktiengesellschaft.

**Content:**
```
(?i)\b(Österreichischen\s+Post\s+Aktiengesellschaft|Telekom\s+Austria\s+Aktiengesellschaft)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Police Directorate`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `408a5429`  
**Description:**
Matches Landespolizeidirektion followed by region.

**Content:**
```
(?i)\b(Landespolizeidirektion\s+[A-Za-z]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finance Court Senate`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `71bccd7c`  
**Description:**
Matches Finanzstrafsenat Wien X des Bundesfinanzgerichtes.

**Content:**
```
(?i)\b(Finanzstrafsenat\s+Wien\s+\d+\s+des\s+Bundesfinanzgericht(?:es|s)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Roelfsen Versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ea6c7e44`  
**Description:**
Matches the specific organization Roelfsen Versicherung.

**Content:**
```
(?i)\b(Roelfsen\s+Versicherung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Houdek Maschinenbau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `427cd7c4`  
**Description:**
Matches the specific organization Houdek Maschinenbau.

**Content:**
```
(?i)\b(Houdek\s+Maschinenbau)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schmeltz Luftfahrt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8b93a331`  
**Description:**
Matches the specific organization Schmeltz Luftfahrt.

**Content:**
```
(?i)\b(Schmeltz\s+Luftfahrt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dorfcon-Verlag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `778f1030`  
**Description:**
Matches the specific organization Dorfcon-Verlag.

**Content:**
```
(?i)\b(Dorfcon-Verlag)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lexdon IT`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ebd061f1`  
**Description:**
Matches the specific organization Lexdon IT.

**Content:**
```
(?i)\b(Lexdon\s+IT)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SeneCura Full Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7b46be1d`  
**Description:**
Matches the full name SeneCura Laurentius-Park Bludenz.

**Content:**
```
(?i)\b(SeneCura\s+Laurentius-Park\s+Bludenz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Lubomir Merschmeyer`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b3b748eb`  
**Description:**
Matches the specific organization Lubomir Merschmeyer.

**Content:**
```
(?i)\b(Lubomir\s+Merschmeyer)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Vienna Magistrate`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `923cbdfe`  
**Description:**
Matches Magistrat der Stadt Wien with department codes, ensuring the full entity is captured.

**Content:**
```
(?i)\b(Magistrat(?:s)?\s+der\s+Stadt\s+Wien(?:,\s+Magistratsabteilung\s+\d+)?(?:,\s+Magistratsabteilung\s+\d+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 9 | 0 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 9 | 392 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_4`)


Claire Al-Hakim, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Rechtsvertretung Bezirk 21, 1210 Wien, Franz-Jonas-Platz 12), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 22. November 2024, GZ 45 R 496/24k-26, mit dem der Beschluss des Bezirksgerichts Floridsdorf vom 2. August 2024, GZ 16 Pu 19/24a-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Claire Al-Hakim`(person)

**Example 1** (doc_id: `deanon_TRAIN/7Ob119_18b`) (sent_id: `deanon_TRAIN/7Ob119_18b_4`)


Matzka als weitere Richter in der Pflegschaftssache der Minderjährigen Silke Wieging, geboren am 20. März 2010, 12. September 1996, vertreten durch das Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 12, 13, 23, 1230 Wien, Rößlergasse 15, Mutter Fiona Wenzlick, Vater Viola Peiniger, vertreten durch Dr. Tassilo Wallentin LL.M, Rechtsanwalt in Wien, wegen Unterhalt, infolge Revisionsrekurses des Vaters gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. Mai 2018, GZ 44 R 104/18x-180, womit der Rekurs des Vaters gegen den Beschluss des Bezirksgerichts Meidling vom 25. Jänner 2018, GZ 1 Pu 73/10b-173, teilweise zurückgewiesen und ihm im Übrigen nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Silke Wieging`(person)
- `20. März`(date)
- `12. September 1996`(date)
- `Fiona Wenzlick`(person)
- `Viola Peiniger`(person)

**Example 2** (doc_id: `deanon_TRAIN/8Ob1_20k`) (sent_id: `deanon_TRAIN/8Ob1_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn, den Hofrat Dr. Stefula und die Hofrätin Mag. Wessely-Kristöfel als weitere Richter in der Pflegschaftssache der mj Niklas Chomicz, geboren am 6. Oktober 2009, 17. Mai 2000, vertreten durch den Magistrat der Stadt Wien, Wiener Kinder- und Jugendhilfe, Rechtsvertretung für den Bezirk 10, 1100 Wien, Alfred-Adler-Straße 12, wegen Unterhalt, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 15. Oktober 2019, GZ 45 R 363/19v-47, mit dem der Beschluss des Bezirksgerichts Favoriten vom 5. Juni 2019, GZ 8 Pu 52/10k-40, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Niklas Chomicz`(person)
- `6. Oktober`(date)
- `17. Mai 2000`(date)

**Example 3** (doc_id: `deanon_TRAIN/10Ob82_10x`) (sent_id: `deanon_TRAIN/10Ob82_10x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des mj Dimitri Ratzenböck, geboren am 6. August 1956, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, MA 11 Amt für Jugend und Familie, Rechtsvertretung für den 3. und 11.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dimitri Ratzenböck`(person)
- `6. August 1956`(date)

**Example 4** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der Pflegschaftssache des mj Konrad Mayr, geboren am 1. August 2020, und der mj Jean Angelis, geboren am 3. Oktober 2014, beide wohnhaft bei der Mutter Leonie Erbut, vertreten durch die Stadt Wien (Wiener Kinder- und Jugendhilfe des Magistrats der Stadt Wien) als Kinder- und Jugendhilfeträger, wegen Unterhalts, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 2. Juli 2019, GZ 45 R 317/19d-40, mit dem der Beschluss des Bezirksgerichts Favoriten vom 10. Mai 2019, GZ 6 Pu 62/15y-32, teilweise bestätigt, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Magistrats der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Konrad Mayr`(person)
- `1. August 2020`(date)
- `Jean Angelis`(person)
- `3. Oktober 2014`(date)
- `Leonie Erbut`(person)

**Example 5** (doc_id: `deanon_TRAIN/10Ob31_18h`) (sent_id: `deanon_TRAIN/10Ob31_18h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Pflegschaftssache der mj 1. OStR Klaus Schepers, geboren am Paulina Dutzschke, 2. Paulina Davisson, geboren am Rudolf Leirer, Bakk. art., 3. Evamaria Yakubov, geboren am 4. April 1998 und 4. OStR Guntram Sepan, geboren am 24. Februar 1988, alle vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 2, 20), 1200 Wien, Dresdnerstraße 43, wegen Unterhaltsvorschuss, infolge des Revisionsrekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 6. Dezember 2017, GZ 45 R 413/17v, 45 R 414/17s, 45 R 415/17p, 45 R 416/17k, 45 R 545/17f-48, womit die Beschlüsse des Bezirksgerichts Leopoldstadt vom 4. Juli 2017, GZ 3 Pu 123/16g-22, -23, -24, -25 (ON 25 in der Fassung des Berichtigungsbeschlusses vom 5. Juli 2017, GZ 3 Pu 123/16g-26), bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht mit dem Auftrag zurückgestellt, 1. den Träger der Kinder- und Jugendhilfe binnen einer Frist von 14 Tagen zur Klarstellung aufzufordern, ob die Erklärung der Zurückziehung der Unterhaltsvorschussanträge der Kinder vom 23.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OStR Klaus Schepers`(person)
- `Paulina Dutzschke`(person)
- `Paulina Davisson`(person)
- `Rudolf Leirer, Bakk. art.`(person)
- `Evamaria Yakubov`(person)
- `4. April 1998`(date)
- `OStR Guntram Sepan`(person)
- `24. Februar 1988`(date)

**Example 6** (doc_id: `deanon_TRAIN/10Ob22_10y`) (sent_id: `deanon_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Tiedke, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tiedke`(person)

**Example 7** (doc_id: `deanon_TRAIN/10Ob22_10y`) (sent_id: `deanon_TRAIN/10Ob22_10y_17`)


5. 2009 auch dem „Magistrat der Stadt Wien MA 11, AJF-R Bezirk 10, Van der Nüll-Gasse 20, 1100 Wien“ als gesetzlichen Vertreter der Minderjährigen zugestellt und von einem Postbevollmächtigten des Jugendamts übernommen wurde.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10Ob22_10y`) (sent_id: `deanon_TRAIN/10Ob22_10y_52`)


Nach dem im Akt befindlichen Rückschein wurde der Beschluss über die pflegschaftsgerichtliche Genehmigung des Scheidungsvergleichs richtigerweise dem „Magistrat der Stadt Wien MA 11, AJF-R Bezirk 10, Van der Nüll-Gasse 20, 1100 Wien“ als gesetzlichen Vertreter der Minderjährigen zugestellt und von einem Postbevollmächtigten dieser Dienststelle übernommen.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Tax Office Acronym FAÖ`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dac428f1`  
**Description:**
Matches FAÖ acronym for Finanzamt Österreich.

**Content:**
```
(?i)\b(FAÖ)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Constitutional Court`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `0bbc25f5`  
**Description:**
Matches Verfassungsgerichtshof and its genitive form.

**Content:**
```
(?i)\b(Verfassungsgerichtshof(?:es)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 29 | 0 | 29 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 29 | 396 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_93`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_151`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_162`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 3** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_167`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_32`)


Mit Beschluss vom 30. März 2016 hat der Oberste Gerichtshof zu 4 Ob 31/16m ua in sechs verbundenen Verfahren, denen Sachverhalte zugrundelagen, die mit jenem dieses Verfahrens vergleichbar sind, die dort näher bezeichneten Bestimmungen des Glücksspielgesetzes und des NÖ Spielautomatengesetzes 2011 (hilfsweise die genannten Gesetze zur Gänze) beim Verfassungsgerichtshof als verfassungswidrig angefochten.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_34`)


Mit Beschluss vom 15. Oktober 2016 zu G 103 – 104/2016-49 ua wies der Verfassungsgerichtshof die Anträge des Obersten Gerichtshofs und anderer Gerichte als unzulässig zurück.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_39`)


1. Mit Erkenntnis vom 15. Oktober 2016 zu E 945/2016-24 ua wies der Verfassungsgerichtshof mehrere Beschwerden ab, die gegen die gesetzliche Beschränkung des Glücksspiels gerichtet waren.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_41`)


Der Verfassungsgerichtshof ging inhaltlich davon aus, dass die Bestimmungen des GSpG allen vom EuGH aufgezeigten Vorgaben des Unionsrechts entsprechen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_51`)


Ungeachtet der Zurückweisung der Anträge des Senats aus formalen Gründen ging der Verfassungsgerichtshof im Erkenntnis über die Beschwerden umfassend auf die Vorgaben des EuGH zur Unionsrechtskonformität von Glücksspielrechtsnormen und auch auf die vom Senat gegen die österreichische Rechtslage geäußerten Bedenken ein.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/4Ob74_21t`) (sent_id: `deanon_TRAIN/4Ob74_21t_65`)


Schon deswegen ist seiner Anregung, eine Prüfung des § 2 NWG (der gar nicht die Entschädigung betrifft) durch den Verfassungsgerichtshof zu veranlassen, nicht zu folgen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/9Ob31_22g`) (sent_id: `deanon_TRAIN/9Ob31_22g_76`)


[17] Darauf, dass die sachliche Rechtfertigung von S 2 und 3 leg cit aus Anlass der Pandemie Gegenstand einer breiten literarischen Kontroverse und eines vor dem Verfassungsgerichtshof anhängigen Gesetzesprüfungsverfahrens (G 279/2021) wurde, ist im gegenwärtigen Verfahrensstadium nicht Bedacht zu nehmen, weil nach dem Vorbringen der Streitteile nicht erkennbar ist, ob hier ein Miet- oder ein Pachtverhältnis vorliegt (in den Schriftsätzen beider Parteien wurden – ebenso wie in den Parteienaussagen – beide Begriffe verwendet;

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_26`)


[7]2.2.Von diesen Grundsätzen abzugehen, besteht hier kein Anlass: [8]3.1.Der Verfassungsgerichtshof hat die Behandlung des von der Klägerin im vorliegenden Verfahren gemäß Art 140a B-VG gestellten Antrags zur Prüfung der Verfassungsmäßigkeit von Art III Abschn 9 und Art VIII Abschn 19 und 20 Amtssitzabk sowie Art XV Statuten abgelehnt (VfGH 15.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_29`)


Der Verfassungsgerichtshof hielt dafür, dass vor dem Hintergrund von Art XIX Abschn 50 lit a Amtssitzabk sowie der – von der Klägerin und Antragstellerin nicht bestrittenen – Möglichkeit, Beschwerde an das Verwaltungsgericht der Internationalen Arbeitsorganisation zu erheben (VfGH 29.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_35`)


[10]3.3.Vor diesem Hintergrund sieht sich auch der Oberste Gerichtshof durch die Rechtsprechung des Verfassungsgerichtshofs und von ihm zitierte EGMR-Judikatur referierenden Revisionsrekurs nicht veranlasst, die Verfassungsgemäßheit von Amtssitzabk und Statut als bindende Staatsverträge in Frage zu stellen (vgl Art 89 Abs 1 und 2 B-VG): Die Beklagte sieht ein mehrstufiges Beschwerdeverfahren vor, zu dem bereits sowohl der EGMR (6. 1. 2015, 415/07, Klausecker, Rz 70 ff) als auch der Verfassungsgerichtshof (29. 9. 2022, SV 1/2021, Pkt IV.2.6 aE) darauf hingewiesen haben, dass auch die Beschwerdemöglichkeit letztlich an das – von der Klägerin erneut als ungenügend vermeinte – Verwaltungsgericht der Internationalen Arbeitsorganisation bzw die Möglichkeit eines Schiedsverfahrens nach dessen Regeln ein hinreichender angemessener alternativer Streitbeilegungsmechanismus wäre.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_85`)


Nur in diesem Fall wäre auch zu prüfen, ob § 330a ASVG unmittelbar anzuwenden wäre oder nicht vielmehr eine Anfechtung beim Verfassungsgerichtshof zu erfolgen hätte.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/10Ob14_18h`) (sent_id: `deanon_TRAIN/10Ob14_18h_65`)


1.2.2 Wie die Beklagte in ihrer Revisionsbeantwortung vorbringt, ist § 4a VZKG bereits Gegenstand eines im November 2017 von der Beklagten gemeinsam mit anderen Kreditunternehmen beim Verfassungsgerichtshof eingebrachten Individualantrags gemäß Art 140 Abs 1 Z 1 lit c B-VG, der dort zu G 293/2017 anhängig ist.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/10Ob14_18h`) (sent_id: `deanon_TRAIN/10Ob14_18h_66`)


Unter einem regt die Beklagte an, auch der Oberste Gerichtshof möge § 4 Abs 2 und § 4a VZKG nF dem Verfassungsgerichtshof zur Überprüfung gemäß Art 140 Abs 1 Z 1 lit a B-VG vorlegen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_25`)


Die darin geltend gemachten Verfassungswidrigkeiten wurden vom Verfassungsgerichtshof im Hinblick auf sein Erkenntnis vom 12.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_27`)


Hervorzuheben ist insbesondere, dass der Verfassungsgerichtshof offensichtlich auch den Umstand, dass die Beklagte nicht im Allein-, sondern im (indirekten) Mehrheitseigentum des Landes Niederösterreich steht, nicht als ausreichendes Differenzierungskriterium für eine weitere Prüfung erachtet hat.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_28`)


Auch die Ausführungen des Klägers zu einem Verstoß gegen das rechtsstaatliche Prinzip und zur mangelnden Kompetenz des Landesgesetzgebers veranlassten den Verfassungsgerichtshof nicht zur Prüfung der angefochtenen Norm.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_31`)


Zu deren Maßgeblichkeit nahm der Verfassungsgerichtshof bereits im erwähnten Erkenntnis vom 12.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/9Ob82_21f`) (sent_id: `deanon_TRAIN/9Ob82_21f_30`)


[9] Allerdings hat schon der Verfassungsgerichtshof (Beschluss vom 30. 9. 2021, V178/2021-12) zu der dort behaupteten Verletzung in den verfassungsgesetzlich gewährleisteten Rechten auf Datenschutz (§ 1 DSG) und im Recht auf Achtung des Privat- und Familienlebens (Art 8 EMRK) ausgeführt, das Vorbringen lasse die behaupteten Rechtsverletzungen als so wenig wahrscheinlich erkennen, dass der Antrag keine Aussicht auf Erfolg habe.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_79`)


Der Verfassungsgerichtshof hat bereits ausgesprochen, dass das verfassungsrechtliche Gebot der (zureichenden) steuerlichen Entlastung von Unterhaltslasten auch im Weg einer gesetzlichen Pauschalierung erfolgen kann.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_81`)


Wenn der Gesetzgeber auf die Vorgaben durch den Verfassungsgerichtshof reagiert und den Familienbonus Plus mit der Zielsetzung eingeführt hat, dass die Unterhaltspflichtigen die Unterhaltslasten zukünftig aus ihrem unversteuerten Einkommen leisten können und nicht eine darauf leistende Steuer dazuverdienen müssen, besteht das Ziel der in Rede stehenden steuergesetzlichen Maßnahme darin, das Einkommen des Geldunterhaltspflichtigen, aus dem der Unterhalt geleistet wird, im Einklang mit den Vorgaben durch den Verfassungsgerichtshof steuerlich zu entlasten.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 25** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_103`)


Da der Gesetzgeber bis 31. Dezember 2018 weder die vom Verfassungsgerichtshof im Erkenntnis zu B 1285/00 in den Raum gestellte pauschalierende Entlastung noch eine andere sachliche Regelung umgesetzt hat, um den verfassungsrechtlichen Vorgaben zu entsprechen, hat sich der Oberste Gerichtshof in seiner Rechtsprechung an der Ansicht des Verfassungsgerichtshofs orientiert.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_125`)


Die vom Verfassungsgerichtshof vorgegebene pauschalierende steuerliche Entlastung, die im Weg des Unterhaltsabsetzbetrags bisher noch nicht ausreichend erreicht wurde, ist durch die Einführung des Familienbonus Plus nunmehr als ausreichend gewährleistet anzusehen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Constitutional Court Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `03fe0b28`  
**Description:**
Matches VfGH acronym.

**Content:**
```
(?i)\b(VfGH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 8 | 348 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/17Os34_15a`) (sent_id: `deanon_TRAIN/17Os34_15a_32`)


Hoheitliches Verwaltungshandeln kommt insbesondere im Einsatz bestimmter Rechtsformen (Verordnung, Bescheid, Akt unmittelbarer verwaltungsbehördlicher Befehls- und Zwangsgewalt, im Innenverhältnis auch Weisung) zum Ausdruck (17 Os 25/14a, EvBl 2014/136, 928; vgl auch RIS-Justiz RS0129612; zur ständigen Rechtsprechung des VfGH grundlegend VfSlg 3.262).

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/13Os137_17x`) (sent_id: `deanon_TRAIN/13Os137_17x_15`)


Sie wären somit nicht dem Gericht, sondern der Verwaltungsbehörde zuzurechnen und daher – als Akte unmittelbarer verwaltungsbehördlicher Befehls- und Zwangsgewalt – (nicht mit Grundrechtsbeschwerde an den Obersten Gerichtshof, sondern) gemäß Art 130 Abs 1 Z 2 B-VG mit Beschwerde an das zuständige Verwaltungsgericht zu bekämpfen (vgl VfGH 13.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_8`)


In ihrem nunmehr gegen die (nach Unterbrechung nach § 62a Abs 6 VfGG und Fortsetzung des Rekursverfahrens nach Vorliegen der VfGH-Entscheidung getroffene) Rekursentscheidung (mit der die erstgerichtliche Zurückweisung der Klage mangels inländischer Gerichtsbarkeit bestätigt wurde) erhobenen außerordentlichen Revisionsrekurs zeigt die Klägerin keine erheblichen Rechtsfragen auf.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_26`)


[7]2.2.Von diesen Grundsätzen abzugehen, besteht hier kein Anlass: [8]3.1.Der Verfassungsgerichtshof hat die Behandlung des von der Klägerin im vorliegenden Verfahren gemäß Art 140a B-VG gestellten Antrags zur Prüfung der Verfassungsmäßigkeit von Art III Abschn 9 und Art VIII Abschn 19 und 20 Amtssitzabk sowie Art XV Statuten abgelehnt (VfGH 15.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_29`)


Der Verfassungsgerichtshof hielt dafür, dass vor dem Hintergrund von Art XIX Abschn 50 lit a Amtssitzabk sowie der – von der Klägerin und Antragstellerin nicht bestrittenen – Möglichkeit, Beschwerde an das Verwaltungsgericht der Internationalen Arbeitsorganisation zu erheben (VfGH 29.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/6Ob233_20p`) (sent_id: `deanon_TRAIN/6Ob233_20p_144`)


Wenngleich es dem Gesetzgeber im Allgemeinen zusteht, Gesetze auch rückwirkend in Kraft zu setzen, kann im Einzelfall eine Rückwirkung als gegen den Gleichheitsgrundsatz (Art 2 StGG, Art 7 B-VG) verstoßend verfassungswidrig sein, wenn dadurch gegen den Vertrauensgrundsatz verstoßen und/oder die Rechtsstellung der von der Rückwirkung Betroffenen maßgeblich verschlechtert wird (vgl VfGH G 228/89;

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/9Ob17_16i`) (sent_id: `deanon_TRAIN/9Ob17_16i_48`)


3.Der Revisionsrekurswerber regt im Zusammenhang mit seinen verfassungsrechtlichen Erwägungen die Vorlage an den VfGH durch den Obersten Gerichtshof (nur) an (klargestellt durch Stellungnahme des Antragstellers vom 6. 5. 2016), weil § 107 Abs 3 Z 3 AußStrG mangels Einbeziehung bzw Einverständnis der betroffenen Person verfassungswidrig sei.

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__9`)


GP 19 ff; vgl VfGH B 181/2014;

**False Positives:**

- `VfGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Gözcü Getränke`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `62abd1b9`  
**Description:**
Matches the specific organization Gözcü Getränke.

**Content:**
```
(?i)\b(Gözcü\s+Getränke)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Labor Court Vienna`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dee27985`  
**Description:**
Matches Arbeits- und Sozialgericht Wien and variations.

**Content:**
```
(?i)\b(Arbeits-\s+und\s+Sozialgericht(?:\s+Wien)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 28 | 0 | 28 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 28 | 376 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9Nc16_11v`) (sent_id: `deanon_TRAIN/9Nc16_11v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Dr. Hopf und Mag. Ziegelbauer als weitere Richter in der Arbeitsrechtssache der klagenden Partei Senta Moshack, vertreten durch Berchtold & Kollerics, Rechtsanwälte in Graz, gegen die beklagte Partei Anton Reinerth, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17-19, wegen Feststellung (Streitwert: 69.000 EUR), über den Delegierungsantrag beider Parteien den Beschluss gefasst:  Spruch Der Akt wird dem Landesgericht für Zivilrechtssachen Graz als Arbeits- und Sozialgericht zur Entscheidung nach § 31a JN zurückgestellt.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Senta Moshack`(person)
- `Anton Reinerth`(person)

**Example 1** (doc_id: `deanon_TRAIN/9Nc16_11v`) (sent_id: `deanon_TRAIN/9Nc16_11v_5`)


Nach Einbringung der Klage, jedoch noch vor Anberaumung einer mündlichen Streitverhandlung in erster Instanz, beantragten die Parteien einvernehmlich die Delegierung der Arbeitsrechtssache an das Landesgericht Linz als Arbeits- und Sozialgericht.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/8ObS6_23z`) (sent_id: `deanon_TRAIN/8ObS6_23z_4`)


Gabriele Svirak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei RgR Maurice Fredekind, Bakk. phil., vertreten durch Burkowski Rechtsanwälte in Linz, gegen die beklagte Partei IEF Service GmbH, 1150 Wien, Linke Wienzeile 246, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17–19, wegen 166 EUR, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 23. Oktober 2023, GZ 11 Rs 65/23t-11.3, mit welchem das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 24. Mai 2023, GZ 11 Cgs 24/23v-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `RgR Maurice Fredekind, Bakk. phil.`(person)

**Example 3** (doc_id: `deanon_TRAIN/8ObA10_12x`) (sent_id: `deanon_TRAIN/8ObA10_12x_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Spenling als Vorsitzenden, die Hofräte Hon.-Prof. Dr. Kuras und Mag. Ziegelbauer sowie die fachkundigen Laienrichter Mag. Dr. Rolf Gleißner und Mag. Manuela Majeranowski als weitere Richter in der Arbeitsrechtssache der klagenden Partei Priv.-Doz.in HR OSR Larissa Abbate, vertreten durch Hasch & Partner Anwaltsgesellschaft mbH in Linz, gegen die beklagte Partei Bachbach-Marine Gesellschaft mbH, Floreweg 8, 9103 Bösenort, Österreich, vertreten durch Mag. Klaus F. Lughofer LLM, Rechtsanwalt in Linz, wegen Feststellung (Streitwert: 30.000 EUR), über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. November 2011, GZ 11 Ra 92/11w-10, womit über Berufung der klagenden Partei das Urteil des Landesgerichts Linz als Arbeits- und Sozialgericht vom 31. August 2011, GZ 11 Cga 101/11d-5, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Priv.-Doz.in HR OSR Larissa Abbate`(person)
- `Bachbach-Marine Gesellschaft mbH`(organisation)
- `Floreweg 8, 9103 Bösenort, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Schinko als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Mag. Irene Kienzl (aus dem Kreis der Arbeitgeber) und Eva-Maria Florianschütz (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Gertrud Johanna Ostrovska, gegen die beklagte Partei Steiermärkische Gebietskrankenkasse, 8011 Graz, Josef-Pongratz-Platz 1, vertreten durch Das Haus des Rechts Rechtsanwälte Destaller-Mader in Graz, wegen Kostenübernahme, infolge Rekurses der beklagten Partei gegen den Beschluss des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 19. November 2009, GZ 8 Rs 73/09f-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 1. September 2009, GZ 29 Cgs 90/09s-6, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ostrovska`(person)

**Example 5** (doc_id: `deanon_TRAIN/10ObS21_10a`) (sent_id: `deanon_TRAIN/10ObS21_10a_133`)


Auch dieser Umstand spricht dafür, dass auch die Ablehnung der Kostenübernahme für ein verordnetes Heilmittel durch eine Feststellungsklage beim Arbeits- und Sozialgericht bekämpft werden kann.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10ObS101_10s`) (sent_id: `deanon_TRAIN/10ObS101_10s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Dr. Erwin Blazek (aus dem Kreis der Arbeitgeber) und Dr. Rotraut Leitner (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Reneé Roeber, vertreten durch Mag. Klaus Philipp, Rechtsanwalt in Mattersburg, gegen die beklagte Partei Pensionsversicherungsanstalt, Friedrich-Hillegeist-Straße 1, 1020 Wien, vertreten durch Dr. Josef Milchram und andere Rechtsanwälte in Wien, wegen Invaliditätspension, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 16. Dezember 2009, GZ 8 Rs 5/09b-42, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Eisenstadt als Arbeits- und Sozialgericht vom 12. September 2008, GZ 23 Cgs 165/07f-20, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Reneé Roeber`(person)

**Example 7** (doc_id: `deanon_TRAIN/10ObS18_12p`) (sent_id: `deanon_TRAIN/10ObS18_12p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Schramm sowie die fachkundigen Laienrichter Dr. Peter Zeitler (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Techn R Sean Birtalan, vertreten durch Arnold & Arnold Rechtsanwälte in Innsbruck, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich- Hillegeist-Straße 1, wegen Invaliditätspension, infolge außerordentlicher Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 6. Dezember 2011, GZ 25 Rs 100/11h-64, womit das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 14. Juli 2011, GZ 16 Cgs 185/07t-59, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Techn R Sean Birtalan`(person)

**Example 8** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn als weitere Richter in der beim Landesgericht Salzburg als Arbeits- und Sozialgericht anhängigen Rechtssache der klagenden Partei Buth Analyse GmbH, Anabel Traudtmann, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Christine Schwemmer, vertreten durch Plankel Mayrhofer & Partner, Rechtsanwälte in Dornbirn, wegen 213,52 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, die Rechtssache an das Arbeits- und Sozialgericht Wien zu delegieren, wird abgewiesen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation
- `Arbeits- und Sozialgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Buth Analyse GmbH`(organisation)
- `Anabel Traudtmann`(person)
- `Christine Schwemmer`(person)

**Example 9** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_4`)


Text Begründung: Mit der am 14. 12. 2012 beim Landesgericht Salzburg als Arbeits- und Sozialgericht eingebrachten Mahnklage begehrte die Klägerin, eine Finanzvermittlungsgesellschaft mit Sitz in Salzburg, von dem im Bundesland Burgenland wohnhaften Beklagten die Rückzahlung von Provisionen aus einem Agentenvertrag.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_6`)


Gleichzeitig beantragte er die Delegierung der Rechtssache an das Arbeits- und Sozialgericht Wien.

**False Positives:**

- `Arbeits- und Sozialgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/8Nc21_10w`) (sent_id: `deanon_TRAIN/8Nc21_10w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Kuras und die Hofrätin Dr. Tarmann-Prentner als weitere Richter in der Rechtssache der klagenden Partei StadtEnergie Werke AG, Wilhelmine Hrncirik, vertreten durch Dr. Hartmut Ramsauer, Rechtsanwalt in Salzburg, gegen die beklagte Partei RgR Isabel Rövekamp, vertreten durch Frimmel/Anetter Rechtsanwaltsgesellschaft mbH in Klagenfurt am Wörthersee, wegen 4.696,20 EUR sA, über den Delegierungsantrag der beklagten Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag, an Stelle des Landesgerichts Salzburg als Arbeits- und Sozialgericht das Landesgericht Klagenfurt als Arbeits- und Sozialgericht zur Verhandlung und Entscheidung über die vorliegende Arbeitsrechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation
- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `StadtEnergie Werke AG`(organisation)
- `Wilhelmine Hrncirik`(person)
- `RgR Isabel Rövekamp`(person)

**Example 12** (doc_id: `deanon_TRAIN/8Nc21_10w`) (sent_id: `deanon_TRAIN/8Nc21_10w_5`)


Mit in Rechtskraft erwachsenem Beschluss vom 23. März 2010 erklärte sich das Bezirksgericht Salzburg für sachlich unzuständig und überwies die Rechtssache an das Landesgericht Salzburg als Arbeits- und Sozialgericht, weil nach dem Parteienvorbringen eine Rechtsstreitigkeit zwischen Arbeitgeber und Arbeitnehmer vorliege.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/8Nc21_10w`) (sent_id: `deanon_TRAIN/8Nc21_10w_6`)


Nach Einbringung eines vorbereitenden Schriftsatzes der Klägerin beantragte der Beklagte die Delegierung des Verfahrens gemäß § 31 JN an das Landesgericht Klagenfurt als Arbeits- und Sozialgericht.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/10ObS110_10i`) (sent_id: `deanon_TRAIN/10ObS110_10i_5`)


Lackner, Rechtsanwälte in Leoben, gegen die beklagte Partei Pensionsversicherungsanstalt, Friedrich-Hillegeist-Straße 1, 1021 Wien, wegen Invaliditätspension, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 5. Mai 2010, GZ 7 Rs 24/10v-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 3. Februar 2010, GZ 21 Cgs 246/09p-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/10ObS99_15d`) (sent_id: `deanon_TRAIN/10ObS99_15d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden, die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm sowie die fachkundigen Laienrichter Mag. Dr. Wolfgang Höfle (aus dem Kreis der Arbeitgeber) und Ing. Thomas Bauer (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Urs Klesy, vertreten durch Dr. Reinhard Tögl Rechtsanwaltsgesellschaft mbH in Graz, gegen die beklagte Partei Versicherungsanstalt für Eisenbahnen und Bergbau, Linke Wienzeile 48-52, 1060 Wien, vertreten durch Dr. Marie-Luise Safranek, Rechtsanwältin in Graz, wegen Wochengeld, infolge Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 25. Juni 2015, GZ 7 Rs 28/15i-9, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 25. Februar 2015, GZ 36 Cgs 216/14d-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Urs Klesy`(person)

**Example 16** (doc_id: `deanon_TRAIN/18OCg2_24d`) (sent_id: `deanon_TRAIN/18OCg2_24d_5`)


Text Begründung: [1] DerKlägerbegehrt mit seiner beim Landesgericht Klagenfurt als Arbeits- und Sozialgericht eingebrachten Klage, das Erkenntnis des Schiedsgerichts der beklagten Glaubensgemeinschaft vom 18.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/18OCg2_24d`) (sent_id: `deanon_TRAIN/18OCg2_24d_18`)


Rechtliche Beurteilung [6] DasLandesgericht Klagenfurtals Arbeits- und Sozialgericht erklärte sich mit Beschluss vom 21.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/8ObS8_22t`) (sent_id: `deanon_TRAIN/8ObS8_22t_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätin Dr. Tarmann-Prentner und den Hofrat Dr. Stefula als weitere Richter (Senat gemäß § 11a Abs 3 Z 2 ASGG) in der Sozialrechtssache der klagenden Partei Holger Sykorski, vertreten durch Dr. Herbert Marschitz und andere Rechtsanwälte in Kufstein, gegen die beklagte Partei IEF-Service GmbH, 6020 Innsbruck, Meraner Straße 1, vertreten durch die Finanzprokuratur in Wien, wegen 34.726 EUR sA (Insolvenzentgelt), über den Rekurs der klagenden Partei gegen den Beschluss des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. Oktober 2022, GZ 25 Rs 56/22d-34, mit dem das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 9. Juni 2022, GZ 44 Cgs 43/21m-27, samt dem ihm vorangegangenen Verfahren für nichtig erklärt und die Klage zurückgewiesen wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Rekurs wird Folge gegeben.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Holger Sykorski`(person)

**Example 19** (doc_id: `deanon_TRAIN/9ObA96_13b`) (sent_id: `deanon_TRAIN/9ObA96_13b_4`)


Brigitte Augustin und Mag. Andreas Hach als weitere Richter in der Arbeitsrechtssache der klagenden Partei DI Anita Crämer, vertreten durch Dr. Gerhard Hiebler und Dr. Gerd Grebenjak, Rechtsanwälte in Leoben, gegen die beklagte Partei, GQG E‑Commerce Gesellschaft mbH, Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich, vertreten durch Siemer-Siegel-Füreder & Partner, Rechtsanwälte in Wien, wegen Feststellung, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 18. April 2013, GZ 6 Ra 18/13h-10, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 7. November 2012, GZ 23 Cga 115/12x-6, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `DI Anita Crämer`(person)
- `GQG E‑Commerce Gesellschaft mbH`(organisation)
- `Franz-Cäsar-Weg 5, 4115 Gumpesberg, Österreich`(address)

**Example 20** (doc_id: `deanon_TRAIN/9ObA66_24g`) (sent_id: `deanon_TRAIN/9ObA66_24g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Mag. Ziegelbauer als Vorsitzenden, den Hofrat Dr. Hargassner und die Hofrätin Mag. Korn sowie die fachkundigen Laienrichter Dr. Johannes Pflug (aus dem Kreis der Arbeitgeber) und Nicolai Wohlmuth (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Paul Bönner, vertreten durch Haider | Obereder | Pilz Rechtsanwält:innen GmbH in Wien, gegen die beklagte Partei Enns-Wind AG, Niels Schmetjen, vertreten durch Dr. Guido Bach, Rechtsanwalt in Wien, wegen Feststellung, in eventu Zahlung von 1.104,62 EUR sA, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 28. Mai 2024, GZ 8 Ra 40/24x-18, mit dem der Berufung der beklagten Partei gegen das Urteil des Landesgerichts Korneuburg als Arbeits- und Sozialgericht vom 6. Dezember 2023, GZ 15 Cga 34/23a-10, nicht Folge gegeben wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Paul Bönner`(person)
- `Enns-Wind AG`(organisation)
- `Niels Schmetjen`(person)

**Example 21** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Gerlinde Saltzmann`(person)

**Example 22** (doc_id: `deanon_TRAIN/14Os5_20x`) (sent_id: `deanon_TRAIN/14Os5_20x_5`)


Text Gründe: Bei der Staatsanwaltschaft Salzburg war zu AZ 11 St 72/17x (unter anderem) gegen Iris Mocker, Norbert Stumber, Sabine Brueckmann, Dr. Gerald Deinhard, Manfred Knoch und Martina Elbrecht ein Ermittlungsverfahren wegen des Verdachts der falschen Beweisaussage nach § 288 Abs 1 StGB im von der Klägerin Mag. Dr. Waltraud Reithe, MBA geführten Verfahren AZ 20 Cga 79/14s des Landesgerichts Salzburg als Arbeits- und Sozialgericht anhängig (ON 1 S 2 iVm ON 2).

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mocker`(person)
- `Stumber`(person)
- `Brueckmann`(person)
- `Deinhard`(person)
- `Knoch`(person)
- `Elbrecht`(person)
- `Reithe`(person)

**Example 23** (doc_id: `deanon_TRAIN/14Os5_20x`) (sent_id: `deanon_TRAIN/14Os5_20x_6`)


Am 29. Mai 2018 stellte die Staatsanwaltschaft Salzburg das Ermittlungsverfahren (erneut) „gemäß § 190 Z 1 StPO“ ein (ON 1 S 7) und begründete dies (auf Antrag des Opfers Mag. Dr. Waltraud Ruprecht, MBA und in einer Stellungnahme zum Fortführungsantrag der Genannten) im Wesentlichen damit, dass die Aussagen der im Verfahren vor dem Arbeits- und Sozialgericht als Zeugen vernommenen Beschuldigten, die ihre Angaben im Ermittlungsverfahren aufrecht hielten, als „stimmig und (…) glaubwürdig zu erachten“ und „in den wesentlichen Punkten konform“ seien.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ruprecht`(person)

**Example 24** (doc_id: `deanon_TRAIN/14Os5_20x`) (sent_id: `deanon_TRAIN/14Os5_20x_33`)


Im vorliegenden Fall bezieht sich der Beschluss des Landesgerichts Salzburg pauschal auf sämtliche vom Fortführungsantrag betroffenen Beschuldigten und ihre Aussagen als Zeugen im Verfahren AZ 20 Cga 79/14s des Landesgerichts Salzburg als Arbeits- und Sozialgericht, ohne die jeweils rechtlich als entscheidend beurteilten Sachverhaltsannahmen (also jene Aussagen, die aus Sicht der Fortführungswerberin und [dieser folgend] des Landesgerichts Salzburg entgegen der Ansicht der Staatsanwaltschaft in objektiver Hinsicht den Tatbestand des § 288 Abs 1 StGB erfüllen) konkret zu nennen und damit einen Bezug zu den vom Auftrag auf Fortführung des Ermittlungsverfahrens betroffenen Taten herzustellen.

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/9ObA64_25i`) (sent_id: `deanon_TRAIN/9ObA64_25i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Mag. Ziegelbauer als Vorsitzenden, die Hofrätin Mag. Korn und den Hofrat Dr. Stiefsohn sowie die fachkundigen Laienrichter Mag. Anja Pokorny (aus dem Kreis der Arbeitgeber) und Dr. Peter Csar (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Vitus Schleiermacher, vertreten durch Mag. Doris Braun, Rechtsanwältin in Graz, gegen die beklagte Partei Land Jennifer Andressen, vertreten durch Mag. Bernd Wurnig, Rechtsanwalt in Graz, wegen 12.697,83 EUR brutto sA und Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 9. Juli 2025, GZ 7 Ra 20/25b-26, mit dem das Urteil des Landesgerichts für Zivilrechtssachen Graz als Arbeits- und Sozialgericht vom 9. September 2024, GZ 9 Cga 8/24m-15, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Arbeits- und Sozialgericht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vitus Schleiermacher`(person)
- `Jennifer Andressen`(person)

</details>

---

## `Bank Full Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ddcc838c`  
**Description:**
Matches full bank names including 'Bankstelle' and location, e.g., Raiffeisenbank Karnische Rion Bankstelle St.Stefan.

**Content:**
```
(?i)\b(Raiffeisenbank\s+[A-Za-z]+\s+(?:Rion\s+)?Bankstelle\s+[A-Za-z\.]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Court with Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `971aef3b`  
**Description:**
Matches court names followed by location suffixes like 'Außenstelle Linz'.

**Content:**
```
(?i)\b((?:Bundesfinanzgericht|Verwaltungsgerichtshof|Verfassungsgerichtshof)(?:s?)(?:,\s+Außenstelle\s+[A-Za-z]+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 48 | 0 | 48 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 48 | 396 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_93`)


Das Berufungsgericht sehe sich daher nicht zu einer Antragstellung an den Verfassungsgerichtshof veranlasst.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_151`)


2. Seine Anregung, ein Gesetzesprüfungsver-fahren beim Verfassungsgerichtshof bezüglich der „von der beklagten Partei ins Treffen geführten gesetzlichen Bestimmungen“ einzuleiten, begründet der Kläger mit einer Verletzung des Gleichheitssatzes.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_162`)


Mangelhaft soll das Berufungsverfahren deshalb geblieben sein, weil das Berufungsgericht keinen Antrag an den Verfassungsgerichtshof gestellt hat: Hat der Oberste Gerichtshof oder ein zur Entscheidung in zweiter Instanz zuständiges Gericht gegen die Anwendung eines (Bundes- oder Landes-)Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken, so ist nach Art 89 Abs 2 B-VG von Amts wegen der Antrag auf Aufhebung dieses Gesetzes beim Verfassungsgerichtshof zu stellen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 3** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_163`)


Nach einhelliger Rechtsprechung steht den Parteien eines Gerichtsverfahrens kein Recht auf Antragstellung hinsichtlich einer Befassung des Verfassungsgerichtshofs zu.

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10ObS63_13g`) (sent_id: `deanon_TRAIN/10ObS63_13g_167`)


Unterlässt ein Gericht die Anfechtung einer Norm beim Verfassungsgerichtshof, steht dagegen nach ständiger Rechtsprechung keiner Partei ein Rechtsmittel zu (RIS-Justiz RS0056514 [T10]).

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/4Ob23_24x`) (sent_id: `deanon_TRAIN/4Ob23_24x_31`)


Der Verwaltungsgerichtshof definiert „Handel“ als eine auf den Warenaustausch zwischen den einzelnen Wirtschaftsgliedern gerichtete gewerbsmäßige Tätigkeit (83/04/0257;

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_32`)


Mit Beschluss vom 30. März 2016 hat der Oberste Gerichtshof zu 4 Ob 31/16m ua in sechs verbundenen Verfahren, denen Sachverhalte zugrundelagen, die mit jenem dieses Verfahrens vergleichbar sind, die dort näher bezeichneten Bestimmungen des Glücksspielgesetzes und des NÖ Spielautomatengesetzes 2011 (hilfsweise die genannten Gesetze zur Gänze) beim Verfassungsgerichtshof als verfassungswidrig angefochten.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_33`)


Mit Beschluss vom 26. September 2016 unterbrach der Senat das mittlerweile anhängige Verfahren über den von der Klägerin gegen den berufungsgerichtlichen Aufhebungsbeschluss erhobenen Rekurs bis zur Entscheidung des Verfassungsgerichtshofs über den vorher erwähnten Antrag, näher bezeichnete Normen des Glücksspielrechts als verfassungswidrig aufzuheben.

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_34`)


Mit Beschluss vom 15. Oktober 2016 zu G 103 – 104/2016-49 ua wies der Verfassungsgerichtshof die Anträge des Obersten Gerichtshofs und anderer Gerichte als unzulässig zurück.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_37`)


Rechtliche Beurteilung Aufgrund der Entscheidung des Verfassungsgerichtshofs war das Rekursverfahren von Amts wegen fortzusetzen.

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_38`)


Der von der Klägerin gegen den Aufhebungsbeschluss erhobene Rekurs ist wegen der zwischenzeitlich ergangenen Entscheidungen des Verfassungsgerichtshofs vom 15. Oktober 2016 zulässig und auch berechtigt.

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_39`)


1. Mit Erkenntnis vom 15. Oktober 2016 zu E 945/2016-24 ua wies der Verfassungsgerichtshof mehrere Beschwerden ab, die gegen die gesetzliche Beschränkung des Glücksspiels gerichtet waren.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_41`)


Der Verfassungsgerichtshof ging inhaltlich davon aus, dass die Bestimmungen des GSpG allen vom EuGH aufgezeigten Vorgaben des Unionsrechts entsprechen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_46`)


2. Auch der Verwaltungsgerichtshof befasste sich inzwischen eingehend mit der Rechtsprechung des Gerichtshofs der Europäischen Union und der unionsrechtlichen Zulässigkeit von Beschränkungen der Glücksspieltätigkeiten durch das GSpG (Ro 2015/17/0022).

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_47`)


Auch der Verwaltungsgerichtshof verneinte eine Unionsrechtswidrigkeit der einschlägigen glücksspielrechtlichen Bestimmungen.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_50`)


3. Auch in der Zusammenschau mit der zitierten Entscheidung des Verwaltungsgerichtshofs erachtet der Senat durch die inhaltliche Entscheidung des Verfassungsgerichtshofs die unions- und verfassungsrechtlichen Fragen als hinreichend geklärt.

**False Positives:**

- `Verwaltungsgerichtshofs` — no gold match — likely missing annotation
- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 16** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_51`)


Ungeachtet der Zurückweisung der Anträge des Senats aus formalen Gründen ging der Verfassungsgerichtshof im Erkenntnis über die Beschwerden umfassend auf die Vorgaben des EuGH zur Unionsrechtskonformität von Glücksspielrechtsnormen und auch auf die vom Senat gegen die österreichische Rechtslage geäußerten Bedenken ein.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_12`)


2. Dabei konnte sich der Oberste Gerichtshof auf einschlägige Judikatur sowohl des Verfassungsgerichtshofs als auch des EuGH stützen: 2.1 Der Verfassungsgerichtshof hat in seinem Erkenntnis G 450/2015 ua Parteianträge von ÖBB-Bediensteten (unter anderem auch des Klägers) abgewiesen, die § 53a und § 56 Abs 18 bis 24 BundesbahnG je idF BGBl I Nr 64/2015 als verfassungswidrig aufzuheben.

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 18** (doc_id: `deanon_TRAIN/4Ob74_21t`) (sent_id: `deanon_TRAIN/4Ob74_21t_65`)


Schon deswegen ist seiner Anregung, eine Prüfung des § 2 NWG (der gar nicht die Entschädigung betrifft) durch den Verfassungsgerichtshof zu veranlassen, nicht zu folgen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/9Ob31_22g`) (sent_id: `deanon_TRAIN/9Ob31_22g_76`)


[17] Darauf, dass die sachliche Rechtfertigung von S 2 und 3 leg cit aus Anlass der Pandemie Gegenstand einer breiten literarischen Kontroverse und eines vor dem Verfassungsgerichtshof anhängigen Gesetzesprüfungsverfahrens (G 279/2021) wurde, ist im gegenwärtigen Verfahrensstadium nicht Bedacht zu nehmen, weil nach dem Vorbringen der Streitteile nicht erkennbar ist, ob hier ein Miet- oder ein Pachtverhältnis vorliegt (in den Schriftsätzen beider Parteien wurden – ebenso wie in den Parteienaussagen – beide Begriffe verwendet;

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_26`)


[7]2.2.Von diesen Grundsätzen abzugehen, besteht hier kein Anlass: [8]3.1.Der Verfassungsgerichtshof hat die Behandlung des von der Klägerin im vorliegenden Verfahren gemäß Art 140a B-VG gestellten Antrags zur Prüfung der Verfassungsmäßigkeit von Art III Abschn 9 und Art VIII Abschn 19 und 20 Amtssitzabk sowie Art XV Statuten abgelehnt (VfGH 15.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_29`)


Der Verfassungsgerichtshof hielt dafür, dass vor dem Hintergrund von Art XIX Abschn 50 lit a Amtssitzabk sowie der – von der Klägerin und Antragstellerin nicht bestrittenen – Möglichkeit, Beschwerde an das Verwaltungsgericht der Internationalen Arbeitsorganisation zu erheben (VfGH 29.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/8ObA10_24i`) (sent_id: `deanon_TRAIN/8ObA10_24i_35`)


[10]3.3.Vor diesem Hintergrund sieht sich auch der Oberste Gerichtshof durch die Rechtsprechung des Verfassungsgerichtshofs und von ihm zitierte EGMR-Judikatur referierenden Revisionsrekurs nicht veranlasst, die Verfassungsgemäßheit von Amtssitzabk und Statut als bindende Staatsverträge in Frage zu stellen (vgl Art 89 Abs 1 und 2 B-VG): Die Beklagte sieht ein mehrstufiges Beschwerdeverfahren vor, zu dem bereits sowohl der EGMR (6. 1. 2015, 415/07, Klausecker, Rz 70 ff) als auch der Verfassungsgerichtshof (29. 9. 2022, SV 1/2021, Pkt IV.2.6 aE) darauf hingewiesen haben, dass auch die Beschwerdemöglichkeit letztlich an das – von der Klägerin erneut als ungenügend vermeinte – Verwaltungsgericht der Internationalen Arbeitsorganisation bzw die Möglichkeit eines Schiedsverfahrens nach dessen Regeln ein hinreichender angemessener alternativer Streitbeilegungsmechanismus wäre.

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 23** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_85`)


Nur in diesem Fall wäre auch zu prüfen, ob § 330a ASVG unmittelbar anzuwenden wäre oder nicht vielmehr eine Anfechtung beim Verfassungsgerichtshof zu erfolgen hätte.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/10Ob14_18h`) (sent_id: `deanon_TRAIN/10Ob14_18h_65`)


1.2.2 Wie die Beklagte in ihrer Revisionsbeantwortung vorbringt, ist § 4a VZKG bereits Gegenstand eines im November 2017 von der Beklagten gemeinsam mit anderen Kreditunternehmen beim Verfassungsgerichtshof eingebrachten Individualantrags gemäß Art 140 Abs 1 Z 1 lit c B-VG, der dort zu G 293/2017 anhängig ist.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/10Ob14_18h`) (sent_id: `deanon_TRAIN/10Ob14_18h_66`)


Unter einem regt die Beklagte an, auch der Oberste Gerichtshof möge § 4 Abs 2 und § 4a VZKG nF dem Verfassungsgerichtshof zur Überprüfung gemäß Art 140 Abs 1 Z 1 lit a B-VG vorlegen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_25`)


Die darin geltend gemachten Verfassungswidrigkeiten wurden vom Verfassungsgerichtshof im Hinblick auf sein Erkenntnis vom 12.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_27`)


Hervorzuheben ist insbesondere, dass der Verfassungsgerichtshof offensichtlich auch den Umstand, dass die Beklagte nicht im Allein-, sondern im (indirekten) Mehrheitseigentum des Landes Niederösterreich steht, nicht als ausreichendes Differenzierungskriterium für eine weitere Prüfung erachtet hat.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_28`)


Auch die Ausführungen des Klägers zu einem Verstoß gegen das rechtsstaatliche Prinzip und zur mangelnden Kompetenz des Landesgesetzgebers veranlassten den Verfassungsgerichtshof nicht zur Prüfung der angefochtenen Norm.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `deanon_TRAIN/8ObA47_17w`) (sent_id: `deanon_TRAIN/8ObA47_17w_31`)


Zu deren Maßgeblichkeit nahm der Verfassungsgerichtshof bereits im erwähnten Erkenntnis vom 12.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_TRAIN/9Ob82_21f`) (sent_id: `deanon_TRAIN/9Ob82_21f_30`)


[9] Allerdings hat schon der Verfassungsgerichtshof (Beschluss vom 30. 9. 2021, V178/2021-12) zu der dort behaupteten Verletzung in den verfassungsgesetzlich gewährleisteten Rechten auf Datenschutz (§ 1 DSG) und im Recht auf Achtung des Privat- und Familienlebens (Art 8 EMRK) ausgeführt, das Vorbringen lasse die behaupteten Rechtsverletzungen als so wenig wahrscheinlich erkennen, dass der Antrag keine Aussicht auf Erfolg habe.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_67`)


RS0117084) war die Judikatur des Verfassungsgerichtshofs.

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_71`)


3.Im Anschluss an das Erkenntnis des Verfassungsgerichtshofs zu G 7/02 ua hat der Oberste Gerichtshof seine unterhaltsrechtliche Judikatur modifiziert (1 Ob 114/02z;

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_79`)


Der Verfassungsgerichtshof hat bereits ausgesprochen, dass das verfassungsrechtliche Gebot der (zureichenden) steuerlichen Entlastung von Unterhaltslasten auch im Weg einer gesetzlichen Pauschalierung erfolgen kann.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_81`)


Wenn der Gesetzgeber auf die Vorgaben durch den Verfassungsgerichtshof reagiert und den Familienbonus Plus mit der Zielsetzung eingeführt hat, dass die Unterhaltspflichtigen die Unterhaltslasten zukünftig aus ihrem unversteuerten Einkommen leisten können und nicht eine darauf leistende Steuer dazuverdienen müssen, besteht das Ziel der in Rede stehenden steuergesetzlichen Maßnahme darin, das Einkommen des Geldunterhaltspflichtigen, aus dem der Unterhalt geleistet wird, im Einklang mit den Vorgaben durch den Verfassungsgerichtshof steuerlich zu entlasten.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 35** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_82`)


Auch wenn der Gesetzgeber in den Gesetzesmaterialien nicht auf die Judikatur des Verfassungsgerichtshofs Bezug nimmt, folgt aus der ident formulierten Zielsetzung mit ausreichender Deutlichkeit, dass der Gesetzgeber den verfassungsrechtlichen Vorgaben Rechnung tragen und die gebotene steuerliche Entlastung durch die neue steuergesetzliche Maßnahme im Weg einer pauschalierenden Regelung umsetzen wollte.

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_86`)


Nach der Zielrichtung des Steuergesetzgebers soll der ausschöpfbare Teildes Familienbonus Plus in generalisierender Betrachtungsweise dazu dienen, das Unterhaltseinkommen nach den Vorgaben des Verfassungsgerichtshofs steuerfrei zu stellen.

**False Positives:**

- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_103`)


Da der Gesetzgeber bis 31. Dezember 2018 weder die vom Verfassungsgerichtshof im Erkenntnis zu B 1285/00 in den Raum gestellte pauschalierende Entlastung noch eine andere sachliche Regelung umgesetzt hat, um den verfassungsrechtlichen Vorgaben zu entsprechen, hat sich der Oberste Gerichtshof in seiner Rechtsprechung an der Ansicht des Verfassungsgerichtshofs orientiert.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation
- `Verfassungsgerichtshofs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 38** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_125`)


Die vom Verfassungsgerichtshof vorgegebene pauschalierende steuerliche Entlastung, die im Weg des Unterhaltsabsetzbetrags bisher noch nicht ausreichend erreicht wurde, ist durch die Einführung des Familienbonus Plus nunmehr als ausreichend gewährleistet anzusehen.

**False Positives:**

- `Verfassungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/10Ob7_11v`) (sent_id: `deanon_TRAIN/10Ob7_11v_36`)


3. Erstmals im Rekurs hatten die Minderjährigen vorgebracht, es sei ihrem Vater durchaus zumutbar, in sein Heimatland zurückzukehren und dort zu arbeiten, zumal vor dem Verwaltungsgerichtshof ein „Ausweisungsverfahren“ anhängig sei und er ohnehin jederzeit mit der Abschiebung bzw Ausweisung rechnen müsse.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/10Ob7_11v`) (sent_id: `deanon_TRAIN/10Ob7_11v_39`)


Ein entsprechendes Vorbringen ist dem Rekurs der Minderjährigen jedoch nicht zu entnehmen, sodass die dort erstmals aufgestellte Behauptung zur Zumutbarkeit der Rückkehr nach Bosnien bereits vor Abschluss des vor dem Verwaltungsgerichtshof anhängigen Verfahrens, eine nicht zulässige Neuerung darstellte.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/10Ob7_11v`) (sent_id: `deanon_TRAIN/10Ob7_11v_42`)


Nach den Umständen des vorliegenden Einzelfalls ließen sich nicht nur die beim Antragsgegner festgestellte geistige Behinderung als derartig berücksichtigungswürdiger Grund ins Treffen führen, sondern auch die - schon vom Rekursgericht ins Auge gefasste - Möglichkeit, dass er in dem vor dem Verwaltungsgerichtshof anhängigen Verfahren obsiegen und dann wieder über einen gültigen Aufenthaltstitel verfügen könnte.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `FAÖ Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8dea6326`  
**Description:**
Matches FAÖ acronym for Finanzamt Österreich.

**Content:**
```
(?i)\b(FA\s+Ö)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Tax Office Full Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6679487e`  
**Description:**
Matches Finanzamt followed by city and number variations, including genitive and more city patterns.

**Content:**
```
(?i)\b(Finanzamt(?:s)?\s+(?:Wien\s+(?:\d+/\d+(?:/\d+)?|9/18/19|1/23|2/20/21/22|3/6/7/11/15\s+Schwechat\s+Gerasdorf|Klosterneuburg|Braunau\s+Ried\s+Schärding|Baden\s+Mödling)|Österreich))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6540f501`  
**Description:**
Matches specific company names ending in GmbH/AG that were missed or captured incorrectly, focusing on clean name patterns.

**Content:**
```
(?i)\b((?:BDO\s+Austria\s+GmbH\s+WP-\s+u\.\s+StBges\.|LeitnerLeitner\s+GmbH\s+Wirtschaftsprüfer\s+und\s+Steuerberater|Unter\s+Donunisee\s+AG))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bankhaus Denzel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f84b7101`  
**Description:**
Matches the specific organization Bankhaus Denzel.

**Content:**
```
(?i)\b(Bankhaus\s+Denzel)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Cervenka&Neunübel Telekom AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b383f1ee`  
**Description:**
Matches the specific organization Cervenka&Neunübel Telekom AG.

**Content:**
```
(?i)\b(Cervenka&Neunübel\s+Telekom\s+AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `PSD Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4b15301e`  
**Description:**
Matches PSD Wien without capturing trailing dates.

**Content:**
```
(?i)\b(PSD\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SVS/SVB`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `dc91a3cf`  
**Description:**
Matches the specific organization SVS/SVB.

**Content:**
```
(?i)\b(SVS/SVB)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Pensionsversicherungsanstalt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `afe7e5b5`  
**Description:**
Matches the specific organization Pensionsversicherungsanstalt.

**Content:**
```
(?i)\b(Pensionsversicherungsanstalt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 8 | 363 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob13_18m`) (sent_id: `deanon_TRAIN/10Ob13_18m_9`)


Die Pensionsversicherungsanstalt hat dem Vater mit rechtskräftigem Bescheid vom 11.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/10Ob13_18m`) (sent_id: `deanon_TRAIN/10Ob13_18m_20`)


6. Die Kinder streben eine Anspannung auf das höhere Aktiveinkommen des bei der Pensionsversicherungsanstalt beschäftigt gewesenen Vaters an.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/10ObS101_10s`) (sent_id: `deanon_TRAIN/10ObS101_10s_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Hoch sowie die fachkundigen Laienrichter Dr. Erwin Blazek (aus dem Kreis der Arbeitgeber) und Dr. Rotraut Leitner (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Reneé Roeber, vertreten durch Mag. Klaus Philipp, Rechtsanwalt in Mattersburg, gegen die beklagte Partei Pensionsversicherungsanstalt, Friedrich-Hillegeist-Straße 1, 1020 Wien, vertreten durch Dr. Josef Milchram und andere Rechtsanwälte in Wien, wegen Invaliditätspension, über die Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 16. Dezember 2009, GZ 8 Rs 5/09b-42, womit infolge Berufung der beklagten Partei das Urteil des Landesgerichts Eisenstadt als Arbeits- und Sozialgericht vom 12. September 2008, GZ 23 Cgs 165/07f-20, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Reneé Roeber`(person)

**Example 3** (doc_id: `deanon_TRAIN/10ObS101_10s`) (sent_id: `deanon_TRAIN/10ObS101_10s_12`)


DasErstgerichterkannte die beklagte Pensionsversicherungsanstalt schuldig, dem Kläger die Invaliditätspension ab 1. 8. 2007 „im gesetzlichen Ausmaß“ zu gewähren.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10ObS18_12p`) (sent_id: `deanon_TRAIN/10ObS18_12p_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Dr. Hradil als Vorsitzenden, die Hofräte Dr. Fellinger und Dr. Schramm sowie die fachkundigen Laienrichter Dr. Peter Zeitler (aus dem Kreis der Arbeitgeber) und AR Angelika Neuhauser (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Techn R Sean Birtalan, vertreten durch Arnold & Arnold Rechtsanwälte in Innsbruck, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich- Hillegeist-Straße 1, wegen Invaliditätspension, infolge außerordentlicher Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 6. Dezember 2011, GZ 25 Rs 100/11h-64, womit das Urteil des Landesgerichts Innsbruck als Arbeits- und Sozialgericht vom 14. Juli 2011, GZ 16 Cgs 185/07t-59, abgeändert wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Techn R Sean Birtalan`(person)

**Example 5** (doc_id: `deanon_TRAIN/10ObS18_12p`) (sent_id: `deanon_TRAIN/10ObS18_12p_10`)


2007 lehnte die beklagte Pensionsversicherungsanstalt den Antrag des Klägers vom 19.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/10ObS110_10i`) (sent_id: `deanon_TRAIN/10ObS110_10i_5`)


Lackner, Rechtsanwälte in Leoben, gegen die beklagte Partei Pensionsversicherungsanstalt, Friedrich-Hillegeist-Straße 1, 1021 Wien, wegen Invaliditätspension, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 5. Mai 2010, GZ 7 Rs 24/10v-10, womit infolge Berufung der klagenden Partei das Urteil des Landesgerichts Leoben als Arbeits- und Sozialgericht vom 3. Februar 2010, GZ 21 Cgs 246/09p-6, bestätigt wurde, in nichtöffentlicher Sitzung zu Recht erkannt:  Spruch

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/10ObS92_17b`) (sent_id: `deanon_TRAIN/10ObS92_17b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, den Hofrat Dr. Schramm und die Hofrätin Dr. Fichtenau sowie die fachkundigen Laienrichter Dr. Gabriele Griehsel (aus dem Kreis der Arbeitgeber) und Dr. Wolfgang Kozak (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Sozialrechtssache der klagenden Partei Dr.in Gerlinde Saltzmann, vertreten durch Mahringer Steinwender Bestebner Rechtsanwälte OG in Salzburg, gegen die beklagte Partei Pensionsversicherungsanstalt, 1021 Wien, Friedrich-Hillegeist-Straße 1, wegen Berufsunfähigkeitspension, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 15. Mai 2017, GZ 11 Rs 22/17k-36, mit dem das Urteil des Landesgerichts Salzburg als Arbeits- und Sozialgericht vom 21. Dezember 2016, GZ 18 Cgs 62/15y-32, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revision wird Folge gegeben.

**False Positives:**

- `Pensionsversicherungsanstalt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr.in Gerlinde Saltzmann`(person)

</details>

---

## `Psychiatrie Otto Wagner Spital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `da45d319`  
**Description:**
Matches the specific organization Psychiatrie Otto Wagner Spital.

**Content:**
```
(?i)\b(Psychiatrie\s+Otto\s+Wagner\s+Spital)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schweizerischen Unfallversicherungsanstalt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b4cc5bc9`  
**Description:**
Matches the specific organization Schweizerischen Unfallversicherungsanstalt.

**Content:**
```
(?i)\b(Schweizerischen\s+Unfallversicherungsanstalt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ÖGK`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bb128e54`  
**Description:**
Matches the specific organization ÖGK.

**Content:**
```
(?i)\b(ÖGK)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 107 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9ObA66_24g`) (sent_id: `deanon_TRAIN/9ObA66_24g_28`)


[7] Nach Ende der Entgeltfortzahlung habe die Klägerin von 2. 12. 2021 bis 28. 2. 2023 Krankengeld von der ÖGK bezogen.

**False Positives:**

- `ÖGK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/17Ob5_24w`) (sent_id: `deanon_TRAIN/17Ob5_24w_20`)


Indem die Vorinstanzen weiters auf die umfassenden vertraglichen Auskunfts- und Einsichtsrechte der Beklagten, ihre Stellung als „Hausbank“ sowie die (tatsächlich nicht gestundeten) Forderungen des Finanzamts und der ÖGK abstellten und davon ausgehend zumindest eine fahrlässige Unkenntnis der Beklagten bejahten, bewegen sie sich innerhalb des ihnen im Einzelfall notwendiger Weise zukommenden Beurteilungsspielraums (vgl RS0064794).

**False Positives:**

- `ÖGK` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bundesministers für Arbeit, Soziales und Konsumentenschutz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `51ec1b4f`  
**Description:**
Matches the specific organization Bundesministers für Arbeit, Soziales und Konsumentenschutz.

**Content:**
```
(?i)\b(Bundesministers\s+für\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesamtes für Soziales und Behindertenwesen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `889f2d6d`  
**Description:**
Matches the specific organization Bundesamtes für Soziales und Behindertenwesen.

**Content:**
```
(?i)\b(Bundesamtes\s+für\s+Soziales\s+und\s+Behindertenwesen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `PSD Wien Full`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `28f19383`  
**Description:**
Matches PSD Wien and its variations including Ambulatorium and location details.

**Content:**
```
(?i)\b(PSD\s+Wien(?:\s+(?:Ambulatorium|Zentrum|Institut))?\s+(?:Landstraße|Wien|\d+\s+\d+)?(?:\s+\d{4})?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SUVA`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `792a89b9`  
**Description:**
Matches Schweizerische Unfallversicherungsanstalt and its acronym SUVA.

**Content:**
```
(?i)\b(Schweizerische\s+Unfallversicherungsanstalt(?:\s*\(\s*SUVA\s*\))?|SUVA)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Städtische`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `02e7f811`  
**Description:**
Matches Wiener Städtische Versicherung.

**Content:**
```
(?i)\b(Wiener\s+Städtische(?:\s+Versicherung)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Allianz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c9b68ce0`  
**Description:**
Matches Allianz.

**Content:**
```
(?i)\b(Allianz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AMS Österreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `795ef291`  
**Description:**
Matches AMS Österreich.

**Content:**
```
(?i)\b(AMS\s+Österreich)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6ef38387`  
**Description:**
Matches Finanzamt followed by specific Austrian locations not covered by the general rule.

**Content:**
```
(?i)\b(Finanzamt\s+(?:Waldviertel|Braunau\s+Ried\s+Schärding|Baden\s+Mödling|Wien\s+(?:\d+/\d+(?:/\d+)?|9/18/19|1/23|2/20/21/22|3/6/7/11/15\s+Schwechat\s+Gerasdorf|Klosterneuburg)))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verwaltungsgerichtshof Genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6c39efd8`  
**Description:**
Matches Verwaltungsgerichtshof and its genitive form Verwaltungsgerichtshofes.

**Content:**
```
(?i)\b(Verwaltungsgerichtshof(?:es)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 394 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/4Ob23_24x`) (sent_id: `deanon_TRAIN/4Ob23_24x_31`)


Der Verwaltungsgerichtshof definiert „Handel“ als eine auf den Warenaustausch zwischen den einzelnen Wirtschaftsgliedern gerichtete gewerbsmäßige Tätigkeit (83/04/0257;

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_46`)


2. Auch der Verwaltungsgerichtshof befasste sich inzwischen eingehend mit der Rechtsprechung des Gerichtshofs der Europäischen Union und der unionsrechtlichen Zulässigkeit von Beschränkungen der Glücksspieltätigkeiten durch das GSpG (Ro 2015/17/0022).

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/4Ob174_16s`) (sent_id: `deanon_TRAIN/4Ob174_16s_47`)


Auch der Verwaltungsgerichtshof verneinte eine Unionsrechtswidrigkeit der einschlägigen glücksspielrechtlichen Bestimmungen.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Ob7_11v`) (sent_id: `deanon_TRAIN/10Ob7_11v_36`)


3. Erstmals im Rekurs hatten die Minderjährigen vorgebracht, es sei ihrem Vater durchaus zumutbar, in sein Heimatland zurückzukehren und dort zu arbeiten, zumal vor dem Verwaltungsgerichtshof ein „Ausweisungsverfahren“ anhängig sei und er ohnehin jederzeit mit der Abschiebung bzw Ausweisung rechnen müsse.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/10Ob7_11v`) (sent_id: `deanon_TRAIN/10Ob7_11v_39`)


Ein entsprechendes Vorbringen ist dem Rekurs der Minderjährigen jedoch nicht zu entnehmen, sodass die dort erstmals aufgestellte Behauptung zur Zumutbarkeit der Rückkehr nach Bosnien bereits vor Abschluss des vor dem Verwaltungsgerichtshof anhängigen Verfahrens, eine nicht zulässige Neuerung darstellte.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/10Ob7_11v`) (sent_id: `deanon_TRAIN/10Ob7_11v_42`)


Nach den Umständen des vorliegenden Einzelfalls ließen sich nicht nur die beim Antragsgegner festgestellte geistige Behinderung als derartig berücksichtigungswürdiger Grund ins Treffen führen, sondern auch die - schon vom Rekursgericht ins Auge gefasste - Möglichkeit, dass er in dem vor dem Verwaltungsgerichtshof anhängigen Verfahren obsiegen und dann wieder über einen gültigen Aufenthaltstitel verfügen könnte.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bundesfinanzgericht Genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bf0fb385`  
**Description:**
Matches Bundesfinanzgericht and its genitive forms.

**Content:**
```
(?i)\b(Bundesfinanzgericht(?:es|s|en)?s?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verwaltungsgericht Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a2941eba`  
**Description:**
Matches Verwaltungsgericht Wien.

**Content:**
```
(?i)\b(Verwaltungsgericht\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FH Kärnten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ee617819`  
**Description:**
Matches FH Kärnten and Fachhochschule Kärnten.

**Content:**
```
(?i)\b(FH\s+Kärnten|Fachhochschule\s+Kärnten)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Karl-Franzens-Universität Graz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ab8984cb`  
**Description:**
Matches Karl-Franzens-Universität Graz.

**Content:**
```
(?i)\b(Karl-Franzens-\s+Universität\s+Graz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BMI`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ba5057d8`  
**Description:**
Matches BMI acronym.

**Content:**
```
(?i)\b(BMI)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ernst & Young`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cf304c34`  
**Description:**
Matches Ernst & Young Steuerberatungsgesellschaft m.b.H. and variations.

**Content:**
```
(?i)\b(Ernst\s+&\s+Young\s+Steuerberatungsgesellschaft\s+m\.b\.H\.?|Ernst\s+&\s+Young\s+Steuerberatungs-GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Sozialversicherungsanstalt der Bauern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `c66a408f`  
**Description:**
Matches Sozialversicherungsanstalt der Bauern.

**Content:**
```
(?i)\b(Sozialversicherungsanstalt\s+der\s+Bauern)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Frontex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7f289fd9`  
**Description:**
Matches Frontex and its full name variations.

**Content:**
```
(?i)\b(Frontex|Europäische\s+Grenzschutzagentur(?:\s+Frontex)?|Europäischer\s+Grenzschutzagentur(?:\s+Frontex)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `University St Gallen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `47ffa6cc`  
**Description:**
Matches Universität St. Gallen variations.

**Content:**
```
(?i)\b(Universität\s+(?:in\s+)?St\.\s+Gallen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `University Innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e768a07c`  
**Description:**
Matches Universität Innsbruck.

**Content:**
```
(?i)\b(Universität\s+Innsbruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `University Vienna`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `24b26279`  
**Description:**
Matches Wirtschaftsuniversität Wien.

**Content:**
```
(?i)\b(Wirtschaftsuniversität\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fachhochschule Wiener Neustadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `84373d73`  
**Description:**
Matches Fachhochschule Wiener Neustadt and FH variants, including the full name with 'GmbH'.

**Content:**
```
(?i)\b(Fachhochschule\s+Wiener\s+Neustadt|FH\s+Wiener\s+Neustadt|FH\s+Campus\s+Wien|FH\s+Wiener\s+Neustadt\s+für\s+Wirtschaft\s+und\s+Technik\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzpolizei`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `536f6ad9`  
**Description:**
Matches Finanzpolizei followed by location.

**Content:**
```
(?i)\b(Finanzpolizei\s+[A-Z][a-z]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BM für Inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `845dd97e`  
**Description:**
Matches BM für Inneres and Bundesministerium für Inneres.

**Content:**
```
(?i)\b(BM\s+für\s+Inneres|Bundesministerium\s+für\s+Inneres)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `OECD`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e0b92186`  
**Description:**
Matches OECD acronym.

**Content:**
```
(?i)\b(OECD)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `EASO`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9c752792`  
**Description:**
Matches EASO acronym.

**Content:**
```
(?i)\b(EASO)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kriminalpolizei`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5f78c131`  
**Description:**
Matches Kriminalpolizei in Österreich.

**Content:**
```
(?i)\b(Kriminalpolizei\s+in\s+Österreich)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Airport Munich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bfdeb8eb`  
**Description:**
Matches Flughafen München.

**Content:**
```
(?i)\b(Flughafen\s+München)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Law Firm GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f87dc614`  
**Description:**
Matches law firms ending in Rechtsanwält... GmbH/OG.

**Content:**
```
(?i)(?<![a-zäöüß\s])([A-Z][a-z]+(?:\s+&\s+[A-Z][a-z]+)*\s+Rechtsanwälte\s+(?:OG|GmbH|GmbH\s*&\s*Co\.\s*KG))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 4 | 0 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 4 | 289 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/7Ob11_22a`) (sent_id: `deanon_TRAIN/7Ob11_22a_6`)


IT Sudtraver GmbH, Wald-Marine, und 2. Tal Seewil GmbH, Grappaweg 1, 5310 Hof, Österreich, beide vertreten durch die DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Herausgabe und Feststellung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2021, GZ 4 R 149/21s-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Tessbach Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `IT Sudtraver GmbH`(organisation)
- `Wald-Marine`(organisation)
- `Tal Seewil GmbH`(organisation)
- `Grappaweg 1, 5310 Hof, Österreich`(address)

**Example 1** (doc_id: `deanon_TRAIN/9Ob67_09g`) (sent_id: `deanon_TRAIN/9Ob67_09g_5`)


Babette Wienkemeier, 3. HR Dario Litwinowa, 4. Eigenbrod Versicherung GmbH & Co KG, Dr. Franz Stumpf-Straße 48, 2002 Ottendorf, Österreich, 5. Dr. David Alswede, 6. Dipl.-Ing. Manuela Himmel, vertreten durch die Gassauer-Fleissner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Ing. Felizia Tscherning, vertreten durch Mag. Markus Adam, Rechtsanwalt in Wien, wegen Räumung (Streitwert 8.954,16 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 16. Juni 2009, GZ 41 R 98/09d-12, womit das Urteil des Bezirksgerichts Innere Stadt Wien vom 26. Februar 2009, GZ 30 C 200/08y-7, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Fleissner Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Babette Wienkemeier`(person)
- `HR Dario Litwinowa`(person)
- `Eigenbrod Versicherung GmbH`(organisation)
- `Dr. Franz Stumpf-Straße 48, 2002 Ottendorf, Österreich`(address)
- `Dr. David Alswede`(person)
- `Dipl.-Ing. Manuela Himmel`(person)
- `Ing. Felizia Tscherning`(person)

**Example 2** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ulm Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Janet Henken`(person)
- `Elvira Nossal`(person)

**Example 3** (doc_id: `deanon_TRAIN/10Ob22_25w`) (sent_id: `deanon_TRAIN/10Ob22_25w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Pflegschaftssache der minderjährigen Lorenz Leimbrock, geboren am 27. September 2021, wohnhaft bei der Mutter MedR Franka Bimboese, vertreten durch die Pacher & Partner Rechtsanwälte GmbH & Co KG in Graz, wegen Unterhalt, über den Revisionsrekurs des Vaters Konrad Czeponik, vertreten durch die Prutsch-Lang & Damitner Rechtsanwälte OG in Graz, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 17. Jänner 2025, GZ 2 R 18/25v-17, mit dem der Beschluss des Bezirksgerichts Graz-Ost vom 29. November 2024, GZ 256 Pu 85/24f-8, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und die Revisionsrekursbeantwortung werden zurückgewiesen.

**False Positives:**

- `Lang & Damitner Rechtsanwälte OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lorenz Leimbrock`(person)
- `27. September`(date)
- `MedR Franka Bimboese`(person)
- `Konrad Czeponik`(person)

</details>

---

## `Tax Office Acronym FA`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cf7294ba`  
**Description:**
Matches FA followed by city/region, ensuring no trailing words are included and handling multiple city names.

**Content:**
```
(?i)\b(FA\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KQPC Versand GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `106961eb`  
**Description:**
Matches the specific company KQPC Versand GMBH.

**Content:**
```
(?i)\b(KQPC\s+Versand\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Event Sudkraftlex GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `bb73a27c`  
**Description:**
Matches the specific company Event Sudkraftlex GMBH.

**Content:**
```
(?i)\b(Event\s+Sudkraftlex\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Sudver Handel Services GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4837153a`  
**Description:**
Matches the specific company Sudver Handel Services GMBH.

**Content:**
```
(?i)\b(Sudver\s+Handel\s+Services\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Glanznorost Institut GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `75d5c666`  
**Description:**
Matches the specific company Glanznorost Institut GMBH.

**Content:**
```
(?i)\b(Glanznorost\s+Institut\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiener Städtischen Versicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1ef06fbd`  
**Description:**
Matches Wiener Städtischen Versicherung.

**Content:**
```
(?i)\b(Wiener\s+Städtischen\s+Versicherung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Federal Administrative Court Acronym FAG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `a323131b`  
**Description:**
Matches FAG acronym for Finanzamt für Groβbetriebe or similar federal administrative court contexts.

**Content:**
```
(?i)\b(FAG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `COFAG Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e2a7df51`  
**Description:**
Matches COFAG acronym for Corona-Fonds-Ausgleichs-Gesellschaft.

**Content:**
```
(?i)\b(COFAG|Cofag)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BHAG Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4c2b96d5`  
**Description:**
Matches BHAG acronym.

**Content:**
```
(?i)\b(BHAG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `District Court Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `4a197a40`  
**Description:**
Matches Bezirksgericht followed by location, handling 'BG' abbreviation.

**Content:**
```
(?i)\b(?:Bezirksgericht\s+([A-Za-zäöüÄÖÜ]+|\w+)|BG\s+Bezirksgericht\s+([A-Za-zäöüÄÖÜ]+|\w+))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 133 | 0 | 133 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 133 | 396 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Kalivoda als Vorsitzende und den Hofräten Hon.-Prof. Dr. Höllwerth und Mag. Dr. Wurdinger als weitere Richter in der Rechtssache der klagenden Partei VetR Nadja Kovalskiy, vertreten durch Dr. Günther Ledolter, Rechtsanwalt in Graz, gegen die beklagte Partei Kraftfenheim AG, Kordelia Weinmeister, LLB, vertreten durch Dr. Matthias Bacher, Rechtsanwalt in Wien, wegen 3.849,91 EUR sA und Feststellung, AZ 11 C 688/19b des Bezirksgerichts Leopoldstadt, infolge Delegierungsantrags der klagenden Partei den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Leopoldstadt zurückgestellt.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Nadja Kovalskiy`(person)
- `Kraftfenheim AG`(organisation)
- `Kordelia Weinmeister, LLB`(person)

**Example 1** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_5`)


Er brachte die Klage zunächst beim Bezirksgericht Graz-Ost ein, welches die Klage wegen örtlicher Unzuständigkeit zurück- und infolge Überweisungsantrags des Klägers an das Bezirksgericht Leopoldstadt überwies.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation
- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 2** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_7`)


Der Kläger stellte den Antrag auf Delegierung der Rechtssache an das Bezirksgericht Graz-Ost.

**False Positives:**

- `Bezirksgericht Graz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_8`)


Das Bezirksgericht Leopoldstadt legte den Akt – entgegen § 31 Abs 3 JN – ohne Äußerung und vor Erledigung der von der Beklagten erhobenen Unzuständigkeitseinrede vor.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_9`)


Der erkennende Senat stellte die Akten dem Bezirksgericht Leopoldstadt ohne Entscheidung über den Delegierungsantrag zurück und führte aus, dass eine Entscheidung über diesen Antrag erst nach rechtskräftiger Entscheidung über die Stattgebung oder Ablehnung der Unzuständigkeitseinrede erfolgen könne (RS0046338; RS0109369).

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_11`)


Das Bezirksgericht Leopoldstadt schränkte die folgende Tagsatzung auf die Frage der Zuständigkeit ein.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_13`)


Das Bezirksgericht Leopoldstadt sprach daraufhin in der Tagsatzung seine Unzuständigkeit aus und überwies die Rechtssache an das nicht offenbar unzuständige Bezirksgericht für Handelssachen Wien.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation
- `Bezirksgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 7** (doc_id: `deanon_TRAIN/7Nc6_20x`) (sent_id: `deanon_TRAIN/7Nc6_20x_15`)


Das Bezirksgericht Leopoldstadt legte den Akt neuerlich – entgegen § 31 Abs 3 JN – ohne Äußerung dem Obersten Gerichtshof vor.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/1Ob167_22y`) (sent_id: `deanon_TRAIN/1Ob167_22y_6`)


Das Bezirksgericht Liezen gab dem – von der Klägerin mit 8.000 EUR bewerteten – Unterlassungsbegehren statt.

**False Positives:**

- `Bezirksgericht Liezen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/14Ns25_17p`) (sent_id: `deanon_TRAIN/14Ns25_17p_3`)


Kopf Der Oberste Gerichtshof hat am 23. Mai 2017 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Philipp als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Mag. Hetlinger, die Hofräte des Obersten Gerichtshofs Dr. Nordmeyer und Dr. Oshidari sowie die Hofrätin des Obersten Gerichtshofs Dr. Mann in Gegenwart der Richteramtsanwärterin Mag. Melounek als Schriftführerin in der Strafsache gegen Fabiano Pflichtbeil wegen Vergehen der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB in dem zu AZ 3 U 21/17x des Bezirksgerichts Lienz und zu AZ 5 U 52/17h des Bezirksgerichts Wiener Neustadt geführten Kompetenzkonflikt nach Anhörung der Generalprokuratur in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Hauptverfahren ist vom Bezirksgericht Wiener Neustadt zu führen.

**False Positives:**

- `Bezirksgericht Wiener` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pflichtbeil`(person)

**Example 10** (doc_id: `deanon_TRAIN/14Ns25_17p`) (sent_id: `deanon_TRAIN/14Ns25_17p_4`)


Gründe:  Rechtliche Beurteilung Mit am 24. Februar 2015 beim Bezirksgericht Lienz eingebrachtem Strafantrag (ON 13) legte die Staatsanwaltschaft Innsbruck Fabiano Pierskala zur Last, er habe seine im Familienrecht begründete Unterhaltspflicht gegenüber Leonardo Mehltreter in den Zeiträumen 1. bis 31. März 2015, 1. bis 30. Juni 2015 und 1. August 2015 bis 3. November 2016 gröblich verletzt, und erachtete durch dieses Verhalten „das“ (richtig: mehrere) Vergehen der Verletzung der Unterhaltspflicht nach § 198 Abs 1 StGB verwirklicht.

**False Positives:**

- `Bezirksgericht Lienz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/14Ns25_17p`) (sent_id: `deanon_TRAIN/14Ns25_17p_5`)


Das Bezirksgericht Lienz überwies die Sache wegen örtlicher Unzuständigkeit dem Bezirksgericht Wiener Neustadt (§ 38 erster Satz StPO).

**False Positives:**

- `Bezirksgericht Lienz` — no gold match — likely missing annotation
- `Bezirksgericht Wiener` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 12** (doc_id: `deanon_TRAIN/3Nc29_25g`) (sent_id: `deanon_TRAIN/3Nc29_25g_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Brenn als Vorsitzenden sowie die Hofrätinnen Dr. Weixelbraun-Mohr und Dr. Kodek als weitere Richter in der Ordinationssache der betreibenden Partei Shirley Pothen, vertreten durch die Summer Schertler Kaufmann Rechtsanwälte GmbH in Bregenz, gegen die verpflichtete Partei Haenssel Landwirtschaft Limited, Mag. Linus Stadlmayr, Malta, wegen 12.985 EUR sA, über den Antrag auf Ordination nach § 28 JN den Beschluss gefasst:  Spruch Für die Bewilligung und den Vollzug der von der betreibenden Partei beabsichtigten Forderungsexekution wird das Bezirksgericht Neulengbach als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Neulengbach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Shirley Pothen`(person)
- `Haenssel Landwirtschaft Limited`(organisation)
- `Mag. Linus Stadlmayr`(person)

**Example 13** (doc_id: `deanon_TRAIN/3Nc29_25g`) (sent_id: `deanon_TRAIN/3Nc29_25g_41`)


Unter Bedachtnahme auf die maßgeblichen Kriterien der Sach- und Parteinähe bzw der Zweckmäßigkeit (vgl RS0106680 [T13]) ist im Hinblick auf den Wohnsitz des Betreibenden das Bezirksgericht Neulengbach als zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht Neulengbach` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/7Nc12_12t`) (sent_id: `deanon_TRAIN/7Nc12_12t_3`)


Kopf Der Oberste Gerichtshof hat durch die Vizepräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Hoch und Mag. Dr. Wurdinger als weitere Richter in der beim Bezirksgericht Bludenz zu AZ 3 C 316/12h anhängigen Rechtssache der klagenden Partei ÖkR Serena Henings, vertreten durch Dr. Michael Battlogg, Rechtsanwalt in Schruns, gegen die beklagten Parteien 1. James Goepfardt, und 2. Hon.-Prof.in Frederike Bonfiglioli, LLB, beide vertreten durch Mag. Gerhard Franz Köstner, Rechtsanwalt in Altenmarkt im Pongau, wegen 1.871,94 EUR sA, über den Delegierungsantrag der beklagten Parteien gemäß § 31 JN den Beschluss gefasst:  Spruch Der Antrag der beklagten Parteien, die Rechtssache an das Bezirksgericht Saalfelden zu delegieren, wird abgewiesen.

**False Positives:**

- `Bezirksgericht Bludenz` — no gold match — likely missing annotation
- `Bezirksgericht Saalfelden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `ÖkR Serena Henings`(person)
- `James Goepfardt`(person)
- `Hon.-Prof.in Frederike Bonfiglioli, LLB`(person)

**Example 15** (doc_id: `deanon_TRAIN/7Nc12_12t`) (sent_id: `deanon_TRAIN/7Nc12_12t_12`)


Sie stellten den Antrag auf Delegierung der Rechtssache an das Bezirksgericht Saalfelden.

**False Positives:**

- `Bezirksgericht Saalfelden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/3Nc12_20z`) (sent_id: `deanon_TRAIN/3Nc12_20z_5`)


Das Bezirksgericht Telfs legte den Akt dem Obersten Gerichtshof nach rechtskräftiger Verneinung der örtlichen Zuständigkeit über Antrag des Betreibenden zwecks Entscheidung über eine Ordination nach § 28 JN (neuerlich) vor.

**False Positives:**

- `Bezirksgericht Telfs` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/10Nc8_22s`) (sent_id: `deanon_TRAIN/10Nc8_22s_8`)


[2] Das Bezirksgericht Schwechat erklärte sich für international unzuständig.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/10Nc8_22s`) (sent_id: `deanon_TRAIN/10Nc8_22s_10`)


[3] Nach Rechtskraft des Zurückweisungsbeschlusses legte das Bezirksgericht Schwechat den Akt zur Entscheidung über den vom Kläger in der Klage und im Rekurs hilfsweise gestellten Ordinationsantrag nach § 28 JN vor.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/9ObA139_19k`) (sent_id: `deanon_TRAIN/9ObA139_19k_4`)


Das Bezirksgericht Linz wird ersucht, das gefertigte Gericht vom Ausgang des Pflegschaftsverfahrens AZ 38 P 208/19y bzw den getroffenen Maßnahmen zu verständigen.

**False Positives:**

- `Bezirksgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `deanon_TRAIN/9ObA139_19k`) (sent_id: `deanon_TRAIN/9ObA139_19k_12`)


Zur Prüfung der Notwendigkeit der Bestellung eines gerichtlichen Erwachsenenvertreters für den Antragsteller ist beim Bezirksgericht Linz zu AZ 38 P 208/19y ein Pflegschaftsverfahren anhängig.

**False Positives:**

- `Bezirksgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/9Ob66_19z`) (sent_id: `deanon_TRAIN/9Ob66_19z_7`)


Text Begründung: Mit seiner beim Bezirksgericht Zell am See (Aufnahmegericht des Bezirksgerichts Saalfelden) am 11.

**False Positives:**

- `Bezirksgericht Zell` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/9Ob66_19z`) (sent_id: `deanon_TRAIN/9Ob66_19z_9`)


Die Streitteile hätten in den (mit der Klage vorgelegten) Werkverträgen als vereinbarten Gerichtsstand das Bezirksgericht Saalfelden vereinbart.

**False Positives:**

- `Bezirksgericht Saalfelden` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/9Ob66_19z`) (sent_id: `deanon_TRAIN/9Ob66_19z_18`)


§ 104 Abs 2 S 2 JN sieht nur insofern eine Einschränkung vor, als Angelegenheiten, welche dem Wirkungskreis der ordentlichen Gerichte überhaupt entzogen sind, durch solche Vereinbarungen nicht vor diese Gerichte, Rechtssachen, welche vor ein Bezirksgericht gehören, nicht vor einen Gerichtshof erster Instanz und ausschließlich den Gerichtshöfen erster Instanz zugewiesene Streitigkeiten nicht vor ein Bezirksgericht gebracht werden können.

**False Positives:**

- `Bezirksgericht gehören` — no gold match — likely missing annotation
- `Bezirksgericht gebracht` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 24** (doc_id: `deanon_TRAIN/9Ob66_19z`) (sent_id: `deanon_TRAIN/9Ob66_19z_21`)


Im vorliegenden Fall haben die Parteien ausdrücklich vereinbart, dass bei eventuellen Streitigkeiten aus den vom Kläger genannten Werkverträgen als vereinbarter Gerichtsstand das Bezirksgericht Saalfelden (nunmehr: Bezirksgericht Zell am See) gilt.

**False Positives:**

- `Bezirksgericht Saalfelden` — no gold match — likely missing annotation
- `Bezirksgericht Zell` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 25** (doc_id: `deanon_TRAIN/9Ob66_19z`) (sent_id: `deanon_TRAIN/9Ob66_19z_31`)


Im vorliegenden Fall haben die Parteien für ihre Streitigkeiten jedoch auch den Gerichtstyp bestimmt und ein konkretes Bezirksgericht genannt.

**False Positives:**

- `Bezirksgericht genannt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/5Nc6_11v`) (sent_id: `deanon_TRAIN/5Nc6_11v_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden und die Hofrätin Dr. Hurch sowie den Hofrat Dr. Höllwerth als weitere Richter in der Rechtssache der klagenden Partei Ing. Manfred Singwald, vertreten durch Mag. Robert Benedikt, Rechtsanwalt in Wien, gegen die beklagte Partei Werkbruck Lebensmittel GmbH, Laurin Mertensmeyer, vertreten durch Dr. Felix Graf, Rechtsanwalt in Feldkirch, wegen Aufhebung eines Vertrags und 5.801 EUR sA, über den Antrag der klagenden Partei auf Bestimmung der Zuständigkeit nach § 28 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung über die zu AZ 6 C 217/10p des Bezirksgerichts Leibnitz eingebrachte Klage wird das Bezirksgericht Leibnitz als örtlich zuständiges Gericht bestimmt.

**False Positives:**

- `Bezirksgericht Leibnitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Singwald`(person)
- `Werkbruck Lebensmittel GmbH`(organisation)
- `Laurin Mertensmeyer`(person)

**Example 27** (doc_id: `deanon_TRAIN/5Nc6_11v`) (sent_id: `deanon_TRAIN/5Nc6_11v_5`)


11. 2010 beim Bezirksgericht Leibnitz eingebrachten Klage gestützt (insbesondere) auf Irrtum die (ex tunc) Aufhebung eines von ihm als Verbraucher mit der Beklagten als Unternehmer über deren - zwischenzeitig bereits wieder aus dem Firmenbuch gelöschten - Zweigniederlassung in Bürs (Vorarlberg) abgeschlossenen Klientenvertrags und die Rückzahlung von ihm geleisteter Betreuungsgebühren in Höhe des Klagsbetrags.

**False Positives:**

- `Bezirksgericht Leibnitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/5Nc6_11v`) (sent_id: `deanon_TRAIN/5Nc6_11v_10`)


Der Kläger begehrte daraufhin für den Fall der rechtskräftigen Verneinung der örtlichen Zuständigkeit durch das angerufene Bezirksgericht die Aktenvorlage an den Obersten Gerichtshof mit dem Antrag, gemäß § 28 JN das Bezirksgericht Leibnitz als örtlich zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht die` — no gold match — likely missing annotation
- `Bezirksgericht Leibnitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 29** (doc_id: `deanon_TRAIN/5Nc6_11v`) (sent_id: `deanon_TRAIN/5Nc6_11v_11`)


Das Bezirksgericht Leibnitz schränkte die Verhandlung gemäß § 189 ZPO auf die Zuständigkeitsfrage ein und sprach sodann mit Beschluss vom 24.

**False Positives:**

- `Bezirksgericht Leibnitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_TRAIN/5Nc6_11v`) (sent_id: `deanon_TRAIN/5Nc6_11v_15`)


1.Das Bezirksgericht Leibnitz hat vor der Aktenvorlage - bestehender höchstgerichtlicher Rechtsprechung (RIS-Justiz RS0046344) folgend - die von der Beklagten erhobene Unzuständigkeitseinrede erledigt und dabei seine örtliche Zuständigkeit verneint.

**False Positives:**

- `Bezirksgericht Leibnitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/5Nc6_11v`) (sent_id: `deanon_TRAIN/5Nc6_11v_30`)


Die Parteinähe spricht daher nach dem derzeitigen Verfahrensstand für das Bezirksgericht Leibnitz.

**False Positives:**

- `Bezirksgericht Leibnitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/5Nc6_11v`) (sent_id: `deanon_TRAIN/5Nc6_11v_31`)


Sonstige, insbesondere unter den Gesichtspunkten der Zweckmäßigkeit und Verfahrensökonomie maßgebliche Umstände, die - überwiegend - für ein anderes Gericht, namentlich für das von der Beklagten präferierte Bezirksgericht Bludenz sprechen würden, sind demgegenüber auf der Grundlage des derzeitigen Aktenstandes nicht zu erkennen.

**False Positives:**

- `Bezirksgericht Bludenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `deanon_TRAIN/5Nc6_11v`) (sent_id: `deanon_TRAIN/5Nc6_11v_32`)


Es war somit spruchgemäß das Bezirksgericht Leibnitz als örtlich zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht Leibnitz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_TRAIN/7Ob58_15b`) (sent_id: `deanon_TRAIN/7Ob58_15b_4`)


Text Begründung: Das Bezirksgericht Vöcklabruck gab dem vom Antragsteller gegen die Richterin Dr. Nikolai Hopfstock erhobenen Ablehnungsantrag nicht Folge.

**False Positives:**

- `Bezirksgericht Vöcklabruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Nikolai Hopfstock`(person)

**Example 35** (doc_id: `deanon_TRAIN/10Nc38_19y`) (sent_id: `deanon_TRAIN/10Nc38_19y_4`)


Text Begründung: Der in 1050 Wien wohnhafteKlägerbegehrte mit seiner beim Bezirksgericht Schwechat eingebrachten Klage, das beklagte Luftfahrtunternehmen gemäß Art 4 Abs 3 iVm Art 7 der Verordnung (EG) Nr 261/2004 (FluggastrechteVO) zur Zahlung eines Ausgleichsanspruchs in Höhe von 600 EUR sowie zur Zahlung von Unterstützungsleistungen gemäß Art 4 iVm Art 8 und 9 der FluggastrechteVO zu verpflichten.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_TRAIN/10Nc38_19y`) (sent_id: `deanon_TRAIN/10Nc38_19y_26`)


Hilfsweise zu seinem Rekursantrag stellte der Kläger den an den Obersten Gerichtshof gerichtetenAntrag, eine Ordination des Rechtsstreits an das Bezirksgericht für Handelssachen Wien gemäß § 28 JNvorzunehmen.

**False Positives:**

- `Bezirksgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_TRAIN/10Nc38_19y`) (sent_id: `deanon_TRAIN/10Nc38_19y_41`)


Da das Bezirksgericht Schwechat die Klage wegen fehlender internationaler Zuständigkeit zurückgewiesen hat, kann eine Ordination nicht auf § 28 Abs 1 Z 1 JN gestützt werden.

**False Positives:**

- `Bezirksgericht Schwechat` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/10Nc17_20m`) (sent_id: `deanon_TRAIN/10Nc17_20m_5`)


12. 2006 zur Einführung eines Europäischen Mahnverfahrens (EuMahnVO) vor dem Bezirksgericht für Handelssachen Wien einzuleiten.

**False Positives:**

- `Bezirksgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/10Nc17_20m`) (sent_id: `deanon_TRAIN/10Nc17_20m_24`)


Dennoch ist der Ordinationsantrag zurückzuweisen: [7] 2.1 Über das Verfahren nach der Europäischen Mahnverordnung ist in Österreich nach § 252 Abs 2 ZPO ausschließlich das Bezirksgericht für Handelssachen Wien zuständig.

**False Positives:**

- `Bezirksgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/9Nc15_14a`) (sent_id: `deanon_TRAIN/9Nc15_14a_4`)


Wendelin Niemands, geboren am 18. Januar 1997, 2. Laura Hynek, geboren am 5. April 2008, und 3. Moritz Netz, geboren am 8. Oktober 2009, AZ 4 PS 106/14f des Bezirksgerichts Innsbruck, infolge Vorlage zur Genehmigung der Übertragung gemäß § 111 JN an das Bezirksgericht Favoriten den Beschluss gefasst:  Spruch Der Akt wird dem Bezirksgericht Innsbruck zurückgestellt.

**False Positives:**

- `Bezirksgericht Favoriten` — no gold match — likely missing annotation
- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Wendelin Niemands`(person)
- `18. Januar`(date)
- `Laura Hynek`(person)
- `5. April`(date)
- `Moritz Netz`(person)
- `8. Oktober`(date)

**Example 41** (doc_id: `deanon_TRAIN/9Nc15_14a`) (sent_id: `deanon_TRAIN/9Nc15_14a_5`)


Text Begründung: Das Bezirksgericht Innsbruck übertrug mit seinem - den Verfahrensbeteiligten noch nicht zugestellten - Beschluss vom 2.

**False Positives:**

- `Bezirksgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/9Nc15_14a`) (sent_id: `deanon_TRAIN/9Nc15_14a_6`)


5. 2014 die Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Favoriten.

**False Positives:**

- `Bezirksgericht Favoriten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/9Nc15_14a`) (sent_id: `deanon_TRAIN/9Nc15_14a_7`)


Das Bezirksgericht Favoriten verweigerte die Übernahme der Zuständigkeit.

**False Positives:**

- `Bezirksgericht Favoriten` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `deanon_TRAIN/10Nc27_20g`) (sent_id: `deanon_TRAIN/10Nc27_20g_3`)


Kopf Der Oberste Gerichtshof hat durch den Vizepräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden sowie die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, den Hofrat Mag. Ziegelbauer und die Hofrätin Dr. Faber als weitere Richter in der Pflegschaftssache der Kinder 1) Aleksandar Nollner, geboren 19. Oktober 2006, 2) Desanka Nichell, geboren 24. Februar 2007, 3) Mihailo Neuman, geboren 26. April 2009, 4) Antonio Nawrozki, geboren 10. Mai 2011, 5) Zivorad Naußedat, geboren 10. Dezember 2015 und 6) Gabriela Naujocks, geboren 26. Oktober 2016, über die Anzeige eines Zuständigkeitsstreits zwischen den Bezirksgerichten Freistadt (AZ 1 Ps 234/20m) und Hernals (AZ 30 Ps 142/15y) nach § 47 JN, den Beschluss gefasst:  Spruch Zur Fortführung des Pflegschaftsverfahrens ist das Bezirksgericht Freistadt zuständig.

**False Positives:**

- `Bezirksgericht Freistadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Nollner`(person)
- `19. Oktober`(date)
- `Nichell`(person)
- `24. Februar`(date)
- `Neuman`(person)
- `26. April`(date)
- `Nawrozki`(person)
- `10. Mai`(date)
- `Naußedat`(person)
- `10. Dezember`(date)
- `Naujocks`(person)
- `26. Oktober`(date)

**Example 45** (doc_id: `deanon_TRAIN/10Nc27_20g`) (sent_id: `deanon_TRAIN/10Nc27_20g_6`)


[2] Das Bezirksgericht Hernals übertrug mit Beschluss vom 11. August 2020, GZ 30 Ps 142/15y-55, die Zuständigkeitgemäß § 44 JNan das Bezirksgericht Freistadt, in dessen Sprengel die Familie seit der Delogierung aus der Wiener Wohnung im Juli 2019 gemeldet sei (auch wenn der aktuelle Aufenthaltsort der Familie nicht bekannt sei).

**False Positives:**

- `Bezirksgericht Hernals` — no gold match — likely missing annotation
- `Bezirksgericht Freistadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 46** (doc_id: `deanon_TRAIN/10Nc27_20g`) (sent_id: `deanon_TRAIN/10Nc27_20g_7`)


[3] Das Bezirksgericht Freistadt erklärte sich mit Beschluss vom 21. Oktober 2020 (ON 60) für örtlich unzuständig (Punkt 1.) und wies den Antrag des Kinder- und Jugendhilfeträgers zurück (Punkt 2.).

**False Positives:**

- `Bezirksgericht Freistadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/10Nc27_20g`) (sent_id: `deanon_TRAIN/10Nc27_20g_11`)


[4] Nach Rechtskraft dieser beiden – gleichzeitig an die Parteien zugestellten – Beschlüsse legte das Bezirksgericht Freistadt den Akt dem Obersten Gerichtshof gemäß § 47 JN zur Entscheidung über den Zuständigkeitsstreit mit dem Bezirksgericht Hernals vor.

**False Positives:**

- `Bezirksgericht Freistadt` — no gold match — likely missing annotation
- `Bezirksgericht Hernals` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 48** (doc_id: `deanon_TRAIN/5Ob233_10s`) (sent_id: `deanon_TRAIN/5Ob233_10s_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Danzl als Vorsitzenden sowie die Hofrätinnen Dr. Hurch und Dr. Lovrek und die Hofräte Dr. Höllwerth und Mag. Wurzer als weitere Richter in der beim Bezirksgericht Bruck/Mur zu 4 Nc 19/09d anhängigen Verfahrenshilfesache des Antragstellers Ruprecht Jostmeier, geboren am 26. Dezember 1988, wegen Ablehnung über den Rekurs des Genannten, gegen den Beschluss des Oberlandesgerichts Graz vom 14. Oktober 2010, GZ 3 Nc 1/10s-2, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Bezirksgericht Bruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ruprecht Jostmeier`(person)
- `26. Dezember 1988`(date)

**Example 49** (doc_id: `deanon_TRAIN/5Ob233_10s`) (sent_id: `deanon_TRAIN/5Ob233_10s_5`)


9. 2009 bewilligte das Bezirksgericht Bruck/Mur dem nunmehrigen Ablehnungswerber die Verfahrenshilfe einschließlich der Beigebung eines Rechtsanwalts für eine gegen das Land Steiermark beabsichtigte Klageführung.

**False Positives:**

- `Bezirksgericht Bruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `deanon_TRAIN/5Ob233_10s`) (sent_id: `deanon_TRAIN/5Ob233_10s_6`)


Der dem Rechtsmittelwerber beigegebene Verfahrenshilfeanwalt ersuchte das Bezirksgericht Bruck/Mur unter Vorlage eines Klageentwurfs um Erteilung einer „Weisung, ob trotz der negativen Prozessaussichten eine Amtshaftungsklage im Rahmen der Verfahrenshilfe beauftragt“ werde.

**False Positives:**

- `Bezirksgericht Bruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_TRAIN/5Ob233_10s`) (sent_id: `deanon_TRAIN/5Ob233_10s_7`)


Das Bezirksgericht Bruck/Mur lehnte mit Note an den Verfahrenshelfer die Erteilung einer solchen Weisung ab und gab dem Rechtsmittelwerber mit weiterer Note bekannt, dass seinem Vertreter „in Anbetracht der Aussichtslosigkeit der Prozessführung“ keine Weisung erteilt werde.

**False Positives:**

- `Bezirksgericht Bruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `deanon_TRAIN/5Ob233_10s`) (sent_id: `deanon_TRAIN/5Ob233_10s_8`)


Diese Mitteilung fasste der Rechtsmittelwerber als Beschluss auf und erhob dagegen Rekurs, den das Bezirksgericht Bruck/Mur selbst mit Beschluss vom 7. 4. 2010 zurückwies.

**False Positives:**

- `Bezirksgericht Bruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_TRAIN/11Os114_12t_11Os115_12i_`) (sent_id: `deanon_TRAIN/11Os114_12t_11Os115_12i__7`)


Text Gründe: Gegen Claudio Mühlmann war beim Bezirksgericht Bregenz zu AZ 6 U 49/12h ein Strafverfahren wegen des Verdachts des Vergehens des unerlaubten Umgangs mit Suchtgiften nach § 27 Abs 1 Z 1 SMG anhängig.

**False Positives:**

- `Bezirksgericht Bregenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mühlmann`(person)

**Example 54** (doc_id: `deanon_TRAIN/11Os114_12t_11Os115_12i_`) (sent_id: `deanon_TRAIN/11Os114_12t_11Os115_12i__10`)


Am 22. März 2012 langte im Telefaxweg die mit 21. März 2012 datierte schriftliche Beschwerde der Staatsanwaltschaft Feldkirch beim Bezirksgericht Bregenz ein (ON 10).

**False Positives:**

- `Bezirksgericht Bregenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_TRAIN/11Os114_12t_11Os115_12i_`) (sent_id: `deanon_TRAIN/11Os114_12t_11Os115_12i__40`)


Die Beschwerde der Staatsanwaltschaft gegen den Beschluss vom 7. März 2012 wurde erst am Donnerstag, den 22. März 2012, sohin nach Fristablauf, im Telefaxweg an das Bezirksgericht Bregenz übermittelt (vgl den in Kopie beiliegenden Sendebericht ON 10).

**False Positives:**

- `Bezirksgericht Bregenz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 56** (doc_id: `deanon_TRAIN/5Nc13_13a`) (sent_id: `deanon_TRAIN/5Nc13_13a_14`)


Mit dem vorliegendenOrdinationsantragbegehren die Kläger, für die Rechtssache das Bezirksgericht Imst als örtlich zuständiges Gericht zu bestimmen.

**False Positives:**

- `Bezirksgericht Imst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/5Nc13_13a`) (sent_id: `deanon_TRAIN/5Nc13_13a_15`)


Sie gestehen zu, dass das angerufene Bezirksgericht Imst nicht zufolge § 83 Abs 1 JN zuständig sei, weil der Bestandgegenstand nicht im Sprengel dieses Bezirksgerichts, sondern im Fürstentum Liechtenstein liege.

**False Positives:**

- `Bezirksgericht Imst` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/10Nc32_14h`) (sent_id: `deanon_TRAIN/10Nc32_14h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden und durch die Hofräte Dr. Fellinger und Dr. Schramm als weitere Richter in der Pflegschaftssache der mj Eleonore Gruenberger, geboren am 22. September 1952, wegen § 111 Abs 2 JN, den Beschluss gefasst:  Spruch Die mit Beschluss des Bezirksgerichts Liezen vom 11. 8. 2014, GZ 16 PU 84/13w-91, ausgesprochene Übertragung der Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Bad Ischl wirdnichtgenehmigt.

**False Positives:**

- `Bezirksgericht Bad` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Eleonore Gruenberger`(person)
- `22. September 1952`(date)

**Example 59** (doc_id: `deanon_TRAIN/10Nc32_14h`) (sent_id: `deanon_TRAIN/10Nc32_14h_6`)


Mit dem unbekämpft gebliebenen Beschluss vom 11. 8. 2014 übertrug das Bezirksgericht Liezen seine Zuständigkeit zur Führung der Pflegschaftssache an das Bezirksgericht Bad Ischl, in dessen Sprengel der Lebensmittelpunkt der Minderjährigen liege, weil sie dort das Gymnasium besuche, die Mutter eine Arztpraxis betreibe und eine Wohnung gemietet habe.

**False Positives:**

- `Bezirksgericht Liezen` — no gold match — likely missing annotation
- `Bezirksgericht Bad` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 60** (doc_id: `deanon_TRAIN/10Nc32_14h`) (sent_id: `deanon_TRAIN/10Nc32_14h_8`)


2014 lehnte das Bezirksgericht Bad Ischl die Übernahme der Zuständigkeit ab, weil der gewöhnliche Aufenthalt bzw der Lebensmittelpunkt der Minderjährigen und ihrer Mutter nach wie vor im Sprengel des Bezirksgerichts Liezen liege, wo sie mit dem Lebensgefährten, mit dem die Mutter ein elf Monate altes Kind habe, wohnten, die Wochenenden von Freitag abends bis Montag früh und auch weitere zwei oder drei Nächte der Woche verbrächten.

**False Positives:**

- `Bezirksgericht Bad` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `deanon_TRAIN/10Nc32_14h`) (sent_id: `deanon_TRAIN/10Nc32_14h_11`)


Rechtliche Beurteilung Das Bezirksgericht Liezen legte den Akt dem Obersten Gerichtshof zur Entscheidung nach § 111 Abs 2 JN vor.

**False Positives:**

- `Bezirksgericht Liezen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_TRAIN/10Nc32_14h`) (sent_id: `deanon_TRAIN/10Nc32_14h_19`)


5. Es ist nicht erkennbar, welcher Vorteil für die Minderjährige, die unverändert ihren gewöhnlichen Aufenthalt im Sprengel des Bezirksgerichts Liezen hat, in einer Übertragung der Zuständigkeit an das Bezirksgericht Bad Ischl gelegen sein könnte.

**False Positives:**

- `Bezirksgericht Bad` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_TRAIN/10Ob82_10x`) (sent_id: `deanon_TRAIN/10Ob82_10x_9`)


In dem vor dem Bezirksgericht St. Pölten am 29. 2. 2003 zu AZ 1 C 220/02d abgeschlossenen Unterhaltsvergleich verpflichtete er sich zu einer monatlichen Unterhaltsleistung von 120 EUR.

**False Positives:**

- `Bezirksgericht St` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/1Ob91_13h`) (sent_id: `deanon_TRAIN/1Ob91_13h_7`)


2008 übertrug das (österreichische) Bezirksgericht Josefstadt der Mutter die alleinige Obsorge.

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_TRAIN/1Ob91_13h`) (sent_id: `deanon_TRAIN/1Ob91_13h_10`)


Das Bezirksgericht Josefstadt sei daher für die von ihm getroffene Obsorgeentscheidung international unzuständig gewesen;

**False Positives:**

- `Bezirksgericht Josefstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Mag. Dr. Wurdinger als weitere Richter in der beim Bezirksgericht Bruck an der Mur zu AZ 4 Nc 19/09d anhängigen Verfahrenshilfesache des Antragstellers Hon.-Prof.in Babette Savvakis, wegen Ablehnung, über den Rekurs des Antragstellers gegen den Beschluss des Oberlandesgerichts Graz vom 14. Oktober 2010, GZ 3 Nc 2/10p-2, den Beschluss gefasst:  Spruch Dem Rekurs wird nicht Folge gegeben.

**False Positives:**

- `Bezirksgericht Bruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hon.-Prof.in Babette Savvakis`(person)

**Example 67** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_5`)


9. 2009 bewilligte das Bezirksgericht Bruck an der Mur dem nunmehrigen Ablehnungswerber die Verfahrenshilfe einschließlich der Beigebung eines Rechtsanwalts für eine gegen das Land Steiermark beabsichtigte Klageführung.

**False Positives:**

- `Bezirksgericht Bruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_6`)


Der dem Rechtsmittelwerber beigegebene Verfahrenshilfeanwalt ersuchte das Bezirksgericht Bruck an der Mur unter Vorlage eines Klageentwurfs um Erteilung einer „Weisung, ob trotz der negativen Prozessaussichten eine Amtshaftungsklage im Rahmen der Verfahrenshilfe beauftragt“ werde.

**False Positives:**

- `Bezirksgericht Bruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_7`)


Das Bezirksgericht Bruck an der Mur lehnte die Erteilung einer solchen Weisung ab und gab dem Rechtsmittelwerber bekannt, dass seinem Vertreter „in Anbetracht der Aussichtslosigkeit der Prozessführung“ keine Weisung erteilt werde.

**False Positives:**

- `Bezirksgericht Bruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_8`)


Diese Mitteilung fasste der Rechtsmittelwerber als Beschluss auf und erhob dagegen Rekurs, den das Bezirksgericht Bruck an der Mur mit Beschluss vom 7. 4. 2010 zurückwies.

**False Positives:**

- `Bezirksgericht Bruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `deanon_TRAIN/10Nc15_11d`) (sent_id: `deanon_TRAIN/10Nc15_11d_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Maja Ispirli, vertreten durch Dr. Clemens Pichler, Rechtsanwalt in Dornbirn, gegen die beklagte Partei Hartwig Dirksmeier, wegen Einverleibung des Eigentumsrechts, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Delegierung der Rechtssache an das Bezirksgericht Salzburg wird abgewiesen.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Maja Ispirli`(person)
- `Hartwig Dirksmeier`(person)

**Example 72** (doc_id: `deanon_TRAIN/10Nc15_11d`) (sent_id: `deanon_TRAIN/10Nc15_11d_4`)


Text Begründung: Der Kläger begehrt mit der beim Bezirksgericht Liesing eingebrachten Klage, den Beklagten schuldig zu erkennen, in die Einverleibung seines Eigentumsrechts an näher bezeichneten Wohnungseigentumsobjekten einzuwilligen, sowie in eventu die Feststellung der Unwirksamkeit eines mit dem Beklagten abgeschlossenen Schenkungsvertrags.

**False Positives:**

- `Bezirksgericht Liesing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_TRAIN/10Nc15_11d`) (sent_id: `deanon_TRAIN/10Nc15_11d_7`)


Das Bezirksgericht Liesing legte den Akt dem Obersten Gerichtshof zur Entscheidung über den Delegierungsantrag vor.

**False Positives:**

- `Bezirksgericht Liesing` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `deanon_TRAIN/6Ob199_10y`) (sent_id: `deanon_TRAIN/6Ob199_10y_5`)


Im vorliegenden Verfahren geht es um die pflegschaftsbehördliche Genehmigung eines Vergleichs vor dem Bezirksgericht Meidling.

**False Positives:**

- `Bezirksgericht Meidling` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_6`)


[2] Mit ihrem am 7. Jänner 2021 „aus Vorsicht“ auch beim Obersten Gerichtshof eingebrachtenAntragbegehrt die anwaltlich nicht vertreteneSchiedsbeklagteals Antragstellerin, die Einvernahme von zehn Personen als Zeugen vor dem Bezirksgericht Liezen.

**False Positives:**

- `Bezirksgericht Liezen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_10`)


Gleichzeitig wurde der idente Antrag auch beim Bezirksgericht Liezen eingebracht.

**False Positives:**

- `Bezirksgericht Liezen` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 77** (doc_id: `deanon_TRAIN/18ONc1_21y`) (sent_id: `deanon_TRAIN/18ONc1_21y_16`)


[5] Aufgrund des Verweises auf § 37 Abs 2 bis 5 JN ist für einen solchen Antrag das Bezirksgericht zuständig, in dessen Sprengel die Amtshandlung vorgenommen werden soll (HausmaningerinFasching/Konecny3§ 602 ZPO Rz 30).

**False Positives:**

- `Bezirksgericht zuständig` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__5`)


Das Abwesenheitsurteil vom 26. September 2018 sowie der unter einem gefasste Beschluss (ON 25) werden aufgehoben und die Sache zu neuer Verhandlung und Entscheidung an das Bezirksgericht Leopoldstadt verwiesen.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__11`)


Nach zwei negativen Versuchen der Vorführung zur Hauptverhandlung am 2. Mai 2018 (ON 10a, 11) und am 27. Juni 2018 (ON 17, 18) führte das Bezirksgericht Leopoldstadt die – wiederholte (§ 276a zweiter Satz StPO) – Hauptverhandlung am 26. September 2018 in Abwesenheit des Angeklagten durch (ON 24), weil auch zu diesem Termin ein Vorführungsversuch erfolglos geblieben war (ON 23).

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i_`) (sent_id: `deanon_TRAIN/12Os16_19y_12Os17_19w_12Os18_19t_12Os19_19i__13`)


Mit Abwesenheitsurteil vom 26. September 2018 (ON 25) sprach das Bezirksgericht Leopoldstadt Nenad Pentzold des Vergehens der Veruntreuung nach § 133 Abs 1 StGB schuldig und verurteilte ihn zu einer Freiheitsstrafe.

**False Positives:**

- `Bezirksgericht Leopoldstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Pentzold`(person)

**Example 81** (doc_id: `deanon_TRAIN/8Nc21_10w`) (sent_id: `deanon_TRAIN/8Nc21_10w_4`)


Text Begründung: Die im Sprengel des Landesgerichts Salzburg ansässige Klägerin begehrte von dem in Kärnten wohnhaften Beklagten mit ihrer beim Bezirksgericht Salzburg eingebrachten Klage die Zahlung von 4.696,20 EUR sA aus dem Titel einer Überzahlung von Provisionen.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_TRAIN/8Nc21_10w`) (sent_id: `deanon_TRAIN/8Nc21_10w_5`)


Mit in Rechtskraft erwachsenem Beschluss vom 23. März 2010 erklärte sich das Bezirksgericht Salzburg für sachlich unzuständig und überwies die Rechtssache an das Landesgericht Salzburg als Arbeits- und Sozialgericht, weil nach dem Parteienvorbringen eine Rechtsstreitigkeit zwischen Arbeitgeber und Arbeitnehmer vorliege.

**False Positives:**

- `Bezirksgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `deanon_TRAIN/8Ob19_24p`) (sent_id: `deanon_TRAIN/8Ob19_24p_4`)


Matzka, Dr. Stefula, Dr. Thunhart und Mag. Dr. Sengstschmid als weitere Richter in der Rechtssache der klagenden Partei Mag. Dr. Brigitte Jonassohn, vertreten durch Dr. Alexander Amann LL.M. (UCLA), Rechtsanwalt in Gamprin-Bendern, Liechtenstein (§ 5 Abs 3 EIRAG), gegen die beklagte Partei Neuschwander + Springenheide Bildung AG, Moses Wollgarten, Deutschland, vertreten durch die Pressl Endl Heinrich Bamberger Rechtsanwälte GmbH in Salzburg, wegen 60.000 EUR sA, infolge Rekurses der klagenden Partei gegen den Beschluss des Oberlandesgerichts Linz als Berufungsgericht vom 14. November 2023, GZ 6 R 147/23i-25, mit dem das Urteil des Landesgerichts Steyr vom 30. Juni 2023, GZ 9 Cg 28/22w-19, aufgehoben wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Das Rekursverfahren wird bis zur Entscheidung des Gerichtshofs der Europäischen Union über den vom Bezirksgericht für Handelssachen Wien am 27. September 2024 zu 22 C 278/20y (22 C [richtig:]269/20z, 22 C 270/20x) gestellten und zu C-751/24 des Europäischen Gerichtshofs anhängigen Antrag auf Vorabentscheidungunterbrochen.

**False Positives:**

- `Bezirksgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Brigitte Jonassohn`(person)
- `Neuschwander + Springenheide Bildung AG`(organisation)
- `Moses Wollgarten`(person)

**Example 84** (doc_id: `deanon_TRAIN/8Ob19_24p`) (sent_id: `deanon_TRAIN/8Ob19_24p_36`)


Im Verfahren 22 C 278/20y (22 C269/20z, 22 C 270/20x) hat das Bezirksgericht für Handelssachen Wien mit Beschluss vom 27.

**False Positives:**

- `Bezirksgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `deanon_TRAIN/10Nc25_10y`) (sent_id: `deanon_TRAIN/10Nc25_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei Stockhorst und Welfle Verlag GmbH, HR Philipp Ludwig, vertreten durch Dr. Wolfgang Waldeck und Dr. Hubert Hasenauer, Rechtsanwälte in Wien, gegen die beklagte Partei See Trilem Werke GmbH, Alessia Vieracker, wegen 6.100 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung wird anstelle des Bezirksgerichts für Handelssachen Wien das Bezirksgericht Linz bestimmt.

**False Positives:**

- `Bezirksgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Stockhorst und Welfle Verlag GmbH`(organisation)
- `HR Philipp Ludwig`(person)
- `See Trilem Werke GmbH`(organisation)
- `Alessia Vieracker`(person)

**Example 86** (doc_id: `deanon_TRAIN/10Nc25_10y`) (sent_id: `deanon_TRAIN/10Nc25_10y_6`)


Weiters stellte sie den Antrag auf Delegierung der Rechtssache an das Bezirksgericht Linz, da in dessen Sprengel sämtliche bisher geführten Zeugen ihren Wohnsitz hätten und sich auch das von der Beklagten gemietete und beschädigte Kraftfahrzeug in Linz befinde.

**False Positives:**

- `Bezirksgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `deanon_TRAIN/10Nc25_10y`) (sent_id: `deanon_TRAIN/10Nc25_10y_7`)


Die Klägerin erklärte, dass sie aus ökonomischen Gründen einer Delegierung der Rechtssache an das Bezirksgericht Linz nicht widerspreche.

**False Positives:**

- `Bezirksgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `deanon_TRAIN/10Nc25_10y`) (sent_id: `deanon_TRAIN/10Nc25_10y_8`)


Das Bezirksgericht für Handelssachen Wien befürwortete die Delegierung an das Bezirksgericht Linz und legte den Akt dem Obersten Gerichtshof zur Entscheidung über den Delegierungsantrag vor.

**False Positives:**

- `Bezirksgericht für` — no gold match — likely missing annotation
- `Bezirksgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 89** (doc_id: `deanon_TRAIN/7Nc4_12s`) (sent_id: `deanon_TRAIN/7Nc4_12s_4`)


Ophelia Kadlecova, und 2. Constanze Ishikawa, wegen Erlassung einer einstweiligen Verfügung, infolge der Vorlage des Aktes 1 C 16/12t des Bezirksgerichts Wiener Neustadt zur Entscheidung über den negativen Kompetenzkonflikt mit dem Bezirksgericht Mürzzuschlag nach § 47 JN den Beschluss gefasst:  Spruch Zur Entscheidung über den Antrag auf Erlassung der einstweiligen Verfügung ist das Bezirksgericht Wiener Neustadt zuständig.

**False Positives:**

- `Bezirksgericht Mürzzuschlag` — no gold match — likely missing annotation
- `Bezirksgericht Wiener` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Ophelia Kadlecova`(person)
- `Constanze Ishikawa`(person)

**Example 90** (doc_id: `deanon_TRAIN/7Nc4_12s`) (sent_id: `deanon_TRAIN/7Nc4_12s_6`)


Text Begründung: Der Antragsteller stellte mit am 2. 1. 2012 beim Bezirksgericht Mürzzuschlag eingelangtem Schriftsatz den Antrag, mit einstweiliger Verfügung gemäß §§ 382g, 381 Z 2 EO gegen die Antragsgegner diverse Verbote zu erlassen.

**False Positives:**

- `Bezirksgericht Mürzzuschlag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `deanon_TRAIN/7Nc4_12s`) (sent_id: `deanon_TRAIN/7Nc4_12s_7`)


Das Bezirksgericht Mürzzuschlag erklärte sich mit am selben Tag gefasstem Beschluss gemäß § 387 Abs 4 EO für unzuständig und überwies das Verfahren nach § 44 JN an das nicht offenbar unzuständige Bezirksgericht Wiener Neustadt.

**False Positives:**

- `Bezirksgericht Mürzzuschlag` — no gold match — likely missing annotation
- `Bezirksgericht Wiener` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 92** (doc_id: `deanon_TRAIN/7Nc4_12s`) (sent_id: `deanon_TRAIN/7Nc4_12s_9`)


Das Bezirksgericht Wiener Neustadt stellte den Provisorialantrag zunächst den Antragsgegnern zur Äußerung zu.

**False Positives:**

- `Bezirksgericht Wiener` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `deanon_TRAIN/7Nc4_12s`) (sent_id: `deanon_TRAIN/7Nc4_12s_11`)


2. 2012 den Beschluss, die Rechtssache wiederum dem Bezirksgericht Mürzzuschlag (zurück-)zuüberweisen.

**False Positives:**

- `Bezirksgericht Mürzzuschlag` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 94** (doc_id: `deanon_TRAIN/7Nc4_12s`) (sent_id: `deanon_TRAIN/7Nc4_12s_13`)


Das Bezirksgericht Wiener Neustadt könne daher seine Unzuständigkeit aussprechen.

**False Positives:**

- `Bezirksgericht Wiener` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `deanon_TRAIN/7Nc4_12s`) (sent_id: `deanon_TRAIN/7Nc4_12s_18`)


Das Bezirksgericht Wiener Neustadt legte den Akt dem Obersten Gerichtshof zur Entscheidung über den negativen Kompetenzkonflikt nach § 47 JN vor.

**False Positives:**

- `Bezirksgericht Wiener` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 96** (doc_id: `deanon_TRAIN/10Ob96_11g`) (sent_id: `deanon_TRAIN/10Ob96_11g_4`)


Text Begründung: Der Vater war - ausgehend von einem Jahresnettoeinkommen von 40.000 EUR im Jahr 2006 - aufgrund des vor dem Bezirksgericht Laa an der Thaya am 6.

**False Positives:**

- `Bezirksgericht Laa` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 97** (doc_id: `deanon_TRAIN/10Nc16_24w`) (sent_id: `deanon_TRAIN/10Nc16_24w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober und Dr. Annerl als weitere Richter in der Pflegschaftssache der minderjährigen Chiara Vöpel, geboren 4. November 2017, folgenden Beschluss gefasst:  Spruch Die mit Beschluss des Bezirksgerichts Weiz vom 9. August 2024, GZ 50 Pu 246/21p-9, ausgesprochene Teilübertragung der Zuständigkeit zur Führung der Pflegschaftssache (Pu-Akt) an das Bezirksgericht Feldkirch wird nicht genehmigt.

**False Positives:**

- `Bezirksgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Chiara Vöpel`(person)
- `4. November`(date)

**Example 98** (doc_id: `deanon_TRAIN/10Nc16_24w`) (sent_id: `deanon_TRAIN/10Nc16_24w_4`)


Text Begründung: [1] Das Bezirksgericht Weiz übertrug mit Beschluss vom 9. August 2024 die Pflegschaftssache gemäß § 111 JN teilweise (Unterhaltsakt) an das Bezirksgericht Feldkirch, weil sich die Minderjährige nunmehr ständig in dessen Sprengel aufhalte.

**False Positives:**

- `Bezirksgericht Weiz` — no gold match — likely missing annotation
- `Bezirksgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 99** (doc_id: `deanon_TRAIN/10Nc16_24w`) (sent_id: `deanon_TRAIN/10Nc16_24w_5`)


Das Bezirksgericht Feldkirch lehnte die Übernahme der Zuständigkeit mit Beschluss vom 20. August 2024 wegen des anhängigen Obsorge- und Kontaktrechtsverfahrens ab und stellte den Akt dem Bezirksgericht Weiz zurück.

**False Positives:**

- `Bezirksgericht Feldkirch` — no gold match — likely missing annotation
- `Bezirksgericht Weiz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

</details>

---

## `Regional Court Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8426a1d3`  
**Description:**
Matches Landesgericht (LG) followed by location.

**Content:**
```
(?i)\b(Landesgericht\s+([A-Za-zäöüÄÖÜ]+|\w+)|LG\s+([A-Za-zäöüÄÖÜ]+|\w+))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 90 | 0 | 90 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 90 | 391 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob167_22y`) (sent_id: `deanon_TRAIN/1Ob167_22y_7`)


[2] Das Landesgericht Leoben als Berufungsgericht hob das erstinstanzliche Urteil zur neuerlichen Entscheidung nach allfälliger Verfahrensergänzung auf.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `deanon_TRAIN/1Ob167_22y`) (sent_id: `deanon_TRAIN/1Ob167_22y_15`)


Mit dem angefochtenen Beschluss hat das Landesgericht Leoben nicht im Berufungsverfahren, sondern im Rekursverfahren den Rekurs sowie weitere Anträge der Klägerin gegen seinen Aufhebungsbeschluss zurückgewiesen (vgl 3 Ob 156/83 = SZ 57/5 = JBl 1984, 617).

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `deanon_TRAIN/1Ob167_22y`) (sent_id: `deanon_TRAIN/1Ob167_22y_26`)


Da somit gegen einen – hier vorliegenden – aufhebenden Beschluss des Berufungsgerichts gemäß § 519 Abs 1 Z 2 ZPO nur dann ein Rekurs an den Obersten Gerichtshof erhoben werden könnte, wenn das Berufungsgericht ausgesprochen hätte, dass (der Wert des Entscheidungsgegenstands 5.000 EUR übersteigt [vgl 4 Ob 206/08k mwN] und) der Rekurs wegen Vorliegens einer erheblichen Rechtsfrage zulässig wäre, hier aber ein solcher Ausspruch nicht vorliegt, hat das Landesgericht Leoben zutreffend in sinngemäßer Anwendung des § 523 ZPO das unzulässige Rechtsmittel und (mangels Rechtsgrundlage) die Anträge auf „Ausspruch der Zulässigkeit des (Revisions-)Rekurses“ und „Abänderung des Ausspruchs über die Zulässigkeit“ zurückgewiesen.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/10Nc12_11p`) (sent_id: `deanon_TRAIN/10Nc12_11p_6`)


Text Begründung: Die Klägerin brachte beim Landesgericht Innsbruck eine Klage ein, mit der sie die Bezahlung von (ausgedehnt) 52.827,98 EUR sA an Schadenersatz wegen eines beim Reitunterricht in der vom Beklagten betriebenen Reitschule erlittenen Reitunfalls verlangt;

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/9Nc16_11v`) (sent_id: `deanon_TRAIN/9Nc16_11v_3`)


Kopf Der Oberste Gerichtshof hat in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten des Obersten Gerichtshofs Dr. Rohrer als Vorsitzenden sowie durch die Hofräte des Obersten Gerichtshofs Dr. Hopf und Mag. Ziegelbauer als weitere Richter in der Arbeitsrechtssache der klagenden Partei Senta Moshack, vertreten durch Berchtold & Kollerics, Rechtsanwälte in Graz, gegen die beklagte Partei Anton Reinerth, vertreten durch die Finanzprokuratur, 1011 Wien, Singerstraße 17-19, wegen Feststellung (Streitwert: 69.000 EUR), über den Delegierungsantrag beider Parteien den Beschluss gefasst:  Spruch Der Akt wird dem Landesgericht für Zivilrechtssachen Graz als Arbeits- und Sozialgericht zur Entscheidung nach § 31a JN zurückgestellt.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Senta Moshack`(person)
- `Anton Reinerth`(person)

**Example 5** (doc_id: `deanon_TRAIN/9Nc16_11v`) (sent_id: `deanon_TRAIN/9Nc16_11v_5`)


Nach Einbringung der Klage, jedoch noch vor Anberaumung einer mündlichen Streitverhandlung in erster Instanz, beantragten die Parteien einvernehmlich die Delegierung der Arbeitsrechtssache an das Landesgericht Linz als Arbeits- und Sozialgericht.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/15Os63_16b`) (sent_id: `deanon_TRAIN/15Os63_16b_5`)


Rechtliche Beurteilung Der dagegen vom Angeklagten erhobenen Berufung wegen Nichtigkeit und Schuld gab das Landesgericht Innsbruck mit Urteil vom 7. Juni 2016, AZ 21 Bl 347/15k nicht, der Berufung wegen Strafe dahin Folge, dass die vom Erstgericht verhängte Geldstrafe gemildert wurde.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `deanon_TRAIN/12Os125_18a`) (sent_id: `deanon_TRAIN/12Os125_18a_5`)


Gemäß § 292 letzter Satz StPO werden das genannte Urteil, das im Übrigen unberührt bleibt, in der Subsumtion der Schuldspruch A./ zugrunde liegenden Taten unter § 28a Abs 2 Z 1 SMG, demgemäß auch der Ausspruch der Freiheitsstrafe (einschließlich der Vorhaftanrechnung) sowie der unter einem gefasste Beschluss gemäß § 494a Abs 1 Z 4 StPO aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht für Strafsachen Wien verwiesen.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `deanon_TRAIN/10Nc8_22s`) (sent_id: `deanon_TRAIN/10Nc8_22s_9`)


Das Landesgericht Korneuburg als Rekursgericht bestätigte diese Entscheidung.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/14Os159_11f_14Os160_11b_`) (sent_id: `deanon_TRAIN/14Os159_11f_14Os160_11b__16`)


Der Vorgang, dass das Urteil des Landesgerichts Wr. Neustadt vom 7. Oktober 2011 in gekürzter Form ausgefertigt wurde, und der Beschluss auf Verlängerung der Probezeit stehen - wie die Generalprokuratur in ihrer Nichtigkeitsbeschwerde zur Wahrung des Gesetzes zutreffend ausführt - mit dem Gesetz nicht im Einklang: Nach der gemäß § 488 Abs 1 StPO auch für das Hauptverfahren vor dem Landesgericht als Einzelrichter geltenden Bestimmung des § 270 Abs 4 StPO ist die Ausfertigung eines Urteils in gekürzter Form nicht zulässig, wenn eine mit Freiheitsentziehung verbundene vorbeugende Maßnahme - wie vorliegend die Unterbringung in einer Anstalt für entwöhnungsbedürftige Rechtsbrecher nach § 22 Abs 1 StGB - angeordnet wurde (RIS-Justiz RS0127071).

**False Positives:**

- `Landesgericht als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `deanon_TRAIN/14Os159_11f_14Os160_11b_`) (sent_id: `deanon_TRAIN/14Os159_11f_14Os160_11b__19`)


Das Landesgericht Wr. Neustadt hat durch seine Beschlussfassung auf Verlängerung der Probezeit nach § 494a Abs 6 StPO eine ihm nicht (mehr) zustehende Kompetenz in Anspruch genommen und solcherart den sich aus dem 16.

**False Positives:**

- `Landesgericht Wr` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `deanon_TRAIN/10Nc9_15b`) (sent_id: `deanon_TRAIN/10Nc9_15b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Fellinger als Vorsitzenden und durch die Hofräte Univ.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der beim Landesgericht Linz zu AZ 1 Cg 193/14v anhängigen Rechtssache der klagenden Partei Mur Kraftalheim Holding GmbH, Gerald Zacharie, vertreten durch Dr. Roland Kassowitz, Rechtsanwalt in Wien, gegen die beklagte Partei Nexstein Textil GmbH, Dipl.-Ing. Lynn Forkarth, vertreten durch Prof. Haslinger & Partner Rechtsanwälte in Linz, wegen 174.624,53 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung der Rechtssache wird anstelle des Landesgerichts Linz das Handelsgericht Wien bestimmt.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mur Kraftalheim Holding GmbH`(organisation)
- `Gerald Zacharie`(person)
- `Nexstein Textil GmbH`(organisation)
- `Dipl.-Ing. Lynn Forkarth`(person)

**Example 12** (doc_id: `deanon_TRAIN/12Os107_11v`) (sent_id: `deanon_TRAIN/12Os107_11v_4`)


In Stattgebung sowie aus Anlass der Nichtigkeitsbeschwerde wird das angefochtene Urteil, das im Übrigen unberührt bleibt, in den Renata Himmeldirk betreffenden Schuldsprüchen B./I./ und II./ und demzufolge auch im Strafausspruch aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Korneuburg verwiesen.

**False Positives:**

- `Landesgericht Korneuburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Himmeldirk`(person)

**Example 13** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__6`)


Dem Landesgericht für Strafsachen Graz wird ein Vorgehen gemäß §§ 14 und 15 dieser Verordnung aufgetragen.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__23`)


Seither besteht das Landesgericht als Schöffengericht aus nur einem (Berufs-)Richter und zwei Schöffen (§ 32 Abs 1 dritter Satz StPO).

**False Positives:**

- `Landesgericht als` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 15** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__28`)


8. Das Landesgericht für Strafsachen Graz hätte demnach die Staatsanwaltschaft und den Angeklagten von der dauernden Verhinderung des Vorsitzenden des Schöffengerichts in Kenntnis setzen und vor Betrauung eines anderen Richters mit der Urteilsausfertigung nach ihrem Einverständnis fragen müssen.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `deanon_TRAIN/13Os33_12w_13Os58_12x_`) (sent_id: `deanon_TRAIN/13Os33_12w_13Os58_12x__30`)


Mit Blick auf § 292 letzter Satz StPO sah sich der Oberste Gerichtshof veranlasst, dem Landesgericht für Strafsachen Graz aufzutragen, gemäß §§ 14 und 15 der Kaiserlichen Verordnung vorzugehen.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_40`)


Dieser Auffassung hat sich zwischenzeitig bereits zweitinstanzliche Rechtsprechung ausdrücklich (vgl etwa LG Salzburg EFSlg 156.701 [2018], 159.791, 159.792 [2019];

**False Positives:**

- `LG Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `deanon_TRAIN/6Ob182_20p`) (sent_id: `deanon_TRAIN/6Ob182_20p_41`)


LG Linz EFSlg 156.702 [2018], 159.793 [2019]) und die Entscheidung 9 Ob 57/17y offensichtlich angeschlossen.

**False Positives:**

- `LG Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_3`)


Kopf Der Oberste Gerichtshof hat durch die Senatspräsidentin Dr. Schenk als Vorsitzende und durch die Hofräte Dr. Vogel und Dr. Jensik als weitere Richter in der beim Landesgericht Innsbruck zu AZ 59 Cg 92/11x anhängigen Rechtssache der klagenden Partei Rudigkeit Finanzen GmbH, Ing. Sascha Rohkrämer, vertreten durch Mag. Heinz Heher, Rechtsanwalt in Wien, gegen die beklagte Partei Suddorftra Manufaktur GmbH, Ludmilla Nottelmann, vertreten durch Dr. Adrian Hollaender, Rechtsanwalt in Innsbruck, wegen Unterlassung, Urteilsveröffentlichung und 67.606 EUR sA, über die Delegierungsanträge der beklagten Partei gemäß § 31 Abs 2 JN, folgenden Beschluss gefasst:  Spruch Die Anträge der beklagten Partei, die Rechtssache an das „Landesgericht Wien“ bzw Handelsgericht Wien zu delegieren, werden abgewiesen.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation
- `Landesgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Rudigkeit Finanzen GmbH`(organisation)
- `Ing. Sascha Rohkrämer`(person)
- `Suddorftra Manufaktur GmbH`(organisation)
- `Ludmilla Nottelmann`(person)

**Example 20** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_6`)


Die Klägerin brachte beim Landesgericht Innsbruck eine Unterlassungs- und Zahlungsklage ein.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `deanon_TRAIN/4Nc3_12x`) (sent_id: `deanon_TRAIN/4Nc3_12x_11`)


Nach Einbringen der Klagebeantwortung beantragte sie die Delegierung an das „Landesgericht Wien“.

**False Positives:**

- `Landesgericht Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `deanon_TRAIN/10Ob32_14z`) (sent_id: `deanon_TRAIN/10Ob32_14z_34`)


Der Revisionsrekurswerber macht im Wesentlichen geltend, das Landesgericht für Zivilrechtssachen Graz vertrete die Ansicht, die durch das FamRÄG 2009 geschaffene Regelung des § 19 Abs 3 UVG hindere nach Vorliegen eines vorläufigen Unterhaltstitels die weitere Bevorschussung nach § 4 Z 2 UVG.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `deanon_TRAIN/10Ob32_14z`) (sent_id: `deanon_TRAIN/10Ob32_14z_52`)


I.3.2 Auch nach der Rechtsprechung zweitinstanzlicher Gerichte hat die Schaffung eines Teiltitels bzw die Erlassung einer einstweiligen Verfügung nach § 382a EO dem Grunde nach nicht die Einstellung von nach § 4 Z 2 UVG gewährten Unterhaltsvorschüssen zur Folge (so zB Landesgericht Linz EFSlg 127.751).

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 24** (doc_id: `deanon_TRAIN/10Ob32_14z`) (sent_id: `deanon_TRAIN/10Ob32_14z_55`)


In EFSlg 60.479 (Landesgericht für Zivilrechtssachen Wien) wird ausgeführt, der allgemeine Grundsatz, dass jede gelungene Titelschöpfung eine Bevorschussung nach § 4 Z 2 UVG ausschließt, finde bei einem Titel nach § 382a EO nur eingeschränkt Anwendung, weil dieser Gedanke von einer Unterhaltsfestsetzung ausgeht, die verfahrensmäßig auf die Schöpfung eines Volltitels abzielt.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `deanon_TRAIN/13Ns61_17z`) (sent_id: `deanon_TRAIN/13Ns61_17z_4`)


2005 den Beschluss gefasst:  Spruch Die Strafsache wird dem zuständigen Gericht abgenommen und dem Landesgericht Klagenfurt delegiert.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `deanon_TRAIN/13Os1_20a`) (sent_id: `deanon_TRAIN/13Os1_20a_5`)


Aus deren Anlass wird das angefochtene Urteil, das im Übrigen unberührt bleibt, im Konfiskationserkenntnis aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht für Strafsachen Wien verwiesen.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `deanon_TRAIN/5Ob233_10s`) (sent_id: `deanon_TRAIN/5Ob233_10s_9`)


Gegen diesen Zurückweisungsbeschluss richtet sich ein noch unerledigter Rekurs des Genannten an das Landesgericht Leoben, in welchem er die Richter der Rechtsmittelsenate in Zivilrechtssachen dieses Gerichtshofs (mit Ausnahme eines einzelnen namentlich genannten Richters) ablehnte.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `deanon_TRAIN/5Ob233_10s`) (sent_id: `deanon_TRAIN/5Ob233_10s_10`)


Gegen die im Ablehnungsverfahren vor dem Landesgericht Leoben (AZ 2 Nc 17/10y) ergangene Entscheidung, womit sein Antrag auf Ablehnung abgewiesen wurde, erhob Helena Jelinek Rekurs an das Oberlandesgericht Graz, den er mit der Ablehnung „sämtlicher Richter des Oberlandesgerichts im Zivilrechtsberufungssenat mit Ausnahme von Dr. Li Garthe “ verband.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Helena Jelinek`(person)
- `Dr. Li Garthe`(person)

**Example 29** (doc_id: `deanon_TRAIN/11Os114_12t_11Os115_12i_`) (sent_id: `deanon_TRAIN/11Os114_12t_11Os115_12i__11`)


Dieser gab das Landesgericht Feldkirch mit Beschluss vom 14. Mai 2012, AZ 25 Bl 38/12w (ON 16 der U-Akten), Folge, hob den angefochtenen Beschluss auf und trug dem Erstgericht die Fortsetzung des Verfahrens auf.

**False Positives:**

- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `deanon_TRAIN/12Os49_20b`) (sent_id: `deanon_TRAIN/12Os49_20b_5`)


Das genannte Urteil, das im Übrigen unberührt bleibt, wird in der rechtlichen Unterstellung der angelasteten Taten (auch) nach § 148 zweiter Fall StGB, demgemäß auch in der zum Schuldspruch gebildeten Subsumtionseinheit sowie im Strafausspruch aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Wiener Neustadt verwiesen.

**False Positives:**

- `Landesgericht Wiener` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `deanon_TRAIN/6Ob16_20a`) (sent_id: `deanon_TRAIN/6Ob16_20a_5`)


Text Begründung: Mit der beim Landesgericht für Zivilrechtssachen Wien eingebrachten Klage begehrt die Klägerin von der in Wien wohnhaften Beklagten die Zahlung von 422.136,06 EUR sA und erhebt diverse Eventualbegehren.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `deanon_TRAIN/13Os44_12p`) (sent_id: `deanon_TRAIN/13Os44_12p_4`)


Text Gründe: Mit Beschluss vom 11. Jänner 2012 (ON 78) wies das Landesgericht für Strafsachen Wien den Einspruch wegen Rechtsverletzung (§ 106 Abs 1 StPO) der Beschuldigten Stefan Hilmar und Irene Hülsing, mit dem sich diese - soweit hier von Interesse - gegen die von der Staatsanwaltschaft verfügte Beschränkung der Akteneinsicht bezüglich einzelner Aktenstücke wendeten, mit der wesentlichen Begründung ab, die bekämpfte Verfügung entspreche den Voraussetzungen des § 51 Abs 2 zweiter Satz StPO.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hilmar`(person)
- `Hülsing`(person)

**Example 33** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_75`)


1. Vorweg ist festzuhalten, dass auf die hier strittigen Leistungen der Klägerin aus sozialhilferechtlicher Sicht das oöSHG 1998 idF des LG LGBl 2018/39 anwendbar ist.

**False Positives:**

- `LG LGBl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_77`)


Die Änderungen des oöSHG 1998 mit dem oö Datenschutz-Anpassungsgesetz 2018, LGBl 2018/55, sind für den vorliegenden Fall sachlich unerheblich, jene durch das LG LGBl 2019/107 sind wegen dessen Inkrafttreten erst mit 1. Jänner 2020 (auch) zeitlich unerheblich.

**False Positives:**

- `LG LGBl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_83`)


Zudem wurde dieses Verbot ohnehin durch die Novellierung des oöSHG mit dem LG LGBl 2018/39 umgesetzt, sodass die Prüfung zunächst auf einfachgesetzlicher Grundlage zu erfolgen hat.

**False Positives:**

- `LG LGBl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `deanon_TRAIN/2Ob185_19y`) (sent_id: `deanon_TRAIN/2Ob185_19y_108`)


Zudem ergibt sich aus den Materialien zur Neufassung des § 17 Abs 5 oöSHG mit dem LG LGBl 2018/39, dass eine konkrete Prüfung alternativer Hilfen bei Vorliegen der Pflegegeldstufe 4 oder höher nicht mehr erforderlich ist (Blg oöLT 705/2018, zu Art I Z 5 [§ 17 Abs 5]).

**False Positives:**

- `LG LGBl` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_4`)


In Stattgebung der Nichtigkeitsbeschwerde wird das angefochtene Urteil aufgehoben, eine neue Hauptverhandlung angeordnet und die Sache an das Landesgericht Salzburg verwiesen.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 38** (doc_id: `deanon_TRAIN/15Os66_19y_15Os67_19w_`) (sent_id: `deanon_TRAIN/15Os66_19y_15Os67_19w__59`)


Das Landesgericht für Strafsachen Wien und das Oberlandesgericht Wien als Berufungsgericht haben somit die (grundsätzliche) Verwirklichung des Entschädigungsanspruchs nach § 6 Abs 1 MedienG in Bezug auf die am 4. Juni 2017 auf dem Facebook-Account von www.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `deanon_TRAIN/15Os42_20w_15Os43_20t_15Os96_20m_15Os97_20h_`) (sent_id: `deanon_TRAIN/15Os42_20w_15Os43_20t_15Os96_20m_15Os97_20h__10`)


Mit Beschluss vom 24. September 2019, GZ 23 Hv 18/19h-29, verpflichtete das Landesgericht Feldkirch den Antragsgegner nach dessen Anhörung nach § 20 Abs 1 MedienG „aufgrund der nicht gehörigen Veröffentlichung des Urteils vom 23. Mai 2019 […] gemäß § 8 lit a Abs 6 MedienG iVm § 34 MedienG“ zur Zahlung einer Geldbuße an den Antragsteller iHv 2.850 Euro (und zwar für den Zeitraum [ersichtlich gemeint] vom 23. Juli 2019 bis einschließlich 18. September 2019 [57 Tage á 50 Euro;

**False Positives:**

- `Landesgericht Feldkirch` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `deanon_TRAIN/7Nc36_14z`) (sent_id: `deanon_TRAIN/7Nc36_14z_4`)


Begründung:  Rechtliche Beurteilung Der Antragsteller macht in einem Verfahren vor dem Landesgericht Leoben Amtshaftungsansprüche gegen die Republik Österreich, sonstige Schadenersatzansprüche gegen eine Journalistin und Inhaberin eines Printmediums sowie Feststellungsansprüche gegen alle dort beklagten Parteien geltend.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `deanon_TRAIN/7Nc36_14z`) (sent_id: `deanon_TRAIN/7Nc36_14z_5`)


Nach Zurück- bzw Abweisung seiner Begehren im Verfahren erster Instanz lehnte er wiederholt Richter des Landesgerichts Leoben, des Oberlandesgerichts Graz und des Obersten Gerichtshofs erfolglos ab (vgl unter anderem Landesgericht Leoben: 2 Nc 24/11d, 2 Nc 25/11a, 2 Nc 28/11t;

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_9`)


Dagegen erhob der Ablehnungswerber Rekurs an das Landesgericht Leoben, mit dem er die Ablehnung von Richtern der Rechtsmittelsenate in Zivilrechtssachen verband.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `deanon_TRAIN/7Ob244_10y`) (sent_id: `deanon_TRAIN/7Ob244_10y_10`)


Gegen die im Ablehnungsverfahren vor dem Landesgericht Leoben ergangene Entscheidung (GZ 2 Nc 20/10i-3) erhob er Rekurs an das Oberlandesgericht Graz, den er mit einer Ablehnung „sämtlicher Richter des Oberlandesgerichts im Zivilrechtsberufungssenat mit Ausnahme von Dr. Florentine Fromeyer “ verband.

**False Positives:**

- `Landesgericht Leoben` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Florentine Fromeyer`(person)

**Example 44** (doc_id: `deanon_TRAIN/11Os22_19y`) (sent_id: `deanon_TRAIN/11Os22_19y_5`)


Aus ihrem Anlass wird das angefochtene Urteil, das sonst unberührt bleibt, im (beide Angeklagten betreffenden) Verfallsausspruch aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht Innsbruck verwiesen.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `deanon_TRAIN/11Os22_19y`) (sent_id: `deanon_TRAIN/11Os22_19y_41`)


In diesem Umfang war die Sache zu neuer Verhandlung und Entscheidung an das Landesgericht Innsbruck zurückzuverweisen, wobei im Sinn des letzten Satzes des § 445 Abs 2 StPO der Vorsitzende des Schöffengerichts als Einzelrichter zuständig ist (RIS-Justiz RS0100271 [insbesondere T13], RS0117920 [T1]).

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `deanon_TRAIN/13Os106_17p`) (sent_id: `deanon_TRAIN/13Os106_17p_6`)


Mit Beschluss vom 27. April 2016, GZ 51 Hv 2/13f-61, wies das Landesgericht für Strafsachen Wien den Antrag des Verurteilten auf Wiederaufnahme dieses Strafverfahrens ab.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `deanon_TRAIN/12Os44_17p`) (sent_id: `deanon_TRAIN/12Os44_17p_4`)


Gründe:  Rechtliche Beurteilung Nach dem Norbert Naegelkraemer durch das Landesgericht Krems an der Donau am 4. Dezember 2015, GZ 16 Hv 32/15g-23, mehrerer Vergehen der gefährlichen Drohung nach § 107 Abs 1 StGB schuldig erkannt und zu einer teilbedingten Freiheitsstrafe verurteilt worden war, ordnete der Einzelrichter des genannten Landesgerichts nach Rechtskraft des Urteils die Zustellung der Aufforderung zum Strafantritt an den Verurteilten an.

**False Positives:**

- `Landesgericht Krems` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `deanon_TRAIN/12Os34_19w`) (sent_id: `deanon_TRAIN/12Os34_19w_4`)


Text Gründe: Im Ermittlungsverfahren gegen Viktor Mittermair und andere Beschuldigte wegen des Verbrechens der Untreue nach § 153 Abs 1 und 3 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 703 St 3/11t (nunmehr AZ 713 St 24/18i) der Staatsanwaltschaft Wien, stellte der Beschuldigte Dr. Stefan Tolmin mit Schriftsatz vom 29. November 2017 – soweit im Folgenden von Relevanz – den Antrag auf Einstellung des Ermittlungsverfahrens „gemäß § 108 StPO“ (ON 558), welchen das Landesgericht für Strafsachen Wien mit Beschluss vom 22. Juni 2018, AZ 352 HR 214/11x, abwies (ON 644).

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mittermair`(person)
- `Tolmin`(person)

**Example 49** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Hon.-Prof. Dr. Kuras und Dr. Brenn als weitere Richter in der beim Landesgericht Salzburg als Arbeits- und Sozialgericht anhängigen Rechtssache der klagenden Partei Buth Analyse GmbH, Anabel Traudtmann, vertreten durch Dr. Ernst Kohlbacher, Rechtsanwalt in Salzburg, gegen die beklagte Partei Christine Schwemmer, vertreten durch Plankel Mayrhofer & Partner, Rechtsanwälte in Dornbirn, wegen 213,52 EUR sA, über den Delegierungsantrag der beklagten Partei den Beschluss gefasst:  Spruch Der Antrag der beklagten Partei, die Rechtssache an das Arbeits- und Sozialgericht Wien zu delegieren, wird abgewiesen.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Buth Analyse GmbH`(organisation)
- `Anabel Traudtmann`(person)
- `Christine Schwemmer`(person)

**Example 50** (doc_id: `deanon_TRAIN/8Nc31_13w`) (sent_id: `deanon_TRAIN/8Nc31_13w_4`)


Text Begründung: Mit der am 14. 12. 2012 beim Landesgericht Salzburg als Arbeits- und Sozialgericht eingebrachten Mahnklage begehrte die Klägerin, eine Finanzvermittlungsgesellschaft mit Sitz in Salzburg, von dem im Bundesland Burgenland wohnhaften Beklagten die Rückzahlung von Provisionen aus einem Agentenvertrag.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `deanon_TRAIN/8Nc21_10w`) (sent_id: `deanon_TRAIN/8Nc21_10w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Spenling als Vorsitzenden sowie den Hofrat Hon.-Prof. Dr. Kuras und die Hofrätin Dr. Tarmann-Prentner als weitere Richter in der Rechtssache der klagenden Partei StadtEnergie Werke AG, Wilhelmine Hrncirik, vertreten durch Dr. Hartmut Ramsauer, Rechtsanwalt in Salzburg, gegen die beklagte Partei RgR Isabel Rövekamp, vertreten durch Frimmel/Anetter Rechtsanwaltsgesellschaft mbH in Klagenfurt am Wörthersee, wegen 4.696,20 EUR sA, über den Delegierungsantrag der beklagten Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag, an Stelle des Landesgerichts Salzburg als Arbeits- und Sozialgericht das Landesgericht Klagenfurt als Arbeits- und Sozialgericht zur Verhandlung und Entscheidung über die vorliegende Arbeitsrechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `StadtEnergie Werke AG`(organisation)
- `Wilhelmine Hrncirik`(person)
- `RgR Isabel Rövekamp`(person)

**Example 52** (doc_id: `deanon_TRAIN/8Nc21_10w`) (sent_id: `deanon_TRAIN/8Nc21_10w_5`)


Mit in Rechtskraft erwachsenem Beschluss vom 23. März 2010 erklärte sich das Bezirksgericht Salzburg für sachlich unzuständig und überwies die Rechtssache an das Landesgericht Salzburg als Arbeits- und Sozialgericht, weil nach dem Parteienvorbringen eine Rechtsstreitigkeit zwischen Arbeitgeber und Arbeitnehmer vorliege.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `deanon_TRAIN/8Nc21_10w`) (sent_id: `deanon_TRAIN/8Nc21_10w_6`)


Nach Einbringung eines vorbereitenden Schriftsatzes der Klägerin beantragte der Beklagte die Delegierung des Verfahrens gemäß § 31 JN an das Landesgericht Klagenfurt als Arbeits- und Sozialgericht.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `deanon_TRAIN/8Nc21_10w`) (sent_id: `deanon_TRAIN/8Nc21_10w_11`)


Die Rechtsfrage der Arbeitnehmerähnlichkeit von Vertriebspartnern der Klägerin sei vor dem Landesgericht Salzburg bereits wiederholt ausjudiziert worden, weshalb die neuerliche Vernehmung von Zeugen zum angebotenen Thema nicht nötig sei.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `deanon_TRAIN/11Os137_20m`) (sent_id: `deanon_TRAIN/11Os137_20m_7`)


[2] Mit (nach allseitigem Rechtsmittelverzicht [ON 27 S 4]) gekürzt ausgefertigtem Urteil vom 16. Oktober 2020, GZ 46 Hv 66/20s-27, verhängte das Landesgericht für Strafsachen Wien über Folkhard wegen am 5. und 8. Juli 2020 begangener Straftaten unter Bedachtnahme gemäß §§ 31, 40 StGB auf das vorgenannte Urteil des Landesgerichts Linz eine (nicht bedingt nachgesehene) Zusatzfreiheitsstrafe von acht Monaten.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Folkhard`(person)

**Example 56** (doc_id: `deanon_TRAIN/11Os137_20m`) (sent_id: `deanon_TRAIN/11Os137_20m_8`)


[3] Unter einem ordnete das Landesgericht für Strafsachen Wien mit gesondert ausgefertigtem Beschluss gemäß § 50 Abs 1 StGB „für die Dauer der Probezeit“ demnach ersichtlich bezogen auf die im Vor-Urteil gewährte bedingte Strafnachsicht – Bewährungshilfe an (ON 29).

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `deanon_TRAIN/18OCg2_24d`) (sent_id: `deanon_TRAIN/18OCg2_24d_5`)


Text Begründung: [1] DerKlägerbegehrt mit seiner beim Landesgericht Klagenfurt als Arbeits- und Sozialgericht eingebrachten Klage, das Erkenntnis des Schiedsgerichts der beklagten Glaubensgemeinschaft vom 18.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `deanon_TRAIN/18OCg2_24d`) (sent_id: `deanon_TRAIN/18OCg2_24d_17`)


[5] DerKlägerbeantragte für den Fall, dass sich das angerufene Landesgericht Klagenfurt für unzuständig erklären sollte, die Überweisung an den nicht offenbar unzuständigen Obersten Gerichtshof.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `deanon_TRAIN/8ObS8_22t`) (sent_id: `deanon_TRAIN/8ObS8_22t_7`)


Das Landesgericht Innsbruck eröffnete mit Beschluss vom 24.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `deanon_TRAIN/4Nc2_22i`) (sent_id: `deanon_TRAIN/4Nc2_22i_5`)


Mittel-Transport -GmbH, Steinerfeld 29, 6710 Nenzing, Österreich, vertreten durch Bernhard Scharmüller, Rechtsanwalt in Linz, wegen 226.122,45 EUR sA, über den Delegierungsantrag der klagenden Partei in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Zur Verhandlung und Entscheidung in dieser Rechtssache wird anstelle des Landesgerichts Linz das Landesgericht für Zivilrechtssachen Wien bestimmt.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mittel-Transport`(organisation)
- `Steinerfeld 29, 6710 Nenzing, Österreich`(address)

**Example 61** (doc_id: `deanon_TRAIN/4Nc2_22i`) (sent_id: `deanon_TRAIN/4Nc2_22i_9`)


Die Klägerin mit Sitz in Wien brachte beim Landesgericht Linz eine Schadenersatzklage gegen die beiden Beklagten mit Sitz in Oberösterreich ein.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `deanon_TRAIN/4Nc2_22i`) (sent_id: `deanon_TRAIN/4Nc2_22i_14`)


[2] Sowohl in der Klage als auch in einem späteren Schriftsatz beantragte die Klägerin die Delegierung des Verfahrens an das Landesgericht für Zivilrechtssachen Wien.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `deanon_TRAIN/4Nc2_22i`) (sent_id: `deanon_TRAIN/4Nc2_22i_19`)


[4] Das Landesgericht Linz hält die Delegierung für zweckmäßig.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `deanon_TRAIN/4Nc2_22i`) (sent_id: `deanon_TRAIN/4Nc2_22i_30`)


[9] Für die Delegierung spricht auch die Möglichkeit, die beiden dann am Landesgericht für Zivilrechtssachen Wien anhängigen Schadenersatzprozesse – allenfalls auch nur für die Einholung des Sachverständigengutachtens – zu verbinden, um die mehrfache Beweisaufnahme zu denselben Beweisthemen zu vermeiden und eine nicht unerhebliche Kostenersparnis zu erzielen (vgl RS0046589 [T11];

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `deanon_TRAIN/6Nc26_10s`) (sent_id: `deanon_TRAIN/6Nc26_10s_10`)


DieKlägerinbeantragt die Delegierung der Rechtssache an das Landesgericht Eisenstadt mit der Begründung, der Ort des durchzuführenden Ortsaugenscheins sei von Eisenstadt aus schneller erreichbar als von Klagenfurt aus, die meisten zu vernehmenden Personen hätten ihren Wohnsitz im Sprengel des Landesgerichts Eisenstadt, auch der Sachverständige könne von Wien aus Eisenstadt schneller erreichen als Klagenfurt.

**False Positives:**

- `Landesgericht Eisenstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `deanon_TRAIN/6Nc26_10s`) (sent_id: `deanon_TRAIN/6Nc26_10s_24`)


im Hinblick auf § 33 JN bestehen auch keine grundsätzlichen Bedenken gegen die Vornahme eines Ortsaugenscheins durch das Landesgericht Klagenfurt im Sprengel des Landesgerichts Eisenstadt (vgl dazuMayrinRechberger, ZPO³ [2006] § 33 JN Rz 1 mwN).

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `deanon_TRAIN/7Nc14_18w`) (sent_id: `deanon_TRAIN/7Nc14_18w_4`)


Matzka als weitere Richter in der beim Landesgericht Klagenfurt zu AZ 29 Cg 32/18a anhängigen Rechtssache der klagenden Partei Mag. Philipp Hinterscheid, vertreten durch Mag. Patrick Mandl, Rechtsanwalt in Wien, gegen die beklagte Partei Nexlogal-Wind Limited, Kindlerweg 65, 8786 Boder, Österreich, Vereinigtes Königreich, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, wegen Vertragsaufhebung und 43.876,22 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, anstelle des Landesgerichts Klagenfurt das Handelsgericht Wien zur Verhandlung und Entscheidung in der Rechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Mag. Philipp Hinterscheid`(person)
- `Nexlogal-Wind Limited`(organisation)
- `Kindlerweg 65, 8786 Boder, Österreich`(address)

**Example 68** (doc_id: `deanon_TRAIN/7Nc14_18w`) (sent_id: `deanon_TRAIN/7Nc14_18w_11`)


Ohne hiezu eine Äußerung der Beklagten einzuholen, legte das Landesgericht Klagenfurt den Akt zur Entscheidung vor; es folge „der vorgebrachten prozessökonomischen Argumentation“.

**False Positives:**

- `Landesgericht Klagenfurt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `deanon_TRAIN/15Os88_20k`) (sent_id: `deanon_TRAIN/15Os88_20k_5`)


Text Gründe: In der Medienrechtssache der Antragsteller Dr. Calvin Lehert und Noel Yasin gegen die Antragsgegnerin Bikmaz Bildung GmbH & Co KG wegen §§ 7 f MedienG brachten die Antragsteller beim Landesgericht für Strafsachen Wien gesondert, jeweils in einem eigenen Schriftsatz aber vertreten durch dieselbe Rechtsanwältin selbständige Entschädigungsanträge gegen die Antragsgegnerin ein.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dr. Calvin Lehert`(person)
- `Noel Yasin`(person)
- `Bikmaz Bildung GmbH`(organisation)

**Example 70** (doc_id: `deanon_TRAIN/14Os5_20x`) (sent_id: `deanon_TRAIN/14Os5_20x_12`)


Das Landesgericht Salzburg gab am 15. Mai 2019 zu AZ 49 Bl 74/18s dem auf § 195 Abs 1 Z 1 und 2 StPO gestützten Antrag (ON 19, 21) des Opfers Mag. Dr. Waltraud Ripsam, MBA, auf Fortführung des Ermittlungsverfahrens gegen die genannten Beschuldigten aus dem Grund des § 195 Abs 1 Z 1 StPO statt (ON 23).

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ripsam`(person)

**Example 71** (doc_id: `deanon_TRAIN/14Os5_20x`) (sent_id: `deanon_TRAIN/14Os5_20x_37`)


Soweit das Landesgericht Salzburg den Auftrag zur Verfahrensfortführung (auch) auf einen Verstoß gegen die Pflicht zur amtswegigen Wahrheitsforschung stützt, unterlässt es die Angabe, welche konkreten Beweise zur vollständigen Klärung des Sachverhalts aufzunehmen wären.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `deanon_TRAIN/6Ob169_25h`) (sent_id: `deanon_TRAIN/6Ob169_25h_5`)


Text Begründung: [1] Mit rechtskräftigem Berufungsurteil vom 27. 6. 2013, AZ 45 R 107/13p, bestätigte das Landesgericht für Zivilrechtssachen Wien das Urteil des Bezirksgerichts Innere Stadt Wien vom 31.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `deanon_TRAIN/11Ns5_12t`) (sent_id: `deanon_TRAIN/11Ns5_12t_3`)


Kopf Der Oberste Gerichtshof hat am 22. Februar 2012 durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Zehetner als Vorsitzenden sowie die Hofräte des Obersten Gerichtshofs Dr. Schwab, Mag. Lendl, Mag. Michel und Dr. Oshidari als weitere Richter in der Strafsache gegen Andreas Novkovic wegen des Verbrechens der Verleumdung nach § 297 Abs 1 zweiter Fall StGB und weiterer strafbarer Handlungen, AZ 112 Hv 208/11w des Landesgerichts für Strafsachen Wien, über den Kompetenzkonflikt zwischen dem Landesgericht für Strafsachen Wien und dem Landesgericht Linz nach Anhörung der Generalprokuratur gemäß § 60 Abs 1 zweiter Satz OGH-Geo.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation
- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Novkovic`(person)

**Example 74** (doc_id: `deanon_TRAIN/11Ns5_12t`) (sent_id: `deanon_TRAIN/11Ns5_12t_4`)


2005 den Beschluss gefasst:  Spruch Die Akten werden dem Landesgericht für Strafsachen Wien zur Vornahme der von § 485 Abs 1 StPO verlangten Prüfung des Strafantrags zurückgestellt.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `deanon_TRAIN/11Ns5_12t`) (sent_id: `deanon_TRAIN/11Ns5_12t_7`)


Mit Beschluss vom 4. Jänner 2012, GZ 112 Hv 208/11w-43, ordnete die Einzelrichterin des Landesgerichts für Strafsachen Wien die Abtretung des Strafverfahrens „gemäß § 37 Abs 1 und Abs 2, Satz 2 und 3 StPO an das Landesgericht Linz“ wegen Führung des Ermittlungsverfahrens durch die Staatsanwaltschaft Linz und wegen Zuständigkeit aufgrund der früheren Straftat an.

**False Positives:**

- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `deanon_TRAIN/11Ns5_12t`) (sent_id: `deanon_TRAIN/11Ns5_12t_12`)


Da vorliegend weder das Landesgericht für Strafsachen Wien noch das Landesgericht Linz einen Beschluss gemäß § 485 Abs 1 Z 1 StPO gefasst, ausgefertigt und sämtlichen zur Beschwerde Berechtigten zugestellt (§ 86 StPO; vglBauer, WK-StPO § 450 Rz 5 f) haben, war der Akt - in Übereinstimmung mit der Stellungnahme der Generalprokuratur - der Einzelrichterin des Landesgerichts für Strafsachen Wien zurückzustellen.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation
- `Landesgericht Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 77** (doc_id: `deanon_TRAIN/11Os13_11p`) (sent_id: `deanon_TRAIN/11Os13_11p_4`)


Aus Anlass der Nichtigkeitsbeschwerde wird das angefochtene Urteil, das im Übrigen unberührt bleibt, in dem Renate Tug betreffenden Abschöpfungserkenntnis aufgehoben und die Sache im Umfang der Aufhebung zu neuer Verhandlung und Entscheidung an das Landesgericht Eisenstadt verwiesen.

**False Positives:**

- `Landesgericht Eisenstadt` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tug`(person)

**Example 78** (doc_id: `deanon_TRAIN/13Os90_16h`) (sent_id: `deanon_TRAIN/13Os90_16h_5`)


Aus deren Anlass wird das angefochtene Urteil, das im Übrigen unberührt bleibt, in der Subsumtion dem Angeklagten Thomas Voborny angelasteter Taten nach § 148 zweiter Fall StGB, in der zum Schuldspruch A gebildeten Subsumtionseinheit, demzufolge auch im diesen Angeklagten betreffenden Strafausspruch, sowie im Verfallserkenntnis aufgehoben und die Sache in diesem Umfang zu neuer Verhandlung und Entscheidung an das Landesgericht für Strafsachen Wien verwiesen.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Voborny`(person)

**Example 79** (doc_id: `deanon_TRAIN/3Ob137_18w_3Nc20_18y_`) (sent_id: `deanon_TRAIN/3Ob137_18w_3Nc20_18y__10`)


Im ersten Rechtsgang wies das Landesgericht für Zivilrechtssachen Wien das Hauptbegehren ab und gab dem Eventualbegehren statt.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 80** (doc_id: `deanon_TRAIN/12Os152_19y`) (sent_id: `deanon_TRAIN/12Os152_19y_16`)


Zugleich fasste das Landesgericht Salzburg den Beschluss, vom Widerruf der dem Genannten gewährten bedingten Entlassung zu AZ 42 BE 3/12v des Landesgerichts Salzburg sowie vom Widerruf der bedingten Strafnachsichten zu AZ 35 Hv 66/16t und AZ 61 Hv 122/17w des Landesgerichts Salzburg abzusehen und die zu AZ 61 Hv 122/17w bestehende Probezeit auf fünf Jahre zu verlängern (ON 27 S 3).

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `deanon_TRAIN/12Os152_19y`) (sent_id: `deanon_TRAIN/12Os152_19y_17`)


Weiters beschloss das Landesgericht Salzburg, „gemäß § 53 StGB in Verbindung mit § 494a Abs 1 Z 4 StPO“ die bedingte Nachsicht des mit Urteil dieses Gerichts vom 20. Jänner 2015 zu AZ 41 Hv 151/14h verhängten „Freiheitsstrafenteils von drei Monaten aus Anlass der neuerlichen Verurteilung zu widerrufen“ (ON 27 S 4).

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `deanon_TRAIN/12Os152_19y`) (sent_id: `deanon_TRAIN/12Os152_19y_20`)


Indem das Landesgericht Salzburg aus Anlass der zu GZ 29 Hv 11/19i-27 erfolgten Verurteilung des Josef Lackerschmid den Widerruf der ihm zu AZ 41 Hv 151/14h des Landesgerichts Salzburg gewährten bedingten Strafnachsicht nur hinsichtlich eines Teils (im Ausmaß von drei Monaten) des in Rede stehenden bedingt nachgesehenen Strafteils (von sechs Monaten) beschloss, hat es seine Strafbefugnis überschritten, weil diese in Ansehung der Entscheidung über den Widerruf der bedingten Strafnachsicht zu AZ 41 Hv 151/14h des Landesgerichts Salzburg darauf beschränkt war, den gesamten seinerzeit bedingt nachgesehenen Sanktionsteil zu widerrufen oder vom Widerruf dieser bedingten Strafnachsicht abzusehen.

**False Positives:**

- `Landesgericht Salzburg` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lackerschmid`(person)

**Example 83** (doc_id: `deanon_TRAIN/12Os71_19m_12Os72_19h_`) (sent_id: `deanon_TRAIN/12Os71_19m_12Os72_19h__5`)


Der dagegen gerichteten Beschwerde hatte das Landesgericht Innsbruck als Vollzugsgericht vom 17. Mai 2018, AZ 22 Bl 38/18f, 22 Bl 43/18s, nicht Folge gegeben.

**False Positives:**

- `Landesgericht Innsbruck` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `deanon_TRAIN/10Nc24_11b`) (sent_id: `deanon_TRAIN/10Nc24_11b_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Hradil als Vorsitzenden sowie die Hofräte Dr. Fellinger und Dr. Hoch als weitere Richter in der Rechtssache der klagenden Partei C. Furtwil-Garten GmbH, Dürnhof 20, 4725 Kahlberg, Österreich, vertreten durch Dr. Carl Benkhofer, Rechtsanwalt in Wien, gegen die beklagte Partei Gebhard Gamelin, BSc LLB, vertreten durch Greiml & Horwath RechtsanwaltsPartnerschaft in Graz, wegen 60.000 EUR sA, AZ 13 Cg 90/11k des Landesgerichts für Zivilrechtssachen Graz, über den Delegierungsantrag der klagenden Partei den Beschluss gefasst:  Spruch Der Antrag, die Rechtssache an das Landesgericht für Zivilrechtssachen Wien zu delegieren, wird abgewiesen.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Furtwil-Garten GmbH`(organisation)
- `Dürnhof 20, 4725 Kahlberg, Österreich`(address)
- `Gebhard Gamelin, BSc LLB`(person)

**Example 85** (doc_id: `deanon_TRAIN/10Nc24_11b`) (sent_id: `deanon_TRAIN/10Nc24_11b_7`)


Weiters beantragte sie die Delegierung des Verfahrens an das Landesgericht für Zivilrechtssachen Wien, weil dies zu einer wesentlichen Verkürzung des Verfahrens, zur Erleichterung des Gerichtszugangs und zu einer wesentlichen Verbilligung des Rechtsstreits führe.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 86** (doc_id: `deanon_TRAIN/10Nc24_11b`) (sent_id: `deanon_TRAIN/10Nc24_11b_18`)


Das Landesgericht für Zivilrechtssachen Graz befürwortete die Delegierung im Wesentlichen mit der Begründung, dass durch die Durchführung des gesamten Beweisverfahrens in Wien jedenfalls eine raschere und kostengünstigere Verfahrensführung gewährleistet sei.

**False Positives:**

- `Landesgericht für` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Magistrate City Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5b8b1658`  
**Description:**
Matches Magistrat der Stadt followed by city name, including genitive forms and department codes.

**Content:**
```
(?i)\bMagistrat(?:s)?\s+der\s+Stadt\s+([A-Za-zäöüÄÖÜ]+(?:\s+MA\s+\d+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 392 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10Ob25_25m`) (sent_id: `deanon_TRAIN/10Ob25_25m_4`)


Claire Al-Hakim, beide vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Rechtsvertretung Bezirk 21, 1210 Wien, Franz-Jonas-Platz 12), wegen Unterhaltsvorschuss, über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 22. November 2024, GZ 45 R 496/24k-26, mit dem der Beschluss des Bezirksgerichts Floridsdorf vom 2. August 2024, GZ 16 Pu 19/24a-20, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Claire Al-Hakim`(person)

**Example 1** (doc_id: `deanon_TRAIN/7Ob119_18b`) (sent_id: `deanon_TRAIN/7Ob119_18b_4`)


Matzka als weitere Richter in der Pflegschaftssache der Minderjährigen Silke Wieging, geboren am 20. März 2010, 12. September 1996, vertreten durch das Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 12, 13, 23, 1230 Wien, Rößlergasse 15, Mutter Fiona Wenzlick, Vater Viola Peiniger, vertreten durch Dr. Tassilo Wallentin LL.M, Rechtsanwalt in Wien, wegen Unterhalt, infolge Revisionsrekurses des Vaters gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 8. Mai 2018, GZ 44 R 104/18x-180, womit der Rekurs des Vaters gegen den Beschluss des Bezirksgerichts Meidling vom 25. Jänner 2018, GZ 1 Pu 73/10b-173, teilweise zurückgewiesen und ihm im Übrigen nicht Folge gegeben wurde, den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht zurückgestellt.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Silke Wieging`(person)
- `20. März`(date)
- `12. September 1996`(date)
- `Fiona Wenzlick`(person)
- `Viola Peiniger`(person)

**Example 2** (doc_id: `deanon_TRAIN/8Ob1_20k`) (sent_id: `deanon_TRAIN/8Ob1_20k_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsrekursgericht durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden sowie die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn, den Hofrat Dr. Stefula und die Hofrätin Mag. Wessely-Kristöfel als weitere Richter in der Pflegschaftssache der mj Niklas Chomicz, geboren am 6. Oktober 2009, 17. Mai 2000, vertreten durch den Magistrat der Stadt Wien, Wiener Kinder- und Jugendhilfe, Rechtsvertretung für den Bezirk 10, 1100 Wien, Alfred-Adler-Straße 12, wegen Unterhalt, über den Revisionsrekurs des Kindes gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 15. Oktober 2019, GZ 45 R 363/19v-47, mit dem der Beschluss des Bezirksgerichts Favoriten vom 5. Juni 2019, GZ 8 Pu 52/10k-40, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Niklas Chomicz`(person)
- `6. Oktober`(date)
- `17. Mai 2000`(date)

**Example 3** (doc_id: `deanon_TRAIN/10Ob26_18y`) (sent_id: `deanon_TRAIN/10Ob26_18y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden und durch die Hofrätinnen und Hofräte Dr. Fichtenau, Dr. Grohmann, Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Pflegschaftssache des minderjährigen VetR Lee Rietze, geboren am 11. November 2014, vertreten durch das Land Oberösterreich als Kinder- und Jugendhilfeträger (Magistrat der Stadt Linz, Abteilung für Soziales, Jugend und Familie, 4040 Linz, Hauptstraße 1–5), wegen Unterhalt und Unterhaltsvorschuss, über den Revisionsrekurs des Vaters und Unterhaltsverpflichteten Dipl.-Ing. Mercedes Rheinfeldt (bei Frau Marion Pinschmidt ), Rumänien, vertreten durch Mag. Michael Schenk, Rechtsanwalt in Linz, gegen den Beschluss des Landesgerichts Linz als Rekursgericht vom 23. Jänner 2017, GZ 15 R 273/16x, 15 R 274/16v-62, womit die Beschlüsse des Bezirksgerichts Linz vom 15. Dezember 2015, GZ 24 PU 504/14a-36 und -37, bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Magistrat der Stadt Linz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `VetR Lee Rietze`(person)
- `11. November`(date)
- `Dipl.-Ing. Mercedes Rheinfeldt`(person)
- `Marion Pinschmidt`(person)

**Example 4** (doc_id: `deanon_TRAIN/10Ob82_10x`) (sent_id: `deanon_TRAIN/10Ob82_10x_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden und durch die Hofräte Dr. Fellinger, Dr. Hoch, Dr. Schramm und die Hofrätin Dr. Fichtenau als weitere Richter in der Pflegschaftssache des mj Dimitri Ratzenböck, geboren am 6. August 1956, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, MA 11 Amt für Jugend und Familie, Rechtsvertretung für den 3. und 11.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dimitri Ratzenböck`(person)
- `6. August 1956`(date)

**Example 5** (doc_id: `deanon_TRAIN/5Ob187_19i`) (sent_id: `deanon_TRAIN/5Ob187_19i_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Jensik als Vorsitzenden sowie die Hofrätin Dr. Grohmann und die Hofräte Mag. Wurzer, Mag. Painsi und Dr. Steger als weitere Richter in der Pflegschaftssache des mj Konrad Mayr, geboren am 1. August 2020, und der mj Jean Angelis, geboren am 3. Oktober 2014, beide wohnhaft bei der Mutter Leonie Erbut, vertreten durch die Stadt Wien (Wiener Kinder- und Jugendhilfe des Magistrats der Stadt Wien) als Kinder- und Jugendhilfeträger, wegen Unterhalts, über den Revisionsrekurs der Kinder gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 2. Juli 2019, GZ 45 R 317/19d-40, mit dem der Beschluss des Bezirksgerichts Favoriten vom 10. Mai 2019, GZ 6 Pu 62/15y-32, teilweise bestätigt, teilweise abgeändert wurde, den Beschluss gefasst:  Spruch Dem Revisionsrekurs wird nicht Folge gegeben.

**False Positives:**

- `Magistrats der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Konrad Mayr`(person)
- `1. August 2020`(date)
- `Jean Angelis`(person)
- `3. Oktober 2014`(date)
- `Leonie Erbut`(person)

**Example 6** (doc_id: `deanon_TRAIN/10Ob31_18h`) (sent_id: `deanon_TRAIN/10Ob31_18h_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Univ.-Prof. Dr. Neumayr als Vorsitzenden, die Hofrätinnen Dr. Fichtenau und Dr. Grohmann, sowie die Hofräte Mag. Ziegelbauer und Dr. Stefula als weitere Richter in der Pflegschaftssache der mj 1. OStR Klaus Schepers, geboren am Paulina Dutzschke, 2. Paulina Davisson, geboren am Rudolf Leirer, Bakk. art., 3. Evamaria Yakubov, geboren am 4. April 1998 und 4. OStR Guntram Sepan, geboren am 24. Februar 1988, alle vertreten durch das Land Wien als Kinder- und Jugendhilfeträger (Magistrat der Stadt Wien, Amt für Jugend und Familie Rechtsvertretung Bezirke 2, 20), 1200 Wien, Dresdnerstraße 43, wegen Unterhaltsvorschuss, infolge des Revisionsrekurses des Bundes, vertreten durch den Präsidenten des Oberlandesgerichts Wien gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 6. Dezember 2017, GZ 45 R 413/17v, 45 R 414/17s, 45 R 415/17p, 45 R 416/17k, 45 R 545/17f-48, womit die Beschlüsse des Bezirksgerichts Leopoldstadt vom 4. Juli 2017, GZ 3 Pu 123/16g-22, -23, -24, -25 (ON 25 in der Fassung des Berichtigungsbeschlusses vom 5. Juli 2017, GZ 3 Pu 123/16g-26), bestätigt wurden, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Akten werden dem Erstgericht mit dem Auftrag zurückgestellt, 1. den Träger der Kinder- und Jugendhilfe binnen einer Frist von 14 Tagen zur Klarstellung aufzufordern, ob die Erklärung der Zurückziehung der Unterhaltsvorschussanträge der Kinder vom 23.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `OStR Klaus Schepers`(person)
- `Paulina Dutzschke`(person)
- `Paulina Davisson`(person)
- `Rudolf Leirer, Bakk. art.`(person)
- `Evamaria Yakubov`(person)
- `4. April 1998`(date)
- `OStR Guntram Sepan`(person)
- `24. Februar 1988`(date)

**Example 7** (doc_id: `deanon_TRAIN/10Ob22_10y`) (sent_id: `deanon_TRAIN/10Ob22_10y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Dr. Schinko als Vorsitzenden sowie die Hofräte Dr. Fellinger, Dr. Hoch, Hon.-Prof. Dr. Neumayr und Dr. Schramm als weitere Richter in der Pflegschaftssache der minderjährigen Annabelle Tiedke, geboren am 24. Juni 2001, vertreten durch das Land Wien als Jugendwohlfahrtsträger (Magistrat der Stadt Wien, Amt für Jugend und Familie - Rechtsvertretung, Bezirk 10, 1100 Wien, Van der Nüll-Gasse 20), über den Revisionsrekurs der Minderjährigen gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 17. September 2009, GZ 44 R 454/09d-38, womit infolge Rekurses des Vaters der Beschluss des Bezirksgerichts Favoriten vom 16. Juni 2009, GZ 40 P 36/08f-U-26, teilweise abgeändert wurde, den B e s c h l u s s gefasst:  Spruch Dem Revisionsrekurs wird Folge gegeben.

**False Positives:**

- `Magistrat der Stadt Wien` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Tiedke`(person)

**Example 8** (doc_id: `deanon_TRAIN/10Ob22_10y`) (sent_id: `deanon_TRAIN/10Ob22_10y_17`)


5. 2009 auch dem „Magistrat der Stadt Wien MA 11, AJF-R Bezirk 10, Van der Nüll-Gasse 20, 1100 Wien“ als gesetzlichen Vertreter der Minderjährigen zugestellt und von einem Postbevollmächtigten des Jugendamts übernommen wurde.

**False Positives:**

- `Magistrat der Stadt Wien MA 11` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `deanon_TRAIN/10Ob22_10y`) (sent_id: `deanon_TRAIN/10Ob22_10y_52`)


Nach dem im Akt befindlichen Rückschein wurde der Beschluss über die pflegschaftsgerichtliche Genehmigung des Scheidungsvergleichs richtigerweise dem „Magistrat der Stadt Wien MA 11, AJF-R Bezirk 10, Van der Nüll-Gasse 20, 1100 Wien“ als gesetzlichen Vertreter der Minderjährigen zugestellt und von einem Postbevollmächtigten dieser Dienststelle übernommen.

**False Positives:**

- `Magistrat der Stadt Wien MA 11` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Law Firm GmbH/OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ce418579`  
**Description:**
Matches law firms ending in Rechtsanwälte GmbH/OG with names, ensuring no preceding context is included.

**Content:**
```
(?i)(?<![a-zäöüß\s])(?<!\w)([A-Z][a-zäöüÄÖÜ]+(?:\s+[A-Z][a-zäöüÄÖÜ]+)*(?:\s+&\s+[A-Z][a-zäöüÄÖÜ]+)*\s+Rechtsanwälte\s+(?:GmbH|OG))(?=\s|,|\.|\(|\)|;|:|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 13 | 0 | 13 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 13 | 351 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/9ObA141_19d`) (sent_id: `deanon_TRAIN/9ObA141_19d_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätin des Obersten Gerichtshofs Dr. Fichtenau und den Hofrat des Obersten Gerichtshof Dr. Hargassner sowie die fachkundigen Laienrichter Dr. Peter Zeitler (aus dem Kreis der Arbeitnehmer) und Angela Taschek (aus dem Kreis der Arbeitgeber) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Adelheid Haaf, LLB, vertreten durch Dr. Thomas Krankl, Rechtsanwalt in Wien, gegen die beklagte Partei Nossack Analyse AG, Sascha Steinke, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 1.397.481,32 EUR netto sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 29. Oktober 2019, GZ 9 Ra 14/19y-44, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch 1.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Adelheid Haaf, LLB`(person)
- `Nossack Analyse AG`(organisation)
- `Sascha Steinke`(person)

**Example 1** (doc_id: `deanon_TRAIN/8Ob4_18y`) (sent_id: `deanon_TRAIN/8Ob4_18y_4`)


Vossbrinck Wind AG, Flurnsbach 9, 4722 Untwüsten, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte GmbH in Wien, und 2. Steinheim-Cloud Limited, Anlauftalstraße 23, 4623 Kalchau, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.141,02 EUR, über die Revision der erstbeklagten Partei gegen das Teilurteil des Handelsgerichts Wien als Berufungsgericht vom 18. September 2017, GZ 60 R 20/17x-29, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 3. Jänner 2017, GZ 20 C 529/15p-24, in der Hauptsache hinsichtlich der erstbeklagten Partei bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Vossbrinck Wind AG`(organisation)
- `Flurnsbach 9, 4722 Untwüsten, Österreich`(address)
- `Steinheim-Cloud Limited`(organisation)
- `Anlauftalstraße 23, 4623 Kalchau, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/8ObA72_19z`) (sent_id: `deanon_TRAIN/8ObA72_19z_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten Hon.-Prof. Dr. Kuras als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Wessely-Kristöfel als weitere Richter sowie die fachkundigen Laienrichter Johannes Püller (aus dem Kreis der Arbeitgeber) und Mag. Michael Puhm (aus dem Kreis der Arbeitnehmer) in der Arbeitsrechtssache der klagenden Partei Hermine Thom, vertreten durch Dr. Markus Orgler, Rechtsanwalt in Innsbruck, gegen die beklagte Partei Mur Brucktridon AG, Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat., vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 4.200,83 EUR sA, über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 17. Oktober 2019, GZ 13 Ra 41/15z-30, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hermine Thom`(person)
- `Mur Brucktridon AG`(organisation)
- `Dipl.-Ing. Griselda Lamberty, Bakk. rer. nat.`(person)

**Example 3** (doc_id: `deanon_TRAIN/7Ob11_22a`) (sent_id: `deanon_TRAIN/7Ob11_22a_6`)


IT Sudtraver GmbH, Wald-Marine, und 2. Tal Seewil GmbH, Grappaweg 1, 5310 Hof, Österreich, beide vertreten durch die DLA Piper Weiss-Tessbach Rechtsanwälte GmbH in Wien, wegen Herausgabe und Feststellung, über die außerordentliche Revision der klagenden Parteien gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 25. November 2021, GZ 4 R 149/21s-23, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Tessbach Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `IT Sudtraver GmbH`(organisation)
- `Wald-Marine`(organisation)
- `Tal Seewil GmbH`(organisation)
- `Grappaweg 1, 5310 Hof, Österreich`(address)

**Example 4** (doc_id: `deanon_TRAIN/5Ob202_09f`) (sent_id: `deanon_TRAIN/5Ob202_09f_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten des Obersten Gerichtshofs Hon.-Prof. Dr. Danzl als Vorsitzenden sowie die Hofrätinnen/Hofräte des Obersten Gerichtshofs Dr. Hurch, Dr. Lovrek, Dr. Höllwerth und Dr. Tarmann-Prentner als weitere Richter in der außerstreitigen Rechtssache der Antragstellerin Kadzimirsz Sicherheit GmbH, Rottenmannerstraße 19, 3231 Wieden, Österreich, vertreten durch Dr. Karl Grigkar, Rechtsanwalt in Wien, wider den Antragsgegner Herbert Dietmaier, vertreten durch Hule Bachmayr-Heyda Nordberg Rechtsanwälte GmbH in Wien, wegen § 12a iVm § 46 Abs 2 MRG, über den Revisionsrekurs der Antragstellerin gegen den Sachbeschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 28. Mai 2009, GZ 39 R 2/09z-17, womit infolge Rekurses der Antragstellerin der Sachbeschluss des Bezirksgerichts Innere Stadt Wien vom 27. Oktober 2008, GZ 48 Msch 9/08v-11, bestätigt wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Revisionsrekurs wird zurückgewiesen.

**False Positives:**

- `Heyda Nordberg Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Kadzimirsz Sicherheit GmbH`(organisation)
- `Rottenmannerstraße 19, 3231 Wieden, Österreich`(address)
- `Herbert Dietmaier`(person)

**Example 5** (doc_id: `deanon_TRAIN/9Ob67_09g`) (sent_id: `deanon_TRAIN/9Ob67_09g_5`)


Babette Wienkemeier, 3. HR Dario Litwinowa, 4. Eigenbrod Versicherung GmbH & Co KG, Dr. Franz Stumpf-Straße 48, 2002 Ottendorf, Österreich, 5. Dr. David Alswede, 6. Dipl.-Ing. Manuela Himmel, vertreten durch die Gassauer-Fleissner Rechtsanwälte GmbH in Wien, gegen die beklagte Partei Ing. Felizia Tscherning, vertreten durch Mag. Markus Adam, Rechtsanwalt in Wien, wegen Räumung (Streitwert 8.954,16 EUR), über die Revision der beklagten Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Wien als Berufungsgericht vom 16. Juni 2009, GZ 41 R 98/09d-12, womit das Urteil des Bezirksgerichts Innere Stadt Wien vom 26. Februar 2009, GZ 30 C 200/08y-7, teilweise abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Die Revision der beklagten Partei wird zurückgewiesen.

**False Positives:**

- `Fleissner Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Babette Wienkemeier`(person)
- `HR Dario Litwinowa`(person)
- `Eigenbrod Versicherung GmbH`(organisation)
- `Dr. Franz Stumpf-Straße 48, 2002 Ottendorf, Österreich`(address)
- `Dr. David Alswede`(person)
- `Dipl.-Ing. Manuela Himmel`(person)
- `Ing. Felizia Tscherning`(person)

**Example 6** (doc_id: `deanon_TRAIN/1Ob38_21a`) (sent_id: `deanon_TRAIN/1Ob38_21a_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch den Senatspräsidenten Univ.-Prof. Dr. Bydlinski als Vorsitzenden sowie die Hofräte und die Hofrätin Mag. Wurzer, Mag. Dr. Wurdinger, Dr. Hofer-Zeni-Rennhofer und Dr. Parzmayr als weitere Richter in der Rechtssache der klagenden Partei HR Janet Henken, vertreten durch die Greiml & Horwath Rechtsanwaltspartnerschaft, Graz, gegen die beklagte Partei Elvira Nossal, vertreten durch die Neger/Ulm Rechtsanwälte GmbH, Graz, wegen 6.720 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Landesgerichts für Zivilrechtssachen Graz als Berufungsgericht vom 3. Juni 2020, GZ 6 R 115/20f-20, mit dem das Urteil des Bezirksgerichts Deutschlandsberg vom 20. März 2020, GZ 11 C 55/19t-16, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Ulm Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Janet Henken`(person)
- `Elvira Nossal`(person)

**Example 7** (doc_id: `deanon_TRAIN/8ObA43_16f`) (sent_id: `deanon_TRAIN/8ObA43_16f_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Vizepräsidenten Prof. Dr. Spenling als Vorsitzenden, die Hofrätinnen Dr. Tarmann-Prentner und Mag. Korn sowie die fachkundigen Laienrichter Dr. Christoph Kainz und Mag. Canan Aytekin-Yildirim als weitere Richter in der Arbeitsrechtssache der klagenden Partei HR Charlotte Hiemer, vertreten durch Freimüller/Obereder/Pilz Rechtsanwält_Innen GmbH in Wien, gegen die beklagte Partei WaldTelekom Betriebe AG, Selina Dorpmanns, BA, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 16.482,15 EUR brutto sA und Feststellung (Streitwert 2.000 EUR), über die außerordentliche Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Wien als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 28. April 2016, GZ 10 Ra 113/15h-61, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `HR Charlotte Hiemer`(person)
- `WaldTelekom Betriebe AG`(organisation)
- `Selina Dorpmanns, BA`(person)

**Example 8** (doc_id: `deanon_TRAIN/7Ob30_10b`) (sent_id: `deanon_TRAIN/7Ob30_10b_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Senatspräsidentin des Obersten Gerichtshofs Dr. Huber als Vorsitzende und die Hofräte des Obersten Gerichtshofs Dr. Schaumüller, Dr. Hoch, Dr. Kalivoda und Dr. Roch als weitere Richter in der Rechtssache der klagenden Partei Hoch Verval GmbH, Andreas Bluemke, vertreten durch Piaty Müller-Mezin Schoeller Rechtsanwälte GmbH in Graz, gegen die beklagte Partei Härtkorn Versicherung Versicherung AG, Teurniastraße 17, 4063 Aistental, Österreich, vertreten durch Christandl Rechtsanwalt GmbH in Graz, wegen 18.409,80 EUR sA, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Graz als Berufungsgericht vom 4. Juni 2009, GZ 4 R 47/09b-33, womit das Urteil des Landesgerichts für Zivilrechtssachen Graz vom 10. Dezember 2008, GZ 14 Cg 195/05f-26, bestätigt wurde, zu Recht erkannt:  Spruch

**False Positives:**

- `Mezin Schoeller Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Hoch Verval GmbH`(organisation)
- `Andreas Bluemke`(person)
- `Härtkorn Versicherung`(organisation)
- `Teurniastraße 17, 4063 Aistental, Österreich`(address)

**Example 9** (doc_id: `deanon_TRAIN/6Ob145_21y`) (sent_id: `deanon_TRAIN/6Ob145_21y_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Gitschthaler als Vorsitzenden, den Hofrat Dr. Nowotny, die Hofrätinnen Dr. Hofer-Zeni-Rennhofer und Dr. Faber und den Hofrat Mag. Pertmayr als weitere Richter in der Rechtssache der gefährdeten Partei Dipl.-Ing. Kirstin Iseler, MA Bakk. rer. nat., vertreten durch DORDA Rechtsanwälte GmbH in Wien, wider die Gegnerin der gefährdeten Partei Wilfried Pawell, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen Unterlassung, über den Rekurs der gefährdeten Partei gegen den Beschluss des Landesgerichts für Zivilrechtssachen Wien als Rekursgericht vom 26. Mai 2021, GZ 47 R 99/21p-19, womit aus Anlass des Rekurses der Gegnerin der gefährdeten Partei die einstweilige Verfügung des Bezirksgerichts Favoriten vom 3. April 2021, GZ 56 C 107/21m-2, als nichtig aufgehoben wurde, den Beschluss gefasst:  Spruch Dem Rekurs wirdFolge gegeben.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Dipl.-Ing. Kirstin Iseler, MA Bakk. rer. nat.`(person)
- `Wilfried Pawell`(person)

**Example 10** (doc_id: `deanon_TRAIN/10Ob22_25w`) (sent_id: `deanon_TRAIN/10Ob22_25w_3`)


Kopf Der Oberste Gerichtshof hat durch den Senatspräsidenten Hon.-Prof. Dr. Nowotny als Vorsitzenden sowie die Hofräte Mag. Schober, Dr. Annerl, Dr. Vollmaier und die Hofrätin Dr. Wallner-Friedl als weitere Richter in der Pflegschaftssache der minderjährigen Lorenz Leimbrock, geboren am 27. September 2021, wohnhaft bei der Mutter MedR Franka Bimboese, vertreten durch die Pacher & Partner Rechtsanwälte GmbH & Co KG in Graz, wegen Unterhalt, über den Revisionsrekurs des Vaters Konrad Czeponik, vertreten durch die Prutsch-Lang & Damitner Rechtsanwälte OG in Graz, gegen den Beschluss des Landesgerichts für Zivilrechtssachen Graz als Rekursgericht vom 17. Jänner 2025, GZ 2 R 18/25v-17, mit dem der Beschluss des Bezirksgerichts Graz-Ost vom 29. November 2024, GZ 256 Pu 85/24f-8, bestätigt wurde, den Beschluss gefasst:  Spruch Der Revisionsrekurs und die Revisionsrekursbeantwortung werden zurückgewiesen.

**False Positives:**

- `Lang & Damitner Rechtsanwälte OG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Lorenz Leimbrock`(person)
- `27. September`(date)
- `MedR Franka Bimboese`(person)
- `Konrad Czeponik`(person)

**Example 11** (doc_id: `deanon_TRAIN/1Ob66_25z`) (sent_id: `deanon_TRAIN/1Ob66_25z_4`)


TEXS Pharma AG, Schlattengasse 7, 8213 Hartensdorf, Österreich, vertreten durch durch die CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 44.826,53 EUR sA, im Verfahren über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 12. Dezember 2024, GZ 3 R 135/24d-73, mit dem das Urteil des Landesgerichts Wels vom 28. August 2024, GZ 36 Cg 40/20i-67, abgeändert wurde, in nichtöffentlicher Sitzung den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei auf Fortsetzung des Verfahrens wird abgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `TEXS Pharma AG`(organisation)
- `Schlattengasse 7, 8213 Hartensdorf, Österreich`(address)

**Example 12** (doc_id: `deanon_TRAIN/9ObA146_19i`) (sent_id: `deanon_TRAIN/9ObA146_19i_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht in Arbeits- und Sozialrechtssachen durch den Senatspräsidenten des Obersten Gerichtshofs Dr. Hopf als Vorsitzenden, die Hofrätinnen Dr. Fichtenau und Mag. Korn sowie die fachkundigen Laienrichter Peter Zeitler (aus dem Kreis der Arbeitgeber) und Angela Taschek (aus dem Kreis der Arbeitnehmer) als weitere Richter in der Arbeitsrechtssache der klagenden Partei Ruprecht Pressl, vertreten durch Dr. Peter Wallnöfer, Mag. Eva Suitner, Rechtsanwälte in Innsbruck, gegen die beklagte Partei Sudcondon-Sicherheit AG, Lydia Pahlenkemper, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 13.546,49 EUR brutto sA und Feststellung (Streitwert: 2.180 EUR), über die außerordentliche Revision der beklagten Partei gegen das Urteil des Oberlandesgerichts Innsbruck als Berufungsgericht in Arbeits- und Sozialrechtssachen vom 6. November 2019, GZ 13 Ra 32/19g-16, den Beschluss gefasst:  Spruch Die außerordentliche Revision wird gemäß § 508a Abs 2 ZPO mangels der Voraussetzungen des § 502 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `Rohrwig Hainz Rechtsanwälte GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Ruprecht Pressl`(person)
- `Sudcondon-Sicherheit AG`(organisation)
- `Lydia Pahlenkemper`(person)

</details>

---

## `Frontex Full Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `681718dd`  
**Description:**
Matches the full name of Frontex organization.

**Content:**
```
(?i)\b(Europäische\s+Grenzschutzagentur(?:\s+Frontex)?|Europäischer\s+Grenzschutzagentur(?:\s+Frontex)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Swiss Invalid Insurance`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ee22bdd0`  
**Description:**
Matches Eidgenössische Invalidenversicherung.

**Content:**
```
(?i)\b(Eidgenössische\s+Invalidenversicherung(?:\s*\(IV\))?|Eidgenössischen\s+Invalidenversicherung(?:\s*\(IV\))?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Swiss Accident Insurance Full`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `df745eac`  
**Description:**
Matches Schweizerische Unfallversicherungsanstalt with optional SUVA.

**Content:**
```
(?i)\b(Schweizerische\s+Unfallversicherungsanstalt(?:\s*\(\s*SUVA\s*\))?|Schweizerischen\s+Unfallversicherungsanstalt(?:\s*\(\s*SUVA\s*\))?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kantonsspitals St. Gallen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `eccd5055`  
**Description:**
Matches Kantonsspitals St. Gallen.

**Content:**
```
(?i)\b(Kantonsspitals\s+St\.\s+Gallen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Steueramt Kanton`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `226aba28`  
**Description:**
Matches Steueramt des Kantons followed by city.

**Content:**
```
(?i)\b(Steueramt\s+des\s+Kantons\s+([A-Za-zäöüÄÖÜ]+))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Higher Technical School`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1f68648f`  
**Description:**
Matches Höhere Lehranstalt for specific fields.

**Content:**
```
(?i)\b(Höhere\s+Lehranstalt\s+für\s+[A-Za-zäöüÄÖÜ\s,]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Real Estate Office`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e8579088`  
**Description:**
Matches Immobilienbüro followed by name.

**Content:**
```
(?i)\b(Immobilienbüro\s+[A-Za-zäöüÄÖÜ]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Federal Ministry of Justice`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `e4ecd3f6`  
**Description:**
Matches Bundesministeriums für Justiz.

**Content:**
```
(?i)\b(Bundesministeriums\s+für\s+Justiz)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 245 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/1Ob41_18p`) (sent_id: `deanon_TRAIN/1Ob41_18p_17`)


2016 langten die Gerichtsstücke mit dem Bericht der österreichischen Botschaft in Moskau und einer Erklärung des Bundesministeriums für Justiz, wonach die russischen Gesetze keine Zustellung gegen den Willen eines Empfängers vorsehen, beim Erstgericht ein.

**False Positives:**

- `Bundesministeriums für Justiz` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Austrian Society for European Politics`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f7433ca7`  
**Description:**
Matches Österreichische Gesellschaft für Europapolitik.

**Content:**
```
(?i)\b(Österreichische\s+Gesellschaft\s+für\s+Europapolitik)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BM für Finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `b35d19c6`  
**Description:**
Matches BM für Finanzen.

**Content:**
```
(?i)\b(BM\s+für\s+Finanzen)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Retailers List`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `36560a7c`  
**Description:**
Matches common retailer names.

**Content:**
```
(?i)\b(Ikea|Obi|Leiner|Möbelix|MömaX|Otto\.de|xxxLutz|Quelle\.at)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 195 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/10ObS101_10s`) (sent_id: `deanon_TRAIN/10ObS101_10s_27`)


Dazu führte es aus, bei der Frage der Verweisbarkeit gelernter Maurer auf die Tätigkeit des Fachmarktberaters sei bisher nicht (bzw nicht ausreichend) zwischen der Tätigkeit in Baustoffabteilungen „klassischer“ SB-Baumärkte (Anm: wie Obi, Baumax, Bauhaus etc) und solchen in „Misch- oder Kombi-Märkten“ (Anm: wie Quester, Öbau, Raiffeisen-Lagerhaus etc) differenziert worden.

**False Positives:**

- `Obi` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Tax Office Acronym FAÖ (Full)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8595a2db`  
**Description:**
Matches Finanzamt Österreich full name.

**Content:**
```
(?i)\b(Finanzamt\s+Österreich)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Tax Office Acronym FAÖ (Genitive)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `fcd679e0`  
**Description:**
Matches Finanzamtes Österreich.

**Content:**
```
(?i)\b(Finanzamtes\s+Österreich)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Tax Office Acronym FAG (Full)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `f0860c4c`  
**Description:**
Matches Finanzamt für Großbetriebe.

**Content:**
```
(?i)\b(Finanzamt\s+für\s+Großbetriebe)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Tax Office Acronym FAG (Genitive)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `3aa20cce`  
**Description:**
Matches Finanzamtes für Großbetriebe.

**Content:**
```
(?i)\b(Finanzamtes\s+für\s+Großbetriebe)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Erste Bank`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `1180e532`  
**Description:**
Matches Erste Bank specifically.

**Content:**
```
(?i)\b(Erste\s+Bank)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `German Federal Tax Court Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `5d3bd748`  
**Description:**
Matches BFH (Bundesfinanzhof) acronym.

**Content:**
```
(?i)\b(BFH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Merkur Treuhand Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6173a21e`  
**Description:**
Matches Merkur Treuhand Steuerberatung GmbH with flexible spacing.

**Content:**
```
(?i)\b(Merkur\s+Treuhand\s+Steuerberatung\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Tax Authority Austria with Code`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `6cc17f97`  
**Description:**
Matches Finanzamt Österreich including optional parenthetical codes like (DST12).

**Content:**
```
(?i)\b(Finanzamt\s+Österreich(?:\s*\([^)]+\))?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WKO Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8b5f45a9`  
**Description:**
Matches WKO (Wirtschaftskammer Österreich) as a standalone entity.

**Content:**
```
(?i)\bWKO\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `UFS with Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `10463d1e`  
**Description:**
Matches UFS followed by a location (e.g., Salzburg), ensuring the full entity is captured but stopping before 'vom'.

**Content:**
```
(?i)\bUFS\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\b(?![\s]*vom)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Tax Office Full Name with Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `769b30f5`  
**Description:**
Matches Finanzamt followed by city names, strictly excluding non-entity contexts like 'Finanzamt am' or 'Finanzamt erliegende'.

**Content:**
```
(?i)\bFinanzamt\s+(?:Österreich|Feldkirch|Bregenz|Innsbruck|Hollabrunn|Korneuburg|Tulln|Braunau|Ried|Schärding|Landeck|Reutte|Wien|Salzburg|Graz|Linz|Villach|Dornbirn|Bregenz|Eisenstadt|St.\s+Pölten|Klagenfurt|Innsbruck|Bregenz|Feldkirch|Hollabrunn|Korneuburg|Tulln|Braunau|Ried|Schärding|Landeck|Reutte|Wien|Salzburg|Graz|Linz|Villach|Dornbirn|Eisenstadt|St.\s+Pölten|Klagenfurt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Amtes für Betrugsbekämpfung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `9234f01c`  
**Description:**
Matches the specific organization 'Amt für Betrugsbekämpfung' or its genitive form.

**Content:**
```
(?i)\b(Amt(?:es)?\s+für\s+Betrugsbekämpfung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific GmbH Names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `ae7c1699`  
**Description:**
Matches specific GmbH names that were missed, including 'Schabetsberger Steuerberatung GmbH', 'Yoga Vidya GmbH', 'Hausverwaltung-GmbH', 'Berwaldkel-Möbel AG', 'Garanta VersicherungsAG', 'DA Deutsche Allgemeine Versicherung AG', 'AVED cosmetic', 'Geschenkartikel GmbH', 'B-GmbH', 'A-GmbH', 'X GmbH', 'UnterRecycling Services GMBH', 'Rhein Normonkel Manufaktur GMBH', 'Klein-Vorholt KI GMBH', 'Gogel Daten GMBH', 'London Film Acadamy'.

**Content:**
```
(?i)\b(Schabetsberger\s+Steuerberatung\s+GmbH|Yoga\s+Vidya\s+GmbH|Hausverwaltung-GmbH|Berwaldkel-Möbel\s+AG|Garanta\s+VersicherungsAG|DA\s+Deutsche\s+Allgemeine\s+Versicherung\s+AG|AVED\s+cosmetic|Geschenkartikel\s+GmbH|B-GmbH|A-GmbH|X\s+GmbH|UnterRecycling\s+Services\s+GMBH|Rhein\s+Normonkel\s+Manufaktur\s+GMBH|Klein-Vorholt\s+KI\s+GMBH|Gogel\s+Daten\s+GMBH|London\s+Film\s+Acadamy)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Magistrate Genitive`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `cf84cf2e`  
**Description:**
Matches Magistrates der Stadt Wien (genitive) and variations.

**Content:**
```
(?i)\b(Magistrates\s+der\s+Stadt\s+Wien(?:,\s+Magistratsabteilung\s+\d+)?)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Limited Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `7156c23b`  
**Description:**
Matches entities ending in Limited.

**Content:**
```
(?i)(?<![a-zäöüß\s])([A-Z][a-zäöüß0-9]*(?:\s+[A-Z][a-zäöüß0-9]*)*(?:\s+&\s+[A-Z][a-zäöüß0-9]*)*\s+Limited)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 336 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/8Ob4_18y`) (sent_id: `deanon_TRAIN/8Ob4_18y_4`)


Vossbrinck Wind AG, Flurnsbach 9, 4722 Untwüsten, Österreich, vertreten durch Kunz Schima Wallentin Rechtsanwälte GmbH in Wien, und 2. Steinheim-Cloud Limited, Anlauftalstraße 23, 4623 Kalchau, Österreich, vertreten durch CMS Reich-Rohrwig Hainz Rechtsanwälte GmbH in Wien, wegen 9.141,02 EUR, über die Revision der erstbeklagten Partei gegen das Teilurteil des Handelsgerichts Wien als Berufungsgericht vom 18. September 2017, GZ 60 R 20/17x-29, womit das Urteil des Bezirksgerichts für Handelssachen Wien vom 3. Jänner 2017, GZ 20 C 529/15p-24, in der Hauptsache hinsichtlich der erstbeklagten Partei bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Cloud Limited` — partial — pred is substring of gold: `Steinheim-Cloud Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Vossbrinck Wind AG`(organisation)
- `Flurnsbach 9, 4722 Untwüsten, Österreich`(address)
- `Steinheim-Cloud Limited`(organisation)
- `Anlauftalstraße 23, 4623 Kalchau, Österreich`(address)

**Example 1** (doc_id: `deanon_TRAIN/7Nc14_18w`) (sent_id: `deanon_TRAIN/7Nc14_18w_4`)


Matzka als weitere Richter in der beim Landesgericht Klagenfurt zu AZ 29 Cg 32/18a anhängigen Rechtssache der klagenden Partei Mag. Philipp Hinterscheid, vertreten durch Mag. Patrick Mandl, Rechtsanwalt in Wien, gegen die beklagte Partei Nexlogal-Wind Limited, Kindlerweg 65, 8786 Boder, Österreich, Vereinigtes Königreich, vertreten durch die Schönherr Rechtsanwälte GmbH in Wien, wegen Vertragsaufhebung und 43.876,22 EUR sA, über den Delegierungsantrag der klagenden Partei gemäß § 31 Abs 2 JN den Beschluss gefasst:  Spruch Der Antrag der klagenden Partei, anstelle des Landesgerichts Klagenfurt das Handelsgericht Wien zur Verhandlung und Entscheidung in der Rechtssache zu bestimmen, wird abgewiesen.

**False Positives:**

- `Wind Limited` — partial — pred is substring of gold: `Nexlogal-Wind Limited`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Mag. Philipp Hinterscheid`(person)
- `Nexlogal-Wind Limited`(organisation)
- `Kindlerweg 65, 8786 Boder, Österreich`(address)

</details>

---

## `Law Firm KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Rule ID:** `8e2afccb`  
**Description:**
Matches law firms ending in KG, excluding GmbH & Co KG patterns.

**Content:**
```
(?i)(?<![a-zäöüß\s])(?<!\w)([A-Z][a-zäöüß]+(?:\s+[A-Z][a-zäöüß]+)*(?:\s+&\s+[A-Z][a-zäöüß]+)*\s+KG)(?=\s|,|\.|\(|\)|;|:|\n|$)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 10 | 0 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 10 | 377 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `deanon_TRAIN/3Ob112_11h`) (sent_id: `deanon_TRAIN/3Ob112_11h_7`)


TraunChemie GmbH & Co KG, Badeteich Bisamberg 16, 4625 Kronberg, Österreich, vertreten durch Siemer-Siegl-Füreder & Partner, Rechtsanwälte OG in Wien, wegen 59.104,03 EUR sA, über die außerordentlichen Revisionsrekurse der beklagten Parteien gegen den Beschluss des Oberlandesgerichts Linz als Rekursgericht vom 2. Mai 2011, GZ 2 R 182/10p-50, womit über Rekurs der klagenden Partei der Beschluss des Landesgerichts Steyr vom 23. August 2010, GZ 4 Cg 154/08t-34, abgeändert wurde, den Beschluss gefasst:  Spruch Die außerordentlichen Revisionsrekurse werden gemäß § 526 Abs 2 Satz 1 ZPO mangels der Voraussetzungen des § 528 Abs 1 ZPO zurückgewiesen.

**False Positives:**

- `TraunChemie GmbH & Co KG` — partial — gold is substring of pred: `TraunChemie GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `TraunChemie GmbH`(organisation)
- `Badeteich Bisamberg 16, 4625 Kronberg, Österreich`(address)

**Example 1** (doc_id: `deanon_TRAIN/7Ob65_15g`) (sent_id: `deanon_TRAIN/7Ob65_15g_3`)


Kopf Der Oberste Gerichtshof hat als Revisionsgericht durch die Hofrätin Dr. Kalivoda als Vorsitzende und durch die Hofräte Dr. Höllwerth, Mag. Dr. Wurdinger, Mag. Malesich und Dr. Singer als weitere Richter in der Rechtssache der klagenden Partei Nortri-Umwelt GmbH & Co KG, Piberberg 8, 4720 Unternfurth, Österreich, vertreten durch Dr. Klaus Plätzer, Rechtsanwalt in Salzburg, gegen die beklagte Partei Anton Adil Versicherungs-Aktiengesellschaft, Am Kastanienhof 90, 6162 Mutters, Österreich, vertreten durch Dr. Johannes Kirschner, Rechtsanwalt in Wels, wegen Feststellung, über die Revision der klagenden Partei gegen das Urteil des Oberlandesgerichts Linz als Berufungsgericht vom 19. Jänner 2015, GZ 1 R 198/14i-14, womit das Urteil des Landesgerichts Wels vom 29. September 2014, GZ 2 Cg 65/14g-10, bestätigt wurde, den Beschluss gefasst:  Spruch Die Revision wird zurückgewiesen.

**False Positives:**

- `Umwelt GmbH & Co KG` — positional overlap with gold: `Nortri-Umwelt GmbH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Nortri-Umwelt GmbH`(organisation)
- `Piberberg 8, 4720 Unternfurth, Österreich`(address)
- `Anton Adil`(person)
- `Am Kastanienhof 90, 6162 Mutters, Österreich`(address)

**Example 2** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_6`)


Die KG wurde aufgelöst und der Geschäftsbetrieb eingestellt.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_9`)


Die Beklagte informierte die Kunden der KG, dass sie alle Geschäfte der KG mit allen Rechten und Pflichten übernehme.

**False Positives:**

- `Die Beklagte informierte die Kunden der KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_11`)


Die KG habe nämlich dahingehend beraten, dass der Schweinestall der Klägerin aufgrund von Mängeln komplett zu sanieren sei.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `deanon_TRAIN/4Ob126_18k`) (sent_id: `deanon_TRAIN/4Ob126_18k_24`)


Die KG sei im Zusammenhang mit der Pensionierung ihres Komplementärs aufgelöst worden, eine Willenseinigung zwischen der KG und der beklagten GmbH über die Übernahme von Vermögenswerten sei den erstgerichtlichen Feststellungen nicht zu entnehmen.

**False Positives:**

- `Die KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `deanon_TRAIN/11Os113_12w`) (sent_id: `deanon_TRAIN/11Os113_12w_6`)


Text Gründe: Mit dem angefochtenen Urteil wurden Bernhard Beinicke und Norbert Wentzlick von der wider sie erhobenen Anklage, sie hätten am 7. Februar 2009 in Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich /Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG, Susanne Schueßler, durch die Vorgabe, die HochForschung GmbH sei eine zahlungsfähige Leasingnehmerin, somit durch Täuschung über Tatsachen, zum Abschluss eines Leasingvertrags über ein Rennfahrzeug für die Dauer von 24 Monaten zu einem monatlichen Entgelt von 10.698,10 Euro, somit zu einer Handlung verleitet, welche die Stadt-Sanitär Services GesmbH & Co KG in einem 50.000 Euro übersteigenden Betrag von insgesamt 235.358,20 Euro am Vermögen schädigte, gemäß § 259 Z 3 StPO (verfehlt auch von der rechtlichen Kategorie; vglLendl, WK-StPO § 259 Rz 1) freigesprochen.

**False Positives:**

- `Deutschland in einverständlichem Zusammenwirken mit auf unrechtmäßige Bereicherung gerichtetem Vorsatz die Geschäftsführerin der DKZ Solar GesmbH & Co KG` — partial — gold is substring of pred: `DKZ Solar GesmbH`
- `Sanitär Services GesmbH & Co KG` — positional overlap with gold: `Stadt-Sanitär Services GesmbH`

> overlaps gold: 2  |  likely missing annotation: 0

**Gold Entities:**

- `Beinicke`(person)
- `Wentzlick`(person)
- `Churer Straße 54, 9064 St. Michael ob der Gurk, Österreich`(address)
- `DKZ Solar GesmbH`(organisation)
- `Schueßler`(person)
- `HochForschung GmbH`(organisation)
- `Stadt-Sanitär Services GesmbH`(organisation)

**Example 7** (doc_id: `deanon_TRAIN/2Ob116_20b`) (sent_id: `deanon_TRAIN/2Ob116_20b_3`)


Kopf Der Oberste Gerichtshof hat als Rekursgericht durch den Senatspräsidenten Dr. Veith als Vorsitzenden und den Hofrat Dr. Musger, die Hofrätin Dr. Solé und die Hofräte Dr. Nowotny und Mag. Pertmayr als weitere Richter in der Rechtssache der klagenden Partei Natalie Pirkmayr, vertreten durch Widter Mayrhauser Wolf Rechtsanwälte OG in Wien, gegen die beklagte Partei Maja Stollhans, vertreten durch Rudeck-Schlager Rechtsanwalts KG in Wien, und die Nebenintervenientinnen auf Seiten der beklagten Partei 1.

**False Positives:**

- `Schlager Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Natalie Pirkmayr`(person)
- `Maja Stollhans`(person)

**Example 8** (doc_id: `deanon_TRAIN/2Ob116_20b`) (sent_id: `deanon_TRAIN/2Ob116_20b_4`)


Bruckgart-Daten GmbH, Paulina Kleisz, vertreten durch Rudeck-Schlager Rechtsanwalts KG in Wien, 2.

**False Positives:**

- `Schlager Rechtsanwalts KG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bruckgart-Daten GmbH`(organisation)
- `Paulina Kleisz`(person)

</details>

---

</details>

---

