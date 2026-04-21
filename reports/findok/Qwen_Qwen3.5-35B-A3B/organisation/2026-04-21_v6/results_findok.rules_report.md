# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-21T19:19:56.452233

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
| Training documents | 385 |
| Validation documents | 97 |
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
| Accuracy (exact match) | 86.4% |
| True Positives | 1030 |
| False Positives | 1415 |
| Micro Precision | 42.1% |
| Micro Recall | 59.1% |
| Micro F1 | 49.2% |
| Macro F1 | 49.2% |

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  <<<FAÖ>>> sowie ein Mitarbeiter der Abgabensicherung geladen wurden.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  <<<FAÖ>>> sowie ein Mitarbeiter der Abgabensicherung geladen wurden.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... strittig, ob das Finanzamt Österreich (in der Folge  kurz: <<<FAÖ>>>) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang ...
```

```
... Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: <<<FAG>>>) erlassenen Bescheiden zuständig ist.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAG` | `FAG` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Das <<<FAG>>> erließ am 21.8.2024 einen Bescheid über die Aufhebung des Umsatzsteuerbescheides ...
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Am 5.11.2024 hob das <<<FAG>>> den Umsatzsteuerbescheid 2022 vom 21.8.2024  erneut nach § ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Verfahren wie folgt:   a) Sachverhalt und Verfahrensablauf bei der <<<Houdek Maschinenbau>>>, Str.Nr.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
95-002/7970, BV 24:  Das Unternehmen <<<Houdek Maschinenbau>>>  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... die Nachfolgejahre wurden folgende  Umgründungsschritte bei <<<Houdek Maschinenbau>>>  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages ...
```

```
... des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die <<<Houdek Maschinenbau>>>  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach ...
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Zum Stichtag 31.12.2008 ist die <<<Houdek Maschinenbau>>>  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan ...
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der <<<Houdek Maschinenbau>>>, insoweit das auch nach der Abspaltung zum  31.12.2007 bei ...
```

```
... insoweit das auch nach der Abspaltung zum  31.12.2007 bei der <<<Houdek Maschinenbau>>>  verbliebende Vermögen betroffen ist.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... diese Bescheide Herrn F persönlich zugestellt würden, da die <<<ÖGK>>> die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... die oben  angeführten Abgaben - entsprechend dem Vorgehen der <<<ÖGK>>> - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Zuge derselben GPLB angefallen seien,  seien diese seitens der <<<ÖGK>>> der GmbH vorgeschrieben worden, sodass Herr F nicht damit  ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... in die Databox des EU gerichtet  wurden, die Bescheide der <<<ÖGK>>> allerdings an die GmbH übermittelt wurden.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... diese Bescheide Herrn F persönlich zugestellt würden, da die <<<ÖGK>>> die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Kff. Sandra Khartchenko  als Rechtsnachfolger der <<<Roelfsen Versicherung>>>, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten ...
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Kff. Sandra Khartchenko  als RNF der <<<Roelfsen Versicherung>>>  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als ...
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (<<<Roelfsen Versicherung>>>  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Bescheidadressaten waren  sowohl das Gruppenmitglied <<<Roelfsen Versicherung>>>  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Generalversammlungsbeschlusses vom  19.08.2009 eine Abspaltung zur Aufnahme in die <<<Roelfsen Versicherung>>>  durch Übertragung des  gesamten Betriebes (mit Ausnahme der ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Im Wirtschaftsjahr 2007 ist gemäß der beim <<<FA Wien 1/23>>>  eingereichten  Körperschaftsteuererklärung 2007 ein steuerlicher ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Am 26.04.2013 erließ das <<<FA Wien 1/23>>>  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Mit Vorlagebericht vom 13.11.2013 hat das <<<FA Wien 1/23>>>  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des <<<FA Wien 1/23>>>  gegenüber der  mitbeteiligten Partei Roelfsen Versicherung ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des <<<FA Wien 1/23>>>  in vollem Umfang im Zuge einer Amtsrevision  angefochten.
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Gegen dieses Erkenntnis ist eine ordentliche Revision an den <<<Verwaltungsgerichtshof>>> nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des <<<VwGH>>>  verwiesen (Ra 2020/13/0089).
```

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... dem vorerst zu entgegnen, dass nach der Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Nach ständiger Rechtsprechung des <<<Verwaltungsgerichtshofes>>> sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Der Bf. ist daher auf die ständige Rechtsprechung des <<<Verwaltungsgerichtshofes>>> zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Gegen dieses Erkenntnis ist eine ordentliche Revision an den <<<Verwaltungsgerichtshof>>> nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht ...
```

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Einwendungen (vor allem  Bescheidbeschwerden) nachzuholen (<<<VwGH>>> 17.10.2001, 98/13/0073;
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
<<<VwGH>>> 27.3.1996, 92/13/0291;
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
<<<VwGH>>> 20.6.1990, 89/13/0249;
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Steuerschuldner durch Bevorzugung unehrlicher, zu  berücksichtigen (<<<VwGH>>> 4.4.1989, 88/14/0245;
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... dem vorerst zu entgegnen, dass nach der Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Nach ständiger Rechtsprechung des <<<Verwaltungsgerichtshofes>>> sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Der Bf. ist daher auf die ständige Rechtsprechung des <<<Verwaltungsgerichtshofes>>> zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... insbesondere weil  das Erkenntnis von der Rechtsprechung des <<<Verwaltungsgerichtshofes>>> abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende ...
```

```
... zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> nicht einheitlich beantwortet wird.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Studium Rechtswissenschaften nach der zitierten Judikatur des  <<<Verwaltungsgerichtshofes>>> (VwGH 01.02.1990, 89/12/0175) als Studienwechsel.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... dem vorerst zu entgegnen, dass nach der Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Nach ständiger Rechtsprechung des <<<Verwaltungsgerichtshofes>>> sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Der Bf. ist daher auf die ständige Rechtsprechung des <<<Verwaltungsgerichtshofes>>> zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... insbesondere weil  das Erkenntnis von der Rechtsprechung des <<<Verwaltungsgerichtshofes>>> abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

```
... zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> nicht einheitlich beantwortet wird.
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des <<<Verwaltungsgerichtshofes>>>  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

```
... zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des <<<Verwaltungsgerichtshofes>>> nicht einheitlich beantwortet wird.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Unzulässigkeit der Revision:  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Revision  Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> die Revision an  den Verwaltungsgerichtshof zulässig, wenn ...
```

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Laut Amtsrevision wurde die Rechtsansicht des <<<Bundesfinanzgerichtes>>>, das freie Wahlrecht des  innerbetrieblichen Verlustausgleiches ...
```

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... und somit  der Verlustvortrag nicht in der im Erkenntnis des <<<Bundesfinanzgerichtes>>> dargestellten Höhe  zusteht (vgl. Seite 7 und 8 der VwGH-Entscheidung).
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Nach Ansicht des <<<VfGH>>> (zB 29.6.1985, G 42/85 ua;
```

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Beschwerde geäußerten verfassungsrechtlichen Bedenken an den <<<VfGH>>> zu tragen.
```

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Der Verfassungsgerichtshof (vgl. <<<VfGH>>> B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine ...
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Der <<<VfGH>>> hat in seinem Erkenntnis eine  14 von 39 Seite 15 von 39
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Dem genannten <<<VfGH>>>-Erkenntnis lag folgender Sachverhalt zu Grunde: Mit  Berufungsentscheidung ...
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Der <<<VfGH>>> bejahte die Anwendbarkeit des Vorfragentatbestandes.
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (<<<VfGH>>> 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  <<<Universität Wien>>> im Diplomstudium Rechtswissenschaften (UA101) inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der <<<Universität Wien>>> im Diplomstudium Rechtswissenschaften inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  <<<Universität Wien>>> im Diplomstudium Rechtswissenschaften (UA101) inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der <<<Universität Wien>>> im Diplomstudium Rechtswissenschaften inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der <<<Universität Wien inskribiert>>>.
```

FP: `Universität Wien inskribiert` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Sommersemester 2020 das Studium  Rechtswissenschaften an der <<<Universität Wien betrieben>>>.
```

FP: `Universität Wien betrieben` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... fest:  T. brach nach vier Semestern das Lehramtsstudium an der <<<Universität Wien ab>>> und begann im  Wintersemester 2022/2023 an der Pädagogischen ...
```

FP: `Universität Wien ab` (organisation)

```
... und begann im  Wintersemester 2022/2023 an der Pädagogischen <<<Hochschule Wien>>> mit dem Bachelorstudium  Lehramt Primarstufe.
```

FP: `Hochschule Wien` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)
- `Pädagogischen Hochschule Wien` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Auf der Homepage der <<<Universität Wien sei folgende Formulierung>>> zu finden:  „Wird das Studium erst später gewechselt, entfällt ...
```

FP: `Universität Wien sei folgende Formulierung` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
...  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der <<<Universität Wien in>>> der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde ...
```

