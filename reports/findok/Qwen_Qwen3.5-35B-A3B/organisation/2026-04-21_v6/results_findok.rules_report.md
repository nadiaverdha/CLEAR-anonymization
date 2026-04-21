# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-21T21:42:00.587856

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-21_v6/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 2327 |
| Validation documents | 218 |
| Test documents | 108 |
| Train sentences | 2327 |
| Validation sentences | 218 |
| Test sentences | 12077 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 30 |
| Max samples in prompt | 50 |
| Refinement iterations | 10 |
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
| Batch size | 40 |
| Refine per batch | 1 |
| Manually annotated examples | 1304 |
| First batch with manual data | 25 |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 86.3% |
| True Positives | 1014 |
| False Positives | 1431 |
| Micro Precision | 41.5% |
| Micro Recall | 58.2% |
| Micro F1 | 48.4% |
| Macro F1 | 48.4% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Landespolizeidirektion` | 0.9% | 100.0% | 0.5% | 8 | 8 | 0 |
| `Tax Authority Abbreviations FAG FAÖ` | 7.1% | 100.0% | 3.7% | 64 | 64 | 0 |
| `Anwälte Mandl & Mitterbauer GmbH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `School for Health Care Grillenreith Specific` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `Bankhaus Entity` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `EASO` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `BMI` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `BM für Inneres` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Bundesministerium für Inneres` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Kriminalpolizei in Österreich` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Flughafen München` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `Arbeits- und Sozialgericht` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Bundesministers für Finanzen` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Höhere Lehranstalt` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Höheren Lehranstalt Genitive` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `King's School` | 0.6% | 100.0% | 0.3% | 5 | 5 | 0 |
| `University of Bristol` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `England Organisation` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Company with GmbH & Partner KG` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Merkur Treuhand Steuerberatung GmbH` | 1.1% | 100.0% | 0.6% | 10 | 10 | 0 |
| `Schabetsberger Steuerberatung GmbH` | 0.7% | 100.0% | 0.3% | 6 | 6 | 0 |
| `Verwaltungsgericht Wien` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Wiederspan Beratung GMBH` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Mur Alver OG` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Generic Company Names` | 1.4% | 100.0% | 0.7% | 12 | 12 | 0 |
| `Bezirkshauptmannschaft with Location` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `ÖBB Abbreviation` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Krankenpflegevereins Bludenz` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Finanzamt Neunkirchen Wr. Neustadt Specific` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Raiffeisenbank Karnische Rion Bankstelle St.Stefan` | 0.6% | 100.0% | 0.3% | 5 | 5 | 0 |
| `Mag. Ghesla Steuerberater GmbH` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `ÖGK Abbreviation` | 4.5% | 100.0% | 2.3% | 40 | 40 | 0 |
| `Bundesministerin für Finanzen` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Mag. [Name] Steuerberater GmbH` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Roelfsen Versicherung` | 3.6% | 100.0% | 1.8% | 32 | 32 | 0 |
| `Lubomir Merschmeyer` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `Houdek Maschinenbau` | 6.2% | 100.0% | 3.2% | 56 | 56 | 0 |
| `Schmeltz Luftfahrt` | 1.3% | 100.0% | 0.6% | 11 | 11 | 0 |
| `Lexdon IT` | 0.8% | 100.0% | 0.4% | 7 | 7 | 0 |
| `Dorfcon-Verlag` | 1.0% | 100.0% | 0.5% | 9 | 9 | 0 |
| `FA Wien 1/23 Specific` | 2.3% | 100.0% | 1.1% | 20 | 20 | 0 |
| `Finanzamt Wien 1/23 Specific` | 2.2% | 100.0% | 1.1% | 19 | 19 | 0 |
| `Finanzamt Wien 1/23 Genitive` | 0.5% | 100.0% | 0.2% | 4 | 4 | 0 |
| `Tritri-IT` | 0.1% | 100.0% | 0.1% | 1 | 1 | 0 |
| `Gözcü Getränke` | 0.3% | 100.0% | 0.2% | 3 | 3 | 0 |
| `KQPC Versand GMBH Specific` | 2.3% | 100.0% | 1.1% | 20 | 20 | 0 |
| `Event Sudkraftlex GMBH Specific` | 2.3% | 100.0% | 1.1% | 20 | 20 | 0 |
| `Sudver Handel Services GMBH Specific` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Glanznorost Institut GMBH Specific` | 0.2% | 100.0% | 0.1% | 2 | 2 | 0 |
| `Magistrat der Stadt Wien with Suffixes` | 4.5% | 95.2% | 2.3% | 42 | 40 | 2 |
| `Finanzamt Österreich Specific` | 11.6% | 94.7% | 6.2% | 114 | 108 | 6 |
| `Bundesamt für Soziales und Behindertenwesen` | 1.5% | 92.9% | 0.7% | 14 | 13 | 1 |
| `SeneCura Variations` | 1.1% | 90.9% | 0.6% | 11 | 10 | 1 |
| `University Full Names JKU WU` | 4.7% | 84.0% | 2.4% | 50 | 42 | 8 |
| `Finanzamt Wien with Variable Districts` | 0.5% | 80.0% | 0.2% | 5 | 4 | 1 |
| `SUVA Abbreviation` | 5.3% | 75.0% | 2.8% | 64 | 48 | 16 |
| `PVA Abbreviation` | 0.6% | 71.4% | 0.3% | 7 | 5 | 2 |
| `Company with OG Suffix` | 0.3% | 60.0% | 0.2% | 5 | 3 | 2 |
| `Company with GmbH & Co KG` | 0.1% | 50.0% | 0.1% | 2 | 1 | 1 |
| `UFS Abbreviation` | 0.1% | 50.0% | 0.1% | 2 | 1 | 1 |
| `Bundesfinanzgerichtes Genitive` | 7.2% | 43.9% | 3.9% | 155 | 68 | 87 |
| `Verwaltungsgerichtshof Genitive` | 13.4% | 42.8% | 8.0% | 325 | 139 | 186 |
| `Frontex` | 0.9% | 42.1% | 0.5% | 19 | 8 | 11 |
| `Bundesfinanzgerichts Genitive` | 1.5% | 41.9% | 0.7% | 31 | 13 | 18 |
| `BFH Abbreviation` | 0.1% | 33.3% | 0.1% | 3 | 1 | 2 |
| `Verfassungsgerichtshof` | 0.7% | 27.3% | 0.3% | 22 | 6 | 16 |
| `University Abbreviations JKU WU` | 1.0% | 22.5% | 0.5% | 40 | 9 | 31 |
| `OECD` | 0.1% | 20.0% | 0.1% | 5 | 1 | 4 |
| `Verwaltungsgerichtshof and VwGH` | 14.3% | 16.8% | 12.4% | 1285 | 216 | 1069 |
| `Pensionsversicherungsanstalt` | 0.2% | 15.4% | 0.1% | 13 | 2 | 11 |
| `Company with AG Suffix` | 0.1% | 14.3% | 0.1% | 7 | 1 | 6 |
| `University Full Names Generalized` | 0.4% | 11.1% | 0.2% | 36 | 4 | 32 |
| `Merkur Treuhand Steuerberatung (Short)` | 0.1% | 9.1% | 0.1% | 11 | 1 | 10 |
| `Amt für Betrugsbekämpfung` | 0.1% | 6.7% | 0.1% | 15 | 1 | 14 |
| `VfGH Abbreviation` | 0.2% | 5.0% | 0.1% | 40 | 2 | 38 |
| `Fachhochschule and FH` | 0.0% | 0.0% | 0.0% | 14 | 0 | 14 |
| `Bundeskanzleramt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `LG für ZRS Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministeriums für Justiz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgericht with LG Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Karl-Franzens- Universität Graz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Europäische Grenzschutzagentur Frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `HLF Abbreviation` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `ÖBUG GmbH Full Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schabetsberger Steuerberatung (Short)` | 0.0% | 0.0% | 0.0% | 6 | 0 | 6 |
| `Bezirksgericht with Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenbank Stallhofen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mittel Unisyn GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bärs & Walterscheidt Handel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ober Lemostnor AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Vennes Recycling AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Österreichische Gesellschaft für Europapolitik` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Unter Donunisee AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schweizerischen Unfallversicherungsanstalt (SUVA)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFG with Außenstelle Linz (Parentheses)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFG with Außenstelle Linz (Comma)` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Bundesfinanzgerichts with Außenstelle Linz` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `SVS/SVB Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PSD Wien Ambulatorium Landstraße` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sozialversicherungsanstalt der Bauern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sozialversicherung der Bauern` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Bundesministers für Arbeit Soziales und Konsumentenschutz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `London Film Academy` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Trafenfen Automotive Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Steiermark Mitte Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mur Ververzor Betriebe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Naaß Elektro GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bersud Möbel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Unter Heimdorf GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Bruck Eisenstadt Oberwart` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Klagenfurt St. Veit Wolfsberg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Vorarlberg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Tax Authority Abbreviations FAG FAÖ`

**F1:** 0.071 | **Precision:** 1.000 | **Recall:** 0.037  

**Format:** `regex`  
**Description:**
Matches the specific tax authority abbreviations 'FAG' (Finanzamt für Großbetriebe) and 'FAÖ' (Finanzamt Österreich) as standalone entities.

**Content:**
```
\b(?:FAG|FA\u00d6)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.037 | 0.071 | 64 | 64 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 64 | 0 | 1491 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.


Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAG` | `FAG` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_5`)


Das FAG erließ am 21.8.2024 einen Bescheid über die Aufhebung des Umsatzsteuerbescheides  2022 vom 8.9.2023 und verband diese mit dem ebenfalls vom selben Tag datierenden  Sachbescheid.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_7`)


Am 5.11.2024 hob das FAG den Umsatzsteuerbescheid 2022 vom 21.8.2024  erneut nach § 299 BAO auf und erließ einen neuen Jahresbescheid.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

</details>

---

## `Houdek Maschinenbau`

**F1:** 0.062 | **Precision:** 1.000 | **Recall:** 0.032  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Houdek Maschinenbau'.

**Content:**
```
\bHoudek\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.032 | 0.062 | 56 | 56 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 56 | 0 | 1481 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_17`)


Der Sachverhalt ergibt sich bisherigen Verfahren wie folgt:   a) Sachverhalt und Verfahrensablauf bei der Houdek Maschinenbau, Str.Nr.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_18`)


95-002/7970, BV 24:  Das Unternehmen Houdek Maschinenbau  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_20`)


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_22`)


Zum Stichtag 31.12.2008 ist die Houdek Maschinenbau  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan vom 29.06.2009 gemäß § 39 UmgrStG in einem ersten  Umgründungsschritt als übertragende Gesellschaft (neben anderen Gesellschaften) mit der  Lexdon IT  als übernehmende Gesellschaft verschmolzen worden.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_25`)


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

---

## `ÖGK Abbreviation`

**F1:** 0.045 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.045 | 40 | 40 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 0 | 1700 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_28`)


Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_74`)


Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_214`)


Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `Roelfsen Versicherung`

**F1:** 0.036 | **Precision:** 1.000 | **Recall:** 0.018  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Roelfsen Versicherung'.

**Content:**
```
\bRoelfsen\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.018 | 0.036 | 32 | 32 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 32 | 0 | 1515 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_7`)


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_10`)


Mit Bescheid vom 29. Jänner 2019 wurde ein Bescheid über die Wiederaufnahme des  Verfahrens betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (Roelfsen Versicherung  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_11`)


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_24`)


zweiten Umgründungsschritt ist auf Grundlage des Generalversammlungsbeschlusses vom  19.08.2009 eine Abspaltung zur Aufnahme in die Roelfsen Versicherung  durch Übertragung des  gesamten Betriebes (mit Ausnahme der unter Punkt Drittens 10.4 des Spaltungs- und  Übernahmsvertrages taxativ angeführten Positionen) erfolgt.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

</details>

---

## `FA Wien 1/23 Specific`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'FA Wien 1/23' specifically to ensure it is captured correctly.

**Content:**
```
\bFA\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1500 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_27`)


Im Wirtschaftsjahr 2007 ist gemäß der beim FA Wien 1/23  eingereichten  Körperschaftsteuererklärung 2007 ein steuerlicher Verlust von € -4.239.321,85 aus den 84  Tankstellen erzielt worden.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)


Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_75`)


Das BFG hat der Beschwerde stattgegeben (Entscheidung vom 27.01.2016, GZ  RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des FA Wien 1/23  gegenüber der  mitbeteiligten Partei Roelfsen Versicherung (als partiellen Gesamtrechtsnachfolger der Houdek Maschinenbau)  abgeändert.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_100`)


Das Erkenntnis des Bundesfinanzgerichts, Außenstelle Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des FA Wien 1/23  in vollem Umfang im Zuge einer Amtsrevision  angefochten.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

</details>

---

## `KQPC Versand GMBH Specific`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches the specific company 'KQPC Versand GMBH'.

**Content:**
```
\bKQPC\s+Versand\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1583 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_10`)


Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_11`)


In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

</details>

---

## `Event Sudkraftlex GMBH Specific`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches the specific company 'Event Sudkraftlex GMBH'.

**Content:**
```
\bEvent\s+Sudkraftlex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1579 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_20`)


Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

## `Finanzamt Wien 1/23 Specific`

**F1:** 0.022 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Wien 1/23' specifically to ensure it is captured correctly.

**Content:**
```
\bFinanzamt\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.022 | 19 | 19 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 0 | 1524 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_3`)


über die Beschwerden vom 29. März 2019 gegen den Bescheid des Finanzamt Wien 1/23  vom 29. Jänner  2019 betreffend Wiederaufnahme § 303 BAO /  KSt 2010 Steuernummer 85-900/3590  zu  Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_102`)


Unmittelbar nachfolgend hat das BFG die Amtsrevision des Finanzamt Wien 1/23 (samt Veranlagungsakten  sowie Auszügen aus dem Arbeitsbogen der Betriebsprüfung) dem VwGH unter der Zahl Ro  2016/15/0010 zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_111`)


Mittels VwGH-Entscheidung vom 13.09.2018 zu Ro 2016/15/0010 hat der VwGH die  Amtsrevision des Finanzamt Wien 1/23  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_135`)


Begründend  wurde deshalb durch das Finanzamt Wien 1/23  im Sachbescheid Feststellungsbescheid Gruppenmitglied  2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ  RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Roelfsen Versicherung  als RNF der  Houdek Maschinenbau  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR  1.047.673,40 ergibt.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_137`)


Die BFG- Entscheidung RV/5101064/2013 vom 27.01.2016 für das Jahr 2007 (Rechtsvorgänger) wurde  seitens des Finanzamt Wien 1/23  mittels Amtsrevision bekämpft.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

</details>

---

## `Generic Company Names`

**F1:** 0.014 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches common capitalized company names that appear in lists (e.g., Ikea, Obi, Leiner) when followed by a comma or end of sentence, or in a list context.

**Content:**
```
\b(?:Ikea|Obi|Leiner|M\u00f6belix|M\u00f6maX|Otto\.de|xxxLutz|Quelle\.at|SENECURA|Be\.|A-GmbH|B-GmbH|Hausverwaltung-GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.007 | 0.014 | 12 | 12 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 0 | 1558 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.

| Predicted | Gold |
|---|---|
| `Ikea` | `Ikea` |
| `Obi` | `Obi` |
| `Leiner` | `Leiner` |
| `Möbelix` | `Möbelix` |
| `MömaX` | `MömaX` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_11`)


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |
| `SENECURA` | `SENECURA` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_12`)


Für 2017: Mobiler Hilfsdienst SENECURA 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 sowie eigene Arztkosten der Bf 633,76 Euro.

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_36`)


Darin wurden weitere Nachweise und Unterlagen zu den Krankheitskosten für  die Mutter der Bf angefordert (Vereinbarung über die Kostentragung mit dem Pflegeheim,  Rechtsgrundlage für die Übernahme der Zahlungen für diverse Lebenshaltungskosten,  Nachweise über tatsächliche Verausgabungen und Kosten der Mutter, Aufgabe des Mobilen  Hilfsdienst SENECURA, Nachweis der Aktiva des Nachlasses der verstorbenen Mutter, etc).

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

</details>

---

## `Schmeltz Luftfahrt`

**F1:** 0.013 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Schmeltz Luftfahrt'.

**Content:**
```
\bSchmeltz\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.013 | 11 | 11 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 0 | 1524 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_20`)


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_21`)


Die Schmeltz Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_26`)


Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_49`)


Teilbetriebe  Schmeltz Luftfahrt:   Verluste  geschlossene  Teilbetriebe  Houdek Maschinenbau:   -326.546,95 6,78 %

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_54`)


Abgespaltene  Tankstellen  Schmeltz Luftfahrt **   Geschlossene  Tankstellen  Houdek Maschinenbau **  Verkaufte  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `Verwaltungsgerichtshof and VwGH`

**F1:** 0.143 | **Precision:** 0.168 | **Recall:** 0.124  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof', 'Verwaltungsgerichtshofes', and 'VwGH', but excludes 'VwGH' when followed by a hyphen (e.g., VwGH-Entscheidung).

**Content:**
```
\bVerwaltungsgerichtshof(?:es)?\b|(?<!\w)VwGH\b(?![\s]*-)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.168 | 0.124 | 0.143 | 1285 | 216 | 1069 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 216 | 1069 | 1525 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_2`)

**False Positives:**


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_143`)

**False Positives:**


Die Nachsicht dient  nicht dazu, im Festsetzungsverfahren unterlassene Einwendungen (vor allem  Bescheidbeschwerden) nachzuholen (VwGH 17.10.2001, 98/13/0073;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_182`)

**False Positives:**


VwGH 27.3.1996, 92/13/0291;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_189`)

**False Positives:**


VwGH 20.6.1990, 89/13/0249;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_192`)

**False Positives:**


Unter dem Gesichtspunkt  der Zweckmäßigkeit (iSd § 20) ist auch die Gleichbehandlung von Abgabepflichtigen, somit  keine Benachteiligung ehrlicher Steuerschuldner durch Bevorzugung unehrlicher, zu  berücksichtigen (VwGH 4.4.1989, 88/14/0245;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

</details>

---

## `Verwaltungsgerichtshof Genitive`

**F1:** 0.134 | **Precision:** 0.428 | **Recall:** 0.080  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs' (genitive forms).

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.428 | 0.080 | 0.134 | 325 | 139 | 186 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 139 | 186 | 1584 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_146`)


Entgegen der Rechtsansicht des Bf, dass der erste tatsächliche Studienwechsel zum Studium  der biotechnischen Verfahren erfolgt ist, gilt auch der Rückwechsel vom Bachelorstudium  Wirtschaftsrecht auf das Studium Rechtswissenschaften nach der zitierten Judikatur des  Verwaltungsgerichtshofes (VwGH 01.02.1990, 89/12/0175) als Studienwechsel.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)

**False Positives:**


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)

**False Positives:**


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)

**False Positives:**


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_71`)

**False Positives:**


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

</details>

---

## `Bundesfinanzgerichtes Genitive`

**F1:** 0.072 | **Precision:** 0.439 | **Recall:** 0.039  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgerichtes' (genitive) specifically.

**Content:**
```
\bBundesfinanzgerichtes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.439 | 0.039 | 0.072 | 155 | 68 | 87 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 68 | 87 | 1655 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_175`)


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_124`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_69`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) ( sent_id: `findok-manually-annotated_TRAIN/149497.1_28`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_69`)

**False Positives:**


III. Zulässigkeit einer Revision  Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des Bundesfinanzgerichtes die Revision an  den Verwaltungsgerichtshof zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der  4 von 5 Seite 5 von 5

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_111`)

**False Positives:**


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_103`)

**False Positives:**


Laut Amtsrevision wurde die Rechtsansicht des Bundesfinanzgerichtes, das freie Wahlrecht des  innerbetrieblichen Verlustausgleiches bei einer § 7 (3)-KStG-Körperschaft zuzulassen und  daraus folgend eine willkürliche Verlustverrechnung zuzulassen, vom revisionswerbenden  Finanzamt nicht geteilt.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_152`)

**False Positives:**


Im Zuge der VwGH- Entscheidung vom 13.09.2018 zu Ro  2016/15/0010 wurde durch den VwGH als Vorfrage für die Höhe des Verlustvortrages für die  Folgejahre nach 2007 ausgeführt, dass entgegen der Rechtsmeinung des BFG kein freies  Wahlrecht in Bezug auf den innerbetrieblichen Verlustausgleich im Jahr 2007 vor der  Abspaltung existiert und daraus folgend ein Verlustvortrag nur nach der Spezialregelung des §  35 UmgrStG iVm § 21 UmgrStG zu gewähren ist (objektbezogener Verlustvortrag) und somit  der Verlustvortrag nicht in der im Erkenntnis des Bundesfinanzgerichtes dargestellten Höhe  zusteht (vgl. Seite 7 und 8 der VwGH-Entscheidung).

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

</details>

---

## `VfGH Abbreviation`

**F1:** 0.002 | **Precision:** 0.050 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'VfGH' (Verfassungsgerichtshof) as an organization.

**Content:**
```
\bVfGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.050 | 0.001 | 0.002 | 40 | 2 | 38 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 38 | 1438 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_46`)


Nach Ansicht des VfGH (zB 29.6.1985, G 42/85 ua;

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated_TRAIN/149418.1_32`)


Das Bundesfinanzgericht sieht sich nicht veranlasst, die von der Bf in der vorliegenden  Beschwerde geäußerten verfassungsrechtlichen Bedenken an den VfGH zu tragen.

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**


Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_157`)

**False Positives:**


Der VfGH hat in seinem Erkenntnis eine  14 von 39 Seite 15 von 39

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_159`)

**False Positives:**


Dem genannten VfGH-Erkenntnis lag folgender Sachverhalt zu Grunde: Mit  Berufungsentscheidung aus dem Jahr 1984 gab die zuständige FLD der Berufung einer  Gesellschafterin gegen die einheitliche und gesonderte Gewinnfeststellung in der Form statt,  dass die im Erstbescheid bei der Gesellschafterin zur Gänze als Gewinnanteil behandelte  Ablösezahlung mit 2/3 zu aktivieren und auf 6 Jahre verteilt abzuschreiben war.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_162`)

**False Positives:**


Der VfGH bejahte die Anwendbarkeit des Vorfragentatbestandes.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**


Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

</details>

---

## `University Full Names Generalized`

**F1:** 0.004 | **Precision:** 0.111 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Universität' or 'Hochschule' followed by a location, stopping strictly before verbs, prepositions, or the word 'Name'.

**Content:**
```
\b(?:Universität|Hochschule)\s+[A-Z][a-zA-Z\s\u00e4\u00f6\u00fc\u00df]+?(?=\s*(?:vom|am|von|ist|hat|wurde|sind|waren|und|sowie|als|an|mit|der|die|das|ein|eine|einem|einer|den|die|dem|des|zur|im|um|zu|bei|nach|\u00fcber|unter|ohne|neben|zwischen|gegen|durch|seit|bis|vor|hinter|\(|,|\.|$|Name))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.111 | 0.002 | 0.004 | 36 | 4 | 32 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 32 | 1672 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_4`)

**False Positives:**


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

FP: `Universität Wien inskribiert` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_46`)

**False Positives:**


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

FP: `Universität Wien betrieben` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_10`)

**False Positives:**


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

FP: `Universität Wien ab` (organisation)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

FP: `Hochschule Wien` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)
- `Pädagogischen Hochschule Wien` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_27`)

**False Positives:**


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

FP: `Universität Wien sei folgende Formulierung` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_54`)

**False Positives:**


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

FP: `Universität Wien in` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Universität Wien` (organisation)

</details>

---

## `University Abbreviations JKU WU`

**F1:** 0.010 | **Precision:** 0.225 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches the specific university abbreviations JKU and WU as standalone entities.

**Content:**
```
\b(?:JKU|WU)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.225 | 0.005 | 0.010 | 40 | 9 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 31 | 632 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_41`)


Siehe Internetseite JKU und WU  Karriereaussichten!


Siehe Internetseite JKU und WU  Karriereaussichten!

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |
| `WU` | `WU` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

| Predicted | Gold |
|---|---|
| `WU` | `WU` |
| `JKU` | `JKU` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

| Predicted | Gold |
|---|---|
| `WU` | `WU` |
| `JKU` | `JKU` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)

**False Positives:**


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_11`)

**False Positives:**


 Abgangsbescheinigung der WU Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- und Sozialwissenschaften, aus welcher unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten sowie der Abschluss der Studieneingangs- und  Orientierungsphase mit 07.03.2018 hervorgeht:    [...]

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)

**False Positives:**


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `JKU` (organisation)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `JKU` (organisation)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `WU` (organisation)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_14`)

**False Positives:**


 Abgangsbescheinigung der JKU Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften (Studienplan 2018W)

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `JKU Linz` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_25`)

**False Positives:**


5. Die belangte Behörde ersuchte mit Schreiben vom 02.12.2021 die Bf. um die in der  Beschwerde angekündigte Nachreichung der Unterlagen der WU Wien (Vergleich der  Studienrichtungen).

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

</details>

---

## `Bundesfinanzgerichts Genitive`

**F1:** 0.015 | **Precision:** 0.419 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgerichts' (genitive) specifically to ensure it is captured when the main BFG rule might miss it due to boundary issues.

**Content:**
```
\bBundesfinanzgerichts\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.419 | 0.007 | 0.015 | 31 | 13 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 18 | 1463 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_112`)


So konnten seitens des Bundesfinanzgerichts keine Feststellungen  hinsichtlich eines unverschuldeten oder unabwendbaren Ereignisses getroffen werden,  welches den Beschwerdeführer an seiner Pflichterfüllung hinderte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_93`)


Diese Sachverhaltsfeststellungen ergeben sich nach Dafürhalten des Bundesfinanzgerichts aus  den vorgelegten Akten des Abgabenverfahrens, dem Vorbringen der Bf. in seiner Beschwerde  sowie den Erhebungen durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) ( sent_id: `findok-manually-annotated_TRAIN/137355.1_233`)


Von Seiten des Bundesfinanzgerichts wird darauf verwiesen, dass § 1116 ABGB den  Vertragsparteien das Recht einräumt, sofern nichts anderes vereinbart wurde, den  Bestandvertrag über eine bewegliche Sache mit einer Frist von 24 Stunden zu kündigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) ( sent_id: `findok-manually-annotated_TRAIN/137355.1_298`)


Von Seiten des Bundesfinanzgerichts wird einleitend nochmals auf den Umstand hingewiesen,  dass die belangte Behörde die Versicherungsprämien nur in jenen Fällen in die  Bemessungsgrundlage miteinbezogen hat, in denen die Versicherung urkundlich vereinbart  und die Versicherungsprämie daher vom Leasingnehmer an die Beschwerdeführerin geleistet  wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated_TRAIN/149834.1_139`)


Die Beschwerde wurde der nunmehr zuständigen Gerichtsabteilung des Bundesfinanzgerichts  aufgrund einer Verfügung des Geschäftsverteilungsausschusses iZm der Pensionierung des  bisherigen Richters mit 01.07.2025 zugeteilt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_100`)

**False Positives:**


Das Erkenntnis des Bundesfinanzgerichts, Außenstelle Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des FA Wien 1/23  in vollem Umfang im Zuge einer Amtsrevision  angefochten.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_124`)

**False Positives:**


Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH der  Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels objektbezogener  Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen Erkenntnis des  Bundesfinanzgerichts dargestellten Höhe zustehe, erweise sich der Spruch des angefochtenen  10 von 39 Seite 11 von 39

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)
- `X GmbH` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_128`)

**False Positives:**


85-900/3590, BV 24 :  Beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  gab es betreffend dem  Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid  Gruppenmitglied:  21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010  27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010 nach Betriebsprüfung   27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010  20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010  (Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung  Rekultivierungskosten)  19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)  29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)  16.12.2013 Vorlage an BFG (damals noch UFS)  17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  Betreffend des Rechtsvorgängers Houdek Maschinenbau  wurde das Erkenntnis des  Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum  Veranlagungsjahr 2007 erlassen.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `85-900/3590` (tax_number)
- `Roelfsen Versicherung` (organisation)
- `UFS` (organisation)
- `Houdek Maschinenbau` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_433`)

**False Positives:**


30 Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH  der Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels  objektbezogener Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen  Erkenntnis des Bundesfinanzgerichts dargestellten Höhe zusteht, erweist sich der Spruch des  angefochtenen Erkenntnisses nicht als rechtswidrig.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)
- `X GmbH` (organisation)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_44`)

**False Positives:**


Die Beschwerde wurde der nunmehr zuständigen Gerichtsabteilung des Bundesfinanzgerichts  aufgrund einer Verfügung des Geschäftsverteilungsausschusses iZm der Pensionierung der  bisherigen Richterin mit 01.07.2025 zugeteilt.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

</details>

---

## `Verfassungsgerichtshof`

**F1:** 0.007 | **Precision:** 0.273 | **Recall:** 0.003  

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
| 0.273 | 0.003 | 0.007 | 22 | 6 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 16 | 1577 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated_TRAIN/149418.1_33`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149708.1`) ( sent_id: `findok-manually-annotated_TRAIN/149708.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) ( sent_id: `findok-manually-annotated_TRAIN/149863.1_50`)


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**


Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_172`)

**False Positives:**


Der Verfassungsgerichtshof ist bei der o.a, Entscheidung zum Ergebnis gelangt, dass ein  derartiger Fall, nämlich wenn eine Entscheidung derselben Behörde für einen früheren  Steuerzeitraum, die sich in der rechtlichen Würdigung des Sachverhaltes direkt auf einen  (einen späteren Steuerzeitraum betreffenden) Bescheid auswirkt, in gleicher Weise behandelt  werden muss, wie der Fall der Vorfrage;

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**


Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_293`)

**False Positives:**


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_295`)

**False Positives:**


Im der  zitierten Entscheidung des Verfassungsgerichtshofes zugrundeliegenden Sachverhalt war  strittig, ob bei nachträglicher Aktivierung eine beantragte Wiederaufnahme für die Folgejahre  zwecks Berücksichtigung der AfA vorzunehmen ist.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

</details>

---

## `SUVA Abbreviation`

**F1:** 0.053 | **Precision:** 0.750 | **Recall:** 0.028  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'SUVA' as an organization.

**Content:**
```
\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.750 | 0.028 | 0.053 | 64 | 48 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 48 | 16 | 937 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_11`)


Der dagegen erhobenen Beschwerde gab das Finanzamt mit Beschwerdevorentscheidung  insoweit teilweise Folge als die Pensionskassenleistung infolge im Streitjahr nicht erfolgter Aus- zahlung außer Ansatz blieb und die von der Invalidenversicherung sowie der SUVA ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe berücksichtigt wurden.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_12`)


Die beantragte Steu- erfreiheit der von der SUVA bezogenen Invalidenrente verneinte das Finanzamt indes mit der  Begründung, dass es sich dabei nicht um dem Grunde und der Höhe nach gleichartige Beträge  aus einer ausländischen Unfallversorgung handle, die einer inländischen gesetzlichen Unfall- versorgung entspreche, weil durch die Schweizer Invalidenrente – anders als in Österreich –  nicht primär ein individueller Schaden ersetzt werde, sondern der ausgefallene Verdienst und  solche Renten somit ein steuerpflichtiges Ersatzeinkommen darstellten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_13`)


3.  Mit Vorlageantrag wurde die Entscheidung über die Beschwerde durch das Bundesfinanzge- richt beantragt, wobei zusätzlich die Anrechnung des auf den steuerpflichtigen Teil der Invali- denrente entfallenden Anteiles der von der SUVA einbehaltenen Quellensteuer (5.623,80 CHF)  geltend gemacht wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_14`)


4.  Mit gesondertem Schriftsatz brachte die steuerliche Vertretung ergänzend vor, dass beim  Beschwerdeführer von der SUVA aufgrund eines Arbeitsunfalles im Jahr 2010 eine Beeinträch- tigung der Erwerbsfähigkeit von 90 % festgestellt worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_18`)


5.  In weiterer Folge setzte das Finanzamt mit Bescheid vom 4. Juli 2017 die Vorauszahlungen  an Einkommensteuer für 2017 und Folgejahre und mit Bescheiden vom 24. November 2017 die  Einkommensteuer 2016 sowie die Vorauszahlungen an Einkommensteuer für 2018 und Folge- jahre unter Berücksichtigung der gesamten von der SUVA bezogenen Invalidenrente fest, wo- gegen sich der Beschwerdeführer mit Beschwerde und – nach Ergehen abweisender Beschwer- devorentscheidungen – mit Vorlageantrag wandte.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_8`)

**False Positives:**


Entscheidungsgründe  I. Verfahrensgang  1.  Mit Bescheid vom 19. Jänner 2017 setzte das Finanzamt die Einkommensteuer für das Jahr  2015 fest, wobei die in Ansatz gebrachten, aus Renten von der Eidgenössischen Invalidenver- sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (SUVA) sowie einer Pensi- onskassenleistung resultierenden Einkünfte aus nichtselbständiger Arbeit aufgrund der Nicht- vorlage der angeforderten Unterlagen im Schätzungswege ermittelt wurden.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenver- sicherung` (organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)

**False Positives:**


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

FP: `SUVA` (organisation)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)

**False Positives:**


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_44`)

**False Positives:**


Es könnten daher in weiterer Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die SUVA-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, steuerfrei zu belassen sei, ge- troffen werden.

FP: `SUVA` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_58`)

**False Positives:**


In den hier interessierenden Jahren be- zog er eine Invalidenrente von der Eidgenössischen Invalidenversicherung (IV) und eine unter  Anrechnung dieser Rente ermittelte Invalidenrente (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (SUVA) in Höhe von jährlich 56.236,80 CHF.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

</details>

---

## `Fachhochschule and FH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Fachhochschule' or 'FH' followed by a location (e.g., Kärnten, Wien).

**Content:**
```
\b(?:Fachhochschule|FH)\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 14 | 0 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 14 | 1674 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_8`)

**False Positives:**


Vom Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an  der Fachhochschule Wiener Neustadt das Bachelorstudium Biotechnische Verfahren.

FP: `Fachhochschule Wiener` (organisation)

**✅ Gold Entities:**
- `Fachhochschule Wiener Neustadt` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_9`)

**False Positives:**


Im Rahmen der Beantwortung des Anspruchsüberprüfungsschreibens gab der Bf. am  16.02.2023 bekannt, dass T. nunmehr seit 15.02.2023 am FH Campus Wien Gesundheits- und  Krankenpflege studiere.

FP: `FH Campus` (organisation)

**✅ Gold Entities:**
- `FH Campus Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_48`)

**False Positives:**


Von Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an der  Fachhochschule Wiener Neustadt das Bachelorstudium Biotechnische Verfahren.

FP: `Fachhochschule Wiener` (organisation)

**✅ Gold Entities:**
- `Fachhochschule Wiener Neustadt` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_79`)

**False Positives:**


Vom Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an  der FH Wiener Neustadt für Wirtschaft und Technik GmbH (Tulln) das Bachelorstudium  Biotechnische Verfahren (FN000568).

FP: `FH Wiener` (organisation)

**✅ Gold Entities:**
- `FH Wiener Neustadt` (organisation)
- `Wirtschaft und Technik GmbH` (organisation)
- `Tulln` (city)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_81`)

**False Positives:**


Seit Februar 2023 studiert T. an der FH Campus Wien Gesundheits- und Krankenpflege  (FC000599).

FP: `FH Campus` (organisation)

**✅ Gold Entities:**
- `FH Campus Wien` (organisation)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `Bundeskanzleramt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundeskanzleramt' and its genitive form 'Bundeskanzleramtes'.

**Content:**
```
\bBundeskanzler(?:amt|amtes)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `LG für ZRS Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'LG für ZRS Wien'

**Content:**
```
\bLG\s+f\u00fcr\s+ZRS\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministeriums für Justiz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministeriums für Justiz' specifically

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

## `Landesgericht with LG Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'LG Landesgericht [Location]' or 'Landesgericht [Location]' or 'LG [Location]', stopping strictly before prepositions or verbs.

**Content:**
```
\b(?:LG\s+(?:Landesgericht\s+)?|Landesgericht\s+)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df\s]+?)(?=\s+(?:im|vom|am|von|ist|bietet|f\u00fchrt|hat|war|wurde|sind|waren|sowie|und|als|an|mit|der|die|das|ein|eine|einem|einer|den|die|dem|des|zur|im|um|zu|bei|nach|\u00fcber|unter|ohne|neben|zwischen|gegen|durch|seit|bis|vor|hinter|\(|,|\.|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Karl-Franzens- Universität Graz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific university name Karl-Franzens- Universität Graz.

**Content:**
```
\bKarl\-Franzens\-\s+Universität\s+Graz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Europäische Grenzschutzagentur Frontex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Europäische Grenzschutzagentur Frontex' and its genitive form.

