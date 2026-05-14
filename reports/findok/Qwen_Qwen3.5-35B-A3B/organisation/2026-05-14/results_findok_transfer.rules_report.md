# Rule Evaluation Report — Qwen/Qwen3.5-35B-A3B (manual_findok)

Generated on: 2026-05-14T08:32:03.896318

---

<details>
<summary>Configuration</summary>

Results can be reproduced by running this command: 
```
 python benchmark.py --config reports/findok/Qwen_Qwen3.5-35B-A3B/organisation/2026-05-14/config.yaml 
```
| Parameter | Value |
|---|---|
| Pool size | None |
| Train ratio | 0.80 |
| Validation ratio | 0.20 |
| Shots per class | None |
| Training documents | 476 |
| Validation documents | 121 |
| Test documents | 1247 |
| Train sentences | 2257 |
| Validation sentences | 711 |
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
| Batch size | 50 |
| Refine per batch | 1 |
| Manually annotated examples | 0 |
| First batch with manual data | None |

</details>

---

**Transfer Learning**

| Property | Value |
|---|---|
| Seeded From | findok |
| Seed Rule Count | 39 |
| New Rules Added | 118 |
| Continuation | synthesize_and_refine |
| Phase1 Train Sentences | 1171 |
| Phase1 Eval Sentences | 213 |
| Transfer Train Sentences | 1086 |
| Transfer Eval Sentences | 498 |

<details>
<summary>Results</summary>

| Metric | Value |
|---|---|
| Accuracy (exact match) | 86.0% |
| True Positives | 172 |
| False Positives | 135 |
| False Negatives | 84 |
| Total Gold Entities | 256 |
| Micro Precision | 56.0% |
| Micro Recall | 67.2% |
| Micro F1 | 61.1% |
| Macro F1 | 61.1% |

</details>

---

<details>
<summary>📊 Summary</summary>

| Rule | F1 | Precision | Recall | Total Predicted | True Positives | False Positives |
|---|---|---|---|---|---|---|
| `Magistrat der Stadt Wien Entities` | 4.6% | 100.0% | 2.3% | 6 | 6 | 0 |
| `Landespolizeidirektion Wien Entities` | 3.1% | 100.0% | 1.6% | 4 | 4 | 0 |
| `Bundesfinanzgericht Entities` | 43.4% | 100.0% | 27.7% | 71 | 71 | 0 |
| `Finanzamt Österreich Nominative` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `ÖGK` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `Finanzamt Österreich` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `Finanzamt and Related Entities` | 2.3% | 100.0% | 1.2% | 3 | 3 | 0 |
| `Pensionsversicherungsanstalt` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `Bundesfinanzgerichts` | 0.8% | 100.0% | 0.4% | 1 | 1 | 0 |
| `Verwaltungsgerichtshof Entities` | 38.6% | 95.4% | 24.2% | 65 | 62 | 3 |
| `Finanzamt Österreich Entities` | 6.0% | 88.9% | 3.1% | 9 | 8 | 1 |
| `Finanzamt Österreich Variants` | 6.0% | 88.9% | 3.1% | 9 | 8 | 1 |
| `Magistrat der Stadt` | 3.1% | 80.0% | 1.6% | 5 | 4 | 1 |
| `BFG Abbreviation` | 8.8% | 70.6% | 4.7% | 17 | 12 | 5 |
| `Wirtschaftsuniversität Wien` | 3.1% | 66.7% | 1.6% | 6 | 4 | 2 |
| `VwGH Contextual` | 2.4% | 4.8% | 1.6% | 83 | 4 | 79 |
| `VwGH Abbreviation` | 2.2% | 3.4% | 1.6% | 116 | 4 | 112 |
| `Specific Private Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Names (No Suffix)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Names (With Suffix)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Reinemut Smoch Handel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Salzburg-Stadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Salzburg-Stadt URL` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Triloglex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company MittelHeizung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Rosilius` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Yavasoglu` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity Zoruniglanz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Entity Sophie Wittmeir` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Klusner` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Tschermack` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company TalVerverwerk` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company SudLandwirtschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Compound Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Bank and Other Companies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Legal Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific IT Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Verlag Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Maschinenbau Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Luftfahrt Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Finanzamt Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Named Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Company Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific Trade Names (No Suffix)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `GmbH & Partner KG Pattern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `WaldTouristik Technologies` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Legal Case Organization Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bank and Institute Names` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific GMBH Names with Special Chars` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Two-Word Company Names (Marine/Wind)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `UnterRecycling Services GMBH Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BMF Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bezirkshauptmannschaft Bludenz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PVA Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SeneCura Laurentius-Park Bludenz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SENECURA Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `ÖBB Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Krankenpflegevereins Bludenz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BFH Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steuerberater OG Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiederspan and Mur Alver Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Henken Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Retail Chain Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `London Film Academy Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundeskanzleramt Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Innsbruck Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Schwechat Gerasdorf Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Deloitte Tax Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ernst & Young Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Technik Valseekel Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Städtische Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Allianz Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Wien 1/23 Entity` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `VfGH Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Wiener Städtische Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `KG Company Suffix` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Innsbruck` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Landespolizeidirketion Tirol` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Arbeits- und Sozialgericht Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Ernst & Young Steuerberatungs-GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verfassungsgerichtshof` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Waldviertel` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `F Personalservice GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `F Personal GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BDO Austria GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA Klosterneuburg` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Universität St. Gallen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verwaltungsgericht Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SUVA` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FA and UFS Abbreviations` | 0.0% | 0.0% | 0.0% | 8 | 0 | 8 |
| `BFG with Location` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Versorgungskasse Deutscher Unternehmen VVaG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Pensionsversicherungsanstalt Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Deutschen Rentenversicherung Bund` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schweizerischen Unfallversicherungsanstalt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Europäische Grenzschutzagentur Frontex` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM für Inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Kriminalpolizei in Österreich` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministerium für Inneres` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministeriums für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BM für Finanzen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Flughafen München` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `OECD` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BMI Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Verfassungsgerichtshofes` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Gesellschaft Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `University Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FH Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fachhochschule Kärnten` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Karl-Franzens- Universität Graz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FAÖ Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `SVS/SVB Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Uni Wien Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Pädagogische Hochschule Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Sozialversicherung der Bauern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `PSD Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Psychiatrie Otto Wagner Spital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesministers für Arbeit, Soziales und Konsumentenschutz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesamtes für Soziales und Behindertenwesen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt City` | 0.0% | 0.0% | 0.0% | 2 | 0 | 2 |
| `Finanzpolizei City` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Immobilienbüro Name` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FAG Acronym` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt für Großbetriebe` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Specific GmbH Patterns` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bank and Chamber Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Federal Ministry Entities` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `LG Innsbruck and LG für ...` | 0.0% | 0.0% | 0.0% | 1 | 0 | 1 |
| `Bezirksgericht Silz` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Eckhardt SteuerberatungsgmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Fachhochschule Wiener Neustadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FH Campus Wien` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `FH Wiener Neustadt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Wien Specific` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `LAG Abbreviation` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesfinanzgericht (BFG)` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesfinanzgericht Compound` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `COFAG and Cofag` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `BHAG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `DA Deutsche Allgemeine Versicherung AG` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AVED cosmetic` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Yoga Vidya GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Geschenkartikel GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `AMS` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Bundesamt für Soziales und Behindertenwesen` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Mag. Ghesla Steuerberater GmbH` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Eidgenössischen Invalidenversicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Swiss Steueramt` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Swiss Kantonsspital` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Steueramt Luzern` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Finanzamt Braunau` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Schweizerische Unfallversicherung` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |
| `Raiffeisenbank Locations` | 0.0% | 0.0% | 0.0% | 0 | 0 | 0 |

</details>

---

<details>
<summary>🏆 Most Precise Rules</summary>

## `Bundesfinanzgericht Entities`

**F1:** 0.434 | **Precision:** 1.000 | **Recall:** 0.277  

**Format:** `regex`  
**Description:**
Matches the Federal Financial Court in various grammatical cases including genitive 's'.

**Content:**
```
\bBundesfinanzgericht(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.277 | 0.434 | 71 | 71 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 71 | 0 | 185 |

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

## `Magistrat der Stadt Wien Entities`

**F1:** 0.046 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches the Vienna City Administration (Magistrat) in various forms including genitive and departmental suffixes including - BA32.

**Content:**
```
\bMagistrat(?:es)?(?:\s+der\s+Stadt\s+Wien)(?:\s*,\s*(?:MA\s*67|Magistratsabteilung\s*6|Magistratsabteilung\s*67|MA\s*6|Magistratsabteilung\s*6\s*-\s*BA32))?\b
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
Matches the Administrative Court in nominative, genitive 'es', and genitive 's' forms.

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

## `Finanzamt Österreich Entities`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches the Austrian Tax Office in nominative and genitive cases.

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

## `Finanzamt Österreich Variants`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches Finanzamt Österreich and its genitive form Finanzamtes Österreich.

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

## `BFG Abbreviation`

**F1:** 0.088 | **Precision:** 0.706 | **Recall:** 0.047  

**Format:** `regex`  
**Description:**
Matches the abbreviation for the Federal Financial Court, excluding dates immediately following and excluding cases where it is part of the compound name '(BFG)'.

**Content:**
```
\bBFG\b(?![\s]*\d{1,2}\.\d{1,2}\.\d{2,4})(?!\s*\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.706 | 0.047 | 0.088 | 17 | 12 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 5 | 180 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_83`)


Mit Schreiben vom 21.8.2025, eingelangt am BFG am 22.8.2025, zog der steuerliche Vertreter  den Antrag auf mündliche Senatsverhandlung zurück.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_137`)


Entgegen der vom Finanzamt getroffenen Beurteilung vertritt das BFG die Auffassung, dass im  streitgegenständlichen Fall eine Betätigung im Sinne des § 1 Abs. 1 LVO vorliegt, weil das  künstlerische Tätigwerden des Bf. sich nicht im Rahmen einer typischen Betätigung im Sinne  des § 1 Abs. 2 Z 2 LVO bewegt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_138`)


Für eine typische erwerbswirtschaftliche Betätigung spricht nach Ansicht des BFG die  hauptberufliche Ausübung der musikalischen Tätigkeit auf Grundlage der gehobenen  musikalischen Ausbildung des Bf.  11 von 14 Seite 12 von 14

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_139`)


In Anbetracht von Art und Umfang der vom Bf. ausgeübten Tätigkeit ist nach Ansicht des BFG  insbesondere aus folgenden Gründen nicht von einer hobbymäßigen Betätigung auszugehen:   der Bf. ist akademisch ausgebildeter Musiker, d.h. er verfügt demnach über eine  entsprechende profunde und einschlägige Hochschulausbildung   er hat auf mehreren Musik-CD’s mitgewirkt   er hat mit namhaften Musikern zusammengearbeitet und trat mit Jazzgrößen auf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_144`)


In Anbetracht der Tatsache, dass der Bf. die in Rede stehende Tätigkeit 2014, aufgrund des  Rückganges der Aufträge und der Tatsache, dass es für ihn immer schwieriger wurde Aufträge  für Auftritte zu erhalten, durch seine betriebswirtschaftlich sinnvolle Entscheidung, beendet  hat und in dem gesamten Betätigungszeitraum (hier von 1975 bis 2014) ein Gesamtüberschuss  erwirtschaftet (laut BVE geht das Finanzamt nicht vom Vorliegen einer Gesamtverlustes über  den gesamten Tätigkeitszeitraum aus) wurde, kann laut Ansicht des BFG keine Liebhaberei  vorliegen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Österreich`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_41`)


Der Bf. erhob gegen das Straferkenntnis mit Anbringen vom 5. September 2025 (fristgerecht)  Beschwerde, führte aus wie im oben angeführten Einspruch gegen die Strafverfügung vom  30. Juni 2025 mit dem Ersuchen, die im Straferkenntnis festgelegte Geldstrafe in Höhe von  65,00 Euro [Anmerkung BFG, gemeint: Geldstrafe in Höhe von 55,00 Euro] herabzusetzen.

**False Positives:**

- `BFG` — partial — pred is substring of gold: `BFG,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG,`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Magistrat der Stadt Wien`(organisation)

