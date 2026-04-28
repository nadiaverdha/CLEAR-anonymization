# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B

Generated on: 2026-04-27T22:41:52.148363

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-04-27_v16/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 400 |
| Validation documents | 101 |
| Test documents | 12 |
| Train sentences | 2755 |
| Validation sentences | 213 |
| Test sentences | 1247 |
| Model | Qwen/Qwen3.5-35B-A3B |
| Max rules | 20 |
| Max samples in prompt | 60 |
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
| Batch size | 20 |
| Refine per batch | 1 |
| Manually annotated examples | 96 |
| First batch with manual data | 132 |

</details>

---

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 86.4% |
| True Positives | 184 |
| False Positives | 138 |
| False Negatives | 72 |
| Total Gold Entities | 256 |
| Micro Precision | 57.1% |
| Micro Recall | 71.9% |
| Micro F1 | 63.7% |
| Macro F1 | 63.7% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Magistrat der Stadt Wien` | 4.6% | 100.0% | 2.3% | 6 | 6 | 0 |
| `Landespolizeidirektion Wien` | 3.1% | 100.0% | 1.6% | 4 | 4 | 0 |
| `Bezirksgericht Entities` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `ÖGK Acronym` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `Pensionsversicherungsanstalt Entities` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `Verwaltungsgerichtshof Entities` | 38.6% | 95.4% | 24.2% | 65 | 62 | 3 |
| `Tax Office Entities` | 10.3% | 93.3% | 5.5% | 15 | 14 | 1 |
| `Bundesfinanzgericht Entities` | 48.6% | 90.4% | 33.2% | 94 | 85 | 9 |
| `Finanzamt Österreich` | 6.0% | 88.9% | 3.1% | 9 | 8 | 1 |
| `Finanzamt Österreich Extended` | 6.0% | 88.9% | 3.1% | 9 | 8 | 1 |
| `University Entities` | 3.1% | 66.7% | 1.6% | 6 | 4 | 2 |
| `Amt für Betrugsbekämpfung` | 1.5% | 66.7% | 0.8% | 3 | 2 | 1 |
| `VwGH Acronym` | 2.2% | 3.4% | 1.6% | 116 | 4 | 112 |
| `AG Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verlag Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Maschinenbau Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Luftfahrt Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenbank General` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Technik Valseekel GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fachhochschule Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FH Campus Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministeriums für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wirtschaft und Technik GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Paugger Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `COFAG Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BHAG Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FAÖ Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FAG Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Deloitte Tax Wirtschaftsprüfungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesheer Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `IT Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landesgericht Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `LG Acronym Court` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BG Acronym Court` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministeriums für Justiz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BKS Steuerberatung GmbH & Co KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Eckhardt SteuerberatungsgmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag. Ghesla Steuerberater GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Eidgenössischen Invalidenversicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schweizerischen Unfallversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Bregenz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GmbH Companies` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `SUVA Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steueramt Luzern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kantonsspital St. Gallen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SüdVersand` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TraunLuftfahrt Solutions` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frontex and Border Agency Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ministry of Interior Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Criminal Police Austria` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `EASO and OECD Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Flughafen München` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `INET Internet Service GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `INET System Informations GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Neunkirchen Wiener Neustadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Neunkirchen Wr. Neustadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UFS Acronym` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `UFS/BFG Compound` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `How to spend it Verlag GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzpolizei Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Rechtsanwälte OG Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFH Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `London Film Academy` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundeskanzleramtes` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `VfGH Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GmbH Extended Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Reinemut + Smoch Handel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Zollamt Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `HLF Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verfassungsgerichtshof Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FH Kärnten Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fachhochschule Kärnten Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Karl-Franzens-Universität Graz Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `TAXCOACH Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Merkur Treuhand Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schabetsberger Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UFS Salzburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Merkur Steuerberatung GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GmbH Partner KG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Rhein Normonkel Manufaktur GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BDO Austria GmbH Full Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `F Personalservice GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenbank Wels Süd Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landespolizeidirektion Tirol Typo` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Henken Organization` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesamt für Soziales und Behindertenwesen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Arbeits- und Sozialgericht` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Retail Chains Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiederspan Beratung GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mur Alver OG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PVA Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SVS SVB Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PSD Wien Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sozialversicherung Bauern Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Psychiatrie Otto Wagner Spital Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Magistrat der Stadt Klagenfurt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministeriums für Inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Immobilienbüro Mandl` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Österreichischen Gesundheitskasse` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Klein-Vorholt KI GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gogel Daten GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `InnMarine GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fensudlog GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Luehrig + Hundertmarck Holz GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministerin für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KQPC Versand GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Event Sudkraftlex GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sudver Handel Services GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Glanznorost Institut GMBH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Erste Bank Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WKO Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirkshauptmannschaft Bludenz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SENECURA` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SeneCura Family Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ÖBB Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Krankenpflegevereins Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Magistrat der Stadt Wien`

**F1:** 0.046 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien' and 'Magistrates der Stadt Wien' including department extensions like 'MA 67' or 'Magistratsabteilung 67'. Updated to handle the full span including the department.

**Content:**
```
\bMagistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s*,\s+(?:MA\s+\d+|Magistratsabteilung\s+\d+))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.046 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 122 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gabriele Friedbacher` (person)
- `Wilhelm Konetzny` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

## `Verwaltungsgerichtshof Entities`

**F1:** 0.386 | **Precision:** 0.954 | **Recall:** 0.242  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.954 | 0.242 | 0.386 | 65 | 62 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 62 | 3 | 192 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_46`)


Dem ist zu entgegnen, dass nach der zitierten Judikatur des Verwaltungsgerichtshofes das  Aufrechterhalten des Berufswunsches nicht maßgeblich ist, wenn die Ausbildung nach ihrem  Abbruch nicht wieder aufgenommen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_135`)


Unter  Zugrundelegung dieser Ausführungen hat der Verwaltungsgerichtshof in der Folge festgestellt,  dass nicht allein der Wechsel der Einrichtung ausschlaggebend ist.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Tax Office Entities`

**F1:** 0.103 | **Precision:** 0.933 | **Recall:** 0.055  

**Format:** `regex`  
**Description:**
Matches Finanzamt and FA variations including common Austrian regions. Explicitly excludes court names to prevent overlap. Added specific pattern for Wien 9/18/19 Klosterneuburg and Wien 6/7/15.

**Content:**
```
\b(?:Finanzamt(?:es)?|FA)\s+(?:Oststeiermark|Waldviertel|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Klosterneuburg|Nieder\u00f6sterreich\s+Mitte|Grieskirchen\s+Wels|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Steiermark\s+Mitte|Freistadt\s+Rohrbach\s+Urfahr|Gmunden\s+V\u00f6cklabruck|Spittal\s+Villach|Landeck\s+Reutte|Wien\s+8/16/17|Wien\s+2/20/21/22|Wien\s+1/23|Wien\s+6/7/15|Kirchdorf\s+Perg\s+Steyr|Innsbruck|Linz|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Braunau\s+Ried\s+Sch\u00e4rding|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Judenburg\s+Liezen|Salzburg-Stadt|Salzburg-Land|Ost|Purkersdorf|Baden\s+M\u00f6dling|Schwechat\s+Gerasdorf|Tirol\s+Ost|Graz-Stadt|Amstetten\s+Melk\s+Scheibbs|Hollabrunn\s+Korneuburg\s+Tulln|\u00d6sterreich|Wien\s+9/18/19\s+Klosterneuburg)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.933 | 0.055 | 0.103 | 15 | 14 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 1 | 242 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `6207 150171` (social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

## `Bundesfinanzgericht Entities`

**F1:** 0.486 | **Precision:** 0.904 | **Recall:** 0.332  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht', its genitive forms 'Bundesfinanzgerichtes' and 'Bundesfinanzgerichts', and the acronym 'BFG'.

**Content:**
```
\b(?:Bundesfinanzgericht(?:es|s)?|BFG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.904 | 0.332 | 0.486 | 94 | 85 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 85 | 9 | 171 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_19`)


6. Mit Schriftsatz vom 04.08.2020 stellte die BF über ihren steuerlichen Vertreter den Antrag  auf Vorlage der Bescheidbeschwerde an das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_27`)


7. Am 12.10.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor und beantragte die Abweisung, da die Ausbildung am 04.10.2017 beendet  worden sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_28`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die BF bezog im streitgegenständlichen Zeitraum Familienbeihilfe und Kinderabsetzbeträge für  ihre Tochter Stella Marschalk, Bakk. techn. (geboren im September 1998).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Stella Marschalk, Bakk. techn.` (person)
- `September 1998` (date)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_38`)


Insbesondere ist den Curricula der beiden Studien entnehmbar, dass beide Studien „dasselbe  Ausbildungsergebnis" (im Sinne der BFG-Entscheidung RV/0180-L/10) zum Ziel haben (s.  angehängte Curricula und BFG-Entscheidung).

**False Positives:**

- `BFG` — no gold match — likely missing annotation
- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_128`)


Es ist zur Klärung der Rechtsmäßigkeit der Rückforderung zunächst zu prüfen, ob ein  „Studienwechsel“ im Sinne des § 2 Abs. 1 lit. b FLAG 1967 überhaupt vorliegt, bevor auf einen  solchen Studienwechsel die Bestimmungen des § 17 StudFG angewendet werden können (BFG  26.02.2022, RV/2100101/2022 mit Verweis auf VwGH 09.07.2008, 2005/13/0142, Rechtssatz  JWR_2005130142_20080709X02).

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_160`)


BFG 05.07.2016, RV/5100209/2012;

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Österreich`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_41`)


Der Bf. erhob gegen das Straferkenntnis mit Anbringen vom 5. September 2025 (fristgerecht)  Beschwerde, führte aus wie im oben angeführten Einspruch gegen die Strafverfügung vom  30. Juni 2025 mit dem Ersuchen, die im Straferkenntnis festgelegte Geldstrafe in Höhe von  65,00 Euro [Anmerkung BFG, gemeint: Geldstrafe in Höhe von 55,00 Euro] herabzusetzen.

**False Positives:**

- `BFG` — partial — pred is substring of gold: `BFG,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG,`(organisation)

</details>

---

## `Finanzamt Österreich`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' and 'Finanzamtes Österreich'.

**Content:**
```
\bFinanzamt(?:es)?\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.889 | 0.031 | 0.060 | 9 | 8 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 1 | 230 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `85-919/9176` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `6207 150171` (social_security_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `75-059/0556` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

## `Finanzamt Österreich Extended`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' and 'Finanzamtes Österreich' including the optional '(DST12)' suffix.

**Content:**
```
\bFinanzamt(?:es)?\s+Österreich(?:\s*\(DST12\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.889 | 0.031 | 0.060 | 9 | 8 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 1 | 230 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `85-919/9176` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `6207 150171` (social_security_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `75-059/0556` (tax_number)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `VwGH Acronym`

**F1:** 0.022 | **Precision:** 0.034 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches the acronym 'VwGH' as a standalone entity, ensuring it is captured even in citation contexts.

**Content:**
```
\bVwGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.034 | 0.016 | 0.022 | 116 | 4 | 112 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 112 | 240 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_148`)


Wie der VwGH bereits in mehreren Erkenntnissen ausfgeührt hat erfordert die berufliche  Tätigkeit eines hauptberuflichen Musikers ein musikalisches Niveau, welches nur durch  regelmäßige Arbeit am Instrument zu erreichen und zu halten ist.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_94`)


Nach der Rechtsprechung des VwGH setzt eine Zwangsläufigkeit aus sittlichen Gründen voraus,  dass sich der Steuerpflichtige nach dem Urteil billig und gerecht denkender Menschen zu der  Leistung verpflichtet halten kann.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_226`)


Auf  die einheitliche zitierte Judikatur des VwGH wird verwiesen.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_41`)


Dazu zählen beispielsweise Erkrankungen, die die Berufsausbildung auf begrenzte Zeit  unterbrechen, oder Urlaube und Schulferien (VwGH vom 16.11.1993, 90/14/0108).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_44`)


Das bloße Aufrechterhalten eines  Berufswunsches ist der tatsächlichen Ausbildung nicht gleichzuhalten (VwGH 24.9.2009,  2009/16/0088, VwGH 21.01.2004, 2003/13/0157, VwGH 14.12.1995, 93/15/0133).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_50`)


Entscheidend ist somit lediglich, ob der Empfänger die  Beträge zu Unrecht erhalten hat (vgl. VwGH 28.10.2009, 2008/15/0329).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_56`)


Ob eine Berufsausbildung im Sinne des FLAG 1967 vorliegt, ist eine Tatfrage (vgl. VwGH  16.11.1993, 90/14/0108), welche in freier Beweiswürdigung zu beantworten ist und einer  ordentlichen Revision nicht zugänglich ist.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `UFS Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'UFS' (Unabhängiger Finanzsenat) as a standalone entity.

**Content:**
```
\bUFS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 8 | 185 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `WU`(organisation)
- `JKU`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_130`)


Allerdings ist durch die mit Einführung des UG 2002 erreichte Autonomie der Universitäten –  und damit verbunden die jeder Einrichtung mögliche individuelle Gestaltung der Studien – bei  einem Wechsel der Studieneinrichtung auch bei gleichbleibender Studienrichtung nicht in  jedem Fall eine Gleichwertigkeit gegeben (UFS 02.11.2011, RV/0289-F/11  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 96).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_134`)


UFS 19.10.2010, RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_143`)


Die Gewährung der Familienbeihilfe  für volljährige Kinder stellt nach den näheren Regelungen des § 2 Abs. 1 lit. b FLAG ersichtlich  darauf ab, dass sich das Kind einer Berufsausbildung mit dem ernstlichen und zielstrebigen,  nach außen erkennbaren Bemühen um den Ausbildungserfolg unterzieht (UFS 19.10.2010,  RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

</details>

---

## `University Entities`

**F1:** 0.031 | **Precision:** 0.667 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches Universität Wien, Wirtschaftsuniversität Wien, and Universität Innsbruck.

**Content:**
```
\b(?:Universität\s+Wien|Wirtschaftsuniversität\s+Wien|Universität\s+Innsbruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.016 | 0.031 | 6 | 4 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 2 | 207 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes Kepler Universität Linz` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_124`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes Kepler Universität Linz` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_147`)


Nach unstrittigem Sachverhalt hat die Tochter der Bf. mit dem Wechsel vom Bachelorstudium  Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien nach dem  Sommersemester 2019, somit nach dem vierten Semester des seit Oktober 2017 dort  betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der Johannes  Kepler Universität Linz mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel  vorgenommen.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes  Kepler Universität Linz` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU Wien)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU Wien)`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU)`(organisation)
- `Johannes Kepler Universität Linz (JKU)`(organisation)

</details>

---

</details>

---

<details>
<summary>🔇 Inactive Rules</summary>

## `AG Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'AG', excluding single-letter prefixes like 'F' and common articles.