**Content:**
```
\bEurop(?:e|en)ische\s+Grenzschutzagentur\s+Frontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ÖBUG GmbH Full Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific long-form law firm name including the 'ÖBUG' prefix and description.

**Content:**
```
\b"?ÖBUG"?\s+DR\.\s+NIKOLAUS\s+Wirtschaftstreuhand\s+GmbH\s*-\s+Wirtschaftsprüfungs-\s+und\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bezirksgericht with Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bezirksgericht' or 'BG Bezirksgericht' followed by a location name.

**Content:**
```
\b(?:BG\s+)?Bezirksgericht\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)(?=\s*(?:vom|am|von|ist|hat|wurde|sind|waren|\(|,|\.|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenbank Stallhofen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific bank name 'Raiffeisenbank Stallhofen'.

**Content:**
```
\bRaiffeisenbank\s+Stallhofen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mittel Unisyn GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Mittel Unisyn GMBH'.

**Content:**
```
\bMittel\s+Unisyn\s+GMBH\b
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

## `Verwaltungsgerichtshof and VwGH`

**F1:** 0.143 | **Precision:** 0.168 | **Recall:** 0.124  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof', 'Verwaltungsgerichtshofes', and 'VwGH', but excludes 'VwGH' when followed by a hyphen (e.g., VwGH-Entscheidung).

**Content:**
```
\bVerwaltungsgerichtshof(?:es)?\b|(?<!\w)VwGH\b(?![\s]*-)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.168 | 0.124 | 0.143 | 1285 | 216 | 1069 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 216 | 1069 | 1525 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_199`)


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_2`)

**False Positives:**


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_143`)

**False Positives:**


Die Nachsicht dient  nicht dazu, im Festsetzungsverfahren unterlassene Einwendungen (vor allem  Bescheidbeschwerden) nachzuholen (VwGH 17.10.2001, 98/13/0073;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_182`)

**False Positives:**


VwGH 27.3.1996, 92/13/0291;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_189`)

**False Positives:**


VwGH 20.6.1990, 89/13/0249;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_192`)

**False Positives:**


Unter dem Gesichtspunkt  der Zweckmäßigkeit (iSd § 20) ist auch die Gleichbehandlung von Abgabepflichtigen, somit  keine Benachteiligung ehrlicher Steuerschuldner durch Bevorzugung unehrlicher, zu  berücksichtigen (VwGH 4.4.1989, 88/14/0245;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_199`)

**False Positives:**


Zu dieser Problematik wurde auf eine  neu erlassene DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des VwGH  verwiesen (Ra 2020/13/0089).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_237`)

**False Positives:**


Eine sachliche Unbilligkeit der Abgabeneinhebung liegt vor, wenn im Einzelfall bei Anwendung  des Gesetzes ein vom Gesetzgeber offenbar nicht beabsichtigtes Ergebnis eintritt (VwGH  30.4.1999, 99/16/0086;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_240`)

**False Positives:**


Der in der anormalen  Belastungswirkung und verglichen mit ähnlichen Fällen, im atypischen Vermögenseingriff  gelegene offenbare Widerspruch der Rechtsanwendung zu den vom Gesetzgeber  beabsichtigten Ergebnissen muss seine Wurzel in einem außergewöhnlichen Geschehensablauf  haben, der eine vom Steuerpflichtigen nach dem gewöhnlichen Lauf nicht zu erwartende  Abgabenschuld ausgelöst hat, die zudem auch ihrer Höhe nach unproportional zum  auslösenden Sachverhalt ist“ (VwGH 21.1.2009, 2008/17/0138).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_241`)

**False Positives:**


Eine solche Unbilligkeit kann beispielsweise vorliegen, wenn eine vom Gesetz objektiv nicht  gewollte Doppelbesteuerung eintritt (VwGH 17.9.1990, 90/15/0118) oder zu einer  Besteuerung des Gewinnanteiles eines Minderheitsgesellschafters zu mehr als 200 % führt  (VwGH 23.4.1980, 3114/79).

FP: `VwGH` (organisation)


Eine solche Unbilligkeit kann beispielsweise vorliegen, wenn eine vom Gesetz objektiv nicht  gewollte Doppelbesteuerung eintritt (VwGH 17.9.1990, 90/15/0118) oder zu einer  Besteuerung des Gewinnanteiles eines Minderheitsgesellschafters zu mehr als 200 % führt  (VwGH 23.4.1980, 3114/79).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_243`)

**False Positives:**


Eine sachliche Unbilligkeit liegt nicht vor, wenn sie ganz allgemein die Auswirkung genereller  Normen ist (VwGH 22.3.1995, 93/15/0072;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_246`)

**False Positives:**


Die Nachsicht dient nicht dazu, im Festsetzungsverfahren unterlassene Einwendungen (vor  allem Bescheidbeschwerden) nachzuholen (VwGH 17.10.2001, 98/13/0073;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_248`)

**False Positives:**


Eine Unbilligkeit könnte  allenfalls vorliegen, wenn solche Rechtsmittel aussichtslos erschienen sind (insbesondere  wegen diesbezüglicher Rechtsauskünfte der Abgabenbehörde, VwGH 14.3.1986, 85/17/0143),  wegen entschuldbaren Rechtsirrtums unterblieben ( VwGH 13.11.1989, 88/15/0121;

FP: `VwGH` (organisation)


Eine Unbilligkeit könnte  allenfalls vorliegen, wenn solche Rechtsmittel aussichtslos erschienen sind (insbesondere  wegen diesbezüglicher Rechtsauskünfte der Abgabenbehörde, VwGH 14.3.1986, 85/17/0143),  wegen entschuldbaren Rechtsirrtums unterblieben ( VwGH 13.11.1989, 88/15/0121;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_249`)

**False Positives:**


20.9.1996, 93/17/0007 ) oder wegen Unzumutbarkeit nicht eingebracht wurden (VwGH  11.11.1982, 15/3470/80).(Ritz BAO6, § 236 Tz 14)  13 von 17 Seite 14 von 17

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_263`)

**False Positives:**


Im Nachsichtsverfahren können daher nicht  Einwände nachgeholt werden, die im Festsetzungsverfahren geltend zu machen gewesen  wären (VwGH 24.1.2007, 2003/13/0062).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_264`)

**False Positives:**


Das heißt, die Nachsicht kann nicht dazu dienen, im  Abgabenfestsetzungsverfahren unterlassene Einwendungen nachzuholen (VwGH 28.4.2004,  2001/14/0022).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_266`)

**False Positives:**


Durch eine Nachsicht können nur solche Auswirkungen der Abgabenvorschriften gemildert  werden, die der Gesetzgeber nicht selbst vorhergesehen hat (vgl. VwGH 24.11.1989,  87/17/0146;

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_272`)

**False Positives:**


Eine Nachsicht würde hier nicht  die Unbilligkeit der Einhebung beheben, sondern das Ergebnis der Abgabenfestsetzung  korrigieren (siehe hiezu VwGH 5.4.1957, 0040/56).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)

**False Positives:**


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

FP: `Verwaltungsgerichtshofes` (organisation)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)

**False Positives:**


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

FP: `Verwaltungsgerichtshofes` (organisation)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_279`)

**False Positives:**


Das  Bundesfinanzgericht hat grundsätzlich auf Grund der zum Zeitpunkt ihrer Entscheidung  gegebenen Sach- und Rechtslage zu entscheiden (vgl. VwGH 24.3.2009, 2006/13/0149).

FP: `VwGH` (organisation)

**✅ Gold Entities:**

</details>

---

## `Verwaltungsgerichtshof Genitive`

**F1:** 0.134 | **Precision:** 0.428 | **Recall:** 0.080  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs' (genitive forms).

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.428 | 0.080 | 0.134 | 325 | 139 | 186 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 139 | 186 | 1584 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_274`)


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_278`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_289`)


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_146`)


Entgegen der Rechtsansicht des Bf, dass der erste tatsächliche Studienwechsel zum Studium  der biotechnischen Verfahren erfolgt ist, gilt auch der Rückwechsel vom Bachelorstudium  Wirtschaftsrecht auf das Studium Rechtswissenschaften nach der zitierten Judikatur des  Verwaltungsgerichtshofes (VwGH 01.02.1990, 89/12/0175) als Studienwechsel.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_163`)


Subjektive  Momente, wie Verschulden an der (ursprünglichen oder weiteren) Auszahlung der  Familienleistungen, Gutgläubigkeit des Empfangs der Familienbeihilfe und des  Kinderabsetzbetrags oder die Verwendung der Familienbeihilfe und des Kinderabsetzbetrags,  sind nach ständiger Rechtsprechung des Verwaltungsgerichtshofes für die Verpflichtung zur  Rückerstattung unrechtmäßiger Beihilfenbezüge unerheblich.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_175`)


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_124`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_45`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes besteht keine Entscheidungspflicht  betreffend Anregung einer Wiederaufnahme des Verfahrens (VwGH 22.5.2014, 2011/15/0064,  VwGH 20.2.2019, Ro 2016/13/0011).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_63`)


Nach der Rechtsprechung des Verwaltungsgerichtshofes (vgl. VwGH 16.10.2016, Ra  2014/15/0058) ist bei einem Antrag auf Wiederaufnahme des Verfahrens das  Neuhervorkommen von Tatsachen aus Sicht des Antragstellers zu beurteilen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_69`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_70`)


Das Erkenntnis folgt der zitierten Rechtsprechung des Verwaltungsgerichtshofes und liegt  damit keine Rechtsfrage grundsätzlicher Bedeutung vor.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) ( sent_id: `findok-manually-annotated_TRAIN/149497.1_28`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_73`)


zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.


zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated_TRAIN/149809.1_27`)


1.1. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


1.1. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_105`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_106`)


Im vorliegenden Fall handelt es sich um keine Rechtfrage von grundsätzlicher Bedeutung, da  das Bundesfinanzgericht in rechtlicher Hinsicht der in der Entscheidung dargestellten Judikatur  des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149765.1`) ( sent_id: `findok-manually-annotated_TRAIN/149765.1_31`)


3.3. Zu Spruchpunkt III. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


3.3. Zu Spruchpunkt III. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) ( sent_id: `findok-manually-annotated_TRAIN/149741.1_43`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) ( sent_id: `findok-manually-annotated_TRAIN/149741.1_44`)


Die gegenständliche Entscheidung gründet auf der zitierten Rechtsprechung des  Verwaltungsgerichtshofes.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_274`)

**False Positives:**


Sofern der Bf. das Vorliegen einer persönliche Unbilligkeit vorbringt, weil die Entrichtung der  Abgabenschulden ihn bei seiner derzeitigen Einkommens- und Vermögenslage in besondere  finanzielle Schwierigkeiten bzw. Notlage bringen und zu einer Existenzgefährdung führen  würde, ist dem vorerst zu entgegnen, dass nach der Rechtsprechung des  Verwaltungsgerichtshofes (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte zur Steuerzahlung heranzuziehen, die Abgabeneinhebung noch nicht unbillig  erscheinen lässt.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_278`)

**False Positives:**


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- und Einkommensverhältnisse zum Zeitpunkt der  Entscheidung über das Ansuchen maßgebend (vgl. VwGH 17.11.2010, 2007/13/0135).

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_289`)

**False Positives:**


Der Bf. ist daher auf die ständige Rechtsprechung des Verwaltungsgerichtshofes zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren eine erhöhte  Mitwirkungspflicht trifft.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_71`)

**False Positives:**


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Eine Rechtsfrage grundsätzlicher Bedeutung liegt vor  Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_75`)

**False Positives:**


Davon ist nach ständiger Rechtsprechung des  Verwaltungsgerichtshofes dann auszugehen, wenn die Abgabenbehörde bei ordnungsgemäßer  Prüfung der Abgabenerklärung die Unrichtigkeit hätte erkennen müssen, ohne ein weiteres  Ermittlungsverfahren durchzuführen (wären Unrichtigkeiten erst nach weiter gehenden  Ermittlungen erkennbar, so sind sie nicht offensichtlich iSd § 293b BAO), wobei die  Unrichtigkeit sowohl in einer unzutreffenden Rechtsauffassung als auch in einer in sich  widersprüchlichen oder eindeutig gegen menschliches Erfahrungsgut sprechenden  Sachverhaltsdarstellung zum Ausdruck kommen kann (VwGH 26.2.2013, 2010/15/0202;

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_111`)

**False Positives:**


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_186`)

**False Positives:**


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes kommt es bei der Frage, ob ein  Wiederaufnahmegrund vorliegt auf den Wissensstand der Behörde im Zeitpunkt der Erlassung  des Bescheides an, mit welchem jenes Verfahren abgeschlossen worden ist, welches  wiederaufgenommen werden soll (VwGH 29.9.2004, 2001/13/0135).

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_261`)

**False Positives:**


2.2 Unzulässige Vermengung der Begründungselemente der VwGH-Entscheidung durch das  FA Wien 1/23  In ihren Ausführungen hinsichtlich der Begründung der Wiederaufnahme nimmt das Finanzamt  immer wieder auf die Entscheidung des Verwaltungsgerichtshofes im Beschwerdeverfahren  22 von 39 Seite 23 von 39

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_264`)

**False Positives:**


Diese  Ausführungen stehen im Widerspruch zum Erkenntnis des Verwaltungsgerichtshofes.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_307`)

**False Positives:**


haben sich durch die Entscheidung des Verwaltungsgerichtshofes keinerlei Änderungen  ergeben.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_311`)

**False Positives:**


- Gegenständlich wurde seitens des Verwaltungsgerichtshofes gerade nicht über eine Vorfrage  iSd § 116 BAO erkannt;

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_486`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1_50`)

**False Positives:**


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_187`)

**False Positives:**


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_188`)

**False Positives:**


Da für die Lösung der Rechtsfrage nicht von der vorhandenen Rechtsprechung des  Verwaltungsgerichtshofes abgewichen wurde, war eine ordentliche Revision als unzulässig zu  erklären.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1_93`)

**False Positives:**


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1_94`)

**False Positives:**


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_73`)

**False Positives:**


zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)


zukommt, insbesondere weil das Erkenntnis nicht von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_107`)

**False Positives:**


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes muss das Merkmal der  Zwangsläufigkeit auch der Höhe nach gegeben sein.

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

</details>

---

## `Finanzamt Österreich Specific`

**F1:** 0.116 | **Precision:** 0.947 | **Recall:** 0.062  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' and 'Finanzamtes Österreich' specifically to avoid partial matches.

**Content:**
```
\bFinanz(?:amt|amtes)\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.947 | 0.062 | 0.116 | 114 | 108 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 108 | 6 | 1573 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Priv.-Doz. Niklas Bußjann  in der Beschwerdesache ÖkR ÖkR Jonas Sternekicker,  Mühlbach 2, 4851 Fischhamering, Österreich, gegen den von der belangten Behörde Finanzamt Österreich am 15. Mai 2025  zu Steuernummer 98-117/5180  ausgefertigten Bescheid betreffend Einkommensteuer für  das Jahr 2024 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 Abs. 1 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde des  Desiree Häfke, Weinrebengasse 209, 4282 Hinterhütten, Österreich, vom 11. September 2023 gegen den Bescheid des Finanzamtes  Österreich vom 7. September 2023 betreffend   - Rückforderung von Familienbeihilfe und Kinderabsetzbeträgen für Kind T. für den Zeitraum  Jänner 2021 bis Dezember 2022   - Rückforderung von Familienbeihilfe für Kind A. für den Zeitraum Jänner 2021 bis Oktober  2022 (Geschwisterstaffel anteilig)  - Rückforderung von Familienbeihilfe für Kind B. für den Zeitraum Jänner 2021 bis Oktober  2021 (Geschwisterstaffel anteilig)  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Wolfgang Pavlik über die Beschwerde der  August Ronzheimer, Daimlerweg 3, 5221 Babenham, Österreich, vom 26. Mai 2023 gegen den Bescheid des Finanzamtes Österreich  vom 28. April 2023 betreffend Abweisung des Antrages auf Familienbeihilfe ab Oktober 2022,  zu Recht erkannt:   Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) ( sent_id: `findok-manually-annotated_TRAIN/149497.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Dr. Hans Blasina in der Beschwerdesache  James Grentz, Katharine-Drexel-Straße 5, 3661 Lohsdorf, Österreich, vertreten durch T & M TRAUNSTEINER U. MITTERER KG,  Schubertviertel 38, 4300 St.Valentin, betreffend Beschwerde vom 16. Mai 2024 gegen den  Bescheid des Finanzamtes Österreich vom 7. Mai 2024 betreffend Anspruchszinsen (§ 205  BAO) 2022 (Einkommensteuer) Steuernummer 90-523/9682  beschlossen:  Die Beschwerde wird gemäß § 261 Abs 1 lit a BAO für gegenstandlos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter R. in der Beschwerdesache   Agatha Vesper, Albersdorfweg 21, 4973 Rabenfurt, Österreich, betreffend Beschwerde vom 9. Juli 2024 gegen den Bescheid des  Finanzamtes Österreich vom 17. Juni 2024 betreffend Abweisung des Antrages vom  31. Jänner 2024 auf den Erhöhungsbetrag zur Familienbeihilfe ab Jänner 2024, Steuernummer  58-042/7990 (SVNR 6155 130467), beschlossen:   Der Vorlageantrag vom 20. November 2024 wird gemäß § 260 Abs. 1 lit. b  Bundesabgabenordnung (BAO) iVm § 264 Abs. 4 lit. e BAO als nicht fristgerecht eingebracht  zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.a Linda Abdulla  in der Beschwerdesache Merlin Jespersen, LLB,  Graf-Hoyos-Weg 5, 9313 Fiming, Österreich, über die Beschwerde vom 17. Dezember 2019 gegen die Bescheide des  Finanzamtes Österreich vom 16. Dezember 2019 betreffend Einkommensteuer  (Arbeitnehmerveranlagung) 2016 bis 2018 zu Steuernummer 37-035/4368  zu Recht  erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149765.1`) ( sent_id: `findok-manually-annotated_TRAIN/149765.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Monika Ahorn in der Beschwerdesache  Irvin Altbauer, Kreuzfeldweg 69, 5272 Himmelschlag, Österreich, vertreten durch Dr. Thomas Krankl, Lerchenfelder Straße  120/2/28, 1080 Wien, über die Beschwerde vom 22. Jänner 2021 gegen den Bescheid des  Finanzamtes Österreich vom 13. Jänner 2021 Einkommensteuer (Arbeitnehmerveranlagung)  2019 (Steuernummer 18-845/4090 ) nach Durchführung einer mündlichen Verhandlung am  07.11.2025 in Anwesenheit des Schriftführers Dietmar Gratz  I. beschlossen:  Der Vorlageantrag vom 23.11.2022 wird als gegenstandslos erklärt (§ 85 Abs. 2 iVm § 256 Abs.  3 iVm § 264 Abs. 4 lit. d BAO).

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Univ.-Prof.in Jacqueline Bruemmer  in der Beschwerdesache Konstanze Bertling,  Pabstbergstraße 45, 9135 Unterort, Österreich, über die Beschwerden vom 24. August 2017 (eingebracht am 28. August 2017)  gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr Finanzamt Österreich) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme des Verfahrens gemäß § 303 BAO betreffend  die Einkommensteuer 2012 und 2013 und über die Beschwerden vom 31. August 2017  (eingebracht am 5. September 2017) gegen die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  Finanzamt Österreich) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme des  Verfahrens gemäß § 303 BAO betreffend die Einkommensteuer 2014 und 2015, Steuernummer  88-575/7122   zu Recht erkannt:   I. Die angefochtenen Bescheide vom 26. Juli 2017 und vom 3. August 2017 werden  gemäß § 279 BAO aufgehoben.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) ( sent_id: `findok-manually-annotated_TRAIN/149741.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Corvin Diebald, Pitzelstätten 4, 2490 Ebenfurth, Österreich, vertreten durch Dr. Ronald Rödler, Lagerstraße 5/1/20, 2460  Bruck/Leitha über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 11. September 2019  betreffend Aussetzung gemäß § 212a BAO zu Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149682.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149682.1_1`)


BESCHLUSS  Das Bundesfinanzgericht beschließt durch den Richter Mag. David Hell LL.B. LL.M. in der  Beschwerdesache Ingolf Johannisbauer, Hochtregister Straße 44, 9560 Weit, Österreich, vertreten durch Dr. Michael Kotschnigg,  Stadlauer Straße 39/I/12, 1220 Wien, betreffend Beschwerde vom 16. Mai 2023 (eingebracht  am 1. September 2025) gegen den Bescheid des Finanzamtes Österreich vom 21. April 2023  betreffend Zurückweisung eines Antrages auf Festsetzung von Umsatzsteuerzinsen gemäß  § 205c BAO, Steuernummer 08-788/8579:  I. Die Beschwerde wird als verspätet zurückgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Ferdinand Mielnickel, Viertelweg 16, 3720 Gaindorf, Österreich, vertreten durch Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien, über die Beschwerde vom  30. November 2017 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt  Österreich) vom 31. Oktober 2017 betreffend Festsetzung eines Verspätungszuschlages  betreffend Einkommensteuer 2015 und 2016 und Umsatzsteuer 2015 und 2016,  Steuernummer 86-167/7419  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt  Österreich` | `Finanzamt  Österreich` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/138550.1`) ( sent_id: `findok-manually-annotated_TRAIN/138550.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eberhard Kreislmeier  in der Beschwerdesache Vera Soldtwedel,  Gaas 20, 3494 Schlickendorf, Österreich, betreffend Beschwerde vom 15. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 betreffend Mehrkindzuschlag 2021 zur  Steuernummer 39-381/5653  beschlossen:  I. Die Parteien werden gemäß § 281a BAO formlos darüber verständigt, dass nach Auffassung  des Bundesfinanzgerichtes ein Vorlageantrag nicht eingebracht wurde.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/138550.1`) ( sent_id: `findok-manually-annotated_TRAIN/138550.1_48`)


IV. Formlose Verständigung gemäß § 281a BAO:  Das Bundesfinanzgericht ist in der Beschwerdesache Vera Soldtwedel (Gaas 20, 3494 Schlickendorf, Österreich) zur Beschwerde  vom 15. April 2022 gegen den Bescheid des Finanzamtes Österreich vom 1. April 2022  4 von 6 Seite 5 von 6

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) ( sent_id: `findok-manually-annotated_TRAIN/149404.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Johann Fischerlehner in der  Beschwerdesache Veronika Ogrissek, Weißeneggerberg 160, 3631 Kienings, Österreich, über die Beschwerde vom 23. September 2024  gegen die Bescheide des Finanzamtes Österreich vom 16. September 2024 betreffend  Pfändung einer Geldforderung und Verfügungsverbot zu Steuernummer 48-541/5488  zu  Recht erkannt:   I. Die Beschwerde gegen den Bescheid betreffend Pfändung einer Geldforderung wird  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) ( sent_id: `findok-manually-annotated_TRAIN/149404.1_12`)


In der Bescheidbeschwerde wurde im Wesentlichen vorgebracht, dass die Unterlagen zum  Einkommen 2021 und 2022 per Fax und per Einschreiben an das Finanzamt Österreich in Wien  zugesandt worden wären.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) ( sent_id: `findok-manually-annotated_TRAIN/149404.1_15`)


Mit Beschwerdevorentscheidung vom 08.10.2024 wurde die gegenständliche  Bescheidbeschwerde als unbegründet abgewiesen und zur Begründung angeführt:  „Der Antrag wird damit begründet, dass sämtliche Unterlagen an das Finanzamt Österreich  zugesandt wurden und man unrechtmäßig den Betrag gepfändet hat.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

FP: `Finanzamtes  Österreich` (organisation)

**✅ Gold Entities:**
- `Dr.in Estelle Niederholz` (person)
- `Hon.-Prof.in OStR Tosca Knoller` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

</details>

---

## `Bundesfinanzgerichtes Genitive`

**F1:** 0.072 | **Precision:** 0.439 | **Recall:** 0.039  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgerichtes' (genitive) specifically.

**Content:**
```
\bBundesfinanzgerichtes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.439 | 0.039 | 0.072 | 155 | 68 | 87 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 68 | 87 | 1655 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_297`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_175`)


Unzulässigkeit der Revision:  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_124`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_69`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149497.1`) ( sent_id: `findok-manually-annotated_TRAIN/149497.1_28`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated_TRAIN/149809.1_27`)


1.1. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_40`)


Mit 01.07.2025 wurde die Beschwerde der nunmehr zuständigen Gerichtsabteilung des  Bundesfinanzgerichtes aufgrund einer Verfügung des Geschäftsverteilungsausschusses iZm der  Pensionierung der zuständigen Richterin zugeteilt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_65`)


Dies wird von der  belangten Behörde ebenfalls nicht bestritten und wird daher seitens des  Bundesfinanzgerichtes als gegeben angenommen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_83`)


(Eine Stornierung der  entsprechenden Guthabensbuchung erfolgt mit 27./28.11.2025 durch die belangte Behörde  aufgrund des Vorhaltes des Bundesfinanzgerichtes vom 26.11.2025.)   § 300 BAO sieht jedoch vor, dass ab Vorlage der Beschwerde die Abgabenbehörden beim  Verwaltungsgericht mit Bescheidbeschwerde angefochtene Bescheide und allfällige  Beschwerdevorentscheidungen bei sonstiger Nichtigkeit weder abändern noch aufheben  können.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_105`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149765.1`) ( sent_id: `findok-manually-annotated_TRAIN/149765.1_31`)


3.3. Zu Spruchpunkt III. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) ( sent_id: `findok-manually-annotated_TRAIN/149741.1_39`)


Über die Beschwerde gegen die Haftungsinanspruchnahme des Beschwerdeführers gemäß  § 9a BAO wurde mit Erkenntnis des Bundesfinanzgerichtes vom 29. Oktober 2025 entschieden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) ( sent_id: `findok-manually-annotated_TRAIN/149741.1_43`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_120`)


Gemäß §§ 2a und 269 Abs. 1 BAO gilt dies auch für Ermessensentscheidungen des  Bundesfinanzgerichtes.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_134`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/138550.1`) ( sent_id: `findok-manually-annotated_TRAIN/138550.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Eberhard Kreislmeier  in der Beschwerdesache Vera Soldtwedel,  Gaas 20, 3494 Schlickendorf, Österreich, betreffend Beschwerde vom 15. April 2022 gegen den Bescheid des  Finanzamtes Österreich vom 1. April 2022 betreffend Mehrkindzuschlag 2021 zur  Steuernummer 39-381/5653  beschlossen:  I. Die Parteien werden gemäß § 281a BAO formlos darüber verständigt, dass nach Auffassung  des Bundesfinanzgerichtes ein Vorlageantrag nicht eingebracht wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/138550.1`) ( sent_id: `findok-manually-annotated_TRAIN/138550.1_59`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  5 von 6 Seite 6 von 6

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/138550.1`) ( sent_id: `findok-manually-annotated_TRAIN/138550.1_61`)


Der gegenständliche Beschluss enthält die explizit im Gesetz (§ 281a BAO) vorgesehene  formlose Verständigung, dass nach Auffassung des Bundesfinanzgerichtes ein Vorlageantrag  nicht eingebracht wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) ( sent_id: `findok-manually-annotated_TRAIN/149404.1_10`)


Der beschwerdeführenden Partei wurde gemäß § 85 Abs. 2 iVm § 2a BAO mit Beschluss des  Bundesfinanzgerichtes vom 5.5.2025 aufgetragen, den Mangel der fehlenden Unterschrift  binnen einer Woche ab Zustellung des Beschlusses nachzuholen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149404.1`) ( sent_id: `findok-manually-annotated_TRAIN/149404.1_95`)


Zur Zulässigkeit einer Revision  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_297`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149552.1_69`)

**False Positives:**


III. Zulässigkeit einer Revision  Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des Bundesfinanzgerichtes die Revision an  den Verwaltungsgerichtshof zulässig, wenn sie von der Lösung einer Rechtsfrage abhängt, der  4 von 5 Seite 5 von 5

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_111`)

**False Positives:**


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_103`)

**False Positives:**


Laut Amtsrevision wurde die Rechtsansicht des Bundesfinanzgerichtes, das freie Wahlrecht des  innerbetrieblichen Verlustausgleiches bei einer § 7 (3)-KStG-Körperschaft zuzulassen und  daraus folgend eine willkürliche Verlustverrechnung zuzulassen, vom revisionswerbenden  Finanzamt nicht geteilt.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_152`)

**False Positives:**


Im Zuge der VwGH- Entscheidung vom 13.09.2018 zu Ro  2016/15/0010 wurde durch den VwGH als Vorfrage für die Höhe des Verlustvortrages für die  Folgejahre nach 2007 ausgeführt, dass entgegen der Rechtsmeinung des BFG kein freies  Wahlrecht in Bezug auf den innerbetrieblichen Verlustausgleich im Jahr 2007 vor der  Abspaltung existiert und daraus folgend ein Verlustvortrag nur nach der Spezialregelung des §  35 UmgrStG iVm § 21 UmgrStG zu gewähren ist (objektbezogener Verlustvortrag) und somit  der Verlustvortrag nicht in der im Erkenntnis des Bundesfinanzgerichtes dargestellten Höhe  zusteht (vgl. Seite 7 und 8 der VwGH-Entscheidung).

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_232`)

**False Positives:**


Auf Basis dieser  Entscheidung des Bundesfinanzgerichtes und der daran anknüpfenden Konsequenzen iHa die  Verlustverrechnung im Jahr 2010 auf Ebene der Rechtsnachfolgerin der Houdek Maschinenbau  wurde  20 von 39 Seite 21 von 39

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**
- `Houdek Maschinenbau` (organisation)

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_235`)

**False Positives:**


Im  Revisionsverfahren wurde VwGH die Entscheidung des Bundesfinanzgerichtes im Hinblick auf  die Höhe des 2007 angefallenen Verlustes explizit bestätigt und die Revision des Finanzamtes  als unbegründet abgewiesen;

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_246`)

**False Positives:**


Unter Zugrundelegung dieser Würdigung habe sich gezeigt, dass  der Verlustvortrag gegenständlich nicht in der im Erkenntnis des Bundesfinanzgerichtes  dargestellten Höhe zustehe, sondern ausschließlich eine Ermittlung auf Basis einer  objektbezogenen Zuordnung erfolgen müsse.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_271`)

**False Positives:**


Der VwGH hält in Rz 30 ausdrücklich fest, dass sich  der Spruch des angefochtenen Erkenntnisses (Erkenntnis des Bundesfinanzgerichtes vom 27.  Jänner 2016, RV/5101064/2013, betreffend Körperschaftsteuer 2007) nicht als rechtswidrig  erweist, auch wenn der Verlustvortrag in den Jahren nach 2007 nur mittels objektbezogener  Zuordnung zu ermittelnder Höhe zusteht.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_381`)

**False Positives:**


Was nunmehr mittels des streitgegenständlichen Wiederaufnahmebescheides und Erlassung  des neuen Feststellungsbescheides GM für 2010 vom 29.1.2019 passiert, ist - wie bereits  erwähnt - nichts anderes als die Rückgängigmachung der Korrektur vom 7.3.2016, nachdem  der Verwaltungsgerichtshof (das Verwaltungsgericht zweiter Stufe) die Rechtsansicht des  Bundesfinanzgerichtes (als Verwaltungsgericht erster Stufe) verworfen hatte.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_429`)

**False Positives:**


Gegen die Entscheidung des Bundesfinanzgerichtes wurde Amtsrevision erhoben.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_446`)

**False Positives:**


Die Abgabenbehörde hat hier die Entscheidung des Bundesfinanzgerichtes vom  27.1.2016 (BFG vom 27.1.2016, RV/5101064/2013) zugrunde gelegt und den Verlustvortrag  erhöht.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_486`)

**False Positives:**


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148650.1_50`)

**False Positives:**


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_187`)

**False Positives:**


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1_74`)

**False Positives:**


sowie  zahlreiche Erkenntnisse des Bundesfinanzgerichtes).

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1_75`)

**False Positives:**


Wegen dieser Bindung ist der Zinsenbescheid nicht (mit Aussicht auf Erfolg) mit der  Begründung anfechtbar, der maßgebende Einkommensteuerbescheid sei inhaltlich  rechtswidrig (Ritz, BAO8, § 205 Tz 34 mit Hinweis auf die ständige Rechtsprechung des  Bundesfinanzgerichtes).

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1_93`)

**False Positives:**


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_121`)

**False Positives:**


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Der Finanzstrafsenat Wien 2 des Bundesfinanzgerichtes hat in der Finanzstrafsache gegen  1.

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**
- `Finanzstrafsenat Wien 2` (organisation)

</details>

---

## `Tax Authority Abbreviations FAG FAÖ`

**F1:** 0.071 | **Precision:** 1.000 | **Recall:** 0.037  

**Format:** `regex`  
**Description:**
Matches the specific tax authority abbreviations 'FAG' (Finanzamt für Großbetriebe) and 'FAÖ' (Finanzamt Österreich) as standalone entities.

**Content:**
```
\b(?:FAG|FA\u00d6)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.037 | 0.071 | 64 | 64 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 64 | 0 | 1491 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149809.1_22`)


Am 5. November 2025 kam es vor dem Bundesfinanzgericht (BFG) zu einem Erörterungstermin  (ET), zu dem der Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  FAÖ sowie ein Mitarbeiter der Abgabensicherung geladen wurden.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_4`)


Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.


Entscheidungsgründe  I. Verfahrensgang  Zwischen den Parteien ist vorerst die Frage strittig, ob das Finanzamt Österreich (in der Folge  kurz: FAÖ) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: FAG) erlassenen Bescheiden zuständig ist.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAG` | `FAG` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_5`)


Das FAG erließ am 21.8.2024 einen Bescheid über die Aufhebung des Umsatzsteuerbescheides  2022 vom 8.9.2023 und verband diese mit dem ebenfalls vom selben Tag datierenden  Sachbescheid.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_7`)


Am 5.11.2024 hob das FAG den Umsatzsteuerbescheid 2022 vom 21.8.2024  erneut nach § 299 BAO auf und erließ einen neuen Jahresbescheid.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_8`)


Weiters hob das FAG am  26.5.2025 den Umsatzsteuerbescheid des Jahres 2023 gemäß § 299 BAO auf und verband  1 von 5 Seite 2 von 5

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_10`)


Dagegen wurde von der Bf. am 16.6.2025 Beschwerde, eingebracht beim FAG, erhoben.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_11`)


Mit Schreiben vom 11.7.2025 teilte das FAG der Bf. mit, dass die Steuernummer auf das FAÖ  übergegangen sei.


Mit Schreiben vom 11.7.2025 teilte das FAG der Bf. mit, dass die Steuernummer auf das FAÖ  übergegangen sei.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |
| `FAÖ` | `FAÖ` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_12`)


Mit Beschwerdevorentscheidungen vom 17.7.2025 wies das FAÖ die Beschwerden sowohl  gegen den Umsatzsteuerbescheid 2022 vom 5.11.2024, als auch jene das Jahr 2023 betreffend  vom 26.5.2025, als unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_13`)


Die Bf. richtete daraufhin am 13.8.2025 einen Vorlageantrag an das FAÖ, dies verbunden mit  dem Antrag auf Durchführung einer mündlichen Verhandlung und Entscheidung durch den  Senat.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_14`)


Inhaltlich monierte die Bf. insbesondere, dass rücksichtlich der Bestimmung des § 59  BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde, nämlich dem FAÖ  anstatt dem FAG, erlassen worden seien.


Inhaltlich monierte die Bf. insbesondere, dass rücksichtlich der Bestimmung des § 59  BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde, nämlich dem FAÖ  anstatt dem FAG, erlassen worden seien.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAG` | `FAG` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_16`)


Das Verwaltungsgericht forderte sowohl das FAÖ als auch das FAG am 21.10.2025 auf, die  bezughabenden Akten vorzulegen und umfassend zum Vorbringen der Bf. Stellung zu nehmen.


Das Verwaltungsgericht forderte sowohl das FAÖ als auch das FAG am 21.10.2025 auf, die  bezughabenden Akten vorzulegen und umfassend zum Vorbringen der Bf. Stellung zu nehmen.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAG` | `FAG` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_17`)


Daraufhin teilte das FAG am 22.10.2025 mit, dass es den Einwand, wonach die  Beschwerdevorentscheidungen vom 17.7.2025 von der unzuständigen Behörde erlassen  worden seien, teile.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_18`)