</details>

---

</details>

---

<details>
<summary>💣 Least Precise Rules</summary>

## `VwGH Abbreviation`

**F1:** 0.022 | **Precision:** 0.034 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches the abbreviation for the Administrative Court (VwGH).

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

## `VwGH Contextual`

**F1:** 0.024 | **Precision:** 0.048 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches VwGH but excludes it when followed by a hyphen and a noun (e.g., VwGH-Rechtsprechung) or immediately by a date/citation number to avoid false positives in citations.

**Content:**
```
\bVwGH\b(?![\-\s]*[A-Z][a-zäöüÄÖÜß]+)(?!\s+\d{2}\.\d{2}\.\d{4})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.048 | 0.016 | 0.024 | 83 | 4 | 79 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 79 | 239 |

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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_41`)


Dazu zählen beispielsweise Erkrankungen, die die Berufsausbildung auf begrenzte Zeit  unterbrechen, oder Urlaube und Schulferien (VwGH vom 16.11.1993, 90/14/0108).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_44`)


Das bloße Aufrechterhalten eines  Berufswunsches ist der tatsächlichen Ausbildung nicht gleichzuhalten (VwGH 24.9.2009,  2009/16/0088, VwGH 21.01.2004, 2003/13/0157, VwGH 14.12.1995, 93/15/0133).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_167`)


Für die Überprüfung dieser  Frage erachte es der VwGH als ausreichend, die Unterscheidung auf die Kernfächer bzw. den  Kernbereich des Studiums zu reduzieren (VwGH 7.8.2001, 97/14/0068).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_44`)


Ebenso trifft es allerdings zu, dass der  Ruin der wirtschaftlichen Existenz des Bestraften den mit der Bestrafung verfolgten Zweck  auch nicht sinnvoll erreicht (vgl. VwGH 24.9.2003, 2003/13/0084, ÖStZ 2004/190, ÖStZB  2004/109).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `FA and UFS Abbreviations`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA' (Finanzamt) and 'UFS' (Unabhängiger Finanzsenat) as organizations.

**Content:**
```
\b(?:FA\s+(?:Wien\s+\d+/\d+|\w+\s+\d+/\d+)|UFS)\b
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

## `Wirtschaftsuniversität Wien`

**F1:** 0.031 | **Precision:** 0.667 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches the University of Economics and Business Vienna.

**Content:**
```
\bWirtschaftsuniversität\s+Wien\b
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

## `Specific Private Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that do not end in GmbH/AG/OG, such as SüdVersand and Raiffeisenbank. Updated to ensure strict boundaries.

**Content:**
```
\b(S\u00fcdVersand|Raiffeisenbank\s+Wels\s+S\u00fcd|TraunLuftfahrt\s+Solutions)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names (No Suffix)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that do not end in standard suffixes like GmbH/AG, based on training data.

**Content:**
```
\b(Textil\s+Steingartlog|Keltrizor\s+Handel|DLCG\s+Bildung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names (With Suffix)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that include 'GMBH' or 'GmbH' but have unique prefixes.

**Content:**
```
\b(Hudec&Christian\s+Immobilien\s+GMBH|Hendrick\s+Recycling\s+GMBH|Stefansky\s+Bau\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Reinemut Smoch Handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name 'Reinemut + Smoch Handel'.

**Content:**
```
Reinemut\s+\+\s+Smoch\s+Handel
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Salzburg-Stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Salzburg-Stadt' and 'FA Salzburg-Stadt' variations.

**Content:**
```
\b(?:Finanzamt|FA)\s+Salzburg\-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Salzburg-Stadt URL`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the URL variant 'www.FA Salzburg-Stadt'.

**Content:**
```
www\.FA\s+Salzburg\-Stadt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Triloglex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Triloglex GMBH.

**Content:**
```
\bTriloglex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company MittelHeizung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name MittelHeizung Werke AG.

**Content:**
```
\bMittelHeizung\s+Werke\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Rosilius`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Rosilius Pflege AG.

**Content:**
```
\bRosilius\s+Pflege\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Yavasoglu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Yavasoglu Analyse AG.

**Content:**
```
\bYavasoglu\s+Analyse\s+AG\b
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

**F1:** 0.434 | **Precision:** 1.000 | **Recall:** 0.277  

**Format:** `regex`  
**Description:**
Matches the Federal Financial Court in various grammatical cases including genitive 's'.

**Content:**
```
\bBundesfinanzgericht(?:es|s)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.277 | 0.434 | 71 | 71 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 71 | 0 | 185 |

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

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_84`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_93`)


Diese Sachverhaltsfeststellungen ergeben sich nach Dafürhalten des Bundesfinanzgerichts aus  den vorgelegten Akten des Abgabenverfahrens, dem Vorbringen der Bf. in seiner Beschwerde  sowie den Erhebungen durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_154`)


Der zitierten Rechtsprechung des Verwaltungsgerichtshofes ist nach Ansicht der Richterin des  Bundesfinanzgericht zu entnehmen, dass ein regelmäßiges Üben zum Erhalt der künstlerischen  Fähigkeiten bzw. des künstlerischen Niveaus als Bestandteil der Tätigkeit von Musikern mit  akademischer Ausbildung gehört und somit Aufwendungen für ein häusliches Arbeitszimmer  abzugsfähig sind.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_161`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_162`)


Hier handelt es sich um keine Rechtsfragen von grundsätzlicher Bedeutung, weil das  Bundesfinanzgericht in rechtlicher Hinsicht der in der Begründung dieser Entscheidung  dargestellten Judikatur des Verwaltungsgerichtshofes folgt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_1`)


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

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_20`)


Mit Schreiben vom 23.7.2025 stellte die steuerliche Vertretung den Antrag auf Entscheidung  über die Beschwerde (Vorlageantrag) durch das Bundesfinanzgericht betreffend den Bescheid  über Festsetzung von Anspruchszinsen für das Jahr 2021 vom 12.3.2025.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_21`)


Mit Vorlagebericht vom 8.10.2025 legte das Finanzamt die gegenständliche Beschwerde vom  25.3.2025 betreffend Festsetzung von Anspruchszinsen für das Jahr 2021 dem  Bundesfinanzgericht zur Entscheidung vor und beantragte die Abweisung im Wesentlichen wie  folgt:  „Sachverhalt:   Der Beschwerdeführer (Bf) brachte am 21.08.2023 die Einkommensteuererklärung für das Jahr  2021 ein.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_33`)


Bezüglich der Einkommensteuer sei bereits die Vorlage an das Bundesfinanzgericht  beantragt, eine Entscheidung dazu liege noch nicht vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_51`)


II. Das Bundesfinanzgericht hat erwogen:  1. Beweiswürdigung  Der vorstehende Verfahrensgang (Sachverhalt) ergibt sich aus dem gesamten Akteninhalt, dem  Vorlagebericht, den im Abgabeninformationssystem gespeicherten Daten und aus dem  Vorbringen der Parteien.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_74`)


sowie  zahlreiche Erkenntnisse des Bundesfinanzgerichtes).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_75`)


Wegen dieser Bindung ist der Zinsenbescheid nicht (mit Aussicht auf Erfolg) mit der  Begründung anfechtbar, der maßgebende Einkommensteuerbescheid sei inhaltlich  rechtswidrig (Ritz, BAO8, § 205 Tz 34 mit Hinweis auf die ständige Rechtsprechung des  Bundesfinanzgerichtes).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_89`)


(Hinweis: Es erging keine Vorlage der Beschwerde gegen  den Einkommensteuerbescheid 2021 an das Bundesfinanzgericht).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_93`)


2.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_94`)


Das Bundesfinanzgericht orientierte sich bei den zu lösenden Rechtsfragen an der zitierten  Judikatur des Verwaltungsgerichtshofes zu § 205 BAO.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


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

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_8`)


2. Beweiswürdigung  Die Feststellungen ergeben sich eindeutig aus dem Akt des Finanzamtes und des  Bundesfinanzgerichtes und sind unstrittig.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_16`)


Gegen einen Beschluss des Bundesfinanzgerichtes ist gemäß Art 133 Abs 4 Bundes- Verfassungsgesetz (B-VG) eine Revision zulässig, wenn sie von der Lösung einer Rechtsfrage  abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil der Beschluss von der  Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche Rechtsprechung fehlt  oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_1`)


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

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_24`)


Mit Eingabe vom 21. Mai 2024 beantragte der Bf. innerhalb verlängerter Frist die Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht sowie die Durchführung einer  mündlichen Verhandlung.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_26`)


Am 13. Juni 2024 legte die belangte Behörde die Beschwerde samt Verwaltungsakt dem  Bundesfinanzgericht zur Entscheidung vor.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_31`)


Am 1. Oktober 2025 fand die beantragte mündliche Verhandlung vor dem Bundesfinanzgericht  statt, in der insbesondere das Vorliegen bzw. Nichtvorliegen von triftigen medizinischen  Gründen diskutiert wurde.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_36`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   Der Bf. bezieht im Streitjahr 2022 Einkünfte aus nichtselbständiger Arbeit.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_63`)


Das Bundesfinanzgericht kommt aus den nachstehenden Gründen im Rahmen der freien  Beweiswürdigung zum Ergebnis, dass die nach der höchstgerichtlichen Rechtsprechung  geforderten triftigen medizinischen Gründe nicht vorliegen:  Zunächst steht unstrittig fest, dass in keinem öffentlichen Krankenhaus eine Terminanfrage  betreffend die Bandscheibenoperation der Ehefrau des Bf. gestellt wurde (vgl. Protokoll zur  Verhandlung vom 1. Oktober 2025 sowie Befundberichte vom 6. und 8. Oktober 2025).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_121`)


3.2. Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_122`)


Das Bundesfinanzgericht ist zum einen der im Erkenntnis angeführten ständigen  Rechtsprechung des Verwaltungsgerichtshofes gefolgt.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_1`)


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

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_137`)


Für den Fall, dass der Beschwerde im Zuge der Beschwerdevorentscheidung nicht Rechnung  getragen werde, werde die Vorlage der Beschwerde an das Bundesfinanzgericht  (Vorlageantrag gem. § 264 BAO).

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_157`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_224`)


Zu Spruchpunkt II. (Revision)  Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_1`)


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

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_14`)


Die Beschwerde sei nachweislich erst am 18.12.2024 vom  zuständigen Sachbearbeiter an das Bundesfinanzgericht vorgelegt worden.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_22`)


5. Am 3.4.2025 stellte der Bf. durch seine steuerliche Vertretung den Antrag auf Vorlage der  Beschwerde zur Entscheidung durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_23`)