**Content:**
```
(?<!Firma\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!Dem\s)(?<!Den\s)(?<!Des\s)(?<!Arbeitgeber\s)(?<!F\s)\b[A-Z][a-z0-9&+\-]*(?:\s+[A-Z][a-z0-9&+\-]*)*\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verlag Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Verlag' preceded by a capitalized word, generalizing 'Dorfcon-Verlag'.

**Content:**
```
\b[A-Z][a-zA-Z0-9&\-]*\s+Verlag\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Maschinenbau Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Maschinenbau' preceded by a capitalized word, generalizing 'Houdek Maschinenbau'.

**Content:**
```
\b[A-Z][a-zA-Z0-9]*\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Luftfahrt Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Luftfahrt' preceded by a capitalized word, generalizing 'Schmeltz Luftfahrt'.

**Content:**
```
\b[A-Z][a-zA-Z0-9]*\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenbank General`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Raiffeisenbank followed by a location name and optional additional words (e.g., Bankstelle, Filiale) to catch full names like 'Raiffeisenbank Karnische Rion Bankstelle St.Stefan'. Updated to be more inclusive of suffixes.

**Content:**
```
\bRaiffeisenbank\s+(?:[A-Z][a-z0-9\-]+\s+)*[A-Z][a-z0-9\-]+(?:\s+(?:Bankstelle|Filiale|Niederlassung|Zweigstelle)\s+[A-Z][a-z0-9\-]+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Technik Valseekel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Technik Valseekel GMBH' to prevent partial matching by generic GMBH rules.

**Content:**
```
\bTechnik\s+Valseekel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fachhochschule Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Fachhochschule Wiener Neustadt and FH Wiener Neustadt variations.

**Content:**
```
\b(?:Fachhochschule\s+Wiener\s+Neustadt|FH\s+Wiener\s+Neustadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FH Campus Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches FH Campus Wien specifically.

**Content:**
```
\bFH\s+Campus\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministeriums für Finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific government ministry name.

**Content:**
```
\bBundesministeriums\s+für\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wirtschaft und Technik GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Wirtschaft und Technik GmbH' to prevent partial matching by generic GmbH rules.

**Content:**
```
\bWirtschaft\s+und\s+Technik\s+GmbH\b
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

## `Bundesfinanzgericht Entities`

**F1:** 0.486 | **Precision:** 0.904 | **Recall:** 0.332  

**Format:** `regex`  
**Description:**
Matches 'Bundesfinanzgericht', its genitive forms 'Bundesfinanzgerichtes' and 'Bundesfinanzgerichts', and the acronym 'BFG'.

**Content:**
```
\b(?:Bundesfinanzgericht(?:es|s)?|BFG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.904 | 0.332 | 0.486 | 94 | 85 | 9 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 85 | 9 | 171 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `FA Graz-Stadt` (organisation)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_19`)


6. Mit Schriftsatz vom 04.08.2020 stellte die BF über ihren steuerlichen Vertreter den Antrag  auf Vorlage der Bescheidbeschwerde an das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_27`)


7. Am 12.10.2020 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht zur  Entscheidung vor und beantragte die Abweisung, da die Ausbildung am 04.10.2017 beendet  worden sei.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_28`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die BF bezog im streitgegenständlichen Zeitraum Familienbeihilfe und Kinderabsetzbeträge für  ihre Tochter Stella Marschalk, Bakk. techn. (geboren im September 1998).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Stella Marschalk, Bakk. techn.` (person)
- `September 1998` (date)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `85-919/9176` (tax_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_41`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Am 12. Oktober 2020 bestätigte The King´s School Worcester:  I am writing to confirm that Maximiliane Sakschewsky, MA [Nachname wie Bf.) was a pupil of The King's  School Worcester from September 2014 until July 2020.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `The King´s School Worcester` (organisation)
- `Maximiliane Sakschewsky, MA` (person)
- `The King's  School Worcester` (organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_89`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  6 von 7 Seite 7 von 7

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `Finanzamtes Österreich` (organisation)
- `6207 150171` (social_security_number)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_36`)


8. Die Bf. beantragte mit Vorlageantrag vom 11.04.2022 die Entscheidung über die  Beschwerde durch das Bundesfinanzgericht und brachte dazu ergänzend vor:  „Ausführungen zu der von mir im Beschwerdeverfahren vorgelegten E-Mail des  Zulassungsservices Lehr und Studienorganisation der Johannes Kepler Universität Linz vom  4 von 16 Seite 5 von 16

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Johannes Kepler Universität Linz` (organisation)

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_50`)


Mit Vorlagebericht vom 26.07.2022 legte die belangte Behörde die Beschwerde dem  Bundesfinanzgericht zur Entscheidung vor und führte dazu aus:  „Sachverhalt:  Aufgrund eines Arbeitsauftrages vom 21.05.2021 sollte der Familienbeihilfe-Anspruch der  Beschwerdeführerin bezüglich ihrer Tochter Viktoria Immohr  vor bzw. im § 15 FLAG Zeitraum  überprüft werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Viktoria Immohr` (person)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_63`)


Am 12.04.2022 reichte die  Beschwerdeführerin den Vorlageantrag ein, damit die Beschwerde dem Bundesfinanzgericht  zur Entscheidung vorgelegt wird und der Bescheid ersatzlos aufgehoben wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Viktoria Immohr` (person)
- `Wirtschaftsuniversität Wien` (organisation)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_86`)


Insbesondere nahm das Bundesfinanzgericht Einsicht in die vorgelegten  Studienpläne.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_108`)


Das Bundesfinanzgericht schließt sich  dieser Sichtweise an.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_171`)


3.3. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  15 von 16 Seite 16 von 16

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_173`)


Mit dem vorliegenden Erkenntnis folgt das Bundesfinanzgericht der zitierten einheitlichen  Rechtsprechung des Verwaltungsgerichtshofes (insbesondere VwGH 09.07.2008,  2005/13/0142).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Finanzamt Österreich` (organisation)
- `69-575/0475` (tax_number)

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_15`)


Das Finanzamt hat am 22. Oktober 2025 den säumigen Bescheid erlassen und dem  Bundesfinanzgericht eine Abschrift übermittelt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_17`)


Da der versäumte Bescheid nunmehr erlassen wurde, ging die Zuständigkeit nicht auf das  Bundesfinanzgericht über.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_19`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz. Quirin Januszis` (person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.` (person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich` (address)
- `Amtes für Betrugsbekämpfung` (organisation)

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Gabriele Friedbacher` (person)
- `Wilhelm Konetzny` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)
- `Magistrat der Stadt Wien, MA 67` (organisation)
- `Magistrates der Stadt Wien` (organisation)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_42`)


Die Magistratsabteilung 67 legte die Beschwerde samt dem bezughabenden Verwaltungsakt  dem Bundesfinanzgericht zur Entscheidung vor (Datum des Einlangens: 1. Oktober 2025).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Magistratsabteilung 67` (organisation)

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_62`)


Auch das Bundesfinanzgericht folgt dieser Vorgehensweise und gibt im gegebenen  Kontext jedoch auch zu bedenken, dass dadurch, dass weder der mit Organstrafverfügung  noch der mit Anonymverfügung verhängte Strafbetrag einbezahlt wurde, ein nicht  unerheblicher zusätzlicher Verwaltungsaufwand verursacht wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_63`)


Im Übrigen wird auf die  vom Bundesfinanzgericht als rechtsrichtig beurteilte Begründung der belangten Behörde im  angefochtenen Straferkenntnis (siehe obige Darstellung) verwiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_67`)


Auch das Bundesfinanzgericht folgt grundsätzlich dieser Strafpraxis.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_80`)


Gemäß § 25 Abs. 2 BFGG hat das Bundesfinanzgericht, soweit dies nicht in der BAO, im ZollR- DG oder im FinStrG geregelt ist, in seiner Entscheidung zu bestimmen, welche  Abgabenbehörde oder Finanzstrafbehörde die Entscheidung zu vollstrecken hat.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Juliana Bartjen  in der Beschwerdesache Renate Brombusch,  Langaberg 10, 5071 Himmelreich, Österreich, vertreten durch smc Steirer Mika & Comp.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Priv.-Doz.in Juliana Bartjen` (person)
- `Renate Brombusch` (person)
- `Langaberg 10, 5071 Himmelreich, Österreich` (address)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_49`)


Für den Fall der Abweisung unserer Beschwerde berufen wir uns auf die von unserer  Mandantschaft erteilte Vollmacht und stellen vorsorglich den Antrag auf Vorlage unserer  Beschwerde an das Bundesfinanzgericht und Entscheidung durch den Senat unter  Anberaumung einer mündlichen Verhandlung unter Hinzuziehung des Parteienvertreters.“

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_65`)


Am 22.02.2017 brachte der steuerliche Vertreter des Bf. einen Antrag auf Vorlage der  Beschwerde an das Bundesfinanzgericht ein.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_83`)


Mit Schreiben vom 21.8.2025, eingelangt am BFG am 22.8.2025, zog der steuerliche Vertreter  den Antrag auf mündliche Senatsverhandlung zurück.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_84`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_93`)


Diese Sachverhaltsfeststellungen ergeben sich nach Dafürhalten des Bundesfinanzgerichts aus  den vorgelegten Akten des Abgabenverfahrens, dem Vorbringen der Bf. in seiner Beschwerde  sowie den Erhebungen durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_137`)


Entgegen der vom Finanzamt getroffenen Beurteilung vertritt das BFG die Auffassung, dass im  streitgegenständlichen Fall eine Betätigung im Sinne des § 1 Abs. 1 LVO vorliegt, weil das  künstlerische Tätigwerden des Bf. sich nicht im Rahmen einer typischen Betätigung im Sinne  des § 1 Abs. 2 Z 2 LVO bewegt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_138`)


Für eine typische erwerbswirtschaftliche Betätigung spricht nach Ansicht des BFG die  hauptberufliche Ausübung der musikalischen Tätigkeit auf Grundlage der gehobenen  musikalischen Ausbildung des Bf.  11 von 14 Seite 12 von 14

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_139`)


In Anbetracht von Art und Umfang der vom Bf. ausgeübten Tätigkeit ist nach Ansicht des BFG  insbesondere aus folgenden Gründen nicht von einer hobbymäßigen Betätigung auszugehen:   der Bf. ist akademisch ausgebildeter Musiker, d.h. er verfügt demnach über eine  entsprechende profunde und einschlägige Hochschulausbildung   er hat auf mehreren Musik-CD’s mitgewirkt   er hat mit namhaften Musikern zusammengearbeitet und trat mit Jazzgrößen auf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_144`)


In Anbetracht der Tatsache, dass der Bf. die in Rede stehende Tätigkeit 2014, aufgrund des  Rückganges der Aufträge und der Tatsache, dass es für ihn immer schwieriger wurde Aufträge  für Auftritte zu erhalten, durch seine betriebswirtschaftlich sinnvolle Entscheidung, beendet  hat und in dem gesamten Betätigungszeitraum (hier von 1975 bis 2014) ein Gesamtüberschuss  erwirtschaftet (laut BVE geht das Finanzamt nicht vom Vorliegen einer Gesamtverlustes über  den gesamten Tätigkeitszeitraum aus) wurde, kann laut Ansicht des BFG keine Liebhaberei  vorliegen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_162`)


Hier handelt es sich um keine Rechtsfragen von grundsätzlicher Bedeutung, weil das  Bundesfinanzgericht in rechtlicher Hinsicht der in der Begründung dieser Entscheidung  dargestellten Judikatur des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr.in Estelle Niederholz` (person)
- `Hon.-Prof.in OStR Tosca Knoller` (person)
- `Holzplatzgasse 34, 5602 Schwaighof, Österreich` (address)
- `Anwälte Mandl & Mitterbauer GmbH` (organisation)
- `Wiesnerstraße 2, 4950  Altheim` (address)
- `01-700/4800` (tax_number)

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_14`)


Der Antragsteller hat  daraufhin eine Entscheidung über diese Beschwerde durch einen Vorlageantrag an das BFG  beantragt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_20`)


Mit Schreiben vom 23.7.2025 stellte die steuerliche Vertretung den Antrag auf Entscheidung  über die Beschwerde (Vorlageantrag) durch das Bundesfinanzgericht betreffend den Bescheid  über Festsetzung von Anspruchszinsen für das Jahr 2021 vom 12.3.2025.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_21`)


Mit Vorlagebericht vom 8.10.2025 legte das Finanzamt die gegenständliche Beschwerde vom  25.3.2025 betreffend Festsetzung von Anspruchszinsen für das Jahr 2021 dem  Bundesfinanzgericht zur Entscheidung vor und beantragte die Abweisung im Wesentlichen wie  folgt:  „Sachverhalt:   Der Beschwerdeführer (Bf) brachte am 21.08.2023 die Einkommensteuererklärung für das Jahr  2021 ein.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_27`)


Darüber wurde folgendermaßen entschieden:   - die Beschwerde gegen den ESt-Bescheid 2020 wurde mit Beschwerdevorentscheidung (BVE)  vom 12.3.2025 (Anm. laut BFG richtig: 11.03.2025) abgewiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_33`)


Bezüglich der Einkommensteuer sei bereits die Vorlage an das Bundesfinanzgericht  beantragt, eine Entscheidung dazu liege noch nicht vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_51`)


II. Das Bundesfinanzgericht hat erwogen:  1. Beweiswürdigung  Der vorstehende Verfahrensgang (Sachverhalt) ergibt sich aus dem gesamten Akteninhalt, dem  Vorlagebericht, den im Abgabeninformationssystem gespeicherten Daten und aus dem  Vorbringen der Parteien.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_74`)


sowie  zahlreiche Erkenntnisse des Bundesfinanzgerichtes).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_75`)


Wegen dieser Bindung ist der Zinsenbescheid nicht (mit Aussicht auf Erfolg) mit der  Begründung anfechtbar, der maßgebende Einkommensteuerbescheid sei inhaltlich  rechtswidrig (Ritz, BAO8, § 205 Tz 34 mit Hinweis auf die ständige Rechtsprechung des  Bundesfinanzgerichtes).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_78`)


es erfolgt daher keine Abänderung des ursprünglichen  Zinsenbescheides (Ritz, BAO8, § 205 Tz 35 mit Hinweis auf VwGH 28.5.2009, 2006/15/0316,  VwGH 31.1.2019, Ro 2018/15/0005; sowie zahlreiche Erkenntnisse des BFG).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_82`)