Das FAÖ gab am selben Tag bekannt, sich der Stellungnahme des FAG  vollinhaltlich anzuschließen.


Das FAÖ gab am selben Tag bekannt, sich der Stellungnahme des FAG  vollinhaltlich anzuschließen.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAG` | `FAG` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_27`)


Alle genannten Bescheide wurden  vom FAG als damals für die Bf. zuständige Behörde erlassen;

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_28`)


die Beschwerden wurden allesamt  beim FAG eingebracht.

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_30`)


Mit Schreiben vom 11.7.2025 wurde die Bf. darüber in Kenntnis gesetzt, dass die  Steuernummer auf das FAÖ übergegangen sei.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_31`)


Mit Beschwerdevorentscheidungen je vom 17.7.2025 wies nunmehr das FAÖ die Beschwerden  gegen die Umsatzsteuerbescheide 2022 und 2023 als unbegründet ab.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_32`)


Die Bf. richtete daraufhin am 13.8.2025 einen Vorlageantrag an das FAÖ, dies verbunden mit  dem Antrag auf Durchführung einer mündlichen Verhandlung und Entscheidung durch den  Senat.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149505.1`) ( sent_id: `findok-manually-annotated_TRAIN/149505.1_34`)


Inhaltlich monierte die Bf. -  soweit für die vorerst maßgebliche Rechtsfrage von Relevanz -, dass rücksichtlich der  Bestimmung des § 59 BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde,  nämlich dem FAÖ anstatt dem FAG, erlassen worden seien.


Inhaltlich monierte die Bf. -  soweit für die vorerst maßgebliche Rechtsfrage von Relevanz -, dass rücksichtlich der  Bestimmung des § 59 BAO die Beschwerdevorentscheidungen von der unzuständigen Behörde,  nämlich dem FAÖ anstatt dem FAG, erlassen worden seien.

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAG` | `FAG` |

</details>

---

## `Houdek Maschinenbau`

**F1:** 0.062 | **Precision:** 1.000 | **Recall:** 0.032  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Houdek Maschinenbau'.

**Content:**
```
\bHoudek\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.032 | 0.062 | 56 | 56 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 56 | 0 | 1481 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_17`)


Der Sachverhalt ergibt sich bisherigen Verfahren wie folgt:   a) Sachverhalt und Verfahrensablauf bei der Houdek Maschinenbau, Str.Nr.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_18`)


95-002/7970, BV 24:  Das Unternehmen Houdek Maschinenbau  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_20`)


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_22`)


Zum Stichtag 31.12.2008 ist die Houdek Maschinenbau  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan vom 29.06.2009 gemäß § 39 UmgrStG in einem ersten  Umgründungsschritt als übertragende Gesellschaft (neben anderen Gesellschaften) mit der  Lexdon IT  als übernehmende Gesellschaft verschmolzen worden.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_25`)


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_26`)


Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_28`)


In den Jahren 2011 bis 2013 fand eine Außenprüfung gemäß § 147 BAO durch die  Großbetriebsprüfung (Außenstelle Linz) über die Jahre 2007 und 2008 bei der Houdek Maschinenbau  statt.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_33`)


Begründend führte das Finanzamt zusammenfassend aus,  dass die Houdek Maschinenbau  aufgrund der Rechtsform eine nach unternehmensrechtlichen  Vorschriften zur Rechnungslegung verpflichtete Körperschaft im Sinne des § 7 Abs. 3 KStG 1988  3 von 39 Seite 4 von 39

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_45`)


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_49`)


Teilbetriebe  Schmeltz Luftfahrt:   Verluste  geschlossene  Teilbetriebe  Houdek Maschinenbau:   -326.546,95 6,78 %

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_51`)


Verluste  verbleibende  Teilbetriebe  Houdek Maschinenbau:  -3.606.018,18 74,89 %

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_54`)


Abgespaltene  Tankstellen  Schmeltz Luftfahrt **   Geschlossene  Tankstellen  Houdek Maschinenbau **  Verkaufte  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **


Abgespaltene  Tankstellen  Schmeltz Luftfahrt **   Geschlossene  Tankstellen  Houdek Maschinenbau **  Verkaufte  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **


Abgespaltene  Tankstellen  Schmeltz Luftfahrt **   Geschlossene  Tankstellen  Houdek Maschinenbau **  Verkaufte  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **


Abgespaltene  Tankstellen  Schmeltz Luftfahrt **   Geschlossene  Tankstellen  Houdek Maschinenbau **  Verkaufte  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_59`)


Ergebnis  Roelfsen Versicherung  -2.966.376,17       Gegen den Körperschaftsteuerbescheid 2007 wurde von der mitbeteiligten Partei  Roelfsen Versicherung (als partieller Gesamtrechtsnachfolger der Houdek Maschinenbau) mit Schreiben vom  31.05.2013 Beschwerde erhoben.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_62`)


Begründend führte die  Beschwerdeführerin in der Beschwerde aus, dass die Gewinnermittlung für 2007 auf der Ebene  der Houdek Maschinenbau  nach allgemeinen Grundsätzen durchzuführen sei, da der  Vermögensübergang hinsichtlich der 11 Tankstellen auf die Schmeltz Luftfahrt  erst mit Ablauf des  Spaltungsstichtages (Spaltungsstichtag 31.12.2007) per 1.1.2008 stattgefunden habe.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_63`)


Die  einzelnen Tankstellen der Houdek Maschinenbau  seien jeweils als eigenständige Teilbetriebe zu  qualifizieren, für die jeweils gesondert der (Teilbetriebs)Gewinn zu ermitteln sei.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_66`)


Die Houdek Maschinenbau  habe daher jene Verluste, die den per 31.12.2007 auf die  Schmeltz Luftfahrt  abgespaltenen Tankstellen zuzurechnen seien, vorrangig (und nicht wie von der  BP vorgesehen nur aliquot) im Wege eines innerbetrieblichen Verlustausgleichs mit Gewinnen  anderer Teilbetriebe ausgeglichen.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_68`)


Der bei der Houdek Maschinenbau  im Jahr  2007 insgesamt entstandene Verlust stehe daher nach Vornahme des innerbetrieblichen  Verlustausgleiches ausschließlich im Zusammenhang mit den übrigen bei der Houdek Maschinenbau  verbliebenen Tankstellen, sodass dieser Verlust zur Gänze zu negativen Einkünften aus  Gewerbebetrieb und damit zu vortragsfähigen Verlusten ausschließlich bei dieser Gesellschaft  führe.


Der bei der Houdek Maschinenbau  im Jahr  2007 insgesamt entstandene Verlust stehe daher nach Vornahme des innerbetrieblichen  Verlustausgleiches ausschließlich im Zusammenhang mit den übrigen bei der Houdek Maschinenbau  verbliebenen Tankstellen, sodass dieser Verlust zur Gänze zu negativen Einkünften aus  Gewerbebetrieb und damit zu vortragsfähigen Verlusten ausschließlich bei dieser Gesellschaft  führe.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_75`)


Das BFG hat der Beschwerde stattgegeben (Entscheidung vom 27.01.2016, GZ  RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des FA Wien 1/23  gegenüber der  mitbeteiligten Partei Roelfsen Versicherung (als partiellen Gesamtrechtsnachfolger der Houdek Maschinenbau)  abgeändert.

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_98`)


Im Ergebnis hat das BFG die Rechtsmeinung des Beschwerdeführers geteilt, wonach der bei der  Lexdon IT  im Jahr 2007 insgesamt entstandene Verlust nach Vornahme des  innerbetrieblichen Verlustausgleichs ausschließlich im Zusammenhang mit den übrigen bei der  Houdek Maschinenbau  verbliebenen Tankstellen verbleibt, sodass dieser Verlust zur Gänze zu  negativen Einkünften und infolge dessen zu vortragsfähigen Verlusten führt (vgl. Seite 3 der  Beschwerde vom 31.5.2013 inklusive Gutachten von Univ.-Prof. Dr. Tina Ehrke-Rabel, welches  als integrierender Bestandteil der Beschwerde 31.05.2013 anzusehen ist).

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

</details>

---

## `SUVA Abbreviation`

**F1:** 0.053 | **Precision:** 0.750 | **Recall:** 0.028  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'SUVA' as an organization.

**Content:**
```
\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.750 | 0.028 | 0.053 | 64 | 48 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 48 | 16 | 937 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_11`)


Der dagegen erhobenen Beschwerde gab das Finanzamt mit Beschwerdevorentscheidung  insoweit teilweise Folge als die Pensionskassenleistung infolge im Streitjahr nicht erfolgter Aus- zahlung außer Ansatz blieb und die von der Invalidenversicherung sowie der SUVA ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe berücksichtigt wurden.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_12`)


Die beantragte Steu- erfreiheit der von der SUVA bezogenen Invalidenrente verneinte das Finanzamt indes mit der  Begründung, dass es sich dabei nicht um dem Grunde und der Höhe nach gleichartige Beträge  aus einer ausländischen Unfallversorgung handle, die einer inländischen gesetzlichen Unfall- versorgung entspreche, weil durch die Schweizer Invalidenrente – anders als in Österreich –  nicht primär ein individueller Schaden ersetzt werde, sondern der ausgefallene Verdienst und  solche Renten somit ein steuerpflichtiges Ersatzeinkommen darstellten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_13`)


3.  Mit Vorlageantrag wurde die Entscheidung über die Beschwerde durch das Bundesfinanzge- richt beantragt, wobei zusätzlich die Anrechnung des auf den steuerpflichtigen Teil der Invali- denrente entfallenden Anteiles der von der SUVA einbehaltenen Quellensteuer (5.623,80 CHF)  geltend gemacht wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_14`)


4.  Mit gesondertem Schriftsatz brachte die steuerliche Vertretung ergänzend vor, dass beim  Beschwerdeführer von der SUVA aufgrund eines Arbeitsunfalles im Jahr 2010 eine Beeinträch- tigung der Erwerbsfähigkeit von 90 % festgestellt worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_18`)


5.  In weiterer Folge setzte das Finanzamt mit Bescheid vom 4. Juli 2017 die Vorauszahlungen  an Einkommensteuer für 2017 und Folgejahre und mit Bescheiden vom 24. November 2017 die  Einkommensteuer 2016 sowie die Vorauszahlungen an Einkommensteuer für 2018 und Folge- jahre unter Berücksichtigung der gesamten von der SUVA bezogenen Invalidenrente fest, wo- gegen sich der Beschwerdeführer mit Beschwerde und – nach Ergehen abweisender Beschwer- devorentscheidungen – mit Vorlageantrag wandte.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_19`)


6.  Mit am 11. Februar 2022 elektronisch eingereichtem Anbringen gab die steuerliche Vertre- tung unter Anschluss einer E-Mail des Steueramtes des Kantons Luzern, wonach die Schweiz  nach Art. 19 DBA-Schweiz das Recht habe, die von der SUVA (öffentlich-rechtlich) ausbezahlte  Rente zu besteuern, bekannt, dass sein Antrag auf Rückerstattung der Schweizer Quellensteuer  in der Schweiz abgewiesen worden sei.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_21`)


von der SUVA bezogenen Rente wie auch die Abzugsfähigkeit der von der Schweiz einbehal- tenen Quellensteuer und gab der Beschwerde gegen den Einkommensteuerbescheid 2015 ge- samthaft gesehen im Umfang der Beschwerdevorentscheidung (Höhe der Schweizer Invaliden- renten, Nichtberücksichtigung einer Pensionskassenleistung) teilweise Folge.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_22`)


Die einzig die  Frage der Steuerpflicht der von der SUVA ausbezahlten Invalidenrente betreffenden Beschwer- den gegen den Einkommensteuerbescheid 2016 und die Einkommensteuervorauszahlungsbe- scheide 2017 sowie 2018 und Folgejahre wurden als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_34`)


Es werde dazu auf die Verfügung der  SUVA vom 8. Jänner 2024 sowie auf die Untersuchungsberichte des Kantonsspitals St. Gallen  und weitere ärztliche Untersuchungsberichte verwiesen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_35`)


Die Unterlagen, welche großteils an  die SUVA gerichtet seien, dürften dabei auch die Grundlage für die Einschätzung der festge- stellten Invalidität darstellen.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_39`)


Angeschlossen waren der Vorhaltsbeantwortung die Rentenbescheinigung der SUVA für das  Jahr 2016, die Verfügung der SUVA vom 8. Jänner 2014 betreffend die Ausrichtung einer Inva- lidenrente und Integritätsentschädigung aufgrund der verbliebenen Beeinträchtigung aus dem  Unfall vom 27. Oktober 2010 sowie der „Unfallakt“ (Schreiben des Kantonsspitals St. Gallen  vom 9. November 2010, Bestätigung der Arbeitsunfähigkeit, diverse Berichte über durchge- führte Untersuchungen und Behandlungen).


Angeschlossen waren der Vorhaltsbeantwortung die Rentenbescheinigung der SUVA für das  Jahr 2016, die Verfügung der SUVA vom 8. Jänner 2014 betreffend die Ausrichtung einer Inva- lidenrente und Integritätsentschädigung aufgrund der verbliebenen Beeinträchtigung aus dem  Unfall vom 27. Oktober 2010 sowie der „Unfallakt“ (Schreiben des Kantonsspitals St. Gallen  vom 9. November 2010, Bestätigung der Arbeitsunfähigkeit, diverse Berichte über durchge- führte Untersuchungen und Behandlungen).

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_45`)


13.  Auf Ersuchen des Bundesfinanzgerichtes vom 2. Juli 2025, zu den Ausführungen des Fi- nanzamtes Stellung zu nehmen und die angeforderten Nachweise nachzureichen bzw. an- hand entsprechend geeigneter Unterlagen zu belegen, dass tatsächlich ein Arbeitsunfall vor- lag (Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles), übermit- telte die steuerliche Vertretung am 30. Juli 2025 ein Schreiben der SUVA betreffend die Ent- scheidungsgrundlagen für die Rentenfestsetzung, diverse Arztberichte sowie den Unfallbe- richt der Arbeitgeberin samt Schadensmeldung an die SUVA.


13.  Auf Ersuchen des Bundesfinanzgerichtes vom 2. Juli 2025, zu den Ausführungen des Fi- nanzamtes Stellung zu nehmen und die angeforderten Nachweise nachzureichen bzw. an- hand entsprechend geeigneter Unterlagen zu belegen, dass tatsächlich ein Arbeitsunfall vor- lag (Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles), übermit- telte die steuerliche Vertretung am 30. Juli 2025 ein Schreiben der SUVA betreffend die Ent- scheidungsgrundlagen für die Rentenfestsetzung, diverse Arztberichte sowie den Unfallbe- richt der Arbeitgeberin samt Schadensmeldung an die SUVA.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |
| `SUVA` | `SUVA` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_50`)


Dem- nach wurde die Minderung der Erwerbsfähigkeit im Hinblick auf die im Einzelnen angeführten  unfallkausalen Diagnosen und Verletzungsfolgen sowie die Beurteilung des Integritätsschadens  nach Gutachten der SUVA mit ärztlicher Abschlussuntersuchung am 22. Juli 2013 mit 30 % be- wertet.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_60`)


Betreffend das Jahr 2015 wurde von der SUVA Quellensteuer in Höhe von 5.623,80 CHF einbe- halten.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 16** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_64`)


Mit Erkenntnis vom 19. Dezember 2024, Ro 2023/15/0003, hob der Verwaltungsgerichtshof  das die Gleichartigkeit der von der SUVA ausbezahlten Invalidenrente und Geldleistungen aus  der gesetzlichen inländischen Unfallversorgung verneinende Erkenntnis des Bundesfinanzge- richtes vom 30. September 2022, RV/1100086/2019, wegen inhaltlicher Rechtswidrigkeit auf.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 17** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_73`)


Die Revision bringt zur Gleichartigkeit der von der SUVA ausbezahlten Schweizer Invalidenrente  Folgendes vor:   […]  Der Verwaltungsgerichtshof stimmt den Ausführungen der Revision zu, dass eine Gleichartig- keit der Leistungen iSd § 3 Abs. 1 Z 4 lit. c EStG 1988 keine völlige Identität in deren gesetzlicher  Ausgestaltung voraussetzt.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 18** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_107`)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_115`)


Das Finanzamt hat die Einkommensteuervorauszahlungen für die Jahre 2017 sowie 2018 und  Folgejahren mit Bescheiden vom 4. Juli 2017 bzw. vom 27. November 2017 gemäß § 45 Abs. 4  EStG 1988 mit 24.000,00 € (2017) bzw. 22.391,00 € (2018) festgesetzt, wobei die von der SUVA  bezogene Invalidenrente jeweils als zur Gänze steuerpflichtig berücksichtigt wurde.

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_8`)

**False Positives:**


Entscheidungsgründe  I. Verfahrensgang  1.  Mit Bescheid vom 19. Jänner 2017 setzte das Finanzamt die Einkommensteuer für das Jahr  2015 fest, wobei die in Ansatz gebrachten, aus Renten von der Eidgenössischen Invalidenver- sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (SUVA) sowie einer Pensi- onskassenleistung resultierenden Einkünfte aus nichtselbständiger Arbeit aufgrund der Nicht- vorlage der angeforderten Unterlagen im Schätzungswege ermittelt wurden.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenver- sicherung` (organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_25`)

**False Positives:**


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

FP: `SUVA` (organisation)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_27`)

**False Positives:**


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_44`)

**False Positives:**


Es könnten daher in weiterer Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die SUVA-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, steuerfrei zu belassen sei, ge- troffen werden.

FP: `SUVA` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_58`)

**False Positives:**


In den hier interessierenden Jahren be- zog er eine Invalidenrente von der Eidgenössischen Invalidenversicherung (IV) und eine unter  Anrechnung dieser Rente ermittelte Invalidenrente (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (SUVA) in Höhe von jährlich 56.236,80 CHF.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_63`)

**False Positives:**


Rechtliche Beurteilung  2.1. SUVA-Invalidenrente  Gemäß § 3 Abs. 1 Z 4 lit. c EStG 1988 sind Geldleistungen aus einer gesetzlichen Unfallversor- gung sowie dem Grunde und der Höhe nach gleichartige Beträge aus einer ausländischen ge- setzlichen Unfallversorgung, die einer inländischen gesetzlichen Unfallversorgung entspricht,  steuerbefreit.

FP: `SUVA` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_124`)

**False Positives:**


Die im Beschwerdefall strittige Frage, ob es sich bei einer infolge eines Arbeitsunfalles von der  Schweizerischen Unfallversicherungsanstalt (SUVA) ausbezahlten Invalidenrente um eine mit  einer Geldleistung aus der inländischen gesetzlichen Unfallversorgung gleichartige ausländi- sche Leistung im Sinne des § 3 Abs. 1 Z 4 lit. c EStG 1988 handelt, ist durch das Erkenntnis des  Verwaltungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, geklärt.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_8`)

**False Positives:**


Entscheidungsgründe  I. Verfahrensgang  1.  Mit Bescheid vom 19. Jänner 2017 setzte das Finanzamt die Einkommensteuer für das Jahr  2015 fest, wobei die in Ansatz gebrachten, aus Renten von der Eidgenössischen Invalidenver- sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (SUVA) sowie einer Pensi- onskassenleistung resultierenden Einkünfte aus nichtselbständiger Arbeit aufgrund der Nicht- vorlage der angeforderten Unterlagen im Schätzungswege ermittelt wurden.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenver- sicherung` (organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_25`)

**False Positives:**


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

FP: `SUVA` (organisation)


10.  Daraufhin ersuchte das Finanzamt die steuerliche Vertretung mit Schreiben vom 22. April  2025, zwecks Feststellung des steuerfreien Anteiles der SUVA-Rente   um Darstellung der örtlichen, zeitlichen und ursächlichen Umstände des Unfalles, aufgrund  dessen die SUVA-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der SUVA) und des Zusammenhanges mit der Beschäftigung;

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_27`)

**False Positives:**


 die Unterlagen der SUVA zur Einschätzung des Grades der Behinderung (zB SUVA-Gutach- ten) und die zugrundeliegenden medizinischen Befunde und Atteste vorzulegen;

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_44`)

**False Positives:**


Es könnten daher in weiterer Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die SUVA-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes vom 19. Dezember 2024, Ro 2023/15/0003, steuerfrei zu belassen sei, ge- troffen werden.

FP: `SUVA` (organisation)

**✅ Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_58`)

**False Positives:**


In den hier interessierenden Jahren be- zog er eine Invalidenrente von der Eidgenössischen Invalidenversicherung (IV) und eine unter  Anrechnung dieser Rente ermittelte Invalidenrente (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (SUVA) in Höhe von jährlich 56.236,80 CHF.

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_63`)

**False Positives:**


Rechtliche Beurteilung  2.1. SUVA-Invalidenrente  Gemäß § 3 Abs. 1 Z 4 lit. c EStG 1988 sind Geldleistungen aus einer gesetzlichen Unfallversor- gung sowie dem Grunde und der Höhe nach gleichartige Beträge aus einer ausländischen ge- setzlichen Unfallversorgung, die einer inländischen gesetzlichen Unfallversorgung entspricht,  steuerbefreit.

FP: `SUVA` (organisation)

**✅ Gold Entities:**

</details>

---

## `University Full Names JKU WU`

**F1:** 0.047 | **Precision:** 0.840 | **Recall:** 0.024  

**Format:** `regex`  
**Description:**
Matches the full names of Johannes Kepler Universität Linz and Wirtschaftsuniversität Wien, including variations with 'Linz' or 'Wien' appended.

**Content:**
```
\b(?:Johannes\s+Kepler\s+Universität\s+Linz(?:\s*\(JKU\))?|Wirtschaftsuniversität\s+Wien(?:\s*\(WU\))?|JKU\s+Linz|WU\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.840 | 0.024 | 0.047 | 50 | 42 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 42 | 8 | 1633 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_6`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_47`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_74`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht (UJ033 500) inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_135`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_6`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_47`)


Im Wintersemester 2018/2019 war sie an der Wirtschaftsuniversität Wien inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_74`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht (UJ033 500) inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_135`)


Vom Wintersemester 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  Wirtschaftsuniversität Wien in der Studienrichtung Wirtschaftsrecht inskribiert.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |
| `Johannes Kepler Universität Linz` | `Johannes Kepler Universität Linz` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_11`)


 Abgangsbescheinigung der WU Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- und Sozialwissenschaften, aus welcher unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten sowie der Abschluss der Studieneingangs- und  Orientierungsphase mit 07.03.2018 hervorgeht:    [...]

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |
| `JKU Linz` | `JKU Linz` |
| `WU Wien` | `WU Wien` |

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_14`)


 Abgangsbescheinigung der JKU Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften (Studienplan 2018W)

| Predicted | Gold |
|---|---|
| `JKU Linz` | `JKU Linz` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_25`)


5. Die belangte Behörde ersuchte mit Schreiben vom 02.12.2021 die Bf. um die in der  Beschwerde angekündigte Nachreichung der Unterlagen der WU Wien (Vergleich der  Studienrichtungen).

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

| Predicted | Gold |
|---|---|
| `WU  Wien` | `WU  Wien` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_29`)


Die von der belangten Behörde angeforderten Angaben der WU Wien wurden mit diesem  Schreiben jedoch nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_33`)


An der WU Wien wurde das Studium  Wirtschafts- und Sozialwissenschaften (Bachelor) betrieben, in Linz handelte es sich um das  Studium Wirtschaftswissenschaften (Bachelor).

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

| Predicted | Gold |
|---|---|
| `Johannes Kepler Universität Linz` | `Johannes Kepler Universität Linz` |

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |
| `JKU Linz` | `JKU Linz` |

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

| Predicted | Gold |
|---|---|
| `Johannes Kepler  Universität Linz` | `Johannes Kepler  Universität Linz` |
| `WU  Wien` | `WU  Wien` |

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

| Predicted | Gold |
|---|---|
| `WU Wien` | `WU Wien` |
| `JKU Linz` | `JKU Linz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)

**False Positives:**


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

FP: `Wirtschaftsuniversität Wien` (organisation)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

FP: `WU Wien` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)

**False Positives:**


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `Johannes Kepler Universität Linz` (organisation)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `JKU Linz` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)

**False Positives:**


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

FP: `Johannes Kepler Universität Linz` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)

**False Positives:**


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

FP: `Wirtschaftsuniversität Wien` (organisation)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

FP: `Johannes Kepler Universität Linz` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_98`)

**False Positives:**


Die belangte Behörde bringt vor, dass von den abgelegten 42 ECTS an der WU Wien lediglich  24 ECTS an der JKU Linz angerechnet wurden.

FP: `JKU Linz` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

</details>

---

## `ÖGK Abbreviation`

**F1:** 0.045 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.045 | 40 | 40 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 0 | 1700 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_28`)


Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_74`)


Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149808.1_214`)


Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_13`)


Herr F (und auch wir als seine steuerliche Vertretung) hätten auch gar nicht damit gerechnet,  dass diese Bescheide Herrn F persönlich zugestellt würden, da die ÖGK die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, sehr wohl der F Personalservice GmbH (als  Rechtsnachfolgerin des Einzelunternehmens) direkt vorgeschrieben habe.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_28`)


Wären die oben  angeführten Abgaben - entsprechend dem Vorgehen der ÖGK - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ebenfalls mit einer Quote von 25%bedient  worden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_74`)


Betreffend der SV- Abgaben, die im Zuge derselben GPLB angefallen seien,  seien diese seitens der ÖGK der GmbH vorgeschrieben worden, sodass Herr F nicht damit  rechnen habe können, dass die Vorschreibung der Abgaben L, DB und DZ 2016 an ihn  persönlich erfolgen würde.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149808.1`) ( sent_id: `findok-manually-annotated_TRAIN/149808.1_214`)


Weiters wurde nochmals  erklärt, dass die Grundlagenbescheide über Finanz-Online in die Databox des EU gerichtet  wurden, die Bescheide der ÖGK allerdings an die GmbH übermittelt wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_22`)


Der Kostenersatz der ÖGK sei auf der Rechnung ersichtlich,  weitere Ersatzleistungen habe es nicht gegeben.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_3`)


Entscheidungsgründe  I. Verfahrensgang  Strittig ist in der vorliegenden Beschwerdesache, ob zu Recht Einkünfte in Höhe von EUR  620,43 von der Österreichischen Gesundheitskasse (im Folgenden: ÖGK) im  Einkommensteuerbescheid 2023 des Beschwerdeführers (im Folgenden: Bf.) berücksichtigt  wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_6`)


Darin  wurden auch Einkünfte von der ÖGK in Höhe von EUR 620,43 berücksichtigt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_15`)


Im Jahr 2023 erhielt der Bf. von der ÖGK eine Erstattung von insgesamt EUR 723,84 an  Beiträgen zur Sozialversicherung (davon entfielen auf die Krankenversicherung EUR 163,53, auf  die Arbeitslosenversicherung EUR 126,77 und auf die Pensionsversicherung EUR 433,54).

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_16`)


Diese  Erstattung hatte ihre Wurzel im Jahr 2022, da in diesem Jahr Beiträge über die  Höchstbeitragsgrundlage hinaus an die ÖGK entrichtet wurden.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_17`)


In einem Schreiben der ÖGK  vom 12.5.2023 wurde der Bf. über die Rückerstattung der Beiträge informiert und darauf  aufmerksam gemacht, dass die rückerstatteten Sozialversicherungsbeiträge steuerpflichtig  sind.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_18`)


Am 20.2.2024 wurde dem Finanzamt von der ÖGK ein Lohnzettel für den Bf. und das Jahr 2023  übermittelt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_20`)


Im Einkommensteuerbescheid 2023 des Bf. kamen bei den Einkünften aus nichtselbständiger  Arbeit auch die von der ÖGK rückerstatteten Sozialversicherungsbeiträge in Höhe von EUR  620,43 zum Ansatz.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_23`)


Darüber hinaus enthält das  Schreiben der ÖGK vom 12.5.2023 eine Aufstellung der für die Berechnung relevanten  Versicherungsverhältnisse 2022 und ergibt sich die Sachverhaltsfeststellung auch daraus.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_27`)


Die Feststellung, wonach der Bf. im Jahr 2023 von der ÖGK eine Erstattung von EUR 723,84  erhielt und sich diese auf das Jahr 2022 bezog, weil in diesem Jahr zu hohe Beiträge geleistet  wurden (nämlich über die Höchstbeitragsgrundlage hinaus), ergibt sich aus dem im Sachverhalt  angeführten Schreiben der ÖGK an den Bf. vom 12.5.2023.


Die Feststellung, wonach der Bf. im Jahr 2023 von der ÖGK eine Erstattung von EUR 723,84  erhielt und sich diese auf das Jahr 2022 bezog, weil in diesem Jahr zu hohe Beiträge geleistet  wurden (nämlich über die Höchstbeitragsgrundlage hinaus), ergibt sich aus dem im Sachverhalt  angeführten Schreiben der ÖGK an den Bf. vom 12.5.2023.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |
| `ÖGK` | `ÖGK` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_32`)


Dieses Schreiben der ÖGK über die Erstattung von Beiträgen in Höhe von EUR 723,84 ist im  finanzbehördlichen Abgabeninformationssystem (JVP) hinterlegt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146878.1_35`)


Aufgrund dieses Schreibens der ÖGK an den Bf. ist für das Bundesfinanzgericht die Grundlage  für den im Jahr 2024 übermittelten Lohnzettel an das Finanzamt (auch dieser ist in der JVP  ersichtlich) und die Berücksichtigung des Betrages von EUR 620,43 im  Einkommensteuerbescheid 2023 des Bf. geklärt.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `Magistrat der Stadt Wien with Suffixes`

**F1:** 0.045 | **Precision:** 0.952 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien' and 'Magistrates der Stadt Wien' with optional suffixes like ', MA 67' or ', Magistratsabteilung 67'.

**Content:**
```
\b(Magistrat|Magistrates)\s+der\s+Stadt\s+Wien(?:\s*,\s*(?:MA\s*\d+|Magistratsabteilung\s*\d+))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.952 | 0.023 | 0.045 | 42 | 40 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 40 | 2 | 1567 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 6` | `Magistrates der Stadt Wien, Magistratsabteilung 6` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag.Dr. Wolfgang Pagitsch in der  Verwaltungsstrafsache gegen Brunhild Katschmareck, Oberwinden 3, 4553 Hausmanning, Österreich, über dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des Magistrates der Stadt Wien, Magistratsabteilung 6,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 des Gebrauchsabgabegesetzes (GAG) vom  8.7.1966, LGBl. für Wien Nr. 20, idF der Kundmachung ABl. der Stadt Wien Nr. 52/2016 zu  Recht erkannt:  I.)

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 6` | `Magistrates der Stadt Wien, Magistratsabteilung 6` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Diego Strzeletzki, Zwerggasse 116, 8961 Steg, Österreich, vom 1. Oktober 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 18. September  2025, GZ. MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Diego Strzeletzki, Zwerggasse 116, 8961 Steg, Österreich, vom 1. Oktober 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 18. September  2025, GZ. MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_8`)


Der Magistrat der Stadt Wien, Magistratsabteilung 67, forderte die Firma Firma, AdrFirma, als  Zulassungsbesitzerin des in Rede stehenden Fahrzeuges mit Schreiben vom 17. Juni 2025, GZ.  MA67/GZ/2025, zur Lenkerauskunft gemäß § 2 Wiener Parkometergesetz 2006 binnen einer  Frist von zwei Wochen ab Zustellung des Schreibens auf (Lenkererhebung).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_27`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  18. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 75,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 17 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_117`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_4`)


Begründung  Verfahrensgang:  Das Bundesfinanzgericht hat mit Erkenntnis vom 17. Juni 2025, GZ. RV/GZ2/2025, die  Beschwerde des Beschwerdeführers (Bf.) vom 6. Mai 2025 gegen das Straferkenntnis des  Magistrates der Stadt Wien vom 3. April 2025, GZ. MA67/GZ1/2024, gemäß § 50  Verwaltungsgerichtsverfahrensgesetz (VwGVG) iVm § 24 Abs. 1 Bundesfinanzgerichtsgesetz  (BFGG) und § 5 Gesetz über das Wiener Abgabenorganisationsrecht (WAOR) als unbegründet  abgewiesen und das angefochtene Straferkenntnis bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Verwaltungsstrafsache gegen Emanuela Deider, Astätt 60, 4682 Wilding, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des  Beschuldigten vom 26. September 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 29. August 2025, Zahl: MA67/MA-GZ/2025 zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Karoline Windsteig in der  Verwaltungsstrafsache gegen Emanuela Deider, Astätt 60, 4682 Wilding, Österreich, wegen der Verwaltungsübertretung  gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005, idF  ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006,  LGBl. für Wien Nr. 9/2006, idF LGBl. für Wien Nr. 71/2018, über die Beschwerde des  Beschuldigten vom 26. September 2025 gegen das Straferkenntnis des Magistrates der Stadt  Wien, Magistratsabteilung 67 vom 29. August 2025, Zahl: MA67/MA-GZ/2025 zu Recht  erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt  Wien, Magistratsabteilung 67` | `Magistrates der Stadt  Wien, Magistratsabteilung 67` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_13`)


In der Folge lastete der Magistrat der Stadt Wien, MA 67, nach durchgeführter Lenkererhebung  (Erteilung der Lenkerauskunft durch Zulassungsbesitzerin per E-Mail am 10. Juli 2025) mit  Strafverfügung vom 11. Juli 2025, zugestellt am 17. Juli 2025, GZ MA67/MA-GZ/2025, dem  Beschwerdeführer (kurz Bf.) an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen  Kennzeichen W-Kennz. (A) am 07. Mai 2025 um 11:59 Uhr in der gebührenpflichtigen  Kurzparkzone in 1050 Wien, Bacherplatz gegenüber 14, abgestellt, ohne für seine  Kennzeichnung mit einem für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu  haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_15`)


Wegen Verletzung des § 5 Abs. 2 Wiener Parkometerabgabeverordnung iVm § 4 Abs. 1 Wiener  Parkometergesetz 2006 verhängte der Magistrat der Stadt Wien über den Bf. eine Geldstrafe in  Höhe € 75,00 (Ersatzfreiheitsstrafe 17 Stunden).

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 13** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_30`)


Die vom Magistrat der Stadt Wien verhängte Geldstrafe sei im Hinblick auf die  Strafzumessungsgründe und den bis zu € 365,00 reichenden Strafsatz, den Unrechtsgehalt der  Tat und das Verschulden, selbst bei ungünstigen wirtschaftlichen Verhältnissen, durchaus  angemessen und keineswegs zu hoch.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 14** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_35`)


Über die Beschwerde wurde erwogen:  Der Bf. hat in seiner Beschwerde gegen das Straferkenntnis des Magistrates der Stadt Wien  vom 29. August 2025, Zahl: MA67/MA-GZ/2025, lediglich die Höhe der verhängten Geldstrafe  bekämpft und die angelastete Verwaltungsübertretung nicht in Abrede gestellt, sodass der  Schuldspruch des Straferkenntnisses in Rechtskraft erwachsen ist.

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 15** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_110`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1_1`)


BESCHLUSS  Das Bundesfinanzgericht fasst durch den Richter Priv.-Doz. Felix Grenzheuser  über die Beschwerde des PhD Ing. Theobald Reuschel,  Schloss Straße 184, 3371 Köchling, Österreich  vom 24. April 2025 gegen die Vollstreckungsverfügung des Magistrates der  Stadt Wien, Magistratsabteilung 6, vom 31. März 2025, Zahl: MA67/GZ/2024 in  Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl.

| Predicted | Gold |
|---|---|
| `Magistrates der  Stadt Wien, Magistratsabteilung 6` | `Magistrates der  Stadt Wien, Magistratsabteilung 6` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1_5`)