6. Am 21.5.2025 legte das Finanzamt die Beschwerde dem Bundesfinanzgericht vor und  beantragte, die Beschwerde als unbegründet abzuweisen.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_25`)


II. Das Bundesfinanzgericht hat erwogen:  1. Sachverhalt   1.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_33`)


Diese Sachverhaltsfeststellungen erfolgen aufgrund der dem Bundesfinanzgericht  vorliegenden Akten des Finanzamtes.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgericht` | `Bundesfinanzgericht` |

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_105`)


Gegen ein Erkenntnis des Bundesfinanzgerichtes ist die Revision zulässig, wenn sie von der  Lösung einer Rechtsfrage abhängt, der grundsätzliche Bedeutung zukommt, insbesondere weil  das Erkenntnis von der Rechtsprechung des Verwaltungsgerichtshofes abweicht, eine solche  Rechtsprechung fehlt oder die zu lösende Rechtsfrage in der bisherigen Rechtsprechung des  Verwaltungsgerichtshofes nicht einheitlich beantwortet wird.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichtes` | `Bundesfinanzgerichtes` |

**Missed by this rule (FN):**

- `Verwaltungsgerichtshofes` (organisation)
- `Verwaltungsgerichtshofes` (organisation)

</details>

---

## `Verwaltungsgerichtshof Entities`

**F1:** 0.386 | **Precision:** 0.954 | **Recall:** 0.242  

**Format:** `regex`  
**Description:**
Matches the Administrative Court in nominative, genitive 'es', and genitive 's' forms.

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

## `BFG Abbreviation`

**F1:** 0.088 | **Precision:** 0.706 | **Recall:** 0.047  

**Format:** `regex`  
**Description:**
Matches the abbreviation for the Federal Financial Court, excluding dates immediately following and excluding cases where it is part of the compound name '(BFG)'.

**Content:**
```
\bBFG\b(?![\s]*\d{1,2}\.\d{1,2}\.\d{2,4})(?!\s*\))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.706 | 0.047 | 0.088 | 17 | 12 | 5 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 12 | 5 | 180 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_83`)


Mit Schreiben vom 21.8.2025, eingelangt am BFG am 22.8.2025, zog der steuerliche Vertreter  den Antrag auf mündliche Senatsverhandlung zurück.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_137`)


Entgegen der vom Finanzamt getroffenen Beurteilung vertritt das BFG die Auffassung, dass im  streitgegenständlichen Fall eine Betätigung im Sinne des § 1 Abs. 1 LVO vorliegt, weil das  künstlerische Tätigwerden des Bf. sich nicht im Rahmen einer typischen Betätigung im Sinne  des § 1 Abs. 2 Z 2 LVO bewegt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_138`)


Für eine typische erwerbswirtschaftliche Betätigung spricht nach Ansicht des BFG die  hauptberufliche Ausübung der musikalischen Tätigkeit auf Grundlage der gehobenen  musikalischen Ausbildung des Bf.  11 von 14 Seite 12 von 14

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_139`)


In Anbetracht von Art und Umfang der vom Bf. ausgeübten Tätigkeit ist nach Ansicht des BFG  insbesondere aus folgenden Gründen nicht von einer hobbymäßigen Betätigung auszugehen:   der Bf. ist akademisch ausgebildeter Musiker, d.h. er verfügt demnach über eine  entsprechende profunde und einschlägige Hochschulausbildung   er hat auf mehreren Musik-CD’s mitgewirkt   er hat mit namhaften Musikern zusammengearbeitet und trat mit Jazzgrößen auf.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_144`)


In Anbetracht der Tatsache, dass der Bf. die in Rede stehende Tätigkeit 2014, aufgrund des  Rückganges der Aufträge und der Tatsache, dass es für ihn immer schwieriger wurde Aufträge  für Auftritte zu erhalten, durch seine betriebswirtschaftlich sinnvolle Entscheidung, beendet  hat und in dem gesamten Betätigungszeitraum (hier von 1975 bis 2014) ein Gesamtüberschuss  erwirtschaftet (laut BVE geht das Finanzamt nicht vom Vorliegen einer Gesamtverlustes über  den gesamten Tätigkeitszeitraum aus) wurde, kann laut Ansicht des BFG keine Liebhaberei  vorliegen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_14`)


Der Antragsteller hat  daraufhin eine Entscheidung über diese Beschwerde durch einen Vorlageantrag an das BFG  beantragt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_27`)


Darüber wurde folgendermaßen entschieden:   - die Beschwerde gegen den ESt-Bescheid 2020 wurde mit Beschwerdevorentscheidung (BVE)  vom 12.3.2025 (Anm. laut BFG richtig: 11.03.2025) abgewiesen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_82`)


Der Antragsteller hat daraufhin eine Entscheidung über diese Beschwerde durch einen  Vorlageantrag an das BFG beantragt.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_84`)


Festgehalten wird, dass die vom Vertreter des Bf. genannte Beschwerdevorentscheidung vom  11.3.2025 nicht die Einkommensteuer für das Jahr 2021, sondern die Einkommensteuer für das  Jahr 2020 betrifft (Die Beschwerde gegen den Einkommensteuerbescheid 2020 wurde dem  BFG zur Entscheidung vorgelegt, die noch unerledigt ist, RV/5100771/2025).

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_155`)


Im Zuge einer Akteneinsicht vor dem BFG wurde die Sach- und Rechtslage mit dem Bf., der  mittlerweile steuerlich nicht mehr vertreten ist, eingehend erörtert.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_158`)


Der oben wiedergegebene Verfahrensablauf wird von den Parteien nicht bestritten, findet im  Akteninhalt Deckung und wird somit vom BFG zum festgestellten Sachverhalt erhoben.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_161`)


Der Sachverhalt und auch die rechtliche Situation wurden dem Bf. anlässlich mehrerer  Telefonate mit ihm und auch im Rahmen der von ihm vorgenommenen Akteneinsicht durch  das BFG erörtert und von ihm zur Kenntnis genommen.

| Predicted | Gold |
|---|---|
| `BFG` | `BFG` |

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

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Österreich`(organisation)

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_41`)


Der Bf. erhob gegen das Straferkenntnis mit Anbringen vom 5. September 2025 (fristgerecht)  Beschwerde, führte aus wie im oben angeführten Einspruch gegen die Strafverfügung vom  30. Juni 2025 mit dem Ersuchen, die im Straferkenntnis festgelegte Geldstrafe in Höhe von  65,00 Euro [Anmerkung BFG, gemeint: Geldstrafe in Höhe von 55,00 Euro] herabzusetzen.

**False Positives:**

- `BFG` — partial — pred is substring of gold: `BFG,`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `BFG,`(organisation)

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

**False Positives:**

- `BFG` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Magistrat der Stadt Wien`(organisation)
- `Magistrat der Stadt Wien`(organisation)

</details>

---

## `Finanzamt Österreich Entities`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches the Austrian Tax Office in nominative and genitive cases.

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

## `Finanzamt Österreich Variants`

**F1:** 0.060 | **Precision:** 0.889 | **Recall:** 0.031  

**Format:** `regex`  
**Description:**
Matches Finanzamt Österreich and its genitive form Finanzamtes Österreich.

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

## `Magistrat der Stadt Wien Entities`

**F1:** 0.046 | **Precision:** 1.000 | **Recall:** 0.023  

**Format:** `regex`  
**Description:**
Matches the Vienna City Administration (Magistrat) in various forms including genitive and departmental suffixes including - BA32.

**Content:**
```
\bMagistrat(?:es)?(?:\s+der\s+Stadt\s+Wien)(?:\s*,\s*(?:MA\s*67|Magistratsabteilung\s*6|Magistratsabteilung\s*67|MA\s*6|Magistratsabteilung\s*6\s*-\s*BA32))?\b
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

## `Landespolizeidirektion Wien Entities`

**F1:** 0.031 | **Precision:** 1.000 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches the Vienna State Police Directorate.

**Content:**
```
\b(Landespolizeidirektion\s+Wien)\b
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

## `Magistrat der Stadt`

**F1:** 0.031 | **Precision:** 0.800 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches Magistrat der Stadt [City].

**Content:**
```
\bMagistrat(?:s)?\s+der\s+Stadt\s+[A-Z][a-zäöüÄÖÜß]+(?:\s+[A-Z][a-zäöüÄÖÜß]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.800 | 0.016 | 0.031 | 5 | 4 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 1 | 124 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_3`)


III. Gemäß § 25 Abs. 2 BFGG wird der Magistrat der Stadt Wien als Vollstreckungsbehörde  bestimmt.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_19`)


In der Folge lastete der Magistrat der Stadt Wien dem Bf. mit Straferkenntnis vom  4. September 2025, GZ. MA67/GZ/2025, die bereits näher bezeichnete  Verwaltungsübertretung an und verhängte auf Grund der Verletzung der Rechtsvorschriften  des § 5 Abs. 2 (Wiener) Parkometerabgabeverordnung in Verbindung mit § 4 Abs. 1 Wiener  Parkometergesetz 2006 eine Geldstrafe in Höhe von 55,00 Euro und setzte für den Fall der  Uneinbringlichkeit eine Ersatzfreiheitsstrafe von 13 Stunden fest.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_81`)


Hier erweist sich der Magistrat der Stadt Wien als Vollstreckungsbehörde zweckmäßig, da dem  Magistrat der Stadt Wien bereits gemäß § 1 Abs. 1 Z 3 VVG die Vollstreckung der von den  (anderen) Verwaltungsgerichten erlassenen Erkenntnisse und Beschlüsse obliegt (vgl. für viele  ausführlich BFG 13.

| Predicted | Gold |
|---|---|
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |
| `Magistrat der Stadt Wien` | `Magistrat der Stadt Wien` |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_1`)


IM NAMEN DER REPUBLI K  Das Bundesfinanzgericht hat durch die Richterin Mag. Gabriele Friedbacher über die  Beschwerde des Wilhelm Konetzny, Fuhrgassel 36, 4672 Oberndorf, Österreich, vom 5. September 2025, gegen das  Straferkenntnis der belangten Behörde Magistrat der Stadt Wien, MA 67, als  Abgabenstrafbehörde, vom 4. September 2025, GZ. MA67/GZ/2025, wegen der  Verwaltungsübertretung gemäß § 5 Abs. 2 Wiener Parkometerabgabeverordnung, ABl. der  Stadt Wien Nr. 51/2005 idF. ABl. der Stadt Wien Nr. 20/2020, in Verbindung mit § 4 Abs. 1  Wiener Parkometergesetz 2006, LGBl. für Wien Nr. 9/2006 idF LGBl. für Wien Nr. 71/2018, zu  Recht erkannt:  I. Gemäß § 50 Verwaltungsgerichtsverfahrensgesetz (VwGVG) in Verbindung mit § 24 Abs. 1  Bundesfinanzgerichtsgesetz (BFGG) und § 5 Gesetz über das Wiener  Abgabenorganisationsrecht (WAOR) wird die Beschwerde als unbegründet abgewiesen und das  Straferkenntnis des Magistrates der Stadt Wien bestätigt.

**False Positives:**