Der Antragsteller hat daraufhin eine Entscheidung über diese Beschwerde durch einen  Vorlageantrag an das BFG beantragt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_84`)


Festgehalten wird, dass die vom Vertreter des Bf. genannte Beschwerdevorentscheidung vom  11.3.2025 nicht die Einkommensteuer für das Jahr 2021, sondern die Einkommensteuer für das  Jahr 2020 betrifft (Die Beschwerde gegen den Einkommensteuerbescheid 2020 wurde dem  BFG zur Entscheidung vorgelegt, die noch unerledigt ist, RV/5100771/2025).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_89`)


(Hinweis: Es erging keine Vorlage der Beschwerde gegen  den Einkommensteuerbescheid 2021 an das Bundesfinanzgericht).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_90`)


Unabhängig vom Ausgang der eingebrachten Beschwerde gegen den  Einkommensteuerbescheid für das Jahr 2020 (und der Vorlage an das BFG) ist die Beschwerde  vom 25.3.2025 gegen den Bescheid vom 12.3.2025 betreffend Festsetzung von  Anspruchszinsen (§ 205 BAO) für das Jahr 2021 als unbegründet abzuweisen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_94`)


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `Finanzamtes Österreich` (organisation)
- `75-059/0556` (tax_number)

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_8`)


2. Beweiswürdigung  Die Feststellungen ergeben sich eindeutig aus dem Akt des Finanzamtes und des  Bundesfinanzgerichtes und sind unstrittig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_16`)


Gegen einen Beschluss des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil der Beschluss von der  Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag.Dr. Katrin Allram` (person)
- `Oleg Dell` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `Finanzamtes Österreich` (organisation)
- `80-738/9953` (tax_number)

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_24`)


Mit Eingabe vom 21. Mai 2024 beantragte der Bf. innerhalb verlängerter Frist die Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht sowie die Durchführung einer  mündlichen Verhandlung.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_26`)


Am 13. Juni 2024 legte die belangte Behörde die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_31`)


Am 1. Oktober 2025 fand die beantragte mündliche Verhandlung vor dem Bundesfinanzgericht  statt, in der insbesondere das Vorliegen bzw. Nichtvorliegen von triftigen medizinischen  Gründen diskutiert wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_36`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. bezieht im Streitjahr 2022 Einkünfte aus nichtselbständiger Arbeit.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_63`)


Das Bundesfinanzgericht kommt aus den nachstehenden Gründen im Rahmen der freien  Beweiswürdigung zum Ergebnis, dass die nach der höchstgerichtlichen Rechtsprechung  geforderten triftigen medizinischen Gründe nicht vorliegen:  Zunächst steht unstrittig fest, dass in keinem öffentlichen Krankenhaus eine Terminanfrage  betreffend die Bandscheibenoperation der Ehefrau des Bf. gestellt wurde (vgl. Protokoll zur  Verhandlung vom 1. Oktober 2025 sowie Befundberichte vom 6. und 8. Oktober 2025).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Dr. Dagobert Nordholt` (person)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `FA Kirchdorf Perg Steyr` (organisation)
- `36-532/2242` (tax_number)

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_137`)


Für den Fall, dass der Beschwerde im Zuge der Beschwerdevorentscheidung nicht Rechnung  getragen werde, werde die Vorlage der Beschwerde an das Bundesfinanzgericht  (Vorlageantrag gem. § 264 BAO).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_155`)


Im Zuge einer Akteneinsicht vor dem BFG wurde die Sach- und Rechtslage mit dem Bf., der  mittlerweile steuerlich nicht mehr vertreten ist, eingehend erörtert.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_157`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_158`)


Der oben wiedergegebene Verfahrensablauf wird von den Parteien nicht bestritten, findet im  Akteninhalt Deckung und wird somit vom BFG zum festgestellten Sachverhalt erhoben.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_161`)


Der Sachverhalt und auch die rechtliche Situation wurden dem Bf. anlässlich mehrerer  Telefonate mit ihm und auch im Rahmen der von ihm vorgenommenen Akteneinsicht durch  das BFG erörtert und von ihm zur Kenntnis genommen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 75** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 76** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Mag. Peter Bilger` (person)
- `Ludger Weynand` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)
- `Finanzamtes Österreich` (organisation)

**Example 77** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_14`)


Die Beschwerde sei nachweislich erst am 18.12.2024 vom  zuständigen Sachbearbeiter an das Bundesfinanzgericht vorgelegt worden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 78** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_22`)


5. Am 3.4.2025 stellte der Bf. durch seine steuerliche Vertretung den Antrag auf Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 79** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_23`)


6. Am 21.5.2025 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht vor und  beantragte, die Beschwerde als unbegründet abzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 80** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_25`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 81** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_33`)


Diese Sachverhaltsfeststellungen erfolgen aufgrund der dem Bundesfinanzgericht  vorliegenden Akten des Finanzamtes.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 82** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_105`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_38`)


Insbesondere ist den Curricula der beiden Studien entnehmbar, dass beide Studien „dasselbe  Ausbildungsergebnis" (im Sinne der BFG-Entscheidung RV/0180-L/10) zum Ziel haben (s.  angehängte Curricula und BFG-Entscheidung).

**False Positives:**

- `BFG` — no gold match — likely missing annotation
- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_128`)


Es ist zur Klärung der Rechtsmäßigkeit der Rückforderung zunächst zu prüfen, ob ein  „Studienwechsel“ im Sinne des § 2 Abs. 1 lit. b FLAG 1967 überhaupt vorliegt, bevor auf einen  solchen Studienwechsel die Bestimmungen des § 17 StudFG angewendet werden können (BFG  26.02.2022, RV/2100101/2022 mit Verweis auf VwGH 09.07.2008, 2005/13/0142, Rechtssatz  JWR_2005130142_20080709X02).

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_160`)


BFG 05.07.2016, RV/5100209/2012;

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Österreich`(organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_41`)


Der Bf. erhob gegen das Straferkenntnis mit Anbringen vom 5. September 2025 (fristgerecht)  Beschwerde, führte aus wie im oben angeführten Einspruch gegen die Strafverfügung vom  30. Juni 2025 mit dem Ersuchen, die im Straferkenntnis festgelegte Geldstrafe in Höhe von  65,00 Euro [Anmerkung BFG, gemeint: Geldstrafe in Höhe von 55,00 Euro] herabzusetzen.

**False Positives:**

- `BFG` — partial — pred is substring of gold: `BFG,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG,`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Magistrat der Stadt Wien`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_47`)


BFG  2.10.2024, RV/6100259/2023).

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_56`)


BFG 16.12.2021,  RV/7102723/2021;

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Verwaltungsgerichtshof Entities`

**F1:** 0.386 | **Precision:** 0.954 | **Recall:** 0.242  

**Format:** `regex`  
**Description:**
Matches 'Verwaltungsgerichtshof' and its genitive forms 'Verwaltungsgerichtshofes' and 'Verwaltungsgerichtshofs'.

**Content:**
```
\bVerwaltungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.954 | 0.242 | 0.386 | 65 | 62 | 3 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 62 | 3 | 192 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_46`)


Dem ist zu entgegnen, dass nach der zitierten Judikatur des Verwaltungsgerichtshofes das  Aufrechterhalten des Berufswunsches nicht maßgeblich ist, wenn die Ausbildung nach ihrem  Abbruch nicht wieder aufgenommen wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_55`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_57`)


Im Übrigen wird der zitierten Judikatur des  Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_2`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133  Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_90`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_4`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_132`)


So unterscheidet der Verwaltungsgerichtshof zu § 2  Abs. 1 lit. b vorletzter Satz FLAG ausdrücklich zwischen dem Wechsel der Einrichtung und dem  Wechsel des Studiums.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_141`)


Ein Studienwechsel liegt nach der Rechtsprechung des Verwaltungsgerichtshofes dann vor,  wenn der Student das von ihm begonnene und bisher betriebene, aber noch nicht  abgeschlossene Studium nicht mehr fortsetzt und an dessen Stelle ein anderes unter den  Geltungsbereich des Studienförderungsgesetzes fallendes Studium beginnt (vgl. VwGH  08.01.2001, 2000/12/0053;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_150`)


Würde man die Kriterien betreffend einen  bloßen Studienortwechsel noch enger ziehen, bliebe für die vom Verwaltungsgerichtshof  gezogene Unterscheidung zwischen Studienortwechsel und Studienwechsel (VwGH  09.07.2008, 2005/13/0142) in der Praxis kein Raum, da wie bereits ausgeführt, angesichts des  Bologna-Studiensystems anders als vor Jahrzehnten wohl kaum noch zwei zu 100% identische  Studien in Österreich bzw. europaweit existieren.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Österreich` (country)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_172`)


das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_173`)


Mit dem vorliegenden Erkenntnis folgt das Bundesfinanzgericht der zitierten einheitlichen  Rechtsprechung des Verwaltungsgerichtshofes (insbesondere VwGH 09.07.2008,  2005/13/0142).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_2`)


Gegen diesen Beschluss ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs. 4  Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_19`)


Zulässigkeit einer Revision  Gegen einen Beschluss des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_20`)


Im gegenständlichen Fall ist eine ordentliche Revision an den Verwaltungsgerichtshof nicht  zulässig, weil sich die Rechtsfolge der Einstellung des Säumnisbeschwerdeverfahrens  unmittelbar aus § 284 Abs. 2 BAO ergibt und somit keine Rechtsfrage von grundsätzlicher  Bedeutung zu lösen war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_5`)


III. Eine ordentliche Revision an den Verwaltungsgerichtshof ist nach Art. 133 Abs. 4 Bundes- Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_39`)


Da die  Uneinbringlichkeit einer Geldstrafe ohnehin unter der Sanktion des Vollzuges der  Ersatzfreiheitsstrafe steht, kommt dem Umstand der Gefährdung der Einbringlichkeit der  aushaftenden Forderung im Falle einer Geldstrafe laut Rechtsprechung des  Verwaltungsgerichtshofes kein Gewicht zu.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_48`)


Im Rahmen eines zu Gunsten des Bf. ausgeübten Ermessens erscheinen die im Spruch  festgesetzten Raten noch geeignet - unter Einhaltung der vom Verwaltungsgerichtshof  judizierten Prämissen - einerseits dem Strafzweck ausreichend Rechnung zu tragen und  andererseits die Entrichtung der Geldstrafe in noch angemessener First zu gewährleisten.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_52`)


Zur Unzulässigkeit der Revision  Gegen diese Entscheidung ist gemäß Art. 133 Abs. 4 B-VG eine Revision nicht zulässig, da das  Erkenntnis nicht von der Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung  zukommt, insbesondere weil das Erkenntnis von der Rechtsprechung des  Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt oder die zu lösende  Rechtsfrage in der bisherigen Rechtsprechung des Verwaltungsgerichtshofes nicht einheitlich  beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_50`)


Der Bf. bekämpft mit der gegenständlichen Beschwerde ausschließlich die mit dem  Straferkenntnis festgesetzte Strafhöhe, somit war entsprechend der ständigen Judikatur des  Verwaltungsgerichtshofes von einer Teilrechtskraft des Schuldspruches auszugehen (vgl. z.B.  VwGH 20.9.2013, 2013/17/0305).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_57`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes handelt es sich bei der  Strafzumessung innerhalb eines gesetzlichen Strafrahmens um eine Ermessensentscheidung,  die nach den Kriterien des § 19 VStG vorzunehmen ist (vgl. VwGH 06.04.2005, 2003/04/0031,  VwGH 17.02.2015, Ra 2015/09/0008).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_83`)


Zur Unzulässigkeit der Revision  Eine Revision des Beschwerdeführers an den Verwaltungsgerichtshof ist auf der Grundlage des  § 25a Abs. 4 VwGG kraft Gesetzes unzulässig, da bei Verwaltungsstrafsachen, bei denen eine  Geldstrafe von bis zu 750 Euro verhängt werden darf und im Erkenntnis eine Geldstrafe von  nicht mehr als 400 Euro verhängt wird, eine Verletzung in subjektiven Rechten ausgeschlossen  ist.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_5`)


II. Gegen dieses Erkenntnis ist eine Revision an den Verwaltungsgerichtshof nach Art. 133 Abs.  4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_153`)


An der in diesen beiden Erkenntnis zum Ausdruck gebrachten Rechtsansicht hat der  Verwaltungsgerichtshof in seinem einen Berufsmusiker und Mitglied der Wiener  Philharmoniker betreffenden, Erkenntnis vom 21. September 2005, 2001/13/0241,  festgehalten und sie vertieft.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Missed by this rule (FN):**

- `Wiener  Philharmoniker` (organisation)

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_162`)


Hier handelt es sich um keine Rechtsfragen von grundsätzlicher Bedeutung, weil das  Bundesfinanzgericht in rechtlicher Hinsicht der in der Begründung dieser Entscheidung  dargestellten Judikatur des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_94`)


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_95`)


Die Revision an den  Verwaltungsgerichtshof ist daher unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_3`)


II. Eine ordentliche Revision an den Verwaltungsgerichtshof ist nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_16`)


Gegen einen Beschluss des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil der Beschluss von der  Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_2`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_107`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes muss das Merkmal der  Zwangsläufigkeit auch der Höhe nach gegeben sein.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_123`)


Zum anderen handelt es sich bei der  Frage, ob triftige medizinische Gründe vorliegen oder nicht, um eine solche der  Beweiswürdigung, zu deren Überprüfung der Verwaltungsgerichtshof als Rechtsinstanz  grundsätzlich nicht berufen ist (vgl. VwGH 10.5.2021, Ra 2021/15/0031 und 5.10.2021,  Ra 2021/15/0059).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_3`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_23`)


Nach ständiger  Rechtsprechung des Verwaltungsgerichtshofes sei es Aufgabe des Vertreters, im  Verwaltungsverfahren allfällig vorliegende Gründe aufzuzeigen, die ihn daran gehindert hätten,  die Abgabenschuld am oder nach dem Fälligkeitstag zu begleichen (VwGH 23.03.2010,  2007/13/0137).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_26`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes obliege dem Vertreter der  Nachweis dafür, wie die Zahlungsmittel zur Verfügung gestanden seien und in welchem  Ausmaß die anderen Gläubiger der GmbH noch Befriedigung erlangten, zu erbringen.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_87`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159) sei der Zumutbarkeit bei Heranziehung eines Haftungspflichtigen angesichts  lange verstrichener Zeit im Rahmen der behördlichen Ermessensausübung Bedeutung  beizumessen, allerdings stelle das herangezogene Erkenntnis nicht auf die zurückliegenden  Abgabenschulden ab, sondern auf den Zeitraum zwischen der Beendigung des Konkurses und  der Geltendmachung der Haftung.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_205`)