I. Verfahrensgang  Mit Strafverfügung vom 03. Jänner 2025, zugestellt am 14. Februar 2025, GZ. MA67/GZ/2024  lastete der Magistrat der Stadt Wien, Magistratsabteilung 67, dem Beschwerdeführer (kurz Bf.)  an, er habe das mehrspurige Kraftfahrzeug mit dem behördlichen Kennzeichen GU-405 NY  (A) am 06. November 2024 um 12:21 Uhr in der gebührenpflichtigen Kurzparkzone in 1020  Wien, Rustenschacherallee vor Baum 1009 abgestellt, ohne für seine Kennzeichnung mit einem  für den Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1_26`)


Mit Zurückweisungsbescheid vom 23. Juni 2025, zugestellt am 30. Juni 2025 wies der Magistrat  der Stadt Wien, MA 67, den Antrag auf Wiedereinsetzung in den vorigen Stand und den  Einspruch gegen die Strafverfügung vom 03. Jänner 2025 zurück.

| Predicted | Gold |
|---|---|
| `Magistrat  der Stadt Wien, MA 67` | `Magistrat  der Stadt Wien, MA 67` |

**Example 19** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) ( sent_id: `findok-manually-annotated_TRAIN/148818.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Irene Kohler über die Beschwerde  des Jean Broderius, Weinwartshof 30, 8151 Södingberg, Österreich, vom 12. Juni 2025, gegen das Straferkenntnis der belangten  Behörde Magistrat der Stadt Wien, MA 67, als Abgabenstrafbehörde, vom 2. Juni 2025, GZ.  MA67/GZ/2025, wegen der Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener  Parkometerabgabeverordnung, ABl. der Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr.  20/2020, in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz 2006, LGBl. für Wien Nr.  9/2006 idF LGBl. für Wien Nr. 71/2018, zu Recht:     I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated_TRAIN/149661.1_1`)

**False Positives:**


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

FP: `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149661.1_1`)

**False Positives:**


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Mag. Renate Schohaj über die Beschwerde des  Martina Hennefahrt, Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich, vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang mit einer Verwaltungsübertretung gemäß § 5 Abs. 2  Wiener Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener Parkometergesetz  2006, den Beschluss gefasst:  Die Beschwerde vom 2. Oktober 2025 wird gemäß §§ 28 Abs. 1 und 31 VwGVG als verspätet  zurückgewiesen.

FP: `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)

**✅ Gold Entities:**
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

</details>

---

## `Roelfsen Versicherung`

**F1:** 0.036 | **Precision:** 1.000 | **Recall:** 0.018  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Roelfsen Versicherung'.

**Content:**
```
\bRoelfsen\s+Versicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.018 | 0.036 | 32 | 32 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 32 | 0 | 1515 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_7`)


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_10`)


Mit Bescheid vom 29. Jänner 2019 wurde ein Bescheid über die Wiederaufnahme des  Verfahrens betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (Roelfsen Versicherung  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_11`)


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_24`)


zweiten Umgründungsschritt ist auf Grundlage des Generalversammlungsbeschlusses vom  19.08.2009 eine Abspaltung zur Aufnahme in die Roelfsen Versicherung  durch Übertragung des  gesamten Betriebes (mit Ausnahme der unter Punkt Drittens 10.4 des Spaltungs- und  Übernahmsvertrages taxativ angeführten Positionen) erfolgt.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_25`)


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_32`)


Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und  verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007  ausschließlich an die Roelfsen Versicherung.


Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und  verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007  ausschließlich an die Roelfsen Versicherung.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_45`)


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_59`)


Ergebnis  Roelfsen Versicherung  -2.966.376,17       Gegen den Körperschaftsteuerbescheid 2007 wurde von der mitbeteiligten Partei  Roelfsen Versicherung (als partieller Gesamtrechtsnachfolger der Houdek Maschinenbau) mit Schreiben vom  31.05.2013 Beschwerde erhoben.


Ergebnis  Roelfsen Versicherung  -2.966.376,17       Gegen den Körperschaftsteuerbescheid 2007 wurde von der mitbeteiligten Partei  Roelfsen Versicherung (als partieller Gesamtrechtsnachfolger der Houdek Maschinenbau) mit Schreiben vom  31.05.2013 Beschwerde erhoben.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_75`)


Das BFG hat der Beschwerde stattgegeben (Entscheidung vom 27.01.2016, GZ  RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des FA Wien 1/23  gegenüber der  mitbeteiligten Partei Roelfsen Versicherung (als partiellen Gesamtrechtsnachfolger der Houdek Maschinenbau)  abgeändert.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_127`)


b) Sachverhalt und Verfahrensablauf beim gegenständlichen (partiellen) Rechtsnachfolger  Roelfsen Versicherung, Str.Nr.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_128`)


85-900/3590, BV 24 :  Beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  gab es betreffend dem  Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid  Gruppenmitglied:  21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010  27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010 nach Betriebsprüfung   27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010  20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010  (Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung  Rekultivierungskosten)  19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)  29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)  16.12.2013 Vorlage an BFG (damals noch UFS)  17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  Betreffend des Rechtsvorgängers Houdek Maschinenbau  wurde das Erkenntnis des  Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum  Veranlagungsjahr 2007 erlassen.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_129`)


Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim  Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Wien 1/23  am 07.03.2016 das  Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO  wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da  11 von 39 Seite 12 von 39

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_132`)


Rechtsansicht  des BFG und der Beschwerdeführerin - nach Vornahme des nach freiem Wahlrecht ausgeübten  innerbetrieblichen Verlustausgleiches ausschließlich im Zusammenhang mit den übrigen bei  der Houdek Maschinenbau  verbliebenen Tankstellen, sodass dieser Verlust zur Gänze zu negativen  Einkünften aus Gewerbebetrieb (und damit zwingend ausschließlich zu vortragsfähigen  Verlusten) bei der Roelfsen Versicherung  führt.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_135`)


Begründend  wurde deshalb durch das Finanzamt Wien 1/23  im Sachbescheid Feststellungsbescheid Gruppenmitglied  2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ  RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Roelfsen Versicherung  als RNF der  Houdek Maschinenbau  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR  1.047.673,40 ergibt.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_140`)


Insgesamt ergaben sich daher bis dato (inklusive dem letzten Wiederaufnahmebescheid  vom07.03.2016) beim gegenständlichen Rechtsnachfolger Roelfsen Versicherung  für das Jahr 2010  folgende Veranlagungsschritte:  21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010  27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010 nach Betriebsprüfung   27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010  20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010  (Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung  Rekultivierungskosten)  12 von 39 Seite 13 von 39

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_142`)


Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der  Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des  Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann,  wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum  Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.


Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der  Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des  Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann,  wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum  Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_190`)


Das BFG hat in seiner Entscheidung vom 27.01.2016, GZ RV/5101064/2013 für das Jahr 2007  das freie Wahlrecht bejaht und deshalb in weiterer Folge eine Verlustzuordnung wie folgt  festgestellt: (Anm.: es folgt eine graphische, zahlenmäßige Darstellung)  Aus der o.a. graphischen Darstellung der BFG-Entscheidung ergibt sich, dass auf Grund des  bejahten Wahlrechtes der gesamte Verlust auch bei der Roelfsen Versicherung  vortragsfähig ist, da  keine Verluste für die abgespaltenen Tankstellen verbleiben, da vorrangig die Gewinne mit den  Verlusten aus abgespaltenen Tankstellen ausgeglichen wurden.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_193`)


Nach der nunmehr  bindenden Rechtsansicht des VwGH steht der Roelfsen Versicherung  kein (zusätzlicher) Verlustvortrag  von EUR 665.812,12 zu.

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

</details>

---

## `FA Wien 1/23 Specific`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'FA Wien 1/23' specifically to ensure it is captured correctly.

**Content:**
```
\bFA\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1500 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_27`)


Im Wirtschaftsjahr 2007 ist gemäß der beim FA Wien 1/23  eingereichten  Körperschaftsteuererklärung 2007 ein steuerlicher Verlust von € -4.239.321,85 aus den 84  Tankstellen erzielt worden.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)


Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_75`)


Das BFG hat der Beschwerde stattgegeben (Entscheidung vom 27.01.2016, GZ  RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des FA Wien 1/23  gegenüber der  mitbeteiligten Partei Roelfsen Versicherung (als partiellen Gesamtrechtsnachfolger der Houdek Maschinenbau)  abgeändert.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_100`)


Das Erkenntnis des Bundesfinanzgerichts, Außenstelle Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des FA Wien 1/23  in vollem Umfang im Zuge einer Amtsrevision  angefochten.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_129`)


Als Folge dieser stattgebenden BFG-Entscheidung vom 27.01.2016, GZ RV/5101064/2013 beim  Rechtsvorgänger für das Jahr 2007, wurde seitens des FA Wien 1/23  am 07.03.2016 das  Veranlagungsjahr 2010 beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  hinsichtlich Feststellungsbescheid Gruppenmitglied gem. § 303 Abs. 1 lit b BAO  wiederaufgenommen und ein zusätzlicher Verlustvortrag von EUR 665.812,12 gewährt, da  11 von 39 Seite 12 von 39

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_142`)


Da sowohl der Roelfsen Versicherung  als auch dem FA Wien 1/23  bewusst war, dass der Ausgang der  Amtsrevision bei der Houdek Maschinenbau  für das Jahr 2007 Bedeutung für die endgültige Höhe des  Verlustvortrages bei der partiellen Rechtsnachfolgerin Roelfsen Versicherung  im Jahr 2010 haben kann,  wurde mit dem steuerlichen Vertreter vereinbart, Unterbrechungshandlungen bis zum  Ausgang der Amtsrevision für das Veranlagungsjahr 2010 zu setzen.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_204`)


Damit hat das FA Wien 1/23  in seinem Bescheid vom 07.03.2016 die Vorfrage gemäß der  Rechtsanschauung in der BFG-Entscheidung beurteilt.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_205`)


(Das FA Wien 1/23  war zu diesem Zeitpunkt  gern.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_251`)


Diesen  Ausführungen des Finanzamtes ist aus folgenden Gründen entgegenzutreten:   2.1 Nichtvorliegen einer Vorfrage im Sinne des § 303 Abs 1 lit c BAO iVm § 116 BAO   Es liegt schon keine Vorfrage iSd § 116 BAO vor, da das FA Wien 1/23  für die hier  entscheidungserheblichen Fragestellungen sachlich zuständige Behörde ist.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_261`)


2.2 Unzulässige Vermengung der Begründungselemente der VwGH-Entscheidung durch das  FA Wien 1/23  In ihren Ausführungen hinsichtlich der Begründung der Wiederaufnahme nimmt das Finanzamt  immer wieder auf die Entscheidung des Verwaltungsgerichtshofes im Beschwerdeverfahren  22 von 39 Seite 23 von 39

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_267`)


Die vom FA Wien 1/23  in weiterer Folge zitierten Ausführungen (Rz 30 VwGH-Entscheidung)  betreffen Ausführungen des VwGH zu - nicht verfahrensgegenständlichen - Folgejahren.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_281`)


Schon aus diesem  Grund kann sich das FA Wien 1/23  für die gegenständliche Wiederaufnahme nicht auf eine  Entscheidung des VwGH, in welcher nur über die Höhe des Verlustes abgesprochen worden ist,  stützen.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_332`)


In verfassungskonformer Interpretation  liegt lt.   Ansicht des FA Wien 1/23  eine Vorfrage gem. § 303 Abs. 1 lit c. BAO vor.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_346`)


Sowohl  die Großbetriebsprüfung, das FA Wien 1/23, die nunmehrige Beschwerdeführerin (die im Übrigen  selbst lediglich für das Jahr 2007 das freie Wahlrecht und die Verlustzuteilung geklärt haben  wollte und daher für das Jahr 2010 "nur" die Streitfrage der Angemessenheit der PKW- Aufwendungen im Verfahren RV/5100056/2014 vor dem BFG vorbrachte) und natürlich auch  der BFG-Richter gingen übereinstimmend in der Vergangenheit davon aus, dass die Streitfrage,   ob ein freies Wahlrecht iZm dem innerbetrieblichen Verlustausgleich vorliegt oder nicht, eine  Streitfrage des Jahres 2007 ist.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_353`)


Das Erkenntnis des BFG wurde zwar  sofort durch das FA Wien 1/23  mittels Amtsrevision bekämpft, war jedoch jedenfalls gem. § 282  BAO durch das Finanzamt umzusetzen.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_372`)


Im Übrigen entspricht dieser Verlustvortrag wieder jenem Betrag, wie er vor der erfolgten  Anpassung an das Erkenntnis des BFG, seitens des FA Wien 1/23  im Rahmen der BVE vom  19.11.2013 festgesetzt worden ist und wogegen - wie bereits erwähnt weder in der  Beschwerde noch im Vorlageantrag - die Rechtsunrichtigkeit eingewandt wurde.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_388`)


Aus diesem Grunde wurden auch seitens des FA Wien 1/23  in weiterer Folge im Jahr  2017 und 2018 Unterbrechungshandlungen für das Jahr 2010 gesetzt, um die  Rechtsproblematik der Verjährung für das Jahr 2010 hintanzuhalten.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_408`)


Somit war es  dem FA Wien 1/23  im Jahr 2016 verwehrt - ungeachtet der eingebrachten Amtsrevision -, den  33 von 39 Seite 34 von 39

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_410`)


Antrag des Finanzamtes:   Das FA Wien 1/23  hält seine Rechtsmeinung weiterhin aufrecht, dass ein Anwendungsfall des §  303 Abs. 1 lit c BAO in verfassungskonformer Interpretation vorliegt.

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

</details>

---

## `KQPC Versand GMBH Specific`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches the specific company 'KQPC Versand GMBH'.

**Content:**
```
\bKQPC\s+Versand\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1583 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_10`)


Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_11`)


In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_18`)


Mit Straferkenntnis vom 28.12.2020, GZ: MA6/196000000656/2019, wurde der Beschuldigte  als handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  wegen 22  Verwaltungsübertretungen nach § 1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG  verurteilt, da er bis zum 22.8.2018 Gebrauchsabgaben für die Monate Juni 2017 bis Jänner  2018 im Zusammenhang mit der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_68`)


Damit entfällt auch die  Haftung der KQPC Versand GMBH  gem. § 9 Abs. 7 VStG.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_7`)


Entscheidungsgründe  I. Bisheriger Verfahrensgang  Mit Straferkenntnis des Magistrats der Stadt Wien, Magistratsabteilung 6, vom 28.12.2020, GZ:  MA6/196000000656/2019, wurde Brunhild Katschmareck  hinsichtlich 22 Verwaltungs-übertretungen nach §  1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG für schuldig befunden, da er als  handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, auf dem  öffentlichen Gemeindegrund, der dem öffentlichen Verkehr dient, ein Gerüst im Ausmaß von  19 m², eine Baustofflagerung im Ausmaß von 12 m² (im Juni und Juli 2017 von 23 m²) und eine  Mobil-Toilette im Ausmaß von 1 m² aufgestellt habe, wobei er hiefür bis zum 22.8.2018 weder  eine Gebrauchsabgabe erwirkt, noch die Gebrauchsabgabe entrichtet habe und dadurch die  Gebrauchsabgaben für die Monate Juni 2017 bis Jänner 2018 verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_10`)


Zudem  wurde im Straferkenntnis ausgesprochen, dass die KQPC Versand GMBH  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die Verfahrenskosten zur ungeteilten Hand hafte.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_11`)


In der am 14.1.2021 vom Beschuldigten dagegen eingebrachten Beschwerde bringt dieser im  Wesentlichen vor, dass für Juni bis Dezember 2017 bereits Verjährung eingetreten und die  KQPC Versand GMBH  im Jänner 2018 nicht mehr tätig gewesen sei.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_18`)


Mit Straferkenntnis vom 28.12.2020, GZ: MA6/196000000656/2019, wurde der Beschuldigte  als handelsrechtlicher Geschäftsführer der KQPC Versand GMBH  wegen 22  Verwaltungsübertretungen nach § 1 Abs 1 iVm § 16 Abs 1 und Tarifpost D 1 und D 4 GAG  verurteilt, da er bis zum 22.8.2018 Gebrauchsabgaben für die Monate Juni 2017 bis Jänner  2018 im Zusammenhang mit der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  verkürzt habe.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_68`)


Damit entfällt auch die  Haftung der KQPC Versand GMBH  gem. § 9 Abs. 7 VStG.

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

</details>

---

## `Event Sudkraftlex GMBH Specific`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches the specific company 'Event Sudkraftlex GMBH'.

**Content:**
```
\bEvent\s+Sudkraftlex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.023 | 20 | 20 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 20 | 0 | 1579 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_20`)


Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_25`)


Zunächst wurde mit Bescheiddatum 16.1.2018 ein Nachbemessungsbescheid an die Event Sudkraftlex GMBH  erlassen und die oa. streitgegenständlichen Gebrauchsabgaben vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_58`)


Da die in der bekämpften Strafentscheidung angeführten Gebrauchsabgaben mit Erlassung des  Abgabenbescheides vom 16.1.2018 an die Event Sudkraftlex GMBH  Mitte/Ende Jänner 2018 erstmals  bescheidmäßig festgesetzt wurden, sind die jeweiligen strafbaren Taten spätestens Ende  Jänner 2018 abgeschlossen worden bzw. hat das strafbare Verhalten aufgehört.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_12`)


Im Zuge eines umfangreichen Vorhalteverfahrens übermittelte die belangte Behörde auch  einen abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die Event Sudkraftlex GMBH  hinsichtlich der oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_13`)


Gebrauchsabgabenverkürzungen und teilte mit, dass auf Basis dieses  Bescheides gegen den Beschuldigten als Geschäftsführer der Event Sudkraftlex GMBH  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung rechtskräftig geworden sei.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_16`)


Der Beschuldigte war im inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der Event Sudkraftlex GMBH.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_17`)


Die KQPC Versand GMBH  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten an der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die Event Sudkraftlex GMBH  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma (Nutzer).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_20`)


Weiters wurde der Beschuldigte bereits mit Strafverfügung vom 19.4.2018, GZ: MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der Event Sudkraftlex GMBH  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, Österreich  rechtskräftig verurteilt, da er bis zum 16.1.2018 oa.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_22`)


Die beiden Strafentscheidungen sind nahezu ident und unterscheiden sich im  Wesentlichen nur hinsichtlich der Funktion des Beschuldigten (Geschäftsführer Event Sudkraftlex GMBH  bzw. Geschäftsführer KQPC Versand GMBH) und des Zeitpunktes hinsichtlich der Beendigung der  Verwaltungsübertretungen (22.8.2018 bzw. 16.1.2018).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_25`)


Zunächst wurde mit Bescheiddatum 16.1.2018 ein Nachbemessungsbescheid an die Event Sudkraftlex GMBH  erlassen und die oa. streitgegenständlichen Gebrauchsabgaben vorgeschrieben.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_58`)


Da die in der bekämpften Strafentscheidung angeführten Gebrauchsabgaben mit Erlassung des  Abgabenbescheides vom 16.1.2018 an die Event Sudkraftlex GMBH  Mitte/Ende Jänner 2018 erstmals  bescheidmäßig festgesetzt wurden, sind die jeweiligen strafbaren Taten spätestens Ende  Jänner 2018 abgeschlossen worden bzw. hat das strafbare Verhalten aufgehört.

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_69`)


Da das Verfahren schon aus diesem Grund einzustellen war, erübrigt es sich auch auf die Frage  einer möglichen Doppelbestrafung (Bestrafung als Vertretungsbefugter gem § 9 Abs 2 VStG der  Event Sudkraftlex GMBH  und der KQPC Versand GMBH) einzugehen (vgl. dazu VwGH 6.3.1997, 95/09/0342).

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

</details>

---

## `Finanzamt Wien 1/23 Specific`

**F1:** 0.022 | **Precision:** 1.000 | **Recall:** 0.011  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Wien 1/23' specifically to ensure it is captured correctly.

**Content:**
```
\bFinanzamt\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.011 | 0.022 | 19 | 19 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 19 | 0 | 1524 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_3`)


über die Beschwerden vom 29. März 2019 gegen den Bescheid des Finanzamt Wien 1/23  vom 29. Jänner  2019 betreffend Wiederaufnahme § 303 BAO /  KSt 2010 Steuernummer 85-900/3590  zu  Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_102`)


Unmittelbar nachfolgend hat das BFG die Amtsrevision des Finanzamt Wien 1/23 (samt Veranlagungsakten  sowie Auszügen aus dem Arbeitsbogen der Betriebsprüfung) dem VwGH unter der Zahl Ro  2016/15/0010 zur Entscheidung vorgelegt.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_111`)


Mittels VwGH-Entscheidung vom 13.09.2018 zu Ro 2016/15/0010 hat der VwGH die  Amtsrevision des Finanzamt Wien 1/23  als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_135`)


Begründend  wurde deshalb durch das Finanzamt Wien 1/23  im Sachbescheid Feststellungsbescheid Gruppenmitglied  2010 vom 07.03.2016 daher ausgeführt, dass gemäß der BFG-Entscheidung GZ  RV/5101064/2013 vom 27.01.2016 „der Verlustvortrag bei Roelfsen Versicherung  als RNF der  Houdek Maschinenbau  um EUR 665.812,12 zu erhöhen ist, sodass sich ein Verlustvortrag von EUR  1.047.673,40 ergibt.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_137`)


Die BFG- Entscheidung RV/5101064/2013 vom 27.01.2016 für das Jahr 2007 (Rechtsvorgänger) wurde  seitens des Finanzamt Wien 1/23  mittels Amtsrevision bekämpft.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_150`)


Die Wiederaufnahme des Verfahrens wird seitens des Finanzamt Wien 1/23  auf den Vorfragetatbestand  gern.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_197`)


Gemäß § 282  BAO war das Finanzamt Wien 1/23  verpflichtet, die Rechtsanschauung des BFG unverzüglich mit den ihr zu  Gebote stehenden rechtlichen Mitteln umzusetzen.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_252`)


Daher hat das  Finanzamt Wien 1/23  sowohl über die Verlustverrechnung im Jahr 2010 als auch über die Verlusthöhe im  Jahr 2007 bzw über die Verlustzuordnung als zuständige Behörde eigenständig zu entscheiden.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_255`)


Gegenständlich war das Finanzamt Wien 1/23  selbst zur Beantwortung der Frage, ob es ein freies  Wahlrecht in Bezug auf den innerbetrieblichen Verlustausgleich und damit eine willkürliche  Verlustzuordnung im Jahr 2007 gibt, sachlich zu ständig und hat auch tatsächlich eine  entsprechende Beurteilung vorgenommen (siehe dazu ua auch das Beschwerdeverfahren  betreffend Körperschaftsteuer 2007, Houdek Maschinenbau).

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_256`)


Demnach handelt es sich dabei -  entgegen der vom Finanzamt Wien 1/23  vertretenen Ansicht - um keine Vorfrage iSd § 116 BAO im  Hinblick auf die endgültige Beurteilung der Höhe des Verlustvortrages betreffend das Jahr  2010.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_260`)


Vom  Finanzamt Wien 1/23  wurde - zutreffender Weise - nicht vorgebracht, dass es für die einzelnen zu  lösenden Rechtsfragen sachlich unzuständig wäre.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_269`)


Damit erweist sich die  Begründung des Finanzamt Wien 1/23  auf Seite 13 Absatz 2 als unzutreffend bzw steht diese im  Widerspruch zur Entscheidung des VwGH.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_276`)


Zusammenfassend kann festgehalten werden, dass vom Finanzamt Wien 1/23  bei der Argumentation  generell übersehen worden ist, dass beim Verlustvortrag lediglich eine Bindung an die Höhe  des im Körperschaftsteuerbescheid ausgewiesen Verlustes besteht.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_314`)


Dass das Finanzamt Wien 1/23  als zuständige Behörde in den  Folgejahren eine unzutreffende Rechtsauffassung angewendet hat und deshalb die Behörde zu  Lasten des Abgabepflichtigen eine Korrektur erwirken möchte, ist vom Grundsatz von Treu und  Glauben gerade nicht umfasst.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_349`)


Wenn nun die Beschwerdeführerin vermeint, dass das  Finanzamt Wien 1/23  bloß irrtümlich von einer Berücksichtigung im Jahr 2007 ausgegangen ist und  deshalb die Amtsrevision für das Jahr 2007 eingebracht hat (Seite 6 - 7 der Beschwerdeschrift),  so ist dem zu entgegnen, dass nicht nur das Finanzamt Wien 1/23, sondern auch die Beschwerdeführerin  und auch das BFG von einer zu klärenden Rechtsfrage für das Jahr 2007 ausgegangen sind.


Wenn nun die Beschwerdeführerin vermeint, dass das  Finanzamt Wien 1/23  bloß irrtümlich von einer Berücksichtigung im Jahr 2007 ausgegangen ist und  deshalb die Amtsrevision für das Jahr 2007 eingebracht hat (Seite 6 - 7 der Beschwerdeschrift),  so ist dem zu entgegnen, dass nicht nur das Finanzamt Wien 1/23, sondern auch die Beschwerdeführerin  und auch das BFG von einer zu klärenden Rechtsfrage für das Jahr 2007 ausgegangen sind.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_355`)


Damit war aber auch das Finanzamt Wien 1/23  gem. § 282 BAO verpflichtet, die Rechtsanschauung  des BFG´s umzusetzen (und zwar ungeachtet des Umstandes, dass sofort eine Amtsrevision  gegen das BFG-Erkenntnis eingebracht wurde).

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_389`)


Seitens des Finanzamt Wien 1/23  und auch seitens der Beschwerdeführerin war es daher klar, dass die letzte Entscheidung in der  Frage der Existenz des freien Wahlrechtes zum innerbetrieblichen Verlustausgleich (und daraus  folgend zur Höhe der Verlustzuweisung und daraus folgend zur endgültigen Höhe des  Verlustvortrages) alleine dem Verwaltungsgerichtshof obliegt.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_405`)


In der BFG-Entscheidung vom 27.01.2016, RV/5101064/2013 wurde unstrittig der Verlust für  die Beschwerdeführerin mit EUR -3.632.188,29 ausgewiesen und ist deshalb betragsmäßig für  das Finanzamt Wien 1/23  verbindlich geworden.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

</details>

---

## `Bundesamt für Soziales und Behindertenwesen`

**F1:** 0.015 | **Precision:** 0.929 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches 'Bundesamt für Soziales und Behindertenwesen' and its genitive forms 'Bundesamtes' and 'Bundesamts'.

**Content:**
```
\bBundes(?:amt|amtes|amts)\s+für\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.929 | 0.007 | 0.015 | 14 | 13 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 1 | 1111 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_38`)


In § 35 Abs. 2 EStG 1988 hat der Gesetzgeber bindend festgelegt, dass die Tatsache der  Behinderung und das Ausmaß der Minderung der Erwerbsfähigkeit (Grad der Behinderung)  durch eine amtliche Bescheinigung der für diese Feststellung zuständigen Stelle - hier das  Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice) – nachzuweisen ist.

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_49`)


– In allen übrigen Fällen sowie bei Zusammentreffen von   Behinderungen verschiedener Art das Bundesamt für Soziales und Behindertenwesen;

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_56`)


Die zuständige Stelle ist im  gegenständlichen Fall das Bundesamt für Soziales und Behindertenwesen  (Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_59`)


Die Bescheinigung des Bundesamts für Soziales  und Behindertenwesen (Sozialministeriumservice) als gesetzlich ausdrücklich geforderter  Nachweis kann durch die Vorlage von zB haus- oder fachärztlichen Bestätigungen,  Privatgutachten oder Arztbriefen anlässlich eines stationären Krankenhausaufenthaltes nicht  ersetzt werden.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales  und Behindertenwesen` | `Bundesamts für Soziales  und Behindertenwesen` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149848.1_78`)


Diese  Feststellung ob, ab wann und in welchem Ausmaß eine Behinderung vorliegt, obliegt nur dem  Bundesamt für Soziales und Behindertenwesen (Sozialministeriumservice).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_18`)


2. Beweiswürdigung  Der Grad der Behinderung oder die voraussichtlich dauernde Unfähigkeit, sich selbst den  Unterhalt zu verschaffen, ist dem Finanzamt Österreich vom Bundesamt für Soziales und  Behindertenwesen mit einer Bescheinigung aufgrund eines ärztlichen  Sachverständigengutachtens nachzuweisen (§ 8 Abs. 6 FLAG).

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und  Behindertenwesen` | `Bundesamt für Soziales und  Behindertenwesen` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_19`)


Sowohl die Abgabenbehörde als  auch das Bundesfinanzgericht sind an die im Sachverständigengutachten des Bundesamts für  Soziales und Behindertenwesen getroffenen Feststellungen gebunden.

| Predicted | Gold |
|---|---|
| `Bundesamts für  Soziales und Behindertenwesen` | `Bundesamts für  Soziales und Behindertenwesen` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_20`)


Gutachten des  Bundesamts für Soziales und Behindertenwesen dürfen lediglich auf Schlüssigkeit,  Vollständigkeit und im Fall mehrerer Gutachten auf Widerspruchsfreiheit überprüft werden (zB  VwGH 9.9.2017, 2013/16/0049).

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_21`)


Die Behinderung der Bf seit Juli 1999 ergibt sich ebenso wie deren Ausmaß von 30% aus dem  Sachverständigengutachten (mit Untersuchung) des Bundesamts für Soziales und  Behindertenwesen vom 5. Dezember 2024.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_22`)


Da sich dieses Gutachten auf sämtliche zum  Zeitpunkt der Gutachtenserstellung vorliegenden Befunde stützt, ist es, was die Frage des  Zeitpunkts des Eintritts der Behinderung und deren Ausmaß anbelangt, das aus Sicht des  Bundesfinanzgerichts glaubwürdigste, weil vollständigste, der insgesamt drei Gutachten des  Bundesamts für Soziales und Behindertenwesen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_26`)


Die Behinderung im Ausmaß von 50% seit Mai 2012 ergibt sich ebenfalls aus dem  Sachverständigengutachten (mit Untersuchung) des Bundesamts für Soziales und  Behindertenwesen vom 5. Dezember 2024.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und  Behindertenwesen` | `Bundesamts für Soziales und  Behindertenwesen` |

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_38`)


Die drei Sachverständigengutachten des Bundesamts für Soziales und Behindertenwesen  widersprechen sich bezüglich der Frage, ob die Bf dauerhaft erwerbsunfähig ist.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_47`)


Gutachtens vom 2. Juli 2021 und der damit im Zusammenhang stehenden chefärztlichen  Stellungnahme vom 6. Juli 2021 kann das Bundesfinanzgericht daher dem Schluss der beiden  Gutachten des Bundesamts für Soziales und Behindertenwesen vom 14. Februar 2024 und vom  5. Dezember 2024, die Bf sei (erst) seit Juli 2021 dauerhaft erwerbsunfähig, nicht folgen.

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales und Behindertenwesen` | `Bundesamts für Soziales und Behindertenwesen` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_148`)

**False Positives:**


Stets ist jedoch erforderlich, dass die Tatsache der Behinderung und das  Ausmaß der Minderung der Erwerbsfähigkeit durch eine amtliche Bescheinigung (hier: des  Bundesamtes für Soziales und Behindertenwesen) nachgewiesen wird (§ 35 Abs. 2 EStG 1988).

FP: `Bundesamtes für Soziales und Behindertenwesen` (organisation)

**✅ Gold Entities:**

</details>

---

## `Bundesfinanzgerichts Genitive`

**F1:** 0.015 | **Precision:** 0.419 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgerichts' (genitive) specifically to ensure it is captured when the main BFG rule might miss it due to boundary issues.

**Content:**
```
\bBundesfinanzgerichts\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.419 | 0.007 | 0.015 | 31 | 13 | 18 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 13 | 18 | 1463 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_112`)


So konnten seitens des Bundesfinanzgerichts keine Feststellungen  hinsichtlich eines unverschuldeten oder unabwendbaren Ereignisses getroffen werden,  welches den Beschwerdeführer an seiner Pflichterfüllung hinderte.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_93`)


Diese Sachverhaltsfeststellungen ergeben sich nach Dafürhalten des Bundesfinanzgerichts aus  den vorgelegten Akten des Abgabenverfahrens, dem Vorbringen der Bf. in seiner Beschwerde  sowie den Erhebungen durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) ( sent_id: `findok-manually-annotated_TRAIN/137355.1_233`)


Von Seiten des Bundesfinanzgerichts wird darauf verwiesen, dass § 1116 ABGB den  Vertragsparteien das Recht einräumt, sofern nichts anderes vereinbart wurde, den  Bestandvertrag über eine bewegliche Sache mit einer Frist von 24 Stunden zu kündigen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/137355.1`) ( sent_id: `findok-manually-annotated_TRAIN/137355.1_298`)


Von Seiten des Bundesfinanzgerichts wird einleitend nochmals auf den Umstand hingewiesen,  dass die belangte Behörde die Versicherungsprämien nur in jenen Fällen in die  Bemessungsgrundlage miteinbezogen hat, in denen die Versicherung urkundlich vereinbart  und die Versicherungsprämie daher vom Leasingnehmer an die Beschwerdeführerin geleistet  wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated_TRAIN/149834.1_139`)


Die Beschwerde wurde der nunmehr zuständigen Gerichtsabteilung des Bundesfinanzgerichts  aufgrund einer Verfügung des Geschäftsverteilungsausschusses iZm der Pensionierung des  bisherigen Richters mit 01.07.2025 zugeteilt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated_TRAIN/149834.1_245`)


Nach der Rechtsprechung des Bundesfinanzgerichts ist eine  18 von 25 Seite 19 von 25

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) ( sent_id: `findok-manually-annotated_TRAIN/135661.1_126`)


Seitens des Bundesfinanzgerichts ist dazu festzustellen, dass der vom Finanzamt angeführten  Begründungserwägung, wonach der Wohnsitz in Ort1 (Ö) „ungeachtet der tatsächlichen  Häufigkeit der Nächtigung in Ort1 (Ö) bzw am weiteren Schweizer Wohnsitz“ als Mittelpunkt  der Lebensinteressen der Bf. zu qualifizieren sei, nicht gefolgt werden kann.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) ( sent_id: `findok-manually-annotated_TRAIN/135661.1_127`)


Nach der  vorliegenden Aktenlage ist auch nach Ansicht des Bundesfinanzgerichts davon auszugehen,  dass bereits im Zeitpunkt der erstmaligen Einbringung des gegenständlichen Kfz durch die Bf.  nach Österreich zwischen der Bf. und A. eine enge Lebensbeziehung bestand.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) ( sent_id: `findok-manually-annotated_TRAIN/135661.1_136`)


Dieser Umstand ist nach Ansicht des Bundesfinanzgerichts im Sinne  des § 1 Abs. 7 MeldeG durchaus beachtlich (vgl. zB VwGH 06.07.2020, Ra 2020/01/0141;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated_TRAIN/149473.1_61`)


Die gegenständliche Rechtssache RV/7100840/2024 wurde mit Verfügung des  Geschäftsverteilungsausschusses des Bundesfinanzgerichts vom 3. Februar 2025 zum Stichtag  7. Februar 2025 der Gerichtsabteilung 1036 zugeteilt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/144052.1`) ( sent_id: `findok-manually-annotated_TRAIN/144052.1_153`)


Schließlich ist zum Nachweis der Nutzungsflächen und -verhältnisse  allgemein darauf zu verweisen, dass eine in freier Beweiswürdigung getroffene Feststellung  des Bundesfinanzgerichts der Kontrolle durch den Verwaltungsgerichtshof grundsätzlich nicht  zugänglich ist;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/149801.1`) ( sent_id: `findok-manually-annotated_TRAIN/149801.1_28`)


Die Krankheitskosten 2020 und 2021 sowie das Kilometergeld 2021 berücksichtigte die bB  bereits als außergewöhnliche Belastungen ohne Selbstbehalt, und auch der Berücksichtigung  des Kilometergelds 2020 als außergewöhnliche Belastung ohne Selbstbehalt steht aus Sicht der  bB (Vorlagebericht vom 5. Dezember 2022, S 5) und des Bundesfinanzgerichts nichts entgegen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 12** (doc_id: `findok-manually-annotated_TRAIN/149801.1`) ( sent_id: `findok-manually-annotated_TRAIN/149801.1_38`)


Wie ausgeführt, hat der Bf trotz  Aufforderung des Bundesfinanzgerichts keinen von § 3 Abs 1 VO vorgesehenen Nachweis  seiner dauernden Mobilitätseinschränkung beigebracht, weswegen die bB den pauschalen  Freibetrag wegen Unzumutbarkeit der Benützung öffentlicher Verkehrsmittel für die Jahre  2020 und 2021 zu Recht versagt hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_100`)

**False Positives:**


Das Erkenntnis des Bundesfinanzgerichts, Außenstelle Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des FA Wien 1/23  in vollem Umfang im Zuge einer Amtsrevision  angefochten.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_124`)