- `Magistrat der Stadt Wien` — partial — pred is substring of gold: `Magistrat der Stadt Wien, MA 67`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Mag. Gabriele Friedbacher`(person)
- `Wilhelm Konetzny`(person)
- `Fuhrgassel 36, 4672 Oberndorf, Österreich`(address)
- `Magistrat der Stadt Wien, MA 67`(organisation)
- `Magistrates der Stadt Wien`(organisation)

</details>

---

## `Wirtschaftsuniversität Wien`

**F1:** 0.031 | **Precision:** 0.667 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches the University of Economics and Business Vienna.

**Content:**
```
\bWirtschaftsuniversität\s+Wien\b
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

## `VwGH Contextual`

**F1:** 0.024 | **Precision:** 0.048 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches VwGH but excludes it when followed by a hyphen and a noun (e.g., VwGH-Rechtsprechung) or immediately by a date/citation number to avoid false positives in citations.

**Content:**
```
\bVwGH\b(?![\-\s]*[A-Z][a-zäöüÄÖÜß]+)(?!\s+\d{2}\.\d{2}\.\d{4})
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.048 | 0.016 | 0.024 | 83 | 4 | 79 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 4 | 79 | 239 |

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

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_41`)


Dazu zählen beispielsweise Erkrankungen, die die Berufsausbildung auf begrenzte Zeit  unterbrechen, oder Urlaube und Schulferien (VwGH vom 16.11.1993, 90/14/0108).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/131197.1`) (sent_id: `findok-manually-annotated_VALIDATE/131197.1_44`)


Das bloße Aufrechterhalten eines  Berufswunsches ist der tatsächlichen Ausbildung nicht gleichzuhalten (VwGH 24.9.2009,  2009/16/0088, VwGH 21.01.2004, 2003/13/0157, VwGH 14.12.1995, 93/15/0133).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_167`)


Für die Überprüfung dieser  Frage erachte es der VwGH als ausreichend, die Unterscheidung auf die Kernfächer bzw. den  Kernbereich des Studiums zu reduzieren (VwGH 7.8.2001, 97/14/0068).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 3** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_168`)


Eine frühe  Spezialisierung auf einen bestimmten Bereich der Betriebswirtschaftslehre könne unter  Umständen für die spätere Berufslaufbahn von Vorteil sein, doch führe dies nach der  Rechtsprechung des VwGH nicht dazu, von einer fehlenden Gleichwertigkeit der  Studienangebote auszugehen (UFS 16.02.2007, RV/0189-G/06 mit Verweis auf VwGH  26.05.2004, 2000/14/0207).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 4** (doc_id: `findok-manually-annotated_VALIDATE/149395.1`) (sent_id: `findok-manually-annotated_VALIDATE/149395.1_44`)


Ebenso trifft es allerdings zu, dass der  Ruin der wirtschaftlichen Existenz des Bestraften den mit der Bestrafung verfolgten Zweck  auch nicht sinnvoll erreicht (vgl. VwGH 24.9.2003, 2003/13/0084, ÖStZ 2004/190, ÖStZB  2004/109).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 5** (doc_id: `findok-manually-annotated_VALIDATE/149647.1`) (sent_id: `findok-manually-annotated_VALIDATE/149647.1_50`)


Der Bf. bekämpft mit der gegenständlichen Beschwerde ausschließlich die mit dem  Straferkenntnis festgesetzte Strafhöhe, somit war entsprechend der ständigen Judikatur des  Verwaltungsgerichtshofes von einer Teilrechtskraft des Schuldspruches auszugehen (vgl. z.B.  VwGH 20.9.2013, 2013/17/0305).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 6** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_136`)


Ausschlaggebend ist daher, ob die konkrete Tätigkeit bei Anlegen eines  abstrakten Maßstabes ("typischerweise") einen Zusammenhang mit einer in der  Lebensführung begründeten Neigung aufweist, wie dies etwa bei einer nebenberuflich  betriebenen schriftstellerischen Tätigkeit zur Herausgabe eines Sachbuches, die erst auf Grund  der hobbymäßigen Beschäftigung mit jener Materie, die im Sachbuch behandelt wird, zu  bejahen ist (VwGH vom 26.4.2000, 96/14/0095).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 7** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_151`)


Solcherart kann der Mittelpunkt der Tätigkeit einer Konzertpianistin nach der  Verkehrsauffassung an dem Ort angenommen werden, an dem sie die überwiegende Zeit an  ihrem Instrument verbringt, im Beschwerdefall in dem in Rede stehenden Arbeitszimmer  (VwGH vom 24. Juni 2004, 2001/15/0052).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 8** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_65`)


Anspruchszinsen im Sinne des § 205 BAO sind eine objektive Rechtsfolge, um mögliche  Zinsvorteile oder Zinsnachteile auszugleichen, die sich aus unterschiedlichen Zeitpunkten der  Abgabenfestsetzung ergeben (VwGH 24.9.2008, 2007/15/0175).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 9** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_67`)


Eine rechtskräftige Einkommen- oder  Körperschaftsteuerfestsetzung wird vom Gesetz nicht verlangt (VwGH 27.3.2008,  2008/13/0036).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 10** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_72`)


Der Zinsenbescheid ist an die im Spruch des zur Nachforderung oder Gutschrift führenden  Bescheides ausgewiesene Nachforderung bzw. Gutschrift gebunden (Ritz, BAO8, § 205 mit  Hinweis auf VwGH 27.2.2008, 2005/13/0039;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 11** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_73`)


VwGH 27.3.2008, 2008/13/0036;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 12** (doc_id: `findok-manually-annotated_VALIDATE/149793.1`) (sent_id: `findok-manually-annotated_VALIDATE/149793.1_78`)


es erfolgt daher keine Abänderung des ursprünglichen  Zinsenbescheides (Ritz, BAO8, § 205 Tz 35 mit Hinweis auf VwGH 28.5.2009, 2006/15/0316,  VwGH 31.1.2019, Ro 2018/15/0005; sowie zahlreiche Erkenntnisse des BFG).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `BFG`(organisation)

**Example 13** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_62`)


Ob solche triftigen  Gründe vorliegen oder nicht, ist eine Frage der Beweiswürdigung (vgl. VwGH 5.10.2021,  Ra 2021/15/0059).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 14** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_68`)


Nach der Rechtsprechung des VwGH ist die Zwangsläufigkeit des Aufwands jedoch  stets nach den Umständen des Einzelfalls zu prüfen (vgl. VwGH 13.3.2023, Ra 2020/13/0057).

**False Positives:**

- `VwGH` — similar text (different position): `VwGH`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `VwGH`(organisation)

**Example 15** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_99`)


Eine allgemeine sittliche  Pflicht, Dritten beizustehen, besteht hingegen nicht (vgl. VwGH 27.9.1995, 92/15/0214).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 16** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_104`)


Auch Aufwendungen, die nicht von der  gesetzlichen Krankenversicherung getragen werden, können dem Steuerpflichtigen  zwangsläufig erwachsen, wenn sie aus triftigen Gründen medizinisch geboten sind (vgl. VwGH  11.2.2016, 2013/13/0064 mwN).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 17** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_108`)


Dabei ist zu beachten, dass triftige  medizinische Gründe auch höhere Aufwendungen als die von Sozialversicherungsträgern  finanzierten zwangsläufig erscheinen lassen (vgl. VwGH 11.2.2022, Ra 2020/13/0062).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 18** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_110`)


Die triftigen medizinischen Gründe  müssen vielmehr in feststehenden oder sich konkret abzeichnenden ernsthaften  gesundheitlichen Nachteilen bestehen, welche ohne die mit höheren Kosten verbundene  medizinische Betreuung eintreten würden (vgl. VwGH 13.5.1986, 85/14/0181).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 19** (doc_id: `findok-manually-annotated_VALIDATE/149825.1`) (sent_id: `findok-manually-annotated_VALIDATE/149825.1_123`)


Zum anderen handelt es sich bei der  Frage, ob triftige medizinische Gründe vorliegen oder nicht, um eine solche der  Beweiswürdigung, zu deren Überprüfung der Verwaltungsgerichtshof als Rechtsinstanz  grundsätzlich nicht berufen ist (vgl. VwGH 10.5.2021, Ra 2021/15/0031 und 5.10.2021,  Ra 2021/15/0059).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshof`(organisation)

**Example 20** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_30`)


Werde der Nachweis einer Gläubigergleichbehandlung nicht in nachvollziehbarer Weise  erbracht, liege es im Ermessen des Finanzamtes, die Haftung für die genannten  Abgabenbeträge auszusprechen, bei Benachteiligung des Abgabengläubigers im Ausmaß der  nachgewiesenen Benachteiligung der Abgabenschuldigkeiten gegenüber den anderen  Verbindlichkeiten der GmbH (z.B. VwGH 29.1.2004, 2000/15/0168).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 21** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_52`)


Die Haftung gem. § 9 BAO sei eine Ausfallshaftung (VwGH 24.2.2004,  99/14/0278).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 22** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_53`)


Voraussetzung sei die objektive Uneinbringlichkeit der betreffenden Abgaben im  Zeitpunkt der Inanspruchnahme des Haftenden (VwGH 31.3.2004, 2003/13/0153).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 23** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_56`)


Zu den abgabenrechtlichen Pflichten würden insbesondere gehören:  die Abgabenentrichtung aus den Mitteln, die der Vertreter verwalte,  die Führung gesetzlicher Aufzeichnungen (VwGH 30.5.1989, 89/14/0043),  die zeitgerechte Einreichung von Abgabenerklärungen (VwGH 29.5.2001, 2000/14/0006).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 24** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_57`)


Die Pflicht des Vertreters, die vom Vertretenen geschuldeten Abgaben zu entrichten, bestehe  nur insoweit, als hierfür liquide Mittel vorhanden seien (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 25** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_58`)


Der Zeitpunkt, für den zu beurteilen sei, ob der Primärschuldnerin die für die  Abgabenentrichtung erforderlichen Mittel zur Verfügung standen, bestimme sich danach,  wann die Abgaben bei Beachtung der abgabenrechtlichen Vorschriften zu entrichten gewesen  wären (VwGH 27.4.2000, 98/15/0003;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 26** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_66`)


Er sei jedoch nicht verpflichtet, den Abgabengläubiger besser als die übrigen Gläubiger zu  behandeln (VwGH 17.8.1998, 98/17/0038).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 27** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_68`)


(VwGH 22.9.1999, 96/15/0049;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 28** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_70`)


VwGH 29.3.2001, 2000/14/0149).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 29** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_72`)


vielmehr habe der Vertreter das Fehlen ausreichender Mittel nachzuweisen   (VwGH 26.9.2000, 99/13/0090;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 30** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_73`)


VwGH 9.8.2001, 98/16/0348).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 31** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_74`)


Gelinge ein solcher Nachweis   nicht, könne die Haftung für den gesamten uneinbringlichen Abgabenrückstand geltend  gemacht werden (VwGH 27.9.2000, 95/14/0056, VwGH 29.3.2001, 2000/14/0149).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Example 32** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_76`)


Die Behörde habe bei entsprechenden Behauptungen und diesbezüglichem  Beweisanbot die zur Entlastung des Vertreters angebotenen Beweise aufzunehmen und  erforderliche Präzisierungen abzufordern, jedenfalls aber konkrete Feststellungen über die  angebotenen Entlastungsbehauptungen zu treffen (VwGH 23.4.1998, 95/15/0145;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 33** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_77`)