Kausalität  Infolge der schuldhaften Pflichtverletzung durch den Bf. konnte die Abgabenbehörde nach der  Judikatur des Verwaltungsgerichtshofes (VwGH 17.5.2004, 2003/17/0134), auch davon  ausgehen, dass die Pflichtverletzung Ursache für die Uneinbringlichkeit der  haftungsgegenständlichen Abgaben war.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_209`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159;

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_219`)


Auf die ständige Rechtsprechung des Verwaltungsgerichtshofes wird hingewiesen,  wonach einer Beschwerdevorentscheidung sowie einem Vorlagebericht Vorhaltscharakter  zukommt (vgl. VwGH vom 29.1.2020, Ra 2019/13/0071, VwGH vom 30.6.2021, Ra  2021/15/0048).

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_4`)


II. Gegen dieses Erkenntnis ist eine ordentliche Revision an den Verwaltungsgerichtshof nach  Art. 133 Abs. 4 Bundes-Verfassungsgesetz (B-VG) nicht zulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_105`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |
| `Verwaltungsgerichtshofes` | `Verwaltungsgerichtshofes` |

**Missed by this rule (FN):**

- `Bundesfinanzgerichtes` (organisation)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_107`)


Die (ordentliche) Revision an den Verwaltungsgerichtshof ist daher unzulässig.

| Predicted | Gold |
|---|---|
| `Verwaltungsgerichtshof` | `Verwaltungsgerichtshof` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_135`)


Unter  Zugrundelegung dieser Ausführungen hat der Verwaltungsgerichtshof in der Folge festgestellt,  dass nicht allein der Wechsel der Einrichtung ausschlaggebend ist.

**False Positives:**

- `Verwaltungsgerichtshof` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `Verwaltungsgerichtshofes` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Tax Office Entities`

**F1:** 0.103 | **Precision:** 0.933 | **Recall:** 0.055  

**Format:** `regex`  
**Description:**
Matches Finanzamt and FA variations including common Austrian regions. Explicitly excludes court names to prevent overlap. Added specific pattern for Wien 9/18/19 Klosterneuburg and Wien 6/7/15.

**Content:**
```
\b(?:Finanzamt(?:es)?|FA)\s+(?:Oststeiermark|Waldviertel|Vorarlberg|Bruck\s+Eisenstadt\s+Oberwart|Klosterneuburg|Nieder\u00f6sterreich\s+Mitte|Grieskirchen\s+Wels|Klagenfurt\s+St\.\s+Veit\s+Wolfsberg|Steiermark\s+Mitte|Freistadt\s+Rohrbach\s+Urfahr|Gmunden\s+V\u00f6cklabruck|Spittal\s+Villach|Landeck\s+Reutte|Wien\s+8/16/17|Wien\s+2/20/21/22|Wien\s+1/23|Wien\s+6/7/15|Kirchdorf\s+Perg\s+Steyr|Innsbruck|Linz|Deutschlandsberg\s+Leibnitz\s+Voitsberg|Braunau\s+Ried\s+Sch\u00e4rding|St\.\s+Johann\s+Tamsweg\s+Zell\s+am\s+See|Judenburg\s+Liezen|Salzburg-Stadt|Salzburg-Land|Ost|Purkersdorf|Baden\s+M\u00f6dling|Schwechat\s+Gerasdorf|Tirol\s+Ost|Graz-Stadt|Amstetten\s+Melk\s+Scheibbs|Hollabrunn\s+Korneuburg\s+Tulln|\u00d6sterreich|Wien\s+9/18/19\s+Klosterneuburg)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.933 | 0.055 | 0.103 | 15 | 14 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 14 | 1 | 242 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Hon.-Prof. Gotthard Clement  in der Beschwerdesache Willibald Endrowait,  St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich, über die Beschwerde vom 3. Dezember 2019 gegen den Bescheid des  FA Graz-Stadt  vom 12. November 2019 über die Rückforderung zu Unrecht bezogener Beträge an  Familienbeihilfe und Kinderabsetzbeträgen für das Kind Stella Marschalk, Bakk. techn.  für den Zeitraum  November 2017 bis Juni 2018 in Höhe von insgesamt 1.781,80 Euro zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Graz-Stadt` | `FA Graz-Stadt` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Hon.-Prof. Gotthard Clement` (person)
- `Willibald Endrowait` (person)
- `St.-Elisabeth-Platz 66, 8502 Heuholz, Österreich` (address)
- `Stella Marschalk, Bakk. techn.` (person)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `85-919/9176` (tax_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `6207 150171` (social_security_number)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |

**Missed by this rule (FN):**

- `Franz Josefskai 53/2/10, 1010 Wien` (address)
- `94-300/0486` (tax_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Wien 9/18/19 Klosterneuburg` | `Finanzamtes Wien 9/18/19 Klosterneuburg` |
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `75-059/0556` (tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Katrin Allram` (person)
- `Oleg Dell` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `80-738/9953` (tax_number)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Dagobert Nordholt  in der Beschwerdesache Dieter Leufkes,  Franz Steiner Weg 3, 9433 Mosern, Österreich, über die Beschwerde vom 17. März 2016 gegen den Bescheid des FA Kirchdorf Perg Steyr  vom 11. Jänner 2016 betreffend Haftungsbescheid / Sonstige 2016 Steuernummer  36-532/2242  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `FA Kirchdorf Perg Steyr` | `FA Kirchdorf Perg Steyr` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Dagobert Nordholt` (person)
- `Dieter Leufkes` (person)
- `Franz Steiner Weg 3, 9433 Mosern, Österreich` (address)
- `36-532/2242` (tax_number)

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

| Predicted | Gold |
|---|---|
| `Finanzamt Kirchdorf Perg Steyr` | `Finanzamt Kirchdorf Perg Steyr` |

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Ludger Weynand` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

## `Finanzamt Österreich`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' and 'Finanzamtes Österreich'.

**Content:**
```
\bFinanzamt(?:es)?\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.889 | 0.031 | 0.060 | 9 | 8 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 1 | 230 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `85-919/9176` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `6207 150171` (social_security_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `75-059/0556` (tax_number)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Katrin Allram` (person)
- `Oleg Dell` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `80-738/9953` (tax_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Ludger Weynand` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

## `Finanzamt Österreich Extended`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Österreich' and 'Finanzamtes Österreich' including the optional '(DST12)' suffix.

**Content:**
```
\bFinanzamt(?:es)?\s+Österreich(?:\s*\(DST12\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.889 | 0.031 | 0.060 | 9 | 8 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 8 | 1 | 230 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Dr. Siegfried Fenz in der Beschwerdesache  Frauke Stuhldreher, Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich, über die Beschwerde vom 30. Juni 2021 gegen den Bescheid des  Finanzamtes Österreich vom 1. Juni 2021 betreffend Gewährung von Familienbeihilfe ab Juli  2019, Steuernummer 85-919/9176, zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Dr. Siegfried Fenz` (person)
- `Frauke Stuhldreher` (person)
- `Dr. Julius Wagner-Jauregg-Straße 20, 2552 Hirtenberg, Österreich` (address)
- `85-919/9176` (tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Ashley Partenfelder  in der Beschwerdesache Patricia Jentz,  Pinnisalm 3, 4694 Penesdorf, Österreich, über die Beschwerde vom 7. Oktober 2021 gegen den Bescheid des  Finanzamtes Österreich vom 17. September 2021 zu SVNR 6207 150171  betreffend  Rückforderung der Familienbeihilfe und des Kinderabsetzbetrages von insgesamt EUR 4.163,20  für den Zeitraum von jeweils Oktober 2019 bis Jänner 2021 für die Kinder der  Beschwerdeführerin mit der SVNr.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Ashley Partenfelder` (person)
- `Patricia Jentz` (person)
- `Pinnisalm 3, 4694 Penesdorf, Österreich` (address)
- `6207 150171` (social_security_number)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


BESCHLUSS  Das Bundesfinanzgericht hat durch die Richterin Priv.-Doz.in Farina Kohlstrunk  in der Beschwerdesache Mathilda Eckholdt,  Kleingassen 3, 4150 Reith, Österreich, vertreten durch Mag. András Péter Radics, Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See, über die Beschwerde vom 8. Oktober 2025, beim Bundesfinanzgericht  am 10. Oktober 2025 eingelangt, wegen behaupteter Verletzung der Entscheidungspflicht  durch das Finanzamt Österreich betreffend einen Antrag auf Durchführung der  Arbeitnehmerveranlagung für das Jahr 2024 vom 31. März 2025, Steuernummer  69-575/0475, beschlossen:  Das Säumnisbeschwerdeverfahren wird gemäß § 284 Abs. 2 letzter Satz BAO eingestellt.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz.in Farina Kohlstrunk` (person)
- `Mathilda Eckholdt` (person)
- `Kleingassen 3, 4150 Reith, Österreich` (address)
- `Mag. András Péter Radics` (person)
- `Obere Hauptstraße 18-20 Tür Top  6, 7100 Neusiedl/See` (address)
- `Bundesfinanzgericht` (organisation)
- `69-575/0475` (tax_number)

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Hon.-Prof. Thassilo Averdiek` (person)
- `Alma Springel` (person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich` (address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg` (organisation)
- `75-059/0556` (tax_number)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag.Dr. Katrin Allram in der Beschwerdesache  Oleg Dell, Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich, vertreten durch CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH, Hegelgasse 8, 1010 Wien, über die Beschwerde vom 8. Februar 2024  gegen den Bescheid des Finanzamtes Österreich vom 5. Jänner 2024 betreffend  Einkommensteuer 2022, Steuernummer 80-738/9953, nach Durchführung einer  mündlichen Verhandlung am 1. Oktober 2025 und am 6. November 2025 zu Recht erkannt:  I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag.Dr. Katrin Allram` (person)
- `Oleg Dell` (person)
- `Ignaz-Halmetschlager-Gasse 6, 9523 St. Michael, Österreich` (address)
- `CENTURION Wirtschaftsprüfungs- und  SteuerberatungsgmbH` (organisation)
- `Hegelgasse 8, 1010 Wien` (address)
- `80-738/9953` (tax_number)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch den Richter Mag. Peter Bilger in der Beschwerdesache  Ludger Weynand, Plestätten 139Y, 4923 Reintal, Österreich, Steuernummer 27-924/8149, über die Beschwerde vom  11. März 2025 gegen den Bescheid des Finanzamtes Österreich vom 9. Jänner 2025 betreffend  Säumniszuschlag 2024 zu Recht erkannt:   I. Der Beschwerde wird teilweise stattgegeben.

| Predicted | Gold |
|---|---|
| `Finanzamtes Österreich` | `Finanzamtes Österreich` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Peter Bilger` (person)
- `Ludger Weynand` (person)
- `Plestätten 139Y, 4923 Reintal, Österreich` (address)
- `27-924/8149` (tax_number)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Finanzamtes  Österreich` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

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

## `Magistrat der Stadt Wien`

**F1:** 0.046 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Wien' and 'Magistrates der Stadt Wien' including department extensions like 'MA 67' or 'Magistratsabteilung 67'. Updated to handle the full span including the department.

**Content:**
```
\bMagistrat(?:es)?\s+der\s+Stadt\s+Wien(?:\s*,\s+(?:MA\s+\d+|Magistratsabteilung\s+\d+))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.023 | 0.046 | 6 | 6 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 6 | 0 | 122 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien, MA 67` | `Magistrat der Stadt Wien, MA 67` |
| `Magistrates der Stadt Wien` | `Magistrates der Stadt Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Mag. Gabriele Friedbacher` (person)
- `Wilhelm Konetzny` (person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich` (address)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

## `Landespolizeidirektion Wien`

**F1:** 0.031 | **Precision:** 1.000 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Landespolizeidirektion Wien'.

**Content:**
```
\bLandespolizeidirektion\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.016 | 0.031 | 4 | 4 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 0 | 222 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_55`)


Am 11. September 2019 bewilligte die Landespolizeidirektion Wien - Verkehrsamt - der Tochter  des Bf. gemäß § 122 Kraftfahrgesetz 1967 die Vornahme von Übungsfahrten für die Klasse B bis  zum 11. März 2021 mit dem Begleiter (Bf.) (Bewilligungsbescheid).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_57`)


Am 20. Februar 2020 überwies der Bf. € 173,10 an die Landespolizeidirektion Wien -  Verkehrsamt (handschriftlich vom Bf. eingefügt: Führerschein Maximiliane Sakschewsky, MA).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Maximiliane Sakschewsky, MA` (person)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_75`)


Diesen Lebensumständen stehen folgende inländische (österreichische) Anknüpfungspunkte  gegenüber: Nachweisliche Aufenthalte  - am 18. August 2019 (6-stündige Unterweisung in die „LEBENSRETTENDEN  SOFORTMASSNAHMEN AM ORT DES VERKEHRSUNFALLS" im Hinblick auf den beabsichtigten  Führerscheinerwerb),  vom 28. Oktober bis 1. November und 16. Dezember bis 25. Dezember 2019 sowie  17. bis 19. Februar 2020 (in Wien mit dem Bf. unternommene Fahrten gemäß § 19 Abs. 8 FSG;  am 20. Februar 2020 wurde vom Bf. die Überweisung von € 173,10 an die  Landespolizeidirektion Wien - Verkehrsamt vorgenommen).

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `Wien` (city)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_7`)


von einem Kontrollorgan der Parkraumüberwachung der Landespolizeidirektion Wien (DNr) am  2. Mai 2025 um 11:09 Uhr in 1100 Wien, Gasse, beanstandet, da ein gültiger Parkschein fehlte.

| Predicted | Gold |
|---|---|
| `Landespolizeidirektion Wien` | `Landespolizeidirektion Wien` |

**Missed by this rule (FN):**

- `1100 Wien` (address)

</details>

---

## `University Entities`

**F1:** 0.031 | **Precision:** 0.667 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches Universität Wien, Wirtschaftsuniversität Wien, and Universität Innsbruck.

**Content:**
```
\b(?:Universität\s+Wien|Wirtschaftsuniversität\s+Wien|Universität\s+Innsbruck)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.016 | 0.031 | 6 | 4 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 2 | 207 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_9`)


angerechneten Prüfungen (ECTS-Punkte) vom Studienzeitraum 10/2017 bis 09/2019  (Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien) in  den Studienzeitraum ab 10/2019 (Bachelorstudium Wirtschaftswissenschaften an der  Johannes Kepler Universität Linz).

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes Kepler Universität Linz` (organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_72`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Die Tochter der Bf. (Viktoria Immohr) studierte von Oktober 2017 – September 2019 das  Bachelorstudium Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien  (Studienkennzahl UJ033 561) und wechselte mit Oktober 2019 zum Bachelorstudium  Wirtschaftswissenschaften an der Johannes Kepler Universität Linz (Studienkennzahl UK033  572), welches sie bis zum 14. Dezember 2020 betrieb.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Viktoria Immohr` (person)
- `Johannes Kepler Universität Linz (` (organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_124`)


Im Beschwerdefall geht die belangte Behörde davon aus, dass die Tochter der Bf. mit dem  Wechsel vom Bachelorstudium Wirtschafts- und Sozialwissenschaften an der  Wirtschaftsuniversität Wien nach dem Sommersemester 2019, somit nach dem vierten  Semester des dort betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an  der Johannes Kepler Universität Linz mit dem Wintersemester 2019/2020 einen  Studienwechsel (und nicht bloß einen Studienortwechsel) vorgenommen habe.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes Kepler Universität Linz` (organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_147`)


Nach unstrittigem Sachverhalt hat die Tochter der Bf. mit dem Wechsel vom Bachelorstudium  Wirtschafts- und Sozialwissenschaften an der Wirtschaftsuniversität Wien nach dem  Sommersemester 2019, somit nach dem vierten Semester des seit Oktober 2017 dort  betriebenen Studiums, zum Bachelorstudium Wirtschaftswissenschaften an der Johannes  Kepler Universität Linz mit dem Wintersemester 2019/2020 jedenfalls einen Studienortwechsel  vorgenommen.

| Predicted | Gold |
|---|---|
| `Wirtschaftsuniversität Wien` | `Wirtschaftsuniversität Wien` |

**Missed by this rule (FN):**

- `Johannes  Kepler Universität Linz` (organisation)

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_10`)


2. Die Bf. legte mit am 09.08.2021 eingelangter Vorhaltsbeantwortung folgende Unterlagen  vor:   Studienerfolgsnachweis an der Wirtschaftsuniversität Wien (WU Wien) vom  07.09.2019 betreffend das Bachelorstudium Wirtschafts- und Sozialwissenschaften  (Studienkennzahl UJ 033561), aus welchem unter anderem die erfolgreiche  Absolvierung von 42 ECTS-Punkten hervorgeht:    [...]

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU Wien)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU Wien)`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_87`)


Strittig war, ob durch den Wechsel der Bf. vom Bachelorstudium „Wirtschafts- und  Sozialwissenschaften“ an der Wirtschaftsuniversität Wien (WU) zum Bachelorstudium  „Wirtschaftswissenschaften“ an der Johannes Kepler Universität Linz (JKU) ein Studienwechsel  (Argumentation des Finanzamtes) oder bloß ein Studienortwechsel (Argumentation der Bf.)  vorlag.

**False Positives:**

- `Wirtschaftsuniversität Wien` — partial — pred is substring of gold: `Wirtschaftsuniversität Wien (WU)`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Wirtschaftsuniversität Wien (WU)`(organisation)
- `Johannes Kepler Universität Linz (JKU)`(organisation)

</details>

---

## `VwGH Acronym`

**F1:** 0.022 | **Precision:** 0.034 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches the acronym 'VwGH' as a standalone entity, ensuring it is captured even in citation contexts.

**Content:**
```
\bVwGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.034 | 0.016 | 0.022 | 116 | 4 | 112 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 112 | 240 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_148`)


Wie der VwGH bereits in mehreren Erkenntnissen ausfgeührt hat erfordert die berufliche  Tätigkeit eines hauptberuflichen Musikers ein musikalisches Niveau, welches nur durch  regelmäßige Arbeit am Instrument zu erreichen und zu halten ist.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_94`)


Nach der Rechtsprechung des VwGH setzt eine Zwangsläufigkeit aus sittlichen Gründen voraus,  dass sich der Steuerpflichtige nach dem Urteil billig und gerecht denkender Menschen zu der  Leistung verpflichtet halten kann.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_226`)