**False Positives:**


Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH der  Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels objektbezogener  Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen Erkenntnis des  Bundesfinanzgerichts dargestellten Höhe zustehe, erweise sich der Spruch des angefochtenen  10 von 39 Seite 11 von 39

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)
- `X GmbH` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_128`)

**False Positives:**


85-900/3590, BV 24 :  Beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  gab es betreffend dem  Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid  Gruppenmitglied:  21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010  27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010 nach Betriebsprüfung   27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010  20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010  (Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung  Rekultivierungskosten)  19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)  29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)  16.12.2013 Vorlage an BFG (damals noch UFS)  17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  Betreffend des Rechtsvorgängers Houdek Maschinenbau  wurde das Erkenntnis des  Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum  Veranlagungsjahr 2007 erlassen.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `85-900/3590` (tax_number)
- `Roelfsen Versicherung` (organisation)
- `UFS` (organisation)
- `Houdek Maschinenbau` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_433`)

**False Positives:**


30 Auch wenn der X GmbH bzw. der mitbeteiligten Partei als Rechtsnachfolgerin der X GmbH  der Verlustvortrag in den Jahren nach 2007 nur in der zuvor dargestellten (mittels  objektbezogener Zuordnung zu ermittelnden) Höhe und somit nicht in der im angefochtenen  Erkenntnis des Bundesfinanzgerichts dargestellten Höhe zusteht, erweist sich der Spruch des  angefochtenen Erkenntnisses nicht als rechtswidrig.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)
- `X GmbH` (organisation)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_44`)

**False Positives:**


Die Beschwerde wurde der nunmehr zuständigen Gerichtsabteilung des Bundesfinanzgerichts  aufgrund einer Verfügung des Geschäftsverteilungsausschusses iZm der Pensionierung der  bisherigen Richterin mit 01.07.2025 zugeteilt.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_22`)

**False Positives:**


Da sich dieses Gutachten auf sämtliche zum  Zeitpunkt der Gutachtenserstellung vorliegenden Befunde stützt, ist es, was die Frage des  Zeitpunkts des Eintritts der Behinderung und deren Ausmaß anbelangt, das aus Sicht des  Bundesfinanzgerichts glaubwürdigste, weil vollständigste, der insgesamt drei Gutachten des  Bundesamts für Soziales und Behindertenwesen.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `Bundesamts für Soziales und Behindertenwesen` (organisation)

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_40`)

**False Positives:**


Hinzu kommt, dass die beiden Gutachten,  die eine dauerhafte Erwerbsunfähigkeit der Bf bejahen, aus Sicht des Bundesfinanzgerichts in  der Frage, seit wann diese dauerhafte Erwerbsunfähigkeit besteht, in sich unschlüssig sind.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_58`)

**False Positives:**


Aus Sicht des Bundesfinanzgerichts konnte die Bf keinen gutachterlichen, wissenschaftlich  fundierten Nachweis darüber führen, dass eine dauerhafte Erwerbsunfähigkeit bereits vor  ihrem 21.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_61`)

**False Positives:**


Die gegenständliche Rechtssache RV/7100840/2024 wurde mit Verfügung des  Geschäftsverteilungsausschusses des Bundesfinanzgerichts vom 3. Februar 2025 zum Stichtag  7. Februar 2025 der Gerichtsabteilung 1036 zugeteilt.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_139`)

**False Positives:**


Die Beschwerde wurde der nunmehr zuständigen Gerichtsabteilung des Bundesfinanzgerichts  aufgrund einer Verfügung des Geschäftsverteilungsausschusses iZm der Pensionierung des  bisherigen Richters mit 01.07.2025 zugeteilt.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_245`)

**False Positives:**


Nach der Rechtsprechung des Bundesfinanzgerichts ist eine  18 von 25 Seite 19 von 25

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1_233`)

**False Positives:**


Von Seiten des Bundesfinanzgerichts wird darauf verwiesen, dass § 1116 ABGB den  Vertragsparteien das Recht einräumt, sofern nichts anderes vereinbart wurde, den  Bestandvertrag über eine bewegliche Sache mit einer Frist von 24 Stunden zu kündigen.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/137355.1_298`)

**False Positives:**


Von Seiten des Bundesfinanzgerichts wird einleitend nochmals auf den Umstand hingewiesen,  dass die belangte Behörde die Versicherungsprämien nur in jenen Fällen in die  Bemessungsgrundlage miteinbezogen hat, in denen die Versicherung urkundlich vereinbart  und die Versicherungsprämie daher vom Leasingnehmer an die Beschwerdeführerin geleistet  wurde.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_126`)

**False Positives:**


Dabei hat das  Bundesfinanzgericht nach der Sach- und Rechtslage zu entscheiden, die im Zeitpunkt seiner  Entscheidung vorliegt und somit auch jene Feststellungsbescheide zu Grunde zu legen, die zum  Zeitpunkt der Entscheidung des Bundesfinanzgerichts dem Rechtsbestand angehören (VwGH  vom 18. Dezember 2019, Ra 2019/15/0154).

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_127`)

**False Positives:**


Für den Beschwerdefall bedeutet dies, dass die zwischenzeitlich ergangenen Entscheidungen  des Bundesfinanzgerichts hinsichtlich der Feststellungsbescheide zur DVM II -  RV/7100470/2014 vom 29. November 2022 - sowie hinsichtlich der Feststellungsbescheide zu  INET II (aufgrund des rechtskräftigem BFG-Erkenntnisses RV/7102483/2013 vom 27.5.2022  bzw. BP-Bericht vom 29.22.2010 (ABNr.: 121095/09) zur St.nr.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_126`)

**False Positives:**


Seitens des Bundesfinanzgerichts ist dazu festzustellen, dass der vom Finanzamt angeführten  Begründungserwägung, wonach der Wohnsitz in Ort1 (Ö) „ungeachtet der tatsächlichen  Häufigkeit der Nächtigung in Ort1 (Ö) bzw am weiteren Schweizer Wohnsitz“ als Mittelpunkt  der Lebensinteressen der Bf. zu qualifizieren sei, nicht gefolgt werden kann.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_127`)

**False Positives:**


Nach der  vorliegenden Aktenlage ist auch nach Ansicht des Bundesfinanzgerichts davon auszugehen,  dass bereits im Zeitpunkt der erstmaligen Einbringung des gegenständlichen Kfz durch die Bf.  nach Österreich zwischen der Bf. und A. eine enge Lebensbeziehung bestand.

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `Österreich` (country)

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_136`)

**False Positives:**


Dieser Umstand ist nach Ansicht des Bundesfinanzgerichts im Sinne  des § 1 Abs. 7 MeldeG durchaus beachtlich (vgl. zB VwGH 06.07.2020, Ra 2020/01/0141;

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**

</details>

---

## `Generic Company Names`

**F1:** 0.014 | **Precision:** 1.000 | **Recall:** 0.007  

**Format:** `regex`  
**Description:**
Matches common capitalized company names that appear in lists (e.g., Ikea, Obi, Leiner) when followed by a comma or end of sentence, or in a list context.

**Content:**
```
\b(?:Ikea|Obi|Leiner|M\u00f6belix|M\u00f6maX|Otto\.de|xxxLutz|Quelle\.at|SENECURA|Be\.|A-GmbH|B-GmbH|Hausverwaltung-GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.007 | 0.014 | 12 | 12 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 0 | 1558 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_47`)


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.


Der Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.

| Predicted | Gold |
|---|---|
| `Ikea` | `Ikea` |
| `Obi` | `Obi` |
| `Leiner` | `Leiner` |
| `Möbelix` | `Möbelix` |
| `MömaX` | `MömaX` |
| `Otto.de` | `Otto.de` |
| `xxxLutz` | `xxxLutz` |
| `Quelle.at` | `Quelle.at` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_11`)


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |
| `SENECURA` | `SENECURA` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_12`)


Für 2017: Mobiler Hilfsdienst SENECURA 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 sowie eigene Arztkosten der Bf 633,76 Euro.

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_36`)


Darin wurden weitere Nachweise und Unterlagen zu den Krankheitskosten für  die Mutter der Bf angefordert (Vereinbarung über die Kostentragung mit dem Pflegeheim,  Rechtsgrundlage für die Übernahme der Zahlungen für diverse Lebenshaltungskosten,  Nachweise über tatsächliche Verausgabungen und Kosten der Mutter, Aufgabe des Mobilen  Hilfsdienst SENECURA, Nachweis der Aktiva des Nachlasses der verstorbenen Mutter, etc).

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

</details>

---

## `Schmeltz Luftfahrt`

**F1:** 0.013 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Schmeltz Luftfahrt'.

**Content:**
```
\bSchmeltz\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.013 | 11 | 11 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 11 | 0 | 1524 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_20`)


Für das ursprünglich streitgegenständliche Jahr 2007 und die Nachfolgejahre wurden folgende  Umgründungsschritte bei Houdek Maschinenbau  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die Houdek Maschinenbau  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach den Bestimmungen des  Bundesgesetz über die Spaltung von Kapitalgesellschaften mit Gesamtrechtsnachfolgewirkung  und unter Inanspruchnahme der umgründungssteuerlichen Begünstigungen des Artikel VI  UmgrStG das in der Übertragungsbilanz dargestellte Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die Schmeltz Luftfahrt  übertragen.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_21`)


Die Schmeltz Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_26`)


Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_49`)


Teilbetriebe  Schmeltz Luftfahrt:   Verluste  geschlossene  Teilbetriebe  Houdek Maschinenbau:   -326.546,95 6,78 %

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_54`)


Abgespaltene  Tankstellen  Schmeltz Luftfahrt **   Geschlossene  Tankstellen  Houdek Maschinenbau **  Verkaufte  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **  Verbleibende  Tankstellen  Houdek Maschinenbau **

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_62`)


Begründend führte die  Beschwerdeführerin in der Beschwerde aus, dass die Gewinnermittlung für 2007 auf der Ebene  der Houdek Maschinenbau  nach allgemeinen Grundsätzen durchzuführen sei, da der  Vermögensübergang hinsichtlich der 11 Tankstellen auf die Schmeltz Luftfahrt  erst mit Ablauf des  Spaltungsstichtages (Spaltungsstichtag 31.12.2007) per 1.1.2008 stattgefunden habe.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_66`)


Die Houdek Maschinenbau  habe daher jene Verluste, die den per 31.12.2007 auf die  Schmeltz Luftfahrt  abgespaltenen Tankstellen zuzurechnen seien, vorrangig (und nicht wie von der  BP vorgesehen nur aliquot) im Wege eines innerbetrieblichen Verlustausgleichs mit Gewinnen  anderer Teilbetriebe ausgeglichen.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_107`)


Einkünfte  könnten demnach ausschließlich durch bloße Bestimmung der Houdek Maschinenbau  auf die  Schmeltz Luftfahrt  übertragen werden oder eben nicht übertragen werden.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_221`)


Nach erfolgter Fristverlängerung wurden am 28.3.2019 sowohl vom Gruppenmitglied als  auch vom Gruppenträger zwei gleichlautende Beschwerden erhoben und jeweils begründend  ausgeführt: „Ausgangslage: Im Jahr 2007 hat die Houdek Maschinenbau  insgesamt 84 Tankstellen  betrieben, wobei mit Stichtag 31.12.2007 11 Teilbetriebs-Tankstellen auf die Schmeltz Luftfahrt  nach Art VI UmgrStG abgespalten wurden.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_222`)


Die Schmeltz Luftfahrt  wurde in weiterer Folge mit der  Dorfcon-Verlag  verschmolzen.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_229`)


Nach Ansicht der Betriebsprüfung GmbH das Finanzamt müsse der gesamte im Jahr 2007  erwirtschaftete Verlust der Houdek Maschinenbau  ermittelt und aufgrund der Abspaltung von 11  Tankstellen aliquot zwischen der Houdek Maschinenbau  und der Schmeltz Luftfahrt  aufgeteilt werden,  wodurch sich nicht nur eine Änderung des steuerlichen Ergebnisses 2007 ergäbe, sondern auch  eine Anpassung der Verlustvorträge und der in Folgejahren vorgenommenen  Verlustverwertung erfolgen müsse.

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

</details>

---

## `Merkur Treuhand Steuerberatung GmbH`

**F1:** 0.011 | **Precision:** 1.000 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches 'Merkur Treuhand Steuerberatung GmbH' specifically, handling potential line breaks.

**Content:**
```
\bMerkur\s+Treuhand\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.006 | 0.011 | 10 | 10 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 0 | 25 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Hartwig Boehler  in der Beschwerdesache DDr.in Josepha de Haan,  Oisching 129, 3071 Wiesen, Österreich, vertreten durch Merkur Treuhand Steuerberatung GmbH, St.-Veit-Gasse 50,  1130 Wien, über die Beschwerde vom 16. Mai 2024 gegen den Bescheid des Finanzamtes  Österreich vom 13. Mai 2024 betreffend Abrechnung gem. § 216 BAO Steuernummer  01-186/7053  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und festgestellt, dass die  Umbuchung des per 3.4.2024 auf dem Abgabenkonto der Beschwerdeführerin bestehenden  Guthabens i.H.v. € 166.146,40 auf Finanzverwahrnisse unrichtig war.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_43`)


B. Umbuchung eines Guthabens auf Finanzverwahrnisse  Mit Schreiben vom 13.3.2024, eingelangt bei der belangten Behörde am selben Tage,  übermittelte die Merkur Treuhand Steuerberatung GmbH der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin und ihr unterfertigte Vollmacht, womit die  Beschwerdeführerin die Merkur Treuhand Steuerberatung GmbH als „Vertreter in allen  steuerlichen, wirtschaftlichen und sonstigen Angelegenheiten“ bevollmächtigt.


B. Umbuchung eines Guthabens auf Finanzverwahrnisse  Mit Schreiben vom 13.3.2024, eingelangt bei der belangten Behörde am selben Tage,  übermittelte die Merkur Treuhand Steuerberatung GmbH der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin und ihr unterfertigte Vollmacht, womit die  Beschwerdeführerin die Merkur Treuhand Steuerberatung GmbH als „Vertreter in allen  steuerlichen, wirtschaftlichen und sonstigen Angelegenheiten“ bevollmächtigt.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_44`)


Weiters wurde  der Merkur Treuhand Steuerberatung GmbH darin die Vollmacht „zum Empfang von  Schriftstücken, insbesondere der Abgabenbehörden, welche nunmehr ausschließlich dem  Bevollmächtigten zuzustellen sind“ erteilt und mitgeteilt, dass durch die vorliegende Vollmacht  „noch etwa beim Finanzamt erliegende vorhergehende Vollmachten außer Kraft gesetzt“  werden.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_45`)


Im (Begleit-) Schreiben vom 13.3.2024 führt die Merkur Treuhand Steuerberatung  GmbH aus, dass die Vollmacht als „Spezialvollmacht für das laufende Verfahren betreffend  Umsatzsteuer und NOVA sowie das Finanzstrafverfahren“ erteilt wurde.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung  GmbH` | `Merkur Treuhand Steuerberatung  GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_54`)


Die Schabetsberger Steuerberatung GmbH leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  Merkur Treuhand Steuerberatung GmbH weiter.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_63`)


Die Feststellungen zum Sicherstellungsauftrag vom 20.3.2024 und zum Pfändungsbescheid  vom 3.4.2024 gründen sich auf eine Einsichtnahme in den Akt RV/702183/2024 des  Bundesfinanzgerichtes (dort bekämpft die Beschwerdeführerin den Pfändungsbescheid vom  3.4.2024), insbesondere auf den Zustellnachweis (Rückschein) zum Sicherstellungsauftrag vom  20.3.2024 und zum Pfändungsbescheid vom 3.4.2024, worin ein Mitarbeiter oder eine  Mitarbeiterin (Unterschrift unleserlich) der Schabetsberger Steuerberatung GmbH die  Übernahme dieser beiden Bescheide am 5.4.2024 bestätigt, sowie auf das Schreiben der  Merkur Treuhand Steuerberatung GmbH vom 13.3.2024 und die damit übermittelte Vollmacht  vom 11.3.2024.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_107`)


Im vorliegenden Fall bestellte die Beschwerdeführerin am 11.3.2024 die Merkur Treuhand  Steuerberatung GmbH zum Zustellbevollmächtigten.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand  Steuerberatung GmbH` | `Merkur Treuhand  Steuerberatung GmbH` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_110`)


Anzumerken ist, dass die Vollmacht zugunsten der Merkur  Treuhand Steuerberatung GmbH entgegen den Ausführungen im Schreiben vom 13.3.2024 alle  steuerlichen Angelegenheiten umfasst und daher nicht auf das laufende Verfahren betreffend  Umsatzsteuer und NOVA sowie das Finanzstrafverfahren eingeschränkt ist.

| Predicted | Gold |
|---|---|
| `Merkur  Treuhand Steuerberatung GmbH` | `Merkur  Treuhand Steuerberatung GmbH` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_121`)


Die hier geschehene Übermittlung der eingescannten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail der Schabetsberger  Steuerberatung GmbH vom 16.4.2024 an die Merkur Treuhand Steuerberatung GmbH konnte  daher keine Heilung der unwirksamen Zustellung bewirken.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

</details>

---

## `SeneCura Variations`

**F1:** 0.011 | **Precision:** 0.909 | **Recall:** 0.006  

**Format:** `regex`  
**Description:**
Matches 'SeneCura', 'SENECURA', 'Senecura', and variations with 'Laurentius Park' (with/without hyphens/spaces).

**Content:**
```
(?i)\bSeneCura(?:\s+(?:Laurentius\s+)?Park(?:\s+Bludenz)?)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.909 | 0.006 | 0.011 | 11 | 10 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 10 | 1 | 1314 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_11`)


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |
| `SENECURA` | `SENECURA` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_12`)


Für 2017: Mobiler Hilfsdienst SENECURA 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 sowie eigene Arztkosten der Bf 633,76 Euro.

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_36`)


Darin wurden weitere Nachweise und Unterlagen zu den Krankheitskosten für  die Mutter der Bf angefordert (Vereinbarung über die Kostentragung mit dem Pflegeheim,  Rechtsgrundlage für die Übernahme der Zahlungen für diverse Lebenshaltungskosten,  Nachweise über tatsächliche Verausgabungen und Kosten der Mutter, Aufgabe des Mobilen  Hilfsdienst SENECURA, Nachweis der Aktiva des Nachlasses der verstorbenen Mutter, etc).

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_50`)


Anschließend brachte die belangte Behörde ergänzend vor, dass sie die Richtigkeit des Inhaltes  der Rechnung vom 25.04.2016 (es wurden 4 weitere Rechnungen/Bestätigungen der SeneCura  im Rahmen des Ermittlungsverfahrens von der Bf bzw von deren Vertreter vorgelegt) in der  Höhe von 985,34 Euro bezweifle und ihr diese nicht gänzlich richtig erscheine, da hier  Kostenteile des Kostenträgers nicht abgerechnet, sondern zugerechnet wurden.

| Predicted | Gold |
|---|---|
| `SeneCura` | `SeneCura` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_61`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Mutter der Bf war in den streitgegenständlichen Jahren im Pflegeheim SeneCura Laurentius  Park Bludenz (beginnend ab 28.01.2016) untergebracht.

| Predicted | Gold |
|---|---|
| `SeneCura Laurentius  Park Bludenz` | `SeneCura Laurentius  Park Bludenz` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_68`)


Die Bf lebte in Wien, die Mutter der Bf war in Bludenz im Pflegeheim SeneCura Laurentius Park  untergebracht.

| Predicted | Gold |
|---|---|
| `SeneCura Laurentius Park` | `SeneCura Laurentius Park` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_69`)


Damit ihre Mutter nicht vereinsamte, übernahm die Bf die Kosten für eine  Besuchshilfe (Mobiler Hilfsdienst Senecura), welcher bereits aber auch in den Jahren, bevor die  Mutter der Bf ins Pflegeheim kam, regelmäßig gebucht war.

| Predicted | Gold |
|---|---|
| `Senecura` | `Senecura` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_77`)


Für das Jahr 2016 wurden von der Bf zusätzlich Pflege(heim)kosten iHv 3.259,47 Euro von  ihrem Konto an SeneCura überwiesen.

| Predicted | Gold |
|---|---|
| `SeneCura` | `SeneCura` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_80`)


2. Beweiswürdigung  Der Sachverhalt ist grundsätzlich unstrittig und ergibt sich als solcher aus dem Akt,  insbesondere den angeführten Aktenteilen wie den Bestätigungen der PVA, des SeneCura  Laurentius Park Bludenz und den Kontoauszügen.

| Predicted | Gold |
|---|---|
| `SeneCura  Laurentius Park Bludenz` | `SeneCura  Laurentius Park Bludenz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_13`)

**False Positives:**


Dazu wurden von der Bf Bestätigungen der PVA, dem SeneCura Laurentius-Park Bludenz und  diverse Arzthonorare von Fachärzten für Nervenheilkunde vorgelegt.

FP: `SeneCura` (organisation)

**✅ Gold Entities:**
- `PVA` (organisation)
- `SeneCura Laurentius-Park Bludenz` (organisation)

</details>

---

## `Dorfcon-Verlag`

**F1:** 0.010 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Dorfcon-Verlag'.

**Content:**
```
\bDorfcon-Verlag\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.010 | 9 | 9 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 0 | 1523 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_21`)


Die Schmeltz Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag  verschmolzen worden.

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_26`)


Die Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz Luftfahrt (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_32`)


Neben der Berücksichtigung der unstrittigen Feststellungen teilte das Finanzamt den erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und Dorfcon-Verlag  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu den abgespaltenen bzw. verbliebenen (Teil-)Betrieben auf und  verweigerte damit im Ergebnis die gänzliche Zurechnung des erzielten Verlustes 2007  ausschließlich an die Roelfsen Versicherung.

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_45`)


Der im Rahmen der Betriebsprüfung ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und Dorfcon-Verlag  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen Rundungsdifferenz € 0,01) aufzuteilen:  Gewinne verkaufte Teilbetriebe  Houdek Maschinenbau:  596.815,17  Gewinne verbleibende Teilbetriebe  Houdek Maschinenbau  586.237,84  Summe Gewinne: 1.183.053,01

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_58`)


Gewinne  216.864,04 80.229,07   885.959,89 1.183.053,01  Ergebnis lt. BP -665.812,12 -246.317,88   -2.720.058,29  -3.632.188,28  Ergebnis  Dorfcon-Verlag  -665.812,12       5 von 39 Seite 6 von 39

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_60`)


(Der Körperschaftsteuerbescheid 2007 des partiellen  Gesamtrechtsnachfolgers Dorfcon-Verlag  vom 26.04.2013, wo Einkünfte aus Gewerbebetrieb  von € -665.812,12 festgesteilt wurden, erwuchs in Rechtskraft).

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_222`)


Die Schmeltz Luftfahrt  wurde in weiterer Folge mit der  Dorfcon-Verlag  verschmolzen.

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_424`)


Der Körperschaftsteuerbescheid 2007 des partiellen Rechtsnachfolgers Dorfcon-Verlag  mit  Einkünften aus Gewerbebetrieb in Höhe von € -665.812,12 erwuchs in Rechtskraft.

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

</details>

---

## `University Abbreviations JKU WU`

**F1:** 0.010 | **Precision:** 0.225 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches the specific university abbreviations JKU and WU as standalone entities.

**Content:**
```
\b(?:JKU|WU)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.225 | 0.005 | 0.010 | 40 | 9 | 31 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 9 | 31 | 632 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_41`)


Siehe Internetseite JKU und WU  Karriereaussichten!


Siehe Internetseite JKU und WU  Karriereaussichten!

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |
| `WU` | `WU` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

| Predicted | Gold |
|---|---|
| `WU` | `WU` |
| `JKU` | `JKU` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_92`)


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.


https://www.jku.at/studium/studienarten/bachelordiplom/ba-wirtschaftswissenschaften/   (Datum der Abfragen: Approbationsdatum dieser Entscheidung) und umfassen jeweils  volkswirtschaftliche, betriebswirtschaftliche und sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (WU: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“,  „Wirtschaftsinformatik“, „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (JKU: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, „E-Business- Management und Kommunikationssysteme“, „Volkswirtschaft“, „Management und Applied  Economics“, „Business Engineering and Logistics Management“) sowie jeweils weiterführende  Fächer wie Mathematik, Statistik, Recht, Fremdsprachen etc.

| Predicted | Gold |
|---|---|
| `WU` | `WU` |
| `JKU` | `JKU` |

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_109`)


In Zusammenschau mit der Bestätigung der JKU, dass die streitgegenständlichen Studien  „grundsätzlich gleichwertig“ sind, wird daher auch im konkreten Fall von einem Wechsel der  Tochter der Bf. zwischen zwei vergleichbaren und gleichwertigen Studien ausgegangen.

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)

**False Positives:**


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_11`)

**False Positives:**


 Abgangsbescheinigung der WU Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- und Sozialwissenschaften, aus welcher unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten sowie der Abschluss der Studieneingangs- und  Orientierungsphase mit 07.03.2018 hervorgeht:    [...]

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)

**False Positives:**


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `JKU` (organisation)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `JKU` (organisation)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `WU` (organisation)


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_14`)

**False Positives:**


 Abgangsbescheinigung der JKU Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften (Studienplan 2018W)

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `JKU Linz` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_25`)

**False Positives:**


5. Die belangte Behörde ersuchte mit Schreiben vom 02.12.2021 die Bf. um die in der  Beschwerde angekündigte Nachreichung der Unterlagen der WU Wien (Vergleich der  Studienrichtungen).

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)

**False Positives:**


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_29`)

**False Positives:**


Die von der belangten Behörde angeforderten Angaben der WU Wien wurden mit diesem  Schreiben jedoch nicht vorgelegt.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_33`)

**False Positives:**


An der WU Wien wurde das Studium  Wirtschafts- und Sozialwissenschaften (Bachelor) betrieben, in Linz handelte es sich um das  Studium Wirtschaftswissenschaften (Bachelor).

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `Linz` (city)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_37`)

**False Positives:**


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

FP: `WU` (organisation)


01.12.2021 (s. Anhang), wonach von einer Gleichwertigkeit der Studien BA Sozial- und  Wirtschaftswissenschaften an der WU Wien und BA Wirtschaftswissenschaften an der JKU Linz  ausgegangen werden könne, tätigt das Finanzamt jedoch nicht.

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)

**False Positives:**


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler  Universität Linz` (organisation)
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_48`)

**False Positives:**


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

FP: `WU` (organisation)


Die Qualifikations- bzw. Ausbildungsziele für ein Studium der Wirtschaftswissenschaften  in Hinblick auf Kompetenzen (im Sinne eines spezialisiertes Systems von Fähigkeiten)  sowie von avisierten Lernergebnissen (operationalisiert durch vollzogene Prüfungen)  sind an beiden Universitäten in Hinblick auf diesen beiden Programme als gleichwertig  anzusehen.“   Curricula (Studienpläne) des BA Sozial- und Wirtschaftswissenschaften der WU Wien  und des BA Wirtschaftswissenschaften der JKU Linz aus dem betreffenden Zeitraum  5 von 16 Seite 6 von 16

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_54`)

**False Positives:**


Aufgrund des Arbeitsauftrages wurde dann ermittelt und es stellte sich ein Studienwechsel mit  WS 19/20 heraus, vom Studium UJ033 561 Bachelorstudium Wirtschafts- und  Sozialwissenschaften an der WU Wien auf UK033 572 Bachelorstudium  Wirtschaftswissenschaften an der JKU Linz.

FP: `WU` (organisation)


Aufgrund des Arbeitsauftrages wurde dann ermittelt und es stellte sich ein Studienwechsel mit  WS 19/20 heraus, vom Studium UJ033 561 Bachelorstudium Wirtschafts- und  Sozialwissenschaften an der WU Wien auf UK033 572 Bachelorstudium  Wirtschaftswissenschaften an der JKU Linz.

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_60`)

**False Positives:**


Im Dezember 2021 langte dann noch eine Bestätigung der JKU  Linz ein, die die beiden Studien „grundsätzlich gleichwertig“ ansah.

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `JKU  Linz` (organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_61`)

**False Positives:**


Weiters wurde jedoch von  den abgelegten 42 ECTS an der WU Wien, nur 24 ECTS an der JKU Linz angerechnet.

FP: `WU` (organisation)


Weiters wurde jedoch von  den abgelegten 42 ECTS an der WU Wien, nur 24 ECTS an der JKU Linz angerechnet.

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_65`)

**False Positives:**


Im gegenständlichen Fall  wurde das erste Studium an der WU Wien nach 4 Semester gewechselt, also nach dem jeweils  dritten inskribierten Semester und daher liegt ein schädlicher Studienwechsel vor.

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_73`)

**False Positives:**


Von den an der WU Wien absolvierten  Lehrveranstaltungen mit 42 ECTS-Punkten wurden 24 ECTS-Punkte an der JKU Linz  angerechnet.

FP: `WU` (organisation)


Von den an der WU Wien absolvierten  Lehrveranstaltungen mit 42 ECTS-Punkten wurden 24 ECTS-Punkte an der JKU Linz  angerechnet.

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_74`)

**False Positives:**


Weiters absolvierte die Tochter der Bf. an der JKU Linz Lehrveranstaltungen mit  31 ECTS-Punkten (ohne Berücksichtigung von Anrechnungen).

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `JKU Linz` (organisation)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)

**False Positives:**


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

FP: `WU` (organisation)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_97`)

**False Positives:**


JKU-Curriculum § 5 Abs. 3; Datum der Abfrage: Approbationsdatum dieser  Entscheidung).

FP: `JKU` (organisation)

**✅ Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_98`)

**False Positives:**


Die belangte Behörde bringt vor, dass von den abgelegten 42 ECTS an der WU Wien lediglich  24 ECTS an der JKU Linz angerechnet wurden.

FP: `WU` (organisation)


Die belangte Behörde bringt vor, dass von den abgelegten 42 ECTS an der WU Wien lediglich  24 ECTS an der JKU Linz angerechnet wurden.

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

</details>

---

## `Landespolizeidirektion`

**F1:** 0.009 | **Precision:** 1.000 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches 'Landespolizeidirektion' followed by a city name.

**Content:**
```
\bLandespolizeidirektion\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.005 | 0.009 | 8 | 8 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 0 | 1125 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_7`)


Entscheidungsgründe  Verfahrensgang:  Das Abstellen des mehrspurigen Kraftfahrzeuges mit dem behördlichen Kennzeichen 123 (A)  wurde von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien  (A118) am 18. April 2025 um 11:07 Uhr in 1120 Wien, Meidlinger Hauptstraße 67,  beanstandet, da ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149675.1_19`)


In dem Schreiben vom 18. August 2025 wurde zum Ergebnis der Beweisaufnahme angeführt:  „Aus der Organstrafverfügung, welche von einem Organ des Parkraumüberwachungsorgans  der Landespolizeidirektion Wien aufgrund eigener dienstlicher Wahrnehmung gelegt wurde,  ergibt sich, dass das Fahrzeug der Marke Marke mit dem behördlichen Kennzeichen 123 am  18.04.2025 um 11:07 Uhr in 1120 Wien, Meidlinger Hauptstraße 67, in einer  gebührenpflichtigen Kurzparkzone abgestellt, ohne für seine Kennzeichnung mit einem für den  Beanstandungszeitpunkt gültigen Parkschein gesorgt zu haben.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149822.1`) ( sent_id: `findok-manually-annotated_TRAIN/149822.1_7`)


Entscheidungsgründe  Das mehrspurige Kraftfahrzeug, mit dem behördlichen Kennzeichen W-Kennz. (A) wurde vom  Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien am 07. Mai 2025  um 11:59 Uhr in der gebührenpflichtigen Kurzparkzone in 1050 Wien, Bacherplatz gegenüber  14, beanstandet, da es zur Beanstandungszeit ohne gültigen Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_75`)


Diesen Lebensumständen stehen folgende inländische (österreichische) Anknüpfungspunkte  gegenüber: Nachweisliche Aufenthalte  - am 18. August 2019 (6-stündige Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" im Hinblick auf den beabsichtigten  Führerscheinerwerb),  vom 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019 sowie  17. bis 19. Februar 2020 (in Wien mit dem Bf. unternommene Fahrten gemäß § 19 Abs. 8 FSG;  am 20. Februar 2020 wurde vom Bf. die Überweisung von € 173,10 an die  Landespolizeidirektion Wien - Verkehrsamt vorgenommen).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/148818.1`) ( sent_id: `findok-manually-annotated_TRAIN/148818.1_7`)


Kontrollorgan DNr der Parkraumüberwachung der Landespolizeidirektion Wien am 28. Februar  2025 um 14:19 Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer  Straße nächst ONr. 164, beanstandet, da es ohne gültig entwerteten Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/148818.1_7`)


Kontrollorgan DNr der Parkraumüberwachung der Landespolizeidirektion Wien am 28. Februar  2025 um 14:19 Uhr in der gebührenpflichtigen Kurzparkzone in 1230 Wien, Altmannsdorfer  Straße nächst ONr. 164, beanstandet, da es ohne gültig entwerteten Parkschein abgestellt war.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

</details>

---

## `Frontex`

**F1:** 0.009 | **Precision:** 0.421 | **Recall:** 0.005  

**Format:** `regex`  
**Description:**
Matches the organization 'Frontex'.

**Content:**
```
\bFrontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.421 | 0.005 | 0.009 | 19 | 8 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 11 | 241 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_6`)


Über Aufforderung der belangten Behörde gliederte der Bf. die Reisekosten wie folgt auf:  Einsätze für die Grenzschutzagentur Frontex: versteuerte Taggelder  Einsatz im Jahr 2018 als Frontex-Beamter in  Sardinien (I) vom 04.06.

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_62`)


Werbungskosten die in Zusammenhang mit Frontex, EASO, ... Einsätzen stehen, dürfen daher in  solchen Fällen nicht berücksichtigt werden.

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_74`)


Da mit den von der  Besteuerung ausgenommenen Taggelder in Zusammenhang mit dem Kurzzeiteinsatz für  Frontex auch die laut Reisekosten-Beilage gesondert beantragten Kilometer-/ und Taggeld iHv  355,15 € abgerechnet wurden steht eine weitere pauschalierte Vergütung nicht zu, daher  wurden mit Beschwerdevorentscheidung vom 13.12.2021 alle in Zusammenhang mit dem  Frontex-Einsatz stehenden weiteren Werbungskosten nicht berücksichtigt.“

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_76`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Beschwerdeführer (Bf.) ist Polizist und wurde gemäß § 39a BDG in der Zeit 26. Februar 2025  an Frontex entsendet und war im Auslandseinsatz in Sizilien.

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_84`)


Die An- und Rückreisekosten zum Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ersetzt.

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_119`)


Der Bf. wurde gemäß § 39a BDG an Frontex für die Zeit vom 26. Februar 2025  entsendet und war  für Frontex im Ausland tätig;


Der Bf. wurde gemäß § 39a BDG an Frontex für die Zeit vom 26. Februar 2025  entsendet und war  für Frontex im Ausland tätig;

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |
| `Frontex` | `Frontex` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_136`)


Frontex unterscheidet bei den „Reimbursement Rules“ (Rückerstattungsvereinbarungen):  https://etendering.ted.europa.eu/document/document-file-download.html?docFileId=69347 )  zwischen Taggeldern und Reisekostenersätzen.

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_6`)

**False Positives:**


Über Aufforderung der belangten Behörde gliederte der Bf. die Reisekosten wie folgt auf:  Einsätze für die Grenzschutzagentur Frontex: versteuerte Taggelder  Einsatz im Jahr 2018 als Frontex-Beamter in  Sardinien (I) vom 04.06.

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Frontex` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_10`)

**False Positives:**


Einsatz im Jahr 2019 als Frontex-Beamter in  Sizilien (I) vom 16.07.

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_25`)

**False Positives:**


Frontex-Einsatz: Anreise  zumFlugh.

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_28`)

**False Positives:**


Frontex-Einsatz in Sizilien  (Trapani) 31 x Frühstück a'  5,85   181,35  181,35  18.08.

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Trapani` (city)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_43`)

**False Positives:**


Zur Reisezulage:  Im Kalenderjahr 2019 war ich einmal für die Organisation "Europäische Grenzschutzagentur  Frontex" in Trapani auf der Insel Silzilien (I) tätig.

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Europäische Grenzschutzagentur  Frontex` (organisation)
- `Trapani` (city)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_46`)

**False Positives:**


Für die Tätigkeit  bei der "Europäischen Grenzschutzagentur Frontex" wird eine Reisezulage in der Höhe von 98,--  Euro täglich gewährt.

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Europäischen Grenzschutzagentur Frontex` (organisation)

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_63`)

**False Positives:**