FP: `Universität Wien in` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Universität Wien` (organisation)

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Gegen dieses Erkenntnis ist eine ordentliche Revision an den <<<Verwaltungsgerichtshof>>> nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... DBA-Durchführungs-Anpassungsverordnung und auf ein Erkenntnis des <<<VwGH>>>  verwiesen (Ra 2020/13/0089).
```

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... dem vorerst zu entgegnen, dass nach der Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Nach ständiger Rechtsprechung des <<<Verwaltungsgerichtshofes>>> sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Der Bf. ist daher auf die ständige Rechtsprechung des <<<Verwaltungsgerichtshofes>>> zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Gegen dieses Erkenntnis ist eine ordentliche Revision an den <<<Verwaltungsgerichtshof>>> nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht ...
```

FP: `Verwaltungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Einwendungen (vor allem  Bescheidbeschwerden) nachzuholen (<<<VwGH>>> 17.10.2001, 98/13/0073;
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
<<<VwGH>>> 27.3.1996, 92/13/0291;
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
<<<VwGH>>> 20.6.1990, 89/13/0249;
```

FP: `VwGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Steuerschuldner durch Bevorzugung unehrlicher, zu  berücksichtigen (<<<VwGH>>> 4.4.1989, 88/14/0245;
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... dem vorerst zu entgegnen, dass nach der Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Nach ständiger Rechtsprechung des <<<Verwaltungsgerichtshofes>>> sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Der Bf. ist daher auf die ständige Rechtsprechung des <<<Verwaltungsgerichtshofes>>> zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren ...
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... insbesondere weil  das Erkenntnis von der Rechtsprechung des <<<Verwaltungsgerichtshofes>>> abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende ...
```

```
... zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> nicht einheitlich beantwortet wird.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Studium Rechtswissenschaften nach der zitierten Judikatur des  <<<Verwaltungsgerichtshofes>>> (VwGH 01.02.1990, 89/12/0175) als Studienwechsel.
```

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... dem vorerst zu entgegnen, dass nach der Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> (VwGH 14.1.1991, 90/15/0060) auch die Notwendigkeit,  Vermögenswerte ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Nach ständiger Rechtsprechung des <<<Verwaltungsgerichtshofes>>> sind für die Entscheidung bei  Nachsichtsersuchen die Vermögens- ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Der Bf. ist daher auf die ständige Rechtsprechung des <<<Verwaltungsgerichtshofes>>> zu § 236 BAO  zu verweisen, wonach den Antragsteller im Nachsichtsverfahren ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... insbesondere weil  das Erkenntnis von der Rechtsprechung des <<<Verwaltungsgerichtshofes>>> abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

```
... zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  <<<Verwaltungsgerichtshofes>>> nicht einheitlich beantwortet wird.
```

FP: `Verwaltungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Allem dann vor, wenn das Erkenntnis von der Rechtsprechung des <<<Verwaltungsgerichtshofes>>>  abweicht, eine solche Rechtsprechung fehlt oder die zu lösende ...
```

FP: `Verwaltungsgerichtshofes` (organisation)

```
... zu lösende Rechtsfrage in der bisherigen  Rechtsprechung des <<<Verwaltungsgerichtshofes>>> nicht einheitlich beantwortet wird.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Fischhamering, Österreich, gegen den von der belangten Behörde <<<Finanzamt Österreich>>> am 15. Mai 2025  zu Steuernummer 98-117/5180  ausgefertigten ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Hinterhütten, Österreich, vom 11. September 2023 gegen den Bescheid des <<<Finanzamtes  Österreich>>> vom 7. September 2023 betreffend   - Rückforderung von Familienbeihilfe ...
```

| Predicted | Gold |
|---|---|
| `Finanzamtes  Österreich` | `Finanzamtes  Österreich` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Babenham, Österreich, vom 26. Mai 2023 gegen den Bescheid des <<<Finanzamtes Österreich>>>  vom 28. April 2023 betreffend Abweisung des Antrages auf Familienbeihilfe ...
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr <<<Finanzamt Österreich>>>) vom 26. Juli  2017 betreffend Abweisung der Wiederaufnahme ...
```

```
... die Bescheide des FA St. Johann Tamsweg Zell am See (nunmehr  <<<Finanzamt Österreich>>>) vom 3. August 2017 betreffend Abweisung der Wiederaufnahme ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... betreffend Beschwerde vom 16. Mai 2024 gegen den  Bescheid des <<<Finanzamtes Österreich>>> vom 7. Mai 2024 betreffend Anspruchszinsen (§ 205  BAO) 2022 ...
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... über die Beschwerde vom 26. März 2025 gegen den Bescheid des <<<Finanzamtes  Österreich>>> vom 12. März 2025 über die Festsetzung von  Anspruchszinsen ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Unzulässigkeit der Revision:  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Revision  Nach Art 133 Abs. 4 B-VG ist gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> die Revision an  den Verwaltungsgerichtshof zulässig, wenn ...
```

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des <<<Bundesfinanzgerichtes>>> ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage ...
```

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Laut Amtsrevision wurde die Rechtsansicht des <<<Bundesfinanzgerichtes>>>, das freie Wahlrecht des  innerbetrieblichen Verlustausgleiches ...
```

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... und somit  der Verlustvortrag nicht in der im Erkenntnis des <<<Bundesfinanzgerichtes>>> dargestellten Höhe  zusteht (vgl. Seite 7 und 8 der VwGH-Entscheidung).
```

FP: `Bundesfinanzgerichtes` (organisation)

**✅ Gold Entities:**

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  <<<FAÖ>>> sowie ein Mitarbeiter der Abgabensicherung geladen wurden.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Beschwerdeführer, sein Steuerberater, ein Vertreter des Fachbereiches des  <<<FAÖ>>> sowie ein Mitarbeiter der Abgabensicherung geladen wurden.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... strittig, ob das Finanzamt Österreich (in der Folge  kurz: <<<FAÖ>>>) zur Erlassung der Beschwerdevorentscheidungen im Zusammenhang ...
```

```
... Zusammenhang mit vom  Finanzamt für Großbetriebe (in der Folge kurz: <<<FAG>>>) erlassenen Bescheiden zuständig ist.
```

| Predicted | Gold |
|---|---|
| `FAÖ` | `FAÖ` |
| `FAG` | `FAG` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Das <<<FAG>>> erließ am 21.8.2024 einen Bescheid über die Aufhebung des Umsatzsteuerbescheides ...
```

| Predicted | Gold |
|---|---|
| `FAG` | `FAG` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Am 5.11.2024 hob das <<<FAG>>> den Umsatzsteuerbescheid 2022 vom 21.8.2024  erneut nach § ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Verfahren wie folgt:   a) Sachverhalt und Verfahrensablauf bei der <<<Houdek Maschinenbau>>>, Str.Nr.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
95-002/7970, BV 24:  Das Unternehmen <<<Houdek Maschinenbau>>>  hat im Jahr 2007 ein Vermögen von 84 Tankstellen besessen.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... die Nachfolgejahre wurden folgende  Umgründungsschritte bei <<<Houdek Maschinenbau>>>  durchgeführt:  Auf Grundlage des Spaltungs- und Übernahmsvertrages ...
```

```
... des Spaltungs- und Übernahmsvertrages vom 18.08.2008 hat die <<<Houdek Maschinenbau>>>  mit Stichtag 31.12.2007 als übertragende Gesellschaft nach ...
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Zum Stichtag 31.12.2008 ist die <<<Houdek Maschinenbau>>>  mit dem verbliebenen Vermögen entsprechend  dem Umgründungsplan ...
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Umgründungsschritte (partielle)  Gesamtrechtsnachfolger der <<<Houdek Maschinenbau>>>, insoweit das auch nach der Abspaltung zum  31.12.2007 bei ...
```

```
... insoweit das auch nach der Abspaltung zum  31.12.2007 bei der <<<Houdek Maschinenbau>>>  verbliebende Vermögen betroffen ist.
```

| Predicted | Gold |
|---|---|
| `Houdek Maschinenbau` | `Houdek Maschinenbau` |
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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Ansatz blieb und die von der Invalidenversicherung sowie der <<<SUVA>>> ausbezahl- ten Invalidenrenten in der nachgewiesenen Höhe berücksichtigt ...
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Die beantragte Steu- erfreiheit der von der <<<SUVA>>> bezogenen Invalidenrente verneinte das Finanzamt indes mit ...
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Teil der Invali- denrente entfallenden Anteiles der von der <<<SUVA>>> einbehaltenen Quellensteuer (5.623,80 CHF)  geltend gemacht ...
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... Vertretung ergänzend vor, dass beim  Beschwerdeführer von der <<<SUVA>>> aufgrund eines Arbeitsunfalles im Jahr 2010 eine Beeinträch- ...
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... und Folge- jahre unter Berücksichtigung der gesamten von der <<<SUVA>>> bezogenen Invalidenrente fest, wo- gegen sich der Beschwerdeführer ...
```

| Predicted | Gold |
|---|---|
| `SUVA` | `SUVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... sicherung (IV) und der Schweizerischen Unfallversicherungsanstalt (<<<SUVA>>>) sowie einer Pensi- onskassenleistung resultierenden Einkünfte ...
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenver- sicherung` (organisation)
- `Schweizerischen Unfallversicherungsanstalt (SUVA)` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... und ursächlichen Umstände des Unfalles, aufgrund  dessen die <<<SUVA>>>-Rente gewährt wurde (zB Krankenhaus-Unfallberichte, Polizeiberichte, ...
```

FP: `SUVA` (organisation)

```
... Krankenhaus-Unfallberichte, Polizeiberichte,  Unterlagen der <<<SUVA>>>) und des Zusammenhanges mit der Beschäftigung;
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Unterlagen der <<<SUVA>>> zur Einschätzung des Grades der Behinderung (zB <<<SUVA>>>-Gutach- ten) und die zugrundeliegenden medizinischen Befunde ...
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Folge auch keine Feststellun- gen, ob und in welchem Ausmaß die <<<SUVA>>>-Rente im Hinblick auf das Erkenntnis des Verwal- tungsgerichtshofes ...
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... (Komplementärrente) von der Schweizeri- schen Unfallversicherungsanstalt (<<<SUVA>>>) in Höhe von jährlich 56.236,80 CHF.
```

FP: `SUVA` (organisation)

**✅ Gold Entities:**
- `Eidgenössischen Invalidenversicherung (IV)` (organisation)
- `Schweizeri- schen Unfallversicherungsanstalt (SUVA)` (organisation)

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Im Wintersemester 2018/2019 war sie an der <<<Wirtschaftsuniversität Wien>>> inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Im Wintersemester 2018/2019 war sie an der <<<Wirtschaftsuniversität Wien>>> inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  <<<Wirtschaftsuniversität Wien>>> in der Studienrichtung Wirtschaftsrecht (UJ033 500) inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... 2018/2019 bis Sommersemester 2019 (= 2 Semester) war sie an der  <<<Wirtschaftsuniversität Wien>>> in der Studienrichtung Wirtschaftsrecht inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Im Wintersemester 2018/2019 war sie an der <<<Wirtschaftsuniversität Wien>>> inskribiert.
```

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... folgende Unterlagen  vor:   Studienerfolgsnachweis an der <<<Wirtschaftsuniversität Wien>>> (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- ...
```

FP: `Wirtschaftsuniversität Wien` (organisation)

```
... Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (<<<WU Wien>>>) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- ...
```

FP: `WU Wien` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
 Studienerfolgsnachweis der <<<Johannes Kepler Universität Linz>>> (JKU Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften ...
```

FP: `Johannes Kepler Universität Linz` (organisation)

```
... absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der <<<JKU Linz>>>  angerechnet wurden
```

FP: `JKU Linz` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der <<<Johannes Kepler Universität Linz>>> (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember ...
```

FP: `Johannes Kepler Universität Linz` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der <<<Wirtschaftsuniversität Wien>>> (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der ...
```

FP: `Wirtschaftsuniversität Wien` (organisation)

```
... (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der <<<Johannes Kepler Universität Linz>>> (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder ...
```

FP: `Johannes Kepler Universität Linz` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU)` (organisation)
- `Johannes Kepler Universität Linz (JKU)` (organisation)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... abgelegten 42 ECTS an der WU Wien lediglich  24 ECTS an der <<<JKU Linz>>> angerechnet wurden.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... diese Bescheide Herrn F persönlich zugestellt würden, da die <<<ÖGK>>> die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... die oben  angeführten Abgaben - entsprechend dem Vorgehen der <<<ÖGK>>> - ebenfalls der Gmbh  vorgeschrieben worden, wären diese Abgaben ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Zuge derselben GPLB angefallen seien,  seien diese seitens der <<<ÖGK>>> der GmbH vorgeschrieben worden, sodass Herr F nicht damit  ...
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... in die Databox des EU gerichtet  wurden, die Bescheide der <<<ÖGK>>> allerdings an die GmbH übermittelt wurden.
```

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... diese Bescheide Herrn F persönlich zugestellt würden, da die <<<ÖGK>>> die SV-Abgaben, die  sich aus derselben Prüfung ergeben hätten, ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des <<<Magistrates der Stadt Wien, Magistratsabteilung 6>>>,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen ...
```

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 6` | `Magistrates der Stadt Wien, Magistratsabteilung 6` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... dessen Beschwerde vom  14.1.2021 gegen das Straferkenntnis des <<<Magistrates der Stadt Wien, Magistratsabteilung 6>>>,  vom 28.12.2020, GZ: MA6/196000000656/2019, wegen 22 Verwaltungsübertretungen ...
```

| Predicted | Gold |
|---|---|
| `Magistrates der Stadt Wien, Magistratsabteilung 6` | `Magistrates der Stadt Wien, Magistratsabteilung 6` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Oktober 2025, gegen das Straferkenntnis der belangten  Behörde <<<Magistrat der Stadt Wien, MA 67>>>, als Abgabenstrafbehörde, vom 18. September  2025, GZ. MA67/GZ/2025, ...
```

```
... Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des <<<Magistrates der Stadt Wien>>> bestätigt.
```

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
III. Gemäß § 25 Abs. 2 BFGG wird der <<<Magistrat der Stadt Wien>>> als Vollstreckungsbehörde  bestimmt.
```

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Der <<<Magistrat der Stadt Wien, Magistratsabteilung 67>>>, forderte die Firma Firma, AdrFirma, als  Zulassungsbesitzerin ...
```

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, Magistratsabteilung 67` | `Magistrat der Stadt Wien, Magistratsabteilung 67` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  <<<Magistrates der Stadt Wien, Magistratsabteilung 6>>> - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang ...
```

FP: `Magistrates der Stadt Wien, Magistratsabteilung 6` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Mag. Renate Schohaj` (person)
- `Martina Hennefahrt` (person)
- `Grete von Zieritz-Gasse 46, 8940 Weißenbach bei Liezen, Österreich` (address)
- `Magistrates der Stadt Wien, Magistratsabteilung 6 - BA32` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... vom 2. Oktober 2025, gegen die Vollstreckungsverfügung des  <<<Magistrates der Stadt Wien, Magistratsabteilung 6>>> - BA32, vom 1. September 2025, GZ.  MA67/GZ1/2024, in Zusammenhang ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Kff. Sandra Khartchenko  als Rechtsnachfolger der <<<Roelfsen Versicherung>>>, Schölmlahn 46, 6380 St. Johann in Tirol, Österreich, vertreten ...
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Kff. Sandra Khartchenko  als RNF der <<<Roelfsen Versicherung>>>  Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als ...
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... betreffend Feststellungsbescheid Gruppenmitglied 2010 erlassen (<<<Roelfsen Versicherung>>>  St. Nr. 85-900/3590) und das Verfahren wiederaufgenommen.
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Bescheidadressaten waren  sowohl das Gruppenmitglied <<<Roelfsen Versicherung>>>  als auch der Gruppenträger Lubomir Merschmeyer  (02-013/5959).
```

| Predicted | Gold |
|---|---|
| `Roelfsen Versicherung` | `Roelfsen Versicherung` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Generalversammlungsbeschlusses vom  19.08.2009 eine Abspaltung zur Aufnahme in die <<<Roelfsen Versicherung>>>  durch Übertragung des  gesamten Betriebes (mit Ausnahme der ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Im Wirtschaftsjahr 2007 ist gemäß der beim <<<FA Wien 1/23>>>  eingereichten  Körperschaftsteuererklärung 2007 ein steuerlicher ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Am 26.04.2013 erließ das <<<FA Wien 1/23>>>  nach Durchführung der Außenprüfung je einen  Körperschaftsteuerbescheid ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Mit Vorlagebericht vom 13.11.2013 hat das <<<FA Wien 1/23>>>  die eingebrachte Beschwerde (ohne Erlassung einer Beschwerdevorentscheidung) ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... RV/5101064/2013) und den Körperschaftsteuerbescheid 2007 des <<<FA Wien 1/23>>>  gegenüber der  mitbeteiligten Partei Roelfsen Versicherung ...
```

| Predicted | Gold |
|---|---|
| `FA Wien 1/23` | `FA Wien 1/23` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des <<<FA Wien 1/23>>>  in vollem Umfang im Zuge einer Amtsrevision  angefochten.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... befunden, da er als  handelsrechtlicher Geschäftsführer der <<<KQPC Versand GMBH>>>  vor der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, ...
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Zudem  wurde im Straferkenntnis ausgesprochen, dass die <<<KQPC Versand GMBH>>>  gem § 9 Abs 7 VStG über  die verhängten Geldstrafen und die ...
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Juni bis Dezember 2017 bereits Verjährung eingetreten und die  <<<KQPC Versand GMBH>>>  im Jänner 2018 nicht mehr tätig gewesen sei.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... inkriminierten Zeitraum sowohl handelsrechtlicher Geschäftsführer  der <<<KQPC Versand GMBH>>>  als auch der Event Sudkraftlex GMBH.
```

| Predicted | Gold |
|---|---|
| `KQPC Versand GMBH` | `KQPC Versand GMBH` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Die <<<KQPC Versand GMBH>>>  war Bauherrin und  Auftraggeber (Gebraucher) der Umbauarbeiten ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... abgabenrechtlichen Nachbemessungsbescheid vom 16.1.2018 an die <<<Event Sudkraftlex GMBH>>>  hinsichtlich der oa.
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Bescheides gegen den Beschuldigten als Geschäftsführer der <<<Event Sudkraftlex GMBH>>>  ein  Verwaltungsstrafverfahren geführt und die Strafverfügung ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... handelsrechtlicher Geschäftsführer  der KQPC Versand GMBH  als auch der <<<Event Sudkraftlex GMBH>>>.
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... der Spiegelgrundstraße 45, 5061 Vorderfager, Österreich, die <<<Event Sudkraftlex GMBH>>>  war  mit dem Bauvorhaben befasst bzw. bauausführende Firma ...
```

| Predicted | Gold |
|---|---|
| `Event Sudkraftlex GMBH` | `Event Sudkraftlex GMBH` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... MA6/ARP-S- 780/2018 u.a., als handelsrechtlicher Geschäftsführer der <<<Event Sudkraftlex GMBH>>>  hinsichtlich der  Spiegelgrundstraße 45, 5061 Vorderfager, ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
über die Beschwerden vom 29. März 2019 gegen den Bescheid des <<<Finanzamt Wien 1/23>>>  vom 29. Jänner  2019 betreffend Wiederaufnahme § 303 BAO / ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Unmittelbar nachfolgend hat das BFG die Amtsrevision des <<<Finanzamt Wien 1/23>>> (samt Veranlagungsakten  sowie Auszügen aus dem Arbeitsbogen ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... 13.09.2018 zu Ro 2016/15/0010 hat der VwGH die  Amtsrevision des <<<Finanzamt Wien 1/23>>>  als unbegründet abgewiesen.
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Begründend  wurde deshalb durch das <<<Finanzamt Wien 1/23>>>  im Sachbescheid Feststellungsbescheid Gruppenmitglied  2010 ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 1/23` | `Finanzamt Wien 1/23` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... 27.01.2016 für das Jahr 2007 (Rechtsvorgänger) wurde  seitens des <<<Finanzamt Wien 1/23>>>  mittels Amtsrevision bekämpft.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Bescheinigung der für diese Feststellung zuständigen Stelle - hier das  <<<Bundesamt für Soziales und Behindertenwesen>>> (Sozialministeriumservice) – nachzuweisen ist.
```

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... bei Zusammentreffen von   Behinderungen verschiedener Art das <<<Bundesamt für Soziales und Behindertenwesen>>>;
```

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Die zuständige Stelle ist im  gegenständlichen Fall das <<<Bundesamt für Soziales und Behindertenwesen>>>  (Sozialministeriumservice).
```

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Die Bescheinigung des <<<Bundesamts für Soziales  und Behindertenwesen>>> (Sozialministeriumservice) als gesetzlich ausdrücklich geforderter ...
```

| Predicted | Gold |
|---|---|
| `Bundesamts für Soziales  und Behindertenwesen` | `Bundesamts für Soziales  und Behindertenwesen` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... welchem Ausmaß eine Behinderung vorliegt, obliegt nur dem  <<<Bundesamt für Soziales und Behindertenwesen>>> (Sozialministeriumservice).
```

| Predicted | Gold |
|---|---|
| `Bundesamt für Soziales und Behindertenwesen` | `Bundesamt für Soziales und Behindertenwesen` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Erwerbsfähigkeit durch eine amtliche Bescheinigung (hier: des  <<<Bundesamtes für Soziales und Behindertenwesen>>>) nachgewiesen wird (§ 35 Abs. 2 EStG 1988).
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
So konnten seitens des <<<Bundesfinanzgerichts>>> keine Feststellungen  hinsichtlich eines unverschuldeten oder ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Sachverhaltsfeststellungen ergeben sich nach Dafürhalten des <<<Bundesfinanzgerichts>>> aus  den vorgelegten Akten des Abgabenverfahrens, dem Vorbringen ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Von Seiten des <<<Bundesfinanzgerichts>>> wird darauf verwiesen, dass § 1116 ABGB den  Vertragsparteien ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Von Seiten des <<<Bundesfinanzgerichts>>> wird einleitend nochmals auf den Umstand hingewiesen,  dass ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Beschwerde wurde der nunmehr zuständigen Gerichtsabteilung des <<<Bundesfinanzgerichts>>>  aufgrund einer Verfügung des Geschäftsverteilungsausschusses ...
```

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Das Erkenntnis des <<<Bundesfinanzgerichts>>>, Außenstelle Linz, vom 27.01.2016, GZ  RV/5101064/2013, wurde ...
```

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Höhe und somit nicht in der im angefochtenen Erkenntnis des  <<<Bundesfinanzgerichts>>> dargestellten Höhe zustehe, erweise sich der Spruch des angefochtenen ...
```

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)
- `X GmbH` (organisation)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Rechtsvorgängers Houdek Maschinenbau  wurde das Erkenntnis des  <<<Bundesfinanzgerichts>>>, Außenstelle Linz, am 27.01.2016 zu GZ RV/5101064/2013 zum ...
```

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `85-900/3590` (tax_number)
- `Roelfsen Versicherung` (organisation)
- `UFS` (organisation)
- `Houdek Maschinenbau` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Höhe und somit nicht in der im angefochtenen  Erkenntnis des <<<Bundesfinanzgerichts>>> dargestellten Höhe zusteht, erweist sich der Spruch des  angefochtenen ...
```

FP: `Bundesfinanzgerichts` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)
- `X GmbH` (organisation)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Beschwerde wurde der nunmehr zuständigen Gerichtsabteilung des <<<Bundesfinanzgerichts>>>  aufgrund einer Verfügung des Geschäftsverteilungsausschusses ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Bescheidbegründung waren Online-Angebote von Küchenzeilen der Unternehmen <<<Ikea>>>,  Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at ...
```

```
... waren Online-Angebote von Küchenzeilen der Unternehmen Ikea,  <<<Obi>>>, Leiner, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

```
... Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, <<<Leiner>>>, Möbelix, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

```
... Online-Angebote von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, <<<Möbelix>>>, MömaX, Otto.de, xxxLutz und Quelle.at angefügt.
```

```
... von Küchenzeilen der Unternehmen Ikea,  Obi, Leiner, Möbelix, <<<MömaX>>>, Otto.de, xxxLutz und Quelle.at angefügt.
```

| Predicted | Gold |
|---|---|
| `Ikea` | `Ikea` |
| `Obi` | `Obi` |
| `Leiner` | `Leiner` |
| `Möbelix` | `Möbelix` |
| `MömaX` | `MömaX` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
...  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst <<<SENECURA>>> 1.026,29 Euro, Eigenanteil lt Bestätigung <<<SENECURA>>>  3.378,91 ...
```

```
... Hilfsdienst <<<SENECURA>>> 1.026,29 Euro, Eigenanteil lt Bestätigung <<<SENECURA>>>  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 ...
```

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |
| `SENECURA` | `SENECURA` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Für 2017: Mobiler Hilfsdienst <<<SENECURA>>> 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 ...
```

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... Verausgabungen und Kosten der Mutter, Aufgabe des Mobilen  Hilfsdienst <<<SENECURA>>>, Nachweis der Aktiva des Nachlasses der verstorbenen Mutter, ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Vermögen, bestehend aus 11 einzeln  benannten Tankstellen, auf die <<<Schmeltz Luftfahrt>>>  übertragen.
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Die <<<Schmeltz Luftfahrt>>>  ist zum  31.10.2010 als übertragende Gesellschaft mit Dorfcon-Verlag ...
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Dorfcon-Verlag  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der <<<Schmeltz Luftfahrt>>> (partielle)  Gesamtrechtsnachfolgerin der Houdek Maschinenbau.
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Teilbetriebe  <<<Schmeltz Luftfahrt>>>:   Verluste  geschlossene  Teilbetriebe  Houdek Maschinenbau: ...
```

| Predicted | Gold |
|---|---|
| `Schmeltz Luftfahrt` | `Schmeltz Luftfahrt` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Abgespaltene  Tankstellen  <<<Schmeltz Luftfahrt>>> **   Geschlossene  Tankstellen  Houdek Maschinenbau **  Verkaufte ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Haan,  Oisching 129, 3071 Wiesen, Österreich, vertreten durch <<<Merkur Treuhand Steuerberatung GmbH>>>, St.-Veit-Gasse 50,  1130 Wien, über die Beschwerde vom 16. ...
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... bei der belangten Behörde am selben Tage,  übermittelte die <<<Merkur Treuhand Steuerberatung GmbH>>> der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin ...
```

```
... unterfertigte Vollmacht, womit die  Beschwerdeführerin die <<<Merkur Treuhand Steuerberatung GmbH>>> als „Vertreter in allen  steuerlichen, wirtschaftlichen und ...
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Weiters wurde  der <<<Merkur Treuhand Steuerberatung GmbH>>> darin die Vollmacht „zum Empfang von  Schriftstücken, insbesondere ...
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung GmbH` | `Merkur Treuhand Steuerberatung GmbH` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Im (Begleit-) Schreiben vom 13.3.2024 führt die <<<Merkur Treuhand Steuerberatung  GmbH>>> aus, dass die Vollmacht als „Spezialvollmacht für das laufende ...
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand Steuerberatung  GmbH` | `Merkur Treuhand Steuerberatung  GmbH` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  <<<Merkur Treuhand Steuerberatung GmbH>>> weiter.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
...  zusammengesetzt wie folgt:  Für 2016: Mobiler Hilfsdienst <<<SENECURA>>> 1.026,29 Euro, Eigenanteil lt Bestätigung <<<SENECURA>>>  3.378,91 ...
```

```
... Hilfsdienst <<<SENECURA>>> 1.026,29 Euro, Eigenanteil lt Bestätigung <<<SENECURA>>>  3.378,91 Euro, PVA-Abzüge (=Kostenanteil von Pension) 9.778,77 ...
```

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |
| `SENECURA` | `SENECURA` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Für 2017: Mobiler Hilfsdienst <<<SENECURA>>> 485,50 Euro, PVA-Abzüge (=Kostenanteil von Pension)  12.560,88 ...
```

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Verausgabungen und Kosten der Mutter, Aufgabe des Mobilen  Hilfsdienst <<<SENECURA>>>, Nachweis der Aktiva des Nachlasses der verstorbenen Mutter, ...
```

| Predicted | Gold |
|---|---|
| `SENECURA` | `SENECURA` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... 25.04.2016 (es wurden 4 weitere Rechnungen/Bestätigungen der <<<SeneCura>>>  im Rahmen des Ermittlungsverfahrens von der Bf bzw von deren ...
```

| Predicted | Gold |
|---|---|
| `SeneCura` | `SeneCura` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... der Bf war in den streitgegenständlichen Jahren im Pflegeheim <<<SeneCura Laurentius  Park Bludenz>>> (beginnend ab 28.01.2016) untergebracht.
```

| Predicted | Gold |
|---|---|
| `SeneCura Laurentius  Park Bludenz` | `SeneCura Laurentius  Park Bludenz` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Dazu wurden von der Bf Bestätigungen der PVA, dem <<<SeneCura>>> Laurentius-Park Bludenz und  diverse Arzthonorare von Fachärzten ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Luftfahrt  ist zum  31.10.2010 als übertragende Gesellschaft mit <<<Dorfcon-Verlag>>>  verschmolzen worden.
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Die <<<Dorfcon-Verlag>>>  ist  auf Grund der Verschmelzung zum 31.10.2010 mit der Schmeltz ...
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Lexdon IT  und einen Körperschaftsteuerbescheid 2007 an die <<<Dorfcon-Verlag>>>, da diese Gesellschaften auf  Grund der Abspaltung der 11 Tankstellen ...
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... erzielten  Verlust 2007 zwischen Roelfsen Versicherung  und <<<Dorfcon-Verlag>>>  grundsätzlich entsprechend der  Zuordnung der Einkünfte zu ...
```

| Predicted | Gold |
|---|---|
| `Dorfcon-Verlag` | `Dorfcon-Verlag` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... ermittelte Verlust wäre  daher zwischen Roelfsen Versicherung  und <<<Dorfcon-Verlag>>>  wie folgt aliquot (unter Außerachtlassung  einer geringfügigen ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der <<<JKU>>> um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: ...
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Siehe Internetseite <<<JKU>>> und WU  Karriereaussichten!
```

```
Siehe Internetseite JKU und <<<WU>>>  Karriereaussichten!
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |
| `WU` | `WU` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Wirtschaftswissenschaften an der WU  Wien und BA Wirtschaftswissenschaften an der <<<JKU>>> um dasselbe Studium handelt,  dürfen wir Ihnen folgendes mitteilen: ...
```

| Predicted | Gold |
|---|---|
| `JKU` | `JKU` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
 Beispieldarstellung Übereinstimmung Lehrplan <<<WU>>> mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, ...
```

```
 Beispieldarstellung Übereinstimmung Lehrplan WU mit <<<JKU>>>:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10 ...
```

| Predicted | Gold |
|---|---|
| `WU` | `WU` |
| `JKU` | `JKU` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... sozialwissenschaftliche Grundlagen,  auswählbare Studienzweige (<<<WU>>>: „Betriebswirtschaft“, „Internationale Betriebswirtschaft“, ...
```

```
... „Volkswirtschaft und Sozioökonomie“) bzw. Studienschwerpunkte  (<<<JKU>>>: „Betriebswirtschaftslehre“, „Internationale Betriebswirtschaftslehre“, ...
```

| Predicted | Gold |
|---|---|
| `WU` | `WU` |
| `JKU` | `JKU` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (<<<WU>>> Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- ...
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `Wirtschaftsuniversität Wien (WU Wien)` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
 Abgangsbescheinigung der <<<WU>>> Wien vom 28.12.2020 betreffend das Bachelorstudium  Wirtschafts- ...
```

FP: `WU` (organisation)

**✅ Gold Entities:**
- `WU Wien` (organisation)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Studienerfolgsnachweis der Johannes Kepler Universität Linz (<<<JKU>>> Linz) vom  06.12.2020 betreffend das Bachelorstudium Wirtschaftswissenschaften ...
```

FP: `JKU` (organisation)

```
... dass Lehrveranstaltungen im Ausmaß  von 31 ECTS-Punkten an der <<<JKU>>> Linz absolviert wurden und dass an der WU Wien  absolvierte ...
```

FP: `JKU` (organisation)

```
... ECTS-Punkten an der JKU Linz absolviert wurden und dass an der <<<WU>>> Wien  absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten ...
```

FP: `WU` (organisation)

```
... absolvierte Lehrveranstaltungen im Ausmaß von 24 ECTS-Punkten an der <<<JKU>>> Linz  angerechnet wurden
```

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `Johannes Kepler Universität Linz (JKU Linz)` (organisation)
- `JKU Linz` (organisation)
- `WU Wien` (organisation)
- `JKU Linz` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
 Abgangsbescheinigung der <<<JKU>>> Linz vom 14.12.2020 betreffend das Bachelorstudium  Wirtschaftswissenschaften ...
```

FP: `JKU` (organisation)

**✅ Gold Entities:**
- `JKU Linz` (organisation)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... der  Beschwerde angekündigte Nachreichung der Unterlagen der <<<WU>>> Wien (Vergleich der  Studienrichtungen).
```

FP: `WU` (organisation)

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
...  wurde von einem Kontrollorgan der Parkraumüberwachung der <<<Landespolizeidirektion Wien>>>  (A118) am 18. April 2025 um 11:07 Uhr in 1120 Wien, Meidlinger ...
```

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... welche von einem Organ des Parkraumüberwachungsorgans  der <<<Landespolizeidirektion Wien>>> aufgrund eigener dienstlicher Wahrnehmung gelegt wurde,  ergibt ...
```

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... W-Kennz. (A) wurde vom  Kontrollorgan der Parkraumüberwachung der <<<Landespolizeidirektion Wien>>> am 07. Mai 2025  um 11:59 Uhr in der gebührenpflichtigen Kurzparkzone ...
```

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Am 11. September 2019 bewilligte die <<<Landespolizeidirektion Wien>>> - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz ...
```

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Am 20. Februar 2020 überwies der Bf. € 173,10 an die <<<Landespolizeidirektion Wien>>> -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Reisekosten wie folgt auf:  Einsätze für die Grenzschutzagentur <<<Frontex>>>: versteuerte Taggelder  Einsatz im Jahr 2018 als <<<Frontex>>>-Beamter ...
```

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Werbungskosten die in Zusammenhang mit <<<Frontex>>>, EASO, ... Einsätzen stehen, dürfen daher in  solchen Fällen ...
```

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... ausgenommenen Taggelder in Zusammenhang mit dem Kurzzeiteinsatz für  <<<Frontex>>> auch die laut Reisekosten-Beilage gesondert beantragten Kilometer-/ ...
```

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... und wurde gemäß § 39a BDG in der Zeit 26. Februar 2025  an <<<Frontex>>> entsendet und war im Auslandseinsatz in Sizilien.
```

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Flughafen München mit dem  privaten PKW wurden dem Bf. vom BMI bzw. <<<Frontex>>> nicht ersetzt.
```

| Predicted | Gold |
|---|---|
| `Frontex` | `Frontex` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Grenzschutzagentur <<<Frontex>>>: versteuerte Taggelder  Einsatz im Jahr 2018 als <<<Frontex>>>-Beamter in  Sardinien (I) vom 04.06.
```

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Frontex` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Einsatz im Jahr 2019 als <<<Frontex>>>-Beamter in  Sizilien (I) vom 16.07.
```

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
<<<Frontex>>>-Einsatz: Anreise  zumFlugh.
```

FP: `Frontex` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
<<<Frontex>>>-Einsatz in Sizilien  (Trapani) 31 x Frühstück a'  5,85   181,35 ...
```

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Trapani` (city)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... einmal für die Organisation "Europäische Grenzschutzagentur  <<<Frontex>>>" in Trapani auf der Insel Silzilien (I) tätig.
```

FP: `Frontex` (organisation)

**✅ Gold Entities:**
- `Europäische Grenzschutzagentur  Frontex` (organisation)
- `Trapani` (city)

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... übertragende Gesellschaft (neben anderen Gesellschaften) mit der  <<<Lexdon IT>>>  als übernehmende Gesellschaft verschmolzen worden.
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Die <<<Lexdon IT>>>  und  Roelfsen Versicherung  sind aufgrund der dargestellten ...
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... 2007 iSd § 19 Abs. 1 BAO an die Roelfsen Versicherung, die <<<Lexdon IT>>>  und einen Körperschaftsteuerbescheid 2007 an die Dorfcon-Verlag, ...
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Der <<<Lexdon IT>>>  als weiterem partiellen  Gesamtrechtsnachfolger wurde ein ...
```

| Predicted | Gold |
|---|---|
| `Lexdon IT` | `Lexdon IT` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Rechtsmeinung des Beschwerdeführers geteilt, wonach der bei der  <<<Lexdon IT>>>  im Jahr 2007 insgesamt entstandene Verlust nach Vornahme des ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... die Ausbildung zur Steuerassistentin und ein Schreiben der <<<Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith>>>, in dem bestätigt wurde, dass die  Tochter die Schule in der ...
```

| Predicted | Gold |
|---|---|
| `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith` | `Schule  für allgemeine Gesundheits- und Krankenpflege Grillenreith` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Bakk. techn.  war von 1.10.2016 bis 4.10.2017 Schülerin an der <<<Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith>>>.
```

| Predicted | Gold |
|---|---|
| `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith` | `Schule für  allgemeine Gesundheits- und Krankenpflege am LKH Grillenreith` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... im Oktober  2017 aus gesundheitlichen Gründen die allgemeine <<<Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith>>>  nicht weiterführen konnte, hat sie diese Ausbildung beendet.
```

| Predicted | Gold |
|---|---|
| `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith` | `Gesundheits- und Krankenpflege-Schule am  LKH Grillenreith` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... Stella Marschalk, Bakk. techn.  war vom 1.10.2016 an in der <<<Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith>>>  in Ausbildung zur Krankenpflegerin.
```

| Predicted | Gold |
|---|---|
| `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith` | `Schule für allgemeine Gesundheits- und  Krankenpflege Grillenreith` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Dem Vorlageantrag beigelegt war ein Schreiben der <<<Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith>>>, in dem bestätigt wurde, dass Stella Marschalk, Bakk. techn. ...
```

| Predicted | Gold |
|---|---|
| `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith` | `Schule für allgemeine Gesundheits- und  Krankenpflege in Grillenreith` |

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Bf. nach Rückfrage mit, dass die An- und Rückreisekosten  zum <<<Flughafen München>>> mit dem privat PKW ohne entsprechende Belege laut Anweisung ...
```

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Frühstückskosten iHv € 181,35, sowie An- und Rückreisekosten zum <<<Flughafen  München>>> iHv € 173,80.
```

| Predicted | Gold |
|---|---|
| `Flughafen  München` | `Flughafen  München` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Die An- und Rückreisekosten zum <<<Flughafen München>>> mit dem  privaten PKW wurden dem Bf. vom BMI bzw. Frontex nicht ...
```

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... pauschale Frühstückskosten sowie die An- und  Rückreisekosten zum <<<Flughafen München>>> als Werbungskosten im Zusammenhang mit der  Auslandstätigkeit ...
```

| Predicted | Gold |
|---|---|
| `Flughafen München` | `Flughafen München` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Die Kosten für die Fahrt  zwischen Wohnort und <<<Flughafen München>>>, die der Bf. mit dem eigenen PKW zurückgelegt  hat, wurden ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Die Tochter studiert an der <<<University of Bristol>>> bis voraussichtlich Juli 2023.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... getragen hat  und ab September 2020 in einem Studentenwohnheim der <<<University of Bristol>>>.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Am 11. Dezember 2020 bestätigte die <<<University of Bristol>>>, that Miss Maximiliane Sakschewsky, MA (Tochter  des Bf.) student ...
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
2…7 is studying for a Chemistry (BSc) full time at the <<<University of Bristol>>>.
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Miss Maximiliane Sakschewsky, MA … started at the <<<University of Bristol>>> on 28 September 2020 and is  expected to complete her course ...
```

| Predicted | Gold |
|---|---|
| `University of Bristol` | `University of Bristol` |

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Abgabenschuldner“) wurden der Beschwerdeführerin am 5.4.2024 zu  Handen der <<<Schabetsberger Steuerberatung GmbH>>>, Fischerstiege 9, 1010 Wien, zugestellt.
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Die <<<Schabetsberger Steuerberatung GmbH>>> leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 ...
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Mitarbeiter oder eine  Mitarbeiterin (Unterschrift unleserlich) der <<<Schabetsberger Steuerberatung GmbH>>> die  Übernahme dieser beiden Bescheide am 5.4.2024 bestätigt, ...
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... Vollmachten (daher auch eine allfällige Zustellvollmacht der  <<<Schabetsberger Steuerberatung GmbH>>>) aufgelöst.
```

| Predicted | Gold |
|---|---|
| `Schabetsberger Steuerberatung GmbH` | `Schabetsberger Steuerberatung GmbH` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
Die Zustellung an die <<<Schabetsberger  Steuerberatung GmbH>>> war unwirksam.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Zeit eines Verfahrens vor dem Verwaltungsgerichtshof, vor dem <<<Verfassungsgerichtshof>>>  oder vor dem Gerichtshof der Europäischen Union.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... hat,  den Antrag auf Aufhebung dieser Rechtsvorschrift beim <<<Verfassungsgerichtshof>>> zu stellen.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Verwaltungsgerichtshof (§ 25a Abs. 2 Z 1 VwGG) oder eine Beschwerde an den  <<<Verfassungsgerichtshof>>> (§ 88a Abs. 2 VfGG) nicht zulässig.
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
Darüber hinaus hat der <<<Verfassungsgerichtshof>>> in seinem Beschluss vom 19. September 2025  zu E 1733/2025 ...
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... unmittelbar im Zusammenhang mit dem  DBA Deutschland - vom <<<Verfassungsgerichtshof>>> geprüft und als verfassungskonform beurteilt  wurde (vgl VfGH ...
```

| Predicted | Gold |
|---|---|
| `Verfassungsgerichtshof` | `Verfassungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Der <<<Verfassungsgerichtshof>>> (vgl. VfGH B 783/89 vom 06.12.1990) hat bereits ausgesprochen, ...
```

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Der <<<Verfassungsgerichtshof>>> ist bei der o.a, Entscheidung zum Ergebnis gelangt, dass ein ...
```

FP: `Verfassungsgerichtshof` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Dies unter Bezug auf ein Erkenntnis des  <<<Verfassungsgerichtshofes>>> (VfGH 6.12.1990, B 783/89), wonach eine Entscheidung derselben ...
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
2.4 Zitierte Entscheidung des <<<Verfassungsgerichtshofes>>> gegenständlich nicht einschlägig   Wie das Finanzamt unter ...
```

FP: `Verfassungsgerichtshofes` (organisation)

```
... einschlägig   Wie das Finanzamt unter Hinweis auf ein Erkenntnis des <<<Verfassungsgerichtshofes>>> (6.12.1990,  B 783/89) ausführt, könne eine Wiederaufnahme ...
```

FP: `Verfassungsgerichtshofes` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Im der  zitierten Entscheidung des <<<Verfassungsgerichtshofes>>> zugrundeliegenden Sachverhalt war  strittig, ob bei nachträglicher ...
```

FP: `Verfassungsgerichtshofes` (organisation)

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Dort besuchte Maximiliane Sakschewsky, MA  ab Herbst 2014 das <<<King's School>>>.
```

| Predicted | Gold |
|---|---|
| `King's School` | `King's School` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Matura - in England Advanced Level  genannt - noch ein Jahr im <<<King's School>>> absolvieren müssen.
```

| Predicted | Gold |
|---|---|
| `King's School` | `King's School` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte <<<The King´s School Worcester>>>:  I am writing to confirm that Maximiliane Sakschewsky, MA ...
```

```
... Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of <<<The King's  School Worcester>>> from September 2014 until July 2020.
```

| Predicted | Gold |
|---|---|
| `The King´s School Worcester` | `The King´s School Worcester` |
| `The King's  School Worcester` | `The King's  School Worcester` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... Sakschewsky, MA  war vom September 2014 bis Juli 2020 Schülerin der <<<King's School Worcester>>>,  Großbritannien.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Kontoinhaber des Kontos mit der  AT78 2024 1897 7421 2903  bei der <<<Raiffeisenbank Karnische Rion  Bankstelle St.Stefan>>>  sei.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... es bei dem Konto mit der AT78 2024 1897 7421 2903  bei der  <<<Raiffeisenbank Karnische Rion  Bankstelle St.Stefan>>>  um kein ODER-Konto, sondern ein UND-Konto handle.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Der <<<Raiffeisenbank Karnische Rion  Bankstelle St.Stefan>>>  wurde der Bescheid vom 10.10.2022 zugestellt und aufgetragen, ...
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... Kontoinhaber des Kontos mit der AT78 2024 1897 7421 2903  bei der  <<<Raiffeisenbank Karnische Rion  Bankstelle St.Stefan>>>.
```

| Predicted | Gold |
|---|---|
| `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` | `Raiffeisenbank Karnische Rion  Bankstelle St.Stefan` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... Beschwerdeführers betreffend  Konto AT78 2024 1897 7421 2903  bei der <<<Raiffeisenbank Karnische Rion  Bankstelle St.Stefan>>>  gründen sich auf die Kontenregisterauskunft.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Bezirkshauptmannschaft Bludenz getragen  werden würden, welche auch die von der <<<PVA>>> einbehaltenen Beträge (das waren die selbst zu  tragende Kosten) ...
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Dazu wurden von der Bf Bestätigungen der <<<PVA>>>, dem SeneCura Laurentius-Park Bludenz und  diverse Arzthonorare ...
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Davon wurde ein Selbstbetrag von der <<<PVA>>> direkt  an den Kostenträger zur teilweisen Deckung der Verpflegungskosten ...
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... (lt Verständigung über die Leistungshöhe zum 01.01.2017 der <<<PVA>>>  war dies ein Betrag von ca 200,00 bis 230,00 Euro) verblieb ...
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

**Example 4** (doc_id: ``) ( sent_id: ``)

```
... insbesondere den angeführten Aktenteilen wie den Bestätigungen der <<<PVA>>>, des SeneCura  Laurentius Park Bludenz und den Kontoauszügen.
```

| Predicted | Gold |
|---|---|
| `PVA` | `PVA` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... 1.026,29 Euro, Eigenanteil lt Bestätigung SENECURA  3.378,91 Euro, <<<PVA>>>-Abzüge (=Kostenanteil von Pension) 9.778,77 Euro (9x1.086,53).
```

FP: `PVA` (organisation)

**✅ Gold Entities:**
- `SENECURA` (organisation)
- `SENECURA` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Für 2017: Mobiler Hilfsdienst SENECURA 485,50 Euro, <<<PVA>>>-Abzüge (=Kostenanteil von Pension)  12.560,88 sowie eigene ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Beschwerdeführer eine Reihe von Urkunden, darunter ein Kreditantrag an die <<<Bankhaus Denzel>>>  vom 7.9.2000, einen Kfz-Zulassungsschein und eine Auflistung ...
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Kreditunterlagen aus dem Jahr 2000 sowie ein Schreiben der <<<Bankhaus Denzel>>>  vom 26.3.2015 vor,  worin ihm mitgeteilt wird, dass auf dem ...
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Beschwerdeführer einen Kredit über ATS 300.000,00 bei der  <<<Bankhaus Denzel>>>  zum Zwecke eines Hausbaues in Ungarn auf.
```

| Predicted | Gold |
|---|---|
| `Bankhaus Denzel` | `Bankhaus Denzel` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... 7.9.2000, der Selbstauskunft vom 31.8.2001 und  dem Schreiben der <<<Bankhaus Denzel>>>  vom 26.3.2015.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Berücksichtigung der € 2.114,80 ein berichtigter Lohnzettel des <<<BMI>>> wäre.
```

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... dem privat PKW ohne entsprechende Belege laut Anweisung des  <<<BMI>>> (National Frontex Point of Contact) nicht refundiert worden ...
```

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Flughafen München mit dem  privaten PKW wurden dem Bf. vom <<<BMI>>> bzw. Frontex nicht ersetzt.
```

| Predicted | Gold |
|---|---|
| `BMI` | `BMI` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... 2020/16/0039-6, liegt die  Grundausbildungsverordnung-Exekutivdienst <<<BMI>>> des Bundesministers für Inneres, BGBl. II  vom 12. Juni 2017, ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... und   2) Magdalena Diegmueller, LLB  als Rechtsnachfolger der <<<Lubomir Merschmeyer>>>, Hilfbergstraße 26, 4861 Pranzing, Österreich, vertreten durch ...
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Gruppenträger 02-013/5959 Magdalena Diegmueller, LLB  als RNF der <<<Lubomir Merschmeyer>>>
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Gruppenmitglied Roelfsen Versicherung  als auch der Gruppenträger <<<Lubomir Merschmeyer>>>  (02-013/5959).
```

| Predicted | Gold |
|---|---|
| `Lubomir Merschmeyer` | `Lubomir Merschmeyer` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... Unternehmensgruppe mit dem Gruppenträger Magdalena Diegmueller, LLB (vormals <<<Lubomir Merschmeyer>>>).
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  <<<Finanzamtes Wien 1/23>>> (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend ...
```

```
... über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  <<<Finanzamtes Wien 1/23>>> (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend ...
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |
| `Finanzamtes Wien 1/23` | `Finanzamtes Wien 1/23` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... über die Beschwerde vom 14. Juni 2012 gegen den Bescheid des  <<<Finanzamtes Wien 1/23>>> (nunmehr Finanzamt Österreich) vom 21. Mai 2012 betreffend ...
```

```
... über die Beschwerde vom 23. Mai 2013 gegen den Bescheid des  <<<Finanzamtes Wien 1/23>>> (nunmehr Finanzamt Österreich) vom 08. März 2013 betreffend ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... die Beschwerde vom 14. November 2016  gegen den Bescheid des <<<Finanzamtes Wien 9/18/19 Klosterneuburg>>> vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre ...
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... die Beschwerde vom 2.  November 2020 gegen den Bescheid des <<<Finanzamtes Wien 9/18/19 Klosterneuburg>>> (nunmehr  zuständig: Finanzamt Österreich) vom 9. September ...
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... der Beschwerde vom 19. April 2016 gegen die Bescheide des  <<<Finanzamtes Wien 9/18/19 Klosterneuburg>>>, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, ...
```

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... Einkommensteuerbescheiden für die Jahre 2001 bis  2003 vom 21.12.2011 setzte das <<<Finanzamt Wien 9/18/19 Klosterneuburg>>> (FA 07) die  Einkommensteuer des Beschwerdeführers (Bf.) u.a. ...
```

| Predicted | Gold |
|---|---|
| `Finanzamt Wien 9/18/19 Klosterneuburg` | `Finanzamt Wien 9/18/19 Klosterneuburg` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... über die Beschwerden vom 23. März 2015 gegen die Bescheide des <<<Finanzamtes Wien  3/6/7/11/15 Schwechat>>> Gerasdorf (heute zuständig: Finanzamt Österreich) vom 17. März ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  <<<Universität Wien>>> im Diplomstudium Rechtswissenschaften (UA101) inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der <<<Universität Wien>>> im Diplomstudium Rechtswissenschaften inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Wintersemester 2015/2016 bis Sommersemester 2018 (= 6 Semester) an der  <<<Universität Wien>>> im Diplomstudium Rechtswissenschaften (UA101) inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

**Example 3** (doc_id: ``) ( sent_id: ``)

```
... Wintersemester 2015/2016 bis Sommersemester 2018 (= 6  Semester) an der <<<Universität Wien>>> im Diplomstudium Rechtswissenschaften inskribiert.
```

| Predicted | Gold |
|---|---|
| `Universität Wien` | `Universität Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Sommersemester 2020 im Diplomstudium  Rechtswissenschaften an der <<<Universität Wien inskribiert>>>.
```

FP: `Universität Wien inskribiert` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Sommersemester 2020 das Studium  Rechtswissenschaften an der <<<Universität Wien betrieben>>>.
```

FP: `Universität Wien betrieben` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... fest:  T. brach nach vier Semestern das Lehramtsstudium an der <<<Universität Wien ab>>> und begann im  Wintersemester 2022/2023 an der Pädagogischen ...
```

FP: `Universität Wien ab` (organisation)

```
... und begann im  Wintersemester 2022/2023 an der Pädagogischen <<<Hochschule Wien>>> mit dem Bachelorstudium  Lehramt Primarstufe.
```

FP: `Hochschule Wien` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)
- `Pädagogischen Hochschule Wien` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Auf der Homepage der <<<Universität Wien sei folgende Formulierung>>> zu finden:  „Wird das Studium erst später gewechselt, entfällt ...
```

FP: `Universität Wien sei folgende Formulierung` (organisation)

**✅ Gold Entities:**
- `Universität Wien` (organisation)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
...  Die Tochter der Bf. war vom WS 2020/21 bis SS 2022 an der <<<Universität Wien in>>> der  Studienrichtung LA Sekundarstufe UF Biologie und Umweltkunde ...
```

FP: `Universität Wien in` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Universität Wien` (organisation)

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Eigeneinkommen der  Mutter der Bf gedeckten Heimkosten von der <<<Bezirkshauptmannschaft Bludenz>>> getragen  werden würden, welche auch die von der PVA einbehaltenen ...
```

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
werden und die Heimkosten würden von der <<<Bezirkshauptmannschaft Bludenz>>> getragen.
```

| Predicted | Gold |
|---|---|
| `Bezirkshauptmannschaft Bludenz` | `Bezirkshauptmannschaft Bludenz` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... welcher nicht  selbst getragen werden konnte, wurde von der <<<Bezirkshauptmannschaft Bludenz>>> getragen.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Ein Firmenbuchauszug vom 9.7.2024 ergab, dass die <<<Gözcü Getränke>>>  seit 15.5.2024 aufgrund  einer Neufassung des Gesellschaftsvertrages ...
```

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Die RgR Dipl. Kff. Sandra Khartchenko (im Beschwerdezeitraum <<<Gözcü Getränke>>>) war im Jahr 2010 Gruppenmittglied  der Unternehmensgruppe ...
```

| Predicted | Gold |
|---|---|
| `Gözcü Getränke` | `Gözcü Getränke` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
Die RgR Dipl. Kff. Sandra Khartchenko (im Beschwerdezeitraum <<<Gözcü Getränke>>>) ist als Rechtsnachfolgerin der  Roelfsen Versicherung  auch ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Schödensack, Ornetsedt 12, 4274 Kollnedt, Österreich, vertreten durch <<<Steuerberater Metzler & Adelsberger OG>>>,  Stadtgraben 25, 6060 Hall in Tirol, über die Beschwerde vom ...
```

| Predicted | Gold |
|---|---|
| `Steuerberater Metzler & Adelsberger OG` | `Steuerberater Metzler & Adelsberger OG` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Höllererweg 4, 2852 Maltern, Österreich, vertreten durch die <<<Achammer & Mennel Rechtsanwälte OG>>>,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des ...
```

| Predicted | Gold |
|---|---|
| `Achammer & Mennel Rechtsanwälte OG` | `Achammer & Mennel Rechtsanwälte OG` |

**Example 2** (doc_id: ``) ( sent_id: ``)

```
... Höllererweg 4, 2852 Maltern, Österreich, vertreten durch die <<<Achammer & Mennel Rechtsanwälte OG>>>,  Schloßgraben 10, 6800 Feldkirch, gegen die Bescheide des ...
```

| Predicted | Gold |
|---|---|
| `Achammer & Mennel Rechtsanwälte OG` | `Achammer & Mennel Rechtsanwälte OG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Aus dem Firmenbuch ist ersichtlich, dass der <<<Beschuldigte sowohl Geschäftsführer der GmbH  als auch verantwortlicher Gesellschafter der OG>>> war, somit in den verfahrensgegenständlichen  Zeiträumen Entscheidungsträger ...
```

FP: `Beschuldigte sowohl Geschäftsführer der GmbH  als auch verantwortlicher Gesellschafter der OG` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Aus dem Firmenbuch ist ersichtlich, dass der <<<Beschuldigte sowohl Geschäftsführer der GmbH  als auch verantwortlicher Gesellschafter der OG>>> war, somit in den verfahrensgegenständlichen  Zeiträumen Entscheidungsträger ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Auf den Lohnzettel des <<<BM für Inneres>>> wird verwiesen.
```

| Predicted | Gold |
|---|---|
| `BM für Inneres` | `BM für Inneres` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Der Betrag, welcher vom <<<BM für Inneres>>> als Bezüge gem. § 26 EStG ausbezahlt wird, betrifft  den Kfz-Aufwand, ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... wahrscheinlich die Dienstreisen im Zuge meiner  Tätigkeit bei der <<<Kriminalpolizei in Österreich>>>.
```

| Predicted | Gold |
|---|---|
| `Kriminalpolizei in Österreich` | `Kriminalpolizei in Österreich` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Dienstreisen ausschließlich im Rahmen der Tätigkeit bei der  <<<Kriminalpolizei in Österreich>>> getätigt worden seien.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Die Bf hat  nämlich ein für das <<<Arbeits- und Sozialgericht Wien>>> erstelltes berufskundliches  Sachverständigengutachten vom ...
```

| Predicted | Gold |
|---|---|
| `Arbeits- und Sozialgericht Wien` | `Arbeits- und Sozialgericht Wien` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
Das für das <<<Arbeits- und  Sozialgericht>>> verfasste berufskundliche Sachverständigengutachten ist das ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... MA  hätte zu dieser Zeit bis zur Erlangung der Matura - in <<<England>>> Advanced Level  genannt - noch ein Jahr im King's School absolvieren ...
```

| Predicted | Gold |
|---|---|
| `England` | `England` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... wohnt 1 Monat bei der Mutter ihres Freundes wegen Lockdown in <<<England>>>).
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... welche die Tochter zusätzlich noch übernommen hatte (Fahrkarten <<<ÖBB>>> für Besuche,  Betriebskosten der Wohnung in Bludenz, Depotgeld ...
```

| Predicted | Gold |
|---|---|
| `ÖBB` | `ÖBB` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... geltend gemachten Besuchskosten wie für die Jahreskarten der <<<ÖBB>>> sowie der  einzelnen Bahn- oder Bustickets bzw Taxirechnungen ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... die Beschwerde vom 11. Oktober 2019 gegen den Bescheid des <<<Finanzamtes  Neunkirchen Wr. Neustadt>>> (nunmehr Finanzamt Österreich) vom 11. September 2019  betreffend ...
```

| Predicted | Gold |
|---|---|
| `Finanzamtes  Neunkirchen Wr. Neustadt` | `Finanzamtes  Neunkirchen Wr. Neustadt` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
für die Jahre 2001 bis 2003 wurde vom <<<Finanzamt Neunkirchen Wr.  Neustadt>>> zu Eingangsrechnungen der geprüften Gesellschaften festgestellt, ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Penken 55, 4903 Hofmanning, Österreich, vertreten durch die <<<Mag. Ghesla Steuerberater GmbH>>>, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen ...
```

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Penken 55, 4903 Hofmanning, Österreich, vertreten durch die <<<Mag. Ghesla Steuerberater GmbH>>>, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Penken 55, 4903 Hofmanning, Österreich, vertreten durch die <<<Mag. Ghesla Steuerberater GmbH>>>, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen ...
```

| Predicted | Gold |
|---|---|
| `Mag. Ghesla Steuerberater GmbH` | `Mag. Ghesla Steuerberater GmbH` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Penken 55, 4903 Hofmanning, Österreich, vertreten durch die <<<Mag. Ghesla Steuerberater GmbH>>>, Kirchstraße  32, 6923 Lauterach, über die Beschwerden gegen ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), <<<Sudver Handel Services GMBH>>>  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, ...
```

| Predicted | Gold |
|---|---|
| `Sudver Handel Services GMBH` | `Sudver Handel Services GMBH` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... GMBH (Baufirma) sowie an die KQPC Versand GMBH (Auftraggeber), <<<Sudver Handel Services GMBH>>>  und Glanznorost Institut GMBH (jeweils Baufirma) als Gesamtschuldner, ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und <<<Glanznorost Institut GMBH>>> (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 ...
```

| Predicted | Gold |
|---|---|
| `Glanznorost Institut GMBH` | `Glanznorost Institut GMBH` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Versand GMBH (Auftraggeber), Sudver Handel Services GMBH  und <<<Glanznorost Institut GMBH>>> (jeweils Baufirma) als Gesamtschuldner, welcher erst am 11.1.2019 ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (<<<Pensionsversicherungsanstalt>>>) in Höhe von  Euro 11.616,84.
```

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (<<<Pensionsversicherungsanstalt>>>) in Höhe von  Euro 11.616,84.
```

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Erwerbsunfähigkeit auf ein von der Bf  vorgelegtes, von der <<<Pensionsversicherungsanstalt>>> in Auftrag gegebenes Gutachten vom 2. Juli  2021: Dieses stellt ...
```

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Eine sich auf das genannte Gutachten der  <<<Pensionsversicherungsanstalt>>> beziehende chefärztliche Stellungnahme vom 6. Juli 2021 hält ...
```

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Da das für die <<<Pensionsversicherungsanstalt>>> erstellte Gutachten festhält,  dass die Bf „seit ca. 2006 mit ...
```

FP: `Pensionsversicherungsanstalt` (organisation)

```
... Jugend am Werk“ tätig ist, geht die sich auf  das Gutachten der <<<Pensionsversicherungsanstalt>>> beziehende chefärztliche Stellungnahme  davon aus, dass die ...
```

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Vor dem  Hintergrund der Ausführungen des von der <<<Pensionsversicherungsanstalt>>> in Auftrag gegebenen  3 von 6 Seite 4 von 6
```

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Neben einer inländischen Rente (<<<Pensionsversicherungsanstalt>>> Wien) bezog er eine Rente der  "Deutschen Rentenversicherung ...
```

FP: `Pensionsversicherungsanstalt` (organisation)

**✅ Gold Entities:**
- `Pensionsversicherungsanstalt Wien` (organisation)
- `Deutschen Rentenversicherung Bund` (organisation)

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Nach Ansicht des <<<VfGH>>> (zB 29.6.1985, G 42/85 ua;
```

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

**Example 1** (doc_id: ``) ( sent_id: ``)

```
... Beschwerde geäußerten verfassungsrechtlichen Bedenken an den <<<VfGH>>> zu tragen.
```

| Predicted | Gold |
|---|---|
| `VfGH` | `VfGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Der Verfassungsgerichtshof (vgl. <<<VfGH>>> B 783/89 vom 06.12.1990) hat bereits ausgesprochen,  dass eine ...
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Der <<<VfGH>>> hat in seinem Erkenntnis eine  14 von 39 Seite 15 von 39
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Dem genannten <<<VfGH>>>-Erkenntnis lag folgender Sachverhalt zu Grunde: Mit  Berufungsentscheidung ...
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Der <<<VfGH>>> bejahte die Anwendbarkeit des Vorfragentatbestandes.
```

FP: `VfGH` (organisation)

**✅ Gold Entities:**

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... unter Bezug auf ein Erkenntnis des  Verfassungsgerichtshofes (<<<VfGH>>> 6.12.1990, B 783/89), wonach eine Entscheidung derselben  Behörde ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch <<<Anwälte Mandl & Mitterbauer GmbH>>>, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Werbungskosten die in Zusammenhang mit Frontex, <<<EASO>>>, ... Einsätzen stehen, dürfen daher in  solchen Fällen nicht ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... mit dem Kurzzeiteinsatz zusammenhängenden, im Lohnzettel des  <<<Bundesministerium für Inneres>>> ausgewiesenen Reisekostenersatz, welcher zuvor iSd § 47 EStG ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... öffentlicher Verkehrsmittel nach  § 3 Abs 1 Verordnung des <<<Bundesministers für Finanzen>>> über außergewöhnliche Belastungen  (hinfort: § 3 Abs 1 VO).
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Beschwerdeführerin bezog für die Tochter T., geb. 2003, wegen Schulbesuch (<<<Höhere  Lehranstalt für Tourismus, Eventmanagement, Sport und Freizeit>>> in Krems) bis Juni 2022  Familienbeihilfe.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Sachverhalt:  T. legte am 30.05.2022 die Reifeprüfung an der <<<Höheren Lehranstalt für Tourismus,  Eventmanagement, Sport und Freizeit>>> ab und machte danach keine weitere Ausbildung.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... 26, 4591 Rosenau am Hengstpaß, Österreich, vertreten durch <<<Grazer Treuhand Steuerberatung GmbH & Partner KG>>>,  Petersgasse 128a, 8010 Graz, über die Beschwerde vom 14.11.2016 ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... erhebe ich hiermit das Rechtsmittel der Beschwerde an das  <<<Verwaltungsgericht Wien>>>.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... „Küche“ wurde zunächst ausgeführt, dass zwei Rechnungen der „<<<Wiederspan Beratung GMBH>>>“  2 von 7 Seite 3 von 7
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... nicht der Bf als Empfänger aufscheine und eine  Rechnung der „<<<Mur Alver OG>>>“ Leuchten aus dem Luxussegment anführe.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Die Kosten lt Bestätigungen des <<<Krankenpflegevereins  Bludenz>>> (welche auch mittels Kontoauszüge nachgewiesen wurden) iHv ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Gemäß § 4 Abs 1 Verordnung der <<<Bundesministerin für Finanzen>>> über die Kriterien zur  Ermittlung des Pendlerpauschales und ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Vollständigkeit halber  wird angemerkt, dass damals alle Beschwerden des <<<Tritri-IT>>> -Konzernes durch denselben  Richter beim BFG entschieden wurden).
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Halauska-Straße 7, 9544 Wiesen, Österreich, vertreten durch <<<TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG>>>, Muthgasse 109, 1190 Wien, über deren Beschwerde vom  3. Dezember ...
```

| Predicted | Gold |
|---|---|
| `TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` | `TAXCOACH Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Viertelweg 16, 3720 Gaindorf, Österreich, vertreten durch Hallas & <<<Partner Wirtschaftsprüfung und  Steuerberatung GmbH & Co KG>>>, Praterstraße 38, 1020 Wien, über die Beschwerde vom  30. November ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... diesem Zusammenhang ins Treffen geführten Entscheidung des <<<UFS  Salzburg>>> vom 20.8.2013, RV/0389-S/13 (dort hatte der Berufungswerber ...
```

| Predicted | Gold |
|---|---|
| `UFS  Salzburg` | `UFS  Salzburg` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Familienbeihilfenanspruch bei  Ausbildung eines Kindes in einem "Drittland", <<<UFS Journal>>> 2011, 371;
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... des Fahrtenbuches sei auf die Rechtsprechung  des deutschen <<<BFH>>> zu verweisen, die auch für die österreichische Rechtslage relevant ...
```

| Predicted | Gold |
|---|---|
| `BFH` | `BFH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
<<<BFH>>>, BStBl 1997 II 642;
```

FP: `BFH` (organisation)

**✅ Gold Entities:**

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
<<<BFH>>>, BStBl 1997 II 642;
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Einrichtung, die im Rahmen  der europäischen Integration oder der <<<OECD>>> tätig ist, oder  2.
```

| Predicted | Gold |
|---|---|
| `OECD` | `OECD` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Internationales Steuer- recht2, 2018, Die Verteilungsnormen im <<<OECD>>>-MA (Art. 6 bis 22 <<<OECD>>>-MA), Teil 2, Rz 707 f].
```

FP: `OECD` (organisation)

```
... recht2, 2018, Die Verteilungsnormen im <<<OECD>>>-MA (Art. 6 bis 22 <<<OECD>>>-MA), Teil 2, Rz 707 f].
```

FP: `OECD` (organisation)

**✅ Gold Entities:**
- `SUVA` (organisation)
- `Österreich` (country)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Internationales Steuer- recht2, 2018, Die Verteilungsnormen im <<<OECD>>>-MA (Art. 6 bis 22 <<<OECD>>>-MA), Teil 2, Rz 707 f].
```

FP: `OECD` (organisation)

```
... recht2, 2018, Die Verteilungsnormen im <<<OECD>>>-MA (Art. 6 bis 22 <<<OECD>>>-MA), Teil 2, Rz 707 f].
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... Pendlerpauschale  in Höhe von 1.476,00 € gekürzten Einkünfte bei der Fa. <<<Berwaldkel-Möbel AG>>>  in Ansatz gebracht.
```

| Predicted | Gold |
|---|---|
| `Berwaldkel-Möbel AG` | `Berwaldkel-Möbel AG` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
II. Das Bundesfinanzgericht hat erwogen:  1. <<<Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG>>>, Niederau 25, 6731 Bühl, Österreich  tätig.
```

FP: `Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG` (organisation)

**✅ Gold Entities:**
- `Bundesfinanzgericht` (organisation)
- `Nexkelkel AG` (organisation)
- `Niederau 25, 6731 Bühl, Österreich` (address)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
II. Das Bundesfinanzgericht hat erwogen:  1. <<<Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG>>>, Niederau 25, 6731 Bühl, Österreich  tätig.
```

FP: `Sachverhalt   Der Bf war in den streitgegenständlichen Jahren beim Nexkelkel AG` (organisation)

**✅ Gold Entities:**
- `Nexkelkel AG` (organisation)
- `Niederau 25, 6731 Bühl, Österreich` (address)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
bis 31.12.2023 <<<Einkünfte aus nichtselbständiger Arbeit von der  X GmbH in Adr AG>>>.
```

FP: `Einkünfte aus nichtselbständiger Arbeit von der  X GmbH in Adr AG` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
<<<Die Entfernung zwischen der Adresse des Arbeitgebers X GmbH in Adr AG>>> und der  österreichischen Wohnadresse Bf-Adr Ö beträgt weniger ...
```

FP: `Die Entfernung zwischen der Adresse des Arbeitgebers X GmbH in Adr AG` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
<<<Die Feststellungen hinsichtlich der Entfernung zwischen der Adresse des Arbeitgebers X GmbH  in Adr AG>>> und der österreichischen Wohnadresse Bf-Adr Ö und der Zeitdauer ...
```

FP: `Die Feststellungen hinsichtlich der Entfernung zwischen der Adresse des Arbeitgebers X GmbH  in Adr AG` (organisation)

**✅ Gold Entities:**
- `X GmbH` (organisation)
- `Bundesministerium für Finanzen` (organisation)

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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
Dass die Bescheide (lediglich) per E-Mail an die <<<Merkur Treuhand  Steuerberatung>>> weitergeleitet wurden, hat diese über Aufforderung des Bundesfinanzgerichtes ...
```

| Predicted | Gold |
|---|---|
| `Merkur Treuhand  Steuerberatung` | `Merkur Treuhand  Steuerberatung` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Haan,  Oisching 129, 3071 Wiesen, Österreich, vertreten durch <<<Merkur Treuhand Steuerberatung>>> GmbH, St.-Veit-Gasse 50,  1130 Wien, über die Beschwerde vom ...
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Hon.-Prof. Univ.-Prof. Hartwig Boehler` (person)
- `DDr.in Josepha de Haan` (person)
- `Oisching 129, 3071 Wiesen, Österreich` (address)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)
- `St.-Veit-Gasse 50,  1130 Wien` (address)
- `Finanzamtes  Österreich` (organisation)
- `01-186/7053` (tax_number)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... bei der belangten Behörde am selben Tage,  übermittelte die <<<Merkur Treuhand Steuerberatung>>> GmbH der belangten Behörde eine am  11.3.2024 von der Beschwerdeführerin ...
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

```
... unterfertigte Vollmacht, womit die  Beschwerdeführerin die <<<Merkur Treuhand Steuerberatung>>> GmbH als „Vertreter in allen  steuerlichen, wirtschaftlichen ...
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur Treuhand Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Weiters wurde  der <<<Merkur Treuhand Steuerberatung>>> GmbH darin die Vollmacht „zum Empfang von  Schriftstücken, ...
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Im (Begleit-) Schreiben vom 13.3.2024 führt die <<<Merkur Treuhand Steuerberatung>>>  GmbH aus, dass die Vollmacht als „Spezialvollmacht für das ...
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Merkur Treuhand Steuerberatung  GmbH` (organisation)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... (Sicherstellungsauftrag) und 3.4.2024 (Pfändung) mit E-Mail vom 16.4.2024 an die  <<<Merkur Treuhand Steuerberatung>>> GmbH weiter.
```

FP: `Merkur Treuhand Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger Steuerberatung GmbH` (organisation)
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

**Example 0** (doc_id: ``) ( sent_id: ``)

```
... NOVA- Meldungen mit dem Hinweis, dass man auf eine Aussage des <<<Amtes für Betrugsbekämpfung>>>  (ABB) warte.
```

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... 7. August 2024 gegen das Erkenntnis des Spruchsenates beim <<<Amt für Betrugsbekämpfung>>> als  Finanzstrafbehörde vom 28. Mai 2024, Geschäftszahl SpS-1, ...
```

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)
- `1960` (date)
- `Dr. A. Schärf-Straße 22, 8783 Gaishorn am See, Österreich` (address)
- `Reinemut + Smoch Handel` (organisation)
- `Zachariasweg 4K, 3250 Wieselburg, Österreich` (address)
- `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` (organisation)
- `Triesterstraße  14, 2351 Wiener Neudorf` (address)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Erkenntnis des Spruchsenates wie folgt abgeändert:  Das beim <<<Amt für Betrugsbekämpfung>>> als Finanzstrafbehörde wegen des Verdachts einer  Verkürzung ...
```

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... belangten Verbandes wird teilweise stattgegeben und das beim <<<Amt für  Betrugsbekämpfung>>> als Finanzstrafbehörde wegen des Verdachts einer Verkürzung ...
```

FP: `Amt für  Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Reinemut + Smoch Handel` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Verfahrensgang ab Spruchsenat:  Mit Erkenntnis des Spruchsenates beim <<<Amt für Betrugsbekämpfung>>> als Finanzstrafbehörde als  Organ des Amtes für Betrugsbekämpfung ...
```

FP: `Amt für Betrugsbekämpfung` (organisation)

```
... für Betrugsbekämpfung als Finanzstrafbehörde als  Organ des <<<Amtes für Betrugsbekämpfung>>> als Finanzstrafbehörde vom 28. Mai 2024,  Geschäftszahl SpS-1, ...
```

FP: `Amtes für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `Amtes für Betrugsbekämpfung als Finanzstrafbehörde` (organisation)
- `OSR Jan Passerschroer, MA` (person)
- `Finanzamts Österreich` (organisation)
- `Reinemut + Smoch Handel` (organisation)
- `72-531/2688` (tax_number)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Mandantschaft, insbesondere des Schreibens vom 17.05.2024  an das <<<Amt für Betrugsbekämpfung>>>, geht hervor, dass Herr OSR Jan Passerschroer, MA  zu den Tatzeitpunkten ...
```

FP: `Amt für Betrugsbekämpfung` (organisation)

**✅ Gold Entities:**
- `OSR Jan Passerschroer, MA` (person)

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

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... einschließlich Sommersemester 2022 absolvierte sie an  der <<<Fachhochschule Wiener>>> Neustadt das Bachelorstudium Biotechnische Verfahren.
```

FP: `Fachhochschule Wiener` (organisation)

**✅ Gold Entities:**
- `Fachhochschule Wiener Neustadt` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... am  16.02.2023 bekannt, dass T. nunmehr seit 15.02.2023 am <<<FH Campus>>> Wien Gesundheits- und  Krankenpflege studiere.
```

FP: `FH Campus` (organisation)

**✅ Gold Entities:**
- `FH Campus Wien` (organisation)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... einschließlich Sommersemester 2022 absolvierte sie an der  <<<Fachhochschule Wiener>>> Neustadt das Bachelorstudium Biotechnische Verfahren.
```

FP: `Fachhochschule Wiener` (organisation)

**✅ Gold Entities:**
- `Fachhochschule Wiener Neustadt` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... einschließlich Sommersemester 2022 absolvierte sie an  der <<<FH Wiener>>> Neustadt für Wirtschaft und Technik GmbH (Tulln) das Bachelorstudium ...
```

FP: `FH Wiener` (organisation)

**✅ Gold Entities:**
- `FH Wiener Neustadt` (organisation)
- `Wirtschaft und Technik GmbH` (organisation)
- `Tulln` (city)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Seit Februar 2023 studiert T. an der <<<FH Campus>>> Wien Gesundheits- und Krankenpflege  (FC000599).
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... 23.03.2023, vor, dass ihre  Tochter T. am 30.05.2022 an der <<<HLF Krems/Donau maturiert habe und damit in die alte  >>>2 von 6 Seite 3 von 6
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Abgabenschuldner“) wurden der Beschwerdeführerin am 5.4.2024 zu  Handen der <<<Schabetsberger Steuerberatung>>> GmbH, Fischerstiege 9, 1010 Wien, zugestellt.
```

FP: `Schabetsberger Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Finanzamt Österreich` (organisation)
- `Schabetsberger Steuerberatung GmbH` (organisation)
- `Fischerstiege 9, 1010 Wien` (address)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Die <<<Schabetsberger Steuerberatung>>> GmbH leitete Scans der ihr zugestellten Bescheide vom  20.3.2024 ...
```

FP: `Schabetsberger Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 2** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Mitarbeiter oder eine  Mitarbeiterin (Unterschrift unleserlich) der <<<Schabetsberger Steuerberatung>>> GmbH die  Übernahme dieser beiden Bescheide am 5.4.2024 bestätigt, ...
```

FP: `Schabetsberger Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger Steuerberatung GmbH` (organisation)
- `Merkur Treuhand Steuerberatung GmbH` (organisation)

**Example 3** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Vollmachten (daher auch eine allfällige Zustellvollmacht der  <<<Schabetsberger Steuerberatung>>> GmbH) aufgelöst.
```

FP: `Schabetsberger Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger Steuerberatung GmbH` (organisation)

**Example 4** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Die Zustellung an die <<<Schabetsberger  Steuerberatung>>> GmbH war unwirksam.
```

FP: `Schabetsberger  Steuerberatung` (organisation)

**✅ Gold Entities:**
- `Schabetsberger  Steuerberatung GmbH` (organisation)

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

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... einer Beschwerdevorentscheidung) dem  damaligen UFS (nunmehr <<<BFG, Außenstelle Linz>>>) zur Entscheidung vorgelegt.
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
Das Erkenntnis des <<<Bundesfinanzgerichts, Außenstelle Linz>>>, vom 27.01.2016, GZ  RV/5101064/2013, wurde seitens des FA ...
```

FP: `Bundesfinanzgerichts, Außenstelle Linz` (organisation)

**✅ Gold Entities:**
- `FA Wien 1/23` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Rechtsvorgängers Houdek Maschinenbau  wurde das Erkenntnis des  <<<Bundesfinanzgerichts, Außenstelle Linz>>>, am 27.01.2016 zu GZ RV/5101064/2013 zum  Veranlagungsjahr ...
```

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

**Example 0** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der <<<Sozialversicherung der Bauern>>>, etc) geht ins Leere.
```

FP: `Sozialversicherung der Bauern` (organisation)

**✅ Gold Entities:**
- `WKO` (organisation)

**Example 1** (doc_id: ``) ( sent_id: ``)

**False Positives:**

```
... Lösen der Gewerbeberechtigung bei  der WKO, das Zahlen der <<<Sozialversicherung der Bauern>>>, etc) geht ins Leere.
```

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