Auf  die einheitliche zitierte Judikatur des VwGH wird verwiesen.

| Predicted | Gold |
|---|---|
| `VwGH` | `VwGH` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_40`)


Nach der Judikatur des Verwaltungsgerichtshofes sind der Natur der Dinge entsprechende  Unterbrechungen des tatsächlichen Ausbildungsvorganges für einen bereits vorher  entstandenen Anspruch auf Familienbeihilfe nicht schädlich (VwGH 20.06.2000, 98/15/0001).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_41`)


Dazu zählen beispielsweise Erkrankungen, die die Berufsausbildung auf begrenzte Zeit  unterbrechen, oder Urlaube und Schulferien (VwGH vom 16.11.1993, 90/14/0108).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_44`)


Das bloße Aufrechterhalten eines  Berufswunsches ist der tatsächlichen Ausbildung nicht gleichzuhalten (VwGH 24.9.2009,  2009/16/0088, VwGH 21.01.2004, 2003/13/0157, VwGH 14.12.1995, 93/15/0133).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 3

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_50`)


Entscheidend ist somit lediglich, ob der Empfänger die  Beträge zu Unrecht erhalten hat (vgl. VwGH 28.10.2009, 2008/15/0329).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_56`)


Ob eine Berufsausbildung im Sinne des FLAG 1967 vorliegt, ist eine Tatfrage (vgl. VwGH  16.11.1993, 90/14/0108), welche in freier Beweiswürdigung zu beantworten ist und einer  ordentlichen Revision nicht zugänglich ist.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_128`)


Es ist zur Klärung der Rechtsmäßigkeit der Rückforderung zunächst zu prüfen, ob ein  „Studienwechsel“ im Sinne des § 2 Abs. 1 lit. b FLAG 1967 überhaupt vorliegt, bevor auf einen  solchen Studienwechsel die Bestimmungen des § 17 StudFG angewendet werden können (BFG  26.02.2022, RV/2100101/2022 mit Verweis auf VwGH 09.07.2008, 2005/13/0142, Rechtssatz  JWR_2005130142_20080709X02).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_141`)


Ein Studienwechsel liegt nach der Rechtsprechung des Verwaltungsgerichtshofes dann vor,  wenn der Student das von ihm begonnene und bisher betriebene, aber noch nicht  abgeschlossene Studium nicht mehr fortsetzt und an dessen Stelle ein anderes unter den  Geltungsbereich des Studienförderungsgesetzes fallendes Studium beginnt (vgl. VwGH  08.01.2001, 2000/12/0053;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_150`)


Würde man die Kriterien betreffend einen  bloßen Studienortwechsel noch enger ziehen, bliebe für die vom Verwaltungsgerichtshof  gezogene Unterscheidung zwischen Studienortwechsel und Studienwechsel (VwGH  09.07.2008, 2005/13/0142) in der Praxis kein Raum, da wie bereits ausgeführt, angesichts des  Bologna-Studiensystems anders als vor Jahrzehnten wohl kaum noch zwei zu 100% identische  Studien in Österreich bzw. europaweit existieren.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)
- `Österreich`(country)

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_167`)


Für die Überprüfung dieser  Frage erachte es der VwGH als ausreichend, die Unterscheidung auf die Kernfächer bzw. den  Kernbereich des Studiums zu reduzieren (VwGH 7.8.2001, 97/14/0068).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_173`)


Mit dem vorliegenden Erkenntnis folgt das Bundesfinanzgericht der zitierten einheitlichen  Rechtsprechung des Verwaltungsgerichtshofes (insbesondere VwGH 09.07.2008,  2005/13/0142).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Verwaltungsgerichtshofes`(organisation)

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_31`)


Die Gewährung von Zahlungserleichterungen für die Entrichtung von Geldstrafen und Kosten  nach dem Finanzstrafgesetz richtet sich damit nach § 212 BAO (vgl. VwGH 24.02.2011,  2010/16/0276, uHa Vorjudikatur).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_44`)


Ebenso trifft es allerdings zu, dass der  Ruin der wirtschaftlichen Existenz des Bestraften den mit der Bestrafung verfolgten Zweck  auch nicht sinnvoll erreicht (vgl. VwGH 24.9.2003, 2003/13/0084, ÖStZ 2004/190, ÖStZB  2004/109).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_50`)


Der Bf. bekämpft mit der gegenständlichen Beschwerde ausschließlich die mit dem  Straferkenntnis festgesetzte Strafhöhe, somit war entsprechend der ständigen Judikatur des  Verwaltungsgerichtshofes von einer Teilrechtskraft des Schuldspruches auszugehen (vgl. z.B.  VwGH 20.9.2013, 2013/17/0305).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_57`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes handelt es sich bei der  Strafzumessung innerhalb eines gesetzlichen Strafrahmens um eine Ermessensentscheidung,  die nach den Kriterien des § 19 VStG vorzunehmen ist (vgl. VwGH 06.04.2005, 2003/04/0031,  VwGH 17.02.2015, Ra 2015/09/0008).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_136`)


Ausschlaggebend ist daher, ob die konkrete Tätigkeit bei Anlegen eines  abstrakten Maßstabes ("typischerweise") einen Zusammenhang mit einer in der  Lebensführung begründeten Neigung aufweist, wie dies etwa bei einer nebenberuflich  betriebenen schriftstellerischen Tätigkeit zur Herausgabe eines Sachbuches, die erst auf Grund  der hobbymäßigen Beschäftigung mit jener Materie, die im Sachbuch behandelt wird, zu  bejahen ist (VwGH vom 26.4.2000, 96/14/0095).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_151`)


Solcherart kann der Mittelpunkt der Tätigkeit einer Konzertpianistin nach der  Verkehrsauffassung an dem Ort angenommen werden, an dem sie die überwiegende Zeit an  ihrem Instrument verbringt, im Beschwerdefall in dem in Rede stehenden Arbeitszimmer  (VwGH vom 24. Juni 2004, 2001/15/0052).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_65`)


Anspruchszinsen im Sinne des § 205 BAO sind eine objektive Rechtsfolge, um mögliche  Zinsvorteile oder Zinsnachteile auszugleichen, die sich aus unterschiedlichen Zeitpunkten der  Abgabenfestsetzung ergeben (VwGH 24.9.2008, 2007/15/0175).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_67`)


Eine rechtskräftige Einkommen- oder  Körperschaftsteuerfestsetzung wird vom Gesetz nicht verlangt (VwGH 27.3.2008,  2008/13/0036).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_72`)


Der Zinsenbescheid ist an die im Spruch des zur Nachforderung oder Gutschrift führenden  Bescheides ausgewiesene Nachforderung bzw. Gutschrift gebunden (Ritz, BAO8, § 205 mit  Hinweis auf VwGH 27.2.2008, 2005/13/0039;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_73`)


VwGH 27.3.2008, 2008/13/0036;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_78`)


es erfolgt daher keine Abänderung des ursprünglichen  Zinsenbescheides (Ritz, BAO8, § 205 Tz 35 mit Hinweis auf VwGH 28.5.2009, 2006/15/0316,  VwGH 31.1.2019, Ro 2018/15/0005; sowie zahlreiche Erkenntnisse des BFG).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_62`)


Ob solche triftigen  Gründe vorliegen oder nicht, ist eine Frage der Beweiswürdigung (vgl. VwGH 5.10.2021,  Ra 2021/15/0059).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

**False Positives:**

- `VwGH` — similar text (different position): `VwGH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VwGH`(organisation)

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_99`)


Eine allgemeine sittliche  Pflicht, Dritten beizustehen, besteht hingegen nicht (vgl. VwGH 27.9.1995, 92/15/0214).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_104`)


Auch Aufwendungen, die nicht von der  gesetzlichen Krankenversicherung getragen werden, können dem Steuerpflichtigen  zwangsläufig erwachsen, wenn sie aus triftigen Gründen medizinisch geboten sind (vgl. VwGH  11.2.2016, 2013/13/0064 mwN).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_108`)


Dabei ist zu beachten, dass triftige  medizinische Gründe auch höhere Aufwendungen als die von Sozialversicherungsträgern  finanzierten zwangsläufig erscheinen lassen (vgl. VwGH 11.2.2022, Ra 2020/13/0062).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_110`)


Die triftigen medizinischen Gründe  müssen vielmehr in feststehenden oder sich konkret abzeichnenden ernsthaften  gesundheitlichen Nachteilen bestehen, welche ohne die mit höheren Kosten verbundene  medizinische Betreuung eintreten würden (vgl. VwGH 13.5.1986, 85/14/0181).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_111`)


Will ein Steuerpflichtiger Aufwendungen als außergewöhnliche Belastung berücksichtigt  wissen, hat er selbst alle Umstände darzulegen, auf welche die abgabenrechtliche  Begünstigung gestützt werden kann (vgl. VwGH 22.12.2004, 2001/15/0116).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_123`)


Zum anderen handelt es sich bei der  Frage, ob triftige medizinische Gründe vorliegen oder nicht, um eine solche der  Beweiswürdigung, zu deren Überprüfung der Verwaltungsgerichtshof als Rechtsinstanz  grundsätzlich nicht berufen ist (vgl. VwGH 10.5.2021, Ra 2021/15/0031 und 5.10.2021,  Ra 2021/15/0059).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_23`)


Nach ständiger  Rechtsprechung des Verwaltungsgerichtshofes sei es Aufgabe des Vertreters, im  Verwaltungsverfahren allfällig vorliegende Gründe aufzuzeigen, die ihn daran gehindert hätten,  die Abgabenschuld am oder nach dem Fälligkeitstag zu begleichen (VwGH 23.03.2010,  2007/13/0137).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_29`)


Unter diesen Umständen hafte er für die uneinbringlichen  Abgabenschuldigkeiten im vollen Ausmaß (z.B. VwGH 22.12.2005, 2005/15/0114).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_30`)


Werde der Nachweis einer Gläubigergleichbehandlung nicht in nachvollziehbarer Weise  erbracht, liege es im Ermessen des Finanzamtes, die Haftung für die genannten  Abgabenbeträge auszusprechen, bei Benachteiligung des Abgabengläubigers im Ausmaß der  nachgewiesenen Benachteiligung der Abgabenschuldigkeiten gegenüber den anderen  Verbindlichkeiten der GmbH (z.B. VwGH 29.1.2004, 2000/15/0168).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_31`)


Da der öffentliche Auftrag  zur Ergreifung aller Mittel, vollstreckbare Abgaben einzubringen, bei einer vorzuwerfenden  Pflichtverletzung allfällige Einzelinteressen verdränge (z.B. VwGH 10.10.2005, 2004/14/0112),  sähe sich das Finanzamt veranlasst, die gesetzliche Vertreterhaftung im erforderlichen Ausmaß  geltend zu machen.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_52`)


Die Haftung gem. § 9 BAO sei eine Ausfallshaftung (VwGH 24.2.2004,  99/14/0278).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_53`)


Voraussetzung sei die objektive Uneinbringlichkeit der betreffenden Abgaben im  Zeitpunkt der Inanspruchnahme des Haftenden (VwGH 31.3.2004, 2003/13/0153).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_55`)