VwGH  20.4.1999, 94/14/0147).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 34** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_85`)


(VwGH 25.6.1990,  89/15/0067).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 35** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_87`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159) sei der Zumutbarkeit bei Heranziehung eines Haftungspflichtigen angesichts  lange verstrichener Zeit im Rahmen der behördlichen Ermessensausübung Bedeutung  beizumessen, allerdings stelle das herangezogene Erkenntnis nicht auf die zurückliegenden  Abgabenschulden ab, sondern auf den Zeitraum zwischen der Beendigung des Konkurses und  der Geltendmachung der Haftung.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 36** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_92`)


Ihm als Vertreter der GmbH sei der Nachweis oblegen, welcher Betrag bei Gleichbehandlung  sämtlicher Gläubiger bezogen auf die jeweiligen Fälligkeitszeitpunkte einerseits und das  Vorhandensein liquider Mittel andererseits - an die Abgabenbehörde zu entrichten gewesen  wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 37** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_94`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt worden sei, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 38** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_95`)


Eine Ausnahme vom Gleichheitsgrundsatz bestehe für Abfuhrabgaben, wie die Lohnsteuer  (VwGH 29.6.1999, 99/14/0040;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 39** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_96`)


VwGH 22.2.2001, 2000/15/0227).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 40** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_99`)


die auf den gekürzten Lohnbetrag  entfallende Lohnsteuer sei zur Gänze zu entrichten (VwGH 16.2.2000, 95/15/0046).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 41** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_102`)


Eine weitere Ausnahme vom Gleichheitsgrundsatz bestehe für Abfuhrabgaben, wie die  Kapitalertragsteuer (VwGH 16.2.2000, 95/15/0046).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 42** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_104`)


Die Pflicht zur Einbehaltung und Abfuhr der Kapitalertragsteuer (§§ 95, 96 EstG 1998) hätten  unter der Sanktion des § 9 Abs. 1 BAO die Vertreter der juristischen Personen zu erfüllen  (VwGH 3.7.2003, 2000/15/0043).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 43** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_107`)


Eine bestimmte Schuldform sei hierfür nicht erforderlich  (VwGH 22.2.2000, 96/14/0158;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 44** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_108`)


VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 45** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_111`)


VwGH 29.5.2001, 99/14/0277;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 46** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_112`)


VwGH 9.8.2001, 98/16/0348).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 47** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_114`)


VwGH 29.6.1999, 99/14/0128).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 48** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_115`)


Der Vertreter habe für die Möglichkeit des Nachweises seines  pflichtgemäßen Verhaltens vorzusorgen (VwGH 7.9.1990, 89/14/0132).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 49** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_116`)


Ihm obliege kein  negativer Beweis, sondern die konkrete (schlüssige) Darstellung der Gründe, die etwa der  rechtzeitigen Abgabenentrichtung entgegengestanden seien (VwGH 4.4.1990, 89/13/0212).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 50** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_122`)


VwGH 20.6.2000, 98/15/0084).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 51** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_141`)


Dazu führte das Finanzamt in der Begründung aus, dass die Geltendmachung einer Haftung in  das Ermessen der Abgabenbehörde gestellt sei (VwGH 23.1.1997, 95/15/0173), wobei die  Ermessensentscheidung im Sinne des § 20 BAO innerhalb der vom Gesetz gezogenen Grenzen  nach Billigkeit und Zweckmäßigkeit unter Berücksichtigung aller in Betracht kommenden  Umstände zu treffen sei.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 52** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_143`)


Aus dem auf die Hereinbringung der Abgabenschuld beim Haftenden gerichteten  Besicherungszweck der Haftungsnorm folge, dass die Geltendmachung der Haftung in der  Regel ermessenskonform sei, wenn die betreffende Abgabe beim Primärschuldner  uneinbringlich sei (vgl. VwGH 25.6.1990, 89/15/0067).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 53** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_146`)


Selbst wenn auf Grund der derzeitigen wirtschaftlichen Situation des Beschwerdeführers die  Abgaben erschwert einbringlich seien, ließe sich daraus eine Unzumutbarkeit der  Haftungsinanspruchnahme nicht ableiten, weil es nach der Rechtsprechung nicht zutreffe, dass  die Haftung nur bis zur Höhe der aktuellen Einkünfte bzw. des aktuellen Vermögens geltend  gemacht werden dürfte (vgl. VwGH 29.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 54** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_148`)


Wie bereits im Haftungsbescheid vom 11.01.2016 ausgeführt, obliege dem Vertreter der GmbH  der Nachweis, welcher Betrag bei Gleichbehandlung sämtlicher Gläubiger bezogen auf die  jeweiligen Fälligkeitszeitpunkte einerseits und das Vorhandensein liquider Mittel andererseits  an die Abgabenbehörde zu entrichten gewesen wäre (VwGH 16.9.2003, 2003/14/0040;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 55** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_150`)


Da trotz Aufforderung vom 24.09.2015 keine rechnerische Darstellung der quotenmäßigen  Gleichbehandlung aller Gläubiger übermittelt wurde, werde die Schlechterstellung des  Finanzamt Kirchdorf Perg Steyr  zu 100% angenommen und die Haftung für den gesamten Abgabenrückstand  ausgesprochen (VwGH 7.12.2000, 2000/16/0601).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Finanzamt Kirchdorf Perg Steyr`(organisation)

**Example 56** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_190`)


Wird eine Abgabe nicht entrichtet, weil der Vertretene überhaupt keine liquiden Mittel hat, so  verletzt der Vertreter dadurch keine abgabenrechtliche Pflicht (VwGH 20.9.1996, 94/17/0420;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 57** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_191`)


VwGH 28.5.2008, 2006/15/0089).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 58** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_192`)


Der Geschäftsführer haftet für nicht entrichtete Abgaben der Gesellschaft auch dann, wenn die  Mittel, die ihm für die Entrichtung aller Verbindlichkeiten zur Verfügung gestanden sind, hierzu  nicht ausreichen; es sei denn, er weist nach, dass er diese Mittel anteilig für die Begleichung  aller Verbindlichkeiten verwendet, die Abgabenschulden daher im Verhältnis nicht schlechter  behandelt hat als andere Verbindlichkeiten (VwGH 19.5.2015, 2013/16/0016).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 59** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_195`)


Am Bf., dem als Geschäftsführer der Primärschuldnerin ausreichend Einblick in die Gebarung  zustand, war es gelegen, das Ausmaß der quantitativen Unzulänglichkeit der in den  Fälligkeitszeitpunkten der Abgaben zur Verfügung stehenden Mittel nachzuweisen (VwGH  19.11.1998, 97/15/0115), da nicht die Abgabenbehörde das Ausreichen der Mittel zur  Abgabenentrichtung nachzuweisen hat, sondern der zur Haftung herangezogene  Geschäftsführer das Fehlen ausreichender Mittel (VwGH 23.4.1998, 95/15/0145).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 60** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_197`)


Tritt der Vertreter diesen  Nachweis nicht an, dann kann ihm die uneinbringliche Abgabe zur Gänze vorgeschrieben  werden (VwGH 28.9.2004, 2001/14/0176).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 61** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_198`)


Die bisherige Rechtsprechung des Verwaltungsgerichtshofes (VwGH 24.1.2017, Ra  2015/16/0078;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 62** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_199`)


VwGH 2.7.2015, 2013/16/0220;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 63** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_200`)


VwGH 24.1.2013, 2012/16/0100), womit dieser  klarstellte, dass eine Betrachtung der Gläubigergleichbehandlung zum jeweiligen  Fälligkeitszeitpunkt zu erfolgen hatte, wurde mit dem Erkenntnis vom 28.6.2022, Ra  2020/13/0067, aufgegeben:  "Dabei kommt es für den Nachweis der Gläubigergleichbehandlung nicht nur auf die  liquiden Mittel zum Fälligkeitstag an, die den an diesem einen Tag jeweilig fälligen  Verbindlichkeiten gegenüberzustellen sind, weil eine derartige Betrachtung für nur einen  einzigen Tag im Monat ohne Berücksichtigung der vorhandenen liquiden Mittel für die  Zeiträume nach der Fälligkeit der Abgaben keinen Nachweis über eine  Gläubigergleichbehandlung geben kann."

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 64** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_204`)


Erfüllung der vollen Abgabenverbindlichkeiten kommt eine Beschränkung der Haftung des Bf.  bloß auf einen Teil der von der Haftung betroffenen Abgabenschulden nicht in Betracht (VwGH  21.1.1991, 90/15/0055).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 65** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_205`)


Kausalität  Infolge der schuldhaften Pflichtverletzung durch den Bf. konnte die Abgabenbehörde nach der  Judikatur des Verwaltungsgerichtshofes (VwGH 17.5.2004, 2003/17/0134), auch davon  ausgehen, dass die Pflichtverletzung Ursache für die Uneinbringlichkeit der  haftungsgegenständlichen Abgaben war.

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 66** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_208`)


Aus dem auf die  Hereinbringung der Abgabenschuld beim Haftenden gerichteten Besicherungszweck der  Haftungsnorm folgt, dass die Geltendmachung der Haftung in der Regel ermessenskonform ist,  wenn die betreffende Abgabe beim Primärschuldner uneinbringlich ist (VwGH  25.6.1990, 89/15/0067).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 67** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_209`)


Nach ständiger Rechtsprechung des Verwaltungsgerichtshofes (zB VwGH 3.9.2008,  2006/13/0159;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 68** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_219`)


Auf die ständige Rechtsprechung des Verwaltungsgerichtshofes wird hingewiesen,  wonach einer Beschwerdevorentscheidung sowie einem Vorlagebericht Vorhaltscharakter  zukommt (vgl. VwGH vom 29.1.2020, Ra 2019/13/0071, VwGH vom 30.6.2021, Ra  2021/15/0048).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation
- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 2

**Gold Entities:**

- `Verwaltungsgerichtshofes`(organisation)

**Example 69** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_46`)


2. Der Säumniszuschlag ist eine „Sanktion eigener Art“ (zB VwGH 21.4.1983, 83/16/0016;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 70** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_51`)


Ein  fehlendes (grobes) Verschulden ist hingegen bedeutsam für die Wiedereinsetzung in den  vorigen Stand (§ 308) wegen Versäumung der Zahlungsfrist (zB VwGH 4.11.1994, 92/16/0167;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 71** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_52`)


VwGH 19.9.1995, 95/14/0050) sowie für § 217 Abs 7 BAO (vgl. Ritz/Koran, BAO8, § 217 Rz 43- 49).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 72** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_55`)