Somit wurden von den beantragten 485,15€ alle in  Zusammenhang mit dem Frontex-Einsatz stehenden Werbungskosten nicht berücksichtigt  (485,15€ - 355,15€).

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_65`)

**False Positives:**


Werbungskosten berücksichtigt werden, da auch diese Kosten im Zusammenhang mit dem  Frontex-Einsatz stehen.“

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_67`)

**False Positives:**


Die Kürzung der Reisekosten um die Aufwendungen iZm dem Frontex-Einsatz seien nicht  gerechtfertigt, da diese Dienstreisen ausschließlich im Rahmen der Tätigkeit bei der  Kriminalpolizei in Österreich getätigt worden seien.

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Kriminalpolizei in Österreich` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_74`)

**False Positives:**


Da mit den von der  Besteuerung ausgenommenen Taggelder in Zusammenhang mit dem Kurzzeiteinsatz für  Frontex auch die laut Reisekosten-Beilage gesondert beantragten Kilometer-/ und Taggeld iHv  355,15 € abgerechnet wurden steht eine weitere pauschalierte Vergütung nicht zu, daher  wurden mit Beschwerdevorentscheidung vom 13.12.2021 alle in Zusammenhang mit dem  Frontex-Einsatz stehenden weiteren Werbungskosten nicht berücksichtigt.“

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Frontex` (organisation)

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_75`)

**False Positives:**


Mit E-Mail vom 28.03.2022 teilte der Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum Flughafen München mit dem privat PKW ohne entsprechende Belege laut Anweisung des  BMI (National Frontex Point of Contact) nicht refundiert worden seien, deshalb seien diese  Kosten als Werbungskosten im Rahmen der Arbeitnehmerveranlagung geltend gemacht  worden.

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Flughafen München` (organisation)
- `BMI` (organisation)

</details>

---

## `Lexdon IT`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Lexdon IT'.

**Content:**
```
\bLexdon\s+IT\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 7 | 7 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 7 | 0 | 1523 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_22`)


Zum Stichtag 31.12.2008 ist die Houdek Maschinenbau  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan vom 29.06.2009 gemäß § 39 UmgrStG in einem ersten  Umgründungsschritt als übertragende Gesellschaft (neben anderen Gesellschaften) mit der  Lexdon IT  als übernehmende Gesellschaft verschmolzen worden.

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_25`)


Die Lexdon IT  und  Roelfsen Versicherung  sind aufgrund der dargestellten Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der Houdek Maschinenbau, insoweit das auch nach der Abspaltung zum  31.12.2007 bei der Houdek Maschinenbau  verbliebende Vermögen betroffen ist.

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_30`)


Am 26.04.2013 erließ das FA Wien 1/23  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen gem. § 14 Abs. 2 Z. 1 SpaltG (und der weiteren  Umgründungsschritte) partielle Gesamtrechtsnachfolger der Houdek Maschinenbau  sind und  demgemäß die Bescheide insoweit an die partiellen Gesamtrechtsnachfolger zu richten sind,  als die Einkünfte den abgespaltenen Tankstellen-Teilbetrieben bzw. den verbleibenden  Teilbetrieben bzw. Vermögen zuzuordnen sind.

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_31`)


Der Lexdon IT  als weiterem partiellen  Gesamtrechtsnachfolger wurde ein Körperschaftsteuerbescheid 2007 zugestellt, der einen  Ergebnisanteil von Null mangels Übergang von verlustverursachenden Vermögen auswies.

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_98`)


Im Ergebnis hat das BFG die Rechtsmeinung des Beschwerdeführers geteilt, wonach der bei der  Lexdon IT  im Jahr 2007 insgesamt entstandene Verlust nach Vornahme des  innerbetrieblichen Verlustausgleichs ausschließlich im Zusammenhang mit den übrigen bei der  Houdek Maschinenbau  verbliebenen Tankstellen verbleibt, sodass dieser Verlust zur Gänze zu  negativen Einkünften und infolge dessen zu vortragsfähigen Verlusten führt (vgl. Seite 3 der  Beschwerde vom 31.5.2013 inklusive Gutachten von Univ.-Prof. Dr. Tina Ehrke-Rabel, welches  als integrierender Bestandteil der Beschwerde 31.05.2013 anzusehen ist).

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_223`)


Die Houdek Maschinenbau  selbst wurde Stichtag 31.12.2008 in einem  ersten Schritt mit der Lexdon IT  verschmolzen und erfolgte in einem zweiten  stichtagsgleichen eine Abspaltung zur Aufnahme in die Roelfsen Versicherung  durch Übertragung des  gesamten Betriebes.

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_224`)


Vor diesem Hintergrund sind die Lexdon IT  und die Roelfsen Versicherung  als  Gesamtrechtsnachfolger der Houdek Maschinenbau  zu beurteilen.

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

</details>

---

## `School for Health Care Grillenreith Specific`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches specific long-form school names for health care in Grillenreith with variations (am LKH, in Grillenreith).

**Content:**
```
\bSchule\s+f\u00fcr\s+allgemeine\s+Gesundheits\-\s+und\s+Krankenpflege\s+(?:am\s+LKH\s+|in\s+)?Grillenreith\b|Gesundheits\-\s+und\s+Krankenpflege\-Schule\s+am\s+LKH\s+Grillenreith\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 789 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_6`)


2. In Beantwortung des Ergänzungsersuchens vom 18.10.2019 übermittelte die BF den  Lehrvertrag ihrer Tochter für die Ausbildung zur Steuerassistentin und ein Schreiben der Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith, in dem bestätigt wurde, dass die  Tochter die Schule in der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

| Predicted | Gold |
|---|---|
| `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith` | `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_10`)


Die Bescheidbegründung lautete:   „Ihre Tochter Stella Marschalk, Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith.

| Predicted | Gold |
|---|---|
| `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith` | `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_13`)


4. Gegen diesen Rückforderungsbescheid erhob die BF mit Schriftsatz vom 27.11.2019  Beschwerde, die sie wie folgt begründete: „Da meine Tochter Stella Marschalk, Bakk. techn.  im Oktober  2017 aus gesundheitlichen Gründen die allgemeine Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith  nicht weiterführen konnte, hat sie diese Ausbildung beendet.

| Predicted | Gold |
|---|---|
| `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith` | `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_20`)


Begründend wurde  ausgeführt:   „Frau  Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith  in Ausbildung zur Krankenpflegerin.

| Predicted | Gold |
|---|---|
| `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith` | `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_26`)


Dem Vorlageantrag beigelegt war ein Schreiben der Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith, in dem bestätigt wurde, dass Stella Marschalk, Bakk. techn.  die Schule in  der Zeit vom 01.10.2016 bis 04.10.2017 absolviert habe.

| Predicted | Gold |
|---|---|
| `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith` | `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/131197.1_29`)


Die Tochter der BF absolvierte in der Zeit vom 01.10.2016 bis 04.10.2017 die Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith.

| Predicted | Gold |
|---|---|
| `Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith` | `Schule für  allgemeine Gesundheits- und Krankenpflege in Grillenreith` |

</details>

---

## `Flughafen München`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Flughafen München' and variations with spaces.

**Content:**
```
\bFlughafen\s+M\u00fcnchen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 231 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_75`)


Mit E-Mail vom 28.03.2022 teilte der Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum Flughafen München mit dem privat PKW ohne entsprechende Belege laut Anweisung des  BMI (National Frontex Point of Contact) nicht refundiert worden seien, deshalb seien diese  Kosten als Werbungskosten im Rahmen der Arbeitnehmerveranlagung geltend gemacht  worden.

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_83`)


Der Bf. macht Werbungskosten geltend, die im Zusammenhang mit dem Auslandseinsatz  stehen und zwar Frühstückskosten iHv € 181,35, sowie An- und Rückreisekosten zum Flughafen  München iHv € 173,80.

| Predicted | Gold |
|---|---|
| `Flughafen  München` | `Flughafen  München` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_84`)


Die An- und Rückreisekosten zum Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ersetzt.

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_127`)


II. Zu den Frühstücks- und Reisekosten:  In Streit steht die Rechtsfrage, ob pauschale Frühstückskosten sowie die An- und  Rückreisekosten zum Flughafen München als Werbungskosten im Zusammenhang mit der  Auslandstätigkeit des Bw., für die er eine steuerfreie Auslandszulage iSd § 21 Gehaltsgesetz  erhalten hat, zu berücksichtigen sind.

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_139`)


Die Kosten für die Fahrt  zwischen Wohnort und Flughafen München, die der Bf. mit dem eigenen PKW zurückgelegt  hat, wurden nicht ersetzt.

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_141`)


Der Beschwerde war daher teilweise Folge zu geben und die An- und Rückreisekosten zum  Flughafen München in Höhe von € 173,80 zum Abzug zuzulassen.

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

</details>

---

## `University of Bristol`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'University of Bristol' specifically.

**Content:**
```
\bUniversity\s+of\s+Bristol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 663 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_26`)


Die Tochter studiert an der University of Bristol bis voraussichtlich Juli 2023.

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_30`)


Bis Mai 2019 lebte die Tochter bei ihrer Mutter in Großbritannien, danach bei dem Onkel ihres  Stiefvaters (ebenfalls in GB), der in diesem Zeitpunkt auch die Unterhaltskosten getragen hat  und ab September 2020 in einem Studentenwohnheim der University of Bristol.

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_66`)


Am 11. Dezember 2020 bestätigte die University of Bristol, that Miss Maximiliane Sakschewsky, MA (Tochter  des Bf.) student no.

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_67`)


2…7 is studying for a Chemistry (BSc) full time at the University of Bristol.

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_68`)


Miss Maximiliane Sakschewsky, MA … started at the University of Bristol on 28 September 2020 and is  expected to complete her course on 9 June 2023.

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_74`)


Im September 2020 nahm Maximiliane Sakschewsky, MA  an der University of  Bristol ein full time- Studium auf.

| Predicted | Gold |
|---|---|
| `University of  Bristol` | `University of  Bristol` |

</details>

---

## `Schabetsberger Steuerberatung GmbH`

**F1:** 0.007 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'Schabetsberger Steuerberatung GmbH' specifically.

**Content:**
```
\bSchabetsberger\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.007 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 20 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_51`)


Beide Bescheide (der an das  Finanzamt Österreich adressierte Pfändungsescheid vom 3.4.2024 ergänzt um die Anmerkung  „Ausfertigung für den Abgabenschuldner“) wurden der Beschwerdeführerin am 5.4.2024 zu  Handen der Schabetsberger Steuerberatung GmbH, Fischerstiege 9, 1010 Wien, zugestellt.

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_54`)


Die Schabetsberger Steuerberatung GmbH leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  Merkur Treuhand Steuerberatung GmbH weiter.

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_63`)


Die Feststellungen zum Sicherstellungsauftrag vom 20.3.2024 und zum Pfändungsbescheid  vom 3.4.2024 gründen sich auf eine Einsichtnahme in den Akt RV/702183/2024 des  Bundesfinanzgerichtes (dort bekämpft die Beschwerdeführerin den Pfändungsbescheid vom  3.4.2024), insbesondere auf den Zustellnachweis (Rückschein) zum Sicherstellungsauftrag vom  20.3.2024 und zum Pfändungsbescheid vom 3.4.2024, worin ein Mitarbeiter oder eine  Mitarbeiterin (Unterschrift unleserlich) der Schabetsberger Steuerberatung GmbH die  Übernahme dieser beiden Bescheide am 5.4.2024 bestätigt, sowie auf das Schreiben der  Merkur Treuhand Steuerberatung GmbH vom 13.3.2024 und die damit übermittelte Vollmacht  vom 11.3.2024.

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_108`)


Gleichzeitig wurden alle bis dahin beim  Finanzamt erliegenden Vollmachten (daher auch eine allfällige Zustellvollmacht der  Schabetsberger Steuerberatung GmbH) aufgelöst.

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_114`)


Die Zustellung an die Schabetsberger  Steuerberatung GmbH war unwirksam.

| Predicted | Gold |
|---|---|
| `Schabetsberger  Steuerberatung GmbH` | `Schabetsberger  Steuerberatung GmbH` |

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_121`)


Die hier geschehene Übermittlung der eingescannten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail der Schabetsberger  Steuerberatung GmbH vom 16.4.2024 an die Merkur Treuhand Steuerberatung GmbH konnte  daher keine Heilung der unwirksamen Zustellung bewirken.

| Predicted | Gold |
|---|---|
| `Schabetsberger  Steuerberatung GmbH` | `Schabetsberger  Steuerberatung GmbH` |

</details>

---

## `Verfassungsgerichtshof`

**F1:** 0.007 | **Precision:** 0.273 | **Recall:** 0.003  

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
| 0.273 | 0.003 | 0.007 | 22 | 6 | 16 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 16 | 1577 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_51`)


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated_TRAIN/149418.1_33`)


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/149708.1`) ( sent_id: `findok-manually-annotated_TRAIN/149708.1_2`)


Gegen diesen Beschluss ist gemäß § 30a Abs. 3 VwGG eine Revision an den  Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  Verfassungsgerichtshof (§ 88a Abs. 2 VfGG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/149863.1`) ( sent_id: `findok-manually-annotated_TRAIN/149863.1_50`)


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_84`)


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149379.1`) ( sent_id: `findok-manually-annotated_TRAIN/149379.1_65`)


Eine Einschränkung finden diese Überlegungen insoweit, als nach der Rechtsprechung des  Verfassungsgerichtshofes (vgl VfGH 05.03.1979, B 175/76), welcher sich der  Verwaltungsgerichtshof (vgl VwGH 13.02.1991, 90/13/0161;

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshofes` | `Verfassungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**


Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_172`)

**False Positives:**


Der Verfassungsgerichtshof ist bei der o.a, Entscheidung zum Ergebnis gelangt, dass ein  derartiger Fall, nämlich wenn eine Entscheidung derselben Behörde für einen früheren  Steuerzeitraum, die sich in der rechtlichen Würdigung des Sachverhaltes direkt auf einen  (einen späteren Steuerzeitraum betreffenden) Bescheid auswirkt, in gleicher Weise behandelt  werden muss, wie der Fall der Vorfrage;

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**


Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_293`)

**False Positives:**


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)


2.4 Zitierte Entscheidung des Verfassungsgerichtshofes gegenständlich nicht einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des Verfassungsgerichtshofes (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme grundsätzlich auch dann erfolgen, wenn eine  Vorfrage im klassischen Sinne nicht vor liege;

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_295`)

**False Positives:**


Im der  zitierten Entscheidung des Verfassungsgerichtshofes zugrundeliegenden Sachverhalt war  strittig, ob bei nachträglicher Aktivierung eine beantragte Wiederaufnahme für die Folgejahre  zwecks Berücksichtigung der AfA vorzunehmen ist.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_301`)

**False Positives:**


Erst der Verfassungsgerichtshof kam zu dem  Ergebnis, dass in diesem Fall ein Wiederaufnahmegrund vorliege bzw eine Wiederaufnahme zu  verfügen sei, um ein gleichheitskonformes Ergebnis zu erreichen.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_313`)

**False Positives:**


- Weiters wurde vom Verfassungsgerichtshof aufgezeigt, dass eine Nichtwiederaufnahme im  Hinblick auf die Jahre 1975 und 1976 auch dem Grundsatz von Treu und Glauben  widersprechen würde, da sich die Abgabepflichtigen auf die ursprüngliche rechtliche  Beurteilung der Behörde verlassen haben.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_316`)

**False Positives:**


Im Ergebnis zeigt sich, dass eine Erweiterung der Regelung des § 303 BAO auch vom  Verfassungsgerichtshof nur in bestimmten Ausnahmefällen angedacht ist.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_385`)

**False Positives:**


Die Parallelität zum vom Verfassungsgerichtshof entschiedenen Fall ergibt  sich daraus, dass nach dem gegenüber der Beschwerdeführerin ergangenen und in Rechtskraft  erwachsenen Bescheid vom 7.3.2016 gegenüber (auch) der Beschwerdeführerin eine anders  lautende Gerichtsentscheidung ergangen ist, nach welcher der Bescheid vom 7.3.2016 so nicht  ergehen hätte dürfen, da die vom BFG gelöste, vom Finanzamt aufgrund der Bindungswirkung  dem Bescheid zugrunde gelegte Rechtsfrage, nachträglich höchstgerichtlich anders beurteilt  bzw. entschieden wurde.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_51`)

**False Positives:**


die Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem Verfassungsgerichtshof  oder vor dem Gerichtshof der Europäischen Union.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149863.1_50`)

**False Positives:**


Darüber hinaus hat der Verfassungsgerichtshof in seinem Beschluss vom 19. September 2025  zu E 1733/2025 bereits festgehalten, dass in Bezug auf § 16 Abs. 1 COFAG-NoAG keine  verfassungsrechtlichen Bedenken bestehen, war doch vor Erlassung dieser Bestimmung  aufgrund allgemeiner zivilrechtlicher Bestimmungen davon auszugehen, dass rechtsgrundlos  ausbezahlte Geldleistungen seitens der COFAG mit einer dem Gesetz (vgl. insbesondere § 1000  ABGB und § 1333 ABGB) entsprechenden Verzinsung vom Empfänger rückzuerstatten sind, und  gebietet ferner das Unionsrecht, dass dem Unionsrecht zuwiderlaufende Beihilfen mit einer  angemessenen Verzinsung zurückzuzahlen sind.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**
- `COFAG` (organisation)

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_53`)

**False Positives:**


Wenn sich die Bf. dadurch benachteiligt fühlt, dass der Prüfungstermin ohne ihre  Einflussmöglichkeit bereits für Mai 2022 angesetzt wurde, ist ihr Folgendes entgegenzuhalten:  Der Verfassungsgerichtshof hat wiederholt zum Ausdruck gebracht, dass der rechtspolitische  Gestaltungsspielraum des Gesetzgebers bei staatlichen Beihilfen, selbst wenn sie hoheitlich  gewährt werden (zur Familienbeihilfe vgl.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_65`)

**False Positives:**


Eine Verfassungswidrigkeit, die es gebieten würde, die Norm zunächst bis zu einer  Entscheidung des Verfassungsgerichtshofes unangewendet zu lassen, kann das  Bundesfinanzgericht nicht erkennen.

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149418.1_33`)

**False Positives:**


Nach Art 89 Abs 2 B-VG iVm Art 135 Abs hat ein Verwaltungsgericht dann, wenn es gegen  die Anwendung eines Gesetzes aus dem Grund der Verfassungswidrigkeit Bedenken hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim Verfassungsgerichtshof zu stellen.

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_84`)

**False Positives:**


Soweit der Beschwerdeführer die Verfassungswidrigkeit des Progressionsvorbehaltes im Blick  hat, wird darauf hingewiesen, dass dieser bereits - unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom Verfassungsgerichtshof geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH 29.3.1962, B 274/61;

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

</details>

---

## `King's School`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'King's School' and 'The King's School' variations.

**Content:**
```
\b(?:The\s+)?King['\u00b4]s\s+School(?:\s+[A-Z][a-zA-Z]+)?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 667 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_12`)


Dort besuchte Maximiliane Sakschewsky, MA  ab Herbst 2014 das King's School.

| Predicted | Gold |
|---|---|
| `King's School` | `King's School` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

| Predicted | Gold |
|---|---|
| `King's School` | `King's School` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_41`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.

| Predicted | Gold |
|---|---|
| `The King´s School Worcester` | `The King´s School Worcester` |
| `The King's  School Worcester` | `The King's  School Worcester` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_71`)


Diese Feststellung beruht auf folgenden Umständen:  Maximiliane Sakschewsky, MA  war vom September 2014 bis Juli 2020 Schülerin der King's School Worcester,  Großbritannien.

| Predicted | Gold |
|---|---|
| `King's School Worcester` | `King's School Worcester` |

</details>

---

## `Raiffeisenbank Karnische Rion Bankstelle St.Stefan`

**F1:** 0.006 | **Precision:** 1.000 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches the specific bank name 'Raiffeisenbank Karnische Rion Bankstelle St.Stefan' handling potential line breaks or extra spaces.

**Content:**
```
\bRaiffeisenbank\s+Karnische\s+Rion\s+Bankstelle\s+St\.Stefan\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.003 | 0.006 | 5 | 5 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 0 | 991 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_13`)


Die belangte Behörde forderte den Beschwerdeführer mit Schreiben vom 08.11.2022 auf,  Nachweise zu erbringen, die belegen, dass dieser nicht Kontoinhaber des Kontos mit der  AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  sei.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_36`)


Der Beschwerdeführer wurde mit Beschluss vom 06.06.2024 aufgefordert einen Nachweis bis  zum 24.06.2024 darüber zu erbringen, dass es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der  Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  um kein ODER-Konto, sondern ein UND-Konto handle.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_39`)


Der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  wurde der Bescheid vom 10.10.2022 zugestellt und aufgetragen, die  gepfändeten Forderungen nicht mehr an den Abgabenschuldiger auszuzahlen.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_41`)


Der Beschwerdeführer ist Kontoinhaber des Kontos mit der AT78 2024 1897 7421 2903  bei der  Raiffeisenbank Karnische Rion  Bankstelle St.Stefan.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145133.1_45`)


Die Feststellungen hinsichtlich der Kontoinhaberschaft des Beschwerdeführers betreffend  Konto AT78 2024 1897 7421 2903  bei der Raiffeisenbank Karnische Rion  Bankstelle St.Stefan  gründen sich auf die Kontenregisterauskunft.

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

</details>

---

## `PVA Abbreviation`

**F1:** 0.006 | **Precision:** 0.714 | **Recall:** 0.003  

**Format:** `regex`  
**Description:**
Matches 'PVA' (Public Health Insurance) as an organization.

**Content:**
```
\bPVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.714 | 0.003 | 0.006 | 7 | 5 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 5 | 2 | 1321 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_10`)


In ihrer Beantwortung vom 27.11.2019 gab die Bf an, dass die nicht vom Eigeneinkommen der  Mutter der Bf gedeckten Heimkosten von der Bezirkshauptmannschaft Bludenz getragen  werden würden, welche auch die von der PVA einbehaltenen Beträge (das waren die selbst zu  tragende Kosten) erhalten würde.

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_13`)


Dazu wurden von der Bf Bestätigungen der PVA, dem SeneCura Laurentius-Park Bludenz und  diverse Arzthonorare von Fachärzten für Nervenheilkunde vorgelegt.

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_63`)


Davon wurde ein Selbstbetrag von der PVA direkt  an den Kostenträger zur teilweisen Deckung der Verpflegungskosten iHv 1.086,53 Euro  überwiesen.

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_64`)


Der Restbetrag (lt Verständigung über die Leistungshöhe zum 01.01.2017 der PVA  war dies ein Betrag von ca 200,00 bis 230,00 Euro) verblieb bei der Mutter der Bf als  „Taschengeld“.

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_80`)


2. Beweiswürdigung  Der Sachverhalt ist grundsätzlich unstrittig und ergibt sich als solcher aus dem Akt,  insbesondere den angeführten Aktenteilen wie den Bestätigungen der PVA, des SeneCura  Laurentius Park Bludenz und den Kontoauszügen.

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_11`)

**False Positives:**


Die selbst zu tragenden Kosten hätten sich  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst SENECURA 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).

FP: `PVA` (organisation)

**✅ Gold Entities:**
- `SENECURA` (organisation)
- `SENECURA` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_12`)

**False Positives:**


Für 2017: Mobiler Hilfsdienst SENECURA 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 sowie eigene Arztkosten der Bf 633,76 Euro.

FP: `PVA` (organisation)

**✅ Gold Entities:**
- `SENECURA` (organisation)

</details>

---

## `Bankhaus Entity`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches entities starting with 'Bankhaus' followed by a name.

**Content:**
```
\bBankhaus\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df\-]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 877 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_11`)


für Wohnraumschaffung, das Pendlerpauschale und die Kosten für doppelte Haushaltsführung  und Familienheimfahrten näher zu erläutern und zu belegen, übermittelte der  Beschwerdeführer eine Reihe von Urkunden, darunter ein Kreditantrag an die Bankhaus Denzel  vom 7.9.2000, einen Kfz-Zulassungsschein und eine Auflistung der Fahrten vom  Familienwohnsitz in Ungarn nach Wien und zurück sowie der Fahrten von seinem Quartier in  Wien zum jeweiligen Arbeitsort und zurück.

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_50`)


Zu den  Kosten der Wohnraumschaffung bzw. -sanierung legte er nochmals die bereits übermittelten  Kreditunterlagen aus dem Jahr 2000 sowie ein Schreiben der Bankhaus Denzel  vom 26.3.2015 vor,  worin ihm mitgeteilt wird, dass auf dem Kreditkonto ein Saldo i.H.v. € 23.904,50 (inkl. Zinsen  sowie Anwalts- und Gerichtskosten) unberichtigt aushaftet und er aufgefordert wird, die  monatlichen Einzahlungen i.H.v. € 200,00 ab sofort auf dieses Kreditkonto vorzunehmen.

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_73`)


Im Jahr 2000 nahm der Beschwerdeführer einen Kredit über ATS 300.000,00 bei der  Bankhaus Denzel  zum Zwecke eines Hausbaues in Ungarn auf.

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_90`)


Die Feststellungen zum Kredit ergeben sich aus den vom Beschwerdeführer vorgelegten  Unterlagen, nämlich dem Kreditantrag vom 7.9.2000, der Selbstauskunft vom 31.8.2001 und  dem Schreiben der Bankhaus Denzel  vom 26.3.2015.

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

</details>

---

## `BMI`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

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
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 237 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_66`)


Mit Schriftsatz vom 07. Jänner 2022 stellte der Bf. einen Vorlageantrag in welchem er  zusätzlich zu dem Vorbringen in der Beschwerde noch angibt, dass eine weitere Möglichkeit für  die steuerfreie Berücksichtigung der € 2.114,80 ein berichtigter Lohnzettel des BMI wäre.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_75`)


Mit E-Mail vom 28.03.2022 teilte der Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum Flughafen München mit dem privat PKW ohne entsprechende Belege laut Anweisung des  BMI (National Frontex Point of Contact) nicht refundiert worden seien, deshalb seien diese  Kosten als Werbungskosten im Rahmen der Arbeitnehmerveranlagung geltend gemacht  worden.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_84`)


Die An- und Rückreisekosten zum Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ersetzt.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144072.1_93`)


Dem Erkenntnis des  Verwaltungsgerichtshofes vom 4. November 2020, Ra 2020/16/0039-6, liegt die  Grundausbildungsverordnung-Exekutivdienst BMI des Bundesministers für Inneres, BGBl. II  vom 12. Juni 2017, zu Grunde.

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

</details>

---

## `Lubomir Merschmeyer`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Lubomir Merschmeyer'.

**Content:**
```
\bLubomir\s+Merschmeyer\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 1543 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_2`)


Kff. Sandra Khartchenko  als Rechtsnachfolger der Roelfsen Versicherung, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten durch  BDO Austria GmbH WP- u. StBges.       und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der Lubomir Merschmeyer, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch  LeitnerLeitner GmbH Wirtschaftsprüfer und Steuerberater, Ottensheimer Straße 32,  4040 Linz,

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_7`)


Kff. Sandra Khartchenko  als RNF der Roelfsen Versicherung  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der Lubomir Merschmeyer

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_11`)


Bescheidadressaten waren  sowohl das Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_419`)


Die RgR Dipl. Kff. Sandra Khartchenko (im Beschwerdezeitraum Gözcü Getränke) war im Jahr 2010 Gruppenmittglied  der Unternehmensgruppe mit dem Gruppenträger Magdalena Diegmueller, LLB (vormals Lubomir Merschmeyer).

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

</details>

---

## `Finanzamt Wien 1/23 Genitive`

**F1:** 0.005 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Finanzamtes Wien 1/23' specifically.

**Content:**
```
\bFinanzamtes\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.005 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 1355 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149861.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Rut Frühoff  in der Beschwerdesache Albert Sondersorg,  Eggenburger Gasse 7, 9121 Rakollach, Österreich, vertreten durch Deloitte Tax Wirtschaftsprüfungs GmbH, Renngasse  1/Freyung, 1010 Wien, über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend  Einkommensteuer 2010 und über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  Finanzamtes Wien 1/23 (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend  Einkommensteuer 2011, Steuernummer 20-968/1669  zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

</details>

---

## `Finanzamt Wien with Variable Districts`

**F1:** 0.005 | **Precision:** 0.800 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt' or 'Finanzamtes' followed by 'Wien' and variable district numbers (e.g., 9/18/19, 3/6/7/11/15).

**Content:**
```
\bFinanz(?:amt|amtes)\s+Wien\s+\d+(?:/\d+)*\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.800 | 0.002 | 0.005 | 5 | 4 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 1 | 1159 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/138410.1`) ( sent_id: `findok-manually-annotated_TRAIN/138410.1_2`)


Gerald Erwin Ehgartner in der  Beschwerdesache Prof.in Klara Dolejsch, vertreten durch die Prof.in Tamara Simanek, über die Beschwerde vom 2.  November 2020 gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg (nunmehr  zuständig: Finanzamt Österreich) vom 9. September 2020 betreffend Abweisung des Antrags  auf Wiedereinsetzung in den vorigen Stand gemäß § 308 BAO zu Recht:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_13`)


Mit den gegenständlich angefochtenen Einkommensteuerbescheiden für die Jahre 2001 bis  2003 vom 21.12.2011 setzte das Finanzamt Wien 9/18/19 Klosterneuburg (FA 07) die  Einkommensteuer des Beschwerdeführers (Bf.) u.a. unter Berücksichtigung der  Grundlagenbescheide vom 9.11.2011 betreffend Mitunternehmerschaft (atypisch stillen  Beteiligung) an der INET Internet Service GmbH und Mitges., St.nr.: ***, (Beteiligung in den  Streitjahren) fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Alois Ahl  in der Beschwerdesache Romana van Straaten, MBA,  Seeanlage Straße V 4p, 9335 St. Johann am Pressen, Österreich, vertreten durch Dr. Anna Schlosser-Péter, Kurrentgasse 6/3, 1010  Wien, über die Beschwerden vom 23. März 2015 gegen die Bescheide des Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf (heute zuständig: Finanzamt Österreich) vom 17. März 2015  betreffend Einkommensteuer (Arbeitnehmerveranlagung) 2011 und 2012, Steuernummer  38-795/8528, zu Recht erkannt:   I. Den Beschwerden wird gemäß § 279 BAO teilweise Folge gegeben.

FP: `Finanzamtes Wien  3/6/7/11/15 Schwechat` (organisation)

**✅ Gold Entities:**
- `Univ.-Prof. Alois Ahl` (person)
- `Romana van Straaten, MBA` (person)
- `Seeanlage Straße V 4p, 9335 St. Johann am Pressen, Österreich` (address)
- `Dr. Anna Schlosser-Péter` (person)
- `Kurrentgasse 6/3, 1010  Wien` (address)
- `Finanzamtes Wien  3/6/7/11/15 Schwechat Gerasdorf` (organisation)
- `Finanzamt Österreich` (organisation)
- `38-795/8528` (tax_number)

</details>

---

## `University Full Names Generalized`

**F1:** 0.004 | **Precision:** 0.111 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Universität' or 'Hochschule' followed by a location, stopping strictly before verbs, prepositions, or the word 'Name'.

**Content:**
```
\b(?:Universität|Hochschule)\s+[A-Z][a-zA-Z\s\u00e4\u00f6\u00fc\u00df]+?(?=\s*(?:vom|am|von|ist|hat|wurde|sind|waren|und|sowie|als|an|mit|der|die|das|ein|eine|einem|einer|den|die|dem|des|zur|im|um|zu|bei|nach|\u00fcber|unter|ohne|neben|zwischen|gegen|durch|seit|bis|vor|hinter|\(|,|\.|$|Name))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.111 | 0.002 | 0.004 | 36 | 4 | 32 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 32 | 1672 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_73`)


Das Bundesfinanzgericht hat erwogen  Sachverhalt   T. war vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  Universität Wien im Diplomstudium Rechtswissenschaften (UA101) inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_134`)


Zusammenfassend wird Folgendes festgestellt:  Zufolge der Aktenlage war T. vom Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der Universität Wien im Diplomstudium Rechtswissenschaften inskribiert.

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_4`)

**False Positives:**


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

FP: `Universität Wien inskribiert` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_46`)

**False Positives:**


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

FP: `Universität Wien betrieben` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_10`)

**False Positives:**


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

FP: `Universität Wien ab` (organisation)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

FP: `Hochschule Wien` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)
- `Pädagogischen Hochschule Wien` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_27`)

**False Positives:**


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

FP: `Universität Wien sei folgende Formulierung` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_54`)

**False Positives:**


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

FP: `Universität Wien in` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Universität Wien` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_57`)

**False Positives:**


Nach vier inskribierten Semestern (ab WS 2022/23) wechselte T. auf die Pädagogische  Hochschule Wien und inskribierte in der Studienrichtung LA Primarstufe (PM098).

FP: `Hochschule Wien` (organisation)

**✅ Gold Entities:**
- `Pädagogische  Hochschule Wien` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated_TRAIN/144562.1_116`)

**False Positives:**


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

FP: `Universität Wien betriebenen Studi` (organisation)


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

FP: `Hochschule Wien` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)
- `Pädagogische Hochschule Wien` (organisation)

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_4`)

**False Positives:**


T. war vom Wintersemester 2015/2016 bis einschließlich Sommersemester 2018 und vom  Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der Universität Wien inskribiert.

FP: `Universität Wien inskribiert` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_46`)

**False Positives:**


Ihre Tochter T. hat von Wintersemester 2015/2016 bis einschließlich Sommersemester 2018  und von Wintersemester 2019/2020 bis einschließlich Sommersemester 2020 das Studium  Rechtswissenschaften an der Universität Wien betrieben.

FP: `Universität Wien betrieben` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_10`)

**False Positives:**


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

FP: `Universität Wien ab` (organisation)


Abweisungsbescheid vom 28. April 2023  Das Finanzamt stellte folgenden Sachverhalt fest:  T. brach nach vier Semestern das Lehramtsstudium an der Universität Wien ab und begann im  Wintersemester 2022/2023 an der Pädagogischen Hochschule Wien mit dem Bachelorstudium  Lehramt Primarstufe.

FP: `Hochschule Wien` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)
- `Pädagogischen Hochschule Wien` (organisation)

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_27`)

**False Positives:**


Auf der Homepage der Universität Wien sei folgende Formulierung zu finden:  „Wird das Studium erst später gewechselt, entfällt die Familienbeihilfe für so viele Semester,  wie in den vor dem Wechsel betriebenen Studien Familienbeihilfe bezogen wurde.

FP: `Universität Wien sei folgende Formulierung` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_54`)

**False Positives:**


Das Bundesfinanzgericht hat erwogen  Folgender unstrittige Sachverhalt ergibt sich aus dem Familienbeihilfenakt:  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der Universität Wien in der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde und UF Spanisch  (Bachelorstudium) inskribiert und wies für das 1.

FP: `Universität Wien in` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_57`)

**False Positives:**


Nach vier inskribierten Semestern (ab WS 2022/23) wechselte T. auf die Pädagogische  Hochschule Wien und inskribierte in der Studienrichtung LA Primarstufe (PM098).

FP: `Hochschule Wien` (organisation)

**✅ Gold Entities:**
- `Pädagogische  Hochschule Wien` (organisation)

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144562.1_116`)

**False Positives:**


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

FP: `Universität Wien betriebenen Studi` (organisation)


Im Beschwerdefall steht zweifelsfrei und unstrittig fest, dass durch den Wechsel des an der  Universität Wien betriebenen Studiums (LA Sekundarstufe UF Biologie und Umweltkunde und  UF Spanisch) nach vier Semestern (WS 2020/21, SS 2021, WS 2021/22, SS 2022) zum Studium  LA Primarstufe (PM098) an die Pädagogische Hochschule Wien ein schädlicher Studienwechsel  iSd § 17 Abs. 1 Z 2 StudFG vorliegt.

FP: `Hochschule Wien` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)
- `Pädagogische Hochschule Wien` (organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_12`)

**False Positives:**


 Studienerfolgsnachweis der Johannes Kepler Universität Linz (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften (Studienplan in  der Fassung 2018W), aus welcher hervorgeht, dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der JKU Linz absolviert wurden und dass an der WU Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der JKU Linz  angerechnet wurden

FP: `Universität Linz` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_27`)

**False Positives:**


Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung Viktoria Immohr“  vor:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

FP: `Universität Linz` (organisation)

**✅ Gold Entities:**
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)

**False Positives:**


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