Zur Verletzung abgabenrechtlicher Pflichten des Vertreters führte das Finanzamt weiters aus,  dass es haftungsrelevant nur sei, wenn sich die Uneinbringlichkeit aus der Verletzung  abgabenrechtlicher Pflichten ergebe (VwGH 18.10.1995, 91/13/0038).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_56`)


Zu den abgabenrechtlichen Pflichten würden insbesondere gehören:  die Abgabenentrichtung aus den Mitteln, die der Vertreter verwalte,  die Führung gesetzlicher Aufzeichnungen (VwGH 30.5.1989, 89/14/0043),  die zeitgerechte Einreichung von Abgabenerklärungen (VwGH 29.5.2001, 2000/14/0006).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_57`)


Die Pflicht des Vertreters, die vom Vertretenen geschuldeten Abgaben zu entrichten, bestehe  nur insoweit, als hierfür liquide Mittel vorhanden seien (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_58`)


Der Zeitpunkt, für den zu beurteilen sei, ob der Primärschuldnerin die für die  Abgabenentrichtung erforderlichen Mittel zur Verfügung standen, bestimme sich danach,  wann die Abgaben bei Beachtung der abgabenrechtlichen Vorschriften zu entrichten gewesen  wären (VwGH 27.4.2000, 98/15/0003;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_59`)


VwGH 31.10.2000, 95/15/0137).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_64`)


Er dürfe hierbei  Abgabenschulden nicht schlechter behandeln als die übrigen Schulden (VwGH 27.05.1998,  95/13/0170;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_65`)


VwGH 17.08.1998, 97/17/0096, 29.03.2001, 2000/16/0149).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_66`)


Er sei jedoch nicht verpflichtet, den Abgabengläubiger besser als die übrigen Gläubiger zu  behandeln (VwGH 17.8.1998, 98/17/0038).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_68`)


(VwGH 22.9.1999, 96/15/0049;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_69`)


VwGH 24.10.2000,  95/14/0090;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_70`)


VwGH 29.3.2001, 2000/14/0149).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_72`)


vielmehr habe der Vertreter das Fehlen ausreichender Mittel nachzuweisen   (VwGH 26.9.2000, 99/13/0090;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_73`)


VwGH 9.8.2001, 98/16/0348).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_74`)


Gelinge ein solcher Nachweis   nicht, könne die Haftung für den gesamten uneinbringlichen Abgabenrückstand geltend  gemacht werden (VwGH 27.9.2000, 95/14/0056, VwGH 29.3.2001, 2000/14/0149).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_76`)


Die Behörde habe bei entsprechenden Behauptungen und diesbezüglichem  Beweisanbot die zur Entlastung des Vertreters angebotenen Beweise aufzunehmen und  erforderliche Präzisierungen abzufordern, jedenfalls aber konkrete Feststellungen über die  angebotenen Entlastungsbehauptungen zu treffen (VwGH 23.4.1998, 95/15/0145;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_77`)


VwGH  20.4.1999, 94/14/0147).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_85`)


(VwGH 25.6.1990,  89/15/0067).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_87`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159) sei der Zumutbarkeit bei Heranziehung eines Haftungspflichtigen angesichts  lange verstrichener Zeit im Rahmen der behördlichen Ermessensausübung Bedeutung  beizumessen, allerdings stelle das herangezogene Erkenntnis nicht auf die zurückliegenden  Abgabenschulden ab, sondern auf den Zeitraum zwischen der Beendigung des Konkurses und  der Geltendmachung der Haftung.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_92`)


Ihm als Vertreter der GmbH sei der Nachweis oblegen, welcher Betrag bei Gleichbehandlung  sämtlicher Gläubiger bezogen auf die jeweiligen Fälligkeitszeitpunkte einerseits und das  Vorhandensein liquider Mittel andererseits - an die Abgabenbehörde zu entrichten gewesen  wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_95`)


Eine Ausnahme vom Gleichheitsgrundsatz bestehe für Abfuhrabgaben, wie die Lohnsteuer  (VwGH 29.6.1999, 99/14/0040;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_96`)


VwGH 22.2.2001, 2000/15/0227).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_99`)


die auf den gekürzten Lohnbetrag  entfallende Lohnsteuer sei zur Gänze zu entrichten (VwGH 16.2.2000, 95/15/0046).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_102`)


Eine weitere Ausnahme vom Gleichheitsgrundsatz bestehe für Abfuhrabgaben, wie die  Kapitalertragsteuer (VwGH 16.2.2000, 95/15/0046).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_104`)


Die Pflicht zur Einbehaltung und Abfuhr der Kapitalertragsteuer (§§ 95, 96 EstG 1998) hätten  unter der Sanktion des § 9 Abs. 1 BAO die Vertreter der juristischen Personen zu erfüllen  (VwGH 3.7.2003, 2000/15/0043).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_105`)


Dies gelte auch für die Kapitalertragsteuer aus verdeckten  Gewinnausschüttungen (VwGH 16.11.2006, 2002/14/0010).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_107`)


Eine bestimmte Schuldform sei hierfür nicht erforderlich  (VwGH 22.2.2000, 96/14/0158;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_108`)


VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_109`)


Daher reiche leichte  Fahrlässigkeit (VwGH 18.10.1995, 91/13/0037, VwGH 31.10.2000, 95/15/0137).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_110`)


Der Vertreter habe dazutun, weshalb er nicht dafür habe Sorge getragen habe, dass der  Vertretene die Abgaben entrichtet habe, widrigenfalls von der Abgabenbehörde eine  schuldhafte Pflichtverletzung angenommen werden dürfe (VwGH 31.10.2000, 95/15/0137;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_111`)


VwGH 29.5.2001, 99/14/0277;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_112`)


VwGH 9.8.2001, 98/16/0348).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_113`)


In der Regel werde nämlich nur  der Vertreter jenen ausreichenden Einblick in die Gebarung des Vertretenen haben, der ihm  entsprechende Behauptungen und Nachweise ermögliche (VwGH 19.11.1998, 97/15/0115;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_114`)


VwGH 29.6.1999, 99/14/0128).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_115`)


Der Vertreter habe für die Möglichkeit des Nachweises seines  pflichtgemäßen Verhaltens vorzusorgen (VwGH 7.9.1990, 89/14/0132).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_116`)


Ihm obliege kein  negativer Beweis, sondern die konkrete (schlüssige) Darstellung der Gründe, die etwa der  rechtzeitigen Abgabenentrichtung entgegengestanden seien (VwGH 4.4.1990, 89/13/0212).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_121`)


Bei schuldhafter  Pflichtverletzung dürfe die Abgabenbehörde mangels dagegensprechender Umstände  annehmen, dass die Pflichtverletzung Ursache der Uneinbringlichkeit sei (VwGH 16.12.1999,  97/15/0051;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_122`)


VwGH 20.6.2000, 98/15/0084).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 74** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_141`)


Dazu führte das Finanzamt in der Begründung aus, dass die Geltendmachung einer Haftung in  das Ermessen der Abgabenbehörde gestellt sei (VwGH 23.1.1997, 95/15/0173), wobei die  Ermessensentscheidung im Sinne des § 20 BAO innerhalb der vom Gesetz gezogenen Grenzen  nach Billigkeit und Zweckmäßigkeit unter Berücksichtigung aller in Betracht kommenden  Umstände zu treffen sei.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 75** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_143`)


Aus dem auf die Hereinbringung der Abgabenschuld beim Haftenden gerichteten  Besicherungszweck der Haftungsnorm folge, dass die Geltendmachung der Haftung in der  Regel ermessenskonform sei, wenn die betreffende Abgabe beim Primärschuldner  uneinbringlich sei (vgl. VwGH 25.6.1990, 89/15/0067).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 76** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_145`)


Zum Hinweis, dass die Haftungssumme aufgrund der Vermögenslage nicht einbringlich sei,  werde auf die ständige Rechtsprechung des Verwaltungsgerichtshofes verwiesen, der darin  anführt, dass die Abgabenbehörde die Frage der Einbringlichkeit der Haftungsschuld beim  Haftenden bei ihren Zweckmäßigkeitsüberlegungen vernachlässigen könne und persönliche  Umstände wie die „wirtschaftliche Leistungsfähigkeit" oder eine Vermögenslosigkeit des  Haftenden in keinem erkennbaren Zusammenhang mit der Geltendmachung der Haftung  stünden (VwGH 28.05.2008, 2006/15/0007 und 2006/15/0089).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 77** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_146`)


Selbst wenn auf Grund der derzeitigen wirtschaftlichen Situation des Beschwerdeführers die  Abgaben erschwert einbringlich seien, ließe sich daraus eine Unzumutbarkeit der  Haftungsinanspruchnahme nicht ableiten, weil es nach der Rechtsprechung nicht zutreffe, dass  die Haftung nur bis zur Höhe der aktuellen Einkünfte bzw. des aktuellen Vermögens geltend  gemacht werden dürfte (vgl. VwGH 29.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 78** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_148`)


Wie bereits im Haftungsbescheid vom 11.01.2016 ausgeführt, obliege dem Vertreter der GmbH  der Nachweis, welcher Betrag bei Gleichbehandlung sämtlicher Gläubiger bezogen auf die  jeweiligen Fälligkeitszeitpunkte einerseits und das Vorhandensein liquider Mittel andererseits  an die Abgabenbehörde zu entrichten gewesen wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 79** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 80** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_188`)


Nach der ständigen Rechtsprechung des Verwaltungsgerichtshofes ist es Sache des  Geschäftsführers, die Gründe darzulegen, die ihn ohne sein Verschulden daran gehindert  haben, die ihm obliegenden abgabenrechtlichen Verpflichtungen zu erfüllen (VwGH  18.10.1995, 91/13/0037, 0038).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 81** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_189`)


Er hat also darzutun, weshalb er nicht dafür Sorge tragen  konnte, dass die Gesellschaft die anfallenden Abgaben rechtzeitig entrichtet hat, andernfalls  von der Abgabenbehörde eine schuldhafte Pflichtverletzung angenommen werden darf (vgl.  VwGH 16.12.2009, 2009/15/0127).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 82** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_190`)


Wird eine Abgabe nicht entrichtet, weil der Vertretene überhaupt keine liquiden Mittel hat, so  verletzt der Vertreter dadurch keine abgabenrechtliche Pflicht (VwGH 20.9.1996, 94/17/0420;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 83** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_191`)


VwGH 28.5.2008, 2006/15/0089).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 84** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_192`)


Der Geschäftsführer haftet für nicht entrichtete Abgaben der Gesellschaft auch dann, wenn die  Mittel, die ihm für die Entrichtung aller Verbindlichkeiten zur Verfügung gestanden sind, hierzu  nicht ausreichen; es sei denn, er weist nach, dass er diese Mittel anteilig für die Begleichung  aller Verbindlichkeiten verwendet, die Abgabenschulden daher im Verhältnis nicht schlechter  behandelt hat als andere Verbindlichkeiten (VwGH 19.5.2015, 2013/16/0016).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 85** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_195`)


Am Bf., dem als Geschäftsführer der Primärschuldnerin ausreichend Einblick in die Gebarung  zustand, war es gelegen, das Ausmaß der quantitativen Unzulänglichkeit der in den  Fälligkeitszeitpunkten der Abgaben zur Verfügung stehenden Mittel nachzuweisen (VwGH  19.11.1998, 97/15/0115), da nicht die Abgabenbehörde das Ausreichen der Mittel zur  Abgabenentrichtung nachzuweisen hat, sondern der zur Haftung herangezogene  Geschäftsführer das Fehlen ausreichender Mittel (VwGH 23.4.1998, 95/15/0145).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 86** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_197`)


Tritt der Vertreter diesen  Nachweis nicht an, dann kann ihm die uneinbringliche Abgabe zur Gänze vorgeschrieben  werden (VwGH 28.9.2004, 2001/14/0176).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 87** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 88** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_199`)


VwGH 2.7.2015, 2013/16/0220;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 89** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_200`)


VwGH 24.1.2013, 2012/16/0100), womit dieser  klarstellte, dass eine Betrachtung der Gläubigergleichbehandlung zum jeweiligen  Fälligkeitszeitpunkt zu erfolgen hatte, wurde mit dem Erkenntnis vom 28.6.2022, Ra  2020/13/0067, aufgegeben:  "Dabei kommt es für den Nachweis der Gläubigergleichbehandlung nicht nur auf die  liquiden Mittel zum Fälligkeitstag an, die den an diesem einen Tag jeweilig fälligen  Verbindlichkeiten gegenüberzustellen sind, weil eine derartige Betrachtung für nur einen  einzigen Tag im Monat ohne Berücksichtigung der vorhandenen liquiden Mittel für die  Zeiträume nach der Fälligkeit der Abgaben keinen Nachweis über eine  Gläubigergleichbehandlung geben kann."

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 90** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_204`)


Erfüllung der vollen Abgabenverbindlichkeiten kommt eine Beschränkung der Haftung des Bf.  bloß auf einen Teil der von der Haftung betroffenen Abgabenschulden nicht in Betracht (VwGH  21.1.1991, 90/15/0055).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 91** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_205`)


Kausalität  Infolge der schuldhaften Pflichtverletzung durch den Bf. konnte die Abgabenbehörde nach der  Judikatur des Verwaltungsgerichtshofes (VwGH 17.5.2004, 2003/17/0134), auch davon  ausgehen, dass die Pflichtverletzung Ursache für die Uneinbringlichkeit der  haftungsgegenständlichen Abgaben war.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 92** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_208`)


Aus dem auf die  Hereinbringung der Abgabenschuld beim Haftenden gerichteten Besicherungszweck der  Haftungsnorm folgt, dass die Geltendmachung der Haftung in der Regel ermessenskonform ist,  wenn die betreffende Abgabe beim Primärschuldner uneinbringlich ist (VwGH  25.6.1990, 89/15/0067).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 93** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_209`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 94** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_210`)


VwGH 16.10.2014, Ro 2014/16/0066) ist dem Element der Zumutbarkeit der  Heranziehung eines Haftungspflichtigen angesichts langer verstrichener Zeit im Rahmen der  behördlichen Ermessensübung besondere Bedeutung beizumessen.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 95** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_219`)


Auf die ständige Rechtsprechung des Verwaltungsgerichtshofes wird hingewiesen,  wonach einer Beschwerdevorentscheidung sowie einem Vorlagebericht Vorhaltscharakter  zukommt (vgl. VwGH vom 29.1.2020, Ra 2019/13/0071, VwGH vom 30.6.2021, Ra  2021/15/0048).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 96** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_46`)


2. Der Säumniszuschlag ist eine „Sanktion eigener Art“ (zB VwGH 21.4.1983, 83/16/0016;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Amt für Betrugsbekämpfung`

**F1:** 0.015 | **Precision:** 0.667 | **Recall:** 0.008  