6. Nach der Rechtsprechung (zB VwGH 24.1.2018, Ra 2017/13/0023;

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

**Example 73** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_91`)


Weil die einbringungshemmende und damit säumniszuschlagsverhindernde  Wirkung eines Antrags gemäß § 217 Abs. 4 lit. b iVm § 230 Abs. 6 BAO auch dann eintritt, wenn  die Abgabe bereits fällig war, hätte dieser Antrag auf Aussetzung nur dann keine die  Einbringung hemmende Wirkung entfaltet, wenn bereits vor Antragstellung ein  Säumniszuschlag festgesetzt worden wäre, weil dem Gesetz nicht zu entnehmen ist, dass durch  einen Aussetzungsantrag Rechtsfolgen, die bereits vor Antragstellung durch die nicht  zeitgerechte Entrichtung einer Abgabe eingetreten sind, rückgängig gemacht werden sollten  und daher ein durch Bescheid der bereits festgesetzte Säumniszuschlag durch einen später  gestellten Aussetzungsantrag beseitigt würde (vgl. VwGH 27.2.2015, 2011/17/0103).

**False Positives:**

- `VwGH` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Finanzamt Österreich Nominative`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches Finanzamt Österreich in nominative case.

**Content:**
```
\bFinanzamt\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.012 | 0.023 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 149 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

## `Finanzamt Österreich`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches Finanzamt Österreich specifically to ensure coverage.

**Content:**
```
\bFinanzamt(?:s)?\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.012 | 0.023 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 149 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

## `Finanzamt and Related Entities`

**F1:** 0.023 | **Precision:** 1.000 | **Recall:** 0.012  

**Format:** `regex`  
**Description:**
Matches Finanzamt, Finanzstrafsenat, Zollamt, and Amt für Betrugsbekämpfung with their specific qualifiers, strictly bounded to avoid matching subsequent text.

**Content:**
```
\b(?:Finanzstrafsenat\s+Wien\s+2|Finanzamt\s+Österreich|Finanzamts\s+Österreich|Zollamt\s+Österreich|Amt\s+für\s+Betrugsbekämpfung\s+als\s+Finanzstrafbehörde|Finanzamt\s+(?:Wien\s+\d+/\d+/\d+|Wien\s+\d+/\d+|\w+\s+\d+/\d+|Österreich|Waldviertel))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.012 | 0.023 | 3 | 3 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 3 | 0 | 149 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/138708.1`) (sent_id: `findok-manually-annotated_VALIDATE/138708.1_163`)