FP: `Universität Linz` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Johannes Kepler Universität Linz` (organisation)

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_47`)

**False Positives:**


Dem Vorlageantrag lagen bei:   E-Mail des Zulassungsservices Lehr- und Studienorganisation der Johannes Kepler  Universität Linz vom 01.12.2021 mit dem Betreff „Vergleichbarkeitsprüfung  Viktoria Immohr“:  „Nach Überprüfung ob es sich bei BA Sozial- und Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der JKU um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: Vergleicht man die Qualifikationsprofile der  beiden Studien, so kann von einer grundsätzlichen Gleichwertigkeit des Studiums  ausgegangen werden.

FP: `Universität Linz` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler  Universität Linz` (organisation)
- `Viktoria Immohr` (person)
- `WU  Wien` (organisation)
- `JKU` (organisation)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)

**False Positives:**


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

FP: `Universität Linz` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) ( sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)

**False Positives:**


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

FP: `Universität Linz` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

</details>

---

## `Bezirkshauptmannschaft with Location`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches 'Bezirkshauptmannschaft' followed by a location name.

**Content:**
```
\bBezirkshauptmannschaft\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 1323 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_10`)


In ihrer Beantwortung vom 27.11.2019 gab die Bf an, dass die nicht vom Eigeneinkommen der  Mutter der Bf gedeckten Heimkosten von der Bezirkshauptmannschaft Bludenz getragen  werden würden, welche auch die von der PVA einbehaltenen Beträge (das waren die selbst zu  tragende Kosten) erhalten würde.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_24`)


werden und die Heimkosten würden von der Bezirkshauptmannschaft Bludenz getragen.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_67`)


Jener Kostenteil der Pflegeheimkosten der Mutter der Bf, welcher nicht  selbst getragen werden konnte, wurde von der Bezirkshauptmannschaft Bludenz getragen.

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

</details>

---

## `Gözcü Getränke`

**F1:** 0.003 | **Precision:** 1.000 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Gözcü Getränke'.

**Content:**
```
\bGözcü\s+Getr\u00e4nke\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.002 | 0.003 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 1379 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_412`)


Ein Firmenbuchauszug vom 9.7.2024 ergab, dass die Gözcü Getränke  seit 15.5.2024 aufgrund  einer Neufassung des Gesellschaftsvertrages infolge Verkaufs nunmehr RgR Dipl.

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_419`)


Die RgR Dipl. Kff. Sandra Khartchenko (im Beschwerdezeitraum Gözcü Getränke) war im Jahr 2010 Gruppenmittglied  der Unternehmensgruppe mit dem Gruppenträger Magdalena Diegmueller, LLB (vormals Lubomir Merschmeyer).

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_420`)


Die RgR Dipl. Kff. Sandra Khartchenko (im Beschwerdezeitraum Gözcü Getränke) ist als Rechtsnachfolgerin der  Roelfsen Versicherung  auch partielle Rechtsnachfolgerin der Houdek Maschinenbau.

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

</details>

---

## `Company with OG Suffix`

**F1:** 0.003 | **Precision:** 0.600 | **Recall:** 0.002  

**Format:** `regex`  
**Description:**
Matches company names ending in 'OG' (Offene Gesellschaft), handling variations like 'Mur Alver OG'.

**Content:**
```
(?<!\w)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df\s&\-]+?\s+OG)(?=\s*(?:\(|,|\.|$|\s+(?:ist|war|wurde|hat|sind|waren|als|von|an|mit|der|die|das|ein|eine|einem|einer|den|die|dem|des|zur|im|um|zu|bei|nach|\u00fcber|unter|ohne|neben|zwischen|gegen|durch|seit|bis|vor|hinter|Ltd\.|\(|$)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.600 | 0.002 | 0.003 | 5 | 3 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 2 | 1572 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Kay Wrulich in der Beschwerdesache   OStR Richarda Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch Steuerberater Metzler & Adelsberger OG,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom 22. August 2019 gegen die gem. §  293b BAO berichtigten Einkommensteuerbescheide der Jahre 2014 – 2017 des Finanzamtes  Innsbruck (nunmehr Finanzamt Österreich) allesamt vom 22. Juli 2019, Steuernummer  31-785/0303, nach öffentlicher mündlicher Verhandlung zu Recht erkannt:   I. Die angefochtenen Bescheide werden aufgehoben.

| Predicted | Gold |
|---|---|
| `Steuerberater Metzler & Adelsberger OG` | `Steuerberater Metzler & Adelsberger OG` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/135661.1`) ( sent_id: `findok-manually-annotated_TRAIN/135661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerden der  Reinhold Moellenkamp, Höllererweg 4, 2852 Maltern, Österreich, vertreten durch die Achammer & Mennel Rechtsanwälte OG,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des Finanzamtes Feldkirch vom  7. Jänner 2020 betreffend Festsetzung der Kraftfahrzeugsteuer für den Zeitraum 8-10/2019  und Festsetzung der Normverbrauchsabgabe für den Zeitraum 07/2019, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Achammer & Mennel Rechtsanwälte OG` | `Achammer & Mennel Rechtsanwälte OG` |

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/135661.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Ungericht über die Beschwerden der  Reinhold Moellenkamp, Höllererweg 4, 2852 Maltern, Österreich, vertreten durch die Achammer & Mennel Rechtsanwälte OG,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des Finanzamtes Feldkirch vom  7. Jänner 2020 betreffend Festsetzung der Kraftfahrzeugsteuer für den Zeitraum 8-10/2019  und Festsetzung der Normverbrauchsabgabe für den Zeitraum 07/2019, zu Recht erkannt:   Den Beschwerden wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Achammer & Mennel Rechtsanwälte OG` | `Achammer & Mennel Rechtsanwälte OG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_195`)

**False Positives:**


Aus dem Firmenbuch ist ersichtlich, dass der Beschuldigte sowohl Geschäftsführer der GmbH  als auch verantwortlicher Gesellschafter der OG war, somit in den verfahrensgegenständlichen  Zeiträumen Entscheidungsträger der belangten Verbände gewesen ist.

FP: `Beschuldigte sowohl Geschäftsführer der GmbH  als auch verantwortlicher Gesellschafter der OG` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_195`)

**False Positives:**


Aus dem Firmenbuch ist ersichtlich, dass der Beschuldigte sowohl Geschäftsführer der GmbH  als auch verantwortlicher Gesellschafter der OG war, somit in den verfahrensgegenständlichen  Zeiträumen Entscheidungsträger der belangten Verbände gewesen ist.

FP: `Beschuldigte sowohl Geschäftsführer der GmbH  als auch verantwortlicher Gesellschafter der OG` (organisation)

**✅ Gold Entities:**

</details>

---

## `BM für Inneres`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'BM für Inneres'.

**Content:**
```
\bBM\s+f\u00fcr\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 245 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_45`)


Auf den Lohnzettel des BM für Inneres wird verwiesen.

| Predicted | Gold |
|---|---|
| `BM für Inneres` | `BM für Inneres` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_51`)


Der Betrag, welcher vom BM für Inneres als Bezüge gem. § 26 EStG ausbezahlt wird, betrifft  den Kfz-Aufwand, die Miete der Wohnung und sonstigen Reisekosten, wie etwa Fahrkarten  usw., jedoch keine Tagesgelder.

| Predicted | Gold |
|---|---|
| `BM für Inneres` | `BM für Inneres` |

</details>

---

## `Kriminalpolizei in Österreich`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

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
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 242 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_55`)


Die Kürzung betrifft wahrscheinlich die Dienstreisen im Zuge meiner  Tätigkeit bei der Kriminalpolizei in Österreich.

| Predicted | Gold |
|---|---|
| `Kriminalpolizei in Österreich` | `Kriminalpolizei in Österreich` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_67`)


Die Kürzung der Reisekosten um die Aufwendungen iZm dem Frontex-Einsatz seien nicht  gerechtfertigt, da diese Dienstreisen ausschließlich im Rahmen der Tätigkeit bei der  Kriminalpolizei in Österreich getätigt worden seien.

| Predicted | Gold |
|---|---|
| `Kriminalpolizei in Österreich` | `Kriminalpolizei in Österreich` |

</details>

---

## `Arbeits- und Sozialgericht`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Arbeits- und Sozialgericht' and 'Arbeits- und Sozialgericht Wien'.

**Content:**
```
\bArbeits\-\s+und\s+Sozialgericht(?:\s+Wien)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1107 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_49`)


Die Bf hat  nämlich ein für das Arbeits- und Sozialgericht Wien erstelltes berufskundliches  Sachverständigengutachten vom 29. März 2013 vorgelegt, das eine Erwerbsunfähigkeit der Bf  zum Zeitpunkt der Gutachtenserstellung verneint.

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_52`)


Das für das Arbeits- und  Sozialgericht verfasste berufskundliche Sachverständigengutachten ist das von der Bf dem  Bundesfinanzgericht vorgelegte zeitlich früheste Gutachten, das eine Beurteilung der  Erwerbs(un)fähigkeit der Bf enthält.

| Predicted | Gold |
|---|---|
| `Arbeits- und  Sozialgericht` | `Arbeits- und  Sozialgericht` |

</details>

---

## `England Organisation`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'England' as an organisation in legal context.

**Content:**
```
\bEngland\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 669 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_17`)


Maximiliane Sakschewsky, MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in England Advanced Level  genannt - noch ein Jahr im King's School absolvieren müssen.

| Predicted | Gold |
|---|---|
| `England` | `England` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/134209.1_58`)


Am 20. April und 15. Mai 2020 überwies der Bf. an K. H., IBAN GB…1233 jeweils € 400,00  (handschriftlich vom Bf. eingefügt:  Maximiliane Sakschewsky, MA  wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in England).

| Predicted | Gold |
|---|---|
| `England` | `England` |

</details>

---

## `ÖBB Abbreviation`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the organization 'ÖBB' (Österreichische Bundesbahnen).

**Content:**
```
\bÖBB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1315 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_40`)


Weiters wurde auch eine Aufstellung der Kosten,  welche die Tochter zusätzlich noch übernommen hatte (Fahrkarten ÖBB für Besuche,  Betriebskosten der Wohnung in Bludenz, Depotgeld für das Pflegeheim, etc), beigelegt.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_76`)


Belege für die geltend gemachten Besuchskosten wie für die Jahreskarten der ÖBB sowie der  einzelnen Bahn- oder Bustickets bzw Taxirechnungen wurden nicht vorgelegt.

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

</details>

---

## `Finanzamt Neunkirchen Wr. Neustadt Specific`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Finanzamt Neunkirchen Wr. Neustadt' and its genitive form.

**Content:**
```
\bFinanz(?:amt|amtes)\s+Neunkirchen\s+Wr\.\s+Neustadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1227 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149741.1`) ( sent_id: `findok-manually-annotated_TRAIN/149741.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht erkennt durch die Richterin Mag. Lisa Fries in der Beschwerdesache  Corvin Diebald, Pitzelstätten 4, 2490 Ebenfurth, Österreich, vertreten durch Dr. Ronald Rödler, Lagerstraße 5/1/20, 2460  Bruck/Leitha über die Beschwerde vom 11. Oktober 2019 gegen den Bescheid des Finanzamtes  Neunkirchen Wr. Neustadt (nunmehr Finanzamt Österreich) vom 11. September 2019  betreffend Aussetzung gemäß § 212a BAO zu Recht:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes  Neunkirchen Wr. Neustadt` | `Finanzamtes  Neunkirchen Wr. Neustadt` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145534.1_76`)


für die Jahre 2001 bis 2003 wurde vom Finanzamt Neunkirchen Wr.  Neustadt zu Eingangsrechnungen der geprüften Gesellschaften festgestellt, dass diesen seitens  der entsprechenden Geschäftspartner niemals Gegenleistungen gegenübergestanden hätten,  sondern die Erbringung von Leistungen durch die in den Rechnungen angeführten Personen  vorgetäuscht wurden.

| Predicted | Gold |
|---|---|
| `Finanzamt Neunkirchen Wr.  Neustadt` | `Finanzamt Neunkirchen Wr.  Neustadt` |

</details>

---

## `Mag. Ghesla Steuerberater GmbH`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific law firm 'Mag. Ghesla Steuerberater GmbH'.

**Content:**
```
\bMag\.\s+Ghesla\s+Steuerberater\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 988 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

</details>

---

## `Mag. [Name] Steuerberater GmbH`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches generic 'Mag. [Name] Steuerberater GmbH' patterns.

**Content:**
```
\bMag\.\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+\s+Steuerberater\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 988 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Peter Steurer in der Beschwerdesache  Gisbert Lindwedel, Penken 55, 4903 Hofmanning, Österreich, vertreten durch die Mag. Ghesla Steuerberater GmbH, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen die Bescheide des Finanzamtes Bregenz  (nunmehr: Finanzamt Österreich) betreffend Einkommensteuer 2015 und 2016 sowie  Festsetzung von Vorauszahlungen an Einkommensteuer für 2017 sowie 2018 und Folgejahre,  85-106/2625, zu Recht erkannt:   1.

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

</details>

---

## `Sudver Handel Services GMBH Specific`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific company 'Sudver Handel Services GMBH'.

**Content:**
```
\bSudver\s+Handel\s+Services\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |

</details>

---

## `Glanznorost Institut GMBH Specific`

**F1:** 0.002 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific company 'Glanznorost Institut GMBH'.

**Content:**
```
\bGlanznorost\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.002 | 2 | 2 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 0 | 1585 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/134689.1_32`)


Weiters erging mit Bescheiddatum 22.8.2018 hinsichtlich der selben Abgabenansprüche ein  weiterer (inhaltsgleicher) Abgabenfestsetzungsbescheid und zwar neuerlich an die Event Sudkraftlex GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 von der  belangten Behörde versandt wurde.

| Predicted | Gold |
|---|---|
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

</details>

---

## `Pensionsversicherungsanstalt`

**F1:** 0.002 | **Precision:** 0.154 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Pensionsversicherungsanstalt' as an organization.

**Content:**
```
\bPensionsversicherungsanstalt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.154 | 0.001 | 0.002 | 13 | 2 | 11 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 11 | 1264 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) ( sent_id: `findok-manually-annotated_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_41`)

**False Positives:**


Denn beide eine dauerhafte Erwerbsunfähigkeit bejahenden Gutachten beziehen sich  hinsichtlich der Frage des Eintritts der dauerhaften Erwerbsunfähigkeit auf ein von der Bf  vorgelegtes, von der Pensionsversicherungsanstalt in Auftrag gegebenes Gutachten vom 2. Juli  2021: Dieses stellt fest, dass der Bf „aufgrund der reduzierten psychomotorischen  Belastbarkeit und der geringen Stresstoleranz mit mehrfach gescheiterten Arbeitsversuchen  […] keine Tätigkeiten zumutbar [sind]“.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_42`)

**False Positives:**


Eine sich auf das genannte Gutachten der  Pensionsversicherungsanstalt beziehende chefärztliche Stellungnahme vom 6. Juli 2021 hält  fest, dass „das Gesamtleistungskalkül […] für Tätigkeiten auf dem allgemeinen Arbeitsmarkt  vorübergehend mehr als 6 Monate nicht aus[reicht] ab Antragstellung 29.06.2021“.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_45`)

**False Positives:**


Da das für die Pensionsversicherungsanstalt erstellte Gutachten festhält,  dass die Bf „seit ca. 2006 mit Unterbrechung bei Jugend am Werk“ tätig ist, geht die sich auf  das Gutachten der Pensionsversicherungsanstalt beziehende chefärztliche Stellungnahme  davon aus, dass die Bf seit 2006 originär invalid (iSd § 255 Abs. 7 ASVG) ist.

FP: `Pensionsversicherungsanstalt` (organisation)


Da das für die Pensionsversicherungsanstalt erstellte Gutachten festhält,  dass die Bf „seit ca. 2006 mit Unterbrechung bei Jugend am Werk“ tätig ist, geht die sich auf  das Gutachten der Pensionsversicherungsanstalt beziehende chefärztliche Stellungnahme  davon aus, dass die Bf seit 2006 originär invalid (iSd § 255 Abs. 7 ASVG) ist.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149874.1_46`)

**False Positives:**


Vor dem  Hintergrund der Ausführungen des von der Pensionsversicherungsanstalt in Auftrag gegebenen  3 von 6 Seite 4 von 6

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_24`)

**False Positives:**


Neben einer inländischen Rente (Pensionsversicherungsanstalt Wien) bezog er eine Rente der  "Deutschen Rentenversicherung Bund".

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**
- `Pensionsversicherungsanstalt Wien` (organisation)
- `Deutschen Rentenversicherung Bund` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_57`)

**False Positives:**


Weder die Höhe der von der Pensionsversicherungsanstalt ausbezahlten Bezüge noch die Höhe  der Rente von der Deutschen Rentenversicherung Bund und der Versorgungskasse Deutscher  Unternehmen VVaG wurde im Verfahren vom Beschwerdeführer bestritten.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**
- `Deutschen Rentenversicherung Bund` (organisation)
- `Versorgungskasse Deutscher  Unternehmen VVaG` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated_TRAIN/149683.1_58`)

**False Positives:**


Auf den aktenkundigen Lohnzettel der Pensionsversicherungsanstalt sowie den im Akt  aufliegenden Kontrollmitteilungen wird verwiesen.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_24`)

**False Positives:**


Neben einer inländischen Rente (Pensionsversicherungsanstalt Wien) bezog er eine Rente der  "Deutschen Rentenversicherung Bund".

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**
- `Pensionsversicherungsanstalt Wien` (organisation)
- `Deutschen Rentenversicherung Bund` (organisation)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_57`)

**False Positives:**


Weder die Höhe der von der Pensionsversicherungsanstalt ausbezahlten Bezüge noch die Höhe  der Rente von der Deutschen Rentenversicherung Bund und der Versorgungskasse Deutscher  Unternehmen VVaG wurde im Verfahren vom Beschwerdeführer bestritten.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**
- `Deutschen Rentenversicherung Bund` (organisation)
- `Versorgungskasse Deutscher  Unternehmen VVaG` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149683.1_58`)

**False Positives:**


Auf den aktenkundigen Lohnzettel der Pensionsversicherungsanstalt sowie den im Akt  aufliegenden Kontrollmitteilungen wird verwiesen.

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

</details>

---

## `VfGH Abbreviation`

**F1:** 0.002 | **Precision:** 0.050 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'VfGH' (Verfassungsgerichtshof) as an organization.

**Content:**
```
\bVfGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.050 | 0.001 | 0.002 | 40 | 2 | 38 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 38 | 1438 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_46`)


Nach Ansicht des VfGH (zB 29.6.1985, G 42/85 ua;

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149418.1`) ( sent_id: `findok-manually-annotated_TRAIN/149418.1_32`)


Das Bundesfinanzgericht sieht sich nicht veranlasst, die von der Bf in der vorliegenden  Beschwerde geäußerten verfassungsrechtlichen Bedenken an den VfGH zu tragen.

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_156`)

**False Positives:**


Der Verfassungsgerichtshof (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine Vorfrage nicht „klassisch" zu verstehen ist.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_157`)

**False Positives:**


Der VfGH hat in seinem Erkenntnis eine  14 von 39 Seite 15 von 39

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_159`)

**False Positives:**


Dem genannten VfGH-Erkenntnis lag folgender Sachverhalt zu Grunde: Mit  Berufungsentscheidung aus dem Jahr 1984 gab die zuständige FLD der Berufung einer  Gesellschafterin gegen die einheitliche und gesonderte Gewinnfeststellung in der Form statt,  dass die im Erstbescheid bei der Gesellschafterin zur Gänze als Gewinnanteil behandelte  Ablösezahlung mit 2/3 zu aktivieren und auf 6 Jahre verteilt abzuschreiben war.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_162`)

**False Positives:**


Der VfGH bejahte die Anwendbarkeit des Vorfragentatbestandes.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_250`)

**False Positives:**


Dies unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde für einen früheren Steuerzeitraum, die sich in der rechtlichen Würdigung des  Sachverhaltes direkt auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid  auswirke, in gleicher Weise behandelt werden müsse, wie der Fall der Vorfrage.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_328`)

**False Positives:**


Dazu ergänzend wird seitens des Finanzamtes zu den Beschwerdeausführungen wie folgt  Stellung genommen:   Wie bereits in der händischen Begründung der Wiederaufnahme vom 29.01.2019 ausgeführt,  kam der VfGH in seiner Entscheidung B 783/89 vom 6.12.1990 zum Schluss, dass auch eine  Wiederaufnahme des Verfahrens in verfassungsgemäßer Interpretation möglich ist und eine  Vorfrage deshalb auch nicht nur "klassisch" zu verstehen ist.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_329`)

**False Positives:**


D.h. durch die Entscheidung des  VfGH wurden die Wiederaufnahmegründe in ihrem Anwendungsbereich de facto erweitert (so  auch Ritz, 6.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_367`)

**False Positives:**


Lt. Ansicht des Finanzamtes liegt damit auch hier  eine weite Auslegung der Wiederaufnahmebestimmung im Sinn der Rechtsprechung des VfGH  vor (verfassungskonforme Interpretation des § 303 Abs. 1 lit c BAO).

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_383`)

**False Positives:**


Die Wiederaufnahme wurde laut Begründung des angefochtenen Bescheides auf die  verfassungskonforme Auslegung des § 303 Abs. 1 lit c BAO - Wiederaufnahmsgrund laut  Erkenntnis des VfGH vom 6.12.1990, B 783/89 (siehe dazu bei Ritz, BAO, 6.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_454`)

**False Positives:**


Dazu hat der VfGH in seinem Erkenntnis vom 6.12.1990, B 783/89  klargestellt, dass als Vorfragetatbestand bei der Wiederaufnahme des Verfahrens auch ein  neuer Bescheid derselben Abgabenbehörde in einem anderen Verfahren in Betracht kommen  kann (siehe Ritz, BAO 5, § 303, Tz 41;

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_457`)

**False Positives:**


In diesem Erkenntnis des VfGH war die Frage zu lösen, ob die nachträgliche Änderung der  behördlichen Auffassung zur Frage der Aktivierung oder Nichtaktivierung eines Aufwandes für  ein bestimmtes Veranlagungsjahr zur Wiederaufnahme nachfolgender - bereits rechtskräftiger  - Veranlagungsjahre, in denen der selbe Aufwand (im Hinblick auf seine Aktivierung)  Auswirkungen zeitigte, führen kann.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_458`)

**False Positives:**


Der VfGH hat zugestanden, dass die rechtliche Beurteilung  eines Sachverhaltes für ein früheres Steuerjahr keine Vorfrage im technischen Sinn darstellt  und dass nach der Judikatur des VwGH die Änderung der rechtlichen Qualifikation eines  Sachverhaltes keine Tatsache iSd § 303 Abs 1 lit. b BAO darstellt.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_459`)

**False Positives:**


Dennoch hat der VfGH die  Wiederaufnahme des Verfahrens in einer verfassungskonformen Interpretation bejaht.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_466`)

**False Positives:**


Im BAO-Kommentar Ritz/Koran wird dazu ausgeführt: „Mit Erk vom 6.12.1990, B 783/89, hat  der VfGH den Katalog der drei Wiederaufnahmsgründe de facto erweitert.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 14** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_468`)

**False Positives:**


Der VfGH hat zugestanden, dass die rechtliche  Beurteilung eines Sachverhaltes für ein früheres Steuerjahr keine Vorfrage im technischen Sinn  darstellt und dass nach der Judikatur des VwGH die Änderung der rechtlichen Qualifikation  eines Sachverhaltes keine Tatsache iSd § 303 Abs 1 lit b darstellt.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 15** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_469`)

**False Positives:**


Dennoch hat der VfGH den Anspruch auf Bewilligung der Wiederaufnahme in  verfassungskonformer Auslegung des § 303 Abs 1 bejaht, „Es stellte einen unerklärlichen  Wertungswiderspruch dar, wollte man annehmen, daß zwar die Tatsache, daß nachträglich  über eine Vorfrage von einer anderen (hiefür zuständigen) Behörde anders entschieden wurde,  einen Wiederaufnahmsgrund darstellt, nicht aber eine Entscheidung derselben Behörde für  einen früheren Steuerzeitraum, der sich in der rechtlichen Würdigung des Sachverhaltes direkt  auf einen (einen späteren Steuerzeitraum betreffenden) Bescheid auswirkt.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 16** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_472`)

**False Positives:**


Diese Überlegungen des VfGH gelten auch für amtswegige Wiederaufnahmen;

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 17** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_476`)

**False Positives:**


Der VfGH hat mit seiner Entscheidung zwar den Weg geebnet, dass auch Entscheidungen der  Abgabenbehörde für einen früheren Steuerzeitraum in verfassungskonformer Interpretation  eine Vorfrage darstellen können bzw. in gleicher Weise behandelt werden müssen.

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 18** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140853.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140853.1_42`)

**False Positives:**


Die Aussetzung der Entscheidung ist mit Bescheidbeschwerde beim Verwaltungsgericht bzw  mit Revision beim VwGH oder mit VfGH-Beschwerde anfechtbar (vgl. Ritz/Koran, BAO7 § 271 Rz  23 mit Verweis auf VwGH 28.01.1971, 1553/69;

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 19** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149473.1_121`)

**False Positives:**


Sowohl nach dem  Wortlaut der Bestimmung des §§ 308 BAO als auch nach der Rechtsprechung muss die  Nachholung der versäumten Handlung nicht zwingend gleichzeitig mit der Einbringung des  Antrags auf Wiedereinsetzung in den vorigen Stand erfolgen, sondern kann auch bereits im  Vorfeld vorgenommen werden (vgl. VfGH 2. 12. 1976, B 369/75, ZfVB 1977/3/1351 = Slg 7935;

FP: `VfGH` (organisation)

**✅ Gold Entities:**

</details>

---

## `Anwälte Mandl & Mitterbauer GmbH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific law firm 'Anwälte Mandl & Mitterbauer GmbH'.

**Content:**
```
\bAnw\u00e4lte\s+Mandl\s*&\s*Mitterbauer\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1293 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Anwälte Mandl & Mitterbauer GmbH` | `Anwälte Mandl & Mitterbauer GmbH` |

</details>

---

## `EASO`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the organization 'EASO'.

**Content:**
```
\bEASO\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 242 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_62`)


Werbungskosten die in Zusammenhang mit Frontex, EASO, ... Einsätzen stehen, dürfen daher in  solchen Fällen nicht berücksichtigt werden.

| Predicted | Gold |
|---|---|
| `EASO` | `EASO` |

</details>

---

## `Bundesministerium für Inneres`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the full name 'Bundesministerium für Inneres'.

**Content:**
```
\bBundesministerium\s+f\u00fcr\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 238 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_72`)


Die Differenz iHv 2.114,80 €  entspricht dem mit dem Kurzzeiteinsatz zusammenhängenden, im Lohnzettel des  Bundesministerium für Inneres ausgewiesenen Reisekostenersatz, welcher zuvor iSd § 47 EStG  durch Abzug vom Arbeitslohn versteuert wurde.

| Predicted | Gold |
|---|---|
| `Bundesministerium für Inneres` | `Bundesministerium für Inneres` |

</details>

---

## `Bundesministers für Finanzen`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Bundesministers für Finanzen' (genitive form).

**Content:**
```
\bBundesministers\s+f\u00fcr\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 45 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149801.1`) ( sent_id: `findok-manually-annotated_TRAIN/149801.1_6`)


Darüber hinaus begehrte er den Freibetrag für Behinderung (§ 35 Abs 3 EStG) und den  pauschalen Freibetrag wegen Unzumutbarkeit der Benützung öffentlicher Verkehrsmittel nach  § 3 Abs 1 Verordnung des Bundesministers für Finanzen über außergewöhnliche Belastungen  (hinfort: § 3 Abs 1 VO).

| Predicted | Gold |
|---|---|
| `Bundesministers für Finanzen` | `Bundesministers für Finanzen` |

</details>

---

## `Höhere Lehranstalt`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Höhere Lehranstalt' followed by the specific long description for tourism/sports schools.

**Content:**
```
\bHöhere\s+Lehranstalt\s+für\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 576 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_3`)


Entscheidungsgründe  Verfahrensgang  Die Beschwerdeführerin bezog für die Tochter T., geb. 2003, wegen Schulbesuch (Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit in Krems) bis Juni 2022  Familienbeihilfe.

| Predicted | Gold |
|---|---|
| `Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit` | `Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit` |

</details>

---

## `Höheren Lehranstalt Genitive`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the genitive form 'Höheren Lehranstalt' for the same school type.

**Content:**
```
\bHöheren\s+Lehranstalt\s+für\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 574 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_34`)


Sachverhalt:  T. legte am 30.05.2022 die Reifeprüfung an der Höheren Lehranstalt für Tourismus,  Eventmanagement, Sport und Freizeit ab und machte danach keine weitere Ausbildung.

| Predicted | Gold |
|---|---|
| `Höheren Lehranstalt für Tourismus,  Eventmanagement, Sport und Freizeit` | `Höheren Lehranstalt für Tourismus,  Eventmanagement, Sport und Freizeit` |

</details>

---

## `Company with GmbH & Partner KG`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches company names ending in 'GmbH & Partner KG'.

**Content:**
```
\b([A-Z][a-zA-Z\s\u00e4\u00f6\u00fc\u00df\-]+?\s+GmbH\s*&\s*Partner\s*KG)(?=\s*(?:\(|,|\.|$|\s+(?:ist|war|wurde|hat|sind|waren|als|von|an|mit|der|die|das|ein|eine|einem|einer|den|die|dem|des|zur|im|um|zu|bei|nach|\u00fcber|unter|ohne|neben|zwischen|gegen|durch|seit|bis|vor|hinter|Ltd\.|\(|$)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 438 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Univ.-Prof. Maximilian Karrer  in der Beschwerdesache VetR Tosca Buecher,  Obere Amtshausgasse 26, 4591 Rosenau am Hengstpaß, Österreich, vertreten durch Grazer Treuhand Steuerberatung GmbH & Partner KG,  Petersgasse 128a, 8010 Graz, über die Beschwerde vom 14.11.2016 gegen den Bescheid des  Finanzamts Graz-Stadt vom 12.10.2016 betreffend Abweisung des Antrages gemäß § 299 BAO  vom 9.7.2015 auf Aufhebung des Einkommensteuerbescheides 2014 des Finanzamts Graz- Stadt vom 20.5.2015 zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Grazer Treuhand Steuerberatung GmbH & Partner KG` | `Grazer Treuhand Steuerberatung GmbH & Partner KG` |

</details>

---

## `Verwaltungsgericht Wien`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgericht Wien' specifically.

**Content:**
```
\bVerwaltungsgericht\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 440 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149308.1_15`)


Die Verfügungen mit den Zahlen   MA67/GZ/2024 vom 31.03.2025 und   MA67/GZ-2/2024 vom 02.04.2025  jedoch sind nicht berechtigt, daher erhebe ich hiermit das Rechtsmittel der Beschwerde an das  Verwaltungsgericht Wien.

| Predicted | Gold |
|---|---|
| `Verwaltungsgericht Wien` | `Verwaltungsgericht Wien` |

</details>

---

## `Wiederspan Beratung GMBH`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Wiederspan Beratung GMBH' specifically.

**Content:**
```
\bWiederspan\s+Beratung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1571 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_25`)


Unter Punkt „Küche“ wurde zunächst ausgeführt, dass zwei Rechnungen der „Wiederspan Beratung GMBH“  2 von 7 Seite 3 von 7

| Predicted | Gold |
|---|---|
| `Wiederspan Beratung GMBH` | `Wiederspan Beratung GMBH` |

</details>

---

## `Mur Alver OG`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Mur Alver OG' specifically.

**Content:**
```
\bMur\s+Alver\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1570 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149691.1_26`)


keine Leistungsbeschreibung enthalte und nicht der Bf als Empfänger aufscheine und eine  Rechnung der „Mur Alver OG“ Leuchten aus dem Luxussegment anführe.

| Predicted | Gold |
|---|---|
| `Mur Alver OG` | `Mur Alver OG` |

</details>

---

## `Krankenpflegevereins Bludenz`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Krankenpflegevereins Bludenz'.

**Content:**
```
\bKrankenpflegevereins\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1304 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149421.1_88`)


Die Kosten lt Bestätigungen des Krankenpflegevereins  Bludenz (welche auch mittels Kontoauszüge nachgewiesen wurden) iHv 625,54 Euro (für 2016),  485,50 Euro (für 2017) und 457,25 Euro (für 2018) sind somit zwangsläufig erwachsen und  werden daher als außergewöhnliche Belastung mit Selbstbehalt anerkannt.

| Predicted | Gold |
|---|---|
| `Krankenpflegevereins  Bludenz` | `Krankenpflegevereins  Bludenz` |

</details>

---

## `Bundesministerin für Finanzen`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the feminine form 'Bundesministerin für Finanzen'.

**Content:**
```
\bBundesministerin\s+für\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1100 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_74`)


Gemäß § 4 Abs 1 Verordnung der Bundesministerin für Finanzen über die Kriterien zur  Ermittlung des Pendlerpauschales und des Pendlereuros, zur Einrichtung eines  Pendlerrechners und zum Vorliegen eines Familienwohnsitzes (Pendlerverordnung), BGBl II  2013/276 idF BGBl II 2022/275 liegt ein Familienwohnsitz (§ 16 Abs 1 Z 6 lit f und § 20 Abs 1 Z 2  lit e EStG 1988) „dort, wo  1.

| Predicted | Gold |
|---|---|
| `Bundesministerin für Finanzen` | `Bundesministerin für Finanzen` |

</details>

---

## `Tritri-IT`

**F1:** 0.001 | **Precision:** 1.000 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Tritri-IT'.

**Content:**
```
\bTritri-IT\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.001 | 0.001 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 1392 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_348`)


(Der Vollständigkeit halber  wird angemerkt, dass damals alle Beschwerden des Tritri-IT -Konzernes durch denselben  Richter beim BFG entschieden wurden).

| Predicted | Gold |
|---|---|
| `Tritri-IT` | `Tritri-IT` |

</details>

---

## `Company with GmbH & Co KG`

**F1:** 0.001 | **Precision:** 0.500 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches company names ending in 'GmbH & Co KG', ensuring the full name including '&' is captured.

**Content:**
```
\b([A-Z][a-zA-Z\s\u00e4\u00f6\u00fc\u00df\-]+?\s+GmbH\s*&\s*Co\s*KG)(?=\s*(?:\(|,|\.|$|\s+(?:ist|war|wurde|hat|sind|waren|als|von|an|mit|der|die|das|ein|eine|einem|einer|den|die|dem|des|zur|im|um|zu|bei|nach|\u00fcber|unter|ohne|neben|zwischen|gegen|durch|seit|bis|vor|hinter|Ltd\.|\(|$)))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.001 | 0.001 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 1214 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149570.1`) ( sent_id: `findok-manually-annotated_TRAIN/149570.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Andreas Stanek in der Beschwerdesache  der Oleg Peltzmann, Bakk. techn., Ludwig Halauska-Straße 7, 9544 Wiesen, Österreich, vertreten durch TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG, Muthgasse 109, 1190 Wien, über deren Beschwerde vom  3. Dezember 2024 gegen den Bescheid des Finanzamtes Österreich vom 13. November 2024  betreffend Anspruchszinsen (§ 205 BAO) 2022, Steuernummer  94-582/7899, zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` | `TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Josef Zwilling in der Beschwerdesache  Ferdinand Mielnickel, Viertelweg 16, 3720 Gaindorf, Österreich, vertreten durch Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG, Praterstraße 38, 1020 Wien, über die Beschwerde vom  30. November 2017 gegen die Bescheide des Finanzamtes Baden Mödling (nunmehr Finanzamt  Österreich) vom 31. Oktober 2017 betreffend Festsetzung eines Verspätungszuschlages  betreffend Einkommensteuer 2015 und 2016 und Umsatzsteuer 2015 und 2016,  Steuernummer 86-167/7419  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

FP: `Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Josef Zwilling` (person)
- `Ferdinand Mielnickel` (person)
- `Viertelweg 16, 3720 Gaindorf, Österreich` (address)
- `Hallas & Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` (organisation)
- `Praterstraße 38, 1020 Wien` (address)
- `Finanzamtes Baden Mödling` (organisation)
- `Finanzamt  Österreich` (organisation)
- `86-167/7419` (tax_number)

</details>

---

## `UFS Abbreviation`

**F1:** 0.001 | **Precision:** 0.500 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'UFS' (Unabhängiger Finanzsenat) followed by a location.

**Content:**
```
\bUFS\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.500 | 0.001 | 0.001 | 2 | 1 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 1 | 249 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_98`)


Gegenteiliges ergibt sich auch nicht aus der von der  belangten Behörde in diesem Zusammenhang ins Treffen geführten Entscheidung des UFS  Salzburg vom 20.8.2013, RV/0389-S/13 (dort hatte der Berufungswerber die Verbuchung einer  von ihm auf Grund einer noch anhängigen VwGH-Beschwerde erwarteten Gutschrift, also  tatsächlich die Verbuchung einer zukünftigen Gutschrift beantragt).

| Predicted | Gold |
|---|---|
| `UFS  Salzburg` | `UFS  Salzburg` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/144169.1_106`)