**Format:** `regex`  
**Description:**
Matches 'Amt für Betrugsbekämpfung' and its genitive form 'Amtes für Betrugsbekämpfung', including optional '(ABB)' suffix.

**Content:**
```
\bAmt(?:es)?\s+für\s+Betrugsbekämpfung(?:\s*\(ABB\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.667 | 0.008 | 0.015 | 3 | 2 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 2 | 1 | 134 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_1`)


IM NAMEN DER REPUBLIK   Das Bundesfinanzgericht hat durch den Richter Priv.-Doz. Quirin Januszis  in der Finanzstrafsache des  Jennifer Papenhagen, Bakk. techn. Bakk. phil., Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich, über die Beschwerde vom 17.12.2024 gegen den Bescheid des  Amtes für Betrugsbekämpfung als Finanzstrafbehörde vom 02. Dezember 2024 betreffend  Abweisung eines Zahlungserleichterungsansuchens, zu Recht erkannt:  I. Der Beschwerde wird gem. § 161 Abs. 1 FinStrG stattgegeben und der angefochtene Bescheid  dahingehend abgeändert, als dem Beschwerdeführer gem. § 172 Abs. 1 FinStrG iVm § 212 Abs.  1 BAO zur Entrichtung des auf dem Strafkonto xxx derzeit mit insgesamt € 3.920,00  aushaftenden Rückstandes ab November 2025 monatliche Raten iHv jeweils € 200,00 gewährt  werden.

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)
- `Priv.-Doz. Quirin Januszis` (person)
- `Jennifer Papenhagen, Bakk. techn. Bakk. phil.` (person)
- `Sonderadresse 23.Bezirk 12, 9431 Kleinedling, Österreich` (address)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_6`)


Entscheidungsgründe  Verfahrensgang:  Mit Erkenntnis des Spruchsenates I-1 als Organ des Amtes für Betrugsbekämpfung als  Finanzstrafbehörde vom 2. Mai 2024 wurde der Beschwerdeführer (in der Folge kurz: Bf.) der  Finanzvergehen a) der Abgabenhinterziehung nach § 33 Abs. 2 lit. a FinStrG und b) der  Finanzordnungswidrigkeit nach § 49 Abs. 1 lit. a FinStrG für schuldig erkannt.

| Predicted | Gold |
|---|---|
| `Amtes für Betrugsbekämpfung` | `Amtes für Betrugsbekämpfung` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_12`)


Diesen Antrag vom 25.11.2024 hat das Amt für Betrugsbekämpfung mit Bescheid vom 02.  Dezember 2024 abgewiesen.

**False Positives:**

- `Amt für Betrugsbekämpfung` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bezirksgericht Entities`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches Bezirksgericht and its genitive form Bezirksgerichtes followed by a location name.

**Content:**
```
\bBezirksgericht(?:es)?\s+[A-Z][a-z]+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 234 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/134209.1`) (sent_id: `findok-manually-annotated_VALIDATE/134209.1_11`)


ihrem Ehemann nach meiner Einwilligung vor dem Bezirksgericht Purkersdorf - Protokoll Ri  Mag. P…, 1P… vom 25.02.2014 - im Sommer 2014 nach Worcester, Vereinigtes Königreich  gezogen.

| Predicted | Gold |
|---|---|
| `Bezirksgericht Purkersdorf` | `Bezirksgericht Purkersdorf` |

**Missed by this rule (FN):**

- `Worcester` (city)
- `Vereinigtes Königreich` (country)

</details>

---

## `ÖGK Acronym`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the acronym 'ÖGK' (Österreichische Gesundheitskasse).

**Content:**
```
\bÖGK\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 49 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_22`)


Der Kostenersatz der ÖGK sei auf der Rechnung ersichtlich,  weitere Ersatzleistungen habe es nicht gegeben.

| Predicted | Gold |
|---|---|
| `ÖGK` | `ÖGK` |

</details>

---

## `Pensionsversicherungsanstalt Entities`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches 'Pensionsversicherungsanstalt'.

**Content:**
```
\bPensionsversicherungsanstalt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 44 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_38`)


Die Ehefrau des Bf. bezieht im Streitjahr 2022  Einkünfte aus nichtselbständiger Arbeit (Pensionsversicherungsanstalt) in Höhe von  Euro 11.616,84.

| Predicted | Gold |
|---|---|
| `Pensionsversicherungsanstalt` | `Pensionsversicherungsanstalt` |

</details>

---

## `AG Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'AG', excluding single-letter prefixes like 'F' and common articles.

**Content:**
```
(?<!Firma\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!Dem\s)(?<!Den\s)(?<!Des\s)(?<!Arbeitgeber\s)(?<!F\s)\b[A-Z][a-z0-9&+\-]*(?:\s+[A-Z][a-z0-9&+\-]*)*\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verlag Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Verlag' preceded by a capitalized word, generalizing 'Dorfcon-Verlag'.

**Content:**
```
\b[A-Z][a-zA-Z0-9&\-]*\s+Verlag\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Maschinenbau Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Maschinenbau' preceded by a capitalized word, generalizing 'Houdek Maschinenbau'.

**Content:**
```
\b[A-Z][a-zA-Z0-9]*\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Luftfahrt Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'Luftfahrt' preceded by a capitalized word, generalizing 'Schmeltz Luftfahrt'.

**Content:**
```
\b[A-Z][a-zA-Z0-9]*\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenbank General`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Raiffeisenbank followed by a location name and optional additional words (e.g., Bankstelle, Filiale) to catch full names like 'Raiffeisenbank Karnische Rion Bankstelle St.Stefan'. Updated to be more inclusive of suffixes.

**Content:**
```
\bRaiffeisenbank\s+(?:[A-Z][a-z0-9\-]+\s+)*[A-Z][a-z0-9\-]+(?:\s+(?:Bankstelle|Filiale|Niederlassung|Zweigstelle)\s+[A-Z][a-z0-9\-]+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Technik Valseekel GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Technik Valseekel GMBH' to prevent partial matching by generic GMBH rules.

**Content:**
```
\bTechnik\s+Valseekel\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fachhochschule Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Fachhochschule Wiener Neustadt and FH Wiener Neustadt variations.

**Content:**
```
\b(?:Fachhochschule\s+Wiener\s+Neustadt|FH\s+Wiener\s+Neustadt)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FH Campus Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches FH Campus Wien specifically.

**Content:**
```
\bFH\s+Campus\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministeriums für Finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific government ministry name.

**Content:**
```
\bBundesministeriums\s+für\s+Finanzen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wirtschaft und Technik GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Wirtschaft und Technik GmbH' to prevent partial matching by generic GmbH rules.

**Content:**
```
\bWirtschaft\s+und\s+Technik\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Paugger Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Paugger Steuerberatung GmbH'.

**Content:**
```
\bPaugger\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `COFAG Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches COFAG and Cofag variations, excluding cases where it is part of a compound word like COFAG-NoAG.

**Content:**
```
\b(?:COFAG|Cofag)\b(?!-)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BHAG Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific acronym BHAG (Bundesheer- und Heeresverwaltungsgesetz? No, likely Bundesheer-AG or similar, but in legal context it's an org).

**Content:**
```
\bBHAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FAÖ Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAÖ' for Finanzamt Österreich.

**Content:**
```
\bFAÖ\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FAG Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'FAG' for Finanzamt für Großbetriebe.

**Content:**
```
\bFAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Deloitte Tax Wirtschaftsprüfungs GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Deloitte Tax Wirtschaftsprüfungs GmbH' to prevent partial matching.

**Content:**
```
\bDeloitte\s+Tax\s+Wirtschaftsprüfungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesheer Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesheer' (Federal Army) and its genitive form 'Bundesheeres'.

**Content:**
```
\bBundesheer(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `IT Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'IT' preceded by a capitalized word, generalizing 'Lexdon IT'.

**Content:**
```
\b[A-Z][a-zA-Z0-9]*\s+IT\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AMS Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'AMS Österreich' and 'Arbeitsmarktservice (AMS)' variations.

**Content:**
```
\b(?:Arbeitsmarktservice\s+\(AMS\)|AMS\s+Österreich)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landesgericht Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Landesgericht and its genitive form Landesgerichtes followed by a location name.

**Content:**
```
\bLandesgericht(?:es)?\s+[A-Z][a-z]+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `LG Acronym Court`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym LG followed by a location or specific court identifier like 'für ZRS Wien'.

**Content:**
```
\bLG\s+(?:für\s+ZRS\s+Wien|[A-Z][a-z]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BG Acronym Court`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym BG followed by a location or full court name.

**Content:**
```
\bBG\s+(?:Bezirksgericht\s+[A-Z][a-z]+|[A-Z][a-z]+)\b
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
Matches Bundesministeriums für Justiz (genitive) and Bundesministerium für Justiz (nominative).

**Content:**
```
\bBundesministerium(?:s)?\s+für\s+Justiz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BKS Steuerberatung GmbH & Co KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'BKS Steuerberatung GmbH & Co KG' to prevent partial matching.

**Content:**
```
\bBKS\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Eckhardt SteuerberatungsgmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Eckhardt SteuerberatungsgmbH'.

**Content:**
```
\bEckhardt\s+SteuerberatungsgmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mag. Ghesla Steuerberater GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Mag. Ghesla Steuerberater GmbH'.

**Content:**
```
\bMag\.\s+Ghesla\s+Steuerberater\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Eidgenössischen Invalidenversicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Eidgenössischen Invalidenversicherung' including hyphenated variations and the optional '(IV)' suffix.

**Content:**
```
\bEidgenössischen\s+Invalidenver-?sicherung\s*(?:\(IV\))?\b
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
**Description:**
Matches 'Schweizerischen Unfallversicherungsanstalt' including hyphenated variations and the optional '(SUVA)' suffix as a single entity.

**Content:**
```
\bSchweizeri-?sch(en)?\s+Unfallversicherungsanstalt\s*(?:\(SUVA\))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Bregenz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Bregenz' and 'Finanzamtes Bregenz'.

**Content:**
```
\bFinanzamt(?:es)?\s+Bregenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GmbH Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'GmbH' or 'GmbH & Co KG', excluding single-letter prefixes like 'F' and common articles, and preventing capture of preceding genitive nouns. Updated to include 'Arbeitgebers' and 'des' in lookbehind.

**Content:**
```
(?<!\w)(?<!der\s)(?<!die\s)(?<!das\s)(?<!Dem\s)(?<!Den\s)(?<!Des\s)(?<!Arbeitgebers\s)(?<!Arbeitgeber\s)(?<!Firma\s)\b[A-Z][a-z0-9&+\-]*(?:\s+[A-Z][a-z0-9&+\-]*)*\s+GmbH(?:\s+&\s+Co\s+KG)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 2 | 0 | 2 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 2 | 108 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_2`)


Wirtschaftsprüfung Steuerberatung  GmbH, Franz Josefskai 53/2/10, 1010 Wien, über die Beschwerde vom 14. November 2016  gegen den Bescheid des Finanzamtes Wien 9/18/19 Klosterneuburg vom 19. Oktober 2016  betreffend Einkommensteuer für die Jahre 2012, 2013 und 2014, Steuernummer  94-300/0486, zu Recht erkannt:   I. Der Beschwerde wird gemäß § 279 BAO Folge gegeben.

**False Positives:**

- `Steuerberatung  GmbH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Franz Josefskai 53/2/10, 1010 Wien`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `94-300/0486`(tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Dr.in Estelle Niederholz  in der Beschwerdesache Hon.-Prof.in OStR Tosca Knoller,  Holzplatzgasse 34, 5602 Schwaighof, Österreich, vertreten durch Anwälte Mandl & Mitterbauer GmbH, Wiesnerstraße 2, 4950  Altheim, über die Beschwerde vom 26. März 2025 gegen den Bescheid des Finanzamtes  Österreich vom 12. März 2025 über die Festsetzung von  Anspruchszinsen (§ 205 BAO) 2021  Steuernummer 01-700/4800  zu Recht erkannt:   I. Die Beschwerde wird gemäß § 279 BAO als unbegründet abgewiesen.

**False Positives:**

- `Mitterbauer GmbH` — partial — pred is substring of gold: `Anwälte Mandl & Mitterbauer GmbH`

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

## `SUVA Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the standalone acronym 'SUVA' (Schweizerische Unfallversicherungsanstalt) which appears frequently in legal texts.

**Content:**
```
\bSUVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Steueramt Luzern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Steueramtes des Kantons Luzern' (genitive) and 'Steueramt des Kantons Luzern' (nominative).

**Content:**
```
\bSteueramt(?:es)?\s+des\s+Kantons\s+Luzern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kantonsspital St. Gallen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Kantonsspitals St. Gallen' (genitive) and 'Kantonsspital St. Gallen' (nominative).

**Content:**
```
\bKantonsspital(?:s)?\s+St\.\s+Gallen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SüdVersand`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'SüdVersand'.

**Content:**
```
\bSüdVersand\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TraunLuftfahrt Solutions`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'TraunLuftfahrt Solutions' and variations with 'GmbH & Co KG' to prevent partial matching.

**Content:**
```
\bTraunLuftfahrt\s+Solutions(?:\s+GmbH\s+&\s+Co\s+KG)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Frontex and Border Agency Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Frontex, Europäische Grenzschutzagentur Frontex, and their variations including genitive forms and spacing variations.

**Content:**
```
\b(?:Europ(?:ä|e)ischen?\s+Grenzschutzagentur\s+Frontex|Frontex)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ministry of Interior Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'BM für Inneres', 'BMI', and 'Bundesministerium für Inneres' variations.

**Content:**
```
\b(?:BM\s+f\u00fcr\s+Inneres|BMI|Bundesministerium\s+f\u00fcr\s+Inneres)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Criminal Police Austria`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `EASO and OECD Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronyms EASO and OECD.

**Content:**
```
\b(?:EASO|OECD)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Flughafen München`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Flughafen München' specifically.

**Content:**
```
\bFlughafen\s+M\u00fcnchen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `INET Internet Service GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'INET Internet Service GmbH' specifically to prevent partial matching by generic GmbH rules.

**Content:**
```
\bINET\s+Internet\s+Service\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `INET System Informations GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'INET System Informations GmbH' specifically to prevent partial matching by generic GmbH rules.

**Content:**
```
\bINET\s+System\s+Informations\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Neunkirchen Wiener Neustadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Neunkirchen Wiener Neustadt' and 'Finanzamts Neunkirchen Wiener Neustadt'.

**Content:**
```
\bFinanzamt(?:s)?\s+Neunkirchen\s+Wiener\s+Neustadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Neunkirchen Wr. Neustadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Neunkirchen Wr. Neustadt' and 'Finanzamtes Neunkirchen Wr. Neustadt' (genitive).

**Content:**
```
\bFinanzamt(?:es)?\s+Neunkirchen\s+Wr\.\s+Neustadt\b
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
**Description:**
Matches the acronym 'UFS' (Unabhängiger Finanzsenat) as a standalone entity.

**Content:**
```
\bUFS\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 8 | 0 | 8 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 8 | 185 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_49`)


 Beispieldarstellung Übereinstimmung Lehrplan WU mit JKU:     Berufungsentscheidung des UFS vom 19.10.2010, RV/0180-L/10  9.

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `WU`(organisation)
- `JKU`(organisation)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_130`)


Allerdings ist durch die mit Einführung des UG 2002 erreichte Autonomie der Universitäten –  und damit verbunden die jeder Einrichtung mögliche individuelle Gestaltung der Studien – bei  einem Wechsel der Studieneinrichtung auch bei gleichbleibender Studienrichtung nicht in  jedem Fall eine Gleichwertigkeit gegeben (UFS 02.11.2011, RV/0289-F/11  (Hebenstreit/Lenneis/Reinalter in Lenneis/Wanke, FLAG2 § 2 Rz 96).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_134`)


UFS 19.10.2010, RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_143`)


Die Gewährung der Familienbeihilfe  für volljährige Kinder stellt nach den näheren Regelungen des § 2 Abs. 1 lit. b FLAG ersichtlich  darauf ab, dass sich das Kind einer Berufsausbildung mit dem ernstlichen und zielstrebigen,  nach außen erkennbaren Bemühen um den Ausbildungserfolg unterzieht (UFS 19.10.2010,  RV/0180-L/10).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_156`)