Auch im Hinblick auf § 34 Abs. 8 EStG 1988, welcher im Rahmen der außergewöhnlichen  Belastung durch bezahlte auswärtige Ausbildungskosten auf vergleichbare Studien im  Einzugsbereich abstellt, hat das Finanzamt Österreich diese Studien offenbar als vergleichbar  angesehen (vgl. die Ausführungen des BFG vom 24.03.2020, RV/5101354/2019 zu einem mit  dem beschwerdegegenständlichen Sachverhalt vergleichbaren Beschwerdefall;

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149394.1`) (sent_id: `findok-manually-annotated_VALIDATE/149394.1_1`)


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

**Example 2** (doc_id: `findok-manually-annotated_VALIDATE/149907.1`) (sent_id: `findok-manually-annotated_VALIDATE/149907.1_26`)


Mit Bescheiden vom 30.8.2024 setzte das Finanzamt Österreich Umsatzsteuer  (Fahrzeugeinzelbesteuerung) in Höhe von 14.218,49 Euro und Normverbrauchsabgabe in Höhe  von 11.785,71 Euro fest.

| Predicted | Gold |
|---|---|
| `Finanzamt Österreich` | `Finanzamt Österreich` |

</details>

---

## `VwGH Abbreviation`

**F1:** 0.022 | **Precision:** 0.034 | **Recall:** 0.016  

**Format:** `regex`  
**Description:**
Matches the abbreviation for the Administrative Court (VwGH).

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

## `ÖGK`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the abbreviation for the Austrian Health Insurance Fund.

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

## `Pensionsversicherungsanstalt`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the Pensionsversicherungsanstalt.

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

## `Bundesfinanzgerichts`

**F1:** 0.008 | **Precision:** 1.000 | **Recall:** 0.004  

**Format:** `regex`  
**Description:**
Matches the Federal Financial Court in genitive case.

**Content:**
```
\bBundesfinanzgerichts\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 1.000 | 0.004 | 0.008 | 1 | 1 | 0 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 1 | 0 | 99 |

</details>

---

<details>
<summary>✅ Worked</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149676.1`) (sent_id: `findok-manually-annotated_VALIDATE/149676.1_93`)


Diese Sachverhaltsfeststellungen ergeben sich nach Dafürhalten des Bundesfinanzgerichts aus  den vorgelegten Akten des Abgabenverfahrens, dem Vorbringen der Bf. in seiner Beschwerde  sowie den Erhebungen durch das Bundesfinanzgericht.

| Predicted | Gold |
|---|---|
| `Bundesfinanzgerichts` | `Bundesfinanzgerichts` |

**Missed by this rule (FN):**

- `Bundesfinanzgericht` (organisation)

</details>

---

## `Specific Private Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that do not end in GmbH/AG/OG, such as SüdVersand and Raiffeisenbank. Updated to ensure strict boundaries.

**Content:**
```
\b(S\u00fcdVersand|Raiffeisenbank\s+Wels\s+S\u00fcd|TraunLuftfahrt\s+Solutions)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names (No Suffix)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that do not end in standard suffixes like GmbH/AG, based on training data.

**Content:**
```
\b(Textil\s+Steingartlog|Keltrizor\s+Handel|DLCG\s+Bildung)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names (With Suffix)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that include 'GMBH' or 'GmbH' but have unique prefixes.

**Content:**
```
\b(Hudec&Christian\s+Immobilien\s+GMBH|Hendrick\s+Recycling\s+GMBH|Stefansky\s+Bau\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Reinemut Smoch Handel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name 'Reinemut + Smoch Handel'.

**Content:**
```
Reinemut\s+\+\s+Smoch\s+Handel
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Salzburg-Stadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Salzburg-Stadt' and 'FA Salzburg-Stadt' variations.

**Content:**
```
\b(?:Finanzamt|FA)\s+Salzburg\-Stadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA Salzburg-Stadt URL`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the URL variant 'www.FA Salzburg-Stadt'.

**Content:**
```
www\.FA\s+Salzburg\-Stadt
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Triloglex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Triloglex GMBH.

**Content:**
```
\bTriloglex\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company MittelHeizung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name MittelHeizung Werke AG.

**Content:**
```
\bMittelHeizung\s+Werke\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Rosilius`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Rosilius Pflege AG.

**Content:**
```
\bRosilius\s+Pflege\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Yavasoglu`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company name Yavasoglu Analyse AG.

**Content:**
```
\bYavasoglu\s+Analyse\s+AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity Zoruniglanz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity Zoruniglanz.

**Content:**
```
\bZoruniglanz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Entity Sophie Wittmeir`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity Sophie Wittmeir (labeled as organisation in training data).

**Content:**
```
\bSophie\s+Wittmeir\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Klusner`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Klusner&P\u00e4ffgen Bildung GMBH' which contains an ampersand.

**Content:**
```
\bKlusner\&P\u00e4ffgen\s+Bildung\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Tschermack`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Tschermack Pharma GMBH'.

**Content:**
```
\bTschermack\s+Pharma\s+GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company TalVerverwerk`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'TalVerverwerkGarten GMBH' and its ellipsis variant.

**Content:**
```
\bTalVerverwerkGarten\s+GMBH(?:\u2026)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company SudLandwirtschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'S\u00fcd-Landwirtschaft'.

**Content:**
```
\bS\u00fcd\-Landwirtschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Compound Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known compound company names with hyphens or specific structures that the generic rule misses.

**Content:**
```
\b(?:Dongartcon\-Landwirtschaft|Monlogtri\-Analyse|RheinMetall\s+Technologien|Logseemon\-Metall|Gumpold\s+Technik)\s+(?:GMBH|AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Bank and Other Companies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known company names like VOLKSBANK WIEN, Conwil-Marine, Tal-Druck, DIAS Telekom Institut.

**Content:**
```
\b(?:VOLKSBANK\s+WIEN|Conwil\-Marine|Tal\-Druck|DIAS\s+Telekom\s+Institut)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Legal Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific organization names found in the training data and failure cases, including BDO, HPS, and others.

**Content:**
```
\b(?:HPS\s+Hergovits,\s+Pinkel\s+&\s+Schnabl\s+Steuerberatungs\s+GmbH|BDO\s+Austria\s+GmbH\s+WP\-\s+u\.\s+StBges\.|Reinemut\s+\+\s+Smoch\s+Handel|Lubomir\s+Merschmeyer|Roelfsen\s+Versicherung|LeitnerLeitner\s+GmbH\s+Wirtschaftsprüfer\s+und\s+Steuerberater|Dorfcon-Verlag|Houdek\s+Maschinenbau|Milan\s+Händlein|Manfredo\s+Herrschmann|Englert\s+Möbel|Laskowsky\s+Umwelt|Annemie\s+Bott|StadtEnergie\s+Holding|Krolitzki\s+Beratung|Butkus\s+Metall|Keldonbach\s+Sicherheit\s+GMBH|TraunChemie\s+GMBH|Gözcü\s+Getränke|Hörup\s+Gastronomie\s+AG|Houdek\s+Maschinenbau|Dorfcon-Verlag|Dammke\s+KI\s+GMBH|Naaß\s+Elektro\s+GMBH|Bersud\s+Möbel\s+GMBH|Unter\s+Heimdorf\s+GMBH|Kornfelder\s+Recycling|WXE\s+Textil\s+GMBH|Obernöder+Kübert\s+Touristik\s+GMBH|Talost\s+GMBH|SüdEvent\s+AG|Kudla&Kühnel\s+Solar|Logal\s+Gruppe|Hempel\s+Heizung\s+GMBH|Dorfkraft-Sanitär\s+AG|ZYJY\s+Automotive\s+AG|NYJ\s+Event\s+AG|Kubzyk\s+Elektro\s+AG|Lütkehans\s+Event\s+GMBH|InnLuftfahrt\s+GMBH|Depp\s+Versand)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific IT Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches IT entities like 'Lexdon IT'

**Content:**
```
(?<!\w)[A-Za-zäöüÄÖÜß]+\s+IT
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Verlag Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Verlag entities like 'Dorfcon-Verlag'

**Content:**
```
(?<!\w)[A-Za-zäöüÄÖÜß\-]+\s*Verlag
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Maschinenbau Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Maschinenbau entities like 'Houdek Maschinenbau'.

**Content:**
```
(?<!\w)[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df]+\s+Maschinenbau\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Luftfahrt Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Luftfahrt entities like 'Schmeltz Luftfahrt'.

**Content:**
```
(?<!\w)[A-Za-zÄÖÜäöüß]+\s+Luftfahrt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Finanzamt Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt entities like 'Finanzamt Wien 1/23' with precise boundaries, stopping before common prepositions or verbs.

**Content:**
```
(?<!\w)Finanzamt\s+(?:Wien\s+\d+/\d+|\w+\s+\d+/\d+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Named Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known entities that do not follow standard patterns: Trafenfen Automotive, DrauFinanzen, Kelgart-Druck, Bezirksgericht Zell am See.

**Content:**
```
\b(?:Trafenfen\s+Automotive|DrauFinanzen|Kelgart-Druck|Bezirksgericht\s+Zell\s+am\s+See)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Company Names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific company names that do not fit the generic pattern or have specific capitalization/spacing issues.

**Content:**
```
\b(?:Chen Setzekorn|Istvan Gerart|InnMarine GMBH|HochLebensmittel Holding GMBH|Ostgart AG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific Trade Names (No Suffix)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known trade names that appear without their legal suffix in the ground truth, prioritizing them over generic suffix rules.

**Content:**
```
\b(?:Kök\s+&\s+Heberlein\s+Bau|Leiss\s+Software|Okur\s+Automotive|Celikkanat\s+Garten|RheinDigital|Getränke\s+Nexdorfzor\s+GMBH|Depp\s+Versand)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `GmbH & Partner KG Pattern`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific 'GmbH & Partner KG' patterns which are common in legal texts for law firms or tax advisors.

**Content:**
```
(?<!\w)([A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß\s\.\&\-]+?)(?:GmbH\s+&\s+Partner\s+KG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `WaldTouristik Technologies`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Specific rule for 'WaldTouristik Technologien' which appears frequently in the training data and is a unique name.

**Content:**
```
\bWaldTouristik\s+Technologien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Legal Case Organization Names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures organization names in 'in der Beschwerdesache' context, specifically looking for names with suffixes (GmbH, AG) or compound structures (u., +) to avoid matching personal names.

**Content:**
```
(?:in der Beschwerdesache der|in der Beschwerdesache des)\s+([A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df][A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df\s\.\&\-\+\u00fc\u00f6\u00e4\u00c4\u00d6\u00DC]+?(?:GmbH?|AG|u\.|\+)[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df\s\.\&\-\+\u00fc\u00f6\u00e4\u00c4\u00d6\u00DC]+?)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bank and Institute Names`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures specific bank or institute names that might not have standard suffixes or are long compound names, e.g., 'Raiffeisen ... in Tirol', 'Inn-Recycling Institut'.

**Content:**
```
(?:Inn\-Recycling\s+Institut|Raiffeisen\s+[A-Za-z\u00c4\u00d6\u00dc\u00e4\u00f6\u00fc\u00df]+\s+(?:Bank|in\s+Tirol))
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific GMBH Names with Special Chars`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known company names containing '&' or 'u.' followed by GMBH.

**Content:**
```
(?:Zschieschank&Hee\u00df Transport|M\u00fcllbrandt u\. Worthmeier Digital|Ober\-Chemie) GMBH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Two-Word Company Names (Marine/Wind)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific two-word company names like 'Logkeltal Marine' and 'Nowothnig Wind' that lack standard suffixes.

**Content:**
```
\b(?:Logkeltal Marine|Nowothnig Wind|S\u00fcd Sudwil)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Huber Swoboda Oswald Aixberger Rechtsanwälte GmbH Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm Huber Swoboda Oswald Aixberger.

**Content:**
```
\b(Huber\s+Swoboda\s+Oswald\s+Aixberger\s+Rechtsanwälte\s+GmbH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `UnterRecycling Services GMBH Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific company UnterRecycling Services GMBH.

**Content:**
```
\b(UnterRecycling\s+Services\s+GMBH)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BMF Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation for the Federal Ministry of Finance.

**Content:**
```
\bBMF\b
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
Matches the District Administrative Authority of Bludenz.

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

## `PVA Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation for the Public Insurance Institution.

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

## `SeneCura Laurentius-Park Bludenz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name of the SeneCura facility in Bludenz.

**Content:**
```
\bSeneCura\s+Laurentius-Park\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `SENECURA Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches SeneCura and its variations including location suffixes (Laurentius Park, Bludenz) in various capitalizations.

**Content:**
```
\bS(?:ENECURA|eneCura|enecura)(?:\s+(?:Laurentius\s+Park(?:\s+Bludenz)?|Bludenz))?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `ÖBB Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Austrian Federal Railways abbreviation ÖBB.

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

## `Krankenpflegevereins Bludenz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific organization 'Krankenpflegevereins Bludenz'.

**Content:**
```
\bKrankenpflegevereins\s+Bludenz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BFH Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation for the Federal Fiscal Court (Bundesfinanzhof).

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

## `Steuerberater OG Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific tax advisor firms ending in OG.

**Content:**
```
\bSteuerberater\s+Metzler\s+&\s+Adelsberger\s+OG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Wiederspan and Mur Alver Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific GmbH and OG entities.

**Content:**
```
\b(?:Wiederspan\s+Beratung\s+GMBH|Mur\s+Alver\s+OG)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Henken Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity 'Henken' as listed in training data.

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

## `Retail Chain Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific retail organizations.

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

## `London Film Academy Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches London Film Academy and its common typo.

**Content:**
```
\bLondon\s+Film\s+(?:Academy|Acadamy)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundeskanzleramt Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Federal Chancellery.

**Content:**
```
\bBundeskanzleramtes\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Innsbruck Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamtes Innsbruck.

**Content:**
```
\bFinanzamtes\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Schwechat Gerasdorf Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt Schwechat Gerasdorf.

**Content:**
```
\bFinanzamt\s+Schwechat\s+Gerasdorf\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Deloitte Tax Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Deloitte Tax Wirtschaftsprüfungs GmbH.

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

## `Ernst & Young Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Ernst & Young Steuerberatungsgesellschaft m.b.H.

**Content:**
```
\bErnst\s+&\s+Young\s+Steuerberatungsgesellschaft\s+m\.b\.H\.\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Technik Valseekel Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Technik Valseekel GMBH.

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

## `Wiener Städtische Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Wiener Städtische.

**Content:**
```
\bWiener\s+Städtische\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Allianz Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Allianz.

**Content:**
```
\bAllianz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Wien 1/23 Entity`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamtes Wien 1/23.

**Content:**
```
\bFinanzamtes\s+Wien\s+1/23\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `VfGH Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation for the Constitutional Court (VfGH).

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

## `Wiener Städtische Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Wiener Städtische and its full insurance name.

**Content:**
```
\bWiener Städtische(?:n Versicherung)?\b
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
Matches AMS Österreich and Arbeitsmarktservice.

**Content:**
```
\b(AMS\s+Österreich|Arbeitsmarktservice(?:\s*\(AMS\))?|Arbeitsmarktservice)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `KG Company Suffix`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches company names ending in GmbH & Co KG, ensuring full name capture.

**Content:**
```
(?<!\w)(?<!durch\s)(?<!die\s)(?<!der\s)(?<!des\s)(?<!bei\sder\s)(?<!bei\sdem\s)(?<!bei\sden\s)(?<!an\sdie\s)(?<!an\sdem\s)(?<!an\sden\s)(?<!bei\s)(?<!in\s)(?<!von\s)(?<!Dr\.\s)(?<!"\s)([A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß\s\.\&\-\+\'\(\)]{1,100})(?:\s+GmbH\s*&\s*Co\s*KG\b)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Innsbruck`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Tax Office Innsbruck.

**Content:**
```
\bFinanzamt\s+Innsbruck\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Landespolizeidirketion Tirol`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the State Police Directorate Tyrol (including the specific typo 'direktion' found in training data).

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

## `Arbeits- und Sozialgericht Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Labour and Social Court with or without Wien.

**Content:**
```
\bArbeits-\s+und\s+Sozialgericht(?:\s+Wien)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Ernst & Young Steuerberatungs-GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm Ernst & Young Steuerberatungs-GmbH.

**Content:**
```
\bErnst\s+&\s+Young\s+Steuerberatungs-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verfassungsgerichtshof`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Constitutional Court.

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

## `FA Waldviertel`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific tax office abbreviation FA Waldviertel.

**Content:**
```
\bFA\s+Waldviertel\b
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
Matches the specific entity F Personalservice GmbH, handling potential spacing variations.

**Content:**
```
\bF\s+Personalservice\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `F Personal GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific entity F Personal GmbH.

**Content:**
```
\bF\s+Personal\s+GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BDO Austria GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific long-form company name BDO Austria GmbH Wirtschaftsprüfungs- und Steuerberatungsgesellschaft.

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

## `FA Klosterneuburg`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific Finanzamt abbreviation for Klosterneuburg.

**Content:**
```
\bFA\s+Klosterneuburg\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Universität St. Gallen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches University of St. Gallen with optional 'in'.

**Content:**
```
\bUniversität\s+(?:in\s+)?St\.\s+Gallen\b
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
**Description:**
Matches the Administrative Court Vienna.

**Content:**
```
\bVerwaltungsgericht\s+Wien\b
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
**Description:**
Matches the Swiss Accident Insurance (SUVA), excluding cases where it is part of a compound noun like SUVA-Rente.

**Content:**
```
\bSUVA\b(?![\-\s]*[A-Z][a-zäöüÄÖÜß]+)
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FA and UFS Abbreviations`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'FA' (Finanzamt) and 'UFS' (Unabhängiger Finanzsenat) as organizations.

**Content:**
```
\b(?:FA\s+(?:Wien\s+\d+/\d+|\w+\s+\d+/\d+)|UFS)\b
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

## `BFG with Location`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches BFG with location qualifiers like 'Außenstelle Linz'.

**Content:**
```
\bBFG\s+(?:Außenstelle\s+Linz|,\s*Außenstelle\s+Linz|\(Außenstelle\s+Linz\))\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific law firm Dr. Roland Gabl Rechtsanwalts- Kommandit-Partnerschaft.

**Content:**
```
\bDr\.\s+Roland\s+Gabl\s+Rechtsanwalts\-\s+Kommandit\-Partnerschaft\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Versorgungskasse Deutscher Unternehmen VVaG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific pension fund Versorgungskasse Deutscher Unternehmen VVaG.

**Content:**
```
\bVersorgungskasse\s+Deutscher\s+Unternehmen\s+VVaG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Pensionsversicherungsanstalt Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific pension insurance office Pensionsversicherungsanstalt Wien.

**Content:**
```
\bPensionsversicherungsanstalt\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Deutschen Rentenversicherung Bund`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the German pension insurance Bund.

**Content:**
```
\bDeutschen\s+Rentenversicherung\s+Bund\b
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
Matches the Swiss Accident Insurance Institution (SUVA) full name.

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

## `Frontex`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the European Border and Coast Guard Agency (Frontex).

**Content:**
```
\bFrontex\b
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
Matches the full name of the European Border and Coast Guard Agency.

**Content:**
```
\bEuropäische\s+Grenzschutzagentur\s+Frontex\b
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
**Description:**
Matches the Federal Ministry of the Interior (BM für Inneres).

**Content:**
```
\bBM\s+für\s+Inneres\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Kriminalpolizei in Österreich`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Criminal Police in Austria.

**Content:**
```
\bKriminalpolizei\s+in\s+Österreich\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesministerium für Inneres`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Federal Ministry of the Interior in nominative and genitive cases.

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

## `Bundesministeriums für Finanzen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Federal Ministry of Finance in various cases.

**Content:**
```
\bBundesministerium(?:s)?\s+für\s+Finanzen\b
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
Matches the abbreviation BM für Finanzen.

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

## `Flughafen München`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Munich Airport.

**Content:**
```
\bFlughafen\s+München\b
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
**Description:**
Matches the OECD organization.

**Content:**
```
\bOECD\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BMI Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation for the Federal Ministry of the Interior.

**Content:**
```
\bBMI\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Verfassungsgerichtshofes`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Constitutional Court in genitive case.

**Content:**
```
\bVerfassungsgerichtshof(?:es)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Gesellschaft Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches organizations named 'Gesellschaft' followed by 'für' and a capitalized noun, e.g., Österreichische Gesellschaft für Europapolitik.

**Content:**
```
\b(?:Österreichische\s+)?Gesellschaft\s+für\s+[A-Z][a-zäöüÄÖÜß]+(?:\s+[A-Z][a-zäöüÄÖÜß]+)*\b
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
**Description:**
Matches Universität Wien specifically.

**Content:**
```
\bUniversität\s+Wien\b
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
**Description:**
Matches FH Kärnten specifically.

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

## `Fachhochschule Kärnten`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Fachhochschule Kärnten specifically.

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

## `Karl-Franzens- Universität Graz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Karl-Franzens- Universität Graz specifically, handling the space after the hyphen.

**Content:**
```
\bKarl-Franzens-\s+Universität\s+Graz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `FAÖ Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation FAÖ for Finanzamt Österreich.

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

## `SVS/SVB Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation SVS/SVB for social security organizations.

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

## `Uni Wien Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the common abbreviation Uni Wien for Universität Wien.

**Content:**
```
\bUni\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Pädagogische Hochschule Wien`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Pädagogische Hochschule Wien in various cases and with flexible whitespace.

**Content:**
```
\bPädagogische\s+Hochschule\s+Wien\b
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
Matches the specific organization Sozialversicherung der Bauern.

**Content:**
```
\bSozialversicherung\s+der\s+Bauern\b
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
**Description:**
Matches PSD Wien.

**Content:**
```
\bPSD\s+Wien\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Psychiatrie Otto Wagner Spital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Psychiatrie Otto Wagner Spital- (with optional hyphen).

**Content:**
```
\bPsychiatrie\s+Otto\s+Wagner\s+Spital-?\b
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
Matches the specific minister title as an organization reference.

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

## `Bundesamtes für Soziales und Behindertenwesen`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Federal Office in genitive case (Bundesamtes).

**Content:**
```
\bBundesamtes\s+für\s+Soziales\s+und\s+Behindertenwesen\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt City`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt followed by a city name (e.g., Finanzamtes Feldkirch, Finanzamt FA).

**Content:**
```
\bFinanzamtes?\s+(?:FA\s+)?[A-Z][a-zäöüÄÖÜß]+(?:\s+[A-Z][a-zäöüÄÖÜß]+)*\b
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

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 9/18/19 Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Franz Josefskai 53/2/10, 1010 Wien`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `94-300/0486`(tax_number)

**Example 1** (doc_id: `findok-manually-annotated_VALIDATE/149803.1`) (sent_id: `findok-manually-annotated_VALIDATE/149803.1_1`)


BESCHLUSS   Das Bundesfinanzgericht hat durch den Richter Hon.-Prof. Thassilo Averdiek  in der Beschwerdesache Alma Springel,  Freiensteinweg 8v, 9433 Kragelsdorf, Österreich  hinsichtlich der Beschwerde vom 19. April 2016 gegen die Bescheide des  Finanzamtes Wien 9/18/19 Klosterneuburg, nunmehr des Finanzamtes Österreich,  Steuernummer 75-059/0556, betreffend Einkommensteuer 2011 - 2013 und Umsatzsteuer  2011 - 2014, jeweils vom 18. Jänner 2016, sowie Einkommensteuer 2015 vom 27. April 2016,  beschlossen:   I. Die Beschwerde wird gemäß § 256 Abs 3 BAO als gegenstandslos erklärt.

**False Positives:**

- `Finanzamtes Wien` — partial — pred is substring of gold: `Finanzamtes Wien 9/18/19 Klosterneuburg`

> overlaps gold: 1  |  likely missing annotation: 0

**Gold Entities:**

- `Bundesfinanzgericht`(organisation)
- `Hon.-Prof. Thassilo Averdiek`(person)
- `Alma Springel`(person)
- `Freiensteinweg 8v, 9433 Kragelsdorf, Österreich`(address)
- `Finanzamtes Wien 9/18/19 Klosterneuburg`(organisation)
- `Finanzamtes Österreich`(organisation)
- `75-059/0556`(tax_number)

</details>

---

## `Finanzpolizei City`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzpolizei followed by a city name.

**Content:**
```
\bFinanzpolizei\s+[A-Z][a-zäöüÄÖÜß]+(?:\s+[A-Z][a-zäöüÄÖÜß]+)*\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Immobilienbüro Name`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Immobilienbüro followed by a name.

**Content:**
```
\bImmobilienbüro\s+[A-Z][a-zäöüÄÖÜß]+(?:\s+[A-Z][a-zäöüÄÖÜß]+)*\b
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
Matches the acronym FAG (Finanzamt für Großbetriebe) as a standalone entity, excluding preceding articles.

**Content:**
```
(?<!\w)(?<!der\s)(?<!die\s)(?<!das\s)(?<!dem\s)(?<!den\s)(?<!des\s)(?<!von\s)(?<!bei\s)(?<!in\s)(?<!an\s)(?<!mit\s)(?<!auf\s)(?<!zu\s)(?<!für\s)(?<!nach\s)(?<!vor\s)(?<!über\s)(?<!unter\s)(?<!ohne\s)(?<!durch\s)(?<!gegen\s)(?<!um\s)(?<!seit\s)(?<!bis\s)(?<!aus\s)(?<!bei\sder\s)(?<!bei\sdem\s)(?<!bei\sden\s)(?<!im\s)(?<!am\s)(?<!zum\s)(?<!zur\s)(?<!ins\s)(?<!ans\s)(?<!vom\s)(?<!zur\s)(?<!der\s)(?<!die\s)(?<!das\s)(?<!dem\s)(?<!den\s)(?<!des\s)\bFAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt für Großbetriebe`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name 'Finanzamt für Großbetriebe'.

**Content:**
```
\bFinanzamt\s+für\s+Großbetriebe\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Specific GmbH Patterns`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific known GmbH patterns like 'A-GmbH' and 'Hausverwaltung-GmbH' with strict boundaries.

**Content:**
```
\b(?:A|Hausverwaltung)\-GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bank and Chamber Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches specific bank and chamber names like Erste Bank and WKO.

**Content:**
```
\b(?:Erste\s+Bank|WKO)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Federal Ministry Entities`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches federal ministry names like Bundesministeriums für Justiz.

**Content:**
```
\bBundesministeriums\s+für\s+Justiz\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `LG Innsbruck and LG für ...`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Landesgericht Innsbruck and LG für [Location] patterns.

**Content:**
```
\b(?:Landesgericht\s+Innsbruck|LG\s+für\s+[A-ZäöüÄÖÜß\s]+)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 1 | 0 | 1 |

**Per-Class Breakdown**

| Class | TP | FP | FN |
|---|---|---|---|
| `organisation` | 0 | 1 | 29 |

</details>

---

<details>
<summary>⚠️ False Positives</summary>

**Example 0** (doc_id: `findok-manually-annotated_VALIDATE/149885.1`) (sent_id: `findok-manually-annotated_VALIDATE/149885.1_50`)


Dieses Verfahren beim LG für  ZRS X, GZ 40S 35/13 i, sei am tt.08.2013 gem. § 152b IO aufgehoben worden.

**False Positives:**

- `LG für  ZRS X` — no gold match — likely missing annotation

> overlaps gold: 0  |  likely missing annotation: 1

</details>

---

## `Bezirksgericht Silz`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the specific court name Bezirksgericht Silz.

**Content:**
```
\bBezirksgericht\s+Silz\b
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
Matches the specific company name Eckhardt SteuerberatungsgmbH.

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

## `Fachhochschule Wiener Neustadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the University of Applied Sciences Wiener Neustadt.

**Content:**
```
\bFachhochschule\s+Wiener\s+Neustadt\b
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
Matches FH Campus Wien.

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

## `FH Wiener Neustadt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches FH Wiener Neustadt (short form).

**Content:**
```
\bFH\s+Wiener\s+Neustadt\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Wien Specific`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Finanzamt Wien with specific district numbers, including the 4-part pattern.

**Content:**
```
\bFinanzamt\s+Wien\s+\d+/\d+/\d+(?:/\d+)?\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `LAG Abbreviation`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the abbreviation LAG (Landesabgabenbehörde) as a standalone entity.

**Content:**
```
\bLAG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesfinanzgericht (BFG)`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name with abbreviation in parentheses.

**Content:**
```
\bBundesfinanzgericht\s+\(BFG\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Bundesfinanzgericht Compound`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full compound name 'Bundesfinanzgericht (BFG)' as a single entity.

**Content:**
```
\bBundesfinanzgericht\s+\(BFG\)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `COFAG and Cofag`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches COFAG and Cofag (case variations) as organizations.

**Content:**
```
\b(?:COFAG|Cofag)\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `BHAG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches BHAG (Bezirkshauptmannschaft) as an organization.

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

## `DA Deutsche Allgemeine Versicherung AG`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name of the insurance company.

**Content:**
```
\bDA Deutsche Allgemeine Versicherung AG\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AVED cosmetic`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches AVED cosmetic as an organization.

**Content:**
```
\bAVED cosmetic\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Yoga Vidya GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Yoga Vidya GmbH as an organization.

**Content:**
```
\bYoga Vidya GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Geschenkartikel GmbH`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Geschenkartikel GmbH as an organization.

**Content:**
```
\bGeschenkartikel GmbH\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `AMS`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the Austrian Public Employment Service (AMS).

**Content:**
```
\bAMS\b
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
Matches the Federal Office for Social Affairs and Disabled Persons in nominative and genitive forms.

**Content:**
```
\bBundesamt(?:s)?\s+für\s+Soziales\s+und\s+Behindertenwesen\b
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
Matches the specific law firm Mag. Ghesla Steuerberater GmbH.

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
Matches the Swiss Federal Invalidity Insurance, handling hyphenation.

**Content:**
```
\bEidgenössischen\s+Invalidenver-?sicherung\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Swiss Steueramt`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Swiss tax offices like 'Steueramtes des Kantons Luzern'.

**Content:**
```
\bSteueramtes\s+des\s+Kantons\s+[A-Z][a-zäöüÄÖÜß]+\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Swiss Kantonsspital`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches Swiss cantonal hospitals like 'Kantonsspitals St. Gallen'.

**Content:**
```
\bKantonsspitals\s+(?:St\.?\s+[A-Z][a-zäöüÄÖÜß]+|[A-Z][a-zäöüÄÖÜß]+)\b
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
Matches the specific tax office 'Steueramt des Kantons Luzern'.

**Content:**
```
\bSteueramt\s+des\s+Kantons\s+Luzern\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Finanzamt Braunau`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches 'Finanzamt Braunau Ried Schärding' and its abbreviation 'FA Braunau Ried Schärding'.

**Content:**
```
\b(?:FA\s+|Finanzamt\s+)Braunau\s+Ried\s+Schärding\b
```

<details>
<summary>📊 Detailed Metrics</summary>

| Precision | Recall | F1 | Total Predicted | TP | FP |
|---|---|---|---|---|---|
| 0.000 | 0.000 | 0.000 | 0 | 0 | 0 |

</details>

---

## `Schweizerische Unfallversicherung`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Matches the full name 'Schweizerischen Unfallversicherungsanstalt (SUVA)'.

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

## `Raiffeisenbank Locations`

**F1:** 0.000 | **Precision:** 0.000 | **Recall:** 0.000  

**Format:** `regex`  
**Description:**
Captures Raiffeisenbank entities including the specific 'Bankstelle St.Stefan' location. Updated to handle the full location string correctly.

**Content:**
```
\bRaiffeisenbank\s+Karnische\s+Rion\s+Bankstelle\s+St\.Stefan\b
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