**False Positives:**


Im Erkenntnis des Bundesfinanzgerichtes vom 26.04.2021, RV/7100436/2021, wurde erwogen:   Gemäß § 53 FLAG 1967 und den unionsrechtlichen Vorschriften ist als "Ausland" i.S.d. FLAG  1967 ein Drittland, nicht aber ein anderer Mitgliedstaat der Europäischen Union (bzw. ein Staat  des EWR oder die Schweiz) anzusehen (siehe auch Kuprian, Kein Familienbeihilfenanspruch bei  Ausbildung eines Kindes in einem "Drittland", UFS Journal 2011, 371;

FP: `UFS Journal` (organisation)

**✅ Gold Entities:**
- `Schweiz` (country)

</details>

---

## `BFH Abbreviation`

**F1:** 0.001 | **Precision:** 0.333 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'BFH' as an organization (Bundesfinanzgericht).

**Content:**
```
\bBFH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.333 | 0.001 | 0.001 | 3 | 1 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 2 | 1204 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/132504.1_64`)


Zur Frage der Ordnungsmäßigkeit des Fahrtenbuches sei auf die Rechtsprechung  des deutschen BFH zu verweisen, die auch für die österreichische Rechtslage relevant sei.

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_43`)

**False Positives:**


BFH, BStBl 1997 II 642;

FP: `BFH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149280.1`) ( sent_id: `findok-manually-annotated_TRAIN/149280.1_49`)

**False Positives:**


BFH, BStBl 1997 II 642;

FP: `BFH` (organisation)

**✅ Gold Entities:**

</details>

---

## `OECD`

**F1:** 0.001 | **Precision:** 0.200 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches the organization 'OECD'.

**Content:**
```
\bOECD\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.200 | 0.001 | 0.001 | 5 | 1 | 4 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 4 | 939 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/136623.1_94`)


Die Zentralstelle kann den Beamten mit seiner Zustimmung  1. zu Ausbildungszwecken oder als Nationalen Experten zu einer Einrichtung, die im Rahmen  der europäischen Integration oder der OECD tätig ist, oder  2.

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated_TRAIN/149828.1_107`)

**False Positives:**


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

FP: `OECD` (organisation)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

FP: `OECD` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)
- `Österreich` (country)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149828.1_107`)

**False Positives:**


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

FP: `OECD` (organisation)


Derartige Zahlungen und somit auch von der SUVA ausbezahlte Invalidenrenten fallen  daher unter die für im Abkommen nicht ausdrücklich erwähnte Einkünfte zur Anwendung kom- mende Auffangbestimmung des Art. 21 DBA-Schweiz, nach welcher das Besteuerungsrecht  ausschließlich dem Ansässigkeitsstaat, im Beschwerdefall somit Österreich zukommt [vgl.  Bendlinger/Kofler in Bendlinger/Kanduth-Kristen/Kofler/Rosenberger, Internationales Steuer- recht2, 2018, Die Verteilungsnormen im OECD-MA (Art. 6 bis 22 OECD-MA), Teil 2, Rz 707 f].

FP: `OECD` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)
- `Österreich` (country)

</details>

---

## `Company with AG Suffix`

**F1:** 0.001 | **Precision:** 0.143 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches company names ending in 'AG' with strict boundaries, preventing capture of preceding 'GmbH' or 'in'.

**Content:**
```
(?<!\w)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df\s\-,]+?\s+AG)(?=\s*(?:\(|,|\.|$|\s+(?:und|sowie|als|von|an|mit|der|die|das|ein|eine|einem|einer)|\s+GmbH|\s+KG|\s+OG|\s+haftenden|\s+und\s+Mitges|\s+der\s+haftenden|\s+in\s+[A-Z]))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.143 | 0.001 | 0.001 | 7 | 1 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 6 | 1623 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138586.1_7`)


Es wurden daher auch im Einkommensteuerbescheid 2016 vom 27.02.2017 bei der  Berechnung des Einkommens und der Einkommensteuer die bereits um das Pendlerpauschale  in Höhe von 1.476,00 € gekürzten Einkünfte bei der Fa. Berwaldkel-Möbel AG  in Ansatz gebracht.

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated_TRAIN/138736.1_16`)

**False Positives:**


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG, Niederau 25, 6731 Bühl, Österreich  tätig.

FP: `Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Nexkelkel AG` (organisation)
- `Niederau 25, 6731 Bühl, Österreich` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/138736.1_16`)

**False Positives:**


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG, Niederau 25, 6731 Bühl, Österreich  tätig.

FP: `Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG` (organisation)

**✅ Gold Entities:**
- `Nexkelkel AG` (organisation)
- `Niederau 25, 6731 Bühl, Österreich` (address)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_28`)

**False Positives:**


bis 31.12.2023 Einkünfte aus nichtselbständiger Arbeit von der  X GmbH in Adr AG.

FP: `Einkünfte aus nichtselbständiger Arbeit von der  X GmbH in Adr AG` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_33`)

**False Positives:**


Die Entfernung zwischen der Adresse des Arbeitgebers X GmbH in Adr AG und der  österreichischen Wohnadresse Bf-Adr Ö beträgt weniger als 20 Kilometer.

FP: `Die Entfernung zwischen der Adresse des Arbeitgebers X GmbH in Adr AG` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149868.1_42`)

**False Positives:**


Die Feststellungen hinsichtlich der Entfernung zwischen der Adresse des Arbeitgebers X GmbH  in Adr AG und der österreichischen Wohnadresse Bf-Adr Ö und der Zeitdauer der Benutzung  eines Massenbeförderungsmittels gründen sich auf eine vom Bundesfinanzgericht  durchgeführte Berechnung mit dem von Bundesministerium für Finanzen im Internet zur  Verfügung gestellten Pendlerrechner.

FP: `Die Feststellungen hinsichtlich der Entfernung zwischen der Adresse des Arbeitgebers X GmbH  in Adr AG` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)
- `Bundesministerium für Finanzen` (organisation)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/140526.1_56`)

**False Positives:**


Der Beschwerdeführer war seit 21.4.1992 und auch noch in den streitgegenständlichen Jahren  als Monteur bei der Cervenka&Neunübel Telekom AG, unselbstständig erwerbstätig.

FP: `Neunübel Telekom AG` (organisation)

**✅ Gold Entities:**
- `Cervenka&Neunübel Telekom AG` (organisation)

</details>

---

## `Merkur Treuhand Steuerberatung (Short)`

**F1:** 0.001 | **Precision:** 0.091 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Merkur Treuhand Steuerberatung' without GmbH suffix if present in specific contexts.

**Content:**
```
\bMerkur\s+Treuhand\s+Steuerberatung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.091 | 0.001 | 0.001 | 11 | 1 | 10 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 10 | 34 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_64`)


Dass die Bescheide (lediglich) per E-Mail an die Merkur Treuhand  Steuerberatung weitergeleitet wurden, hat diese über Aufforderung des Bundesfinanzgerichtes  im Verfahren RV/702183/2024 mitgeteilt und auch das diesbezügliche E-Mail vorgelegt.

| Predicted | Gold |
|---|---|
| `Merkur Treuhand  Steuerberatung` | `Merkur Treuhand  Steuerberatung` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_1`)

**False Positives:**


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Univ.-Prof. Hartwig Boehler  in der Beschwerdesache DDr.in Josepha de Haan,  Oisching 129, 3071 Wiesen, Österreich, vertreten durch Merkur Treuhand Steuerberatung GmbH, St.-Veit-Gasse 50,  1130 Wien, über die Beschwerde vom 16. Mai 2024 gegen den Bescheid des Finanzamtes  Österreich vom 13. Mai 2024 betreffend Abrechnung gem. § 216 BAO Steuernummer  01-186/7053  zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO teilweise Folge gegeben und festgestellt, dass die  Umbuchung des per 3.4.2024 auf dem Abgabenkonto der Beschwerdeführerin bestehenden  Guthabens i.H.v. € 166.146,40 auf Finanzverwahrnisse unrichtig war.

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Univ.-Prof. Hartwig Boehler` (person)
- `DDr.in Josepha de Haan` (person)
- `Oisching 129, 3071 Wiesen, Österreich` (address)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)
- `St.-Veit-Gasse 50,  1130 Wien` (address)
- `Finanzamtes  Österreich` (organisation)
- `01-186/7053` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_43`)

**False Positives:**


B. Umbuchung eines Guthabens auf Finanzverwahrnisse  Mit Schreiben vom 13.3.2024, eingelangt bei der belangten Behörde am selben Tage,  übermittelte die Merkur Treuhand Steuerberatung GmbH der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin und ihr unterfertigte Vollmacht, womit die  Beschwerdeführerin die Merkur Treuhand Steuerberatung GmbH als „Vertreter in allen  steuerlichen, wirtschaftlichen und sonstigen Angelegenheiten“ bevollmächtigt.

FP: `Merkur Treuhand Steuerberatung` (organisation)


B. Umbuchung eines Guthabens auf Finanzverwahrnisse  Mit Schreiben vom 13.3.2024, eingelangt bei der belangten Behörde am selben Tage,  übermittelte die Merkur Treuhand Steuerberatung GmbH der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin und ihr unterfertigte Vollmacht, womit die  Beschwerdeführerin die Merkur Treuhand Steuerberatung GmbH als „Vertreter in allen  steuerlichen, wirtschaftlichen und sonstigen Angelegenheiten“ bevollmächtigt.

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur Treuhand Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_44`)

**False Positives:**


Weiters wurde  der Merkur Treuhand Steuerberatung GmbH darin die Vollmacht „zum Empfang von  Schriftstücken, insbesondere der Abgabenbehörden, welche nunmehr ausschließlich dem  Bevollmächtigten zuzustellen sind“ erteilt und mitgeteilt, dass durch die vorliegende Vollmacht  „noch etwa beim Finanzamt erliegende vorhergehende Vollmachten außer Kraft gesetzt“  werden.

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_45`)

**False Positives:**


Im (Begleit-) Schreiben vom 13.3.2024 führt die Merkur Treuhand Steuerberatung  GmbH aus, dass die Vollmacht als „Spezialvollmacht für das laufende Verfahren betreffend  Umsatzsteuer und NOVA sowie das Finanzstrafverfahren“ erteilt wurde.

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur Treuhand Steuerberatung  GmbH` (organisation)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_54`)

**False Positives:**


Die Schabetsberger Steuerberatung GmbH leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  Merkur Treuhand Steuerberatung GmbH weiter.

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_63`)

**False Positives:**


Die Feststellungen zum Sicherstellungsauftrag vom 20.3.2024 und zum Pfändungsbescheid  vom 3.4.2024 gründen sich auf eine Einsichtnahme in den Akt RV/702183/2024 des  Bundesfinanzgerichtes (dort bekämpft die Beschwerdeführerin den Pfändungsbescheid vom  3.4.2024), insbesondere auf den Zustellnachweis (Rückschein) zum Sicherstellungsauftrag vom  20.3.2024 und zum Pfändungsbescheid vom 3.4.2024, worin ein Mitarbeiter oder eine  Mitarbeiterin (Unterschrift unleserlich) der Schabetsberger Steuerberatung GmbH die  Übernahme dieser beiden Bescheide am 5.4.2024 bestätigt, sowie auf das Schreiben der  Merkur Treuhand Steuerberatung GmbH vom 13.3.2024 und die damit übermittelte Vollmacht  vom 11.3.2024.

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 6** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_107`)

**False Positives:**


Im vorliegenden Fall bestellte die Beschwerdeführerin am 11.3.2024 die Merkur Treuhand  Steuerberatung GmbH zum Zustellbevollmächtigten.

FP: `Merkur Treuhand  Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur Treuhand  Steuerberatung GmbH` (organisation)

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_110`)

**False Positives:**


Anzumerken ist, dass die Vollmacht zugunsten der Merkur  Treuhand Steuerberatung GmbH entgegen den Ausführungen im Schreiben vom 13.3.2024 alle  steuerlichen Angelegenheiten umfasst und daher nicht auf das laufende Verfahren betreffend  Umsatzsteuer und NOVA sowie das Finanzstrafverfahren eingeschränkt ist.

FP: `Merkur  Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur  Treuhand Steuerberatung GmbH` (organisation)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_121`)

**False Positives:**


Die hier geschehene Übermittlung der eingescannten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail der Schabetsberger  Steuerberatung GmbH vom 16.4.2024 an die Merkur Treuhand Steuerberatung GmbH konnte  daher keine Heilung der unwirksamen Zustellung bewirken.

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger  Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

</details>

---

## `Amt für Betrugsbekämpfung`

**F1:** 0.001 | **Precision:** 0.067 | **Recall:** 0.001  

**Format:** `regex`  
**Description:**
Matches 'Amt für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung'.

**Content:**
```
\b(?:Amt|Amtes)\s+f\u00fcr\s+Betrugsbek\u00e4mpfung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.067 | 0.001 | 0.001 | 15 | 1 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 14 | 1263 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_22`)


Die belangte Behörde verweigere die Buchung der UVAs und NOVA- Meldungen mit dem Hinweis, dass man auf eine Aussage des Amtes für Betrugsbekämpfung  (ABB) warte.

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_2`)

**False Positives:**


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_3`)

**False Positives:**


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_10`)

**False Positives:**


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_15`)

**False Positives:**


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amt für Betrugsbekämpfung` (organisation)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amtes für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_89`)

**False Positives:**


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146475.1_140`)

**False Positives:**


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Zollamt Österreich` (organisation)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_2`)

**False Positives:**


Herrn OSR Jan Passerschroer, MA, geb. am 1960, Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich  2. Reinemut + Smoch Handel, Zachariasweg 4K, 3250 Wieselburg, Österreich   beide vertreten durch HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH, Triesterstraße  14, 2351 Wiener Neudorf,   wegen der Finanzvergehen der Abgabenhinterziehungen und Finanzordnungswidrigkeiten  gemäß §§ 33 Abs. 1 und Abs. 2 lit. a und 49 Abs. 1 lit. a FinStrG des Finanzstrafgesetzes  (FinStrG) über die Beschwerden des Beschuldigten und des belangten Verbandes jeweils vom  7. August 2024 gegen das Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, in der Sitzung am 10. Dezember  2024 in Anwesenheit der Schriftführerin zu Recht erkannt:  1.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 7** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_3`)

**False Positives:**


Der Beschwerde des Beschuldigten wird teilweise stattgegeben und das angefochtene  Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim Amt für Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung an Einkommensteuer 2019 des Beschuldigten von € 7.315,00, einer Verkürzung der  Reinemut + Smoch Handel  an Umsatzsteuer 7/2019 im Teilbetrag von € 63,82 sowie einer Verkürzung von  Umsatzsteuer 1-12/2017 der *OG* von € 599,99 geführte Finanzstrafverfahren wird gemäß §§  136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 8** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_10`)

**False Positives:**


Der Beschwerde des belangten Verbandes wird teilweise stattgegeben und das beim Amt für  Betrugsbekämpfung als Finanzstrafbehörde wegen des Verdachts einer Verkürzung an  Umsatzsteuer 7/2019 der Reinemut + Smoch Handel  im Teilbetrag von € 63,82 geführte Finanzstrafverfahren  wird gemäß §§ 136, 157, 82 Abs. 3 lit. c FinStrG eingestellt.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 9** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_15`)

**False Positives:**


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amt für Betrugsbekämpfung` (organisation)


Entscheidungsgründe  Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim Amt für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, wurden   „I. Herr OSR Jan Passerschroer, MA  schuldig erkannt, er hat im Bereich des Finanzamts Österreich   a) vorsätzlich unter Verletzung einer abgabenrechtlichen Offenlegungs- und   Wahrheitspflicht durch Nichtabgabe der Einkommensteuererklärungen für die Jahre 2019 und  2020 eine Verkürzung an   Einkommensteuer 2019 in Höhe von € 7.315,00   Einkommensteuer 2020 in Höhe von € 1.525,00  Gesamt: € 8.840,00  zu bewirken versucht, und  b) als der für die steuerlichen Angelegenheiten verantwortliche Geschäftsführer der Firma  Reinemut + Smoch Handel, St.Nr. 72-531/2688  vorsätzlich unter Verletzung der Verpflichtung zur Abgabe  von dem § 21 des Umsatzsteuergesetzes 1994 (UStG) entsprechenden Voranmeldungen eine  Verkürzung von Vorauszahlungen im Teilbetrag von   Umsatzsteuer 7/2019 von € 2.792,16  Umsatzsteuer 10/2021 von € 1.077,23  Umsatzsteuer 11/2021 von € 1.695,00  Umsatzsteuer 3/2022 von € 980,00  2 von 22 Seite 3 von 22

FP: `Amtes für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 10** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_89`)

**False Positives:**


3. Feststellungen des Vorsatzes nach § 33 (1) sowie des Vorsatzes und der Wissentlichkeit nach  § 33 (2) a und b FinStrG  Aus den Ausführungen unserer Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das Amt für Betrugsbekämpfung, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten  in einem psychisch instabilen Zustand war.

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

**Example 11** (doc_id: `findok-manually-annotated_TRAIN/146475.1`) ( sent_id: `findok-manually-annotated_TRAIN/146475.1_140`)

**False Positives:**


Die Darlegung hat, wenn die  Handhabung der verletzten Abgaben- oder Monopolvorschriften dem Zollamt Österreich  obliegt, gegenüber diesem, sonst gegenüber einem Finanzamt oder dem Amt für  Betrugsbekämpfung zu erfolgen.

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Zollamt Österreich` (organisation)

</details>

---

## `Fachhochschule and FH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Fachhochschule' or 'FH' followed by a location (e.g., Kärnten, Wien).

**Content:**
```
\b(?:Fachhochschule|FH)\s+[A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 14 | 0 | 14 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 14 | 1674 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_8`)

**False Positives:**


Vom Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an  der Fachhochschule Wiener Neustadt das Bachelorstudium Biotechnische Verfahren.

FP: `Fachhochschule Wiener` (organisation)

**✅ Gold Entities:**
- `Fachhochschule Wiener Neustadt` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_9`)

**False Positives:**


Im Rahmen der Beantwortung des Anspruchsüberprüfungsschreibens gab der Bf. am  16.02.2023 bekannt, dass T. nunmehr seit 15.02.2023 am FH Campus Wien Gesundheits- und  Krankenpflege studiere.

FP: `FH Campus` (organisation)

**✅ Gold Entities:**
- `FH Campus Wien` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_48`)

**False Positives:**


Von Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an der  Fachhochschule Wiener Neustadt das Bachelorstudium Biotechnische Verfahren.

FP: `Fachhochschule Wiener` (organisation)

**✅ Gold Entities:**
- `Fachhochschule Wiener Neustadt` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_79`)

**False Positives:**


Vom Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an  der FH Wiener Neustadt für Wirtschaft und Technik GmbH (Tulln) das Bachelorstudium  Biotechnische Verfahren (FN000568).

FP: `FH Wiener` (organisation)

**✅ Gold Entities:**
- `FH Wiener Neustadt` (organisation)
- `Wirtschaft und Technik GmbH` (organisation)
- `Tulln` (city)

**Example 4** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_81`)

**False Positives:**


Seit Februar 2023 studiert T. an der FH Campus Wien Gesundheits- und Krankenpflege  (FC000599).

FP: `FH Campus` (organisation)

**✅ Gold Entities:**
- `FH Campus Wien` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_138`)

**False Positives:**


Vom Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an  der FH Wiener Neustadt für Wirtschaft und Technik GmbH (Tulln) das Bachelorstudium  Biotechnische Verfahren.

FP: `FH Wiener` (organisation)

**✅ Gold Entities:**
- `FH Wiener Neustadt` (organisation)
- `Wirtschaft und Technik GmbH` (organisation)
- `Tulln` (city)

**Example 6** (doc_id: `findok-manually-annotated_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated_TRAIN/143567.1_142`)

**False Positives:**


Seit Februar 2023 studiert T. an der FH Campus Wien Gesundheits- und Krankenpflege.

FP: `FH Campus` (organisation)

**✅ Gold Entities:**
- `FH Campus Wien` (organisation)

**Example 7** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_8`)

**False Positives:**


Vom Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an  der Fachhochschule Wiener Neustadt das Bachelorstudium Biotechnische Verfahren.

FP: `Fachhochschule Wiener` (organisation)

**✅ Gold Entities:**
- `Fachhochschule Wiener Neustadt` (organisation)

**Example 8** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_9`)

**False Positives:**


Im Rahmen der Beantwortung des Anspruchsüberprüfungsschreibens gab der Bf. am  16.02.2023 bekannt, dass T. nunmehr seit 15.02.2023 am FH Campus Wien Gesundheits- und  Krankenpflege studiere.

FP: `FH Campus` (organisation)

**✅ Gold Entities:**
- `FH Campus Wien` (organisation)

**Example 9** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_48`)

**False Positives:**


Von Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an der  Fachhochschule Wiener Neustadt das Bachelorstudium Biotechnische Verfahren.

FP: `Fachhochschule Wiener` (organisation)

**✅ Gold Entities:**
- `Fachhochschule Wiener Neustadt` (organisation)

**Example 10** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_79`)

**False Positives:**


Vom Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an  der FH Wiener Neustadt für Wirtschaft und Technik GmbH (Tulln) das Bachelorstudium  Biotechnische Verfahren (FN000568).

FP: `FH Wiener` (organisation)

**✅ Gold Entities:**
- `FH Wiener Neustadt` (organisation)
- `Wirtschaft und Technik GmbH` (organisation)
- `Tulln` (city)

**Example 11** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_81`)

**False Positives:**


Seit Februar 2023 studiert T. an der FH Campus Wien Gesundheits- und Krankenpflege  (FC000599).

FP: `FH Campus` (organisation)

**✅ Gold Entities:**
- `FH Campus Wien` (organisation)

**Example 12** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_138`)

**False Positives:**


Vom Wintersemester 2020/2021 bis einschließlich Sommersemester 2022 absolvierte sie an  der FH Wiener Neustadt für Wirtschaft und Technik GmbH (Tulln) das Bachelorstudium  Biotechnische Verfahren.

FP: `FH Wiener` (organisation)

**✅ Gold Entities:**
- `FH Wiener Neustadt` (organisation)
- `Wirtschaft und Technik GmbH` (organisation)
- `Tulln` (city)

**Example 13** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/143567.1_142`)

**False Positives:**


Seit Februar 2023 studiert T. an der FH Campus Wien Gesundheits- und Krankenpflege.

FP: `FH Campus` (organisation)

**✅ Gold Entities:**
- `FH Campus Wien` (organisation)

</details>

---

## `Bundeskanzleramt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundeskanzleramt' and its genitive form 'Bundeskanzleramtes'.

**Content:**
```
\bBundeskanzler(?:amt|amtes)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `LG für ZRS Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'LG für ZRS Wien'

**Content:**
```
\bLG\s+f\u00fcr\s+ZRS\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministeriums für Justiz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministeriums für Justiz' specifically

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

## `Landesgericht with LG Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'LG Landesgericht [Location]' or 'Landesgericht [Location]' or 'LG [Location]', stopping strictly before prepositions or verbs.

**Content:**
```
\b(?:LG\s+(?:Landesgericht\s+)?|Landesgericht\s+)([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df\s]+?)(?=\s+(?:im|vom|am|von|ist|bietet|f\u00fchrt|hat|war|wurde|sind|waren|sowie|und|als|an|mit|der|die|das|ein|eine|einem|einer|den|die|dem|des|zur|im|um|zu|bei|nach|\u00fcber|unter|ohne|neben|zwischen|gegen|durch|seit|bis|vor|hinter|\(|,|\.|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Karl-Franzens- Universität Graz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific university name Karl-Franzens- Universität Graz.

**Content:**
```
\bKarl\-Franzens\-\s+Universität\s+Graz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Europäische Grenzschutzagentur Frontex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Europäische Grenzschutzagentur Frontex' and its genitive form.

**Content:**
```
\bEurop(?:e|en)ische\s+Grenzschutzagentur\s+Frontex\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `HLF Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'HLF' followed by a location (e.g., Krems/Donau).

**Content:**
```
\bHLF\s+[A-Z][a-zA-Z\s/]+
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 576 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149824.1_28`)

**False Positives:**


Die Bf. bringt im Vorlageantrag, eingelangt beim Finanzamt am 23.03.2023, vor, dass ihre  Tochter T. am 30.05.2022 an der HLF Krems/Donau maturiert habe und damit in die alte  2 von 6 Seite 3 von 6

FP: `HLF Krems/Donau maturiert habe und damit in die alte  ` (organisation)

**✅ Gold Entities:**
- `HLF Krems/Donau` (organisation)

</details>

---

## `ÖBUG GmbH Full Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific long-form law firm name including the 'ÖBUG' prefix and description.

**Content:**
```
\b"?ÖBUG"?\s+DR\.\s+NIKOLAUS\s+Wirtschaftstreuhand\s+GmbH\s*-\s+Wirtschaftsprüfungs-\s+und\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schabetsberger Steuerberatung (Short)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Schabetsberger Steuerberatung' without GmbH suffix.

**Content:**
```
\bSchabetsberger\s+Steuerberatung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 6 | 0 | 6 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 6 | 26 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_51`)

**False Positives:**


Beide Bescheide (der an das  Finanzamt Österreich adressierte Pfändungsescheid vom 3.4.2024 ergänzt um die Anmerkung  „Ausfertigung für den Abgabenschuldner“) wurden der Beschwerdeführerin am 5.4.2024 zu  Handen der Schabetsberger Steuerberatung GmbH, Fischerstiege 9, 1010 Wien, zugestellt.

FP: `Schabetsberger Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich` (organisation)
- `Schabetsberger Steuerberatung GmbH` (organisation)
- `Fischerstiege 9, 1010 Wien` (address)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_54`)

**False Positives:**


Die Schabetsberger Steuerberatung GmbH leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  Merkur Treuhand Steuerberatung GmbH weiter.

FP: `Schabetsberger Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 2** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_63`)

**False Positives:**


Die Feststellungen zum Sicherstellungsauftrag vom 20.3.2024 und zum Pfändungsbescheid  vom 3.4.2024 gründen sich auf eine Einsichtnahme in den Akt RV/702183/2024 des  Bundesfinanzgerichtes (dort bekämpft die Beschwerdeführerin den Pfändungsbescheid vom  3.4.2024), insbesondere auf den Zustellnachweis (Rückschein) zum Sicherstellungsauftrag vom  20.3.2024 und zum Pfändungsbescheid vom 3.4.2024, worin ein Mitarbeiter oder eine  Mitarbeiterin (Unterschrift unleserlich) der Schabetsberger Steuerberatung GmbH die  Übernahme dieser beiden Bescheide am 5.4.2024 bestätigt, sowie auf das Schreiben der  Merkur Treuhand Steuerberatung GmbH vom 13.3.2024 und die damit übermittelte Vollmacht  vom 11.3.2024.

FP: `Schabetsberger Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 3** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_108`)

**False Positives:**


Gleichzeitig wurden alle bis dahin beim  Finanzamt erliegenden Vollmachten (daher auch eine allfällige Zustellvollmacht der  Schabetsberger Steuerberatung GmbH) aufgelöst.

FP: `Schabetsberger Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger Steuerberatung GmbH` (organisation)

**Example 4** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_114`)

**False Positives:**


Die Zustellung an die Schabetsberger  Steuerberatung GmbH war unwirksam.

FP: `Schabetsberger  Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger  Steuerberatung GmbH` (organisation)

**Example 5** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/146072.1_121`)

**False Positives:**


Die hier geschehene Übermittlung der eingescannten Bescheide vom  20.3.2024 (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail der Schabetsberger  Steuerberatung GmbH vom 16.4.2024 an die Merkur Treuhand Steuerberatung GmbH konnte  daher keine Heilung der unwirksamen Zustellung bewirken.

FP: `Schabetsberger  Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger  Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

</details>

---

## `Bezirksgericht with Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bezirksgericht' or 'BG Bezirksgericht' followed by a location name.

**Content:**
```
\b(?:BG\s+)?Bezirksgericht\s+([A-Z][a-zA-Z\u00e4\u00f6\u00fc\u00df]+)(?=\s*(?:vom|am|von|ist|hat|wurde|sind|waren|\(|,|\.|$))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenbank Stallhofen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific bank name 'Raiffeisenbank Stallhofen'.

**Content:**
```
\bRaiffeisenbank\s+Stallhofen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mittel Unisyn GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Mittel Unisyn GMBH'.

**Content:**
```
\bMittel\s+Unisyn\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bärs & Walterscheidt Handel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Bärs & Walterscheidt Handel GMBH'.

**Content:**
```
\bB\u00e4rs\s*&\s*Walterscheidt\s+Handel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ober Lemostnor AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Ober Lemostnor AG'.

**Content:**
```
\bOber\s+Lemostnor\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Vennes Recycling AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Vennes Recycling AG'.

**Content:**
```
\bVennes\s+Recycling\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Österreichische Gesellschaft für Europapolitik`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Österreichische Gesellschaft für Europapolitik'.

**Content:**
```
\bÖsterreichische\s+Gesellschaft\s+für\s+Europapolitik\b
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
**Description:**
Matches the specific abbreviation 'BM für Finanzen'.

**Content:**
```
\bBM\s+für\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Unter Donunisee AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Unter Donunisee AG'.

**Content:**
```
\bUnter\s+Donunisee\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schweizerischen Unfallversicherungsanstalt (SUVA)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name 'Schweizerischen Unfallversicherungsanstalt (SUVA)' and its variations.

**Content:**
```
\bSchweizerischen\s+Unfallversicherungsanstalt\s*\(\s*SUVA\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BFG with Außenstelle Linz (Parentheses)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BFG (Außenstelle Linz)' as a complete organization entity.

**Content:**
```
\bBFG\s*\(\s*Außenstelle\s+Linz\s*\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BFG with Außenstelle Linz (Comma)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BFG, Außenstelle Linz' as a complete organization entity.

**Content:**
```
\bBFG\s*,\s*Außenstelle\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 1483 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_74`)

**False Positives:**


Mit Vorlagebericht vom 13.11.2013 hat das FA Wien 1/23  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr BFG, Außenstelle Linz) zur Entscheidung vorgelegt.

FP: `BFG, Außenstelle Linz` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)
- `UFS` (organisation)

</details>

---

## `Bundesfinanzgerichts with Außenstelle Linz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgerichts, Außenstelle Linz' as a complete organization entity.

**Content:**
```
\bBundesfinanzgerichts\s*,\s*Außenstelle\s+Linz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 1476 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_100`)

**False Positives:**


Das Erkenntnis des Bundesfinanzgerichts, Außenstelle Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des FA Wien 1/23  in vollem Umfang im Zuge einer Amtsrevision  angefochten.

FP: `Bundesfinanzgerichts, Außenstelle Linz` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)

**Example 1** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/145564.1_128`)

**False Positives:**


85-900/3590, BV 24 :  Beim gegenständlichen partiellen Rechtsnachfolger Roelfsen Versicherung  gab es betreffend dem  Veranlagungszeitraum 2010 folgende Verfahrensschritte iZm dem Feststellungsbescheid  Gruppenmitglied:  21.12.2011 Erstbescheid Feststellungsbescheid Gruppenmitglied 2010  27.05.2013 Wiederaufnahme des Verfahrens betreffend Feststellungsbescheid  Gruppenmitglied 2010 nach Betriebsprüfung   27.05.2013 neuer Sachbescheid Feststellungsbescheid Gruppenmitglied 2010  20.06.2013 Einbringung Beschwerde gegen Feststellungsbescheid Gruppenmitglied 2010  (Beschwerdepunkte Angemessenheitsprüfung PKW sowie Rückstellungsbildung  Rekultivierungskosten)  19.11.2013 Beschwerdevorentscheidung (Abweisung Beschwerdepunkt  Angemessenheitsprüfung PKW, teilweise Stattgabe bei Rückstellungsbildung  Rekultivierungskosten)  29.11.2013 Vorlageantrag (verbleibender Streitpunkt Angemessenheitsprüfung PKW)  16.12.2013 Vorlage an BFG (damals noch UFS)  17.08.2015 Erkenntnis des BFG RV/5100056/2014 - unbegründete Abweisung (unbegründete  Abweisung des Beschwerdepunktes Angemessenheitsprüfung PKW)  Betreffend des Rechtsvorgängers Houdek Maschinenbau  wurde das Erkenntnis des  Bundesfinanzgerichts, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum  Veranlagungsjahr 2007 erlassen.

FP: `Bundesfinanzgerichts, Außenstelle Linz` (organisation)

**✅ Gold Entities:**
- `85-900/3590` (tax_number)
- `Roelfsen Versicherung` (organisation)
- `UFS` (organisation)
- `Houdek Maschinenbau` (organisation)

</details>

---

## `SVS/SVB Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation 'SVS/SVB' as an organization.

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

## `PSD Wien Ambulatorium Landstraße`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full entity 'PSD Wien Ambulatorium Landstraße'.

**Content:**
```
\bPSD\s+Wien\s+Ambulatorium\s+Landstraße\b
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
**Description:**
Matches 'Sozialversicherungsanstalt der Bauern' and its genitive form 'Sozialversicherungsanstalt der Bauern' (contextual genitive often drops 's' in specific legal phrasing or is just the base form).

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

## `Sozialversicherung der Bauern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherung der Bauern' and its genitive form 'Sozialversicherung der Bauern'.

**Content:**
```
\bSozialversicherung\s+der\s+Bauern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 695 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated-filtered-higher-courts_TRAIN/149834.1_200`)

**False Positives:**


Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.

FP: `Sozialversicherung der Bauern` (organisation)

**✅ Gold Entities:**
- `WKO` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_TRAIN/149834.1`) ( sent_id: `findok-manually-annotated_TRAIN/149834.1_200`)

**False Positives:**


Auch die weiteren Tätigkeiten, welche vom Bf als „nach außen hin  eindeutig erkennbare Tätigkeit“ vorgebracht wurden (das Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der Sozialversicherung der Bauern, etc) geht ins Leere.

FP: `Sozialversicherung der Bauern` (organisation)

**✅ Gold Entities:**
- `WKO` (organisation)

</details>

---

## `Bundesministers für Arbeit Soziales und Konsumentenschutz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministers für Arbeit, Soziales und Konsumentenschutz'.

**Content:**
```
\bBundesministers\s+für\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `London Film Academy`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'London Film Academy' and the specific typo 'London Film Acadamy'.

**Content:**
```
\bLondon\s+Film\s+Acad(eme|emy)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Trafenfen Automotive Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Trafenfen Automotive' found in training data.

**Content:**
```
\bTrafenfen\s+Automotive\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Steiermark Mitte Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Steiermark Mitte' and 'Finanzamt Steiermark Mitte'.

**Content:**
```
\b(?:FA|Finanzamt)\s+Steiermark\s+Mitte\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mur Ververzor Betriebe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Mur Ververzor Betriebe'.

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

## `Naaß Elektro GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Naaß Elektro GMBH'.

**Content:**
```
\bNaaß\s+Elektro\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bersud Möbel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Bersud Möbel GMBH'.

**Content:**
```
\bBersud\s+Möbel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Unter Heimdorf GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Unter Heimdorf GMBH'.

**Content:**
```
\bUnter\s+Heimdorf\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Bruck Eisenstadt Oberwart`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Bruck Eisenstadt Oberwart' and its genitive form.

**Content:**
```
\bFinanz(?:amt|amtes)\s+Bruck\s+Eisenstadt\s+Oberwart\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Klagenfurt St. Veit Wolfsberg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Klagenfurt St. Veit Wolfsberg' and its genitive form.

**Content:**
```
\bFinanz(?:amt|amtes)\s+Klagenfurt\s+St\.\s+Veit\s+Wolfsberg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Vorarlberg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA Vorarlberg' and 'Finanzamt Vorarlberg'.

**Content:**
```
\b(?:FA|Finanzamt)\s+Vorarlberg\b
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