In allen Fällen von Studienortwechseln bezüglich Rechtswissenschaften hat das  Bundesfinanzgericht – soweit ersichtlich – einen Studienwechsel verneint und ist ebenfalls von  einem „bloßen“ Studienortwechsel, welcher nicht zu einem Studienwechsel führte,  ausgegangen und dies teilweise trotz abweichenden Studienaufbaus (2 bzw. 3  Studienabschnitte), da der Studieninhalt im Wesentlichen, im Kernbereich, deckungsgleich war  (UFS 19.10.2010, RV/0180-L/10;

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_164`)


vgl. auch UFS  16.02.2007, RV/0189-G/06).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_26`)


Von einer Liebhabereitätigkeit kann ja wohl nur dann gesprochen werden, wenn jemand,  dessen Hauptberuf sich von seinem Hobby, dem er aus besonderer Neigung nachgeht (siehe  UFS 27.11.2003, RV/0509-L/02), unterscheidet, und dieses Hobby zu steuerlich unbeachtlichen  Gesamtverlusten führt.

**False Positives:**

- `UFS` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `UFS/BFG Compound`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific compound acronym 'UFS/BFG' as a single entity.

**Content:**
```
\bUFS/BFG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `How to spend it Verlag GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'How to spend it Verlag GmbH' to prevent partial matching.

**Content:**
```
\bHow to spend it Verlag GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzpolizei Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzpolizei' followed by a location name (e.g., Finanzpolizei Feldkirch).

**Content:**
```
\bFinanzpolizei\s+[A-Z][a-z]+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Rechtsanwälte OG Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches law firm names ending in 'Rechtsanwälte' including slash-separated names and 'OG' suffixes. Tightened to require at least two capitalized words or a slash before 'Rechtsanwälte' to reduce false positives on partial names.

**Content:**
```
\b[A-Z][a-z0-9&/\s]+(?:\s+[A-Z][a-z0-9&/\s]+)*\s+Rechtsanwälte(?:\s+OG)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BFH Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'BFH' (Bundesfinanzgericht) which is the German Federal Fiscal Court.

**Content:**
```
\bBFH\b
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
Matches 'London Film Academy' and the common misspelling 'London Film Acadamy', including variations with extra spaces.

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

## `Bundeskanzleramtes`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundeskanzleramt' and its genitive form 'Bundeskanzleramtes'.

**Content:**
```
\bBundeskanzleramt(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `VfGH Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'VfGH' (Verwaltungsgerichtshof) which was missing.

**Content:**
```
\bVfGH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GmbH Extended Names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches GmbH names that continue with a dash and additional descriptive text (e.g., 'GmbH - Wirtschaftsprüfungs...').

**Content:**
```
\b[A-Z][a-z0-9&+\-]*(?:\s+[A-Z][a-z0-9&+\-]*)*\s+GmbH\s+-\s+[A-Z][a-z0-9&+\-\s]*
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Reinemut + Smoch Handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Reinemut + Smoch Handel'.

**Content:**
```
\bReinemut\s+\+\s+Smoch\s+Handel\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'HPS Hergovits, Pinkel & Schnabl Steuerberatungs GmbH' to prevent partial matching by generic GmbH rules.

**Content:**
```
\bHPS\s+Hergovits,\s+Pinkel\s+&\s+Schnabl\s+Steuerberatungs\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Zollamt Österreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Zollamt Österreich' and 'Zollamtes Österreich' (genitive).

**Content:**
```
\bZollamt(?:es)?\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `HLF Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Höheren Lehranstalt für Tourismus...' and 'HLF Krems/Donau' variations, handling genitive 'Höheren' and flexible spacing.

**Content:**
```
\b(?:Höheren\s+Lehranstalt\s+für\s+Tourismus,\s+Eventmanagement,\s+Sport\s+und\s+Freizeit|HLF\s+Krems/Donau)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verfassungsgerichtshof Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Verfassungsgerichtshof' and its genitive forms 'Verfassungsgerichtshofes', 'Verfassungsgerichtshofs'.

**Content:**
```
\bVerfassungsgerichtshof(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FH Kärnten Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FH Kärnten' specifically.

**Content:**
```
\bFH\s+Kärnten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fachhochschule Kärnten Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Fachhochschule Kärnten' specifically.

**Content:**
```
\bFachhochschule\s+Kärnten\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Karl-Franzens-Universität Graz Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Karl-Franzens- Universität Graz' with flexible spacing around the hyphen.

**Content:**
```
\bKarl-Franzens-?\s+Universität\s+Graz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `TAXCOACH Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'TAXCOACH Wirtschaftsprüfung und Steuerberatung GmbH & Co KG' handling variable whitespace.

**Content:**
```
\bTAXCOACH\s+Wirtschaftsprüfung\s+und\s+Steuerberatung\s+GmbH\s+&\s+Co\s+KG\b
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
**Description:**
Matches 'Merkur Treuhand Steuerberatung' and 'Merkur Treuhand Steuerberatung GmbH' to handle both base and full names.

**Content:**
```
\bMerkur\s+Treuhand\s+Steuerberatung(?:\s+GmbH)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schabetsberger Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Schabetsberger Steuerberatung GmbH' to prevent partial matching by generic GmbH rules.

**Content:**
```
\bSchabetsberger\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `UFS Salzburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'UFS Salzburg' to capture the full name including the location.

**Content:**
```
\bUFS\s+Salzburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Merkur Steuerberatung GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Merkur Steuerberatung GmbH' to prevent partial matching by generic GmbH rules.

**Content:**
```
\bMerkur\s+Steuerberatung\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GmbH Partner KG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in 'GmbH & Partner KG' to handle variations like 'Grazer Treuhand Steuerberatung GmbH & Partner KG'.

**Content:**
```
\b[A-Z][a-z0-9&+\-]*(?:\s+[A-Z][a-z0-9&+\-]*)*\s+GmbH\s+&\s+Partner\s+KG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Rhein Normonkel Manufaktur GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Rhein Normonkel Manufaktur GMBH' to prevent partial matching and ensure all-caps words are handled.

**Content:**
```
\bRhein\s+Normonkel\s+Manufaktur\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BDO Austria GmbH Full Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific long company name 'BDO Austria GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft' to prevent partial matching.

**Content:**
```
\bBDO\s+Austria\s+GmbH\s+Wirtschaftsprüfungs-\s+und\s+Steuerberatungsgesellschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `F Personalservice GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'F Personalservice GmbH' including trailing punctuation and variable whitespace.

**Content:**
```
\bF\s+Personalservice\s+GmbH\.?
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Raiffeisenbank Wels Süd Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Raiffeisenbank Wels Süd' to prevent truncation by the generic rule.

**Content:**
```
\bRaiffeisenbank\s+Wels\s+Süd\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landespolizeidirektion Tirol Typo`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific typo 'Landespolizeidirketion Tirol' found in training data.

**Content:**
```
\bLandespolizeidirketion\s+Tirol\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Henken Organization`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Henken' as an organization (likely a firm or party name in legal context).

**Content:**
```
\bHenken\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesamt für Soziales und Behindertenwesen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full organization name 'Bundesamt für Soziales und Behindertenwesen' and its genitive form 'Bundesamts für Soziales und Behindertenwesen'.

**Content:**
```
\bBundesamts?\s+f\u00fcr\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Arbeits- und Sozialgericht`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

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
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Retail Chains Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific retail chains found in training data: Ikea, Obi, Leiner, Möbelix, MömaX, Otto.de, xxxLutz, Quelle.at.

**Content:**
```
\b(?:Ikea|Obi|Leiner|Möbelix|MömaX|Otto\.de|xxxLutz|Quelle\.at)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiederspan Beratung GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Wiederspan Beratung GMBH'.

**Content:**
```
\bWiederspan\s+Beratung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Mur Alver OG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Mur Alver OG'.

**Content:**
```
\bMur\s+Alver\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `PVA Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'PVA' (Public Health Insurance) as a standalone entity.

**Content:**
```
\bPVA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SVS SVB Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'SVS/SVB' (Social Insurance) as a standalone entity.

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

## `PSD Wien Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches PSD Wien variations including the full 'Ambulatorium Landstraße' name and the standalone 'PSD Wien'.

**Content:**
```
\b(?:PSD\s+Wien\s+Ambulatorium\s+Landstraße|PSD\s+Wien)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Sozialversicherung Bauern Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Sozialversicherungsanstalt der Bauern' and 'Sozialversicherung der Bauern'.

**Content:**
```
\bSozialversicherung(?:sanstalt)?\s+der\s+Bauern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Psychiatrie Otto Wagner Spital Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Psychiatrie Otto Wagner Spital' including the trailing hyphen variant found in training data.

**Content:**
```
\bPsychiatrie\s+Otto\s+Wagner\s+Spital(?:-)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministers für Arbeit, Soziales und Konsumentenschutz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministers für Arbeit, Soziales und Konsumentenschutz' (genitive) and 'Bundesministerium für Arbeit, Soziales und Konsumentenschutz' (nominative).

**Content:**
```
\bBundesminister(?:ium)?s?\s+für\s+Arbeit,\s+Soziales\s+und\s+Konsumentenschutz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm 'Tschurtschenthaler, Walder, Fister Rechtsanwälte GmbH' to prevent partial matching by generic rules.

**Content:**
```
\bTschurtschenthaler,\s+Walder,\s+Fister\s+Rechtsanwälte\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Magistrat der Stadt Klagenfurt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Magistrat der Stadt Klagenfurt' and its genitive form 'Magistrats der Stadt Klagenfurt'.

**Content:**
```
\bMagistrat(?:s)?\s+der\s+Stadt\s+Klagenfurt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministeriums für Inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerium für Inneres' and its genitive form 'Bundesministeriums für Inneres'.

**Content:**
```
\bBundesministerium(?:s)?\s+für\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Immobilienbüro Mandl`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Immobilienbüro Mandl'.

**Content:**
```
\bImmobilienbüro\s+Mandl\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Österreichischen Gesundheitskasse`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Österreichischen Gesundheitskasse' and its genitive form 'Österreichischen Gesundheitskasse' variations.

**Content:**
```
\bÖsterreichischen\s+Gesundheitskasse\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Klein-Vorholt KI GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Klein-Vorholt KI GMBH' to prevent partial matching by generic GMBH rules.

**Content:**
```
\bKlein\-Vorholt\s+KI\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gogel Daten GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Gogel Daten GMBH' to prevent partial matching by generic GMBH rules.

**Content:**
```
\bGogel\s+Daten\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `InnMarine GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'InnMarine GMBH' to ensure it is captured even if generic rules fail due to case sensitivity or lookbehind issues.

**Content:**
```
\bInnMarine\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Fensudlog GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Fensudlog GMBH' to ensure it is captured.

**Content:**
```
\bFensudlog\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Luehrig + Hundertmarck Holz GMBH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'Luehrig + Hundertmarck Holz GMBH' to ensure it is captured.

**Content:**
```
\bLuehrig\s+\+\s+Hundertmarck\s+Holz\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministerin für Finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Bundesministerin für Finanzen' (feminine form of the ministry).

**Content:**
```
\bBundesministerin\s+f\u00fcr\s+Finanzen\b
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
**Description:**
Matches the specific company 'KQPC Versand GMBH' to prevent partial matching by generic GmbH rules.

**Content:**
```
\bKQPC\s+Versand\s+GMBH\b
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
**Description:**
Matches the specific company 'Event Sudkraftlex GMBH' to prevent partial matching by generic GmbH rules.

**Content:**
```
\bEvent\s+Sudkraftlex\s+GMBH\b
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
**Description:**
Matches the specific company 'Sudver Handel Services GMBH' to prevent partial matching by generic GmbH rules.

**Content:**
```
\bSudver\s+Handel\s+Services\s+GMBH\b
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
**Description:**
Matches the specific company 'Glanznorost Institut GMBH' to prevent partial matching by generic GmbH rules.

**Content:**
```
\bGlanznorost\s+Institut\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Erste Bank Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific bank name 'Erste Bank' found in legal texts.

**Content:**
```
\bErste\s+Bank\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WKO Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the acronym 'WKO' (Wirtschaftskammer Österreich) as a standalone entity.

**Content:**
```
\bWKO\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bezirkshauptmannschaft Bludenz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Bezirkshauptmannschaft Bludenz' found in training data.

**Content:**
```
\bBezirkshauptmannschaft\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SENECURA`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company 'SENECURA' found in training data.

**Content:**
```
\bSENECURA\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SeneCura Family Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches SeneCura and its variations (SENECURA, Senecura, SeneCura Laurentius-Park Bludenz, etc.) with flexible spacing and hyphenation.

**Content:**
```
\b(?:S(?:ene(?:Cura(?:\s+Laurentius[\-\s]Park\s+Bludenz|\s+Laurentius\s+Park|\s+Park)|cura)|ENECURA)|Senecura)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ÖBB Acronym`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Austrian Federal Railways acronym 'ÖBB'.

**Content:**
```
\bÖBB\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Krankenpflegevereins Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Krankenpflegevereins' followed by a location name (e.g., Bludenz), handling variable whitespace.

**Content:**
```
\bKrankenpflegevereins\s+[A-Z][a-z]+\b
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

